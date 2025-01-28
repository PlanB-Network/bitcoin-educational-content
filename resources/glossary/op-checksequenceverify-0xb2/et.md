---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Teeb tehingu kehtetuks, kui mõni neist omadustest on täheldatud:


- Korstnat on tühi;
- Väärtus virna tipus on väiksem kui `0`;
- Tehingu versioon on väiksem kui `2` või; sisendi `nSequence` väljal on keelatud või; timelocki tüüp ei ole sama kui `nSequence` väljal ja virna tipus olev väärtus (reaalajas või plokkide arv) või; virna tipus olev väärtus on suurem kui sisendi `nSequence` väljal olev väärtus.

Kui täheldatakse ühte või mitut neist omadustest, ei saa käsikirja "OP_CHECKSEQUENCEVERIFY" sisaldavat käsikirja täita. Kui kõik tingimused kehtivad, siis toimib `OP_CHECKSEQUENCEVERIFY` nagu `OP_NOP`, mis tähendab, et see ei tee skriptiga ühtegi toimingut. See justkui kaob. `OP_CHECKSEQUENCEVERIFY` seab seega suhtelise ajalise piirangu UTXO kulutamisele, mis on tagatud seda sisaldava skriptiga. See võib seda teha kas reaalajas või plokkide arvuna. Selleks piirab ta sisendi `nSequence` väljale võimalikke väärtusi, mida ta kulutab, ja see `nSequence` väli ise piirab, millal seda sisendit sisaldav tehing saab plokki lisada.

> ► *See opkood on asenduseks koodile `OP_NOP`. See paigutati `OP_NOP3` peale. Tihti viidatakse sellele akronüümiga "CSV". Pange tähele, `OP_CSV` ei tohi segi ajada tehingu väljaga `nSequence`. Esimene kasutab viimast, kuid nende olemus ja toimingud on erinevad.*