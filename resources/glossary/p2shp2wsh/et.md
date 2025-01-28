---
term: P2SH-P2WSH

---
P2SH-P2WSH tähendab *Pay to Script Hash - Pay to Witness Script Hash*. See on standardne skripti mudel, mida kasutatakse UTXO kulutustingimuste loomiseks, mida tuntakse ka kui "Nested SegWit".

P2SH-P2WSH võeti kasutusele koos SegWiti rakendamisega 2017. aasta augustis. See skript kirjeldab P2WSH-i sisse pakitud P2SH-i. See lukustab bitcoinid skripti hashi põhjal. Erinevus klassikalisest P2WSH-st seisneb selles, et skript on mähitud klassikalise P2SH `redeemScript`i sisse.

See skript loodi SegWit'i käivitamisel, et hõlbustada selle kasutuselevõttu. See võimaldab seda uut standardit kasutada isegi teenuste või rahakottidega, mis ei ole veel algselt SegWitiga ühilduvad. Seetõttu ei ole tänapäeval enam väga asjakohane kasutada sedalaadi pakendatud SegWit-skripte, kuna enamik rahakotte on rakendanud natiivse SegWiti. P2SH-P2WSH-aadressid kirjutatakse `Base58Check` kodeeringut kasutades ja need algavad alati `3`-ga, nagu iga P2SH-aadress.