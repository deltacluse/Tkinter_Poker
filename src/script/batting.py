#-*- coding: utf-8 -*-
#되도록 혼자 해보고 싶지만 어떻게 해야될지 모르겠으니 마구잡이로 시작합니다.

class batting:
    def __init__(self, hvmoney, btmoney):
        self.btmoney = btmoney
        self.hvmoney = hvmoney
        self.tablemoney = 0
        self.beformoney = 0
        self.turn = 1
        self.raizcount = 0
        self.callcount = 0

    # raise
    def raiz(self, time):
        btmoney = tablemoney * (time - 1)
        if hvmoney < btmoney:
            btmoney = hvmoney
        beformoney = btmoney
        tablemoney += btmoney
        raizcount = 1
        callcount = 0

    # Call
    def Call(self, say, beformon, hvmoney, btmoney, turn, callcount, user, finishscen):
        if hvmoney>=beformon:

            btmoney = beformon
            hvmoney = hvmoney - btmoney

            self.tablemoney += btmoney
            self.raizcount = 0
            self.callcount +=1
            self.theend(raizcount, callcount, user, finishscen)

        elif hvmoney<beformon:
            self.allin(beformon, hvmoney, self.tablemoney)

    #check
    def check(self, beformon, btmoney, hvmoney, turn):
        if hvmoney >=beformon and turn==1:
            btmoney = 0
            hvmoney = hvmoney - beformon
        elif turn !=1:
            pass

        elif hvmoney<beformon:
            self.allin()

    #end
    def theend(raiz, call, user, finishscen):
        if raiz == 1 and call == user:
            return finishscen

    #올인
    def allin(tablemoney, hymoney, btmoney):
        tablemoney = tablemoney + hvmoney
        btmoney = hvmoney
        hvmoney = 0