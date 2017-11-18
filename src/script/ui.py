from tkinter import *
import PIL.Image
import PIL.ImageTk


class Poker():
    def __init__(self):
        self.root = Tk()
        self.set_window()  # 창 설정
        self.create_widgets()  # 화면 구성
        self.root.mainloop()

    def set_window(self):

        self.FullWidth = self.root.winfo_screenwidth() - 16
        self.FullHeight = self.root.winfo_screenheight() - 100

        self.setHeight = {
            'self.otherFrame': self.FullHeight * 0.4,
            'self.battingFrame': self.FullHeight * 0.3,
            'self.myFrame': self.FullHeight * 0.3
        }

        self.root.title("PokerGame")
        self.root.geometry("{0}x{1}+0+20".format(self.FullWidth, self.FullHeight))
        self.root.configure(bg='#22741C')
        self.root.resizable(False, False)

    def create_widgets(self):
        # OtherPlayer Frame
        self.otherFrame = Frame(self.root, bg='#22741C', width=self.FullWidth, height=self.setHeight['self.otherFrame'])
        self.otherFrame.place(x=0, y=0)
        # Batting Frame
        self.battingFrame = Frame(self.root, bg='#22741C', width=self.FullWidth, height=self.setHeight['self.battingFrame'])
        self.battingFrame.place(x=0, y=self.setHeight['self.otherFrame'])
        # My Frame
        self.myFrame = Frame(self.root, bg='#22741C', width=self.FullWidth, height=self.setHeight['self.myFrame'])
        self.myFrame.place(x=0, y=self.setHeight['self.otherFrame'] + self.setHeight['self.battingFrame'])

        # Other Player Grid
        self.otherCell = []  # OtherPlayer Cell Group
        self.otherCellSub = [[], [], []]  # OtherPlayer Cell Card, Batting, Money
        for i in range(3):
            player = Frame(self.otherFrame, bg='#22741C')
            player.grid(row=0, column=i, padx=self.FullWidth * 0.4 / 6, pady=self.setHeight['self.otherFrame'] / 7 / 4)
            self.otherCell.append(player)
            for j in range(3):
                cell = Frame(player, bg='red', width=self.FullWidth * 0.2, height=self.setHeight['self.otherFrame'] / 7)
                cell.grid(row=j, column=0, pady=self.setHeight['self.otherFrame'] / 7 / 4)
                self.otherCellSub[i].append(cell)
            self.otherCellSub[i][0].configure(height=self.setHeight['self.otherFrame'] * 3 / 7)

        # Batting Grid
        self.text_self.battedMoney = StringVar()
        self.battedMoney = Label(self.battingFrame, bg='red', width=int(self.FullWidth / 7 * 0.2), height=int(self.setHeight['self.battingFrame'] / 16 * 0.6), textvariable=self.text_self.battedMoney, fg='white')
        self.battedMoney.pack(padx=self.FullWidth * 0.4, pady=self.setHeight['self.battingFrame'] * 0.2)
        self.text_self.battedMoney.set("tablemoney")

        # My Grid
        self.moneyFrame = Frame(self.myFrame, bg='#22741C', width=self.FullWidth * 0.2, height=self.setHeight['self.myFrame'])
        self.moneyFrame.grid(row=0, column=0)
        self.CardFrame = Frame(self.myFrame, bg='#22741C', width=self.FullWidth * 0.6, height=self.setHeight['self.myFrame'])
        self.CardFrame.grid(row=0, column=1)
        self.ButtonFrame = Frame(self.myFrame, bg='#22741C', width=self.FullWidth * 0.2, height=self.setHeight['self.myFrame'])
        self.ButtonFrame.grid(row=0, column=2)

        # My Money Label
        self.text_battingMoney = StringVar()
        self.battedMoney = Label(self.moneyFrame, bg='red', width=int(self.FullWidth / 7 * 0.2), height=int(self.setHeight['self.myFrame'] / 16 * 0.6), textvariable=self.text_battingMoney, fg='white')
        self.battedMoney.pack(pady=self.setHeight['self.myFrame'] * 0.2)
        self.text_battingMoney.set("mymoney")

        # My Cards
        Img_battedMoney = []
        for i in range(7):
            Img_battedMoney.append(PIL.Image.open("..\image\D{0}.png".format(i + 1)))
            Img_battedMoney[i] = PIL.ImageTk.PhotoImage(Img_battedMoney[i].resize((int(self.setHeight['self.myFrame'] * 0.75 * 0.8), int(self.setHeight['self.myFrame'] * 0.8))))
            card = Label(self.CardFrame, bg='white', width=self.setHeight['self.myFrame'] * 0.75 * 0.8, height=self.setHeight['self.myFrame'] * 0.8, image=Img_battedMoney[i], relief=SOLID)
            card.place(x=i * (self.FullWidth * 0.6 / 8) + (self.FullWidth * 0.3 * 0.25 - self.setHeight['self.myFrame'] * 0.75 * 0.4), y=self.setHeight['self.myFrame'] * 0.1)

        # Batting Button
        Button_1 = Button(self.ButtonFrame, text="1.5 raise")
        Button_1.config(height=int(self.setHeight['self.myFrame'] / 16 * 0.3), width=int(self.FullWidth / 7 * 0.2 * 0.4))
        Button_1.grid(row=0, column=0, padx=self.FullWidth * 0.2 * 0.04, pady=self.setHeight['self.myFrame'] * 0.02)
        Button_2 = Button(self.ButtonFrame, text="2 raise")
        Button_2.config(height=int(self.setHeight['self.myFrame'] / 16 * 0.3), width=int(self.FullWidth / 7 * 0.2 * 0.4))
        Button_2.grid(row=1, column=0, padx=self.FullWidth * 0.2 * 0.04, pady=self.setHeight['self.myFrame'] * 0.02)
        Button_3 = Button(self.ButtonFrame, text="4 raise")
        Button_3.config(height=int(self.setHeight['self.myFrame'] / 16 * 0.3), width=int(self.FullWidth / 7 * 0.2 * 0.4))
        Button_3.grid(row=2, column=0, padx=self.FullWidth * 0.2 * 0.04, pady=self.setHeight['self.myFrame'] * 0.02)
        Button_4 = Button(self.ButtonFrame, text="check")
        Button_4.config(height=int(self.setHeight['self.myFrame'] / 16 * 0.3), width=int(self.FullWidth / 7 * 0.2 * 0.4))
        Button_4.grid(row=0, column=1, padx=self.FullWidth * 0.2 * 0.04, pady=self.setHeight['self.myFrame'] * 0.02)
        Button_5 = Button(self.ButtonFrame, text="call")
        Button_5.config(height=int(self.setHeight['self.myFrame'] / 16 * 0.3), width=int(self.FullWidth / 7 * 0.2 * 0.4))
        Button_5.grid(row=1, column=1, padx=self.FullWidth * 0.2 * 0.04, pady=self.setHeight['self.myFrame'] * 0.02)
        Button_6 = Button(self.ButtonFrame, text="fold")
        Button_6.config(height=int(self.setHeight['self.myFrame'] / 16 * 0.3), width=int(self.FullWidth / 7 * 0.2 * 0.4))
        Button_6.grid(row=2, column=1, padx=self.FullWidth * 0.2 * 0.04, pady=self.setHeight['self.myFrame'] * 0.02)
