---
term: SWEEP TRANSACTION
---

Model ili obrazac transakcije korišćen u analizi lanca za određivanje prirode transakcije. Ovaj model karakteriše potrošnja jednog UTXO kao ulaza i proizvodnja jednog UTXO kao izlaza. Interpretacija ovog modela je da smo u prisustvu samotransfera. Korisnik je prebacio svoje bitkoine sebi, na drugi Address koji poseduje. Pošto nema promene u transakciji, vrlo je malo verovatno da se radi o plaćanju. Naime, kada se vrši plaćanje, gotovo je nemoguće da platiša ima UTXO koji tačno odgovara iznosu koji zahteva prodavac, uz dodatak transakcijskih naknada. Generalno, platiša je stoga primoran da proizvede izlaz za kusur. Tada znamo da posmatrani korisnik verovatno još uvek poseduje taj UTXO. U kontekstu analize lanca, ako znamo da UTXO korišćen kao ulaz u transakciji pripada Alisi, možemo pretpostaviti da UTXO u izlazu takođe pripada njoj.


![](../../dictionnaire/assets/6.webp)


> ► *U francuskom, "sweep transaction" bi se mogao prevesti kao "transaction de balayage".*