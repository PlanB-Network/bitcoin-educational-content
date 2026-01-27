---
name: Ashigaru - Stowaway
description: Kako da napravim Payjoin transakciju na Ashigaru?
---
![cover](assets/cover.webp)



> *Primorajte špijune blockchaina da preispitaju sve što misle da znaju.*

Payjoin je Bitcoin struktura transakcije dizajnirana da poboljša poverljivost korisnika uključivanjem direktne saradnje sa primaocem plaćanja. Postoji nekoliko implementacija koje olakšavaju njenu primenu i automatizuju proces. Najpoznatija od njih je nesumnjivo Stowaway, koju je prvobitno razvio Samurai Wallet tim, a sada je integrisana u njegov fork Ashigaru.



## Kako funkcioniše Stowaway?



Kao što je ranije pomenuto, Ashigaru integriše PayJoin alat pod nazivom `Stowaway`. Ovo je dostupno u Ashigaru aplikaciji na Androidu. Da bi se izvršio Payjoin, primalac (koji takođe preuzima ulogu saradnika) mora koristiti softver kompatibilan sa Stowaway-om, tj. trenutno samo Ashigaru.



Stowaway je zasnovan na kategoriji transakcija koje su Samuraji nazivali "Cahoots". Cahoot je kolaborativna transakcija između nekoliko korisnika, koja uključuje razmenu informacija izvan Bitcoin blockchaina. Ashigaru trenutno nudi dva Cahoots alata: Stowaway (Payjoins) i StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Transakcije u dosluhu zahtevaju razmenu delimično potpisanih transakcija između korisnika. Ovaj proces može biti dug i zamoran, posebno kada se obavlja na daljinu. Međutim, i dalje je moguće to uraditi ručno, ako su saradnici na istoj lokaciji. U konkretnom smislu, to podrazumeva skeniranje pet QR kodova uzastopno, razmenjenih između dva učesnika.



Na daljinu, ovaj metod postaje previše složen. Da bi to rešio, Samourai je razvio protokol za šifrovanu komunikaciju zasnovan na Tor-u pod nazivom "*Soroban*". Zahvaljujući Sorobanu, razmene potrebne za Payjoin su automatizovane i odvijaju se u pozadini.



Ove šifrovane komunikacije zahtevaju vezu i autentifikaciju između Cahoot učesnika. Zato se Soroban oslanja na korisničke Paynyms. Ako još niste upoznati sa načinom na koji Paynyms funkcionišu, pogledajte ovaj posvećeni vodič da saznate više:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Ukratko, Paynym je jedinstveni identifikator povezan sa vašim wallet, omogućavajući vam aktivaciju raznih funkcija, uključujući šifrovane razmene. Ima oblik identifikatora praćenog ilustracijom. Evo, na primer, onaj koji ja koristim na Testnet:



![Image](assets/fr/01.webp)



**Da sumiramo:**





- payjoin" = Specifična struktura kolaborativne transakcije;





- `Stowaway` = Implementacija Payjoin dostupna na Ashigaru ;





- `Cahoots` = Ime koje je Samourai dao svim njihovim vrstama kolaborativnih transakcija, posebno Payjoin `Stowaway`, preuzet danas na Ashigaru ;





- soroban = Šifrovani komunikacioni protokol uspostavljen na Toru koji omogućava saradnju sa drugim korisnicima u `Cahoots` transakciji;





- paynym" = Jedinstveni wallet identifikator koji se koristi za uspostavljanje komunikacije sa drugim korisnikom na "Soroban", kako bi se izvršila "Chahoots" transakcija.



Za detaljniji pregled kako Payjoins funkcionišu i njihovu korisnost u onchain privatnosti, preporučujem ovaj drugi vodič:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Kako da uspostavim vezu između Paynyms?



Da biste započeli, naravno, trebaće da instalirate Ashigaru i kreirate :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Da biste izvršili udaljenu Cahoots transakciju, uključujući PayJoin (*Stowaway*) putem Ashigaru, prvo morate "pratiti" korisnika s kojim želite sarađivati, koristeći njihov Paynym. U slučaju Stowaway-a, to znači pratiti osobu kojoj želite poslati bitkoine. Ako još ne znate kako pratiti drugi Paynym, detaljnu proceduru ćete pronaći u ovom vodiču:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Kako da napravim Payjoin na Ashigaru?



Da biste izvršili Stowaway transakciju, kliknite na sliku vašeg Paynyma u gornjem levom uglu ekrana, a zatim otvorite meni `Collaborate`. Osoba koja učestvuje u transakciji sa vama mora učiniti isto, osim ako ne razmenjujete QR kodove lično.



![Image](assets/fr/02.webp)



Imate dve opcije: izaberite `Initiate` ako ste pošiljalac uplate, ili `Participate` ako ste primalac ovog payjoin-a.



![Image](assets/fr/03.webp)



Ako ste primalac, procedura je veoma jednostavna. Za daljinsku saradnju putem Soroban mreže, kliknite na `Participate`, izaberite nalog koji želite da koristite, zatim pritisnite `LISTEN FOR CAHOOTS REQUESTS` da biste sačekali zahtev koji šalje platiša.



![Image](assets/fr/04.webp)



S druge strane, za ličnu saradnju putem skeniranja QR koda, idite na početnu stranicu vašeg wallet, pritisnite ikonu QR koda na vrhu ekrana, a zatim skenirajte QR kod koji je obezbedio platiša koji inicira transakciju.



![Image](assets/fr/05.webp)



Ako ste u ulozi platioca, tj. onoga koji inicira transakciju, idite na meni `Collaborate`, zatim izaberite `Initiate`.



![Image](assets/fr/06.webp)



Za tip transakcije, pošto želimo da napravimo Payjoin Stowaway, izaberite ovu opciju.



![Image](assets/fr/07.webp)



Zatim možete birati između online saradnje (*Cahoots* putem *Soroban*) ili saradnje licem u lice, uz razmenu QR kodova.



![Image](assets/fr/08.webp)



### Cahoots online



Ako ste izabrali opciju `Online`, onda izaberite primaoca iz Paynyms koje pratite.



![Image](assets/fr/09.webp)



Kliknite na `Set up transaction`, zatim izaberite račun sa kojeg želite izvršiti trošak.



![Image](assets/fr/10.webp)



Na sledećoj stranici unesite detalje transakcije: iznos koji se šalje primaocu i stopu naplate. Nema potrebe unositi adresu primaoca, jer će je primalac sam preneti tokom PSBT razmena.



Zatim kliknite na `Review transaction setup`.



![Image](assets/fr/11.webp)



Proverite informacije pažljivo, uverite se da vaš saradnik sluša zahteve *Cahoots*, zatim kliknite na zeleni taster `BEGIN TRANSACTION` da biste započeli razmenu PSBT-ova putem Sorobana.



![Image](assets/fr/12.webp)



Sačekajte dok oba učesnika ne potpišu transakciju, zatim je emitujte na Bitcoin mreži.



![Image](assets/fr/13.webp)



### Razgovori licem u lice



Ako želite da obavite razmenu lično, izaberite tip transakcije `STONEWALL X2`, zatim odaberite opciju `In Person / Manual`.



![Image](assets/fr/14.webp)



Kliknite na `Set up transaction`, zatim izaberite račun sa kojeg želite izvršiti trošak.



![Image](assets/fr/15.webp)



Na sledećoj stranici unesite detalje transakcije: iznos koji se šalje primaocu i stopu naplate. Nema potrebe unositi adresu za prijem, jer će primalac sam preneti tokom PSBT razmene.



Zatim kliknite na `Review transaction setup`.



![Image](assets/fr/16.webp)



Proverite detalje, zatim pritisnite zeleni taster `BEGIN TRANSACTION` da započnete razmenu PSBT-ova putem skeniranja QR koda.



![Image](assets/fr/17.webp)



Razmena se vrši naizmeničnim skeniranjem sa saradnikom: kliknite na `PRIKAŽI QR KOD` da prikažete vaš QR kod saradniku, koji će ga skenirati. On će zatim kliknuti na `PRIKAŽI QR KOD` da prikaže svoj, a vi ćete ga skenirati pomoću `POKRENI QR Skeniranje`. Ponavljajte ovaj proces dok svih pet koraka razmene ne bude završeno.



![Image](assets/fr/18.webp)



Kada su sve razmene završene, proverite detalje transakcije, zatim je oslobodite povlačenjem zelene strelice na dnu ekrana.



![Image](assets/fr/19.webp)



[Transakcija je objavljena](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Njena struktura je sledeća:



![Image](assets/fr/20.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Ako analiziramo ovu transakciju, vidimo moj UTXO od `164,211 sats` na ulaznoj strani, kao i UTXO od `190,002 sats` koji pripada stvarnom primaocu uplate. Na izlaznoj strani, dobijam razmenu UTXO od `63,995 sats`, dok primalac dobija UTXO od `290,002 sats`. Upoređujući ulaze i izlaze, možemo videti da je primalac zaista zaradio `100,000 sats`, što odgovara iznosu moje stvarne uplate, i da sam ja izgubio `100,000 sats`, na šta sam dodao troškove mining.



Očigledno, mogu opisati ovu strukturu jer sam sam izgradio transakciju. Ali za spoljnog posmatrača, generalno je nemoguće odrediti koji UTXO-i pripadaju kojem učesniku, bilo u ulazima ili izlazima.



Da biste produbili svoje znanje o upravljanju privatnošću na lancu na Bitcoin, preporučujem da pohađate moju obuku BTC 204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c