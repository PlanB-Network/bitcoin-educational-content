import os
import re

def trouver_fichier_markdown():
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    fichiers_md = [f for f in os.listdir(parent_dir) if f.endswith(".md")]
    
    if not fichiers_md:
        return None
    
    if len(fichiers_md) == 1:
        return os.path.join(parent_dir, fichiers_md[0])
    
    print("Multiple Markdown files found:")
    for idx, fichier in enumerate(fichiers_md):
        print(f"{idx + 1}. {fichier}")
    
    choix = int(input("Select the number of the file to be used as a source: ")) - 1
    return os.path.join(parent_dir, fichiers_md[choix])

def lire_titres(fichier_md):
    titres = []
    current_part = None
    current_chapter = None
    current_uuid = None

    with open(fichier_md, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            if match := re.match(r'^(#+)\s+(.*)', ligne):
                niveau = len(match.group(1))
                titre = match.group(2).strip()
                if niveau == 1:
                    current_part = titre
                    current_uuid = None
                elif niveau == 2:
                    current_chapter = titre
                    current_uuid = None
                titres.append((niveau, titre, current_uuid))
            elif match := re.match(r'^<(.+Id)>(.+)</\1>$', ligne):
                current_uuid = match.group(2).strip()
                if current_part and not current_chapter:
                    titres[-1] = (titres[-1][0], titres[-1][1], current_uuid)
                elif current_chapter:
                    titres[-1] = (titres[-1][0], titres[-1][1], current_uuid)
                current_uuid = None

    return titres

def ecrire_plan(titres, fichier_plan):
    with open(fichier_plan, 'w', encoding='utf-8') as fichier:
        dernier_niveau = 0
        num_partie = -1
        num_chapitre = 0
        for niveau, titre, uuid in titres:
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
            if uuid:
                fichier.write(f"{prefixe}{titre} ({uuid})\n")
            else:
                fichier.write(f"{prefixe}{titre}\n")
            dernier_niveau = niveau

def main():
    chemin_md = trouver_fichier_markdown()
    if not chemin_md:
        print("No Markdown file found.")
        return

    chemin_plan = os.path.join(os.path.dirname(chemin_md), "plan.txt")
   
    titres = lire_titres(chemin_md)
    
    ecrire_plan(titres, chemin_plan)

    print("plan.txt created!")

if __name__ == "__main__":
    main()
