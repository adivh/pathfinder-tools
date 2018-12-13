from re import match
from tkinter import messagebox
from tkinter import Tk
from tkinter import Toplevel
from tkinter import ttk

from unit import Unit
from unit_widget import Unit_Widget



class Window:
        


    def __init__(self):
        self.root = Tk()
        self.root.title("Party Manager")
        self.root.geometry("400x200")
        self.draw_health_decor = False

        self.add_unit_widgets = ttk.Button(self.root, command=self.create_new_unit_window, text="Add Member")
        self.add_unit_widgets.grid(column=0, row=0)

        self.remove_unit_widgets = ttk.Button(self.root, command=self.remove_unit, text="Del Member")
        self.remove_unit_widgets.grid(column=1, row=0)

        self.unit_widgets = []
        self.health_limit_min = 0
        self.health_limit_max = 0



    def add_unit(self, health_min, health_max, health_cur, window=None):
        ''' Add a Unit_Widget to the window.
            The window parameter is used when this method is called in conjunction with a unit creation window.
            If a window is passed and a unit_widget is successfully created, the window will be destroyed. '''

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

        for unit in self.unit_widgets:
            unit.new_health_limit(self.health_limit_min, self.health_limit_max)
            unit.update()

        # Create a new unit_widget.

        self.unit_widgets.append(Unit_Widget(self.root, Unit(_min, _max, _cur), self.health_limit_min, self.health_limit_max))
        self.unit_widgets[-1].grid(0, len(self.unit_widgets), columnspan=2)

        # Destroy window after successfully adding the unit_widget.

        if window is not None:
            window.destroy()
    
    

    def create_new_unit_window(self):
        ''' This method creates a unit creation window.
            The method is designed for interal use.
            External method calls are not recommended. '''

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



    def remove_unit(self):
        ''' Remove the last unit in a group. '''

        if len(self.unit_widgets) == 0:
            return

        _res = messagebox.askyesno(title="Remove Unit", message="Are you sure?")

        if _res:
            self.unit_widgets[-1].forget_and_destroy()
            del self.unit_widgets[-1]

            self.health_limit_min = 0
            self.health_limit_max = 0

            for unit_widget in self.unit_widgets:
                self.health_limit_min = min(self.health_limit_min, unit_widget.unit.health_min)
                self.health_limit_max = max(self.health_limit_max, unit_widget.unit.health_max)

            for unit_widget in self.unit_widgets:
                unit_widget.new_health_limit(self.health_limit_min, self.health_limit_max)
                unit_widget.update()


    
    def start(self):
        ''' Start the window.
            This method calls tkinter.Tk.mainloop().
            Calling this method blocks until the window is closed. '''

        self.root.mainloop()