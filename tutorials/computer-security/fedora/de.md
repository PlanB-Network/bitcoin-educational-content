---
name: Fedora
description: Die Linux-Distribution, die Ihnen einen kostenlosen, vollständigen und sicheren Arbeitsbereich bietet.
---


![cover](assets/cover.webp)





Fedora ist ein freies, quelloffenes Linux-Betriebssystem, das 2003 auf den Markt kam, von der **Fedora-Projekt**-Gemeinschaft entwickelt und von **Red Hat Linux** unterstützt wird. Es ist bekannt für seine Stabilität, gute Leistung und Benutzerfreundlichkeit, was es zu einer ausgezeichneten Wahl für Anfänger und fortgeschrittene Benutzer gleichermaßen macht. Das System läuft auf den meisten modernen Prozessorarchitekturen und lässt sich daher leicht auf praktisch jedem Computer installieren. Fedora ist auch in mehreren vorkonfigurierten Editionen erhältlich, die als "Fedora Spins" oder "Fedora Editions" bezeichnet werden und für spezielle Anforderungen (Videospiele, Astronomie, Entwicklung...) konzipiert sind.



## Fedora Linux Architektur



Wie Sie bereits gelesen haben, ist Fedora ein freies Betriebssystem, das auf dem Linux-Kernel basiert. Der Linux-Kernel ist der Teil des Betriebssystems, der mit der Computerhardware kommuniziert und Systemressourcen wie Speicher und Rechenleistung verwaltet.



Fedora Linux enthält eine Vielzahl von Software-Tools und Anwendungen, die für die Ausführung des Betriebssystems auf dem Linux-Kernel erforderlich sind. Die modulare Architektur von Fedora bedeutet, dass es hauptsächlich aus einer Sammlung einzelner Komponenten besteht, die bei Bedarf einfach hinzugefügt, entfernt oder ersetzt werden können. Dies ermöglicht es Ihnen, das Betriebssystem so zu gestalten, dass Sie nur die Ressourcen verwenden, die Sie benötigen.



Fedora enthält auch eine Desktop-Umgebung, d.h. den Interface, über den die Benutzer Aufgaben ausführen und auf Anwendungen zugreifen. Die Standard-Desktop-Umgebung von Fedora ist GNOME, eine benutzerfreundliche, einfach zu bedienende und stark anpassbare Desktop-Umgebung.



## Warum Fedora wählen?



Unter der Vielzahl der verfügbaren Linux-Distributionen sticht Fedora vor allem durch:





- Modularität**: Da Fedora mit verschiedenen Prozessorarchitekturen kompatibel ist, kann es auf den meisten Computern installiert werden, auch auf solchen mit geringer Leistung, und passt sich perfekt an Ihre Bedürfnisse an.





- Ein einfaches, intuitives Interface**: Fedora kombiniert ein modernes grafisches Interface mit einem leistungsstarken Kommandozeilen-Interface, wodurch es für alle Profile einfach zu bedienen ist.





- Kernel-Stabilität**: Fedora basiert auf Red Hat und ist bekannt für die Zuverlässigkeit seiner Updates, insbesondere der Kernel-Updates, die dank der kostenlosen Beiträge einer großen Community ohne größere Fehler durchgeführt werden.





- Schnelle, einfache Installation**: Mit einer Image-Größe von nur 3 GB ist die Installation schnell und einfach, auch auf Rechnern mit begrenzten Ressourcen.



## Fedora-Ausgaben



Abhängig von Ihrem Profil und Ihrer Nutzung bietet Fedora Editionen, die Ihren Bedürfnissen entsprechen. Sie finden hauptsächlich:





- Fedora Workstation**: Diese Edition ist ideal für den privaten und/oder professionellen Einsatz auf Ihren Computern und enthält allgemeine Dienstprogramme wie Browser, eine Office-Suite (Texteditoren) und Software zur Medienwiedergabe.





- Fedora Server**: Diese Edition ist der Serververwaltung gewidmet. Fedora Server enthält eine Vielzahl von Tools, die Ihnen bei der Bereitstellung und Verwaltung von Servern in Ihrem eigenen Umfang helfen.





- Fedora CoreOS**: Möchten Sie Cloud-Anwendungen einfach ausführen und bereitstellen? Fedora CoreOS ist die Edition, die Ihnen die Werkzeuge zum Erstellen und Verwalten von Images, z. B. mit Docker und Kubernetes, bietet.



In diesem Tutorial werden wir uns mit der Fedora Workstation Edition beschäftigen. Die unten beschriebenen Prozesse sind jedoch für die anderen Editionen ähnlich.



## Installieren und Konfigurieren von Fedora Workstation



Die Installation von Fedora Workstation erfordert die folgende Hardwarekonfiguration:




- Ein USB-Stick mit mindestens **8 GB** zum Booten des Betriebssystems.
- Mindestens **40 GB freier Speicherplatz** auf der Hard-Festplatte Ihres Computers.
- 4 GB RAM** für ein reibungsloses Erlebnis.



### Fedora Workstation herunterladen



Sie können die [Fedora Workstation] Edition (https://fedoraproject.org/fr/workstation/download) von der offiziellen Website des Fedora-Projekts herunterladen. Wählen Sie dann die Version aus, die Ihrer Prozessorarchitektur entspricht (32-Bit - 64-Bit) und klicken Sie auf das Symbol **Download**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Einen bootfähigen USB-Stick erstellen



Um Fedora zu installieren, müssen Sie einen bootfähigen USB-Stick mit einer Software wie [Balena Etcher] (https://etcher.balena.io/) erstellen.



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Sobald Sie die Installation von Balena Etcher abgeschlossen haben, öffnen Sie die Anwendung und wählen Sie das heruntergeladene Fedora Workspace ISO-Image aus. Wählen Sie Ihren USB-Stick als Zielmedium und klicken Sie auf die Schaltfläche **Flash**, um mit der Erstellung des bootfähigen Schlüssels zu beginnen.



![boot](assets/fr/05.webp)


### Installation von Fedora



Wenn Sie den USB-Stick gebootet haben, schalten Sie den Computer aus.


Schalten Sie Ihren Computer ein und rufen Sie das BIOS während des Starts auf, indem Sie die Taste `F2`, `F12` oder `ESC` drücken, je nach Computer.



Wählen Sie in den Boot-Optionen Ihren USB-Stick als primäres Boot-Gerät aus. Wenn Sie diese Auswahl bestätigen, wird Ihr Computer neu gestartet und das Fedora-Installationsprogramm** auf dem USB-Stick wird automatisch gestartet.



Sobald Ihr Computer vom USB-Stick gebootet hat, erscheint der **GRUB-Bildschirm**.



In diesem Stadium haben Sie die folgenden Möglichkeiten:




- Medium testen**: Mit dieser Option können Sie die Integrität des USB-Sticks überprüfen und sicherstellen, dass alle für eine korrekte Installation erforderlichen Abhängigkeiten vorhanden sind. Dies ist ein optionaler Schritt, der jedoch empfohlen wird, wenn Sie Zweifel am USB-Stick haben.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Fedora starten**: Damit wird Fedora im "Live"-Modus gestartet, ohne Installation.



Klicken Sie auf dem Fedora-Desktop (Live-Modus) auf **Fedora installieren** (oder auf Hard-Diskette installieren), um den Installationsprozess zu starten. Sie können sich für eine spätere Installation entscheiden und Fedora testen, ohne es installieren zu müssen.



![install-live](assets/fr/08.webp)



Der erste Schritt besteht darin, Fedoras **Installationssprache** und **Tastaturlayout** auszuwählen



![language](assets/fr/10.webp)





- Auswahl der Installationsdiskette:



Wählen Sie die Hard-Diskette, auf der Sie Fedora installieren möchten.



Wenn die Festplatte leer ist, verwendet Fedora automatisch den gesamten verfügbaren Speicherplatz. Andernfalls können Sie die Partitionierung anpassen (manuell oder automatisch).



![disk](assets/fr/11.webp)





- Verschlüsselung:



In diesem Stadium schlägt Fedora vor, Ihre Festplatte zu verschlüsseln, um ein zusätzliches Layer an Sicherheit zu schaffen. Dadurch wird sichergestellt, dass Ihre Daten nur von Ihrem Fedora-System gelesen werden können.



![chiffrement](assets/fr/12.webp)



Bevor Sie die Installation starten, zeigt Fedora eine Zusammenfassung Ihrer Auswahl an. Bestätigen Sie diese und klicken Sie auf die Schaltfläche "Installieren", um die Fedora-Installation zu starten.



![resume](assets/fr/13.webp)



Während der Installation kopiert Fedora Dateien und konfiguriert das System. Nach Abschluss der Installation wird der Computer automatisch neu gestartet.



![installation](assets/fr/14.webp)



### Grundlegende Konfiguration


Bei der ersten Verwendung müssen Sie noch einige Einstellungen vornehmen:




- Ändern Sie die Systemsprache, falls erforderlich.



![language](assets/fr/15.webp)





- Wählen Sie ein Tastaturlayout, das Ihren Wünschen entspricht.



![keyboard](assets/fr/16.webp)





- Wählen Sie Ihre Zeitzone, indem Sie den Namen Ihrer Stadt in die Suchleiste eingeben und dann auf den entsprechenden Vorschlag klicken.



![timezone](assets/fr/17.webp)





 - Aktivieren oder deaktivieren Sie den Zugriff auf Ihre Position für Anwendungen, die dies benötigen, sowie das automatische Senden von Fehlerberichten.



![location](assets/fr/18.webp)





- Entscheiden Sie, ob Sie Software-Repositories von Drittanbietern aktivieren möchten.



![logs](assets/fr/19.webp)





- Geben Sie Ihren vollständigen Namen ein und legen Sie einen Benutzernamen für Ihr Konto fest.



![name](assets/fr/20.webp)





- Erstellen Sie ein sicheres Passwort für Ihre Sitzung: so lang wie möglich (mindestens 20 Zeichen), so zufällig wie möglich und mit einer Vielzahl von Zeichen (Kleinbuchstaben, Großbuchstaben, Zahlen und Symbole). Denken Sie daran, Ihr Passwort zu speichern.



![mdp](assets/fr/21.webp)



Sobald alle diese Schritte abgeschlossen sind, starten Sie Fedora und können es sofort verwenden, ohne einen weiteren Neustart.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Sobald Ihre Installation abgeschlossen ist, können Sie Ihr Interface mit einigen vorinstallierten Dienstprogrammen konsultieren.



![install-now](assets/fr/09.webp)



## Entdecken Sie die grundlegenden Aufgaben



### Surfen im Internet


Der Standardbrowser von Fedora ist **Firefox**. Er ist einfach zu benutzen und für die meisten Bedürfnisse geeignet.


Wenn Sie einen anderen Browser bevorzugen, können Sie ihn über den **Softwaremanager** oder über das **Terminal** installieren.


### Textverarbeitung


Fedora enthält standardmäßig die Office-Suite **LibreOffice**, die mehrere nützliche Werkzeuge bietet:




- Writer** für die Textverarbeitung.
- Calc** für Tabellenkalkulationen.
- Impress** zum Erstellen von Präsentationen.


## Installation von Anwendungen


Um neue Anwendungen zu installieren, können Sie Fedoras **Softwaremanager** (genannt _Software_) verwenden, der die Installation einfach und visuell gestaltet.  Allerdings ist die Verwendung des **Terminals** oft schneller und genauer.



Denken Sie vor der Installation von Software immer daran, die **Repositorien** zu aktualisieren, um sicherzustellen, dass Sie Zugang zu den neuesten verfügbaren Versionen haben.



Verwenden Sie dann den folgenden Befehl, um die Installation der gewünschten Anwendung zu starten:


sudo dnf install software_name`


## Aktualisierung des Betriebssystems


Nach der Installation ist es wichtig, Fedora zu aktualisieren, um von den neuesten Sicherheitspatches und Software-Updates zu profitieren.


### Option 1: Über Interface-Grafik




- Öffnen Sie Fedora **Einstellungen** und gehen Sie dann zum Abschnitt **System**.
- Klicken Sie auf **Softwareaktualisierung**.
- Starten Sie den Download der Updates und warten Sie, bis der Vorgang abgeschlossen ist.



Nach der Installation von Updates kann ein **Neustart** erforderlich sein.


### Option 2: Über das Terminal




- Öffnen Sie ein Terminal und beginnen Sie mit der Aktualisierung der **Repositorien**, um sicherzustellen, dass Sie die neuesten Versionen von:



```shell
sudo dnf check-update
```





- Aktualisieren Sie anschließend die gesamte installierte Software mit dem folgenden Befehl:



```shell
sudo dnf upgrade
```



Jetzt ist Ihr Fedora-System auf dem neuesten Stand und bereit für alle Ihre täglichen Aufgaben. Entdecken Sie unser Tutorial über Linux Mint, eine weitere Linux-Distribution, und wie Sie eine gesunde und sichere Umgebung für Ihre Bitcoin-Transaktionen einrichten können.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5