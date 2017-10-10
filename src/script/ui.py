from tkinter import*

root=Tk()
root.title("PokerGame")
root.geometry("{0}x{1}+-7+0".format(
    root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background ='#22741C')

frame = Frame(root)

root.resizable(False, False)





# p : player 1~3 card (나 : player0)



p_1 = Frame(background='white', height=180, width=300)
p_1.grid(row=0, column=0 , padx=45, pady=20)

p_2 = Frame(background='white', height=180, width=300)
p_2.grid(row=0, column=2 , pady=10)

p_3 = Frame(background='white', height=180, width=300)
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

root.mainloop()