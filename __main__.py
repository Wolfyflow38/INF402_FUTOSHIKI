from typing import Self
from json import loads
from math import log10

class table(object):
    def __init__(self: Self, i: int | str = 5) -> None:
        _t = type(i)
        if _t == int:
            if i > 0:
                self.n = i
                self.values : list[list[int]] = [[0 for m in range(i)] for l in range(i)]
                self.h_sign = [[None for m in range(i)] for l in range(i - 1)]
                self.v_sign = [[None for m in range(i - 1)] for l in range(i)]
                self._s = int(log10(self.n)) + 1 
            else:
                raise ValueError()
        elif _t == str:
            _v = loads(i)
            self.__init__(_v["size"])
            # TODO
        else: # innatteignable
            raise TypeError()
        return None

    def _pad_f(self: Self, to_pad: str) -> str:
        return " " * (self._s - len(to_pad)) + to_pad

    def __repr__(self: Self) -> str:
        rv : list[str] = list((("-" * self._s).join(["|" for i in range(self.n + 1)]) + "\n").join(
            map(lambda _x: _x + "\n", ["", *[
                "|".join(["", *[
                    self._pad_f(str(self.values[x][y]) if self.values[x][y] != 0 else "")
                    for y in range(self.n)
                ], ""]) for x in range(self.n)
            ], ""])
        )[1:])
        h_base_off = 3 + self.n + self._s * self.n + self._s
        h_x_off = 1 + self._s
        h_y_off = 2 * (1 + self.n + self._s * self.n + self._s)
        v_base_off = 2 * (2 + self._s * self.n + self.n) + 1
        v_x_off = 1 + self._s
        v_y_off = 2 * (2 + self._s * self.n + self.n)
        for x in range(self.n):
            for y in range(self.n):
                if y + 1 < self.n:
                    if self.v_sign[x][y] is not None:
                        rv[v_base_off + v_x_off * x + v_y_off * y
                        ] = "v" if self.v_sign[x][y] else "^"
                if x + 1 < self.n:
                    if self.h_sign[x][y] is not None:
                        rv[h_base_off + h_x_off * x + h_y_off * y
                        ] = ">" if self.h_sign[x][y] else "<"
        return "".join(rv)

    __len__ = lambda self: self.n

    __str__ = __repr__

    __int__ = __len__

    __bool__ = lambda self: sum(map(sum, self.values))

    # 0 <= x < n, 0 <= y < n, 0 < v <= n
    def gen_id(self: Self, x: int, y: int, v: int) -> int:
        return x * n * n + y * n + v

    def set_value_at(self: Self, x: int, y: int, v: int | None) -> None:
        if v is None:
            v = 0
        elif not -self.n < v < self.n:
            raise ValueError()
        self.values[x][y] = v        

    def set_v_sign_at(self: Self, x: int, y: int, v: bool | None) -> None:
        self.v_sign[x][y] = v

    def set_h_sign_at(self: Self, x: int, y: int, v: bool | None) -> None:
        self.h_sign[x][y] = v

    def gen_c_clauses() -> list[str]:
        return []

    def gen_v_clauses() -> list[str]:
        return []
        
    def gen_h_clauses() -> list[str]:
        return []
        
    def gen_h_sign_clauses() -> list[str]:
        return []
        
    def gen_v_sign_clauses() -> list[str]:
        return []
        
    def gen_clauses(self: Self) -> list[str]:
        return [
            *gen_c_clauses(),
            *gen_h_clauses(),
            *gen_v_clauses(),
            *gen_h_sign_clauses(),
            *gen_v_sign_clauses()
        ]

    def gen_dimacs(self: Self) -> str:
        cl = self.gen_clauses()
        return "p cnf " + str(self.n ** 3) + str(len(cl)) + "\n" + "\n".join(cl)


if __name__ == '__main__':
    ta = table('{"size":4}')
    ta.set_value_at(0,0,1)
    ta.set_h_sign_at(0,0,True)
    ta.set_h_sign_at(2,3,False)
    ta.set_v_sign_at(3,2,True)
    print(ta)
    pass # TODO