---
term: INZIRA Y'IKOMOKA
---

Mu bijanye n'ibipapuro vy'amahera vy'ubukuru (HD), inzira y'ugukura yerekeza ku rutonde rw'ibiharuro bikoreshwa mu gukura imfunguruzo z'abana ku rufunguzo rw'umukuru. Idondowe muri BIP32, iyi nzira igaragaza imiterere y'igiti co gukuramwo imfunguruzo z'abana. Inzira y'ugukomoka igereranywa n'urutonde rw'ibiharuro bitandukanijwe n'ibiharuro, kandi yama itangurana n'urufunguzo rwa mbere (rwerekanwa na `m/`). Nk'akarorero, inzira isanzwe ishobora kuba `m/84'/0'/0'/0/0`. Buri rwego rw'inkomoko rufitaniye isano n'uburebure bwihariye:


- `m /` yerekana urufunguzo rw'ibanga. Ni ikintu kidasanzwe ku Wallet kandi ntishobora kugira abavukanyi mu burebure bumwe. Urufunguzo rwa mbere rukomoka ata guca ku ruhande kuri seed;

`m / purpose' /` yerekana intumbero y'inkomoko ifasha kumenya urugero rukurikira. Iyi nzira idondaguwe muri BIP43. Nk’akarorero, iyo Wallet yubahiriza ingingo ngenderwako ya BIP84 (SegWit V0), urutonde rwoba rero `84'`;

**`m / intumbero' / Coin-ubwoko' /`** yerekana ubwoko bw'amahera y'ibanga. Ivyo bituma habaho itandukaniro rigaragara hagati y’amashami yihariye amafaranga y’ibanga rimwe n’ayo yihariye ayandi mu gice ca Coin Wallet. Urutonde rwerekeye Bitcoin ni **`0'`**;

`m / intumbero' / Coin-ubwoko' / konti' /` yerekana inomero ya konti. Ubwo burebure buratuma vyoroha gutandukanya no gutunganya Wallet mu makonti atandukanye. Izo konti ziharurwa guhera kuri `0'`. Imfunguruzo zagutse (`xpub`, `xprv`...) ziboneka kuri uru rwego rw'uburebure;

`m / intumbero' / Coin-ubwoko' / konti' / guhindura /` yerekana inzira. Inkuru yose nk'uko isobanurwa mu burebure bwa 3 ifise inzira zibiri mu burebure bwa 4: uruzitiro rw'inyuma n'uruzitiro rw'imbere (na rwo rwitwa "uguhinduka"). Uruzitiro rw'inyuma rukuramwo amaderesi agenewe gusangizwa abantu bose, ni ukuvuga amaderesi turonswa iyo dufyonda kuri "kwakira" muri porogarama yacu ya Wallet. Uruhererekane rw’imbere ruva ku maderesi atagenewe guhindurwa ku mugaragaro, ahanini guhindura amaderesi. Uruhererekane rw'inyuma rumenyekana n'urutonde `0` kandi uruhererekane rw'imbere rumenyekana n'urutonde `1`. Uzobona ko kuva muri ubwo burebure, tutagikora ivy’ugukura bikomeye, ahubwo dukora ivy’ugukura bisanzwe (nta apostrophe). Ni kubera ubu buryo dushobora gukura imfunguruzo zose z'abana muri `xpub` zazo;



- `m / intumbero' / Coin-ubwoko' / konti' / ihinduka / Address-index` yerekana gusa umubare wa Address yakira n'imfunguruzo zayo zibiri, kugira ngo itandukanye n'abavukanyi bayo ku burebure bumwe ku ishami rimwe. Nk’akarorero, Address ya mbere ikomotse ifise urutonde `0`, iya kabiri Address ifise urutonde `1`, n’ibindi...*


Nk'akarorero, nimba Address yanje yakira ifise inzira y'ugukomoka `m / 86' / 0' / 0' / 0 / 5`, turashobora gukuramwo amakuru akurikira:


- `86'` vyerekana ko turiko turakurikiza urugero rw'inkomoko rwa BIP86 (Taproot / SegWit V1);
- `0'` vyerekana ko ari Bitcoin Address;
- `0'` vyerekana ko turi ku nkuru ya mbere ya Wallet;
- `0` yerekana ko ari Address yo hanze;

`5` yerekana ko ari Address y’inyuma ya gatandatu y’iyi nkuru.


![](../../dictionnaire/assets/18.webp)