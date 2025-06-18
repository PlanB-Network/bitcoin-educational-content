---
name: Lipa
description: Postavljanje i korišćenje Lipa lightning mobilnog Wallet
---
![cover](assets/cover.webp)


A Bitcoin Lightning Wallet je mobilna aplikacija koja omogućava trenutne, niskotarifne transakcije na Bitcoin's Lightning Network. Za razliku od transakcija na glavnom Blockchain (On-Chain), Lightning plaćanja su skoro trenutna i zahtevaju minimalne naknade, što ih čini posebno pogodnim za male, svakodnevne isplate.


Lightning novčanici, kao i svi mobilni novčanici, smatraju se "Hot" novčanicima jer su povezani na Internet. Stoga su prvenstveno namenjeni za upravljanje manjim iznosima novca za vašu svakodnevnu potrošnju. Za veće iznose, preporučljivo je koristiti sigurnija rešenja za skladištenje kao što su hardverski novčanici.


Ako želite da saznate više o Lightning Network i razumete kako tehnički funkcioniše, preporučujem da pohađate ovaj kurs:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

U ovom vodiču, pogledaćemo **Lipa**, jednostavan i efikasan Lightning Wallet razvijen u Švajcarskoj.


## Predstavljamo Lipa


Lipa je ne-kustodijalni Lightning Wallet koji se ističe jednostavnošću korišćenja i preglednim Interface. Razvijen od strane švajcarskog tima, naglašava poverljivost i lakoću korišćenja za početnike.


Ključne karakteristike uključuju:




- Intuitivni korisnik Interface
- Autonomno upravljanje Lightning kanalom
- Podrška za LNURL protokol
- Mogućnost kupovine bitkoina direktno u aplikaciji


## Instalacija i konfiguracija Lipa


Prvi korak je preuzimanje aplikacije Lipa. Za sada je dostupna samo na iOS :




- [Za Apple](https://apps.apple.com/app/lipa-Bitcoin-lightning/id1602180066)


Android verzija je trenutno u razvoju i biće dostupna uskoro.


![Installation de Lipa](assets/fr/01.webp)


Kada pokrenete aplikaciju, stići ćete na početni ekran, koji vam nudi dve opcije:




- Kreiraj novi Wallet
- Vratite postojeći Wallet iz rezervne kopije


Kada odaberete svoju opciju, aplikacija će vas podstaći da omogućite obaveštenja. Ovaj korak je važan, jer su obaveštenja neophodna za :




- Primajte obaveštenja kada su uplate primljene, čak i kada je aplikacija zatvorena.
- Budite informisani o koracima uključenim u kupovinu Bitcoin putem njihovog integrisanog rešenja


Aplikacija zatim predstavlja svoje glavne funkcije kroz niz uvodnih ekrana:




- Besprekoran prijem uplata**: Korisnici mogu primati Bitcoin uplate čak i kada je aplikacija zatvorena, što garantuje pouzdanost i praktičnost.
- Adrese za Lightning bez starateljstva**: Lipa sada podržava adrese za Lightning bez starateljstva, poboljšavajući privatnost i sigurnost tako što korisnicima daje potpunu kontrolu nad njihovim bitcoinima.
- Kontrola nad analitičkim podacima** : Sa transparentnošću i poverljivošću kao prioritetima, korisnici mogu pregledati tipove prikupljenih podataka i odabrati svoje preferencije deljenja.
- Pošalji putem broja telefona**: Nema potrebe za složenim adresama - jednostavno izaberite kontakt, unesite iznos i pošaljite bitkoine direktno na njihov broj telefona.


Aplikacija takođe ima koristi od kontinuiranih poboljšanja u pogledu stabilnosti, sigurnosti i pouzdanosti, kako bi se garantovalo optimalno korisničko iskustvo.


## Navigacija aplikacijom


Interface aplikacije Lipa organizovana je oko 4 glavne kartice dostupne putem navigacione trake na dnu ekrana:


![Navigation principale](assets/fr/02.webp)




- Početna**: Prikazuje vaš trenutni saldo i istoriju transakcija
- Skenner**: Omogućava vam da skenirate QR kodove za plaćanje
- Mapa**: Prikazuje interaktivnu mapu preduzeća u vašem području koja prihvataju Bitcoin
- Postavke**: Pristup postavkama aplikacije, rezervnim kopijama i preferencijama


Dodatni meni može se pristupiti povlačenjem početnog ekrana nadole:


![Menu supplémentaire](assets/fr/03.webp)


Ova gesta otkriva dodatne funkcije kao što su :




- Kupovina bitkoina
- On-Chain Bitcoin depozit
- Kreiranje Lightning faktura za primanje bitkoina
- Lightning Invoice plaćanje


## Sačuvaj svoj Wallet


Da biste napravili rezervnu kopiju vašeg Wallet, idite na karticu "Settings" i odaberite "Recovery phrase". Lipa koristi frazu za oporavak koju je neophodno pažljivo zapisati na fizički medij (papir, metal). Ova fraza je jedini način da povratite svoja sredstva ako vaš telefon bude izgubljen ili ukraden. Da biste potvrdili vašu rezervnu kopiju, aplikacija će vas zamoliti da potvrdite 3 nasumične reči iz vaše fraze.


![Backup](assets/fr/04.webp)


Za više informacija o tome kako pravilno napraviti rezervnu kopiju i upravljati vašom frazom za oporavak, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Primite bitkoine


Da biste primili bitkoine, imate dve opcije. Da biste pristupili ovim opcijama, vratite se na početni ekran i povucite ekran nadole. Zatim možete ili:




- Odaberite "Transfer BTC" da primite bitkoine On-Chain. Zatim jednostavno skenirajte QR kod sa vašim drugim Wallet i završite transakciju.
- Odaberite "Zahtev" da primite putem Lightning Network i unesite iznos koji želite da primite.


U oba slučaja, moraćete da platite naknadu u iznosu od 0,4% od sume, ili oko 2.500 Sats ako aplikacija mora da otvori novi kanal plaćanja (što će neizbežno biti slučaj za prvu uplatu).


![Recevoir des bitcoins on chain](assets/fr/05.webp)


![Recevoir des bitcoins lightning](assets/fr/06.webp)


## Pošalji bitkoine


Da biste poslali bitkoine, idite na početni ekran, povucite ekran nadole i izaberite "Plati". Zatim jednostavno ili:




- unesi munju LNURL Address
- skenirajte QR kod munje da izvršite plaćanje.


Takođe možete otići na drugu karticu na dnu ekrana da direktno skenirate QR kod.


![Envoi de bitcoins](assets/fr/07.webp)


## Kupi bitkoine


Lipa nudi mogućnost kupovine bitkoina direktno u aplikaciji uz naknadu od 1,5%. Da biste izvršili kupovinu, idite na početni ekran i povucite nadole da biste prikazali meni. Zatim izaberite "Buy BTC". Tri uvodna ekrana će vas voditi kroz proces kupovine.


![Menu d'achat](assets/fr/08.webp)


Zatim jednostavno unesite podatke o banci sa računa koji ćete koristiti za kupovinu. Izaberite svoju valutu i unesite svoj e-mail Address.


Nakon ekrana za učitavanje, pronaći ćete referentni broj koji treba uključiti u transfer koji ćete izvršiti, kao i bankovne podatke za Exchange.


![Sélection du montant](assets/fr/09.webp)


Sve što treba da uradite je da koristite svoju banku za prenos željenog iznosa, postavite transfer tako što ćete navesti prethodno preuzeti RIB i naznačiti referencu u trenutku transakcije kako bi Lipa mogla da poveže ovaj bankarski pokret sa vašim Lipa Wallet.


![Confirmation d'achat](assets/fr/10.webp)


## Prednosti i nedostaci


### Pogodnosti




- Intuitivni Interface
- Ispravne naknade za uslugu
- Nekustodijalni
- Integrisano Bitcoin rešenje za kupovinu
- Integracija BTCmap
- podrška za NFC


### Nedostaci




- Nije moguće poslati bitkoine on chain
- Nešto duže od prosečnog plaćanja


Lipa je odličan izbor za početak sa Lightning Network, posebno pogodan za korisnike koji traže jednostavno rešenje za svakodnevna plaćanja. Njegova jednostavnost korišćenja i pregledan Interface čine ga idealnim Wallet za početnike, dok nudi osnovne funkcije za svakodnevnu upotrebu Lightning-a.


## Resursi




- [Lipina zvanična veb stranica](https://lipa.swiss/)
- [Lipa support](https://getlipa.atlassian.net/servicedesk/customer/portal/1)