---
term: P2SH-P2WSH
---

P2SH-P2WSH tähistab *Maksa Skripti Räsi - Maksa Tunnistaja Skripti Räsi*. See on standardne skriptimudel, mida kasutatakse kulutamistingimuste seadmiseks UTXO-le, mida tuntakse ka kui "Pesastatud SegWit".

P2SH-P2WSH tutvustati SegWiti rakendamisega augustis 2017. See skript kirjeldab P2WSH-d, mis on mähitud P2SH sisse. See lukustab bitcoine skripti räsi põhjal. Erinevus klassikalisest P2WSH-st on see, et skript on mähitud klassikalise P2SH `redeemScript`i.

See skript loodi SegWiti käivitamisel selle vastuvõtu hõlbustamiseks. See võimaldab kasutada seda uut standardit isegi teenustega või rahakottidega, mis ei ole veel SegWitiga natiivselt ühilduvad. Tänapäeval ei ole seetõttu enam väga asjakohane kasutada selliseid mähitud SegWiti skripte, kuna enamik rahakotte on rakendanud natiivse SegWiti. P2SH-P2WSH aadresse kirjutatakse kasutades `Base58Check` kodeeringut ja need algavad alati `3`-ga, nagu iga P2SH aadress.