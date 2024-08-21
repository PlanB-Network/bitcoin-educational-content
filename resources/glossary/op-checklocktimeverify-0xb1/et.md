---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Muudab tehingu kehtetuks, kui kõik need tingimused ei ole täidetud:
* Stack ei ole tühi;
* Stacki tipus olev väärtus on suurem või võrdne `0`-ga;
* Ajaluku tüüp on sama nii `nLockTime` väljal kui ka stacki tipus oleva väärtuse puhul (reaalne aeg või ploki number);
* Sisendi `nSequence` väli ei ole võrdne `0xffffffff`-ga;
* Stacki tipus olev väärtus on suurem või võrdne tehingu `nLockTime` välja väärtusega.

Kui ükskõik milline neist tingimustest ei ole täidetud, ei saa skripti, mis sisaldab `OP_CHECKLOCKTIMEVERIFY`, rahuldada. Kui kõik need tingimused on kehtivad, siis `OP_CHECKLOCKTIMEVERIFY` toimib nagu `OP_NOP`, mis tähendab, et see ei tee skriptiga midagi. See on justkui kadunud. `OP_CHECKLOCKTIMEVERIFY` seab seega aja piirangu UTXO kulutamisele, mille turvamiseks seda skripti kasutatakse. See võib seda teha kas Unixi aja kuupäeva või ploki numbri kujul. Selleks piirab see võimalikke väärtusi tehingu `nLockTime` väljal, mis kulutab seda, ja see `nLockTime` väli ise piirab, millal tehingut saab plokki lisada.

> ► *See operaator on asendus `OP_NOP`-ile. See asetati `OP_NOP2` peale. Seda nimetatakse sageli lühendi "CLTV" järgi. Pane tähele, et `OP_CLTV` ei tohiks segi ajada tehingu `nLockTime` väljaga. Esimene kasutab teist, kuid nende olemused ja toimingud on erinevad.*