---
name: SeedSigner
description: Hardware Wallet koji je DIY, bez stanja, pristupačan i potpuno izolovan od mreže
---

![cover](assets/cover.webp)



SeedSigner je open-source Hardware Wallet Bitcoin koji svako može sam izgraditi koristeći jeftine, univerzalne elektronske komponente. Za razliku od komercijalnih proizvoda kao što su Ledger, Coldcard ili Trezor, ovo nije gotov uređaj proizveden od strane kompanije: to je projekat zajednice koji omogućava svima da kreiraju svoj uređaj, kontrolišući svaki korak.



SeedSigner je dizajniran da bude 100% ***air-gapped***: nikada se ne povezuje na Internet, nema Wi-Fi ili Bluetooth (u slučaju Raspberry Pi Zero v1.3) i nikada nije povezan na računar za Exchange podatke. Komunikacija je isključivo putem QR koda Exchange sistema. Konkretno, vaš softver za upravljanje portfoliom (kao što je Sparrow wallet) prikazuje transakciju koja treba da se potpiše u obliku QR kodova; skenirate ih kamerom SeedSignera, zatim uređaj potpisuje transakciju koristeći vaše privatne ključeve privremeno smeštene u njegovoj RAM memoriji. Na kraju, generiše QR kodove koji sadrže potpisanu transakciju, koje skenirate svojim softverom da biste je poslali na Bitcoin mrežu.



![Image](assets/fr/001.webp)



SeedSigner je takođe ***stateless***. Drugim rečima, ne čuva trajno vaš seed ili vaše privatne ključeve, za razliku od drugih hardverskih novčanika. Svaki put kada ponovo pokrenete uređaj, njegova memorija je potpuno prazna, osim ako ne konfigurišete uređaj da sačuva vaša podešavanja na microSD kartici. Stoga morate ponovo uneti vaš seed svaki put kada ga koristite, a najpraktičniji metod je da ga sačuvate u obliku QR koda, koji se skenira pri pokretanju pomoću SeedSigner-ove kamere. Ovaj način rada značajno smanjuje površinu napada: čak i ako lopov ukrade vaš uređaj, neće pronaći nikakve informacije na njemu, jer je uvek prazan po defaultu.



Još jedna opcija za čuvanje vašeg seed i korišćenje sa SeedSigner-om je korišćenje *SeedKeeper* pametne kartice u kombinaciji sa kompatibilnim čitačem. Ovo vam pruža veoma robustan *secure element* za čuvanje vašeg seed, dok koristite ekran SeedSigner-a za potpisivanje transakcija. Ali ova posebna konfiguracija je tema drugog posvećenog vodiča. Ovde ćemo se koncentrisati na osnovnu upotrebu SeedSigner-a:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Projekat SeedSigner zauzima važno mesto u ekosistemu Bitcoin, jer svima, svuda u svetu, nudi mogućnost da iskoriste naprednu sigurnost za zaštitu svojih bitkoina. Njegova glavna prednost leži u pristupačnosti: potrebni hardver može se kupiti za manje od $50. Štaviše, omogućava ljudima koji žive u ograničenim zemljama da izgrade svoj sopstveni Hardware Wallet od standardnih računarskih komponenti, koje je lako pronaći i koje su manje podložne regulatornim ograničenjima.



Ali čak i izvan ovih posebnih konteksta, SeedSigner može biti zanimljiva opcija za vas: open-source je, radi bez stanja i bez povezivanja, i smanjuje vektore napada povezane sa Supply lancem vašeg Hardware Wallet.



## 1. Potrebna oprema



Da biste napravili svoj SeedSigner, biće vam potrebne sledeće komponente:





- Raspberry Pi Zero
    - Verzija 1.3 se preporučuje, jer nema ni Wi-Fi ni Bluetooth, što osigurava potpunu izolaciju.
 - W i v2 verzije su takođe kompatibilne, ali uključuju Wi-Fi/Bluetooth čip. Stoga je preporučljivo fizički ga deaktivirati uklanjanjem radio modula sa kartice. Operacija je relativno jednostavna, ali zahteva preciznost (fina klješta su dovoljna za Zero W, dok je za v2 potrebna Hot olovka da bi se uklonila metalna ploča koja skriva modul). Neću ulaziti u detalje u ovom vodiču, ali sve instrukcije ćete pronaći u ovom dokumentu: *[Disabling WiFi/Bluetooth by hardware](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Imajte na umu: neki modeli Raspberry Pi Zero se prodaju bez unapred zalemljenih GPIO pinova. Možete ili kupiti verziju sa integrisanim pinovima direktno (najjednostavnije rešenje), ili kupiti pinove zasebno i zalemiti ih sami (složenije rešenje).
 - Ne zaboravite uključiti micro-USB napajanje Supply.



![Image](assets/fr/002.webp)





- Waveshare 1.3" ekran (240×240 px)** (en français)
    - Važno je odabrati upravo ovaj model: postoje drugi slični ekrani, ali sa drugačijom rezolucijom. Bez definicije od 240×240 px, ekran će biti neupotrebljiv.
    - Prikaz uključuje tri dugmeta i mini-džojstik koji služi kao korisnikov Interface.



![Image](assets/fr/003.webp)





- Kamera kompatibilna sa Raspberry Pi Zero**
    - Opcija 1: standardna kamera sa širokim zlatnim okvirom (proverite kompatibilnost sa vašim kućištem).
    - Opcija 2: kompaktnija kamera "*Zero*", dizajnirana posebno za Pi Zero.



![Image](assets/fr/004.webp)





- MicroSD** kartica
    - Preporučeni kapacitet: između 4 i 32 GB.





- Housing (opciono, ali preporučeno)** (opciono, ali preporučeno)** (opciono, ali preporučeno)** (opciono, ali preporučeno)** (preporučeno)
    - Štiti uređaj i olakšava korišćenje.
    - Najpopularniji model je "*Orange Pill Case*", za koji su [dostupni STL fajlovi otvorenog koda za 3D štampu](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Kutije su takođe dostupne kod [nezavisnih prodavaca povezanih sa projektom](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Možete kupiti ove komponente zasebno ili, radi veće jednostavnosti, odabrati gotove pakete koji uključuju sav potreban hardver. Lično, naručio sam svoj paket [sa ovog francuskog sajta](https://bitcoinbazar.fr/), ali ćete takođe pronaći listu prodavaca za svaki region sveta na [SeedSigner stranici za hardver](https://seedsigner.com/hardware/). Ako više volite da kupujete komponente pojedinačno, dostupne su na glavnim e-commerce platformama ili u specijalizovanim prodavnicama.



## 2. Priprema softvera



Kada sakupite svoj hardver, potrebno je da pripremite microSD karticu instaliranjem SeedSigner sistema na nju. Da biste to uradili, idite na svoj svakodnevni lični računar i priključite microSD karticu namenjenu za SeedSigner.



### 2.1. Preuzimanje



Idite na [zvanično GitHub spremište projekta](https://github.com/SeedSigner/seedsigner/releases). Na najnovijoj verziji softvera, preuzmite :




- `.img` slika koja odgovara vašem Pi modelu.
- Datoteka `.sha256.txt`.
- Datoteka `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Pre nego što započnemo instalaciju, hajde da proverimo softver.



### 2.2 Verifikacija pod Linux-om i macOS-om



Počnite tako što ćete uvesti zvanični javni ključ projekta SeedSigner direktno sa Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminal bi trebalo da vam kaže da je ključ uvezen ili ažuriran. Zatim, pokrenite komandu za verifikaciju na datoteci sa potpisom (zapamtite da modifikujete komandu prema vašoj verziji, ovde `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Ako je sve ispravno, izlaz bi trebao glasiti `Good signature`. To znači da je datoteka `.sha256.txt` potpisana ključem koji ste upravo uvezli i da je potpis važeći. Zanemarite poruku upozorenja `WARNING: This key is not certified with a trusted signature`: ovo je normalno, jer je sada na vama da proverite da li ključ pripada projektu SeedSigner.



Da biste to uradili, uporedite poslednjih 16 karaktera otiska prsta prikazanog sa onima dostupnim na [Keybase.io/SeedSigner](https://keybase.io/seedsigner), na njihovom [zvaničnom Twitteru](https://twitter.com/SeedSigner/status/1530555252373704707), ili u fajlu objavljenom na [SeedSigner.com](https://seedsigner.com/keybase.txt). Ako se ovi identifikatori tačno poklapaju, možete biti sigurni da je ključ zaista od projekta. Ako ste u nedoumici, odmah prestanite i zatražite pomoć od SeedSigner zajednice (Telegram, X, GitHub...).



Kada je ključ validiran, možete proveriti da preuzeta slika nije modifikovana (zapamtite da izmenite komandu u skladu sa vašom verzijom, ovde `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Pod Linuxom, ova komanda je ugrađena.
- Upozorenje: macOS verzije pre `Big Sur (11)` ne prepoznaju opciju `--ignore-missing`. U tom slučaju, uklonite je i ignorišite upozorenja o nedostajućim fajlovima.



Očekivani rezultat je `OK` pored `.img` fajla. Ovo potvrđuje da je otpremljena slika identična onoj koju je objavio projekat i da nije modifikovana.



### 2.3 Verifikacija Windows-a



Na Windows-u, procedura je slična, ali su komande različite. Počnite instaliranjem [Gpg4win](https://www.gpg4win.org/) i otvorite aplikaciju *Kleopatra*. Uvezite javni ključ projekta SeedSigner sa URL-a Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Zatim, otvorite PowerShell u fascikli gde se nalaze vaši preuzeti fajlovi (`Shift` + desni klik > `Open PowerShell here`). Pokrenite sledeću komandu da proverite potpis manifesta (ne zaboravite da izmenite komandu prema vašoj verziji, ovde `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Ako je sve ispravno, izlaz bi trebao glasiti `Good signature`. To znači da je datoteka `.sha256.txt` potpisana ključem koji ste upravo uvezli i da je potpis važeći. Ignorišite poruku upozorenja `WARNING: This key is not certified with a trusted signature`: ovo je normalno, jer je sada na vama da proverite da li ključ koji je korišćen pripada projektu SeedSigner.



Da biste to uradili, uporedite poslednjih 16 karaktera otiska prsta prikazanog sa onima dostupnim na [Keybase.io/SeedSigner](https://keybase.io/seedsigner), na njihovom [zvaničnom Twitteru](https://twitter.com/SeedSigner/status/1530555252373704707), ili u fajlu objavljenom na [SeedSigner.com](https://seedsigner.com/keybase.txt). Ako se ovi identifikatori tačno poklapaju, možete biti sigurni da je ključ zaista od projekta. Ako ste u nedoumici, odmah prestanite i zatražite pomoć od SeedSigner zajednice (Telegram, X, GitHub...).



Kada je ključ validiran, potrebno je proveriti da li slika fajl nije oštećen. Da biste to uradili, koristite sledeću komandu u PowerShell-u :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Primer za Raspberry Pi Zero 2 (ne zaboravite da izmenite komandu u skladu sa vašom verzijom, ovde `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell zatim izračunava Hash SHA256 vaše slikovne datoteke. Uporedite ovaj Hash sa odgovarajućom vrednošću u `seedsigner.0.8.6.sha256.txt`.




- Ako su dve vrednosti strogo identične, provera je uspešna i možete nastaviti.
- Ako se razlikuju, datoteka je oštećena ili korumpirana. Nemojte je koristiti i ponovo pokrenite preuzimanje.



![Image](assets/fr/013.webp)



Uspešna verifikacija garantuje da je vaš `.img` fajl i autentičan (potpisan od strane SeedSigner) i neizmenjen (nemodifikovan). Nakon toga možete bezbedno preći na sledeći korak.



### 2.4. Flešuj sliku



Ako ga već nemate, preuzmite softver [Balena Etcher] (https://etcher.balena.io/), zatim :




- Umetnite microSD karticu u vaš računar.
- Pokreni Etcher.
- Odaberite preuzetu i verifikovanu `.img` datoteku.
- Izaberite microSD karticu kao cilj.
- Kliknite na `Flash!`.



![Image](assets/fr/014.webp)



Sačekajte dok se proces ne završi: vaša microSD kartica je spremna za upotrebu. Sada je vreme za sklapanje!



## 3. Sklapanje SeedSignera



Kada vaša microSD kartica bude pripremljena i na nju bude instaliran SeedSigner softver, možete nastaviti sa finalnom montažom. Radite polako, jer su neki delovi osetljivi (posebno stolnjak, kamera i GPIO pinovi).



### 3.1 Priprema kućišta



Prvo, otvorite kućište. Proverite da je čisto i da nema zaostalih plastičnih delova od 3D štampe koji ometaju unutrašnje pričvršćivače. Obratite pažnju na:




- Lokacija kamere (mala kružna rupa napred).
- Otvaranje za ekran.
- Izrezi za micro-USB portove i microSD slot na Raspberry Pi Zero.



### 3.2 Instalacija kamere



Pronađite konektor za traku kamere na Raspberry Pi Zero: to je tanak crni trak sa strane ploče, koji se može malo podići da se otvori. Pažljivo ga podignite, bez forsiranja: trebalo bi da se jednostavno nagne nekoliko milimetara.



![Image](assets/fr/015.webp)



Umetnite poklopac kamere. Braon/bakreni deo treba da bude okrenut nadole. Uverite se da je čvrsto postavljen u konektor, bez uvrtanja.



![Image](assets/fr/016.webp)



Zatvorite crnu traku da zaključate stolnjak (osetićete blagi klik). Pažljivo proverite da li ostaje na mestu i da se ne pomera.



![Image](assets/fr/017.webp)



Zatim postavite modul kamere u odgovarajuću rupu u kućištu. U zavisnosti od modela, može se direktno pričvrstiti ili zahtevati malu lepljivu traku da ga drži na mestu. Sočivo mora biti savršeno poravnato, okrenuto ka spolja.



### 3.3 Instaliranje Raspberry Pi Zero



Ako koristite kućište, umetnite Raspberry Pi Zero ploču unutra. Pažljivo poravnajte portove sa predviđenim otvorima.



Zatim postavite Waveshare displej na vrh Raspberry Pi Zero. GPIO pinovi na Pi-ju treba da se savršeno poklope sa ženskim konektorom displeja. Polako pritisnite displej na pinove, primenjujući ravnomeran pritisak sa svake strane kako biste izbegli njihovo savijanje.



![Image](assets/fr/018.webp)



Ako imate kućište, dovršite sklapanje dodavanjem prednje ploče i džojstika.



Konačno, ubacite microSD karticu koja sadrži flešovani softver u bočni slot Raspberry Pi Zero uređaja. Uverite se da je kartica kliknula na mesto.



### 3.4 Prvo pokretanje



Povežite micro-USB kabl za napajanje na namenski port. Sačekajte oko jedan minut. Trebalo bi da se pojavi SeedSigner logo, a zatim početni ekran.



![Image](assets/fr/019.webp)



Za početak, proverite da li različite komponente rade ispravno tako što ćete otići na meni `Settings > I/O test`.



![Image](assets/fr/020.webp)



Testirajte sve dugmiće i proverite da li pravilno reaguju. Zatim kliknite na dugme `KEY1` da proverite da li kamera radi kako se očekuje. Ovo će napraviti fotografiju.



![Image](assets/fr/021.webp)



### 3.5 Podešavanje kamere



U zavisnosti od toga kako ste montirali vaš SeedSigner, kamera može prikazivati obrnuti prikaz. Da biste to ispravili, idite na `Settings > Advanced > Camera rotation` i izaberite rotaciju od 180° ako je potrebno.



![Image](assets/fr/022.webp)



Ako ste promenili orijentaciju kamere ili želite da promenite druga podešavanja (kao što je jezik Interface) kasnije, moraćete da omogućite trajnost podešavanja na microSD kartici. U suprotnom, vaša podešavanja će se vratiti na podrazumevana svaki put kada ponovo pokrenete uređaj, jer Raspberry Pi Zero nema trajnu memoriju.



Da biste to uradili, otvorite meni `Settings > Persistent settings`, zatim izaberite `Enabled`.



![Image](assets/fr/023.webp)



Ako je sve funkcionalno, vaš SeedSigner je sada spreman za upotrebu!



## 4. SeedSigner postavke



Pre nego što kreirate svoj Bitcoin Wallet, hajde da konfigurišemo SeedSigner. Pošto radi na Raspberry Pi Zero bez trajne memorije, njegova podešavanja se ne čuvaju automatski osim ako ih ne sačuvate na microSD kartici. Zato se uverite da ste omogućili ovu opciju, inače će ova podešavanja biti izgubljena pri ponovnom pokretanju (pogledajte korak 3.5).



### 4.1 Pristup meniju parametara



Pokrenite svoj SeedSigner i sačekajte da se pojavi početni ekran. Koristeći džojstik, idite na opciju `Settings`, zatim potvrdite pritiskom na centralno dugme. Sada ulazite u glavni meni podešavanja.



![Image](assets/fr/024.webp)



### 4.2 Biranje softvera za upravljanje portfoliom



Zatim pristupite meniju `Coordinator software`.



![Image](assets/fr/025.webp)



`Coordinator` se odnosi na softver za upravljanje portfoliom s kojim će vaš SeedSigner komunicirati putem QR kodova. Ovaj softver je instaliran ili na vašem računaru ili na vašem pametnom telefonu. Omogućiće vam upravljanje vašim bitcoinima, ali bez ikakvog pristupa vašim privatnim ključevima. SeedSigner ostaje jedini uređaj sposoban da potpisuje vaše transakcije.



Trenutna verzija firmvera podržava nekoliko softverskih paketa: Sparrow, Specter, BlueWallet, Nunchuk i Keeper. U mom slučaju, koristim **Sparrow wallet**, koji posebno preporučujem zbog njegove jednostavnosti i bogate funkcionalnosti.



Ako ne znate kako da ga instalirate, možete pratiti ovaj vodič:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Jednostavno izaberite softver po vašem izboru iz menija.



![Image](assets/fr/026.webp)



### 4.3 Prikaz jedinica i količine



U meniju `Denomination Display` možete izabrati jedinicu u kojoj će iznosi biti prikazani:




- `BTC`
- mBTC` (mili-Bitcoin, ili 0.001 BTC)
- gW-20 (satošiji, ili 1/100,000,000 BTC)



Jedinica **Sats** je generalno najpraktičnija za male količine.



![Image](assets/fr/027.webp)



### 4.4 Napredna podešavanja



Sada idite na meni `Advanced`. Ovde ćete pronaći nekoliko korisnih opcija:




- gW-22 network`: da se menja samo ako želite da koristite SeedSigner na Testnet.
- gustina QR koda`: podešava količinu informacija sadržanih u svakom QR kodu. Možete ostaviti podrazumevanu vrednost, osim ako smatrate da je teško čitati prilikom skeniranja.
- `Xpub export`: omogućava ili onemogućava izvoz vašeg proširenog javnog ključa (`xpub`, `ypub`, `zpub`) u softver za upravljanje portfoliom putem QR koda (funkcija koju ćemo koristiti kasnije, pa je za sada ostavite omogućenu).
- `Script types`: definiše tipove skripti dozvoljene za zaključavanje vaših bitkoina. Ne morate menjati ovaj parametar, jer će tip skripte biti direktno postavljen na Sparrow. Ovde su u pitanju samo skripte koje SeedSigner ima ovlašćenje da manipuliše.



### 4.5 Izbor jezika



Konačno, u meniju `Language`, možete promeniti jezik Interface prema vašim preferencijama.



![Image](assets/fr/028.webp)



## 5. Kreiranje i čuvanje seed



seed (ili Mnemonic fraza) čini osnovu vašeg Bitcoin portfolija. Koristi se za generisanje vaših privatnih ključeva i adresa, i omogućava pristup vašim sredstvima. SeedSigner nudi nekoliko metoda za njeno generisanje, koje ćemo istražiti u ovom delu.



Pre nego što počnemo, nekoliko osnovnih podsetnika:




- Ova fraza vam daje pun, neograničen pristup svim vašim bitcoinima.** Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem SeedSigner-u ;
- Obično se koristi fraza od 12 reči za vraćanje Wallet ako je Hardware Wallet izgubljen ili ukraden. Ali pošto je SeedSigner *bez stanja* uređaj, nikada ne registruje vaš seed. Tako da vaši fizički bekapi nisu samo rezervne kopije, već **jedini način da koristite vaš Wallet**. Ako izgubite ove bekape, vaši bitkoini će biti trajno izgubljeni. Zato ih pažljivo bekapujte, na nekoliko medija i na sigurnim mestima;
- Ako tek počinjete, toplo vam savetujem da pročitate ovaj vodič za detaljno razumevanje rizika povezanih sa upravljanjem Mnemonic frazom :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Pristupite alatu za kreiranje seed



Sa početnog ekrana SeedSigner-a, idite na meni `Tools`.



![Image](assets/fr/029.webp)



Sada ćete generate svoj seed. seed je jednostavno veliki nasumični broj. Što je nasumičnije generisan, to je sigurniji. SeedSigner nudi dva načina za to:




- kamera": seed se generiše iz vizuelnog šuma fotografije. Snimite sliku nasumičnog okruženja (objekat, pejzaž, lice, itd.) čije varijacije piksela se koriste za generate entropiju. To je brza metoda, ali nije reproduktivna.
- bacanja kockica": bacate kockice kako biste stvorili potrebnu entropiju. To oduzima više vremena, ali je ponovljivo i stoga proverljivo. Ako se odlučite za ovu metodu, pratite savete u ovom vodiču (nema potrebe da ovde izračunavate kontrolni zbir, SeedSigner se time bavi):



https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Kreiranje seed sa fotografijom



Ako izaberete metodu fotografije, kliknite na `New seed` (sa ikonom kamere), uslikajte i potvrdite. Zatim izaberite dužinu vaše rečenice (12 ili 24 reči), koja će se pojaviti na ekranu za čuvanje. Sledeći koraci su identični delu 5.3.



### 5.3 Kreiranje seed sa kockicama



U ovom vodiču koristimo metodu **Bacanja kockica**. Kliknite na `New seed` (sa ikonom kockice).



![Image](assets/fr/030.webp)



Zatim izaberite dužinu vaše Mnemonic fraze. 12 reči već nude dovoljan nivo sigurnosti, tako da je to izbor koji preporučujem.



![Image](assets/fr/031.webp)



Bacite kockice i unesite dobijene brojeve koristeći kursor. Pritisnite centralno dugme da potvrdite svaki unos. Ako napravite grešku, možete se vratiti nazad. Koristite nekoliko različitih kockica da smanjite uticaj bilo koje neuravnotežene kockice. Uverite se da vas niko ne posmatra tokom ove operacije.



![Image](assets/fr/032.webp)



Kada unesete svojih 50 bacanja, SeedSigner generiše vašu rečenicu. **Pažljivo pratite uputstva u ovom vodiču ako tek počinjete:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Prikaz i čuvanje seed



Pažljivo zapišite reči vaše Mnemonic fraze na odgovarajući fizički nosač (papir ili metal).



![Image](assets/fr/033.webp)



### 5.5 Provera rezervne kopije



Da biste izbegli greške u bekapu, SeedSigner vas traži da verifikujete svoj bekap. Kliknite na `Verify`.



![Image](assets/fr/034.webp)



Zatim unesite traženu reč prema njenom redosledu u rečenici. Na primer, ovde moram da izaberem treću reč u svojoj rečenici.



![Image](assets/fr/035.webp)



Ako napravite grešku, SeedSigner će vas obavestiti, i moraćete da počnete ispočetka, pazeći da zabeležite svoju Mnemonic frazu kada vam bude data. Ovaj korak verifikacije osigurava da je vaša rezervna kopija tačna i kompletna. Kada bude potvrđena, ekran će prikazati `Backup Verified`.



![Image](assets/fr/036.webp)



Za potpuniji test restauracije, pratite ovaj vodič :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Razumevanje koncepta "uređaja bez stanja"



SeedSigner je uređaj bez trajne memorije. To znači da vaš seed nikada nije sačuvan unutar uređaja (za razliku od Ledger, Trezor ili Coldcard, na primer). Čim isključite napajanje, seed potpuno nestaje iz njegove RAM memorije. Kada se SeedSigner ponovo pokrene, vraća se u prazno stanje: moraćete ponovo da mu date vaš seed da biste potpisali vaše transakcije.



Ovo pruža suštinsku zaštitu. Za razliku od drugih hardverskih novčanika, SeedSigner je zasnovan na Raspberry Pi Zero bez fizičke zaštite, uključujući *secure element*. Ali pošto se ne čuvaju osetljivi podaci, čak i fizički kompromitovan uređaj ne bi omogućio napadaču da izvuče vaše privatne ključeve ili potroši vaše bitkoine.



S druge strane, ova arhitektura podrazumeva dodatnu odgovornost: bez rezervne kopije, vaša sredstva su definitivno izgubljena. Zato preporučujem **dvostruku rezervnu kopiju**. Već imate svoju frazu za oporavak: ovo je vaša glavna dugoročna rezervna kopija, koju treba čuvati na sigurnom mestu. Sada ćemo napraviti kopiju ove fraze u obliku **QR koda**.



Svaki put kada koristite SeedSigner, skenirate ovaj QR kod kamerom uređaja kako bi privremeno učitao vaš seed u svoju memoriju dok potpisujete svoje transakcije. Ova druga rezervna kopija, namenjena za svakodnevnu upotrebu, takođe mora biti čuvana sa najvećom pažnjom: svako ko poseduje ovaj QR kod ima potpuni pristup vašim bitcoinima.


Takođe vam savetujem da čuvate svoj QR kod i svoju Mnemonic frazu na dve odvojene lokacije, kako biste izbegli gubitak svega u slučaju zahteva.



Konačno, naprednija i sigurnija alternativa je korišćenje SeedSigner-a sa **SeedKeeper**-om, koji čuva seed u secure element. Da biste saznali više, pogledajte ovaj vodič :



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Napišite otisak prsta glavnog ključa



Kada je verifikacija završena, SeedSigner prikazuje otisak prsta glavnog ključa vašeg Wallet. Ovaj otisak prsta identifikuje vaš Wallet i osigurava da u budućnosti koristite ispravnu frazu za oporavak. Ne otkriva nikakve informacije o vašim privatnim ključevima, tako da ga možete bezbedno čuvati na digitalnom mediju. Samo se pobrinite da imate dostupnu kopiju i nikada je ne izgubite.



![Image](assets/fr/037.webp)



Takođe je u ovoj fazi da možete dodati **passphrase BIP39** kako biste pojačali sigurnost vašeg Wallet. Ova opcija može biti vredna, u zavisnosti od vaše strategije bekapa, ali takođe nosi rizike: ako izgubite passphrase, pristup vašim bitkoinima će biti trajno izgubljen.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Ako još niste upoznati sa konceptom passphrase, pozivam vas da pročitate ovaj sveobuhvatni vodič na tu temu:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Čuvanje seed u QR formatu (*SeedQR*)



SeedSigner vam omogućava da konvertujete vaš seed u papirni QR kod, nazvan *SeedQR*. Ova metoda pojednostavljuje ponovno učitavanje vašeg Wallet, jer izbegava ručno prepisivanje svake reči.



Da biste to uradili, biće vam potreban prazan papirni ili metalni QR kod koji odgovara dužini vaše Mnemonic fraze. Ako ste kupili kompletan paket za vaš SeedSigner, šabloni su obično uključeni. Ako nisu, možete ih preuzeti i odštampati (ili ručno reprodukovati) ovde:




- [12-word format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24-word format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Compact format 12 words](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Compact format 24 words](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Sa vašeg seed ekrana, izaberite `Backup seed`.



![Image](assets/fr/039.webp)



Zatim izaberite `Export as SeedQR`.



![Image](assets/fr/040.webp)



Zatim izaberite željeni format (normalan ili kompaktan) prema dostupnom šablonu za papir.



![Image](assets/fr/041.webp)



Kliknite `Begin` da biste započeli kreiranje *SeedQR*-a. SeedSigner će zatim prikazati niz mreža (A1, A2, B1, itd.), od kojih svaka odgovara delu koda.



![Image](assets/fr/042.webp)



Pažljivo reprodukuj svaku crnu tačku na svom listu za čuvanje, zatim koristi džojstik da pređeš na sledeći BLOCK. Odvoji vreme: jednostavno neusklađivanje može učiniti QR kod neupotrebljivim.



Nekoliko saveta:




- Počnite sa olovkom kako biste mogli ispraviti sve greške, a zatim se vratite korišćenju finog crnog penkala kada završite;
- Dobro centrirana tačka u sredini kvadrata je sve što vam treba, nema potrebe da ga potpuno popunite.



![Image](assets/fr/043.webp)



Zatim kliknite na `Confirm SeedQR` i skenirajte vaš QR kod da proverite da li ispravno radi.



![Image](assets/fr/044.webp)



Ako se prikaže poruka `Success`, vaš *SeedQR* je važeći: možete preći na sledeći korak.



![Image](assets/fr/045.webp)



**Čuvajte ovaj list jednako strogo kao vašu frazu za oporavak. Svako ko poseduje ovaj QR kod može rekonstruisati vaše privatne ključeve i ukrasti vaše bitkoine.**



Čestitamo, vaš Bitcoin portfelj je sada pokrenut! Sada ćemo uvesti njegove javne komponente u **Sparrow wallet** kako bismo ga lakše upravljali.



## 6. Uvezi Wallet u Sparrow



Kada je vaš SeedSigner postavljen i vaš seed ispravno generisan i sačuvan, sledeći korak je povezivanje ovog portfolija sa softverom za upravljanje kao što je Sparrow wallet. Vaš seed će uvek ostati van mreže, jer će samo javni deo vašeg portfolija biti prenet na Sparrow. Ovo će omogućiti softveru da prikaže vaše adrese, transakcije i kreira nove transakcije, bez mogućnosti da ikada potroši vaše bitkoine. Da biste potrošili svoje bitkoine, vaš SeedSigner će uvek morati da potpiše transakciju pripremljenu od strane Sparrow.



### 6.1 Priprema SeedSigner-a



Umetnite microSD koja sadrži operativni sistem, uključite vaš SeedSigner, zatim učitajte seed koji ste upravo kreirali iz vašeg rezervnog QR koda. Na početnom ekranu, izaberite `Scan`, zatim skenirajte vaš SeedQR sa SeedSigner-om.



![Image](assets/fr/046.webp)



Proverite da li otisak prsta na vašem glavnom ključu odgovara otisku prsta na vašem Wallet. Ako koristite passphrase, unesite ga u ovoj fazi.



![Image](assets/fr/047.webp)



Ovo vas vodi do menija za vaš portfolio, u mom slučaju nazvanog `d4149b27`. Ako ste ponovo na početnom ekranu, izaberite `Seeds`, zatim odaberite otisak koji odgovara vašem portfoliju. Zatim kliknite na `Export Xpub`.



![Image](assets/fr/048.webp)



Odaberite tip portfolija. U našem slučaju, to je jedan portfolio: odaberite `Single Sig`.



![Image](assets/fr/049.webp)



Sledeći dolazi izbor standarda skriptovanja. Najnoviji i najekonomičniji u smislu troškova transakcije je `Taproot`. Stoga vam savetujem da odaberete ovaj standard.



![Image](assets/fr/050.webp)



Pojaviće se poruka upozorenja. Ovo je normalno: ovaj prošireni javni ključ (`xpub`) omogućava vam da vidite sve adrese izvedene iz vašeg seed (na prvom nalogu). Ne omogućava vam da trošite svoja sredstva, ali otkriva strukturu vašeg portfolija. Ako ikada procuri, to je problem za vašu privatnost, ali ne i za sigurnost vaših bitkoina: omogućava vam da ih vidite, ali ne i da ih trošite.



Kliknite `Razumem`, zatim `Izvezi Xpub` ako ste zadovoljni prikazanim informacijama.



SeedSigner zatim generiše vaš xpub u obliku dinamičkog QR koda koji sadrži sve podatke potrebne za upravljanje vašim portfoliom u Sparrow wallet.



![Image](assets/fr/051.webp)



Možete koristiti joystick za podešavanje osvetljenosti ekrana radi lakšeg skeniranja QR koda.



### 6.2 Uvoz novog portfolija u Sparrow wallet



Uverite se da imate instaliran Sparrow wallet softver na vašem računaru. Ako ne znate kako da preuzmete, proverite i instalirajte ga ispravno, molimo vas da pogledate naš kompletan vodič na tu temu:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Na vašem računaru, otvorite Sparrow wallet, zatim u meniju kliknite `File → Import Wallet`.



![Image](assets/fr/052.webp)



Pomeri dole do `SeedSigner`, zatim izaberi `Skeniraj...`. Tvoja veb kamera će se otvoriti: skeniraj dinamički QR kod prikazan na ekranu tvog SeedSigner-a.



![Image](assets/fr/053.webp)



Dodelite ime svom portfoliju, zatim kliknite na `Create Wallet`. Sparrow će vas zatim zamoliti da postavite lozinku za zaključavanje lokalnog pristupa ovom Wallet. Izaberite jaku lozinku: ona štiti pristup podacima vašeg portfolija u Sparrow (javnim ključevima, adresama, oznakama i istoriji transakcija). Ova lozinka nije potrebna za obnavljanje portfolija u kasnijem periodu: samo vaša Mnemonic fraza (i eventualno vaš passphrase) je potrebna za ovu svrhu.



Preporučujem da sačuvate ovu lozinku u menadžeru lozinki kako biste izbegli njen gubitak.



![Image](assets/fr/054.webp)



Vaš keystore je sada uspešno uvezen.



![Image](assets/fr/055.webp)



Zatim proverite da li se `Master fingerprint` prikazan u Sparrow podudara sa onim prethodno zabeleženim u vašem SeedSigner-u.



Vaš SeedSigner i Sparrow wallet su sada sigurno povezani. Sparrow deluje kao kompletan menadžment Interface, dok SeedSigner ostaje jedini uređaj sposoban za potpisivanje vaših transakcija. Sada ste spremni da primate i šaljete bitkoine u potpuno air-gapped konfiguraciji.



## 7. Primanje i slanje bitkoina



Vaš SeedSigner i Sparrow wallet su sada konfigurisani da rade zajedno. U ovom poslednjem delu, pogledaćemo kako primati i slati bitkoine koristeći ovu konfiguraciju.



### 7.1 Primanje bitkoina



#### 7.1.1 Generisanje prijema Address



Na vašem računaru, otvorite Sparrow wallet i otključajte vaš SeedSigner Wallet koristeći vašu lozinku. Uverite se da je softver povezan sa serverom (zarez na donjem desnom uglu). U bočnoj traci, kliknite na `Receive`.



![Image](assets/fr/056.webp)



Prikazan je novi Bitcoin Address. Videćete :




- Tekst Address (počinje sa `bc1p...` ako koristiš P2TR kao ja),
- Odgovarajući QR kod,
- Polje `Label` za praćenje vaših transakcija.



Toplo preporučujem da dodate oznaku na svaki Bitcoin račun na vašem Wallet. Ovo će vam omogućiti da lako identifikujete poreklo svakog UTXO i poboljšate upravljanje privatnošću. Da biste dublje istražili ovu važnu temu, možete pogledati posvećenu obuku na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Da biste dodali oznaku, jednostavno unesite ime u polje `Label`, a zatim potvrdite.



Na primer:



```txt
Label : Sale of the Raspberry Pi Zero
```



Vaš Address je sada povezan sa ovom oznakom u svim Sparrow odeljcima.



![Image](assets/fr/057.webp)



#### 7.1.2 Address verifikacija na SeedSigner-u



Pre nego što podelite svoj primljeni Address, veoma je važno proveriti da li pripada vašem seed. Ovaj korak osigurava da vaš SeedSigner može potpisati transakcije povezane sa ovim Address. Takođe štiti od mogućih napada u kojima Sparrow prikazuje lažni Address. Zapamtite da Sparrow radi u nesigurnom okruženju (vašem računaru), koje ima mnogo veću površinu za napad nego vaš SeedSigner, koji je potpuno izolovan. Zato nikada ne treba slepo verovati bilo kojem primljenom Address prikazanom na Sparrow dok ga ne verifikujete sa vašim Hardware Wallet.



Na Sparrow, kliknite na QR kod Address da ga uvećate: zatim će biti prikazan preko celog ekrana.



![Image](assets/fr/058.webp)



Na vašem SeedSigner-u, iz glavnog menija, izaberite `Scan`. Skenirajte QR kod prikazan na ekranu vašeg računara, zatim izaberite seed koji odgovara vašem Wallet (u mom slučaju, otisak prsta `d4149b27`).



![Image](assets/fr/059.webp)



Ako skenirani Address odgovara onom izvedenom iz vašeg seed, ekran SeedSigner-a će prikazati poruku: `Address Verified`.



![Image](assets/fr/060.webp)



Ovo potvrđuje da Address pripada vašem Wallet i da možete sa sigurnošću primati bitkoine od njega.



#### 7.1.3 Prijem sredstava



Sada možete komunicirati ovaj Address (u tekstualnom ili QR kod obliku) osobi ili odeljenju koje treba da vam pošalje Satss. Kada transakcija bude emitovana na mreži, pojaviće se u kartici `Transactions` Sparrow wallet.



![Image](assets/fr/061.webp)



### 7.2 Pošalji bitkoine



Slanje bitcoina pomoću SeedSigner-a je proces u 3 koraka:




- Kreiranje transakcije u Sparrow ;
- Potpis transakcije na SeedSigner ;
- Konačna distribucija transakcije putem Sparrow.



Sva razmena između dva uređaja vrši se isključivo korišćenjem QR kodova.



#### 7.2.1 Kreiranje transakcije u Sparrow



U Sparrow wallet, možete kliknuti na karticu `Send` u bočnoj traci s leve strane. Međutim, ja više volim da koristim karticu `UTXOs`, koja vam omogućava da vežbate "*Coin Control*". Ova metoda vam daje preciznu kontrolu nad korišćenim UTXO-ima, tako da možete kontrolisati informacije koje otkrivate tokom transakcije.



U kartici `UTXOs` izaberite novčiće koje želite da potrošite, zatim kliknite na `Send Selected`.



![Image](assets/fr/062.webp)



Zatim popunite polja za transakciju:




- U `Plati`, nalepite primalacov Address ili kliknite na ikonu kamere da skenirate QR kod;
- U `Label`, dodajte oznaku za praćenje ovog troška;
- U polje `Amount` unesite iznos koji treba poslati;
- Na kraju, odaberite stopu naknade na osnovu trenutnih tržišnih uslova (procene su dostupne na [Mempool.space](https://Mempool.space/)).



Kada su polja popunjena, pažljivo proverite informacije, zatim kliknite na `Create Transaction >>`.



![Image](assets/fr/063.webp)



Proverite detalje transakcije da biste se uverili da je sve ispravno, zatim kliknite na `Finalize Transaction for Signing`.



![Image](assets/fr/064.webp)



Transakcija je sada spremna, ali još nije potpisana. Da biste prikazali [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/PSBT) kao QR kod, kliknite na `Prikaži QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Potpisivanje transakcije sa SeedSigner



Uključite svoj SeedSigner i skenirajte svoj SeedQR da biste pristupili svom portfoliju, kao i obično. Na početnom ekranu izaberite `Scan`, zatim skenirajte QR kod prikazan na Sparrow.



![Image](assets/fr/066.webp)



Zatim izaberite seed da odgovara vašem portfoliju.



![Image](assets/fr/067.webp)



SeedSigner automatski detektuje da je ovo PSBT i prikazuje rezime transakcije:




   - Iznos poslat,
   - Izlazne adrese,
   - Povezani troškovi transakcije.



Kliknite na `Review Details` i pažljivo proverite sve informacije direktno na SeedSigner ekranu. Najvažnije stavke za proveru su poslati iznos, primalac Address i iznos bilo kakvih primenjenih naknada.



![Image](assets/fr/068.webp)



Ako je sve ispravno, izaberite `Approve PSBT` da potpišete transakciju koristeći odgovarajući privatni ključ(eve).



![Image](assets/fr/069.webp)



Jednom potpisan, SeedSigner generiše novi QR kod koji sadrži potpisanu transakciju, spreman za skeniranje od strane Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Emitovanje transakcije sa Sparrow



Sada kada je transakcija važeća, potrebno je emitovati je na Bitcoin mreži, kako bi stigla do Miner koji će je dodati u BLOCK.



Na Sparrow, kliknite na `QR Scan`.



![Image](assets/fr/071.webp)



Prikažite QR kod koji prikazuje vaš SeedSigner (onaj potpisane transakcije) kameri. Sparrow će dekodirati potpis i prikazati potpune detalje transakcije. Izvršite završnu proveru da su sve informacije tačne, zatim kliknite na Emituj Transakciju da biste je emitovali na Bitcoin mreži.



![Image](assets/fr/072.webp)



Vaša transakcija je sada poslata na Bitcoin mrežu. Možete pratiti njen napredak u `Transakcije` kartici Sparrow wallet.



![Image](assets/fr/073.webp)



Sada ste savladali osnove korišćenja SeedSigner-a. Da biste produbili svoje znanje i istražili naprednije upotrebe, pozivam vas da pogledate sledeći vodič:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Takođe možete podržati razvoj SeedSigner open-source projekta donacijom u bitkoinima!](https://seedsigner.com/donate/)**



*Kredit: neke od slika u ovom vodiču dolaze sa [zvanične SeedSigner projektne veb stranice](https://seedsigner.com/) i [GitHub repozitorijuma](https://github.com/SeedSigner/seedsigner).*