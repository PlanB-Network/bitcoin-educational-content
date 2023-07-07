---
name: RaspiBlitz
description: Anleitung zur Einrichtung Ihres RaspiBlitz
---

![image](assets/0.jpeg)

# RaspiBlitz

Der RaspiBlitz ist ein Do-it-yourself-Lightning-Node (LND und/oder Core Lightning), der zusammen mit einem Bitcoin-Fullnode auf einem RaspberryPi (1TB SSD) und einem schönen Display läuft, um die Einrichtung und Überwachung zu erleichtern.

Der RaspiBlitz richtet sich hauptsächlich an Personen, die lernen möchten, wie man seinen eigenen dezentralen Node von zu Hause aus betreibt - denn: Nicht dein Node, nicht deine Regeln. Entdecken und entwickeln Sie das wachsende Ökosystem des Lightning-Netzwerks, indem Sie ein vollwertiger Teil davon werden. Bauen Sie ihn als Teil eines Workshops oder als Wochenendprojekt selbst auf.

![video](https://youtu.be/DTHlSPMz3ns)

RASPIBLITZ - Anleitung zum Betreiben eines Lightning- und Bitcoin-Fullnodes von BTC session

# Parman's Raspiblitz-Einrichtungsanleitung

> Die folgende Anleitung wurde von Parman (https://twitter.com/parman_the) zur Verfügung gestellt. Sie können ihm hier Trinkgeld geben: dandysack84@walletofsatoshi.com Originalquelle: https://armantheparman.com/raspiblitz/

Der Raspiblitz ist ein ausgezeichnetes System zum Betreiben eines Bitcoin-Nodes und zugehöriger Apps. Ich empfehle dies und den My Node Node den meisten Benutzern (idealerweise zwei Nodes für Redundanz). Ein großer Vorteil ist, dass der Raspiblitz-Node "Free Open Source Software" ist, im Gegensatz zu MyNode oder Umbrel. Warum ist das wichtig? Vlad Costa erklärt es. Sie können den RaspbiBlitz auch mit einer WLAN-Verbindung anstelle von Ethernet betreiben - hier finden Sie eine ergänzende Anleitung dazu. (Ich habe noch keine Möglichkeit gefunden, dies mit MyNode zu tun).

Sie können einen fertigen Node mit einem angeschlossenen Minibildschirm kaufen oder ihn selbst bauen (Sie benötigen keinen Bildschirm).

Die Anleitung auf der GitHub-Seite ist ausgezeichnet, aber möglicherweise zu detailliert für einen mäßig erfahrenen Benutzer. Meine Anweisungen werden knapper und hoffentlich einfacher zu befolgen sein.

Im Wesentlichen ist der Prozess sehr ähnlich wie der Prozess zum Einrichten eines MyNode-Nodes mit einem Raspberry Pi 4. Die Raspiblitz-Anleitung empfiehlt den Kauf eines Monitors, aber Sie benötigen wirklich keinen und ich würde es nicht empfehlen. Sie benötigen nicht einmal eine zusätzliche Tastatur oder Maus. Greifen Sie einfach über einen Computer im selben Heimnetzwerk auf das Terminalmenü des Geräts zu und verwenden Sie den SSH-Befehl über das Terminal. Dies ist mit Linux/Mac (einfach) und mit Windows etwas schwieriger möglich.

## Schritt 1: Kaufen Sie die Ausrüstung.

Sie benötigen genau die gleiche Ausrüstung wie für einen MyNode-Node. Sie können es mit einem der beiden versuchen, der einzige Unterschied besteht in den Daten auf der Micro-SD-Karte.

- Raspberry Pi 4, 4 GB oder 8 GB Arbeitsspeicher (4 GB reichen aus)
- Offizielles Raspberry Pi-Netzteil (sehr wichtig! Verwenden Sie kein generisches, ernsthaft)
- Ein Gehäuse für den Pi (FLIRC-Gehäuse ist großartig. Das gesamte Gehäuse ist ein Kühlkörper und Sie benötigen keinen Lüfter, der laut sein kann)
- 32-GB-Micro-SD-Karte (Sie benötigen eine, aber ein paar sind praktisch)
- Ein Speicherkartenleser (die meisten Computer haben keinen Steckplatz für eine Micro-SD-Karte).
- Externe SSD-Festplatte mit 1 TB.
- Ein Ethernet-Kabel (zur Verbindung mit Ihrem Heimrouter).

Sie benötigen keinen Monitor (oder Tastatur oder Maus).
Hinweis: Dies ist die falsche Festplatte: Dies ist eine tragbare externe Festplatte. Es ist kein SSD. SSD ist entscheidend. Deshalb ist es billig (Preis in AUD)

![image](assets/1.png)

Dies ist der richtige Typ:

![image](assets/2.png)

Dies ist schneller, aber unnötig teuer:

![image](assets/3.png)

## Schritt 2: Raspiblitz-Image herunterladen

Navigieren Sie zur Raspiblitz-Github-Website und suchen Sie den Link "Image herunterladen":

![image](assets/4.png)

Der SHA-256-Hash der heruntergeladenen Datei wird auf der Website bereitgestellt. Er ändert sich bei jedem Update. Wenn Sie nicht verstehen, worum es geht, sollten Sie dies tun, daher habe ich einen Leitfaden geschrieben, den Sie hier lesen können.

![image](assets/5.png)

## Schritt 3: Image überprüfen

Bevor Sie fortfahren, wenn Sie sich auf der Befehlszeile nicht im Dateisystem auskennen, ist es einfach zu erlernen und Sie sollten es tun.

Hier ist ein nützliches Video für Linux, das auch für Mac gilt.

Für Windows gibt es hier ein einfaches Tutorial.
Mac/Linux

Warten Sie, bis der Download der Datei abgeschlossen ist (wichtig!) und öffnen Sie dann das Terminal, navigieren Sie zum Speicherort der heruntergeladenen Datei und geben Sie den folgenden Befehl ein...

```
shasum -a 256 xxxxxxxxxxxxxx
```

wobei xxxxxxxxxxxxxx der Name der gerade heruntergeladenen Datei ist. Wenn Sie sich nicht im Verzeichnis befinden, in dem sich diese Datei befindet, müssen Sie den vollständigen Pfad eingeben.

Der Computer denkt etwa 20 Sekunden lang nach. Überprüfen Sie, ob die Ausgabedatei mit der zuvor von der Website heruntergeladenen übereinstimmt. Wenn sie identisch ist, können Sie fortfahren.
Windows

Öffnen Sie die Eingabeaufforderung und navigieren Sie zum Speicherort der heruntergeladenen Datei und geben Sie diesen Befehl ein:

```
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

wobei xxxxxxxxxxxxxx der Name der gerade heruntergeladenen Datei ist. Wenn Sie sich nicht im Verzeichnis befinden, in dem sich diese Datei befindet, müssen Sie den vollständigen Pfad eingeben.

Der Computer denkt etwa 20 Sekunden lang nach. Überprüfen Sie, ob die Ausgabedatei mit der zuvor von der Website heruntergeladenen übereinstimmt. Wenn sie identisch ist, können Sie fortfahren.

## Schritt 4: SD-Karte flashen

Sie können Balena Etcher verwenden, um dies zu tun. Laden Sie es hier herunter.

Etcher ist selbsterklärend zu verwenden. Legen Sie Ihre Micro-SD-Karte ein und flashen Sie die Raspiblitz-Software (.img-Datei) auf die SD-Karte.

![image](assets/6.png)

![image](assets/7.png)

![image](assets/8.png)

![image](assets/9.png)

Sobald der Vorgang abgeschlossen ist, ist das Laufwerk nicht mehr lesbar. Sie erhalten möglicherweise einen Fehler vom Betriebssystem und das Laufwerk sollte vom Desktop verschwinden. Ziehen Sie die Karte heraus.

## Schritt 5: Pi einrichten und SD-Karte einlegen

Die Teile (Gehäuse nicht gezeigt):

![image](assets/10.png)

![image](assets/11.png)

Schließen Sie das Ethernet-Kabel und den USB-Anschluss der Festplatte an (noch nicht die Stromversorgung). Vermeiden Sie eine Verbindung zu den blauen USB-Anschlüssen in der Mitte. Sie sind USB 3. Verwenden Sie den USB 2-Anschluss, auch wenn das Laufwerk möglicherweise USB 3-fähig ist (zuverlässiger).

![image](assets/12.png)

Die Micro-SD-Karte wird hier eingesetzt:

![image](assets/13.png)

Schließlich schließen Sie die Stromversorgung an:

![image](assets/14.png)

## Schritt 6: IP-Adresse des Pi finden

Du benötigst keinen Monitor für den Raspiblitz. Du benötigst jedoch einen anderen Computer im Heimnetzwerk. Wenn dein Pi nicht über Ethernet verbunden ist und du dich auf WLAN verlassen möchtest, erfordert das Finden der IP einige Computerkenntnisse. Kann dir leider nicht helfen. Du benötigst eine Ethernet-Verbindung. (Das Problem entsteht durch den Zugriff auf einen Monitor und das Betriebssystem, um WLAN zu verbinden und ein Passwort einzugeben.)
Überprüfe deinen Router, um eine Liste aller IPs aller verbundenen Geräte zu erhalten.

Ich habe 192.168.0.1 im Browser eingegeben (Anweisungen, die mit meinem Router kamen), mich angemeldet und konnte mein Gerät mit der IP 192.168.0.191 sehen. Beachte, dass diese IP-Adressen für das Internet nicht öffentlich sichtbar sind (sie gehen zuerst über den Router), sondern nur Identifikatoren für Geräte in deinem Heimnetzwerk sind.

Das Finden der IP ist entscheidend.

> UPDATE: Du kannst das Terminal auf einem Mac oder Linux-Computer verwenden, um die IP-Adresse aller über Ethernet verbundenen Geräte im Heimnetzwerk mit dem Befehl "arp -a" zu finden. Die Ausgabe ist nicht so schön wie das, was der Router anzeigen wird, aber alle Informationen, die du benötigst, sind vorhanden. Wenn nicht offensichtlich ist, welches der Pi ist, führe einen Versuch und Irrtum durch.

## Schritt 7: SSH in den Pi

Denke daran, die SD-Karte in den Pi einzulegen, bevor du ihn einschaltest. Warte ein paar Minuten und öffne dann auf einem anderen Linux/Mac das Terminal.

Für Mac/Linux gib im Terminal Folgendes ein:

```
ssh admin@IP-Adresse_deines_Pis
```

Für Windows musst du putty installieren, um dich über SSH mit dem Pi zu verbinden. Gib den gleichen Befehl wie oben ein.

Beim ersten Mal oder immer wenn du das Betriebssystem des Pi durch das Wechseln der SD-Karte änderst, erhältst du möglicherweise diesen Fehler...

![image](assets/15.png)

Die Lösung besteht darin, zum Speicherort der "known_hosts"-Datei zu navigieren (es wird dir in der Fehlermeldung angezeigt) und sie zu löschen. Der Befehl lautet "rm known_hosts".

Wiederhole dann den SSH-Befehl, um dich anzumelden. Folgendes wird passieren...

![image](assets/16.png)

Gib "yes" (vollständiges Wort) ein, um fortzufahren.

Wenn erfolgreich, wirst du nach einem Passwort gefragt. Dies ist nicht für deinen Computer, sondern für den Raspiblitz. Das generische Passwort lautet "raspiblitz" und du wirst es später ändern. Das Terminal-Fenster wird blau und du hast Menüoptionen wie die alten DOS-Menüs. Navigiere mit den Pfeiltasten oder der Maus.

![image](assets/17.png)

Folge den Anweisungen, lege deine Passwörter fest und dann wird deine Festplatte erkannt und du erhältst die Möglichkeit, sie bei Bedarf zu formatieren.

Dann wirst du gefragt, ob du die Blockchain-Daten von einer anderen Quelle kopieren oder sie erneut herunterladen möchtest. Das Kopieren ist ein Lernprozess und die Anweisungen sind ziemlich gut und gut aufzubewahren...

![image](assets/18.png)

Der einfache, aber langsamere Weg besteht darin, die gesamte Kette von Grund auf herunterzuladen...

![image](assets/19.png)

Viel Text wird über den Terminalbildschirm flackern. Du könntest es für den Prozess des Blockchain-Downloads halten, aber es sieht für mich so aus, als ob es einen privaten Schlüssel für die Kommunikation generiert.

Dann erscheinen Lightning-Optionen.

![image](assets/20.png)

Erstelle ein neues Passwort, um deine Lightning-Wallet zu sperren, dann wird eine neue Wallet erstellt und du erhältst 24 Wörter zum Aufschreiben...

![image](assets/21.png)
Stellen Sie sicher, dass Sie es aufschreiben und sicher aufbewahren. Ich habe von einer Person gehört, die es nicht getan hat, weil er nicht vorhatte, Lightning zu verwenden, aber dann ein Jahr später beschloss, es zu verwenden und Kanäle zu öffnen. Dann merkte er, dass seine Wörter nicht gesichert waren und ich erinnere mich, dass es nicht möglich war, die Wörter erneut vom Gerät abzurufen. Er musste alle seine Kanäle schließen und von vorne beginnen. Er ist damit davongekommen, aber andere könnten nicht so viel Glück haben.

Danach scrollt einige Minuten lang Text durch das Terminalfenster. Dann...

![image](assets/22.png)

Sie werden von der SSH-Sitzung abgemeldet. Melden Sie sich erneut an, diesmal mit Ihrem neuen Passwort, Passwort A. Sobald Sie angemeldet sind, werden Sie nach Passwort C gefragt, um Ihre Lightning-Wallet zu entsperren.

Jetzt warten wir. Wir sehen uns in 2 Wochen. Sie können das Terminal schließen, es hat keine Auswirkungen auf den Pi, es ist nur ein Kommunikationsfenster.

![image](assets/23.png)

Wenn Sie aus irgendeinem Grund den Pi herunterfahren möchten, bevor die Blockchain fertig heruntergeladen ist, ist das in Ordnung, solange Sie es ordnungsgemäß tun. Die Blockchain wird dort weiter heruntergeladen, wo sie aufgehört hat, sobald Sie sich erneut verbinden.

Drücken Sie STRG+C, um den blauen Bildschirm zu verlassen. Sie greifen auf das Linux-Terminal des Pi zu. Hier können Sie "menu" eingeben, um den folgenden Bildschirm zu laden, und von dort aus können Sie den Pi ausschalten.

![image](assets/24.png)

ENDE der Anleitung

> Die folgende Anleitung wurde von Parman (https://twitter.com/parman_the) zur Verfügung gestellt.
> Sie können ihm hier Trinkgeld geben: dandysack84@walletofsatoshi.com Originalquelle: https://armantheparman.com/raspiblitz/

Ab jetzt ist Ihr Knoten bereit. Wenn Sie weitere Optionen erkunden möchten, schauen Sie im GitHub nach weiteren Tutorials und Anleitungen: https://github.com/raspiblitz/raspiblitz#feature-documentation
