---
name: Mempool
description: Istražite čitav ekosistem Bitcoin.
---

![cover](assets/cover.webp)



Protokol Bitcoin je pseudoniman, decentralizovan mreža otvorena za konsultacije. Članovi (čvorovi), tj. računari sa instancom Bitcoin softvera, imaju neograničen pristup svim podacima objavljenim na Bitcoin. Međutim, u ranim godinama Bitcoin, protokol nije bio tako široko dostupan kao što je danas.


U ranim danima Bitcoin, bilo je neophodno pokrenuti Bitcoin čvor kako bi se pristupilo odgovarajućim alatima (bitcoin-cli) za ispitivanje mreže putem komandnih linija.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Pokrenuti su projekti za proširenje Bitcoin zajednice, čineći je dostupnijom svima koji ne poseduju čvor i/ili nemaju potrebne tehničke veštine.



U ovom vodiču ćemo pogledati projekat **Mempool.space**, njegove karakteristike i uticaj koji je imao na ekosistem Bitcoin.



## Šta je Mempool.space?



**Mempool.space** je open-source explorer koji pruža korisne informacije o transakcijama, naknadama za transakcije, blokovima i rudarima na različitim Bitcoin protokol mrežama. Pokrenut 2020. godine, donosi značajno poboljšanje korisničkog iskustva kroz reprezentativne grafike, glatke animacije i pregledne interfejse.



Da biste razumeli projekat, Mempool (memorijski bazen) je virtuelni prostor u kojem se čuvaju sve transakcije koje čekaju potvrdu na Bitcoin mreži. Mempool je poput "čekaonice" gde Bitcoin transakcije čekaju da budu potvrđene. Svaki računar na mreži (čvor) ima svoju čekaonicu, što objašnjava zašto nisu sve transakcije vidljive svima u isto vreme.



Glavni uticaj platforme u ekosistemu Bitcoin je što vam omogućava pristup raznovrsnim informacijama u memorijskim oblastima većine čvorova prisutnih na Bitcoin bez potrebe da pokrećete jedan. Mempool.space je repozitorijum za pregledanje i pretraživanje Bitcoin protokol mreža.



Sve šira upotreba u ekosistemu i činjenica da je Mempool.space otvorenog koda omogućili su njegovo integrisanje u sve više ličnih hosting sistema. Sada možete imati svoju instancu Mempool.space direktno na svom ličnom čvoru. Pogledajte naš vodič o konfigurisanju Mempool.space na vašem Umbrel čvoru ispod.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Osnove Mempool.space



Kao što je gore pomenuto, [Mempool.space](https://Mempool.space) je Bitcoin protokol istraživač koji vam omogućava da pratite vaše transakcije i njihovu propagaciju na odabranoj Bitcoin mreži u realnom vremenu, sa grafičkog Interface.



Mempool.space podržava mnoge mreže Bitcoin protokola.


U traci menija, pronaći ćete sledeće mreže:




- Mainnet** : Glavna Bitcoin mreža gde se odvijaju stvarne Bitcoin transakcije.
- Signet**: Test mreža koja koristi digitalne potpise za validaciju blokova bez potrebe za resursima koje zahteva glavna mreža.
- Testnet 3**: Mreža za testiranje i razvoj bez rizika na Bitcoin protokolu.
- Testnet 4** : Nova verzija Testnet 3 donosi veću stabilnost i nova pravila konsenzusa u testno okruženje.



![reseaux](assets/fr/01.webp)



Na početnoj stranici, sa leve strane u Green, videćete moguće buduće blokove (grupe transakcija) spremne za validaciju i integraciju (rudarenje) u Bitcoin mrežu. U proseku, blok se rudari svakih deset minuta: sačuvajte ovu informaciju, jer će biti korisna kasnije u našem razvoju.


U purpurnoj boji, na desnoj strani, pronaći ćete nedavno iskopane blokove na Bitcoin, pri čemu broj poslednjeg iskopanog bloka predstavlja trenutnu visinu mreže.



![blocs](assets/fr/02.webp)



Deo **Naknade za transakcije** je procenitelj naknada za transakcije. Što su veće naknade dodeljene vašoj transakciji, veća je verovatnoća da će vaša transakcija biti dodata u sledeći blok spreman za rudarenje.


Naknade za transakcije predstavljaju trošak koji će Miner uzeti od vas da bi ubacio vašu transakciju u kandidatski blok za Mining. Definiše se odnosom sat/vB (Satoshi/Virtual Bytes) koji predstavlja broj satoshija koje plaćate za prostor koji će vaša transakcija zauzeti u kandidatskom bloku.



⚠️ VAŽNO: U slučaju zasićenja Mempool, rudari daju prioritet transakcijama koje nude najbolji Satoshi/vByte odnos. Što je vaša transakcija teža (veća), to će joj biti potrebno više satoshija da bi bila brzo uključena.



![fees-visualizer](assets/fr/03.webp)



Deo **Mempool Goggles** omogućava vam da vizualizujete prostor koji zauzima transakcija.



![mempool](assets/fr/04.webp)



Blok se rudari otprilike svakih deset minuta zbog težine Proof of Work koju rudari moraju obezbediti da bi dodali svoj kandidatski blok u lanac izrudarenih blokova. Ova težina varira svakih **2016 blokova**, što je ekvivalentno otprilike **2 nedelje**. Evoluciju ove težine možete videti ovde.



![difficulty](assets/fr/05.webp)



Dodavanje novog bloka glavnom lancu daje Miner validiranog bloka pravo na nagradu koja se sastoji od fiksnog dela (prepolovljenog svakih 210.000 blokova**, što je ekvivalentno otprilike 4 godine** tokom prepolovljavanja) i naknada za transakcije.



![halving](assets/fr/06.webp)



## Pristupite detaljima transakcije



U traku za pretragu Mempool.space možete uneti svoj Bitcoin Address ili svoj transaction ID da biste saznali više o svojoj istoriji.



![search](assets/fr/07.webp)



Na stranici sa detaljima transakcije, pronaći ćete opšte informacije o vašoj transakciji:




- Status**: Potvrđeno kada je dodato u blok, nepotvrđeno kada čeka u Mempool.
- Naknade za transakciju**.
- Procenjeno vreme dolaska (ETA)** :  Približno vreme koje će biti potrebno da vaša transakcija bude dodata u blok. Izračunava se prema odnosu koji čine naknade povezane sa ovom transakcijom.



![general-txinfo](assets/fr/08.webp)



Sekcija **Flow** prikazuje grafikon vaših komponenti transakcije.



Ulazi (prethodni UTXO), korišćeni za vašu transakciju, i izlazi koji daju primaocima pravo da koriste bitkoine iz svakog izlaza predstavljanjem potpisa potrebnog za njihovo trošenje.



![flow](assets/fr/09.webp)



Više detalja o korišćenim adresama možete pronaći u odeljku **Ulazi i Izlazi**.



![address](assets/fr/10.webp)



Otkrijte različite Bitcoin transakcione šeme kako biste poboljšali svoju poverljivost.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ubrzajte svoje transakcije



U ekosistemu Bitcoin, aspekt validacije transakcija od strane rudara je intrinzično povezan sa naknadama za transakcije koje su povezane sa tom transakcijom. Rudari daju prioritet transakcijama sa višim odnosom naknada (satoši/vBajtovi), što može uticati na validnost vaše transakcije ako ne platite razumne naknade koje rudari prihvataju. Vaša transakcija bi se zaglavila u Mempool čekajući blok koji prihvata njen odnos naknada.



Srećom, postoje dve metode dostupne na Bitcoin mreži za ubrzanje potvrde vaše transakcije.





- RBF** - Zamena uz naknadu: Metod koji vam omogućava da potrošite iste unose kao vaša transakcija sa niskom naknadom, ali ovog puta povećanjem naknade za transakciju kako biste ubrzali validaciju. Vaša nova transakcija će biti brže validirana i uključena u blok, čime će transakcija sa niskom naknadom postati nevažeća.



Možete izvršiti akciju zamene naknade sa portfeljima koji prihvataju ovaj mehanizam. Na primer, pogledajte naš članak o portfelju Blue Wallet.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- CPFP** - Child pay for parent: Pristup inspirisan RBF, ali na strani primaoca. Kada je transakcija u kojoj ste vi primalac blokirana u Mempool, imate opciju da potrošite izlaze (UTXO-e) te transakcije, uprkos tome što još nije potvrđena, tako što ćete dodeliti više naknada ovoj novoj transakciji kako bi prosečne naknade - transakcije za koju ste primalac i pokrenute transakcije - podstakle rudare da uključe obe transakcije u blok.



⚠️ Prva transakcija mora biti uključena u blok kako bi druga transakcija bila potvrđena.



Ako vam svi ovi termini deluju previše tehnički, preporučujem da [pogledate naš rečnik](https://planb.network/resources/glossary), koji sadrži definicije svih tehničkih termina vezanih za Bitcoin i njegov ekosistem.



Pored ovih metoda, Mempool.space, zahvaljujući svojim vezama sa preko 80% rudara prisutnih na Bitcoin mreži, takođe vam omogućava da ubrzate bilo koju od vaših **nepotvrđenih** transakcija, čak i one koje ne aktiviraju RBF, plaćanjem naknade rudarima u Exchange za ubacivanje vaše jeftine transakcije u sledeći blok spreman za rudarenje.



Na stranici sa detaljima transakcije, kliknite na dugme **Ubrzaj**, zatim nastavite da platite vašoj suprotnoj strani rudarima.



![accelerate-section](assets/fr/11.webp)


## Maloletnici



Miner se odnosi na osobu koja upravlja rudnikom, tj. računar koji učestvuje u procesu Mining, koji se sastoji od učešća u Proof-of-Work. Miner grupiše transakcije na čekanju u svom Mempool kako bi formirao kandidatski blok. Zatim traži važeći Hash, manji ili jednak cilju, za zaglavlje ovog bloka menjajući različite nonce. Ako pronađe važeći Hash, emituje svoj blok na Bitcoin mrežu i zarađuje povezanu novčanu nagradu, koja se sastoji od subvencije bloka (stvaranje novih bitkoina ex-nihilo) i naknade za transakciju.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Rudari su poput "validatora" koji verifikuju i grupišu transakcije u blokove. Da bi dodali novi blok u Bitcoin mrežu, moraju rešiti složenu matematičku zagonetku (Proof-of-Work). Prvi Miner koji reši zagonetku osvaja Bitcoin nagradu (blok grant + naknade za transakcije uključene u blok).



Težina ovog Proof of Work se prati, omogućavajući vam da vizualizujete evoluciju računske snage potrebne za rudare. U odeljcima ispod ćete pronaći:





- Procena ukupnih nagrada koje su rudari dobili tokom poslednjeg podešavanja težine, kao i procene sledećeg Halving blok granta, koji se dešava na svakih 210.000 blokova (približno 04 godine).



![rewards](assets/fr/12.webp)



Ova težina se prilagođava svakih 2016 blokova (otprilike svake dve nedelje). Ona je obrnuto proporcionalna prosečnom vremenu koje je rudarima potrebno da Miner svakih 2016 blokova.


Kada je prosečno vreme koje rudari provode manje od 10 minuta, težina se povećava, što dokazuje da je rudarima bilo lakše da validiraju Miner blokove. Suprotno tome, kada je prosečno vreme veće od 10 minuta, težina se smanjuje.



![mining-pool](assets/fr/13.webp)





- Grupe rudara: S obzirom na poteškoće koje su uključene, grupa rudara sarađuje kako bi pomogla u pronalaženju Proof of Work na Bitcoin, u onome što nazivamo **pool**. Kada grupa iskopa blok, dobijena nagrada se distribuira prema procentu uspeha u pretrazi delimičnog rešenja svakog Miner, tj. doprinosu u računarskoj snazi u potrazi za Proof-of-Work, ili prema metodi naknade dogovorenoj saradnjom.





![mining](assets/fr/14.webp)



## Lightning Network infrastruktura



Mempool ne pruža samo informacije o mrežnoj infrastrukturi Bitcoin (glavni lanac). Takođe integriše alate za vizualizaciju i istraživanje za Bitcoin-ov Lightning sloj.



U odeljku **Lightning** možete videti sve postojeće veze između Lightning čvorova.



![network-stats](assets/fr/15.webp)



Ovaj Interface pruža informacije o :





- Lightning Network statistika.



![distribution](assets/fr/16.webp)




⚠️ **VAŽNO**: Kapacitet platnog kanala označava maksimalni iznos koji čvor može poslati drugom čvoru tokom Lightning transakcije.





- Lightning čvorovi su raspoređeni prema provajderu internet usluga (usluga hostinga) i opcionalno prema kapacitetu platnog kanala.



![distribution](assets/fr/17.webp)





- Istorija ukupnog kapaciteta Lightning Network.


Takođe ćete pronaći rangiranje ovih čvorova prema kapacitetu njihovih platnih kanala.



![ranking](assets/fr/18.webp)



## Više grafike



Mempool.space je idealna platforma za uživanje u interakciji sa Bitcoin protokol mrežama. Grafici ne samo da pružaju vizuelne podatke koji vam pomažu da odlučite kada da izvršite transakcije, već i precizne parametre koji vam omogućavaju da u realnom vremenu vizualizujete snagu i zdravlje Bitcoin mreže i povezane Lightning infrastrukture.



U odeljku **Grafika** možete videti osnovne podatke o mreži Bitcoin:




- Evolucija veličine Mempool: Možete posmatrati kako veličina Mempool varira, što može ukazivati na periode visoke ili niske aktivnosti na mreži.



![graphs](assets/fr/19.webp)






- Evolucija transakcija i naknada za transakcije na odabranoj mreži: Praćenjem varijacija u broju transakcija po sekundi, možete predvideti periode zagušenja ili niske aktivnosti i optimizovati svoje naknade za transakcije. Ovaj grafikon vam daje perspektivu o kapacitetu mreže da obradi obim transakcija.



![graphs](assets/fr/20.webp)



Sada kada ste stigli do kraja svog putovanja na Mempool.space, postanite sopstveni istraživač i pratite svoje transakcije u realnom vremenu. Molimo vas da ispod pronađete naš članak o Bitcoin **Public Pool** istraživaču.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1