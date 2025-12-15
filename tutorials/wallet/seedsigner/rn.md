---
name: SeedSigner
description: DIY, nta gihugu, bishoboka kandi vyuzuye umuyaga-gapped wallet hardware
---

![cover](assets/cover.webp)



SeedSigner ni igikoresho gifunguye wallet Bitcoin umuntu wese ashobora kwiyubakira akoresheje ibikoresho vy’ubuhinga bwa none bitazimvye bikoreshwa muri rusangi. Udakunze ibikoresho vy’ubudandaji nka Ledger, Coldcard canke Trezor, iki si igikoresho giteguwe gukoreshwa gikozwe n’ishirahamwe: ni umugambi w’abanyagihugu utuma umuntu wese yihingurira igikoresho ciwe, akagenzura intambwe yose.



SeedSigner yakozwe kugira ngo ibe 100% ***ikoreshwa n’umuyaga***: ntiyigera ifatanya na Internet, nta Wi-Fi canke Bluetooth igira (mu gihe ca Raspberry Pi Zero v1.3) kandi ntiyigera ihurizwa na mudasobwa kugira ngo ihindure amakuru. Ivyo guhanahana amakuru bica gusa ku buryo bwo guhanahana amakode ya QR. Mu majambo nyayo, porogarama yawe yo gucunga ibiharuro vyawe (nk’iyitwa Sparrow Wallet) yerekana amafaranga azoshirwako umukono mu buryo bw’amakode ya QR; urabicapura ukoresheje kamera ya SeedSigner, hanyuma ico gikoresho kigashira umukono ku gikorwa gikoresheje imfunguruzo zawe z’ibanga zibitswe mu gihe gito muri RAM yaco. Ubwa nyuma, iratanga amakode ya QR arimwo iyo nzira yashizweko umukono, iyo uyicapura ukoresheje porogarama yawe kugira ngo uyirungike ku rubuga rwa Bitcoin.



![Image](assets/fr/001.webp)



SeedSigner na we nyene ni ***uwutagira igihugu***. Mu yandi majambo, ntizigama seed yawe canke imfunguruzo zawe z’ibanga ubuziraherezo, bitandukanye n’izindi nkweto z’ibikoresho. Igihe cose usubiye gufungura, ubwonko bwayo buraba ubusa rwose, kiretse iyo utunganije igikoresho kugira ngo kibike ivyo washizeho ku ikarita ya microSD. Ubwirizwa rero gusubira kwinjiza seed yawe igihe cose uyikoresheje, uburyo bwiza cane ni ukuyibika mu buryo bwa kode ya QR, kugira ngo ishobore gucapurwa igihe utanguye gukoresha kamera ya SeedSigner. Ubwo buryo bwo gukora buragabanya cane igitero: naho umusuma yokwiba igikoresho cawe, nta makuru azoronka kuri co, kuko cama ari ubusa ku buryo busanzwe.



Iyindi nzira yo kubika seed yawe no kuyikoresha na SeedSigner ni ugukoresha ikarita y’ubwenge *SeedKeeper* ifatanijwe n’igisomyi gihuye. Ivyo biguha *Secure Element* ikomeye cane yo kubika seed yawe, mu gihe ukoresha igicapo ca SeedSigner kugira ngo usinye amafaranga. Ariko iyo configuration yihariye ni ikiganiro c’iyindi nyigisho yihariye. Aha, tuzokwibanda ku gukoresha kw'ishimikiro kwa SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Umugambi wa SeedSigner ufise ikibanza gihambaye mu bidukikije vya Bitcoin, kuko uha umuntu wese, aho hose kw’isi, ubushobozi bwo kwungukira ku mutekano uteye imbere kugira ngo bakingire amafaranga yabo ya bitcoins. Inyungu yayo nyamukuru iri mu gushikira abantu bose: ibikoresho bisabwa bishobora kugurwa ku madolari atarenga 50. Ikindi, bituma abantu baba mu bihugu bibujijwe kwiyubakira ibikoresho vyabo vya wallet bakoresheje ibihimba vya mudasobwa bisanzwe, ivyo bikaba vyoroshe kuronka kandi bidashobora guterwa n’amategeko.



Ariko no hanze y’ivyo bihe vyihariye, SeedSigner ishobora kuba uburyo bushimishije kuri wewe: ni open-source, ikora ata gihugu kandi ifise airgapped, kandi igabanya ibitero bihuye n’uruhererekane rw’ibikoresho vyawe vya wallet.



## 1. Ibikoresho bisabwa



Kugira ngo wubake SeedSigner yawe, uzokenera ibi bikurikira:





- Rasiberi Pi Zero
    - Verisiyo 1.3 ni yo ikenewe, kuko nta Wi-Fi canke Bluetooth ifise, bikaba bituma umuntu yitandukanya n’abandi.
 - Verisiyo za W na v2 na zo nyene zirahuye, ariko zifise igice ca Wi-Fi/Bluetooth. Ni vyiza rero ko uwuzimya ku mubiri mu gukuraho igice c’iradiyo kiri ku karata. Ivyo bikorwa birasanzwe, ariko bisaba ko umuntu akora neza (ibipimo vyiza bihagije ku Zero W, mu gihe ikaramu ishushe ikenewe ku v2 kugira ngo ikureho igipande c’icuma kinyegeza iyo module). Sinzoja mu ndondoro muri iyi nyigisho, ariko uzosanga amabwirizwa yose muri iyi nyandiko: *[Guhagarika WiFi/Bluetooth n'ibikoresho](https://github.com/rpi_guhagarika_wifi_na_bt_n'ibikoresho)*.
 - Iyumvire: hariho ibigereranyo vya Raspberry Pi Zero bigurishwa ata n’ibipimo vya GPIO vyateguwe mbere. Ushobora kugura verisiyo ifise amapin yunze ubumwe ataco akora (umuti woroshe), canke ukagura amapin atandukanye maze ukayasoda wewe nyene (umuti ugoye cane).
 - Ntimwibagire gushiramwo umuyagankuba wa micro-USB.



![Image](assets/fr/002.webp)





- Gusangira umupfunda 1.3" igicapo (240×240 px)** (mu gifaransa)
    - Ni ngombwa guhitamwo iki kigereranyo: hariho izindi nkuru zisa n'izo, ariko zifise ubushobozi butandukanye. Ata nsobanuro ya 240×240 px, ikigaragaza ntikizokoreshwa.
    - Ico gicapo gifise amabuto atatu n’igikoresho gitoyi co gukoresha.



![Image](assets/fr/003.webp)





- Raspberry Pi Zero**-ihuye n'ikamera
    - Ihitamwo rya mbere: kamera isanzwe ifise igitanda cagutse c’inzahabu (suzuma ko ihuye n’inzu yawe).
    - Ihitamwo rya 2: kamera "*Zero*" ikomeye cane, yakozwe cane cane kuri Pi Zero.



![Image](assets/fr/004.webp)





- Ikarata MicroSD**
    - Ubushobozi bugenewe: hagati ya 4 na 32 GB.





- Inzu (nivyo ariko birakenewe)** (nivyo ariko birakenewe)** (nivyo ariko birakenewe)** (nivyo ariko birakenewe)**)
    - Ikingira igikoresho kandi kigatuma vyoroha gukoresha.
    - Icogereranyo gikundwa cane ni "*Orange Pill Case*", iyo [amadosiye ya STL y'inkomoko yuguruye aboneka mu gucapura 3D](https://github.com/Imbuto/igiti/igiti/igiti/igiti).
    - Amasandugu araboneka kandi ku [bagurisha bigenga bafitaniye isano n’uwo mugambi](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Ushobora kugura ivyo bihimba ukwavyo canke, kugira ngo bibe vyoroshe, ugahitamwo amapaki yiteguye arimwo ibikoresho vyose bikenewe. Ku bwanje, nasavye ipaki yanje [kuri uru rubuga rw’igifaransa](https://bitcoinbazar.fr/), ariko uzosanga kandi urutonde rw’abagurisha akarere kose k’isi kuri [paji y’ibikoresho vy’umugambi wa SeedSigner](https://seedsigner.com/hardware/). Niba ushaka kugura ivyo bihimba umwumwe wese, biraboneka ku mbuga zikomeye z’ubudandaji canke mu maduka yihariye.



## 2. Gutegura porogaramu



Uhejeje gukoranya ibikoresho vyawe, ukeneye gutegura ikarita ya microSD mu kuyishiramwo ubuhinga bwa SeedSigner. Kugira ngo ubikore, genda kuri mudasobwa yawe ya misi yose, hanyuma ushiremwo microSD yawe yagenewe SeedSigner.



### 2.1. Gukurura



Genda kuri [ububiko buzwi bw'umugambi bwa GitHub](https://github.com/Umushingantahe w'imbuto/umunyamuryango w'imbuto/ibisohoka). Ku verisiyo nshasha ya porogaramu, fungura :




- Ishusho `.img` ihuye n'akarorero kawe ka Pi.
- Dosiye `.sha256.txt`.
- Dosiye `.sha256.inyandiko.sig`.



![Image](assets/fr/006.webp)



Imbere yo gutangura gushiramwo, reka tugenzure porogarama.



### 2.2 Gusuzuma munsi ya Linux na macOS



Tangira mu kwinjiza urufunguzo rwa bose rw'umugambi wa SeedSigner uhereye kuri Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminal ikwiye kukubwira ko urufunguzo rwashizwemwo canke rwavuguruwe. Inyuma, ukoreshe itegeko ryo kugenzura kuri dosiye y'umukono (wibuke guhindura itegeko ukurikije verisiyo yawe, hano `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Niba vyose ari ukuri, igisohoka gikwiye gusoma `Umukono mwiza`. Ivyo bisigura ko dosiye `.sha256.txt` yashizweko umukono n'urufunguzo uherutse kwinjiza, kandi ko umukono ufise akamaro. Irengagize ubutumwa bw'imburi `IMBURIZO: Uru rufunguzo ntirwemejwe n'umukono wizewe`: ivyo ni ibisanzwe, kuko ubu ari wewe ushobora kugenzura ko urufunguzo rwakoreshejwe ari urw'umugambi wa SeedSigner.



Kugira ngo ubikore, gereranya inyuguti 16 za nyuma z’urutoke rwerekanwa n’izo ziboneka kuri [Keybase.io/SeedSigner](https://keybase.io/seedsigner]), kuri [Twitter yabo yemewe](https. [Imbuto.com](https://imbuto.com/urufunguzo.txt). Nimba ivyo bimenyetso bihuye neza na neza, urashobora kwemera udakeka ko urufunguruzo ari urw’umugambi vy’ukuri. Niba ugira amakenga, uhagarare ubwo nyene usabe umuryango w’abamenyeshamakuru b’imbuto (Telegram, X, GitHub...) ngo bagufashe.



Iyo urufunguzo rwemejwe, ushobora kugenzura ko ishusho yakuweko itahinduwe (wibuke guhindura itegeko rishingiye kuri verisiyo yawe, hano `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Munsi ya Linux, iri tegeko ryubatswemwo.
- Imburi: verisiyo za macOS imbere ya `Big Sur (11)` ntizimenya uburyo bwa `--kwirengagiza-kubura`. Muri ivyo, uyikureho kandi wirengagize imburi zijanye n’amadosiye abuze.



Igisubizo citezwe ni `OK` iruhande ya dosiye `.img`. Ivyo vyemeza ko ishusho yashizweko isa n’iyo umugambi wasohowe kandi ko itahinduwe.



### 2.3 Igenzura rya Windows



Kuri Windows, uburyo bwo kubikora burasa ariko amabwirizwa aratandukanye. Tangana n’ugushiramwo [Gpg4win]() hanyuma ufungure porogarama ya *Kleopatra*. Injira urufunguzo rwa bose rw'umugambi wa SeedSigner kuva ku rubuga rwa URL :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Inyuma, fungura PowerShell muri dosiye aho amadosiye yawe yakuweho ari (`Shift` + kanda iburyo > `Fungura PowerShell hano`). Gukoresha itegeko rikurikira kugira ngo usuzume umukono w'ikimenyetso (wibuke guhindura itegeko ukurikije verisiyo yawe, hano `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Niba vyose ari ukuri, igisohoka gikwiye gusoma `Umukono mwiza`. Ivyo bisigura ko dosiye `.sha256.txt` yashizweko umukono n'urufunguzo uherutse kwinjiza, kandi ko umukono ufise akamaro. Nimwirengagize ubutumwa bw'imburi `IMBURIZO: Uru rufunguzo ntirwemejwe n'umukono wizewe`: ivyo ni ibisanzwe, kuko ubu ari wewe ushobora kugenzura ko urufunguzo rwakoreshejwe ari urw'umugambi wa SeedSigner.



Kugira ngo ubikore, gereranya inyuguti 16 za nyuma z’urutoke rwerekanwa n’izo ziboneka kuri [Keybase.io/SeedSigner](https://keybase.io/seedsigner]), kuri [Twitter yabo yemewe](https. [Imbuto.com](https://imbuto.com/urufunguzo.txt). Nimba ivyo bimenyetso bihuye neza na neza, urashobora kwemera udakeka ko urufunguruzo ari urw’umugambi vy’ukuri. Niba ugira amakenga, uhagarare ubwo nyene usabe umuryango w’abamenyeshamakuru b’imbuto (Telegram, X, GitHub...) ngo bagufashe.



Urufunguzo rumaze kwemezwa, ukeneye kugenzura ko dosiye y’ishusho itarononekaye. Kugira ngo ubikore, koresha itegeko rikurikira muri PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Akarorero ka Raspberry Pi Zero 2 (wibuke guhindura itegeko ukurikije verisiyo yawe, hano `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell rero ibara SHA256 hash ya dosiye yawe y'ishusho. Gereranya iyi hash n'agaciro kahuye muri `imbuto.0.8.6.sha256.txt`.




- Iyo izo nkuru zibiri zisa cane, isuzuma riraroranirwa kandi urashobora kubandanya.
- Iyo zitandukanye, dosiye irasenyuka canke irasenyuka. Ntuyikoreshe, kandi wongere utangure kuyikuramwo.



![Image](assets/fr/013.webp)



Igenzura ryiza ryemeza ko dosiye yawe `.img` ari iyo ukuri (yashizweko umukono na SeedSigner) kandi ko itahinduwe (itahinduwe). Ushobora rero gutera intambwe ikurikira ata nkomanzi.



### 2.4. Gukayangana ishusho



Niba utarayigira, fungura porogarama ya [Balena Etcher] (https://etcher.balena.io/), hanyuma :




- Injira ikarata ya microSD muri mudasobwa yawe.
- Gutanguza Etcher.
- Hitamwo dosiye `.img` yavanwe kandi yagenzuwe.
- Hitamwo ikarita ya microSD nk’intumbero.
- Fyonda kuri `Umuco!`.



![Image](assets/fr/014.webp)



Rindira gushika iyo nzira irangiye: microSD yawe irateguwe gukoreshwa. None ni igihe co gukorana!



## 3. Iteraniro ry'Umushingantahe w'Imbuto



Ikarata yawe ya microSD imaze gutegurwa no gucapura n’ubuhinga bwa SeedSigner, urashobora gukomeza gukoranya ivya nyuma. Fata umwanya wawe, kuko ibice bimwe bimwe bishobora gusenyuka (cane cane igitambaro co ku meza, kamera n’ibipimo vya GPIO).



### 3.1 Gutegura inzu



Mbere na mbere, fungura urubanza rwawe. Suzuma ko isukuye kandi ko ata n’imwe isigaye y’ipulasitike yo gucapura 3D iri mu nzira y’ibifatanya imbere. Raba :




- Aho kamera iri (umwobo mutoyi w’uruziga imbere).
- Igifunguruzo c’ibarabara.
- Ivyo bice vy’ibikoresho vya Raspberry Pi Zero vy’ibikoresho vya USB n’ivy’ibikoresho vya microSD.



### 3.2 Gushiramwo kamera



Tora aho urudodo rwo gufata amasanamu rufatanya kuri Raspberry Pi Zero: ni umurongo w’umwirabura mutoyi uri ku ruhande rw’urubaho, ushobora guterurwa gatoyi kugira ngo ufunguke. Uyiduze witonze, utayihatira: ikwiye gusa guhengamira milimetero nkeyi.



![Image](assets/fr/015.webp)



Niwinjize igipfukisho ca kamera. Igice c’inzobe/umuringa gikwiye kuraba hasi. Raba neza ko yicaye neza mu gifatanya, ataco ihinduye.



![Image](assets/fr/016.webp)



Funga umurongo w’umwirabura kugira ngo ufunge igitambaro co ku meza (uzokwiyumva ukanda gatoyi). Suzuma neza ko iguma mu kibanza cayo kandi ko itagenda.



![Image](assets/fr/017.webp)



Hanyuma ushire iyo module ya kamera mu mwobo ukwiye wo mu nzu. Bivanye n’ico gikoresho, yoshobora guca mu nzira ata guca ku ruhande canke igasaba agace gatoyi k’ugufatanya kugira ngo igumye mu kibanza cayo. Ico gikoresho gitegerezwa kuba gitunganye neza, kiraba hanze.



### 3.3 Gushiramwo Raspberry Pi Zero



Niba ukoresha igisandugu, shiramwo urubaho rwa Raspberry Pi Zero imbere. Niwitonde, ushire hamwe ivyuho n’ibifunguruzo vyatanzwe.



Hanyuma ushire ikigaragaza Waveshare hejuru y’ikigaragaza Pi Zero. Ivyuma vya GPIO vya Pi bikwiye guhura neza n’umufatanyabikorwa w’igitsina gore w’ikigaragaza. Buhorobuhoro, ukanda kuri iyo nkuru ku bipimo, ushireko mbere n’umukazo ku ruhande rumwe rumwe kugira ngo ntuzipfuke.



![Image](assets/fr/018.webp)



Niba ufise ikibazo, heza ikoraniro mu kwongerako igipande c’imbere n’igikoresho co gukoresha.



Ubwa nyuma, shiramwo ikarata microSD irimwo porogarama y’umuco mu gice ca Raspberry Pi Zero gishizwe ku ruhande. Raba neza ko ikanda mu kibanza cayo.



### 3.4 Gutangura kwa mbere



Huza umugozi w’amashanyarazi wa micro-USB ku nzira yihariye. Rindira nk'umunota umwe. Ikimenyetso ca SeedSigner gikwiye kuboneka, gikurikirwa n’igicapo c’inzu.



![Image](assets/fr/019.webp)



Kugira ngo utangure, suzuma ko ibice bitandukanye bikora neza mu kuja kuri `Ivyagezwe > I/O test` menu.



![Image](assets/fr/020.webp)



Gerageza amabuto yose maze urabe ko yishura neza. Hanyuma ukande kuri buto ya `KEY1` kugira ngo umenye ko kamera ikora nk’uko vyitezwe. Ivyo bizofata ifoto.



![Image](assets/fr/021.webp)



### 3.5 Guhindura kamera



Bivanye n'ingene washizeho SeedSigner yawe, kamera ishobora kwerekana ishusho ihindutse. Kugira ngo ubikosore, genda kuri `Imiterere > Ivyiza > Guhindura kamera` hanyuma uhitemwo guhindura 180° nimba bikenewe.



![Image](assets/fr/022.webp)



Niba warahinduye aho kamera ihagaze canke wipfuza guhindura ibindi bikoresho (nk’ururimi rw’ibarabara) mu nyuma, uzokenera gutuma ibintu bigumaho kuri microSD. Ahandi ho, amasetingi yawe azosubira ku vyo yahora igihe cose usubiye gufungura, kuko Raspberry Pi Zero nta memory igumaho.



Kugira ngo ubikore, fungura `Ivyagezwe > Ivyagezwe bihoraho`, hanyuma uhitemwo `Ibishobojwe`.



![Image](assets/fr/023.webp)



Niba vyose bikora, SeedSigner yawe ubu irateguwe gukoreshwa!



## 4. Amagenamiterere y'Umushingantahe w'Imbuto



Imbere yo kurema Bitcoin wallet yawe, reka dushireho SeedSigner. Nk’uko ikora kuri Raspberry Pi Zero ata memory igumaho, amasetingi yayo ntabikwa ubwayo kiretse uyabitse ku ikarita ya microSD. Rero urabe neza ko warashoboje iyo nzira, ahandi ho izo settings zizobura iyo usubiye gufungura (raba intambwe ya 3.5).



### 4.1 Ububiko bw'imirongo



Tangira SeedSigner yawe maze urindire ko igicapo c'inzu kigaragara. Ukoresheje joystick, genda kuri `Settings`, hanyuma wemeze ukanda buto iri hagati. Ubu rero winjira muri menyu y’imiterere nyamukuru.



![Image](assets/fr/024.webp)



### 4.2 Guhitamwo porogaramu yo gucunga ibikorwa



Hanyuma winjire muri `Porogaramu y'umuhuzabikorwa`.



![Image](assets/fr/025.webp)



`Umuhuzabikorwa` yerekeza kuri porogarama yo gucunga ibikorwa SeedSigner yawe azovugana na yo biciye ku makode ya QR. Iyi porogarama ishobora gushirwa kuri mudasobwa yawe canke kuri telefone yawe ngendanwa. Bizogufasha gucunga ama bitcoins yawe, ariko utazokwigera ubona imfunguruzo zawe z’ibanga. SeedSigner iguma ari co gikoresho conyene gishobora gusinya amafaranga yawe.



Ivyo bikoresho bifasha porogarama nyinshi: Sparrow, Spectre, BlueWallet, Nunchuk na Keeper. Ku bijanye nanje, nkoresha **Sparrow Wallet**, iyo nsaba cane cane kubera ko yoroshe kandi ikora neza.



Niba utazi uko woyishiramwo, ushobora gukurikira iyi nyigisho:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Hitamwo gusa porogarama uhisemwo mu vyo ubona.



![Image](assets/fr/026.webp)



### 4.3 Ibice n'umubare vyerekanywe



Mu `Iyerekanwa ry'Igiciro`, ushobora guhitamwo igice amafaranga yerekanwamwo:




- 'BTC`
- mBTC` (imili-ibice, canke 0.001 BTC)
- gW-15 (amasatoshi, canke 1/100.000.000 BTC)



Igikoresho ca **sats** ni co muri rusangi gikoreshwa cane ku mahera make.



![Image](assets/fr/027.webp)



### 4.4 Amagenamiterere ateye imbere



Ubu rero genda kuri `Ivyateye imbere`. Aha uzosanga uburyo bwinshi ngirakamaro:




- gW-17 urubuga`: guhindurwa gusa iyo wipfuza gukoresha SeedSigner kuri Testnet.
- qR code density`: ihindura urugero rw’amakuru ari muri kode ya QR imwe imwe. Ushobora gusiga agaciro ka mbere, kiretse ubonye ko bigoye gusoma igihe uriko urakora scanner.
- `Xpub export`: ishoboza canke ibuza kwohereza hanze urufunguzo rwawe rwa bose rwagutse (`xpub`, `ypub`, `zpub`) kuri porogaramu yo gucunga ibitabo biciye kuri kode ya QR (igikorwa tuzokoresha mu nyuma, rero reka gishobozwe ubu).
- `Ubwoko bw'inyandiko`: busobanura ubwoko bw'inyandiko bwemewe gufunga amafaranga yawe. Ntukeneye guhindura iyi parametere, kuko ubwoko bw'inyandiko buzoshirwa kuri Sparrow. Aha, inyandiko gusa SeedSigner yemerewe gukoresha ni zo zireba.



### 4.5 Guhitamwo ururimi



Ubwa nyuma, mu `Ururimi`, ushobora guhindura ururimi rw'ibarabara kugira ngo rujane n'ivyo ukunda.



![Image](assets/fr/028.webp)



## 5. Guhingura no kubika seed



seed (canke ijambo ry’ukwibuka) ni ryo shingiro ry’ibitabu vyawe vya Bitcoin. Ikoreshwa mu gukura imfunguruzo zawe n’amaderesi yawe bwite, kandi itanga uburyo bwo kuronka amahera yawe. SeedSigner itanga uburyo bwinshi bwo kuyihingura, ivyo tuzobiraba muri iki gice.



Imbere y’uko dutangura, ivyo twibutsa bikeyi bihambaye:




- Iri jambo ritanga uburenganzira bwo gukoresha amafaranga yawe yose, ataco abujijwe.** Umuntu wese afise iri jambo arashobora kwiba amahera yawe, mbere atashobora gushika ku SeedSigner yawe ;
- Kenshi, amajambo y’amajambo 12 arakoreshwa kugira ngo umuntu asubizeho wallet iyo atakaje canke yibwe ibikoresho vya wallet. Ariko kuko SeedSigner ari igikoresho *kitagira igihugu*, ntikigera candika seed yawe. Rero ama backups yawe y’umubiri si ama backup gusa, ariko **uburyo bwonyene bwo gukoresha wallet yawe**. Iyo utakaje izo backups, bitcoins zawe zizobura ubuziraherezo. Rero mubishigikire mwitonze, ku binyamakuru vyinshi no mu bibanza bitekanye;
- Niba uriko uratangura, ndaguhanura cane gusoma iyi nyigisho kugira ngo utahure neza ingorane ziri mu gucunga amajambo y'ukwibuka :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Gushikira igikoresho co kurema seed



Kuva ku rubuga rw'intango rwa SeedSigner, genda kuri `Ibikoresho`.



![Image](assets/fr/029.webp)



Ubu uzoba generate seed yawe. seed ni umubare munini gusa w’imburakimazi. Uko igenda ivugwa mu buryo butari bwo, ni ko igenda itekanye. SeedSigner itanga uburyo bubiri bwo kubikora:




- camera": seed ikomoka ku rusaku rw'amaso rw'ifoto. Ufata ishusho y'ibidukikije bitari vyo (ikintu, ahantu, mu maso, n'ibindi) bifise amahinduka ya pixels akoreshwa ku entropy ya generate. Ni uburyo bwihuta, ariko ntibushobora gusubirwamwo.
- dice Rolls": utera dice kugira ngo ureme entropy ikenewe. Bifata umwanya munini, ariko birashobora gusubirwamwo kandi rero birashobora kugenzurwa. Niwahitamwo ubu buryo, kurikiza impanuro ziri muri iyi nyigisho (ntibikenewe kubara checksum hano, SeedSigner iravyitaho):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Gukora seed n'ifoto



Niwahitamwo uburyo bwo gufata amafoto, ukande kuri `New seed` (ifise ikimenyetso ca kamera), ufate ifoto maze uyishire mu ngiro. Hanyuma uhitemwo uburebure bw’interuro yawe (amajambo 12 canke 24), izoboneka ku rubuga kugira ngo uzibike. Intambwe zikurikira zisa n'izo mu gice ca 5.3.



### 5.3 Gukora seed n'ibice



Muri iyi nyigisho, dukoresha uburyo bwa **Dice Rolls**. Fyonda kuri `seed nshasha` (ifise ikimenyetso c'amadayimoni).



![Image](assets/fr/030.webp)



Hanyuma uhitemwo uburebure bw’ijambo ryawe ry’ukwibuka. Amajambo 12 asanzwe atanga urugero rw’umutekano ruhagije, rero iri ni ryo hitamwo nsaba.



![Image](assets/fr/031.webp)



Zirikana amadayimoni yawe maze winjize imibare ivuyemwo ukoresheje urudome. Kanda buto iri hagati kugira ngo wemeze ikintu cose winjije. Iyo ukoze ikosa, urashobora gusubira inyuma. Koresha amadayimoni atandukanye menshi kugira ngo ugabanye ingaruka z’amadayimoni yose ataringaniye. Raba neza ko ata muntu ariko arakuraba mu gihe c’iyi operation.



![Image](assets/fr/032.webp)



Iyo umaze kwinjiza ama throws yawe 50, SeedSigner iratanga sentensi yawe. **Kurikiza neza amabwirizwa ari muri iyi nyigisho nimba uriko uratangura:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Kwerekana no kubika seed



Wandike witonze amajambo y’ijambo ryawe ry’ukwibuka ku kintu kibereye co gushigikira (impapuro canke icuma).



![Image](assets/fr/033.webp)



### 5.5 Gusuzuma ububiko



Kugira ngo wirinde amakosa yose yo gusubiza inyuma, SeedSigner iragusaba kugenzura ububiko bwawe. Fyonda kuri `Suzuma`.



![Image](assets/fr/034.webp)



Hanyuma winjize ijambo usavye ukurikije urutonde rwaryo mu nteruro. Nk’akarorero, aha ntegerezwa guhitamwo ijambo rya gatatu mu nteruro yanje.



![Image](assets/fr/035.webp)



Iyo ukoze ikosa, SeedSigner azokumenyesha, kandi uzobwirizwa gusubira gutangura, urabe neza ko wanditse ijambo ryawe ry’ukwibuka igihe riguhawe. Iyi ntambwe yo kugenzura iratuma ububiko bwawe bugororotse kandi bushitse. Igihe bimaze kwemezwa, igicapo kizokwerekana `Igisubizo cagenzuwe`.



![Image](assets/fr/036.webp)



Kugira ngo ubone ikigeragezo co gusubizaho, kurikiza iyi nyigisho :



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Gutahura iciyumviro c'"igikoresho kitagira igihugu



SeedSigner ni igikoresho kitagira ubwonko buhoraho. Ivyo bisigura ko seed yawe itigera ibikwa imbere mu gikoresho (bitandukanye n’akarorero Ledger, Trezor canke Coldcard). Ukimara kuzimya umuriro, seed irazimangana burundu muri RAM yayo. Iyo usubiye gutangura, SeedSigner isubira mu rwego rw’ubusa: uzoca ubwirizwa kuyiha seed yawe kandi, kugira ngo ishobore gusinya amafaranga yawe.



Ivyo biratanga uburinzi buhambaye. Udakunze izindi nkoko z’ibikoresho, SeedSigner ishingiye kuri Raspberry Pi Zero, idafise uburinzi bw’umubiri, harimwo *Ikintu gitekanye*. Ariko kubera ko ata makuru y’agaciro abikwa, mbere n’igikoresho gishobora guhungabanywa ku mubiri nticokwemera ko uwugutera akuraho imfunguruzo zawe z’ibanga canke ngo akoreshe amahera yawe y’ibiceri.



Ku rundi ruhande, iyo nyubakwa isobanura inshingano y’inyongera: ata n’umwe yogufasha, amahera yawe arazimangana ata kabuza. Ni co gituma ndabagira inama yo gukora **backup kabiri**. Usanzwe ufise ijambo ryawe ryo gukira: iri ni ryo ry’ingenzi ry’igihe kirekire, ryo kubika ahantu hatagira inkomanzi. None tugiye gukora kopi y'iri jambo mu buryo bwa **QR code**.



Igihe cose ukoresheje SeedSigner, uracapura iyo kode ya QR ukoresheje kamera y’ico gikoresho kugira ngo ishire seed yawe mu ciyumviro cayo mu gihe uriko urashira umukono ku vyo ukoresha. Iyi backup ya kabiri, igenewe gukoreshwa buri musi, na yo nyene itegerezwa kubikwa neza cane: umuntu wese afise iyi kode ya QR arashobora kuronka amafaranga yawe yose.


Ndaguhanura kandi ngo ubike kode yawe ya QR n’ijambo ryawe ry’ukwibuka ahantu habiri hatandukanye, kugira ngo ntutakaze vyose iyo habaye ikirego.



Ubwa nyuma, uburyo buteye imbere kandi butekanye ni ugukoresha SeedSigner n'**SeedKeeper**, ibika seed muri secure element. Kugira ngo umenye vyinshi, raba iyi nyigisho:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Kwandika urutoke rw'urufunguzo rwa mbere



Igihe igenzura rirangiye, SeedSigner yerekana urutoke rw’urufunguzo rwa wallet yawe. Ico kimenyetso c’urutoke kigaragaza wallet yawe kandi kigatuma ukoresha ijambo ryiza ryo gukira muri kazoza. Nta makuru n’amwe yerekana yerekeye imfunguruzo zawe z’ibanga, rero urashobora kuzibika ata nkomanzi ku buryo bwa digitale. Raba neza gusa ko ubika kopi umuntu ashobora kuyironka kandi ntuzokwigere uyitakaza.



![Image](assets/fr/037.webp)



Ni muri iyi ntambwe kandi ushobora kwongerako **passphrase BIP39** kugira ngo ukomeze umutekano wa wallet yawe. Bivanye n’ingene ukoresha ubuhinga bwo gusubiza inyuma, iyo nzira yoshobora kuba ngirakamaro, ariko kandi irazana ingorane: iyo utakaje passphrase, uburenganzira bwo gushika ku bitcoins zawe buzobura ubuziraherezo.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Niba utaramenya neza iciyumviro ca passphrase, ndagutumiye gusoma iyi nyigisho yuzuye ku bijanye n’ico kibazo:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Kubika seed mu buryo bwa QR (*ImbutoQR*)



SeedSigner iragufasha guhindura seed yawe mu kode ya QR y’impapuro, yitwa *SeedQR*. Ubwo buryo buratuma vyoroha gusubira gushiramwo wallet yawe, kuko bituma udasubira kwandika ijambo ryose n’amaboko.



Kugira ngo ubikore, uzokenera urupapuro rudafise ikintu canke kode QR y’icuma ihuye n’uburebure bw’ijambo ryawe ry’ukwibuka. Niba waraguze umuzigo wuzuye wa SeedSigner yawe, ibigereranyo akenshi birashirwamwo. Niba atarivyo, urashobora kubikura kuri internet ukabicapura (canke ukabisubiramwo n’ukuboko) hano :




- [Igishushanyo c'amajambo 12](https://github.com/Imbuto/imbuto/blob/dev/inyandiko/imbuto_qr/ibigereranyo_bishobora_gucapwa/uruzitiro_25x25.pdf)
- [Uburyo bw'amajambo 24](https://github.com/Imbuto/imbuto/blob/dev/inyandiko/imbuto_qr/ibigereranyo_bishobora_gucapwa/uruzitiro_29x29.pdf)
- [Igishushanyo c'amajambo 12](https://github.com/Imbuto/imbuto/blob/dev/inyandiko/imbuto_qr/ibigereranyo_bishobora_gucapwa/uruzitiro_21x21.pdf)
- [Igishushanyo c'amajambo 24](https://github.com/Imbuto/imbuto/blob/dev/inyandiko/imbuto_qr/ibigereranyo_bishobora_gucapwa/uruzitiro_25x25.pdf)



Ku mugaragaro wawe wa seed, hitamwo `Imbuto yo Gusubizaho`.



![Image](assets/fr/039.webp)



Hanyuma uhitemwo `Gusohora nk'ImbutoQR`.



![Image](assets/fr/040.webp)



Hanyuma uhitemwo uburyo wipfuza (ubusanzwe canke bukomeye) bivanye n’urugero rw’impapuro ruriho.



![Image](assets/fr/041.webp)



Fyonda `Tangura` kugira ngo utangure kurema *SeedQR*. SeedSigner izoca yerekana urutonde rw'ibiharuro (A1, A2, B1, n'ibindi), kimwe cose kikaba gihuye n'igice ca kode.



![Image](assets/fr/042.webp)



Usubiremwo witonze akadomo kose k’umwirabura kari ku rupapuro rwawe rwo kubika, hanyuma ukoreshe joystick kugira ngo ugende ku gice gikurikira. Fata umwanya wawe: guhindura neza kode birashobora gutuma kode ya QR idakoreshwa.



Impanuro nke:




- Tangana n’ikaramu kugira ngo ushobore gukosora amakosa yose, hanyuma usubire gukoresha ikaramu nziza cane y’umwirabura umaze guheza;
- Intumbero iri hagati neza hagati y’ikibanza ni co conyene ukeneye, nta nkeka ko uyizuza yose.



![Image](assets/fr/043.webp)



Hanyuma ukande kuri `Confirm SeedQR`, hanyuma ushireko kode yawe ya QR kugira ngo umenye ko ikora neza.



![Image](assets/fr/044.webp)



Iyo ubutumwa `Success` bugaragaye, *SeedQR* yawe irakora: ushobora gutera intambwe ikurikira.



![Image](assets/fr/045.webp)



**Ugumye uru rupapuro nk’uko ijambo ryawe ryo gukira rimeze. Umuntu wese afise iyi QR code arashobora gusubira kwubaka imfunguruzo zawe z’ibanga no kwiba amafaranga yawe y’ibiceri.**



Urasangwa, igitabu cawe ca Bitcoin ubu kiratangura gukora! Ubu tuzokwinjiza ibice vyayo vya bose muri **Sparrow Wallet** kugira ngo tuyicunge mu buryo bworoshe.



## 6. Gushiramwo wallet muri Sparrow



Igihe SeedSigner yawe imaze gushirwaho kandi seed yawe ikaba yarakozwe neza kandi ikabikwa, intambwe ikurikira ni uguhuza iyi nkuru na porogaramu y'uburongozi nka Sparrow Wallet. seed yawe izokwama iguma itari ku murongo, kuko igice ca bose gusa c'ibitabo vyawe kizorungikwa kuri Sparrow. Ivyo bizotuma iyo porogarama ishobora kwerekana amaderesi yawe, amafaranga yawe no kwubaka amafaranga mashasha, ataco ushobora gukoresha amafaranga yawe y’ibiceri. Kugira ngo ukoreshe amafaranga yawe, SeedSigner yawe azokwama ategerezwa gusinya ku gikorwa categuwe na Sparrow.



### 6.1 Gutegura umukono w'imbuto



Injira microSD irimwo ubuhinga bwo gukoresha, ushireko SeedSigner yawe, hanyuma ushiremwo seed uherutse kurema ukoresheje kode yawe ya QR y’inyuma. Ku rubuga rw'Imbere, hitamwo `Scan`, hanyuma uscan SeedQR yawe ukoresheje SeedSigner.



![Image](assets/fr/046.webp)



Suzuma ko urutoke ruri ku rufunguzo rwawe rwa mbere rujanye n'urutoke ruri kuri wallet yawe. Niba uriko urakoresha passphrase, yinjize muri iyi ntambwe.



![Image](assets/fr/047.webp)



Ivyo bigutwara ku rutonde rw'ibitabo vyawe, mu gihe canje citwa `d4149b27`. Niwaba usubiye ku mugaragaro w'intango, hitamwo `Imbuto`, hanyuma uhitemwo icapa rihuye n'igitabo cawe. Hanyuma ukande kuri `Sohora Xpub`.



![Image](assets/fr/048.webp)



Hitamwo ubwoko bw'ibitabo. Mu gihe cacu, ni igitabu kimwe: hitamwo `Single Sig`.



![Image](assets/fr/049.webp)



Igikurikira ni uguhitamwo urugero rw’inyandiko. Igiherutse kandi gifise ubutunzi bwinshi mu bijanye n'ibiciro vy'ugucuruza ni `Taproot`. Ndaguhanura rero ngo uhitemwo iyo ngingo ngenderwako.



![Image](assets/fr/050.webp)



Ubutumwa bwo kugabisha buzoboneka. Ivyo ni ibisanzwe: uru rufunguzo rwa bose rwagutse (`xpub`) rugufasha kubona amaderesi yose yava kuri seed yawe (ku konti ya mbere). Ntibiguha uburenganzira bwo gukoresha amahera yawe, ariko birahishura imiterere y’ibitabo vyawe. Iyo yigeze gusohoka, ni ingorane ku buzima bwite bwawe, ariko si ku mutekano w’ama bitcoins yawe: iraguha uburenganzira bwo kuyabona, ariko ntuyakoreshe.



Fyonda `Ndatahura`, hanyuma `Sohora Xpub` nimba unyuzwe n'amakuru yerekanwa.



SeedSigner rero itanga xpub yawe mu buryo bwa kode ya QR irimwo amakuru yose ukeneye kugira ngo ushobore gucunga ibitabo vyawe muri Sparrow Wallet.



![Image](assets/fr/051.webp)



Ushobora gukoresha joystick kugira ngo utunganye umuco w’ibarabara kugira ngo ushobore gucapura kode ya QR mu buryo bworoshe.



### 6.2 Kwinjiza ibitabo bishasha muri Sparrow Wallet



Raba neza ko ufise porogarama ya Sparrow Wallet iri kuri mudasobwa yawe. Niba utazi uko woyikura, uyisuzume kandi uyishiremwo neza, raba inyigisho yacu yuzuye ku bijanye n’ico kibazo:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kuri mudasobwa yawe, fungura Sparrow Wallet, hanyuma mu rutonde rw'ibintu, ukande `Dosiye → Injira Wallet`.



![Image](assets/fr/052.webp)



Hanukira kuri `Umushingantahe w'imbuto`, hanyuma uhitemwo `Guca...`. Webcam yawe izofunguka: scanner kode ya QR ihinduka yerekanwa ku rubuga rwawe rwa SeedSigner.



![Image](assets/fr/053.webp)



Guha izina igitabu cawe, hanyuma ukande kuri `Rema Wallet`. Sparrow izoca igusaba gushinga ijambobanga ryo gufunga uburenganzira bwo gukoresha iyi wallet. Hitamwo ijambobanga rikomeye: rikingiye ukuronka amakuru y’ibitabo vyawe muri Sparrow (imfunguruzo za bose, aderesi, ibimenyetso n’amateka y’ibikorwa). Iryo jambobanga ntirikenewe kugira ngo usubiremwo igitabo c’ibintu mu nyuma: ijambo ryawe ry’ukwibuka gusa (kandi bishoboka ko ari passphrase yawe) ni ryo rikenewe ku bw’iyo ntumbero.



Ndagusavye ubike iri jambobanga mu mucungerezi w’ijambobanga kugira ngo nturitakaze.



![Image](assets/fr/054.webp)



Ububiko bwawe bw'urufunguzo bwarashizwemwo neza.



![Image](assets/fr/055.webp)



Hanyuma usuzume ko `Ikimenyetso c'urutoke c'umukuru` kigaragara muri Sparrow gihuye n'ico canditswe mbere muri SeedSigner yawe.



Igikoresho cawe co gusinya imbuto na Sparrow Wallet ubu birahuye neza. Sparrow ikora nk’umurongo w’uburongozi wuzuye, mu gihe SeedSigner iguma ari yo yonyene ishobora gusinya amafaranga yawe. Ubu rero witeguriye kwakira no kohereza ama bitcoins mu buryo bufise ikirere cose.



## 7. Kwakira no kohereza amafaranga y’ibiceri .



SeedSigner yawe na Sparrow Wallet ubu vyatunganijwe kugira ngo bikore hamwe. Muri iki gice ca nyuma, turaza kuraba ingene twokwakira no kohereza ama bitcoins dukoresheje iyi configuration.



### 7.1 Kwakira ama bitcoins



#### 7.1.1 Gutanga aderesi y'ukwakira



Kuri mudasobwa yawe, fungura Sparrow Wallet hanyuma ufungure SeedSigner yawe wallet ukoresheje ijambobanga ryawe. Raba neza ko porogarama ihuye na server (notch iri hasi iburyo). Mu ruhande, kanda kuri `Kwakira`.



![Image](assets/fr/056.webp)



Aderesi nshasha ya Bitcoin iragaragazwa. Uzobona :




- Aderesi y'inyandiko (itangura na `bc1p...` niba ukoresha P2TR nk'uko nkora),
- Kode ya QR ihuye,
- Umurima wa `Label` wo gukurikirana amafaranga yawe.



Ndagusavye cane ko wongerako ikimenyetso ku mpapuro z’amahera zose ziri kuri wallet yawe. Ivyo bizokuronsa uburenganzira bwo kumenya bitagoranye aho UTXO imwe imwe yose ikomoka no gutuma urushirizaho gucunga neza ubuzima bwite bwawe. Kugira ngo ushiremwo cane iyo nkuru ihambaye, urashobora kuraba amahugurwa yagenewe Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Kugira ngo wongereko ikimenyetso, shiramwo izina mu mwanya `Ikimenyetso`, hanyuma wemeze.



Nk'akarorero:



```txt
Label : Sale of the Raspberry Pi Zero
```



Ubu aderesi yawe ifatanye n’iki kimenyetso mu bice vyose vya Sparrow.



![Image](assets/fr/057.webp)



#### 7.1.2 Igenzura rya Address ku Mushingantahe w'Imbuto



Imbere yo gusangira aderesi yawe, birahambaye cane ko usuzuma ko ari iya seed yawe. Iyi ntambwe ituma SeedSigner yawe ishobora gusinya amafaranga ajanye n'iyi aderesi. Irakingira kandi ibitero bishobora gushika aho Sparrow yerekana aderesi y’ubuhendanyi. Ibuka ko Sparrow ikoresha ahantu hatagira umutekano (mudasobwa yawe), ifise ahantu hanini cane ho gutera kuruta SeedSigner yawe, ikaba iri ukwayo rwose. Ni co gituma udakwiye kwigera wemera ataco uzi amaderesi y’ukwakira yerekanwa kuri Sparrow gushika uyasuzumye ukoresheje ibikoresho vyawe vya wallet.



Ku Sparrow, fyonda ku kode ya QR y’iyo aderesi kugira ngo uyikuze: izoca yerekanwa ku rubuga rwose.



![Image](assets/fr/058.webp)



Ku SeedSigner yawe, mu bimenyetso nyamukuru, hitamwo `Scan`. Scan code ya QR yerekanwa ku rubuga rwa mudasobwa yawe, hanyuma uhitemwo seed ihuye na wallet yawe (mu gihe canje, urutoke rwa `d4149b27`).



![Image](assets/fr/059.webp)



Niba aderesi ya scanner ihuye n'iyo yavuye kuri seed yawe, igicapo ca SeedSigner kizokwerekana ubutumwa: `Address Verified`.



![Image](assets/fr/060.webp)



Ivyo vyemeza ko iyo aderesi ari iya wallet yawe kandi ko ushobora kuyironka wizigiye.



#### 7.1.3 Kwakira amafaranga



Ubu ushobora kumenyesha iyo aderesi (mu nyandiko canke mu buryo bwa QR code) umuntu canke igisata gikeneye kukurungikira satss. Igihe amafaranga amaze gutangazwa ku rubuga, azoboneka mu gice ca `Ibikorwa` ca Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Wohereze ama bitcoins



Kurungika amafaranga y'ibiceri n'umusinya w'imbuto ni inzira y'intambwe 3:




- Irema ry’ibikorwa muri Sparrow ;
- Umukono w'ibikorwa ku SeedSigner ;
- Ugusangira kwa nyuma kw’isoko biciye kuri Sparrow.



Ivyo vyose bihanahana hagati y’ivyo bikoresho bibiri bikorwa gusa hakoreshejwe amakode ya QR.



#### 7.2.1 Gukora ubucuruzi muri Sparrow



Mu Sparrow Wallet, ushobora gufyonda ku `Kohereza` mu ruhande rw'ibubamfu. Ariko rero, ndakunda gukoresha urupapuro rwa `UTXOs`, rugufasha kwimenyereza "*Coin Control*". Ubu buryo buraguha ububasha bwo kugenzura neza ama UTXO akoreshwa, kugira ngo ushobore kugenzura amakuru uhishura mu gihe c’ugucuruza.



Mu `UTXOs`, hitamwo ibiceri wipfuza gukoresha, hanyuma ukande `Ohereza Ivyatoranijwe`.



![Image](assets/fr/062.webp)



Hanyuma wuzuze ivyicaro vy'amafaranga:




- Mu `Pay to`, shiramwo aderesi y’uwuronka canke ukande ku kimenyetso ca kamera kugira ngo ushireko kode ya QR;
- Mu `Ikimenyetso`, wongeremwo ikimenyetso co gukurikirana iyo nsiguro;
- Mu `Igiciro`, shiramwo igiciro kizorungikwa;
- Ubwa nyuma, hitamwo igipimo c’amahera ushingiye ku mibereho y’isoko (ibiharuro biraboneka kuri [mempool.space](https://mempool.space/)).



Ivyo bibanza bimaze kwuzura, suzuma neza amakuru, hanyuma ukande kuri `Create Transaction >>`.



![Image](assets/fr/063.webp)



Suzuma amakuru y'ibikorwa kugira ngo umenye neza ko vyose ari ukuri, hanyuma ukande kuri `Sozera ibikorwa kugira ngo usinye`.



![Image](assets/fr/064.webp)



Ivyo bikoresho ubu birateguwe, ariko ntibirashirwako umukono. Kugira ngo ugaragaze [PSBT (*Partially Signed Bitcoin Transaction*)](PSBT) nk'ikode ya QR, kanda kuri `Kwerekana QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Gusinya amasezerano n'umusinya w'imbuto



Hindukiza SeedSigner yawe maze ushireko SeedQR yawe kugira ngo ushikire igitabu cawe, nk’uko bisanzwe. Ku rubuga rw'intango, hitamwo `Scan`, hanyuma scanne kode ya QR yerekanwa kuri Sparrow.



![Image](assets/fr/066.webp)



Hanyuma uhitemwo seed kugira ngo ihure n’ivyo ufise.



![Image](assets/fr/067.webp)



SeedSigner ihita imenya ko ari PSBT maze igaragaza incamake y'ivyo yakoze:




   - Amafaranga yoherejwe,
   - Aderesi z'isohoka,
   - Ibiciro bijanye n’ugucuruza.



Fyonda kuri `Isubiramwo ry'Ibisobanuro` maze usuzume neza amakuru yose ataco akora ku rubuga rwa SeedSigner. Ibintu bihambaye cane umuntu akwiye kugenzura ni amahera yoherejwe, aho uwuyakira aba n’amahera yoherezwa.



![Image](assets/fr/068.webp)



Niba vyose bimeze neza, hitamwo `Kwemeza PSBT` kugira ngo ushire umukono ku gikorwa ukoresheje urufunguzo rw'ibanga rujanye n'ivyo.



![Image](assets/fr/069.webp)



Iyo imaze gusinywa, SeedSigner itanga kode nshasha ya QR irimwo amafaranga yashizweko umukono, yiteguriye gupimwa na Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Gutangaza ivy'ugucuruza kuva kuri Sparrow



Ubu iyo nzira y’ubudandaji ifise akamaro, irakeneye gutangazwa ku rubuga rwa Bitcoin, kugira ngo igere ku mucukuzi azoyishira ku gice.



Ku Sparrow, fyonda ku `Isuzuma rya QR`.



![Image](assets/fr/071.webp)



Yerekana kode ya QR yerekanwa na SeedSigner yawe (iyo y’ugucuruza kwasinywe) kuri webcam. Sparrow izocapura umukono maze yerekane amakuru yose yerekeye ivy’ugucuruza. Suzuma ubwa nyuma ko amakuru yose ari ukuri, hanyuma ukande kuri Broadcast Transaction kugira ngo uyatangaze ku rubuga rwa Bitcoin.



![Image](assets/fr/072.webp)



Ubu amafaranga yawe yarungitswe ku rubuga rwa Bitcoin. Ushobora gukurikirana ingene itera imbere mu gice ca `Ibikorwa` ca Sparrow Wallet.



![Image](assets/fr/073.webp)



Ubu waramenye neza ivy'ishimikiro vyo gukoresha SeedSigner. Kugira ngo ushiremwo ubumenyi bwinshi no gutohoza ingene ikoreshwa mu buryo buteye imbere, ndagutumiye ngo urabe inyigisho ikurikira:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Ushobora kandi gushigikira iterambere ry'umugambi wa SeedSigner mu gutanga intererano mu bice vy'amahera!](https://seedsigner.com/donate/)**



*Iciyumviro: amwe mu mashusho ari muri iyi nyigisho ava ku [urubuga rwemewe rw’umugambi wa SeedSigner](https://umusinyi w’imbuto.com/) no ku [bubiko bwa GitHub](https://github.com/Umusinyi w’imbuto/umusinyi w’imbuto).*