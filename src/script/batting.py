#-*- coding: utf-8 -*-

class batting:
    def __init__(self, hvMoney):
        self.hvMoney = hvMoney
        self.update(0, 0)

    # raise
    def raiz(self, times):
        self.btMoney = self.tableMoney * (times - 1)
        if self.hvMoney < self.btMoney:
            self.btMoney = self.hvMoney
        self.beforeMoney = self.btMoney
        self.tableMoney += self.btMoney

    # Call
    def call(self, finishscen):
        if self.hvMoney >= self.beformon:
            self.btMoney = self.beformon
        else:
            self.btMoney = self.hvMoney
        self.hvMoney -= self.btMoney
        self.tableMoney += self.btMoney

    def update(self, beforeMoney, tableMoney):
        self.beforeMoney = beforeMoney
        self.tableMoney = tableMoney

turn = 0
raizCount = 0
callCount = 0

def turnCheck(playerList):
    if(raizCount == 1 and callCount == len(playerList)-1):
        turn += 1
        raizCount = 0
        callCount = 0




player = ['Kim', 'Ai1', 'Ai2', 'Ai3']