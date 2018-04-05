# popup a GUI dialog for unpacker script arguments, and run it

from tkinter import *
from unpacker import unpack
from formrows import makeFormRow


def unpackDialog():
    win = Toplevel()
    win.title('Enter Unpack Parameters')
    var = makeFormRow(win, label='Input file', width=11)
    win.bind('<Key-Return>', lambda event: win.destroy())  # when enter is pressed
    win.grab_set()
    win.focus_set()
    win.wait_window()
    return var.get()


def runUnpackDialog():
    input = unpackDialog()
    if input != '':  # if file is entered
        print('Unpacker:', input)
        unpack(ifile=input, prefix='')  # default, writes out new files without a 'new' prefix


if __name__ == '__main__':
    Button(None, text='popup', command=runUnpackDialog).pack()
    mainloop()
