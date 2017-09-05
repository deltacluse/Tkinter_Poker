import random
import jk

#덱 셔플
class card :
	def __init__(self) :
		self.original_card = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13",
								"D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13",
								"H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13",
								"C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13"]
	
	#게임 시작
	def game_start(self) :
		playing_deck = self.original_card
		random.shuffle(playing_deck)
		return playing_deck
	
class gameStart :
	def __init__(self) :
	
	#순서 결정
	def order(self, winner) :
		if winner == 0 :
			return 0
		else :
			return winner
	
	#카드 분배 
	def deal(self, idx) :
		for i in range(3) :
			for j in range(4) :
				playing_card[(idx + j) % 4].append(card_list[0])
				del card_list[0]
		return playing_card
	
#player 순서 결정
player = ["player", "computer1", "computer2", "computer3"]
