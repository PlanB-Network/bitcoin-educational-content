---
term: BIP0044
definition: Standard isobanura imiterere yuzuye y'inzira za derivation ku mawallet ya HD purpose, coin_type, account, change na address_index.
---

Iciyumviro co gushiramwo uburyo busanzwe bwo gukuraho amakuru ku ma wallets ya HD. BIP44 yubakiye ku ngingo ngenderwako zashinzwe muri BIP32 ku bijanye n’ugukuraho urufunguzo no muri BIP43 ku bijanye no gukoresha umurima w’intumbero.

Isobanura imiterere y'inkomoko y'urugero rutanu: `m / intumbero' / ubwoko_ bw'igiceri' / konti' / guhindura / aderesi_index`.

Aha niho hari ido n’ido ry’uburebure buri bumwe:


- `m /` yerekana urufunguzo rw'ibanga. Ni ikintu kidasanzwe ku Wallet kandi ntigishobora kugira abavukanyi mu burebure bumwe. Urufunguzo nyamukuru rukomoka ata guca ku ruhande kuri seed ya Wallet;
- `m / purpose' /` yerekana intumbero y'inkomoko ifasha kumenya urugero rukurikira. Iyi nzira idondaguwe muri BIP43. Nk'akarorero, iyo Wallet ikurikije urugero rwa BIP84 (SegWit V0), urutonde rwoba rero `84'`;

`m / intumbero' / Coin-ubwoko' /` yerekana ubwoko bw'amahera y'ibanga. Ivyo bituma habaho itandukaniro rigaragara hagati y’amashami yihariye ku mafaranga amwe y’ibanga n’ayo yihariye ayandi mafaranga y’ibanga mu ma Coin Wallet menshi. Urutonde rwerekeye Bitcoin ni `0'`;


- `m / intumbero' / Coin-ubwoko' / konti' /` yerekana inomero ya konti. Ubwo burebure buratuma umuntu ashobora gutandukanya no gutunganya neza Wallet mu makonti atandukanye. Izo konti ziharurwa guhera kuri `0'`. Imfunguruzo zagutse (`xpub`, `xprv`...) ziboneka muri ubu burebure;
- `m / intumbero' / Coin-ubwoko' / konti' / guhindura /` yerekana uruzitiro. Inkuru yose nk'uko isobanuwe mu burebure bwa 3 ifise iminyororo ibiri mu burebure bwa 4: urudodo rw'inyuma n'urudodo rw'imbere (na rwo nyene rwitwa "uguhinduka"). Uruhererekane rw'inyuma rukuramwo amaderesi agenewe kumenyeshwa abantu bose, ni ukuvuga amaderesi twahawe iyo dufyonda kuri "kwakira" muri porogarama yacu ya Wallet. Uruhererekane rw'imbere ruva ku maderesi atagenewe guhindurwa ku mugaragaro, ni ukuvuga, ahanini guhindura amaderesi. Uruhererekane rw'inyuma rumenyekana n'urutonde `0` kandi uruhererekane rw'imbere rumenyekana n'urutonde `1`. Uzobona ko kuva muri ubwo burebure, tutagikora ivy’ugukura bikomeye, ahubwo dukora ivy’ugukura bisanzwe (nta apostrophe). Ni kubera ubu buryo dushobora gukura imfunguruzo zose z'abana muri `xpub` zabo;
- `m / intumbero' / Coin-ubwoko' / konti' / ihinduka / Address-index` yerekana gusa umubare wa Address yakira n'imfunguruzo zayo zibiri, kugira ngo itandukanye n'abavukanyi bayo ku burebure bumwe ku ishami rimwe. Nk’akarorero, Address ya mbere ikomotse ifise urutonde `0`, iya kabiri Address ifise urutonde `1`, n’ibindi...*

Nk'akarorero, nimba Address yanje ifise inzira y'ugukomoka `m / 86' / 0' / 0' / 0 / 5`, turashobora gukuramwo amakuru akurikira:


- `86'` vyerekana ko turiko turakurikiza urugero rw'inkomoko rwa BIP86 (Taproot canke SegWitV1);
- `0'` vyerekana ko ari Bitcoin Address;
- `0'` vyerekana ko turi ku nkuru ya mbere ya Wallet;
- `0` yerekana ko ari Address yo hanze;

`5` yerekana ko ari Address y’inyuma ya gatandatu y’iyi nkuru.