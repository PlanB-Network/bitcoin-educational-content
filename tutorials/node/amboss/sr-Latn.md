---
name: Amboss
description: Istraži i analiziraj Lightning Network
---

![cover](assets/cover.webp)



Lightning Network je Layer protokola Bitcoin, koji je prvenstveno razvijen da podstakne usvajanje Bitcoin plaćanja na dnevnoj bazi povećanjem brzine obrade svake transakcije. Na osnovu principa decentralizacije, Lightning Network se sastoji od čvorova (računara koji pokreću Lightning implementaciju) koji komuniciraju peer-to-peer, prenoseći podatke (plaćanja i verifikaciju plaćanja) jedni drugima.



https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Baš kao i na glavnom lancu, postalo je neophodno omogućiti korisnicima da znaju informacije i status mreže, kako bi se olakšale veze između čvorova i minimizirao problem likvidnosti koji se obično javlja u mreži. Zaista, na Lightning Network, preporučujemo mikro-plaćanja relativno manjih iznosa nego što su to transakcije na Bitcoin glavnom lancu.



Važno je napomenuti da nisu svi Lightning čvorovi dostupni na platformi Amboss.



Kao [Mempool Space](https://Mempool.space), koji pruža korisne informacije o glavnom lancu Bitcoin protokola, od 2022. [Amboss](https://amboss.space) pruža informacije o :





- Čvorovi na Lightning Network
- Kanali plaćanja i njihov kapacitet plaćanja
- Lightning Network evolucija tokom vremena
- Statistika o naplatama čvorovima za prosleđivanje vaših uplata.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

U ovom vodiču, provest ćemo vas kroz ovu platformu, koja je esencijalni resurs za korisnike Lightning Network, one koji žele povezati svoj čvor kako bi proširili mrežu, itd.




## Pronađi parove



Jedan od ciljeva Amboss platforme je omogućiti raznim čvorovima u mreži da se povežu i komuniciraju informacije međusobno. Na početnoj stranici platforme možete direktno pretraživati ime čvora koji već znate, ili pronaći čvorove iz najpopularnijih Lightning portfolija koje koristite.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Na početnoj stranici, takođe ćete pronaći čvorove klasifikovane prema :




- Evolucija kapaciteta: količina Bitcoin povezana sa javnim ključem čvora i ukupna dostupna u svim njegovim kanalima.
- Evolucija kanala: broj novih veza sa drugim čvorovima u mreži.
- Popularnost čvora: koliko često se čvor koristi.



![nodes](assets/fr/03.webp)



Odabir pravog čvora za povezivanje stoga se svodi na proveru sledećih kriterijuma:





- Osigurajte da čvor ima dovoljnu količinu bitkoina; što je veći kapacitet čvora, to je veći iznos bitkoina koji možete platiti.





- Osigurajte da čvor ima veliki broj veza i otvorenih kanala sa drugim čvorovima u mreži.





- Proverite da je čvor aktivan i da ga njegovi vršnjaci i dalje cene proverom broja novih kanala; što više novih kanala ovaj čvor ima otvorenih, to ga više cene drugi čvorovi u mreži.



Kada pronađete pravi čvor, kliknite na njegovo ime da biste bili preusmereni na stranicu sa informacijama o čvoru.



Na ovom Interface, proverom Timestamp novokreiranog kanala, dobićete trag o aktivnosti ovog čvora. Takođe ćete pronaći informacije o kapacitetu kanala ovog čvora: ove informacije su ključne ako želite aktivno koristiti ovaj čvor za izvršavanje svojih plaćanja.




![node_info](assets/fr/04.webp)



U levom delu pronaći ćete više detalja o lokaciji ovog čvora. Na primer, možete videti :




- Javni ključ: identifikator odmah ispod imena čvora.
- Geografski položaj ovog čvora.




![channels](assets/fr/05.webp)



Ovaj Interface vam govori konekciju Address za ovaj čvor: ima oblik `pubkey@ip:port`. U našem primeru, želimo da se povežemo na čvor čiji:




- javni ključ `pubkey` je: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Port: `9735`



![geoinfo](assets/fr/06.webp)



U odeljku **Channels** videćete listu otvorenih kanala i veze čvora sa drugim čvorovima u mreži. Na ovom Interface, nekoliko informacija je ključno da potvrdimo da li ovaj čvor odgovara našim potrebama ili je pouzdan:





- Dolazni odnos**: Iznos koji će vam čvor naplatiti za svaki milion Satoshi koji primi, u zavisnosti od izabranog kanala.
- Odnos (delovi na milion)** : koji predstavlja broj Satoshi po milion jedinica koje će vam čvor naplatiti kada odlučite da izvršite uplatu putem jednog od njegovih kanala. Recimo da odlučite da izvršite uplatu od `10_000 Sats` putem kanala čiji je ppm odnos `500 Sats`, moraćete da platite čvoru `10_000 * 500 / 1_000_000` satoshija, što je ekvivalentno `5 Sats`.
- Maksimum [HTLC](https://planb.network/resources/glossary/htlc)** : Maksimalna količina koju ovaj čvor dozvoljava da prenesete putem jednog od ovih kanala.



Konsultovanjem tabele u ovom Interface, možete pronaći sve ove informacije i na čvoru kojem je dodeljena.



![channels_info](assets/fr/07.webp)



U odeljku **Channel maps** možete videti distribuciju i kapacitet različitih kanala na ovom čvoru. Možete promeniti kriterijume distribucije prikazane izborom jedne od opcija u padajućoj listi sa desne strane.



![cha_maps](assets/fr/08.webp)



Deo **Zatvoreni kanali** grupišu se svi bivši kanali čvora prema tipu zatvaranja:




- Međusobno zatvaranje**: predstavlja sporazum obe strane, koje koriste svoj privatni ključ da potpišu transakciju koja označava zatvaranje kanala i raspodelu stanja unutar njega
- **Prinudno zatvaranje**: predstavlja naglo, jednostrano zatvaranje jednog dela kanala. Ova vrsta zatvaranja se ne preporučuje, jer je Lightning Network protokol zasnovan na kaznama: kada pokušate da prevarite saldo kanala, rizikujete da izgubite sav raspoloživi saldo u tom kanalu.



![closed](assets/fr/09.webp)



Dobijte informacije o tranzitnim naknadama za usmeravanje vaših uplata kroz kanal na čvoru koji koristite.



![fees](assets/fr/10.webp)



## Informacije o mreži



Amboss se fokusira ne samo na informacije o članovima mreže, već i na stanje same mreže.



U odeljku **Statistika**, ispod levog menija "Simulacije", naći ćete grafikon koji prikazuje verovatnoću uspešne uplate kao funkciju iznosa uplate.



Zapravo, primetićete da kriva opada jer, kako se iznos vaše uplate povećava, imate manju šansu da ta uplata prođe. Ovo odražava pravi problem likvidnosti na Lightning Network. Na primer, vaša uplata od `10_000` satoshija ima `79%` šanse da bude izvršena. S druge strane, za uplatu od `3_000_000` satoshija imate manje od `13%` šanse za uspeh.



![network](assets/fr/11.webp)



Meni **Statistika mreže** omogućava vam grafički prikaz statistike za :




- Kanali plaćanja
- Čvorovi
- Kapacitet
- Naknade
- Evolucija kanala.



![network_stat](assets/fr/12.webp)



U meniju **Market statistics**, opcija **Order details** omogućava vam da vidite potražnju za likvidnošću na Lightning Network. Ovaj grafikon takođe može prikazati koji kanali su najtraženiji i/ili koji imaju značajan kapacitet.



![markets](assets/fr/13.webp)




## Alati



Amboss nudi brojne alate koji vam pomažu da optimizujete vaše pretrage i akcije.



### Lightning Network dekoder



Ovaj alat je uglavnom odgovoran za pružanje detalja o strukturi Lightning Invoice, Lightning Address ili Lightning URL.



Na početnoj stranici, u odeljku **Alati**, pošaljite svoj Lightning Address, na primer.



![decoder](assets/fr/14.webp)



Iz ovog dekodera možete dobiti informacije kao što su :




- javni ključ čvora povezan sa vašim Lightning Address;
- Vreme isteka Invoice iz vašeg Address;
- Minimalni i maksimalni iznos koji možete poslati;
- Nostr čvor povezan sa vašim Address, ako je Nostr omogućen na ovom čvoru.



![decode](assets/fr/15.webp)



### Magma IA



Otkrijte najnoviji alat koji je predstavio Amboss za efikasno upravljanje vašim vezama sa Lightning Network čvorovima. Magma AI koristi posvećenu veštačku inteligenciju da se fokusira na važan problem: pravljenje dobrog izbora čvorova za povezivanje.



![magma](assets/fr/16.webp)



### Satoshi kalkulator



Saznajte trenutnu cenu Bitcoin u vašoj lokalnoj valuti (EUR / USD). Na početnoj stranici koristite satoshi kalkulator da biste saznali trenutnu tržišnu cenu.



![calculator](assets/fr/17.webp)




Sada ste završili kompletnu turu kroz funkcije platforme i alate za analizu. Molimo vas da ispod pronađete naš članak o Bitcoin **Mempool.space** istraživaču.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f