from tkinter import *

root=Tk()
FullWidth = root.winfo_screenwidth()
FullHeight = root.winfo_screenheight()
root.title("PokerGame")
root.geometry("{0}x{1}+-7+0".format(FullWidth, FullHeight))
root.configure(background ='#22741C')

main = Frame(root)

root.resizable(False, False)

setHeight = {
    'otherFrame' : 310,
    'battingFrame' : 200,
    'myFrame' : 200
}
setWidth = {
    'otherFrame': 200,
    'battingFrame': 200,
    'myFrame': 200
}


otherFrame = Frame(root, background='white', height=setHeight['otherFrame'], width=setWidth['otherFrame'])
otherFrame.place(x = 0, y = 0)
battingFrame = Frame(root, background = 'black', height=setHeight['battingFrame'], width=setWidth['battingFrame'])
battingFrame.place(x = 0, y = setHeight['otherFrame'])
myFrame = Frame(root, background = 'white', height=setHeight['myFrame'], width=setWidth['myFrame'])
myFrame.place(x = 0, y = setHeight['otherFrame'] + setHeight['battingFrame'])

#Other Player Grid
otherPlayer = []
otherPlayerSub = [[],[],[]]
for i in range(3):
    player = Frame(otherFrame, background = 'white')
    player.grid(row=0, column=i, padx = FullWidth*0.4/6, pady = 15)
    otherPlayer.append(player)
    for j in range(3) :
        cell = Frame(player, background = 'red', height = 50, width = FullWidth * 0.2)
        cell.grid(row = j, column = 0, pady = 5)
        otherPlayerSub[i].append(cell)
    otherPlayerSub[i][0].configure(height = 150)

#Batting Grid
"""
# p : player 1~3 card (나 : player0)

p_1 = Frame(otherFrame, background='white', height=180, width=300)
p_1.grid(row=0, column=0 , padx=45, pady=20)

p_2 = Frame(otherFrame, background='white', height=180, width=300)
p_2.grid(row=0, column=2 , pady=10)

p_3 = Frame(otherFrame, background='white', height=180, width=300)
p_3.grid(row=0, column=4, columnspan = 2 , pady=10)

# money(소지금)
m_1 = Frame(background = 'white', height=50, width=300)
m_1.grid(row=1, column=0 , pady=10)

m_2 = Frame(background = 'white', height=50, width=300)
m_2.grid(row=1, column=2, pady=10)

m_3 = Frame(background = 'white', height=50, width=300)
m_3.grid(row=1, column=4, columnspan = 2 , pady=20)

# personal beting (배팅)
b_1 = Frame(background = 'white', height=50, width=300)
b_1.grid(row=2, column=0, padx=10, pady=10)

b_2 = Frame(background = 'white', height=50, width=300)
b_2.grid(row=2, column=2, padx=10, pady=10)

b_3 = Frame(background = 'white', height=50, width=300)
b_3.grid(row=2, column=4, columnspan = 2 , padx=10, pady=10)


# bet(판돈)

Bet2 = Frame(background = 'white', height=210, width=750)
Bet2.grid(row=3, column=1, columnspan = 3, padx=10,  pady=10)

# 내 소지금
m_0 = Frame(background = 'white', height=150, width=280)
m_0.grid(row=4, column=0, rowspan = 3 , padx=10, pady=10)

# 내 카드
p_0 = Frame(background = 'white', height = 170, width = 500)
p_0.grid(row=4, column=1, rowspan = 3, columnspan = 3 , padx=10, pady=10)


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