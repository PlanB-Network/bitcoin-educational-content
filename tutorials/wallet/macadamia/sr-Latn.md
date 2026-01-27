---
name: Macadamia Wallet
description: Cashu mobilni wallet za anonimna i trenutna BTC plaćanja
---

![cover](assets/cover.webp)



Macadamia Wallet je iOS mobilni wallet koji implementira Cashu protokol, Chaumian ecash sistem koji omogućava potpuno anonimna Bitcoin plaćanja. Zahvaljujući slepim potpisima, nijedan posmatrač ne može povezati vaše depozite sa vašim troškovima, nudeći poverljivost sličnu fizičkom novcu.



U ovom vodiču ćemo pogledati kako instalirati i konfigurisati Macadamia, izvršiti vaše prve Cashu transakcije (Mint, Send, Receive, Melt) i upravljati višestrukim mintovima kako biste osigurali vaša sredstva.



## Šta je Macadamia Wallet?



### Cashu protokol



Cashu koristi slepe potpise koje je izumeo David Chaum: deponujete bitkoine kod servera "kovnice", koji izdaje ekvivalentne tokene u satoshijima. Kovnica potpisuje ove tokene bez uvida u njihov sadržaj, što onemogućava povezivanje token sa korisnikom. Razmene su off-chain, peer-to-peer, i potpuno neprozirne - čak ni kovnica ne može pratiti ko kome plaća.



Macadamia je open source wallet iOS razvijen u Swift/SwiftUI. Radi bez naloga ili KYC, vaši tokeni su pohranjeni lokalno i zaštićeni seed frazom. Kod je moguće pregledati na GitHub-u, a tokeni su interoperabilni sa drugim Cashu novčanicima (Minibits, Cashu.me).



### Model starateljstva i kompromis



**Važno**: Cashu funkcioniše na kustodijalnom modelu. Tokeni su obećanja za plaćanje (IOU) podržana rezervama kovnice Bitcoin. Ako kovnica nestane, vaši tokeni gube svoju vrednost. Ovo je kompromis za maksimalnu poverljivost.



Koristite Macadamia kao fizički wallet: samo male količine. Rasporedite svoja sredstva preko nekoliko kovnica da biste razredili rizik.



## Glavne karakteristike



Macadamia implementira četiri osnovne operacije Cashu protokola. **Mint** konvertuje vaše satoshije u tokene putem Lightning fakture. **Send** vam omogućava da šaljete tokene besplatno putem QR koda ili linka, potpuno off-chain. **Receive** vam omogućava da primate tokene ili generate Lightning fakturu. **Melt** plaća Lightning fakturu uništavanjem vaših tokena.



wallet podržava upravljanje više kovnica istovremeno. Možete zameniti tokene između različitih kovnica putem Lightning-a.



## Podržane platforme



Macadamia je dostupna samo na iOS 17 ili novijem za iPhone i iPad. Izvorna Swift/SwiftUI aplikacija nudi optimalnu integraciju sa Apple ekosistemom.



Cashu protokol garantuje interoperabilnost između novčanika. Možete obnoviti svoju seed frazu u drugim aplikacijama kao što su Minibits na Androidu ili Nutstash na desktopu.



Trenutna verzija se distribuira putem TestFlight-a. Koristite samo male količine sa ovom beta verzijom.



## Instalacija



Macadamia je trenutno dostupan putem TestFlight-a, Apple-ovog programa za beta testiranje. Evo kako da ga instalirate:



### Instalacija putem TestFlight-a



**Korak 1: Preuzmite TestFlight**



Ako već nemate aplikaciju TestFlight na svom uređaju, potražite "TestFlight" u App Store-u i instalirajte je. TestFlight je zvanična Apple-ova aplikacija za testiranje beta verzija iOS aplikacija.



**Korak 2: Pridružite se Macadamia beta programu** (na francuskom)



Kada je TestFlight instaliran, pratite ovu pozivnicu sa vašeg iPhone-a ili iPad-a: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Veza će automatski otvoriti TestFlight i ponuditi vam da instalirate Macadamia Wallet. Dodirnite "Prihvati" zatim "Instaliraj" da biste započeli preuzimanje. Aplikacija teži oko deset megabajta i potrebno je samo nekoliko sekundi za instalaciju.



![Installation TestFlight](assets/fr/01.webp)



### Važne informacije o beta verzijama



Macadamia je još uvek u fazi aktivnog razvoja. TestFlight verzije se često ažuriraju i mogu uvesti nove funkcije ili ispraviti greške. Međutim, kao i kod svake beta verzije, mogu se pojaviti kvarovi. **Snažno preporučujemo da koristite samo male iznose**, koje prihvatate da mogu biti izgubljeni u slučaju tehničkog problema.



Macadamia ne prikuplja nikakve korisničke podatke prema prikazanoj politici privatnosti. Obavezno proverite da je developer cypherbase UG prilikom instalacije.



## Početna konfiguracija



Prilikom prvog pokretanja, Macadamia generiše BIP-39 rečenicu od 12 reči. Zapišite ih na sigurno mesto - nikada kao snimak ekrana. Ove reči vam omogućavaju da ponovo kreirate vaš wallet i trošite vaše tokene.



![Configuration initiale](assets/fr/02.webp)



Pratite četiri koraka: dobrodošlica, prihvatanje uslova, sačuvajte seed rečenicu i konačna potvrda.



![Interface principale](assets/fr/03.webp)



Once configuration is complete, Macadamia presents three main tabs. **Wallet** displays your balance and transaction history. **Mints** lets you manage your Cashu servers. **Settings** gives access to settings and your seed phrase.



![Ajout d'un mint](assets/fr/04.webp)



Sada treba da konfigurišete mint, tj. Cashu server koji će izdavati vaše tokene. Idite na karticu "Mints", dodirnite "Add new Mint URL", i unesite adresu izabranog minta (npr. mint.cubabitcoin.org). Pogledajte bitcoinmints.com ili cashu.space za ugledne javne mintove. Validirajte samo mintove čiju ste reputaciju proverili, jer će oni imati starateljstvo nad vašim satoshijima.



## Svakodnevna upotreba



### Kreiranje novih tokena (Mint)



Da biste napunili svoj wallet Macadamia sa ecash-om, potrebno je da izvršite operaciju "Mint" (da kreirate tokene). Dodirnite "Receive", zatim izaberite opciju "Lightning". Unesite željeni iznos (npr. 1000 sats), izaberite mint koji će se koristiti, zatim generate Lightning fakturu.



![Opération Mint](assets/fr/05.webp)



Platite Lightning fakturu generisanu sa vašim uobičajenim wallet (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Cashu tokeni se pojavljuju odmah na vašem saldu nakon plaćanja.



### Pošalji tokene



Da biste poslali Cashu tokene drugom korisniku, dodirnite dugme "Pošalji" na glavnom ekranu, zatim izaberite "Ecash". Unesite iznos koji želite poslati (npr. 50 sats) i dodajte opisni memo ako je potrebno.



![Envoi Ecash](assets/fr/07.webp)



Podeli QR kod ili generisani tekst putem iMessage, Signal ili Telegram. Primalac preuzima sredstva odmah i bez naknade.



### Primite tokene



Da biste primili Cashu tokene koje je poslao drugi korisnik, dodirnite "Primi" zatim izaberite "Ecash". Skenirajte token QR kod ili nalepite token link koji ste primili.



![Réception Ecash](assets/fr/08.webp)



Dodirnite "Redeem" da biste preuzeli token.



### Lightning (Melt) plaćanja



Da biste platili Lightning fakturu sa svojim Cashu tokenima, dodirnite "Pošalji" zatim izaberite "Lightning". Zalepite BOLT11 fakturu koju želite platiti.



![Paiement Lightning](assets/fr/11.webp)



Mint uništava vaše tokene i izvršava Lightning uplatu. Tako možete platiti bilo koju Lightning uslugu uz očuvanje vaše anonimnosti.



### Zameni između nane



Kada primite tokene iz mint-a koji niste konfigurisali, Macadamia vam nudi nekoliko opcija za upravljanje tim tokenima.



![Swap inter-mints](assets/fr/09.webp)



Dodajte novi mint ili zamenite tokene postojećim mintom. Zamena koristi Lightning kao most za anonimni prenos vaših sredstava.



### Napredno upravljanje višestrukim mintovanjem



Macadamia nudi sofisticirane alate za upravljanje višestrukim mintovima istovremeno i strateško raspoređivanje vaših sredstava.



![Gestion multi-mints](assets/fr/10.webp)



"Distribute Funds" automatski distribuira vaš saldo prema procentima (npr. 50/50). "Transfer" omogućava ručne prenose između mintova kako biste diverzifikovali svoje rizike.



## Prednosti i ograničenja



**Istaknuto** :





- Maksimalna poverljivost**: Nepratljive transakcije, čak ni od strane kovnice. Bez blockchain metapodataka, razmene bez tragova između korisnika.
- Brzo i besplatno**: Besplatni trenutni transferi unutar minute, idealno za mikrouplate.
- Interoperabilnost**: standardizovani Cashu tokeni za upotrebu sa drugim kompatibilnim novčanicima (Minibits, Nutstash).
- Simplicity**: Interface iOS native je dostupan početnicima dok ostaje proverljiv (open source).



**Ograničenja** :





- Model čuvanja**: potrebna je poverenje u mint. Ako mint nestane, vaši tokeni gube svoju vrednost.
- iOS only**: Nema Android/desktop verzije. Cashu interoperabilnost omogućava pristup putem drugih novčanika, ali optimalno iskustvo ostaje na iOS-u.
- Zavisnost od Mint-a**: Mint van mreže = nije moguće izvršiti transakcije koje zahtevaju njegovu intervenciju (Mint, Melt).
- Tehnologija u razvoju** : Aktivni razvoj, mogući bagovi, standardi u evoluciji.



## Najbolje prakse





- Diversifikujte svoje kovnice**: Rasporedite svoje žetone na nekoliko renomiranih kovnica kako biste razredili rizik.
- Ograničite iznose**: Koristite Macadamia kao fizički wallet za dnevna plaćanja, ne kao sef.
- Osigurajte svoj seed**: Čuvajte svoju frazu od 12 reči na papiru na sigurnom mestu. Povremeno testirajte obnavljanje.
- Proveri mente**: Poseti cashu.space i forume zajednice pre nego što dodaš mentu. Izaberi one sa dobrim vremenom rada i solidnom reputacijom.
- VPN ili Tor**: Sakrijte svoj IP pomoću VPN/Tor da biste maksimizirali privatnost mreže.
- Pridružite se zajednici**: Telegram/Discord Cashu grupe za novosti, preporuke za mint i najbolje prakse.



## Zaključak



Macadamia Wallet donosi osobine fizičkog novca u digitalni Bitcoin. Kombinovanjem Chaum i Lightning slepih potpisa, nudi elegantno rešenje za transakcionu poverljivost. Njegov izvorni iOS interfejs čini sofisticiranu kriptografsku tehnologiju dostupnom, dok ostaje otvorenog koda i interoperabilan sa Cashu ekosistemom.



Model starateljstva zahteva budnost i dobre bezbednosne prakse. Ako se pravilno koristi, Macadamia postaje neprocenjiv alat za svakodnevna plaćanja koja zahtevaju anonimnost, dopunjujući nekustodijalne novčanike za štednju.



## Resursi



### Službena dokumentacija




- Zvanična veb stranica: [macadamia.cash](https://macadamia.cash)
- Macadamia FAQ: [macadamia.cash/faq](https://macadamia.cash/faq)
- Izvorni kod na GitHub-u: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Dokumentacija za Cashu




- Tehnička dokumentacija: [docs.cashu.space](https://docs.cashu.space)
- Lista javnih kovnica: [bitcoinmints.com](https://bitcoinmints.com)
- Zvanični protokol vebsajt: [cashu.space](https://cashu.space)



### Zajednica




- Telegram Cashu grupa: [t.me/cashu_ecash](https://t.me/cashu_ecash)