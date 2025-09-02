---
name: Arch Linux
description: Minimalistička, visokoperformansna distribucija dizajnirana prema KISS filozofiji.
---

![cover](assets/cover.webp)



Arch Linux je distribucija poznata po svojoj robusnosti, performansama i prilagodljivosti, posebno za razvojne svrhe. Nudi izvanrednu stabilnost i okruženje pogodno za prilagođavanje, podržano izuzetno brzim i pouzdanim upraviteljem paketa. Njena filozofija se zasniva na principu **KISS** (*Keep It Simple, Stupid*): ponuditi laganu, jednostavnu, brzu i nepretrpanu distribuciju, dok korisniku ostavlja veliku slobodu.



## Zašto izabrati Arch Linux?





- Besplatan i otvoren izvor**: Kao većina Linux distribucija, Arch Linux je potpuno besplatan. Nema licenci, što ga čini odličnim izborom za studente, freelancere ili entuzijaste.
- KISS** filozofija: Arch je dizajniran da bude jednostavan, lagan i efikasan. Pruža samo osnovne stvari, omogućavajući vam da izgradite svoje okruženje à la carte.
- Pacman** package manager: Pacman je brz, pouzdan i dobro dizajniran upravitelj paketa. Omogućava efikasnu instalaciju i ažuriranje softvera, i upravlja zavisnostima sa preciznošću.
- Sveobuhvatna dokumentacija i aktivna zajednica**: [Arch Wiki](https://wiki.archlinux.org) je verovatno jedna od najboljih tehničkih dokumentacija u Linux svetu. To je rudnik zlata za razumevanje onoga što radite. Zajednica, koja se uglavnom sastoji od iskusnih profila, je veoma aktivna i može vam pomoći ako zapnete, pod uslovom da ste prethodno malo istražili.



## Instalacija i konfiguracija



### Preduslovi



Materijali potrebni:





- USB ključ od najmanje **8 GB**
- 2 GB** RAM minimum
- Računar sa najmanje 20 GB slobodnog prostora na disku



### Preuzmi



![0_1](assets/fr/01.webp)



Od 2017. godine, Arch Linux više ne podržava 32-bitne arhitekture. Dostupne su samo 64-bitne verzije.





- Posetite [zvaničnu veb stranicu](https://mir.archlinux.fr/iso/latest/) da preuzmete najnoviju zvaničnu verziju ISO slike.



### Kreiraj bootabilni ključ



Da biste kreirali USB fleš disk sa mogućnošću pokretanja, možete koristiti alat kao što je **Balena Etcher**:





- Preuzmite Balena Etcher sa [zvanične veb stranice](https://etcher.balena.io).
- Pokrenite softver, izaberite Arch Linux ISO sliku.
- Izaberite vaš USB ključ kao ciljni uređaj.
- Kliknite na **Flash** da biste započeli kreiranje bootable ključa.



![0_2](assets/fr/02.webp)



## Instaliranje Arch Linuxa



## Pokretanje sa USB ključa





- Isključite računar potpuno
- Priključite USB ključ za pokretanje sistema
- Ponovo pokrenite računar i uđite u BIOS/UEFI pritiskom na **F1**, **Escape**, **F9**, itd. (u zavisnosti od vašeg modela)
- U meniju za pokretanje izaberite USB ključ kao uređaj za pokretanje. Ako je sve ispravno podešeno, bićete prebačeni na Arch Linux Interface ekran za pokretanje.



## Pokretanje instalacije



Na ekranu za pokretanje, izaberite prvu opciju za pokretanje instalacije. Imajte na umu da Arch Linux ne nudi grafički instalacioni program. Kada se pokrene, bićete prebačeni u terminal u režimu root.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Konfiguracija tastature



Možete prikazati dostupne rasporede sa:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Zatim učitaj raspored sa:



```shell
loadkeys nom-disposition
```



Podrazumevano, tastatura je na engleskom (qwerty), ali možete prebaciti na `azerty` sa `loadkeys fr`.



### Podešavanje datuma i vremena



Arch Linux koristi alat `timedatectl` za upravljanje sistemskim satom.



![0_7](assets/fr/07.webp)





- Podesite svoju vremensku zonu pomoću:


```shell
timedatectl set-timezone Europe/Paris
```





- Proverite da li je automatska sinhronizacija omogućena sa:


```shell
timedatectl status
```





- Aktivirajte ga ako je potrebno:


```shell
timedatectl set-ntp true
```




Ovo aktivira NTP, protokol za automatsku sinhronizaciju sa vremenskim serverima. Ovaj korak je važan kako bi se izbegle greške u datumu prilikom instalacije paketa ili konfigurisanja SSL sertifikata kasnije.



### Partitionisanje diska





- Proverite da li vaš sistem pokreće u **UEFI** ili **BIOS** sa:



```shell
ls /sys/firmware/efi
```



Ako datoteka postoji, nalazite se u **UEFI**. U suprotnom, nalazite se u **BIOS (Legacy)**.




- Prikaži dostupne diskove:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Pokreni Partition Manager:



```shell
cfdisk /dev/nom-du-disque
```



Izaberite **GPT** ako ste u UEFI, **DOS** ako ste u BIOS-u.



![0_9](assets/fr/09.webp)



#### Rezultati za kreiranje




- U UEFI** režimu



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- U BIOS-u



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Odaberite **Write**, upišite **yes**, zatim **Quit**.



### Formatiranje particija





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



### Osnovna instalacija sistema



Montiraj **root** particiju:





- Na BIOS-u:


```shell
mount /dev/sda2 /mnt
```




- na UEFI:


```shell
mount /dev/sda3 /mnt
```



Zatim instalirajte osnovne pakete:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate datoteka **fstab**, koja omogućava operativnom sistemu da automatski upravlja montiranjem particija pri svakom pokretanju, bez ručne intervencije:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Uđite u **Chroot** okruženje:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Konfiguracija sistema





- Instalirajte uređivač teksta za uređivanje:



```shell
pacman -S vim
```





- Postavi jezik:


Izmenite `/etc/locale.gen` zatim uklonite komentar sa linije `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Postavite ime mašine:



```shell
echo nom_machine > /etc/hostname
```





- Postavite root lozinku:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Instaliranje GRUB-a



Instaliraj:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Kada se preuzme, potrebno je instalirati ga prema formatu particije diska.




- Za **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Za **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Finalizacija





- Izađite iz chroot okruženja:


```shell
exit
```





- Ukloni particije:


```shell
umount -R /mnt
```





- Ponovo pokreni:


```shell
reboot
```



Prilikom pokretanja, prijavite se sa svojim **root** korisničkim imenom i lozinkom.



![0_18](assets/fr/18.webp)


## Mreža povezana nakon ponovnog pokretanja



Može se desiti da nijedna mrežna veza nije aktivna pri ponovnom pokretanju. Možete navesti interfejse sa:



```shell
ip link
```



Zatim konfigurišite Interface mrežu unosom sledećeg teksta u terminal



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface grafika (GNOME)



Podrazumevano, **Arch Linux** ne sadrži grafički Interface. Da biste dodali jedan:



Ažuriraj sistem:



```shell
pacman -Syu
```



Instalirajte **Xorg** sledećom komandom i pritisnite enter svaki put da zadržite podrazumevane izbore:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Instalirajte **GNOME** sledećom komandom i pritisnite enter svaki put da zadržite podrazumevane izbore:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Aktivirajte **session manager**:



```shell
systemctl enable gdm
systemctl start gdm
```



Sistem se automatski ponovo pokreće i dobijate Interface grafički login. Prijavite se sa root korisničkim imenom i lozinkom.



![0_21](assets/fr/21.webp)



## Kreiranje korisnika



Jednom u **Interface GNOME**, trebaće da kreirate novog korisnika za veću sigurnost i bezbednije, bezrizično korišćenje. Uđite u aplikacije i izaberite opciju "konzola" da pokrenete terminal.





- Dodaj korisnika:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Instaliraj **sudo**:


```shell
pacman -S sudo
```





- Aktiviraj **sudo** prava:



```shell
EDITOR=nano visudo
```





- Zatim uklonite komentar sa linije:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Ponovo pokrenite sistem i prijavite se sa svojim korisničkim imenom.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Instaliranje softvera



Pošto je Arch Linux minimalistički, mnogo softvera nije instalirano podrazumevano. Da biste dodali ono što vam je potrebno, otkucajte sledeću komandu:



```shell
pacman -S nom_du_paquet_a_installe
```



Na primer, da biste instalirali uređivač teksta **nano**, možete upisati:



```shell
pacman -S nano
```



Da biste instalirali lagani veb pregledač kao što je `firefox`, koristite:



```shell
pacman -S firefox
```



Konačno, ako želite da dodate osnovne mrežne alate kao što je `net-tools`, komanda bi bila:



```shell
pacman -S net-tools
```



Ne zaboravite da možete instalirati nekoliko paketa u jednoj komandi tako što ćete ih navesti odvojeno:



```shell
pacman -S vim firefox net-tools
```



Arch Linux se ističe svojom izuzetnom stabilnošću, minimalističkom filozofijom i robusnošću, što ga čini idealnim izborom za razvojna okruženja. Pružajući samo osnovne elemente, nudi laganu, visokoperformansnu osnovu koju je lako prilagoditi vašim specifičnim potrebama. Ovaj minimalistički pristup takođe omogućava veću kontrolu nad sistemom, jačajući sigurnost ograničavanjem površine napada. Zahvaljujući aktivnoj zajednici i iscrpnoj dokumentaciji, Arch Linux vam može pomoći da kreirate sigurno, fleksibilno okruženje optimizovano za profesionalni razvoj.



Ako ste uživali u početku sa Arch Linuxom, svidet će vam se naš vodič o **Fedora OS**, modularnom, sigurnom i robusnom operativnom sistemu koji se prilagođava vašim potrebama i upotrebama.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1