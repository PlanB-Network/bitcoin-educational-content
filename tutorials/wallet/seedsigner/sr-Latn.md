---
name: SeedSigner
description: DIY, bezdržavni, pristupačni i potpuno izolovani wallet hardver
---

![cover](assets/cover.webp)



SeedSigner je open-source wallet Bitcoin hardver koji svako može sam izraditi koristeći jeftine elektronske komponente opšte namene. Za razliku od komercijalnih proizvoda kao što su Ledger, Coldcard ili Trezor, ovo nije gotov uređaj proizveden od strane kompanije: to je projekat zajednice koji omogućava svakome da kreira svoj uređaj, kontrolišući svaki korak.



SeedSigner je dizajniran da bude 100% ***air-gapped***: nikada se ne povezuje na Internet, nema Wi-Fi ili Bluetooth (u slučaju Raspberry Pi Zero v1.3) i nikada nije povezan na računar radi razmene podataka. Komunikacija se odvija isključivo putem sistema za razmenu QR kodova. Konkretno, vaš softver za upravljanje portfoliom (kao što su Sparrow Wallet) prikazuje transakciju koja treba da se potpiše u obliku QR kodova; skenirate ih kamerom SeedSignera, zatim uređaj potpisuje transakciju koristeći vaše privatne ključeve privremeno smeštene u njegovoj RAM memoriji. Na kraju, generiše QR kodove koji sadrže potpisanu transakciju, koje skenirate svojim softverom da biste je poslali na Bitcoin mrežu.



![Image](assets/fr/001.webp)



SeedSigner je takođe ***stateless***. Drugim rečima, ne čuva trajno vaš seed ili vaše privatne ključeve, za razliku od drugih hardverskih novčanika. Svaki put kada ponovo pokrenete uređaj, njegova memorija je potpuno prazna, osim ako ne konfigurišete uređaj da sačuva vaša podešavanja na microSD kartici. Stoga morate ponovo uneti vaš seed svaki put kada ga koristite, a najpraktičniji metod je da ga sačuvate u obliku QR koda, koji se skenira pri pokretanju pomoću kamere SeedSignera. Ovaj način rada značajno smanjuje površinu napada: čak i ako lopov ukrade vaš uređaj, neće pronaći nikakve informacije na njemu, jer je uvek prazan po defaultu.



Još jedna opcija za čuvanje vašeg seed i korišćenje sa SeedSigner-om je korišćenje *SeedKeeper* pametne kartice u kombinaciji sa kompatibilnim čitačem. Ovo vam pruža veoma robustan *Secure Element* za čuvanje vašeg seed, dok koristite ekran SeedSigner-a za potpisivanje transakcija. Ali ova posebna konfiguracija je tema drugog posvećenog vodiča. Ovde ćemo se koncentrisati na osnovnu upotrebu SeedSigner-a:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Projekat SeedSigner zauzima važno mesto u ekosistemu Bitcoin, jer svima, svuda u svetu, nudi mogućnost da iskoriste naprednu sigurnost za zaštitu svojih bitkoina. Njegova glavna prednost leži u pristupačnosti: potrebni hardver može se kupiti za manje od $50. Štaviše, omogućava ljudima koji žive u ograničenim zemljama da izgrade svoj sopstveni wallet hardver od standardnih računarskih komponenti, koje je lako pronaći i koje su manje podložne regulatornim ograničenjima.



Ali čak i izvan ovih posebnih konteksta, SeedSigner može biti zanimljiva opcija za vas: otvorenog je koda, radi bez stanja i bez povezivanja na mrežu, i smanjuje vektore napada povezane sa lancem snabdevanja vašeg wallet hardvera.



## 1. Potrebna oprema



Da biste napravili svoj SeedSigner, biće vam potrebne sledeće komponente:





- Raspberry Pi Zero
    - Preporučuje se verzija 1.3, jer nema ni Wi-Fi ni Bluetooth, što osigurava potpunu izolaciju.
 - W i v2 verzije su takođe kompatibilne, ali uključuju Wi-Fi/Bluetooth čip. Stoga je preporučljivo fizički ga deaktivirati uklanjanjem radio modula sa kartice. Operacija je relativno jednostavna, ali zahteva preciznost (fina klješta su dovoljna za Zero W, dok je za v2 potrebna vruća olovka da se ukloni metalna ploča koja skriva modul). Neću ulaziti u detalje u ovom vodiču, ali sve instrukcije ćete pronaći u ovom dokumentu: *[Disabling WiFi/Bluetooth by hardware](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Imajte na umu: neki modeli Raspberry Pi Zero se prodaju bez unapred zalemljenih GPIO pinova. Možete ili kupiti verziju sa integrisanim pinovima direktno (najjednostavnije rešenje), ili kupiti pinove zasebno i zalemiti ih sami (složenije rešenje).
 - Ne zaboravite uključiti micro-USB napajanje.



![Image](assets/fr/002.webp)





- Waveshare 1.3" ekran (240×240 px)** (na francuskom)
    - Važno je odabrati upravo ovaj model: postoje drugi slični ekrani, ali sa drugačijom rezolucijom. Bez definicije od 240×240 px, ekran će biti neupotrebljiv.
    - Ekran ima tri dugmeta i mini-džojstik za korisnički interfejs.



![Image](assets/fr/003.webp)





- Kamera kompatibilna sa Raspberry Pi Zero**
    - Opcija 1: standardna kamera sa širokim zlatnim okvirom (proverite kompatibilnost sa vašim kućištem).
    - Opcija 2: kompaktnija kamera "*Zero*", dizajnirana posebno za Pi Zero.



![Image](assets/fr/004.webp)





- MicroSD** kartica
    - Preporučeni kapacitet: između 4 i 32 GB.





- Stanovanje (opciono, ali preporučeno)** (opciono, ali preporučeno)** (opciono, ali preporučeno)** (opciono, ali preporučeno)**)
    - Štiti uređaj i olakšava korišćenje.
    - Najpopularniji model je "*Orange Pill Case*", za koji su [open-source STL fajlovi dostupni za 3D štampu](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Kutije su takođe dostupne od [nezavisnih prodavaca povezanih sa projektom](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Možete kupiti ove komponente zasebno ili, radi veće jednostavnosti, odlučiti se za gotove pakete koji uključuju sav potreban hardver. Lično, naručio sam svoj paket [na ovom francuskom sajtu](https://bitcoinbazar.fr/), ali ćete takođe pronaći listu prodavaca za svaki region sveta na [stranici hardvera projekta SeedSigner](https://seedsigner.com/hardware/). Ako više volite da kupujete komponente pojedinačno, dostupne su na glavnim platformama za e-trgovinu ili u specijalizovanim prodavnicama.



## 2. Priprema softvera



Kada sakupite svoj hardver, potrebno je da pripremite microSD karticu instaliranjem SeedSigner sistema na nju. Da biste to uradili, idite na svoj svakodnevni lični računar i priključite microSD karticu namenjenu za SeedSigner.



### 2.1. Preuzimanje



Idite na [zvanično GitHub spremište projekta](https://github.com/SeedSigner/seedsigner/releases). Na najnovijoj verziji softvera, preuzmite :




- `.img` slika koja odgovara vašem Pi modelu.
- Datoteka `.sha256.txt`.
- Datoteka `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Pre nego što započnemo instalaciju, hajde da proverimo softver.



### 2.2 Verifikacija pod Linux i macOS



Počnite uvozom zvaničnog javnog ključa projekta SeedSigner direktno sa Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminal bi trebalo da vam kaže da je ključ uvezen ili ažuriran. Zatim, pokrenite komandu za verifikaciju na datoteci sa potpisom (zapamtite da modifikujete komandu prema vašoj verziji, ovde `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Ako je sve ispravno, izlaz bi trebalo da glasi `Good signature`. To znači da je datoteka `.sha256.txt` potpisana ključem koji ste upravo uvezli i da je potpis važeći. Ignorišite poruku upozorenja `WARNING: This key is not certified with a trusted signature`: ovo je normalno, jer je sada na vama da proverite da li ključ koji je korišćen pripada projektu SeedSigner.



Da biste to uradili, uporedite poslednjih 16 karaktera otiska prsta prikazanog sa onima dostupnim na [Keybase.io/SeedSigner](https://keybase.io/seedsigner), na njihovom [zvaničnom Twitteru](https://twitter.com/SeedSigner/status/1530555252373704707), ili u fajlu objavljenom na [SeedSigner.com](https://seedsigner.com/keybase.txt). Ako se ovi identifikatori tačno poklapaju, možete biti sigurni da je ključ zaista od projekta. Ako ste u nedoumici, odmah stanite i zatražite pomoć od SeedSigner zajednice (Telegram, X, GitHub...).



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



Ako je sve ispravno, izlaz bi trebao glasiti `Good signature`. To znači da je datoteka `.sha256.txt` potpisana ključem koji ste upravo uvezli i da je potpis važeći. Ignorišite poruku upozorenja `WARNING: This key is not certified with a trusted signature`: ovo je normalno, jer je sada na vama da proverite da li ključ pripada projektu SeedSigner.



Da biste to uradili, uporedite poslednjih 16 karaktera otiska prsta prikazanog sa onima dostupnim na [Keybase.io/SeedSigner](https://keybase.io/seedsigner), na njihovom [zvaničnom Twitteru](https://twitter.com/SeedSigner/status/1530555252373704707), ili u fajlu objavljenom na [SeedSigner.com](https://seedsigner.com/keybase.txt). Ako se ovi identifikatori tačno poklapaju, možete biti sigurni da je ključ zaista od projekta. Ako ste u nedoumici, odmah prestanite i zatražite pomoć od SeedSigner zajednice (Telegram, X, GitHub...).



Kada je ključ validiran, potrebno je proveriti da li slika fajl nije oštećen. Da biste to uradili, koristite sledeću komandu u PowerShell-u:



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Primer za Raspberry Pi Zero 2 (zapamtite da izmenite komandu u skladu sa vašom verzijom, ovde `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell zatim izračunava SHA256 hash vaše slikovne datoteke. Uporedite ovaj hash sa odgovarajućom vrednošću u `seedsigner.0.8.6.sha256.txt`.




- Ako su dve vrednosti strogo identične, provera je uspešna i možete nastaviti.
- Ako se razlikuju, datoteka je oštećena ili korumpirana. Nemojte je koristiti i ponovo pokrenite preuzimanje.



![Image](assets/fr/013.webp)



Uspešna verifikacija garantuje da je vaš `.img` fajl i autentičan (potpisan od strane SeedSigner) i neizmenjen (nemodifikovan). Zatim možete bezbedno preći na sledeći korak.



### 2.4. Flešuj sliku



Ako ga već nemate, preuzmite softver [Balena Etcher] (https://etcher.balena.io/), zatim :




- Umetnite microSD karticu u vaš računar.
- Pokreni Etcher.
- Odaberite preuzetu i verifikovanu `.img` datoteku.
- Izaberite microSD karticu kao cilj.
- Kliknite na `Flash!`.



![Image](assets/fr/014.webp)



Sačekajte da se proces završi: vaša microSD kartica je spremna za upotrebu. Sada je vreme za sklapanje!



## 3. Sklapanje SeedSigner-a



Kada je vaša microSD kartica pripremljena i na nju je instaliran SeedSigner softver, možete nastaviti sa finalnom montažom. Odvojite vreme, jer su neki delovi krhki (posebno stolnjak, kamera i GPIO pinovi).



### 3.1 Priprema kućišta



Prvo, otvorite kućište. Proverite da je čisto i da nema zaostalih plastičnih delova od 3D štampe koji ometaju unutrašnje pričvršćivače. Obratite pažnju na:




- Lokacija kamere (mala kružna rupa napred).
- Otvaranje za ekran.
- Izrezi za micro-USB portove i microSD slot na Raspberry Pi Zero.



### 3.2 Instalacija kamere



Pronađite konektor za traku kamere na Raspberry Pi Zero: to je tanak crni trak na strani ploče, koji se može malo podići da se otvori. Pažljivo ga podignite, bez forsiranja: trebalo bi da se jednostavno nagne nekoliko milimetara.



![Image](assets/fr/015.webp)



Umetnite poklopac kamere. Braon/bakreni deo treba da bude okrenut nadole. Uverite se da je čvrsto postavljen u konektor, bez uvrtanja.



![Image](assets/fr/016.webp)



Zatvorite crnu traku da zaključate stolnjak (osetićete blagi klik). Pažljivo proverite da li ostaje na mestu i da se ne pomera.



![Image](assets/fr/017.webp)



Zatim postavite modul kamere u odgovarajuću rupu u kućištu. U zavisnosti od modela, može se direktno pričvrstiti ili zahtevati malu lepljivu traku da ga drži na mestu. Sočivo mora biti savršeno poravnato, okrenuto ka spolja.



### 3.3 Instaliranje Raspberry Pi Zero



Ako koristite kućište, umetnite Raspberry Pi Zero ploču unutra. Pažljivo poravnajte portove sa predviđenim otvorima.



Zatim postavite Waveshare displej na Raspberry Pi Zero. GPIO pinovi na Pi-ju treba da se savršeno poravnaju sa ženskim konektorom displeja. Polako pritisnite displej na pinove, primenjujući ravnomeran pritisak sa svake strane kako biste izbegli njihovo savijanje.



![Image](assets/fr/018.webp)



Ako imate kućište, dovršite sklapanje dodavanjem prednje ploče i džojstika.



Na kraju, ubacite microSD karticu koja sadrži flešovani softver u bočni slot Raspberry Pi Zero uređaja. Uverite se da je kartica pravilno umetnuta i da klikne na mesto.



### 3.4 Prvo pokretanje



Povežite micro-USB kabl za napajanje na namenski port. Sačekajte oko jedan minut. Trebalo bi da se pojavi SeedSigner logo, a zatim početni ekran.



![Image](assets/fr/019.webp)



Za početak, proverite da li različite komponente rade ispravno odlaskom na meni `Settings > I/O test`.



![Image](assets/fr/020.webp)



Testirajte sve dugmiće i uverite se da pravilno reaguju. Zatim kliknite na dugme `KEY1` da proverite da li kamera radi kako se očekuje. Ovo će napraviti fotografiju.



![Image](assets/fr/021.webp)



### 3.5 Podešavanje kamere



U zavisnosti od toga kako ste montirali vaš SeedSigner, kamera može prikazivati obrnuti prikaz. Da biste to ispravili, idite na `Settings > Advanced > Camera rotation` i izaberite rotaciju od 180° ako je potrebno.



![Image](assets/fr/022.webp)



Ako ste promenili orijentaciju kamere ili želite da promenite druga podešavanja (kao što je jezik interfejsa) kasnije, moraćete da omogućite čuvanje podešavanja na microSD kartici. U suprotnom, vaša podešavanja će se vratiti na podrazumevana svaki put kada ponovo pokrenete uređaj, jer Raspberry Pi Zero nema trajnu memoriju.



Da biste to uradili, otvorite meni `Settings > Persistent settings`, zatim izaberite `Enabled`.



![Image](assets/fr/023.webp)



Ako je sve funkcionalno, vaš SeedSigner je sada spreman za upotrebu!



## 4. SeedSigner postavke



Pre nego što kreirate svoj Bitcoin wallet, hajde da konfigurišemo SeedSigner. Kako radi na Raspberry Pi Zero bez trajne memorije, njegova podešavanja se ne čuvaju automatski osim ako ih ne sačuvate na microSD kartici. Zato se uverite da ste omogućili ovu opciju, inače će ova podešavanja biti izgubljena pri ponovnom pokretanju (pogledajte korak 3.5).



### 4.1 Pristup meniju parametara



Pokrenite svoj SeedSigner i sačekajte da se pojavi početni ekran. Koristeći džojstik, navigirajte do opcije `Settings`, zatim potvrdite pritiskom na centralno dugme. Sada ulazite u glavni meni podešavanja.



![Image](assets/fr/024.webp)



### 4.2 Biranje softvera za upravljanje portfoliom



Zatim pristupite meniju `Coordinator software`.



![Image](assets/fr/025.webp)



`Coordinator` se odnosi na softver za upravljanje portfoliom sa kojim će vaš SeedSigner komunicirati putem QR kodova. Ovaj softver je instaliran ili na vašem računaru ili na vašem pametnom telefonu. Omogućiće vam da upravljate vašim bitcoinima, ali bez ikakvog pristupa vašim privatnim ključevima. SeedSigner ostaje jedini uređaj sposoban da potpisuje vaše transakcije.



Trenutna verzija firmvera podržava nekoliko programa: Sparrow, Specter, BlueWallet, Nunchuk i Keeper. U mom slučaju, koristim **Sparrow Wallet**, koji posebno preporučujem zbog njegove jednostavnosti i bogate funkcionalnosti.



Ako ne znaš kako da ga instaliraš, možeš pratiti ovaj vodič:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Jednostavno izaberite softver po vašem izboru iz menija.



![Image](assets/fr/026.webp)



### 4.3 Prikaz jedinica i količine



U meniju `Denomination Display` možete izabrati jedinicu u kojoj će iznosi biti prikazani:




- `BTC`
- mBTC` (mili-bitkoin, ili 0,001 BTC)
- gW-15 (satoši, ili 1/100,000,000 BTC)



Jedinica **sats** je generalno najpraktičnija za male količine.



![Image](assets/fr/027.webp)



### 4.4 Napredna podešavanja



Sada idite na meni `Advanced`. Ovde ćete pronaći nekoliko korisnih opcija:




- gW-17 mreža`: izmeniti samo ako želite da koristite SeedSigner na Testnet.
- gustina qR koda`: podešava količinu informacija sadržanih u svakom QR kodu. Možete ostaviti podrazumevanu vrednost, osim ako smatrate da je teško čitati prilikom skeniranja.
- `Xpub export`: omogućava ili onemogućava izvoz vašeg proširenog javnog ključa (`xpub`, `ypub`, `zpub`) u softver za upravljanje portfoliom putem QR koda (funkcija koju ćemo koristiti kasnije, pa je za sada ostavite omogućenu).
- `Script types`: definiše tipove skripti dozvoljene za zaključavanje vaših bitkoina. Ne morate menjati ovaj parametar, jer će tip skripte biti direktno postavljen na Sparrow. Ovde su u pitanju samo skripte koje SeedSigner ima ovlašćenje da manipuliše.



### 4.5 Izbor jezika



Konačno, u meniju `Language` možete promeniti jezik interfejsa prema vašim preferencijama.



![Image](assets/fr/028.webp)



## 5. Kreiranje i čuvanje seed



seed (ili mnemonička fraza) čini osnovu vašeg Bitcoin portfolija. Koristi se za izvođenje vaših privatnih ključeva i adresa, i omogućava pristup vašim sredstvima. SeedSigner nudi nekoliko metoda za njegovo generisanje, koje ćemo razmotriti u ovom odeljku.



Pre nego što počnemo, nekoliko osnovnih podsetnika:




- Ova fraza daje pun, neograničen pristup svim vašim bitcoinima.** Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem SeedSigner-u ;
- Obično se koristi fraza od 12 reči za vraćanje wallet u slučaju gubitka ili krađe wallet hardvera. Ali pošto je SeedSigner *bez stanja* uređaj, on nikada ne registruje vaš seed. Dakle, vaši fizički bekapi nisu samo rezervne kopije, već **jedini način da koristite vaš wallet**. Ako izgubite ove bekape, vaši bitkoini će biti trajno izgubljeni. Zato ih pažljivo bekapujte, na nekoliko medija i na sigurnim mestima;
- Ako tek počinjete, toplo vam savetujem da pročitate ovaj vodič za detaljno razumevanje rizika povezanih sa upravljanjem mnemonikom:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Pristup alatu za kreiranje seed



Sa početnog ekrana SeedSigner-a, idite na meni `Tools`.



![Image](assets/fr/029.webp)



Sada ćete generate vaš seed. seed je jednostavno veliki nasumični broj. Što je nasumičnije generisan, to je sigurniji. SeedSigner nudi dva načina za to:




- kamera": seed se generiše iz vizuelnog šuma fotografije. Uzimate sliku nasumičnog okruženja (objekat, pejzaž, lice, itd.) čije varijacije piksela se koriste za generate entropiju. To je brza metoda, ali nije reproduktivna.
- bacanje kockica": bacate kockice kako biste stvorili potrebnu entropiju. To je vremenski zahtevnije, ali ponovljivo i stoga proverljivo. Ako se odlučite za ovu metodu, pratite savete u ovom vodiču (nema potrebe da ovde izračunavate kontrolni zbir, SeedSigner se time bavi):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Kreiranje seed sa fotografijom



Ako izaberete metodu fotografije, kliknite na `New seed` (sa ikonom kamere), uslikajte i potvrdite. Zatim izaberite dužinu vaše rečenice (12 ili 24 reči), koja će se pojaviti na ekranu za čuvanje. Sledeći koraci su identični delu 5.3.



### 5.3 Kreiranje seed sa kockicama



U ovom vodiču koristimo metodu **Bacanja kockica**. Kliknite na `New seed` (sa ikonom kockice).



![Image](assets/fr/030.webp)



Zatim izaberite dužinu vaše mnemoničke fraze. 12 reči već nudi dovoljan nivo sigurnosti, tako da je ovo izbor koji preporučujem.



![Image](assets/fr/031.webp)



Bacite kockice i unesite dobijene brojeve koristeći kursor. Pritisnite centralno dugme da potvrdite svaki unos. Ako napravite grešku, možete se vratiti nazad. Koristite nekoliko različitih kockica da smanjite uticaj bilo koje neuravnotežene kockice. Uverite se da vas niko ne posmatra tokom ove operacije.



![Image](assets/fr/032.webp)



Kada unesete svojih 50 bacanja, SeedSigner generiše vašu rečenicu. **Pažljivo pratite uputstva u ovom vodiču ako tek počinjete:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Prikaz i čuvanje seed



Pažljivo zapišite reči svoje mnemoničke fraze na odgovarajući fizički nosač (papir ili metal).



![Image](assets/fr/033.webp)



### 5.5 Provera rezervne kopije



Da biste izbegli greške u bekapu, SeedSigner vas pita da verifikujete svoj bekap. Kliknite na `Verify`.



![Image](assets/fr/034.webp)



Zatim unesite traženu reč prema njenom redosledu u rečenici. Na primer, ovde moram da izaberem treću reč u svojoj rečenici.



![Image](assets/fr/035.webp)



Ako napravite grešku, SeedSigner će vas obavestiti, i moraćete da počnete ispočetka, pazeći da zabeležite svoju mnemoničku frazu kada vam bude data. Ovaj korak verifikacije osigurava da je vaša rezervna kopija tačna i kompletna. Kada bude potvrđena, ekran će prikazati `Backup Verified`.



![Image](assets/fr/036.webp)



Za potpuniji test restauracije, pratite ovaj vodič :



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Razumevanje koncepta "uređaja bez stanja"



SeedSigner je uređaj bez trajne memorije. To znači da vaš seed nikada nije sačuvan unutar uređaja (za razliku od Ledger, Trezor ili Coldcard, na primer). Čim isključite napajanje, seed potpuno nestaje iz njegove RAM memorije. Kada ponovo pokrenete uređaj, SeedSigner se vraća u prazno stanje: tada ćete morati ponovo uneti vaš seed, kako bi mogao potpisati vaše transakcije.



Ovo pruža suštinsku zaštitu. Za razliku od drugih hardverskih novčanika, SeedSigner je zasnovan na Raspberry Pi Zero, koji nema fizičku zaštitu, uključujući *Secure Element*. Ali pošto se ne čuvaju osetljivi podaci, čak i fizički kompromitovan uređaj ne bi omogućio napadaču da izvuče vaše privatne ključeve ili potroši vaše bitkoine.



S druge strane, ova arhitektura podrazumeva dodatnu odgovornost: bez rezervne kopije, vaša sredstva su definitivno izgubljena. Zato preporučujem **dvostruku rezervnu kopiju**. Već imate svoju frazu za oporavak: ovo je vaša glavna dugoročna rezervna kopija, koju treba čuvati na sigurnom mestu. Sada ćemo kreirati kopiju ove fraze u obliku **QR koda**.



Svaki put kada koristite SeedSigner, skenirate ovaj QR kod kamerom uređaja kako bi privremeno učitao vaš seed u svoju memoriju dok potpisujete svoje transakcije. Ova druga rezervna kopija, namenjena za svakodnevnu upotrebu, takođe mora biti čuvana s najvećom pažnjom: svako ko poseduje ovaj QR kod ima potpuni pristup vašim bitcoinima.


Takođe vam savetujem da čuvate vaš QR kod i vašu mnemonicku frazu na dve odvojene lokacije, kako biste izbegli gubitak svega u slučaju zahteva.



Konačno, naprednija i sigurnija alternativa je korišćenje SeedSigner-a sa **SeedKeeper**-om, koji čuva seed u secure element. Da biste saznali više, pogledajte ovaj tutorijal:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Napišite otisak prsta glavnog ključa



Kada je verifikacija završena, SeedSigner prikazuje otisak prsta glavnog ključa vašeg wallet. Ovaj otisak prsta identifikuje vaš wallet i osigurava da u budućnosti koristite ispravnu frazu za oporavak. Ne otkriva nikakve informacije o vašim privatnim ključevima, tako da ga možete bezbedno čuvati na digitalnom mediju. Samo se pobrinite da imate dostupnu kopiju i nikada je ne izgubite.



![Image](assets/fr/037.webp)



Takođe je u ovoj fazi moguće dodati **passphrase BIP39** kako biste pojačali sigurnost vašeg wallet. U zavisnosti od vaše strategije bekapa, ova opcija može biti vredna, ali takođe nosi rizike: ako izgubite passphrase, pristup vašim bitkoinima će biti trajno izgubljen.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Ako još niste upoznati sa konceptom passphrase, pozivam vas da pročitate ovaj sveobuhvatan vodič na tu temu:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Čuvanje seed u QR formatu (*SeedQR*)



SeedSigner vam omogućava da konvertujete vaš seed u papirni QR kod, nazvan *SeedQR*. Ova metoda pojednostavljuje ponovno učitavanje vašeg wallet, jer izbegava ručno prepisivanje svake reči.



Da biste to uradili, biće vam potreban prazan papirni ili metalni QR kod koji odgovara dužini vaše mnemoničke fraze. Ako ste kupili kompletan paket za vaš SeedSigner, šabloni su obično uključeni. Ako nisu, možete ih preuzeti i odštampati (ili ih ručno reprodukovati) ovde:




- [12-word format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24-word format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Compact format 12 words](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Sažeti format 24 reči](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Sa vašeg seed ekrana, izaberite `Backup Seed`.



![Image](assets/fr/039.webp)



Zatim izaberite `Export as SeedQR`.



![Image](assets/fr/040.webp)



Zatim odaberite željeni format (normalan ili kompaktan) prema dostupnom predlošku za papir.



![Image](assets/fr/041.webp)



Kliknite `Begin` da biste započeli kreiranje *SeedQR*-a. SeedSigner će zatim prikazati niz mreža (A1, A2, B1, itd.), od kojih svaka odgovara delu koda.



![Image](assets/fr/042.webp)



Pažljivo reprodukujte svaku crnu tačku na vašem listu za čuvanje, zatim koristite džojstik da pređete na sledeći blok. Uzmite svoje vreme: jednostavno neusklađivanje može učiniti QR kod neupotrebljivim.



Nekoliko saveta:




- Počnite sa olovkom kako biste mogli ispraviti sve greške, a zatim se vratite korišćenju fine crne olovke kada završite;
- Dobro centrirana tačka u sredini kvadrata je sve što vam treba, nema potrebe da ga potpuno popunite.



![Image](assets/fr/043.webp)



Zatim kliknite na `Confirm SeedQR` i skenirajte svoj QR kod da proverite da li ispravno radi.



![Image](assets/fr/044.webp)



Ako se prikaže poruka `Success`, vaš *SeedQR* je važeći: možete preći na sledeći korak.



![Image](assets/fr/045.webp)



**Čuvajte ovaj list jednako strogo kao vašu frazu za oporavak. Svako ko poseduje ovaj QR kod može rekonstruisati vaše privatne ključeve i ukrasti vaše bitkoine.**



Čestitamo, vaš Bitcoin portfolio je sada pokrenut! Sada ćemo uvesti njegove javne komponente u **Sparrow Wallet** kako bismo ga lako upravljali.



## 6. Uvezi wallet u Sparrow



Kada je vaš SeedSigner postavljen i vaš seed pravilno generisan i sačuvan, sledeći korak je povezivanje ovog portfolija sa softverom za upravljanje kao što su Sparrow Wallet. Vaš seed će uvek ostati van mreže, jer će samo javni deo vašeg portfolija biti prenet na Sparrow. Ovo će omogućiti softveru da prikaže vaše adrese, transakcije i kreira nove transakcije, bez mogućnosti trošenja vaših bitkoina. Da biste potrošili svoje bitkoine, vaš SeedSigner će uvek morati da potpiše transakciju pripremljenu od strane Sparrow.



### 6.1 Priprema SeedSigner-a



Umetnite microSD koja sadrži operativni sistem, uključite vaš SeedSigner, zatim učitajte seed koji ste upravo kreirali iz vašeg rezervnog QR koda. Na početnom ekranu, izaberite `Scan`, zatim skenirajte vaš SeedQR sa SeedSigner-om.



![Image](assets/fr/046.webp)



Proverite da otisak prsta na vašem glavnom ključu odgovara otisku prsta na vašem wallet. Ako koristite passphrase, unesite ga u ovoj fazi.



![Image](assets/fr/047.webp)



Ovo vas vodi do menija za vaš portfolio, u mom slučaju nazvanog `d4149b27`. Ako ste ponovo na početnom ekranu, izaberite `Seeds`, zatim odaberite štampu koja odgovara vašem portfoliju. Zatim kliknite na `Export Xpub`.



![Image](assets/fr/048.webp)



Odaberite tip portfolija. U našem slučaju, to je jedan portfolio: odaberite `Single Sig`.



![Image](assets/fr/049.webp)



Sledeći dolazi izbor standarda skriptovanja. Najnoviji i najekonomičniji u smislu troškova transakcije je `Taproot`. Stoga vam savetujem da odaberete ovaj standard.



![Image](assets/fr/050.webp)



Pojaviće se poruka upozorenja. Ovo je normalno: ovaj prošireni javni ključ (`xpub`) omogućava vam da vidite sve adrese izvedene iz vašeg seed (na prvom nalogu). Ne omogućava vam da trošite svoja sredstva, ali otkriva strukturu vašeg portfolija. Ako ikada procuri, to je problem za vašu privatnost, ali ne i za sigurnost vaših bitkoina: omogućava vam da ih vidite, ali ne i da ih trošite.



Kliknite `Razumem`, zatim `Izvezi Xpub` ako ste zadovoljni prikazanim informacijama.



SeedSigner zatim generiše vaš xpub u obliku dinamičkog QR koda koji sadrži sve podatke potrebne za upravljanje vašim portfoliom u Sparrow Wallet.



![Image](assets/fr/051.webp)



Džojstikom možete podesiti osvetljenost ekrana za lakše skeniranje QR koda.



### 6.2 Uvoz novog portfolija u Sparrow Wallet



Uverite se da imate instaliran Sparrow Wallet softver na vašem računaru. Ako ne znate kako da preuzmete, proverite i pravilno instalirate, pogledajte naš kompletan vodič na tu temu:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Na vašem računaru, otvorite Sparrow Wallet, zatim u meniju kliknite `File → Import Wallet`.



![Image](assets/fr/052.webp)



Pomeri dole do `SeedSigner`, zatim izaberi `Skeniraj...`. Tvoja veb kamera će se otvoriti: skeniraj dinamički QR kod prikazan na ekranu tvog SeedSigner-a.



![Image](assets/fr/053.webp)



Dodelite ime svom portfoliju, zatim kliknite na `Create Wallet`. Sparrow će vas zatim zamoliti da postavite lozinku za zaključavanje lokalnog pristupa ovom wallet. Izaberite jaku lozinku: ona štiti pristup podacima vašeg portfolija u Sparrow (javne ključeve, adrese, oznake i istoriju transakcija). Ova lozinka nije potrebna za obnavljanje portfolija u kasnijem periodu: samo vaša mnemonička fraza (i moguće vaš passphrase) je potrebna u tu svrhu.



Preporučujem da sačuvaš ovu lozinku u menadžeru lozinki kako bi izbegao/la njen gubitak.



![Image](assets/fr/054.webp)



Vaš keystore je sada uspešno uvezen.



![Image](assets/fr/055.webp)



Zatim proverite da li se `Master fingerprint` prikazan u Sparrow podudara sa onim ranije zabeleženim u vašem SeedSigner-u.



Vaš SeedSigner i Sparrow Wallet su sada sigurno povezani. Sparrow deluje kao kompletan interfejs za upravljanje, dok SeedSigner ostaje jedini uređaj sposoban za potpisivanje vaših transakcija. Sada ste spremni da primate i šaljete bitkoine u potpuno vazdušno izolovanoj konfiguraciji.



## 7. Primanje i slanje bitkoina



Vaš SeedSigner i Sparrow Wallet su sada konfigurisani da rade zajedno. U ovom poslednjem delu, pogledaćemo kako primati i slati bitkoine koristeći ovu konfiguraciju.



### 7.1 Primanje bitkoina



#### 7.1.1 Generisanje adrese za prijem



Na vašem računaru, otvorite Sparrow Wallet i otključajte vaš SeedSigner wallet koristeći vašu lozinku. Uverite se da je softver povezan sa serverom (zarez na donjem desnom uglu). U bočnoj traci, kliknite na `Receive`.



![Image](assets/fr/056.webp)



Prikazana je nova Bitcoin adresa. Videćete :




- Tekst adresa (počinje sa `bc1p...` ako koristiš P2TR kao ja),
- Odgovarajući QR kod,
- Polje `Label` za praćenje vaših transakcija.



Preporučujem da dodate oznaku svakom bitcoin računu na vašem wallet. Ovo će vam omogućiti da lako identifikujete poreklo svakog UTXO i poboljšate upravljanje privatnošću. Da biste dublje istražili ovu važnu temu, možete pogledati posvećenu obuku na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Da biste dodali oznaku, jednostavno unesite ime u polje `Label`, a zatim potvrdite.



Na primer:



```txt
Label : Sale of the Raspberry Pi Zero
```



Vaša adresa je sada povezana sa ovom oznakom u svim Sparrow odeljcima.



![Image](assets/fr/057.webp)



#### 7.1.2 Address verifikacija na SeedSigner



Pre nego što podelite svoju adresu za primanje, veoma je važno da proverite da li pripada vašem seed. Ovaj korak osigurava da vaš SeedSigner može potpisati transakcije povezane sa ovom adresom. Takođe štiti od mogućih napada u kojima Sparrow prikazuje lažnu adresu. Zapamtite da Sparrow radi u nesigurnom okruženju (vašem računaru), koje ima mnogo veću površinu za napad nego vaš SeedSigner, koji je potpuno izolovan. Zato nikada ne treba slepo verovati adresama za primanje prikazanim na Sparrow dok ih ne verifikujete sa vašim wallet hardverom.



Na Sparrow, kliknite na QR kod adrese da ga uvećate: zatim će biti prikazan preko celog ekrana.



![Image](assets/fr/058.webp)



Na vašem SeedSigner-u, iz glavnog menija, izaberite `Scan`. Skenirajte QR kod prikazan na ekranu vašeg računara, zatim izaberite seed koji odgovara vašem wallet (u mom slučaju, otisak prsta `d4149b27`).



![Image](assets/fr/059.webp)



Ako skenirana adresa odgovara onoj izvedenoj iz vašeg seed, ekran SeedSigner-a će prikazati poruku: `Address Verified`.



![Image](assets/fr/060.webp)



Ovo potvrđuje da adresa pripada vašem wallet i da možete sa sigurnošću primati bitkoine sa nje.



#### 7.1.3 Prijem sredstava



Sada možete komunicirati ovu adresu (u tekstualnom ili QR kod obliku) osobi ili odeljenju koje treba da vam pošalje satss. Kada transakcija bude emitovana na mreži, pojaviće se u kartici `Transactions` Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Pošalji bitkoine



Slanje bitcoina pomoću SeedSigner-a je proces u 3 koraka:




- Kreiranje transakcije u Sparrow ;
- Potpis transakcije na SeedSigner ;
- Konačna distribucija transakcije putem Sparrow.



Sva razmena između dva uređaja vrši se isključivo korišćenjem QR kodova.



#### 7.2.1 Kreiranje transakcije u Sparrow



U Sparrow Wallet, možete kliknuti na karticu `Send` u bočnoj traci s leve strane. Međutim, ja preferiram korišćenje kartice `UTXOs`, koja vam omogućava da vežbate "*Coin Control*". Ova metoda vam daje preciznu kontrolu nad korišćenim UTXO-ima, tako da možete kontrolisati informacije koje otkrivate tokom transakcije.



Na kartici `UTXOs`, izaberite novčiće koje želite da potrošite, zatim kliknite na `Send Selected`.



![Image](assets/fr/062.webp)



Zatim popunite polja za transakciju:




- U `Plati`, nalepite adresu primaoca ili kliknite na ikonu kamere da skenirate QR kod;
- U `Label`, dodajte oznaku za praćenje ovog troška;
- U polje `Amount` unesite iznos koji treba poslati;
- Konačno, odaberite stopu naknade na osnovu trenutnih tržišnih uslova (procene su dostupne na [mempool.space](https://mempool.space/)).



Kada su polja popunjena, pažljivo proverite informacije, a zatim kliknite na `Create Transaction >>`.



![Image](assets/fr/063.webp)



Proverite detalje transakcije kako biste bili sigurni da je sve ispravno, zatim kliknite na `Finalize Transaction for Signing`.



![Image](assets/fr/064.webp)



Transakcija je sada spremna, ali još nije potpisana. Da biste prikazali [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) kao QR kod, kliknite na `Prikaži QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Potpisivanje transakcije sa SeedSigner



Uključite svoj SeedSigner i skenirajte svoj SeedQR da biste pristupili svom portfoliju, kao i obično. Na početnom ekranu izaberite `Scan`, zatim skenirajte QR kod prikazan na Sparrow.



![Image](assets/fr/066.webp)



Zatim izaberite seed da odgovara vašem portfoliju.



![Image](assets/fr/067.webp)



SeedSigner automatski detektuje da je ovo PSBT i prikazuje rezime transakcije:




   - Iznos poslat,
   - Izlazne adrese,
   - Povezani transakcioni troškovi.



Kliknite na `Review Details` i pažljivo proverite sve informacije direktno na SeedSigner ekranu. Najvažnije stavke koje treba proveriti su poslata suma, adresa primaoca i iznos primenjenih naknada.



![Image](assets/fr/068.webp)



Ako je sve ispravno, izaberite `Approve PSBT` da potpišete transakciju koristeći odgovarajući privatni ključ(eve).



![Image](assets/fr/069.webp)



Jednom potpisan, SeedSigner generiše novi QR kod koji sadrži potpisanu transakciju, spreman za skeniranje od strane Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Emitovanje transakcije sa Sparrow



Sada kada je transakcija validna, potrebno je emitovati je na Bitcoin mreži, kako bi stigla do rudara koji će je dodati u blok.



Na Sparrow, kliknite na `QR Scan`.



![Image](assets/fr/071.webp)



Prikažite QR kod koji prikazuje vaš SeedSigner (onaj potpisane transakcije) veb kameri. Sparrow će dekodirati potpis i prikazati sve detalje transakcije. Izvršite konačnu proveru da li su sve informacije tačne, a zatim kliknite na Emituj Transakciju da biste je emitovali na Bitcoin mreži.



![Image](assets/fr/072.webp)



Vaša transakcija je sada poslata na mrežu Bitcoin. Možete pratiti njen napredak u kartici `Transakcije` Sparrow Wallet.



![Image](assets/fr/073.webp)



Sada ste savladali osnove korišćenja SeedSigner-a. Da biste produbili svoje znanje i istražili naprednije upotrebe, pozivam vas da pogledate sledeći vodič:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Takođe možete podržati razvoj SeedSigner open-source projekta donacijom u bitkoinima!](https://seedsigner.com/donate/)**



*Kredit: neke od slika u ovom vodiču dolaze sa [zvanične SeedSigner projektne veb stranice](https://seedsigner.com/) i [GitHub repozitorijuma](https://github.com/SeedSigner/seedsigner).*