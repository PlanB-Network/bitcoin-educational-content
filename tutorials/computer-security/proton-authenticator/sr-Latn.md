---
name: Proton Authenticator
description: Kako mogu koristiti Proton Authenticator za zaštitu svojih naloga pomoću 2FA?
---
![cover](assets/cover.webp)



Dvofaktorska autentifikacija (2FA) dodaje dodatnu sigurnosnu barijeru vašim nalozima zahtevajući, pored vaše lozinke, dodatni dokaz koji samo vi imate. Omogućavanje 2FA drastično smanjuje rizik od hakovanja, čak i ako je vaša lozinka kompromitovana putem fišinga ili curenja podataka. Bez 2FA, napadaču bi bila potrebna samo vaša lozinka da pristupi vašim nalozima; sa 2FA, trebao bi mu i vaš drugi faktor, čime se osujećuju većina pokušaja krađe naloga.



Različite vrste 2FA postoje. SMS kodovi su bolji nego ništa, ali ostaju ranjivi na napade zamene SIM kartice i presretanje. Ne preporučujemo SMS kao primarni 2FA. Aplikacije za autentifikaciju (TOTP) generate privremene kodove lokalno na vašem uređaju, što ih čini mnogo težim za presretanje. Fizički sigurnosni ključevi nude najbolju sigurnost, ali zahtevaju posvećen hardver.



Proton Authenticator je TOTP autentifikator. To je Protonov odgovor na ograničenja postojećih aplikacija: mnoge su vlasničke, sadrže praćenje oglasa i ne nude šifrovanu rezervnu kopiju. Proton Authenticator se izdvaja pružanjem aplikacije otvorenog koda, bez oglasa i praćenja, sa šifrovanom rezervnom kopijom od kraja do kraja.



## Predstavljamo Proton Authenticator



Proton Authenticator je mobilna i desktop TOTP aplikacija za autentifikaciju koju je razvio Proton, poznat po svojim uslugama fokusiranim na privatnost. Kao i svi Proton proizvodi, aplikacija je otvorenog koda i prošla je nezavisne sigurnosne revizije. Dostupna je besplatno na svim platformama (Android, iOS, Windows, macOS, Linux).



Proton Authenticator nudi sledeće ključne funkcije:





- Generisanje **TOTP** kodova za vaše 2FA naloge, kompatibilno sa većinom sajtova koji koriste Google Authenticator, Authy, itd.





- **Opcionalna šifrovana rezervna kopija u oblaku**: možete povezati aplikaciju sa svojim Proton nalogom kako biste napravili rezervnu kopiju i sinhronizovali svoje kodove sa end-to-end enkripcijom. Ako izgubite svoj uređaj, jednostavno povežite novi kako biste povratili sve svoje kodove.





- **Sinhronizacija na više uređaja**: prijavljivanjem u Proton u aplikaciji, vaši 2FA kodovi se automatski sinhronizuju između više uređaja putem end-to-end enkripcije. Na iOS-u, alternativa je sinhronizacija putem iCloud-a.





- **Lokalno zaključavanje pomoću lozinke ili biometrije**: aplikacija nudi zaključavanje pomoću PIN-a i/ili otiska prsta/Face ID-a. Tako da čak i ako neko fizički pristupi vašem otključanom telefonu, neće moći da otvori Proton Authenticator.





- **Bez prikupljanja podataka ili praćenja**: Proton je posvećen tome da ne prikuplja lične podatke putem aplikacije. Nema skrivenog oglašavanja ili analize ponašanja.





- **Jednostavan uvoz/izvoz**: jedna od jakih strana Proton Authenticator-a je njegov čarobnjak za uvoz postojećih naloga, kompatibilan sa drugim aplikacijama (Google Authenticator, Authy, Aegis, itd.). Takođe možete izvesti svoje kodove u datoteku ako je potrebno.



Ukratko, Proton Authenticator ima za cilj da bude beskompromisno 2FA rešenje: sigurno, privatno, fleksibilno.



## Instalacija



Proton Authenticator je dostupan besplatno na svim platformama. Da biste preuzeli aplikaciju, idite na zvaničnu stranicu: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Zvanična stranica Proton Authenticator-a koja prikazuje glavne funkcije aplikacije i Interface*



Na ovoj stranici ćete pronaći linkove za preuzimanje za sve operativne sisteme: Android, iOS, Windows, macOS i Linux. Jednostavno kliknite na operativni sistem po vašem izboru i pratite standardne korake instalacije.



U ovom vodiču pokazaćemo vam kako da instalirate i konfigurišete ga na macOS-u, a zatim ćemo pogledati kako da instalirate aplikaciju na iOS-u i sinhronizujete vaše kodove između dva uređaja.



### Instalacija na macOS



Kada preuzmete i instalirate aplikaciju, pokrenite Proton Authenticator. Prilikom prvog pokretanja, aplikacija vas vodi kroz nekoliko početnih ekrana za konfiguraciju:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Proton Authenticator početni ekran sa porukom "Sigurnost u svakom kodu" i dugmetom "Započni "*



### Početni uvoz



Ako Proton Authenticator otkrije da ste prethodno koristili drugu 2FA aplikaciju, može se pojaviti čarobnjak za uvoz. Podržava direktan uvoz iz određenih aplikacija (Google Authenticator, 2FAS, Authy, Aegis, itd.). Alternativno, možete preskočiti ovaj korak i dodati svoje naloge ručno kasnije.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Čarobnjak za uvoz za prenos kodova iz drugih aplikacija za autentifikaciju*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Kompatibilne aplikacije za uvoz: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth i Google Authenticator*



### Lokalna zaštita aplikacije



Postavite PIN za otključavanje ili omogućite biometrijsko otključavanje (Touch ID) ako je dostupno. Ovaj korak je ključan kako biste sprečili da bilo ko ko koristi vaš Mac dobije slobodan pristup vašim 2FA kodovima.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Ekran za konfiguraciju Touch ID sa porukom "Zaštitite svoje podatke" i dugmetom "Aktiviraj Touch ID "*



### Opcije sinhronizacije



Aplikacija vam takođe omogućava da aktivirate iCloud sinhronizaciju kako biste bezbedno napravili rezervnu kopiju podataka između vaših Apple uređaja.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*Opcija sinhronizacije sa iCloud-om sa porukom "Sigurno napravite rezervnu kopiju svojih podataka uz šifrovanu sinhronizaciju sa iCloud-om"*



Kada su ovi koraci završeni, Proton Authenticator je spreman za upotrebu.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface glavni prazan Proton Authenticator sa opcijama "Kreiraj novi kod" i "Uvezi kodove"*



## Dodajte 2FA nalog sa ProtonMail



Sada ćemo pogledati kako dodati vaš prvi 2FA kod, koristeći ProtonMail kao primer. Ova metoda radi identično za sve usluge koje podržavaju dvofaktorsku autentifikaciju.



### Omogući 2FA na ProtonMail-u



Prvo, možete se konsultovati sa našim vodičem za ProtonMail za više informacija:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Prijavite se na svoj ProtonMail nalog i idite na podešavanja bezbednosti. Potražite opciju "Dvofaktorska autentifikacija" i aktivirajte je.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*ProtonMail podešavanja stranice sa opcijom "Authenticator app" u odeljku "Two-factor authentication "*



Kliknite na dugme da aktivirate autentifikator i ProtonMail će vas uputiti da izaberete aplikaciju za autentifikaciju.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*ProtonMail 2FA prozor za konfiguraciju sa dugmadima "Otkaži" i "Dalje"*



ProtonMail će zatim prikazati QR kod koji treba da skenirate pomoću vaše aplikacije za autentifikaciju.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMail QR kod za skeniranje pomoću vaše aplikacije za autentifikaciju, sa dostupnom opcijom "Unesite ključ ručno umesto toga"*



Ako želite da unesete ključ ručno, kliknite na "Unesite ključ ručno umesto toga" da biste videli tajni ključ.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Ručno unošenje 2FA informacija: Ključ, Interval (30) i Cifre (6)*



### Skenirajte QR kod pomoću Proton Authenticator-a



U Proton Authenticator-u na macOS-u, kliknite na "Create a new code". Aplikacija vam nudi nekoliko opcija: **Scan a QR code** ili **Enter the key manually**.



Koristite kameru svog Mac-a da skenirate QR kod prikazan na ProtonMail ekranu. Kada skenirate QR kod, bićete preusmereni na ekran za konfiguraciju novog koda.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Novi prozor za kreiranje unosa sa naslovom (ProtonMail), tajnom, pošiljaocem (Proton), parametrima cifara i poljima intervala*



Proton Authenticator će automatski popuniti informacije. Možete prilagoditi ime ako želite, zatim kliknite "Sačuvaj".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*Kod TOTP generisan za ProtonMail (848 812) sa prikazanim preostalim vremenom*



### Potvrdi konfiguraciju



ProtonMail će tražiti da unesete 6-cifreni kod generisan od strane Proton Authenticator-a kako biste potvrdili da 2FA radi ispravno.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*ProtonMail ekran za validaciju traži da unesete 6-cifreni kod (848812)*



Kopirajte kod iz aplikacije (klikom na njega) i nalepite ga u ProtonMail da biste završili aktivaciju.



Kada se verifikuje, ProtonMail će vas zamoliti da preuzmete svoje kodove za oporavak. Važno je da ih pažljivo sačuvate.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*ProtonMail ekran za oporavak kodova sa listom kodova za spasavanje i dugmetom "Preuzmi "*



### Hitni kodovi



Kada dodajete nalog, sačuvajte kodove za oporavak koje pruža usluga. Većina sajtova nudi statičke, jednokratne kodove za oporavak koje treba čuvati na sigurnom mestu. Čuvajte ove rezervne kodove van Proton Authenticator-a kako biste mogli pristupiti svom nalogu ako izgubite pristup 2FA aplikaciji.



## Instalacija IOS-a i uvoz koda



Sada kada ste postavili Proton Authenticator na macOS, možda ćete želeti da ga koristite i na vašem iPhone ili iPad uređaju. Evo kako da dobijete vaše 2FA kodove na više uređaja.



### Preuzmite aplikaciju na iOS-u



Idite u App Store i potražite "Proton Authenticator". Preuzmite i instalirajte aplikaciju na svoj iOS uređaj.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Proces instalacije na iOS-u: početni ekran, čarobnjak za uvoz, izbor kompatibilnih aplikacija i završni ekran "Uvezi kodove iz Proton Authenticator-a"*



### Metod 1: Izvoz/Uvoz putem JSON datoteke



Ako ne koristite automatsku sinhronizaciju (iCloud ili Proton nalog), moraćete ručno da prenesete svoje kodove sa Mac-a na iPhone:



**Korak 1 - Izvoz iz macOS** :



Na vašem Mac-u, otvorite Proton Authenticator i idite na Podešavanja (ikona zupčanika). U meniju, kliknite na "Izvoz".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Proton Authenticator meni sa podešavanjima na macOS-u sa vidljivom opcijom "Izvoz"*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Prozor za izvoz sa nazivom datoteke "Proton_Authenticator_backup_2025" i dugmetom "Sačuvaj "*



Sačuvaj JSON datoteku na svom Mac-u. Možeš je poslati sigurnim emailom ili sačuvati u iCloud Drive za pristup sa svog iPhone-a.



**Korak 2 - Uvoz na iOS** :



Na vašem iPhone-u, instalirajte Proton Authenticator i tokom konfiguracije, izaberite opciju za uvoz kodova. Izaberite "Proton Authenticator" sa liste i uvezite JSON fajl.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Proces uvoza na iOS-u: lokalizacija JSON datoteke, potvrda uvoza i ekrani za konfiguraciju sa opcijama Face ID i iCloud*



### Metoda 2: Automatska sinhronizacija



**Preko Proton naloga (za sinhronizaciju na više platformi)** :



Ako još niste postavili Proton nalog i želite da sinhronizujete između različitih operativnih sistema, aplikacija će vas podstaći da kreirate ili povežete Proton nalog.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Ekran za sinhronizaciju uređaja koji vas pita da kreirate besplatan Proton nalog ili da se povežete sa postojećim nalogom*



**Preko iCloud-a (samo za Apple ekosistem)** :


Ako koristite samo Apple uređaje, možete odabrati iCloud sinhronizaciju u postavkama aplikacije. Ova metoda će automatski i sigurno sinhronizovati vaše kodove između svih vaših Apple uređaja, bez potrebe za Proton nalogom.



## Šifrovana rezervna kopija i obnova



Jedna od ključnih karakteristika Proton Authenticator-a je njegovo end-to-end bekapovanje 2FA kodova, osiguravajući da gubitak ili promena uređaja ne znači da morate početi ispočetka.



### Šifrovanje od kraja do kraja



Kada je u pitanju šifrovana cloud rezervna kopija sa Proton Authenticator-om, vaši TOTP tajni ključevi su šifrovani lokalno na vašem uređaju pre nego što budu poslati na Proton server. Dešifrovanje je moguće samo od strane vas, na vašim uređajima povezanim sa vašim Proton nalogom. Proton AG nema ključ za čitanje vaših registrovanih kodova.



Na iOS-u, ako se odlučite za iCloud umesto Proton naloga, vaši podaci su šifrovani prema Apple standardima. Lokalna rezervna kopija na Androidu vam omogućava da šifrujete rezervnu datoteku lozinkom po vašem izboru.



### Obnova u slučaju gubitka



Ako je vaš telefon izgubljen, ukraden ili promenite uređaj :



**Sa omogućenim Proton backup-om**: Instalirajte Proton Authenticator na novom uređaju. Tokom početnog podešavanja, prijavite se na isti Proton nalog. Aplikacija će odmah sinhronizovati i preuzeti sve vaše 2FA kodove iz šifrovane rezervne kopije.



**Sa iCloud backup (iOS)**: Povežite novi iPhone/iPad sa istim Apple ID-jem i obavezno aktivirajte iCloud Keychain. Nakon instalacije Proton Authenticator-a, povežite se sa iCloud-om. Vaši kodovi bi trebalo da se sinhronizuju putem iCloud-a i pojave.



**Nema rezervne kopije u oblaku**: Moraćete ručno da uvezete svoje naloge. Ako ste izvezli rezervnu kopiju, koristite funkciju Uvoz u Proton Authenticator-u. U najgorem slučaju, ako niste imali rezervnu kopiju, moraćete da koristite rezervne kodove za svaku uslugu ili da kontaktirate podršku.



Proton Authenticator vam omogućava da izvezete svoje naloge u bilo kom trenutku, bilo kao šifrovanu datoteku ili kao QR kod sa više naloga. Ove opcije vam pružaju dodatnu sigurnost.



## Najbolje prakse



Korišćenje 2FA autentifikatora značajno poboljšava vašu sigurnost, ali određene najbolje prakse moraju biti poštovane:



### Sačuvaj svoje hitne kodove



Kada aktivirate 2FA na nekoj usluzi, često dobijate listu kodova za oporavak. Držite ih van telefona (na papiru, u šifrovanom menadžeru lozinki, itd.). U slučaju potpunog gubitka vašeg autentifikatora, ovi statični kodovi će vas spasiti.



### Nemojte mešati svoje lozinke i 2FA kodove



Primamljivo je koristiti menadžer lozinki koji takođe čuva TOTP-ove. Međutim, čuvanje lozinke i 2FA koda na istom mestu stvara jednu tačku slabosti i slabi dvostruku autentifikaciju. Za maksimalnu sigurnost, mnogi stručnjaci preporučuju razdvajanje dva faktora: lozinke u sigurnom menadžeru, a 2FA kodove u zasebnoj aplikaciji kao što je Proton Authenticator. Ipak, korišćenje integrisanog menadžera je i dalje bolje nego nemati 2FA uopšte.



### Aktivirajte nekoliko metoda 2FA



Idealno je koristiti više od jednog drugog faktora na vašim kritičnim nalozima. Ne ustručavajte se dodati fizički sigurnosni ključ ako to usluga omogućava. Pogledajte naš vodič o fizičkim ključevima Yubikey za više informacija:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Isto tako, držite odštampane hitne kodove pri ruci.



### Ostani diskretan i zaštiti svoj uređaj



Ne dozvolite nikome da pretražuje vaš otključan telefon. Sa Proton Authenticator-om, vaši kodovi su zaštićeni PIN-om/biometrijom - ne otkrivajte ovaj PIN. Slično tome, pazite na phishing: čak i sa 2FA, ako date kod lažnom sajtu u realnom vremenu, napadač bi ga mogao iskoristiti.



### Ažuriranja i revizije



Ažurirajte Proton Authenticator redovno (ažuriranja ispravljaju moguće nedostatke). Kako je kod otvoren, zajednica sprovodi neformalne revizije, a Proton objavljuje rezultate formalnih revizija.



## Poređenje sa drugim aplikacijama



Kako se Proton Authenticator poredi sa drugim aplikacijama za autentifikaciju? Evo komparativnog pregleda:



**Proton Authenticator**: Otvoreni kod, opcioni E2EE šifrovani oblak za bekap, sinhronizacija na više uređaja, lokalno zaključavanje, bez praćenja, dostupno na mobilnim uređajima i desktopu.



**Google Authenticator**: Vlasnički, bekap putem Google naloga od 2023. ali bez end-to-end enkripcije (ključevi mogu biti vidljivi Google-u), sinhronizacija na više uređaja dodata 2023, nema zaključavanje aplikacije po defaultu, sadrži Google trackere.



**Aegis Authenticator**: Otvoreni kod, samo lokalna sigurnosna kopija, bez sinhronizacije sa oblakom, zaključavanje kodom/biometrijom, bez praćenja, samo za Android.



**Authy**: Vlasnički, lozinkom šifrovani cloud backup ali zatvoren kod, sinhronizacija na više uređaja, PIN zaključavanje/otisak prsta, prikuplja broj telefona, desktop aplikacija se ukida u martu 2024.



U nastavku ćete pronaći naš vodič za Authy:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator je jedno od najopsežnijih i najsigurnijih rešenja dostupnih: otvorenog koda, sinhronizacija šifrovana na više uređaja, bez komercijalnog praćenja.



## Resursi i podrška



### Službena dokumentacija




- **Zvanična veb stranica**: [proton.me/authenticator](https://proton.me/authenticator) - Predstavljanje proizvoda i preuzimanja
- **Stranica za preuzimanje**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Linkovi za sve operativne sisteme
- **Proton podrška**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Zvanični vodič za aktivaciju 2FA
- **Proton blog**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Najava i detaljne funkcije



### Izvorni kod i transparentnost




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Otvoreni izvorni kod
- **Bezbednosne provere**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Izveštaji nezavisnih revizija



### Preporučeni testovi bezbednosti


Nakon konfiguracije, testirajte vašu postavku:




- [Have I Been Pwned](https://haveibeenpwned.com/) - Proverite da li su vaši nalozi kompromitovani
- [2FA Directory](https://2fa.directory/) - Lista usluga koje podržavaju 2FA



### Zajednice i diskusije




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Zvanična Proton zajednica
- **Forum Privacy Guides**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Tehničke diskusije o pitanjima privatnosti
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Opšti saveti o privatnosti



### Drugo




- [Have I Been Pwned](https://haveibeenpwned.com/) - Proverite da li su vaši nalozi kompromitovani
- [2FA Directory](https://2fa.directory/) - Lista usluga koje podržavaju 2FA