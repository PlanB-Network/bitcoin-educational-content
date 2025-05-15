---
term: BIP0072
---

Dovršava BIP70 i BIP71 definišući proširenje Bitcoin URI (BIP21) sa dodatnim parametrom `r`. Ovaj parametar omogućava uključivanje linka ka sigurnom zahtevu za plaćanje potpisanom SSL sertifikatom trgovca. Kada klijent klikne na ovaj prošireni URI, njihov Wallet kontaktira server trgovca kako bi zatražio detalje plaćanja. Ovi detalji se automatski popunjavaju u Wallet transakciji Interface, a klijent može biti obavešten da plaća vlasniku domena koji odgovara sertifikatu za potpisivanje (na primer, "pandul.fr"). Pošto je ovo poboljšanje povezano sa BIP70, nikada nije bilo široko prihvaćeno.