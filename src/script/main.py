import play
import ui

order = 0 #턴 순서

#카드분배(3장씩)
deck = play.game(100)
deck.game_start()
for _ in range(3) :
    deck.deal(order)
print(deck.hand)

#오픈할 카드 선택
deck.open(0) #첫 번째 카드를 오픈
print(deck.hand)

#오픈된 족보로 순서 결정
order=deck.ordering()
print(deck.player[order])

#베팅페이즈(플레이어객체생성)
user = play.batting(100000)
com1 = play.batting(100000)
com2 = play.batting(100000)
com3 = play.batting(100000)
player = [user, com1, com2, com3]

while len(deck.hand[0]) < 6:
    deck.deal(order)    #순서대로 카드분배(1장씩)
    order=deck.ordering()   #오픈된 족보로 순서 결정
    #베팅 및 알고리즘 (순서대로 베팅)

deck.deal(order)
#여기서 베팅

#게임종료
