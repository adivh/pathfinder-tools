from re import match
from tkinter import messagebox
from tkinter import Tk
from tkinter import Toplevel
from tkinter import ttk

from healthbar import Healthbar
from unit import Unit

class Window:
        

    def __init__(self):
        self.root = Tk()
        self.root.title("Party Manager")
        self.root.geometry("400x200")

        self.add_units = ttk.Button(self.root, command=self.create_new_unit_window, text="Add Member")
        self.add_units.grid(column=0, row=0)

        self.remove_units = ttk.Button(self.root, command=self.remove_unit, text="Del Member")
        self.remove_units.grid(column=2, row=0)

        self.units = []
        self.healthbars = []

        self.root.mainloop()

    
    def create_new_unit_window(self):

        unit_window = Toplevel(self.root)
        unit_window.title("New Unit")

        health_cur = ttk.Entry(unit_window)
        health_cur.pack()

        health_max = ttk.Entry(unit_window)
        health_max.pack()

        health_min = ttk.Entry(unit_window)
        health_min.pack()

        create_unit = ttk.Button(unit_window, command=lambda: self.add_unit(health_cur.get(), health_max.get(), health_min.get(), unit_window), text="Create Unit")
        create_unit.pack()


    def add_unit(self, health_cur, health_max, health_min, window):

        try:
            _cur = int(health_cur)
            _max = int(health_max)
            _min = int(health_min)
        except:
            return

        self.units.append(Unit(_cur, _max, _min))
        self.healthbars.append(Healthbar(self.root, _cur, _max, _min))
        self.healthbars[-1].grid(0, len(self.healthbars))

        if window is not None:
            window.destroy()


    def remove_unit(self):
        if len(self.healthbars) == 0:
            return

        _res = messagebox.askyesno(title="Remove Unit", message="Are you sure?")

        if _res:
            self.healthbars[-1].forget_and_destroy()
            del self.healthbars[-1]