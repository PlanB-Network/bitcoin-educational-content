---
name: Beitrag - Tutorial mit GitHub Desktop (Fortgeschrittene)
description: Vollständige Anleitung zum Vorschlagen eines Tutorials zum Plan ₿ Network mit GitHub Desktop
---
![cover](assets/cover.webp)

Bevor Sie diese Anleitung zum Hinzufügen eines neuen Tutorials lesen, müssen Sie einige vorbereitende Schritte durchgeführt haben. Wenn Sie das noch nicht getan haben, sollten Sie zuerst dieses einführende Tutorial lesen und dann hierher zurückkommen:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Das haben Sie bereits:


- Wählen Sie das Thema Ihres Tutorials;
- Kontaktieren Sie das Plan ₿ Network Team über [die Telegram-Gruppe] (https://t.me/PlanBNetwork_ContentBuilder) oder paolo@planb.network;
- Wählen Sie Ihre Beitragstools aus.

In diesem Tutorial werden wir sehen, wie Sie Ihr Tutorial zum Plan ₿ Network hinzufügen, indem Sie Ihre lokale Umgebung mit GitHub Desktop einrichten. Wenn Sie bereits mit Git vertraut sind, ist dieses sehr detaillierte Tutorial vielleicht nicht notwendig für Sie. Ich würde eher empfehlen, dieses andere Tutorial zu konsultieren, in dem ich nur die wichtigsten Richtlinien vorstelle, ohne detaillierte Schritt-für-Schritt-Anleitung:


- Erfahrene Benutzer**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Wenn Sie es vorziehen, Ihre lokale Umgebung nicht einzurichten, folgen Sie dieser anderen Anleitung für Anfänger, in der wir die Änderungen direkt über die Weboberfläche von GitHub vornehmen:


- Anfänger (Webschnittstelle)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Voraussetzungen

Erforderliche Software, um diesem Tutorial zu folgen:


- [GitHub Desktop](https://desktop.github.com/);
- Ein Markdown-Dateieditor wie [Obsidian] (https://obsidian.md/);
- Ein Code-Editor ([VSC](https://code.visualstudio.com/) oder [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Voraussetzungen vor Beginn des Tutorials:


- Sie haben ein [GitHub-Konto] (https://github.com/signup);
- Haben Sie einen Fork des [Plan ₿ Network source repository] (https://github.com/PlanB-Network/bitcoin-educational-content);
- Verfügen Sie über [ein Professorenprofil im Plan ₿ Network] (https://planb.network/professors) (nur wenn Sie ein vollständiges Tutorium vorschlagen).

Wenn Sie Hilfe benötigen, um diese Voraussetzungen zu erfüllen, werden Ihnen meine anderen Tutorials helfen:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
Sobald alles an Ort und Stelle ist und Ihre lokale Umgebung mit Ihrem eigenen Fork des Plan ₿ Network richtig eingerichtet ist, können Sie mit dem Hinzufügen des Tutorials beginnen.

## 1 - Einen neuen Zweig erstellen

Öffnen Sie Ihren Browser und gehen Sie auf die Seite Ihres Forks des Plan ₿ Network Repository. Dies ist der Fork, den Sie auf GitHub eingerichtet haben. Die URL Ihres Forks sollte wie folgt aussehen: `https://github.com/[Ihr-Benutzername]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Vergewissern Sie sich, dass Sie sich auf dem Hauptzweig `dev` befinden und klicken Sie dann auf die Schaltfläche `Sync fork`. Wenn Ihr Fork nicht auf dem neuesten Stand ist, wird GitHub Ihnen anbieten, Ihren Branch zu aktualisieren. Fahren Sie mit dieser Aktualisierung fort. Wenn Ihr Zweig hingegen bereits auf dem neuesten Stand ist, wird GitHub Sie darüber informieren:

![TUTO](assets/fr/04.webp)

Öffnen Sie die GitHub-Desktop-Software und stellen Sie sicher, dass Ihr Fork in der oberen linken Ecke des Fensters korrekt ausgewählt ist:

![TUTO](assets/fr/05.webp)

Klicken Sie auf die Schaltfläche "Herkunft abrufen". Wenn Ihr lokales Repository bereits auf dem neuesten Stand ist, schlägt GitHub Desktop keine weiteren Maßnahmen vor. Andernfalls wird die Option "Herkunft abrufen" angezeigt. Klicken Sie auf diese Schaltfläche, um Ihr lokales Repository zu aktualisieren:

![TUTO](assets/fr/06.webp)

Überprüfen Sie, ob Sie sich tatsächlich auf dem Hauptzweig `dev` befinden:

![TUTO](assets/fr/07.webp)

Klicken Sie auf diesen Zweig und dann auf die Schaltfläche "Neuer Zweig":

![TUTO](assets/fr/08.webp)

Stellen Sie sicher, dass der neue Zweig auf dem Quell-Repository basiert, nämlich `PlanB-Network/bitcoin-educational-content`.

Benennen Sie Ihren Zweig so, dass der Titel den Zweck klar erkennen lässt, und trennen Sie die einzelnen Wörter mit Bindestrichen. Nehmen wir zum Beispiel an, unser Ziel ist es, eine Anleitung zur Verwendung der Sparrow Wallet Software zu schreiben. In diesem Fall könnte der Arbeitszweig, der für die Erstellung dieses Tutorials vorgesehen ist, den Namen "tuto-sparrow-wallet-loic" tragen. Sobald Sie den entsprechenden Namen eingegeben haben, klicken Sie auf `Zweig erstellen`, um die Erstellung des Zweigs zu bestätigen:

![TUTO](assets/fr/09.webp)

Klicken Sie nun auf die Schaltfläche "Zweig veröffentlichen", um Ihren neuen Arbeitszweig in Ihrem Online-Zweig auf GitHub zu speichern:

![TUTORIAL](assets/fr/10.webp)

Auf dem GitHub-Desktop sollten Sie sich nun in Ihrem neuen Zweig befinden. Das bedeutet, dass alle Änderungen, die Sie lokal auf Ihrem Computer vornehmen, ausschließlich in diesem speziellen Zweig gespeichert werden. Solange dieser Zweig auf GitHub Desktop ausgewählt bleibt, entsprechen die lokal auf Ihrem Computer sichtbaren Dateien denen dieses Zweigs (`tuto-sparrow-wallet-loic`) und nicht denen des Hauptzweigs (`dev`).

![TUTORIAL](assets/fr/11.webp)

Für jeden neuen Artikel, den Sie veröffentlichen möchten, müssen Sie einen neuen Zweig von `dev` erstellen. Ein Zweig in Git ist eine parallele Version des Projekts, die es Ihnen ermöglicht, Änderungen vorzunehmen, ohne den Hauptzweig zu beeinflussen, bis die Arbeit zum Zusammenführen bereit ist.

## 2 - Hinzufügen der Tutorial-Dateien

Nun, da der Arbeitszweig erstellt ist, ist es an der Zeit, Ihr neues Tutorial zu integrieren. Sie haben zwei Möglichkeiten: Verwenden Sie mein Python-Skript, das die Erstellung der erforderlichen Dokumente automatisiert, oder erstellen Sie jede Datei manuell. Wir werden uns die Schritte ansehen, die für jede Option zu befolgen sind.

### Mit meinem Python-Skript

Sie müssen es auf Ihrem Rechner installieren:


- Python 3.8 oder höher;
- Die notwendigen Abhängigkeiten für das Skript. Ausführen:

```bash
pip install customtkinter appdirs
```

Um das Skript zu verwenden, wechseln Sie in den Ordner, in dem es gespeichert ist. Das Skript befindet sich im Plan ₿ Network Data Repository unter dem Pfad: `bitcoin-educational-content/scripts/tutorial-related/new-tutorial-creation/`.

Führen Sie den Befehl aus, sobald Sie sich im Ordner befinden:

```bash
python new-tutorial-creation.py
```

Eine grafische Benutzeroberfläche (GUI) wird geöffnet. Beim ersten Mal müssen Sie alle erforderlichen Informationen eingeben, aber bei späteren Verwendungen des Skripts werden Ihre persönlichen Informationen gespeichert, so dass Sie sie nicht erneut eingeben müssen.

![TUTORIAL](assets/fr/37.webp)

Beginnen Sie mit der Angabe des lokalen Pfads, der zum Ordner "/tutorials" auf Ihrem Klon des Repositorys führt (`.../bitcoin-educational-content/tutorials/`). Sie können ihn manuell notieren oder auf die Schaltfläche "Durchsuchen" klicken, um durch Ihren Datei-Explorer zu navigieren.

![TUTORIAL](assets/fr/38.webp)

Wählen Sie die Sprache, in der Sie Ihr Tutorium verfassen wollen.

![TUTORIAL](assets/fr/39.webp)

Wählen Sie eine Hauptkategorie für Ihr Lernprogramm.

![TUTORIAL](assets/fr/40.webp)

Wählen Sie dann je nach der von Ihnen gewählten Hauptkategorie eine passende Unterkategorie aus.

![TUTORIAL](assets/fr/41.webp)

Legen Sie einen Schwierigkeitsgrad für das Lernprogramm fest.

![TUTORIAL](assets/fr/42.webp)

Wählen Sie den Namen des Verzeichnisses, das speziell für Ihr Lernprogramm erstellt wurde. Der Name dieses Ordners sollte die im Tutorium behandelte Software widerspiegeln, wobei die Wörter mit Bindestrichen verbunden werden. Der Ordner könnte zum Beispiel "red-wallet" heißen:

![TUTO](assets/fr/43.webp)

Die `project_id` ist die UUID des Unternehmens oder der Organisation, die hinter dem im Tutorial vorgestellten Tool steht, verfügbar [in der Liste der Projekte] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Für ein Tutorial über die Sparrow-Wallet-Software würden Sie zum Beispiel diese `project_id` in der Datei finden: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Diese Information wird der YAML-Datei Ihres Tutorials hinzugefügt, weil das Plan ₿ Network eine Datenbank von Unternehmen und Organisationen unterhält, die in Bitcoin oder verwandten Projekten aktiv sind. Durch das Hinzufügen der `project_id`, die mit Ihrem Tutorial verbunden ist, schaffen Sie eine Verbindung zwischen Ihrem Inhalt und der betreffenden Einheit.

***Update:*** In der neuen Version des Skripts müssen Sie die `Projekt_id` nicht mehr manuell eingeben. Es wurde eine Suchfunktion hinzugefügt, um das Projekt anhand seines Namens zu finden und automatisch die entsprechende "project_id" abzurufen. Geben Sie den Anfang des Projektnamens in das Feld "Projektname" ein, um nach dem Projekt zu suchen, und wählen Sie dann das gewünschte Unternehmen aus dem Dropdown-Menü aus. Die "project_id" wird automatisch in das Feld darunter eingetragen. Sie haben auch die Möglichkeit, sie manuell einzutragen, falls erforderlich.

![TUTO](assets/fr/44.webp)

Wählen Sie für die Tags 2 oder 3 relevante Schlüsselwörter aus, die mit dem Inhalt Ihres Tutorials zusammenhängen, und wählen Sie diese ausschließlich [aus der Liste der Plan ₿ Network Tags] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).

![TUTO](assets/fr/45.webp)

Geben Sie im Feld "GitHub-ID des Mitwirkenden" Ihre GitHub-ID ein.

![TUTO](assets/fr/46.webp)

Geben Sie in das Feld "PBN-Professoren-ID" Ihre ID mit den Worten aus der BIP39-Liste ein, wie sie auf [Ihr Professorenprofil] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) erscheint.

![TUTO](assets/fr/47.webp)

Weitere Einzelheiten zu Ihrer Professoren-ID finden Sie in der folgenden Anleitung:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Sobald alle Informationen eingegeben und überprüft wurden, klicken Sie auf "Tutorial erstellen", um die Erstellung Ihrer Tutorial-Dateien zu bestätigen. Dadurch werden der Ordner Ihres Tutorials und alle erforderlichen Dateien im ausgewählten Kategorieordner lokal erstellt.

![TUTO](assets/fr/48.webp)

Sie können nun den Unterabschnitt "Ohne mein Python-Skript" sowie Schritt 3 "Ausfüllen der YAML-Datei" überspringen, da das Skript diese Aktionen bereits automatisch für Sie durchgeführt hat. Gehen Sie direkt zu Schritt 4 über und beginnen Sie mit dem Schreiben Ihres Tutorials.

Weitere Informationen zu diesem Python-Skript finden Sie auch in der README-Datei (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Ohne mein Python-Skript

Öffnen Sie Ihren Dateimanager und navigieren Sie zum Ordner "bitcoin-educational-content", der den lokalen Klon Ihres Repositorys darstellt. Normalerweise finden Sie ihn unter "Dokumente", "GitHub", "Bitcoin-Education-Content".

Innerhalb dieses Verzeichnisses müssen Sie den entsprechenden Unterordner finden, in dem Sie Ihr Lernprogramm ablegen möchten. Die Organisation der Ordner spiegelt die verschiedenen Bereiche der Plan ₿ Network Website wider. In unserem Beispiel, in dem wir ein Tutorial über Sparrow Wallet hinzufügen wollen, ist es angebracht, den folgenden Pfad zu wählen: `bitcoin-educational-content\tutorials\wallet`, was dem Abschnitt `WALLET` auf der Website entspricht:

![TUTO](assets/fr/12.webp)

Innerhalb des Ordners "wallet" müssen Sie ein neues Verzeichnis erstellen, das speziell für Ihr Lernprogramm bestimmt ist. Der Name dieses Ordners sollte an die im Tutorium behandelte Software erinnern, wobei die Wörter mit Bindestrichen verbunden werden müssen. In meinem Beispiel trägt der Ordner den Namen "Sparrow-Wallet":

![TUTO](assets/fr/13.webp)

In diesem neuen Unterordner, der Ihrem Lehrgang gewidmet ist, müssen mehrere Elemente hinzugefügt werden:


- Erstellen Sie einen Ordner `Assets`, der alle für Ihren Lehrgang notwendigen Illustrationen aufnehmen soll;
- Innerhalb dieses Ordners "Assets" müssen Sie einen Unterordner erstellen, der nach dem ursprünglichen Sprachcode des Lernprogramms benannt ist. Wenn das Lernprogramm beispielsweise auf Englisch verfasst ist, muss dieser Unterordner den Namen `en` tragen. Legen Sie dort alle visuellen Elemente des Tutorials ab (Diagramme, Bilder, Screenshots usw.).
- Es muss eine Datei "tutorial.yml" erstellt werden, um die Details Ihres Tutorials zu erfassen;
- Eine Datei im Markdown-Format muss erstellt werden, um den eigentlichen Inhalt Ihres Tutorials zu schreiben. Diese Datei muss entsprechend dem Sprachcode des Textes benannt werden. Zum Beispiel muss die Datei für ein auf Französisch geschriebenes Tutorial "fr.md" heißen.

![TUTO](assets/fr/14.webp)

Zusammenfassend lässt sich die Hierarchie der zu erstellenden Dateien wie folgt darstellen:

```plaintext
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Ausfüllen der YAML-Datei

Füllen Sie die Datei "tutorial.yml" aus, indem Sie die folgende Vorlage kopieren:

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

Hier sind die Details zu den Pflichtfeldern:


- **id**: Eine UUID (_Universally Unique Identifier_) zur eindeutigen Identifizierung des Lernprogramms. Sie können sie mit [einem Online-Tool] (https://www.uuidgenerator.net/version4) erzeugen. Die einzige Voraussetzung ist, dass diese UUID zufällig ist, um Konflikte mit anderen UUIDs auf der Plattform zu vermeiden;
- **project_id**: Die UUID des Unternehmens oder der Organisation, die hinter dem im Lernprogramm vorgestellten Tool steht [aus der Liste der Projekte] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Wenn Sie zum Beispiel ein Tutorial über die Sparrow Wallet Software erstellen, finden Sie diese `project_id` in der folgenden Datei: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Diese Information wird der YAML-Datei Ihres Tutorials hinzugefügt, weil das Plan ₿ Network eine Datenbank aller Unternehmen und Organisationen unterhält, die an Bitcoin oder verwandten Projekten arbeiten. Durch das Hinzufügen der `project_id` der Entität, die mit Ihrem Tutorial in Verbindung steht, schaffen Sie eine Verbindung zwischen den beiden Elementen;
- **tags**: 2 oder 3 relevante Schlüsselwörter, die sich auf den Inhalt des Tutorials beziehen und ausschließlich [aus der Liste der Tags des Plan ₿ Network] (https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ausgewählt werden;
- **category**: Die Unterkategorie, die dem Inhalt des Tutorials entspricht, entsprechend der Struktur des Plan ₿ Network (z. B. für Geldbörsen: `Desktop`, `Hardware`, `Mobile`, `Backup`);
- **level**: Der Schwierigkeitsgrad des Tutorials, unter:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: Ihre `Beitragszahler_id` (BIP39-Wörter), wie sie auf [Ihrem Professorprofil] (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) angezeigt wird;
- **original_language**: Die Originalsprache des Tutorials (z.B. `fr`, `en`, etc.);
- **proofreading**: Informationen über den Korrekturleseprozess. Füllen Sie den ersten Teil aus, da das Korrekturlesen Ihres eigenen Tutoriums als erste Validierung zählt:
    - **language**: Sprachcode des Korrekturlesens (z. B. "fr", "en" usw.).
    - **last_contribution_date**: Das heutige Datum.
    - **urgency**: Leer lassen.
    - **contributors_ide": Ihre GitHub-ID.
    - **reward**: Leer lassen.

Weitere Einzelheiten zu Ihrer Professorenkennung finden Sie in der entsprechenden Anleitung:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Hier ist ein Beispiel für eine fertige `tutorial.yml`-Datei für ein Tutorial über die Blockstream Green Wallet:

```yaml
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
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [Titel]
description: [Beschreibung]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```