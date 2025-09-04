---
name: Trezor U2F & FIDO2
description: Ojačajte svoju online sigurnost uz Trezor
---
![cover](assets/cover.webp)



Trezor uređaji su hardverski novčanici prvobitno dizajnirani da osiguraju Bitcoin novčanik, ali takođe imaju napredne opcije za snažnu autentifikaciju na vebu. Zahvaljujući njihovoj kompatibilnosti sa **U2F** i **FIDO2** protokolima, omogućavaju vam da osigurate pristup vašim onlajn nalozima bez oslanjanja isključivo na lozinke.



U2F (*Universal 2nd Factor*) protokol su uveli Google i Yubico 2014. godine, a zatim ga je standardizovala FIDO alijansa. Omogućava dodavanje drugog fizičkog faktora autentifikacije (2FA) prilikom prijavljivanja. Kada se aktivira, pored klasične lozinke, korisnici moraju odobriti svaki pokušaj povezivanja sa svojim nalogom pritiskom na dugme na svom Trezoru. U ovom kontekstu, Trezor radi na sličan način kao Yubikey.



Ova metoda se zasniva na asimetričnoj kriptografiji: nikakvi tajni podaci se ne prenose, što čini phishing ili presretanje napada neefikasnim. U2F sada podržava mnogo online servisa.



Pored U2F, koji omogućava dvofaktorsku autentifikaciju, Trezori takođe podržavaju FIDO2 (*Fast IDentity Online 2.0*), evoluciju U2F-a. Ovo je standardizovani protokol autentifikacije iz 2018. godine, koji proširuje logiku U2F-a i ima za cilj da potpuno zameni lozinke. Bazira se na dva sastavna dela: WebAuthn (sa strane pregledača) i CTAP2 (sa strane fizičkog ključa). FIDO2 omogućava autentifikaciju bez lozinke: korisnici se identifikuju isključivo putem svog Trezor uređaja, koji deluje kao jedinstveni kriptografski token, bez dodatne lozinke. Ovaj protokol je sada kompatibilan sa brojnim onlajn servisima, posebno onima usmerenim ka preduzećima.



Pored funkcionalnosti "*passwordless* (prevod: bez lozinke)", FIDO2 takođe omogućava dvofaktorsku autentifikaciju na sličan način kao U2F.



FIDO2 takođe uvodi pojam rezidentnih kredencijala, tj. identifikatora koji su direktno uskladišteni u Trezoru, a koji uključuju i privatni ključ koji omogućava povezivanje i informacije o identifikaciji korisnika. Ovaj mehanizam omogućava autentifikaciju bez lozinke: jednostavno priključite svoj Trezor i potvrdite pristup, bez unosa ID-a ili lozinke. Suprotno tome, nerezidentni kredencijali, koji su konvencionalniji, skladište samo privatni ključ u uređaju; korisnički ID ostaje uskladišten na serverskoj strani i stoga se mora unositi pri svakom povezivanju. Kasnije ćemo pogledati kako ih sačuvati sa vašim Trezorom.



U ovom vodiču ćemo otkriti kako aktivirati U2F ili FIDO2 za dvofaktorsku autentifikaciju, a zatim kako konfigurisati FIDO2 za pristup vašim nalozima bez lozinke, direktno sa vašim Trezorom.



**Napomena:** U2F je kompatibilan sa svim Trezor modelima, ali FIDO2 je podržan samo na Safe 3, Safe 5 i Model T, ne na Model One.



## Korišćenje U2F/FIDO2 za 2FA na Trezoru



Pre nego što počnete, uverite se da ste podesili svoj Bitcoin novčanik na vašem Trezoru. Važno je da pravilno sačuvate vašu Mnemonic (bezbednosnu) frazu, jer se ključevi korišćeni za U2F i FIDO2 u dvofaktorskoj autentifikaciji izvode iz ove Mnemonic fraze. Ako vaš Trezor bude izgubljen ili oštećen, možete povratiti pristup vašim ključevima unosom vaše Mnemonic fraze na drugom Trezor uređaju (imajte na umu da za FIDO2 kredencijali u režimu "*bez lozinke*", samo seed nije dovoljan, kao što ćemo videti u narednim odeljcima).



Povežite svoj Trezor sa računarom i otključajte ga.



![Image](assets/fr/01.webp)



Pristupite nalogu koji želite da osigurate dvofaktorskom autentifikacijom. Na primer, koristiću Bitwarden nalog. Opciju za 2FA obično ćete pronaći u postavkama usluge, pod karticama "*authentication*", "*security*", "*login*" ili "*password*".



![Image](assets/fr/02.webp)



U odeljku posvećenom dvofaktorskoj autentifikaciji, izaberite opciju "*Passkey*" (termin može varirati u zavisnosti od sajta koji koristite).



![Image](assets/fr/03.webp)



Često će vam biti zatraženo da potvrdite vašu trenutnu lozinku.



![Image](assets/fr/04.webp)



Dajte svom sigurnosnom ključu ime radi lakšeg prepoznavanja, zatim kliknite na "*Read Key*".



![Image](assets/fr/05.webp)



Podaci o vašem nalogu će se pojaviti na Trezor ekranu. Dodirnite ekran ili pritisnite dugme da potvrdite. Takođe će vam biti zatraženo da potvrdite vaš PIN kod.



![Image](assets/fr/06.webp)



Registrujte ovaj sigurnosni ključ.



![Image](assets/fr/07.webp)



Od sada, kada želite da se povežete na svoj nalog, pored vaše uobičajene lozinke, bićete zamoljeni da povežete vaš Trezor.



![Image](assets/fr/08.webp)



Zatim možete pritisnuti ekran vašeg Trezora da potvrdite autentifikaciju.



![Image](assets/fr/09.webp)



Prednost korišćenja Trezor hardverskog novčanika za dvofaktorsku autentifikaciju je što možete lako povratiti svoje ključeve zahvaljujući Mnemonic frazi. Pored ove osnovne rezervne kopije, možete koristiti i hitni kod koji obezbeđuje svaka usluga gde ste aktivirali 2FA. Ovaj hitni kod vam omogućava da se povežete na svoj nalog ako izgubite sigurnosni ključ. Stoga zamenjuje 2FA za povezivanje ako je potrebno.



Na primer, na Bitwardenu možete pristupiti ovom kodu klikom na "*View recovery code*".



![Image](assets/fr/10.webp)



Preporučujem da ovaj kod čuvate na drugom mestu od mesta gde čuvate svoju glavnu lozinku, kako biste sprečili da budu ukradeni zajedno. Na primer, ako je vaša lozinka sačuvana u menadžeru lozinki, čuvajte svoj 2FA hitni kod na papiru, odvojeno.



Ovaj pristup vam nudi dva nivoa bekapa u slučaju gubitka vašeg Trezora za 2FA autentifikaciju: prvi bekap koristeći Mnemonic frazu za sve vaše naloge, i drugi specifičan za svaki nalog sa hitnim kodovima. Međutim, važno je **ne pomešati ulogu Mnemonic fraze sa ulogom hitnog koda**:




- Mnemonic fraza  od 12 ili 24 reči daje vam pristup ne samo ključevima korišćenim za 2FA na svim vašim nalozima, već i vašim bitcoinima osiguranim sa vašim Trezorom ;
- Hitni kod vam omogućava da privremeno zaobiđete zahtev za 2FA samo na dotičnom nalogu (u ovom primeru, samo na Bitwarden-u).



## Korišćenje FIDO2 na Trezoru



Pored dvofaktorske autentifikacije, FIDO2 takođe omogućava autentifikaciju bez lozinke, tj. bez potrebe za unosom lozinke prilikom prijavljivanja na sajt. Jednostavno povežite svoj Trezor sa računarom kako biste na ovaj način pristupili svom sigurnom nalogu. Evo kako da konfigurišete ovu funkciju.



Pre nego što počnete, uverite se da ste postavili svoj Bitcoin novčanik na vašem Trezor-u. Važno je sačuvati Mnemonic frazu, jer su FIDO2 "*passwordless*" identifikatori enkriptovani sa vašim seed-om (saznaćemo kako da pravilno sačuvamo ove identifikatore u sledećem odeljku).



Povežite Trezor sa računarom i otključajte ga.



![Image](assets/fr/01.webp)



Pristupite nalogu koji želite da osigurate u "*passwordless*" režimu. Koristiću Bitwarden nalog kao primer. Ova opcija se obično nalazi u podešavanjima usluge, često pod karticom "*authentication*", "*security*" ili "*password*".



Na primer, na Bitwardenu se opcija nalazi pod karticom "*Master password*". Kliknite na "*Turn on*" da biste aktivirali autentifikaciju putem FIDO2.



![Image](assets/fr/11.webp)



Često će vam biti zatraženo da potvrdite svoju lozinku.



![Image](assets/fr/12.webp)



Detalji vašeg naloga će se pojaviti na Trezor ekranu. Dodirnite ekran ili pritisnite dugme da potvrdite. Takođe ćete morati da potvrdite svoj PIN kod.



![Image](assets/fr/13.webp)



Na sajtu, dodajte ime da biste zapamtili svoj sigurnosni ključ, zatim kliknite na "*Turn on*".



![Image](assets/fr/14.webp)



Zatim će vam biti zatraženo da se identifikujete kako biste proverili da li ključ ispravno radi.



![Image](assets/fr/15.webp)



Od sada, kada se prijavljujete na svoj nalog, više neće biti potrebno unositi vašu email adresu ili prijavu. Jednostavno kliknite na dugme da se autentifikujete fizičkim ključem na obrascu za prijavu.



![Image](assets/fr/16.webp)



Potvrdite vezu sa vašim Trezorom unosom vašeg PIN-a na hardverskom novčaniku.



![Image](assets/fr/17.webp)



Bićete povezani sa svojim nalogom bez potrebe da unosite lozinku.



![Image](assets/fr/18.webp)



**Imajte na umu da čak i ako aktivirate autentifikaciju bez lozinke putem FIDO2 na vašem Trezoru, glavna lozinka za vaš online nalog će i dalje biti važeća za prijavljivanje**



## Sačuvaj svoje FIDO2 kredencijale (rezidentne kredencijale)



Ako koristite FIDO2 ili U2F za dvofaktorsku autentifikaciju, tj. za prijavljivanje na naloge koji zahtevaju lozinku pored 2FA validacije putem vašeg Trezora, tada će sama Mnemonic fraza omogućiti pristup vašim ključevima. Međutim, ako koristite FIDO2 u "*bezlozinskom*" režimu kao što je opisano u prethodnom odeljku, biće potrebno napraviti kopiju vaših FIDO kredencijala pored pravljenja rezervne kopije vaše Mnemonic fraze koja šifruje te kredencijale.



Da biste to uradili, potreban vam je računar sa instaliranim Python-om. Otvorite terminal i pokrenite sledeću komandu da instalirate neophodan Trezor softver:



```shell
pip3 install --upgrade trezor
```



Povežite svoj Trezor sa računarom putem USB-a i otključajte ga koristeći svoj PIN kod.



![Image](assets/fr/01.webp)



Da biste preuzeli listu FIDO2 identifikatora sačuvanih na Trezoru, pokrenite sledeću komandu:



```shell
trezorctl fido credentials list
```



Potvrdite izvoz na vašem Trezoru.



![Image](assets/fr/19.webp)



Vaši FIDO2 podaci za prijavu će biti prikazani na vašem terminalu. Na primer, za moj Bitwarden nalog, dobio sam ove informacije:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Kopiraj i sačuvaj sve ove informacije u tekstualnu datoteku. Ne postoji značajan rizik povezan sa ovom rezervnom kopijom, osim otkrivanja da koristite ove usluge sa FIDO2. "*ID kredencijala*" je šifrovan korišćenjem vašeg seed-a novčanika, što znači da napadač koji dobije ovu rezervnu kopiju ne bi mogao da se poveže na vaše naloge, već samo da primeti da koristite ove naloge. Da biste dešifrovali ove ID-ove, potreban vam je seed u vašem novčaniku.



Stoga možete kreirati nekoliko kopija ovog tekstualnog fajla i čuvati ih na različitim mestima, na primer lokalno na vašem računaru, na servisu za hosting fajlova i na eksternim medijima kao što je USB stik. Međutim, imajte na umu da ova rezervna kopija nije automatski ažurirana, tako da ćete morati da je obnovite svaki put kada uspostavite novu "*passwordless*" vezu sa vašim Trezorom.



Sada zamislimo da ste pokvarili svoj Trezor. Da biste povratili svoje FIDO2 kredencijale, prvo ćete morati da povratite svoj novčanik koristeći svoju Mnemonic frazu na novom FIDO2-kompatibilnom Trezor uređaju.



Kada se oporavak završi, da biste uvezli svoje FIDO2 identifikatore na novom uređaju, pokrenite sledeću komandu u svom terminalu:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Jednostavno zamenite `<CREDENTIAL_ID>` jednim od vaših identifikatora. Na primer, u mom slučaju, ovo bi bilo:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Vaš Trezor će vas upitati da uvezete svoj FIDO2 identifikator. Potvrdite pritiskom na ekran.



![Image](assets/fr/20.webp)



Vaš FIDO2 prijava sada je operativna na vašem Trezoru. Ponovite ovaj postupak za svaki od vaših identifikatora.



Čestitamo, sada ste u toku sa korišćenjem vašeg Trezora sa U2F i FIDO2! Ako vam je ovaj vodič bio koristan, bio bih veoma zahvalan ako biste pritisnuli zeleni palac ispod. Slobodno podelite ovaj vodič na vašim društvenim mrežama. Hvala vam puno!



Preporučio bih i ovaj drugi vodič, u kojem razmatramo drugo rešenje za U2F i FIDO2 autentifikaciju:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e
