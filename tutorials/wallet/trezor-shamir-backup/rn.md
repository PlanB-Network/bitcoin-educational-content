---
name: Trezor Shamir Backup
description: Amajambo y'ugusangira rimwe n'ugusangira kenshi Mnemonic kuri Trezor
---
![cover](assets/cover.webp)



*Ishusho: [Trezor.io]*



## Amahitamwo mashasha yo gusubiza inyuma kuri Trezor



Kuva mu mwaka w’2023, Trezor yaratanga uburyo bushasha bwo gucungera amakuru bwitwa ***Single-share Backup***, buhoro buhoro bugasubirira uburyo bwa kera bushingiye kuri BIP39 buboneka ku ma wallet menshi. Udakunze amajambo ya kera y’amajambo 12 canke 24 Mnemonic, iyi nzira nshasha ishingiye ku majambo imwe y’amajambo 20 akomoka ku rugero rwateguwe na SatoshiLabs: **SLIP39**. Intumbero ni ugutuma ububiko bukomera kandi bugasomwa, mu gihe bishoboza kwimuka neza ku citegererezo c’ububiko bukwiragijwe.



Ico kigereranyo gikwiragijwe citwa ***Igikorwa co gusangira vyinshi***. Ishingiye kuri iyo ngingo nyene, ariko aho gutanga ijambo rimwe rya Mnemonic, riyigabanyamwo ibice vyinshi vyitwa ***shares***, kimwe cose kikaba ari ijambo rya Mnemonic mu buryo bwaco bwite. Kugira ngo Wallet isubireho, umubare kanaka w'izo *migabane* (isobanurwa n' *umurongo*) utegerezwa gusubira guhurizwa hamwe. Nk'akarorero, mu mugambi wa 3-ku-5, *imigabane* 3 yose kuri 5 izogarura Wallet. Urashobora kubona ko uburyo bwo gucungera amakuru bwa Trezor butandukanye n’amasakoshi ya Multisig. Kugira ngo ukoreshe ama bitcoins yawe, usaba gusa Hardware Wallet Trezor yawe. Ni umukono umwe gusa usabwa. Gukwirakwiza bikoreshwa gusa ku rugero rw’ijambo Mnemonic, ni ukuvuga ivy’inyuma.



![Image](assets/fr/01.webp)



Iyi sisitemu itorera umuti ingorane y'intangamarara imwe y'ijambo Mnemonic ata ngorane zijanye n'ugucungera Multisig canke passphrase BIP39. Inzira yo gusubirana ntigishingiye ku makuru amwe, ahubwo ishingiye ku makuru menshi, harimwo n’inyungu yo kwihanganira gutakaza bivuye ku nzira y’imbere.



Abakoresha bakoze Wallet ifise *Igikoresho co gusangira kimwe* barashobora guhindukira bakaja ku *Igikoresho co gusangira vyinshi* igihe cose batabwirizwa kwimura Wallet yabo. Ukwakira amaderesi n’amakonti bizoguma ari bimwe. Uburyo bwa *Multi-share* bugira ico bukoze gusa ku bijanye n’ugusubiza inyuma, mu gihe ibindi vya Wallet biguma bitahindutse.



Ivy’ugusangira ibintu vyinshi* biraboneka kuri Trezor Model T, Safe 3 na Safe 5. Ivyo ntibishigikirwa na Trezor Model One.



**Iciyumviro gihambaye:** Uburyo bwa Trezor bwo *Multi-share* buratekanye mu buryo bw'ibanga, kuko bukoresha umugambi wa *Shamir wo gusangira ibanga* mu gukwiragiza. Turahanura cane ko utokoresha uburyo busa n’ubwo n’amaboko, mu gucapura ijambo rya kera rya Mnemonic wewe nyene. Ni umugenzo mubi wongerera cane ingorane zo kwibwa no gutakaza amafaranga yawe ya bitcoins, rero ntubikore. Invugo ya kera ya Mnemonic irabikwa yose uko ingana.



## Ibanga rya Shamir ryo gusangira muri SLIP39



Uburyo bwo gukingira amakuru bushingiye ku *Multi-share* kuri Trezor ni *Igishushanyo co gusangira ibanga rya Shamir* (SSSS). Ingingo yayo ni iyi: amakuru y’ibanga (muri iki gihe, seed ya Wallet) ahindurwa igiharuro c’imibare. Hanyuma haharurwa uturongo twinshi tw’iyi nkuru, umwe wose ukaba umugabane. Ibanga ry’intango risubirwamwo n’ugushiramwo amajambo menshi, mu gukoranya umubare mutoyi w’ibiharuro (uruzitiro).



Nta makuru y’ibanga ashobora gukurwa mu mubare w’imigabane iri munsi y’urugero, bikaba vyemeza umutekano w’ivyiyumviro utunganye w’amakuru y’ibanga. Mu yandi majambo, mbere n’umuterabwoba afise ububasha bwo gukoresha ubuhinga butagira aho bugarukira ntashobora gutekereza ku seed iyo atashitse ku rugero.



SLIP39 ikoresha iyo nzira kugira ngo itangaze seed Wallet. Buri mugabane ni interuro y’amajambo 20, yubatswe ku rutonde rw’amajambo 1024 (rutandukanye n’urutonde rwa BIP39).



## Gushinga ububiko bwo gusangira vyinshi ku Trezor



Igihe urema Wallet yawe kuri Trezor, ufise uburyo butatu butandukanye:




- Koresha ijambo rya kera ry’ikirundi BIP39 Mnemonic ry’amajambo 12 canke 24;
- Koresha ijambo ry’ikirundi ry’umugabane umwe Mnemonic (SLIP39);
- Gutegura amajambo menshi ya Mnemonic mu Gusangira vyinshi (SLIP39).



Niwahitamwo ijambo ry'ugusangira rimwe SLIP39 Mnemonic, uzoshobora guhindura ukaja ku gusangira vyinshi mu nyuma ataco ukeneye gusubiramwo Wallet. Ku rundi ruhande, iyo utanguye n’ijambo rya kera BIP39 Wallet (ijambo ry’amajambo 12 canke 24), ntuzoshobora kurihindura ataco rihinduye ngo ribe Multi-share. Uzobwirizwa gukora Wallet nshasha ya Multi-share kuva mu ntango maze ushire amahera yawe kuri Wallet ya kera uyishire ku yindi nshasha biciye ku nzira imwe canke nyinshi za Bitcoin. Ivyo ni igikorwa kigoye cane kandi gitwara amahera menshi. Niba ushaka gukora iyo migrasion, ndagusavye ugure Trezor nshasha ya Hardware Wallet kugira wirinde kwinjira muri seed yawe kuri software ya Wallet.



Muri iyi nyigisho, tuzobanza kuraba ingene twoshiraho Multi-share igihe dukora Wallet, hanyuma, mu gice gikurikira, tuzobona ingene twohindura Single-share mu Multi-share kuri Wallet iriho.



Niba ukeneye gufashwa mu gutegura igikoresho cawe, turafise kandi inyigisho zitomoye ku kigereranyo cose ca Trezor:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Ku modoka nshasha ya Wallet



Ubu wararangije gutegura Trezor yawe kandi witeguye gukora Wallet. Muri Trezor Suite, fyonda ku buto "*Rema Wallet nshasha*".



![Image](assets/fr/02.webp)



Hitamwo "*Gusangira vyinshi*", hanyuma ukande kuri "*Rema Wallet*".



![Image](assets/fr/03.webp)



Wemere amabwirizwa y'ikoreshwa kuri Trezor yawe maze wemeze ko Wallet yaremwe.



![Image](assets/fr/04.webp)



Muri Trezor Suite, kanda kuri "*Bandanya ukora ububiko*".



![Image](assets/fr/05.webp)



Soma neza amabwirizwa, uyamenyeshe, hanyuma ukande kuri "*Rema Wallet backup*".



![Image](assets/fr/06.webp)



Kugira ngo umenye vyinshi ku buryo bwiza bwo kubika no gucunga amajambo yawe ya Mnemonic, ndagusavye cane gukurikira iyi yindi nyigisho, cane cane nimba uri umutanguzi:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ku Trezor, hitamwo umubare wose w'imigabane wipfuza gutunganya. Ivyiyumviro bikunze kuboneka ni 2-de-3 na 3-de-5. Ku karorero, nzokora 2-de-3, rero nzotora imigabane 3. Buri mugabane uzogereranya amajambo 20 Mnemonic.



*Ku bakoresha Safe 5, naho igicapo kizovuga ngo "Tap to continue", mu vy'ukuri uzokenera guca hejuru kugira ngo wemeze*



![Image](assets/fr/07.webp)



Hanyuma wemeze igipimo, ni ukuvuga umubare w’imigabane isabwa kugira ngo umuntu asubire kuronka Wallet n’ama bitcoins arimwo.



![Image](assets/fr/08.webp)



Trezor izokora imigabane yawe itandukanye (amajambo Mnemonic) ikoresheje umubare wayo w’imburakimazi. Raba neza ko udashobora kurabwa mu gihe c’iyi operation. Andika amajambo atangwa ku rubuga ku gikoresho c’umubiri uhisemwo. Ni vyiza ko amajambo aguma afise inomero kandi akurikirana.



Ndagusavye kwandika umugabane wose ku buryo butandukanye maze ukawucungera neza ububiko bwawo kugira ngo wirinde ko benshi bashobora gushikira ahantu hamwe. Nk’akarorero, ku bijanye n’ugutunganya 2-of-3 nk’ukwanje, uburyo bumwe bwoba ari ubwo kubika umugabane umwe i muhira iwanje, uwundi n’umugenzi nizigira, uwa nyuma nkawubika mu safe ya banki. Guhitamwo aho uzobika ibintu bizovana n’ingene uzokwikingira.



Ushobora kubona hejuru y'ibarabara umugabane uriko urabona ubu.



n’ukuri, ntushobora kwigera usangira aya majambo kuri internet, nk’uko ndiko ndabikora muri iyi nyigisho. Aka karorero Wallet kazokoreshwa gusa kuri Testnet kandi kazokurwaho ku mpera y’inyigisho.



![Image](assets/fr/09.webp)



Kugira ngo ugende ku majambo akurikira, fyonda ahantu hasi ku rubuga. Ushobora gusubira inyuma mu gunyerera hasi. Umaze kwandika amajambo yose, ushire urutoke rwawe ku gicapo kugira ngo ugende ku gindi gice gikurikira, hanyuma usubiremwo ivyo.



![Image](assets/fr/10.webp)



Ku mpera y’inyandiko yose yo gusangira, uzosabwa guhitamwo amajambo ari mu nteruro yawe ya Mnemonic kugira ngo wemeze ko wayanditse neza.



![Image](assets/fr/11.webp)



Kandi nivyo, warashoboye gukora backup ya Wallet yawe ukoresheje uburyo bwa Multi-share. Ubu ushobora kubandanya n'amabwirizwa asigaye y'imiterere.



### Ku nzira y’umugabane umwe iriho Wallet



Niba usanzwe ufise Trezor Wallet ifise ububiko bw’ugusangira rimwe (ijambo SLIP39 Mnemonic, atari ijambo rya kera rya BIP39), kandi wipfuza gutuma ububiko bwawe bwa Wallet buboneka kandi bukagira umutekano, urashobora gushinga uburyo bwo gusangira vyinshi ataco ukeneye guhindura bico yawe.



Kugira ngo ubikore, huza kandi ufungure Hardware Wallet yawe. Mu Suite ya Trezor, genda kuri Amategeko.



![Image](assets/fr/12.webp)



Genda ku rubuga rwa "*Igikoresho*".



![Image](assets/fr/13.webp)



Hanyuma ukande kuri "*Rema ububiko bw'ibintu vyinshi*".



![Image](assets/fr/14.webp)



Soma amabwirizwa, hanyuma ukande kuri "*Rema ububiko bw'ibintu vyinshi*".



![Image](assets/fr/15.webp)



Uzoca ukenera kwinjiza ijambo ryawe ry’ubu rya Mnemonic (ugusangira rimwe) ku gicapo cawe ca Trezor. Hitamwo umubare w'amajambo (imbere ni 20).



![Image](assets/fr/16.webp)



Hanyuma ukoreshe klavye iri ku rubuga ya Trezor kugira ngo winjize ijambo ryose ry’interuro yawe ya Mnemonic ubu.



![Image](assets/fr/17.webp)



Ushobora rero guhitamwo uko ukoresha Multi-share Backup yawe ukurikije amabwirizwa yatanzwe mu gice ca mbere.



![Image](assets/fr/18.webp)



Umaze gukora Multi-share Backup yawe, uzokenera gufata ingingo y’ico uzokora n’ijambo ryawe ry’intango ry’ugusangira rimwe Mnemonic. Uko Bitcoin Wallet iguma ari imwe, iri jambo rimwe rizokwama rituma umuntu ashobora kuyironka. Ivyo bizovana n’ingene ukoresha umutekano wawe, ariko muri rusangi, ni vyiza gusenyura iri jambo kugira ngo ukureho iyo ngingo imwe gusa y’ukunanirwa, ari yo nyene intumbero ya Multi-share Backup. Niwafata ingingo yo kuyisambura, urabe ko ubigira ata nkomanzi, kuko **iracari itanga uburenganzira bwo gushika ku ma bitcoins yawe**.



Urasangwa, ubu uri ku rugero rwo gukoresha ama Backups y’ugusangira rimwe n’ugusangira kenshi ku bikoresho vya Trezor. Niba wifuza gutera intambwe imbere mu mutekano wawe wa Wallet, raba iyi nyigisho ku majambo y'ibanga ya BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Niwaba wabonye iyi nyigisho ari ngirakamaro, noshima cane iyo usiga urukumu rwa Green aha hepfo. Ntutinye gusangiza abandi iyi nkuru ku mbuga zanyu zo gusangirirako amakuru. Murakoze cane!



## Ibindi bikoresho





- [Igitabu-0039: Ibanga rya Shamir ryo gusangira amakode ya Mnemonic]
- [Ivyiyumviro vy’ugusangira vyinshi kuri Trezor](https://trezor.io/kwiga/a/ugusangira-vyinshi-ku-trezor);
- [Wikipedia: Ugusangira ibanga rya Shamir](ibanga rya Shamir).