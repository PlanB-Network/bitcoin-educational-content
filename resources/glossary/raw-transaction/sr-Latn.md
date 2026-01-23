---
term: Sirova transakcija
definition:
---

Transakcija Bitcoin koja je izgrađena i potpisana, postoji u svom binarnom obliku. Sirova transakcija (*raw TX*) je konačna reprezentacija transakcije, neposredno pre nego što se emituje na mreži. Ova transakcija sadrži sve neophodne informacije za njeno uključivanje u blok:


- Verzija;
- Zastava;
- Ulazi;
- Izlazi;
- Vreme zaključavanja;
- Svedok.


Ono što se naziva "*raw transaction*" predstavlja sirove podatke koji se dvaput propuštaju kroz SHA256 Hash funkciju do generate transakcije txid. Ovi podaci se zatim koriste u Merkle Tree bloka da integrišu transakciju u Blockchain.


