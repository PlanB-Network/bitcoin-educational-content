---
term: Ibendera rya SIGHASH

---

Igiharuro kiri mu gikorwa ca Bitcoin kigaragaza ibice vy’igikorwa (ivyo kwinjira n’ivyo gusohoka) bipfutse n’umukono ujana, gutyo bikaba bidahinduka. Ibendera rya SigHash ni byte yongewe ku mukono wa digitale w'inyungu yose. Rero, uguhitamwo SigHash Flag biragira ico bikoze ku bice vy’ugucuruza bifunzwe n’umukono kandi bishobora guhindurwa inyuma. Ubwo buryo buratuma abasinye bakora neza kandi ata nkomanzi amakuru y’ibikorwa vy’ubudandaji bishingiye ku ciyumviro c’uwushizeko umukono. Hariho amabendera atatu nyamukuru ya SigHash:



- `SIGHASH_ALL` (`0x01`): Umukono ukoreshwa ku vyinjizwa vyose n’ibisohoka vyose vy’ugucuruza, gutyo bikabifunga vyose;



- `SIGHASH_NONE` (`0x02`): Umukono ukoreshwa ku vyinjizwa vyose ariko nta na kimwe mu bisohoka, bikaba vyemerera ibisohoka guhindurwa inyuma y'umukono;



- `SIGHASH_SINGLE` (`0x03`): Umukono upfuka ivyinjijwe vyose n'isohoka rimwe gusa rihuye n'urutonde rw'ivyinjijwe vyashizweko umukono.


Uretse ayo mabendera atatu ya SigHash, umuhinduzi `SIGHASH_ANYONECANPAY` (`0x80`) ashobora gufatanywa na buri bwoko bwa kera. Iyo uwo muhinduzi akoreshejwe, igice gusa c’ivyo bishizwemwo ni co gishirwako umukono, ibindi bikasigara vyuguruye kugira ngo bihindurwe. Aha niho hari imigwi iriho n'umuhinduzi:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Umukono ukoreshwa ku nkuru imwe mu gihe upfutse ibisohoka vyose vy'ugucuruza;



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Umukono upfuka ikintu kimwe co kwinjiza, ataco wiyemeje ku gisohoka;



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Umukono ukoreshwa ku yinjijwe imwe kandi gusa ku gisohoka gifise urutonde rumwe n'urwo rwinjijwe.


> ► *Ijambo rimwe rimwe rikoreshwa kuri "SigHash" ni "Ubwoko bw'Isinya Hash".*