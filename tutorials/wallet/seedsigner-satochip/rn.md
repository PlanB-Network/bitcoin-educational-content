---
name: Satochip x SeedSigner
description: Ni gute wokoresha Satochip n’Imbuto yawe?
---

![cover](assets/cover.webp)



*Turashimira [Igitabu c'Ivy'Imibano](https://www.youtube.com/@Igitabu c'Imibano/) ku fork yayo y'ubuhinga bwa SeedSigner bwo gufasha ikarita y'ubwenge, iyo tuzokoresha muri iyi nyigisho



---

Satochip ni igikoresho gifise ubuhinga bw’ikarita y’ubwenge wallet gifise ikintu c’umutekano cemewe na EAL6+, kimwe mu bipimo vy’umutekano vy’agaciro kanini. Ihinguwe kandi ikoreshwa n’ishirahamwe ry’Ababirigi ryitwa iryo zina nyene: Satochip.



Igiciro c’amayero 25, Satochip iratandukanye n’izindi kubera agaciro kayo k’amahera. Kubera ko ifise igice gikomeye, iratanga ubushobozi bwo kunanira ibitero vy’umubiri. Ikindi, kode yayo y'inkomoko ya applet ni inkomoko yuguruye yose, ifise uruhusha rwo gukoresha *AGPLv3*.



Ku rundi ruhande, uburyo bwayo buratuma habaho imipaka imwimwe y’ingene ikora. Intambamyi nyamukuru ya Satochip ni ukutagira igicapo gihuriweko: abakoresha rero bategerezwa gusinya amasezerano ata co bazi, bakizigira gusa ikigaragaza kuri mudasobwa yabo.



Kugira ngo ushobore gutsinda iyo ntege nke, uburyo bushimishije cane ni ukubukoresha hamwe n’umumenyeshamakuru w’imbuto. Muri iyo nzira, uguhanahana amakuru ntikugikorwa ata guca ku ruhande hagati ya mudasobwa na Satochip, ahubwo biciye ku guhanahana amakode ya QR hagati ya mudasobwa na SeedSigner. SeedSigner rero ikora nk’igicapo co kwizigira: kigaragaza amakuru azoshirwako umukono, mu gihe umukono ubwawo ukorwa na Satochip. Udakunze gukoresha SeedSigner isanzwe (canke mbere gukoresha hamwe na Seedkeeper), seed ntiyigera ishirwa muri SeedSigner. SeedSigner rero iba igicapo ca Satochip, igakuraho ingorane zijanye n’ugusinya ata wubona.



Turavye ingorane mu buryo bunyuranye, gukoresha SeedSigner na Satochip vyuzuza ikinogo kinini muri SeedSigner: ubushobozi bwo kubika no gukoresha seed muri secure element.



Mu vyiyumviro vyanje, iyi ntunganyo itanga ivyiza vyinshi ku bikoresho bisanzwe:




- Satochip igura nk’amayero 25, kandi kubera ko iyo applet ari open-source, urashobora kuyishiramwo wewe nyene ku smartcard idafise ikintu. Ushobora rero kwongerako igiciro c'ibice vya SeedSigner n'ivyo gusoma amakarata y'ubwenge: bivanye n'aho ugura iki gikoresho, igiciro cose gikwiye kuba hagati ya €70 na €100.
- Porogaramu zose ziri mu gutegura ni izo gufungura: porogarama ya SeedSigner n’iyi Satochip.
- Ushobora kwungukira ku kintu c’umutekano cemejwe.
- Ivyo bishobora gukorwa vyose mu buryo bw’ubuhinga bwa none, ata gukoresha ibikoresho vy’ubuhinga bwa none vyerekeye gukoreshwa na Bitcoin, bishobora gutanga uburyo bwo guhakana no kunanira ingeramizi zimwezimwe zo hanze (harimwo, bivanye n’igihugu, igitutu ca Leta). Ivyo navyo ni umuti ushimishije nimba ukuronka amasakoshi y’ibikoresho vy’ubudandaji bibujijwe canke bidashoboka mu karere kawe.




## 1. Ibikoresho bisabwa



Kugira ngo ukore ivyo, uzokenera ibi bikurikira:




- Ibikoresho bisanzwe bikenewe n'umuhinga mu vy'imbuto :
 - a Raspberry Pi Zero n'ibipimo vya GPIO,
 - 1.3" Igikoresho co gusangira umupfunda,
 - kamera ihuye,
 - ikarita ya microSD.



![Image](assets/fr/01.webp)





- Igikoresho co kwagura SeedSigner, kiboneka [mu iduka ryemewe rya Satochip](https://satochip.io/igicuruzwa/igikoresho co kwagura-seedsigner/), kigufasha gusoma no kwandika ku ikarita y’ubwenge ukoresheje SeedSigner yawe. Iyindi nzira ni ugukoresha [igikoresho co hanze co gusoma amakarata y’ubwenge](https://satochip.io/igicuruzwa/igikoresho co gusoma amakarata y’ubwenge/), gishobora gufatanywa n’umugozi ku nzira ya Micro-USB iri kuri Raspberry Pi. Ariko rero, jewe ubwanje sinarigeze ngerageza uwo muti;
- [Ikarata ya Satochip](Ikarata y’ubwenge], canke [ikarata y’ubwenge idafise ikintu] yo gushiramwo applet ya Satochip (igikoresho co kwagura kigurishwa na Satochip a blank smartsd alrea). Igikoresho co kwagura ca Satochip na co nyene gifasha uburyo bwa [SIM JavaCard] Ushobora rero guhitamwo iyi format nimba ubishaka.



![Image](assets/fr/02.webp)



Ku bindi bisobanuro ku bikoresho bisabwa kugira ngo umuntu akoranirize hamwe SeedSigner, urashobora kuraba igice ca 1 c’iyi yindi nyigisho:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Shiraho porogaramu



Kugira ngo ukoreshe SeedSigner yawe ukoresheje Satochip, ukeneye gushiramwo ubundi buhinga, butandukanye n’ubw’intango bwa SeedSigner, kugira ngo ushobore gufasha gusoma ikarita y’ubwenge. Ku bw'ivyo, [ndabahimiriza gukoresha fork kuva kuri "**Isubiramwo rya gatatu**"](https://github.com/Isubiramwo rya gatatu/umusinyi w'imbuto). Gukuraho [verisiyo nshasha y'ishusho](`.zip`) ihuye n'akarorero ka Raspberry Pi uriko urakoresha.



![Image](assets/fr/03.webp)



Niba utayifise, fungura porogarama ya [Balena Etcher] (https://etcher.balena.io/), hanyuma ugende gutya:




- Injira ikarata ya microSD muri mudasobwa yawe;
- Gutanguza Etcher ;
- Hitamwo dosiye `.zip` uherutse gukuraho;
- Hitamwo ikarita ya microSD nk’intumbero;
- Fyonda kuri `Umuco!`.



![Image](assets/fr/04.webp)



Rindira gushika iyo nzira irangiriye: microSD yawe ubu irateguwe gukoreshwa. Ubu urashobora gutera imbere mu gukoranya igikoresho cawe.



Kubindi bisobanuro ku bijanye no gushiramwo porogarama n’ukugenzura porogarama (intambwe ndagusavye cane gutera), raba inyigisho ikurikira:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Gukoranya igikoresho co gusoma ikarata y'ubwenge



Tangana n’ugushira kamera kuri Raspberry Pi Zero, uyishire neza mu gipimo ca kamera hanyuma uyifunge n’agace k’umwirabura. Hanyuma ushire Pi hasi mu gitereko, urabe neza ko ivyuho bihuye n’ibifunguruzo bihuye.



![Image](assets/fr/05.webp)



Hanyuma ushire igikoresho co gusoma ikarita y’ubwenge ku bipimo vya GPIO vya Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Nimushire igipfukisho c’ipulasitike hejuru y’igikoresho co gusoma ikarata y’ubwenge gushika gishizwe neza.



![Image](assets/fr/07.webp)



Hanyuma wongereko igicapo ku bipimo vya GPIO vy’ivyo bikoresho.



![Image](assets/fr/08.webp)



Ubwa nyuma, shiramwo ikarata ya microSD irimwo porogarama y’ivyuma mu gicapo co ku ruhande kiri kuri Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Ubu ushobora gufatanya SeedSigner yawe biciye ku nzira ya Micro-USB ya Raspberry Pi Zero, canke biciye ku nzira ya USB-C y'iyo nzira. Ivyo vyose birakora. Rindira amasegonda make kugira ngo utangure, hanyuma ubone igicapo c’akabazo kigaragara.



![Image](assets/fr/10.webp)



Kugira ngo umenye vyinshi ku bijanye n’ugutegura kwa mbere kwa SeedSigner yawe, ndagusavye ko uraba igice ca 4 c’inyigisho ikurikira:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Ushireko ikarita y'ubwenge ifise applet ya Satochip (ntibikenewe)



Niba usanzwe ufise Satochip, urashobora gusimbuka iyi ntambwe ukaja ku ntambwe ya 4. Muri iki gice, turaza kuraba ingene woshira applet ya Satochip ku smartcard idafise ikintu (uburyo bwa DIY). Ico gikoresho ni porogarama ntoyi gusa ikoreshwa kuri smartcard idushoboza gucungera ibikorwa vyihariye.



Kugira ngo utangure, fungura `Ibikoresho > Ibikoresho vy'ikarita y'ubwenge` kuri SeedSigner yawe.



![Image](assets/fr/11.webp)



Hanyuma uhitemwo `Ibikoresho vyo kwikorera > Shiraho Applet`.



![Image](assets/fr/12.webp)



Injira ikarata yawe y'ubwenge mu gisomyi ca SeedSigner, n'igice kiraba hasi, hanyuma uhitemwo igice ca `Satochip`.



![Image](assets/fr/13.webp)



Turagusavye wihangane mu gihe co gushiramwo: iyo nzira ishobora gutwara amasegonda mirongo.



![Image](assets/fr/14.webp)



Iyo applet imaze gushirwamwo neza, ushobora gukomeza ku ntambwe ya 4.



![Image](assets/fr/15.webp)




## 5. Guhingura no kuzigama seed.



### 5.1. Gutanga seed.



Ubu ko ufise ibikoresho vyawe vyose n’ibikoresho vyawe vyose bikora neza, urashobora gukomeza gukora igitabu cawe ca Bitcoin. Kugira ngo ubikore, shiramwo SeedSigner yawe, hanyuma generate seed yawe nk’uko bigenda ku SeedSigner isanzwe, mu gutera ivyatsi canke mu gufata ifoto:




- Genda kuri `Ibikoresho > Kamera / Ivyuma vy'amadayimoni`;
- Hanyuma ukurikize inzira y’uguhingura entropi hakurikijwe uburyo bwatowe;
- Ubwa nyuma, nushire backup ya seed ku bikoresho vy’umubiri maze usuzume neza iyo backup.



![Image](assets/fr/16.webp)



Niba wifuza kubona ido n’ido ry’iyi nzira, ukurikire igice ca 5 c’iyi nyigisho:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Kuzigama seed ku Mucungezi w'Imbuto



Iyo seed imaze gukorwa, ni co gihe conyene iba muri RAM ya SeedSigner. Ku bijanye nanje, nshaka kubibika kuri [Umucungezi w’imbuto](https://satochip.io/igicuruzwa/umucungezi w’imbuto/), ikindi gikoresho ca Satochip gigenewe kubika amabanga. Nzokoresha iki gikoresho nk’uburyo bwa nyuma, mu gihe Satochip yanje yoba yatakaje.



Ingamba zo gusubiza inyuma zatowe hano zivana n’ivyo ukunda, ariko ni ngombwa ko ufise n’imiburiburi kopi imwe y’ijambo ryawe ry’ukwibuka, haba ku bimenyeshamakuru vy’umubiri (impapuro canke ivyuma) canke, nk’uko biri aha, mu Mucungezi w’Imbuto. Ushobora kandi kugwiza umubare w’ibisubizo nk’uko bisabwa. Kubindi bisobanuro ku ngabire zo gucungera ibitabo, ndagusavye gusoma iyi nyigisho :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Kugira ngo ukore ububiko bwa seed yawe ku Mucungezi w'Imbuto, genda kuri `Backup Seed`.



![Image](assets/fr/17.webp)



Hanyuma winjize Umucungezi w'Imbuto yawe mu gisomwa c'ikarata y'ubwenge, hanyuma uhitemwo `Ku Mucungezi w'Imbuto`.



![Image](assets/fr/18.webp)



Injira PIN yawe kugira ngo uyifungure.



![Image](assets/fr/19.webp)



Hitamwo `Ikimenyetso` kugira ngo umenye neza amabanga yawe atandukanye abitswe kuri Seedkeeper. Ushobora, nk'akarorero, kuguma ufise icapa ca wallet canke ukagaragaza neza `Imbuto`. Ihitamwo rivana n’ivyo ukunda be n’ingorane.



![Image](assets/fr/20.webp)



Nimba ubuhinga bwawe bwo gusubiza inyuma bwishingikiriza gusa kuri iyi Seedkeeper, ndagusavye cane ko ukora ikigeragezo co gusubirana ataco kimaze ubu, hanyuma ugereranye ibimenyetso vy’intoke kugira ngo umenye ko gusubiza inyuma biriko birakora.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Icode ya PIN ya Seedkeeper ikwiye kuba ndende kandi idasanzwe uko bishoboka kwose, kugira ngo ntihagire uwugerageza gukoresha inguvu z’agahomerabunwa iyo ikarita ishobora gusenyuka. Ushobora kandi kubika kopi y’iyi kode ya PIN, ibitswe ahantu hatandukanye na Seedkeeper. Iyo udafise iyo PIN, ntuzoshobora gushika ku mnemonic ibitswe muri Seedkeeper, kandi amafaranga yawe azobura ubuziraherezo.



### 5.3. Bika seed kuri Satochip



None ko igitabu cawe cakozwe, kigabikwa kandi kigasuzumwa, tuzogirungika kuri Satochip. Kugira ngo ubikore, urabe neza ko seed ishizwe muri RAM ya SeedSigner. Hanyuma ugende kuri `Ibikoresho > Ibikoresho vy'Ikarata > Ibikorwa vya Satochip`.



![Image](assets/fr/21.webp)



Injira Satochip yawe mu gikoresho co gusoma ikarita y'ubwenge, hanyuma uhitemwo `Gutangura n'Imbuto`.



![Image](assets/fr/22.webp)



Ico gikoresho kigusaba kwinjiza kode ya PIN ya Satochip; nk’uko ikarita ari nshasha kandi itatanguje, nta PIN iracariho. Injira kode iyo ari yo yose kugira ngo usimbuke iyi ntambwe (si iyo kubuza).



![Image](assets/fr/23.webp)



SeedSigner ibona ko Satochip yawe itatanguje. Fyonda `Ndatahura` kugira ngo wemeze.



![Image](assets/fr/24.webp)



Ushobora rero gushinga kode ya PIN ya Satochip, kuva ku nyuguti 4 gushika ku nyuguti 16. Kugira ngo ukomeze umutekano wa wallet yawe, hitamwo kode ndende, idasanzwe: ni yo yonyene ikurinda gushika ku mubiri ku majambo yawe y’ukwibuka.



Ibuka kubika iyo PIN igihe nyene iremwe, haba mu gikoresho co gucungera ijambobanga ry’umutekano canke ku gikoresho c’umubiri, bivanye n’ingene ukoresha ubuhinga bwawe bwite. Mu gihe ca nyuma, urabe neza ko utazokwigera ubika umurongo urimwo PIN ahantu hamwe na Satochip yawe, ahandi ho uburinzi buzoba ubusa. Ni vyiza kugira kopi y'inyuma: **Udafise iyi PIN, ntuzoshobora gushika ku seed yawe, kandi ama bitcoins yawe azozimangana ubuziraherezo**.



![Image](assets/fr/25.webp)



Uwo SeedSigner aca akubaza seed yo kwinjiza muri Satochip. Hitamwo uwo urutoke rwiwe rujanye n’ivyo uherutse gukora.



![Image](assets/fr/26.webp)



seed yawe ubu irashirwa muri Satochip.



![Image](assets/fr/27.webp)



Ubu ushobora kuzimya SeedSigner yawe.



Niba wifuza gukoresha passphrase BIP39 kugira ngo wongere umutekano wa wallet yawe, raba igice ca 6 c’iyi nyigisho:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Injira wallet muri Sparrow



Ubu ko igitabo cawe kiriko kirakora, tuzozana amakuru yaco ya bose ("*keystore*") muri Sparrow Wallet canke mu yindi porogarama yo gucunga igitabo. Iyi porogaramu izokoreshwa mu guhingura, gukwiragiza no gukurikirana amafaranga yawe. Ariko rero, ntizoshobora kubishirako umukono, kuko Satochip yonyene (n’ibindi vyose bishobora gusubiza inyuma) ni vyo bifise imfunguruzo z’ibanga zikenewe muri iyo nzira.



### 6.1 Gutegura umukono w'imbuto na Satochip



Injiramwo ikarita ya microSD irimwo ubuhinga bwo gukoresha, hanyuma ufungure SeedSigner yawe. Kugeza ubu, ntaco ishobora gukora, kuko itaramenya seed yawe. Uzotangura winjiza Satochip mu gikoresho co gusoma ikarita y'ubwenge, kuko ari co gifata seed yawe.



Kuva ku rubuga rw'Imbere, genda kuri `Ibikoresho > Ibikoresho vya Smartcard > Ibikorwa vya Satochip`.



![Image](assets/fr/28.webp)



Hanyuma ukande kuri `Sohora Xpub`.



![Image](assets/fr/29.webp)



Hitamwo ubwoko bw'ibitabo. Mu gihe cacu, ni igitabu kimwe: hitamwo `Single Sig`.



![Image](assets/fr/30.webp)



Igikurikira ni uguhitamwo urugero rw’inyandiko. Hitamwo ivya nyuma: `SegWit y'imvukira`.



![Image](assets/fr/31.webp)



Ubwa nyuma, hitamwo `Umuhuzabikorwa`, ni ukuvuga porogarama yo gucunga ibitabo wipfuza gukoresha. Aha, tuzoba turiko turakoresha Sparrow Wallet.



![Image](assets/fr/32.webp)



Ubutumwa bwo kugabisha buraboneka: ivyo ni ibisanzwe rwose. Urufunguzo rwa bose rwagutse (`xpub`) rugufasha kubona amaderesi yose yava kuri seed yawe (ku konti ya mbere). Ariko rero, ntibitanga uburenganzira bwo kuronka amahera yawe: gutangazwa kwavyo vyotuma ubuzima bwite bwawe buhungabana, ariko ntibitanga umutekano w’amahera yawe y’ibiceri. Mu yandi majambo, biratuma wihweza uburinganire bwawe, mugabo ntubukoreshe.



Fyonda kuri `Ndatahura`.



![Image](assets/fr/33.webp)



Hanyuma winjize PIN ya Satochip yawe kugira ngo uyifungure. Iyi ni kode wasobanuye kandi ukabika mu ntambwe ya 5.



![Image](assets/fr/34.webp)



Ubwa nyuma, fyonda ku `Export Xpub` nimba unyuzwe n'amakuru yerekanwa.



![Image](assets/fr/35.webp)



SeedSigner rero itanga xpub yawe mu buryo bwa kode ya QR, irimwo amakuru yose ukeneye kugira ngo ushobore gucunga ibitabo vyawe muri Sparrow Wallet. Ushobora guhindura umuco w’ibarabara ukoresheje joystick kugira ngo gucapura kode ya QR vyorohe.



### 6.2 Kwinjiza ibitabo bishasha muri Sparrow Wallet



Raba neza ko porogarama ya Sparrow Wallet iri kuri mudasobwa yawe. Niba utazi uko woyikura, suzuma ko ari iyo ukuri maze uyishiremwo neza, raba inyigisho yacu yuzuye ku bijanye n'ico kibazo :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kuri mudasobwa yawe, fungura Sparrow Wallet, hanyuma mu rutonde rw'ibintu, ukande `Dosiye → Injira Wallet`.



![Image](assets/fr/36.webp)



Hanukira kuri `Umushingantahe w'imbuto`, hanyuma uhitemwo `Guca...`. Webcam yawe izokora: scanner kode ya QR ikora neza yerekanwa ku rubuga rwawe rwa SeedSigner.



![Image](assets/fr/37.webp)



Ha izina igitabo cawe, hanyuma ukande kuri `Rema Wallet`. Sparrow izoca igusaba gushinga ijambobanga ryo gufunga uburenganzira bwo gukoresha iyi wallet. Hitamwo ijambobanga rikomeye: rikingiye amakuru yawe muri Sparrow (imfunguruzo za bose, aderesi, ibimenyetso n’amateka y’ibikorwa). Ariko rero, iryo jambobanga ntirikenewe kugira ngo usubiremwo wallet muri kazoza: ijambo ryawe ry’ukwibuka gusa (kandi bishoboka ko passphrase yawe) rizoba.



Ndagusavye ubike iri jambobanga mu mucungerezi w’ijambobanga, kugira ngo nturitakaze.



![Image](assets/fr/38.webp)



Ububiko bwawe bw'urufunguzo bwashizwemwo neza.



![Image](assets/fr/39.webp)



Ubu rero suzuma ko `Ikimenyetso c'urutoke c'Umukuru` kigaragara muri Sparrow Wallet gihuye n'ico mbere cabonetse kuri SeedSigner yawe.



SeedSigner izoca igusaba gucapura aderesi y’ukwakira ivuye kuri Sparrow wallet yawe kugira ngo wemeze ko ivyo ushizemwo ari ukuri.



![Image](assets/fr/40.webp)



Satochip yawe (biciye kuri SeedSigner) na Sparrow Wallet ubu zihuye neza. Sparrow ikora nk’umurongo w’uburongozi wuzuye, mu gihe Satochip iguma ari yo yonyene ishobora gusinya amafaranga yawe. Ubu rero witeguriye kwakira no kohereza ama bitcoins mu buryo bufise ikirere cose.



![Image](assets/fr/41.webp)



## 7. Kwakira no kohereza amafaranga y’ibiceri .



Satochip yawe na Sparrow Wallet ubu vyatunganijwe kugira ngo bikore hamwe. Muri iki gice, turasigura intambwe ku yindi ingene wokwakira no kohereza ama bitcoins muri ubu buryo.



### 7.1 Kwakira ama bitcoins



#### 7.1.1 Gutanga aderesi y'ukwakira



Kuri mudasobwa yawe, fungura Sparrow Wallet maze ufungure `Satochip-SeedSigner` yawe wallet ukoresheje ijambobanga ryawe. Suzuma ko iyo porogarama ihuye na server (ikimenyetso kiri hasi iburyo). Hanyuma, mu ruhande, ukande kuri `Kwakira`.



![Image](assets/fr/42.webp)



Haca haboneka aderesi nshasha ya Bitcoin. Uzosanga :




- Aderesi mu buryo bw'inyandiko (gutangura na `bc1q...` nimba uriko urakoresha P2WPKH, nk'uko biri muri aka karorero) ;
- Igiharuro ca QR gifitaniye isano ;
- Umurima wa `Label`, ngirakamaro mu gukurikirana amafaranga yawe.



Ndagusavye cane ko wongerako ikimenyetso ku mpapuro z’amahera zose ziri muri wallet yawe. Ivyo bizokugirira akamaro mu kumenya aho UTXO imwe imwe yose ikomoka no gucungera neza ubuzima bwite bwawe. Kugira ngo umenye vyinshi ku bijanye n’iyi nyigisho ihambaye, raba amahugurwa yihariye kuri Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Kugira ngo wongereko ikimenyetso, shiramwo izina mu mwanya `Ikimenyetso`, hanyuma wemeze.



Nk'akarorero:



```txt
Label : Sale of the Raspberry Pi Zero
```



Ubu aderesi yawe ifatanye n’iki kimenyetso mu bice vyose vya Sparrow.



![Image](assets/fr/43.webp)



#### 7.1.2 Igenzura rya Address ku Mushingantahe w'Imbuto



Imbere yo kumenyesha uwuguha aderesi yawe, birahambaye ko usuzuma ko ari iya seed yawe. Iyi ntambwe ituma Satochip yawe ishobora gusinya amafaranga ajanye n’iyi aderesi. Birazibira kandi ibitero bishobora kubaho aho Sparrow yokwerekana aderesi y’ubuhendanyi. Zirikana ko Sparrow ikoresha ahantu hatagira umutekano (mudasobwa yawe), aho igitero cayo ari kinini cane kuruta ica Satochip yawe, iyo Satochip iri ukwayo rwose. Ni co gituma udakwiye kwigera wizigira ataco uzi amaderesi yerekanwa muri Sparrow imbere y’uko uyasuzuma ku bikoresho vyawe vya wallet.



Muri Sparrow, fyonda ku kode ya QR y’iyo aderesi kugira ngo uyikuze: izoca yerekanwa ku rubuga rwose.



![Image](assets/fr/44.webp)



Ku SeedSigner yawe, shiramwo Satochip mu gisomwa, hanyuma mu rutonde nyamukuru, uhitemwo `Scan`. Scan kode ya QR yerekanwa kuri mudasobwa yawe, hanyuma uhitemwo `Koresha ikarita ya Satochip`.



![Image](assets/fr/45.webp)



Hanyuma wemeze ubwoko bw'inyandiko ikoreshwa (muri iki gihe, `Native SegWit`), winjize kode ya PIN ya Satochip kugira ngo uyifungure, hanyuma wemeze amakuru ya `xpub`.



![Image](assets/fr/46.webp)



Niba aderesi ya scanner ihuye n'iyo yavuye kuri seed yawe, SeedSigner izokwerekana ubutumwa: `Address Yagenzuwe`.



![Image](assets/fr/47.webp)



Ushobora rero kumenya neza ko iyo aderesi ari iyo mu gitabu cawe.



#### 7.1.3 Kwakira amafaranga



Ubu ushobora gutanga iyo aderesi mu buryo bw’inyandiko canke ukoresheje kode yayo ya QR ku muntu canke igisata gikeneye kukurungikira satss. Igihe amafaranga amaze gutangazwa ku rubuga, azoboneka mu gice ca `Ibikorwa` ca Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Wohereze ama bitcoins



Kurungika amafaranga y’ibiceri n’imiterere ya Satochip-SeedSigner birimwo intambwe 3:




- Irema ry’ibikorwa muri Sparrow ;
- Gusinya kuri iri sezerano kuri Satochip, biciye ku SeedSigner ;
- Ubwa nyuma, iyo nzira iratangazwa ku rubuga rwa Sparrow.



Ivyo vyose bihanahana hagati y’ivyo bikoresho bibiri bibera gusa biciye ku makode ya QR.



#### 7.2.1 Gukora ubucuruzi muri Sparrow



Muri Sparrow Wallet, ushobora gukora igikorwa ukanda ku rubuga rwa `Send` ruri mu ruhande rw'ibubamfu. Ariko rero, ndakunda gukoresha urupapuro rwa `UTXOs`, rugufasha kwimenyereza *Coin Control*. Ubu buryo buratanga ubugenzuzi nyabwo ku ma UTXO akoreshwa, kugira ngo ugabanye amakuru ahishurirwa mu gihe c’ibikorwa vyawe.



Mu `UTXOs`, hitamwo ibiceri wipfuza gukoresha, hanyuma ukande `Kohereza Ivyatoranijwe`.



![Image](assets/fr/49.webp)



Hanyuma wuzuze ivyicaro vy'amafaranga:




- Mu `Pay to`, shiramwo aderesi y'uwuronka canke scanner kode yiwe ya QR ukoresheje ikimenyetso ca kamera ;
- Mu `Ikimenyetso`, wongeremwo ikimenyetso kugira ngo ukurikirane iyo nsiguro;
- Mu `Igiciro`, shiramwo igiciro kizorungikwa;
- Ubwa nyuma, hitamwo igipimo c’amahera uzotanga bivanye n’ingene urubuga ruri (ibiharuro biraboneka kuri [mempool.space](https://mempool.space/)).



Umaze kwuzuza ivyicaro vyose, subiramwo neza amakuru, hanyuma ukande kuri `Create Transaction >>`.



![Image](assets/fr/50.webp)



Suzuma amakuru y'ibikorwa ubwa nyuma kugira ngo ubone ko ari ukuri, hanyuma ukande kuri `Sozera ibikorwa kugira ngo usinye`.



![Image](assets/fr/51.webp)



Ubu iyo nzira y’ugucuruza irateguwe, ariko ntiyashirwako umukono. Kugira ngo ugaragaze [PSBT (*Partially Signed Bitcoin Transaction*)](kwerekana amajambo) nk’ikode ya QR, kanda kuri `Kwerekana QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Gusinya amasezerano na Satochip



Ushireko SeedSigner yawe maze winjize Satochip yawe nk’uko bisanzwe. Ku rubuga rw'intango, hitamwo `Scan`, hanyuma scanne kode ya QR yerekanwa kuri Sparrow.



![Image](assets/fr/53.webp)



Hitamwo `Koresha ikarita ya Satochip`.



![Image](assets/fr/54.webp)



Injira kode yawe ya PIN kugira ngo ufungure ikarita y’ubwenge.



![Image](assets/fr/55.webp)



SeedSigner ibona ko iyi ari PSBT maze igaragaza incamake y'ivyo yakoze:




   - Amafaranga yoherejwe,
   - Aderesi y'aho umuntu aja,
   - Ibiciro bijanye n’ugucuruza.



Fyonda kuri `Isubiramwo ry'Ibisobanuro` maze usuzume amakuru yose ataco akora ku rubuga rwa SeedSigner. Ibintu bihambaye cane vyo gusuzuma ni amahera yoherezwa, amaderesi y’aho umuntu aja n’amahera yo gukoresha.



![Image](assets/fr/56.webp)



Niba vyose biri ku rutonde, hitamwo `Kwemeza PSBT` kugira ngo ushire umukono ku giciro ukoresheje Satochip.



![Image](assets/fr/57.webp)



Iyo umukono umaze kurangira, SeedSigner itanga kode nshasha ya QR irimwo amafaranga yashizweko umukono, yiteguriye gupimwa na Sparrow.



#### 7.2.3 Gutangaza ivy'ugucuruza kuva kuri Sparrow



Ubu iyo nzira yashizweko umukono kandi yemejwe, igisigaye ni ukuyitangaza ku rubuga rwa Bitcoin kugira ngo umucukuzi w’amabuye y’agaciro ashobore kuyishira mu gice c’ibarabara. Muri Sparrow, fyonda ku `Scan QR`.



![Image](assets/fr/58.webp)



Yerekana kode ya QR yerekanwa kuri SeedSigner yawe (iyo irimwo amafaranga yashizweko umukono) kuri webcam. Sparrow izoca yerekana amakuru yose yerekeye ivy’ugucuruza. Suzuma ko amakuru yose ari ukuri, hanyuma ukande kuri "Broadcast Transaction" kugira ngo uyatangaze ku rubuga rwa Bitcoin.



![Image](assets/fr/59.webp)



Ivyo ugurisha ubu birarungikwa ku rubuga. Ushobora gukurikirana ivyemezo vyayo mu `Ibikorwa` tab ya Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Usubire kuronka wallet yawe



Nk’uko twabibonye mu bice vyabanje, bivanye n’ingene ukoresha umutekano, hari uburyo bwinshi bwo gusubiza inyuma ijambo ryawe ryo gusubirana uretse Satochip yawe :




- Gukoresha *SeedQR* ya kera n'Umushingantahe w'Imbuto ;
- Mu kwandika iryo jambo ry’ukwibuka ku gikoresho c’umubiri;
- Canke mu kubibika ku Mucungezi w'Imbuto, nk'uko vyasiguwe mu gice ca 5.2.



Uko biri kwose, hariho ibintu 2 nyamukuru ukeneye kwinjiramwo: gutakaza Satochip canke gutakaza SeedSigner. Reka turabe ingene twovyifatamwo muri ivyo bihe vyose.



### 8.1. Kugarura wallet yawe ukoresheje Satochip



Niba ugifise Satochip yawe ariko SeedSigner yawe ivunitse canke ikaba yazimiye, ibintu birasanzwe vyoroshe gucungera, kuko wallet yawe ikiri muri Satochip.



Ihitamwo ryiza ni ugutanga impanuro ku bice bikenewe no gusubira kwubaka SeedSigner nshasha kuva mu ntango. Kubera ko iki ari igikoresho "kitagira igihugu", ntaco bimaze nimba ukoresha SeedSigner imwe canke iyindi: igihe cose uzoba ushobora kwinjiza Satochip yawe, vyose bizogenda neza.



Niba udashaka gusubira kwubaka, urashobora kandi gukoresha Satochip yawe mu buryo bwa kera, ni ukuvuga uhereye kuri mudasobwa yawe, utaciye muri SeedSigner. Ubu buryo burakora neza cane, ariko buragabanya cane umutekano wa Bitcoin wallet yawe: uratakaza "*air-gapped*" isolation kandi ubu utegerezwa gusinya ataco ubona, kuko SeedSigner yakoze nk'igicapo cizigirwa. Ariko rero, ivyo bishobora kuba umuti w’igihe gito mu gihe c’ivyihutirwa, canke iyo udashobora gusubira kwubaka SeedSigner.



Kugira ngo ubikore, uzokenera ikarita y’ubwenge ya USB canke igikoresho co gusoma NFC. Ugurure wallet wipfuza gusubiza muri Sparrow, hanyuma ugende kuri `Ivyagezwe` hanyuma ukande `Subiriza`.



![Image](assets/fr/61.webp)



Injira Satochip yawe mu gisomwa c'amakarata y'ubwenge gifatanye na mudasobwa, hanyuma ukande kuri `Import` iruhande ya `Satochip`.



![Image](assets/fr/62.webp)



Ubwa nyuma, shiramwo PIN y’ikarata yawe y’ubwenge kugira ngo uyifungure. Uzoheza ushobore gushika ku wallet yawe, ukore amafaranga maze uyasinye ukoresheje Satochip ihuye.



### 8.2. Kugarura ibitabo vyawe ukoresheje SeedSigner



Ikindi, gikomeye cane ni iyo utakaje uburenganzira bwo gukoresha Satochip yawe irimwo seed: yaba yamenetse, yazimiye, yibwe, canke wibagiwe PIN code yayo. Niba Satochip yawe yibwe canke yazimiye, turagusavye cane ko, iyo umaze kuronka amahera yawe, ubwo nyene urungika amafaranga yawe y’ibiceri (bitcoins) kuri wallet nshasha, ivutse n’iyindi seed. Ivyo bituma uwushobora kukutera adashobora kwigera aronka uburenganzira bwo gushika kuri satss yawe.



Kugira ngo wongere ubone uburenganzira bwo gukoresha ibitabo vyawe no kwimurira amahera yawe, ushobora gusa gushiramwo seed yawe muri SeedSigner. Bivanye n'ivyo wakoresheje, urafise uburyo bwinshi:





- Injira ijambo ryawe ry'ukwibuka n'amaboko mu `Imbuto > Injira amajambo 12 seed`.



![Image](assets/fr/63.webp)





- Scan *SeedQR* yawe ukanda kuri buto ya `Scan` iri kuri paji y'intango.



![Image](assets/fr/64.webp)





- Canke ushire seed yawe uvuye ku Mucungezi w'Imbuto, biciye ku `Imbuto > Kuva ku Mucungezi w'Imbuto` (ubu ni uburyo ndiko ndakoresha muri iyi nyigisho). Uzokenera gusa kwinjiza PIN y'Umucungezi w'Imbuto maze uhitemwo ibanga rizokoreshwa nka seed kuri SeedSigner.



![Image](assets/fr/65.webp)



Igihe seed imaze gushirwa muri SeedSigner, uburyo bwose ukoresha, uzoshobora gusinya igikorwa kimwe canke vyinshi kugira ngo wimure amafaranga yawe ku wallet nshasha, idashobora gusenyuka. Kugira umenye ingene wobikora, raba igice ca 7.2 c’inyigisho ikurikira:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Ubu urazi gukoresha Satochip kugira ngo ucungere neza igitabu cawe ca Bitcoin ufatanije na SeedSigner.



Niba iyi setup yakwemeje, ntukekeranye gushigikira imigambi ituma bishoboka:




- Mu kugura ibikoresho vyawe ataco ukoresheje [ku rubuga rwa Satochip](https://satochip.io/shop/);
- Mu gutanga [intererano ku mugambi w’Umushingantahe w’Imbuto](https://umushingantahe w’imbuto.com/intererano/);
- Mu kwiyandikisha kuri [umurongo wa YouTube wa Crypto Guide](https://www.youtube.com/@CryptoGuide/), urongowe n’umuntu abungabunga ububiko bwa GitHub bufise porogarama yahinduwe twakoresheje muri iyi nyigisho.