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
 
c=input("entrez la longueur d'un côté")

for x in range(0,c,1):
    for y in range(0,c,1) :
        flag=input("valeur ou signe ? v/s/n")
        if flag=="v":
            print("choisissez une valeur entre 1 et ",c,"\n")
            val=input("entrez la valeur")
            ta.set_value_at(x, y, val) 
        elsif flag=="s" and x+2<=c :
            si=input("lignes ou colonnes ? l/c")
            if si==l :
                print("> ou < ou None \n")
                si_flag=input("sup/inf/N") 
                if si_flag=="sup":
                ta.set_h_sign_at(x, y, True)
                elsif si_flag=="inf":
                ta.set_h_sign_at(x, y, False)    
            elsif si==c and y+2<=c :
                print("> ou < ou None \n")
                si_flag=input("sup/inf/N") 
                if si_flag=="sup":
                    ta.set_h_sign_at(x, y, True)
                elsif si_flag=="inf":
                    ta.set_h_sign_at(x, y, False)
                
#    ta.set_h_sign_at(0, 0, True) => signe horizontal : case 0,0> 1,0 => limite x=c-2
#    ta.set_h_sign_at(1, 0, True) => 1,0 > 2.0
#    ta.set_h_sign_at(0, 1, True)
#    ta.set_h_sign_at(2, 3, False)
#    ta.set_v_sign_at(3, 2, True) => y_lim=c-2
#    print(ta)
    print(ta.gen_dimacs())
    return 0
