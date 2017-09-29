#-*- coding: utf-8 -*-
class batting:
    def __init__(self, hvMoney):  # 게임 시작할 때 각 플레이어 객체 생성, hvMoney는 보유금
        self.hvMoney = hvMoney  # 보유금 넣기
        self.bfMoney = 0  # 이번 턴에 낸 돈 누적
        self.play = True  # 추가 플레이 가능(올인이면 불가능)

    # raise
    def raiz(self, times):  # 레이즈, times는 몇 배 레이즈인지

        global tableMoney
        global beforeMoney

        self.btMoney = tableMoney * (times - 1)  # 내야할 돈은 판돈 * (배수 - 1)
        if self.hvMoney < (self.btMoney-self.bfMoney):  # 낼 돈이 없으면
            self.btMoney = self.hvMoney  # 올인
            self.hvMoney = 0  # 올인
            self.play = False  # 추가 플레이 불가능
        else:  # 낼 돈이 있으면
            self.hvMoney -= (self.btMoney - self.bfMoney)  # 더 내야할 돈만 내기 (이번 턴에 낸 돈 누적을 빼줌)
            self.bfMoney += self.btMoney  # 이번 턴 돈 누적
        beforeMoney = self.btMoney  # 다음 사람이 낼 금액
        tableMoney += self.btMoney  # 테이블 머니에 낸 돈 추가

    # Call
    def call(self):

        global tableMoney
        global beforeMoney

        self.btMoney = beforeMoney  # 내야할 돈은 전 사람이 낸 금액
        if self.hvMoney < (self.btMoney - self.bfMoney):  # 낼 돈이 없으면
            self.btMoney = self.hvMoney  # 올인
            self.hvMoney = 0  # 올인
            self.play = False  # 추가 플레이 불가능
        else:  # 낼 돈이 있으면
            self.hvMoney -= (self.btMoney - self.bfMoney)  # 더 내야할 돈만 내기 (이번 턴에 낸 돈 누적을 빼줌)
            self.bfMoney += self.btMoney  # 이번 턴 돈 누적
        tableMoney += self.btMoney  # 테이블 머니에 낸 돈 추가


# 테스트

tableMoney = 10000

Kim = batting(100000)
Ai1 = batting(100000)
Ai2 = batting(100000)
Ai3 = batting(100000)

Kim.raiz(1.5)
print("Kim", Kim.hvMoney, beforeMoney, tableMoney)
Ai1.call()
print("Ai1", Ai1.hvMoney, beforeMoney, tableMoney)
Ai2.raiz(2)
print("Ai2", Ai2.hvMoney, beforeMoney, tableMoney)
Ai3.call()
print("Ai3", Ai3.hvMoney, beforeMoney, tableMoney)
Kim.call()
print("Kim", Kim.hvMoney, beforeMoney, tableMoney)
Ai1.call()
print("Ai1", Ai1.hvMoney, beforeMoney, tableMoney)