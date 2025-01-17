---
term: P2SH

---
P2SH tähendab *Pay to Script Hash*. See on standardne skripti mudel, mida kasutatakse UTXO kulutustingimuste kehtestamiseks. Erinevalt P2PK ja P2PKH skriptidest, kus kulutustingimused on ette kindlaks määratud, võimaldab P2SH suvaliste kulutustingimuste ja lisafunktsioonide integreerimist tehinguskripti.

Tehniliselt sisaldab P2SH-tehingu "scriptPubKey" pigem "redeemScripti" krüptograafilist hashi kui selgesõnalisi kulutustingimusi. See hash saadakse `SHA256` hashi abil. Bitcoinide saatmisel P2SH-aadressile ei avaldata selle aluseks olevat `redeemScript'i`. Tehingus sisaldub ainult selle hash. P2SH-aadressid on kodeeritud `Base58Check`is ja algavad numbriga `3`. Kui saaja soovib saadud bitcoine kulutada, peab ta esitama `redeemScript`, mis vastab `scriptPubKey`-s sisalduvale hashile, koos vajalike andmetega, mis vastavad selle `redeemScripti` tingimustele. Näiteks P2SH multisignatuurse skripti puhul võib skript nõuda mitme privaatvõtme allkirju.

P2SH kasutamine pakub suuremat paindlikkust, kuna see võimaldab luua suvalisi skripte, ilma et saatja teaks üksikasju. P2SH võeti kasutusele 2012. aastal koos BIP16-ga.