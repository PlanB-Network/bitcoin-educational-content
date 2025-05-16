---
term: KAZI YA Hash
---

Chaguo za kukokotoa za hisabati ambazo huchukua ingizo la ukubwa tofauti (unaoitwa ujumbe) na kutoa towe la saizi isiyobadilika (inayoitwa Hash, hashing, digest au alama ya vidole). Vitendaji vya Hash vinatumika sana katika kriptografia. Zinaonyesha sifa mahususi zinazozifanya zinafaa kutumika katika miktadha salama:


- Upinzani wa picha: lazima iwe vigumu sana kupata ujumbe unaozalisha Hash maalum, yaani, kupata picha ya awali $ m $ kwa Hash $ h $ vile $ h = H (m) $, ambapo $ H $ ni kazi ya Hash;
- Upinzani wa pili wa picha: ukipewa ujumbe $m_1$, lazima iwe vigumu sana kupata ujumbe mwingine $m_2$ (tofauti na $m_1$) kiasi kwamba $H(m_1) = H(m_2)$;
- Upinzani wa mgongano: lazima iwe vigumu sana kupata jumbe mbili tofauti $m_1$ na $m_2$ kiasi kwamba $H(m_1) = H(m_2)$;
- Upinzani wa tamper: mabadiliko madogo katika pembejeo lazima kusababisha mabadiliko makubwa na yasiyotabirika katika pato.


Katika muktadha wa Bitcoin, chaguo za kukokotoa za Hash hutumiwa kwa madhumuni kadhaa, ikiwa ni pamoja na utaratibu wa Proof-of-Work (*Proof-of-Work*), vitambulishi vya muamala, kizazi cha Address, ukokotoaji wa cheki, na uundaji wa miundo ya data kama vile miti ya Merkle. Kwa upande wa itifaki, Bitcoin hutumia kipekee chaguo za kukokotoa `SHA256d`, pia huitwa `HASH256`, ambayo inajumuisha `SHA256` Hash maradufu. `HASH256` pia hutumika katika kukokotoa hesabu fulani za hundi, hasa kwa vitufe vilivyopanuliwa (`xpub`, `xprv`...). Kwa upande wa Wallet, zifuatazo pia hutumiwa:


- `SHA256` rahisi kwa hesabu za misemo ya Mnemonic;
- `SHA512` ndani ya algoriti za `HMAC` na `PBKDF2` zinazotumika katika mchakato wa kupata pochi za kubainisha na za tabaka;
- `HASH160`, ambayo inaelezea matumizi mfululizo ya `SHA256` na `RIPEMD160`. `HASH160` hutumika katika mchakato wa kuzalisha anwani za kupokea (isipokuwa P2PK na P2TR) na katika kukokotoa alama za vidole za ufunguo wa mzazi kwa funguo zilizopanuliwa.


> ► *Kwa Kiingereza, inarejelewa kama "tendakazi ya Hash".*