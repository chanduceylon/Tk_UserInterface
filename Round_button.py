#######Basic switch in tkinter######

from tkinter import *
root= Tk()

class CustomButton(Canvas):
    def __init__(self, parent, width, height, color, channelNo, txt="",  command=None):
        Canvas.__init__(self, parent, borderwidth=1,
            relief="flat", highlightthickness=0)
        self.command = command
        self.channelNo = channelNo
        self.width = width
        self.height=height
        self.txt=txt
        self.clicked=False
        padding = 4
        id = self.create_oval((padding,padding,
            width+padding, height+padding), outline=color, fill=color)
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0) + padding
        height = (y1-y0) + padding
        self.configure(width=width, height=height)
        self.create_text((x1+x0)/2, (y1+y0)/2, text=txt)
        self.bind("<Button-1>", self._on_press)
       # self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
       if(self.clicked == False):
           padding = 4
           id = self.create_oval((padding, padding,
                                  self.width + padding, self.height + padding), outline="black", fill='red')
           (x0, y0, x1, y1) = self.bbox("all")
           width = (x1 - x0) + padding
           height = (y1 - y0) + padding
           self.configure(width=width, height=height)
           self.create_text((x1 + x0) / 2, (y1 + y0) / 2, text='On')
           self.clicked=True
       else:
           padding = 4
           id = self.create_oval((padding, padding,
                                  self.width + padding, self.height + padding), outline="black", fill='green')
           (x0, y0, x1, y1) = self.bbox("all")
           width = (x1 - x0) + padding
           height = (y1 - y0) + padding
           self.configure(width=width, height=height)
           self.create_text((x1 + x0) / 2, (y1 + y0) / 2, text='Off')
           self.clicked = False



    def _on_release(self, event):
        self.configure(relief="flat")
        if self.command is not None:
            self.command()


#app = Tk()

button = CustomButton(root, 100, 100, 'green',1, "123")
button.place(x=600, y=300)
root.mainloop()