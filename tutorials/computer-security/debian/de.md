---
name: Debian
description: Eine Linux-Distribution, die für ihre Stabilität, Robustheit und Kompatibilität bekannt ist.
---

![cover](assets/cover.webp)



Debian ist eine freie GNU/Linux-Distribution, die für ihre Robustheit und Zuverlässigkeit bekannt ist. Der Linux-Kernel und alle Pakete werden rigoros getestet, um felsenfeste Stabilität und ein hohes Maß an Sicherheit zu gewährleisten. Debian eignet sich sowohl für Server als auch für Workstations und bietet eine benutzerfreundliche Erfahrung und einen umfangreichen Software-Katalog. Ob Sie nun ein sicheres System für den täglichen Gebrauch oder eine Produktionsumgebung suchen, Debian ist die richtige Wahl.



## Warum Debian wählen?





- Frei und offen**: Debian ist vollständig quelloffen, was Transparenz und keine Lizenzgebühren garantiert.
- Stabilität und Sicherheit**: Jede Veröffentlichung durchläuft einen gründlichen Testprozess, was Debian zu einer der zuverlässigsten und sichersten Distributionen auf dem Markt macht.
- Aktive Community**: Eine große Community und eine umfangreiche Dokumentation stehen Ihnen zur Verfügung, wenn Sie Unterstützung benötigen.
- Leichtgewichtig und skalierbar**: Sie können Debian auf Rechnern mit bescheidenen Ressourcen installieren und dabei eine gute Leistung beibehalten.
- Umfangreicher Softwarekatalog**: Über 50.000 offizielle Pakete sind über die Repositories verfügbar.



## Wählen Sie eine Interface-Grafik



Debian bietet mehrere Desktop-Umgebungen, die Ihren Bedürfnissen entsprechen:





- GNOME**: moderner, intuitiver Interface, ideal für Anfänger. Es bietet ein flüssiges, einfach zu bedienendes grafisches Menü für den Zugriff auf Anwendungen.
- XFCE**: leicht und schnell, perfekt für weniger leistungsstarke Rechner.
- KDE Plasma**: hochgradig anpassbar, mit einem Windows-ähnlichen Erscheinungsbild.
- Cinnamon**: einfacher, eleganter Interface, inspiriert von Windows.
- LXDE / LXQt**: ultraleicht, geeignet für ältere Computer.
- MATE**: einfach und klassisch, ähnlich dem alten GNOME.



💡 Für ein komfortables, leicht zu handhabendes Erlebnis ist **GNOME sehr zu empfehlen**.



## Installieren und Konfigurieren von Debian


### Hardware-Anforderungen



Bevor Sie mit der Installation beginnen, vergewissern Sie sich bitte, dass Sie über die folgenden Geräte verfügen:





- USB-Stick**: mindestens 8 GB, um das bootfähige ISO-Image zu speichern.
- Speicher mit wahlfreiem Zugriff (RAM)**: 4 GB für eine reibungslose Installation und Bedienung.
- Festplattenspeicher**: Mindestens 15 GB freier Speicherplatz für das System und die Updates.



### Herunterladen



Die Wahl des Debian-Images hängt von Ihrer Prozessorarchitektur ab:





- AMD64**: Laden Sie die "Live-Hybrid"-Edition von der [Download]-Liste herunter (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: Holen Sie sich das DVD-Image von der offiziellen [Debian]-Website (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Andere Architekturen**: finden Sie die ISO, die Ihrer Architektur entspricht, [hier] (https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Erstellen eines bootfähigen USB-Sticks



Sobald Sie das entsprechende ISO-Image heruntergeladen haben, erstellen Sie Ihr Installationsmedium:




- Laden Sie Balena Etcher** von der [offiziellen Website] (https://etcher.balena.io/) herunter, holen Sie sich die Binärdatei für Ihr System und installieren Sie sie.



![etcher](assets/fr/02.webp)





- Starten Sie Etcher**: Öffnen Sie die Software und wählen Sie das zuvor heruntergeladene Debian-ISO-Image.
- Wählen Sie den USB-Stick**: Geben Sie Ihren Stick (8 GB+) als Ziel an.
- Flash starten**: Klicken Sie auf **Flash!** und warten Sie, bis der Vorgang abgeschlossen ist.



![flash](assets/fr/03.webp)



Ihr USB-Stick ist nun bereit für die Installation von Debian.



## Installation von Debian auf Ihrem System



### Booten vom USB-Stick



So starten Sie die Installation von Ihrem USB-Stick:




- Schalten Sie** den Computer vollständig aus.
- Starten Sie** neu und rufen Sie dann BIOS/UEFI auf, indem Sie sofort `ESC`, `F2`, `F11` (oder die entsprechende Taste je nach Hersteller) drücken.
- Wählen Sie im Boot-Menü **Ihren USB-Stick** als Boot-Gerät aus.
- Bestätigen Sie** mit der Eingabetaste, um das Debian-Image zu starten: Dies führt Sie zum Willkommensbildschirm des Installers.



### Starten der Installation



Startbildschirm:



![starting](assets/fr/04.webp)



Wenn Sie vom USB-Stick booten, bietet der Debian-Begrüßungsbildschirm mehrere Optionen an:




- Live-System**: Startet Debian ohne Installation, ideal zum Testen der Umgebung.
- Start Installer**: startet die Installation direkt auf der Hard-Diskette.
- Erweiterte Installationsoptionen**: ermöglicht Ihnen den Zugriff auf benutzerdefinierte Installationsmodi.



Um Debian im Live-Modus zu erkunden, wählen Sie **Live-System** und bestätigen Sie mit **Eingabe**. Sie können dann die Installation starten, indem Sie in der Live-Umgebung auf **Debian installieren** klicken.



![system](assets/fr/05.webp)





- Sprachauswahl** (optional)



Wählen Sie die Hauptsprache Ihres Debian-Systems aus der Liste und klicken Sie dann auf OK.



![language](assets/fr/06.webp)





- Zeitzone** (GMT)



Wählen Sie Ihre geografische Zone, um Datum und Uhrzeit automatisch einzustellen.



![timezone](assets/fr/07.webp)





- Tastatur-Layout



Wählen Sie die Sprache und das Layout Ihrer Tastatur. Verwenden Sie das integrierte Testfeld, um zu prüfen, ob jede Taste das erwartete Zeichen erzeugt.



![keyboard](assets/fr/08.webp)



### Partitionierung der Festplatte





- Datenträger löschen**: Wenn Sie eine eigene Partition haben, wird mit dieser Option der gesamte Inhalt gelöscht.
- Manuelle Partitionierung**: Wählen Sie diese Option, um Partitionen nach Bedarf zu erstellen, ihre Größe zu ändern oder zu löschen.



![disk](assets/fr/09.webp)





- Erstellen eines Benutzerkontos



Geben Sie Ihren vollständigen Namen, Ihren Kontonamen und ein sicheres Passwort ein, damit Ihre Sitzung sicher ist.



![user](assets/fr/10.webp)





- Zusammenfassung der Parameter**



Es wird eine Übersicht über Ihre Auswahl angezeigt: Überprüfen Sie jeden Punkt und gehen Sie zurück, um ihn gegebenenfalls zu ändern.



![settings](assets/fr/11.webp)





- Starten der Installation



Klicken Sie auf **Installieren**, um mit dem Kopieren der Dateien und der Konfiguration des Systems zu beginnen, und warten Sie dann, bis der Vorgang abgeschlossen ist.



![install](assets/fr/12.webp)





- Neustart**



Sobald die Installation abgeschlossen ist, starten Sie den Computer neu, um alle Konfigurationen zu übernehmen und auf Ihr neues Debian-System zuzugreifen.



![restart](assets/fr/13.webp)



Geben Sie beim Start den Benutzernamen und das Kennwort für den Zugriff auf das System ein.



![login](assets/fr/14.webp)



## Aktualisierung des Systems



Bevor Sie Ihr System in Betrieb nehmen, sollten Sie es unbedingt aktualisieren. So profitieren Sie von den neuesten Software-Patches, aktuellen Repositories und in einigen Fällen auch von Sicherheits-Patches für das Betriebssystem selbst.



### Option 1: Aktualisierung über den grafischen Interface (GNOME)



Wenn Sie Debian mit der GNOME-Desktop-Umgebung installiert haben, können Sie Aktualisierungen grafisch durchführen. Öffnen Sie dazu die Anwendung **Software** und gehen Sie dann auf die Registerkarte **Aktualisierungen**. Klicken Sie dann auf **Neustart und Aktualisierung**, um den Prozess zu starten.



### Option 2: Aktualisierung über das Terminal (empfohlen)



Diese Methode bietet eine umfassendere Kontrolle. Sie ermöglicht die Aktualisierung von Repositories, Softwarepaketen und ggf. des Kernels.




- Öffnen Sie das Terminal mit der Tastenkombination "Strg + Alt + T".
- Aktualisieren Sie die Liste der verfügbaren Pakete mit dem folgenden Befehl:



```shell
sudo apt update
```



Geben Sie Ihr Passwort ein, wenn Sie dazu aufgefordert werden (beachten Sie, dass während der Eingabe keine Zeichen angezeigt werden - das ist normal).





- So installieren Sie verfügbare Updates:



```shell
sudo apt full-upgrade
```



## Entdecken Sie die grundlegenden Aufgaben



### Surfen im Internet



Der Standard-Webbrowser unter Debian ist **Firefox**. Wenn Sie einen anderen Browser bevorzugen, können Sie einen anderen installieren, sofern er in den Debian-Repositorien verfügbar ist (z. B. Chromium, Brave...).



### Textverarbeitung



Die **LibreOffice**-Suite wird unter Debian standardmäßig installiert.





- Zum Schreiben von Dokumenten verwenden Sie **LibreOffice Writer**, das Äquivalent zu Microsoft Word.
- Für Tabellenkalkulationen ist **LibreOffice Calc** eine Alternative zu Excel.
- Schließlich können Sie mit **LibreOffice Impress** Präsentationen erstellen, genau wie mit PowerPoint.



## Installation von Anwendungen



Es gibt zwei Möglichkeiten, Anwendungen unter Debian zu installieren:



### Grafische Methode:



Sie können den **Softwaremanager** (zugänglich über die grafische Interface) verwenden, um Anwendungen zu suchen und zu installieren.



### Befehlszeilenmethode:



Wenn die gesuchte Anwendung nicht im grafischen Interface angezeigt wird oder wenn Sie das Terminal bevorzugen, verwenden Sie den folgenden Befehl:



```shell
sudo apt install <name>
```



Ersetzen Sie `<Name>` durch den Namen des Pakets. Zum Beispiel, um `curl` zu installieren:



```shell
sudo apt install curl
```



### Installieren eines manuell heruntergeladenen Pakets:



Wenn Sie eine `.deb`-Datei (Debian-Paket) heruntergeladen haben, können Sie sie mit dem folgenden Befehl installieren:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Ihr Debian-System ist nun installiert und kann für Ihre täglichen Aufgaben verwendet werden.


Dank der **GNOME**-Desktop-Umgebung können Sie über eine benutzerfreundliche grafische Interface auf eine Vielzahl von Anwendungen zugreifen, die sowohl für Anfänger als auch für fortgeschrittene Benutzer ideal sind.



Es ist auch möglich, die Arbeitsumgebung zu wechseln (z.B. zu XFCE, KDE, etc.), ohne Debian neu installieren zu müssen. Verwenden Sie dazu einfach das Terminal und installieren Sie die neue Umgebung Ihrer Wahl.



Um mehr über Debian und allgemein über GNU/Linux-Distributionen zu erfahren, empfehle ich Ihnen diesen Kurs:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1