---
term: BIP0061
---

Uvedena je poruka odbijanja u komunikacionom protokolu između čvorova. Cilj BIP61 je da doda mehanizam povratne informacije kada čvor primi transakciju ili blok od drugog čvora koji smatra nevažećim. Ova poruka odbijanja bi omogućila čvoru da pošiljaocu signalizira razlog zašto je odbijen. Ova vrsta komunikacije je bila namenjena poboljšanju interoperabilnosti među različitim klijentima i komunikacijama između punih čvorova i SPV klijenata. Funkcionalnosti koje je doneo BIP61 su na kraju napuštene počevši od verzije 0.20.0 Bitcoin Core-a, jer su smatrane nepotrebnim dok su uključivale povećane potrebe za propusnim opsegom.