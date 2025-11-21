---
term: NAKNADA ZA TRANSAKCIJU
---

Naknade za transakcije predstavljaju iznos koji ima za cilj da kompenzuje rudare za njihovo učešće u Proof of Work mehanizmu. Ove naknade podstiču rudare da uključe transakcije u blokove koje kreiraju. One proizlaze iz razlike između ukupnog iznosa ulaza i ukupnog iznosa izlaza u transakciji:


```text
fees = inputs - outputs
```


Oni su izraženi u `Sats/vBytes`, što znači da naknade ne zavise od količine poslatih bitkoina, već od težine transakcije. Slobodno ih bira pošiljalac transakcije i određuju brzinu njenog uključivanja u blok putem aukcijskog mehanizma. Na primer, recimo da napravim transakciju sa ulazom od `100,000 Sats`, izlazom od `40,000 Sats`, i još jednim izlazom od `58,500 Sats`. Ukupno za izlaze je `98,500 Sats`. Naknade dodeljene ovoj transakciji su `1,500 Sats`. Miner koji uključuje moju transakciju može kreirati `1,500 Sats` u svom Coinbase Transaction u Exchange za `1,500 Sats` koje nisam povratio u svojim izlazima.


Transakcije sa višim naknadama, u odnosu na njihovu veličinu, tretiraju se kao prioritet od strane rudara, što može ubrzati proces potvrde. Suprotno tome, transakcije sa nižim naknadama mogu biti odložene tokom perioda velike zagušenosti. Vredi napomenuti da su Bitcoin naknade za transakcije različite od subvencije za blok, koja je dodatni podsticaj za rudare. Block reward se sastoji od novih bitkoina stvorenih sa svakim iskopanim blokom (subvencija za blok), kao i prikupljenih naknada za transakcije. Dok se subvencija za blok smanjuje tokom vremena zbog ukupnog Supply limita bitkoina, naknade za transakcije će i dalje igrati ključnu ulogu u podsticanju rudara da učestvuju.


Na nivou protokola, ništa ne sprečava korisnike da uključe transakcije bez ikakvih naknada u blok. U stvarnosti, ovakva transakcija bez naknade je izuzetna. Po defaultu, Bitcoin čvorovi ne prosleđuju transakcije sa naknadama manjim od `1 sat/vBytes`. Ako su neke transakcije bez naknade prošle, to je zato što su bile direktno integrisane od strane pobedničkog Miner, bez prolaska kroz mrežu čvorova. Na primer, sledeća transakcija ne uključuje naknade:


```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```


U ovom konkretnom primeru, to je bila transakcija koju je inicirao direktor F2Pool Mining pool. Kao redovan korisnik, trenutna donja granica je stoga `1 sat/vBytes`.

Takođe je potrebno razmotriti granice čišćenja. Tokom perioda velike zagušenosti, mempool-ovi čvorova čiste svoje transakcije na čekanju ispod određenog praga, kako bi poštovali svoj dodeljeni RAM limit. Ovaj limit slobodno bira korisnik, ali mnogi ostavljaju podrazumevanu vrednost Bitcoin Core na 300 MB. Može se modifikovati u `Bitcoin.conf` fajlu sa `maxmempool` parametrom.

> ► *Na engleskom to nazivamo "transaction fees".*