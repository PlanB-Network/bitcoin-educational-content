---
term: P2TR
---

P2TR inawakilisha *Lipa kwa Taproot*, ambayo ni muundo wa kawaida wa hati unaotumiwa kuweka masharti ya matumizi kwenye UTXO (Pato la Muamala Usiotumika). Ilianzishwa kwa kutekelezwa kwa Taproot mnamo Novemba 2021. P2TR hutumia itifaki ya Schnorr kujumlisha funguo za kriptografia, pamoja na miti ya Merkle kwa hati mbadala, inayojulikana kama MAST (*Mti wa Hati Mbadala wa Merkelized*). Tofauti na shughuli za kawaida ambapo masharti ya matumizi yanafichuliwa hadharani (wakati mwingine wakati wa kupokea, wakati mwingine wakati wa matumizi), P2TR inaruhusu kufichwa kwa hati ngumu nyuma ya ufunguo mmoja unaoonekana wa umma.


Kitaalam, hati ya P2TR hufunga bitcoins kwenye ufunguo wa kipekee wa umma wa Schnorr, unaoashiria kama $K$. Hata hivyo, ufunguo huu $K$ kwa hakika ni jumla ya ufunguo wa umma $P$ na ufunguo wa umma $M$, wa mwisho ukikokotwa kutoka Merkle Root ya orodha ya `scriptPubKey`. Bitcoins zilizofungwa na hati ya P2TR zinaweza kutumika kwa njia mbili tofauti: ama kwa kuchapisha saini ya ufunguo wa umma $ P $, au kwa kukidhi mojawapo ya maandiko yaliyomo kwenye Merkle Tree. Chaguo la kwanza linaitwa "* njia ya ufunguo *" na ya pili "* njia ya hati *".


Kwa hivyo, P2TR inaruhusu watumiaji kutuma bitcoins ama kwa ufunguo wa umma au kwa hati nyingi za chaguo lao. Faida nyingine ya hati hii ni kwamba, ingawa kuna njia nyingi za kutumia pato la P2TR, ni ile inayotumika tu inayohitaji kufichuliwa wakati wa matumizi, kuruhusu njia mbadala zisizotumiwa kubaki za faragha. P2TR ni toleo la 1 la matokeo ya SegWit, kumaanisha kuwa sahihi za ingizo za P2TR huhifadhiwa katika ushuhuda wa muamala, na si katika `scriptSig`. Anwani za P2TR hutumia usimbaji wa `Bech32m` na kuanza na `bc1p`.