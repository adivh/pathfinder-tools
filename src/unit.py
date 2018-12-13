class Unit:


    def __init__(self, health_min, health_max, health_cur):
        # Assign health values guaranteeing the following properties:
        #   - self.health_min is always negative
        #   - self.health_max is always positive
        #   - self.health_cur is always in [self.health_min, self.health_max]

        self.health_min = min(health_min, -health_min)
        self.health_max = max(health_max, -health_max)
        self.health_cur = min(max(health_cur, self.health_min), self.health_max)