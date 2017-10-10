from play import *

order=0

#카드분배(3장씩)
deck=game(100)
deck.game_start()
print(deck.playing_deck)
deck.deal_first()
print(deck.hand)
print(deck.playing_deck)

#오픈할 카드 선택
deck.open(0) #첫번째 있는 카드를 오픈
print(deck.hand)
print(deck.playing_deck)

#오픈된 족보로 순서 결정
order=deck.ordering()

#베팅페이즈(플레이어객체생성)
user = batting(100000)
com1 = batting(100000)
com2 = batting(100000)
com3 = batting(100000)

while len(deck.hand[0]) < 6:
    deck.deal(order)    #순서대로 카드분배(1장씩)
    order=deck.ordering()   #오픈된 족보로 순서 결정
    #베팅 및 알고리즘 (순서대로 베팅)

deck.deal(order)
#여기서 베팅

#게임종료료