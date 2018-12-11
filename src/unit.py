class Unit:

    def __init__(self, health_cur, health_max, health_min):
        self.health_cur = 0 if (health_cur <= 0) else (health_cur if (health_cur <= health_max) else health_max)
        self.health_max = health_max
        self.health_min = health_min if (health_min < 0) else 0