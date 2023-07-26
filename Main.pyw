# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:29:05 2023

@author: besdawty
"""

from tkinter import *
import tkinter.messagebox as box

col_bg = "#ffffff" # Background Col
col_fg = "#45474a" # Foreground Col
col_im = "#55bac9" # Important col
col_bt = "#629e80" # Button Col
col_et = "#414540" # Entry text
col_eb = "#96ab91" # Entry Background

conversion_factors = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "rod": 5.0292
}


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
    
    if value.strip() == "":
        box.showerror("A Very Basic Error", "Please enter something!")
        return None
    
    if not_float(value):
        box.showerror("A Very Basic Error", "Please enter a valid number!\nnot " + str(value) + "?!")
        return None
    
    return float(value) * conversion_factors[unit]
    

def calculate_values(row, rowu, col, colu, self):
    row = conv_m(row,rowu)
    col = conv_m(col,colu)

    if row is not None and col is not None:
        ppm = ppm2(row, col)
        pha = ppm * 10000
        ppa = ppm * 4047

        result_text = "Plants per m2 = {:20,.2f}\nPlants per ha = {:20,.0f}\nPlants per acre = {:20,.0f}\n".format(ppm, pha, ppa)
        self.result_label.config(text=result_text)

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background=col_bg)

        self.parent = parent
        self.parent.title("Plant Spacing Calculator")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
        w = 435
        h = 530
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.create_widgets()
        

    def create_widgets(self):
        img = PhotoImage(file="img.png")
        img = img.subsample(2, 2)
        label = Label(self, image = img)
        label.image = img
        label.grid(row=1, column=1, columnspan = 5, pady=10)

        quit_button = Button(self, text="Quit", fg=col_im, bg=col_fg,
            command=self.onQuest)
        quit_button.grid(row=5, column=5, pady=5, padx=5, sticky=E)

        calculate_button = Button(self, text="Calculate", fg=col_fg, bg=col_bt,
                                  command=lambda: calculate_values(inputs_r_sp.get(), r_sp.get(), inputs_c_sp.get(), c_sp.get(), self))
        calculate_button.grid(row=5, column=1, pady=5, padx=5, sticky=W)

        r_sp = StringVar(self)
        r_sp.set("cm") # initial value
        lable_r_sp = Label(self, text="Row spacing", fg=col_fg, bg=col_bg)
        lable_r_sp.grid(row=2, column=1, padx=5, pady=5, sticky=E)
        inputs_r_sp = Entry(self, bd =1, fg=col_et, bg=col_eb, width=8)
        inputs_r_sp.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        opt_r_sp = OptionMenu(self, r_sp, *conversion_factors.keys())
        opt_r_sp.grid(row=2, column=3, padx=5, pady=5, sticky=W)
        opt_r_sp.config(bd=2, fg=col_fg, bg=col_bt)

        c_sp = StringVar(self)
        c_sp.set("cm") # initial value
        lable_c_sp = Label(self, text="Column spacing", fg=col_fg, bg=col_bg)
        lable_c_sp.grid(row=3, column=1, padx=5, pady=5, sticky=E)
        inputs_c_sp = Entry(self, bd =1, fg=col_et, bg=col_eb, width=8)
        inputs_c_sp.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        opt_c_sp = OptionMenu(self, c_sp, *conversion_factors.keys())
        opt_c_sp.grid(row=3, column=3, padx=5, pady=5, sticky=W)
        opt_c_sp.config(bd=2, fg=col_fg, bg=col_bt)

        self.result_label = Label(self, text="", fg=col_fg, bg=col_eb, justify=CENTER)
        self.result_label.grid(row=6, column=0, columnspan=5, pady=10)


    def onQuest(self):
        result = box.askquestion("Quit", "Did you intend to Quit?")
        if result == 'yes':
            self.parent.quit()
            self.parent.destroy()
        else:
            return True

def main():
    root = Tk()
    root.option_add('*Font', 'Arial 12')  # Set default font size for the app
    root.configure(background=col_fg)
    ex = Example(root)
    root.mainloop()

main()
