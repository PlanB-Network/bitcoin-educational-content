---
name: BitBanana
description: Mobilni menadžer za vaš Lightning čvor
---

![cover](assets/cover.webp)



U ovom vodiču naučićete kako da instalirate i konfigurišete BitBanana na Androidu kako biste kontrolisali svoj Lightning čvor sa pametnog telefona. Videćemo kako da povežete aplikaciju sa vašom postojećom infrastrukturom (Umbrel, RaspiBlitz, myNode, ili bilo kojim LND/Core Lightning čvorom), kako da izvršavate Lightning plaćanja, upravljate kanalima na daljinu, pregledate prihode od rutiranja i napravite rezervne kopije vaših konfiguracija. Takođe ćete naučiti o najboljim bezbednosnim praksama za zaštitu pristupa vašem čvoru i kako se BitBanana poredi sa Zeusom, popularnom alternativom.



## Predstavljamo BitBanana



BitBanana je aplikacija otvorenog koda za Android mobilne uređaje koja pretvara vaš pametni telefon u potpunu komandnu tablu za daljinsko upravljanje vašim Lightning čvorom. Za razliku od Lightning novčanika, koji integrišu lokalni čvor na telefonu, BitBanana usvaja filozofiju 100% daljinskog upravljanja: aplikacija ne drži satoshi i povezuje se samo sa vašom postojećom infrastrukturom.



Razvijena od strane Michaela Wünscha pod MIT licencom, aplikacija garantuje potpunu transparentnost bez prikupljanja ličnih podataka i verifikovane reproduktivne izgradnje. BitBanana nativno podržava LND i Core Lightning putem standardnih URI-ova (`lndconnect://` i `clngrpc://`), drastično pojednostavljujući početnu konfiguraciju. Aplikacija takođe prepoznaje LndHub i Nostr Wallet Connect za korisnike bez ličnog čvora, iako ovi režimi rade kustodijalno sa ograničenom funkcionalnošću.



Interfejs nudi potpuni pristup svim kritičnim funkcijama vašeg čvora: slanje i primanje uplata (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), upravljanje Lightning kanalima (otvaranje, zatvaranje, podešavanje naknada, balansiranje), napredna kontrola novčića i upravljanje osmatračnicom. BitBanana takođe implementira nekoliko robusnih sigurnosnih slojeva: biometrijsko zaključavanje, stealth mod, hitni PIN i podršku za Tor kako bi se anonimne veze.



## Podržane platforme i instalacija



### Instalacija



BitBanana je isključivo dostupan za Android 8.0 ili noviji. Aplikacija ne postoji na iOS-u i nije planirana nijedna verzija. Ovo ograničenje je objašnjeno istorijom projekta: BitBanana je direktni naslednik Zap Android-a, koji je prvobitno razvio Michael Wünsch, koji je odlučio da nastavi svoj rad pod sopstvenim brendom. Zap je bio porodica zasebnih aplikacija (Zap Android, Zap iOS, Zap Desktop) koje su razvijali različiti saradnici sa zasebnim bazama koda. BitBanana prati samo Android granu.



Pored toga, iOS ekosistem predstavlja značajna regulatorna i tehnička ograničenja za nekustodijalne Lightning aplikacije. U 2023. godini, Apple je odbio Zeus ažuriranje zbog "kršenja licenci", a u 2024. godini, Phoenix Wallet je napustio američki App Store suočen sa regulatornim neizvesnostima u vezi sa Lightning provajderima usluga. Ove prepreke objašnjavaju zašto mnogi Lightning developeri preferiraju Android, koji nudi otvoreniju politiku za nekustodijalne aplikacije.



Tri metode instalacije su dostupne za Android: Google Play Store (5000+ instalacija, automatska ažuriranja), F-Droid (reproducibilne verzije, verifikacija izvornog koda), ili ručni APK sa GitHub-a.



![BitBanana](assets/fr/01.webp)



Zvanična veb stranica bitbanana.app (levo) se hvali sa "100% Samokustodijalno sa NULTIM prikupljanjem podataka". Centralni ekran prikazuje tri opcije preuzimanja: F-Droid (preporučeno), Google Play i APK. Ekran desno prikazuje dozvole za obaveštenja za upozorenja o plaćanju.



Aplikacija zahteva dozvole: mreža (povezivanje čvorova), kamera (QR kodovi), NFC (LNURL), pozadinske usluge (obaveštenja), biometrija (bezbednost) i WireGuard VPN. Nema praćenja, nulta kolekcija podataka. Omogućite zaključavanje lozinkom ili biometrijom za sigurniji pristup.



## Početna konfiguracija



### Povezivanje na LND čvor



Da povežete BitBanana sa vašim LND čvorom (Umbrel, RaspiBlitz, myNode), nabavite `lndconnect` URI ili QR kod koji sadrži adresu, TLS sertifikat i autentifikacioni makarun.



Za ovaj vodič koristimo LND čvor putem umbrel-a. Za više detalja, pogledajte naš posvećeni vodič :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Na aplikaciji Lightning Node, pristupite meniju u gornjem desnom uglu i odaberite "Connect wallet".



![BitBanana](assets/fr/04.webp)



Odaberite **gRPC (Tor)** za povezivanje putem Tor-a (preporučeno). Prikazuju se QR kod i detalji (Host .onion, Port 10009, Macaroon).



![BitBanana](assets/fr/02.webp)



U BitBanana, pritisnite "CONNECT NODE", skenirajte QR kod ili nalepite URI. Dozvolite pristup kameri, zatim proverite prikazanu .onion adresu pre potvrđivanja.



**Core Lightning** veza



Ako koristite Core Lightning (CLN) umesto LND, proces ostaje identičan, sa URI `clngrpc://` koji sadrži međusobne TLS sertifikate. Core Lightning nativno podržava BOLT12 (ponude), omogućavajući ponovnu upotrebu faktura i ponavljajuća plaćanja koja nisu dostupna na LND.



**Povezivanje bez ličnog čvora (LNbits/hostovano)**



Ako nemate Lightning čvor, BitBanana se može povezati sa hostovanim uslugama putem LndHub-a (protokol koji koriste BlueWallet i LNbits) ili Nostr Wallet Connect (NWC). Molimo obratite pažnju: ovi režimi rade u kustodijalnom režimu (usluga hostuje vaša sredstva) sa ograničenom funkcionalnošću. Nećete moći da upravljate kanalima ili konfigurišete naknade za rutiranje, i moći ćete samo da šaljete i primate Lightning uplate.



Za više detalja o LNbits ili Nostr Wallet Connect, molimo vas da pogledate naše razne tutorijale:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Svakodnevna upotreba



### Interface glavni



Početni ekran prikazuje vaš Lightning saldo, sa menijem u gornjem levom uglu koji omogućava pristup sledećim sekcijama: Kanali, Rutiranje, Potpisivanje/Verifikacija, Čvorovi, Kontakti, Podešavanja, Bekap. Ikonica sata (gore desno) otvara istoriju transakcija. Dugmad "Pošalji" i "Primi" na dnu omogućavaju vam da šaljete i primate vaše satoshije.



![BitBanana](assets/fr/05.webp)



### Lightning i on-chain plaćanja



![BitBanana](assets/fr/10.webp)



**Pošalji uplatu:** Pritisnite dugme "Pošalji" sa početnog ekrana. Ekran za uplatu (levo) nudi vam da nalepite adresu ili podatke o uplati u polje "Address ili podaci o uplati", sa QR skenerom u gornjem desnom uglu za skeniranje kodova. Takođe možete odabrati kontakt sačuvan u odeljku Kontakti kako biste izbegli skeniranje svaki put.



BitBanana inteligentno prepoznaje sve formate plaćanja: klasične Lightning fakture (nizovi karaktera koji počinju sa `lnbc`), Lightning Address (format e-pošte kao što je `utilisateur@domaine.com`), LNURL-pay kodove za dinamična plaćanja, LNURL-withdraw za povlačenje sredstava, pa čak i Keysend plaćanja direktno na Lightning javni ključ bez prethodne fakture. Aplikacija automatski obavlja potrebna LNURL razrešenja u pozadini.



Jednom kada je faktura učitana, BitBanana prikazuje potpune detalje: tačan iznos, procenjene naknade za rutiranje, opis plaćanja (ako ga je obezbedio primalac) i datum isteka fakture. Nakon potvrde, plaćanje se usmerava putem vaših Lightning kanala. Zatim možete videti putanju koja je pređena korak po korak i naknade koje su stvarno plaćene u detaljima transakcije.



**Primite uplatu:** Pritisnite dugme "Primite". Selektor (desni ekran) vam omogućava da birate između Lightning (trenutna uplata putem vaših kanala) i On-Chain. Za Lightning račun, unesite željeni iznos u satoshijima (ili ostavite na 0 da kreirate fakturu bez fiksnog iznosa koji platiša treba da popuni), i dodajte opcionalni opis koji će se pojaviti na fakturi. BitBanana trenutno generiše Lightning fakturu sa QR kodom za skeniranje. Takođe možete kopirati fakturu kao tekst i poslati je putem e-maila. Čim uplata bude primljena, push obaveštenje vas obaveštava i transakcija se odmah pojavljuje u istoriji sa svim svojim detaljima.



### Kanali i usmeravanje



![BitBanana](assets/fr/06.webp)



Deo "Channels" prikazuje vaše mogućnosti slanja/primanja i navodi vaše kanale sa jedinstvenim avatarima. Svaki kanal prikazuje svoju likvidnost podeljenu između lokalnog i udaljenog balansa. Dodirnite kanal za potpune detalje i radnje (zatvaranje, promena naknada za rutiranje). Tri tačke u gornjem desnom uglu daju pristup opciji "Rebalance" za ponovno balansiranje likvidnosti vaših kanala. Dugme "+" otvara novi kanal.



Odeljak za usmeravanje (centralni ekran) prikazuje prihode od prosleđivanja po periodima (1D, 1W, 1M, 3M, 6M, 1Y) sa detaljnom istorijom prosleđivanja kako biste optimizovali svoju strategiju.



Potpiši/Verifikuj (desni ekran) omogućava vam da kriptografski potpišete/verifikujete poruke kako biste dokazali kontrolu nad čvorom.



### Više čvorova i parametara



![BitBanana](assets/fr/07.webp)



**Upravljanje Čvorovima**: prikazuje vaše čvorove, sa dugmadima za ručno dodavanje, skeniranje QR koda ili prebacivanje između čvorova. Konkretno, možete postaviti različite tipove veze na isti čvor: LAN, VPN ili Tor.



**Upravljanje kontaktima**: čuva vaše Lightning kontakte za brza plaćanja.



**Postavke**: prilagodite valutu, jezik, avatare. Odeljak Bezbednost i Privatnost: Zaključavanje aplikacije (PIN/biometrija), Sakrij saldo (tajni režim), Tor (anonimizacija IP-a). Konfiguracija cenovnih proročišta, istraživača blokova, prilagođenih procenitelja naknada.



## Prednosti i ograničenja



**Istaknuto:**




- Totalna mobilnost: kontroliši svoj Lightning čvor sa bilo kog mesta
- Puna funkcionalnost: plaćanja (LNURL, Lightning Address, BOLT 12), upravljanje kanalima, kontrola novčića, osmatračnice, multi-čvorovi
- Sigurnost: PIN/biometrija, skriveni režim, hitni PIN, izvorni Tor, blokiranje snimaka ekrana
- Besplatno, otvorenog koda (MIT), bez provizija, bez prikupljanja podataka



**Ograničenja:**




- Zahteva aktivan Lightning čvor (ili LNbits u skrbničkom režimu)
- Nema planirane verzije za iOS
- Osiguravanje pristupa telefonu je ključno (macaroon admin = totalni pristup čvoru)



## Najbolje prakse



**Bezbednost:**




- Aktiviraj PIN/biometrijsku zaštitu (sprečava neovlašćen pristup čvoru)
- Postavite PIN za hitne slučajeve (briše osetljive podatke u slučaju prinude)
- Nikada ne delite svoj URI za prijavu ili macaroon
- Stealth mod u neprijateljskim okruženjima



**Prijava:**




- VPN mesh (Tailscale, ZeroTier): najbolji kompromis između brzine i sigurnosti
- Tor: maksimalna poverljivost, veća latencija
- Clearnet: izbegavati osim ako nije neophodno (izloženost IP-a, otvoreni portovi)



### Bekap i obnova



Konačno, tu je meni "Backup", koji vam omogućava da sačuvate vaše konfiguracije za migraciju telefona ili ponovnu instalaciju.



![BitBanana](assets/fr/08.webp)



**Važno:** Rezerva NE sadrži seed ili rezervne kopije kanala (to treba uraditi na čvoru). Sadrži: konfiguracije čvora (adrese, sertifikate, makarone), oznake, kontakte, parametre. Dugme za vraćanje omogućava uvoz postojeće rezerve. Potvrda je potrebna pre čuvanja.



![BitBanana](assets/fr/09.webp)



Unesite lozinku za šifrovanje (desni ekran). Sistem otvara birač datoteka (levi ekran) za čuvanje `BitBananaBackup_2025-XX-XX.dat`. Potvrda "Backup kreiran".



**Bezbednost:** Čuvajte rezervnu kopiju šifrovanu (lični cloud, USB, NAS). Nikada ne delite fajlove ili lozinke. Redovno testirajte obnavljanje. Rezervna kopija obnavlja veze, ne sredstva.



## BitBanana vs Zeus: Koja je razlika?



Ako istražujete mobilne aplikacije za upravljanje Lightning čvorom, verovatno ćete naići na Zeus, popularnu alternativu za BitBanana. Za razliku od BitBanana, koji se fokusira isključivo na daljinsku kontrolu postojećeg čvora, Zeus ima sveobuhvatniji pristup, nudeći dva režima rada: Lightning čvor ugrađen direktno u aplikaciju (ugrađeni režim sa integrisanim LND) i daljinsko povezivanje sa spoljnim čvorom, baš kao BitBanana.



Ova dvostruka funkcionalnost čini Zeus posebno privlačnim za početnike koji žele eksperimentisati sa Lightning-om bez ikakve prethodne infrastrukture. Ugrađeni režim omogućava trenutni start sa kompletnim mobilnim čvorom, dok napredni korisnici mogu preći na daljinsko povezivanje kada njihov lični čvor bude konfigurisan. Zeus takođe podržava LND i Core Lightning za daljinsko povezivanje, kao što je BitBanana.



Još jedna velika prednost Zeusa je njegova dostupnost na više platformi (iOS i Android), dok BitBanana ostaje isključivo na Androidu. Zeus takođe uključuje Olympus LSP infrastrukturu kako bi olakšao primanje Lightning uplata putem kanala na vreme, sistem prodajnog mesta za trgovce i integrisanu funkcionalnost zamene za upravljanje likvidnošću.



Međutim, BitBanana zadržava svoje specifične prednosti: jednostavniji, pregledniji interfejs, bolje korisničko iskustvo (UX) zahvaljujući isključivom fokusu na daljinsku kontrolu i edukativni pristup sa kontekstualnim objašnjenjima. Zeus nudi više funkcionalnosti, ali na račun složenijeg interfejsa. Aplikacija je posebno pogodna za korisnike koji žele da kontrolišu čvor isključivo na daljinu, bez kustodijalnih funkcija.



Da biste saznali više o Zeusu, pogledajte sledeće tutorijale:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Zaključak



BitBanana pretvara vaš Android pametni telefon u potpunu Lightning kontrolnu tablu, nudeći neviđenu mobilnost za operatere čvorova. Aplikacija pokriva sve funkcionalnosti: plaćanja (svi formati), upravljanje kanalima, kontrolu novčića, osmatračnice, multi-čvor, sa poboljšanom sigurnošću (PIN/biometrija, Tor, hitni PIN).



Potpuno suveren, BitBanana ne prikuplja podatke i ne ugrožava ni poverljivost ni kontrolu vaših sredstava. Otvoreni izvorni kod (MIT) garantuje transparentnost.



## Resursi



### Zvanična dokumentacija




- [BitBanana website](https://bitbanana.app)
- [Complete documentation](https://docs.bitbanana.app)
- [GitHub izvorni kod](https://github.com/michaelWuensch/BitBanana)



### Instalacija




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)