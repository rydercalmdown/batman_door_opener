import abc
from integrations import pneumatics


class PatternBase(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def pattern(self):
        pass

    @abc.abstractmethod
    def callback(self):
        pass

    @abc.abstractmethod
    def is_active(self):
        return True


class BatmanPattern(PatternBase):

    def pattern(self):
        return [84, 86, 96, 98, 91, 93]

    def callback(self):
        print('Batman Pattern')
        pneumatics.activate()

    def is_active(self):
        return True


def add_patterns(listener):
    """Adds all patterns from patterns.py"""
    pattern_classes = PatternBase.__subclasses__()
    for p_class in pattern_classes:
        p = p_class()
        if p.is_active():
            print('Adding {}'.format(p_class))
            listener.add_pattern(p.pattern(), p.callback)
        else:
            print('Skipping {}'.format(p_class))
