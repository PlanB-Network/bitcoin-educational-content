---
name: My Node
description: Gushiraho Bitcoin yawe Node yanje
---

![image](assets/0.webp)


[Igikoresho canje](https://mynodebtc.com/) ni uburyo bworoshe, bukomeye bwo gukoresha igikoresho ca Bitcoin n’ica Lightning! Turahuza porogarama nziza cane zifunguye na Interface yacu, uburongozi, n’ugushigikira kugira ngo ushobore gukoresha Bitcoin na Lightning mu buryo bworoshe, mu mwiherero, kandi ata nkomanzi.


## Ubwoko bw'imiterere y'urudodo


Hariho uburyo butandukanye bwo gutegura Node. MyNode ni nziza cane. Hariho apps nyinshi zijana nazo, mbere n’izindi nyinshi iyo urishe version ya premium. Ahandi ho biraruhije cane gukuraho izo apps zose wewe nyene. MyNode iratuma vyoroha cane nk’uko uzobibona.


Iyindi nzira kandi isa n’iyo ni RaspiBlitz. GUI si nziza nk’iyo, kandi amaporogarama arahurirana cane n’amaporogarama azana na MyNode, ariko Raspiblitz ni porogarama y’ubuntu (FOSS) kandi MyNode ntabwo ari yo. Iyindi ntandukaniro ni uko MyNode ikoreshwa mu gikoresho ca Docker. Nsanga Docker iteye ubwoba na Hard yo gutorera umuti ingorane. Ivyo ni ingorane gusa iyo uhuye n’amakosa canke ibikoko. Uwo muhinguzi atanga imfashanyo ku bakoresha ba premium kandi hariho n’umugwi wo kuganira kuri Telegram.


RaspiBlitz ni porogarama nyinshi gusa zishizwe kuri Linux, ata Docker. Igikoresho co hanze ca Hard gishobora gufatanywa bitagoranye n’iyindi mashini ya Linux ifise Bitcoin core, kandi kure uragenda, iyo ukeneye.


Iyindi nzira ni ugushiramwo gusa Bitcoin core n’ubwoko bwa Electrum Server (hariho bwinshi) kuri sisitemu ikoresha. Ndafise ubuyobozi bwo gukoresha Linux (Raspberry Pi), Mac, na Windows.


## Urutonde rw'ibisuma



- Pi 4, ububiko bwa 4Gb canke 8Gb (4Gb ni vyinshi)
- Inguvu za Raspberry Pi zizwi (Birahambaye cane! Nturonke ivy’urugero, vy’ukuri)
- Ikibazo c’aba Pi. Ikibazo ca FLIRC ni ikintu giteye ubwoba. Ico gikoresho cose ni igikoresho co gukura ubushuhe kandi ntukeneye umuyaga, ushobora gutera urusaku
- 16 Gb microSD card (urakeneye imwe, ariko nkeyi zirafasha)
- Igikoresho co gusoma ikarita y’ububiko (mudasobwa nyinshi ntizizogira aho zishobora gushiramwo ikarita ya microSD).
- Inyuma SSD 1Tb Hard umuduga.

Iciyumviro: SSD ni ikintu gihambaye cane. Ntukoreshe umuduga wa Hard wo hanze naho woba uhendutse


- Umugozi wa ethernet (wo gufatanya na router yo muhira yawe)
- Ntukeneye umugenzuzi


## Kuvanaho ishusho ya MyNode


Kuja ku rubuga rwa MyNode


![image](assets/1.webp)


Fyonda `Kuvana ubu`


Gukuraho verisiyo ya Raspberry Pi 4:


![image](assets/2.webp)


Ni dosiye nini:


![image](assets/3.webp)


Kuvanaho amajambo ya SHA 256


![image](assets/4.webp)


Gufungura terminal kuri Mac canke Linux canke ku rubuga rwa Windows. Ubwoko:


```bash
shasum -a 256 DOWNLOADEDFILENAME # <--- Mac/Linux
certUtil -hashfile DOWNLOADEDFILENAME SHA256 # <--- Windows
```


Iyo orodinateri irazirikana amasegonda 20 canke arenga. Hanyuma, usuzume ko hashfile y’isohoka ihuye n’iyo wakuwe ku rubuga mu ntambwe ibanza. Nimba ari kimwe, urashobora gukomeza.

Gukayangana ikarita ya SD


## Gukuraho no gushiramwo Balena Etcher. Urubuga


Nta n’umwe nashoboye kuronka umukono wa digitale w’ivyo. Niba uzi uko bigenda, ndagusavye umbwire nzosubiramwo iyi nkuru.


Etcher ni iyo kwisigura gukoresha. Injira ikarita yawe ya micro SD hanyuma ushireko porogarama ya Raspberry Pi (dosiye .img) kuri ikarita SD.


![image](assets/5.webp)

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

![image](assets/10.webp)

![image](assets/11.webp)


Iyo bimaze gukorwa, iyo drive ntiba igishobora gusomwa. Ushobora kuronka ikosa riva kuri sisitemu ikoresha, kandi umuduga ukwiye kuzimangana kuri mudasobwa. Kura iyo karata.


## Gushiraho Pi no kwinjiza ikarita SD


Ibice (ikibazo ntivyerekanwa):


![image](assets/12.webp)

![image](assets/13.webp)


Huza umugozi wa ethernet, n’umugozi wa USB wa Hard (nta nguvu iracariho). Irinde gufatanya n’ibikoresho vya USB vy’ibara ry’ubururu biri hagati. Ni USB 3. MyNode iragusavye gukoresha port ya USB 2, naho nyene iyo drive yoba ishobora gukoresha USB 3.


![image](assets/14.webp)


Ikarata ya micro SD ija hano:


![image](assets/15.webp)


Ubwanyuma, huza ubushobozi:


![image](assets/16.webp)


## Rondera IP Address ya Pi


Ntiwigera ukenera umugenzuzi afise MyNode. Ariko rero, urakeneye uwundi mudasobwa uri ku rubuga rwo muhira. Nimba Pi yawe idahuye na ethernet, kandi ushaka kwizigira WiFi, kuronka IP bisaba ubuhinga bwo gukoresha mudasobwa bwo ku rwego rwo hejuru. Ntashobora kugufasha, mbabarira. Ukeneye uruja n’uruza rwa ethernet. (Ikibazo kiva ku gukenera gushika ku moniteur na operating system kugira ngo ushobore kwifatanya na WiFi no kwinjiza ijambo banga).


Suzuma router yawe, kugira ngo ubone urutonde rw’ama IP yose y’ibikoresho vyose bihuye.


Nanditse 192.168.0.1 muri Mucukumbuzi (amabwirizwa yaje na router yanje), ndinjira, maze ndashobora kubona igikoresho “MyNode” gifise IP 192.168.0.18. Iyumvire ko izo IP addresses zitaboneka ku mugaragaro kuri internet (zibanza guca kuri router), ni ibimenyetso gusa vy’ibikoresho biri ku rubuga rwawe rwo muhira.


Kuronka IP ni ikintu gihambaye cane.


**Iciyumviro:** ushobora gukoresha terminal iri ku mashini ya Mac canke Linux kugira uronke IP Address y’ibikoresho vyose bihuye na Ethernet ku rubuga rwo muhira ukoresheje itegeko “arp -a”. Ivyo usohora si vyiza nk’ivyo router izokwerekana, ariko amakuru yose ukeneye arahari. Niba bitagaragara neza ko ari Pi, gerageza n’amakosa.


## SSH muri Pi


Ufise uburenganzira bwo kwinjira mu gikoresho uri kure n’itegeko rya SSH, ariko ntibisabwa (ni iyo RaspiBlitz Node). Nzokwereka ingene bimeze, kuko ari vyiza cane.


Gufungura mudasobwa Mac canke Linux (ya Windows, ushireko putty, igikoresho ca SSH) wandike:


```bash
ssh admin@192.168.0.18
```


Koresha IP yawe bwite Address. Izina ry’ukoresha ry’igikoresho ca MyNode ni “admin” ku buryo busanzwe. Ijambobanga ni “Bolt” ku buryo busanzwe.


Niba warakoresheje Pi yawe mbere ugahindura micro SD card, uzobona iri kosa:


![image](assets/17.webp)


Ico ukeneye gukora n’ukuja aho dosiye “known_hosts” iri maze ukayifuta. Ni vyiza ku. Ubutumwa bw'ikosa burakwereka inzira. Kuri jewe yari /Abakoresha/Izina ryanje/.ssh/


Ntimwibagire “.” imbere ya ssh, ibi vyerekana ko ari ububiko bwihishije.


Hanyuma wongere ugerageze itegeko rya ssh.


Ubu uzobona iki gisohoka:


![image](assets/18.webp)


Dosiye wasivye yasivye kandi uriko wongerako urutoke rushasha. Andika yego na <winjize>.


Uzosabwa kwinjiza ijambobanga. Ni “Bolt” .


Ubu ufise uburenganzira bwo gukoresha MyNode Pi, ata n’ikigenzura, kandi ushobora kwemeza ko vyose vyuzuye neza.


![image](assets/19.webp)


## Ushobora kuronka biciye ku mucukumbuzi w'urubuga


Gufungura umucukumbuzi. Bikenewe ko ari mudasobwa iri ku rubuga rwawe rwo muhira, ivyo ntushobora kubikora uri hanze. Hari inzira, ariko ni Hard. Nta n’umwe nabigerageje.


Andika IP Address mw'idirisha ry'umucukumbuzi Address. Ivyo bizoshika:


![image](assets/20.webp)


Injira ijambobanga “Bolt” – urihindure mu nyuma.


Hanyuma ibi bizoshika:


![image](assets/21.webp)


Hitamwo uburyo bwo gutwara umuvuduko


![image](assets/22.webp)


None rero turindiriye.


Hari igihe uzobazwa nimba ushaka gushiramwo urufunguzo rw’igicuruzwa cawe, canke ukoreshe “igitabu c’abanyagihugu” c’ubuntu — ngiye kwerekana igitabu ca Premium. Ndabagira inama yo kwishura verisiyo ya premium nimba mushobora kuyigura, birabereye cane.


![image](assets/23.webp)


Uzoca ubona ingene ama blocks yashizweho atera imbere. Bifata imisi:


![image](assets/24.webp)


Ni vyiza kuzimya imashini mu gihe co kuyikurako nimba ukeneye. Genda kuri settings urondere buto yo kuzimya imashini. Ntukikure umugozi gusa, woshobora kwonona installation canke umuduga wa Hard.


Raba neza, kare, genda kuri”Ivyagezwe” maze uzimye quicksync. Izotangura gukuraho igice ca mbere kuva mu ntango.


![image](assets/25.webp)


Nashaka gukomeza n’uguhingura iyo nzira, rero ng’iyi iyindi MyNode nateguye mbere. Uko ni ko iyo paji isa iyo Blockchain ihuriweko, kandi “amaporogarama” menshi yarafunguwe kandi arahuzwa:


![image](assets/26.webp)


Zirikana ko Electrum Server na yo nyene ikeneye gukorana, rero Bitcoin Blockchain ikimara gukorana, fyonda ku buto kugira ngo utangure iyo nzira – bifata umusi umwe canke ibiri. Ibindi vyose birashobozwa mu minota mikeyi iyo umaze guhitamwo kubishoboza. Ushobora gukanda ibintu maze ukabitohoza. Nta kintu uzomena. Iyo hari ikintu kivunitse (ivyo vyaranshikiye, ariko nibwira ko kubera nari mfise ibice bihendutse) uzobwirizwa gusubira gucapura maze ugasubira gutangura gukuraho. Ikibazo mfise kuri MyNode ni uko iyo ukeneye “re-flash” uheza ugakenera gusubira gutangura sync ya Blockchain uhereye ku ntango. Hari uburyo bwo gutorera umuti ivyo, ariko ntivyoroshe.


Niba ushaka kugerageza n’iyindi node, tuvuge RaspiBlitz, ukeneye SSD y’inyongera y’inyuma Hard drive, n’iyindi micro SD card yo guca ibibatsi. Ahandi ho, n’ibikoresho bimwe, ntushobora gukoresha MyNode na RaspiBlitz icarimwe, biragaragara. Niba ushaka gukora ivyo, igihe co kugura uwundi Raspberry Pi.


None ko ufise node iriko irakora, uyikoreshe, ntuyireke gusa yicare aho ataco ikugiriye. Kurikira ingingo yanje (na videwo) yerekeye ingene wohuza Desktop yawe ya Electrum Wallet na Server ya Electrum na Bitcoin core hano.