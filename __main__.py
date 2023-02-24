# nos fichier, cf : celui qui l'ecrit

from graphique import run_graphique     # contient le mode graphique
from texte import run_texte             # contient le mode texte

# librarie standard, cf : internet

from sys import argv                    # les argument du programe
import argparse                         # lire les arguments du programe


if __name__ == '__main__':
    flag_graph = False
    named_args = dict()
    unnamed_args = tuple()
    # TODO
    # recuperer les argument du program
    main_func = run_graphique if flag_graph else run_texte
    main_func(*unnamed_args, **named_args)
