---
term: VIN
---

Specifičan element Bitcoin transakcije koji određuje izvor sredstava korišćenih za ispunjavanje izlaza. Svaki `vin` se odnosi na neutrošeni izlaz (UTXO) iz prethodne transakcije. Transakcija može sadržati više ulaza, od kojih je svaki identifikovan kombinacijom `txid` (identifikator originalne transakcije) i `vout` (indeks izlaza u toj transakciji).


Svaki `vin` uključuje sledeće informacije:


- `txid`: identifikator prethodne transakcije koja sadrži izlaz korišćen ovde kao ulaz;
- `vout`: indeks izlaza u prethodnoj transakciji;
- `scriptSig` ili `scriptWitness`: skripta za otključavanje koja pruža potrebne podatke za ispunjavanje uslova postavljenih od strane `scriptPubKey` prethodne transakcije čija se sredstva troše, obično pružanjem kriptografske potpisa;
- `nSequence`: specifično polje koje se koristi za označavanje vremenskog zaključavanja ovog unosa, kao i drugih opcija kao što je RBF.