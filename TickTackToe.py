from tkinter import *
import tkinter.messagebox
tk=Tk()
tk.title("Tic Tac Toe")
click = True
    
def game(buttons):
    global click
    if buttons["text"]==" " and click==True:
        buttons["text"]="x"
        click=False
    elif buttons["text"]==" " and click==False:
        buttons["text"]="o"
        click=True
    elif(button1["text"]=="x" and button2["text"]=="x" and button3["text"]=="x" or
         button4["text"]=="x" and button5["text"]=="x" and button6["text"]=="x" or
         button7["text"]=="x" and button8["text"]=="x" and button9["text"]=="x" or
         button3["text"]=="x" and button5["text"]=="x" and button7["text"]=="x" or
         button1["text"]=="x" and button5["text"]=="x" and button9["text"]=="x" or
         button1["text"]=="x" and button4["text"]=="x" and button7["text"]=="x" or
         button2["text"]=="x" and button5["text"]=="x" and button8["text"]=="x" or
         button3["text"]=="x" and button6["text"]=="x" and button9["text"]=="x"):
        tkinter.messagebox.showinfo("X wins", "Congratulations you won the game")
    else:
        (button1["text"]=="o" and button2["text"]=="o" and button3["text"]=="o" or
         button4["text"]=="o" and button5["text"]=="o" and button6["text"]=="o" or
         button7["text"]=="o" and button8["text"]=="o" and button9["text"]=="o" or
         button3["text"]=="o" and button5["text"]=="o" and button7["text"]=="o" or
         button1["text"]=="o" and button5["text"]=="o" and button9["text"]=="o" or
         button1["text"]=="o" and button4["text"]=="o" and button7["text"]=="o" or
         button2["text"]=="o" and button5["text"]=="o" and button8["text"]=="o" or
         button3["text"]=="o" and button6["text"]=="o" and button9["text"]=="o")
        tkinter.messagebox.showinfo("O wins", "Congratulations you won the game")

buttons=StringVar()
button1=Button(tk,text=" ",font=('Times 20 bold'),height=4,width=8,command=lambda:game(button1))
button1.grid(row=1, column=0,sticky=S+N+E+W)
button2=Button(tk,text=" ",font=('Times 20 bold'),height=4,width=8,command=lambda:game(button2))
button2.grid(row=1, column=1,sticky=S+N+E+W)
button3=Button(tk,text=" ",font=('Times 20 bold'),height=4,width=8,command=lambda:game(button3))
button3.grid(row=1, column=2,sticky=S+N+E+W)
button4=Button(tk,text=" ",font=('Times 20 bold'),height=4,width=8,command=lambda:game(button4))
button4.grid(row=2, column=0,sticky=S+N+E+W)
button5=Button(tk,text=" ",font=('Times 20 bold'),height=4,width=8,command=lambda:game(button5))
button5.grid(row=2, column=1,sticky=S+N+E+W)
button6=Button(tk,text=" ",font=('Times 20 bold'),height=4,width=8,command=lambda:game(button6))
button6.grid(row=2, column=2,sticky=S+N+E+W)
button7=Button(tk,text=" ",font=('Times 20 bold'),height=4,width=8,command=lambda:game(button7))
button7.grid(row=3, column=0,sticky=S+N+E+W)
button8=Button(tk,text=" ",font=('Times 20 bold'),height=4,width=8,command=lambda:game(button8))
button8.grid(row=3, column=1,sticky=S+N+E+W)
button9=Button(tk,text=" ",font=('Times 20 bold'),height=4,width=8,command=lambda:game(button9))
button9.grid(row=3, column=2,sticky=S+N+E+W)

tk.mainloop()
      
