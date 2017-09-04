import random
import jk

#덱 셔플
card = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13",
        "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13",
        "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13",
        "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13"]

card_list = card
random.shuffle(card_list)

#player 순서 결정
player = ["player", "computer1", "computer2", "computer3"]

winner = "player"

while winner != player[0] :
    player.append(player[0])
    del player[0]

print(player)

#카드 분배
player_card = []
computer1_card = []
computer2_card = []
computer3_card = []

for i in range(4) :
    player_card.append(card_list[0])
    del card_list[0]
    computer1_card.append(card_list[0])
    del card_list[0]
    computer2_card.append(card_list[0])
    del card_list[0]
    computer3_card.append(card_list[0])
    del card_list[0]

# 카드 버리기
drop_card = [] #버릴 카드 넘겨받기
player_card.remove(drop_card[0])
computer1_card.remove(drop_card[1])
computer2_card.remove(drop_card[2])
computer3_card.remove(drop_card[3])