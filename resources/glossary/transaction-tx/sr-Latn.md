---
term: TRANSAKCIJA (TX)
---

U kontekstu Bitcoin, transakcija (skraćeno "TX") je operacija zabeležena na Blockchain koja prenosi Ownership bitkoina sa jednog ili više ulaza na jedan ili više izlaza. Svaka transakcija koristi Nepotrošene Izlaze Transakcija (UTXO-e) kao ulaze, koji su izlazi iz prethodnih transakcija, i stvara nove UTXO-e kao izlaze, koji se mogu koristiti kao ulazi u budućim transakcijama.


Svaki unos uključuje referencu na postojeći izlaz zajedno sa skriptom potpisa (`scriptSig`) koja ispunjava uslove potrošnje (`scriptPubKey`) uspostavljene od strane izlaza na koji se odnosi. Ovo je ono što omogućava otključavanje bitkoina. Izlazi definišu nove uslove potrošnje (`scriptPubKey`) za prenete bitkoine, često u obliku javnog ključa ili Address sa kojim su bitkoini sada povezani.