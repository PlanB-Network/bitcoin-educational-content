import os
from PIL import Image

def parse_input(input_files):
    image_paths = []
    temp_path = ""  # Accumulateur pour les chemins non entourés de guillemets
    in_quotes = False  # Indicateur pour savoir si on est à l'intérieur de guillemets

    for part in input_files.split(' '):
        if part.startswith('"'):
            in_quotes = True
            temp_path += part[1:]  # Enlever le guillemet de début
        elif part.endswith('"'):
            if in_quotes:
                # Ajouter à la liste le chemin complet entre guillemets
                image_paths.append(temp_path + " " + part[:-1])  # Enlever le guillemet de fin
                temp_path = ""  # Réinitialiser pour le prochain chemin
                in_quotes = False
            else:
                # Gérer un cas où un chemin se termine par un guillemet sans commencer par un
                temp_path += " " + part
                image_paths.append(temp_path)
                temp_path = ""
        elif in_quotes:
            # Accumuler les parties du chemin entre guillemets
            temp_path += " " + part
        else:
            # Ajouter directement les chemins sans guillemets
            image_paths.append(part)

    # Gérer le cas où le dernier élément n'est pas suivi d'un guillemet
    if temp_path:
        image_paths.append(temp_path)

    return image_paths

def convert_to_webp(image_paths):
    for image_path in image_paths:
        image_path = image_path.strip()  # Nettoyer les espaces blancs éventuels
        if not os.path.isfile(image_path):
            print(f"Le fichier {image_path} n'existe pas.")
            continue

        with Image.open(image_path) as image:
            image_output_path = os.path.splitext(image_path)[0] + '.webp'
            image.save(image_output_path, 'WEBP')
            print(f"{image_path} a été converti en {image_output_path}.")

        os.remove(image_path)
        print(f"{image_path} a été supprimé.")

if __name__ == "__main__":
    input_files = input("Drag and drop ! (formats : .png, .jpeg, .jpg) : ")
    image_paths = parse_input(input_files)
    convert_to_webp(image_paths)