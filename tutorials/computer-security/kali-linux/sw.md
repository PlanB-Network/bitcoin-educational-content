---
name: Kali
description: Kusakinisha Kali Linux kwenye VirtualBox, kama fimbo ya USB inayoweza kusomeka, au kama buti mbili, hatua kwa hatua.
---

![cover-kali](assets/cover.webp)



## Utangulizi



### Kwa nini Kali Linux?



**Kali Linux** ni usambazaji wa Linux uliobobea katika usalama wa IT.


Hii ndio sababu tunatumia Kali Linux:





- Imesanidiwa awali na anuwai ya zana za kupenta (majaribio ya mfumo na usalama wa mtandao).
- Ni **chanzo huria na isiyolipishwa**, kwa hivyo unaweza kuitumia na kuirekebisha bila malipo.
- Ni **inayotegemewa na salama**, bora kwa kujifunza kuhusu usalama wa mtandao.
- Inakuruhusu kujifunza jinsi ya kutumia Linux katika mazingira tayari kwa majaribio.
- Inaweza kusakinishwa kwa njia tofauti: **VirtualBox**, **ufunguo wa USB unaoweza kusomeka**, au **boot mbili**.



## Ufungaji na usanidi



### 1. Mahitaji



**Vifaa vinavyohitajika:**





- Kichakataji cha 64-bit** (Intel au AMD).
- Kiwango cha chini cha GB 8 cha RAM** (GB 4 inaweza kutosha kwa usakinishaji wa mwanga au VM).
- Nafasi ya diski ya GB 50 bila malipo** ili kusakinisha Kali Linux.
- Muunganisho wa Mtandao** ili kupakua picha na masasisho ya ISO.
- Ufunguo wa USB wa angalau GB 8** ili kuunda media inayoweza kusomeka (ikiwa unataka kusakinisha Kali kwenye Kompyuta au kuijaribu kwenye USB Moja kwa Moja).



Ni muhimu kuhifadhi nakala ya data yako kabla ya kusakinisha kwenye Kompyuta iliyopo.



### 2. Pakua





- Nenda kwenye [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Chagua picha ya ISO kwa programu yako:
  - Sakinisha Picha** : kwa usakinishaji wa Kompyuta.
  - Picha Pepe**: kusakinisha Kali kwenye VirtualBox au VMware.
- Pakua picha ya ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Unda ufunguo wa USB wa bootable



Unaweza kutumia zana kadhaa, kama vile Balena Etcher :





- Pakua na usakinishe [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Fungua Balena Etcher, kisha uchague picha ya Kali ISO.
- Chagua kitufe cha USB kama media lengwa.
- Bonyeza Flash na usubiri mchakato ukamilike.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Kusakinisha na kupata Kali Linux



#### 4.1 Inawasha kitufe cha USB





- Zima kompyuta.
- Chomeka ufunguo wa USB (ulio na Kali Linux).
- Washa kompyuta yako. Kwenye Kompyuta za hivi karibuni, mfumo unapaswa kutambua kiotomati ufunguo wa boot wa USB. Ikiwa sivyo, fungua upya kwa kushikilia ufunguo wa ufikiaji wa BIOS/UEFI (kawaida F2, F12 au Futa, kulingana na chapa).
  - Katika menyu ya BIOS/UEFI, chagua kitufe chako cha USB kama kifaa cha kuwasha.
  - Hifadhi na uanze upya.



#### 4.2 Kuzindua usakinishaji



##### Skrini ya kuanza



Wakati wa kuwasha kutoka kwa fimbo ya USB, skrini ya boot ya Kali Linux inapaswa kuonekana. Chagua kati ya **usakinishaji wa picha** na **usakinishaji wa maandishi**. Katika mfano huu, tumechagua usakinishaji wa picha.



![capture](assets/fr/06.webp)



Ukitumia picha ya **Moja kwa moja**, utaona hali nyingine, **Live**, ambayo pia ni chaguo-msingi la kuanzisha.



![Mode Live](assets/fr/07.webp)



##### Uchaguzi wa lugha



Chagua lugha unayopendelea kwa usakinishaji na mfumo.



![Sélection de la langue](assets/fr/08.webp)



Tafadhali bainisha eneo lako la kijiografia.



![Options d'accessibilité](assets/fr/09.webp)



##### Usanidi wa kibodi



Chagua mpangilio wa kibodi yako. Sehemu ya majaribio inapatikana ili kuangalia kama funguo zinalingana na usanidi wako.



![Configuration du clavier](assets/fr/10.webp)



##### Muunganisho wa mtandao



Kisakinishi sasa kitachanganua violesura vya mtandao wako, kutafuta huduma ya DHCP, kisha kukuarifu kuweka jina la seva pangishi ya mfumo wako. Katika mfano ulio hapa chini, tumeingiza **"kali "** kama jina la mwenyeji.



![Configuration réseau](assets/fr/11.webp)



Unaweza kutoa kwa hiari jina la kikoa chaguo-msingi ambalo mfumo huu utatumia (thamani zinaweza kurejeshwa kutoka kwa DHCP au ikiwa kuna mfumo wa uendeshaji uliopo).



![Choix du type d'installation](assets/fr/12.webp)



##### Akaunti za watumiaji



Ifuatayo, unda akaunti ya mtumiaji kwa mfumo (jina kamili, jina la mtumiaji na nenosiri kali).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Saa za eneo



Chagua eneo lako la kijiografia ili kuweka wakati wa mfumo.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Aina ya kugawa



Kisakinishi kisha huchanganua diski zako na kuonyesha chaguo kadhaa kulingana na usanidi wako.



Katika mwongozo huu, tunaanza kutoka kwa ** diski tupu **, ambayo inatoa ** chaguzi nne iwezekanavyo **.


Tutachagua **Kuongozwa - tumia diski nzima**, kwani hapa tunafanya usakinishaji wa mara moja wa Kali Linux (boot moja). Hii ina maana kwamba hakuna mfumo mwingine wa uendeshaji utahifadhiwa, na disk nzima inaweza kufutwa.



Ikiwa diski yako tayari ina data, chaguo la ziada **Iliyoongozwa - tumia nafasi kubwa zaidi inayopakana ya bure** inaweza kuonyeshwa.



Mbadala hii hukuruhusu kusakinisha Kali Linux bila kufuta data iliyopo, na kuifanya iwe bora kwa uanzishaji mara mbili na mfumo mwingine.



Kwa upande wetu, diski ni tupu, hivyo chaguo hili halionekani.



![Choix du partitionnement](assets/fr/17.webp)



Chagua diski ya kugawanywa.



![capture](assets/fr/18.webp)



Kulingana na mahitaji yako, unaweza kuchagua kuweka faili zako zote katika kizigeu kimoja (tabia chaguomsingi) au kuwa na sehemu tofauti za saraka moja au zaidi za kiwango cha juu.



Ikiwa huna uhakika unachotaka, chagua chaguo la **Faili zote katika kizigeu kimoja**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Kisha utakuwa na fursa ya mwisho ya kuangalia usanidi wa diski yako kabla ya programu ya usakinishaji kufanya mabadiliko yoyote yasiyoweza kutenduliwa. Mara tu unapobofya _Endelea_, programu ya usakinishaji itazinduliwa na usakinishaji utakuwa karibu kukamilika.



![capture](assets/fr/21.webp)



##### LVM iliyosimbwa kwa njia fiche



Ikiwa chaguo hili liliwezeshwa katika hatua ya awali, Kali Linux sasa itafanya ufutaji salama wa diski kuu kabla ya kukuuliza nenosiri la LVM.



Tafadhali tumia nenosiri dhabiti, vinginevyo onyo kuhusu passphrase dhaifu litaonyeshwa.



##### Maelezo ya wakala



Kali Linux hutumia hazina kusambaza programu. Utahitaji kuingiza maelezo muhimu ya seva mbadala ikiwa mazingira yako yanatumia moja.



Ikiwa **huna uhakika** kama utatumia seva mbadala, **acha wazi**. Kuingiza taarifa za uongo kutazuia muunganisho kwenye hazina.



![capture](assets/fr/22.webp)



##### Metapets



Ikiwa ufikiaji wa mtandao haujasanidiwa, utahitaji **kusanidi zaidi** unapoombwa.



Ikiwa unatumia picha ya **Live**, hatua inayofuata haitaonyeshwa.



Kisha unaweza kuchagua [metapackages](https://www.kali.org/docs/general-use/metapackages/) ungependa kusakinisha. Chaguzi chaguo-msingi zitasakinisha mfumo wa kawaida wa Kali Linux, kwa hivyo hutahitaji kurekebisha chochote.



![capture](assets/fr/23.webp)



#### Taarifa ya kuanza



Kisha uthibitishe usakinishaji wa kipakiaji cha boot cha GRUB.



![capture](assets/fr/24.webp)



##### Anzisha upya



Hatimaye, bofya Endelea ili kuanzisha upya usakinishaji wako mpya wa Kali Linux.



![capture](assets/fr/25.webp)



#### 4.3 Kusasisha na kusanidi Kali Linux baada ya usakinishaji



Kusasisha mfumo wako ni hatua muhimu baada ya usakinishaji mpya. Una chaguzi mbili:



##### Chaguo 1: Kupitia kiolesura cha picha cha mtumiaji (GUI)



Kali, kama Debian/Ubuntu, inatoa kidhibiti cha sasisho cha picha kilichojumuishwa.



1. Bofya kwenye **menu kuu** (juu kushoto au chini kulingana na eneo-kazi lako).


2. Fungua **"Kisasisho cha Programu "**.


3. Chombo kitafanya:




    - Angalia vifurushi ili kusasishwa.
    - Utaona orodha (pamoja na ukubwa na matoleo).
    - Inakuruhusu kuzindua sasisho kwa mbofyo mmoja.


4. Weka nenosiri lako la msimamizi (`sudo`) unapoombwa.


5. Wacha iweke na uanze tena ikiwa ni lazima.



##### Chaguo 2: Kupitia terminal



Fungua terminal na uendeshe:



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Haipendekezi kutumia akaunti ya **mizizi** kwa kazi ya kila siku; unda mtumiaji asiye na mizizi badala yake.



Katika terminal yako, chapa amri hizi:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Toka na uingie tena na mtumiaji mpya.



Wacha tufanye muhtasari wa kazi za kimsingi za Kali Linux kwenye jedwali.



### Kazi za kimsingi chini ya Kali Linux




| **Kundi** | **Kazi ya Msingi** | **Maelezo / Lengo** | **Njia Kuu** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Urambazaji wa Mfumo** | Fungua terminal | Pata ufikiaji wa mstari mkuu wa amri wa Kali | Bonyeza ikona ya terminal au tumia `Ctrl + Alt + T` |
| | Vinjari folda | Sogeza kwenye muundo wa folda za mfumo | `cd /njia/ya/folda`, `ls` kuorodhesha faili |
| | Unda / futa folda | Panga faili | `mkdir jina_la_folda`, `rm -r jina_la_folda` |
| **Usimamizi wa Faili** | Nakili / sogeza faili | Shughulikia faili kwenye terminal | `cp faili lengo`, `mv faili lengo` |
| | Futa faili | Punguza nafasi kwenye diski | `rm jina_la_faili` |
| | Onyesha maudhui ya faili ya maandishi | Soma faili haraka | `cat faili.txt`, `less faili.txt` |
| **Usimamizi wa Mfumo** | Sasisha Kali Linux | Sakinisha matoleo mapya na viraka vya usalama | `sudo apt update && sudo apt full-upgrade -y` |
| | Sakinisha programu | Ongeza zana mpya au huduma | `sudo apt install jina_la_kifurushi` |
| | Futa programu | Safisha mfumo | `sudo apt remove jina_la_kifurushi` |
| | Safisha utegemezi usiohitajika | Pata nafasi kwenye diski | `sudo apt autoremove` |
| **Mtandao na Intaneti** | Angalia muunganisho wa mtandao | Jaribu ufikiaji wa Intaneti | `ping google.com` |
| | Tambua anwani ya IP | Jua usanidi wako wa mtandao | `ip a` au `ifconfig` |
| | Badilisha mtandao wa Wi-Fi | Unganisha kwenye sehemu nyingine ya ufikiaji | Ikona ya mtandao → Chagua Wi-Fi unayotaka |
| **Akaunti na Ruhusa** | Tekeleza amri ya msimamizi | Pata haki za root kwa muda | `sudo amri` |
| | Unda mtumiaji mpya | Ongeza akaunti ya ndani | `sudo adduser jina_la_mtumiaji` |
| | Badilisha nenosiri | Linda akaunti | `passwd` |
| **Muonekano na Faraja** | Badilisha mandhari ya nyuma | Binafsisha desktop | Bonyeza kulia kwenye desktop → **Mipangilio ya Desktop** |
| | Badilisha mandhari / ikona | Boresha usomaji na urembo | Mipangilio → Muonekano / Mandhari |
| **Zana za Kali** | Fungua menyu ya zana | Chunguza zana za majaribio na usalama | Menyu ya **Programu → Kali Linux** |
| | Zindua zana (mfano: nmap, wireshark) | Ugunduzi wa vitendo wa huduma za usalama | `sudo nmap`, `wireshark`, nk. |
| **Msaada na Nyaraka** | Pata msaada kuhusu amri | Elewa amri kabla ya kuitumia | `man amri` au `amri --help` |

## Hitimisho



Kusakinisha Kali Linux ni hatua ya kwanza tu ya kugundua mazingira haya yenye nguvu yanayohusu usalama wa mtandao. Kwa kufahamu kazi za kimsingi na usimamizi wa mfumo, kila mtu anaweza kuanza kuchunguza zana zilizojengewa ndani na kuelewa utendakazi wa ndani wa mfumo wa Linux. Kali inatoa jukwaa bora la kujifunza, kwa ajili ya kuimarisha ujuzi wa kiufundi na kuendeleza utamaduni halisi wa usalama wa IT.