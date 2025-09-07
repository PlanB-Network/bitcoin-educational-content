---
name: Arch Linux
description: Minimalistická, vysoce výkonná distribuce navržená podle filozofie KISS.
---

![cover](assets/cover.webp)



Arch Linux je distribuce proslulá svou robustností, výkonem a přizpůsobivostí, zejména pro vývojové účely. Nabízí vynikající stabilitu a prostředí vhodné pro přizpůsobení, podporované extrémně rychlým a spolehlivým správcem balíčků. Jeho filozofie je založena na principu **KISS** (*Keep It Simple, Stupid*): nabídnout lehkou, jednoduchou, rychlou a nenáročnou distribuci a zároveň ponechat uživateli velkou volnost.



## Proč si vybrat Arch Linux?





- Zdarma a s otevřeným zdrojovým kódem**: Arch Linux je stejně jako většina linuxových distribucí zcela zdarma. Neplatí se za něj žádné licenční poplatky, takže je vynikající volbou pro studenty, nezávislé pracovníky nebo nadšence.
- Filozofie KISS**: Arch je navržen tak, aby byl jednoduchý, lehký a efektivní. Poskytuje pouze to nejnutnější a umožňuje vám vytvořit si prostředí à la carte.
- Správce balíčků Pacman**: Pacman je rychlý, spolehlivý a dobře navržený správce balíčků. Umožňuje efektivní instalaci a aktualizaci softwaru a precizně spravuje závislosti.
- Komplexní dokumentace a aktivní komunita**: [Arch Wiki](https://wiki.archlinux.org) je pravděpodobně jednou z nejlepších technických dokumentací ve světě Linuxu. Je to zlatý důl pro pochopení toho, co děláte. Komunita složená převážně ze zkušených profilů je velmi aktivní a může vám pomoci, pokud se zaseknete, za předpokladu, že jste si předtím udělali menší průzkum.



## Instalace a konfigurace



### Předpoklady



Potřebné materiály:





- Klíč USB o velikosti alespoň **8 GB**
- minimálně 2 GB** RAM
- Počítač s alespoň 20 GB volného místa na disku



### Stáhnout



![0_1](assets/fr/01.webp)



Od roku 2017 již Arch Linux nepodporuje 32bitové architektury. K dispozici jsou pouze 64bitové verze.





- Navštivte [oficiální webové stránky](https://mir.archlinux.fr/iso/latest/) a stáhněte si nejnovější oficiální verzi obrazu ISO.



### Vytvoření zaváděcího klíče



K vytvoření bootovacího USB flash disku můžete použít nástroj, jako je **Balena Etcher**:





- Balena Etcher si můžete stáhnout z [oficiální webové stránky](https://etcher.balena.io).
- Spusťte software a vyberte obraz ISO systému Arch Linux.
- Jako cílové zařízení vyberte klíč USB.
- Kliknutím na **Flash** zahájíte vytváření zaváděcího klíče.



![0_2](assets/fr/02.webp)



## Instalace systému Arch Linux



## Zavedení systému na klíči USB





- Úplné vypnutí počítače
- Připojení zaváděcího klíče USB
- Restartujte počítač a vstupte do systému BIOS/UEFI stisknutím tlačítek **F1**, **Escape**, **F9** atd. (v závislosti na modelu)
- Ve spouštěcí nabídce vyberte jako spouštěcí zařízení klíč USB. Pokud je vše správně nastaveno, zobrazí se spouštěcí obrazovka Arch Linuxu Interface.



## Spuštění instalace



Na spouštěcí obrazovce vyberte první možnost pro spuštění instalace. Všimněte si, že Arch Linux nenabízí grafický instalátor. Po spuštění budete přesměrováni do terminálu v režimu roota.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Konfigurace klávesnice



Dostupná rozložení můžete zobrazit pomocí:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Poté načtěte rozložení pomocí:



```shell
loadkeys nom-disposition
```



Ve výchozím nastavení je klávesnice anglická (qwerty), ale můžete ji přepnout na `azerty` pomocí `loadkeys fr`.



### Nastavení data a času



Arch Linux používá ke správě systémových hodin nástroj `timedatectl`.



![0_7](assets/fr/07.webp)





- Nastavení časového pásma pomocí:


```shell
timedatectl set-timezone Europe/Paris
```





- Zkontrolujte, zda je povolena automatická synchronizace pomocí:


```shell
timedatectl status
```





- V případě potřeby jej aktivujte:


```shell
timedatectl set-ntp true
```




Tím se aktivuje protokol NTP pro automatickou synchronizaci s časovými servery. Tento krok je důležitý, abyste se vyhnuli chybám v datu při pozdější instalaci balíčků nebo konfiguraci certifikátů SSL.



### Rozdělení disku





- Zkontrolujte, zda se váš systém spouští v **UEFI** nebo **BIOS** s:



```shell
ls /sys/firmware/efi
```



Pokud soubor existuje, jste v **UEFI**. V opačném případě jste v systému **BIOS (Legacy)**.




- Seznam dostupných disků:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Spusťte Správce diskových oddílů:



```shell
cfdisk /dev/nom-du-disque
```



Pokud používáte UEFI, vyberte **GPT**, pokud používáte BIOS, vyberte **DOS**.



![0_9](assets/fr/09.webp)



#### Vytvoření skóre




- V režimu UEFI**



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- V systému BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Vyberte možnost **Zapsat**, zadejte **ano** a poté **Ukončit**.



### Formátování oddílů





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



### Základní instalace systému



Připojte **kořenový** oddíl:





- V systému BIOS:


```shell
mount /dev/sda2 /mnt
```




- na UEFI:


```shell
mount /dev/sda3 /mnt
```



Poté nainstalujte základní balíčky:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate soubor **fstab**, který umožňuje operačnímu systému automaticky spravovat připojování oddílů při každém spuštění systému bez nutnosti ručního zásahu:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Vstupte do prostředí **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Konfigurace systému





- Nainstalujte si textový editor pro úpravu:



```shell
pacman -S vim
```





- Nastavení jazyka:


Upravte `/etc/locale.gen` a odkomentujte řádek `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Nastavení názvu stroje:



```shell
echo nom_machine > /etc/hostname
```





- Nastavení hesla roota:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Instalace systému GRUB



Nainstalujte:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Po stažení je třeba jej nainstalovat podle formátu diskového oddílu.




- Pro systém **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Pro **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Finalizace





- Ukončení prostředí chroot:


```shell
exit
```





- Odstraňte oddíly:


```shell
umount -R /mnt
```





- Restartování:


```shell
reboot
```



Při spuštění se přihlaste pomocí přihlašovacího jména a hesla **root**.



![0_18](assets/fr/18.webp)


## Připojení k síti po restartu



Může se stát, že při restartu nebude aktivní žádné síťové připojení. Rozhraní můžete vypsat pomocí:



```shell
ip link
```



Poté nakonfigurujte síť Interface zadáním následujícího textu do terminálu



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Grafika Interface (GNOME)



Ve výchozím nastavení neobsahuje **Arch Linux** grafický modul Interface. Chcete-li jej přidat:



Aktualizace systému:



```shell
pacman -Syu
```



Nainstalujte **Xorg** pomocí následujícího příkazu a pokaždé stiskněte enter, abyste zachovali výchozí volby:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Nainstalujte **GNOME** pomocí následujícího příkazu a pokaždé zadejte, abyste zachovali výchozí volby:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Aktivujte správce **sekcí**:



```shell
systemctl enable gdm
systemctl start gdm
```



Systém se automaticky restartuje a zobrazí se grafické přihlášení Interface. Přihlaste se pomocí uživatelského jména a hesla root.



![0_21](assets/fr/21.webp)



## Vytvoření uživatele



Jakmile se dostanete do prostředí **Interface GNOME**, musíte si vytvořit nového uživatele, abyste měli větší bezpečnost a mohli jej používat bezpečněji a bez rizika. Vstupte do aplikací a zvolte možnost "konzola" pro spuštění terminálu.





- Přidání uživatele:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Instalace **sudo**:


```shell
pacman -S sudo
```





- Aktivujte práva **sudo**:



```shell
EDITOR=nano visudo
```





- Pak odkomentujte řádek:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Restartujte systém a přihlaste se pod svým uživatelským jménem.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Instalace softwaru



Protože je Arch Linux minimalistický, mnoho softwaru není ve výchozím nastavení nainstalováno. Chcete-li přidat to, co potřebujete, zadejte následující příkaz:



```shell
pacman -S nom_du_paquet_a_installe
```



Chcete-li například nainstalovat textový editor **nano**, můžete zadat příkaz:



```shell
pacman -S nano
```



Chcete-li nainstalovat lehký webový prohlížeč, například `firefox`, použijte:



```shell
pacman -S firefox
```



Pokud chcete přidat základní síťové nástroje, jako je `net-tools`, příkaz bude:



```shell
pacman -S net-tools
```



Nezapomeňte, že jedním příkazem můžete nainstalovat několik balíčků tak, že je uvedete v samostatném seznamu:



```shell
pacman -S vim firefox net-tools
```



Arch Linux vyniká pozoruhodnou stabilitou, minimalistickou filozofií a robustností, což z něj činí ideální volbu pro vývojová prostředí. Poskytuje pouze to nejnutnější a nabízí tak lehký, vysoce výkonný základ, který lze snadno přizpůsobit vašim specifickým potřebám. Tento minimalistický přístup také upřednostňuje větší kontrolu nad systémem a posiluje bezpečnost omezením prostoru pro útoky. Díky aktivní komunitě a vyčerpávající dokumentaci vám Arch Linux pomůže vytvořit bezpečné a flexibilní prostředí optimalizované pro profesionální vývoj.



Pokud se vám líbily začátky s Arch Linuxem, určitě se vám bude líbit náš návod na **Fedora OS**, modulární, bezpečný a robustní operační systém, který se přizpůsobí vašim potřebám a způsobům použití.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1