---
name: Bitfeed
description: Istražite glavnu Bitcoin protokolnu lanac.
---

![cover](assets/cover.webp)



Bitfeed je platforma za vizualizaciju onchain sloja Bitcoin protokola. Pokrenuta je od strane jednog od saradnika na projektu Mempool.space i ističe se prvenstveno po svom minimalističkom izgledu i jednostavnosti korišćenja.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

U ovom vodiču ćemo pogledati ovaj alat, koji vam omogućava da istražite sve transakcije i blokove na mreži.



## Početak sa Bitfeed-om



Bitfeed je platforma koja se fokusira na tri glavne tačke:





- Blockchain konsultacija**,
- Pretraga transakcija**,
- Vizualizacija mempool-a**.



### Konsultovanje blockchaina



Na početnoj strani Bitfeed-a, uglavnom ćete pronaći :





- Traka za pretragu: Ovaj deo je početna tačka za upite o blockchainu. Ovde možete pretraživati određeni blok po njegovom broju ili hešu. Takođe možete pretraživati određene transakcije i Bitcoin adrese kako biste verifikovali određene informacije o transakcijama na mreži.



![searchBar](assets/fr/01.webp)



U gornjem levom uglu možete videti trenutnu cenu bitkoina, procenjenu u američkim dolarima (USD).



![price](assets/fr/02.webp)



Na desnoj bočnoj traci nalazi se meni platforme. Iz ovog menija možete prilagoditi interfejs platforme prema vašim željama, dodati ili ukloniti stavke i prilagoditi filtere prikaza. Na primer, pogledajte veličinu svakog bloka po vrednosti ili po težini u virtuelnim bajtovima (vBytes).



![menu](assets/fr/03.webp)



U centru stranice nalazi se poslednji iskopani blok, sa prikazom svih transakcija uključenih u taj blok. Ovaj odeljak pruža informacije o vremenskoj oznaci, ukupnom broju bitkoina uključenih u blok, veličini bloka u bajtovima, broju transakcija i prosečnom odnosu troškova transakcije po virtuelnom bajtu u bloku.



![block](assets/fr/04.webp)



Možete se vratiti kroz istoriju kanala pretraživanjem određenog bloka u traci za pretragu i pregledati ga prema vašim kriterijumima.



Na primer, želimo da pregledamo transakcije u bloku `879488`.



![bloc](assets/fr/05.webp)



Prva transakcija ovog bloka predstavlja **coinbase** transakciju koja omogućava rudaru ovog bloka da zaradi mining nagradu, koja se može potrošiti tek nakon što se iskopa 100 blokova, a sastoji se od uključenih naknada za transakcije i blok granta. Ova transakcija je ona koja omogućava izdavanje novih bitkoina u sistemu.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f

Podrazumevano, transakcije u bloku su predstavljene prema dva kriterijuma:




- Veličina, koja može varirati između vrednosti i težine (vBytes) ;
- Boja može varirati između starosti i odnosa transakcijskih naknada po virtuelnom bajtu.



![options](assets/fr/07.webp)



Stoga možemo zaključiti da sve transakcije uključene u isti blok imaju isti broj potvrda u blockchainu. Najveće kocke predstavljaju transakcije koje sadrže najveći iznos bitcoina.



Ovo tumačenje dodatno potvrđuje opcija menija **"Info "**, koja nas obaveštava o prevodu boje i veličine transakcija bloka.



![infos](assets/fr/08.webp)



Takođe možete pregledati transakcije bloka prema virtuelnim bajtovima i odnosu naknade. Ovaj prikaz može se razlikovati od prethodnog, jer bitcoin vrednost uključena u transakciju ne definiše njenu veličinu.



![visualisation](assets/fr/09.webp)



### Pregled transakcija



Možete pretražiti transakciju koristeći njen identifikator putem trake za pretragu. Takođe možete kliknuti na kocku da biste videli informacije vezane za tu transakciju.



U našem slučaju, hajde da uzmemo transakciju koja zauzima najveći prostor u bloku `879488`.



![biggest](assets/fr/10.webp)



Videćete da ova transakcija ima `42,989`, što predstavlja razliku između poslednjeg iskopanog bloka i našeg izabranog bloka. Ove potvrde pomažu u jačanju sigurnosti Bitcoin mreže, jer bi napadači, da bi zlonamerno izmenili ovu transakciju, morali da poseduju ekvivalentnu računarsku snagu da ponovo napišu čitav glavni lanac blokova.



Veličina ove transakcije je `57,088 vBytes`, uglavnom zbog velikog broja UTXO-a korišćenih u njenoj konstrukciji (842 unosa). Iznenađujuće, primenjeni odnos naknade ostaje relativno nizak (samo 4 sats/vByte) u poređenju sa prosekom celog bloka od 5.82 sats/vByte.



Transakcija koja zauzima najviše prostora stoga nije nužno transakcija sa najvišim odnosom troškova transakcije.



![transaction](assets/fr/11.webp)



Ako pratite skalu u meniju **Info**, transakcija sa najvišim odnosom troškova transakcije je ljubičasta. To je transakcija [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) sa odnosom troškova transakcije od `147.49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool vizualizacija



Mempool je virtualna lokacija gde se Bitcoin transakcije koje čekaju da budu uključene u blok grupišu zajedno. Bitfeed omogućava konsultaciju [mempoola](https://planb.academy/resources/glossary/mempool) nekoliko Bitcoin rudara, nudeći širok spektar praćenja transakcija.



![mempool](assets/fr/13.webp)



U ovom odeljku možete pratiti sve važeće i još nepotvrđene transakcije na glavnom lancu Bitcoin mreže.



![unconfirmed](assets/fr/14.webp)



Sada imate vodič za korišćenje Bitfeed platforme za analizu blokova i transakcija kako biste vizualizovali informacije dostupne na glavnom lancu Bitcoin mreže, uz korist minimalističkog, jednostavnog interfejsa. Ako vam se dopao ovaj vodič, preporučujemo da napravite sledeći korak: otkrijte Lightning Network putem Amboss projekta.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017