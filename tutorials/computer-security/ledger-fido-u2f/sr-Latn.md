---
name: Ledger U2F & FIDO2
description: Poboljšajte svoju online sigurnost uz Ledger
---
![cover](assets/cover.webp)



Ledger uređaji su hardverski novčanici prvobitno dizajnirani za osiguranje Bitcoin Wallet, ali takođe imaju napredne opcije za snažnu autentifikaciju na vebu. Zahvaljujući njihovoj kompatibilnosti sa **U2F** i **FIDO2** protokolima, omogućavaju vam da osigurate pristup svojim online nalozima postavljanjem drugog faktora autentifikacije.



U2F (Universal 2nd Factor) protokol su uveli Google i Yubico 2014. godine, a zatim ga je standardizovala FIDO alijansa. Omogućava dodavanje drugog fizičkog faktora autentifikacije (2FA) prilikom prijavljivanja. Kada se aktivira, pored klasične lozinke, korisnici moraju odobriti svaki pokušaj povezivanja sa svojim nalogom pritiskom na dugme na svom Ledger. U ovom kontekstu, Ledger radi na sličan način kao Yubikey. U2F je zapravo podkomponenta FIDO2 standarda, obuhvatajući ga dok donosi značajna poboljšanja, uključujući podršku za moderne pretraživače i veću fleksibilnost u upravljanju ključevima za autentifikaciju.



Ove metode se zasnivaju na asimetričnoj kriptografiji: nikakvi tajni podaci se ne prenose, što čini phishing ili presretanje napada neefikasnim. U2F i FIDO2 sada podržava mnogo onlajn servisa.



U ovom vodiču pokazaćemo vam kako da aktivirate U2F i FIDO2 za dvofaktorsku autentifikaciju sa vašim Ledger.



**Napomena:** U2F i FIDO2 su podržani na svim Ledger uređajima opremljenim najnovijim firmware-om: od verzije 2.1.0 za Nano X i Nano S classic, i od verzije 1.1.0 za Nano S Plus. Stax i Flex modeli su nativno kompatibilni.



## Instalirajte aplikaciju Ledger Security Key



Ako koristite uređaj Ledger, verovatno znate da sam firmver ne sadrži sve funkcije potrebne za upravljanje kripto novčanicima. Na primer, da biste koristili Bitcoin Wallet, potrebno je da instalirate aplikaciju "*Bitcoin*". Slično tome, za upravljanje MFA ključevima, potrebno je da instalirate aplikaciju "*Security Key*".



Pre nego što počnete, uverite se da ste postavili svoj Bitcoin Wallet na svoj Ledger. Važno je da pravilno sačuvate svoj Mnemonic, jer se ključevi korišćeni za 2FA izvode iz ovog Mnemonic. Ako vaš Ledger bude izgubljen ili oštećen, možete povratiti pristup svojim ključevima unosom vaše Mnemonic fraze na drugi Ledger uređaj (za sada, FIDO2 identifikatori u "*passwordless*" režimu još uvek nisu podržani na Ledgerima, tako da nema rezidentnih identifikatora).



Povežite svoj Ledger sa računarom i otključajte ga.



![Image](assets/fr/01.webp)



Da biste instalirali aplikaciju, otvorite softver [Ledger Live] (https://www.Ledger.com/Ledger-live), zatim idite na karticu "*My Ledger*". Pronađite aplikaciju "*Security Key*" i instalirajte je na svoj uređaj.



![Image](assets/fr/02.webp)



Aplikacija "*Security Key*" sada bi trebalo da se pojavi zajedno sa ostalim aplikacijama instaliranim na vašem Ledger.



![Image](assets/fr/03.webp)



Kliknite na aplikaciju da biste je ostavili otvorenom za sledeće korake u vodiču.



![Image](assets/fr/04.webp)



## Koristite U2F/FIDO2 za 2FA sa Ledger



Pristupite nalogu koji želite da osigurate dvofaktorskom autentifikacijom. Na primer, koristiću Bitwarden nalog. Opciju za 2FA obično ćete pronaći u podešavanjima usluge, pod karticama "*authentication*", "*security*", "*login*" ili "*password*".



![Image](assets/fr/05.webp)



U odeljku posvećenom dvofaktorskoj autentifikaciji, izaberite opciju "*Passkey*" (termin može varirati u zavisnosti od sajta koji koristite).



![Image](assets/fr/06.webp)



Često će vam biti zatraženo da potvrdite vašu trenutnu lozinku.



![Image](assets/fr/07.webp)



Dajte svom sigurnosnom ključu ime radi lakšeg prepoznavanja, zatim kliknite na "*Pročitaj ključ*".



![Image](assets/fr/08.webp)



Detalji vašeg naloga će se pojaviti na Ledger ekranu. Pritisnite dugme "*Registruj*" da potvrdite (ili oba dugmeta istovremeno, u zavisnosti od modela koji koristite).



![Image](assets/fr/09.webp)



Ključ za pristup je uspešno registrovan.



![Image](assets/fr/10.webp)



Registrujte ovaj sigurnosni ključ.



![Image](assets/fr/11.webp)



Od sada, kada se prijavite na svoj nalog, pored uobičajene lozinke, bićete zamoljeni da povežete svoj Ledger.



![Image](assets/fr/12.webp)



Zatim možete pritisnuti dugme "*Log in*" na vašem Ledger ekranu da potvrdite autentifikaciju (ili oba dugmeta istovremeno, u zavisnosti od modela koji koristite).



![Image](assets/fr/13.webp)



Prednost korišćenja Hardware Wallet Ledger za dvofaktorsku autentifikaciju je što možete lako povratiti svoje ključeve zahvaljujući Mnemonic frazi. Pored ove osnovne rezervne kopije, možete koristiti i hitni kod koji obezbeđuje svaka usluga gde ste aktivirali 2FA. Ovaj hitni kod vam omogućava da se povežete na svoj nalog ako izgubite sigurnosni ključ. Stoga zamenjuje 2FA za povezivanje ako je potrebno.



Na primer, na Bitwardenu možete pristupiti ovom kodu klikom na "*View recovery code*".



![Image](assets/fr/14.webp)



Preporučujem da ovaj kod čuvate na drugom mestu od mesta gde čuvate svoju glavnu lozinku, kako biste sprečili da budu ukradeni zajedno. Na primer, ako je vaša lozinka sačuvana u menadžeru lozinki, čuvajte svoj 2FA hitni kod na papiru, odvojeno.



Ovaj pristup vam nudi dva nivoa bekapa u slučaju gubitka vašeg Ledger za 2FA autentifikaciju: prvi bekap koristeći Mnemonic frazu za sve vaše naloge, i drugi, specifičan za nalog, koristeći hitne kodove. Međutim, važno je **ne pomešati ulogu Mnemonic sa ulogom hitnog koda** :




- 12- ili 24-rečenična Mnemonic fraza vam daje pristup ne samo ključevima korišćenim za 2FA na svim vašim nalozima, već i vašim bitcoinima osiguranim sa vašim Ledger ;
- Hitni kod vam omogućava da privremeno zaobiđete zahtev za 2FA samo na dotičnom nalogu (u ovom primeru, samo na Bitwarden-u).



Čestitamo, sada ste u toku sa korišćenjem vašeg Ledger za MFA! Ako ste smatrali da je ovaj vodič koristan, bio bih veoma zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj vodič na vašim društvenim mrežama. Hvala vam puno!



Preporučio bih i ovaj drugi vodič, u kojem razmatramo drugo rešenje za U2F i FIDO2 autentifikaciju:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e