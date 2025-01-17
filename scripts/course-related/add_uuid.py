import os
import re
import uuid
import sys

sys.dont_write_bytecode = True

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
    
    choix = int(input("Select the number of the file to be modified: ")) - 1
    return os.path.join(parent_dir, fichiers_md[choix])

def lire_fichier_markdown(chemin_md):
    with open(chemin_md, 'r', encoding='utf-8') as fichier:
        return fichier.readlines()

def ecrire_fichier_markdown(chemin_md, lignes):
    with open(chemin_md, 'w', encoding='utf-8') as fichier:
        fichier.writelines(lignes)

def generer_uuid():
    return str(uuid.uuid4())

def ajouter_uuids_si_absents(lignes):
    nouvelles_lignes = []
    i = 0
    uuids_ajoutes = []
    while i < len(lignes):
        ligne = lignes[i]
        nouvelles_lignes.append(ligne)

        if match := re.match(r'^(#+)\s+(.*)', ligne):
            niveau = len(match.group(1))
            titre = match.group(2).strip()
            if niveau == 1:
                balise_id = 'partId'
            elif niveau == 2:
                balise_id = 'chapterId'
            else:
                i += 1
                continue

            if i + 1 < len(lignes) and re.match(rf'^<{balise_id}>.+</{balise_id}>$', lignes[i + 1].strip()):
                nouvelles_lignes.append(lignes[i + 1])
                i += 2
                continue

            nouvel_uuid = generer_uuid()
            nouvelles_lignes.append(f"<{balise_id}>{nouvel_uuid}</{balise_id}>\n")
            uuids_ajoutes.append((titre, nouvel_uuid))
        i += 1

    return nouvelles_lignes, uuids_ajoutes

def main():
    chemin_md = trouver_fichier_markdown()
    if not chemin_md:
        print("No Markdown file found.")
        return

    lignes = lire_fichier_markdown(chemin_md)
    nouvelles_lignes, uuids_ajoutes = ajouter_uuids_si_absents(lignes)
    ecrire_fichier_markdown(chemin_md, nouvelles_lignes)

    if uuids_ajoutes:
        print("Added UUIDs:")
        for titre, nouvel_uuid in uuids_ajoutes:
            print(f"- Title: {titre}, - UUID: {nouvel_uuid}")
    else:
        print("No UUIDs were added.")

if __name__ == "__main__":
    main()
