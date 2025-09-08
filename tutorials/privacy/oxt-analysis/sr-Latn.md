---
name: OXT - Analiza lanca
description: Savladajte osnove analize lanaca na Bitcoin-u
---
![cover](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai novčanika i zaplene njihovih servera 24. aprila, **veb-sajt OXT.me trenutno nije dostupan**. Međutim, moguće je da će ovaj alat biti ponovo pokrenut u narednim nedeljama. U međuvremenu, možete iskoristiti ovaj vodič da biste razumeli osnove analize lanca na Bitcoin-u. Sve heuristike i obrasci predstavljeni ovde ostaju primenljivi na Bitcoin transakcije. Iako su ovi alati manje optimizovani od OXT, možete privremeno koristiti [Mempool.space](https://Mempool.space/) ili [Bitcoin Explorer](https://bitcoinexplorer.org/) da biste teorijske koncepte ovog članka sproveli u praksu.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

U ovom članku ćete naučiti osnovne teorijske osnove potrebne za započinjanje osnovnih analiza lanaca na Bitcoin-u, i što je još važnije, kako da razumete kako oni koji vas posmatraju funkcionišu. Iako ovaj članak nije praktičan vodič za OXT alat (tema koju ćemo pokriti u budućem vodiču), on sakuplja skup ključnih znanja za njegovo korišćenje. Za svaki model, metriku i indikator koji su predstavljeni, obezbeđen je link ka primeru transakcije na OXT, što će vam omogućiti da bolje razumete njegovu upotrebu i vežbate uz vaše čitanje.


## Uvod

Jedna od funkcija novca je rešavanje problema dvostrukog podudaranja želja. U sistemu zasnovanom na razmeni (barteru), kako bi došlo do uspešne razmene, potrebno je ne samo pronaći osobu koja nudi robu koja zadovoljava moju potrebu, već joj istovremeno ponuditi robu jednake vrednosti koja zadovoljava njenu potrebu. Pronalaženje ove ravnoteže se pokazuje složenim. Zato pribegavamo novcu, koji nam omogućava da premestimo vrednost kako u prostoru tako i u vremenu.


Da bi novac rešio ovaj problem, neophodno je da strana koja pruža dobru ili uslugu bude uverena u svoju sposobnost da kasnije potroši taj iznos. Dakle, svaki racionalni pojedinac koji je spreman da prihvati novac, bilo digitalni ili fizički, pobrinuće se da on ispunjava dva osnovna kriterijuma:


- Novčić mora biti netaknut i autentičan;
- i ne sme biti dvostruko potrošen.


Ako koristimo fizički novac, prva karakteristika je najkompleksnija za potvrditi. U različitim periodima istorije, integritet metalnih kovanica često je bio narušen praksama kao što su sečenje ili bušenje. Na primer, tokom antičkog Rima, bilo je uobičajeno da građani stružu ivice zlatnih kovanica kako bi prikupili malo plemenitog metala, dok su ih i dalje zadržavali za buduće transakcije. Ovo je posebno razlog zašto su kasnije žlebovi utiskivani na ivice kovanica. Autentičnost je takođe teška karakteristika za proveru na fizičkom monetarnom medijumu. Danas su tehnike za borbu protiv falsifikovanja sve složenije, primoravajući trgovce da ulažu u skupe sisteme za verifikaciju.


S druge strane, zbog svoje prirode, dvostruko trošenje nije problem za fizičke valute. Ako vam dam novčanicu od 10 €, ona neopozivo napušta moje vlasništvo da bi ušla u vaše, čime se isključuje svaka mogućnost višestrukog trošenja novčanih jedinica koje predstavlja.

Za digitalnu valutu, izazov je drugačiji. Osiguravanje autentičnosti i integriteta novčića je često jednostavnije, ali osiguravanje odsustva dvostrukog trošenja je složenije. Svako digitalno dobro je u suštini informacija. Za razliku od fizičkih dobara, informacija se ne deli tokom razmene već se širi umnožavanjem. Na primer, ako vam pošaljem dokument putem e-pošte, on se tada duplira. Na vašoj strani, ne možete sa sigurnošću potvrditi da sam izbrisao originalni dokument.


Jedini način da se izbegne ovo dupliranje digitalnog dobra je da budete svesni svih razmena u sistemu. Na ovaj način, može se znati ko šta poseduje i ažurirati račune svih na osnovu obavljenih transakcija. Ovo se radi, na primer, sa skripturnim novcem. Kada platite €10 trgovcu kreditnom karticom, banka beleži razmenu i ažurira svoju knjigu računa.


Na Bitcoin-u, prevencija dvostrukog trošenja se vrši na isti način. Nastoji se potvrditi odsustvo transakcije koja je već potrošila predmetne novčiće. Ako oni nikada nisu korišćeni, onda možemo biti sigurni da do dvostrukog trošenja neće doći. Ovo je čuvena fraza Satoshi Nakamoto-a u [White Paper-u](https://planb.network/resources/glossary/white-paper): "*Jedini način da se potvrdi odsustvo transakcije je da budemo svesni svih transakcija.*"


Za razliku od bankarskog modela, na Bitcoin-u, ne želimo da moramo verovati centralnom entitetu. Stoga, svi korisnici moraju biti u mogućnosti da potvrde odsustvo dvostrukog trošenja, bez oslanjanja na treću stranu. Dakle, svi moraju biti upoznati sa svim Bitcoin transakcijama.


Upravo to javno širenje informacija komplikuje zaštitu privatnosti na Bitcoin-u. U tradicionalnom bankarskom sistemu, teoretski, samo finansijska institucija je svesna obavljenih transakcija. Međutim, na Bitcoin-u, svi korisnici su informisani o svim transakcijama, putem svojih odgovarajućih čvorova.


Zbog ovog ograničenja u širenju informacija, Bitcoin model privatnosti se razlikuje od onog u bankarskom sistemu. U potonjem, transakcije su povezane sa identitetom korisnika, ali je protok informacija prekinut između pouzdane treće strane i javnosti. Drugim rečima, vaš bankar zna da svako jutro kupujete baget u lokalnoj pekari, ali vaš komšija nije svestan svih tih transakcija. U slučaju Bitcoin-a, pošto se protok informacija ne može prekinuti između transakcija i javnog domena, model privatnosti se oslanja na odvajanje identiteta korisnika od samih transakcija.

![analysis](assets/en/1.webp)

*Dijagram inspirisan Satoshi Nakamoto-ovim u White Paper-u: Bitcoin: Peer-to-Peer Elektronski Novčani Sistem, sekcija 10 "Privatnost".*

Pošto su Bitcoin transakcije javne, postaje moguće uspostaviti veze između njih kako bi se došlo do informacija o uključenim stranama. Ova aktivnost čak predstavlja posebnu oblast, obično nazvanu "analiza lanca". U ovom članku vas pozivam da istražite osnove analize lanca kako biste razumeli kako se vaši bitkoini prate.


Većina kompanija koje se bave analizom lanaca posluju kao crne kutije i ne otkrivaju svoje metodologije. Stoga je teško dobiti informacije o ovoj praksi. Za pisanje ovog članka, uglavnom sam se oslanjao na nekoliko dostupnih otvorenih resursa:


- Veći deo mog članka je preuzet iz serije od četiri članka pod nazivom: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), koju je proizveo Samourai novčanik 2021. godine;
- Takođe sam koristio razne izveštaje sa [OXT Research](https://medium.com/oxt-research), kao i njihov besplatni alat za analizu lanca ;
- Šire gledano, moje znanje dolazi iz različitih tvitova i sadržaja od [@LaurentMT](https://twitter.com/LaurentMT) i [@ErgoBTC](https://twitter.com/ErgoBTC);
- Takođe sam bio inspirisan [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) u kojem sam učestvovao zajedno sa [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), i [@LaurentMT](https://twitter.com/LaurentMT).


Želeo bih da zahvalim njihovim autorima, programerima i producentima. Bez njihovih različitih sadržaja i softvera, ovaj članak ne bi postojao. Takođe zahvaljujem recenzentima koji su pažljivo ispravili ovaj tekst i obogatili me svojim stručnim savetima:


- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).


*Za vašu informaciju, dodao sam tehnički mini rečnik na kraju članka da definišem određene pojmove. Ako vidite reč koju ne razumete sa zvezdicom, njena definicija je na dnu stranice.*


## Šta je analiza lanca?

Analiza lanca je praksa koja obuhvata sve metode za praćenje tokova Bitcoin-a na Blockchain-u. Generalno, analiza lanca se oslanja na posmatranje karakteristika u uzorcima prethodnih transakcija. Zatim uključuje identifikaciju tih istih karakteristika u transakciji koju neko želi da analizira i izvođenje mogućih interpretacija. Ovaj metod rešavanja problema, zasnovan na praktičnom pristupu za pronalaženje dovoljno dobrog rešenja, naziva se heuristika.


Da pojednostavimo, analiza lanca se vrši u dva glavna koraka:

1. Identifikacija poznatih karakteristika;

2. Dedukcija hipoteza.


Jedan od ciljeva analize lanca je grupisanje različitih aktivnosti na Bitcoin-u kako bi se utvrdila jedinstvenost korisnika koji ih je izvršio. Nakon toga, biće moguće pokušati povezati ovaj skup aktivnosti sa stvarnim identitetom.


Seti se mog uvoda. Objasnio sam zašto se model privatnosti Bitcoin-a prvobitno oslanjao na odvajanje identiteta korisnika od njihovih transakcija. Stoga bi bilo primamljivo misliti da je analiza lanca nepotrebna, jer čak i ako neko uspe da grupiše aktivnosti [On-Chain](https://planb.network/en/resources/glossary/onchain), one ne mogu biti povezane sa stvarnim identitetom. Teoretski, ova izjava je tačna. Kriptografski parovi ključeva se koriste za uspostavljanje uslova trošenja na UTXO-ima. Po svojoj suštini, ovi parovi ključeva ne otkrivaju nikakve informacije o identitetu njihovih vlasnika. Dakle, čak i ako neko uspe da grupiše aktivnosti povezane sa različitim parovima ključeva, to nam ne govori ništa o entitetu iza tih aktivnosti.


Međutim, praktična stvarnost je mnogo složenija. Postoji mnoštvo ponašanja koja rizikuju povezivanje stvarnog identiteta sa On-Chain aktivnošću. U analizi, ovo se naziva ulaznom tačkom, i postoji mnogo njih. Najčešća, naravno, je KYC (Know Your Customer). Ako povučete svoje bitkoine sa regulisane platforme na jednu od svojih ličnih adresa za primanje, onda neki ljudi mogu povezati vaš identitet sa ovom adresom. Šire gledano, ulazna tačka može biti bilo koji oblik interakcije između vašeg stvarnog života i Bitcoin transakcije. Na primer, ako objavite adresu za primanje na svojim društvenim mrežama, to može biti ulazna tačka za analizu. Ako izvršite plaćanje u bitkoinima svom pekaru, oni mogu povezati vaše lice (koje je deo vašeg identiteta) sa Bitcoin adresom.

Ove ulazne tačke su gotovo neizbežne kada se koristi Bitcoin. Iako neko može pokušati da ograniči njihov obim, one će ostati prisutne. Zato je ključno kombinovati metode usmerene na očuvanje vaše privatnosti. Dok održavanje prihvatljive razdvojenosti između vašeg stvarnog identiteta i vaših transakcija jeste pohvalan pristup, ostaje nedovoljno. Zaista, ako se sve tvoje on-chain aktivnosti mogu povezati u jednu celinu, čak i najmanja početna tačka može ugroziti jedini sloj privatnosti koji si prethodno uspostavio/la.


Stoga je takođe neophodno baviti se analizom lanca u našoj Bitcoin upotrebi. Na taj način možemo minimizirati agregaciju naših aktivnosti i ograničiti uticaj ulazne tačke na našu privatnost. Tačno, da bismo bolje suprotstavili analizi lanca, koji je bolji pristup od upoznavanja sa metodama koje se koriste u analizi lanca? Ako želite da znate kako da poboljšate svoju privatnost na Bitcoin-u, morate razumeti ove metode. Ovo će vam omogućiti da bolje shvatite tehnike poput [CoinJoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) ili [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), i da smanjite greške koje biste mogli napraviti.


U tome možemo povući analogiju sa kriptografijom i kriptoanalizom. Dobar kriptograf je pre svega dobar kriptoanalitičar. Da bi se zamislio novi algoritam šifrovanja, mora se znati sa kojim napadima će se suočiti, kao i proučiti zašto su prethodni algoritmi bili razbijeni. Isti princip važi za privatnost na Bitcoin-u. Razumevanje metoda analize lanca je ključ za zaštitu od nje. Zato vam nudim ovaj članak.


Ključno je razumeti da analiza lanca nije egzaktna nauka. Ona se oslanja na heuristike izvedene iz prethodnih zapažanja ili logičkih interpretacija. Ova pravila omogućavaju prilično pouzdane rezultate, ali nikada sa apsolutnom preciznošću. Drugim rečima, analiza lanca uvek uključuje dimenziju verovatnoće u donetim zaključcima. Možemo proceniti sa više ili manje sigurnosti da dve adrese pripadaju istom entitetu, ali potpuna sigurnost će uvek biti nedostižna.


Ceo cilj analize lanca leži upravo u agregaciji različitih heuristika kako bi se smanjio rizik od greške. To je, na neki način, akumulacija dokaza koja nam omogućava da se približimo stvarnosti.


Ove poznate heuristike mogu se grupisati u različite kategorije koje ćemo detaljno obraditi zajedno:


- Transakcioni obrasci (ili transakcioni modeli);
- Interna heuristika transakcije;
- Eksterna heuristika transakcije.


Vredi napomenuti da su prve dve heuristike na Bitcoin-u formulisane od strane samog Satoshi Nakamoto-a. On ih razmatra u delu 10 White Paper-a. Kao što ćemo kasnije videti, zanimljivo je primetiti da ove dve heuristike i dalje zadržavaju preimućstvo u analizi lanca danas. To su:


- Heuristika zajedničkog vlasništva nad ulazima, eng. Common Input Ownership Heuristic (CIOH);
- i ponovna upotreba adresa.


Hajde da zajedno istražimo uočljive karakteristike i tumačenja koja se mogu izvesti za sprovođenje analize.


## Transakcioni obrasci (ili transakcioni modeli)

Obrazac transakcije je jednostavno tipičan model transakcije koji se može pronaći na Blockchain-u, čije je tumačenje verovatno poznato. Kada proučavamo obrasce, fokusiraćemo se na jednu transakciju koju ćemo analizirati na visokom nivou. Drugim rečima, gledaćemo samo broj ulaza i izlaza, bez zadržavanja na njenim specifičnijim detaljima ili njenom okruženju. Iz posmatranog modela, moći ćemo da protumačimo prirodu transakcije. Zatim ćemo tražiti karakteristike o njenoj strukturi i izvesti tumačenje.


### Jednostavno slanje (ili jednostavno plaćanje)

Ovaj model karakteriše potrošnja jednog ili više UTXO-a kao ulaza i proizvodnja dva UTXO-a kao izlaza.


![analysis](assets/en/2.webp)


Tumačenje ovog modela je da smo u prisustvu transakcije slanja ili plaćanja. Korisnik je iskoristio svoje sopstvene UTXO-e kao ulaz kako bi u izlazu formirao jedan UTXO za plaćanje i jedan za kusur (koji se vraća istom korisniku). Stoga znamo da posmatrani korisnik verovatno više nije u posedu jednog od dva UTXO-a u izlazu (onog za plaćanje), ali je i dalje u posedu drugog UTXO (onog za kusur).


U ovom trenutku, nemoguće je za nas da preciziramo koji izlaz predstavlja koji UTXO, pošto to nije cilj ovog modela. Moći ćemo to da uradimo oslanjajući se na heuristike koje ćemo proučiti u narednom delu. U ovoj fazi, naš cilj je ograničen na identifikaciju prirode transakcije o kojoj je reč, što je, u ovom slučaju, jednostavno slanje.


Na primer, ovde je Bitcoin transakcija koja usvaja obrazac jednostavnog slanja:

### Čišćenje ("sweep" na engleskom)

Ovaj model karakteriše potrošnja jednog UTXO kao ulaza i proizvodnja jednog UTXO kao izlaza.


![analysis](assets/en/3.webp)


Tumačenje ovog modela je da smo u prisustvu samoprenosa. Korisnik je prebacio svoje bitkoine sebi, na drugu adresu koju poseduje. Zaista, pošto nema promene u transakciji, vrlo je malo verovatno da se radi o plaćanju. Tada znamo da je posmatrani korisnik verovatno još uvek u posedu ovog UTXO-a.


Na primer, ovde je transakcija Bitcoin koja usvaja obrazac "sweep":

[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://Mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)


Međutim, ovakav obrazac može takođe otkriti samoprenos sredstava na nalog na berzi kriptovaluta (platformi za razmenu kriptovaluta). Upravo će proučavanje poznatih adresa i konteksta same transakcije omogućiti da utvrdimo da li je u pitanju sweep (prebacivanje svih sredstava) ka ličnom novčaniku pod sopstvenim nadzorom (eng. self-custody wallet), ili povlačenje sredstava ka nekoj platformi.

### Konsolidacija

Ovaj model karakteriše potrošnja nekoliko UTXO-a kao ulaza i proizvodnja jednog UTXO kao izlaza.


![analysis](assets/en/4.webp)


Tumačenje ovog modela je da smo u prisustvu konsolidacije. Ovo je uobičajena praksa među korisnicima Bitcoin-a, sa ciljem spajanja nekoliko UTXO-a u očekivanju mogućeg povećanja transakcijskih naknada. Izvršavanjem ove operacije tokom perioda kada su naknade niske, moguće je uštedeti na budućim naknadama.


Možemo zaključiti da je korisnik iza ove transakcije verovatno bio u posedu svih UTXO-a na ulazu i da je još uvek u posedu UTXO na izlazu. Stoga, to je sigurno samoprenos.


Baš kao i "sweep", ovaj tip obrasca može takođe otkriti samoprenos na račun na berzi za trgovinu kriptovalutama. Slično kao i kod sweep-a, ovakav obrazac može ukazivati na samoprenos na račun na berzi. Da bismo utvrdili da li se radi o konsolidaciji u sopstveni novčanik ili o povlačenju sredstava na platformu, potrebno je analizirati poznate adrese i transakcioni kontekst.


Na primer, ovde je Bitcoin transakcija koja usvaja obrazac konsolidacije:

[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://Mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)

### Model grupnog trošenja (eng. Batch Spending Model)

Ovaj model karakteriše potrošnja nekoliko UTXO-a kao ulaza (često samo jednog) i proizvodnja mnogo UTXO-a kao izlaza.


![analysis](assets/en/5.webp)


Tumačenje ovog modela je da smo u prisustvu grupne potrošnje. Ovo je praksa koja verovatno otkriva značajnu ekonomsku aktivnost, kao što je platforma za trgovinu, na primer. Grupna potrošnja omogućava ovim entitetima da uštede na naknadama kombinovanjem svojih izdataka u jednu transakciju.


Možemo zaključiti da ulaz UTXO dolazi od kompanije sa značajnom ekonomskom aktivnošću i da će se UTXO izlazi raspršiti. Neki će pripadati klijentima kompanije. Drugi mogu ići ka partnerskim kompanijama. Na kraju, sigurno će biti kusur koji se vraća kompaniji koja je izdala transakciju.


Na primer, ovde je Bitcoin transakcija koja usvaja obrazac grupnog trošenja:

[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://Mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)


### Transakcije specifične za protokol

Među obrascima transakcija, možemo takođe identifikovati modele koji otkrivaju upotrebu specifičnog protokola. Na primer, Whirlpool coinjoins će imati lako prepoznatljivu strukturu koja im omogućava da se razlikuju od drugih klasičnih transakcija.


![analysis](assets/en/6.webp)


Analiza ovog obrasca sugeriše da smo verovatno u prisustvu kolaborativne transakcije. Takođe je moguće uočiti CoinJoin. Ako se ova poslednja hipoteza pokaže tačnom, tada bi broj izlaza mogao da nam pruži približnu procenu broja učesnika.


Na primer, ovde je Bitcoin transakcija koja usvaja obrazac kolaborativnog tipa CoinJoin transakcije:

[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://Mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)


Postoje mnogi drugi protokoli koji imaju svoje specifične strukture. Tako bismo mogli razlikovati transakcije tipa Wabisabi ili Stamps transakcije, na primer.


## Interna heuristika transakcija

Interna heuristika je specifična karakteristika identifikovana unutar same transakcije, bez potrebe za ispitivanjem njenog okruženja, što nam omogućava da donosimo zaključke. Za razliku od obrazaca koji se fokusiraju na celokupnu strukturu transakcije, interne heuristike se zasnivaju na skupu podataka koji se mogu izdvojiti. Ovo uključuje:


- Iznosi različitih UTXO-a, kako dolaznih tako i odlaznih;
- Sve što je povezano sa skriptama:  adrese za prijem, verzionisanje, vremenska zaključavanja (locktimes) i slično...


Generalno, ova vrsta heuristike nam omogućava da identifikujemo promenu u specifičnoj transakciji. Na taj način, možemo nastaviti da pratimo entitet kroz više različitih transakcija.


Još jednom vas podsećam da ove heuristike nisu apsolutno precizne. Posmatrane pojedinačno, omogućavaju nam samo da identifikujemo verovatne scenarije. Akumulacija nekoliko heuristika doprinosi smanjenju nesigurnosti, ali je nikada potpuno ne eliminiše.


### Unutrašnje sličnosti

Ova heuristika uključuje proučavanje sličnosti između ulaza i izlaza iste transakcije. Ako se ista karakteristika primeti na ulazima i samo na jednom od izlaza transakcije, onda je verovatno da taj izlaz predstavlja kusur.


Najočiglednija karakteristika je ponovna upotreba prijemne adresu u istoj transakciji.


![analysis](assets/en/7.webp)


Ova heuristika ostavlja malo prostora za sumnju. Osim ako njihov privatni ključ nije kompromitovan, ista primajuća adresa neizbežno otkriva aktivnost jednog korisnika. Interpretacija koja sledi je da je kusur transakcije izlaz sa istom adresom kao ulaz. Ovo nam omogućava da nastavimo praćenje pojedinca na osnovu ovog [kusura](https://planb.network/resources/glossary/change) (eng. change).


Na primer, ovde je transakcija na koju se ova heuristika verovatno može primeniti:

[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://Mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)


Ove sličnosti između ulaza i izlaza ne zaustavljaju se na ponovnoj upotrebi adrese. Svaka sličnost u korišćenju skripti može omogućiti primenu heuristike. Na primer, ponekad se može primetiti isto verzionisanje između ulaza i jednog od izlaza transakcije.


![analysis](assets/en/8.webp)

Na ovom dijagramu možemo videti da ulaz broj 0 otključava P2WPKH skriptu (SegWit V0 počinje sa "bc1q"). Izlaz broj 0 koristi isti tip skripte. Međutim, izlaz broj 1 koristi P2TR skriptu (SegWit V1 počinje sa "bc1p"). Interpretacija ove karakteristike je da je verovatno da je adresa sa istim verzionisanjem kao ulaz u stvari kusur adresa. Stoga bi i dalje pripadao istom korisniku.

Evo transakcije gde se ova heuristika verovatno može primeniti:

[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://Mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)


U ovoj transakciji možemo videti da ulaz broj 0 i izlaz broj 1 koriste P2WPKH skripte (SegWit V0), dok izlaz broj 0 koristi drugačiji tip skripte, P2PKH (Legacy).


### Plaćanja zaokruženih iznosa

Još jedna interna heuristika koja nam može pomoći da identifikujemo kusur je ona sa okruglim brojem. Generalno, kada se suočimo sa jednostavnim obrascem plaćanja (1 ulaz i 2 izlaza), ako jedan od izlaza troši okrugli iznos, onda on predstavlja plaćanje.


![analysis](assets/en/9.webp)


Procesom eliminacije, ako jedan izlaz predstavlja uplatu, drugi predstavlja kusur. Stoga možemo interpretirati da je verovatno da korisnik u unosu i dalje poseduje izlaz koji je identifikovan kao kusur.


Treba napomenuti da ova heuristika nije uvek primenljiva, jer se većina plaćanja i dalje vrši u fiat valutama. Naime, kada trgovac u Francuskoj prihvati Bitcoin, obično ne prikazuje stabilne cene u Sats iliti satošijima. Radije bi se odlučili za konverziju između cene u evrima i iznosa u bitkoinima koji treba platiti. Stoga, ne bi trebalo da postoji okrugli broj u izlazu transakcije. Ipak, analitičar bi mogao pokušati da izvrši ovu konverziju uzimajući u obzir kurs koji je bio na snazi u trenutku kada je transakcija emitovana na mrežu.


Ako jednog dana, Bitcoin postane preferirana obračunska jedinica u našim razmenama, ova heuristika bi mogla postati još korisnija za analizu.


Na primer, ovde je transakcija gde se ova heuristika verovatno može primeniti:

### Velika potrošnja


Kada se uoči dovoljno veliki razmak između dva izlaza transakcije u jednostavnom modelu plaćanja, može se proceniti da je veći izlaz verovatno kusur.


![analysis](assets/en/10.webp)


Ova heuristika najvećeg izlaza je verovatno najnepreciznija od svih. Ako se identifikuje sama po sebi, prilično je slaba. Međutim, ova karakteristika se može kombinovati sa drugim heuristikama kako bi se smanjila neizvesnost naše interpretacije.


Na primer, ako ispitamo transakciju koja sadrži izlaz sa zaokruženim iznosom i drugi izlaz sa većim iznosom, zajednička primena heuristike zaokruženih plaćanja i one koja se odnosi na najveći izlaz omogućava nam da smanjimo nivo nesigurnosti.


Na primer, ovde je transakcija na koju se ova heuristika verovatno može primeniti:

[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://Mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)


## Eksterne heuristike za transakciju

Proučavanje spoljašnjih heuristika je analiza sličnosti, obrazaca i karakteristika određenih elemenata koji nisu svojstveni samoj transakciji. Drugim rečima, ako smo se ranije ograničavali na iskorišćavanje elemenata svojstvenih transakciji sa unutrašnjim heuristikama, sada proširujemo naše polje analize na okruženje transakcije zahvaljujući spoljašnjim heuristikama.


### Ponovna upotreba adrese

Ovo je jedna od najpoznatijih heuristika među Bitcoin entuzijastima. Ponovo korišćenje adrese omogućava uspostavljanje veze između različitih transakcija i različitih UTXO-a. Ova pojava se primećuje kada se ista adresa za prijem Bitcoina koristi više puta.

Tumačenje ponovne upotrebe adrese je da svi UTXO-ovi zaključani na ovoj adresi pripadaju (ili su pripadali) istom entitetu. Ova heuristika ostavlja malo prostora za nesigurnost. Kada se identifikuje, tumačenje koje sledi ima veliku šansu da odgovara stvarnosti.

Kao što je objašnjeno u uvodu, ovu heuristiku je otkrio sam Satoshi Nakamoto. U White Paper-u, on posebno pominje rešenje za sprečavanje korisnika da je proizvode, što je jednostavno korišćenje sveže adrese za svaku novu transakciju: "*Kao dodatna zaštita, mogao bi se koristiti novi par ključeva za svaku transakciju kako bi ostali nepovezani sa zajedničkim vlasnikom.*"


Na primer, ovde je ponovo korišćen adresa u više transakcija:

[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://Mempool.space/Address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)


### Sličnost skripti i jedinstveni identifikatori novčanika

Pored ponovne upotrebe adrese, postoje mnoge druge heuristike koje mogu povezati radnje sa istim novčanikom ili sa klasterom adresa.


Prvo, analitičar može koristiti sličnosti u upotrebi skripti. Na primer, određene manjinske skripte kao što je Multisig mogu se lakše uočiti nego SegWit V0 skripte. Što je veća grupa u kojoj se skrivamo, teže nas je uočiti. Ovo je naročito razlog zašto, na CoinJoin Whirlpool protokolu, svi učesnici koriste potpuno isti tip skripte.


Šire gledano, analitičar se takođe može fokusirati na karakteristične identifikatore novčanika. Ovo su specifični procesi za upotrebu koje bi neko mogao pokušati da identifikuje kako bi ih iskoristio kao heuristike za praćenje. Drugim rečima, ako neko primeti akumulaciju istih unutrašnjih karakteristika na transakcijama koje se pripisuju praćenoj jedinici, može pokušati da identifikuje te iste karakteristike na drugim transakcijama.


Na primer, može se identifikovati da praćeni korisnik sistematski šalje svoju promenu na P2TR* adrese (bc1p…). Ako se ovaj proces ponavlja, može se koristiti kao heuristika za nastavak naše analize. Mogu se koristiti i drugi identifikatori, kao što su redosled UTXO-a, postavljanje promene u izlazima, signalizacija RBF (Replace-by-fee), ili čak broj verzije i locktime.

Kao što [@LaurentMT](https://twitter.com/LaurentMT) navodi u [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (frankofoni podcast), korisnost jedinstvenih identifikatora novčanika u analizi lanca značajno raste tokom vremena. Zaista, sve veći broj tipova skripti i sve postepenije uvođenje ovih novih funkcija od strane softverskih novčanika naglašavaju razlike. Čak se dešava da se može tačno identifikovati softver koji koristi praćeni entitet. Stoga je važno razumeti da je proučavanje jedinstvenih identifikatora novčanika posebno relevantno za nedavne transakcije, više nego za one inicirane početkom 2010-ih.

Da rezimiramo, jedinstveni identifikator može biti bilo koja specifična praksa, izvedena automatski od strane novčanika ili ručno od strane korisnika, koja se može pronaći na drugim transakcijama kako bi pomogla u našoj analizi.


### CIOH

CIOH, za "Common Input Ownership Heuristic," što bi se moglo prevesti kao "heuristika zajedničkog vlasništva ulaza" ili "heuristika zajedničkog trošenja," je heuristika koja navodi da kada transakcija ima više ulaza, oni verovatno svi dolaze od jednog entiteta. Shodno tome, te adrese se povezuju sa istim entitetom.

Da bi se primenio CIOH, prvo se posmatra transakcija koja ima više ulaza. To može biti dva ulaza, kao i trideset ulaza. Kada se uoči ova karakteristika, proverava se da li transakcija ne odgovara poznatom obrascu. Na primer, ako ima 5 ulaza sa približno istim iznosom i 5 izlaza sa tačno istim iznosom, znamo da je to struktura CoinJoin Whirlpool. Stoga, CIOH se ne može primeniti.


Međutim, ako transakcija ne odgovara nijednom poznatom obrascu kolaborativne transakcije, onda se može interpretirati da svi ulazi verovatno dolaze od istog entiteta. Ovo može biti veoma korisno za proširenje već poznatog klastera ili za nastavak praćenja.


![analysis](assets/en/11.webp)


CIOH je otkrio Satoshi Nakamoto. On o tome raspravlja u delu 10 White Paper-a: "*[...] veza je neizbežna kod transakcija sa više ulaza, koje nužno otkrivaju da su njihovi ulazi bili u vlasništvu istog vlasnika. Rizik je da, ako se vlasnik ključa otkrije, veze mogu otkriti druge transakcije koje su pripadale istom vlasniku.*"

Posebno je fascinantno primetiti da je Satoši Nakamoto, još pre zvaničnog pokretanja Bitcoina, već identifikovao dve glavne ranjivosti po privatnost korisnika — heuristiku zajedničkog vlasništva nad ulazima (CIOH) i ponovnu upotrebu adresa. Takva predviđanja su zaista izuzetna, jer upravo te dve heuristike i danas predstavljaju najkorisnije alate u analizi podataka na blokčejnu.


### Off-chain podaci

Očigledno, analiza lanca nije ograničena na On-Chain podatke. Bilo koji podaci iz prethodne analize ili dostupni na internetu takođe se mogu koristiti za preciziranje analize.


Na primer, ako se primeti da se praćene transakcije sistematski emituju sa istog Bitcoin čvora i može se identifikovati njegova IP adresa, moglo bi biti moguće uočiti druge transakcije od istog entiteta.


Analitičar takođe ima opciju da se osloni na analize koje su prethodno postale open-source, ili na sopstvene prethodne analize. Možda neko može pronaći rezultat koji ukazuje na klaster adresa koje su već identifikovane. Ponekad je takođe moguće osloniti se na rezultate koji ukazuju na platforme za razmenu, pri čemu su adrese ovih platformi uglavnom poznate.


Slično tome, može se izvršiti analiza eliminacijom. Na primer, ako tokom analize transakcije sa dva izlaza, jedan od njih je povezan sa poznatim, ali različitim klasterom adresa od entiteta koji se prati, onda se može interpretirati da drugi izlaz verovatno predstavlja kusur.


U okviru analize blokčejna koristi se i OSINT, odnosno prikupljanje podataka iz javno dostupnih izvora putem internetskih pretraga. Zbog toga se savetuje da se adrese za primanje ne objavljuju direktno na društvenim mrežama ili na veb-sajtu, bilo pod pseudonimom ili ne.


### Modeli zasnovani na vremenu (eng. Temporal Models)

Možda se ne pomisli odmah na to, ali određena ljudska ponašanja su prepoznatljiva On-Chain. Najkorisnije u studiji je vaš obrazac spavanja! Da, kada spavate, pretpostavlja se da ne emitujete Bitcoin transakcije. Pošto generalno spavate u približno isto vreme, uobičajeno je koristiti vremenske analize u On-Chain analizi. To jednostavno uključuje beleženje vremena u kojem se transakcije određenog entiteta emituju na Bitcoin mrežu. Analiziranje ovih vremenskih obrazaca omogućava nam da zaključimo brojne informacije.

Prvo i najvažnije, vremenska analiza ponekad može identifikovati prirodu entiteta koji se prati. Ako se primeti da se transakcije emituju dosledno tokom 24 sata, to može ukazivati na snažnu ekonomsku aktivnost. Entitet iza ovih transakcija verovatno je poslovni subjekt, potencijalno međunarodni, i možda sa automatizovanim procedurama unutar kompanije.


Na primer, prepoznao sam ovaj obrazac pre nekoliko nedelja dok sam analizirao transakciju koja je greškom dodelila 19 bitkoina u naknadama. Jednostavna vremenska analiza mi je omogućila da pretpostavim da imamo posla sa automatizovanom uslugom, i stoga verovatno velikim entitetom kao što je kripto berza: https://twitter.com/Loic_Pandul/status/1701127409712452072


Nekoliko dana kasnije ispostavilo se da su sredstva u vlasništvu PayPala, posredstvom berze Paxos.

S druge strane, ako se vidi da je vremenski obrazac prilično raspoređen na 16 specifičnih sati, onda se može proceniti da imamo posla sa individualnim korisnikom, ili možda lokalnim biznisom u zavisnosti od obima razmenjenih podataka.


Iza prirode posmatranog entiteta, vremenski obrazac nam takođe može dati približnu lokaciju korisnika. Tako možemo povezati druge transakcije i koristiti Timestamp ovih kao dodatnu heuristiku koja se može dodati našoj analizi.


Na primer, na adresu koja je više puta ponovo korišćena, a koju sam prethodno pomenuo, može se primetiti da su transakcije, bilo dolazne ili odlazne, koncentrisane u intervalu od 13 sati.

![analysis](assets/notext/12.webp)

*Kredit: OXT*


Ovaj interval verovatno odgovara Evropi, Africi ili Bliskom Istoku. Stoga se može tumačiti da korisnik iza ovih transakcija živi tamo.


U drugačijem kontekstu, upravo vremenska analiza ovog tipa omogućila je postavljanje hipoteze da Satoši Nakamoto nije delovao iz Japana, već zapravo iz Sjedinjenih Američkih Država: [https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f)


### Analiza obima

Još jedna eksterna heuristika koja se može koristiti je analiza obima trgovanja. Na osnovu iznosa prisutnih u svakoj transakciji pripisanih entitetu, ove informacije se mogu koristiti kao dodatna heuristika za ostatak analize.

Ova heuristika je očigledno prilično slaba, ali može pomoći u smanjenju nesigurnosti kada se doda drugim heuristikama.


## Kako se zaštititi od analize lanca?

Kao Bitcoin korisnik, imate pravo da zaštitite svoju privatnost. Ovo proizlazi iz vaših prirodnih prava da posedujete i raspolažete sobom, koja su svojstvena svakom pojedincu, bez obzira na bilo kakva zakonodavna ograničenja.


Ovo prirodno pravo na zaštitu privatnosti takođe se pretvara u pravo-potraživanje, utvrđeno u članu 12 Univerzalne deklaracije o ljudskim pravima, koje navodi da "*Niko ne sme biti podvrgnut proizvoljnom mešanju u njegovu privatnost, porodicu, dom ili prepisku, niti napadima na njegovu čast i ugled. Svi imaju pravo na zakonsku zaštitu protiv takvog mešanja ili napada.*".


Međutim, osnovna delatnost kompanija koje se bave analizom lanaca upravo se sastoji u upadanju u vašu privatnu sferu, čime se ugrožava poverljivost vaše prepiske. Iako bi se moglo nadati da će, u skladu sa prethodno pomenutim pravu na zaštitu, države energično braniti našu privatnost, ne samo da to zanemaruju, već i značajno finansiraju finansiranje ovih analitičkih kompanija. Bilo bi uzaludno i nadati se podršci strukovnih udruženja, koja deluju spremno da pristanu na sve ustupke pred zakonodavcem.


De fakto, ovo pravo na privatnost u okviru Bitcoina ne postoji. Stoga je na vama, korisniku, da afirmišete svoje prirodno pravo i zaštitite poverljivost svoje prepiske. To podrazumeva usvajanje različitih tehnika i načina upotrebe, koji će vam omogućiti da sprečite ili zavarate heuristike koje se koriste u analizi lanca.


### Izbegavanje upadanja u heuristike

Prvo i najvažnije, pre nego što razmotrimo radikalnije metode, preporučljivo je da ograničimo našu izloženost heuristikama koje se koriste za analizu lanaca koliko god je to moguće. Kao što je ranije pomenuto, dve najmoćnije heuristike su ponovna upotreba adresa i CoinJoin.


Osnovni princip za osiguranje vaše privatnosti na Bitcoin-u leži u korišćenju nove, čiste adrese za svaku dolaznu transakciju na vašem nov;aniku. Ponovna upotreba adrese je zaista glavna pretnja poverljivosti na Bitcoin-u.

Za pojedinačnog korisnika, generisanje nove adrese za svaku dolaznu uplatu je veoma jednostavno. Moderni novčanici to rade automatski čim kliknete na "Primi" (eng. Receive). Dakle, ako pridajete i najmanji značaj privatnosti vaših transakcija, korišćenje novih adresa predstavlja apsolutni minimum. Ako vam ikada zatreba statična tačka kontakta na internetu, umesto da stavite primajuću adresu, možete koristiti rešenja [poput PayNym koja implementiraju BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).

Dalje, ako želite da se suprotstavite analizi lanca, izbegavajte spajanje UTXO-a na ulazu transakcije. U najmanju ruku, ako zaista morate da spojite, preferirajte UTXO-e koji imaju isti izvor. Ova preporuka podrazumeva dobro upravljanje vašim UTXO-ima. Kada kupujete svoje bitkoine, preferirajte transfere koji uključuju velike iznose kako biste maksimizirali broj plaćanja koja možete izvršiti bez potrebe za spajanjem. Takođe vam savetujem da označite svoje UTXO-e u svom softveru kako biste identifikovali njihovo poreklo i izbegli spajanje iz različitih izvora.


Šire gledano, za sve ostale heuristike, morate ih poznavati kako biste pokušali da ne upadnete u njih:


- Ne koristite manjinske skripte. Preferirajte SegWit V0 ili moguće SegWit V1;
- Ne vršite uplate u okruglim iznosima. Na primer, ako treba da pošaljete 100k Sats prijatelju, pošaljite mu 114,486 Sats. Oni će vam zauzvrat kupiti piće;
- Pokušajte da uvek nemate kusur koji je mnogo veći od iznosa plaćanja;
- Nemojte objavljivati svoje adrese za primanje na društvenim mrežama;
- Koristite svoj čvor pod Tor-om da emitujete svoje transakcije;
- Pokušajte da ne emitujete uvek svoje Bitcoin transakcije u isto vreme…


### Korišćenje alata za privatnost

Takođe možete koristiti metode koje čine vašu upotrebu Bitcoin-a dvosmislenom kako biste sprečili ili zavarali analizu lanca.


Najpopularnija tehnika je sigurno CoinJoin, kolaborativna struktura transakcija koja mobilizuje nekoliko UTXO-a istih iznosa. Cilj ovde je razbijanje determinističkih veza, čime se sprečavaju analize od sadašnjosti ka prošlosti i od prošlosti ka sadašnjosti. CoinJoin omogućava verodostojno poricanje skrivajući vaše kovanice unutar velike grupe neprepoznatljivih kovanica. Ako želite da saznate više o CoinJoin, kako tehnički tako i praktično, predlažem da pročitate ove druge članke i tutorijale:


- [CoinJoin - SAMOURAI novčanik](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [CoinJoin - SPARROW novčanik](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

![analysis](assets/en/13.webp)


CoinJoin je odličan alat za stvaranje uverljive poricljivosti za novčiće, ali nije optimizovan za sve potrebe korisničke privatnosti. Konkretno, CoinJoin nije dizajniran da postane alat za plaćanje. Veoma je rigidan kada je reč o iznosima koji se razmenjuju, kako bi se postigla maksimalna verodostojnost u mogućnosti poricanja (plausible deniability). Pošto se ne može slobodno birati iznos transakcijskih izlaza, CoinJoin se ne može koristiti za plaćanja u bitkoinima.


Na primer, zamislite da želim da platim svoj baget u bitkoinima dok optimizujem svoju privatnost. S obzirom na nemogućnost odabira iznosa rezultujućeg UTXO-a iz CoinJoin-a, našao bih se u situaciji da ne mogu prilagoditi iznos svoje potrošnje ceni koju je postavio pekar. Stoga, CoinJoin se pokazuje kao neadekvatan za platne transakcije.


Drugi alati su osmišljeni kako bi zadovoljili potrebe privatnosti u specifičnijim slučajevima upotrebe. Na primer, imamo [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), vrstu mini-CoinJoin-a, koja uključuje samo dva učesnika i zasniva se na strukturi koja omogućava plaćanje.


Jedinstvenost PayJoin-a leži u njegovoj sposobnosti da proizvede transakciju koja izgleda obično, dok je zapravo mini-CoinJoin između dva korisnika. U ovoj strukturi, primalac transakcije učestvuje među ulazima zajedno sa stvarnim pošiljaocem. Tako primalac ubacuje uplatu sebi unutar transakcije koja omogućava stvarnu uplatu.


Na primer, ako kupite baget od svog pekara za 6,000 satošija koristeći UTXO od 10,000 satošija, i želite da uradite PayJoin, vaš pekar će dodati UTXO od 15,000 satošija koji pripada njima kao ulaz u vašu originalnu transakciju, koji će u potpunosti povratiti kao izlaz, kako bi prevarili heuristike:


![analysis](assets/en/14.webp)


Naknade za transakcije su zanemarene kako bi se pojednostavilo razumevanje šeme.


Ciljevi PayJoin-a su dvostruki. Prvo, ima za cilj da prevari spoljnog posmatrača stvaranjem mamca kroz COH. Zaista, kada analitičar posmatra ovu transakciju, pomisliće da može primeniti COH, i tako pretpostaviti zajedničko vlasništvo nad različitim ulazima. U stvarnosti, ova pretpostavka je netačna, jer jedan ulaz pripada pošiljaocu, dok drugi pripada primaocu. Stoga, PayJoin kvari analizu lanca vodeći analitičara pogrešnim putem.

Drugi cilj PayJoin-a je da prevari analitičara o stvarnom iznosu transakcije, zahvaljujući specifičnoj strukturi svojih izlaza. Tako PayJoin spada u oblast steganografije. Omogućava da se stvarni iznos transakcije sakrije unutar obmanjujuće transakcije.


Zaista, ako ponovo razmotrimo naš primer korišćenja PayJoin-a za kupovinu bageta, spoljašnji posmatrač bi mogao pomisliti da se bavimo uplatom od 4,000 satošija ili 21,000 satošija. U stvarnosti, uplata za baget je 6,000 satošija: 21,000 - 15,000 = 6,000. Prava vrednost uplate je stoga skrivena unutar lažne uplate koja služi kao mamac za analizu lanca.


Iza PayJoin-a i CoinJoin-a, postoje mnoge druge Bitcoin strukture transakcija koje ili blokiraju analizu lanca ili je obmanjuju. Među njima, mogao bih pomenuti [Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) i [StonewallX2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b) transakcije, koje omogućavaju ili pravljenje fleksibilnog mini CoinJoin-a ili imitaciju fleksibilnog mini CoinJoin-a. Tu su i [Ricochet](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) transakcije koje simuliraju promenu vlasništva nad bitkoinima pravljenjem mnoštva lažnih transfera sebi.


Svi ovi alati su dostupni na Samourai novčaniku na mobilnom uređaju i Sparrow novčaniku na računaru. Ako želite da saznate više o ovim specifičnim strukturama transakcija, savetujem vam da pogledate moje tutorijale:


- [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PayJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PayJoin - SPARROW Wallet](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).


## Zaključak

Analiza lanca je praksa koja uključuje pokušaj praćenja toka bitkoina na on-chain-u. Da bi to uradili, analitičari traže obrasce i karakteristike kako bi izveli manje ili više verovatne hipoteze i interpretacije.


Tačnost ovih heuristika varira: neke pružaju viši stepen sigurnosti od drugih, ali nijedna ne može tvrditi da je nepogrešiva. Međutim, akumulacija nekoliko konvergentnih heuristika može ublažiti ovu inherentnu sumnju, iako je nemoguće potpuno je eliminisati.

Možemo kategorizovati ove metode u tri različite glavne kategorije:


- Šabloni, fokusirani na celokupnu strukturu svake transakcije;
- Interna heuristika, koja omogućava iscrpno ispitivanje svih detalja transakcije, bez proširivanja na njen kontekst;
- Eksterne heuristike, koje obuhvataju analizu transakcije u njenom okruženju, kao i sve spoljašnje podatke koji mogu pružiti uvid.


Kao Bitcoin korisnik, neophodno je savladati osnovne principe analize lanca kako biste je efikasno suzbili i time zaštitili svoju privatnost.


## Tehnički Mini-Rečnik:

**P2PKH:** akronim za Pay to Public Key Hash. To je standardni skript model koji se koristi za uspostavljanje uslova trošenja nad UTXO-em. Omogućava zaključavanje bitkoina na heš javnog ključa, odnosno na primajućoj adresi. Ovaj skript je povezan sa Legacy standardom i uveden je u prvim verzijama Bitcoin-a od strane Satoshi Nakamoto-a. Za razliku od P2PK, gde je javni ključ eksplicitno uključen u skript, P2PKH koristi kriptografski otisak javnog ključa, sa nekim metapodacima, koji se takođe naziva "primajuća adresa". Ovaj skript uključuje RIPEMD160 Hash SHA256 javnog ključa i propisuje da, kako bi pristupio sredstvima, primalac mora obezbediti javni ključ koji odgovara ovom hešu, kao i važeći digitalni potpis generisan iz povezanog privatnog ključa. P2PKH adrese su kodirane koristeći Base58Check format, koji im daje otpornost na tipografske greške kroz upotrebu kontrolne sume. Ove adrese uvek počinju sa brojem 1.

**P2TR:** akronim za Pay to Taproot ("plati korenu"). To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO-u. P2TR je uveden implementacijom Taproot-a u novembru 2021. Koristi Schnorr protokol za agregaciju kriptografskih ključeva, kao i Merkle stabla za alternativne skripte, poznate kao MAST (Merkelized Alternative Script Tree). Za razliku od tradicionalnih transakcija gde su uslovi trošenja javno izloženi (ponekad pri prijemu, ponekad pri trošenju), P2TR omogućava skrivanje složenih skripti iza jednog očiglednog javnog ključa. Tehnički, P2TR skripta zaključava bitkoine na jedinstveni Schnorr javni ključ, označen kao K. Međutim, ovaj K ključ je zapravo agregat javnog ključa P i javnog ključa M, pri čemu se potonji izračunava iz Merkle Root liste ScriptPubKeys. Agregacija ključeva se vrši korišćenjem Schnorr protokola potpisa. Bitkoini zaključani sa P2TR skriptom mogu se potrošiti na dva različita načina: ili objavljivanjem potpisa za javni ključ P, ili ispunjavanjem jedne od skripti sadržanih u Merkle Tree. Prva opcija se zove "put ključa", a druga "put skripte". Tako P2TR omogućava korisnicima da šalju bitkoine ili na javni ključ ili na više skripti po svom izboru. Još jedna prednost ove skripte je što, iako postoji više načina za trošenje P2TR izlaza, samo onaj koji se koristi treba da bude otkriven pri trošenju, omogućavajući da neiskorišćene alternative ostanu privatne. Na primer, zahvaljujući Schnorr agregaciji ključeva, javni ključ P može sam po sebi biti agregirani ključ, potencijalno predstavljajući Multisig. P2TR je verzija 1 SegWit izlaza, što znači da se potpisi za P2TR ulaze čuvaju u svedoku transakcije, a ne u ScriptSig. P2TR adrese koriste Bech32m kodiranje i počinju sa bc1p.

**P2WPKH:** Akronim za Pay to Witness Public Key Hash. To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO. P2WPKH je uveden implementacijom SegWit u avgustu 2017. Ova skripta je slična P2PKH (Pay to Public Key Hash), jer takođe zaključava bitkoine na osnovu heša javnog ključa, odnosno, na primajućoj adresi. Razlika leži u načinu na koji se potpisi i skripte uključuju u transakciju. U slučaju P2WPKH, informacija o skripti potpisa (ScriptSig) se premješta iz tradicionalne strukture transakcije u poseban odeljak nazvan Witness. Ovo premještanje je karakteristika SegWit (Segregated Witness) ažuriranja. Ova tehnika ima prednost smanjenja veličine podataka transakcije u glavnom delu, dok zadržava neophodnu skriptu za validaciju u posebnom odeljku. Kao rezultat, P2WPKH transakcije su generalno manje skupe u smislu naknada u poređenju sa Legacy transakcijama. P2WPKH adrese su napisane koristeći Bech32 kodiranje, što doprinosi konciznijem i manje sklonom greškama pisanju zahvaljujući BCH kontrolnoj sumi. Ove adrese uvek počinju sa bc1q, što ih čini lako prepoznatljivim od Legacy primajućih adresa. P2WPKH je verzija 0 SegWit izlaza.


**UTXO:** Akronim za Neutrošeni Izlaz Transakcije. UTXO je izlaz transakcije koji još nije potrošen ili korišćen kao ulaz za novu transakciju. UTXO-i predstavljaju deo bitkoina koji korisnik poseduje i koji su trenutno dostupni za trošenje. Svaki UTXO je povezan sa specifičnim izlaznim skriptom, koji definiše neophodne uslove za trošenje bitkoina. Transakcije u Bitcoin-u koriste ove UTXO-e kao ulaze i kreiraju nove UTXO-e kao izlaze. Model UTXO-a je fundamentalni za Bitcoin, jer omogućava laku verifikaciju da transakcije ne pokušavaju da potroše bitkoine koji ne postoje ili su već potrošeni. U suštini, UTXO je deo bitcoina.
