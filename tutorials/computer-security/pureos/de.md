---
name: PureOS
description: Die Linux-Distribution, die Ihnen die Kontrolle über Ihr digitales Leben gibt.
---

![cover](assets/cover.webp)



Der Schutz persönlicher Daten hat im digitalen Zeitalter für jeden Internetnutzer höchste Priorität. Unternehmen, Organisationen und sogar Betriebssysteme sind nützliche Informationsquellen, um Ihr Profil und Ihren Lebensstil zu definieren. Die Wahl des richtigen Betriebssystems ist der erste Schritt zur Stärkung Ihrer Online-Privatsphäre. In diesem Tutorial werfen wir einen Blick auf PureOS, eine Linux-Distribution, die auf Datenschutz ausgerichtet ist.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Erste Schritte mit PureOS



PureOS ist ein Debian-basiertes Betriebssystem, das von Purism entwickelt wurde. PureOS ist sowohl für IT-Profis als auch für Benutzer geeignet, die eine einfache, leicht zu bedienende Distribution suchen. Es ist einzigartig, weil es *Freie Software* ist und sich auf den Schutz der persönlichen Daten seiner Nutzer konzentriert, indem es einen Rahmen schafft, der auf der von Debian angebotenen Privatsphäre, Freiheit, Sicherheit und Stabilität basiert.



### Warum PureOS wählen?





- Einfaches, intuitives Interface**: GNOME bietet einen übersichtlichen Interface-Desktop, der so gestaltet ist, dass er auch für Personen, die mit der Kommandozeile nicht vertraut sind, einfach zu bedienen ist.





- Kostenlos**: Wie die meisten Linux-Distributionen ist auch PureOS völlig kostenlos. Allerdings ist ein monatliches Abonnement erhältlich, um Entwickler zu unterstützen.





- Sicherheit und Stabilität**: Die Architektur und der Betriebsmodus von PureOS machen es zu einer äußerst sicheren Distribution, die Datenschutz und Systemstabilität garantiert.





- Dokumentation und aktive Gemeinschaft**: PureOS verfügt über eine übersichtliche, leicht zugängliche Dokumentation und eine engagierte, reaktionsfreudige Community, die es einfach macht, Probleme zu lösen und das System Schritt für Schritt zu erlernen.



## Installation und Konfiguration



Für die Installation und Konfiguration von PureOS auf Ihrem Computer benötigen Sie die folgenden minimalistischen Funktionen:




- Ein USB-Stick mit mindestens 8 GB zum Flashen des Systems.
- 4 GB RAM.
- 30 GB freier Speicherplatz auf Ihrer Hard-Festplatte.



Rufen Sie die [offizielle PureOS-Website] (https://pureos.net/) auf und laden Sie das ISO-Image des Betriebssystems entsprechend der Architektur Ihres Computers herunter.



Um die PureOS-Installation zu starten, müssen Sie einen bootfähigen USB-Stick mit einer Flash-Software wie [Balena Etcher] (https://www.balena.io/etcher) erstellen.



In drei einfachen Schritten können Sie einen USB-Stick mit dem PureOS-Betriebssystem booten.





- Stecken Sie den USB-Stick ein und starten Sie die heruntergeladene Balena-Software.
- Wählen Sie dann das PureOS-ISO-Image
- Wählen Sie den USB-Stick als Ausgabegerät, klicken Sie dann auf die Schaltfläche **Flash** und warten Sie, bis der Vorgang abgeschlossen ist.



![0_01](assets/fr/01.webp)



Sobald der USB-Stick gebootet wurde, starten Sie den Computer neu, auf dem Sie PureOS installieren möchten.



Rufen Sie beim Booten das BIOS auf, indem Sie die Taste "ESC", "F9" oder "F11" drücken, je nach Gerät. Wählen Sie den USB-Stick als Boot-Gerät aus und drücken Sie zur Bestätigung die Taste "ENTER".



### Startbildschirm



PureOS bietet mehrere Optionen zum Starten des Betriebssystems. Wählen Sie die Option **Test oder PureOS installieren**, um die Installation des Betriebssystems zu starten.



![0_02](assets/fr/02.webp)



Stellen Sie die Sprache und das Tastaturlayout ein, die Sie auf Ihrem Computer verwenden möchten.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Erlauben oder verweigern Sie Anwendungen den Zugriff auf Ihren **geografischen Standort**, um personalisierte Empfehlungen für Ihr Gebiet zu erhalten.



![0_05](assets/fr/05.webp)



Sie können eine Verbindung zu Ihrem bestehenden **NextCloud**-Konto herstellen, um Daten abzurufen, die mit der Office-Suite verknüpft sind, die Sie auf einem anderen System verwenden.



![0_06](assets/fr/06.webp)



Es gibt eine Anleitung, aber Sie können das Fenster schließen, wenn Sie diesen Schritt überspringen möchten.



![0_08](assets/fr/08.webp)



### Starten der Installation



Klicken Sie auf das Menü **Aktivitäten** und erkunden Sie die Anwendungen und Tools, die auf dem System vorinstalliert sind. Klicken Sie auf **Install PureOS**, um die Installation zu starten



![0_09](assets/fr/09.webp)



Stellen Sie die Systemsprache und das Tastaturlayout wie gewünscht ein und konfigurieren Sie dann den Hard-Festplattenpartitionierungsmodus.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Sie haben zwei Möglichkeiten, Ihre Hard-Festplatte zu partitionieren:




- Diskette löschen**: Für eine vollständige Installation von PureOS, wobei alle bereits vorhandenen Daten auf der Hard-Platte gelöscht werden.



![0_14](assets/fr/14.webp)





- Manuelle Partitionierung** zur Erstellung eigener Partituren



⚠️ Wenn Sie manuell Partitionen für Ihr Betriebssystem erstellen, stellen Sie sicher, dass Sie eine mindestens 2 GB große Partition für den PureOS-Betrieb und eine weitere Partition für Daten zuweisen.



![0_15](assets/fr/15.webp)



Aktivieren Sie die **Festplattenverschlüsselung**, wenn Sie Ihre Daten schützen wollen. Geben Sie ein starkes, komplexes Passwort ein.



Verknüpfen Sie einen Benutzer mit Ihrem Betriebssystem, indem Sie einen Benutzernamen und ein alphanumerisches Passwort mit mindestens 20 Zeichen festlegen, um die Sicherheit Ihrer Daten zu erhöhen.



![0_16](assets/fr/16.webp)



Überprüfen Sie die von Ihnen vorgenommenen Einstellungen und ändern Sie sie bei Bedarf.



![0_17](assets/fr/17.webp)



Klicken Sie auf **Installieren** und dann auf **Jetzt installieren**, um zu bestätigen, dass PureOS auf Ihrem Computer installiert wurde.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Wenn die Installation abgeschlossen ist, aktivieren Sie das Kontrollkästchen **Jetzt neu starten**, um den Computer neu zu starten, und bestätigen Sie dann:




- Die Sprache.
- Tastaturlayout.
- Ihr NextCloud-Konto (optional).



![0_25](assets/fr/25.webp)



## Aktualisierungen



Bevor Sie PureOS verwenden, sollten Sie Ihr System unbedingt aktualisieren. So können Sie von den neuesten Funktionen und Sicherheitspatches profitieren und eine höhere Stabilität gewährleisten.





- Aktualisierung über Interface-Grafik**:


Öffnen Sie die Anwendung **Software**, und wechseln Sie dann zur Registerkarte **Updates**. Verfügbare Updates werden automatisch angezeigt. Klicken Sie auf **Herunterladen** und dann auf **Installieren**, sobald der Download abgeschlossen ist.





- Aktualisierung über Terminal**:


Öffnen Sie das Terminal und geben Sie den folgenden Befehl ein, um die Liste der verfügbaren Pakete zu aktualisieren:



```shell
sudo apt update
```



Geben Sie Ihr Passwort ein und bestätigen Sie es. Installieren Sie dann die Updates mit:



```shell
sudo apt full-upgrade
```



## PureOS für die Entwicklung



Standardmäßig enthält PureOS nicht alle für die Entwicklung erforderlichen Tools.


Sie können sie mit dem folgenden Befehl schnell installieren:



```shell
sudo apt install build-essential git curl
```



Dies installiert die Kompilierwerkzeuge **Git** und **Curl**, die in den meisten Entwicklungsumgebungen nützlich sind.



## PureOS-Umgebung



PureOS zeichnet sich durch seinen innovativen Ansatz für echte Konvergenz aus: Ein einziges Betriebssystem sorgt für einen reibungslosen, nahtlosen Betrieb auf einer Vielzahl von Geräten, einschließlich Laptops, Tablets, Mini-PCs und Smartphones.



PureOS-Anwendungen sind so konzipiert, dass sie adaptiv sind: Sie passen sich automatisch an die Bildschirmgröße und den Eingabemodus (Touch oder Tastatur/Maus) an. Beispielsweise passt der GNOME-Webbrowser seinen Interface dynamisch an, um sowohl auf mobilen als auch auf Desktop-Geräten ein optimales Erlebnis zu bieten.



PureOS enthält auch die **LibreOffice** Office-Suite, die:





- Writer**: ein komplettes Textverarbeitungsprogramm zum Erstellen und Bearbeiten von Dokumenten.
- Calc**: ein leistungsstarkes Tabellenkalkulationsprogramm zur Verwaltung Ihrer Daten und Berechnungen.
- Impress**: ein Werkzeug zur Erstellung professioneller Präsentationen.



Mit dieser kostenlosen Suite können Sie effizient arbeiten, ohne auf proprietäre Software angewiesen zu sein.



PureOS bietet eine einheitliche, sichere und flexible Umgebung, die auf einer 100%igen Open-Source-Distribution basiert, die eine vollständige Kontrolle und die strikte Wahrung der Privatsphäre garantiert. Seine echte Konvergenz erleichtert die Erstellung von Anwendungen, die mit verschiedenen Gerätetypen, wie Computern, Tablets und Smartphones, kompatibel sind, ohne dass komplexe Anpassungen erforderlich sind.



Mit nativem Zugriff auf wichtige Tools, robusten Paketmanagern und einem reichhaltigen Open-Source-Ökosystem vereinfacht PureOS die Anwendungsentwicklung, das Testen und die Bereitstellung in einer sicheren Umgebung. Seine stabile Architektur und Commitment Vertraulichkeit machen es zu einer zuverlässigen Plattform für eine Vielzahl von Anwendungen, einschließlich Blockchain Entwicklung, Rapid Prototyping oder Produktionsumgebungen.



Entdecken Sie unseren Kurs zur Stärkung Ihrer Sicherheit und zum Schutz Ihrer digitalen Privatsphäre.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1