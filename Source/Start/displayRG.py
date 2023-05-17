from tkinter import *

# init tk
window = Tk()
window.title("GAME FIGHT")

# photo load
backgr = PhotoImage(file="./utils/image_button/b.png")
home = PhotoImage(file="./utils/image_button/home.png")
pause = PhotoImage(file="./utils/image_button/pause.png")
play = PhotoImage(file="./utils/image_button/playp.png")
setting = PhotoImage(file="./utils/image_button/settings.png")
volume = PhotoImage(file="./utils/image_button/volume.png")
interrogation = PhotoImage(file="./utils/image_button/interrogation.png")
door = PhotoImage(file="./utils/image_button/door.png")
# func
def rungame():
    rungame__.config(text="True")

def quit_py():
    quit_py__.config(text="False")

def quit():
    quit__.config(text="False")

def reset():
    rungame__.config(text="False")
    quit_py__.config(text="True")


# var
quit_py__ = Label(window, text="True")
rungame__ = Label(window, text="False")
quit__ = Label(window, text="True")

# display label and button
label = Label(window, image=backgr)
label.grid(row=0, column=0)

# frame btn
frame = Frame(window)

player = Button(frame, image=play, command=rungame)
player.grid(row=0, column=0, ipadx=35)

homer = Button(frame, image=pause, command=quit_py)
homer.grid(row=0, column=1, ipadx=35)

setter = Button(frame, image=setting)
setter.grid(row=0, column=2, ipadx=35)

volumer = Button(frame, image=volume)
volumer.grid(row=0, column=3, ipadx=35)

interrogationer = Button(frame, image=interrogation)
interrogationer.grid(row=0, column=4, ipadx=35)

dor = Button(frame, image=door, command=quit)
dor.grid(row=0, column=5, ipadx=27)

frame.grid(row=1, column=0)
