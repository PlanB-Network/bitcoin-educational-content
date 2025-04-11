---
term: P2PKH

---
P2PKH tähendab *Pay to Public Key Hash*. See on standardne skripti mudel, mida kasutatakse UTXO kulutustingimuste kehtestamiseks. See võimaldab bitcoinide lukustamist avaliku võtme hashile, st vastuvõtva aadressi kohta. See skript on seotud Legacy-standardiga ja selle võttis kasutusele Satoshi Nakamoto Bitcoini esimestes versioonides.

Erinevalt P2PK-st, kus avalik võti on sõnaselgelt lisatud skriptis, kasutab P2PKH avaliku võtme krüptograafilist sõrmejälge. See skript sisaldab avaliku võtme "SHA256"-i "RIPEMD160"-heksat ja sätestab, et raha kättesaamiseks peab saaja esitama avaliku võtme, mis vastab sellele heksale, ning sellega seotud privaatvõtme alusel loodud kehtiva digitaalallkirja. P2PKH-aadressid on kodeeritud `Base58Check`-vormingus, mis annab neile kontrollsumma kasutamise kaudu kindluse trükivigade vastu. Need aadressid algavad alati numbriga `1`.