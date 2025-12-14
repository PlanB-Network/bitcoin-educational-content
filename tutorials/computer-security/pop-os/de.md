---
name: Pop!_OS
description: Anleitung zur Installation von Pop!_OS, einer Linux-Distribution
---

![cover](assets/cover.webp)



## Einführung



Pop!OS ist ein Linux-basiertes Betriebssystem, das von **System76** entwickelt wurde, einem amerikanischen Hersteller, der sich auf Maschinen für Entwickler, Designer und fortgeschrittene Benutzer spezialisiert hat.



Pop!OS wurde entwickelt, um eine moderne, stabile und leistungsstarke Umgebung zu bieten und zeichnet sich durch eine einfache Bedienung, leistungsstarke Tools und einen starken Fokus auf Produktivität aus.



### Wer ist System76?



System76 ist ein 2005 gegründetes amerikanisches Unternehmen mit Sitz in Denver, das sich auf die Herstellung von Notebooks, Desktops und Servern spezialisiert hat, die speziell für Linux entwickelt wurden.



Im Gegensatz zu traditionellen Herstellern entwickelt System76 Maschinen, die offen, reparierbar und auf Softwarefreiheit ausgerichtet sind.



System76 stellt nicht nur Computer her.



Das Unternehmen entwickelt auch :




- Pop!OS**, sein eigenes Linux-basiertes Betriebssystem;
- COSMIC**, die moderne, leistungsstarke Desktop-Umgebung, die von Pop!OS ;
- Open Firmware**, eine Open-Source-Firmware, die auf Coreboot basiert;
- werkzeuge für Entwickler und Designer.



Ziel ist es, eine hochwertige Hardware- und Software-Integration zu bieten, die mit dem Apple-Ökosystem vergleichbar ist, aber völlig offen und auf Linux basiert.



## Ein modernes, stabiles und zugängliches System



Pop!OS baut auf den Grundlagen von Ubuntu auf und bietet hervorragende Stabilität, breite Hardwarekompatibilität und Zugang zu einem umfangreichen Software-Ökosystem.


Es bietet eine elegante Oberfläche, den COSMIC-Desktop, der so gestaltet ist, dass er auch für neue Benutzer flüssig, intuitiv und anpassbar ist.



## Eine ideale Wahl für Entwickler, Designer und anspruchsvolle Anwender



Pop!OS wird besonders geschätzt von :





- entwickler (vorinstallierte Werkzeuge, erweiterte Kachelverwaltung),
- benutzer mit Nvidia- oder AMD-Grafikkarten,
- studenten und Berufstätige, die ein zuverlässiges System suchen,
- windows-Benutzer, die eine einfache Umstellung vornehmen möchten.



Es umfasst automatische Kacheln, ein übersichtliches Software-Center und integrierte Produktivitätswerkzeuge, die die tägliche Arbeit erleichtern.



## Pop!OS Höhepunkte





- Optimierte Leistung** dank regelmäßiger Updates.
- Zwei ISO-Versionen verfügbar**: Standard und Nvidia-optimiert.
- Erhöhte Sicherheit** (LUKS-Verschlüsselung bei der Installation verfügbar).
- Interface COSMIC** ergonomisch und modern.
- Hohe Kompatibilität** mit Ubuntu und Flatpak-Software.



## POP!OS sicher herunterladen



### 1. Voraussetzungen



Bevor Sie POP!OS herunterladen und installieren, müssen Sie einige Dinge tun, um die Installationsumgebung korrekt vorzubereiten.



### Erforderliche Ausrüstung





- Ein kompatibler Computer**: Intel- oder AMD-Prozessor, Intel- / AMD- / Nvidia-GPU.
- Mindestens 4 GB RAM** (8 GB für eine komfortable Nutzung empfohlen).
- mindestens 20 GB freier Speicherplatz** (40 GB oder mehr empfohlen).
- Ein USB-Stick** mit mindestens 4 GB, um das Installationsmedium zu erstellen.



### Internetverbindung



Eine stabile Verbindung ist nützlich für :





- laden Sie das ISO-Image herunter,
- updates nach der Installation installieren.



Pop!OS kann auch ohne eine Verbindung laufen, aber die Installation ist über das Internet viel reibungsloser.



### Datensicherung



Wenn Pop!OS ein anderes System (Windows, Ubuntu, etc.) ersetzen oder neben diesem bestehen soll, ist es ratsam, wichtige Dateien zu sichern, bevor Sie fortfahren.



### Prüfen Sie, ob ein Nvidia-Grafikprozessor vorhanden ist (falls zutreffend)



Für Computer, die mit einer Nvidia-Grafikkarte ausgestattet sind, müssen Sie das spezielle ISO-Image herunterladen, das die Nvidia-Treiber enthält.


Diese Prüfung ist sehr einfach:





- indem Sie die PC-Spezifikationen konsultieren,
- oder indem Sie das Grafikkartenmodell in den Systemeinstellungen nachschlagen.



### Download von der offiziellen Website



Das Pop!OS ISO-Image sollte direkt von der offiziellen System76-Seite heruntergeladen werden: [system76.com/pop](https://system76.com/pop/).



Auf dieser Seite finden Sie immer die aktuellste Version, angepasst an Ihre Hardware.



![capture](assets/fr/03.webp)



### Version wählen: Standard oder Nvidia, oder Raspberry Pi (ARM64)



Pop!OS ist in drei Varianten erhältlich:



### Standardausführung



Empfohlen für Computer mit :





- intel- oder AMD-Prozessor;
- einen integrierten Intel- oder AMD-Grafikprozessor;
- eine AMD Radeon-Grafikkarte.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia-Version



Empfohlen für Computer, die mit Nvidia-Grafikkarten ausgestattet sind.


Dieses Image enthält bereits Nvidia-Treiber, was die Installation erleichtert und Grafikprobleme reduziert.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Raspberry Pi-Version (ARM64)



Für Raspberry Pi 4 und 400 (ARM-Prozessor).


Dies ist eine spezielle Version für diese Mini-Computer, die an die ARM-Architektur angepasst ist.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Einen bootfähigen USB-Stick erstellen



Sie können verschiedene Tools verwenden, wie z. B. Balena Etcher :





- Laden Sie [Balena Etcher] (https://etcher.balena.io/) herunter und installieren Sie es.



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Öffnen Sie den Balena Etcher und wählen Sie das Pop!OS ISO-Image aus.
- Wählen Sie einen USB-Stick als Zielmedium.
- Klicken Sie auf Flash und warten Sie, bis der Vorgang abgeschlossen ist.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Installation und Sicherung von Pop!OS



### Booten vom USB-Stick





- Schalten Sie den Computer aus.
- Stecken Sie den USB-Stick (mit Pop!OS) ein.
- Schalten Sie Ihren Computer ein. Bei neueren PCs sollte das System den USB-Startschlüssel automatisch erkennen. Ist dies nicht der Fall, starten Sie den Computer neu, indem Sie die BIOS/UEFI-Zugriffstaste (je nach Hersteller normalerweise F2, F12 oder Entf) gedrückt halten.
  - Wählen Sie im BIOS/UEFI-Menü Ihren USB-Stick als Boot-Gerät aus.
  - Speichern und neu starten.



### Starten der Installation



Sobald Sie Ihren bootfähigen USB-Stick als Startgerät ausgewählt haben, startet Ihr Computer in einer Pop!OS Live-Umgebung.



Wählen Sie Ihre Sprache.



![Capture](assets/fr/10.webp)



Wählen Sie einen Ort.



![Capture](assets/fr/11.webp)



Wählen Sie eine Sprache für die Tastatureingabe.



![Capture](assets/fr/12.webp)



Wählen Sie ein Tastaturlayout.



![Capture](assets/fr/13.webp)



Wählen Sie die Option "Saubere Installation" für eine Standardinstallation. Dies ist die beste Option für neue Linux-Benutzer, aber beachten Sie, dass dabei der gesamte Inhalt des Ziellaufwerks gelöscht wird. Alternativ können Sie die Option "Demo-Modus" wählen, um Pop!OS in der Live-Umgebung weiter zu testen.



![Capture](assets/fr/14.webp)



Wählen Sie "Benutzerdefiniert (Erweitert)", um GParted aufzurufen. Mit diesem Tool können Sie erweiterte Funktionen konfigurieren, wie z. B. duales Booten, Erstellen einer separaten `/home`-Partition oder Platzieren der `/tmp`-Partition auf einem anderen Laufwerk.



Klicken Sie auf "Löschen und Installieren", um Pop!OS auf dem ausgewählten Laufwerk zu installieren.



![Capture](assets/fr/15.webp)



### Konfiguration des Benutzerkontos



Der nächste Abschnitt des Installationsprogramms führt Sie durch die Erstellung eines Benutzerkontos, damit Sie sich bei Ihrem neuen Betriebssystem anmelden können.



Geben Sie einen vollständigen Namen (mit beliebigem Text in Groß- oder Kleinbuchstaben) sowie einen Benutzernamen (in Kleinbuchstaben) an:



![Capture](assets/fr/16.webp)



Sobald das Konto erstellt wurde, werden Sie aufgefordert, ein neues Passwort festzulegen.



![Capture](assets/fr/17.webp)



### Vollständige Festplattenverschlüsselung



Die Verschlüsselung der Systemfestplatte ist nicht notwendig, aber sie garantiert die Sicherheit der Benutzerdaten für den Fall, dass sich jemand unbefugten physischen Zugang zum Gerät verschafft.



Das Laufwerk kann mit Ihrem Anmeldekennwort verschlüsselt werden, indem Sie das Kontrollkästchen "Verschlüsselungskennwort ist dasselbe wie das Kennwort des Benutzerkontos" aktivieren. Sie können dieses Kontrollkästchen auch deaktivieren und unten "Kennwort festlegen" wählen. Wählen Sie "Nicht verschlüsseln", um den Verschlüsselungsprozess zu ignorieren.



![Capture](assets/fr/18.webp)



Wenn Sie die Schaltfläche "Kennwort festlegen" gewählt haben, erscheint eine zusätzliche Aufforderung, Ihr Verschlüsselungskennwort festzulegen.



Fahren Sie mit dem nächsten Schritt des Installationsprogramms fort. Pop!OS beginnt nun mit der Installation auf der Festplatte.



![Capture](assets/fr/19.webp)



Starten Sie nach Abschluss der Installation Ihren Computer neu und melden Sie sich an, um die Konfiguration des Benutzerkontos abzuschließen.



Wenn Sie die Boot-Reihenfolge so geändert haben, dass Ihr Live-USB-Stick beim Starten Vorrang hat, schalten Sie den Computer vollständig aus und entfernen Sie den Installations-USB-Stick. Wenn Sie sich im Dual-Boot-Modus befinden, drücken Sie die entsprechenden Tasten, um die Konfiguration aufzurufen und das Laufwerk mit der Pop!OS-Installation auszuwählen.



![Capture](assets/fr/20.webp)



### NVIDIA-Grafiken



Wenn Sie von der Intel/AMD-ISO installiert haben und Ihr System über eine diskrete NVIDIA-Grafikkarte verfügt, oder wenn Sie eine solche zu einem späteren Zeitpunkt hinzugefügt haben, müssen Sie die Treiber für Ihre Karte manuell installieren, um eine optimale Leistung zu erzielen. Führen Sie den folgenden Befehl in einem Befehlsterminal aus, um den Treiber zu installieren:



```bash
sudo apt install system76-driver-nvidia
```



Sie können auch NVIDIA-Grafiktreiber aus dem Pop!_Shop installieren.



![Capture](assets/fr/20.webp)



## Installation der wichtigsten Werkzeuge



Pop!OS bietet über seinen Pop!Shop eine breite Palette von Software an, aber viele wichtige Tools können auch über das Terminal mit `apt` oder `flatpak` installiert werden. Hier erfahren Sie, wie Sie die wichtigsten Tools für eine vollständige Arbeitsumgebung installieren.



### Installation des Terminals



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### Installation über Pop! Shop (grafische Schnittstelle)





- Öffnen Sie **Pop!_Shop** über das Hauptmenü.
- Verwenden Sie die Suchleiste, um die gewünschten Anwendungen zu finden (z. B. "Brave").
- Klicken Sie für jede Anwendung auf **Installieren**.
- Pop!_Shop verwaltet automatisch Abhängigkeiten und Updates.



## Aktualisierung des Systems



### Option 1: Über die grafische Benutzeroberfläche (GUI)



Pop!OS verfügt über einen einfachen, intuitiven grafischen Update-Manager.



1. Klicken Sie auf das **Hauptmenü** (Symbol unten links).


2. Öffnen Sie **"Pop!_Shop "**.


3. Klicken Sie im Pop!_Shop auf die Registerkarte **"Updates "**.


4. Das System sucht automatisch nach verfügbaren Updates.


5. Klicken Sie auf **"Alle aktualisieren "**, um die Installation der Updates zu starten.


6. Geben Sie Ihr Passwort ein, wenn Sie dazu aufgefordert werden.


7. Lassen Sie den Vorgang abschließen und starten Sie ihn gegebenenfalls neu.



### Option 2: Über das Terminal



Öffnen Sie ein Terminal und geben Sie :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Benutzerverwaltung



Wir empfehlen, für den täglichen Betrieb ein Standard-Benutzerkonto mit sudo-Rechten zu verwenden.



So erstellen Sie einen neuen Benutzer:



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Melden Sie sich ab und dann mit diesem neuen Benutzer wieder an.



### Verwaltung von Grafiktreibern





- Bei Nvidia-Karten sollten Sie überprüfen, ob die proprietären Treiber installiert sind:



```bash
sudo apt install system76-driver-nvidia
```





- Für AMD/Intel sind die Treiber in der Regel standardmäßig enthalten.



### Firewall aktivieren (UFW)



Pop!OS blockiert den Netzwerkverkehr standardmäßig nicht. Aktivieren Sie UFW, um die Sicherheit zu erhöhen:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Automatische Updates konfigurieren



Um das System ohne manuelle Eingriffe auf dem neuesten Stand zu halten:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Anpassen von Aussehen und Verhalten





- Öffnen Sie **Systemeinstellungen** → **Erscheinungsbild**, um ein helles oder dunkles Thema auszuwählen.
- Konfigurieren Sie aktive Ecken, Animationen und Erweiterungen über den COSMIC-Manager.
- Passen Sie das Desktop-Layout an, um Ihren Arbeitsablauf zu optimieren.



### Konfigurieren Sie die automatische Sicherung



Pop!OS integriert Tools wie Deja Dup für die Datensicherung:





- Starten Sie **Backup** über das Menü.
- Wählen Sie ein externes Laufwerk oder einen Speicherort im Netzwerk.
- Planen Sie regelmäßige Backups.



### Installation von nützlichen GNOME/COSMIC-Erweiterungen



Hier sind einige empfohlene Erweiterungen zur Verbesserung der Benutzerfreundlichkeit:





- Dash to Dock**: Anwendungsleiste immer sichtbar.
- GSConnect**: Synchronisierung mit Android.
- Zwischenablage-Indikator**: Erweiterte Verwaltung der Zwischenablage.



Installieren Sie sie über :



```bash
sudo apt install gnome-shell-extensions
```



Aktivieren Sie sie dann in den Einstellungen.



### Optimierung der Speicher- und Swap-Verwaltung



Überprüfen Sie Ihren Swap-Status:



```bash
swapon --show
```



Erhöhen Sie ggf. die Auslagerungsgröße oder konfigurieren Sie eine Auslagerungsdatei:



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Fügen Sie sie zur Datei `/etc/fstab` hinzu, damit sie automatisch eingehängt wird.



## Paket- und Repository-Verwaltung



### Verständnis der Paketquellen



Pop!OS, das auf Ubuntu basiert, verwendet hauptsächlich :





- Offizielle Ubuntu**-Repositorien: für die meiste stabile Software.
- System76**-Repositories: für Treiber, Firmware und spezielle Tools.
- Flatpak**: Zugriff auf eine breite Palette von Sandbox-Anwendungen.
- Snap** (optional): ein weiteres universelles Paketformat.



---

### Hinzufügen und Verwalten von PPA-Repositories



Um häufig aktualisierte Software zu installieren, können bestimmte PPAs (Personal Package Archives) hinzugefügt werden:



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Schlussfolgerung



Pop!OS ist eine moderne, stabile Linux-Distribution, die sowohl für Anfänger als auch für fortgeschrittene Benutzer geeignet ist.



Dank der intuitiven COSMIC-Benutzeroberfläche und der integrierten Tools bietet es ein flüssiges und produktives Erlebnis, sei es für die Entwicklung, die Erstellung oder den täglichen Gebrauch.



Dieses Tutorial behandelt die wichtigsten Schritte: Vorbereitung, Herunterladen, Installation, Ersteinstellungen und wichtige Tools.



Sie können Pop!OS gerne weiter erforschen und Ihre Umgebung anpassen, um das Beste daraus zu machen.