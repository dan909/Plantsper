# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:29:05 2023

@author: besdawty
"""

from tkinter import *
import tkinter.messagebox as box

col_bg = "#EEEEDB" # Background Col
col_fg = "#003b6f" # Foreground Col
col_im = "#da635d" # Important col
col_bt = "#088DA5" # Button Col
col_et = "#000b16" # Entry text
col_eb = "#DEDEB8" # Entry Background


def ppm2(row,col):
    ppm = 1/(float(row)*float(col))
    return ppm

def not_float(value):
  try:
    float(value)
    return False
  except ValueError:
    return True


def conv_m(value, unit):
    print(value)
    print(unit)
    
    if not_float(value):
        box.showerror("A Very Basic Error", "You enterd: " + value + "\nYOU NEED TO ENTER NUMBERS!!") 
    elif unit == "mm":
        return float(value)/1000
    elif unit == "cm":
        return float(value)/100
    elif unit == "m":
        return float(value)
    elif unit == "km":
        return float(value)*1000
    elif unit == "inch":
        return float(value)/39.37
    elif unit == "foot":
        return float(value)/3.281
    elif unit == "yard":
        return float(value)/1.094
    elif unit == "rod":
        return float(value)/5.029
    else:
        box.showerror("A Very Basic Error", "Not a known unit?!") 
    

def valueGET(row, rowu, col, colu):
    row = conv_m(row,rowu)
    col = conv_m(col,colu)
    
    ppm = ppm2(row,col)
    pha = ppm*10000
    ppa = ppm*4047

    
    box.showinfo("Answer", 
                 "Plants per m2 = {:20,.2f}\nPlants per ha = {:20,.0f}\nPlants per acre = {:20,.0f}\n".format(ppm, pha, ppa))


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background=col_bg)

        self.parent = parent
        self.parent.title("Plant Spacing Calculator")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):

        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        quitButton = Button(self, text="Quit", fg=col_im, bg=col_fg,
            command=self.onQuest)
        quitButton.place(x=250, y=120)

        inform = Button(self, text="Calculate", fg=col_fg, bg=col_bt,
                        command=lambda: valueGET(inputs_r_sp.get(), r_sp.get(), inputs_c_sp.get(), c_sp.get()))
        inform.place(x=5, y=120)

        r_sp = StringVar(self)
        r_sp.set("cm") # initial value
        lable_r_sp = Label(self, text="Row spacing", fg=col_fg, bg=col_bg)
        lable_r_sp.grid(row=1, column=1)
        inputs_r_sp = Entry(self, bd =1, fg=col_et, bg=col_eb, width=8)
        inputs_r_sp.grid(row=1, column=2)
        opt_r_sp = OptionMenu(self, r_sp, "mm", "cm", "m", "km", "inch", "foot", "yard","rod")
        opt_r_sp.grid(row=1, column=3)
        opt_r_sp.config(bd=2, fg=col_fg, bg=col_bt)

        c_sp = StringVar(self)
        c_sp.set("cm") # initial value
        lable_c_sp = Label(self, text="Column spacing", fg=col_fg, bg=col_bg)
        lable_c_sp.grid(row=2, column=1)
        inputs_c_sp = Entry(self, bd =1, fg=col_et, bg=col_eb, width=8)
        inputs_c_sp.grid(row=2, column=2)
        opt_c_sp = OptionMenu(self, c_sp, "mm", "cm", "m", "km", "inch", "foot", "yard","rod")
        opt_c_sp.grid(row=2, column=3)
        opt_c_sp.config(bd=2, fg=col_fg, bg=col_bt)


    def onQuest(self):
        result = box.askquestion("Quit", "Did you intend to Quit?")
        if result == 'yes':
            global root
            root.quit()
            root.destroy()
        else:
            return True

def main():
    global root
    root = Tk()
    ex = Example(root)
    root.mainloop()

main()