---
name: Beitrag - Tutorials
description: Wie schlägt man ein neues Tutorial im PlanB Netzwerk vor?
---
![cover](assets/cover.webp)

Die Mission von PlanB ist es, erstklassige Bildungsressourcen über Bitcoin in möglichst vielen Sprachen bereitzustellen. Alle Inhalte, die auf der Website veröffentlicht werden, sind Open-Source und werden auf GitHub gehostet, was jedem die Möglichkeit bietet, an der Bereicherung der Plattform teilzunehmen. Beiträge können verschiedene Formen annehmen: Korrekturlesen und Korrigieren bestehender Texte, Übersetzen in andere Sprachen, Aktualisieren von Informationen oder Erstellen neuer Tutorials, die auf unserer Website noch nicht verfügbar sind.

In diesem Tutorial werde ich erklären, wie man den Abschnitt "Tutorials" des PlanB Netzwerks ändert. Wenn Sie ein neues Tutorial hinzufügen oder ein bestehendes verbessern möchten, ist dieser Artikel für Sie! Wir werden im Detail betrachten, wie man zum PlanB Netzwerk über GitHub beiträgt, während man Obsidian, ein Schreibtool, verwendet.

## Voraussetzungen

Um zum PlanB Netzwerk beizutragen, haben Sie 3 Optionen, abhängig von Ihrem Erfahrungsgrad mit GitHub:
1. **Erfahrene Benutzer**: Fahren Sie mit Ihren üblichen Methoden fort und konsultieren Sie dieses Tutorial, um sich mit der Struktur des PlanB Repositories, spezifischen Anforderungen und dem Workflow vertraut zu machen.
2. **Anfänger, die bereit sind zu lernen**: Ich empfehle, Ihre eigene Arbeitsumgebung einzurichten. Folgen Sie diesem Tutorial sowie unseren anderen unten aufgeführten Artikeln, die Sie Schritt für Schritt anleiten.
3. **Anfänger für kleinere Beiträge**: Für Aufgaben, die weniger Änderungen erfordern, wie Korrekturlesen oder Korrekturen, verwenden Sie direkt die Web-Oberfläche von GitHub, ohne eine komplette lokale Umgebung einzurichten.

**Software, die benötigt wird, um meinem Tutorial zu folgen:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- Ein Code-Editor ([VSC](https://code.visualstudio.com/) oder [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/1.webp)
**Voraussetzungen, bevor Sie mit dem Tutorial beginnen:**
- Ein [GitHub-Konto](https://github.com/signup) haben.
- Einen Fork des [PlanB Netzwerk Quell-Repositories](https://github.com/PlanB-Network/bitcoin-educational-content) haben.
- Ein [Professor-Profil im PlanB Netzwerk](https://planb.network/professors) haben (nur wenn Sie ein komplettes Tutorial vorschlagen).

**Wenn Sie Hilfe benötigen, um diese Voraussetzungen zu erfüllen, werden meine anderen Tutorials Sie anleiten:**
**[Git und GitHub verstehen](https://planb.network/tutorials/others/basics-of-github)**
**[Ein GitHub-Konto erstellen](https://planb.network/tutorials/others/create-github-account)**
**[Ihre Arbeitsumgebung einrichten](https://planb.network/tutorials/others/github-desktop-work-environment)**
**[Ein Professor-Profil erstellen](https://planb.network/tutorials/others/create-teacher-profile)**
## Welche Art von Inhalten soll auf PlanB Netzwerk geschrieben werden?
Wir suchen vor allem nach Tutorials über Werkzeuge, die mit Bitcoin oder seinem Ökosystem in Verbindung stehen. Diese Inhalte können um sechs Hauptkategorien organisiert werden:
- Wallet;
- Node;
- Mining;
- Händler;
- Exchange;
- Privatsphäre.
![tutorial](assets/2.webp)
Über diese speziell auf Bitcoin bezogenen Themen hinaus sucht PlanB auch nach Beiträgen zu Themen, die die individuelle Souveränität hervorheben, wie:
- Open-Source-Tools;
- Informatik;
- Kryptographie;
- Energie;
- Mathematik;
- Wirtschaft;
- DIYs;
- LifeHacking...
Zum Beispiel haben wir derzeit Tutorials über Tails, Nostr oder GrapheneOS. Diese Tools stehen nicht direkt in Verbindung mit Bitcoin, aber es sind Systeme, die uns im Prozess der Souveränität in der digitalen Welt interessieren können. Diese Inhalte können in eine Unterkategorie des Abschnitts "Andere" integriert werden.
Sie haben die Wahl, ein Tutorial von Grund auf neu zu gestalten oder ein bereits auf Ihrer Website veröffentlichtes Tutorial zu nehmen (vorausgesetzt, Sie besitzen das Urheberrecht), um es auch auf dem PlanB Network zu teilen, indem Sie einen Link zum Originalartikel hinzufügen.

Unabhängig von Ihrer Wahl, beachten Sie, dass alle Inhalte, die auf dem PlanB Network veröffentlicht werden, unter der freien Lizenz [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) stehen. Diese Lizenz erlaubt es jedem, Ihren Inhalt zu kopieren und potenziell zu modifizieren, vorausgesetzt, die Originalquelle wird gebührend genannt.

## Wie schlägt man ein Tutorial auf dem PlanB Network vor?

Sobald alles eingerichtet ist und Ihre lokale Umgebung mit Ihrem eigenen Fork des PlanB Network gut eingerichtet ist, können Sie beginnen, das Tutorial hinzuzufügen.

### Erstellen Sie einen neuen Branch

- Öffnen Sie Ihren Browser und gehen Sie zur Seite Ihres Forks des PlanB-Repositorys. Dies ist der Fork, den Sie auf GitHub eingerichtet haben. Die URL Ihres Forks sollte so aussehen: `https://github.com/[Ihr-Benutzername]/bitcoin-educational-content`:
![tutorial](assets/3.webp)
- Stellen Sie sicher, dass Sie sich im Hauptbranch `dev` befinden, dann klicken Sie auf den `Sync fork`-Button. Wenn Ihr Fork nicht auf dem neuesten Stand ist, wird GitHub anbieten, Ihren Branch zu aktualisieren. Führen Sie dieses Update durch. Ist Ihr Branch hingegen bereits auf dem neuesten Stand, wird GitHub Sie informieren:
![tutorial](assets/4.webp)
- Öffnen Sie die GitHub Desktop-Software und stellen Sie sicher, dass Ihr Fork in der oberen linken Ecke des Fensters korrekt ausgewählt ist:
![tutorial](assets/5.webp)
- Klicken Sie auf den `Fetch origin`-Button. Wenn Ihr lokales Repository bereits auf dem neuesten Stand ist, wird GitHub Desktop keine weiteren Aktionen vorschlagen. Andernfalls erscheint die Option `Pull origin`. Klicken Sie auf diesen Button, um Ihr lokales Repository zu aktualisieren: ![tutorial](assets/6.webp)
- Stellen Sie sicher, dass Sie sich im Hauptbranch `dev` befinden:
![tutorial](assets/7.webp)
- Klicken Sie auf diesen Branch, dann klicken Sie auf den `New Branch`-Button:
![tutorial](assets/8.webp)
- Stellen Sie sicher, dass der neue Branch auf dem Quellrepository basiert, nämlich `PlanB-Network/bitcoin-educational-content`.
- Benennen Sie Ihren Branch so, dass der Titel klar seinen Zweck angibt, indem Sie Bindestriche verwenden, um jedes Wort zu trennen. Angenommen, unser Ziel ist es, ein Tutorial über die Verwendung der Sparrow Wallet-Software zu schreiben. In diesem Fall könnte der Arbeitsbranch, der diesem Tutorial gewidmet ist, benannt werden als: `tuto-sparrow-wallet-loic`. Sobald der passende Name eingegeben ist, klicken Sie auf `Create branch`, um die Erstellung des Branchs zu bestätigen:
![tutorial](assets/9.webp)
- Klicken Sie nun auf den `Publish branch`-Button, um Ihren neuen Arbeitsbranch auf Ihrem Online-Fork auf GitHub zu speichern:
![tutorial](assets/10.webp)
Nun sollten Sie auf GitHub Desktop auf Ihrem neuen Branch sein. Das bedeutet, dass alle lokal auf Ihrem Computer vorgenommenen Änderungen ausschließlich auf diesem spezifischen Branch aufgezeichnet werden. Solange dieser Branch auf GitHub Desktop ausgewählt bleibt, entsprechen die lokal auf Ihrem Rechner sichtbaren Dateien denen dieses Branchs (`tuto-sparrow-wallet-loic`) und nicht denen des Hauptbranchs (`dev`).
![tutorial](assets/11.webp)
Für jeden neuen Artikel, den Sie veröffentlichen möchten, müssen Sie einen neuen Branch von `dev` erstellen. Ein Branch in Git ist eine parallele Version des Projekts, die es Ihnen ermöglicht, Änderungen vorzunehmen, ohne den Hauptbranch zu beeinflussen, bis die Arbeit bereit ist, zusammengeführt zu werden.
### Hinzufügen des Tutorials

Jetzt, da der Arbeitsbranch erstellt ist, ist es an der Zeit, Ihr neues Tutorial zu integrieren.
- Öffnen Sie Ihren Dateimanager und navigieren Sie zum Ordner `bitcoin-educational-content`, der den lokalen Klon Ihres Repositories darstellt. Normalerweise sollten Sie ihn unter `Documents\GitHub\bitcoin-educational-content` finden. Innerhalb dieses Verzeichnisses ist es notwendig, den entsprechenden Unterordner für die Platzierung Ihres Tutorials zu lokalisieren. Die Organisation der Ordner spiegelt die verschiedenen Abschnitte der PlanB Network-Website wider. In unserem Beispiel, da wir ein Tutorial über Sparrow Wallet hinzufügen möchten, ist es angebracht, zum folgenden Pfad zu gehen: `bitcoin-educational-content\tutorials\wallet`, der der `WALLET`-Sektion auf der Website entspricht: ![tutorial](assets/12.webp)
- Innerhalb des `wallet`-Ordners müssen Sie ein neues Verzeichnis speziell für Ihr Tutorial erstellen. Der Name dieses Ordners muss die in dem Tutorial behandelte Software evozieren, wobei Wörter mit Bindestrichen verbunden werden sollen. Für mein Beispiel wird der Ordner `sparrow-wallet` betitelt sein:
![tutorial](assets/13.webp)
- In diesem neuen Unterordner, der Ihrem Tutorial gewidmet ist, müssen mehrere Elemente hinzugefügt werden:
	- Erstellen Sie einen `assets`-Ordner, der dazu bestimmt ist, alle Illustrationen aufzunehmen, die für Ihr Tutorial notwendig sind;
    - Innerhalb dieses `assets`-Ordners müssen Sie 8 Unterordner mit den Namen `fr`, `de`, `en`, `it`, `es`, `ja`, `vi` und `pt` erstellen, um die Visuals entsprechend den zugehörigen Sprachen zu klassifizieren. Sie müssen auch einen `notext`-Unterordner für Visuals hinzufügen, die keine Übersetzung benötigen, wie zum Beispiel Screenshots;
	- Eine `tutorial.yml`-Datei muss erstellt werden, um die Details zu Ihrem Tutorial aufzuzeichnen;
	- Eine Datei im Markdown-Format ist zu erstellen, um den eigentlichen Inhalt Ihres Tutorials zu schreiben. Diese Datei muss gemäß dem Sprachcode der Schrift benannt werden. Zum Beispiel sollte für ein Tutorial, das auf Französisch geschrieben ist, die Datei `fr.md` genannt werden.
![tutorial](assets/14.webp)
- Zusammengefasst sieht hier die Hierarchie der zu erstellenden Dateien aus:
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (zu modifizieren mit der richtigen Kategorie)
        └── sparrow-wallet/ (zu modifizieren mit dem Namen des Tutorials)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (zu modifizieren entsprechend dem passenden Sprachcode)
```

- Um zu beginnen, öffnen Sie Ihre `tutorial.yml`-Datei mit Ihrem Code-Editor.
- Füllen Sie jedes Feld mit den unten angegebenen Informationen aus:
- **builder**: Geben Sie den Namen des Unternehmens ein, das die Software herstellt, für die Sie ein Tutorial erstellen;
- **tags**: Bestimmen Sie eine Reihe von Schlüsselwörtern, die eng mit dem Thema Ihres Artikels zusammenhängen, um dessen Suche und Indexierung zu erleichtern;
- **Kategorie**: Wählen Sie eine geeignete Unterkategorie unter den auf der PlanB-Website verfügbaren aus, basierend auf dem Inhalt Ihres Tutorials. Zum Beispiel, für ein Tutorial im Bereich `WALLET`, sind die verfügbaren Optionen `Desktop`, `Hardware` und `Mobil`;
- **Level**: Geben Sie den Schwierigkeitsgrad Ihres Tutorials an, indem Sie eine der folgenden vier Kategorien wählen:
    - Anfänger (`beginner`),
    - Fortgeschrittene (`intermediary`),
    - Fortgeschritten (`advanced`),
    - Experte (`expert`).
- **Professor**: Geben Sie Ihre Mitwirkenden-ID an, wie sie in Ihrem Profil als Lehrkraft erscheint. Für weitere Details siehe [das entsprechende Tutorial](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **Link** (optional): Falls Sie eine Quellwebsite für das Tutorial, das Sie entwickeln, wie Ihre eigene persönliche Seite, nennen möchten, können Sie hier den betreffenden Link hinzufügen.
![tutorial](assets/15.webp)
- Sobald Sie Ihre `tutorial.yml`-Datei bearbeitet haben, speichern Sie Ihr Dokument, indem Sie auf `Datei > Speichern` klicken:
![tutorial](assets/16.webp)
- Sie können jetzt Ihren Code-Editor schließen.
- Im Ordner `assets` müssen Sie eine Datei namens `logo.webp` hinzufügen, die als Thumbnail für Ihren Artikel dienen wird. Dieses Bild muss im `.webp`-Format vorliegen und quadratische Abmessungen haben, um mit der Benutzeroberfläche zu harmonieren. Sie haben die Freiheit, das Logo der Software, die im Tutorial behandelt wird, oder ein anderes relevantes Bild zu wählen, vorausgesetzt, es ist frei von Rechten. Fügen Sie außerdem ein Bild mit dem Titel `cover.webp` am gleichen Ort hinzu. Dieses Bild wird oben in Ihrem Tutorial angezeigt. Stellen Sie sicher, dass dieses Bild, wie das Logo, Nutzungsrechte respektiert und für den Kontext Ihres Tutorials geeignet ist:
![tutorial](assets/17.webp)
- Nun können Sie Ihre Datei öffnen, die Ihr Tutorial beherbergen wird, benannt nach dem Code Ihrer Sprache, wie `de.md`. Gehen Sie zu Obsidian, auf der linken Seite des Fensters, scrollen Sie durch den Ordnerbaum zum Ordner Ihres Tutorials und zur gesuchten Datei:
![tutorial](assets/18.webp)
- Klicken Sie auf die Datei, um sie zu öffnen:
![tutorial](assets/19.webp)
- Wir beginnen damit, den `Eigenschaften`-Abschnitt am Anfang des Dokuments auszufüllen. Wenn dieser Abschnitt in Ihrer Datei fehlt (wenn das Dokument völlig leer ist), können Sie ihn reproduzieren, indem Sie ihn aus einem anderen vorhandenen Tutorial kopieren: ![tutorial](assets/20.webp)
- Sie können ihn auch manuell auf diese Weise mit Ihrem Code-Editor hinzufügen:
```markdown
---
name: [Titel]
description: [Beschreibung]
---
```
![tutorial](assets/21.webp)
- Füllen Sie den Namen Ihres Tutorials und eine kurze Beschreibung dazu aus:
![tutorial](assets/22.webp)
- Fügen Sie dann Ihr Cover-Bild am Anfang Ihres Tutorials hinzu. Dazu tippen Sie:
```markdown
![cover-sparrow](assets/cover.webp)
```
- Diese Syntax wird immer dann nützlich sein, wenn Sie ein Bild zu Ihrem Tutorial hinzufügen müssen. Das Ausrufezeichen zeigt an, dass es sich um ein Bild handelt, wobei der alternative Text (alt) zwischen den Klammern angegeben ist. Der Pfad zum Bild wird zwischen den Klammern angegeben:
![tutorial](assets/23.webp)
- Fahren Sie mit dem Schreiben Ihres Tutorials fort, indem Sie Ihren Inhalt schreiben. Wenn Sie einen Untertitel integrieren möchten, wenden Sie das entsprechende Markdown-Format an, indem Sie den Text mit `##` prefixen:
![tutorial](assets/24.webp)

### Wie fügt man Diagramme zum Tutorial hinzu?
Die Sprachunterordner im `assets`-Ordner dienen dazu, die Diagramme und Visualisierungen zu organisieren, die Ihr Tutorial begleiten werden. Wenn Ihre Bilder Text enthalten, stellen Sie sicher, dass Sie diese für jede betroffene Sprache übersetzen, um Ihren Inhalt einem internationalen Publikum zugänglich zu machen. Für Diagramme ohne zu übersetzenden Text oder Screenshots, platzieren Sie diese direkt im `notext`-Unterordner. ![tutorial](assets/25.webp)
Um Ihre Bilder zu benennen, setzen Sie einfach Nummern in der Reihenfolge ihres Erscheinens im Tutorial. Benennen Sie zum Beispiel Ihr erstes Bild `1.webp`, Ihr zweites `2.webp` und so weiter.

Wenn dasselbe Diagramm in mehrere Sprachen übersetzt wird, behalten Sie denselben Dateinamen für die verschiedenen Übersetzungen in den Sprachunterordnern bei, wie zum Beispiel `en/1.webp`, `fr/1.webp`, `pt/1.webp` usw.

Sie haben die Möglichkeit, verschiedene Bildformate wie `jpeg`, `png` oder `webp` zu verwenden. Es wird empfohlen, das `webp`-Format zu wählen, damit die Bilder weniger Speicherplatz benötigen.
![tutorial](assets/26.webp)
Um ein Diagramm in Ihr Dokument einzufügen, verwenden Sie den folgenden Befehl in Markdown und achten Sie darauf, den passenden Alternativtext und den korrekten Pfad des Bildes anzugeben:
```markdown
![sparrow](assets/notext/1.webp)
```
Das Ausrufezeichen am Anfang zeigt an, dass es sich um ein Bild handelt. Der Alternativtext, der die Zugänglichkeit und SEO unterstützt, wird zwischen den Klammern platziert. Schließlich wird der Pfad zum Bild zwischen den Klammern angegeben: ![tutorial](assets/27.webp)
Wenn Sie eigene Diagramme erstellen möchten, stellen Sie sicher, dass Sie sich an die Grafikcharta von PlanB Network halten, um eine visuelle Konsistenz zu gewährleisten:
- **Schriftart**: Verwenden Sie [Rubik](https://fonts.google.com/specimen/Rubik);
- **Farben**:
	- Orange: #FF5C00
	- Schwarz: #000000
	- Weiß: #FFFFFF

**Es ist zwingend erforderlich, dass alle in Ihre Tutorials integrierten Visualisierungen lizenzfrei sind oder mit der Lizenz der Quelldatei übereinstimmen**. Außerdem werden alle auf PlanB Network veröffentlichten Diagramme unter der CC-BY-SA-Lizenz zur Verfügung gestellt, ebenso wie der Text.

**-> Tipp:** Beim öffentlichen Teilen von Dateien, wie Bildern, ist es wichtig, überflüssige Metadaten zu entfernen. Diese können sensible Informationen enthalten, wie Standortdaten, Erstellungsdaten oder Details über den Autor. Um Ihre Privatsphäre zu schützen, ist es ratsam, diese Metadaten zu entfernen. Um diese Operation zu vereinfachen, können Sie spezialisierte Tools wie [Exif Cleaner](https://exifcleaner.com/) verwenden, das die Möglichkeit bietet, die Metadaten eines Dokuments mit einem einfachen Drag-and-Drop zu bereinigen.

### Wie speichert und pusht man das Tutorial?

Sobald Sie Ihr Tutorial in der von Ihnen gewählten Sprache fertiggestellt haben, ist der nächste Schritt, einen **Pull Request** einzureichen. Der Administrator wird dann die fehlenden Übersetzungen Ihres Tutorials hinzufügen, dank unserer automatisierten Übersetzungsmethode.

- Um mit dem Pull Request fortzufahren, öffnen Sie die GitHub Desktop-Software.
- Die Software sollte automatisch die Änderungen erkennen, die Sie lokal im Vergleich zum ursprünglichen Repository gemacht haben. Überprüfen Sie vor dem Fortfahren sorgfältig auf der linken Seite der Schnittstelle, dass diese Änderungen genau dem entsprechen, was Sie erwartet haben: ![tutorial](assets/28.webp)
- Fügen Sie einen Titel für Ihren Commit hinzu und klicken Sie dann auf den blauen `Commit to [your branch]`-Button, um diese Änderungen zu validieren: ![tutorial](assets/29.webp)
Ein Commit ist eine Speicherung der vorgenommenen Änderungen am Branch, begleitet von einer beschreibenden Nachricht, die es ermöglicht, die Entwicklung eines Projekts im Laufe der Zeit zu verfolgen. Es ist also eine Art Zwischencheckpoint.
- Klicken Sie dann auf den `Push origin`-Button. Dadurch wird Ihr Commit zu Ihrem Fork gesendet: ![Tutorial](assets/30.webp) - Wenn Sie Ihr Tutorial noch nicht abgeschlossen haben, können Sie später darauf zurückkommen und neue Commits machen.
- Wenn Sie Ihre Bearbeitungen für diesen Branch abgeschlossen haben, klicken Sie jetzt auf den `Preview Pull Request`-Button: ![Tutorial](assets/31.webp)
- Sie können ein letztes Mal überprüfen, ob Ihre Änderungen korrekt sind, dann klicken Sie auf den `Create pull request`-Button:
![Tutorial](assets/32.webp)
Ein Pull Request ist eine Anfrage, um die Änderungen von Ihrem Branch in den Hauptbranch des PlanB Network-Repositorys zu integrieren, was die Überprüfung und Diskussion der Änderungen vor ihrer Zusammenführung ermöglicht.

- Sie werden automatisch in Ihrem Browser zu GitHub auf die Vorbereitungsseite Ihres Pull Requests weitergeleitet:
![Tutorial](assets/33.webp)
- Geben Sie einen Titel an, der die Änderungen, die Sie mit dem Quell-Repository zusammenführen möchten, kurz zusammenfasst.
- Fügen Sie einen kurzen Kommentar hinzu, der diese Änderungen beschreibt.
- Klicken Sie auf den grünen `Create pull request`-Button, um die Zusammenführungsanfrage zu bestätigen:
![Tutorial](assets/34.webp)
Ihr PR wird dann im `Pull Request`-Tab des Hauptrepositorys von PlanB Network sichtbar sein. Jetzt müssen Sie nur noch warten, bis ein Administrator Sie kontaktiert, um die Zusammenführung Ihres Beitrags zu bestätigen oder um eventuelle zusätzliche Änderungen anzufordern.
![Tutorial](assets/35.webp)
Nach der Zusammenführung Ihres PR mit dem Hauptbranch wird empfohlen, Ihren Arbeitsbranch (`tuto-sparrow-wallet`) zu löschen, um eine saubere Historie auf Ihrem Fork zu bewahren. GitHub bietet Ihnen diese Option automatisch auf der Seite Ihres PR an:
![Tutorial](assets/36.webp)
In der GitHub Desktop-Software können Sie zurück zum Hauptbranch Ihres Forks (`dev`) wechseln.
![Tutorial](assets/7.webp)
Wenn Sie Änderungen an Ihrem Beitrag vornehmen möchten, nachdem Sie Ihren PR bereits eingereicht haben, hängt das Vorgehen vom aktuellen Status Ihres PR ab:
- Wenn Ihr PR noch offen ist und noch nicht zusammengeführt wurde, führen Sie die Änderungen lokal durch, während Sie im gleichen Branch bleiben. Sobald die Änderungen abgeschlossen sind, verwenden Sie den `Push origin`-Button, um einen neuen Commit zu Ihrem noch offenen PR hinzuzufügen;
- Falls Ihr PR bereits mit dem Hauptbranch zusammengeführt wurde, müssen Sie den Prozess von vorne beginnen, indem Sie einen neuen Branch erstellen und dann einen neuen PR einreichen. Stellen Sie sicher, dass Ihr lokales Repository mit dem Quell-Repository von PlanB Network synchronisiert ist, bevor Sie fortfahren.
