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

In diesem Tutorial für erfahrene Git-Benutzer fassen wir kurz die wichtigsten Schritte und Richtlinien für das Anbieten eines neuen Plan ₿ Network Tutorials zusammen. Wenn Sie mit Git und GitHub nicht vertraut sind, empfehle ich Ihnen, stattdessen eines dieser beiden anderen, detaillierteren Tutorials zu besuchen, die Sie Schritt für Schritt führen:


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

```
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

```
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

```
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

```
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
```

Hier sind die erforderlichen Felder:


- id**: Eine UUID (_Universally Unique Identifier_) zur eindeutigen Identifizierung des Lernprogramms. Sie können sie mit [einem Online-Tool] (https://www.uuidgenerator.net/version4) erzeugen. Die einzige Einschränkung ist, dass diese UUID zufällig sein muss, damit sie nicht mit einer anderen UUID auf der Plattform kollidiert;
- project_id** : Die UUID des Unternehmens oder der Organisation, die hinter dem im Tutorium vorgestellten Tool steht [aus der Liste der Projekte] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Wenn Sie zum Beispiel ein Tutorial über die Green Wallet Software machen, können Sie diese `project_id` in der folgenden Datei finden: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Diese Information wird in der YAML-Datei Ihres Tutorials hinzugefügt, weil das Plan ₿ Network eine Datenbank aller Unternehmen und Organisationen unterhält, die an Bitcoin oder verwandten Projekten arbeiten. Indem Sie die `project_id` der verlinkten Entität zu Ihrem Tutorial hinzufügen, schaffen Sie eine Verbindung zwischen den beiden Elementen;
- tags**: 2 oder 3 relevante Schlüsselwörter, die sich auf den Inhalt des Tutorials beziehen und ausschließlich [aus der Tag-Liste des Plan ₿ Network] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ausgewählt werden;
- kategorie** : Die Unterkategorie, die dem Inhalt des Tutorials entspricht, gemäß der Plan ₿ Netzwerkstruktur (z.B. für Wallets: `Desktop`, `Hardware`, `Mobile`, `Backup`) ;
- stufe** : Schwierigkeitsgrad des Tutorials, von :
    - anfängerin
    - mittel
    - fortgeschritten
    - experte
- professor**: Ihre "contributor_id" (BIP39-Wörter), wie sie auf [Ihr Lehrerprofil] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) angezeigt wird;
- original_language** : Die Originalsprache des Tutorials (z.B. `fr`, `en`, etc.) ;
- korrekturlesen**: Informationen über den Korrekturleseprozess. Füllen Sie den ersten Teil aus, denn das Korrekturlesen Ihres eigenen Tutoriums zählt als erste Validierung:
    - sprache**: Korrekturlesen von Sprachcodes (z. B. `fr`, `en`, usw.).
    - letzter_Beitrag_datum**: Das heutige Datum.
    - dringlichkeit** : Leer lassen.
    - contributors_id** : Ihre GitHub-ID.
    - belohnung** : Leer lassen.

Weitere Einzelheiten zu Ihrer Lehrer-ID finden Sie in der entsprechenden Anleitung:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
```
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
```

### 5 - Schreiben Sie den Inhalt


- Füllen Sie die Eigenschaften der Markdown-Datei mit :
    - Der Titel (`Name`).
    - Eine kurze Beschreibung (`description`).
- Fügen Sie das Titelbild am Anfang des Tutorials mit Hilfe der Markdown-Syntax hinzu (ersetzen Sie "grün" durch den Namen des abgebildeten Tools):

```
![cover-green](assets/cover.webp)
```


- Schreiben Sie den Inhalt des Tutorials in Markdown:
    - Verwenden Sie gut gegliederte Überschriften (`##`), Listen und Absätze.
    - Einfügen von Bildmaterial mit der Markdown-Syntax :

```
![nom-image](assets/en/001.webp)
```


- Legen Sie die Diagramme und Bilder in den entsprechenden Unterordner der Sprache in `/assets`.

### 6 - Speichern und Absenden des Tutorials


- Speichern Sie Ihre Änderungen lokal, indem Sie eine Übergabe mit einer beschreibenden Nachricht erstellen.
- Übertragen Sie die Änderungen auf Ihren GitHub-Fork.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Sobald Sie fertig sind, erstellen Sie einen Pull Request (PR) auf GitHub, um die Integration Ihrer Änderungen vorzuschlagen.
- Fügen Sie dem PR einen Titel und eine kurze Beschreibung hinzu. Geben Sie im Kommentar die entsprechende Nummer der Ausgabe an.

### 7 - Korrekturlesen und Zusammenführen


- Warten Sie auf die Bestätigung oder Rückmeldung durch einen Administrator.
- Falls erforderlich, nehmen Sie Korrekturen vor und veröffentlichen Sie neue Commits.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Sobald der PR zusammengeführt worden ist, können Sie Ihren Arbeitszweig löschen.

## Standards für die Erstellung von Inhalten


- Von der Plattform unterstützte Formatierung** :
    - Klassisches Markdown: Listen, Links, Bilder, Zitate, Fett- und Kursivdruck usw.
    - LaTeX (nur Block, nicht Inline): abgegrenzt durch `$$`.
    - Inline-Code: Syntax mit einem einzigen Backtick.
    - Code-Blöcke: Syntax mit drei Backticks, zum Beispiel :

```
print("Hello, Bitcoin!")
```


- Illustrationen und Diagramme** :
    - Alle Bilder müssen im WebP-Format vorliegen. Verwenden Sie dieses kostenlose Tool, um sie bei Bedarf zu konvertieren: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Benennen Sie Bildmaterial mit 2 oder 3 Ziffern (z. B. "001.webp", "002.webp").
    - Verwenden Sie für Tutorials zu mobilen oder Hardware-Geldbörsen Modelle.
    - Verwenden Sie nur selbst erstelltes oder lizenzfreies Bildmaterial.
    - Stellen Sie sicher, dass sie relevant und von hoher Qualität sind.
- Grafische Charta** :
    - Schriftart: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Farben Plan ₿ Netzwerk :
        - Orange: "#FF5C00"
        - Schwarz: `#000000`
        - Weiß: "#FFFFFF

Wenn Sie technische Schwierigkeiten haben, Ihr Tutorial einzureichen, zögern Sie bitte nicht, auf [unserer speziellen Telegram-Gruppe für Beiträge] (https://t.me/PlanBNetwork_ContentBuilder) um Hilfe zu bitten. Herzlichen Dank!