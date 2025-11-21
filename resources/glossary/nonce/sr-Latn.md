---
term: Nonce
---

U kontekstu računarstva, termin "Nonce" odnosi se na broj koji se koristi samo jednom, a zatim zamenjuje. Često je nasumičan ili pseudo-nasumičan. Nonce se koriste u raznim kriptografskim protokolima kako bi se osigurala sigurnost procesa. Na primer, ECDSA potpisi korišćeni unutar Bitcoin protokola uključuju upotrebu Nonce. To znači da ovaj broj mora biti nov za svaki potpis. Ako to nije slučaj, moguće je izračunati privatni ključ korišćenjem poređenja dva potpisa koja koriste isti Nonce.


Nonce se takođe koriste u procesu Bitcoin Mining. Rudari povećavaju ove promenljive vrednosti unutar svojih kandidatskih blokova. Oni modifikuju vrednost Nonce kako bi pronašli kriptografski Hash koji je niži ili jednak cilju težine. Ovaj proces zahteva značajnu računarsku snagu, jer uključuje iscrpnu pretragu među velikim brojem mogućih nonce vrednosti. Kada Miner pronađe Nonce koji, kada je uključen u njihov blok, proizvodi digest koji ispunjava kriterijume težine, blok se emituje na mrežu, a Miner osvaja nagradu.


> ► *Godine 2010, istraživači su otkrili da je Sonyjeva PlayStation 3 koristila isti Nonce prilikom potpisivanja različitih paketa koda. Ova ponovna upotreba Nonce omogućila je napadačima da izračunaju privatni ključ korišćen za potpisivanje softvera. Sa privatnim ključem u rukama, napadači su mogli kreirati važeće potpise za bilo koji kod, omogućavajući im da pokreću neovlašćeni softver, uključujući piratske igre ili prilagođene operativne sisteme, direktno na PS3.*

> ► *Postoji uobičajena zabluda o poreklu termina "Nonce." Neki tvrde da predstavlja skraćenicu za "broj korišćen samo jednom." U stvarnosti, poreklo reči datira iz 18. veka i dolazi iz semantičke evolucije staroengleskog izraza "then anes," što je značilo "za tu priliku."*