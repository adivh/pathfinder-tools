from unit import Unit
from window import Window



window = Window()

window.add_unit('Walter', ['Druide'], [2], -6, 19, 14)
window.add_unit('Bob', ['Schurke'], [1], -5, 18, -3)
window.add_unit('Hans', ['Magier'], [4], -6, 22, 9)

window.start()