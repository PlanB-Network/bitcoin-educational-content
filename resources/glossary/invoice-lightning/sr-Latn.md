---
term: Invoice lightning
definition: Lightning zahtev za plaćanje koji sadrži sve informacije potrebne za izvršenje transakcije.
---

Zahtev za Lightning plaćanje generisan od strane primaoca, koji sadrži sve informacije potrebne za završetak transakcije.


Invoice Lightning sadrži odredište plaćanja u obliku javnog ključa čvora primaoca, ali takođe i prefiks `LN`, iznos, vreme do isteka, Hash tajne korišćene u HTLC-ovima, i druge metapodatke, od kojih su neki opcionalni, kao što su opcije rutiranja. Ovi računi su definisani BOLT11 standardom. Kada se plati, Invoice Lightning ne može biti ponovo korišćen.


