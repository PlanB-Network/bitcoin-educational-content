name: Nerdminer

## description: Beginnen Sie mit dem Bitcoin-Mining mit einer Gewinnchance nahe 0.

![cover](assets/cover.jpeg)

> Konfiguration Ihres NerdMiner_v2

In diesem Tutorial werden wir Sie durch die notwendigen Schritte führen, um einen NerdMiner_v2 einzurichten, der eine spezielle Hardware (einen ESP-32 S3) für das Bitcoin-Mining ist.
Natürlich kann die Rechenleistung eines solchen Geräts nicht mit den ASICs von Amateur- oder professionellen Minern konkurrieren. Dennoch ist der NerdMiner ein perfektes pädagogisches Werkzeug, um das Bitcoin-Mining greifbar zu machen. Und wer weiß, mit (sehr viel) Glück finden Sie vielleicht einen Block und die dazugehörige Belohnung. Für Neugierige werden wir in Abschnitt [Schätzung der Gewinnwahrscheinlichkeit](#estimation-de-la-probabilite-de-gain) sehen. In Bezug auf den Stromverbrauch verbraucht ein NerdMiner 0,5 W; zum Vergleich, eine LED-Lampe verbraucht durchschnittlich 20 Mal mehr.

Bevor wir die verschiedenen Schritte durchgehen, listen wir das benötigte Material auf:

- ein [Lilygo T-Display S3](https://lilygo.cc/products/t-display-s3)
- ein [USB-C-Netzteil](https://amzn.eu/d/gIOot90)
- ein 3D-Gehäuse: Wenn Sie einen 3D-Drucker haben, können Sie die [3D-Datei herunterladen](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons), sonst können Sie es im [Online-Shop von Silexperience](https://silexperience.company.site/NerdMiner_V2-p544379757) kaufen.
- ein PC mit installiertem Chrome-Browser
- eine Internetverbindung
- eine Bitcoin-Adresse

Sie können auch ein vorgefertigtes NerdMiner-Kit bei verschiedenen Händlern kaufen, wie zum Beispiel:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

Zuerst werden wir sehen, wie man die Software auf den ESP-32 S3 flashen kann, und dann werden wir sehen, wie man ihn neu startet, um das WLAN-Netzwerk zu ändern. Diese Schritte sind für Windows-Benutzer gedacht. Wenn Sie ein Linux-Betriebssystem verwenden, führen Sie bitte die [Vorbereitungsschritte](#etapes-preliminaires-pour-utilisateurs-linux) aus, um die Erkennung des ESP-32 S3 durch Ihr System zu ermöglichen.

# Installation der NerdMiner_v2-Software

Die Installation der Software wird durch die Verwendung des Webflashers erheblich vereinfacht.

## Schritt 1: Vorbereitung des Webflashers

Zunächst müssen Sie zum [Online-Flasher NM2](https://bitmaker-hub.github.io/diyflasher/) gehen.

Wählen Sie dann die Firmware für Ihren ESP-32 aus. In den meisten Fällen ist dies die Standardversion: T-Display S3. Klicken Sie dann auf "Flash".

> ⚠️ Es ist wichtig, dass Sie den Chrome-Browser verwenden, da dieser standardmäßig das Flashen und den Zugriff auf Ihre USB-Ports ermöglicht.

![](assets/webflasher.png)

## Schritt 2: Anschließen des ESP-32

Sobald der Webflasher gestartet ist, öffnet sich ein Popup-Fenster, das die verschiedenen vom Browser erkannten USB-Ports anzeigt.
Sie können dann Ihren ESP-32 anschließen und ein neuer Port wird angezeigt (hier ist es der Port ttyACM0). Wählen Sie ihn aus und klicken Sie auf "Verbinden".

![](assets/flasher-port-serial.png)

Die Software wird dann in wenigen Sekunden auf Ihren ESP32 heruntergeladen.

![](assets/NM2-sucessfully-installed.png)

## Schritt 3: Konfiguration des NerdMiner

Die Konfiguration Ihres NerdMiners erfolgt über ein Smartphone oder einen Computer.
Aktivieren Sie WLAN und verbinden Sie sich mit dem lokalen Netzwerk NerdMinerAP. Wenn Sie ein Smartphone verwenden, wird die Konfigurationsseite automatisch geöffnet. Andernfalls geben Sie in einem Browser die Adresse 192.168.4.1 ein.
Wählen Sie dann "WiFi konfigurieren".

Sie können nun Ihren NerdMiner konfigurieren.
Beginnen Sie damit, sich mit Ihrem WLAN-Netzwerk zu verbinden, indem Sie Ihren Netzwerknamen auswählen und das zugehörige Passwort eingeben.

Dann können Sie den Mining-Pool auswählen, an dem Sie teilnehmen möchten. In der Bitcoin-Mining-Branche ist es üblich, die Rechenleistung zu bündeln, um die Chancen auf das Finden eines Blocks zu erhöhen, im Austausch für die Aufteilung der Belohnung proportional zur bereitgestellten Hashrate.
Für NerdMiner können Sie einen der folgenden Pools auswählen:

| Pool-URL          | Port  | URL                        | Status                                 |
| ----------------- | ----- | -------------------------- | -------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Standard-Solo-Mining-Pool, Open Source |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Wartung durch CHMEX                    |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Wartung durch djerfy                   |

Sobald Sie Ihren Pool ausgewählt haben, müssen Sie Ihre Bitcoin-Adresse eingeben, um die Belohnung im Falle (außergewöhnlich) des Auffindens eines Blocks zu erhalten.

Wählen Sie auch Ihre Zeitzone, damit der NerdMiner die Uhrzeit korrekt anzeigen kann.
Sie können jetzt auf "Speichern" klicken.

![](assets/wifi-configuration.jpg)

Herzlichen Glückwunsch, Sie sind jetzt Teil des Bitcoin-Mining-Netzwerks!

## Bedienung des NerdMiner

Die NerdMinerv2-Software besteht aus 3 verschiedenen Bildschirmen, auf die Sie zugreifen können, indem Sie auf die Schaltfläche oben rechts auf Ihrem Bildschirm klicken:

- Der Hauptbildschirm zeigt die Statistiken Ihres NerdMiners an.
- Der zweite Bildschirm zeigt die Uhrzeit, Ihre Hashrate, den Bitcoin-Preis und die Blockhöhe an.
- Der dritte Bildschirm bietet Zugriff auf die Statistiken des weltweiten Bitcoin-Mining-Netzwerks.
  ![](assets/NM2-screens.png)

Wenn Sie Ihren NerdMiner neu starten möchten, z.B. um das WLAN-Netzwerk zu wechseln, drücken Sie die obere Taste 5 Sekunden lang.

Wenn Sie einmal auf die untere Taste drücken, wird Ihr NerdMiner ausgeschaltet. Durch zweimaliges Klicken wird die Bildschirmausrichtung umgekehrt.

### Vorbereitende Schritte für Linux-Benutzer

Hier sind die Schritte, damit Chrome Ihren seriellen Port auf einem Linux-System erkennen kann.

1. Identifizieren Sie den zugehörigen Port:

- Schließen Sie Ihren ESP-32 an Ihren Computer an.
- Öffnen Sie ein Terminal.
- Geben Sie den folgenden Befehl ein, um alle Ports aufzulisten:
  - `dmesg | grep tty`
  - oder `ls /dev/tty*`
- Um sicherzugehen, welcher Port es ist, können Sie den Befehl erneut ausführen, ohne dass der ESP-32 angeschlossen ist.

2. Ändern Sie die Berechtigung des zugehörigen Ports:

- Standardmäßig erfordert der Zugriff auf serielle Ports Root-Berechtigungen. Wir werden sie also verfügbar machen, indem wir Ihren Benutzer zur Gruppe "dialout" hinzufügen.
  - `sudo usermod -a -G dialout IHR_BENUTZERNAME`, ersetzen Sie "IHR_BENUTZERNAME" durch Ihren Benutzernamen.
  - Melden Sie sich dann ab und wieder an oder starten Sie das System neu, um sicherzustellen, dass die Gruppenänderungen wirksam werden.

Jetzt, da Ihr ESP-32 von Ihrem System erkannt wird, können Sie zum [ersten Schritt](#schritt-1-vorbereitung-des-webflashers) zurückkehren, um die Software zu installieren.

## Fazit

Und da haben Sie es! Ihr NerdMiner_v2 ist jetzt konfiguriert und einsatzbereit.

Viel Spaß beim Mining und viel Glück!

### Schätzung der Gewinnwahrscheinlichkeit

Lassen Sie uns den Spaß haben, die Wahrscheinlichkeit abzuschätzen, dass wir die Belohnung für einen Block gewinnen können. Diese Schätzung ist grob und dient nur dazu, die Größenordnung der Wahrscheinlichkeit zu ermitteln.
Angenommen, unser NerdMiner hat eine Hashrate von etwa 50 kH/s und ist mit dem [Standard-Pool](https://web.public-pool.io/#/) verbunden, der eine Gesamthashrate von etwa 100 TH/s hat.

Angesichts einer Gesamthashrate von etwa 450 EH/s (das sind $4,5 \times 10^{20}$ Hashes pro Sekunde) können wir davon ausgehen, dass die Wahrscheinlichkeit, dass der Solo-Mining-Pool den nächsten Block gewinnt, 2 zu 10 Millionen beträgt, also etwa einmal alle 5 Millionen Blöcke, was etwa einmal pro Jahrhundert passieren kann. Und in einem solchen Fall würde ein NerdMiner einen fünf Milliardstel ($5 \times 10^{-10}$) der Blockbelohnung erhalten, also 31,25 Msats für eine Belohnung von 6,25 BTC.
Obwohl die Chancen, zu gewinnen, äußerst gering sind, kann Ihnen NerdMiner neben seiner Funktion als pädagogisches Werkzeug und Kuriosität auch ein Lotterieticket im Bitcoin-Mining zu einem marginalen Stromkostenpreis von 0,5 W bieten. Warum also nicht Ihr Glück versuchen?

### Weitere Informationen

Hier sind einige Links, falls Sie Ihre Lektüre zu diesem Thema ergänzen möchten:

- [NerdMiner_v2 Projektseite](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Vollständige Dokumentation zu NerdMiners](https://docs.bitwater.ch/nerd-miner-v2/)
