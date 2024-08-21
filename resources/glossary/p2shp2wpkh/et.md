---
term: P2SH-P2WPKH
---

P2SH-P2WPKH tähistab *Maksa Skripti Räsi - Maksa Tunništaja Avaliku Võtme Räsi*. See on standardne skriptimudel, mida kasutatakse kulutamistingimuste seadmiseks UTXO-le, mida tuntakse ka kui "Pesastatud SegWit".

P2SH-P2WPKH tutvustati SegWiti rakendamisega augustis 2017. See skript on P2WPKH, mis on pakitud P2SH sisse. See lukustab bitcoine avaliku võtme räsi põhjal. Erinevus klassikalisest P2WPKH-st on see, et skript on pakitud klassikalise P2SH `redeemScript`i.

See skript loodi SegWiti käivitamisel selle vastuvõtu hõlbustamiseks. See võimaldab kasutada seda uut standardit isegi teenustega või rahakottidega, mis ei ole veel SegWitiga natiivselt ühilduvad. See on omamoodi üleminekuskript uuele standardile. Täna ei ole seega enam väga asjakohane kasutada selliseid pakitud SegWiti skripte, kuna enamik rahakotte on rakendanud natiivse SegWiti. P2SH-P2WPKH aadresse kirjutatakse kasutades `Base58Check` kodeeringut ja need algavad alati `3`-ga, nagu iga P2SH aadress.

> ► *`P2SH-P2WPKH` nimetatakse mõnikord ka `P2WPKH-pesastatud-P2SH-s`.*