import sys                   # this will give  your version you are using
print(sys.version)


import tkinter

window = tkinter.Tk()
window.title("Quit")

top_f = tkinter.Frame(window).pack()
bottom_f = tkinter.Frame(window).pack(side = "bottom")

btn1 = tkinter.Button(top_f,text = "Button 1",bg = "Pink", fg = "Blue",).pack()
btn2 = tkinter.Button(top_f,text = "Button 2",bg = "Violet", fg = "Red").pack()
btn3 = tkinter.Button(top_f,text = "Button 3",bg = "Indigo", fg = "Orange").pack(side = "left")
btn4 = tkinter.Button(top_f,text = "Button 4",bg = "Teal", fg = "Yellow").pack(side = "left")
btn5 = tkinter.Button(bottom_f,text = "Button 5",bg = "Silver" ,fg = "Green").pack(side = "right")
btn6 = tkinter.Button(bottom_f,text = "Button 6",bg = "Turquoise", fg = "Black").pack(side = "right")

window.mainloop()


