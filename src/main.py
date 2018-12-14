from unit import Unit
from window import Window



window = Window()

window.add_unit('Günther', ['Magier'], [4], -6, 22, 9)
window.add_unit('Walterine', ['Druide'], [2], -7, 19, -3)
window.add_unit('Bob', ['Paladin'], [1], -5, 18, 14)
window.add_unit('Haralda', ['Schurke'], [3], -6, 15, 15)

window.start()