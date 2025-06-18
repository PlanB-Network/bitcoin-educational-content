---
name: Proton Wallet
description: Instaliranje i korišćenje Proton Bitcoin Wallet
---
![cover](assets/cover.webp)


Proton je švajcarska kompanija specijalizovana za digitalnu privatnost, osnovana 2014. godine od strane naučnika iz CERN-a. Poznata po svojim open source rešenjima, Proton nudi niz usluga uključujući Proton Mail, Proton VPN i Proton Drive.


Proton je nedavno predstavio Proton Wallet, open-source, self-custody Bitcoin Wallet dostupan kao mobilna aplikacija ili web klijent, povezan sa vašim Proton nalogom. Funkcionalnosti Wallet su za sada relativno klasične, sa osnovnim alatima koji se očekuju od dobrog Bitcoin Wallet, kao što su RBF (*Replace-by-fee*), označavanje, ili mogućnost dodavanja BIP39 passphrase.


Posebna karakteristika ovog Wallet je mogućnost slanja bitcoina koristeći email primaoca Address, za što Proton automatski generiše prazan Bitcoin Address povezan sa korisnikovim Wallet. Proton planira dodati nove funkcije u budućnosti, uključujući Lightning i coinjoins (verovatno koristeći Whirlpool, kako sugeriše aktivnost na njihovom GitHub repozitorijumu).


## Kreiraj Proton nalog


Da biste koristili Proton Wallet, potreban vam je Proton nalog. Možete ga besplatno kreirati prateći prve korake ovog vodiča posvećenog kreiranju Proton poštanskog sandučeta (samo deo "*Kreiranje Proton naloga*"). Kada vaš nalog bude podešen, možete nastaviti sa ostatkom ovog vodiča.


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Poveži se na Proton Wallet


Idite na [veb-sajt Proton Wallet](https://proton.me/Wallet) i kliknite na dugme "*Get Proton Wallet*".


![Image](assets/fr/01.webp)


Izaberite opciju "*Besplatno*" pretplate, zatim kliknite na "*Prijavi se*".


![Image](assets/fr/02.webp)


Unesite email i lozinku povezane sa vašim Proton nalogom da biste se prijavili.


![Image](assets/fr/03.webp)


Vaš nalog bi sada trebao biti prikazan. Kliknite na "*Počnite koristiti Proton Wallet sada*".


![Image](assets/fr/04.webp)


## Kreiraj Bitcoin Wallet


Izaberite podrazumevanu fiat valutu za vaš nalog, zatim kliknite na "*Create new Wallet*".


![Image](assets/fr/05.webp)


Vaš Bitcoin Wallet je sada kreiran. Teoretski ga možete odmah početi koristiti, ali je veoma važno da prvo sačuvate vaš Mnemonic. Da biste to uradili, kliknite na "*Osigurajte vaš Wallet*" u gornjem desnom uglu Interface.


![Image](assets/fr/06.webp)


Ako to već niste učinili na Proton-u, od vas će se tražiti da postavite rezervnu kopiju za svoj nalog i osigurate ga korišćenjem 2FA metode. Ove mere bezbednosti, iako se primenjuju na ceo vaš Proton nalog, još su relevantnije kada je vaš Bitcoin Wallet integrisan u njega. Toplo preporučujem da ih primenite.


![Image](assets/fr/07.webp)


Da biste sačuvali svoju Mnemonic frazu, kliknite na "*Backup this Wallet's seed phrase*".


![Image](assets/fr/08.webp)


Unesite svoju Proton lozinku.


![Image](assets/fr/09.webp)


Zatim kliknite na "*View Wallet seed phrase*" da prikažete Mnemonic frazu vašeg Wallet.


![Image](assets/fr/10.webp)


Proton Wallet prikazuje vašu 12-rečnu Mnemonic frazu. **Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitkoinima**. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez pristupa vašem Proton nalogu. Ova 12-rečna fraza može se koristiti za vraćanje pristupa vašim bitkoinima ako izgubite pristup svom nalogu. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.


Možete to napisati na parčetu papira, ili za dodatnu sigurnost, preporučujem graviranje na bazi od nerđajućeg čelika kako biste ga zaštitili od požara, poplave ili urušavanja.


![Image](assets/fr/11.webp)


Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_Naravno, nikada ne bi trebalo da slikate ove reči, za razliku od onoga što radim u ovom vodiču._


Kliknite na dugme "*Done*" kada sačuvate svoju frazu.


![Image](assets/fr/12.webp)


## Otkrijte Interface


Proton Wallet-ov Interface je veoma intuitivan. Sa leve strane ćete pronaći različite novčanike i njihove povezane račune. "*Primarni*" račun je vaš glavni račun. Iz razloga poverljivosti, bitkoini primljeni putem Proton email-a Address su smešteni na poseban račun, nazvan "*Bitcoin putem Email-a*".


![Image](assets/fr/13.webp)


Da biste dodali novi nalog, kliknite na "*Dodaj nalog*".


![Image](assets/fr/14.webp)


Da biste kreirali novi Wallet, kliknite na simbol "*+*" pored "*Wallets*".


![Image](assets/fr/15.webp)


Ovo je mesto gde možete dodati BIP39 passphrase na novi Wallet.


![Image](assets/fr/16.webp)


Da biste produbili svoje znanje o passphrase, preporučujem ovaj vodič:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Primite bitkoine


Da biste primili bitkoine u vaš Wallet, izaberite željeni nalog sa leve strane Interface, zatim kliknite na dugme "*Receive*".


![Image](assets/fr/17.webp)


Proton Wallet zatim automatski generiše novi, prazni Address.


![Image](assets/fr/18.webp)


Jednom kada je transakcija završena, pronaći ćete je u odeljku "*Transakcije*". Kliknite na "*+Dodaj*" da biste dodelili oznaku transakciji.


![Image](assets/fr/19.webp)


## Pošalji bitkoine


Sada kada imate bitkoine u vašem Wallet, možete ih poslati. Izaberite nalog po vašem izboru na levoj strani Interface, zatim kliknite na "*Pošalji*".


![Image](assets/fr/20.webp)


Unesite primaoca Bitcoin Address. Možete skenirati QR kod klikom na mali logo. Da biste poslali na e-mail Address, unesite ga direktno u ovo polje. Kada unesete Bitcoin Address, kliknite na malu strelicu, a zatim na "*Potvrdi*".


![Image](assets/fr/21.webp)


Unesite iznos koji želite poslati, bilo u fiat valuti ili u bitkoinima, zatim kliknite na "*Pregled*".


![Image](assets/fr/22.webp)


Odaberite naknadu za transakciju na osnovu trenutne situacije na tržištu.


![Image](assets/fr/23.webp)


Dodajte oznaku svojoj transakciji, zatim dvaput proverite sve detalje. Ako je sve ispravno, kliknite na "*Potvrdi i pošalji*" da potpišete i pošaljete transakciju.


![Image](assets/fr/24.webp)


Vaša transakcija će se sada pojaviti na čekanju potvrde u odeljku "*Transakcije*" vašeg naloga.


![Image](assets/fr/25.webp)


## Prijavite se u aplikaciju


Pored veb klijenta, Proton Wallet je dostupan i putem mobilne aplikacije. Povezivanjem Wallet sa vašim Proton nalogom, možete sinhronizovati vaš Wallet između veb klijenta i mobilne aplikacije.


Preuzmite Proton Wallet iz vaše prodavnice aplikacija:




- [On the App Store](https://apps.apple.com/us/app/proton-Wallet-secure-btc/id6479609548);
- [Na Google Play Store](https://play.google.com/store/apps/details?id=me.proton.Wallet.android).


![Image](assets/fr/26.webp)


Nakon instalacije, kliknite na "*Log in*" i unesite svoj email Address i Proton lozinku.


![Image](assets/fr/27.webp)


Imaćete pristup vašem Bitcoin Wallet, sa istim funkcijama kao na web klijentu.


![Image](assets/fr/28.webp)


Čestitamo, sada znate kako da postavite i koristite Proton Wallet. Ako ste našli ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala što delite!


Da biste nastavili dalje, preporučujem ovaj vodič o Jade Plus, najnovijem Hardware Wallet kompanije Blockstream:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262