from tkinter import *
from tkinter.messagebox import *

ERROR_MESSAGE_1 = "Invalid input."
ERROR_MESSAGE_2 = "Can't divide by 0."

class Calculator():
    def __init__(self):
        self.total = 0 #Retient ou le total des opérations est rendu
        self.current = "" #Contient le contenu de l'écran d'affichage
        self.new_num = True #Recommence le nombre
        self.op_pending = False #Si il y a une opération en attente
        self.op = "" #Opération à effectuer
        self.eq = False #Lorsque la touche égale est appuyée.

    def flush_text_box(self):
        text_box.configure(state="normal")
        text_box.delete(0, END)
        text_box.configure(state="disabled")

#Fonction pour afficher les chiffres à l'écran
    def num_press(self, num):
        if self.eq == True:
            self.all_cancel()
            self.eq = False

        if self.current == "0":
            if num == 0:
                return
            else:
                if num != '.':
                    self.all_cancel()

        temp = text_box.get()        
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            if temp2 == '.':
                self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp2
        self.display(temp2)
        self.op = ""

#Fonction pour la touche Égale
    def calc_total(self):
        if (not self.current) or (self.op):
            return 
        self.eq = True
        self.do_sum() #set total
        self.display(self.total)

#Fonction pour afficher à l'écran
    def display(self, value):
        text_box.configure(state="normal")
        if text_box.get() == ERROR_MESSAGE_1:
            text_box.delete(0,END)
        text_box.insert(END, value)
        text_box.configure(state="disabled")
        self.current = text_box.get()

        #Vous devez écrire le code pour afficher l'information dans le textbox.

#Fonction pour calculer
#Une division par 0 devrait montrer un message d'erreur "Can't Divide by 0."
    def do_sum(self):
        #Vous devez définir le code pour les différentes opérations de la calculatrice.
        #Une division par 0 devrait montrer un message d'erreur "Can't Divide by 0."
        self.new_num = True
        self.op_pending = False
        try:
           self.total = eval(self.current)
        except ZeroDivisionError as error:
            showerror("Title", ERROR_MESSAGE_2)
        self.flush_text_box()        

#Fonction pour storer l'opération
    def operation(self, op):
        if (not self.current):
            return 

        self.op_pending = True
        self.new_num = True
        self.eq = False

        if self.current[-1] in ['-','+','/','*']:
            temp = text_box.get()[:-1] 
            self.all_cancel()
            self.display(temp)
            
        if op in self.current:
            self.do_sum()
            self.display(self.total)

        self.op = op
        self.display(op)

#Fonction pour canceller (Touche A/C)
    def all_cancel(self):
        #You must write the code to reset the different variables.
        self.flush_text_box()
        
        self.total = 0 #Retient or the total of operations is rendered
        self.current = "" #Contains the content of the display screen
        self.new_num = True #Recommences the number
        self.op_pending = False #If there is a pending operation
        self.op = "" # Operation to perform
        self.eq = False #When the equal key is pressed.
        #Vous devez écrire le code pour réinitialiser les différentes variables.
        
#Fonction pour les pourcentages
    def calc_percent(self):
        if (not self.current) or (self.op):
            return  
        self.do_sum()
        self.current = float(eval(self.current))
        self.current = (self.total * (self.current/100))
        self.display(self.current)

#Fonction pour changer les nombres en positifs et négatifs
    def sign(self):
        self.eq = False
        if (not self.current) or (self.op):
            return 
        self.calc_total()

        self.flush_text_box()
        self.display(self.total * -1)
        #Vous devez écrire le code pour changer le signe du nombre entré.

#Déclaration de l'application "Calculator"
tk = Tk()
frame = Frame(tk)
frame.pack()

tk.title("Calculator")
calc = Calculator()

#Déclaration du text_box (C'est important de l'appeller text_box)
text_box = Entry(frame, width=20, font=("Arial",12), justify=RIGHT)
text_box.grid(row=0, column=0, columnspan=4)
text_box.focus_set()
text_box.configure(state="disabled", disabledbackground="white", disabledforeground="black")

# Déclaration des boutons de 1 à 9
bttn_0 = Button(frame, text = "0", height = 3, width = 5)
bttn_0["command"] = lambda: calc.num_press(0)
bttn_0.grid(row = 5, column = 0, columnspan = 2, pady = 1, sticky=N+S+E+W)

bttn_1 = Button(frame, text = "1", height = 3, width = 5)
bttn_1["command"] = lambda: calc.num_press(1)
bttn_1.grid(row = 4, column = 0, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_2 = Button(frame, text = "2", height = 3, width = 5)
bttn_2["command"] = lambda: calc.num_press(2)
bttn_2.grid(row = 4, column = 1, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_3 = Button(frame, text = "3", height = 3, width = 5)
bttn_3["command"] = lambda: calc.num_press(3)
bttn_3.grid(row = 4, column = 2, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_4 = Button(frame, text = "4", height = 3, width = 5)
bttn_4["command"] = lambda: calc.num_press(4)
bttn_4.grid(row = 3, column = 0, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_5 = Button(frame, text = "5", height = 3, width = 5)
bttn_5["command"] = lambda: calc.num_press(5)
bttn_5.grid(row = 3, column = 1, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_6 = Button(frame, text = "6", height = 3, width = 5)
bttn_6["command"] = lambda: calc.num_press(6)
bttn_6.grid(row = 3, column = 2, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_7 = Button(frame, text = "7", height = 3, width = 5)
bttn_7["command"] = lambda: calc.num_press(7)
bttn_7.grid(row = 2, column = 0, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_8 = Button(frame, text = "8", height = 3, width = 5)
bttn_8["command"] = lambda: calc.num_press(8)
bttn_8.grid(row = 2, column = 1, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_9 = Button(frame, text = "9", height = 3, width = 5)
bttn_9["command"] = lambda: calc.num_press(9)
bttn_9.grid(row = 2, column = 2, columnspan = 1, pady = 1, sticky=N+S+E+W)

#Déclaration des autres boutons.
bttn_ac = Button(frame, text = "A/C", height = 3, width = 5)
bttn_ac["command"] = lambda: calc.all_cancel()
bttn_ac.grid(row = 1, column = 0, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_sign = Button(frame, text = "+/-", height = 3, width = 5)
bttn_sign["command"] = lambda: calc.sign()
bttn_sign.grid(row = 1, column = 1, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_pc = Button(frame, text = "%", height = 3, width = 5)
bttn_pc["command"] = lambda: calc.calc_percent()
bttn_pc.grid(row = 1, column = 2, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_divide = Button(frame, text = "÷", height = 3, width = 5)
bttn_divide["command"] = lambda: calc.operation('/')
bttn_divide.grid(row = 1, column = 3, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_mul = Button(frame, text = "×", height = 3, width = 5)
bttn_mul["command"] = lambda: calc.operation('*')
bttn_mul.grid(row = 2, column = 3, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_sub = Button(frame, text = "-", height = 3, width = 5)
bttn_sub["command"] = lambda: calc.operation('-')
bttn_sub.grid(row = 3, column = 3, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_sum = Button(frame, text = "+", height = 3, width = 5)
bttn_sum["command"] = lambda: calc.operation('+')
bttn_sum.grid(row = 4, column = 3, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_dot = Button(frame, text = ".", height = 3, width = 5)
bttn_dot["command"] = lambda: calc.num_press('.')
bttn_dot.grid(row = 5, column = 2, columnspan = 1, pady = 1, sticky=N+S+E+W)

bttn_eq = Button(frame, text = "=", height = 3, width = 5)
bttn_eq["command"] = lambda: calc.calc_total()
bttn_eq.grid(row = 5, column = 3, columnspan = 1, pady = 1, sticky=N+S+E+W)

tk.mainloop()