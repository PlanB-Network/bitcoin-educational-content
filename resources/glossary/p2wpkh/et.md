---
term: P2WPKH
---

P2WPKH tähistab *Maksa tunnistaja avaliku võtme räsi* (Pay to Witness Public Key Hash). See on standardne skriptimudel, mida kasutatakse UTXO kulutamistingimuste kehtestamiseks. P2WPKH tutvustati SegWiti rakendamisega augustis 2017.

See skript on sarnane P2PKH-ga (*Maksa avaliku võtme räsi*), kuna see lukustab bitcoine ka avaliku võtme räsi, st vastuvõtva aadressi, põhjal. Erinevus seisneb selles, kuidas allkirju ja skripte tehingusse kaasatakse. P2WPKH puhul liigutatakse allkirjaskripti teave (`scriptSig`) traditsioonilisest tehingustruktuurist eraldi sektsiooni nimega `Witness`. See liigutus on SegWiti (*Segregated Witness*, eraldatud tunnistaja) uuenduse omadus, mis aitab vältida allkirjade muudetavust. P2WPKH tehingud on üldiselt vähem kulukad tasude osas võrreldes Legacy tehingutega, kuna tunnistaja osa maksab vähem.

P2WPKH aadresse kirjutatakse kasutades `Bech32` kodeeringut koos kontrollsummaga BCH koodi kujul. Need aadressid algavad alati `bc1q`-ga. P2WPKH on versioon 0 SegWiti väljund.