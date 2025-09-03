---
name: Arch Linux
description: Minimalistinen, suorituskykyinen jakelu, joka on suunniteltu KISS-filosofian mukaisesti.
---

![cover](assets/cover.webp)



Arch Linux on jakelu, joka on tunnettu vankkuudestaan, suorituskyvystään ja mukautuvuudestaan erityisesti kehitystarkoituksiin. Se tarjoaa erinomaista vakautta ja räätälöintiä suosivan ympäristön, jota tukee erittäin nopea ja luotettava paketinhallinta. Sen filosofia perustuu **KISS** (*Keep It Simple, Stupid*) -periaatteeseen: tarjota kevyt, yksinkertainen, nopea ja selkeä jakelu, joka jättää käyttäjälle paljon vapautta.



## Miksi valita Arch Linux?





- Ilmainen ja avoin lähdekoodi**: Kuten useimmat Linux-jakelut, Arch Linux on täysin ilmainen. Lisenssimaksuja ei ole, joten se on erinomainen valinta opiskelijoille, freelancereille tai harrastajille.
- KISS**-filosofia: Arch on suunniteltu yksinkertaiseksi, kevyeksi ja tehokkaaksi. Se tarjoaa vain välttämättömät asiat, joten voit rakentaa ympäristösi à la carte.
- Pacman**-paketinhallinta: Pacman on nopea, luotettava ja hyvin suunniteltu paketinhallintaohjelma. Se mahdollistaa ohjelmistojen tehokkaan asentamisen ja päivittämisen ja hallitsee riippuvuudet tarkasti.
- Kattava dokumentaatio ja aktiivinen yhteisö**: [Arch Wiki](https://wiki.archlinux.org) on luultavasti yksi Linux-maailman parhaista teknisistä dokumentaatiosta. Se on kultakaivos sen ymmärtämiseen, mitä olet tekemässä. Yhteisö, joka koostuu enimmäkseen kokeneista profiileista, on hyvin aktiivinen ja voi auttaa sinua, jos jäät jumiin, edellyttäen, että olet tehnyt hieman tutkimusta etukäteen.



## Asennus ja konfigurointi



### Edellytykset



Tarvittavat materiaalit:





- Vähintään **8 Gt:n kokoinen USB-tikku**
- vähintään 2 GB** RAM-muistia
- Tietokone, jossa on vähintään 20 Gt vapaata levytilaa



### Lataa



![0_1](assets/fr/01.webp)



Vuodesta 2017 lähtien Arch Linux ei enää tue 32-bittisiä arkkitehtuureja. Vain 64-bittiset versiot ovat saatavilla.





- Käy [virallisella verkkosivustolla](https://mir.archlinux.fr/iso/latest/) lataamassa ISO-kuvan uusin virallinen versio.



### Luo käynnistettävä avain



Voit luoda käynnistettävän USB-muistitikun käyttämällä työkalua, kuten **Balena Etcher**:





- Lataa Balena Etcher [virallisilta verkkosivuilta](https://etcher.balena.io).
- Käynnistä ohjelmisto ja valitse Arch Linuxin ISO-kuva.
- Valitse kohdelaitteeksi USB-muistitikku.
- Napsauta **Flash** aloittaaksesi käynnistettävän avaimen luomisen.



![0_2](assets/fr/02.webp)



## Arch Linuxin asentaminen



## Käynnistäminen USB-muistitikulta





- Sammuta tietokone kokonaan
- Kytke käynnistettävä USB-levy
- Käynnistä uudelleen ja siirry BIOS/UEFI-käyttöjärjestelmään painamalla **F1**, **Escape**, **F9** jne. (mallista riippuen)
- Valitse käynnistysvalikossa USB-levy käynnistyslaitteeksi. Jos kaikki on asetettu oikein, pääset Arch Linux Interface:n käynnistysnäyttöön.



## Asennuksen käynnistäminen



Valitse käynnistysnäytössä ensimmäinen vaihtoehto asennuksen käynnistämiseksi. Huomaa, että Arch Linux ei tarjoa graafista asennusohjelmaa. Kun asennus on käynnistetty, pääset pääkäyttäjätilassa olevaan päätelaitteeseen.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Näppäimistön kokoonpano



Voit näyttää käytettävissä olevat asettelut painikkeella:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Lataa sitten asettelu:



```shell
loadkeys nom-disposition
```



Oletusarvoisesti näppäimistö on englanninkielinen (qwerty), mutta voit vaihtaa `azerty`-näppäimistöksi `loadkeys fr`:llä.



### Päivämäärän ja kellonajan asettaminen



Arch Linux käyttää `timedatectl`-työkalua järjestelmän kellon hallintaan.



![0_7](assets/fr/07.webp)





- Aseta aikavyöhyke valitsemalla:


```shell
timedatectl set-timezone Europe/Paris
```





- Tarkista, että automaattinen synkronointi on käytössä:


```shell
timedatectl status
```





- Aktivoi se tarvittaessa:


```shell
timedatectl set-ntp true
```




Tämä aktivoi NTP-protokollan, joka mahdollistaa automaattisen synkronoinnin aikapalvelimien kanssa. Tämä vaihe on tärkeä, jotta vältytään päivämäärävirheiltä, kun asennetaan paketteja tai määritetään SSL-varmenteita myöhemmin.



### Levyn osiointi





- Tarkista, käynnistyykö järjestelmäsi **UEFI**- tai **BIOS**-ohjelmalla:



```shell
ls /sys/firmware/efi
```



Jos tiedosto on olemassa, olet **UEFI**:ssä. Muussa tapauksessa olet **BIOS (Legacy)**:ssä.




- Luettele käytettävissä olevat levyt:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Käynnistä Partition Manager:



```shell
cfdisk /dev/nom-du-disque
```



Valitse **GPT**, jos olet UEFI:ssä, **DOS**, jos olet BIOS:ssa.



![0_9](assets/fr/09.webp)



#### Pisteet luoda




- UEFI**-tilassa



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- BIOSissa



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Valitse **Kirjoita**, kirjoita **Kyllä** ja sitten **Lopeta**.



### Osioiden alustaminen





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



### Järjestelmän perusasennus



Kiinnitä **juuri-osio**:





- BIOS:


```shell
mount /dev/sda2 /mnt
```




- uEFI:ssä:


```shell
mount /dev/sda3 /mnt
```



Asenna sitten olennaiset paketit:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate **fstab**-tiedosto, jonka avulla käyttöjärjestelmä voi automaattisesti hallita osioiden asentamista jokaisella käynnistyskerralla ilman manuaalisia toimenpiteitä:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Siirry **Chroot**-ympäristöön:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Järjestelmän kokoonpano





- Asenna tekstieditori muokkaamaan:



```shell
pacman -S vim
```





- Aseta kieli:


Muokkaa `/etc/locale.gen` ja poista kommentti riviltä `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Aseta koneen nimi:



```shell
echo nom_machine > /etc/hostname
```





- Aseta pääkäyttäjän salasana:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### GRUBin asentaminen



Asenna:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Kun olet ladannut sen, sinun on asennettava se levyosion muodon mukaan.




- **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Viimeistely





- Poistu chroot-ympäristöstä:


```shell
exit
```





- Poista osiot:


```shell
umount -R /mnt
```





- Käynnistä uudelleen:


```shell
reboot
```



Käynnistettäessä kirjaudu sisään **juuritunnuksellasi** ja salasanallasi.



![0_18](assets/fr/18.webp)


## Verkkoyhteys uudelleenkäynnistyksen jälkeen



Voi käydä niin, että verkkoyhteys ei ole aktiivinen uudelleenkäynnistyksen yhteydessä. Voit luetella liitännät komennolla:



```shell
ip link
```



Määritä sitten Interface -verkko syöttämällä päätelaitteeseen seuraava teksti



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface-grafiikka (GNOME)



Oletusarvoisesti **Arch Linux** ei sisällä graafista Interface:ää. Voit lisätä sellaisen:



Päivitä järjestelmä:



```shell
pacman -Syu
```



Asenna **Xorg** seuraavalla komennolla ja paina enteriä joka kerta, jotta oletusvalinnat säilyvät:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Asenna **GNOME** seuraavalla komennolla ja kirjoita joka kerta pitääksesi oletusvalinnat:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Aktivoi **session manager**:



```shell
systemctl enable gdm
systemctl start gdm
```



Järjestelmä käynnistyy automaattisesti uudelleen, ja saat Interface:n graafisen kirjautumisen näkyviin. Kirjaudu sisään pääkäyttäjänimellä ja salasanalla.



![0_21](assets/fr/21.webp)



## Käyttäjän luominen



Kun olet **Interface GNOME**:ssa, sinun on luotava uusi käyttäjä paremman turvallisuuden ja turvallisemman, riskittömän käytön takaamiseksi. Siirry sovelluksiin ja valitse "konsoli"-vaihtoehto käynnistääksesi päätelaitteen.





- Lisää käyttäjä:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Asenna **sudo**:


```shell
pacman -S sudo
```





- Aktivoi **sudo-oikeudet**:



```shell
EDITOR=nano visudo
```





- Poista sitten kommentti riviltä:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Käynnistä järjestelmä uudelleen ja kirjaudu sisään käyttäjätunnuksellasi.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Ohjelmiston asentaminen



Koska Arch Linux on minimalistinen, monia ohjelmistoja ei asenneta oletusarvoisesti. Voit lisätä tarvitsemasi tiedostot kirjoittamalla seuraavan komennon:



```shell
pacman -S nom_du_paquet_a_installe
```



Voit esimerkiksi asentaa **nano**-tekstieditorin kirjoittamalla:



```shell
pacman -S nano
```



Jos haluat asentaa kevyen verkkoselaimen, kuten `firefox`, käytä:



```shell
pacman -S firefox
```



Lopuksi, jos haluat lisätä keskeiset verkkotyökalut, kuten `net-tools`, komento on:



```shell
pacman -S net-tools
```



Älä unohda, että voit asentaa useita paketteja yhdellä komennolla listaamalla ne erikseen:



```shell
pacman -S vim firefox net-tools
```



Arch Linux erottuu edukseen huomattavan vakauden, minimalistisen filosofian ja vankkuuden ansiosta, mikä tekee siitä ihanteellisen valinnan kehitysympäristöihin. Se tarjoaa vain välttämättömät asiat, joten se tarjoaa kevyen ja suorituskykyisen perustan, jota on helppo mukauttaa omiin tarpeisiisi. Tämä minimalistinen lähestymistapa suosii myös järjestelmän parempaa hallintaa, mikä vahvistaa turvallisuutta rajoittamalla hyökkäyspintaa. Aktiivisen yhteisönsä ja kattavan dokumentaationsa ansiosta Arch Linux voi auttaa sinua luomaan turvallisen, joustavan ympäristön, joka on optimoitu ammattimaiseen kehitykseen.



Jos olet nauttinut Arch Linuxin käytön aloittamisesta, rakastat varmasti opastustamme **Fedora OS**:stä, joka on modulaarinen, turvallinen ja vankka käyttöjärjestelmä, joka mukautuu tarpeisiisi ja käyttötarkoituksiisi.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1