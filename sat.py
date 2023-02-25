from subprocess import run
from collections.abc import Callable
from tempfile import mkstemp
from os import close, fdopen, remove

solver_data: dict[str, Callable[[str], str]] = {}

def get_solver(sat: str):
    return solver_data[sat]

def solve(dimacs : str, sat: str = "minisat") -> str:
    return get_solver(sat)(dimacs)

def solver(func: Callable[[str], str]):
    solver_data[func.__name__] = func

@solver
def minisat(dimacs : str) -> str:
    fd_in, path_in = mkstemp(text=True)
    f_in = fdopen(fd_in)
    f_in.write(dimacs)
    f_in.close()
    fd_out, path_out = mkstemp(text=True)
    close(fd_out)
    v = run(["minisat", path_in, path_out])
    code = v.returncode
    remove(path_in)
    rv = ""
    if code == 10:
        with open(path_out, "r") as f:
            rv = f.read(None)
        remove(path_out)
        return rv
    else:
        remove(path_out)
        raise ValueError()
        