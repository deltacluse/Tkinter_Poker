from tkinter import *
import PIL.Image
import PIL.ImageTk
import play
import ai_algorism


class Poker:
    def __init__(self):
        self.playing()

        self.root = Tk()
        self.set_window()  # 창 설정
        self.create_widgets()  # 화면 구성
        self.root.mainloop()

    def set_window(self):

        # self.full_width = self.root.winfo_screenwidth() - 16
        # self.full_height = self.root.winfo_screenheight() - 100
        self.full_width = 1366
        self.full_height = 768

        self.set_height = {
            'self.frame_other': self.full_height * 0.4,
            'self.frame_batting': self.full_height * 0.3,
            'self.frame_user': self.full_height * 0.3
        }

        self.root.title("PokerGame")
        self.root.geometry("{0}x{1}+0+20".format(self.full_width, self.full_height))
        self.root.configure(bg='#22741C')
        self.root.resizable(False, False)

    def create_widgets(self):
        # OtherPlayer Frame
        self.frame_other = Frame(self.root, bg='#22741C', width=self.full_width, height=self.set_height['self.frame_other'])
        self.frame_other.place(x=0, y=0)
        # Batting Frame
        self.frame_batting = Frame(self.root, bg='#22741C', width=self.full_width, height=self.set_height['self.frame_batting'])
        self.frame_batting.place(x=0, y=self.set_height['self.frame_other'])
        # My Frame
        self.frame_user = Frame(self.root, bg='#22741C', width=self.full_width, height=self.set_height['self.frame_user'])
        self.frame_user.place(x=0, y=self.set_height['self.frame_other'] + self.set_height['self.frame_batting'])

        # Other Player Grid
        self.other_cell = []  # OtherPlayer Cell Group
        self.other_cell_sub = [[], [], []]  # OtherPlayer Cell Card, Batting, Money
        for i in range(3):
            player = Frame(self.frame_other, bg='#22741C')
            player.grid(row=0, column=i, padx=self.full_width * 0.4 / 6, pady=self.set_height['self.frame_other'] / 7 / 4)
            self.other_cell.append(player)
            for j in range(3):
                cell = Frame(player, bg='red', width=self.full_width * 0.2, height=self.set_height['self.frame_other'] / 7)
                cell.grid(row=j, column=0, pady=self.set_height['self.frame_other'] / 7 / 4)
                self.other_cell_sub[i].append(cell)
            self.other_cell_sub[i][0].configure(height=self.set_height['self.frame_other'] * 3 / 7)

        # Ai cards
        self.img_ai_cards = [[], [], []]
        self.ai_card = [[], [], []]
        for i in range(3):
            for j in range(7):
                self.img_ai_cards[i].append(PIL.Image.open("..\image\{0}.png".format(self.game.hand[i][j])))
                self.img_ai_cards[i][j] = PIL.ImageTk.PhotoImage(self.img_ai_cards[i][j].resize((int(self.set_height['self.frame_other'] * 3 / 7 * 0.75), int(self.set_height['self.frame_other'] * 3 / 7))))
                card = Label(self.other_cell_sub[i][0], width=self.set_height['self.frame_other'] * 3 / 7 * 0.75, height=self.set_height['self.frame_other'] * 3 / 7, image=self.img_ai_cards[i][j], relief=SOLID)
                card.configure(image=self.img_ai_cards[i][j])
                card.place(x=i * (self.full_width * 0.2 - self.set_height['self.frame_other'] * 3 / 7 * 0.75), y=0)
                self.ai_card[i].append(card)

        # Batting Grid
        self.text_batted_money = StringVar()
        self.batted_money = Label(self.frame_batting, bg='red', width=int(self.full_width / 7 * 0.2), height=int(self.set_height['self.frame_batting'] / 16 * 0.6), textvariable=self.text_batted_money, fg='white')
        self.batted_money.pack(padx=self.full_width * 0.4, pady=self.set_height['self.frame_batting'] * 0.2)
        self.text_batted_money.set("tablemoney")

        # My Grid
        self.frame_money = Frame(self.frame_user, bg='#22741C', width=self.full_width * 0.2, height=self.set_height['self.frame_user'])
        self.frame_money.grid(row=0, column=0)
        self.frame_card = Frame(self.frame_user, bg='#22741C', width=self.full_width * 0.6, height=self.set_height['self.frame_user'])
        self.frame_card.grid(row=0, column=1)
        self.frame_button = Frame(self.frame_user, bg='#22741C', width=self.full_width * 0.2, height=self.set_height['self.frame_user'])
        self.frame_button.grid(row=0, column=2)

        # My Money Label
        self.text_batting_money = StringVar()
        self.batted_money = Label(self.frame_money, bg='red', width=int(self.full_width / 7 * 0.2), height=int(self.set_height['self.frame_user'] / 16 * 0.6), textvariable=self.text_batting_money, fg='white')
        self.batted_money.pack(pady=self.set_height['self.frame_user'] * 0.2)
        self.text_batting_money.set("mymoney")

        # User cards
        self.img_user_cards = []
        self.user_card = []
        for i in range(7):
            self.img_user_cards.append(PIL.Image.open("..\image\{0}.png".format(self.game.hand[0][i])))
            self.img_user_cards[i] = PIL.ImageTk.PhotoImage(self.img_user_cards[i].resize((int(self.set_height['self.frame_user'] * 0.75 * 0.8), int(self.set_height['self.frame_user'] * 0.8))))
            card = Label(self.frame_card, width=self.set_height['self.frame_user'] * 0.75 * 0.8, height=self.set_height['self.frame_user'] * 0.8, image=self.img_user_cards[i], relief=SOLID)
            card.configure(image=self.img_user_cards[i])
            card.place(x=i * (self.full_width * 0.6 / 8) + (self.full_width * 0.3 * 0.25 - self.set_height['self.frame_user'] * 0.75 * 0.4), y=self.set_height['self.frame_user'] * 0.1)
            self.user_card.append(card)

        # Batting Button
        self.buttons = []
        button_1 = Button(self.frame_button, text="1.5 raise", command=lambda: (self.betting.raise_(0, 1.5), self.next()))
        button_1.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_1.grid(row=0, column=0, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_1)
        button_2 = Button(self.frame_button, text="2 raise", command=lambda: (self.betting.raise_(0, 2), self.next()))
        button_2.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_2.grid(row=1, column=0, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_2)
        button_3 = Button(self.frame_button, text="4 raise", command=lambda: (self.betting.raise_(0, 4), self.next()))
        button_3.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_3.grid(row=2, column=0, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_3)
        button_4 = Button(self.frame_button, text="check", command=lambda: self.next(), state='disabled')
        button_4.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_4.grid(row=0, column=1, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_4)
        button_5 = Button(self.frame_button, text="call", command=lambda: (self.betting.call(0), self.turn_check(), self.next()))
        button_5.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_5.grid(row=1, column=1, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_5)
        button_6 = Button(self.frame_button, text="fold", command=lambda: (self.game.fold('user'), self.fold()))
        button_6.config(width=int(self.full_width / 7 * 0.2 * 0.4), height=int(self.set_height['self.frame_user'] / 16 * 0.3))
        button_6.grid(row=2, column=1, padx=self.full_width * 0.2 * 0.04, pady=self.set_height['self.frame_user'] * 0.02)
        self.buttons.append(button_6)

    def ui_update(self, index):
        self.table_money_update()
        if index == 0:
            self.user_image_update()
        elif 1 <= index <= 3:
            self.ai_image_update(index)
        
    def table_money_update(self):
        self.text_batted_money.set(self.betting.table_money)

    def user_image_update(self):
        for i in range(7):
            self.img_user_cards[i] = PIL.Image.open("..\image\{0}.png".format(self.game.hand[0][i]))
            self.img_user_cards[i] = PIL.ImageTk.PhotoImage(self.img_user_cards[i].resize((int(self.set_height['self.frame_user'] * 0.75 * 0.8), int(self.set_height['self.frame_user'] * 0.8))))
            self.user_card[i].configure(image=self.img_user_cards[i])
            
    def ai_image_update(self, index):
        for j in range(7):
            self.img_ai_cards[index][j] = (PIL.Image.open("..\image\{0}.png".format(self.game.hand[index][j])))
            self.img_ai_cards[index][j] = PIL.ImageTk.PhotoImage(self.img_ai_cards[index][j].resize((int(self.set_height['self.frame_other'] * 3 / 7 * 0.75), int(self.set_height['self.frame_other'] * 3 / 7))))
            self.ai_card[index][j].configure(image=self.img_ai_cards[index][j])

    def playing(self):
        self.turn = 1
        self.player = ['user', 'com1', 'com2', 'com3']
        self.order = 0  # 턴 순서

        # 베팅페이즈(플레이어객체생성)
        self.have_money = [100000, 100000, 100000, 100000]
        self.betting = play.Betting(self.have_money)
        self.ai = ai_algorism.Ai(self)  # ai 객체 생성

        # 카드분배(3장씩)
        self.game = play.Game(self.player)
        self.game.game_start()
        for _ in range(3):
            self.game.distribute(self.order)

        self.game.open(0)  # 오픈할 카드 선택
        self.order = self.game.ordering()  # 오픈된 족보로 순서 결정

    def turn_check(self):
        if self.turn == 5:
            self.game_finish()
        elif self.betting.call_count == 3:
            self.next_turn()

    def change_button_state(self, state):
        for i in range(6):
            if i != 3:
                self.buttons[i].configure(state=format(state))

    def next_turn(self):
        self.betting.finish_turn()
        self.game.distribute(self.order)  # 순서대로 카드분배(1장씩)
        self.user_image_update()
        self.order = self.game.ordering()  # 오픈된 족보로 순서 결정
        self.turn += 1
        self.buttons[3].configure(state='normal')
        if self.turn == 5:
            self.change_button_state('disabled')

    def next(self):
        self.ui_update(0)
        self.change_button_state('disabled')
        # Ai 작동 시작
        self.ai.ai_turn()
        # Ai 작동 종료
        self.change_button_state('normal')

    def fold(self):
        self.change_button_state('disabled')
        # Ai 작동 시작

        # Ai 작동 종료

    def game_finish(self):
        pass


a = Poker()
