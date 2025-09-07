---
name: Arch Linux
description: Minimalistisk, högpresterande distribution utformad enligt KISS-filosofin.
---

![cover](assets/cover.webp)



Arch Linux är en distribution som är känd för sin robusthet, prestanda och anpassningsbarhet, särskilt för utvecklingsändamål. Den erbjuder utmärkt stabilitet och en miljö som är lätt att anpassa, med stöd av en extremt snabb och pålitlig pakethanterare. Filosofin bygger på **KISS**-principen (*Keep It Simple, Stupid*): att erbjuda en lätt, enkel, snabb och överskådlig distribution, samtidigt som användaren har stor frihet.



## Varför välja Arch Linux?





- Fri och öppen källkod**: Som de flesta Linux-distributioner är Arch Linux helt gratis. Det finns inga licensavgifter, vilket gör det till ett utmärkt val för studenter, frilansare eller entusiaster.
- KISS** filosofi: Arch är utformat för att vara enkelt, lätt och effektivt. Den innehåller bara det viktigaste, så att du kan bygga din miljö à la carte.
- Pacman** är en pakethanterare: Pacman är en snabb, pålitlig och väldesignad pakethanterare. Den möjliggör effektiv installation och uppdatering av programvara och hanterar beroenden med precision.
- Omfattande dokumentation och en aktiv gemenskap**: [Arch Wiki] (https://wiki.archlinux.org) är förmodligen en av de bästa tekniska dokumentationerna i Linux-världen. Det är en guldgruva för att förstå vad du gör. Communityt, som mestadels består av erfarna profiler, är mycket aktivt och kan hjälpa dig om du kör fast, förutsatt att du har gjort lite efterforskningar i förväg.



## Installation och konfiguration



### Förkunskapskrav



Material som krävs:





- Ett USB-minne på minst **8 GB**
- minst 2 GB** RAM-minne
- En dator med minst 20 GB ledigt diskutrymme



### Nedladdningar



![0_1](assets/fr/01.webp)



Sedan 2017 har Arch Linux inte längre stöd för 32-bitarsarkitekturer. Endast 64-bitarsversioner finns tillgängliga.





- Besök [den officiella webbplatsen] (https://mir.archlinux.fr/iso/latest/) för att ladda ner den senaste officiella versionen av ISO-bilden.



### Skapa en startbar nyckel



För att skapa ett startbart USB-minne kan du använda ett verktyg som **Balena Etcher**:





- Ladda ner Balena Etcher från den [officiella webbplatsen](https://etcher.balena.io).
- Starta programmet och välj Arch Linux ISO-image.
- Välj din USB-nyckel som målenhet.
- Klicka på **Flash** för att börja skapa den startbara nyckeln.



![0_2](assets/fr/02.webp)



## Installera Arch Linux



## Starta på USB-nyckel





- Stäng av din dator helt och hållet
- Anslut det startbara USB-minnet
- Starta om och gå till BIOS/UEFI genom att trycka på **F1**, **Escape**, **F9**, etc. (beroende på modell)
- I startmenyn väljer du USB-nyckeln som startenhet. Om allt är korrekt inställt kommer du till startskärmen för Arch Linux Interface.



## Starta installationen



På startskärmen väljer du det första alternativet för att starta installationen. Observera att Arch Linux inte erbjuder någon grafisk installation. När installationen har startats kommer du till en terminal i root-läge.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Konfiguration av tangentbord



Du kan visa de tillgängliga layouterna med:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Ladda sedan en layout med:



```shell
loadkeys nom-disposition
```



Som standard är tangentbordet på engelska (qwerty), men du kan byta till `azerty` med `loadkeys fr`.



### Ställa in datum och tid



Arch Linux använder verktyget `timedatectl` för att hantera systemklockan.



![0_7](assets/fr/07.webp)





- Ställ in din tidszon med:


```shell
timedatectl set-timezone Europe/Paris
```





- Kontrollera att automatisk synkronisering är aktiverad med:


```shell
timedatectl status
```





- Aktivera den om det behövs:


```shell
timedatectl set-ntp true
```




Detta aktiverar NTP, protokollet för automatisk synkronisering med tidsservrar. Detta steg är viktigt för att undvika datumfel när du installerar paket eller konfigurerar SSL-certifikat senare.



### Diskpartitionering





- Kontrollera om ditt system startar i **UEFI** eller **BIOS** med:



```shell
ls /sys/firmware/efi
```



Om filen finns, befinner du dig i **UEFI**. Annars befinner du dig i **BIOS (Legacy)**.




- Lista de tillgängliga diskarna:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Starta Partition Manager:



```shell
cfdisk /dev/nom-du-disque
```



Välj **GPT** om du använder UEFI och **DOS** om du använder BIOS.



![0_9](assets/fr/09.webp)



#### Poäng för att skapa




- I UEFI**-läge



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



Välj **Write**, skriv **yes** och sedan **Quit**.



### Formatering av partitioner





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



### Grundläggande systeminstallation



Montera **root**-partitionen:





- Om BIOS:


```shell
mount /dev/sda2 /mnt
```




- på UEFI:


```shell
mount /dev/sda3 /mnt
```



Installera sedan de nödvändiga paketen:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate filen **fstab**, som gör det möjligt för operativsystemet att automatiskt hantera partitionsmontering vid varje start, utan manuell inblandning:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Gå in i miljön **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Systemkonfiguration





- Installera en textredigerare för att redigera:



```shell
pacman -S vim
```





- Ställa in språk:


Redigera `/etc/locale.gen` och kommentera sedan bort raden `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Ställ in maskinens namn:



```shell
echo nom_machine > /etc/hostname
```





- Ange root-lösenord:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Installera GRUB



Installera:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



När du har hämtat den måste du installera den enligt diskpartitionsformatet.




- För **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- För **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Färdigställande





- Avsluta chroot-miljön:


```shell
exit
```





- Ta bort partitionerna:


```shell
umount -R /mnt
```





- Starta om:


```shell
reboot
```



Vid uppstart loggar du in med ditt **root**-inloggningsnamn och lösenord.



![0_18](assets/fr/18.webp)


## Nätverksanslutning efter omstart



Det kan hända att ingen nätverksanslutning är aktiv vid omstart. Du kan lista gränssnitten med:



```shell
ip link
```



Konfigurera sedan Interface-nätverket genom att skriva in följande text i terminalen



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface-grafik (GNOME)



Som standard innehåller **Arch Linux** ingen grafisk Interface. För att lägga till en:



Uppdatera systemet:



```shell
pacman -Syu
```



Installera **Xorg** med följande kommando och tryck på enter varje gång för att behålla standardvalen:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Installera **GNOME** med följande kommando och ange varje gång för att behålla standardvalen:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Aktivera **session manager**:



```shell
systemctl enable gdm
systemctl start gdm
```



Systemet startas om automatiskt och du får den grafiska inloggningen Interface. Logga in med användarnamnet och lösenordet root.



![0_21](assets/fr/21.webp)



## Skapa en användare



När du väl är i **Interface GNOME** måste du skapa en ny användare för ökad säkerhet och säkrare, riskfri användning. Gå in i program och välj alternativet "console" för att starta terminalen.





- Lägg till en användare:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Installera **sudo**:


```shell
pacman -S sudo
```





- Aktivera **sudo**-rättigheter:



```shell
EDITOR=nano visudo
```





- Ta sedan bort raden:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Starta om systemet och logga in med ditt användarnamn.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Installera programvara



Eftersom Arch Linux är minimalistiskt är det många program som inte är installerade som standard. För att lägga till det du behöver skriver du följande kommando:



```shell
pacman -S nom_du_paquet_a_installe
```



Om du till exempel vill installera textredigeraren **nano** kan du skriva:



```shell
pacman -S nano
```



För att installera en lättviktig webbläsare som `firefox`, använd:



```shell
pacman -S firefox
```



Slutligen, om du vill lägga till viktiga nätverksverktyg som `net-tools`, skulle kommandot vara:



```shell
pacman -S net-tools
```



Glöm inte att du kan installera flera paket i ett enda kommando genom att lista dem separat:



```shell
pacman -S vim firefox net-tools
```



Arch Linux utmärker sig genom sin anmärkningsvärda stabilitet, minimalistiska filosofi och robusthet, vilket gör det till ett perfekt val för utvecklingsmiljöer. Genom att bara tillhandahålla det viktigaste erbjuder det en lättviktig, högpresterande grund som är lätt att anpassa till dina specifika behov. Det minimalistiska tillvägagångssättet ger också större kontroll över systemet, vilket stärker säkerheten genom att begränsa attackytan. Tack vare sin aktiva community och omfattande dokumentation kan Arch Linux hjälpa dig att skapa en säker och flexibel miljö som är optimerad för professionell utveckling.



Om du tyckte om att komma igång med Arch Linux kommer du att älska vår handledning om **Fedora OS**, ett modulärt, säkert och robust operativsystem som anpassar sig till dina behov och användningsområden.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1