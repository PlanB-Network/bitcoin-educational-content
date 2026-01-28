---
term: Output script descriptors
definition: Amagambo ateرتe yerekana ibisohokera muri script n'amakuru yo kugarura ikigega.
---

Insobanuro z'inyandiko y'isohoka, canke insobanuro gusa, ni imvugo zitunganijwe zidondora neza inyandiko y'isohoka (`scriptPubKey`) kandi zitanga amakuru yose akenewe kugira ngo ukurikirane ibikorwa vy'inyandiko canke biva ku nyandiko yihariye. Ivyo bisobanuro bifasha gucunga neza imfunguruzo mu bikoresho vya HD biciye mu ndondoro isanzwe y’imiterere n’ubwoko bw’amaderesi akoreshwa.


Inyungu nyamukuru y’abadondora iri mu bushobozi bwabo bwo gushiramwo amakuru yose ahambaye yo gusubizaho Wallet mu murongo umwe (ukwongerako ijambo ry’ugusubizaho). Mu kubika Descriptor n’amajambo ahuye na Mnemonic, birashoboka ko udasubizaho gusa imfunguruzo z’ibanga ariko kandi n’imiterere nyayo ya Wallet n’imirongo y’inyandiko ijana. Nkako, gusubirana Wallet ntibisaba gusa kumenya seed ya mbere ariko kandi bisaba n'ibimenyetso vyihariye vy'ugukura kw'abana babiri, hamwe n'`xpub` y'ikintu cose ku bijanye na Multisig Wallet. Mbere, vyiyumvirwa ko ayo makuru azwi na bose ata co avuze. Ariko rero, n’uguhinduka kw’inyandiko be n’uguseruka kw’imiterere ikomeye cane, ayo makuru yoshobora kugora gusobanura, gutyo ayo makuru agahinduka amakuru y’ibanga n’ay’inguvu z’abantu. Gukoresha ibisobanuro vyorosha cane igikorwa: birahagije kumenya amajambo (amajambo) yo gusubizaho n’ijambo Descriptor rihuye n’iryo kugira ngo umuntu asubizeho vyose mu buryo bwizewe kandi butekanye.


Descriptor igizwe n’ama Elements menshi:


- Inyandiko ikora nka `pk` (Ishura-ku-rufunguzo rwa Pub), `pkh` (Ishura-ku-rufunguzo rwa Pub-Hash), `wpkh` (Ishura-ku-Icabona-Urufunguzo rwa Pub-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Ishura-ku-Icabona-Itangazo), `W-S). `multi` (Imikono myinshi), na `sortedmulti` (Imikono myinshi ifise imfunguruzo zitoranijwe);
- Inzira z'inkomoko, nk'akarorero, `[d34db33f/44h/0h/0h]` zigaragaza inzira y'inkomoko n'urutoke rw'urufunguzo rw'umukuru rwihariye;
- Imfunguruzo mu buryo butandukanye nk'imfunguruzo za bose z'icumi na zitandatu canke imfunguruzo za bose zagutse (`xpub`);
- Igiharuro c'igenzura, kibanzirizwa na Hash, kugira ngo hasuzumwe ubutungane bwa Descriptor.


Nk’akarorero, Descriptor ku P2WPKH Wallet yoshobora gusa n’iyi:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/#jy0l7n
r4
```

Muri iyi Descriptor, igikorwa c'inkomoko `wpkh` kigaragaza ubwoko bw'inyandiko ya Pay-to-Witness-Public-Key-Hash. Ikurikirwa n'inzira y'inkomoko irimwo:


- `cdeab12f`: urutoke rw'urufunguzo rwa mbere;
- `84h`: bisobanura gukoresha intumbero ya BIP84, igenewe amaderesi ya SegWit v0;
- `0h`: ivyo bikaba vyerekana ko ari amafaranga y’i BTC kuri Mainnet;
- `0h`: yerekeza ku nomero ya konti yihariye ikoreshwa muri Wallet.


Descriptor kandi irimwo urufunguzo rwa bose rwagutse rukoreshwa muri iyi Wallet:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Inyuma, ikimenyetso `/<0;1>/*` kigaragaza ko Descriptor ishobora generate aderesi kuva ku ruhererekane rw'inyuma (`0`) n'urwo mu mutima (`1`), n'ikimenyetso (`*`) cemerera gukuraho urutonde rw'amaderesi menshi mu buryo bushobora guhindurwa kuri porogarama ya kera-2.


Ubwa nyuma, `#jy0l7nr4` igereranya umubare w'igenzura kugira ngo ugenzure ubutungane bwa Descriptor.