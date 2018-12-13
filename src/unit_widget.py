from healthbar import Healthbar



class Unit_Widget:


    def __init__(self, root, health_min, health_max, health_cur, health_limit_min, health_limit_max):
        self.healthbar = Healthbar(root, health_min, health_max, health_cur, health_limit_min, health_limit_max)



    def forget_and_destroy(self):
        self.healthbar.forget_and_destroy()



    def grid(self, column, row):
        self.healthbar.grid(column, row)



    def new_health_limit(self, health_limit_min, health_limit_max):
        self.healthbar.new_health_limit(health_limit_min, health_limit_max)



    def update(self):
        self.healthbar.update()