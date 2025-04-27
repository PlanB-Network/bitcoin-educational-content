---
name: Elektrum

description: Potpuni vodič za Electrum, od početnika do heroja
---

![cover](assets/cover.webp)


Pronađite ispod nekoliko izvora opisa za Electrum:



- [X](https://twitter.com/ElectrumWallet)
- [Electrum website](https://electrum.org/)
- [Electrum dokumentacija](https://electrum.readthedocs.io/)


Evo šta Rogzy misli o ovom vodiču:


> Moram reći, kada sam naišao na ovaj vodič bio sam šokiran. Čestitke Armanu the Parmanu za ovo. Bilo bi šteta ne ugostiti ga ovde i prevesti na što više jezika. Iskreno, dajte napojnicu tom tipu.

Originalna objava je sledeća:


![Electrum Desktop Wallet (Mac / Linux) - download, verify, connect to your node.](https://youtu.be/wHmQNcRWdHM)


![Making a Bitcoin transaction with Electrum](https://youtu.be/-d_Zd7VcAfQ)


## Zašto Electrum?


Ovo je detaljan vodič o tome kako koristiti Electrum Bitcoin Wallet, sa rešenjima za sve njegove zamke i trikove - nešto što sam razvio nakon nekoliko godina korišćenja i podučavanja studenata o Bitcoin sigurnosti/privatnosti. Electrum nije najbolji Bitcoin Wallet za osobu koja želi da sve bude što jednostavnije i preferira da ostane na početničkom nivou. Umesto toga, namenjen je osobi koja jeste, ili teži da bude, "napredni" korisnik.


Za novog Bitcoinera, odlično je samo ako je pod nadzorom iskusnog korisnika koji će im pokazati put. Ako uče da ga koriste sami, bilo bi bezbedno pod uslovom da odvoje vreme i koriste ga u testnom okruženju sa samo malim brojem Sats u početku. Ovaj vodič podržava taj poduhvat, ali je takođe dobar referentni materijal za bilo koga drugog.


**Upozorenje:** ovaj vodič je obiman. Nemojte pokušavati da sve ovo uradite u jednom danu. Najbolje je sačuvati vodič i raditi postepeno tokom vremena.


## Preuzimanje Electrum


Idealno je koristiti namenski računar Bitcoin za vaše Bitcoin transakcije (Moj vodič za ovo https://armantheparman.com/mint/) _(DOSTUPNO i u odeljku za privatnost)_. U redu je vežbati sa malim iznosima na "prljavom" računaru kada tek učite (ko zna koliko je skrivenog malvera vaš redovni računar sakupio tokom godina – ne želite da izložite svoje Bitcoin novčanike njima).


Preuzmite Electrum sa https://electrum.org/.


Kliknite na karticu Download na vrhu.


Kliknite na link za preuzimanje koji odgovara vašem računaru. Bilo koji Linux ili Mac računar može koristiti Python link (crveni krug). Linux računar sa Intel ili AMD čipom može koristiti Appimage (Green krug; ovo je kao Windows izvršna datoteka). Raspberry Pi uređaj ima ARM mikroprocesor i može koristiti samo Python verziju (crveni krug), ne Appimage, iako Pi koristi Linux. Plavi krug je za Windows, a crni krug je za Mac.


![image](assets/1.webp)


## Verifikacija Electrum


Svrha „provere“ preuzimanja je da se osigura da nijedan bit podataka nije izmenjen. To vas sprečava da koristite „hakovanu“ zlonamernu verziju softvera. U redu je preskočiti ovo pod uslovom da koristite preuzetu kopiju samo za vežbanje, tj. ne koristite novčanike koji drže ozbiljan novac. Zatim, kada budete spremni da koristite Electrum za svoja stvarna sredstva, trebalo bi da obrišete svoju kopiju i počnete ispočetka, ovog puta proveravajući svoje preuzimanje.


Da bismo to uradili, koristimo alate za kriptografiju sa javnim/privatnim ključem – gpg, o čemu je napisan vodič ovde (https://armantheparman.com/gpg/). Alat gpg dolazi sa svim Linux operativnim sistemima. Za Mac i Windows, pogledajte gpg link za uputstva za preuzimanje.


Pored preuzimanja Electrum softvera, zbog bezbednosti, takođe vam je potrebna digitalna POTPIS softvera. Ovo je niz teksta (zapravo je broj kodiran pomoću teksta) koji je programer proizveo svojim PRIVATNIM gpg ključem. Koristeći gpg program, možemo zatim „testirati“ POTPIS u odnosu na njegov JAVNI ključ (kreiran iz programerovog privatnog ključa) kojem svi imaju pristup, naspram preuzetog FAJLA.


Drugim rečima, sa tri ulaza (potpis, javni ključ i datoteka), dobijamo izlaz tačno ili netačno kako bismo potvrdili da datoteka nije izmenjena.


Da biste dobili potpis, kliknite na link koji odgovara datoteci koju ste preuzeli (pogledajte obojene strelice):


![image](assets/2.webp)


Klikom na link datoteka se može automatski preuzeti u vaš folder za preuzimanja, ili se može otvoriti u pregledaču. Ako se otvori u pregledaču, potrebno je da sačuvate datoteku. Možete kliknuti desnim tasterom miša i izabrati „sačuvaj kao“. U zavisnosti od operativnog sistema ili pregledača, možda ćete morati da kliknete desnim tasterom miša na belu površinu, a ne na tekst.


Ispod je prikazano kako izgleda preuzeti tekst. Možete videti da postoji više potpisa – ovo su potpisi različitih osoba. Možete verifikovati svaki ili bilo koji. Pokazaću vam kako da verifikujete samo potpis programera.


![image](assets/3.webp)


Zatim, treba da nabaviš javni ključ od ThomasV-a – on je glavni developer. Možeš ga dobiti direktno od njega, sa njegovog Keybase naloga, Github-a, od nekog drugog, sa keyserver-a, ili sa Electrum sajta.


Dobijanje sajtom Electrum je zapravo najmanje siguran način, jer ako je ovaj sajt zlonameran (upravo ono što proveravamo) zašto uzimamo javni ključ sa njega (javni ključ bi mogao biti lažan)?


Da bi za sada bilo jednostavno, pokazaću vam kako da ga preuzmete sa sajta, ali imajte ovo na umu. Ovde je kopija (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc ) na GitHub-u sa kojom možete da ga uporedite.


Pomeri stranicu malo naniže da pronađeš link ka javnom ključu od ThomasV-a (crveni krug ispod). Klikni na njega i preuzmi ga, ili ako se otvori neki tekst u pretraživaču, desni klik za čuvanje.


![image](assets/4.webp)


Sada imate 3 nove datoteke, verovatno sve u folderu za preuzimanja. Nije važno gde se nalaze, ali proces je lakši ako ih sve stavite u isti folder.


Tri fajla:


1. Preuzimanje Electrum

2. Datoteka potpisa (obično ima isti naziv datoteke kao i preuzimanje Electrum-a sa dodatkom “.asc”

3. Javni ključ ThomasaV.


Otvorite terminal na Mac ili Linux, ili komandni prompt (CMD) na Windows.


Idite u direktorijum Downloads (ili gde god da ste stavili ta tri fajla). Ako nemate pojma šta ovo znači, naučite iz ovog kratkog videa za Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) i ovog za Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Zapamtite da su na Linux računarima nazivi direktorijuma osetljivi na velika i mala slova.


U terminalu, ukucajte ovo da uvezete ThomasV-jev javni ključ u "keyring" vašeg računara (keyring je apstraktan koncept – zapravo je samo datoteka na vašem računaru):


```bash
gpg --import ThomasV.asc
```


Uverite se da naziv datoteke odgovara onome što ste preuzeli. Takođe, obratite pažnju da je u pitanju dupla crtica, a ne jedna. Takođe, primetite da postoji razmak pre i posle „–import“. Zatim pritisnite <enter>.


Datoteka bi trebalo da se uveze. Ako dobijete grešku, proverite da li ste u direktorijumu gde datoteka zaista postoji. Da biste proverili u kom ste direktorijumu (na Mac ili Linux), otkucajte pwd. Da biste videli koje datoteke su u direktorijumu u kojem se nalazite (na Mac ili Linux), otkucajte ls. Trebalo bi da vidite tekstualnu datoteku “ThomasV.asc” navedenu, moguće među ostalim datotekama.


Zatim pokrećemo komandu da verifikujemo potpis.


```bash
gpg –verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```


Primetite da ovde postoje 4 "Elements", svaki razdvojen razmakom. Naizmenično sam podebljao tekst da biste lakše videli. Četiri Elements su:


1. gpg program

2. opcija –verify

3. naziv datoteke potpisa

4. naziv datoteke programa


Od interesa, ponekad možete izostaviti 4. element i računar će pretpostaviti šta mislite. Nisam siguran, ali verujem da to funkcioniše samo ako se nazivi fajlova razlikuju samo po "asc" na kraju.


Nemojte samo kopirati nazive datoteka koje sam ovde prikazao – proverite da li se podudaraju sa nazivom datoteke koju imate na svom sistemu.


Pritisnite <enter> da pokrenete komandu. Trebalo bi da vidite “good signature from ThomasV” što ukazuje na uspeh. Biće nekih grešaka jer nemamo javne ključeve za potpise drugih ljudi koji su sadržani u fajlu sa potpisima (ovaj sistem kombinovanja potpisa u jednom fajlu može se promeniti u kasnijim verzijama). Takođe, postoji upozorenje na dnu koje možemo ignorisati (ovo nas upozorava da nismo eksplicitno rekli računaru da verujemo ThomasV javnom ključu).


Sada imamo verifikovanu kopiju Electrum-a koja je bezbedna za korišćenje.


## Pokretanje Electrum


### Pokretanje Electrum-a ako koristite Python


Ako ste preuzeli Python verziju, ovo je način kako da je pokrenete. Videćete na stranici za preuzimanje ovo:


![image](assets/5.webp)


Za Linux, dobra je ideja prvo ažurirati vaš sistem:


```bash
sudo apt-get update
sudo apt-get upgrade
```


Kopirajte označeni žuti tekst, nalepite ga u terminal i pritisnite <enter>. Bićete upitani za vašu lozinku, moguće i za potvrdu da nastavite, a zatim će instalirati te fajlove („zavisnosti“).


Takođe ćete morati da ekstrahujete zipovani fajl u direktorijum po vašem izboru. To možete uraditi pomoću grafičkog korisničkog interfejsa Interface, ili iz komandne linije (komanda označena roze bojom) – zapamtite da se vaši nazivi fajlova mogu razlikovati. (Napomena da kada smo verifikovali preuzimanje u prethodnom odeljku, verifikovali smo zip fajl, a ne ekstrahovani direktorijum.)


Postoji opcija za „instalaciju“ korišćenjem PIP programa, ali to je nepotrebno i dodaje dodatne korake i instalaciju fajlova. Samo pokrenite program koristeći terminal da biste sve to zaobišli.


Koraci (Linux) su:


1. navigirajte do direktorijuma gde su fajlovi ekstrahovani

2. upiši: ./run_electrum


Na Mac-u, koraci su isti, ali možda ćete prvo morati instalirati Python3 i koristiti ovu komandu za pokretanje:


```bash
python3 ./run_electrum
```


Jednom kada je Electrum pokrenut, prozor terminala će ostati otvoren. Ako ga zatvorite, to će prekinuti Electrum program. Samo ga minimizirajte dok koristite Electrum.


### Pokretanje Electrum-a sa Appimage-om


Ovo je malo lakše, ali ne tako lako kao izvršna datoteka za Windows. U zavisnosti od verzije Linuxa koju koristite, podrazumevano, Appimage datoteke mogu imati postavljene atribute tako da sistem ne dozvoljava izvršavanje. Moramo to promeniti. Ako vaš Appimage radi, možete preskočiti ovaj korak. Idite do mesta gde se datoteka nalazi, koristeći terminal, a zatim pokrenite ovu komandu:


```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```


„sudo“ daje privilegije superkorisnika; „chmod“ je komanda za promenu moda, menjajući ko može da čita, piše ili izvršava; „ug+x“ znači da menjamo korisnika i grupu kako bismo omogućili izvršavanje.


Prilagodite naziv datoteke kako bi odgovarao vašoj verziji.


Zatim će se Electrum pokrenuti dvostrukim klikom na ikonu Appimage.


### Pokretanje Electrum-a na Mac-u


Samo dvaput kliknite na preuzetu datoteku (to je „disk”). Otvoriće se prozor. Prevucite ikonu Electrum u prozoru na vašu radnu površinu, ili gde god želite da zadržite program. Zatim možete „izbaciti” disk i obrisati disk (preuzetu datoteku).


Da biste pokrenuli program, samo dvaput kliknite na njega. Možda ćete dobiti neke Mac-specifične greške "dadilje" koje treba zaobići.


### Pokretanje Electrum-a na Windows-u


Uprkos tome što najviše mrzim Windows, ovo je najjednostavnija metoda. Samo dvaput kliknite na izvršnu datoteku da biste je pokrenuli.


## Počni sa lažnim Wallet


Kada prvi put učitate Electrum, otvoriće se prozor ovakav:


![image](assets/6.webp)


Kasnije ćemo ručno odabrati vaš server, ali za sada ostavite podrazumevani i automatski se povežite.


Zatim, kreirajte lažni Wallet – nikada nemojte stavljati sredstva u ovaj Wallet. Svrha ovog lažnog Wallet je da prođete kroz softver i osigurate da sve radi dobro pre nego što učitate vaš pravi Wallet. Pokušavamo da izbegnemo slučajno odavanje privatnosti sa pravim Wallet. Ako samo vežbate, Wallet koji kreirate može se smatrati lažnim Wallet ionako.


Možete ostaviti ime kao „default_wallet“ ili ga promeniti u šta god želite, i kliknite dalje. Kasnije, ako imate više novčanika, možete ih pronaći i otvoriti u ovoj fazi tako što ćete prvo kliknuti na „Izaberi…“


![image](assets/7.webp)


Izaberite “Standard Wallet” i <Dalje>:


![image](assets/8.webp)


Zatim, izaberite „Već imam seed“. Ne želim da steknete naviku kreiranja Electrum seed, jer koristi sopstveni protokol koji nije kompatibilan sa drugim novčanicima – zato ne klikćemo „novi seed“.


![image](assets/9.webp)


Idite na https://iancoleman.io/bip39/ i kreirajte lažni seed. Prvo, promenite broj reči na 12 (što je uobičajena praksa), zatim kliknite na “generate” i kopirajte reči iz okvira u vaš clipboard.


![image](assets/10.webp)


Zatim nalepite reči u Electrum. Evo primera:


![image](assets/11.webp)


Electrum će tražiti reči koje odgovaraju sopstvenom protokolu. Moramo to zaobići. Kliknite na opcije i izaberite BIP39 seed:


![image](assets/12.webp)


seed tada postaje važeći. (Pre nego što to uradite, Electrum je očekivao Electrum seed pa je ovaj seed smatran nevažećim). Pre nego što kliknete dalje, obratite pažnju na tekst koji kaže „Checksum OK“. Važno je (za pravi Wallet koji možda kasnije koristite) da ovo vidite pre nego što nastavite, jer potvrđuje validnost seed koji ste uneli. Upozorenje pri dnu može se ignorisati, to je prigovor Electrum developera o BIP39 i njihovim „FUD’ey“ tvrdnjama da je njihova verzija (koja nije kompatibilna sa drugim novčanicima) superiorna.


**Brzo skretanje za važno upozorenje:** svrha kontrolnog zbira je da se osigura da ste uneli svoj seed bez grešaka u kucanju. Kontrolni zbir je završni deo seed (12. reč postaje kontrolna reč) koja se matematički određuje prema prvom delu seed (11 reči). Ako biste nešto pogrešno otkucali na početku, kontrolna reč se matematički neće poklapati i Wallet softver će vas upozoriti. To ne znači da se seed ne može koristiti za kreiranje funkcionalnog Bitcoin Wallet. Zamislite da kreirate Wallet sa greškom u kucanju, učitate Wallet sa Bitcoin, a onda jednog dana možda budete morali da obnovite Wallet, ali kada to uradite, ne ponovite grešku u kucanju – obnovićete pogrešan Wallet! Prilično je opasno što Electrum dozvoljava da nastavite sa kreiranjem Wallet ako je vaš kontrolni zbir nevažeći, pa budite upozoreni, vaša je odgovornost da se uverite. Drugi novčanici neće vam dozvoliti da nastavite, što je mnogo sigurnije. Ovo je jedna od stvari koje mislim kada kažem da je Electrum u redu za korišćenje, kada naučite da ga pravilno koristite (Electrum programeri bi trebalo da poprave ovo).


Primetite da ako želite da dodate passphrase, prilika da to izaberete je u ovom prozoru opcija, odmah na vrhu.


Nakon što kliknete na OK, bićete vraćeni tamo gde ste uneli frazu seed. Ako ste odabrali opciju passphrase, NE unosite je sa rečima seed (podsetnik za to dolazi sledeće).


Ako niste zatražili passphrase, sledeći ekran koji ćete videti prikazuje više opcija za vaš Wallet tip skripte i putanju derivacije o kojima možete saznati više ovde (https://armantheparman.com/public-and-private-keys/), ali samo ostavite podrazumevane vrednosti i nastavite.


![image](assets/13.webp)


**Za dodatne informacije** Prva opcija vam omogućava da birate između:



- legacy (adrese koje počinju sa „1“),
- Pay-to-Script-Hash (adrese koje počinju sa „3“),
- bech32/native SegWit (adrese koje počinju sa „bc1q“).


U vreme pisanja, Electrum još uvek ne podržava Taproot (adrese koje počinju sa "bc1p"). Druga opcija u ovom prozoru omogućava vam da izmenite put derivacije. Predlažem da to nikada ne menjate, posebno pre nego što razumete šta to znači. Ljudi će naglašavati važnost zapisivanja puta derivacije kako biste mogli da povratite svoj Wallet ako bude potrebno, ali ako ga ostavite kao podrazumevani, verovatno ćete biti u redu, tako da ne paničite – ali je i dalje dobra praksa zapisati put derivacije.


Dalje, biće vam data opcija da dodate LOZINKU. Ovo ne treba mešati sa “passphrase”. Lozinka zaključava fajl na vašem računaru. passphrase je deo sastava privatnog ključa. Pošto je ovo lažni Wallet, možete ostaviti lozinku praznu i nastaviti.


![image](assets/14.webp)


Dobićete iskačući prozor o obaveštenjima za novu verziju (predlažem da odaberete ne). Wallet će se zatim generate i biti spreman za korišćenje (ali zapamtite, ovaj Wallet je predviđen za brisanje, to je samo lažni Wallet).


![image](assets/15.webp)


Postoji nekoliko stvari koje predlažem da uradite kako biste postavili softversko okruženje (potrebno samo jednom):


### Promeni jedinice u BTC


Idite na gornji meni, alati –> electrum postavke, i tamo pod opštim tabom, naći ćete opciju da promenite “osnovnu jedinicu” na BTC.

Omogući karticu Adrese i Novčići


Idite na gornji meni, pogled, i izaberite “prikaži adrese”. Zatim se vratite na pogled i izaberite “prikaži novčiće”.


### Omogući Oneserver


Podrazumevano, Electrum se povezuje na nasumičan čvor. Takođe se povezuje na mnoge druge sekundarne čvorove. Nisam siguran koje podatke razmenjuje sa tim sekundarnim čvorovima, ali ne želimo da se to dešava, zbog privatnosti. Čak i ako navedete čvor, npr. svoj čvor, ovi brojni drugi čvorovi će takođe biti povezani, i nisam siguran koje informacije se dele. Bez obzira na to, lako je sprečiti. Pre nego što vam pokažem kako da navedete svoj čvor, nateraćemo Electrum da se poveže samo na jedan server u isto vreme.


**Napomena:** postoji način da se ovo uradi specificiranjem “oneserver” iz komandne linije, ali ne preporučujem ovaj način. Pokazaću alternativu za koju mislim da je dugoročno lakša i verovatnije je da neće dozvoliti slučajno povezivanje sa drugim čvorovima.


Razlog zašto koristimo lažni Wallet je taj što bismo, da smo učitali naš pravi Wallet, sa našim pravim Bitcoin, do sada nenamerno povezali na nasumični čvor (čak i ako smo odabrali “ručno postavi server” na početku, i dalje se povezuje na ove druge sekundarne čvorove iz nekog razloga (hej Electrum developeri, trebalo bi da popravite ovo). Ako bi naš Wallet bio privatan, ovo bi bila katastrofa.


Takođe ne možemo izvršiti korake koje ću vam pokazati u nastavku bez prethodnog učitavanja neke vrste Wallet. (Uredićemo konfiguracionu datoteku koja se popunjava i postaje spremna za uređivanje tek kada se učita Wallet).


Sada isključite Electrum **(VAŽNO: ako to ne uradite, sledeće promene koje napravite će biti izbrisane)**.


### LINUX/MAC Konfig File


Otvorite terminal u Linuxu ili Mac-u (uputstva za Windows kasnije):


Trebalo bi da automatski budete u početnom folderu. Odatle, idite do skrivenog foldera sa podešavanjima za electrum (ovo je drugačije mesto od onog gde se nalazi aplikacija).


```bash
cd .electrum
```


Primetite tačku pre „electrum“ koja označava da je to skriveni folder.


Još jedan način da stignete tamo je da ukucate:


```bash
cd ~/.electrum
```


gde “~” predstavlja putanju do vašeg kućnog direktorijuma. Možete videti punu putanju vašeg trenutnog direktorijuma pomoću komande “pwd“.


Jednom kada ste u direktorijumu “.electrum”, otkucajte “nano config” i pritisnite <enter>.


Otvaraće se uređivač teksta (nazvan nano) sa otvorenom konfiguracionom datotekom. Miš ovde ne funkcioniše mnogo. Koristite strelice na tastaturi da dođete do linije koja kaže:


```json
"oneserver": false,
```


Promeni "false" u "true"; i ne diraj sintaksu (ne briši zarez ili tačka-zarez).


Pritisnite <ctrl> x, da izađete, zatim „y“ da sačuvate, zatim <enter> što potvrđuje promenu bez uređivanja imena datoteke.


Sada ponovo pokrenite Electrum. Zatim kliknite na krug u donjem desnom uglu, što otvara mrežna podešavanja. Zatim, blizu vrha u kartici pregleda, videćete “connected to 1 node” – ovo označava uspeh.


Neposredno ispod toga, videćete tekstualno polje i serverov Address je tamo. Trenutno ste povezani na taj nasumični čvor. Više o povezivanju na čvor u sledećem odeljku.


### Windows Config File


Datoteka konfiguracije za Windows je malo teže pronaći. Direktorijum je: `C:/Users/Parman/AppData/Roaming/Electrum`


Očigledno, morate promeniti “Parman” u svoje korisničko ime za računar.


U toj fascikli ćeš pronaći config fajl. Otvori ga pomoću tekst editora i izmeni liniju:


```json
"oneserver": false,
```


Promenite „false“ u „true“; ne remetite sintaksu (ne brišite zarez ili tačka-zarez).


Zatim sačuvaj datoteku i izađi.


## Poveži Electrum sa čvorom


Zatim, želimo da povežemo naš dummy Wallet na čvor po našem izboru. Ako niste spremni da pokrenete čvor, možete uraditi jedno od sledećeg:


1. Povežite se na lični čvor prijatelja (zahteva Tor)

2. Povežite se sa čvorom pouzdane kompanije

3. Poveži se sa nasumičnim čvorom (ne preporučuje se).


Usput, ovde su uputstva kako da pokrenete svoj čvor, i ovo su razlozi zašto bi trebalo. (pogledajte tutorijale u odeljku Čvor ili u našim besplatnim kursevima)


### Povežite se na čvor prijatelja putem Tor-a (Vodič uskoro dolazi.)


### Povežite se sa čvorom pouzdane kompanije


Jedini razlog da ovo uradite bio bi ako morate pristupiti Blockchain, a nemate svoj čvor na raspolaganju (ili prijateljev).


Hajde da se povežemo na Bitaroo-ov čvor – Rečeno nam je da oni ne prikupljaju podatke. Oni su Bitcoin Samo Exchange, koje vodi strastveni Bitcoiner. Povezivanje sa njima uključuje malo poverenja, ali je bolje nego povezivanje na nasumičan čvor, koji bi mogao biti nadzorna kompanija.


Dođite do Postavki mreže klikom na krug u donjem desnom delu prozora Wallet (crveno označava da nije povezano, Green označava da je povezano, a plavo označava da je povezano putem Tor-a).


![image](assets/16.webp)


Kada kliknete na ikonu kruga, pojaviće se iskačući prozor: Vaš Wallet će prikazati “connected to 1 node” pošto smo to ranije forsirali.


Poništite izbor polja „automatski odaberi server“, a zatim u polje Server unesite Bitaroo-ove podatke kako je prikazano:


![image](assets/17.webp)


Zatvori prozor, i sada bi trebalo da budemo povezani na Bitaroo čvor. Da potvrdimo, krug bi trebalo da bude Green. Klikni ponovo i proveri da se detalji servera nisu vratili na nasumičan čvor.


### Povežite se sa svojim čvorom


Ako imate svoj čvor, to je sjajno. Ako imate samo Bitcoin Core, a nemate i Electrum SERVER, još uvek nećete moći da povežete Electrum Wallet sa svojim čvorom.


**Imajte na umu da su Electrum Server i Electrum Wallet različite stvari:** server je softver potreban da bi Electrum Wallet mogao komunicirati Bitcoin Blockchain – ne znam zašto je dizajniran na ovaj način – moguće zbog brzine, ali možda grešim.


Ako pokrećete softverski paket za čvor kao što je MyNode (onaj koji preporučujem ljudima da počnu sa njim), Raspiblitz (preporučuje se kako postajete napredniji), ili Umbrel (lično ga još ne preporučujem jer sam iskusio previše problema), onda ćete moći da povežete vaš Wallet jednostavno unosom IP Address računara (Raspberry Pi) koji pokreće čvor, plus dvotačka, i 50002, kao što je prikazano na slici u prethodnom odeljku. (Dalje ću vam pokazati kako da pronađete IP Address vašeg čvora).


Otvorite postavke mreže (kliknite na Green ili crveni krug u donjem desnom uglu). Poništite izbor u polju „automatski odaberi server“, zatim unesite svoj IP Address kao što sam ja uradio, vaš će biti drugačiji, ali dvotačka i „50002“ treba da budu isti.


![image](assets/18.webp)


Zatvori prozor, i sada bismo trebali biti povezani na tvoj čvor. Da potvrdiš, klikni ponovo na krug i proveri da se detalji servera nisu vratili na nasumični čvor.


Ponekad, uprkos tome što sve radite ispravno, čini se da odbija da se poveže. Evo šta možete pokušati...



- Nadogradite na noviju verziju Electrum-a i vašeg softvera čvora;
- Pokušajte obrisati folder cache u direktorijumu “.electrum”;
- Pokušajte promeniti port sa 50002 na 50001 u mrežnim podešavanjima;
- Koristite [ovaj vodič](https://armantheparman.com/tor/) za povezivanje koristeći Tor kao alternativu;
- Ponovo instaliraj Electrum Server na čvoru.


## Pronalaženje IP adrese vašeg čvora Address


IP Address nije nešto što običan korisnik obično zna kako da pronađe i koristi. Pomogao sam mnogim ljudima da pokrenu čvor, a zatim povežu svoje novčanike sa čvorom – prepreka često izgleda da je pronalaženje njegovog IP Address.


Za MyNode, možete upisati u prozor pregledača: `mynode.local`


Ponekad, “mynode.local” ne radi (proverite da ga ne kucate u Google traku za pretragu. Da biste naterali navigacionu traku da prepozna vaš tekst kao Address, a ne kao pretragu, prethodite tekst sa `http://` ovako: `http://mynode.local`. Ako to ne radi, pokušajte sa “s”, ovako: `https://mynode.local`.


Ovo će pristupiti uređaju, i možete kliknuti na link za postavke (pogledajte moj plavi "krug" ispod) da biste prikazali ovaj ekran gde se nalazi IP Address:


![image](assets/19.webp)


Ova stranica će se učitati i videćete IP čvora (plavi “krug”)


![image](assets/20.webp)


Zatim, u budućnosti, možete ukucati 192.168.0.150, ili http://192.168.0.150 u vaš pretraživač.


Za Raspiblitz (kada se ne povezuje ekran), potreban je drugačiji metod (koji radi i za MyNode):


Prijavite se na veb stranicu vašeg rutera – ovde ćemo pronaći IP Address svih vaših povezanih uređaja. Veb stranica rutera će biti IP Address koji unosite u veb pregledač. Moj izgled je:


http://192.168.0.1


Da biste dobili pristupne podatke za prijavu na ruter, možete ih potražiti u korisničkom priručniku ili ponekad čak i na nalepnici na samom ruteru. Potražite korisničko ime i lozinku. Ako ih ne možete pronaći, pokušajte Korisnik: "admin" Lozinka: "password"


Ako možete da se prijavite, videćete svoje povezane uređaje i iz njihovih imena može biti jasno koji je vaš čvor. IP Address će biti tamo.


### Ako prva dva metoda ne uspeju, poslednji će raditi, ali je zamoran:


Prvo, pronađite IP Address bilo kog uređaja na vašoj mreži (trenutni računar će biti dovoljan).


Na Mac-u, naći ćete ga u mrežnim preferencama:


![image](assets/21.webp)


Zanima nas prvih 4 Elements (192.168.0), ne 4. element, „166“ koji vidite na slici (vaš će biti drugačiji).


Za Linux, koristite komandnu liniju:


```bash
ifconfig | grep inet
```


Ta vertikalna linija je simbol “pipe” i naći ćete je ispod tastera <delete>. Videćete neki izlaz i IP Address. (Ignorišite 127.0.0.1 to nije to, i ignorišite netmasku)


Za Windows, otvorite komandnu liniju (cmd) i unesite:


```bash
ipconfig/all
```


i pritisnite Enter. IP Address se može pronaći u izlazu.


To je bio lakši deo. Deo Hard je sada pronaći IP vašeg čvora Address – moramo koristiti brute-force pogađanje. Recimo na primer da IP vašeg računara Address počinje sa 192.168.0.xxx, onda za vaš čvor, u pretraživaču, pokušajte: `https://192.168.0.2`


Najmanji mogući broj je 2 (0 znači bilo koji uređaj, a 1 pripada ruteru) i najveći, verujem da je 255 (to je u binarnom obliku 11111111, najveći broj koji može biti sadržan u 1 bajtu).


Jedan po jedan, napredujte ka 255. Na kraju ćete se zaustaviti na tačnom broju koji učitava vašu MyNode stranicu (ili RaspiBlitz stranicu). Tada ćete znati koji broj da unesete u Electrum mrežna podešavanja da biste se povezali sa vašim čvorom.


Izgledaće otprilike ovako (obavezno uključite dvotačku i broj nakon toga):


![image](assets/22.webp)


**Napomena** korisno je znati da su ove IP adrese INTERNE za vašu kućnu mrežu. Niko spolja ih ne može videti i nisu osetljive. One su poput telefonskih ekstenzija u velikoj organizaciji koje vas usmeravaju na različite telefone.


## Izbriši lažni Wallet


Sada smo uspešno povezani sa jednim i samo jednim čvorom. Ovako će se Electrum učitavati po podrazumevanim postavkama od sada. Sada bi trebalo da obrišete lažni Wallet (Meni: fajl –> obriši), u slučaju da slučajno pošaljete sredstva na ovaj nesigurni Wallet (Nesiguran je jer ga nismo kreirali na bezbedan način).


## Napravi vežbu Wallet


Nakon brisanja lažnog Wallet, počnite ponovo i napravite novi, na isti način, samo ovaj put zapišite reči seed i čuvajte ih prilično sigurno.


Dobra je ideja naučiti kako Electrum funkcioniše uz ovu praksu Wallet, bez nezgrapnog Hardware Wallet (potrebnog za visoku sigurnost). Stavite samo malu količinu Bitcoin u ovaj Wallet – Pretpostavite da ćete izgubiti ovaj novac. Kada postanete vešti, onda naučite koristiti Electrum sa Hardware Wallet.


U novom Wallet koji ste kreirali, videćete listu adresa. Green adrese se nazivaju „prijemne adrese“. One su proizvod 3 stvari:



- seed fraza
- passphrase
- Putanja izvođenja


Vaš novi Wallet ima skup adresa za primanje koje se mogu matematički i reproduktivno kreirati pomoću bilo kojeg Software Wallet koji ima seed, passphrase i put derivacije. Ima ih 4,3 milijarde! Više nego što će vam trebati. Electrum vam prikazuje samo prvih 20, a zatim još kako koristite prve.


Više informacija o privatnim ključevima Bitcoin možete pronaći u ovom vodiču.


![image](assets/23.webp)


Ovo je veoma različito od nekih drugih novčanika koji prikazuju samo 1 Address u isto vreme.


Zato što ste uneli frazu seed prilikom kreiranja ovog Wallet, Electrum ima privatni ključ za svaku od adresa, i trošenje sa ovih adresa je moguće.


Takođe imajte na umu da postoje žute adrese, nazvane "adrese za kusur" – Ovo su samo još jedan skup adresa iz različite matematičke grane (još 4,3 milijarde ovih postoji). Koriste ih Wallet da automatski pošalju višak sredstava nazad u Wallet kao kusur. Na primer, ako uzmete 1.5 Bitcoin i potrošite 0.5 kod trgovca, ostatak od 1.0 mora negde da ode. Vaš Wallet će ga potrošiti na sledeći prazan žuti kusur Address – u suprotnom, ide u Miner! Za više informacija o ovome (UTXO) pogledajte ![ovaj vodič](https://armantheparman.com/UTXO/).


Zatim, vratite se na Ian Colman vebsajt za privatne ključeve i unesite seed (umesto da generišete jedan). Videćete ispod da se informacije o privatnom i javnom ključu menjaju; sve ispod zavisi od stvari iznad na stranici.


**Zapamti:** nikada ne bi trebalo da uneseš seed svog pravog Bitcoin Wallet ili računara, malver može da ga ukrade. Koristimo samo vežbovni Wallet, u svrhe učenja, tako da je sada u redu.


Pomeri se dole i promeni putanju derivacije na BIP84 (SegWit) da odgovara tvom Electrum Wallet klikom na karticu BIP84.


![image](assets/24.webp)


Ispod toga, videćete prošireni privatni ključ naloga i prošireni javni ključ naloga:


![image](assets/25.webp)


Idite na Electrum i uporedite da li se poklapaju. Na vrhu se nalazi meni, Wallet –>informacije:


![image](assets/26.webp)


Ovo se pojavljuje:


![image](assets/27.webp)


Primetite da se dva javna ključa podudaraju.


Zatim, uporedite adrese. Vratite se na sajt Iana Colemana i skrolujte do dna:


![image](assets/28.webp)


Primeti da se podudaraju sa adresama u Electrumu.


Sada ćemo proveriti adrese za kusur. Pomaknite se malo nagore do putanje derivacije i promenite poslednju 0 u 1:


![image](assets/29.webp)


Sada se pomerite nadole i uporedite adrese sa žutim adresama u Electrumu.


Zašto smo sve ovo uradili?


Ubacili smo seed reči kroz dva različita nezavisna softverska programa kako bismo se uverili da nam daju iste informacije. Ovo značajno smanjuje rizik da se zlonamerni kod krije unutra i daje nam lažne privatne ili javne ključeve, ili adrese.


Sledeće što treba uraditi je primiti mali test i potrošiti ga unutar Wallet sa jednog Address na drugi.


## Testiranje Wallet (Naučite kako ga koristiti)


Ovde ću vam pokazati kako da primite UTXO na vaš Wallet, a zatim ga premestite (potrošite) na drugi Address unutar Wallet. Ovo je veoma mala količina koju nećemo imati ništa protiv da izgubimo.


Ovo ima nekoliko svrha.



- Dokazaće da imate moć da trošite novčiće u novom Wallet.
- Pokazaće kako koristiti Electrum softver za izvršavanje transakcije (i neke funkcije), pre nego što dodamo dodatnu složenost radi sigurnosti (koristeći Hardware Wallet ili računar bez mrežnog pristupa)
- To će ojačati ideju da imate mnogo adresa za izbor za primanje i trošenje, unutar istog Wallet.


Otvorite svoj test Electrum Wallet i kliknite na karticu Adrese, zatim desnim klikom miša kliknite na prvi Address i izaberite Kopiraj –> Address:


![image](assets/30.webp)


Address je sada u memoriji vašeg računara.


Sada idi na Exchange gde imaš nešto Bitcoin, i hajde da povučemo malu količinu na ovaj Address, recimo 50,000 Sats. Koristiću Coinbase kao primer jer je to najčešće korišćen Exchange, iako su oni neprijatelj Bitcoin, i gadi mi se da se prijavim na stari napušteni nalog za ovu svrhu.


Prijavite se i kliknite na dugme Pošalji/Primi, koje se od danas nalazi u gornjem desnom uglu veb stranice.


![image](assets/31.webp)


Očigledno nemam sredstva na Coinbase-u, ali zamisli da ovde ima sredstava i prati dalje: Zalepi Address iz Electrum-a u polje “To” kao što sam uradio. Takođe ćeš morati da izabereš iznos (predlažem oko 50,000 Sats). Nemoj stavljati “opcionalnu poruku” – Coinbase već prikuplja dovoljno tvojih podataka (i prodaje ih), nema potrebe da im pomažeš. Na kraju, klikni “Continue”. Posle toga ne znam koje ćeš druge iskačuće prozore dobiti, tu si prepušten sebi, ali metoda je slična za sve berze.


![image](assets/32.webp)


U zavisnosti od Exchange, možda ćete videti Sats u vašem Wallet odmah, ili sa nekim zakašnjenjem od sati/dana.


Imajte na umu da će Electrum prikazati primljene novčiće čak i ako nisu potvrđeni na Blockchain. Novčići koje imate se čitaju sa liste čekanja Bitcoin čvora, ili "Mempool". Kada uđu u blok, videćete sredstva kao potvrđena.


Sada kada imamo UTXO u našem Wallet, trebali bismo ga označiti. Samo mi možemo videti ovu oznaku, nema nikakve veze sa javnim Ledger. Sve naše Electrum oznake su vidljive samo na računaru koji koristimo. Zapravo možemo sačuvati fajl i koristiti ga za vraćanje svih naših oznaka na drugi računar koji koristi isti Wallet.


### Napravite etiketu za UTXO


Trebala mi je donacija za ovaj test Wallet, zahvaljujući @Sathoarder za obezbeđivanje živog UTXO (10,000 Sats), i još jedna osoba (anon) je donirala za isti Address (5000 Sats). Primetite da ima 15,000 Sats u prvom Address stanju, i ukupno 2 transakcije (krajnja desna kolona). Na dnu, Stanje je 10,000 Sats potvrđeno, i još 5,000 Sats su nepotvrđeni (još uvek u Mempool).


![image](assets/33.webp)


Sada, ako pređemo na karticu Coins, možemo videti dva "primljena novčića" ili UTXO-a. Obe su u istom Address.


![image](assets/34.webp)


Vraćajući se na karticu Address, ako dvaput kliknete na područje „labels“ pored Address, moći ćete uneti neki tekst, a zatim pritisnite <enter> da sačuvate:


![image](assets/35.webp)


Ovo je dobra praksa kako biste mogli pratiti odakle su došle vaše kovanice, da li su bez KYC-a ili ne, i koliko vas je svaki UTXO koštao (u slučaju da trebate prodati i izračunati porez koji će vam vaša vlada ukrasti).


Idealno bi bilo da izbegavate akumuliranje više novčića u istom Address. Ako ipak odlučite da to uradite (nemojte), možete označiti svaki novčić umesto svih istom oznakom koristeći Address metodu. Ne možete zapravo otići na karticu "novčići" i tamo urediti oznake (ne, to bi bilo previše intuitivno!). Morate otići na karticu Istorija, pronaći transakciju, označiti je, i onda ćete videti oznake u sekciji novčića. Sve oznake koje vidite u sekciji novčića dolaze iz Address oznaka ILI oznaka iz istorije, ali svaka oznaka iz istorije nadjačava bilo koju Address oznaku. Da biste sačuvali svoje oznake u fajl, možete ih izvesti iz menija na vrhu, Wallet–>oznake–>izvoz.


Dalje, hajde da potrošimo novčiće sa prvog Address na drugi Address. Desni klik na prvi Address i izaberite “spend from” (Ovo zapravo nije neophodno u ovom scenariju, ali zamislite da imamo mnogo novčića na mnogo adresa; koristeći ovu funkciju, možemo naterati Wallet da potroši samo novčiće koje želimo. Ako želimo da izaberemo više novčića na više adresa, možemo izabrati adrese levim klikom miša dok držimo taster command, zatim desni klik i izaberemo “spend from”:


![image](assets/36.webp)


Jednom kada to uradite, na dnu prozora Wallet će se pojaviti traka Green koja pokazuje broj novčića koje ste odabrali i ukupan iznos dostupan za trošenje.


Takođe možete potrošiti pojedinačne novčiće unutar Address i isključiti druge u istom Address, ali to se ne preporučuje jer ostavljate novčiće u Address koji je kriptografski oslabljen zbog trošenja jednog od novčića (još jedan razlog da ne stavljate više novčića u jedan Address, osim iz razloga privatnosti, je taj što, s obzirom na to da biste ih trebali sve potrošiti ako potrošite jedan, ovo postaje nepotrebno skupo). Evo kako da izaberete jedan novčić iz zajedničkog Address, ali nemojte to raditi:


![image](assets/37.webp)


Sada imamo dva novčića odabrana za trošenje. Zatim smo odlučili gde da ih potrošimo. Pošaljimo ih na drugi Address. Trebaće da kopiramo Address ovako:


![image](assets/38.webp)


Zatim idite na karticu „Send“ i nalepite drugi Address u polje „pay to“. Nema potrebe da dodajete opis; možete, ali to možete učiniti kasnije uređivanjem oznaka. Za iznos, izaberite „Max“ da potrošite sve novčiće koje smo odabrali. Zatim kliknite „Pay“, a zatim kliknite dugme „advanced“ na iskačućem prozoru koji se pojavi.


![image](assets/39.webp)


Uvek kliknite na „napredno“ u ovoj fazi kako bismo dobili preciznu kontrolu i tačno proverili šta se nalazi u transakciji. Evo transakcije:


![image](assets/40.webp)


Vidimo dva unutrašnja bela okvira/prozora. Gornji je prozor za ulaze (koji novčići se troše), a donji je za izlaze (gde novčići idu).


Napomena, status (gore levo) je „unsigned“ za sada. „Poslati iznos“ je 0 jer se novčići prenose unutar Wallet. Naknada je 481 Sats. Imajte na umu da ako bi bila 480 Sats, poslednja nula bi bila izostavljena, ovako, 0.0000048 i umornom oku, ovo može izgledati kao 48 Sats – budite pažljivi (nešto što bi Electrum developeri trebalo da poprave).


Veličina transakcije odnosi se na veličinu podataka u bajtovima, ne na količinu Bitcoin. “Replace by fee” je uključen po defaultu i omogućava vam da ponovo pošaljete transakciju sa većom naknadom ako je potrebno. LockTime vam omogućava da podesite kada je transakcija važeća – još nisam eksperimentisao s tim, ali savetujem da ga ne koristite osim ako potpuno ne razumete šta radite i niste imali malo prakse sa manjim iznosima.


Na dnu, imamo neke fancy Mining alate za prilagođavanje naknada. Sve što treba da uradite za interne transfere je da postavite na minimalnu naknadu od 1 sat/bajt. Samo ručno unesite broj u polje Ciljna naknada. Da biste proverili odgovarajuću naknadu za eksterno plaćanje, možete posetiti https://Mempool.space da vidite koliko je Mempool zauzet, a prikazane su i neke predložene naknade.


![image](assets/41.webp)


Odabrao sam 1 sat/bajt.


U ulaznom prozoru vidimo dva unosa. Prvi je donacija od 5000 sat. Na levoj strani vidimo njenu transakciju Hash (koju možemo potražiti na Blockchain). Pored nje, nalazi se "21" – ovo označava da je to izlaz označen sa 21 u toj transakciji (zapravo je 22. izlaz jer je prvi označen nulom).


Nešto što treba napomenuti: UTXO-i postoje samo unutar transakcije. Da bismo potrošili UTXO, moramo ga referencirati i tu referencu staviti u ulaz nove transakcije. Izlazi tada postaju novi UTXO-i, a stari UTXO postaje STXO (Potrošeni izlaz transakcije).


Druga linija je donacija od 10.000 sat. Ima „0“ pored transakcije Hash iz koje je došla jer je to prvi (i moguće jedini) izlaz za tu transakciju.


U donjem prozoru vidimo naš Address. Primetite da zbir ulaza Bitcoin ne odgovara u potpunosti zbiru izlaza. Razlika ide na Miner. Miner gleda na neslaganje u svim transakcijama u bloku koji pokušava da iskopa, i dodaje taj broj svojoj nagradi. (Mining naknade na ovaj način su potpuno odvojene od lanca transakcija i započinju novi život).


Ako prilagodimo naknadu Mining, izlazna vrednost će se automatski promeniti.


**Vredi napomenuti ovde:** obratite pažnju na boju adresa u prozoru transakcije. Zapamtite da su Green adrese navedene u vašoj Address kartici. Ako je Address označen Green (ili žutom bojom) u prozoru transakcije, onda je Electrum prepoznao Address kao jednu od svojih. Ako Address nije označen, onda je to spoljni Address (spoljan za trenutno otvoren Wallet), i trebalo bi da ga proverite sa dodatnom pažnjom.


Kada proverite sve u transakciji i budete sigurni da ste zadovoljni kojim novčićima trošite i gde novčići idu, možete kliknuti na „finalizuj.”


![image](assets/42.webp)


Nakon što kliknete na “finalise”, više ne možete praviti izmene – Ako je potrebno, morate zatvoriti ovo i početi ispočetka. Primetite da se dugme “finalise” promenilo u “export”, i pojavila su se nova dugmad: “save”, “combine”, “sign” i “broadcast”. Dugme “broadcast” je zasivljeno jer transakcija nije potpisana i stoga je nevažeća u ovoj fazi.


Kada kliknete na potpisivanje, ako imate lozinku za Wallet, bićete upitani za nju, a zatim će se status (gore desno) promeniti iz „Nepotpisano“ u „Potpisano“. Tada će dugme „Emituj“ biti dostupno.


Nakon što emitujete, možete zatvoriti prozor transakcije. Ako odete na karticu Address, sada ćete videti da je prvi Address prazan, a drugi Address ima 1 UTXO.


Napomena: Videćete sve ove promene čak i pre nego što transakcija bude ubačena u blok, ili „potvrđena“. Ovo je zato što Electrum ažurira stanja/transakcije ne samo na osnovu Blockchain podataka, već i Mempool podataka. Ne rade svi novčanici ovo.


Nešto što treba napomenuti je da umesto emitovanja, možemo sačuvati transakciju za kasnije. Može biti sačuvana ili u nepotpisanom ili potpisanom stanju.


Kliknite na dugme „izvoz“ (paradoksalno, NEMOJTE kliknuti na dugme „sačuvaj“), i videćete nekoliko opcija. Transakcija je kodirana tekstom, i stoga može biti sačuvana na nekoliko načina.


![image](assets/43.webp)


Čuvanje u QR kod je veoma zanimljivo. Ako izaberete ovu opciju, pojaviće se QR:


![image](assets/44.webp)


Možete zatim fotografisati QR kod. Postoji nekoliko stvari koje možete uraditi sa ovim, ali za sada, recimo samo da ga kasnije učitavate nazad u Wallet. Možete zatvoriti Electrum, ponovo učitati Wallet, i otići na meni Alati:


![image](assets/45.webp)


Ovo će pokrenuti kameru vašeg računara. Zatim pokažite kameri fotografiju QR koda na vašem telefonu, i to će učitati transakciju nazad, tačno onako kako ste je ostavili.


Nije intuitivno kako učitati sačuvane transakcije, pa obratite posebnu pažnju. Učitavanje transakcije nije "alat", ali je opcija skrivena u meniju alata (još jedna stvar koju bi Electrum programeri trebali popraviti).


Sličan proces je moguć sa transakcijom sačuvanom kao fajl. Pokušajte vežbati sa bilo kojom metodom, unutar istog Wallet. Neću to ovde objašnjavati, ali možete koristiti ovu funkciju da prenesete transakciju između istog Wallet na različitim računarima, između multisignature novčanika, i ka i od hardverskih novčanika. Evo nekoliko uputstava.


Sada, vraćajući se na dugme „sačuvaj“ – ovo nije način da se sačuva tekst transakcije. Ono što ovo zapravo radi jeste da kaže Electrum Wallet da prepozna ovu transakciju na lokalnom računaru kao podnetu kao uplatu. Ako to uradite slučajno, videćete transakciju sa malom ikonicom računara. Možete kliknuti desnim tasterom miša i obrisati transakciju – ne brinite, ne možete obrisati Bitcoin na ovaj način. Electrum će tada zaboraviti da se ova transakcija ikada dogodila, i „vratiće“ Sats nazad i prikazati Sats na ispravnoj lokaciji gde zapravo postoje.


### Promenite adrese


Promene adresa su zanimljive. Morate razumeti UTXO da biste razumeli ovo objašnjenje. Ako trošite na Address iznos koji je manji od UTXO, onda će ostatak Bitcoin otići na Miner osim ako nije specificiran izlaz za kusur.


Možda imate 6.15 Bitcoin UTXO i želite potrošiti 0.15 Bitcoin da donirate nekim demonstrantima koji su potlačeni od strane tiranske “demokratske” vlade negde u svetu. Zatim biste uzeli 6.15 Bitcoin (koristeći funkciju “spend from” u Electrum-u), i stavili ga u transakciju.


Uneli biste Address demonstranata u polje „plati”, možda biste stavili „EndTheFed & WEF” u polje „opis”, a za iznos biste uneli 0.15 Bitcoin i kliknuli „plati”, zatim „napredno”.


Na ekranu transakcije, za ulazni prozor, videćete 6.15 Bitcoin UTXO. Za izlazni prozor, videćete Address koji nije istaknut (ovo je Address protestanata) sa 0.15 Bitcoin pored njega. Takođe ćete videti žuti Address sa nešto manje od 6.0 Bitcoin. Ovo je promena Address automatski izabrana od strane Wallet iz jedne od svojih žutih adresa za promene. Svrha promene Address je da Wallet može staviti kusur u njih bez ometanja dostupnosti adresa za primanje koje možda planirate koristiti ili za koje ste poslali fakture. Ako će ih kasnije koristiti kupci, na primer, ne želite da vaš Wallet automatski koristi te adrese i puni ih. To je neuredno i loše za privatnost.


Imajte na umu da će se, kako prilagođavate naknadu Mining, iznos povrata automatski prilagoditi, a ne iznos plaćanja.


### Ručno menjanje ili plati mnogima


Ovo je zaista zanimljiva funkcija Electrum-a. Pristupate joj ovako.


![image](assets/46.webp)


Zatim možete uneti više odredišta za UTXO saldo koji trošite, ovako:


![image](assets/47.webp)


Nalepite Address, upišite zarez, zatim razmak, zatim iznos, zatim <enter>, zatim to ponovite. NEMOJTE UNOSITI IZNOS U PROZORE "AMOUNT" – Electrum će popuniti ukupno ovde dok unosite pojedinačne iznose u prozor "Pay to".


Ovo vam omogućava da ručno odredite gde ide promena (npr. određeni Address u vašem Wallet, ili drugi Wallet), ili možete platiti mnogim ljudima odjednom. Ako vaš ukupni iznos nije dovoljno visok da odgovara veličini UTXO, Electrum će i dalje kreirati dodatni izlaz za promenu za vas.


Funkcija Pay to Many takođe omogućava mogućnost kreiranja sopstvenih “PayJoins” ili “CoinJoins” – van okvira ovog članka, ali imam vodič ovde. (https://armantheparman.com/cj/)


## Novčanici


Želim da demonstriram samo za gledanje Wallet koristeći Electrum. Da bih to uradio, prvo moram definisati "Wallet". Postoje dva načina na koja se "Wallet" koristi u Bitcoin:



- Tip A, „Wallet“ – odnosi se na softver koji vam prikazuje vaše adrese i stanja, npr. Electrum, Blue Wallet, Sparrow Wallet itd.



- Tip B, „Wallet“ – odnosi se na jedinstvenu kolekciju adresa koje su povezane sa kombinacijom naše seed_phrase/passphrase/derivation_path. Postoji 8,6 milijardi adresa u bilo kojem Wallet (4,3 milijarde adresa za primanje i 4,3 milijarde adresa za promenu). Ako promenite bilo šta u seed frazi, passphrase ili derivation path, dobijate neiskorišćeni Wallet sa novih, i svih jedinstvenih, 8,6 milijardi praznih adresa.


Na koji tip se neko odnosi kada koristi reč „Wallet“ je očigledno iz konteksta.


## Gledanje Wallet – vežba


Nije potpuno jasno čemu služi gledanje Wallet, ali počeću objašnjenjem šta je to, kako napraviti jedan za vežbu, a zatim ćemo se vratiti njegovoj svrsi kasnije kada objasnim više o hardverskim novčanicima. (Za detaljan pregled kako koristiti Hardware Wallet i razne specifične brendove, pogledajte ovde.)


Napravićemo lažni regularni Wallet (ovog puta dodajući malo više složenosti sa passphrase), a zatim njegov odgovarajući posmatrački Wallet. Ako želite, možete tačno kopirati onaj koji sam napravio ili kreirati svoj – ovaj Wallet treba odbaciti; nemojte ga zapravo koristiti. Počnite generisanjem 12-reči seed koristeći Ian Coleman vebsajt.


Primetite 12 nasumičnih reči na snimku ekrana ispod, i da sam uneo passphrase u polje passphrase:


passphrase: „Craig Wright je lažov i prevarant i treba da bude u zatvoru. Takođe, Ross Ulbricht treba odmah da bude pušten iz zatvora.“


passphrase može biti dug do 100 karaktera, i idealno bi trebalo da bude jednoznačan i ne previše kratak – Onaj koji sam koristio je samo za zabavu – Generalno predlažem izbegavanje velikih slova i simbola samo da biste smanjili stres prilikom pokušaja kombinacija ako ikada budete imali problem sa pamćenjem vašeg passphrase.


![image](assets/48.webp)


Zatim, u Electrum-u, idite na meni file–>new/restore. Unesite jedinstveno ime da kreirate novi Wallet i kliknite „next“.


![image](assets/49.webp)


Sledeći koraci bi vam do sada trebali biti poznati, pa ću ih navesti bez slika:



- Standard Wallet
- Već imam seed
- Kopiraj i nalepi 12 reči u okvir, ili ih unesi ručno.
- Kliknite opcije i izaberite BIP39, i takođe kliknite na passphrase kvačicu („proširi ovaj seed sa prilagođenim rečima“)
- Unesite svoj passphrase tačno onako kako ste to uradili na Ian Coleman stranici
- Ostavite podrazumevanu semantiku skripte i putanju derivacije
- Nema potrebe dodavati lozinku (zaključava Wallet)


Sada se vratite na Ian Coleman sajt, idite dole do odeljka “derivation path” i kliknite na karticu “BIP 84” da biste izabrali iste skript semantike kao podrazumevane u Electrum (Native SegWit).


![image](assets/50.webp)


Prošireni privatni i javni ključevi su odmah ispod, i menjaju se kada napravite izmene u putanji derivacije (ili bilo čemu drugom višem na stranici).


![image](assets/51.webp)


Videćete i „BIP32 extended private/public“ ključeve – za sada ih treba ignorisati.


Račun prošireni privatni ključ može se koristiti za potpuno regenerisanje vašeg Wallet. Račun prošireni javni ključ, međutim, može proizvesti samo ograničenu verziju istog Wallet (posmatrajući Wallet) – Ako stavite ovaj ključ u Electrum, on će i dalje proizvesti svih 8,6 milijardi adresa koje bi seed ili prošireni privatni ključ imao, ali neće biti dostupnih privatnih ključeva za Electrum, tako da trošenje nije moguće. Hajde da to uradimo sada da bismo demonstrirali poentu:


Kopiraj „prošireni javni ključ naloga“ u međumemoriju.


Zatim idite na Electrum, ostavite otvoren trenutni Wallet koji smo napravili, i idite na file–>new/restore. Proces pravljenja Wallet je malo drugačiji nego ranije:



- Standard Wallet
- Koristite glavni ključ
- Nalepite prošireni javni ključ u polje i nastavite
- Nema potrebe unositi passphrase; već je deo proširenog javnog ključa
- Nema potrebe ulaziti u semantiku skripte i putanju derivacije
- Nema potrebe dodavati lozinku (zaključava Wallet)


Kada se Wallet učita, trebalo bi da primetite da su učitane tačno iste adrese kao i prethodno kada je unet seed. Takođe, trebalo bi da primetite na samom vrhu u naslovnoj traci, piše „watching Wallet“. Ovaj Wallet može da vam prikaže vaše adrese i stanja (proverom stanja putem čvora), ali niste u mogućnosti da POTPIŠETE transakcije (jer watching Wallet nema privatne ključeve).


Onda koja je poenta toga?


Jedan razlog, iako ne glavni, jeste taj što potencijalno možete posmatrati svoj Wallet i njegov balans na računaru bez izlaganja vaših privatnih ključeva bilo kakvom malveru na računaru.


Drugi razlog je taj što je OBAVEZNO za obavljanje plaćanja ako odlučite da svoje privatne ključeve držite van računara; objasniću:


**Hardverski novčanici (HWW)** su kreirani kako bi uređaj mogao da čuva vaše privatne ključeve sigurno (zaključano PIN-om), da nikada ne izlaže ključeve računaru (čak i kada je povezan sa računarom putem kabla), i sami po sebi nisu u mogućnosti da se povežu na internet. Takav uređaj ne može samostalno da obavlja transakcije jer sve Bitcoin transakcije počinju referenciranjem na UTXO(e) na Blockchain (koji je na čvoru). Wallet mora da specificira u kojem transaction ID se nalazi UTXO, i koji izlaz transakcije je onaj koji treba da se potroši. Tek nakon što se specificira ulaz može se uopšte kreirati nova transakcija, a kamoli potpisati. Hardverski novčanici ne mogu da kreiraju transakcije jer nemaju pristup bilo kojim UTXO-ima – nisu povezani ni sa čim!


Prošireni javni ključ se obično izvlači iz HWW, a adrese se zatim prikazuju na računaru – mnogi ljudi će biti upoznati sa Ledger softverom ili Trezor Suite koji prikazuju adrese i stanja na njihovom računaru – ovo je posmatrajući Wallet. Ovi programi mogu kreirati transakcije, ali ne mogu potpisivati. Oni mogu imati transakcije potpisane samo od strane HWW-ova koji su povezani sa njima. HWW preuzima novo generisanu transakciju od posmatrajućeg Wallet, potpisuje je, a zatim je šalje nazad na računar za emitovanje čvoru. **HWW ne može sam emitovati**, njegov povezani posmatrajući Wallet to radi. Na ovaj način, dva novčanika (javni ključ Wallet na računaru i privatni ključ Wallet u HWW) sarađuju da generate, potpisuju i emituju, sve dok se osigurava da privatni ključevi ostanu izolovani i dalje od uređaja povezanog na internet.


## Delimično potpisane Bitcoin transakcije (PSBTs)


Moguće je da se transakcija kreira i sačuva u fajl, kasnije ponovo učita, potpiše, sačuva, ponovo učita i na kraju emituje – ne kažem da bi neko to trebao da uradi; samo kažem da je to moguće.


Sada razmotrite 3 od 5 multisignature Wallet – 5 privatnih ključeva kreira Wallet, a 3 su potrebna da bi se u potpunosti potpisala transakcija (Pogledajte ovde da saznate više o multisignature Wallet ključevima). Moguće je imati 5 različitih računara, svaki sa jednim od pet privatnih ključeva.


Računar jedan bi mogao generate transakciju i potpisati je. Zatim bi mogao sačuvati je u fajl i poslati je putem emaila Računaru 2. Računar 2 može zatim potpisati, i potencijalno sačuvati fajl u QR kod, i preneti QR putem Zoom poziva Računaru 3 na drugom kraju sveta. Računar 3 može uhvatiti QR, učitati transakciju u electrum, i potpisati transakciju. Nakon prva 2 potpisa, transakcija je bila PSBT (Partially Signed Bitcoin Transaction). Nakon trećeg potpisa, transakcija je postala potpuno potpisana i validna, spremna za emitovanje.


Da biste saznali više o PSBTS, pogledajte ovaj vodič. (https://armantheparman.com/PSBT/)


## Korišćenje hardverskih novčanika sa Electrum-om


Imam vodič o korišćenju hardverskih novčanika uopšte, za koji mislim da bi bilo važno da ga pročitaju ljudi koji su novi u HWW-ima. (https://armantheparman.com/using-hwws/)


Postoje i vodiči o raznim brendovima HWW-ova koji se povezuju sa Sparrow Bitcoin Wallet, a mogu se pronaći ovde. (https://armantheparman.com/hwws/)


Ovo će biti moj prvi vodič koji pokazuje kako koristiti Hardware Wallet sa Electrum – Koristiću ColdCard Hardware Wallet za demonstraciju. Ovo nije zamišljeno kao detaljan vodič o ColdCard-u, taj vodič je ovde. Samo pokazujem tačke specifične za Electrum. (https://armantheparman.com/cc/)


### Povezivanje putem micro SD kartice (bez mreže)


Pre nego što povežete vaš pravi Wallet putem ColdCard-a, nadam se da ste prošli kroz prethodne korake učitavanja Electrum lažnog Wallet i postavljanja mrežnih parametara.


Zatim, na ColdCard-u, umetnite SD karticu. Pretpostavljam da ste već kreirali vaš seed. Ako pristupate Wallet sa passphrase, primenite ga sada. Pomerite se nadole i izaberite meni Advanced/Tools –>Export Wallet –> Electrum Wallet.


Možete se pomeriti nadole i pročitati poruku. Uvek vam nudi da odaberete “1” za unos broja računa koji nije nula (nešto što je deo putanje derivacije), ali ako ste pratili moj savet, niste menjali podrazumevane putanje derivacije, tako da nećete želeti broj računa koji nije nula; samo pritisnite znak za potvrdu da nastavite.


Zatim izaberite semantiku skripte. Većina ljudi će izabrati „Native SegWit“.


Reći će „Electrum Wallet file written“, i prikazaće ime datoteke. Mentalno ga zabeležite.


Zatim izvadite micro SD karticu i stavite je u računar sa Electrumom.


Neki operativni sistemi će automatski otvoriti istraživač datoteka kada umetnete microSD. Mnogi ljudi će videti novu Wallet datoteku i dvaput kliknuti na nju, i pitati se zašto ne radi. To nije sjajan dizajn. Zapravo morate ignorisati istraživač datoteka (zatvoriti ga), i otvoriti Wallet datoteku koristeći Electrum:


Otvorite Electrum. Ako je već otvoren sa nekim drugim Wallet, izaberite file –> new. Tražimo ovaj prozor:


![image](assets/52.webp)


Evo trik, nije intuitivan. Kliknite „choose“. Zatim pretražite sistem datoteka na microSD kartici i pronađite Wallet datoteku i otvorite je.


Sada ste otvorili svoj Hardware Wallet i odgovarajući Wallet za gledanje. Lepo.


### Povezivanje putem USB kabla.


Ovaj način bi trebao biti lakši, ali za Linux računare, mnogo je teže. Nešto što se zove "Udev pravila" treba da se ažurira. Evo kako (detaljan vodič https://armantheparman.com/gpg-articles/ ), i ukratko:


Dobro je osigurati da je sistem ažuriran. Zatim:


```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```


onda...


```bash
python3 -m pip install ckcc-protocol
```


Ako dobijete grešku, proverite da li je pip instaliran. Možete proveriti sa (pip –version), a možete ga instalirati sa (sudo apt install python3-pip)


Kreirajte ili modifikujte postojeći fajl, /etc/udev/rules.d/


Kao ovo:


```bash
sudo nano /etc/udev/rules.d
```


Uređivač teksta će se otvoriti. Kopirajte tekst odavde i nalepite ga u datoteku rules.d, sačuvajte i izađite.


![image](assets/53.webp)


Zatim pokrenite ove komande jednu za drugom:


```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```


Ako dobijete poruku „group plugdev“ već postoji, to je u redu, nastavite. Nakon druge komande, nećete dobiti povratnu informaciju/odgovor, samo nastavite sa trećom komandom.


Možda ćete morati da isključite i ponovo povežete ColdCard sa računarom.


Ako ni nakon svega ovoga ne možete povezati ColdCard, pokušao bih ažurirati firmware (uskoro vodič, ali za sada možete pronaći uputstva na web stranici proizvođača).


Dalje, kreirajte novi Wallet:



- Standard Wallet
- Koristite hardverski uređaj
- Skeniraće i detektovati vaš ColdCard. Nastavite.
- Odaberite semantiku skripte i putanju derivacije
- Odlučite da li datoteku Wallet treba šifrovati (preporučeno)


### Transakcije korišćenjem ColdCard


Sa povezanim kablom, transakcije su jednostavne. Potpisivanje transakcija će biti bez problema.


Ako koristite uređaj na način koji je izolovan od mreže, morate ručno preneti sačuvanu transakciju između uređaja koristeći microSD karticu. Postoje neki trikovi.


Nakon kreiranja transakcije i njenog finalizovanja, potrebno je da kliknete na dugme za izvoz u donjem levom uglu. Videćete “save to file” što, paradoksalno, nije ono što želimo. Zapravo, prvo morate otići do poslednje opcije u meniju koja kaže “for hardware wallets”, a zatim, unutar tog izbora, pronaći drugi “save to file” i odabrati to. Zatim sačuvajte fajl na microSD, izvadite karticu i stavite je u ColdCard. Zapamtite da možda treba da primenite passphrase da biste izabrali tačan Wallet. Ekran će prikazati da je spreman za potpisivanje. Kliknite na kvačicu, pregledajte transakciju i nastavite potvrđivanjem kvačicom. Kada završite, izvadite karticu i vratite je u računar.


Zatim treba da otvorimo transakciju koristeći electrum. Funkcija je skrivena u meniju alati –> učitaj transakciju. Navigirajte kroz sistem fajlova i pronađite fajl. Svaki put kada potpišete, biće tri fajla. Originalni sačuvani fajl koji je Watching Wallet napravio, i dva koja je napravio ColdCard (ne znam zašto to radi). Jedan će imati oznaku “signed” a drugi “final”. Nije intuitivno, ali “signed” nije koristan, treba da otvorimo “final” transakciju.


Jednom kada to učitate, možete kliknuti na „emituj“ i uplata će biti izvršena.


## Ažuriranje Electrum-a i skriveni direktorijum “.electrum”


Electrum živi na vašem računaru na dva mesta. Postoji sama aplikacija, i postoji skriveni konfiguracioni folder. Taj folder se nalazi na različitim mestima u zavisnosti od vašeg operativnog sistema:


Prozori:


```bash
C:/Users/your_user_name_goes_here/AppData/Roaming/Electrum
```


Mac:


```bash
/Users/your_user_name_goes_here/.electrum
```


Linux:


```bash
/home/your_user_name_goes_here/.electrum
```


Imajte na umu da `.` pre `electrum` na Linuxu i Macu – to označava da je direktorijum skriven. Takođe, imajte na umu da se ovaj direktorijum kreira (automatski) tek kada prvi put pokrenete Electrum. Direktorijum sadrži konfiguracioni fajl electrum-a, kao i direktorijum koji čuva sve novčanike koje ste sačuvali.


Ako izbrišete Electrum program sa svog računara, skriveni direktorijum će ostati, osim ako ga i vi aktivno ne izbrišete.


Da biste nadogradili electrum, prolazite kroz isti postupak kao što sam opisao na početku za preuzimanje i verifikaciju. Zatim ćete imati dve kopije programa na svom računaru i možete pokrenuti bilo koju – svaki program će pristupiti istom skrivenom electrum folderu za svoju konfiguraciju i Wallet pristup. Sve stvari koje smo sačuvali, kao što su osnovna jedinica, podrazumevani čvor za povezivanje, druge postavke i pristup novčanicima, ostaće jer je sve to sačuvano u tom folderu.


### Premještanje vašeg Electrum-a i novčanika na drugi računar


Da biste to uradili, možete kopirati programske fajlove na USB drajv, a takođe kopirati i .electrum direktorijum. Zatim ih kopirajte ili premestite na novi računar. Ne morate ponovo verifikovati program. Uverite se da kopirate .electrum direktorijum na podrazumevanu lokaciju (zapamtite da ga kopirate PRE nego što pokrenete Electrum prvi put na tom računaru, inače će se popuniti prazna podrazumevana .electrum fascikla, što bi vas moglo zbuniti).


## Etikete


Kao što sam ranije objasnio, na kartici Address postoji kolona sa oznakama. Možete dvaput kliknuti tamo i uneti beleške za sebe (to je samo na vašem računaru, nije javno i nije na Blockchain).


![image](assets/54.webp)


Kada premestite svoj Electrum Wallet na drugi računar, možda ćete želeti da ne izgubite sve te beleške. Možete ih sačuvati u datoteku koristeći meni, Wallet > labels > export, a zatim na novom računaru koristiti Wallet > labels > import.


## Saveti:


Ako smatrate da je ovaj resurs koristan i želite da podržite ono što radim za Bitcoin, možete donirati neki Sats ovde:


Static Lightning Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/electrum/