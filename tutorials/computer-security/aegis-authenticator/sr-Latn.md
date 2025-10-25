---
name: Aegis Authenticator
description: Kako možete koristiti Aegis Authenticator za zaštitu svojih naloga dvofaktorskom autentifikacijom?
---

![cover](assets/cover.webp)



Danas je dvofaktorska autentifikacija (2FA) ključna za zaštitu online naloga. Pored lozinke, dodaje drugi faktor (često 6-cifreni kod) koji ističe nakon 30 sekundi, što hakerima znatno otežava posao. Korišćenje posvećene TOTP (*Time-based One-Time Password*) aplikacije je sigurnije od SMS-a, koji može biti ugrožen napadima zamene SIM kartice.



Međutim, nisu sve aplikacije za autentifikaciju jednake. Mnoge vlasničke solucije (Google Authenticator, Authy, itd.) predstavljaju probleme: one su vlasničke i zatvorenog koda (nemoguće je proveriti njihovu sigurnost), ponekad integrišu reklamne trackere, ne nude šifrovanu rezervnu kopiju vaših kodova, a mogu čak i sprečiti izvoz vaših naloga kako bi vas zaključale u njihov ekosistem.



S druge strane, Aegis Authenticator se predstavlja kao besplatna i etička alternativa ovim aplikacijama. Aegis je besplatna, sigurna, open-source aplikacija za upravljanje vašim tokenima za dvostepenu verifikaciju na Androidu. Njegov razvoj se fokusira na osnovne funkcije koje druge aplikacije ne nude, uključujući robusnu enkripciju lokalnih podataka i mogućnost sigurnih rezervnih kopija. Sve u svemu, Aegis nudi lokalno, proverljivo rešenje za dvostruku autentifikaciju, idealno za svakoga ko želi da zadrži potpunu kontrolu nad svojim 2FA kodovima.



## Predstavljamo Aegis Authenticator



Aegis Authenticator je aplikacija otvorenog koda za 2FA za Android, objavljena pod GPL v3 licencom. Izdvaja se svojom filozofijom "privatnost po dizajnu": aplikacija radi potpuno offline i ne zahteva vezu sa udaljenim servisom. Kao rezultat toga, vaši tokeni ostaju uskladišteni lokalno na vašem uređaju, u sigurnom sefu čiji ključ posedujete samo vi.



### Ključne karakteristike



**Šifrovani trezor:** svi vaši OTP kodovi su sačuvani u AES-256 šifrovanom trezoru (GCM režim), zaštićenom glavnom lozinkom koju definiše korisnik. Ovaj trezor možete otključati putem lozinke ili biometrijskih podataka (otisci prstiju, prepoznavanje lica) radi dodatne pogodnosti. U nedostatku lozinke, podaci bi bili nešifrovani - stoga vam snažno preporučujemo da postavite lozinku.



**Napredna organizacija:** Aegis drži vaše brojne 2FA naloge dobro organizovanim. Možete sortirati unose abecednim redom ili po željenom redosledu, grupisati ih po kategorijama (npr. Lično, Posao, Društveno) radi lakšeg pronalaženja, i dodeliti svakom unosu personalizovanu ikonu. Uključena je traka za pretragu kako biste odmah pronašli uslugu ili nalog po imenu.



**Šifrovane lokalne rezervne kopije:** Da biste osigurali da nikada ne izgubite pristup svojim nalozima, Aegis nudi automatske rezervne kopije vašeg sefa. One su šifrovane (putem lozinke) i mogu se sačuvati na lokaciji po vašem izboru (interna memorija, cloud folder, itd.). Aplikacija takođe može ručno izvesti bazu podataka vaših naloga, u šifrovanom ili nešifrovanom formatu prema potrebi. Uvoz naloga iz drugih 2FA aplikacija je jednako jednostavan (Aegis podržava uvoz iz Authy, Google Authenticator, FreeOTP, andOTP, itd.).



**Security and privacy:** aplikacija je potpuno van mreže po defaultu. Ne zahteva mrežne dozvole - što znači da ne prenosi podatke spoljašnjem svetu, i ne sadrži module za praćenje oglasa ili analizu ponašanja. Aegis ne prikazuje oglase i ne zahteva korisnički nalog: čim je instalirana, radi bez registracije. Kako je njen izvorni kod javan na GitHub-u, zajednica može slobodno da ga proveri, garantujući odsustvo zlonamernih ili skrivenih funkcionalnosti.



**Moderni Interface:** Aegis usvaja uredan Material Design, sa podrškom za tamnu temu (uključujući AMOLED režim) i čak opcionalni prikaz pločica za prikaz vaših kodova kao mreža. Interface je čist, bez suvišnih detalja, i sprečava snimanje ekrana kodova kao meru bezbednosti.



## Instalacija



Kako je Aegis Authenticator otvorenog koda, njegovi programeri preferiraju kanale distribucije koji poštuju privatnost. Postoje dva glavna načina za instalaciju:



### Preko F-Droid (preporučeno)



Najbezbedniji i najlakši način je putem F-Droid-a, besplatne alternativne prodavnice. Ako F-Droid još nije instaliran na vašem telefonu, počnite tako što ćete ga preuzeti sa zvaničnog sajta [F-Droid.org](https://f-droid.org). Zatim :





- Otvorite F-Droid i proverite da li ste ažurirali svoje repozitorijume kako biste dobili najnoviji spisak aplikacija.
- Pretraži "Aegis Authenticator" u F-Droid. Zvanična aplikacija bi trebalo da se pojavi (izdavač: Beem Development)
- Pokrenite instalaciju pritiskom na Instaliraj. Kako je Aegis jedna od aplikacija verifikovanih od strane F-Droid-a, imate koristi od pouzdanog i sigurnog preuzimanja.



Instalacija putem F-Droid-a nudi prednost automatskog ažuriranja aplikacija čim budu objavljene. Štaviše, F-Droid garantuje da je aplikacija bez neželjenih vlasničkih komponenti.



### Preko GitHub-a (potpisani APK)



Ako više volite da instalirate aplikaciju bez korišćenja prodavnice, možete preuzeti zvanični APK direktno sa GitHub stranice projekta. Na Aegis repozitorijumu ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), idite na odeljak Releases gde se objavljuju stabilne verzije.





- Preuzmite najnoviju verziju APK-a
- Pre nego što instalirate APK, uverite se da ste na svom uređaju (u Android podešavanjima) autorizovali instalaciju aplikacija iz nepoznatih izvora.
- APK koji je dostavljen na GitHub potpisan je od strane programera istim ključem kao i na F-Droid



Nakon ručne instalacije, aplikacija će funkcionisati identično. Imajte na umu da ažuriranja neće biti automatska: potrebno je periodično proveravati GitHub za nove verzije.



### Google Play Store vs F-Droid



Aegis Authenticator je dostupan i na Google Play Store-u i na F-Droid-u, pružajući vam izbor metode instalacije:



**Google Play Store:**




- ✅ Automatska ažuriranja integrisana u Android sistem
- ✅ Jednostavna, poznata instalacija
- ✅ Isti potpisan APK kao na drugim kanalima



**F-Droid (preporučeno) :**




- ✅ Besplatna i otvorena prodavnica
- ✅ Reproduktivna i proverljiva konstrukcija
- ✅ Nije potrebna Google usluga
- ✅ Poštovanje filozofije slobodnog softvera



Izbor između ove dve opcije zavisi od vaših preferencija u vezi sa Google ekosistemom. Ako preferirate jednostavnost, Play Store je idealan. Ako želite pristup koji više poštuje privatnost, nezavisan od Google usluga, F-Droid je bolji izbor.



## Prva konfiguracija



Kada se Aegis pokrene prvi put, predložen je početni postupak konfiguracije kako bi se osigurao vaš 2FA kod:



![Configuration initiale Aegis](assets/fr/01.webp)



*Početni proces konfiguracije Aegis-a: ekran dobrodošlice, izbori sigurnosti, definisanje glavne lozinke i finalizacija*



### Postavite glavnu lozinku



Aegis će vas prvo zamoliti da izaberete glavnu lozinku. Ova lozinka će se koristiti za šifrovanje svih vaših autentifikacionih tokena sačuvanih u trezoru. Preporučujemo da postavite jaku, jedinstvenu lozinku koju ćete znati samo vi.



**⚠️ Upozorenje:** nemojte zaboraviti ovu lozinku - ako je izgubite, vaši šifrovani 2FA kodovi će postati nedostupni (ne postoji zadnja vrata). Aegis će vas zamoliti da unesete lozinku dva puta radi potvrde.



### Omogući otključavanje biometrijom (opciono)



Ako vaš Android uređaj ima čitač otisaka prstiju ili drugi biometrijski senzor, Aegis će vas pozvati da aktivirate biometrijsko otključavanje. Ova opcija je opcionalna, ali vrlo praktična: omogućava vam brzo otključavanje aplikacije otiskom prsta ili licem, umesto da svaki put unosite lozinku.



Imajte na umu da su biometrijski podaci dodatna pogodnost: vaša glavna lozinka je i dalje potrebna ako se biometrijski podaci promene ili ako se uređaj ponovo pokrene.



### Otkrij postavke aplikacije



Kada uđete u aplikaciju (glavni Interface je u početku prazan), upoznajte se sa dostupnim opcijama konfiguracije. Pristupite podešavanjima putem padajućeg menija u gornjem desnom uglu ekrana (tri vertikalne tačke), zatim izaberite "Podešavanja".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface glavni Aegis prazan na početku, pristup meniju parametara i pregled dostupnih opcija*



Meni podešavanja Aegis-a grupiše nekoliko važnih sekcija:





- **Izgled**: Prilagodite temu (svetla, tamna, AMOLED), jezik i druge vizuelne postavke
- **Ponašanje**: Konfigurišite ponašanje aplikacije prilikom interakcije sa listom unosa
- **Ikone paketi**: upravljajte i uvozite ikone pakete kako biste prilagodili izgled i doživljaj vaših naloga
- **Bezbednost**: Postavke za šifrovanje, biometrijsko otključavanje, automatsko zaključavanje i druge bezbednosne parametre
- **Bekapovi**: Konfigurišite automatske bekapove na lokaciju po vašem izboru
- **Import & Export**: Uvezite rezervne kopije iz drugih aplikacija za autentifikaciju i ručno izvezite svoj Aegis trezor
- **Dnevnik revizije**: Detaljan dnevnik svih značajnih događaja u aplikaciji



Ova jasna organizacija omogućava vam da konfigurišete Aegis prema vašim preferencijama i potrebama za sigurnošću.



## Dodajte 2FA nalog



Sa konfiguriranim Aegis-om, pređimo na suštinu: dodavanje vaših naloga sa dvofaktorskom autentifikacijom. Proces je jednostavan, a Aegis nudi nekoliko metoda za integraciju vaših autentifikacionih kodova.



### Tri dostupne metode sabiranja



Sa glavnog Aegis Interface, pritisnite dugme **+** u donjem desnom uglu da biste pristupili opcijama dodavanja. Imate tri opcije:





- **Skeniraj QR kod**: Skeniraj direktno QR kod prikazan od strane veb servisa
- **Skeniraj sliku**: Skeniraj QR kod sa slike sačuvane na svom uređaju
- **Unesite ručno**: Ručno unesite informacije o 2FA nalogu



### Praktičan primer: konfigurisanje Bitwarden-a



Uzmimo konkretan primer aktivacije 2FA na Bitwardenu da ilustrujemo proces:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Primer aktivacije 2FA na Bitwardenu: Interface web sa opcijama autentifikacije i preporuka za Aegis*





- **Prijavljivanje i pristup podešavanjima**: Prijavite se na svoj Bitwarden nalog i pristupite podešavanjima, kartica "Bezbednost"
- **Odsek za provajdere**: Idite na odsek "Provajderi" i kliknite na "Upravljaj" u odeljku "Aplikacija za autentifikaciju"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Kompletan proces dodavanja naloga: QR kod prikazan od strane usluge, tajni ključ vidljiv i unet verifikacioni kod*





- **Skeniraj QR kod**: Otvara se iskačući prozor sa QR kodom i tajnim ključem
- **U Aegis**: Koristite "Skeniraj QR kod" da automatski preuzmete informacije
- **Verifikacija**: Unesite 6-cifreni kod koji je generisao Aegis u polje "Verifikacioni kod"
- **Aktivacija**: Kliknite na "Uključi" da biste završili aktivaciju



### Dodajte detalje ručno



Ako više volite ili niste u mogućnosti da skenirate QR kod, koristite opciju "Unesite ručno". Formular vam omogućava da unesete:



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Proces dodavanja novog 2FA naloga: prazan Interface, dodaj opcije, ručni unos i nalog uspešno dodat*





- **Ime**: Ime usluge (npr. Bitwarden, GitHub...)
- **Izdavalac**: Izdavalac (često identičan imenu)
- **Grupa**: Opcionalno, za organizovanje vaših naloga po kategoriji
- **Napomena**: Lične primedbe na ovom nalogu
- **Tajna**: Tajni ključ koji obezbeđuje usluga (podrazumevano maskiran)
- **Napredno**: Napredni parametri (algoritam, period, broj cifara)



Kada je nalog dodat, pojavljuje se na vašoj listi sa trenutnim kodom i indikatorom vremena koji pokazuje preostalo vreme do obnove.



### Univerzalna kompatibilnost



Aegis je kompatibilan sa svim uslugama koje koriste TOTP i HOTP standarde, uključujući praktično sve sajtove koji nude 2FA: društvene mreže, banke, menadžere lozinki, kripto platforme, itd.



### Organizacija ulaza



Kada dodate nekoliko naloga, cenićete Aegis-ove alate za organizaciju:





- **Prilagođeno sortiranje:** Podrazumevano, nalozi su navedeni abecednim redom, ali možete ručno promeniti redosled
- **Grupe i kategorije:** Kreirajte grupe kako biste odvojili svoje lične naloge od poslovnih naloga, ili ih grupišite prema tipu usluge (bankarstvo, e-mail, društvene mreže, itd.)
- **Prilagođene ikone:** Aegis pokušava automatski dodeliti odgovarajuću ikonu ako je dostupna, u suprotnom možete izabrati iz mnogih generičkih ikona ili uvesti sliku
- **Brza pretraga:** Traka za pretragu na vrhu omogućava vam da unesete nekoliko slova kako biste odmah filtrirali odgovarajuće unose



Dodirom na unos, OTP kod se prikazuje u punoj veličini (ako je bio skriven) i možete ga kopirati u međumemoriju dugim pritiskom - zgodno za lepljenje u aplikaciju na koju želite da se povežete.



## Sigurnost i rezervne kopije



Sa bezbednošću u srcu Aegis-a, važno je razumeti kako su vaši 2FA kodovi zaštićeni i kako osigurati njihovu postojanost u slučaju problema.



### Bezbednosna arhitektura



**Robusna enkripcija**: Svi vaši kodovi su sačuvani u enkriptovanom sefu koristeći **AES-256 algoritam u GCM modu**, u kombinaciji sa vašom glavnom lozinkom. Izvođenje ključa zasnovano je na **scrypt**-u, pružajući poboljšanu zaštitu protiv napada grube sile.



**Sigurno otključavanje** : Glavna lozinka je potrebna za dešifrovanje vaših podataka. Biometrija (opcionalno) koristi **Android Secure Keystore** i TEE (Trusted Execution Environment) za zaštitu ključa za šifrovanje.



**Minimalne dozvole**: Aegis radi van mreže po defaultu, zahtevajući samo pristup kameri (QR skeniranje), biometriji i vibratoru. Podaci se ne prikupljaju niti dele.



### Opcije za bekap



Aegis nudi nekoliko strategija bekapa kako bi zadovoljio različite potrebe za sigurnošću i praktičnošću:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface kompletan sa dodatim nalogom, upozorenjem o rezervnoj kopiji, automatskim podešavanjima rezervne kopije i strategijama rezervne kopije*



**1. Automatske lokalne sigurnosne kopije**




- Konfigurišite odredišni folder po vašem izboru
- Prilagodljiva učestalost (nakon svake promene, dnevno, itd.)
- Datoteke zaštićene lozinkom i šifrovane (.aesvault)
- Kompatibilan sa sinhronizovanim fasciklama (Nextcloud, Dropbox, itd.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Proces odabira rezervne fascikle: istraživač datoteka, odredišna fascikla i autorizacija pristupa*



**2. Android** cloud backupovi




- Opcionalna integracija sa sistemom za pravljenje rezervnih kopija na Androidu
- Dostupno samo za šifrovane sefove (očuvana sigurnost)
- Transparentna sigurnosna kopija sa drugim Android podacima
- Automatsko vraćanje na prethodno stanje prilikom promene uređaja



**3. Ručni** izvozi




- Izvoz na zahtev putem **Podešavanja > Uvoz i Izvoz**
- Izbor šifrovanog (preporučeno) ili otvorenog formata
- Korisno za migracije ili povremene rezervne kopije



### Dobre bezbednosne prakse





- Čuvajte nekoliko rezervnih verzija kako biste sprečili oštećenje
- Redovno testirajte **svoje rezervne kopije pokušajem vraćanja**
- Čuvajte kodove za oporavak koje pruža usluga odvojeno
- **Vaša glavna lozinka** je i dalje potrebna čak i uz rezervne kopije u oblaku
- **Osigurajte svoju glavnu lozinku**: koristite jedinstvenu, jaku lozinku pohranjenu u menadžeru lozinki
- **Ažurirajte svoju aplikaciju** sa najnovijim sigurnosnim zakrpama
- Aktiviraj **automatsko zaključavanje** u podešavanjima kako bi osigurao pristup aplikaciji
- Onemogući **snimke ekrana** (podrazumevana opcija) kako bi sprečio presretanje tvojih kodova
- **Koristite biometriju štedljivo**: preferirajte lozinke za kritične pristupe



## Poređenje sa drugim aplikacijama



Kako se Aegis poredi sa drugim popularnim aplikacijama za autentifikaciju?



### Aegis vs Google Authenticator



**Egis :**




- ✅ Otvoreni kod i moguće izvršiti reviziju
- ✅ Lokalna šifrovana sigurnosna kopija
- ✅ Napredna organizacija (grupe, ikone, pretraga)
- ✅ Nema prikupljanja podataka
- ❌ Samo za Android



**Google Autentifikator :**




- ✅ Dostupno na Androidu i iOS-u
- ✅ Sinhronizacija sa oblakom (od 2023)
- ❌ Zatvoreni izvorni kod
- ❌ Ograničena funkcionalnost
- ❌ Potencijalno prikupljanje podataka od strane Google-a



### Aegis vs Authy



**Egis :**




- ✅ Otvoreni kod
- ✅ Nije potreban nalog
- ✅ Izvoz koda moguć
- ✅ Totalna kontrola podataka
- ❌ Nema izvorne sinhronizacije na više uređaja



**Authy :**




- ✅ Sinhronizacija na više uređaja
- ✅ Dostupno na Androidu i iOS-u
- ❌ Zatvoreni izvorni kod
- ❌ Zahteva broj telefona
- ❌ Nije moguće izvesti kodove
- ❌ Desktop aplikacije uklonjene u martu 2024



Aegis je odličan izbor za korisnike Androida koji cene transparentnost, lokalnu sigurnost i potpunu kontrolu nad svojim podacima. Alternative poput Authy su bolje ako vam je apsolutno potrebna automatska sinhronizacija na više uređaja.




## Zaključak



Aegis Authenticator je odlično rešenje za one koji traže aplikaciju za dvofaktorsku autentifikaciju koja je prijateljska prema privatnosti, sigurna i transparentna. Njegov pristup otvorenog koda, u kombinaciji sa snažnom enkripcijom i urednim Interface, čini ga vrhunskim izborom za zaštitu vaših online naloga.



Iako je ograničen na Android i nedostaje mu nativna sinhronizacija sa oblakom, Aegis više nego nadoknađuje ova ograničenja svojom filozofijom "privatnost po dizajnu" i potpunom kontrolom podataka. Za korisnike zabrinute za svoju digitalnu privatnost, Aegis nudi kredibilnu i moćnu alternativu dominantnim vlasničkim rešenjima na tržištu.



Bezbednost vaših online naloga ne mora zavisiti od dobre volje komercijalnih kompanija. Sa Aegis-om, vi zadržavate kontrolu nad vašim autentifikacionim kodovima, u digitalnom sefu čiji ključ držite samo vi.



## Resursi



### Zvanične veb stranice




- **Zvanična veb stranica**: [getaegis.app](https://getaegis.app/) - Prezentacija aplikacije i preuzimanje
- **Izvorni kod**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Zvanični GitHub repozitorijum
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Instalacija putem besplatne prodavnice



### Tehnička dokumentacija




- **Vault dokumentacija**: [Vault dizajn](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Tehnički opis enkripcije i sigurne arhitekture
- **Službena FAQ**: [getaegis.app/#faq](https://getaegis.app/#faq) - Odgovori na često postavljana pitanja
- **Projekat viki**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Kompletna korisnička dokumentacija