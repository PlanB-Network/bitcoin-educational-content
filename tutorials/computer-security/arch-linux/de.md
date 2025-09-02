---
name: Arch Linux
description: Minimalistische, leistungsstarke Distribution, die nach der KISS-Philosophie entwickelt wurde.
---

![cover](assets/cover.webp)



Arch Linux ist eine Distribution, die für ihre Robustheit, Leistung und Anpassungsfähigkeit bekannt ist, insbesondere für Entwicklungszwecke. Sie bietet eine ausgezeichnete Stabilität und eine Umgebung, die die Anpassung fördert, unterstützt durch einen extrem schnellen und zuverlässigen Paketmanager. Seine Philosophie basiert auf dem **KISS** (*Keep It Simple, Stupid*) Prinzip: eine leichte, einfache, schnelle und übersichtliche Distribution anzubieten, die dem Benutzer viel Freiheit lässt.



## Warum Arch Linux wählen?





- Frei und quelloffen**: Wie die meisten Linux-Distributionen ist auch Arch Linux völlig kostenlos. Es fallen keine Lizenzgebühren an, was es zu einer hervorragenden Wahl für Studenten, Freiberufler oder Enthusiasten macht.
- KISS**-Philosophie: Arch ist so konzipiert, dass es einfach, leicht und effizient ist. Es bietet nur das Wesentliche und ermöglicht es Ihnen, Ihre Umgebung à la carte zu gestalten.
- Pacman** Paketmanager: Pacman ist ein schneller, zuverlässiger und gut durchdachter Paketmanager. Er ermöglicht eine effiziente Installation und Aktualisierung von Software und verwaltet Abhängigkeiten mit Präzision.
- Umfassende Dokumentation und eine aktive Gemeinschaft**: Das [Arch Wiki] (https://wiki.archlinux.org) ist wahrscheinlich eine der besten technischen Dokumentationen in der Linux-Welt. Es ist eine Goldmine, um zu verstehen, was Sie tun. Die Gemeinschaft, die hauptsächlich aus erfahrenen Profilen besteht, ist sehr aktiv und kann Ihnen helfen, wenn Sie nicht weiterkommen, vorausgesetzt, Sie haben vorher ein wenig recherchiert.



## Installation und Konfiguration



### Voraussetzungen



Erforderliche Materialien:





- Ein USB-Stick mit mindestens **8 GB**
- mindestens 2 GB** RAM
- Ein Computer mit mindestens 20 GB freiem Speicherplatz



### Herunterladen



![0_1](assets/fr/01.webp)



Seit 2017 unterstützt Arch Linux keine 32-Bit-Architekturen mehr. Es sind nur noch 64-Bit-Versionen verfügbar.





- Besuchen Sie [die offizielle Website](https://mir.archlinux.fr/iso/latest/), um die neueste offizielle Version des ISO-Abbilds herunterzuladen.



### Einen bootfähigen Schlüssel erstellen



Um einen bootfähigen USB-Stick zu erstellen, können Sie ein Tool wie **Balena Etcher** verwenden:





- Laden Sie Balena Etcher von der [offiziellen Website](https://etcher.balena.io) herunter.
- Starten Sie die Software und wählen Sie das Arch Linux ISO-Image aus.
- Wählen Sie Ihren USB-Stick als Zielgerät.
- Klicken Sie auf **Flash**, um mit der Erstellung des bootfähigen Schlüssels zu beginnen.



![0_2](assets/fr/02.webp)



## Installation von Arch Linux



## Booten auf USB-Stick





- Schalten Sie Ihren Computer vollständig aus
- Stecken Sie den bootfähigen USB-Stick ein
- Starten Sie neu und rufen Sie BIOS/UEFI auf, indem Sie **F1**, **Escape**, **F9** usw. (je nach Modell) drücken
- Wählen Sie im Boot-Menü den USB-Stick als Boot-Gerät. Wenn alles korrekt eingerichtet ist, wird der Arch Linux Interface-Bootbildschirm angezeigt.



## Starten der Installation



Wählen Sie auf dem Startbildschirm die erste Option, um die Installation zu starten. Beachten Sie, dass Arch Linux kein grafisches Installationsprogramm anbietet. Nach dem Start werden Sie zu einem Terminal im Root-Modus weitergeleitet.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Konfiguration der Tastatur



Sie können die verfügbaren Layouts mit anzeigen:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Laden Sie dann ein Layout mit:



```shell
loadkeys nom-disposition
```



Standardmäßig ist die Tastatur in Englisch (qwerty), aber Sie können mit "loadkeys fr" auf "azerty" umschalten.



### Datum und Uhrzeit einstellen



Arch Linux verwendet das Werkzeug `timedatectl`, um die Systemuhr zu verwalten.



![0_7](assets/fr/07.webp)





- Stellen Sie Ihre Zeitzone mit ein:


```shell
timedatectl set-timezone Europe/Paris
```





- Vergewissern Sie sich, dass die automatische Synchronisierung mit aktiviert ist:


```shell
timedatectl status
```





- Aktivieren Sie es, falls erforderlich:


```shell
timedatectl set-ntp true
```




Damit wird NTP aktiviert, das Protokoll für die automatische Synchronisierung mit Zeitservern. Dieser Schritt ist wichtig, um Datumsfehler bei der späteren Installation von Paketen oder der Konfiguration von SSL-Zertifikaten zu vermeiden.



### Partitionierung der Festplatte





- Überprüfen Sie, ob Ihr System in **UEFI** oder **BIOS** mit:



```shell
ls /sys/firmware/efi
```



Wenn die Datei existiert, befinden Sie sich in **UEFI**. Andernfalls befinden Sie sich im **BIOS (Legacy)**.




- Liste der verfügbaren Festplatten:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Partition Manager starten:



```shell
cfdisk /dev/nom-du-disque
```



Wählen Sie **GPT**, wenn Sie sich in UEFI befinden, **DOS**, wenn Sie sich in BIOS befinden.



![0_9](assets/fr/09.webp)



#### Partituren zu erstellen




- Im UEFI**-Modus



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- Im BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Wählen Sie **Schreiben**, geben Sie **Ja** und dann **Beenden** ein.



### Partitionen formatieren





- UEFI**:



```shell
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dev/sda3
```





- BIOS**:



```shell
mkswap /dev/sda1
swapon /dev/sda1
mkfs.ext4 /dev/sda2
```



![0_11](assets/fr/11.webp)



### Grundlegende Systeminstallation



Hängen Sie die **Wurzelpartition** ein:





- Im BIOS:


```shell
mount /dev/sda2 /mnt
```




- unter UEFI:


```shell
mount /dev/sda3 /mnt
```



Installieren Sie dann die wichtigsten Pakete:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate die Datei **fstab**, die es dem Betriebssystem ermöglicht, das Einhängen von Partitionen bei jedem Start automatisch zu verwalten, ohne manuelles Eingreifen:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Geben Sie die **Chroot**-Umgebung ein:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Konfiguration des Systems





- Installieren Sie einen Texteditor zum Bearbeiten von:



```shell
pacman -S vim
```





- Stellen Sie die Sprache ein:


Bearbeiten Sie `/etc/locale.gen` und entfernen Sie die Markierung in der Zeile `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Legen Sie den Maschinennamen fest:



```shell
echo nom_machine > /etc/hostname
```





- Root-Passwort festlegen:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### GRUB-Installation



Installieren Sie die:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Nach dem Herunterladen müssen Sie es entsprechend dem Format der Festplattenpartition installieren.




- Für **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Für **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Fertigstellung





- Beenden Sie die Chroot-Umgebung:


```shell
exit
```





- Entfernen Sie die Partitionen:


```shell
umount -R /mnt
```





- Neustart:


```shell
reboot
```



Melden Sie sich beim Starten mit Ihrem **root**-Login und Passwort an.



![0_18](assets/fr/18.webp)


## Netzwerkverbindung nach Neustart



Es kann vorkommen, dass beim Neustart keine Netzwerkverbindung aktiv ist. Sie können die Schnittstellen mit auflisten:



```shell
ip link
```



Konfigurieren Sie dann das Interface-Netzwerk, indem Sie den folgenden Text in das Terminal eingeben



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface-Grafiken (GNOME)



Standardmäßig enthält **Arch Linux** keinen grafischen Interface. Um einen hinzuzufügen:



Aktualisieren Sie das System:



```shell
pacman -Syu
```



Installieren Sie **Xorg** mit dem folgenden Befehl und drücken Sie jedes Mal die Eingabetaste, um die Standardeinstellungen beizubehalten:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Installieren Sie **GNOME** mit dem folgenden Befehl und geben Sie jedes Mal ein, um die Standardeinstellungen beizubehalten:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Aktivieren Sie den **Sitzungsmanager**:



```shell
systemctl enable gdm
systemctl start gdm
```



Das System wird automatisch neu gestartet, und Sie erhalten die grafische Interface-Anmeldung. Melden Sie sich mit dem Root-Benutzernamen und dem Passwort an.



![0_21](assets/fr/21.webp)



## Erstellen eines Benutzers



Sobald Sie sich in **Interface GNOME** befinden, müssen Sie einen neuen Benutzer anlegen, um mehr Sicherheit und eine risikofreie Nutzung zu gewährleisten. Geben Sie Anwendungen ein und wählen Sie die Option "Konsole", um das Terminal zu starten.





- Einen Benutzer hinzufügen:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Installieren **sudo**:


```shell
pacman -S sudo
```





- Aktivieren Sie **sudo** Rechte:



```shell
EDITOR=nano visudo
```





- Dekommentieren Sie dann die Zeile:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Starten Sie das System neu und melden Sie sich mit Ihrem Benutzernamen an.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Installation der Software



Da Arch Linux minimalistisch ist, wird eine Menge Software standardmäßig nicht installiert. Um das hinzuzufügen, was Sie benötigen, geben Sie den folgenden Befehl ein:



```shell
pacman -S nom_du_paquet_a_installe
```



Um z.B. den Texteditor **nano** zu installieren, können Sie:



```shell
pacman -S nano
```



Um einen leichtgewichtigen Webbrowser wie `firefox` zu installieren, verwenden Sie:



```shell
pacman -S firefox
```



Wenn Sie schließlich wichtige Netzwerk-Tools wie `net-tools` hinzufügen möchten, lautet der Befehl:



```shell
pacman -S net-tools
```



Vergessen Sie nicht, dass Sie mehrere Pakete mit einem einzigen Befehl installieren können, indem Sie sie einzeln auflisten:



```shell
pacman -S vim firefox net-tools
```



Arch Linux zeichnet sich durch seine bemerkenswerte Stabilität, seine minimalistische Philosophie und seine Robustheit aus, was es zu einer idealen Wahl für Entwicklungsumgebungen macht. Durch die Beschränkung auf das Wesentliche bietet es eine schlanke, leistungsstarke Grundlage, die sich leicht an Ihre spezifischen Anforderungen anpassen lässt. Dieser minimalistische Ansatz begünstigt auch eine bessere Kontrolle über das System und erhöht die Sicherheit, da die Angriffsfläche begrenzt wird. Dank der aktiven Community und der ausführlichen Dokumentation kann Arch Linux Ihnen helfen, eine sichere, flexible und für die professionelle Entwicklung optimierte Umgebung zu schaffen.



Wenn Ihnen der Einstieg in Arch Linux gefallen hat, wird Ihnen unser Tutorial über **Fedora OS** gefallen, ein modulares, sicheres und robustes Betriebssystem, das sich an Ihre Bedürfnisse und Anwendungen anpassen lässt.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1