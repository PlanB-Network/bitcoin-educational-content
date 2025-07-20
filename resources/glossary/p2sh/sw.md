---
term: P2SH
---

P2SH inawakilisha *Lipa kwa Hati Hash*. Ni muundo wa hati wa kawaida unaotumiwa kuweka masharti ya matumizi kwenye UTXO. Tofauti na hati za P2PK na P2PKH, ambapo masharti ya matumizi yamefafanuliwa mapema, P2SH inaruhusu ujumuishaji wa masharti ya matumizi holela na utendakazi wa ziada ndani ya hati ya muamala.


Kitaalam, katika muamala wa P2SH, `scriptPubKey` ina kriptografia Hash ya `redeemscript`, badala ya masharti dhahiri ya matumizi. Hash hii inapatikana kwa kutumia `SHA256` Hash. Wakati wa kutuma bitcoins kwa P2SH Address, msingi wa `redeemscript` haujafunuliwa. Hash yake pekee ndiyo imejumuishwa katika shughuli hiyo. Anwani za P2SH zimesimbwa katika `Base58Check` na kuanza na nambari `3`. Mpokeaji anapotaka kutumia bitcoins zilizopokewa, lazima atoe `redeemscript` inayolingana na Hash iliyopo katika `scriptPubKey`, pamoja na data muhimu ili kukidhi masharti ya `redeemscript` hii. Kwa mfano, katika hati ya saini nyingi za P2SH, hati inaweza kuhitaji saini kutoka kwa funguo nyingi za kibinafsi.


Utumiaji wa P2SH hutoa unyumbulifu zaidi, kwani huruhusu ujenzi wa hati kiholela bila mtumaji kujua maelezo. P2SH ilianzishwa mwaka 2012 na BIP16.