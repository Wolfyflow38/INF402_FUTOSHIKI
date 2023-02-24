from graphique import run_graphique
from table import table


if __name__ == '__main__':
    ta = table('{"size": 10}')
    ta.set_value_at(0, 0, 1)
    ta.set_h_sign_at(0, 0, True)
    ta.set_h_sign_at(1, 0, True)
    ta.set_h_sign_at(0, 1, True)
    ta.set_h_sign_at(2, 3, False)
    ta.set_v_sign_at(3, 2, True)
    print(ta)
    print(ta.gen_dimacs())
    flag_graph = False
    if flag_graph:
        run_graphique(output = None, input = None)
    elif:
        pass # TODO: Mode texte
