---
name: BTCPay Server
description: Prihvatanje BTC uplata bez posrednika
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server je besplatan, open-source softverski paket koji je kreirao Nicolas Dorier i omogućava prihvatanje bitcoin plaćanja bez posrednika. Dizajniran da ponudi autonomiju i finansijski suverenitet, instalira se na sopstvenom serveru i pruža kompletno upravljanje transakcijama, od fakturisanja do validacije on-chain ili Lightning Network plaćanja, i računovodstva. Lako se integriše sa e-commerce sajtovima (WooComerce, Shopify, itd.) ili se može koristiti kao terminal za plaćanje u fizičkim prodavnicama (*POS*).



BTCPay Server je bez sumnje najnaprednije rešenje za trgovce koji žele da prihvate bitcoin. To je najopsežniji i najrobustniji softver u smislu bezbednosti, suvereniteta i poverljivosti. S druge strane, takođe je i najkompleksniji za instalaciju i održavanje. Postoje i jednostavnije alternative: neke su potpuno kustodijalne, kao OpenNode, dok druge nude zanimljiv kompromis između jednostavnosti korišćenja i suvereniteta, kao Swiss Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Cilj ovog vodiča je da vas korak po korak provede kroz instalaciju, konfiguraciju i korišćenje BTCPay Server-a, kako biste mogli da implementirate sigurnu, nezavisnu platnu infrastrukturu u skladu sa Bitcoin etosom.



## BTCPay Server funkcije



Centralizovana Bitcoin point-of-sale rešenja, kao što je *OpenNode* na primer, nude jednostavnost korišćenja, ali se oslanjaju na treću stranu jer ne mogu biti samostalno hostovana i u većini slučajeva su vlasnička. Iako olakšavaju postavljanje plaćanja, uključuju provizije i izlažu korisnike većim rizicima nego rešenje kao što je BTCPay Server, kako u pogledu čuvanja sredstava, tako i poverljivosti.



BTCPay Server je namenjen onlajn ili fizičkim trgovcima, udruženjima i neprofitnim organizacijama koje žele da primaju donacije u bitkoinima. Takođe je idealno rešenje za vlasnike projekata i programere koji traže direktnu podršku od svoje zajednice.



Posebne funkcije BTCPay Server-a uključuju :




- njegova **potpuna autonomija**,
- odsustvo **KYC** procedure,
- potpuna kontrola sredstava**,
- eliminacija platformskih naknada.



Postajući sopstveni procesor plaćanja, eliminišete bilo kakvu zavisnost od centralizovane treće strane između vas i vaših kupaca. Možete prihvatati plaćanja direktno u bitkoinima i generate fakturama za plaćanje. Ovo osigurava da ni vi ni vaša kompanija ne možete biti zabranjeni od strane bilo koga drugog. Igrate ulogu i banke i procesora plaćanja, bez potrebe da plaćate provizije posredniku za svaku transakciju.



Naknade za transakcije za **on-chain** ostaju, ali se mogu smanjiti korišćenjem **Liquid** ili **Lightning** mreže.



Pored toga :




- Potpuno prilagodljiv interfejs i fakture;
- Izvorna podrška za **Tor** radi poboljšane poverljivosti;
- Podrška za **crowdfunding**, **POS** i **dugmad za plaćanje**;
- Kompatibilan sa mnogim valutama ;
- Bitcoin direktna i peer-to-peer plaćanja ;
- Potpuna kontrola nad vašim privatnim ključevima;
- Poboljšana privatnost ;
- Poboljšana sigurnost ;
- Softver koji se samostalno hostuje ;
- Podrška za **SegWit** i **Lightning network** ;
- Interni, portfelj zasnovan na čvorovima, sa integracijom hardverskih portfelja.



## Instalacija i konfiguracija BTCPay Servera



### Biranje načina hostinga



BTCPay Server može biti instaliran na nekoliko različitih načina. U zavisnosti od vaših potreba i resursa, postoje tri glavne opcije:




- BTCPay Server hostovan od strane treće strane**: koristite platformu koja hostuje uslugu za vas. Jednostavno je, ali obično nije besplatno.
- BTCPay Server samostalno hostovan na cloud serveru** (npr. putem [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) ili bilo kog drugog provajdera). Ovo je preporučeno rešenje za većinu početnika trgovaca.
- BTCPay Server instaliran na vašem sopstvenom hardveru (lokalno)** : na računaru, mini-PC-ju ili Umbrel-u. Ova metoda je tehnički zahtevnija, ali nudi potpunu nezavisnost.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Za start-up trgovca, **implementacija na cloud serveru** je najbolji kompromis između autonomije, jednostavnosti i sigurnosti, bez potrebe za upravljanjem celokupnom tehničkom infrastrukturom.



BTCPay Server može se brzo implementirati kod brojnih provajdera hostinga. Među njima, **Voltage** se ističe kao referentno rešenje za korisnike koji zahtevaju **pouzdanu**, **profesionalnu** i **suverenu** infrastrukturu.



### Kreirajte BTCPay Server instancu na Voltage



**Voltage** je gotova Bitcoin i Lightning hosting platforma koja vam omogućava da trenutno implementirate sopstveni BTCPay Server, bez složene konfiguracije ili održavanja servera.



Posetite [zvaničnu Voltage veb stranicu](https://voltage.cloud).



![capture](assets/fr/03.webp)



Kreirajte **korisnički nalog** sa važećom e-mail adresom i jakom lozinkom.



![capture](assets/fr/04.webp)



Voltage nudi **besplatnu 7-dnevnu probu**. Imajte na umu da ćete nakon naše 7-dnevne besplatne probe biti pozvani da se prijavite za fiksnu pretplatu od **$25 mesečno** kako biste nastavili **držati vaše čvorove aktivnim**.



Kada kreirate svoj Voltage nalog i prvi put se prijavite, bićete preusmereni na početnu stranicu, koja ima dva glavna dela:




- Deo za **Infrastrukturu** za upravljanje Lightning čvorovima, Bitcoin Core, BTCPay Serverom i drugim Bitcoin uslugama u oblaku;
- i odeljak **Payments** koji vam omogućava pristup Voltage's API Lightning za integraciju Bitcoin plaćanja u prilagođene aplikacije.



Da biste implementirali svoju instancu **BTCPay Server**, kliknite na **Access infrastructure**. Ovde možete kreirati, upravljati i nadgledati sve svoje usluge, uključujući vaš čvor Bitcoin i BTCPay Server.



#### Kreiraj grup



Pre nego što možete da implementirate uslugu, platforma će vas podstaći da **kreirate grupu**. **Grupa** (radni prostor) je radni prostor koji grupiše sve vaše Bitcoin i Lightning usluge (npr. čvor, BTCPay Server, istraživač, itd.). To je pomalo kao fascikla koja sadrži vaše različite projekte.



![capture](assets/fr/05.webp)



Za potrebe ovog tutorijala, grupa koju smo kreirali će se zvati **Genesis**. Možete dodati profilnu sliku ako želite. Kada to uradite, kliknite na dugme **Kreiraj**. Možete pozvati druge korisnike da se pridruže grupi, pa čak i promeniti ime grupe ako želite.



Na početnoj stranici grupe pojavljuje se nekoliko opcija:




- Lightning Nodes** : to deploy a complete Lightning node (LND) ;
- Bitcoin Core Nodes** : za pokretanje kompletnog Bitcoin čvora ;
- BTCPay Server** : da hostujete spremnu BTCPay instancu;
- Nostr Accounts**: za upravljanje Nostr identitetima.



Aktivirajte **dvostruku autentifikaciju (2FA)** kako biste osigurali svoj nalog i usluge (dugme je vidljivo crveno ako je deaktivirano).



![capture](assets/fr/06.webp)



Kliknite na **BTCPay Server** među opcijama, zatim na **Launch a BTCPay Store**.



![capture](assets/fr/07.webp)



Voltage će vas zatim zamoliti da **kreirate i konfigurišete vašu BTCPay Server instance** tako što ćete odabrati **ime usluge** (1) i omogućiti Lightning plaćanja (2).



Trebaće vam Lightning čvor ako odlučite da prihvatate Lightning uplate.



Ako već nemate Bitcoin ili Lightning čvor, Voltage će vam automatski predložiti da ga kreirate.



Kliknite na **Create a Lightning node** (3) .



![capture](assets/fr/08.webp)



Jednom kada se nađete na interfejsu za kreiranje čvora, bićete upitani da izaberete između **standardnog** i **profesionalnog** rasporeda.



Možete kreirati pravi čvor (**Mainnet**) ili testni čvor (**Testnet**). Zatim kliknite na dugme **Nastavi**.



![capture](assets/fr/09.webp)



Za ovaj vodič, koristimo standardni plan. Unesite **ime čvora**, **lozinku** i pritisnite dugme **Kreiraj**.



![capture](assets/fr/10.webp)



Nakon nekoliko trenutaka, vaš čvor će biti operativan i moći ćete otvoriti besplatan kanal sa kapacitetom prijema od 500.000 sats.



![capture](assets/fr/11.webp)



Malo dalje desno, pronaći ćete sve informacije koje su vam potrebne o vašem čvoru!



![capture](assets/fr/12.webp)



Sada kada smo pokrenuli naš Lightning čvor, vratimo se na instalaciju našeg BTCPay servera. Sada možete kliknuti na dugme **Create BTCPay**.



![capture](assets/fr/13.webp)



Otvoriće se stranica sa vašim podrazumevanim podacima za prijavu, zajedno sa porukom koja vas poziva da promenite početnu lozinku. Kada to uradite, kliknite na dugme **Prijavi se sada** da biste pristupili svom interfejsu.



![capture](assets/fr/14.webp)



To je to! Vaš BTCPay server je spreman za korišćenje. Bićete preusmereni direktno na stranicu za prijavu vašeg BTCPay servera.



![capture](assets/fr/15.webp)



Kada se prijavite, konfigurišite svoju prvu **prodavnicu**:





- Dajte mu **ime**.





- Izaberite **podrazumevanu valutu** (EUR, USD, CFA, itd.).





- Odaberite **provajdera kursa** (npr. CoinGecko).



![capture](assets/fr/16.webp)



Bićete preusmereni na kontrolnu tablu vaše prodavnice. Na interfejsu kontrolne table, primetićete da je dugme **Kreiraj svoju prodavnicu** označeno zelenom bojom, jer je ovaj korak već završen.



![capture](assets/fr/17.webp)



Malo niže imamo dugmad **Configure wallet** i **Configure Lightning node**. U našem slučaju, već smo se povezali na Lightning čvor koji radi na naponu. Tako da to ovde nećemo morati da radimo.



Hajde da pređemo na konfigurisanje portfolija. Kliknite na dugme **Konfiguriši portfolio**.



Pošto tek počinjemo sa BTCPay Server-om, hajde da povežemo postojeći wallet. Zato pritisnite **Poveži postojeći portfolio**.



![capture](assets/fr/18.webp)



Morate zatim izabrati svoju **metodu uvoza**. Među dostupnim opcijama, odaberite **Unesite prošireni javni ključ**.



![capture](assets/fr/19.webp)



Povezivanjem postojećeg wallet, možete primati svoje uplate **direktno na ovaj eksterni wallet**, bez da BTCPay server ima pristup vašem privatnom ključu. Dakle, čak i ako bi server bio hakovan ili javni ključ (`xpub`) kompromitovan, napadač bi mogao videti vašu istoriju transakcija, ali bi bilo **nemoguće pristupiti vašim sredstvima**.



Kada kliknete na dugme **Unesite prošireni javni ključ**, bićete **preusmereni** na stranicu gde morate uneti ovaj ključ.



Sada hajde da preuzmemo **prošireni javni ključ**.



### Povezivanje Bitcoin wallet



Da biste primili svoje uplate, potrebno je da povežete Bitcoin wallet sa svojom prodavnicom. Da biste to uradili, imate nekoliko opcija:





- Portfolio hardvera** (Ledger, Trezor, Coldcard...) ;





- Portfolio softvera** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- BTCPay Server** interna wallet (nije preporučeno, jer je manje sigurna i više izlaže vaša sredstva u slučaju hakovanja servera).



U ovom vodiču koristićemo **softverski portfelj**, koji je pristupačniji za početnu konfiguraciju. Možete birati između nekoliko kompatibilnih aplikacija: **Electrum**, **Phoenix**, **Zeus**, **Muun**, itd.



Za demonstraciju ćemo koristiti **Electrum**. Otvorite **Electrum**, kliknite na **Portfolio**, zatim na **Information** :



![capture](assets/fr/20.webp)



Zatim, kopirajte **master javni ključ (xpub)**.



![capture](assets/fr/21.webp)



Kada kopirate glavni javni ključ, nalepite ga u predviđeno polje na BTCPay Server stranici.



![capture](assets/fr/22.webp)



Nakon verifikacije, bićete preusmereni na kontrolnu tablu vaše prodavnice.



![capture](assets/fr/23.webp)



### Generiši prodajno mesto (PoS)



Jednom kada postavite svoju prodavnicu i portfolio, sada možete postaviti **Point of Sale (PoS)** da počnete primati Bitcoin uplate direktno od svojih kupaca.



Ova integrisana funkcija **BTCPay Server-a** je idealna za **trgovce, zanatlije, restorane ili pružaoce usluga** koji žele da prihvate Bitcoin **bez veb sajta** ili posebnih tehničkih veština.



### Koja je svrha prodajnog mesta?



**PoS** je **pojednostavljeni POS interfejs** koji funkcioniše kao **Bitcoin terminal za plaćanje**.


Omogućava vam da :




- Kreirajte **meni proizvoda ili usluga** sa fiksnim cenama.
- Generiši **trenutni račun sa QR kodom** za skeniranje.
- Podelite **URL za plaćanje** koji je dostupan putem pametnog telefona, tableta ili računara.



Drugim rečima, PoS pretvara vaš BTCPay Server u **direktni prodajni interfejs**, gde se svaka uplata prima **u vaš sopstveni Bitcoin wallet**, bez posrednika.



### Konfigurisanje PoS-a



Na BTCPay kontrolnoj tabli, kliknite na **PLUGINS**, zatim na **Point of sale**.



Zatim kliknite na **Kreiraj novu PoS aplikaciju**. Ova akcija dodaje **novu aplikaciju** u vašu BTCPay prodavnicu, kao da instalirate mini interni prodajni sajt.



Otvara se stranica za kreiranje vaše aplikacije. Definišite **ime aplikacije**: ovo je interno ime, vidljivo samo sa vaše kontrolne table (npr. _Prodavnica Cipela_).



Kliknite na **Create** da biste potvrdili.



![capture](assets/fr/24.webp)



Kada se kreira, bićete preusmereni na **Detaljnu stranicu za konfiguraciju** prodajnog mesta.



### Prilagodite svoj prodajni interfejs



Na ovoj stranici možete definisati osnovne elemente vašeg PoS-a:





- Ime aplikacije** (interni naziv za upravljanje, može se promeniti u bilo kom trenutku).





- Prikaži naslov** (ono što će vaši kupci videti na vrhu stranice).





- Stil prodajnog mesta** (**Opis** režim je pogodan za usluge kao što su šišanje ili obroci, dok je režim **Katalog proizvoda** idealan za prodavnice koje nude više artikala).





- Prikaži valutu** (izaberi **XOF**, **EUR** ili **USD** prema tvojim uobičajenim cenama).**





- Lista proizvoda** (dodajte svoje proizvode, opise i cene ovde).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Sačuvaj i testiraj svoj PoS



Kada završite sa konfigurisanjem, kliknite na **Save** da sačuvate svoja podešavanja, zatim na **View** da pregledate svoj PoS.



Videćete stranicu koja prikazuje vaše proizvode, sa svakim dugmetom koje odgovara artiklu ili usluzi.



Čim kupac odabere proizvod :



1. BTCPay automatski generiše Bitcoin ili Lightning** fakturu.



2. Na ekranu se pojavljuje **QR kod**.



3. Kupci mogu **skenirati i platiti direktno** sa svojim Bitcoin wallet.




![capture](assets/fr/27.webp)



### Konačni rezultat



Sada imate kompletan **Bitcoin Point of Sale** koji možete:





- Otvorite sa pametnog telefona ili tableta u vašoj prodavnici ;





- Prikaži na ekranu za skeniranje od strane kupca ;





- Ili podelite putem javnog **URL**, kao pojednostavljenu stranicu narudžbine.



Sa svakom uplatom, iznos se automatski pripisuje na **vaš sopstveni BTCPay wallet**, bez posrednika ili naknada trećih strana.


Ovo pretvara vaš PoS u **samostalni Bitcoin terminal za plaćanje**.




## Svakodnevna upotreba



Pre nego što unovčite bilo kakve stvarne isplate, preporučujemo da sprovedete **test** kako biste proverili da li sve funkcioniše ispravno.



### Testiraj uplatu





- Kreirajte fakturu** iz vašeg PoS interfejsa (na primer, proizvod 1 satoshi ili mala količina).





- Skenirajte QR kod na ekranu** koristeći Bitcoin ili Lightning wallet (kao što su **Phoenix**, **Muun** ili **Wallet od Satoshi**).




![capture](assets/fr/28.webp)





- Potvrdite uplatu** u vašem wallet: transakcija se šalje trenutno.





- Povratak na BTCPay Server**: faktura će se pojaviti kao **Plaćena** na listi.



![capture](assets/fr/29.webp)



Čestitamo! Vaš prodajni sistem je sada **funkcionalan**. Možete početi primati Bitcoin uplate od svojih kupaca, jednostavno, brzo i bez posrednika.



### Kreirajte fakturu za kupca



U meniju **Invoices** kliknite na **New invoice**.



![capture](assets/fr/30.webp)



Unesite **iznos** i **lokalnu valutu** (BTCPay automatski izračunava protivvrednost u BTC), kao i ostale informacije o proizvodu.



![capture](assets/fr/31.webp)



Podelite **QR kod** ili **URL** sa kupcem.



![capture](assets/fr/32.webp)



### Prati plaćanja primljena



Još uvek u meniju **Fakture**, videćete listu svih vaših transakcija.


Mogući statusi su :





- Na čekanju**: uplata još nije potvrđena.





- Plaćeno**: uplata potvrđena.





- Isteklo**: faktura nije plaćena do datuma dospeća.



### Vraćanje novca kupcu



U meniju **Invoices** izaberite fakturu za refundaciju.



![capture](assets/fr/33.webp)



Kliknite na **Refund** i unesite Bitcoin adresu koju je obezbedio kupac.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Izveštaji i izvoz podataka



BTCPay Server vam omogućava da **izvezete svoje transakcije** (u CSV ili Excel formatu). Ovo je veoma praktično za vaše knjigovodstvo i praćenje blagajne.



![capture](assets/fr/36.webp)



U meniju **Izveštaj** kliknite na **Izvoz**: sve vaše transakcije će biti sačuvane u CSV fajlu, koji potom možete pregledati lokalno.



## Bezbednost i najbolje prakse



Autonomija koju pruža BTCPay Server (potpuna suverenost nad vašim sredstvima) je prava snaga. Ali uz ovu slobodu dolazi i veća odgovornost u pogledu bezbednosti. Upravljanjem sopstvenim plaćanjima, preuzimate ulogu svoje banke. Zato je imperativ usvojiti najbolje prakse kako biste zaštitili svoja sredstva, svoje podatke i svoju infrastrukturu. Ovde su glavne tačke koje treba razmotriti.



### Osigurajte pristup svom serveru





- Koristite jaku lozinku: kombinujte velika i mala slova, brojeve i specijalne karaktere. Izbegavajte ponovno korišćenje postojeće lozinke.
- Aktivirajte dvofaktorsku autentifikaciju (2FA) da biste pristupili svom BTCPay interfejsu.
- Redovno ažurirajte svoj operativni sistem, svoju BTCPay Server instance i svoje zavisnosti (Docker, Bitcoin node, Lightning node...). Ažuriranja često ispravljaju bezbednosne ranjivosti.



### Upravljanje i pravljenje rezervnih kopija privatnih ključeva





- Sačuvajte svoje privatne ključeve i seed fraze van mreže, na fizičkom mediju (papir ili metal).
- Po mogućstvu koristite wallet hardver wallet.
- Čuvajte nekoliko kopija svojih rezervnih kopija, na odvojenim, zaštićenim fizičkim lokacijama.



### Sigurna plaćanja i poverljivost





- Koristite Tor mrežu ili VPN da sakrijete IP adresu vašeg servera i zaštitite vašu privatnost.
- Onemogući nepotrebne portove na svom serveru i ograniči SSH konekcije samo na pouzdane adrese.
- Aktivirajte HTTPS (SSL sertifikat) za sve veze sa vašim BTCPay web interfejsom.
- Nikada ne delite svoj administrativni interfejs sa osobljem koje nije obučeno za upravljanje portfoliom Bitcoin.



### Implementacija najboljih praksi za Lightning mrežu



Vaša prodavnica je povezana sa **Lightning čvorom hostovanim na Voltage**, što znatno pojednostavljuje tehničko upravljanje mrežom. Ipak, ostaje važno usvojiti **dobre prakse nadzora i bezbednosti**:





- Sačuvajte podatke za prijavu i pristupne ključeve vašeg Voltage čvora API** (koji omogućavaju povezivanje BTCPay-a).
- Zaštitite svoj Voltage nalog** dvofaktorskom autentifikacijom i jakom lozinkom.
- Pratite status čvora i kanala** sa vaše Voltage kontrolne table: ovo vam pomaže da uočite bilo kakve anomalije ili desinhronizaciju.
- Izbegavajte deljenje vaših API** akreditiva ili njihovo javno izlaganje (npr. u kodu sajta).
- U slučaju migracije, jednostavno **ponovo konfigurišite vezu između BTCPay i Voltage**: nijedan kanal ne treba ručno zatvarati.



Sa Voltage-om, imate koristi od **sigurne, visoko dostupne** i **automatski bekapovane** infrastrukture, dok zadržavate **punu suverenost nad vašim Lightning plaćanjima**.



### Organizujte i strukturirajte interne procedure





- Definišite jasnu politiku upravljanja pristupom: ko može kreirati fakturu, pregledati uplate, pristupiti čvoru, itd.
- Dokumentujte vaše procedure za bekap i vraćanje podataka kako biste mogli brzo reagovati u slučaju incidenta.
- Redovno testirajte obnavljanje svojih rezervnih kopija kako biste bili sigurni da rade ispravno.
- Obučite svoje osoblje ili saradnike u osnovnoj operativnoj bezbednosti: budnost protiv fišinga, korišćenje sigurnih lozinki, poštovanje poverljivosti.



### Nadzirati i uspostaviti stalno održavanje





- Kontinuirano pratite aktivnost vašeg servera koristeći alate za logovanje ili nadgledanje.
- Zakažite periodični pregled bezbednosti: proverite ažuriranja, pristup, rezervne kopije i doslednost transakcija.



Čestitamo! Stigli ste do kraja ovog tutorijala. Sada možete samostalno koristiti BTCPay Server, što će vam olakšati upravljanje vašom prodavnicom.



Da biste saznali više, preporučujem da pohađate naš kompletan kurs obuke o integraciji Bitcoin u vašu kompaniju:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a