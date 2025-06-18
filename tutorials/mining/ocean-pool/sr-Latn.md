---
name: Ocean Mining

description: Uvod u Ocean Mining
---

![signup](assets/cover.webp)


**Maj 2024**


Ocean Mining je donekle jedinstven Mining pool. Ovde nisu potrebni nalozi, adrese e-pošte, niti lozinke. Baš kao i Bitcoin, sve je transparentno, pseudonimno, a saradnici mogu birati između četiri različita bloka šablona.


### Sistem kompenzacije


Sistem kompenzacije Ocean-a naziva se TIDES, "Transparentni Indeks Različitih Proširenih Udelâ". Ovaj sistem beleži rad koji obavljaju rudari, poznat kao "udeli". Bazen izračunava procenat "udela" za svakog saradnika, zatim dodaje njihov Bitcoin Address u šablon bloka bazena kao korisnika ovog procenta Block reward.


Blok šablon se ažurira otprilike svakih 10 sekundi kako bi se uzeli u obzir najunosniji novi transakcije i promenila distribucija Block reward ako je potrebno.


![signup](assets/rem.webp)


Da li su vaši uređaji povezani ili ne u trenutku kada bazen iskopa novi blok nije važno. Već poslati rad se čuva za narednih osam blokova koje bazen pronađe.


Zadržavanje rada za osam blokova umesto resetovanja brojača na nulu sa svakim novim iskopanim blokom znači da će vaša kompenzacija biti 100% tek kada bazen pronađe osam blokova nakon što ste počeli da doprinosite. To takođe znači da ćete nastaviti da budete kompenzovani za osam blokova ako prestanete da doprinosite bazenu.


Ovaj mehanizam izravnava kompenzaciju i obeshrabruje "skakanje po bazenima", što podrazumeva redovno menjanje bazena u zavisnosti od toga koji će verovatno pronaći sledeći blok.


### Povlačenja


Operacija Ocean Mining omogućava svojim saradnicima da povrate "čiste" bitkoine, što znači bitkoine koji su direktno izdati od strane Block reward.


Za razliku od većine drugih bazena, Ocean ne prima novoiskopane bitkoine; adrese saradnika su direktno integrisane u šablon bloka.


Za sada, minimalni iznos da biste zaista imali koristi od čistih bitkoina je 1,048,576 Sats. Sa svakim blokom koji rudari bazen, vaš udeo "udela" mora vam omogućiti više od 1,048,576 Sats da bi vam ih Block reward direktno isplatio.

U suprotnom, vaš Sats će zadržati Ocean dok vaša ukupna nagrada ne premaši ovaj iznos.


Svi bitkoini privremeno čuvani od strane Ocean nalaze se na ovom Address: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, sve je proverljivo na TimeChain-u.](https://Mempool.space/Address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)

Takođe je moguće povući vaš Sats putem Lightning koristeći BOLT12. Videćemo kako da ovo postavimo.


### Naknade za bazen


Naknade se kreću od 0% do 2% u zavisnosti od izabranog šablona bloka.


## Transparentnost okeana


### Podaci o saradniku


![signup](assets/1.webp)


Sve informacije o bazenu su transparentne, uključujući sve korisničke podatke. Da bismo razumeli ovu tačku, uzmimo primer:


[Na Ocean kontrolnoj tabli](https://ocean.xyz/dashboard), imate brojne informacije kao što su Hashrate tokom poslednjih šest meseci, broj učesnika u bazenu, ukupan broj iskopanih bitkoina, itd.


Fokusiraćemo se na odeljak "Contributors". Možete videti listu svih saradnika sa njihovim prosečnim Hashrate tokom poslednja tri sata, kao i procenat **"shares"** i **"Hash"** u odnosu na ostatak grupe.


**"Shares %"** je procenat rada koji je obezbedio doprinosilac u okviru poslednjih osam blokova u poređenju sa ostatkom bazena.


**"Hash %"** je procenat prosečnog Hashrate koji je obezbedio doprinosilac tokom poslednja tri sata u poređenju sa ostatkom bazena.


![signup](assets/2.webp)


Primetićete da su "Contributors" identifikovani kao Bitcoin Address. Možete kliknuti na bilo koju od ovih adresa za više detalja.


Ako uzmemo prvi, onaj sa najvišim Hashrate [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), možete videti sve detalje o ovom korisniku: Hashrate, broj iskopanih bitkoina, sa kojim blokom, pa čak i detalje o svakoj njihovoj mašini (ASICs). Međutim, oni ostaju anonimni, kao i na Bitcoin.


### Blok Šablon


U gornjem levom uglu na kontrolnoj tabli, imate "Sledeći blok". Na ovoj stranici postoje četiri različita šablona blokova. Ocean omogućava svakom saradniku da izabere šablon bloka koji želi da podrži. Ovo nema direktan uticaj na vašu naknadu. Kada bazen iskopa blok, svi saradnici su kompenzovani bez obzira na šablon koji su izabrali. Ovo jednostavno omogućava svima da "glasaju" za šablon bloka koji im odgovara.


![signup](assets/3.webp)


**CORE:** Naknada 2%, ovo je klasični Bitcoin Core šablon bez filtera, kako je napisano na njihovoj stranici "Uključuje transakcije i većinu spama"


**CORE+ANTISPAM:** Naknada 0%, Bitcoin Core sa filterom protiv određenih transakcija kao što su Ordinals "Uključuje transakcije i ograničava spam"


**OCEAN:** Naknada 0%, Bitcoin Čvor "Uključuje samo transakcije i razumno male podatke"


**DATA-FREE:** Naknada 0%, Bitcoin Čvor "Uključuje samo transakcije bez bilo kakvih proizvoljnih podataka"


### Razlika između Bitcoin Core i Bitcoin Knot

Bitcoin Core je softver koji omogućava rad oko 99% Bitcoin čvorova širom sveta. Bitcoin je protokol, što znači da, baš kao i Internet, gde postoji više pretraživača, može postojati nekoliko različitih softverskih programa koji koegzistiraju na istom TimeChain-u. Međutim, zbog brige o kompatibilnosti i kako bi se smanjio rizik od grešaka koje bi ostavile neizbrisive tragove na TimeChain-u, gotovo svi Bitcoin programeri rade na Bitcoin Core. Bitcoin Knots je Fork od Bitcoin Core, što znači da deli većinu njihovog koda, čime se značajno smanjuje rizik od grešaka. Ovaj Fork je kreirao Luke Dashjr, koji je želeo da primeni restriktivnija pravila nego Bitcoin Core bez kreiranja Hard Fork. Sada, Bitcoin Core i Bitcoin Knots koegzistiraju zahvaljujući Nakamoto konsenzusu.


## Dodavanje radnika


Da biste dodali radnika, počnite izborom šablona bloka. Ovaj izbor će odrediti URL bazena koji ćete uneti na vaš Miner (ASICs).



- CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`


Dalje, za polje korisnika unesite Bitcoin Address koji posedujete. Ovde je lista kompatibilnih tipova Address:


- P2PKH** (Originalni tip Address. Počinje sa „1”)
- P2SH** (Multisignature ili P2SH-SegWit. Počinje sa “3”)
- Bech32** (SegWit. Počinje sa „bc“.)
- Bech32m** (Taproot. Počinje sa „bc“. Duže od Bech32.)


Ako imate više rudara, možete uneti isti Address za sve njih kako bi se njihove Hash stope kombinovale i prikazale kao jedan Miner. Takođe ih možete razlikovati dodavanjem različitog imena svakom. Da biste to uradili, jednostavno dodajte “.ime_radnika” nakon Bitcoin Address.


Konačno, za polje za lozinku, koristite `x`.


**Primer:**

Ako izaberete šablon **OCEAN**, vaš Bitcoin Address je `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` i želite da imenujete vaš Miner „Brrrr“, onda ćete morati uneti sledeće informacije u Interface vašeg Miner:



- URL**: `stratum+tcp://mine.ocean.xyz:3334`
- KORISNIK**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- LOZINKA**: `x`


Nekoliko minuta nakon pokretanja Mining, moći ćete da vidite svoje podatke na Ocean sajtu pretraživanjem vašeg Address.


### Pregled kontrolne table


- Akcije u Reward Window**: Ovi podaci pokazuju broj akcija, rad koji ste poslali u bazen u okviru poslednjih 8 blokova koje je bazen iskopao.
- Procijenjene nagrade u Windows**: Procjena broja Sats koje ćete zaraditi sa već obavljenim poslom. Ovo ne uzima u obzir transakcione naknade, već samo coinbase, nove bitcoine koje izdaje mreža.
- Procena Zarade Sledećeg Bloka**: Procena broja Sats zarađenih ako se blok iskopa sada. Zapamtite, ako je ova vrednost manja od 1,048,576 Sats, nećete direktno primiti Sats na vaš Address. Oni će biti poslati na Oceanov Address dok vaša zarada ne premaši ovaj prag.


Ispod, imate grafikon koji prikazuje vašu Hashrate istoriju do 6 meseci.


![signup](assets/4.webp)


Ovde imate prosečan Hashrate tokom različitih vremenskih skala, od 60s do 24h, kao i istoriju blokova koje je rudarski bazen iskopao, a za koje ste doprineli i bili nagrađeni.


![signup](assets/5.webp)


Imate opciju da izvezete CSV fajl ove istorije pomoću dugmeta **Preuzmi CSV**.


![signup](assets/6.webp)


U sledećem odeljku imate listu svih rudara koje ste povezali sa bazenom pomoću ovog Address. Imate, naravno, njihove pojedinačne Hashrate, ali i broj Sats koje su pojedinačno dobili za svoj rad.


![signup](assets/7.webp)


Možete kliknuti na **Nadimak** bilo kojeg Miner. Tada ćete imati sve informacije koje smo upravo videli, ali specifično za taj Miner.


A na dnu stranice, dodatne informacije gde možete videti istoriju uplata na vašem Address, Sats koji ste iskopali, ali još niste plaćeni, i ukupno Sats koji ste iskopali.


![signup](assets/8.webp)


Ovde možete videti da u polju **Procenjeno vreme do minimalne isplate** piše Lightning jer smo postavili BOLT12 ponudu.


### Postavljanje Lightning povlačenja


Kao što ste razumeli, Ocean ima za cilj da maksimizira transparentnost i minimizira starateljstvo (držanje vašeg Sats u vaše ime).


Zato je, za Lightning isplate, neophodno koristiti **BOLT12 ponude**. Ovo je novi način plaćanja na Lightning Network koji počinje da se pojavljuje 2024. godine i omogućava nekoliko stvari:


- To je višekratni link za plaćanje, koji omogućava automatska plaćanja i, za razliku od Lightning Address, BOLT12 je ne-kustodijalan.
- Takođe je metod plaćanja koji pruža dokaz da je uplata izvršena, što nije slučaj sa LNURL-ovima.
- Veoma važno, može se koristiti zajedno sa Bitcoin potpisom da dokaže da ste i vlasnik BTC Address i BOLT12 ponude.

Od danas (maj 2024), postoji nekoliko rešenja za korišćenje ove metode. U ovom primeru, koristićemo Start9 server sa Core Lightning. Kada drugi alati, kao što je Phoenix Wallet na primer, integrišu BOLT12 ponude, ovaj vodič će ostati primenljiv. Uverite se da imate otvorene kanale sa dolaznom likvidnošću, inače plaćanja neće funkcionisati.


Počnite tako što ćete otići na svoju kontrolnu tablu na Ocean sajtu unosom vašeg BTC Address, zatim kliknite na karticu **Configuration**.


![signup](assets/9.webp)


Kopiraćemo tekst **Description**, ovde:

`OCEAN Isplate za bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`


Sada idite na vaš Core Lightning Interface na vašem Start9 serveru (ili bilo koji Wallet sposoban da pruži BOLT12 ponudu).


![signup](assets/10.webp)


Kliknite na **Primi**.


Proveri **Ponudu**, zatim nalepi prethodno kopirani tekst u polje **Opis** i ostavi polje **Iznos** prazno.


![signup](assets/11.webp)


Kliknite na **generate Ponuda**.


![signup](assets/12.webp)


Generisali ste višekratni i trajni link za plaćanje koji ne zahteva centralni server kao što je slučaj sa Lightning adresama. Kopirajte link i zatim se vratite na Ocean stranicu.


U polje **Lightning BOLT12 Offer** zalepite link za plaćanje i ostavite polje **Block Height** na njegovoj podrazumevanoj vrednosti. Kliknite na **generate**.


![signup](assets/13.webp)


Da bi Ocean osigurao da je ovaj link za plaćanje zaista vaš bez korišćenja sistema naloga, potrebno je da potpišete poruku koja je upravo generisana vašim privatnim ključem koji odgovara Bitcoin Address koji koristite. Postoji mnogo rešenja za potpisivanje poruke vašim privatnim ključem. U ovom vodiču, uzećemo primer BlueWallet-a, ali metoda je ista za sve novčanike.


![signup](assets/14.webp)


Pod pretpostavkom da je vaš privatni ključ u BlueWallet-u (možete učiniti isto sa Hardware Wallet), kliknite na odgovarajući Wallet.


![signup](assets/15.webp)


Zatim na **…** u gornjem desnom uglu.


![signup](assets/15bis.webp)


I **potpiši/verifikuj poruku**.


![signup](assets/16.webp)


U ovom prozoru imate tri polja: **Address**, **Potpis**, i **Poruka**.


U polje **Address** unesite vaš Bitcoin Address. Ako se vratimo na naš primer, to je Address: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.


Ostavite polje **Potpis** prazno.

I nalepite generisanu poruku u polje **Poruka** na Ocean-ovoj stranici: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`

Kliknite na **Sign**.


Ovo će generate biti kriptografski potpis koji dokazuje da ste vlasnik Address `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, i ovaj potpis je jedinstven zahvaljujući poruci koju je obezbedio Ocean, generisanoj iz BOLT12 linka za plaćanje.


![signup](assets/17.webp)


Kopiraj potpis i nalepi ga na Oceanovu stranicu, zatim klikni na **POTVRDI**.


![signup](assets/18.webp)


Trebalo bi da vidite poruku o potvrdi.


![signup](assets/19.webp)


Sada idite na karticu **My Stats**. Dodatne informacije su prikazane na vrhu sa BOLT12 linkom za plaćanje koji ste prethodno generisali sa Core Lightning na Start9.


![signup](assets/20.webp)