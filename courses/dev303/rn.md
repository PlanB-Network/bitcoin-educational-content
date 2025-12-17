---
name: Kwiga Rust na Bitcoin.
goal: Teza imbere ubuhinga bwawe bwo gutegura Rust biciye mu gukora kode ya Bitcoin
objectives: 

  - Menya ururimi rwa Rust
  - Gutahura igituma ukoresha Rust mu gutegura Bitcoin.
  - Kuronka ishingiro ry'umuravyo SDK

---

# Urugendo rwa Rust rw'abubatsi ba Bitcoin



Muri iri shure ry’ibikorwa, ryafashwe amasanamu mu gihe c’amahugurwa yateguwe na Fulgur’ Ventures mu kwezi kwa Gitugutu 2023, uzotsimbataza ubuhinga bwawe bwo gukora Rust mu kwubaka ibice vy’ukuri vyibanda kuri Bitcoin n’imigambi mito mito. Tuzovuga ivy’ishimikiro vya Rust, igituma Rust ikoreshwa mu gutegura Bitcoin (umutekano w’ukwibuka, ubushobozi, n’ugukorana neza), n’ingene wotangura gukoresha Lightning SDK kugira ngo wubake ibintu vyo kwishura.


Mu bice vyose, uzokwimenyereza uburyo nyamukuru bwa Rust (ubutunzi, ubuzima, ibiranga, async), ukore n’ibintu vya kera vya Bitcoin (imfunguruzo, ibikorwa, inyandiko), kandi utere imbere mu gushiramwo ivyiyumviro vya Lightning (ibihimba, imirongo, amafagitire).


Nta gutegura Rust canke Bitcoin imbere y’igihe bisabwa cane, naho nyene kumenya neza porogarama z’ishimikiro bifasha. Iryo shure rirabereye abatangura ariko rirafasha cane abahinga bajabuka baja muri Bitcoin.


+++

# Imenyekanisha

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Incamake y'amashure

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Imenyekanisha**


Ikaze muri iri shure ry'intango ry'ivy'iporogarama ku SDKs. Muri iri huriro, uzokwiga ivy’ishimikiro vya Rust, hanyuma wibande kuri Rust ikoreshwa muri porogarama ya Bitcoin, hanyuma uheze n’ibintu bimwebimwe bikoreshwa ukoresheje SDKs.


Amasanamu y’ayo mahugurwa azoboneka mu congereza gusa ubu kandi yari mu nama y’ubuzima yateguwe mu kwezi kwa Gitugutu guheze i Toscane na Fulgure Venture. Iryo huriro rizoba ryibanda ku ndwi ya mbere gusa. Igice ca kabiri cari kigenewe RGB kandi gishobora gusangwa mu nyigisho ya RGB.


https://planb.academy/en/courses/rgb-programming-3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Iryo huriro riguha akaryo ko guteza imbere ubuhinga bwawe bwo gukora porogarama kuri Lightning Network ukoresheje Rust na SDK zitandukanye. Igenewe abahinguzi bafise ubumenyi bukomeye bwo gukora porogarama bashaka kwisuka mu gutegura ivy’ubuhinga bwa Lightning Network. Uzomenya ivy’ishimikiro vya Rust, igituma ibereye gutegura Bitcoin, hanyuma ugende ku gushirwa mu ngiro ukoresheje SDKs zidasanzwe.


**Igice ca 2: Iga gukora code na Rust**

Muri iki gice, uzobona ivy’ishimikiro vya Rust biciye mu bice bigenda biratera imbere. Uzokwiga kwandika kode ya Rust, utahure ivyihariye vyayo, kandi umenye neza ibintu vyayo vy’ingenzi mu bice indwi vy’ido n’ido. Iyi module ni ngombwa kugira ngo umuntu atahure igituma Rust ari ururimi rwo gukunda cane mu guteza imbere Bitcoin.


**Igice ca 3: Rust na Bitcoin**

Aha, tuzokwihweza mu buryo bwimbitse igituma Rust ari ihitamwo ribereye mu guteza imbere Bitcoin. Uzomenya ivyerekeye urugero rwayo rw’ikosa, igikoresho ca UniFFI, n’ibiranga asynchronous – vyose ni ibintu nyamukuru mu kwubaka porogarama ikomeye kandi itekanye.


**Igice ca 4: Iterambere rya LNP/BP n'ama SDK**

Uzokwiga ingene wotegura amanode ya LN ukoresheje SDK zitandukanye nka Breez SDK na Greenlight ya Lipa. Uzobona ingene woshira mu ngiro ibikorwa vya Lightning Network ukoresheje amasomero yagenewe kworohereza Bitcoin n’iterambere rya Lightning.


Ni mwiteguye gukura mu buhinga bwanyu bwa Lightning Network na Rust? Reka tugende!

# Menya uko ukoresha igitabu c'umugese

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Intangamarara ya Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<Id y'umwigisha>e7e63d59-ea19-4960-9446-61bd4dcc98f0</Id y'umwigisha>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Gushiramwo no gucunga Rust na Rustup


Igihe utanguye urugendo rwawe na Rust, intambwe ya mbere ni ugushinga ahantu heza ho gutera imbere. Uburyo bushimikijwe cane bwo gushiramwo Rust ni biciye muri Rustup, uburyo bwo gucunga ibikoresho bujejwe gushiramwo no guhindura ibintu mu migambi itandukanye no mu bibanza bitandukanye.


Rustup ikora nk’ibirenze gusa gushiramwo—ikora nk’igikoresho co gucunga neza ibidukikije vyawe vy’iterambere rya Rust. Na Rustup, urashobora gushiramwo mu buryo bworoshe izindi ntumbero zo gukoranya amakuru ku bikoresho bitandukanye, nka ARM64 yo gutegura Android canke ibindi vyubatswe woshobora gukenera gushigikira. Ico gikoresho kandi gikora neza ivy’uguhindura Rust, ivyo bikaba ari ivy’agaciro cane kubera ko Rust isohora verisiyo nshasha idahinduka hafi buri ndwi zitandatu. Iyo ukeneye guhindura ku bijanye n'isohorwa rishasha, itegeko ryoroshe rya `rustup update` rikora vyose ubwavyo.


Igihe ushizeho Rustup, birabereye gutahura uburyo bwo gucungera umutekano buri muri vyo. Ivyo bikoresho bica bikura kandi bikabikora ku rubuga rwemewe rwa Rust biciye kuri HTTPS, ivyo bikaba bitanga umutekano w’ivy’ubuhinga bwo gutwara ibintu. Amapaki yavanwe na Rustup na Cargo ava mu bibanza vyizigirwa (crates.io n’ibikorwa remezo vyemewe vya Rust) kandi yungukira ku gupfuka HTTPS. Naho ubu buryo butekanye ku bikorwa vyinshi vy’iterambere, amashirahamwe amwe amwe afise amategeko akomeye y’umutekano yoshobora guhitamwo gushiramwo Rust biciye ku mucungerezi w’amapaki y’ugukwiragiza kwabo kwa Linux, ivyo bikaba bitanga urugero rw’inyongera rw’ukwizigira biciye ku bikorwa remezo vyo gusinya amapaki vy’ugukwiragiza. Ku bijanye n’inyigisho n’iterambere rusangi, Rustup ni igikoresho gishingiye neza kandi cizigirwa cane mu bidukikije vya Rust.


Ku bikorwa vyinshi vy’iterambere, ushobora gushiramwo Rustup ukoresheje inyandiko yo gushiramwo itangwa ku rubuga rwemewe rwa Rust. Igikoresho kizogusaba guhitamwo hagati y'amahitamwo atandukanye y'uruzitiro rw'ibikoresho, n'uruzitiro rw'ibikoresho ruhamye ari rwo ruhitamwo rwiza ku bakoresha benshi. Ivyo gushiramwo bibera mu bubiko bwawe bwo muhira, ntibisaba uburenganzira bw'umuyobozi, kandi bishiraho ibihinduka vyose bikenewe kugira ngo bikoreshwe ubwo nyene.


### Gutahura ibikoresho vya Rust n'ibice vyavyo


Iterambere ry’ibidukikije rya Rust rigizwe n’ibice vyinshi vy’ingenzi bikorana kugira ngo bihe ikibanza c’iporogarama yuzuye. Gutahura ivyo bihimba biragufasha kugendera neza mu nzira y’iterambere rya Rust no gutorera umuti ingorane iyo zivutse.


Igikoresho co gukoranya Rust, kizwi nka `rustc`, ni co gikora umushinge w'ibikoresho vya Rust. Naho woshobora gukoresha `rustc` mu buryo butaziguye kugira ngo ukore porogarama za Rust, ibikorwa vyinshi vy'iterambere vyishimikije Cargo, umuyobozi w'amapaki ya Rust n'uburyo bwo kwubaka. Cargo ikora nk’uko npm ikora mu bidukikije vya JavaScript, gucunga ibiva ku bindi, guhuza inyubako, no gutanga amabwirizwa akwiriye ku bikorwa vy’iterambere rusangi. Iyo ukoresheje amabwirizwa nka `cargo build` canke `cargo run`, Cargo itunganya uburyo bwo gukoranya, ifata umuti w'ibiva ku bindi, kandi igacungera imiterere y'umugambi muri rusangi.


Clippy ni linter isesangura kode yawe igatanga ivyiyumviro vyo gutera imbere. Mu buryo butandukanye n’abagenzura insiguro y’amajambo, Clippy aratahura imvugo za Rust kandi arashobora gutanga impanuro z’uburyo bwinshi bw’imvugo bwo gukora ibikorwa vyihariye. Ico gikoresho kirafasha mu kwiga ingendo nziza za Rust no kwandika kode ishobora kubungabunga.


Igikoresho ca Rust kirimwo kandi ibikoresho vy’inyandiko vyuzuye be n’inyandiko zisanzwe zo mu bubiko bw’ibitabu, zishobora gushikirizwa biciye ku rubuga rwemewe rw’inyandiko za Rust. Iyi nyandiko ikora nk’ishingiro ry’agaciro mu gihe c’iterambere, itanga amakuru arambuye yerekeye ibikorwa vy’ububiko bw’ibitabu, ubwoko, n’ibice. Ivyo bitabo birimwo ingero nyinshi n’insobanuro zigufasha gutahura atari gusa ivyo ibikorwa bikora, ariko n’ingene wobikoresha neza muri porogarama zawe.


Rust ishigikira imirongo myinshi yo gusohora: ihamye, beta, n’ijoro. Umurongo ushikamye utanga ibisohoka vyageragejwe neza bibereye gukoreshwa mu guhingura. Umurongo wa beta utanga ivyerekanwa vy’isohoka rikurikira ridahinduka, ahanini rikoreshwa mu kugerageza kwa nyuma imbere y’uko risohoka ku mugaragaro. Iryo joro ry’umurongo ririmwo ibintu vy’igerageza biriko birategurwa, bishobora kuba ngirakamaro mu kugerageza ubushobozi bushasha bwa Rust, naho ivyo bintu bishobora guhinduka canke bikakurwaho mu bizosohoka muri kazoza.


### Guhingura no gucunga imigambi ya Rust n'imizigo


Ivyumba vy’iterambere vya Rust vy’ubu bikikuje Cargo, bituma imigambi irema neza, gucunga neza abavyifatamwo neza, n’uburyo bwo kwubaka. Aho gukora ububiko n'amadosiye n'amaboko, Cargo itanga itegeko rya `cargo new` kuri generate imiterere y'umugambi yuzuye n'ibintu bibereye.


Iyo uremye umugambi mushasha ufise `cargo new project_name`, Cargo ishiraho ububiko busanzwe, irema dosiye y'ishimikiro `main.rs` ifise "Muraho, isi!" porogaramu, itangura ububiko bwa Git, kandi itanga dosiye `Cargo.toml` yo gutunganya umugambi. Dosiye `Cargo.toml` ikora nk'inzira nyamukuru y'imiterere y'umugambi wawe, irimwo amakuru y'umugambi wawe n'urutonde rw'ibintu vyose bishingiye kuri kode yawe isaba.


Cargo itanga amabwirizwa menshi y’ingenzi ku bikorwa vy’iterambere vya misi yose. Itegeko rya `cargo build` rikoranya umugambi wawe n'ibiwushingiyeko, rikora amadosiye ashobora gukorwa mu bubiko bwa `target`. Kugira ngo umuntu asubiremwo vyihuse mu gihe c'iterambere, `cargo run` ihuza inyubako n'ugushitsa mu ntambwe imwe. Itegeko rya `cargo check` rikora ivyigwa vyose vy'ugukoranya ataco rikora, bikaba bituma vyihuta cane kuruta kwubaka kwuzuye iyo ushaka gusa kugenzura ko kode yawe ikoranya neza.


Igihe utegura kode yo gukoresha, ibendera `--release` rishobora gutuma ibintu bigenda neza kandi rikakuraho ivyemezo vy'ugukosora. Release builds zigenda ningoga kandi zitanga ibikorwa bitobito, ariko zifata igihe kirekire kugira ngo zikoranirize hamwe no gukuraho amakuru y’ingirakamaro yo gukosora. Igikoresho gikoresha uburyo butandukanye bwo gutuma ibintu bigenda neza mu gihe co gusohora inyubako kandi kigahagarika igihe co gukora nk’ugutahura umubare wose, ivyo bikaba bituma ibikorwa vyiza ariko bikakuraho ivyemezo bimwebimwe vy’umutekano biri mu nyubakwa zo gukosora.


### Ibintu bihinduka, Ibintu Bihinduka, n'Ivyiyumviro vy'Umutekano vya Rust


Rust ifata uburyo butandukanye bwo gucunga ibihinduka kuruta indimi nyinshi. Ku mburabuzi, ibihinduka vyose biri muri Rust ntibihinduka, bisobanura ko agaciro kavyo kadashobora guhinduka inyuma y'uguhabwa igikorwa ca mbere. Iyi ngingo y’uguhingura igamije gukingira amakosa asanzwe yo muri porogarama aterwa n’amahinduka ya leta atategerezwa.


Iyo umenyesheje umuhinduzi ukoresheje `let x = 5`, uwo muhinduzi aba uwudahinduka ku buryo busanzwe. Igerageza ryose ryo guhindura agaciro karyo mu nyuma rizovamwo ikosa ryo gukoranya. Ico gisabwa co kudahinduka gihatira abahinguzi kwiyumvira neza igihe amahinduka ya Leta ari ngombwa vy’ukuri kandi kigatuma inyifato ya kode ishobora gutegekanirwa. Ibibazo vyinshi vyo muri porogarama biva ku bihinduka bihinduka ataco biteze, kandi ukudahinduka kwa Rust kurafasha gukingira ivyo bibazo.


Iyo ukeneye vy'ukuri guhindura agaciro k'umuhinduzi, Rust isaba gutangaza neza uguhinduka ukoresheje ijambo ry'ingenzi `mut`: `let mut x = 5`. Iryo tangazo ritomoye rikora nk'ikimenyetso gitomoye ku mukozi n'abandi bategura ko agaciro k'iyi mpinduka gashobora guhinduka mu gihe porogarama iriko irashirwa mu ngiro. Igisabwa co kumenyesha mu buryo butomoye ko umuntu ashobora guhinduka, kiraremesha umuntu kwiyumvira neza nimba vy’ukuri uguhinduka ari ngombwa ku kintu cose gihinduka.


Rust nayo irashigikira igitutu, kigufasha gutangaza umuhinduzi mushasha afise izina rimwe n'umuhinduzi wa kera. Mu buryo butandukanye n’uguhinduka, gutera igitutu bituma haba igihinduka gishasha rwose gishobora kuba gifise izina rimwe, kigahisha neza igihinduka ca kera. Ubwo buryo buragaragara ko ari ngirakamaro canecane igihe umuntu ahindura amakuru biciye mu ntambwe nyinshi, nko gucapura urudodo mu mubare hanyuma akarugira uwundi mubare. Hamwe n'igitutu, ushobora kuguma ufise izina ry'umuhinduzi ridahinduka mu gihe cose c'ihinduka mu gihe uhindura ubwoko bw'umuhinduzi ku ntambwe yose.


Itandukaniro hagati y’ugutera igitutu n’uguhinduka riraba ikintu gihambaye igihe turimbura amahinduka y’ubwoko. Hamwe n'igitutu, ushobora guhindura agaciro n'ubwoko bw'umuhinduzi kuko uriko urema umuhinduzi mushasha. Mu guhindura, ushobora guhindura agaciro gusa mu gihe uguma ufise ubwoko bumwe, kuko uriko urahindura umuhinduzi ariho aho kurema uwundi mushasha.


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


### Ubwoko bw'amakuru n'ubwoko bwa sisitemu y'ishimikiro


Rust ishira mu ngiro uburyo bukomeye, butahinduka aho agaciro kose gategerezwa kugira ubwoko busobanuwe neza buzwi mu gihe co gukoranya. Naho ivyo vyoshobora gusa n'ibibujijwe ugereranyije n'indimi zanditswe mu buryo bukomeye, ubushobozi bwo gutahura ubwoko bwa Rust busobanura ko udakenera gusobanura ubwoko mu buryo butomoye. Umukozi ashobora kenshi kumenya ubwoko bukwiye bishingiye ku kuntu ukoresha agaciro.


Ariko rero, hari ibintu bimwebimwe bisaba ko haba ibisobanuro vy’ubwoko bitomoye. Igihe ukoresha ibikorwa rusangi nka `parse()`, bishobora guhindura imirongo mu bwoko butandukanye bw'imibare, umukozi akeneye kumenya ubwoko bwihariye ushaka. Muri ibi bihe, utanga ubwoko bw'ibisobanuro ukoresheje insiguro y'inyuguti: `reka wibaze: u32 = "42".parse().expect("Si umubare!")`.


Ubwoko bw'ibiharuro vya Rust burimwo imibare yose, imibare y'inyuguti ziterera, ibiharuro vy'inyuguti, n'inyuguti. Ubwoko bw'umubare wose buratanga ubugenzuzi nyabwo ku gukoresha ubwenge n'ibiranga ibikorwa. Ubwoko bw'imibare yose bwitwa mu buryo butunganye: `i8`, `i16`, `i32`, `i64`, na `i128` ku mibare yose ifise umukono, na `u8`, `u16`, `u32`, `u64`, na `u128` ku mibare yose idafise umukono. Imibare yerekana ubwaguke bw'ibice, bituma ikoreshwa ry'ubwenge n'agaciro bica bigaragara.


Ubwoko bwa `isize` na `usize` bukwiye kwitwararikwa cane uko bujanye n'ubwubatsi bwawe. Ku bikoresho vy’ibice 64, ubwo bwoko bufise ubwaguke bw’ibice 64, mu gihe ku bikoresho vy’ibice 32, bufise ubwaguke bw’ibice 32. Ubwo bwoko bukoreshwa cane mu gukora indexing y'imirongo n'uguhindura ubwonko kubera ko buhuye n'ubunini bw'ijambo ry'ubwubatsi bw'intumbero, bikaba bishoboza gukora neza imibare y'ibimenyetso n'ibikorwa vy'ubwonko.


Rust itanga uburyo bwinshi bwo kwandika amajambo y'imibare yose, harimwo imirongo y'icumi, y'icumi na gatandatu (`0x`), y'icumi (`0o`), n'ibiri (`0b`). Ushobora kandi gukoresha uturongo aho hose mu mibare kugira ngo ushobore gusoma neza, nk'ukwandika `1_000_000` aho kwandika `1000000`. Ivyo bimenyetso bishizwe munsi ntaco bihindura ku gaciro ariko birashobora gutuma imibare myinshi isomwa neza.


Ubwoko bw'inyuguti zireremba muri Rust buragororotse: `f32` ku mibare y'inyuguti zireremba zifise ukuri kumwe na `f64` ku mibare y'inyuguti zireremba zibiri. Ubwoko bwa `f64` burakundwa cane kubera ubuhinga bwabwo bwo gukora neza cane be n'uko ama processeur ya none ashobora gukora neza ibikorwa vy'ibice 64 nk'ibikorwa vy'ibice 32.


### Ubwoko bw'ibirungo hamwe n'imitunganirize y'amakuru


Uretse ubwoko bw'ibiharuro, Rust itanga ubwoko bw'ibiharuro buhuriza hamwe agaciro kenshi. Tuples zigufasha gufatanya agaciro k'ubwoko butandukanye mu gaciro kamwe k'uruvange. Urema ibiharuro ukoresheje uturongo kandi ushobora gusobanura ubwoko bw'ikintu cose: `reka ibiharuro: (i32, f64, u8) = (500, 6.4, 1)`.


Ivyiyumviro bifasha gusenyura, bigufasha gukuraho agaciro k'umuntu ku giti ciwe: `reka (x, y, z) = tup`. Iyi nsiguro irema ibihinduka bitatu bitandukanye biva ku bice vya tuple. Canke, ushobora gushika ku bintu vy'ibice ukoresheje akadomo k'utudomo n'urutonde rw'ibintu: `tup.0`, `tup.1`, `tup.2`.


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


Amabara yo muri Rust atandukanye cane n’amabara canke urutonde rwo mu zindi ndimi nyinshi kubera ko afise ubunini budahinduka buca buba igice c’ubwoko bwayo. Urutonde rw'imibare itanu yose rufise ubwoko `[i32; 5]`, aho akarongo gatandukanya ubwoko bw'ikintu n'uburebure bw'urutonde. Aya makuru y'ubunini bw'urugero rw'ubwoko ashoboza umukozi gukora isuzuma ry'imipaka kandi akamenya neza ko ibikorwa vyakira amabara bimenya neza igitigiri c'ibintu vyo kwitega.


Ushobora gutanguza amabara ukoresheje urutonde rw'ibintu vyose mu buryo butomoye: `[1, 2, 3, 4, 5]`, canke ukoresheje insiguro y'amajambo ngufi ku mabara afise agaciro gasubirwamwo: `[3; 5]` irema urutonde rw'ibintu bitanu, vyose bifise agaciro ka 3. Iyi nkuru ngufi ni ngirakamaro mu gutanguza ububiko canke kurema urutonde rufise agaciro ka mbere.


Ugushika ku nzira bikoresha ubuhinga bwo kwandika nk'indimi nyinshi, ariko Rust itanga igihe co gukoranya n'igihe co gukora. Iyo winjiye ku rutonde rufise urutonde rudahinduka umukozi ashobora kugenzura, ruzofata uburenganzira bwo hanze y'imipaka mu gihe co gukora. Ku bimenyetso bihinduka bimenyekana mu gihe co gukora, Rust yinjiza ivyigwa vy’imipaka bizotuma porogarama igira ubwoba iyo ugerageje gushika ku bimenyetso bitagira akamaro, bikabuza guhungabanya umutekano w’ubwenge.



## Ownership n’Umutekano w’Ukwibuka muri Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Gutahura uburyo bwihariye bwa Rust bwo gucunga ubwonko


Iki gice kiravuga kuri kimwe mu vyiyumviro bihambaye cane vya Rust. Naho ivyiyumviro vya kera bishobora kuba vyari bimenyerewe n’abakora porogarama bava mu zindi ndimi, ubutunzi ni uburyo Rust ikoresha mu gutorera umuti umutekano w’ukwibuka ata gukusanya imyanda.


Rust yakozwe n’intumbero nyamukuru yo gukingira ibibazo bijanye n’ukwibuka bitera ingorane indimi zo ku rugero ruto nka C na C++. Ivyo bibazo birimwo ibikoko bikoreshwa inyuma y’ubuntu, aho ubwonko bushikira inyuma y’aho busohokeye, n’ugusesagura ububiko, aho porogarama zandika hanze y’imipaka y’ububiko bwatanzwe. Inzira z’imigenzo z’izo ngorane zari zigizwe n’uguhinduranya ivyo Rust irondera gukuraho. Indimi zo ku rwego rwo hejuru nka Java na Go zitorera umuti umutekano w’ubwenge biciye mu kwegeranya imyanda, aho uburyo bwikora buhora bumenya kandi bukabohora ubwonko butakoreshejwe. Ariko rero, abakusanya imyanda barazana amafaranga y’ibikorwa kandi barashobora gutuma habaho uguhagarika ataco umuntu yiteze mu gihe c’ugushitsa porogarama, bikaba bituma badakwiriye gukora porogarama z’imirongo aho ibikorwa bihoraho ari ngirakamaro.


Rust ishika ku mutekano wo kwibuka ahanini biciye mu gusesangura ibintu bihoraho bikorwa mu gihe co gukoranya. Ico gikoresho gisuzuma kode y’inkomoko kandi gishobora kumenya nimba ibikorwa vyinshi vyo kwibuka bifise umutekano ataco bisaba gukusanya imyanda. Ku bibazo bidashobora kugenzurwa mu buryo butahinduka—nk’ugushika ku rutonde n’ibiharuro vy’igihe co gukora—Rust yinjiza amasuzuma y’imipaka atera ubwoba aho kwemera inyifato itasobanuwe. Ubwo buryo buratandukanye cane n’ibikoresho vyo gusesangura ibintu bihoraho biriho ku rurimi C na C++, vyasubiwemwo ku ndimi zitagenewe gusesangura ibintu bihoraho mu buryo burambuye. Amategeko y’inyuguti n’ururimi rwa Rust yarakozwe kuva mu ntango kugira ngo bishobore gusuzuma cane igihe co gukoranya, kugira ngo iyo porogarama imaze gukoranya neza, izokora neza canke igatera ubwoba nk’uko vyari bitegekanijwe aho kwerekana inyifato itasobanuwe.


### Uburyo bwa Ownership: Amategeko n’Ingingo ngenderwako


Ibuye ry'imfuruka ry'umutekano w'ubwenge bwa Rust ni uburyo bwo kuba nyirayo, bugenzura ingene ubwonko bucungirwa mu gihe cose porogarama imaze gushirwaho. Ownership ikoresha amategeko atatu y’ishimikiro umukozi w’ivy’ubuhinga akurikiza ibihe vyose:


1. Agaciro kose kari muri Rust gafise nyen’ako (umuhinduzi afise agaciro)

2. Hashobora kuba nyen’umutungo umwe gusa ku gihe .

3. Iyo nyen'umutungo agiye hanze y'urugero, agaciro karagabanywa .


Ivyiyumviro biri muri Rust bisobanurwa n'ibimenyetso bigoramye, haba mu mibiri y'ibikorwa, mu bice vy'ivyangombwa, canke mu bice vy'ivyigwa vyaremwe mu buryo butomoye. Iyo umuhinduzi amenyeshejwe mu rwego, urwo rwego ruca ruba nyen'agaciro k'umuhinduzi. Ihinduka riguma rishikira kandi rifise akamaro mu kiringo cose c'ubuzima bw'urugero, ariko igihe igikorwa kiva mu rugero, ibihinduka vyose vy'umuntu bica bisukurwa biciye mu nzira yitwa gutera.


Ivyo gusukura vyikora bishirwa mu ngiro biciye ku buryo bwo gutera bwa Rust, aho ururimi ruhamagara mu buryo butagaragara igikorwa co gutera ku bihinduka biva hanze y'urugero. Ku bwoko bw'ishimikiro, ivyo bisigura gusa ko ubwonko bushizweko ikimenyetso c'uko buboneka kugira ngo busubire gukoreshwa. Ku bwoko bukomeye cane bucungera ibikoresho, gushirwa mu ngiro kw'ibintu bishobora gukora ibindi bikorwa vyo gusukura, nko gufunga ibikoresho vya dosiye canke kurekura amahuza y'urubuga. Iyi nzira, yaguzwe muri RAII ya C++ (Resource Acquisition Is Initialization), ituma ibikoresho vyama bisohoka neza ataco bisaba kode y’isuku igaragara ku muntu akora porogarama.


### Kwimura Ownership n'Imiterere y'Ukwibuka


Gutahura ingene ubutunzi bugenda hagati y’ibihinduka bisaba gusuzuma itandukaniro hagati y’ubwoko bworoshe n’ubwoko bugoranye mu bijanye n’imiterere y’ubwenge n’inyifato yo kwigana. Ubwoko bworoshe nk'imibare yose, booleans, n'imibare y'inyuguti ziterera zifise ubunini buhoraho, buzwi igihe co gukora kandi zishobora gukoporwa neza. Iyo ushizeho umuhinduzi umwe w'umubare wose uwundi, Rust irema kopi yuzuye, yigenga y'agaciro, igatuma ivyo bihinduka vyose bibaho icarimwe ata ngorane z'ubunywanyi.


Ubwoko bukomeye nk'imirongo buratanga ingorane itandukanye kubera ko bucungera ubwonko bugenewe. Urudodo muri Rust rugizwe n'ibice bitatu bibitswe ku rutonde: ikimenyetso c'amakuru y'inyuguti yatanzwe n'ikirundo, uburebure bw'urudodo, n'ubushobozi bwose bw'ububiko bwatanzwe. Uwo mubumbe utuma imirongo ikura kandi igabanuka neza mu gihe iguma izi imbibe zayo. Iyo ushizeho umuhinduzi umwe w'urudodo ku wundi, Rust ihanganye n'ihitamwo: yoshobora gukopa gusa imiterere ishingiye ku kirundo (guhingura ibimenyetso bibiri ku makuru y'ikirundo kimwe) canke gukora kopi yimbitse y'amakuru yose y'ikirundo.


Inyifato ya Rust ni ukwimurira ubutunzi aho kwimurira kopi, kwimurira amakuru y'ikirundo kuva ku mpinduka y'inkomoko ku mpinduka y'aho ija no guhindura inkomoko. Ubu buryo burabuza ikintu giteye akaga aho ibihinduka vyinshi bishobora guhindura ubwonko bumwe bw’ikirundo canke aho ubwonko bumwe bwoshobora kurekurwa incuro nyinshi iyo ibihinduka bivuye mu rwego. Igikorwa kijanye n'ukwimura ni ciza kubera ko gikopa gusa umubumbe mutoyi ushingiye ku kirundo, atari amakuru ashobora kuba manini y'ikirundo, mu gihe kibungabunga umutekano w'ubwenge mu kumenya neza ko ari uwufise uburenganzira bumwe.


### Ivyerekeye n'ugutiza


Naho ukwimuka kw’ubutunzi gutanga umutekano, birashobora kuba bibuza igihe ukeneye gukoresha agaciro mu bibanza vyinshi utahinduye ubutunzi. Rust ivyifatamwo neza biciye mu kugurana, ivyo bikaba bituma ibikorwa n’ibihinduka bishobora kuronka amakuru mu gihe gito ataco bifata. Igikoresho, cakozwe hakoreshejwe umukoresha w'ampersand, gitanga uburenganzira bwo gusoma gusa ku gaciro mu gihe gisiga uburenganzira n'umuhinduzi w'intango.


Ivyerekeye bituma ibikorwa bishobora gukora ku makuru bitayakoresheje, bikaba bishoboka gukoresha agaciro kamwe incuro nyinshi muri porogarama yose. Iyo ushizeho ivyerekanwa ku gikorwa, uba uriko uragurisha amakuru mu gihe gito, kandi igikorwa kigomba kugarura ivyerekanwa imbere y'uko nyen'igikorwa c'intango ashobora gusubira kugenzura vyose. Iryo jambo ry’ikigereranyo ry’ugutiza ryerekana kamere y’igihe gito y’ugushikira: nk’uko nyene woshobora kuguriza igitabu umugenzi mu gihe uguma ufise uburenganzira bwo kugironka, ibisobanuro bituma umuntu ashobora kuronka igitabu mu gihe gitoyi mu gihe uguma ufise ubucuti bw’uburenganzira bwo kuronka igitabu c’intango.


Ivyiyumviro bishobora guhinduka biragwiza ico ciyumviro kugira ngo vyemeze guhindura amakuru yaguzwe, ariko hakaba hariho amategeko akomeye kugira ngo umuntu agumane umutekano. Rust yemera gusa guhindura ikintu kimwe ku gice c'amakuru igihe cose, bikabuza amarushanwa y'amakuru aho ibice vyinshi vya porogarama bishobora guhindura icarimwe ubwonko bumwe. Ikindi, ntushobora kugira ibisobanuro bihinduka n'ibidahinduka ku makuru amwe icarimwe, kuko ivyo bishobora gutuma haba ibintu aho kode yiyumvira ko amakuru ahagaze neza mu gihe iyindi kode iriko irayahindura. Aya mategeko arashirwa mu ngiro mu gihe co gukoranya, akuraho ivyigwa vyose vy’ibibazo vy’ugukorana bitera ingorane izindi ndimi zo gukora porogarama.


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


### Ubwoko bw'imirongo n'ibice


Rust itandukanya hagati y'amajambo y'urudodo n'ubwoko bw'urudodo, yerekana ingamba zitandukanye zo gucunga ubwenge n'ibikorwa. Inyuguti z'urudodo zishizwe mu buryo butaziguye mu rutonde rw'ibiharuro kandi zifise ubwoko &str (igice c'urudodo), zigereranya ukuntu umuntu abona mu makuru y'urudodo adahinduka. Ivyo bimenyetso birakora neza kuko ntibisaba gutanga umwanya wo gukora, ariko ntibishobora guhindurwa kuko biri muri kode ya porogarama.


Ubwoko bw'urudodo, mu buryo butandukanye, bucungera ububiko bugenewe kandi bushobora gukura, kugabanuka, no guhindurwa mu gihe co gukora. Ushobora kurema Urudodo kuva ku rurimi rw'ikirundi ukoresheje Urudodo::kuva () canke uburyo busa n'ubwo, butanga ububiko bw'ikirundo kandi bugakopa ibirimwo ijambo ry'ikirundi. Iryo tandukaniro rituma Rust ishobora gukora neza (ikoresheje amajambo nyayo iyo bishoboka) be n’uguhinduranya (ikoresheje String iyo bikenewe guhindura).


Ivyiyumviro vy'imirongo (&str) bitanga ubuhinga bukomeye bwo gukorana n'ibice vy'imirongo ata gukopa amakuru. Igipande kirimwo ikimenyetso c'intango y'amakuru y'urudodo n'uburebure, bigufasha gukoresha neza urudodo ruto. Inyuguti y'ibice ikoresha ibice (nk'akarorero, &s[0..5]) kugira ngo ugaragaze igice c'urudodo co gukoresha. Kubera ko ibice ari ibisobanuro, bitegekanijwe n'amategeko yo kugurana, bikabuza urudodo ruri munsi guhindurwa mu gihe ibice biriho. Iyi nzira y'igihe co gukoranya ibuza ibibazo bisanzwe nk'ugushika ku bubiko butagira akamaro inyuma y'aho urudodo rw'intango rubohowe canke ruhinduwe.


### Imirongo, Vectors, n'Ibice rusangi


Iciyumviro c'igice kirarenga imirongo ku rutonde urwo ari rwo rwose rw'ibintu, kigatanga uburyo bumwe bwo gukorana n'imirongo y'ubunini budahinduka n'imirongo y'inguvu. Ivyiyumviro biri muri Rust bifise uburebure bwavyo bushizwe mu bwoko bwavyo (nk'akarorero, [i32; 5] ku vyiyumviro vy'imibare itanu y'ibice 32), bikaba bituma bibereye ku bihe bisaba igihe co gukora. Imikorere yemera amabara ishobora gushitsa uburebure nyabwo busabwa, ngirakamaro ku bikorwa nk'imikorere y'ububiko bw'ibanga ikeneye inyungu zifise ubunini nyabwo.


Ivyiyumviro (&[T]) bitanga ubundi buryo bwo guhindura, bugereranya ukuntu umuntu abona mu rutonde rw'ibintu rwose rufatanye ataco bimaze ububiko buri munsi. Ushobora kurema ibice bivuye mu mirongo, amavector, canke ibindi bice, kandi igice kimwe gishobora kwerekeza ku bice bitandukanye vy'amakuru mu buzima bwaco bwose. Ukwo guhinduranya bituma ibice biba vyiza ku bikorwa bikeneye gukora urutonde ata kwitwararika uburyo bwo kubika canke ubunini nyabwo.


Isano hagati y'ubwoko bw'ibintu (String, Vec<T>) n'ibindi bice vy'ibintu (&str, &[T]) bikurikira uburyo bumwe muri Rust yose. Ubwoko bw'ibintu bucungera ubwonko bwabwo kandi burashobora guhindurwa, mu gihe ibice bitanga uburyo bwiza, bwo gusoma gusa ku bice vy'ayo makuru. Iyi nzira ishoboza APIs zishobora guhinduka (zemera ubwoko butandukanye bw’inyungu biciye mu bice) kandi zikora neza (zirinda gukopa bidakenewe), mu gihe zigumya ivyemezo vy’umutekano vya Rust biciye mu buryo bwo kugurana.



## Inyubako, Ubwoko bw'amakuru agoranye

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Ivyubatswe muri Rust bikora nk’umushinge wo kurema ubwoko bw’amakuru butoroshe, asa n’amashure yo mu zindi ndimi zo gukora porogarama. Bigufasha gukoranya amakuru ajanye hamwe mu gice kimwe, gifatanye gishobora kubamwo ivyicaro vyinshi vy’ubwoko butandukanye. Inyuguti yo gusobanura umubumbe ikurikira uburyo bugororotse: ukoresha ijambo ry'ingenzi `struct` rikurikiwe n'izina ry'umubumbe, hanyuma ugasobanura ivyicaro biri mu bimenyetso bigoramye ukoresheje inyuguti y'inyuguti kugira ngo ugaragaze ubwoko bw'umurima wose.


Rust ikurikira amategeko yihariye yo gutanga amazina ku mibumbe umukozi azoshira mu ngiro biciye ku ngabisho. Amazina y'imibumbe akwiye gukoresha CamelCase (izwi kandi nka PascalCase), mu gihe amazina y'imirima mu mibumbe akwiye gukoresha snake_case n'imirongo. Iryo koraniro rifasha kugumana ubumwe mu bibanza vyose vya kode vya Rust kandi rituma kode isomwa n'abandi bategura.


Gukora ingero z'imiterere bisaba ko ugaragaza agaciro k'imirima yose ukoresheje izina ry'imiterere ikurikiwe n'ibimenyetso vy'imiterere birimwo ibikorwa vy'imiterere. Iyo ufise urugero rw'imiterere, ushobora gushika no guhindura ivyicaro bimwe bimwe ukoresheje akamenyetso k'utudomo, igihe urugero rwamenyeshejwe ko rushobora guhinduka. Iyi nkuru y'utudomo ikora neza muri Rust, itandukanye n'indimi nka C++ aho ushobora gukoresha abakozi batandukanye ku bimenyetso n'ibintu bitaziguye.


### Imikorere y'ubwubatsi n'inzira ngufi z'umurima


Rust nta vyubatswemwo nk'indimi zimwe zimwe zishingiye ku bintu, ariko ushobora kurema ibikorwa bigarura ingero z'imiterere kugira ngo bikoreshe intumbero imwe. Iyi mikorere y'ubwubatsi ifata amaparametere ku bibanza bimwe canke vyose kandi ishobora gushinga agaciro mburabuzi ku bindi. Igihe wandika izo nshingano, Rust itanga ururimi rugufi rworoshe: iyo parameter ifise izina rimwe n'umurima w'imiterere, ushobora gusa kwandika izina ry'umurima rimwe aho kurisubiramwo mu buryo bwa `umurima: agaciro`.


Inkuru z'imiterere zishobora kandi kuremwa mu gukopa agaciro kuva ku nkuru zihari hakoreshejwe insiguro y'ivugurura ry'imiterere. Iki kintu kigufasha kurema urugero rushasha mu gihe ugaragaza gusa ivyicaro ushaka guhindura, n'ibindi bibanza vyose bikopiwe bivuye ku nkuru iriho. Ariko rero, iki gikorwa gikurikiza amategeko y’ubutunzi ya Rust, bisobanura ko ubwoko butagira Kopi buzokwimurirwa mu nkuru y’inkomoko, bishobora gutuma ibice vy’inkuru y’intango bidashobora gukoreshwa inyuma. Ico gikoresho gikurikirana izo nzira z’ibice mu buryo bw’ubwenge, kikagufasha kubandanya ukoresha imirima itahinduwe mu gihe ubuza gushika ku mirima yimuriwe.


### Imibumbe ya Tuple n'imibumbe y'ibice


Rust ishigikira imibumbe ya tuple, ariyo mibumbe ifise ivyicaro bitagira izina bishikirizwa n'urutonde aho gushikirwa n'izina. Ivyo ni ngirakamaro ku bwoko bworoshe bw'ibizingira canke igihe ukeneye umubumbe ariko udakeneye ivyicaro vy'amazina. Ushobora gushika ku bibanza vy'imiterere y'ibice ukoresheje utudomo dukurikiwe n'urutonde rw'ibibanza, nka `.0` ku bibanza vya mbere, `.1` ku bibanza vya kabiri, n'ibindi. Ubu buryo burakora neza ku mibumbe izingira agaciro kamwe canke irimwo agaciro gatoyi gusa gafitaniye isano cane aho amazina yoshobora kuba arengeye.


Ivyiyumviro vy’ibice bigereranya uburyo bworoshe kuruta ubundi bwose bw’imiterere—nta makuru na gato birimwo. Naho ivyo vyoshobora gusa n’ibitagira akamaro mu ntango, imibumbe y’ibice iragira agaciro iyo ikorana n’uburyo bw’imico ya Rust, kuko ishobora gushitsa inyifato ata makuru na make ibitswe. Ivyo bibanza vy’ubusa bikora nk’ibimenyetso canke ibibanza mu mirongo ya Rust iteye imbere cane.


### Uburyo n'imikorere ijana


Inyubakwa zironka ibikorwa vy'inyongera iyo wongeyeko inyifato biciye mu bice vy'ishyirwa mu bikorwa. Ukoresheje ijambo ry'ingenzi `impl` rikurikiwe n'izina ry'imiterere, ushobora gusobanura uburyo bukora ku nkuru z'imiterere yawe. Uburyo ni ibikorwa bifata `self` nk'igipimo ca mbere, gishobora kuba agaciro k'umuntu (`self`), ishingiro ridahinduka (`&self`), canke ishingiro rihinduka (`&mut self`), bivanye n'ico uburyo bukeneye gukora n'instance.


Ihitamwo ry'ubwoko bw'imirongo `ubwiwe` rigena inyifato y'uburyo ku bijanye n'ubunywanyi. Uburyo bufata `&self` burashobora gusoma kuva ku nkuru ataco bufata, bikaba bituma bubereye ibikorwa bitahindura imiterere. Uburyo bufata `&mut self` burashobora guhindura instance mu gihe buca bureka uwuhamagara kuguma afise ububasha. Uburyo bufata `ubwiwe` ku gaciro burarya urugero, ivyo bikaba bibereye ku bikorwa bihindura umubumbe mu kindi kintu canke igihe uburyo bugereranya igikorwa ca nyuma kuri urwo rugero.


Imikorere ifatanye ni imikorere isobanuwe mu gice c'ishyirwa mu ngiro idafata `self` nk'umurongo. Ivyo bisa n'uburyo butahinduka mu zindi ndimi kandi bikoreshwa cane nk'ibikorwa vy'ubwubatsi canke ibikorwa vy'ubuhinga bijanye n'ubwoko. Uhamagara ibikorwa bifitaniye isano ukoresheje insiguro y'inyuguti zibiri (`Ubwoko::izina_ry'ibikorwa()`), ribitandukanya neza n'uburyo buhamagarwa ku nkuru.


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


#### Ibara: Amahitamwo y'Ivyitegererezo n'Ibihinduka


Ivyiyumviro biri muri Rust birafise ubushobozi bwinshi kuruta ivyiyumviro biri mu zindi ndimi nyinshi. Naho bishobora guserukira imigwi yoroshe y'ibidahinduka vy'amazina, Rust enums zishobora kandi gutwara amakuru muri buri mpinduka, bikaba bituma zibereye gushushanya ibintu aho agaciro gashobora kuba kamwe mu bwoko canke intara zitandukanye. Buri mpinduka y'ibara ishobora kubamwo ubwoko butandukanye n'ingero z'amakuru, kuva ku nta makuru na gato gushika ku mibumbe igoranye ifise ivyicaro vy'amazina.


Ubushobozi bwo gufatanya amakuru n'ibihinduka vy'ibara burakuraho amakosa menshi asanzwe yo gukora porogarama aboneka mu zindi ndimi. Aho kubungabunga ibihinduka bitandukanye ku kimenyetso c’ubwoko n’amakuru ajanye—ashobora guhinduka bitagoranye—Rust enums zifatanya amakuru y’ubwoko n’amakuru ubwayo. Iyi nzira ituma amakuru yama ahuye n’ivyo ahinduye, bikabuza ukudahuza bishobora gutuma haba amakosa mu gihe co gukora.


Impinduka za Enum zishobora kubamwo amakuru mu buryo bwinshi: nta makuru y'amabendera yoroshe, amakuru ameze nk'ay'ibibanza bitagira izina, canke amakuru ameze nk'ay'imiterere n'ibibanza vy'amazina. Ushobora mbere kuvanga iyo mico mu rutonde rumwe, ugahitamwo uburyo bukwiye kuri buri mpinduka. Ukwo guhindura bituma enums zibereye gushushanya ivyiyumviro bikomeye vy'intara aho ibintu bitandukanye bisaba amakuru atandukanye.


#### Ubwoko bw'amahitamwo: Gufata neza ukubura


Imwe mu nkuru zihambaye cane za Rust ni `Ihitamwo<T>`, igereranya agaciro gashobora kubaho canke kutabaho. Iyi enum ifise uburyo bubiri: `Some(T)` irimwo agaciro k'ubwoko T, na `Nta` igereranya ukutagira agaciro. Ubwoko bw'Ihitamwo bukora nk'umuti wa Rust ku bibazo vy'ibimenyetso vy'ubusa bitera ingorane izindi ndimi nyinshi, bikaba bihatira abahinguzi gukora neza ibibazo aho agaciro gashobora kubura.


Gukoresha ubwoko bw'amahitamwo bituma kode yawe ikomeye cane kuko umukozi agusaba gukorana n'ukubaho n'ukutabaho kw'agaciro. Ntushobora gukoresha mu mpanuka agaciro gashobora kubura utabanje kugenzura nimba kariho. Ukwo gukoresha gutomoye kubuza ibidasanzwe vy'ibimenyetso vy'ubusa n'amakosa asa n'ayo y'igihe co gukora ari inkomoko rusangi y'ibibazo mu zindi ndimi za porogarama.


Ubwoko bw’Ihitamwo burafatanya n’uburyo bwo guhuza ivyitegererezo bwa Rust, bikagufasha gukora ivyo bibazo vyose bibiri. Uburyo nka `unwrap_or()` butanga uburyo bwiza bwo gukuraho agaciro n'ibiharuro vy'inyuma, mu gihe uburyo nka `map()` na `and_then()` bushobora gukoresha porogarama zikorana n'agaciro k'ubusa.


### Urugero rwo guhuza n'imvugo zihuye


Guhuza ivyitegererezo biciye mu mvugo `guhuza` bitanga uburyo bwo gukorana n'ibiharuro n'ubundi bwoko bw'amakuru. Invugo ihuye isuzuma agaciro maze igakora kode itandukanye ishingiye ku citegererezo agaciro gahuye. Igishushanyo cose gishobora gusenyura agaciro kahuye, kigafatanya ibice vyaco ku bihinduka bishobora gukoreshwa mu gice ca kode gihuye.


Invugo zihuye zitegerezwa kuba zishitse, bisobanura ko zitegerezwa gukorana n'ikibazo cose gishoboka ku bwoko buriko burahuzwa. Ico gisabwa kirinda ibikoko bishobora gushika iyo hari ibintu bimwebimwe bisigaye bitafashwe ku mpanuka. Iyo udashaka gufata ikibazo cose mu buryo butomoye, ushobora gukoresha urugero rw'inyuguti (`_`) kugira ngo ufate ibibazo vyose bisigaye, canke ubohe ibibazo bitafashwe n'umuhinduzi niba ukeneye gushika ku gaciro.


Inyubako ya `if let` itanga ubundi buryo butomoye bwo guhura iyo witwararika gusa urugero rumwe rudasanzwe. Iyi nsiguro ni ngirakamaro cane iyo ukorana n'ubwoko bw'amahitamwo canke iyo ushaka gukora kode gusa iyo agaciro gahuye n'umuhinduzi w'ibara. `if let` construct ishobora kubamwo `else` clause ku bibazo aho urugero rudahuye, bikaba ari uburyo bworoshe bwo gukorana n'urugero rworoshe.


#### Amakoraniro: Gucungera amatsinda y'amakuru


Ico kibanza c'ibitabu ca Rust gitanga ubwoko bwinshi bw'amakuru yo gucungera imigwi y'amakuru ajanye. Izo nkuru ni rusangi, bisobanura ko zishobora kubika ibintu vy’ubwoko bwose, kandi zikora uburongozi bw’ubwenge ubwazo. Amakoraniro akoreshwa cane ni ama vectors y'urutonde rwategekanijwe, amakarata y'amakuru y'agaciro k'urufunguzo, n'imirongo y'amakuru y'inyandiko.


#### Vectors: Imirongo y'inguvu


Vectors zigereranya ama arrays ashobora gukura ashobora guhindura ubunini mu gihe porogarama iriko irashirwa mu ngiro. Mu buryo butandukanye n'imirongo y'ubunini butahinduka, ama vecteur atanga ubwonko ku kirundo kandi ashobora kwaguka canke kugabanuka uko bikenewe. Guhingura umurongo akenshi bisaba gusobanura ubwoko butomoye igihe utanguye n'umurongo utagira ikintu, kuko uwukora umurongo akeneye kumenya ubwoko bw'ibintu umurongo uzoba urimwo.


Vecteurs zitanga uburyo bwinshi bwo gushika ku bintu, kimwe cose kikaba gifise ibiranga umutekano bitandukanye. Igiharuro c'urutonde (`vec[0]`) gitanga uburyo bwo gushikako ariko kizotera ubwoba iyo urutonde ruri hanze y'imipaka. Uburyo bwa `get()` bugarukana `Ihitamwo`, buguha uburenganzira bwo gukoresha neza ukuronka hanze y'imipaka. Guhitamwo hagati y’izo nzira bivana n’uko ushobora kwemeza ko urutonde rufise akamaro canke ko ukeneye gutorera umuti ibishobora kunanirwa.


Amategeko y’inguzanyo ya Rust akora ku ma vecteur, akabuza ibibazo rusangi vy’umutekano w’ukwibuka. Niwaba ufise ivyerekeye ikintu c'umurongo, ntushobora guhindura umurongo gushika iyo nsiguro ivuye mu rwego. Ivyo bibuza ibintu aho ibisobanuro bishobora kwerekana ububiko butagenewe inyuma y'ibikorwa vy'umurongo nk'ugusunika ibintu bishasha canke gukuraho umurongo.


#### Ikarata ya Hash: Ububiko bw'agaciro k'urufunguzo


Ikarata za Hash zitanga ububiko bwiza bw'agaciro k'urufunguzo aho ushobora kwihuta kurondera agaciro bishingiye ku mfungurwa zijanye n'urufunguzo rwazo. Imfunguruzo n'agaciro vyose bishobora kuba vy'ubwoko bwose, naho imfunguruzo zitegerezwa gushitsa ibiranga bikenewe kugira ngo hashing n'ukugereranya uburinganire. Ikarata ya Hash ifata uburenganzira bw'agaciro kashizwemwo kiretse iyo agaciro gashize mu ngiro akaranga ko Kopa.


Ikarata ya Hash itanga uburyo bwinshi bwo kwinjiza no guhindura agaciro. Uburyo bw'ishimikiro bwa `insert()` buzokwandika agaciro kariho, mu gihe `entry()` itanga uburyo bwo kwinjiza bushobora guhinduka. Injira API ishobora kuguha uburenganzira bwo kwinjiza agaciro gusa iyo atariho, canke guhindura agaciro kariho bishingiye ku kuntu kari ubu. Iyi API ni ngirakamaro ku mirongo nk'uguharura ibibaye canke kubungabunga imibare yose y'urugendo.


Igihe utora agaciro ku makarita ya hash, uburyo bwa `get()` bugarukana `Ihitamwo` kuko urufunguzo rwasabwe rushobora kutabaho. Ushobora gukoresha uburyo nka `copied()` guhindura kuva kuri `Ihitamwo<&T>` ku `Ihitamwo<T>` ku bwoko bwa Kopi, na `unwrap_or()` kugira ngo ushireho agaciro mburabuzi iyo imfunguruzo zibuze.


### Ugukoresha imirongo na Unicode


Imirongo iri muri Rust ni UTF-8 encoded, itanga ubufasha bushitse bwa Unicode ariko izana ubugoyagoye ugereranyije n’imirongo yoroshe ya ASCII. Ubwoko bwa `String` bugereranya amakuru y'inyandiko afise, ashobora gukura, mu gihe ibice vy'urudodo (`&str`) bitanga ivyerekanwa vy'urudodo mu makuru y'urudodo. Ushobora guhindura hagati y'ubu bwoko nk'uko bikenewe, n'ibice vy'urudodo bikoreshwa kenshi ku mirongo y'imikorere kugira ngo wemere imirongo y'umunyagihugu n'amajambo y'urudodo.


Gukoresha imirongo birimwo uburyo bwo kwongerako umwandiko, guhindura agaciro kenshi hamwe, no gukura imirongo mito. Uburyo bwa `push_str()` bwongerako ibice vy'imirongo ataco bufata, mu gihe `format!` macro itanga uburyo bwo kwubaka imirongo ivuye mu bice vyinshi. Igihe ukorana n'ibimenyetso vy'imirongo, utegerezwa kwitwararika kwubahiriza imbibe z'inyuguti UTF-8 kugira ngo wirinde ubwoba bw'igihe co gukora.


Ku bijanye n'ugukora neza inyuguti ku nyuguti, imirongo itanga uburyo bwo gusubiramwo nka `chars()` ku gaciro ka Unicode na `bytes()` ku kuronka byte zidasanzwe. Izo iterators zikora neza UTF-8 encoding, zigatuma udashobora gucapura inyuguti nyinshi mu mpanuka. Ubwo buryo buratekanye kandi burashobora kwizigirwa kuruta gukoresha amaboko, cane cane iyo ukorana n’inyandiko mpuzamakungu zishobora kuba zirimwo inyuguti zikomeye za Unicode.



## Uburyo bwo gutorera umuti amakosa y'ivyiciro bibiri vya Rust

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust ifata uburyo butandukanye cane bwo gutorera umuti amakosa ugereranije n’indimi nyinshi zo gukora porogarama. Naho indimi nyinshi zishingiye ahanini ku bintu bidasanzwe, Rust itandukanya ivyiciro bibiri bitandukanye vy’amakosa kandi itanga uburyo bwihariye bwo gutorera umuti ubwoko bumwebumwe. Iki gice kiratohoza uburyo bwo gutorera umuti amakosa bushitse bwa Rust, kikaba kivuga ku makosa adashobora gusubirwamwo ahagarika ugushirwa mu ngiro kwa porogarama be n’amakosa ashobora gusubirwamwo atuma porogarama zikomeza gukora neza.


### Amakosa adashobora gusubirwamwo n'ubwoba


Amakosa adashobora gusubirwamwo agereranya ibintu aho porogarama yinjiye mu gihe kidahuye canke kitari citezwe aho idashobora gusubirwamwo ata nkomanzi. Ivyo birimwo ibintu nk’ugushika ku rutonde rutari ku rugero, kugerageza ibikorwa bihungabanya umutekano w’ubwenge, canke guhura n’ibintu vyerekana amakosa y’ishimikiro y’ubwenge bwa porogarama. Iyo mwene ayo makosa abayeho, inyishu ibereye ni uguhagarika iyo porogarama ubwo nyene aho gutera ingorane y’ibindi biturire canke inyifato idasobanutse.


Muri Rust, amakosa adashobora gusubirwamwo atuma umuntu agira ubwoba, ivyo bikaba bituma porogarama ihungabana mu buryo bugenzurwa. Imbere y’uko irangiza, Rust ikora igikorwa citwa unwinding, aho isubira inyuma ica mu gitereko c’amahamagara kugira ngo itange urutonde rw’ibirundo rw’ido n’ido rwerekana neza aho ubwoba bwabaye. Iyi nzira yo gufungura ifasha abahinguzi kumenya inkomoko y’ingorane mu gihe co gukosora. Ku bikorwa bihambaye cane canke ubuhinga bushizwemwo, urashobora guhagarika gufungura no gutunganya Rust kugira ngo ihagarike ubwo nyene iyo habaye ubwoba, naho ivyo bitanga amakuru yo gukosora kugira ngo ihereze vuba.


Ushobora gutera ubwoba ukoresheje `ubwoba!` macro n'ubutumwa busanzwe. Iyo habaye ubwoba, uzobona igisohoka kigaragaza urudodo rwateye ubwoba n'ubutumwa bujana. Gushinga `RUST_BACKTRACE` ibidukikije bihinduka bitanga amakuru y'inyongera yo gukosora, yerekana urutonde rw'amahamagara rwose rwatumye haba ubwoba. Nk'akarorero, kugerageza gushika ku kintu 99 c'umurongo urimwo ibintu bitatu gusa bizoba generate ubwoba bufise ubutumwa "index out of bounds", hamwe n'inyuma yerekana urutonde nyarwo rw'amahamagara y'ibikorwa vyatumye haba ikosa.


### Amakosa ashobora gusubirwamwo n'igisubizo


Amakosa ashobora gusubirwamwo agereranya ibintu vyitezwe vyo kunanirwa porogarama zishobora gukora neza ataco ziheze. Ingero ni nk'ukugerageza gufungura dosiye itahari, ukunanirwa kw'ihuriro ry'urubuga, canke inyungu y'umukoresha idakwiriye. Kubera ivyo bihe, Rust itanga `Igisubizo` enum, kigaragaza neza ibikorwa bishobora kunanirwa kandi kigahatira abahinguzi gukorana n'ibibazo vy'uguterimbere n'ugutsindwa.


Igiharuro ca `Igisubizo` gisobanurwa n'ibihinduka bibiri: `Ok(T)` ku bikorwa vyiza birimwo agaciro k'ubwoko `T`, na `Err(E)` ku kunanirwa birimwo ikosa ry'ubwoko `E`. Iyi nzira ikoresha uburyo bw’ubwoko bwa Rust kugira ngo ibintu bishobora kunanirwa ntibishobora kwirengagizwa. Imikorere ishobora kunanirwa igarura `Igisubizo`, kandi kode yo guhamagara itegerezwa gukora neza ivy'uguterimbere n'ivy'amakosa, kenshi hakoreshejwe uburyo bwo guhuza n'imvugo `guhuza`.


Rimbura `Dosiye::fungura` igikorwa, kigarura `Igisubizo<Dosiye, std::io::Ikosa>`. Iyo ufunguye dosiye, uronka ikintu `Dosiye` iyo bishoboka canke `std::io::Error` iyo igikorwa kidashoboka. Ushobora guhura kuri iki ciyumviro kugira ngo ukoreshe neza ikibazo cose. Mu gihe c'uguterimbere, ushobora gukomeza n'ibikorwa vya dosiye, mu gihe mu gihe c'ikosa, ushobora kugerageza kurema dosiye, kugerageza uburyo bundi, canke gukwiragiza ikosa kuri kode y'uguhamagara. Ukwo gukoresha gutomoye gutuma porogarama yawe ifata ingingo zijanye n’ugusubiza amakosa aho gusenyuka ataco yiteze.


### Ikosa ryo gutorera umuti uburyo n'inzira ngufi


Naho guhuza ivyitegererezo bigaragara bitanga ubugenzuzi bushitse ku bijanye no gutorera umuti amakosa, Rust itanga uburyo bwinshi bwo gutorera umuti amakosa asanzwe. Uburyo bwa `unwrap` bukura agaciro k'uguterimbere mu `Igisubizo` ariko bugatera ubwoba iyo habaye ikosa, bikaba bituma biba ngirakamaro mu gukora ivyerekanwa vyihuse canke mu bihe aho wizigiye ko igikorwa kizororanirwa. Uburyo bwa `expect` burakora gutyo nyene ariko buragufasha gutanga ubutumwa bw'ubwoba busanzwe, bigatuma gukosora vyoroha iyo ibintu bigenda nabi.


Kugira ngo ushobore gutorera umuti amakosa, uburyo nka `unwrap_or_else` buraguha uburenganzira bwo gutanga ugufunga gukora iyo ikosa ribaye, bishoboza gusubizaho uburyo busanzwe. Ushobora gufatanya ivyo bikorwa kugira ngo ukoreshe ibintu bikomeye, nk'ukugerageza gufungura dosiye no kuyirema iyo itahari, ufise ingamba zitandukanye zo gukorana n'amakosa ku ntambwe yose.


Igikoresho c'ikimenyetso c'ikibazo (`?`) gitanga insiguro ndende y'ugukwiragira kw'amakosa, ivyo bikaba bisanzwe muri porogarama za Rust. Iyo wongeyeko `?` ku `Igisubizo`, bihita bifungura agaciro kashoboye maze bikagarura amakosa ubwo nyene bivuye ku gikorwa kiriho. Iyi operator ishobora gukoreshwa gusa mu bikorwa bigarura ubwoko bwa `Igisubizo`, kugira ngo amakosa ashobore gukwiragizwa neza hejuru y'ikirundo c'amahamagara. Igikoresho ca `?` gituma kode yo gufata amakosa ishobora gusomwa cane mu gukuraho amajambo ahuye n'amajambo menshi mu gihe kigumya insobanuro y'ugukwiragira kw'amakosa.


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


### Ikosa ry'ukwiragira n'imiterere y'imikorere


Ugukwiragiza amakosa ni iciyumviro nyamukuru mu gufata amakosa ya Rust, bituma ibikorwa bishobora guca amakosa hejuru y'ikirundo c'amahamagara aho kuyafata mu karere. Igihe ukora ibikorwa bishobora kunanirwa, ushobora kugarura ubwoko bwa `Igisubizo` kugira ngo uhe abahamagara uburenganzira bwo gufata ingingo y'ingene bofata amakosa. Ubu buryo burateza imbere ugufata amakosa aho igikorwa cose mu ruhererekane rw’uguhamagara gishobora gufata amakosa mu karere canke kikayarungika kuri kode yo ku rwego rwo hejuru ifise ikibanza kinini co gufata ingingo zo gusubirana.


Igikoresho c’ikimenyetso c’ikibazo kirosha gukwiragiza amakosa. Aho kwandika amajambo y'uguhuza ku gikorwa cose gishobora kunanirwa, ushobora gufatanya ibikorwa hamwe n'abakoresha `?`, ugakora kode isomwa ifata inzira y'uguterimbere mu gihe ikwiragiza amakosa yose ashobora kubaho. Iyi nzira irasanzwe cane ku buryo ibikorwa vyinshi vya Rust vyateguwe cane cane kugira ngo bikore neza n'umukoresha wa `?`, bikaba bishoboza gukora neza amakosa mu rutonde rwawe rwose.


Igihe ufata ingingo hagati y’amakosa yo gutera ubwoba n’ayo gusubiza, zirikana nimba kode y’uguhamagara ishobora gusubirana mu buryo bubereye kubera ukunanirwa. Iyo ukunanirwa kugereranya ikosa ryo muri porogarama canke ikibazo c’urutonde rudashobora gusubirana, gutera ubwoba birabereye. Ariko rero, iyo ukunanirwa ari ikintu citezwe ko kode yo guhamagara ishobora gukora mu buryo butandukanye bivanye n'aho iri, kugarura `Igisubizo` bitanga uguhinduranya neza n'ugukoranya.


### Ivyiza vyo gukora n'ivyo kwiyumvira


Gutorera umuti neza amakosa muri Rust bisaba kwiyumvira neza igihe co guhagarika umutima n’igihe co gusubiza amakosa. Koresha ubwoba ku bihe bigereranya amakosa yo gukora porogarama canke ibihugu bidakwiye kwigera bibaho muri porogarama zigororotse, nk’ugushika ku makuru akomeye uzi ko ari meza. Nk'akarorero, gusesangura urudodo rwa aderesi IP rwakozwe n'amakode akomeye wasuzumye ko ari ukuri birashobora gukoresha `expect` n'ubutumwa busobanura igituma igikorwa kitagomba kwigera kinanirwa.


Ku bijanye n'inyandiko igenzurwa n'ukoresha canke imigenderanire y'inyuma, wama uhitamwo kugarura ubwoko bwa `Igisubizo` aho guhagarika umutima. Abakoresha barakora amakosa, amadosiye arafutwa, n’amahuza y’urubuga arananirwa – ivyo ni ibintu bisanzwe porogarama zateguwe neza zikwiye gukora neza. Mu kugarura amakosa y'ivyo bihe, wemera ko kode yo guhamagara ishira mu ngiro ingamba zibereye zo gusubizaho, yaba ari ugutuma umukoresha yinjiza ibintu bitandukanye, gusubira ku gaciro ka mbere, canke kwerekana ubutumwa bw'amakosa bufasha.


Niwiyumvire kurema ubwoko busanzwe bushira mu ngiro kwemeza mu gihe c'ubwubatsi kugira ngo ubuze ibihugu bitagira akamaro gukwiragira biciye muri porogarama yawe. Nk'akarorero, nimba porogarama yawe isaba imibare iri mu rutonde runaka, rema ubwoko bw'igipfukisho cemeza ivyinjijwe mu gihe c'ubwubatsi kandi nta buryo butanga bwo kurema ingero zidafise akamaro. Ubu buryo bukoresha uburyo bw'ubwoko bwa Rust kugira ngo ukureho amakosa yose mu gutuma ibihugu bitagira akamaro bidashobora guserukira, bikagabanya ivy'ugusuzuma amakosa y'igihe co gukora mu rutonde rwawe rwose.


## Ibirango vya porogaramu ikora, gufunga n'ibimenyetso vy'ubwenge


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Naho Rust atari ururimi rwo gukora porogarama rutagira agasembwa, rushiramwo ibintu bihumekewe n’ibigereranyo vy’iporogarama zikora. Ivyo bifasha abahinguzi kwandika kode ngufi bakoresheje ivyiyumviro nk’ugufunga n’ugusubiramwo. Rust irimwo ivyo bintu bikora kugira ngo itange ibikoresho bishobora guhinduka vyo gutunganya amakuru n’uburyo bwo guhamagara.


Ivyo bikoresho bikoreshwa muri Rust biragumya ingingo ngenderwako nyamukuru z’ururimi zerekeye umutekano wo kwibuka be n’ibintu bitagira agaciro. Iyo ukoresheje ugufunga n’ugusubiramwo, ntuba uriko uratanga ibikorwa kugira ngo ugaragaze – umukozi wa Rust aratunganya neza ivyo vyubatswe kugira ngo akore kode y’imashini ikora neza igereranywa n’uburyo bwa kera bushingiye ku nzira.


### Gutahura ivy'ugufunga


Ivyugarijwe muri Rust ni ibikorwa bitazwi bishobora gufata ibihinduka biva mu bidukikije vyavyo. Mu zindi ndimi zo gukora porogarama, ivyo akenshi vyitwa ibikorwa vya lambda. Ikintu nyamukuru kiranga ibipfukisho ni ubushobozi bwavyo bwo "gufunga" ibidukikije vyavyo, bisobanura ko bishobora gushika no gukoresha ibihinduka biri mu rwego aho ugufunga gusobanurwa.


Inyuguti z'ugufunga zikoresha inyuguti z'imiyoboro (`|`) aho gukoresha uturongo kugira ngo zisobanure ibipimo. Ku gufunga ata mirongo, wandika `||`, kandi ku gufunga kufise imirongo, ubishira ku rutonde hagati y'imiyoboro nka `|x, y|`. Nimba umubiri w’ugufunga ugizwe n’imvugo imwe, urashobora gukuraho amajambo apfutse, ivyo bikaba bituma insiguro y’amajambo iba ndende cane.


Rimbura aka karorero ngirakamaro k’ishirahamwe ry’amashati ritanga amashati yihariye ashingiye ku vyo abakiriya bakunda. Iyo umukiriya yerekanye ibara akunda, bararonka iryo bara; ahandi ho, baronka ibara ryinshi cane nk'iry'imbere. Ukoresheje ugufunga, iyi nzira iba: `uguhitamwo_ukoresha.gufungura_canke_ibindi(|| ubwiwe.vyinshi_bibitswe())`. Ivyo gufunga `|| self.most_stocked()` itanga agaciro mburabuzi gusa iyo bikenewe, kandi ishobora gushika ku `self` ivuye mu bidukikije vyayo.


### Ubwoko bwo gufunga Inference n'uguhinduranya


Kimwe mu bintu vyiza cane vya Rust bifise ibipfukisho ni ugushiramwo ubwoko bwikora. Udakunze ibikorwa bisanzwe aho ugomba gusobanura neza ubwoko bw'ibipimo n'ubwoko bw'ibisubizo, gufunga bishobora kenshi gukuraho ubwo bwoko bivuye ku mirongo. Ico gikoresho gisuzuma ingene iyo nzira yo gufunga ikoreshwa maze kigaca kimenya ubwoko bukwiye. Ariko rero, iyo ugufunga guhamagawe n'ubwoko bumwe bumwe, ubwo bwoko buraba ubudahinduka kuri iyo nkuru y'ugufunga.


Ushobora kubika ivyugarijwe mu bihinduka nk'ibindi bipimo vyose, bikabagira abanyagihugu bo mu rwego rwa mbere mu rurimi. Iyo ushizeho ugufunga umuhinduzi, ushobora kuwuhamagara mu nyuma ukoresheje uturongo: `let my_closure = |x| x + 1; reka igisubizo = gufunga_kwanje(5);`. Uguhinduranya bigufasha guca mu gufunga nk'imvo ku bikorwa, kubigarura bivuye mu bikorwa, no kubikoresha mu miterere y'amakuru.


Niba umukozi adashobora gusobanura ubwoko canke nimba ushaka gusobanura neza, ushobora gutanga ibisobanuro ku mirongo y'ugufunga no kugarura ubwoko ukoresheje insiguro isa n'ibikorwa: `|x: i32| -> i32 {x + 1}`. Ukwo kwandika gutomoye rimwe na rimwe birakenewe mu bihe bikomeye aho umukozi akeneye amakuru y'inyongera kugira ngo atore umuti neza ubwoko.


### Gufata ibidukikije bihinduka


Ivyumba bishobora gufata ibihinduka biva mu bidukikije vyavyo mu buryo butatu butandukanye: biciye ku nsiguro idahinduka, biciye ku nsiguro ihinduka, canke mu gufata uburenganzira. Igikoresho ca Rust gica kigena uburyo bwo gufata buzitiye cane buhazwa n’ivyo ukeneye mu gufunga, hakurikijwe ingingo ngenderwako y’agateka gatoyi.


Iyo ugufunga gukeneye gusa gusoma agaciro, gufata biciye ku nsiguro idahinduka. Ivyo bituma umuhinduzi w'intango aguma ashobora gushikwako inyuma y'aho ugufunga gusobanuwe no guhamagarwa. Nk'akarorero, igipfukisho gicapura urutonde kizoguza urutonde ataco gihinduye, kiguhe uburenganzira bwo kubandanya ukoresha urutonde inyuma y'aho igipfukisho gishitse.


Niba ugufunga gukeneye guhindura umuhinduzi yafashwe, bitegerezwa gufatwa n'ihinduka ry'ihinduka. Muri iki gihe, umuhinduzi yafashwe n'ugufunga ubwavyo bitegerezwa kumenyeshwa ko ari ibihinduka. Ugufunga gushobora rero guhindura umuhinduzi yafashwe, ariko amategeko y’inguzanyo aracariho – ntushobora kugira ibindi bimenyetso vy’uwo muhinduzi mu gihe ugufunga guhinduka kuriho.


Uburyo bwo gufata buzitiye cane ni ugufata uburenganzira, bujana ibihinduka vyafashwe mu gufunga. Ivyo birakenewe igihe ugufunga bishobora kubaho kuruta urugero aho ibihinduka vyasobanuwe mu ntango, nk'igihe indodo zivyara. Ushobora guhatira gufata ubutunzi ukoresheje ijambo ry'ingenzi `kwimura` imbere y'imirongo y'ugufunga: `kwimura |x| { /* umubiri wo gufunga */ }`. Ivyo ni ngombwa kugira ngo indodo zibe zitekanye, kuko indodo zidashobora kugurana neza izindi ndodo zishobora guhera no gukuraho ibihinduka vyazo.


### Ibirango vyo gufunga n'ubwoko bw'imikorere


Rust igereranya ugufunga biciye mu buryo bw'ibiranga bifise ibiranga bitatu vy'ingenzi: `FnOnce`, `FnMut`, na `Fn`. Ivyo bimenyetso bikora urutonde rudondora ingene ibipfukisho bishobora kwitwa n’ico bishobora gukora ku bihinduka vyafashwe.


`FnOnce` ni akaranga k'ishimikiro kuruta ayandi yose amafunga yose ashira mu ngiro. Rigereranya ivyugarijwe bishobora guhamagarwa n’imiburiburi rimwe. Hariho ibifunga, cane cane ivyo bihindura agaciro kafashwe canke bikabirya mu buryo bumwe, bishobora guhamagarwa rimwe gusa kubera ko bihonya canke bihindura amakuru yavyo yafashwe mu gihe c’ugushirwa mu ngiro.


`FnMut` igereranya ibipfukisho bishobora kwitwa incuro nyinshi kandi bishobora guhindura ibidukikije vyavyo vyafashwe. Ivyo bifunga bifata ibihinduka biciye ku nzira zihinduka kandi bishobora kubihindura mu guhamagara kenshi. Amategeko y'inguzanyo atuma iyo `FnMut` ipfutse ikora, ifise uburenganzira bwo guhinduka bwihariye ku bihinduka vyayo vyafashwe.


`Fn` ni co kintu gikingira cane, kigereranya ugufunga gushobora kwitwa incuro nyinshi ata guhindura ibidukikije vyavyo vyafashwe. Ivyo bipfukisho bifata gusa biciye ku nsiguro idahinduka kandi bishobora guhamagarwa rimwe ataco bihungabanya ku bijanye n’umutekano wa Rust. Iyo ugufunga gushize mu ngiro `Fn`, bica bishira mu ngiro `FnMut` na `FnOnce` navyo nyene, kuko guhamagarwa incuro nyinshi ata mpinduka bisobanura guhamagarwa n'ihinduka no guhamagarwa rimwe.


### Gukorana n'abasubiramwo


Iterators muri Rust zitanga uburyo bwo gukora urutonde rw'amakuru. Ni ubunebwe, bisobanura ko ata gikorwa na kimwe bakora gushika ubariye mu guhamagara uburyo busubiramwo mu vy’ukuri biciye mu makuru. Iryo suzuma ry’ubunebwe rituma habaho uruhererekane rwiza rw’ibikorwa ata kurema amakoraniro yo hagati.


Igishushanyo `Iterator` gisobanura imikorere nyamukuru n'ubwoko bujanye n'ubwoko `Item` bugereranya ivyo iterator itanga, n'uburyo `bukurikira` bugarura `Ihitamwo<Self::Item>`. Igihe `ikurikira` igaruka `Nta`, iterator iraruha. Iyi nzira iremesha abasubiramwo guserukira urutonde rufise impera n'urushobora kutagira impera ata nkomanzi.


Ushobora kurema ibisubiramwo bivuye mu makoraniro ukoresheje uburyo nka `iter()` bwo gusubiramwo, `iter_mut()` ku gusubiramwo guhinduka, na `into_iter()` ku gusubiramwo. Guhitamwo hagati y’ubu buryo bivana n’uko ukeneye guhindura ibintu be n’uko ushaka gukoresha ivy’intango.


### Iterator n'abaguzi


Iterator adapters ni uburyo buhindura iterator imwe mu yindi, bikagufasha gukoranya ibikorwa. Ivyuma bisanzwe birimwo `ikarata` yo guhindura ikintu cose, `akayunguruzo` ko guhitamwo ibintu bishingiye ku nsiguro, na `enumerate` yo kwongerako urutonde. Ivyo bikoresho ni ubunebwe – nta gikorwa na kimwe bikora gushika bipfuye.


Uburyo bwa `ikarata` bukoresha ugufunga ku kintu cose, bukagihindura ikindi kintu. Nk'akarorero, `imibare.iter().ikarata(|x| x * 2)` irema iterateri igabanya kabiri umubare wose. Uburyo bwa `akayunguruzo` bugumya gusa ibintu ivyo gufunga kw'intangamarara bigarukana ukuri: `imibare.iter().akayunguruzo(|&x| x > 10)` bugumya gusa imibare irenze icumi.


Uburyo bw’abaguzi mu vy’ukuri burasubiramwo biciye mu makuru maze bukazana igisubizo ca nyuma. Uburyo bwa `collect` burarya iterator maze bukarema ikoraniro rivuye muri ryo. Kenshi ukeneye kugaragaza ubwoko bw'ikoraniro: `reka vec: Vec<_> = iterator.ikoraniro()`. Abandi baguzi barimwo `sum` yo kwongerako ibintu vy'imibare, `fold` yo kwirundanira agaciro n'igikorwa gisanzwe, na `for_each` yo gukora ingaruka mbi ku kintu cose.


### Ivyitegererezo vy'Iterator


Ibindi bikorwa vy'iterateri birimwo `zip` yo gufatanya iterateri zibiri mu buryo bw'ibintu, `uruzitiro` rwo gufatanya iterateri, na `filter_map` yo gufatanya ukuyungurura n'ikarita mu gikorwa kimwe. Uburyo bwa `zip` bukora amabiri abiri avuye mu bintu bihuye vy'ibisubiramwo bibiri: `a.iter().


Uburyo bwa `fold` ni ngirakamaro mu kwirundanira agaciro. Bifata agaciro k'intango n'ugufunga gufatanya umurundo n'ikintu cose: `imibare.iter().fold(0, |acc, x| acc + x)` ihuriza hamwe imibare yose. Iyi nzira ishobora gushitsa ibindi bikorwa vyinshi nk'ukurondera agaciro kanini, kwubaka imirongo, canke kurema imiterere y'amakuru igoranye.


Iminyorororo y'abasubiramwo ishobora guserura amahinduka y'amakuru agoranye mu buryo butomoye. Nk'akarorero, gutunganya amakuru y'amajwi bishobora kubamwo: `ibiharuro.iter().zip(ububiko.iter()).ikarita(|(c, b)| c * b).umubare::<i32>() >> 12`. Ivyo bigwiza ibiharuro bihuye n’agaciro k’ububiko, bikaja hamwe ibivuyemwo, bigahindura agaciro ka nyuma, vyose mu mvugo imwe isomwa.


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


### Intangamarara y'ibimenyetso vy'ubwenge


Ivyerekana vy’ubwenge ni imibumbe y’amakuru ikora nk’ivyerekana vya kera ariko itanga ubushobozi bwongereweko n’ugucungera ubwonko bwikora. Udakunze ibisobanuro vyoroshe, ibimenyetso vy'ubwenge birafise amakuru vyerekana kandi birashobora gushiramwo inyifato isanzwe y'ugutanga ubwonko, gukuraho, n'uburyo bwo kuronka. Ni ibikoresho vy’ingenzi vyo gucunga amakuru yatanzwe n’ibirundo no gushirwa mu ngiro uburyo bugoranye bwo kuba umunyamuryango burengeye uburyo bw’ubutunzi bwa Rust.


Ivyo biva ku bushobozi bwabo bwo gukora ibikorwa vyo gucunga ubwonko vyari gusaba ko umuntu akoresha amaboko. Iyo ikimenyetso c'ubwenge kivuye mu rwego, gishobora kwikurako ubwonko bujanye n'ivyo, kigabanya igitigiri c'ibiharuro, canke kigakora ibindi bikorwa vyo gusukura. Iyi nzira y’ubuhinga ifasha gukingira ukuvuza kw’ubwenge n’amakosa yo gukoresha-inyuma y’ubuntu mu gihe itanga uburyo bwo guhinduranya kuruta gutanga gusa.


Ivyerekana vy'ubwenge bishira mu ngiro ibiranga bibiri: `Deref` na `Drop`. Igishushanyo ca `Deref` kiremesha ikimenyetso c'ubwenge gikoreshwa nk'aho coba ari ikimenyetso c'amakuru arimwo. Igishushanyo `Drop` gishoboza gusukura igihe ikimenyetso c'ubwenge gisenyutse. Ivyo vyose hamwe, bituma ibimenyetso vy’ubwenge bishobora gucungera ubwonko ubwavyo.


### Agasanduku k'ubwenge


`Agasanduku<T>` ni ikimenyetso c'ubwenge gisanzwe, gitanga ikirundo c'ubwoko bwose `T`. Iyo uremye `Akazu`, agaciro karimwo kabikwa ku kirundo aho kubikwa ku kirundo, kandi `Agasanduku` ubwako (ari ryo kimenyetso gusa) kabikwa ku kirundo. Iyi indirection ni ngirakamaro igihe ukeneye kubika amakuru menshi utayahinduye, igihe ukeneye ubwoko butazwi ubunini bw'igihe co gukora, canke igihe ushaka kwimurira uburenganzira bw'amakuru y'ikirundo neza.


Gukora `Akazu` biragoye: `reka boxed_value = Agasanduku::new(42);` itanga umubare wose ku kirundo. `Box` ihita icungera ubu buhinga – iyo `Box` ivuye mu rwego, ihita igabanya ubu buhinga bw'ikirundo. Ukwo gusukura kwikora gukingira ubwonko gusohoka ataco bisaba gucungera ubwonko n’amaboko.


Kimwe mu bihambaye cane mu gukoresha `Box` ni ugushoboza imiterere y'amakuru asubiramwo. Rimbura urutonde rwuzuye aho urudodo rumwe rumwe rurimwo agaciro n'ikimenyetso c'urudodo rukurikira. Ata `Box`, ntushobora gusobanura mwene iyo miterere kuko umukozi w'ivy'ubuhinga ntashobora kumenya ubunini bw'ubwoko burimwo. Mu gukoresha `Akazu<Node>` ku kimenyetso gikurikira, uca umenagura ingorane y'ubunini busubira inyuma kuko `Akazu` gafise ubunini buzwi, budahinduka ataco burimwo.


### Gushira mu ngiro akaranga ka Deref


Igishushanyo `Deref` kiremesha ubwoko gukurwaho hakoreshejwe umukoresha `*`, bituma ibimenyetso vy'ubwenge vyigenza nk'ibisobanuro ku makuru yavyo arimwo. Iyo ushize mu ngiro `Deref` ku kimenyetso c'ubwenge, ushoboza gukuraho ibimenyetso vy'ubwenge bituma ikimenyetso c'ubwenge gica ibibatsi kugira ngo gikoreshwe. Ibi bisigura ko ushobora guhamagara uburyo ku bwoko burimwo biciye ku nzira y'ubwenge ata gukuraho.


Igishushanyo `Deref` gisobanura ubwoko bujanye n'ivyo `Target` bugaragaza ubwoko bw'ibimenyetso igikorwa co gukuraho ibimenyetso gikwiye gutanga. Ico kintu gisaba gushirwa mu ngiro uburyo bwa `deref` bugarura ivyerekanwa ku bwoko bw'intumbero. Ku `Akazu<T>`, ugushirwa mu ngiro kugarura ivyerekanwa ku gaciro ka `T` karimwo.


Rust ikora igikorwa co guhatira deref, bisobanura ko umukozi ashobora kwinjiza amahamagara kuri `deref` iyo bikenewe kugira ngo ubwoko buhure. Ni co gituma ushobora gutanga `String` ku gikorwa citeze `&str` – umukozi ahita akuraho `String` kugira ngo aronke igice c'urudodo. Ivyo bishobora gufatanya ingero nyinshi, rero `Box<String>` ishobora guhindurwa ubwayo ikaba `&str` biciye mu bikorwa vyinshi vya deref.


### Ishirwa mu ngiro ry'Itonyanga


Igishushanyo `Drop` kigufasha gusobanura kode y'isuku ikoreshwa iyo agaciro kavuye mu rwego. Ivyo birahambaye cane cane ku bimenyetso vy'ubwenge bicungera ibikoresho birenze ubwonko bworoshe, nk'ibikoresho vy'amadosiye, amahuza y'urubuga, canke ibara ry'ibimenyetso. Igishushanyo ca `Drop` gifise uburyo bumwe, `drop`, bufata ivyerekanwa bihinduka kuri `self` maze bugakora isuku.


Ubwoko bwinshi ntibukeneye gushirwa mu ngiro kwa `Drop` kubera ko Rust ikora ubwayo gutera imirima yabo. Ariko rero, ibimenyetso vy’ubwenge akenshi birakenera ubuhinga busanzwe kugira ngo bisukure neza ibikoresho bicungera. Nk'akarorero, ikimenyetso c'ubwenge giharurwa n'ibiharuro gikeneye kugabanya igiharuro c'ibiharuro no gukuraho amakuru asangiye igihe ibiharuro vya nyuma bikurwako.


Ushobora kandi gutera agaciro imbere y'uko kava mu rwego ukoresheje `std::mem::drop()`. Iyi nshingano ifata uburenganzira bw'agaciro maze ikayitera, bishobora kuba ngirakamaro mu kurekura ibikoresho kare canke kumenya neza ko isuku riba ahantu kanaka muri porogarama yawe. Igikorwa kigaragara co gutera ni igikorwa c’akaranga gusa gifata uburenganzira – igikorwa nyaco kiba iyo agaciro kaguye ku mpera y’igikorwa.


Uyu mushinge w’ibifunga, ibisubiramwo, n’ibimenyetso vy’ubwenge biha abahinguzi ba Rust ibikoresho vyo kwandika kode igaragaza, itekanye kandi ikora neza. Ivyo bikoresho birakorana kugira ngo bishobore gukora porogarama zisanzwe mu gihe bigumya ivyemezo nyamukuru vya Rust vyerekeye umutekano w’ukwibuka n’ubushobozi.



## Ibara ry'ibisobanuro n'uguhinduka kw'imbere

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Ibara ry'Ibisobanuro na RC


Ibara ry’ibimenyetso rigereranya ubundi bwoko bw’ishimikiro bw’ikimenyetso c’ubwenge muri Rust, cagenewe canecane gutuma habaho ibintu vyinshi vy’ubutunzi. Udakunze Box, ikurikiza amategeko ya kera y’uburenganzira bw’umuntu umwe aho ikigo kimwe ari co gifise amakuru, RC (Reference Counter) iremeza ibice vyinshi vya kode yawe gusangira uburenganzira bw’amakuru amwe icarimwe. Uwo murongo w’ubutunzi busangiye ukora biciye mu buryo bwo kubara bukurikirana ingene amakuru ariho ku bijanye n’amakuru kanaka.


Uburyo bwo guharura bukora mu kubungabunga igiharuro co mu mutima kigenda kirongerekana igihe cose ukora clone ya RC kigaca kigabanuka iyo RC ivuye. Ukwibuka kurabohorwa gusa iyo iki giharuro gishitse kuri zero, bikaba bituma amakuru aguma ari meza igihe cose hariho ivyerekeye. Ubu buryo burabuza gutanga amakuru mbere y’igihe mu gihe bushoboza uburyo bwo gusangira amakuru bushobora guhinduka butashoboka iyo umuntu afise Box yoroshe.


Akarorero ngirakamaro aho RC ari ngirakamaro ni uguhingura imiterere y'amakuru asangiye nk'urutonde rwuzuye aho urutonde rwinshi rushobora kwerekeza ku gice kimwe c'umurizo. Rimbura kugerageza gukora urutonde rubiri rutandukanye rwompi ruvuga urutonde rumwe. Iyo Box ifise ububasha, ivyo ntibishoboka kubera ko kwimurira igice gisangiwe ku rutonde rwa mbere bihindura ububasha, bikabuza gukoreshwa mu rutonde rwa kabiri. RC itorera umuti ivyo mu kuguha uburenganzira bwo gukora clone y’ishingiro aho gukora clone y’amakuru ari munsi yayo, bituma imiterere yasangiye ishoboka mu gihe uguma ufise umutekano w’ubwenge.


Iyo ukoze clone ya RC, ntuba uriko urasubiramwo amakuru yo mu mutima utitaye ku bunini bwayo canke ukuntu igoye. Ahubwo, uriko urema ikindi kigereranyo ku kibanza kimwe c'ukwibuka kandi ukongerako igiharuro c'ikimenyetso. Ivyo bituma gukora cloning instances za RC bikora neza mbere no ku mibumbe myinshi y’amakuru, kuko ni vyo vyonyene bikopororwa mu gihe amakuru ashingiyeko aguma mu kibanza cayo.


### Guhinduka kw'imbere na RefCell


RefCell izana uguhinduka kw’imbere, bigufasha guhindura amakuru mbere n’igihe ufise gusa ivyerekanwa bitahinduka. Ubu bushobozi burahindura cane ingene amategeko y’inguzanyo ya Rust ashirwa mu ngiro mu gukura amasheki mu gihe co gukoranya gushika mu gihe co gukora. Naho ibisobanuro bisanzwe vyishingikiriza ku mukozi kugira ngo asuzume umutekano wo kugurana, RefCell ikora ivyo bipimo mu gihe c’ugushirwa mu ngiro kwa porogarama, itanga uguhinduranya kwinshi ku giciro c’ubwoba bushobora kubaho mu gihe co gukora.


Ingingo nyamukuru iri inyuma ya RefCell ni ugukomeza amategeko y’inguzanyo amwe amwe Rust isanzwe ishira mu ngiro mu gihe co gukoranya, ariko ukayasuzuma mu buryo bukomeye. Igihe cose, ushobora kugira igisobanuro kimwe gihinduka canke umubare uwo ari wo wose w'ibisobanuro bidahinduka ku makuru ari muri RefCell. Iyo kode yawe igerageje kurenga kuri ayo mategeko mu kurema inguzanyo zihushanye icarimwe, porogarama izotera ubwoba aho gutuma haba inyifato idasobanutse.


Ivyo bigenzura igihe co gukora bishobora gutuma habaho uburyo bumwe bumwe bwo gukora porogarama umukozi yoshobora kwanka mbere n'igihe mu vy'ukuri ataco akora. Isesengura ridahinduka ry’umuhinguzi w’ibitabu ntirishobora kwama ryemeza ko uburyo butoroshe bwo kugurana ari ukuri, ivyo bikaba bituma rikora amakosa ku ruhande rwo kwiyubara. RefCell iraguha uburenganzira bwo gukuraho izo nzitizi z'ubuzima iyo wizigiye ko kode yawe igororotse, ariko ukwo kwizigira kuzanana n'inshingano yo kumenya neza ko ikoreshwa neza kugira ngo wirinde gusenyuka kw'igihe co gukora.


Ikoreshwa rusangi rya RefCell ririmwo ibintu vy'ugutwenga mu bihe vy'igerageza. Igihe ushize mu ngiro akaranga gatanga gusa uburenganzira bwo kwironsa, ariko ugushirwa mu ngiro kwawe kw'ibinyoma gukeneye gukurikirana amahinduka y'igihugu imbere, RefCell irashoboza iyo nzira. Ushobora gupfuka igihugu c'imbere muri RefCell, ugatuma iyo mock ihindura amakuru yayo yo gukurikirana mbere biciye ku nzira idahinduka.


### Gufatanya RC na RefCell ku gihugu gishobora guhinduka


Ihuriro rya RC na RefCell rituma habaho uburyo bwo guhindura ibintu, aho benevyo benshi bashobora guhindura amakuru amwe. RC itanga ubushobozi bwo gusangira, mu gihe RefCell ishoboza ihinduka biciye mu bimenyetso bidahinduka. Iryo huriro ni ngirakamaro mu bihe nk'imiterere y'ibishushanyo, ububiko, canke ikintu cose aho ibice vyinshi vya porogarama yawe bikeneye gusoma no kwandika amakuru asangiye.


Iyo uzingirije RefCell imbere muri RC, urema umubumbe ushobora guhindurwa no gukwiragizwa muri porogarama yawe yose, igishushanyo cose kikaba gitanga uburenganzira bwo gushika ku makuru amwe amwe ashobora guhinduka. Abafise amakuru bose barashobora guhindura amakuru bakoresheje uburyo bwa RefCell borrow_mut, ariko bategerezwa kwubahiriza amategeko y'inguzanyo mu gihe co gukora. Iyi nzira ishobora gutuma haba ibintu bikomeye vyo gusangira amakuru mu gihe igumya ivyemezo vy’umutekano vya Rust biciye mu gusuzuma igihe co gukora.


Ariko rero, ukwo guhinduranya biza n’imburi zihambaye ku bijanye n’ugusohoka kw’ubwenge be n’ingendo z’ibimenyetso. Iyo ukoresheje RC na RefCell, birashoboka guhingura mu mpanuka ibimenyetso vy'uruziga aho imiterere y'amakuru yishingira, haba mu buryo butaziguye canke biciye mu ruhererekane rw'ibimenyetso. Izo nzira zibuza igiharuro c'ibimenyetso kidashobora gushika kuri zero, bikaba bituma ubwonko buva mu bwenge kubera ko amakuru asa n'ayama afise ibimenyetso bikora mbere n'igihe atagishobora gushikirwa n'ibindi bice vya porogarama.


Umuti w'ingendo z'ibimenyetso ni ugukoresha ibimenyetso bigoyagoya, bitagira ico bikoze ku giharuro c'ibimenyetso bikoreshwa mu gufata ingingo zo gucunga ubwonko. Ivyiyumviro bigoyagoya bigufasha kuguma ufise amasano hagati y’imiterere y’amakuru ataco uyigumyeho, ugaca inzinguzingu zishobora kubaho mu gihe uzigama ubushobozi bwo kuronka amakuru afitaniye isano igihe akiriho.


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


### Umutekano w'urudodo n'ivy'ishimikiro


Uburyo bwa Rust bwo gukorana n’ibindi bibanza ku gukingira amarushanwa y’amakuru n’ibibazo vy’umutekano w’ubwenge mu gihe co gukoranya. Uburyo bw'ubwoko bushitsa umutekano w'indodo biciye mu bimenyetso nka `Kohereza` na `Guhuza`, bigaragaza ubwoko nk'umutekano wo kwimurira hagati y'indodo canke umutekano wo gushika ku gihe kimwe. Iryo genzura ry'igihe co gukoranya rifata ibibazo vyinshi vy'igihe kimwe vyoboneka gusa mu gihe co gukora mu zindi ndimi zo gukora porogarama.


Gukora indodo muri Rust bikurikira uburyo bugororotse hakoreshejwe indodo::spawn, ifata ugufunga kugira ngo ikore mu indodo nshasha maze igasubiza igikoresho co gucunga ubuzima bw'indodo. Urudodo rwavutse rugendana n'urudodo nyamukuru, kandi ushobora gukoresha uburyo bwo gufatanya ku gikoresho kugira ngo urindire ko ruheza. Hatariho gufatanya gutomoye, indodo zavyawe zishobora guhera iyo indodo nyamukuru isohotse, bishobora gutuma igikorwa kitarangiye gihagarara.


Ijambo ry'ingenzi ry'ukwimuka riba rihambaye cane iyo ukora n'indodo kubera ko ugufunga kwaciye ku ndodo zavyawe kenshi gukenera kugira amakuru yabo aho kuyagura. Kubera ko indodo zavyawe zishobora kubaho kuruta urugero rwaziremye, kugurana urugero rw’umuvyeyi bituma habaho ukurenga ku mategeko mu buzima bwose. Kwimurira amakuru mu gufunga urudodo bihindura ubutunzi, bikaba bituma amakuru aguma ari meza mu buzima bwose bw'urudodo mu gihe bibuza gushika ku rudodo kuva ku rwego rw'intango.


Ubutumwa buratanga ubundi buryo bwo gusangira igihugu biciye mu nzira zituma indodo zivugana mu kohereza amakuru aho gusangira ubwonko. Ico kibanza c’ibitabu ca Rust gitanga imirongo y’ibitabu vy’abaguzi benshi (MPSC), aho indodo nyinshi zishobora kohereza ubutumwa ku ndodo imwe yakira. Iyi nzira irakuraho ibibazo vyinshi vyo guhuza mu kwirinda gusangira igihugu gihinduka, aho kwizigira uguhana ubutumwa kugira ngo habeho uguhuza.


### Gusangiye Leta n'Igihugu na Mutex na Arc


Iyo ubutumwa buca butabereye, Rust itanga uburyo busanzwe bwo gusangira Leta biciye mu Mutex (ugutandukanya) ifatanijwe na Arc (Ibara ry’Ivyerekeye Atomic). Mutex ikora vyose kugira ngo urudodo rumwe gusa rushobore gushika ku makuru akinzwe ku gihe kimwe mu gusaba indodo kuronka urufunguzo imbere yo gushika ku makuru. Igifunguzo kirarekurwa ubwaco iyo ikintu co kurinda kigaruwe n’igikorwa c’igifunguzo kivuye mu rwego, kikabuza ibintu bisanzwe vy’ugufunga bitewe n’ugufungura kwibagiwe.


Arc ikora nk'indodo-umutekano ingana na RC, ikoresheje ibikorwa vy'atome kugira ngo icungere igiharuro c'ishingiro ata nkomanzi ku ndodo nyinshi. Naho RC ikora neza cane ku bikorwa vy’urudodo rumwe, uguharura kwayo kw’intangamarara kutagira atome kurema imibereho y’amarushanwa iyo umuntu ashitseko avuye ku rudodo rwinshi. Arc's atomic counters zituma uguhindura igiharuro c'ibimenyetso bishika ata nkomanzi mbere no mu gihe c'ugushika ku gihe kimwe, bikaba bituma bibereye gusangira amakuru ku mipaka y'urudodo.


Ihuriro rya Arc na Mutex rirema urugero rw'imimerere ihinduka rusangi muri porogarama zikorana. Mu kuzingira Mutex mu Arc, ushobora gukora clone ya Arc kugira ngo ushiremwo uburenganzira bwo gushika kuri mutex imwe ku ndodo nyinshi, indodo yose ishobora kuronka urufunguzo no guhindura amakuru akinzwe ata nkomanzi. Iyi nzira itanga ubushobozi bwo guhinduranya igihugu mu gihe igumya ivyemezo vy’umutekano vya Rust biciye mu kugenzura igihe co gukoranya no gufunga igihe co gukora.


Ibiranga Send na Sync bikora inyuma y'ivyo bimenyetso kugira ngo bimenyekane ko urudodo rutekanye mu gihe co gukoranya. Send yerekana ko ubwoko bushobora kwimurirwa mu yindi ndodo ata nkomanzi, mu gihe Sync yerekana ko ibisobanuro vy'ubwoko bishobora gusangizwa ata nkomanzi hagati y'indodo. Ubwoko bwinshi burashira mu ngiro izo kamere iyo ibice vyavyo bifise umutekano, ariko ubwoko bumwe bumwe nka RC na RefCell ntibubishira mu ngiro kubera ko butagenewe gukoreshwa rimwe. Ivyo bishirwa mu ngiro vy’akaranga vyikora bibuza kwinjira mu mpanuka ivy’uguhungabanya umutekano w’urudodo mu gihe vyemerera ubwoko butekanye gukora ata nkomanzi mu bihe bimwe.


## Gutahura ama Macro ya Rust

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Intangamarara y'Ibikoresho Bikomeye muri Rust


Macros muri Rust ni ikintu gifasha abahinguzi kwandika kode itanga izindi kode mu gihe co gukora. Udakunze ibikorwa, bihamagarwa mu gihe co gukora, macros ziragwizwa kare mu nzira yo gukoranya, imbere yo gusuzuma ubwoko n'intambwe za nyuma. Iryo tandukaniro ry'ishimikiro rituma macros zigira akamaro cane cane mu kugabanya ugusubiramwo kode no kurema indimi zitandukanye muri porogarama za Rust.


Ikimenyetso kimenyekana cane c’uguhamagara kwa macro ni ikimenyetso c’ugutangara (!) gikurikira izina rya macro. Nk'akarorero, iyo ukoresheje `println!("Yambu, isi!")`, nturiko urahamagara igikorwa ariko uriko urahamagara macro. Iyi macro iragwira mu kode igoye cane ikora ibikorwa vyo guhindura n'ugusohora. Ikimenyetso c'ugutangara gikora nk'ikimenyetso c'amaso ku bategura ko uguhingura kode y'igihe co gukoranya biriko biraba aho guhamagara igikorwa gisanzwe.


Rust itanga ubwoko butatu butandukanye bw’ama macros, imwe yose ifise intumbero zitandukanye mu bidukikije vy’ururimi:



- Macros nk'ibikorwa**: Bisa n'amahamagara y'ibikorwa ariko bikora mu gihe co gukoranya (nk'akarorero, `vec!`, `println!`)
- Gukuraho macros**: Gushira mu ngiro ubwavyo ibiranga ubwoko (nk'akarorero, `#[gukuraho(Gukosora, Gukora)]`)
- Macros zisa n'ibiranga**: Guhindura inyifato y'ibintu vya kode bikoreshwako (nk'akarorero, `#[ikigeragezo]`, `#[tokio::ingenzi]`)


Gutahura ubwo bwoko butandukanye bwa macro ni ngombwa kugira ngo porogarama ya Rust ikore neza, kuko imwe yose ivuga ku bijanye n’ikoreshwa ry’ibintu n’ingene porogarama ikoreshwa.


### Ubwoko bwa Macros n'ingene zikoreshwa


Macro zimeze nk'ibikorwa zigereranya ubwoko bwa macro busanzwe buboneka muri porogarama ya Rust. Izo macros zikoresha insiguro isa n'iy'uguhamagara ibikorwa ariko zikora ivy'uguhuza ku vyo zishiramwo kuri generate kode ibereye. `vec!` macro ni akarorero rusangi k'iki kiciro, ishobora gutuma abahinguzi bashobora kurema no gutanguza amavecteur afise insiguro y'amajambo. Iyo wanditse `vec![1, 2, 3, 4]`, macro iragwiza ivyo mu kode irema vecteur nshasha, isunika ikintu cose ku giti cayo, igasubiza vecteur yuzuye.


Derive macros itanga uburyo bwo gushirwa mu ngiro bwite ku bwoko busanzwe, igabanura cane kode y'ibara ry'umuriro. Iyo wongeyeko `#[derive(Debug)]` ku nsobanuro ya struct canke enum, uba uriko urategeka umukozi wo gukora generate gushirwa mu ngiro kwuzuye kw'akaranga ka Debug k'ubwo bwoko. Iyi nzira y'ugushirwa mu ngiro ikorana n'imiterere ikenewe kugira ngo yerekane ibirimwo ubwoko mu buryo bushobora gusomwa n'umuntu. Uburyo bwo gukuraho burashigikira ibiranga vyinshi vy’ibitabo, harimwo Clone, PartialEq, bikaba bituma ari igikoresho gikoreshwa cane mu kugabanya ivyuma vy’amazi.


Macros zisa n'ibiranga zihindura inyifato y'ibintu vya kode zisobanura, zitanga uburyo bwo kwongerako amakuru canke guhindura inyifato y'ugukoranya. Izo macros zigaragara nk'ibiranga bishizwe hejuru y'insobanuro z'ubwoko, ibikorwa, canke ibindi vyubatswe na kode. Nk'akarorero, `#[non_exhaustive]` akaranga kuri enum yerekana ko izindi mpinduka zishobora kwongerwa mu verisiyo zizoza, bisaba invugo zihuye kugira ngo zishiremwo ikibazo mburabuzi. Ubu buryo buratuma habaho uguhuza imbere mu gihe butanga inyandiko zitomoye z’ubushobozi bw’ubwo bwoko bwo gutera imbere.


### Gukora Macros zimeze nk'ibikorwa vy'umuntu ku giti ciwe


Kwandika ama macros ameze nk'ibikorwa vy'umugenzo birimwo gutahura insiguro y'amajambo y'urugero rwa Rust ku nsobanuro za macros. Insobanuro ya macro ikoresha uburyo bwo gutangaza aho ugaragaza uburyo buhuye n'imirongo itandukanye y'injiza n'ibigereranyo vy'uguhingura kode bihuye. Buri macro ishobora kubamwo amashami menshi, bikayifasha gukorana n’imirongo itandukanye y’injiza n’itegeko ry’i generate ribereye ku kibazo cose.


Niwiyumvire kurema macro y’ubuhinga busanzwe yerekana ingingo ngenderwako z’ishimikiro z’ubwubatsi bwa macro. Insobanuro ya macro itangura na `macro_rules!` ikurikiwe n'izina rya macro n'urutonde rw'amashami ahuye n'imiterere. Ishami ryose rigizwe n’urugero rujanye n’inyuguti yihariye y’injiza be n’urugero rwa kode rutanga kode ya Rust ihuye. Nk'akarorero, ishami ryoroshe ryoshobora guhura n'ibimenyetso vy'ubusa `[]` na kode ya generate kugira ngo ureme umurongo w'ubusa, mu gihe irindi shami rihuye n'invugo imwe maze rikazana kode kugira ngo ureme umurongo ufise ikintu kimwe.


Macros zica zigira akamaro cane cane iyo ushize mu ngiro uburyo bw'imvo zihinduka ukoresheje insiguro y'isubiramwo. Igishushanyo `$($x:expr),*` gihuye n'imvugo zero canke nyinshi zitandukanijwe n'ibimenyetso, bituma macro ishobora gukora umubare w'imvo n'imvano. Igishushanyo c'uguhingura kode gihuye gikoresha `$(vec.push($x);)*` kugira ngo gisubiremwo ku mvugo zose zihuye n'imvugo z'umuntu ku giti ciwe za generate kuri buri imwe. Ubwo buryo bwo gusubiramwo buratuma ama macros ashobora kwandika kode ya generate yoba idashoboka canke ikaba ari amajambo menshi cane kwandika n’amaboko.


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


Ivyo gukoranya bihindura amahamagara macro mu kode yagutse imbere y'uko ubwoko bugenzurwa n'ugutunganirizwa bishika. Iyo umukozi ahura n'ihamagarwa rya macro, ihuza input n'ibigereranyo vyasobanuwe maze igasubirira ihamagarwa rya macro na kode yavutse. Iyi kode yagutse ica mu nzira zisanzwe zo gukoranya, harimwo no kugenzura ubwoko no kuyitunganya neza. Ibikoresho nka `cargo expand` bituma abahinguzi basuzuma kode yashizweho, bitanga ubushobozi bwo gukosora igihe bakora macros zikomeye.


### Ivyiyumviro vya Macro biteye imbere no gukosora


Iterambere rya Macro risaba gutahura itandukaniro hagati y’igihe co gukora n’igihe co gukora. Macros zikora mu gihe co gukoranya, zitanga kode izokora mu gihe co gukora. Ukwo gutandukanya kw’igihe bisigura ko ubuhinga bwa macro butashobora kuva ku gaciro k’igihe co gukora, ariko kandi burashoboza gutuma habaho uguhindura neza aho imibare igoye ishobora gukorwa rimwe mu gihe co gukoranya aho gusubiramwo mu gihe co gukora.


Uburyo bwo guhuza ivyitegererezo mu macros burashigikira ibice bitandukanye bisobanura ubwoko bw'ibintu vya kode bishobora guhuzwa. Igisobanuro ca `expr` gihuye n'imvugo, `ty` gihuye n'ubwoko, `ident` gihuye n'ibimenyetso, n'ibindi vyinshi bitanga ubugenzuzi bwiza ku kwemeza ivyinjijwe. Ivyo bimenyetso bituma ama macros aronka inyungu ibereye mu buryo bw'inyuguti kandi agatanga ubutumwa bw'ikosa butomoye iyo inyuguti idakwiriye ihuye.


Gukosora ama macros bizana ingorane zidasanzwe kubera kamere yavyo y’igihe co gukoranya. Itegeko rya `cargo expand` ni ngirakamaro mu guteza imbere macro, kuko ryerekana kode yagutse yuzuye iterwa n'amahamagara ya macro. Ico gikoresho kiratuma abahinguzi bashobora kugenzura ko ama macros yabo generate ari kode yitezwe no kumenya ibibazo biri mu nzira yo kwagura. Iyo kode yakozwe na macro irimwo amakosa, igisohoka cagutse gifasha kumenya neza nimba ingorane iri mu nsobanuro ya macro canke mu miterere ya kode yakozwe.


Macros zikomeye zishobora gushirwa mu ngiro uburyo busubiramwo, aho macro yihamagara n'imvo zahinduwe kugira ngo ikoreshe kode y'ivyaduka canke isubiramwo. Ariko rero, ama macros asubiramwo asaba guhingura neza kugira ngo umuntu yirinde ibibazo vy’ukwaguka n’ugukoranya bitagira iherezo. Igihe co gukoranya ama macro bisigura ko mbere n’ugushirwa mu ngiro kwa macro kudakora neza bigira ico bikoze gusa ku muvuduko wo gukoranya, ntibigira ico bikoze ku gihe co gukora, ariko macros zikomeye cane zishobora gutuma igikorwa co kwubaka kigenda buhoro cane.



# Rust na Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Kubera iki Rust ku bijanye n'iterambere rya Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


Guhitamwo Rust ku Bitcoin n’iterambere rya Lightning si ivy’impfagusa. Iterambere rya Bitcoin rifise amabanga yihariye ayitandukanya n’iterambere rya porogarama zisanzwe. Igihe bakorana na Bitcoin, abahinguzi kenshi baba bariko barafata amahera y’abakoresha mu bidukikije aho amakosa ashobora kuba adashobora gusubirwamwo. Mu buryo butandukanye n’uburyo bw’ivy’ubutunzi bwa kera bufise uburinzi bushingiye ku mategeko n’uburyo bwo gusubiza amahera, uburyo Bitcoin ikoreshwa mu buryo butandukanye bisigura ko iyo amafaranga amaze gutangazwa, ata bubasha bwo gusaba ko amafaranga asubizwa. Ivyo bintu vy’ukuri bisaba urugero rwo hejuru rw’inshingano n’ugukora neza mu gutegura porogarama.


Filozofiya yo "kwihuta no gusenyura ibintu" ikora mu nzego nyinshi z'ubuhinga ntabwo ikora ku gutegura Bitcoin. Ahubwo, ibidukikije bisaba indimi n’ibikoresho bifasha abahinguzi guhingura porogarama zikomeye kandi zitekanye aho ukunanirwa gukingirwa canke gufatwa neza. Ni co gituma imigambi myinshi izwi cane ya Bitcoin yakwegereye Rust, harimwo n’Igikoresho co Gutegura Bitcoin (BDK), Igikoresho co Gutegura Imiravyo (LDK), na BreezSDK.


Rust itanga ibintu bitatu vy’ingenzi biyigira neza cane mu gutegura Bitcoin: uburyo bukomeye butahinduka, ibikoresho vyiza vy’ubuhinga bwa none, n’uguhuza n’ibindi bikoresho. Ico kimwe cose muri ivyo biranga kigira ico gikoze ku bushobozi bw’ururimi bwo gufasha abahinguzi kwandika kode zitekanye kandi zishobora kwizigirwa zo gukoresha ibikorwa vy’amahera y’ibanga.


### Ubwoko bukomeye bwa Rust


Uburyo bwo kwandika bwa Rust buratanga ibiranga kwandika bihoraho n’ibikomeye bikorana kugira ngo bifate amakosa imbere y’uko ashobora kugira ico akoze ku bakoresha. Ivyo bisigura ko ugusuzuma ubwoko bishika mu gihe co gukoranya, bisaba abahinguzi gutorera umuti ukudahuza kw'ubwoko imbere y'uko porogarama ishobora kubakwa. Ivyo bitandukanye n'indimi zanditswe mu buryo bukomeye aho amakosa yo kwandika agaragara gusa mu gihe c'ugukora, bishobora kuba inyuma y'aho porogarama ikoreshejwe kandi iriko irakoresha amahera nyayo y'abakoresha.


Inkomezi z’uburyo bw’ubwoko bwa Rust zijanye n’ukuntu zigaragaza n’ukuntu zikomeye mu bibazo vyo gushushanya. Udakunze indimi zifise uburyo bw'ubwoko bugoyagoya nka C, aho abahinguzi bagarukira ku bwoko bw'ishimikiro nk'imibare n'imiterere, Rust iremeza ubwoko bw'ubutunzi bushobora guserukira neza ivyiyumviro vy'intara bikomeye. Nk'akarorero, ushobora kurema ubwoko butandukanya ubwoko butandukanye bw'urutonde canke ugashitsa ko ibikorwa bimwebimwe bikorwa gusa ku bwoko bw'ibintu vyihariye.


Igituma uburyo bw’ubwoko bwa Rust bugira akamaro mu gutegura Bitcoin ni uburyo bukoresha mu gukingira ubwonko. Ubwo bwoko bumwe bw'uburyo bugereranya ubuhinga bwo gukora ubucuruzi na bwo burakorana n'ubuninahazwa bw'ubwenge n'ubugenzuzi bw'ugushikira. Iryo banga ribiri risobanura ko imigwi isanzwe y’ubugoyagoye, nk’ugusohoka kw’ubwenge, amakosa atagira kabiri, n’imibereho y’amarushanwa, bikurwaho burundu n’umuhinguzi. Ubuhinga bw’ubwoko burashira mu ngiro ivyo vyemezo vy’umutekano biciye mu vyiyumviro nk’ubutunzi, ugutiza, n’uguharura ibimenyetso, bikaba bigoye cane gushiramwo ibikoko bijanye n’ukwibuka bishobora gutuma umutekano canke ugushikama bihungabana.


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


### Ibikoresho vya none n'ugushigikira imbuga zitandukanye


Rust's tooling ecosystem itanga abahinguzi ibikoresho bifasha mu gutanga umusaruro no mu buryo bw'amakode. Igikoresho ca Rust ubwaco nticagenewe guhindura kode mu buryo bwa binaire gusa, ariko ni igikoresho co kwigisha gifasha abahinguzi kwiga no gutera imbere. Iyo habaye amakosa yo gukoranya, uwukoranya aratanga insobanuro zitomoye z’ivyo vyacitse nabi kandi akenshi agatanga ivyiyumviro vyihariye vyo gukosora. Ubwo buryo burafise akamaro cane cane ku bategura bashasha muri Rust, kuko uwo muhinguzi yigisha neza ingendo nziza kandi afasha mu gukingira amakosa asanzwe.


Ururimi rurimwo Cargo, umuyobozi w’amapaki yunze ubumwe akora uburongozi bw’ibiva ku bindi, inyubako, igerageza, n’uguhingura inyandiko. Ukwo guhuza gukuraho uguca ibice kuboneka mu ndimi za kera nka C++, aho ibikoresho vyinshi bihiganwa bitera ukudahuza mu migambi. Cargo kandi irashigikira ivyungura nka rustfmt ku bijanye no guhindura kode na Clippy ku bijanye n’ugusesangura, kugira ngo kode ikurikize amabwirizwa y’imiterere idahinduka kandi igafata ibibazo bishobora kubaho imbere y’uko bihinduka ingorane.


Ubushobozi bwa Rust bwo gukoresha ubuhinga butandukanye burarengeye ubuhinga bwa kera bwo gukoresha kugira ngo bushiremwo ubuhinga bwo gukoresha telefone ngendanwa nka Android na iOS, hamwe n’ubuhinga bwa WebAssembly bwo gukoresha ubuhinga bushingiye ku mucukumbuzi. Iyi nfashanyo y'ibikoresho vyinshi ni ngirakamaro ku bikorwa vya Bitcoin bikeneye gukoreshwa mu bidukikije bitandukanye. Nk’akarorero, imigambi nka Mutiny Wallet ikoresha ubuhinga bwa Rust bwo gukora amasakoshi ya Lightning akora ataco akora mu bikoresho vy’urubuga, ikintu coba kidashoboka n’ubuhinga bwa kera bwo ku rubuga gusa.


### Gutahura ubwoko bw'amakosa n'ingaruka zayo


Gutorera umuti neza amakosa bitangura no gutahura ivyiciro bitandukanye vy’amakosa ashobora gushika mu gihe porogarama iriko irashirwa mu ngiro. Rimbura ubuhinga bworoshe bwo guca inzira buharura inzira ziri hagati y’ibice vy’ubutaka. Aka karorero karerekana ubwoko butatu bw’amakosa abahinguzi bategerezwa gutorera umuti: amakosa y’injiza atagira akamaro, amakosa y’ibikoresho vy’igihe co gukora, n’amakosa y’ubwenge.


Amakosa y'injiza atagira akamaro abaho iyo igikorwa cakiriye amaparametere adahuye n'ibisabwa. Nk'akarorero, iyo urutonde rw'ibiharuro vy'ubutaka rukoresha imibare yose ifise umukono ku burebure bw'uburebure ariko rukaronka agaciro kabi aho agaciro keza gusa ari ko gafise akamaro, igikorwa ntigishobora gukomeza mu buryo bufise insiguro. Aya makosa agereranya ukurenga ku masezerano hagati y'uwuhamagara n'igikorwa, kandi inyishu ibereye ni ukwanka ivyo winjije no kugarura ikimenyetso c'ikosa.


Amakosa y'ibikoresho vy'igihe co gukora aba iyo ivy'inyuma bitaboneka canke bidashobora gushikwako. Gusoma dosiye y’ikarata vyoshobora kunanirwa kubera ko iyo dosiye itahari, porogarama idafise uruhusha rukwiye, canke igikoresho co kubika ibintu kitaboneka. Aya makosa ari hanze y’ubuhinga bwa porogarama kandi akenshi asaba gukosora ibidukikije aho guhindura kode. Ariko rero, ibikorwa bikomeye bitegerezwa kwitega no gufata neza ivyo bintu.


Amakosa y’ubwenge agereranya ibibazo mu gushirwa mu ngiro kwa porogarama canke ukutumvikana ku bijanye n’ingene ibice bikorana. Iyo algorithme y'inzira igarukanye inzira y'ubusa iyo ihawe intango n'iherezo bifise akamaro, ivyo vyerekana akaga gakeneye gukosorwa muri kode ubwayo. Udakunze ubundi bwoko bw'amakosa, amakosa y'ubwenge akenshi asaba gukosora no guhindura kode kugira ngo atorerwe umuti.


### Ingamba zo gucungera amakosa akomeye


Kugira ngo umuntu yubake porogarama yizigirwa bisaba ingamba zigabanya amahirwe yo gukora amakosa kandi zigafata neza amakosa adashobora kwirindwa. Ingamba ya mbere ni uguhagarika amakosa ashobora kubaho biciye mu guhingura ubwoko bwitondewe. Mu guhitamwo ubwoko bushobora gusa guserukira agaciro kabereye, abahinguzi barashobora gukuraho amashure yose y'amakosa y'injiza atagira akamaro. Nk'akarorero, gukoresha imibare yose idafise ikimenyetso ku gaciro kadashobora kuba kabi bibuza amakosa y'agaciro kabi mu gihe co gukoranya.


Ivyemezo bitanga uwundi murongo wo gukingira mu kugenzura neza ko ivyo vyitezwe ari ukuri mu gihe porogarama iriko irashirwa mu ngiro. Ivyo bipimo bifise intumbero nyinshi: bifata ibikoko mu gihe c’igerageza, bituma porogarama zidakora kare iyo ingorane zishitse (bituma gukosora ibibazo vyoroha), kandi bikora nk’inyandiko zishobora gukorwa zidondora ivyo umuhinguzi w’iporogarama yiyumvira. Iyo ikirego kidashoboka, vyerekana ko iciyumviro nyamukuru ku bijanye n’ingene porogarama imeze carenganye, mu bisanzwe bikaba vyerekana ikosa ry’ubwenge rikeneye gukorwako itohoza.


Ingingo ngenderwako y’ibintu bitari vyo bifasha gucungera ibigoranye mu kumenya neza ko amakosa afatwa ku rwego rukwiye rw’urutonde. Ivyerekeye ugushirwa mu ngiro kw’imbere, harimwo ubwoko bw’amakosa yihariye ava mu masomero yo hasi, ntibikwiye gukwiragira birenze imbibe z’imirongo. Ahubwo, igice cose gikwiye guhindura amakosa mu majambo afise insiguro kuri urwo rwego rw’ugutahura. Nk'akarorero, porogaramu ya wallet ikoresha ububiko bw'ibitabo bwa Bitcoin ikwiye guhindura amakosa yo gusesangura ibisobanuro vyo ku rugero ruto mu butumwa bwo ku rugero rwo hejuru nk'"imiterere ya wallet idakora" itanga amakuru ashobora gukoreshwa ku bakoresha canke kode yo guhamagara.


Ubu buryo bwo gutorera umuti amakosa, bufatanijwe n’uburyo bw’ubwoko bwa Rust n’ibikoresho, burafasha gufata ingorane zishobora kubaho hakiri kare mu nzira y’iterambere, imbere y’uko zishobora gutera ingorane abakoresha canke zigahungabanya umutekano w’ibikorwa vya Bitcoin.



## Ikosa ry'akarorero

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust itanga uburyo bushitse bwo gutorera umuti amakosa bujanye n’umutekano n’ubushobozi. Naho ivyiyumviro rusangi vy’akarorero k’amakosa bikoreshwa mu ndimi zose zo gukora porogarama, Rust itanga ibikoresho n’ibigereranyo vyihariye bituma gutorera umuti amakosa bigaragara kandi bishoboka. Gutahura ubwo buryo ni ikintu gihambaye cane mu kwandika ibikorwa bikomeye vya Rust bishobora guhangana n’ibintu bitari bitezwe mu gihe biguma bikora neza kandi bifise umutekano.


### Ubwoba n'ingene bukoreshwa


Uburyo bwo gutera ubwoba bwa Rust bugereranya uburyo butaziguye kuruta ubundi bwo gutorera umuti amakosa adashobora gusubirwamwo. Iyo uhamagara macro `panic!`, porogarama ica ihagarika gukora, igahagarika canke igahagarika bivanye n'ingene uyitunganije. Igikoresho c'ubwoba cemera ubutumwa bw'urudodo budondora ivyo vyacitse nabi, bugatanga ikibanza co gukosora. Ikindi, uburyo nka `unwrap()` na `expect()` ku bwoko bw'Igisubizo n'Ihitamwo bukora nk'inzira ngufi zo gutera ubwoba iyo ubwo bwoko burimwo agaciro k'amakosa canke Nta n'imwe. Uburyo bwa `expect()` buragufasha gutanga ubutumwa busanzwe, bugatuma bugira amakuru menshi kurusha `unwrap()` igihe ukora ibitari vyo.


Naho vyoroshe, ubwoba bukwiye gukoreshwa neza mu mategeko y’uguhingura. Hariho ibintu bitari bike aho ubwoba butemewe gusa ariko bukaba ari bwiza. Igihe wandika ingero canke ibigereranyo, ubwoba buratanga uburyo busukuye bwo kwibanda ku bikorwa nyamukuru ata gutera umuvurungano kode n’ugutorera umuti amakosa yose. Mu bidukikije vy’ibigeragezo, ubwoba ni bwo kenshi bwipfuzwa iyo ivyemezo bitashoboye, kuko vyerekana neza ko hari ikintu kitari citezwe cabaye. Umuryango wa Rust nawo uremera ibihe aho abahinguzi bafise ubumenyi bwinshi kurusha abahinguzi, nk’igihe bariko barasesangura aderesi za IP zifise amakode akomeye zizwi ko zifise akamaro.


Ariko rero, umutekano ugaragara w'ubwoba "bugenzuwe n'umuhinguzi" urashobora guhenda. Rimbura ivy'aho ukora hard-code kuri aderesi IP ugakoresha `expect()` kuko uzi ko ari ngirakamaro. Mu gihe, uko kode itera imbere, ako gaciro gakomeye gashobora guhindurwa kakaba ikintu kidahinduka, hanyuma ako gahinduka gashobora guhindurwa kakaba ikintu nka "localhost" kugira ngo umuntu ashobore gukoresha neza. Mu kanya nk'ako gukubita, ubwoba bwawe "butekanye" burahinduka ukunanirwa kw'igihe co gukora. Ivyo bigaragaza igituma muri rusangi ari vyiza kwirinda ubwoba mu bijanye n’uguhingura ibintu maze ahubwo ugasubiza ubwoko bw’amakosa bukwiye bushobora gufatwa neza.


Imwe mu nzira zidasanzwe ku itegeko rya "kwirinda ubwoba" ni ibikorwa vya mutex. Iyo uhamagara `lock()` kuri mutex, igarura Igisubizo kuko lock ishobora kunanirwa iyo uwundi murongo uteye ubwoba mu gihe ufashe mutex. Ivyo bituma haba ibintu bitera urujijo aho kode yawe yo mu karere ironka ikosa ry’ikintu cabaye mu gihe gitandukanye rwose. Kubera ko udashobora gutorera umuti neza ikosa ryavuye mu ubwoba bw’iyindi nzira, abahinguzi benshi babona ko vyemewe gufungura amafunguro ya mutex, cane cane iyo ugumye ufise codebase idafise ubwoba ahandi hantu.


### Gukorana n'Igisubizo n'Ubwoko bw'Amahitamwo


Ubwoko bw'Igisubizo ni bwo bukora umugongo w'uburyo bwo gutorera umuti amakosa bwa Rust. Nk'ibara rishobora gufata `Ok(agaciro)` canke `Err(ikosa)`, Igisubizo kiguhatira kwemera ko ibikorwa bishobora kunanirwa. Ubwoko bw'Ihitamwo bukora intumbero isa n'iyo ku bibazo aho agaciro gashobora kuba katahari, karimwo `Some(value)` canke `None`. Naho Option itatanga amakuru y'ido n'ido y'ikosa, ni nziza ku bihe aho ukubura agaciro bifise insiguro kandi vyitezwe.


Ivyo vyose Result na Option bitanga uburyo bwinshi bwo gukoresha butuma gutorera umuti amakosa bigenda neza. Uburyo bwa `unwrap_or()` bugarura agaciro karimwo iyo kariho, canke agaciro mburabuzi iyo hari ikosa canke Nta. Iyi nzira ni ngirakamaro cane iyo ufise igisubizo gikwiriye, nk'ugusesangura inyungu y'umukoresha n'imbere y'igihe iyo gusesangura bidashoboka. Uburyo bwa `unwrap_or_default()` bukora gutyo nyene ariko bukoresha agaciro k'ubwoko aho kugusaba gusobanura kamwe. Naho ubu buryo butashobora gutorera umuti amakosa mu buryo bwa kera, buratanga uburyo bwo gusenya ibikorwa mu buryo bw’ubuntu iyo ingorane zishitse.


Ikimenyetso c'ikibazo (`?`) ni insiguro ndende y'ugukwiragiza amakosa. Iyo ikoreshejwe ku Gisubizo canke Ihitamwo, ikuraho agaciro k'uguterimbere iyo kariho, canke igaca igarura ikosa kuva ku gikorwa kiriho iyo hari ingorane. Uyu mukoresha akuraho amakosa yo gusuzuma amajambo asanzwe mu ndimi nka Go, aho utegerezwa gusuzuma no kugarura amakosa ku ntambwe yose. Igikoresho c’ikimenyetso c’ikibazo mu vy’ukuri gitanga isukari y’inyuguti ku bijanye n’ugusubirayo vuba, kikagufasha kwandika kode isukuye, y’umurongo yibanda ku nzira y’umunezero mu gihe ukora ubwawe ku gukwiragira kw’amakosa.


### Ivyitegererezo vyo gutorera umuti amakosa


Uburyo bwa `map()` ku bwoko bw'Igisubizo n'Ihitamwo burashoboza gukoresha amakosa ashobora gutuma kode igaragara cane kandi ishobora gukorana. Iyo uhamagara `map()` ku Gisubizo, igikorwa gitanzwe gikoreshwa ku gaciro k'uguterimbere iyo kiriho, mu gihe amakosa ahita akwiragizwa ataco ahinduye. Iyi nzira ni ngirakamaro igihe ukora ibikorwa vy'uruzitiro, kuko ushobora kwibanda ku guhindura agaciro ata gusubiramwo amakosa. Uburyo bwa `map_err()` butanga imikorere ihinduka, ishobora kugufasha guhindura ubwoko bw'amakosa mu gihe usiga agaciro k'uguterimbere katahindutse.


Guhindura amakosa bica biba ikintu gihambaye cane igihe wubaka ibikorwa vy’imirongo aho ibice bitandukanye bikeneye ubwoko butandukanye bw’amakosa. Rimbura igikorwa gisesangura ivyo umukoresha yinjije kandi gikeneye guhindura amakosa yo gusesangura yo mu rwego rwo hasi mu makosa yihariye y'intara. Ukoresheje `map_err()`, ushobora guhindura mu buryo bworoshe ikosa rusangi "imiterere y'umubare udakora" mu ikosa "imyaka idakora" rifise insiguro mu rwego rw'ikoreshwa ryawe. Iryo hinduka rishika aho ikosa ribera, bituma kode ishobora gusomwa no kubungabungwa kuruta amabarabara ya kera yo kugerageza aho gufata amakosa bitandukanywa n’ibikorwa bishobora kunanirwa.


Ihuriro ry'umukoresha w'ikimenyetso c'ikibazo n'ikarita y'amakosa rituma habaho uburyo bwo gufata amakosa mu buryo butomoye. Ushobora gukora ibikorwa, guhindura amakosa nk'uko bikenewe, no kuyakwiragiza hejuru y'uruganda rw'amahamagara n'ivyuma bikeyi. Ubu buryo butuma ugufata amakosa biguma hafi y’ibikorwa bishobora kunanirwa mu gihe bigumya itandukaniro risukuye hagati y’inzira z’uguterimbere n’iz’amakosa.


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


### Amasomero yo hanze n'ibidukikije vyo gutorera umuti amakosa


Igikoresho c’ibidukikije ca Rust kirimwo amasomero menshi azwi cane yongera ubushobozi bw’amasomero asanzwe bwo gutorera umuti amakosa. Ico kibanza c'ibitabo `anyhow` gitanga uburyo bworoshe bwo gutorera umuti amakosa mu gutanga ubwoko bw'ikosa ry'isi yose bushobora guhinduka ubwabwo buva ku bwoko bw'ikosa bwose bushira mu ngiro akaranga k'ikosa. Iryo hinduka ry’ubwite rituma ukoresha umukoresha w’ikimenyetso c’ikibazo afise ubwoko butandukanye bw’amakosa ata guhindura ry’amaboko, bikaba bituma biba ngirakamaro cane ku bikorwa aho udakeneye gutandukanya ubwoko butandukanye bw’amakosa mu buryo bwa porogarama.


Naho `anyhow` isumba izindi mu kworohereza amakosa mu gukoresha aho amakosa yerekanwa cane cane ku bakoresha, irafise aho igarukira mu gutegura ububiko bw'ibitabo. Kubera ko `anyhow` mu vy'ukuri ihindura amakosa yose mu butumwa bw'urudodo, abaguzi b'ibitabo vyawe ntibashobora kwishura mu buryo bworoshe ku makosa atandukanye. Ivyo bituma `uko biri kwose` bibereye cane ibikorwa vy'abakoresha kuruta amasomero akeneye gutanga amakuru y'amakosa atunganijwe ku baguzi bayo.


Uburyo bwo gutorera umuti amakosa buteye imbere cane bujanye n'uguhingura ubwoko bw'amakosa busanzwe bugereranya uburyo bwihariye bwo kunanirwa kw'ikoreshwa ryawe canke ububiko bw'ibitabo. Igishushanyo c’ikosa giteguwe neza coshobora gutandukanya hagati y’ivyo winjije bitagira akamaro (ivyo uwuhamagara ashobora gukosora), amakosa yo mu gihe co gukora (ashobora gusubirwamwo), n’ukunanirwa guhoraho (kwerekana ibibazo canke ibintu bidashobora gusubirwamwo). Ubu buryo butunganijwe buratuma abaguzi ba kode yawe bafata ingingo zijanye n’ubwenge ku bijanye n’ingene bovyifatamwo ku bwoko butandukanye bw’ibibazo, haba ivyo bisobanura gusubira kugerageza ibikorwa, gutuma abakoresha bashiramwo ibintu bitandukanye, canke gutanga raporo y’ibibazo ku bategura.


## UniFFI, Guhuza amasomero ya Rust mu ndimi nyinshi


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Intangamarara ya UniFFI n'Iterambere ry'Imirongo Mitandukanye


UniFFI ni igikoresho co gutuma amasomero ya Rust ashobora gukoreshwa mu ndimi nyinshi zo gukora porogarama n’ibibanza vyinshi. Ico gikoresho cakozwe na Mozilla, gitorera umuti ingorane nyamukuru mu gutegura porogarama za none: ingene twokoresha neza inyungu z’ubushobozi n’umutekano za Rust mu gihe tuguma duhuye n’ibidukikije bitandukanye vy’iterambere. Ico gikoresho kiraheza kigatanga ururimi rwo gufatanya amasomero ya Rust, bikaba bituma abahinguzi badakeneye gukora n’amaboko kode y’ururimi rwose rwo gukoresha.


Ikibazo nyamukuru UniFFI itorera umuti kiva ku kamere ka Rust nk’ururimi rwo gukoranijwe. Iyo kode ya Rust ikoranijwe, itanga igisohoka c’ibice bibiri gifise igikorwa c’amahanga Interface (FFI) kigaragaza urugero rwo hasi rushobora kuba urugamba gukoresha ataco ruvuze ruvuye mu ndimi zo ku rwego rwo hejuru nka Python, Swift, canke Kotlin. Mu migenzo, umuhinga mu bijanye n’ububiko bw’ibitabu wese yokenera kwandika kode y’ururimi rwose rwo gukoresha, ivyo bikaba bituma habaho intambamyi ikomeye yo kwemerwa n’ibindi bikoresho. UniFFI irakuraho iyo nzira y’ugusubira inyuma mu gutanga uburyo bumwe bwo gutuma ivyo bifatanya bivaho.


Filozofiya y’uguhingura igikoresho ishingiye ku gutuma abahinguzi ba Rust bibanda ku nzira nyamukuru y’ubudandaji bwabo mu gihe batuma amasomero yabo ashobora gushikirwa n’abahinguzi bakora mu zindi ndimi. Umuhinguzi wa iOS akoresha Swift, nk'akarorero, arashobora gukoresha ububiko bwa Rust biciye mu biboshe vyakozwe na UniFFI vyerekana interface ya Swift, ata kimenyetso c'uko ugushirwa mu ngiro kwanditswe muri Rust. Ukwo gukorana neza gutuma amashirahamwe ashobora gukoresha inyungu z'ibikorwa vya Rust ataco asaba abagize amashirahamwe bose kwiga Rust.


### Gutahura ubuhinga bwo kwubaka n'ingene ibikorwa vya UniFFI bigenda


UniFFI ikora biciye mu nzira y’ibikorwa isobanuwe neza ihindura amasomero ya Rust mu bitabo bihuye n’indimi nyinshi. Ivyo bitangura n’uguhingura dosiye y’ururimi rw’insobanuro imwe (UDL), ikora nk’isobanuro ry’ibarabara ridondora ibice vy’ububiko bwawe bw’ibitabu bwa Rust bikwiye gukoreshwa mu zindi ndimi. Iyi dosiye ya UDL ikora nk'amasezerano hagati y'ugushirwa mu ngiro kwa Rust yawe n'imirongo y'ururimi yavutse.


Ubwubatsi bukurikira ugutandukanya gutomoye kw’ibintu bihangayikishije. Abahinguzi babungabunga ububiko bwabo bwa Rust n'imvugo n'ibigereranyo vya Rust, hanyuma bagahingura dosiye ya UDL itandukanye igaragaza ikarita y'urubuga rwa bose ku buryo bw'ubwoko bwa UniFFI. Igikoresho co gufatanya amakuru ca UniFFI gikora ububiko bw’ibitabu bwa Rust be n’ibisobanuro vya UDL kugira ngo gikoreshe amakuru y’ururimi kavukire ku bibanza vy’intumbero bisabwa. Ivyo bifatanya bikora ibikorwa vyose bikomeye vyo gukorana n’ugukuraho amakuru hagati y’igihe co gukoresha ururimi rw’amahanga n’itegeko rya Rust.


Mu gihe c’ugukora, ubwubatsi burarema uburyo buteye imbere aho kode y’ikoreshwa yanditswe mu rurimi rw’intumbero (nka Kotlin ya Android) ikorana na kode y’ubufatanye yavutse isa n’iyivukiye muri urwo rurimi. Iyi nzira y’ugufatanya ikora ubuhinduzi hagati y’ubwoko bw’ururimi n’ubwoko bwa Rust, icungera ubwonko ata nkomanzi ku mipaka y’ururimi, kandi itanga uburyo bwo gutorera umuti amakosa akurikije amategeko y’ururimi rwo gukoresha. Ivyiyumviro vy’ubudandaji vya Rust biguma bitahindutse kandi ntibimenya ivyerekeye indimi nyinshi zubatswe hejuru yavyo.


### Gukorana na UDL: Interface Insobanuro n'Ubwoko bw'Ikarita


Ururimi rw’Insobanuro Rumwe rukora nk’ibuye ry’imfuruka ry’imikorere ya UniFFI, rutanga uburyo bwo gutangaza ibice vy’ububiko bw’ibitabu bwa Rust bikwiye gushirwa ahabona n’ingene bikwiye gushikirizwa mu ndimi zigenewe. Dosiye za UDL zitegerezwa kubamwo nibura umwanya w'amazina umwe, ukora nk'igikoresho c'ibikorwa bishobora guhamagarwa ataco bisaba. Iyi mikorere y'umwanya w'amazina ikora ibikorwa vyoroshe bifata agaciro nk'ibipimo kandi bikagarura ibisubizo.


UDL ishigikira urutonde rw’ubwoko bwubatswemwo bujanye n’ubwoko bwa Rust buhuye. Ubwoko bw'ishimikiro burimwo ibintu vya kera nk'ibiharuro, ubunini bw'imibare itandukanye (u8, u32, n'ibindi), imibare y'inyuguti ziterera, n'imirongo. Ubwoko bukomeye cane burimwo amavectors, amakarata ya hash, n'ivyiyumviro vyihariye vya Rust nk'ubwoko bw'amahitamwo (bugereranywa n'inyuguti y'ikibazo) n'ubwoko bw'Inyishu zo gutorera umuti amakosa. Uburyo bw'ubwoko burashigikira kandi ibara, ibara ryoroshe rishingiye ku gaciro n'ibara rikomeye ririmwo amakuru ajanye, bishobora gutuma habaho ubuhinga bwo guhindura amakuru mu mipaka y'ururimi.


Ivyiyumviro biri muri Rust birahindurwa mu nkoranyamagambo muri UDL, bikaguma bihuye hafi n’umwe mu gihe bihuza n’amategeko y’inyuguti ya UDL. Iyo Rust structs zifise uburyo bujanye n'ivyo, zishobora gushirwa ahabona nk'interfaces muri UDL, iyo generate nk'amashure afise uburyo mu ndimi zishingiye ku bintu nka Kotlin canke Swift. Iyi karata irazigama uburyo bwo guhingura bushingiye ku bintu abahinguzi biteze muri izo ndimi mu gihe bagumana imiterere n’inyifato y’ugushirwa mu ngiro kwa Rust.


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


Ishirwa mu ngiro rya Rust ryoshobora gusobanura ubwo bwoko no gushira mu ngiro akaranga ka `uniffi::export` ku biboshe vya generate vya Kotlin, Swift, Python, n'izindi ndimi zishigikiwe.


### Gufata amakosa n'ibiranga biteye imbere


UniFFI itanga uburyo bwo gutorera umuti amakosa buzigama uburyo bw'amakosa bushingiye ku ngaruka bwa Rust mu gihe buhindurwa neza ku ndimi zigenewe. Imikorere igarura ubwoko bw'ibisubizo muri Rust ishobora gushirwako ikimenyetso n'ijambo ry'ingenzi "throws" muri UDL, igaragaza ubwoko bw'amakosa ishobora gutanga. Aya makosa ategerezwa gusobanurwamwo nk'amakosa enums muri dosiye ya UDL kandi ategerezwa gushirwa mu ngiro akaranga k'Ikosa ka Rust muri kode ya Rust. Igikapu c’amakosa gitanga ubuhinga bwiza bwo gushitsa iyo kamere, kigabanura cane kode y’ivyuma vy’amazi.


Impinduro yo gutorera umuti amakosa yerekana uburyo UniFFI ikoresha mu kumenya ururimi. Mu Kotlin, ibikorwa vyerekanwa nk'ugutera mu buryo bwa UDL generate butera ibidasanzwe bikurikira amasezerano ya Java/Kotlin. Ibohe rya Python naryo nyene rikoresha uburyo budasanzwe bwa Python. Iyi mpinduro ituma gutorera umuti amakosa bimeze nk’ibisanzwe kandi bimeze nk’ibisanzwe mu rurimi rwose rukoreshwa mu gihe bizigama insobanuro y’ubwoko bw’amakosa y’intango ya Rust.


Ivyuma bikoreshwa mu guhamagara bigereranya ikindi kintu giteye imbere gishobora gutuma habaho uguhanahana amakuru hagati y’amasomero ya Rust n’ibikoresho bikoresha. Igihe ububiko bw'ibitabu bwa Rust bukeneye gusubira guhamagara muri kode y'ibikorwa, abahinguzi barashobora gusobanura ibiranga muri Rust maze bakabishirako ikimenyetso nk'ibihuza gusubira guhamagara muri UDL. Igikoresho gikoresha ivyo bikoresho gishira mu ngiro izo nzira mu rurimi rwabo kavukire, kandi UniFFI ikora ibikorwa bikomeye bisabwa kugira ngo ihamagare izo nzira zivuye muri kode ya Rust. Iyi nzira isaba ko umuntu yiyumvira neza umutekano w’urudodo, kuko guhamagara bishobora kujabuka imbibe z’urudodo, bikaba bisaba ko haba imbibe zo kohereza no gukorana ku ruhande rwa Rust.


### Ibikorwa vyo mw'isi nyakuri n'imipaka iriho ubu


UniFFI yaremewe mu muryango w’iterambere ry’amahera y’ibanga n’ivy’ubuhinga bwa none, n’imigambi ikomeye nka BDK (Igikoresho co guteza imbere Bitcoin), LDK (Igikoresho co guteza imbere umuravyo), n’ugushirwa mu ngiro gutandukanye kwa wallet bikoresha mu gutanga SDKs zigendanwa. Iyi migambi yerekana uko UniFFI ikoresha mu bidukikije vy’ubuhinga.


Gusuzuma amadosiye ya UDL y’ukuri avuye muri iyo migambi birerekana uburyo n’ingene ibikorwa vyiza vyavuye mu gukoresha mu buryo bubereye. Nk'akarorero, dosiye ya UDL ya BDK yerekana ingene ibigereranyo vy'intara bikomeye bifise amabara menshi, imiterere, n'imirongo bishobora gukoreshwa neza kugira ngo haboneke SDK zigendagenda zitandukanye. Uguhuza kw’inyuguti ya UDL mu migambi itandukanye bisigura ko abahinguzi bamenyereye ububiko bumwe bukoreshwa na UniFFI bashobora gutahura ningoga no gukorana n’abandi, bikaba bituma habaho ingaruka z’uruja n’uruza zigirira akamaro ibidukikije vyose.


Ariko rero, UniFFI irafise aho igarukira abahinguzi bategerezwa kwitwararika. Igihambaye cane ni ukubura ugushigikirwa kw’imirongo idakorana. Ivyo vyose bifatanya birahuye, bisaba abahinguzi gukora ibikorwa bitahuye muri kode yabo ya Rust no gutanga imirongo ihuye ku bikorwa bikoresha. Ikindi, gushiramwo inyandiko birazana ingorane: inyandiko zanditswe muri kode ya Rust ntizija mu biboshe vyavutse, mu gihe inyandiko ziri mu madosiye ya UDL zitaboneka kugira ngo ziyobore abaguzi ba Rust bo mu bubiko bw’ibitabu. Naho hariho utwigoro tubandanya two gutorera umuti izo nzitizi biciye mu gusesangura no guhingura, ziguma ari izo kwitwararika mu gushirwa mu ngiro kw’ubu. Ubwa nyuma, UniFFI itanga ubufatanye bw’ururimi ariko ntikora ku bijanye n’ugupfunyika n’ugukwiragiza kw’urubuga, bikasiga abahinguzi gucungera intambwe za nyuma zo guhingura amapaki ashobora gukwiragizwa ku rubuga rwose rw’intumbero.


# Gutegura LNP/BP na SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## LN urudodo kuri SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### Gutahura ubwubatsi bwa LDK


Igikoresho co gutegura umuravyo (LDK) gifata uburyo butandukanye bwo gushirwa mu ngiro kwa Lightning Network ugereranyije n'ubuhinga bwa kera nka CLightning canke LND. Naho ama node asanzwe ya Lightning akora nk’ibikorwa vyuzuye vya daemon bikora ubudasiba ku mashini, LDK ikora nk’ububiko bw’ibitabu bwa Rust butanga ibice vya kera vyo kwubaka inyishu za Lightning zisanzwe. Iryo tandukaniro ry’ubwubatsi rituma LDK ishobora guhinduka, bikaba vyemerera abahinguzi gukoranya ibikorwa vya Lightning mu buryo bujanye n’ibisabwa vy’umugambi wabo.


Filozofiya nyamukuru iri inyuma ya LDK ishingiye ku guhindura ibintu no guhindura ibintu. Aho gutanga umuti w’ikintu kimwe, LDK itanga ibihimba bimwebimwe bishobora guhurizwa hamwe, guhindurwa canke gusubirizwa vyose. Igice kimwekimwe cose kizana n'ibikorwa vy'imbere bikora hanze y'agasanduku, ariko abahinguzi bagumana umwidegemvyo wo gusubirira ibikorwa vyabo iyo bikenewe. Nk’akarorero, LDK irimwo ibikorwa vy’ugukurikirana blockchain, gusinya ku bikorwa, no guhanahana amakuru ku rubuga, yamara ivyo vyose birashobora gusubirizwa n’imiti isanzwe ihuye n’ibintu vyihariye vy’ikoreshwa canke ibidukikije.


Iyi nzira y’ibice ishoboza LDK gukora ku mbuga zitandukanye no ku bintu vyoba bigoye ku nzira za kera z’umuravyo. Porogaramu zikoreshwa kuri telefone ngendanwa, amaporogarama y’urubuga, ibikoresho vyinjijwemwo, n’ibikoresho vy’ubuhinga bwihariye vyose birashobora gukoresha ibihimba vya LDK mu buryo bujanye n’ingorane zavyo n’ivyo bisabwa. Ubwubatsi bw’isomero buratuma abahinguzi bashobora guhingura porogarama zikoreshwa na Lightning batafunzwe mu mice y’imikorere yategekanijwe canke mu bishingiye kuri sisitemu.


### LDK ikoresha ibibazo n'uguhinduranya urubuga


Uguhinduranya kw'ubwubatsi kwa LDK gufungura ibikorwa vyinshi vy'ikoreshwa bishika kure cane y'ugukoresha imirongo y'umuravyo. Iterambere rya wallet ry'amatelefone ngendanwa rigereranya kimwe mu bikoresho bikomeye cane, aho LDK ishoboza guhingura amasakoshi y'umuravyo atagira ububiko asa na Phoenix wallet. Ivyo bikoresho bishobora kuguma bigenzura abakoresha imfunguruzo z’ibanga mu gihe bikorana n’abatanga ibikorwa vya Lightning (LSPs) igihe baza kuri interineti, bikaba vyemerera kwakira amahera ata nkomanzi no gucunga imirongo mbere n’aho hariho uguhuza kw’ibihe bimwe bimwe.


Ugushiramwo umutekano w’ibikoresho (HSM) vyerekana ikindi kintu gikomeye co gukoresha LDK. Mu gukuraho gusa ibice vyo gusinya no kugenzura ibikorwa, abahinguzi barashobora guhingura ibikoresho vyo gusinya bimenya Lightning bitahura ivyerekeye n’ingaruka z’ibikorwa vya Lightning. Ubwo bushobozi burarenga gusinyana amasezerano yoroshe kugira ngo bushiremwo isesengura ry’ubwenge ry’ugurungika amahera, ibikorwa vy’imirongo, n’ingingo zihambaye cane ku bijanye n’umutekano. HSM irashobora gusuzuma nimba igikorwa giserukira ukwishyura mu buryo bubereye, igikorwa co gutuma umuntu agira inzira, canke ukugerageza bishobora kuba ari bibi, bikaba biha abakoresha ubumenyi bufise insiguro ku bijanye n’umutekano.


Ibikoresho vy’umuravyo bishingiye ku rubuga vyungukira cane ku buhinga bwa LDK bwo guhingura ibintu ata n’umwe ahamagaye. Kubera ko ibidukikije vya WebAssembly bitagira uburyo bwo gushika ku bikoresho vya sisitemu nk’ibidukikije vy’amadosiye, amasokete y’urubuga, canke inkomoko z’entropi, uburyo butagira agasembwa bwa LDK butuma imikorere ya Lightning ikora neza mu bidukikije vy’umucukumbuzi. Abahinguzi barashobora gushiramwo ivyicaro vy’uruja n’uruza bakoresheje WebSockets kandi bagatanga ubukomezi buhuye n’umucukumbuzi n’inkomoko z’ubudasa mu gihe bagumye bubahiriza amategeko yuzuye ya Lightning.


### Ibice nyamukuru n'ubwubatsi bushingiye ku bintu


Ubwubatsi bw’imbere muri LDK buzunguruka ibice vyinshi vy’ingenzi bikorana biciye mu buryo bushingiye ku bintu bishika. Uburyo bwo gucunga urunganwe burakora ivy’uguhanahana amakuru vyose n’izindi nzira za Lightning, bugashira mu ngiro umurongo w’urusaku wo gupfuka no gucunga imiterere y’ubutumwa kugira ngo amategeko ya Lightning yubahirizwe. Ico gice gikora kidashingiye ku buryo bwo gutwara ibintu, kigatuma abahinguzi bashobora gushiramwo ubuhinga bwo gukorana n’abandi biciye ku bikoresho vya TCP, WebSockets, amahuriro y’uruhererekane ya USB, canke ubundi buryo bwose bwo guhanahana amakuru bufise inzira zibiri.


Umuyobozi w’umurongo akora nk’umuhuzabikorwa mukuru w’ibikorwa vy’umurongo wa Lightning, akora cane n’umuyobozi w’urunganwe kugira ngo akore ibikorwa vyo gufungura, gufunga no kwishura umurongo. Iyo umuhinguzi atanguye gufungura umurongo, umuyobozi w’umurongo arema ubutumwa bukenewe bw’amasezerano maze agahuza n’umuyobozi w’urunganwe kugira ngo ashobore gukora igikorwa co guhanahana amakuru mu ntambwe nyinshi. Ukwo gutandukanya ivyiyumviro bituma habaho ugutahura gusukuye hagati y’ubuhinga bwa Lightning n’ibisobanuro vy’itumanaho ry’urubuga.


Uburyo bw'ibintu vya LDK butanga amatangazo atari yo ku bikorwa vyose bihambaye n'amahinduka y'intara. Ivyabaye bipfutse ibikorwa vyose vya Lightning, kuva ku guhuza n’uguca ku nzira gushika ku kuroranirwa no ku kunanirwa kw’ukwishura, amahinduka y’imirongo, n’ivyemezo vy’imirongo. Ubu buryo bushingiye ku bintu bishika buratuma ibikorwa bishobora kwishura neza ku bikorwa vy’urubuga rwa Lightning mu gihe bigumya itandukaniro risukuye hagati y’imikorere nyamukuru ya LDK n’ubuhinga bwihariye bw’ibikorwa. Abahinguzi barashobora gushiramwo ibikoresho vy’ibintu bimenyerewe bihindura imirongo y’abakoresha, bitera amatangazo, canke bitanguza ibikorwa vyo gukurikirana bishingiye ku bintu vy’urubuga rwa Lightning.


### Blockchain Ubufatanye n'Ubucungezi bw'Amakuru


Blockchain data integration iserukira kimwe mu bice vy’ubuhinga bwa LDK, vyagenewe kwakira vyose kuva ku nzira zuzuye za Bitcoin gushika ku bakiriya bagendagenda bafise uburemere buke. LDK ishigikira uburyo bubiri bw’intango bwo gukorana n’ibindi bikoresho, buri bumwe butunganijwe neza kubera ingorane zitandukanye z’ubutunzi n’ibisabwa vyo gukora. Uburyo bw’amabuye yuzuye buremesha ibikorwa bifise uburenganzira bwo kuronka amakuru yuzuye y’amabuye y’agaciro kugira ngo bishikirize amabuye yose kuri LDK, bikaba bishoboza gukurikirana ibikorwa vyose no gusubiza ubwo nyene ibintu bifitaniye isano n’ivy’amabuye y’agaciro.


Ku bidukikije bifise ubutunzi buke, LDK itanga uburyo bushingiye ku kuyungurura bugabanya uburebure bw’umurongo n’ibisabwa vyo kubika. Muri ubu buryo, LDK imenyesha inyungu zayo zo kugenzura biciye ku nzira zitaboneka, isaba gukurikirana IDs z’ibikorwa vyihariye, UTXOs, canke uburyo bw’inyandiko. Igikoresho gishobora rero gushitsa iyo nzira yo kugenzura hakoreshejwe amaserveri ya Electrum, abashakashatsi b’amabarabara, canke ayandi makuru y’amabarabara yoroshe. Ubu buryo buratuma ama wallets y’amatelefone ngendanwa n’ibikoresho vyo ku rubuga bishobora kuguma bikora Lightning ataco bisaba gukorana n’ibindi vyose.


Igipande c’ugushikama muri LDK gikurikira ingingo ngenderwako nyene z’ugutahura, kigatanga ibikorwa bifise amakuru y’ibice bibiri ategerezwa kubikwa no kuronswa mu buryo bwizigirwa. LDK ikora ibikorwa vyose bigoranye vyo gukurikirana no gukuraho urutonde rw’imirongo ya Lightning, amakuru y’urusaku rw’urubuga, n’ayandi makuru ahambaye. Ibikoresho bikeneye gusa gushiramwo uburyo bwo kubika bwizewe, haba hakoreshejwe uburyo bwo kubika amadosiye bwo mu karere, ibikorwa vyo kubika amakuru mu gicu, canke uburyo bwihariye bwo kubika amakuru. Iyi nzira ituma uburongozi bwa Leta ya Lightning buguma bukomeye mu gihe yemerera ibikorwa guhitamwo inyishu zo kubika zihuye n’ibisabwa vyo gukora n’ibigereranyo vy’umutekano.


### Ibirango biteye imbere n'imirongo yo kwinjiza


Ubushobozi bwa LDK burashika no ku biranga Lightning Network nk’ukwishura mu nzira nyinshi, gutuma inzira zigenda neza, no gucunga urusaku rwo ku rubuga. Uburyo bwo gutanga inzira buragumya iciyumviro gitomoye c’ivy’ubuhinga bwa Lightning Network biciye mu kwifatanya n’amasezerano y’urusaku, bikaba bishoboza kurondera inzira y’ubwenge yo kwishura. Ibikorwa birashobora guhindura ingingo z’inzira biciye mu mirongo y’imiterere kandi birashobora no gushiramwo uburyo bwo gukoresha inzira busanzwe ku bikorwa vy’ikoreshwa vyihariye.


Uburyo bwo gufatanya ururimi bw’isomero burashoboza gukorana na LDK mu bidukikije vyinshi vy’iporogarama, bugafasha Java, Kotlin, Swift, TypeScript, JavaScript, na C++. Ukwo gukorana n’ibindi bikoresho bitandukanye bituma porogarama zo kuri telefone ngendanwa zanditswe mu ndimi kavukire zishobora gushiramwo ibikorwa vya Lightning mu gihe ziguma zifise ibiranga ibikorwa vyiza. Uburyo bwo gufatanya burazigama ubuhinga bwa LDK bushingiye ku bintu n’imiterere y’ibice mu ndimi zose zishigikiwe, bikaba vyemeza ko ubumenyi bw’abahinguzi buhuye ataco buvuze ku rubuga rw’intumbero.


Igereranyo ry’amahera n’ugutangaza amakuru y’ibikorwa bigereranya ibindi bice aho LDK itanga uburenganzira bwo guhindura. Ibikorwa birashobora gushitsa ingamba zo kugereranya amafaranga zishingiye ku migenzo zijanye n’ingene zikora n’ivyo abakoresha basaba. Na vyo nyene, ugutangaza amakuru y’ibikorwa birashobora guhindurwa kugira ngo bikore n’imirongo itandukanye y’urubuga rwa Bitcoin, kuva ku nzira zitaziguye za full node gushika ku bikorwa vy’ugutangaza amakuru vy’abandi. Ukwo guhinduranya gutuma ibikorwa bishingiye kuri LDK bishobora gutuma imigenderanire yavyo y’ubuhinga bwa none igenda neza kubera ibikorwa vyavyo vy’umwihariko mu gihe bigumya ivyubahiriza amategeko ya Lightning n’ingingo mfatirwako z’umutekano.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### Ingorane y'iterambere ry'umuravyo


Gutegura porogaramu zifatanya n’amahera y’umuravyo biratanga intambamyi ikomeye ku bategura benshi. Kugira ngo ureme app ifise ubushobozi bwo kwishura Lightning, abayikora barakeneye cane kuba abahinga mu Lightning, bagatahura ivyiyumviro bikomeye nk’ugucungera imirongo, gucungera amafaranga, n’ugutunganya urubuga. Ivyo bisabwa vy’ubuhinga biratuma haba ingorane y’ishimikiro ku kwemera Lightning: naho urubuga rwa Lightning ubwarwo rukora kandi ukwishyura kwizigirwa, ubuhinga butoroshe burabuza gukwiragizwa mu bikorwa vya misi yose.


Ingorane nyamukuru iri mu ntambamyi iri hagati y’ivyo abahinguzi bakeneye n’ivyo bashaka gutanga. Abahinguzi bakora mu bihe vy’iherezo bikomeye kandi bakunda inyishu zigororotse zituma bibanda ku mikorere nyamukuru y’ikoreshwa ryabo aho kuba abahinga mu bikorwa remezo vyo kwishura. Iyo Lightning integration igoye, abahinguzi barakwegeranya mu buryo busanzwe ku mirongo y’ububiko kuko itanga inzira y’ukurwanywa guke. Ariko rero, iyo mpengamiro yo gukora ibikorwa vy’ububiko irahungabanya iciyumviro c’agaciro k’ishimikiro ca Bitcoin c’ubusegaba bw’ivy’ubutunzi butagira ububiko.


### Iyerekwa rya Breez, Umuravyo Hose


Breez yavuye mu ciyumviro coroshe ariko gifise icipfuzo kinini: gutuma umuntu wese ahuzwa n’urubuga rwa Lightning biciye ku nzira zisanzwe zijanye n’ubutunzi bwa Lightning. Uburyo iyo sosiyete ikoresha buratahura ko naho urubuga rwa Lightning rukora neza mu vy’ubuhinga, rukeneye cane kwemerwa n’abarukoresha kugira ngo rushike ku bushobozi bwarwo bwose. Iyi ngorane yo kwemera irarenga abakoresha ku giti cabo kugira ngo ishiremwo ibidukikije vyose vy’ibikorwa n’ibikorwa bishobora kwungukira ku gukorana n’umuravyo.


Iryo koraniro ry’intango rya Breez ryerekanye iyo nzira mu guha abakoresha urudodo rw’umuravyo rudashobora gucungerwa rukora ataco ruri ku matelefone yabo ngendanwa. Iyi porogaramu yerekanye ubushobozi bwa Lightning nk’ugutanga amafaranga make ku ba podcasters n’imikorere y’aho bagurisha. Ariko rero, porogarama ya Breez nayo yerekanye ikintu gikomeye c’ubwubatsi: ubuhinga bwa porogarama y’amatelefone ngendanwa ntibworosha guhanahana amakuru hagati y’ibikorwa, bikaba bihatira abahinguzi kwubaka ibintu vyose bijanye na Lightning muri porogarama imwe aho kwemera ko ibikorwa vyihariye bikoresha ibikorwa remezo vya Lightning bisangiye.


Ivyo iyo sosiyete yize kuri app Breez vyatumye ibona ikintu gihambaye cane: kazoza k’ukwemera Lightning kavana no gutsinda abayikora. Iyo ubufatanye bwa Lightning butagira ububiko bubaye uburyo bworoshe ku bategura, buca buba uburyo bwo guhitamwo. Ubwo buryo kandi buratanga inyungu mu bijanye n’amategeko, kuko porogarama zitari izo mu bubiko zihura n’intambamyi nkeyi zijanye n’amategeko kuruta ibikorwa vyo mu bubiko, ivyo bikaba bituma abahinguzi bashobora kwohereza porogarama zabo kw’isi yose.


### Ubwubatsi bwa Breez SDK


Breez SDK itanga uburyo bundi bwo gushiramwo ibikorwa vya Lightning mu bikorwa. Aho gusaba ko porogarama yose ikoresha urudodo rwayo rw’umuco, SDK itanga ubuhinga bugumya ingingo ngenderwako zitari izo kuzigama mu gihe yorosha ubumenyi bw’abahinguzi. Mu ntumbero yayo, SDK iha umukoresha wese w’iherezo urudodo rwiwe bwite rw’umuravyo rukoreshwa ku bikorwa remezo vya Greenlight, igikorwa ca Blockstream co kwakira urudodo rw’umuravyo rushingiye ku gicu.


Ubwo buhinga bwo kwubaka buratorera umuti ingorane nyinshi zikomeye icarimwe. Abakoresha ntibakeneye kwiganyira ku bijanye n’ugucungera urutonde rw’amakuru, igihe server ikoresha canke gucungera ibikorwa remezo—ivyo vyoba ari ivyiyumviro bikomeye cane ku baguzi basanzwe. Ariko rero, bitandukanye n’imiti y’ububiko bwa kera, Greenlight ntiyigera ironka uburenganzira bwo gukoresha imfunguruzo z’abakoresha. Igikoresho c’umuravyo kiri mu gicu ntigishobora gukora ibikorwa vyose ata gikoresho gihuye neza gishobora gusinya amafaranga n’ubutumwa. Iyi nzira igumya inyungu z’umutekano zo kwibungabunga mu gihe ikuraho ubugoyagoye bwo gukora.


SDK nayo irashigikira ugukorana. Ibikoresho vyinshi birashobora gufatanya n’umurongo w’umuravyo w’umukoresha umwe hakoreshejwe ijambo rimwe seed, bikaba vyemerera abakoresha kuguma bafise uburinganire bumwe bw’umuravyo mu bikoresho bitandukanye vy’umwihariko. Nk’akarorero, uwukoresha yoshobora kugira porogarama rusangi ya Lightning wallet be n’iporogarama yihariye yo gutangaza amakuru, vyose bikaba bishobora gushika ku mahera amwe n’imihora ya Lightning. Ubwo buhinga buratuma habaho uguteza imbere ibikorwa vy’ubuhinga vyihariye kandi vyihariye mu gihe haguma hariho ibikorwa remezo vy’ivy’ubutunzi bimwe.


### Abatanga ibikorwa vy'umuravyo n'amahera y'igihe nyene


Ikintu gihambaye ca Breez SDK ni ugufatanya kwayo n’abatanga ibikorwa vy’umuravyo (LSPs), bakora nk’abatanga ibikorwa vya Internet ariko ku rubuga rwa Lightning. LSPs zitorera umuti kimwe mu bibazo bikomeye cane vya Lightning: ugucungera amafaranga. Mu mihora y’umuravyo, amahera ashobora guca gusa mu nzira aho amahera ari, nk’amabuye ari ku gitereko c’amabuye ashobora guca gusa aho hari umwanya.


SDK ishira mu ngiro imirongo "just-in-time" biciye mu ma LSP, igacungera amafaranga ataco umukoresha akora. Iyo umukoresha akeneye kwakira amahera ariko atagira amahera ahagije yinjira, LSP ica ifungura umurongo mushasha wa Lightning mu gihe amahera ashika. Ivyo bigenda ata nkomanzi mu nyuma, bikaba vyerekana ko abakoresha bashobora kwama baronka amahera batatahura ubuhinga bw’imirongo y’inyuma.


Ukwo gushiramwo LSP kurarenga uburongozi bworoshe bw’amahera. SDK irimwo ibikorwa vyose vya Lightning bitari mu gasandugu: ibikorwa vy’umutekano vyubatswemwo, on-chain gukorana biciye mu guhinduranya ubwato, fiat on-ramps biciye mu bikorwa nka MoonPay, n’ugushigikira amasezerano ya LNURL. Ubuhinga kandi buratanga ububiko n’ugusubirana ata nkomanzi, bigatuma abakoresha batigera batakaza uburenganzira bwo kuronka amahera yabo naho abatanga ibikorwa remezo bohinduka canke ntibaboneke.


### Ishirwa mu ngiro n'ubumenyi bw'abategura


Breez SDK ishira imbere ubumenyi bw’abahinguzi biciye mu buryo bwayo bushitse, bufise amabateri. SDK itanga ubufatanye bw’indimi nyinshi zo gukora porogarama harimwo Rust, Swift, Kotlin, Python, Go, React Native, Flutter, na C#, bikaba vyemerera abakora porogarama gushiramwo amahera y’umuravyo bakoresheje ibikoresho vy’iterambere bakunda. Ubwubatsi burakuraho ubugoyagoye bwa Lightning biciye ku APIs mu gihe bugumya umutekano w’urubuga rwa Lightning.


Ibice nyamukuru birakorana kugira ngo bihe ubwo bumenyi bworoshe. Igikoresho co gusesangura ivyinjijwe gikora ubwaco uburyo butandukanye bwo kwishura, kigamenya nimba urudodo rugereranya invoice, LNURL, canke ubundi buryo bwo kwishura maze kikarurungika ku gikorwa co kwishura kibereye. Igikoresho co gusinya kijejwe gucungera ibikorwa vyose vy’ubuhinga bwo gukingira amakuru mu nyuma, mu gihe igikoresho co guhindura amakuru gicungera imigenderanire ya on-chain mu buryo buboneye. Iyi nzira ituma abahinguzi bibanda ku ciyumviro c’agaciro kidasanzwe c’ikoreshwa ryabo aho kuba abahinga mu vy’ibikorwa remezo vya Lightning.


Ubwubatsi bwa SDK butagira icizigiro buratuma naho Greenlight ishobora kwihweza ivy’imirongo n’amakuru y’inzira, ntishobora kuronka amahera y’abakoresha canke gukora ibikorwa bitaremewe. Abakoresha baraguma bafise ububasha bwose ku mfunguruzo zabo z’ibanga, zitazokwigera ziva ku bikoresho vyabo. Ubwo buryo bugereranya uguhuza kwiyumviriwe neza hagati y’ukworohereza ibikorwa n’ubuzima bwite, butanga inzira ngirakamaro yo kwemera Lightning mu gihe hazigama ingingo ngenderwako nyamukuru za Bitcoin z’ubusegaba bw’ivy’ubutunzi.


## LDK na Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Gutahura imipaka y'ibikoresho vyo guteza imbere umuravyo (LDK)


Igikoresho co gutegura umuco ni ihuriro ry’amasomero ya Rust yagenewe guha abategura uburyo bwo guhindura igihe bubaka ibikorwa vya Lightning Network. Ariko rero, ukwo guhinduranya biza n'ingorane zikomeye zo gushirwa mu ngiro zabonetse mu gihe c'iterambere ry'isi nyakuri kuri Lipa. Kamere ya LDK iri ku rugero ruto bisigura ko abahinguzi bategerezwa gukora ibikorwa vyinshi bigoranye bigenjeje neza, kuva ku guhuza igishushanyo c’urubuga gushika ku gutuma inzira y’ukwishura igenda neza. Naho ubu buryo butanga ubugenzuzi bwose ku gushirwa mu ngiro kwa Lightning, bisaba uburyo bwinshi bwo gutegura n’ubuhinga bwimbitse kugira ngo umuntu ashike ku kwizigirwa kwiteguriye gukora.


Kimwe mu bintu bihambaye cane vyari vyabuze muri LDK ni ugushigikira LNURL, urugero rwemewe cane rworohereza imigenderanire ya Lightning Network ku bakoresha. Ikindi, ukutagira ibiva mu bikorwa vy’ubuhinga bwa none vyatumye haba ingorane zikomeye mu bikorwa, cane cane mu bibanza vy’amahera menshi. Ivyiyumviro vya Anchor bitorera umuti ingorane y’ishimikiro n’ugufunga inguvu z’imirongo ya Lightning: iyo amafaranga y’uruja n’uruza ateye imbere cane, imirongo ifise amafaranga yategekanijwe imbere y’igihe yoshobora kutaba ishoboka gufunga ku ruhande rumwe kubera ko amafaranga yategekanijwe imbere y’igihe aba adahagije kugira ngo umuntu yemeze ko akora ibikorwa. Ivyo vyagaragaye ko ari ingorane cane cane ku bikorwa vy’amatelefone ngendanwa vya wallet, aho abakoresha bashobora guheba wallet batahuje ugufunga imihora y’ubufatanye, bikaba bisiga amahera ashobora guhagarara mu gihe amafaranga yongerekana.


Ugukura kwa LDK kwagaragaye kandi mu nzira y’ukwishura idashobora kwizigirwa, ikibazo gikomeye ku gikorwa cose ca Lightning. Naho ari ugushirwa mu ngiro gukomeye mu vy’ubuhinga, urugero rwagutse rwa LDK nk’umuti rusangi rwatumye bigorana gutorera umuti ibibazo vyihariye vyihuse. Ishirahamwe ry’iterambere ryasanze rimara umwanya munini ritorera umuti ingorane z’inzira no gushirwa mu ngiro ibintu bikwiye gukorwa neza ku rwego rw’ububiko bw’ibitabu, amaherezo bikagira ingaruka ku muvuduko w’iterambere n’uburyo bw’ubumenyi bw’abakoresha.


### Kumenya ivyiza vya Breez SDK n'umuco w'icatsi kibisi


Ihinduka ry’ubuhinga bwa Breez SDK ryari rigereranya uguhinduka mu buryo bw’ubwubatsi, kuva ku nzira y’umuravyo yigenga gushika ku muti ushingiye ku gicu ukoreshwa n’igikorwa ca Greenlight ca Blockstream. Iryo hinduka ryaciye ryisubiriza ubwo nyene ingingo zitari nke zikomeye z’ububabare zashikiwe n’ugushirwa mu ngiro kwa LDK. Iterambere rikomeye cane ryaje mu kwizigirwa kw’amahera, ahanini bivuye ku bushobozi bwa Greenlight bwo kubungabunga igicapo c’urubuga rwama ruriho. Udakunze gukoresha ubuhinga bwa kera bwa Lightning bugendagenda butegerezwa guhuza amakuru y’urubuga igihe porogarama itangura, ama node ya Greenlight akora ubudasiba mu gicu, akaguma amenye urubuga mu gihe nyaco kandi agatanga amakuru yuzuye y’igishushanyo igihe abakoresha bahuye.


Iyi nyubakwa ikoresha ubuhinga bwa Core Lightning (CLN) bwageragejwe mu ntambara, bumaze imyaka bugenda neza nk’imwe mu nzira z’intango za Lightning Network. Ubumenyi bwarundanijwe n’ukwizigirwa kwagaragaye kwa CLN vyatumye habaho iterambere ry’ugushikama ry’umugambi wa LDK mutoyi. Iyo abakoresha bakoresheje wallet yabo ikoreshwa na Greenlight, baca baragira ubumenyi bwose bw’urubuga n’ubushobozi bwo gukoresha inzira y’uruzitiro rwa Lightning ruguma rukora, bikaba bikuraho ugucererwa kw’ugukorana n’ukudakeka kw’inzira vyari bibabaje mu gushirwa mu ngiro kwa kera.


Ivyiyumviro vy’imiterere ya Breez SDK vyari ngirakamaro mu gutegura wallet. Aho gutanga igikoresho ca Lightning rusangi, Breez yibanda canecane ku bikorwa vy’abakoresha ba wallet, bikaba vyemerera umugwi w’iterambere wibanda ku nguvu zabo ku guhingura inyishu zitomoye kuri iki kibazo c’ikoreshwa ry’umwihariko. Ubwo buryo bushingiye ku ntumbero bwatumye Breez ishobora kwinjiza ibikorwa vy’ingenzi ataco bihinduye muri SDK, harimwo n’imikorere ya Lightning Service Provider (LSP) ituma abakoresha bashobora kwakira amahera ubwo nyene iyo wallet ishizweho, ataco bisaba kugira ngo umuntu akoreshe uburyo bwo gufungura umurongo n’amaboko.


### Ibirango vyose n'ubumenyi bw'abakoresha


Uburyo buhuriweko bwa Breez SDK burarenga ibikorwa vy’ishimikiro vya Lightning, bushiramwo ibintu bituma umuntu ashobora gukoresha neza. Ugushiramwo LSP kwubatswemwo kurakuraho intambamyi ya kera yo gusaba abakoresha gutahura uburongozi bw’imirongo, bikaba bishoboza kwakira amahera ubwo nyene ku bikoresho bishasha vya wallet. Iyi nzira yo gushiramwo ifasha mu kwemera abantu bose, kuko abakoresha bashobora gutangura kwakira amahera ya Lightning ata bumenyi bw’ubuhinga canke uburyo bwo gutegura.


Ibikorwa vy’uguhinduranya ku murongo bitanga uwundi murongo wo gutuma ubumenyi bw’abakoresha bugenda neza mu gutuma abakoresha bashobora gushikiriza uburinganire bumwe. Aho guhatira abakoresha gutahura itandukaniro riri hagati ya Lightning na on-chain Bitcoin, igikorwa co guhinduranya gishobora guhindura ubwaco hagati y’izo nzira uko bikenewe. Igihe abakoresha bakeneye kwishura on-chain, iyo sisitemu irashobora guhindura ata nkomanzi amahera ya Lightning ku on-chain Bitcoin inyuma y’ivyo biganiro, igakomeza kwihenda kw’uko hariho uburinganire bumwe, bw’amazi mu gihe ikorana n’ibintu bigoranye vy’ubuhinga imbere.


Infashanyo ya SDK ku bizigamirwa vy'imirongo ya zero iratorera umuti ingorane ikomeye y'ubumenyi bw'abakoresha mu gushirwa mu ngiro kwa Lightning kwa kera. Ivy’ububiko bw’imirongo mu bisanzwe bibuza abakoresha gukoresha amahera yabo yose yerekanwa, bikaba bitera urujijo iyo amahera yishurwa ataco ashoboye naho bisa n’uko amahera ahagije. Mu gukuraho ivyo bizigamirwa, Breez irashoboza abakoresha gukoresha amahera yabo yose yerekanwa, naho ivyo bisaba ko LSP yemera ingorane z’inyongera. Ivyo bihuza bitanga akarorero k’uburyo bwa Breez bushingiye ku bakoresha, aho ubuhinga butoroshe n’ingorane bifatwa n’abatanga ibikorwa kugira ngo bareme ubumenyi bw’abakoresha busanzwe.


Ibindi bimenyetso nk’ugushigikira LNURL, ibikorwa vy’uguhindura amafaranga, n’uguhuza ibikoresho vyinshi birarushiriza kwerekana uburyo SDK ikoresha mu gutegura wallet. Ubwubatsi bushingiye ku gicu buratuma abakoresha bashobora gushika ku nzira yabo ya Lightning bakoresheje ibikoresho vyinshi canke ibikorwa vyinshi, Breez ikaba ikorana n’uguhuza ibintu muri ivyo bibanza bitandukanye vyo gushikamwo. Ibintu vy’ikarata y’inzira vyo muri kazoza birimwo gukoresha vyose kugira ngo wallet ishobore gukura amazi mu mazi, gukoranya amazi kugira ngo haboneke uburongozi bw’imirongo y’amazi, n’isoko ry’amashirahamwe y’ubuhinga bwa none (LSPs) kugira ngo haboneke uguhiganwa gukomeye mu gutanga ibikorwa.


### Gusuzuma ivy'uguhuza n'ivy'ugushira hamwe


Guhindukira ukaja kuri Breez SDK na Greenlight bizana amasezerano ahambaye yo gushiramwo ubutegetsi hagati ategerezwa kwihwezwa neza mu bijanye n’ingingo ngenderwako zo gushiramwo ubutegetsi hagati za Bitcoin. Ubwubatsi bushingiye ku gicu bisigura ko ama node y’abakoresha ya Lightning akora ku bikorwa remezo vya Blockstream, bikaba bituma habaho ivyifatamwo ku bikorwa vya Greenlight bikomeza no ku gutera imbere kwa Breez. Ukwo gushiramwo amahera hamwe kurarenga gusa, bishobora kugira ingaruka ku bushobozi bw’abakoresha bwo gusubirana amahera iyo ibikorwa bitabonetse canke iyo habayeho ugucengera.


Ivyiyumviro vyo gusubirana biratanga ingorane zidasanzwe muri iyo nyubakwa. Naho abakoresha bagumye bagenzura imfunguruzo zabo z’ibanga, kuronka amahera ata bikorwa remezo vya Greenlight vyosaba ubuhinga bwo guhindura ama node yigenga ya Core Lightning no kugarura imirongo y’imirongo. Ku bakoresha ku giti cabo, iyo nzira yo gusubirana yoshobora kuba igoye cane, kandi mbere n’abatanga wallet bohura n’ingorane zikomeye zo kwimurira ibibanza vyose vy’abakoresha mu bindi bikorwa remezo iyo ibikorwa vya Greenlight bihagarara.


Ivyerekeye ubuzima bwite na vyo nyene birahinduka bitewe n’iryo hinduka ry’ubwubatsi. Ivyo bikoresho bishingiye ku gicu bisigura ko Greenlight ishobora kubona aho umuntu yishura, mu gihe ubuhinga bwa kera bwa LSP gusa bwagabanya amakuru ku rugero rw’amahera n’igihe co kwishura. Invoice mu gicu irarushiriza kwagura amakuru ashobora gushirwa ahabona, kuko amafagitire atakoreshejwe mbere yaguma ari ay’ibanga ku bikoresho vy’abakoresha ubu aca mu bikorwa remezo vya Blockstream.


Naho ivyo bibazo vyo gushiramwo ibintu vyose hamwe, inyungu ngirakamaro akenshi ziruta ingorane zo mu vyiyumviro ku bikorwa vyinshi. Ukwizigirwa gukomeye, urutonde rw’ibintu vyose, n’ubumenyi bwiza bw’abakoresha bituma abahinguzi ba wallet bibanda ku buhinga bushasha bwo gukoresha aho kwibanda ku gucunga ibikorwa remezo vya Lightning. Ukwo gucapura kw’ibikorwa kwerekana uburyo bwo gukura aho abatanga ibikorwa vy’ubuhinga bwihariye bafata ingingo zikomeye z’ubuhinga, bikaba bituma abahingura porogarama bibanda ku bumenyi bw’abakoresha n’ubuhinga bwo gukora ubucuruzi. Urufunguruzo ruri mu gutahura neza ivyo bihuza no gufata ingingo zishingiye ku makuru zishingiye ku bisabwa vy’ikoreshwa ry’ibintu vyihariye be n’ingero zo kwihanganira ingorane.




# Igice ca nyuma

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Amasuzuma n'Ibipimo

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Iciyumviro

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>