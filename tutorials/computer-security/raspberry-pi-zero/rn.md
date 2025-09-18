---
name: Raspberry Pi Zero
description: Uko wokora mudasobwa ntoyi, ifise umwuka, idahenda cane ukoresheje Raspberry Pi Zero n’ibikoresho vyo gukoresha.
---
![cover](assets/cover.webp)



Niba umaze igihe uri kuri paji za Plan ₿ Network, waramaze kumenya ko kimwe mu bintu vy’umutekano bivugwa cane, hafi y’uko ari ngombwa, **ari ugucungera amahera biciye mu kubika imfunguruzo zawe z’ibanga ata murongo**.



Niba utarabibona, muri iyi nyigisho yose uzosangamwo amahuza ku bikoresho vy’inkomoko yuguruye ushobora gukoresha kugira ngo umenye vyinshi kuvyerekeye.



Kugira rero umuntu ashobore gucungera imfunguruzo z’ibanga atari mu murongo, arakenera igikoresho kidakorana n’urubuga ubudasiba, haba ari [Hardware Wallet](https://planb.network/resources/glossary/hardware-Wallet) canke mudasobwa ifise ikirere, yihariye gukora iyo nzira yihariye.



Wobikora gute nimba nk’akarorero udafise ubushobozi bwo kugura ibikoresho bikora ico gikorwa gusa, mugabo ntushaka kureka iyo ntambwe y’umutekano?



## Umuti


None iyo nkubwira ko woshobora gukora igikoresho kitari ku murongo mu buryo bwa mudasobwa y’umuyagankuba ingana n’ubunini n’uburemere bwa flash drive ya USB kandi ikaba igura ama euro 35? None ntiwovyemera?



Bandanya usome.



Nzobabwira n’ibindi: soma inzira yose. Umuti ushikirijwe ni uwuhenda, ariko si wo nyawo woroshe kuruta iyindi yose. Ubanza kuronka iciyumviro rusangi, hanyuma ugafata ingingo yo gukoresha umwanya wawe mu bushakashatsi bumwebumwe bw’umuntu ku giti ciwe maze ugahitamwo, ufise amahoro yo mu mutima uko bishoboka kwose, nimba wobikora be n’ingene wobikora.



## Ibisabwa


**1** A [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (ata n’imwe igira inyuma) ni yo shingiro ryo kwubaka mudasobwa ikora neza cane, ariko hejuru ya vyose nta makarita ya Wi-Fi na Bluetooth ifise, ibisabwa kugira ngo ivyo bishoboke.





- Igiciro**: nk’isaha cumi n’itanu igihe twandika iyi nyigisho (Myandagaro 2025).
- Gukomeza gukora**: Raspberry itanga icemeza ko izokora gushika muri Mukakaro 2030.



PI Zero zitagira Wi-Fi na Bluetooth, ikibabaje ni uko zitaboneka. Ushobora kuronka uburyo bwo gukoresha PI Zero W na PI Zero 2W mu buryo bworoshe. Muri iki gihe, ushobora guhagarika ibikorwa vy'ihuriro mu guhindura dosiye ya config. Uhejeje gushiramwo ubuhinga bwo gukoresha, uzokenera kwongerako ibi bintu kuri config:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



igice c’iyi nsiguro kizokwereka ingene wobikora n’aho wobikora. Ariko rero, nimba vy’ukuri ushaka kumenya neza, urashobora kuronka inyigisho nyinshi ku rubuga zo gukuraho igice ca Wi-Fi ukoresheje agace gatoyi k’uguca, ubwoko bubereye gukoresha ku bipande vy’ubuhinga bwa none.



**2** _Igikoresho co gutangura_ ca Raspberry PI Zero: nk'uko bimeze mw'isi ya Raspberry, amagufa atagira ikintu, ata n'ikibazo co hanze. Vyongeye, ubutunzi buke bw’ico kigo gitoyi buratuma umuntu ashobora gukorana n’isi yo hanze.



Igihe nafata ingingo yo kubandanya, nasanze [iki . 1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+vant+geeek+pi%2Caps%2C88 ubushobozi bwose bwa PI Zero. Nkako, iyo kit irimwo USB A -> micro USB power Supply, akazu gatoyi ka USB, adapteur ya mini-HDMI -> HDMI, igikoresho co gukura ubushuhe c’umuringa, n’igikoresho co hanze c’aluminium. Ivyo bikoresho kandi birimwo n’ibikoresho vyo gushiramwo PI Zero mu gitereko gishasha.





- Igiciro**: 19,99 amayero.



**3** Iyi nyigisho ntigusaba ko ukoresha amahera menshi kuri mudasobwa ya airgap. Ariko rero, urakwiye kumenya ko uzokenera klavye n’imbeba vya USB (bifise amabara akomeye, wirinde Bluetooth) n’ikigaragaza. Bivanye n’ivyo winjiza kuri moniteur yawe, ushobora gukenera adapteur iva kuri mini-HDMI, iyo nzira yonyene iboneka kuri PI Zero. Ubwa nyuma, raba Hard kubera yuko twese dufise keyboard n’imbeba bitagira umurongo mu nzu ahantu-ni igihe co kubizimya Dust.



## Ingengo y'imari y'inyongera



**4** Ushobora kuronka ubushobozi bw’umwimerere Supply kuri Raspberry, bugura ama euros nka 15.00.



**5** Jewe ubwanje nahisemwo gukoresha ububasha Supply butanzwe mu _starter kit_, ndabufatanya, ariko, n’umugozi wa USBA → miniUSB witwa `no data`, ugura amayero 3,70.



**6** Ikarata ya micro SD, kugira ngo ibe n’ububiko bw’ibintu vyinshi bugera kuri 32 GB; iyo uburyo/urugero rw’inganda ari rwiza.



**7** Uzokenera system, adapteur ya USB kuri micro SD, nk’iyo ubona kw’ifoto. Sisitemu ikoresha ya PI Zero yawe n’ubuhinga bwayo bwo kwibuka, mu vy’ukuri, bizokora kuri iyo media.



![img](assets/it/06.webp)



## Gushiramwo sisitemu ikoresha


Imbere yo gufunga PI Zero yawe mu kibanza, ndagusavye gushiramwo ubuhinga bwo gukoresha. Uzoheza ushobore kugenzura LED yerekana ko ikora, uhereye ku nkoko.



Kugira ngo mpitemwo no guturira uburyo bwo gukoresha, nahisemwo uburyo bworoshe: gukoresha igikoresho ca Raspberry`s `PI Imager`.



![img](assets/it/01.webp)



Genda kuri [Raspberry Github](https://github.com/raspberrypi/rpi-imager/releases) kugira ngo ubone igisohoka gishasha ca Imager, uhitemwo ico kibereye cane ubuhinga bwawe bwo gukoresha (umurongo wa 1.9.6 igihe twandika). Uzobona ko iruhande y’itunga ryose hariho kandi Hash y’idosiye ihuye. Ivyo bizoba ngirakamaro mu kugenzura.



![img](assets/it/02.webp)



Ndagusavye ko wosuzuma uburyo uzoba uriko urakoresha kuri mudasobwa yawe ya airgap, kugira ngo wewe ubwawe ugire amahoro yo mu mutima. Ivyo bizokuronsa icizigiro c’uko uriko ukoresha verisiyo yemewe (itari mbi) ya Imager kandi, kubera ivyo, Raspi OS.



Ubwo nyene umaze gukuraho, imashini yawe usanzwe ukoresha ihuye na Internet .



Hanyuma ufungure terminal ya Linux maze utegure ivyo uzokura, ukore ububiko bwa `raspios` ngirakamaro mu gukorana na bwo.



![img](assets/it/19.webp)



Gukuraho Imager ku Linux yawe ukoresheje `wget`.



![img](assets/it/20.webp)



Ubwa nyuma, ukoreshe itegeko rya dosiye `sha256sum` maze ugereranye Hash n’iyo Raspberry yatanze muri Github yayo.



![img](assets/it/21.webp)



Canke, nimba ufise Windows, fungura Power Shell wandike itegeko rikurikira:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Uzoronka Hash itegerezwa guhura n’iyo yasohowe kuri Raspberry Github.



Umaze kugenzura ko ivyo waronse, urashobora gushiramwo Imager kuri mudasobwa yawe ya misi yose maze ukayifungura. Imager ni igikoresho ukeneye kugira ngo uturire umurongo w'ibikorwa kuri micro SD, iyo na yo ikaba ari "system disk" ya PI Zero.



Ivyo bikorwa ni vyoroshe cane: banza uhitemwo igikoresho ca Raspberry uzokoresha (rero witwararike **model yawe** ya Raspi Zero), hanyuma ushiremwo verisiyo ya OS, hanyuma uhitemwo aho ikarita ya micro SD izoshirwa kugira ngo ushireko OS.



### Intambwe yambere



![img](assets/it/03.webp)



### Intambwe ya kabiri



![img](assets/it/07.webp)



**Iciyumviro neza**: uhitemwo `PI OS 32-bit`, ni yo yonyene ikorana na PI Zero.



### Intambwe ya gatatu



![img](assets/it/08.webp)



(Urabe maso cane ngo usige _Exclude System Drive_ yatowe kugira ngo ntusabwe gushiramwo ubuhinga bwa Raspi kuri mudasobwa yawe.)



Igihe vyose bimaze gutegurwa, Imager izokubaza nimba woshima gukoresha amasetingi y’ibintu vy’umuntu ku giti ciwe. Hitamwo ico ushaka, canke ukande _Oya_ kugira ngo ukomeze n'amahitamwo mburabuzi.



![img](assets/it/09.webp)



Wemeze ko ushaka gukuraho ibiri muri micro SD



![img](assets/it/10.webp)



Imager itangura guca ibibatsi kuri micro SD, umurongo w’uguhindura uzokumenyesha ingene bigenda.



![img](assets/it/11.webp)



Ku mpera hariho ukugenzura kwikora, ndabagira inama yo kutabihagarika.



![img](assets/it/12.webp)



Amaherezo ubutumwa buraboneka ku rubuga, kandi nimba vyose vyagenze neza, bisa n’ivyo usoma kw’ishusho.



![img](assets/it/13.webp)



Ubu ushobora vy’ukuri gukuraho micro SD mu gisomyi maze ukayishira mu gice ca PI Zero. Inguvu zibe kuri Raspberry ntoyi maze wihweze LED: twiteze ko ari Green kandi ikazimya, yerekana ko ubuhinga bwo gukoresha busanzwe bukoreshwa, hanyuma igakomeza gucana. Niwabona ibindi bimenyetso, nk’akarorero iyo LED izimvye incuro zisanzwe canke ikaba itukura, raba FAQ canke [amapaji y’ihuriro ry’infashanyo](https://forums.raspberrypi.com/).



## Itunganywa rya mbere


Intango ya mbere ya Raspi OS iragenda buhoro gatoyi kuruta uko bisanzwe kuko itegerezwa gukora ibikorwa vy’ugushiraho vy’ukuri. Ariko vyose nivyagenda neza, uzosanga igicapo c’akabazo.



![img](assets/it/14.webp)



Fyonda kuri _Ibikurikira_ kugira ngo ushireho akarere, cane cane kugira ngo ushiremwo klavye ibereye. Niwitwararike cane ivyo vya nyuma.



![img](assets/it/15.webp)



Fyonda kuri _Next_ uzosabwa gukora user yawe, wandike amakuru yawe maze uyazigame neza.



![img](assets/it/16.webp)



Umupfumu akusaba guhitamwo umucukumbuzi w'urubuga, hagati ya Chromium na Firefox; ishobora kandi kukubaza ivyerekeye imiterere y’urubuga rwa Wi-Fi nimba ukorana na Zero W canke 2W PI. Genda ukande _Skip_.



Hari igihe uzosabwa guhindura porogarama n’uburyo bwo gukoresha biri mu ndege. Hitamwo _Skip_: ku ntumbero z'iki gikorwa mu vy'ukuri turiko turakora imashini itari ku murongo, itegerezwa kuguma itari ku murongo kuva ubu.



Ubwa nyuma, bishobora kugusaba gukoresha `ssh`, ariko n'iyi ntambwe na yo nyene uyishire, kuko ari Zero airgap IP.



![img](assets/it/17.webp)



Nta vyinshi vyo gutunganya. Niwaheza, subiramwo Raspberry kugira ngo amahinduka agire ico akora.



![img](assets/it/18.webp)



## Igihombo gishasha ca mudasobwa


Amaze gusubira gufungura, mudasobwa yawe nshasha ya airgap irateguye. PI Zero ikwereka desktop nshasha, ushobora gukorana nayo biciye ku GUI canke ukoresheje umurongo w'amabwirizwa.



![img](assets/it/22.webp)



### Intambwe zambere za PI Zero W canke 2W


Niba ukoresha urutonde rwa Raspberry PI Zero W canke 2W, urupapuro rwawe rufise ibice vya Wi-Fi na Bluetooth ku rupapuro. Mu gihe c’ugutegura kwa mbere warasivye ivy’uguhuza, rero PI Zero ntihuye na Internet. Ubu rero urashobora guhagarika izo chips zibiri ubuziraherezo biciye kuri porogarama.



Nkako, Raspi OS itanga dosiye `config.txt` ushobora guhindura uko ushaka. `Config` iri mu gice ca `boot`, mu bubiko bwa `firmware`, kandi ushobora kuyihindura no kuyibika ukoresheje uburenganzira bwa `root`.



Gufungura terminal kuva ku kimenyetso kiri hejuru ibubamfu maze ibe `umuzi`.(1)



![img](assets/it/23.webp)



(1) Niba Raspi OS itagufise ngo ureme ijambobanga rya `root` mu ntambwe za kera, ndagusavye ko ubikora ubu, ukoresheje itegeko rya `passwd`. Kugira umukoresha `umuzi` yigendereye umukoresha wawe bwite birashobora kwemeza ko ari vyiza cane mu bihe vyo gukira.



Na terminal, reba dosiye `config.txt` maze witegure kuyihindura ukoresheje umuhinduzi wa `nano`.



![img](assets/it/24.webp)



Ivyo guhindura bikwiye gukorwa ahantu hasi muri `config` yose, inyuma y'amajambo `[All]`. Ni muri iki gihe uzokwongerako amabwirizwa `dtoverlay` yerekanwa mu ntango y'inyigisho.



![img](assets/it/25.webp)



Bika, ufunge, wongere utangure. Mu ntambwe ikurikira tuzoja ku gutohoza aka Raspberry gatoyi.



## Ni igiki wokwitega kuri iki gikoresho?


Turavye [ibisobanuro vy’ubuhinga](https://www.raspberrypi.com/products/raspberry-pi-zero/) bivuye ku rubuga rwa Raspberry, PI Zero ifise umurongo umwe BCM2835 n’ubuhinga bwa RAM 512 MB, rero ntibisa n’ibikomeye cane.



Kubera ko terminal iremereye, tuzokoresha umurongo w’amabwirizwa kugira ngo turonde imiterere ya sisitemu.



Iyo ushizeho umuriro uzobona igicapo gitoyi c’ibara ry’umunywamazi, gikurikiwe n’ubutumwa bwo kwakira buva kuri Raspberry, mu mfuruka yo hasi ibubamfu, ubutumwa bwa kernel bujanye n’ugutangura.



Igihe PI OS desktop ibonetse, fungura terminal wandike:



```bash
uname -a
```


Iri tegeko rizokwereka verisiyo ya kernel iriko irakoreshwa ubu ku rubuga, hamwe n'ayandi makuru.



![img](assets/it/26.webp)



Ushobora kandi kubona amakuru kuri CPU na hardware wandika:



```bash
lscpu
```



![img](assets/it/27.webp)



Kandi urabe `ivyiza/ivyigwa/amakuru`.



![img](assets/it/28.webp)



Kugira ngo umenye verisiyo ya Debian n'izina ry'isohoka:



"bash"


lsb_gusohora -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



"bash"


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Gukoresha


Naho ubushobozi busa n’ubuke (ku mpapuro no kugereranywa n’ububasha bw’amamashini y’ubu) PI Zero irakora cane cane nk’ibarabara ry’inyuma.





- Ubwa mbere ushobora kuja mu bimenyetso nyamukuru maze ugahumekerwa n'igice ca _Add/Remove software_, aho uzosanga ibikoresho vyinshi vyo gukora porogarama no kwimenyereza. Ibuka ko ushobora no kubikora uri ku nzira, ariko wama ufise uburenganzira bwa `root`.



![img](assets/it/33.webp)





- Ushobora "kwemera" iki gikoresho kitari ku murongo kugira ngo ubike inyandiko zitandukanye z'ibanga, zizoguma ziboneka igihe bikenewe, ata na rimwe ziboneka kuri Internet.
- Ushobora gukoresha iyi ntunganyo kugira ngo generate imfunguruzo zawe za GPG ata nkomanzi.
- Woshobora mbere gukoresha ako "agakinisho gatoyi" gashasha nk'igikoresho co gusinya ku nzira y'ikirere, [mu gukurikiza impanuro za Arman The . Parman](ingene-woshinga-umuyagankuba-pi-utagira-umuyaga-ukoresha-verisiyo-nshasha-y'umuyagankuba-Wallet-85e59ecaddc0).



Mu Wallets nzi neza, imwe gusa itanga isohoka ry’ibice 32 ni Electrum. Erega: Zero IP nk’uko twayiteguye muri iyi nyigisho yogufasha kuguma ufise imfunguruzo z’ibanga zitari ku murongo w’ivyo twashizeho ku bijanye n’ikirere ca Wallet twavuze muri iyi nyigisho:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Insozero


Ivyo bikoresho birafise, kumbure, intege nke imwe nini: micro SD ni uburyo bwo gutanga ingorane. Ni ikintu gishobora gukoreshwa cane; kumbure uramaze kumenya ivyo, uhereye ku kubikoresha na telefone yawe. Uhejeje gushiramwo porogarama zose uzoshaka gukoresha kuri Zero airgap IP, ukore backup nziza ya micro SD y’agaciro, ukoresheje igikoresho ca Raspi OS ufise.



![img](assets/it/34.webp)



Uko ivyo ukeneye bigenda birakura, kandi n’ubushobozi bwawe bwo gukoresha ingengo y’imari, urashobora gutohoza ibindi bisubizo vya Raspberry canke bisa n’ivyo. Ku bijanye n’ukwibuka, nk’akarorero, PI 5 itanga ubushobozi bwo gukoranya umuduga wa M2 NVME, uwo na wo ukaba ukomeye cane kuruta microSD.



Ntukibagire gufata amajambo no kwandika intambwe yose y’ugushiramwo porogarama y’ubuhinga ugiye gukoresha utari mu nzira. **vuba canke vuba hazosohoka Raspi OS ivuguruwe** uzoshaka ata kabuza kuvyungukirako. Aho uzobwirizwa gukuraho vyose ugasubira kubikora vyose (kumbure ukoresheje micro SD nshasha 😂).



Imyimenyerezo twahejeje gukora, twiyumvira ko ari igerageza ryawe rya mbere na ryo nyene, uzoribuka igihe kirekire. Si ko vyama bishoboka gutanga ibikoresho ku bikorwa `bishizwemwo` bitari mu murongo, ata kwirengagiza kwitwararika imashini ifise umwuka wo gufungura no kugenzura rimwe na rimwe.



Ariko rero, warabikoze, ndagushimiye! Kandi uzoshobora gutanga ivyiyumviro vy’uwo muti ku bantu bose bakeneye kuguma bafise ingengo y’imari hasi.