---
term: PRIJEM Address
---

Informacije korišćene za primanje bitkoina. Address se obično konstruira heširanjem javnog ključa, koristeći `SHA256` i `RIMPEMD160`, i dodavanjem metapodataka ovom sažetku. Javni ključevi korišćeni za konstruisanje primajućeg Address su deo korisnikovog Wallet i stoga su izvedeni iz njihovog seed. Na primer, SegWit adrese se sastoje od sledećih informacija:


- HRP da označi "Bitcoin": `bc`;
- Razdvojnik: `1`;
- Verzija SegWit korišćena: `q` ili `p`;
- Nosač: sažetak javnog ključa (ili direktno javni ključ u slučaju Taproot);
- Kontrolna suma: BCH kod.


Međutim, prijemni Address može takođe predstavljati nešto drugo u zavisnosti od korišćenog modela skripte. Na primer, P2SH adrese su konstruisane korišćenjem skripte Hash. S druge strane, Taproot adrese sadrže direktno prilagođeni javni ključ bez njegovog heširanja.


Primanje Address može biti predstavljeno u obliku alfanumeričkog niza ili kao QR kod. Svaki Address može se koristiti više puta, ali ovo je praksa koja se strogo ne preporučuje. Zaista, kako bi se održao određeni nivo privatnosti, savetuje se da se svaki Bitcoin Address koristi samo jednom. Novi Address treba generisati za svaku dolaznu uplatu na nečiji Wallet. Address je kodiran u `Bech32` za SegWit V0 adrese, u `Bech32m` za SegWit V1 adrese, i u `Base58check` za Legacy adrese. Sa tehničke tačke gledišta, primanje Bitcoin se prevodi u posedovanje privatnog ključa povezanog sa javnim ključem (i tako Address). Kada neko primi bitkoine, pošiljalac ažurira postojeće ograničenje na njihovom trošenju tako da samo primalac sada može imati ovu moć.


![](../../dictionnaire/assets/23.webp)