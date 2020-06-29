from tkinter import *
import cv2
import time

class gui:

    def __init__(self, tk: Tk):
        self.tk = tk
        self.img = None
        self.counter = 0

        self.vs = cv2.VideoCapture(0)

        tk.title("Window Title")
        self.tk.geometry("300x300")
        self.tk.resizable(0,0)

        self.textEntry = Entry(tk)
        self.textEntry.pack(side=TOP)

        self.button1 = Button(tk, text="Enter", command=self.enterButton)
        self.button1.pack(side=TOP)


    def initCamera(self):
        self.img = self.vs.read()[1]
        time.sleep(1)

    def updateVideo(self):
        self.img = self.vs.read()[1]
        cv2.imshow("Demo Win", self.img)
        cv2.waitKey(1)

    def enterButton(self):
        cv2.imwrite(f"{self.textEntry.get()}.png", self.img)

root = Tk()
GUI = gui(root)

while True:
    GUI.updateVideo()
    root.update_idletasks()
    root.update()