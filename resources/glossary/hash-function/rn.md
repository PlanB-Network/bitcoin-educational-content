---
term: Hash IMIKORO
---

Igikorwa kijanye n’imibare gifata inyungu y’ingero ihinduka (yitwa ubutumwa) kigatanga inyungu y’ingero idahinduka (yitwa Hash, hashing, digest, canke urutoke). Ibikorwa vya Hash ni ibintu vya kera bikoreshwa cane mu gukora amakuru y’ibanga. Birerekana ibintu vyihariye bituma bibereye gukoreshwa mu bibanza bitekanye:

**Uguhangana n’ishusho y’imbere**: bitegerezwa kuba bigoye cane kuronka ubutumwa butanga Hash yihariye, ni ukuvuga, kuronka ishusho y’imbere $m$ ku Hash $h$ ku buryo $h = H(m)$, aho $H$ ari igikorwa ca Hash;

**Uguhangana kwa kabiri kw'ishusho y'imbere:** guhabwa ubutumwa $m_1$, bitegerezwa kuba bigoye cane kuronka ubundi butumwa $m_2$ (butandukanye na $m_1$) ku buryo $H(m_1) = H(m_2)$;

**Uguhangana n’ugutomboka**: bitegerezwa kuba bigoye cane kuronka ubutumwa bubiri butandukanye $m_1$ na $m_2$ ku buryo $H(m_1) = H(m_2)$;

**Tamper resistance:** amahinduka mato mato mu vyo winjiza ategerezwa gutuma haba amahinduka akomeye kandi atamenyekana mu vyo usohora.


Mu bijanye na Bitcoin, ibikorwa vya Hash bikoreshwa mu ntumbero nyinshi, harimwo uburyo bwa Proof-of-Work (*Proof-of-Work*), ibimenyetso vy’ibikorwa, uguhingura Address, uguharura umubare w’igenzura, no kurema imiterere y’amakuru nk’ibiti vya Merkle. Ku ruhande rw'amasezerano, Bitcoin ikoresha gusa igikorwa ca `SHA256d`, citwa kandi `HASH256`, gifise `SHA256` Hash zibiri. `HASH256` ikoreshwa kandi mu kubara ibiharuro bimwe bimwe, cane cane ku mfunguruzo zagutse (`xpub`, `xprv`...). Ku ruhande rwa Wallet, ibi bikurikira na vyo nyene birakoreshwa:


- `SHA256` yoroshe ku biharuro vy'amajambo ya Mnemonic;
- `SHA512` mu `HMAC` na `PBKDF2` ubuhinga bukoreshwa mu nzira yo gukuraho ama wallets y'ivy'imbere n'ivy'imbere;
- `HASH160`, idondora ikoreshwa rikurikirana rya `SHA256` na `RIPEMD160`. `HASH160` ikoreshwa mu nzira yo gutanga amaderesi y'ukwakira (uretse P2PK na P2TR) no mu kubara ibimenyetso vy'intoke vy'urufunguzo rw'umuvyeyi ku rufunguzo rwagutse.


> ► *Mu congereza, vyitwa "igikorwa ca Hash".*