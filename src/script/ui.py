from tkinter import *

root=Tk()
FullWidth = root.winfo_screenwidth() - 16
FullHeight = root.winfo_screenheight() - 38
root.title("PokerGame")
root.geometry("{0}x{1}+0+0".format(FullWidth, FullHeight))
root.configure(background ='#22741C')

main = Frame(root)

root.resizable(False, False)

setHeight = {
    'otherFrame' : FullHeight * 0.4,
    'battingFrame' : FullHeight * 0.2,
    'myFrame' : FullHeight * 0.4
}
#OtherPlayer Frame
otherFrame = Frame(root, background='white', height=setHeight['otherFrame'], width=FullWidth)
otherFrame.place(x = 0, y = 0)
#Batting Frame
battingFrame = Frame(root, background = 'black', height=setHeight['battingFrame'], width=FullWidth)
battingFrame.place(x = 0, y = setHeight['otherFrame'])
#My Frame
myFrame = Frame(root, background = 'white', height=setHeight['myFrame'], width=FullWidth)
myFrame.place(x = 0, y = setHeight['otherFrame'] + setHeight['battingFrame'])

#Other Player Grid
#Card Grid = 3/7 (1)
#Coin, Batting Grid = 1/7 (1, 1)
#pady = 1/28 (8)
otherCell = [] #OtherPlayer Cell Group
otherCellSub = [[],[],[]] #OtherPlayer Cell Card, Batting, Money
for i in range(3):
    player = Frame(otherFrame, background = 'white')
    player.grid(row=0, column=i, padx = FullWidth*0.4/6, pady = setHeight['otherFrame']/7/4)
    otherCell.append(player)
    for j in range(3) :
        cell = Frame(player, background = 'red', height = setHeight['otherFrame']/7, width = FullWidth * 0.2)
        cell.grid(row = j, column = 0, pady =  setHeight['otherFrame']/7/4)
        otherCellSub[i].append(cell)
    otherCellSub[i][0].configure(height = setHeight['otherFrame']*3/7)

#myGrid
moneyFrame = Frame(myFrame, background = 'blue', height = setHeight['myFrame'], width = FullWidth * 0.2)
moneyFrame.grid(row = 0, column = 0)
CardFrame = Frame(myFrame, bg = 'white', height = setHeight['myFrame'], width = FullWidth * 0.6)
CardFrame.grid(row = 0, column = 1)
ButtonFrame = Frame(myFrame, bg = 'blue', height = setHeight['myFrame'], width = FullWidth * 0.2)
ButtonFrame.grid(row = 0, column = 2)

"""
#배팅 버튼이 올 자리

Button_1 = Button( text ="1.5 raise")
Button_1.config(height =3, width = 15 )
Button_1.grid(row = 4, column = 4 , padx=5, pady=5)
Button_2 = Button( text ="2 raise")
Button_2.config(height =3, width = 15 )
Button_2.grid(row = 5, column = 4  , padx=5, pady=5)
Button_3 = Button( text ="4 raise")
Button_3.config(height =3, width = 15 )
Button_3.grid(row = 6, column = 4  , padx=5, pady=5)
Button_4 = Button( text ="check")
Button_4.config(height =3, width = 15 )
Button_4.grid(row = 4, column = 5  , padx=5, pady=5)
Button_5 = Button( text ="call")
Button_5.config(height =3, width = 15 )
Button_5.grid(row = 5, column = 5  , padx=5, pady=5)
Button_6 =Button( text ="fold")
Button_6.config(height =3, width = 15 )
Button_6.grid(row = 6, column = 5  , padx=5, pady=5)
"""
root.mainloop()