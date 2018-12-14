class Unit:



    def __init__(self, name, classes, levels, health_min, health_max, health_cur):
        ''' name: string, classes: [string], levels: [int], health_min,health_max,health_cur: int '''

        self.name = name
        self.classes = classes
        self.levels = levels
        
        # Assign health values guaranteeing the following properties:
        #   - self.health_min is always negative
        #   - self.health_max is always positive
        #   - self.health_cur is always in [self.health_min, self.health_max]

        self.health_min = min(health_min, -health_min)
        self.health_max = max(health_max, -health_max)
        self.health_cur = min(max(health_cur, self.health_min), self.health_max)
    


    def unit_identifier(self):
        res = self.name + ' |'
        for i in range(0, len(self.classes)):
            res = res + ' ' + str(self.classes[i]) + ' ' + str(self.levels[i])
        return res
