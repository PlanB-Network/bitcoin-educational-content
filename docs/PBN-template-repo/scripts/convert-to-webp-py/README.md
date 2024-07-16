# Image to WEBP Converter
**UPDATE:** I've made a complete program for local image conversion with a GUI that's easier to use than this script, supports more formats, and automatically removes unnecessary metadata from images. You can test it here on the repo: https://github.com/LoicPandul/ImagesConverter

**MISE À JOUR :** J'ai fait un logiciel complet pour la conversion d'image en local avec une GUI plus simple à utiliser que ce script, qui prend en charge plus de formats, et qui supprime automatiquement les métadonnées inutiles des images. Je vous conseille de le tester ici sur son repo : https://github.com/LoicPandul/ImagesConverter

---

EN : This little python script converts PNG, JPEG and JPG images into WEBP images. You can use it to quickly convert visuals and diagrams for your PlanB Network tutorials. The WEBP format allows you to reduce the size of your assets. The script converts the file and then deletes the source file automatically.

FR : Ce petit script python convertit les images PNG, JPEG et JPG en images WEBP. Vous pouvez l'utiliser pour convertir rapidement des visuels et des schémas pour vos tutoriels PlanB Network. Le format WEBP vous permet de réduire la taille de vos images. Le script convertit le fichier et supprime ensuite automatiquement le fichier source.

## Requirements

- Python 3
- Pillow

## EN - Installation

1. Navigate to the `convert_to_webp.py` file in the GitHub web interface ;
2. Click on the file to open it ;
3. Above the file's content, click on the `Download raw file` arrow to download the script.

To install the dependencies, run:
```
pip install Pillow
```

## FR - Installation

1. Naviguez jusqu'au fichier `convert_to_webp.py` dans l'interface web de GitHub ;
2. Cliquez sur le fichier pour l'ouvrir ;
3. Au-dessus du contenu du fichier, cliquez sur la flèche `Download raw file` pour télécharger le script.

Pour installer les dépendances, exécutez dans un terminal :
```
pip install Pillow
```

## EN - Usage

To use the script, open a terminal in the folder where `convert_to_webp.py` is located and execute:

```
python convert_to_webp.py
```

Drag and drop your image files onto the terminal where the script is being executed, then follow the on-screen instructions. You can drop multiple images at once. Press `enter` to execute.

## FR - Usage

Pour utiliser le script, ouvrez un terminal dans le dossier où se trouve `convert_to_webp.py` et exécutez :
```
python convert_to_webp.py
```

Glissez et déposez vos fichiers image sur le terminal où le script est exécuté, puis suivez les instructions à l'écran. Vous pouvez déposer plusieurs images en même temps. Tapez `entrer` pour exécuter.