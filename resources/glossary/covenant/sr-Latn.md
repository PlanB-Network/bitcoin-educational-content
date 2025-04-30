---
term: SAVEZ
---

Mehanizam koji omogućava nametanje specifičnih uslova o tome kako se određeni komad valute može trošiti, uključujući buduće transakcije. Pored uslova koje obično dozvoljava skript jezik na UTXO, zavet nameće dodatna ograničenja na to kako se ovaj Bitcoin može trošiti u narednim transakcijama. Tehnički, uspostavljanje zaveta se dešava kada `scriptPubKey` UTXO definiše ograničenja na `scriptPubKey` izlaza transakcije koja troši navedeni UTXO. Proširivanjem opsega skripta, zaveti bi omogućili brojne razvojne mogućnosti na Bitcoin kao što su bilateralno sidrenje drajvčejnova, implementacija trezora, ili poboljšanje nadsistemskih sistema kao što je Lightning. Predlozi zaveta se razlikuju na osnovu tri kriterijuma:


- Njihov opseg;
- Njihova implementacija;
- Njihova rekurzivnost.


Postoji mnogo predloga koji bi omogućili korišćenje zaveta na Bitcoin. Najnapredniji u procesu implementacije su: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) i `OP_VAULT`. Među ostalim predlozima su: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, itd.


Da biste bolje razumeli koncept ugovora, razmotrite ovu analogiju: zamislite sef koji sadrži 500€ u sitnim novčanicama. Ako uspete da otključate ovaj sef pravim ključem, onda možete slobodno koristiti ovaj novac kako želite. Ovo je normalna situacija sa Bitcoin. Sada, zamislite da isti sef ne sadrži 500€ u novčanicama, već vaučere za obrok iste vrednosti. Ako uspete da otvorite ovaj sef, možete koristiti ovu sumu. Međutim, vaša sloboda trošenja je ograničena, jer ove vaučere možete koristiti samo za plaćanje u određenim restoranima. Dakle, postoji prvi uslov za trošenje ovog novca, a to je da uspete da otvorite sef odgovarajućim ključem. Ali postoji i dodatni uslov u vezi sa budućom upotrebom ove sume: mora se potrošiti isključivo u partnerskim restoranima, a ne slobodno. Ovaj sistem ograničenja na buduće transakcije je ono što se naziva ugovor.


> ► *U francuskom jeziku ne postoji izraz koji tačno obuhvata značenje reči "covenant". Moglo bi se govoriti o "klauzuli", "paktu" ili "Commitment", ali to ne bi tačno odgovaralo terminu "covenant". Ovaj termin je preuzet iz pravne terminologije koja omogućava opisivanje ugovorne klauzule koja nameće trajne obaveze na imovinu.*