import random
import jk

#덱 셔플
class card :
	def __init__(self) :
		self.original_card = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13",
								"D01", "D02", "D03", "D04", "D05", "D06", "D07", "D08", "D09", "D10", "D11", "D12", "D13",
								"H01", "H02", "H03", "H04", "H05", "H06", "H07", "H08", "H09", "H10", "H11", "H12", "H13",
								"C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13"]
	
	#게임 시작
	def game_start(self) :
		playing_deck = self.original_card
		random.shuffle(playing_deck)
		return playing_deck
	
class gameStart :
	def __init__(self) :
		player = ["player", "computer1", "computer2", "computer3"]
		
	#순서 결정
	def order(self, winner) :
		if winner == 0 :
			return 0
		else :
			return winner
	
	#카드 처음 분배 
	def deal_first(self, idx) :
		for i in range(3) :
			for j in range(4) :
				playing_card[(idx + j) % 4].append(card_list[0])
				del card_list[0]
		return playing_card

	# 분배
	def deal(self, idx) :
		for i in range(len(playing_card)) :
			playing_card[(idx + j) % 4].append(card_list[0])
			del card_list[0]
		return playing_card
