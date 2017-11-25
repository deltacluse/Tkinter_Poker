import random
import time


class Ai:
    def __init__(self, parent):  # 부모로 main.py의 Poker 클래스 객체 a를 받아옴
        self.parent = parent

    # AI 순서 시작
    def ai_turn(self, index):
        for i in range(index, 4):
            self.parent.other_cell[i-1].configure(bg='#fffb0f')
            self.parent.root.update()
            time.sleep(1)
            self.parent.other_cell[i-1].configure(bg='#22741C')
            if self.betting(i):
                break

    # AI 배팅
    def betting(self, index):  # index : 몇 번째 AI
        print("Index : " + format(index))
        temp = random.randrange(0, 4)  # 0 ~ 3 랜덤
        if self.parent.is_turn_start:  # 턴 첫 번째 순서라면
            if temp > 0:
                print("raise")
                self.parent.text_other_betting[index-1].set("raise")
                self.parent.betting.raise_(index, 1.5)
            elif temp == 0:
                print("check")
                self.parent.text_other_betting[index-1].set("check")
                self.parent.is_turn_start = False
        else:
            if temp == 0:
                print("raise")
                self.parent.text_other_betting[index-1].set("raise")
                self.parent.betting.raise_(index, 1.5)
            elif temp > 0:
                print("call")
                self.parent.text_other_betting[index-1].set("call")
                self.parent.betting.call(index)
        self.parent.ui_update()
        if self.parent.turn_check():  # 턴이 넘어감
            return True

    def open(self):
        self.parent.game.open(1, 0)  # AI 1 오픈
        self.parent.game.open(2, 0)  # AI 2 오픈
        self.parent.game.open(3, 0)  # AI 3 오픈
