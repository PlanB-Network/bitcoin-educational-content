---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Muudab tehingu kehtetuks, kui täheldatakse ühtegi neist omadustest:
* Stack on tühi;
* Stacki tipus olev väärtus on väiksem kui `0`;
* Stacki tipus oleva väärtuse keelulipp on määratlemata ja; Tehingu versioon on väiksem kui `2` või; Sisendi `nSequence` välja keelulipp on seatud või; Ajaluku tüüp ei ühti `nSequence` välja ja stacki tipus oleva väärtuse vahel (reaalne aeg või plokkide arv) või; Stacki tipus olev väärtus on suurem kui sisendi `nSequence` välja väärtus.

Kui täheldatakse üht või mitut neist omadustest, ei saa skripti, mis sisaldab `OP_CHECKSEQUENCEVERIFY`, rahuldada. Kui kõik tingimused on kehtivad, siis toimib `OP_CHECKSEQUENCEVERIFY` nagu `OP_NOP`, mis tähendab, et see ei tee skriptiga mingit toimingut. Justkui see kaoks. Seega kehtestab `OP_CHECKSEQUENCEVERIFY` suhtelise ajapiirangu UTXO kulutamisele, mille turvamiseks seda skripti kasutatakse. See võib seda teha kas reaalse aja vormis või plokkide arvuna. Selleks piirab see võimalikke väärtusi sisendi `nSequence` välja jaoks, mis kulutab seda, ning see `nSequence` väli ise piirab, millal tehingut, mis sisaldab seda sisendit, saab plokki lisada.

> ► *See operaator on asendus `OP_NOP`-ile. See asetati `OP_NOP3` peale. Seda nimetatakse sageli lühendi "CSV" järgi. Pane tähele, et `OP_CSV` ei tohiks segi ajada tehingu `nSequence` väljaga. Esimene kasutab teist, kuid nende olemused ja toimingud on erinevad.*