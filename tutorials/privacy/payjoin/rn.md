---
name: Payjoin
description: PayJoin kuri Bitcoin ni iki?
---
![Payjoin thumbnail - steganography](assets/cover.webp)





## Gutahura Ibikorwa vya PayJoin ku Bitcoin.


PayJoin ni umubumbe wihariye w’ugucuruza kwa Bitcoin kwongereza ubuzima bwite bw’ukoresha mu gihe c’ukwishura mu gukorana n’uwuronka ukwishyura.


Mu mwaka w’2015, [LaurentMT](https://twitter.com/LaurentMT) yaravuze ubwa mbere ubwo buryo nk’“ibikorwa vy’ubuhinga bwa none” mu nyandiko ishobora gushikwako . [hano] (aha] (inyandiko y'ivyo bikoresho). Ubu buhinga bwaje kwemerwa n’ishirahamwe Samourai Wallet, ryabaye umukiriya wa mbere yabushize mu ngiro n’igikoresho ca Stowaway mu 2018. Iciyumviro ca PayJoin kiraboneka kandi muri [BIP79](Https. [BIP78] (Ubuhinga bwa none). Amajambo menshi arakoreshwa mu kwerekeza kuri PayJoin:


- PayJoin
- Ububiko
- P2EP (Ukwishura-ku-Iherezo-Iciyumviro)
- Ibikorwa vy'ubucuruzi


Ubudasa bwa PayJoin buri mu bushobozi bwayo bwo gukora generate igikorwa kimeze nk’igisanzwe iyo umuntu abibonye ubwa mbere ariko mu vy’ukuri ari mini CoinJoin hagati y’abantu babiri. Kugira ngo ivyo bishoboke, urutonde rw’ugucuruza rushiramwo uwuronka amahera iruhande y’uwurungika vy’ukuri mu vyo yinjiza. Uwuronka ashiramwo amahera yishura hagati mu vyo akora, ivyo bikaba bituma ashobora kwishurwa.


Reka dufate akarorero nyako: iyo uguze baguette ku `4000 Sats` ukoresheje UTXO ya `10,000 Sats` maze ugahitamwo PayJoin, umutetsi wawe azokwongerako UTXO ya `15,000 Sats` nk’uko bazoronka nk’uko bazoronka, ku `4000 Sats` yawe:

![Payjoin transaction diagram](assets/en/1.webp)


Muri aka karorero, umutetsi ashiramwo `15.000 Sats` nk’inyungu agasohoka afise `19.000 Sats`, n’itandukaniro ry’ukuri `4000 Sats`, ari ryo giciro c’umukate w’umukate. Ku ruhande rwawe, winjira ufise `10.000 Sats` ugaheza ukagira `6.000 Sats` nk’isohoka, bikaba bigereranya umubare w’amahera `-4000 Sats`, ari vyo biciro vy’inyama z’ingurube. Kugira ngo nshobore kworohereza akarorero, narakuye n’ibigirankana amahera ya Mining muri iri soko.


## Ni igiki gifise intumbero y’ugucuruza PayJoin?


Igurisha rya PayJoin rifise intumbero zibiri zituma abakoresha bashobora kwongereza ubuzima bwite bw’amahera bariha.

Mbere na mbere, PayJoin ifise intumbero yo kuzimiza uwuyibona wo hanze mu kurema uruyeri mu gusesangura uruhererekane. Ivyo bishoboka biciye ku nzira y’ubuhinga bwa Ownership (CIOH). Kenshi, iyo igikorwa co kuri Blockchain gifise ibintu vyinshi vyinjizwa, bifatwa ko ivyo bintu vyose bishobora kuba ari ivy’ikigo kimwe canke umukoresha umwe. Gutyo, iyo umuhinga mu vy’ugusesangura asuzuma ivy’ubudandaji bwa PayJoin, baca bajana mu kwemera ko ivyo vyose bishirwamwo biva ku muntu umwe. Ariko rero, iyo nzira y’ugutahura nta co imaze kuko uwuronka amahera na we nyene atanga ivyo yinjiza iruhande y’uwuronka amahera nyayo. Rero, isesengura ry’uruzitiro rihindurwa rikaja ku nsobanuro ihinduka ikinyoma.


Ikindi kandi, PayJoin iremeza kandi guhenda umuntu wo hanze yihweza ku bijanye n’ingero nyayo y’amahera yatanzwe. Mu gusuzuma ingene ibikorwa vy’ubudandaji bigenda, uwo musesanguzi yoshobora kwizera ko amahera yishurwa angana n’ingero y’imwe mu nzira zisohoka. Ariko mu vy’ukuri, amahera yo kwishura ntahuye n’ivyo bivako vyose. Mu vy'ukuri ni itandukaniro hagati y'ivyo uwuronka asohora UTXO n'ivyo uwuronka yinjiza UTXO. Muri ubwo buryo, igikorwa ca PayJoin kigwa mu rwego rw’ubuhinga bwa steganography. Bituma umuntu ashobora guhisha umubare nyawo w’ibintu bigurishwa mu gihe c’ubudandaji bw’ikinyoma bukora nk’uruyeri.


Ndagusavye, wibuke insobanuro yacu ya **Inyandiko**:

> Steganography ni ubuhinga bwo guhisha amakuru mu bindi bimenyetso canke ibintu mu buryo butuma ukubaho kw’ayo makuru yanyegejwe kutaboneka. Nk’akarorero, ubutumwa bw’ibanga burashobora guhishwa imbere mu kadomo mu nyandiko ataco buhuriyeko, bigatuma umuntu adashobora kububona n’ijisho ryiwe (ubu ni ubuhinga bwa micropoint). Mu buryo butandukanye n’ugushiramwo amakuru, ivyo bikaba bituma amakuru adashobora gutahurwa ata rufunguzo rwo gufungura, steganography ntihindura amakuru. Iguma yerekanwa ahantu abantu bose bayibona. Intumbero yayo ahubwo ni iyo guhisha ukubaho kw’ubutumwa bw’ibanga, mu gihe gupfuka amakuru y’ibanga bigaragaza neza ko hariho amakuru yihishije, naho nyene ata rufunguzo umuntu ashobora kuyaronka.

Reka dusubire ku karorero kacu k’ugucuruza PayJoin kugira ngo umuntu yishure baguette.

![Payjoin transaction schema from the outside](assets/en/2.webp)

Mu kubona iyo nzira kuri Blockchain, uwubibona wo hanze akurikiza ubuhinga busanzwe bwo gusesangura uruhererekane yobisobanura gutya: "*Alice yashize hamwe UTXO 2 nk'ibintu vyinjijwe mu nzira kugira ngo yishure `19,000 Sats` kuri Bob*."

![Incorrect interpretation of Payjoin transaction from the outside](assets/en/3.webp)

Ivyo bisobanuro biragaragara ko ataco bimaze kuko nk’uko musanzwe mubizi, izo UTXO zibiri z’injiza si iz’umuntu umwe. Ikindi kandi, agaciro nyako k’amahera yishuwe si `19.000 Sats`, ahubwo ni `4.000 Sats`. Isesengura ry’uwubibona wo hanze rero ryerekezwa ku nsozero itari yo, rikagira ngo ubuzima bwite bw’abafatanyabikorwa buzigame.![Igishushanyo c’ibikorwa vya PayJoin](assets/en/1.webp)

Niba wipfuza gusuzuma igikorwa nyaco ca PayJoin, ng’iki kimwe nakoze kuri Testnet: n 333c2f465d3668c678691a091cdd6e5984c)



**Ibikoresho vyo hanze:**


- 10:10, 11. 10 Igikoresho co gucungera amakuru y'ivy'ubuhinga bw'ivy'ubuhinga bw'ivy'ubuhinga bw'ivy'ubuhinga bw'ivy'ubuhinga.
- Ivyo bimenyetso vy'ubuhinga bwa none.
- Urubuga rwitwa PayJoin.org/

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c