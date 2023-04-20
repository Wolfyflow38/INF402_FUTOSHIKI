# nos fichier, cf : celui qui l'ecrit

from table import table

# librarie standard, cf : internet

from sys import stdout, stdin
from _io import TextIOWrapper

def run_texte(ta: table) -> int:
    """
    fonction principale en mode textuel
    """
    if ta is None:
        while True:
            try:
                c = int(input("taille?"))
                ta = table('{"size": %d}' % c)
            except:
                continue
            else:
                break
    if __debug__:
            assert(ta is not None)
    while True:
        cmd = " ".join(filter(None, input("?").split()))

#    ta.set_value_at(0, 0, 1)
#    ta.set_h_sign_at(0, 0, True)
#    ta.set_h_sign_at(1, 0, True)
#    ta.set_h_sign_at(0, 1, True)
#    ta.set_h_sign_at(2, 3, False)
#    ta.set_v_sign_at(3, 2, True)
#    print(ta)
    print(ta.gen_dimacs())
    return 0
