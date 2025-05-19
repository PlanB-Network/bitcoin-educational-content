---
name: LNP2PBot
description: Kompletan vodič za LNP2PBot i P2P Bitcoin trgovanje
---
![cover](assets/cover.webp)


## Uvod


Peer-to-peer razmene bez KYC (P2P) su ključne za očuvanje poverljivosti korisnika i finansijske autonomije. Omogućavaju direktne transakcije između pojedinaca bez potrebe za verifikacijom identiteta, što je od suštinskog značaja za one koji cene privatnost. Za dublje razumevanje teorijskih koncepata, pogledajte kurs BTC204:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Kupovina i prodaja Bitcoin peer-to-peer (P2P) je jedan od najprivatnijih metoda za sticanje ili raspolaganje bitcoinima. LNP2PBot je open source Telegram bot koji omogućava P2P razmene na Lightning Network, omogućavajući brze, niskotarifne transakcije bez KYC-a.


### Zašto koristiti Lnp2pbot?




- Nije potreban KYC
- Brze transakcije na Lightning Network
- Niski troškovi
- Jednostavan Interface putem Telegrama, popularne aplikacije za razmenu poruka dostupne sa bilo kog mesta na svetu
- Integrisani sistem reputacije
- Automatski eskrou za sigurnu trgovinu
- Podrška za više valuta
- Aktivna i rastuća zajednica


### Preduslovi


Da biste koristili Lnp2pbot, trebat će vam :


1. Lightning Network Wallet (Breez, Phoenix ili Blixt preporučeno)


2. Instalirana aplikacija Telegram (https://telegram.org/)


3. Telegram nalog sa definisanim korisničkim imenom


## Instalacija i konfiguracija


### 1. Konfigurisanje vašeg Lightning Wallet


Počnite instaliranjem kompatibilnog Lightning Wallet. Evo naših detaljnih preporuka:


**Preporučeni novčanici**




- [Breez](https://breez.technology)**:
  - Odlično za početnike
  - Intuitivan, moderan Interface
  - Nekustodijalni (vi zadržavate kontrolu nad svojim sredstvima)
  - Savršeno kompatibilan sa Lnp2pbot
  - Dostupno na iOS i Android


Ispod je link ka uputstvu za ovaj Wallet:


https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06


- [Phoenix](https://phoenix.acinq.co)** :
  - Jednostavno i pouzdano
  - Automatska konfiguracija kanala
  - Izvorna podrška za BOLT11 fakture
  - Odličan za svakodnevne transakcije
  - Dostupno na iOS i Android


Ispod je link ka uputstvu za ovaj Wallet:


https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


- [Blixt](https://blixtwallet.github.io)** :
  - Više tehnički, ali veoma kompletno
  - Napredne opcije konfiguracije
  - Savršeno za iskusne korisnike
  - Otvoreni kod
  - Dostupno na Androidu


Ispod je link ka uputstvu za ovaj Wallet:


https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Važne napomene o drugim novčanicima**


⚠️ **Važno**: Pre nego što prodate Sats, uverite se da vaš Wallet podržava fakture za "zadržavanje", koje bot koristi kao sistem eskroua.




- Wallet od Satoshi**: Dobro funkcioniše za primanje Sats, ali može imati kašnjenja u ažuriranju stanja ako je prodaja otkazana.
- Muun**: Nije preporučeno jer plaćanja mogu propasti zbog ograničenja naknada za usmeravanje botova (maksimalno 0,2%).
- Aqua**: Radi da primi Sats, ali može imati duža kašnjenja (do 48 sati) za ažuriranja stanja u slučaju otkazivanja prodaje.


💡 **Savjet**: Za optimalno iskustvo, odlučite se za preporučene novčanike (Breez, Phoenix ili Blixt).


⚠️ **Važno**: Ne zaboravite da sačuvate svoje fraze za oporavak na sigurnom mestu.


### 2. Početak rada sa Lnp2pbot


1. Kliknite na ovaj link da pristupite botu: [@lnp2pBot](https://t.me/lnp2pbot)


2. Telegram će se automatski otvoriti


3. Kliknite na "Start" ili pošaljite komandu "/start"


4. Bot će vas zamoliti da kreirate korisničko ime ako ga već nemate.


5. Bot će vas voditi kroz početnu konfiguraciju


### 3. Pridruži se zajednici




- Pridružite se glavnom kanalu: [@p2plightning](https://t.me/p2plightning)
- Podrška: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)


## Kupovina i prodaja Bitcoina


Postoje dva glavna načina za Exchange bitkoina na Lnp2pbot:


1. Pregledajte i odgovorite na postojeće ponude na tržištu


2. Kreirajte svoju ponudu za kupovinu ili prodaju


U ovom vodiču, detaljno ćemo pogledati kako :




- Kupite bitkoine iz postojeće ponude
- Prodajte bitkoine kreiranjem sopstvene ponude


### Kako kupiti Bitkoine


**1. Pronađite i odaberite ponudu**


![Sélection d'une offre de vente](assets/fr/01.webp)


Pregledajte ponude na [@p2plightning](https://t.me/p2plightning) i kliknite na dugme "Buy satoshis" ispod oglasa koji vas zanima.


**2. Validiraj ponudu i iznos**


![Validation de l'offre](assets/fr/02.webp)


1. Povratak na bot četat


2. Potvrdite svoj izbor ponude


3. Unesite iznos u fiat valuti koji želite da kupite


4. Bot će vas zamoliti da obezbedite Lightning Invoice za iznos u satoshijima


**3. Kontaktirajte prodavca**


![Mise en relation](assets/fr/03.webp)


Jednom kada je Invoice poslat, bot vas povezuje sa prodavcem.


**4. Komunikacija sa prodavcem**


![Chat privé](assets/fr/04.webp)


Kliknite na nadimak prodavca da otvorite privatni kanal za ćaskanje gde možete Exchange detalje o fiat plaćanju.


**5. Potvrda o uplati


![Confirmation du paiement](assets/fr/05.webp)


Nakon što izvršite fiat uplatu, koristite komandu `/fiatsent` u bot četu. Kada transakcija bude završena, moći ćete da ocenite prodavca i transakcija će biti zatvorena.


### Kako prodati Bitcoine


**1. Kreiraj prodajnu ponudu**


![Création d'une offre de vente](assets/fr/06.webp)


Da biste kreirali prodajnu ponudu, jednostavno koristite komandu :


`/prodaj`


Bot će vas zatim voditi korak po korak:


1. Izaberite svoju valutu


2. Naznačite količinu satoshija za prodaju


3. Za cenu, imate dve opcije:




   - Postavite fiksnu cenu za količinu satoshija
   - Koristite tržišnu cenu sa opcijom primene premije (pozitivne ili negativne)


💡 **Savjet**: Premija vam omogućava da prilagodite svoju cenu u odnosu na tržišnu cenu. Na primer, premija od -1% znači da prodajete za 1% manje od tržišne cene.


**2. Potvrda kreiranja narudžbine**


![Confirmation de l'ordre de vente](assets/fr/07.webp)


Kada je narudžbina kreirana, videćete potvrdu sa opcijom da otkažete narudžbinu koristeći komandu `/cancel`.


**3. Upravljanje prodajom**


![Prise de l'ordre par un acheteur](assets/fr/08.webp)




- Kada kupac odgovori na vašu ponudu, dobićete obaveštenje sa QR kodom i Invoice za plaćanje.
- Proverite profil i reputaciju kupca.


![Mise en relation avec l'acheteur](assets/fr/09.webp)




- Kliknite na nadimak kupca da otvorite kanal za privatnu diskusiju.
- Komunicirajte detalje o fiat uplati kupcu.
- Sačekajte potvrdu fiat uplate od kupca.
- Proverite da li je uplata primljena na vaš račun.


![Confirmation de la fin de l'ordre](assets/fr/10.webp)




- Potvrdite transakciju sa `/release` i završite narudžbinu. Imaćete priliku da ocenite kupca.


## Dobre prakse i bezbednost


### Saveti za bezbednost




- Počnite sa malim količinama
- Uvek proveravajte reputaciju korisnika
- Koristite samo predložene metode plaćanja
- Čuvajte svu komunikaciju u bot četu
- Nikada ne delite osetljive informacije


### Sistem reputacije




- Svaki korisnik ima ocenu reputacije
- Uspešne transakcije povećavaju vaš skor
- Izaberite korisnike sa dobrom reputacijom
- Prijavite svako sumnjivo ponašanje moderatorima


### Rešavanje sporova


1. Kada se problemi pojave, ostanite smireni i profesionalni


2. Koristite komandu `/dispute` da otvorite tiket


3. Obezbedite sve potrebne dokaze


4. Sačekajte moderatora


## Poređenje sa drugim rešenjima


Lnp2pbot ima nekoliko prednosti i nedostataka u odnosu na druga P2P Exchange rešenja kao što su Peach, Bisq, HodlHodl i Robosat:


### Prednosti Lnp2pbot




- Nije potreban KYC** : Za razliku od nekih platformi, Lnp2pbot ne zahteva verifikaciju identiteta, čime se čuva poverljivost korisnika.
- Brze transakcije**: Zahvaljujući Lightning Network, transakcije su gotovo trenutne.
- Niske naknade** : Troškovi transakcija su niži nego kod tradicionalnih berzi.
- Dostupnost na mobilnim uređajima**: LNP2PBot je dostupan putem Telegrama, što ga čini jednostavnim za korišćenje na mobilnim uređajima.
- Lako za korišćenje** : Lnp2pbot-ov intuitivni Interface čini ga lakim za korišćenje, čak i za manje iskusne korisnike.


### Nedostaci Lnp2pbot




- Telegram zavisnost**: Korišćenje Lnp2pbot-a zahteva Telegram nalog, što možda nije pogodno za sve korisnike.
- Manja likvidnost**: U poređenju sa etabliranijim platformama kao što je Bisq, likvidnost može biti ograničenija.


U poređenju, rešenja kao što je Bisq nude veću likvidnost i desktop Interface, ali mogu uključivati veće naknade i duže vreme transakcije. HodlHodl i Robosat, u međuvremenu, takođe nude trgovanje bez KYC-a, ali sa različitim strukturama naknada i interfejsima.


## Korisni resursi




- Zvanična veb stranica: https://lnp2pbot.com/
- Dokumentacija: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Podrška: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)