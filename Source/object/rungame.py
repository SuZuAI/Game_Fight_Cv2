from tkinter import *
def rungame():
    done = False
    def subrun():
        nonlocal done
        win = Tk()
        win.title("test")
        win.geometry("300x300")

        def start():
            nonlocal done
            done = True
            win.destroy()

        def quit():
            nonlocal done
            done = False
            win.destroy()

        btn = Button(win, text="Start", font=("sans", 30),pady= 90, padx=100, fg="blue", state="active", command=start)
        btn.grid(column=1, row=1)

        btn_quit = Button(win, text="Quit", command=quit, font=("sans", 15), pady=15, justify=LEFT)
        btn_quit.grid(column=1, row = 2)

        win.mainloop()
    subrun()
    return done
