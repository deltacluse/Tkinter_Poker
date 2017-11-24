import random

class Ai:
    def __init__(self, parent):  # 부모로 main.py의 Poker 클래스 객체 a를 받아옴
        self.parent = parent

    def ai_turn(self, index):  # 버튼 클릭하면 user 차례 끝나고 실행되는 ai 진행
        for i in range(index, 4):
            if self.betting(i):
                break

    def betting(self, index):  # 각 ai가 실행하는 코드
        print("index : " + format(index))
        if self.parent.is_turn_start:
            print(format(index) + " / raise")
            self.parent.betting.raise_(index, 4)
        else:
            if random.random() % 2 == 1:
                print(format(index) + " / raise")
                self.parent.betting.raise_(index, 2)
            else:
                print(format(index) + " / call")
                self.parent.betting.call(index)
        self.parent.ui_update()
        if self.parent.turn_check():  # 턴이 넘어감
            return True

    def open(self):
        self.parent.game.open(1, 0)
        self.parent.game.open(2, 0)
        self.parent.game.open(3, 0)
