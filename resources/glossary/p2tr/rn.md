---
term: P2TR
---

P2TR ihagarariye *Pay to Taproot*, ariyo nzira y’inyandiko ikoreshwa mu gushinga ivyangombwa vyo gukoresha amahera kuri UTXO (Igisubizo c’Ibikorwa Bitakoreshejwe). Yatangujwe n’ugushirwa mu ngiro kwa Taproot mu kwezi kwa 11/2021. P2TR ikoresha umurongo wa Schnorr mu gukoranya imfunguruzo z’ubuhinga bwa none, hamwe n’ibiti vya Merkle vy’inyandiko zindi, zizwi nka MAST (*Igiti c’inyandiko zindi za Merkelized*). Mu buryo butandukanye n’ibikorwa vya kera aho ivy’ugukoresha amahera bigaragazwa ku mugaragaro (rimwe na rimwe mu gihe co kwakira, rimwe na rimwe mu gihe co gukoresha amahera), P2TR iremeza guhisha inyandiko zikomeye inyuma y’urufunguzo rumwe ruboneka rwa bose.


Mu buryo bw’ubuhinga, inyandiko ya P2TR ifunga bitcoins ku rufunguzo rwa bose rwihariye rwa Schnorr, rwerekanwa na $K$. Ariko rero, uru rufunguzo $K$ mu vy'ukuri ni umugwi w'urufunguzo rwa bose $P$ n'urufunguzo rwa bose $M$, rwa nyuma rukabarwa ruvuye kuri Merkle Root y'urutonde rwa `scriptPubKey`. Ivyo bice vy’amahera vyugarijwe n’inyandiko ya P2TR bishobora gukoreshwa mu buryo bubiri butandukanye: haba mu gutangaza umukono w’urufunguzo rwa bose $P$, canke mu guhazwa n’imwe mu nyandiko ziri muri Merkle Tree. Ihitamwo rya mbere ryitwa "*inzira y'urufunguzo*" n'irya kabiri "*inzira y'inyandiko*".


Gutyo, P2TR iremesha abakoresha kohereza ama bitcoins haba ku rufunguzo rwa bose canke ku nyandiko nyinshi bahisemwo. Ikindi ciza c’iyi nyandiko ni uko, naho hari uburyo bwinshi bwo gukoresha igisohoka ca P2TR, iyo ikoreshwa yonyene ni yo ikeneye guhishurirwa igihe co gukoresha, bikaba bituma ubundi buryo butakoreshwa buguma ari ubw’ibanga. P2TR ni verisiyo 1 SegWit isohoka, bisobanura ko imikono y'inyungu za P2TR ibikwa mu cabona c'ibikorwa, atari mu `scriptSig`. Aderesi za P2TR zikoresha ubuhinga bwa `Bech32m` kandi zitangura na `bc1p`.