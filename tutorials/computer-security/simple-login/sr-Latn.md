---
name: Jednostavna prijava
description: Identitet zaštićen pseudonimima
---
![cover](assets/cover.webp)

## Prijava = email = gubitak privatnosti


U digitalnom svetu, postalo je standardna praksa imati nalog za svaku platformu kojoj se želi pristupiti.

Svaka od ovih usluga zahteva prijavu, obično povezanu sa parom _korisničko ime_ i _lozinka_. Često je korisničko ime lični email korisnika.


Kada se koristi lični email Address za svaku prijavu, lako je zamisliti prvu posledicu: gubitak poverljivosti, što postaje značajno ako je Address sastavljen od _ime.prezime@serviceemail.com_.


Programeri alata otvorenog koda kreirali su niz aplikacionih paketa, nastalih upravo kako bi korisnicima omogućili da povrate deo privatnosti: i dalje će se prijavljivati, ali koristeći pseudonim umesto alata koji otkriva njihov privatni identitet.


Najjednostavniji među onima koje sam lično probao i još uvek testiram je [Simple Login](https://simplelogin.io/).


## Pseudonim


Email alias jednostavno zamenjuje deo _name.surname_ vaše email adrese Address sa fiktivnim imenom. Za korisnika se ništa ne menja; alias servis prosleđuje emailove ka i od uobičajenog Address kao i obično. Svi mogu nastaviti da koriste svoj inbox kao i uvek, ali umesto prikazivanja pravog imena, prikazaće se neprepoznatljiv korisnik. Ova usluga treba da bude efikasna, a do sada se Simple Login pokazao upravo takvim.


Kada prvi put posetite Simple Login sajt, morate kreirati nalog (i ovde!), koristeći "zvanični" email Address. Ovde morate uneti email, lozinku i rešiti captcha-u.


![image](assets/it/02.webp)


Simple Login šalje verifikacionu poruku na navedeni email Address. Umesto klika na dugme za verifikaciju, preporučljivo je kopirati link i nalepiti ga u Address traku.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Nadzorna tabla Simple Login-a se odmah otvara, sa kratkim vodičem za navigaciju.


![image](assets/it/05.webp)


Treba napomenuti da Simple Login automatski aktivira pretplatu na bilten, koja se može deaktivirati iz odgovarajuće komande.


![image](assets/it/06.webp)


## Postavke


Možete odmah pogledati _Settings_ kako biste otkrili funkcije usluge. Simple Login počinje sa svim opcijama aktivnim, uključujući _Premium_ opcije, koje ostaju dostupne 10 dana. Nakon što probni period istekne, imaćete mogućnost da kreirate 10 aliasa sa ovim profilom i možete direktno povezati vaš Proton email, jer je Simple Login preuzet od strane švajcarskog provajdera email usluga.


![image](assets/it/07.webp)


Možete postaviti niz parametara ili proveriti da li je vaša e-pošta već ugrožena u smislu privatnosti.


![image](assets/it/08.webp)


Konačno, možete izvesti rezervnu kopiju svog profila ili uvesti jednu od drugog provajdera.


![image](assets/it/09.webp)


### Radni Email


Oni koji koriste email sa ličnim domenom kao poslovni email mogu postaviti svoj privatni domen.


![image](assets/it/10.webp)


Sa glavnog panela, odabirom _Mailboxes_, moguće je čak dodati i druge email adrese, kao i koristiti alias-e koji će biti kreirani u skladu s tim. U ovom uputstvu, na primer, odlučio sam da kreiram profil sa _gmail.com_ mailbox-om, a zatim da povežem _proton.me_ Address.


![image](assets/it/11.webp)


Dodavanje novog Address, posebno ako pripada Proton provajderu, vođena procedura pokazuje mogućnost ulaska u _sudo_ režim, super korisnik. Simple Login će tražiti da unesete lozinku ovog poštanskog sandučeta, kako bi se dokazala legitimnost Ownership.


⚠️ **Lično savetujem da ovo ne radite**. ⚠️


![image](assets/it/12.webp)


**Bolje je pristupiti email sandučetu -> kopirati link za verifikaciju i zalepiti ga u URL traku -> i dobiti verifikaciju bez otkrivanja lozinke.**


![image](assets/it/13.webp)


Od dve unete adrese, jedna postaje podrazumevana, a druga je sekundarna, ali se lako mogu zameniti, a podešavanje je lako prepoznatljivo na kontrolnoj tabli.


![image](assets/it/14.webp)


Nakon dodavanja druge e-pošte Address (opcionalno), da vidimo šta možemo uraditi sa Simple Login.


## Kreiranje aliasa


Na panelu, prva opcija menija je označena kao _Alias_, gde ih možete kreirati. Imate opciju da nasumično kreirate generate alijase klikom na dugme Random Alias, što je Green dugme prikazano na sledećoj fotografiji. Ova funkcija kreira jedinstveni i intrigantni email Address.


![image](assets/it/24.webp)


Ako, međutim, želite da diferencirate usluge davanjem različitih imena, morate izabrati _New Custom Alias_. Time možete dati aliasu ime usluge kojoj želite pristupiti (društvene mreže, provajderi usluga, online događaji, stranci koje ste slučajno sreli, itd.). Ostalo je u nadležnosti Simple Login-a.

Za zabavu (ali ne baš, da budem iskren) odlučio sam da kreiram alias za banku i nazvao ga `BANK`. Iako je istina da moja banka zna sve o meni, zabavlja me da komuniciram s njima koristeći email Address koji im je nerazumljiv. Simple Login zaista generiše nasumično ime, koje je od onog koje izaberemo odvojeno sa `.`


Ovde, nova e-pošta Address može postati:


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- i tako dalje


Može se izabrati više domena: javni su dostupni uz besplatan plan, dok drugi, označeni kao privatni (uključujući _@simplelogin.com_), proširuju izbor za korisnike koji odluče da se pretplate na plaćeni plan.


![image](assets/it/15.webp)


Kada su nasumični sufiks i domen odabrani, možete postaviti da li ovaj novi (i bizarni) Address treba da služi kao alias samo za jednu od ličnih email adresa, ili za sve njih. Alias postaje spreman i aktivan nakon klika na _Create_


![image](assets/it/16.webp)


Nova e-pošta Address je kreirana i sada je vidljiva, spremna za slanje (banci!) jednostavnim kopiranjem.


![image](assets/it/18.webp)


U ovom trenutku, možete se fokusirati na kreiranje aliasa za svaku uslugu ili platformu kojoj želite pristupiti i gde je email potreban kao suštinski parametar za kreiranje naloga.


![image](assets/it/19.webp)


Za entuzijaste privatnosti, postoji i opcija da se generate email Address zasnovan na UUID protokolu (ne na prepoznatljivim imenima), koji kreira jedinstveni 128-bitni identifikator koji nije pod kontrolom centralizovanih strana. Ova funkcija, koja je korisna za osetljive naloge, može se pronaći u meniju _Random Alias_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Kao što možete videti, ovo je email Address koji zahteva odgovarajuće upravljanje.


Ako promenite mišljenje i više ne želite da koristite alias, samo kliknite na komandu _More_ za svaki pojedinačni alias i izaberite _Delete_.


![image](assets/it/23.webp)


## Upravljanje Aliasima


Kreiranje aliasa je jednostavno, kao i njihovo upravljanje, što zahteva samo malo pažnje i discipline. Sav saobraćaj će, zapravo, i dalje prolaziti kroz email inbox koji smo na početku definisali kao zvanični. Obaveštenja i važne komunikacije sa platformi će nastaviti da stižu na Gmail, Proton, ili koji god email provajder da je u pitanju.


Rezultat je, međutim, da smo sačuvali glavni Address koji, od trenutka kreiranja pseudonima, možemo slobodno odlučiti kome ćemo ga otkriti, a kome ne.


Alias funkcioniše i za primanje i za slanje: drugi korisnik će zaista primiti odgovor sa alias.preoccupy789@8shield.net, ako je ovo pseudonim izabran za tog određenog primaoca.


## Pros


Sve u svemu, korišćenje pseudonima je efikasan način da zaštitite svoj identitet i privatnost. Adrese e-pošte često prikupljaju brokeri podataka i veb-sajtovi kako bi pratili navike i ponašanje korisnika. Iako vas pseudonim ne čini potpuno neprimetnim, dosledno korišćenje jednog je pozitivan korak ka zaštiti vaših informacija. Štaviše, u našem "globalnom digitalnom selu", gde su hakovanje, prodaja podataka i kršenja bezbednosti previše česti, vrlo je verovatno da je e-pošta koju koristite za registraciju na raznim veb-sajtovima već kompromitovana ili na meti.


Jedinstveni pseudonim, korišćen za svaku prijavu, **odmah nam omogućava da shvatimo koja platforma šalje spam (ili još gore) u naš poštanski sandučić, jer je email identifikovan aliasom povezanim s njim**. Nemate pojma koliko spama i fišinga dolazi iz takozvanih pouzdanih kanala, jer su institucionalni, dok ne počnete koristiti alias za banke, jedan za poštanske usluge, ili specifičan za neke obavezne vladine usluge. Kada se identifikuje pošiljalac spama (ili još gore), znaćete da je taj sajt kompromitovan, preduzimajući sve mere predostrožnosti da zaštitite sve podatke koji su dati (razmislite o kreditnim karticama!) tom specifičnom sajtu, koji može shvatiti proboj nedeljama kasnije.


Što se tiče Simple Login-a, ovaj alat ima sledeće funkcije:



- mobilna aplikacija (takođe sa F-Droid) i ekstenzija za pregledač, za upravljanje aliasima u bilo kojoj situaciji;
- dvofaktorska autentifikacija za svaki novi pseudonim, što povećava stepen nezavisnosti od same usluge;
- PGP podrška (za _Premium korisnike);
- jednostavno kreiranje svake vrste aliasa (prilagođeni, nasumični i UUID);
- među besplatnim planovima u sektoru, mogućnost korišćenja aliasa sa više "zvaničnih" email sandučića. Drugi konkurenti ograničavaju na samo jedan.


## Nedostaci


- 10 aliasâ možda neće biti dovoljno ako planirate da intenzivno koristite Simple Login. U ovom slučaju, plaćeni plan, koji je prilično pristupačan, je koristan za povećanje broja dostupnih aliasâ.
- Nije moguće kreirati alias sa specifičnim imenom i domenom. Nasumični sufiks, dodat nakon imena koje izaberemo, generiše Address koji se u najboljem slučaju može opisati kao bizaran. Tradicionalni društveni mediji obično odbijaju da odobre naloge kreirane sa ovakvim tipom email adresa. Nostr to rešava!
- Ako koristite alias za slanje poruke nekome, lako možete završiti u folderu za neželjenu poštu primaoca. Kao prvi korak, preporučljivo je koristiti pseudonim za primanje, baš kao u slučaju kreiranja naloga, pretplate na mailing listu, itd.