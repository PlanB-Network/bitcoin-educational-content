---
term: PayJoin
---

Specifična struktura transakcije Bitcoin koja poboljšava privatnost korisnika tokom trošenja saradnjom sa primaocem plaćanja. Jedinstvenost PayJoin leži u njegovoj sposobnosti da generate transakciju koja na prvi pogled izgleda obično, ali je zapravo mini CoinJoin između dve strane. Za ovo, struktura transakcije uključuje primaoca plaćanja u ulaze zajedno sa stvarnim pošiljaocem. Tako primalac uključuje plaćanje sebi usred transakcije koje im omogućava da budu plaćeni. Na primer, ako kupite baget za `6,000 Sats` koristeći UTXO od `10,000 Sats`, i odlučite se za PayJoin, vaš pekar će dodati UTXO od `15,000 Sats` koji pripada njima kao ulaz, koji će u potpunosti povratiti kao izlaz, pored vaših `6,000 Sats`.


Transakcija PayJoin ispunjava dva cilja. Prvo, ima za cilj da zavara spoljnog posmatrača stvaranjem mamca u analizi lanca na Common Input Ownership Heuristic (CIOH). Obično, kada transakcija na Blockchain ima više ulaza, pretpostavlja se da svi ti ulazi verovatno pripadaju istoj entitetu. Tako, kada analitičar ispituje transakciju PayJoin, navodi se na verovanje da svi ulazi dolaze od iste osobe. Međutim, ova percepcija je netačna jer primalac plaćanja takođe doprinosi ulazima zajedno sa stvarnim platiocem. Drugo, PayJoin takođe obmanjuje spoljnog posmatrača o stvarnom iznosu plaćanja koje je izvršeno. Ispitivanjem strukture transakcije, analitičar može verovati da je plaćanje ekvivalentno iznosu jednog od izlaza. U stvarnosti, iznos plaćanja ne odgovara nijednom od izlaza. To je zapravo razlika između UTXO primaoca u izlazu i UTXO primaoca u ulazu. U tome, transakcija PayJoin spada u oblast steganografije. Omogućava skrivanje stvarnog iznosa transakcije unutar lažne transakcije koja deluje kao mamac.


![](../../dictionnaire/assets/14.webp)


> ► *PayJoin se takođe ponekad naziva "P2EP (Pay-to-End-Point)", "Stowaway" ili "steganografska transakcija".*