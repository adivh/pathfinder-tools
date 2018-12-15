from charactersheet_loader import Charactersheet_Loader

unit = Charactersheet_Loader.load_unit('../chars/bob.yaml')
if unit is not None:
    unit.debug()