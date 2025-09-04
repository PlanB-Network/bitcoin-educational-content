---
name: Bull Bitcoin Wallet
description: Saznajte kako koristiti Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Ovaj vodič vas vodi kroz instalaciju, konfiguraciju i korišćenje Bull Bitcoin Mobile. Naučićete kako da primate i šaljete sredstva na tri mreže: onchain, Liquid i Lightning, i kako da prenesete vaš Bitcoin sa jedne mreže na drugu. Dodaci pružaju resurse i kontakte, osnovne informacije i kratka objašnjenja tehničkih pojmova.



## Uvod



**Bull Bitcoin Mobile**, developed by **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([create account](https://app.bullbitcoin.com/registration/orangepeel)), je **self-custodial** Bitcoin Wallet, što znači da imate potpunu kontrolu nad svojim privatnim ključevima i stoga nad svojim sredstvima, bez oslanjanja na treću stranu. Otvorenog koda i ukorenjen u Cypherpunk filozofiji, ovaj Wallet kombinuje jednostavnost, poverljivost i napredne funkcije kao što su zamene između mreža i podrška za PayJoin. Omogućava vam upravljanje vašim bitcoinima na tri mreže: **Bitcoin onchain**, **Liquid** i **Lightning**, svaka prilagođena specifičnim upotrebama.



### Kontekst razvoja



Wallet odgovara na veliki izazov: Bitcoin mrežne naknade nisu pogodne za male uplate ili za otvaranje malih samostalno hostovanih Lightning kanala. Wallet Bull Bitcoin Mobile nudi rešenje sa samostalnim čuvanjem dok se oslanja na 3 glavne Bitcoin mreže:





- Bitcoin network (onchain)**: Idealno za srednjoročno do dugoročno skladištenje UTXO-a i transakcije velike vrednosti, gde su naknade proporcionalno zanemarljive.
- Liquid Network**: Dizajniran za brze (~2 minuta), poverljivije (skrivene sume), niskotarifne transakcije, savršen za akumulaciju malih iznosa ili zaštitu vaše privatnosti.
- Lightning** network: Optimizovan za trenutna, niskotarifna plaćanja, pogodan za dnevne transakcije male do srednje vrednosti.



Sa Bull Bitcoin Mobile, na primer, možete akumulirati male iznose u portfolijima **Liquid** ili **Lightning** i zatim, kada dostignete značajan iznos, možete:





- Prenos na onchain mrežu za sigurno srednjoročno ili dugoročno skladištenje, uz poboljšanu poverljivost sa Liquid i/ili Lightning upstream, i sa onchain naknadama za jednu transakciju.



### Kontinuirana evolucija



Wallet se stalno razvija, tako da nemojte biti iznenađeni ako pronađete neslaganja između ovog vodiča i vaše ažurirane aplikacije.




- Na primer, od 19.07.2025., dugmad **"Kupi / Prodaj / Plati "** su vidljiva, ali zasivljena u aplikaciji, jer će ove opcije, dostupne na Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel), uskoro biti integrisane za jedinstveno iskustvo. Njihova upotreba će ostati potpuno opcionalna. Mnogi drugi razvojni projekti su u toku ili planirani: upravljanje sa više Wallet, passphrase, kompatibilnost sa hardverskim novčanicima...
- Na [BullBitcoin GitHub-u](https://github.com/orgs/SatoshiPortal/projects/49), možete pogledati trenutne teme i nadolazeće razvojne projekte. Pošto je projekat 100% open-source i "izgrađen u javnosti", možete nam poslati vaše predloge i sve greške na koje naiđete.




## 1. Preduslovi



Pre nego što počnete koristiti **Bull Bitcoin Mobile**, uverite se da imate sledeće stavke:





- Kompatibilan pametni telefon**: **iOS** (iPhone ili iPad) ili **Android** uređaj
- Internet konekcija
- Sigurnosni medij za bekap**: Zapišite svoju **frazu za oporavak** (12 reči) na papir ili metal i čuvajte je na sigurnom mestu.
- Osnovno znanje**: Minimalno razumevanje Bitcoin koncepta (adrese, transakcije, naknade) je korisno, iako ovaj vodič objašnjava svaki korak za početnike.



## 2. Instalacija





- Preuzmite aplikaciju** :
 - [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Preuzmite iz prodavnice aplikacija za Android uređaje
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Preuzmite APK za Android uređaje direktno**
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** Preuzmite putem TestFlight-a za Apple uređaje
 - Proverite ime programera (Bull Bitcoin) kako biste izbegli lažne aplikacije.
 - Uverite se da preuzeta verzija odgovara najnovijoj stabilnoj verziji navedenoj na GitHub-u.
 - Bull Bitcoin Mobile je **open-source**. Da biste pogledali kod: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Instaliraj aplikaciju




## 3. Inicijalna konfiguracija



### 3.1 Pokreni aplikaciju :



Aplikacija koristi jedinstvenu frazu za oporavak od 12 reči za oba portfolija:




 - osigurati Bitcoin' Wallet**: Za transakcije na Bitcoin mreži (onchain)
 - instant Payments' Wallet**: Za trenutne transakcije na Liquid i Lightning mrežama



Prilikom otvaranja, od vas se traži da uvezete postojeću frazu za oporavak ili da kreirate novu Wallet :



![image](assets/fr/02.webp)



### 3.2 Fraza za oporavak :



Ako želite ponovo koristiti postojeći Wallet, kliknite na "**Recover Wallet**" i unesite 12 reči vaše fraze za oporavak.



Inače, kliknite na "**Create New Wallet**" :




- Zapišite svoju frazu za oporavak s najvećom pažnjom. Zapišite je na papir ili metal i čuvajte na sigurnom mestu (sef, vanmrežna lokacija). Ova fraza je vaš jedini način pristupa vašim bitcoinima u slučaju gubitka uređaja ili brisanja aplikacije.
- Takođe je važno napomenuti da bilo ko sa ovom frazom može ukrasti sve vaše bitkoine. Nikada je ne čuvajte digitalno:
 - Nema snimka ekrana
 - Nema rezervnih kopija oblaka, e-pošte ili poruka
 - Bez kopiranja/lepljenja (rizik od čuvanja u međumemoriji)



**! Ova tačka je kritična**. Za dalju pomoć :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Obezbeđivanje pristupa :





- Idite na podešavanja, a zatim kliknite na **PIN kod**.
- Postavite robustan **PIN kod** za zaštitu pristupa aplikaciji.
- Ovaj korak je opcionalan, ali se snažno preporučuje kako bi se sprečilo da bilo ko ko ima pristup vašem telefonu dobije pristup vašem Wallet.



![image](assets/fr/03.webp)



### 3.4 Povezivanje na lični čvor (opciono):



Wallet BullBitcoin se po podrazumevanoj vrednosti povezuje na Electrum servere: prvi kojim upravlja Bull Bitcoin i sekundarni server od Blockstream-a, za koje se smatra da ne čuvaju logove, smanjujući rizik od praćenja.



Za veću poverljivost, možete povezati aplikaciju sa sopstvenim Bitcoin čvorom putem Electrum servera (uputstva su dostupna na [BullBitcoin's GitHub](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Primanje sredstava



Primanje sredstava sa **Bull Bitcoin Mobile** je jednostavno i prilagođeno vašim potrebama, bilo da koristite :




  - mreža **Bitcoin (onchain)** za dugoročnu zaštitu,
  - mreža **Liquid** za brzo, više Confidential Transactions,
  - **Lightning** mreža za trenutna, niskovredna plaćanja.



Aplikacija automatski generiše Lightning prijemne ili Invoice adrese, u zavisnosti od izabrane mreže. Evo kako da nastavite za svaku mrežu.



### 4.1. onchain (Bitcoin mreža)



Na početnom ekranu, možete:




- ili odaberite **Secure Bitcoin Wallet** zatim kliknite na "**Receive "** :



![image](assets/fr/04.webp)





- ili kliknite na "**Receive**", a zatim izaberite mrežu **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Opcija "Kopiraj ili skeniraj samo Address" onemogućena (podrazumevano)



![image](assets/fr/06.webp)





- Ovo omogućava pristup opcionalnim naprednim parametrima. Možete navesti:
 - Iznos u BTC, Sats ili fiat.
 - **lična beleška** koja će biti uključena u kopiju URI / QR koda.
 - Aktivacija **PayJoin** (pogledajte Dodatak 3 za detalje), koja poboljšava poverljivost kombinovanjem unosa pošiljaoca i primaoca.





- Primer automatski generisanog URI-ja** :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- Usage**: Kopiraj URI da podeliš sa pošiljaocem, ili mu dozvoli da skenira QR kod.



#### 4.1.2. Omogućena opcija "Kopiraj ili skeniraj samo Address"



![image](assets/fr/07.webp)





- Sa omogućenim podešavanjem **"Kopiraj ili skeniraj samo Address"**, aplikacija generiše jednostavan Bitcoin Address u SegWit (bech32) formatu.





- Primer:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Čak i ako unesete iznos ili belešku, oni neće biti uključeni u QR kod ili u kopiju Address





- Upotreba**: Kopirajte Address da ga podelite sa pošiljaocem ili mu dozvolite da skenira QR kod.



#### 4.1.3. Generisanje novog Address





- Zašto koristiti novi Address za svaku transakciju? Ovo **štiti vašu privatnost** sprečavanjem povezivanja više uplata sa istim Address, i ograničava mogućnosti praćenja na Blockchain.
 - Podrazumevano, Bull Bitcoin automatski generiše neiskorišćeni Address.**
 - Možete forsirati kreiranje novog Address klikom na **"New Address"** na dnu ekrana.
 - Sve vaše adrese su povezane sa vašom seed frazom: bez obzira na to koliko adresa koristite, vaš portfolio će prikazivati jedinstveni saldo i može automatski konsolidovati sredstva kada se izvrši isporuka.





- Savet: Uvek koristite novi Address** koji obezbeđuje Bull Bitcoin, osim ako nemate specifičnu potrebu (npr. javni Address za primanje donacija).



### 4.2. Liquid



Na početnom ekranu, možete:




- ili odaberite **Instant payments Wallet** zatim kliknite na **"Receive "** pa **"Liquid"** :



![image](assets/fr/08.webp)





- ili kliknite na "**Receive**", a zatim izaberite mrežu **Liquid**:



![image](assets/fr/09.webp)



Kada ste na ekranu **"Receive "**, kopirajte Liquid Address:





- Nema iznosa ili beleške. Primer:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Ili tako što navedete **iznos** (u BTC, Sats ili fiat) i/ili **ličnu belešku** koja će biti uključena u kopiju URI / QR koda. Primer:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Koristi**: Kopiraj Address/URI da podeliš sa pošiljaocem, ili mu dozvoli da skenira QR kod.



### 4.3. Munja



Na početnom ekranu, možete:




- ili odaberite **Instant payments Wallet** zatim kliknite na "**Receive "** :



![image](assets/fr/10.webp)





- ili kliknite na "**Receive**", a zatim izaberite **Lightning** mrežu:



![image](assets/fr/11.webp)



#### 4.3.1. Operacija, ograničenja i koristi





- Mehanizam**: Bull Bitcoin Wallet je Wallet koji omogućava plaćanja putem Lightning-a. Sredstva primljena putem Lightning-a se čuvaju na mreži **Liquid** (u Wallet Instant Payments) zahvaljujući automatskoj zameni putem **Boltz**. Ovo vam omogućava interakciju sa Lightning-om bez potrebe za upravljanjem kanalima likvidnosti, dok ostajete u samostalnom staranju o sredstvima.





- Ograničenja:**
 - Minimalni iznos** od 100 satoshija (od 19.07.2025) kada generate Invoice.
 - Vi plaćate troškove**, koji će biti oduzeti od iznosa koji šalje pošiljalac, za razliku od primanja sa Wallet Lightning native, gde samo pošiljalac plaća troškove transfera pored poslatog iznosa. Od 19/07/2025, 47 Sats se oduzima od poslatog iznosa.





- Prednosti** :
 - Samokustodijalno**: Vaša sredstva ostaju pod vašom kontrolom, uskladištena na Liquid Network.
 - Nema visokih onchain naknada**: Skladištenje na Liquid izbegava skupe onchain depozite za otvaranje vašeg Lightning kanala ili dodavanje likvidnosti. Ove operacije se mogu izvršiti kasnije, kada iznos akumuliran na Liquid opravda naknade.





- Savjet:** Ako pošiljalac ima Wallet Bull Bitcoin, koristite direktno Liquid Network da izbegnete naknade za zamenu.



#### 4.3.2. generate Invoice





- Unesite **iznos** (u BTC, Sats ili fiat)





- Dodajte **ličnu belešku** koja će biti integrisana u Invoice. Ako pošiljalac plati Invoice, vaš Wallet će je takođe uključiti u detalje transakcije.





- Invoice validity:** The Lightning Invoice is valid for **12 hours**. After this time, it expires and can no longer be paid. A new Invoice must be generated.





- Upotreba**: Kopirajte Invoice da ga podelite sa pošiljaocem, ili mu dozvolite da skenira QR kod.




## 5. Slanje sredstava



### 5.1. Osnovni princip



Ili sa početne stranice, ili iz novčanika :



![image](assets/fr/12.webp)



da pristupite ekranu za slanje:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** olakšava slanje novca automatskim prepoznavanjem mreže (Bitcoin, Liquid ili Lightning) na osnovu unetog (kopiranog ili skeniranog putem QR koda) Address ili Invoice.



### 5.2. onchain transmission (Bitcoin mreža)



#### 5.2.1. Pošalji ekran



**Akcija**: Unesite ili skenirajte Bitcoin na lancu Address





- Ako iznos nije definisan, na primer:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Zatim možete izabrati na ekranu za slanje :
 - Iznos u BTC, sat ili fiat. Minimalni iznos: 546 satoshija dana 22/07/2025.
 - Opciona napomena za identifikaciju transakcije. Vidljivo samo vama, u detaljima transakcije.



![image](assets/fr/14.webp)





- Ako je iznos već definisan, na primer :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Bićete direktno prebačeni na ekran za potvrdu ispod.



#### 5.2.2 Ekran za potvrdu



Odvojite vreme da proverite sve parametre, posebno iznos, odredište Address i naknade.


Zatim možete prilagoditi parametre:



![image](assets/fr/15.webp)




- Naknade**: Možete izabrati :
  - Ili brzina izvršenja** vaše transakcije, a povezane naknade će biti procenjene
  - Ili naknade**, u režimu apsolutnih naknada (ukupne naknade u satoshijima) ili relativnih naknada (naknade po bajtu), i brzina vaše transakcije će biti procenjena





- Napredna podešavanja** :





 - Replace-by-fee (RBF)** : Aktivirana po defaultu, ova funkcija ubrzava transakciju plaćanjem veće naknade (pogledajte Dodatak 4 za detalje).





 - Ručno odabiranje UTXO**: Ako su vaša sredstva pohranjena na nekoliko različitih Wallet adresa, možete odabrati adrese s kojih ćete poslati sredstva. Zašto biste to učinili? Sa sve većim prihvatanjem Bitcoin, troškovi transfera rastu. Slanje s nekoliko adresa s malim iznosima je skuplje nego slanje s jedne Address, ali to učiniti sada izbegava potrebu da se to uradi kasnije, kada će naknade biti još veće. Ovo se zove **konsolidacija UTXO.**



![image](assets/fr/16.webp)





- Slanje sa PayJoin**: Ako je funkcija aktivirana od strane primaoca koji je dostavio URI, npr. :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Zatim će Bull Bitcoin Mobile konfigurisati slanje kombinovanjem vaših UTXO-a sa UTXO-ima primaoca kao ulaz, poboljšavajući poverljivost (pogledajte Dodatak 3 za detalje).



### 5.3. Pošalji na Liquid



#### 5.3.1 Pošalji ekran



Mreža **Liquid** omogućava brze transakcije (~2 minuta zahvaljujući jednom bloku po minutu), više poverljive (maskirani iznosi) nego na onchain mreži, i sa veoma niskim naknadama. Sredstva se povlače sa **Instant Payments Wallet**.



**Akcija**: Unesite ili skenirajte Liquid Address





- Ako iznos nije definisan, na primer :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Zatim možete izabrati na ekranu za slanje :




- Iznos u BTC, sat ili fiat. Nema minimuma, 1 Satoshi moguće;
- Opciona napomena za identifikaciju transakcije. Vidljivo samo vama, u detaljima transakcije.



![image](assets/fr/17.webp)





- Ako je iznos već definisan, na primer :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Bićete direktno preusmereni na ekran za potvrdu ispod.



#### 5.3.2 Ekran za potvrdu



Odvojite vreme da proverite sve parametre, posebno količinu i odredište Address.



![image](assets/fr/18.webp)





- Naknade**: Proporcionalne složenosti transakcije, generalno na osnovu 0.1 sat/vB, tj. 20-40 satoshija za jednostavnu transakciju (33 Sats na 07/22/2025).



### 5.4. Pošalji na Lightning



#### 5.4.1 Pošalji ekran



**Lightning** mreža omogućava trenutna, niskotarifna plaćanja za male iznose, idealna za male dnevne transakcije.



**Akcija**: Unesite ili skenirajte Lightning Invoice





- Ako skeniraš LN-URL Address koji ti omogućava da postaviš iznos


Primer: `orangepeel@walletofsatoshi.com`.


onda možete izabrati na ekranu za slanje :




 - Iznos u BTC, sat ili fiat. Minimalni iznos od 1000 satoshija dana 23/07/2025.
 - Opciona napomena za identifikaciju transakcije. Biće poslata primaocu.



![image](assets/fr/19.webp)





- Ako skeniraš Lightning Invoice koji sadrži definisanu količinu


Primer:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Bićete direktno prebačeni na ekran za potvrdu ispod.



Napomena: iznos mora biti veći od 21 Sats dana 23.07.2025.



#### 5.4.2 Operacija, ograničenja i koristi





- Mehanizam**: Sredstva se povlače iz **Instant Payments Wallet** (Liquid) i konvertuju putem **Liquid → Lightning** zamene sa **Boltz**.





- Ograničenja:**
 - Minimalni iznos** veći od Wallet Lightning native (vidi gore)
 - Troškovi** plus Liquid → Lightning zamena putem Boltz





- Prednosti** :
 - Samokustodijalno**: Vaša sredstva ostaju pod vašom kontrolom, smeštena na Liquid Network, i prenosiva putem Lightning-a ako je potrebno
 - Nema visokih onchain naknada**: Čuvanje na Liquid vam je uštedelo skupe onchain depozite za otvaranje vašeg Lightning kanala ili dodavanje likvidnosti. Ove operacije se mogu obaviti kasnije, kada iznos akumuliran na Liquid opravda naknade.





- Savjet:** Ako primalac ima Wallet Bull Bitcoin, koristite Liquid Network direktno da izbegnete troškove zamene.



#### 5.3.3 Ekran za potvrdu



Odvojite vreme da proverite sve parametre, posebno količinu i odredište Address.



![image](assets/fr/20.webp)




## 6. Prikaži istoriju



**Bull Bitcoin Mobile** olakšava praćenje vaših transakcija na mrežama **Bitcoin (onchain)**, **Liquid** i **Lightning**. Istorija se može pristupiti na dva načina i prikazuje detaljne informacije za svaku vrstu transakcije. Takođe možete proveriti vaše transakcije koristeći spoljne blok pretraživače.



### 6.1. Istorija pristupa





- Putem početnog ekrana** :
 - Kliknite na **Secure Bitcoin Wallet** da biste pogledali **onchain** transakcije, ili na **Instant Payments Wallet** za **Liquid** i **Lightning** transakcije.
 - Istorija je prikazana direktno ispod ukupnog portfolija, filtrirana prema tipu Wallet koji je izabran.



![image](assets/fr/21.webp)





- Putem posvećenoj stranici** :
 - Na početnom ekranu kliknite na **simbol istorije** (ikona sata ili slična).
 - Pristupite stranici sa spiskom svih transakcija, sa filterima po tipu akcije: **Pošalji**, **Primi**, **Zameni**, **PayJoin**, **Prodaj**, **Kupi** (napomena: Prodaja i Kupovina su u razvoju i nisu dostupne u ovom trenutku, 20. jul 2025).



![image](assets/fr/22.webp)



### 6.2. Detalji transakcije



Svaka transakcija prikazuje specifične informacije u zavisnosti od mreže i tipa akcije (slanje ili primanje). Ovde su dostupni detalji za **transakciju na lancu** :



![image](assets/fr/23.webp)



### 6.3. Provera putem Block explorer



Lista istraživača za **Bitcoin onchain**, **Liquid** i **Lightning** mreže nalazi se u Dodatku 4.



Za **Lightning**, transakcije nisu vidljive na javnim pretraživačima. Proverite detalje (uključujući Swap ID za Boltz) u aplikaciji.




## 7. Postavke



Stranica "Settings" može se direktno pristupiti sa početne stranice aplikacije Bull Bitcoin i koristi se za konfigurisanje i upravljanje različitim aspektima portfolija i korisničkog iskustva.



![image](assets/fr/24.webp)





- Wallet Backup**: Prikazuje frazu za oporavak portfolija za sigurno bekapovanje. Pogledajte odeljak 3. o kreiranju portfolija za najbolje prakse u upravljanju i čuvanju fraze za oporavak.





- Wallet Detalji** :
 - Pubkey**: Javni ključ povezan sa Wallet, koristi se za generate Bitcoin adrese prijema.
 - Derivation Path**: Derivation path used to generate Wallet addresses from the private key.





- Electrum Server (Bitcoin Node)**: Postavite vezu sa prilagođenim Bitcoin čvorom za onchain transakcije.





- PIN Kod**: Aktivirajte i/ili izmenite sigurnosni kod za zaštitu pristupa aplikaciji i funkcijama Wallet.





- Valuta**: Izaberite da li želite prikazivanje iznosa u BTC ili Sats, i podrazumevanu fiat valutu (dolar, evro, itd.).





- Auto Swap Settings**: Funkcija _Auto Swap_ omogućava vam da automatizujete prenos vašeg BTC sa **Instant Payments Wallet (Liquid)** na vaš **Bitcoin On-Chain** Wallet, čim iznos dostigne prag koji smatrate dovoljno visokim da opravda trošak transakcije.





- Logovi**: Pregledni dnevnici aktivnosti, koji se mogu deliti sa tehničkom podrškom radi olakšavanja rešavanja problema.





- Pristup Telegramu za podršku** : Direktan link ka zvaničnom Telegram kanalu za korisničku podršku.





- Github pristup** : Link ka [Bull Bitcoin Github repozitorijumu](https://github.com/SatoshiPortal) za pregled otvorenog koda ili prijavu problema.




## DODACI



### A1. Objašnjenje PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definicija** :




- PayJoin, ili **Pay-to-EndPoint (P2EP)**, je Bitcoin transakcijska tehnika koja poboljšava poverljivost na **onchain** mreži. Kombinuje unose pošiljaoca i primaoca u jednoj transakciji, čineći iznose i adrese težim za praćenje.



**Operacija:**




- U PayJoin transakciji, pošiljalac i primalac rade zajedno putem kompatibilnog PayJoin servera kako bi generate zajedničku transakciju.
- Umesto da samo pošiljalac obezbeđuje unose (UTXO), primalac takođe doprinosi jednim od svojih UTXO-a. Ovo zamagljuje informacije vidljive na Blockchain: umesto jednog unosa koji odgovara stvarnom iznosu, sada postoje dva unosa, a izlazi ne odražavaju direktno razmenjeni iznos.
- Konačna transakcija podseća na standardnu Bitcoin transakciju (više ulaza/više izlaza), ali skriva stvarni iznos poslat i veze između adresa zahvaljujući steganografskoj strukturi.



**Za upotrebu u Bull Bitcoin Mobilni**




- Primi** (Address Supply): PayJoin je podrazumevano omogućen.
- Pošalji** : Wallet automatski detektuje PayJoin URI i konfiguriše transakciju u skladu s tim, na primer:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Prednosti**




- Poboljšana poverljivost**: PayJoin poništava pretpostavku da svi unosi u transakciji pripadaju jednom entitetu. Sa PayJoin, ulazi dolaze i od pošiljaoca i od primaoca, razbijajući ovu pretpostavku.
- Količinsko maskiranje** : Stvarna količina razmenjena ne pojavljuje se direktno u izlazima. Izračunava se kao razlika između dolaznog i odlaznog UTXO primaoca, što analizu čini obmanjujućom.



**Ograničenja**




- PayJoin zahteva da pošiljalac i primalac koriste kompatibilne novčanike, u suprotnom se koristi standardna onchain transakcija.
- Transakcija je nešto složenija (više ulaza i izlaza), što rezultira nešto višim troškovima.
- Iako je dizajniran da podseća na standardnu transakciju, napredne heuristike (npr. dvosmisleni izlazi, poznati PayJoin serveri) mogu navesti nekoga da posumnja na njenu upotrebu, iako bez apsolutne sigurnosti.



**Više informacija:**




- [Rečnik](https://planb.network/fr/resources/glossary/payjoin)
- Poglavlje [Transakcije PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Objašnjenje Replace-by-fee (RBF)



**Definicija**: Replace-by-fee (RBF) je funkcija Bitcoin mreže koja omogućava pošiljaocu da ubrza potvrdu **onchain** transakcije pristajući da plati višu naknadu.



**Ograničenja** :




- RBF nije dostupan za Liquid ili Lightning transakcije.
- Početna transakcija mora biti označena kao kompatibilna sa RBF kada se kreira, što Bull Bitcoin Mobile radi automatski osim ako nije onemogućeno.



**Više informacija:**




- [Rečnik](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Najbolje prakse



Da biste koristili **Bull Bitcoin Mobile** sigurno i efikasno, pratite ove preporuke. One će vam pomoći da zaštitite svoja sredstva, optimizujete svoje transakcije i sačuvate svoju poverljivost na mrežama **Bitcoin (onchain)**, **Liquid** i **Lightning**.





- Osigurajte svoju frazu za oporavak** :
 - Uputstvo: [Sačuvajte svoju Mnemonic frazu](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Kurs [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Koristite sigurnu autentifikaciju** :
 - Aktivirajte **jak PIN** ili **biometrijsku autentifikaciju** (otiska prsta ili prepoznavanje lica) kako biste zaštitili pristup aplikaciji.
 - Nikada ne delite svoj PIN ili biometrijske podatke.





- Zaštitite svoju privatnost** :
 - generate novi Address za svaki onchain ili Liquid prijem kako bi se ograničilo praćenje na Blockchain.
 - Koristite PayJoin kada je dostupan da povećate poverljivost u vezi sa iznosom poslatim na lancu
 - Za maksimalnu poverljivost, povežite svoj Wallet sa sopstvenim Bitcoin čvorom putem Electrum servera umesto korišćenja javnog čvora.





- Izaberite mrežu koja najbolje odgovara vašim potrebama** :
 - Onchain**: Preferirano za dugoročno čuvanje ili transakcije velike vrednosti (naknade zanemarljive u odnosu na iznos).
 - Liquid**: Koristite za brze, niskobudžetne transfere sa poboljšanom poverljivošću.
 - Lightning**: Odaberite trenutne, niskotarifne transfere za male iznose. Ako ste dva Wallet Bull Bitcoin korisnika, izaberite Liquid da izbegnete Lightning <> Liquid naknade za zamenu putem Boltz.





- Uvek proverite adrese za dostavu** :
 - Pre nego što pošaljete sredstva, pažljivo proverite Address. Sredstva poslana na pogrešan Address su zauvek izgubljena. Koristite kopiranje/lepljenje ili skeniranje QR koda, nikada ne kopirajte/modifikujte Address ručno.





- Optimizujte troškove** :
 - Za transakcije na lancu, izaberite odgovarajuće naknade (sporo, srednje, brzo) u skladu sa hitnošću i zagušenošću mreže.
 - Koristite Liquid, ili Lightning za male količine.
 - Aktivirajte Replace-by-fee (RBF) (pogledajte Dodatak 4) za onchain isporuke ako predviđate potrebu za ubrzanjem potvrde.





- Ažurirajte aplikaciju redovno




### A4. Dodatni resursi





- Zvanični linkovi i podrška:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : support email
 - [Službena veb stranica Bull Bitcoin](https://bullbitcoin.com/) :** Informacije o uslugama Bull Bitcoin, kreiranju naloga, pristupu aplikaciji
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Pogledajte kod, evoluciju i plan puta, doprinesite razvoju...
 - [Account X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
 - Telegram** grupa za Wallet mobilni: grupni čet sa podrškom, pogledajte stranicu "Postavke".





- Blok istraživači :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Lightning: **[1ML (Lightning Network)](https://1ml.com/)**





- Učenje i tutorijali:** **[Plan ₿ Network](https://planb.network/)** :
 - Osiguravanje vaše fraze za oporavak



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Rečnik](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** :
 - [Rečnik](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin



#### Pregled kompanije



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, je najstarija ne-depozitna Exchange platforma posvećena isključivo Bitcoin, osnovana 2013. godine u Bitcoin Ambasadi u Montrealu, Kanada. Na čelu sa Francisom Pouliotom, priznatim pionirem u Bitcoin ekosistemu, kompanija se pozicionira kao ključni igrač u promovisanju finansijskog suvereniteta i autonomije korisnika. Njena misija je omogućiti pojedincima da povrate kontrolu nad svojim novcem koristeći Bitcoin kao alat za slobodu i plaćanje, dok odbacuju fiat valute i kriptovalute osim Bitcoin.



![image](assets/fr/26.webp)



[Kreiraj svoj nalog](https://app.bullbitcoin.com/registration/orangepeel) sa 0.25% popusta na Bitcoin kupovine i prodaje.



#### Vrednosti i filozofija



Bik Bitcoin se ističe po svojim Commitment do Cypherpunk principima i Bitcoin etici:





- Ekskluzivni fokus na Bitcoin** : Platforma je verna viziji decentralizovane valute otporne na cenzuru.





- Nekustodijan** : Korisnici zadržavaju potpunu kontrolu nad svojim Bitcoinima slanjem sredstava u svoje portfelje.





- Poverljivost**: Minimizovano prikupljanje ličnih podataka, sa opcijama kupovine bez KYC za transakcije ispod 999 USD. Podaci su zaštićeni u skladu sa propisima (FINTRAC u Kanadi, AMF u Francuskoj).





- Transparentnost**: Nema skrivenih naknada, troškovi su uključeni u spread (razlika između kupovne i prodajne cene).





- Finansijski suverenitet**: Bull Bitcoin promoviše nezavisnost od tradicionalnih bankarskih sistema i centralizovanih institucija.



#### Glavne usluge





- Fiat deposit** : Korisnici mogu finansirati svoj Bull Bitcoin račun fiat valutom (CAD, EUR, itd.) putem bankovnog transfera ili gotovinom/debitnom karticom u odabranim kanadskim poštama.





- Kupovina Bitcoin** : Korisnici mogu kupiti Bitcoin koji se šalje direktno u njihov ne-depozitni portfolio, garantujući potpunu kontrolu nad njihovim sredstvima.





- Zakazana kupovina Bitcoin**: Bull Bitcoin nudi automatizovanu uslugu ponovljene kupovine (DCA - Dollar Cost Averaging) u redovnim intervalima, koristeći vaš raspoloživi saldo, sa direktnim prenosom Bitcoina na Wallet koji kontroliše korisnik, smanjujući uticaj cenovne volatilnosti.



Imajte na umu da opcija pod nazivom "AutoBuy" omogućava konverziju vaših fiat valuta čim dodirnu vaš Bull Bitcoin saldo, i slanje vaših Bitcoina na vaš sopstveni Wallet. Ova opcija se takođe može kombinovati sa ponavljajućim bankovnim transferom zakazanim sa vašom bankom kako biste napravili DCA. Ova opcija automatizuje vaše Bitcoin akumulacije bez potrebe da ikada otvorite aplikaciju.






- Kupite Bitcoin po fiksnoj ceni 'Limit Order'**: Omogućava vam da kupite Bitcoin po ceni unapred određenoj od strane korisnika, koja se automatski izvršava kada cena indeksa Bull Bitcoin dostigne ili padne ispod postavljenog limita.





- Prodaja Bitcoin**: Korisnici mogu prodati svoje Bitcoine i primiti sredstva u fiat valuti direktno na svoj bankovni račun putem bankovnog ili SEPA transfera.





- Plaćanja trećih strana**: Bull Bitcoin omogućava korisnicima da šalju fiat novac na bankovne račune iz svojih Bitcoina, potpuno transparentno za primaoca.





- Bull Bitcoin Prime**: Bull Bitcoin Prime je premijum usluga za klijente sa visokim neto vrednostima i preduzeća, koja nudi prilagođena rešenja i premijum podršku. Ovo uključuje pristup smanjenim naknadama, posvećenog menadžera naloga i prilagođene korporativne usluge. Ova usluga je namenjena institucijama, profesionalnim trgovcima i korporativnim klijentima koji traže dubinsku ekspertizu i prioritetni tretman.





- Mobilni Wallet**: Bull Bitcoin nudi open-source, samostalni mobilni Wallet, dostupan na Android i iOS, koji podržava onchain, Liquid i Lightning Network transakcije.





- Obrazovna podrška**: Besplatni vodiči i personalizovano mentorstvo kako bi se korisnicima pomoglo da kreiraju, osiguraju i upravljaju svojim Bitcoin portfolijima, jačajući finansijsku autonomiju.



#### Usklađenost i bezbednost





- Regulatory**: Registrovan kod FINTRAC (Kanada) i AMF (Francuska), Bull Bitcoin ispunjava KYC/AML zahteve.





- Sigurnost**: Korišćenje sigurnih portfolija i preporuke za offline skladištenje. Lični podaci su hostovani na Bull-ovoj Bitcoin infrastrukturi, koja je 100% samostalno hostovana i ne oslanja se na treće strane.