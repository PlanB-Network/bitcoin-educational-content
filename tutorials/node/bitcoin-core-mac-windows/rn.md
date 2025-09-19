---
name: "Bitcoin Core (macOS & Windows)"
description: Shiraho Bitcoin core kuri Mac canke kuri Windows
---
![cover](assets/cover.webp)


Gushiramwo Bitcoin core kuri mudasobwa yawe isanzwe birashoboka, ariko si vyiza. Niba udafise ikibazo co gusiga mudasobwa yawe 24/7, rero ivyo bizogenda neza. Iyo ukeneye kuzimya orodinateri, birababaza kurindira ko porogarama ikorana igihe cose usubiye kuyifungura.


Aya mabwirizwa ni ay’abakoresha Mac canke Windows. Abakoresha Linux ntibazokenera imfashanyo yanje cane, ariko amabwirizwa ya Linux asa cane na Mac.


## Gutangura gusukura


Ivyiza ni uko woba ushaka gukoresha orodinateri isukuye, idafise ibintu bibi. Naho woba ukoresha Hardware Wallet, malware irashobora kuguhenda mu biceri vyawe.


Ushobora guhanagura mudasobwa ya kera, ukayikoresha nk’umudasobwa yihariye Bitcoin, canke ukagura mudasobwa/laptop yihariye.


## Umuduga wa Hard


Bitcoin core izotwara amakuru agera kuri 400 gigabytes kuri drive yawe, kandi izobandanya gukura. Ushobora gukoresha umuduga wawe wo mu mutima, ariko ushobora no gufatanya umuduga wo hanze Hard. Nzobasigurira izo nzira zompi. Ivyiza ni uko wokoresha umuduga ukomeye. Niba ufise mudasobwa ya kera, birashoboka ko ata n’imwe muri izo ifise imbere. Gusa ugura SSD yo hanze y’amaterabyte 1 canke 2 maze ukoreshe iyo. Ivyo gutwara imodoka bisanzwe birashoboka ko bizokora, ariko woshobora guhera mu kugira ibibazo kandi bizogenda buhoro cane.


![image](assets/fr/01.webp)


## Gukuraho Bitcoin core.


Genda kuri Bitcoin.org (urabe neza ko utaja kuri Bitcoin.com, ari urubuga rw’amahera y’ibinyoma rwa Roger Ver, ruhenda abantu ngo bagure amahera ya Bitcoin aho kugura amahera ya Bitcoin)


Iyo umaze gushikayo, biratangaje ko ataco bigaragara aho woronka iyo porogarama. Genda ku rutonde rw’ibikoresho maze ukande kuri “Bitcoin core”, nk’uko vyerekanwa aha hepfo:


![image](assets/fr/02.webp)


Ivyo bizokujana kuri paji yo gukuraho:


![image](assets/fr/03.webp)


Fyonda kuri buto ya Bitcoin core y'umutuku:


![image](assets/fr/04.webp)


Hariho uburyo bwinshi bwo guhitamwo, bivanye n’ivyo mudasobwa yawe ikoresha. Ivyo bibiri vya mbere birafitaniye isano n’iyi nsiguro; hitamwo Windows canke Mac ku ruhande rw’ibubamfu. Izotangura gukurwako umaze kuyikanda, bishoboka cane ko izoja mu bubiko bwawe bw’Ivyakuweko.


## Genzura ivyo waronse (igice ca 1)


Ukeneye dosiye irimwo ama hashes y'ibisohoka bitandukanye. Iyi dosiye yahora iri kuri paji y’ivyo gukura kuri Bitcoin.org, ariko ubu yaje kuri bitcoincore.org/ru/gukura:


![image](assets/fr/05.webp)


Ukeneye dosiye y'ibice bibiri SHA256. Iyi dosiye irimwo SHA256 hashes z'amapaki atandukanye yo gukuraho ya Bitcoin core.


Inyuma y’aho, turakeneye gukora Hash kuri Bitcoin core maze tukayigereranya n’ico dosiye ivuga ko Hash ikwiye kuba. Hanyuma tukamenya ko ivyo gukuraho bisa n’ivyo umuntu yiteze, nk’uko bivugwa kuri bitcoincore.org.


Subira ugende ku bubiko bw’ivyo ushobora gukuraho maze ukore iri tegeko (subiriza X’s izina rya dosiye y’ivyo ushobora gukuraho Full node Bitcoin neza na neza):


```bash
shasum -a 256 XXXXXXXXXXXX # <--- FOR MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- FOR WINDOWS
```


Uzoronka igisohoka ca Hash. Bishire ahabona, hanyuma ubigereranye na Hash iri muri dosiye SHA256SUMS.


Niba ibisohoka bisa, rero warasuzumye ko ata n’agace k’amakuru kahinduwe... hafi. Turacari dukeneye kumenya neza ko dosiye SHA256SUMS atari mbi.


Kugira ngo dukomeze intambwe ikurikira, dutegerezwa kuba dufise gpg kuri mudasobwa yacu.


Kugira ngo ubikore, raba uburongozi bwanje bwa SHA256/gpg, hanyuma ugende nk’igice c’igice kivuga ngo “Download gpg”, hanyuma urondere umutwe mutoyi wa sisitemu yawe ikoresha. Hanyuma rero mugaruke ngaha.


## Kuronka urufunguzo rwa bose


Subira kuri paji yo gukuraho, rondera dosiye y'imikono ya SHA256 Hash


![image](assets/fr/06.webp)


Uyifyondeko maze ubike iyo dosiye kuri disiki, vyiza ni ububiko bw’ivyo ushobora gukuraho.


Iyi dosiye irimwo imikono y'abantu batandukanye, ya dosiye SHA256SUMS.


Turashaka urufunguzo rwa bose rw’umuhinguzi, Wladimir J. van der Laan ku rufunguzo rwa mudasobwa yacu. Indangamuntu yiwe y'urufunguzo rwa bose ni:

1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964


Kopa ico canditswe muri iri tegeko rikurikira:


```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```


Kubera inyungu, igihe cose, ushobora kubona imfunguruzo ziri mu mfunguruzo za mudasobwa ukoresheje iri tegeko:


```bash
gpg --list-keys
```


## Suzuma ivyo waronse (igice ca 2)


Turafise urufunguzo rwa bose, rero ubu turashobora kugenzura dosiye SHA256SUMS irimwo ama hashes y'ivyo Bitcoin core yaronse, n'umukono w'ayo ma hashes.


Ugurure Terminal canke CMD kandi, maze urabe neza ko uri mu bubiko bw’Ivyakuweko. Uvuye ng'aho, shira mu ngiro iri tegeko:


```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```


Dosiye ya mbere iri ku rutonde ni inyandiko nyayo ya dosiye y'umukono. Dosiye ya kabiri iri ku rutonde ikwiye kuba inyandiko nyayo ya dosiye y'inyandiko irimwo ama hashes. Izo dosiye zompi zikwiye kuba mu bubiko bumwe kandi ukeneye kuba mu bubiko bw'amadosiye, ahandi ho, utegerezwa kwandika inzira yuzuye ya dosiye yose.


Iyi ni yo nkuru ukwiye kuronka


![image](assets/fr/07.webp)


Ni vyiza kwirengagiza ubutumwa bw’IBURIRO – ubwo ni ukukwibutsa ko utahuye na Wladimir ku gice c’urufunguzo maze ukamubaza ubwawe urufunguzo rwiwe rwa bose, hanyuma ukabwira mudasobwa yawe ko yizigira urwo rufunguzo bimwe bishitse.


Niba wararonse ubu butumwa, ubu urazi ko dosiye SHA256SUMS.asc itahinduwe inyuma y’aho Wladimir ayishizeko umukono.


## Gushiramwo Bitcoin core


Ntukwiye kukenera amabwirizwa arambuye yerekeye ingene woshiramwo iyo porogarama.


![image](assets/fr/08.webp)


## Kwiruka Bitcoin core


Ku Mac, ushobora kuronka imburi (Apple iracari anti-Bitcoin)


![image](assets/fr/09.webp)


Fyonda OK, hanyuma ufungure Ivyo Ukunda


![image](assets/fr/10.webp)


Fyonda kuri Icon y'Umutekano n'Ibanga:


![image](assets/fr/11.webp)


Hanyuma ukande “fungura uko biri kwose”:


![image](assets/fr/12.webp)


Ikosa rizosubira kugaragara, ariko ubu uzoba ufise buto OPEN iriho. Kandako.


![image](assets/fr/13.webp)


Bitcoin core ikwiye gufunguka kandi uzoshikirizwa amahitamwo amwe amwe:


![image](assets/fr/14.webp)


Aha ushobora guhitamwo gukoresha inzira y’imbere y’aho Blockchain izomanurwa, canke ushobora guhitamwo umuduga wawe wo hanze. Ndabagira inama yo kudahindura inzira y'imbere nimba ugiye gukoresha umuduga wo mu mutima, bituma ibintu vyoroha gushinga iyo ushizeho izindi porogarama zo kuvugana na Bitcoin core.


Ushobora guhitamwo gukoresha node ya pruned, birazigama umwanya, ariko bikagabanya ivyo ushobora gukora n’urudodo rwawe. Uko biri kwose, uzoba uriko urakuraho Blockchain yose kandi uyigenzura uko biri kwose, rero nimba ufise umwanya, uzigame ivyo wakuraho, kandi ntucike nimba ushobora kuvyirinda.


Uhejeje kwemeza, Blockchain izotangura gukurwako. Bizofata imisi myinshi.


![image](assets/fr/15.webp)


Ushobora gufunga mudasobwa ugasubira kuvyikurako niwabishaka, ntaco bizokwonona.