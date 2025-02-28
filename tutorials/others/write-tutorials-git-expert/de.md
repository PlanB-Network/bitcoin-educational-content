---
name: Beitrag - Git-Tutorial (Fortgeschrittene)
description: Leitfaden für fortgeschrittene Benutzer, der ein Tutorial zu Plan ₿ Network mit Git bietet
---
![cover](assets/cover.webp)

Bevor Sie dieses Tutorial zum Hinzufügen eines neuen Tutorials lesen, müssen Sie einige vorbereitende Schritte durchgeführt haben. Falls Sie dies noch nicht getan haben, sehen Sie sich bitte zuerst dieses einführende Tutorial an und kommen Sie dann hierher zurück:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Sie haben bereits :


- Wählen Sie ein Thema für Ihr Lernprogramm;
- Kontaktieren Sie das Plan ₿ Network Team über [Telegram group] (https://t.me/PlanBNetwork_ContentBuilder) oder paolo@planb.network;
- Wählen Sie Ihre Beitragstools.

In diesem Tutorial für erfahrene Git-Nutzer fassen wir kurz die wichtigsten Schritte und Richtlinien für das Anbieten eines neuen Plan ₿ Network Tutorials zusammen. Wenn Sie mit Git und GitHub nicht vertraut sind, empfehle ich Ihnen, stattdessen eines dieser beiden anderen, ausführlicheren Tutorials zu lesen, die Sie Schritt für Schritt begleiten:


- Fortgeschrittene (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Anfänger (Webschnittstelle)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Empfohlene Werkzeuge

Zur Bearbeitung von Markdown-Dateien :


- Obsidian** (kostenlos, nicht quelloffen)
- Mark Text** (kostenlos, Open-Source)
- Zettlr** (kostenlos, Open-Source)
- Typora** (Payware, ~€15, nicht Open-Source)

Für Git :


- Git** (kostenlos, Open-Source)
- GitHub Desktop** (kostenlos, Open-Source)
- Sourcetree** (kostenlos, nicht Open-Source)

Zur Bearbeitung von YAML-Dateien :


- Visual Studio Code** (kostenlos, Open-Source)
- Sublime Text** (kostenlos mit Einschränkungen, nicht Open-Source)

Erstellen von Diagrammen und visuellen Darstellungen :


- Canva** (kostenlos mit kostenpflichtigen Optionen, nicht Open-Source)
- Inkscape** (Kostenlos, Open-Source)
- Penpot** (kostenlos, Open-Source)

## Arbeitsabläufe

### 1 - Konfigurieren Sie Ihre lokale Umgebung


- Sie müssen Ihren eigenen Fork des [Plan ₿ Network Repository auf GitHub] (https://github.com/PlanB-Network/bitcoin-educational-content) haben.
- Synchronisieren Sie den Hauptzweig (`dev`) Ihrer Abspaltung mit dem Quell-Repository.
- Aktualisieren Sie Ihren lokalen Klon.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - Einen neuen Zweig erstellen


- Vergewissern Sie sich, dass Sie auf dem `dev`-Zweig sind.
- Erstellen Sie einen neuen Zweig mit einem beschreibenden Namen (z.B. `tuto-green-wallet-loic`).
- Veröffentlichen Sie diesen Zweig in Ihrem Online-Zweig.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Fügen Sie die Dokumente des Tutorials hinzu

***Hinweis:*** Sie können die Schritte 3 und 4 mit [meinem Python-GUI-Skript] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation) automatisieren. Führen Sie das Skript direkt aus seinem Ordner in Ihrem lokalen Klon aus und füllen Sie dann die erforderlichen Felder in der grafischen Benutzeroberfläche aus. Weitere Informationen zur Installation und Verwendung des Skripts finden Sie in der [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Wenn Sie es lieber manuell machen möchten, folgen Sie diesen Schritten:


- Suchen Sie den entsprechenden Ordner im lokalen Repository (z. B. `tutorials/wallet`).
- Erstellen Sie ein Verzeichnis für das Tutorial mit einem eindeutigen Namen (z. B. `green-wallet`). Dieser Ordnername bestimmt auch den URL-Pfad des Tutorials. Er sollte in Kleinbuchstaben geschrieben sein, keine Sonderzeichen (außer Bindestrichen) und keine Leerzeichen enthalten.
- Fügen Sie die folgenden Elemente zu diesem Verzeichnis hinzu:
    - Ein Unterordner mit dem Namen `assets`, der :
        - Zwei `.webp`-Bilder:
            - logo.webp": Das Logo des Tutorials (quadratisches Format mit Hintergrund). Dieses Logo muss die vorgestellte Software oder das Werkzeug repräsentieren. Wenn das Tutorial nicht spezifisch für ein Tool ist (z.B.: ein allgemeiner Leitfaden für die Erstellung einer mnemonischen Phrase), können Sie ein geeignetes Bild auswählen (z.B.: ein allgemeines Symbol).
            - cover.webp": Ein Titelbild, das zu Beginn des Tutorials angezeigt wird.
        - Ein Unterordner mit dem Code der Originalsprache des Tutorials. Wenn das Lernprogramm z. B. in Englisch verfasst ist, sollte dieser Unterordner "de" heißen. Legen Sie alle visuellen Elemente des Tutorials (Diagramme, Bilder, Screenshots usw.) in diesem Ordner ab.
    - Eine "tutorial.yml"-Datei mit Metadaten (Autor, Tags, Kategorie, Schwierigkeitsgrad usw.).
    - Eine Markdown-Datei mit dem Tutorial, benannt nach dem Sprachcode (z.B. `fr.md`, `en.md`, etc.).

```bash
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - Ausfüllen der YAML-Datei


- Vervollständigen Sie die Datei `tutorial.yml` wie folgt:

```yaml
id:
project_id:
tags:
-
-
-
category:
level:
credits:
professor:
# Proofreading metadata
original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributors_id:
-
reward:
````
Voici le détail des champs obligatoires :
- **id** : Un UUID (_Universally Unique Identifier_) permettant d’identifier de manière unique le tutoriel. Vous pouvez le générer avec [un outil en ligne](https://www.uuidgenerator.net/version4). La seule contrainte est que cet UUID soit aléatoire pour ne pas avoir de conflit avec un autre UUID sur la plateforme ;
- **project_id** : L'UUID de l’entreprise ou de l’organisation derrière l’outil présenté dans le tutoriel [depuis la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, si vous réalisez un tutoriel sur le logiciel Green Wallet, vous pouvez trouver ce `project_id` dans le fichier suivant : `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Cette information est ajoutée dans le fichier YAML de votre tutoriel parce que Plan ₿ Network maintient une base de données de toutes les entreprises et organisations opérant sur Bitcoin ou des projets connexes. En ajoutant le `project_id` de l'entité liée à votre tutoriel, vous créez un lien entre les deux éléments ;
- **tags** : 2 ou 3 mots-clés pertinents liés au contenu du tutoriel, choisis exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ;
- **category** : La sous-catégorie correspondant au contenu du tutoriel, selon la structure du site Plan ₿ Network (par exemple pour les wallets : `desktop`, `hardware`, `mobile`, `backup`) ;
- **level** : Le niveau de difficulté du tutoriel, parmi :
- `beginner`
- `intermediate`
- `advanced`
- `expert`
- **professor** : Votre `contributor_id` (mots BIP39) tel qu'affiché sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) ;
- **original_language** : La langue d’origine du tutoriel (par exemple `fr`, `en`, etc.) ;
- **proofreading** : Informations sur le processus de relecture. Remplissez la première partie, car la relecture de votre propre tutoriel compte comme une première validation :
- **language** : Code de langue de la relecture (par exemple `fr`, `en`, etc.).
- **last_contribution_date** : Date du jour.
- **urgency** : Laissez vide.
- **contributors_id** : Votre ID GitHub.
- **reward** : Laissez vide.
Pour davantage de détails sur votre identifiant de professeur, reportez-vous au tutoriel correspondant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
```

id: e84edaa9-fb65-48c1-a357-8a5f27996143

projekt_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:


  - geldbörsen
  - software
  - tasten

kategorie: Handy

niveau: Anfänger

kredite:

professor: ziemlich-privat

# Korrekturlesen von Metadaten

original_language: fr

korrekturlesen:


  - sprache: fr

last_contribution_date: 2024-11-20

dringlichkeit:

mitwirkende_id:


      - LoicPandul

belohnung:

```
### 5 - Rédigez le contenu
- Complétez les propriétés du fichier Markdown avec :
- Le titre (`name`).
- Une courte description (`description`).
- Ajoutez l’image de couverture en haut du tutoriel avec la syntaxe Markdown (remplacez "green" par le nom de l’outil présenté) :
```

![cover-green](assets/cover.webp)

```
- Rédigez le contenu du tutoriel en Markdown :
- Utilisez des titres bien structurés (`##`), des listes et des paragraphes.
- Insérez des visuels avec la syntaxe Markdown :
```

![nom-image](assets/en/001.webp)

```
- Placez les schémas et images dans le sous-dossier de langue correspondant, dans `/assets`.
### 6 - Enregistrez et soumettez le tutoriel
- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.
```

# Erstellen Sie eine Übergabe mit einer beschreibenden Nachricht

git commit -m "Tutorial zur grünen Geldbörse hinzufügen"

# Schieben Sie Ihre Änderungen auf Ihre Gabel

git push origin tuto-grün-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Erstellen Sie einen Commit, der die vorgenommenen Korrekturen beschreibt

git commit -m "Korrekturen nach Überprüfung des Green-Wallet-Tutorials"

# Korrekturen auf der Gabel drücken

git push origin tuto-grün-wallet-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("Hallo, Bitcoin!")

```