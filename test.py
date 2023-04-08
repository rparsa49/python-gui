from tkinter import *

# window class


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # create menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # adding menus to menu item
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.clickExitButton)
        menu.add_cascade(label="File", menu=fileMenu)

        # adding subitems to menu
        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)
        # widget will take the whole window
        self.pack(fill=BOTH, expand=1)

        # create button
        exitButton = Button(self, text="Bye bye!",
                            command=self.clickExitButton)

        # place button at top right
        exitButton.place(x=430, y=0)

    def clickExitButton(self):
        exit()


# initialie tkinter app
root = Tk()

# create a window
app = Window(root)


# set window  title
root.wm_title("Roya's Window")

# initialize size of button
root.geometry("500x500")

# show window
root.mainloop()
