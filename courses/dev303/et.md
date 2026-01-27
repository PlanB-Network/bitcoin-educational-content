---
name: Rust õppimine koos Bitcoin-ga
goal: Rust arendusoskuste arendamine Bitcoin kodeerimise abil
objectives: 

  - Rust keelega harjumine
  - Mõista, miks kasutada Rust Bitcoin arendamiseks
  - Hankige Lightning SDK alus

---

# Rust ekspeditsioon Bitcoin ehitajatele



Sellel praktilisel kursusel, mis on filmitud Fulgur' Ventures'i poolt oktoobris 2023 korraldatud seminaril, arendate Rust oskusi, ehitades tõelisi Bitcoin-le keskenduvaid komponente ja miniprojekte. Käsitleme Rust põhialuseid, miks Rust kasutatakse Bitcoin arendamiseks (mälu turvalisus, jõudlus ja turvaline samaaegsus) ning kuidas alustada Lightning SDKga maksefunktsioonide ehitamist.


Kõikides peatükkides harjutate Rust põhilisi mustreid (omand, eluead, tunnused, asünkroonika), töötate Bitcoin primitiividega (võtmed, tehingud, skriptid) ja integreerite järk-järgult Lightning'i kontseptsioone (sõlmed, kanalid, arved).


Eelnev Rust või Bitcoin arendus ei ole tingimata vajalik, kuigi programmeerimise algtasemete tundmine on abiks. Kursus on algaja-sõbralik, kuid samas piisavalt praktiline Bitcoin-ga alustavatele inseneridele.


+++

# Sissejuhatus

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Kursuse ülevaade

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Esitlus**


Tere tulemast sellele SDKde algajaile mõeldud programmeerimiskursusele. Sellel koolitusel õpite Rust põhitõdesid, seejärel keskendute Rust-le, mida rakendatakse Bitcoin programmeerimisel, ja lõpetate mõne kasutusjuhuga SDK-de abil.


Koolituse videod on esialgu kättesaadavad ainult inglise keeles ja see oli osa Fulgure Venture poolt eelmise aasta oktoobris Toscanas korraldatud live-seminarist. See koolitus keskendub ainult esimesele nädalale. Teine pool oli suunatud RGB-le ja on leitav RGB kursusest.


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

See koolitus annab teile võimaluse arendada oma programmeerimisoskusi Lightning Network-l, kasutades Rust ja erinevaid SDK-sid. See on mõeldud kindla programmeerimisoskusega arendajatele, kes soovivad sukelduda Lightning Network-spetsiifilisse arendusse. Te saate teada Rust põhitõdesid, miks see sobib Bitcoin arendamiseks, ning seejärel liigute edasi praktilise rakendamise juurde, kasutades spetsiaalseid SDK-sid.


**Rubriik 2: Õppige Rust** abil koodima

Selles jaotises tutvustame teile Rust põhialuseid mitme järjestikuse peatüki kaudu. Seitsme üksikasjaliku osa jooksul õpite Rust koodi kirjutama, mõistate selle eripärasid ja omandate selle põhifunktsioone. See moodul on hädavajalik, et mõista, miks Rust on Bitcoin arendamiseks eelistatud keel.


**Jagu 3: Rust ja Bitcoin**

Siinkohal uurime põhjalikult, miks Rust on asjakohane valik Bitcoin arendamiseks. Saate teada selle veamudelist, UniFFI-vahendist ja asünkroonsetest omadustest - kõik need on olulised elemendid töökindla ja turvalise tarkvara loomisel.


**Jagu 4: LNP/BP arendamine SDKdega**

Te saate teada, kuidas arendada LN sõlmi, kasutades erinevaid SDK-sid, nagu Breez SDK ja Greenlight for Lipa. Sa näed, kuidas rakendada Lightning Network rakendusi, kasutades Bitcoin ja Lightning arenduse lihtsustamiseks mõeldud raamatukogusid.


Kas olete valmis Lightning Network oskusi Rust abil arendama? Läheme!

# Õppige rooste raamatuga koodi kirjutama

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Rust tutvustus

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Rust paigaldamine ja haldamine Rustupiga


Kui alustate oma teekonda Rust-ga, siis esimene samm on korraliku arenduskeskkonna loomine. Kõige enam soovitatakse Rust paigaldamist Rustup'i kaudu, mis on tööriistaketi haldussüsteem, mis tegeleb paigaldamise ja uuendustega erinevates projektides ja platvormidel.


Rustup on midagi enamat kui lihtsalt paigaldaja - see toimib teie Rust arenduskeskkonna tervikliku haldusvahendina. Rustupiga saate hõlpsasti paigaldada täiendavaid kompileerimisihte erinevate platvormide jaoks, näiteks ARM64 Android'i arendamiseks või muude arhitektuuride jaoks, mida teil võib olla vaja toetada. Tööriist käsitseb ka Rust uuendusi sujuvalt, mis on eriti väärtuslik, arvestades, et Rust annab uue stabiilse versiooni välja umbes iga kuue nädala tagant. Kui teil on vaja uuendada viimasele versioonile, siis lihtne käsk `rustup update` tegeleb kõigega automaatselt.


Rustupi paigaldamisel tasub mõista sellega seotud turvamudelit. Paigaldusprotsess laeb alla ja täidab skripti ametlikust Rust veebisaidist HTTPS-i kaudu, mis tagab transpordikihi krüptoturbe. Rustupi ja Cargo poolt alla laaditavad paketid pärinevad usaldusväärsetest allikatest (crates.io ja ametlik Rust infrastruktuur) ja kasutavad HTTPS-krüpteerimist. Kuigi see lähenemisviis on turvaline enamiku arendusstsenaariumide puhul, võivad mõned rangete turvapoliitikatega organisatsioonid eelistada Rust installimist oma Linuxi distributsiooni paketihalduri kaudu, mis pakub täiendavat usalduskihti distributsiooni enda pakettide allkirjastamise infrastruktuuri kaudu. Õppimiseks ja üldiseks arendamiseks on Rustup hästi tõestatud ja laialdaselt usaldusväärne vahend Rust ökosüsteemis.


Enamiku arendusstsenaariumide puhul saate Rustupi paigaldada, käivitades ametlikul Rust veebisaidil pakutava paigaldusskripti. Paigaldaja palub teil valida erinevate tööriistakomplektide vahel, kusjuures enamikele kasutajatele on soovitatav valida stabiilne tööriistakomplekt. Paigaldamine toimub teie kodukataloogi, ei nõua administraatori õigusi ja seab kõik vajalikud keskkonnamuutujad koheseks kasutamiseks.


### Rust tööriistakettide ja komponentide mõistmine


Rust arendusökosüsteem koosneb mitmest võtmekomponendist, mis töötavad koos, et pakkuda täielikku programmeerimiskeskkonda. Nende komponentide mõistmine aitab teRust arendusprotsessis tõhusamalt navigeerida ja tekkinud probleemide korral neid lahendada.


Rust kompilaator, tuntud kui `rustc`, moodustab Rust tööriistakomplekti tuuma. Kuigi teoreetiliselt võiksite Rust programmide kompileerimiseks kasutada `rustc` otse, sõltub enamik arendustöödest Cargo, Rust paketihalduri ja build-süsteemi abil. Cargo toimib sarnaselt npmiga JavaScript'i ökosüsteemis, hallates sõltuvusi, koordineerides koostamist ja pakkudes mugavaid käske tavaliste arendusülesannete jaoks. Kui käivitate käske nagu `cargo build` või `cargo run`, siis Cargo korraldab kompileerimisprotsessi, tegeleb sõltuvuste lahendamisega ja haldab üldist projekti struktuuri.


Clippy on linter, mis analüüsib teie koodi ja teeb parandusettepanekuid. Erinevalt tavalistest süntaksikontrollijatest mõistab Clippy Rust idioome ja võib soovitada idiomaatilisemaid viise konkreetsete ülesannete täitmiseks. See tööriist aitab õppida Rust parimaid tavasid ja kirjutada paremini hooldatavat koodi.


Rust tööriistakomplekt sisaldab ka põhjalikke dokumenteerimisvahendeid ja standardset raamatukogu dokumentatsiooni, mis on kättesaadav ametliku Rust dokumentatsiooni veebisaidi kaudu. See dokumentatsioon on arenduse ajal asendamatu viide, mis annab üksikasjalikku teavet standardraamatukogu funktsioonide, tüüpide ja moodulite kohta. Dokumentatsioon sisaldab ulatuslikke näiteid ja selgitusi, mis aitavad teil mõista mitte ainult seda, mida funktsioonid teevad, vaid ka seda, kuidas neid oma programmides tõhusalt kasutada.


Rust toetab mitmeid versioonikanaleid: stabiilne, beetaversioon ja öine versioon. Stabiilne kanal pakub põhjalikult testitud versioone, mis sobivad tootmiskasutuseks. Beeta-kanal pakub järgmise stabiilse väljaande eelvaadet, mida kasutatakse peamiselt lõplikuks testimiseks enne ametlikku väljaannet. Öine kanal sisaldab aktiivses arenduses olevaid eksperimentaalseid funktsioone, mis võivad olla kasulikud Rust uute võimaluste proovimiseks, kuigi need funktsioonid võivad muutuda või tulevastes versioonides eemaldatud olla.


### Rust projektide loomine ja haldamine Cargo abil


Kaasaegse Rust arenduse keskmes on Cargo, mis lihtsustab projektide loomist, sõltuvuste haldamist ja koostamisprotsessi. Selle asemel, et käsitsi luua katalooge ja faile, pakub Cargo käsku `cargo new`, et luua generate täielik projektistruktuur koos mõistlike vaikeväärtustega.


Kui loote uue projekti käsuga `cargo new project_name`, loob Cargo standardse kataloogistruktuuri, loob põhifaili `main.rs` koos programmiga "Hello, world!", initsialiseerib Git-repositooriumi ja genereerib projekti konfiguratsiooni jaoks faili `Cargo.toml`. Fail `Cargo.toml` on teie projekti keskne konfiguratsioonipunkt, mis sisaldab metaandmeid teie projekti kohta ja loetleb kõik sõltuvused, mida teie kood vajab.


Cargo pakub mitmeid olulisi käske igapäevaseks arendustegevuseks. Käsk `cargo build` kompileerib teie projekti ja selle sõltuvused, luues käivitatavad failid kataloogis `target`. Kiireks iteratsiooniks arenduse ajal ühendab käsk `cargo run` ehitamise ja täitmise üheks sammuks. Käsk `cargo check` teostab kõik kompileerimise kontrollid ilma lõpliku käivitatava faili loomiseta, mis teeb selle oluliselt kiiremaks kui täieliku buildi, kui soovite lihtsalt kontrollida, kas teie kood on õigesti kompileeritud.


Kui valmistate koodi ette tootearenduse jaoks, võimaldab lipp `--release` optimeerimist ja eemaldab vigade kõrvaldamise kinnitused. Release build'id töötavad kiiremini ja toodavad väiksemaid käivitatavaid programme, kuid nende kompileerimine võtab kauem aega ja nad eemaldavad kasulikku silumisalast teavet. Kompilaator rakendab mitmesuguseid optimeerimisi release-koostude ajal ja lülitab välja jooksuaegsed kontrollid, nagu täisarvu ülevoolu tuvastamine, mis parandab jõudlust, kuid eemaldab mõned debug-komplektides esinevad turvagarantiid.


### Muutujad, muudetavus ja Rust ohutusfilosoofia


Rust läheneb muutujate haldamisele teisiti kui enamik keeli. Vaikimisi on kõik muutujad Rust-s muutumatud, mis tähendab, et nende väärtusi ei saa pärast algset määramist muuta. Selle disainiotsuse eesmärk on vältida tavalisi programmeerimisvigu, mis tekivad ootamatutest olekumuutustest.


Kui te deklareerite muutuja, kasutades `let x = 5`, muutub see muutuja vaikimisi muutumatuks. Kõik katsed selle väärtust hiljem muuta toovad kaasa kompileerimisvea. See muutumatuse nõue sunnib arendajaid hoolikalt mõtlema, millal oleku muutmine on tõesti vajalik ja muudab koodi käitumise prognoositavamaks. Paljud programmeerimisvead tulenevad muutujate ootamatutest muutustest ja Rust vaikimisi muutumatus aitab neid probleeme vältida.


Kui teil on tõesti vaja muutuja väärtust muuta, nõuab Rust muutuvuse selgesõnalist deklareerimist võtmesõna `mut` abil: `let mut x = 5`. See selgesõnaline deklareerimine on selge signaal nii kompilaatorile kui ka teistele arendajatele, et selle muutuja väärtus võib programmi täitmise ajal muutuda. Nõue deklareerida muutuvust selgesõnaliselt julgustab hoolikalt kaaluma, kas muutuvus on iga muutuja puhul tõesti vajalik.


Rust toetab ka varjutamist, mis võimaldab teil deklareerida uue muutuja sama nimega kui eelmine muutuja. Erinevalt mutatsioonist luuakse varjutamisega täiesti uus muutuja, millel on sama nimi, mis tegelikult varjab eelmise muutuja. See tehnika osutub eriti kasulikuks, kui andmeid muudetakse mitme sammu kaudu, näiteks kui parsitakse string numbriks ja seejärel töödeldakse seda numbrit edasi. Varjutamise abil saate säilitada muutuja nime järjepidevalt kogu teisendusprotsessi vältel, muutes samal ajal muutuja tüüpi igal sammul.


Tüübimuutuste käsitlemisel muutub oluliseks erinevus varjutuse ja mutatsiooni vahel. Varjutamise puhul saate muuta nii muutuja väärtust kui ka tüüpi, sest te loote uue muutuja. Mutatsiooniga saab muuta ainult väärtust, säilitades samas tüübi, sest te muudate olemasolevat muutujat, mitte ei loo uut.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Andmetüübid ja tüübisüsteemi alused


Rust rakendab tugevat, staatilist tüübisüsteemi, kus igal väärtusel peab olema hästi määratletud tüüp, mis on teada kompileerimise ajal. Kuigi see võib tunduda piirav võrreldes dünaamiliselt tüpiseeritud keeltega, tähendab Rust tüübi tuletamise võime, et tüüpe tuleb harva selgesõnaliselt määrata. Kompilaator suudab tavaliselt määrata sobiva tüübi selle põhjal, kuidas te väärtust kasutate.


Teatud olukordades on siiski vaja selgesõnalisi tüübimärkusi. Kui kasutate üldisi funktsioone nagu `parse()`, mis võivad teisendada stringid erinevateks numbrilisteks tüüpideks, peab kompilaator teadma, millist tüüpi te soovite. Sellistel juhtudel annoteerite tüübi, kasutades kooloni süntaksit: `let guess: u32 = "42".parse().expect("Mitte number!")`.


Rust skalaartüüpide hulka kuuluvad täisarvud, ujukomaarvud, booleanid ja tähemärgid. Tervikutüüpide süsteem võimaldab täpset kontrolli mälukasutuse ja jõudluse omaduste üle. Terviktüübid on süstemaatiliselt nimetatud: `i8`, `i16`, `i32`, `i64` ja `i128` täisarvude jaoks ning `u8`, `u16`, `u32`, `u64` ja `u128` täisarvude jaoks. Numbrid näitavad bittide laiust, mis teeb mälukasutuse ja väärtusvahemikud kohe selgeks.


Erilist tähelepanu väärivad tüübid `isize` ja `usize`, kuna need kohanduvad teie sihtarhitektuuriga. 64-bitistes süsteemides on need tüübid 64 bitti laiad, samas kui 32-bitistes süsteemides on nad 32 bitti laiad. Neid tüüpe kasutatakse tavaliselt massiivide indekseerimiseks ja mälu offsettide määramiseks, sest need vastavad sihtarhitektuuri loomulikule sõnasuurusele, võimaldades tõhusat osutiaritmeetikat ja mäluoperatsioone.


Rust pakub mitut võimalust täisarvuliste kirjete kirjutamiseks, sealhulgas kümnendsüsteemi, heksadetsimaalset (`0x`), oktaal- (`0o`) ja binaarsüsteemi (`0b`) formaati. Samuti võite kasutada numbrilistes literaalides kõikjal alajaotusi, et parandada loetavust, näiteks kirjutada `1_000_000` asemel `1000000`. Alamjooned ei mõjuta väärtust, kuid võivad muuta suured arvud loetavamaks.


Rust ujukomatüübid on lihtsad: `f32` ühe täpsusega ja `f64` kahe täpsusega ujukomaarvude jaoks. Tüüpi `f64` eelistatakse üldiselt selle suurema täpsuse ja asjaolu tõttu, et moodsad protsessorid suudavad sageli 64-bitiseid ujukomaoperatsioone sama tõhusalt kui 32-bitiseid operatsioone.


### Liidetud tüübid ja andmete korraldus


Lisaks skalaartüüpidele pakub Rust ka liittüüpe, mis rühmitavad mitu väärtust kokku. Tuplid võimaldavad eri tüüpi väärtusi kombineerida üheks liitväärtuseks. Tuplid luuakse sulgudes ja iga elemendi tüübi saab määrata: `let tup: (i32, f64, u8) = (500, 6.4, 1)`.


Tuplid toetavad destruktureerimist, mis võimaldab eraldada üksikuid väärtusi: `let (x, y, z) = tup`. See süntaks loob tupli komponentidest kolm eraldi muutujat. Alternatiivina saab tupli elementidele otse juurde pääseda, kasutades punkti märkimist koos elementide indeksiga: `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Massiivid Rust-s erinevad oluliselt paljude teiste keelte massiividest või loenditest, sest neil on fikseeritud suurus, mis muutub osaks nende tüübist. Viie täisarvu massiivi tüüp on `[i32; 5]`, kus semikoolon eraldab elemendi tüübi massiivi pikkusest. See tüübitasandi suurusinfo võimaldab kompilaatoril teostada piiride kontrolli ja tagab, et massiive vastuvõtvad funktsioonid teavad täpselt, kui palju elemente nad peavad ootama.


Massiivide initsialiseerimiseks saate loetleda kõik elemendid selgesõnaliselt: `[1, 2, 3, 4, 5]` või kasutades lühisüntaxi korduvate väärtustega massiividele: `[3; 5]` loob viiest elemendist koosneva massiivi, millel kõigil on väärtus 3. See lühisõnastus on kasulik puhvrite initsialiseerimiseks või vaikeväärtustega massiivide loomiseks.


Massiividele juurdepääsul kasutatakse nurksulgude märkimist nagu enamikus keeltes, kuid Rust pakub nii kompileerimis- kui ka jooksuaegset piiride kontrolli. Kui pääsete massiivi juurde konstantse indeksiga, mida kompilaator saab kontrollida, püüab ta kompileerimisaegse juurdepääsu piiridest väljapoole. Dünaamiliste indeksite puhul, mis on määratud tööajal, lisab Rust piirikontrolli, mis paneb programmi paanikasse, kui üritate pöörduda kehtetu indeksile, vältides mälu ohutuse rikkumisi.



## Ownership ja Rust mälu turvalisus

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Rust unikaalse lähenemisviisi mõistmine mäluhaldusele


Selles peatükis käsitletakse Rust ühte kõige olulisemat mõistet. Kui eelmised mõisted võisid tunduda tuttavad teistest keeltest tulnud programmeerijatele, siis omandiõigus on Rust lähenemine mälu turvalisuse lahendamisele ilma prügikoristuseta.


Rust on loodud eesmärgiga vältida mäluga seotud vigu, mis vaevavad madala taseme keeli nagu C ja C++. Nende probleemide hulka kuuluvad use-after-free vead, kus mälu kasutatakse pärast selle vabastamist, ja puhvri ülevoolud, kus programmid kirjutavad väljaspool eraldatud mälupiiride piire. Traditsioonilised lahendused nendele probleemidele on olnud seotud kompromissidega, mida Rust püüab kõrvaldada. Kõrgema taseme keeled nagu Java ja Go lahendavad mälu turvalisuse prügikoristuse abil, kus automaatne protsess tuvastab perioodiliselt kasutamata mälu ja vabastab selle. Kuid prügikogujad põhjustavad jõudluse ülekoormust ja võivad programmi täitmise ajal põhjustada ettearvamatuid pausse, mistõttu nad ei sobi süsteemide programmeerimiseks, kus järjepidev jõudlus on kriitilise tähtsusega.


Rust saavutab mäluohutuse peamiselt kompileerimise ajal teostatava staatilise analüüsi abil. Kompilaator uurib lähtekoodi ja suudab kindlaks teha, kas enamik mäluoperatsioone on turvalised, ilma et oleks vaja prügikoristust. Juhtumite puhul, mida ei saa staatiliselt kontrollida - näiteks massiivide kasutamine jooksuajal arvutatud indeksitega - lisab Rust piirikontrolli, mis paneb paanika, mitte ei luba määratlemata käitumist. See lähenemine erineb põhimõtteliselt C ja C++ jaoks olemasolevatest staatilistest analüsaatoritest, mis on paigaldatud keeltesse, mis algselt ei olnud mõeldud ulatuslikuks staatiliseks analüüsiks. Rust süntaks ja keelereeglid töötati algusest peale välja, et võimaldada ulatuslikku kompileerimise ajalist kontrolli, mis tagab, et kui programm on edukalt kompileeritud, siis töötab see kas ohutult või paaniliselt, mitte aga määratlemata käitumisega.


### Ownership süsteem: Reeglid ja põhimõtted


Rust mälu turvalisuse garantiide nurgakivi on omandisüsteem, mis reguleerib, kuidas mälu hallatakse kogu programmi täitmise ajal. Ownership töötab kolme põhireegli alusel, mida kompilaator alati järgib:


1. Igal Rust väärtusel on omanik (muutuja, mis hoiab seda väärtust)

2. Korraga võib olla ainult üks omanik

3. Kui omanik väljub reguleerimisalast, langeb väärtus ära


Rust-s defineeritakse ulatused tavaliselt kumerate sulgude abil, kas funktsioonide kehades, tingimuslike plokkide või selgesõnaliselt loodud ulatuse plokkide sees. Kui muutuja on deklareeritud vahemikus, saab see vahemik muutuja väärtuse omanikuks. Muutuja jääb kättesaadavaks ja kehtivaks kogu vahemiku eluea jooksul, kuid niipea, kui täitmine väljub vahemikust, puhastatakse kõik omanduses olevad muutujad automaatselt protsessi kaudu, mida nimetatakse mahakandmiseks (dropping).


See automaatne puhastamine on rakendatud Rust loobumismehhanismi abil, kus keel kutsub kaudselt loobumisfunktsiooni muutujate väljumisel ulatusest. Põhitüüpide puhul tähendab see lihtsalt seda, et mälu märgitakse taaskasutamiseks vabaks. Keerulisemate tüüpide puhul, mis haldavad ressursse, võivad kohandatud loobumise rakendused teha täiendavaid puhastustoiminguid, näiteks sulgeda failikäepidemeid või vabastada võrguühendusi. See muster, mis on laenatud C++ RAII (Resource Acquisition Is Initialization), tagab, et ressursid vabastatakse alati korralikult, ilma et see nõuaks programmeerijalt selgesõnalist puhastamise koodi.


### Ownership teisaldamine ja mälu paigutus


Muutujate vahelise omandiõiguse ülemineku mõistmiseks on vaja uurida lihtsate ja keeruliste tüüpide erinevust mälu paigutuse ja kopeerimiskäitumise osas. Lihtsatel tüüpidel, nagu täisarvud, boole'id ja ujukomaarvud, on kompileerimise ajal fikseeritud ja teadaolev suurus ning neid saab tõhusalt kopeerida. Kui te omistate ühe täisarvu muutuja teisele, loob Rust väärtuse täieliku, sõltumatu koopia, mis võimaldab mõlemal muutujal samaaegselt eksisteerida ilma omandiõiguse probleemita.


Keerulised tüübid, nagu stringid, kujutavad endast teistsugust väljakutset, sest nad haldavad dünaamiliselt eraldatud mälu. String koosneb Rusts kolmest komponendist, mis on salvestatud virna: viide kuhjaga eraldatud tähemärkide andmetele, stringi praegune pikkus ja eraldatud puhvri kogumaht. See struktuur võimaldab stringidel tõhusalt kasvada ja kahaneda, säilitades samal ajal teadmise nende piiridest. Kui te määrate ühe String-muutuja teisele, seisab Rust valiku ees: ta võib kopeerida ainult virna-põhist struktuuri (luues kaks osutajat samadele kuhjaandmetele) või teha kõigi kuhjaandmete sügava koopia.


Rust käitub vaikimisi nii, et kopeerimise asemel liigutatakse omanik, viies kuhjaandmed lähtemuutujast sihtmuutujasse ja tühistades lähtemuutuja. See lähenemisviis hoiab ära ohtliku stsenaariumi, kus mitu muutujat võivad muuta sama kuhja mälu või kus sama mälu võidakse vabastada mitu korda, kui muutujad väljuvad ulatusest. Liikumisoperatsioon on tõhus, sest see kopeerib ainult väikese virna-põhise struktuuri, mitte potentsiaalselt suuri kuhjaandmeid, säilitades samal ajal mälu turvalisuse, tagades ühe omaniku.


### Viited ja laenamine


Ehkki omandiõiguse liikumine pakub turvalisust, võib see olla piirav, kui on vaja kasutada väärtust mitmes kohas ilma omandiõiguse üleandmiseta. Rust lahendab selle probleemi laenamise abil, mis võimaldab funktsioonidel ja muutujatel ajutiselt andmetele ligi pääseda ilma omandiõigust võtmata. Viide, mis on loodud ampersand-operaatoriga, annab väärtusele ainult lugemisõigusega juurdepääsu, jättes samal ajal omandiõiguse algsele muutujale.


Viited võimaldavad funktsioonidel toimida andmetega ilma neid tarbimata, võimaldades sama väärtust programmis mitu korda kasutada. Kui te annate viite funktsioonile üle, siis laenate andmeid ajutiselt ja funktsioon peab viite tagastama, enne kui algne omanik saab täieliku kontrolli tagasi. See laenamise metafoor peegeldab juurdepääsu ajutist iseloomu: nii nagu te võite laenata raamatut sõbrale, säilitades samal ajal omandiõiguse, võimaldavad viited ajutist juurdepääsu, säilitades samal ajal algse omandisuhte.


Muutuvad viited laiendavad seda kontseptsiooni, et võimaldada laenatud andmete muutmist, kuid rangete piirangutega, et säilitada turvalisus. Rust lubab igal ajahetkel ainult ühte muutuvat viidet andmetele, vältides andmevõistlusi, kus mitu programmiosa võib samaaegselt muuta sama mälu. Lisaks ei saa samaaegselt olla nii muutuvaid kui ka muutumatuid viiteid samadele andmetele, sest see võib põhjustada olukordi, kus kood eeldab, et andmed on stabiilsed, samal ajal kui teine kood neid aktiivselt muudab. Need reeglid jõustatakse kompileerimise ajal, kõrvaldades terved klassid paralleelsuse vigu, mis vaevavad teisi süsteemiprogrammeerimiskeeli.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Stringitüübid ja viilud


Rust eristab string literaale ja String tüüpi, mis peegeldab erinevaid mäluhaldusstrateegiaid ja kasutusjuhtumeid. String literaalid on varjatud otse kompileeritud binaarsesse faili ja neil on tüüp &str (string slice), mis kujutab vaadet muutumatutele string-andmetele. Need literaalid on tõhusad, sest nad ei nõua jooksuaegset eraldamist, kuid neid ei saa muuta, kuna nad on osa programmi koodist.


String-tüüp seevastu haldab dünaamiliselt eraldatud mälu ning võib kasvada, kahaneda ja muutuda töö ajal. Stringi saab luua literaalist, kasutades String::from() või sarnaseid meetodeid, mis eraldab kuhja mälu ja kopeerib literaali sisu. See erinevus võimaldab Rust-l optimeerida nii jõudlust (kasutades literaale, kui see on võimalik) kui ka paindlikkust (kasutades Stringi, kui on vaja muuta).


Stringiviilud (&str) pakuvad võimsat abstraktsiooni stringide osadega töötamiseks ilma andmeid kopeerimata. Viil sisaldab näitajat stringi alguse andmetele ja pikkust, mis võimaldab tõhusalt viidata alamstringidele. Slice'i süntaks kasutab vahemikke (nt &s[0..5]), et määrata, millisele stringi osale viidata. Kuna viilud on viited, kehtivad nende suhtes laenutusreeglid, mis takistavad aluseks oleva stringi muutmist viilude olemasolu ajal. See kompileerimise ajaline jõustamine hoiab ära tavalised vead, näiteks juurdepääsu kehtetule mälule pärast seda, kui algne string on vabastatud või muudetud.


### Massiivid, vektorid ja üldised viilud


Slice'i kontseptsioon laieneb stringidest mis tahes elementide jadale, pakkudes ühtset võimalust töötada nii fikseeritud suurusega massiividega kui ka dünaamiliste vektoritega. Rust massiivide pikkus on kodeeritud nende tüübis (nt [i32; 5] viie 32-bitise täisarvu massiivi puhul), mis muudab need sobivaks olukordades, kus on vaja kompileerimisajal garanteeritud suurust. Funktsioonid, mis aktsepteerivad massiive, võivad kehtestada täpseid pikkuse nõudeid, mis on kasulikud selliste operatsioonide puhul nagu krüptograafilised funktsioonid, mis vajavad täpse suurusega sisendeid.


Viilud (&[T]) pakuvad paindlikumat alternatiivi, mis kujutab endast vaadet mis tahes külgnevale elementide järjestusele, sõltumata aluseks olevast salvestusest. Viilud saab luua massiividest, vektoritest või teistest viiludest ning sama viil võib kogu oma eluea jooksul viidata erinevatele andmeosadele. Selline paindlikkus muudab viilud ideaalseks funktsioonide jaoks, mis peavad töötlema jadasid, hoolimata konkreetsest salvestusmehhanismist või täpsest suurusest.


Omanditüüpide (String, Vec<T>) ja nende laenatud viilude (&str, &[T]) vaheline suhe järgib kogu Rust-s järjepidevat mustrit. Omanikud tüübid haldavad oma mälu ja neid saab muuta, samas kui viilud pakuvad tõhusat, ainult lugemisega juurdepääsu nende andmete osadele. Selline disain võimaldab APIsid, mis on nii paindlikud (võttes erinevaid sisendtüüpe vastu viilude kaudu) kui ka tõhusad (vältides tarbetut kopeerimist), säilitades samal ajal Rust ohutustagatised laenutussüsteemi kaudu.



## Struktuurid, komplekssete andmetüüpide loomine

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Rust struktuurid on aluseks keerukate andmetüüpide loomisele, sarnaselt teiste programmeerimiskeelte klassidega. Need võimaldavad rühmitada omavahel seotud andmeid üheks ühtseks tervikuks, mis võib sisaldada mitmeid eri tüüpi välju. Struktuuri defineerimise süntaks on lihtne: te kasutate võtmesõna "struktuur", millele järgneb struktuuri nimi, seejärel defineerite väljad sulgudes, kasutades kooloni süntaksit iga välja tüübi määramiseks.


Rust järgib struktuuride puhul konkreetseid nimetamiskonventsioone, mida kompilaator nõuab hoiatuste kaudu. Struktuuride nimed peaksid kasutama CamelCase'i (tuntud ka kui PascalCase), samas kui struktuuris olevad väljade nimed peaksid kasutama snake_case'i koos allajoonega. See konventsioon aitab säilitada järjepidevust Rust koodibaasides ja muudab koodi teistele arendajatele loetavamaks.


Struktuuride instantside loomiseks peate määrama kõigi väljade väärtused, kasutades struktuuri nime, millele järgnevad lahtrite määranguid sisaldavad kumerad sulgud. Kui teil on struktuuri instants, saate üksikutele väljadele ligi pääseda ja neid muuta, kasutades punktmärkust, tingimusel, et instants on deklareeritud muutuvana. See punktmärkimine töötab Rusts järjepidevalt, erinevalt keeltest nagu C++, kus te võite kasutada erinevaid operaatoreid näitajate ja otseste objektide jaoks.


### Konstruktori funktsioonid ja väljade otseteed


Rust-l ei ole sisseehitatud konstruktoreid nagu mõnel objektorienteeritud keelel, kuid te saate luua funktsioone, mis tagastavad struktuuride instantsid, mis täidavad sama eesmärki. Need konstruktori funktsioonid võtavad tavaliselt parameetrid mõnele või kõigile väljadele ja võivad teistele määrata vaikeväärtused. Selliste funktsioonide kirjutamisel pakub Rust mugavat lühendit: kui parameetril on sama nimi kui struktuuriväljal, võib lihtsalt kirjutada välja nime üks kord, selle asemel, et korrata seda formaadis `väli: väärtus`.


Struktuuriinstantse saab luua ka olemasolevate instantside väärtuste kopeerimise teel, kasutades struct update süntaksit. See funktsioon võimaldab teil luua uue instantsi, määrates ainult need väljad, mida soovite muuta, kusjuures kõik muud väljad kopeeritakse olemasolevast instantsist. See operatsioon järgib aga Rust omandireegleid, mis tähendab, et mitte-kopeeritavad tüübid teisaldatakse lähteinstantsist, mis võib muuta algse instantsi osad hiljem kasutuskõlbmatuks. Kompilaator jälgib neid osalisi liigutusi intelligentselt, võimaldades jätkata nende väljade kasutamist, mida ei liigutatud, kuid takistades samal ajal juurdepääsu liigutatud väljadele.


### Tupelstruktuurid ja ühikstruktuurid


Rust toetab topelstruktuurid, mis on struktuurid, millel on nimetamata väljad, millele pääseb juurde pigem indeksi kui nime järgi. Need on kasulikud lihtsate manteltüüpide puhul või kui teil on vaja struktuuri, kuid ei ole vaja nimelisi välju. Tupelstruktuuride väljadele pääseb ligi, kasutades punkti märkimist, millele järgneb välja indeks, näiteks `.0` esimese välja jaoks, `.1` teise jaoks jne. See lähenemine töötab hästi struktuuride puhul, mis ümbritsevad ühte väärtust või sisaldavad vaid mõnda tihedalt seotud väärtust, kus nimed võivad olla üleliigsed.


Ühikstruktuurid on struktuuride lihtsaim vorm - need ei sisalda üldse mingeid andmeid. Kuigi see võib esialgu tunduda mõttetu, muutuvad ühikstruktuurid Rust omadussüsteemiga töötades väärtuslikuks, kuna nendega saab rakendada käitumist ilma andmeid salvestamata. Need tühjad struktuurid toimivad Rust edasijõudnute mustrites markeritena või paigutussalvestusena.


### Meetodid ja nendega seotud funktsioonid


Struktuurid saavad lisafunktsionaalsust, kui lisate käitumist rakendusblokkide kaudu. Kasutades võtmesõna `impl`, millele järgneb struktuuri nimi, saate defineerida meetodeid, mis toimivad teie struktuuri instantsidega. Meetodid on funktsioonid, mis võtavad esimese parameetrina `self`, mis võib olla omandatud väärtus (`self`), muutumatu viide (`&self`) või muutuv viide (`&mut self`), sõltuvalt sellest, mida meetod peab instantsiga tegema.


Parameetri `self` tüübi valik määrab meetodi käitumise seoses omandiõigusega. Meetodid, mis võtavad `&self`, saavad lugeda instantsist ilma omandit võtmata, mistõttu sobivad nad operatsioonideks, mis ei muuda struktuuri. Meetodid, mis võtavad `&mut self`, võivad instantsi muuta, võimaldades kutsujale siiski omandiõiguse säilitamist. Meetodid, mis võtavad `self` väärtuse järgi, tarbivad instantsi, mis sobib operatsioonide jaoks, mis muudavad struktuuri millekski muuks või kui meetod kujutab endast lõplikku operatsiooni selle instantsiga.


Seotud funktsioonid on funktsioonid, mis on defineeritud rakendusplokis ja mis ei võta parameetrina `self`. Need on sarnased teiste keelte staatiliste meetoditega ja neid kasutatakse tavaliselt konstruktoritena või tüübiga seotud abifunktsioonidena. Assotsieerunud funktsioone kutsutakse topeltkooloni süntaksiga (`Type::function_name()`), mis eristab neid selgelt meetoditest, mida kutsutakse instantside peal.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Loendused: Modelleerimisvalikud ja -variandid


Rust loenditel on rohkem võimalusi kui loenditel paljudes teistes keeltes. Kuigi nad võivad kujutada lihtsaid nimeliste konstandide kogumeid, võivad Rust loendused kanda ka andmeid iga variandi sees, mistõttu sobivad nad selliste olukordade modelleerimiseks, kus väärtus võib olla üks mitmest erinevast tüübist või olekust. Iga enumivariant võib sisaldada eri tüüpi ja erineva hulga andmeid, alates sellest, et andmeid ei ole üldse, kuni keeruliste struktuurideni koos nimeliste väljadega.


Võimalus lisada andmeid enum-variantidele kõrvaldab paljud teistes keeltes levinud programmeerimisvead. Selle asemel, et säilitada eraldi muutujaid tüübinäitaja ja seotud andmete jaoks - mis võivad kergesti muutuda ebajärjekindlaks -, ühendab Rust enumid tüübiinfo andmetega. See disain tagab, et andmed vastavad alati variandile, vältides mittevastavusi, mis võivad põhjustada tööaegseid vigu.


Enum-variandid võivad sisaldada andmeid mitmel kujul: lihtsate lipukeste puhul puuduvad andmed, nimetamata väljade puhul tuplilaadsed andmed või nimeliste väljadega struktuurilaadsed andmed. Neid stiile võib isegi ühe enumi sees segada, valides iga variandi jaoks sobivaima vormi. Selline paindlikkus muudab enumid sobivaks keerukate domeenimõistete modelleerimiseks, kus eri juhtudel on vaja erinevat teavet.


#### Valiku tüüp: Puudumise turvaline käsitlemine


Üks Rust tähtsamaid enumeid on `Option<T>`, mis esindab väärtusi, mis võivad olla või mitte olla olemas. Sellel enumil on kaks varianti: `Some(T)`, mis sisaldab T-tüüpi väärtust, ja `None`, mis tähistab väärtuse puudumist. Tüüp Option on Rust lahendus nullnäidiku probleemidele, mis vaevavad paljusid teisi keeli, sundides arendajaid selgesõnaliselt tegelema juhtumitega, kus väärtused võivad puududa.


Valikutüüpide kasutamine muudab teie koodi töökindlamaks, sest kompilaator nõuab, et te käsitleksite nii väärtuste olemasolu kui ka puudumist. Te ei saa kogemata kasutada potentsiaalselt puuduvat väärtust, kontrollimata kõigepealt, kas see on olemas. Selline selgesõnaline käitlemine hoiab ära nullnäidiku erandid ja sarnased jooksuaegsed vead, mis on teistes programmeerimiskeeltes levinud vigade allikad.


Tüüp Option on integreeritud Rust mustri sobitamise süsteemiga, mis võimaldab teil käsitleda mõlemat juhtumit. Meetodid nagu `unwrap_or()` pakuvad mugavaid viise väärtuste väljavõtmiseks koos tagavaraväärtustega, samas kui meetodid nagu `map()` ja `and_then()` võimaldavad funktsionaalse programmeerimise mustreid valikuliste väärtustega töötamiseks.


### Mustri sobitamine koos sobitusväljenditega


Mustri sobitamine `match` avaldiste abil annab võimaluse töötada enumide ja muude andmetüüpidega. Vastavusavaldis uurib väärtust ja täidab erinevat koodi vastavalt sellele, millisele mustrile väärtus vastab. Iga muster võib sobitatud väärtust destruktureerida, sidudes selle osad muutujatega, mida saab kasutada vastavas koodiplokis.


Vastavusavaldused peavad olema ammendavad, mis tähendab, et nad peavad käsitlema kõiki võimalikke vastatava tüübi juhtumeid. See nõue hoiab ära vead, mis võivad tekkida, kui teatud juhtumid jäetakse kogemata käsitlemata. Kui te ei taha iga juhtumit selgesõnaliselt käsitleda, võite kasutada metsiku mustri (`_`), et püüda kõik ülejäänud juhtumid või siduda käsitlemata juhtumid muutujale, kui teil on vaja juurdepääsu väärtusele.


Konstruktsioon `if let` pakub kokkuvõtlikumat alternatiivi sobitamiseks, kui teid huvitab ainult üks konkreetne muster. See süntaks on eriti kasulik, kui töötate Option-tüüpidega või kui soovite koodi käivitada ainult siis, kui väärtus vastab konkreetsele enum-variandile. Konstruktsioon `if let` võib sisaldada `else` klauslit juhtudeks, kui muster ei vasta, mis teeb sellest lihtsate mustri sobitamise stsenaariumide käsitlemise lihtsaima viisi.


#### Kollektsioonid: Andmerühmade haldamine


Rust standardraamatukogu pakub mitmeid kollektsioonitüüpe seotud andmete rühmade haldamiseks. Need kogumid on üldised, mis tähendab, et neis saab salvestada mis tahes tüüpi elemente ja need haldavad mälu automaatselt. Kõige sagedamini kasutatavad kollektsioonid on vektorid järjestatud loendite jaoks, hash-kaardid võtmeväärtusühenduste jaoks ja stringid tekstiandmete jaoks.


#### Vektorid: Dünaamilised massiivid


Vektorid kujutavad kasvavaid massiive, mille suurus võib programmi täitmise ajal muutuda. Erinevalt fikseeritud suurusega massiividest eraldavad vektorid mälu kuhjaga ja võivad vastavalt vajadusele laieneda või kahaneda. Vektori loomine nõuab sageli selgesõnalist tüübi märkimist, kui alustatakse tühja vektoriga, sest kompilaator peab teadma, mis tüüpi elemente vektor sisaldab.


Vektorid pakuvad mitmeid võimalusi elementidele juurdepääsuks, millest igaühel on erinevad turvaomadused. Indeksi märkimine (`vec[0]`) annab otsese juurdepääsu, kuid paanikat tekitab, kui indeks on väljaspool piire. Meetod `get()` tagastab `Option`, mis võimaldab graatsiliselt käsitleda piiride ületamist. Valik nende lähenemisviiside vahel sõltub sellest, kas te saate tagada indeksi kehtivust või peate võimalikke tõrkeid käsitlema.


Rust laenutusreeglid kehtivad vektorite suhtes, vältides tavalisi mäluohutusprobleeme. Kui teil on viide vektori elemendile, ei saa te vektorit muuta enne, kui see viide läheb väljapoole ulatust. See hoiab ära olukorrad, kus viited võivad osutada vabastatud mälule pärast vektorioperatsioone, näiteks uute elementide sisestamist või vektori tühjendamist.


#### Hash kaardid: Key-Value Storage


Hash kaardid pakuvad tõhusat võtme-väärtuse salvestust, kus saab kiiresti otsida väärtusi nendega seotud võtmete alusel. Nii võtmed kui ka väärtused võivad olla mis tahes tüüpi, kuigi võtmed peavad rakendama vajalikke omadusi hashinguks ja võrdsuse võrdlemiseks. Hash kaardid võtavad sisestatud väärtuste omandiõiguse, välja arvatud juhul, kui väärtused rakendavad omadust Copy.


Hash kaardid pakuvad mitmeid meetodeid väärtuste sisestamiseks ja uuendamiseks. Põhiline meetod `insert()` kirjutab olemasolevad väärtused üle, samas kui `entry()` pakub paindlikumat sisestamisloogikat. API sissekanne võimaldab sisestada väärtusi ainult siis, kui neid veel ei ole, või uuendada olemasolevaid väärtusi nende praeguse seisundi alusel. See API on kasulik selliste mustrite puhul nagu esinemiste loendamine või jooksvate kogusummade säilitamine.


Hash-kaartide väärtuste otsimisel tagastab meetod `get()` meetodi `Option`, kuna soovitud võtit ei pruugi olla olemas. Te võite kasutada meetodeid nagu `copied()`, et teisendada `Option<&T>`st `Option<T>`sse, kui tegemist on Copy tüüpi, ja `unwrap_or()`, et pakkuda vaikeväärtusi, kui võtmed puuduvad.


### Stringide käsitlemine ja Unicode


Rust stringid on kodeeritud UTF-8 koodiga, mis pakub täielikku Unicode-tuge, kuid muudab need võrreldes lihtsate ASCII stringidega keerulisemaks. String-tüüp `String` kujutab enda omanduses olevaid, kasvatatavaid tekstandmeid, samas kui string-viilud (`&str`) pakuvad laenatud vaateid string-andmetele. Nende tüüpide vahel saab konverteerida vastavalt vajadusele, kusjuures string-slices kasutatakse sageli funktsiooniparameetrite jaoks, et võtta vastu nii omatud stringid kui ka string-literaalid.


Stringiga manipuleerimine hõlmab meetodeid teksti lisamiseks, mitme väärtuse vormindamiseks koos ja alamjoonte eraldamiseks. Meetod `push_str()` lisab stringilõike ilma omanikuta, samas kui makro `format!` pakub paindlikku viisi stringide konstrueerimiseks mitmest komponendist. Stringindeksitega töötamisel tuleb olla ettevaatlik, et järgida UTF-8 tähemärkide piire, et vältida paanikaid tööajal.


Turvaliseks märkide kaupa töötlemiseks pakuvad stringid iteratsioonimeetodeid nagu `chars()` Unicode'i skalaarväärtuste jaoks ja `bytes()` tooraine baitide ligipääsuks. Need iteraatorid käitlevad UTF-8 kodeeringut õigesti, tagades, et te ei lõhu kogemata mitmikbaidiseid märke. Selline lähenemine on turvalisem ja usaldusväärsem kui käsitsi indekseerimine, eriti kui töötate rahvusvahelise tekstiga, mis võib sisaldada keerulisi Unicode-märke.



## Rust kahe kategooria veakäitlussüsteem

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust läheneb veakäsitlusele põhimõtteliselt teisiti kui enamik programmeerimiskeeli. Kui paljud keeled tuginevad peamiselt eranditele, siis Rust eristab kahte erinevat veakategooriat ja pakub spetsiifilisi mehhanisme mõlema tüübi käsitlemiseks. Selles peatükis uuritakse Rust põhjalikku veakäitlussüsteemi, mis hõlmab nii parandamatuid vigu, mis lõpetavad programmi täitmise, kui ka taastatavaid vigu, mis võimaldavad programmidel jätkata tööd väärikalt.


### Parandamatud vead ja paanika


Parandamatud vead kujutavad endast olukordi, kus programm on sattunud ebajärjekindlasse või ootamatusse olekusse, millest ta ei saa ohutult taastuda. Nende hulka kuuluvad sellised stsenaariumid nagu juurdepääs massiivi piiridest väljapoole, katsed teha operatsioone, mis rikuvad mälu turvalisust, või tingimused, mis viitavad programmi loogika põhilistele vigadele. Selliste vigade ilmnemisel on asjakohane reageerida programmi kohesele lõpetamisele, selle asemel et riskida edasise vigastuse või määratlemata käitumisega.


Rust-s käivitavad taastamatud vead paanika, mis põhjustab programmi kontrollitud kokkuvarisemise. Enne lõpetamist teostab Rust protsessi nimega unwinding, mille käigus ta kõnnib tagasi läbi kutsete virna, et esitada üksikasjalik virna jälg, mis näitab täpselt, kus paanika tekkis. See lahtipööramise protsess aitab arendajatel tuvastada probleemi allikat silumise ajal. Jõudluskriitiliste rakenduste või manussüsteemide puhul võite keelata tagasipööramise ja konfigureerida Rust nii, et see katkestab paanika ilmnemisel kohe, kuigi see ohverdab kiirema lõpetamise nimel vigade kõrvaldamise teabe.


Paanika saab käivitada selgesõnaliselt, kasutades makrot `panic!` koos kohandatud sõnumiga. Kui paanika tekib, näete väljundit, mis näitab, milline lõim paanikas oli ja sellega seotud sõnumit. Keskkonnamuutuja `RUST_BACKTRACE` seadistamine annab täiendavat silumisalast teavet, näidates kogu paanika tekkimiseni viinud kõnede virna. Näiteks, kui üritatakse ligi pääseda ainult kolme elementi sisaldava vektori elemendile 99, siis generate annab paanika koos sõnumiga "index out of bounds" ja tagasiside, mis näitab vea põhjustanud funktsioonikutsete täpset järjestust.


### Taastatavad vead koos tulemusega


Taastatavad vead kujutavad endast eeldatavaid veatingimusi, mida programmid suudavad väärikalt käsitleda ilma lõpetamata. Näideteks on näiteks katse avada faili, mida ei ole olemas, võrguühenduse tõrked või vigane kasutaja sisestus. Rust pakub nende olukordade jaoks enumit `Result`, mis esindab selgesõnaliselt operatsioone, mis võivad ebaõnnestuda, ja sunnib arendajaid käsitlema nii õnnestumise kui ka ebaõnnestumise juhtumeid.


Tulemuse enum on defineeritud kahe variandiga: `Ok(T)` edukate operatsioonide jaoks, mis sisaldavad väärtust tüüpi `T`, ja `Err(E)` ebaõnnestumiste jaoks, mis sisaldavad viga tüüpi `E`. See disain kasutab Rust tüübisüsteemi, et tagada, et võimalikke tõrkeid ei saa ignoreerida. Funktsioonid, mis võivad ebaõnnestuda, tagastavad tulemuse `Result` ja kutsuv kood peab selgesõnaliselt käsitlema nii õnnestumise kui ka vea juhtumeid, kasutades tavaliselt mudeli sobitamist `match` väljenditega.


Võtame näiteks funktsiooni `File::open`, mis tagastab `Tulemuse<File, std::io::Error>`. Faili avamisel saadakse kas objekt `File`, kui operatsioon õnnestub, või `std::io::Error`, kui operatsioon ebaõnnestub. Saate selle tulemusega sobitada, et iga juhtumit asjakohaselt käsitleda. Edu korral võite jätkata failioperatsioonidega, samas kui vea korral võite üritada faili luua, proovida alternatiivset lähenemist või levitada viga kutsuvale koodile. Selline selgesõnaline käitlemine tagab, et teie programm teeb teadlikke otsuseid vigade kõrvaldamise kohta, mitte ei jookse ootamatult kokku.


### Veakäitluse mustrid ja otseteed


Kuigi selgesõnaline mustri sobitamine annab täieliku kontrolli veakäitluse üle, pakub Rust mitmeid mugavusmeetodeid tavaliste veakäitlusmustrite jaoks. Meetod `unwrap` võtab `Result`ist välja edevuse väärtuse, kuid paanitseb vea ilmnemisel, mistõttu on see kasulik kiireks prototüüpimiseks või olukordades, kus olete kindel, et operatsioon õnnestub. Meetod `expect` töötab sarnaselt, kuid võimaldab anda kohandatud paanikasõnumi, mis lihtsustab vigade kõrvaldamist, kui asjad lähevad valesti.


Paindlikuma veakäsitluse jaoks võimaldavad meetodid nagu `unwrap_or_else` pakkuda sulgemist, mis käivitub vea ilmnemisel, võimaldades kohandatud taastamisloogikat. Neid operatsioone saab aheldada, et käsitleda keerulisi stsenaariume, näiteks püüda avada faili ja luua see, kui seda ei ole olemas, kusjuures iga sammu jaoks on erinevad veakäitlusstrateegiad.


Küsimärgi operaator (`?`) annab lühikese süntaksi vigade edastamiseks, mis on Rust programmides tavaline. Kui te lisate `?` tulemusele `Result`, siis see mähib automaatselt edukad väärtused lahti ja tagastab vead kohe jooksvast funktsioonist. Seda operaatorit saab kasutada ainult funktsioonides, mis tagastavad `Result` tüüpi, tagades, et vigu saab korralikult ülespoole kutsete virna levitada. Operaator `?` muudab veakäitluskoodi palju loetavamaks, kõrvaldades sõnalised sobitusväljendid, säilitades samas selgesõnalise vea leviku semantika.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Vea levik ja funktsioonide kujundamine


Vea levik on Rust veakäitluse põhikontseptsioon, mis võimaldab funktsioonidel vigu ülespoole edasi anda, selle asemel, et neid lokaalselt käsitleda. Kui projekteerite funktsioone, mis võivad ebaõnnestuda, peaksite tagastama `Result` tüüpi, et anda kutsujale paindlikkus otsustada, kuidas vigadega ümber käia. See lähenemine soodustab komponeeritavat veakäitlust, kus iga funktsioon kõneahelas saab vigu käsitleda kas lokaalselt või edastada neid ülespoole kõrgemal tasemel koodile, millel on rohkem konteksti taastamisotsuste tegemiseks.


Küsitav operaator lihtsustab vigade levikut. Selle asemel, et kirjutada iga potentsiaalselt ebaõnnestunud operatsiooni jaoks üksikasjalikke vasteavaldusi, saab operatsioone ahelatada operaatoritega `?`, luues loetava koodi, mis tegeleb edukuse teega, levitades samal ajal automaatselt kõik tekkivad vead. See muster on nii levinud, et paljud Rust funktsioonid on loodud spetsiaalselt selleks, et nad töötaksid hästi koos operaatoriga `?`, võimaldades sujuvat veakäitlust kogu teie koodibaasis.


Paanika ja vigade tagastamise vahel otsustades kaaluge, kas kutsuv kood saab mõistlikult vigadest taastuda. Kui tõrge kujutab endast programmeerimisviga või taastamatut süsteemi seisundit, on paanikastamine asjakohane. Kui aga tõrge on oodatav seisund, mida kutsuv kood võib sõltuvalt kontekstist erinevalt käsitleda, pakub "Tulemuse" tagastamine suuremat paindlikkust ja koostatavust.


### Parimad tavad ja projekteerimisega seotud kaalutlused


Tõhus veakäitlus Rust-s nõuab läbimõeldud kaalumist, millal tuleb paanikat tekitada ja millal tuleb vigu tagastada. Kasutage paanikat olukordades, mis kujutavad endast programmeerimisvigu või seisundeid, mis ei tohiks korrektsetes programmides kunagi tekkida, näiteks juurdepääs kõvakodeeritud andmetele, mille kehtivus on teada. Näiteks kõvakodeeritud IP-aadressi stringi analüüsimisel, mille õigsust te olete kontrollinud, võib ohutult kasutada `expect` koos kirjeldava sõnumiga, mis selgitab, miks operatsioon ei tohiks kunagi ebaõnnestuda.


Kasutaja poolt juhitava sisendi või välise süsteemi interaktsiooni puhul eelistage alati tagastada `Tulemus` tüüpi, mitte paaniliselt. Kasutajad teevad vigu, failid kustutatakse ja võrguühendused ebaõnnestuvad - need on normaalsed tingimused, mida hästi disainitud programmid peaksid graatsiliselt käsitlema. Nende olukordade puhul vigade tagastamisega võimaldate kutsuvale koodile rakendada sobivaid taastamisstrateegiaid, olgu selleks siis kasutajalt teistsuguse sisendi küsimine, vaikimisi väärtuste taastamine või abistavate veateadete kuvamine.


Kaaluge võimalust luua kohandatud tüübid, mis jõustavad valideerimise konstrueerimise ajal, et vältida kehtetute olekute levikut teie programmis. Näiteks kui teie programm nõuab arvude kasutamist teatud vahemikus, looge ümbritsev tüüp, mis valideerib sisendi konstrueerimise ajal ja ei võimalda luua vigaseid eksemplare. Selline lähenemine kasutab Rust tüübisüsteemi, et kõrvaldada terved veaklassid, muutes kehtetud olekud esindamatuks, vähendades vajadust jooksuaegse veakontrolli järele kogu teie koodibaasis.


## Funktsionaalse programmeerimise omadused, sulgemised ja nutikad osutajad


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Kuigi Rust ei ole puhas funktsionaalne programmeerimiskeel, sisaldab see funktsionaalsetest programmeerimisparadigmadest inspireeritud funktsioone. Need funktsioonid võimaldavad arendajatel kirjutada ülevaatlikku koodi, kasutades selliseid mõisteid nagu sulgemised ja iteraatorid. Rust sisaldab neid funktsionaalseid elemente, et pakkuda paindlikke vahendeid andmetöötluseks ja tagasikutsumehhanismideks.


Rust funktsionaalse programmeerimise funktsioonid säilitavad keele põhiprintsiibid, nagu mälu turvalisus ja nullkulu abstraktsioonid. Kui kasutate sulgemisi ja iteraatoreid, ei ohverda jõudlust väljendusrikkuse nimel - Rust kompilaator optimeerib neid konstruktsioone, et toota tõhusat masinkoodi, mis on võrreldav traditsiooniliste tsüklipõhiste lähenemisviisidega.


### Sulgemise mõistmine


Rust sulgemised on anonüümsed funktsioonid, mis võivad ümbritsevast keskkonnast muutujaid hõivata. Teistes programmeerimiskeeltes nimetatakse neid sageli lambda-funktsioonideks. Sulgemisfunktsioonide peamine omadus on nende võime "sulgeda" oma keskkonda, mis tähendab, et nad saavad kasutada ja kasutada muutujaid, mis on olemas selles vahemikus, kus sulgemine on defineeritud.


Sulgude süntaksis kasutatakse parameetrite defineerimiseks sulgude asemel piibumärke (`|`). Parameetriteta sulgemise puhul kirjutatakse `||` ja parameetritega sulgemise puhul loetletakse need torude vahele nagu `|x, y|`. Kui sulgemise keha koosneb ühestainsast väljendist, võib sulgesid vahele jätta, mis muudab süntaksi väga lühikeseks.


Vaadake seda praktilist näidet t-särkidega tegelevast ettevõttest, mis annab klientide eelistuste põhjal eksklusiivseid särke. Kui klient on määranud oma lemmikvärvi, saab ta selle värvi; vastasel juhul saab ta vaikimisi kõige rohkem laos oleva värvi. Kasutades sulgemisi, muutub see loogika: `user_preference.unwrap_or_else(|| self.most_stocked())`. Sulgemine `||| self.most_stocked()` annab vaikeväärtuse ainult siis, kui see on vajalik, ja see saab juurdepääsu `self` keskkonnast.


### Sulgemistüübi tuletamine ja paindlikkus


Üks Rust kõige mugavamaid funktsioone koos sulgemisega on automaatne tüübi tuletamine. Erinevalt tavalistest funktsioonidest, kus tuleb parameetrite tüübid ja tagastustüübid selgesõnaliselt määrata, saavad sulgurid need tüübid sageli kontekstist tuletada. Kompilaator analüüsib, kuidas sulgemist kasutatakse, ja määrab sobivad tüübid automaatselt. Kui aga sulge on kutsutud konkreetsete tüüpidega, muutuvad need tüübid selle sulge eksemplari jaoks fikseerituks.


Sulgemisi saab salvestada muutujatesse nagu mis tahes muid väärtusi, muutes need keele esimese klassi kodanikeks. Kui te määrate sulgemise muutujale, saate seda hiljem sulgude abil välja kutsuda: lase my_closure = |x| x + 1; lase result = my_closure(5);`. See paindlikkus võimaldab sulgeid anda funktsioonidele argumentidena, tagastada neid funktsioonidest ja kasutada neid andmestruktuurides.


Kui kompilaator ei saa tüüpe tuletada või kui soovite olla selgesõnaline, saate sulgemisparameetrid ja tagasitulekutüübid märkida, kasutades funktsioonidega sarnast süntaksit: `|x: i32| -> i32 { x + 1 }`. Selline selgesõnaline tüübistamine on mõnikord vajalik keerukates stsenaariumides, kus kompilaator vajab lisateavet, et tüüpe õigesti lahendada.


### Keskkonnamuutujate hõivamine


Sulgemised võivad muutujaid oma keskkonnast hõivata kolmel erineval viisil: muutumatu viitega, muutuva viitega või omandiõiguse võtmisega. Rust kompilaator määrab automaatselt kõige piiravama kinnipüüdmismeetodi, mis rahuldab teie sulgemise vajadusi, järgides vähimate privileegide põhimõtet.


Kui sulgemine vajab ainult väärtuse lugemist, võtab see kinni muutumatu viite abil. See võimaldab algset muutujat kasutada ka pärast sulgemise defineerimist ja kutsumist. Näiteks closing, mis trükib nimekirja, laenab nimekirja muutumatult, võimaldades jätkata nimekirja kasutamist pärast closure'i täitmist.


Kui sulgemine peab muutma hõivatud muutujat, peab see hõivama muutuva viitega. Sel juhul tuleb nii tabatud muutuja kui ka sulgemine ise deklareerida muutuvaks. Seejärel võib sulgemine muuta hõivatud muutujat, kuid laenamise reeglid kehtivad endiselt - te ei saa omada teisi viiteid sellele muutujale, kui muutuv sulgemine on olemas.


Kõige piiravam püüdmismeetod on omandiõiguse võtmine, mis liigutab püütud muutujad sulgemisse. See on vajalik siis, kui sulgemine võib ületada algselt defineeritud muutujate ulatuse, näiteks lõimede loomisel. Omanikuõiguse hõivamist saab sundida, kasutades võtmesõna `move` enne closure'i parameetreid: `move |x| { /* closure body */ }`. See on oluline niidi turvalisuse jaoks, kuna niidid ei saa ohutult laenata teistelt niididelt, mis võivad lõpetada ja oma muutujaid maha jätta.


### Sulgemise tunnused ja funktsioonitüübid


Rust kujutab sulgemisi kolme peamise tunnuse süsteemi kaudu: `FnOnce`, `FnMut` ja `Fn`. Need tunnused moodustavad hierarhia, mis kirjeldab, kuidas sulgemisi saab kutsuda ja mida nad saavad teha hõivatud muutujatega.


`FnOnce` on kõige elementaarsem tunnus, mida kõik sulgemised rakendavad. See esindab sulgemisi, mida saab kutsuda vähemalt üks kord. Mõnda sulgurit, eriti neid, mis liigutavad hõivatud väärtusi või tarbivad neid mingil viisil, saab kutsuda ainult üks kord, sest nad hävitavad või liigutavad oma hõivatud andmeid täitmise ajal.


`FnMut` tähistab sulgemisi, mida saab kutsuda mitu korda ja mis võivad muuta oma hõivatud keskkonda. Need sulgemised haaravad muutujaid muutuvate viidetega ja võivad neid muuta mitme kutsumise jooksul. Laenureeglid tagavad, et kui `FnMut` sulgemine on aktiivne, on tal ainuõiguslik muutuv juurdepääs oma hõivatud muutujatele.


`Fn` on kõige piiravam tunnus, mis esindab sulgemisi, mida saab kutsuda mitu korda ilma nende hõivatud keskkonda muutmata. Need sulgemised võtavad kinni ainult muutumatu viite abil ja neid saab kutsuda samaaegselt, ilma et Rust ohutustagatisi rikutaks. Kui sulgemine rakendab `Fn`, siis rakendab ta automaatselt ka `FnMut` ja `FnOnce`, kuna mitmel korral ilma mutatsioonita kutsutavus eeldab mutatsiooniga kutsutavust ja ühekordset kutsumist.


### Töötamine iteraatoritega


Rust iteraatorid pakuvad võimalust andmete jadade töötlemiseks. Nad on laisad, mis tähendab, et nad ei tee mingit tööd enne, kui te neid kasutate, kutsudes meetodeid, mis tegelikult andmeid läbi iteratsiooni läbivad. Selline laisk hindamine võimaldab operatsioonide tõhusat aheldamist ilma vahekogumite loomiseta.


Tunnus `Iterator` määratleb põhifunktsionaalsuse koos seotud tüübiga `Item`, mis esindab seda, mida iterator annab, ja meetodiga `next`, mis tagastab `Option<Self::Item>`. Kui meetod `next` tagastab `None`, on iteraator ammendunud. Selline disain võimaldab iteraatoritel ohutult esitada nii lõplikke kui ka potentsiaalselt lõpmatuid jadasid.


Kollektsioonidest saab luua iteraatoreid, kasutades meetodeid nagu `iter()` laenutava iteratsiooni jaoks, `iter_mut()` muutuva laenutava iteratsiooni jaoks ja `into_iter()` tarbiva iteratsiooni jaoks. Valik nende meetodite vahel sõltub sellest, kas teil on vaja muuta elemente ja kas soovite tarbida algset kollektsiooni.


### Iteraatori adapterid ja tarbijad


Iteraatorite adapterid on meetodid, mis muudavad ühe iteraatori teiseks, võimaldades operatsioone üksteisega aheldada. Tavalised adapterid on `map` iga elemendi teisendamiseks, `filter` elementide valimiseks predikaadi alusel ja `enumerate` indeksite lisamiseks. Need adapterid on laisad - nad ei tee tööd enne, kui neid ei tarbita.


Meetod "map" rakendab iga elemendi suhtes sulgemist, muutes selle millekski muuks. Näiteks `numbers.iter().map(|x| x * 2)` loob iteraatori, mis kahekordistab iga arvu. Meetod `filter` säilitab ainult need elemendid, mille puhul predikaadi sulgemine annab tõese tulemuse: `numbers.iter().filter(|&x| x > 10)` säilitab ainult numbrid, mis on suuremad kui kümme.


Tarbijameetodid läbivad andmeid ja annavad lõpptulemuse. Meetod `collect` tarbib iteraatori ja loob sellest kollektsiooni. Sageli tuleb määrata kollektsiooni tüüp: `let vec: Vec<_> = iterator.collect()`. Muude tarbijate hulka kuuluvad `sum` numbriliste elementide liitmiseks, `fold` väärtuste akumuleerimiseks kohandatud operatsiooniga ja `for_each` külgmõjude teostamiseks igal elemendil.


### Täiustatud iteraatorite mustrid


Täiendavad iteratsioonitoimingud on `zip` kahe iteraatori elementide kaupa ühendamiseks, `chain` iteraatorite ühendamiseks ja `filter_map` filtreerimise ja kaardistamise ühendamiseks ühes toimingus. Meetod `zip` loob paarid kahe iteraatori vastavatest elementidest: `a.iter().zip(b.iter())` toodab tuplid `(a[0], b[0]), (a[1], b[1]), ...`.


Meetod `fold` on kasulik väärtuste akumuleerimiseks. See võtab algväärtuse ja sulgemise, mis ühendab akumulaatori iga elemendiga: `numbers.iter().fold(0, |acc, x| acc + x)` summeerib kõik arvud. Selle mustriga saab teostada palju muid operatsioone, nagu maksimumväärtuste leidmine, stringide moodustamine või keeruliste andmestruktuuride loomine.


Iteraatorite ahelad võimaldavad keerulisi andmetransformatsioone lühidalt väljendada. Näiteks audioandmete töötlemine võib hõlmata järgmist: koefitsiendid.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. See korrutab vastavad koefitsiendid ja puhvri väärtused, summeerib tulemused ja nihutab lõppväärtuse, kõik ühes loetavas väljendis.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Sissejuhatus Smart Pointers'ile


Nutikad osutajad on andmestruktuurid, mis toimivad nagu traditsioonilised osutajad, kuid pakuvad lisavõimalusi ja automaatset mäluhaldust. Erinevalt lihtsatest viidetest on arukad osutajad nende poolt osutatavate andmete omanikud ja nad võivad rakendada kohandatud käitumist mälu eraldamise, eraldamise ja juurdepääsu mustrite puhul. Need on olulised vahendid kuhjaga eraldatud andmete haldamiseks ja keeruliste omandimustrite rakendamiseks, mis lähevad Rust põhilisest omandisüsteemist kaugemale.


"Nutikas" aspekt tuleneb nende võimest automaatselt tegeleda mäluhaldusülesannetega, mis muidu nõuaksid käsitsi sekkumist. Kui nutikas osuti läheb väljapoole ulatust, võib see automaatselt vabastada seotud mälu, vähendada viidearvu või teha muid puhastustoiminguid. Selline automatiseerimine aitab vältida mälulekkeid ja kasutamisjärgseid vigu, pakkudes samal ajal suuremat paindlikkust kui ainult virna jaotamine.


Nutikad osutajad rakendavad tavaliselt kahte peamist omadust: `Deref` ja `Drop`. Tunnus `Deref` võimaldab kasutada arukat osutajat nii, nagu oleks see viide sisalduvatele andmetele. Tunnus `Drop` võimaldab kohandatud puhastusloogikat, kui nutinäidik hävitatakse. Koos võimaldavad need tunnused arukatel osutajatel automaatselt mälu hallata.


### Box Smart Pointer


`Box<T>` on lihtsaim nutikas osutaja, mis pakub kuhja jaotamist mis tahes tüüpi `T` jaoks. `Box`i loomisel salvestatakse sisalduv väärtus mitte virna, vaid kuhja, ja `Box` ise (mis on lihtsalt osuti) salvestatakse virna. Selline suunamine on kasulik, kui on vaja salvestada suuri andmehulki ilma neid liigutamata, kui on vaja tundmatu kompileerimisajaga tüüpi või kui tahetakse efektiivselt üle kanda kuhja andmete omandiõigust.


Boxi loomine on lihtne: `let boxed_value = Box::new(42);`eraldab kuhjaga täisarvu. `Box` haldab seda mälu automaatselt - kui `Box` väljub ulatusest, vabastab ta automaatselt kuhja mälu. See automaatne puhastamine hoiab ära mälulekked, ilma et oleks vaja käsitsi mälu hallata.


Üks tähtsamaid "Kasti" kasutusjuhtumeid on rekursiivsete andmestruktuuride võimaldamine. Mõelgem lingitud loendile, kus iga sõlm sisaldab väärtust ja näitajat järgmisele sõlmpunktile. Ilma `Box`ita ei saa sellist struktuuri defineerida, sest kompilaator ei saa määrata iseennast sisaldava tüübi suurust. Kasutades `Box<Node>` järgmise osuti jaoks, lahendate rekursiivse suuruse probleemi, sest `Box`il` on teadaolev, fikseeritud suurus, sõltumata sellest, mida ta sisaldab.


### Deref-traidi rakendamine


Tunnus `Deref` lubab tüüpi dereferentsida operaatori `*` abil, muutes nutikad osutajad käituma nagu viited sisalduvatele andmetele. Kui te rakendate `Deref` targa osuti jaoks, lubate automaatse dereferentsi, mis muudab targa osuti kasutamise läbipaistvaks. See tähendab, et te võite kutsuda meetodid sisalduvale tüübile otse läbi aruka osuti ilma selgesõnalise dereferentseerimiseta.


Tunnus `Deref` määratleb seotud tüübi `Target`, mis määrab, millist tüüpi viide peaks tuletamise operatsioon andma. Tunnus nõuab meetodi `deref` rakendamist, mis tagastab viite sihttüübile. Rakenduse `Box<T>` puhul tagastab implementatsioon viite sisalduvale `T` väärtusele.


Rust teostab automaatset deref coercion'i, mis tähendab, et kompilaator saab automaatselt sisestada `deref'i' üleskutse, kui see on vajalik, et muuta tüübid ühilduvaks. Seetõttu võite anda `String` funktsiooni, mis ootab `&str` - kompilaator automaatselt derefitseerib `String`i, et saada stringilõik. See sundimine võib olla mitmetasandiline, nii et `Box<String>` saab automaatselt konverteerida `&str`-ks mitme deref-operatsiooni kaudu.


### Custom Drop rakendamine


Tunnus `Drop` võimaldab teil määrata kohandatud puhastamise koodi, mis käivitub, kui väärtus läheb väljapoole ulatust. See on eriti oluline intelligentsete osutajate puhul, mis haldavad ressursse, mis lähevad kaugemale lihtsast mälust, näiteks failikäepidemed, võrguühendused või viidearvud. Tunnusel `Drop` on üks meetod, `drop`, mis võtab muutuva viite `self` ja teostab puhastamise.


Enamik tüüpe ei vaja kohandatud `Drop` rakendusi, sest Rust tegeleb automaatselt nende väljade eemaldamisega. Kuid nutikad näitajad vajavad sageli kohandatud loogikat, et nende hallatavad ressursid korralikult ära koristada. Näiteks viitega loendatud arukas osutaja peab viide loendust vähendama ja potentsiaalselt vabastama jagatud andmed, kui viimane viide langeb.


Saate väärtuse ka selgesõnaliselt välja jätta, enne kui see väljub ulatusest, kasutades `std::mem::drop()`. See funktsioon võtab väärtuse omandiõiguse ja laseb selle kohe maha, mis võib olla kasulik ressursside varaseks vabastamiseks või selle tagamiseks, et puhastamine toimuks teie programmi konkreetses punktis. Eksplitsiitne drop-funktsioon on lihtsalt identiteedifunktsioon, mis võtab omandiõiguse - tegelik töö toimub siis, kui väärtus funktsiooni lõpus maha jäetakse.


See sulgemiste, iteraatorite ja nutikate osutajate vundament annab Rust arendajatele vahendid väljendusrikka, turvalise ja tõhusa koodi kirjutamiseks. Need funktsioonid töötavad koos, et võimaldada ühiseid programmeerimismustreid, säilitades samal ajal Rust põhilised mälu turvalisuse ja jõudluse garantiid.



## Viidete lugemine ja sisemine muutuvus

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Viitelugemine RC-ga


Viitelugemine kujutab endast Rusts veel üht põhilist tüüpi arukat osutajat, mis on spetsiaalselt loodud mitme omaniku stsenaariumi võimaldamiseks. Erinevalt Boxist, mis järgib traditsioonilisi ühe omaniku reegleid, kus andmed kuuluvad ühele üksusele, võimaldab RC (Reference Counter) mitmel teie koodi osal jagada üheaegselt samade andmete omandiõigust. See jagatud omandiõiguse mudel töötab loendusmehhanismi kaudu, mis jälgib, kui palju viiteid on konkreetsele andmestikule olemas.


Võrdlusloendussüsteem töötab sisemise loenduri abil, mis suureneb iga kord, kui kloonid RC-i, ja väheneb, kui RC-i loobutakse. Mälu vabastatakse alles siis, kui see loendur jõuab nullini, tagades, et andmed jäävad kehtima nii kaua, kui mõni viide on olemas. Selline lähenemine takistab enneaegset deallokatsiooni, võimaldades samal ajal paindlikke andmete jagamise mustreid, mis oleks võimatu lihtsa Boxi omandiõiguse korral.


Praktiline näide, kus RC on kasulik, hõlmab ühiste andmestruktuuride, näiteks lingitud loendite loomist, kus mitu loendit võivad viidata samale sabaosale. Mõelgem sellele, et püüame luua kaks eraldi nimekirja, mis mõlemad viitavad ühisele alamjärjele. Boxi omandiõiguse korral muutub see võimatuks, sest jagatud osa viimine esimesse loendisse annab üle omandiõiguse, takistades selle kasutamist teises loendis. RC lahendab selle probleemi, võimaldades kloonida viite, mitte aga aluseks olevaid andmeid, mis teeb ühise struktuuri võimalikuks, säilitades samas mälu turvalisuse.


Kui kloonid RC-i, ei dubleeri sa sisemisi andmeid, olenemata nende suurusest või keerukusest. Selle asemel loote te teise viite samale mälukohale ja suurendate viite loendurit. See muudab RC-instantside kloonimise tõhusaks isegi suurte andmestruktuuride puhul, kuna ainult viide ise kopeeritakse, samas kui aluseks olevad andmed jäävad alles.


### RefCelli sisemine muutuvus


RefCell toob sisse sisemise muutuvuse, mis võimaldab andmeid muuta isegi siis, kui teil on ainult muutumatu viide sellele. See võime muudab põhimõtteliselt Rust laenutusreeglite jõustamist, viies kontrollimise kompileerimisajast jooksutusajale. Kui tavalised viited tuginevad kompilaatorile, et kontrollida laenamise turvalisust, siis RefCell teostab need kontrollid programmi täitmise ajal, pakkudes suuremat paindlikkust võimalike tööaegsete paanikate hinnaga.


RefCelli põhiprintsiip hõlmab samade laenutusreeglite säilitamist, mida Rust tavaliselt rakendab kompileerimise ajal, kuid kontrollib neid dünaamiliselt. Igal ajahetkel võib RefCelli sees olla kas üks muutuv viide või suvaline arv muutumatuid viiteid andmetele. Kui teie kood üritab neid reegleid rikkuda, luues samaaegselt vastuolulisi laenutusi, satub programm paanikasse, mitte ei tekita määratlemata käitumist.


See tööaja kontroll võimaldab teatud programmeerimismustreid, mida kompilaator võib tagasi lükata isegi siis, kui need on tegelikult turvalised. Kompilaatori staatiline analüüs ei saa alati tõestada, et keerulised laenutusmustrid on õiged, mistõttu ta kaldub ettevaatlikkuse poole. RefCell võimaldab teil need konservatiivsed piirangud kõrvale jätta, kui olete kindel oma koodi korrektsuses, kuid selle kindlusega kaasneb kohustus tagada õige kasutamine, et vältida jooksutusaegseid tõrkeid.


RefCelli tavaline kasutusjuhtum hõlmab mock-objekte testimisstsenaariumides. Kui rakendate tunnuse, mis pakub ainult muutumatut ligipääsu iseendale, kuid teie mõnituse rakendamine peab jälgima oleku muutusi sisemiselt, võimaldab RefCell seda mustrit. Saate sisemise oleku mähendada RefCelliga, mis võimaldab mockil muuta oma jälgimisandmeid isegi muutumatu liidese kaudu.


### RC ja RefCell kombineerimine jagatud muutuva oleku jaoks


RC ja RefCell kombinatsioon loob mustri jagatud muutuva oleku jaoks, kus mitu omanikku võivad kõik potentsiaalselt muuta samu andmeid. RC pakub jagatud omandiõiguse võimalust, samal ajal kui RefCell võimaldab mutatsiooni muutumatute viidete kaudu. See kombinatsioon on kasulik sellistes stsenaariumides nagu graafistruktuurid, vahemälud või mis tahes olukorras, kus programmi mitu osa vajavad nii lugemis- kui ka kirjutamisjuurdepääsu jagatud andmetele.


Kui pakendate RefCelli RC-i sisse, loote struktuuri, mida saab kloonida ja jaotada kogu programmis, kusjuures iga kloon annab ligipääsu samadele muutuvatele alusandmetele. Kõik omanikud saavad potentsiaalselt andmeid muuta, kasutades RefCelli meetodit borrow_mut, kuid nad peavad siiski järgima laenutusreegleid tööajal. See muster võimaldab keerulisi andmete jagamise stsenaariume, säilitades samal ajal Rust turvagarantiid jooksuaegsete kontrollide kaudu.


Sellise paindlikkusega kaasnevad aga olulised hoiatused seoses mälulekete ja viitamistsüklitega. Kui kasutatakse RC koos RefCelliga, on võimalik kogemata luua ringviiteid, kus andmestruktuurid viitavad iseendale kas otse või viidete ahela kaudu. Need tsüklid takistavad viitamiste arvu kunagi nullini jõudmist, põhjustades mälulekkeid, sest andmetel näib olevat alati aktiivseid viiteid, isegi kui need ei ole ülejäänud programmist enam ligipääsetavad.


Viitetsüklite lahendus hõlmab nõrkade viidete kasutamist, mis ei osale mäluhalduse otsuste tegemisel kasutatavas viidete arvus. Nõrgad viited võimaldavad säilitada ühendusi andmestruktuuride vahel ilma neid elus hoidmata, katkestades potentsiaalsed tsüklid, säilitades samal ajal võimaluse pääseda ligi seotud andmetele, kui need on veel olemas.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### Niiditurvalisuse ja samaaegsuse alused


Rust lähenemisviis samaaegsusele keskendub andmete võidujooksude ja mälu turvalisuse probleemide vältimisele kompileerimise ajal. Tüüpsüsteem tagab niiditurvalisuse selliste tunnuste nagu `Send` ja `Sync` kaudu, mis märgivad tüübid vastavalt niitide vaheliseks ülekandmiseks või samaaegseks juurdepääsuks turvaliseks. Selline kompileerimise ajaline kontroll avastab paljud samaaegsusvead, mis teistes süsteemiprogrammeerimiskeeltes ilmneksid alles tööajal.


Niitide loomine Rust-s järgib lihtsat mustrit, kasutades thread::spawn, mis võtab uues niidis täidetava sulgemise ja tagastab käepideme niidi elutsükli haldamiseks. Loodud lõim töötab samaaegselt põhilõngaga ning käepidemega saab kasutada join-meetodit, et oodata lõpetamist. Ilma selgesõnalise liitmiseta võib loodud lõim lõpetada, kui peamine lõim väljub, mis võib katkestada pooleli jäänud töö.


Märksõna move muutub niidiga töötamisel väga oluliseks, sest sulgemised, mis on edastatud genereeritud niidile, peavad sageli oma andmeid omama, mitte neid laenama. Kuna loodud lõimed võivad elada kauem kui nende looja, tekitab nende laenamine vanematest lõimedest võimalikke eluea rikkumisi. Andmete teisaldamine lõime sulgemisele annab omandiõiguse üle, tagades, et andmed jäävad kehtima kogu lõime eluea jooksul, takistades samal ajal juurdepääsu algsest ulatusest.


Sõnumite edastamine pakub alternatiivi jagatud olekuga samaaegsusele kanalite kaudu, mis võimaldavad lõimedel suhelda pigem andmete saatmise kui mälu jagamise teel. Rust standardraamatukogu pakub Multiple Producer Single Consumer (MPSC) kanaleid, kus mitu niiti saavad saata sõnumeid ühele vastuvõtvale niidile. See muster kõrvaldab paljud sünkroniseerimisprobleemid, vältides täielikult jagatud muutuva oleku kasutamist, tuginedes selle asemel koordineerimiseks sõnumite vahetamisele.


### Jagatud oleku samaaegsus Mutexi ja Arciga


Kui sõnumite edastamine ei sobi, pakub Rust traditsioonilist jagatud oleku samaaegsust Mutexi (vastastikuse välistamise) ja Arc'i (Atomic Reference Counter) abil. Mutex tagab, et korraga saab kaitstud andmetele ligi ainult üks niit, nõudes, et niidid omandaksid enne andmetele ligipääsu lukustuse. Lukk vabastatakse automaatselt, kui lukustusoperatsiooni poolt tagastatud kaitseobjekt läheb väljapoole ulatust, vältides sellega tavalisi ummikseisustsenaariume, mida põhjustavad unustatud lukustused.


Arc on RC-i niidikindel ekvivalent, mis kasutab aatomioperatsioone, et hallata viidearvu turvaliselt mitme niidi vahel. Kuigi RC töötab suurepäraselt ühe niidi stsenaariumide puhul, tekitab selle mitte-atomaarne viitelugemine võistlustingimusi, kui seda kasutatakse mitmest niidist. Arc'i atomaarsed loendurid tagavad, et viidete arvu muutmine toimub ohutult ka samaaegse juurdepääsu korral, mistõttu sobib see andmete jagamiseks üle niidipiiride.


Arc'i ja Mutexi kombinatsioon loob mustri jagatud muutuva oleku jaoks samaaegsetes programmides. Mutexi mähkimisega Arc'ile saab Arc'i kloonida, et jaotada ligipääs samale mutexile mitme niidi vahel, kusjuures iga niit saab lukustust omandada ja kaitstud andmeid turvaliselt muuta. See muster pakub jagatud oleku paindlikkust, säilitades samal ajal Rust ohutustagatised kompileerimisajal kontrollimise ja jooksuaegse lukustuse kaudu.


Tunnused Send ja Sync töötavad kulisside taga, et tagada niiditurvalisus kompileerimise ajal. Send näitab, et tüüpi saab turvaliselt teisele niidile üle kanda, samas kui Sync näitab, et viiteid tüübile saab turvaliselt jagada niitide vahel. Enamik tüüpe rakendab neid omadusi automaatselt, kui nende komponendid on niidikindlad, kuid mõned tüübid nagu RC ja RefCell ei rakenda neid automaatselt, sest nad ei ole mõeldud samaaegseks juurdepääsuks. See automaatne tunnuse implementatsioon takistab juhuslikku niiditurvalisuse rikkumist, võimaldades samal ajal turvalistel tüüpidel tõrgeteta töötada samaaegsetes kontekstides.


## Rust makrode mõistmine

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Sissejuhatus makrode Rust-sse


Rust makrod on metaprogrammeerimise funktsioon, mis võimaldab arendajatel kirjutada koodi, mis genereerib teisi koode kompileerimise ajal. Erinevalt funktsioonidest, mida kutsutakse tööajal, laiendatakse makrosid kompileerimisprotsessi alguses, enne tüübikontrolli ja hilisemat faasi. See põhimõtteline erinevus muudab makrod eriti kasulikuks koodi kordamise vähendamiseks ja Rust programmides valdkonnapõhiste keelte loomiseks.


Makrokõne kõige paremini äratuntavaks märgiks on makronime järel olev hüüumärk (!). Näiteks, kui kasutate `println!("Hello, world!")`, siis ei kutsu te funktsiooni, vaid kutsute üles makrot. See makro laieneb keerulisemaks koodiks, mis tegeleb vormindamise ja väljundoperatsioonidega. Hüüumärk on arendajatele visuaalseks märguandeks, et tegemist on kompileerimisajal koodi genereerimisega, mitte tavalise funktsioonikõne tegemisega.


Rust pakub kolme erinevat tüüpi makrosid, millest igaühel on keele ökosüsteemis erinev otstarve:



- Funktsioonilaadsed makrot**: Sarnanevad funktsioonikõnedega, kuid toimivad kompileerimise ajal (nt `vec!`, `println!`)
- Makrode tuletamine**: Tüüpide tunnuste automaatne rakendamine (nt `#[derive(Debug, Clone)]`)
- Atribuudilaadsed makrotunnused**: Muudavad nende koodielementide käitumist, millele neid rakendatakse (nt `#[test]`, `#[tokio::main]`)


Nende erinevate makrotüüpide mõistmine on tõhusaks Rust programmeerimiseks hädavajalik, sest iga makro on suunatud konkreetsetele kasutusjuhtumitele ja programmeerimismustritele.


### Makrode tüübid ja nende rakendused


Funktsioonilaadsed makrotüübid on Rust programmeerimisel kõige sagedamini esinev makrotüüp. Need makros kasutavad funktsiooni kutsega sarnast süntaksit, kuid viivad oma sisendil generate sobiva koodi suhtes läbi mustri sobitamise. Makro `vec!` on selle kategooria tavaline näide, mis võimaldab arendajatel luua ja initsialiseerida vektoreid lühikese süntaksiga. Kui kirjutate `vec![1, 2, 3, 4]`, laiendab makro selle koodiks, mis loob uue vektori, lükkab iga elemendi eraldi ja tagastab valmis vektori.


Derive-makrosid pakuvad automaatset omaduste rakendamist kohandatud tüüpide jaoks, vähendades oluliselt katlakoodi. Kui lisate `#[derive(Debug)]` struktuuri või enumi definitsioonile, annate kompilaatorile korralduse generate jaoks selle tüübi Debug-traidi täielikuks rakendamiseks. See genereeritud implementatsioon tegeleb vormindusloogikaga, mis on vajalik tüübi sisu kuvamiseks inimesele loetavas formaadis. Derive-mehhanism toetab mitmeid standardseid raamatukogu tunnuseid, sealhulgas Clone, PartialEq, mistõttu on see üldkasutatav vahend boilerplate'i vähendamiseks.


Atribuudilaadsed makrotunnused muudavad nende koodielementide käitumist, mida nad kommenteerivad, pakkudes võimalust lisada metaandmeid või muuta kompileerimise käitumist. Need makros ilmuvad atribuutidena, mis on paigutatud tüübimääratluste, funktsioonide või muude koodikonstruktsioonide kohale. Näiteks atribuut `#[non_exhaustive]` enumil näitab, et tulevastes versioonides võidakse lisada täiendavaid variante, nõudes, et sobitusavaldused sisaldaksid vaikimisi juhtumit. See mehhanism tagab edasiühilduvuse, pakkudes samas selget dokumentatsiooni tüübi arengupotentsiaali kohta.


### Kohandatud funktsioonilaadsete makrode loomine


Kohandatud funktsioonilaadsete makrode kirjutamine eeldab Rust makrodefinitsioonide süntaksi mõistmist. Makrode määratlemisel kasutatakse deklaratiivset lähenemist, kus te määrate mustrid, mis vastavad erinevatele sisendvormidele ja vastavatele koodi genereerimise mallidele. Iga makro võib sisaldada mitut haru, mis võimaldab tal käsitleda erinevaid sisendmustreid ja generate igale juhtumile vastavat koodi.


Kaaluge kohandatud vektormakro loomist, mis demonstreerib makrokonstruktsiooni põhiprintsiipe. Makro definitsioon algab sõnaga `macro_rules!`, millele järgneb makro nimi ja rida mustritele vastavaid harusid. Iga haru koosneb mustrist, mis vastab konkreetsele sisendsüntaksile, ja koodimustrist, mis genereerib vastava Rust koodi. Näiteks võib lihtne haru sobida tühjade sulgude `[]` ja generate koodiga, et luua tühi vektor, samas kui teine haru sobib ühe väljendi jaoks ja genereerib koodi, et luua ühe elemendiga vektor.


Eriti kasulikuks muutuvad makrod, kui rakendatakse muutuja argumentide mustreid, kasutades kordussüntaksit. Muster `$($x:expr),*` vastab nullile või mitmele komadega eraldatud väljenditele, mis võimaldab makroga käsitleda suvalist arvu argumente. Vastav koodi genereerimise mall kasutab `$(vec.push($x);)*`, et itereerida kõigi vastavate väljendite üle ja generate üksikute push-avalduste jaoks. See kordusmehhanism võimaldab makrode generate koodi, mida oleks võimatu või äärmiselt mahukas käsitsi kirjutada.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


Kompileerimisprotsess muudab makrokutsed laiendatud koodiks enne tüübikontrolli ja optimeerimist. Kui kompilaator kohtab makrokutse, võrdleb ta sisendit määratletud mustritega ja asendab makrokutse genereeritud koodiga. Seejärel läbib see laiendatud kood tavalise kompileerimisprotsessi, sealhulgas tüübikontrolli ja optimeerimise. Tööriistad nagu `cargo expand` võimaldavad arendajatel kontrollida genereeritud koodi, mis annab keerukate makrode arendamisel väärtuslikke silumisvõimalusi.


### Täiustatud makrokontseptsioonid ja vigade kõrvaldamine


Makrode arendamine nõuab, et mõistetaks vahet kompileerimis- ja tööaegse täitmise vahel. Makros täidetakse kompileerimise ajal, genereerides koodi, mis käivitatakse tööajal. Selline ajaline eraldamine tähendab, et makroloogika ei saa sõltuda tööaegsetest väärtustest, kuid see võimaldab ka optimeerimist, kus keerulisi arvutusi saab teha üks kord kompileerimise ajal, mitte korduvalt täitmise ajal.


Makrosüsteem toetab erinevaid fragmentide spetsifikaatoreid, mis määravad, millist tüüpi koodielemente saab sobitada. Spetsifikaator `expr` vastab väljenditele, `ty` vastab tüüpidele, `ident` vastab identifikaatoritele ja mitmed teised pakuvad peenemat kontrolli sisendi valideerimise üle. Need spetsifikaatorid tagavad, et makros saavad süntaktiliselt korrektse sisendi ja annavad selgeid veateateid, kui kohtuvad valesti süntaksiga.


Makrode silumine on nende kompileerimise ajalise olemuse tõttu ainulaadne probleem. Käsk `cargo expand` on kasulik makrode arendamisel, kuna see kuvab makrode kutsumisel genereeritud täielikult laiendatud koodi. See tööriist võimaldab arendajatel kontrollida, et nende makrode generate on kavandatud kood ja tuvastada probleeme laiendamisloogikas. Kui makroga genereeritud kood sisaldab vigu, aitab laiendatud väljund täpselt kindlaks teha, kas probleem on makrodefinitsioonis või genereeritud koodi struktuuris.


Komplekssed makrot võivad rakendada rekursiivseid mustreid, kus makro kutsub end iseenda muudetud argumentidega, et käsitleda sisendatud või iteratiivset koodi genereerimist. Rekursiivsed makros nõuavad siiski hoolikat kavandamist, et vältida lõpmatut laiendamist ja kompileerimise jõudlusprobleeme. Makrode laiendamise laad tähendab, et isegi ebatõhusad makrode rakendused mõjutavad ainult kompileerimise kiirust, mitte aga tööeaegset jõudlust, kuid liiga keerulised makrod võivad oluliselt aeglustada koostamisprotsessi.



# Rust & Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Miks Rust Bitcoin arendamiseks

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


Rust valik Bitcoin ja Lightningi arendamiseks ei ole juhuslik. Bitcoin arendamisega kaasnevad ainulaadsed kohustused, mis eristavad seda tavapärasest tarkvaraarendusest. Bitcoin-ga töötades tegelevad arendajad sageli kasutajate rahaliste vahenditega keskkonnas, kus vead võivad olla pöördumatud. Erinevalt traditsioonilistest finantssüsteemidest, millel on regulatiivsed kaitsemeetmed ja tagastamismehhanismid, tähendab Bitcoin detsentraliseeritud olemus, et kui tehing on eetrisse läinud, ei ole asutust, kelle poole pöörduda raha tagasisaamiseks. See reaalsus nõuab suuremat vastutust ja täpsust tarkvaraarenduses.


Paljudes tehnoloogiasektorites toimiv "liigu kiiresti ja lõhu asju" filosoofia lihtsalt ei kehti Bitcoin arenduse puhul. Selle asemel on ökosüsteemis vaja keeli ja vahendeid, mis aitavad arendajatel luua töökindlat ja turvalist tarkvara, kus vead kas välditakse või neid käsitletakse väärikalt. Seepärast on paljud silmapaistvad Bitcoin projektid, sealhulgas Bitcoin arenduskomplekt (BDK), Lightning Development Kit (LDK) ja BreezSDK, liikunud Rust suunas.


Rust pakub kolme olulist omadust, mis muudavad selle Bitcoin arendamiseks eriti sobivaks: staatiline tugev tüübisüsteem, rikkalik kaasaegne tööriistade valik ja platvormideülene ühilduvus. Kõik need omadused aitavad kaasa keele võimele aidata arendajatel kirjutada turvalisemat ja usaldusväärsemat koodi krüptorahaoperatsioonide töötlemiseks.


### Rust staatiline tugevat tüüpi süsteem


Rust tüübisüsteem pakub nii staatilist kui ka tugevat tüübistamist, mis töötavad koos, et tabada vead enne, kui need saavad kasutajat mõjutada. Staatiline olemus tähendab, et tüübikontroll toimub kompileerimise ajal, mis nõuab arendajatelt tüübivigade lahendamist juba enne programmi koostamist. See on vastuolus dünaamiliselt tüpiseeritud keeltega, kus tüübivigad ilmnevad alles tööajal, potentsiaalselt pärast seda, kui tarkvara on kasutusele võetud ja tegelikke kasutajarahasid käitleb.


Rust tüübisüsteemi tugevus viitab selle väljendusrikkusele ja rangusele probleemide modelleerimisel. Erinevalt nõrgemate tüübisüsteemidega keeltest, nagu C, kus arendajad on piiratud selliste põhitüüpidega nagu numbrid ja struktuurid, võimaldab Rust rikkalikku tüübimodelleerimist, millega saab täpselt esitada keerukaid valdkondlikke mõisteid. Näiteks saab luua tüüpe, mis eristavad eri liiki loendeid või kehtestavad, et teatud operatsioone tehakse ainult teatud objektitüüpidega.


Rust tüübisüsteem on Bitcoin arendamisel oluline tänu selle lähenemisviisile mälu turvalisusele. Sama tüüpsüsteem, mis modelleerib äriloogikat, tegeleb ka mälu omandiõiguse ja ühise juurdepääsu kontrolliga. See topeltvastutus tähendab, et tavalised haavatavuste klassid, nagu mälulekked, topeltvabad vead ja võistlustingimused, on kompilaatori poolt täielikult kõrvaldatud. Tüübisüsteem tagab need turvagarantiid selliste mõistete nagu omandiõigus, laenamine ja viitelugemine abil, mistõttu on äärmiselt raske lisada mäluga seotud vigu, mis võiksid ohustada turvalisust või stabiilsust.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Kaasaegsed tööriistad ja platvormideülene tugi


Rust tööriistade ökosüsteem pakub arendajatele vahendeid, mis aitavad tootlikkust ja koodi kvaliteeti parandada. Rust kompilaator ise ei ole mõeldud mitte ainult koodi binaarseks tõlkimiseks, vaid ka õppevahendiks, mis aitab arendajatel õppida ja areneda. Kompileerimisvigade ilmnemisel annab kompilaator üksikasjalikud selgitused selle kohta, mis läks valesti, ja soovitab sageli konkreetseid parandusi. Selline lähenemine on eriti väärtuslik Rust-ga alustavatele arendajatele, sest kompilaator õpetab tõhusalt häid tavasid ja aitab vältida tavalisi vigu.


Keel sisaldab Cargo, ühtset paketihaldurit, mis tegeleb sõltuvuste haldamise, koostamise, testimise ja dokumentatsiooni koostamisega. Selline standardiseerimine välistab vanemate keelte, nagu C++, killustatuse, kus mitmed konkureerivad tööriistad tekitavad projektides vastuolusid. Cargo toetab ka selliseid laiendusi nagu rustfmt koodi vormindamiseks ja Clippy staatiliseks analüüsiks, tagades, et kood järgib järjepidevaid stiilijuhiseid ja avastab võimalikud probleemid enne, kui need probleemideks muutuvad.


Rust platvormideülesed võimalused ulatuvad traditsioonilistest operatsioonisüsteemidest kaugemale, hõlmates ka mobiiliplatvorme nagu Android ja iOS, samuti WebAssembly'd brauseripõhiste rakenduste jaoks. Selline platvormideülene tugi on kasulik Bitcoin rakenduste puhul, mis peavad töötama erinevates keskkondades. Näiteks projektid nagu Mutiny Wallet kasutavad Rust WebAssembly'i kompileerimist, et luua otse veebibrauserites töötavaid Lightning-rahakotte, mis oleks traditsiooniliste veebitehnoloogiate puhul ainuüksi ebapraktiline.


### Veatüüpide ja nende tagajärgede mõistmine


Tõhus veatöötlus algab programmi täitmise ajal tekkida võivate vigade eri kategooriate mõistmisest. Võtame näiteks lihtsa marsruutimisrakenduse, mis arvutab marsruute geograafiliste punktide vahel. See näide illustreerib kolme põhilist veatüüpi, millega arendajad peavad tegelema: valed sisendvead, tööaja ressursivigad ja loogikavead.


Vale sisendvead tekivad siis, kui funktsioon saab parameetrid, mis ei vasta selle nõuetele. Näiteks kui geograafilises koordinaatsüsteemis kasutatakse pikkuskraadiks täisarvu, kuid funktsioon saab negatiivse väärtuse, mille puhul kehtivad ainult positiivsed väärtused, siis ei saa funktsioon mõtestatult jätkata. Need vead kujutavad endast lepingu rikkumist kutsuja ja funktsiooni vahel ning asjakohane vastus on tavaliselt sisendi tagasilükkamine ja veateate tagastamine.


Käitusaegsed ressursivigad tekivad siis, kui välised sõltuvused ei ole kättesaadavad või ligipääsmatu. Kaardifaili lugemine võib ebaõnnestuda, sest faili ei ole olemas, rakendusel puuduvad õiged õigused või mäluseade ei ole kättesaadav. Need vead on programmiloogikast välised ja nõuavad sageli pigem keskkonna parandamist kui koodi muutmist. Siiski peavad töökindlad rakendused neid stsenaariume ette nägema ja neid graatsiliselt käsitlema.


Loogikavead kujutavad endast vigu programmi rakendamisel või arusaamatusi komponentide koostoimimisest. Kui marsruutimisalgoritm tagastab tühja tee, kui talle on antud õiged algus- ja lõpp-punktid, näitab see loogilist viga, mis tuleb parandada koodis endas. Erinevalt teistest veatüüpidest nõuavad loogikavead tavaliselt silumist ja koodi muutmist, et neid lahendada.


### Robustse veahalduse strateegiad


Usaldusväärse tarkvara loomine nõuab ennetavaid strateegiaid, mis vähendavad vea võimalusi ja käitlevad vältimatuid vigu graatsiliselt. Esimene strateegia hõlmab võimalike vigade piiramist hoolika tüübidisaini abil. Valides tüübid, mis võivad esindada ainult kehtivaid väärtusi, saavad arendajad kõrvaldada terved kehtetute sisendvigade klassid. Näiteks, kui kasutatakse täisarvusid, mille väärtus ei saa olla negatiivne, välditakse negatiivse väärtuse vigu kompileerimise ajal.


Väited pakuvad veel ühe kaitsekihi, kontrollides selgesõnaliselt, et oodatavad tingimused on programmi täitmise ajal tõesed. Need kontrollid täidavad mitut eesmärki: nad püüavad testimise käigus vigu, põhjustavad probleemide ilmnemisel programmide varajase ebaõnnestumise (mis lihtsustab vigade kõrvaldamist) ja on käivitatav dokumentatsioon, mis kirjeldab programmeerija eeldusi. Kui väide ebaõnnestub, näitab see, et programmi oleku kohta tehtud põhieeldus on rikutud, mis tavaliselt viitab loogikavigale, mida tuleb uurida.


Kihiliste abstraktsioonide põhimõte aitab hallata keerukust, tagades, et vigu käsitletakse süsteemi asjakohastel tasanditel. Sisemise rakendamise üksikasjad, sealhulgas spetsiifilised veatüübid madalama taseme raamatukogudest, ei tohiks levida allsüsteemi piiridest kaugemale. Selle asemel peaks iga kiht tõlkima vead terminiteks, mis on antud abstraktsioonitasemel mõttekad. Näiteks wallet rakendus, mis kasutab Bitcoin raamatukogu, peaks tõlkima madalama tasandi kirjelduse parsimisvead kõrgemal tasemel teadeteks nagu "kehtetu wallet konfiguratsioon", mis annavad kasutajatele või kutsuvale koodile rakendatavat teavet.


Selline lähenemine veakäitlusele koos Rust tüübisüsteemi ja tööriistadega aitab võimalikke probleeme avastada juba arendusprotsessi alguses, enne kui need võivad mõjutada kasutajaid või ohustada Bitcoin rakenduste turvalisust.



## Veamudel

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust pakub terviklikku lähenemist veakäsitlusele, mis tasakaalustab ohutuse ja praktilisuse. Kuigi üldised veamudeli kontseptsioonid kehtivad kõigis programmeerimiskeeltes, pakub Rust konkreetseid vahendeid ja mustreid, mis muudavad veakäitluse nii selgesõnaliseks kui ka hallatavaks. Nende mehhanismide mõistmine on oluline, et kirjutada töökindlaid Rust rakendusi, mis suudavad ootamatuid olukordi graatsiliselt käsitleda, säilitades samas jõudluse ja ohutuse.


### Paanika ja selle asjakohane kasutamine


Rust paanikamehhanism kujutab endast kõige otsesemat viisi taastamatute vigade käsitlemiseks. Makro `panic!` väljakutsumisel peatab programm kohe täitmise, kas katkestades või lahti kerides, sõltuvalt teie konfiguratsioonist. Paanikamakro võtab vastu string-teate, mis kirjeldab, mis läks valesti, pakkudes konteksti silumiseks. Lisaks on meetodid nagu `unwrap()` ja `expect()` Result ja Option tüüpidel paanika otseteedeks, kui need tüübid sisaldavad vastavalt veaväärtusi või None. Meetod `expect()` võimaldab teil anda kohandatud sõnumi, mis teeb selle veidi informatiivsemaks kui `unwrap()` vigade silumiseks.


Vaatamata oma lihtsusele, tuleks paanikat tootekoodis kasutada mõistlikult. On mitmeid stsenaariume, kus paanika on mitte ainult vastuvõetav, vaid soovitatav. Näidete või prototüüpide kirjutamisel annab paanika puhta võimaluse keskenduda põhifunktsionaalsusele, ilma et kood oleks koormatud ulatusliku veakäsitlusega. Testimiskeskkondades on paanika sageli soovitud käitumine, kui kinnitused ebaõnnestuvad, sest see näitab selgelt, et midagi ootamatut on toimunud. Rust kogukond tunnistab ka olukordi, kus arendajatel on rohkem teadmisi kui kompilaatoril, näiteks kui parsitakse kõvasti kodeeritud IP-aadresse, mis on teadaolevalt kehtivad.


Kuid "kompilaatori poolt kontrollitud" paanika näiline ohutus võib olla petlik. Mõelge stsenaariumile, kus te programmeerite IP-aadressi ja kasutate `expect()`, sest teate, et see on kehtiv. Aja jooksul, kui kood areneb, võib see kõvasti kodeeritud väärtus muutuda konstandiks ja hiljem võib see konstant muutuda millekski nagu "localhost", et parandada kasutajakogemust. Järsku muutub teie "turvaline" paanika jooksuaegseks veaks. See areng näitab, miks on üldiselt parem vältida paanikat tootekoodis ja selle asemel tagastada sobivaid veatüüpe, mida saab graatsiliselt käsitleda.


Üks märkimisväärne erand reeglist "väldi paanikat" hõlmab mutex-operatsioone. Kui te kutsute `lock()` mutexile, siis tagastab see tulemuse, sest lukustus võib ebaõnnestuda, kui mõni teine niit paanikasse sattus, kui ta mutexi hoidis. See tekitab segadust tekitava olukorra, kus teie kohalik kood saab vea millegi eest, mis juhtus täiesti teises kontekstis. Kuna te ei saa mõistlikult käsitleda viga, mis pärineb teise niidi paanikast, peavad paljud arendajad mutexi lukkude lahtipakkimist vastuvõetavaks, eriti kui te säilitate paanikavaba koodibaasi mujal.


### Töötamine tulemuste ja valikute tüüpidega


Tulemuse tüüp moodustab Rust veakäitlussüsteemi selgroo. Kuna Result on enum, mis võib sisaldada kas `Ok(väärtus)` või `Err(viga)`, sunnib Result teid selgesõnaliselt tunnistama, et operatsioonid võivad ebaõnnestuda. Tüüp Option täidab sarnast eesmärki juhtudel, kus väärtus võib lihtsalt puududa, sisaldades kas `Some(value)` või `None`. Kuigi Option ei anna üksikasjalikku veateavet, sobib see suurepäraselt olukordadesse, kus väärtuse puudumine on mõttekas ja oodatud.


Nii Result kui ka Option pakuvad mitmeid kasulikke meetodeid, mis muudavad veakäitluse ergonoomilisemaks. Meetod `unwrap_or()` tagastab sisalduva väärtuse, kui see on olemas, või vaikeväärtuse, kui on viga või None. See muster on eriti kasulik, kui teil on mõistlik varuvariant, näiteks kasutaja sisendi analüüsimisel mõistliku vaikimisi väärtusega, kui analüüs ei õnnestu. Meetod `unwrap_or_default()` töötab sarnaselt, kuid kasutab tüübi vaikeväärtust selle asemel, et nõuda selle määramist. Kuigi need meetodid ei käsitle tehniliselt vigu traditsioonilises mõttes, pakuvad nad võimalust funktsionaalsuse graatsiliseks vähendamiseks probleemide ilmnemisel.


Küsimärgi operaator (`?`) on lühike süntaks vea propageerimiseks. Kui seda rakendatakse tulemuse või valiku suhtes, võtab see välja edevuse väärtuse, kui see on olemas, või tagastab kohe vea praeguse funktsiooni, kui esineb probleem. See operaator kõrvaldab keelte nagu Go puhul levinud laialivalguvad veakontrolli mustrid, kus tuleb käsitsi kontrollida ja tagastada vigu igal sammul. Küsimärgi operaator annab sisuliselt süntaktilise suhkru varajase tagastamise jaoks, mis võimaldab kirjutada puhast, lineaarset koodi, mis keskendub õnnelikule teele, käsitledes samal ajal automaatselt vigade levikut.


### Täiustatud veakäitluse mustrid


Meetod `map()` tüübidele Result ja Option võimaldab funktsionaalses stiilis veakäitlust, mis võib muuta koodi väljendusrikkamaks ja komponeeritavamaks. Kui te kutsute `map()` result'ile, rakendatakse antud funktsiooni edevuse väärtusele, kui see on olemas, samas kui vead levivad automaatselt ilma muutusteta. See muster on kasulik operatsioonide aheldamisel, kuna saate keskenduda väärtuste teisendamisele ilma korduva veajuhtumite käsitlemiseta. Meetod `map_err()` pakub vastupidist funktsionaalsust, võimaldades teisendada veatüüpe, jättes edu väärtused muutmata.


Vigade ümberkujundamine muutub otsustavaks, kui ehitatakse mitmekihilisi rakendusi, kus erinevad komponendid vajavad erinevaid veatüüpe. Võtame näiteks funktsiooni, mis parseldab kasutaja sisendit ja peab teisendama madalatasemelised parsimisvead valdkonnapõhisteks vigadeks. Kasutades funktsiooni `map_err()`, saate hõlpsasti muuta üldise vea "kehtetu numbriformaat" kontekstipõhisemaks veaks "kehtetu vanus", mis on teie rakenduse domeenis mõistlik. See ümberkujundamine toimub otse vea tekkimise kohas, mis muudab koodi loetavamaks ja hooldatavamaks kui traditsioonilised try-catch-blokid, kus veakäitlus on eraldatud operatsioonidest, mis võivad ebaõnnestuda.


Küsimärgi operaatori ja vea kaardistamise kombinatsioon loob kokkuvõtlikud veakäitlusmustrid. Saate operatsioone aheldada, vigu vastavalt vajadusele teisendada ja neid minimaalse katlakiviga ülespoole kutsete virna levitada. Selline lähenemine hoiab veakäsitluse operatsioonide lähedal, mis võivad ebaõnnestuda, säilitades samal ajal puhta eraldatuse edu- ja veateede vahel.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Välised raamatukogud ja veakäitluse ökosüsteemid


Rust ökosüsteem sisaldab mitmeid populaarseid raamatukogusid, mis laiendavad standardraamatukogu veakäitlusvõimalusi. Raamatukogu `anyhow` pakub lihtsustatud lähenemist veakäsitlusele, pakkudes universaalset veatüüpi, mis suudab automaatselt teisendada mis tahes veatüübi, mis rakendab standardset veatunnust Error. See automaatne teisendamine võimaldab kasutada küsimärgioperaatorit erinevate veatüüpidega ilma käsitsi teisendamiseta, mis teeb selle eriti kasulikuks rakendustes, kus ei ole vaja programmiliselt eristada erinevaid veatüüpe.


Kuigi `anyhow` sobib suurepäraselt veakäitluse lihtsustamiseks rakendustes, kus vead kuvatakse peamiselt kasutajatele, on sellel piirangud raamatukogude arendamisel. Kuna `anyhow` teisendab kõik vead sisuliselt string-teadeteks, ei saa teie raamatukogu tarbijad lihtsalt programmiliselt reageerida erinevatele veatingimustele. See piirang muudab `anyhow` sobivamaks lõppkasutaja rakenduste jaoks kui raamatukogude jaoks, mis peavad andma oma tarbijatele struktureeritud veateavet.


Edasijõudnumad veakäsitlusviisid hõlmavad kohandatud veatüüpide loomist, mis modelleerivad teie rakenduse või raamatukogu spetsiifilisi veamooduseid. Hästi kavandatud veamudel võib eristada kehtetuid sisendeid (mida kutsuja saab parandada), tööaja vigu (mida võib uuesti proovida) ja püsivaid tõrkeid (mis näitavad vigu või parandamatuid tingimusi). Selline struktureeritud lähenemine võimaldab teie koodi tarbijatel teha arukaid otsuseid selle kohta, kuidas reageerida erinevat tüüpi vigadele, olgu see siis operatsioonide uuesti proovimine, kasutajate üleskutse teistsuguse sisendi saamiseks või vigadest teatamine arendajatele.


## UniFFI, Rust raamatukogude ühendamine mitme keelega


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### UniFFI ja platvormideülese arenduse tutvustus


UniFFI on vahend Rust raamatukogude kättesaadavaks tegemiseks mitmes programmeerimiskeeles ja platvormil. See Mozilla poolt välja töötatud vahend tegeleb tänapäevase tarkvaraarenduse põhiprobleemiga: kuidas kasutada Rust jõudluse ja ohutuse eeliseid, säilitades samal ajal ühilduvuse erinevate arendusökosüsteemide vahel. Tööriist genereerib Rust raamatukogude jaoks automaatselt keelekohastusi, kõrvaldades arendajate vajaduse luua iga sihtkeele jaoks käsitsi liidese kood.


Põhiprobleem, mille UniFFI lahendab, tuleneb Rust kui kompileeritud keele olemusest. Kui Rust kood kompileeritakse, toodab see binaarset väljundit koos Foreign Function Interface (FFI), mis esitab madala taseme liidese, mida võib olla keeruline kasutada otse kõrgema taseme keeltest, nagu Python, Swift või Kotlin. Traditsiooniliselt pidi iga raamatukogu arendaja kirjutama iga sihtkeele jaoks kohandatud sidumiskoodi, mis tekitab märkimisväärse takistuse platvormideülesele kasutusele võtmisele. UniFFI kõrvaldab selle üleliigsuse, pakkudes standardiseeritud lähenemisviisi nende sidemete automaatseks genereerimiseks.


Tööriista disainifilosoofia keskendub sellele, et Rust arendajad saaksid keskenduda oma põhilisele äriloogikale, tehes samal ajal oma raamatukogud kättesaadavaks teistes keeltes töötavatele arendajatele. Näiteks iOSi arendaja, kes kasutab Swifti, saab kasutada Rust raamatukogu UniFFI loodud sidemete kaudu, mis esitavad täiesti emakeelse Swift-liidese, ilma et oleks näha, et selle aluseks olev rakendus on kirjutatud Rust keeles. Selline sujuv integratsioon võimaldab meeskondadel kasutada Rust jõudluse eeliseid, ilma et kõik meeskonnaliikmed peaksid Rust tundma õppima.


### UniFFI arhitektuuri ja töökorralduse mõistmine


UniFFI töötab täpselt määratletud tööprotsessi kaudu, mis muudab Rust raamatukogud mitme keelega ühilduvateks pakettideks. Protsess algab Unified Definition Language (UDL) faili loomisega, mis on liidese spetsifikatsioon, mis kirjeldab, millised osad teie Rust raamatukogust peaksid olema avatud teistele keeltele. See UDL-fail toimib lepinguna teie Rust rakenduse ja loodud keelekohustuste vahel.


Arhitektuur järgib selget probleemide lahusust. Arendajad säilitavad oma Rust raamatukogu standardsete Rust idioomide ja mustrite abil, seejärel loovad eraldi UDL-faili, mis kaardistab avaliku liidese UniFFI tüübisüsteemile. UniFFI sidumise generaator töötleb nii Rust raamatukogu kui ka UDL-spetsifikatsiooni, et toota emakeelseid sidumisi soovitud sihtplatvormidele. Need genereeritud sidumised tegelevad kogu keerulise andmete marshalinguga ja unmarshalinguga võõrkeelse tööaja ja Rust koodi vahel.


Sõiduaegselt loob arhitektuur kihilise lähenemisviisi, kus sihtkeeles (näiteks Kotlin Androidile) kirjutatud rakenduskood suhtleb genereeritud sidumiskoodiga, mis näib olevat täiesti emakeelne. See siduv kiht tegeleb tõlkimisega keelespetsiifiliste tüüpide ja Rust tüüpide vahel, haldab mälu turvaliselt üle keelepiiride ja pakub veakäitlust, mis järgib sihtkeele konventsioone. Rust aluseks olev äriloogika jääb muutumatuks ja ei ole teadlik selle peale ehitatud mitmest keeleliidesest.


### Töötamine UDLiga: Interface määratlus ja tüübi kaardistamine


UniFFI funktsionaalsuse nurgakiviks on Unified Definition Language, mis pakub deklaratiivset võimalust määrata, millised Rust raamatukogu osad peaksid olema avatud ja kuidas neid tuleks sihtkeeltes esitada. UDL-failid peavad sisaldama vähemalt ühte nimeruumi, mis toimib konteinerina funktsioonidele, mida saab otse välja kutsuda, ilma et oleks vaja objekti instantseerida. Need nimeruumi funktsioonid tegelevad tavaliselt lihtsate operatsioonidega, mis võtavad parameetritena väärtusi ja tagastavad tulemusi.


UDL toetab laiaulatuslikku hulka sisseehitatud tüüpe, mis loomulikult vastavad Rust tüübile. Põhitüüpide hulka kuuluvad standardsed algtüübid, nagu booleans, erinevad täisarvude suurused (u8, u32 jne), ujukomaarvud ja stringid. Keerulisemate tüüpide hulka kuuluvad vektorid, hash-kaardid ja Rust-spetsiifilised mõisted, nagu optsioonitüübid (esindatud küsimärgi süntaksiga) ja veakäitluse tulemitüübid. Tüüpsüsteem toetab ka loendusi, nii lihtsaid väärtusel põhinevaid loendusi kui ka keerulisi loendusi, mis sisaldavad seotud andmeid, võimaldades andmete modelleerimist, mis on võimalik üle keeltepiiride.


Rust struktuurid tõlgitakse UDL-i sõnastikeks, säilitades peaaegu üks-ühele vastavuse, kohandudes samal ajal UDL-i süntaksikonventsioonidega. Kui Rust struktuuridel on seotud meetodid, saab neid UDLis esitada liidetena, mis generate objektorienteeritud sihtkeeltes, nagu Kotlin või Swift, on meetoditega klassid. Selline kaardistamine säilitab objektorienteeritud disainimustrid, mida arendajad nendes keeltes ootavad, säilitades samal ajal Rust aluseks oleva rakenduse struktuuri ja käitumise.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


Vastav Rust rakendamine määratleks need tüübid ja rakendaks `uniffi::export` atribuuti generate sidumistele Kotlini, Swifti, Pythoni ja muude toetatud keelte jaoks.


### Veakäitlus ja täiustatud funktsioonid


UniFFI pakub veakäsitlust, mis säilitab Rust tulemuspõhise veamudeli, kuid tõlgib selle sihtkeele jaoks asjakohaselt. Funktsioone, mis Rust-s tagastavad Result-tüüpi, saab UDL-is tähistada võtmesõnaga "throws", täpsustades, milliseid veatüüpe nad võivad tekitada. Need vead tuleb UDL-failis defineerida vigade enumidena ja need peavad rakendama Rust standardset Error-traiti Rust koodis. Thiserror crate pakub mugavat makrot selle tunnuse rakendamiseks, mis vähendab oluliselt boilerplate koodi.


Veakäsitluse tõlge näitab UniFFI keeletundlikku lähenemist. Kotlinis on UDL generate funktsioonid, mis on tähistatud UDLis viskajatena, meetodid, mis viskavad erandeid vastavalt Java/Kotlini konventsioonidele. Pythoni sidumised kasutavad sarnaselt Pythoni erandite mudelit. Selline tõlge tagab, et veakäitlus tundub igas sihtkeeles loomulik ja idiomaatiline, säilitades samal ajal algsete Rust veatüüpide semantilise tähenduse.


Tagasikutsumisliidesed on veel üks täiustatud funktsioon, mis võimaldab kahesuunalist suhtlust Rust raamatukogude ja tarbivate rakenduste vahel. Kui Rust raamatukogu peab rakenduskoodi tagasi kutsuma, saavad arendajad Rusts defineerida tunnused ja märkida need UDLis tagasikutsumisliidesteks. Tarbijarakendus rakendab neid liideseid oma emakeeles ja UniFFI tegeleb keerulise marshalinguga, mis on vajalik nende tagasikutsete funktsioonide kutsumiseks Rust koodist. See muster nõuab hoolikat tähelepanu niiditurvalisusele, kuna tagasikutsumised võivad ületada niidipiire, mis nõuab Rust poolel Send- ja Sync-piiranguid.


### Reaalsed rakendused ja praegused piirangud


UniFFI on vastu võetud krüptovaluuta ja plokiahela arenduskogukonnas, kusjuures suuremad projektid nagu BDK (Bitcoin Development Kit), LDK (Lightning Development Kit) ja erinevad wallet rakendused kasutavad seda mobiilsete SDKde pakkumiseks. Need projektid näitavad UniFFI kasutamist tootmiskeskkondades.


Nende projektide reaalsete UDL-failide uurimine näitab praktilise kasutamise käigus tekkinud mustreid ja parimaid tavasid. Näiteks BDK UDL-fail näitab, kuidas keerukaid domeenimudeleid, mis sisaldavad mitmeid enumeid, struktuure ja liideseid, saab tõhusalt kaardistada, et luua terviklikke mobiilseid SDKsid. UDL-süntaksi järjepidevus erinevates projektides tähendab, et ühe UniFFI-võimelise raamatukoguga kursis olevad arendajad saavad kiiresti aru teistest ja saavad nendega töötada, luues võrgustikuefekti, mis toob kasu kogu ökosüsteemile.


UniFFI-l on siiski märkimisväärsed piirangud, millega arendajad peavad arvestama. Kõige olulisem on asünkroonsete liideste toetuse puudumine. Kõik genereeritud sidumised on sünkroonsed, mistõttu arendajad peavad Rust koodis tegelema asünkroonsete operatsioonidega ja esitama tarbivatele rakendustele sünkroonseid liideseid. Lisaks sellele kujutab endast väljakutset dokumentatsiooni paigutamine: Rust koodis kirjutatud dokumentatsioon ei kandu üle genereeritud sidumistele, samas kui UDL-failides sisalduv dokumentatsioon ei ole kättesaadav Rust raamatukogu otsestele tarbijatele. Kuigi praegu tehakse jõupingutusi nende piirangute kõrvaldamiseks automaatse analüüsi ja genereerimise abil, on need praeguste rakenduste puhul endiselt probleemiks. Lõpuks genereerib UniFFI keelekohustusi, kuid ei tegele platvormipõhise pakendamise ja levitamisega, jättes arendajatele ülesandeks levitatavate pakettide loomise viimased sammud iga sihtplatvormi jaoks.


# LNP/BP arendamine SDKga

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## LN sõlme SDK-l

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### LDK modulaarse arhitektuuri mõistmine


Lightning Development Kit (LDK) läheneb Lightning Network rakendamisele teisiti kui traditsiooniline sõlmede tarkvara nagu CLightning või LND. Kui tavalised Lightning-sõlmed toimivad kui täielikud daemon rakendused, mis töötavad pidevalt masinas, siis LDK toimib modulaarse Rust raamatukoguna, mis pakub algkomponente kohandatud Lightning-lahenduste loomiseks. See arhitektuuriline erinevus muudab LDK paindlikuks, võimaldades arendajatel Lightning-funktsioone kokku panna viisil, mis vastab nende konkreetsetele projektinõuetele.


LDK põhifilosoofia keskmes on modulaarsus ja kohandatavus. Selle asemel, et pakkuda monoliitseid lahendusi, pakub LDK üksikuid komponente, mida saab kombineerida, kohandada või täielikult asendada. Iga komponent on varustatud vaikimisi rakendustega, mis töötavad kohe karbist välja, kuid arendajad säilitavad vabaduse asendada oma rakendusi, kui see on vajalik. Näiteks sisaldab LDK vaikimisi rakendusi plokiahela jälgimiseks, tehingute allkirjastamiseks ja võrgukommunikatsiooniks, kuid iga neist saab asendada kohandatud lahendustega, mis on kohandatud konkreetsetele kasutusjuhtumitele või keskkondadele.


Selline modulaarne ülesehitus võimaldab LDK-l toimida erinevatel platvormidel ja stsenaariumides, mis oleksid traditsiooniliste Lightning-sõlmede jaoks keeruline. Mobiilirakendused, veebibrauserid, manustatud seadmed ja spetsiaalne riistvara saavad kõik kasutada LDK komponente viisil, mis vastab nende ainulaadsetele piirangutele ja nõuetele. Raamatukogu arhitektuur tagab, et arendajad saavad luua Lightning-võimelisi rakendusi, ilma et nad oleksid lukustatud etteantud toimimismustritesse või süsteemisõltuvustesse.


### LDK kasutusjuhtumid ja platvormi paindlikkus


LDK arhitektuuriline paindlikkus avab arvukalt kasutusvõimalusi, mis ulatuvad kaugemale traditsioonilistest Lightning-sõlmede rakendustest. Mobiilne wallet arendus on üks veenvamaid rakendusi, kus LDK võimaldab luua Phoenix wallet-ga sarnaseid mittevajavaid Lightning-rahakotte. Need mobiilsed rakendused võivad säilitada kasutaja kontrolli privaatvõtmete üle, sünkroonides samal ajal Lightning-teenusepakkujatega (LSP), kui nad on võrgus, võimaldades sujuvat maksete vastuvõtmist ja kanalite haldamist isegi katkendliku ühenduvuse korral.


Riistvaralise turvamooduli (HSM) integreerimine on LDK teine võimas kasutusviis. Ekstraheerides ainult tehingu allkirjastamise ja kontrollimise komponendid, saavad arendajad luua Lightning-teadlikke allkirjastamisseadmeid, mis mõistavad Lightning-tehingute konteksti ja mõju. See võime läheb kaugemale lihtsast tehingu allkirjastamisest ja hõlmab maksete edastamise, kanalioperatsioonide ja turvalisuse seisukohalt oluliste otsuste arukat analüüsi. HSM saab hinnata, kas tehing kujutab endast seaduslikku makset, marsruutimisoperatsiooni või potentsiaalselt pahatahtlikku katset, pakkudes kasutajatele sisukaid turbeülevaateid.


Veebipõhised Lightning-rakendused saavad LDK süsteemivälise disaini filosoofiast olulist kasu. Kuna WebAssembly keskkondades puudub otsene juurdepääs süsteemiressurssidele, nagu failisüsteemid, võrgupesad või entroopia allikad, võimaldab LDK puhas lähenemisviis Lightning'i funktsionaalsust sujuvalt kasutada brauseri keskkondades. Arendajad saavad rakendada kohandatud võrgukihte, kasutades WebSockets'i, ning pakkuda brauseriga ühilduvaid püsivus- ja juhuslikkuse allikaid, säilitades samal ajal Lightningi protokolli täieliku vastavuse.


### Põhikomponendid ja sündmusepõhine arhitektuur


LDK sisemine arhitektuur keerleb mitme võtmekomponendi ümber, mis töötavad koos sündmusepõhise süsteemi kaudu. Peer-haldussüsteem tegeleb kogu suhtlusega teiste Lightning-sõlmedega, rakendades krüpteerimiseks müraprotokolli ja hallates sõnumite struktuure Lightning-protokollile vastavuse tagamiseks. See komponent töötab sõltumatult aluseks olevast transpordimehhanismist, võimaldades arendajatel rakendada võrgukasutust TCP-sokettide, WebSocketsi, USB-seeriaühenduste või mis tahes muu kahesuunalise sidekanali kaudu.


Kanalihaldur on Lightning-kanali toimingute keskne koordinaator, kes teeb tihedat koostööd partnerjuhiga, et teostada kanali avamis-, sulgemis- ja makseoperatsioone. Kui arendaja algatab kanali avamise, loob kanalihaldur vajalikud protokolli sõnumid ja koordineerib partnerihalduriga mitmeastmelise läbirääkimisprotsessi läbiviimist. Selline probleemide lahusus võimaldab puhtalt abstraheerida välkprotokolli loogika ja võrgukommunikatsiooni üksikasjad.


LDK sündmuste süsteem pakub asünkroonseid teateid kõigi oluliste toimingute ja oleku muutuste kohta. Sündmused hõlmavad kogu Lightningi toimingute spektrit, alates partnerite ühendustest ja katkestamistest kuni maksete õnnestumise ja ebaõnnestumiseni, kanali oleku muutusteni ja plokiahela kinnitusteni. Selline sündmustepõhine lähenemisviis võimaldab rakendustel reageerida asjakohaselt Lightning-võrgu tegevusele, säilitades samal ajal LDK põhifunktsioonide ja rakendusspetsiifilise loogika selge eraldatuse. Arendajad saavad rakendada kohandatud sündmuste käitlejaid, mis ajakohastavad kasutajaliideseid, käivitavad teateid või algatavad Lightning-võrgu sündmuste põhjal järeltegevusi.


### Blockchain Integratsioon ja andmehaldus


Blockchain andmete integreerimine on üks LDK abstraktsioonikihtidest, mis on loodud nii Bitcoin sõlmedest kuni kergete mobiilsete klientideni. LDK toetab kahte peamist plokiahela suhtlusviisi, millest kumbki on optimeeritud erinevate ressursipiirangute ja tegevusnõuete jaoks. Täieliku ploki režiim võimaldab rakendustel, millel on juurdepääs täielikele plokiahela andmetele, edastada LDK-le terveid plokke, võimaldades terviklikku tehingu jälgimist ja koheselt reageerida asjakohastele plokiahela sündmustele.


Piiratud ressurssidega keskkondade jaoks pakub LDK filtreerimispõhist lähenemisviisi, mis vähendab ribalaiuse ja salvestusruumi nõudeid. Selles režiimis edastab LDK oma seirehuvid abstraktsete liideste kaudu, taotledes konkreetsete tehingu ID-de, UTXO-de või skriptimustrite jälgimist. Rakenduskihi saab seejärel rakendada seda jälgimist, kasutades Electrum servereid, plokkide uurijaid või muid kergeid plokiahela andmeallikaid. Selline lähenemisviis võimaldab mobiilseid rahakotte ja veebirakendusi säilitada Lightning-funktsioone, ilma et oleks vaja täielikku plokiahela sünkroniseerimist.


LDK püsivuskiht järgib samu abstraktsiooniprintsiipe, pakkudes rakendustele binaarseid andmeplokke, mida tuleb usaldusväärselt salvestada ja välja otsida. LDK tegeleb kogu keerukusega, mis on seotud salamakanalite olekute, võrgukõnede andmete ja muu kriitilise teabe serialiseerimise ja deserialiseerimisega. Rakendused peavad lihtsalt rakendama usaldusväärseid salvestusmehhanisme, kasutades selleks kas kohalikke failisüsteeme, pilve salvestusteenuseid või spetsiaalseid andmebaasisüsteeme. Selline ülesehitus tagab, et Lightningi olekuhaldus jääb töökindlaks, võimaldades samal ajal rakendustel valida salvestuslahendusi, mis vastavad nende tegevusnõuetele ja turvamudelitele.


### Täiustatud funktsioonid ja integratsioonimustrid


LDK võimalused laienevad Lightning Network funktsioonidele, nagu mitmepoolsed maksed, marsruudi optimeerimine ja võrgu kuulujuttude haldamine. Marsruudisüsteem säilitab Lightning Network topoloogiast tervikliku ülevaate kuulujutuprotokollis osalemise kaudu, mis võimaldab maksete jaoks arukat teeotsingut. Rakendused saavad konfiguratsiooniparameetrite kaudu mõjutada marsruutimisotsuseid ja isegi rakendada kohandatud marsruutimisloogikat spetsiaalsete kasutusjuhtumite jaoks.


Raamatukogu keelte sidumise süsteem võimaldab LDK integreerimist mitmetes programmeerimiskeskkondades, toetades Java, Kotlin, Swift, TypeScript, JavaScript ja C++. Selline platvormideülene ühilduvus võimaldab emakeelsetes keeltes kirjutatud mobiilirakendustel Lightning'i funktsionaalsust lisada, säilitades samal ajal optimaalsed jõudlusomadused. Sidumissüsteem säilitab LDK sündmustepõhise arhitektuuri ja modulaarse disaini kõigis toetatud keeltes, tagades arendajatele järjepideva kogemuse sõltumata sihtplatvormist.


Tasude hindamine ja tehingute edastamine on täiendavad valdkonnad, kus LDK pakub paindlikkust. Rakendused saavad rakendada kohandatud tasude hindamise strateegiaid, mis võtavad arvesse nende konkreetseid toimimismudeleid ja kasutajate nõudeid. Samamoodi saab kohandada tehingu edastamist nii, et see toimiks erinevate Bitcoin võrguliideste, alates otsestest full node ühendustest kuni kolmandate isikute ringhäälinguteenusteni. Selline paindlikkus tagab, et LDK-põhised rakendused saavad optimeerida oma plokiahela suhtlust oma konkreetsete kasutusjuhtumite jaoks, säilitades samal ajal Lightning-protokollide ja turvastandardite vastavuse.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### Välkkiirte arendamise väljakutse


Lightning-makseid integreerivate rakenduste väljatöötamine kujutab endast enamiku arendajate jaoks märkimisväärset takistust. Lightning-maksefunktsiooniga rakenduse loomiseks peavad arendajad sisuliselt saama Lightningi ekspertideks, mõistes keerulisi kontseptsioone, nagu kanalite haldamine, likviidsuse tasakaalustamine ja võrgutopoloogia. See eksperditeadmiste nõue tekitab Lightningi kasutuselevõtu jaoks põhiprobleemi: kuigi Lightning-võrk ise on toimiv ja maksed usaldusväärsed, takistab tehniline keerukus laialdast integreerimist igapäevarakendustesse.


Põhiprobleem seisneb selles, et arendajate vajaduste ja nende soovide vahel valitseb lõhe. Arendajad töötavad tavaliselt pingeliste tähtaegade all ja eelistavad lihtsaid lahendusi, mis võimaldavad neil keskenduda oma rakenduse põhifunktsioonile, mitte muutuda makseinfrastruktuuri ekspertideks. Kui Lightning'i integreerimine on keeruline, kalduvad arendajad loomulikult haldusalaste lahenduste poole, sest need pakuvad vähima vastupanu teed. Selline kalduvus hoiuteenuste poole õõnestab aga Bitcoin põhilist väärtuspakkumist, mis seisneb mittehoiustamise finantssuveräänsuses.


### Breez nägemus, välk kõikjal


Breez sai alguse lihtsast, kuid ambitsioonikast visioonist: ühendada kõik Lightning-võrku intuitiivsete Lightning-majanduse liideste kaudu. Ettevõtte lähenemisviis tunnistab, et kuigi Lightning-võrk toimib tehniliselt hästi, vajab see oma täieliku potentsiaali saavutamiseks hädasti kasutajate omaksvõttu. See vastuvõtmise väljakutse ulatub kaugemale kui üksikud kasutajad, hõlmates kogu rakenduste ja teenuste ökosüsteemi, mis võiks Lightningi integreerimisest kasu saada.


Esialgne Breez rakendus näitas seda visiooni, pakkudes kasutajatele otse mobiiltelefonis töötavat mittevajavat Lightning-sõlme. See rakendus tutvustas Lightningi võimalusi, nagu mikromaksete voogedastus podcasteritele ja müügipunkti funktsioonid. Breez rakendus näitas aga ka kriitilist arhitektuurilist piirangut: mobiilirakenduste ökosüsteem ei hõlbusta lihtsat suhtlust rakenduste vahel, sundides arendajaid ehitama kõik Lightninguga seotud funktsioonid ühte rakendusse, selle asemel et võimaldada spetsialiseeritud rakendustel kasutada jagatud Lightningi infrastruktuuri.


Ettevõtte Breez rakendusest saadud õppetundide põhjal jõuti olulisele järeldusele: Lightning'i tulevane kasutuselevõtt sõltub arendajate võitmisest. Kui mittekohustuslik Lightningi integreerimine muutub arendajate jaoks kõige lihtsamaks võimaluseks, muutub see vaikimisi valikuks. Selline lähenemisviis pakub ka regulatiivseid eeliseid, kuna mittekaitstav tarkvara seisab silmitsi vähemate regulatiivsete takistustega kui hoideteenused, mis teeb arendajatele lihtsamaks oma rakenduste ülemaailmse tarnimise.


### Breez SDK arhitektuur


Breez SDK pakub alternatiivset lähenemist Lightning-funktsioonide integreerimiseks rakendustesse. Selle asemel, et nõuda igale rakendusele oma Lightning-sõlme, pakub SDK arhitektuuri, mis säilitab mittekasutatavad põhimõtted, lihtsustades samal ajal arendaja kogemust. Selle keskmes on SDK, mis annab igale lõppkasutajale oma isikliku Lightning-sõlme, mis töötab Greenlight'i infrastruktuuris, Blockstream'i pilvepõhises Lightning-sõlme majutusteenuses.


Selline arhitektuur lahendab korraga mitu kriitilist probleemi. Kasutajad ei pea muretsema andmebaasi haldamise, serveri tööaja või infrastruktuuri hoolduse pärast - mured, mis oleksid tavatarbijate jaoks üle jõu käivad. Kuid erinevalt traditsioonilistest haldusalastest lahendustest ei ole Greenlightil kunagi juurdepääsu kasutajate võtmetele. Lightning-sõlm pilves ei saa teha ühtegi toimingut ilma aktiivselt ühendatud rakenduseta, mis suudab tehinguid ja sõnumeid allkirjastada. Selline disain säilitab isehoidmise turbe-eelised, kuid välistab samas operatiivse keerukuse.


SDK toetab ka koostalitlusvõimet. Mitu rakendust saab sama kasutaja Lightning-sõlme ühendada, kasutades sama seed fraasi, mis võimaldab kasutajatel säilitada ühe Lightning-saldo erinevate erirakenduste vahel. Näiteks võib kasutajal olla nii üldine Lightning wallet rakendus kui ka spetsiaalne podcasting-rakendus, mis mõlemad pääsevad ligi samadele fondidele ja Lightning-kanalitele. Selline arhitektuur võimaldab arendada sihipäraseid, spetsialiseeritud rakendusi, säilitades samal ajal ühtse finantsinfrastruktuuri.


### Välkteenuse pakkujad ja Just-in-Time likviidsus


Breez SDK kriitiline komponent on selle integreerimine Lightning Service Providers (LSP), mis toimivad analoogselt Interneti-teenuse pakkujatega, kuid Lightning-võrgu jaoks. LSPd lahendavad ühe Lightningi kõige keerulisematest väljakutsetest: likviidsuse juhtimine. Lightningi kanalites saavad vahendid liikuda ainult sinna, kus on olemas likviidsus, sarnaselt helmedega abakus, mis saavad liikuda ainult seal, kus on ruumi.


SDK rakendab "just-in-time" kanaleid LSPde kaudu, hallates automaatselt likviidsust ilma kasutaja sekkumiseta. Kui kasutajal on vaja saada makse, kuid tal puudub piisav sissetulev likviidsus, avab LSP automaatselt uue Lightning-kanali makse saabumise hetkel. See protsess toimub sujuvalt taustal, tagades, et kasutajad saavad alati makseid vastu võtta, ilma et nad peaksid mõistma kanalite mehaanikat.


See LSPde integreerimine ulatub kaugemale lihtsast likviidsuse juhtimisest. SDK sisaldab terviklikku Lightning-funktsionaalsust: sisseehitatud valvuriteenused turvalisuse tagamiseks, on-chain koostalitlusvõime allveevahetuste kaudu, fiat-on-ramp teenuste nagu MoonPay kaudu ja LNURL-protokollide tugi. Süsteem pakub ka sujuvat varundamist ja taastamist, mis tagab, et kasutajad ei kaota kunagi juurdepääsu oma rahalistele vahenditele isegi siis, kui infrastruktuuriteenuse pakkujad vahetuvad või muutuvad kättesaamatuks.


### Rakendamise ja arendaja kogemus


Breez SDK seab arendajate kogemuse esikohale tänu oma terviklikule, patareisid sisaldavale lähenemisviisile. SDK pakub sidemeid mitmetele programmeerimiskeeltele, sealhulgas Rust, Swift, Kotlin, Python, Go, React Native, Flutter ja C#, mis võimaldab arendajatel integreerida Lightning-makseid, kasutades oma eelistatud arendusvahendeid. Arhitektuur abstraheerib Lightningi keerukuse APIde kaudu, säilitades samal ajal Lightningi võrgu turvalisuse.


Selle lihtsustatud kasutuskogemuse tagamiseks töötavad peamised komponendid koos. Sisendparser käsitleb automaatselt erinevaid makseformaate, määrates, kas string kujutab endast arvet, LNURLi või muud makseviisi, ja suunab selle asjakohasele töötlemisfunktsioonile. Integreeritud allkirjastaja haldab kõiki krüptograafilisi toiminguid taustal, samal ajal kui vahetaja tegeleb on-chain interaktsiooniga läbipaistvalt. Selline ülesehitus võimaldab arendajatel keskenduda oma rakenduse ainulaadsele väärtuspakkumisele, mitte muutuda Lightning-infrastruktuuri ekspertideks.


SDK usaldusteta arhitektuur tagab, et kuigi Greenlight saab jälgida kanali olekut ja marsruutimisandmeid, ei saa nad pääseda ligi kasutaja rahalistele vahenditele ega teha volitamata toiminguid. Kasutajad säilitavad täieliku kontrolli oma isiklike võtmete üle, mis ei lahku kunagi nende seadmetest. See lähenemisviis kujutab endast hoolikalt kaalutud kompromissi toimimise lihtsuse ja privaatsuse vahel, pakkudes praktilist teed Lightningi kasutuselevõtuks, säilitades samal ajal Bitcoin finantssuveräänsuse põhiprintsiibid.


## LDK vs Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Lightning Development Kit (LDK) piirangute mõistmine


Lightning Development Kit on Rust raamatukogude kogumik, mis on mõeldud arendajatele paindlikkuse tagamiseks Lightning Network rakenduste loomisel. Selle paindlikkusega kaasnevad siiski olulised rakendamisprobleemid, mis ilmnesid Lipa tegeliku arenduse käigus. LDK madala taseme olemus tähendab, et arendajad peavad iseseisvalt tegelema paljude keeruliste ülesannetega, alates võrgu graafide sünkroniseerimisest kuni maksete marsruutimise optimeerimiseni. Kuigi selline lähenemisviis pakub täielikku kontrolli Lightning'i rakendamise üle, nõuab see märkimisväärseid arendusressursse ja sügavat tehnilist asjatundlikkust, et saavutada tootmiskõlblik töökindlus.


Üks kõige kriitilisemaid puuduvaid funktsioone LDKs oli LNURLi tugi, mis on laialdaselt vastu võetud standard, mis lihtsustab Lightning Network interaktsiooni lõppkasutajate jaoks. Lisaks sellele tekitas ankurväljundite puudumine tõsiseid operatiivseid probleeme, eriti kõrge maksumusega keskkondades. Anchor väljundid lahendavad põhiprobleemi Lightning-kanalite sundsulgemise puhul: kui võrgutasud tõusevad järsult, võib etteantud tasuga kanaleid olla võimatu ühepoolselt sulgeda, sest etteantud tasu muutub tehingu kinnitamiseks ebapiisavaks. See piirang osutus eriti problemaatiliseks wallet mobiilirakenduste puhul, kus kasutajad võivad wallet-st loobuda, kooskõlastamata kanalite ühiselt sulgemist, jättes potentsiaalselt rahalised vahendid tasude tõusu ajal hätta.


LDK suhteline ebaküpsus ilmnes ka ebausaldusväärses maksete marsruutimises, mis on iga Lightning-rakenduse jaoks kriitiline probleem. Vaatamata sellele, et LDK on tehniliselt usaldusväärne rakendus, muutis selle kui üldise lahenduse lai ulatus konkreetsete probleemide kiire lahendamise keeruliseks. Arendusmeeskond pidi kulutama palju aega marsruutimisprobleemide lahendamisele ja selliste funktsioonide rakendamisele, mida tuleks ideaaljuhul käsitleda raamatukogu tasandil, mis lõppkokkuvõttes mõjutas arenduskiirust ja kasutajakogemuse kvaliteeti.


### Breez SDK ja Greenlight'i eeliste avastamine


Üleminek Breez SDK-le kujutas endast arhitektuurilise lähenemise muutust, liikudes isehaldatavalt Lightning-sõlmelt pilvepõhisele lahendusele, mida toetab Blockstream'i Greenlight'i teenus. See muutus lahendas kohe mitu kriitilist valupunkti, mida LDK rakendamisel kogeti. Kõige olulisem paranemine toimus maksete usaldusväärsuse osas, mis tulenes peamiselt Greenlight'i võimest säilitada alati ajakohast võrgugraafikut. Erinevalt traditsioonilistest mobiilse Lightning'i rakendustest, mis peavad rakenduse käivitamisel sünkroonima võrguteavet, töötavad Greenlight'i sõlmed pidevalt pilves, säilitades reaalajas teadlikkust võrgust ja pakkudes kasutajate ühendamisel koheselt täielikke graafikuandmeid.


See arhitektuur kasutab lahinguproovitud Core Lightning (CLN) rakendamist, mis on juba aastaid edukalt suunanud makseid kui üks algsetest Lightning Network rakendustest. CLNi kogutud kogemused ja tõestatud usaldusväärsus pakkusid kohe stabiilsuse paranemise võrreldes noorema LDK projektiga. Kui kasutajad aktiveerivad oma Greenlight'i jõul töötava wallet, pärivad nad koheselt pidevalt töötava Lightning-sõlme täielikud võrguteadmised ja marsruutimisvõimalused, kõrvaldades sünkroonimisviivitused ja marsruutimise ebakindluse, mis vaevasid eelmist rakendust.


Breez SDK arvamuslik disainifilosoofia oli kasulik wallet arendamisel. Selle asemel, et pakkuda üldist Lightning-tööriistakomplekti, keskendub Breez konkreetselt wallet lõppkasutaja rakendustele, mis võimaldab arendusmeeskonnal keskenduda selle konkreetse kasutusviisi jaoks terviklike lahenduste loomisele. Selline sihipärane lähenemisviis võimaldas Breez-l integreerida olulised teenused otse SDK-sse, sealhulgas Lightning Service Provider (LSP) funktsioon, mis võimaldab kasutajatel saada makseid kohe pärast wallet paigaldamist, ilma et oleks vaja käsitsi kanalite avamise protseduure.


### Põhjalikud funktsioonid ja kasutajakogemuse parandused


Breez SDK integreeritud lähenemisviis ulatub Lightning'i põhifunktsioonidest kaugemale, hõlmates funktsioone, mis parandavad kasutajakogemust. Sisseehitatud LSP-integratsioon kõrvaldab traditsioonilise barjääri, mis nõuab kasutajatelt arusaamist kanalihaldusest, võimaldades uute wallet-i paigalduste puhul koheselt makseid vastu võtta. See sisseelamisprotsess aitab kaasa peavoolu vastuvõtmisele, kuna kasutajad saavad alustada Lightning-maksete vastuvõtmist ilma tehniliste teadmiste või seadistamisprotseduurideta.


Vahetuse funktsioon pakub kasutajakogemuse optimeerimiseks veel ühe tasandi, võimaldades kasutajatele ühtse saldo esitamist. Selle asemel, et sundida kasutajaid mõistma vahet Lightning ja on-chain Bitcoin vahel, võimaldab vahetusteenus vajaduse korral automaatselt nende kihtide vahel vahetada. Kui kasutajatel on vaja teha on-chain makseid, saab süsteem sujuvalt vahetada Lightning-vahendeid on-chain Bitcoin-ks, säilitades ühtse, likviidse saldo illusiooni, käsitledes samas tehnilist keerukust ettevõttesiseselt.


SDK toetus nullkanaliliste reservide jaoks lahendab märkimisväärse kasutajakogemuse probleemi traditsioonilistes Lightningi rakendustes. Kanalireservid takistavad tavaliselt kasutajatel kogu näidatud saldo kulutamist, tekitades segadust, kui maksed ebaõnnestuvad, kuigi raha on ilmselt piisavalt. Breez võimaldab kasutajatel nende reservide kaotamisega kulutada kogu näidatud saldo, kuigi see nõuab, et LSP võtaks täiendava riski. See kompromiss on näide Breez kasutajakesksest lähenemisviisist, kus teenusepakkujad võtavad tehnilise keerukuse ja riski enda kanda, et luua intuitiivne kasutajakogemus.


Täiendavad funktsioonid, nagu LNURL-tugi, vahetuskursi teenused ja mitme seadme sünkroniseerimine, näitavad veelgi SDK terviklikku lähenemist wallet arendamisele. Pilvepõhine arhitektuur võimaldab kasutajatel pääseda oma Lightning-sõlme juurde mitmest seadmest või rakendusest, kusjuures Breez tegeleb seisundi sünkroniseerimisega nende erinevate juurdepääsupunktide vahel. Tulevased teekaardi elemendid hõlmavad spend-all-funktsioone wallet täieliku äravoolu jaoks, ühendamist dünaamilise kanalihalduse jaoks ja konkureerivate LSPde turgu, et luua tervislik konkurents teenuse osutamisel.


### Kompromisside hindamine ja tsentraliseerimisega seotud probleemid


Üleminek Breez SDK-le ja Greenlight'ile toob kaasa olulisi tsentraliseerimise kompromisse, mida tuleb hoolikalt kaaluda Bitcoin detsentraliseerimise põhimõtete kontekstis. Pilvepõhine arhitektuur tähendab, et kasutajate Lightning-sõlmed töötavad Blockstream'i infrastruktuuril, mis loob sõltuvust nii Greenlight'i jätkuvast toimimisest kui ka Breez jätkuvast arendamisest. See tsentraliseerimine ulatub kaugemale kui pelgalt mugavus, mõjutades potentsiaalselt kasutajate võimet saada raha tagasi, kui teenused muutuvad kättesaamatuks või kui toimub tsensuur.


Taastamisstsenaariumid kujutavad endast selles arhitektuuris erilisi väljakutseid. Kuigi kasutajad säilitavad kontrolli oma isiklike võtmete üle, nõuab juurdepääs rahalistele vahenditele ilma Greenlight'i infrastruktuurita tehnilisi teadmisi sõltumatute Core Lightning'i sõlmede käivitamiseks ja kanalite seisundi taastamiseks. Üksikute kasutajate jaoks osutuks see taastamisprotsess tõenäoliselt liiga keeruliseks ning isegi wallet pakkujatel oleks Greenlight'i teenuste lõpetamise korral märkimisväärseid probleeme terve kasutajate baasi üleviimisega alternatiivsele infrastruktuurile.


Selle arhitektuurimuudatusega muutuvad ka privaatsuse kaalutlused. Pilvepõhine marsruutimine tähendab, et Greenlight saab potentsiaalselt ülevaate maksete sihtkohtadest, samas kui varasemad ainult LSP-arhitektuurid piirasid teabe lekkimist maksesummade ja ajastusega. Invoice genereerimine pilves laiendab veelgi potentsiaalset teabele avatust, kuna kasutamata arved, mis varem jäid kasutajate seadmetes privaatseks, läbivad nüüd Blockstream'i infrastruktuuri.


Vaatamata nendele tsentraliseerimise probleemidele kaalub praktiline kasu sageli üles teoreetilised riskid paljude kasutusjuhtumite puhul. Parem töökindlus, ulatuslik funktsioonide kogum ja parem kasutajakogemus võimaldavad wallet arendajatel keskenduda pigem rakenduskihi uuendustele kui välkkiirte infrastruktuuri haldamisele. Selline tööjaotus peegeldab küpsevat ökosüsteemi, kus spetsialiseerunud teenusepakkujad tegelevad keeruliste tehniliste väljakutsetega, võimaldades rakenduse arendajatel keskenduda kasutajakogemusele ja äriloogikale. Oluline on nende kompromisside selge mõistmine ja teadlike otsuste tegemine konkreetsete kasutusjuhtumite nõuete ja riskitaluvuse taseme alusel.




# Lõplik osa

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Arvamused ja hinnangud

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Kokkuvõte

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>