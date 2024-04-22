import re

def lire_titres(fichier_md):
    titres = []
    with open(fichier_md, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            if match := re.match(r'^(#+)\s+(.*)', ligne):
                niveau = len(match.group(1))
                titre = match.group(2).strip()
                titres.append((niveau, titre))
    return titres

def ecrire_plan(titres, fichier_plan):
    with open(fichier_plan, 'w', encoding='utf-8') as fichier:
        dernier_niveau = 0
        num_partie = -1
        num_chapitre = 0
        for niveau, titre in titres:
            if niveau == 1:
                num_partie += 1
                num_chapitre = 0
                prefixe = f"Partie {num_partie} - "
            elif niveau == 2:
                num_chapitre += 1
                prefixe = f"    Chapitre {num_chapitre} - "
            else:
                prefixe = '    ' * (niveau - 1) + '| '
            
            if niveau == 1 and dernier_niveau != 0:
                fichier.write('\n')
            fichier.write(f"{prefixe}{titre}\n")
            dernier_niveau = niveau

def main():
    chemin_md = "../fr.md"
    chemin_plan = "../plan.txt"
   
    titres = lire_titres(chemin_md)
    
    ecrire_plan(titres, chemin_plan)

    print("Plan créé !")

if __name__ == "__main__":
    main()
