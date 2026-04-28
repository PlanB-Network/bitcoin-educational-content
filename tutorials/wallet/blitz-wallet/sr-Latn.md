---
name: Blitz Wallet
description: Najjednostavniji Bitcoin novčanik.
---

![cover](assets/cover.webp)

Korisničko iskustvo je jedan od presudnih faktora pri izboru Bitcoin novčanika. U ovom tutorijalu, predstavljamo vam Blitz Wallet, novčanik koji stavlja jednostavnost u centar svog pristupa: zahvaljujući integraciji **Spark** protokola, Blitz vam nudi jedan od najjednostavnijih i najkompletnijih Bitcoin novčanika na tržištu, sa trenutnim plaćanjima i bez tehničkog upravljanja.

## Šta je Blitz Wallet?

Blitz Wallet je **self-custodial** i **open source** Bitcoin novčanik, koji se oslanja na vašu suverenost i glatko i intuitivno korisničko iskustvo.

[Blitz Wallet](https://blitz-wallet.com/) je mobilna aplikacija dostupna na Android-u (Play Store) i iOS-u (App Store).

Za razliku od tradicionalnih Lightning novčanika koji zahtevaju upravljanje platnim kanalima i dolaznom likvidnošću, Blitz Wallet se oslanja na **Spark protokol** kako bi eliminisao ove tehničke složenosti. Rezultat: trenutna plaćanja od prvog primljenog satošija, bez ikakve prethodne konfiguracije. Cilj Blitz-a je da plaćanja u bitkoinu učini jednostavnim kao klasična aplikacija za plaćanje, bez ikada ugrožavanja self-custody vaših sredstava.

Blitz Wallet takođe podržava **čitljive adrese** u formatu `korisnik@domen.com` (putem LNURL), što omogućava slanje bitkoinа jednako lako kao e-mail, bez manipulisanja dugačkim invoice-ima ili QR codes-ovima pri svakoj transakciji.

## Razumevanje Spark protokola

Pre nego što pređemo na praksu, korisno je razumeti tehnologiju koja pokreće Blitz Wallet ispod haube: **Spark protokol**.

### Šta je Spark?

Spark je open source protokol nadsloja izgrađen na Bitcoin-u, razvijen od strane tima Lightspark. Omogućava izvršavanje trenutnih transakcija sa niskim troškovima, uz očuvanje self-custody vaših bitkoinа.

Za razliku od Lightning Network koji se oslanja na **platne kanale** između dve strane, Spark koristi tehnologiju zvanu **statechain** (lanac stanja). Osnovni princip je sledeći: umesto pomeranja bitkoinа na blockchain-u pri svakoj transakciji, Spark prenosi **pravo potrošnje** sa jednog korisnika na drugog, bez on-chain pomeranja.

### Kako funkcioniše?

Da biste razumeli Spark na intuitivan način, zamislite da trošenje bitkoina na Spark-u zahteva kompletiranje slagalice od dva dela:
- Jedan deo drži korisnik (na primer, Alice).
- Drugi deo drži grupa operatera zvana **Spark Entity (SE)**.

Samo kombinacija dva odgovarajuća dela omogućava trošenje bitkoinа.

Kada Alice želi da pošalje svoje bitkoine Bob-u, evo šta se dešava: nova slagalica se zajednički kreira između Bob-a i SE. Slagalica zadržava isti oblik, ali delovi koji je čine se menjaju. Od sada, Bob-ov deo odgovara delu SE. Stari deo Alice postaje neupotrebljiv, jer je SE uništio svoj odgovarajući deo. Vlasništvo nad bitkoinima je promenilo ruke, **bez ikakve transakcije na blockchain-u**.

Bob zatim može ponoviti isti proces da pošalje te bitkoine Carol, i tako dalje. Svaki transfer funkcioniše zamenom delova slagalice, a ne pomeranjem sredstava on-chain.

### Zašto je bezbedno?

Legitimno pitanje se postavlja: šta se dešava ako SE zapravo ne uništi svoj stari deo?

Spark Entity nije jedan entitet: to je grupa nezavisnih operatera. Deo SE nikada ne drži jedan operater. Zamena slagalice zahteva saradnju više operatera. Dovoljno je da **jedan jedini operater bude pošten** tokom transfera da bi sprečio reaktivaciju stare slagalice. Nijedan izolovani operater ne može tajno sačuvati staru aktivnu slagalicu ili je ponovo kreirati kasnije.

Pored toga, Spark integriše mehanizam jednostranog izlaza: uvek možete povratiti svoje bitkoine on-chain bez saradnje SE. Ovaj rezervni mehanizam je sastavni deo Spark arhitekture i garantuje da nikada niste zavisni od mreže za pristup vašim sredstvima.

### Spark naspram Lightning Network

Spark i Lightning nisu u konkurenciji: oni su **komplementarni**. Blitz Wallet integriše oba, što vam omogućava da uživate u prednostima svakog.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Tehnologija**               | Statechains (lanci stanja)   | Platni kanali         |
| **Upravljanje kanalima**      | Nije potrebno                | Potrebno              |
| **Dolazna likvidnost**        | Nije potrebna                | Potrebna              |
| **Trenutne transakcije**      | Da                           | Da                    |
| **Self-custody**              | Da                           | Da                    |
| **Lightning kompatibilnost**  | Da (putem atomic swaps)      | Nativno               |

Lightning Network ostaje odličan protokol za trenutna plaćanja, ali nameće tehnička ograničenja (upravljanje kanalima, dolazna likvidnost, čvor na mreži...) koja mogu obeshrabriti početnike. Spark uklanja ta ograničenja dok ostaje kompatibilan sa Lightning-om.

## Instalacija i konfiguracija

U ovom tutorijalu, baziramo se na Android verziji Blitz Wallet-a, ali svi procesi predstavljeni u nastavku važe i za iOS.

![installation](assets/fr/01.webp)

Pošto je Blitz Wallet self-custody novčanik, imate izbor između **kreiranja novog novčanika** ili **uvoza fraze za oporavak** (12 ili 24 reči) iz postojećeg novčanika.

Ovde krećemo sa kreiranjem novog novčanika. U nastavku pogledajte naše preporuke o čuvanju vaše fraze za oporavak:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **VAŽNO**: Ovih 12 ili 24 reči za oporavak su **jedini ključ za pristup vašim bitkoinima**. Blitz je self-custodial novčanik: ni Blitz ni Spark nemaju pristup vašoj frazi za oporavak niti vašim sredstvima. Ako izgubite ove reči, trajno ćete izgubiti pristup vašim bitkoinima. Ne delite ih ni sa kim: ko god ih poseduje može potrošiti vaše bitkoine.

Zatim kreirajte **PIN** za obezbeđivanje pristupa vašem novčaniku.

![setup-wallet](assets/fr/02.webp)

## Početak rada sa Blitz-om

Izvršavanje transakcija sa Blitz-om je intuitivnije nego kod većine drugih Bitcoin novčanika. Interfejs je minimalistički i fokusiran na tri glavne akcije: slanje, skeniranje i primanje.

### Primanje bitkoinа

Da biste primili bitkoine na vaš Blitz novčanik, kliknite na ikonu **"Strelica nadole"** (↓), unesite iznos u satošijima koji želite da primite, dodajte opcionalni opis, a zatim će novčanik generisati invoice koji možete podeliti sa pošiljaocem.

⚠️ **NAPOMENA**: Satoši (ili "sat") je najmanja jedinica bitkoina: **1 bitkoin = 100 000 000 satošija**.

Jedna od posebnosti Blitz Wallet-a je što podržava više mreža i protokola Bitcoin ekosistema:

- **Lightning Network**: Jedan od nadslojeva Bitcoin-a koji omogućava trenutna mikroplaćanja sa veoma niskim naknadama. Idealan za male svakodnevne iznose.

- **Bitcoin (on-chain)**: Glavni blockchain Bitcoin protokola, pogodan za transakcije većih iznosa gde su maksimalna bezbednost i konačnost prioritet.

- **Liquid Network**: Sidechain (paralelni lanac) Bitcoin-a razvijen od strane Blockstream-a, koji omogućava brze i poverljive transakcije koristeći Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Podrazumevano, Blitz generiše Lightning invoice, ali možete izabrati mrežu na kojoj želite da primite vaše satošije klikom na dugme **"Choose format"**.

![receive-sats](assets/fr/03.webp)

### Kreiranje kontakata

Blitz Wallet pojednostavljuje ponavljajuće slanje bitkoinа zahvaljujući svom sistemu kontakata.

U meniju **Contacts**, možete registrovati Blitz korisnička imena ili Lightning adrese (LNURL) sa kojima često komunicirate.

Na taj način možete slati satošije na te adrese u par klikova, bez skeniranja QR code-a ili ručnog unošenja adrese svaki put.

### Slanje bitkoinа

Pored klasičnih metoda slanja bitkoina (skeniranje QR code-a, ručni unos adrese), Blitz nudi nekoliko praktičnih opcija:

- **Sa slike** (*From Image*): Uvezite QR code iz vaše foto galerije.
- **Iz međuspremnika** (*From Clipboard*): Nalepite prethodno kopiranu adresu ili invoice.
- **Ručni unos** (*Manual Input*): Direktno unesite Bitcoin adresu, Lightning invoice ili čitljivu adresu (na primer `korisnik@walletofsatoshi.com`).
- **Iz vaših kontakata**: Izaberite prethodno registrovanog primaoca za slanje u par klikova.

U meniju **Wallet**, kliknite na dugme **"Strelica nagore"** (↑), izaberite vaš metod slanja, unesite iznos za slanje, dodajte opis i potvrdite transakciju.

Minimalni iznos za slanje trenutno je **1 000 satošija**.

![send-bitcoin](assets/fr/05.webp)

## Blitz prodavnica

Pored operacija prenosa bitkoinа, Blitz Wallet integriše prodavnicu u kojoj možete potrošiti vaše bitkoine za kupovinu digitalnih usluga direktno iz aplikacije.

Iz glavnog menija, kliknite na karticu **Store** za pristup prodavnici. Tamo ćete takođe pronaći pristup platformi **Bitrefill** koja omogućava kupovinu poklon kartica od hiljada trgovaca širom sveta, direktno u bitkoinu.

- **Veštačka inteligencija**: Pristupite najnovijim generativnim AI modelima (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) i platite vaše kredite direktno u satošijima. Više paketa je dostupno prema vašim potrebama (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonimni SMS**: Šaljite i primajte SMS poruke svuda u svetu bez otkrivanja vašeg ličnog broja telefona. Usluga se naplaćuje u satošijima za svaku poslatu poruku.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Zaštitite vašu privatnost na mreži pretplatom na VPN WireGuard (nedeljno, mesečno ili kvartalno), sa plaćanjem u bitkoinu direktno iz Blitz prodavnice. Potrebno je samo da preuzmete WireGuard klijent aplikaciju na vaš uređaj da biste je koristili.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet iza kulisa: idemo dalje

Iza jednostavnosti korišćenja Blitz Wallet-a krije se dobro osmišljena tehnička arhitektura koja kombinuje više slojeva Bitcoin ekosistema.

### Raspodela vašeg salda

Blitz Wallet upravlja vašim saldom transparentno, raspodeljujući vaša sredstva između različitih protokola prema potrebama. Kada je vaš saldo ispod 500 000 satošija, Blitz koristi **Liquid Network** i atomic swaps da vam pruži glatko iskustvo i omogući transakcije na Lightning Network čak i sa malim iznosima.

Ovaj pristup garantuje jednostavno usvajanje za nove korisnike, bez potrebe da razumeju osnovne mehanizme. Možete pogledati raspodelu vašeg salda između različitih slojeva u meniju **Podešavanja > Balance Info**.

![balance](assets/fr/09.webp)

### Lightning režim (opciono)

Podrazumevano, Blitz Wallet koristi Liquid Network i Spark protokol da vam pruži glatko iskustvo bez tehničke konfiguracije. Međutim, Blitz vam daje mogućnost da aktivirate **Lightning režim** koji će automatski otvoriti platni kanal kada dostignete saldo od **500 000 satošija** (0,005 BTC).

Da aktivirate Lightning režim, idite u **Podešavanja**, zatim u odeljku **Tehnička podešavanja**, kliknite na opciju **Node Info**.

![enable-lightning](assets/fr/10.webp)

Zahvaljujući Spark protokolu, ova aktivacija je **opciona**: Spark već omogućava Lightning kompatibilna plaćanja bez potrebe za otvaranjem kanala ili upravljanjem dolaznom likvidnošću. Nativni Lightning režim ostaje koristan za napredne korisnike koji žele da imaju sopstveni Lightning čvor integrisan u aplikaciji.

### Prodajno mesto (PoS)

Blitz Wallet integriše funkcionalnost **prodajnog mesta** koja omogućava trgovcima da prihvataju plaćanja u bitkoinu direktno iz aplikacije.

U meniju **Podešavanja > Point-of-sale**, možete konfigurisati:

- Jedinstveni identifikator vaše prodavnice
- Lokalnu fiat valutu za prikaz cena
- Instrukcije za vaše zaposlene
- Opciju napojnice za vaše kupce

Vaši kupci samo treba da skeniraju generisani QR code da izvrše svoje plaćanje u bitkoinu, trenutno.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Resursi korišćeni za pisanje ovog tutorijala:
- Blog [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
