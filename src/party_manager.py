from tkinter import filedialog
from tkinter import IntVar
from tkinter import messagebox
from tkinter import Tk
from tkinter import Toplevel
from tkinter import ttk

from charactersheet_loader import Charactersheet_Loader
from unit import Unit
from unit_widget import Unit_Widget



class Party_Manager:
        


    def __init__(self):
        self.root = Tk()
        self.root.title("Party Manager")
        #self.root.geometry("400x200")
        self.draw_health_decor = False

        self.add_unit_widgets = ttk.Button(self.root, command=self.create_file_dialog, text="Add Member")
        self.add_unit_widgets.grid(sticky='e', column=0, row=0)

        self.remove_unit_widgets = ttk.Button(self.root, command=self.create_remove_unit_window, text="Del Member")
        self.remove_unit_widgets.grid(sticky='w', column=1, row=0)

        self.unit_widgets = []
        self.marked_for_delete = []
        self.health_limit_min = 0
        self.health_limit_max = 0



    def add_unit(self, name, classes, levels, health_min, health_max, health_cur, window=None):
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

        _unit = Unit(name, classes, levels, _min, _max, _cur)
        self.unit_widgets.append(Unit_Widget(self.root, _unit, self.health_limit_min, self.health_limit_max))
        self.unit_widgets[-1].grid(0, Unit_Widget.height * len(self.unit_widgets), columnspan=2)

        self.marked_for_delete.append(IntVar())

        # Destroy window after successfully adding the unit_widget.

        if window is not None:
            window.destroy()



    def create_file_dialog(self):
        ''' Create a file dialog to load charactersheets. 
            This will accept all files but ignore files not ending in .yaml or .yml. '''
        
        _path = filedialog.askopenfilenames()
        
        for path in _path:
            if path.endswith('.yaml') or path.endswith('.yml'):
                unit = Charactersheet_Loader.load_unit(path)
                self.add_unit(unit.name, unit.classes, unit.levels, unit.health_min, unit.health_max, unit.health_cur)

    
    

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

        create_unit = ttk.Button(unit_window, command=lambda: self.add_unit('Horst', ['Perversling'], [1], health_min.get(), health_max.get(), health_cur.get(), unit_window), text="Create Unit")
        create_unit.pack()



    def create_remove_unit_window(self):
        ''''''

        if len(self.unit_widgets) == 0:
            return
        
        selection_window = Toplevel(self.root)
        selection_window.title('Remove units')

        checkbuttons = []

        for i in range(0, len(self.unit_widgets)):
            checkbuttons.append(ttk.Checkbutton(selection_window, variable=self.marked_for_delete[i], text=self.unit_widgets[i].unit.name))
            checkbuttons[i].grid(sticky='w', column=0, row=i)

        remove_button = ttk.Button(selection_window, command=lambda: self.remove_units_by_checkbox(selection_window), text='Remove units')
        remove_button.grid(column=1, row=len(checkbuttons))



    def remove_units_by_checkbox(self, window=None):
        ''' Remove all checked units. For internal use only. '''

        if len(self.unit_widgets) == 0:
            return

        index = 0
        while index < len(self.unit_widgets):
            if self.marked_for_delete[index].get():
                self.unit_widgets[index].forget_and_destroy()
                del self.unit_widgets[index]
                del self.marked_for_delete[index]
            else:
                index = index + 1
                
                
        self.health_limit_min = 0
        self.health_limit_max = 0

        for unit_widget in self.unit_widgets:
            self.health_limit_min = min(self.health_limit_min, unit_widget.unit.health_min)
            self.health_limit_max = max(self.health_limit_max, unit_widget.unit.health_max)

        for i in range(0, len(self.unit_widgets)):
            self.unit_widgets[i].new_health_limit(self.health_limit_min, self.health_limit_max)
            self.unit_widgets[i].forget()
            self.unit_widgets[i].grid(0, Unit_Widget.height * i + 1, columnspan=2)
            self.unit_widgets[i].update()

        if window is not None:
            window.destroy()


    
    def start(self):
        ''' Start the window.
            This method calls tkinter.Tk.mainloop().
            Calling this method blocks until the window is closed. '''

        self.root.mainloop()



if __name__ == '__main__':
    import sys
    import os
    
    app = Party_Manager()

    if len(sys.argv) > 1 and sys.argv[1] is not '' and os.path.isdir(sys.argv[1]):
        for filename in os.listdir(sys.argv[1]):
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                unit = Charactersheet_Loader.load_unit(sys.argv[1] + filename)
                app.add_unit(unit.name, unit.classes, unit.levels, unit.health_min, unit.health_max, unit.health_cur)

    app.start()