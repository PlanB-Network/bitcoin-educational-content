---
name: Raspberry Pi Zero
description: Wie man mit einem Raspberry Pi Zero und einem Zubehörkit einen minimalen, luftgetrennten und kostengünstigen Computer baut.
---
![cover](assets/cover.webp)



Wenn Sie schon eine Weile auf den Seiten von Plan ₿ Network unterwegs sind, haben Sie bereits gelernt, dass eine der am meisten empfohlenen Sicherheitseinstellungen, fast ein Muss, **die Verwaltung von Geldern durch Offline-Speicherung Ihrer privaten Schlüssel** ist.



Falls Sie es noch nicht entdeckt haben, finden Sie in diesem Tutorial Links zu Open-Source-Ressourcen, mit denen Sie mehr darüber erfahren können.



Um private Schlüssel offline zu verwalten, benötigt man daher ein dauerhaft vom Netzwerk getrenntes Gerät, sei es ein [Hardware-Wallet](https://planb.network/resources/glossary/hardware-wallet) oder ein Airgap-Computer, der dieser speziellen Funktion gewidmet ist.



Wie gehen Sie vor, wenn Sie z. B. nicht die Möglichkeit haben, Hardware zu kaufen, die nur diese Aufgabe erfüllt, Sie aber nicht auf diese Sicherheitsstufe verzichten wollen?



## Die Lösung


Was wäre, wenn ich Ihnen sagen würde, dass Sie ein Offline-Gerät in Form eines Airgap-Computers herstellen können, das die Größe und das Gewicht eines USB-Sticks hat und 35 Euro kostet? Würden Sie das nicht glauben?



Lesen Sie weiter.



Ich erzähle Ihnen mehr: Lesen Sie ganz durch. Die vorgeschlagene Lösung ist billig, aber sie ist nicht gerade die einfachste. Zunächst müssen Sie sich einen Überblick verschaffen, dann beschließen Sie, einen Teil Ihrer Zeit in persönliche Nachforschungen zu investieren und in aller Ruhe zu entscheiden, ob und wie Sie vorgehen wollen.



## Anforderungen


**1** Ein [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): Der PI Zero (ohne jegliche Zusatzbezeichnung) bildet die Grundlage für den Bau eines Computers mit minimaler Leistung, ist jedoch vor allem frei von Wi-Fi- und Bluetooth-Karten, die für den Zweck dieser Übung unerlässlich sind.





- Kosten**: etwa 15,00 zum Zeitpunkt der Erstellung dieses Tutorials (August 2025).
- Kontinuität der Produktion**: Raspberry garantiert die Produktion bis Januar 2030.



PI Zero ohne Wi-Fi und Bluetooth sind leider praktisch nicht mehr erhältlich. Möglicherweise können Sie die Alternativen PI Zero W und PI Zero 2W leichter finden. In diesem Fall können Sie die Verbindungsfunktionen deaktivieren, indem Sie die Konfigurationsdatei ändern. Nach der Installation des Betriebssystems müssen Sie diese Punkte in der Konfigurationsdatei hinzufügen:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



in einem Abschnitt dieses Leitfadens erfahren Sie, wie und wo Sie dies tun können. Wenn Sie jedoch ganz sicher gehen wollen, finden Sie im Internet mehrere Anleitungen zum Entfernen des Wi-Fi-Chips mit einem kleinen Cutter, der für die Arbeit an elektronischen Platinen geeignet ist.



**2** Ein _Starterkit_ für den Raspberry PI Zero: wie in der Raspberry-Welt üblich, ohne Gehäuse. Darüber hinaus sind die begrenzten Ressourcen eines solchen kleinen Board Bedingung die Möglichkeiten der Verbindung mit der Außenwelt.



Als ich mich entschied, weiterzumachen, fand ich [dieses Kit](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) voller Zubehör, um das volle Potenzial des PI Zero auszuschöpfen. Das Kit enthält einen USB A -> Micro-USB-Strom Supply, einen kleinen USB-Hub, einen Mini-HDMI -> HDMI-Adapter, einen Kupferkühlkörper und ein Aluminiumgehäuse. Das Kit enthält auch die Schrauben und Inbusschlüssel, die benötigt werden, um den PI Zero in das neue Gehäuse einzubauen.





- Kosten**: 19.99 Euro.



**3** Für dieses Tutorial müssen Sie keine großen Summen für den Airgap-Computer ausgeben. Sie sollten jedoch wissen, dass Sie eine USB-Tastatur und -Maus (unbedingt kabelgebunden, vermeiden Sie Bluetooth) und einen Monitor benötigen. Je nach Eingang Ihres Monitors benötigen Sie möglicherweise einen Adapter für Mini-HDMI, den einzigen verfügbaren Ausgang des PI Zero. Und schließlich sollten Sie bedenken, dass wir alle irgendwo im Haus eine nicht kabellose Tastatur und Maus haben - es ist Zeit, sie zu entfernen.



## Extra Budget



**4** Sie können den originalen Power-Supply von Raspberry für ca. 15,00 Euro erhalten.



**5** Ich persönlich habe mich für das im _Starterkit_ mitgelieferte Power-Supply entschieden, allerdings in Kombination mit einem USBA → miniUSB sogenannten `no data` Kabel, das 3,70 Euro kostet.



**6** Eine Micro-SD-Karte mit mindestens 32 GB Speicherkapazität, besser in Industriequalität.



**7** Du brauchst ein System, einen USB-zu-Micro-SD-Adapter, wie den, den du auf dem Bild siehst. Das Betriebssystem und der Speicher deines PI Zero funktionieren auf diesem Medium.



![img](assets/it/06.webp)



## Installation des Betriebssystems


Bevor Sie Ihren PI Zero in das Gehäuse einschließen, empfehle ich Ihnen, das Betriebssystem zu installieren. Dann können Sie die LED, die den Betrieb anzeigt, gleich überprüfen.



Um das Betriebssystem auszuwählen und zu brennen, habe ich mich für den einfachsten Weg entschieden: mit dem Tool `PI Imager` des Raspberry.



![img](assets/it/01.webp)



Gehe also auf das [Github von Raspberry](https://github.com/raspberrypi/rpi-imager/releases), um die neueste Version des Imagers herunterzuladen, und wähle diejenige, die am besten zu deinem Betriebssystem passt (v. 1.9.6 zum Zeitpunkt der Erstellung). Du wirst feststellen, dass neben jedem Asset auch der Hash der entsprechenden Datei angezeigt wird. Dieser wird uns für die Überprüfung nützlich sein.



![img](assets/it/02.webp)



Ich empfehle Ihnen, das Betriebssystem, das Sie auf Ihrem airgap-Computer verwenden werden, zu überprüfen, damit Sie sich keine Sorgen machen müssen. Dies gibt Ihnen die Gewissheit, dass Sie mit einer legitimen (nicht bösartigen) Version des Imagers und folglich des Raspi OS arbeiten.



Führen Sie die Überprüfung sofort nach dem Herunterladen durch, wenn Ihr Computer, den Sie normalerweise benutzen, mit dem Internet verbunden ist



Öffnen Sie dann das Linux-Terminal und bereiten Sie den Download vor, indem Sie ein Verzeichnis `raspios` erstellen, das für die Arbeit mit dem Programm nützlich ist.



![img](assets/it/19.webp)



Laden Sie den Imager für Ihre Linux-Distribution mit `wget` herunter.



![img](assets/it/20.webp)



Führen Sie abschließend den Befehl `sha256sum` aus und vergleichen Sie den Hash mit dem von Raspberry auf Github bereitgestellten Wert.



![img](assets/it/21.webp)



Unter Windows können Sie auch die Power Shell öffnen und den folgenden Befehl eingeben:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Sie erhalten den Hash, der mit dem auf Raspberry Github veröffentlichten übereinstimmen muss.



Sobald Sie den Download verifiziert haben, können Sie Imager auf Ihrem Alltagsrechner installieren und öffnen. Imager ist das Tool, das Sie benötigen, um das Betriebssystem auf die Micro-SD zu brennen, die die "Systemplatte" von PI Zero sein wird.



Der Vorgang ist denkbar einfach: Wählen Sie zunächst das Raspberry-Gerät aus, das Sie verwenden möchten (achten Sie also auf **Ihr Modell** des Raspi Zero), dann die Betriebssystemversion und schließlich den Speicherort der Micro-SD-Karte, auf die das Betriebssystem geflasht werden soll.



### Erster Schritt



![img](assets/it/03.webp)



### Zweiter Schritt



![img](assets/it/07.webp)



**Bitte beachten**: Wählen Sie `PI OS 32-bit`, das einzige, das mit PI Zero funktioniert.



### Dritter Schritt



![img](assets/it/08.webp)



(Achten Sie darauf, dass die Option _Systemlaufwerk ausschließen_ nicht ausgewählt ist, damit Sie nicht aufgefordert werden, das Betriebssystem des Raspi auf Ihrem Computer zu installieren)



Wenn alles eingerichtet ist, fragt der Imager Sie, ob Sie benutzerdefinierte Einstellungen verwenden möchten. Wählen Sie, was Sie möchten, oder klicken Sie auf _No_, um mit den Standardoptionen fortzufahren.



![img](assets/it/09.webp)



Bestätigen Sie, dass Sie den Inhalt der Micro-SD-Karte löschen möchten



![img](assets/it/10.webp)



Der Imager beginnt mit dem Flashen des Betriebssystems auf die Micro-SD, eine Bildlaufleiste informiert Sie über den Fortschritt.



![img](assets/it/11.webp)



Am Ende erfolgt eine automatische Überprüfung, ich rate Ihnen, diese nicht abzubrechen.



![img](assets/it/12.webp)



Schließlich erscheint eine Meldung auf dem Bildschirm, und wenn alles erfolgreich war, sieht sie so aus, wie auf dem Bild zu sehen ist.



![img](assets/it/13.webp)



Nun kannst du die microSD-Karte wirklich aus dem Lesegerät entfernen und in den Slot des PI Zero einsetzen. Schalte den kleinen Raspberry ein und beobachte die LED: Wir erwarten, dass sie grün leuchtet und blinkt, was auf das normale Laden des Betriebssystems hinweist, und dann dauerhaft eingeschaltet bleibt. Falls du andere Anzeichen hast, z. B. wenn die LED regelmäßig blinkt oder rot leuchtet, siehe die FAQ oder [die Support-Forenseiten](https://forums.raspberrypi.com/).



## Erste Konfiguration


Der erste Start von Raspi OS ist etwas langsamer als üblich, da es eine Reihe von Installationsaufgaben durchführen muss. Aber wenn alles gut gegangen ist, werden Sie einen Willkommensbildschirm vorfinden.



![img](assets/it/14.webp)



Klicken Sie auf _Weiter_, um die geografische Region festzulegen, insbesondere um die richtige Tastatur zu laden. Achten Sie besonders auf Letzteres.



![img](assets/it/15.webp)



Klicken Sie auf _Weiter_ und Sie werden aufgefordert, Ihren Benutzer zu erstellen, notieren Sie Ihre Anmeldedaten und bewahren Sie sie gut auf.



![img](assets/it/16.webp)



Der Assistent bittet Sie, einen Standard-Webbrowser auszuwählen, entweder Chromium oder Firefox; er kann Sie auch nach den Wi-Fi-Netzwerkeinstellungen fragen, wenn Sie mit einer Zero W oder 2W PI arbeiten. Fahren Sie fort und klicken Sie auf _Skip_.



An einem bestimmten Punkt werden Sie aufgefordert, die integrierte Software und das Betriebssystem zu aktualisieren. Wählen Sie _Skip_: Für die Zwecke dieser Übung bauen wir tatsächlich einen Offline-Rechner, der ab diesem Zeitpunkt offline bleiben muss.



Schließlich werden Sie möglicherweise aufgefordert, `ssh` zu aktivieren, aber lehnen Sie auch diesen Schritt ab, da es sich um eine Zero-Airgap-IP handelt.



![img](assets/it/17.webp)



Es gibt nicht viel mehr zu konfigurieren. Wenn Sie fertig sind, starten Sie den Raspberry neu, damit die Änderungen wirksam werden.



![img](assets/it/18.webp)



## Ein neuer Computer-Luftspalt


Nach dem Neustart ist dein neuer airgap Computer bereit. PI Zero zeigt Ihnen den neuen Desktop, mit dem Sie entweder über die grafische Benutzeroberfläche oder über die Kommandozeile arbeiten können.



![img](assets/it/22.webp)



### Erste Schritte für PI Zero W oder 2W


Wenn Sie mit einem Raspberry PI Zero W oder 2W arbeiten, hat Ihr Board Chips für Wi-Fi und Bluetooth an Bord. Bei der ersten Einrichtung haben Sie die Verbindungskonfiguration übersprungen, sodass der PI Zero nicht mit dem Internet verbunden ist. Jetzt können Sie die beiden Chips per Software dauerhaft deaktivieren.



Raspi OS stellt eine Datei `config.txt` zur Verfügung, die Sie nach Ihren Wünschen bearbeiten können. Die `config` befindet sich in der `boot` Partition, im `firmware` Verzeichnis, und Sie können sie mit `root` Rechten bearbeiten und speichern.



Öffnen Sie das Terminal über das Symbol oben links und es wird zu `root`.(1)



![img](assets/it/23.webp)



(1) Wenn Raspi OS Sie nicht dazu gebracht hat, das `root`-Passwort während der vorherigen Schritte zu erstellen, empfehle ich Ihnen, dies jetzt mit dem `passwd`-Befehl zu tun. Die Tatsache, dass sich der `root`-Benutzer unabhängig von Ihrem persönlichen Benutzer bewegt, kann sich in Wiederherstellungssituationen als sehr praktisch erweisen.



Suchen Sie im Terminal nach der Datei `config.txt` und bereiten Sie sich darauf vor, sie mit dem Editor `nano` zu bearbeiten.



![img](assets/it/24.webp)



Die Bearbeitung sollte am Ende der gesamten `config` erfolgen, nach den Worten `[All]`. An dieser Stelle fügen Sie die zu Beginn des Lehrgangs gezeigten "dtoverlay"-Befehle ein.



![img](assets/it/25.webp)



Speichern, schließen und neu starten. Im nächsten Schritt gehen wir zur Erkundung des kleinen Raspberrys über.



## Was ist von diesem Gerät zu erwarten?


Laut den [technischen Spezifikationen](https://www.raspberrypi.com/products/raspberry-pi-zero/) auf der Raspberry-Website verfügt der PI Zero über einen BCM2835-Prozessor mit einem Kern und 512 MB RAM, was ihn nicht sehr leistungsstark erscheinen lässt.



Da das Terminal leichter ist, werden wir die Befehlszeile verwenden, um die Systemkonfigurationen zu untersuchen.



Nach dem Einschalten sehen Sie einen kurzen regenbogenfarbenen Bildschirm, gefolgt von einer Willkommensnachricht von Raspberry und, in der unteren linken Ecke, Kernel-Meldungen zum Booten.



Wenn der PI OS-Desktop erscheint, öffnen Sie das Terminal und geben Sie ein:



```bash
uname -a
```


Dieser Befehl zeigt Ihnen die aktuell verwendete Kernel-Version auf dem Bildschirm an, sowie weitere Informationen.



![img](assets/it/26.webp)



Sie können auch Informationen über die CPU und die Hardware anzeigen, indem Sie diese eingeben:



```bash
lscpu
```



![img](assets/it/27.webp)



Und siehe auch `proc/mem/info`.



![img](assets/it/28.webp)



Um die Version von Debian und den Codenamen der Veröffentlichung herauszufinden:



```` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



```` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Verwenden Sie


Obwohl die Leistung (auf dem Papier und im Vergleich zur Leistung heutiger Rechner) begrenzt erscheint, ist der PI Zero sehr leistungsfähig, insbesondere als Terminal.





- Zuerst können Sie die Hauptmenüs aufrufen und sich von der Tafel _Software hinzufügen/entfernen_ inspirieren lassen, wo Sie eine Reihe von Dienstprogrammen zum Programmieren und Üben finden. Denken Sie daran, dass Sie dies auch vom Terminal aus tun können, aber immer mit `root`-Rechten.



![img](assets/it/33.webp)





- Sie können dieses Offline-Gerät "adoptieren", um eine Vielzahl vertraulicher Dokumente zu speichern, auf die Sie bei Bedarf zugreifen können, ohne jemals mit dem Internet verbunden zu sein.
- Sie können diese Konfiguration verwenden, um Ihre GPG-Schlüssel sicher zu verwahren.
- Du könntest dieses neue „Spielzeug“ sogar als Airgap-Signaturgerät nutzen, [indem du den Ratschlägen von Arman The Parman folgst](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Unter den Geldbörsen, die ich kenne, ist die einzige, die eine 32-Bit-Version bietet Electrum. Nun: die Zero IP, wie wir es in diesem Tutorial vorbereitet würde Ihnen erlauben, die privaten Schlüssel offline die Einrichtung für Wallet Luftspalt, die wir in diesem Tutorial behandelt zu halten:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Schlussfolgerungen


Die Einrichtung hat wahrscheinlich einen großen Schwachpunkt: Die Micro-SD ist ein Medium, das Probleme bereiten kann. Sie ist anfällig für starke Beanspruchung; vielleicht haben Sie bereits Erfahrung damit, wenn Sie sie mit Ihrem Telefon verwenden. Nachdem Sie die gesamte Software installiert haben, die Sie auf dem Zero airgap IP verwenden möchten, sollten Sie mit dem verfügbaren Raspi OS-Tool ein gutes Backup der wertvollen Micro-SD erstellen.



![img](assets/it/34.webp)



Wenn Ihre Bedürfnisse und damit Ihre finanziellen Möglichkeiten wachsen, können Sie andere Raspberry- oder ähnliche Lösungen erkunden. Apropos Speicher: Der PI 5 bietet zum Beispiel die Möglichkeit, ein M2-NVME-Laufwerk einzubauen, das sicherlich robuster ist als microSD.



Vergessen Sie nicht, sich Notizen zu machen und jeden Schritt der Installation von Dienstprogrammen, die Sie offline verwenden wollen, zu dokumentieren. **Früher oder später wird ein aktualisiertes Raspi-Betriebssystem herauskommen**, das Sie unbedingt nutzen wollen. Dann müssen Sie alles löschen und noch einmal von vorne anfangen (vielleicht mit einer neuen Micro-SD 😂).



Die Übung, die wir soeben durchgeführt haben, wird Ihnen noch lange in Erinnerung bleiben, vorausgesetzt, es ist auch Ihr erstes Experiment. Es ist nicht immer möglich, die Hardware für "eingebettete" Operationen offline zu verwenden, ohne die Aufmerksamkeit auf eine Maschine zu vernachlässigen, die man von Zeit zu Zeit einschalten und überprüfen muss.



Aber Sie haben es geschafft, herzlichen Glückwunsch! Und Sie können diese Lösung all jenen vorschlagen, die ihr Budget einschränken müssen.