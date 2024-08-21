---
term: P2PKH
---

P2PKH tähistab *Maksa Avaliku Võtme Räsi* (Pay to Public Key Hash). See on standardne skriptimudel, mida kasutatakse UTXO kulutamistingimuste kehtestamiseks. See võimaldab lukustada bitcoine avaliku võtme räsi, st vastuvõtva aadressi, peale. See skript on seotud Legacy standardiga ja tutvustati Bitcoin'i varajastes versioonides Satoshi Nakamoto poolt.

Erinevalt P2PK-st, kus avalik võti on skriptis selgelt kaasatud, kasutab P2PKH avaliku võtme krüptograafilist sõrmejälge. See skript sisaldab avaliku võtme `SHA256` räsi `RIPEMD160` räsi ja nõuab, et fondidele juurdepääsuks peab saaja esitama avaliku võtme, mis vastab sellele räsile, samuti kehtiva digitaalse allkirja, mis on genereeritud seotud privaatvõtmest. P2PKH aadresse kodeeritakse kasutades `Base58Check` formaati, mis annab neile robustsuse trükivigade vastu läbi kontrollsumma kasutamise. Need aadressid algavad alati numbriga `1`.