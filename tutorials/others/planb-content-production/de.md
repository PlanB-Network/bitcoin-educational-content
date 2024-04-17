---
name: Beitrag - Obsidian
description: Wie kann man zum PlanB-Netzwerk mit GitHub und Obsidian beitragen?
---
![cover](assets/cover.jpeg)

Die Mission von PlanB ist es, erstklassige Bildungsressourcen über Bitcoin in möglichst vielen Sprachen bereitzustellen. Alle Inhalte, die auf der Website veröffentlicht werden, sind Open-Source und werden auf GitHub gehostet, was jedem die Möglichkeit bietet, an der Bereicherung der Plattform teilzunehmen. Beiträge können verschiedene Formen annehmen: Korrekturlesen und Korrigieren bestehender Texte, Übersetzen in andere Sprachen, Aktualisieren von Informationen oder Erstellen neuer Tutorials, die auf unserer Website noch nicht verfügbar sind.

Wenn Sie zum PlanB-Netzwerk beitragen möchten, sich aber mit der Nutzung von GitHub nicht wohl fühlen, ist dieses Tutorial speziell für Sie konzipiert. Wir werden detailliert beschreiben, wie man über GitHub zum PlanB-Netzwerk beitragen kann, während man Obsidian verwendet, ein Tool, das das Schreiben erleichtern soll.

Sie werden sehen, dass die Einrichtung des gesamten Arbeitsprozesses ziemlich langwierig ist, besonders wenn Sie GitHub zuvor noch nie verwendet haben. Die Nutzung von Git erleichtert jedoch die Zusammenarbeit beim Schreiben von Inhalten, da sie eine präzise Nachverfolgung von Änderungen, ein effizientes Versionsmanagement ermöglicht und auch die Überprüfung und Verbesserung von Inhalten durch andere Mitwirkende ermöglicht. Darüber hinaus werden Sie feststellen, dass Git Ihre Arbeit erheblich erleichtert, sobald der Arbeitsprozess auf Ihrem PC eingerichtet ist. Sie könnten sogar den Wunsch entwickeln, Git für Ihre anderen persönlichen Projekte zu verwenden, weil diese Software so effektiv ist.

## Git-Glossar
- **Fetch origin:** Befehl, der aktuelle Informationen und Änderungen aus einem entfernten Repository abruft, ohne sie mit Ihrer lokalen Arbeit zu verschmelzen.
- **Pull origin:** Befehl, der Aktualisierungen aus einem entfernten Repository abruft und sofort in Ihren lokalen Zweig integriert, um ihn zu synchronisieren.
- **Sync Fork:** Befehl auf GitHub, der Ihren Fork eines Projekts mit den neuesten Änderungen aus dem Quellrepository aktualisiert.
- **Push origin:** Befehl, der verwendet wird, um Ihre lokalen Änderungen an ein entferntes Repository zu senden.
- **Pull Request:** Eine Anfrage, die von einem Mitwirkenden gesendet wird, um anzuzeigen, dass sie Änderungen in einem Zweig in einem entfernten Repository vorgenommen haben und wünschen, dass diese Änderungen überprüft und möglicherweise in den Hauptzweig des Repositories integriert (gemerged) werden.
- **Commit:** Speichern Ihrer Änderungen. Ein Commit ist wie ein Sofort-Snapshot Ihrer Arbeit in einem bestimmten Moment, der hilft, eine Geschichte der Änderungen zu bewahren.
- **Branch:** Eine parallele Version des Repositories, die es Ihnen ermöglicht, an Änderungen zu arbeiten, ohne den Hauptzweig (im PlanB-Repository als "`dev`" bezeichnet) zu beeinflussen.
- **Merge:** Zusammenführen besteht darin, die Änderungen von einem Zweig in einen anderen zu integrieren. Es wird beispielsweise verwendet, um die Änderungen von einem Arbeitszweig in den Hauptzweig hinzuzufügen.
- **Fork:** Ein Repository zu forken bedeutet, eine Kopie dieses Repositories auf Ihrem eigenen GitHub-Konto zu erstellen, sodass Sie am Projekt arbeiten können, ohne das ursprüngliche Repository zu beeinflussen.
- **Clone:** Ein Repository zu klonen bedeutet, eine lokale Kopie auf Ihrem Computer zu erstellen, die Ihnen Zugang zu allen Dateien und der Änderungshistorie gibt.

- **Repository:** Ein Speicherplatz für ein Projekt auf GitHub. Es enthält alle Projektdateien sowie die Geschichte aller vorgenommenen Änderungen.

## Welche Art von Inhalten soll auf dem PlanB-Netzwerk geschrieben werden?
Wir suchen primär nach Tutorials zu Werkzeugen, die mit Bitcoin oder seinem Ökosystem in Verbindung stehen. Diese Inhalte können um sechs Hauptkategorien strukturiert werden:
- Wallet;
- Node;
- Mining;
- Händler;
- Börse;
- Privatsphäre.

Über diese speziell mit Bitcoin verbundenen Themen hinaus sucht PlanB auch nach Beiträgen zu Themen, die die individuelle Souveränität hervorheben, wie:
- Open-Source-Tools;
- Informatik;
- Kryptografie;
- Energie;
- Mathematik;
- Wirtschaft;
- DIY;
- LifeHacking...
Zum Beispiel haben wir derzeit Tutorials über Tails, Nostr oder GrapheneOS. Diese Tools stehen nicht direkt in Verbindung mit Bitcoin, aber es sind Systeme, die uns im Ansatz zur Souveränität in der digitalen Welt interessieren können oder beim Erlernen, wie man diese erreicht. Diese Inhalte können in eine Unterkategorie des Abschnitts "Andere" integriert werden.
Sie haben die Wahl, ein Tutorial von Grund auf neu zu gestalten oder ein Tutorial, das zuvor auf Ihrer Website veröffentlicht wurde (vorausgesetzt, Sie besitzen das Urheberrecht), erneut zu veröffentlichen, um es auch im PlanB-Netzwerk zu teilen, indem Sie einen Link zum Originalartikel hinzufügen.

Unabhängig von Ihrer Wahl, beachten Sie, dass alle Inhalte, die im PlanB-Netzwerk veröffentlicht werden, unter der freien Lizenz [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) stehen. Diese Lizenz erlaubt es jedem, Ihren Inhalt zu kopieren und potenziell zu modifizieren, vorausgesetzt, die Originalquelle wird gebührend genannt.

## Beitragungsprozess
Um ein Tutorial zur PlanB-Netzwerkseite hinzuzufügen, müssen Sie einen Pull Request im GitHub-Repository, das derzeit [sovereign-university-data](https://github.com/DecouvreBitcoin/sovereign-university-data) heißt, machen. Ihr Beitrag muss der Standardstruktur entsprechen und alle notwendigen Dateien beinhalten. Dies ist genau das, was wir in den folgenden Teilen detailliert beschreiben werden.

Dann wird ein Administrator Ihr Tutorial überprüfen. Falls Anpassungen erforderlich sind, wird er Sie informieren, damit die Änderungen vorgenommen werden können. Einmal genehmigt, wird das Tutorial in das Repository integriert.

## Schritt 1: Erstellen eines GitHub-Kontos
Wenn Sie sich noch nicht bei GitHub angemeldet haben, müssen Sie ein Konto erstellen. Gehen Sie dazu auf [https://github.com/signup](https://github.com/signup). Geben Sie Ihre E-Mail-Adresse ein, dann wählen Sie ein starkes Passwort. ![github](assets/1.webp)
Wählen Sie als Nächstes Ihren Benutzernamen. Sie haben die Möglichkeit, Ihre wahre Identität zu offenbaren oder die Verwendung eines Pseudonyms zu bevorzugen. Klicken Sie auf `Continue` und vervollständigen Sie das Captcha. Eine E-Mail mit einem Bestätigungscode wird Ihnen zugesandt; Sie müssen diesen eingeben, um die Erstellung Ihres Kontos abzuschließen.
![github](assets/2.webp)
Beantworten Sie die Fragen, wenn Sie möchten, dass GitHub Sie zu bestimmten Tools führt, oder klicken Sie auf `skip personalization`, um zu überspringen.
![github](assets/3.webp)
Wählen Sie den kostenlosen Plan, indem Sie auf den Button `Continue for free` klicken.
![github](assets/4.webp)
Sie werden dann zu Ihrem Dashboard weitergeleitet. Wenn Sie möchten, können Sie Ihr Konto anpassen, indem Sie auf Ihr Profilbild oben rechts auf dem Bildschirm klicken und dann das Menü `Settings` aufrufen.
![github](assets/5.webp)
In diesem Abschnitt haben Sie die Möglichkeit, ein neues Profilbild hinzuzufügen, einen Namen auszuwählen, Ihre Biografie anzupassen oder einen Link zu Ihrer persönlichen Website hinzuzufügen.
![github](assets/6.webp)
Ich rate Ihnen auch, einen Blick in das Menü `Password and authentication` zu werfen, um die Zwei-Faktor-Authentifizierung einzurichten.
![github](assets/7.webp)

## Schritt 2: Installieren von GitHub Desktop
Gehen Sie auf https://desktop.github.com/, um die GitHub Desktop-Software herunterzuladen. Diese Software ermöglicht es Ihnen, einfach mit GitHub zu interagieren, ohne ein Terminal verwenden zu müssen.
![github](assets/8.webp)
Beim ersten Start der Software werden Sie aufgefordert, Ihr GitHub-Konto zu verbinden. Klicken Sie dazu auf `Sign in to GitHub.com`.

![github](assets/9.webp)

Eine Authentifizierungsseite wird in Ihrem Browser geöffnet. Geben Sie Ihre E-Mail-Adresse und das im vorherigen Schritt gewählte Passwort ein, dann klicken Sie auf den Button `Sign in`.
![github](assets/10.webp)
Klicken Sie auf `Authorize desktop`, um die Verbindung zwischen Ihrem Konto und der Software zu bestätigen. ![github](assets/11.webp)
Sie werden automatisch zur GitHub Desktop-Software weitergeleitet. Klicken Sie auf `Finish`.

![github](assets/12.webp)

Wenn Sie gerade Ihr GitHub-Konto erstellt haben, werden Sie auf eine Seite weitergeleitet, die anzeigt, dass Sie noch keine Repositories erstellt haben. In diesem Stadium lassen Sie die GitHub Desktop-Software beiseite; wir werden später darauf zurückkommen.

![github](assets/13.webp)

## Schritt 3: Obsidian installieren
Lassen Sie uns mit der Installation der Schreibsoftware fortfahren. Hier haben Sie mehrere Optionen. Es gibt eine Vielzahl von Software, die auf das Bearbeiten von Markdown-Dateien spezialisiert ist, wie Typora, das speziell für das Schreiben entwickelt wurde. Obwohl es nicht ideal ist, können Sie sich auch für einen Code-Editor wie Visual Studio Code (VSC) oder Sublime Text entscheiden. Als Schriftsteller bevorzuge ich jedoch die Verwendung der Obsidian-Software. Lassen Sie uns gemeinsam sehen, wie man sie installiert und startet. ![github](assets/14.webp)
Gehen Sie zu https://obsidian.md/download und laden Sie die Software herunter. Installieren Sie sie, wählen Sie Ihre Sprache und klicken Sie dann auf `Quick Start`.

![github](assets/15.webp)

Sie gelangen zur Obsidian-Software. Im Moment haben Sie keine Dateien geöffnet.

![github](assets/16.webp)

## Schritt 4: Das PlanB Network Repository forken
Gehen Sie zum Datenrepository des PlanB Network unter folgender Adresse: [https://github.com/DecouvreBitcoin/sovereign-university-data](https://github.com/DecouvreBitcoin/sovereign-university-data). Wenn Sie nicht in Ihrem GitHub-Konto angemeldet sind, melden Sie sich bitte erneut an.
![github](assets/17.webp)
Klicken Sie auf dieser Seite auf den `Fork`-Button oben rechts im Fenster.
![github](assets/18.webp)
Im Erstellungsmenü können Sie die Standardeinstellungen beibehalten. Stellen Sie sicher, dass das Kästchen `Copy the dev branch only` angekreuzt ist, und klicken Sie dann auf den `Create fork`-Button.
![github](assets/19.webp)
Dann gelangen Sie zu Ihrem eigenen Fork des PlanB Network-Repositorys.
![github](assets/20.webp)
Dieser Fork stellt somit ein separates Repository vom Original dar, obwohl es derzeit dieselben Daten enthält. Sie werden jetzt an diesem neuen Repository arbeiten.

## Schritt 5: Ihr Repository klonen
Kehren Sie zur GitHub Desktop-Software zurück. Bis jetzt sollte Ihr Fork im Abschnitt `Your repositories` erscheinen. Wenn Sie ihn nicht sofort sehen, verwenden Sie den Doppelpfeil-Button, um die Liste zu aktualisieren. Wenn Ihr Fork erscheint, klicken Sie darauf, um ihn auszuwählen.

![github](assets/21.webp)

Klicken Sie dann auf den blauen Button: `Clone [username]/sovereign-university-data`.

![github](assets/22.webp)

Anschließend haben Sie die Möglichkeit, den lokalen Zugriffspfad auf Ihrem Computer zu ändern, wo der Klon Ihres Repositorys gespeichert wird. Sie können den Standardpfad beibehalten. Um zu bestätigen, klicken Sie auf den blauen `Clone`-Button.

![github](assets/23.webp)

Warten Sie, während GitHub Desktop Ihren Fork lokal klont.

![github](assets/24.webp)
Nachdem das Repository geklont wurde, bietet Ihnen die Software zwei Optionen. Sie müssen die erste auswählen: `To contribute to the parent project`. Diese Wahl ermöglicht es Ihnen, Ihre zukünftige Arbeit als Beitrag zum Elternprojekt (`DecouvreBitcoin/sovereign-university-data`) zu präsentieren und nicht ausschließlich als Änderung Ihres persönlichen Forks (`[username]/sovereign-university-data`). Sobald die Option ausgewählt ist, klicken Sie auf `Continue`.
![github](assets/25.webp)
Ihr GitHub Desktop ist nun korrekt konfiguriert. Jetzt können Sie die Software im Hintergrund offen lassen, um den Änderungen zu folgen, die wir vornehmen werden.
![github](assets/26.webp)

## Schritt 6: Erstellen Sie ein neues Obsidian-Tresor
Öffnen Sie die Obsidian-Software und klicken Sie auf das kleine Tresor-Symbol unten links im Fenster.

![github](assets/27.webp)

Klicken Sie auf den `Open`-Button, um einen vorhandenen Ordner als Tresor zu öffnen.

![github](assets/28.webp)

Ihr Datei-Explorer wird sich öffnen. Sie müssen den Ordner mit dem Titel `GitHub` finden und auswählen, der sich in Ihrem `Dokumente`-Verzeichnis unter Ihren Dateien befinden sollte. Dieser Pfad entspricht dem, den Sie in Schritt 5 festgelegt haben. Nachdem Sie den Ordner ausgewählt haben, bestätigen Sie seine Auswahl. Die Erstellung Ihres Tresors auf Obsidian wird dann auf einer neuen Seite der Software gestartet.

![github](assets/29.webp)

-> **Achtung**, es ist wichtig, nicht den Ordner `sovereign-university-data` zu wählen, wenn Sie einen neuen Tresor in Obsidian erstellen. Wählen Sie stattdessen den übergeordneten Ordner `GitHub`. Wenn Sie den Ordner `sovereign-university-data` auswählen, wird der Konfigurationsordner `.obsidian`, der Ihre lokalen Obsidian-Einstellungen enthält, automatisch in das Repository integriert. Dies möchten wir vermeiden, da es nicht notwendig ist, Ihre Obsidian-Konfigurationen in das PlanB Network-Repository zu übertragen. Eine Alternative wäre, den Ordner `.obsidian` zur `.gitignore`-Datei hinzuzufügen, aber diese Methode würde ebenfalls eine Änderung der `.gitignore`-Datei des Quell-Repositorys zur Folge haben, was nicht wünschenswert ist.

Auf der linken Seite des Fensters können Sie den Dateibaum mit Ihren verschiedenen GitHub-Repositories sehen, die lokal geklont wurden. Indem Sie auf die Pfeile neben den Ordnernamen klicken, können Sie sie erweitern, um auf die Unterordner der Repositories und deren Dokumente zuzugreifen.

![github](assets/30.webp)

Vergessen Sie nicht, Obsidian auf den Dunkelmodus einzustellen: "*Licht zieht Käfer an*" ;)

## Schritt 7: Installieren Sie einen Code-Editor
Die meisten Ihrer Änderungen werden an Dateien im Markdown-Format (`.md`) vorgenommen. Um diese Dokumente zu bearbeiten, können Sie Obsidian verwenden, die Software, über die wir zuvor gesprochen haben. Allerdings verwendet das PlanB Network andere Dateiformate, und einige davon müssen Sie ändern.
Beispielsweise müssen Sie beim Erstellen eines neuen Tutorials eine YAML (`.yml`)-Datei erstellen, um die Tags Ihres Tutorials, seinen Titel sowie Ihre Lehrer-ID einzuschließen. Obsidian bietet nicht die Möglichkeit, diese Art von Dateien zu ändern, daher benötigen Sie einen Code-Editor.
Hierfür stehen Ihnen mehrere Optionen zur Verfügung. Obwohl das Standard-Notepad auf Ihrem Computer verwendet werden kann, um diese Änderungen vorzunehmen, ist diese Lösung nicht ideal für saubere Arbeit. Ich empfehle eher, Software zu wählen, die speziell für diesen Zweck entwickelt wurde, wie [VS Code](https://code.visualstudio.com/download) oder [Sublime Text](https://www.sublimetext.com/download). Sublime Text, das besonders leichtgewichtig ist, wird für unsere Bedürfnisse mehr als ausreichend sein.
![github](assets/31.webp)
Installieren Sie eines dieser Programme und legen Sie es für später beiseite.

## Schritt 8: Fügen Sie einen neuen Lehrer hinzu (optional)
Wenn Sie zuvor zum PlanB Network beigetragen haben, haben Sie bereits eine Mitwirkenden-ID. Sie können diese in Ihrem Lehrerordner finden, der über [diese Seite](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/professors) zugänglich ist. Wenn dies der Fall ist, können Sie diesen Schritt überspringen und direkt zu Schritt 9 gehen.
![github](assets/32.webp)
Wenn Sie noch nicht zum PlanB-Netzwerk beigetragen haben, müssen Sie Ihr Profil erstellen, damit Ihr Name in Ihren zukünftigen Tutorials erscheint. Dazu beginnen wir mit der Erstellung eines neuen Zweigs, der Ihrem Lehrerprofil gewidmet ist. Ein Zweig in Git ist eine parallele Version des Projekts, die es Ihnen ermöglicht, Änderungen vorzunehmen, ohne den Hauptzweig zu beeinflussen, bis die Arbeit bereit ist, zusammengeführt zu werden.
Bevor Sie einen neuen Zweig erstellen, ist es wichtig sicherzustellen, dass Sie an der aktuellsten Version des Projekts arbeiten, um das Risiko von Konflikten beim Zusammenführen Ihrer Änderungen zu verringern. Öffnen Sie dazu Ihren Browser und gehen Sie zur Seite Ihres Forks des PlanB-Repositorys. Dies ist der Fork, den Sie auf GitHub in Schritt 4 erstellt haben. Die URL Ihres Forks sollte wie folgt aussehen:

`https://github.com/[Benutzername]/sovereign-university-data`
![github](assets/34.webp)
Stellen Sie sicher, dass Sie sich im Hauptzweig `dev` befinden, und klicken Sie dann auf die Schaltfläche `Sync fork`. Wenn Ihr Fork nicht auf dem neuesten Stand ist, wird GitHub anbieten, Ihren Zweig zu aktualisieren. Führen Sie diese Synchronisierung durch. Ist Ihr Zweig hingegen bereits auf dem neuesten Stand, wird GitHub Sie informieren.
![github](assets/35.webp)
Jetzt, da Ihr Fork auf GitHub mit dem Quell-Repository des PlanB-Netzwerks synchronisiert ist, ist es an der Zeit, auch das lokale Repository auf Ihrem Computer zu aktualisieren. Öffnen Sie die GitHub Desktop-Software und stellen Sie sicher, dass Ihr Fork in der oberen linken Ecke des Fensters korrekt ausgewählt ist.
Klicken Sie auf die Schaltfläche `Fetch origin`. Wenn Ihr lokales Repository bereits auf dem neuesten Stand ist, wird GitHub Desktop keine weiteren Aktionen vorschlagen. Andernfalls erscheint die Option `Pull origin`. Klicken Sie auf diese Schaltfläche, um Ihr lokales Repository zu aktualisieren.

Nachdem Sie Ihr Repository mit den neuesten Beiträgen synchronisiert haben, sind Sie bereit, einen neuen Arbeitszweig zu erstellen. Verwenden Sie weiterhin GitHub Desktop und stellen Sie sicher, dass Sie sich im Hauptzweig `dev` befinden.

Klicken Sie auf diesen Zweig und dann auf die Schaltfläche `New Branch`.

Stellen Sie sicher, dass der neue Zweig auf dem Quell-Repository basiert, nämlich `DecouvreBitcoin/sovereign-university-data`. Benennen Sie Ihren Zweig so, dass der Titel klar seinen Zweck angibt, und verwenden Sie Bindestriche, um jedes Wort zu trennen. Da dieser Zweig für das Hinzufügen eines Professorenprofils vorgesehen ist, könnte ein Beispielname sein: `add-professor-[Ihr-Name]`. Nachdem Sie den Namen eingegeben haben, klicken Sie auf `Create branch`, um dessen Erstellung zu bestätigen.

Klicken Sie nun auf die Schaltfläche `Publish branch`, um Ihren neuen Arbeitszweig in Ihrem Online-Fork auf GitHub zu speichern.

An diesem Punkt sollten Sie sich in GitHub Desktop auf Ihrem neuen Zweig befinden. Das bedeutet, dass alle lokal auf Ihrem Computer vorgenommenen Änderungen ausschließlich in diesem spezifischen Zweig aufgezeichnet werden. Solange dieser Zweig in GitHub Desktop ausgewählt bleibt, entsprechen die lokal auf Ihrem Gerät sichtbaren Dateien denen dieses Zweigs (`add-professor-Ihr-Name`) und nicht denen des Hauptzweigs (`dev`).

Um Ihr Professorenprofil hinzuzufügen, öffnen Sie Ihren Datei-Explorer und gehen Sie zu Ihrem lokalen Repository im Ordner `professors`. Sie finden ihn unter dem Pfad: `\GitHub\sovereign-university-data\professors`.

Erstellen Sie in diesem Ordner einen neuen Ordner, der mit Ihrem Namen oder Pseudonym benannt ist. Stellen Sie sicher, dass im Ordnernamen keine Leerzeichen enthalten sind. Wenn Ihr Name also "Loic Pandul" ist und kein anderer Professor diesen Namen hat, sollte der zu erstellende Ordner `loic-pandul` heißen.

Um die Aufgabe zu erleichtern, können Sie bereits alle Dokumente von einem anderen Professor in Ihren eigenen Ordner kopieren und einfügen. Anschließend werden wir diese Dokumente bearbeiten, um sie gemäß Ihrem Profil anzupassen.
Beginnen Sie damit, zum Ordner `assets` zu navigieren. Löschen Sie das Profilbild des Professors, das Sie zuvor kopiert haben, und ersetzen Sie es durch Ihr eigenes Profilbild. Es ist zwingend erforderlich, dass dieses Bild im `.webp`-Format vorliegt und den Namen `profile` trägt, was den vollständigen Dateinamen `profile.webp` ergibt. Beachten Sie, dass dieses Bild im Internet veröffentlicht und für jeden zugänglich sein wird. ![github](assets/45.webp)

Öffnen Sie als Nächstes die Datei `professor.yml` mit Ihrem Code-Editor (VSC oder Sublime Text). Sie gelangen zu der Datei, die von einem bestehenden Professor kopiert wurde.

![github](assets/46.webp)

Sie müssen dann die vorhandenen Informationen durch Ihre eigenen aktualisieren:
- **name:** geben Sie Ihren Namen oder Ihr Pseudonym ein;
- **links:** geben Sie Ihre Konten in sozialen Netzwerken wie Twitter und Nostr an, sowie die URL Ihrer persönlichen Website (optional);
- **affiliation:** nennen Sie den Namen des Unternehmens, bei dem Sie angestellt sind (optional);
- **tags:** geben Sie Ihre Spezialisierungsgebiete aus der folgenden Liste an, wobei Sie Ihre eigenen Themen hinzufügen können. Achten Sie jedoch darauf, die Anzahl der Tags auf höchstens 4 zu begrenzen, um eine gute Benutzeroberfläche zu gewährleisten:
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
- **tips:** geben Sie Ihre Lightning-Adresse für Spenden an, damit Leser Ihrer zukünftigen Tutorials Ihnen einige Sats senden können (optional);
- **company:** falls Sie eine besitzen, geben Sie den Namen Ihres Unternehmens an (optional).

![github](assets/47.webp)

Sie müssen auch die `contributor-id` ändern. Dieser Identifikator wird verwendet, um Sie auf der Website zu erkennen, wird jedoch außerhalb von GitHub nicht öffentlich gemacht. Sie sind frei, eine beliebige Kombination aus zwei Wörtern zu wählen, die sich auf die englische Liste der 2048 Wörter aus BIP39 bezieht, hier zugänglich: [https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Vergessen Sie nicht, zwischen den beiden gewählten Wörtern einen Bindestrich einzufügen. Zum Beispiel habe ich hier `crazy-cactus` gewählt.

![github](assets/48.webp)

Sobald Sie die Änderungen am Dokument `professor.yml` abgeschlossen haben, klicken Sie auf `Datei > Speichern`, um Ihre Datei zu speichern. Sie können dann Ihren Code-Editor schließen.

![github](assets/49.webp)
Es ist an der Zeit, mit dem Schreiben Ihrer Biografie zu beginnen. Innerhalb Ihrer Lehrerdatei können Sie Dokumente in Sprachen löschen, die Sie nicht betreffen und die ursprünglich von einem anderen Lehrer kopiert wurden. Behalten Sie ausschließlich die Datei, die Ihrer Muttersprache entspricht. In meinem Fall habe ich beispielsweise nur die Datei `fr.yml` behalten, da meine Sprache Französisch ist.
![github](assets/50.webp)

Doppelklicken Sie auf diese Datei, um sie mit Ihrem Code-Editor zu öffnen. In dieser Datei haben Sie die Möglichkeit, Ihre vollständige Biografie im Abschnitt `bio` und eine Zusammenfassung oder einen prägnanten Titel unter `short_bio` zu schreiben.

![github](assets/51.webp)

Nachdem Sie Ihr Dokument `fr.yml` gespeichert haben, ist es notwendig, eine Kopie dieser Datei für jede der folgenden sechs Sprachen zu erstellen:
- Deutsch (DE);
- Englisch (EN);
- Französisch (FR);
- Spanisch (ES);
- Italienisch (IT);
- Portugiesisch (PT).
Fügen Sie Ihre Originaldatei ein und übersetzen Sie jedes Dokument in die entsprechende Sprache. Wenn Sie die Sprache beherrschen, können Sie die Übersetzung manuell durchführen. Andernfalls können Sie gerne ein automatisches Übersetzungstool oder einen Chatbot verwenden. Wenn Sie möchten, können Sie auch nur die Biografie in Ihrer Muttersprache beibehalten; wir werden uns dann um die Übersetzung kümmern, nachdem Sie Ihren Pull Request eingereicht haben.
![github](assets/52.webp)

Ihr Lehrerverzeichnis sollte dann so aussehen:

![github](assets/53.webp)

Kehren Sie nun zu GitHub Desktop zurück. Auf der linken Seite Ihres Fensters sollten Sie alle Änderungen an den Dokumenten sehen, die spezifisch für Ihren Branch sind. Stellen Sie sicher, dass diese Änderungen tatsächlich korrekt sind.

![github](assets/54.webp)

Wenn die Änderungen für Sie korrekt erscheinen, geben Sie einen Titel für Ihren Commit ein. Ein Commit ist das Speichern der Änderungen, die am Branch vorgenommen wurden, begleitet von einer beschreibenden Nachricht, die es ermöglicht, die Entwicklung eines Projekts über die Zeit zu verfolgen. Sobald der Titel eingegeben ist, drücken Sie den blauen `Commit to [your branch]`-Button, um diese Änderungen zu bestätigen.

![github](assets/55.webp)

Klicken Sie dann auf den `Push origin`-Button. Dadurch wird Ihr Commit zu Ihrem Fork gesendet.

![github](assets/56.webp)

Wenn Sie Ihre Änderungen für diesen Branch abgeschlossen haben, klicken Sie jetzt auf den `Preview Pull Request`-Button.

![github](assets/57.webp)

Sie können ein letztes Mal überprüfen, ob Ihre Änderungen tatsächlich korrekt sind, und dann auf den `Create pull request`-Button klicken.

![github](assets/58.webp)

Sie werden automatisch in Ihrem Browser auf GitHub zur Seite für die Vorbereitung Ihres Pull Requests weitergeleitet. Ein Pull Request ist eine Anfrage, um die Änderungen Ihres Branches in den Hauptbranch des PlanB Network-Repositorys zu integrieren, was die Überprüfung und Diskussion von Änderungen vor ihrer Zusammenführung ermöglicht.
![github](assets/59.webp)
Auf dieser Vorbereitungsseite geben Sie einen Titel an, der kurz die Änderungen zusammenfasst, die Sie mit dem Quell-Repository zusammenführen möchten. Fügen Sie einen kurzen Kommentar hinzu, der diese Änderungen beschreibt. Nach Abschluss dieser Schritte klicken Sie auf den grünen `Create pull request`-Button, um die Anfrage zur Zusammenführung zu bestätigen. ![github](assets/60.webp)
Ihr PR wird dann im `Pull Request`-Tab des Hauptrepositorys von PlanB Network sichtbar sein. Sie müssen nun warten, bis ein Administrator Sie kontaktiert, um die Zusammenführung Ihres Beitrags zu bestätigen oder um zusätzliche Änderungen anzufordern.
![github](assets/61.webp)
Nachdem Ihr PR mit dem Hauptbranch zusammengeführt wurde, wird empfohlen, Ihren Arbeitsbranch (`add-professor-your-name`) zu löschen, um eine saubere Historie auf Ihrem Fork zu bewahren. GitHub wird Ihnen diese Option automatisch auf Ihrer PR-Seite anbieten:
![github](assets/62.webp)
In der GitHub Desktop-Software können Sie zurück zum Hauptbranch Ihres Forks (`dev`) wechseln.

![github](assets/63.webp)

Wenn Sie Änderungen an Ihrem Beitrag vornehmen möchten, nachdem Sie Ihren PR bereits eingereicht haben, hängt das Vorgehen vom aktuellen Status Ihres PR ab:
- Wenn Ihr PR noch offen ist und noch nicht zusammengeführt wurde, nehmen Sie die Änderungen lokal vor, während Sie auf demselben Branch bleiben. Sobald die Änderungen abgeschlossen sind, verwenden Sie den `Push origin`-Button, um einen neuen Commit zu Ihrem noch offenen PR hinzuzufügen;
- Falls Ihr PR bereits mit dem Hauptbranch zusammengeführt wurde, müssen Sie den Prozess von vorne beginnen, indem Sie einen neuen Branch erstellen und dann einen neuen PR einreichen. Stellen Sie sicher, dass Ihr lokales Repository mit dem Quell-Repository von PlanB Network synchronisiert ist, bevor Sie fortfahren.

## Schritt 9: Hinzufügen eines neuen Tutorials
Herzlichen Glückwunsch, Sie haben alle Vorbereitungsschritte abgeschlossen! Sie sind jetzt bereit, zum PlanB-Netzwerk beizutragen. Von nun an müssen Sie für jeden neuen Artikel, den Sie veröffentlichen möchten, einen neuen Branch von `dev` erstellen. Ein Branch in Git ist eine parallele Version des Projekts, die es Ihnen ermöglicht, Änderungen vorzunehmen, ohne den Hauptbranch zu beeinflussen, bis die Arbeit bereit ist, zusammengeführt zu werden.
Bevor Sie fortfahren und einen neuen Branch erstellen, ist es wichtig sicherzustellen, dass Sie an der aktuellsten Version des Projekts arbeiten, um das Risiko von Konflikten beim Zusammenführen Ihrer Änderungen zu reduzieren. Dazu öffnen Sie Ihren Browser und gehen zur Seite Ihres Forks des PlanB-Repositorys. Dies ist der Fork, den Sie auf GitHub in Schritt 4 erstellt haben. Die URL Ihres Forks sollte wie folgt aussehen: `https://github.com/[Ihr-Benutzername]/sovereign-university-data`.
![github](assets/34.webp)
Stellen Sie sicher, dass Sie sich im Hauptbranch `dev` befinden, und klicken Sie dann auf den `Sync fork`-Button. Wenn Ihr Fork nicht auf dem neuesten Stand ist, wird GitHub anbieten, Ihren Branch zu aktualisieren. Führen Sie dieses Update durch. Ist Ihr Branch hingegen bereits auf dem neuesten Stand, wird GitHub Sie darüber informieren. ![github](assets/35.webp)
Jetzt, da Ihr Fork auf GitHub mit dem Quellrepository des PlanB-Netzwerks synchronisiert ist, ist es an der Zeit, auch das lokale Repository auf Ihrem Computer zu aktualisieren. Öffnen Sie die GitHub Desktop-Software und stellen Sie sicher, dass Ihr Fork in der oberen linken Ecke des Fensters korrekt ausgewählt ist.

![github](assets/36.webp)

Klicken Sie auf den `Fetch origin`-Button. Wenn Ihr lokales Repository bereits auf dem neuesten Stand ist, wird GitHub Desktop keine weiteren Aktionen vorschlagen. Andernfalls erscheint die Option `Pull origin`. Klicken Sie auf diesen Button, um Ihr lokales Repository zu aktualisieren.

![github](assets/37.webp)

Nachdem Sie Ihr Repository mit den neuesten Beiträgen synchronisiert haben, sind Sie bereit, einen neuen Arbeitsbranch zu erstellen. Noch immer in GitHub Desktop, überprüfen Sie, dass Sie tatsächlich im Hauptbranch `dev` sind.

![github](assets/38.webp)

Klicken Sie auf diesen Branch und dann auf den `New Branch`-Button.

![github](assets/64.webp)

Stellen Sie sicher, dass der neue Branch auf dem Quellrepository basiert, nämlich `DecouvreBitcoin/sovereign-university-data`. Benennen Sie Ihren Branch so, dass der Titel klar seinen Zweck angibt, indem Sie Wörter durch Bindestriche trennen. Nehmen wir zum Beispiel an, unser Ziel ist es, ein Tutorial zur Verwendung der Sparrow Wallet-Software zu schreiben. In diesem Fall könnte der Arbeitsbranch, der diesem Tutorial gewidmet ist, benannt werden als: `tuto-sparrow-wallet-loic`. Sobald der passende Name eingegeben ist, müssen Sie nur noch auf `Create branch` klicken, um die Erstellung des Branchs zu bestätigen.

![github](assets/65.webp)

Klicken Sie nun auf den `Publish branch`-Button, um Ihren neuen Arbeitsbranch in Ihrem Online-Fork auf GitHub zu speichern.

![github](assets/66.webp)

An diesem Punkt sollten Sie sich in GitHub Desktop auf Ihrem neuen Branch befinden. Das bedeutet, dass alle lokal auf Ihrem Computer vorgenommenen Änderungen ausschließlich auf diesem spezifischen Branch aufgezeichnet werden. Solange dieser Branch in GitHub Desktop ausgewählt bleibt, entsprechen die lokal auf Ihrem Rechner sichtbaren Dateien denen dieses Branchs (`tuto-sparrow-wallet-loic`) und nicht denen des Hauptbranchs (`dev`).

![github](assets/68.webp)
Jetzt, da der Arbeitszweig erstellt wurde, ist es an der Zeit, Ihr neues Tutorial zu integrieren. Dazu öffnen Sie Ihren Dateimanager und navigieren zum Ordner `sovereign-university-data`, der den lokalen Klon Ihres Repositories darstellt. Normalerweise sollten Sie ihn unter `Documents\GitHub\sovereign-university-data` finden. Innerhalb dieses Verzeichnisses ist es notwendig, den entsprechenden Unterordner für die Platzierung Ihres Tutorials zu lokalisieren. Die Organisation der Ordner spiegelt die verschiedenen Abschnitte der PlanB Network-Website wider. In unserem Beispiel, da wir ein Tutorial über Sparrow Wallet hinzufügen möchten, ist es angebracht, zum folgenden Pfad zu gehen: `sovereign-university-data\tutorials\wallet`, der dem Abschnitt `WALLET` auf der Website entspricht.![github](assets/69.webp)

Innerhalb des `wallet`-Ordners müssen Sie ein neues Verzeichnis speziell für Ihr Tutorial erstellen. Der Name dieses Ordners sollte die in dem Tutorial behandelte Software evozieren, wobei darauf zu achten ist, Wörter mit Bindestrichen zu verbinden. In meinem Beispiel wird der Ordner `sparrow-wallet` betitelt.

![github](assets/70.webp)

In diesem neuen Ordner, der Ihrem Tutorial gewidmet ist, ist es angebracht, verschiedene Elemente vorzubereiten:
- Erstellen Sie einen `assets`-Ordner, der dazu bestimmt ist, alle Illustrationen aufzunehmen, die für Ihr Tutorial notwendig sind;
	- Innerhalb dieses `assets`-Ordners müssen Sie 6 Unterordner mit den Namen `fr`, `de`, `en`, `it`, `es` und `pt` erstellen, um die Visuals entsprechend den zugehörigen Sprachen zu klassifizieren.
- Eine `tutorial.yml`-Datei muss erstellt werden, um die Details zu Ihrem Tutorial aufzuzeichnen;
- Eine Datei im Markdown-Format ist zu erstellen, um den eigentlichen Inhalt Ihres Tutorials zu schreiben. Diese Datei muss gemäß dem Sprachcode der Verfassung betitelt werden. Zum Beispiel muss für ein auf Französisch geschriebenes Tutorial die Datei `fr.md` genannt werden.

Die Organisation Ihres Ordners sollte so aussehen:

![github](assets/71.webp)

Zu Beginn öffnen Sie Ihre `tutorial.yml`-Datei mit Ihrem Code-Editor. Füllen Sie sie mit den unten angegebenen Informationen aus:
- **builder**: Geben Sie den Titel Ihres Tutorials ein, der sowohl präzise als auch evokativ in Bezug auf den Inhalt sein muss, den Sie präsentieren werden;
- **tags**: Bestimmen Sie eine Reihe von Schlüsselwörtern, die eng mit dem Thema Ihres Artikels verwandt sind, um dessen Suche und Indizierung zu erleichtern;
- **category**: Wählen Sie eine passende Unterkategorie unter den auf der PlanB-Website verfügbaren aus, basierend auf dem Inhalt Ihres Tutorials. Zum Beispiel, für ein Tutorial, das mit dem Abschnitt `WALLET` verwandt ist, sind die verfügbaren Optionen `Desktop`, `Hardware` und `Mobile`;
- **level**: Geben Sie den Schwierigkeitsgrad Ihres Tutorials an, indem Sie sich für eine der folgenden vier Kategorien entscheiden:
	- Anfänger (`beginner`),
	- Fortgeschrittene (`intermediary`),
	- Fortgeschrittene (`advanced`),
- Experte (`expert`).- **professor**: Geben Sie Ihre Mitwirkenden-ID ein, wie sie in Ihrem Profil als Professor erscheint. Für weitere Details siehe Schritt 8 dieses Artikels;
- **link** (optional): Wenn Sie eine Quellwebsite für das Tutorial, das Sie entwickeln, wie Ihre eigene persönliche Seite, nennen möchten, können Sie hier den entsprechenden Link hinzufügen.

![github](assets/72.webp)

Sobald Sie die Bearbeitung Ihrer `tutorial.yml`-Datei abgeschlossen haben, speichern Sie Ihr Dokument, indem Sie auf `Datei > Speichern` klicken. Sie können jetzt Ihren Code-Editor schließen.

![github](assets/73.webp)
Im Ordner `assets` müssen Sie eine Datei mit dem Namen `logo.webp` hinzufügen, die als Thumbnail für Ihren Artikel dienen wird. Dieses Bild, das im `.webp`-Format vorliegen muss, sollte quadratische Abmessungen haben, um sich der Benutzeroberfläche anzupassen. Sie können frei das Logo der in dem Tutorial behandelten Software oder ein anderes relevantes Bild wählen, vorausgesetzt, es ist frei von Rechten.
Fügen Sie außerdem ein Bild mit dem Titel `cover.jpeg` am gleichen Ort hinzu. Dieses Bild wird oben in Ihrem Tutorial angezeigt. Stellen Sie sicher, dass dieses Bild, wie das Logo, die Nutzungsrechte respektiert und für den Kontext Ihres Tutorials geeignet ist.

![github](assets/74.webp)

Die Sprachunterordner im Ordner `assets` dienen dazu, die Diagramme und Visualisierungen zu organisieren, die Ihr Tutorial begleiten werden. Wenn Ihre Bilder Text enthalten, sollten Sie erwägen, sie für jede betroffene Sprache zu übersetzen, um Ihren Inhalt einem internationalen Publikum zugänglich zu machen.

**-> Tipp:** Wenn Sie Dateien öffentlich teilen, wie zum Beispiel Bilder, ist es wichtig, überflüssige Metadaten zu entfernen. Diese können sensible Informationen enthalten, wie Standortdaten, Erstellungsdaten oder Details über den Autor. Um Ihre Privatsphäre zu schützen, ist es ratsam, diese Metadaten zu löschen. Um diese Operation zu vereinfachen, können Sie spezialisierte Werkzeuge wie [Exif Cleaner](https://exifcleaner.com/) verwenden, die das Bereinigen der Metadaten eines Dokuments durch einfaches Ziehen und Ablegen ermöglichen.

Nun können Sie Ihre Datei öffnen, die Ihr Tutorial beherbergen wird, benannt nach dem Code Ihrer Sprache, wie `de.md`. Gehen Sie zu Obsidian, auf der linken Seite des Fensters, scrollen Sie durch den Ordnerbaum, bis Sie den Ordner Ihres Tutorials und die gesuchte Datei erreichen.

![github](assets/75.webp)

Klicken Sie auf die Datei, um sie zu öffnen.

![github](assets/76.webp)

Wir beginnen damit, den Abschnitt `Properties` am Anfang des Dokuments auszufüllen. Für den Fall, dass dieser Abschnitt in Ihrer Datei fehlt (wenn das Dokument völlig leer ist), können Sie ihn reproduzieren, indem Sie ihn aus einem anderen vorhandenen Tutorial kopieren.

![github](assets/77.webp)
Sie können ihn auch manuell auf diese Weise mit Ihrem Code-Editor hinzufügen:
![github](assets/78.webp)

Füllen Sie den Namen Ihres Tutorials sowie eine kurze Beschreibung desselben aus.

![github](assets/79.webp)

Fügen Sie dann Ihr Cover-Bild am Anfang Ihres Tutorials hinzu. Dazu tippen Sie:

`![cover-sparrow](assets/cover.jpeg)`

Diese Syntax wird immer dann nützlich sein, wenn es notwendig ist, ein Bild zu Ihrem Tutorial hinzuzufügen. Das Ausrufezeichen zeigt an, dass es sich um ein Bild handelt, wobei der alternative Text (alt) zwischen den Klammern angegeben ist. Der Pfad zum Bild wird zwischen den Klammern angegeben.

![github](assets/80.webp)

Fahren Sie mit dem Schreiben Ihres Tutorials fort, indem Sie Ihren Inhalt verfassen. Wenn Sie einen Untertitel integrieren möchten, wenden Sie das entsprechende Markdown-Format an, indem Sie den Text mit `##` voranstellen.

![github](assets/81.webp)

Wenn Sie visuelle Elemente zu Ihrem Tutorial hinzufügen, stellen Sie sicher, dass Sie den Pfad auswählen, der der Sprache Ihres Inhalts entspricht. Zum Beispiel:

`![sparrow](assets/1.webp)`

![github](assets/82.webp)

Wenn Ihr visuelles Element Text enthält, wie zum Beispiel ein Diagramm, ist es ratsam, es in die sechs vorgeschlagenen Sprachen (Deutsch, Englisch, Französisch, Italienisch, Spanisch und Portugiesisch) zu übersetzen und jede übersetzte Version in ihrem eigenen sprachspezifischen Unterordner innerhalb des `assets`-Ordners zu platzieren.
Bilder müssen sequenziell nach ihrer Erscheinungsreihenfolge im Tutorial nummeriert werden. Das erste Bild wird also `1.webp` genannt, das zweite `2.webp` und so weiter. Sie können verschiedene Bildformate wie `jpeg`, `png` oder `webp` verwenden.![github](assets/83.webp)
Sobald Sie Ihr Tutorial in der Sprache Ihrer Wahl fertiggestellt haben, besteht der nächste Schritt darin, einen Pull Request zu übermitteln. Der Administrator wird dann die fünf fehlenden Übersetzungen Ihres Tutorials hinzufügen, dank unserer automatisierten Übersetzungsmethode. Um mit dem Pull Request fortzufahren, öffnen Sie die GitHub Desktop-Software. Diese sollte automatisch die Änderungen erkennen, die Sie lokal im Vergleich zum ursprünglichen Repository gemacht haben. Überprüfen Sie vor dem Fortfahren sorgfältig auf der linken Seite der Schnittstelle, ob diese Änderungen genau dem entsprechen, was Sie erwartet haben.

![github](assets/84.webp)

Wenn die Änderungen für Sie korrekt erscheinen, fügen Sie einen Titel für Ihren Commit hinzu. Ein Commit ist eine Speicherung der vorgenommenen Änderungen am Branch, begleitet von einer beschreibenden Nachricht, die es ermöglicht, die Entwicklung eines Projekts über die Zeit zu verfolgen. Sobald der Titel eingegeben ist, drücken Sie den blauen `Commit to [your branch]`-Button, um diese Änderungen zu validieren.

![github](assets/85.webp)

Klicken Sie dann auf den `Push origin`-Button. Dies wird Ihren Commit zu Ihrem Fork senden.

![github](assets/86.webp)
Wenn Sie Ihre Bearbeitungen für diesen Branch abgeschlossen haben, klicken Sie jetzt auf den `Preview Pull Request`-Button.
![github](assets/87.webp)

Sie können ein letztes Mal überprüfen, ob Ihre Änderungen korrekt sind, dann klicken Sie auf den `Create pull request`-Button.

![github](assets/88.webp)

Sie werden automatisch in Ihrem Browser auf GitHub zur Vorbereitungsseite Ihres Pull Requests weitergeleitet. Ein Pull Request ist eine Anfrage, um die Änderungen von Ihrem Branch in den Hauptbranch des PlanB Network-Repositorys zu integrieren, was die Überprüfung und Diskussion der Änderungen vor ihrer Zusammenführung ermöglicht.
![github](assets/89.webp)
Auf dieser Vorbereitungsseite geben Sie einen Titel an, der kurz die Modifikationen zusammenfasst, die Sie mit dem Quell-Repository zusammenführen möchten. Fügen Sie einen kurzen Kommentar hinzu, der diese Änderungen beschreibt. Nach Abschluss dieser Schritte klicken Sie auf den grünen `Create pull request`-Button, um die Zusammenführungsanfrage zu bestätigen.
![github](assets/90.webp)
Ihr PR wird dann im `Pull Request`-Tab des Hauptrepositorys von PlanB Network sichtbar sein. Jetzt müssen Sie nur noch warten, bis ein Administrator Sie kontaktiert, um die Zusammenführung Ihres Beitrags zu bestätigen oder um zusätzliche Änderungen anzufordern.
![github](assets/91.webp)
Nach der Zusammenführung Ihres PR mit dem Hauptbranch wird empfohlen, Ihren Arbeitsbranch (`tuto-sparrow-wallet`) zu löschen, um eine saubere Historie auf Ihrem Fork zu bewahren. GitHub wird Ihnen diese Option automatisch auf der Seite Ihres PR anbieten:
![github](assets/92.webp)
In der GitHub Desktop-Software können Sie zurück zum Hauptbranch Ihres Forks (`dev`) wechseln.

![github](assets/63.webp)

Wenn Sie Änderungen an Ihrem Beitrag vornehmen möchten, nachdem Sie bereits Ihren PR eingereicht haben, hängt das Verfahren vom aktuellen Zustand Ihres PR ab:
- Wenn Ihr PR noch offen ist und noch nicht zusammengeführt wurde, führen Sie die Änderungen lokal durch, während Sie auf demselben Branch bleiben. Sobald die Änderungen abgeschlossen sind, verwenden Sie den `Push origin`-Button, um einen neuen Commit zu Ihrem noch offenen PR hinzuzufügen;
- Falls Ihr PR bereits mit dem Hauptbranch zusammengeführt wurde, müssen Sie den Prozess von vorne beginnen, indem Sie einen neuen Branch erstellen und dann einen neuen PR einreichen. Stellen Sie sicher, dass Ihr lokales Repository mit dem Quell-Repository von PlanB Network synchronisiert ist, bevor Sie fortfahren.