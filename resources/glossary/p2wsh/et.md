---
term: P2WSH
---

P2WSH tähistab *Pay to Witness Script Hash*. See on standardne skriptimudel, mida kasutatakse UTXO kulutamistingimuste kehtestamiseks. P2WSH tutvustati koos SegWiti rakendamisega augustis 2017.

See skript on sarnane P2SH-ga (*Pay to Public Script Hash*), kuna see lukustab bitcoine samuti skripti räsi põhjal. Erinevus seisneb selles, kuidas allkirjad ja skriptid tehingusse kaasatakse. Selle tüüpi skripti bitcoinide kulutamiseks peab saaja esitama algse skripti, mida nimetatakse `witnessScript` (võrdne `redeemScript`-iga), koos nõutavate allkirjadega. See mehhanism võimaldab keerukamate kulutamistingimuste, nagu multisigide, rakendamist.

P2WSH kontekstis viiakse allkirjaskripti teave (`scriptWitness`, võrdne `scriptSig`-iga) traditsioonilisest tehingustruktuurist eraldi sektsiooni nimega `Witness`. See samm on SegWiti (*Segregated Witness*) uuenduse omadus, mis aitab vältida allkirja muudetavust. P2WSH tehingud on üldiselt odavamad tasude poolest võrreldes Legacy tehingutega, kuna tunnistaja osa maksab vähem.

P2WSH aadresse kirjutatakse kasutades `Bech32` kodeeringut koos kontrollsummaga BCH koodi kujul. Need aadressid algavad alati `bc1q`-ga. P2WSH on versioon 0 SegWiti väljund.