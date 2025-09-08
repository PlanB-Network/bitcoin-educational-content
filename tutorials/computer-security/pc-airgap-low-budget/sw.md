---
name: Kompyuta ndogo, ya bajeti ya chini ya airgap
description: Jinsi ya kutengeneza kompyuta ya airgap na Raspberry PI Zero na seti ya vifaa. Yote na bajeti ya euro 35.00.
---
![cover](assets/cover.webp)



Ikiwa umekuwa kwenye kurasa za Plan ₿ Network kwa muda, tayari umejifunza kwamba mojawapo ya mipangilio ya usalama inayopendekezwa zaidi, ambayo ni lazima, **ni usimamizi wa fedha kwa kuhifadhi nje ya mtandao wa funguo zako za faragha**.



Ikiwa bado hujaigundua, katika somo hili lote utapata viungo vya kufungua rasilimali ili ujifunze zaidi kuihusu.



Kwa hivyo, ili kudhibiti funguo za faragha nje ya mtandao, unahitaji kifaa ambacho kimetenganishwa daima kutoka kwa mtandao, iwe ni [Hardware Wallet](https://planb.network/resources/glossary/hardware-Wallet) au kompyuta ya airgap, kitakachotolewa kwa utendakazi huu mahususi.



Unafanyaje ikiwa, kwa mfano, huna uwezo wa kununua vifaa vinavyofanya kazi hii tu, lakini hutaki kuacha hatua hii ya usalama?



## Suluhisho


Je, nikikuambia kuwa unaweza kutengeneza kifaa cha nje ya mtandao kwa njia ya kompyuta ya airgap ambacho ni saizi na uzito wa kiendeshi cha USB flash na kinagharimu euro 35? Je, hungeamini?



Endelea kusoma.



Nitakuambia zaidi: soma njia yote. Suluhisho lililopendekezwa ni la bei nafuu, lakini sio rahisi kabisa. Kwanza unapata wazo la jumla, kisha unaamua kuwekeza muda wako katika utafiti fulani wa kibinafsi na kuchagua, kwa amani ya akili iwezekanavyo, kama na jinsi ya kuendelea.



## Mahitaji


**1** [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (bila kifupisho chochote baada yake) ndio msingi wa kutengeneza kompyuta yenye utendakazi mdogo, lakini kwa kiasi kikubwa haina Wi-Fi na kadi za Bluetooth, mahitaji ya lazima kwa madhumuni haya.





- Gharama**: takriban 15.00 wakati wa kuandika mafunzo haya (Agosti 2025).
- Mwendelezo wa uzalishaji**: Raspberry huhakikisha uzalishaji hadi Januari 2030.



PI Zero bila Wi-Fi na Bluetooth, kwa bahati mbaya imekuwa haipatikani. Unaweza kupata njia mbadala za PI Zero W na PI Zero 2W kwa urahisi zaidi. Katika kesi hii, unaweza kuzima kazi za uunganisho kwa kubadilisha faili ya usanidi. Baada ya kusanikisha mfumo wa uendeshaji, utahitaji kuongeza vitu hivi kwenye usanidi:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



sehemu ya mwongozo huu itakuonyesha jinsi na mahali pa kuifanya. Walakini, ikiwa unataka kuwa na uhakika, unaweza kupata mafunzo kadhaa kwenye wavuti ya kuondoa chip ya Wi-Fi na kikata kidogo, aina inayofaa kwa kufanya kazi kwenye bodi za elektroniki.



**2** _starter kit_ kwa Raspberry PI Zero: kama ilivyo desturi kwa ulimwengu wa Raspberry, mifupa tupu, bila kipochi cha nje. Kwa kuongeza, rasilimali ndogo za bodi ndogo hiyo zinaweka uwezekano wa kuunganishwa na ulimwengu wa nje.



Nilipoamua kuendelea, nilipata [seti hii](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminium-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+8+8sr8-8068s) kamili ya vifaa, ili kuchukua fursa kamili ya uwezo kamili wa PI Zero. Kwa kweli, seti hii ina USB A -> nishati ndogo ya USB Supply, kitovu kidogo cha USB, mini-HDMI -> adapta ya HDMI, heatsink ya shaba, na kipochi cha nje cha alumini. Pia zinazotolewa na kit ni screws na allen wrench zinazohitajika kuweka PI Zero katika kesi mpya.





- Gharama**: euro 19.99.



**3** Mafunzo haya hayahitaji kutumia bajeti kubwa kwenye kompyuta ya airgap. Unapaswa kujua, hata hivyo, kwamba utahitaji kibodi ya USB na panya (iliyo na waya kabisa, epuka Bluetooth) na mfuatiliaji. Kulingana na ingizo la kifuatiliaji chako, unaweza kuhitaji adapta kutoka mini-HDMI, pato pekee linalopatikana kwenye PI Zero. Hatimaye, angalia Hard kwa ukweli kwamba sisi sote tuna kibodi isiyo na waya na panya ndani ya nyumba mahali fulani-ni wakati wa kuzizima Dust.



## Bajeti ya Ziada



**4** Unaweza kupata nishati asili ya Supply kutoka Raspberry, inayogharimu takriban euro 15.00.



**5** Mimi binafsi nilichagua kutumia nishati ya Supply iliyotolewa katika _starter kit_, nikiichanganya, hata hivyo, na USBA → miniUSB inayoitwa kebo ya `hakuna data`, inayogharimu euro 3.70.



**6** Kadi ndogo ya SD, kuwa na angalau hifadhi ya wingi ya GB 32; ikiwa ubora wa viwanda/kiwango ni bora.



**7** Utahitaji mfumo, adapta ya USB hadi micro SD, kama ile unayoona kwenye picha. Mfumo wa uendeshaji wa PI Zero yako na kumbukumbu yake, kwa kweli, itafanya kazi kwenye media hiyo.



![img](assets/it/06.webp)



## Ufungaji wa Mfumo wa Uendeshaji


Kabla ya kufunga PI Zero yako katika kesi hiyo, ninapendekeza usakinishe mfumo wa uendeshaji. Kisha utaweza kuangalia LED inayoonyesha operesheni, moja kwa moja kutoka kwa popo.



Ili kuchagua na kuchoma mfumo wa uendeshaji, nilichagua njia rahisi zaidi: kutumia zana ya Raspberry `PI Imager`.



![img](assets/it/01.webp)



Kisha nenda kwenye [Raspberry's Github](https://github.com/raspberrypi/rpi-imager/releases) ili kupakua toleo jipya zaidi la Taswira, ukichagua ile inayofaa zaidi mfumo wako wa uendeshaji (Mst. 1.9.6 wakati wa kuandika). Utaona kwamba, karibu na kila mali, pia kuna Hash ya faili inayolingana. Itakuja kwa manufaa kwa uthibitishaji.



![img](assets/it/02.webp)



Ninapendekeza kwamba uthibitishe mfumo wa uendeshaji utakaokuwa ukitumia kwenye kompyuta yako ya airgap, kwa amani yako binafsi ya akili. Hii itakupa imani kuwa unafanya kazi na toleo halali (sio hasidi) la Imager na, kwa hivyo, Raspi OS.



Thibitisha mara moja unapopakua, na mashine yako unayotumia kwa kawaida ikiwa imeunganishwa kwenye Mtandao



Kisha fungua terminal ya Linux na uandae upakuaji, ukitengeneza saraka ya `raspios` muhimu kwa kufanya kazi nayo.



![img](assets/it/19.webp)



Pakua Imager kwa usambazaji wako wa Linux na `wget`.



![img](assets/it/20.webp)



Hatimaye, endesha faili `sha256sum` amri na ulinganishe Hash na ile iliyotolewa na Raspberry kwenye Github yake.



![img](assets/it/21.webp)



Au, ikiwa unayo Windows, fungua Shell ya Nguvu na chapa amri ifuatayo:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Utapata Hash ambayo lazima ilingane na ile iliyochapishwa kwenye Raspberry Github.



Mara baada ya kuthibitisha upakuaji, unaweza kusakinisha Imager kwenye kompyuta yako ya kila siku na kuifungua. Imager ni chombo unachohitaji kuchoma mfumo wa uendeshaji kwa SD ndogo, ambayo itakuwa "diski ya mfumo" ya PI Zero.



Mchakato ni rahisi sana: kwanza chagua kifaa cha Raspberry utakachotumia (kwa hivyo zingatia **mfano wako** wa Raspi Zero), kisha toleo la Mfumo wa Uendeshaji, na hatimaye sehemu ya kupachika ya kadi ndogo ya SD ili kuwasha OS.



### Hatua ya Kwanza



![img](assets/it/03.webp)



### Hatua ya Pili



![img](assets/it/07.webp)



**Kumbuka vizuri**: chagua `PI OS 32-bit`, pekee inayofanya kazi na PI Zero.



### Hatua ya Tatu



![img](assets/it/08.webp)



(Kuwa mwangalifu sana kuacha _Exclude System Drive_ iliyochaguliwa ili kuepuka kushawishiwa kusakinisha mfumo wa uendeshaji wa Raspi kwenye kompyuta yako.)



Kila kitu kitakapowekwa, Mpiga Picha atakuuliza ikiwa ungependa kutumia mipangilio maalum. Chagua unachotaka, au ubofye _No_ ili kuendelea na chaguo-msingi.



![img](assets/it/09.webp)



Thibitisha kuwa unataka kufuta yaliyomo kwenye SD ndogo



![img](assets/it/10.webp)



Kipiga picha kinaanza kuwaka mfumo wa uendeshaji kwa SD ndogo, upau wa kusogeza utakujulisha maendeleo.



![img](assets/it/11.webp)



Mwishoni kuna uthibitishaji wa moja kwa moja, nakushauri usiiache.



![img](assets/it/12.webp)



Hatimaye ujumbe unaonekana kwenye skrini, na ikiwa kila kitu kilifanikiwa, inaonekana kama kile ulichosoma kwenye picha.



![img](assets/it/13.webp)



Sasa unaweza kuondoa SD ndogo kutoka kwa msomaji na kuiweka kwenye nafasi ya PI Zero. Washa Raspberry kidogo na uangalie kuongozwa: tunatarajia kuwa Green kwa rangi na flash inayoonyesha upakiaji wa kawaida wa mfumo wa uendeshaji, na kisha uendelee kuendelea. Iwapo una viashirio vingine, kama vile ikiwa kidude kinamulika mara kwa mara au ni nyekundu kwa rangi, wasiliana na Maswali Yanayoulizwa Mara kwa Mara au [kurasa za mijadala ya usaidizi](https://forums.raspberrypi.com/).



## Usanidi wa Kwanza


Uanzishaji wa kwanza wa Raspi OS ni polepole zaidi kuliko kawaida kwa sababu inapaswa kutekeleza idadi ya kazi halisi za usakinishaji. Lakini ikiwa kila kitu kimeenda vizuri, utapata skrini ya kukaribisha.



![img](assets/it/14.webp)



Bofya _Next_ ili kuweka eneo la kijiografia, hasa kwa kupakia kibodi sahihi. Kulipa kipaumbele maalum kwa mwisho.



![img](assets/it/15.webp)



Bofya _Next_ na utaulizwa kuunda mtumiaji wako, andika kitambulisho chako na uziweke vizuri.



![img](assets/it/16.webp)



Mchawi hukuuliza uchague kivinjari chaguo-msingi cha wavuti, kati ya Chromium na Firefox; inaweza pia kukuuliza kuhusu mipangilio ya mtandao wa Wi-Fi ikiwa unafanya kazi na Zero W au 2W PI. Endelea na ubofye _Ruka_.



Wakati fulani utaombwa kuboresha programu kwenye ubao na mfumo wa uendeshaji. Chagua _Ruka_: kwa madhumuni ya zoezi hili kwa kweli tunaunda mashine ya nje ya mtandao, ambayo lazima isalie nje ya mtandao kufikia wakati huu.



Hatimaye, inaweza kukuuliza uwashe `ssh`, lakini ukatae hatua hii pia, kwa kuwa ni IP ya hewa ya Zero.



![img](assets/it/17.webp)



Hakuna mengi zaidi ya kusanidi. Baada ya kumaliza, anzisha tena Raspberry ili mabadiliko yaanze kutumika.



![img](assets/it/18.webp)



## Airgap Mpya ya Kompyuta


Baada ya kuwasha upya, kompyuta yako mpya ya airgap iko tayari. PI Zero inakuonyesha desktop mpya, ambayo unaweza kufanya kazi nayo kupitia GUI au kutoka kwa mstari wa amri.



![img](assets/it/22.webp)



### Hatua za Kwanza za PI Zero W au 2W


Ikiwa unafanya kazi na mfululizo wa Raspberry PI Zero W au 2W, ubao wako una vichipu vya Wi-Fi na Bluetooth ubaoni. Wakati wa usanidi wa kwanza uliruka usanidi wa uunganisho, kwa hivyo PI Zero haijaunganishwa kwenye Mtandao. Sasa unaweza kulemaza chipsi hizo mbili kabisa kupitia programu.



Kwa kweli, Raspi OS hutoa faili ya `config.txt` ambayo unaweza kuhariri kwa kupenda kwako. `Config` iko katika kizigeu cha `boot`, katika saraka ya `firmware`, na unaweza kuihariri na kuihifadhi kwa marupurupu ya `root`.



Fungua terminal kutoka kwa ikoni iliyo upande wa juu kushoto na inakuwa `mzizi`.(1)



![img](assets/it/23.webp)



(1) Ikiwa Raspi OS haikukuruhusu kuunda nenosiri la `mizizi` wakati wa hatua za awali, ninapendekeza ufanye hivyo sasa, kwa amri ya `passwd`. Kuwa na mtumiaji `mzizi` kuhama bila kutegemea mtumiaji wako binafsi kunaweza kuwa rahisi sana katika hali za uokoaji.



Ukiwa na terminal, angalia faili ya `config.txt` na uwe tayari kuihariri ukitumia kihariri `nano`.



![img](assets/it/24.webp)



Uhariri unapaswa kufanywa chini ya `usanidi` mzima, baada ya maneno `[Yote]`. Ni katika hatua hii ambapo utaongeza amri `dtoverlay` iliyoonyeshwa mwanzoni mwa somo.



![img](assets/it/25.webp)



Hifadhi, funga na uanze upya. Katika hatua inayofuata tutaenda kwenye uchunguzi wa Raspberry kidogo.



## Nini cha Kutarajia kutoka kwa Kifaa hiki?


Kwa kuangalia [ubainifu wa kiufundi](https://www.raspberrypi.com/products/raspberry-pi-zero/) kutoka kwa tovuti ya Raspberry, PI Zero ina kichakataji cha msingi 1 cha BCM2835 na RAM ya MB 512, kwa hivyo haiahidi kuwa na nguvu sana.



Kwa kuwa terminal ni nyepesi, tutatumia mstari wa amri ili kuchunguza usanidi wa mfumo.



Unapowasha utaona skrini fupi ya rangi ya upinde wa mvua, ikifuatiwa na ujumbe wa kukaribisha kutoka kwa Raspberry na, katika kona ya chini kushoto, jumbe za kernel zinazohusiana na uanzishaji.



Wakati desktop ya PI OS inaonekana, fungua terminal na chapa:



```bash
uname -a
```


Amri hii itakuonyesha toleo la kernel linalotumika sasa kwenye skrini, pamoja na habari zingine.



![img](assets/it/26.webp)



Unaweza pia kuona habari juu ya CPU na maunzi kwa kuandika:



```bash
lscpu
```



![img](assets/it/27.webp)



Na pia angalia `proc/mem/info`.



![img](assets/it/28.webp)



Ili kujua toleo la Debian na jina la msimbo la kutolewa:



``` bash


lsb_kutolewa -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Tumia


Ingawa utendakazi unaonekana kuwa mdogo (kwenye karatasi na ikilinganishwa na nguvu za mashine za leo) PI Zero inafanya kazi, haswa kama terminal.





- Kwanza unaweza kwenda kwenye menyu kuu na kupata msukumo wa paneli ya _Ongeza/Ondoa programu_, ambapo utapata huduma kadhaa za kupanga na kufanya mazoezi. Kumbuka kuwa unaweza pia kufanya hivi kutoka kwa terminal, lakini kila wakati na marupurupu ya `root`.



![img](assets/it/33.webp)





- Unaweza "kupitisha" kifaa hiki cha nje ya mtandao ili kuhifadhi aina mbalimbali za hati za siri, ambazo zitaendelea kufikiwa inapohitajika, bila kuonyeshwa Mtandaoni.
- Unaweza kutumia usanidi huu kwa generate funguo zako za GPG kwa usalama.
- Unaweza, hata, kutumia "kichezeo" hiki kipya kama kifaa cha sahihi cha airgap, [kwa kufuata ushauri wa Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-8dd5c0-51).



Miongoni mwa Pochi ambazo ninazifahamu, pekee ambayo hutoa toleo la 32-bit ni Electrum. Vema: IP ya Sifuri jinsi tulivyoitayarisha katika mafunzo haya itakuruhusu kuweka funguo za faragha nje ya mtandao zilizowekwa kwa Wallet airgap ambayo tulishughulikia katika mafunzo haya:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Hitimisho


Usanidi una, pengine, udhaifu mmoja mkubwa: SD ndogo ni kati ambayo inaweza kutoa matatizo. Ni hatari kwa matumizi makubwa; labda tayari una uzoefu na hii, kutokana na kuitumia na simu yako. Baada ya kusakinisha programu zote utakazotaka kutumia kwenye IP ya Zero airgap, fanya chelezo nzuri ya SD ndogo ya thamani, ukitumia zana ya Raspi OS uliyonayo.



![img](assets/it/34.webp)



Mahitaji yako yanapokua, na pamoja nao uwezekano wako wa bajeti, unaweza kuchunguza Raspberry nyingine au ufumbuzi sawa. Akizungumzia kumbukumbu, kwa mfano, PI 5 inatoa uwezekano wa kukusanya gari la M2 NVME, ambalo hakika ni imara zaidi kuliko microSD.



Usisahau kuandika na kuandika kila hatua ya usakinishaji wa programu ya matumizi ambayo unakaribia kutumia nje ya mtandao. **hivi karibuni au baadaye Raspi OS iliyosasishwa itatoka** ambayo hakika utataka kunufaika nayo. Wakati huo itabidi ufute kila kitu na uifanye tena (labda na micro SD mpya 😂).



Zoezi ambalo tumemaliza kufanya, tukichukulia kuwa ni jaribio lako la kwanza pia, utakumbuka kwa muda mrefu. Si mara zote inawezekana kuweka maunzi kwa shughuli `zilizopachikwa` nje ya mtandao, bila kupuuza tahadhari kwa mashine iliyo na nafasi ya hewa kuwasha na kuangalia mara kwa mara.



Umemaliza, ingawa, pongezi! Na utaweza kupendekeza suluhisho hili kwa wale wote wanaohitaji kuweka bajeti zao chini.