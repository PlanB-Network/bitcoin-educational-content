---
name: Mnemonic Fraza - Bacanje Kockica
description: Kako da generate svoj sopstveni recovery phrase pomoću kockica?
---

![cover](assets/cover.webp)


U ovom vodiču ćete naučiti kako ručno konstruisati frazu za oporavak za Bitcoin Wallet koristeći bacanje kockica.


**UPOZORENJE:** Generisanje Mnemonic fraze na siguran način zahteva da se ne ostavi nikakav digitalni trag tokom njenog kreiranja, što je gotovo nemoguće. U suprotnom, Wallet bi predstavljao preveliku površinu za napad, značajno povećavajući rizik od krađe vaših bitkoina. **Stoga se strogo savetuje da ne prebacujete sredstva na Wallet koji zavisi od fraze za oporavak koju ste sami generisali.** Čak i ako pratite ovaj vodič doslovno, postoji rizik da fraza za oporavak može biti kompromitovana. **Zbog toga, ovaj vodič ne bi trebalo primenjivati za kreiranje pravog Wallet.** Korišćenje Hardware Wallet za ovaj zadatak je mnogo manje rizično, jer generiše frazu offline, a pravi kriptografi su razmotrili upotrebu kvalitativnih izvora entropije.


Ovaj vodič se može pratiti isključivo u eksperimentalne svrhe za kreiranje fiktivnog Wallet, bez namere da se koristi sa stvarnim bitkoinima. Međutim, iskustvo nudi dve prednosti:



- Prvo, omogućava vam da bolje razumete mehanizme na bazi vašeg Bitcoin Wallet;
- Drugo, omogućava vam da znate kako to uraditi. Ne kažem da će jednog dana biti korisno, ali možda hoće!


## Šta je Mnemonic fraza?


Fraza za oporavak, koja se ponekad naziva i "Mnemonic," "seed fraza," ili "tajna fraza," je sekvenca koja se obično sastoji od 12 ili 24 reči, a generiše se na pseudo-slučajan način iz izvora entropije. Pseudo-slučajna sekvenca se uvek završava kontrolnim zbirom.


Mnemonic fraza, zajedno sa opcionalnom passphrase, koristi se za determinističko izvođenje svih ključeva povezanih sa HD (Hijerarhijski Deterministički) Wallet. To znači da je iz ove fraze moguće deterministički generate i ponovo kreirati sve privatne i javne ključeve Bitcoin Wallet, i samim tim, pristupiti sredstvima povezanim s njim.

![mnemonic](assets/notext/1.webp)

Svrha ove rečenice je da obezbedi jednostavan način za pravljenje rezervnih kopija i oporavak bitkoina. Neophodno je čuvati Mnemonic frazu na sigurnom i bezbednom mestu, jer bi svako ko poseduje ovu frazu imao pristup sredstvima odgovarajućeg Wallet. Ako se koristi u kontekstu tradicionalnog Wallet, i bez opcionalnog passphrase, često predstavlja SPOF (Single Point Of Failure).

Obično vam se ova fraza daje direktno prilikom kreiranja vašeg Wallet, od strane softvera ili korišćenog Hardware Wallet. Međutim, moguće je i da sami generate ovu frazu, a zatim je unesete na odabranu podršku kako biste dobili Wallet ključeve. Ovo ćemo naučiti da radimo u ovom vodiču.


## Priprema potrebnih materijala


Za kreiranje vaše fraze za oporavak ručno, biće vam potrebno:



- List papira;
- Hemijska olovka ili obična olovka, po mogućstvu različitih boja radi lakše organizacije;
- Nekoliko kockica, kako bi se smanjili rizici od pristrasnosti povezani sa neuravnoteženom kockicom;
- [Lista od 2048 BIP39 reči](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) odštampana.


Nakon toga, upotreba računara sa terminalom postaje neophodna za izračunavanje kontrolne sume. Upravo iz tog razloga savetujem protiv ručnog generisanja Mnemonic fraze. Po mom mišljenju, intervencija računara, čak i uz mere predostrožnosti navedene u ovom vodiču, značajno povećava ranjivost Wallet.


Za eksperimentalni pristup koji se tiče "fiktivnog Wallet", moguće je koristiti vaš uobičajeni računar i njegov terminal. Međutim, za rigorozniji pristup usmeren na ograničavanje rizika kompromitovanja vaše fraze, idealno bi bilo koristiti PC koji nije povezan na internet (po mogućstvu bez wifi komponente ili RJ45 žičane veze), opremljen sa minimalno periferija (sve bi trebalo da budu povezane kablom, kako bi se izbegao Bluetooth), i pre svega, koji radi na amnezičnoj Linux distribuciji kao što je [Tails](https://tails.boum.org/index.fr.html), pokrenutoj sa prenosivog medija.


![mnemonic](assets/notext/2.webp)


U stvarnom kontekstu, bilo bi ključno osigurati poverljivost vašeg radnog prostora odabirom lokacije daleko od znatiželjnih pogleda, bez prolaska ljudi i bez kamera (web kamere, telefoni...).

Preporučuje se korišćenje velikog broja kockica kako bi se smanjio uticaj potencijalno neuravnotežene kockice na entropiju. Pre njihove upotrebe, preporučuje se provera kockica: to se može postići testiranjem u činiji sa vodom zasićenom solju, omogućavajući kockicama da plutaju. Zatim nastavite da bacate svaku kockicu oko dvadeset puta u slanoj vodi, posmatrajući rezultate. Ako se jedna ili dve strane pojavljuju nesrazmerno u poređenju sa ostalima, produžite test sa više bacanja. Ravnomerno raspoređeni rezultati ukazuju na to da je kockica pouzdana. Međutim, ako jedna ili dve strane redovno dominiraju, te kockice treba ostaviti po strani, jer bi mogle ugroziti entropiju vaše Mnemonic fraze i, posledično, sigurnost vaše Wallet.

U stvarnim uslovima, nakon obavljanja ovih provera, bili biste spremni da generate neophodnu entropiju. Za eksperimentalni fiktivni Wallet kreiran kao deo ovog tutorijala, mogli biste prirodno preskočiti ove pripreme.


## Nekoliko podsetnika o frazi za oporavak


Da bismo započeli, pregledaćemo osnove kreiranja Mnemonic fraze prema BIP39. Kao što je ranije objašnjeno, fraza se izvodi iz pseudo-slučajnih informacija određene veličine, kojima se dodaje kontrolni zbir kako bi se osigurala njena celovitost.


Veličina ove početne informacije, često nazvane "entropija," određuje se brojem reči koje želite da dobijete u frazi za oporavak. Najčešći formati su fraze od 12 i 24 reči, koje proizlaze iz entropije od 128 bita i 256 bita. Evo tabele koja prikazuje različite veličine entropije prema BIP39:


| Phrase (words) | Entropy (bits) | Checksum (bits) | Entropy + Checksum (bits) |
| -------------- | -------------- | --------------- | ------------------------- |
| 12             | 128            | 4               | 132                       |
| 15             | 160            | 5               | 165                       |
| 18             | 192            | 6               | 198                       |
| 21             | 224            | 7               | 231                       |
| 24             | 256            | 8               | 264                       |

Entropija je, dakle, nasumičan broj između 128 i 256 bita. U ovom vodiču, uzećemo primer fraze od 12 reči, u kojoj je entropija 128 bita, što znači da ćemo generate nasumičan niz od 128 `0` ili `1`. Ovo predstavlja broj sastavljen od 128 cifara u bazi 2 (binarno).

Na osnovu ove entropije, generisaće se kontrolna suma. Kontrolna suma je vrednost izračunata iz skupa podataka, koja se koristi za proveru integriteta i validnosti tih podataka tokom prenosa ili skladištenja. Algoritmi za kontrolnu sumu su dizajnirani da otkriju slučajne greške ili izmene u podacima.

U slučaju naše Mnemonic fraze, funkcija kontrolnog zbira je da uoči bilo kakve greške pri unosu fraze u Wallet softver. Nevažeći kontrolni zbir signalizira prisustvo greške u frazi. Suprotno tome, važeći kontrolni zbir ukazuje na to da je fraza najverovatnije tačna.


Da bi se dobio ovaj kontrolni zbir, entropija se propušta kroz SHA256 Hash funkciju. Ova operacija proizvodi 256-bitni niz kao izlaz, od kojeg će biti zadržani samo prvi `N` bitovi, pri čemu `N` zavisi od željene dužine fraze za oporavak (pogledajte tabelu iznad). Dakle, za frazu od 12 reči, zadržaće se prva 4 bita Hash.

![mnemonic](assets/en/3.webp)

Ovih prvih 4 bita, koji čine kontrolni zbir, zatim će biti dodati originalnoj entropiji. U ovoj fazi, fraza za oporavak je praktično konstituisana, ali je još uvek u binarnom obliku. Da bismo ovu binarnu sekvencu pretvorili u reči u skladu sa BIP39 standardom, prvo ćemo podeliti sekvencu na segmente od 11 bita.

![mnemonic](assets/notext/4.webp)

Svaki od ovih paketa predstavlja broj u binarnom sistemu koji će zatim biti konvertovan u decimalni broj (baza 10). Dodaćemo `1` svakom broju, jer u računarstvu, brojanje počinje od `0`, ali BIP39 lista je numerisana počevši od `1`.


![mnemonic](assets/notext/5.webp)


Konačno, broj u decimalnom obliku nam govori poziciju odgovarajuće reči u [listi od 2048 BIP39 reči](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf). Sve što preostaje je da izaberemo ove reči kako bismo sastavili frazu za oporavak za naš Wallet.


![mnemonic](assets/notext/6.webp)


Sada, pređimo na vežbu! Izvršićemo generate frazu za oporavak od 12 reči. Međutim, ova operacija ostaje identična u slučaju fraze od 24 reči, osim što bi zahtevala 256 bita entropije i kontrolni zbir od 8 bita, kao što je navedeno u tabeli ekvivalencije na početku ovog odeljka.


## Korak 1: Generisanje Entropije


Pripremite svoj list papira, olovku i kockice. Za početak, potrebno je nasumično generisati generate 128 bita, odnosno niz od 128 `0` i `1` u nizu. Da bismo to uradili, koristićemo kockice.

![mnemonic](assets/notext/7.webp)


Kockice imaju 6 strana, sve sa identičnom verovatnoćom da budu bačene. Međutim, naš cilj je da proizvedemo binarni rezultat, što znači dva moguća ishoda. Stoga ćemo dodeliti vrednost `0` svakom bacanju koje pokaže paran broj, a `1` za svaki neparan broj. Kao rezultat, izvešćemo 128 bacanja kako bismo kreirali naš 128-bitni entropijski niz. Ako kocka pokaže `2`, `4` ili `6`, zabeležićemo `0`; za `1`, `3` ili `5`, to će biti `1`. Svaki rezultat će biti zabeležen sekvencijalno, s leva na desno i odozgo na dole.


Da bismo olakšali sledeće korake, grupisaćemo bitove u pakete od četiri i tri, kao što je prikazano na slici ispod. Svaka linija mora imati 11 bitova: 2 paketa od 4 bita i jedan paket od 3 bita.


![mnemonic](assets/notext/8.webp)


Kao što možete videti u mom primeru, dvanaesta reč se trenutno sastoji od samo 7 bita. Oni će biti dopunjeni sa 4 bita kontrolne sume u sledećem koraku kako bi formirali 11 bita.


![mnemonic](assets/notext/9.webp)


## Korak 2: Izračunavanje kontrolnog zbira


Ovaj korak je najkritičniji u ručnom generisanju Mnemonic fraze, jer zahteva upotrebu računara. Kao što je ranije pomenuto, kontrolni zbir odgovara početku SHA256 Hash generisanog iz entropije. Iako je teoretski moguće izračunati SHA256 ručno za unos od 128 ili 256 bita, ovaj zadatak bi mogao potrajati čitavu nedelju. Štaviše, svaka greška u ručnim proračunima bila bi identifikovana tek na kraju procesa, primoravajući vas da počnete ispočetka. Stoga je nezamislivo obaviti ovaj korak samo sa papirom i olovkom. Računar je gotovo obavezan. Ako i dalje želite da naučite kako da ručno uradite SHA256, objašnjavamo kako to učiniti u [kursu CRYPTO301](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f).


Iz tog razloga, toplo savetujem protiv kreiranja ručne fraze za stvarni Wallet. Po mom mišljenju, korišćenje računara u ovoj fazi, čak i uz sve neophodne mere predostrožnosti, nerazumno povećava površinu napada Wallet.

Da bismo izračunali kontrolni zbir ostavljajući što manje tragova, koristićemo amnezijsku Linux distribuciju sa prenosivog diska pod nazivom **Tails**. Ovaj operativni sistem se pokreće sa USB memorije i radi isključivo na RAM-u računara, bez interakcije sa Hard diskom. Dakle, u teoriji, ne ostavlja tragove na računaru nakon što se isključi. Imajte na umu da je Tails kompatibilan samo sa x86_64 tipom procesora, a ne sa ARM tipom procesora.

Da biste započeli, sa svog uobičajenog računara, [preuzmite Tails sliku sa zvanične veb stranice](https://tails.net/install/index.fr.html). Osigurajte autentičnost preuzimanja koristeći potpis programera ili alat za verifikaciju koji nudi sajt.

![mnemonic](assets/notext/10.webp)

Prvo formatirajte vaš USB stik, zatim instalirajte Tails koristeći alat kao što je [Balena Etcher](https://etcher.balena.io/).

![mnemonic](assets/notext/11.webp)

Nakon što potvrdite da je flešovanje uspešno, isključite računar. Zatim nastavite sa isključivanjem napajanja Supply i uklonite Hard drajv sa matične ploče vašeg računara. U slučaju da je prisutna WiFi kartica, treba je isključiti. Slično tome, uklonite bilo koji RJ45 Ethernet kabl. Da biste smanjili rizik od curenja podataka, preporučuje se da isključite internet kutiju i isključite mobilni telefon. Takođe, obavezno isključite sve suvišne periferne uređaje sa računara, kao što su mikrofon, veb kamera, zvučnici ili slušalice, i proverite da su ostali periferni uređaji povezani samo putem kabla. Svi ovi koraci pripreme računara nisu neophodni, ali jednostavno pomažu da se smanji površina napada koliko god je to moguće u stvarnom kontekstu.


Proverite da li je vaš BIOS podešen da dozvoli pokretanje sa spoljnog uređaja. Ako nije, promenite ovo podešavanje, zatim restartujte vaš računar. Kada obezbedite računarsko okruženje, restartujte računar sa USB stikom sa Tails OS.


Na početnom ekranu Tails-a, izaberite jezik po vašem izboru, zatim pokrenite sistem klikom na `Start Tails`.


![mnemonic](assets/notext/12.webp)


Sa desktopa, kliknite na karticu `Applications`.


![mnemonic](assets/notext/13.webp)


Idite na meni `Utilities`.


![mnemonic](assets/notext/14.webp)


I konačno, kliknite na aplikaciju `Terminal`.


![mnemonic](assets/notext/15.webp)


Stići ćete na novi prazan komandni terminal.


![mnemonic](assets/notext/16.webp)

Ukucajte komandu `echo`, a zatim vaš prethodno generisani entropijski niz, vodeći računa da umetnete razmak između `echo` i vašeg niza binarnih cifara.

![mnemonic](assets/notext/17.webp)


Dodajte dodatni razmak, zatim unesite sledeću komandu, koristeći _pipe_ (`|`):


```plaintext
| shasum -a 256 -0


![mnemonic](assets/notext/18.webp)


U primeru sa mojom entropijom, ukupna komanda je sledeća:


```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```


U ovoj komandi:



- `echo` se koristi za slanje niza bitova;
- `|`, _pipe_, se koristi za usmeravanje izlaza komande `echo` u ulaz sledeće komande;
- `shasum` pokreće heš funkciju koja pripada SHA (_Secure Hash Algorithm_) porodici;
- `-a` specificira izbor određenog algoritma heširanja;
- `256` označava da se koristi algoritam SHA256;
- `-0` omogućava da se unos interpretira kao binarni broj.


Nakon pažljivog proveravanja da vaša binarna sekvenca ne sadrži greške u kucanju, pritisnite taster `Enter` da izvršite komandu. Terminal će zatim prikazati SHA256 Hash vaše entropije.


![mnemonic](assets/notext/19.webp)


Za sada, Hash je izražen u heksadecimalnom formatu (baza 16). Na primer, moj je:


```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```


Da bismo finalizirali našu Mnemonic frazu, potrebna su nam samo prva 4 bita Hash, koja čine kontrolni zbir. U heksadecimalnom formatu, svaki karakter predstavlja 4 bita. Dakle, zadržaćemo samo prvi karakter Hash. Za frazu od 24 reči, bilo bi potrebno uzeti u obzir prva dva karaktera. U mom primeru, to odgovara slovu: `a`. Pažljivo zabeležite ovaj karakter negde na vašem listu, a zatim isključite računar.


Sledeći korak je da ovaj heksadecimalni karakter (baza 16) konvertujete u binarnu vrednost (baza 2), jer je naša fraza konstruisana u ovom formatu. Da biste to uradili, možete koristiti sledeću tabelu konverzije:


| Decimal (base 10) | Hexadecimal (base 16) | Binary (base 2) |
| ----------------- | --------------------- | --------------- |
| 0                 | 0                     | 0000            |
| 1                 | 1                     | 0001            |
| 2                 | 2                     | 0010            |
| 3                 | 3                     | 0011            |
| 4                 | 4                     | 0100            |
| 5                 | 5                     | 0101            |
| 6                 | 6                     | 0110            |
| 7                 | 7                     | 0111            |
| 8                 | 8                     | 1000            |
| 9                 | 9                     | 1001            |
| 10                | a                     | 1010            |
| 11                | b                     | 1011            |
| 12                | c                     | 1100            |
| 13                | d                     | 1101            |
| 14                | e                     | 1110            |
| 15                | f                     | 1111            |

U mom primeru, slovo `a` odgovara binarnom broju `1010`. Ova 4 bita formiraju kontrolni zbir naše fraze za oporavak. Sada ih možete dodati entropiji koja je već zabeležena na vašem listu papira, postavljajući ih na kraj poslednje reči.


![mnemonic](assets/notext/20.webp)


Vaša Mnemonic fraza je sada kompletna, ali je u binarnom formatu. Sledeći korak će biti da je konvertujete u decimalni sistem kako biste zatim mogli da povežete svaki broj sa odgovarajućom rečju na BIP39 listi.


## Korak 3: Pretvaranje reči u decimalne brojeve


Da biste svaku binarnu liniju pretvorili u decimalni broj, koristićemo metodu koja olakšava ručno računanje. Trenutno imate dvanaest linija na papiru, svaka sastavljena od 11 binarnih cifara `0` ili `1`. Da biste nastavili sa konverzijom u decimalni sistem, dodelite svakoj prvoj cifri vrednost `1024` ako je `1`, u suprotnom `0`. Za drugu cifru, vrednost `512` će biti dodeljena ako je `1`, u suprotnom `0`, i tako dalje do jedanaeste cifre. Odgovarajuće vrednosti su sledeće:



- 1st bit: `1024`;
- 2nd bit: `512`;
- 3. bit: `256`;
- 4. bit: `128`;
- 5th bit: `64`;
- 6. bit: `32`;
- 7. bit: `16`;
- 8. bit: `8`;
- 9. bit: `4`;
- 10. bit: `2`;
- 11. bit: `1`.


Za svaku liniju, sabraćemo vrednosti koje odgovaraju ciframa `1` da bismo dobili decimalni broj ekvivalentan binarnom broju. Uzmimo primer binarne linije koja je jednaka:


```plaintext
1010 1101 101
```


Konverzija bi bila sledeća:

![mnemonic](assets/notext/21.webp)

Rezultat bi tada bio:


```plaintext
1389
```


Za svaki bit jednak `1`, prijavite odgovarajući broj ispod. Za svaki bit jednak `0`, ne prijavljujte ništa.


![mnemonic](assets/notext/22.webp)

Zatim, jednostavno saberite sve brojeve validirane pomoću `1` da biste dobili decimalni broj koji predstavlja svaki binarni red. Na primer, evo kako to izgleda za moj list:

![mnemonic](assets/notext/23.webp)


## Korak 4: Pretraga reči fraze Mnemonic


Sa dobijenim decimalnim brojevima, sada možemo locirati odgovarajuće reči na listi kako bismo sastavili Mnemonic frazu. Međutim, numeracija 2048 reči na BIP39 listi kreće se od `1` do `2048`. Ali, naši izračunati binarni rezultati kreću se od `0` do `2047`. Stoga, postoji pomak za jednu jedinicu koji treba ispraviti. Da biste ispravili ovaj pomak, jednostavno dodajte `1` na dvanaest prethodno izračunatih decimalnih brojeva.


![mnemonic](assets/notext/24.webp)


Nakon ovog prilagođavanja, imate rang svakog reči unutar liste. Sve što preostaje je da identifikujete svaku reč po njenom broju. Očigledno, kao i kod svih drugih koraka, ne smete koristiti računar za izvođenje ove konverzije. Stoga, obavezno unapred odštampajte listu.


[**-> Odštampaj BIP39 listu u A4 formatu.**](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf)


Na primer, ako je broj dobijen iz prvog reda 1721, odgovarajuća reč će biti 1721. na listi:


```plaintext
1721. strike
```


![mnemonic](assets/notext/25.webp)

Na ovaj način, sukcesivno nastavljamo sa 12 reči kako bismo konstruisali našu Mnemonic frazu.


![mnemonic](assets/notext/26.webp)


## Korak 5: Kreiranje Bitcoin Wallet


U ovom trenutku, sve što preostaje je da uvezemo našu Mnemonic frazu u Bitcoin Wallet softver. U zavisnosti od naših preferencija, ovo se može uraditi na desktop softveru da bismo dobili Hot Wallet, ili na Hardware Wallet za Cold Wallet.


![mnemonic](assets/notext/27.webp)


Samo tokom uvoza možete proveriti validnost vašeg kontrolnog zbira. Ako softver prikaže poruku kao što je `Invalid Checksum`, to znači da se greška uvukla u vaš proces kreiranja. Generalno, ova greška potiče ili iz pogrešnog proračuna tokom ručnih konverzija i sabiranja, ili iz tipografske greške prilikom unosa vaše entropije u terminal na Tails-u. Biće potrebno da ponovo pokrenete proces od početka kako biste ispravili ove greške.


![mnemonic](assets/notext/28.webp)

Nakon što kreirate svoj Wallet, ne zaboravite da napravite rezervnu kopiju vaše fraze za oporavak na fizičkom medijumu, kao što je papir ili metal, i uništite tabelu korišćenu tokom njenog generisanja kako biste sprečili bilo kakvo curenje informacija.


## Specifičan slučaj opcije bacanja kockica na Coldcard uređajima


Hardverski novčanici iz porodice Coldcard nude [funkciju pod nazivom _Dice Roll_](https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7), za generate oporavak fraze vašeg Wallet pomoću kockica. Ova metoda je odlična jer vam daje direktnu kontrolu nad kreiranjem entropije, bez potrebe za korišćenjem spoljnog uređaja za izračunavanje kontrolne sume kao u našem vodiču.


Međutim, nedavno su prijavljeni incidenti krađe Bitcoin zbog nepravilne upotrebe ove funkcije. Zaista, previše ograničen broj bacanja kockica može dovesti do nedovoljne entropije, teoretski omogućavajući brute force napad na Mnemonic frazu i krađu povezanih bitkoina. Da biste izbegli ovaj rizik, savetuje se da izvršite najmanje 99 bacanja kockica na Coldcard-u, što osigurava dovoljnu entropiju.


Metod interpretacije rezultata koji predlaže Coldcard razlikuje se od onog predstavljenog u ovom vodiču. Dok u vodiču preporučujemo 128 bacanja da bismo postigli 128 bita sigurnosti, Coldcard predlaže 99 bacanja da bi se dostiglo 256 bita sigurnosti. Naime, u našem pristupu, za svako bacanje kocke moguća su samo dva ishoda: parni (`0`) ili neparni (`1`). Stoga je entropija generisana svakim bacanjem jednaka `log2(2)`. U slučaju Coldcard-a, koji uzima u obzir šest mogućih strana kocke (od `1` do `6`), entropija po bacanju je jednaka `log2(6)`. Zato u našem vodiču moramo izvesti više bacanja da bismo postigli isti nivo entropije.


```plaintext
Entropy = number of rolls * log2(number of possible outcomes on the dice)

Coldcard :

Entropy = 99 * log2(6)
Entropy = 255.91

Our tutorial :

Entropy = 128 * log2(2)
Entropy = 128
```