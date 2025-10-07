---
term: HTLC
---

Bihagarariye "*Igihe c'Igihe Contract*". Ubu ni uburyo bwa Smart contract bukoreshwa cane cane ku Muravyo. Rimwe na rimwe kandi riboneka mu guhinduranya atome. Mu bisanzwe, HTLC ituma amahera yoherezwa bishingiye ku guhishurirwa kw’ibanga, kandi ikaba irimwo n’igihe co kurinda amahera y’uwayohereje iyo habaye ugucuruzwa kwananiwe.


Ku Lightning, HTLC iragufasha kohereza bitcoins ku node udafise umurongo utaziguye, mu guca mu mihora myinshi, ataco ukeneye kwizigira mu nzira. Ukwishura hagati y’urudodo rumwe rumwe bishingiye ku gutanga ishusho y’imbere (ibanga, iyo rikoreshejwe, rihuye n’agaciro bemeranije). Iyo uwuronka amahera ya nyuma atanga iyo shusho y’imbere, arashobora gusaba amahera, kandi birashoboka ko buri nzira yo hagati ishobora gusaba amahera mu buryo bw’uruzitiro.


Nk’akarorero, iyo Alice ashaka kohereza BTC 1 kuri David, ariko atagira umurongo utaziguye na we, ategerezwa guca kuri Bob na Carol, bafise umurongo wo kwishurana. Ehe ingene ugucuruza bigenda:




- David atanga Alice n’umuravyo Invoice. Ivyo birimwo Hash $h$ y’ibanga $s$ (ishusho y’imbere) Dawidi wenyene azi. Rero dufise: $h = \umwandiko{Hash}(s)$ ;
- Alice arema HTLC na Bob, uwo na we akamurungikira BTC 1 ku gihe Bob yomuha ibanga $s$ (ishusho y’imbere) ihuye na Hash $h$ ;
- Bob akora HTLC na Carol, nawe akamurungikira BTC 1 ku bijanye n’uko yotanga iryo banga nyene $s$ ;
- Carol akora HTLC na David, uwo nawe akamuha uwundi BTC 1 iyo ahishuriye $s$ preimage;
- David ahishurira Carol $s$ (ivyo wenyene yari azi) kugira ngo aronke BTC 1. Carol ubu ashobora gukoresha $s$ kugira aronke BTC kuri Bob. Kandi Bob, ubu azi $s$, na we nyene akora kuri Alice.


Ubwa nyuma, Alice yarungikiye David BTC 1 biciye kuri Bob na Carol (igikorwa kitagira aho kigarukira kuri abo ba nyuma), ata n’umwe ategerezwa kwizigirana, kuko vyose bicungiwe mu buryo bw’uruzi n’ivyo aba HTLC bameze.


HTLCs rero zituma habaho ivyo bita "atome" exchanges: canke iyo nzira y'uguhindura iraheza ikaroranirwa yose, canke ikananirwa, amahera agasubirwamwo. Ivyo bituma haba umutekano w’amafaranga, mbere no hagati y’abantu benshi ataco bakeneye kwizigirana.