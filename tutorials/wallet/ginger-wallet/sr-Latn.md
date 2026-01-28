---
name: Ginger Wallet
description: Open-source, self-custody Bitcoin wallet software, fork from Wasabi Wallet, integrating Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet je open source, ne-kustodijalni Bitcoin portfelj fokusiran na poverljivost i privatnost. Počeo je kao fork iz Wasabi Wallet (nakon verzije 2.0.7.2 - MIT licenca).



Ginger Wallet zadržava tehničku arhitekturu Wasabi-ja dok dodaje nekoliko specifičnih funkcija. Prema [dokumentaciji Ginger Wallet](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), Wasabi naglašava **autonomiju i kontrolu**, dok se Ginger fokusira na **jednostavnost korišćenja, sigurnost i pojednostavljeno iskustvo**, čineći ga pristupačnim za one manje upoznate sa tehničkim aspektima.



Ginger Wallet je wallet softver samo za računare (nema mobilnu aplikaciju).



## Šta je Coinjoin?



**Coinjoin** je posebna struktura transakcije Bitcoin koja okuplja nekoliko učesnika u jednoj zajedničkoj transakciji. Ovaj mehanizam meša unose različitih korisnika u zajedničku transakciju, čineći izuzetno teškim - ako ne i često nemogućim, ako se pravilno izvede - praćenje sredstava. Kao rezultat, postaje gotovo nemoguće za spoljnog posmatrača da sa sigurnošću identifikuje poreklo i odredište bitkoina uključenih u transakciju, za razliku od konvencionalnih Bitcoin transakcija.



Za vas, kao korisnika, coinjoin pomaže u očuvanju vaše poverljivosti. Na primer, ako primite donaciju od 10,000 sats na Bitcoin adresu, pošiljalac može pratiti ova sredstva i, u nekim slučajevima, zaključiti da posedujete veću količinu bitcoina, ili posmatrati vaše aktivnosti. Praveći coinjoin nakon ove donacije od 10,000 sats, prekidate mogućnost praćenja: pošiljalac više neće moći da izvuče bilo kakve informacije o vama iz ove uplate.



Chaumian coinjoin nudi visok nivo sigurnosti, jer sredstva ostaju pod isključivom kontrolom korisnika u svakom trenutku. Čak ni operateri koordinirajućih servera ne mogu preusmeriti bitkoine učesnika ni pod kojim okolnostima. Ni korisnici ni koordinatori ne moraju verovati jedni drugima: svaki zadržava kontrolu nad svojim privatnim ključevima i ostaje isključivo ovlašćen da validira transakcije. Nijedna treća strana stoga ne može prisvojiti vaše bitkoine tokom coinjoin-a, niti uspostaviti direktnu vezu između vaših ulaza i izlaza.



Da biste saznali više o coinjoin-u, pogledajte BTC 204 kurs na Plan ₿ Akademiji :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Instaliraj Ginger Wallet



Da biste instalirali Ginger Wallet, posetite veb-sajt [Ginger Wallet](https://gingerwallet.io).



Pritisnite **Download** da preuzmete odgovarajuću verziju za vaš računar (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Druga opcija je da odete na [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) projekta da biste ga preuzeli.



![screen](assets/fr/04.webp)



Zatim pokrenite instalacioni program.



![screen](assets/fr/05.webp)




## Postavke parametara



### Preliminarne konfiguracije



Otvorite Ginger Wallet, izaberite željeni jezik.



![screen](assets/fr/06.webp)



Od samog početka, Ginger vas podseća na troškove uključene u coinjoin proces.



![screen](assets/fr/07.webp)



Zatim pritisnite **Start**, zatim **New** da kreirate novi portfolio.



![screen](assets/fr/08.webp)



Dalje, sačuvaj i potvrdi svoj seedphrase.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Za dodatnu sigurnost, Ginger Wallet vam daje opciju dodavanja passphrase.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Ovaj passphrase, kada se doda, biće tražen svaki put kada pokušate da pristupite svom portfoliju.



![screen](assets/fr/12.webp)



Ginger automatski aktivira podrazumevani **Coinjoin** kada kreirate svoj portfolio. O tome ste obavešteni i zatim možete prilagoditi podešavanje prema svojim potrebama.



![screen](assets/fr/13.webp)




### Opšta podešavanja



Kada kreirate svoj prvi portfolio, bićete preusmereni na Ginger Wallet interfejs.



![screen](assets/fr/14.webp)



Aktivirajte **Diskretni režim**, ako želite da sakrijete stanja u vašim novčanicima.



![screen](assets/fr/15.webp)



Možete kreirati više portfolija na Ginger Wallet. Samo kliknite na **Dodaj portfolio**.



![screen](assets/fr/16.webp)



Ginger podržava upotrebu hardverskih portfolija putem standardnog Bitcoin Core interfejsa, iako direktna integracija iz ili u hardverski portfolio još nije dostupna.



Kompatibilni hardverski portfoliji uključuju (ali nisu ograničeni na) :




- Blockstream Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- itd.



Sada kliknite na **Settings**.



![screen](assets/fr/17.webp)



Ova podešavanja su ona aplikacije uopšte, i konfiguracije koje napravite tamo će se primeniti na sve portfelje.



U **Postavkama**, imate kartice :





- General**



![screen](assets/fr/18.webp)





- Izgled



Na ovoj kartici možete promeniti jezik, valutu i jedinicu prikaza naknade (BTC/Satoshi), između ostalog.



![screen](assets/fr/19.webp)





- Bitcoin**



Ova kartica vam omogućava da omogućite Bitcoin Knots da se pokrene pri pokretanju aplikacije, izaberete vašu mrežu (Main/RegTest), i vašeg provajdera stope naplate (Mempool Space/Blockstream info/Full Node), itd.



![screen](assets/fr/20.webp)





- Bezbednosne funkcije**



Na kartici Bezbednost, možete omogućiti dvofaktorsku autentifikaciju, aktivirati ili deaktivirati Tor, pa čak i onemogućiti ga kada se aplikacija Ginger zatvori.



![screen](assets/fr/21.webp)



**NB** :




- Za dvofaktorsku autentifikaciju, uverite se da vaša aplikacija za autentifikaciju podržava SHA256 protokol i 8-cifrene kodove. Ginger Wallet zahteva 8-cifreni 2FA kod kako bi poboljšao bezbednost. Ovaj duži format čini kod mnogo težim za pogađanje ili kompromitovanje, nudeći veću zaštitu protiv neovlašćenog pristupa.
- Podrazumevano, sav saobraćaj Ginger mreže prolazi kroz Tor, eliminišući potrebu za ručnom konfiguracijom. Ako je Tor već aktivan na vašem sistemu, Ginger će mu automatski dati prioritet.



Ali kada deaktivirate Tor u postavkama, vaša privatnost ostaje uglavnom očuvana, osim u dve situacije:




- tokom Coinjoin-a, koordinator bi mogao povezati vaše ulaze i izlaze sa vašom IP adresom;
- kada emitujete transakciju, zlonamerni čvor na koji se povezujete mogao bi da poveže vašu transakciju sa vašom IP adresom.



Ne zaboravite da pritisnete **Done** (u donjem desnom uglu) svaki put, da biste sačuvali svoja podešavanja. Neka podešavanja zahtevaju da Ginger Wallet bude restartovan kako bi stupila na snagu.



Pored toga, traka za pretragu na vrhu portfolija omogućava vam da pretražujete i pristupate bilo kojem parametru, itd...



![screen](assets/fr/22.webp)




### Konfiguracija portfolija



Nekoliko portfolija može biti kreirano u aplikaciji, tako da svaki portfolio može biti konfigurisan prema vašim potrebama. Da biste to uradili, kliknite na **tri tačke** ispred imena portfolija, zatim na **Podešavanja portfolija**.



![screen](assets/fr/23.webp)



Kao što možete videti, osim parametra wallet, moći ćete da vidite svoje UTXO-e (spisak tokena koje posedujete), statistike i informacije o wallet (na primer, prošireni javni ključ).



Da biste se vratili na konfiguraciju portfolija, kada kliknete na parametre portfolija, bićete preusmereni na sledeće kartice:




- General** (gde možete promeniti ime portfolija) ;



![screen](assets/fr/24.webp)





- Coinjoin** (gde možete prilagoditi postavke za coinjoin za ovaj wallet) ;



![screen](assets/fr/25.webp)





- Alati** (gde možete proveriti svoj seedphrase, ponovo sinhronizovati svoj portfolio ili ga izbrisati).



![screen](assets/fr/26.webp)




## Primite bitkoine



![video](https://youtu.be/cqv35wBDWMQ)



Da biste primili bitkoine u vaš wallet na Ginger Wallet:




- pritisnite **Receive** ;



![screen](assets/fr/27.webp)





- Unesite ime izvora sa kojim želite da povežete adresu. Ovo je označavanje za praćenje vaših uplata. Ovo nema on-chain implikacije; to je jednostavno informacija o sledljivosti koja se čuva lokalno u vašoj aplikaciji;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- kliknite na malu strelicu levo od **Generate** da biste izabrali format adrese (**SegWit** /**Taproot**), zatim kliknite na **Generate**, da biste generate generisali adresu i QR kod.



![screen](assets/fr/29.webp)



Ovu adresu ili QR kod će vaš pošiljalac koristiti da vam pošalje bitkoine.



![screen](assets/fr/30.webp)




## Pošalji bitkoine




![video](https://youtu.be/2nf5aAimfhg)



Da uradiš ovo :




- Pritisnite dugme **Pošalji**;
- unesite adresu primaoca, iznos koji se šalje i oznaku;
- proveri pregled transakcije i potvrdi slanje.



![screen](assets/fr/31.webp)




## Potroši bitkoine



Lako je kupiti i prodati Bitcoin sa Ginger Wallet. U samo nekoliko koraka, možete potrošiti svoje bitkoine.



### Kupi bitkoine



![video](https://youtu.be/lEqTBzm5MEA)



Korisnici Ginger Wallet mogu kupiti bitkoine.





- Pritisnite dugme **Kupi**. Ovo dugme ostaje vidljivo čak i ako je wallet prazan.



![screen](assets/fr/32.webp)





- Izaberite svoju zemlju, ili čak svoju državu (u nekim regionima, kao što je Kanada), pre nego što nastavite sa kupovinom bitkoina. Zapravo, kada prvi put kliknete na funkciju **Kupi**, takođe ćete morati da navedete svoj region.



![screen](assets/fr/33.webp)



Pritisnite **Nastavi** da biste nastavili kroz proces kupovine.





- Zatim unesite iznos bitkoina koji želite da kupite u predviđeno polje. Takođe možete izabrati valutu transakcije.



![screen](assets/fr/34.webp)



Svaka valuta ima minimalni i maksimalni limit kupovine. Na primer, u USD, maksimalni limit je $30,000.



Ako ste već obavili kupovinu, možete pogledati istoriju transakcija klikom na dugme **Prethodne narudžbine**. Prikazaće se lista prošlih transakcija i njihov status.





- Izaberite ponudu koja vam odgovara.



U ovom trenutku, videćete listu svih dostupnih ponuda. Za svaku ponudu, imate :




 - ime dobavljača (1) ;
 - broj bitkoina ekvivalentan prethodno unetom iznosu, način plaćanja i naknada za kupovinu (2) ;
 - dugme **Prihvati** (3).



![screen](assets/fr/35.webp)



Naknade navedene u ponudi ne predstavljaju dodatni trošak. One su već uključene u ukupan iznos ponude.



Gornji desni ugao ekrana, označen kao **Sve**, omogućava vam da filtrirate ponude prema načinu plaćanja. Vaš odabrani način plaćanja biće postavljen kao podrazumevani, ali se može promeniti u bilo kom trenutku.



![screen](assets/fr/36.webp)



Ako pronađete odgovarajuću ponudu, kliknite na dugme **Prihvati** da biste nastavili sa kupovinom. Zatim ćete biti preusmereni na stranicu prodavca, gde možete završiti transakciju.



### Prodaja bitkoina



Korisnici Ginger Wallet mogu prodati Bitcoin. Dugme **Prodaj** je vidljivo samo kada su sredstva dostupna u portfoliju.





- Kliknite na **Prodaj**.



![screen](assets/fr/37.webp)





- Kao i kod opcije **Buy**, kada prvi put koristite funkciju Sell, morate odabrati svoju zemlju pre nego što nastavite sa prodajom bitcoina.





- Zatim, treba da unesete količinu Bitcoina koju želite da prodate. Možete uneti ovu količinu u BTC ili u fiat valuti kao što je američki dolar (USD).





- Kada to uradite, videćete listu dostupnih ponuda. Izaberite prodajnu ponudu koja vam odgovara, zatim kliknite na **Prihvati** da nastavite.





- Sada treba da finalizujete transakciju:
 - Jednom kada prihvatite ponudu, bićete preusmereni na stranicu dobavljača;
 - Pratite uputstva na stranici dobavljača ;
 - U nekom trenutku, dobićete adresu primaoca i tačan iznos za slanje;
 - Zatim se vratite na Ginger Wallet da nastavite proces;
 - Kada se vratite u Ginger Wallet, pojaviće se dijalog prozor koji vam omogućava da nastavite klikom na **Pošalji**.



Ovo će otvoriti ekran **Pošalji** sa unapred popunjenom adresom primaoca i iznosom. Takođe možete koristiti dugme **Pošalji** na početnom ekranu. Iako možete ručno poslati transakciju, preporučujemo da je završite putem dijaloga za optimizovan proces.



## Pravljenje coinjoin-a na Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Zaštitite poverljivost svojih bitkoina pomoću **Coinjoin**, direktno integrisanog u Ginger Wallet. wallet koristi **WabiSabi**, Chaumian coinjoin protokol dizajniran da olakša pristupačnije i efikasnije coinjoin-ove.



Na vama je da izaberete strategiju coinjoin-a (automatsku ili ručnu) koja vam najviše odgovara.



Ginger Coinjoin je spreman za korišćenje čim ga preuzmete (nisu potrebni dodatni koraci). Automatski, Ginger Coinjoin radi u pozadini kako bi zaštitio vašu privatnost pri svakoj transakciji. U praksi, Coinjoin igrač će se pojaviti kad god imate saldo koji može biti anonimizovan.



Što se tiče ručnog pokretanja coinjoin-a, to je operacija na jedan klik. Pokrenite rundu i sačekajte da se coinjoin transakcija izgradi i potvrdi. Videćete rezultat anonimizacije u interfejsu.



Nekoliko mešanja se može izvršiti dok se ne postigne željeni nivo anonimnosti. Takođe možete isključiti određene delove iz mešanja.



Podrazumevano, Ginger koristi sopstvenog koordinatora sa svim unapred konfiguriranim parametrima i garantovanim naknadama. Coinjoin transakcije tokena vrednih više od 0.03 BTC podrazumevaju naknadu koordinatora od 0.3% pored mining naknade. Unosi od 0.03 BTC ili manje, kao i remiksi, oslobođeni su naknada koordinatora, čak i nakon jedne transakcije. Stoga, plaćanje izvršeno Coinjoin sredstvima omogućava i pošiljaocu i primaocu da remiksuju svoje novčiće bez dodatnih naknada koordinatora.



Ginger preferira coinjoin-ove sa više učesnika nego manje, brže runde. Veći coinjoin-ovi nude više anonimnosti, niže troškove i veću efikasnost prostora bloka.




## Bezbednost i najbolje prakse



Želja za decentralizacijom i očuvanjem privatnosti zahteva usvajanje nekoliko najboljih praksi:




- Uvek čuvajte svoj seedphrase na sigurnom mestu van mreže;
- Ako izgubite računar ili sumnjate na neovlašćen pristup, odmah kreirajte novi wallet. Prenesite svoja sredstva u ovaj novi portfelj i obrišite stari;
- Koristite različitu adresu za svaki prijem kako biste izbegli ponovno korišćenje adresa;
- Uvek preuzimajte aplikacije za svoj portfolio isključivo sa zvaničnog GitHub naloga ili zvanične veb stranice.



Sada ste upoznati sa korišćenjem aplikacije Ginger Wallet za slanje, primanje i trošenje vaših bitkoina.



Ako ste našli ovaj vodič korisnim, molim vas ostavite mi zeleni palac ispod. Slobodno podelite ovaj članak putem vaših društvenih mreža. Hvala vam puno!



Takođe predlažem da pogledate ovaj vodič o tome kako koristiti Liana računarsku aplikaciju za slanje i primanje bitkoina, kao i implementaciju automatizovanog plana imovine.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04