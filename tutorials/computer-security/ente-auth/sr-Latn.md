---
name: Ente Auth
description: Aplikacija otvorenog koda, sa end-to-end enkripcijom za 2FA autentifikaciju
---
![cover](assets/cover.webp)



Dvofaktorska autentifikacija (2FA) postala je neophodna za zaštitu naših online naloga. Pored vaše uobičajene lozinke, zahteva privremeni kod, koji obično generiše posebna aplikacija. Ovaj mehanizam, poznat kao TOTP (Time-Based One-Time Password), garantuje da čak i ako vaša lozinka bude kompromitovana, napadač neće moći da pristupi vašem nalogu bez posedovanja ovog drugog faktora, koji se obnavlja svakih 30 sekundi.



Međutim, odabir prave aplikacije za autentifikaciju nije trivijalan. Google Authenticator, iako popularan, ima velike nedostatke: vlasnički kod koji je nemoguće revidirati, sinhronizacija bez end-to-end enkripcije i rizik od potpunog gubitka kodova u slučaju problema sa vašim telefonom. Druga rešenja, kao što je Authy, zahtevaju broj telefona i ne garantuju potpunu poverljivost.



**Ente Auth** se ističe kao moderna, sigurna alternativa. Ova besplatna, open source, multiplatformska aplikacija, koju je razvila ekipa iza [Ente Photos](https://ente.io), nudi end-to-end enkriptovane cloud backup-e i besprekornu sinhronizaciju između svih vaših uređaja. Za razliku od vlasničkih rešenja, Ente Auth vam daje potpunu kontrolu nad vašim autentifikacionim kodovima bez ugrožavanja vaše privatnosti.



U ovom vodiču pokazaćemo vam korak po korak kako instalirati i koristiti Ente Auth, i zašto se ovo rešenje razlikuje od tradicionalnih autentifikatora.



## Predstavljamo Ente Auth



Ente Auth je razvijen od strane tima iza Ente Photos, usluge za skladištenje fotografija koja je krajnje šifrovana i prijateljska prema privatnosti. U skladu sa filozofijom Ente ("Ente" znači "moje" na malajalamskom, simbolizujući kontrolu nad vašim podacima), Ente Auth je dizajniran da korisnicima vrati potpunu kontrolu nad njihovim kodovima za dvofaktorsku autentifikaciju.



### Glavne karakteristike



**Standardni TOTP kodovi**: Ente Auth generiše privremene kodove kompatibilne sa većinom servisa (GitHub, Google, Binance, ProtonMail, itd.). Možete dodati onoliko 2FA naloga koliko vam je potrebno, a aplikacija izračunava kodove na osnovu datih tajni.



**Kraj-do-kraja šifrovana rezervna kopija u oblaku**: Vaši kodovi su sigurno pohranjeni na mreži. Samo vi možete da ih dešifrujete - ključ za šifrovanje se izvodi iz vaše lozinke i poznat je samo vama. Ente (server) nema saznanja o vašim tajnama, pa čak ni o nazivima vaših naloga, jer je sve šifrovano na strani klijenta koristeći arhitekturu bez znanja.



**Sinhronizacija na više uređaja**: Možete instalirati Ente Auth na nekoliko uređaja (smartfon, tablet, računar) i pristupiti svojim kodovima na svim njima. Sve promene se automatski i trenutno prenose na vaše druge uređaje putem šifrovanog oblaka, pružajući vam veliku fleksibilnost u svakodnevnom radu.



**Minimalistički, intuitivni Interface**: Aplikacija nudi pojednostavljeni Interface, lako ga je naučiti čak i za korisnike bez tehničkog znanja. 2FA nalozi su prikazani sa imenom usluge, vašim prijavnim imenom i 6-cifrenim kodom, koji se ažurira u realnom vremenu. Ente Auth takođe prikazuje sledeći kod nekoliko sekundi unapred kako biste izbegli probleme sa istekom.



**Otvoreni kod i revidiran**: Izvorni kod Ente Auth-a je [javan na GitHub-u](https://github.com/ente-io/auth) pod AGPL v3.0 licencom. Bilo koji programer može ga revidirati kako bi proverio nedostatke ili nepoželjno ponašanje. Implementirana kriptografija bila je predmet [nezavisne eksterne revizije](https://ente.io/blog/cryptography-audit/), što je garancija ozbiljnosti sigurnosti aplikacije.



### Prednosti i ograničenja



**Prednosti:**




- Privatnost po dizajnu sa end-to-end enkripcijom
- Sigurna sinhronizacija između svih vaših uređaja
- Revidibilan otvoreni izvorni kod
- Interface jasno, intuitivno korisničko Interface
- Automatska rezervna kopija za sprečavanje gubitka kodova
- Dostupno na svim platformama (mobilnim i desktop)



**Ograničenja:**




- Potrebna internet konekcija za sinhronizaciju
- Napredni korisnici mogu preferirati 100% offline rešenja kao što je Aegis (samo za Android)
- Relativno nedavno u poređenju sa ustaljenim rešenjima



## Instalacija



Ente Auth je dostupan na većini popularnih platformi. Možete preuzeti aplikaciju sa [zvanične veb stranice](https://ente.io/auth) ili iz zvaničnih prodavnica.



![Installation d'Ente Auth](assets/fr/01.webp)



*Ente Auth stranica za preuzimanje sa svim dostupnim platformama*



### Android


Imate nekoliko opcija:




- **Google Play Store**: Pretraži "Ente Auth" za klasičnu instalaciju
- **F-Droid**: Dostupno iz kataloga aplikacija otvorenog koda za Android, sa garancijom verifikovane izrade i bez vlasničkog sadržaja
- **Ručno instaliranje**: APK datoteke mogu se preuzeti sa [GitHub stranice projekta](https://github.com/ente-io/auth/releases) sa integrisanim obaveštenjem o novim verzijama



### iOS (iPhone/iPad)


Instalirajte Ente Auth direktno iz Apple App Store-a pretraživanjem imena aplikacije. iOS aplikacija se takođe može pokrenuti na Mac računarima opremljenim Apple Silicon čipovima (M1/M2) putem Mac App Store-a.



### Računari (Windows, macOS, Linux)


Ente Auth nudi izvorne desktop aplikacije. Posetite [ente.io/download](https://ente.io/download) ili [Releases sekciju na GitHub-u](https://github.com/ente-io/auth/releases) :





- **Windows**: Isporučen je EXE instalacioni program
- **macOS**: Prevucite i otpustite DMG sliku diska u Aplikacije
- **Linux**: Više formata dostupno (prenosivi AppImage, .deb za Debian/Ubuntu, .rpm za Fedora/Red Hat)



**Napomena:** Ovaj vodič je zasnovan na Ente Auth v4.4.4 i novijim verzijama. Ranije verzije mogu imati manje razlike Interface.



### Interface Web


Bez instalacije, možete pristupiti svojim kodovima putem [auth.ente.io](https://auth.ente.io) iz bilo kog pregledača. Interface web je ograničen na pregledanje kodova (korisno za rešavanje problema), jer dodavanje naloga zahteva mobilnu ili desktop aplikaciju iz bezbednosnih razloga.



## Prva konfiguracija



### Kreiranje naloga



Kada prvi put pokrenete Ente Auth, imate dve opcije:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Ente Auth početni ekran sa opcijama za kreiranje naloga*



**Sa nalogom (preporučeno)**: Izaberite "Kreiraj nalog" i unesite svoj e-mail Address i lozinku. **Važno**: ova lozinka služi kao glavna lozinka za šifrovanje vaših podataka. Izaberite jaku, jedinstvenu lozinku, jer ne postoji konvencionalna procedura za resetovanje bez gubitka podataka. Ako je izgubite, vaši šifrovani podaci će biti nepreuzimljivi.



**Offline režim**: Izaberite "Koristi bez rezervnih kopija" da biste koristili aplikaciju lokalno bez oblaka. U ovom režimu, vaši kodovi ostaju na uređaju, ali ćete ih morati ručno izvoziti da biste ih sačuvali.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Proces verifikacije e-pošte i generisanje 24-reči ključa za oporavak*



Za verifikaciju e-pošte može biti zatraženo da se potvrdi kreiranje naloga i omogući oporavak na novom uređaju. Ente Auth će vam takođe obezbediti ključ za oporavak od 24 reči (zasnovan na BIP39 metodi). **Važno je da sačuvate ovaj ključ** na sigurnom mestu: to je vaš jedini način za oporavak podataka ako zaboravite lozinku.



### Lokalna sigurnost



Preporučujem da omogućite lokalnu zaštitu pomoću koda ili biometrije. Idite na **Podešavanja → Bezbednost → Zaključani ekran** i konfigurišite :





- **Otključavanje biometrijom**: Face ID, otisak prsta u zavisnosti od mogućnosti vašeg uređaja
- **PIN/lozinka specifična za aplikaciju**
- **Kašnjenje automatskog zaključavanja**: npr. "Odmah" ili nakon 30 sekundi neaktivnosti



Ova zaštita sprečava neovlašćen pristup vašim kodovima ako neko dobije pristup vašem otključanom telefonu. Imajte na umu da je ova brava dodatna barijera: vaši podaci ostaju šifrovani od kraja do kraja čak i bez ove zaštite.



## Dodaj 2FA naloge



### Standard procedure



Da biste dodali novi 2FA nalog, uzmimo konkretan primer aktiviranja 2FA na Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Ente Auth's main Interface spreman za dodavanje prvog 2FA* naloga



**Service side (Bull Bitcoin)**: Prijavite se na svoj Bull Bitcoin nalog, idite na sigurnosne postavke i omogućite dvofaktorsku autentifikaciju.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* meni sigurnosnih postavki



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Opcija za omogućavanje dvofaktorske autentifikacije na Bull Bitcoin*



Usluga će zatim prikazati QR kod koji treba da skenirate pomoću vaše aplikacije za autentifikaciju:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*QR kod generisan od strane Bull Bitcoin za skeniranje sa vašim autentifikatorom*



**U Ente Auth**: Kliknite na "Unesite ključ za podešavanje" zatim skenirajte QR kod prikazan od strane Bull Bitcoin. Ente Auth će automatski prepoznati nalog i popuniti polja.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Konfigurisanje detalja naloga Bull Bitcoin u Ente Auth*



Možete prilagoditi naziv usluge i svoju prijavu kako biste ih lakše pronašli. Napredne postavke (SHA1 algoritam, period od 30s, 6 cifara) su generalno ispravne po defaultu.



**Validacija na strani usluge**: Vratite se na Bull Bitcoin i unesite 6-cifreni kod generisan od strane Ente Auth za finalizaciju aktivacije.



![Saisie du code 2FA](assets/fr/09.webp)



*Unesite kod koji je generisao Ente Auth za validaciju 2FA* aktivacije



![2FA activée](assets/fr/10.webp)



*Potvrda uspešne aktivacije 2FA na Bull Bitcoin*



**Rezervni kodovi**: Bik Bitcoin će vam obezbediti kodove za oporavak. **Sačuvajte ih na sigurnom mestu, odvojeno od vašeg autentifikatora.**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Opcija za generate rezervne kodove za hitne slučajeve na Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Lista kodova za oporavak koje treba čuvati na sigurnom mestu*



### Organizacija i upravljanje



Ente Auth nudi nekoliko praktičnih funkcija:



**Brzo kopiranje**: Pritisnite kod da biste ga automatski kopirali u međumemoriju.



**Radnje osetljive na kontekst**: Pritisnite i držite (ili desni klik na desktopu) da biste uredili, obrisali, delili ili zakačili unos.



**Tagovi i pretraga**: Organizujte svoje naloge pomoću tagova (lični/profesionalni, po kategoriji usluge) i koristite traku za pretragu za brzo filtriranje.



![Création d'un tag](assets/fr/17.webp)



*Proces kreiranja oznaka: kontekstualni meni i dijalog za kreiranje*



![Tag appliqué](assets/fr/18.webp)



*Oznaka "Bitcoin" uspešno primenjena na nalog Bull Bitcoin*



**Automatske ikone**: Svaki unos može biti ilustrovan logotipom usluge, zahvaljujući integraciji [Simple Icons] paketa ikona (https://simpleicons.org/).



**Privremeno sigurno deljenje**: Jedinstvena funkcija Ente Auth, sigurno deljenje omogućava vam da prenesete 2FA kod kolegi bez otkrivanja osnovne tajne. generate šifrovani link važi maksimalno 2, 5 ili 10 minuta - primalac vidi kod u realnom vremenu, ali ga ne može izvesti niti pristupiti podacima naloga. Ova metoda je idealna za tehničku pomoć ili privremenu saradnju, nudeći nivo sigurnosti koji nije moguć sa jednostavnim snimkom ekrana ili tekstualnom porukom.



![Partage sécurisé](assets/fr/19.webp)



*Interface privremeno sigurno deljenje: izaberite trajanje (5 min)*



**Siguran izvoz/uvoz**: Ente Auth vam omogućava da izvezete svoje kodove u druge aplikacije ili da ih uvezete iz Google Authenticator-a i drugih rešenja. Izvoz se vrši putem šifrovane datoteke ili QR koda, što garantuje prenosivost vaših podataka bez ugrožavanja sigurnosti.



**BIP39 ključ za oporavak**: Aplikacija automatski generiše frazu za oporavak od 24 reči prema BIP39 (Bitcoin predlog za poboljšanje) standardu, identičnu onima u kripto novčanicima. Ova fraza je vaš krajnji ključ za oporavak, omogućavajući vam da povratite sve vaše kodove čak i ako zaboravite vašu glavnu lozinku.



## Konfiguracija i postavke



Ente Auth nudi brojne opcije prilagođavanja dostupne putem postavki aplikacije:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Pregled parametara dostupnih u Ente Auth*



### Upravljanje nalozima i podacima



![Paramètres de sécurité](assets/fr/14.webp)



*Napredne opcije sigurnosti: verifikacija emaila, PIN kod, aktivne sesije*



Postavke bezbednosti vam omogućavaju da:




- Omogući verifikaciju e-pošte za nove veze
- Aktiviraj pristupni ključ
- Pogledajte aktivne sesije na vašim različitim uređajima
- Podešavanje PIN koda ili biometrije



### Interface i opcije korišćenja



![Paramètres généraux](assets/fr/15.webp)



*Parametri Interface i prilagođavanje aplikacije*



Opšta podešavanja uključuju :




- **Jezik**: Interface višejezični
- **Prikaz**: Velike ikone, kompaktni režim
- **Privatnost**: Sakrij kodove, brza pretraga
- **Telemetrija**: Prijavljivanje grešaka (može se onemogućiti)



## Bekap i sinhronizacija



### Kako funkcioniše enkripcija



Kada dodate nalog sa povezanim Ente nalogom, aplikacija odmah šifrira ove osetljive podatke lokalno koristeći vaš glavni ključ (izveden iz vaše lozinke). Šifrovani podaci se zatim šalju na Ente server za skladištenje.



Zahvaljujući ovom mehanizmu, krajnje do kraja šifrovana cloud rezervna kopija vaših kodova je uvek dostupna. Ako izgubite svoj uređaj, jednostavno ponovo instalirajte Ente Auth i ponovo se povežite: aplikacija će automatski preuzeti i dešifrovati sve vaše kodove.



### Sinhronizacija više uređaja



Ako koristite Ente Auth na pametnom telefonu i računaru, sve dodatke ili izmene na jednom uređaju videćete u roku od nekoliko sekundi na drugom. Ova sinhronizacija prolazi kroz Ente-ov cloud, ali pošto su podaci end-to-end enkriptovani, server vidi samo nečitljiv enkriptovani sadržaj.



![Synchronisation mobile](assets/fr/16.webp)



*Demonstracija sinhronizacije: isti Bull Bitcoin nalog dostupan na mobilnom i desktop uređaju*



Sinhronizacija je besprekorna: instalirajte Ente Auth na svoj pametni telefon, prijavite se sa svojim akreditivima i svi vaši 2FA kodovi (ovde Bull Bitcoin) će se automatski pojaviti. Primer iznad pokazuje savršenu sinhronizaciju između desktopa i mobilnog uređaja - isti Bull Bitcoin kod je dostupan na oba uređaja.



Što se tiče poverljivosti, ni Ente ni bilo koja treća strana nemaju pristup vašim 2FA tajnama. Čak su i metapodaci (oznake, beleške, imena usluga) šifrovani pre slanja. Ova arhitektura sa nultim znanjem osigurava da samo vi možete dešifrovati vaše kodove.



### Van mreže



Sinhronizacija zahteva internet, ali Ente Auth savršeno funkcioniše van mreže na svakom uređaju, jer su svi podaci lokalno sačuvani. Promene napravljene van mreže se stavljaju u red i sinhronizuju čim se veza obnovi.



## Sigurnost i privatnost



### Kriptografske garancije



Ente Auth je zasnovan na robusnoj end-to-end enkripciji sa arhitekturom bez znanja. Vaši kodovi su šifrovani ključem koji samo vi posedujete, izvedenim iz vaše glavne lozinke korišćenjem naprednih funkcija derivacije ključa.



**Arhitektura nultog znanja:** Ente fizički ne može pristupiti vašim podacima. Čak su i metapodaci (imena usluga, oznake, beleške) šifrovani na strani klijenta pre prenosa. Ovaj pristup osigurava da, u slučaju napada na vaše servere ili zahteva vlade, Ente može otkriti samo šifrovane podatke koji se ne mogu pročitati bez vaše lozinke.



**Lokalno šifrovanje**: Proces šifrovanja se u potpunosti odvija na vašem uređaju pre nego što se pošalje u oblak. Ente-ovi serveri primaju i čuvaju samo šifrovane podatke, što onemogućava neovlašćen pristup, čak i za administratore usluge.



### Transparentnost i revizije



Kako je kod [open source](https://github.com/ente-io/auth), zajednica može verifikovati odsustvo backdoor-a. Ente je imao [više eksternih revizija](https://ente.io/blog/cryptography-audit/) sprovedenih kako bi se potvrdila sigurnost njegove implementacije:





- **Cure53** (Nemačka): Revizija bezbednosti aplikacije i kriptografije
- **Symbolic Software** (Francuska): Specijalizovana stručnost u kriptografiji
- **Fallible** (India): Testiranje penetracije i analiza ranjivosti



Ove nezavisne revizije, koje sprovode priznate firme, garantuju da Ente Auth-ova kriptografska implementacija ispunjava najbolje bezbednosne prakse i nema kritične nedostatke.



### Politika privatnosti



Ente Auth primenjuje [primerenu politiku privatnosti](https://ente.io/privacy/) zasnovanu na minimalnom prikupljanju podataka. Čuvaju se samo informacije koje su strogo neophodne za rad usluge: vaš e-mail Address za autentifikaciju i oporavak naloga.



**Bez praćenja ili telemetrije**: Za razliku od većine aplikacija, Ente Auth ne prikuplja metrike korišćenja, podatke o identifikaciji grešaka niti informacije o ponašanju. Aplikacija funkcioniše bez nametljivog oglašavanja ili analitičkih tragača.



**Usklađenost sa GDPR-om**: Ente je u potpunosti usklađen sa Evropskom opštom uredbom o zaštiti podataka. Imate pravo da pristupite, ispravite ili obrišete svoje podatke u bilo kom trenutku. [Izvoz podataka](https://ente.io/take-control/) je udaljen samo jedan klik, a trajno brisanje vašeg naloga briše sve vaše podatke sa servera.



**Decentralizovano, sigurno skladištenje**: Vaši šifrovani podaci su replicirani kod 3 različita provajdera, u 3 različite zemlje, garantujući optimalnu dostupnost dok se izbegava zavisnost od jednog provajdera oblaka.



Poslovni model Ente zasnovan je na plaćenoj usluzi Ente Photos, što nam omogućava da ponudimo Ente Auth **besplatno i bez ograničenja** bez ugrožavanja vaše privatnosti monetizacijom vaših podataka. Ovaj pristup garantuje održivost usluge bez oslanjanja na oglašavanje ili preprodaju ličnih podataka.



## Poređenje sa drugim rešenjima




| Aplikacija              | Otvoreni kod | Sigurnosna kopija u oblaku | E2EE | Sinhronizacija više uređaja | Platforme                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (bez E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(desktop aplikacije uklonjene august 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(nedavna, manje uspostavljena)*              |

Ente Auth se izdvaja kao jedno od retkih rešenja koje kombinuje sve prednosti: transparentnost izvornog koda, šifrovanu rezervnu kopiju u oblaku i sinhronizaciju između platformi.



## Preporučeni slučajevi upotrebe



### Pojedinačni korisnici



Ente Auth je idealan za osobe koje su svesne bezbednosti i sistematski aktiviraju 2FA. Više nećete morati da brinete o gubitku kodova prilikom promene telefona, ili da birate između pogodnosti i sigurnosti.



### Porodica i korišćenje više uređaja



Aplikacija dolazi do izražaja ako koristite nekoliko uređaja. Možete sačuvati svoje kodove na pametnim telefonima i tabletima, ili deliti određene porodične kodove (Netflix, porodični cloud) sinhronizovano i sigurno.



### Profesionalna upotreba



Za timove koji upravljaju osetljivim nalozima, Ente Auth olakšava saradnju uz očuvanje bezbednosti, zahvaljujući naprednim funkcijama deljenja integrisanim u odeljak "Organizacija i upravljanje".



## Najbolje prakse





- **Sačuvajte svoje hitne kodove**: Čuvajte kodove za oporavak koje pruža svaka usluga dalje od vašeg telefona.





- **Koristite jaku glavnu lozinku**: Vaša Ente Auth glavna lozinka mora biti jedinstvena i snažna, jer štiti sve vaše kodove.





- **Aktiviraj lokalnu zaštitu**: Konfiguriši PIN ili biometriju kako bi sprečio neovlašćen fizički pristup.





- **Ne preterujte sa prilagođavanjem**: Izbegavajte napredne izmene koje bi mogle ugroziti sinhronizaciju.





- **Ažurirajte aplikaciju**: Ažuriranja ispravljaju sigurnosne propuste i poboljšavaju funkcionalnost.





- **Testiranje vraćanja**: Povremeno proverite da li možete da vratite svoje kodove na drugom uređaju.



## Zaključak



Ente Auth predstavlja moderno, sveobuhvatno rešenje za dvofaktorsku autentifikaciju. Kombinovanjem sigurnosti, transparentnosti i jednostavnosti korišćenja, ova open source aplikacija zadovoljava potrebe zahtevnih korisnika bez žrtvovanja praktičnosti.



Za razliku od vlasničkih rešenja koja vas zaključavaju u neprozirni ekosistem, Ente Auth vam vraća kontrolu nad vašim podacima za autentifikaciju dok vas štiti od slučajnog gubitka zahvaljujući svojim šifrovanim rezervnim kopijama.



Bilo da ste pojedinac koji želi da zaštiti svoje lične naloge ili tim koji upravlja poslovnim pristupom, Ente Auth je pametan izbor za modernizaciju vašeg pristupa digitalnoj sigurnosti bez ugrožavanja privatnosti.



## Resursi i podrška



### Zvanična dokumentacija




- **Zvanična veb stranica**: [ente.io/auth](https://ente.io/auth)
- **Help centar**: [help.ente.io/auth](https://help.ente.io/auth)
- **Tehnički blog**: [ente.io/blog](https://ente.io/blog)



### Izvorni kod i transparentnost




- **GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- **Kriptografski audit**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Zajednica




- **Discord**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit**: [r/enteio](https://reddit.com/r/enteio)