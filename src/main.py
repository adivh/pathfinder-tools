import os

from charactersheet_loader import Charactersheet_Loader
from unit import Unit
from window import Window



window = Window()

for filename in os.listdir('../chars'):
    if filename.endswith('.yaml'):
        unit = Charactersheet_Loader.load_unit('../chars/' + filename)
        window.add_unit(unit.name, unit.classes, unit.levels, unit.health_min, unit.health_max, unit.health_cur)

window.start()