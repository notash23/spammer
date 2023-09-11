import time
from tkinter import *
import pyautogui

root = Tk()
root.title("Spammer")
root.geometry("500x500")
myLabel = Label(root, text="Enter the spam text")
myLabel.pack(pady=50, padx=250)
e = Entry(root, width=75)
e.pack()


def onclick():
    f = e.get()
    time.sleep(5)
    while True:
        pyautogui.typewrite(f)
        pyautogui.press('enter')


button = Button(root, text="enter", command=onclick)
button.pack()
root.mainloop()
