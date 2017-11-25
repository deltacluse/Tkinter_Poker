from tkinter import *
from time import gmtime, strftime
import PIL.Image
import PIL.ImageTk
import time
import play
import ai_algorism


class Poker:
    def __init__(self):
        self.turn = 1  # 몇 번째 턴인지
        self.fold_count = 0  # fold 수
        self.player = ['user', 'com1', 'com2', 'com3']
        self.order = 0  # 턴 순서
        self.is_turn_start = True  # 턴 시작인지

        # 베팅페이즈(플레이어객체생성)
        self.have_money = [100000000, 100000000, 100000000, 100000000]  # user, com1, com2, com3의 보유금
        self.betting = play.Betting(self, self.have_money)  # 배팅 객체 생성
        self.ai = ai_algorism.Ai(self)  # AI 객체 생성

        # 카드분배(3장씩)
        self.game = play.Game(self.player)  # 게임 객체 생성
        self.game.game_start()  # 게임 시작
        for _ in range(3):
            self.game.distribute(self.order)  # 카드 분배

        self.game.open(0, 0)  # 유저가 오픈할 카드 선택
        self.ai.open()  # AI가 오픈할 카드 선택
        self.order = self.game.ordering(2, 2 + self.turn)  # 오픈된 족보로 순서 결정

        # 화면 구성
        self.root = Tk()
        self.set_window()  # 창 설정
        self.create_widgets()  # 화면 구성
        self.ui_update()  # 보유금, 테이블 머니, user 카드 이미지, AI 카드 이미지 초기화
        self.next(self.order)  # 순서대로 진행
        self.root.mainloop()

    def set_window(self):

        # self.full_width = self.root.winfo_screenwidth() - 16  # 창 가로 길이 설정
        # self.full_height = self.root.winfo_screenheight() - 100  # 창 세로 길이 설정
        self.full_width = 1366
        self.full_height = 768

        self.set_height = {
            'self.frame_other': self.full_height * 0.4,  # AI UI 높이
            'self.frame_batting': self.full_height * 0.3,  # 테이블 UI 높이
            'self.frame_user': self.full_height * 0.3  # user UI 높이
        }

        self.root.title("PokerGame")  # 윈도우 이름
        self.root.geometry("{0}x{1}+0+20".format(self.full_width, self.full_height))  # 윈도우 크기
        self.root.configure(bg='#22741C')  # 윈도우 배경색
        self.root.resizable(False, False)  # 윈도우 크기 변경 불가

    def create_widgets(self):
        # OtherPlayer Frame
        self.frame_other = Frame(self.root, bg='#22741C', width=self.full_width, height=self.set_height['self.frame_other'])
        self.frame_other.place(x=0, y=0)
        # Batting Frame
        self.frame_batting = Frame(self.root, bg='#22741C', width=self.full_width, height=self.set_height['self.frame_batting'])
        self.frame_batting.place(x=0, y=self.set_height['self.frame_other'] - 15)
        # My Frame
        self.frame_user = Frame(self.root, bg='#22741C', width=self.full_width, height=self.set_height['self.frame_user'])
        self.frame_user.place(x=0, y=self.set_height['self.frame_other'] + self.set_height['self.frame_batting'] - 20)

        # Other Player Grid
        self.other_cell = []  # OtherPlayer Cell Group
        self.other_cell_sub = [[], [], []]  # OtherPlayer Cell Card, Batting, Money
        for i in range(3):
            player = Frame(self.frame_other, bg='#22741C')
            player.grid(row=0, column=i, padx=self.full_width * 0.4 / 6, pady=self.set_height['self.frame_other'] / 7 / 4)
            self.other_cell.append(player)
            for j in range(3):
                cell = Frame(player, bg='#22741C', width=self.full_width * 0.2)
                cell.grid(row=j, column=0, pady=self.set_height['self.frame_other'] / 7 / 4)
                self.other_cell_sub[i].append(cell)
            self.other_cell_sub[i][0].configure(height=self.set_height['self.frame_other'] * 3 / 7)

        # AI 보유금 UI
        self.text_other_money = []
        self.label_other_money = []
        for i in range(3):
            self.text_other_money.append(StringVar())
            self.text_other_money[i].set(self.have_money[i+1])
            cell = Label(self.other_cell_sub[i][1], bg='#9ee899', width=int(self.full_width * 0.02), height=2, textvariable=self.text_other_money[i], font=("FiraCode", 12), relief=SOLID, borderwidth=3)
            cell.pack()
            self.label_other_money.append(cell)

        # AI 배팅 UI
        self.text_other_betting = []
        self.label_other_betting = []
        for i in range(3):
            self.text_other_betting.append(StringVar())
            self.text_other_betting[i].set("-----")
            cell = Label(self.other_cell_sub[i][1], bg='#9ee899', width=int(self.full_width * 0.02), height=2, textvariable=self.text_other_betting[i], font=("FiraCode", 12), relief=SOLID, borderwidth=3)
            cell.pack()
            self.label_other_betting.append(cell)

        # AI 카드 UI
        self.img_ai_cards = [[], [], []]
        self.ai_card = [[], [], []]
        for i in range(3):
            for j in range(7):
                if 0 <= j <= 2:
                    self.img_ai_cards[i].append(PIL.Image.open("..\image\{0}.png".format(0)))
                else:
                    self.img_ai_cards[i].append(PIL.Image.open("..\image\{0}.png".format(self.game.hand[i+1][j])))
                self.img_ai_cards[i][j] = PIL.ImageTk.PhotoImage(self.img_ai_cards[i][j].resize((int(self.set_height['self.frame_other'] * 3 / 7 * 0.75), int(self.set_height['self.frame_other'] * 3 / 7))))
                card = Label(self.other_cell_sub[i][0], width=self.set_height['self.frame_other'] * 3 / 7 * 0.75, height=self.set_height['self.frame_other'] * 3 / 7, image=self.img_ai_cards[i][j], relief=SOLID)
                card.configure(image=self.img_ai_cards[i][j])
                card.place(x=j * (self.full_width * 0.2 / 9.5), y=0)
                self.ai_card[i].append(card)

        # Batting Grid
        self.text_batted_money = StringVar()
        self.batted_money = Label(self.frame_batting, bg='#9ee899', width=20, height=4, textvariable=self.text_batted_money, font=("FiraCode", 20), relief=SOLID, borderwidth=3)
        self.batted_money.pack(padx=self.full_width * 0.4, pady=self.set_height['self.frame_batting'] * 0.2)

        # My Grid
        self.frame_money = Frame(self.frame_user, bg='#22741C', width=self.full_width * 0.2, height=self.set_height['self.frame_user'])
        self.frame_money.grid(row=0, column=0)
        self.frame_card = Frame(self.frame_user, bg='#22741C', width=self.full_width * 0.6, height=self.set_height['self.frame_user'])
        self.frame_card.grid(row=0, column=1)
        self.frame_button = Frame(self.frame_user, bg='#22741C', width=self.full_width * 0.2, height=self.set_height['self.frame_user'])
        self.frame_button.grid(row=0, column=2)

        # user 보유금 UI
        self.text_batting_money = StringVar()
        self.batted_money = Label(self.frame_money, bg='#9ee899', width=int(self.full_width / 7 * 0.08), height=int(self.set_height['self.frame_user'] / 16 * 0.4), textvariable=self.text_batting_money, font=("FiraCode", 20), relief=SOLID, borderwidth=3)
        self.batted_money.pack(padx=10, pady=self.set_height['self.frame_user'] * 0.2)

        # user 카드 UI
        self.img_user_cards = []
        self.user_card = []
        for i in range(7):
            self.img_user_cards.append(PIL.Image.open("..\image\{0}.png".format(self.game.hand[0][i])))
            self.img_user_cards[i] = PIL.ImageTk.PhotoImage(self.img_user_cards[i].resize((int(self.set_height['self.frame_user'] * 0.75 * 0.8), int(self.set_height['self.frame_user'] * 0.8))))
            card = Label(self.frame_card, width=self.set_height['self.frame_user'] * 0.75 * 0.8, height=self.set_height['self.frame_user'] * 0.8, image=self.img_user_cards[i], relief=SOLID)
            card.configure(image=self.img_user_cards[i])
            card.place(x=i * (self.full_width * 0.6 / 8) + (self.full_width * 0.3 * 0.25 - self.set_height['self.frame_user'] * 0.75 * 0.4) - 10, y=self.set_height['self.frame_user'] * 0.1)
            self.user_card.append(card)

        # user 배팅 UI
        self.buttons = []
        button_1 = Button(self.frame_button, text="1.5 raise", command=lambda: self.raise_(1.5))
        button_1.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_1.grid(row=0, column=0, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_1)
        button_2 = Button(self.frame_button, text="2 raise", command=lambda: self.raise_(2))
        button_2.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_2.grid(row=1, column=0, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_2)
        button_3 = Button(self.frame_button, text="4 raise", command=lambda: self.raise_(4))
        button_3.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_3.grid(row=2, column=0, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_3)
        button_4 = Button(self.frame_button, text="check", command=lambda: self.check(), state='disabled')
        button_4.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_4.grid(row=0, column=1, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_4)
        button_5 = Button(self.frame_button, text="call", command=lambda: self.call())
        button_5.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_5.grid(row=1, column=1, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_5)
        button_6 = Button(self.frame_button, text="fold", command=lambda: (self.game.fold('user'), self.fold()))
        button_6.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_6.grid(row=2, column=1, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_6)

    # 전체 UI 업데이트
    def ui_update(self):
        self.text_update()  # 텍스트 업데이트
        self.root.update()  # tkinter 업데이트
        self.user_image_update()  # user 카드 이미지 업데이트
        self.ai_image_update()  # AI 카드 이미지 업데이트

    # 텍스트 업데이트
    def text_update(self):
        for i in range(3):
            self.text_other_money[i].set(self.have_money[i+1])  # AI 보유금 업데이트
        self.text_batted_money.set(self.betting.table_money)  # 테이블 머니 업데이트
        self.text_batting_money.set(self.have_money[0])  # user 보유금 업데이트

    # user 카드 이미지 업데이트
    def user_image_update(self):
        for i in range(7):
            self.img_user_cards[i] = PIL.Image.open("..\image\{0}.png".format(self.game.hand[0][i]))
            self.img_user_cards[i] = PIL.ImageTk.PhotoImage(self.img_user_cards[i].resize((int(self.set_height['self.frame_user'] * 0.75 * 0.8), int(self.set_height['self.frame_user'] * 0.8))))
            self.user_card[i].configure(image=self.img_user_cards[i])

    # AI 카드 이미지 업데이트
    def ai_image_update(self):
        for i in range(3):
            for j in range(2, 6):
                self.img_ai_cards[i][j] = (PIL.Image.open("..\image\{0}.png".format(self.game.hand[i+1][j])))
                self.img_ai_cards[i][j] = PIL.ImageTk.PhotoImage(self.img_ai_cards[i][j].resize((int(self.set_height['self.frame_other'] * 3 / 7 * 0.75), int(self.set_height['self.frame_other'] * 3 / 7))))
                self.ai_card[i][j].configure(image=self.img_ai_cards[i][j])

    # 턴이 끝났는지 체크 / 게임이 끝났는지 체크
    def turn_check(self):
        print("call count : " + format(self.betting.call_count))
        if self.betting.call_count == (3 - self.fold_count):
            self.turn += 1
            if self.turn == 6:
                self.game_finish()
            else:
                self.next_turn()
            return True  # 턴이 넘어감
        return False  # 턴이 안 넘어감

    # 다음 턴 시작
    def next_turn(self):
        time.sleep(1)  # 1초 대기
        for i in range(3):
            self.text_other_betting[i].set("-----")  # AI 배팅 UI 초기화
        self.is_turn_start = True  # 턴 시작 True
        print("\nTurn : " + format(self.turn))
        self.betting.next_turn()  # 배팅 객체 - 다음 턴 시작
        self.order = self.game.ordering(2, 2 + self.turn)  # 오픈된 족보로 순서 결정
        self.game.distribute(self.order)  # 순서대로 카드분배(1장씩)
        self.next(self.order)  # 순서대로 진행

    # 순서대로 진행
    def next(self, index):  # index : 시작 순서
        self.ui_update()  # 전체 UI 업데이트
        if 1 <= index <= 3:  # AI 순서
            self.change_button_state('disabled')  # user 배팅 버튼 전체 비활성화
            self.buttons[3].configure(state='disabled')  # user 체크 버튼 비활성화
            self.ai.ai_turn(index)  # AI 객체 - AI 순서 시작
            self.change_button_state('normal')  # user 배팅 버튼 전체 활성화
        elif index == 0 and self.is_turn_start:  # user 순서이고 턴의 첫 순서면
            self.buttons[3].configure(state='normal')  # user 체크 버튼 활성화
            self.buttons[4].configure(state='disabled')  # user 콜 버튼 비활성화

    # user 레이즈
    def raise_(self, times):  # times : 레이즈 배수
        print("Index : 0\n%s raise" % times)
        self.betting.raise_(0, times)  # 배수만큼 레이즈
        self.is_turn_start = False  # 턴 시작 False
        self.next(1)  # 다음 순서 시작

    # user 레이즈
    def check(self):
        print("Index : 0\ncheck")
        self.is_turn_start = False  # 턴 시작 False
        self.next(1)  # 다음 순서 시작

    # user 콜
    def call(self):
        print("Index : 0\ncall")
        self.betting.call(0)  # 배팅 객체 - 콜
        self.is_turn_start = False  # 턴 시작 False
        if not self.turn_check():  # 턴이 끝나지 않았으면
            self.next(1)  # 다음 순서 시작

    # user fold
    def fold(self):
        self.change_button_state('disabled')  # user 배팅 버튼 전체 비활성화
        # Ai 작동 시작
        while self.turn < 6:  # 게임 종료까지
            self.ai.ai_turn(1)  # AI 객체 - AI 순서 시작
        # Ai 작동 종료

    # 게임 종료
    def game_finish(self):
        for i in range(3):  # AI 카드 공개
            for j in range(7):
                self.img_ai_cards[i][j] = (PIL.Image.open("..\image\{0}.png".format(self.game.hand[i+1][j])))
                self.img_ai_cards[i][j] = PIL.ImageTk.PhotoImage(self.img_ai_cards[i][j].resize((int(self.set_height['self.frame_other'] * 3 / 7 * 0.75), int(self.set_height['self.frame_other'] * 3 / 7))))
                self.ai_card[i][j].configure(image=self.img_ai_cards[i][j])
        self.change_button_state('disabled')  # user 배팅 버튼 전체 비활성화

        self.order = self.game.ordering(0, 2 + self.turn)  # 전체 패로 1등 결정
        print("< Game Over >")
        print("Winner : " + format(self.player[self.order]))

    # user 배팅 버튼 상태 변경
    def change_button_state(self, state):
        if state == 'normal':
            for i in range(6):
                if i != 3:
                    self.buttons[i].configure(state='normal')
        elif state == 'disabled':
            for i in range(6):
                self.buttons[i].configure(state='disabled')


print("----------Game Log----------")
print(time.ctime())
print("\n< Game Start >\n")
print("Turn : 1")

start = Poker()  # Poker 객체 생성
