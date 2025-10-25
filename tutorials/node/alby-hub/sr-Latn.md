---
name: Alby Hub
description: Kako lako pokrenuti svoj Lightning čvor?
---
![cover](assets/cover.webp)


Alby Hub je najnoviji softver otvorenog koda od Alby-ja, kompanije koja stoji iza popularne Lightning web ekstenzije. Alby Hub je samostalni novčanik sa Lightning čvorom koji je najlakši za korišćenje, dostupan sa bilo kog mesta za integraciju sa desetinama aplikacija. Alby Hub je jednostavan interfejs za korišćenje za upravljanje Lightning čvorovima.


U ovom vodiču ćemo pogledati različite načine korišćenja Alby Hub-a kako bismo ga povezali sa Alby Go, Alby-jevom mobilnom aplikacijom ili Alby web ekstenzijom. Ovo će vam omogućiti da trošite svoj satošije u pokretu dok ste autonomni u upravljanju vašim čvorom.


![ALBY HUB](assets/fr/01.webp)


## Šta je Alby Hub?


Alby Hub je postavljen da bude novi vodeći alat u Alby ekosistemu. Ovaj softver omogućava korisnicima da lako upravljaju sopstvenim novčanikom u samostalnom vlasništvu (self-custodial), uz integrisani Lightning čvor, pri čemu zadržavaju kontrolu nad svojim ključevima (samostalno čuvanje).


Alby Hub je veoma prilagodljiv alat. Može zadovoljiti potrebe i početnika i naprednih korisnika. Početnici će ga koristiti za jednostavno upravljanje pravim Lightning čvorom, bez potrebe da se suočavaju sa složenošću u pozadini. Za iskusnije korisnike, Alby Hub može služiti kao kompletan interfejs za napredno upravljanje postojećim Lightning čvorom.


U zavisnosti od vaših potreba, Alby Hub je dostupan u 4 konfiguracije:




- **Alby Hub Cloud :**


Ova prva opcija – Alby cloud – idealna je za početnike. Omogućava vam da postavite Hub direktno na server koji održava Alby, kojem pristupate putem Alby Hub interfejsa. Iako Alby upravlja serverom, zadržavate suverenitet nad vašim sredstvima, jer su vaši ključevi šifrovani pomoću lozinke poznate samo vama. Međutim, vaši ključevi moraju ostati dešifrovani u RAM-u kako bi čvor mogao da funkcioniše, što ih teoretski izlaže riziku ako neko fizički pristupi serveru. To je zanimljiv kompromis za početnike, ali je važno biti svestan rizika.


Glavna prednost ove opcije je što dobijate Lightning čvor koji radi 24/7, bez potrebe da sami upravljate hostingom. Štaviše, bekapi vašeg Lightning čvora su pojednostavljeni i automatizovani, u poređenju sa opcijama samostalnog hostovanja gde morate sami upravljati bekapima kanala.


Alby Cloud je plaćena usluga [Pogledajte njihove cene](https://albyhub.com/#pricing) za više detalja. Naknada se automatski oduzima iz vašeg novčanika putem Lightning fakture koju izdaje Alby. Ovo se vrši preko NWC konekcije koja konfiguriše vaš čvor da automatski plaća Alby fakture vezane za vašu pretplatu.





- **Alby Hub sa postojećim čvorom :**


Ako već imate hostovan čvor, na primer na Umbrel-u ili Start9, Alby Hub se može koristiti kao napredni interfejs za upravljanje, na isti način kao ThunderHub ili RTL.




- **Alby Hub lokal :**


Moguće je instalirati Alby Hub direktno na vaš PC, iako je ova opcija manje praktična, jer vaš PC mora ostati aktivan sve vreme kako biste daljinski pristupili Lightning čvoru. Međutim, ova alternativa može biti pogodna za vaše specifične potrebe.




- **Alby Hub na ličnom serveru :**


Za napredne korisnike, Alby Hub se može implementirati na ličnom serveru jednostavnom komandom. Ova opcija nije pokrivena u ovom vodiču, ali možete pronaći posebna uputstva [na Alby-jevom GitHub-u](https://github.com/getAlby/hub?tab=readme-ov-file#docker).


Ovaj vodič se uglavnom fokusira na interfejs, koji će biti isti bez obzira na izabranu opciju. Takođe ćemo pogledati kako da implementiramo Alby Hub sa plaćenom cloud opcijom, a zatim sa opcijom node-in-box (Umbrel ili Start9).


![ALBY HUB](assets/fr/02.webp)


Za lokalnu instalaciju na vašem računaru, [preuzmite i instalirajte softver prema vašem operativnom sistemu](https://github.com/getAlby/hub/releases), zatim pratite iste instrukcije na interfejsu.


![ALBY HUB](assets/fr/03.webp)


## Kreiraj Alby nalog


Prvi korak je kreiranje Alby naloga. Iako ovo nije neophodno za korišćenje Alby Hub-a, omogućava vam da u potpunosti iskoristite dostupne opcije, uključujući mogućnost dobijanja Lightning adrese.


Idite na [zvaničnu Alby veb stranicu](https://getalby.com/) i kliknite na dugme "*Create Account*".


![ALBY HUB](assets/fr/04.webp)


Unesite nadimak i email adresu, zatim kliknite na "*Sign up*". Ovaj email će se kasnije koristiti za prijavu na vaš nalog.


![ALBY HUB](assets/fr/05.webp)


Unesite verifikacioni kod koji ste primili putem e-pošte.


![ALBY HUB](assets/fr/06.webp)


Kada se prijavite na svoj online nalog, kliknite na dugme "*Nastavi*", engleski "*Continue*".


![ALBY HUB](assets/fr/07.webp)


Kliknite "*Continue*" ponovo.


![ALBY HUB](assets/fr/08.webp)


## Opcija hostovanja u oblaku


Zatim ćete morati da birate između opcije sa sopstvenim hostingom, gde instalirate Alby Hub na sopstveni uređaj, ili premium opcija. Počeću objašnjenjem kako da nastavite sa Pro Cloud opcijom (imajte na umu da je ovo plaćena opcija, detalje pogledajte u prethodnom odeljku).


Kliknite na "*Upgrade*".


![ALBY HUB](assets/fr/09.webp)


Potvrdite klikom na "*Subscribe Now*".


![ALBY HUB](assets/fr/10.webp)


Kliknite na "*Launch Alby Hub*".


![ALBY HUB](assets/fr/11.webp)


Sačekajte nekoliko trenutaka dok se vaš čvor kreira.


![ALBY HUB](assets/fr/12.webp)


I to je to, vaš Alby Hub je sada konfigurisan. U sledećem delu pokazaću vam kako da instalirate Alby Hub na postojeći čvor. Ako još uvek nemate Lightning čvor, možete preći na sledeći odeljak da biste konfigurisali Alby Hub na Alby Cloud-u.


![ALBY HUB](assets/fr/13.webp)


## Opcija samostalnog hostovanja


Ako više volite da koristite Alby Hub kao interfejs za vaš postojeći Lightning čvor, imate nekoliko opcija: instalirajte ga na server, lokalno na vašem računaru, ili putem node-in-box (Umbrel ili Start9). Korišćenje Alby Hub-a u ovim konfiguracijama je besplatno. Fokusiraćemo se na opciju node-in-box, jer smatram da opcija servera, bez fizičkog pristupa, predstavlja slične rizike kao i verzija u oblaku, a lokalna instalacija na PC-u je često neprikladna.


Da biste ovo postavili na Umbrel (koraci za Start9 su identični), prvo morate imati već konfigurisan LND čvor.


Prijavite se na svoj Umbrel interfjes i idite u prodavnicu aplikacija.


![ALBY HUB](assets/fr/14.webp)


Potraži aplikaciju "*Alby Hub*".


![ALBY HUB](assets/fr/15.webp)


Instalirajte ga na vaš čvor.


![ALBY HUB](assets/fr/16.webp)


Vaš Alby Hub interfejs je sada spreman. Možete pratiti ostatak tutorijala kao da koristite cloud interfejs, ali bez opcija plaćene verzije. Štaviše, za razliku od cloud verzije, vaši ključevi su sačuvani lokalno na vašem čvoru, a ne na Albyjevim serverima.


![ALBY HUB](assets/fr/17.webp)


## Pokreni Alby Hub


Kliknite na dugme "*Get Started*".


![ALBY HUB](assets/fr/18.webp)


Alby Hub će vas zatim zatražiti da izaberete lozinku. Ova lozinka je veoma važna, jer će se koristiti za šifrovanje vašeg novčanika. U plaćenoj verziji u oblaku, vaši ključevi se čuvaju na Alby serveru, šifrovani ovom lozinkom koju samo vi znate, zatim dešifrovani i čuvani samo u RAM-u za potpisivanje transakcija kada je to potrebno.


Stoga je neophodno odabrati jaku lozinku. Svako ko ima ovu lozinku mogao bi potencijalno dobiti pristup vašem čvoru. Uverite se da ste napravili jednu ili više fizičkih kopija ove lozinke na papiru, ili još bolje, na komadu metala radi dodatne sigurnosti.


Kada pažljivo odaberete i sačuvate svoju lozinku, kliknite na "*Create Password*".


![ALBY HUB](assets/fr/19.webp)


Sada imate pristup svom Lightning čvoru.


![ALBY HUB](assets/fr/20.webp)


Prva akcija koju treba preduzeti je da sačuvate svoju frazu za oporavak, iz koje se izvode vaši ključevi. Da biste to uradili, kliknite na "Settings". Ova fraza vam omogućava da povratite pristup vašem novčaniku ako ste omogućili automatske rezervne kopije.


![ALBY HUB](assets/fr/21.webp)


Zatim idite na karticu "*Backup*". Unesite svoju lozinku da biste pristupili.


![ALBY HUB](assets/fr/22.webp)


Zatim ćete imati pristup svojoj frazi za oporavak od 12 reči. Napravite jednu ili više fizičkih kopija ove fraze na papiru ili metalu i čuvajte ih na sigurnom mestu.


![ALBY HUB](assets/fr/23.webp)


Kada sačuvate frazu, označite polje da potvrdite da ste je sačuvali i kliknite na "*Continue*".


![ALBY HUB](assets/fr/24.webp)


## Kako mogu povratiti pristup svojim bitcoinima?


Pre nego što pošaljete sredstva na vaš Alby Hub, važno je razumeti kako ih povratiti u slučaju problema, kao i koje su informacije potrebne za ovaj povratak. Proces se razlikuje u zavisnosti od prirode sredstava koja treba povratiti i načina hostovanja vašeg čvora.


Za korisnike plaćenog clouda, potpuni oporavak vaših bitkoina zahteva tri osnovna elementa:



- Vaša fraza za oporavak;
- Pristup vašem Alby nalogu, za preuzimanje automatskih rezervnih kopija.


Odsustvo bilo koje od ove 2 informacije učinilo bi nemogućim da povratite svoje bitkoine u potpunosti.


Za one koji pokreću Alby Hub na sopstvenom uređaju, proces oporavka je dokumentovan [ovde](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).


Ako ste instalirali Alby Hub na postojećem čvoru, moraćete da pratite proces oporavka tog specifičnog operativnog sistema čvora. Na primer: Umbrel nudi [opciju](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) da šifruje najnoviji status vaših Lightning kanala i sačuva ga dinamički i anonimno putem Tor-a. Imajte na umu da samo automatske sigurnosne kopije iz Alby-ja omogućavaju da potpuno oporavite vaš Hub bez zatvaranja bilo kojih kanala.


## Kupite svoj prvi Lightning kanal


Sada možete pratiti uputstva koja pruža Alby Hub. Kliknite na dugme da otvorite svoj prvi kanal za dolazni novac.


![ALBY HUB](assets/fr/25.webp)


Odaberite "*Open Channel*". Ako ne nameravate da postanete čvor za rutiranje i ne trebate ga posebno, preporučujem da se odlučite za privatne kanale.


![ALBY HUB](assets/fr/26.webp)


Alby Hub će generisati fakturu za vas koju trebati platiti. Ova uplata pokriva troškove transakcije potrebne za otvaranje vašeg kanala, kao i naknade za uslugu LSP-a (*Lightning Service Provider*) koji će otvoriti kanal prema vašem čvoru, omogućavajući vam da odmah primate uplate.


![ALBY HUB](assets/fr/27.webp)


Kada je faktura plaćena i transakcija potvrđena, vaš prvi Lightning kanal je uspostavljen.


![ALBY HUB](assets/fr/28.webp)


U kartici "*Node*" možete videti da sada imate dolazni novac, što vam omogućava da primate uplate putem Lightning-a.


![ALBY HUB](assets/fr/29.webp)


Da biste primili uplatu, kliknite na karticu "*Wallet*" a zatim na "*Receive*".


![ALBY HUB](assets/fr/30.webp)


Unesite iznos i dodajte opis ako je potrebno, zatim kliknite na "*Create Invoice*".


![ALBY HUB](assets/fr/31.webp)


Primio sam svoju prvu uplatu od 120,000 satošija.


![ALBY HUB](assets/fr/32.webp)


Vraćanjem na karticu "*Wallet*" možete proveriti svoj saldo na novčaniku. Imajte na umu da Alby Hub automatski izdvaja 354 satošija kada izvršite svoju prvu uplatu. Za svaki Lightning kanal koji otvorite nakon toga, Alby Hub će automatski izdvojiti rezervu ekvivalentnu 1% kapaciteta kanala. Ova rezerva je sigurnosna mera koja omogućava vašem čvoru da povrati sredstva iz kanala u slučaju pokušaja prevare od strane vašeg partnera. Zato, iako sam poslao 120,000 satošija, na mom saldu je prikazano samo 119,646 Sats (satošija).


![ALBY HUB](assets/fr/33.webp)


## Uplata bitkoina na blokčejn/on-chain


Ako želite da imate odlazni novac za plaćanja, možete i sami otvoriti kanal. Da biste to uradili, trebaju vam onchain bitcoini u vašem novčaniku.


Sa kartice "*Node*", kliknite na "*Deposit*".


![ALBY HUB](assets/fr/34.webp)


Pošaljite bitkoine na prikazanu adresu. Ova adresa je izvedena iz vaše prethodno sačuvane fraze za oporavak.


![ALBY HUB](assets/fr/35.webp)


Poslao sam 72.000 Sats. Sada su vidljivi u "*Savings Balance*", koje uključuje sva sredstva koja posedujem na lancu, a ne na Lightning-u.


![ALBY HUB](assets/fr/36.webp)


## Otvorite Lightning kanal


Sada kada imate sredstva na lancu, možete otvoriti novi Lightning kanal. Preporučljivo je otvoriti nekoliko kanala, sa dovoljnim iznosima kako biste osigurali da uvek možete izvršavati plaćanja bez ograničenja. Većina LSP-ova (*Lightning Service Providers*) zahteva minimum od 150,000 Sats za otvaranje kanala sa vama.


U kartici "*Node*", kliknite na "*Open Channel*".


![ALBY HUB](assets/fr/37.webp)


Odaberite veličinu vašeg kanala. Preporučujem da ne otvarate kanale koji su previše mali, imajući na umu da je ovo Lightning čvor i da mašina koja hostuje vaše ključeve ne nudi isti nivo sigurnosti kao hardverski novčanici. Zato budite pažljivi sa iznosima koje odlučite da blokirate.


![ALBY HUB](assets/fr/38.webp)


U meniju "*Advanced Options*", možete izabrati sa kojim LSP-om ćete otvoriti vaš kanal, ili ručno uneti drugi Lightning čvor.


![ALBY HUB](assets/fr/39.webp)


Zatim kliknite na "*Open Channel*".


![ALBY HUB](assets/fr/40.webp)


Sačekajte dok se vaš kanal ne potvrdi na lancu.


![ALBY HUB](assets/fr/41.webp)


Vaš novi kanal će se sada pojaviti na kartici "*Node*".


![ALBY HUB](assets/fr/42.webp)


## Upravljanje čvorovima


Upravljanje vašim Lightning kanalima je lakše nego što mislite. Alby Hub vam omogućava da prenesete Sats između vašeg potrošnog salda i vašeg On-Chain salda. Tako možete povećati kapacitet potrošnje ili primanja.


![ALBY HUB](assets/fr/66.webp)


## Povežite aplikaciju za troškove


Sada kada imate funkcionalan Lightning čvor, možete ga koristiti za primanje i trošenje satošija na dnevnoj bazi. Iako je veb interfejs Alby Hub-a zgodan za upravljanje vašim čvorom, nije idealan za brzo obavljanje transakcija u pokretu. Za ovo ćemo koristiti aplikaciju Lightning novčanik instaliran na našem pametnom telefonu.


U ovom vodiču preporučujem da se odlučite za Alby Go, koji je vrlo jednostavan za korišćenje, ali možete koristiti i druge kompatibilne aplikacije kao što je Zeus.


![ALBY HUB](assets/fr/43.webp)


Da biste instalirali Alby Go, idite u prodavnicu aplikacija na svom uređaju:




- [Za Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Za Apple](https://apps.apple.com/us/app/alby-go/id6471335774).


![ALBY HUB](assets/fr/44.webp)


Android korisnici takođe mogu instalirati aplikaciju putem `.apk` fajla [dostupnog na Albyjevom GitHub-u](https://github.com/getAlby/go/releases).


![ALBY HUB](assets/fr/45.webp)


Kada se aplikacija pokrene, kliknite na "*Connect Wallet*".


![ALBY HUB](assets/fr/46.webp)


U vašem Alby Hub-u, ispod App Store-a, pronađite “Alby Go” i kliknite na “Connect”

![ALBY HUB](assets/fr/47.webp)

Kliknite na „Connect with One-Tab Connections“. Ovo će vam omogućiti da povežete vaš Alby Hub jednim klikom sa drugim aplikacijama koristeći Alby Go.


![ALBY HUB](assets/fr/48.webp)


Alby Hub će zatim generisati tajnu da uspostavi vezu sa Alby Go.


![ALBY HUB](assets/fr/49.webp)


Vratite se na aplikaciju Alby Go, skenirajte QR kod ili nalepite tajnu.


![ALBY HUB](assets/fr/50.webp)


Kliknite na "*Finish*".


![ALBY HUB](assets/fr/51.webp)


Sada imate daljinski pristup svom Lightning čvoru putem Alby Hub-a sa svog pametnog telefona, što vam omogućava da lako trošite i primate satošije u pokretu, svakog dana.


![ALBY HUB](assets/fr/52.webp)


Ako je potrebno, možete upravljati dozvolama za ovu vezu direktno na Alby Hubu klikom na nju.


![ALBY HUB](assets/fr/53.webp)


Da biste primili Sats, jednostavno kliknite na "*Receive*".


![ALBY HUB](assets/fr/54.webp)


Izmenite iznos i opis za fakturu klikom na "*Invoice*".


![ALBY HUB](assets/fr/55.webp)


Naplatite fakturu da biste primili satošije.

![ALBY HUB](assets/fr/56.webp)


Da biste poslali Sats, kliknite na "*Send*".


![ALBY HUB](assets/fr/57.webp)


Skenirajte fakturu koji želite platiti.


![ALBY HUB](assets/fr/58.webp)


Zatim kliknite na "*Plati*".


![ALBY HUB](assets/fr/59.webp)


Vaša transakcija je potvrđena.


![ALBY HUB](assets/fr/60.webp)


Klikom na malu strelicu, možete pristupiti istoriji transakcija.


![ALBY HUB](assets/fr/61.webp)


Ove transakcije su takođe vidljive na vašem Alby Hub-u.


![ALBY HUB](assets/fr/62.webp)


## Prilagodite svoju Lightning adresu


Alby vam nudi opciju Lightning adrese. Ovo vam omogućava da primate uplate na vaš čvor bez potrebe da ručno generišete i fakturu svaki put. Po defaultu, Alby vam dodeljuje Lightning adresu, ali je možete prilagoditi. Prijavite se na vaš Alby online nalog, kliknite na vaše ime u gornjem desnom uglu, zatim izaberite "*Settings*".


![ALBY HUB](assets/fr/63.webp)


Idite na meni "*Lightning Address*".


![ALBY HUB](assets/fr/64.webp)


Izmenite svoju adresu, zatim potvrdite klikom na "*Update your lightning Address*".


![ALBY HUB](assets/fr/65.webp)


Imajte na umu da kada vaš adresa bude promenjena, više vam ne pripada. Zato se postarajte da nikada više ne šaljete satošije na tu adresu.


I to je to, sada znate kako da koristite Lightning sa svojim čvorom koristeći Alby Hub alat. Ako ste smatrali da je ovaj vodič koristan, bio bih veoma zahvalan ako biste kliknuli na zeleni palac dole. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!


Da biste detaljno razumeli sve Lightning mehanizme koje smo koristili u ovom vodiču, toplo vam preporučujem da otkrijete naš besplatni trening na tu temu :


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
