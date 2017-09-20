#-*- coding: utf-8 -*-
#되도록 혼자 해보고 싶지만 어떻게 해야될지 모르겠으니 마구잡이로 시작합니다.

class batting:
    def __init__(self, firstmoney, hvmoney, tablemoney, btmoney, user):
        self.firstmoney = firstmoney
        self.btmoney = 10000
        self.hvmoney = firstmoney - btmoney
        self.self.tablemoney = self.tablemoney
        self.turn = 0

    #raise
    def raiz(self, hvmoney, beformon, btmoney, times, raizcount, callcount):
        if hvmoney>=beformon:
            btmoney = (beformon + btmoney * (times-1))
            hvmoney = hvmoney - (btmoney * (times-1))

            self.tablemoney += btmoney
            raizcount = 1
            callcount = 0

        elif hvmoney<beformon:
            self.allin(beformon,hvmoney,self.tablemoney)


    # Call
    def Call(self, say, beformon, hvmoney, btmoney, turn, callcount, user, finishscen):
        if hvmoney>=beformon:

            btmoney = beformon
            hvmoney = hvmoney - btmoney

            self.tablemoney += btmoney
            raizcount = 0
            callcount +=1
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


    #fold
    def fold(btmoney, hvmoney, least, user):
        least.remove(user)


    #allin
    def allin(self):
        self.tablemoney = self.tablemoney + self.hvmoney
        btmoney = self.hvmoney
        hvmoney = 0
    
    
