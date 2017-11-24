import random
import time


class Ai:
    def __init__(self, parent):  # 부모로 main.py의 Poker 클래스 객체 a를 받아옴
        self.parent = parent

    def ai_turn(self, index):  # 버튼 클릭하면 user 차례 끝나고 실행되는 ai 진행
        for i in range(index, 4):
            self.parent.other_cell[i-1].configure(bg='#fffb0f')
            self.parent.root.update()
            time.sleep(1)
            self.parent.other_cell[i-1].configure(bg='#22741C')
            if self.betting(i):
                break

    def betting(self, index):  # 각 ai가 실행하는 코드
        print("index : " + format(index))
        temp = random.randrange(0, 4)  # 0, 1 중 하나 랜덤
        if self.parent.is_turn_start:
            if temp > 0:
                self.parent.text_other_betting[index-1].set("raise")
                self.parent.betting.raise_(index, 1.5)
            elif temp == 0:
                self.parent.text_other_betting[index-1].set("check")
                self.parent.is_turn_start = False
        else:
            if temp == 0:
                self.parent.text_other_betting[index-1].set("raise")
                self.parent.betting.raise_(index, 1.5)
            elif temp > 0:
                self.parent.text_other_betting[index-1].set("call")
                self.parent.betting.call(index)
        self.parent.ui_update()
        if self.parent.turn_check():  # 턴이 넘어감
            return True

    def open(self):
        self.parent.game.open(1, 0)
        self.parent.game.open(2, 0)
        self.parent.game.open(3, 0)
