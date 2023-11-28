---
name: My Node
description: Richten Sie Ihre Bitcoin-MyNode ein
---

![Bild](assets/0.jpeg)

https://mynodebtc.com/

Der einfachste und leistungsstärkste Weg, um eine Bitcoin- und Lightning-Node auszuführen! Wir kombinieren die besten Open-Source-Software mit unserer Benutzeroberfläche, Verwaltung und Unterstützung, damit Sie Bitcoin und Lightning einfach, privat und sicher nutzen können.

## Arten von Node-Setups

Es gibt verschiedene Node-Setups. MyNode ist ausgezeichnet. Es gibt viele Apps, die damit geliefert werden, und noch mehr, wenn Sie für die Premium-Version bezahlen. Es ist ansonsten sehr mühsam, all diese Apps selbst herunterzuladen. Mit MyNode ist es jedoch ziemlich einfach, wie Sie sehen werden.

Eine alternative und ähnliche Option ist RaspiBlitz. Die Benutzeroberfläche ist nicht so schön und die Apps überschneiden sich weitgehend mit den Apps, die mit MyNode geliefert werden, aber Raspiblitz ist kostenlose Open-Source-Software (FOSS) und MyNode ist es nicht ganz. Ein weiterer Unterschied besteht darin, dass MyNode in einem Docker-Container ausgeführt wird. Ich finde Docker einschüchternd und schwer zu beheben. Dies ist nur ein Problem, wenn Sie auf Fehler oder Fehler stoßen. Der Entwickler bietet Hilfe für Premium-Benutzer an und es gibt auch eine Telegramm-Chatgruppe.

Der RaspiBlitz besteht nur aus mehreren Programmen, die auf Linux installiert sind, ohne Docker. Die externe Festplatte kann problemlos an einen anderen Linux-Computer mit Bitcoin Core angeschlossen werden, und schon kann es losgehen, wenn Sie es benötigen.

Eine weitere Option besteht darin, Bitcoin Core und eine Variante des Electrum-Servers (es gibt mehrere) auf einem Betriebssystem zu installieren. Ich habe Anleitungen für Linux (Raspberry Pi), Mac und Windows.

## Einkaufsliste

- Raspberry Pi 4, 4 GB Speicher oder 8 GB (4 GB reichen aus)

- Offizielles Raspberry Pi-Netzteil (sehr wichtig! Kein generisches verwenden, ernsthaft)

- Ein Gehäuse für den Pi. Das FLIRC-Gehäuse ist fantastisch. Das gesamte Gehäuse ist ein Kühlkörper und Sie benötigen keinen Lüfter, der laut sein kann.

- 16 GB microSD-Karte (Sie benötigen eine, aber ein paar sind praktisch)

- Ein Speicherkartenleser (die meisten Computer haben keinen Steckplatz für eine microSD-Karte).

- Externe SSD-Festplatte mit 1 TB.  
  Hinweis: SSD ist entscheidend. Verwenden Sie keine tragbare externe Festplatte, auch wenn sie günstiger ist.

- Ein Ethernet-Kabel (zur Verbindung mit Ihrem Heimrouter)

- Sie benötigen keinen Monitor

## MyNode-Image herunterladen

Navigieren Sie zum MyNode-Website-Link

![Bild](assets/1.jpeg)

Klicken Sie auf <Jetzt herunterladen>

Laden Sie die Version für Raspberry Pi 4 herunter:

![Bild](assets/2.jpeg)

Es ist eine große Datei:

![Bild](assets/3.jpeg)

Laden Sie die SHA 256-Hashes herunter

![Bild](assets/4.jpeg)

Öffnen Sie das Terminal auf Mac oder Linux oder die Eingabeaufforderung für Windows. Geben Sie ein:

```
Mac/Linux: "shasum -a 256 HERUNTERGELADENERDATEINAME"
Windows: "certUtil -hashfile HERUNTERGELADENERDATEINAME SHA256"
```

Der Computer denkt etwa 20 Sekunden lang nach. Überprüfen Sie dann, ob die Ausgabedatei mit dem zuvor von der Website heruntergeladenen Hash übereinstimmt. Wenn es identisch ist, können Sie fortfahren.
Flashen Sie die SD-Karte

## Balena Etcher herunterladen und installieren. Link

Ich konnte die digitale Signatur dafür nicht finden. Wenn Sie wissen, wie es geht, lassen Sie es mich bitte wissen und ich werde diesen Artikel aktualisieren.
Etcher ist selbsterklärend in der Verwendung. Legen Sie Ihre Micro-SD-Karte ein und flashen Sie die Raspberry Pi-Software (.img-Datei) auf die SD-Karte.

![image](assets/5.jpeg)
![image](assets/6.jpeg)
![image](assets/7.jpeg)
![image](assets/8.jpeg)
![image](assets/9.jpeg)
![image](assets/10.jpeg)
![image](assets/11.jpeg)

Sobald dies erledigt ist, ist das Laufwerk nicht mehr lesbar. Sie erhalten möglicherweise einen Fehler vom Betriebssystem und das Laufwerk sollte vom Desktop verschwinden. Ziehen Sie die Karte heraus.

## Richten Sie den Pi ein und legen Sie die SD-Karte ein

Die Teile (Gehäuse nicht gezeigt):

![image](assets/12.jpeg)
![image](assets/13.jpeg)

Schließen Sie das Ethernet-Kabel und den USB-Anschluss der Festplatte an (noch nicht die Stromversorgung). Vermeiden Sie eine Verbindung zu den blau markierten USB-Anschlüssen in der Mitte. Es handelt sich um USB 3. MyNode empfiehlt die Verwendung des USB 2-Anschlusses, obwohl das Laufwerk möglicherweise USB 3-fähig ist.

![image](assets/14.jpeg)

Die Micro-SD-Karte wird hier eingesetzt:

![image](assets/15.jpeg)

Schließlich schließen Sie die Stromversorgung an:

![image](assets/16.jpeg)

## Finden Sie die IP-Adresse des Pi

Sie benötigen nie einen Monitor mit dem MyNode. Sie benötigen jedoch einen anderen Computer im Heimnetzwerk. Wenn Ihr Pi nicht über Ethernet verbunden ist und Sie auf WLAN angewiesen sind, erfordert das Auffinden der IP-Adresse fortgeschrittene Computerkenntnisse. Ich kann Ihnen leider nicht helfen. Sie benötigen eine Ethernet-Verbindung. (Das Problem ergibt sich daraus, dass Sie Zugriff auf einen Monitor und das Betriebssystem benötigen, um eine Verbindung zum WLAN herzustellen und ein Passwort einzugeben).

Überprüfen Sie Ihren Router, um eine Liste aller IPs aller verbundenen Geräte zu erhalten.

Ich habe 192.168.0.1 im Browser eingegeben (Anweisungen, die mit meinem Router geliefert wurden), mich angemeldet und konnte ein Gerät "MyNode" mit der IP 192.168.0.18 sehen. Beachten Sie, dass diese IP-Adressen für das Internet nicht öffentlich sichtbar sind (sie gehen zuerst über den Router), sondern nur Identifikatoren für Geräte in Ihrem Heimnetzwerk sind.

Das Auffinden der IP-Adresse ist entscheidend.

> UPDATE: Sie können das Terminal auf einem Mac- oder Linux-Computer verwenden, um die IP-Adresse aller über Ethernet verbundenen Geräte im Heimnetzwerk mit dem Befehl "arp -a" zu finden. Die Ausgabe ist nicht so schön wie das, was der Router anzeigen wird, aber alle Informationen, die Sie benötigen, sind vorhanden. Wenn nicht offensichtlich ist, welches das Pi ist, führen Sie eine Probefahrt durch.

## SSH in den Pi

Sie haben die Möglichkeit, sich über den SSH-Befehl remote auf das Gerät einzuloggen, aber es ist nicht erforderlich (es ist erforderlich, wenn es sich um ein RaspiBlitz Node handelt). Ich zeige Ihnen trotzdem, wie es geht, da es sehr praktisch ist.

Öffnen Sie einen Mac- oder Linux-Computer (für Windows laden Sie putty, ein SSH-Tool, herunter) und geben Sie Folgendes ein:

```
ssh admin@192.168.0.18
```

Verwenden Sie Ihre eigene IP-Adresse. Der Benutzername für das MyNode-Gerät ist standardmäßig "admin". Das Passwort ist standardmäßig "bolt".

Wenn Sie Ihren Pi zuvor verwendet und die Micro-SD-Karte ausgetauscht haben, erhalten Sie diesen Fehler:

![image](assets/17.jpeg)

Was Sie tun müssen, ist zu dem Ort zu navigieren, an dem sich die Datei "known_hosts" befindet, und sie zu löschen. Es ist sicher. Die Fehlermeldung zeigt Ihnen den Pfad. Für mich war es /Benutzer/MeinBenutzername/.ssh/'
Vergiss nicht den "." vor ssh, das zeigt an, dass es sich um ein verstecktes Verzeichnis handelt.
Versuche dann den ssh-Befehl erneut.

Diesmal siehst du folgende Ausgabe:

![image](assets/18.jpeg)

Die gelöschte Datei wurde gelöscht und du fügst einen neuen Fingerabdruck hinzu. Gib "yes" ein und drücke die Eingabetaste.

Du wirst aufgefordert, das Passwort einzugeben. Es lautet "bolt".

Du hast jetzt Terminalzugriff auf den MyNode Pi, ohne einen Monitor, und kannst bestätigen, dass alles reibungslos geladen wurde.

![image](assets/19.jpeg)

## Zugriff über den Webbrowser

Öffne einen Browser. Es muss sich um einen Computer in deinem Heimnetzwerk handeln, von außerhalb kannst du dies nicht tun. Es gibt einen Weg, aber er ist schwierig. Ich habe es nicht getestet.

Gib die IP-Adresse in die Adressleiste des Browsers ein. Folgendes wird passieren:

![image](assets/20.jpeg)

Gib das Passwort "bolt" ein - ändere es später.

Dann wird Folgendes passieren:

![image](assets/21.jpeg)

Wähle "Format Drive"

![image](assets/22.jpeg)

Jetzt warten wir.

Irgendwann wirst du gefragt, ob du deinen Produktkey eingeben möchtest oder die kostenlose "Community Edition" verwenden möchtest - ich werde die Premium Edition zeigen. Ich empfehle, für die Premium-Version zu bezahlen, wenn du es dir leisten kannst, es lohnt sich sehr.

![image](assets/23.jpeg)

Du siehst dann den Fortschritt des heruntergeladenen Blocks. Es dauert Tage:

![image](assets/24.jpeg)

Es ist sicher, die Maschine während des Downloads auszuschalten, wenn du es musst. Gehe zu den Einstellungen und finde den Button zum Ausschalten der Maschine. Ziehe nicht einfach das Kabel heraus, du könntest die Installation oder die Festplatte beschädigen.

Stelle sicher, dass du frühzeitig zu "Einstellungen" gehst und QuickSync deaktivierst. Es wird den anfänglichen Blockdownload von vorne beginnen.

![image](assets/25.jpeg)

Ich wollte mit der Erstellung des Leitfadens fortfahren, also hier ist ein weiterer MyNode, den ich zuvor vorbereitet habe. So sieht die Seite aus, wenn die Blockchain synchronisiert ist und mehrere "Apps" aktiviert und synchronisiert wurden:

![image](assets/26.jpeg)

Beachte, dass auch der Electrum Server synchronisiert werden muss. Sobald die Bitcoin-Blockchain synchronisiert ist, klicke auf den Button, um den Vorgang zu starten - es dauert einen oder zwei Tage. Alles andere wird innerhalb weniger Minuten aktiviert, sobald du es auswählst. Du kannst Dinge anklicken und erkunden. Du wirst nichts kaputt machen. Wenn etwas kaputt geht (das ist mir passiert, aber ich denke, weil ich billige Teile hatte), musst du erneut flashen und den Download erneut starten. Das Problem, das ich mit MyNode habe, ist, dass wenn du "re-flashen" musst, du die Blockchain-Synchronisierung wieder von vorne beginnen musst. Es gibt technische Möglichkeiten, dies zu umgehen, aber es ist nicht einfach.

Wenn du auch einen anderen Knoten ausprobieren möchtest, zum Beispiel einen RaspiBlitz, benötigst du eine zusätzliche SSD-externe Festplatte und eine weitere microSD-Karte zum Flashen. Ansonsten ist es die gleiche Ausrüstung, du kannst MyNode und RaspiBlitz natürlich nicht gleichzeitig ausführen. Wenn du das tun möchtest, ist es Zeit, nach einem weiteren Raspberry Pi zu suchen.

Jetzt, da du einen laufenden Knoten hast, benutze ihn, lass ihn nicht einfach untätig herumstehen. Folge meinem Artikel (und Video), wie du deine Electrum Desktop Wallet mit dem Electrum Server und Bitcoin Core verbindest.
