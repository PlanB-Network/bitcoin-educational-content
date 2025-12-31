---
name: Matrix
description: Vodič za razumevanje, konfigurisanje i korišćenje Matrix-a, sigurnog, otvorenog i decentralizovanog komunikacionog platforma.
---

![cover](assets/cover.webp)



## Šta je Matrix?



Matrix je **decentralizovani komunikacioni protokol** dizajniran da omogući razmenu poruka, fajlova i audio/video poziva između korisnika i aplikacija, bez oslanjanja na centralno preduzeće. Za razliku od tradicionalnih platformi za razmenu poruka, Matrix je **otvorena infrastruktura**, uporediva sa email-om: svako može izabrati server ili ga samostalno upravljati, zadržavajući mogućnost razmene sa ostatkom mreže.



Matrica se odlikuje trima temeljnim principima:



### Protokol, ne aplikacija



Matrix nije aplikacija kao WhatsApp ili Telegram.


To je standardizovani jezik koji mnoge aplikacije mogu koristiti.


Drugim rečima, širok spektar Element softvera, FluffyChat, Cinny, Nheko i drugi, omogućavaju pristup istoj Matrix mreži.



Ovo garantuje potpunu slobodu: promena aplikacije bez gubitka kontakata, raznovrsnost interfejsa, nezavisnost od jednog dobavljača.



![capture](assets/fr/03.webp)



### Decentralizovana, federisana mreža



Struktura Matrix-a zasniva se na **federaciji**, modelu u kojem nekoliko nezavisnih servera sarađuje međusobno.


Svaki server (nazvan _homeserver_) može da hostuje korisnike, sobe za ćaskanje i sinhronizuje poruke sa drugim serverima na mreži.


Tako:





- nijedan entitet ne kontroliše ceo sistem;
- server može nestati bez uticaja na ostatak mreže;
- svaka organizacija ili pojedinac može upravljati svojim prostorom.



Ovaj model osigurava **visoku otpornost** i odražava vrednosti tehnološkog suvereniteta.



![capture](assets/fr/03.webp)



### Siguran, šifrovan sistem



Matrix podržava **end-to-end enkripciju (E2EE)** za privatne razmene i enkriptovane grupe.


Poruke mogu čitati samo učesnici, ne i posrednički serveri.


Ovaj pristup omogućava komunikaciju bez izlaganja sadržaja razmene trećoj strani, uz zadržavanje transparentnosti protokola i mogućnosti hostovanja sopstvenog servera.



![capture](assets/fr/05.webp)



### Jedinstvena interoperabilnost



Jedna od glavnih prednosti Matrix-a je njegova sposobnost da deluje kao **most između različitih komunikacionih sistema**. Zahvaljujući _mostovima_, moguće je povezati :





- Telegram
- WhatsApp
- Signal
- Messenger
- Slack
- Discord
- IRC, XMPP, itd.



Ovo omogućava ujedinjenje zajednica rasutih po nekoliko platformi, uz zadržavanje kontrole nad infrastrukturom.



![capture](assets/fr/06.webp)



## Kako Matrix funkcioniše?



Ovaj odeljak prikazuje unutrašnju strukturu Matrix mreže kako bi se razumelo kako korisnici, serveri i aplikacije međusobno deluju unutar ovog decentralizovanog ekosistema. Matrix se zasniva na tri osnovna elementa: _homeserverima_, identitetima i _klijentima_ koji se koriste za komunikaciju.



### Serveri: kućni serveri



Matrix radi na nezavisnim serverima koji se zovu _homeservers_.


Svaki homeserver upravlja :





- korisničke naloge koje hostuje,
- privatni razgovori i saloni u kojima ovi korisnici učestvuju,
- sinhronizacija sa drugim mrežnim serverima.



Svi kućni serveri povezani na Matrix mrežu automatski razmenjuju poruke i događaje iz zajedničkih dnevnih soba. Na primer:





- korisnik registrovan na serveru A može da ćaska sa korisnikom na serveru B,
- salon može biti raspoređen na desetine servera,
- niko nema kontrolu nad salonom ili zajednicom u celini.



Ovaj model je veoma otporan i omogućava svakoj organizaciji ili pojedincu da upravlja sopstvenom infrastrukturom.



### Identifikatori matrica



Svaki korisnik ima jedinstveni identifikator, nazvan **MXID** (_Matrix ID_), koji izgleda kao adresa:



```bash
@nomdutilisateur:serveur.xyz
```



Sastoji se od :





- korisničko ime, ispred kojeg stoji **@**
- ime servera na kojem je nalog kreiran, prethodi **:**



Primeri:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Ovaj identifikator omogućava komunikaciju sa bilo kojim drugim Matrix korisnikom, bez obzira na server sa kojeg potiče.



### Matrix klijenti (aplikacije)



Da biste koristili Matrix, potrebno je da se povežete sa aplikacijom koja se zove **klijent Matrix**.



Najpoznatiji su :





- Element (web, mobilni, desktop)
- FluffyChat (mobilni)
- Cinny (minimalistički web/desktop)
- Nheko (desktop)



Ove aplikacije su samo interfejsi za :





- da biste videli poruke,
- pošalji tekst, slike ili datoteke,
- pridružite se ili kreirajte sajmove,
- obavljati audio/video pozive.



Sve aplikacije komuniciraju sa serverima putem istog standardizovanog protokola.



### Sobe i privatne poruke (DM)



U Matrixu, razmene se odvijaju u **sobama** :





- soba može biti javna ili privatna
- može da primi dvoje ljudi ili hiljade
- može se deliti između nekoliko servera
- ima jedinstveni identifikator koji počinje sa **!**



Privatne poruke su jednostavno sobe za ćaskanje sa dva učesnika, često se nazivaju **DM (Direct Messages)**.



Sinhronizacija salona odvija se u realnom vremenu između učesničkih servera, osiguravajući besprekorno iskustvo uz održavanje decentralizacije.



## Zašto koristiti Matrix?



Matrix nije samo alternativa centralizovanim sistemima za razmenu poruka: to je tehnologija koja zadovoljava stvarne potrebe u pogledu digitalnog suvereniteta, bezbednosti i interoperabilnosti. Postoji mnogo razloga zašto sve više ljudi, kompanija i institucija bira ovaj protokol za komunikaciju.



### Povratite kontrolu nad vašim komunikacijama



Većina platformi za razmenu poruka funkcioniše na centralizovanom modelu: jedan igrač kontroliše servere, pristup, podatke i pravila korišćenja. Ovaj model podrazumeva potpunu zavisnost od dobavljača.


Matrix pristupa na drugačiji način.


Svako može izabrati gde će hostovati svoj nalog, ili čak postaviti sopstveni server. Nijedan entitet nije u poziciji da blokira korisnika, zahteva nametljivo identifikovanje ili nametne promenu politike.


Ova arhitektura vraća autonomiju i pojedincima i organizacijama. Komunikacije više nisu zasnovane na poverenju u kompaniju, već na otvorenom, dokumentovanom i proverljivom protokolu.



### Sigurna, šifrovana komunikacija



Matrix podržava end-to-end enkripciju za privatne razgovore i grupe. Ovaj mehanizam osigurava da samo učesnici mogu čitati poruke, čak i ako one prolaze kroz servere trećih strana u federaciji.



Protokol koristi Megolm/Olm algoritam, dizajniran posebno za pružanje snažne sigurnosti u distribuiranim okruženjima sa više uređaja.



Ovo omogućava da :





- zaštititi osetljive razgovore,
- sprečiti neovlašćeni pristup (čak i sa serverskog hosta),
- održavajte poverljivost na duži rok.



Šifrovanje nije opcija: to je osnovna komponenta protokola.



### Više nije zavisan od jedne aplikacije



Matrix nije aplikacija, već protokol.



Ova raznolikost kupaca garantuje :





- izbor prilagođen individualnim potrebama,
- sposobnost korišćenja Matrix-a na bilo kojoj vrsti uređaja,
- nema zavisnosti od jednog softvera.



Ako je kupac nepodoban ili se prestane održavati, jednostavno odaberite drugog: račun nastavlja normalno da funkcioniše.



### Federisanje i međusobno povezivanje različitih zajednica



Federacija omogućava različitim serverima da rade zajedno dok se upravljaju nezavisno.


Tako:





- organizacija može upravljati sopstvenim homeserverom,
- pojedinci mogu da se pridruže javnim serverima,
- svi mogu komunicirati jedni s drugima kao da su na istoj platformi.



Ova fleksibilnost omogućava kreiranje komunikacionih prostora prilagođenih svakoj potrebi: timovima, udruženjima, zajednicama, institucijama ili open source projektima.



Matrix je posebno popularan u tehničkim krugovima, aktivističkim kolektivima, istraživačima, vladama i sve više u Bitcoin zajednicama.



### Jedinstvena interoperabilnost u pejzažu razmene poruka



Jedna od glavnih prednosti Matrix-a je njegova sposobnost da **proširi** razmene zahvaljujući mostovima koji mogu povezati :





- WhatsApp
- Telegram
- Signal
- Slack
- Discord
- IRC
- XMPP
- i mnoge druge platforme



Matrica tako postaje ujedinjujući sloj za komunikacije, okupljajući nekoliko zajednica raspršenih po različitim aplikacijama.



Ova interoperabilnost smanjuje fragmentaciju i pojednostavljuje saradnju.



### Besplatan, otvoren i održiv protokol



Matriks protokol je potpuno otvorenog koda i razvijen je transparentno.


Ovo garantuje nekoliko prednosti:





- kontinuirana evolucija standarda,
- mogućnost da bilo ko proveri kod,
- nezavisnost od komercijalnih ili političkih promena,
- dugoročna otpornost.



Za razliku od vlasničkih sistema za razmenu poruka, budućnost Matrix-a ne zavisi od jedne kompanije, već od globalne zajednice i otvorenog standarda.



## Kako da napravim Matrix nalog?



Kreiranje Matrix naloga je jednostavno i ne zahteva tehničke veštine. Korisnici mogu da se pridruže postojećem serveru, kreiraju prijavu i odmah počnu da ćaskaju. Ovaj odeljak opisuje osnovne korake.



### Izaberite server (javni ili privatni)



Matrix je federativna mreža: postoji mnogo servera (homeservera) kojima upravljaju različite organizacije, zajednice ili pojedinci. Izbor servera određuje samo _gde_ je nalog hostovan, ali ne sprečava komunikaciju sa celom mrežom.


**Dve opcije su dostupne:**



### - Koristite javni server



Ovo je najjednostavnije rešenje.


Primeri popularnih servera:





- _matrix.org_ (najpoznatiji)
- _envs.net_
- tematski servers zajednice (tehnologija, privatnost, otvoreni kod...)



Ovi serveri su pogodni za početnike koji žele brzo da se registruju.



### - Koristite privatni server



Idealno za :





- organizacija,
- porodica,
- projekat otvorenog koda,
- radni tim,
- ili za suverenu, samostalno hostovanu upotrebu.



U ovom slučaju, neko mora da upravlja serverom (Synapse, Dendrite, Conduit...).


Bez obzira na to koji server odaberete, korisnici mogu međusobno razgovarati zahvaljujući federaciji.



### Kreirajte nalog korak po korak



Kako je Matrix otvoren protokol, može mu pristupiti nekoliko aplikacija.


Kao što je opisano iznad, oni nude različite interfejse i funkcionalnosti u zavisnosti od zahteva:





- Element**: najkompletniji klijent, dostupan na svim platformama.
- FluffyChat**: jednostavan, moderan i idealan za mobilne uređaje.
- Nheko**: lagan, ergonomski klijent za računare.
- SchildiChat**: Element varijanta sa ergonomskim poboljšanjima.
- NeoChat**: integrisan u KDE ekosistem.



Izbor klijenta nema uticaja na nalog: svi rade sa bilo kojim Matrix serverom.



### Klasični koraci :





- Otvorite izabranu aplikaciju. U našem slučaju, to ćemo uraditi sa [Element](app.element.io).
- Izaberite "Kreiraj nalog".



![cover-kali](assets/fr/10.webp)



Radi jednostavnosti, možete kreirati Matrix nalog koristeći **Google, Facebook, Apple, GitHub ili GitLab**. Ove usluge će samo znati da je njihov nalog korišćen za pristup Matrix-u: ovo je poznato kao **socijalna konekcija**.



Radi veće poverljivosti, možete se registrovati ručno odabirom **korisničkog imena**, **lozinke** i **e-mail adrese**.



U zavisnosti od izabranog servera, može biti potreban **captcha**, kao i prihvatanje **uslova korišćenja**.



Jednom kada je registracija potvrđena, šalje se e-mail sa potvrdom.


Jednostavno kliknite na link da aktivirate svoj nalog i pristupite veb aplikaciji (Element) kako biste se pridružili svojim prvim Matrix razgovorima.



![cover-kali](assets/fr/11.webp)



Sada imate nalog i koristite Web verziju Elementa.



## Dodajte svoj prvi kontakt



Da biste komunicirali sa nekim na Matrix-u, sve što treba da znate je njihov puni identifikator, koji se zove **Matrix ID**.



Primer:



`@alice:matrix.org @bened:monserveur.bj`



### Dodaj kontakt



Da biste pozvali prijatelje u svoj grupni čet, kliknite na krug sa `i` u gornjem desnom uglu. Ovo otvara desni panel. Kliknite na "Ljudi" da prikažete listu članova u ovoj sobi: trenutno bi trebalo da ste jedini prisutni.



![cover-kali](assets/fr/12.webp)



Kliknite na "Pozovi u ovu sobu" na vrhu liste ljudi i otvoriće se prozor kako biste mogli da pozovete svoje prijatelje da vam se pridruže u Matrixu. Ako su već prijavljeni na Matrix, unesite njihov Matrix ID. Ako nisu, unesite njihovu e-mail adresu i biće pozvani da nam se pridruže.



Ne postoji sistem "prijatelja": kontakt je jednostavno osoba sa kojom je započet razgovor.



![cover-kali](assets/fr/13.webp)



Osoba koju ste pozvali može prihvatiti ili odbiti poziv. Ako prihvati, trebalo bi da ih vidite kako se pridružuju sobi. Što više, to bolje!



![cover-kali](assets/fr/14.webp)



### Postavljanje sopstvenog servera



Matrix zaista dolazi do izražaja kada se koristi u kombinaciji sa ličnim serverom.


Postavljanje sopstvenog kućnog servera omogućava vam da:





- održavajte potpunu kontrolu nad podacima,
- definiše sopstvena pravila korišćenja,
- ugostiti više naloga (prijatelji, tim, zajednica),
- i osigurati maksimalnu otpornost u slučaju ograničenja ili cenzure.



**Dostupna rešenja:**





- Synapse**: istorijska i najkompletnija implementacija.
- Dendrite**: lakši, snažniji i dizajniran za budućnost protokola.
- Conduit**: minimalistička varijanta koja se lako implementira.



**Preduslovi:**





- naziv domena,
- mašina ili VPS,
- minimalne veštine administracije sistema.



Čak i ako zahteva malo konfiguracije, upravljanje sopstvenim serverom pretvara Matrix u suveren i trajan alat.



### Pridruživanje vašim prvim sajmovima



Matrix se u velikoj meri oslanja na _sobe_ (dnevne sobe).


Postoje javni, privatni, zajednički, tehnički, lokalni i međunarodni sajmovi.



**Tri načina da se pridružite salonu:**



1. **Putem veze za poziv** (često u obliku `matrix.to` URL-a).


2. **Pretraga imena salona** u aplikaciji.


3. **Unošenjem punog ID-a emisije**, npr. :


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Jednom kada se pridružite, chatroom se ponaša kao klasična diskusiona grupa, sa istorijom, enkripcijom, fajlovima, reakcijama i audio/video pozivima, u zavisnosti od korišćenog klijenta.



![capture](assets/fr/09.webp)



## Idemo dalje



Kada savladate osnove, Matrix nudi mnoštvo naprednih mogućnosti. Bilo da želite povezati druge sisteme za razmenu poruka, hostovati sopstveni server ili organizovati zajednicu, ekosistem je veoma bogat.



### Mostovi (WhatsApp, Telegram, Signal, itd.)



Most povezuje Matrix sa drugim sistemima za razmenu poruka.


Sa njim možete slati i primati poruke od:





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discord
- Slack**
- IRC** (IRC)
- i mnogi drugi



### Šta mostovi mogu da urade





- Centralizujte sve vaše razgovore u Matrix
- Obezbedite otvoreni interfejs za interakciju sa vlasničkim uslugama
- Upravljajte zajednicom na više platformi sa jedne lokacije



Neki mostovi su zvanični, drugi su zasnovani na zajednici.


U zavisnosti od odeljenja, možda će zahtevati :





- lični server,
- dodatna konfiguracija,
- ili korišćenje postojećeg javnog mosta.



### Korišćenje Matrix-a za Bitcoin organizaciju, zajednicu ili projekat



Matrix nije samo lični alat.


Može se koristiti za strukturiranje radnih grupa, organizovanje lokalnih zajednica ili upravljanje komunikacijom projekta.



**Primeri upotrebe:**





- Zajednice otvorenog koda
- Bitcoin i projekti ekosistema Lightning
- Studentske ili developerske grupe
- Građanske organizacije
- Nezavisni mediji
- Lokalne grupe i udruženja



**Zašto je ovo zanimljivo?





- 100% open-source** alat
- Suverena i decentralizovana** komunikacija
- Prostori organizovani u **salone**, **podgrupe**, **privatne salone**, itd.
- Integracija sa Nextcloud, GitLab, Mattermost, ili prilagođenim botovima
- Fino podešeno upravljanje dozvolama i moderacijom



Matrix tada postaje stub komunikacije za svaku strukturu koja želi ostati nezavisna od velikih centralizovanih platformi.



## Zaključak



Matrix predstavlja moderno, otvoreno i sigurno rešenje za komunikaciju u realnom vremenu, nudeći decentralizovanu alternativu tradicionalnim platformama. Zahvaljujući svojoj federativnoj arhitekturi i naprednim enkripcijskim protokolima, omogućava korisnicima da zadrže kontrolu nad svojim podacima dok uživaju u fluidnom, interoperabilnom iskustvu. Bilo za ličnu, profesionalnu ili zajedničku upotrebu, Matrix nudi robustan i skalabilan okvir za izgradnju komunikacionih okruženja prilagođenih današnjim potrebama.



Da biste saznali više i otkrili sve funkcije koje nudi Matrix, možete pogledati zvaničnu dokumentaciju dostupnu ovde:


[https://matrix.org/docs/](https://matrix.org/docs/)