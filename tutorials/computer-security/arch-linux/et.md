---
name: Arch Linux
description: Minimalistlik, suure jõudlusega jaotus, mis on loodud KISS-filosoofia kohaselt.
---

![cover](assets/cover.webp)



Arch Linux on distributsioon, mis on tuntud oma töökindluse, jõudluse ja kohanemisvõime poolest, eriti arenduseesmärkidel. See pakub suurepärast stabiilsust ja kohandamist soodustavat keskkonda, mida toetab äärmiselt kiire ja usaldusväärne paketihaldur. Selle filosoofia põhineb **KISS** (*Keep It Simple, Stupid*) põhimõttel: pakkuda kerget, lihtsat, kiiret ja lihtsat distributsiooni, jättes samas kasutajale palju vabadust.



## Miks valida Arch Linux?





- Tasuta ja avatud lähtekoodiga**: Arch Linux on nagu enamik Linuxi distributsioone täiesti tasuta. Litsentsitasusid ei ole, mistõttu on see suurepärane valik üliõpilastele, vabakutselistele või entusiastidele.
- KISS** filosoofia: Arch on loodud lihtsaks, kergeks ja tõhusaks. See pakub ainult hädavajalikku, võimaldades teil luua oma keskkonda à la carte.
- Pacman** paketihaldur: Pacman on kiire, usaldusväärne ja hästi disainitud paketihaldur. See võimaldab tarkvara tõhusat paigaldamist ja uuendamist ning haldab täpselt sõltuvusi.
- Põhjalik dokumentatsioon ja aktiivne kogukond**: [Arch Wiki](https://wiki.archlinux.org) on tõenäoliselt üks parimaid tehnilisi dokumente Linuxi maailmas. See on kullaauk, et mõista, mida sa teed. Kogukond, mis koosneb enamasti kogenud profiilidest, on väga aktiivne ja võib sind aidata, kui sa hätta jääd, eeldusel, et oled eelnevalt natuke uurinud.



## Paigaldamine ja konfigureerimine



### Eeltingimused



Vajalikud materjalid:





- Vähemalt **8 GB suurune USB-mälu**
- vähemalt 2 GB** RAM
- Arvuti, millel on vähemalt 20 GB vaba kettaruumi



### Lae alla



![0_1](assets/fr/01.webp)



Alates 2017. aastast ei toeta Arch Linux enam 32-bitiseid arhitektuure. Saadaval on ainult 64-bitised versioonid.





- Külastage [ametlik kodulehekülg](https://mir.archlinux.fr/iso/latest/), et laadida alla ISO-kujutise uusim ametlik versioon.



### Luua käivitatav võti



Käivitatava USB-mäluseadme loomiseks saate kasutada sellist tööriista nagu **Balena Etcher**:





- Lae Balena Etcher alla [ametlik kodulehekülg](https://etcher.balena.io).
- Käivitage tarkvara, valige Arch Linuxi ISO-pilt.
- Valige sihtseadmeks oma USB-mälu.
- Klõpsake **Flash**, et alustada käivitatava võtme loomist.



![0_2](assets/fr/02.webp)



## Arch Linuxi paigaldamine



## Käivitamine USB-mäluseadmelt





- Lülitage arvuti täielikult välja
- Ühendage käivitatav USB-mäluseade
- Taaskäivitage ja sisenege BIOS/UEFI-süsteemi, vajutades **F1**, **Escape**, **F9** jne (sõltuvalt mudelist)
- Valige alglaadimismenüüst alglaadimisseadmeks USB-mäluseade. Kui kõik on õigesti seadistatud, jõuate Arch Linux Interface alglaadimisekraanile.



## Paigalduse käivitamine



Käivitamisekraanil valige paigaldamise käivitamiseks esimene valik. Pange tähele, et Arch Linux ei paku graafilist paigaldusprogrammi. Pärast käivitamist viiakse teid root-režiimis olevasse terminali.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Klaviatuuri konfiguratsioon



Saate kuvada olemasolevad kujundused koos:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Seejärel laadige paigutus:



```shell
loadkeys nom-disposition
```



Vaikimisi on klaviatuur inglise keeles (qwerty), kuid sa võid lülituda `loadkeys fr`ga `azerty` peale.



### Kuupäeva ja kellaaja seadmine



Arch Linux kasutab süsteemi kella haldamiseks tööriista `timedatectl`.



![0_7](assets/fr/07.webp)





- Seadistage oma ajavööndiga:


```shell
timedatectl set-timezone Europe/Paris
```





- Kontrollige, et automaatne sünkroniseerimine on lubatud funktsiooniga:


```shell
timedatectl status
```





- Aktiveerige see vajaduse korral:


```shell
timedatectl set-ntp true
```




See aktiveerib NTP, protokolli automaatse sünkroniseerimise ajaserveritega. See samm on oluline, et vältida hiljem pakettide paigaldamisel või SSL-sertifikaatide konfigureerimisel kuupäevavigu.



### Ketta partitsioneerimine





- Kontrollige, kas teie süsteem käivitub **UEFI** või **BIOS** süsteemiga:



```shell
ls /sys/firmware/efi
```



Kui fail on olemas, olete **UEFI**. Vastasel juhul olete **BIOSis (Legacy)**.




- Loetlege olemasolevad kettad:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Käivitage Partition Manager:



```shell
cfdisk /dev/nom-du-disque
```



Valige **GPT**, kui olete UEFI-s, **DOS**, kui olete BIOS-s.



![0_9](assets/fr/09.webp)



#### Punktide loomine




- UEFI** režiimis



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- BIOSis



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Valige **Kirjuta**, sisestage **jah** ja seejärel **Lõpeta**.



### Partitsioonide vormindamine





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



### Põhiline süsteemi paigaldamine



Paigaldage **juur** partitsiooni:





- BIOSis:


```shell
mount /dev/sda2 /mnt
```




- uEFIs:


```shell
mount /dev/sda3 /mnt
```



Seejärel paigaldage olulised paketid:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate fail **fstab**, mis võimaldab operatsioonisüsteemil automaatselt hallata partitsioonide paigaldamist igal käivitamisel ilma käsitsi sekkumiseta:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Sisestage keskkond **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Süsteemi konfiguratsioon





- Paigaldage tekstiredaktor, et muuta:



```shell
pacman -S vim
```





- Määrake keel:


Redigeeri `/etc/locale.gen` ja eemalda kommentaarid realt `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Määra masina nimi:



```shell
echo nom_machine > /etc/hostname
```





- Seadistage juurkasutaja parool:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### GRUBi paigaldamine



Paigaldage:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Pärast allalaadimist peate selle paigaldama vastavalt kettapartitsiooni formaadile.




- **BIOS** puhul:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- **UEFI** puhul:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Lõplikustamine





- Väljumine chroot-keskkonnast:


```shell
exit
```





- Eemaldage vaheseinad:


```shell
umount -R /mnt
```





- Restart:


```shell
reboot
```



Käivitamisel logige sisse oma **juurtunnuse** ja parooliga.



![0_18](assets/fr/18.webp)


## Võrguühendus pärast taaskäivitust



Võib juhtuda, et taaskäivitamisel ei ole võrguühendus aktiivne. Liidesed saate loetleda koos:



```shell
ip link
```



Seejärel konfigureerige Interface võrk, sisestades terminali järgmise teksti



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface graafika (GNOME)



Vaikimisi ei sisalda **Arch Linux** graafilist Interface. Et lisada üks:



Värskendage süsteemi:



```shell
pacman -Syu
```



Paigaldage **Xorg** järgmise käsuga ja vajutage iga kord enter, et säilitada vaikimisi valikud:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Paigaldage **GNOME** järgmise käsuga ja sisestage iga kord, et säilitada vaikimisi valikud:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Aktiveerige **sessioonihaldur**:



```shell
systemctl enable gdm
systemctl start gdm
```



Süsteem taaskäivitub automaatselt ja te saate Interface graafilise sisselogimise. Logige sisse juurkasutaja nime ja parooliga.



![0_21](assets/fr/21.webp)



## Kasutaja loomine



Kui olete **Interface GNOME's**, peate suurema turvalisuse ja turvalisema, riskivaba kasutamise tagamiseks looma uue kasutaja. Sisestage rakendused ja valige terminali käivitamiseks valik "konsool".





- Lisa kasutaja:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Paigalda **sudo**:


```shell
pacman -S sudo
```





- Aktiveerige **sudo** õigused:



```shell
EDITOR=nano visudo
```





- Seejärel eemaldage kommentaarid realt:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Käivitage süsteem uuesti ja logige sisse oma kasutajanimega.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Tarkvara paigaldamine



Kuna Arch Linux on minimalistlik, ei ole palju tarkvara vaikimisi paigaldatud. Selleks, et lisada see, mida vajate, kirjutage järgmine käsk:



```shell
pacman -S nom_du_paquet_a_installe
```



Näiteks tekstiredaktori **nano** installimiseks võite kirjutada:



```shell
pacman -S nano
```



Kergema veebibrauseri, näiteks `firefox` paigaldamiseks kasutage:



```shell
pacman -S firefox
```



Lõpuks, kui soovite lisada olulisi võrguvahendeid nagu `net-tools`, siis on käsk:



```shell
pacman -S net-tools
```



Ärge unustage, et saate paigaldada mitu paketti ühe käsuga, loetledes need eraldi:



```shell
pacman -S vim firefox net-tools
```



Arch Linux paistab silma märkimisväärse stabiilsuse, minimalistliku filosoofia ja töökindluse poolest, mis teeb sellest ideaalse valiku arenduskeskkondade jaoks. Kuna see pakub ainult hädavajalikku, pakub see kerget ja suure jõudlusega alust, mida on lihtne kohandada vastavalt teie konkreetsetele vajadustele. See minimalistlik lähenemine soodustab ka suuremat kontrolli süsteemi üle, tugevdades turvalisust, piirates rünnakupinda. Tänu aktiivsele kogukonnale ja põhjalikule dokumentatsioonile aitab Arch Linux luua turvalise, paindliku keskkonna, mis on optimeeritud professionaalseks arenduseks.



Kui teile meeldis alustada Arch Linuxiga, siis meeldib teile meie õpetus **Fedora OS** kohta, mis on modulaarne, turvaline ja töökindel operatsioonisüsteem, mis kohandub vastavalt teie vajadustele ja kasutusviisidele.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1