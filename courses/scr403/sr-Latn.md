---
name: Duboko zaranjanje u Simplicity
goal: Savladajte filozofiju dizajna, sistem tipova i ceo životni ciklus jezika Simplicity
objectives:
  - Razumeti tri osnovna načina kompozicije i devet kombinatora koji čine potpun jezik
  - Izgraditi logiku Bulovih vrednosti, aritmetiku i SHA-256 iz minimalnog sistema tipova jezika Simplicity
  - Shvatiti kako sporedni efekti Failure i Reader omogućavaju stvarnu interakciju sa blokčejnom
  - Naučiti kako Simplicity programi postaju Taproot adrese i kako se troše pomoću witness podataka
---

# Duboko zaranjanje u Simplicity

Duboko istraživanje teorije i dizajnerskih odluka iza jezika Simplicity, zasnovano na kompletnoj seriji od pet članaka ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) autora [dr. Russella O'Connora](https://r6.ca/), tvorca jezika Simplicity u Blockstream Research. Ovaj kurs objašnjava *zašto* je Simplicity projektovan baš tako, a ne kako se u njemu piše.

Kurs prati članke dr. O'Connora kroz tri osnovna načina kombinovanja izračunavanja, minimalni sistem tipova i njegovu teoremu potpunosti, izgradnju praktičnih tipova podataka i aritmetike od prvih principa, pažljivo uvođenje sporednih efekata za interakciju sa blokčejnom, i na kraju način na koji se programi ugrađuju u adrese i troše on-chain.

+++

# Uvod

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Pregled kursa

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Dobrodošli u SCR403 — Duboko zaranjanje u Simplicity!

Ovaj kurs je zasnovan na seriji članaka **"Delving Simplicity"** koju je napisao [dr. Russell O'Connor](https://r6.ca/), developer infrastrukturne tehnologije u [Blockstreamu](https://blockstream.com/) i tvorac jezika Simplicity. Originalni članci su objavljeni na forumu [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) i predstavljaju primarni izvorni materijal za ovaj kurs. Zahvalni smo mu na pionirskom radu, koji je omogućio ovaj obrazovni sadržaj.

### Šta ćete naučiti

Ovaj kurs istražuje filozofiju dizajna i matematičke osnove jezika Simplicity, skriptnog jezika nove generacije aktiviranog na [Liquid Networku](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) u julu 2025. Prati kompletnu seriju od pet članaka i strukturisan je u dve glavne sadržajne celine:

1. **Osnove jezika Simplicity** — Zašto blokčejn izračunavanje zahteva fundamentalno drugačiji jezik, tri načina kombinovanja operacija (sekvencijalni, paralelni, uslovni) i devet osnovnih kombinatora koji čine matematički potpun jezik
2. **Od tipova podataka do programa** — Izgradnja logike Bulovih vrednosti, aritmetike i SHA-256 od prvih principa; razumevanje sporednih efekata Failure i Reader koji omogućavaju interakciju sa blokčejnom; i učenje kako se programi ugrađuju u Taproot adrese putem Commitment Merkle Root-ova i troše pomoću witness podataka

### Preduslovi

Ovo je kurs **ekspertskog nivoa** (približno 10 sati). Trebalo bi da vam budu bliski:
- Osnovni koncepti Bitcoin skriptovanja (šta radi validacija transakcije)
- Fundamentalni programski koncepti (tipovi, funkcije, kompozicija)
- Izvesno poznavanje matematičke notacije je korisno, ali nije obavezno. Sve uvodimo kako napredujemo

### Ključni resursi

- **Originalni članci**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) dr. Russella O'Connora na Delving Bitcoin
- **Simplicity repozitorijum**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — izvorni kod i formalni dokazi u Rocq-u
- **Zvanični sajt**: [simplicity-lang.org](https://simplicity-lang.org/) — dokumentacija i referenca za SimplicityHL
- **Blockstream blog**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — tehnički pregled

Spremni da zaronite u jedan od najelegantnijih komada Bitcoin inženjeringa? Krenimo!

## Šta je Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Ako dolazite na ovaj kurs bez predznanja o Simplicityju, ovo poglavlje će vas orijentisati pre nego što zaronimo u dubinu.

### Simplicity ukratko

Simplicity je **jezik pametnih ugovora izvorno za Bitcoin**, danas aktivan na Liquid Networku. Prvi put ga je zamislio dr. Russell O'Connor oko 2012. godine, a detaljno je opisan u njegovom radu iz 2017. *Simplicity: A New Language for Blockchains*; aktiviran je na Liquid Networku u julu 2025, nakon godina formalne verifikacije i razvoja.

Za razliku od Ethereumovog Solidityja, koji je Turing-kompletan jezik ugovora visokog nivoa, Simplicity je namerno minimalan. Ima:
- **Tri konstruktora tipova** (jedinični, suma, proizvod)
- **Devet kombinatora** (osnovne operacije i pravila kompozicije)
- **Bez petlji, bez rekurzije, bez dinamičke memorije**

Iz samo tih primitiva možete izgraditi svako izračunavanje koje vam je potrebno za validaciju transakcije, od logike Bulovih vrednosti do punog SHA-256 heširanja.

### Šta danas možete raditi sa Simplicityjem?

Simplicity već pokreće stvarne aplikacije na Liquid Networku. Najistaknutija je [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), tržište opcija bez orakla gde korisnici trguju call opcijama na L-BTC koristeći USDt kao kolateral (osnovni ugovor podržava i put opcije). Drugi živi Simplicity projekti uključuju [Swaption](https://swaption.io/) kompanije SideSwap (opcije) i projekat otvorenog koda [Deadcat](https://github.com/Resolvr-io/deadcat) kompanije Resolvr (tržišta predviđanja). Izvan DeFi-ja, Simplicity omogućava napredne uslove trošenja kao što su trezori, covenant-i i složene multisig šeme koje bi bile nemoguće ili nesigurne u Bitcoin Scriptu.

### Šta ovaj kurs jeste — i šta nije

Ovo **nije** praktični tutorijal za kodiranje. Ovde nećete pisati Simplicity programe. Ako to tražite, pogledajte:
- [simplicity-lang.org](https://simplicity-lang.org/) — zvaničnu dokumentaciju i jezik visokog nivoa SimplicityHL
- [Simplicity GitHub repozitorijum](https://github.com/BlockstreamResearch/simplicity) — referentnu implementaciju, primere i Rocq dokaze
- [Blockstream blog objavu](https://blog.blockstream.com/en-simplicity-github/) o tome kako početi

Ono čime se ovaj kurs **bavi**: **filozofskim i tehničkim izborima** iza dizajna jezika Simplicity. Zašto je ovaj jezik napravljen baš ovako? Zašto samo devet kombinatora? Zašto nema rekurzije? Zašto je važno to što se sistem tipova povezuje sa Gentzenovim sekventnim računom?

Zamislite to kao razumevanje **zašto je motor napravljen baš ovako**, umesto učenja kako da vozite auto.

### Kome je namenjen?

Ovaj kurs je idealan za:
- **Developere protokola** koji žele da razumeju osnove jezika Simplicity pre pisanja koda
- **Bitcoin istraživače** zainteresovane za formalnu verifikaciju i pristup zasnovan na teoriji tipova
- **Računarske naučnike** radoznale u vezi sa vezom između sekventnog računa i blokčejn izračunavanja
- **Napredne bitkoinere** koji žele da prevaziđu površinsko razumevanje Liquidovih mogućnosti skriptovanja

Ako su vam termini poput "tipovi sume", "kombinatori" ili "sekventni račun" potpuno novi, ne brinite, sve objašnjavamo od početka. Ali budite spremni na gusto, matematičko putovanje.

### Od članaka do kursa

Originalna serija "Delving Simplicity" dr. O'Connora strukturisana je kao pet tehničkih članaka. Ovaj kurs reorganizuje i anotira taj materijal u progresivnu putanju učenja sa kvizovima koji proveravaju vaše razumevanje usput. Ideje, definicije i dokazi su njegovi, a mi smo format prilagodili strukturisanom obrazovanju.

# Osnove jezika Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Fundamentalni načini kombinovanja izračunavanja

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Sada kada je Simplicity aktiviran na Liquid Networku, želeo bih da napravim detaljno zaranjanje u filozofiju i dizajn jezika Simplicity.

Bitcoinova validacija transakcija je značajno drugačija primena od običnog dizajna programskih jezika. Cena prostora u bloku je velika, pa programi moraju biti kompaktni. Programi u Bitcoin transakcijama se uvek izvršavaju samo nad jednim ulazom i svi izvršavaju program nad istim ulazom. Takođe, akter koji autorizuje transakciju već unapred zna ishod izračunavanja: da je transakcija validna.

Tipično će akter koji autorizuje izvršiti mnogo skuplja izračunavanja kako bi izveo witness podatke koji potvrđuju validnost transakcije, dok programi koji se izvršavaju na blokčejnu treba da provere validnost witness podataka. Provera validnosti je često mnogo jeftinija od dokazivanja validnosti.

Dizajnirali smo Simplicity imajući na umu ove jedinstvene izazove dizajna jezika. Na primer, Simplicity zahteva da se neizvršene grane orežu tako da se ne pojavljuju na blokčejnu. Koraci predobrade pažljivo su dizajnirani tako da pokazuju (kvazi-)linearnu vremensku složenost u odnosu na veličinu Simplicity programa. Umesto "gasa" koristi se statička analiza, jer se gas ne može izračunati bez izvršavanja koda na propisan način, tako da detalji modela izvršavanja ne postanu kritični za konsenzus. Nema dinamičke alokacije memorije tokom izvršavanja. I tako dalje.

Pre nego što zaronimo u detalje dizajna jezika Simplicity, želim da ovu seriju počnem malo programskom filozofijom o opštim načinima kombinovanja osnovnih građevnih blokova radi stvaranja nove funkcionalnosti.

### Kompozicija

Pretpostavimo da neko dizajnira jezik za programabilne transakcije za blokčejn poput Bitcoina. Konkretno, programi imaju pristup samo podacima transakcije i UTXO podacima ulaza, a izvršavanje samo određuje validnost transakcije (što omogućava keširanje rezultata izvršavanja). Recimo da se počinje sa nekim skupom osnovnih operacija koje mogu obavljati razne zadatke, kao što su osnovna izračunavanja, čitanje i/ili obrada podataka iz transakcije i verifikacija potpisa. Svaka operacija troši neki tip ulaza (moguće prazan) i vraća neki tip izlaza. Koji su načini na koje možemo kombinovati te osnovne operacije u složenije operacije?

### Sekvencijalna kompozicija

![Sekvencijalna kompozicija](assets/en/001.webp)

Najfundamentalniji metod kompozicije je sekvencijalna kompozicija. Ako imamo dve osnovne operacije, pri čemu tip izlaznih podataka jedne odgovara tipu ulaznih podataka druge, možemo kombinovati te dve operacije u novu kompozitnu operaciju. Ta nova operacija izvršava ove dve osnovne operacije u nizu, uzimajući kao ulaz ulaz prve operacije, prosleđujući izlaz te prve operacije u ulaz druge operacije, i na kraju vraćajući izlaz te druge operacije.

Naravno, ne moramo da se ograničimo samo na kombinovanje osnovnih operacija. Sada kada imamo neke kompozitne operacije, možemo i njih kombinovati pomoću funkcionalne kompozicije.

U matematici se ova sekvencijalna kompozicija često jednostavno naziva "kompozicija", pa bi neko mogao pomisliti da je to jedini način komponovanja stvari. Međutim, imamo i druge načine komponovanja operacija.

### Paralelna kompozicija

![Paralelna kompozicija](assets/en/002.webp)

Pretpostavimo da imamo dve operacije; mogu biti osnovne ili složene, i obe uzimaju isti tip ulaza. Drugi fundamentalni način komponovanja ove dve operacije jeste da se obe izvrše nad istim ulazom. To se zove paralelna kompozicija, a tip izlaza je "proizvod" tipova izlaza originalnih operacija i sadrži par dva izlaza.

Iako se to zove "paralelna" kompozicija, i dve operacije bi se u principu mogle izvršavati paralelno, paralelno izvršavanje nije operativni zahtev. Paralelnu kompoziciju možemo implementirati "sekvencijalno" tako što prvo izvršimo jednu operaciju, a zatim drugu. Ne zanimaju nas detalji implementacije paralelne kompozicije sve dok je izlaz isti.

### Uslovna kompozicija

![Uslovna kompozicija](assets/en/003.webp)

Uslovna kompozicija je dual paralelne kompozicije. U ovom slučaju imamo dve operacije koje proizvode isti izlaz, a komponujemo ih tako što biramo jednu od njih za izvršavanje. Ulaz za ovu kompozitnu operaciju je "suma" ili "tagovana unija" tipova ulaza originalne operacije. U ovom slučaju tag, "Left" ili "Right", predstavlja jedan bit u podacima ulaza koji određuje koji se tip podataka nosi, a samim tim i koja se od dve operacije može izvršiti.

Uslovna kompozicija funkcioniše na isti način čak i kada je ulaz suma dva identična tipa. Tip sume i dalje sadrži tag, a vrednost tog taga određuje koja od dve operacije treba da se izvrši.

### Kompozicija u Bitcoin Scriptu

Postoji mnogo načina da se ove tri vrste kompozicije realizuju u različitim programskim jezicima. U Bitcoin Scriptu, sekvencijalna kompozicija se realizuje (približno) nadovezivanjem dve rutine (zato se Bitcoin Script naziva konkatenativnim programskim jezikom), pošto se izlaz jedne rutine ostavlja na steku da ga potroši naredna rutina. Paralelna kompozicija se postiže upotrebom operacija dupliranja i zamene za manipulaciju stekom tako da se dve rutine mogu izvršiti nad istim ulazom. Stvari nisu sasvim jednostavne, jer se ono što nazivamo "proizvodom" tipova obično realizuje korišćenjem više stavki na steku. Nadam se da vidite opštu ideju.

Uslovna kompozicija se, naravno, realizuje pomoću `OP_IF`, koji grana na osnovu vrednosti na steku. U ovom slučaju gornja stavka na steku igra ulogu taga, a obično su naredna stavka ili stavke na steku različitih "tipova" koji zavise od vrednosti taga. Za svaki slučaj, tipovi stavki na steku mogu biti pogodni za obradu samo od strane jedne od grana u `OP_IF`. Međutim, nakon što stignemo do `OP_ENDIF`, stavke na steku moraju biti konzistentnog "tipa" tako da preostali skript može da nastavi nezavisno od toga koja je grana prethodno izabrana.

### Kompozicija u Simplicityju

Simplicity smo dizajnirali sa kombinatorima koji direktno implementiraju ove tri forme kompozicije. Uz još nekoliko kombinatora koji podržavaju druge osnovne operacije povezane sa tipovima proizvoda i sume, jezgro jezika Simplicity na kraju se sastoji od devet kombinatora dovoljnih za izražavanje svakog konačnog izračunavanja. O tome ćemo detaljnije govoriti u sledećem poglavlju.

### Četvrta vrsta kompozicije

Pre kraja treba pomenuti da u računarstvu postoji bar još jedna vrsta kompozicije, a to je "rekurzivna kompozicija". U rekurzivnoj kompoziciji jedna operacija se iterira više puta.

Imajte na umu da Bitcoin Script ne podržava rekurzivnu kompoziciju, a slično tome, izričito smo isključili neograničenu rekurziju iz dizajna jezika Simplicity. Naša teza je da je neograničeno iterativno izračunavanje bolje implementirati pomoću rekurzivnih covenant-a koji računaju kroz više transakcija. To korisnicima omogućava da izbegnu ograničenja prostora u bloku i standardnosti i da bolje predvide troškove transakcija.

Ipak, postoje načini zloupotrebe Simplicityjeve funkcije delegiranja da se obezbedi nešto što podseća na neograničenu rekurzivnu kompoziciju, o čemu ćemo možda govoriti kasnije u ovoj seriji.

### Zaključak

Pregledali smo tri glavne forme kompozicije za transformisanje osnovnih operacija u složene operacije:

- sekvencijalna kompozicija
- paralelna kompozicija
- uslovna kompozicija

Razmotrili smo kako se ove forme kompozicije realizuju u Bitcoin Scriptu i nagovestili kako su uticale na dizajn jezika Simplicity. Primetili smo da je četvrta vrsta kompozicije, rekurzivna kompozicija, posebno isključena i iz Simplicityja i iz Bitcoin Scripta.

U sledećem poglavlju opisaćemo devet kombinatora koji čine jezgro jezika Simplicity, kako služe direktnoj realizaciji ove tri forme kompozicije i kako to formira potpun jezik za opisivanje svakog konačnog izračunavanja.

## Potpunost kombinatora jezika Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

U ovom poglavlju uvodimo jezgro jezika Simplicity i pokazujemo da je jezik potpun, što znači da se svako konačno izračunavanje može izraziti u njemu.

### Simplicity tipovi

Simplicity podržava tri fundamentalna konstruktora tipova. Tip proizvoda `A × B` predstavlja izlaze paralelne kompozicije, dok tip sume `A + B` (tagovana unija) obrađuje ulaze uslovne kompozicije. Treći tip je jedinični tip.

### Jedinični tip

Jedinični tip, označen kao `𝟙` ili `ONE`, sadrži tačno jednu vrednost: praznu torku `⟨⟩` ili `()`. Ovaj nultobitni tip podataka ne nosi nikakvu informaciju.

### Tip sume

Tip sume `A + B` kombinuje dva tipa sa tagovima koji označavaju "levo" ili "desno". Vrednosti se pišu kao `σᴸ(a)` ili `inl(a)` za vrednosti tagovane levo i `σᴿ(b)` ili `inr(b)` za vrednosti tagovane desno. Tagovi ostaju različiti čak i kada se kombinuju identični tipovi.

#### Bulov tip

Tip `𝟙 + 𝟙`, označen kao `𝟚` ili `TWO`, predstavlja jednobitni tip sa dve vrednosti. Po konvenciji, `σᴸ⟨⟩` predstavlja false/nulu, dok `σᴿ⟨⟩` predstavlja true/jedinicu.

### Tip proizvoda

Tipovi proizvoda `A × B` sadrže parove vrednosti koji se pišu kao `⟨a, b⟩` ili `(a, b)`. Tip `𝟚 × 𝟚` ima četiri vrednosti, različite od četiri vrednosti u `𝟚 + 𝟚`.

### Jezgreni Simplicity izrazi

Operacije se označavaju kao `f : A ⊢ B`, što znači ulazni tip `A` i izlazni tip `B`. Simplicity je "prvog reda" — nema funkcijske tipove.

### Dve osnovne operacije

Jezgreni jezik pruža dve osnovne operacije:

**Identitet (`iden`).** Operacija identiteta propušta svoj ulaz neizmenjen:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Jedinica (`unit`).** Jedinična operacija odbacuje svoj ulaz i vraća praznu torku:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

One formiraju porodice sa jednom operacijom po tipu.

### Tri kombinatora kompozicije

Sekvencijalna kompozicija koristi `comp f g` (piše se `f ⨾ g` ili `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Paralelna kompozicija koristi `pair f g` (piše se `f ▵ g` ili `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Uslovna kompozicija koristi `case f g : (A + B) × C ⊢ D`, pružajući granama pristup zajedničkom okruženju `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Zašto uslovna kompozicija ima ovaj oblik — suma u paru sa zajedničkim okruženjem `C` — umesto jednostavnijeg `copair f g : A + B ⊢ C` koji samo bira granu? Zato što goli `copair` ne može da izrazi **distribuciju**: funkciju `dist : (A + B) × C ⊢ A × C + B × C` koja gura zajednički ulaz u onu granu koja je izabrana. Ugradnjom okruženja `C` direktno u `case`, Simplicity dobija uslovnu kompoziciju *i* distribuciju iz jednog kombinatora — jednu od ključnih dizajnerskih odluka koja jezgro jezika drži na devet kombinatora.

### Još četiri kombinatora

Potrošnja proizvoda koristi `take` i `drop`:

**take** izvlači levi element:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** izvlači desni element:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Proizvodnja sume koristi `injl` i `injr`:

**injl** obavija levim tagom:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** obavija desnim tagom:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Devet jezgrenih kombinatora

Ukupno, Simplicity ima tačno devet jezgrenih kombinatora:

| Kombinator | Svrha |
|---|---|
| `iden` | Propušta ulaz |
| `unit` | Odbacuje ulaz |
| `comp` | Sekvencijalna kompozicija |
| `pair` | Paralelna kompozicija |
| `case` | Uslovna kompozicija |
| `take` | Izvlači levo iz proizvoda |
| `drop` | Izvlači desno iz proizvoda |
| `injl` | Ubrizgava u levo sume |
| `injr` | Ubrizgava u desno sume |

### Simplicity i sekventni račun

Dizajn jezika Simplicity izvodi se iz konjunktivno-disjunktivnog fragmenta Gentzenovog sekventnog računa. Preciznije, to je varijanta *funkcionalne interpretacije* sekventnog računa, koja je sama analogna Curry-Howardovoj korespondenciji između prirodne dedukcije i lambda računa. Pravila kombinatora pokazuju "manje tipove u premisama nego u zaključcima", što Bit Machineu — Simplicityjevom apstraktnom interpreteru zasnovanom na steku — omogućava da minimizuje kopiranje podataka tokom izvršavanja.

### Vrednosti nisu izrazi

Simplicity izrazi označavaju operacije, ne vrednosti. Notacija `scribe b : A ⊢ B` predstavlja jedinstven izraz koji uvek vraća vrednost `b`, služeći kao notacijska pogodnost, a ne kao kombinator. To odražava Bitcoin Script, gde operacije poput `OP_1` guraju vrednosti umesto da ih direktno izražavaju.

### Simplicityjeva teorema potpunosti

Kada imamo svih devet kombinatora, kako znamo da nam ništa ne nedostaje — da je tih devet zaista dovoljno? Simplicityjeva teorema potpunosti daje odgovor: za svaku funkciju između (konačnih) Simplicity tipova, neki Simplicity izraz je označava. Dokaz je konstruktivan — pokazuje kako se izraz gradi:

1. **Razložite ulaz**: Pomoću ugnježdenih `case` izraza, potpuno razložite svaki ulaz bilo kog tipa na njegove sastavne bitove
2. **Izgradite lookup tabelu**: Za svaki mogući ulaz, koristite `scribe` da proizvedete odgovarajući izlaz
3. **Sastavite**: Ugnježdeni slučajevi i scribes zajedno formiraju ogromnu lookup tabelu koja implementira funkciju

Ova teorema je formalno verifikovana u Rocq asistentu za dokaze (ranije Coq). Dokaz je deo zvaničnog Simplicity repozitorijuma i mašinski je proveren na ispravnost.

Iako teorema potpunosti garantuje da devet Simplicityjevih kombinatora može izraziti svaku funkciju između (konačnih) Simplicity tipova, rezultujući izrazi iz konstrukcije lookup tabele nepraktično su veliki. Funkcija nad 256-bitnim ulazima zahtevala bi lookup tabelu sa 2²⁵⁶ unosa. Zato se sledeća poglavlja fokusiraju na izgradnju efikasnih izraza koji iskorišćavaju strukturu izračunavanja, umesto da se sve brute-force pristupom gura kroz lookup tabele.

### Zaključak

Jezgreni jezik Simplicity uključuje sistem tipova i kombinatore koji omogućavaju svako konačno izračunavanje. Iako teorema potpunosti garantuje izražajnost, rezultujući izrazi iz generičke konstrukcije nepraktično su veliki. Praktični razvoj u Simplicityju uključuje iskorišćavanje računske strukture za sažete izraze. Sledeća poglavlja istražuju strukture podataka, interakcije sa transakcijama i dodatne kombinatore.

# Od tipova podataka do programa

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Izgradnja tipova podataka

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

U prethodnim poglavljima pokazali smo kako je jezgreni skup Simplicity kombinatora dovoljan za implementaciju svakog konačnog čistog izračunavanja. Ovo poglavlje pokazuje kako se iz tih primitiva grade praktične strukture podataka i izračunavanja — na isti način na koji su računari izgrađeni od logičkih kola.

### Logika Bulovih vrednosti

Bulov tip, označen kao `𝟚`, jednak je `𝟙 + 𝟙` i ima dve vrednosti: `σᴸ⟨⟩` (false) i `σᴿ⟨⟩` (true). Pomoću jezgrenih kombinatora mogu se konstruisati operatori logike Bulovih vrednosti.

#### Operacija And

Logička operacija `and : 𝟚 × 𝟚 ⊢ 𝟚` uzima dva bita i vraća jedan bit. Implementacija grana na prvom bitu: ako je false, vrati false; u suprotnom, vrati drugi bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testiranje sa `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Testiranje sa `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Druge logičke operacije

Operacija `not` zahteva pomoćni kombinator:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Početno `iden ▵ unit : A ⊢ A × 𝟙` dodaje prazno "okruženje" ulazu, omogućavajući primenu kombinatora `case`. Upotreba `take` u dve grane odbacuje to prazno okruženje da bi izvršila `f` ili `g`.

Druge logičke operacije nad Bulovim vrednostima:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bit sabirači

"Polusabirač" uzima dva bita i sabira ih, proizvodeći dvobitni izlaz: bit prenosa i bit zbira.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

"Puni sabirač" sabira tri bita, proizvodeći dvobitni izlaz. Ulaz koristi ugnježdenu torku `(𝟚 × 𝟚) × 𝟚`.

Za ugnježdene torke koristi se kompaktna notacija:

- `O f` označava `take f`
- `I f` označava `drop f`
- `H` označava `iden`

Na primer, `I O H` znači `drop (take iden) : A × (B × C) ⊢ B`, izvlačeći srednju vrednost. Notacija priziva binarne cifre: kada se o ugnježdenim torkama razmišlja kao o binarnim stablima, notacija predstavlja obrnute binarne cifre položaja u stablu. Ovi izrazi formiraju De Bruijnove indekse za Simplicity.

**Napomena:** Notacija `I`, `O` i `H` primenjuje se samo na podizraze koji se sastoje isključivo od `take`, `drop` i `iden`.

Puni sabirač komponuje dva polusabirača, uzimajući logički `or` bitova prenosa:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

U prvoj liniji, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` pokreće polusabirač nad prva dva bita, čuvajući poslednji bit.

U drugoj liniji, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` čuva prvi bit (izlazni prenos prvog polusabirača) i pokreće polusabirač nad poslednja dva bita.

U poslednjoj liniji, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` uzima logički OR prva dva bita (izlazne prenose oba polusabirača) i vraća izlazni bit zbira drugog polusabirača.

Ovo demonstrira programiranje u Simplicityju: korišćenje notacije `I`, `O` i `H` za referenciranje bitova podataka, formiranje pogodnih "okruženja" za pozivanje drugih funkcija putem sekvencijalne kompozicije.

Korisnici ne definišu direktno operacije niskog nivoa. Kasnije u ovoj seriji razmatra se standardna biblioteka jetova koji implementiraju uobičajene funkcije. Od krajnjih korisnika se ne očekuje da programiraju direktno u Simplicityju, slično kao u Bitcoin Scriptu. Umesto toga, jezici višeg nivoa poput SimplicityHL generišu Simplicity kod, upravljajući "okruženjima" podizraza i prevodeći imenovane promenljive u odgovarajuće sekvence `take` i `drop`.

### Vektori

Vektori fiksne dužine definišu se formiranjem iteriranih proizvoda tipa `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Oni se mogu pisati kao `A^2`, `A^4`, `A^8` itd.

Vektori su definisani samo za dužine koje su stepeni dvojke. Drugi stepeni zahtevaju izbor konvencija zagrađivanja.

Za dati izraz `f : A ⊢ B`, ponovljeno uparivanje ga "mapira" preko vektora fiksne dužine:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Za datu funkciju `f : A × B ⊢ B`, iteracija ili "folding" preko vektora fiksne dužine:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Postoji mnogo varijacija. Za dato `f : A × B ⊢ C`, "zip" preko uparenih vektora sa `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Za dato `f : (A × B) × C ⊢ C`, fold preko uparenih vektora sa `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Kombinovanje `map` i `fold-right` stvara akumulirajuće kombinatore: `f : A × C ⊢ C × B` daje `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Moguće su još mnoge varijante.

#### Višebitne reči

Bit vektor daje višebitne cele brojeve. Na primer, `𝟚³²` je tip 32-bitne reči. `𝟚²⁵⁶` je tip 256-bitne reči, pogodan za heševe i kriptografske operacije.

Koristeći puni sabirač, jedna varijanta vektorskih operacija definiše "ripple carry sabirač" nad višebitnim rečima:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` uzima dva n-bitna binarna broja i jednobitni ulazni prenos, vraćajući jednobitnu zastavicu izlaznog prenosa i n-bitni zbir.

#### SHA-256

Rekurzivnim definisanjem aritmetičkih operacija nad višebitnim rečima — oduzimanja, množenja, deljenja — i bitovnih logičkih operacija kao što su logički AND, OR, XOR, i njihovim ponovljenim kombinovanjem, može se izgraditi čak i funkcija kompresije bloka za SHA-256:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

SHA-256 kompresija formalno je definisana pomoću Simplicityja u Rocq asistentu za dokaze (ranije Coq), uz formalni dokaz da je implementacija `sha256-hash-block` ispravna.

Kompresija radi presporo kao sirovi Simplicity. Jetovi nativno izvršavaju uobičajene funkcije poput SHA-256 kompresije. Čiste Simplicity implementacije služe kao formalne specifikacije za jetove.

### Opcioni tipovi

Opcioni tipovi nastaju uzimanjem sume sa jediničnim tipom:

```
Option A ≔ 𝟙 + A
```

Tip `Option A` može se pisati kao `A?` ili `𝕊 A` (gde `𝕊` znači "naslednik"). Funkcije se mapiraju preko opcionih tipova:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Monadski kombinatori poput bind-a mogu se definisati:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Baferi promenljive dužine

"Baferi" su tipovi za delimično popunjene vektore:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Tip `Xᑉ⁸` razvija se u `(1 + X⁴) × ((1 + X²) × (1 + X))`. Tretiranje ovoga kao polinoma i razvijanje daje `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Tumačeno kao tip, predstavlja sumu svih mogućih torki od X dužine do 7, uključujući praznu torku. To je tačno tip listi sa dužinom strogo manjom od 8.

Kao i kod vektora, operacije mapiranja i foldovanja mogu se definisati nad baferima. Operacije steka uključuju `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` i `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` dodaje stavku u bafer, vraćajući pun vektor ako dođe do prelivanja. `pop-<n` uklanja stavku, vraćajući manji bafer i uklonjenu stavku, opciono ne vraćajući ništa ako je originalni bafer bio prazan.

Definicija `push-<n`, rekurzivno:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Sirovi Simplicity postaje težak za praćenje iznad određenih nivoa složenosti. Krajnji korisnici koriste jezike višeg nivoa poput SimplicityHL koji generišu ove idiomatske izraze.

### Zaključak

Ovo poglavlje pokazalo je kako se iz bitova grade logičke operacije. Iz njih se pojavila aritmetika na nivou bitova, omogućavajući rezonovanje o izvršavanju. Razvijeni su vektorski tipovi, pokazujući iteraciju preko višebitnih reči za definisanje aritmetike. Dalje, kriptografske operacije poput SHA-256 i validacije Schnorr potpisa mogu se definisati koristeći samo Simplicity kombinatore — sve su zaista definisane pomoću Simplicityja.

Ovo poglavlje nije sveobuhvatan vodič kroz sve moguće tipove podataka i operacije koje se mogu izgraditi u Simplicityju, ali ilustruje postizanje praktične funkcionalnosti unutar Simplicityjevih ograničenja. Uprkos konačno ograničenim tipovima, mogu se definisati korisni vektori, bafer tipovi i operacije koje iteriraju preko tih struktura.

Stvarne specifikacije operacija standardne biblioteke neznatno se razlikuju od definicija ovde. Na primer, puni sabirač koristi trostruki XOR i logičku funkciju "većine", a ne dva polusabirača.

U praksi, Simplicity programi koriste jetove za aritmetičke i kriptografske operacije. Međutim, jetovi samo zamenjuju izraze. Kombinatori koji iteriraju preko bafera i vektora ne mogu biti zamenjeni jetovima, pa se pojavljuju u stvarnim Simplicity programima. Ipak, umesto direktnog korišćenja njih, krajnji korisnici koriste jezike višeg nivoa poput SimplicityHL koji generišu takve izraze.

Rekurzivno definisani kombinatori izgledaju kao da eksponencijalno rastu po veličini izraza. To nije problematično. Tokom serijalizacije, izrazi se kodiraju kao DAG-ovi (usmereni aciklični grafovi), a ne kao stabla. Stvarna reprezentacija raste samo linearno.

Do sada su razmatrana samo čista izračunavanja. Interakcija sa podacima transakcije za zadatke poput potpisivanja transakcija zahteva neki način da programi ne uspeju ako su potpisi nevalidni. Sledeće poglavlje razmatra sporedne efekte u Simplicityju.

## Dva sporedna efekta

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

U prethodnim poglavljima pokazali smo kako izgraditi neke strukture podataka i izračunavanja koristeći jezgreni skup Simplicity kombinatora. Kao što smo primetili, jezgreni kombinatori su dovoljni za implementaciju svakog konačnog čistog izračunavanja. To otvara pitanje: šta se još može postići? Možemo dodati dodatne sporedne efekte našim izrazima.

Postoje razne vrste mogućih sporednih efekata za izraze: ažuriranje stanja, pisanje u log, bacanje izuzetka, čitanje iz okruženja, pozivanje nastavka itd. Sporedni efekti dostupni u Simplicityju zavisiće od primene.

Za Bitcoin i Liquid aplikacije trenutno imamo dva sporedna efekta: Failure efekat, koji je efekat izuzetka gde izuzetak ima tip `𝟙`, i Reader efekat, koji omogućava pristup podacima iz transakcionog okruženja. Naši jezgreni kombinatori su "čisti"; nemaju sporedne efekte. Međutim, jetovi mogu uvesti nove primitive koji imaju sporedne efekte.

### Jetovi sa efektima

Kasnije u ovom kursu govorićemo više o jetovima, ali ovde uvodimo nekoliko primera jetova da ilustrujemo njihove sporedne efekte.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` je jet za izraz koji uzima x-only javni ključ, 256-bitnu poruku i Schnorr potpis, i ne vraća ništa! Prema svom tipu, trebalo bi da se ponaša isto kao `unit`. Razlika leži u sporednom efektu jeta: ako validacija potpisa ne uspe, onda se celokupno izračunavanje prekida bacanjem izuzetka (jediničnog tipa). To je Failure efekat.

#### Verify

`verify : 𝟚 ⊢ 𝟙` je ogoljeni jet za izražavanje Failure efekta. Ako je ulaz za `verify` `false`, celokupno izračunavanje se prekida bacanjem izuzetka. Ako je ulaz `true`, ništa se ne vraća, ali izračunavanje može da se nastavi.

#### Heševi transakcije

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` izgleda kao konstantna funkcija, pošto postoji samo jedna moguća ulazna vrednost: prazna torka. Međutim, ovaj jet čita iz transakcionog okruženja i proizvodi heš podataka transakcije koji je analogan sažetku poruke `SIGHASH_ALL` koji se koristi u verifikaciji potpisa u Bitcoin Scriptu. Ovo je primer Reader efekta: vraćena vrednost zavisi od transakcionog okruženja unutar kog se jet izvršava. Postoji nekoliko drugih heširajućih jetova koji heširaju različite podskupove podataka transakcionog okruženja kako bi pomogli u izgradnji prilagođenih sažetaka poruka za potpise.

#### Jetovi introspekcije

`input-sequence : 𝟚³² ⊢ 𝟚³²?` je funkcija koja uzima indeks ulaza i vraća sequence broj transakcije za taj ulaz, opciono ne vraćajući ništa ako je indeks van granica. Ponovo, izlazna vrednost nije čista funkcija indeksa ulaza; umesto toga, operacija koristi Reader efekat da pristupi transakcionom okruženju kako bi odredila izlaznu vrednost. Postoji nekoliko drugih jetova introspekcije koji vraćaju različite fragmente podataka transakcionog okruženja.

### Klasifikovanje efekata

Nisu svi sporedni efekti isti. Neki sporedni efekti ponašaju se bolje od drugih. Efekte možemo klasifikovati prema tome koliko su podložni transformacijama programa.

#### Komutativni efekti

Komutativni efekat je onaj kod koga, ako zamenite izlaze dva izraza, možete bezbedno zameniti i same izraze bez promene efekta izraza. Razmotrite `swap = I H ▵ O H : A × B ⊢ B × A`. Ako `f ▵ g ⨾ swap = g ▵ f` za svaki izraz `f` i `g` sa sporednim efektima, onda su efekti komutativni.

Čitanje podataka transakcije iz okruženja je komutativni efekat zato što je rezultat čitanja iz okruženja isti, bez obzira kojim redom izvršavamo čitanje.

Uopšteno, bacanje izuzetka nije komutativni efekat. Ako `f` baci neki izuzetak `e₁`, a `g` baci neki drugi izuzetak `e₂`, onda koji će izuzetak biti bačen iz para `f` i `g` zavisi od redosleda kojim se izvršavaju.

Međutim, u posebnom slučaju Failure efekta, u kome se može baciti samo izuzetak jediničnog tipa, efekat je komutativan. Bez obzira koji od `f` ili `g` baci izuzetak, rezultujući izuzetak biće isti, zato što postoji samo jedna moguća vrednost izuzetka.

#### Idempotentni efekti

Idempotentni efekat je onaj kod koga, ako duplirate izlaz izraza, možete bezbedno duplirati i sam izraz bez promene efekta izraza. Razmotrite `dup = iden ▵ iden : A ⊢ A × A`. Ako `f ⨾ dup = dup ⨾ f ▵ f` za svaki `f` sa sporednim efektima, onda su efekti idempotentni.

Čitanje podataka transakcije iz okruženja je idempotentni efekat. Bacanje izuzetka je takođe idempotentni efekat. Iako će se izvršiti samo jedan od dva duplirana izraza, svaki izuzetak bačen od `dup ⨾ f ▵ f` biće isti kao izuzetak bačen od `f ⨾ dup`.

Međutim, pisanje u log možda nije idempotentno, jer bi dupliranje efekta dovelo do toga da se log poruka pojavi dva puta. Međutim, ako se log sastoji od _skupa_ poruka umesto _liste_ poruka, onda bi efekat bio idempotentan (i komutativan), zato što je ubacivanje u skup samo po sebi idempotentna operacija.

#### Jedinični efekti

Jedinični efekat je onaj kod koga, ako odbacite izlaz izraza, možete bezbedno odbaciti i sam izraz bez promene efekata izraza. Ako je uvek slučaj da `f ⨾ unit = unit` za svaki `f` sa sporednim efektima, onda su vaši efekti jedinični.

Čitanje podataka iz okruženja jedna je od retkih vrsta jediničnih efekata. Ako se rezultat čitanja podataka transakcije iz okruženja odbaci, ceo izraz koji obavlja čitanje može se odbaciti.

Failure efekat nije jediničan. Ako `f` baci izuzetak, onda će ga baciti i `f ⨾ unit`; izvršavanje čak neće ni stići do kombinatora `unit` pre nego što se izračunavanje prekine. S druge strane, `unit` očigledno ne bi bacio nikakav izuzetak, pa bi efekti `f ⨾ unit` i `unit` bili različiti.

Da rezimiramo, evo kako se gore razmatrani efekti ponašaju u odnosu na ova tri svojstva:

| Efekat | Komutativan | Idempotentan | Jediničan |
| --- | :---: | :---: | :---: |
| Reader (transakciono okruženje) | ✓ | ✓ | ✓ |
| Failure (izuzetak jediničnog tipa) | ✓ | ✓ | ✗ |
| Writer (log kao skup) | ✓ | ✓ | ✗ |
| Opšti izuzeci (proizvoljan tip) | ✗ | ✓ | ✗ |

### Efekti dozvoljeni u Simplicityju

Što tip efekta ima uređenija svojstva, to Simplicity optimizator ima više prostora za transformisanje programa koji koriste te efekte. Idealno, dozvolili bismo samo efekte koji imaju sva tri svojstva: komutativnost, idempotentnost i jediničnost. To bi optimizatoru omogućilo da izvrši bilo koju vrstu transformacije programa koju želi. Međutim, čitanje iz okruženja jedini je efekat koji zadovoljava sva tri svojstva.

Umesto toga zahtevamo da Simplicity efekti budu komutativni i idempotentni. Oba efekta koja koristimo u Simplicityju, Failure efekat i Reader efekat, komutativni su i idempotentni. To omogućava izvođenje velike klase optimizacija nad Simplicity kodom.

Međutim, gore opisana transformacija "odbacivanja", pokušaj zamene `f ⨾ unit` sa `unit`, ili bilo koja slična transformacija, nije dozvoljena ako `f` može proizvesti Failure efekat. Zaista, zamislite da `f` sadrži tvrdnju `bip0340-verify`. Bilo bi katastrofalno pokušati optimizacijom ukloniti tu proveru.

### Zašto uopšte dozvoliti sporedne efekte?

Zašto Simplicity uopšte dozvoljava sporedne efekte? Zar ne bi bilo bolje kada bi svaki program uzimao celu transakciju kao ulaz i vraćao Bulov izlaz koji odlučuje da li je transakcija validna ili nije?

#### Grupna verifikacija

Jedan razlog zašto imamo Failure efekat jeste podrška [grupnoj verifikaciji](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) Schnorr potpisa. U grupnoj verifikaciji, mnoge pojedinačne provere Schnorr potpisa udružuju se na takav način da, ako bilo koja pojedinačna provera potpisa ne uspe, onda cela grupa ne uspe.

Ovaj postupak grupisanja poboljšava efikasnost u odnosu na pojedinačno verifikovanje svakog potpisa. Mana je to što, ako grupna verifikacija ne uspe, ne saznajemo koja specifična provera ili provere potpisa nisu uspele.

Korišćenjem failure sporednog efekta, `bip0340-verify` obezbeđuje da, ako provera potpisa ne uspe, cela transakcija ne uspe. Ako bi `bip0340-verify` umesto toga vraćao `𝟚`, Bulov tip, za uspeh ili neuspeh, onda bi neuspešna provera potpisa i dalje mogla dovesti do grane u kojoj skript uspeva. U takvom slučaju morali bismo da znamo da li je konkretan potpis validan ili nije, pa ne bismo mogli da iskoristimo grupnu verifikaciju.

#### Prethodno izračunati podaci transakcije

Problem u ranom Bitcoin Scriptu bio je to što je heš funkcija korišćena za kreiranje sažetaka poruka za potpise bila linearna u odnosu na veličinu transakcije. Tipično svaki ulaz kreira bar jedan sažetak poruke za verifikaciju potpisa, pa je ukupna količina heširanja bila kvadratna u odnosu na veličinu transakcije.

Ovaj problem je rešen u Segwitu i kasnijim iteracijama Bitcoin Scripta redefinisanjem sažetaka poruka tako da se mogu izračunati u konstantnom vremenu po proveri potpisa. To se oslanja na `PrecomputedTransactionData`, koji jednom unapred izračunava heševe podataka transakcije i zatim se deli sa sighash izračunavanjima svakog ulaza. Simplicityjevi jetovi za heširanje transakcija oslanjaju se na istu vrstu prethodno izračunatih podataka transakcije kako bi obezbedili da jetovi rade u konstantnom vremenu.

Pretpostavimo da `sig-all-hash` ne koristi Reader efekat. Pretpostavimo da smo nekako uspeli da izgradimo Simplicity tip za transakciono okruženje. Nazovimo ga `TxEnv`, tako da bi `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` bio tip jeta. Takva definicija zahtevala bi da jet `sig-all-hash` može da izračuna heš bilo koje transakcije, ne samo transakcije u koju je uključen. Simplicity programi mogli bi da kopiraju dati `TxEnv` i proslede izmenjenu kopiju u `sig-all-hash`. U takvom slučaju `sig-all-hash` ne bi mogao da se osloni na `PrecomputedTransactionData`, i vratili bismo se na zahtev za linearnim vremenom u odnosu na bilo koje podatke transakcije prosleđene u ovu verziju `sig-all-hash`.

Zato što `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` koristi Reader efekat za pristup podacima transakcije, on dobija pristup _samo_ fiksnom transakcionom okruženju. Iz tog razloga, implementacija jeta može bezbedno koristiti `PrecomputedTransactionData` i raditi u konstantnom vremenu.

### Agregacija potpisa preko više ulaza

Iako ni Liquid ni Bitcoin trenutno ne podržavaju [agregaciju potpisa preko više ulaza](https://hrf.org/latest/cisa-research-paper/), želeli bismo da proverimo da Simplicity može biti kompatibilan sa njom kada za to dođe vreme.

Iako detalji nisu razrađeni, zamišljamo da se poluagregacija implementira pomoću Writer efekta. To jest, novi jet sa tipom kao što je `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` uzeo bi javni ključ, sažetak poruke i `r`-komponentu Schnorr potpisa (Schnorr potpis se sastoji od `r`-komponente i `s`-komponente) i upisao ih u transakcioni log pre nastavka izvršavanja. Zatim bi, negde drugde u transakciji ili uz transakciju, bila data agregirana `s`-komponenta za sve poluagregirane Schnorr potpise. Transakcija bi bila validna samo kada je takva agregirana `s`-komponenta data za sve zabeležene ključeve, poruke i `r`-komponente.

Da bi ispunio Simplicityjeve zahteve, ovaj Writer efekat mora biti idempotentan i komutativan. To se može obezbediti tretiranjem writer loga kao skupa torki ključ, poruka, `r`-komponenta. To funkcioniše zato što su operacije nad skupovima idempotentne i komutativne. Tretiranje loga kao skupa vrednosti bilo bi kompatibilno sa algoritmom verifikacije poluagregacije.

### Zaključak

U ovom poglavlju pogledali smo dodavanje sporednih efekata izračunavanjima koja Simplicity može da radi. Klasifikovali smo različite vrste efekata prema tome koliko su dobro ponašani u odnosu na različite vrste transformacija programa. Odlučili smo da Simplicityjeve efekte ograničimo na one koji su komutativni i idempotentni.

Dva efekta koja koristimo za Bitcoin i Liquid aplikacije jesu Reader efekat, za pristup transakcionom okruženju, i Failure efekat, za prekidanje i neuspeh programa. Neki jetovi koriste primitivne operacije u kojima se mogu pojaviti ove vrste sporednih efekata.

Failure efekat određuje izlaz Simplicity programa: program ili ne uspeva, čineći transakciju nevalidnom, ili program uspeva. Reader efekat pruža jednu vrstu ulaza Simplicity programu: okruženje koje sadrži podatke transakcije. Ali moramo obezbediti i druge ulaze, kao što su digitalni potpisi, Simplicity programima.

U sledećem poglavlju pogledaćemo šta su Simplicity programi, kako se pretvaraju u adrese i kako dodajemo druge ulaze, kao što su potpisi, Simplicity programima.

## Programi i adrese

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

U prethodnom poglavlju opisali smo dva sporedna efekta koja se koriste u Simplicityju: Failure efekat, koji određuje uspeh ili neuspeh programa, i Reader efekat, koji pruža pristup transakcionom okruženju. Sada prelazimo na praktično pitanje: šta je tačno Simplicity program i kako postaje adresa na blokčejnu?

### Simplicity programi

Simplicity program se definiše kao Simplicity izraz tipa `𝟙 ⊢ 𝟙`. Ovaj tipski potpis znači da program ne uzima smislen ulaz (samo jediničnu vrednost) i ne proizvodi smislen izlaz (samo jediničnu vrednost). Reader efekat hvata ulaz transakcionog okruženja, dok Failure efekat označava uspeh ili neuspeh. Ti efekti obrađuju U/I, a ne sami Simplicity tipovi.

### Commitment Merkle Root

Umesto čuvanja kompletnih programa on-chain, Bitcoin koristi commitments — praksu koja se proteže od Pay-to-Script-Hash (P2SH). Simplicity koristi Commitment Merkle Root (CMR).

Svaki kombinator dobija SHA-256 tag izveden iz obrasca: `Simplicity␟Commitment␟[identifier]`, gde `␟` predstavlja ASCII kod 31 (separator jedinica).

Svaki tag je SHA-256 heš odgovarajuće pre-image niske navedene ispod:

| Kombinator | Pre-image taga (ASCII niska) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Simplicity izraz se zatim rekurzivno hešira u 256-bitni CMR izračunavanjem tagovanog SHA-256 midstate-a za svaki kombinator zajedno sa CMR-ovima njegovih argumenata (pišite `#ᶜ(e)` za CMR izraza `e`, i `∥` za konkatenaciju bajtova):

| Kombinator | CMR pravilo |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Binarni kombinatori (`comp`, `pair`, `case`) konkateniraju CMR-ove oba deteta; unarni kombinatori (`take`, `drop`, `injl`, `injr`) konkateniraju CMR svog jedinog deteta nakon 32 bajta `0x00` paddinga; a nularni listovi (`iden`, `unit`) heširaju samo svoj tag. Dve konvencije čine ovo jeftinim za izračunavanje: koriste se SHA-256 midstate-ovi tako da **svaki izraz zahteva najviše jedan poziv funkcije SHA-256 kompresije** (pod pretpostavkom da je midstate do konstantnih tagova unapred izračunat), a konstruktori sa jednim argumentom prefiksuju svoj argument sa 32 bajta `0x00` paddinga, što omogućava malo dodatne predobrade implementacijama koje to žele.

Za kombinator `unit` — nularni konstruktor bez podizraza argumenata — ovo pravilo se specijalizuje u `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, gde je `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (tag se ubacuje dvaput). Rezultujući CMR za trivijalni `unit` program je:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Kritično, CMR se ne obavezuje na tipove Simplicity izraza, već se umesto toga oslanja na inferenciju tipova tokom trošenja.

### Adrese

Adrese koriste BIP-0341 Taproot mehanizam sa CMR-ovima ugrađenim pod TapLeaf verzijom `0xbe`. Proces uključuje:

1. Izračunavanje TapLeaf tagovanog heša koji kombinuje bajt verzije, dužinu CMR-a i sam CMR
2. Tweakovanje internog javnog ključa (koristeći NUMS tačku kada se ne želi putanja trošenja ključem)
3. Konvertovanje u bech32m format
4. Dodavanje odgovarajućih kontrolnih zbirova

Kada se ne želi putanja trošenja ključem, interni javni ključ postavlja se na **NUMS** ("Nothing-Up-My-Sleeve") tačku: tačku na krivoj namerno izabranu tako da niko ne zna njen diskretni logaritam — drugim rečima, tačku bez odgovarajućeg privatnog ključa. Pošto niko nikada ne može proizvesti potpis za nju, putanja trošenja ključem dokazivo je neupotrebljiva, a izlaz se može potrošiti *samo* kroz ugrađenu Simplicity skriptnu putanju. U stvarnoj aplikaciji, ovu NUMS tačku treba randomizovati kako preporučuje BIP-0341, tako da se izlazi bez putanje trošenja ključem ne razlikuju od običnih Taproot izlaza (korist za privatnost).

#### Od Simplicityja do adrese

Prođimo kroz celu derivaciju za najjednostavniji mogući program: `unit : 𝟙 ⊢ 𝟙`, no-op koji uvek uspeva.

**1. Tag kombinatora.** Prvo izračunajte `unit` tag:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Ubacite tag dvaput da dobijete CMR programa:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf heš.** Prefiksujte CMR Simplicityjevom TapLeaf verzijom `0xbe` i dužinom CMR-a `0x20` (32 bajta), zatim uzmite Elements TapLeaf tagovani heš (tagovani heš je `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Sa samo ovim jednim listom nema TapBranches, pa je ovaj heš već TapTree root.

**4. TapTweak.** Pošto ne želimo putanju trošenja ključem, koristimo BIP-0341 NUMS tačku kao interni ključ i tweakujemo je TapTree rootom:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Izlazni ključ.** Tweakujte interni ključ na krivoj, `output_pk = lift_x(internal_pk) ⊕ t·G` (aritmetika eliptičke krive je ovde sažeta), što daje x-only izlazni ključ `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Bech32m adresa.** Kodirajte x-only izlazni ključ, prefiksujte `p` (karakter SegWit v1 witness-verzije), dodajte Liquid-testnet prefiks čitljiv ljudima `tex1` i prikačite Bech32m kontrolni zbir. Konačna adresa je:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

To je bilo mnogo posla — ali veliki deo toga nameće sam Taproot, ne Simplicity.

### Witness izrazi

Novi tip kombinatora rešava odsustvo ulaza u Simplicity programe: witness izraz. Kombinator `witness` dozvoljava da se podaci potpisa i drugi witness materijal integrišu u programe.

```
      w : B
-----------------
witness w : A ⊢ B
```

Semantika witness izraza je jednostavna: on ignoriše svoj ulaz i jednostavno vraća vrednost `w` (koja može biti bilo kog Simplicity tipa), tj. `⟦witness w⟧(a) = w`. To ne dodaje **nikakvu novu izražajnost** — prema teoremi potpunosti, Simplicity već može izgraditi svaku takvu konstantnu funkciju (setite se makroa `scribe` iz prethodnih poglavlja). Poenta kombinatora `witness` leži u potpunosti u njegovom **CMR-u**: vrednost `w` je **isključena** iz CMR-a izraza, pa se adresa može izračunati pre nego što je `w` poznato, a `w` se dostavlja u vreme trošenja.

Ova dizajnerska odluka podržava orezivanje — neizvršene uslovne grane ne moraju biti otkrivene on-chain, uključujući i njihove povezane witness izraze. Kada se grana oreže, verifikatoru je potreban samo CMR orezenog podstabla, ne njegov stvarni sadržaj.

### Witness vrednosti

Može delovati kao ograničenje to što witness izraz može držati samo *vrednost*, a ne opštiji Simplicity izraz. Ali programi za UTXO blokčejnove izvršavaju se samo jednom. Nema potrebe prosleđivati ceo podizraz u witness čvor: korisnik može jednostavno sam izvršiti taj podizraz, off-chain, i prepisati njegov izlaz u witness vrednost da dobije potpuno isti rezultat.

(Kasnije u ovom kursu srešćemo kombinator `disconnect`, koji se ponaša slično witness izrazu koji *zaista* uzima ceo Simplicity izraz kao svoj argument.)

Alternativni dizajn ubacio bi sve witness podatke kao argument u Simplicity program najvišeg nivoa. Witness izrazi su poželjniji iz dva razloga. Prvo, **orezivanje**: neizvršene grane `case` izraza nikada se ne otkrivaju on-chain, a svi witness izrazi unutar tih grana orezuju se zajedno sa njima. Drugo, **lokalnost**: witness izrazi nam omogućavaju da svaku witness vrednost postavimo tačno tamo gde se koristi, umesto da je provlačimo naniže iz ulaza programa najvišeg nivoa.

### Inferencija tipova

Pošto se CMR-ovi ne obavezuju na tipove, sistem tipova se rekonstruše tokom trošenja. Simplicityjev algoritam inferencije tipova određuje minimalne tipove za svaki podizraz na osnovu strukture kombinatora. Preciznije, inferencija izračunava *glavni* (najopštiji) tip svakog podizraza; sve tipske promenljive koje ostanu slobodne zatim se instanciraju na jedinični tip `𝟙`, što daje jedinstven, minimalan tip za program.

### Zaključak

U ovom poglavlju ustanovili smo da su Simplicity programi izrazi tipa `𝟙 ⊢ 𝟙`, objasnili kako se Commitment Merkle Root-ovi konstruišu iz tagovanih SHA-256 heševa svakog kombinatora, i pokazali kako se CMR-ovi pretvaraju u on-chain adrese putem BIP-0341 Taproota. Uveli smo witness izraze kao mehanizam za pružanje podataka potpisa i drugih ulaza u vreme trošenja, bez obavezivanja na njihove vrednosti u vreme kreiranja adrese.

# Završna sekcija

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Recenzije i ocene

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Završni ispit

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Zaključak

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
