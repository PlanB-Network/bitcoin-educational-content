---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Muudab tehingu kehtetuks, kui kõik need tingimused ei ole täidetud:


- Korstnat ei ole tühi;
- Väärtus virna tipus on suurem või võrdne `0`;
- Ajaluku tüüp on sama, mis väljal `nLockTime` ja virna tipus oleval väärtusel (reaalajas või plokinumber);
- Sisendi `nSequence` väli ei ole võrdne `0xffffffffffff`;
- Väärtus virna tipus on suurem või võrdne tehingu `nLockTime` välja väärtusega.

Kui mõni neist tingimustest ei ole täidetud, ei saa skripti "OP_CHECKLOCKTIMEVERIFY" sisaldavat käsku täita. Kui kõik need tingimused kehtivad, siis toimib `OP_CHECKLOCKTIMEVERIFY` nagu `OP_NOP`, mis tähendab, et see ei tee skriptile mingit toimingut. See justkui kaob. `OP_CHECKLOCKTIMEVERIFY` seab seega ajalise piirangu UTXO kulutamisele, mis on tagatud seda sisaldava skriptiga. See võib seda teha kas Unixi ajadatumi või plokinumbri kujul. Selleks piirab see tehingu kulutamise lahtri `nLockTime` võimalikke väärtusi ja see `nLockTime` väli ise piirab, millal tehingut saab plokki lisada.

> ► *See opkood on asenduseks koodile `OP_NOP`. See paigutati `OP_NOP2` peale. Tihti nimetatakse seda lühendiga "CLTV". Märkus: `OP_CLTV` ei tohi segi ajada tehingu väljaga `nLockTime`. Esimene kasutab viimast, kuid nende olemus ja toimingud on erinevad.*