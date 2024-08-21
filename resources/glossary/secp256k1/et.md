---
term: SECP256K1
---

Nimi, mis on antud spetsiifilisele elliptilisele kõverale, mida kasutatakse Bitcoin'i protokollis ECDSA (*Elliptic Curve Digital Signature Algorithm*) ja Schnorri digitaalallkirja algoritmide rakendamiseks. `secp256k1` kõver valiti Bitcoin'i leiutaja Satoshi Nakamoto poolt. Sellel on mõned huvitavad omadused, eriti jõudluse eelised.

`secp256k1` kasutamine Bitcoin'is tähendab, et iga privaatvõti (juhuslik 256-bitine number) on kaardistatud vastavale avalikule võtmele läbi privaatvõtme punkti liitmise ja kahekordistamise `secp256k1` kõvera generaatorpunkti abil. See toiming on lihtne teostada ühes suunas, kuid praktiliselt võimatu tagasi pöörata, mis kujutab endast Bitcoin'i digitaalallkirjade turvalisuse alust.

`secp256k1` kõver on määratletud elliptilise kõvera võrrandiga $y^2 = x^3 + 7$, mis tähendab, et sellel on kordajad $a$ võrdne $0$ ja $b$ võrdne $7$ üldises elliptilise kõvera võrrandi vormis $y^2 = x^3 + ax + b$. `secp256k1` on määratletud üle lõpliku välja, mille kord on väga suur algarv, spetsiifiliselt $p = 2^{256} - 2^{32} - 977$. Kõveral on ka grupi kord, mis on kõvera eristuvate punktide arv, eelnevalt määratletud generaatorpunkt (või punkt $G$), mida kasutatakse krüptograafilistes operatsioonides võtmepaaride genereerimiseks, ja kofaktor võrdne $1$-ga.

> ► *“SEC” tähistab “Standards for Efficient Cryptography”. “P256” näitab, et kõver on määratletud välja $\mathbb{Z}_p$ üle, kus $p$ on 256-bitine algarv. “K” viitab selle leiutaja nimele, Neal Koblitz. Lõpuks, “1” näitab, et see on selle kõvera esimene versioon.*