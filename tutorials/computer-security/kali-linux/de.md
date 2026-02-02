---
name: Kali
description: Installation von Kali Linux auf VirtualBox, als bootfähiger USB-Stick oder als Dual-Boot, Schritt für Schritt.
---

![cover-kali](assets/cover.webp)



## Einführung



### Warum Kali Linux?



**Kali Linux** ist eine auf IT-Sicherheit spezialisierte Linux-Distribution.


Hier ist der Grund, warum wir Kali Linux verwenden:





- Es ist mit einer breiten Palette von Pentesting-Tools (System- und Netzwerksicherheitstests) vorkonfiguriert.
- Es ist **quelloffen und frei**, Sie können es also frei verwenden und verändern.
- Es ist **zuverlässig und sicher**, ideal um etwas über Cybersicherheit zu lernen.
- Es ermöglicht Ihnen, den Umgang mit Linux in einer testbereiten Umgebung zu erlernen.
- Es kann auf verschiedene Arten installiert werden: **VirtualBox**, **bootfähiger USB-Stick**, oder **dual boot**.



## Installation und Konfiguration



### 1. Voraussetzungen



**Erforderliche Ausrüstung:**





- 64-Bit-Prozessor** (Intel oder AMD).
- mindestens 8 GB RAM** (4 GB können für eine einfache Installation oder VM ausreichend sein).
- 50 GB freier Festplattenplatz** für die Installation von Kali Linux.
- Internetverbindung** zum Herunterladen des ISO-Images und der Updates.
- Einen USB-Stick** mit mindestens 8 GB, um bootfähige Medien zu erstellen (wenn Sie Kali auf einem PC installieren oder auf einem Live-USB testen möchten).



Es ist wichtig, dass Sie Ihre Daten vor der Installation auf einem vorhandenen PC sichern.



### 2. Herunterladen





- Gehen Sie zu [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Wählen Sie das ISO-Image für Ihre Anwendung aus:
  - Install Image** : für die PC-Installation.
  - Virtuelles Image**: zur Installation von Kali auf VirtualBox oder VMware.
- Laden Sie das ISO-Image herunter.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Einen bootfähigen USB-Stick erstellen



Sie können verschiedene Tools verwenden, wie z. B. Balena Etcher :





- Laden Sie [Balena Etcher](https://etcher.balena.io/) herunter und installieren Sie es.



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Öffnen Sie Balena Etcher und wählen Sie dann das Kali-ISO-Image aus.
- Wählen Sie einen USB-Stick als Zielmedium.
- Klicken Sie auf Flash und warten Sie, bis der Vorgang abgeschlossen ist.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Installation und Sicherung von Kali Linux



#### 4.1 Booten mit dem USB-Stick





- Schalten Sie den Computer aus.
- Stecken Sie den USB-Stick (mit Kali Linux) ein.
- Schalten Sie Ihren Computer ein. Bei neueren PCs sollte das System den USB-Startschlüssel automatisch erkennen. Ist dies nicht der Fall, starten Sie den Computer neu, indem Sie die BIOS/UEFI-Zugriffstaste (je nach Hersteller normalerweise F2, F12 oder Entf) gedrückt halten.
  - Wählen Sie im BIOS/UEFI-Menü Ihren USB-Stick als Boot-Gerät aus.
  - Speichern und neu starten.



#### 4.2 Starten der Installation



##### Startbildschirm



Wenn Sie vom USB-Stick booten, sollte der Kali Linux-Bootbildschirm erscheinen. Wählen Sie zwischen **grafischer Installation** und **Textinstallation**. In diesem Beispiel haben wir uns für die grafische Installation entschieden.



![capture](assets/fr/06.webp)



Wenn Sie das **Live**-Image verwenden, sehen Sie einen weiteren Modus, **Live**, der auch die Standard-Startoption ist.



![Mode Live](assets/fr/07.webp)



##### Auswahl der Sprache



Wählen Sie Ihre bevorzugte Sprache für die Installation und das System.



![Sélection de la langue](assets/fr/08.webp)



Bitte geben Sie Ihren geografischen Standort an.



![Options d'accessibilité](assets/fr/09.webp)



##### Konfiguration der Tastatur



Wählen Sie Ihr Tastaturlayout. Es gibt ein Testfeld, mit dem Sie überprüfen können, ob die Tasten mit Ihrer Konfiguration übereinstimmen.



![Configuration du clavier](assets/fr/10.webp)



##### Netzwerkverbindung



Die Installation scannt nun Ihre Netzwerkschnittstellen, sucht nach einem DHCP-Dienst und fordert Sie dann auf, einen Hostnamen für Ihr System einzugeben. Im folgenden Beispiel haben wir **"kali "** als Host-Namen eingegeben.



![Configuration réseau](assets/fr/11.webp)



Sie können optional einen Standard-Domänennamen angeben, den dieses System verwenden wird (Werte können von DHCP abgerufen werden oder wenn ein bereits vorhandenes Betriebssystem existiert).



![Choix du type d'installation](assets/fr/12.webp)



##### Benutzerkonten



Als Nächstes erstellen Sie das Benutzerkonto für das System (vollständiger Name, Benutzername und ein sicheres Passwort).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Zeitzone



Wählen Sie Ihr geografisches Gebiet, um die Systemzeit einzustellen.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Art der Unterteilung



Das Installationsprogramm durchsucht dann Ihre Festplatten und zeigt je nach Ihrer Konfiguration verschiedene Optionen an.



In dieser Anleitung gehen wir von einer **leeren Diskette** aus, so dass **vier Möglichkeiten** zur Auswahl stehen.


Wir wählen **Geführt - gesamte Festplatte verwenden**, da wir hier eine einmalige Installation von Kali Linux (Single Boot) durchführen. Dies bedeutet, dass kein anderes Betriebssystem beibehalten wird und die gesamte Festplatte gelöscht werden kann.



Wenn Ihre Festplatte bereits Daten enthält, wird möglicherweise eine zusätzliche Option **Geführt - größten zusammenhängenden freien Speicherplatz verwenden** angezeigt.



Diese Alternative ermöglicht es Ihnen, Kali Linux zu installieren, ohne vorhandene Daten zu löschen, und ist somit ideal für ein Dual-Boot mit einem anderen System.



In unserem Fall ist die Festplatte leer, so dass diese Option nicht erscheint.



![Choix du partitionnement](assets/fr/17.webp)



Wählen Sie die zu partitionierende Festplatte aus.



![capture](assets/fr/18.webp)



Je nach Bedarf können Sie alle Dateien in einer einzigen Partition speichern (Standardverhalten) oder separate Partitionen für ein oder mehrere Verzeichnisse der obersten Ebene einrichten.



Wenn Sie sich nicht sicher sind, was Sie wollen, wählen Sie die Option **Alle Dateien in einer einzigen Partition**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Sie haben dann eine letzte Gelegenheit, Ihre Festplattenkonfiguration zu überprüfen, bevor das Installationsprogramm unwiderrufliche Änderungen vornimmt. Sobald Sie auf _Fortfahren_ geklickt haben, wird das Installationsprogramm gestartet und die Installation ist fast abgeschlossen.



![capture](assets/fr/21.webp)



##### Verschlüsselter LVM



Wenn diese Option im vorherigen Schritt aktiviert wurde, führt Kali Linux nun ein sicheres Löschen der Festplatte durch, bevor es Sie nach einem LVM-Passwort fragt.



Bitte verwenden Sie ein sicheres Passwort, da sonst eine Warnung über ein schwaches passphrase angezeigt wird.



##### Informationen zur Vollmacht



Kali Linux verwendet Repositories, um Anwendungen zu verteilen. Sie müssen die erforderlichen Proxy-Informationen eingeben, wenn Ihre Umgebung einen solchen verwendet.



Wenn Sie **nicht sicher** sind, ob Sie einen Proxy verwenden sollen, **leerlassen**. Die Eingabe falscher Informationen verhindert die Verbindung zu den Repositories.



![capture](assets/fr/22.webp)



##### Metapete



Wenn der Netzwerkzugang nicht konfiguriert wurde, müssen Sie nach Aufforderung eine **Weitere Konfiguration** vornehmen.



Wenn Sie das **Live**-Bild verwenden, wird der nächste Schritt nicht angezeigt.



Sie können dann die [Metapakete](https://www.kali.org/docs/general-use/metapackages/) auswählen, die Sie installieren möchten. Mit den Standardoptionen wird ein Standard-Kali-Linux-System installiert, so dass Sie nichts ändern müssen.



![capture](assets/fr/23.webp)



#### Informationen zur Inbetriebnahme



Bestätigen Sie dann die Installation des GRUB-Bootloaders.



![capture](assets/fr/24.webp)



##### Neustart



Klicken Sie abschließend auf Weiter, um Ihre neue Kali Linux-Installation neu zu starten.



![capture](assets/fr/25.webp)



#### 4.3 Aktualisieren und Konfigurieren von Kali Linux nach der Installation



Die Aktualisierung Ihres Systems ist ein wichtiger Schritt nach einer Neuinstallation. Sie haben zwei Möglichkeiten:



##### Option 1: Über die grafische Benutzeroberfläche (GUI)



Kali bietet, wie Debian/Ubuntu, einen integrierten grafischen Update-Manager.



1. Klicken Sie auf das **Hauptmenü** (oben links oder unten, je nach Desktop).


2. Öffnen Sie **"Software Updater "**.


3. Das Werkzeug wird :




    - Überprüfen Sie die zu aktualisierenden Pakete.
    - Sie erhalten eine Liste (mit Größen und Versionen).
    - Ermöglicht es Ihnen, die Aktualisierung mit einem einzigen Klick zu starten.


4. Geben Sie Ihr Administrator-Passwort (`sudo`) ein, wenn Sie dazu aufgefordert werden.


5. Lassen Sie es installieren und starten Sie es gegebenenfalls neu.



##### Option 2: Über das Terminal



Öffnen Sie ein Terminal und führen Sie :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Es ist nicht ratsam, das **root**-Konto für die tägliche Arbeit zu verwenden; erstellen Sie stattdessen einen Nicht-Root-Benutzer.



Geben Sie in Ihrem Terminal die folgenden Befehle ein:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Melden Sie sich ab und melden Sie sich mit dem neuen Benutzer wieder an.



Lassen Sie uns einige grundlegende Kali Linux-Aufgaben in einer Tabelle zusammenfassen.



### Grundlegende Aufgaben unter Kali Linux




| **Kategorie** | **Basisaufgabe** | **Beschreibung / Ziel** | **Hauptmethode** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Systemnavigation** | Terminal öffnen | Zugriff auf die Hauptbefehlszeile von Kali | Klicken Sie auf das Terminal-Symbol oder nutzen Sie `Ctrl + Alt + T` |
| | Ordner durchsuchen | Navigieren in der Systemstruktur | `cd /pfad/zum/ordner`, `ls` zum Auflisten von Dateien |
| | Ordner erstellen / löschen | Dateien organisieren | `mkdir ordnername`, `rm -r ordnername` |
| **Dateiverwaltung** | Datei kopieren / verschieben | Dateien im Terminal manipulieren | `cp datei ziel`, `mv datei ziel` |
| | Datei löschen | Festplattenspeicher freigeben | `rm dateiname` |
| | Inhalt einer Textdatei anzeigen | Eine Datei schnell lesen | `cat datei.txt`, `less datei.txt` |
| **Systemverwaltung** | Kali Linux aktualisieren | Installieren der neuesten Versionen und Sicherheitspatches | `sudo apt update && sudo apt full-upgrade -y` |
| | Software installieren | Ein neues Tool oder Dienstprogramm hinzufügen | `sudo apt install paketname` |
| | Software löschen | Das System bereinigen | `sudo apt remove paketname` |
| | Unnötige Abhängigkeiten entfernen | Festplattenspeicher gewinnen | `sudo apt autoremove` |
| **Netzwerk und Internet** | Netzwerkverbindung prüfen | Den Internetzugang testen | `ping google.com` |
| | IP-Adresse identifizieren | Die Netzwerkkonfiguration kennen | `ip a` oder `ifconfig` |
| | Wi-Fi-Netzwerk wechseln | Verbindung zu einem anderen Zugangspunkt herstellen | Netzwerksymbol → Gewünschtes Wi-Fi auswählen |
| **Konten und Berechtigungen** | Administratorbefehl ausführen | Vorübergehend Root-Rechte erhalten | `sudo befehl` |
| | Neuen Benutzer erstellen | Ein lokales Konto hinzufügen | `sudo adduser benutzername` |
| | Passwort ändern | Ein Konto sichern | `passwd` |
| **Aussehen und Komfort** | Hintergrundbild ändern | Den Desktop personalisieren | Rechtsklick auf den Desktop → **Schreibtischeinstellungen** |
| | Design / Icons ändern | Lesbarkeit und Ästhetik verbessern | Einstellungen → Erscheinungsbild / Designs |
| **Kali-Tools** | Tool-Menü öffnen | Test- und Sicherheits-Tools erkunden | Menü **Anwendungen → Kali Linux** |
| | Ein Tool starten (z.B. nmap, wireshark) | Praktische Entdeckung von Sicherheits-Utilities | `sudo nmap`, `wireshark`, etc. |
| **Hilfe und Dokumentation** | Hilfe zu einem Befehl erhalten | Einen Befehl vor der Verwendung verstehen | `man befehl` oder `befehl --help` |

## Schlussfolgerung



Die Installation von Kali Linux ist nur der erste Schritt, um diese leistungsstarke Umgebung für die Cybersicherheit zu entdecken. Durch die Beherrschung grundlegender Aufgaben und der Systemverwaltung kann jeder damit beginnen, die eingebauten Tools zu erforschen und die innere Funktionsweise eines Linux-Systems zu verstehen. Kali bietet eine hervorragende Lernplattform, sowohl für die Stärkung der technischen Fähigkeiten als auch für die Entwicklung einer echten Kultur der IT-Sicherheit.