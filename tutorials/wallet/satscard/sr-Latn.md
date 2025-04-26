---
name: Satscard
description: Postavljanje i korišćenje Satscard sa Nunchuk
---
![cover](assets/cover.webp)


Bitcoin je elektronski sistem gotovine koji nam omogućava obavljanje transakcija od osobe do osobe. Međutim, da bismo bili uvereni da je transakcija nepromenljiva, potrebno je sačekati nekoliko potvrda (obično 6), kako bi se izbegao bilo kakav pokušaj dvostrukog trošenja od strane pošiljaoca. Ovo kašnjenje u validaciji ponekad može biti nezgodno, posebno kada se želi trenutna konačnost slična fizičkoj gotovini. Za razliku od gotovine, gde se posedovanje novčanice prenosi trenutno, Bitcoin transakcije uključuju vreme čekanja pre nego što se definitivno smatraju nepovratnim.


Ovo je mesto gde dolazi Satscard. Nudi metodu za omogućavanje fizičkog i trenutnog prenosa bitkoina, bez potrebe za obavljanjem On-Chain transakcije. Satscard funkcioniše kao kartica na donosioca koja omogućava siguran prenos Bitcoin Ownership, pružajući tako iskustvo bliže tradicionalnom novcu. U ovom vodiču, predstaviću vam ovo rešenje.


## Šta je Satscard?


Satscard od Coinkite-a je naslednik Opendime-a. To je NFC kartica koja omogućava fizički prenos bitcoina, slično kao novčanica ili kovanica. Za razliku od tradicionalnog Hardware Wallet, Satscard je kartica na donosioca, što znači da fizičko posedovanje kartice izjednačava sa Ownership bitcoina koji su osigurani ključevima pohranjenim na njoj. Njena cena se kreće između $6.99 i $17.99 u zavisnosti od odabranog dizajna.


![SATSCARD](assets/notext/01.webp)


Satscard čip je opremljen sa 10 slotova, što mu omogućava da skladišti bitkoine do 10 puta na 10 različitih adresa. Svaki slot funkcioniše nezavisno i teoretski bi trebalo da se koristi samo jednom za zaključavanje bitkoina u njemu. Da biste potrošili bitkoine, jednostavno otpečatite slot pomoću kompatibilne aplikacije, kao što je Nunchuk, unosom 6-cifrenog verifikacionog koda navedenog na poleđini Satscard-a.


Kartica osigurava da privatni ključ koji obezbeđuje bitkoine na Blockchain ne može biti zadržan od strane prethodnog vlasnika nakon što se fizički razdvoji od kartice. Primalac takođe može verifikovati validnost slota i iznos pohranjen u njemu u trenutku Exchange.


Ovaj sistem je posebno koristan za kupovinu fizičkih dobara sa bitkoinima, ili za davanje bitkoina kao poklon.


## Kako kupiti Satscard?


Satscard je dostupan za kupovinu [na zvaničnom Coinkite sajtu](https://store.coinkite.com/store/category/satscard). Da biste ga kupili u fizičkoj prodavnici, možete pronaći [listu sertifikovanih prodavaca](https://coinkite.com/resellers) na sajtu.

Trebaće vam i telefon kompatibilan sa NFC komunikacijama, ili USB uređaj za čitanje NFC kartica na standardnoj frekvenciji od 13,56 MHz.

## Kako učitati slot na Satscard?


Kada primite svoju Satscard, prvi korak je da proverite pakovanje kako biste se uverili da nije otvoreno. Ako je pakovanje oštećeno, to može ukazivati na to da je kartica kompromitovana i možda nije autentična.


Da biste upravljali Satscard-om, koristićemo mobilnu aplikaciju **Nunchuk Wallet**. Uverite se da je vaš pametni telefon kompatibilan sa NFC-om, zatim preuzmite Nunchuk sa [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073), ili direktno putem njegovog [`.apk` fajla](https://github.com/nunchuk-io/nunchuk-android/releases).


![SATSCARD](assets/notext/02.webp)


U teoriji, mogli biste direktno poslati bitkoine na Address naveden na poleđini vaše Satscard bez korišćenja Nunchuk-a. Međutim, savetujem da to ne radite, jer ćemo prvo proveriti da li je Address prvog slota zaista izveden iz privatnog ključa pohranjenog u Satscard i da nije lažni Address.


Ako koristite Nunchuk prvi put, aplikacija će vam ponuditi da kreirate nalog. Za potrebe ovog tutorijala, nije neophodno kreirati nalog. Dakle, izaberite "*Nastavi kao gost*" da nastavite bez naloga.


![SATSCARD](assets/notext/03.webp)


Zatim kliknite na "*Unassisted Wallet*".


![SATSCARD](assets/notext/04.webp)


Zatim kliknite na dugme "*Istražiću sam*".


![SATSCARD](assets/notext/05.webp)


Jednom kada se nađete na početnom ekranu Nunchuk-a, kliknite na "*NFC*" logo na vrhu ekrana.


![SATSCARD](assets/notext/06.webp)


Držite svoj Satscard na poleđini telefona da ga skenirate.


![SATSCARD](assets/notext/07.webp)


Nunchuk prikazuje prijemni Address koji odgovara prvom slotu vaše Satscard kartice. Obično bi ovaj Address trebao biti identičan onom ručno napisanom na poleđini vaše kartice. Kopirajte ovaj Address i koristite ga za prenos bitkoina koje želite zaključati u ovom slotu.


![SATSCARD](assets/notext/08.webp)


## Kako proveriti bitkoine na slotu?


Jednom kada je transakcija potvrđena, možete proveriti stanje povezano sa slotom vaše Satscard kartice skeniranjem pomoću Nunchuk-a. Tako, tokom transakcije, primalac bitkoina može odmah putem svoje Nunchuk aplikacije da verifikuje da kartica zaista sadrži bitkoine koji mu se duguju.


![SATSCARD](assets/notext/09.webp)

Ako druga strana nema Nunchuk aplikaciju, i dalje može proveriti validnost Satscard-a. Jednostavno aktivirajte NFC na svom pametnom telefonu i postavite Satscard na zadnju stranu uređaja. Ovo će automatski otvoriti Satscard veb-sajt u pregledaču, gde se može proveriti validnost kartice kao i iznos u bitkoinima povezan sa njom.

![SATSCARD](assets/notext/10.webp)


## Kako povući bitkoine sa slota?


Sada kada je prvi slot Satscard-a napunjen određenom količinom bitcoina, možete predati karticu primaocu uplate.


![SATSCARD](assets/notext/11.webp)


Ako ste primalac, potrebno je da instalirate Nunchuk. Kada uđete u aplikaciju, kliknite na "*NFC*" logo na vrhu ekrana.


![SATSCARD](assets/notext/12.webp)


Postavite svoj Satscard na zadnju stranu telefona.


![SATSCARD](assets/notext/13.webp)


Nunchuk će otkriti iznos osiguran na Address.


![SATSCARD](assets/notext/14.webp)


Da biste otpečatili privatni ključ i prebacili bitkoine na Address koji posedujete, kliknite na dugme "*Otpečati i prebaci saldo*".


![SATSCARD](assets/notext/15.webp)


Opcija "*Sweep to a Wallet*" omogućava vam da direktno pošaljete bitkoine na Wallet koji je već prisutan u vašoj Nunchuk aplikaciji. Da biste prebacili sredstva na drugi prijemni Address, izaberite "*Withdraw to an Address*".


![SATSCARD](assets/notext/16.webp)


Unesite primajući Address gde želite poslati bitkoine osigurane Satscard-om. Uverite se da je uneti Address tačan (ovo je jedini put kada ga možete proveriti), zatim kliknite na dugme "*Create transaction*".


![SATSCARD](assets/notext/17.webp)


Unesite PIN kod vaše Satscard kartice. Ovaj 6-cifreni kod je zabeležen na poleđini fizičke kartice.


![SATSCARD](assets/notext/18.webp)


Držite svoju Satscard na poleđini pametnog telefona dok potpisujete transakciju privatnim ključem pohranjenim na NFC kartici.


![SATSCARD](assets/notext/19.webp)


Vaša transakcija je sada potpisana i emitovana na Bitcoin mreži, što znači da je slot korišćen na vašoj Satscard kartici sada prazan.


![SATSCARD](assets/notext/20.webp)


## Kako ponovo koristiti Satscard?


Za razliku od jednokratnih rešenja kao što je Opendime, Satscard je opremljen čipom koji sadrži 10 nezavisnih slotova, omogućavajući do 10 operacija sa jednom karticom. Prvi slot, fabrički konfigurisan od strane Coinkite, odgovara prijemnom Address napisanom na poleđini vaše Satscard kartice.


![SATSCARD](assets/notext/21.webp)

Da biste aktivirali ostalih 9 slotova, potrebno je da generate par ključeva i Address putem aplikacije Nunchuk. Na početnoj stranici aplikacije, kliknite na "*NFC*" logo na vrhu ekrana.

![SATSCARD](assets/notext/22.webp)


Postavite svoj Satscard na zadnju stranu telefona.


![SATSCARD](assets/notext/23.webp)


Nunchuk ukazuje da nijedan slot nije aktivan na kartici, što je normalno jer je prvi već korišćen, a drugi još nije generisan. Da biste videli prethodno korišćene slotove, kliknite na "*View unsealed slots*". Strogo se savetuje da se ovi slotovi ne koriste ponovo, jer bi to dovelo do ponovne upotrebe Address što je štetno za vašu On-Chain privatnost. Stoga ćemo postaviti novi slot klikom na dugme "*Yes*".


![SATSCARD](assets/notext/24.webp)


Sada ćete morati da izaberete kako da generate vaš glavni lančani kod.


Slotovi na Satscard prate BIP32 standard, što znači da derivacija kriptografskih ključeva koji osiguravaju bitkoine ne zavisi od Mnemonic fraze kao u BIP39 novčanicima, već direktno od glavnog privatnog ključa i glavnog lanca koda. Ova dva Elements koriste se kao ulaz u HMAC-SHA512 funkciju za generate par ključeva deteta. Svaki slot ima svoj glavni ključ i svoj glavni lanac koda. Postoji samo jedan nivo derivacije za svaki slot.


Par ključeva za prvi slot unapred generiše Coinkite. Zato imate direktan pristup do njega putem Nunchuk-a, i zašto je primanje Address napisano na poleđini NFC kartice. Međutim, za ostale slotove, vi ste odgovorni za generisanje ključeva.


Glavni privatni ključ za svaki slot generiše direktno Satscard, a glavni lanci kodova moraju biti obezbeđeni spolja. Za lanac kodova vašeg novog slota, imate dve opcije: dozvolite Nunchuk generate da to uradi automatski odabirom "*Automatic*", ili ga kreirajte sami odabirom "*Advanced*" i unosom u predviđeni prostor. Da bi lanac kodova bio efikasan, potrebno je da bude što je moguće nasumičniji.


![SATSCARD](assets/notext/25.webp)


Unesite 6-cifreni PIN naveden na poleđini Satscard kartice.


![SATSCARD](assets/notext/26.webp)


Postavite svoj Satscard na zadnju stranu telefona.


![SATSCARD](assets/notext/27.webp)


Novi slot je uspešno konfigurisan. Sada možete videti prijemni Address za deponovanje bitkoina. Da biste nastavili sa učitavanjem, pratite uputstva u odeljku "*Kako učitati slot na Satscard?*" ovog tutorijala.

Ovaj proces možete ponoviti do 10 puta na svakoj Satscard kartici.


Čestitamo, sada ste u toku sa korišćenjem Satscard-a! Ako vam je ovaj vodič bio od pomoći, bio bih zahvalan ako biste mogli ostaviti palac gore ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!