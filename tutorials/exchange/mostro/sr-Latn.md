---
name: Mostro
description: KYC-free Bitcoin P2P exchange platform via Lightning and Nostr
---

![cover](assets/cover.webp)



Kako da kupite ili prodate bitkoine a da ne ugrozite svoju finansijsku suverenost? Centralizovane platforme nameću invazivne KYC procedure koje izlažu vaše lične podatke, uz mogućnost proizvoljnog zamrzavanja naloga ili državnog nadzora.



**Mostro P2P** nudi decentralizovanu alternativu koja kombinuje Lightning Network, Nostr protokol i hold fakture. Njegova glavna inovacija: automatizovani escrow sistem gde vaši bitcoini ostaju pod vašom kontrolom tokom cele razmene, eliminišući rizik od krađe, bankrota berze ili proizvoljne konfiskacije.



## Šta je Mostro P2P?



Mostro P2P je open source Bitcoin protokol za razmenu koji je kreirao **grunch**, developer popularnog Telegram bota **lnp2pbot** lansiranog 2021. godine. Iako je lnp2pbot već omogućavao P2P razmene bez KYC-a putem Lightning-a, predstavljao je veliku ranjivost: **Telegram predstavlja centralizovanu tačku kvara** podložnu cenzuri od strane vlada.



Mostro predstavlja **decentralizovanu evoluciju** ovog koncepta: zamenom Telegrama sa **Nostr** protokolom (necenzurisana mreža distribuiranih releja), Mostro eliminiše ovaj sistemski rizik. Protokol kombinuje Lightning Network za trenutne transakcije, Nostr za komunikaciju otpornu na cenzuru, i **hold invoices** kako bi stvorio zaista nekustodijalni automatski eskrou.



### Tehnička arhitektura



Mostro radi kroz tri komponente:




- Daemon Mostrod**: koordinira razmene između korisnika i Lightning Network
- Lightning** čvor: kreira hold fakture (~24h kriptografski escrow)
- Mostro** korisnici: korisnički interfejsi (CLI, Mobilni, Veb)



Nalozi se objavljuju na Nostr kao javni događaji (tip 38383), dok se privatne trgovine prenose putem end-to-end šifrovanih poruka (NIP-59, NIP-44). Svaka Mostro instanca definiše svoje naknade (uglavnom između 0.3% i 1%) i limite transakcija (u rasponu od nekoliko hiljada do nekoliko stotina hiljada sats, u zavisnosti od instance).



### Odlučujuće prednosti



**Otporan na cenzuru**: Nijedna vlada ne može ugasiti Mostro sve dok Nostr releji postoje negde u svetu. Za razliku od ranjivog lnp2pbot putem Telegrama, Mostro omogućava razmene koje su **otporne na cenzuru**.



**Escrow non-custodial**: Lightning hold invoices zaključavaju vaše bitkoine bez trajnog prenosa. Vaša sredstva ostaju pod vašom kontrolom i automatski vam se vraćaju u slučaju problema (~24h).



**Poverljivost po dizajnu**: Dva režima dostupna da odgovaraju vašim potrebama. Režim reputacije** povezuje vašu reputaciju sa vašim Nostr ključem kako bi izgradio trajno poverenje. Režim potpune privatnosti** favorizuje apsolutnu anonimnost sa jednokratnim efemernim ključevima.



## Glavne karakteristike



**Decentralizovana komunikacija**: Svi nalozi su objavljeni na Nostr putem kriptografski potpisanih događaja. Privatni pregovori se prenose putem end-to-end šifrovanih poruka, garantujući apsolutnu poverljivost.



**Sistem reputacije**: Ocena od 5 zvezdica sa iterativnim proračunom trajno sačuvana na Nostr-u. Omogućava vam da postepeno izgradite reputaciju pouzdanog trgovca.



**Decentralizovana arbitraža**: U slučaju spora, nepristrasni arbitar ispituje dokaze i donosi odluku na osnovu transparentnih kriterijuma. Svaki spor generiše jedinstveni token za praćenje.



**Fleksibilnost plaćanja**: Podrška za mnoge fiat valute putem yadio.io usluge kursa razmene. Prihvata SEPA transfere, PayPal, Revolut, gotovinu i bilo koji metod dogovoren između strana.



## Mostro kupci dostupni



Mostro nudi dva glavna operativna klijenta za vaše P2P razmene.



### Mostro CLI - Komandna Linija Klijent



**Mostro CLI** je najzreliji i najfunkcionalniji klijent. Napisan u Rust, nudi čitav spektar Mostro funkcija putem komandne linije. Kompatibilan sa macOS, Linux i Windows.



**Glavne kontrole** :




- `listorders`: Prikaži sve dostupne narudžbine
- `neworder` : Kreiraj novu kupovnu ili prodajnu narudžbu
- `takesell` / `takebuy`: Preuzmi nalog za kupovinu ili prodaju
- `fiatsent`: Potvrdi slanje fiat uplate
- `release`: Oslobodi escrow i finaliziraj razmenu
- `getdm`: Pregledaj direktne poruke
- `rate` : Proceni svog partnera nakon razmene



Idealno za tehničke korisnike, automatizaciju i okruženja koja zahtevaju maksimalnu sigurnost.



### Mostro Mobile - Aplikacija za pametne telefone



**Mobilna aplikacija** u alfa verziji omogućava trgovanje P2P direktno sa vašeg pametnog telefona. Intuitivni grafički Interface sa navigacijom putem kartica, pregledom narudžbi, naprednim filtrima i integrisanim četom za komunikaciju sa vašim suprotnim stranama.



Dostupno za **Android** (preko APK na GitHub-u), to je optimalan izbor za korisnike koji preferiraju jednostavnost i povremeno trgovanje putem mobilnog uređaja.



### Mostro-web - Interface web (u razvoju)



Interface napredna JavaScript veb aplikacija u fazi aktivnog razvoja. Dizajnirana da ponudi kompletno korisničko iskustvo sa opsežnim funkcionalnostima za trgovanje i upravljanje portfoliom. Pristup putem pregledača bez potrebe za instalacijom.



## Instalacija i konfiguracija



Ovaj vodič će vas provesti kroz instalaciju i korišćenje dva glavna Mostro klijenta: CLI i mobilne aplikacije.



### Osnovni preduslovi



Pre nego što počnete, biće vam potrebno :





- Radni Lightning Network** wallet sa dovoljnom likvidnošću (ili kompatibilan sa Lightning-om)
 - Preporučeno: Phoenix, Breez, Wallet ili Satoshi...
 - Minimalno 1000 satoshija likvidnosti za testiranje



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Privatni ključ Nostr** (format `nsec1...`)
 - Kreirajte posvećeni ključ za trgovanje na [nostrkeygen.com](https://nostrkeygen.com/)
 - Važno**: Nikada ne koristite svoj glavni lični Nostr ključ
 - Čuvajte svoj privatni ključ na sigurnom mestu (menadžer lozinki)





- Opcionalno, ali preporučeno**: VPN ili Tor veza za maskiranje vaše IP adrese



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI instalacija



#### Na macOS-u



**Korak 1: Rust provera**



Proverite da li je Rust instaliran (potrebna verzija 1.64+):



```bash
rustc --version
```



Ako Rust nije instaliran :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Korak 2: Kloniranje repozitorijuma**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Korak 3: Konfiguracija**



Kopiraj i izmeni sledeće:



```bash
cp .env-sample .env
```



Otvorite `.env` i konfigurišite svoja podešavanja:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Važno za CLI/Mobilnu** sinhronizaciju: Da biste pristupili istim porudžbinama na CLI i mobilnoj aplikaciji, morate koristiti **isti Mostro Pubkey** i iste **Nostr releje** u oba klijenta. Proverite ova podešavanja u Podešavanjima na mobilnoj aplikaciji.



![Configuration .env](assets/fr/02.webp)



**Korak 4: Instalacija**



Kompajlirajte i instalirajte CLI :



```bash
cargo install --path .
```



Kompilacija traje 1-2 minuta. Izvršni fajl `mostro-cli` biće instaliran u `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Korak 5: Proveri**



Proverite da sve radi:



```bash
mostro-cli --help
```



Trebalo bi da vidite kompletnu listu narudžbina.



![Vérification avec --help](assets/fr/04.webp)



#### Na Linuxu (Ubuntu/Debian)



Instalacija identična macOS-u, uz dodatak:



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Zatim pratite korake 3 i 4 u odeljku za macOS.



#### Na Windowsu



Prvo instalirajte Rust putem [rustup.rs](https://rustup.rs/), zatim koristite PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Identicalna konfiguracija: kopirajte `.env-sample` u `.env` i popunite vaše parametre.



### Instaliranje Mostro Mobile



#### Na Androidu



**Korak 1**: Idite na [GitHub stranicu sa izdanjima](https://github.com/MostroP2P/mobile/releases) i preuzmite datoteku **app-release.apk** (približno 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Korak 2:** Kada preuzmete, otvorite APK datoteku iz vaših preuzimanja. Android će vas pitati da autorizujete instalaciju sa ovog izvora.



![Téléchargement et installation APK](assets/fr/11.webp)



**Korak 3**: Pratite ekrane za uvod, koji prikazuju funkcionalnosti:




- Trgujte Bitcoin slobodno - bez KYC** : Trgujte bez verifikacije identiteta zahvaljujući Nostr
- Privatnost po podrazumevano**: Izaberite između režima reputacije i režima potpune privatnosti
- Sigurnost na svakom koraku**: Zaštita uz fakture sa ne-kustodijalnim zadržavanjem



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Korak 4**: Nastavite sa procesom uvođenja kako biste otkrili :




- Potpuno šifrovani čet**: Komunikacija šifrovana od kraja do kraja
- Prihvatite ponudu**: Pregledajte knjigu naloga i izaberite ponudu
- Ne možete pronaći ono što vam treba?** : Kreirajte svoju sopstvenu prilagođenu narudžbinu



![Suite onboarding](assets/fr/13.webp)



**Korak 5:** Kada je proces prijave završen, aplikacija automatski generiše par Nostr ključeva. Idite na meni (☰) zatim **Nalog** da sačuvate svoje **Tajne Reči** (fraza za oporavak). Takođe, na ovom ekranu imate opciju da promenite prethodno pomenuti režim privatnosti.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Važno**: Zapišite svoju frazu za oporavak na sigurno mesto (menadžer lozinki, sef za papire).



### Početna sigurnosna konfiguracija



Koju god platformu koristiš :





- Posvećen ključ**: Koristite poseban Nostr identitet za trgovanje
- Male količine**: Počnite sa manje od sats 10,000 da biste započeli
- Više releja**: Konfigurišite 3-5 geografski raznovrsnih releja
- Zaštita mreže**: Aktivirajte VPN ili Tor da sakrijete svoju IP adresu
- Wallet secure**: Aktivirajte automatsko zaključavanje vašeg wallet Lightning



## Koristi sa CLI



Ovaj odeljak demonstrira kupovinu bitkoina putem Mostro CLI prateći stvarni slučaj upotrebe.



### Korak 1: Navedi dostupne narudžbine



Komanda `listorders` prikazuje sve aktivne narudžbine:



```bash
mostro-cli listorders
```



Videćete tabelu sa detaljima svake narudžbine: ID, tip (kupovina/prodaja), iznos, valuta, način plaćanja.



![Liste des ordres disponibles](assets/fr/05.webp)



U ovom primeru, vidljiv je nalog za prodaju 5 EUR putem Revoluta (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Korak 2: Preuzimanje narudžbine



Da biste kupili ove bitkoine, preuzmite narudžbinu sa `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro će vas zamoliti da obezbedite **Lightning fakturu** za primanje BTC-a. Tačan iznos u satoshijima je naveden (ovde: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Korak 3: Obezbedite svoj Lightning račun



Generiši Lightning fakturu sa svog wallet (Phoenix, Breez, itd.) za tačan iznos, zatim je pošalji :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Sistem potvrđuje pošiljku i govori vam da sačekate da prodavac plati fakturu na čekanju pre nego što aktivirate eskrou.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Korak 4: Kontaktirajte prodavca



Jednom kada je escrow aktiviran, koristite `dmtouser` da zatražite detalje plaćanja od prodavca:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Korak 5: Preuzmi odgovor



Proveri direktne poruke da vidiš odgovor prodavca:



```bash
mostro-cli getdm
```



Prodavac vam daje svoj ID za plaćanje (ovde njegov Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Korak 6: Izvršavanje fiat uplate



Pošaljite uplatu putem dogovorenog metoda (Revolut u ovom primeru) na dostavljene kontakt podatke. **Sačuvajte sve prateće dokumente** (screenshot-ove, reference transakcija).



### Korak 7: Potvrdite slanje uplate



Kada uplata bude izvršena, obavestite Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Korak 8: Prijem bitkoina



Čim prodavac potvrdi prijem fiat-a i oslobodi escrow komandom `release`, odmah dobijaš svoje bitkoine na Lightning fakturi koju si obezbedio.



### Korak 9: Evaluacija



Ocenite prodavca kako biste doprineli decentralizovanoj reputaciji:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Korisne komande



**Otkaži narudžbinu** (pre nego što je preuzeta) :


```bash
mostro-cli cancel -o <order-id>
```



**Kreiraj novu prodajnu narudžbu** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Otvorite spor** :


```bash
mostro-cli dispute -o <order-id>
```



## Koristite sa mobilnom aplikacijom



Ovaj odeljak prikazuje prodaju bitkoina putem Mostro Mobile-a prateći stvarni slučaj upotrebe.



### Interface glavni



Aplikacija ima 3 glavne kartice:





- Order Book**: Pregledajte dostupne naloge za kupovinu (BUY BTC) i prodaju (SELL BTC)
- Moje trgovine**: Pogledajte vaše aktivne i istorijske naloge
- Ćaskom**: Komunicirajte sa svojim partnerima koristeći brojke



![Interface principale](assets/fr/14.webp)



### Preporučena konfiguracija



Pre trgovanja, konfigurišite nekoliko postavki putem menija (☰) > **Settings** :





- Lightning Address** (opciono): Da primate uplate direktno
- Relays**: Dodajte nekoliko Nostr releja za otpornost (npr. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Proverite javni ključ instance Mostro koju koristite



![Paramètres de l'application](assets/fr/16.webp)



**Važno za CLI/Mobilnu sinhronizaciju**: Ako koristite i CLI i mobilnu aplikaciju, konfigurišite **potpuno iste Nostr releje i Mostro Pubkey** u oba klijenta. Bez ove identične konfiguracije, nećete videti iste porudžbine dostupne na oba interfejsa. Releji i Mostro Pubkey vidljivi u Podešavanjima (screenshot iznad) moraju odgovarati onima u vašem CLI `.env' fajlu.



### Korak 1: Kreirajte nalog za prodaju



Pritisnite zeleni **"+"** dugme u donjem desnom uglu, zatim odaberite **PRODAJ** (crveno dugme).



![Boutons de création d'ordre](assets/fr/17.webp)



Popunite obrazac za kreiranje :



1. **Valuta**: Odaberite valutu koju želite da primite (EUR, USD, itd.)


2. **Amount** : Unesite iznos u fiat valuti (npr. 1 do 3 EUR)


3. **Metode plaćanja** : Izaberite metodu (npr. "Revolut")


4. **Tip cene**: Izaberite "Tržišna cena"


5. **Premija**: Podesite premiju (klizač od -10% do +10%, preporučeno: 0% za brzu prodaju)



Pritisnite **Submit** da objavite svoju narudžbu.



### Korak 2: Potvrda objavljivanja



Vaša narudžbina je sada objavljena! Biće dostupna 24 sata. Možete je otkazati u bilo kom trenutku pre nego što je kupac preuzme izvršavanjem komande `cancel`.



![Ordre publié](assets/fr/18.webp)



Porudžbina se pojavljuje na kartici **Moje trgovine** sa statusom "Na čekanju" i oznakom "Kreirano od strane vas".



### Korak 3: Kupac preuzima vašu narudžbinu



Kada kupac preuzme vašu narudžbu, dobijate obaveštenje. Pogledajte detalje u **Moje trgovine**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Važno uputstvo**: Morate sada **platiti fakturu na čekanju** prikazanu da biste zaključali svoje bitkoine (ovde 4674 sats za 1-5 EUR) u eskrou. Imate **maksimalno 15 minuta**, inače će razmena biti otkazana.



Kopirajte fakturu na čekanju i platite je sa svog wallet Lightning (Phoenix, Breez, itd.).



### Korak 4: Komunicirajte sa kupcem



Jednom kada je eskrou aktiviran, pritisnite **CONTACT** da otvorite šifrovani čet sa kupcem.



Kupac (ovde "anonymous-gloriaZhao") će vas kontaktirati da zatraži vaše podatke za plaćanje. Molimo vas da odgovorite sa vašim podacima (Revtag, IBAN, itd.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Korak 5: Prijem fiat uplate



Sačekajte dok ne primite fiat uplatu na vaš Revolut račun (ili drugi dogovoreni metod). **Pažljivo proverite**:




- Tačan iznos
- Pošiljalac
- Referenca ako se zatraži



Kupac će vas obavestiti putem četa da je poslao uplatu. Mostro će takođe prikazati poruku koja potvrđuje da vam je fiat poslat.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Korak 6: Oslobađanje escrow-a



Kada **potvrdite prijem** fiat uplate na vašem računu, pritisnite zeleni taster **RELEASE** i potvrdite slanje satss kupcu.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoini se trenutno prenose kupcu putem njegovog Lightning računa.



### Korak 7: Proceni razmatranje



Nakon objavljivanja, pritisnite **OCENI** da ocenite kupca. Izaberite od 1 do 5 zvezdica (ovde 5/5) i pritisnite **Pošalji ocenu**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Razmena je završena!



### Kupite bitkoine putem mobilne aplikacije



Proces za **kupovinu** bitkoina je sličan, ali obrnut:



1. Pregledajte **Order Book** > karticu **BUY BTC** da biste videli naloge za prodaju


2. Kliknite na zanimljivu narudžbinu da biste videli detalje


3. Pritisnite **Take Order**


4. Pružite svoj Lightning račun (generisan iz vašeg wallet)


5. Sačekajte da prodavac aktivira escrow


6. Kontaktirajte prodavca putem **CONTACT** za detalje o plaćanju


7. Pošaljite fiat uplatu (sačuvajte dokaz)


8. Prodavac oslobađa escrow nakon verifikacije


9. Primite bitkoine trenutno na vašem Lightning računu


10. Ocenite prodavca (1-5 zvezdica)



### Upravljanje problemima



**Otkaži narudžbu**: U **Moje trgovine**, pritisnite vašu narudžbu, a zatim dugme **OTKAŽI** (dostupno samo pre nego što bude preuzeta).



**Otvorite spor**: Ako dođe do neslaganja, pritisnite **SPOR** u detaljima narudžbine. Priložite sve dokaze (screenshot-ove razgovora, reference bankovnih transakcija).



## Prednosti i ograničenja



### Pogodnosti



**Finansijski suverenitet**: Vaši bitkoini nikada ne napuštaju vašu direktnu kontrolu zahvaljujući mehanizmu hold fakture, eliminišući rizik od bankrota berze ili piraterije.



**Otporan na cenzuru**: Nijedna vlast ne može ugasiti mrežu ili cenzurisati vaše naloge. Sistem funkcioniše sve dok su Nostr releji operativni.



**Podrazumevana anonimnost**: Samo pseudonimni Nostr ključ vas identifikuje, bez KYC ili ličnih podataka. Komunikacija šifrovana od kraja do kraja.



**Fleksibilnost plaćanja**: Moguć je bilo koji međusobno prihvaćen način plaćanja (transferi, mobilne aplikacije, gotovina, razmena).



### Ograničenja



**Rani razvoj**: Rudimentarni interfejsi i potrebna tehnička kriva učenja.



**Ograničena likvidnost**: Ograničen broj naloga, posebno za velike iznose ili retke valute.



**Tehnički zahtevi**: Potrebno osnovno razumevanje Lightning-a i Nostr-a.



**Individualna odgovornost**: Nema centralizovane podrške u slučaju problema, potreban oprez.



## Zaključak



Mostro P2P predstavlja obećavajuću alternativu centralizovanim berzama, kombinujući Lightning Network, Nostr i automatizovani escrow za istinski decentralizovanu trgovinu. Uprkos ranoj fazi razvoja i ograničenoj likvidnosti, platforma već nudi finansijski suverenitet, otpornost na cenzuru i podrazumevanu anonimnost.



Za bitkoinere koji preferiraju autonomiju i poverljivost, Mostro je održiva opcija vredna progresivnog istraživanja. Njegova decentralizovana arhitektura garantuje evoluciju zajednice, a ne komercijalnu evoluciju, otvarajući put ka budućnosti zaista slobodnih Bitcoin razmena.



## Resursi



### Zvanična dokumentacija




- [Mostro official website](https://mostro.network)
- [Tehnička dokumentacija](https://mostro.network/docs-english/index.html)
- [Mostro Foundation](https://mostro.foundation)



### Izvorni kod i razvoj




- [Main GitHub repository](https://github.com/MostroP2P/mostro)
- [Web klijent](https://github.com/MostroP2P/mostro-web)
- [Kupac CLI](https://github.com/MostroP2P/mostro-cli)



### Zajednica




- [Nostr Protocol](https://nostr.com)
- [Lightning Network Vodiči](https://lightning.network)