---
name: GitHub Desktop
description: Wie richtet man seine lokale Arbeitsumgebung ein?
---
![github](assets/cover.webp)

Die Mission von PlanB ist es, erstklassige Bildungsressourcen über Bitcoin in möglichst vielen Sprachen bereitzustellen. Alle Inhalte, die auf der Website veröffentlicht werden, sind Open-Source und werden auf GitHub gehostet, was es jedem ermöglicht, an der Bereicherung der Plattform teilzunehmen. Beiträge können verschiedene Formen annehmen: Korrigieren und Korrekturlesen bestehender Texte, Übersetzen in andere Sprachen, Aktualisieren von Informationen oder Erstellen neuer Tutorials, die auf unserer Website noch nicht verfügbar sind.

Wenn Sie zum PlanB-Netzwerk beitragen möchten, müssen Sie GitHub verwenden, um Änderungen vorzuschlagen. Dazu haben Sie zwei Möglichkeiten:
- **Direkt über die Web-Oberfläche von GitHub beitragen**: Dies ist die einfachste Methode. Wenn Sie Anfänger sind oder nur wenige kleine Beiträge leisten möchten, ist diese Option wahrscheinlich die beste für Sie;
- **Lokal mit Git beitragen**: Diese Methode eignet sich besser, wenn Sie regelmäßig oder bedeutende Beiträge zum PlanB-Netzwerk leisten möchten. Obwohl das Einrichten Ihrer lokalen Git-Umgebung auf Ihrem Computer zunächst komplex erscheinen mag, ist dieser Ansatz auf lange Sicht effizienter. Er ermöglicht eine flexiblere Verwaltung von Änderungen. Wenn Sie neu dabei sind, machen Sie sich keine Sorgen, **wir erklären den gesamten Prozess der Einrichtung Ihrer Umgebung in diesem Tutorial** (versprochen, Sie müssen keine Befehlszeilen eingeben ^^).

Wenn Sie keine Ahnung haben, was GitHub ist, oder wenn Sie mehr über die technischen Begriffe im Zusammenhang mit Git und GitHub erfahren möchten, empfehle ich Ihnen, unseren einführenden Artikel zu lesen, um sich mit diesen Konzepten vertraut zu machen.

https://planb.network/tutorials/others/basics-of-github



- Zunächst benötigen Sie natürlich ein GitHub-Konto. Wenn Sie bereits eines haben, können Sie sich anmelden, andernfalls können Sie unser Tutorial nutzen, um ein neues zu erstellen.

https://planb.network/tutorials/others/create-github-account



## Schritt 1: Installieren Sie GitHub Desktop

- Gehen Sie zu https://desktop.github.com/, um die GitHub Desktop-Software herunterzuladen. Diese Software ermöglicht es Ihnen, einfach mit GitHub zu interagieren, ohne ein Terminal verwenden zu müssen:
![github-desktop](assets/1.webp)
- Wenn Sie die Software zum ersten Mal starten, werden Sie aufgefordert, Ihr GitHub-Konto zu verbinden. Klicken Sie dazu auf `Sign in to GitHub.com`:
![github-desktop](assets/2.webp)
- Eine Authentifizierungsseite wird in Ihrem Browser geöffnet. Geben Sie Ihre E-Mail-Adresse und das bei der Erstellung Ihres Kontos gewählte Passwort ein, dann klicken Sie auf den `Sign in`-Button:
![github-desktop](assets/3.webp)
- Klicken Sie auf `Authorize desktop`, um die Verbindung zwischen Ihrem Konto und der Software zu bestätigen:
![github-desktop](assets/4.webp)
- Sie werden automatisch zur GitHub Desktop-Software weitergeleitet. Klicken Sie auf `Finish`: ![github-desktop](assets/5.webp)
- Wenn Sie gerade Ihr GitHub-Konto erstellt haben, werden Sie zu einer Seite weitergeleitet, die anzeigt, dass Sie noch keine Repositories erstellt haben. Stellen Sie zu diesem Zeitpunkt die GitHub Desktop-Software beiseite; wir werden später darauf zurückkommen: ![github-desktop](assets/6.webp)

## Schritt 2: Installieren Sie Obsidian

Lassen Sie uns mit der Installation der Schreibsoftware fortfahren. Hier haben Sie mehrere Optionen. Sie benötigen eine Software, die das Bearbeiten von Markdown-Dateien unterstützt, da das PlanB-Netzwerk dieses Format für Textdateien in seinem Repository verwendet.
Es gibt eine Vielzahl von Software, die speziell für das Bearbeiten von Markdown-Dateien entwickelt wurde, wie zum Beispiel Typora, das speziell für das Schreiben konzipiert wurde. Obwohl es nicht ideal ist, kann man sich auch für einen Code-Editor wie Visual Studio Code (VSC) oder Sublime Text entscheiden. Als Autor bevorzuge ich jedoch die Verwendung der Software Obsidian. Lassen Sie uns gemeinsam anschauen, wie man sie installiert und damit beginnt.

- Gehen Sie zu https://obsidian.md/download und laden Sie die Software herunter: ![github-desktop](assets/7.webp)
- Installieren Sie Obsidian, starten Sie die Software, wählen Sie Ihre Sprache und klicken Sie dann auf `Quick Start`: ![github-desktop](assets/8.webp)
- Sie gelangen zur Obsidian-Software. Momentan haben Sie keine Dateien geöffnet: ![github-desktop](assets/9.webp)

## Schritt 3: Forken Sie das PlanB Network Repository

- Gehen Sie zum Datenrepository des PlanB Network unter folgender Adresse: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Klicken Sie auf dieser Seite auf den `Fork`-Button oben rechts im Fenster: ![github-desktop](assets/11.webp)
- Im Erstellungsmenü können Sie die Standardeinstellungen belassen. Stellen Sie sicher, dass das Kästchen `Copy the dev branch only` angekreuzt ist, und klicken Sie dann auf den `Create fork`-Button: ![github-desktop](assets/12.webp)
- Sie gelangen dann zu Ihrem eigenen Fork des PlanB Network Repository: ![github-desktop](assets/13.webp)
Dieser Fork stellt ein separates Repository vom Original dar, obwohl es derzeit dieselben Daten enthält. Sie werden jetzt an diesem neuen Repository arbeiten.

Wir haben gewissermaßen eine Kopie des PlanB Network-Quellrepositorys erstellt. Ihr Fork (die Kopie) und das Originalrepository werden sich nun unabhängig voneinander entwickeln. Im Originalrepository können andere Mitwirkende neue Daten hinzufügen, während Sie an Ihrem Fork eigene Änderungen vornehmen.
Um die Konsistenz zwischen diesen beiden Repositories zu wahren, wird es notwendig sein, sie regelmäßig zu synchronisieren, damit sie dieselben Informationen abrufen. Um Ihre Änderungen an das Quellrepository zu senden, werden Sie das, was man einen **Pull Request** nennt, verwenden. Und um Änderungen vom Quellrepository in Ihren Fork zu integrieren, werden Sie den Befehl **Sync fork** verwenden, der in der GitHub-Webinterface verfügbar ist.
![github-desktop](assets/14.webp)

## Schritt 4: Klonen des Forks

- Kehren Sie zur GitHub Desktop-Software zurück. Ihr Fork sollte mittlerweile im Abschnitt `Your repositories` erscheinen. Wenn Sie ihn nicht sofort sehen, verwenden Sie den Doppelpfeil-Button, um die Liste zu aktualisieren. Wenn Ihr Fork erscheint, klicken Sie darauf, um ihn auszuwählen:
![github-desktop](assets/15.webp)
- Klicken Sie dann auf den blauen Button: `Clone [username]/bitcoin-educational-content`:
![github-desktop](assets/16.webp)
- Behalten Sie den Standardpfad bei. Um zu bestätigen, klicken Sie auf den blauen `Clone`-Button:
![github-desktop](assets/17.webp)
- Warten Sie, während GitHub Desktop Ihren Fork lokal klont:
![github-desktop](assets/18.webp)
- Nachdem Sie das Repository geklont haben, bietet Ihnen die Software zwei Optionen an. Sie müssen die erste wählen: `To contribute to the parent project`. Diese Wahl ermöglicht es Ihnen, Ihre zukünftigen Arbeiten als Beitrag zum übergeordneten Projekt (`PlanB-Network/bitcoin-educational-content`) zu präsentieren und nicht ausschließlich als Modifikation Ihres persönlichen Forks (`[username]/bitcoin-educational-content`). Sobald die Option gewählt ist, klicken Sie auf `Continue`: ![github-desktop](assets/19.webp)
- Ihr GitHub Desktop ist jetzt korrekt konfiguriert. Nun können Sie die Software im Hintergrund offen lassen, um den Modifikationen zu folgen, die wir vornehmen werden.
![github-desktop](assets/20.webp)
Was wir in diesem Stadium erreicht haben, ist die Erstellung einer lokalen Kopie Ihres Repositories, die auf GitHub gehostet wird. Zur Erinnerung, dieses Repository ist ein Fork des Quell-Repositories des PlanB Netzwerks. Sie werden in der Lage sein, Modifikationen an dieser lokalen Kopie vorzunehmen, wie das Hinzufügen von Tutorials, Übersetzungen oder Korrekturen. Sobald diese Modifikationen gemacht sind, werden Sie den Befehl **Push origin** verwenden, um Ihre lokalen Modifikationen zu Ihrem auf GitHub gehosteten Fork zu senden.

Sie können auch Modifikationen vom Fork abrufen, zum Beispiel während einer Synchronisation mit dem PlanB Netzwerk Repository. Dafür werden Sie den Befehl **Fetch origin** verwenden, um die Modifikationen zu Ihrer lokalen Kopie (Ihrem Klon) herunterzuladen, und dann den Befehl **Pull origin** verwenden, um sie mit Ihrer Arbeit zusammenzuführen. Dies ermöglicht es Ihnen, auf dem neuesten Stand der Entwicklungen des Projekts zu bleiben, während Sie effektiv beitragen.

![github-desktop](assets/21.webp)
## Schritt 5: Erstellen Sie ein neues Obsidian-Tresor

- Öffnen Sie die Obsidian-Software und klicken Sie auf das kleine Tresor-Symbol unten links im Fenster:
![github-desktop](assets/22.webp)
- Klicken Sie auf den `Open`-Button, um einen vorhandenen Ordner als Tresor zu öffnen: ![github-desktop](assets/23.webp)
- Ihr Datei-Explorer wird sich öffnen. Sie müssen den Ordner mit dem Titel `GitHub` lokalisieren und auswählen, der sich in Ihrem `Dokumente`-Verzeichnis unter Ihren Dateien befinden sollte. Dieser Pfad entspricht dem, den Sie während Schritt 4 festgelegt haben. Nachdem Sie den Ordner ausgewählt haben, bestätigen Sie seine Auswahl. Die Erstellung Ihres Tresors auf Obsidian wird dann auf einer neuen Seite der Software gestartet:

![github-desktop](assets/24.webp)
-> **Achtung**, es ist wichtig, nicht den `bitcoin-educational-content`-Ordner beim Erstellen eines neuen Tresors in Obsidian auszuwählen. Wählen Sie stattdessen den übergeordneten Ordner, `GitHub`. Wenn Sie den `bitcoin-educational-content`-Ordner auswählen, wird der Konfigurationsordner `.obsidian`, der Ihre lokalen Obsidian-Einstellungen enthält, automatisch in das Repository integriert. Dies wollen wir vermeiden, da es nicht notwendig ist, Ihre Obsidian-Konfigurationen zum PlanB Netzwerk Repository zu übertragen. Eine Alternative wäre, den `.obsidian`-Ordner zur `.gitignore`-Datei hinzuzufügen, aber diese Methode würde auch die `.gitignore`-Datei des Quell-Repositories ändern, was nicht wünschenswert ist.

- Auf der linken Seite des Fensters können Sie den Dateibaum mit Ihren verschiedenen GitHub-Repositories sehen, die lokal geklont wurden.
- Indem Sie auf die Pfeile neben den Ordnernamen klicken, können Sie sie erweitern, um auf die Unterordner der Repositories und deren Dokumente zuzugreifen:
![github-desktop](assets/25.webp)
- Vergessen Sie nicht, Obsidian auf den Dunkelmodus einzustellen: "Licht zieht Käfer an" ;)

## Schritt 6: Installieren Sie einen Code-Editor
Die meisten Ihrer Änderungen werden an Dateien im Markdown-Format (`.md`) vorgenommen. Um diese Dokumente zu bearbeiten, können Sie Obsidian verwenden, die Software, über die wir zuvor gesprochen haben. Das PlanB-Netzwerk verwendet jedoch auch andere Dateiformate, und Sie müssen einige davon ändern.
Beispielsweise müssen Sie beim Erstellen eines neuen Tutorials eine YAML-Datei (`.yml`) erstellen, um die Tags für Ihr Tutorial, dessen Titel und Ihre Lehrer-ID einzugeben. Obsidian bietet nicht die Möglichkeit, diesen Dateityp zu modifizieren, daher benötigen Sie einen Code-Editor.

Hierfür stehen Ihnen mehrere Optionen zur Verfügung. Obwohl das Standard-Notepad Ihres Computers für diese Änderungen verwendet werden kann, ist diese Lösung nicht ideal für saubere Arbeit. Ich empfehle, eine speziell für diesen Zweck entwickelte Software zu wählen, wie [VS Code](https://code.visualstudio.com/download) oder [Sublime Text](https://www.sublimetext.com/download). Sublime Text, besonders leichtgewichtig, wird für unsere Bedürfnisse mehr als ausreichend sein.
- Installieren Sie eines dieser Programme und halten Sie es für Ihre zukünftigen Änderungen bereit. ![github-desktop](assets/26.webp)
Herzlichen Glückwunsch! Ihre Arbeitsumgebung ist nun eingerichtet, um zum PlanB-Netzwerk beizutragen. Sie können jetzt unsere anderen spezifischen Tutorials für jeden Beitragstyp (Übersetzung, Korrekturlesen, Schreiben.

https://planb.network/tutorials/others

..) erkunden.
