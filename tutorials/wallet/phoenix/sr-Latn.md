---
name: Feniks
description: Instaliranje i korišćenje Phoenix Wallet
---
![cover](assets/cover.webp)


Phoenix je samostalni Lightning Wallet i čvor koji je razvila ACINQ, francuska kompanija specijalizovana za softverska rešenja zasnovana na Lightning mreži. Za razliku od kustodijalnih Lightning novčanika kao što su Wallet ili Satoshi, gde bitkoini drži treća strana, Phoenix omogućava korisnicima da zadrže potpunu kontrolu nad svojim privatnim ključevima.


Phoenix funkcioniše kao pravi Lightning čvor ugrađen u vaš telefon, automatski otvarajući kanal sa ACINQ-ovim Lightning čvorom. Aplikacija je zasnovana na Lightning-KMP, multiplatformskoj implementaciji Lightning Network u Kotlinu, optimizovanoj za mobilne novčanike. Za razliku od drugih rešenja za Lightning čvorove, Phoenix u velikoj meri pojednostavljuje upravljanje. Korisnik ne mora da se bavi otvaranjem i zatvaranjem kanala, pokretanjem Bitcoin čvora ili upravljanjem likvidnošću na Lightning Network. Phoenix se brine o svim tim tehničkim operacijama u pozadini.


Ova aplikacija kombinuje jednostavnost korišćenja i pogodnost mobilnih Lightning novčanika sa sigurnošću i suverenitetom pravog ličnog Lightning čvora. Phoenix omogućava sigurno, efikasno i autonomno korišćenje Lightning Network, uz uživanje u fluidnom, intuitivnom korisničkom iskustvu.


Zauzvrat, primenjuju se određene naknade:




- Slanje putem Lightning-a košta 0.4% od iznosa plus 4 Sats ;
- Ako je potreban keš za primanje putem Lightning-a, naplaćuje se 1% iznosa;
- Svaki kanal košta 1000 Sats za otvaranje.


Po mom mišljenju, Phoenix predstavlja odlično srednje rešenje između kustodijalnih Lightning portfolija i ručnog upravljanja Lightning čvorom. Ova aplikacija je podjednako pogodna za početnike i napredne korisnike koji ne žele da se bave detaljima upravljanja sopstvenim LND ili Core Lightning. Hajde da saznamo kako da je koristimo!


![Image](assets/fr/01.webp)


## Instaliraj aplikaciju


Idite u svoju prodavnicu aplikacija i instalirajte Phoenix :




- Na [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.Mainnet);
- Na [App Store](https://apps.apple.com/fr/app/phoenix-Wallet/id1544097028?l=en-GB).


![Image](assets/fr/02.webp)


Možete takođe instalirati aplikaciju [pomoću apk fajla na njihovom GitHub repozitorijumu](https://github.com/ACINQ/phoenix/releases).


![Image](assets/fr/03.webp)


## Kreiranje portfolija


Kada se aplikacija pokrene, kliknite na dugme "*Next*" da preskočite prezentaciju, zatim na "*Start*".


![Image](assets/fr/04.webp)


Odaberite "*Kreiraj novi Wallet*".


![Image](assets/fr/05.webp)


I to je to, vaš Lightning Wallet i čvor su sada kreirani.


![Image](assets/fr/06.webp)


## Sačuvaj Mnemonic frazu


Pre nego što počnemo, potrebno je da sačuvamo našu 12-rečnu Mnemonic frazu. Ova fraza omogućava potpun, neograničen pristup svim vašim bitcoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem telefonu.


Fraza od 12 reči vraća pristup vašim bitcoinima u slučaju gubitka, krađe ili oštećenja vašeg telefona. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.


Možete ga napisati na papir ili, radi dodatne sigurnosti, ugravirati na nerđajući čelik kako biste ga zaštitili od požara, poplave ili urušavanja. Izbor medija za vaš Mnemonic zavisiće od vaše sigurnosne strategije, ali ako koristite Phoenix kao potrošački portfelj koji sadrži umerene iznose, papir bi trebao biti dovoljan.


Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Kliknite na poruku prikazanu na vrhu Interface "*Sačuvaj svoj Wallet...*".


![Image](assets/fr/07.webp)


Zatim kliknite na "*Save my Wallet*".


![Image](assets/fr/08.webp)


Zatim kliknite na "*View my key*" i sačuvajte svoju Mnemonic frazu na fizičkom mediju.


![Image](assets/fr/09.webp)


Označite dva polja na dnu Interface da potvrdite da je rezervna kopija uspešno završena.


![Image](assets/fr/10.webp)


## Postavljanje aplikacije


Pre nego što obavite svoje prve transakcije, možete prilagoditi postavke klikom na ikonu zupčanika u donjem levom uglu Interface.


![Image](assets/fr/11.webp)


U meniju "*Display*" možete izabrati temu aplikacije, oznaku korišćenu za Bitcoin i vašu lokalnu fiat valutu.


![Image](assets/fr/12.webp)


U "*Opcije plaćanja*", pronaći ćete razne napredne postavke za Lightning plaćanja. Možete zadržati podrazumevane postavke.


![Image](assets/fr/13.webp)


U "*Upravljanje kanalima*", postavite maksimalnu naknadu koju ste spremni da platite prilikom otvaranja Lightning kanala.


![Image](assets/fr/14.webp)


U meniju "*Access control*" toplo preporučujem da aktivirate sistem autentifikacije kako biste osigurali pristup aplikaciji na vašem telefonu. Ovo će sprečiti bilo koga ko ima pristup vašem otključanom telefonu da pristupi Phoenix-u i ukrade vaše bitkoine.


![Image](assets/fr/15.webp)


U meniju "*Electrum server*", ako imate Electrs server, možete ga povezati da emitujete vaše transakcije.


![Image](assets/fr/16.webp)


Da biste poboljšali poverljivost svojih veza, omogućite veze putem Tor-a u meniju "*Tor*". Iako korišćenje Tor-a može malo usporiti vaše uplate i zahteva da Phoenix aplikacija bude otvorena u prvom planu prilikom primanja, značajno povećava vašu privatnost.


![Image](assets/fr/17.webp)


## Primite bitkoine On-Chain


Prilikom prve upotrebe, imate opciju da napunite svoj Phoenix Wallet sa sredstvima sa On-Chain. Takođe možete izvršiti ovaj prvi depozit direktno sa Lightning-a (pogledajte sledeći odeljak), ali u oba slučaja će se primeniti dodatne naknade za otvaranje vašeg prvog kanala.


Kliknite na dugme "*Receive*".


![Image](assets/fr/18.webp)


Prevucite QR kod udesno da otkrijete Bitcoin koji prima Address. Pošaljite iznos koji želite da položite sa Phoenix.


![Image](assets/fr/19.webp)


Iznos primljen On-Chain će se prvo pojaviti kao na čekanju u okviru stanja vašeg portfolija. Biće potrebne 3 potvrde pre nego što sredstva budu dostupna za korišćenje.


![Image](assets/fr/20.webp)


Jednom kada sredstva budu primljena, Phoenix automatski otvara Lightning kanal za vas. Sada možete slati i primati bitkoine putem Lightning Network.


![Image](assets/fr/21.webp)


## Primite bitkoine putem Lightning-a


Da biste primili Sats putem Lightning Network, kliknite na dugme "*Receive*".


![Image](assets/fr/22.webp)


Fenix generiše Lightning Invoice. Možete ga ili skenirati ili poslati osobi koja želi da vam prenese Sats.


![Image](assets/fr/23.webp)


Klikom na dugme "*Edit*", možete dodati opis koji će biti vidljiv platiocu na Invoice, i definisati određeni iznos koji platioc mora poslati.


![Image](assets/fr/24.webp)


Klasične fakture pomenute gore mogu se koristiti samo jednom. Za opciju plaćanja koja se može ponovo koristiti, možete koristiti svoj višekratni QR kod, koji je BOLT12 ponuda.


![Image](assets/fr/25.webp)


Jednom kada ponuda Invoice ili BOLT12 bude rešena, transakcija će se pojaviti na vašem Lightning Wallet.


![Image](assets/fr/26.webp)


## Pošalji bitkoine putem Lightning-a


Sada kada imate Sats na Phoenixu, spremni ste za plaćanja putem Lightning Network. Počnite klikom na dugme "*Send*".


![Image](assets/fr/27.webp)


Na raspolaganju vam je nekoliko opcija. Klikom na "*Skeniraj QR kod*", možete skenirati Lightning Invoice, BOLT12 ponudu, ili čak primanje Address za On-Chain uplatu.


![Image](assets/fr/28.webp)


Informacije možete uneti i ručno putem tastature u polje na vrhu Interface, ili uneti Lightning Address (BOLT12 ili LNURL). Takođe možete direktno nalepiti informacije koristeći dugme "*Paste*".


![Image](assets/fr/29.webp)


Za ovaj primer, skenirao sam Invoice za 10,000 Sats. Da biste izvršili uplatu, samo kliknite na "*Plati*".


![Image](assets/fr/30.webp)


Transakcija je završena.


![Image](assets/fr/31.webp)


Čestitamo, sada znate kako da konfigurišete i koristite Phoenix. Ako vam je ovaj vodič bio koristan, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala što delite!


Da biste stvari podigli na viši nivo, pogledajte ovaj vodič na Alby Hub-u, još jedno inovativno i jednostavno rešenje za pokretanje sopstvenog Lightning čvora:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

A da biste saznali više o tehničkom radu Lightning Network, možete pronaći odličnu besplatnu obuku Fanisa Mihalakisa o Plan ₿ Network :


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb