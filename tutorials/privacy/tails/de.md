---
name: Tails

description: Tails auf einem USB-Stick installieren
---

_**Von Hari Seldon im Rahmen von Agora256 angebotener Leitfaden**_

![image](assets/cover.jpeg)

Ein tragbares und amnesisches Betriebssystem, das Sie vor Überwachung und Zensur schützt.

## Warum sollte man einen USB-Stick mit installiertem Tails haben?

Tails (https://tails.boum.org/) ist der einfachste Weg, um jederzeit einen sicheren Computer zur Verfügung zu haben, der auf dem Computer, den Sie verwenden, keine Spuren hinterlässt.

Um Tails zu verwenden, schalten Sie den Computer aus, den Sie zur Verfügung haben (bei Ihren Eltern, bei Ihren Freunden, in einem Internetcafé...) und starten Sie ihn mit Ihrem Tails-USB-Stick anstelle von Windows, macOS oder Linux.

Danach haben Sie einen Arbeits- und Kommunikationsraum, der unabhängig vom gewöhnlichen Betriebssystem ist und niemals die Festplatte verwendet.

Tails schreibt niemals auf die Festplatte und verwendet nur den Arbeitsspeicher des Computers, um zu funktionieren. Dieser Speicher wird beim Ausschalten von Tails vollständig gelöscht und entfernt somit alle möglichen Spuren.

## Einige konkrete Anwendungsfälle

Um Ihnen konkrete Ideen für den Nutzen eines USB-Sticks mit Tails immer bei sich zu geben, hier eine kleine, nicht erschöpfende Liste, die vom Agora256-Team zusammengestellt wurde:

- Sich mit dem Internet und Tor verbinden, um Websites ohne Spuren zu besuchen;
- Ein PDF von einer verdächtigen Website öffnen;
- Ihre Bitcoin-Private-Key-Backup mit der Electrum-Wallet testen;
- Eine Bürosoftware (LibreOffice) verwenden und an einem Computer arbeiten, der Ihnen nicht gehört;
- Die ersten Schritte in einer Linux-Umgebung machen, um die Welt von Microsoft und Apple zu verlassen.

## Wie kann man Tails vertrauen?

Bei der Verwendung von Software gibt es immer ein gewisses Maß an Vertrauen, aber dieses muss nicht blind sein. Ein Werkzeug wie Tails sollte versuchen, seinen Benutzern Mittel zur Verfügung zu stellen, um vertrauenswürdig zu sein. Für Tails bedeutet das:

- Öffentlicher Quellcode: https://gitlab.tails.boum.org/;
- Ein Projekt, das auf renommierten Projekten basiert: Tor und Debian;
- Überprüfbare und reproduzierbare Downloads;
- Empfehlungen von verschiedenen Personen und Organisationen.

## Installations- und Verwendungshandbuch

Dieses Installationshandbuch soll Sie durch jeden Schritt der Installation führen. Wir werden nicht mehr als der offizielle Leitfaden die auszuführenden Aktionen beschreiben, sondern wir werden Sie in die richtige Richtung lenken und Ihnen Tipps und Tricks geben.

Aus praktischen Gründen werden diese Ratschläge auf die macOS- und Linux-Plattformen ausgerichtet sein.
🛠️
Bevor Sie mit diesem Verfahren beginnen, stellen Sie bitte sicher, dass Sie einen USB-Stick mit einer Lesegeschwindigkeit von mindestens 150 MB/s und einer Größe von mindestens 8 GB besitzen, idealerweise vom Typ USB 3.0.

Voraussetzungen:

- 1 USB-Stick, nur für Tails, mit mindestens 8 GB
- Ein mit dem Internet verbundener Computer mit Linux, macOS (oder Windows)
- Insgesamt etwa eine Stunde Zeit, abhängig von der Geschwindigkeit Ihrer Internetverbindung, davon eine halbe Stunde für die Installation (1,3 GB Download-Datei)

## Schritt 1: Tails von Ihrem Computer herunterladen

![image](assets/1.jpeg)

> 🔗 Offizieller Tails-Abschnitt: https://tails.boum.org/install/linux/index.fr.html#download

Das Herunterladen der Installationsdatei mit der .img-Erweiterung kann je nach Internet-Downloadgeschwindigkeit einige Zeit in Anspruch nehmen. Planen Sie also genügend Zeit ein. Mit einer modernen und leistungsstarken Leitung dauert es weniger als 5 Minuten.

Speichern Sie die Datei in einem bekannten Ordner wie "Downloads", da dies für den nächsten Schritt erforderlich ist.

## Schritt 2: Überprüfen Sie Ihren Download

![image](assets/2.jpeg)

> 🔗 Offizieller Tails-Abschnitt: https://tails.boum.org/install/linux/index.fr.html#verify

Die Überprüfung des Downloads stellt sicher, dass er von den Tails-Entwicklern stammt und nicht während des Downloads beschädigt oder abgefangen wurde.

Es ist möglich, manuell zu überprüfen, ob die gerade heruntergeladene Datei die erwartete ist, indem Sie PGP verwenden. Ohne fortgeschrittene Kenntnisse bietet diese Überprüfung jedoch das gleiche Sicherheitsniveau wie die JavaScript-Überprüfung auf der Download-Seite, ist jedoch viel komplizierter und fehleranfällig.

Verwenden Sie daher die Schaltfläche "Ihren Download auswählen ..." im offiziellen Abschnitt, um die Datei zu überprüfen!

## Schritt 3: Tails auf Ihrem USB-Stick installieren

![image](assets/3.jpeg)

> 🔗 Offizieller Tails-Abschnitt:
>
> - Linux: https://tails.boum.org/install/linux/index.fr.html#install
> - macOS: https://tails.boum.org/install/mac/index.fr.html#etcher und https://tails.boum.org/install/mac/index.fr.html#install

Dieser Schritt, Tails auf Ihrem USB-Stick zu installieren, ist der schwierigste im gesamten Leitfaden, insbesondere wenn Sie dies noch nie zuvor gemacht haben. Der wichtigste Punkt ist, das Verfahren im offiziellen Abschnitt für Ihr Betriebssystem (Linux oder macOS) sorgfältig auszuwählen.

Sobald die empfohlenen Tools installiert und vorbereitet sind, kann die Datei mit der .img-Erweiterung auf Ihren Stick kopiert werden (alle vorhandenen Daten werden dabei gelöscht), um ihn unabhängig "bootfähig" zu machen.

Viel Erfolg! Und weiter zu Schritt 4.

## Schritt 4: Starten Sie Tails von Ihrem USB-Stick neu

![image](assets/4.jpeg)

> 🔗 Offizieller Abschnitt von Tails: https://tails.boum.org/install/linux/index.fr.html#restart
> Es ist Zeit, einen Ihrer Computer mit Ihrem neuen USB-Stick zu starten. Stecken Sie diesen in einen der USB-Anschlüsse und starten Sie neu!

> 💡 Die meisten Computer starten nicht automatisch von einem Tails-USB-Stick, aber Sie können die Startmenütaste drücken, um eine Liste möglicher Geräte anzuzeigen, von denen aus gestartet werden kann.

Um herauszufinden, welche Taste Sie drücken müssen, um das Startmenü anzuzeigen und den USB-Stick anstelle Ihrer üblichen Festplatte auszuwählen, finden Sie hier eine nicht erschöpfende Liste nach Hersteller:

| Hersteller | Taste            |
| ---------- | ---------------- |
| Acer       | F12, F9, F2, Esc |
| Apple      | Option           |
| Asus       | Esc              |
| Clevo      | F7               |
| Dell       | F12              |
| Fujitsu    | F12, Esc         |
| HP         | F9               |
| Huawei     | F12              |
| Intel      | F10              |
| Lenovo     | F12              |
| MSI        | F11              |
| Samsung    | Esc, F12, F2     |
| Sony       | F11, Esc, F10    |
| Toshiba    | F12              |
| andere...  | F12, Esc         |

Nachdem der USB-Stick ausgewählt wurde, sollten Sie diesen neuen Startbildschirm sehen. Das ist ein gutes Zeichen, lassen Sie den Computer also weiter hochfahren...

![image](assets/5.jpeg)

## Schritt 5: Willkommen bei Tails!

![image](assets/6.jpeg)

> 🔗 Offizieller Abschnitt von Tails: https://tails.boum.org/install/linux/index.fr.html#tails

Eine oder zwei Minuten nach dem Bootloader und dem Ladescreen erscheint der Willkommensbildschirm.

![image](assets/7.jpeg)

Wählen Sie auf dem Willkommensbildschirm Ihre Sprache und Tastaturbelegung in der Sektion Sprache & Region aus. Klicken Sie auf Tails starten.

![image](assets/8.jpeg)

Wenn Ihr Computer nicht über ein Kabel mit Ihrem Netzwerk verbunden ist, lesen Sie bitte die offiziellen Tails-Anweisungen, um Ihnen bei der Verbindung mit einem kabellosen Netzwerk zu helfen (Abschnitt "Testen Sie Ihr WLAN").

Sobald Sie mit dem lokalen Netzwerk verbunden sind, erscheint der Tor-Verbindungsassistent, um Ihnen bei der Verbindung zum Tor-Netzwerk zu helfen.

![image](assets/9.jpeg)

Sie können nun anonym surfen, die Optionen und die in Tails enthaltene Software erkunden. Viel Spaß dabei, Sie haben hier genügend Spielraum für Fehler, da nichts auf dem USB-Stick geändert wird... Bei Ihrem nächsten Neustart werden alle Ihre Erfahrungen vergessen sein!

## In einem zukünftigen Leitfaden...

Sobald Sie etwas mehr mit Ihrem eigenen Tails-USB-Stick experimentiert haben, werden wir in einem anderen Artikel weitere fortgeschrittene Themen erkunden, wie:

> Aktualisieren Sie einen Schlüssel mit der neuesten Version von Tails; Konfigurieren und verwenden Sie den persistenten Speicher; Installieren Sie zusätzliche Software.
> Bis dahin, wie immer, wenn Sie Fragen haben, zögern Sie nicht, sie mit der Agora256-Community zu teilen. Gemeinsam lernen wir, um morgen besser zu sein als wir es heute sind!

> _**Von Hari Seldon im Rahmen von Agora256 vorgeschlagener Leitfaden; ursprünglicher Beitrag: https://agora256.com/installer-tails-usb/**_
