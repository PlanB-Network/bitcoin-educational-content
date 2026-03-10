---
name: Bisq Easy Mobile
description: Protokol za trgovanje od osobe do osobe za nove korisnike bitkoina - bez posrednika, bez KYC.
---
![cover](assets/cover.webp)


## Uvod


[Bisq Easy](https://bisq.network/bisq-easy/) protokol trgovanja je dizajniran za [Bisq 2](https://github.com/bisq-network/bisq2), naslednika [Bisq v1](https://github.com/bisq-network/bisq). Bisq 2 će podržavati više protokola trgovanja, mreže za privatnost i identitete. Omogućava kupovinu Bitcoin bez naknada za trgovanje i bez zahteva za sigurnosnim depozitom. Namenjen je novim kupcima Bitcoin koji traže opciju bez KYC-a i žele da budu efikasno uvedeni od strane iskusnih i upućenih prodavaca koji su upoznati sa Bisq platformom.


Trenutno je Bisq Easy jedini trgovinski protokol za Bisq 2. Planirano je više trgovinskih protokola u budućnosti. Saznajte više o Bisq 2 u ovom vodiču:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

Ovaj kratki vodič je dopuna gornjem uputstvu o kupovini Bitcoin koristeći [Bisq Easy Mobile](https://github.com/bisq-network/bisq-mobile) aplikaciju i Lightning.


## 1️⃣ Početak


Za početak, preuzmite Bisq Easy Mobile sa [stranice za preuzimanje](https://bisq.network/downloads/). Preporučuje se da verifikujete preuzimanje. Uputstva za verifikaciju su takođe dostupna na [stranici za preuzimanje](https://bisq.network/downloads/). Nakon instalacije, potrebno je da prihvatite `Korisnički ugovor`. Zatim, kreirajte javni profil koji se sastoji od `nadimka` i avatara (predstavljenog `ikonicom bota`). Sa Bisq Easy, možete takođe kreirati više korisničkih profila unutar jednog klijenta. Nakon kratke inicijalizacije, stići ćete na `Početni ekran`. Aplikacija ističe edukativni materijal direktno na glavnoj stranici. Dodirnite `Otvorite vodič za trgovinu` da biste se upoznali sa najnovijim informacijama.


![image](assets/en/01.webp)


Vodič za trgovinu objašnjava sve relevantno u jednostavnim koracima:



- Kako trgovati na Bisq Easy
- Kako funkcioniše proces trgovine
- Šta treba da znam o pravilima trgovine.


Još jedan važan deo je **"Koliko je bezbedno trgovati na Bisq Easy?"**


![image](assets/en/08.webp)


Označite polje označeno sa `Pročitao/la sam i razumeo/la` i dodirnite `Završi`.


![image](assets/en/02.webp)


## 2️⃣ Napravite rezervnu kopiju svojih podataka


Pre nego što počnemo, hajde da obavimo neke administrativne zadatke i kreiramo `backup` vaše datoteke za skladištenje podataka. Idite na `Više` > `Backup & Restore` da sačuvate svoj profil i istoriju trgovanja. Ako izgubite uređaj bez backup-a, vaš ugled i tekuće trgovine su neobnovljivi. Unesite `Lozinku` da šifrujete svoj backup.


![image](assets/en/11.webp)


## 3️⃣ Ponude


Sa `Početnog ekrana`, postoje dva načina za navigaciju do ponuda. Dodirnite `Istraži ponude` u sredini ekrana ili dodirnite `Ponude` u donjem meniju. Odatle, izaberite `valutu` kojom želite da trgujete.


![image](assets/en/03.webp)


Za razliku od [Bisq 1](https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), koji zahteva kolateral, Bisq Easy se oslanja isključivo na reputaciju prodavca za sigurnost. Iako ovaj pristup omogućava kupcima da kupe Bitcoin po prvi put bez prethodnog vlasništva, on postavlja visok stepen poverenja u sposobnost prodavca da isporuči Bitcoin nakon primanja fiat uplata. Stoga je Bisq Easy sigurnosni model optimizovan samo za male iznose trgovine i trgovine su ograničene na ekvivalent od $600 USD po transakciji kako bi se minimizirao rizik. U odeljku `Offerbook`, izaberite filtere za metode plaćanja i poravnanje u Lightning ili Bitcoin (on-chain).


![image](assets/en/04.webp)


Nakon primene `filtera`, izaberite odgovarajuću ponudu od uglednog trgovinskog partnera. Prodavčev unapred izabrani način plaćanja i tip poravnanja (`Lightning` ili `on-chain`) će biti prikazani. Uverite se da se ovi podudaraju sa vašim preferencijama pre nego što nastavite. Ovde biramo opciju Lightning ⚡.


![image](assets/en/05.webp)


Pregledajte i potvrdite detalje trgovine dodirom na `Confirm take offer`. Zatim će se pojaviti iskačući ekran koji potvrđuje da ste uspešno prihvatili ponudu. Dodirnite Prikaži trgovinu u `Open Trades`. U odeljku Open Trades nalepite svoj `Lightning invoice` i dodirnite `Send to the seller` da ga podelite. Sada sačekajte podatke o prodavčevom platnom računu. Prodavcima može trebati vremena da odgovore. Povremeno proveravajte ažuriranja u prozoru za ćaskanje.


![image](assets/en/06.webp)


Pošaljite kratak pozdrav u ćaskanju. Prodavac će podeliti podatke o plaćanju kada bude online.


![image](assets/en/09.webp)


Kada primite potrebne podatke o plaćanju od prodavca, nastavite sa izvršavanjem plaćanja. Nakon toga, dodirnite dugme `Potvrdite da ste izvršili plaćanje`, a zatim strpljivo sačekajte potvrdu prijema. ️ ⌛️


Konačno, kada prodavac potvrdi prijem uplate, morate takođe potvrditi prijem Bitcoin. Time se završava kupovina korišćenjem Bisq u Easy Mode. Čestitamo! Sada možete da pritisnete dugme `zatvori trgovinu`.


![image](assets/en/10.webp)


## 4️⃣ Rešavanje sporova na Bisq Easy


Ako nešto pođe po zlu sa vašom trgovinom, i kupci i prodavci mogu zatražiti podršku za medijaciju.


**Šta medijatori mogu da urade:**

• Pomozite olakšavanje uspešnog završetka trgovine

• Verifikuj fiat, altcoin i Bitcoin uplate

• Otkazati trgovine kada je potrebno

• Prijavite ozbiljna kršenja pravila moderatorima za potencijalne zabrane korisnika


**Posledice za prevarantske prodavce:**

U zavisnosti od tipa reputacije:



- Reputacija BSQ obveznica**: DAO može konfiskovati njihove vezane BSQ
- Onion Address Reputacija**: Njihova Bisq 1 onion adresa može biti zabranjena


**Važna napomena:** Pošto je sav ugled vezan za vaš korisnički profil, zabrana potpuno onemogućava vaš ugled.


## 5️⃣ Kreirajte svoju ponudu


Umesto da prihvatite postojeće ponude, možete kreirati svoju ponudu za kupovinu i dozvoliti prodavcima da dođu do vas. Ovo je prava opcija ako ne pronađete nijednu ponudu sa odgovarajućom premijom ili metodama plaćanja na tržištu na kojem želite da trgujete, iako ćete morati da sačekate da prodavac prihvati.


Sa ekrana `Offers` dodirnite zeleni `+` ikonu u donjem desnom uglu. Zatim izaberite `Buy Bitcoin` i odaberite vašu fiat valutu.


Postavite parametre trgovine:



- Fiksni iznos ili Raspon iznosa**: Izaberite koliko želite da potrošite.
- Metod plaćanja**: Izaberite iz dostupnih opcija
- Poravnanje**: Izaberite Lightning ⚡ ili ₿ on-chain


Pregledajte svoje podatke i dodirnite `Kreiraj ponudu`. Vaša ponuda se sada pojavljuje u `Knjizi ponuda`.


![image](assets/en/07.webp)


*Napomena: Kao kupac na Bisq Easy, ne treba vam reputacija—ovo je ključna prednost. Prodavci snose zahtev za reputacijom i rizik, zbog čega naplaćuju premije. Vaša ponuda treba samo da bude dovoljno atraktivno cenovno postavljena da bi je ugledni prodavci razmotrili.*


Jednom kada je objavljeno, sačekajte u odeljku `Offerbook`. Kada prodavac prihvati vašu ponudu, dobićete obaveštenje. Otvorite trgovinu u `Open Trades`, gde prodavac i vi možete razmeniti vaše podatke o plaćanju. Pošaljite svoju Bitcoin adresu ili Lightning fakturu prodavcu. Nakon slanja fiat-a, potvrdite uplatu. Kada prodavac potvrdi prijem, oslobodiće Bitcoins kako bi završili trgovinu.


## 🎯 Zaključak


Bisq Easy omogućava kupovine Bitcoin bez kolaterala, rešavajući klasičan problem "kokoška ili jaje" za nove kupce. Kompromis je jasan: oslanjate se na reputaciju prodavca umesto na zaključana sredstva za sigurnost. Ovaj pristup zasnovan na poverenju objašnjava tipičnu premiju od 5-15%, koja kompenzuje ugledne prodavce za njihovu investiciju u izgradnju poverenja i pružanje podrške. Iako sistem ograničava trgovine na male iznose kako bi se obuzdali potencijalni gubici, uvek se držite prodavaca sa solidnim reputacionim ocenama. Za novajlije spremne da prihvate ove uslove, Bisq Easy nudi jednostavan ulaz u Bitcoin.


## 📚 Bisq Laki Mobilni Resursi


[Github](https://github.com/bisq-network/bisq-mobile) | [Website ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)