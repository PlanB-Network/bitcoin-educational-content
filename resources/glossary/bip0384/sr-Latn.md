---
term: BIP0384
---

Upoznaje `combo(KEY)` funkciju za deskriptore. Ova funkcija opisuje skup mogućih izlaznih skripti za dati javni ključ. Tako pokriva više tipova skripti istovremeno, uključujući P2PK, P2PKH, P2WPKH i P2SH-P2WPKH. Ako je dati ključ kompresovan, testiraju se sve 4 vrste skripti, a ako nije, testiraju se samo 2 Legacy tipa skripti. Cilj je pojednostaviti predstavljanje ključeva u deskriptorima pružanjem jedinstvene metode za generate različite varijante izlaznih skripti zasnovanih na istom javnom ključu. BIP384 je implementiran zajedno sa svim ostalim BIP-ovima vezanim za deskriptore (osim BIP386) u verziji 0.17 Bitcoin Core.