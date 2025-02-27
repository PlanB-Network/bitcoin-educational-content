---
name: GitHub Account
description: Wie erstellt man sein eigenes Konto auf GitHub?
---

![cover](assets/cover.webp)

Die Mission von PlanB ist es, erstklassige Bildungsressourcen über Bitcoin bereitzustellen, die in so vielen Sprachen wie möglich verfügbar sind. Alle auf der Website veröffentlichten Inhalte sind Open-Source und werden auf GitHub gehostet, was jedem die Möglichkeit bietet, zur Bereicherung der Plattform beizutragen. Beiträge können verschiedene Formen annehmen: Korrekturlesen und Korrigieren bestehender Texte, Übersetzen in andere Sprachen, Aktualisieren von Informationen oder Erstellen neuer Tutorials, die auf unserer Website noch nicht verfügbar sind.

Wenn Sie zum PlanB-Netzwerk beitragen möchten, müssen Sie Git und GitHub verwenden. Wenn diese Tools für Sie neu sind oder ihre Funktionsweise undurchsichtig erscheint, keine Panik, dieser Artikel ist für Sie! Wir werden gemeinsam die Grundlagen von Git und GitHub sowie die zugehörige technische Terminologie durchgehen, um Ihnen die effektive Nutzung dieser Tools im Anschluss zu ermöglichen.

## Was ist Git?

Git ist ein Versionskontrollsystem, das speziell für die Verwaltung von Softwareprojekten entwickelt wurde. Erstellt im Jahr 2005 von Linus Torvalds, ist Git schnell zum Standard in der Softwareentwicklungsbranche für Versionskontrolle geworden. Aber was bedeutet das genau?
![git](assets/11.webp)
Im Kern ermöglicht Git Entwicklern, Änderungen am Quellcode eines Projekts im Laufe der Zeit nachzuverfolgen. Das bedeutet, dass mit jeder Änderung am Code Git eine neue Version des Projekts aufzeichnet. Tritt ein Fehler auf oder funktioniert ein experimentelles Feature nicht wie erwartet, ist es möglich, zu einem früheren Zustand des Codes zurückzukehren, wie eine Art Zeitmaschine für Dateien.

Eine der Schlüsselfunktionen von Git ist die Verwaltung von Zweigen. Ein Zweig ist eine Art parallele Linie, auf der Entwickler unabhängig vom Rest des Projekts arbeiten können. Dies erleichtert die Hinzufügung neuer Funktionen oder die Korrektur von Fehlern, ohne den Hauptcode zu stören. Sobald die Änderungen getestet und validiert sind, können sie mit dem Hauptzweig zusammengeführt werden.

Eine Besonderheit von Git ist seine Fähigkeit, auf verteilte Weise zu operieren. Jeder Entwickler hat eine vollständige Kopie des Projekts auf der eigenen Festplatte, was es ihm ermöglicht, offline zu arbeiten und Änderungen später zu integrieren, wenn eine Internetverbindung verfügbar ist. Dies reduziert das Risiko von Konflikten und ermöglicht es mehreren Entwicklern, gleichzeitig am selben Projekt zu arbeiten, ohne sich gegenseitig in die Quere zu kommen.
Ursprünglich wurde Git hauptsächlich für Softwareentwicklungsprojekte konzipiert. Es kann jedoch auch verwendet werden, um Schreibprojekte zu verwalten. Statt an Code, arbeiten wir an Text. Und genau diese Methode hat das PlanB-Netzwerk übernommen, um seinen Inhalt zu verwalten! Git erleichtert die Zusammenarbeit an Kursen und Tutorials, da es eine präzise Nachverfolgung von Änderungen, eine effiziente Versionsverwaltung ermöglicht und auch die Überprüfung und Verbesserung von Inhalten durch andere Mitwirkende ermöglicht.
## Was ist GitHub?

GitHub ist eine Plattform für die Verwaltung und das Hosting von Quellcode, basierend auf dem Versionskontrollsystem Git, das wir gerade besprochen haben. Gestartet im Jahr 2008, hat GitHub schnell an Beliebtheit gewonnen und ist zu einer unverzichtbaren Referenz für Entwickler weltweit geworden. Aber worin unterscheidet sich GitHub von Git, und warum ist es so entscheidend für unsere Methode der Inhaltsproduktion?
![github](assets/12.webp)
Zunächst ist es wichtig zu verstehen, dass GitHub auf Git aufbaut (wie im vorherigen Abschnitt besprochen). Während Git das Tool ist, das Codeänderungen nachverfolgt, ist GitHub der Online-Dienst, der diesen Code hostet, teilt und verwaltet.

Stellen Sie sich Git als eine Art Logbuch vor, das jeder Entwickler auf seinem eigenen Computer verwendet, um alle Änderungen in seinem Projekt aufzuzeichnen. GitHub hingegen ist wie eine öffentliche Bibliothek, in der all diese Logbücher geteilt, verglichen und kombiniert werden können.
Der grundlegende Unterschied zwischen Git und GitHub liegt in ihrer Funktion: Git ist das Tool, das lokal von jedem Entwickler verwendet wird, um ihre Codeversionen zu verwalten, während GitHub die Online-Plattform ist, die diese Versionen hostet und die Zusammenarbeit erleichtert.
GitHub ist viel mehr als nur ein Dienst zum Hosten von Code. Es ist eine Kollaborationsplattform, die es Entwicklern ermöglicht, effizient zusammenzuarbeiten. Und tatsächlich nutzt das PlanB Network diese Plattform, um nicht nur den gesamten Code, der die Website antreibt, zu hosten, sondern auch, und das ist für uns von Interesse, alle Inhalte (Tutorials, Schulungen, Ressourcen...).

## Einige technische Begriffe

Bei der Verwendung von Git und GitHub werden Sie auf Befehle und Funktionen stoßen, deren Namen komplex erscheinen mögen. In diesem letzten Teil gebe ich einfache Definitionen, um die technischen Begriffe zu verstehen, denen Sie bei der Verwendung von Git und GitHub begegnen könnten:

- **Fetch origin:** Befehl, der aktuelle Informationen und Änderungen aus einem entfernten Repository abruft, ohne sie mit Ihrer lokalen Arbeit zusammenzuführen. Es aktualisiert Ihr lokales Repository mit neuen Branches und Commits, die im entfernten Repository vorhanden sind.

- **Pull origin:** Befehl, der Updates aus einem entfernten Repository abruft und sofort in Ihren lokalen Branch integriert, um diesen zu synchronisieren. Dies kombiniert die Schritte von Fetch und Merge in einem einzigen Befehl.
- **Sync Fork:** Eine Funktion auf GitHub, die es Ihnen ermöglicht, Ihren Fork eines Projekts mit den neuesten Änderungen aus dem Quellrepository zu aktualisieren. Dies stellt sicher, dass Ihre Kopie des Projekts auf dem neuesten Stand mit der Hauptentwicklung bleibt.
- **Push origin:** Befehl, der verwendet wird, um Ihre lokalen Änderungen an ein entferntes Repository zu senden.

- **Pull Request:** Eine Anfrage, die von einem Beitragenden gesendet wird, um anzugeben, dass sie Änderungen an einem Branch in einem entfernten Repository vorgenommen haben und wünschen, dass diese Änderungen überprüft und möglicherweise in den Hauptbranch des Repositories integriert werden.

- **Commit:** Speichern Ihrer Änderungen. Ein Commit ist wie ein sofortiger Schnappschuss Ihrer Arbeit zu einem bestimmten Zeitpunkt, der es ermöglicht, eine Historie von Änderungen zu behalten. Jeder Commit enthält eine beschreibende Nachricht, die erklärt, was geändert wurde.

- **Branch:** Eine parallele Version des Repositories, die es Ihnen ermöglicht, an Änderungen zu arbeiten, ohne den Hauptbranch (oft "main" oder "master" genannt) zu beeinflussen. Branches erleichtern die Entwicklung neuer Funktionen und die Korrektur von Fehlern, ohne das Risiko, stabilen Code zu stören.

- **Merge:** Zusammenführen besteht darin, die Änderungen von einem Branch in einen anderen zu integrieren. Es wird beispielsweise verwendet, um die Änderungen von einem Arbeitsbranch auf den Hauptbranch zu übertragen, was die verschiedenen Beiträge hinzufügt.

- **Fork:** Ein Repository zu forken bedeutet, eine Kopie dieses Repositories auf Ihrem eigenen GitHub-Konto zu erstellen, was es Ihnen ermöglicht, am Projekt zu arbeiten, ohne das ursprüngliche Repository zu beeinflussen. Der Fork kann entweder seinen eigenen Weg gehen und zu einem anderen Projekt als das Original werden, oder er kann sich regelmäßig mit dem Originalprojekt synchronisieren, um dazu beizutragen.

- **Clone:** Ein Repository zu klonen bedeutet, eine lokale Kopie auf Ihrem Computer zu erstellen, was Ihnen Zugang zu allen Dateien und der Historie gibt. Dies ermöglicht es Ihnen, direkt lokal am Projekt zu arbeiten.

- **Repository:** Speicherplatz für ein Projekt auf GitHub. Ein Repository enthält alle Projektdateien sowie die Historie aller Änderungen, die daran vorgenommen wurden. Es ist die Grundlage der Speicherung und Zusammenarbeit auf GitHub.

- **Issue:** Ein Werkzeug zur Verfolgung von Aufgaben und Fehlern auf GitHub. Issues ermöglichen es, Probleme zu melden, Verbesserungen vorzuschlagen oder über neue Funktionen zu diskutieren. Jedes Issue kann zugewiesen, beschriftet und kommentiert werden.

Diese Liste ist natürlich nicht erschöpfend. Es gibt viele andere technische Begriffe, die spezifisch für Git und GitHub sind. Die hier erwähnten sind jedoch die Hauptbegriffe, auf die Sie häufig stoßen werden.

## Wie man ein GitHub-Konto erstellt

Wenn Sie zum PlanB-Netzwerk beitragen möchten, benötigen Sie ein GitHub-Konto. In diesem Tutorial führen wir Sie Schritt für Schritt durch den Prozess, wie Sie Ihr eigenes Konto erstellen, einrichten und ordnungsgemäß absichern können.

- Gehen Sie zu [https://github.com/signup](https://github.com/signup).
- Geben Sie Ihre E-Mail-Adresse ein, dann klicken Sie auf den grünen `Continue`-Button:
![github](assets/1.webp)
- Wählen Sie ein starkes Passwort, dann klicken Sie auf den grünen `Continue`-Button:
![github](assets/2.webp)
- Wählen Sie als Nächstes Ihren Benutzernamen. Sie können Ihre echte Identität offenbaren oder ein Pseudonym verwenden. Dann klicken Sie auf den grünen `Continue`-Button:
![github](assets/3.webp)
- Vervollständigen Sie das Captcha:
![github](assets/4.webp)
- Eine E-Mail mit einem Bestätigungscode wird Ihnen zugesandt; Sie müssen diesen eingeben, um die Erstellung Ihres Kontos abzuschließen:
![github](assets/5.webp)
- Beantworten Sie die Fragen, wenn Sie möchten, dass GitHub Sie zu bestimmten Tools führt, oder klicken Sie auf `skip personalization`, um dies zu überspringen:
![github](assets/6.webp)
- Wählen Sie den kostenlosen Tarif, indem Sie auf den `Continue for free`-Button klicken:
![github](assets/7.webp)
- Sie werden dann zu Ihrem Dashboard weitergeleitet.
- Wenn Sie möchten, können Sie Ihr Konto anpassen, indem Sie auf Ihr Profilbild oben rechts auf dem Bildschirm klicken und dann das Menü `Settings` aufrufen:
![github](assets/8.webp)
- In diesem Abschnitt haben Sie die Möglichkeit, ein neues Profilbild hinzuzufügen, einen Namen auszuwählen, Ihre Biografie anzupassen oder einen Link zu Ihrer persönlichen Website hinzuzufügen:
![github](assets/9.webp)
- Ich empfehle auch, das Menü `Password and authentication` zu besuchen, um mindestens eine Zwei-Faktor-Authentifizierung einzurichten:
![github](assets/10.webp)
