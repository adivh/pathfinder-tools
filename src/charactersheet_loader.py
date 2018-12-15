import yaml

from unit import Unit


class Charactersheet_Loader:



    @staticmethod
    def load_unit(path):
        with open(path, 'r') as stream:
            try:
                _data = yaml.load(stream)
            except:
                raise ValueError('Failed to load ' + path)
        
        _classes = []
        _levels = []

        for _class in _data['classes']:
            for classname in _class:
                _classes.append(classname)
                _levels.append(_class[classname])

        return Unit(_data['name'], _classes, _levels, int(_data['stats'][0]['health_min']), int(_data['stats'][1]['health_max']), int(_data['stats'][2]['health_cur']))