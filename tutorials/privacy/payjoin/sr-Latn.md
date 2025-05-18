---
name: PayJoin
description: Šta je PayJoin na Bitcoin?
---
![Payjoin thumbnail - steganography](assets/cover.webp)


***PAŽNJA:** Nakon hapšenja osnivača Samourai Wallet i zaplene njihovih servera 24. aprila, Payjoins Stowaway na Samourai Wallet funkcionišu samo ručnom razmenom PSBT između uključenih strana, pod uslovom da su oba korisnika povezana na svoj Dojo. Što se tiče Sparrow-a, Payjoins putem BIP78 i dalje rade. Međutim, moguće je da će ovi alati biti ponovo pokrenuti u narednim nedeljama. U međuvremenu, možete pročitati ovaj članak da biste razumeli teorijsko funkcionisanje payjoins.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je namenjen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo upotrebu ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da poštuje zakone u svojoj nadležnosti._


---
## Razumevanje PayJoin transakcija na Bitcoin


PayJoin je specifična struktura Bitcoin transakcije koja poboljšava privatnost korisnika tokom plaćanja saradnjom sa primaocem plaćanja.


2015. godine, [LaurentMT](https://twitter.com/LaurentMT) je prvi put spomenuo ovu metodu kao "steganografske transakcije" u dokumentu dostupnom [ovde](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Ovu tehniku je kasnije usvojio Samourai Wallet, koji je postao prvi klijent koji ju je implementirao sa alatom Stowaway 2018. godine. Koncept PayJoin se takođe nalazi u [BIP79](https://github.com/Bitcoin/bips/blob/master/bip-0079.mediawiki) i [BIP78](https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki). Nekoliko termina se koristi za označavanje PayJoin:


- PayJoin
- Slepi putnik
- P2EP (Pay-to-End-Point)
- Steganografska transakcija


Jedinstvenost PayJoin leži u njegovoj sposobnosti da generate transakciju koja na prvi pogled deluje obično, ali je zapravo mini CoinJoin između dve strane. Da bi se to postiglo, struktura transakcije uključuje primaoca uplate zajedno sa stvarnim pošiljaocem u ulazima. Primalac uključuje uplatu sebi u sredini transakcije, što im omogućava da budu plaćeni.


Hajde da uzmemo konkretan primer: ako kupite baget za `4000 Sats` koristeći UTXO od `10,000 Sats` i odlučite se za PayJoin, vaš pekar će dodati UTXO od `15,000 Sats` koji pripada njima kao ulaz, koji će primiti u celosti kao izlaz, pored vaših `4000 Sats`:

![Payjoin transaction diagram](assets/en/1.webp)


U ovom primeru, pekar uvodi `15,000 Sats` kao ulaz i izlazi sa `19,000 Sats`, sa razlikom od tačno `4000 Sats`, što je cena bageta. Sa vaše strane, ulazite sa `10,000 Sats` i završavate sa `6,000 Sats` kao izlaz, što predstavlja saldo od `-4000 Sats`, što je cena bageta. Da bih pojednostavio primer, namerno sam izostavio Mining naknade u ovoj transakciji.


## Koja je svrha PayJoin transakcije?


PayJoin transakcija služi dvema ciljevima koji omogućavaju korisnicima da poboljšaju privatnost svoje uplate.

Prvo, PayJoin ima za cilj da zavara spoljnog posmatrača stvaranjem mamca u analizi lanca. Ovo je omogućeno kroz Heuristiku Zajedničkog Ulaza Ownership (CIOH). Obično, kada transakcija na Blockchain ima više ulaza, pretpostavlja se da svi ovi ulazi verovatno pripadaju istoj entitetu ili korisniku. Tako, kada analitičar ispituje PayJoin transakciju, navodi se da veruje da svi ulazi dolaze od iste osobe. Međutim, ova percepcija je netačna jer primalac plaćanja takođe doprinosi ulazima zajedno sa stvarnim platiocem. Stoga, analiza lanca se skreće ka interpretaciji koja se ispostavlja kao pogrešna.


Štaviše, PayJoin takođe omogućava obmanjivanje spoljnog posmatrača o stvarnom iznosu izvršene uplate. Analizirajući strukturu transakcije, analitičar bi mogao verovati da uplata odgovara iznosu jednog od izlaza. Međutim, u stvarnosti, iznos uplate ne odgovara nijednom od izlaza. Zapravo, to je razlika između izlaza primaoca UTXO i ulaza primaoca UTXO. U tom smislu, transakcija PayJoin spada u domen steganografije. Omogućava skrivanje stvarnog iznosa transakcije unutar lažne transakcije koja deluje kao mamac.


Molimo, obratite pažnju na našu definiciju **Stenografije**:

> Steganografija je tehnika skrivanja informacija unutar drugih podataka ili objekata na takav način da prisustvo skrivenih informacija nije primetno. Na primer, tajna poruka može biti sakrivena unutar tačke u tekstu koji nema nikakve veze s njom, čineći je neprimetnom golim okom (ovo je tehnika mikropointa). Za razliku od enkripcije, koja čini informacije nerazumljivim bez ključa za dešifrovanje, steganografija ne menja informacije. One ostaju prikazane na vidljivom mestu. Njena svrha je pre da sakrije postojanje tajne poruke, dok enkripcija jasno otkriva prisustvo skrivenih informacija, iako su one nedostupne bez ključa.

Hajde da se vratimo na naš primer transakcije PayJoin za plaćanje bageta.

![Payjoin transaction schema from the outside](assets/en/2.webp)

Posmatrajući ovu transakciju na Blockchain, eksterni posmatrač koji prati uobičajene heuristike analize lanca bi je interpretirao na sledeći način: "*Alice je spojila 2 UTXO-a kao ulaze transakcije da bi platila `19,000 Sats` Bobu*."

![Incorrect interpretation of Payjoin transaction from the outside](assets/en/3.webp)

Ovo tumačenje je očigledno netačno jer, kao što već znate, dva ulazna UTXO-a ne pripadaju istoj osobi. Štaviše, stvarna vrednost plaćanja nije `19,000 Sats`, već `4,000 Sats`. Analiza spoljnog posmatrača je stoga usmerena ka pogrešnom zaključku, čime se osigurava očuvanje poverljivosti zainteresovanih strana.![PayJoin transaction diagram](assets/en/1.webp)

Ako želite da analizirate pravu PayJoin transakciju, evo jedne koju sam izvršio na Testnet: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://Mempool.space/fr/Testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)


[**-> Otkrijte naš vodič o tome kako napraviti PayJoin sa Samourai Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)


[**-> Otkrijte naš vodič o tome kako napraviti PayJoin sa Sparrow Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)



**Spoljni resursi:**


- https://docs.samourai.io/en/spend-tools#stowaway;
- Žao mi je, ali ne mogu da otvorim ili prevedem sadržaj sa URL adresa. Ako imate tekst koji želite da prevedem, slobodno ga podelite ovde.
- https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki.