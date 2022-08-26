from tkinter import *

class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()

        self.passwordLabel = Label(master, text="Enter the password")
        self.passwordLabel.grid(row=0, column=1)
        self.passwordLabel.place(x=3, y=3)

        self.passwordInput = StringVar()
        self.passwordInput = Entry(textvariable=self.passwordInput)
        self.passwordInput.grid(row=0, column=135)
        self.passwordInput.place(x=150, y=3)

        self.message = Message(master, text = '', width=280) 
        self.message.grid(row=3)
        self.message.place(x=0, y=50)

        def buttonClick():
            if self.passwordInput.get() == 'password':
                print("Verified!")
                self.message.config(text="You have access to something special.")
            else:
                print("Not Verified!")
                self.message.config(text="Access denied.")

        self.submitButton = Button(master, text="Submit", command=buttonClick)
        self.submitButton.grid(row=1, column=1)
        self.submitButton.place(x=225, y=28)

        def quit_window():
            master.destroy()

        self.quitButton = Button(master, text="QUIT", command=quit_window, fg='red')
        self.quitButton.grid(row=30, column=1)
        self.quitButton.place(x=3, y=130, width=279)

if __name__ == "__main__":
    mw = Tk()
    mw.title('Login')
    mw.geometry("285x160")

    guiFrame = GUI(master=mw)    
    guiFrame.mainloop()

    