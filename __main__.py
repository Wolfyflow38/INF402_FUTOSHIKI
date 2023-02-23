from typeing import Union
from json import loads

class table(object):
    def __init__(self, i: Union[int, str] = 5):
        _t = i.__class__
        if _t == int:
            if i > 0:
                pass # l'argument est un entier
            else:
                raise ValueError()
        elif _t == str:
            _v = loads(i)
            self.__init__(_v["size"])
            # TODO
        else:
            raise TypeError()

if __name__ == '__main__':
    pass # TODO