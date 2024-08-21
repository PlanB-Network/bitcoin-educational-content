---
term: P2PK
---

P2PK tähistab *Maksa Avalikule Võtmele*. See on standardne skriptimudel, mida kasutatakse Bitcoinis, et määrata UTXO kulutamise tingimused. See võimaldab lukustada bitcoine otse avalikule võtmele, mitte aadressile.
Tehniliselt sisaldab P2PK skript avalikku võtit ja juhist, mis nõuab vastava digitaalse allkirja esitamist vahendite vabastamiseks. Kui omanik soovib bitcoine kulutada, peab ta esitama vastava privaatvõtmega loodud allkirja. Seda allkirja kontrollitakse kasutades ECDSA (*Elliptilise Kõvera Digitaalallkirja Algoritmi*). P2PK-d kasutati sageli Bitcoin'i varajastes versioonides, eriti Satoshi Nakamoto poolt. Tänapäeval on selle kasutus peaaegu olematu.