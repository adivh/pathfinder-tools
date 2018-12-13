from re import match
from tkinter import messagebox
from tkinter import Tk
from tkinter import Toplevel
from tkinter import ttk

from unit_widget import Unit_Widget



class Window:
        


    def __init__(self):
        self.root = Tk()
        self.root.title("Party Manager")
        self.root.geometry("400x200")
        self.draw_health_decor = False

        self.add_units = ttk.Button(self.root, command=self.create_new_unit_window, text="Add Member")
        self.add_units.grid(column=0, row=0)

        self.remove_units = ttk.Button(self.root, command=self.remove_unit, text="Del Member")
        self.remove_units.grid(column=1, row=0)

        self.units = []
        self.health_limit_min = 0
        self.health_limit_max = 0


    
    def start(self):
        self.root.mainloop()
    
    
    def create_new_unit_window(self):

        unit_window = Toplevel(self.root)
        unit_window.title("New Unit")

        health_min = ttk.Entry(unit_window)
        health_min.pack()

        health_max = ttk.Entry(unit_window)
        health_max.pack()

        health_cur = ttk.Entry(unit_window)
        health_cur.pack()

        create_unit = ttk.Button(unit_window, command=lambda: self.add_unit(health_min.get(), health_max.get(), health_cur.get(), unit_window), text="Create Unit")
        create_unit.pack()



    def add_unit(self, health_min, health_max, health_cur, window=None):

        try:
            _min = int(health_min)
            _max = int(health_max)
            _cur = int(health_cur)
        except:
            return

        # Consolidate input to be signed correctly.

        _min = min(_min, -_min)
        _max = max(_max, -_max)

        # Adjust global health limits.
        # Forward gloabal health limits to every existing unit_widgets.

        self.health_limit_min = min(self.health_limit_min, _min)
        self.health_limit_max = max(self.health_limit_max, _max)

        for unit in self.units:
            unit.new_health_limit(self.health_limit_min, self.health_limit_max)
            unit.update()

        # Create a new unit_widget.

        self.units.append(Unit_Widget(self.root, _min, _max, _cur, self.health_limit_min, self.health_limit_max))
        self.units[-1].grid(0, len(self.units))

        # Destroy window after successfully adding the unit_widget.

        if window is not None:
            window.destroy()



    def remove_unit(self):
        if len(self.units) == 0:
            return

        _res = messagebox.askyesno(title="Remove Unit", message="Are you sure?")

        if _res:
            self.units[-1].forget_and_destroy()
            del self.units[-1]

            self.health_limit_min = 0
            self.health_limit_max = 0

            for unit in self.units:
                self.health_limit_min = min(self.health_limit_min, unit.healthbar.health_min)
                self.health_limit_max = max(self.health_limit_max, unit.healthbar.health_max)

            for unit in self.units:
                unit.new_health_limit(self.health_limit_min, self.health_limit_max)
                unit.update()