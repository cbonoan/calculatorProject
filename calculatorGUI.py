from tkinter import *
import re
import math

class Calc():
    def __init__(self):
        self.current = "" 

    def display(self,value):
        output.delete(0,END)
        output.insert(0,value)
    
    def clear(self):
        self.current = ""
        self.display(self.current)

    def back(self):
        self.current = self.current[:-1]
        self.display(self.current)

    def negate(self,num):
        temp = -1*float(num)
        self.display(temp)

    def press(self,num):
        temp = str(num)
        self.current += temp
        output.insert(END,temp)

    def function(self,op):
        if(op == "ln"):
            arg = float(output.get())
            if arg > 0:
                self.current = str(math.log(arg))
                self.display(self.current)
            else:
                self.display("Error")
        elif(op == "sqrt"):
            arg = float(output.get())
            if arg > 0:
                self.current = str(arg**(1/2))
                self.display(self.current)
            else:
                self.display("Error")
        elif(op == "sq"):
            arg = float(output.get())
            self.current = str(arg**2)
            self.display(self.current)

    def power(self,expression):
        split = expression.split("^")
        split = [int(x) for x in split]
        self.display(split[0]**split[1])
        

    def trig(self,func):
        degrees = float(output.get())
        radians = math.radians(degrees) #convert input to radians first 
        if func == "sin":
            ans = math.sin(radians)
            self.current = str(ans)
            self.display(self.current)
        elif func == "cos":
            ans = math.cos(radians)
            self.current = str(ans)
            self.display(self.current)
        elif func == "tan":
            ans = math.tan(radians)
            self.current = str(ans)
            self.display(self.current)

    
    def calc_total(self,expression):
        if "^" in expression:
            self.power(expression)
        else:
            try:
                temp = str(eval(expression))
                self.display(temp)
            except SyntaxError:
                self.display("Error")
            except ZeroDivisionError:
                self.display("Cannot Divide By Zero")

if __name__=="__main__": 
    express = Calc()
    gui = Tk()
    gui.geometry('300x250')
    gui.title("Scientific Calculator")
    gui.configure(bg="light blue")

    #output field 
    output = Entry(gui, bg="light gray")
    output.grid(columnspan=5, ipadx=90,ipady=10)
    
    operators = ["/","*","-","+"]
    numbers = [0,1,2,3,4,5,6,7,8,9]

    buttonClear = Button(gui, text="BKSP",
    command = lambda: express.back())
    buttonClear.grid(row=1,column=0)
    buttonCancel = Button(gui, text="Cancel",
    command = lambda: express.clear())
    buttonCancel.grid(row=1,column=2)
    buttonEnter = Button(gui, text=" = ", width=4,
    command = lambda: express.calc_total(output.get()))
    buttonEnter.grid(row=1,column=4)
    #buttons exp,ln,sqrt,sq
    buttonExp = Button(gui,text="exp",height=1,width=4,
    command = lambda:express.press("^"))
    buttonExp.grid(row=2, column=0)
    buttonLN = Button(gui,text="ln",height=1,width=4,
    command = lambda x = "ln": express.function("ln"))
    buttonLN.grid(row=3, column=0)
    buttonSqrt = Button(gui,text="sqrt",height=1,width=4,
    command = lambda x = "sqrt": express.function("sqrt"))
    buttonSqrt.grid(row=4, column=0)
    buttonSq = Button(gui,text="sq",height=1,width=4,
    command = lambda x = "sq": express.function("sq"))
    buttonSq.grid(row=5, column=0)
    #buttons 0-9 and operators
    num_bttns = []
    opers = []
    i = 0
    for row in range(2,5):
        for col in range(1,4):
            num_bttns.append(Button(gui,text = numbers[i],height=1,width=4,
            command = lambda x = numbers[i]: express.press(x)))
            num_bttns[i].grid(row=row,column=col, pady=5)
            i += 1
    num_bttns.append(Button(gui,text=numbers[i],height=1,width=4,
    command=lambda x = numbers[i]: express.press(x)))
    num_bttns[i].grid(row=5,column=1,pady=5)

    row=2
    index=0
    for i in operators:
        opers.append(Button(gui,text=i,height=1,width=4,
        command = lambda x=i: express.press(x)))
        opers[index].grid(row=row,column=4,pady=5)
        row += 1
        index += 1
    #buttons decimal and +/-
    buttonDec =  Button(gui, text=" . ",height=1,width=4,
    command=lambda: express.press("."))
    buttonDec.grid(row=5,column=2)
    buttonNeg =  Button(gui, text=" +/- ",height=1,width=4,
    command=lambda: express.negate(output.get()))
    buttonNeg.grid(row=5,column=3)
    #trig buttons 
    buttonSin = Button(gui,text=" sin ", height=1,width=4,
    command = lambda: express.trig("sin"))
    buttonSin.grid(row=6,column=1,pady=5) 
    buttonCos = Button(gui,text=" cos ", height=1,width=4,
    command = lambda: express.trig("cos"))
    buttonCos.grid(row=6,column=2)
    buttonTan = Button(gui,text=" tan ", height=1,width=4,
    command = lambda: express.trig("tan"))
    buttonTan.grid(row=6,column=3)

    gui.mainloop() 
