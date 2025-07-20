---
term: ANALIZA HEURISTIČKA
---

Heuristička analiza za lanac Bitcoin je porodica empirijskih metoda koje se koriste za praćenje toka bitkoina na Blockchain na osnovu karakteristika uočenih u transakcijama. Heuristika je praktičan pristup rešavanju problema, često putem približnih metoda, ali predstavlja dovoljno dobro rešenje za postizanje datog cilja. Ove heuristike daju prilično pouzdane rezultate, ali nikada sa apsolutnom preciznošću. Drugim rečima, analiza lanca uvek uključuje određeni stepen verovatnoće u donetim zaključcima. Na primer, može se proceniti sa više ili manje sigurnosti da dve adrese pripadaju istoj entitetu, ali potpuna sigurnost je uvek nedostižna. Ceo cilj analize lanca leži upravo u agregaciji različitih heuristika kako bi se smanjio rizik od greške. To je, na neki način, akumulacija dokaza koja nam omogućava da se približimo stvarnosti. U ovom kontekstu, razlikuju se interne i eksterne heuristike.


Interni heuristički pristupi fokusiraju se na karakteristike specifične za pojedinačnu transakciju. U svoju analizu uključuju Elements kao što su iznosi UTXO-a, korišćeni skripti, verzije ili vremena zaključavanja. Na primer, heuristika zaokruženog plaćanja omogućava identifikaciju izlaza transakcije kao verovatno plaćanje ako je njegov iznos zaokružen broj. Ove heuristike često omogućavaju identifikaciju kusura (novca vraćenog istom korisniku) i tako omogućavaju nastavak praćenja.


Eksterne heuristike, s druge strane, analiziraju sličnosti i karakteristike izvan same transakcije. One obuhvataju celokupno transakcijsko okruženje. Na primer, ponovna upotreba Address kroz više transakcija je eksterna heuristika. CIOH je takođe jedna od njih.