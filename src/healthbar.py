from tkinter import Canvas

class Healthbar:
    


    def __init__(self, root, health_min, health_max, health_cur, health_limit_min, health_limit_max):

        # Assign health values guaranteeing the following properties:
        #   - self.health_min is always negative
        #   - self.health_max is always positive
        #   - self.health_cur is always in [self.health_min, self.health_max]

        self.health_min = min(health_min, -health_min)
        self.health_max = max(health_max, -health_max)
        self.health_cur = min(max(health_cur, self.health_min), self.health_max)

        # Assign health limits.
        # Health limits are used for scaling and are adjusted to fit the health values.

        self.health_limit_min = min(self.health_min, health_limit_min)
        self.health_limit_max = max(self.health_max, health_limit_max)

        # Configure health bar dimensions here!

        self.width = 200
        self.height = 20
        self.step = self.width / (self.health_limit_max - self.health_limit_min)
        
        # Create a canvas for the health bar.

        self.background = Canvas(root, width=self.width, height=self.height)

    

    def forget_and_destroy(self):
        ''' Hide the healthbar and destroy it. '''
        
        self.background.grid_forget()
        self.background.destroy()



    def grid(self, column, row, columnspan=1):
        ''' Place the healthbar and draw it. '''

        self.background.grid(column=column, row=row, columnspan=columnspan)
        self.update()



    def new_health_limit(self, health_limit_min, health_limit_max):
        ''' Assign health limits for scaling purposes.
            Health limits will always be readjusted to guarantee {self.health_min, self.health_max} are inside of [health__limit_min, health_limit_max]. '''

        self.health_limit_min = min(self.health_min, health_limit_min)
        self.health_limit_max = max(self.health_max, health_limit_max)
        self.step = self.width / (self.health_limit_max - self.health_limit_min)

    

    def update(self):
        ''' Update the health bar.
            Updating causes health bar rectangles to be deleted.
            If self.health_cur is not 0, they will be drawn again to correctly represent the current health value. '''

        _cur = self.step * (self.health_cur - self.health_limit_min)
        _zero = self.step * -self.health_limit_min
        _min = self.step * (self.health_min - self.health_limit_min)
        _max = self.step * (self.health_max - self.health_limit_min)

        self.background.delete('all')

        if self.health_cur < 0:
            self.background.create_rectangle(_cur, self.height * 0.5 - 1, _max, self.height * 0.5 + 1, outline='magenta4', fill='magenta4')
            self.background.create_rectangle(_min, 0, _cur, self.height, fill='grey10')
            self.background.create_rectangle(_cur, 0, _zero, self.height, fill='magenta4')
        
        elif self.health_cur > 0:
            self.background.create_rectangle(_cur, self.height * 0.5 - 1, _max, self.height * 0.5 + 1, outline='black', fill='white')
            self.background.create_rectangle(_min, 0, _zero, self.height, fill='grey10')
            self.background.create_rectangle(_zero, 0, _cur, self.height, fill='royal blue')
        
        else:
            self.background.create_rectangle(_cur, self.height * 0.5 - 1, _max, self.height * 0.5 + 1, outline='black', fill='black')
            self.background.create_rectangle(_min, 0, _zero, self.height, fill='grey10')


        