---
name: Nunchuk
description: Wallet mobilni pogodan za sve
---
![cover](assets/cover.webp)



## Moćan Wallet


Nunchuk je stigao krajem 2020. godine sa jasnom filozofijom: učiniti multi-potpis standardom. Stoga je dizajniran da obavlja veoma napredne funkcije, sa vrednim izborom da se dizajn direktno izgradi na Bitcoin Core, referentnom softveru za Bitcoin ekosistem.



Nakon više od 4 godine razvoja i korišćenja, spreman je za isprobavanje u većem obimu. Ako ste početnik i niste upoznati sa Nunchuk-om, ovaj vodič će vam pomoći da napravite prve korake i otkrijete ovaj softver, čije ćete napredne funkcije moći da naučite nakon što pređete prvi utisak. Sam tutorijal je posvećen korisnicima srednjeg nivoa koji poseduju potrebne veštine da prate sve korake, ali može biti inspiracija za svakoga da sazna kako da unapredi veštine. Počećemo sa mobilnom verzijom, i ovo isticanje je neophodno, jer Nunchuk ima softver koji može da radi i na računarima.



## Preuzmi


Prvi korak je definitivno odlučiti gde preuzeti aplikaciju. Idite na [zvanični sajt](https://nunchuk.io/) gde možete pronaći neku dokumentaciju (ne mnogo, ali je početak), prezentaciju funkcija, kao i, pri kraju stranice, sve linkove za preuzimanje.



📌 Za ovaj tutorijal odlučio sam da vam pokažem kako da preuzmete Software Wallet iz Github repozitorijuma i kako da verifikujete izdanje pre nego što ga instalirate na vaš mobilni telefon. **Sledeći postupak se može uraditi samo sa vašeg računara**, tako da vam preporučujem da sve ove korake uradite sa vašeg desktopa ili laptopa i - nakon svih verifikacija - prenesete `.apk` fajl na vaš mobilni telefon.



![image](assets/en/01.webp)



Ako vaše veštine nisu veoma napredne, možete odlučiti da preuzmete `.apk` sa zvaničnih prodavnica i preskočite direktno na deo za konfiguraciju ovog vodiča. Ako, s druge strane, želite da napravite iskorak, nastavite da pratite korak po korak.



Dakle, sa svog desktop računara kliknite _Visit our open source repository_



Link će vas odvesti na Nunchukovu Github stranicu, gde ćete pronaći brojne repozitorijume. Fokusiraćemo se na _nunchuk-android_.



![image](assets/en/02.webp)



Na sledećem ekranu, pronađite sa desne strane odeljak _Releases_ i izaberite _Latest_



![image](assets/en/03.webp)



Pod _Assets_, preuzmite izdanje (u ovom primeru 1.67.apk), zajedno sa datotekama SHA256SUMS i SHA256SUMS.asc.



![image](assets/en/04.webp)



Da biste pronašli GPG ključ programera, vratite se na odeljak _Releases_ u repozitorijumu i potražite verziju 1.9.53 (ili raniju) koja sadrži link za preuzimanje _GPG Key_



![image](assets/en/05.webp)



Nastavićemo sa verifikacijom putem praktičnog alata koji nudi Sparrow wallet, koji ima posvećen prozor za ovu svrhu i podržava PGP potpise i SHA256 manifeste.



Zatim pokrenite Sparrow i iz menija _Tools_ izaberite _Verify Download_.



![image](assets/en/06.webp)



U prozoru koji se pojavi, pronaći ćete polja za "popunjavanje": izaberite dugme _Browse_ sa desne strane i odaberite, za svako polje, odgovarajuće datoteke koje ste upravo preuzeli sa Github-a. Kada završite sve korake, prozor će izgledati kao što sledi, sa Green oznakama i Hash potvrdom manifesta.



![image](assets/en/07.webp)


**N.B. snimak ekrana je sa Windows računara, ista praksa se može koristiti za bilo koji operativni sistem na vašem računaru, samo instalirajte Sparrow wallet. I verifikujte!**



Možete pronaći vodič za Sparrow wallet da preuzmete ovaj Software Wallet


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Možete zatim preneti `.apk` datoteku sa svog računara na telefon.



![image](assets/en/08.webp)



i instalirajte Nunchuk



![image](assets/en/09.webp)



Pre nego što pokrenete Nunchuk na svom telefonu, otvorite Orbot i stavite pridošlicu na listu aplikacija koje će biti usmerene preko Tor-a.



![image](assets/en/11.webp)



Sada pokrenite Nunchuk. Za funkcije projekta-koje nisu predmet ovog tutorijala-Nunchuk, kada se otvori, pozvaće vas da se prijavite putem email-a ili Google profila. Dok ne planirate da iskoristite napredne planove Nunchuk Inc, **izbegavajte prijavljivanje** i nastavite odabirom opcije _Nastavi kao gost_.



![image](assets/en/12.webp)



## Postavke


Nunchuk se predstavlja sa prozorom prezentacije _Home_, gde je lako razumeti njegovu operativnu filozofiju o kojoj ćemo detaljnije govoriti za trenutak.



Na dnu možete pronaći menije, i kao prvi korak, izaberite _Profil_ da pristupite podešavanjima.



![image](assets/en/10.webp)



Zatim izaberite _Postavke prikaza_, nastavljajući da ignorišete poziv za kreiranje naloga.



![image](assets/en/14.webp)



Na ekranu ispod možete proveriti da li je Wallet online i možete povezati svoj server, pažljivo prateći uputstva na linku koji se nudi klikom na _ovaj vodič_.



![image](assets/en/15.webp)



Sačuvaj postavke komandom _Save network settings_, vrati se u meni _Profile_ i izaberi _Security settings_.



![image](assets/en/16.webp)



Iz ovog menija podešavate kako da zaštitite otvaranje aplikacije. Da biste sprečili neželjeni pristup, možete zaštititi Nunchuk telefonskom biometrijom i/ili dodati sigurnosni PIN.



![image](assets/en/17.webp)



Takođe pogledajte meni _About_, koji ćete uvek pronaći u prozoru _Profile_



![image](assets/en/18.webp)



što će vam omogućiti da proverite verziju aplikacije ili da kontaktirate programere ako je potrebno.



![image](assets/en/19.webp)



## Generisanje Ključeva i Wallet


Kao što je lako pretpostaviti iz Nunchukove filozofije, softver je zamišljen kao koristan alat za upravljanje Wallets sa više potpisa. Da bi obavljao ovu funkciju, Nunchuk omogućava kreiranje Wallet odvajanjem od ključeva potrebnih za organizovanje digitalnih potpisa.



Zapravo, idealno funkcionisanje Nunchuk-a uključuje kreiranje Novčanika koji mogu biti samo za gledanje, zavisni od ključeva koji mogu biti "Colds."



Na prethodnim ekranima možda ste primetili da postoji meni na dnu pod nazivom _Keys_. Ako ste upravo preuzeli Nunchuk, u oba _Home_ i _Keys_ videćete veliko dugme koje vas poziva da dodate ključ, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Ovo je upravo kako Nunchuk funkcioniše:** prvo generate/importujete ključeve, a zatim kreirate Wallet, konfigurišući ga da izabere koji ključevi će autorizovati otključavanje sredstava pohranjenih na njemu.



Čak i u slučaju Wallet singlesig, prvo kreirate ključ, a tek onda Wallet. I to je tačno ono što ćemo sada uraditi, počevši sa Wallet singlesig da probijemo led i otkrijemo funkcije Nunchuk-a.



Kliknite _Dodaj ključ_



![image](assets/en/22.webp)



Nunchuk prikazuje brojne podržane uređaje za potpisivanje, ali za početak odaberite _Software_.



![image](assets/en/23.webp)



Nunchuk će generate Mnemonic koji će biti sačuvan na uređaju. Zatim treba da zapišete redosled reči za rezervnu kopiju, stvarajući najbolje uslove okoline i osiguravajući da imate vremena da to uradite dobro i tiho. Softver prikazuje Mnemonic samo jednom, bilo da odlučite da ga prikažete sada ili kasnije, zato izaberite _Kreiraj i sačuvaj sada_.



![image](assets/en/24.webp)



Nunchuk generiše 24-rečenice Mnemonic reči, koje se odmah pojavljuju na sledećem ekranu.



![image](assets/en/25.webp)



a zatim je nastavio sa brzim proveravanjem, tražeći od vas da izaberete tačnu reč, od 3 ponuđene opcije, koja odgovara broju u Mnemonic sekvenci.


Ako ste pravilno napisali Mnemonic, dugme _Nastavi_ postaje operativno. Pritisnite ga da biste nastavili.



![image](assets/en/26.webp)



Imenujte svoj ključ i pritisnite _Nastavi_.



![image](assets/en/27.webp)



Na kraju ovih koraka, bićete upitani da li želite da dodate [passphrase](https://planb.academy/en/resources/glossary/passphrase-bip39) svojoj Mnemonic frazi. Ako nemate potrebno znanje o tome kako koristiti passphrase, kako napraviti njegovu rezervnu kopiju ili kako funkcioniše, preporučujem da izaberete _Ne treba mi lozinka_.



![image](assets/en/28.webp)



Ključ je konačno kreiran i prikazan vam je u meniju:




- Sa _Key Spec_ je naznačen glavni otisak prsta
- Imate postavke, tri tačke u gornjem desnom uglu, gde možete obrisati ključ ili potpisati poruku
- Pored imena ključa naći ćete ikonu pera, klikom na koju možete urediti ime Ključa, na primer da biste u budućnosti držali ključeve u redu.
- Kao poslednju komandu, možete proveriti status zdravlja ključa: pritiskom na _Pokreni proveru zdravlja_ možete omogućiti aplikaciji da proveri da li je ključ kompromitovan.



Kada si dobar, klikni _Done_



![image](assets/en/29.webp)



U meniju _Keys_ videćete kako se pojavljuje vaš prvi ključ.



![image](assets/en/30.webp)



Idite na meni _Home_, pojavljuje se opcija za kreiranje Wallet. Kliknite _Create new wallet_.



![image](assets/en/31.webp)



Nunchuk vam pokazuje niz mogućnosti koje se uglavnom odnose na usluge koje kompanija nudi, a koje nisu predmet ovog vodiča.



U ovom vodiču ćemo kreirati _Hot Wallet i _Custom wallet_ detaljno opisujući detalje.


Hajde da počnemo sa _Prilagođeni novčanik_.



![image](assets/en/32.webp)



Na jednostavan način, aplikacija će vas zamoliti da imenujete ovaj novi Wallet i izaberete skriptu za adrese. Za tutorijal sam odlučio da ostavim podrazumevano podešavanje, _Native segwit_. Kada završite, izaberite _Continue_



![image](assets/en/33.webp)



Konfiguracija Wallet nastavlja da vas pita da postavite kojim ključem će sredstva ovog Wallet biti otključana. Ukoliko postoji više ključeva, biće vam prikazana lista sa koje možete izabrati. Mi smo za sada kreirali samo jedan, tako da biramo da stavimo oznaku na taj. U donjem desnom uglu možete videti kako će vas Nunchuk pitati da postavite vaše buduće Wallet multi-potpise, povećavajući broj _Potrebnih ključeva_.



![image](assets/en/34.webp)



Pošto kreiramo singlesig, ostavljamo `1` i kliknemo na _Continue_.



Na kraju se pojavljuje ekran za verifikaciju, gde možete proveriti karakteristike Wallet:




- ime
- `1/1 Multisig` oznaka, što je način na koji Nunchuk imenuje Wallet singlesig
- `Native SegWit`
- ključ `Keys`, sa svojim otiskom prsta i putanjom derivacije



Kada budete zadovoljni, pritisnite _Create wallet_



![image](assets/en/35.webp)



Wallet je kreiran i možete preuzeti [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) datoteku kao rezervnu kopiju. Da biste se vratili na glavni meni, kliknite strelicu u gornjem levom uglu.



![image](assets/en/36.webp)



Nalazite se u _Home_, gde vam je prikazan novokreirani Wallet koji izveštava o stanju bilansa i statusu konekcije. Klikom na plavi prostor možete pristupiti glavnim funkcijama Wallet.



![image](assets/en/37.webp)





- Ikonica sočiva u gornjem desnom uglu omogućava vam pretragu transakcija;
- `View Wallet config` daje pristup meniju za konfiguraciju, gde možete urediti ime Wallet i omogućiti napredne opcije, gore desno (od kojih ne možete napraviti snimke ekrana). Ovde možete izvesti konfiguraciju Wallet, oznake, zameniti ključeve, promeniti [gap limit](https://planb.academy/en/resources/glossary/gap-limit) i još mnogo toga.



## Transakcije sa Nunchuk



Nagrade _Primi_



![image](assets/en/38.webp)



Aplikacija je programirana da prikaže QR kod Address ili kopira/deli scriptPubKey za primanje sredstava na lancu.



![image](assets/en/39.webp)



Imali smo UTXO koji je stigao na ovaj prvi Address,



![image](assets/en/40.webp)



ali i dalje kliknemo na _Receive_ da primimo još jedan.



![image](assets/en/41.webp)



Svrha je da otkrijete da vam Nunchuk prijavljuje ovaj novi Address kao _Nekorišćena adresa_, ali vam takođe pokazuje da imate _Korišćene adrese_ i njihov broj.



### Trošenje transakcije sa kontrolom novčića



Kada stigne i ovaj drugi UTXO, vratite se na glavni ekran Wallet da proverite status dve dolazne transakcije i, što je najvažnije, kliknite na opciju _View coins_



![image](assets/en/42.webp)



gde će vam biti prikazani pojedinačni UTXO-i. Ovde možete izabrati da pogledate jedan posebno klikom na malu strelicu pored iznosa



![image](assets/en/43.webp)



i proverite kada je stiglo, opis, blokirajte UTXO kako se ne bi potrošilo i više.



![image](assets/en/44.webp)



Ali ako se vratite na meni _Coins_ klikom na strelicu u gornjem desnom uglu, možete uključiti "Coin Control" da trošite svoje UTXO-e na kontrolisaniji način.



U sledećem primeru, odlučio sam da izaberem UTXO od 21,000 Sats i zatim kliknem na simbol u donjem levom uglu.



![image](assets/en/45.webp)



Nunchuk automatski otvara prozor _Nova transakcija_ za trošenje ovog UTXO. U transakciji trošenja, prvo morate ručno postaviti iznos ili odabrati _Pošalji sve odabrano_ da biste poslali celokupni saldo kontrole novčića, bez generisanja ostataka. Kada je iznos postavljen, izaberite _Nastavi_



![image](assets/en/46.webp)



Sada Nunchuk pokazuje gde da nalepite Address na koji treba preneti ova sredstva, detaljno opišite opis i završite transakciju.



![image](assets/en/47.webp)



Odabirom opcije _Create transaction_ automatsko upravljanje naknadama i transakcijama prepušta se aplikaciji. Preporučujem odabir opcije _Custom transaction_ za veću kontrolu.



Na ovom novom ekranu važno je odabrati




- _Oduzmi naknadu od iznosa za slanje_, kako bi se sprečilo da naknade budu plaćene od strane drugog UTXO prisutnog u Wallet, trošeći ga i generišući ostatak (što je izbegljiv gubitak privatnosti);
- i onda ručno postavite naknade nakon provere na exploreru.



Kada završite sve ove korake, kliknite na _Continue_



![image](assets/en/48.webp)



Sledeći ekran je potpuni rezime transakcije. Ako je sve u redu, potvrdite izborom _Potvrdi i kreiraj transakciju_.



![image](assets/en/49.webp)



Sa _Pending signatures_ Nunchuk vas obaveštava da transakcija čeka vaš potpis za odobrenje troška, koji dodajete klikom na _Sign_.



![image](assets/en/50.webp)



Komanda _Broadcast_ pojavljuje se na dnu kako bi propagirala finalizovanu i potpisanu transakciju.



![image](assets/en/51.webp)



### Transakcija trošenja iz menija _Pošalji_



Dok smo na glavnoj stranici Wallet vidimo da transakcija izlazi i čeka potvrdu, koristimo meni _Send_ da simuliramo dnevni trošak.



![image](assets/en/52.webp)



Klikom na _Pošalji_, zapravo se pojavljuje ekran za slanje transakcije, koji je isti kao onaj upravo viđen, ali bez prolaska kroz kontrolu novčića.



Takođe, u ovom drugom primeru odlučio sam da izaberem _Custom transaction_ i pošaljem ceo iznos, ali sam mogao da ga podesim ručno. Kada odlučite o iznosu za slanje, pritisnite _Continue_.



![image](assets/en/53.webp)



Zatim uvek napravite slučaj da li su naknade oduzete iz UTXO u pitanju (u ovom primeru izbor je prisilan, jer postoji samo jedan), ručno prilagodite naknade prema situaciji u to vreme u Mempool, i pritisnite _Nastavi_.



![image](assets/en/54.webp)



Ako je ekran sažetka zadovoljavajući, izaberite _Potvrdi i kreiraj transakciju_.



![image](assets/en/55.webp)



Potpiši transakciju sa _Sign_



![image](assets/en/56.webp)



i propagirajte ga na mrežu.



![image](assets/en/57.webp)



Wallet je u ovom trenutku sa saldom na nuli i istorijom koja se ažurira.



![image](assets/en/58.webp)



## Kreiranje "Hot Wallet"



Poslednje, i da ne izostavimo ništa iz početnih faza Nunchuk mobilnog, hajde da vidimo kako ovo stvara ono što aplikacija naziva "Hot Wallet."



U meniju _Home_ u Nunchuk-u, gde se pojavljuje lista Novčanika, kliknite na `+` u gornjem desnom uglu.



![image](assets/en/59.webp)



Izaberite _Hot wallet_ iz opcija



![image](assets/en/60.webp)



Nunchuk daje nekoliko saveta o rukovanju Hot novčanicima na stranici za prezentaciju, gde ćete odabrati _Continue_ da nastavite.



![image](assets/en/61.webp)



Nakon nekoliko trenutaka Wallet je kreiran i pojavljuje se na listi u braon boji. Ovo je boja kojom vas Nunchuk upozorava da još niste napravili rezervnu kopiju Wallet.



![image](assets/en/62.webp)



Kliknite na ime Wallet, da biste pristupili njegovim konfiguracijama, i možda ćete primetiti poziv da odmah napravite rezervnu kopiju fraze Mnemonic.



![image](assets/en/63.webp)



Postupak je isti kao što smo već videli, tako da se nećemo ponovo zadržavati na njemu. Kada bude gotov, Nunchuk će vas odvesti na odgovarajuću stranicu ključa, koju možete urediti kao onu koju ste kreirali pomoću _Custom_ postupka.



![image](assets/en/64.webp)



Takođe pokušajte _Pokreni proveru zdravlja_



![image](assets/en/65.webp)



ili da vidite kako da prikažete sve svoje Novčanike na _Početnoj_ aplikacije.



![image](assets/en/66.webp)



## Da imate na umu da nastavite samostalno


Baš kao što postoji redosled za kreiranje, to jest, prvo generisanje ključeva, a zatim Wallet, biće potrebno da održavate obrnut redosled za brisanje ovih stavki iz vaše aplikacije.



Ako imate potrebu da obrišete jedan od ključeva, prvo treba da imate predviđanje da obrišete Wallet, ili Novčanike, koji koriste jedan od ključeva za potpisivanje transakcija: prvo obrišete Novčanike i tek onda ključeve. Ako ne sledite ovaj redosled, nećete biti u mogućnosti da uklonite ključ.



Sada kada znate kako da počnete sa Nunchuk-om, možete nastaviti da proučavate ovu aplikaciju i otkrivate njene tajne. U ovom vodiču smo napravili samo prve korake, ali postoje sofisticiranije primene i napredne potrebe koje ovaj Software Wallet može da vam pomogne da ispunite.