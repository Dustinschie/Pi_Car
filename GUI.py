from Tkinter import *
from client import Client
class GUI:
    __validControls = ('w','s','a','d','wa', 'aw', 'wd', 'dw',
        'sa', 'as', 'sd', 'ds')

    def __init__(self):
        self.multiKey = ''
        hostIP = raw_input("Enter Client IP address:")

        self.client = Client(str(hostIP))
        self.window = Tk()   #   Create Window
        self.window.title("Driver")  #   set Title
        self.canvas = Canvas(self.window, bg = 'white', width = 200, 
            height = 200)
        self.canvas.pack()

        #   Bind with <Button-1> event
        self.canvas.bind("<B1-Motion>", self.processMouseEvent)
        self.canvas.bind("<Button-3>", self.processMouseEvent)
        #   Bind with <Key> event
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()

        self.window.mainloop()

    def processMouseEvent(self, event):
        self.canvas.delete("all")
        # print(event.x, event.y)
        print(event.x_root, event.y_root)
        self.canvas.create_line(100, 
            100, event.x, event.y, arrow = "last", fill = "blue")



    def processKeyEvent(self, event):
        # print("keysym? ", event.keysym)
        # print("char? ", event.char)
        # print("keycode? ", event.keycode)
        string = str(self.multiKeyHandler(event.char))
        self.client.send(string)
        print("\t" + string)

    #   psuedo multi-key event handler
    def multiKeyHandler(self, key):
        if key in GUI.__validControls:
            if len(self.multiKey) == 0:
                self.multiKey = key
            elif len(self.multiKey) == 1:
                if self.multiKey != key:
                    temp = self.multiKey + key
                    if temp in GUI.__validControls:
                        self.multiKey = temp
                    else:
                        self.multiKey = key
            elif key not in self.multiKey:
                if key == 'w':
                    self.multiKey = self.multiKey.replace("s", 'w')
                elif key == 's':
                    self.multiKey = self.multiKey.replace("w", 's')
                elif key == 'a':
                    self.multiKey = self.multiKey.replace("d", 'a')
                else:
                    self.multiKey = self.multiKey.replace("a", 'd')
        else:
            self.multiKey = ''

        return self.multiKey

GUI()
