---
term: SEED NODES
---

Staatiline avalike Bitcoin'i sõlmede nimekiri, mis on otse integreeritud Bitcoin Core'i lähtekoodi (`bitcoin/src/chainparamsseeds.h`). See nimekiri toimib ühenduspunktina uutele Bitcoin'i sõlmedele võrguga liitumisel, kuid seda kasutatakse ainult juhul, kui DNS seemned ei anna nende päringule 60 sekundi jooksul vastust. Sellisel juhul ühendub uus Bitcoin'i sõlm nende seemnesõlmedega, et luua võrguga esmane ühendus ja taotleda teiste sõlmede IP-aadresse. Lõppeesmärk on hankida vajalik informatsioon Algse Ploki Allalaadimise (IBD) sooritamiseks ja sünkroniseerimiseks kõige rohkem tööd kogunud ahelaga. Seemnesõlmede nimekiri sisaldab peaaegu 1000 sõlme, mis on identifitseeritud vastavalt BIP155 poolt kehtestatud standardile. Seega esindavad seemnesõlmed kolmandat ühenduse loomise meetodit võrku Bitcoin'i sõlme jaoks, pärast võimalikku `peers.dat` faili kasutamist, mille on loonud sõlm ise, ja DNS seemnete taotlemist.

> ► *Märkus, seemnesõlmi ei tohiks segi ajada "DNS seemnetega", mis on teine meetod ühenduste loomiseks.*