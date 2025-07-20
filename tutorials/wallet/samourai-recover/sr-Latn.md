---
name: Samourai Wallet - Oporavak
description: Kako povratiti bitkoine zaglavljene na Samourai Wallet?
---

![cover](assets/cover.webp)


Nakon hapšenja osnivača Samourai Wallet i zaplene njihovih servera 24. aprila, neke funkcionalnosti aplikacije su sada neoperativne, a korisnici koji nemaju svoj Dojo više ne mogu emitovati transakcije.


Nakon što sam pomogao nekoliko korisnika u oporavku njihovih bitcoina u poslednjim danima, verujem da sam naišao na većinu problema koji se mogu pojaviti tokom obnove Samourai Wallet. Stoga će ovaj vodič započeti izveštajem o situaciji kako bi se identifikovale funkcionalnosti koje ostaju operativne i one koje više nisu dostupne unutar Samourai Wallet ekosistema i softvera pogođenog ovim incidentom. Zatim ćemo korak po korak nastaviti sa oporavkom Samourai Wallet koristeći Sparrow Wallet softver. Ispitaćemo sve potencijalne prepreke na koje se može naići tokom ovog procesa i videti rešenja za njihovo rešavanje. Na kraju, u poslednjem delu, otkrićete potencijalne rizike po vašu privatnost nakon zaplene servera.


_Veliko hvala [@Louferlou](https://twitter.com/Louferlou), koji je pomogao mnogim korisnicima u njihovom oporavku i podelio svoja iskustva sa mnom, a takođe je doprineo testiranju kako bi se utvrdilo šta još uvek funkcioniše._


## Da li Samourai Wallet još uvek radi?


Da, **aplikacija Samourai Wallet i dalje radi**, ali pod određenim uslovima.


Prvo, neophodno je da je aplikacija prethodno bila instalirana na vašem pametnom telefonu. Google Play Store je uklonio aplikaciju, a APK je bio hostovan na zaplenjenom sajtu. Stoga je trenutno komplikovano instalirati Samourai. Možda ćete pronaći APK-ove na internetu, ali savetujem da ih ne preuzimate osim ako niste sigurni u izvor.


S obzirom na to da stranica Samourai Wallet više nije dostupna na Google Play Store-u, nije moguće onemogućiti automatska ažuriranja. Ako se aplikacija vrati na platforme za preuzimanje, bilo bi pametno **onemogućiti automatska ažuriranja** dok ne bude dostupno više informacija o razvoju slučaja.


Ako je Samourai Wallet već instaliran na vašem pametnom telefonu, i dalje biste trebali moći pristupiti aplikaciji. Da biste koristili Wallet funkcionalnost Samouraia, neophodno je povezati Dojo. Prethodno su korisnici bez ličnog Dojo-a zavisili od Samouraievih servera za pristup Bitcoin Blockchain informacijama i za emitovanje transakcija. Sa zaplenom ovih servera, aplikacija više ne može pristupiti ovim podacima.

Ako ranije niste imali povezan Dojo, ali ga sada imate, možete ga podesiti da ponovo koristite svoju Samourai aplikaciju. Ovo uključuje proveru vaših rezervnih kopija, brisanje Wallet (Wallet, ne aplikaciju), i obnavljanje Wallet povezivanjem vašeg Dojo-a sa aplikacijom. Za više detalja o ovim koracima, možete pogledati [ovaj vodič, u odeljku "_Priprema vašeg Samourai Wallet-a_" : CoinJoin - DOJO](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2).

Ako je vaša Samourai aplikacija već bila povezana sa vašim sopstvenim Dojo-om, onda Wallet deo savršeno funkcioniše za vas. Još uvek možete videti svoj saldo i emitovati transakcije. Uprkos svemu što se dešava, mislim da Samourai Wallet ostaje najbolji mobilni Wallet softver trenutno. Lično, planiram da ga i dalje koristim.


Glavni problem na koji možete naići je nepristupačnost Whirlpool naloga iz aplikacije. Obično, Samourai pokušava da uspostavi vezu sa vašim Whirlpool CLI i započne CoinJoin cikluse pre nego što vam omogući pristup ovim nalozima. Međutim, pošto ova veza više nije moguća, aplikacija nastavlja da pretražuje beskonačno, a da vam nikada ne omogući pristup Whirlpool nalozima. U tom slučaju, možete povratiti ove naloge na drugom Wallet softveru dok samo zadržavate depozitni nalog na Samourai.


### Koji alati su još uvek dostupni na Samourai?


S druge strane, neki alati su ili pogođeni gašenjem servera ili potpuno nedostupni.


Što se tiče alata za individualnu potrošnju, sve funkcioniše normalno pod uslovom, naravno, da imate svoj Dojo. Normalne Stonewall transakcije (a ne Stonewall x2) rade bez ikakvih problema.


Komentari na Twitteru su istakli da privatnost koju nudi Stonewall transakcija sada može biti smanjena. Dodata vrednost Stonewall transakcije leži u činjenici da je neodvojiva od Stonewall x2 transakcije u smislu strukture. Kada analitičar naiđe na ovaj specifičan obrazac, ne može odrediti da li je u pitanju standardni Stonewall sa jednim korisnikom ili Stonewall x2 koji uključuje dva korisnika. Međutim, kao što ćemo videti u narednim pasusima, sprovođenje Stonewall x2 transakcija postalo je složenije zbog nedostupnosti Sorobana. Neki stoga misle da bi analitičar sada mogao pretpostaviti da je svaka transakcija sa ovom strukturom normalan Stonewall. Lično, ne delim ovu pretpostavku. Iako Stonewall x2 transakcije mogu biti ređe (i mislim da su već bile pre ovog incidenta), činjenica da su i dalje moguće može poništiti celu analizu zasnovanu na pretpostavci da nisu.

**[-> Saznajte više o Stonewall transakcijama.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**

Što se tiče Ricochet-a, nisam bio u mogućnosti da proverim da li je usluga još uvek operativna, jer ne posedujem Dojo na Testnet, i radije ne bih rizikovao da potrošim `100 000 Sats` na Wallet koji bi mogao biti pod kontrolom vlasti. Ako ste imali priliku da nedavno testirate ovaj alat, pozivam vas da me kontaktirate kako bismo mogli ažurirati ovaj članak.


Ako treba da koristiš Ricochet, budi svestan da uvek možeš da izvršiš ovu operaciju ručno sa bilo kojim Wallet softverom. Da bi naučio kako da ručno pravilno izvršiš razne skokove, preporučujem da pogledaš ovaj drugi članak: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589)


Alat JoinBot više nije operativan, jer je u potpunosti zavisio od učešća Wallet kojim je upravljao Samourai.


Što se tiče drugih vrsta kolaborativnih transakcija, često nazivanih "cahoots", one ostaju moguće, ali samo ručno. Pre gašenja servera, imali ste dve opcije za izvođenje Stonewall x2 ili Stowaway (PayJoin) transakcija:



- Koristite Soroban mrežu za automatsko i daljinsko Exchange PSBT-ove;
- Ili izvršite ove razmene ručno skeniranjem više QR kodova.


Nakon nekoliko testova, čini se da Soroban više ne funkcioniše. Da bi se izvršile ove kolaborativne transakcije, Exchange podataka mora se stoga obaviti ručno. Evo dve opcije za izvođenje ovog Exchange:



- Ako ste fizički blizu svog saradnika, možete skenirati QR kodove uzastopno;
- Ako ste udaljeni od svog saradnika, možete Exchange PSBT-ove putem spoljnog komunikacionog kanala do aplikacije. Međutim, budite oprezni, jer su podaci sadržani u ovim PSBT-ovima osetljivi u smislu privatnosti. Preporučujem korišćenje šifrovane usluge za razmenu poruka kako biste osigurali poverljivost Exchange.


**[-> Saznajte više o Stonewall x2 transakcijama.](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)**


**[-> Saznajte više o Stowaway transakcijama.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**


Što se tiče Whirlpool, čini se da protokol više ne funkcioniše, čak ni za korisnike koji imaju svoj Dojo. Posmatrao sam svoj RoninDojo ovih poslednjih nekoliko dana i pokušao neke osnovne manipulacije, ali Whirlpool CLI nije bio u mogućnosti da se poveže od kada je server ugašen.


Međutim, ostajem optimističan da se ovaj protokol može ponovo aktivirati ili možda drugačije osmisliti u narednim nedeljama, u zavisnosti od toga kako se situacija razvija. Ova pauza bi mogla biti prilika da se istraže novi pristupi ili potencijalna poboljšanja ovog sistema.


### Koji su spoljašnji alati još uvek dostupni?


Što se tiče drugih alata povezanih sa Samourai okruženjem, neki su još uvek dostupni dok drugi nisu.


Besplatna veb stranica za analizu lanaca OXT.me nažalost trenutno nije dostupna.


Whirlpool Stats Tool više nije dostupan za preuzimanje, jer je bio hostovan na Samourai-evom GitLab-u. Čak i ako ste prethodno preuzeli ovaj Python alat lokalno na vašem računaru, ili ako je bio instaliran na vašem RoninDojo čvoru, WST trenutno neće raditi. Naime, zavisio je od podataka koje je pružao OXT.me za svoje funkcionisanje, a ovaj sajt više nije dostupan. Trenutno, WST nije posebno koristan jer je Whirlpool protokol neaktivan.


Sajt KYCP.org trenutno više nije dostupan.


GitLab koji je hostovao kod za Boltzmann Calculator Python alat je takođe zaplenjen. U ovom trenutku, stoga više nije moguće preuzeti ovaj alat. Ali ako imate RoninDojo, možete nastaviti da koristite Boltzmann Calculator na isti način kao i ranije.


Što se tiče RoninDojo-a, ovaj softver za node-in-box nastavlja da funkcioniše ispravno uprkos nedostupnosti određenih specifičnih alata kao što su Whirlpool CLI i WST. I dalje se može koristiti za drugi Wallet softver zahvaljujući Fulcrum-u ili Electrs-u. Ako želite da dobijete više informacija o RoninDojo-u ili ako imate specifična pitanja, preporučujem vam da se pridružite [njihovoj Telegram grupi](https://t.me/RoninDojoNode).


Međutim, izvorni kod za RoninDojo trenutno više nije dostupan, jer je bio hostovan na Samourai-ovom GitLab-u. Stoga trenutno nije moguće ručno ga instalirati na Raspberry Pi.


Što se tiče softvera Watch-only wallet Sentinel, situacija je slična onoj sa aplikacijom Samourai. Ako imate svoj Dojo, možete nastaviti koristiti Sentinel bez ikakvih problema. Međutim, ako nemate Dojo, više nećete moći uspostaviti vezu. Za razliku od Samourai, Sentinel vebsajt je i dalje dostupan online. Ali budite oprezni sa ovim sajtom i APK-om koji se tamo nudi, jer nije jasno ko trenutno kontroliše te resurse.


### Da li je Sparrow Wallet pogođen?


Sparrow Wallet nastavlja da radi normalno, sa izuzetkom Samourai alata koji više nisu dostupni. Trenutno više nije moguće izvoditi coinjoin transakcije putem Sparrow-a. Slično tome, alati za kolaborativno trošenje više nisu dostupni, jer Sparrow ne nudi opciju ručnog Exchange PSBT-ova, za razliku od Samourai-a. Za sve ostale funkcionalnosti, Sparrow radi bez problema. Takođe možete koristiti ovaj softver za oporavak Samourai Wallet ako je potrebno.


## Kako povratiti Samourai Wallet?


Kao što smo videli u prethodnim odeljcima, ako posedujete svoj Dojo, nije nužno potrebno menjati softver. **Samourai ostaje odličan izbor Hot Wallet** za vaše svakodnevne troškove. Međutim, ako nemate Dojo ili ako više volite da se odlučite za drugi softver, objasniću kompletan proces oporavka, detaljno navodeći sve potencijalne prepreke na koje možete naići.


U svakom slučaju, važno je da odvojite vreme i osigurate da ne napravite greške. Zapamtite, nema žurbe, jer vi držite svoje privatne ključeve, a zaplena Samourai servera ne utiče na to ni na koji način. Šta god da se desi, očigledno je da ne mogu pristupiti vašim privatnim ključevima.


### Verifikuj passphrase


Da biste povratili svoj Wallet, morate imati svoj passphrase, čak i ako se odlučite za oporavak putem rezervne datoteke. Počnite proverom validnosti ovog passphrase. Otvorite svoju Samourai Wallet aplikaciju, kliknite na svoju Paynym ikonu u gornjem levom uglu, zatim izaberite `Settings`.


![samourai](assets/1.webp)


Zatim, kliknite na `Troubleshooting` a zatim na `passphrase/backup test`.


![samourai](assets/2.webp)


Unesite svoj passphrase i kliknite `Ok`. Ako je ispravan, Samurai će ga potvrditi. Takođe imate opciju da verifikujete rezervnu datoteku ako planirate da je koristite kasnije.


![samourai](assets/3.webp)


Ovaj korak je opcionalan, ali preporučen. Potvrđuje da je passphrase ispravan, eliminišući potencijalni izvor problema kasnije. Ako Samourai naznači da je passphrase neispravan u ovoj fazi, oporavak neće biti moguć. Uverite se da ste uneli passphrase ispravno i proverite ga ponovo.


### Opcija 1: Oporavi Wallet na Sparrow pomoću rezervne kopije


Od verzije 1.8.6 Sparrow Wallet, moguće je direktno uvesti vaš Samourai Wallet koristeći rezervnu tekstualnu datoteku pod nazivom `samourai.txt`, koju vaša aplikacija automatski generiše. Ova datoteka sadrži sve potrebne informacije za oporavak vašeg Wallet i šifrovana je vašim passphrase radi sigurnosti.


Ako izaberete ovu opciju, biće vam potreban vaš ažurirani `samourai.txt` fajl i vaš passphrase. Da biste generate ovaj fajl na Samourai Wallet, kliknite na tri mala tačkice u gornjem desnom uglu, zatim izaberite `Export Wallet backup`.


![samourai](assets/4.webp)

Dalje, izaberite `Export to Clipboard`. Nakon toga, biće potrebno da ovaj fajl prenesete na vaš PC na siguran način. Pošto je fajl enkriptovan, ali je passphrase dovoljan da ga dekriptuje, važno je preduzeti mere opreza tokom prenosa. Ako se odlučite za direktan prenos kao običan tekst, potrebno je da kreirate `samourai.txt` fajl na vašem PC-ju i nalepite sadržaj iz clipboard-a u njega. Alternativa bi bila da direktno preuzmete `samourai.txt` fajl iz fajlova sačuvanih na vašem telefonu.

Kada imate pristup datoteci na vašem računaru, otvorite Sparrow Wallet, kliknite na karticu `File`, i izaberite `Import Wallet` da biste započeli uvoz vašeg Wallet.


![samourai](assets/5.webp)


Pomeri se dole do `Samourai Backup`, klikni na `Import File`, a zatim izaberi svoj `samourai.txt` fajl.


![samourai](assets/6.webp)


Sparrow će vas zatim tražiti lozinku za dešifrovanje datoteke. Ova lozinka je zapravo vaš passphrase. Unesite je u odgovarajuće polje i kliknite na `Import`.


![samourai](assets/7.webp)


Ako se u ovoj fazi vaš Wallet ne pojavi, moguće je da ste napravili grešku prilikom kopiranja datoteke `samourai.txt` ili prilikom unosa passphrase. Možete se obratiti odeljku za rešavanje problema za dodatnu pomoć.


![samourai](assets/8.webp)


Za tip skripte, ako niste konfigurisali druge skripte u Samourai, obično bi trebalo da koristite samo SegWit V0 (Native SegWit / P2WPKH). Zadržite ovu podrazumevanu skriptu i kliknite na `Import`.


![samourai](assets/9.webp)


Nazovite svoj Wallet, na primer, "Samourai Recovery", a zatim kliknite na `Create Wallet`.


![samourai](assets/10.webp)


Sparrow će vas zatim zamoliti da izaberete lozinku. Ova lozinka štiti samo pristup vašem Wallet na ovom računaru i ne odnosi se na derivaciju ključeva vašeg Wallet. Obavezno izaberite jaku lozinku, zapišite je da biste je zapamtili, i kliknite na `Set Password`.


![samourai](assets/11.webp)


Sparrow će zatim izvesti ključeve vašeg Wallet i pretražiti odgovarajuće transakcije.


![samourai](assets/12.webp)


Za sada je dostupan samo vaš depozitni račun. Ako ste koristili Samourai samo za ovaj račun, trebali biste videti sva svoja sredstva. Međutim, ako ste takođe koristili Whirlpool, moraćete da izvedete `premix`, `postmix` i `badbank` račune. Na Sparrow-u, jednostavno kliknite na karticu `Settings`, zatim na `Add Accounts...`.


![samourai](assets/13.webp)

U prozoru koji se otvori, izaberite `Whirlpool Accounts` iz padajućeg menija, zatim kliknite na `OK`.

![samourai](assets/14.webp)


Videćete zatim vaše različite Whirlpool naloge, a Sparrow će izvesti potrebne ključeve za korišćenje povezanih bitkoina.


![samourai](assets/15.webp)


Ako koristite drugi softver osim Sparrow-a, kao što je Electrum, za oporavak vašeg Samourai Wallet, ovde su Whirlpool indeksi naloga za ručni oporavak:



- Depozit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


Sada imate pristup svojim bitcoinima na Sparrow. Ako vam je potrebna pomoć pri korišćenju Sparrow Wallet, možete pogledati i [naš posvećeni vodič](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).


Takođe preporučujem ručno uvoz etiketa koje ste povezali sa vašim UTXO-ima na Samourai. Ovo će vam omogućiti efikasnu kontrolu novčića na Sparrow-u naknadno.


### Opcija 2: Povrati Wallet na Sparrow sa frazom Mnemonic


Ako ne želite da izvršite oporavak pomoću rezervne datoteke, možete se odlučiti za tradicionalniju metodu jednostavnim korišćenjem vaše 12-reči fraze za oporavak i vašeg passphrase. Ova druga opcija je često jednostavnija.


Za početak, uverite se da imate svoju frazu za oporavak i svoj passphrase pri ruci. Zatim, otvorite Sparrow Wallet softver, kliknite na karticu `File`, i izaberite `Import Wallet` da biste započeli uvoz vašeg Wallet.


![samourai](assets/16.webp)


Izaberite `Mnemonic Words (BIP39)` i, u padajućem meniju, kliknite na `Use 12 Words`.


![samourai](assets/17.webp)


Unesite 12 reči vaše fraze za oporavak redosledom kojim idu.


![samourai](assets/18.webp)


Ako Sparrow prikaže poruku `Invalid Checksum`, to ukazuje da kontrolni zbir fraze za oporavak nije važeći, što verovatno znači da ste napravili grešku prilikom unosa reči.


![samourai](assets/19.webp)


Ako je vaša fraza tačna, označite polje `Koristiti passphrase?` i unesite vaš passphrase u predviđeno polje. Na kraju, ako sve izgleda ispravno, kliknite na dugme `Otkrij Wallet`.


![samourai](assets/20.webp)


Nazovite svoj Wallet, na primer, "Samourai Recovery", zatim kliknite na `Create Wallet`.


![samourai](assets/21.webp)

Sparrow će vas zatim zamoliti da izaberete lozinku. Ova lozinka štiti pristup vašem Wallet na ovom računaru i nije povezana sa derivacijom ključeva vašeg Wallet. Uverite se da ste izabrali jaku lozinku, zapišite je da biste je zapamtili, i kliknite na `Set Password`.

![samourai](assets/22.webp)


Sparrow će zatim izvesti ključeve za vaš Wallet i tražiti odgovarajuće transakcije.


![samourai](assets/23.webp)


Ako se u ovoj fazi vaš Wallet ne pojavi, moguće je da ste napravili grešku prilikom unosa passphrase ili fraze za oporavak. Možete se obratiti posvećenom odeljku za rešavanje problema za dodatnu pomoć.


Za sada je dostupan samo vaš depozitni račun. Ako ste koristili Samourai samo za ovaj račun, trebalo bi da vidite sva vaša sredstva. Međutim, ako ste takođe koristili Whirlpool, biće potrebno da izvedete `premix`, `postmix` i `badbank` račune. Na Sparrow-u, jednostavno kliknite na karticu `Settings`, zatim na `Add Accounts...`.


![samourai](assets/24.webp)


U prozoru koji se otvori, izaberite `Whirlpool Accounts` iz padajuće liste, zatim kliknite na `OK`.


![samourai](assets/25.webp)


Videćete zatim vaše različite Whirlpool naloge, a Sparrow će izvesti potrebne ključeve za korišćenje povezanih bitkoina.


![samourai](assets/26.webp)


Ako koristite drugi softver poput Electrum-a za oporavak vašeg Samourai Wallet, ovde su Whirlpool indeksi naloga za ručni oporavak:



- Depozit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


Sada imate pristup svojim bitcoinima na Sparrow. Ako vam je potrebna pomoć pri korišćenju Sparrow Wallet, možete se obratiti i [našem posvećenom vodiču](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).


Takođe preporučujem ručno uvoz etiketa koje ste povezali sa vašim UTXO-ima na Samourai. Ovo će vam omogućiti efikasnu kontrolu novčića na Sparrow-u naknadno.


### Koji su uobičajeni problemi na koje se nailazi?


Nakon što sam pomogao nekoliko ljudi u proteklih nekoliko dana, verujem da sam naišao na većinu problema koji mogu sprečiti oporavak vašeg Wallet. Ako i dalje ne možete pristupiti svom Wallet uprkos prethodnim tutorijalima, evo nekoliko dodatnih preporuka.

Prvo i najvažnije, da bi oporavak bio uspešan, apsolutno je neophodno da fraza za oporavak bude tačna. Ako niste u mogućnosti da pronađete svoju frazu od 12 reči, možete koristiti _opcija 1_ za oporavak iz Samourai rezervne datoteke. Takođe možete pristupiti svojoj frazi za oporavak direktno u Samourai Wallet tako što ćete otići na `Settings`, zatim `Wallet`, i na kraju odabrati `Show 12-word recovery phrase`.


Zatim, greška u kucanju u vašem passphrase tokom oporavka će rezultirati netačnim izvedenim ključevima, što će sprečiti oporavak vašeg Wallet na Sparrow. **passphrase mora biti savršeno tačan!**


Da biste to rešili, prvo vam savetujem da proverite validnost vašeg passphrase u aplikaciji Samourai kao što je opisano u odeljku "_Verify the passphrase_" ovog članka:


1. **Validacija u Samourai:** Ako Samourai potvrdi da je passphrase tačan, pokušajte ponovo oporavak od početka, pazeći da tačno unesete passphrase u Sparrow bez greške;

2. **passphrase Greška:** Ako Samourai ukazuje da je passphrase netačan, besmisleno je nastaviti pokušaje na Sparrow. Dok se ne pronađe tačan passphrase, oporavak vašeg Wallet je nemoguć. Ako ste trajno izgubili svoj passphrase, čuvajte svoju Samourai aplikaciju. Sve što možete da uradite je da se nadate da će serveri biti restartovani kako biste mogli da vršite troškove direktno iz aplikacije bez potrebe za oporavkom. **Ne pokušavajte da povežete Dojo u ovom slučaju**, jer bi to podrazumevalo resetovanje vašeg Wallet na Samourai, što zahteva pristup passphrase.


Među ostalim uočenim greškama, mnoge su povezane sa mrežnom konfiguracijom na Sparrow.


Prvo, osigurajte da je Sparrow ispravno konfigurisan u `Mainnet` modu umesto u `Testnet` modu. Naime, ako Sparrow traži vaše transakcije na Testnet, neće pronaći ništa, jer je vaš Wallet na Mainnet. Testnet je alternativna verzija Bitcoin, koja se koristi isključivo za testiranje i razvoj, i radi na zasebnoj mreži od glavne mreže (Mainnet), sa sopstvenim blokovima i transakcijama. Da biste proverili na kojoj mreži se nalazite, kliknite na karticu `Tools`, zatim na `Restart In`. Ako je prikazana opcija `Mainnet`, onda niste na glavnoj mreži. Izaberite je da ponovo pokrenete Sparrow na Mainnet, a zatim ponovo započnite proces oporavka.


![samourai](assets/27.webp)

Neki su takođe naišli na poteškoće pri povezivanju Sparrow-a sa svojim čvorom. U donjem desnom uglu Sparrow-a, obojeni prekidač pokazuje da li je vaš softver pravilno povezan sa Bitcoin čvorom. Da biste preuzeli svoje Samourai transakcije, neophodno je da softver bude dobro povezan. Proverite da li je prekidač aktiviran, kao na mojoj slici ispod (žuto za javni čvor, Green za Bitcoin Core, i plavo za Electrum server).

![samourai](assets/28.webp)


Ako prekidač nije aktiviran, kliknite na njega da ponovo aktivirate vezu.


![samourai](assets/29.webp)


Ako problem potraje, evo nekoliko mogućih rešenja:



- Ako pokušavate da se povežete sa sopstvenim Electrum serverom (plavi) ili vašim Bitcoin Core (Green) i Sparrow ne može da se poveže, proverite informacije o vezi pod `File > Preferences... > Server`;


![samourai](assets/30.webp)



- Ako problem sa vezom i dalje postoji, to može biti zbog nepotpune sinhronizacije vašeg čvora. Osigurajte da su vaš čvor i vaš indeksator 100% sinhronizovani. Ako je potrebno, kao poslednje sredstvo, isključite vaš čvor iz Sparrow-a i povežite se na javni čvor;
- Ako ste već bili povezani na javni čvor i veza ne uspe, pokušajte promeniti čvor odabirom drugog sa padajuće liste.


![samourai](assets/31.webp)


Ako ste uspešno povratili svoj Wallet, ali izgleda nepotpuno, možda postoji problem vezan za derivaciju.


Problem može nastati ako koristite svoj Samourai depozitni račun sa drugačijim tipom skripte od `P2WPKH`. Podrazumevano, Samourai koristi ovaj tip skripte, ali ako ste ga ručno promenili, morate ga takođe prilagoditi prilikom oporavka na Sparrow.


Da biste izveli grane za druge tipove skripti, potrebno je da ponovite proces oporavka za svaki korišćeni tip skripte. Za ovo, idite na `File > New Wallet` na Sparrow, izaberite drugi tip skripte iz padajuće liste, kliknite na `New or Imported Software Wallet`, i pratite iste korake kao u početnom vodiču.


![samourai](assets/32.webp)


Još jedan problem sa derivacijom na koji sam naišao odnosi se na vrednost Gap Limit. Ova vrednost govori Sparrow-u nakon koliko praznih adresa treba da prestane sa derivacijom novih adresa. Ako nakon oporavka primetite da nedostaju neke transakcije, to može biti zbog preniske vrednosti Gap Limit-a. Da biste to rešili, idite na nalog koji uzrokuje problem, na primer, postmix nalog (ako je u pitanju više naloga, ponovite ovu operaciju za svaki).


![samourai](assets/33.webp)


Kliknite na karticu `Settings`, a zatim na dugme `Advanced...`.

![samourai](assets/34.webp)

Postepeno povećavajte vrednost Gap Limita, na primer, ovde sam ga postavio na `400`. Zatim, kliknite na dugme `Close`.


![samourai](assets/35.webp)


Kliknite na `Apply` da završite. Sparrow će zatim izvesti veći broj adresa i tražiti sredstva na njima, što bi trebalo pomoći u oporavku svih vaših transakcija.


![samourai](assets/36.webp)


To pokriva razne probleme sa oporavkom na koje sam naišao u poslednjih nekoliko dana. Ako, nakon što isprobaš sva ova rešenja, i dalje imaš problema, pozivam te da se pridružiš [Discover Bitcoin Discordu](https://discord.gg/xKKm29XGBb) kako bi zatražio pomoć. Redovno posećujem ovaj Discord i biće mi drago da pomognem ako imam rešenje. Drugi bitkoineri će takođe moći da podele svoja iskustva i ponude svoju pomoć. **U svakom slučaju, neophodno je da čuvaš svoju frazu za oporavak, rezervnu datoteku i passphrase poverljivo**. Ne deli ih ni sa kim, jer bi to moglo omogućiti da ti ukradu bitkoine.


Jednom kada je oporavak završen, sada imate pristup svojim bitcoinima. To je dobra stvar, ali možda neće biti dovoljno. Zaista, zaplena servera otvara nove potencijalne rizike za vašu privatnost. U sledećem odeljku ćemo detaljno ispitati ove rizike i navesti mere predostrožnosti koje treba preduzeti kako biste zaštitili svoju privatnost.


## Koje su posledice po privatnost vaših transakcija?


### Kao korisnik Samourai bez Dojo


Ako ste koristili Samourai Wallet bez povezivanja sopstvenog Dojo-a, vaši xpub-ovi su morali biti preneti na Samourai servere da bi aplikacija funkcionisala. Sa zaplenom ovih servera, moguće je da vlasti sada imaju pristup tim xpub-ovima.


Ovaj scenario ostaje hipotetičan. Ne znamo da li su ovi xpub-ovi zabeleženi, da li je bilo koje potencijalno skladište uništeno, da li su ih vlasti pronašle i da li planiraju da ih koriste za analizu lanca. Međutim, u takvoj situaciji, razumno je razmotriti najgori mogući scenario, gde vlasti poseduju xpub-ove korisnika koji nisu povezali svoj Dojo.

Za referencu, xpub je niz karaktera koji sadrži sve neophodne Elements za generisanje javnih ključeva potomaka (javni ključ + lančani kod). Koristi se u hijerarhijski determinističkim novčanicima za generate primanje adresa i praćenje transakcija računa bez izlaganja povezanih privatnih ključeva. Ovo omogućava, na primer, kreiranje "samo-za-gledanje" Wallet. Međutim, otkrivanje xpub-ova može ugroziti privatnost korisnika, jer omogućava trećim stranama da prate transakcije i vide stanja povezanih računa.

Svi koji znaju vaše xpubs mogu tako videti sve adrese za primanje vašeg Wallet, one korišćene u prošlosti, kao i one koje će biti generisane u budućnosti.


Za korisnike bez Dojo-a, potencijalno curenje vaših xpub-ova ima dve glavne posledice:



- Coinjoin-ovi koje ste možda izvršili postaju neefikasni sa stanovišta privatnosti za svakoga ko zna vaše xpub-ove, tako da vaši novčići gube svu anonimnost;
- Ova osoba takođe može pratiti sve adrese za primanje vašeg Samourai Wallet.


Stoga je važno razmotriti najgori mogući scenario i rastati se sa ovim Wallet, potencijalno ugroženim u smislu privatnosti. Da biste to učinili, kreirajte novi Wallet od nule sa drugim softverom, kao što je Sparrow Wallet. Nakon što proverite validnost vaših rezervnih kopija, prenesite sva svoja sredstva obavljanjem transakcija. Iako ova operacija ne prekida vezu praćenja vaših kovanica, sprečiće vlasti da sa sigurnošću znaju adrese vašeg novog Wallet.


Tokom ove operacije prenosa, preporučujem da izbegavate konsolidaciju vaših novčića. Ako pretpostavimo da su vaši xpub-ovi kompromitovani, konsolidacija neće imati uticaj sa stanovišta osobe koja ima pristup tim xpub-ovima, jer je vaša privatnost već ugrožena sa njima. Međutim, savetujem vam da ne konsolidujete previše vaše novčiće, prvenstveno da biste zaštitili svoju privatnost od drugih ljudi. U najgorem slučaju, samo vlasti mogu imati pristup vašim xpub-ovima, ali ostatak sveta ne zna za njih. Dakle, sa stanovišta drugih, konsolidacija vaših novčića mogla bi značajno narušiti vašu privatnost zbog Common Input Ownership Heuristike (CIOH).


**Napomena:** da biste definitivno prekinuli praćenje, možete razmotriti i izvođenje coinjoin-a sa ovog novog Wallet.

**Upozorenje:** Samo preuzimanje vašeg Samourai Wallet na Sparrow Wallet nije dovoljno. Neophodno je kreirati potpuno novi Wallet sa novom frazom za oporavak ako želite da izbegnete korišćenje xpub-ova koji su možda procureli. Ako uvezete vaš postojeći seed u Sparrow, samo menjate softver za upravljanje Wallet, ali Wallet ostaje isti.


### Kao korisnik Sparrow ili Samourai sa Dojo


Ako je vaš Wallet upravljan samo na Sparrow Wallet, vaši xpubs nisu mogli procuriti, bilo da koristite javni čvor ili svoj vlastiti Bitcoin čvor. Slično tome, ako koristite Samourai aplikaciju i oduvek ste povezivali ovu aplikaciju sa svojim Dojo-om od kreiranja vašeg Wallet, vaši xpubs su takođe sigurni.


Međutim, ako ste koristili isti Wallet tokom perioda **bez sopstvenog Dojo-a** a zatim sa sopstvenim Dojo-om, moguće je da su Samourai serveri mogli imati pristup vašim xpub-ovima, i stoga bi vlasti mogle znati za njih. Ako ste u ovoj specifičnoj situaciji, savetujem vam da sledite preporuke iz prethodnog odeljka i smatrate vaše xpub-ove kompromitovanim.


Za one koji su oduvek koristili Sparrow ili Samourai sa svojim sopstvenim Dojo-om, glavni rizik je da bi anonseti vaših novčića potencijalno mogli biti smanjeni. Pretpostavimo, u najgorem slučaju, da svi korisnici bez Dojo-a imaju svoje xpub-ove u rukama vlasti, tada bi put njihovih novčića kroz CoinJoin cikluse mogao biti praćen od strane tih vlasti.


Da bismo ovo ilustrovali, uzmimo konkretan primer. Zamislite da ste učestvovali u prvom ciklusu CoinJoin, praćenom sa dva dodatna nizvodna CoinJoin ciklusa. Ako xpub-ovi korisnika bez Dojo-a nisu procureli, tada bi potencijalni anonset vašeg novčića bio 13.


![samourai](assets/37.webp)


Međutim, ako uzmemo u obzir da su xpubs procurili i da ste naišli na korisnika bez dojo-a tokom početnog CoinJoin, a zatim 2 tokom prvog nizvodnog CoinJoin, tada bi vaš potencijalni anonset bio samo 10 umesto 13 iz ugla autoriteta.


![samourai](assets/38.webp)

Ovaj potencijalni pad u anonsetu je složen za kvantifikaciju, jer zavisi od brojnih faktora, a svaki novčić je pogođen drugačije. Na primer, korisnik bez Dojo-a susretnut u ranim ciklusima mnogo više utiče na potencijalni anonset nego onaj susretnut u kasnijim ciklusima. Da bismo vam dali ideju o situaciji, koja ostaje hipotetička, najnovija statistika koju je pružio Samourai pokazuje da između 85% i 90% novčića uključenih u coinjoin dolazi od korisnika sa Dojo, Sparrow, ili Bitcoin Keeper, tj. korisnika koji, čak i u najgorem scenariju, ne bi videli da su im xpubs procurili.

Iako je ove brojke teško proveriti, čine mi se doslednim iz dva razloga:



- Sparrow Wallet se široko koristi;
- Većina softvera za node-in-box nudi Dojo implementacije, a ovi mejnstrim softveri poput Umbrel su veoma popularni danas.


Dakle, potrebno je razmotriti nekoliko aspekata. Ako vam je privatnost vaših kovanica u odnosu na vlasti izuzetno važna, bilo bi razumno pripremiti se za najgori scenario, i teško je garantovati 100% da se vaši Whirlpool CoinJoin ciklusi ne bi mogli pratiti zbog potencijalnog curenja xpub-ova od korisnika bez Dojo-a. Iako je ova pretpostavka veoma malo verovatna, nije nemoguća.


S druge strane, ako privatnost vaših novčića u odnosu na autoritet koji potencijalno poseduje ove xpub-ove nije ključna za vas, onda se situacija može posmatrati drugačije.


Navodim "vis-à-vis the authority" jer je važno zapamtiti da samo vlast koja je zaplenila servere potencijalno zna za ove xpub-ove. Ako je vaš cilj korišćenja CoinJoin bio da sprečite vašeg pekara da prati vaša sredstva, onda on nije bolje informisan nego pre zaplene servera.


Konačno, neophodno je razmotriti početni anonset vašeg novčića, pre zaplene servera. Uzmimo za primer novčić koji je dostigao perspektivni anonset od 40,000; potencijalno smanjenje ovog anonseta je verovatno zanemarljivo. Zaista, sa već veoma visokim osnovnim anonsetom, malo je verovatno da bi prisustvo nekoliko korisnika bez Dojo-a moglo radikalno promeniti situaciju. Međutim, ako je vaš novčić imao anonset od 40, onda bi ovaj potencijalni curenje moglo ozbiljno uticati na vaše anonsete i potencijalno omogućiti praćenje.

S obzirom na to da je alat WST sada van upotrebe nakon gašenja OXT.me, možete samo proceniti ove anonsete. Za retrospektivni anonset, nema previše razloga za brigu jer model Whirlpool osigurava da je veoma visok od prvog CoinJoin, zahvaljujući nasleđu vaših kolega. Jedini slučaj gde ovo može predstavljati problem je ako vaš novčić nije bio remixovan nekoliko godina i bio je mixovan na početku lansiranja pool-a. Što se tiče prospektivnog anonseta, možete ispitati koliko dugo je vaš novčić bio dostupan za coinjoin-ove. Ako je prošlo nekoliko meseci, onda verovatno ima izuzetno visok prospektivni anonset. Suprotno tome, ako je dodat u pool samo nekoliko sati pre nego što su serveri zaplenjeni, onda je njegov prospektivni anonset verovatno veoma nizak.

[**-> Saznajte više o anonsetima i njihovoj metodi izračunavanja.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


Još jedan aspekt koji treba razmotriti je uticaj konsolidacija na anonsetove novčića koji su bili mešani. S obzirom da Whirlpool nalozi više nisu dostupni putem Samourai aplikacije, verovatno je da su mnogi korisnici preneli svoje Wallet na drugi softver i pokušali da povuku svoja sredstva iz Whirlpool. Konkretno, prošlog vikenda, kada su naknade za transakcije na Bitcoin mreži bile relativno visoke, postojala je jaka tehnička i ekonomska motivacija za konsolidaciju post-mix novčića. To znači da je verovatno da su mnogi korisnici napravili značajne konsolidacije.


Problem sa ovim post-mix konsolidacijama je što one uvek smanjuju anonsete, ne samo za korisnika koji ih izvodi već i za korisnike koje su sreli tokom svojih CoinJoin ciklusa. Iako nisam bio u mogućnosti da precizno verifikujem ili kvantifikujem ovaj fenomen, ekonomski podsticaji vezani za transakcione naknade u to vreme mogu nas navesti da pretpostavimo da su anonseti potencijalno niži.


### Kao Sentinel korisnik


Mreža operacija aplikacije Watch-only wallet Sentinel slična je onoj kod Samourai. Da biste pristupili informacijama Wallet, aplikacija mora preneti xpubs, javne ključeve i adrese koje ste obezbedili Dojo-u. Ako ste uvek koristili svoj Dojo na Sentinel-u, nema problema i možete nastaviti da koristite aplikaciju bez brige. Međutim, ako ste zavisili od Samourai servera za vaš Sentinel, moguće je da su vaši xpubs bili izloženi. U tom slučaju, preporučljivo je slediti isti proces promene Wallet koji se preporučuje za Samourai Wallet kada je povezan na Samourai servere.


U malo verovatnom slučaju da ste koristili svoj Dojo sa Samourai, ali ne i sa Sentinel, bilo bi mudrije smatrati da su vaši xpubs kompromitovani.


## Zaključak


Hvala što ste pročitali ovaj članak do kraja. Ako mislite da nedostaju informacije ili imate predloge, slobodno me kontaktirajte da podelite svoje misli. Takođe, ako vam je potrebna dodatna pomoć u oporavku vašeg Samourai Wallet uprkos ovom vodiču, pozivam vas da se pridružite [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) kako biste zatražili pomoć. Redovno posećujem ovaj Discord i biće mi drago da vam pomognem ako imam rešenje. Drugi bitkoineri će takođe moći da podele svoja iskustva i ponude svoju podršku. **U svakom slučaju, važno je da čuvate svoju frazu za oporavak, rezervnu datoteku i passphrase poverljivim**. Nemojte ih deliti ni sa kim, jer bi to moglo omogućiti krađu vaših bitkoina.