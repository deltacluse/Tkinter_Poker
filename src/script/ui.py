from tkinter import *
from PIL import Image

root=Tk()

FullWidth = root.winfo_screenwidth() - 16
FullHeight = root.winfo_screenheight() - 100

# FullWidth = 800
# FullHeight = 600

root.title("PokerGame")
root.geometry("{0}x{1}+0+20".format(FullWidth, FullHeight))
root.configure(background ='#22741C')
root.resizable(False, False)

setHeight = {
    'otherFrame' : FullHeight * 0.4,
    'battingFrame' : FullHeight * 0.3,
    'myFrame' : FullHeight * 0.3
}

#OtherPlayer Frame
otherFrame = Frame(root, background='#22741C', height=setHeight['otherFrame'], width=FullWidth)
otherFrame.place(x = 0, y = 0)
#Batting Frame
battingFrame = Frame(root, background = '#22741C', height=setHeight['battingFrame'], width=FullWidth)
battingFrame.place(x = 0, y = setHeight['otherFrame'])
#My Frame
myFrame = Frame(root, background = '#22741C', height=setHeight['myFrame'], width=FullWidth)
myFrame.place(x = 0, y = setHeight['otherFrame'] + setHeight['battingFrame'])

#Other Player Grid
#Card Grid = 3/7 (1)
#Coin, Batting Grid = 1/7 (1, 1)
#pady = 1/28 (8)
otherCell = [] #OtherPlayer Cell Group
otherCellSub = [[],[],[]] #OtherPlayer Cell Card, Batting, Money
for i in range(3):
    player = Frame(otherFrame, background = '#22741C')
    player.grid(row=0, column=i, padx = FullWidth*0.4/6, pady = setHeight['otherFrame']/7/4)
    otherCell.append(player)
    for j in range(3) :
        cell = Frame(player, background = 'red', height = setHeight['otherFrame']/7, width = FullWidth * 0.2)
        cell.grid(row = j, column = 0, pady =  setHeight['otherFrame']/7/4)
        otherCellSub[i].append(cell)
    otherCellSub[i][0].configure(height = setHeight['otherFrame']*3/7)

#Batting Grid
text_battedMoney = StringVar()
battedMoney = Label(battingFrame, background = 'red', height = int(setHeight['battingFrame'] / 16 * 0.6), width = int(FullWidth / 7 * 0.2), textvariable = text_battedMoney, foreground = 'white')
battedMoney.pack(padx = FullWidth * 0.4, pady = setHeight['battingFrame']*0.2)
text_battedMoney.set("tablemoney")

#My Grid
moneyFrame = Frame(myFrame, background = '#22741C', height = setHeight['myFrame'], width = FullWidth * 0.2)
moneyFrame.grid(row = 0, column = 0)
CardFrame = Frame(myFrame, background = '#22741C', height = setHeight['myFrame'], width = FullWidth * 0.6)
CardFrame.grid(row = 0, column = 1)
ButtonFrame = Frame(myFrame, background = '#22741C', height = setHeight['myFrame'], width = FullWidth * 0.2)
ButtonFrame.grid(row = 0, column = 2)

#My Money Label
text_battingMoney = StringVar()
battedMoney = Label(moneyFrame, background = 'red', height = int(setHeight['myFrame'] / 16 * 0.6), width = int(FullWidth / 7 * 0.2), textvariable = text_battingMoney, foreground = 'white')
battedMoney.pack(pady = setHeight['myFrame'] * 0.2)
text_battingMoney.set("mymoney")

#My Cards
img_battedMoney = []
for i in range(7):
    img_battedMoney.append(Image.open("..\image\c{0}.png".format(i+1)))
    img_battedMoney[i] = img_battedMoney[i].resize((int(setHeight['myFrame'] * 0.75), int(setHeight['myFrame'])))
    card = Label(CardFrame, background = 'white', height = setHeight['myFrame'] * 0.8, width = setHeight['myFrame'] * 0.75 * 0.8, image = img_battedMoney[i], relief = SOLID)
    card.place(x = i * (FullWidth * 0.6 / 8) + (FullWidth * 0.3 * 0.25 - setHeight['myFrame'] * 0.75 * 0.4), y = setHeight['myFrame'] * 0.1)

#My Cards
# img_battedMoney = []
# for i in range(7):
#     img_battedMoney.append(PhotoImage(file = "..\image\c{0}.png".format(i+1)).subsample(2,2))
#     img_battedMoney[i] = img_battedMoney[i].subsample(int(179 / setHeight['myFrame'] * 0.75), 251)
#     img_battedMoney[i] = img_battedMoney[i].zoom(int(setHeight['myFrame'] * 0.75), int(setHeight['myFrame']))
#     card = Label(CardFrame, background = 'white', height = setHeight['myFrame'] * 0.8, width = setHeight['myFrame'] * 0.75 * 0.8, image = img_battedMoney[i], relief = SOLID)
#     card.place(x = i * (FullWidth * 0.6 / 8) + (FullWidth * 0.3 * 0.25 - setHeight['myFrame'] * 0.75 * 0.4), y = setHeight['myFrame'] * 0.1)

#Batting Button
Button_1 = Button(ButtonFrame, text ="1.5 raise")
Button_1.config(height = int(setHeight['myFrame'] / 16 * 0.3), width = int(FullWidth / 7 * 0.2 * 0.4))
Button_1.grid(row = 0, column = 0, padx = FullWidth * 0.2 * 0.04, pady=setHeight['myFrame'] * 0.02)
Button_2 = Button(ButtonFrame, text ="2 raise")
Button_2.config(height = int(setHeight['myFrame'] / 16 * 0.3), width = int(FullWidth / 7 * 0.2 * 0.4))
Button_2.grid(row = 1, column = 0, padx = FullWidth * 0.2 * 0.04, pady=setHeight['myFrame'] * 0.02)
Button_3 = Button(ButtonFrame, text ="4 raise")
Button_3.config(height = int(setHeight['myFrame'] / 16 * 0.3), width = int(FullWidth / 7 * 0.2 * 0.4))
Button_3.grid(row = 2, column = 0, padx = FullWidth * 0.2 * 0.04, pady=setHeight['myFrame'] * 0.02)
Button_4 = Button(ButtonFrame, text ="check")
Button_4.config(height = int(setHeight['myFrame'] / 16 * 0.3), width = int(FullWidth / 7 * 0.2 * 0.4))
Button_4.grid(row = 0, column = 1, padx = FullWidth * 0.2 * 0.04, pady=setHeight['myFrame'] * 0.02)
Button_5 = Button(ButtonFrame, text ="call")
Button_5.config(height = int(setHeight['myFrame'] / 16 * 0.3), width = int(FullWidth / 7 * 0.2 * 0.4))
Button_5.grid(row = 1, column = 1, padx = FullWidth * 0.2 * 0.04, pady=setHeight['myFrame'] * 0.02)
Button_6 =Button(ButtonFrame, text ="fold")
Button_6.config(height = int(setHeight['myFrame'] / 16 * 0.3), width = int(FullWidth / 7 * 0.2 * 0.4))
Button_6.grid(row = 2, column = 1, padx = FullWidth * 0.2 * 0.04, pady=setHeight['myFrame'] * 0.02)

root.mainloop()