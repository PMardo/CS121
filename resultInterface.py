import tkinter
from tkinter.constants import INSERT
from tkinter.constants import END

DEFAULT_FONT = ('Verdana', 12)

class ResultApplication:
    def __init__(self, file):
        self._root_window = tkinter.Tk()
        self.text = tkinter.Text(self._root_window)
        f = open(file, 'r')
        for line in f.read():
            self.text.insert(INSERT, line)
        self.text.pack()
        self._root_window.mainloop()