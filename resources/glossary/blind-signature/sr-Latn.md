---
term: SLEPAK POTPIS
---

Chaumovi slepi potpisi su oblik digitalnog potpisa gde izdavalac potpisa ne zna sadržaj poruke koju potpisuje. Međutim, potpis se kasnije može verifikovati uz originalnu poruku. Ovu tehniku je razvio kriptograf David Chaum 1983. godine.


Razmotrimo primer kompanije koja želi da autentifikuje poverljiv dokument, kao što je Contract, bez otkrivanja njegovog sadržaja. Kompanija primenjuje proces maskiranja koji kriptografski transformiše originalni dokument na reverzibilan način. Ovaj modifikovani dokument se šalje sertifikacionom autoritetu koji primenjuje slepi potpis bez poznavanja osnovnog sadržaja. Nakon što primi maskirani potpisani dokument, kompanija uklanja masku sa potpisa. Rezultat je originalni dokument autentifikovan potpisom autoriteta, a da autoritet nikada nije video originalni sadržaj.


Dakle, Chaumovi slepi potpisi omogućavaju sertifikaciju autentičnosti dokumenta bez poznavanja njegovog sadržaja, osiguravajući i poverljivost korisničkih podataka i integritet potpisanog dokumenta.


U Bitcoin, ovaj protokol se koristi u sistemima Chaumian banaka kao sloj (Cashu, Fedimint, itd.), ali posebno u Chaumian CoinJoin protokolima, kako bi se osiguralo da koordinator ne može povezati ulaz sa izlazom.