import tkinter

window = tkinter.Tk()
window.title("return something")


def out_put():
    tkinter.Label(window, text="Hacking is not a crime , = It is art you poples can not understand ").pack()


tkinter.Button(window,text = "click me !" , command = out_put).pack()

window.mainloop()
