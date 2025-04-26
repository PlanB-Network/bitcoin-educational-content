---
term: P2SH-P2WPKH

---
P2SH-P2WPKH tähendab *Pay to Script Hash - Pay to Witness Public Key Hash*. See on standardne skripti mudel, mida kasutatakse UTXO kulutustingimuste loomiseks, mida tuntakse ka kui "Nested SegWit".

P2SH-P2WPKH võeti kasutusele koos SegWiti rakendamisega 2017. aasta augustis. See skript on P2WPKH, mis on pakitud P2SH-sse. See lukustab bitcoinid avaliku võtme hashi põhjal. Erinevus klassikalisest P2WPKH-st seisneb selles, et skript on mähitud klassikalise P2SH `redeemScript`i sisse.

See skript loodi SegWit'i käivitamisel, et hõlbustada selle kasutuselevõttu. See võimaldab seda uut standardit kasutada isegi teenuste või rahakottidega, mis ei ole veel algselt SegWitiga ühilduvad. Tegemist on omamoodi üleminekuskeptiga uue standardi suunas. Tänapäeval ei ole seetõttu enam väga asjakohane kasutada sedalaadi pakendatud SegWit-skripte, kuna enamik rahakotte on rakendanud natiivse SegWiti. P2SH-P2WPKH-aadressid kirjutatakse `Base58Check` kodeeringut kasutades ja need algavad alati `3`-ga, nagu iga P2SH-aadress.

> ► *`P2SH-P2WPKH` nimetatakse mõnikord ka `P2WPKH-p2SH-siseselt-P2SH`