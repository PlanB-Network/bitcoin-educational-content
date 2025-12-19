---
term: URUPFUZO RWAGUYE
---

Urutonde rw'inyuguti rufatanya urufunguzo (rwa bose canke rw'ibanga), chain code ijana narwo, n'urutonde rw'amakuru y'imbere. Urufunguzo rwagutse rukoranya Elements yose ikenewe kugira ngo umuntu akureho urufunguzo rw'abana mu kimenyetso kimwe. Bikoreshwa mu bikoresho vy’ubuhinga n’ivy’ubuhinga kandi bishobora kuba vy’ubwoko bubiri: urufunguzo rwa bose rwagutse (rukoreshwa mu gukuraho urufunguzo rwa bose rw’abana) canke urufunguzo rw’ibanga rwagutse (rukoreshwa mu gukuraho urufunguzo rw’ibanga rw’abana n’urwa bose). Urufunguzo rwagutse rero rurimwo amakuru atandukanye, adondowe muri BIP32, mu buryo bukurikirana:

**Intango:** `prv` na `pub` ni HRP (Igice Gisomwa n'Umuntu) kigaragaza nimba ari urufunguzo rw'ibanga rwagutse (`prv`) canke urufunguzo rwa bose rwagutse (`pub`). Urudome rwa mbere rw'intango rwerekana verisiyo y'urufunguzo rwagutse: `x` ku Iragi canke SegWit V1 kuri Bitcoin, `t` ku Iragi canke SegWit V1 kuri Bitcoin Testnet, `y` ku SegWit y'Ikigo kuri Bitcoin, `u` ku G`3-4 y'Ikigo, `W` ku G`3-4. V0 kuri Bitcoin, `v` kuri SegWit V0 kuri Bitcoin Testnet.


- Uburebure, bugaragaza umubare w’ibikomoka ku rufunguzo rwa mbere kugira ngo bishike ku rufunguzo rwagutse;
- Urutoke rw’umuvyeyi. Ivyo bigereranya bytes 4 za mbere za `HASH160` z'urufunguzo rwa bose rw'umuvyeyi;
- Index. Uwo ni wo mubare w’ababiri mu bavukanyi bawo aho urufunguzo rwagutse rukomoka;

*Ivyo chain code;*


- Byte y'ugushiramwo iyo ari urufunguzo rw'ibanga `0x00`;
- Urufunguzo rw’ibanga canke rwa bose;
- Igitigiri c'igenzura. Igereranya bytes 4 za mbere za `HASH256` z'urufunguzo rwagutse rwasigaye.


Mu bikorwa, urufunguzo rwa bose rwagutse rukoreshwa kugira ngo generate ironke amaderesi no kugira ngo yihweze ibikorwa vya konti ata gushikiriza urufunguzo rw’ibanga rujanye n’ivyo. Ivyo bishobora gutuma, nk'akarorero, hakorwa ico bita "watch-only" Wallet. Ariko rero, birahambaye kumenya ko urufunguzo rwa bose rwagutse ari amakuru y’agaciro ku bwite bw’uwurukoresha, kuko gutangazwa kwarwo bishobora gutuma abandi bantu bashobora gukurikirana amafaranga akoreshwa no kubona amahera asigaye kuri konti ijana.