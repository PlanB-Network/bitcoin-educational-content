---
term: OP_CHECKSIGADD (0XBA)

---

Gukuraho agaciro gatatu ka mbere mu kirundo: `urufunguzo rwa bose`, `CScriptNum` `n`, na `umukono`. Iyo umukono utari umurongo w'ubusa kandi udafise akamaro, inyandiko irahera n'ikosa. Niba umukono ari mwiza canke ari ubusa (`OP_0`), ibintu bibiri birashikirizwa:


- Niba umukono ari umurongo w'ubusa: `CScriptNum` ifise agaciro ka `n` irasunikwa ku kirundo, maze ugushirwa mu ngiro birabandanya;
- Niba umukono utari umurongo w'ubusa kandi uguma ukora: `CScriptNum` ifise agaciro ka `n + 1` irasunikwa ku kirundo, maze ugushirwa mu ngiro birabandanya.

Kugira ngo vyorohe, `OP_CHECKSIGADD` ikora igikorwa kimeze nka `OP_CHECKSIG`, ariko aho gusunika ukuri canke ikinyoma ku kirundo, yongerako `1` ku gaciro ka kabiri kari hejuru y'ikirundo iyo umukono ufise akamaro, canke isiga ako gaciro katahindutse iyo umukono ugereranya umurongo w'ubusa. `OP_CHECKSIGADD` iremesha guhingura amategeko y'imikono myinshi muri Tapscript nk'uko biri muri `OP_CHECKMULTISIG` na `OP_CHECKMULTISIGVERIFY` ariko mu buryo bushobora kugenzurwa, bisobanura ko ikuraho uburyo bwo kurondera mu kugenzura multisig ya kera kandi gutyo igatuma igenzura ryihuta mu gihe igabanya umuzigo w'ibikorwa vya C. Iyi opcode yongewe muri Tapscript gusa kubera ivyo Taproot ikeneye.