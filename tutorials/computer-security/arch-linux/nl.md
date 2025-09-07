---
name: Arch Linux
description: Minimalistische distributie met hoge prestaties, ontworpen volgens de KISS-filosofie.
---

![cover](assets/cover.webp)



Arch Linux is een distributie die bekend staat om zijn robuustheid, prestaties en aanpassingsvermogen, vooral voor ontwikkelingsdoeleinden. Het biedt een uitstekende stabiliteit en een omgeving die bevorderlijk is voor aanpassingen, ondersteund door een extreem snelle en betrouwbare pakketbeheerder. De filosofie is gebaseerd op het **KISS** (*Keep It Simple, Stupid*) principe: het aanbieden van een lichte, eenvoudige, snelle en overzichtelijke distributie, terwijl het de gebruiker veel vrijheid laat.



## Waarom kiezen voor Arch Linux?





- Gratis en open source**: Net als de meeste Linux-distributies is Arch Linux helemaal gratis. Er zijn geen licentiekosten, waardoor het een uitstekende keuze is voor studenten, freelancers of enthousiastelingen.
- KISS** filosofie: Arch is ontworpen om eenvoudig, licht en efficiënt te zijn. Het biedt alleen het essentiële, zodat je je omgeving à la carte kunt opbouwen.
- Pacman** pakketbeheerder: Pacman is een snelle, betrouwbare en goed ontworpen pakketbeheerder. Het maakt efficiënte installatie en updaten van software mogelijk en beheert afhankelijkheden met precisie.
- Uitgebreide documentatie en een actieve gemeenschap**: de [Arch Wiki](https://wiki.archlinux.org) is waarschijnlijk een van de beste technische documentaties in de Linux-wereld. Het is een goudmijn om te begrijpen wat je aan het doen bent. De gemeenschap, die voornamelijk bestaat uit ervaren profielen, is erg actief en kan je helpen als je vastloopt, op voorwaarde dat je van tevoren wat onderzoek hebt gedaan.



## Installatie en configuratie



### Vereisten



Benodigde materialen:





- Een USB-sleutel van minstens **8 GB**
- minimaal 2 GB** RAM
- Een computer met minstens 20 GB vrije schijfruimte



### Downloaden



![0_1](assets/fr/01.webp)



Sinds 2017 ondersteunt Arch Linux geen 32-bits architecturen meer. Alleen 64-bits versies zijn beschikbaar.





- Ga naar [de officiële website](https://mir.archlinux.fr/iso/latest/) om de nieuwste officiële versie van het ISO-image te downloaden.



### Een opstartbare sleutel maken



Om een bootable USB flash drive te maken, kun je een tool zoals **Balena Etcher** gebruiken:





- Download Balena Etcher van de [officiële website] (https://etcher.balena.io).
- Start de software en selecteer de Arch Linux ISO image.
- Kies je USB-sleutel als doelapparaat.
- Klik op **Flash** om te beginnen met het maken van de opstartbare sleutel.



![0_2](assets/fr/02.webp)



## Arch Linux installeren



## Opstarten op USB-sleutel





- Schakel uw computer volledig uit
- Sluit de opstartbare USB-sleutel aan
- Herstart en ga naar BIOS/UEFI door op **F1**, **Escape**, **F9**, etc. te drukken (afhankelijk van je model)
- Kies in het opstartmenu de USB-sleutel als opstartapparaat. Als alles correct is ingesteld, kom je in het opstartscherm van Arch Linux Interface.



## De installatie starten



Kies in het opstartscherm de eerste optie om de installatie te starten. Arch Linux heeft geen grafisch installatieprogramma. Eenmaal gestart, kom je in een terminal in rootmodus.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Configuratie toetsenbord



U kunt de beschikbare lay-outs weergeven met:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Laad vervolgens een lay-out met:



```shell
loadkeys nom-disposition
```



Standaard is het toetsenbord in het Engels (qwerty), maar je kunt overschakelen naar `azerty` met `loadkeys fr`.



### Datum en tijd instellen



Arch Linux gebruikt het hulpprogramma `timedatectl` om de systeemklok te beheren.



![0_7](assets/fr/07.webp)





- Stel uw tijdzone in met:


```shell
timedatectl set-timezone Europe/Paris
```





- Controleer of automatische synchronisatie is ingeschakeld met:


```shell
timedatectl status
```





- Activeer het indien nodig:


```shell
timedatectl set-ntp true
```




Dit activeert NTP, het protocol voor automatische synchronisatie met tijdservers. Deze stap is belangrijk om datumfouten te voorkomen als je later pakketten installeert of SSL-certificaten configureert.



### Schijfpartitionering





- Controleer of je systeem opstart in **UEFI** of **BIOS** met:



```shell
ls /sys/firmware/efi
```



Als het bestand bestaat, ben je in **UEFI**. Anders ben je in **BIOS (Legacy)**.




- Geef de beschikbare schijven weer:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Partition Manager starten:



```shell
cfdisk /dev/nom-du-disque
```



Kies **GPT** als je in UEFI zit, **DOS** als je in BIOS zit.



![0_9](assets/fr/09.webp)



#### Scores maken




- In UEFI**-modus



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- In BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Selecteer **Schrijven**, typ **ja** en vervolgens **Afsluiten**.



### Partities formatteren





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



### Basisinstallatie van het systeem



Koppel de **root** partitie aan:





- In het BIOS:


```shell
mount /dev/sda2 /mnt
```




- op UEFI:


```shell
mount /dev/sda3 /mnt
```



Installeer vervolgens de essentiële pakketten:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate het **fstab** bestand, dat het besturingssysteem in staat stelt om het mounten van partities automatisch te beheren bij elke boot, zonder handmatige tussenkomst:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Ga naar de **Chroot** omgeving:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Systeemconfiguratie





- Installeer een teksteditor om:



```shell
pacman -S vim
```





- De taal instellen:


Bewerk `/etc/locale.gen` en verwijder het commentaar uit de regel `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Stel de machinenaam in:



```shell
echo nom_machine > /etc/hostname
```





- Root-wachtwoord instellen:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### GRUB installeren



Installeer de:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Eenmaal gedownload, moet je het installeren volgens het formaat van de schijfpartitie.




- Voor **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Voor **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Afronding





- Sluit de chroot omgeving af:


```shell
exit
```





- Verwijder de partities:


```shell
umount -R /mnt
```





- Opnieuw opstarten:


```shell
reboot
```



Log bij het opstarten in met uw **root** login en wachtwoord.



![0_18](assets/fr/18.webp)


## Netwerkverbinding na opnieuw opstarten



Het kan gebeuren dat er geen netwerkverbinding actief is bij het herstarten. Je kunt de interfaces oplijsten met:



```shell
ip link
```



Configureer dan het Interface netwerk door de volgende tekst in de terminal in te voeren



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface afbeeldingen (GNOME)



Standaard bevat **Arch Linux** geen grafische Interface. Om er een toe te voegen:



Werk het systeem bij:



```shell
pacman -Syu
```



Installeer **Xorg** met het volgende commando en druk telkens op enter om de standaardkeuzes te behouden:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Installeer **GNOME** met het volgende commando en voer telkens in om de standaardkeuzes te behouden:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Activeer de **sessiebeheerder**:



```shell
systemctl enable gdm
systemctl start gdm
```



Het systeem start automatisch opnieuw op en je krijgt de Interface grafische login. Log in met de root gebruikersnaam en het wachtwoord.



![0_21](assets/fr/21.webp)



## Een gebruiker aanmaken



Eenmaal in **Interface GNOME**, moet je een nieuwe gebruiker aanmaken voor meer veiligheid en veiliger, risicoloos gebruik. Voer toepassingen in en kies de "console" optie om de terminal te starten.





- Een gebruiker toevoegen:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Installeer **sudo**:


```shell
pacman -S sudo
```





- Activeer **sudo** rechten:



```shell
EDITOR=nano visudo
```





- Verwijder dan het commentaar uit de regel:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Start het systeem opnieuw op en log in met je gebruikersnaam.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Software installeren



Omdat Arch Linux minimalistisch is, is veel software niet standaard geïnstalleerd. Om toe te voegen wat je nodig hebt, typ je het volgende commando:



```shell
pacman -S nom_du_paquet_a_installe
```



Om bijvoorbeeld de **nano** teksteditor te installeren, typ je:



```shell
pacman -S nano
```



Om een lichtgewicht webbrowser zoals `firefox` te installeren, gebruik je:



```shell
pacman -S firefox
```



Als je tenslotte essentiële netwerkgereedschappen zoals `net-tools` wilt toevoegen, is het commando:



```shell
pacman -S net-tools
```



Vergeet niet dat je meerdere pakketten in één commando kunt installeren door ze apart te vermelden:



```shell
pacman -S vim firefox net-tools
```



Arch Linux valt op door zijn opmerkelijke stabiliteit, minimalistische filosofie en robuustheid, waardoor het een ideale keuze is voor ontwikkelomgevingen. Door alleen het essentiële te bieden, biedt het een lichtgewicht, high-performance basis die eenvoudig aan te passen is aan je specifieke behoeften. Deze minimalistische aanpak bevordert ook een grotere controle over het systeem, waardoor de beveiliging wordt versterkt door het aanvalsoppervlak te beperken. Dankzij de actieve gemeenschap en uitgebreide documentatie kan Arch Linux je helpen om een veilige, flexibele omgeving te creëren die geoptimaliseerd is voor professionele ontwikkeling.



Als je het leuk vond om met Arch Linux aan de slag te gaan, vind je onze tutorial over **Fedora OS** vast geweldig. Dit is een modulair, veilig en robuust besturingssysteem dat zich aanpast aan jouw behoeften en gebruik.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1