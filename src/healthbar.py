from tkinter import ttk

class Healthbar:
    

    def __init__(self, root, health_cur, health_max, health_min):

        if health_max <= 0:
            raise ValueError("health_max = " + str(health_max))

        _cur = health_cur
        _max = health_max
        _min = health_min

        if _min > 0:
            _min = -_min

        if _cur > _max:
            _cur = _max

        if _cur < _min:
            _cur = _min

        self.positive = ttk.Progressbar(root, maximum = _max, value=_cur if _cur > 0 else 0)
        self.negative = ttk.Progressbar(root, maximum = -_min, value=-_cur if _cur < 0 else 0)


#        if _cur > 0:
#            self.positive.step(_cur)
#        else:
#            self.negative.step(-_cur)


    def forget_and_destroy(self):
        self.positive.grid_forget()
        self.positive.destroy()
        self.negative.grid_forget()
        self.negative.destroy()


    def grid(self, column, row):
        self.negative.grid(column=column, row=row)
        self.positive.grid(column=column+1, row=row, columnspan=2)