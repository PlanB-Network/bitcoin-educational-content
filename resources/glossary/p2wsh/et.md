---
term: P2WSH

---
P2WSH tähendab *Pay to Witness Script Hash*. See on standardne skripti mudel, mida kasutatakse UTXO kulutustingimuste kehtestamiseks. P2WSH võeti kasutusele koos SegWiti rakendamisega 2017. aasta augustis.

See skript on sarnane P2SH (*Pay to Public Script Hash*), kuna see lukustab samuti bitcoinid skripti hashi põhjal. Erinevus seisneb selles, kuidas allkirjad ja skriptid tehingusse kaasatakse. Selleks, et kulutada bitcoine seda tüüpi skripti kohta, peab saaja esitama originaalskripti, mida nimetatakse `witnessScript` (samaväärne `redeemScript`iga), koos nõutavate allkirjadega. See mehhanism võimaldab rakendada keerulisemaid kulutamistingimusi, näiteks multisigs.

P2WSH kontekstis viiakse allkirjastamisskripti teave (`scriptWitness`, mis on samaväärne `scriptSig`ga) traditsioonilisest tehingustruktuurist eraldi sektsiooni nimega `Witness`. See liikumine on SegWit (*Segregated Witness*) uuenduse omadus, mis aitab vältida allkirjade võltsimist. P2WSH-tehingud on üldjuhul odavamad tasude poolest võrreldes Legacy-tehingutega, kuna tunnistajas olev osa maksab vähem.

P2WSH-aadressid kirjutatakse "Bech32" kodeeringut kasutades koos kontrollsummaga BCH-koodi kujul. Need aadressid algavad alati tähega `bc1q`. P2WSH on 0-versiooni SegWit väljund.