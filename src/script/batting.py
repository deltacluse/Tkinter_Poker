#-*- coding: utf-8 -*-
tableMoney = 0
beforeMoney = 0

class batting:
    def __init__(self, hvMoney):
        self.hvMoney = hvMoney

    # raise
    def raiz(self, times):
        self.btMoney = tableMoney * (times - 1)
        if self.hvMoney < self.btMoney:
            self.btMoney = self.hvMoney
        beforeMoney = self.btMoney
        tableMoney += self.btMoney

    # Call
    def call(self):
        if self.hvMoney >= beformon:
            self.btMoney = beformon
        else:
            self.btMoney = self.hvMoney
        self.hvMoney -= self.btMoney
        tableMoney += btMoney


# 돈 계산할 때 냈던 금액 제외하고 내기