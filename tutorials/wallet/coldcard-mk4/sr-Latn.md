---
name: COLDCARD Mk4
description: Vodič za postavljanje i korišćenje COLDCARD Mk4 sa Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Hardware wallets** su fizički uređaji napravljeni isključivo za sigurno čuvanje privatnog ključa Bitcoin. Oni čuvaju privatne ključeve offline, što znači da hakeri ne mogu doći do njih putem interneta. Dok se **softverski wallets** uglavnom koriste za svakodnevne transakcije, **hardverski wallets** se često koriste za sigurno čuvanje većih količina bitcoina na duži vremenski period. Kada se vrši Bitcoin transakcija koristeći **hardverski wallets**, wallet može potpisati transakcije unutar uređaja, tako da privatni ključ nikada nije izložen okruženjima povezanima na internet.


U ovom vodiču, istražićemo jedan od najpopularnijih hardvera wallets koje proizvodi Coinkite, Coldcard Mk4. Pogledaćemo kako postaviti i koristiti ovaj hardver wallet za obavljanje Bitcoin transakcija.


## Pregled Coldcard Mk4


Coldcard Mk4 je Bitcoin-only hardver wallet proizveden od strane Coinkite. Ovaj uređaj je opremljen ekranom, numeričkom tastaturom i zaštitnim kliznim poklopcem. Pored toga, uređaj nudi nekoliko načina povezivanja i interakcije, uključujući USB-C, rad u izolovanom režimu koristeći MicroSD karticu, NFC i režim virtuelnog diska. Mk4 takođe uključuje napredne sigurnosne funkcije kao što su BIP39 passphrase i trik PIN-ovi, pružajući korisnicima veću kontrolu i zaštitu nad njihovim Bitcoin.


## Početno podešavanje: PIN i reči protiv fišinga


Da biste započeli, Coldcard Mk4 se može kupiti direktno sa [Coinkite's website](https://store.coinkite.com/store). Kupci takođe mogu izabrati da plate koristeći fiat valutu ili Bitcoin. Pored toga, biće vam potrebna i MicroSD kartica (4 GB je dovoljno) i izvor napajanja koji se može povezati putem USB-C kabla (Coldcard Mk4 ima samo USB-C ulaz za napajanje). Imajte na umu da, pošto Mk4 nema ugrađenu bateriju, mora biti povezan na izvor napajanja sve vreme dok se koristi.


Primićete svoj Mk4 u vrećici koja pokazuje da li je otvarana. Molimo vas da se uverite da vrećica nije kompromitovana. Ako primetite nešto što može biti problem, kao što je oštećenje ili cepanje vrećice, možete obavestiti Coinkite slanjem emaila na support@coinkite.com. Pored toga, možete pronaći 12-cifreni broj na vrećici koja pokazuje da li je otvarana, koji ćemo nazvati brojem vrećice Mk4. Ovaj broj vrećice će se kasnije koristiti za verifikaciju da uređaj nije bio kompromitovan tokom transporta i da dolazi direktno od Coinkite. Broj vrećice je sigurno pohranjen u Coldcard-ovom secure element koristeći OTP (One-Time-Programmable) fleš memoriju, što znači da se ne može promeniti nakon programiranja. Kada prvi put uključite uređaj, broj prikazan na ekranu mora odgovarati onom na vrećici. Ovo osigurava da je Mk4 koji ste primili originalni uređaj iz fabrike i da nije zamenjen ili modifikovan. Iako ova verifikacija potvrđuje samo integritet uređaja u trenutku prvog uključivanja, secure element nastavlja da štiti vaše privatne ključeve, PIN i passphrase, čineći izuzetno teškim da bilo kakvo neovlašćeno menjanje ugrozi vaš Bitcoin. Pored toga, dobre prakse, kao što je pravilno osiguranje podataka vezanih za vaš wallet, biće korisne za ukupnu sigurnost samog Coldcard-a. Za dodatne informacije, možete se obratiti ovom [članku](https://blog.coinkite.com/understanding-mk4-security-model/) koji detaljno objašnjava sigurnosni model Coldcard-a.


Tastatura se sastoji od 10 numeričkih dugmadi, OK (`✓`) dugmeta i dugmeta za otkazivanje (`✕`). Neka numerička dugmad se takođe mogu koristiti za navigaciju: `5` za navigaciju gore (`^`), `7` za navigaciju levo (`<`), `8` za navigaciju dole `˅`, i `9` za navigaciju desno (`>`).


![01](assets/en/01.webp)


Ako nema problema sa pakovanjem, možete otvoriti torbu. Mk4 će doći sa wallet rezervnom karticom koja se može koristiti za čuvanje informacija o PIN-u uređaja, rečima protiv phishinga i seedphrase. Pratite sledeće korake za inicijalizaciju:


1. Pripremite papir i olovku.

2. Povežite Mk4 na izvor napajanja (USB-C kabl) i umetnite MicroSD karticu.

3. Kada se uređaj prvi put uključi, ekran će prikazati poruku u vezi sa Uslovima prodaje i korišćenja Coldcard. Pomerite se nadole, zatim pritisnite `✓` za nastavak.

4. Zatim će se na ekranu prikazati broj od 12 cifara. Proverite ovaj broj sa onim na vreći sa zaštitom od neovlašćenog otvaranja i dodatnom kopijom broja vreće koja je uključena u vreću sa zaštitom od neovlašćenog otvaranja kako biste se uverili da uređaj nije bio otvaran. Ako se brojevi ne podudaraju, odmah kontaktirajte podršku Coinkite pre nego što nastavite. U suprotnom, pritisnite `✓` za nastavak.


![02](assets/en/02.webp)


5. Izaberite `Choose PIN Code`.

6. Krećite se nadole dok čitate uputstva da biste prešli na sledeći korak.


![03](assets/en/03.webp)


7. Na Mk4, kreirajte i unesite prefiks PIN-a (mora imati od 2 do 6 karaktera) i zapišite ga, zatim pritisnite `✓` za nastavak.

8. Zapišite dve reči prikazane na ekranu. Ovo su reči za zaštitu od fišinga. Pritisnite `✓` da nastavite.


![04](assets/en/04.webp)


9. Kreirajte i unesite sufiks PIN-a (ili ostatak PIN-a, mora imati od 2 do 6 karaktera) i zapišite ga. Pritisnite `✓` za nastavak.

10. Ponovo unesite svoj PIN prefiks. Pritisnite `✓` za nastavak.


![05](assets/en/05.webp)


11. Proverite da li su anti-phishing reči iste kao one koje ste napisali u koraku 8. Pritisnite `✓` da nastavite.

12. Ponovo unesite sufiks PIN-a (ili ostatak PIN-a). Pritisnite `✓` za nastavak.


![06](assets/en/06.webp)


13. PIN i reči protiv krađe identiteta za vaš Mk4 su sada uspešno kreirani i sačuvani na uređaju.


![07](assets/en/07.webp)


Imajte na umu da će Mk4 uvek tražiti da unesete svoj PIN svaki put kada uključite svoj uređaj. Bez ovog PIN-a, ne možete pristupiti svom Coldcard Mk4. Zato se pobrinite da napravite dovoljne rezervne kopije za PIN i reči protiv krađe identiteta.


## Postavljanje vašeg Wallet


Sledeći korak je postavljanje vašeg wallet. Postoje tri načina da to uradite:


- Kreiranje novog wallet (standard)
- Kreiranje novog wallet sa bacanjem kockica
- Uvoz wallet


### Kreiranje novog wallet (standard)


Da biste kreirali novi wallet, jednostavno uradite sledeće korake.


1. Izaberite `New Wallet` (ili `New Seed Words`) > Izaberite `12 Word` ili `24 Word (default)` u zavisnosti od vaših preferencija.


![08](assets/en/08.webp)


2. Uređaj će generisati 12 ili 24 reči kao vaš seedphrase na osnovu vašeg izbora. Navigirajte nadole dok pažljivo zapisujete svaku reč redosledom kojim se pojavljuje. Zatim pritisnite `✓` za nastavak.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Uređaj će vas zamoliti da verifikujete vaš seedphrase tako što će postavljati pitanja nasumičnim redosledom (na primer, `Reč 1 je?`, zatim `Reč 5 je?`, zatim `Reč 12 je?`, i tako dalje) i za svako pitanje će biti ponuđene tri reči. Pogledajte belešku iz Koraka 2 i izaberite tačne reči (pritiskom na `1`, `2` ili `3`, u zavisnosti od toga koja opcija odgovara tačnoj reči) kako biste završili kreiranje wallet.


![09](assets/en/09.webp)


4. Mk4 će zatim pitati da li želite da omogućite NFC/Tap ili ne. Za sada, izaberite `✕` za ovu opciju. Ovo se može promeniti u podešavanjima u budućnosti.

5. Konačno, Mk4 će takođe ako želite onemogućiti USB port (koji se može koristiti za prenos podataka bez vazdušnog jaza). Za sada, izaberite `✓` za ovu opciju. Ovo se može promeniti u podešavanjima u budućnosti.

6. Ekran će sada prikazati glavni meni sa `Ready to Sign` na vrhu. Ovo označava završetak procesa kreiranja wallet.


![10](assets/en/10.webp)


### Kreiranje novog wallet sa bacanjem kockica


Alternativno, možete se odlučiti i za generisanje novog seedphrase sa entropijom. Uradite to ako ne verujete Mk4-ovom sveže generisanom seedphrase.


Procedura na Coldcard Mk4 je sledeća:


1. Izaberite `New Wallet` (ili `New Seed Words`) > Izaberite `12 Word Dice Roll` ili `24 Word Dice Roll` u zavisnosti od vaših preferencija.

2. Bićete zamoljeni da unesete rezultate bacanja kockica. Svako bacanje kockica dodaje slučajnost procesu kreiranja wallet, osiguravajući da vaš seedphrase bude generisan na potpuno siguran i nepredvidiv način. Minimalan broj bacanja je 50 za 12-rečeni seedphrase i 99 za 24-rečeni seedphrase. Pritisnite `✓` nakon što unesete najmanje 99 vrednosti bacanja kockica.


![11](assets/en/11.webp)


3. Uređaj će generisati 12 ili 24 reči kao vaš seedphrase na osnovu vašeg izbora. Pomaknite se nadole dok pažljivo zapisujete svaku reč redosledom kojim se pojavljuju. Zatim pritisnite `✓` za nastavak.

4. Uređaj će vas zamoliti da verifikujete vaš seedphrase tako što će postavljati pitanja nasumičnim redosledom (na primer, `Reč 1 je?`, zatim `Reč 5 je?`, zatim `Reč 12 je?`, i tako dalje) i za svako pitanje će biti ponuđena tri izbora reči. Pogledajte belešku iz Koraka 3 i izaberite tačne reči (pritiskom na `1`, `2` ili `3`, u zavisnosti od toga koja opcija odgovara tačnoj reči) kako biste završili kreiranje wallet.


![12](assets/en/12.webp)


5. Mk4 će zatim pitati da li želite da omogućite NFC/Tap ili ne. Za sada, izaberite `✕` za ovu opciju. Ovo se može promeniti u podešavanjima u budućnosti.

6. Konačno, Mk4 će takođe ako želite onemogućiti USB port (koji se može koristiti za prenos podataka bez vazdušnog jaza). Za sada, izaberite `✓` za ovu opciju. Ovo se može promeniti u podešavanjima u budućnosti.

7. Ekran će sada prikazati glavni meni sa `Ready to Sign` na vrhu. Ovo označava završetak procesa kreiranja wallet.


![13](assets/en/13.webp)


### Uvoz wallet


Konačna opcija je da uvezete wallet. To možete učiniti ako želite da povratite wallet iz seedphrase koji već imate. Možete pratiti ove korake:


1. Izaberite `Import Existing`.

2. Odaberite `24 Reči`, `18 Reči` ili `12 Reči`, u zavisnosti od broja reči vašeg seedphrase.


![14](assets/en/14.webp)


3. Coldcard Mk4 će vas zatim pitati šta je svaka reč u uzastopnom redosledu. Za svaku reč, navigirajte dole ili gore dok ne pronađete pravi prefiks za svaku reč. Uređaj će suziti mogućnosti dok ne pronađete tačnu reč. Uradite ovo za ostale reči.

4. Za poslednju reč, Coldcard Mk4 će prikazati samo ograničen broj mogućih reči. Ako nema podudaranja, možda ste pogrešno uneli reči. U suprotnom, izaberite reč koja se podudara sa onom na vašem seedphrase.


![15](assets/en/15.webp)


5. Mk4 će zatim pitati da li želite da omogućite NFC/Tap ili ne. Za sada, izaberite `✕` za ovu opciju. Ovo se može promeniti u podešavanjima u budućnosti.

6. Konačno, Mk4 će takođe ako želite onemogućiti USB port (koji se može koristiti za prenos podataka bez vazdušnog jaza). Za sada, izaberite `✓` za ovu opciju. Ovo se može promeniti u podešavanjima u budućnosti.

7. Ekran će sada prikazati glavni meni sa `Ready to Sign` na vrhu. Ovo označava završetak procesa kreiranja wallet.


![16](assets/en/16.webp)


Imajte na umu da je seedphrase jedini pristup za povratak vašeg wallet. Napravite rezervnu kopiju vašeg seedphrase i čuvajte je na sigurnom mestu. **Nisu vaši ključevi, nisu vaši novčići**, ko god ima vaš seedphrase ima pristup vašim bitcoinima!


## Postavljanje vašeg passphrase


Jedna od najboljih praksi u Bitcoin je korišćenje passphrase. passphrase deluje kao 13. ili 25. reč pored seedphrase. Ono što ga čini drugačijim je to što možete izabrati koju god frazu želite, dok se seedphrase bira iz unapred određenog spiska od 2048 reči. Podrazumevano, nakon postavljanja vašeg wallet, počećete sa wallet sa praznim passphrase. Da biste postavili ne-prazan passphrase, jednostavno uradite sledeće korake:


1. Idite na `Passphrase`.

2. Pomaknite se nadole da pročitate opis o passphrase, zatim pritisnite `✓` da nastavite.

3. Izaberite `Edit Phrase`.


![17](assets/en/17.webp)


4. Unesite svoj passphrase:


   - Pritisnite `1` (slova), `2` (brojevi) ili `3` (simboli) da biste izabrali tip karaktera.
   - Pritisnite `4` da biste promenili mala i velika slova (može se koristiti samo prilikom unosa slova).
   - Krećite se pomoću `^` ili `˅` da biste izabrali karakter za vaš passphrase.
   - Krećite se koristeći `<` ili `>` za pomeranje između karaktera. Takođe možete koristiti `>` za dodavanje razmaka.
   - Pritisnite `✕` da obrišete znakove.
   - Pritisnite `✓` kada završite uređivanje passphrase.

5. Pored toga, ostale opcije imaju sledeće funkcionalnosti:


   - `Add Word` ili `Add Numbers` može se koristiti za dodavanje slova/brojeva na passphrase koji trenutno uređujete.
   - Pritisnite `Clear ALL` da resetujete passphrase koji trenutno uređujete.
   - Pritisnite `CANCEL` da se vratite u glavni meni.

6. Zapišite svoj passphrase kao rezervnu kopiju.

7. Pritisnite `APPLY` da pristupite wallet sa passphrase koji ste upravo postavili.

8. Mk4 će zatim prikazati otisak glavnog ključa dužine 8 karaktera. Ovo se može smatrati "ID"-em wallet. Zapišite ovaj otisak i pritisnite `✓` za nastavak.


![18](assets/en/18.webp)


9. Sada će wallet prikazati glavni meni wallet sa passphrase koji ste uneli.

10. Važno je napomenuti da wallet neće ukazati da ste uneli pogrešan passphrase, jer svaki passphrase odgovara svom wallet sa jedinstvenim identitetom (otisak glavnog ključa). Stoga je dobra praksa ponovo uneti isti passphrase i proveriti da li proizvodi isti otisak wallet, kako biste osigurali da ste ga ispravno uneli. Da biste to uradili, izvršite Korake 11 do 14.

11. Na glavnom meniju, izaberite `Restore Master`, zatim pritisnite `✓`. Sada ste ponovo u glavnom meniju wallet sa praznim passphrase.


![19](assets/en/19.webp)


12. Idite na `Passphrase` ponovo, zatim pritisnite `✓` da nastavite.

13. Ponovo unesite passphrase koji ste zapisali u Koraku 6, zatim pritisnite `APPLY`.

14. Proverite otisak glavnog ključa dužine 8 karaktera sa onim koji ste zapisali u Koraku 8. Ako se oba otiska ne podudaraju, možda ste uneli pogrešne karaktere. Možete izabrati novi passphrase i ponoviti proces od Koraka 1. Ali ako se oba otiska podudaraju, to znači da ste ispravno uneli passphrase.

15. wallet sa vašim izabranim passphrase je spreman za upotrebu.


## Izvoz Wallet u Sparrow


Kao i drugi hardverski wallet, Coldcard Mk4 ne može se koristiti samostalno. Potrebno je da bude povezan sa softverskim wallet koji deluje kao interfejs. Softverski wallet omogućava vam da pregledate svoj saldo, kreirate transakcije i upravljate adresama, dok Coldcard bezbedno potpisuje te transakcije bez ikakvog izlaganja vaših privatnih ključeva.


U ovom vodiču, koristićemo Sparrow Wallet kao interfejs. Procedura za izvoz wallet je sledeća:


1. Uverite se da imate umetnutu MicroSD karticu u Mk4.

2. Izvršite korake "Postavljanje vašeg passphrase" na wallet sa passphrase koji želite da izvezete. Ako želite da izvezete wallet sa praznim passphrase, možete preskočiti ovaj korak.

3. Idite na `Advanced/Tools` > Izaberite `Export Wallet` > Odaberite `Generic JSON` > Skrolujte naniže dok čitate uputstva, zatim pritisnite `✓`.


![20](assets/en/20.webp)


4. Mk4 je sada kreirao datoteku sa `.json` formatom na MicroSD kartici.


![21](assets/en/21.webp)


5. Uklonite MicroSD karticu iz Cold kartice i umetnite je u uređaj gde su instalirani Sparrow Wallet.

6. Otvori Sparrow Wallet.

7. Kliknite na `File`


![22](assets/en/22.webp)


Zatim, kliknite na `New Wallet`


![23](assets/en/23.webp)


Zatim unesite ime za wallet


![24](assets/en/24.webp)


Nakon toga, kliknite na `Create Wallet`


![25](assets/en/25.webp)


8. Izaberite `Tip skripte`.


![26](assets/en/26.webp)


9. U odeljku Keystore izaberite `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Potraži Coldcard i klikni na `Import File...`.


![28](assets/en/28.webp)


11. Izaberite datoteku koja je kreirana u Koraku 4 (onu sa `.json` formatom).


![29](assets/en/29.webp)


12. Na Mk4, vratite se na glavni meni i idite na `Advanced/Tools` > `View Identity`. Uverite se da otisak prsta prikazan na ekranu Mk4 odgovara onom na Sparrow Wallet (glavni otisak prsta u odeljku Keystore)

13. Kliknite dugme `Apply` u donjem desnom uglu.


![30](assets/en/30.webp)


14. Opcionalno, možete dodati lozinku za izvezeni wallet. Ova lozinka je potrebna svaki put kada otvorite aplikaciju Sparrow Wallet za pristup wallet. Ako zaboravite lozinku u budućnosti, jednostavno možete ponoviti Korake 1-13 i odabrati novu lozinku.


![31](assets/en/31.webp)


15. wallet je sada uspešno izvezen i spreman za upotrebu.


![32](assets/en/32.webp)


## Primanje bitcoina


Dalje ćemo naučiti kako primiti Bitcoin koristeći Mk4. Ovaj proces je prilično jednostavan jer ne morate koristiti sam Mk4 uređaj. Sve dok ste već izvezli svoj wallet u Sparrow, možete primiti Bitcoin direktno preko Sparrow Wallet. Pratite ove korake da primite bitkoine sa Mk4:


1. Otvori Sparrow Wallet.

2. Izaberite `Open Wallet` > Odaberite wallet fajl na koji želite da primite bitcoin > Unesite lozinku povezanu sa tim wallet.


![33](assets/en/33.webp)


3. Na interfejsu Sparrow kliknite na karticu `Receive` na levoj strani interfejsa.


![34](assets/en/34.webp)


4. Adresa zajedno sa QR kodom će se pojaviti na vrhu. Možete kopirati i nalepiti adresu ili skenirati QR kod koristeći wallet koji ćete koristiti za slanje bitcoina na Sparrow Wallet. Opcionalno, možete uneti oznaku za bitcoin koji primate.


![35](assets/en/35.webp)


5. Nakon što pošaljete bitkoine, na interfejsu Sparrow kliknite na karticu `Transactions` na levoj strani interfejsa. Videćete novi unos na vrhu istorije transakcija, koji odgovara transakciji koju ste upravo izvršili.


![36](assets/en/36.webp)


6. Takođe možete navigirati na kartici `UTXOs` na levoj strani interfejsa da biste videli bitcoin koji ste upravo primili.


![37](assets/en/37.webp)


## Slanje bitcoina


Za razliku od primanja bitkoina, trošenje bitkoina povezanih sa vašom Cold karticom zahteva da koristite Cold karticu za potpisivanje transakcija. Procedura slanja bitkoina sa Mk4 je sledeća:


1. Ubacite MicroSD karticu u uređaj gde je instaliran vaš Sparrow Wallet.

2. Otvori Sparrow Wallet.

3. Izaberite `Open Wallet` > Odaberite wallet fajl koji želite da koristite za slanje bitkoina > Unesite lozinku povezanu sa tim wallet.


![38](assets/en/38.webp)


4. Na interfejsu Sparrow, kliknite na karticu `Send` na levoj strani interfejsa.


![39](assets/en/39.webp)


5. Na kartici `Pay to` unesite adresu na koju želite poslati bitkoine.

6. Dodajte oznaku za transakciju.

7. Unesite količinu bitkoina koju želite poslati.

8. Unesite naknadu prebacivanjem `Range` ili direktnim unosom broja u deo `Fee`.


![40](assets/en/40.webp)


9. U donjem desnom uglu kliknite na `Create Transaction`.


![41](assets/en/41.webp)


10. Bićete prebačeni u novu karticu transakcije čije je ime oznaka koju ste uneli u Koraku 6. Kliknite na `Finalize Transaction for Signing`.


![42](assets/en/42.webp)


11. Kliknite `Save Transaction` i sačuvajte transakciju na MicroSD kartici. Preimenujte datoteku ako je potrebno. Ovaj korak će sačuvati transakciju kao PSBT datoteku.


![43](assets/en/43.webp)


12. Izvadite MicroSD karticu i umetnite je u vaš Coldcard Mk4.

13. Uključite svoj Mk4 povezivanjem na izvor napajanja.

14. Unesite svoj PIN.

15. Idite na `Passphrase` i unesite passphrase od wallet koji želite da koristite za slanje bitkoina. Ako želite da koristite wallet sa praznim passphrase, preskočite ovaj korak.

16. Uverite se da je otisak glavnog ključa isti kao onaj na vašem Sparrow Wallet. Ovo možete proveriti na kartici `Settings` na levoj strani interfejsa Sparrow Wallet. Zatim pritisnite `✓` na vašem Mk4 da nastavite. Ovo će vas odvesti do glavnog menija.

17. Na glavnom meniju Mk4, izaberite `Ready to Sign`. Ekran će prikazati poruku `OKAY TO SEND?`. Proverite da li su iznos bitkoina koji želite poslati i adresa primaoca tačni. Pritisnite `✓` za potvrdu ili `✕` za otkazivanje.

18. Ako postoji više PSBT fajlova za izbor, Mk4 će prikazati poruku `Choose PSBT file to be signed`. Pritisnite `✓` za nastavak. Zatim, izaberite PSBT fajl koji želite da potpišete navigacijom dole ili gore. Izvršite Korak 17 na toj transakciji.


![44](assets/en/44.webp)


19. Mk4 će sada prikazati poruku `PSBT Signed` zajedno sa imenom datoteke potpisanog PSBT. Pritisnite `✓` za nastavak.

20. Uklonite MicroSD karticu iz Cold kartice i umetnite je u uređaj gde su instalirani Sparrow Wallet.

21. Na Sparrow Wallet, kliknite na `Load Transaction`.


![45](assets/en/45.webp)


22. Odaberite datoteku sa istim imenom kao onu kreiranu u Koraku 19.


![46](assets/en/46.webp)


23. Kliknite `Broadcast Transaction`.


![47](assets/en/47.webp)


24. Vaša transakcija je emitovana i trenutno se obrađuje. Možete otići na karticu `Transakcije` da biste videli status potvrde vaše transakcije.


![48](assets/en/48.webp)


## Ažuriranje firmvera


### Provera verzije firmvera


Firmware za Coldcard Mk4 uvek se može nadograditi na noviju verziju. Da biste proverili da li je vaš Mk4 nadograđen na najnoviju verziju ili ne, izvršite sledeće korake:

1. Uključite svoj Mk4 povezivanjem na izvor napajanja.

2. Unesite svoj PIN.

3. Idite na `Advanced/Tools` > Izaberite `Upgrade Firmware` > Izaberite `Show Version`.


![49](assets/en/49.webp)


Proverite verziju prikazanu na ekranu Mk4 sa onom na [Coinkite's website](https://coldcard.com/downloads). Ako je verzija drugačija, možete nadograditi firmware na noviju verziju.


![50](assets/en/50.webp)


### Ažuriranje vašeg firmvera


Ako želite da nadogradite firmver na najnoviju verziju, uradite sledeće korake:


1. Ubacite MicroSD karticu u vaš laptop/PC.

2. Idite na [Coinkite's website](https://coldcard.com/downloads) i preuzmite najnoviji firmware na vašu MicroSD karticu (Crveno dugme desno od Mk4 slike sa brojem verzije na njemu).


![51](assets/en/51.webp)


Takođe možete preuzeti druge verzije klikom na `All Files on Mk4` i istraživanjem verzije koju želite da preuzmete. Preuzeta datoteka će biti u `.dfu` formatu.


![52](assets/en/52.webp)


3. Uklonite MicroSD karticu i umetnite je u vaš Mk4.

4. Uključite svoj Mk4 povezivanjem na izvor napajanja.

5. Unesite svoj PIN.

6. Idite na `Advanced/Tools` > Izaberite `Upgrade Firmware` > Izaberite `From MicroSD` > Skrolujte nadole dok čitate uputstva, zatim pritisnite `✓`.


![53](assets/en/53.webp)


7. Izaberite `.dfu` datoteku koju ste preuzeli u Koraku 2.

8. Coldcard Mk4 će prikazati poruku `Install this new firmware?`. Pomerajte se nadole dok čitate uputstva, a zatim pritisnite `✓`.


![54](assets/en/54.webp)


9. Sačekajte da Mk4 završi instalaciju novog firmvera. Ne isključujte izvor napajanja tokom instalacije.

10. Po završetku, Mk4 će se ponovo pokrenuti. Možete uneti svoj PIN i izvršiti korake "Provera verzije firmvera" da biste proverili da li je firmver nadograđen ili ne.


## Napredne funkcije


### Promenite svoj PIN


Ako želite da promenite svoj PIN za prijavu, jednostavno izvršite sledeće korake:


1. Pripremite olovku i parče papira.

2. Uključite svoj Mk4 povezivanjem na izvor napajanja.

3. Unesite svoj PIN.

4. Idite na `Settings` > Izaberite `Login Settings` > Izaberite `Change Main PIN`

5. Krećite se naniže dok čitate poruku, zatim pritisnite `✓` da nastavite.


![55](assets/en/55.webp)


6. Unesite svoj stari PIN.

7. Unesite novi prefiks PIN-a (mora imati od 2 do 6 karaktera) i zapišite ga.

8. Mk4 će sada prikazati dve nove reči za zaštitu od fišinga, zapišite ih, a zatim pritisnite `✓` da nastavite.

9. Unesite novi sufiks PIN-a (ili ostatak PIN-a, mora imati od 2 do 6 karaktera) i zapišite ga.


![56](assets/en/56.webp)


10. Ponovo unesite svoj novi prefiks PIN-a.

11. Proverite da li se reči za zaštitu od krađe identiteta podudaraju sa onima koje ste napisali u Koraku 8.

12. Ponovo unesite novi sufiks PIN-a (ili ostatak PIN-a).


![57](assets/en/57.webp)


13. Vaš PIN je uspešno promenjen.


### Trik PIN-ovi - Dodaj novi trik


Trik PIN je alternativni PIN kod različit od onog koji koristite za postavljanje vaše Cold kartice Mk4 po prvi put. Kada uključite vaš Mk4, možete uneti trik PIN(ove) umesto vašeg Glavnog PIN-a da biste pokrenuli određene akcije. Da biste konfigurisali trik PIN u Mk4, možete uraditi sledeće korake:


1. Pripremite olovku i parče papira.

2. Uključite svoj Mk4 povezivanjem na izvor napajanja.

3. Unesite svoj PIN.

4. Idite na `Settings` > Izaberite `Login Settings` > Izaberite `Trick PINs` > Izaberite `Add New Trick`.


![58](assets/en/58.webp)


5. Unesite prefiks za trik PIN (mora imati od 2 do 6 karaktera) i zapišite ga.

6. Mk4 će sada prikazati dve nove reči za zaštitu od fišinga, zapišite ih, a zatim pritisnite `✓` da nastavite.

7. Unesite sufiks vašeg trik PIN-a (ili ostatak PIN-a, mora biti dug od 2 do 6 karaktera) i zapišite ga.


![59](assets/en/59.webp)


8. Pomerite se dole ili gore da biste izabrali akciju koju želite da povežete sa trikom PIN koji ste upravo kreirali. Lista akcija je:


    - `Brick Self`, kada je odabrano, čipovi vašeg Mk4 će biti uništeni nakon što se unese PIN, čineći vaš Mk4 trajno neupotrebljivim.
    - `Wipe Seed`, možete izabrati između sledećih akcija:
      - `Wipe & Reboot`: seed je obrisan i Coldcard će se ponovo pokrenuti nakon što se unese PIN.
      - `Silent Wipe`: seed se briše tiho, međutim Coldcard će se ponašati kao da je PIN unet pogrešno.
      - `Wipe -> Wallet`: seed se tiho briše, a Cold kartica će vas odvesti u wallet pod pritiskom.
    - `Duress Wallet`, kada je odabran, vaš Mk4 će dovesti do duress wallet nakon što se unese PIN.
    - `Login Countdown`, you can choose between the folowing actions:
      - `Brisanje & Odbrojavanje`: seed se odmah briše, zatim Mk4 počinje prikazivati odbrojavanje.
      - `Odbrojavanje & Brick`: Odbrojavanje počinje i Mk4 će se "brick"-ovati nakon što istekne vreme.
      - `Just Countdown`: Mk4 će započeti odbrojavanje i ponovo će se pokrenuti nakon što istekne vreme.
    - `Look Blank`, kada je odabrano, nakon što se unese lažni PIN, Cold kartica se ponaša kao da je seedphrase obrisana, ali je zapravo i dalje u memoriji.
    - `Just Reboot`, kada je odabrano, Coldcard će se ponovo pokrenuti nakon što se unese trik PIN.
    - `Delta Mode`, Ova napredna funkcija namenjena je iskusnim korisnicima i dizajnirana je da štiti od ozbiljnih pretnji, kao što je prinuda od strane nekoga sa insajderskim znanjem. Kada je Delta Mode aktiviran, COLDCARD izgleda kao da otvara pravi wallet, omogućavajući napadaču da pregleda i potvrdi da izgleda autentično. Međutim, tajno blokira sve potpisivanje transakcija, tako da se bitcoin ne može poslati. Takođe onemogućava pristup seed frazi, a svaki pokušaj da se ona pogleda će je potpuno izbrisati. Da bi lažni wallet izgledao uverljivije, Trick PIN korišćen za Delta Mode mora početi istim brojevima kao pravi PIN (tako da prikazuje iste anti-phishing reči) ali se završava drugačije.
    - `Policy Unlock`, kada je odabrano, Single Signer Spending Policy (SSSP) će biti onemogućen nakon što se unese lažni PIN.
    - `Policy Unlock & Wipe`, kada je odabrano, pretvara se da onemogućava SSSP, ali će obrisati seedphrase u tom procesu.

9. Nakon što odaberete radnju koju želite da uparite sa trik PIN-om, potvrdite svoj izbor pritiskom na `✓`. Vaš trik PIN je uspešno konfigurisan.

10. U `Settings` > `Login Settings` > `Trick PINs`, možete videti listu trik PIN-ova koje ste kreirali i akcije povezane sa njima. Možete odabrati da rekonfigurišete trik PIN-ove i akcije povezane sa njima. Takođe ih možete sakriti ili obrisati tako što ćete odabrati PIN, a zatim izabrati `Hide Trick` ili `Delete Trick`.


![60](assets/en/60.webp)


### Trik PIN-ovi - Dodaj ako je pogrešno


Alternativno, možete dodati akciju `Add If Wrong` koja će se pokrenuti nakon što se pogrešan PIN unese određeni broj puta. Ovo možete konfigurisati izvođenjem sledećih koraka:


1. Uključite svoj Mk4 povezivanjem na izvor napajanja.

2. Unesite svoj PIN.

3. Idite na `Settings` > Izaberite `Login Settings` > Izaberite `Trick PINs` > Izaberite `Add If Wrong`.


![61](assets/en/61.webp)


4. Mk4 će prikazati poruku u vezi sa ovom postavkom. Pomaknite se naniže dok čitate objašnjenje, zatim pritisnite `✓` da nastavite.

5. Unesite broj pogrešnih pokušaja potrebnih za pokretanje akcije. Napomena: Maksimalan broj pokušaja je `12`. Ovo je zato što je Mk4 dizajniran tako da kada se pogrešan PIN unese `13` puta, uređaj će se blokirati i postati trajno neupotrebljiv. Nakon što unesete broj, pritisnite `✓` za nastavak.

6. Krećite se gore ili dole da biste izabrali akciju. Dostupne akcije su sledeće:


   - `Obriši, Stop`: seedphrase je obrisan i uređaj prikazuje “Seed je obrisan, Stop.”
   - `Obriši & Ponovo pokreni`: seedphrase se briše i uređaj se ponovo pokreće bez ikakve poruke.
   - `Silent Wipe`: seedphrase se tiho briše i uređaj se ponaša kao da je unet pogrešan PIN (nema očigledne poruke o brisanju).
   - `Brick Self`: Uređaj je trajno onemogućen i prikazuje samo „Bricked.”
   - `Poslednja šansa`: seedphrase je izbrisan, ali imate još jedan pokušaj za unos PIN-a; unesite pogrešan PIN ponovo i uređaj će biti neupotrebljiv.
   - `Samo Restartuj`: Uređaj se jednostavno ponovo pokreće i ništa drugo se ne menja.

Izaberite radnju koju želite da primenite i pritisnite `✓` da nastavite


![62](assets/en/62.webp)


7. Bićete vraćeni u direktorijum `Settings > Login Settings > Trick PINs`. Ispod `Trick PINs:` naći ćete listu trik pinova zajedno sa akcijom `WRONG PIN`. Takođe možete sakriti ili obrisati odabirom PIN-a, a zatim odaberite `Hide Trick` ili `Delete Trick`.


![63](assets/en/63.webp)



## Zaključak


Ovaj vodič pruža uputstvo o tome kako postaviti Mk4, kako obavljati Bitcoin transakcije sa Mk4 i kako koristiti neke napredne funkcije Mk4. Nudi sigurne i fleksibilne načine za čuvanje i upravljanje vašim bitcoinima. Njegov dizajn osigurava da privatni ključevi nikada ne napuštaju uređaj, dok funkcije kao što su passphrases, trik PIN-ovi i transakcije bez mreže daju korisnicima potpunu kontrolu nad njihovim sigurnosnim postavkama. Može se upariti sa Sparrow Wallet za korisnički prijatno iskustvo kreiranja, potpisivanja i upravljanja Bitcoin transakcijama bez ugrožavanja privatnosti ili sigurnosti.


Ako želite da istražite druge funkcionalnosti, možete pogledati dokumentaciju na vebsajtu Coinkite [ovde](https://coldcard.com/docs/). Nadam se da ćete ovaj vodič smatrati korisnim kada budete koristili svoj Coldcard Mk4. Hvala i vidimo se sledeći put!