---
term: PSBT
---

Akronim za "Partially Signed Bitcoin Transaction". To je specifikacija uvedena sa BIP174 kako bi se standardizovao način na koji se nedovršene transakcije konstruiraju u softveru povezanom sa Bitcoin, kao što je Wallet softver. PSBT obuhvata transakciju u kojoj ulazi možda nisu u potpunosti potpisani. Uključuje sve potrebne informacije za učesnika da potpiše transakciju bez potrebe za dodatnim podacima. Dakle, PSBT može imati 3 različita oblika:


- Potpuno konstruisana transakcija, ali još nije potpisana;
- Delimično potpisana transakcija, gde su neki ulazi potpisani dok drugi još nisu;
- Ili potpuno potpisana Bitcoin transakcija, koja se može konvertovati da bude spremna za emitovanje na mreži.


PSBT format omogućava interoperabilnost između različitih Wallet softvera i uređaja za potpisivanje (Hardware Wallet). Trenutno se koristi verzija 0 PSBT, kako je definisano u BIP174, ali verzija 2 se predlaže putem BIP370.


> ► *Verzija 1 PSBT ne postoji. Pošto je verzija 0 bila prva verzija, druga verzija je neformalno nazvana verzija 2. Ava Chow, koja je autor BIP370, je stoga odlučila da dodeli broj 2 ovoj novoj verziji kako bi izbegla bilo kakvu zabunu.*