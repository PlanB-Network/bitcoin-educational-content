---
name: Gucengera muri Simplicity
goal: Kumenya neza filozofiya y'ubuhinguzi, sisitemu y'ubwoko, n'ubuzima bwose bwa Simplicity
objectives:
  - Gutahura uburyo butatu bw'ishimikiro bwo gufatanya ibintu biharuye na combinators icenda zigira ururimi rwuzuye
  - Kwubaka logique ya Boolean, ubuharuro, na SHA-256 uhereye kuri sisitemu y'ubwoko ntoyi ya Simplicity
  - Gutahura ingene ingaruka zo ku ruhande za Failure na Reader zituma habaho gukorana nyakuri na blockchain
  - Kwiga ingene porogarama za Simplicity zicika amaderesi ya Taproot kandi zikoreshwa mu kwishura hakoreshejwe amakuru ya witness
---

# Gucengera muri Simplicity

Ugucengera kwimbitse mu nyigisho n'ingingo z'ubuhinguzi ziri inyuma y'ururimi Simplicity, bishingiye ku rukurikirane rw'ibiganiro bitanu vyuzuye ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) vya [Dr. Russell O'Connor](https://r6.ca/), umuremyi wa Simplicity muri Blockstream Research. Iri shure risigura *igituma* Simplicity yahinguwe uko imeze, si ingene umuntu ayandika.

Iri shure rikurikira ibiganiro vya Dr. O'Connor biciye mu buryo butatu bw'ishimikiro bwo gufatanya ibintu biharuye, sisitemu y'ubwoko ntoyi n'iteoreme yayo y'ukwuzura, ukwubaka ubwoko bw'amakuru ngirakamaro n'ubuharuro uhereye ku mahame ya mbere, ukwongeramwo n'ubwitonzi ingaruka zo ku ruhande kugira ngo habe gukorana na blockchain, hanyuma ubwa nyuma ingene porogarama zishirwa mu maderesi kandi zigakoreshwa on-chain.

+++

# Intangamarara

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Incamake y'amashure

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Ikaze muri SCR403 — Gucengera muri Simplicity!

Iri shure rishingiye ku rukurikirane rw'ibiganiro **"Delving Simplicity"** vyanditswe na [Dr. Russell O'Connor](https://r6.ca/), umuhinguzi w'ubuhinga bw'ibikorwa remezo muri [Blockstream](https://blockstream.com/) akaba n'umuremyi wa Simplicity. Ivyo biganiro vy'umwimerere vyasohotse ku rubuga rwa [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) kandi ni vyo bikoresho nyamukuru iri shure ryubakiyeko. Turakenguruka igikorwa ciwe c'intango, catumye ibi bikoresho vy'inyigisho bishoboka.

### Ivyo uzokwiga

Iri shure rirasuzuma filozofiya y'ubuhinguzi n'imishinge y'imibare biri inyuma ya Simplicity, ururimi rwa scripting rw'urunganwe rukurikira rwatangujwe kuri [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) muri Mukakaro 2025. Rikurikira urukurikirane rwose rw'ibiganiro bitanu kandi ritunganijwe mu bice bibiri nyamukuru vy'ibirimo:

1. **Imishinge ya Simplicity** — Igituma ubuharuro bwa blockchain busaba ururimi rutandukanye mu mizi, uburyo butatu bwo gufatanya ibikorwa (bikurikirana, bibangabanganye, bisunga ikintu), na combinators icenda z'ishimikiro zigira ururimi rwuzuye mu mibare
2. **Kuva ku Bwoko bw'Amakuru gushika kuri Porogarama** — Kwubaka logique ya boolean, ubuharuro, na SHA-256 uhereye ku mahame ya mbere; gutahura ingaruka zo ku ruhande za Failure na Reader zituma habaho gukorana na blockchain; no kwiga ingene porogarama zishirwa mu maderesi ya Taproot biciye kuri Commitment Merkle Roots kandi zikoreshwa mu kwishura hakoreshejwe amakuru ya witness

### Ibisabwa imbere yo gutangura

Iri ni ishure ryo ku **rwego rw'abahinga** (nk'amasaha 10). Ukwiye kuba umenyereye:
- Ivyiyumviro vy'ishimikiro vya Bitcoin scripting (ico kwemeza transaction gukora)
- Ivyiyumviro vy'ishimikiro vyo gukora porogarama (ubwoko, functions, composition)
- Kumenyera gato inyandiko z'imibare birafasha ariko si ngombwa. Tuzosigura vyose uko tubandanya

### Ibikoresho nyamukuru

- **Ibiganiro vy'umwimerere**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) vya Dr. Russell O'Connor kuri Delving Bitcoin
- **Ububiko bwa Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — source code n'ivyemezo vya Rocq vyemewe mu buryo formal
- **Urubuga rwemewe**: [simplicity-lang.org](https://simplicity-lang.org/) — inyandiko n'aho wihereza amakuru ya SimplicityHL
- **Blog ya Blockstream**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — incamake y'ubuhinga

Witeguye kwinjira muri kimwe mu bihinguzi vy'ubuhinga bwa Bitcoin bifise ubwiza buhanitse? Reka dutangure!

## Simplicity ni iki?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Nimba uje muri iri shure ata ntango ufise muri Simplicity, iki kigabane kizogufasha kumenya aho uri imbere y'uko twinjira mu vyimbitse.

### Simplicity muri make

Simplicity ni **ururimi rwa smart contract kavukire rwa Bitcoin**, rukora kuri Liquid Network uno musi. Rwiyumviriwe ubwa mbere na Dr. Russell O'Connor hafi ya 2012 kandi rusigurwa mu mpapuro ziwe zo muri 2017 *Simplicity: A New Language for Blockchains*, rwatangujwe kuri Liquid Network muri Mukakaro 2025 inyuma y'imyaka y'igenzura formal n'iterambere.

Bitandukanye na Solidity ya Ethereum, ari ururimi rwa contract rwo ku rwego rwo hejuru kandi Turing-complete, Simplicity ni ntoyi ku bushake. Ifise:
- **Abarema ubwoko batatu** (unit, sum, product)
- **Combinators icenda** (ibikorwa vy'ishimikiro n'amategeko ya composition)
- **Nta loops, nta recursion, nta memory ihinduka ku gihe c'ikoreshwa**

Uhereye kuri ivyo bintu vy'ishimikiro gusa, urashobora kwubaka ubuharuro bwose ukeneye kugira ngo wemeze transactions, kuva kuri logique ya boolean gushika ku hashing yuzuye ya SHA-256.

### Wokora iki na Simplicity uno musi?

Simplicity iramaze gukoreshwa mu bikorwa nyakuri kuri Liquid Network. Ikiboneka cane ni [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), isoko ry'options ridakeneye oracle aho abakoresha bacuruza call options kuri L-BTC bakoresheje USDt nk'ingwati (contract iri inyuma kandi ishigikira puts). Iyindi migambi ya Simplicity ikora irimwo [Swaption](https://swaption.io/) ya SideSwap (options) n'umugambi open-source [Deadcat](https://github.com/Resolvr-io/deadcat) wa Resolvr (amasoko yo guhanura). Hanze ya DeFi, Simplicity ituma habaho ibisabwa vy'itegeko ryo gukoresha amahera biteye imbere nk'ama vaults, covenants, n'uburyo bwa multisig bugoye butoshoboka canke butagira umutekano muri Bitcoin Script.

### Iri shure ari iki — kandi atari iki

Iri **si** ishure ryo kwandika code ukoresheje amaboko. Ntuzokwandika porogarama za Simplicity hano. Nimba ari vyo urondera, raba:
- [simplicity-lang.org](https://simplicity-lang.org/) — inyandiko zemewe n'ururimi rwo ku rwego rwo hejuru SimplicityHL
- [Ububiko bwa Simplicity kuri GitHub](https://github.com/BlockstreamResearch/simplicity) — ishirwa mu ngiro ry'ifatiro, uburorero, n'ivyemezo vya Rocq
- [Ikiganiro ca blog ya Blockstream](https://blog.blockstream.com/en-simplicity-github/) ku bijanye no gutangura

Ico iri shure **rivugako**: **amahitamwo ya filozofiya n'ubuhinga** ari inyuma y'ubuhinguzi bwa Simplicity. Kubera iki uru rurimi rwaremwe muri ubu buryo? Kubera iki combinators icenda gusa? Kubera iki ata recursion? Kubera iki bihambaye ko sisitemu y'ubwoko ifitaniye isano na sequent calculus ya Gentzen?

Rivyiyumvire nk'ugutahura **igituma moteri yubatswe muri ubu buryo** aho kwiga gutwara imodoka.

### Ni bande rigenewe?

Iri shure ribereye:
- **Abahinguzi ba protocol** bashaka gutahura imishinge ya Simplicity imbere yo kwandika code
- **Abashakashatsi ba Bitcoin** bashimishwa n'igenzura formal n'uburyo bushingiye ku nyigisho y'ubwoko
- **Abahinga ba mudasobwa** bafise inyota ku sano riri hagati ya sequent calculus n'ubuharuro bwa blockchain
- **Ababitcoiners bateye imbere** bashaka kurenga ugutahura kwo ku ruhande gusa ku bushobozi bwa scripting bwa Liquid

Nimba amajambo nka "sum types", "combinators", canke "sequent calculus" ari mashasha rwose kuri wewe, ntugire ubwoba, turasigura vyose duhereye ku ntango. Ariko witegure urugendo ruremereye kandi rw'imibare.

### Kuva ku biganiro gushika kw'ishure

Urukurikirane rw'umwimerere "Delving Simplicity" rwa Dr. O'Connor rwatunganijwe nk'ibiganiro bitanu vy'ubuhinga. Iri shure rirasubira gutunganya no gusigurira ivyo bikoresho mu nzira y'ukwiga itera imbere, hamwe n'ibibazo vyo kugerageza ugutahura kwawe uko ugenda. Ivyiyumviro, insiguro, n'ivyemezo ni ivyiwe, natwe twarahinduye uburyo kugira ngo bibe inyigisho itunganijwe.

# Imishinge ya Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Uburyo bw'Ishimikiro bwo Gufatanya Ubuharuro

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Ubu Simplicity imaze gutanguzwa kuri Liquid Network, nshaka gukora ugucengera kwimbitse muri filozofiya n'ubuhinguzi bw'ururimi Simplicity.

Kwemeza transactions za Bitcoin ni ikoreshwa ritandukanye cane n'ubuhinguzi bw'indimi zisanzwe zo gukora porogarama. Igiciro c'ikibanza muri block kiri hejuru cane rero porogarama zikwiye kuba ntoyi. Porogarama ziri muri transactions za Bitcoin zikorwa gusa ku input imwe kandi abantu bose bakorera porogarama kuri input imwe. Vyongeye, uwutanga uruhusha rwa transaction aba asanzwe azi inyishu y'ubuharuro imbere y'igihe: ko transaction yemewe.

Akenshi uwutanga uruhusha azokoresha ubuharuro buzimbutse cane kugira ngo akure amakuru ya witness yemeza ko transaction yemewe, mu gihe porogarama zikora kuri blockchain zikwiye gusuzuma ko amakuru ya witness ari yo. Gusuzuma ko ikintu ari co akenshi birahendutse cane kuruta kwerekana ko ari co.

Twahinguye Simplicity tuzirikana ubu bwoko bw'ingorane zidasanzwe z'ubuhinguzi bw'ururimi. Nk'akarorero, Simplicity isaba ko amashami adakoreshejwe akurwaho kugira ngo ntaboneke kuri blockchain. Intambwe zo gutegura imbere zateguwe n'ubwitonzi kugira ngo zerekane complexity y'igihe (quasi-)linear mu bunini bwa porogarama ya Simplicity. Isesengura static rirakoreshwa aho gukoresha "gas", idashobora kubarwa umuntu atabanje gukora code mu buryo bwategetswe, kugira ngo ido n'ido ry'ukuntu execution ikorwa ntiribe ibintu bihambaye ku consensus. Nta dynamic memory allocation mu gihe c'ikoreshwa. N'ibindi.

Imbere yo kwinjira mu ndondoro z'ubuhinguzi bwa Simplicity, nshaka gutangura uru rukurikirane n'filozofiya yo gukora porogarama ku bijanye n'uburyo rusangi bwo gufatanya ibice vy'ishimikiro kugira ngo habe ubushobozi bushasha.

### Composition

Dufate ko umuntu ariko arahungura ururimi rw'amasezerano ashobora gutegurwa kuri blockchain nka Bitcoin. Cane cane, porogarama zishobora gusa gushikira amakuru ya transaction n'amakuru ya UTXO y'ama inputs, kandi execution igena gusa ko transaction yemewe (ivyo bigatuma inyishu ya execution ishobora kubikwa muri cache). Reka tuvuge ko umuntu atangurana n'umugwi w'ibikorwa vy'ishimikiro bishobora gukora imirimo itandukanye nk'ubuharuro bw'ishimikiro, gusoma no/canke gutunganya amakuru ava muri transaction, n'ukwemeza umukono. Igikorwa cose kirya input y'ubwoko bunaka (ishobora kuba iri ubusa) kigatanga output y'ubwoko bunaka. Ni ubuhe buryo dushobora gufatanya ibi bikorwa vy'ishimikiro bikaba ibikorwa bigoye kuruta?

### Sequential Composition

![Sequential Composition ikurikirana](assets/en/001.webp)

Uburyo bwa composition bw'ishimikiro kuruta ubundi ni sequential composition. Nimba dufise ibikorwa bibiri vy'ishimikiro, kimwe gifise ubwoko bw'amakuru ya output buhuye n'ubwoko bw'amakuru ya input y'ikindi, turashobora gufatanya ivyo bikorwa bibiri bikaba igikorwa gishasha kigizwe n'ivyo bibiri. Ico gikorwa gishasha gikoresha ivyo bikorwa bibiri vy'ishimikiro bikurikirana, gifata nk'input input y'igikorwa ca mbere, kigaca gitanga output y'ico gikorwa ca mbere muri input y'igikorwa ca kabiri, hanyuma amaherezo kigasubiza output y'ico gikorwa ca kabiri.

Birumvikana ko tutabwirizwa kugarukira ku gufatanya ibikorwa vy'ishimikiro gusa. Ubu ko dufise ibikorwa bigizwe n'ibindi, turashobora no kubifatanya dukoresheje functional composition.

Mu mibare, iyi sequential composition akenshi yitwa gusa "composition", kandi umuntu yoshobora kwiyumvira ko ari bwo buryo bwonyene bwo gufatanya ibintu. Ariko dufise ubundi buryo bwo gufatanya ibikorwa.

### Parallel Composition

![Parallel Composition ibangabanganye](assets/en/002.webp)

Dufate ko dufise ibikorwa bibiri, bishobora kuba ibikorwa vy'ishimikiro canke bigoye, kandi vyose bifata ubwoko bumwe bwa input. Uburyo bwa kabiri bw'ishimikiro bwo gufatanya ivyo bikorwa bibiri ni ukubikoresha vyose kuri input imwe. Ivyo vyitwa parallel composition, kandi ubwoko bwa output ni "product" y'ubwoko bw'ama outputs y'ivyo bikorwa vy'umwimerere kandi burimwo ipare y'ama outputs abiri.

Naho ibi vyitwa composition "parallel", kandi ivyo bikorwa bibiri vyoshobora mu ngingo gukorwa bibangabanganye, gukora bibangabanganye si ikintu gisabwa mu mikorere. Turashobora gushira mu ngiro parallel composition "bikurikirana" mu gukora igikorwa kimwe ubwa mbere hanyuma igikorwa ca kabiri. Ntitwitaye ku ndondoro z'ukuntu parallel composition ishirwa mu ngiro igihe output ari imwe.

### Conditional Composition

![Conditional Composition ishingiye ku kintu](assets/en/003.webp)

Conditional composition ni dual ya parallel composition. Muri iki gihe dufise ibikorwa bibiri bitanga output imwe, kandi tubifataniriza hamwe mu guhitamwo kimwe muri vyo co gukora. Input y'iki gikorwa kigizwe n'ibindi ni "sum" canke "tagged union" y'ubwoko bw'ama inputs y'igikorwa c'umwimerere. Muri iki gihe tag, "Left" canke "Right", ni bit imwe mu makuru ya input igena ubwoko bw'amakuru butwawe, kandi rero igena kimwe muri vya bikorwa bibiri gishobora gukorwa.

Conditional composition ikora muri ubwo buryo nyene naho input yaba ari sum y'ubwoko bubiri bumwe. Sum type iracafise tag, kandi agaciro k'iyo tag ni ko kagena kimwe muri vya bikorwa bibiri kizokorwa.

### Composition muri Bitcoin Script

Hari uburyo bwinshi bwo gushira mu ngiro ubu bwoko butatu bwa composition mu ndimi zitandukanye zo gukora porogarama. Muri Bitcoin Script, sequential composition ishirwa mu ngiro (hafi) biciye ku gufatanya routines zibiri (ni co gituma Bitcoin Script yitwa ururimi rwo gukora porogarama concatenative) kuko output ya routine imwe isigara kuri stack kugira ngo iribwe na routine ikurikira. Parallel composition ishikwako hakoreshejwe ibikorwa vya duplicate na swap kugira ngo bihindure stack ku buryo routines zibiri zishobora gukorwa kuri input imwe. Ibintu si vyose bigenda mu buryo butaziguye kuko ico twita "product" y'ubwoko akenshi gishirwa mu ngiro hakoreshejwe ibintu vyinshi vya stack. Nizigiye ko ushobora kubona iciyumviro rusangi.

Conditional composition, birumvikana, ishirwa mu ngiro na `OP_IF` itandukanya amashami yisunze agaciro kari kuri stack. Muri iki gihe ikintu kiri hejuru kuri stack gikina uruhara rwa tag, kandi akenshi ikintu gikurikira canke ibintu biri kuri stack bifise "ubwoko" butandukanye bivana n'agaciro ka tag. Ku kibazo cose, ubwoko bw'ibintu vya stack bushobora kuba bubereye gusa gutunganywa n'imwe mu mashami ya `OP_IF`. Ariko tumaze gushika kuri `OP_ENDIF`, ibintu vya stack bitegerezwa kuba bifise "ubwoko" buhuye ku buryo script isigaye ishobora kubandanya itarinze kwitaho ishami ryafashwe imbere.

### Composition muri Simplicity

Twahinguye Simplicity ifise combinators zishira mu ngiro ubu buryo butatu bwa composition ata guca hirya. Hamwe n'izindi combinators nkeyi zo gushigikira ibindi bikorwa vy'ishimikiro bijanye na product na sum types, ururimi rw'ishimikiro rwa Simplicity amaherezo rugizwe na combinators icenda zihagije kugira ngo ziserure ubuharuro bwose bufise iherezo. Tuzobiganirako mu buryo burambuye mu kigabane gikurikira.

### Ubwoko bwa Kane bwa Composition

Imbere yo kurangiza dukwiye kuvuga ko hari nibura ubundi bwoko bumwe bwa composition buboneka muri Computer Science, ari bwo "recursive composition". Muri recursive composition igikorwa kimwe gisubirwamwo incuro nyinshi.

Menya ko Bitcoin Script idashigikira recursive composition, kandi nk'uko nyene, twakuye recursion itagira urugero mu buhinguzi bwa Simplicity mu buryo butomoye. Iciyumviro cacu ni uko ubuharuro busubirwamwo butagira urugero bushirwa mu ngiro neza kuruta hakoreshejwe recursive covenants zihara hejuru ya transactions nyinshi. Ivyo bituma abakoresha birinda ibibujijwe vy'ikibanza ca block n'amategeko ya standardness kandi bagashobora gutegura neza ibiciro vya transaction.

Ariko rero, hari uburyo bwo gukoresha nabi feature ya delegation ya Simplicity kugira ngo itange ikintu gisa na recursive composition itagira urugero, ivyo twoshobora kuganirako mu nyuma muri uru rukurikirane.

### Iciyumviro ca nyuma

Twasuzumye uburyo butatu nyamukuru bwa composition bwo guhindura ibikorwa vy'ishimikiro bikaba ibikorwa bigoye:

- sequential composition
- parallel composition
- conditional composition

Twaganiriye ingene ubu buryo bwa composition bushirwa mu ngiro muri Bitcoin Script, kandi twerekanye incamake y'ingene bwagize ingaruka ku buhinguzi bw'ururimi Simplicity. Twabonye ko ubwoko bwa kane bwa composition, recursive composition, bwakuwe mu buryo bwihariye muri Simplicity no muri Bitcoin Script.

Mu kigabane gikurikira tuzosigura combinators icenda zigize umushaha w'ururimi Simplicity, ingene zifasha gushira mu ngiro ata guca hirya ubu buryo butatu bwa composition, n'ingene ivyo bigira ururimi rwuzuye rwo gusigura ubuharuro bwose bufise iherezo.

## Ukwuzura kwa Combinators kwa Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

Muri iki kigabane turatangiza ururimi rw'ishimikiro rwa Simplicity kandi twerekana ko ururimi rwuzuye, bisigura ko ubuharuro bwose bufise iherezo bushobora guserurwa muri rwo.

### Ubwoko bwa Simplicity

Simplicity ishigikira abarema ubwoko batatu b'ishimikiro. Ubwoko product `A × B` buserukira ama outputs ya parallel composition, mu gihe ubwoko sum `A + B` (tagged union) bufata ama inputs ya conditional composition. Ubwoko bwa gatatu ni unit type.

### Unit Type

Unit type, yandikwa `𝟙` canke `ONE`, irimwo agaciro kamwe gusa: tuple iri ubusa `⟨⟩` canke `()`. Ubu bwoko bw'amakuru bwa zeru-bit nta makuru butwara.

### Sum Type

Sum type `A + B` ifatanya ubwoko bubiri bufise tags zerekana "left" canke "right." Values zandikwa nka `σᴸ(a)` canke `inl(a)` ku values zifise tag ya left, na `σᴿ(b)` canke `inr(b)` ku values zifise tag ya right. Izo tags ziguma zitandukanye naho hoba hariko hafatanywa ubwoko bumwe.

#### Boolean Type

Ubwoko `𝟙 + 𝟙`, bwandikwa `𝟚` canke `TWO`, buserukira ubwoko bwa bit imwe bufise values zibiri. Ku mugenzo, `σᴸ⟨⟩` iserukira false/zero, mu gihe `σᴿ⟨⟩` iserukira true/one.

### Product Type

Product types `A × B` zirimwo ama pares ya values yandikwa nka `⟨a, b⟩` canke `(a, b)`. Ubwoko `𝟚 × 𝟚` bufise values zine, zitandukanye n'ama values ane ari muri `𝟚 + 𝟚`.

### Imvugo z'Ishimikiro za Simplicity

Ibikorwa vyandikwa nka `f : A ⊢ B`, bisigura ubwoko bwa input `A` n'ubwoko bwa output `B`. Simplicity ni "first-order" — nta function types ifise.

### Ibikorwa Bibiri vy'Ishimikiro

Ururimi rw'ishimikiro rutanga ibikorwa bibiri vy'ishimikiro:

**Identity (`iden`).** Igikorwa identity kirengana input yaco ata gihindutse:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Igikorwa unit kirata input yaco kigaca gisubiza tuple iri ubusa:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Ivyo bigira imiryango ifise igikorwa kimwe kuri buri bwoko.

### Combinators Zitatu za Composition

Sequential composition ikoresha `comp f g` (yandikwa `f ⨾ g` canke `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Parallel composition ikoresha `pair f g` (yandikwa `f ▵ g` canke `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Conditional composition ikoresha `case f g : (A + B) × C ⊢ D`, igaha amashami uburyo bwo gushikira shared environment `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Kubera iki conditional composition ifata iyi shusho — sum iparanye na shared environment `C` — aho gufata `copair f g : A + B ⊢ C` yoroshe ihitamwo gusa ishami? Kuko `copair` yonyene idashobora guserura **distribution**: function `dist : (A + B) × C ⊢ A × C + B × C` isunika shared input mw'ishami ryose ryafashwe. Mu kwinjiza environment `C` mu `case` ubwayo, Simplicity ironka conditional composition *hamwe* na distribution ivuye kuri combinator imwe — kimwe mu ngingo nyamukuru z'ubuhinguzi zituma ururimi rw'ishimikiro ruguma kuri combinators icenda.

### Izindi Combinators Zine

Gukoresha product bikorwa na `take` na `drop`:

**take** ikura element ya left:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** ikura element ya right:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Gukora sum bikoresha `injl` na `injr`:

**injl** izinga n'itag ya left:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** izinga n'itag ya right:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Combinators Icenda z'Ishimikiro

Muri rusangi, Simplicity ifise combinators icenda z'ishimikiro neza na neza:

| Combinator | Ico ikora |
|---|---|
| `iden` | Irengana input |
| `unit` | Ita input |
| `comp` | Sequential composition |
| `pair` | Parallel composition |
| `case` | Conditional composition |
| `take` | Ikura left muri product |
| `drop` | Ikura right muri product |
| `injl` | Ishira muri left ya sum |
| `injr` | Ishira muri right ya sum |

### Simplicity na Sequent Calculus

Ubuhinguzi bwa Simplicity buva ku gice conjunctive-disjunctive ca sequent calculus ya Gentzen. Mu buryo bwuzuye kuruta, ni variant ya *functional interpretation* ya sequent calculus, ubwayo isa n'isano rya Curry-Howard hagati ya natural deduction na lambda calculus. Amategeko ya combinator yerekana "ubwoko buto mu vyiyumviro vy'imbere kuruta mu vyiyumviro vya nyuma," bigatuma Bit Machine — interpreter ya abstract stack machine ya Simplicity — igabanya gukopa amakuru mu gihe c'ikoreshwa.

### Values si Expressions

Imvugo za Simplicity ziserukira ibikorwa, si values. Inyandiko `scribe b : A ⊢ B` iserukira expression idasanzwe ihora isubiza value `b`, ikora nk'uburyo bworoshe bwo kwandika aho kuba combinator. Ivyo bisa na Bitcoin Script, aho ibikorwa nka `OP_1` bisunika values aho kuvyerekana ata guca hirya.

### Teoreme y'Ukwuzura ya Simplicity

Dufise combinators zose icenda, tumenya gute ko ata co tubuze — ko izo icenda vy'ukuri zihagije? Teoreme y'Ukwuzura ya Simplicity irishura: kuri function iyo ari yo yose hagati y'ubwoko bwa Simplicity (bufise iherezo), hari expression ya Simplicity iyiserukira. Icemezo kirubaka — kirerekana ingene umuntu yubaka iyo expression:

1. **Gusambura input**: Ukoresheje expressions `case` zishizwe imbere mu zindi, sambura neza input iyo ari yo yose y'ubwoko ubwo ari bwo bwose mu bits ziyigize
2. **Kwubaka lookup table**: Kuri buri input ishoboka, koresha `scribe` kugira ngo utange output ihuye na yo
3. **Gukoranya**: Izo cases na scribes zishizwe imbere mu zindi zikorana zigakora lookup table nini ishira mu ngiro iyo function

Iyi teoreme yemejwe mu buryo formal mu proof assistant Rocq (yahoze yitwa Coq). Icemezo kiri mu bubiko bwemewe bwa Simplicity kandi cagenzuwe n'imashini ko ari co.

Naho teoreme y'ukwuzura yemeza ko combinators icenda za Simplicity zishobora guserura function iyo ari yo yose hagati y'ubwoko bwa Simplicity (bufise iherezo), expressions zivuye mu nyubako ya lookup-table ziba nini cane ku buryo zidashoboka mu bikorwa. Function ku ma inputs ya 256-bit yosaba lookup table ifise entries 2²⁵⁶. Ni co gituma ibigabane bikurikira vyibanda ku kwubaka expressions zikora neza zikoresha structure y'ubuharuro, aho gukoresha inguvu mu gushira vyose muri lookup tables.

### Iciyumviro ca nyuma

Ururimi rw'ishimikiro rwa Simplicity rufise sisitemu y'ubwoko na combinators bituma ubuharuro bwose bufise iherezo bushoboka. Naho teoreme y'Ukwuzura yemeza ubushobozi bwo guserura, expressions zivuye mu nyubako rusangi ziba nini cane ku buryo zidashoboka mu bikorwa. Iterambere rya Simplicity ryo mu bikorwa risaba gukoresha structure y'ubuharuro kugira ngo habe expressions ngufi. Ibigabane bikurikira birasuzuma data structures, gukorana na transactions, n'izindi combinators.

# Kuva ku Bwoko bw'Amakuru gushika kuri Porogarama

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Kwubaka Ubwoko bw'Amakuru

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

Mu bigabane vyabanje, twerekanye ingene umugwi w'ishimikiro wa combinators za Simplicity uhagije kugira ngo ushire mu ngiro ubuharuro pure ubwo ari bwo bwose bufise iherezo. Iki kigabane cerekana ingene twubaka data structures n'ubuharuro ngirakamaro tuvuye kuri ivyo bintu vy'ishimikiro — nka kurya mudasobwa zubakwa ziva kuri logic gates.

### Logique ya Boolean

Ubwoko bwa Boolean, bwandikwa `𝟚`, bungana na `𝟙 + 𝟙` kandi bufise values zibiri: `σᴸ⟨⟩` (false) na `σᴿ⟨⟩` (true). Ukoresheje combinators z'ishimikiro, operators za logique ya Boolean zirashobora kwubakwa.

#### Igikorwa And

Igikorwa ca logique `and : 𝟚 × 𝟚 ⊢ 𝟚` gifata bits zibiri kigasubiza bit imwe. Ishirwa mu ngiro ryaco ritandukanya amashami rishingiye kuri bit ya mbere: nimba ari false, subiza false; ahandi ho, subiza bit ya kabiri.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Kugerageza ukoresheje `⟨false, false⟩`:

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

Kugerageza ukoresheje `⟨true, true⟩`:

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

#### Ibindi Bikorwa vya Logique

Igikorwa `not` gisaba combinator ifasha:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

`iden ▵ unit : A ⊢ A × 𝟙` yo mu ntango yongerako "environment" iri ubusa kuri input, bigatuma combinator `case` ishobora gukoreshwa. Gukoresha `take` mu mashami abiri birata iyo environment iri ubusa kugira ngo bikore `f` canke `g`.

Ibindi bikorwa vya logique ya Boolean:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bit Adders

"Half-adder" ifata bits zibiri ikazongeranya, igatanga output ya bits zibiri: carry bit na sum bit.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

"Full-adder" yongeranya bits zitatu, igatanga output ya bits zibiri. Input ikoresha nested tuple `(𝟚 × 𝟚) × 𝟚`.

Ku ma tuples yashizwe imbere mu yandi, hakoreshwa inyandiko ngufi:

- `O f` yerekana `take f`
- `I f` yerekana `drop f`
- `H` yerekana `iden`

Nk'akarorero, `I O H` bisigura `drop (take iden) : A × (B × C) ⊢ B`, bikura value yo hagati. Iyo nyandiko ivyutsa iciyumviro c'imibare ya binary: igihe umuntu yiyumvira nested tuples nk'ibiti vya binary, iyo nyandiko iserukira imibare ya binary ihinduwe y'ibibanza vyo muri ico giti. Izi expressions zigira De Bruijn indices za Simplicity.

**Iciyumviro:** Inyandiko `I`, `O`, na `H` ikoreshwa gusa ku subexpressions zigizwe na `take`, `drop`, na `iden` gusa.

Full-adder ifatanya half-adders zibiri, igafata logique `or` ya carry bits:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

Mu murongo wa mbere, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` ikoresha half-adder ku bits zibiri za mbere, ikabika bit ya nyuma.

Mu murongo wa kabiri, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` ibika bit ya mbere (carry-out ya half-adder ya mbere) kandi igakoresha half-adder ku bits zibiri za nyuma.

Mu murongo wa nyuma, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` ifata OR ya logique y'ama bits abiri ya mbere (carry-outs z'ama half-adders yompi) kandi igasubiza sum-out bit ya half-adder ya kabiri.

Ivyo vyerekana gukora porogarama muri Simplicity: gukoresha inyandiko `I`, `O`, na `H` kugira ngo werekane data bits, ugakora "environments" zibereye zo guhamagara izindi functions biciye kuri sequential composition.

Abakoresha ntibasigura ibikorwa vyo ku rwego rwo hasi ata guca hirya. Mu nyuma uru rukurikirane ruzoganira standard library jets zishira mu ngiro functions zisanzwe. Abakoresha ba nyuma ntibitezweko gukora porogarama ata guca hirya muri Simplicity, nk'uko bimeze kuri Bitcoin Script. Ahubwo, indimi zo ku rwego rwo hejuru nka SimplicityHL zitanga code ya Simplicity, zigacunga subexpression "environments" kandi zigahindura variables zifise amazina zikaba urukurikirane rukwiye rwa `take` na `drop`.

### Vectors

Fixed-length vectors zisigurwa mu gukora products zisubirwamwo z'ubwoko `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Zishobora kwandikwa nka `A^2`, `A^4`, `A^8`, n'ibindi.

Vectors zisigurwa gusa ku burebure buri powers of two. Izindi powers zisaba guhitamwo conventions zo gushira mu tubago.

Ku expression `f : A ⊢ B`, pairing isubirwamwo "maps" yayo hejuru ya fixed-length vectors:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Ku function `f : A × B ⊢ B`, iteration canke "folding" hejuru ya fixed-length vectors:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Hari variations nyinshi. Ku `f : A × B ⊢ C`, "zip" hejuru ya paired vectors na `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Ku `f : (A × B) × C ⊢ C`, fold hejuru ya paired vectors na `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Gufatanya `map` na `fold-right` bitanga accumulating combinators: `f : A × C ⊢ C × B` bitanga `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Hari n'izindi variants nyinshi zishoboka.

#### Multi-bit Words

Bit vector itanga integers z'ama bits menshi. Nk'akarorero, `𝟚³²` ni ubwoko bwa word ya 32-bit. `𝟚²⁵⁶` ni ubwoko bwa word ya 256-bit, bubereye hashes n'ibikorwa vya cryptography.

Hakoreshejwe full-adder, variant y'ibikorwa vya vector isigura "ripple carry adder" hejuru ya words z'ama bits menshi:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` ifata imibare ibiri ya binary ya n-bit n'input ya carry ya bit imwe, igasubiza flag ya carry-out ya bit imwe n'umubare wose wa n-bit.

#### SHA-256

Mu gusigura mu buryo recursive ibikorwa vy'ubuharuro ku ma words y'ama bits menshi — gukurako, gukuba, kugabura — n'ibikorwa vya logique vya bit-wise nka logical AND, OR, XOR, no kubifatanya kenshi, mbere n'igikorwa ca block compression ca SHA-256 kirashobora kwubakwa:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

Compression ya SHA-256 isigurwa mu buryo formal hakoreshejwe Simplicity muri proof assistant Rocq (yahoze yitwa Coq), hamwe n'icemezo formal c'uko ishirwa mu ngiro rya `sha256-hash-block` ari ryo.

Iyo compression ikora buhoro cane nk'iyo ari Simplicity raw. Jets zikoresha functions zisanzwe nka SHA-256 compression mu buryo native. Ishirwa mu ngiro rya Simplicity pure rikora nk'ibisobanuro formal vya jets.

### Option Types

Option types zivana no gufata sum hamwe na unit type:

```
Option A ≔ 𝟙 + A
```

Ubwoko `Option A` bushobora kwandikwa nka `A?` canke `𝕊 A` (aho `𝕊` bisigura "successor"). Functions zikora map hejuru ya option types:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Combinators za monadic nka bind zirashobora gusigurwa:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Variable Length Buffers

"Buffers" ni ubwoko bw'ama vectors yuzuye igice:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Ubwoko `Xᑉ⁸` bwaguka bukaba `(1 + X⁴) × ((1 + X²) × (1 + X))`. Kubufata nka polynomial no kubwagura bitanga `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Kubusigura nk'ubwoko, buserukira sum y'ama tuples yose ashoboka ya X gushika kuri 7, harimwo tuple iri ubusa. Ibi ni neza na neza ubwoko bw'ama lists afise uburebure buri munsi cane ya 8.

Nk'uko bimeze kuri vectors, ibikorwa vya mapping na folding birashobora gusigurwa hejuru ya buffers. Ibikorwa vya stack birimwo `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` na `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` yongerako item kuri buffer, igasubiza vector yuzuye iyo habaye overflow. `pop-<n` ikurako item, igasubiza buffer ntoyi n'item yakuweko, canke igasubiza nothing iyo buffer y'umwimerere yari iri ubusa.

Insiguro ya `push-<n`, mu buryo recursive:

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

Simplicity raw ica igora gukurikira iyo complexity irenze urwego runaka. Abakoresha ba nyuma bakoresha indimi zo ku rwego rwo hejuru nka SimplicityHL zitanga izo expressions zikoreshwa ku mugenzo.

### Iciyumviro ca nyuma

Iki kigabane cerekanye ingene twubaka ibikorwa vya logique tuvuye kuri bits. Biciye kuri ivyo, ubuharuro bwo ku rwego rwa bit bwaravutse, butuma bishoboka kuzirikana ku execution. Ubwoko bwa vector bwaratejwe imbere, bwerekana iteration hejuru ya words z'ama bits menshi kugira ngo hasigurwe ubuharuro. Tubandanye, ibikorwa vya cryptography nka SHA-256 n'ukwemeza umukono wa Schnorr birashobora gusigurwa hakoreshejwe combinators za Simplicity gusa — vyose vyarasiguwe vy'ukuri hakoreshejwe Simplicity.

Iki kigabane si indongozi yuzuye y'ubwoko bw'amakuru n'ibikorwa vyose bishobora kwubakwa muri Simplicity, ariko kirerekana ingene hashikwako ubushobozi ngirakamaro mu bibazo Simplicity yemera. Naho ubwoko bufise imipaka y'iherezo, vectors ngirakamaro, buffer types, n'ibikorwa bisubirwamwo hejuru y'izo structures birashobora gusigurwa.

Ibisobanuro nyakuri vy'ibikorwa vya standard library biratandukana gato n'insiguro ziri hano. Nk'akarorero, full-adder ikoresha XOR y'inzira 3 na function ya logique ya "majority" aho gukoresha half-adders zibiri.

Mu bikorwa, porogarama za Simplicity zikoresha jets ku bikorwa vy'ubuharuro na cryptography. Ariko jets zisubirira expressions gusa. Combinators zisubirwamwo hejuru ya buffers na vectors ntizishobora gusubirirwa na jets, kandi zigaragara muri porogarama nyakuri za Simplicity. Naho aho kuzikoresha ata guca hirya, abakoresha ba nyuma bakoresha indimi zo ku rwego rwo hejuru nka SimplicityHL zitanga izo expressions.

Combinators zisigurwa mu buryo recursive zisa n'izikura mu bunini bwa expression ku buryo exponential. Ibi si ingorane. Mu gihe ca serialization, expressions zishirwamwo nka DAGs (directed acyclic graphs) aho kuba trees. Uko ziserurwa vy'ukuri gukura gusa mu buryo linear.

Gushika ubu, ubuharuro pure gusa ni bwo twari twarimbuye. Gukorana n'amakuru ya transaction ku bikorwa nk'ugushira umukono kuri transactions bisaba uburyo bumwe bwo gutuma porogarama zinanirwa iyo imikono itari yo. Ikigabane gikurikira kivuga ku ngaruka zo ku ruhande muri Simplicity.

## Ingaruka Zibiri zo ku Ruhande

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

Mu bigabane vyabanje, twerekanye ingene twubaka data structures n'ubuharuro dukoresheje umugwi w'ishimikiro wa combinators za Simplicity. Nk'uko twabibonye, combinators z'ishimikiro zirahagije kugira ngo zishire mu ngiro ubuharuro pure ubwo ari bwo bwose bufise iherezo. Ivyo bizana ikibazo: ni ibindi iki bishobora gushikwako? Turashobora kwongerako ingaruka zo ku ruhande ku expressions zacu.

Hari ubwoko butandukanye bw'ingaruka zo ku ruhande zishoboka ku expressions: guhindura state, kwandika muri log, gutera exception, gusoma muri environment, guhamagara continuation, n'ibindi. Ingaruka zo ku ruhande ziboneka muri Simplicity zizovana n'aho ikoreshwa.

Ku bikorwa vya Bitcoin na Liquid, ubu dufise ingaruka zibiri zo ku ruhande: ingaruka ya Failure, ari ingaruka ya exception aho exception ifise ubwoko `𝟙`, n'ingaruka ya Reader ituma amakuru ava muri environment ya transaction ashobora gushikirwa. Combinators zacu z'ishimikiro ni "pure"; nta ngaruka zo ku ruhande zifise. Ariko jets zishobora kwinjiza primitives nshasha zifise ingaruka zo ku ruhande.

### Jets zifise Effects

Tuzovuga vyinshi ku bijanye na jets mu nyuma muri iri shure, ariko hano turatangiza uturorero duke twa jets kugira ngo twerekane ingaruka zazo zo ku ruhande.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` ni jet ya expression ifata x-only pubkey, ubutumwa bwa 256-bit, n'umukono wa Schnorr, igasubiza nothing! Dukurikije ubwoko bwayo, ikwiye kwitwara nka `unit`. Itandukaniro riri mu ngaruka zo ku ruhande za jet: iyo ukwemeza umukono binaniwe, ubuharuro bwose burahagarikwa mu gutera exception (y'ubwoko unit). Iyi ni ingaruka ya Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` ni jet yoroheje cane yo guserura ingaruka ya Failure. Iyo input ya `verify` ari `false`, ubuharuro bwose burahagarikwa mu gutera exception. Iyo input ari `true`, nta kintu gisubizwa, ariko ubuharuro burashobora kubandanya.

#### Transaction Hashes

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` isa n'aho ari function idahinduka, kuko hari value imwe gusa ishoboka ya input: tuple iri ubusa. Ariko iyi jet isoma muri environment ya transaction kandi igatanga hash y'amakuru ya transaction isa na message digest ya `SIGHASH_ALL` ikoreshwa mu kwemeza umukono muri Bitcoin Script. Iki ni akarorero k'ingaruka ya Reader: value isubizwa ivana na environment ya transaction jet ikoreramwo. Hari izindi jets nyinshi za hashing zihasha uduce dutandukanye tw'amakuru ya environment ya transaction kugira ngo zifashe kwubaka message digests yihariye y'imikono.

#### Introspection Jets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` ni function ifata index ya input igasubiza sequence number ya transaction kuri iyo input, canke igasubiza nothing iyo index iri hanze y'urugero. Na ho nyene, value ya output si function pure y'iyo input index, ahubwo, ico gikorwa gikoresha ingaruka ya Reader kugira ngo gishikire environment ya transaction kugira ngo kimenye value ya output. Hari izindi jets nyinshi za introspection zisubiza uduce dutandukanye tw'amakuru ya environment ya transaction.

### Gutandukanya Effects

Si ingaruka zo ku ruhande zose zingana. Zimwe mu ngaruka zo ku ruhande zitwara neza kuruta izindi. Turashobora gutandukanya effects hisunzwe ukuntu zemerera program transformations.

#### Commutative Effects

Commutative effect ni aho, iyo uhinduye ama outputs y'expressions zibiri, ushobora guhindura expressions ubwazo ata ngorane utahinduye effect y'iyo expression. Raba `swap = I H ▵ O H : A × B ⊢ B × A`. Iyo `f ▵ g ⨾ swap = g ▵ f` kuri expression yose `f` na `g` zifise ingaruka zo ku ruhande, rero effects ni commutative.

Gusoma amakuru ya transaction muri environment ni commutative effect kuko inyishu yo gusoma muri environment ari imwe, uko twoba twakurikiranije gusoma kose.

Muri rusangi, gutera exception si commutative effect. Iyo `f` iteye exception `e₁` kandi `g` igatera iyindi exception `e₂`, exception iterwa ivuye muri pair ya `f` na `g` ivana n'urutonde bikorerwamwo.

Ariko, mu kibazo kidasanzwe c'ingaruka ya Failure, aho exception y'ubwoko unit gusa ishobora guterwa, effect ni commutative. Uko `f` canke `g` yotera exception kwose, exception iva muri vyo izoba imwe, kuko hari value imwe gusa ishoboka ya exception.

#### Idempotent Effects

Idempotent effect ni aho, iyo usubiyemwo output y'expression, ushobora gusubiramwo expression ubwayo ata ngorane utahinduye effect y'iyo expression. Raba `dup = iden ▵ iden : A ⊢ A × A`. Iyo `f ⨾ dup = dup ⨾ f ▵ f` kuri `f` yose ifise ingaruka zo ku ruhande, rero effects ni idempotent.

Gusoma amakuru ya transaction muri environment ni idempotent effect. Gutera exception na vyo ni idempotent effect. Naho expression imwe gusa muri izo zibiri zasubiwemwo ari yo izokorwa, exception iyo ari yo yose iterwa na `dup ⨾ f ▵ f` izoba imwe n'exception iterwa na `f ⨾ dup`.

Ariko, kwandika muri log bishobora kutaba idempotent, kuko gusubiramwo effect vyotuma ubutumwa bwa log bugaragara kabiri. Ariko, iyo log igizwe na _set_ y'ubutumwa aho kuba _list_ y'ubutumwa, rero iyo effect yoba idempotent (kandi commutative) kuko kwinjiza muri set ubwavyo ari igikorwa idempotent.

#### Unitary Effects

Unitary effect ni aho, iyo uta output y'expression, ushobora guta expression ubwayo ata ngorane utahinduye effects z'iyo expression. Iyo vyama ari uko `f ⨾ unit = unit` kuri `f` yose ifise ingaruka zo ku ruhande, rero effects zawe ni unitary.

Gusoma amakuru muri environment ni bumwe mu bwoko buke bwa unitary effects. Iyo inyishu yo gusoma amakuru ya transaction muri environment itawe, expression yose ikora ukwo gusoma ishobora gutabwa.

Ingaruka ya failure si unitary. Iyo `f` iteye exception rero na `f ⨾ unit` izayitera; execution ntizoshika no kuri combinator `unit` imbere y'uko ubuharuro buhagarikwa. Ku rundi ruhande, `unit` biragaragara ko itotera exception iyo ari yo yose, rero effects za `f ⨾ unit` na `unit` zoba zitandukanye.

Mu ncamake, dore ingene effects twaganiriye hejuru zihagaze ku bijanye n'ivyo bintu bitatu:

| Effect | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (environment ya transaction) | ✓ | ✓ | ✓ |
| Failure (exception y'ubwoko unit) | ✓ | ✓ | ✗ |
| Writer (log nk'iset) | ✓ | ✓ | ✗ |
| Exceptions rusangi (ubwoko ubwo ari bwo bwose) | ✗ | ✓ | ✗ |

### Effects Zemewe muri Simplicity

Uko ubwoko bwa effect bufise ibintu vyiza vyinshi, ni ko optimizer ya Simplicity ironka umwanya munini wo guhindura porogarama zikoresha izo effects. Vyiza cane twokwemerera gusa effects zifise ivyo bintu vyose bitatu: commutative, idempotent, na unitary. Ivyo vyotuma optimizer ishobora gukora ubwoko ubwo ari bwo bwose bwa program transformation ishaka. Ariko gusoma muri environment ni yo effect yonyene ishitsa ivyo bintu bitatu vyose.

Ahubwo dusaba ko effects za Simplicity ziba commutative na idempotent. Effects zibiri dukoresha muri Simplicity, ingaruka ya Failure n'ingaruka ya Reader, ni commutative kandi ni idempotent. Ivyo bituma umugwi munini w'optimizations ushobora gukorwa kuri code ya Simplicity.

Ariko, transformation yo "guta" yasiguwe hejuru, igerageza gusubiriza `f ⨾ unit` na `unit`, canke transformation isa na yo iyo ari yo yose ntiyemewe iyo `f` ishobora gutanga ingaruka ya Failure. Ni ko biri koko, iyumvire iyo `f` yoba irimwo assertion ya `bip0340-verify`. Vyoba ari ivyago kugerageza gukuraho ico gisuzumwa biciye kuri optimization.

### Kubera iki Twemera Ingaruka zo ku Ruhande na Gato?

Kubera iki Simplicity yemera ingaruka zo ku ruhande na gato? Ntivyoba vyiza kuruta iyo porogarama yose ifata transaction yose nk'input maze igasubiza output ya Boolean igena nimba transaction yemewe canke itemewe?

#### Batch Verification

Imwe mu mpamvu dufise ingaruka ya Failure ni ugushigikira [batch verification](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) y'imikono ya Schnorr. Muri batch verification, amasuzuma menshi y'imikono ya Schnorr ashirwa hamwe ku buryo iyo isuzuma rimwe ry'umukono rinaniwe, batch yose inanirwa.

Ubu buryo bwo gushira hamwe butuma ibintu bikora neza kuruta kwemeza umukono wose ukwawo. Ingaruka mbi ni uko iyo batch verification inaniwe, tutamenya isuzuma ry'umukono ryihariye canke amasuzuma yananiwe.

Mu gukoresha ingaruka yo ku ruhande ya failure, `bip0340-verify` ireemeza ko iyo isuzuma ry'umukono rinaniwe, transaction yose inanirwa. Iyo `bip0340-verify` yari gusubiza `𝟚`, ubwoko bwa Boolean, ku kuroranirwa canke kunanirwa, isuzuma ry'umukono rinaniwe ryari kugishobora gushikana kw'ishami aho script iroranirwa. Muri ico gihe twari gukenera kumenya nimba uwo mukono wihariye wemewe canke utemewe, kandi rero ntitwari gushobora kwungukira kuri batch verification.

#### Amakuru ya Transaction Yabanje Guharurwa

Ingorane muri Bitcoin Script yo mu ntango yari uko hashing function ikoreshwa mu kurema message digests y'imikono yari linear mu bunini bwa transaction. Akenshi input yose irema nibura message digest imwe yo kwemeza umukono, rero mu rusangi ingano ya hashing yari quadratic mu bunini bwa transaction.

Iyo ngorane yakosowe muri Segwit no mu bindi bisubirwamwo vya Bitcoin Script mu gusubira gusigura message digests ku buryo zishobora guharurwa mu gihe constant kuri buri suzuma ry'umukono. Ivyo vyishimikiza kugira `PrecomputedTransactionData`, ibanza guharura hashes z'amakuru ya transaction rimwe hanyuma igasangira n'ama sighash computations ya buri input. Jets za hashing ya transaction za Simplicity zishingira kuri ubwo bwoko nyene bw'amakuru ya transaction yabanje guharurwa kugira ngo zemeze ko jets zikora mu gihe constant.

Dufate ko `sig-all-hash` itakoresha ingaruka ya Reader. Dufate ko mu buryo bumwe twashoboye kwubaka ubwoko bwa Simplicity bwa environment ya transaction. Reka tuyite `TxEnv`, ku buryo `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` yoba ari bwo bwoko bwa jet. Insiguro nk'iyo yosaba jet `sig-all-hash` gushobora guharura hash ya transaction iyo ari yo yose, si transaction irimwo gusa. Porogarama za Simplicity zoshobora gukopa `TxEnv` yahawe zikayihereza `sig-all-hash` nk'ikopi yahinduwe. Muri ico gihe `sig-all-hash` ntiyoshobora kwishimikiza `PrecomputedTransactionData`, kandi twosubira gusaba igihe linear mu makuru ya transaction ayo ari yo yose yoherezwa muri iyi version ya `sig-all-hash`.

Kubera ko `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` ikoresha ingaruka ya Reader kugira ngo ishikire amakuru ya transaction, ibona _gusa_ environment ya transaction idahinduka. Kubera iyo mpamvu, ishirwa mu ngiro rya jet rishobora gukoresha `PrecomputedTransactionData` mu mutekano kandi rigakora mu gihe constant.

### Cross-Input Signature Aggregation

Naho Liquid na Bitcoin ata n'imwe ishigikira [cross-input signature aggregation](https://hrf.org/latest/cisa-research-paper/) muri iki gihe, turashaka kugenzura ko Simplicity ishobora guhuza na yo igihe izoba igeze.

Naho ido n'ido ritarakorwa, twiyumvira half-aggregation izoshirwa mu ngiro hakoreshejwe ingaruka ya Writer. Ni ukuvuga, jet nshasha ifise ubwoko nka `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` yofata public key, message digest, n'igice `r` c'umukono wa Schnorr (umukono wa Schnorr ugizwe n'igice `r` n'igice `s`) ikavyandika muri log ya transaction imbere yo kubandanya execution. Hanyuma, ahandi muri transaction canke hamwe na transaction, igice `s` aggregate c'imikono yose ya Schnorr yakozwe half-aggregated cotangwa. Transaction yoba yemewe gusa iyo ico gice `s` aggregate gitanzwe ku mfunguruzo zose, ubutumwa bwose, n'ibice `r` vyanditswe muri log.

Kugira ngo ishikire ibisabwa vya Simplicity, iyi ngaruka ya Writer ikwiye kuba idempotent na commutative. Ivyo bishobora kwemezwa mu gufata writer log nk'iset y'ama tuples ya key, message, n'igice `r`. Ivyo bikora kuko ibikorwa vya set ari idempotent kandi commutative. Gufata log nk'iset ya values vyoba bihuye n'algorithm yo kwemeza half-aggregation.

### Iciyumviro ca nyuma

Muri iki kigabane twaravye ukongera ingaruka zo ku ruhande ku buharuro Simplicity ishobora gukora. Twatandukanije ubwoko butandukanye bwa effects hisunzwe ukuntu zitwara neza imbere y'ubwoko butandukanye bwa program transformation. Twafashe ingingo yo kugarukira ku effects za Simplicity ziba commutative na idempotent.

Effects zibiri dukoresha ku bikorwa vya Bitcoin na Liquid ni ingaruka ya Reader, yo gushikira environment ya transaction, n'ingaruka ya Failure, yo guhagarika no kunaniza porogarama. Jets zimwe zikoresha primitive operations aho ubu bwoko bw'ingaruka zo ku ruhande bushobora kuboneka.

Ingaruka ya Failure igena output ya porogarama ya Simplicity: porogarama canke irananirwa, transaction ikaba itemewe, canke porogarama iraroranirwa. Ingaruka ya Reader itanga ubwoko bumwe bwa input kuri porogarama ya Simplicity: environment irimwo amakuru ya transaction. Ariko kandi turakeneye gutanga izindi inputs, nk'imikono ya digital, kuri porogarama za Simplicity.

Mu kigabane gikurikira tuzoraba ico porogarama za Simplicity ari co, ingene zihindurwa amaderesi, n'ingene twongerako izindi inputs, nk'imikono, kuri porogarama za Simplicity.

## Porogarama n'Amaderesi

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

Mu kigabane cabanje twasiguye ingaruka zibiri zo ku ruhande zikoreshwa muri Simplicity: ingaruka ya Failure, igena ukuroranirwa canke ukunanirwa kwa porogarama, n'ingaruka ya Reader, itanga ubushobozi bwo gushikira environment ya transaction. Ubu duhindukirira ikibazo co mu bikorwa: porogarama ya Simplicity ni iki neza na neza, kandi icika gute aderesi kuri blockchain?

### Porogarama za Simplicity

Porogarama ya Simplicity isigurwa nk'expression ya Simplicity y'ubwoko `𝟙 ⊢ 𝟙`. Iyi type signature isobanura ko porogarama idafata input ifise insobanuro (gusa value ya unit) kandi idatanga output ifise insobanuro (gusa value ya unit). Ingaruka ya Reader ifata input ya environment ya transaction, mu gihe ingaruka ya Failure yerekana ukuroranirwa canke ukunanirwa. Izi effects zicunga I/O aho kuba ubwoko bwa Simplicity ubwabwo.

### Commitment Merkle Root

Aho kubika porogarama zuzuye on-chain, Bitcoin ikoresha commitments — umugenzo wavuye kuri Pay-to-Script-Hash (P2SH). Simplicity ikoresha Commitment Merkle Root (CMR).

Buri combinator ironka tag ya SHA-256 ikomoka ku pattern: `Simplicity␟Commitment␟[identifier]`, aho `␟` iserukira ASCII code 31 (unit separator).

Buri tag ni hash ya SHA-256 y'umurongo pre-image uhuye na yo uri hasi:

| Combinator | Tag pre-image (ASCII string) |
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

Expression ya Simplicity ica ihashwa mu buryo recursive ikaba CMR ya 256-bit mu guharura tagged SHA-256 midstate kuri buri combinator hamwe na CMRs z'arguments zayo (andika `#ᶜ(e)` ku CMR ya expression `e`, na `∥` ku gufatanya bytes):

| Combinator | Itegeko rya CMR |
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

Binary combinators (`comp`, `pair`, `case`) zifatanya CMRs z'abana bompi; unary combinators (`take`, `drop`, `injl`, `injr`) zifatanya CMR y'umwana wazo umwe inyuma ya bytes 32 za padding `0x00`; kandi nullary leaves (`iden`, `unit`) zihasha tag yazo yonyene. Conventions zibiri zituma ibi bihenduka guharura: SHA-256 midstates zirakoreshwa ku buryo **buri expression isaba guhamagara function ya SHA-256 compression incuro imwe gusa** (twiyumviriye ko midstate gushika kuri tags zidahinduka yabanje guharurwa), kandi constructors z'argument imwe zishira imbere argument yazo bytes 32 za padding `0x00`, ivyo bigatuma habaho akandi gatoya ko kubanza guharura ku mashirwa mu ngiro abishaka.

Ku combinator `unit` — constructor nullary idafise argument sub-expressions — iri tegeko rihinduka `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, aho `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (tag irinjizwa kabiri). CMR ivamwo ku porogarama yoroshe `unit` ni:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Ikihambaye cane, CMR ntiyishiramwo commitments ku bwoko bwa expressions za Simplicity, ahubwo yizigira type inference mu gihe co redemption.

### Amaderesi

Amaderesi akoresha uburyo bwa Taproot bwa BIP-0341 hamwe na CMRs zishirwa munsi ya TapLeaf version `0xbe`. Uburyo burimwo:

1. Guharura TapLeaf tagged hash ifatanya version byte, uburebure bwa CMR, na CMR ubwayo
2. Guhindura internal public key (ukoresheje NUMS point iyo ata key-spend path ishakwa)
3. Guhindura mu format ya bech32m
4. Kwongerako checksums zikwiye

Iyo ata key-spend path ishakwa, internal public key ishirwa kuri **NUMS** ("Nothing-Up-My-Sleeve") point: point yo kuri curve yahiswemwo ku bushake ku buryo ata n'umwe azi discrete logarithm yayo — mu yandi majambo, point idafise private key ihuye na yo. Kubera ko ata muntu ashobora na rimwe gutanga umukono wayo, key-spend path ntishobora gukoreshwa mu buryo bwemejwe, kandi output ishobora gukoreshwa *gusa* biciye ku nzira ya script ya Simplicity yashizwemwo commitment. Mu gikorwa nyakuri, iyi NUMS point ikwiye guhindurwa random nk'uko BIP-0341 ibishikiriza, kugira ngo outputs zidafise key-spend path ntizitandukanye n'outputs zisanzwe za Taproot (inyungu y'ubuzima bwite).

#### Kuva kuri Simplicity gushika kuri Aderesi

Reka tugende buhoro mu gukura kwose ku porogarama yoroshe ishoboka: `unit : 𝟙 ⊢ 𝟙`, no-op ihora iroranirwa.

**1. Tag ya combinator.** Banza uharure tag ya `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Injiza tag kabiri kugira ngo uronke CMR ya porogarama:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf hash.** Shira imbere ya CMR TapLeaf version ya Simplicity `0xbe` n'uburebure bwa CMR `0x20` (bytes 32), hanyuma ufate Elements TapLeaf tagged hash (tagged hash ni `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Kubera ko hari leaf imwe gusa, nta TapBranches zihari, rero iyi hash ni yo TapTree root.

**4. TapTweak.** Kubera ko dushaka ko ata key-spend path ibaho, dukoresha BIP-0341 NUMS point nk'internal key tukayitweak hamwe na TapTree root:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Output key.** Tweak internal key kuri curve, `output_pk = lift_x(internal_pk) ⊕ t·G` (ubuharuro bwa elliptic-curve buravugwa muri make hano), bigatanga x-only output key `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Aderesi ya Bech32m.** Encode x-only output key, shiramwo prefix `p` (inyuguti ya SegWit v1 witness-version), wongereko human-readable prefix ya Liquid-testnet `tex1`, hanyuma wongereko Bech32m checksum. Aderesi ya nyuma ni:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Ico cari igikorwa kinini — ariko igice kinini caco gitegetswe na Taproot ubwayo, si na Simplicity.

### Witness Expressions

Ubwoko bushasha bwa combinator burishura ukubura input muri porogarama za Simplicity: witness expression. Combinator `witness` iremera ko amakuru y'umukono n'ibindi bikoresho vya witness vyinjizwa muri porogarama.

```
      w : B
-----------------
witness w : A ⊢ B
```

Semantics ya witness expression iroroshe: irirengagiza input yayo maze igasubiza gusa value `w` (ishobora kuba ubwoko bwa Simplicity ubwo ari bwo bwose), ni ukuvuga `⟦witness w⟧(a) = w`. Ibi nta **bushobozi bushasha bwo guserura** bwongerako — dukurikije teoreme y'ukwuzura, Simplicity isanzwe ishobora kwubaka function iyo ari yo yose idahinduka nk'iyo (ibuka macro `scribe` yo mu bigabane vyabanje). Akamaro ka combinator `witness` kari muri **CMR** yayo gusa: value `w` **ntishirwa** muri CMR y'iyo expression, rero aderesi irashobora guharurwa imbere y'uko `w` imenyekana, kandi `w` itangwa mu gihe co redemption.

Iyi ngingo y'ubuhinguzi ishigikira pruning — amashami ya conditional adakoreshejwe ntakwiye guhishurwa on-chain, harimwo na witness expressions zayo. Iyo ishami ryaciwe, verifier akeneye gusa CMR ya subtree yaciwe, si ibiyirimwo vy'ukuri.

### Witness Values

Bishobora gusa n'aho ari imipaka kuba witness expression ishobora gufata gusa *value*, atari expression ya Simplicity rusangi kuruta. Ariko porogarama za blockchains zishingiye kuri UTXO zikorwa incuro imwe gusa. Nta mpamvu yo guha witness node sub-expression yose: umukoresha ashobora gukora iyo sub-expression ubwiwe, off-chain, hanyuma akandika output yayo muri witness value kugira ngo aronke inyishu imwe nyene.

(Mu nyuma muri iri shure tuzohura na combinator `disconnect`, yitwara cane nka witness expression *ifata* expression yose ya Simplicity nk'argument yayo.)

Ubundi buhinguzi bwoshobora kwinjiza amakuru yose ya witness nk'argument kuri porogarama ya Simplicity yo ku rwego rwo hejuru. Witness expressions zirakundwa kubera impamvu zibiri. Iya mbere, **pruning**: amashami adakoreshejwe ya expressions `case` ntiyigera ahishurwa on-chain, kandi witness expressions izo ari zo zose ziri muri ayo mashami zicibwa hamwe na yo. Iya kabiri, **locality**: witness expressions zituma dushira buri witness value neza aho ikoreshwa, aho kuyitwara tuyikuye kuri input yo ku rwego rwo hejuru ya porogarama.

### Type Inference

Kubera ko CMRs zitiyemeza ubwoko, sisitemu y'ubwoko irasubira kwubakwa mu gihe co redemption. Algorithm ya type inference ya Simplicity igena ubwoko buto bukenewe kuri buri subexpression hisunzwe structure ya combinator. Mu buryo bwuzuye kuruta, inference iharura ubwoko *principal* (rusangi kuruta) bwa buri subexpression; type variables izo ari zo zose zisigaye zidegemvya zica zishirwa kuri unit type `𝟙`, ivyo bigatanga ubwoko budasanzwe kandi buto bwa porogarama.

### Iciyumviro ca nyuma

Muri iki kigabane twashizeho ko porogarama za Simplicity ari expressions z'ubwoko `𝟙 ⊢ 𝟙`, twasiguye ingene Commitment Merkle Roots zubakwa zivuye kuri tagged SHA-256 hashes za buri combinator, kandi twerekanye ingene CMRs zihinduka amaderesi on-chain biciye kuri BIP-0341 Taproot. Twatangije witness expressions nk'uburyo bwo gutanga amakuru y'umukono n'izindi inputs mu gihe co gukoresha amahera ata gushira commitments ku values zazo mu gihe co kurema aderesi.

# Igice ca Nyuma

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Isubiramwo & Amanota

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Ikibazo ca Nyuma

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Iciyumviro ca nyuma

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
