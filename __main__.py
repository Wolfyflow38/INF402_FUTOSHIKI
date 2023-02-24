# nos fichier, cf : celui qui l'ecrit
from graphique import run_graphique     # contient le mode graphique
from texte import run_texte             # contient le mode texte
# librarie standard, cf : internet
from sys import argv                    # les argument du programe
import argparse                         # lire les arguments du programe

if __name__ == '__main__':
    flag_graph = False
    # TODO
    # recuperer les argument du program
    if flag_graph:
        run_graphique(output = None, input = None)
    else:
        run_texte(output = None, input = None)

