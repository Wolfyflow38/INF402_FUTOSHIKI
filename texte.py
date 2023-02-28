# nos fichier, cf : celui qui l'ecrit

from table import table

# librarie standard, cf : internet

from sys import stdout, stdin
from _io import TextIOWrapper

"""

"""
def run_texte(input_file : TextIOWrapper, output_file : TextIOWrapper) -> int:
    ta = table('{"size": 10}')
    ta.set_value_at(0, 0, 1)
    ta.set_h_sign_at(0, 0, True)
    ta.set_h_sign_at(1, 0, True)
    ta.set_h_sign_at(0, 1, True)
    ta.set_h_sign_at(2, 3, False)
    ta.set_v_sign_at(3, 2, True)
#    print(ta)
    print(ta.gen_dimacs())
    return 0
