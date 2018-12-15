from tkinter import ttk

from unit import Unit



class Unit_Identifier:



    def __init__(self, parent):
        self.parent = parent
        self.label = ttk.Label(parent.parent, text=parent.unit.unit_identifier())


    
    def forget_and_destroy(self):
        ''' Hide the Unit_Identifier and destroy it. '''

        self.label.grid_forget()
        self.label.destroy()


    
    def grid(self, column, row, columnspan=1):
        ''' Place the Unit_Identifier. '''

        self.label.grid(sticky='w', column=column, row=row, columnspan=columnspan)



    def update(self):
        ''' Update the Unit_Identifier. '''

        self.label.config(text=self.parent.unit.unit_identifier())