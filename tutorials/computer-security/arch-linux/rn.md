---
name: Arch Linux
description: Ivyo gukwiragiza bifise ubushobozi buke, bikora cane, vyateguwe hakurikijwe ubuhinga bwa KISS.
---

![cover](assets/cover.webp)



Arch Linux ni distribution izwi cane kubera ubukomezi bwayo, ubushobozi bwayo n’ubushobozi bwo guhindura, cane cane ku bijanye n’iterambere. Itanga ugushikama kwiza cane n’ibidukikije vyiza vyo guhindura ibintu, bishigikiwe n’umucungerezi w’amapaki yihuta cane kandi yizigirwa. Filozofiya yayo ishingiye ku ngingo ya **KISS** (*Keep It Simple, Stupid*): gutanga uburyo bwo gutanga amakuru yoroshe, yoroshe, yihuta kandi ataco akora, mu gihe umuntu asiga umwidegemvyo mwinshi ku muntu akoresha.



## Ni kuki uhisemwo Arch Linux?





- Inkomoko y’ubuntu kandi yuguruye**: Cokimwe n’ibindi bikoresho vyinshi vya Linux, Arch Linux ni ubuntu rwose. Nta mahera y’uruhusha, ivyo bikaba bituma ari ihitamwo ryiza cane ku banyeshure, abakora ibikorwa vy’ubuhinga canke ababikunda.
- KISS** filozofiya: Arch yakozwe kugira ngo ibe yoroshe, yoroshe kandi ikore neza. Itanga gusa ivy’ingenzi, bikagufasha kwubaka ibidukikije vyawe à la carte.
- Pacman** umuyobozi w’amapaki: Pacman ni umuyobozi w’amapaki yihuta, yizigirwa kandi ateguwe neza. Bishoboza gushiramwo neza no guhindura porogarama, no gucunga neza ivyo bishingiyeko.
- Ivyanditswe vyuzuye n'umuryango ukora**: [Wiki ya Arch](https://wiki.archlinux.org) birashoboka ko ari imwe mu nyandiko nziza cane z'ubuhinga kw'isi ya Linux. Ni icumbi ry’inzahabu ryo gutahura ivyo uriko urakora. Umuryango, ahanini ugizwe n’abantu bazi utuntu n’utundi, urakora cane kandi urashobora kugufasha iyo uhagaze, igihe cose wakoze ubushakashatsi bukeyi imbere y’aho.



## Gushiramwo no gutunganya



### Ibisabwa



Ibikoresho bisabwa:





- Urufunguzo rwa USB rwo nibura **8 GB**
- 2 GB** RAM n'imiburiburi
- Mudasobwa ifise nibura 20 GB z'umwanya kuri disiki



### Gukurura



![0_1](assets/fr/01.webp)



Kuva mu mwaka w’2017, Arch Linux ntigishobora gufasha ubuhinga bwo kwubaka bufise ibice 32. Verisiyo z’ibice 64 gusa ni zo ziboneka.





- Sura [urubuga rwemewe](https://mir.archlinux.fr/iso/latest/) kugira ngo ubone verisiyo nshasha yemewe y’ishusho ya ISO.



### Rema urufunguzo rwo gufungura



Kugira ngo ureme umuduga wa USB ushobora gufunguka, ushobora gukoresha igikoresho nka **Balena Etcher**:





- Gukuraho igitabu ca Balena ku rubuga rwemewe (https://etcher.balena.io).
- Tangaza porogaramu, uhitemwo ishusho ya Arch Linux ISO.
- Hitamwo urufunguzo rwawe rwa USB nk'igikoresho ushaka.
- Fyonda kuri **Flash** kugira utangure kurema urufunguzo rwo gufungura.



![0_2](assets/fr/02.webp)



## Gushiramwo Arch Linux



## Gufungura ku rufunguzo rwa USB





- Zima mudasobwa yawe burundu
- Shiramwo urufunguzo rwa USB rushobora gutangura
- Subira ufungure maze winjire muri BIOS/UEFI ukanda **F1**, **Escape**, **F9**, n'ibindi (bivanye n'umuderi wawe)
- Mu nzira y’ugutangura, hitamwo urufunguzo rwa USB nk’igikoresho co gutangura. Niba vyose vyateguwe neza, uzojanwa ku rubuga rwo gutangura rwa Arch Linux Interface.



## Gutanguza gushiramwo



Ku rubuga rwo gutangura, hitamwo uburyo bwa mbere bwo gutangura gushiramwo. Zirikana ko Arch Linux idatanga igikoresho co gushiramwo ibishushanyo. Iyo umaze gutangura, uzojanwa ku terminal iri mu buryo bw’imizi.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Imiterere ya klavye



Ushobora kwerekana imiterere iriho na:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Hanyuma ushiremwo imiterere na:



```shell
loadkeys nom-disposition
```



Ku mburabuzi, klavye iri mu congereza (qwerty), ariko ushobora guhindukira ukaja kuri `azerty` ukoresheje `loadkeys fr`.



### Gushinga itariki n'isaha



Arch Linux ikoresha igikoresho ca `timedatectl` kugira ngo igenzure isaha ya sisitemu.



![0_7](assets/fr/07.webp)





- Gushinga isaha yawe na:


```shell
timedatectl set-timezone Europe/Paris
```





- Suzuma ko uguhuza kwihuta gukoreshwa na:


```shell
timedatectl status
```





- Bikoreshe iyo bikenewe:


```shell
timedatectl set-ntp true
```




Ivyo bituma NTP, ni ukuvuga umurongo w’uguhuza n’ibikoresho vy’igihe bikora. Iyi ntambwe ni ngirakamaro kugira ngo wirinde amakosa y'itariki igihe ushiramwo amapaki canke utunganya ivyemezo vya SSL mu nyuma.



### Gucapura disiki





- Suzuma nimba sisitemu yawe ifungura muri **UEFI** canke **BIOS** na:



```shell
ls /sys/firmware/efi
```



Niba dosiye iriho, uri muri **UEFI**. Ahandi ho, uri muri **BIOS (Iragi)**.




- Urutonde rw'amadisike ariho:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Tangira Umucungerezi w'Imigabane:



```shell
cfdisk /dev/nom-du-disque
```



Hitamwo **GPT** iyo uri muri UEFI, **DOS** iyo uri muri BIOS.



![0_9](assets/fr/09.webp)



#### Amanota yo kurema




- Mu buryo bwa **UEFI**



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- Muri BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Hitamwo **Wandike**, wandike **egome**, hanyuma **Reka**.



### Guhindura imigabane





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



### Gushiramwo sisitemu y'ishimikiro



Gutera **imizi** y'umugabane:





- Kuri BIOS:


```shell
mount /dev/sda2 /mnt
```




- kuri UEFI:


```shell
mount /dev/sda3 /mnt
```



Hanyuma ushiremwo amapaki y'ingenzi:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate dosiye **fstab**, ishobora gutuma sisitemu ikoresha ishobora gucungera ubwayo ugushiraho imigabane ku gihe cose utangura, ataco umuntu akora:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Injira mu bidukikije vya **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Gutunganya sisitemu





- Shiraho umuhinduzi w'inyandiko kugira ngo uhindure:



```shell
pacman -S vim
```





- Gushinga ururimi:


Guhindura `/n'ibindi/akarere.gen` hanyuma ukureho ibitekerezo ku murongo `ru_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Gushinga izina ry'imashini:



```shell
echo nom_machine > /etc/hostname
```





- Gushinga ijambobanga ry'umuzi:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Gushiramwo GRUB



Shiraho:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Iyo umaze kuyikurako, ukeneye kuyishiramwo ukurikije uburyo bwo gucapura disiki.




- Ku **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Ku **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Gusozera





- Sohoka mu bidukikije vya chroot:


```shell
exit
```





- Kuraho imigabane:


```shell
umount -R /mnt
```





- Gusubira gutangura:


```shell
reboot
```



Mu gutangura, winjiremwo ukoresheje **umuzi** wawe n'ijambobanga ryawe.



![0_18](assets/fr/18.webp)


## Ihuriro ry'urubuga inyuma yo gusubira gufungura



Bishobora gushika ko ata nzira y’urubuga ikora iyo usubiye gutangura. Ushobora gutanga urutonde rw'ibigaragara na:



```shell
ip link
```



Hanyuma ushireho urubuga rwa Interface winjiza umwandiko ukurikira muri terminal .



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Ibishushanyo vya Interface (GNOME)



Ku mburabuzi, **Arch Linux** nta gishushanyo Interface irimwo. Kugira ngo wongereko kimwe:



Kuvugurura sisitemu:



```shell
pacman -Syu
```



Shiraho **Xorg** n'itegeko rikurikira hanyuma ukande enter igihe cose kugira ngo ugume ufise amahitamwo:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Shiraho **GNOME** n'itegeko rikurikira maze winjize igihe cose kugira ngo ugume ufise amahitamwo:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Gukoresha **umuyobozi w'ikiganiro**:



```shell
systemctl enable gdm
systemctl start gdm
```



Sisitemu irasubira gukora ubwayo maze ukabona igishushanyo c’injira ca Interface. Injira n'izina ry'umuzi n'ijambobanga.



![0_21](assets/fr/21.webp)



## Gukora umukoresha



Igihe umaze gushika muri **Interface GNOME**, uzokenera kurema umukoresha mushasha kugira ngo ukoreshe neza kandi ukoreshe ata ngorane. Injira mu bikoresho maze uhitemwo "console" kugira ngo utangure terminal.





- Kwongerako umukoresha:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Shiraho **sudo**:


```shell
pacman -S sudo
```





- Gukoresha uburenganzira bwa **sudo**:



```shell
EDITOR=nano visudo
```





- Hanyuma ushireho ibitekerezo kuri uwo murongo:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Subira ufungure sisitemu maze winjiremwo ukoresheje izina ryawe.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Gushiramwo porogaramu



Kubera ko Arch Linux ari minimalist, porogarama nyinshi ntizishirwamwo ku buryo busanzwe. Wongereko ivyo ukeneye, wandike itegeko rikurikira:



```shell
pacman -S nom_du_paquet_a_installe
```



Nk'akarorero, kugira ngo ushiremwo **nano** umuhinduzi w'inyandiko, ushobora kwandika:



```shell
pacman -S nano
```



Kugira ngo ushireho umucukumbuzi w'urubuga yoroshe nka `firefox`, koresha:



```shell
pacman -S firefox
```



Ubwanyuma, niwaba ushaka kwongerako ibikoresho vy'ingenzi vy'urubuga nka `net-tools`, itegeko ryoba:



```shell
pacman -S net-tools
```



Ntukibagire ko ushobora gushiramwo amapaki menshi mw'itegeko rimwe mu kuyashira ku rutonde atandukanye:



```shell
pacman -S vim firefox net-tools
```



Arch Linux igaragara kubera ugushikama kwayo gutangaje, filozofiya y’ubuhinga bukeyi n’ubukomezi bwayo, bikaba biyigira ihitamwo ryiza ku bidukikije vy’iterambere. Mu gutanga ivy’ingenzi gusa, itanga umushinge woroshe, ukora neza cane, woroshe guhindura bivanye n’ivyo ukeneye. Ubwo buryo bw’ubuhinga bukeyi buratuma kandi umuntu ashobora kugenzura cane iyo nzira, bugakomeza umutekano mu kugabanya aho umuntu ashobora gutera. Kubera umuryango wayo ukora n’inyandiko zishitse, Arch Linux irashobora kugufasha kurema ikibanza gitekanye, gishobora guhinduka gibereye iterambere ry’umwuga.



Niba warashimishijwe no gutangura gukoresha Arch Linux, uzokunda inyigisho yacu ku **Fedora OS**, ubuhinga bwo gukoresha bufise ibice, butekanye kandi bukomeye bujanye n’ivyo ukeneye n’ivyo ukoresha.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1