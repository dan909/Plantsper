# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:29:05 2023

@author: besdawty
modified using GPT3.5
"""

from tkinter import *
import tkinter.messagebox as box

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


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="#f0f0f0")
        self.parent = parent
        self.parent.title("Plant Spacing Calculator")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        
    def centerWindow(self):
        w = 430
        h = 490
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.create_widgets()

    def create_widgets(self):
        img = PhotoImage(file="img.png")
        img = img.subsample(2, 2)
        label = Label(self, image=img)
        label.image = img
        label.grid(row=1, column=0, columnspan=3, pady=10)

        self.r_sp = StringVar(self)
        self.r_sp.set("cm")  # initial value
        label_r_sp = Label(self, text="Row spacing:")
        label_r_sp.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.inputs_r_sp = Entry(self, bd=1)
        self.inputs_r_sp.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        opt_r_sp = OptionMenu(self, self.r_sp, *conversion_factors.keys())
        opt_r_sp.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        self.c_sp = StringVar(self)
        self.c_sp.set("cm")  # initial value
        label_c_sp = Label(self, text="Column spacing:")
        label_c_sp.grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.inputs_c_sp = Entry(self, bd=1)
        self.inputs_c_sp.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        opt_c_sp = OptionMenu(self, self.c_sp, *conversion_factors.keys())
        opt_c_sp.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        # Create StringVar variables for live updating
        self.inputs_r_sp_sv = StringVar(self, value="")
        self.inputs_c_sp_sv = StringVar(self, value="")

        # Associate StringVar with Entry widgets
        self.inputs_r_sp = Entry(self, bd=1, textvariable=self.inputs_r_sp_sv)
        self.inputs_r_sp.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.inputs_c_sp = Entry(self, bd=1, textvariable=self.inputs_c_sp_sv)
        self.inputs_c_sp.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        self.result_label = Label(self, text="", fg="#45474a", bg="#f0f0f0", justify=LEFT)
        self.result_label.grid(row=4, column=0, columnspan=3, pady=10)

        # Register the callback for live updating
        self.inputs_r_sp_sv.trace("w", self.update_result)
        self.inputs_c_sp_sv.trace("w", self.update_result)
        self.r_sp.trace("w", self.update_result)
        self.c_sp.trace("w", self.update_result)
        

    def update_result(self, *args):
        try:
            row = float(self.inputs_r_sp_sv.get()) * conversion_factors[self.r_sp.get()]
            col = float(self.inputs_c_sp_sv.get()) * conversion_factors[self.c_sp.get()]

            ppm = ppm2(row, col)
            pha = ppm * 10000
            ppa = ppm * 4047

            result_text = f"Plants per m2: {ppm:,.2f}\nPlants per ha: {pha:,.0f}\nPlants per acre: {ppa:,.0f}"
            self.result_label.config(text=result_text)
        except ValueError:
            self.result_label.config(text="")

    def on_quit(self):
        result = box.askquestion("Quit", "Did you intend to quit?")
        if result == 'yes':
            self.parent.quit()
            self.parent.destroy()

def main():
    root = Tk()
    root.option_add('*Font', 'Arial 12')  # Set default font size for the app
    ex = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    
