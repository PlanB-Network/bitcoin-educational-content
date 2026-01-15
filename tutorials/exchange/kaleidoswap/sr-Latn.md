---
name: KaleidoSwap
description: Napredni vodič za trgovanje imovinom RGB na Lightning Network sa KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap je sofisticirana open-source desktop aplikacija koja premošćuje jaz između RGB protokola i Lightning Network. Služi kao sveobuhvatno sučelje za upravljanje RGB Lightning čvorovima, interakciju sa RGB Lightning pružaocima usluga (LSPs) putem LSPS1 specifikacije, i izvršavanje atomskih zamena RGB sredstava.


Kao rešenje bez starateljstva, KaleidoSwap omogućava korisnicima da zadrže potpunu kontrolu nad svojim ključevima i podacima. Korišćenjem paradigme klijentske validacije RGB, omogućava privatne i skalabilne pametne ugovore na vrhu Bitcoin. Ovaj vodič ulazi u napredne funkcije KaleidoSwap-a, vodeći vas kroz složenosti upravljanja "Obojenim" UTXO, likvidnost kanala za specifične asete i model trgovanja uzimač-davalac, osiguravajući da možete u potpunosti iskoristiti ovaj moćni protokol decentralizovane razmene.


## Instalacija


KaleidoSwap pruža unapred izgrađene binarne datoteke za glavne operativne sisteme, ali za napredne korisnike, izgradnja iz izvornog koda osigurava da koristite najnoviji kod sa vašim specifičnim konfiguracijama.


### Preuzmi binarne datoteke


Možete preuzeti najnovije izdanje za vaš operativni sistem sa [zvaničnog sajta](https://kaleidoswap.com/) ili sa [stranice sa izdanjima na GitHub-u](https://github.com/kaleidoswap/desktop-app/releases).


### Metode Instalacije


1.  **Windows**: Preuzmite `.exe` instalacioni program i pokrenite ga.

2.  **macOS**: Preuzmite `.dmg` fajl, otvorite ga i prevucite KaleidoSwap u vaš folder Aplikacije.

3.  **Linux**: Preuzmite `.AppImage` ili `.deb` datoteku i instalirajte/pokrenite je.



## Opcije Postavljanja Čvora


Kada prvi put pokrenete KaleidoSwap, biće vam prikazan **Ekran za povezivanje**. Ovo je prvi korak u konfigurisanja vašeg okruženja.


![Node Selection Screen](assets/en/01.webp)


Morate izabrati kako da se povežete sa RGB Lightning Network. Ovaj izbor utiče na vaš nivo kontrole i privatnosti.


### Opcija 1: Lokalni čvor (Preporučeno za samostalno čuvanje)


**Za potpunu kontrolu i privatnost**, pokrenite čvor direktno na vašem računaru, pogledajte prednosti ispod:


- Samostalno čuvanje**: Vi držite ključeve. Nijedna treća strana ne može zamrznuti vaša sredstva ili cenzurisati vaše transakcije.
- Privatnost**: Vaši podaci ostaju na vašem uređaju.
- Nezavisnost**: Bez oslanjanja na spoljne pružaoce usluga.


Ako izaberete **Local Node**, bićete prebačeni na ekran za podešavanje gde možete kreirati novi wallet ili obnoviti postojeći.


![Local Node Setup Screen](assets/en/02.webp)


### Opcija 2: Udaljeni Čvor


Povežite se na udaljeni RGB Lightning Node (samohostovan na VPS-u ili kod hosting provajdera).


- Prednosti**: Nema lokalne potrošnje resursa, dostupnost 24/7.
- Kompromis**: Zahteva poverenje u domaćina ili upravljanje udaljenim serverom.


![Remote Node Setup Screen](assets/en/03.webp)


**KaleidoSwap je dizajniran da osnaži samostalno čuvanje.** Snažno preporučujemo pokretanje sopstvenog čvora—bilo lokalno (Opcija 1) ili samostalnim hostovanjem udaljenog čvora—kako biste u potpunosti iskoristili svojstva otporna na cenzuru Bitcoin i RGB.


## Kreiranje Wallet


KaleidoSwap upravlja sa Bitcoin i RGB sredstvima. Proces kreiranja wallet inicijalizuje keystore koji osigurava vaša on-chain sredstva i stanja vaših Lightning kanala.


Evo detaljnog procesa:

1. Otvorite KaleidoSwap i izaberite **Local Node**.

2. Kliknite na **Create New Wallet**.

3. **Postavljanje Naloga**: Unesite **Naziv Naloga** i izaberite **Mrežu** (npr. Bitcoin Mainnet, Testnet, Signet).

4. **Napredna konfiguracija** (Opcionalno): Ako ste napredni korisnik, možete konfigurisati prilagođene RPC krajnje tačke, URL-ove indeksatora ili Proxy postavke u okviru "Napredne postavke".

5. Kliknite **Nastavi**.

6. **Lozinka**: Postavite jaku lozinku da šifrujete vašu wallet datoteku lokalno.

7. **Recovery Phrase**: Zapišite svoju seed frazu i čuvajte je na sigurnom mestu.


    - Kritično**: Ova fraza je potrebna za povrat vaših on-chain sredstava i identiteta čvora.
    - Upozorenje**: **Stanja kanala munje ne mogu se u potpunosti oporaviti samo iz seed**. Morate takođe održavati Staticke Bekape Kanala (SCB) kako biste povratili sredstva zaključana u kanalima.


![Wallet Creation Screen](assets/en/04.webp)



## Pregled kontrolne table


Kada vaš wallet bude kreiran, bićete preusmereni na glavnu **Kontrolnu tablu**.


![KaleidoSwap Dashboard](assets/en/05.webp)


_Napomena: Snimak ekrana iznad prikazuje wallet koji je već finansiran i ima aktivne kanale. Novi wallet će prikazivati nulte bilanse i neće imati aktivne kanale dok ga ne finansirate._


## Finansiranje vašeg Wallet


Da biste upravljali sa RGB sredstvima, potrebno je da finansirate svoj wallet. KaleidoSwap podržava deponovanje i Bitcoin i RGB sredstava putem on-chain transakcija ili Lightning Network.


### Depozitovanje Bitcoin


1. Kliknite **Depozit** u meniju Brze Akcije.

2. Izaberite **BTC** sa liste sredstava.


![Select BTC Asset](assets/en/06.webp)


3. Izaberite metod depozita: **On-chain** ili **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- On-chain**: Skenirajte QR kod ili kopirajte adresu da pošaljete Bitcoin sa drugog wallet.
- Lightning**: Generiši fakturu za željeni iznos.


![BTC On-chain Deposit](assets/en/08.webp)


### Depozitovanje RGB sredstava i obojenih UTXO-a


Da biste primili RGB sredstva (kao što je USDT), potrebno je da imate specifične UTXO-ove dostupne za "bojenje" (dodeljivanje sredstva).


1. Kliknite na **Deposit** i izaberite RGB sredstvo (npr. USDT). **Važno**: Ako je ovo **prvi put** da vaš čvor prima ovo specifično sredstvo, **ostavite polje za ID sredstva prazno**. Unos ID-a za nepoznato sredstvo će uzrokovati da čvor vrati grešku jer ga još ne prepoznaje.

2. Izaberite **On-chain** ili **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### Načini primanja na lancu: Witness vs. Blinded


Kada primate RGB imovinu on-chain, imate dva režima privatnosti:



- Blinded Receive (Recommended for Privacy)**: You provide a "blinded" UTXO to the sender. You are asking the sender to send assets to an existing UTXO that you own, but you obfuscate the actual UTXO identifier. This offers better privacy.
- Witness Receive**: Vi pružate standardnu Bitcoin adresu. Tražite od pošiljaoca da kreira *novi* UTXO za vas slanjem sredstava na tu adresu. Ovo omogućava da se RGB sredstva direktno povežu sa novim UTXO kreiranim transakcijom.


#### Lightning Deposit


Za Lightning depozite, jednostavno generate fakturu. RGB sredstvo će biti prosleđeno vama kroz vaše otvorene kanale.


![USDT Lightning Invoice](assets/en/10.webp)



## Otvaranje kanala sa RGB sredstvima


Da biste usmerili RGB sredstva preko Lightning Network, potreban vam je kanal sa dovoljnom likvidnošću i alokacijom sredstava. Najlakši način da započnete je da **Kupite Kanal** od LSP-a (Lightning Service Provider).


### Kupovina kanala od Kaleido LSP


1. Idite na karticu **Kanali**. Videćete opcije "Otvori kanal" (ručno) ili "Kupi kanal" (LSP).

2. Kliknite **Buy Channel**.


![Channels Dashboard](assets/en/11.webp)


3. **Poveži se sa LSP**: Aplikacija će se povezati sa podrazumevanim Kaleido LSP. Ovaj provajder nudi dolaznu likvidnost i podržava RGB rutiranje sredstava.


![Connect to LSP](assets/en/12.webp)


4. **Konfiguriši Kanal**:


    - Kapacitet**: Odaberite ukupni kapacitet Bitcoin za kanal.
    - RGB Allocation**: Izaberite RGB sredstvo (npr. USDT) koje želite da primate ili šaljete. LSP će osigurati da je kanal konfigurisan da podržava ovo sredstvo.


![Configure Channel](assets/en/13.webp)



    - RGB Alokacija**: Izaberite RGB sredstvo (npr. USDT) koje želite da možete primati ili slati. LSP će osigurati da je kanal konfigurisan da podržava ovo sredstvo.


![RGB Allocation](assets/en/14.webp)


5.  **Payment**: Morate platiti naknadu LSP-u za otvaranje kanala i obezbeđivanje likvidnosti. Možete platiti koristeći **Lightning** ili **On-chain** Bitcoin. Plaćanje se može izvršiti sa vašeg unutrašnjeg KaleidoSwap wallet ili spoljnog wallet.


![Complete Payment](assets/en/15.webp)


6. Kada uplata bude potvrđena, LSP će pokrenuti transakciju otvaranja kanala. Videćete ekran sa porukom **Porudžbina završena**.


![Order Completed](assets/en/16.webp)


7. Nakon potvrde na blockchain-u, vaš kanal će biti aktivan i spreman za RGB transfere.



## Trgovanje: Taker-Maker model


KaleidoSwap-ov trgovački mehanizam radi na **Taker-Maker modelu**. Možete ručno zamijeniti sredstva s partnerom ili koristiti Market Maker (LSP).


### Zamena sa Market Maker-om (LSP)


Ovo je najčešći način trgovanja. Delujete kao **Taker**, izvršavajući naloge protiv dostupne likvidnosti koju obezbeđuje LSP (**Maker**).


1. Idite na karticu **Trade** i izaberite **Market Maker**.

2. **Unesite iznos**: Unesite iznos Bitcoin koji želite poslati (ili imovinu koju želite primiti). Interfejs će prikazati procenjeni kurs i naknade.


![Market Maker Swap](assets/en/17.webp)


3. **Potvrdi zamenu**: Pregledajte detalje, uključujući kurs i tačan iznos koji ćete primiti. Kliknite na **Potvrdi zamenu**.


![Confirm Swap](assets/en/18.webp)


4. **Processing**: Zamena se izvršava atomski na Lightning Network. Videćete ekran sa statusom koji pokazuje da je zamena na čekanju.


![Swap Pending](assets/en/19.webp)


5. **Uspeh**: Kada su HTLC-ovi rešeni, zamena je završena i sredstva su u vašem kanalu.


![Swap Success](assets/en/20.webp)



## Developer API


Za programere koji razvijaju na vrhu KaleidoSwap-a, aplikacija izlaže API koji podržava:



- RGB LSPS1**: Za automatizovane usluge likvidnosti.
- Swap API**: Za programatsko trgovanje i kreiranje tržišta.
- WebSocket**: Za pretplate na tržišne podatke u realnom vremenu.


Pogledajte [API Dokumentaciju](https://docs.kaleidoswap.com/api/introduction) za potpune krajnje tačke i specifikacije.


## Zaključak


KaleidoSwap vam omogućava da iskoristite privatnost i skalabilnost RGB sredstava na Lightning Network. Razumevanjem Obojenih UTXO-a i alokacije sredstava u kanalima, možete u potpunosti iskoristiti ovaj moćni protokol decentralizovane razmene.