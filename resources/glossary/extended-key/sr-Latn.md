---
term: PRODUŽENI KLJUČ
---

Niz karaktera koji kombinuje ključ (javni ili privatni), njegov povezani lančani kod i niz metapodataka. Prošireni ključ objedinjuje sve Elements neophodne za izvođenje podređenih ključeva u jedan identifikator. Koriste se u determinističkim i hijerarhijskim novčanicima i mogu biti dve vrste: prošireni javni ključ (koristi se za izvođenje podređenih javnih ključeva) ili prošireni privatni ključ (koristi se za izvođenje i podređenih privatnih i javnih ključeva). Prošireni ključ tako uključuje nekoliko različitih delova podataka, opisanih u BIP32, u sledećem redosledu:


- Prefiks: `prv` i `pub` su HRP (Human Readable Part) koji označavaju da li je u pitanju prošireni privatni ključ (`prv`) ili prošireni javni ključ (`pub`). Prvo slovo prefiksa označava verziju proširenog ključa: `x` za Legacy ili SegWit V1 na Bitcoin, `t` za Legacy ili SegWit V1 na Bitcoin Testnet, `y` za Nested SegWit na Bitcoin, `u` za Nested SegWit na Bitcoin Testnet, `z` za SegWit V0 na Bitcoin, `v` za SegWit V0 na Bitcoin Testnet.
- Dubina, koja označava broj izvedenica od glavnog ključa do proširenog ključa;
- Otisak prsta roditelja. Ovo predstavlja prva 4 bajta `HASH160` roditeljskog javnog ključa;
- Indeks. Ovo je broj para među njegovom braćom i sestrama od kojeg je izveden prošireni ključ;
- Kod lanca;
- Bajt za popunjavanje ako je to privatni ključ `0x00`;
- Privatni ili javni ključ;
- Kontrolni zbir. Predstavlja prva 4 bajta `HASH256` ostatka proširenog ključa.


U praksi, prošireni javni ključ se koristi za generate adrese za primanje i za praćenje transakcija na računu bez izlaganja povezanih privatnih ključeva. Ovo može omogućiti, na primer, kreiranje takozvanog "samo-za-gledanje" Wallet. Međutim, važno je napomenuti da je prošireni javni ključ osetljiva informacija za privatnost korisnika, jer njegovo otkrivanje može omogućiti trećim stranama da prate transakcije i vide stanje povezanog računa.