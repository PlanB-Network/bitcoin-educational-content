---
name: Arch Linux
description: Usambazaji mdogo, wa utendaji wa juu ulioundwa kulingana na falsafa ya KISS.
---

![cover](assets/cover.webp)



Arch Linux ni usambazaji unaojulikana kwa uimara, utendakazi na uwezo wake wa kubadilika, hasa kwa madhumuni ya maendeleo. Inatoa uthabiti bora na mazingira yanayofaa kubinafsisha, inayoungwa mkono na msimamizi wa kifurushi wa haraka sana na anayetegemewa. Falsafa yake inategemea kanuni ya **KISS** (*Iweke Rahisi, Kijinga*): kutoa usambazaji mwepesi, rahisi, wa haraka na usio na vitu vingi, huku ukiacha uhuru mwingi kwa mtumiaji.



## Kwa nini uchague Arch Linux?





- Chanzo huria na huria**: Kama ugawaji mwingi wa Linux, Arch Linux ni bure kabisa. Hakuna ada za leseni, na kuifanya kuwa chaguo bora kwa wanafunzi, wafanyikazi wa kujitegemea au wapendaji.
- Falsafa ya KISS**: Arch imeundwa kuwa rahisi, nyepesi na bora. Inatoa tu mambo muhimu, hukuruhusu kujenga mazingira yako à la carte.
- Kidhibiti kifurushi cha Pacman**: Pacman ni meneja wa kifurushi wa haraka, anayetegemewa na iliyoundwa vizuri. Inawezesha usakinishaji na usasishaji bora wa programu, na kudhibiti utegemezi kwa usahihi.
- Uhifadhi wa kina na jumuiya inayotumika**: [Arch Wiki](https://wiki.archlinux.org) pengine ni mojawapo ya hati bora zaidi za kiufundi katika ulimwengu wa Linux. Ni mgodi wa dhahabu kwa kuelewa unachofanya. Jumuiya, inayojumuisha wasifu wenye uzoefu, ina shughuli nyingi na inaweza kukusaidia ikiwa utakwama, mradi tu umefanya utafiti kidogo hapo awali.



## Ufungaji na usanidi



### Masharti



Nyenzo zinazohitajika:





- Kitufe cha USB cha angalau **8 GB**
- 2 GB** kiwango cha chini cha RAM
- Kompyuta iliyo na angalau GB 20 ya nafasi ya bure ya diski



### Pakua



![0_1](assets/fr/01.webp)



Tangu 2017, Arch Linux haitumii tena usanifu wa 32-bit. Matoleo ya 64-bit pekee yanapatikana.





- Tembelea [tovuti rasmi](https://mir.archlinux.fr/iso/latest/) ili kupakua toleo rasmi la hivi punde la picha ya ISO.



### Unda ufunguo wa bootable



Ili kuunda kiendeshi cha USB cha bootable, unaweza kutumia zana kama **Balena Etcher**:





- Pakua Balena Etcher kutoka [tovuti rasmi](https://etcher.balena.io).
- Zindua programu, chagua picha ya Arch Linux ISO.
- Chagua ufunguo wako wa USB kama kifaa lengwa.
- Bofya kwenye **Mweko** ili kuanza kuunda ufunguo unaoweza kuwashwa.



![0_2](assets/fr/02.webp)



## Inasakinisha Arch Linux



## Inawasha kitufe cha USB





- Zima kompyuta yako kabisa
- Chomeka ufunguo wa USB unaoweza kuwashwa
- Washa upya na uingize BIOS/UEFI kwa kubofya **F1**, **Escape**, **F9**, n.k. (kulingana na mtindo wako)
- Katika menyu ya kuwasha, chagua kitufe cha USB kama kifaa cha kuwasha. Ikiwa kila kitu kimewekwa kwa usahihi, utapelekwa kwenye skrini ya boot ya Arch Linux Interface.



## Kuzindua ufungaji



Kwenye skrini ya boot, chagua chaguo la kwanza ili kuzindua usakinishaji. Kumbuka kuwa Arch Linux haitoi kisakinishi cha picha. Mara baada ya kuzinduliwa, utapelekwa kwenye terminal katika hali ya mizizi.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Usanidi wa kibodi



Unaweza kuonyesha muundo unaopatikana na:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Kisha pakia mpangilio na:



```shell
loadkeys nom-disposition
```



Kwa chaguo-msingi, kibodi iko kwa Kiingereza (qwerty), lakini unaweza kubadili hadi `azerty` kwa `loadkeys fr`.



### Kuweka tarehe na wakati



Arch Linux hutumia zana ya `timedatectl` kudhibiti saa ya mfumo.



![0_7](assets/fr/07.webp)





- Weka saa za eneo lako na:


```shell
timedatectl set-timezone Europe/Paris
```





- Angalia kuwa ulandanishi otomatiki umewezeshwa na:


```shell
timedatectl status
```





- Iwashe ikiwa ni lazima:


```shell
timedatectl set-ntp true
```




Hii inawasha NTP, itifaki ya ulandanishi otomatiki na seva za wakati. Hatua hii ni muhimu ili kuepuka hitilafu za tarehe wakati wa kusakinisha vifurushi au kusanidi vyeti vya SSL baadaye.



### Ugawaji wa diski





- Angalia ikiwa mfumo wako unaanza katika **UEFI** au **BIOS** na:



```shell
ls /sys/firmware/efi
```



Ikiwa faili iko, uko kwenye **UEFI**. Vinginevyo, uko kwenye **BIOS (Legacy)**.




- Orodhesha diski zinazopatikana:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Anza Kidhibiti cha Kugawanya:



```shell
cfdisk /dev/nom-du-disque
```



Chagua **GPT** ikiwa uko kwenye UEFI, **DOS** ikiwa uko kwenye BIOS.



![0_9](assets/fr/09.webp)



#### Alama za kuunda




- Katika hali ya UEFI**



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- Katika BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Chagua **Andika**, chapa **ndiyo**, kisha **Toka**.



### Uumbizaji partitions





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



### Ufungaji wa mfumo wa msingi



Panda kizigeu cha **mizizi**:





- Kwenye BIOS:


```shell
mount /dev/sda2 /mnt
```




- kwenye UEFI:


```shell
mount /dev/sda3 /mnt
```



Kisha sasisha vifurushi muhimu:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate faili ya **fstab**, ambayo huwezesha mfumo wa uendeshaji kudhibiti kiotomatiki uwekaji kizigeu kwenye kila buti, bila uingiliaji kati wa mikono:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Weka mazingira ya **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Usanidi wa mfumo





- Sakinisha kihariri maandishi ili kuhariri:



```shell
pacman -S vim
```





- Weka lugha:


Hariri `/etc/locale.gen` kisha ubatilishe mstari `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Weka jina la mashine:



```shell
echo nom_machine > /etc/hostname
```





- Weka nenosiri la mizizi:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Inasakinisha GRUB



Sakinisha:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Mara baada ya kupakuliwa, unahitaji kuiweka kulingana na muundo wa kugawanya diski.




- Kwa **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Kwa **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Kuhitimisha





- Ondoka kwenye mazingira ya chroot:


```shell
exit
```





- Ondoa partitions:


```shell
umount -R /mnt
```





- Anzisha upya:


```shell
reboot
```



Unapoanzisha, ingia na kuingia kwa **root** na nenosiri lako.



![0_18](assets/fr/18.webp)


## Muunganisho wa mtandao baada ya kuwasha upya



Inaweza kutokea kwamba hakuna muunganisho wa mtandao unaofanya kazi kwenye kuwasha upya. Unaweza kuorodhesha miingiliano na:



```shell
ip link
```



Kisha usanidi mtandao wa Interface kwa kuingiza maandishi yafuatayo kwenye terminal



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Michoro ya Interface (GNOME)



Kwa chaguomsingi, **Arch Linux** haina mchoro Interface. Ili kuongeza moja:



Sasisha mfumo:



```shell
pacman -Syu
```



Sakinisha **Xorg** kwa amri ifuatayo na ubonyeze ingiza kila wakati ili kuweka chaguo-msingi:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Sakinisha **GNOME** kwa amri ifuatayo na uweke kila wakati ili kuweka chaguo-msingi:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Washa **kidhibiti kikao**:



```shell
systemctl enable gdm
systemctl start gdm
```



Mfumo unaanza upya kiotomatiki na unapata kuingia kwa picha ya Interface. Ingia na mzizi jina la mtumiaji na nenosiri.



![0_21](assets/fr/21.webp)



## Kuunda mtumiaji



Ukiwa katika **Interface GNOME**, utahitaji kuunda mtumiaji mpya kwa usalama zaidi na matumizi salama, yasiyo na hatari. Ingiza programu na uchague chaguo la "console" ili kuzindua terminal.





- Ongeza mtumiaji:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Sakinisha **sudo**:


```shell
pacman -S sudo
```





- Amilisha haki za **sudo**:



```shell
EDITOR=nano visudo
```





- Kisha uondoe maoni kwenye mstari:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Anzisha tena mfumo na uingie na jina lako la mtumiaji.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Inasakinisha programu



Kwa kuwa Arch Linux ni minimalist, programu nyingi hazijasakinishwa kwa chaguo-msingi. Ili kuongeza kile unachohitaji, chapa amri ifuatayo:



```shell
pacman -S nom_du_paquet_a_installe
```



Kwa mfano, ili kusakinisha **nano** kihariri maandishi, unaweza kuandika:



```shell
pacman -S nano
```



Ili kusakinisha kivinjari chepesi cha wavuti kama vile `firefox`, tumia:



```shell
pacman -S firefox
```



Mwishowe, ikiwa unataka kuongeza zana muhimu za mtandao kama vile `net-tools`, amri itakuwa:



```shell
pacman -S net-tools
```



Usisahau kwamba unaweza kusanikisha vifurushi kadhaa kwa amri moja kwa kuorodhesha kando:



```shell
pacman -S vim firefox net-tools
```



Arch Linux inasimama nje kwa utulivu wake wa ajabu, falsafa ndogo na uimara, na kuifanya kuwa chaguo bora kwa mazingira ya maendeleo. Kwa kutoa tu mambo muhimu, inatoa msingi mwepesi, wa utendaji wa juu ambao ni rahisi kubinafsisha kulingana na mahitaji yako mahususi. Mbinu hii ndogo pia inapendelea udhibiti mkubwa zaidi wa mfumo, ikiimarisha usalama kwa kupunguza eneo la mashambulizi. Shukrani kwa jumuiya yake inayofanya kazi na uwekaji kumbukumbu kamili, Arch Linux inaweza kukusaidia kuunda mazingira salama, yanayonyumbulika yaliyoboreshwa kwa maendeleo ya kitaaluma.



Ikiwa umefurahia kuanza kutumia Arch Linux, utapenda mafunzo yetu kuhusu **Fedora OS**, mfumo wa uendeshaji wa kawaida, salama na thabiti ambao hubadilika kulingana na mahitaji na matumizi yako.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1