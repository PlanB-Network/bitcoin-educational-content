---
name: Kujifunza Rust na Bitcoin
goal: Boresha ujuzi wako wa ukuzaji wa Rust kupitia msimbo wa Bitcoin
objectives: 

  - Jizoeze Lugha ya Rust
  - Elewa kwa nini utumie Rust katika kutengeneza Bitcoin
  - Pata msingi wa Lightning SDK

---

# Safari ya Rust kwa Wajenzi wa Bitcoin



Katika kozi hii ya vitendo, ambayo ilirekodiwa wakati wa semina iliyoandaliwa na Fulgur' Ventures mnamo Oktoba 2023, utaendeleza ujuzi wako wa Rust kwa kujenga vipengele na miradi midogo inayolenga Bitcoin. Tutaangazia misingi ya Rust, kwa nini Rust inatumika kwa ajili ya ukuzaji wa Bitcoin (usalama wa kumbukumbu, utendaji, na upatanifu salama), na jinsi ya kuanza na Lightning SDK ili kujenga vipengele vya malipo.


Katika sura zote, utafanya mazoezi ya mifumo ya msingi ya Rust (umiliki, maisha, sifa, async), utafanya kazi na vitu vya awali vya Bitcoin (funguo, miamala, hati), na ujumuishe dhana za Umeme hatua kwa hatua (nodi, njia, ankara).


Hakuna uundaji wa awali wa Rust au Bitcoin unaohitajika sana, ingawa ujuzi wa programu za msingi husaidia. Kozi hii ni rafiki kwa wanaoanza lakini inafaa vya kutosha kwa wahandisi wanaoingia Bitcoin.


+++

# Utangulizi

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Muhtasari wa kozi

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Utangulizi**


Karibu kwenye kozi hii ya programu rafiki kwa wanaoanza kwenye SDK. Katika mafunzo haya, utajifunza misingi ya Rust, kisha uzingatia Rust inayotumika kwenye programu ya Bitcoin, na umalizie na baadhi ya matumizi kwa kutumia SDK.


Video za mafunzo hayo zitapatikana kwa Kiingereza pekee kwa sasa na zilikuwa sehemu ya semina ya moja kwa moja iliyoandaliwa Oktoba iliyopita huko Tuscany na Fulgure Venture. Mafunzo haya yatalenga wiki ya kwanza pekee. Kipindi cha pili kililenga RGB na kinaweza kupatikana katika kozi ya RGB.


https://planb.academy/en/courses/rgb-programming-3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Mafunzo haya yanakupa fursa ya kukuza ujuzi wako wa programu kwenye Lightning Network kwa kutumia Rust na SDK mbalimbali. Yameundwa kwa ajili ya watengenezaji programu wenye ujuzi mzuri wa programu ambao wanataka kujifunza zaidi kuhusu uundaji mahususi wa Lightning Network. Utajifunza misingi ya Rust, kwa nini inafaa kwa uundaji wa Bitcoin, na kisha kuendelea na utekelezaji wa vitendo kwa kutumia SDK maalum.


**Sehemu ya 2: Jifunze kuandika msimbo kwa kutumia Rust**

Katika sehemu hii, utagundua misingi ya Rust kupitia mfululizo wa sura zinazoendelea. Utajifunza kuandika msimbo wa Rust, kuelewa umahususi wake, na kufahamu vipengele vyake muhimu katika sehemu saba zilizo na maelezo. Moduli hii ni muhimu kuelewa kwa nini Rust ni lugha inayopendelewa kwa ajili ya uundaji wa Bitcoin.


**Sehemu ya 3: Rust na Bitcoin**

Hapa, tutachunguza kwa undani kwa nini Rust ni chaguo linalofaa kwa ajili ya uundaji wa Bitcoin. Utajifunza kuhusu mfumo wake wa hitilafu, zana ya UniFFI, na sifa zisizolingana - vyote ni vipengele muhimu katika kujenga programu imara na salama.


**Sehemu ya 4: Uundaji wa LNP/BP kwa kutumia SDK**

Utajifunza jinsi ya kutengeneza nodi za LN kwa kutumia SDK mbalimbali kama vile Breez SDK na Greenlight kwa Lipa. Utaona jinsi ya kutekeleza programu za Lightning Network kwa kutumia maktaba zilizoundwa ili kurahisisha uundaji wa Bitcoin na Lightning.


Uko tayari kukuza ujuzi wako wa Lightning Network ukitumia Rust? Twende!

# Jifunze jinsi ya kuandika msimbo kwa kutumia kitabu cha kutu

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Utangulizi wa Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Kusakinisha na Kusimamia Rust kwa kutumia Rustup


Unapoanza safari yako na Rust, hatua ya kwanza inahusisha kuweka mazingira sahihi ya maendeleo. Mbinu inayopendekezwa zaidi ya kusakinisha Rust ni kupitia Rustup, mfumo wa usimamizi wa mnyororo wa zana unaoshughulikia usakinishaji na masasisho katika miradi na majukwaa tofauti.


Rustup hutumika kama zaidi ya kisakinishi tu—inafanya kazi kama zana kamili ya usimamizi kwa mazingira yako ya uundaji wa Rust. Ukiwa na Rustup, unaweza kusakinisha kwa urahisi malengo ya ziada ya mkusanyiko kwa mifumo tofauti, kama vile ARM64 kwa uundaji wa Android au usanifu mwingine ambao unaweza kuhitaji kuuunga mkono. Zana hii pia hushughulikia masasisho ya Rust bila shida, ambayo ni muhimu sana ikizingatiwa kwamba Rust hutoa toleo jipya thabiti takriban kila baada ya wiki sita. Unapohitaji kusasisha hadi toleo jipya zaidi, amri rahisi ya 'rustup update' hushughulikia kila kitu kiotomatiki.


Wakati wa kusakinisha Rustup, inafaa kuelewa mfumo wa usalama unaohusika. Mchakato wa usakinishaji hupakua na kutekeleza hati kutoka kwa tovuti rasmi ya Rust kupitia HTTPS, ambayo hutoa usalama wa kriptografia ya safu ya usafiri. Vifurushi vilivyopakuliwa na Rustup na Cargo vinatoka kwa vyanzo vinavyoaminika (crates.io na miundombinu rasmi ya Rust) na hufaidika na usimbaji fiche wa HTTPS. Ingawa mbinu hii ni salama kwa hali nyingi za uundaji, baadhi ya mashirika yenye sera kali za usalama yanaweza kupendelea kusakinisha Rust kupitia meneja wa vifurushi vya usambazaji wa Linux, ambavyo hutoa safu ya ziada ya uaminifu kupitia miundombinu ya utiaji saini wa vifurushi vya usambazaji. Kwa madhumuni ya kujifunza na maendeleo ya jumla, Rustup ni zana iliyoanzishwa vizuri na inayoaminika sana katika mfumo ikolojia wa Rust.


Kwa hali nyingi za usanidi, unaweza kusakinisha Rustup kwa kuendesha hati ya usakinishaji iliyotolewa kwenye tovuti rasmi ya Rust. Kisakinishi kitakuomba uchague kati ya chaguo tofauti za mnyororo wa zana, huku mnyororo thabiti wa zana ukiwa chaguo linalopendekezwa kwa watumiaji wengi. Usakinishaji hutokea kwenye saraka yako ya nyumbani, bila kuhitaji marupurupu ya msimamizi, na huweka vigezo vyote muhimu vya mazingira kwa matumizi ya haraka.


### Kuelewa Minyororo na Vipengele vya Rust


Mfumo ikolojia wa uundaji wa Rust una vipengele kadhaa muhimu vinavyofanya kazi pamoja ili kutoa mazingira kamili ya upangaji programu. Kuelewa vipengele hivi hukusaidia kupitia mchakato wa uundaji wa Rust kwa ufanisi zaidi na kutatua matatizo yanapojitokeza.


Kikusanyaji cha Rust, kinachojulikana kama `rustc`, huunda kiini cha mnyororo wa zana wa Rust. Ingawa unaweza kutumia kinadharia `rustc` moja kwa moja kukusanya programu za Rust, kazi nyingi za uundaji hutegemea Cargo, meneja wa kifurushi cha Rust na mfumo wa ujenzi. Cargo hufanya kazi sawa na npm katika mfumo ikolojia wa JavaScript, kudhibiti utegemezi, kuratibu ujenzi, na kutoa amri rahisi kwa kazi za kawaida za uundaji. Unapoendesha amri kama `cargo build` au `cargo run`, Cargo hupanga mchakato wa ujumuishaji, hushughulikia utatuzi wa utegemezi, na husimamia muundo mzima wa mradi.


Clippy ni mhariri anayechambua msimbo wako na kutoa mapendekezo ya maboresho. Tofauti na vikaguzi vya sintaksia vya msingi, Clippy anaelewa nahau za Rust na anaweza kupendekeza njia zaidi za nahau za kukamilisha kazi maalum. Zana hii husaidia katika kujifunza mbinu bora za Rust na kuandika msimbo unaoweza kudumishwa zaidi.


Msururu wa zana wa Rust pia unajumuisha zana kamili za uandishi wa nyaraka na nyaraka za kawaida za maktaba, zinazopatikana kupitia tovuti rasmi ya uandishi wa nyaraka wa Rust. Nyaraka hizi hutumika kama marejeleo muhimu wakati wa uundaji, zikitoa taarifa za kina kuhusu kazi za kawaida za maktaba, aina, na moduli. Nyaraka hizo zinajumuisha mifano na maelezo mengi yanayokusaidia kuelewa si tu kazi zinafanya nini, bali jinsi ya kuzitumia kwa ufanisi katika programu zako.


Rust inasaidia njia nyingi za kutolewa: thabiti, beta, na kila usiku. Njia thabiti hutoa matoleo yaliyojaribiwa vizuri yanayofaa kwa matumizi ya uzalishaji. Njia ya beta inatoa hakikisho la toleo linalofuata thabiti, linalotumika hasa kwa majaribio ya mwisho kabla ya kutolewa rasmi. Njia ya usiku inajumuisha vipengele vya majaribio vilivyo chini ya uundaji amilifu, ambavyo vinaweza kuwa muhimu kwa kujaribu uwezo mpya wa Rust, ingawa vipengele hivi vinaweza kubadilika au kuondolewa katika matoleo yajayo.


### Kuunda na Kusimamia Miradi ya Rust kwa Kutumia Mizigo


Uundaji wa kisasa wa Rust unazingatia Cargo, ambayo hurahisisha uundaji wa miradi, usimamizi wa utegemezi, na mchakato wa ujenzi. Badala ya kuunda saraka na faili mwenyewe, Cargo hutoa amri ya `mzigo mpya` kwa generate muundo kamili wa mradi wenye chaguo-msingi zinazofaa.


Unapounda mradi mpya kwa kutumia `cargo new project_name`, Cargo huanzisha muundo sanifu wa saraka, huunda faili ya msingi ya `main.rs` yenye programu ya "Hello, world!", huanzisha hazina ya Git, na hutoa faili ya `Cargo.toml` kwa ajili ya usanidi wa mradi. Faili ya `Cargo.toml` hutumika kama sehemu kuu ya usanidi wa mradi wako, ikiwa na metadata kuhusu mradi wako na kuorodhesha vitegemezi vyote ambavyo msimbo wako unahitaji.


Cargo hutoa amri kadhaa muhimu kwa kazi ya uundaji wa kila siku. Amri ya `cargo build` hukusanya mradi wako na utegemezi wake, na kuunda faili zinazoweza kutekelezwa katika saraka ya `target`. Kwa uundaji wa haraka wakati wa uundaji, `cargo run` huchanganya ujenzi na utekelezaji katika hatua moja. Amri ya `cargo check` hufanya ukaguzi wote wa mkusanyiko bila kutoa utekelezaji wa mwisho, na kuifanya iwe haraka zaidi kuliko ujenzi kamili unapotaka tu kuthibitisha kwamba msimbo wako unakusanywa kwa usahihi.


Wakati wa kuandaa msimbo kwa ajili ya utumaji wa uzalishaji, bendera ya `--release` huwezesha uboreshaji na kuondoa madai ya utatuzi. Miundo ya utoaji huendeshwa kwa kasi zaidi na hutoa vitendakazi vidogo vinavyoweza kutekelezwa, lakini huchukua muda mrefu kukusanya na kuondoa taarifa muhimu za utatuzi. Kikusanyaji hutumia uboreshaji mbalimbali wakati wa miundo ya utoaji na huzima ukaguzi wa muda wa utekelezaji kama vile ugunduzi wa kufurika kwa nambari kamili, ambao huboresha utendaji lakini huondoa baadhi ya dhamana za usalama zilizopo katika miundo ya utatuzi.


### Vigezo, Ubadilikaji, na Falsafa ya Usalama ya Rust


Rust inachukua mbinu tofauti ya usimamizi wa vigeugeu kuliko lugha nyingi. Kwa chaguo-msingi, vigeugeu vyote katika Rust havibadiliki, ikimaanisha kuwa thamani zao haziwezi kubadilishwa baada ya mgawo wa awali. Uamuzi huu wa muundo unalenga kuzuia makosa ya kawaida ya programu yanayotokana na mabadiliko yasiyotarajiwa ya hali.


Unapotangaza kigezo kwa kutumia `let x = 5`, kigezo hicho huwa hakibadiliki kwa chaguo-msingi. Jaribio lolote la kurekebisha thamani yake baadaye litasababisha hitilafu ya mkusanyiko. Sharti hili la kutobadilika huwalazimisha wasanidi programu kufikiria kwa makini kuhusu wakati mabadiliko ya hali yanahitajika kweli na hufanya tabia ya msimbo iweze kutabirika zaidi. Hitilafu nyingi za programu hutokana na vigezo vinavyobadilika bila kutarajia, na kutobadilika kwa chaguo-msingi kwa Rust husaidia kuzuia matatizo haya.


Unapohitaji kweli kurekebisha thamani ya kigezo, Rust inahitaji tamko dhahiri la ubadilikaji kwa kutumia neno muhimu la `mut`: `let mut x = 5`. Tamko hili dhahiri hutumika kama ishara wazi kwa mkusanyaji na wasanidi programu wengine kwamba thamani ya kigezo hiki inaweza kubadilika wakati wa utekelezaji wa programu. Sharti la kutangaza ubadilikaji waziwazi linahimiza kuzingatia kwa makini kama ubadilikaji ni muhimu kwa kila kigezo.


Rust pia inasaidia uvuli, ambayo hukuruhusu kutangaza kigezo kipya chenye jina sawa na kigezo kilichopita. Tofauti na mabadiliko, uvuli huunda kigezo kipya kabisa ambacho kina jina sawa, na kuficha kigezo kilichopita kwa ufanisi. Mbinu hii inathibitika kuwa muhimu sana wakati wa kubadilisha data kupitia hatua nyingi, kama vile kuchanganua mfuatano kuwa nambari na kisha kusindika nambari hiyo zaidi. Kwa uvuli, unaweza kudumisha jina la kigezo thabiti katika mchakato mzima wa mabadiliko huku ukibadilisha aina ya kigezo katika kila hatua.


Tofauti kati ya kivuli na mabadiliko inakuwa muhimu wakati wa kuzingatia mabadiliko ya aina. Kwa kivuli, unaweza kubadilisha thamani na aina ya kigezo kwa sababu unaunda kigezo kipya. Kwa mabadiliko, unaweza kubadilisha thamani tu huku ukidumisha aina ile ile, kwa kuwa unabadilisha kigezo kilichopo badala ya kuunda kipya.


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


### Aina za Data na Aina Misingi ya Mfumo


Rust hutekeleza mfumo imara na tuli wa aina ambapo kila thamani lazima iwe na aina iliyofafanuliwa vizuri inayojulikana wakati wa kukusanya. Ingawa hii inaweza kuonekana kuwa na vikwazo ikilinganishwa na lugha zilizoandikwa kwa njia inayobadilika, uwezo wa kukisia aina wa Rust unamaanisha kuwa mara chache huhitaji kutaja aina waziwazi. Kikusanyaji kwa kawaida kinaweza kubaini aina inayofaa kulingana na jinsi unavyotumia thamani hiyo.


Hata hivyo, hali fulani zinahitaji maelezo ya aina dhahiri. Unapotumia vitendakazi vya jumla kama vile `parse()`, ambavyo vinaweza kubadilisha mifuatano kuwa aina mbalimbali za nambari, mkusanyaji anahitaji kujua ni aina gani maalum unayotaka. Katika hali hizi, unatoa maelezo ya aina kwa kutumia sintaksia ya koloni: `hebu nadhani: u32 = "42".parse().expect("Sio nambari!")`.


Aina za skala za Rust zinajumuisha nambari kamili, nambari za nukta zinazoelea, boolean, na herufi. Mfumo wa aina kamili hutoa udhibiti sahihi juu ya matumizi ya kumbukumbu na sifa za utendaji. Aina kamili hupewa majina kimfumo: `i8`, `i16`, `i32`, `i64`, na `i128` kwa nambari kamili zilizosainiwa, na `u8`, `u16`, `u32`, `u64`, na `u128` kwa nambari kamili ambazo hazijasainiwa. Nambari zinaonyesha upana wa biti, na kufanya matumizi ya kumbukumbu na safu za thamani kuwa wazi mara moja.


Aina za `isize` na `usize` zinastahili kupewa kipaumbele maalum zinapozoea usanifu lengwa wako. Kwenye mifumo ya biti 64, aina hizi zina upana wa biti 64, huku kwenye mifumo ya biti 32, zina upana wa biti 32. Aina hizi hutumika kwa kawaida kwa uorodheshaji wa safu na marekebisho ya kumbukumbu kwa sababu zinalingana na ukubwa wa asili wa neno la usanifu lengwa, na kuwezesha hesabu bora za kielekezi na shughuli za kumbukumbu.


Rust hutoa njia nyingi za kuandika nambari halisi nambari, ikiwa ni pamoja na umbizo la desimali, heksadesimali (`0x`), oktali (`0o`), na muundo wa binary (`0b`). Unaweza pia kutumia alama za chini popote ndani ya nambari halisi nambari ili kuboresha usomaji, kama vile kuandika `1_000_000` badala ya `1000000`. Nambari hizo za chini hazina athari kwenye thamani lakini zinaweza kufanya nambari kubwa zisomeke zaidi.


Aina za nukta zinazoelea katika Rust ni rahisi: `f32` kwa usahihi mmoja na `f64` kwa nambari za nukta zinazoelea zenye usahihi maradufu. Aina ya `f64` kwa ujumla hupendelewa kutokana na usahihi wake wa juu na ukweli kwamba vichakataji vya kisasa mara nyingi vinaweza kushughulikia shughuli za nukta zinazoelea za biti 64 kwa ufanisi kama shughuli za biti 32.


### Aina za Mchanganyiko na Mpangilio wa Data


Zaidi ya aina za scalar, Rust hutoa aina za kiwanja ambazo huweka thamani nyingi pamoja. Vijiti hukuruhusu kuchanganya thamani za aina tofauti katika thamani moja ya kiwanja. Unaunda vijiti kwa kutumia mabano na unaweza kubainisha aina ya kila kipengele: `let tup: (i32, f64, u8) = (500, 6.4, 1)`.


Vijiti vinaunga mkono uundaji wa muundo, ambao hukuruhusu kutoa thamani za kibinafsi: `let (x, y, z) = tup`. Sintaksia hii huunda vigeu vitatu tofauti kutoka kwa vipengele vya kijiti. Vinginevyo, unaweza kufikia vipengele vya kijiti moja kwa moja kwa kutumia nukuu ya nukta yenye faharasa ya kipengele: `tup.0`, `tup.1`, `tup.2`.


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


Safu katika Rust hutofautiana sana na safu au orodha katika lugha zingine nyingi kwa sababu zina ukubwa usiobadilika ambao unakuwa sehemu ya aina yao. Safu ya nambari tano kamili ina aina ya `[i32; 5]`, ambapo nusukoloni hutenganisha aina ya kipengele na urefu wa safu. Taarifa hii ya ukubwa wa kiwango cha aina huwezesha mkusanyaji kufanya ukaguzi wa mipaka na kuhakikisha kwamba safu zinazopokea kazi zinajua haswa ni vipengele vingapi vya kutarajia.


Unaweza kuanzisha safu kwa kuorodhesha vipengele vyote waziwazi: `[1, 2, 3, 4, 5]`, au kwa kutumia sintaksia ya mkono mfupi kwa safu zenye thamani zinazorudiwa: `[3; 5]` huunda safu ya vipengele vitano, vyote vikiwa na thamani ya 3. Mfupi huu ni muhimu kwa kuanzisha bafa au kuunda safu zenye thamani chaguo-msingi.


Ufikiaji wa safu hutumia nukuu ya mabano ya mraba kama lugha nyingi, lakini Rust hutoa ukaguzi wa mipaka ya muda wa kukusanya na ya muda wa utekelezaji. Unapofikia safu yenye faharasa isiyobadilika ambayo mkusanyaji anaweza kuthibitisha, itakamata ufikiaji wa nje ya mipaka wakati wa kukusanya. Kwa faharasa zinazobadilika zilizobainishwa wakati wa utekelezaji, Rust huingiza ukaguzi wa mipaka ambao utasababisha programu kuingiwa na hofu ikiwa utajaribu kufikia faharasa batili, na kuzuia ukiukaji wa usalama wa kumbukumbu.



## Ownership na Usalama wa Kumbukumbu katika Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Kuelewa Mbinu ya Kipekee ya Rust ya Usimamizi wa Kumbukumbu


Sura hii inashughulikia mojawapo ya dhana muhimu zaidi za Rust. Ingawa dhana za awali zinaweza kuwa zimeeleweka kwa watengenezaji programu kutoka lugha zingine, umiliki ni mbinu ya Rust ya kutatua usalama wa kumbukumbu bila ukusanyaji wa takataka.


Rust iliundwa kwa lengo la msingi la kuzuia hitilafu zinazohusiana na kumbukumbu zinazoathiri lugha za kiwango cha chini kama vile C na C++. Masuala haya ni pamoja na hitilafu zisizotumika baada ya kutolewa, ambapo kumbukumbu hupatikana baada ya kutolewa, na bafa hufurika, ambapo programu huandika nje ya mipaka ya kumbukumbu iliyotengwa. Suluhisho za kitamaduni za matatizo haya zimehusisha maelewano ambayo Rust inatafuta kuondoa. Lugha za kiwango cha juu kama Java na Go hutatua usalama wa kumbukumbu kupitia ukusanyaji wa takataka, ambapo mchakato otomatiki hutambua na kutoa kumbukumbu isiyotumika mara kwa mara. Hata hivyo, wakusanyaji wa taka huanzisha gharama za utendaji na zinaweza kusababisha kusitishwa kusikotabirika wakati wa utekelezaji wa programu, na kuzifanya zisifae kwa programu za mifumo ambapo utendaji thabiti ni muhimu.


Rust inafanikisha usalama wa kumbukumbu hasa kupitia uchanganuzi tuli unaofanywa wakati wa kukusanya. Kikusanyaji huchunguza msimbo chanzo na kinaweza kubaini kama shughuli nyingi za kumbukumbu ni salama bila kuhitaji ukusanyaji wa takataka. Kwa hali ambazo haziwezi kuthibitishwa kitakwimu—kama vile ufikiaji wa safu na fahirisi zilizohesabiwa kwa wakati wa utekelezaji—Rust huingiza mipaka huangalia hofu hiyo badala ya kuruhusu tabia isiyofafanuliwa. Mbinu hii inatofautiana kimsingi na vichanganuzi tuli vinavyopatikana kwa C na C++, ambavyo viliwekwa upya kwenye lugha ambazo hazikuundwa awali kwa uchanganuzi kamili tuli. Sheria za sintaksia na lugha za Rust ziliundwa kutoka chini hadi chini ili kuwezesha uthibitishaji mpana wa wakati wa kukusanya, kuhakikisha kwamba mara tu programu inapokusanywa kwa mafanikio, itafanya kazi salama au hofu kwa kutabirika badala ya kuonyesha tabia isiyofafanuliwa.


### Mfumo wa Ownership: Sheria na Kanuni


Msingi wa dhamana za usalama wa kumbukumbu za Rust ni mfumo wa umiliki, ambao husimamia jinsi kumbukumbu inavyosimamiwa katika kipindi chote cha programu ambacho tayari kimesakinishwa. Ownership hufanya kazi kwa sheria tatu za msingi ambazo mkusanyaji hutekeleza wakati wote:


1. Kila thamani katika Rust ina mmiliki (kigezo kinachoshikilia thamani)

2. Kunaweza kuwa na mmiliki mmoja tu kwa wakati mmoja

3. Mmiliki anapopoteza uwezo wake, thamani hupunguzwa


Michoro katika Rust kwa kawaida hufafanuliwa na vibandiko vilivyopinda, iwe katika miili ya utendaji, vizuizi vyenye masharti, au vizuizi vya michoro vilivyoundwa wazi. Wakati kigezo kinatangazwa ndani ya wigo, wigo huo unakuwa mmiliki wa thamani ya kigezo. Kigezo hubaki kupatikana na halali katika maisha yote ya wigo, lakini mara tu utekelezaji unapoondoka kwenye wigo, vigezo vyote vinavyomilikiwa husafishwa kiotomatiki kupitia mchakato unaoitwa kuacha.


Usafi huu otomatiki unatekelezwa kupitia utaratibu wa kushuka wa Rust, ambapo lugha huita kitendakazi cha kushuka kwenye vigeu vinavyotoka nje ya wigo. Kwa aina za msingi, hii ina maana tu kwamba kumbukumbu imewekwa alama kama inapatikana kwa matumizi tena. Kwa aina ngumu zaidi zinazosimamia rasilimali, utekelezaji maalum wa kushuka unaweza kufanya shughuli za ziada za usafi, kama vile kufunga vipini vya faili au kutoa miunganisho ya mtandao. Muundo huu, uliokopwa kutoka kwa RAII ya C++ (Upataji wa Rasilimali Ni Uanzishaji), unahakikisha kwamba rasilimali hutolewa ipasavyo kila wakati bila kuhitaji msimbo dhahiri wa usafi kutoka kwa programu.


### Kuhamisha Ownership na Mpangilio wa Kumbukumbu


Kuelewa jinsi uhamishaji wa umiliki kati ya vigezo kunahitaji kuchunguza tofauti kati ya aina rahisi na aina changamano katika suala la mpangilio wa kumbukumbu na tabia ya kunakili. Aina rahisi kama vile nambari kamili, boolean, na nambari za nukta zinazoelea zina ukubwa usiobadilika na unaojulikana wakati wa kukusanya na zinaweza kunakiliwa kwa ufanisi. Unapogawa kigezo kimoja cha nambari kamili kwa kingine, Rust huunda nakala kamili na huru ya thamani, ikiruhusu vigezo vyote viwili kuwepo kwa wakati mmoja bila wasiwasi wowote wa umiliki.


Aina tata kama vile nyuzi hutoa changamoto tofauti kwa sababu husimamia kumbukumbu iliyotengwa kwa njia inayobadilika. Kamba katika Rust ina vipengele vitatu vilivyohifadhiwa kwenye rundo: kielekezi cha data ya herufi zilizotengwa kwa rundo, urefu wa sasa wa kamba, na uwezo wa jumla wa bafa iliyotengwa. Muundo huu huruhusu nyuzi kukua na kupungua kwa ufanisi huku ukidumisha ujuzi wa mipaka yao. Unapogawa kigezo kimoja cha Kamba kwa kingine, Rust inakabiliwa na chaguo: inaweza kunakili muundo unaotegemea rundo tu (kuunda vielekezi viwili kwa data sawa ya rundo) au kufanya nakala ya kina ya data yote ya rundo.


Tabia chaguo-msingi ya Rust ni kuhamisha umiliki badala ya kunakili, kuhamisha data ya chungu kutoka kwa kigezo cha chanzo hadi kigezo cha mwisho na kuibatilisha chanzo. Mbinu hii huzuia hali hatari ambapo vigeu vingi vinaweza kurekebisha kumbukumbu sawa ya chungu au ambapo kumbukumbu sawa inaweza kutolewa mara nyingi wakati vigeu vinapotoka. Uendeshaji wa kuhamisha ni mzuri kwa sababu hunakili tu muundo mdogo unaotegemea chungu, sio data inayoweza kuwa kubwa ya chungu, huku ikidumisha usalama wa kumbukumbu kwa kuhakikisha umiliki mmoja.


### Marejeleo na Kukopa


Ingawa hatua za umiliki hutoa usalama, zinaweza kuwa na vikwazo unapohitaji kutumia thamani katika sehemu nyingi bila kuhamisha umiliki. Rust hushughulikia hili kupitia kukopa, ambayo inaruhusu vitendakazi na vigeu kufikia data kwa muda bila kuchukua umiliki. Marejeleo, yaliyoundwa kwa kutumia opereta wa ampersand, hutoa ufikiaji wa kusoma tu kwa thamani huku ikiacha umiliki na kigezo asili.


Marejeleo huwezesha vitendakazi kufanya kazi kwenye data bila kuitumia, na hivyo kuwezesha kutumia thamani sawa mara nyingi katika programu nzima. Unapopitisha marejeleo kwenye kitendakazi, unaikopesha data kwa muda, na kitendakazi lazima kirudishe marejeleo kabla mmiliki wa asili hajaweza kupata udhibiti kamili. Mfano huu wa kukopa unaonyesha hali ya muda ya ufikiaji: kama vile unavyoweza kuazima kitabu kwa rafiki huku ukihifadhi umiliki, marejeleo huruhusu ufikiaji wa muda huku ukihifadhi uhusiano wa awali wa umiliki.


Marejeleo yanayoweza kubadilishwa hupanua dhana hii ili kuruhusu urekebishaji wa data iliyokopwa, lakini kwa vikwazo vikali ili kudumisha usalama. Rust inaruhusu marejeleo moja tu yanayoweza kubadilishwa kwa kipande cha data wakati wowote, kuzuia mbio za data ambapo sehemu nyingi za programu zinaweza kurekebisha kumbukumbu sawa kwa wakati mmoja. Zaidi ya hayo, huwezi kuwa na marejeleo yanayoweza kubadilishwa na yasiyoweza kubadilishwa kwa data sawa kwa wakati mmoja, kwani hii inaweza kusababisha hali ambapo msimbo unadhani data ni thabiti huku msimbo mwingine ukiibadilisha kikamilifu. Sheria hizi zinatekelezwa wakati wa kukusanya, na kuondoa madarasa yote ya hitilafu za sarafu zinazoathiri lugha zingine za programu za mifumo.


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


### Aina za Kamba na Vipande


Rust hutofautisha kati ya herufi halisi za mfuatano na aina ya String, ikiakisi mikakati tofauti ya usimamizi wa kumbukumbu na matumizi. Herufi halisi za mfuatano zimepachikwa moja kwa moja kwenye jozi iliyokusanywa na zina aina ya &str (kipande cha mfuatano), inayowakilisha mwonekano katika data ya mfuatano isiyobadilika. Herufi hizi halisi zinafaa kwa sababu hazihitaji mgao wa muda wa utekelezaji, lakini haziwezi kurekebishwa kwa kuwa ni sehemu ya msimbo wa programu.


Aina ya String, kwa upande mwingine, hudhibiti kumbukumbu iliyotengwa kwa njia inayobadilika na inaweza kukua, kupunguzwa, na kurekebishwa wakati wa utekelezaji. Unaweza kuunda String kutoka kwa njia halisi kwa kutumia String::from() au mbinu zinazofanana, ambazo hutenga kumbukumbu ya heap na kunakili maudhui ya halisi. Tofauti hii inaruhusu Rust kuboresha utendaji (kwa kutumia maandishi halisi inapowezekana) na kubadilika (kwa kutumia String wakati marekebisho yanahitajika).


Vipande vya kamba (&str) hutoa ufupisho wenye nguvu wa kufanya kazi na sehemu za nyuzi bila kunakili data. Kipande kina kiashiria cha mwanzo wa data ya nyuzi na urefu, kinachokuruhusu kurejelea nyuzi ndogo kwa ufanisi. Sintaksia ya vipande hutumia masafa (k.m., &s[0..5]) kubainisha sehemu gani ya nyuzi ya kurejelea. Kwa sababu vipande ni marejeleo, vinakabiliwa na sheria za kukopa, kuzuia nyuzi msingi kurekebishwa wakati vipande vipo. Utekelezaji huu wa wakati wa kukusanya huzuia hitilafu za kawaida kama vile kufikia kumbukumbu batili baada ya nyuzi asili kutolewa au kurekebishwa.


### Safu, Vekta, na Vipande vya Jumla


Wazo la kipande linaenea zaidi ya nyuzi hadi kwenye mfuatano wowote wa vipengele, na kutoa njia moja ya kufanya kazi na safu za ukubwa usiobadilika na vekta zinazobadilika. Safu katika Rust zina urefu wake uliosimbwa katika aina yake (k.m., [i32; 5] kwa safu ya nambari tano za biti 32, na kuzifanya zifae kwa hali zinazohitaji dhamana ya ukubwa wa muda wa kukusanya. Kazi zinazokubali safu zinaweza kutekeleza mahitaji halisi ya urefu, muhimu kwa shughuli kama kazi za kriptografia zinazohitaji ingizo la ukubwa halisi.


Vipande (&[T]) hutoa mbadala unaonyumbulika zaidi, unaowakilisha mwonekano katika mfuatano wowote wa vipengele vilivyounganishwa bila kujali hifadhi ya msingi. Unaweza kuunda vipande kutoka kwa safu, vekta, au vipande vingine, na kipande hicho hicho kinaweza kurejelea sehemu tofauti za data katika maisha yake yote. Unyumbulifu huu hufanya vipande kuwa bora kwa kazi zinazohitaji kuchakata mfuatano bila kujali utaratibu maalum wa kuhifadhi au ukubwa halisi.


Uhusiano kati ya aina zinazomilikiwa (String, Vec<T>) na wenzao wa vipande vilivyokopwa (&str, &[T]) hufuata muundo thabiti katika Rust yote. Aina zinazomilikiwa hudhibiti kumbukumbu zao na zinaweza kurekebishwa, huku vipande vikitoa ufikiaji mzuri na wa kusoma pekee wa sehemu za data hiyo. Muundo huu huwezesha API ambazo zinaweza kunyumbulika (kukubali aina mbalimbali za ingizo kupitia vipande) na zenye ufanisi (kuepuka kunakili bila lazima), huku zikidumisha dhamana za usalama za Rust kupitia mfumo wa kukopa.



## Miundo, Aina za Data Changamano za Jengo

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Miundo katika Rust hutumika kama msingi wa kuunda aina changamano za data, sawa na madarasa katika lugha zingine za programu. Hukuruhusu kuunganisha data zinazohusiana pamoja katika kitengo kimoja, chenye mshikamano ambacho kinaweza kuwa na sehemu nyingi za aina tofauti. Sintaksia ya kufafanua muundo hufuata muundo ulio wazi: unatumia neno muhimu la `struct` ikifuatiwa na jina la muundo, kisha fafanua sehemu zilizo ndani ya vibano vilivyopinda kwa kutumia sintaksia ya koloni ili kubainisha aina ya kila sehemu.


Rust hufuata kanuni maalum za majina ya miundo ambazo mkusanyaji atatekeleza kupitia maonyo. Majina ya miundo yanapaswa kutumia CamelCase (pia inajulikana kama PascalCase), huku majina ya sehemu ndani ya muundo yanapaswa kutumia snake_case yenye mistari ya chini. Kanuni hii husaidia kudumisha uthabiti katika besi za msimbo za Rust na kufanya msimbo usomeke zaidi kwa wasanidi programu wengine.


Kuunda mifano ya miundo kunahitaji kubainisha thamani za sehemu zote kwa kutumia jina la muundo likifuatiwa na vibandiko vilivyopinda vyenye mgawo wa sehemu. Ukishakuwa na mfano wa muundo, unaweza kufikia na kurekebisha sehemu za kibinafsi kwa kutumia nukuu ya nukta, mradi mfano huo umetangazwa kuwa unaoweza kubadilika. Nukuu hii ya nukta hufanya kazi kwa uthabiti katika Rust, tofauti na lugha kama C++ ambapo unaweza kutumia waendeshaji tofauti kwa viashiria dhidi ya vitu vya moja kwa moja.


### Kazi za Mjenzi na Njia za Mkato za Sehemu


Rust haina wajenzi waliojengewa ndani kama lugha zingine zinazolenga vitu, lakini unaweza kuunda vitendaji vinavyorudisha mifano ya muundo ili kutumikia kusudi moja. Vitendaji hivi vya wajenzi kwa kawaida huchukua vigezo kwa baadhi au sehemu zote na vinaweza kuweka thamani chaguo-msingi kwa zingine. Wakati wa kuandika vitendaji kama hivyo, Rust hutoa mkato unaofaa: ikiwa kigezo kina jina sawa na sehemu ya muundo, unaweza kuandika jina la sehemu mara moja badala ya kulirudia katika umbizo la `sehemu: thamani`.


Mifano ya muundo pia inaweza kuundwa kwa kunakili thamani kutoka kwa mifano iliyopo kwa kutumia sintaksia ya sasisho la muundo. Kipengele hiki hukuruhusu kuunda mfano mpya huku ukibainisha sehemu unazotaka kubadilisha pekee, huku sehemu zingine zote zikinakiliwa kutoka kwa mfano uliopo. Hata hivyo, operesheni hii inafuata sheria za umiliki za Rust, ambayo ina maana kwamba aina zisizo za Nakala zitahamishwa kutoka kwa mfano chanzo, na hivyo kufanya sehemu za mfano asili zisiweze kutumika baadaye. Kikusanyaji hufuatilia hatua hizi zisizo kamili kwa busara, na kukuruhusu kuendelea kutumia sehemu ambazo hazikuhamishwa huku zikizuia ufikiaji wa sehemu zilizohamishwa.


### Miundo ya Tuple na Miundo ya Vitengo


Rust inasaidia miundo ya tuple, ambayo ni miundo yenye sehemu zisizo na majina zinazofikiwa kwa faharasa badala ya jina. Hizi ni muhimu kwa aina rahisi za vifungashio au unapohitaji muundo lakini hazihitaji sehemu zilizopewa majina. Unafikia sehemu za muundo wa tuple kwa kutumia nukuu ya nukta ikifuatiwa na faharasa ya sehemu, kama vile `.0` kwa sehemu ya kwanza, `.1` kwa sehemu ya pili, na kadhalika. Mbinu hii inafanya kazi vizuri kwa miundo inayofunga thamani moja au yenye thamani chache zinazohusiana kwa karibu ambapo majina yanaweza kuwa yasiyo ya lazima.


Miundo ya vitengo inawakilisha umbo rahisi zaidi la miundo—haina data kabisa. Ingawa hii inaweza kuonekana haina maana mwanzoni, miundo ya vitengo inakuwa na thamani inapofanya kazi na mfumo wa sifa wa Rust, kwani inaweza kutekeleza tabia bila kuhifadhi data yoyote. Miundo hii tupu hutumika kama alama au vishikilia nafasi katika ruwaza za Rust zilizoendelea zaidi.


### Mbinu na Kazi Zinazohusiana


Miundo hupata utendaji kazi wa ziada unapoongeza tabia kupitia vizuizi vya utekelezaji. Kwa kutumia neno muhimu la `impl` linalofuatwa na jina la muundo, unaweza kufafanua mbinu zinazofanya kazi katika mifano ya muundo wako. Mbinu ni kazi zinazochukua `self` kama kigezo chao cha kwanza, ambacho kinaweza kuwa thamani inayomilikiwa (`self`), marejeleo yasiyobadilika (`&self`), au marejeleo yanayoweza kubadilika (`&mut self`), kulingana na kile mbinu inahitaji kufanya na mfano huo.


Chaguo la aina ya vigezo vya `self` huamua tabia ya mbinu kuhusu umiliki. Mbinu za kuchukua `&self` zinaweza kusoma kutoka kwa mfano bila kuchukua umiliki, na kuzifanya zifae kwa shughuli ambazo hazibadilishi muundo. Mbinu za kuchukua `&mut self` zinaweza kurekebisha mfano huku zikimruhusu mpigaji kudumisha umiliki. Mbinu za kuchukua `self` kwa thamani hutumia mfano, ambao unafaa kwa shughuli zinazobadilisha muundo kuwa kitu kingine au wakati mbinu inawakilisha operesheni ya mwisho kwenye mfano huo.


Kazi zinazohusiana ni kazi zinazofafanuliwa ndani ya kizuizi cha utekelezaji ambacho hakichukui `self` kama kigezo. Hizi ni sawa na mbinu tuli katika lugha zingine na hutumika sana kama wajenzi au kazi za matumizi zinazohusiana na aina. Unaita kazi zinazohusiana kwa kutumia sintaksia ya koloni mbili (`Aina::jina_la_kazi()`), ambayo huzitofautisha waziwazi na mbinu zinazoitwa kwenye mifano.


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


#### Hesabu: Chaguo za Uundaji wa Mifano na Tofauti


Hesabu katika Rust zina uwezo zaidi kuliko enum katika lugha zingine nyingi. Ingawa zinaweza kuwakilisha seti rahisi za vigeu vilivyopewa majina, enum za Rust pia zinaweza kubeba data ndani ya kila lahaja, na kuzifanya zifae kwa hali za uundaji ambapo thamani inaweza kuwa moja ya aina au hali kadhaa tofauti. Kila lahaja ya enum inaweza kuwa na aina na kiasi tofauti cha data, kuanzia kutokuwa na data kabisa hadi miundo changamano yenye sehemu zilizopewa majina.


Uwezo wa kuunganisha data kwenye vibadala vya enum huondoa makosa mengi ya kawaida ya programu yanayopatikana katika lugha zingine. Badala ya kudumisha vigeu tofauti kwa kiashiria cha aina na data inayohusiana—ambayo inaweza kuwa isiyolingana kwa urahisi—enum za Rust huunganisha taarifa za aina na data yenyewe. Muundo huu unahakikisha kwamba data inalingana na kigeu kila wakati, na kuzuia kutolingana ambako kunaweza kusababisha makosa ya wakati wa utekelezaji.


Lahaja za Enum zinaweza kuwa na data katika aina kadhaa: hakuna data ya bendera rahisi, data inayofanana na tuple kwa sehemu zisizo na majina, au data inayofanana na muundo na sehemu zilizotajwa. Unaweza hata kuchanganya mitindo hii ndani ya enum moja, ukichagua umbo linalofaa zaidi kwa kila aina. Unyumbulifu huu hufanya enum zifae kwa ajili ya kuunda dhana changamano za kikoa ambapo kesi tofauti zinahitaji taarifa tofauti.


#### Aina ya Chaguo: Kushughulikia Kutokuwepo kwa Usalama


Mojawapo ya enum muhimu zaidi za Rust ni `Option<T>`, ambayo inawakilisha thamani ambazo zinaweza kuwepo au zisipo. Enum hii ina aina mbili: `Some(T)` yenye thamani ya aina ya T, na `None` inayowakilisha kutokuwepo kwa thamani. Aina ya Chaguo hutumika kama suluhisho la Rust kwa matatizo ya null pointer ambayo yanasumbua lugha zingine nyingi, na kulazimisha wasanidi programu kushughulikia waziwazi kesi ambapo thamani zinaweza kukosekana.


Kutumia aina za Chaguo hufanya msimbo wako kuwa imara zaidi kwa sababu mkusanyaji anakuhitaji kushughulikia uwepo na kutokuwepo kwa thamani. Huwezi kutumia kwa bahati mbaya thamani ambayo inaweza kukosa bila kuangalia kwanza kama ipo. Ushughulikiaji huu dhahiri huzuia vighairi vya null pointer na makosa kama hayo ya wakati wa utekelezaji ambayo ni vyanzo vya kawaida vya hitilafu katika lugha zingine za programu.


Aina ya Chaguo huunganishwa na mfumo wa kulinganisha ruwaza wa Rust, na kukuruhusu kushughulikia visa vyote viwili. Mbinu kama `unwrap_or()` hutoa njia rahisi za kutoa thamani zenye chaguo-msingi za kurudi nyuma, huku mbinu kama `map()` na `and_then()` zikiwezesha ruwaza za programu zinazofanya kazi kwa kufanya kazi na thamani za hiari.


### Ulinganishaji wa Mifumo na Misemo Inayolingana


Ulinganishaji wa ruwaza kupitia misemo ya `match` hutoa njia ya kufanya kazi na enums na aina zingine za data. Usemi wa match huchunguza thamani na kutekeleza msimbo tofauti kulingana na muundo ambao thamani inalingana. Kila ruwaza inaweza kuharibu muundo wa thamani inayolingana, ikiunganisha sehemu zake na vigeu vinavyoweza kutumika katika kizuizi cha msimbo kinacholingana.


Misemo ya ulinganishaji lazima iwe kamili, ikimaanisha lazima ishughulikie kila kesi inayowezekana kwa aina inayolinganishwa. Sharti hili huzuia hitilafu ambazo zinaweza kutokea ikiwa kesi fulani zingeachwa bila kushughulikiwa kwa bahati mbaya. Usipotaka kushughulikia kila kesi waziwazi, unaweza kutumia muundo wa wildcard (`_`) kukamata kesi zote zilizobaki, au kufunga kesi ambazo hazijashughulikiwa kwenye kigezo ikiwa unahitaji ufikiaji wa thamani.


Muundo wa `ikiwa let` hutoa njia mbadala iliyofupishwa zaidi ya kulinganisha unapojali tu muundo mmoja maalum. Sintaksia hii ni muhimu sana unapofanya kazi na aina za Chaguo au unapotaka kutekeleza msimbo tu ikiwa thamani inalingana na lahaja fulani ya enum. Muundo wa `ikiwa let` unaweza kujumuisha kifungu cha `else` kwa hali ambapo muundo haulingani, na kuifanya kuwa njia rahisi ya kushughulikia hali rahisi za kulinganisha muundo.


#### Mikusanyiko: Kusimamia Vikundi vya Data


Maktaba ya kawaida ya Rust hutoa aina kadhaa za ukusanyaji kwa ajili ya kudhibiti makundi ya data zinazohusiana. Makusanyo haya ni ya jumla, ikimaanisha kuwa yanaweza kuhifadhi vipengele vya aina yoyote, na hushughulikia usimamizi wa kumbukumbu kiotomatiki. Makusanyo yanayotumika sana ni vekta kwa orodha zilizopangwa, ramani za hash kwa miunganisho ya thamani muhimu, na mifuatano ya data ya maandishi.


#### Vekta: Safu Zinazobadilika


Vekta zinawakilisha safu zinazoweza kupandwa ambazo zinaweza kubadilisha ukubwa wakati wa utekelezaji wa programu. Tofauti na safu za ukubwa usiobadilika, vekta hugawa kumbukumbu kwenye rundo na zinaweza kupanuka au kupungua inapohitajika. Kuunda vekta mara nyingi kunahitaji ufafanuzi wa aina wazi wakati wa kuanza na vekta tupu, kwa kuwa mkusanyaji anahitaji kujua ni aina gani ya vipengele ambavyo vekta itakuwa navyo.


Vekta hutoa njia nyingi za kufikia vipengele, kila moja ikiwa na sifa tofauti za usalama. Nukuu ya faharasa (`vec[0]`) hutoa ufikiaji wa moja kwa moja lakini itaogopa ikiwa faharasa imevuka mipaka. Mbinu ya `get()` hurudisha `Option`, ikikuruhusu kushughulikia ufikiaji wa nje ya mipaka kwa uzuri. Chaguo kati ya mbinu hizi inategemea kama unaweza kuhakikisha faharasa ni halali au unahitaji kushughulikia hitilafu zinazoweza kutokea.


Sheria za kukopa za Rust zinatumika kwa vekta, kuzuia masuala ya kawaida ya usalama wa kumbukumbu. Ukishikilia marejeleo ya kipengele cha vekta, huwezi kurekebisha vekta hadi marejeleo hayo yatoweke. Hii inazuia hali ambapo marejeleo yanaweza kuelekeza kwenye kumbukumbu iliyosambazwa baada ya shughuli za vekta kama vile kusukuma vipengele vipya au kusafisha vekta.


#### Ramani za Hash: Hifadhi ya Thamani Muhimu


Ramani za Hash hutoa hifadhi bora ya thamani ya funguo ambapo unaweza kutafuta haraka thamani kulingana na funguo zinazohusiana nazo. Funguo na thamani zote mbili zinaweza kuwa za aina yoyote, ingawa funguo lazima zitekeleze sifa muhimu za upigaji hashi na ulinganisho wa usawa. Ramani za Hash huchukua umiliki wa thamani zilizoingizwa isipokuwa thamani zitekeleze sifa ya Nakala.


Ramani za Hash hutoa mbinu kadhaa za kuingiza na kusasisha thamani. Mbinu ya msingi ya `insert()` itabadilisha thamani zilizopo, huku `entry()` ikitoa mantiki rahisi zaidi ya kuingiza. Ingizo la API hukuruhusu kuingiza thamani tu ikiwa hazipo tayari, au kusasisha thamani zilizopo kulingana na hali yao ya sasa. API hii ni muhimu kwa mifumo kama vile matukio ya kuhesabu au kudumisha jumla zinazoendeshwa.


Unaporejesha thamani kutoka kwa ramani za hash, mbinu ya `get()` hurejesha `Option` kwa kuwa ufunguo ulioombwa huenda usiwepo. Unaweza kutumia mbinu kama `copied()` kubadilisha kutoka `Option<&T>` hadi `Option<T>` kwa aina za Nakili, na `unwrap_or()` kutoa thamani chaguo-msingi wakati funguo hazipo.


### Ushughulikiaji wa Kamba na Unicode


Mifuatano katika Rust imesimbwa kwa UTF-8, ambayo hutoa usaidizi kamili wa Unicode lakini huanzisha ugumu ikilinganishwa na mifuatano rahisi ya ASCII. Aina ya `String` inawakilisha data ya maandishi inayomilikiwa, inayoweza kukuzwa, huku vipande vya mifuatano (`&str`) vikitoa mitazamo iliyokopwa kuwa data ya mifuatano. Unaweza kubadilisha kati ya aina hizi inapohitajika, huku vipande vya mifuatano vikitumika mara nyingi kwa vigezo vya utendaji ili kukubali mifuatano inayomilikiwa na mifuatano halisi ya mifuatano.


Ubadilishaji wa mfuatano unajumuisha mbinu za kuambatanisha maandishi, kupangilia thamani nyingi pamoja, na kutoa mfuatano mdogo. Mbinu ya `push_str()` huambatanisha vipande vya mfuatano bila kuchukua umiliki, huku makro ya `format!` ikitoa njia rahisi ya kujenga mfuatano kutoka kwa vipengele vingi. Unapofanya kazi na fahirisi za mfuatano, lazima uwe mwangalifu kuheshimu mipaka ya herufi za UTF-8 ili kuepuka hofu ya wakati wa utekelezaji.


Kwa usindikaji salama wa herufi kwa herufi, mifuatano hutoa mbinu za kirudiarudia kama vile `chars()` kwa thamani za kielelezo cha Unicode na `baiti()` kwa ufikiaji wa baiti ghafi. Virudiarudia hivi hushughulikia usimbaji wa UTF-8 kwa usahihi, kuhakikisha hugawanyi herufi za baiti nyingi kwa bahati mbaya. Mbinu hii ni salama na ya kuaminika zaidi kuliko uorodheshaji wa mikono, hasa unapofanya kazi na maandishi ya kimataifa ambayo yanaweza kuwa na herufi changamano za Unicode.



## Mfumo wa Kushughulikia Hitilafu za Kategoria Mbili za Rust

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust inachukua mbinu tofauti kabisa ya kushughulikia makosa ikilinganishwa na lugha nyingi za programu. Ingawa lugha nyingi hutegemea zaidi tofauti, Rust hutofautisha kati ya kategoria mbili tofauti za makosa na hutoa mifumo maalum ya kushughulikia kila aina. Sura hii inachunguza mfumo kamili wa kushughulikia makosa wa Rust, ikishughulikia makosa yasiyoweza kurejeshwa ambayo husitisha utekelezaji wa programu na makosa yanayoweza kurejeshwa ambayo huruhusu programu kuendelea kufanya kazi kwa uzuri.


### Makosa na Hofu Isiyoweza Kurekebishwa


Hitilafu zisizoweza kurejeshwa zinawakilisha hali ambapo programu imeingia katika hali isiyo thabiti au isiyotarajiwa ambayo haiwezi kupona kwa usalama. Hizi ni pamoja na matukio kama vile kufikia safu isiyo na mipaka, kujaribu shughuli zinazokiuka usalama wa kumbukumbu, au kukutana na hali zinazoonyesha makosa ya msingi ya mantiki ya programu. Wakati makosa kama hayo yanapotokea, jibu linalofaa ni kukomesha programu mara moja badala ya kuhatarisha ufisadi zaidi au tabia isiyoeleweka.


Katika Rust, hitilafu zisizoweza kurejeshwa husababisha hofu, ambayo husababisha programu kuanguka kwa njia iliyodhibitiwa. Kabla ya kuisha, Rust hufanya mchakato unaoitwa kufungua, ambapo hupitia kwenye rundo la simu ili kutoa maelezo ya kina ya rundo yanayoonyesha haswa mahali ambapo hofu ilitokea. Mchakato huu wa kufungua huwasaidia wasanidi programu kutambua chanzo cha tatizo wakati wa utatuzi wa matatizo. Kwa programu muhimu za utendaji au mifumo iliyopachikwa, unaweza kuzima kufungua na kusanidi Rust ili kuisha mara moja wakati hofu inapotokea, ingawa hii huondoa taarifa za utatuzi wa matatizo ili kuisha haraka.


Unaweza kusababisha hofu waziwazi kwa kutumia makro ya `panic!` ukitumia ujumbe maalum. Wakati hofu inapotokea, utaona matokeo yanayoonyesha ni uzi gani uliopanikishwa na ujumbe unaohusiana. Kuweka kigezo cha mazingira cha `RUST_BACKTRACE` hutoa taarifa za ziada za utatuzi wa matatizo, kuonyesha rundo kamili la simu lililosababisha hofu. Kwa mfano, kujaribu kufikia kipengele 99 cha vekta yenye vipengele vitatu pekee kutabadilisha generate kuwa hofu yenye ujumbe wa "faharasa nje ya mipaka", pamoja na mfuatano wa nyuma unaoonyesha mfuatano halisi wa simu za utendaji kazi zilizosababisha hitilafu.


### Makosa Yanayoweza Kurejeshwa Yenye Matokeo


Hitilafu zinazoweza kurejeshwa zinawakilisha hali zinazotarajiwa za hitilafu ambazo programu zinaweza kushughulikia kwa uzuri bila kukomesha. Mifano ni pamoja na kujaribu kufungua faili ambayo haipo, hitilafu za muunganisho wa mtandao, au ingizo batili la mtumiaji. Kwa hali hizi, Rust hutoa enum ya `Result`, ambayo inawakilisha waziwazi shughuli ambazo zinaweza kushindwa na kuwalazimisha wasanidi programu kushughulikia kesi zote mbili za mafanikio na hitilafu.


Enum ya `Result` imefafanuliwa kwa lahaja mbili: `Ok(T)` kwa shughuli zilizofanikiwa zenye thamani ya aina ya `T`, na `Err(E)` kwa hitilafu zenye hitilafu ya aina ya `E`. Muundo huu hutumia mfumo wa aina wa Rust ili kuhakikisha kwamba hitilafu zinazoweza kutokea haziwezi kupuuzwa. Vitendakazi vinavyoweza kushindwa hurudisha `Result`, na msimbo wa kupiga simu lazima ushughulikie waziwazi visa vya mafanikio na hitilafu, kwa kawaida kwa kutumia ulinganishaji wa muundo na misemo ya `mechi`.


Fikiria chaguo-msingi la `Faili::fungua`, ambalo hurejesha `Result<Faili, std::io::Error>`. Unapofungua faili, unapokea kitu cha `Faili` ikiwa kimefanikiwa au `std::io::Error` ikiwa operesheni itashindwa. Unaweza kulinganisha matokeo haya ili kushughulikia kila kesi ipasavyo. Katika kesi ya mafanikio, unaweza kuendelea na shughuli za faili, huku katika kesi ya hitilafu, unaweza kujaribu kuunda faili, kujaribu mbinu mbadala, au kueneza hitilafu kwenye msimbo wa kupiga simu. Ushughulikiaji huu dhahiri unahakikisha kwamba programu yako hufanya maamuzi ya kimakusudi kuhusu urejeshaji wa hitilafu badala ya kuanguka bila kutarajia.


### Hitilafu katika Kushughulikia Mifumo na Njia za Mkato


Ingawa ulinganishaji dhahiri wa ruwaza hutoa udhibiti kamili wa utunzaji wa hitilafu, Rust inatoa mbinu kadhaa za urahisi kwa ruwaza za kawaida za utunzaji wa hitilafu. Mbinu ya `unwrap` hutoa thamani ya mafanikio kutoka kwa `Tokeo` lakini husababisha hofu ikiwa hitilafu itatokea, na kuifanya iwe muhimu kwa uundaji wa haraka wa prototype au hali ambapo una uhakika kwamba operesheni itafanikiwa. Mbinu ya `expect` inafanya kazi vivyo hivyo lakini hukuruhusu kutoa ujumbe maalum wa hofu, na kurahisisha utatuzi wa hitilafu wakati mambo yanapoenda vibaya.


Kwa utunzaji wa hitilafu unaonyumbulika zaidi, mbinu kama `unwrap_or_else` hukuruhusu kutoa hitilafu inayofanya kazi wakati hitilafu inapotokea, na kuwezesha mantiki maalum ya urejeshaji. Unaweza kuunganisha shughuli hizi pamoja ili kushughulikia hali ngumu, kama vile kujaribu kufungua faili na kuiunda ikiwa haipo, ukiwa na mikakati tofauti ya utunzaji wa hitilafu kwa kila hatua.


Opereta ya alama ya kuuliza (`?`) hutoa sintaksia fupi ya uenezaji wa hitilafu, ambayo ni ya kawaida katika programu za Rust. Unapoongeza `?` kwenye `Tokeo`, hufungua kiotomatiki thamani zilizofanikiwa na hurejesha hitilafu mara moja kutoka kwa chaguo-msingi la sasa. Opereta hii inaweza kutumika tu katika chaguo-msingi zinazorudisha aina za `Tokeo`, kuhakikisha kwamba hitilafu zinaweza kuenezwa ipasavyo kwenye rundo la simu. Opereta ya `?` hufanya msimbo wa utunzaji wa hitilafu usomeke zaidi kwa kuondoa misemo inayolingana na vitenzi huku ikidumisha semantiki dhahiri ya uenezaji wa hitilafu.


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


### Uenezaji wa Makosa na Ubunifu wa Vitendo


Uenezaji wa hitilafu ni dhana ya msingi katika utunzaji wa hitilafu wa Rust, kuruhusu chaguo za utendaji kupitisha hitilafu kwenye rundo la simu badala ya kuzishughulikia ndani ya eneo. Unapobuni chaguo za utendaji ambazo zinaweza kushindwa, unapaswa kurudisha aina za `Result` ili kuwapa wapigaji kura uhuru wa kuamua jinsi ya kushughulikia hitilafu. Mbinu hii inakuza utunzaji wa hitilafu unaoweza kutungwa ambapo kila chaguo la utendaji katika mnyororo wa simu linaweza kushughulikia hitilafu ndani ya eneo au kuzipitisha hadi msimbo wa kiwango cha juu ambao una muktadha zaidi wa kufanya maamuzi ya urejeshaji.


Kiendeshaji cha alama ya kuuliza hurahisisha uenezaji wa makosa. Badala ya kuandika misemo ya ulinganisho wa vitenzi kwa kila operesheni inayoweza kushindwa, unaweza kuunganisha shughuli pamoja na viendeshaji vya `?`, na kuunda msimbo unaoweza kusomeka unaoshughulikia njia ya mafanikio huku ukieneza kiotomatiki makosa yoyote yanayotokea. Muundo huu ni wa kawaida sana kiasi kwamba vitendakazi vingi vya Rust vimeundwa mahsusi kufanya kazi vizuri na kiendeshaji cha `?`, na kuwezesha utunzaji wa makosa kwa ufasaha katika mfumo wako wa msimbo.


Unapoamua kati ya makosa ya kuogopa na kurudisha, fikiria kama msimbo wa kupiga simu unaweza kupona kutokana na hitilafu. Ikiwa hitilafu inawakilisha hitilafu ya programu au hali ya mfumo isiyoweza kurejeshwa, kuogopa kunafaa. Hata hivyo, ikiwa hitilafu ni sharti linalotarajiwa ambalo msimbo wa kupiga simu unaweza kushughulikia tofauti kulingana na muktadha, kurejesha `Matokeo` hutoa unyumbufu na uthabiti bora.


### Mbinu Bora na Mambo ya Kuzingatia katika Ubunifu


Ushughulikiaji mzuri wa hitilafu katika Rust unahitaji kuzingatia kwa makini wakati wa kuogopa dhidi ya wakati wa kurudisha hitilafu. Tumia hofu kwa hali zinazowakilisha hitilafu za programu au hali ambazo hazipaswi kutokea katika programu sahihi, kama vile kufikia data ngumu ambayo unajua ni halali. Kwa mfano, kuchanganua kamba ya anwani ya IP ngumu ambayo umethibitisha kuwa sahihi kunaweza kutumia kwa usalama `expect` na ujumbe unaoelezea kwa nini operesheni haipaswi kushindwa kamwe.


Kwa mwingiliano wa ingizo au mfumo wa nje unaodhibitiwa na mtumiaji, napendelea kila wakati kurudisha aina za `Matokeo` badala ya kuwa na hofu. Watumiaji hufanya makosa, faili hufutwa, na miunganisho ya mtandao hushindwa - haya ni hali ya kawaida ambayo programu zilizoundwa vizuri zinapaswa kushughulikia kwa uzuri. Kwa kurudisha makosa kwa hali hizi, unaruhusu msimbo wa kupiga simu kutekeleza mikakati inayofaa ya urejeshaji, iwe hiyo inamshawishi mtumiaji kuingiza data tofauti, kurudi kwenye thamani chaguo-msingi, au kuonyesha ujumbe muhimu wa hitilafu.


Fikiria kuunda aina maalum zinazotekeleza uthibitishaji wakati wa ujenzi ili kuzuia hali batili kuenea kupitia programu yako. Kwa mfano, ikiwa programu yako inahitaji nambari ndani ya masafa maalum, tengeneza aina ya kifungashio kinachothibitisha ingizo wakati wa ujenzi na haitoi njia ya kuunda mifano batili. Mbinu hii inatumia mfumo wa aina wa Rust ili kuondoa aina nzima za makosa kwa kufanya hali batili zisiweze kuwakilishwa, na kupunguza hitaji la ukaguzi wa hitilafu za wakati wa utekelezaji katika mfumo wako wa msimbo.


## Vipengele vya Programu Vinavyofanya Kazi, Vifungashio na Vidokezo Mahiri


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Ingawa Rust si lugha safi ya programu inayofanya kazi, inajumuisha vipengele vilivyoongozwa na mifumo ya programu inayofanya kazi. Vipengele hivi huwawezesha wasanidi programu kuandika msimbo mfupi kwa kutumia dhana kama vile kufunga na kurudiarudia. Rust inajumuisha vipengele hivi vya utendaji ili kutoa zana zinazoweza kubadilika kwa ajili ya usindikaji wa data na mifumo ya kurudisha data.


Vipengele vya utendakazi wa programu katika Rust hudumisha kanuni kuu za lugha za usalama wa kumbukumbu na vifupisho visivyo na gharama kubwa. Unapotumia vifungashio na virudiaji, hautoi utendaji kwa ajili ya usemi - mkusanyiko wa Rust huboresha miundo hii ili kutoa msimbo mzuri wa mashine unaolingana na mbinu za kitamaduni zinazotegemea kitanzi.


### Kuelewa Kufungwa


Kufungwa katika Rust ni chaguo zisizojulikana ambazo zinaweza kunasa vigezo kutoka kwa mazingira yanayowazunguka. Katika lugha zingine za programu, hizi mara nyingi huitwa chaguo za lambda. Sifa muhimu ya kufungwa ni uwezo wao wa "kufunga" mazingira yao, ikimaanisha kuwa wanaweza kufikia na kutumia vigezo vilivyopo katika wigo ambapo kufungwa kunafafanuliwa.


Sintaksia ya vifungashio hutumia herufi za bomba (`|`) badala ya mabano kufafanua vigezo. Kwa kifungashio kisicho na vigezo, unaandika `||`, na kwa vifungashio vyenye vigezo, unaviorodhesha kati ya mabomba kama `|x, y|`. Ikiwa mwili wa kifungashio una usemi mmoja, unaweza kuacha vibandiko vilivyopinda, na kufanya sintaksia iwe fupi sana.


Fikiria mfano huu wa vitendo wa kampuni ya fulana inayotoa mashati ya kipekee kulingana na mapendeleo ya wateja. Ikiwa mteja amebainisha rangi anayoipenda, anapokea rangi hiyo; vinginevyo, anapata rangi iliyojaa zaidi kama chaguo-msingi. Kwa kutumia vifungashio, mantiki hii inakuwa: `user_preference.unwrap_or_else(|| self.most_stocked())`. Kifungashio `|| self.most_stocked()` hutoa thamani chaguo-msingi inapohitajika tu, na inaweza kufikia `self` kutoka kwa mazingira yake.


### Aina ya Kufungwa na Unyumbufu


Mojawapo ya vipengele rahisi zaidi vya Rust vyenye vifungashio ni ukadiriaji wa aina otomatiki. Tofauti na vitendakazi vya kawaida ambapo lazima ubainishe wazi aina za vigezo na aina za kurudi, vifungashio mara nyingi vinaweza kukadiria aina hizi kutoka kwa muktadha. Kikusanyaji huchambua jinsi kifungashio kinavyotumika na huamua aina zinazofaa kiotomatiki. Hata hivyo, mara tu kifungashio kinapoitwa na aina maalum, aina hizo huwa hazibadiliki kwa mfano huo wa kufungwa.


Unaweza kuhifadhi vifungashio katika vigeu kama thamani nyingine yoyote, na kuvifanya kuwa raia wa daraja la kwanza katika lugha. Unapoweka kifungashio kwenye kigeu, unaweza kukiita baadaye kwa kutumia mabano: `let my_closure = |x| x + 1; let result = my_closure(5);`. Unyumbulifu huu hukuruhusu kupitisha vifungashio kama hoja kwa vitendaji, kuvirudisha kutoka kwa vitendaji, na kuvitumia katika miundo ya data.


Ikiwa mkusanyaji hawezi kukisia aina au ikiwa unataka kuwa wazi, unaweza kunukuu vigezo vya kufungwa na kurudisha aina kwa kutumia sintaksia inayofanana na vitendakazi: `|x: i32| -> i32 {x + 1}`. Uchapaji huu wazi wakati mwingine ni muhimu katika hali ngumu ambapo mkusanyaji anahitaji taarifa za ziada ili kutatua aina kwa usahihi.


### Kukamata Vigezo vya Mazingira


Vifungashio vinaweza kunasa vigeu kutoka kwa mazingira yao kwa njia tatu tofauti: kwa marejeleo yasiyobadilika, kwa marejeleo yanayoweza kubadilika, au kwa kuchukua umiliki. Kikusanyaji cha Rust huamua kiotomatiki njia ya kunasa yenye vikwazo zaidi inayokidhi mahitaji ya kufungwa kwako, kwa kufuata kanuni ya upendeleo mdogo.


Wakati kufungwa kunahitaji tu kusoma thamani, kunasa kwa marejeleo yasiyobadilika. Hii inaruhusu kigezo asili kubaki kupatikana baada ya kufungwa kufafanuliwa na kuitwa. Kwa mfano, kufungwa kunakochapisha orodha kutaikopa orodha bila kubadilika, kukuruhusu kuendelea kutumia orodha baada ya kufungwa kutekelezwa.


Ikiwa kufungwa kunahitaji kurekebisha kigezo kilichonaswa, lazima kinase kwa marejeleo yanayoweza kubadilishwa. Katika hali hii, kigezo kilichonaswa na kufungwa chenyewe lazima vitangazwe kama vinavyoweza kubadilishwa. Kufungwa kunaweza kurekebisha kigezo kilichonaswa, lakini sheria za kukopa bado zinatumika - huwezi kuwa na marejeleo mengine ya kigezo hicho wakati kufungwa kunakoweza kubadilishwa.


Mbinu yenye vikwazo zaidi ya kunasa ni kuchukua umiliki, ambayo huhamisha vigeu vilivyonaswa hadi kwenye kufungwa. Hii ni muhimu wakati kufungwa kunaweza kudumu zaidi ya upeo ambapo vigeu vilifafanuliwa awali, kama vile wakati wa kutoa nyuzi. Unaweza kulazimisha kunasa umiliki kwa kutumia neno muhimu la `move` kabla ya vigezo vya kufungwa: `move |x| { /* closing body */ }`. Hii ni muhimu kwa usalama wa nyuzi, kwani nyuzi haziwezi kukopa kwa usalama kutoka kwa nyuzi zingine ambazo zinaweza kukomesha na kuacha vigeu vyake.


### Sifa za Kufungwa na Aina za Kazi


Rust inawakilisha kufungwa kupitia mfumo wa sifa wenye sifa tatu muhimu: `FnOnce`, `FnMut`, na `Fn`. Sifa hizi huunda safu ya uongozi inayoelezea jinsi kufungwa kunavyoweza kuitwa na kile wanachoweza kufanya na vigeu vilivyonakiliwa.


`FnOnce` ni sifa ya msingi zaidi ambayo vifungashio vyote hutekeleza. Inawakilisha vifungashio ambavyo vinaweza kuitwa angalau mara moja. Baadhi ya vifungashio, hasa vile vinavyohamisha thamani zilizonaswa au kuzitumia kwa njia fulani, vinaweza kuitwa mara moja tu kwa sababu huharibu au kuhamisha data yao iliyonaswa wakati wa utekelezaji.


`FnMut` inawakilisha vifungashio ambavyo vinaweza kuitwa mara nyingi na vinaweza kubadilisha mazingira yao yaliyonaswa. Vifungashio hivi hunasa vigeu kwa marejeleo yanayoweza kubadilishwa na vinaweza kuvibadilisha katika simu nyingi. Sheria za kukopa zinahakikisha kwamba wakati kufungwa kwa `FnMut` kunafanya kazi, kuna ufikiaji wa kipekee unaoweza kubadilishwa kwa vigeu vyake vilivyonaswa.


`Fn` ndiyo sifa yenye vikwazo zaidi, inayowakilisha kufungwa ambako kunaweza kuitwa mara nyingi bila kubadilisha mazingira yao yaliyonaswa. Kufungwa huku kunachukuliwa tu kwa marejeleo yasiyobadilika na kunaweza kuitwa kwa wakati mmoja bila kukiuka dhamana za usalama za Rust. Ikiwa kufungwa kunatekeleza `Fn`, hutekeleza kiotomatiki `FnMut` na `FnOnce` pia, kwa kuwa kuweza kuitwa mara nyingi bila mabadiliko kunamaanisha kuweza kuitwa pamoja na mabadiliko na kuweza kuitwa mara moja.


### Kufanya kazi na Warudiaji


Virudiaji katika Rust hutoa njia ya kuchakata mfuatano wa data. Ni wavivu, ikimaanisha kuwa hawafanyi kazi yoyote hadi utakapozitumia kwa kutumia mbinu zinazorudia kupitia data. Tathmini hii ya uvivu inaruhusu uunganishaji mzuri wa shughuli bila kuunda makusanyo ya kati.


Sifa ya `Iterator` hufafanua utendaji kazi wa msingi na aina inayohusiana ya `Item` inayowakilisha kile ambacho kirudishi hutoa, na mbinu ya `next` inayorudisha `Option<Self::Item>`. `next` inaporudisha `None`, kirudishi huwa kimeisha. Muundo huu huruhusu virudishi kuwakilisha mfuatano wenye kikomo na uwezekano usio na kikomo kwa usalama.


Unaweza kuunda virudiaji kutoka kwa mikusanyiko kwa kutumia mbinu kama vile `iter()` kwa ajili ya kukopa marudio, `iter_mut()` kwa ajili ya kukopa marudio yanayoweza kubadilishwa, na `into_iter()` kwa ajili ya kutumia marudio. Chaguo kati ya mbinu hizi linategemea kama unahitaji kurekebisha vipengele na kama unataka kutumia mkusanyiko wa asili.


### Adapta za Kipima Muda na Watumiaji


Adapta za kipima ni mbinu zinazobadilisha kipima kimoja kuwa kingine, na kukuruhusu kuunganisha shughuli pamoja. Adapta za kawaida ni pamoja na `map` ya kubadilisha kila kipengele, `kichujio` cha kuchagua vipengele kulingana na kiambishi, na `enumerate` ya kuongeza fahirisi. Adapta hizi ni za uvivu - hazifanyi kazi yoyote hadi zitumike.


Mbinu ya `map` hutumia kufungwa kwa kila kipengele, na kukibadilisha kuwa kitu kingine. Kwa mfano, `numbers.iter().map(|x| x * 2)` huunda kirudiarudia kinachoongeza kila nambari mara mbili. Mbinu ya `kichujio` huweka vipengele tu ambavyo kufungwa kwa kiarifu hurejelea kuwa kweli: `numbers.iter().filter(|&x| x > 10)` huweka nambari kubwa kuliko kumi pekee.


Mbinu za watumiaji hupitia data mara kwa mara na kutoa matokeo ya mwisho. Mbinu ya `collect` hutumia kirudia na kuunda mkusanyiko kutoka kwake. Mara nyingi unahitaji kutaja aina ya mkusanyiko: `let vec: Vec<_> = iterator.collect()`. Watumiaji wengine hujumuisha `sum` kwa kuongeza vipengele vya nambari, `fold` kwa kukusanya thamani kwa kutumia operesheni maalum, na `for_each` kwa kutekeleza athari mbaya kwenye kila kipengele.


### Mifumo ya Kina ya Kirudiarudia


Shughuli za ziada za kirudiarudia ni pamoja na `zip` kwa kuchanganya vipengele viwili vya kirudiarudia, `mnyororo` kwa kuunganisha virudiarudia, na `filter_map` kwa kuchanganya kuchuja na kupanga ramani katika operesheni moja. Mbinu ya `zip` huunda jozi kutoka kwa vipengele vinavyolingana vya virudiarudia viwili: `a.iter().zip(b.iter())` hutoa nakala `(a[0], b[0]), (a[1], b[1]), ...`.


Mbinu ya `fold` ni muhimu kwa kukusanya thamani. Inachukua thamani ya awali na ufungaji unaochanganya mkusanyiko na kila kipengele: `numbers.iter().fold(0, |acc, x| acc + x)` hujumlisha nambari zote. Muundo huu unaweza kutekeleza shughuli zingine nyingi kama vile kutafuta thamani za juu zaidi, kujenga mifuatano, au kuunda miundo changamano ya data.


Minyororo ya iterator inaweza kuelezea mabadiliko changamano ya data kwa ufupi. Kwa mfano, usindikaji wa data ya sauti unaweza kuhusisha: `coefficients.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Hii huzidisha viambato vinavyolingana na thamani za bafa, hujumlisha matokeo, na hubadilisha thamani ya mwisho, yote katika usemi mmoja unaoweza kusomeka.


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


### Utangulizi wa Viashiria Mahiri


Viashiria mahiri ni miundo ya data inayofanya kazi kama viashiria vya kitamaduni lakini hutoa uwezo wa ziada na usimamizi wa kumbukumbu kiotomatiki. Tofauti na marejeleo rahisi, viashiria mahiri humiliki data wanayoelekeza na vinaweza kutekeleza tabia maalum kwa ajili ya ugawaji wa kumbukumbu, ugawaji wa data, na mifumo ya ufikiaji. Ni zana muhimu za kudhibiti data iliyotengwa kwa wingi na kutekeleza mifumo tata ya umiliki ambayo inazidi mfumo wa msingi wa umiliki wa Rust.


Kipengele cha "mahiri" kinatokana na uwezo wao wa kushughulikia kiotomatiki kazi za usimamizi wa kumbukumbu ambazo vinginevyo zingehitaji uingiliaji kati wa mikono. Kiashiria mahiri kinapopotea, kinaweza kuondoa kumbukumbu inayohusiana kiotomatiki, kupunguza hesabu za marejeleo, au kufanya shughuli zingine za usafi. Kiotomatiki hiki husaidia kuzuia uvujaji wa kumbukumbu na makosa ya matumizi baada ya kutokuwepo huku kikitoa unyumbufu zaidi kuliko ugawaji wa rafu pekee.


Viashiria mahiri kwa kawaida hutekeleza sifa mbili muhimu: `Deref` na `Drop`. Sifa ya `Deref` huruhusu kiashiria mahiri kutumika kana kwamba ni marejeleo ya data iliyomo. Sifa ya `Drop` huwezesha mantiki ya usafishaji maalum wakati kiashiria mahiri kinapoharibiwa. Kwa pamoja, sifa hizi huruhusu viashiria mahiri kudhibiti kumbukumbu kiotomatiki.


### Kiashiria Mahiri cha Sanduku


`Box<T>` ni kiashiria mahiri rahisi zaidi, kinachotoa mgao wa chungu kwa aina yoyote ya `T`. Unapounda `Box`, thamani iliyomo huhifadhiwa kwenye chungu badala ya chungu, na `Box` yenyewe (ambayo ni kiashiria tu) huhifadhiwa kwenye chungu. Uelekezaji huu ni muhimu unapohitaji kuhifadhi kiasi kikubwa cha data bila kuisogeza, unapohitaji aina yenye ukubwa usiojulikana wa muda wa kukusanya, au unapotaka kuhamisha umiliki wa data ya chungu kwa ufanisi.


Kuunda `Box` ni rahisi: `let boxed_value = Box::new(42);` hugawa nambari kamili kwenye rundo. `Box` hudhibiti kumbukumbu hii kiotomatiki - wakati `Box` inapotoweka, huhamisha kumbukumbu ya rundo kiotomatiki. Usafi huu otomatiki huzuia uvujaji wa kumbukumbu bila kuhitaji usimamizi wa kumbukumbu kwa mikono.


Mojawapo ya visa muhimu zaidi vya matumizi ya `Box` ni kuwezesha miundo ya data inayojirudia. Fikiria orodha iliyounganishwa ambapo kila nodi ina thamani na kielekezi cha nodi inayofuata. Bila `Box`, huwezi kufafanua muundo kama huo kwa sababu mkusanyaji hawezi kubaini ukubwa wa aina inayojirudia. Kwa kutumia `Box<Node>` kwa kielekezi kinachofuata, unavunja tatizo la ukubwa unaojirudia kwa sababu `Box` ina ukubwa unaojulikana na usiobadilika bila kujali ina nini.


### Utekelezaji wa Sifa ya Deref


Sifa ya `Deref` inaruhusu aina kuachwa kwa marejeleo kwa kutumia opereta wa `*`, na kufanya viashiria mahiri vifanye kama marejeleo ya data iliyomo. Unapotekeleza `Deref` kwa kiashiria mahiri, unawezesha uondoaji wa marejeleo kiotomatiki unaofanya kiashiria mahiri kuwa wazi kutumia. Hii ina maana kwamba unaweza kupiga simu mbinu kwenye aina iliyomo moja kwa moja kupitia kiashiria mahiri bila uondoaji marejeleo dhahiri.


Sifa ya `Deref` hufafanua aina inayohusiana `Target` ambayo hubainisha aina ya marejeleo ambayo operesheni ya uondoaji marejeleo inapaswa kutoa. Sifa inahitaji kutekeleza mbinu ya `deref` ambayo hurejesha marejeleo kwa aina lengwa. Kwa `Box<T>`, utekelezaji hurejesha marejeleo kwa thamani ya `T` iliyomo.


Rust hufanya ulazimishaji wa kiotomatiki wa kukwepa marejeleo, ambayo ina maana kwamba mkusanyaji anaweza kuingiza simu kiotomatiki kwenye `deref` inapohitajika ili kufanya aina ziendane. Hii ndiyo sababu unaweza kupitisha `String` kwenye kitendakazi kinachotarajia `&str` - mkusanyaji huondoa marejeleo ya `String` kiotomatiki ili kupata kipande cha mfuatano. Ulazimishaji huu unaweza kuunganishwa katika viwango vingi, kwa hivyo `Box<String>` inaweza kubadilishwa kiotomatiki kuwa `&str` kupitia shughuli nyingi za kukwepa marejeleo.


### Utekelezaji Maalum wa Kuacha


Sifa ya `Drop` hukuruhusu kutaja msimbo maalum wa usafishaji unaofanya kazi wakati thamani inapotoweka. Hii ni muhimu sana kwa viashiria mahiri vinavyosimamia rasilimali zaidi ya kumbukumbu rahisi, kama vile vipini vya faili, miunganisho ya mtandao, au hesabu za marejeleo. Sifa ya `Drop` ina njia moja, `drop`, ambayo inachukua marejeleo yanayoweza kubadilishwa kwa `self` na kufanya usafishaji.


Aina nyingi hazihitaji utekelezaji maalum wa `Drop` kwa sababu Rust hushughulikia kiotomatiki kudondosha sehemu zao. Hata hivyo, viashiria mahiri mara nyingi huhitaji mantiki maalum ili kusafisha ipasavyo rasilimali wanazosimamia. Kwa mfano, kiashiria mahiri kilichohesabiwa marejeleo kinahitaji kupunguza idadi ya marejeleo na uwezekano wa kusambaza data iliyoshirikiwa wakati marejeleo ya mwisho yanapotoshwa.


Unaweza pia kuangusha thamani moja kwa moja kabla haijatoka kwenye wigo kwa kutumia `std::mem::drop()`. Kitendakazi hiki huchukua umiliki wa thamani na kuiangusha mara moja, ambayo inaweza kuwa muhimu kwa kutoa rasilimali mapema au kuhakikisha usafi unafanyika katika hatua maalum katika programu yako. Kitendakazi cha kuangusha dhahiri ni kitendakazi cha utambulisho tu kinachochukua umiliki - kazi halisi hutokea wakati thamani inaachwa mwishoni mwa kitendakazi.


Msingi huu wa vifungashio, virudiaji, na viashiria mahiri huwapa wasanidi programu wa Rust zana za kuandika msimbo unaoeleweka, salama, na ufanisi. Vipengele hivi hufanya kazi pamoja ili kuwezesha mifumo ya kawaida ya programu huku vikidumisha dhamana kuu za Rust za usalama na utendaji wa kumbukumbu.



## Hesabu ya Marejeleo na Ubadilikaji wa Ndani

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Kuhesabu Marejeleo kwa kutumia RC


Kuhesabu marejeleo kunawakilisha aina nyingine ya msingi ya kiashiria mahiri katika Rust, iliyoundwa mahsusi kuwezesha hali nyingi za umiliki. Tofauti na Box, ambayo hufuata sheria za kitamaduni za umiliki mmoja ambapo huluki moja inamiliki data, RC (Reference Counter) inaruhusu sehemu nyingi za msimbo wako kushiriki umiliki wa data sawa kwa wakati mmoja. Mfumo huu wa umiliki wa pamoja hufanya kazi kupitia utaratibu wa kuhesabu unaofuatilia ni marejeleo mangapi yaliyopo kwa kipande fulani cha data.


Mfumo wa kuhesabu marejeleo hufanya kazi kwa kudumisha kihesabu cha ndani kinachoongezeka kila wakati unapobadilisha RC na kupunguza wakati RC inapoachwa. Kumbukumbu huachiliwa tu wakati kihesabu hiki kinafikia sifuri, kuhakikisha kwamba data inabaki halali mradi tu marejeleo yoyote yapo. Mbinu hii huzuia ugawaji wa mapema huku ikiwezesha mifumo rahisi ya kushiriki data ambayo isingewezekana kwa umiliki rahisi wa Kisanduku.


Mfano wa vitendo ambapo RC ni muhimu unahusisha kuunda miundo ya data iliyoshirikiwa kama orodha zilizounganishwa ambapo orodha nyingi zinaweza kurejelea sehemu moja ya mkia. Fikiria kujaribu kuunda orodha mbili tofauti ambazo zote zinarejelea mfuatano wa kawaida. Kwa umiliki wa Sanduku, hii inakuwa haiwezekani kwa sababu kuhamisha sehemu iliyoshirikiwa kwenye orodha ya kwanza huhamisha umiliki, kuzuia matumizi yake katika orodha ya pili. RC hutatua hili kwa kukuruhusu kuiga marejeleo badala ya data ya msingi, na kufanya muundo ulioshirikiwa uwezekane huku ukidumisha usalama wa kumbukumbu.


Unapoiga RC, hunakili data ya ndani bila kujali ukubwa au ugumu wake. Badala yake, unaunda marejeleo mengine kwa eneo lile lile la kumbukumbu na kuongeza kihesabu cha marejeleo. Hii inafanya uundaji wa matukio ya RC kuwa na ufanisi hata kwa miundo mikubwa ya data, kwani marejeleo yenyewe pekee ndiyo yanayonakiliwa huku data ya msingi ikibaki mahali pake.


### Ubadilishaji wa Ndani kwa kutumia RefCell


RefCell inaleta mabadiliko ya ndani, ambayo hukuruhusu kubadilisha data hata unapokuwa na marejeleo yasiyobadilika tu. Uwezo huu hubadilisha kimsingi jinsi sheria za kukopa za Rust zinavyotekelezwa kwa kuhamisha ukaguzi kutoka wakati wa kukusanya hadi wakati wa utekelezaji. Ingawa marejeleo ya kawaida hutegemea mkusanyaji kuthibitisha usalama wa kukopa, RefCell hufanya ukaguzi huu wakati wa utekelezaji wa programu, ikitoa unyumbufu mkubwa kwa gharama ya hofu zinazowezekana za wakati wa utekelezaji.


Kanuni kuu ya RefCell inahusisha kudumisha sheria zile zile za kukopa ambazo Rust huzitekeleza kwa kawaida wakati wa kukusanya, lakini kuziangalia kwa njia inayobadilika. Wakati wowote, unaweza kuwa na marejeleo moja yanayoweza kubadilika au idadi yoyote ya marejeleo yasiyobadilika kwa data iliyo ndani ya RefCell. Ikiwa msimbo wako utajaribu kukiuka sheria hizi kwa kuunda mikopo inayokinzana kwa wakati mmoja, programu itaogopa badala ya kutoa tabia isiyoeleweka.


Ukaguzi huu wa wakati wa utekelezaji huwezesha ruwaza fulani za programu ambazo mkusanyaji anaweza kukataa hata zinapokuwa salama. Uchambuzi tuli wa mkusanyaji hauwezi kuthibitisha kila wakati kwamba ruwaza tata za kukopa ni sahihi, na kuipelekea kufanya makosa kwa upande wa tahadhari. RefCell hukuruhusu kupuuza vikwazo hivi vya kihafidhina unapojiamini katika usahihi wa msimbo wako, lakini ujasiri huu unakuja na jukumu la kuhakikisha matumizi sahihi ili kuepuka ajali za wakati wa utekelezaji.


Kesi ya kawaida ya matumizi ya RefCell inahusisha vitu vya majaribio katika hali za majaribio. Wakati wa kutekeleza sifa ambayo hutoa ufikiaji usiobadilika wa kibinafsi, lakini utekelezaji wako wa majaribio unahitaji kufuatilia mabadiliko ya hali ndani, RefCell huwezesha muundo huu. Unaweza kufunga hali ya ndani katika RefCell, ikiruhusu mock kubadilisha data yake ya ufuatiliaji hata kupitia kiolesura kisichobadilika.


### Kuchanganya RC na RefCell kwa Hali Inayoweza Kubadilishwa Pamoja


Mchanganyiko wa RC na RefCell huunda muundo wa hali inayoweza kubadilishwa pamoja, ambapo wamiliki wengi wanaweza kurekebisha data sawa. RC hutoa uwezo wa umiliki ulioshirikiwa, huku RefCell ikiwezesha mabadiliko kupitia marejeleo yasiyobadilika. Mchanganyiko huu ni muhimu katika hali kama vile miundo ya grafu, akiba, au hali yoyote ambapo sehemu nyingi za programu yako zinahitaji ufikiaji wa kusoma na kuandika wa data iliyoshirikiwa.


Unapofunga RefCell ndani ya RC, unaunda muundo ambao unaweza kutengenezwa kwa nakala na kusambazwa katika programu yako yote, huku kila nakala ikitoa ufikiaji wa data ile ile inayoweza kubadilishwa. Wamiliki wote wanaweza kurekebisha data kwa kutumia mbinu ya RefCell ya borrow_mut, lakini bado lazima waheshimu sheria za kukopa wakati wa utekelezaji. Muundo huu huwezesha hali ngumu za kushiriki data huku ukidumisha dhamana za usalama za Rust kupitia ukaguzi wa wakati wa utekelezaji.


Hata hivyo, unyumbulifu huu unakuja na tahadhari muhimu kuhusu uvujaji wa kumbukumbu na mizunguko ya marejeleo. Unapotumia RC na RefCell, inawezekana kuunda marejeleo ya mviringo kwa bahati mbaya ambapo miundo ya data hujirejelea yenyewe, ama moja kwa moja au kupitia mnyororo wa marejeleo. Mizunguko hii huzuia hesabu ya marejeleo kufikia sifuri, na kusababisha uvujaji wa kumbukumbu kwa sababu data inaonekana kuwa na marejeleo amilifu kila wakati hata wakati haipatikani tena kutoka kwa programu nyingine.


Suluhisho la mizunguko ya marejeleo linahusisha kutumia marejeleo dhaifu, ambayo hayachangii hesabu ya marejeleo inayotumika kwa maamuzi ya usimamizi wa kumbukumbu. Marejeleo dhaifu hukuruhusu kudumisha miunganisho kati ya miundo ya data bila kuiweka hai, kuvunja mizunguko inayowezekana huku ukihifadhi uwezo wa kufikia data inayohusiana wakati bado ipo.


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


### Misingi ya Usalama na Upatanifu wa Uzi


Mbinu ya Rust ya ulinganifu wa sarafu inalenga katika kuzuia mbio za data na masuala ya usalama wa kumbukumbu wakati wa kukusanya. Mfumo wa aina hutekeleza usalama wa nyuzi kupitia sifa kama `Tuma` na `Sawazisha`, ambazo huashiria aina kama salama kwa uhamisho kati ya nyuzi au salama kwa ufikiaji wa wakati mmoja mtawalia. Uthibitishaji huu wa wakati wa kukusanya unakamata hitilafu nyingi za ulinganifu wa sarafu ambazo zingeonekana tu wakati wa utekelezaji katika lugha zingine za programu za mifumo.


Kuunda nyuzi katika Rust hufuata muundo rahisi kwa kutumia thread::spawn, ambayo inachukua mzingo kutekeleza katika uzi mpya na hurejesha mpini kwa ajili ya kudhibiti mzunguko wa maisha wa uzi. Uzi uliozalishwa huendeshwa sambamba na uzi mkuu, na unaweza kutumia mbinu ya kujiunga kwenye mpini ili kusubiri kukamilika. Bila uunganishaji dhahiri, nyuzi zilizozalishwa zinaweza kusitishwa wakati uzi mkuu unapotoka, na hivyo kukatiza kazi isiyokamilika.


Neno muhimu la kuhamisha linakuwa muhimu wakati wa kufanya kazi na nyuzi kwa sababu kufungwa kunakopitishwa kwenye nyuzi zilizozalishwa mara nyingi huhitaji kumiliki data zao badala ya kuikopesha. Kwa kuwa nyuzi zilizozalishwa zinaweza kuishi muda mrefu kuliko wigo ulioziunda, kukopa kutoka kwa wigo mkuu husababisha ukiukwaji wa maisha yote. Kuhamisha data kwenye kufungwa kwa nyuzi huhamisha umiliki, kuhakikisha data inabaki halali kwa maisha yote ya nyuzi huku ikizuia ufikiaji kutoka kwa wigo asili.


Uwasilishaji wa ujumbe hutoa njia mbadala ya hali ya pamoja kupitia njia zinazoruhusu nyuzi kuwasiliana kwa kutuma data badala ya kushiriki kumbukumbu. Maktaba ya kawaida ya Rust hutoa njia za Multiple Producer Single Consumer (MPSC), ambapo nyuzi nyingi zinaweza kutuma ujumbe kwa uzi mmoja unaopokea. Muundo huu huondoa masuala mengi ya usawazishaji kwa kuepuka hali inayoweza kubadilishwa pamoja kabisa, badala yake hutegemea ubadilishanaji wa ujumbe kwa uratibu.


### Ushirikiano wa Hali ya Pamoja na Mutex na Arc


Wakati uwasilishaji wa ujumbe haufai, Rust hutoa hali ya pamoja ya kitamaduni kupitia Mutex (utenganishaji wa pande zote) pamoja na Arc (Kihesabu cha Marejeleo ya Atomiki). Mutex inahakikisha kwamba uzi mmoja tu ndio unaweza kufikia data iliyolindwa kwa wakati mmoja kwa kuhitaji uzi kupata kufuli kabla ya kufikia data. Kufuli hutolewa kiotomatiki wakati kitu cha mlinzi kinachorejeshwa na operesheni ya kufuli kinapotoweka, na kuzuia matukio ya kawaida ya mkwamo unaosababishwa na kufunguliwa kusahaulika.


Arc hutumika kama sawa na RC katika usalama wa nyuzi, kwa kutumia shughuli za atomiki kudhibiti hesabu ya marejeleo kwa usalama katika nyuzi nyingi. Ingawa RC inafanya kazi kikamilifu kwa hali zenye nyuzi moja, hesabu yake ya marejeleo isiyo ya atomiki huunda hali ya mbio inapofikiwa kutoka kwa nyuzi nyingi. Vihesabu vya atomiki vya Arc huhakikisha kwamba marekebisho ya hesabu ya marejeleo hufanyika kwa usalama hata chini ya ufikiaji wa wakati mmoja, na kuifanya iweze kushiriki data katika mipaka ya nyuzi.


Mchanganyiko wa Arc na Mutex huunda muundo wa hali inayoweza kubadilishwa pamoja katika programu zinazofanana. Kwa kufunga Mutex kwenye Arc, unaweza kuiga Arc ili kusambaza ufikiaji wa mutex sawa kwenye nyuzi nyingi, huku kila uzi ukiweza kupata kufuli na kurekebisha data iliyolindwa kwa usalama. Muundo huu hutoa unyumbufu wa hali iliyoshirikiwa huku ukidumisha dhamana za usalama za Rust kupitia uthibitishaji wa wakati wa kukusanya na kufunga wakati wa utekelezaji.


Sifa za Kutuma na Kusawazisha hufanya kazi nyuma ya pazia ili kuhakikisha usalama wa uzi wakati wa kukusanya. Kutuma kunaonyesha kuwa aina inaweza kuhamishiwa kwa usalama kwenye uzi mwingine, huku Kusawazisha kunaonyesha kuwa marejeleo ya aina yanaweza kushirikiwa kwa usalama kati ya nyuzi. Aina nyingi hutekeleza sifa hizi kiotomatiki wakati vipengele vyao viko salama kwenye uzi, lakini baadhi ya aina kama RC na RefCell hazizitekelezi waziwazi kwa sababu hazijaundwa kwa ajili ya ufikiaji wa wakati mmoja. Utekelezaji huu wa sifa otomatiki huzuia kuanzishwa kwa ajali kwa ukiukaji wa usalama wa uzi huku ukiruhusu aina salama kufanya kazi vizuri katika miktadha ya wakati mmoja.


## Kuelewa Macro za Rust

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Utangulizi wa Macros katika Rust


Macro katika Rust ni kipengele cha metaprogramu kinachoruhusu wasanidi programu kuandika msimbo unaozalisha msimbo mwingine wakati wa kukusanya. Tofauti na vitendakazi, ambavyo huitwa wakati wa utekelezaji, makro hupanuliwa mapema katika mchakato wa kukusanya, kabla ya kuangalia aina na hatua za baadaye. Tofauti hii ya msingi hufanya makro kuwa muhimu sana kwa kupunguza marudio ya msimbo na kuunda lugha maalum za kikoa ndani ya programu za Rust.


Kiashiria kinachotambulika zaidi cha simu ya makro ni alama ya mshangao (!) inayofuata jina la makro. Kwa mfano, unapotumia `println!("Habari, dunia!")`, huiti chaguo la kazi bali unaita makro. Macro hii hupanuka na kuwa msimbo mgumu zaidi unaoshughulikia shughuli za uumbizaji na utoaji. Alama ya mshangao hutumika kama kidokezo cha kuona kwa wasanidi programu kwamba utengenezaji wa msimbo wa wakati wa kukusanya unatokea badala ya simu ya chaguo la kazi ya kawaida.


Rust hutoa aina tatu tofauti za makro, kila moja ikihudumia madhumuni tofauti katika mfumo ikolojia wa lugha:



- Macro zinazofanana na kazi**: Hufanana na simu za kazi lakini hufanya kazi wakati wa kukusanya (k.m., `vec!`, `println!`)
- Toa makro**: Tekeleza kiotomatiki sifa za aina (k.m., `#[toa(Debug, Clone)]`)
- Makro** zinazofanana na sifa: Badilisha tabia ya vipengele vya msimbo vinavyotumika (k.m., `#[jaribio]`, `#[tokio::main]`)


Kuelewa aina hizi tofauti za makro ni muhimu kwa upangaji programu wa Rust wenye ufanisi, kwani kila moja inashughulikia matumizi maalum na mifumo ya upangaji programu.


### Aina za Macro na Matumizi Yake


Macro zinazofanana na utendaji kazi zinawakilisha aina ya makro inayopatikana sana katika programu ya Rust. Macro hizi hutumia sintaksia sawa na miito ya utendaji kazi lakini hufanya ulinganisho wa muundo kwenye ingizo lao kwa msimbo unaofaa wa generate. Macro ya `vec!` ni mfano wa kawaida wa kategoria hii, inayowaruhusu watengenezaji kuunda na kuanzisha vekta kwa sintaksia fupi. Unapoandika `vec![1, 2, 3, 4]`, makro huipanua hii kuwa msimbo unaounda vekta mpya, husukuma kila kipengele kimoja kimoja, na kurudisha vekta iliyokamilishwa.


Macro za Derive hutoa utekelezaji wa sifa otomatiki kwa aina maalum, na hivyo kupunguza kwa kiasi kikubwa msimbo wa boilerplate. Unapoongeza `#[derive(Debug)]` kwenye ufafanuzi wa muundo au enum, unaelekeza kikusanyaji kwa generate utekelezaji kamili wa sifa ya Debug kwa aina hiyo. Utekelezaji huu uliozalishwa hushughulikia mantiki ya umbizo inayohitajika ili kuonyesha yaliyomo ya aina katika umbizo linaloweza kusomwa na binadamu. Utaratibu wa derive huunga mkono sifa nyingi za kawaida za maktaba, ikiwa ni pamoja na Clone, PartialEq, na kuifanya kuwa kifaa kinachotumika sana kupunguza boilerplate.


Macro zinazofanana na sifa hurekebisha tabia ya vipengele vya msimbo wanavyoandika, na kutoa njia ya kuongeza metadata au kubadilisha tabia ya mkusanyiko. Macro hizi huonekana kama sifa zilizowekwa juu ya ufafanuzi wa aina, kazi, au miundo mingine ya msimbo. Kwa mfano, sifa ya `#[non_exhaustive]` kwenye enum inaonyesha kwamba vibadala vya ziada vinaweza kuongezwa katika matoleo yajayo, na kuhitaji misemo ya ulinganisho ili kujumuisha kesi chaguo-msingi. Utaratibu huu unahakikisha utangamano wa mbele huku ukitoa nyaraka wazi za uwezo wa mageuko ya aina.


### Kuunda Macro Maalum Zinazofanana na Kitendakazi


Kuandika makro maalum zinazofanana na kitendakazi kunahusisha kuelewa sintaksia ya ulinganishaji wa muundo wa Rust kwa fasili za makro. Ufafanuzi wa makro hutumia mbinu ya kubainisha ambapo unabainisha ruwaza zinazolingana na aina tofauti za ingizo na violezo vinavyolingana vya uundaji wa msimbo. Kila makro inaweza kuwa na matawi mengi, ikiiruhusu kushughulikia ruwaza mbalimbali za ingizo na msimbo unaofaa wa generate kwa kila kisa.


Fikiria kuunda makro ya vekta maalum inayoonyesha kanuni za msingi za ujenzi wa makro. Ufafanuzi wa makro huanza na `macro_rules!` ikifuatiwa na jina la makro na mfululizo wa matawi yanayolingana na muundo. Kila tawi lina muundo unaolingana na sintaksia maalum ya ingizo na kiolezo cha msimbo kinachozalisha msimbo unaolingana wa Rust. Kwa mfano, tawi rahisi linaweza kulinganisha mabano tupu `[]` na msimbo wa generate ili kuunda vekta tupu, huku tawi lingine likilinganisha usemi mmoja na kuzalisha msimbo ili kuunda vekta yenye kipengele kimoja.


Macro huwa muhimu sana wakati wa kutekeleza ruwaza za hoja zinazobadilika kwa kutumia sintaksia ya marudio. Muundo `$($x:expr)**` hulingana na misemo sifuri au zaidi iliyotenganishwa na koma, na kuruhusu makro kushughulikia idadi ya hoja zisizo na mpangilio. Kiolezo kinacholingana cha kutengeneza msimbo hutumia `$(vec.push($x);)*` kurudia juu ya misemo yote inayolingana na kauli za kusukuma za generate kwa kila moja. Utaratibu huu wa marudio huwezesha makro kupata msimbo wa generate ambao haungewezekana au haungekuwa wa maneno mengi kuandika kwa mkono.


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


Mchakato wa ujumuishaji hubadilisha simu za makro kuwa msimbo uliopanuliwa kabla ya ukaguzi wa aina na uboreshaji kutokea. Kikusanyaji kinapokutana na ombi la makro, hulinganisha ingizo dhidi ya mifumo iliyoainishwa na hubadilisha wito wa makro na msimbo uliozalishwa. Msimbo huu uliopanuliwa kisha hupitia michakato ya kawaida ya ujumuishaji, ikiwa ni pamoja na ukaguzi wa aina na uboreshaji. Zana kama `kupanua mizigo` huruhusu wasanidi programu kukagua msimbo uliozalishwa, na kutoa uwezo muhimu wa utatuzi wa matatizo wakati wa kutengeneza makro tata.


### Dhana za Macro za Kina na Utatuzi wa Makosa


Ukuzaji wa makro unahitaji kuelewa tofauti kati ya utekelezaji wa muda wa kukusanya na utekelezaji wa wakati wa utekelezaji. Macro hutekeleza wakati wa mkusanyiko, na kutoa msimbo utakaoendeshwa wakati wa utekelezaji. Mgawanyiko huu wa muda unamaanisha kuwa mantiki ya makro haiwezi kutegemea thamani za wakati wa utekelezaji, lakini pia huwezesha uboreshaji ambapo hesabu tata zinaweza kufanywa mara moja wakati wa mkusanyiko badala ya kurudia wakati wa utekelezaji.


Mfumo wa kulinganisha ruwaza katika makro huunga mkono vibainishi mbalimbali vya vipande vinavyofafanua aina ya vipengele vya msimbo vinavyoweza kulinganishwa. Kibainishi cha `expr` kinalinganisha misemo, aina za vilinganishi vya `ty`, vitambulishi vya vilinganishi vya `ident`, na vingine kadhaa hutoa udhibiti mzuri wa uthibitishaji wa ingizo. Vibainishi hivi vinahakikisha kwamba makro hupokea ingizo halali la kisintaksia na hutoa ujumbe wazi wa hitilafu wakati sintaksia batili inapokutana.


Kutatua matatizo ya makro hutoa changamoto za kipekee kutokana na asili yao ya muda wa kukusanya. Amri ya `kupanua mizigo` ni muhimu kwa ajili ya ukuzaji wa makro, kwani inaonyesha msimbo uliopanuliwa kikamilifu unaozalishwa na maombi ya makro. Zana hii inaruhusu wasanidi programu kuthibitisha kwamba makro zao generate msimbo unaokusudiwa na kutambua matatizo katika mantiki ya upanuzi. Wakati msimbo uliozalishwa na makro una hitilafu, matokeo yaliyopanuliwa husaidia kubainisha kama tatizo liko katika ufafanuzi wa makro au muundo wa msimbo uliozalishwa.


Macro changamano zinaweza kutekeleza mifumo ya kujirudia, ambapo makro inajiita yenye hoja zilizorekebishwa ili kushughulikia utengenezaji wa msimbo uliowekwa au unaojirudia. Hata hivyo, makro za kujirudia zinahitaji muundo makini ili kuepuka masuala ya upanuzi usio na kikomo na utendaji wa mkusanyiko. Hali ya upanuzi wa makro kwa wakati wa kukusanya ina maana kwamba hata utekelezaji usiofaa wa makro huathiri tu kasi ya mkusanyiko, si utendaji wa wakati wa utekelezaji, lakini makro changamano kupita kiasi zinaweza kupunguza kasi ya mchakato wa ujenzi kwa kiasi kikubwa.



# Rust na Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Kwa nini Rust kwa Maendeleo ya Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


Uchaguzi wa Rust kwa ajili ya ukuzaji wa Bitcoin na Lightning si bahati mbaya. Ukuzaji wa Bitcoin una majukumu ya kipekee yanayoutofautisha na ukuzaji wa kawaida wa programu. Wakati wa kufanya kazi na Bitcoin, watengenezaji mara nyingi hushughulikia fedha za watumiaji katika mazingira ambapo makosa yanaweza kutoweza kurekebishwa. Tofauti na mifumo ya kifedha ya jadi yenye ulinzi wa udhibiti na mifumo ya kurudisha pesa, asili ya Bitcoin ya kugatuliwa ina maana kwamba mara tu muamala unapotangazwa, hakuna mamlaka ya kukata rufaa kwa ajili ya urejeshaji wa fedha. Ukweli huu unahitaji kiwango cha juu cha uwajibikaji na usahihi katika ukuzaji wa programu.


Falsafa ya "songa haraka na uvunje mambo" inayofanya kazi katika sekta nyingi za teknolojia haitumiki kwa uundaji wa Bitcoin. Badala yake, mfumo ikolojia unahitaji lugha na zana zinazowasaidia watengenezaji kuunda programu imara na salama ambapo hitilafu huzuiwa au kushughulikiwa kwa uzuri. Hii ndiyo sababu miradi mingi maarufu ya Bitcoin imeelekea Rust, ikiwa ni pamoja na Bitcoin Development Kit (BDK), Lightning Development Kit (LDK), na BreezSDK.


Rust inatoa sifa tatu muhimu zinazoifanya iweze kufaa zaidi kwa ajili ya uundaji wa Bitcoin: mfumo thabiti usiobadilika, zana za kisasa zenye utajiri, na utangamano wa mifumo mbalimbali. Kila moja ya sifa hizi huchangia uwezo wa lugha kuwasaidia watengenezaji kuandika msimbo salama na unaoaminika zaidi wa kushughulikia shughuli za sarafu za kidijitali.


### Mfumo wa Aina ya Nguvu Tuli ya Rust


Mfumo wa aina wa Rust hutoa sifa za uandishi tuli na imara zinazofanya kazi pamoja ili kubaini hitilafu kabla hazijawaathiri watumiaji. Hali tuli ina maana kwamba ukaguzi wa aina hutokea wakati wa kukusanya, na kuhitaji wasanidi programu kutatua tofauti za aina kabla hata ya programu kujengwa. Hii inatofautiana na lugha zinazoandikwa kwa njia inayobadilika ambapo hitilafu za aina hujitokeza tu wakati wa utekelezaji, ikiwezekana baada ya programu kusambazwa na inashughulikia fedha halisi za watumiaji.


Nguvu ya mfumo wa aina wa Rust inarejelea uwazi wake na ukali wake katika matatizo ya uundaji wa mifumo. Tofauti na lugha zenye mifumo dhaifu ya aina kama vile C, ambapo wasanidi programu wamewekewa mipaka ya aina za msingi kama vile nambari na miundo, Rust inaruhusu uundaji wa mifumo tajiri ambayo inaweza kuwakilisha dhana changamano za kikoa kwa usahihi. Kwa mfano, unaweza kuunda aina zinazotofautisha kati ya aina tofauti za orodha au kulazimisha kwamba shughuli fulani zinafanywa tu kwenye aina maalum za vitu.


Kinachofanya mfumo wa aina wa Rust kuwa muhimu kwa ajili ya uundaji wa Bitcoin ni mbinu yake ya usalama wa kumbukumbu. Mfumo wa aina hiyo hiyo unaounda mantiki ya biashara pia hushughulikia umiliki wa kumbukumbu na udhibiti wa ufikiaji wa pamoja. Jukumu hili maradufu linamaanisha kwamba makundi ya kawaida ya udhaifu, kama vile uvujaji wa kumbukumbu, makosa yasiyo na kikomo, na hali ya mbio, huondolewa kabisa na mkusanyaji. Mfumo wa aina hutekeleza dhamana hizi za usalama kupitia dhana kama vile umiliki, kukopa, na kuhesabu marejeleo, na kufanya iwe vigumu sana kuanzisha hitilafu zinazohusiana na kumbukumbu ambazo zinaweza kuhatarisha usalama au utulivu.


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


### Usaidizi wa Vifaa vya Kisasa na Jukwaa Mtambuka


Mfumo wa vifaa wa Rust huwapa watengenezaji zana zinazosaidia katika uzalishaji na ubora wa msimbo. Kikusanyaji cha Rust chenyewe kimeundwa sio tu kutafsiri msimbo katika umbo la jozi, bali kutumika kama zana ya kielimu inayowasaidia watengenezaji kujifunza na kuboresha. Wakati makosa ya mkusanyiko yanapotokea, kikusanyaji hutoa maelezo ya kina ya kile kilichoenda vibaya na mara nyingi hupendekeza marekebisho maalum. Mbinu hii ni muhimu sana kwa watengenezaji wapya wa Rust, kwani kikusanyaji hufundisha kwa ufanisi mazoea mazuri na husaidia kuzuia makosa ya kawaida.


Lugha hiyo inajumuisha Cargo, meneja wa vifurushi vilivyounganishwa vinavyoshughulikia usimamizi wa utegemezi, ujenzi, upimaji, na utengenezaji wa nyaraka. Usanifishaji huu huondoa mgawanyiko unaoonekana katika lugha za zamani kama vile C++, ambapo zana nyingi zinazoshindana huunda kutolingana katika miradi. Cargo pia inasaidia viendelezi kama vile rustfmt kwa uundaji wa msimbo na Clippy kwa uchanganuzi tuli, kuhakikisha kwamba msimbo unafuata miongozo thabiti ya mtindo na kushughulikia masuala yanayoweza kutokea kabla hayajawa matatizo.


Uwezo wa Rust wa mifumo mbalimbali hupanua zaidi ya mifumo ya uendeshaji ya kitamaduni hadi kujumuisha mifumo ya simu kama vile Android na iOS, pamoja na WebAssembly kwa programu zinazotegemea kivinjari. Usaidizi huu wa mifumo mbalimbali ni muhimu kwa programu za Bitcoin zinazohitaji kuendeshwa katika mazingira mbalimbali. Kwa mfano, miradi kama Mutiny Wallet hutumia mkusanyiko wa WebAssembly wa Rust ili kuunda pochi za Lightning zinazoendeshwa moja kwa moja kwenye vivinjari vya wavuti, jambo ambalo halingewezekana kwa teknolojia za jadi za wavuti pekee.


### Kuelewa Aina za Makosa na Matokeo Yake


Ushughulikiaji mzuri wa hitilafu huanza kwa kuelewa kategoria tofauti za hitilafu zinazoweza kutokea wakati wa utekelezaji wa programu. Fikiria programu rahisi ya uelekezaji inayohesabu njia kati ya sehemu za kijiografia. Mfano huu unaonyesha aina tatu za msingi za hitilafu ambazo wasanidi programu lazima wazishughulikie: hitilafu batili za ingizo, hitilafu za rasilimali za wakati wa utekelezaji, na hitilafu za mantiki.


Hitilafu batili za kuingiza hutokea wakati chaguo la kazi linapokea vigezo ambavyo havikidhi mahitaji yake. Kwa mfano, ikiwa mfumo wa uratibu wa kijiografia hutumia nambari kamili zilizosainiwa kwa longitudo lakini hupokea thamani hasi ambapo thamani chanya pekee ndizo halali, chaguo la kazi haliwezi kuendelea kwa maana. Hitilafu hizi zinawakilisha ukiukaji wa mkataba kati ya mpigaji simu na chaguo la kazi, na jibu linalofaa kwa kawaida ni kukataa ingizo na kurudisha dalili ya hitilafu.


Hitilafu za rasilimali za wakati wa utekelezaji hutokea wakati utegemezi wa nje haupatikani au haupatikani. Kusoma faili ya ramani kunaweza kushindwa kwa sababu faili haipo, programu haina ruhusa zinazofaa, au kifaa cha kuhifadhi hakipatikani. Hitilafu hizi ni nje ya mantiki ya programu na mara nyingi zinahitaji marekebisho ya kimazingira badala ya mabadiliko ya msimbo. Hata hivyo, programu thabiti lazima zitabiri na kushughulikia matukio haya kwa uzuri.


Makosa ya kimantiki yanawakilisha hitilafu katika utekelezaji wa programu au kutoelewana kuhusu jinsi vipengele vinavyoingiliana. Ikiwa algoriti ya uelekezaji inarudisha njia tupu inapopewa sehemu halali za kuanza na mwisho, hii inaonyesha dosari ya kimantiki ambayo inahitaji kusahihishwa katika msimbo wenyewe. Tofauti na aina zingine za hitilafu, makosa ya kimantiki kwa kawaida huhitaji utatuzi na urekebishaji wa msimbo ili kutatua.


### Mikakati ya Usimamizi wa Makosa Imara


Kujenga programu inayoaminika kunahitaji mikakati makini inayopunguza fursa za makosa na kushughulikia makosa yasiyoepukika kwa uzuri. Mkakati wa kwanza unahusisha kupunguza makosa yanayowezekana kupitia muundo makini wa aina. Kwa kuchagua aina ambazo zinaweza kuwakilisha thamani halali pekee, wasanidi programu wanaweza kuondoa madarasa yote ya makosa batili ya ingizo. Kwa mfano, kutumia nambari kamili ambazo hazijasainiwa kwa thamani ambazo haziwezi kuwa hasi huzuia makosa hasi ya thamani wakati wa kukusanya.


Madai hutoa safu nyingine ya ulinzi kwa kuangalia waziwazi kwamba hali zinazotarajiwa zinatimia wakati wa utekelezaji wa programu. Ukaguzi huu unatimiza madhumuni mengi: unakamata hitilafu wakati wa majaribio, husababisha programu kushindwa mapema matatizo yanapotokea (kufanya utatuzi kuwa rahisi), na hutumika kama nyaraka zinazoweza kutekelezwa zinazoelezea mawazo ya msanidi programu. Madai yanaposhindwa, yanaonyesha kwamba dhana ya msingi kuhusu hali ya programu imekiukwa, kwa kawaida ikiashiria hitilafu ya kimantiki inayohitaji uchunguzi.


Kanuni ya ufupisho wa tabaka husaidia kudhibiti ugumu kwa kuhakikisha kwamba makosa yanashughulikiwa katika viwango vinavyofaa vya mfumo. Maelezo ya utekelezaji wa ndani, ikiwa ni pamoja na aina maalum za makosa kutoka maktaba za ngazi ya chini, hayapaswi kusambaa zaidi ya mipaka ya mfumo mdogo. Badala yake, kila safu inapaswa kutafsiri makosa katika maneno yenye maana katika kiwango hicho cha ufupisho. Kwa mfano, programu ya wallet inayotumia maktaba ya Bitcoin inapaswa kutafsiri makosa ya uchanganuzi wa maelezo ya kiwango cha chini kuwa ujumbe wa ngazi ya juu kama vile "usanidi batili wa wallet" ambao hutoa taarifa zinazoweza kutekelezwa kwa watumiaji au msimbo wa kupiga simu.


Mbinu hii ya kushughulikia makosa, pamoja na mfumo wa aina ya Rust na vifaa, husaidia kubaini matatizo yanayoweza kutokea mapema katika mchakato wa usanidi, kabla hayajaathiri watumiaji au kuhatarisha usalama wa programu za Bitcoin.



## Mfano wa hitilafu

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust hutoa mbinu kamili ya kushughulikia makosa ambayo husawazisha usalama na utendakazi. Ingawa dhana za jumla za modeli ya makosa zinatumika katika lugha za programu, Rust hutoa zana na mifumo maalum ambayo hufanya kushughulikia makosa kuwa wazi na rahisi kudhibiti. Kuelewa mifumo hii ni muhimu kwa kuandika programu thabiti za Rust ambazo zinaweza kushughulikia hali zisizotarajiwa kwa uzuri huku zikidumisha utendaji na usalama.


### Hofu na Matumizi Yake Yanayofaa


Utaratibu wa hofu wa Rust unawakilisha njia ya moja kwa moja zaidi ya kushughulikia hitilafu zisizoweza kurejeshwa. Unapoita makro ya `panic!`, programu husimamisha utekelezaji mara moja, ama kuacha au kufungua kulingana na usanidi wako. Macro ya hofu hukubali ujumbe wa kamba unaoelezea kilichokwenda vibaya, na kutoa muktadha wa utatuzi wa matatizo. Zaidi ya hayo, mbinu kama `unwrap()` na `expect()` kwenye aina za Matokeo na Chaguo hutumika kama njia za mkato za hofu wakati aina hizi zina thamani za hitilafu au Hakuna mtawalia. Mbinu ya `expect()` hukuruhusu kutoa ujumbe maalum, na kuifanya iwe na taarifa zaidi kidogo kuliko `unwrap()` wakati wa utatuzi wa matatizo.


Licha ya unyenyekevu wake, hofu inapaswa kutumika kwa busara katika msimbo wa uzalishaji. Kuna matukio kadhaa ambapo hofu haikubaliki tu bali inapendekezwa. Wakati wa kuandika mifano au mifano, hofu hutoa njia safi ya kuzingatia utendaji kazi mkuu bila kujumuisha msimbo kwa kushughulikia makosa kwa kina. Katika mazingira ya majaribio, hofu mara nyingi ni tabia inayotakiwa wakati madai yanashindwa, kwani inaonyesha wazi kwamba jambo lisilotarajiwa lilitokea. Jumuiya ya Rust pia inatambua hali ambapo wasanidi programu wana ujuzi zaidi kuliko mkusanyaji, kama vile wakati wa kuchanganua anwani za IP zenye msimbo mgumu ambazo zinajulikana kuwa halali.


Hata hivyo, usalama unaoonekana wa hofu "zilizothibitishwa na mkusanyaji" unaweza kuwa wa kudanganya. Fikiria hali ambapo unaweka msimbo mgumu kwenye anwani ya IP na kutumia `expect()` kwa sababu unajua ni halali. Baada ya muda, kadri msimbo unavyobadilika, thamani hiyo ngumu inaweza kubadilishwa kuwa nambari isiyobadilika, na baadaye nambari hiyo inaweza kubadilishwa kuwa kitu kama "localhost" kwa uzoefu bora wa mtumiaji. Ghafla, hofu yako "salama" inakuwa hitilafu ya wakati wa utekelezaji. Mageuzi haya yanaonyesha kwa nini kwa ujumla ni bora kuepuka hofu katika msimbo wa uzalishaji na badala yake kurudisha aina sahihi za hitilafu ambazo zinaweza kushughulikiwa kwa uzuri.


Isipokuwa moja muhimu kwa sheria ya "epuka hofu" inahusisha shughuli za mutex. Unapoita `lock()` kwenye mutex, inarudisha Matokeo kwa sababu kufuli kunaweza kushindwa ikiwa uzi mwingine utaingiwa na hofu wakati unashikilia mutex. Hii inaunda hali ya kutatanisha ambapo msimbo wako wa ndani hupokea hitilafu kwa jambo lililotokea katika muktadha tofauti kabisa. Kwa kuwa huwezi kushughulikia hitilafu iliyotokana na hofu ya uzi mwingine, watengenezaji wengi wanaona kuwa inakubalika kufungua kufuli za mutex, haswa ikiwa unadumisha msingi wa msimbo usio na hofu mahali pengine.


### Kufanya Kazi na Aina za Matokeo na Chaguo


Aina ya Matokeo huunda uti wa mgongo wa mfumo wa kushughulikia hitilafu wa Rust. Kama enum inayoweza kushikilia `Sawa(thamani)` au `Err(kosa)`, Matokeo yanakulazimisha kukubali waziwazi kwamba shughuli zinaweza kushindwa. Aina ya Chaguo hutumika sawa kwa hali ambapo thamani inaweza kuwa haipo, ikiwa na `Baadhi(thamani)` au `Hakuna`. Ingawa Chaguo haitoi taarifa za kina za hitilafu, ni kamili kwa hali ambapo kutokuwepo kwa thamani kuna maana na kunatarajiwa.


Matokeo na Chaguo zote mbili hutoa mbinu kadhaa za matumizi ambazo hufanya utunzaji wa makosa kuwa wa ergonomic zaidi. Mbinu ya `unwrap_or()` inarudisha thamani iliyomo ikiwa ipo, au thamani chaguo-msingi ikiwa kuna hitilafu au Hakuna. Muundo huu ni muhimu hasa unapokuwa na njia mbadala inayofaa, kama vile kuchanganua ingizo la mtumiaji kwa chaguo-msingi linaloeleweka wakati uchanganuzi unashindwa. Mbinu ya `unwrap_or_default()` inafanya kazi vivyo hivyo lakini hutumia thamani chaguo-msingi ya aina badala ya kukuhitaji kutaja moja. Ingawa mbinu hizi hazishughulikii makosa kitaalamu kwa maana ya kitamaduni, hutoa njia ya kuharibu utendaji kwa uzuri wakati matatizo yanapotokea.


Kiendeshaji cha alama ya kuuliza (`?`) ni sintaksia fupi ya uenezaji wa makosa. Inapotumika kwenye Matokeo au Chaguo, huondoa thamani ya mafanikio ikiwa ipo, au hurejesha mara moja kosa kutoka kwa chaguo la sasa ikiwa kuna tatizo. Kiendeshaji hiki huondoa mifumo ya kukagua makosa ya kitenzi ambayo ni ya kawaida katika lugha kama Go, ambapo lazima uangalie mwenyewe na urudishe makosa katika kila hatua. Kiendeshaji cha alama ya kuuliza kimsingi hutoa sukari ya kisintaksia kwa marejesho ya mapema, ikikuruhusu kuandika msimbo safi, wa mstari unaozingatia njia ya furaha huku ukishughulikia kiotomatiki uenezaji wa makosa.


### Mifumo ya Kina ya Kushughulikia Makosa


Mbinu ya `map()` kwenye aina za Matokeo na Chaguo huwezesha utunzaji wa hitilafu za mtindo wa kiutendaji ambazo zinaweza kufanya msimbo kuwa wa kuelezea zaidi na wa kutunga. Unapoita `map()` kwenye Matokeo, chaguo-msingi lililotolewa hutumika kwa thamani ya mafanikio ikiwa ipo, huku hitilafu zikienezwa kiotomatiki bila marekebisho. Muundo huu ni muhimu wakati wa kuunganisha shughuli, kwani unaweza kuzingatia kubadilisha thamani bila kushughulikia visa vya hitilafu mara kwa mara. Mbinu ya `map_err()` hutoa utendaji kinyume, hukuruhusu kubadilisha aina za hitilafu huku ukiacha thamani za mafanikio bila kubadilika.


Mabadiliko ya hitilafu huwa muhimu wakati wa kujenga programu zenye tabaka ambapo vipengele tofauti vinahitaji aina tofauti za hitilafu. Fikiria kitendakazi kinachochanganua ingizo la mtumiaji na kinahitaji kubadilisha makosa ya uchanganuzi wa kiwango cha chini kuwa makosa mahususi ya kikoa. Kwa kutumia `map_err()`, unaweza kutafsiri kwa urahisi hitilafu ya jumla ya "muundo batili wa nambari" kuwa hitilafu ya "umri batili" ya muktadha zaidi ambayo inaeleweka ndani ya kikoa cha programu yako. Mabadiliko haya hutokea pale tu ambapo hitilafu hutokea, na kufanya msimbo usomeke zaidi na kudumishwa kuliko vitalu vya kawaida vya kujaribu-kukamata ambapo utunzaji wa hitilafu hutenganishwa na shughuli ambazo zinaweza kushindwa.


Mchanganyiko wa kiendeshaji cha alama ya kuuliza na ramani ya makosa huunda mifumo mifupi ya kushughulikia makosa. Unaweza kuratibu shughuli, kubadilisha makosa inavyohitajika, na kuyaeneza kwenye rundo la simu kwa kutumia kiwango kidogo cha boilerplate. Mbinu hii huweka utunzaji wa makosa karibu na shughuli ambazo zinaweza kushindwa huku ikidumisha utengano safi kati ya njia za mafanikio na makosa.


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


### Maktaba za Nje na Mifumo ya Ikolojia ya Kushughulikia Makosa


Mfumo ikolojia wa Rust unajumuisha maktaba kadhaa maarufu zinazopanua uwezo wa kushughulikia makosa wa maktaba ya kawaida. Maktaba ya `anyhow` hutoa mbinu rahisi ya kushughulikia makosa kwa kutoa aina ya makosa ya jumla ambayo inaweza kubadilisha kiotomatiki kutoka kwa aina yoyote ya makosa ambayo hutekeleza sifa ya kawaida ya Hitilafu. Ubadilishaji huu otomatiki hukuruhusu kutumia kiendeshaji cha alama ya kuuliza na aina tofauti za makosa bila ubadilishaji wa mwongozo, na kuifanya iwe muhimu sana kwa programu ambapo huhitaji kutofautisha kiprogramu kati ya aina tofauti za makosa.


Ingawa `anyhow` ina sifa nzuri katika kurahisisha utunzaji wa makosa kwa programu ambapo makosa huonyeshwa kwa watumiaji, ina mapungufu katika uundaji wa maktaba. Kwa kuwa `anyhow` kimsingi hubadilisha makosa yote kuwa ujumbe wa kamba, watumiaji wa maktaba yako hawawezi kujibu kwa urahisi kwa hali tofauti za makosa kiprogramu. Kikwazo hiki hufanya `anyhow` kufaa zaidi kwa programu za watumiaji wa mwisho kuliko maktaba zinazohitaji kutoa taarifa za makosa zilizopangwa kwa watumiaji wao.


Mbinu za hali ya juu zaidi za kushughulikia hitilafu zinahusisha kuunda aina maalum za hitilafu zinazounda mfumo maalum wa hitilafu za programu au maktaba yako. Mfumo wa hitilafu ulioundwa vizuri unaweza kutofautisha kati ya ingizo batili (ambalo mpigaji anaweza kurekebisha), hitilafu za wakati wa utekelezaji (ambazo zinaweza kujaribiwa tena), na hitilafu za kudumu (ambazo zinaonyesha hitilafu au hali ambazo haziwezi kurejeshwa). Mbinu hii iliyopangwa inawawezesha watumiaji wa msimbo wako kufanya maamuzi ya busara kuhusu jinsi ya kujibu aina tofauti za hitilafu, iwe hiyo inamaanisha kujaribu tena shughuli, kuwashawishi watumiaji kwa ingizo tofauti, au kuripoti hitilafu kwa watengenezaji programu.


## UniFFI, Kuunganisha Maktaba za Rust na Lugha Nyingi


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Utangulizi wa UniFFI na Maendeleo ya Jukwaa Mtambuka


UniFFI ni zana ya kufanya maktaba za Rust zipatikane katika lugha na majukwaa mengi ya programu. Iliyotengenezwa na Mozilla, zana hii inashughulikia changamoto ya msingi katika ukuzaji wa programu za kisasa: jinsi ya kutumia faida za utendaji na usalama za Rust huku ikidumisha utangamano na mifumo ikolojia mbalimbali ya maendeleo. Chombo hiki huzalisha kiotomatiki vifungo vya lugha kwa maktaba za Rust, na kuondoa hitaji la watengenezaji kuunda msimbo wa kiolesura kwa kila lugha lengwa.


Tatizo kuu ambalo UniFFI hutatua linatokana na asili ya Rust kama lugha iliyokusanywa. Wakati msimbo wa Rust unapokusanywa, hutoa matokeo ya binary yenye Foreign Function Interface (FFI) ambayo inatoa kiolesura cha kiwango cha chini ambacho kinaweza kuwa changamoto kutumia moja kwa moja kutoka kwa lugha za kiwango cha juu kama Python, Swift, au Kotlin. Kijadi, kila msanidi programu wa maktaba angehitaji kuandika msimbo maalum wa kufunga kwa kila lugha lengwa, na kuunda kizuizi kikubwa kwa utumiaji wa mifumo mbalimbali. UniFFI huondoa upungufu huu kwa kutoa mbinu sanifu ya kuzalisha vifungo hivi kiotomatiki.


Falsafa ya muundo wa kifaa hiki inalenga kuwawezesha watengenezaji wa Rust kuzingatia mantiki yao ya msingi ya biashara huku wakifanya maktaba zao zipatikane kwa watengenezaji wanaofanya kazi katika lugha zingine. Kwa mfano, msanidi programu wa iOS anayetumia Swift anaweza kutumia maktaba ya Rust kupitia vifungo vilivyotengenezwa na UniFFI ambavyo vinawasilisha kiolesura asilia cha Swift, bila dalili kwamba utekelezaji wa msingi umeandikwa katika Rust. Muunganisho huu usio na mshono huruhusu timu kutumia faida za utendaji za Rust bila kuwataka wanachama wote wa timu kujifunza Rust.


### Kuelewa Usanifu na Mtiririko wa Kazi wa UniFFI


UniFFI hufanya kazi kupitia mtiririko wa kazi uliofafanuliwa vizuri unaobadilisha maktaba za Rust kuwa vifurushi vinavyooana na lugha nyingi. Mchakato huanza na uundaji wa faili ya Unified Definition Language (UDL), ambayo hutumika kama vipimo vya kiolesura vinavyoelezea ni sehemu gani za maktaba yako ya Rust zinapaswa kufichuliwa kwa lugha zingine. Faili hii ya UDL hufanya kazi kama mkataba kati ya utekelezaji wako wa Rust na vifungo vya lugha vilivyozalishwa.


Usanifu huu unafuata mgawanyo dhahiri wa masuala. Wasanidi programu hudumisha maktaba yao ya Rust yenye nahau na mifumo ya kawaida ya Rust, kisha huunda faili tofauti ya UDL inayounganisha kiolesura cha umma na mfumo wa aina wa UniFFI. Kijenereta cha kufunga cha UniFFI huchakata maktaba ya Rust na vipimo vya UDL ili kutoa vifungo vya lugha asilia kwa majukwaa lengwa yaliyoombwa. Vifungo hivi vilivyozalishwa hushughulikia upangaji na utenganishaji wote tata wa data kati ya muda wa utekelezaji wa lugha ya kigeni na msimbo wa Rust.


Wakati wa utekelezaji, usanifu huunda mbinu yenye tabaka ambapo msimbo wa programu ulioandikwa katika lugha lengwa (kama vile Kotlin kwa Android) huingiliana na msimbo wa kufunga unaozalishwa ambao unaonekana asili kabisa ya lugha hiyo. Safu hii ya kufunga hushughulikia tafsiri kati ya aina maalum za lugha na aina za Rust, hudhibiti kumbukumbu kwa usalama kuvuka mipaka ya lugha, na hutoa utunzaji wa makosa unaofuata kanuni za lugha lengwa. Mantiki ya biashara ya msingi ya Rust bado haijabadilika na haijui violesura vingi vya lugha vilivyojengwa juu yake.


### Kufanya kazi na UDL: Ufafanuzi wa Interface na Ramani ya Aina


Lugha ya Ufafanuzi Uliounganishwa hutumika kama msingi wa utendaji kazi wa UniFFI, ikitoa njia ya kubainisha ni sehemu gani za maktaba ya Rust zinapaswa kufichuliwa na jinsi zinapaswa kuwasilishwa katika lugha lengwa. Faili za UDL lazima ziwe na angalau nafasi moja ya majina, ambayo hufanya kazi kama chombo cha chaguo ambazo zinaweza kuitwa moja kwa moja bila kuhitaji uanzishaji wa kitu. Chaguo hizi za nafasi ya majina kwa kawaida hushughulikia shughuli rahisi ambazo huchukua thamani kama vigezo na matokeo ya kurudisha.


UDL inasaidia seti kamili ya aina zilizojengewa ndani ambazo huunganishwa kiasili na aina zinazolingana za Rust. Aina za msingi zinajumuisha primitives za kawaida kama vile booleans, ukubwa mbalimbali wa nambari kamili (u8, u32, nk), nambari za nukta zinazoelea, na nyuzi. Aina ngumu zaidi ni pamoja na vekta, ramani za hash, na dhana maalum za Rust kama vile aina za Chaguo (zinazowakilishwa na sintaksia ya alama ya swali) na aina za Matokeo kwa ajili ya kushughulikia hitilafu. Mfumo wa aina pia unaunga mkono hesabu, enums rahisi zinazotegemea thamani na enums changamano ambazo zina data inayohusiana, kuruhusu uundaji wa data unaotafsiri kuvuka mipaka ya lugha.


Miundo katika Rust hutafsiriwa kuwa kamusi katika UDL, ikidumisha mawasiliano ya karibu moja hadi moja huku ikibadilika kulingana na kanuni za sintaksia za UDL. Wakati miundo ya Rust ina mbinu zinazohusiana, zinaweza kufichuliwa kama violesura katika UDL, ambavyo generate kama madarasa yenye mbinu katika lugha lengwa zinazolenga kitu kama Kotlin au Swift. Ramani hii huhifadhi mifumo ya muundo inayolenga kitu ambayo watengenezaji wanatarajia katika lugha hizi huku ikidumisha muundo na tabia ya utekelezaji wa Rust.


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


Utekelezaji sambamba wa Rust ungefafanua aina hizi na kutekeleza sifa ya `uniffi::export` kwa vifungo vya generate kwa Kotlin, Swift, Python, na lugha zingine zinazoungwa mkono.


### Ushughulikiaji wa Makosa na Vipengele vya Kina


UniFFI hutoa utunzaji wa hitilafu unaohifadhi mfumo wa hitilafu unaotegemea Matokeo wa Rust huku ukiutafsiri ipasavyo kwa lugha lengwa. Vitendakazi vinavyorudisha aina za Matokeo katika Rust vinaweza kuwekwa alama na neno muhimu la "throws" katika UDL, na kubainisha ni aina gani za hitilafu ambazo zinaweza kutoa. Makosa haya lazima yafafanuliwe kama enums za hitilafu katika faili ya UDL na lazima yatekeleze sifa ya kawaida ya Hitilafu ya Rust katika msimbo wa msingi wa Rust. Kreti ya hitilafu hii hutoa makro rahisi ya kutekeleza sifa hii, na kupunguza msimbo wa boilerplate kwa kiasi kikubwa.


Tafsiri ya kushughulikia makosa inaonyesha mbinu ya UniFFI inayofahamu lugha. Katika Kotlin, vitendakazi vilivyowekwa alama kama kutupa mbinu za UDL generate ambazo hutoa vighairi kufuatia kanuni za Java/Kotlin. Vifungashio vya Python vile vile hutumia mfumo wa vighairi wa Python. Tafsiri hii inahakikisha kwamba kushughulikia makosa kunahisi kuwa kwa kawaida na kwa lugha lengwa huku ikihifadhi maana ya kisemantiki ya aina asilia za hitilafu za Rust.


Violesura vya kurudisha simu vinawakilisha kipengele kingine cha hali ya juu kinachowezesha mawasiliano ya pande mbili kati ya maktaba za Rust na programu zinazotumia. Wakati maktaba ya Rust inahitaji kurudisha simu kwenye msimbo wa programu, wasanidi programu wanaweza kufafanua sifa katika Rust na kuziweka alama kama violesura vya kurudisha simu katika UDL. Programu inayotumia hutumia violesura hivi katika lugha yao ya asili, na UniFFI hushughulikia uratibu tata unaohitajika ili kutumia violesura hivi kutoka kwa msimbo wa Rust. Muundo huu unahitaji kuzingatia kwa makini usalama wa nyuzi, kwani violesura vinaweza kuvuka mipaka ya nyuzi, na hivyo kuhitaji mipaka ya Kutuma na Kusawazisha upande wa Rust.


### Matumizi Halisi ya Ulimwengu na Mapungufu ya Sasa


UniFFI imepitishwa katika jumuiya ya maendeleo ya sarafu za kidijitali na blockchain, huku miradi mikubwa kama vile BDK (Bitcoin Development Kit), LDK (Lightning Development Kit), na utekelezaji mbalimbali wa wallet ukiitumia kutoa SDK za simu. Miradi hii inaonyesha matumizi ya UniFFI katika mazingira ya uzalishaji.


Kuchunguza faili za UDL za ulimwengu halisi kutoka kwa miradi hii kunaonyesha mifumo na mbinu bora ambazo zimeibuka kutokana na matumizi ya vitendo. Faili ya UDL ya BDK, kwa mfano, inaonyesha jinsi mifumo changamano ya kikoa yenye enum, structs, na interfaces nyingi zinaweza kupangwa kwa ufanisi ili kuunda SDK kamili za simu. Uthabiti wa sintaksia ya UDL katika miradi tofauti inamaanisha kwamba wasanidi programu wanaofahamu maktaba moja inayowezeshwa na UniFFI wanaweza kuelewa na kufanya kazi na wengine haraka, na kuunda athari ya mtandao inayofaidi mfumo mzima wa ikolojia.


Hata hivyo, UniFFI ina mapungufu yanayoonekana ambayo watengenezaji lazima wazingatie. Muhimu zaidi ni ukosefu wa usaidizi wa violesura visivyo na ulinganifu. Viungo vyote vinavyozalishwa ni vya usawazishaji, na hivyo kuwahitaji watengenezaji kushughulikia shughuli zisizo na ulinganifu ndani ya msimbo wao wa Rust na kuwasilisha violesura vinavyolingana kwa matumizi ya programu. Zaidi ya hayo, uwekaji wa nyaraka unaleta changamoto: nyaraka zilizoandikwa katika msimbo wa Rust hazihamishiwi kwenye viungo vinavyozalishwa, huku nyaraka katika faili za UDL zikiwa hazipatikani kuwaelekeza watumiaji wa Rust wa maktaba. Ingawa kuna juhudi zinazoendelea za kushughulikia mapungufu haya kupitia uchanganuzi na uzalishaji kiotomatiki, zinabaki kuwa mambo ya kuzingatia kwa utekelezaji wa sasa. Hatimaye, UniFFI hutoa viungo vya lugha lakini haishughulikii ufungashaji na usambazaji maalum wa jukwaa, na kuwaacha watengenezaji kusimamia hatua za mwisho za kuunda vifurushi vinavyoweza kusambazwa kwa kila jukwaa lengwa.


# Kuendeleza LNP/BP kwa kutumia SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## Nodi ya LN kwenye SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### Kuelewa Usanifu wa Moduli wa LDK


Kifaa cha Ukuzaji wa Umeme (LDK) kinatumia mbinu tofauti ya utekelezaji wa Lightning Network ikilinganishwa na programu ya nodi za kitamaduni kama vile CLightning au LND. Ingawa nodi za kawaida za Umeme hufanya kazi kama programu kamili za daemon zinazoendelea kwenye mashine, LDK hufanya kazi kama maktaba ya moduli ya Rust ambayo hutoa vipengele vya awali vya kujenga suluhisho maalum za Umeme. Tofauti hii ya usanifu hufanya LDK iwe rahisi kubadilika, ikiruhusu watengenezaji kukusanya utendakazi wa Umeme kwa njia zinazokidhi mahitaji yao maalum ya mradi.


Falsafa kuu ya LDK inazingatia modularity na ubadilikaji. Badala ya kutoa suluhisho la monolithic, LDK hutoa vipengele vya kibinafsi ambavyo vinaweza kuunganishwa, kubinafsishwa, au kubadilishwa kabisa. Kila kipengele huja na utekelezaji chaguo-msingi unaofanya kazi nje ya boksi, lakini watengenezaji huhifadhi uhuru wa kubadilisha utekelezaji wao wenyewe inapohitajika. Kwa mfano, LDK inajumuisha utekelezaji chaguo-msingi wa ufuatiliaji wa blockchain, utiaji saini wa miamala, na mawasiliano ya mtandao, lakini yoyote kati ya haya yanaweza kubadilishwa na suluhisho maalum zilizoundwa kwa hali au mazingira maalum ya matumizi.


Muundo huu wa moduli huwezesha LDK kufanya kazi katika majukwaa na hali mbalimbali ambazo zingekuwa changamoto kwa nodi za jadi za Umeme. Programu za simu, vivinjari vya wavuti, vifaa vilivyopachikwa, na vifaa maalum vyote vinaweza kutumia vipengele vya LDK kwa njia zinazokidhi vikwazo na mahitaji yao ya kipekee. Usanifu wa maktaba unahakikisha kwamba watengenezaji wanaweza kuunda programu zinazowezeshwa na Umeme bila kufungwa katika mifumo ya uendeshaji iliyopangwa mapema au utegemezi wa mfumo.


### Kesi za Matumizi ya LDK na Unyumbufu wa Jukwaa


Unyumbufu wa usanifu wa LDK hufungua matumizi mengi ambayo yanaenea zaidi ya uwekaji wa nodi za kawaida za Lightning. Uundaji wa wallet ya Simu unawakilisha mojawapo ya programu zinazovutia zaidi, ambapo LDK huwezesha uundaji wa pochi za Lightning zisizohifadhiwa sawa na Phoenix wallet. Utekelezaji huu wa simu unaweza kudumisha udhibiti wa mtumiaji juu ya funguo za kibinafsi huku ukilinganisha na Watoa Huduma za Lightning (LSPs) wanapoingia mtandaoni, kuruhusu upokeaji wa malipo usio na mshono na usimamizi wa chaneli hata kwa muunganisho wa muda mfupi.


Muunganisho wa Moduli ya Usalama wa Vifaa (HSM) unaonyesha matumizi mengine yenye nguvu kwa LDK. Kwa kutoa vipengele vya utiaji saini na uthibitishaji wa miamala pekee, wasanidi programu wanaweza kuunda vifaa vya utiaji saini vinavyofahamu Umeme vinavyoelewa muktadha na athari za miamala ya Umeme. Uwezo huu unazidi utiaji saini rahisi wa miamala ili kujumuisha uchanganuzi wa busara wa usambazaji wa malipo, shughuli za njia, na maamuzi muhimu ya usalama. HSM inaweza kutathmini kama muamala unawakilisha malipo halali, operesheni ya uelekezaji, au jaribio linaloweza kuwa na nia mbaya, na kuwapa watumiaji maarifa ya usalama yenye maana.


Programu za Lightning zinazotegemea Wavuti hunufaika pakubwa na falsafa ya muundo wa mfumo usiotumia simu ya LDK. Kwa kuwa mazingira ya WebAssembly hayana ufikiaji wa moja kwa moja kwa rasilimali za mfumo kama vile mifumo ya faili, soketi za mtandao, au vyanzo vya entropy, mbinu safi ya LDK inaruhusu utendaji wa Lightning kufanya kazi vizuri katika mazingira ya kivinjari. Wasanidi programu wanaweza kutekeleza tabaka maalum za mitandao kwa kutumia WebSockets na kutoa vyanzo vya kudumu na nasibu vinavyoendana na kivinjari huku wakidumisha utiifu kamili wa itifaki ya Lightning.


### Vipengele vya Msingi na Usanifu Unaoendeshwa na Matukio


Usanifu wa ndani wa LDK unazunguka vipengele kadhaa muhimu vinavyofanya kazi pamoja kupitia mfumo unaoendeshwa na matukio. Mfumo wa usimamizi wa rika hushughulikia mawasiliano yote na nodi zingine za Umeme, kutekeleza itifaki ya kelele kwa ajili ya usimbaji fiche na kusimamia miundo ya ujumbe kwa ajili ya kufuata itifaki ya Umeme. Sehemu hii hufanya kazi bila kujali utaratibu wa msingi wa usafirishaji, ikiruhusu wasanidi programu kutekeleza mitandao kupitia soketi za TCP, WebSockets, miunganisho ya serial ya USB, au njia nyingine yoyote ya mawasiliano ya pande mbili.


Meneja wa chaneli hutumika kama mratibu mkuu wa shughuli za chaneli za Lightning, akifanya kazi kwa karibu na meneja rika kutekeleza shughuli za kufungua, kufunga, na malipo ya chaneli. Msanidi programu anapoanzisha ufunguzi wa chaneli, meneja wa chaneli huunda ujumbe muhimu wa itifaki na huratibu na meneja rika ili kushughulikia mchakato wa mazungumzo ya hatua nyingi. Mgawanyiko huu wa wasiwasi huruhusu ufupisho safi kati ya mantiki ya itifaki ya Lightning na maelezo ya mawasiliano ya mtandao.


Mfumo wa matukio wa LDK hutoa arifa zisizo na mpangilio kwa shughuli zote muhimu na mabadiliko ya hali. Matukio hufunika wigo mzima wa shughuli za Lightning, kuanzia miunganisho ya wenzao na miunganisho hadi mafanikio na kushindwa kwa malipo, mabadiliko ya hali ya chaneli, na uthibitisho wa blockchain. Mbinu hii inayoendeshwa na matukio huruhusu programu kujibu ipasavyo shughuli za mtandao wa Lightning huku ikidumisha utengano safi kati ya utendaji kazi mkuu wa LDK na mantiki mahususi ya programu. Wasanidi programu wanaweza kutekeleza vidhibiti maalum vya matukio vinavyosasisha violesura vya watumiaji, kusababisha arifa, au kuanzisha vitendo vya ufuatiliaji kulingana na matukio ya mtandao wa Lightning.


### Ujumuishaji na Usimamizi wa Data wa Blockchain


Ujumuishaji wa data wa Blockchain unawakilisha mojawapo ya tabaka za ufupisho za LDK, iliyoundwa ili kutoshea kila kitu kuanzia nodi kamili za Bitcoin hadi wateja wepesi wa simu. LDK inasaidia aina mbili kuu za mwingiliano wa blockchain, kila moja ikiwa imeboreshwa kwa vikwazo tofauti vya rasilimali na mahitaji ya uendeshaji. Hali kamili ya blockchain inaruhusu programu zenye ufikiaji wa data kamili ya blockchain kupitisha vitalu vizima kwa LDK, kuwezesha ufuatiliaji kamili wa miamala na majibu ya haraka kwa matukio husika ya blockchain.


Kwa mazingira yenye vikwazo vya rasilimali, LDK hutoa mbinu inayotegemea kuchuja ambayo hupunguza mahitaji ya kipimo data na hifadhi. Katika hali hii, LDK huwasilisha mambo yanayoihusu ufuatiliaji kupitia violesura dhahania, ikiomba ufuatiliaji wa vitambulisho maalum vya miamala, UTXO, au mifumo ya hati. Safu ya programu inaweza kisha kutekeleza ufuatiliaji huu kwa kutumia seva za Electrum, wachunguzi wa block, au vyanzo vingine vya data vya blockchain vyepesi. Mbinu hii huwezesha pochi za simu na programu za wavuti kudumisha utendakazi wa Umeme bila kuhitaji usawazishaji kamili wa blockchain.


Safu ya uendelevu katika LDK inafuata kanuni zile zile za uchukuaji, ikitoa programu zenye matone ya data ya jozi ambayo lazima yahifadhiwe na kupatikana kwa uhakika. LDK hushughulikia ugumu wote wa kuweka mfululizo na kuondoa serial katika hali za chaneli za Lightning, data ya umbea wa mtandao, na taarifa zingine muhimu. Programu zinahitaji tu kutekeleza mifumo ya hifadhi inayoaminika, iwe ni kwa kutumia mifumo ya faili ya ndani, huduma za hifadhi ya wingu, au mifumo maalum ya hifadhidata. Ubunifu huu unahakikisha kwamba usimamizi wa hali ya Lightning unabaki imara huku ukiruhusu programu kuchagua suluhisho za hifadhi zinazolingana na mahitaji yao ya uendeshaji na mifumo ya usalama.


### Vipengele vya Kina na Mifumo ya Ujumuishaji


Uwezo wa LDK unapanuka hadi vipengele vya Lightning Network kama vile malipo ya njia nyingi, uboreshaji wa njia, na usimamizi wa umbea wa mtandao. Mfumo wa upelekaji data unadumisha mtazamo kamili wa topolojia ya Lightning Network kupitia ushiriki wa itifaki ya umbea, na kuwezesha utafutaji wa njia kwa busara kwa malipo. Programu zinaweza kushawishi maamuzi ya upelekaji data kupitia vigezo vya usanidi na zinaweza hata kutekeleza mantiki maalum ya upelekaji data kwa matumizi maalum.


Mfumo wa kuunganisha lugha wa maktaba huwezesha ujumuishaji wa LDK katika mazingira mengi ya programu, ikiunga mkono Java, Kotlin, Swift, TypeScript, JavaScript, na C++. Utangamano huu wa mifumo mbalimbali huruhusu programu za simu zilizoandikwa katika lugha asilia kuingiza utendakazi wa Lightning huku zikidumisha sifa bora za utendaji. Mfumo wa kuunganisha huhifadhi usanifu unaoendeshwa na matukio wa LDK na muundo wa moduli katika lugha zote zinazoungwa mkono, na kuhakikisha uzoefu thabiti wa msanidi programu bila kujali jukwaa lengwa.


Makadirio ya ada na utangazaji wa miamala huwakilisha maeneo ya ziada ambapo LDK hutoa unyumbulifu. Programu zinaweza kutekeleza mikakati maalum ya ukadiriaji wa ada inayozingatia mifumo yao maalum ya uendeshaji na mahitaji ya mtumiaji. Vile vile, utangazaji wa miamala unaweza kubinafsishwa ili kufanya kazi na violesura mbalimbali vya mtandao wa Bitcoin, kuanzia miunganisho ya moja kwa moja ya full node hadi huduma za utangazaji za wahusika wengine. Unyumbulifu huu unahakikisha kwamba programu zinazotegemea LDK zinaweza kuboresha mwingiliano wao wa blockchain kwa matumizi yao maalum huku zikidumisha kufuata itifaki ya Lightning na viwango vya usalama.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### Changamoto ya Ukuzaji wa Umeme


Kutengeneza programu zinazounganisha malipo ya Lightning kunaleta kikwazo kikubwa kwa watengenezaji wengi. Ili kuunda programu yenye utendaji kazi wa malipo ya Lightning, watengenezaji kimsingi wanahitaji kuwa wataalamu wa Lightning, kuelewa dhana changamano kama vile usimamizi wa chaneli, usawazishaji wa ukwasi, na topolojia ya mtandao. Sharti hili la utaalamu husababisha tatizo la msingi kwa matumizi ya Lightning: ingawa mtandao wa Lightning wenyewe unafanya kazi na malipo yanaaminika, ugumu wa kiufundi huzuia ujumuishaji mkubwa katika programu za kila siku.


Changamoto kuu iko katika pengo kati ya kile ambacho watengenezaji wanahitaji na kile wanachotaka kutoa. Wasanidi programu kwa kawaida hufanya kazi chini ya tarehe za mwisho zilizowekwa na wanapendelea suluhisho za moja kwa moja zinazowaruhusu kuzingatia utendaji kazi wa msingi wa programu zao badala ya kuwa wataalamu katika miundombinu ya malipo. Wakati ujumuishaji wa Lightning ni mgumu, watengenezaji huvutiwa na suluhisho za utunzaji kwa sababu hutoa njia ya upinzani mdogo. Hata hivyo, mwelekeo huu wa huduma za utunzaji hudhoofisha pendekezo la msingi la thamani la Bitcoin la uhuru wa kifedha usio wa utunzaji.


### Maono ya Breez, Umeme Kila Mahali


Breez iliibuka kutoka kwa maono rahisi lakini yenye malengo makubwa: kuwafanya kila mtu aunganishwe na mtandao wa Lightning kupitia violesura angavu kwa uchumi wa Lightning. Mbinu ya kampuni inatambua kwamba ingawa mtandao wa Lightning unafanya kazi vizuri kitaalamu, unahitaji sana kupitishwa kwa mtumiaji ili kufikia uwezo wake kamili. Changamoto hii ya kupitishwa inaenea zaidi ya watumiaji binafsi ili kujumuisha mfumo mzima wa programu na huduma ambazo zinaweza kufaidika na ujumuishaji wa Lightning.


Programu ya asili ya Breez ilionyesha maono haya kwa kuwapa watumiaji nodi ya Lightning isiyo ya kuhifadhi inayofanya kazi moja kwa moja kwenye simu zao za mkononi. Programu hii ilionyesha uwezo wa Lightning kama vile kutiririsha malipo madogo kwa watangazaji wa podikasti na utendaji wa sehemu ya mauzo. Hata hivyo, programu ya Breez pia ilifunua kizuizi muhimu cha usanifu: mfumo ikolojia wa programu ya simu haurahisishi mawasiliano rahisi kati ya programu, na kulazimisha wasanidi programu kujenga vipengele vyote vinavyohusiana na Lightning kuwa programu moja badala ya kuruhusu programu maalum kutumia miundombinu ya Lightning iliyoshirikiwa.


Mafunzo ya kampuni kutoka kwa programu ya Breez yalisababisha ufahamu muhimu: mustakabali wa kupitishwa kwa Lightning unategemea kushinda wasanidi programu. Ikiwa ujumuishaji wa Lightning usio wa uangalizi unakuwa chaguo rahisi zaidi kwa watengenezaji, unakuwa chaguo chaguo-msingi. Mbinu hii pia inatoa faida za udhibiti, kwani programu isiyo ya uangalizi inakabiliwa na vikwazo vichache vya udhibiti kuliko huduma za uangalizi, na hivyo kurahisisha wasanidi programu kusafirisha programu zao duniani kote.


### Usanifu wa SDK wa Breez


SDK ya Breez hutoa mbinu mbadala ya kuunganisha utendakazi wa Lightning katika programu. Badala ya kuhitaji kila programu kuendesha nodi yake ya Lightning, SDK hutoa usanifu unaodumisha kanuni zisizo za uangalizi huku ikirahisisha uzoefu wa msanidi programu. Katika kiini chake, SDK humpa kila mtumiaji nodi yake ya Lightning inayoendesha miundombinu ya Greenlight, huduma ya upangishaji nodi za Lightning inayotegemea wingu ya Blockstream.


Usanifu huu hutatua matatizo kadhaa muhimu kwa wakati mmoja. Watumiaji hawahitaji kuwa na wasiwasi kuhusu usimamizi wa hifadhidata, muda wa seva kufanya kazi, au matengenezo ya miundombinu—wasiwasi ambao ungekuwa mkubwa kwa watumiaji wa kawaida. Hata hivyo, tofauti na suluhisho za kitamaduni za uhifadhi, Greenlight kamwe haina ufikiaji wa funguo za mtumiaji. Nodi ya Umeme katika wingu haiwezi kufanya shughuli zozote bila programu iliyounganishwa kikamilifu ambayo inaweza kusaini miamala na ujumbe. Muundo huu unadumisha faida za usalama za uhifadhi binafsi huku ukiondoa ugumu wa uendeshaji.


SDK pia inasaidia utendakazi shirikishi. Programu nyingi zinaweza kuunganishwa na nodi ya Lightning ya mtumiaji mmoja kwa kutumia kifungu sawa cha seed, na hivyo kuruhusu watumiaji kudumisha usawa mmoja wa Lightning katika programu tofauti maalum. Kwa mfano, mtumiaji anaweza kuwa na programu ya jumla ya Lightning wallet na programu maalum ya podikasti, zote zikifikia fedha sawa na njia za Lightning. Usanifu huu unawezesha ukuzaji wa programu maalum na zenye umakini huku ukidumisha miundombinu ya kifedha iliyounganishwa.


### Watoa Huduma za Umeme na Ukwasi wa Wakati Uliopangwa


Sehemu muhimu ya Breez SDK ni muunganiko wake na Watoa Huduma za Umeme (LSPs), ambao hufanya kazi sawa na Watoa Huduma za Intaneti lakini kwa mtandao wa Umeme. LSP hutatua mojawapo ya changamoto ngumu zaidi za Umeme: usimamizi wa ukwasi. Katika njia za Umeme, fedha zinaweza kutiririka tu katika mwelekeo ambapo ukwasi upo, sawa na shanga kwenye abacus ambayo inaweza kusonga tu pale ambapo kuna nafasi.


SDK hutekeleza njia za "kwa wakati unaofaa" kupitia LSP, ikidhibiti kiotomatiki ukwasi bila kuingilia kati kwa mtumiaji. Mtumiaji anapohitaji kupokea malipo lakini hana ukwasi wa kutosha unaoingia, LSP hufungua kiotomatiki njia mpya ya Lightning wakati malipo yanapofika. Mchakato huu hufanyika kwa urahisi chinichini, kuhakikisha watumiaji wanaweza kupokea malipo bila kuelewa utaratibu wa msingi wa njia.


Muunganisho huu wa LSP unaenea zaidi ya usimamizi rahisi wa ukwasi. SDK inajumuisha utendaji kamili wa Lightning kutoka kwenye kisanduku: huduma za mnara uliojengewa ndani kwa ajili ya usalama, ushirikiano wa on-chain kupitia ubadilishaji wa manowari, njia za juu kupitia huduma kama MoonPay, na usaidizi wa itifaki za LNURL. Mfumo pia hutoa nakala rudufu na urejeshaji usio na mshono, kuhakikisha watumiaji hawapotezi ufikiaji wa fedha zao hata kama watoa huduma za miundombinu watabadilika au hawatapatikana.


### Uzoefu wa Utekelezaji na Msanidi Programu


SDK ya Breez inaweka kipaumbele uzoefu wa msanidi programu kupitia mbinu yake kamili, inayojumuisha betri. SDK hutoa viambatisho kwa lugha nyingi za programu ikiwa ni pamoja na Rust, Swift, Kotlin, Python, Go, React Native, Flutter, na C#, na kuruhusu wasanidi programu kuunganisha malipo ya Lightning kwa kutumia zana zao za usanidi wanazopendelea. Usanifu huo huondoa ugumu wa Lightning kupitia API huku ukidumisha usalama wa mtandao wa Lightning.


Vipengele muhimu hufanya kazi pamoja ili kutoa uzoefu huu rahisi. Kichanganuzi cha ingizo hushughulikia kiotomatiki miundo tofauti ya malipo, ikiamua kama mfuatano unawakilisha ankara, LNURL, au njia nyingine ya malipo na kuielekeza kwenye kitendakazi kinachofaa cha utunzaji. Kitia sahihi kilichojumuishwa husimamia shughuli zote za kriptografia chinichini, huku kibadilishaji kikishughulikia mwingiliano wa on-chain kwa uwazi. Muundo huu huruhusu wasanidi programu kuzingatia pendekezo la thamani la kipekee la programu zao badala ya kuwa wataalamu wa miundombinu ya Lightning.


Usanifu usioaminika wa SDK unahakikisha kwamba ingawa Greenlight inaweza kuchunguza hali ya chaneli na taarifa za uelekezaji, hawawezi kufikia fedha za watumiaji au kufanya shughuli zisizoidhinishwa. Watumiaji hudumisha udhibiti kamili juu ya funguo zao za kibinafsi, ambazo haziondoki kamwe kwenye vifaa vyao. Mbinu hii inawakilisha mabadilishano yaliyofikiriwa kwa uangalifu kati ya urahisi wa uendeshaji na faragha, ikitoa njia ya vitendo ya kupitishwa kwa umeme mkuu huku ikihifadhi kanuni kuu za Bitcoin za uhuru wa kifedha.


## LDK dhidi ya Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Kuelewa Mapungufu ya Kifaa cha Ukuzaji wa Umeme (LDK)


Kifaa cha Ukuzaji wa Umeme ni mkusanyiko wa maktaba za Rust zilizoundwa ili kuwapa wasanidi programu unyumbufu wakati wa kujenga programu za Lightning Network. Hata hivyo, unyumbufu huu unakuja na changamoto kubwa za utekelezaji zilizoonekana wazi wakati wa ukuzaji wa ulimwengu halisi katika Lipa. Hali ya chini ya LDK ina maana kwamba wasanidi programu lazima washughulikie kazi nyingi ngumu kwa kujitegemea, kuanzia usawazishaji wa grafu ya mtandao hadi uboreshaji wa uelekezaji wa malipo. Ingawa mbinu hii inatoa udhibiti kamili juu ya utekelezaji wa Umeme, inahitaji rasilimali kubwa za uundaji na utaalamu wa kina wa kiufundi ili kufikia uaminifu ulio tayari kwa uzalishaji.


Mojawapo ya vipengele muhimu zaidi vilivyokosekana katika LDK ilikuwa usaidizi wa LNURL, kiwango kilichopitishwa sana ambacho hurahisisha mwingiliano wa Lightning Network kwa watumiaji wa mwisho. Zaidi ya hayo, kutokuwepo kwa matokeo ya nanga kulileta changamoto kubwa za uendeshaji, hasa katika mazingira ya ada kubwa. Matokeo ya Anchor hutatua tatizo la msingi la kufungwa kwa nguvu ya chaneli ya umeme: wakati ada za mtandao zinapoongezeka sana, njia zenye ada zilizoainishwa mapema zinaweza kuwa ngumu kufunga upande mmoja kwa sababu ada iliyowekwa mapema haitoshi kwa uthibitisho wa muamala. Kizuizi hiki kilithibitika kuwa tatizo hasa kwa programu za simu za wallet, ambapo watumiaji wanaweza kuacha wallet bila kuratibu kufungwa kwa chaneli za ushirika, na kuacha fedha zikikwama wakati wa ongezeko la ada.


Ukosefu wa ukomavu wa LDK pia ulijidhihirisha katika uelekezaji wa malipo usioaminika, suala muhimu kwa programu yoyote ya Lightning. Licha ya kuwa utekelezaji mzuri wa kitaalamu, wigo mpana wa LDK kama suluhisho la jumla ulifanya iwe vigumu kushughulikia masuala maalum haraka. Timu ya uundaji ilijikuta ikitumia muda mwingi kutatua matatizo ya uelekezaji na kutekeleza vipengele ambavyo vinapaswa kushughulikiwa katika ngazi ya maktaba, hatimaye kuathiri kasi ya maendeleo na ubora wa uzoefu wa mtumiaji.


### Kugundua Faida za Breez SDK na Greenlight


Mpito hadi Breez SDK uliwakilisha mabadiliko katika mbinu ya usanifu, ukihama kutoka nodi ya Lightning inayojisimamia yenyewe hadi suluhisho linalotegemea wingu linaloendeshwa na huduma ya Blockstream's Greenlight. Mabadiliko haya yalishughulikia mara moja sehemu kadhaa muhimu za maumivu zilizopatikana na utekelezaji wa LDK. Uboreshaji muhimu zaidi ulikuja katika uaminifu wa malipo, haswa kutokana na uwezo wa Greenlight kudumisha grafu ya mtandao inayoendelea kila wakati. Tofauti na utekelezaji wa jadi wa Lightning wa simu ambao lazima ulandanishe taarifa za mtandao wakati programu inapoanza, nodi za Greenlight huendesha kazi mfululizo katika wingu, kudumisha ufahamu wa mtandao wa wakati halisi na kutoa data kamili ya grafu mara moja wakati watumiaji wanapounganisha.


Usanifu huu unatumia utekelezaji wa Core Lightning (CLN) uliojaribiwa vitani, ambao umekuwa ukiendesha malipo kwa mafanikio kwa miaka mingi kama moja ya utekelezaji wa awali wa Lightning Network. Uzoefu uliokusanywa na uaminifu uliothibitishwa wa CLN ulitoa maboresho ya haraka ya uthabiti juu ya mradi mdogo wa LDK. Watumiaji wanapowasha wallet yao inayoendeshwa na Greenlight, wanarithi mara moja maarifa kamili ya mtandao na uwezo wa kuendesha nodi ya Lightning inayoendelea kufanya kazi, na kuondoa ucheleweshaji wa usawazishaji na kutokuwa na uhakika wa kuendesha ambao uliathiri utekelezaji uliopita.


Falsafa ya muundo wa Breez SDK yenye maoni ilikuwa muhimu kwa ajili ya uundaji wa wallet. Badala ya kutoa zana ya jumla ya Lightning, Breez inalenga hasa programu za wallet za mtumiaji wa mwisho, ikiruhusu timu ya uundaji kuzingatia juhudi zao katika kuunda suluhisho kamili kwa ajili ya matumizi haya mahususi. Mbinu hii iliyolengwa iliwezesha Breez kuunganisha huduma muhimu moja kwa moja kwenye SDK, ikiwa ni pamoja na utendaji wa Mtoa Huduma wa Lightning (LSP) unaoruhusu watumiaji kupokea malipo mara moja baada ya usakinishaji wa wallet, bila kuhitaji taratibu za kufungua njia kwa mikono.


### Vipengele Vizuri na Uboreshaji wa Uzoefu wa Mtumiaji


Mbinu jumuishi ya Breez SDK inaenea zaidi ya utendaji wa msingi wa Lightning, ikijumuisha vipengele vinavyoongeza uzoefu wa mtumiaji. Muunganisho wa LSP uliojengewa ndani huondoa kizuizi cha kitamaduni cha kuwataka watumiaji kuelewa usimamizi wa chaneli, na kuwezesha upokeaji wa malipo ya haraka kwa usakinishaji mpya wa wallet. Mchakato huu wa uanzishaji husaidia katika utumiaji wa kawaida, kwani watumiaji wanaweza kuanza kupokea malipo ya Lightning bila ujuzi wowote wa kiufundi au taratibu za usanidi.


Utendaji wa ubadilishaji wa mnyororo hutoa safu nyingine ya uboreshaji wa uzoefu wa mtumiaji kwa kuwezesha uwasilishaji wa salio moja kwa watumiaji. Badala ya kuwalazimisha watumiaji kuelewa tofauti kati ya Lightning na on-chain Bitcoin, huduma ya ubadilishaji inaruhusu ubadilishaji kiotomatiki kati ya tabaka hizi inapohitajika. Watumiaji wanapohitaji kufanya malipo ya on-chain, mfumo unaweza kubadilisha fedha za Lightning kwa on-chain Bitcoin nyuma ya pazia bila shida, ukidumisha udanganyifu wa usawa mmoja, wa kioevu huku ukishughulikia ugumu wa kiufundi ndani.


Usaidizi wa SDK kwa akiba ya njia sifuri hushughulikia changamoto kubwa ya uzoefu wa mtumiaji katika utekelezaji wa jadi wa Umeme. Akiba ya njia kwa kawaida huzuia watumiaji kutumia salio lao kamili lililoonyeshwa, na kusababisha mkanganyiko wakati malipo yanashindwa licha ya fedha zinazoonekana kutosha. Kwa kuondoa akiba hizi, Breez huwawezesha watumiaji kutumia salio lao kamili lililoonyeshwa, ingawa hii inahitaji LSP kukubali hatari zaidi. Makubaliano haya yanaonyesha mbinu ya Breez inayozingatia mtumiaji, ambapo ugumu wa kiufundi na hatari huchukuliwa na watoa huduma ili kuunda uzoefu wa mtumiaji angavu.


Vipengele vya ziada kama vile usaidizi wa LNURL, huduma za viwango vya ubadilishaji, na ulandanishi wa vifaa vingi vinaonyesha zaidi mbinu kamili ya SDK ya uundaji wa wallet. Usanifu unaotegemea wingu huwawezesha watumiaji kufikia nodi yao ya Umeme kutoka kwa vifaa au programu nyingi, huku Breez ikishughulikia ulandanishi wa hali katika sehemu hizi tofauti za ufikiaji. Vipengee vya ramani ya siku zijazo ni pamoja na utendaji wa matumizi yote kwa ajili ya mifereji kamili ya maji ya wallet, uunganishaji wa usimamizi wa chaneli zinazobadilika, na soko la LSP zinazoshindana ili kuanzisha ushindani mzuri katika utoaji wa huduma.


### Kutathmini Masuala ya Kubadilishana na Kuweka Kati


Mpito wa Breez SDK na Greenlight unaleta makubaliano muhimu ya ujumuishaji ambayo lazima yazingatiwe kwa uangalifu katika muktadha wa kanuni za ugawaji wa madaraka za Bitcoin. Usanifu unaotegemea wingu unamaanisha kuwa nodi za umeme za watumiaji hufanya kazi kwenye miundombinu ya Blockstream, na kuunda utegemezi katika operesheni inayoendelea ya Greenlight na maendeleo yanayoendelea ya Breez. Ujumuishaji huu unaenea zaidi ya urahisi tu, na unaweza kuathiri uwezo wa watumiaji wa kurejesha fedha ikiwa huduma hazipatikani au ikiwa udhibiti utatokea.


Hali za urejeshaji zinaleta changamoto mahususi katika usanifu huu. Ingawa watumiaji wanadhibiti funguo zao za kibinafsi, kupata fedha bila miundombinu ya Greenlight kutahitaji utaalamu wa kiufundi ili kuzungusha nodi huru za Umeme wa Core na kurejesha hali za chaneli. Kwa watumiaji binafsi, mchakato huu wa urejeshaji unaweza kuwa mgumu kupita kiasi, na hata watoa huduma wa wallet wangekabiliwa na changamoto kubwa zinazohamisha idadi nzima ya watumiaji hadi miundombinu mbadala ikiwa huduma za Greenlight zingekomeshwa.


Mawazo ya faragha pia hubadilika kutokana na mabadiliko haya ya usanifu. Uelekezaji unaotegemea wingu unamaanisha kuwa Greenlight inaweza kupata mwonekano katika maeneo ya malipo, ilhali usanifu wa awali wa LSP pekee ulipunguza uvujaji wa taarifa kwa kiasi na muda wa malipo. Uzalishaji wa Invoice katika wingu huongeza zaidi uwezekano wa mfiduo wa taarifa, kwani ankara ambazo hazikutumika ambazo hapo awali zilibaki kuwa za faragha kwenye vifaa vya watumiaji sasa hupitia miundombinu ya Blockstream.


Licha ya wasiwasi huu wa ujumuishaji, faida za vitendo mara nyingi huzidi hatari za kinadharia kwa matumizi mengi. Utegemezi ulioboreshwa, seti kamili ya vipengele, na uzoefu bora wa mtumiaji huwawezesha watengenezaji wa wallet kuzingatia uvumbuzi wa safu ya programu badala ya usimamizi wa miundombinu ya Lightning. Mgawanyiko huu wa kazi unaonyesha mfumo ikolojia unaokua ambapo watoa huduma maalum hushughulikia changamoto ngumu za kiufundi, na kuwaruhusu watengenezaji wa programu kuzingatia uzoefu wa mtumiaji na mantiki ya biashara. Jambo la msingi liko katika kuelewa maelewano haya waziwazi na kufanya maamuzi sahihi kulingana na mahitaji maalum ya matumizi na viwango vya uvumilivu wa hatari.




# Sehemu ya Mwisho

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Mapitio na Ukadiriaji

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Hitimisho

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>