---
name: OXT - Chain Analysis
description: Savladajte osnove analize lanaca na Bitcoin
---
![cover](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai Wallet i zaplene njihovih servera 24. aprila, **veb-sajt OXT.me trenutno nije dostupan**. Međutim, moguće je da će ovaj alat biti ponovo pokrenut u narednim nedeljama. U međuvremenu, možete iskoristiti ovaj vodič da biste razumeli osnove analize lanca na Bitcoin. Sve heuristike i obrasci predstavljeni ovde ostaju primenljivi na Bitcoin transakcije. Iako su ovi alati manje optimizovani od OXT, možete privremeno koristiti [Mempool.space](https://Mempool.space/) ili [Bitcoin Explorer](https://bitcoinexplorer.org/) da biste teorijske koncepte ovog članka sproveli u praksu.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije budu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

U ovom članku ćete naučiti osnovne teorijske osnove potrebne za započinjanje osnovnih analiza lanaca na Bitcoin, i što je još važnije, kako da razumete kako oni koji vas posmatraju funkcionišu. Iako ovaj članak nije praktičan vodič za OXT alat (tema koju ćemo pokriti u budućem vodiču), on sakuplja skup ključnih znanja za njegovo korišćenje. Za svaki model, metriku i indikator koji su predstavljeni, obezbeđen je link ka primeru transakcije na OXT, što će vam omogućiti da bolje razumete njegovu upotrebu i vežbate uz vaše čitanje.


## Uvod

Jedna od funkcija novca je rešavanje problema dvostrukog podudaranja želja. U sistemu zasnovanom na trampi, završavanje Exchange zahteva ne samo pronalaženje osobe koja nudi dobar koji zadovoljava moju potrebu, već i pružanje njima dobara ekvivalentne vrednosti koja zadovoljava njihovu potrebu. Pronalaženje ove ravnoteže se pokazuje složenim. Zato pribegavamo novcu, koji nam omogućava da premestimo vrednost kako u prostoru tako i u vremenu.


Da bi novac rešio ovaj problem, neophodno je da strana koja pruža dobru ili uslugu bude uverena u svoju sposobnost da kasnije potroši taj iznos. Dakle, svaki racionalni pojedinac spreman da prihvati novac, bilo digitalni ili fizički, će se pobrinuti da ispunjava dva osnovna kriterijuma:


- Novčić mora biti netaknut i autentičan;
- i ne sme biti dvostruko potrošen.


Ako koristimo fizički novac, prva karakteristika je najkompleksnija za potvrditi. U različitim periodima istorije, integritet metalnih kovanica često je bio narušen praksama kao što su sečenje ili bušenje. Na primer, tokom antičkog Rima, bilo je uobičajeno da građani stružu ivice zlatnih kovanica kako bi prikupili malo plemenitog metala, dok su ih i dalje zadržavali za buduće transakcije. Ovo je posebno razlog zašto su kasnije žlebovi utiskivani na ivice kovanica. Autentičnost je takođe teška karakteristika za proveru na fizičkom monetarnom medijumu. Danas su tehnike za borbu protiv falsifikovanja sve složenije, primoravajući trgovce da ulažu u skupe sisteme za verifikaciju.


S druge strane, zbog svoje prirode, dvostruko trošenje nije problem za fizičke valute. Ako vam dam novčanicu od 10 €, ona neopozivo napušta moje vlasništvo da bi ušla u vaše, čime se isključuje svaka mogućnost višestrukog trošenja novčanih jedinica koje predstavlja.

Za digitalnu valutu, izazov je drugačiji. Osiguravanje autentičnosti i integriteta novčića je često jednostavnije, ali osiguravanje odsustva dvostrukog trošenja je složenije. Svako digitalno dobro je u suštini informacija. Za razliku od fizičkih dobara, informacija se ne deli tokom razmene već se širi umnožavanjem. Na primer, ako vam pošaljem dokument putem e-pošte, on se tada duplira. Na vašoj strani, ne možete sa sigurnošću potvrditi da sam izbrisao originalni dokument.


Jedini način da se izbegne ovo dupliranje digitalnog dobra je da budete svesni svih razmena u sistemu. Na ovaj način, može se znati ko šta poseduje i ažurirati račune svih na osnovu obavljenih transakcija. Ovo se radi, na primer, sa skripturnim novcem. Kada platite €10 trgovcu kreditnom karticom, banka to beleži Exchange i ažurira Ledger.


Na Bitcoin, prevencija dvostrukog trošenja se vrši na isti način. Nastoji se potvrditi odsustvo transakcije koja je već potrošila predmetne novčiće. Ako oni nikada nisu korišćeni, onda možemo biti sigurni da do dvostrukog trošenja neće doći. Ovo je čuvena fraza iz Satoshi Nakamoto u Belom Papiru: "*Jedini način da se potvrdi odsustvo transakcije je da budemo svesni svih transakcija.*"


Za razliku od bankarskog modela, na Bitcoin, ne želimo da moramo verovati centralnom entitetu. Stoga, svi korisnici moraju biti u mogućnosti da potvrde odsustvo dvostrukog trošenja, bez oslanjanja na treću stranu. Dakle, svi moraju biti upoznati sa svim Bitcoin transakcijama.


Upravo to javno širenje informacija komplikuje zaštitu privatnosti na Bitcoin. U tradicionalnom bankarskom sistemu, teoretski, samo finansijska institucija je svesna obavljenih transakcija. Međutim, na Bitcoin, svi korisnici su informisani o svim transakcijama, putem svojih odgovarajućih čvorova.


Zbog ovog ograničenja u širenju, Bitcoin model privatnosti se razlikuje od onog u bankarskom sistemu. U potonjem, transakcije su povezane sa identitetom korisnika, ali je protok informacija prekinut između pouzdane treće strane i javnosti. Drugim rečima, vaš bankar zna da svako jutro kupujete baget u lokalnoj pekari, ali vaš komšija nije svestan svih tih transakcija. U slučaju Bitcoin, pošto se protok informacija ne može prekinuti između transakcija i javne domene, model privatnosti se oslanja na odvajanje identiteta korisnika od samih transakcija.

![analysis](assets/en/1.webp)

*Dijagram inspirisan Satoshi Nakamoto-ovim u Belom Papiru: Bitcoin: Peer-to-Peer Elektronski Novčani Sistem, sekcija 10 "Privatnost".*

Pošto su Bitcoin transakcije javne, postaje moguće uspostaviti veze između njih kako bi se došlo do informacija o uključenim stranama. Ova aktivnost čak predstavlja posebnu oblast, obično nazvanu "analiza lanca". U ovom članku vas pozivam da istražite osnove analize lanca kako biste razumeli kako se vaši bitkoini prate.


Većina kompanija koje se bave analizom lanaca posluju kao crne kutije i ne otkrivaju svoje metodologije. Stoga je teško dobiti informacije o ovoj praksi. Za pisanje ovog članka, uglavnom sam se oslanjao na nekoliko dostupnih otvorenih resursa:


- Veći deo mog članka je preuzet iz serije od četiri članka pod nazivom: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), koju je proizveo Samourai Wallet 2021. godine;
- Takođe sam koristio razne izveštaje sa [OXT Research](https://medium.com/oxt-research), kao i njihov besplatni alat za analizu lanca ;
- Šire gledano, moje znanje dolazi iz različitih tvitova i sadržaja od [@LaurentMT](https://twitter.com/LaurentMT) i [@ErgoBTC](https://twitter.com/ErgoBTC);
- Takođe sam bio inspirisan [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) u kojem sam učestvovao zajedno sa [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), i [@LaurentMT](https://twitter.com/LaurentMT).


Želeo bih da zahvalim njihovim autorima, programerima i producentima. Bez njihovih različitih sadržaja i softvera, ovaj članak ne bi postojao. Takođe zahvaljujem recenzentima koji su pažljivo ispravili ovaj tekst i obogatili me svojim stručnim savetima:


- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).


*Za vašu informaciju, dodao sam tehnički miniglosar na kraju članka da definišem određene pojmove. Ako vidite reč koju ne razumete sa zvezdicom, njena definicija je na dnu stranice.*


## Šta je analiza lanca?

Analiza lanca je praksa koja obuhvata sve metode za praćenje tokova Bitcoin na Blockchain. Generalno, analiza lanca se oslanja na posmatranje karakteristika u uzorcima prethodnih transakcija. Zatim uključuje identifikaciju tih istih karakteristika u transakciji koju neko želi da analizira i izvođenje mogućih interpretacija. Ovaj metod rešavanja problema, zasnovan na praktičnom pristupu za pronalaženje dovoljno dobrog rešenja, naziva se heuristika.


Da pojednostavimo, analiza lanca se vrši u dva glavna koraka:

1. Identifikacija poznatih karakteristika;

2. Dedukcija hipoteza.


Jedan od ciljeva analize lanca je grupisanje različitih aktivnosti na Bitcoin kako bi se utvrdila jedinstvenost korisnika koji ih je izvršio. Nakon toga, biće moguće pokušati povezati ovaj skup aktivnosti sa stvarnim identitetom.


Seti se mog uvoda. Objasnio sam zašto se model privatnosti Bitcoin prvobitno oslanjao na odvajanje identiteta korisnika od njihovih transakcija. Stoga bi bilo primamljivo misliti da je analiza lanca nepotrebna, jer čak i ako neko uspe da grupiše aktivnosti On-Chain, one ne mogu biti povezane sa stvarnim identitetom. Teoretski, ova izjava je tačna. Kriptografski parovi ključeva se koriste za uspostavljanje uslova na UTXO-ima. Po svojoj suštini, ovi parovi ključeva ne otkrivaju nikakve informacije o identitetu njihovih vlasnika. Dakle, čak i ako neko uspe da grupiše aktivnosti povezane sa različitim parovima ključeva, to nam ne govori ništa o entitetu iza tih aktivnosti.


Međutim, praktična stvarnost je mnogo složenija. Postoji mnoštvo ponašanja koja rizikuju povezivanje stvarnog identiteta sa On-Chain aktivnošću. U analizi, ovo se naziva ulaznom tačkom, i postoji mnogo njih. Najčešća, naravno, je KYC (Know Your Customer). Ako povučete svoje bitkoine sa regulisane platforme na jednu od svojih ličnih adresa za primanje, onda neki ljudi mogu povezati vaš identitet sa ovim Address. Šire gledano, ulazna tačka može biti bilo koji oblik interakcije između vašeg stvarnog života i Bitcoin transakcije. Na primer, ako objavite primanje Address na svojim društvenim mrežama, to može biti ulazna tačka za analizu. Ako izvršite plaćanje u bitkoinima svom pekaru, oni mogu povezati vaše lice (koje je deo vašeg identiteta) sa Bitcoin Address.

Ove ulazne tačke su gotovo neizbežne kada se koristi Bitcoin. Iako neko može pokušati da ograniči njihov obim, one će ostati prisutne. Zato je ključno kombinovati metode usmerene na očuvanje vaše privatnosti. Dok održavanje prihvatljive razdvojenosti između vašeg stvarnog identiteta i vaših transakcija jeste pohvalan pristup, ostaje nedovoljno. Naime, ako se sve vaše aktivnosti na On-Chain mogu grupisati zajedno, onda čak i najmanja ulazna tačka može ugroziti jedinu Layer privatnosti koju ste uspostavili.


Stoga je takođe neophodno baviti se analizom lanca u našoj upotrebi Bitcoin. Na taj način možemo minimizirati agregaciju naših aktivnosti i ograničiti uticaj ulazne tačke na našu privatnost. Tačno, da bismo bolje suprotstavili analizi lanca, koji je bolji pristup od upoznavanja sa metodama koje se koriste u analizi lanca? Ako želite da znate kako da poboljšate svoju privatnost na Bitcoin, morate razumeti ove metode. Ovo će vam omogućiti da bolje shvatite tehnike poput [CoinJoin](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-samourai-Wallet-e566803d-ab3f-4d98-9136-5462009262ef) ili [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), i da smanjite greške koje biste mogli napraviti.


U tome možemo povući analogiju sa kriptografijom i kriptoanalizom. Dobar kriptograf je pre svega dobar kriptoanalitičar. Da bi se zamislio novi algoritam šifrovanja, mora se znati sa kojim napadima će se suočiti, kao i proučiti zašto su prethodni algoritmi bili razbijeni. Isti princip važi za privatnost na Bitcoin. Razumevanje metoda analize lanca je ključ za zaštitu od nje. Zato vam nudim ovaj članak.


Ključno je razumeti da analiza lanca nije egzaktna nauka. Ona se oslanja na heuristike izvedene iz prethodnih zapažanja ili logičkih interpretacija. Ova pravila omogućavaju prilično pouzdane rezultate, ali nikada sa apsolutnom preciznošću. Drugim rečima, analiza lanca uvek uključuje dimenziju verovatnoće u donetim zaključcima. Možemo proceniti sa više ili manje sigurnosti da dve adrese pripadaju istoj entitetu, ali potpuna sigurnost će uvek biti nedostižna.


Ceo cilj analize lanca leži upravo u agregaciji različitih heuristika kako bi se smanjio rizik od greške. To je, na neki način, akumulacija dokaza koja nam omogućava da se približimo stvarnosti.


Ove poznate heuristike mogu se grupisati u različite kategorije koje ćemo detaljno obraditi zajedno:


- Transakcioni obrasci (ili transakcioni modeli);
- Interna heuristika transakcije;
- Eksterni heuristici za transakciju.


Vredi napomenuti da su prve dve heuristike na Bitcoin formulisane od strane samog Satoshi Nakamota. On ih razmatra u delu 10 Belog papira. Kao što ćemo kasnije videti, zanimljivo je primetiti da ove dve heuristike i dalje zadržavaju preimućstvo u analizi lanca danas. To su:


- zajednički ulazni Ownership heuristički (CIOH);
- i ponovna upotreba Address.


Hajde da zajedno istražimo uočljive karakteristike i tumačenja koja se mogu izvesti za sprovođenje analize.


## Transakcioni obrasci (ili transakcioni modeli)

Obrazac transakcije je jednostavno tipičan model transakcije koji se može pronaći na Blockchain, čije je tumačenje verovatno poznato. Kada proučavamo obrasce, fokusiraćemo se na jednu transakciju koju ćemo analizirati na visokom nivou. Drugim rečima, gledaćemo samo broj ulaza i izlaza, bez zadržavanja na njenim specifičnijim detaljima ili njenom okruženju. Iz posmatranog modela, moći ćemo da protumačimo prirodu transakcije. Zatim ćemo tražiti karakteristike o njenoj strukturi i izvesti tumačenje.


### Jednostavno slanje (ili jednostavno plaćanje)

Ovaj model karakteriše potrošnja jednog ili više UTXO-a kao ulaza i proizvodnja dva UTXO-a kao izlaza.


![analysis](assets/en/2.webp)


Tumačenje ovog modela je da smo u prisustvu transakcije slanja ili plaćanja. Korisnik je iskoristio svoje sopstvene UTXO-e kao ulaz da bi zadovoljio u izlazu plaćanje UTXO i kusur UTXO (kusur koji se vraća istom korisniku). Stoga znamo da posmatrani korisnik verovatno više nije u posedu jednog od dva UTXO-a u izlazu (onog za plaćanje), ali je i dalje u posedu drugog UTXO (onog za kusur).


U ovom trenutku, nemoguće je za nas da preciziramo koji izlaz predstavlja koji UTXO, pošto to nije cilj ovog modela. Moći ćemo to da uradimo oslanjajući se na heuristike koje ćemo proučiti u narednom delu. U ovoj fazi, naš cilj je ograničen na identifikaciju prirode transakcije o kojoj je reč, što je, u ovom slučaju, jednostavno slanje.


Na primer, ovde je Bitcoin transakcija koja usvaja obrazac jednostavnog slanja:

### Sweep ("sweep" na engleskom)

Ovaj model karakteriše potrošnja jednog UTXO kao ulaza i proizvodnja jednog UTXO kao izlaza.


![analysis](assets/en/3.webp)


Tumačenje ovog modela je da smo u prisustvu samoprenosa. Korisnik je prebacio svoje bitkoine sebi, na drugi Address koji poseduje. Zaista, pošto nema promene u transakciji, vrlo je malo verovatno da se radi o plaćanju. Tada znamo da je posmatrani korisnik verovatno još uvek u posedu ovog UTXO.


Na primer, ovde je transakcija Bitcoin koja usvaja obrazac "sweep":

[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://Mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)


Međutim, ova vrsta obrasca može takođe otkriti samoprenos na Exchange nalog (kriptovalutna Exchange platforma). Biće to proučavanje poznatih adresa i konteksta transakcije koje će nam omogućiti da saznamo da li je to prebacivanje na samostalno čuvanje Wallet ili povlačenje na platformu.


### Konsolidacija

Ovaj model karakteriše potrošnja nekoliko UTXO-a kao ulaza i proizvodnja jednog UTXO kao izlaza.


![analysis](assets/en/4.webp)


Tumačenje ovog modela je da smo u prisustvu konsolidacije. Ovo je uobičajena praksa među korisnicima Bitcoin, sa ciljem spajanja nekoliko UTXO-a u očekivanju mogućeg povećanja transakcijskih naknada. Izvršavanjem ove operacije tokom perioda kada su naknade niske, moguće je uštedeti na budućim naknadama.


Možemo zaključiti da je korisnik iza ove transakcije verovatno bio u posedu svih UTXO-a na ulazu i da je još uvek u posedu UTXO na izlazu. Stoga, to je sigurno samoprenos.


Baš kao i "sweep", ovaj tip obrasca može takođe otkriti samoprenos na Exchange račun. Biće to proučavanje poznatih adresa i konteksta transakcije koje će nam omogućiti da saznamo da li je to konsolidacija na samostalno čuvanje Wallet ili povlačenje na platformu.


Na primer, ovde je Bitcoin transakcija koja usvaja obrazac konsolidacije:

[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://Mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)

### Model trošenja po serijama

Ovaj model karakteriše potrošnja nekoliko UTXO-a kao ulaza (često samo jednog) i proizvodnja mnogo UTXO-a kao izlaza.


![analysis](assets/en/5.webp)


Tumačenje ovog modela je da smo u prisustvu grupne potrošnje. Ovo je praksa koja verovatno otkriva značajnu ekonomsku aktivnost, kao što je Exchange, na primer. Grupna potrošnja omogućava ovim entitetima da uštede na naknadama kombinovanjem svojih izdataka u jednu transakciju.


Možemo zaključiti da ulaz UTXO dolazi od kompanije sa značajnom ekonomskom aktivnošću i da će se izlazi UTXOs raspršiti. Neki će pripadati klijentima kompanije. Drugi mogu ići ka partnerskim kompanijama. Na kraju, sigurno će biti promena koja se vraća izdavačkoj kompaniji.


Na primer, ovde je transakcija Bitcoin koja usvaja obrazac grupnog trošenja:

[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://Mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)


### Transakcije specifične za protokol

Među obrascima transakcija, možemo takođe identifikovati modele koji otkrivaju upotrebu specifičnog protokola. Na primer, Whirlpool coinjoins će imati lako prepoznatljivu strukturu koja im omogućava da se razlikuju od drugih klasičnih transakcija.


![analysis](assets/en/6.webp)


Analiza ovog obrasca sugeriše da smo verovatno u prisustvu kolaborativne transakcije. Takođe je moguće uočiti CoinJoin. Ako se ova poslednja hipoteza pokaže tačnom, tada bi broj izlaza mogao da nam pruži približnu procenu broja učesnika.


Na primer, ovde je transakcija Bitcoin koja usvaja obrazac kolaborativnog tipa transakcije CoinJoin:

[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://Mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)


Postoje mnogi drugi protokoli koji imaju svoje specifične strukture. Tako bismo mogli razlikovati transakcije tipa Wabisabi ili Stamps transakcije, na primer.


## Interna heuristika transakcija

Interna heuristika je specifična karakteristika identifikovana unutar same transakcije, bez potrebe za ispitivanjem njenog okruženja, što nam omogućava da donosimo zaključke. Za razliku od obrazaca koji se fokusiraju na celokupnu strukturu transakcije, interne heuristike se zasnivaju na skupu podataka koji se mogu izdvojiti. Ovo uključuje:


- Iznosi različitih UTXO-a, kako dolaznih tako i odlaznih;
- Sve što je povezano sa skriptama: primanje adresa, verzionisanje, vremena zaključavanja...


Generalno, ova vrsta heuristike nam omogućava da identifikujemo promenu u specifičnoj transakciji. Na taj način, možemo nastaviti da pratimo entitet kroz više različitih transakcija.


Još jednom vas podsećam da ove heuristike nisu apsolutno precizne. Posmatrane pojedinačno, omogućavaju nam samo da identifikujemo verovatne scenarije. Akumulacija nekoliko heuristika doprinosi smanjenju nesigurnosti, ali je nikada potpuno ne eliminiše.


### Unutrašnje sličnosti

Ova heuristika uključuje proučavanje sličnosti između ulaza i izlaza iste transakcije. Ako se ista karakteristika primeti na ulazima i samo na jednom od izlaza transakcije, onda je verovatno da taj izlaz predstavlja kusur.


Najočiglednija karakteristika je ponovna upotreba prijemnog Address u istoj transakciji.


![analysis](assets/en/7.webp)


Ova heuristika ostavlja malo prostora za sumnju. Osim ako njihov privatni ključ nije kompromitovan, isti primajući Address neizbežno otkriva aktivnost jednog korisnika. Interpretacija koja sledi je da je promena transakcije izlaz sa istim Address kao ulaz. Ovo nam omogućava da nastavimo praćenje pojedinca od ove promene.


Na primer, ovde je transakcija na koju se ova heuristika verovatno može primeniti:

[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://Mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)


Ove sličnosti između ulaza i izlaza ne zaustavljaju se na ponovnoj upotrebi Address. Svaka sličnost u korišćenju skripti može omogućiti primenu heuristike. Na primer, ponekad se može primetiti isto verzionisanje između ulaza i jednog od izlaza transakcije.


![analysis](assets/en/8.webp)

Na ovom dijagramu možemo videti da ulazni broj 0 otključava P2WPKH skriptu (SegWit V0 počinje sa "bc1q"). Izlazni broj 0 koristi isti tip skripte. Međutim, izlazni broj 1 koristi P2TR skriptu (SegWit V1 počinje sa "bc1p"). Interpretacija ove karakteristike je da je verovatno da je Address sa istim verzionisanjem kao ulaz promena Address. Stoga bi i dalje pripadao istom korisniku.

Evo transakcije gde se ova heuristika verovatno može primeniti:

[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://Mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)


U ovoj transakciji možemo videti da ulaz broj 0 i izlaz broj 1 koriste P2WPKH skripte (SegWit V0), dok izlaz broj 0 koristi drugačiji tip skripte, P2PKH (Legacy).


### Plaćanja Zaokruženih Iznosa

Još jedna interna heuristika koja nam može pomoći da identifikujemo promenu je ona sa okruglim brojem. Generalno, kada se suočimo sa jednostavnim obrascem plaćanja (1 ulaz i 2 izlaza), ako jedan od izlaza troši okrugli iznos, onda on predstavlja plaćanje.


![analysis](assets/en/9.webp)


Procesom eliminacije, ako jedan izlaz predstavlja uplatu, drugi predstavlja kusur. Stoga možemo interpretirati da je verovatno da korisnik u unosu i dalje poseduje izlaz koji je identifikovan kao kusur.


Treba napomenuti da ova heuristika nije uvek primenljiva, jer se većina plaćanja i dalje vrši u fiat valutama. Naime, kada trgovac u Francuskoj prihvati Bitcoin, obično ne prikazuje stabilne cene u Sats. Radije bi se odlučili za konverziju između cene u evrima i iznosa u bitkoinima koji treba platiti. Stoga, ne bi trebalo da postoji okrugli broj u izlazu transakcije. Ipak, analitičar bi mogao pokušati da izvrši ovu konverziju uzimajući u obzir Exchange kurs koji je bio na snazi kada je transakcija emitovana na mreži.


Ako jednog dana, Bitcoin postane preferirana obračunska jedinica u našim razmenama, ova heuristika bi mogla postati još korisnija za analizu.


Na primer, ovde je transakcija gde se ova heuristika verovatno može primeniti:

### Velika potrošnja


Kada se uoči dovoljno veliki razmak između dva izlaza transakcije u jednostavnom modelu plaćanja, može se proceniti da je veći izlaz verovatno kusur.


![analysis](assets/en/10.webp)


Ova heuristika najvećeg izlaza je verovatno najnepreciznija od svih. Ako se identifikuje sama po sebi, prilično je slaba. Međutim, ova karakteristika se može kombinovati sa drugim heuristikama kako bi se smanjila neizvesnost naše interpretacije.


Na primer, ako ispitamo transakciju koja sadrži izlaz sa zaokruženim iznosom i drugi izlaz sa većim iznosom, zajednička primena heuristike zaokruženih plaćanja i one koja se odnosi na najveći izlaz omogućava nam da smanjimo nivo nesigurnosti.


Na primer, ovde je transakcija na koju se ova heuristika verovatno može primeniti:

[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://Mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)


## Eksterne Heuristike za Transakciju

Proučavanje spoljašnjih heuristika je analiza sličnosti, obrazaca i karakteristika određenih Elements koji nisu svojstveni samoj transakciji. Drugim rečima, ako smo se ranije ograničavali na iskorišćavanje Elements svojstvenih transakciji sa unutrašnjim heuristikama, sada proširujemo naše polje analize na okruženje transakcije zahvaljujući spoljašnjim heuristikama.


### Address Ponovna upotreba

Ovo je jedna od najpoznatijih heuristika među Bitcoin entuzijastima. Address ponovno korišćenje omogućava uspostavljanje veze između različitih transakcija i različitih UTXO-a. Primećuje se kada se Bitcoin koji prima Address koristi više puta.


Tumačenje ponovne upotrebe Address je da svi UTXO-ovi zaključani na ovom Address pripadaju (ili su pripadali) istom entitetu. Ova heuristika ostavlja malo prostora za nesigurnost. Kada se identifikuje, tumačenje koje sledi ima veliku šansu da odgovara stvarnosti.

Kao što je objašnjeno u uvodu, ovu heuristiku je otkrio sam Satoshi Nakamoto. U Belom Papiru, on posebno pominje rešenje za sprečavanje korisnika da je proizvode, što je jednostavno korišćenje svežeg Address za svaku novu transakciju: "*Kao dodatni firewall, mogao bi se koristiti novi par ključeva za svaku transakciju kako bi ostali nepovezani sa zajedničkim vlasnikom.*"


Na primer, ovde je Address ponovo korišćen u više transakcija:

[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://Mempool.space/Address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)


### Sličnost skripti i otisaka prstiju Wallet

Pored ponovne upotrebe Address, postoje mnoge druge heuristike koje mogu povezati radnje sa istim Wallet ili sa klasterom adresa.


Prvo, analitičar može koristiti sličnosti u upotrebi skripti. Na primer, određene manjinske skripte kao što je Multisig mogu se lakše uočiti nego SegWit V0 skripte. Što je veća grupa u kojoj se skrivamo, teže nas je uočiti. Ovo je naročito razlog zašto, na CoinJoin Whirlpool protokolu, svi učesnici koriste potpuno isti tip skripte.


Šire gledano, analitičar se takođe može fokusirati na karakteristične otiske prstiju Wallet. Ovo su specifični procesi za upotrebu koje bi neko mogao pokušati da identifikuje kako bi ih iskoristio kao heuristike za praćenje. Drugim rečima, ako neko primeti akumulaciju istih unutrašnjih karakteristika na transakcijama koje se pripisuju praćenoj jedinici, može pokušati da identifikuje te iste karakteristike na drugim transakcijama.


Na primer, može se identifikovati da praćeni korisnik sistematski šalje svoju promenu na P2TR* adrese (bc1p…). Ako se ovaj proces ponavlja, može se koristiti kao heuristika za nastavak naše analize. Mogu se koristiti i drugi otisci, kao što su redosled UTXO-a, postavljanje promene u izlazima, signalizacija RBF (Replace-by-fee), ili čak broj verzije i locktime.

Kao što [@LaurentMT](https://twitter.com/LaurentMT) navodi u [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (frankofoni podcast), korisnost Wallet otisaka prstiju u analizi lanca značajno raste tokom vremena. Zaista, sve veći broj tipova skripti i sve postepenije uvođenje ovih novih funkcija od strane Wallet softvera naglašavaju razlike. Čak se dešava da se može tačno identifikovati softver koji koristi praćeni entitet. Stoga je važno razumeti da je proučavanje otiska prsta Wallet posebno relevantno za nedavne transakcije, više nego za one inicirane početkom 2010-ih.

Da rezimiramo, otisak prsta može biti bilo koja specifična praksa, izvedena automatski od strane Wallet ili ručno od strane korisnika, koja se može pronaći na drugim transakcijama kako bi pomogla u našoj analizi.


### CIOH

CIOH, za "Common Input Ownership Heuristic," što bi se moglo prevesti kao "heuristika zajedničkog Ownership ulaza" ili "heuristika zajedničkog trošenja," je heuristika koja navodi da kada transakcija ima više ulaza, oni verovatno svi dolaze od jednog entiteta. Shodno tome, njihov Ownership je zajednički.


Da bi se primenio CIOH, prvo se posmatra transakcija koja ima više ulaza. To može biti dva ulaza, kao i trideset ulaza. Kada se uoči ova karakteristika, proverava se da li transakcija ne odgovara poznatom obrascu. Na primer, ako ima 5 ulaza sa približno istim iznosom i 5 izlaza sa tačno istim iznosom, znamo da je to struktura CoinJoin Whirlpool. Stoga, CIOH se ne može primeniti.


Međutim, ako transakcija ne odgovara nijednom poznatom obrascu kolaborativne transakcije, onda se može interpretirati da svi ulazi verovatno dolaze od iste entitete. Ovo može biti veoma korisno za proširenje već poznatog klastera ili za nastavak praćenja.


![analysis](assets/en/11.webp)


CIOH je otkrio Satoshi Nakamoto. On o tome raspravlja u delu 10 Bele knjige: "*[...] veza je neizbežna kod transakcija sa više ulaza, koje nužno otkrivaju da su njihovi ulazi bili u vlasništvu istog vlasnika. Rizik je da, ako se vlasnik ključa otkrije, veze mogu otkriti druge transakcije koje su pripadale istom vlasniku.*"

Posebno je fascinantno primetiti da je Satoshi Nakamoto, čak i pre zvaničnog lansiranja Bitcoin, već identifikovao dve glavne ranjivosti privatnosti za korisnike, naime CIOH i ponovnu upotrebu Address. Takva predviđanja su prilično izuzetna, jer ove dve heuristike ostaju, čak i danas, najkorisnije u analizi lanca.


### off-chain Podaci

Očigledno, analiza lanca nije ograničena na On-Chain podatke. Bilo koji podaci iz prethodne analize ili dostupni na Internetu takođe se mogu koristiti za preciziranje analize.


Na primer, ako se primeti da se praćene transakcije sistematski emituju sa istog Bitcoin čvora i može se identifikovati njegov IP Address, moglo bi biti moguće uočiti druge transakcije od iste entitete.


Analitičar takođe ima opciju da se osloni na analize koje su prethodno postale open-source, ili na sopstvene prethodne analize. Možda neko može pronaći rezultat koji ukazuje na klaster adresa koje su već identifikovane. Ponekad je takođe moguće osloniti se na rezultate koji ukazuju na Exchange, pri čemu su adrese ovih platformi uglavnom poznate.


Slično tome, može se izvršiti analiza eliminacijom. Na primer, ako tokom analize transakcije sa dva izlaza, jedan od njih je povezan sa poznatim, ali različitim klasterom adresa od entiteta koji se prati, onda se može interpretirati da drugi izlaz verovatno predstavlja kusur.


Analiza lanca takođe uključuje deo OSINT-a (Open Source Intelligence) koji je malo više generalistički sa pretragama interneta. Zbog toga se savetuje da se adrese za primanje ne objavljuju direktno na društvenim mrežama ili na veb-sajtu, bilo pod pseudonimom ili ne.


### Temporalni modeli

Možda se ne pomisli odmah na to, ali određena ljudska ponašanja su prepoznatljiva On-Chain. Najkorisnije u studiji je vaš obrazac spavanja! Da, kada spavate, pretpostavlja se da ne emitujete Bitcoin transakcije. Pošto generalno spavate u približno isto vreme, uobičajeno je koristiti vremenske analize u On-Chain analizi. To jednostavno uključuje beleženje vremena u kojem se transakcije određene entitete emituju na Bitcoin mrežu. Analiziranje ovih vremenskih obrazaca omogućava nam da zaključimo brojne informacije.

Prvo i najvažnije, vremenska analiza ponekad može identifikovati prirodu entiteta koji se prati. Ako se primeti da se transakcije emituju dosledno tokom 24 sata, to može ukazivati na snažnu ekonomsku aktivnost. Entitet iza ovih transakcija verovatno je poslovni subjekt, potencijalno međunarodni, i možda sa automatizovanim procedurama unutar kompanije.


Na primer, prepoznao sam ovaj obrazac pre nekoliko nedelja dok sam analizirao transakciju koja je greškom dodelila 19 bitkoina u naknadama. Jednostavna vremenska analiza mi je omogućila da pretpostavim da imamo posla sa automatizovanom uslugom, i stoga verovatno velikim entitetom kao što je Exchange: https://twitter.com/Loic_Pandul/status/1701127409712452072


Zaista, nekoliko dana kasnije, otkriveno je da sredstva pripadaju PayPalu, preko Paxos Exchange.


S druge strane, ako se vidi da je vremenski obrazac prilično raspoređen na 16 specifičnih sati, onda se može proceniti da imamo posla sa individualnim korisnikom, ili možda lokalnim biznisom u zavisnosti od obima razmenjenih podataka.


Iza prirode posmatranog entiteta, vremenski obrazac nam takođe može dati približnu lokaciju korisnika. Tako možemo povezati druge transakcije i koristiti Timestamp ovih kao dodatnu heuristiku koja se može dodati našoj analizi.


Na primer, na Address koji je više puta ponovo korišćen, a koji sam prethodno pomenuo, može se primetiti da su transakcije, bilo dolazne ili odlazne, koncentrisane u intervalu od 13 sati.

![analysis](assets/notext/12.webp)

*Kredit: OXT*


Ovaj interval verovatno odgovara Evropi, Africi ili Bliskom Istoku. Stoga se može tumačiti da korisnik iza ovih transakcija živi tamo.


U drugačijem registru, to je takođe vremenska analiza ovog tipa koja je omogućila hipotezu da Satoshi Nakamoto nije delovao iz Japana, već zapravo iz Sjedinjenih Država: [https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f)


### Analiza Volumena

Još jedna eksterna heuristika koja se može koristiti je analiza obima trgovanja. Na osnovu iznosa prisutnih u svakoj transakciji pripisanoj entitetu, ove informacije se mogu koristiti kao dodatna heuristika za ostatak analize.

Ova heuristika je očigledno prilično slaba, ali može pomoći u smanjenju nesigurnosti kada se doda drugim heuristikama.


## Kako se zaštititi od analize lanca?

Kao korisnik Bitcoin, imate pravo da zaštitite svoju privatnost. Ovo proizlazi iz vaših prirodnih prava da posedujete i raspolažete sobom, koja su svojstvena svakom pojedincu, bez obzira na bilo kakva zakonodavna ograničenja.


Ovo prirodno pravo na zaštitu privatnosti takođe se pretvara u pravo-potraživanje, utvrđeno u članu 12 Univerzalne deklaracije o ljudskim pravima, koje navodi da "*Niko ne sme biti podvrgnut proizvoljnom mešanju u njegovu privatnost, porodicu, dom ili prepisku, niti napadima na njegovu čast i ugled. Svi imaju pravo na zakonsku zaštitu protiv takvog mešanja ili napada.*".


Međutim, osnovna delatnost kompanija koje se bave analizom lanaca upravo se sastoji u upadanju u vašu privatnu sferu, čime se ugrožava poverljivost vaše prepiske. Iako bi se moglo nadati da će, u skladu sa prethodno pomenutim pravom na zahtev, države energično braniti našu privatnost, ne samo da to zanemaruju, već i značajno finansiraju finansiranje ovih analitičkih kompanija. Takođe bi bilo uzaludno nadati se podršci od strane sektorskih udruženja, koja izgleda spremna da učine sve ustupke pred zakonodavcem.


De facto, this claim-right to privacy on Bitcoin does not exist. It is therefore up to you, the user, to assert your natural right and protect the confidentiality of your correspondence. This involves adopting various techniques and usage practices, which will allow you to prevent or deceive the heuristics used for chain analysis.


### Izbegavanje upadanja u heuristike

Prvo i najvažnije, pre nego što razmotrimo radikalnije metode, preporučljivo je da ograničimo našu izloženost heuristikama koje se koriste za analizu lanaca koliko god je to moguće. Kao što je ranije pomenuto, dve najmoćnije heuristike su Address ponovna upotreba i CoinJoin.


Osnovni princip za osiguranje vaše privatnosti na Bitcoin leži u korišćenju novog, čistog Address za svaku dolaznu transakciju na vaš Wallet. Ponovna upotreba Address je zaista glavna pretnja poverljivosti na Bitcoin.

Za pojedinačnog korisnika, generisanje novog Address za svaku dolaznu uplatu je veoma jednostavno. Moderni novčanici to rade automatski čim kliknete na "Primi". Dakle, ako pridajete i najmanji značaj privatnosti vaših transakcija, korišćenje novih adresa predstavlja apsolutni minimum. Ako vam ikada zatreba statična tačka kontakta na internetu, umesto da stavite primajući Address, možete koristiti rešenja [poput PayNym koja implementiraju BIP47](https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).

Dalje, ako želite da se suprotstavite analizi lanca, izbegavajte spajanje UTXO-a na ulazu transakcije. U najmanju ruku, ako zaista morate da spojite, preferirajte UTXO-e koji imaju isti izvor. Ova preporuka podrazumeva dobro upravljanje vašim UTXO-ima. Kada kupujete svoje bitkoine, preferirajte transfere koji uključuju velike iznose kako biste maksimizirali broj plaćanja koja možete izvršiti bez potrebe za spajanjem. Takođe vam savetujem da označite svoje UTXO-e u svom softveru kako biste identifikovali njihovo poreklo i izbegli spajanje iz različitih izvora.


Šire gledano, za sve ostale heuristike, morate ih poznavati kako biste pokušali da ne upadnete u njih:


- Ne koristite manjinske skripte. Preferirajte SegWit V0 ili moguće SegWit V1;
- Ne vršite uplate u okruglim iznosima. Na primer, ako treba da pošaljete 100k Sats prijatelju, pošaljite mu 114,486 Sats. Oni će vam zauzvrat kupiti piće;
- Pokušajte da uvek nemate kusur koji je mnogo veći od iznosa plaćanja;
- Nemojte objavljivati svoje adrese za primanje na društvenim mrežama;
- Koristite svoj čvor pod Tor-om da emitujete svoje transakcije;
- Pokušajte da ne emitujete uvek svoje Bitcoin transakcije u isto vreme…


### Korišćenje alata za privatnost

Takođe možete koristiti metode koje čine vašu upotrebu Bitcoin dvosmislenom kako biste sprečili ili zavarali analizu lanca.


Najpopularnija tehnika je sigurno CoinJoin, kolaborativna struktura transakcija koja mobilizuje nekoliko UTXO-a istih iznosa. Cilj ovde je razbijanje determinističkih veza, čime se sprečavaju analize od sadašnjosti ka prošlosti i od prošlosti ka sadašnjosti. CoinJoin omogućava verodostojno poricanje skrivajući vaše kovanice unutar velike grupe neprepoznatljivih kovanica. Ako želite da saznate više o CoinJoin, kako tehnički tako i praktično, predlažem da pročitate ove druge članke i tutorijale:


- [CoinJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-samourai-Wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [CoinJoin - SPARROW Wallet](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-sparrow-Wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

![analysis](assets/en/13.webp)


CoinJoin je odličan alat za stvaranje uverljive poricljivosti za novčiće, ali nije optimizovan za sve potrebe korisničke privatnosti. Konkretno, CoinJoin nije dizajniran da postane alat za plaćanje. Veoma je rigidan u pogledu iznosa koji se razmenjuju kako bi se usavršila proizvodnja uverljive poricljivosti. Pošto se ne može slobodno birati iznos transakcijskih izlaza, CoinJoin se ne može koristiti za plaćanja u bitkoinima.


Na primer, zamislite da želim da platim svoj baget u bitkoinima dok optimizujem svoju privatnost. S obzirom na nemogućnost odabira iznosa rezultujućeg UTXO iz CoinJoin, našao bih se u situaciji da ne mogu prilagoditi iznos svoje potrošnje ceni koju je postavio pekar. Stoga, CoinJoin se pokazuje kao neadekvatan za platne transakcije.


Drugi alati su osmišljeni kako bi zadovoljili potrebe privatnosti u specifičnijim slučajevima upotrebe. Na primer, imamo [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), vrstu mini-CoinJoin, koja uključuje samo dva učesnika i zasniva se na strukturi koja omogućava plaćanje.


Jedinstvenost PayJoin leži u njegovoj sposobnosti da proizvede transakciju koja izgleda obično, dok je zapravo mini-CoinJoin između dva korisnika. U ovoj strukturi, primalac transakcije učestvuje među ulazima zajedno sa stvarnim pošiljaocem. Tako primalac ubacuje uplatu sebi unutar transakcije koja omogućava stvarnu uplatu.


Na primer, ako kupite baget od svog pekara za 6,000 Sats od UTXO od 10,000 Sats, i želite da uradite PayJoin, vaš pekar će dodati UTXO od 15,000 Sats koji pripada njima kao ulaz u vašu originalnu transakciju, koji će u potpunosti povratiti kao izlaz, kako bi prevarili heuristike:


![analysis](assets/en/14.webp)


Naknade za transakcije su zanemarene kako bi se pojednostavilo razumevanje šeme.


Ciljevi PayJoin su dvostruki. Prvo, ima za cilj da prevari spoljnog posmatrača stvaranjem mamca kroz COH. Zaista, kada analitičar posmatra ovu transakciju, pomisliće da može primeniti COH, i tako pretpostaviti zajednički Ownership različitih ulaza. U stvarnosti, ova pretpostavka je netačna, jer jedan ulaz pripada pošiljaocu, dok drugi pripada primaocu. Stoga, PayJoin kvari analizu lanca vodeći analitičara pogrešnim putem.

Drugi cilj PayJoin je da prevari analitičara o stvarnom iznosu transakcije, zahvaljujući specifičnoj strukturi svojih izlaza. Tako PayJoin spada u oblast steganografije. Omogućava da se stvarni iznos transakcije sakrije unutar obmanjujuće transakcije.


Zaista, ako ponovo razmotrimo naš primer korišćenja PayJoin za kupovinu bageta, spoljašnji posmatrač bi mogao pomisliti da se bavimo uplatom od 4,000 Sats ili 21,000 Sats. U stvarnosti, uplata za baget je 6,000 Sats: 21,000 - 15,000 = 6,000. Prava vrednost uplate je stoga skrivena unutar lažne uplate koja služi kao mamac za analizu lanca.


Iza PayJoin i CoinJoin, postoje mnoge druge Bitcoin strukture transakcija koje ili blokiraju analizu lanca ili je obmanjuju. Među njima, mogao bih pomenuti [Stonewall](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) i [StonewallX2](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b) transakcije, koje omogućavaju ili pravljenje fleksibilnog mini CoinJoin ili imitaciju fleksibilnog mini CoinJoin. Tu su i [Ricochet](https://planb.network/tutorials/privacy/On-Chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) transakcije koje simuliraju promenu Ownership bitkoina pravljenjem mnoštva lažnih transfera sebi.


Svi ovi alati su dostupni na Samourai Wallet na mobilnom uređaju i Sparrow Wallet na računaru. Ako želite da saznate više o ovim specifičnim strukturama transakcija, savetujem vam da pogledate moje tutorijale:


- [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PayJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/On-Chain/PayJoin-samourai-Wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PayJoin - SPARROW Wallet](https://planb.network/tutorials/privacy/On-Chain/PayJoin-sparrow-Wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/On-Chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).


## Zaključak

Analiza lanca je praksa koja uključuje pokušaj praćenja toka bitkoina On-Chain. Da bi to uradili, analitičari traže obrasce i karakteristike kako bi izveli manje ili više plauzibilne hipoteze i interpretacije.


Tačnost ovih heuristika varira: neke pružaju viši stepen sigurnosti od drugih, ali nijedna ne može tvrditi da je nepogrešiva. Međutim, akumulacija nekoliko konvergentnih heuristika može ublažiti ovu inherentnu sumnju, iako je nemoguće potpuno je eliminisati.

Možemo kategorizovati ove metode u tri različite glavne kategorije:


- Šabloni, fokusirani na celokupnu strukturu svake transakcije;
- Interna heuristika, koja omogućava iscrpno ispitivanje svih detalja transakcije, bez proširivanja na njen kontekst;
- Eksterne heuristike, koje obuhvataju analizu transakcije u njenom okruženju, kao i sve spoljašnje podatke koji mogu pružiti uvid.


Kao korisnik Bitcoin, neophodno je savladati osnovne principe analize lanca kako biste je efikasno suzbili i time zaštitili svoju privatnost.


## Tehnički Mini-Rečnik:

**P2PKH:** akronim za Pay to Public Key Hash. To je standardni skript model koji se koristi za uspostavljanje uslova trošenja na UTXO. Omogućava zaključavanje bitkoina na Hash javnog ključa, odnosno na primajućem Address. Ovaj skript je povezan sa Legacy standardom i uveden je u prvim verzijama Bitcoin od strane Satoshi Nakamoto. Za razliku od P2PK, gde je javni ključ eksplicitno uključen u skript, P2PKH koristi kriptografski otisak javnog ključa, sa nekim metapodacima, koji se takođe naziva "primajući Address". Ovaj skript uključuje RIPEMD160 Hash SHA256 javnog ključa i propisuje da, kako bi pristupio sredstvima, primalac mora obezbediti javni ključ koji odgovara ovom Hash, kao i važeći digitalni potpis generisan iz povezanog privatnog ključa. P2PKH adrese su kodirane koristeći Base58Check format, koji im daje otpornost na tipografske greške kroz upotrebu kontrolne sume. Ove adrese uvek počinju sa brojem 1.

**P2TR:** akronim za Pay to Taproot ("plati korenu"). To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO. P2TR je uveden implementacijom Taproot u novembru 2021. Koristi Schnorr protokol za agregaciju kriptografskih ključeva, kao i Merkle stabla za alternativne skripte, poznate kao MAST (Merkelized Alternative Script Tree). Za razliku od tradicionalnih transakcija gde su uslovi trošenja javno izloženi (ponekad pri prijemu, ponekad pri trošenju), P2TR omogućava skrivanje složenih skripti iza jednog očiglednog javnog ključa. Tehnički, P2TR skripta zaključava bitkoine na jedinstveni Schnorr javni ključ, označen kao K. Međutim, ovaj K ključ je zapravo agregat javnog ključa P i javnog ključa M, pri čemu se potonji izračunava iz Merkle Root liste ScriptPubKeys. Agregacija ključeva se vrši korišćenjem Schnorr protokola potpisa. Bitkoini zaključani sa P2TR skriptom mogu se potrošiti na dva različita načina: ili objavljivanjem potpisa za javni ključ P, ili ispunjavanjem jedne od skripti sadržanih u Merkle Tree. Prva opcija se zove "put ključa", a druga "put skripte". Tako P2TR omogućava korisnicima da šalju bitkoine ili na javni ključ ili na više skripti po svom izboru. Još jedna prednost ove skripte je što, iako postoji više načina za trošenje P2TR izlaza, samo onaj koji se koristi treba da bude otkriven pri trošenju, omogućavajući da neiskorišćene alternative ostanu privatne. Na primer, zahvaljujući Schnorr agregaciji ključeva, javni ključ P može sam po sebi biti agregirani ključ, potencijalno predstavljajući Multisig. P2TR je verzija 1 SegWit izlaza, što znači da se potpisi za P2TR ulaze čuvaju u svedoku transakcije, a ne u ScriptSig. P2TR adrese koriste Bech32m kodiranje i počinju sa bc1p.

**P2WPKH:** Akronim za Pay to Witness Public Key Hash. To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO. P2WPKH je uveden implementacijom SegWit u avgustu 2017. Ova skripta je slična P2PKH (Pay to Public Key Hash), jer takođe zaključava bitkoine na osnovu Hash javnog ključa, odnosno, primajućeg Address. Razlika leži u načinu na koji se potpisi i skripte uključuju u transakciju. U slučaju P2WPKH, informacija o skripti potpisa (ScriptSig) se premješta iz tradicionalne strukture transakcije u poseban odeljak nazvan Witness. Ovo premještanje je karakteristika SegWit (Segregated Witness) ažuriranja. Ova tehnika ima prednost smanjenja veličine podataka transakcije u glavnom telu, dok zadržava neophodnu skriptu za validaciju u posebnom odeljku. Kao rezultat, P2WPKH transakcije su generalno manje skupe u smislu naknada u poređenju sa Legacy transakcijama. P2WPKH adrese su napisane koristeći Bech32 kodiranje, što doprinosi konciznijem i manje sklonom greškama pisanju zahvaljujući BCH kontrolnoj sumi. Ove adrese uvek počinju sa bc1q, što ih čini lako prepoznatljivim od Legacy primajućih adresa. P2WPKH je verzija 0 SegWit izlaza.


**UTXO:** Akronim za Neutrošeni Izlaz Transakcije. UTXO je izlaz transakcije koji još nije potrošen ili korišćen kao ulaz za novu transakciju. UTXO-i predstavljaju deo bitkoina koji korisnik poseduje i koji su trenutno dostupni za trošenje. Svaki UTXO je povezan sa specifičnim izlaznim skriptom, koji definiše neophodne uslove za trošenje bitkoina. Transakcije u Bitcoin koriste ove UTXO-e kao ulaze i kreiraju nove UTXO-e kao izlaze. Model UTXO je fundamentalni za Bitcoin, jer omogućava laku verifikaciju da transakcije ne pokušavaju da potroše bitkoine koji ne postoje ili su već potrošeni. U suštini, UTXO je deo Bitcoin.