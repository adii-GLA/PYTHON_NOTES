# from tkinter import *
# root=Tk()
# mylabel=Label(root,text="hello world")
# mylabel.pack()
# root.mainloop()

#-----------------------------------------------------------------------------

# import tkinter as tk
# window = tk.Tk()
# window.title("My First Tkinter App")
# label = tk.Label(window, text="Hello, world!")
# label.pack()
# window.mainloop()

#-----------------------------------------------------------------------------

# from tkinter import *
# root = Tk()
# root.title("WELCOME TO THE SBI BANK")
# mylabel = Label(root, text="Hello, world!")
# mylabel2 = Label(root, text="welcome")
# mylabel.grid(row=0,column=0)
# mylabel2.grid(row=1,column=1)
# #label.pack()
# root.mainloop()

#-----------------------------------------------------------------------------

# from tkinter import *
# root = Tk()
# root.title("ATM")
# mybutton1=Button(root,text="0",padx=80,fg="black",bg="white")
# mybutton2=Button(root,text="1",padx=80,fg="black",bg="white")
# mybutton3=Button(root,text="2",padx=80,fg="black",bg="white")
# mybutton4=Button(root,text="3",padx=80,fg="black",bg="white")
# mybutton5=Button(root,text="4",padx=80,fg="black",bg="white")
# mybutton6=Button(root,text="5",padx=80,fg="black",bg="white")
# mybutton7=Button(root,text="6",padx=80,fg="black",bg="white")
# mybutton8=Button(root,text="7",padx=80,fg="black",bg="white")
# mybutton9=Button(root,text="8",padx=80,fg="black",bg="white")
# mybutton10=Button(root,text="9",padx=80,fg="black",bg="white")
# mybutton11=Button(root,text="Reset",padx=70,fg="black",bg="pink")
# mybutton12=Button(root,text="Change pin",padx=52,fg="black",bg="skyblue")
# mybutton13=Button(root,text="Reciept",padx=63,fg="black",bg="lightgreen")
# mybutton14=Button(root,text="Check balance",padx=45,fg="black",bg="lightyellow")
# mybutton15=Button(root,text="Exit",padx=74,fg="black",bg="red")
# mybutton1.grid(row=0,column=0)
# mybutton2.grid(row=0,column=1)
# mybutton3.grid(row=0,column=2)
# mybutton4.grid(row=1,column=0)
# mybutton5.grid(row=1,column=1)
# mybutton6.grid(row=1,column=2)
# mybutton7.grid(row=2,column=0)
# mybutton8.grid(row=2,column=1)
# mybutton9.grid(row=2,column=2)
# mybutton10.grid(row=3,column=0)
# mybutton11.grid(row=3,column=1)
# mybutton12.grid(row=3,column=2)
# mybutton13.grid(row=4,column=0)
# mybutton14.grid(row=4,column=1)
# mybutton15.grid(row=4,column=2)
# root.geometry("600x400")
# root.mainloop()

#------------------------------------------------------------------------------------

# from tkinter import *
# root = Tk()
# mytext1 = Entry(root, width=50)
# mytext2 = Entry(root, width=50)
# mytext3 = Entry(root, width=50)
# mytext1.pack()
# mytext2.pack()
# mytext3.pack()
# def mufunct1():
#     recieved_text = mytext1.get()
#     mylabel1 = Label(root, text=recieved_text)
#     mylabel1.pack()
# mybutton = Button(root, text='Submit1', command=mufunct1,padx=40, fg='black')
# mybutton.pack()
# def mufunct2():
#     recieved_text = mytext2.get()
#     mylabel1 = Label(root, text=recieved_text)
#     mylabel1.pack()
# mybutton = Button(root, text='Submit2', command=mufunct2,padx=40, fg='black')
# mybutton.pack()
# def mufunct3():
#     recieved_text = mytext3.get()
#     mylabel1 = Label(root, text=recieved_text)
#     mylabel1.pack()
# mybutton = Button(root, text='Submit3', command=mufunct3,padx=40, fg='black')4
# mybutton.pack()
# root.mainloop()

#------------------------------------------------------------------------------------------

# from tkinter import *
# root = Tk()
# root.geometry('500x200')
# root.minsize(200,200)
# root.maxsize(1000,800)

# cb1 = Checkbutton(root, text="Option 1")
# cb2 = Checkbutton(root, text="Option 2")
# cb3 = Checkbutton(root, text="Option 3")
# cb1.pack()
# cb2.pack()
# cb3.pack()
# root.mainloop()

#------------------------------------------------------------------------------------------

# from tkinter import *
# root = Tk()
# root.geometry('500x400')
# root.minsize(200,200)
# root.maxsize(1000,800)
# checkvar = IntVar()
# def show():
#     mylabel1 = Label(root, text=checkvar.get())
#     mylabel1.pack()
# cb1 = Checkbutton(root, text="Option 1", variable=checkvar)
# cb1.pack()
# mybutton = Button(root, text='Click', command=show)
# mybutton.pack()
# root.mainloop()

#------------------------------------------------------------------------------------

# Lambda Functions Examples
# Ex-1
# add = lambda x,y: x + y
# result = add(3,5)
# print(result)
# from tkinter import *
# root=Tk()
# def click(value):
#     print(f"Button click by user is {value}")
# btn1=Button(root,text="Button 1",command= lambda : click(1)).pack()
# btn2=Button(root,text="Button 1",command= lambda : click(2)).pack()
# btn3=Button(root,text="Button 1",command= lambda : click(3)).pack()
# btn4=Button(root,text="Button 1",command= lambda : click(4)).pack()
# root.mainloop()

#------------------------------------------------------------------------------------

# from tkinter import *
# root = Tk()
# root.geometry("600x500")
# root.title("Calculator")
# entry1 = Entry(root, width=50, border=10)
# entry1.grid(row=0, column=0, columnspan=3)
# button1 = Button(root, text="1", fg="Black", font=50, padx=40, pady=20)
# button2 = Button(root, text="2", fg="Black", font=50, padx=40, pady=20)
# button3 = Button(root, text="3", fg="Black", font=50, padx=40, pady=20)
# button4 = Button(root, text="4", fg="Black", font=50, padx=40, pady=20)
# button5 = Button(root, text="5", fg="Black", font=50, padx=40, pady=20)
# button6 = Button(root, text="6", fg="Black", font=50, padx=40, pady=20)
# button7 = Button(root, text="7", fg="Black", font=50, padx=40, pady=20)
# button8 = Button(root, text="8", fg="Black", font=50, padx=40, pady=20)
# button9 = Button(root, text="9", fg="Black", font=50, padx=40, pady=20)
# button0 = Button(root, text="0", fg="Black", font=50, padx=40, pady=20)
# button_add = Button(root, text="+", fg="Black", font=50, padx=40, pady=20)
# button_sub = Button(root, text="-", fg="Black", font=50, padx=42, pady=20)
# button_div = Button(root, text="/", fg="Black", font=50, padx=40, pady=20)
# button_mult = Button(root, text="*", fg="Black", font=50, padx=40, pady=20)
# button_equal = Button(root, text="=", fg="Black", font=50, padx=150, pady=20)
# button_clear = Button(root, text="Clr", fg="Black", font=50, padx=35, pady=20)
# button1.grid(row=1,column=0)
# button2.grid(row=1,column=1)
# button3.grid(row=1,column=2)
# button4.grid(row=2,column=0)
# button5.grid(row=2,column=1)
# button6.grid(row=2,column=2)
# button7.grid(row=3,column=0)
# button8.grid(row=3,column=1)
# button9.grid(row=3,column=2)
# button0.grid(row=4,column=0)
# button_add.grid(row=4, column=1)
# button_sub.grid(row=4, column=2)
# button_div.grid(row=5, column=0)
# button_mult.grid(row=5, column=1)
# button_clear.grid(row=5, column=2)
# button_equal.grid(row=6, column=0, columnspan=3)
# root.mainloop()

#-------------------------------------------------------------------------------------------

# from tkinter import *
# root = Tk()
# root.geometry("600x500")
# root.title("TIC-TAC-TOE")
# button1 = Button(root, fg="Black", font=50, padx=40, pady=20)
# button2 = Button(root, fg="Black", font=50, padx=40, pady=20)
# button3 = Button(root, fg="Black", font=50, padx=40, pady=20)
# button4 = Button(root, fg="Black", font=50, padx=40, pady=20)
# button5 = Button(root, fg="Black", font=50, padx=40, pady=20)
# button6 = Button(root, fg="Black", font=50, padx=40, pady=20)
# button7 = Button(root, fg="Black", font=50, padx=40, pady=20)
# button8 = Button(root, fg="Black", font=50, padx=40, pady=20)
# button9 = Button(root, fg="Black", font=50, padx=40, pady=20)
# button1.grid(row=1,column=0)
# button2.grid(row=1,column=1)
# button3.grid(row=1,column=2)
# button4.grid(row=2,column=0)
# button5.grid(row=2,column=1)
# button6.grid(row=2,column=2)
# button7.grid(row=3,column=0)
# button8.grid(row=3,column=1)
# button9.grid(row=3,column=2)
# root.mainloop()
# winner_pattern=[
#     [0,1,2],
#     [0,3,6],
#     [0,4,8],
#     [1,4,7],
#     [2,5,8],
#     [2,4,6],
#     [3,4,5],
#     [6,7,8]
# ];

#----------------------------------------------------------------------------------------------

# import tkinter as tk
# from tkinter import messagebox
# current_player = "X"
# def switch_player():
#     global current_player
#     if current_player == "X":
#         current_player = "O"
#     else:
#         current_player = "X"
# def check_winner():
#     # Check rows
#     for i in range(3):
#         if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
#             return buttons[i][0]["text"]
#     # Check columns
#     for i in range(3):
#         if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
#             return buttons[0][i]["text"]
#     # Check diagonals
#     if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
#         return buttons[0][0]["text"]
#     if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
#         return buttons[0][2]["text"]
#     return None
# def reset_game():
#     global current_player
#     current_player = "X"
#     for i in range(3):
#         for j in range(3):
#             buttons[i][j]["text"] = ""
# def button_click(row, col):
#     if buttons[row][col]["text"] == "":
#         buttons[row][col]["text"] = current_player
#         winner = check_winner()
#         if winner:
#             messagebox.showinfo("Tic-Tac-Toe", f"{winner} wins!")
#             reset_game()
#         else:
#             switch_player()
# root = tk.Tk()
# root.title("Tic-Tac-Toe")
# buttons = [[None] * 3 for _ in range(3)]
# for i in range(3):
#     for j in range(3):
#         button = tk.Button(root, text="", width=10, height=3, command=lambda row=i, col=j: button_click(row, col))
#         button.grid(row=i, column=j)
#         buttons[i][j] = button
# reset_button = tk.Button(root, text="Reset", command=reset_game)
# reset_button.grid(row=3, column=1)
# root.mainloop()







