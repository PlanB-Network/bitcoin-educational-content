---
term: CoinJoin
---

CoinJoin je tehnika koja se koristi za prekidanje sledljivosti bitkoina. Oslanja se na kolaborativnu transakciju sa specifičnom strukturom istog imena: CoinJoin transakcija. CoinJoin transakcije pomažu u poboljšanju zaštite privatnosti korisnika Bitcoin tako što otežavaju eksternim posmatračima analizu transakcija. Ova struktura omogućava mešanje više novčića u jednoj transakciji, što otežava određivanje veza između ulaznih i izlaznih adresa.


Opšta operacija CoinJoin je sledeća: različiti korisnici koji žele da mešaju deponuju iznos kao ulaz transakcije. Ovi ulazi će izaći kao različiti izlazi istog iznosa. Na kraju transakcije, nemoguće je odrediti koji izlaz pripada kojem korisniku. Tehnički ne postoji veza između ulaza i izlaza CoinJoin transakcije. Veza između svakog korisnika i svakog UTXO je prekinuta, na isti način kao što je istorija svake kovanice.


![](../../dictionnaire/assets/4.webp)


Da bi se omogućio CoinJoin bez da bilo koji korisnik izgubi kontrolu nad svojim sredstvima u bilo kom trenutku, transakciju prvo konstruira koordinator, a zatim je prenosi svakom korisniku. Svaki korisnik zatim potpisuje transakciju na svojoj strani nakon što proveri da li mu odgovara, a zatim se svi potpisi dodaju transakciji. Ako korisnik ili koordinator pokuša da ukrade sredstva drugih menjajući izlaze CoinJoin transakcije, potpisi će biti nevažeći i transakcija će biti odbijena od strane čvorova. Kada se beleženje izlaza učesnika vrši korišćenjem Chaumovih slepih potpisa kako bi se izbegla veza sa ulazom, to se naziva "Chaumian CoinJoin".


Ovaj mehanizam povećava poverljivost transakcija bez potrebe za izmenama Bitcoin protokola. Specifične implementacije CoinJoin, kao što su Whirlpool, JoinMarket ili Wabisabi, nude rešenja za olakšavanje procesa koordinacije među učesnicima i poboljšanje efikasnosti CoinJoin transakcije. Evo primera CoinJoin transakcije:


```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```


Teško je sa sigurnošću utvrditi ko je prvi uveo ideju CoinJoin na Bitcoin, i ko je imao ideju korišćenja slepih potpisa Davida Chauma u ovom kontekstu. Često se smatra da je Gregory Maxwell prvi o tome diskutovao [u poruci na BitcoinTalk-u 2013. godine](https://bitcointalk.org/index.php?topic=279249.0):

Korišćenje Chaum slepih potpisa: Korisnici se povezuju i pružaju ulaze (i menjaju adrese) kao i kriptografski blinded verziju Address na koju žele da pošalju svoje privatne novčiće; server potpisuje tokene i vraća ih. Korisnici se anonimno ponovo povezuju, otkrivaju svoje izlazne adrese i šalju ih nazad serveru. Server može videti da su svi izlazi potpisani od strane njega i da, shodno tome, svi izlazi dolaze od validnih učesnika. Kasnije, ljudi se ponovo povezuju i potpisuju.

Maxwell, G. (2013, August 22). *CoinJoin: Bitcoin privatnost za stvarni svet*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0


Međutim, postoje raniji spomeni, kako za Chaum potpise u kontekstu mešanja, tako i za coinjoins. [U junu 2011, Duncan Townsend predstavlja na BitcoinTalk-u](https://bitcointalk.org/index.php?topic=12751.0) mikser koji koristi Chaum potpise na način vrlo sličan modernim Chaumian coinjoins. U istoj temi, postoji [poruka od hashcoin-a kao odgovor na Duncan Townsend-a](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) za poboljšanje njegovog miksera. Ova poruka predstavlja ono što najviše podseća na coinjoins. Takođe postoji pomen sličnog sistema u [poruci od Alex Mizrahi iz 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), dok je savetovao kreatore Tenebrix-a. Sam termin "CoinJoin" nije izmislio Greg Maxwell, već je potekao od ideje Petera Todda.


> ► *Termin "CoinJoin" nema francuski prevod. Neki bitkoineri takođe koriste termine "mix", "mixing" ili "mixage" da se odnose na CoinJoin transakciju. Mixing je zapravo proces koji se koristi u srži CoinJoin. Takođe, važno je ne mešati mixing kroz coinjoins sa mixingom kroz centralnog aktera koji preuzima bitkoine tokom procesa. Ovo nema veze sa CoinJoin gde korisnik ne gubi kontrolu nad svojim bitkoinima tokom procesa.*