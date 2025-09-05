---
name: Ricochet
description: Razumevanje i korišćenje Ricochet transakcija
---
![cover ricochet](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, Ricochet alat više nije dostupan. Međutim, moguće je da će ovaj alat biti ponovo uveden u narednim nedeljama. U međuvremenu, možete izvesti Ricochet samo ručno. Teorijski deo ovog članka ostaje relevantan za razumevanje njegovog rada i učenje kako da ga uradite ručno.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> Premium alat koji dodaje dodatne „preskoke“ u istoriji vaše transakcije. Na taj način zbunjuje crne liste i pomaže u zaštiti od neopravdanih zatvaranja naloga od strane trećih lica.

## Šta je Ricochet?


Ricochet je tehnika koja uključuje sprovođenje više fiktivnih transakcija prema sebi kako bi se simulirao prenos Bitcoin vlasništva. Ovaj alat se razlikuje od drugih Samourai transakcija jer ne pruža perspektivnu anonimnost, već oblik retrospektivne anonimnosti. Ricochet pomaže da se zamagle specifičnosti koje bi mogle ugroziti fungibilnost Bitcoin novčića.


Na primer, ako izvršite CoinJoin, vaš izlazni novčić iz mešanja će biti identifikovan kao takav. Alati za analizu lanca mogu otkriti obrasce CoinJoin transakcija i označiti novčiće koji iz njih izlaze. Zaista, CoinJoin ima za cilj da prekine istorijske veze novčića, ali njihov prolazak kroz coinjoin-ove ostaje detektabilan. Da napravimo analogiju, ovaj fenomen je sličan šifrovanju teksta: iako ne možemo pristupiti originalnom čistom tekstu, lako je prepoznatljivo da je šifrovanje primenjeno.


Precizno, ova oznaka "CoinJoin output coin" može uticati na fungibilnost UTXO-a. Regulisana lica, kao što su platforme za kripto trgovinu, mogu odbiti da prihvate UTXO koji je prošao kroz CoinJoin, ili čak zahtevati objašnjenja od njegovog vlasnika, uz rizik da im nalog bude blokiran ili sredstva zamrznuta. U nekim slučajevima, platforma može čak prijaviti vaše ponašanje državnim vlastima.


Tu dolazi do izražaja Ricochet metoda. Da bi se zamaglio trag koji ostavlja CoinJoin, Ricochet izvršava četiri uzastopne transakcije gde korisnik prenosi svoja sredstva na različite adrese koje pripadaju njemu. Nakon ovog niza transakcija, Ricochet alat konačno usmerava bitkoine na njihovu krajnju destinaciju, kao što je platforma za trgovinu. Cilj je stvoriti distancu između originalne CoinJoin transakcije i konačnog čina trošenja. Na taj način, alati za analizu lanca će misliti da je verovatno došlo do prenosa vlasništva nakon CoinJoin-a, te stoga nije potrebno preduzimati akciju protiv pošiljaoca.


![ricochet diagram](assets/en/1.webp)


Suočeni sa Ricochet metodom, moglo bi se zamisliti da bi softver za analizu lanaca produbio svoje ispitivanje izvan četiri skoka. Međutim, ove platforme se suočavaju sa dilemom u optimizaciji praga detekcije. Moraju uspostaviti granicu na broju skokova nakon kojih priznaju da je verovatno došlo do promene vlasništva i da bi vezu sa prethodnim CoinJoin-om trebalo ignorisati. Međutim, određivanje ovog praga je rizično: svako proširenje posmatranog broja skokova eksponencijalno povećava obim lažno pozitivnih rezultata, tj. pojedinaca pogrešno označenih kao učesnici u CoinJoin-u, kada je operaciju zapravo izveo neko drugi. Ovaj scenario predstavlja veliki rizik za ove kompanije, jer lažno pozitivni rezultati dovode do nezadovoljstva, što može navesti pogođene klijente ka konkurenciji. Dugoročno gledano, previše ambiciozan prag dovodi platformu do gubitka više klijenata nego njeni konkurenti, što bi moglo ugroziti njenu održivost. Stoga je komplikovano za ove platforme da povećaju broj posmatranih skokova, a 4 je često dovoljan broj da se suprotstavi njihovim analizama.


Dakle, **najčešći slučaj upotrebe za Ricochet nastaje kada je potrebno prikriti prethodno učešće UTXO-a u CoinJoin-u koji pripada vama**. Idealno bi bilo izbegavati prenos bitkoina koji su prošli kroz CoinJoin ka regulisanim entitetima. Međutim, u slučaju da ne postoji druga opcija, posebno u hitnosti da se bitkoini pretvore u fiat valutu, Ricochet nudi efikasno rešenje.


## Kako funkcioniše Ricochet na Samourai novčaniku?

Ricochet je jednostavno metoda gde neko šalje bitkoine samom sebi. Stoga je potpuno moguće ručno simulirati Ricochet bez korišćenja specijalizovanog alata. Međutim, za one koji žele da automatizuju proces uz dobijanje uglađenijeg rezultata, Ricochet alat dostupan kroz aplikaciju Samourai novčanika je dobro rešenje.


Pošto se usluga plaća Samourai-u, Ricochet izaziva trošak od `100,000 satošija` kao naknadu za uslugu, pored rudarskih naknada. Stoga se njegova upotreba više preporučuje za transfere značajnih iznosa.


Samourai aplikacija nudi dve varijante Ricochet-a:


- Ojačani Ricochet, ili "isporuka u fazama," nudi prednost raspodele Samourai naknada za uslugu preko pet uzastopnih transakcija. Ova opcija takođe osigurava da je svaka transakcija emitovana u različito vreme i zabeležena u različitom bloku, što blisko oponaša ponašanje promene vlasništva. Iako sporija, ova metoda je poželjna za one koji nisu u žurbi, jer maksimizuje efikasnost Ricochet-a poboljšavajući njegovu otpornost na analizu lanca.
- Klasični Ricochet, koji je dizajniran da brzo izvrši operaciju emitovanjem svih transakcija u smanjenom vremenskom intervalu. Ova metoda, dakle, nudi manje privatnosti i niži otpor analizi u poređenju sa ojačanom metodom. Trebalo bi je preferirati samo za hitne transfere.


## Kako izvesti Ricochet na Samourai novčaniku?

Da biste izvršili Ricochet transakciju iz aplikacije Samourai novčanik, pratite naš video tutorijal:

![Ricochet YouTube video tutorial](https://youtu.be/Gsz0zuVo3N4)


Ako želite proučiti Ricochet transakcije izvedene u ovom vodiču, evo ih:


- Prva Ricochet transakcija: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://Mempool.space/fr/Testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Poslednja Ricochet transakcija: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://Mempool.space/fr/Testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)


**Spoljni resursi:**


- https://docs.samourai.io/en/Wallet/features/ricochet
