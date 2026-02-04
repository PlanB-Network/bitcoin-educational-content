---
name: Kali
description: Gushiramwo Kali Linux kuri VirtualBox, nk’inkoni ya USB ishobora gufungurwa, canke nk’inkoni y’ugufungura kabiri, intambwe ku yindi.
---

![cover-kali](assets/cover.webp)



## Imenyekanisha



### Kubera iki Linux?



**Kali Linux** ni ubuhinga bwa Linux bwihariye mu mutekano w’ubuhinga bwa none.


Ehe igituma dukoresha Kali Linux:





- Ibanza gutegurwa n’ibikoresho vyinshi vy’ugupima (ibipimo vy’umutekano wa sisitemu n’urubuga).
- Ni **open source kandi ni ubuntu**, rero urashobora kuyikoresha no kuyihindura ku buntu.
- Ni **ukwizigirwa kandi gutekanye**, ni vyiza cane mu kwiga ivyerekeye umutekano wo kuri internet.
- Iragufasha kwiga gukoresha Linux mu bidukikije vyiteguye gupima.
- Ishobora gushirwa mu buryo butandukanye: **VirtualBox**, **urufunguzo rwa USB rushobora gufungurwa**, canke **ugufungura kabiri**.



## Gushiramwo no gutunganya



### 1. Ibisabwa



**Ibikoresho bisabwa:**





- Igikoresho c’ibice 64** (Intel canke AMD).
- 8 GB RAM n’imiburiburi** (4 GB zishobora kuba zihagije ku gushiramwo umuco canke VM).
- 50 GB y'umwanya kuri disiki y'ubuntu** kugira ngo ushiremwo Kali Linux.
- Internet** kugira ngo ubone ishusho ya ISO n’ibindi bishasha.
- Urufunguzo rwa USB rwa 8 GB** kugira ngo ukore ubuhinga bwo gufungura (niba ushaka gushiramwo Kali kuri PC canke ukayigerageza kuri Live USB).



Ni vyiza ko ukora backup y’amakuru yawe imbere yo kuyashira kuri PC isanzweho.



### 2. Gukuraho





- Genda kuri [kali.org/kuronka-kali](www.kali.org/kuronka-kali/#ibibanza-vya-kali)
- Hitamwo ishusho ya ISO y'ikoreshwa ryawe:
  - Gushiramwo Ishusho** : ku gushiramwo PC.
  - Ishusho y'ukuri**: gushiramwo Kali kuri VirtualBox canke VMware.
- Gukuraho ishusho ya ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Rema urufunguzo rwa USB rushobora gufunguka



Ushobora gukoresha ibikoresho vyinshi, nka Balena Etcher :





- Gukuraho no gushiramwo [Igishushanyo ca Balena](https://igishushanyo.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Ugurure Balena Etcher, hanyuma uhitemwo ishusho ya Kali ISO.
- Hitamwo urufunguzo rwa USB nk'ivyo ukoresha.
- Fyonda kuri Flash hanyuma urindire ko igikorwa kirangira.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Gushiramwo no gukingira Kali Linux



#### 4.1 Gufungura ku rufunguzo rwa USB





- Zima mudasobwa.
- Nimushiremwo urufunguzo rwa USB (rurimwo Kali Linux).
- Hindukiza mudasobwa yawe. Ku ma PC aherutse gusohoka, iyo sisitemu ikwiye kumenya ubwayo urufunguzo rwo gufungura USB. Niba bitameze gutyo, subira gufungura ufashe urufunguzo rwo gushika kuri BIOS/UEFI (kenshi F2, F12 canke Delete, bivanye n’ibara).
  - Mu BIOS/UEFI, hitamwo urufunguzo rwawe rwa USB nk’igikoresho co gutangura.
  - Bika kandi wongere utangure.



#### 4.2 Gutanguza gushiramwo



##### Igishushanyo co gutangura



Igihe ufunguye kuri USB, igicapo co gufungura ca Kali Linux gikwiye kuboneka. Hitamwo hagati ya **gushiramwo ibishushanyo** na **gushiramwo umwandiko**. Muri aka karorero, twahisemwo gushiramwo ibishushanyo.



![capture](assets/fr/06.webp)



Niwakoresha ishusho **Live**, uzobona ubundi buryo, **Live**, na bwo ni uburyo bwo gutangura.



![Mode Live](assets/fr/07.webp)



##### Guhitamwo ururimi



Hitamwo ururimi ukunda rwo gushiramwo n’ivyo gukoresha.



![Sélection de la langue](assets/fr/08.webp)



Urasabwe kuvuga aho uri.



![Options d'accessibilité](assets/fr/09.webp)



##### Imiterere ya klavye



Hitamwo uko klavye yawe iteye. Hariho ikibanza co kugerageza kugira ngo ugenzure ko imfunguruzo zihuye n'imiterere yawe.



![Configuration du clavier](assets/fr/10.webp)



##### Ihuriro ry'urubuga



Ivyo bizoca bicapura interfaces zawe z’urubuga, birondere service ya DHCP, hanyuma bigusabe kwinjiza izina ry’umushitsi wa sisitemu yawe. Mu karorero kari musi, twinjije **"kali "** nk'izina ry'umushitsi.



![Configuration réseau](assets/fr/11.webp)



Ushobora gutanga izina ry'indangarubuga ry'imbere y'igihe iyi sisitemu izokoresha (agaciro gashobora kuronswa muri DHCP canke nimba hariho sisitemu y'ikoreshwa ya kera).



![Choix du type d'installation](assets/fr/12.webp)



##### Konti z'abakoresha



Inyuma y’aho, ushireho konti y’ukoresha ya sisitemu (izina ryose, izina ry’ukoresha n’ijambobanga rikomeye).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Akarere k'isaha



Hitamwo aho uba kugira ngo ushireho isaha ya sisitemu.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Ubwoko bwo gucapura



Ico gikoresho gica gicapura ama disk yawe maze kikagaragaza amahitamwo menshi bivanye n’ingene ukora.



Muri iyi nsiguro, dutangura kuri **disque blank**, itanga **amahitamwo ane ashoboka**.


Tugiye guhitamwo **Guided - ukoreshe disk yose**, nk'uko hano turiko turakora ugushiraho Kali Linux rimwe (gutangura rimwe). Ivyo bisigura ko ata yindi porogarama izogumaho, kandi ko disiki yose ishobora gukurwaho.



Niba disiki yawe isanzwe irimwo amakuru, uburyo bwo kwongerako **Burongowe - ukoreshe umwanya munini w'ubusa** bushobora kugaragazwa.



Iyi nzira ishobora kugufasha gushiramwo Kali Linux utakuyeho amakuru asanzwe, bikaba bituma iba nziza cane mu gufungura kabiri n’iyindi sisitemu.



Mu gihe cacu, disiki iri ubusa, rero iyo nzira ntiboneka.



![Choix du partitionnement](assets/fr/17.webp)



Hitamwo disiki izogabanywa.



![capture](assets/fr/18.webp)



Bivanye n'ivyo ukeneye, ushobora guhitamwo kubika amadosiye yawe yose mu gice kimwe (inyifato mburabuzi) canke ukagira ibice bitandukanye vy'ububiko bumwe canke bwinshi bwo ku rwego rwo hejuru.



Niba utazi neza ico ushaka, hitamwo **Amadosiye yose mu gice kimwe**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Uzoca uronka akaryo ka nyuma ko kugenzura uko disiki yawe iteye imbere y’uko porogarama yo gushiramwo ibintu ihindura ibintu bidashobora gusubirwamwo. Uhejeje gukanda kuri _Continue_, porogarama yo gushiramwo izotangura kandi gushiramwo bizoba hafi kurangira.



![capture](assets/fr/21.webp)



##### LVM yashizwemwo amakuru



Niba iyo nzira yari yakoreshejwe mu ntambwe iheze, Kali Linux ubu izokora ugukuraho hard disk itekanye imbere yo kukusaba ijambobanga rya LVM.



Urasabwa gukoresha ijambobanga rikomeye, ahandi ho imburi yerekeye passphrase idakomeye izogaragara.



##### Amakuru y'uwuserukira



Kali Linux ikoresha ububiko bwo gukwiragiza porogaramu. Uzokenera kwinjiza amakuru akenewe y'ubutumwa nimba ibidukikije vyawe bikoresha.



Niba **utazi neza** nimba ukoresha proxy, **siga ubusa**. Kwinjiza amakuru y’ibinyoma bizokubuza gukorana n’ibibanza vy’ububiko.



![capture](assets/fr/22.webp)



##### Ibikoko



Niba uburyo bwo gushika ku rubuga butatunganijwe, uzokenera **gukomeza gutunganya** iyo usabwe.



Niba ukoresha ishusho **Live**, intambwe ikurikira ntizogaragara.



Ushobora rero guhitamwo [amapaki](https://www.kali.org/docs/ikoreshwa rusangi/amapaki/) wipfuza gushiramwo. Amahitamwo y'imbere azoshiraho uburyo busanzwe bwa Kali Linux, rero ntuzokenera guhindura ikintu na kimwe.



![capture](assets/fr/23.webp)



#### Amakuru yo gutangura



Hanyuma wemeze ko GRUB boot loader yashizweho.



![capture](assets/fr/24.webp)



##### Gusubira gutangura



Ubwa nyuma, fyonda ku Continue kugira ngo wongere utangure ku nzira yawe nshasha ya Kali Linux.



![capture](assets/fr/25.webp)



#### 4.3 Guhindura no gutunganya Kali Linux inyuma yo gushirwaho



Guhindura ubuhinga bwawe ni intambwe ihambaye inyuma yo gushiramwo ibintu bishasha. Ufise uburyo bubiri:



##### Ihitamwo rya 1: Biciye ku kigaragara c'ukoresha (GUI)



Kali, nka Debian/Ubuntu, itanga umuyobozi w'ivugurura ry'ibishushanyo.



1. Fyonda kuri **main menu** (hejuru ibubamfu canke hasi bivanye n’ibiro vyawe).


2. Gufungura **"Igikoresho co guhindura porogaramu "**.


3. Ico gikoresho kizo :




    - Suzuma amapaki azohindurwa.
    - Uzobona urutonde (rufise ubunini n'imirongo).
    - Iguha uburenganzira bwo gutanguza ivugurura n'ugukanda rimwe.


4. Injira ijambobanga ry'umuyobozi wawe (`sudo`) iyo usabwe.


5. Reka ishiremwo hanyuma isubire gutangura nimba bikenewe.



##### Amahitamwo ya 2: Biciye ku kibanza



Gufungura ikibanza maze ukoreshe :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Si vyiza gukoresha konti ya **root** mu bikorwa vya misi yose; rema umukoresha atari umuzi aho.



Mu nzira yawe, wandike aya mabwirizwa:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Sohoka maze usubire kwinjirana n'ukoresha mushasha.



Reka dufate mu ncamake ibikorwa bimwe bimwe vy’ishimikiro vya Kali Linux mu meza.



### Ibikorwa vy'ishimikiro biri munsi ya Kali Linux




| **Igice** | **Igikorwa remezo** | **Insiguro / Intumbero** | **Uburyo nyamukuru** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Kugendagenda muri sisitemu** | Kwugurura ikiranga-ndagiro (terminal) | Kwinjira aho banditse amategeko muri Kali | Fyonda ku gishushanyo c'ikiranga-ndagiro canke koresha `Ctrl + Alt + T` |
| | Kuraba mu bikubiye mu madosiye | Kugendagenda mu biti vy'amadosiye ya sisitemu | `cd /inzira/iyenda/mw'idosiye`, `ls` kugira urabe amadosiye ahari |
| | Kurema / gusiba idosiye | Gutunganya amadosiye | `mkdir izina_ry_idosiye`, `rm -r izina_ry_idosiye` |
| **Gucunga amadosiye** | Kwandukura / kwimura idosiye | Gukoresha amadosiye mu kiranga-ndagiro | `cp idosiye aho_ijanywe`, `mv idosiye aho_ijanywe` |
| **Gusiba idosiye** | Gusiba idosiye | Kurondera aho dushira ibindi bintu kuri disiki | `rm izina_ry_idosiye` |
| | Kwerekana ibiri mw'idosiye y'icandiko | Gusoma idosiye vuba na vuba | `cat idosiye.txt`, `less idosiye.txt` |
| **Gucunga sisitemu** | Kuvugurura Kali Linux | Mushiremo uburyo bushasha n'ukurinda umutekano | `sudo apt update && sudo apt full-upgrade -y` |
| | Mushiremo porogaramu | Kwongeramo igikoresho gishasha | `sudo apt install izina_ry_igikoresho` |
| | Gusiba porogaramu | Gusukura sisitemu | `sudo apt remove izina_ry_igikoresho` |
| | Gusukura ibintu bitagikenewe | Kurondera aho dushira ibindi bintu kuri disiki | `sudo apt autoremove` |
| **Imiyoboro n'Ikiyago (Internet)** | Kuraba ko imiyoboro ikora | Kugeregeza kwinjira kuri internet | `ping google.com` |
| | Kuraba IP address | Kumenya uko imiyoboro yawe yubatse | `ip a` canke `ifconfig` |
| | Guhindura Wi-Fi | Kwinjira mu yindi Wi-Fi | Igishushanyo c'imiyoboro → Hitamo Wi-Fi ushaka |
| **Makonti n'uburenganzira** | Gukora itegeko ry'umuyobozi | Kuronka uburenganzira bwa root mu mwanya muto | `sudo itegeko` |
| | Kurema umukoresha mushasha | Kwongeramo ikonti nshasha | `sudo adduser izina_ry_umukoresha` |
| | Guhindura ijambo ry'ibanga | Kurinda ikonti | `passwd` |
| **Isura n'uburyohe** | Guhindura ishusho y'inyuma | Gutunganya aho ukorera | Fyonda iburyo ku mbuga ukorerako → **Ibigenewe imbuga** |
| | Guhindura isura / ibishushanyo | Gutuma vyoroherana gusoma n'ubwiza | Ibigenewe → Isura / Imisura |
| **Ibikoresho vya Kali** | Kwugurura urutonde rw'ibikoresho | Kuraba ibikoresho vyo kugerageza n'umutekano | Urutonde rw' **Aporikasiyo → Kali Linux** |
| | Gutanguza igikoresho (nk'akarorero: nmap, wireshark) | Kumenya gukoresha ibikoresho vy'umutekano | `sudo nmap`, `wireshark`, n'ibindi. |
| **Ubufasha n'inyandiko** | Kuronka ubufasha ku itegeko | Gutahura itegeko imbere yo kurikoresha | `man itegeko` canke `itegeko --help` |

## Iciyumviro



Gushiramwo Kali Linux ni intambwe ya mbere gusa yo kumenya iki kibanza gikomeye c’umutekano wo kuri internet. Mu kumenya neza ibikorwa vy’ishimikiro n’ugucungera sisitemu, umuntu wese arashobora gutangura gutohoza ibikoresho vyubatswemwo no gutahura ingene sisitemu ya Linux ikora imbere. Kali itanga urubuga rwiza cane rwo kwigirako, rwo gukomeza ubuhinga bwo mu vy’ubuhinga no guteza imbere umuco nyawo w’umutekano w’ubuhinga bwa none.