from healthbar import Healthbar



class Unit_Widget:


    def __init__(self, root, health_min, health_max, health_cur, health_limit_min, health_limit_max):
        self.healthbar = Healthbar(root, health_min, health_max, health_cur, health_limit_min, health_limit_max)



    def forget_and_destroy(self):
        ''' Calling this method will hide and destroy all subwidgets.
            This effectively destroys the Unit_Widget. '''

        self.healthbar.forget_and_destroy()



    def grid(self, column, row, columnspan=1):
        ''' This method calls tkinters grid manager to place all subwidgets on the window.
            The Unit_Widget will never exceed the dimensions specified in the method parameters.
            Try calling self.update() if the Unit_Widget is not showing properly. '''

        self.healthbar.grid(column, row, columnspan=columnspan)



    def new_health_limit(self, health_limit_min, health_limit_max):
        ''' Change the health limit on the Unit_Widget's healthbar.
            The health limit is used to scale the healthbar.
            Assigning the same health limits to all Unit_Widgets will cause the healthbars to align on the zero health mark
            and to have the same length per health.
            If the unit's health values {health_min, health_max} are outside the assigned health limit [health_limit_min,health_limit_max],
            the health limit will automatically be extended beyond the specified parameters to fit the entire health bar.
            This may cause healthbars to not align anymore and can be avoided by passing valid health limits. '''

        self.healthbar.new_health_limit(health_limit_min, health_limit_max)



    def update(self):
        ''' Update the entire Unit_Widget. '''

        self.healthbar.update()