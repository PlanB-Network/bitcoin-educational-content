---
name: Arch Linux
description: Minimalistisk, høytytende distribusjon utformet i henhold til KISS-filosofien.
---

![cover](assets/cover.webp)



Arch Linux er en distribusjon som er kjent for sin robusthet, ytelse og tilpasningsdyktighet, spesielt for utviklingsformål. Den tilbyr utmerket stabilitet og et miljø som bidrar til tilpasning, støttet av en ekstremt rask og pålitelig pakkehåndtering. Filosofien er basert på **KISS** (*Keep It Simple, Stupid*)-prinsippet: å tilby en lett, enkel, rask og oversiktlig distribusjon, samtidig som brukeren får stor frihet.



## Hvorfor velge Arch Linux?





- Gratis og åpen kildekode**: Som de fleste Linux-distribusjoner er Arch Linux helt gratis. Det er ingen lisensavgifter, noe som gjør den til et utmerket valg for studenter, frilansere eller entusiaster.
- KISS**-filosofien: Arch er designet for å være enkel, lett og effektiv. Den inneholder bare det viktigste, slik at du kan bygge opp miljøet ditt à la carte.
- Pakkebehandleren Pacman**: Pacman er en rask, pålitelig og veldesignet pakkebehandler. Den muliggjør effektiv installasjon og oppdatering av programvare, og håndterer avhengigheter med presisjon.
- Omfattende dokumentasjon og et aktivt fellesskap**: [Arch Wiki] (https://wiki.archlinux.org) er sannsynligvis en av de beste tekniske dokumentasjonene i Linux-verdenen. Det er en gullgruve for å forstå hva du gjør. Fellesskapet, som for det meste består av erfarne profiler, er svært aktivt og kan hjelpe deg hvis du står fast, forutsatt at du har gjort litt research på forhånd.



## Installasjon og konfigurasjon



### Forutsetninger



Materialer som kreves:





- En USB-nøkkel på minst **8 GB**
- minimum 2 GB** RAM
- En datamaskin med minst 20 GB ledig diskplass



### Last ned



![0_1](assets/fr/01.webp)



Siden 2017 har Arch Linux ikke lenger støtte for 32-bits arkitekturer. Kun 64-biters versjoner er tilgjengelige.





- Besøk [det offisielle nettstedet] (https://mir.archlinux.fr/iso/latest/) for å laste ned den nyeste offisielle versjonen av ISO-bildet.



### Opprett en oppstartbar nøkkel



For å lage en oppstartbar USB-minnepinne kan du bruke et verktøy som **Balena Etcher**:





- Last ned Balena Etcher fra [offisiell nettside] (https://etcher.balena.io).
- Start programvaren, velg Arch Linux ISO-bildet.
- Velg USB-nøkkelen din som målenhet.
- Klikk på **Flash** for å starte opprettelsen av den oppstartbare nøkkelen.



![0_2](assets/fr/02.webp)



## Installere Arch Linux



## Oppstart på USB-nøkkel





- Slå av datamaskinen helt
- Plugg inn den oppstartbare USB-nøkkelen
- Start på nytt og gå inn i BIOS/UEFI ved å trykke på **F1**, **Escape**, **F9**, osv
- I oppstartsmenyen velger du USB-nøkkelen som oppstartsenhet. Hvis alt er riktig konfigurert, kommer du til oppstartsskjermen til Arch Linux Interface.



## Starter installasjonen



På oppstartsskjermen velger du det første alternativet for å starte installasjonen. Merk at Arch Linux ikke tilbyr et grafisk installasjonsprogram. Når du har startet installasjonen, blir du ført til en terminal i root-modus.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Tastaturkonfigurasjon



Du kan vise de tilgjengelige layoutene med:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Last deretter inn en layout med:



```shell
loadkeys nom-disposition
```



Som standard er tastaturet på engelsk (qwerty), men du kan bytte til `azerty` med `loadkeys fr`.



### Stille inn dato og klokkeslett



Arch Linux bruker verktøyet `timedatectl` til å styre systemklokken.



![0_7](assets/fr/07.webp)





- Still inn tidssonen din med:


```shell
timedatectl set-timezone Europe/Paris
```





- Kontroller at automatisk synkronisering er aktivert med:


```shell
timedatectl status
```





- Aktiver den om nødvendig:


```shell
timedatectl set-ntp true
```




Dette aktiverer NTP, protokollen for automatisk synkronisering med tidsservere. Dette trinnet er viktig for å unngå datofeil når du installerer pakker eller konfigurerer SSL-sertifikater senere.



### Diskpartisjonering





- Sjekk om systemet starter i **UEFI** eller **BIOS** med:



```shell
ls /sys/firmware/efi
```



Hvis filen finnes, befinner du deg i **UEFI**. Hvis ikke, er du i **BIOS (Legacy)**.




- Liste over tilgjengelige disker:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Start Partition Manager:



```shell
cfdisk /dev/nom-du-disque
```



Velg **GPT** hvis du bruker UEFI, og **DOS** hvis du bruker BIOS.



![0_9](assets/fr/09.webp)



#### Poeng for å skape




- I UEFI**-modus



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- I BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Velg **Write**, skriv **yes** og deretter **Quit**.



### Formatering av partisjoner





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



### Grunnleggende systeminstallasjon



Monter **root**-partisjonen:





- På BIOS:


```shell
mount /dev/sda2 /mnt
```




- på UEFI:


```shell
mount /dev/sda3 /mnt
```



Installer deretter de viktigste pakkene:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate **fstab**-filen, som gjør det mulig for operativsystemet å håndtere partisjonsmontering automatisk ved hver oppstart, uten manuell inngripen:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Gå inn i **Chroot**-miljøet:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Systemkonfigurasjon





- Installer et tekstredigeringsprogram for å redigere:



```shell
pacman -S vim
```





- Still inn språket:


Rediger `/etc/locale.gen` og fjern deretter kommentarene i linjen `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Angi maskinens navn:



```shell
echo nom_machine > /etc/hostname
```





- Angi root-passord:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Installere GRUB



Installer:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Når du har lastet ned, må du installere den i henhold til diskpartisjonsformatet.




- For **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- For **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Ferdigstillelse





- Avslutt chroot-miljøet:


```shell
exit
```





- Fjern partisjonene:


```shell
umount -R /mnt
```





- Start på nytt:


```shell
reboot
```



Ved oppstart logger du på med **root**-påloggingen og passordet ditt.



![0_18](assets/fr/18.webp)


## Nettverkstilkobling etter omstart



Det kan hende at ingen nettverkstilkobling er aktiv ved omstart. Du kan liste opp grensesnittene med:



```shell
ip link
```



Konfigurer deretter Interface-nettverket ved å skrive inn følgende tekst i terminalen



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface-grafikk (GNOME)



Som standard inneholder **Arch Linux** ingen grafisk Interface. For å legge til en:



Oppdater systemet:



```shell
pacman -Syu
```



Installer **Xorg** med følgende kommando, og trykk enter hver gang for å beholde standardvalgene:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Installer **GNOME** med følgende kommando, og skriv inn hver gang for å beholde standardvalgene:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Aktiver **session manager**:



```shell
systemctl enable gdm
systemctl start gdm
```



Systemet starter automatisk på nytt, og du får opp den grafiske Interface-påloggingen. Logg inn med root-brukernavnet og -passordet.



![0_21](assets/fr/21.webp)



## Opprette en bruker



Når du er inne i **Interface GNOME**, må du opprette en ny bruker for å oppnå større sikkerhet og tryggere, risikofri bruk. Gå inn i programmer og velg alternativet "konsoll" for å starte terminalen.





- Legg til en bruker:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Installer **sudo**:


```shell
pacman -S sudo
```





- Aktiver **sudo**-rettigheter:



```shell
EDITOR=nano visudo
```





- Fjern deretter kommentarene i linjen:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Start systemet på nytt, og logg inn med brukernavnet ditt.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Installere programvare



Siden Arch Linux er minimalistisk, er det mye programvare som ikke er installert som standard. For å legge til det du trenger, skriver du inn følgende kommando:



```shell
pacman -S nom_du_paquet_a_installe
```



Hvis du for eksempel vil installere tekstredigeringsprogrammet **nano**, kan du skrive:



```shell
pacman -S nano
```



For å installere en lett nettleser som `firefox`, bruker du:



```shell
pacman -S firefox
```



Hvis du ønsker å legge til viktige nettverksverktøy som `net-tools`, kan du bruke kommandoen:



```shell
pacman -S net-tools
```



Husk at du kan installere flere pakker i én og samme kommando ved å liste dem opp separat:



```shell
pacman -S vim firefox net-tools
```



Arch Linux skiller seg ut med sin bemerkelsesverdige stabilitet, minimalistiske filosofi og robusthet, noe som gjør det til et ideelt valg for utviklingsmiljøer. Ved å tilby kun det aller nødvendigste, får du et lett, høytytende fundament som er enkelt å tilpasse til dine spesifikke behov. Denne minimalistiske tilnærmingen gir også større kontroll over systemet, noe som styrker sikkerheten ved å begrense angrepsflaten. Takket være det aktive fellesskapet og den omfattende dokumentasjonen kan Arch Linux hjelpe deg med å skape et sikkert og fleksibelt miljø som er optimalisert for profesjonell utvikling.



Hvis du har hatt glede av å komme i gang med Arch Linux, vil du elske vår veiledning om **Fedora OS**, et modulært, sikkert og robust operativsystem som tilpasser seg dine behov og bruksområder.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1