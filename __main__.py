# nos fichier, cf : celui qui l'ecrit

from graphique import run_graphique     # contient le mode graphique
from texte import run_texte             # contient le mode texte

# librarie standard, cf : internet

import sys                              # les argument du programe
import argparse                         # lire les arguments du programe


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Futoshiki solver")

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('-t', '--text', action='store_false', dest='flag_graph')
    mode.add_argument('-g', '--graphic', action='store_true', dest='flag_graph')
    
    
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args()

    main_func = run_graphique if args.flag_graph else run_texte

    main_func(input_file=args.infile, output_file=args.outfile)
