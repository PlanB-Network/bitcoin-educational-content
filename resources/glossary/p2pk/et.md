---
term: P2PK

---
P2PK tähendab *Pay to Public Key*. See on standardne skripti mudel, mida kasutatakse Bitcoinis UTXO kulutustingimuste loomiseks. See võimaldab bitcoinide lukustamist otse avalikule võtmele, mitte aadressile.

Tehniliselt sisaldab P2PK-skript avalikku võtit ja juhendit, mis nõuab rahaliste vahendite avamiseks vastavat digitaalallkirja. Kui omanik soovib bitcoin'e kulutada, peab ta esitama allkirja, mis on toodetud vastava privaatvõtmega. Seda allkirja kontrollitakse ECDSA (*Elliptic Curve Digital Signature Algorithm*) abil. P2PK-d kasutati sageli Bitcoini esimestes versioonides, eelkõige Satoshi Nakamoto poolt. Tänapäeval seda enam peaaegu ei kasutata.