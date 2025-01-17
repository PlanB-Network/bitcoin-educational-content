---
name: PlanB Professor
description: Wie Sie Ihr Profil als Professor im PlanB Netzwerk hinzufügen können?
---
![cover](assets/cover.webp)

Die Mission von PlanB ist es, erstklassige Bildungsressourcen über Bitcoin in möglichst vielen Sprachen bereitzustellen. Alle Inhalte, die auf der Website veröffentlicht werden, sind Open-Source und werden auf GitHub gehostet, was es jedem ermöglicht, an der Bereicherung der Plattform teilzunehmen. Beiträge können verschiedene Formen annehmen: Korrekturlesen und Überprüfen bestehender Texte, Erstellen von Schulungskursen, Übersetzen in andere Sprachen, Aktualisieren von Informationen oder Erstellen neuer Tutorials, die auf unserer Website noch nicht verfügbar sind.

Wenn Sie ein neues vollständiges Tutorial oder einen Kurs im PlanB Netzwerk hinzufügen möchten, müssen Sie Ihr Profil als Professor erstellen. Dies ermöglicht es Ihnen, für die Inhalte, die Sie auf der Website produzieren, ordnungsgemäß gutgeschrieben zu werden.
![tutorial](assets/1.webp)
Wenn Sie zuvor zum PlanB Netzwerk beigetragen haben, haben Sie wahrscheinlich bereits eine Beitragenden-ID. Sie können diese in Ihrem Professorenordner finden, zugänglich [über diese Seite](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors). Wenn dies der Fall ist, können Sie dieses Tutorial überspringen und direkt mit dem Beitrag beginnen.
![tutorial](assets/2.webp)

Lassen Sie uns gemeinsam entdecken, wie man einen neuen Professor in diesem Tutorial hinzufügt!

## Voraussetzungen

**Software, die benötigt wird, um meinem Tutorial zu folgen:**
- [GitHub Desktop](https://desktop.github.com/)
- Ein Code-Editor ([VSC](https://code.visualstudio.com/) oder [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/3.webp)
**Voraussetzungen, bevor Sie mit dem Tutorial beginnen:**
- Ein [GitHub-Konto](https://github.com/signup) besitzen.
- Einen Fork des [PlanB Netzwerk-Quellrepositories](https://github.com/PlanB-Network/bitcoin-educational-content) haben.

**Wenn Sie Hilfe benötigen, um diese Voraussetzungen zu erfüllen, werden Sie meine anderen Tutorials leiten:**
**[Verständnis von Git und GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[Erstellen eines GitHub-Kontos](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Einrichten Ihrer Arbeitsumgebung](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**

## Wie erstellt man ein neues Profil als Professor?

- Öffnen Sie Ihren Browser und navigieren Sie zur Seite Ihres Forks des PlanB Repositories. Die URL Ihres Forks sollte so aussehen: `https://github.com/[Benutzername]/bitcoin-educational-content`
![tutorial](assets/4.webp)
- Stellen Sie sicher, dass Sie sich im Hauptzweig `dev` befinden, dann klicken Sie auf den `Sync fork`-Knopf. Wenn Ihr Fork nicht auf dem neuesten Stand ist, wird GitHub Ihnen anbieten, Ihren Zweig zu aktualisieren. Führen Sie diese Synchronisation durch.

- Wenn Ihr Zweig andererseits bereits auf dem neuesten Stand ist, wird GitHub Sie informieren:
![tutorial](assets/5.webp)- Öffnen Sie GitHub Desktop und stellen Sie sicher, dass Ihr Fork in der oberen linken Ecke des Fensters korrekt ausgewählt ist:
![tutorial](assets/6.webp)
- Klicken Sie auf den `Fetch origin`-Knopf.

- Wenn Ihr lokales Repository bereits auf dem neuesten Stand ist, wird GitHub Desktop keine weiteren Aktionen vorschlagen. Andernfalls erscheint die Option `Pull origin`. Klicken Sie auf diesen Knopf, um Ihr lokales Repository zu aktualisieren:
![tutorial](assets/7.webp)
- Stellen Sie sicher, dass Sie sich im Hauptzweig `dev` befinden:
![tutorial](assets/8.webp)
- Klicken Sie auf diesen Zweig, dann klicken Sie auf den `New Branch`-Knopf:
![tutorial](assets/9.webp)
- Stellen Sie sicher, dass der neue Zweig auf dem Quell-Repository basiert, nämlich `PlanB-Network/bitcoin-educational-content`.
- Benennen Sie Ihren Zweig so, dass der Titel klar seinen Zweck beschreibt, indem Sie Bindestriche verwenden, um jedes Wort zu trennen. Da dieser Zweig für das Hinzufügen eines Professorenprofils vorgesehen ist, könnte ein Beispielname sein: `add-professor-[Ihr-Name]`. Nachdem Sie den Namen eingegeben haben, klicken Sie auf `Create branch`, um dessen Erstellung zu bestätigen:
![Tutorial](assets/10.webp)
- Klicken Sie nun auf den Button `Publish branch`, um Ihren neuen Arbeitszweig in Ihrem Online-Fork auf GitHub zu speichern:
![Tutorial](assets/11.webp)
- Zu diesem Zeitpunkt sollten Sie in GitHub Desktop auf Ihrem neuen Zweig sein. Das bedeutet, dass alle lokal auf Ihrem Computer vorgenommenen Änderungen ausschließlich auf diesem spezifischen Zweig aufgezeichnet werden. Solange dieser Zweig in GitHub Desktop ausgewählt bleibt, entsprechen die lokal auf Ihrem Gerät sichtbaren Dateien denen dieses Zweigs (`add-professor-Ihr-Name`), und nicht denen des Hauptzweigs (`dev`):
![Tutorial](assets/12.webp)
- Um Ihr Professorenprofil hinzuzufügen, öffnen Sie Ihren Datei-Explorer und navigieren zu Ihrem lokalen Repository im Ordner `professors`. Sie finden ihn unter dem Pfad: `\GitHub\bitcoin-educational-content\professors`.

- Erstellen Sie innerhalb dieses Ordners einen neuen Ordner, benannt nach Ihrem Namen oder Pseudonym. Stellen Sie sicher, dass im Ordnernamen keine Leerzeichen enthalten sind. Wenn Ihr Name also "Loic Pandul" ist und kein anderer Professor diesen Namen hat, wird der zu erstellende Ordner `loic-pandul` genannt:
![Tutorial](assets/13.webp)
- Um die Dinge zu vereinfachen, können Sie bereits alle Dokumente von einem anderen Professor in Ihren eigenen Ordner kopieren und einfügen. Wir werden dann fortfahren, diese Dokumente zu modifizieren, um sie gemäß Ihrem Profil anzupassen:
![Tutorial](assets/14.webp)
- Beginnen Sie, indem Sie zum Ordner `assets` navigieren. Löschen Sie das Profilbild des Professors, das Sie zuvor kopiert haben, und ersetzen Sie es durch Ihr eigenes Profilbild. Es ist zwingend erforderlich, dass dieses Bild im `.webp`-Format vorliegt und den vollständigen Dateinamen `profile.webp` trägt. Beachten Sie, dieses Bild wird im Internet veröffentlicht und ist für jeden zugänglich: ![Tutorial](assets/15.webp)
- Öffnen Sie als Nächstes die Datei `professor.yml` mit Ihrem Code-Editor (VSC oder Sublime Text, zum Beispiel). Sie gelangen zu der Datei, die von einem bestehenden Professor kopiert wurde:
![Tutorial](assets/16.webp)
- Sie müssen dann die vorhandenen Informationen mit Ihren eigenen aktualisieren:
	- **name:** Schreiben Sie Ihren Namen oder Ihr Pseudonym;
	- **links:** Geben Sie Ihre Konten in sozialen Netzwerken wie Twitter und Nostr an, sowie die URL Ihrer persönlichen Website (optional);
	- **affiliation:** Erwähnen Sie den Namen des Unternehmens, das Sie beschäftigt (optional);
	- **tags:** Spezifizieren Sie Ihre Spezialisierungsgebiete aus der folgenden Liste, wobei Sie eigene Themen hinzufügen können. Achten Sie jedoch darauf, die Anzahl der Tags auf höchstens 4 zu begrenzen, um eine gute Benutzeroberfläche zu gewährleisten:
	    - privacy,
	    - cryptography,
	    - bitcoin,
	    - mining,
	    - lightning-network,
	    - economy,
	    - history,
	    - merchants,
	    - security,
	    - ...
	- **tips:** Geben Sie Ihre Lightning-Adresse für Spenden an, damit Leser Ihrer zukünftigen Tutorials Ihnen einige Sats senden können (optional);
	- **company:** Wenn Sie eine besitzen, geben Sie den Namen Ihres Unternehmens an (optional). Sie müssen dann die vorhandenen Informationen mit Ihren eigenen aktualisieren:
![Tutorial](assets/17.webp)- Sie müssen auch die `contributor-id` ändern. Dieser Identifikator wird verwendet, um Sie auf der Website zu erkennen, ist jedoch außerhalb von GitHub nicht öffentlich. Sie können frei jede Kombination aus zwei Wörtern wählen, die sich auf [die englische Liste von 2048 Wörtern aus BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) bezieht. Vergessen Sie nicht, einen Bindestrich zwischen die beiden gewählten Wörter einzufügen. Zum Beispiel habe ich hier `crazy-cactus` gewählt:
![Tutorial](assets/18.webp)
- Sobald Sie die Änderungen am `professor.yml` Dokument abgeschlossen haben, klicken Sie auf `Datei > Speichern`, um Ihre Datei zu speichern. Sie können dann Ihren Code-Editor schließen:
![Tutorial](assets/19.webp)
- Innerhalb Ihres Professor-Ordners können Sie Dokumente in Sprachen, die für Sie nicht relevant sind und die ursprünglich von einem anderen Professor kopiert wurden, löschen. Behalten Sie nur die Datei, die Ihrer Muttersprache entspricht. Zum Beispiel habe ich in meinem Fall nur die `fr.yml` Datei behalten, da meine Sprache Französisch ist: ![Tutorial](assets/20.webp)
- Doppelklicken Sie auf diese Datei, um sie mit Ihrem Code-Editor zu öffnen.

- In dieser Datei haben Sie die Möglichkeit, Ihre komplette Biografie im Abschnitt `bio` zu schreiben und eine Zusammenfassung oder einen prägnanten Titel unter `short_bio`:
![Tutorial](assets/21.webp)
- Nachdem Sie Ihr `fr.yml` Dokument gespeichert haben, müssen Sie eine Kopie dieser Datei für jede der folgenden acht Sprachen erstellen:
    - Deutsch (DE);
    - Englisch (EN);
    - Französisch (FR);
    - Spanisch (ES);
    - Italienisch (IT);
    - Portugiesisch (PT);
    - Japanisch (JA);
    - Vietnamesisch (VI).

- Fahren Sie fort, indem Sie Ihre Originaldatei kopieren und in die entsprechende Sprache übersetzen. Wenn Sie die Sprache beherrschen, können Sie die Übersetzung manuell durchführen. Andernfalls können Sie gerne ein automatisches Übersetzungstool oder einen Chatbot verwenden:
![Tutorial](assets/22.webp)
- Wenn Sie möchten, können Sie auch nur die Biografie in Ihrer Muttersprache behalten; wir werden uns dann um die Übersetzung nach Einreichung Ihres Pull Requests kümmern.

- Ihr Professor-Ordner sollte nun so aussehen:
![Tutorial](assets/23.webp)
```plaintext
vorname-nachname/
├── fr.yml
├── it.yml
├── es.yml
├── en.yml
├── de.yml
├── pt.yml
├── ja.yml
├── vi.yml
├── professor.yml
└── assets/
    └── profil.webp
```
- Kehren Sie nun zu GitHub Desktop zurück.
- Auf der linken Seite Ihres Fensters sollten Sie alle Änderungen an den Dokumenten sehen, die spezifisch für Ihren Branch sind. Stellen Sie sicher, dass diese Änderungen korrekt sind:
![Tutorial](assets/24.webp)
- Wenn die Änderungen korrekt erscheinen, geben Sie einen Titel für Ihren Commit ein. Ein Commit ist ein Speichern der Änderungen, die am Branch vorgenommen wurden, begleitet von einer beschreibenden Nachricht, die es ermöglicht, die Entwicklung eines Projekts im Laufe der Zeit zu verfolgen.
- Sobald der Titel eingegeben ist, drücken Sie den blauen `Commit to [your branch]` Knopf, um diese Änderungen zu bestätigen:
![Tutorial](assets/25.webp)
- Klicken Sie dann auf den `Push origin` Knopf. Dies sendet Ihren Commit zu Ihrem Fork:
![Tutorial](assets/26.webp)
- Wenn Sie mit Ihren Änderungen für diesen Branch fertig sind, klicken Sie jetzt auf den `Preview Pull Request` Knopf:
![Tutorial](assets/27.webp)
- Sie können ein letztes Mal überprüfen, ob Ihre Änderungen korrekt sind, und dann auf den Button `Create pull request` klicken: ![tutorial](assets/28.webp) - Sie werden automatisch in Ihrem Browser auf GitHub zur Vorbereitungsseite des Pull Requests weitergeleitet. Ein Pull Request ist eine Anfrage, um die Änderungen von Ihrem Branch in den Hauptbranch des PlanB Network Repositories zu integrieren, was die Überprüfung und Diskussion der Änderungen vor ihrer Zusammenführung ermöglicht: ![tutorial](assets/29.webp)
- Geben Sie auf dieser Vorbereitungsseite einen Titel an, der die Änderungen, die Sie mit dem Quellrepository zusammenführen möchten, kurz zusammenfasst.
- Fügen Sie einen kurzen Kommentar hinzu, der diese Änderungen beschreibt.
- Nachdem Sie diese Schritte abgeschlossen haben, klicken Sie auf den grünen Button `Create pull request`, um die Anfrage zur Zusammenführung zu bestätigen: ![tutorial](assets/30.webp)
- Ihr PR wird dann im Tab `Pull Request` des Hauptrepositories von PlanB Network sichtbar sein. Alles, was Sie jetzt tun müssen, ist zu warten, bis ein Administrator Sie kontaktiert, um die Zusammenführung Ihres Beitrags zu bestätigen oder um eventuelle zusätzliche Änderungen anzufordern: ![tutorial](assets/31.webp)
- Nach der Zusammenführung Ihres PR mit dem Hauptbranch wird empfohlen, Ihren Arbeitsbranch (`add-professor-your-name`) zu löschen, um eine saubere Historie auf Ihrem Fork zu bewahren. GitHub wird Ihnen diese Option automatisch auf Ihrer PR-Seite anbieten: ![tutorial](assets/32.webp)
- In der GitHub Desktop-Software können Sie zurück zum Hauptbranch Ihres Forks (`dev`) wechseln: ![tutorial](assets/8.webp)
- Wenn Sie Änderungen an Ihrem Profil vornehmen möchten, nachdem Sie bereits Ihren PR eingereicht haben, hängt das Verfahren vom aktuellen Status Ihres PR ab:
	- Wenn Ihr PR noch offen ist und noch nicht zusammengeführt wurde, machen Sie die Änderungen lokal, während Sie auf demselben Branch bleiben. Sobald die Änderungen abgeschlossen sind, verwenden Sie den Button `Push origin`, um einen neuen Commit zu Ihrem noch offenen PR hinzuzufügen;
	- Falls Ihr PR bereits mit dem Hauptbranch zusammengeführt wurde, müssen Sie den Prozess neu starten, indem Sie einen neuen Branch erstellen und dann einen neuen PR einreichen. Stellen Sie sicher, dass Ihr lokales Repository mit dem PlanB Network Quellrepository synchronisiert ist, bevor Sie fortfahren.
