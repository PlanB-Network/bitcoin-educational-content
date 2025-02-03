---
term: P2WPKH

---
P2WPKH tähendab *Pay to Witness Public Key Hash*. See on standardne skripti mudel, mida kasutatakse UTXO kulutustingimuste loomiseks. P2WPKH võeti kasutusele koos SegWiti rakendamisega 2017. aasta augustis.

See skript on sarnane P2PKH-ga (*Pay to Public Key Hash*), sest ka see lukustab bitcoinid avaliku võtme, st vastuvõtva aadressi hash'i alusel. Erinevus seisneb selles, kuidas allkirjad ja skriptid on tehingusse kaasatud. P2WPKH puhul on allkirjastusskripti teave (`scriptSig`) viidud traditsioonilisest tehingu struktuurist eraldi sektsiooni nimega `Witness`. See liikumine on SegWit (*Segregated Witness*) uuenduse funktsioon, mis aitab vältida allkirjade võltsimist. P2WPKH-tehingud on üldjuhul odavamad tasude poolest võrreldes Legacy-tehingutega, kuna tunnistajas olev osa maksab vähem.

P2WPKH-aadressid kirjutatakse "Bech32" kodeeringut kasutades koos kontrollsummaga BCH-koodi kujul. Need aadressid algavad alati tähega `bc1q`. P2WPKH on SegWiti versiooni 0 väljund.