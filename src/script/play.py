import random
import jk

global tableMoney
global berforeMoney

tableMoney=1000
beforeMoney=tableMoney


#덱 셔플
class game :
    def __init__(self,tableMoney) :
        self.original_card = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13",
                                "D01", "D02", "D03", "D04", "D05", "D06", "D07", "D08", "D09", "D10", "D11", "D12", "D13",
                                "H01", "H02", "H03", "H04", "H05", "H06", "H07", "H08", "H09", "H10", "H11", "H12", "H13",
                                "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13"]
        self.hand=[[],[],[],[]]
        self.player = ["Player", "Computer1", "Computer2", "Computer3"]

    #게임 시작
    def game_start(self) :
        self.playing_deck = self.original_card
        random.shuffle(self.playing_deck)

    #순서 결정
    def ordering(self) :
        scores=[jk.check(i) for i in [self.hand[j] for j in range(4)]]
        scores=([i.getscore() for i in scores])
        print(scores)
        return scores.index(max(scores))

    # 분배
    def deal(self, order) :
        for hand in self.hand[order:]+self.hand[:order] :
            hand.append(self.playing_deck[0])
            del self.playing_deck[0]

    #오픈할 카드 선택
    def open(self,number):
        if number!=2:
            self.hand[0][2],self.hand[0][number]=self.hand[0][number],self.hand[0][2] #위치 변경

class batting:
    def __init__(self, hvMoney):  # 게임 시작할 때 각 플레이어 객체 생성, hvMoney는 보유금
        self.hvMoney = hvMoney  # 보유금 넣기
        self.bfMoney = 0  # 이번 턴에 낸 돈 누적
        self.play = True  # 추가 플레이 가능(올인이면 불가능)
        self.iscall = 0

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
        self.iscall=1

        self.btMoney = beforeMoney  # 내야할 돈은 전 사람이 낸 금액
        if self.hvMoney < (self.btMoney - self.bfMoney):  # 낼 돈이 없으면
            self.btMoney = self.hvMoney  # 올인
            self.hvMoney = 0  # 올인
            self.play = False  # 추가 플레이 불가능
        else:  # 낼 돈이 있으면
            self.hvMoney -= (self.btMoney - self.bfMoney)  # 더 내야할 돈만 내기 (이번 턴에 낸 돈 누적을 빼줌)
            self.bfMoney += self.btMoney  # 이번 턴 돈 누적
        tableMoney += self.btMoney  # 테이블 머니에 낸 돈 추가

    def fold(self,player):
        del self.hand[player]