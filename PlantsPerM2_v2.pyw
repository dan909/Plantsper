from tkinter import *
import tkinter.messagebox as box

conversion_factors_length = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "rod": 5.0292
}

conversion_factors_density = {
    "cm2": 10000,
    "m2": 1,
    "hectare": 1/10000,
    "km2": 1/1000000,
    "square_inch": 1550,
    "square_foot": 10.764,
    "square_yard": 1.196,
    "square_rod": 25.293,  
    "acre": 0.0002470966,
    "mile2": 0.000000386
}


def spacing_from_ppm(ppm):
    if ppm <= 0:
        box.showerror("A Very Basic Error", "Plants per square meter must be greater than 0!")
        return None
    
    return 1 / (ppm ** 0.5)


def spacing_rect_from_ppm(ppm, other_sp):
    if ppm <= 0:
        box.showerror("A Very Basic Error", "Plants per square meter must be greater than 0!")
        return None

    if other_sp <= 0:
        box.showerror("A Very Basic Error", "Plants per square meter must be with a value greater than 0!")
        return None
    
    return (1/other_sp)/ppm


def ppm2(row,col):
    ppm = 1/(float(row)*float(col))
    return ppm


def make_result_text(row,row_u,col,col_u,ppm,ppm_u):
    if ppm.strip() == "":
        row = float(row) * conversion_factors_length[row_u]
        col = float(col) * conversion_factors_length[col_u]
        
        a_ppm = ppm2(row, col)
        a_pha = a_ppm * 10000
        a_ppa = a_ppm * 4047

        return f"Density: {a_ppm:,.2f} Plants per m2\nDensity: {a_pha:,.0f} Plants per ha\nDensity: {a_ppa:,.0f} Plants per acre"
    
    elif row.strip() == "" and col.strip() == "":
        a_ppm = float(ppm)*conversion_factors_density[ppm_u]
        suggested_spacing = spacing_from_ppm(a_ppm)
        
        return f"Suggested spacing: {suggested_spacing:.2f} m X {suggested_spacing:.2f} m"
    
    else:
        a_ppm = float(ppm)*conversion_factors_density[ppm_u]
        suggested_spacing = spacing_from_ppm(a_ppm)

        try:
            other = float(row) * conversion_factors_length[row_u]
        except ValueError:
            other = float(col) * conversion_factors_length[col_u]

        suggested_spacing = spacing_rect_from_ppm(a_ppm,other)
        
        return f"Suggested spacing: {other} m X {suggested_spacing:.2f} m"
    


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="#f0f0f0")
        self.parent = parent
        self.parent.title("Plant Spacing Calculator")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        
    def centerWindow(self):
        w = 430
        h = 520
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
        opt_r_sp = OptionMenu(self, self.r_sp, *conversion_factors_length.keys())
        opt_r_sp.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        self.c_sp = StringVar(self)
        self.c_sp.set("cm")  # initial value
        label_c_sp = Label(self, text="Column spacing:")
        label_c_sp.grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.inputs_c_sp = Entry(self, bd=1)
        self.inputs_c_sp.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        opt_c_sp = OptionMenu(self, self.c_sp, *conversion_factors_length.keys())
        opt_c_sp.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        self.ppm_sp = StringVar(self)
        self.ppm_sp.set("m2")  # initial value
        label_ppm_sp = Label(self, text="Density:")
        label_ppm_sp.grid(row=4, column=0, padx=5, pady=5, sticky=E)
        self.inputs_ppm_sp = Entry(self, bd=1)
        self.inputs_ppm_sp.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        opt_ppm_sp = OptionMenu(self, self.ppm_sp, *conversion_factors_density.keys())
        opt_ppm_sp.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        # Create StringVar variables for live updating
        self.inputs_r_sp_sv = StringVar(self, value="")
        self.inputs_c_sp_sv = StringVar(self, value="")
        self.inputs_ppm_sp_sv = StringVar(self, value="")

        # Associate StringVar with Entry widgets
        self.inputs_r_sp = Entry(self, bd=1, textvariable=self.inputs_r_sp_sv)
        self.inputs_r_sp.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.inputs_c_sp = Entry(self, bd=1, textvariable=self.inputs_c_sp_sv)
        self.inputs_c_sp.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self.inputs_ppm_sp = Entry(self, bd=1, textvariable=self.inputs_ppm_sp_sv)
        self.inputs_ppm_sp.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Register the callback for live updating
        self.inputs_r_sp_sv.trace("w", self.update_result)
        self.inputs_c_sp_sv.trace("w", self.update_result)
        self.inputs_ppm_sp_sv.trace("w", self.update_result)
        self.r_sp.trace("w", self.update_result)
        self.c_sp.trace("w", self.update_result)
        self.ppm_sp.trace("w", self.update_result)

        self.result_label = Label(self, text="", fg="#45474a", bg="#f0f0f0", justify=LEFT)
        self.result_label.grid(row=5, column=0, columnspan=3, pady=10)

    def update_result(self, *args):
        try:
            result_text = make_result_text(self.inputs_r_sp_sv.get(),self.r_sp.get(),self.inputs_c_sp_sv.get(),self.c_sp.get(),self.inputs_ppm_sp_sv.get(),self.ppm_sp.get())
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
