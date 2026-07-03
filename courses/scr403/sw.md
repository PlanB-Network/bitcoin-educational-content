---
name: Kuzama Ndani ya Simplicity
goal: Kumudu falsafa ya usanifu, mfumo wa aina, na mzunguko kamili wa maisha wa Simplicity
objectives:
  - Kuelewa mbinu tatu za msingi za utungaji na kombineta tisa zinazounda lugha kamili
  - Kujenga mantiki ya boolean, arithmetiki, na SHA-256 kutoka kwenye mfumo mdogo wa aina wa Simplicity
  - Kuelewa jinsi athari za upande za Failure na Reader zinavyowezesha mwingiliano halisi wa blockchain
  - Kujifunza jinsi programu za Simplicity zinavyogeuka kuwa anwani za Taproot na kukombolewa kwa data ya witness
---

# Kuzama Ndani ya Simplicity

Uchunguzi wa kina wa nadharia na maamuzi ya usanifu nyuma ya lugha ya Simplicity, ukitokana na mfululizo kamili wa makala tano wa ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) na [Dr. Russell O'Connor](https://r6.ca/), mbunifu wa Simplicity katika Blockstream Research. Kozi hii inaeleza *kwa nini* Simplicity iliundwa jinsi ilivyo, si jinsi ya kuiandika.

Kozi inafuata makala za Dr. O'Connor kupitia njia tatu za msingi za kuchanganya ukokotoaji, mfumo mdogo wa aina na nadharia yake ya ukamilifu, ujenzi wa aina za data na arithmetiki za vitendo kutoka kanuni za kwanza, uingizaji makini wa athari za upande kwa mwingiliano wa blockchain, na hatimaye jinsi programu zinavyowekwa kama ahadi kwenye anwani na kukombolewa on-chain.

+++

# Utangulizi

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Muhtasari wa kozi

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Karibu SCR403 — Kuzama Ndani ya Simplicity!

Kozi hii inategemea mfululizo wa makala **"Delving Simplicity"** ulioandikwa na [Dr. Russell O'Connor](https://r6.ca/), Infrastructure Tech Developer katika [Blockstream](https://blockstream.com/) na mbunifu wa Simplicity. Makala asilia yalichapishwa kwenye jukwaa la [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) na yanaunda nyenzo kuu ya chanzo kwa kozi hii. Tunashukuru kwa kazi yake ya upainia, iliyoifanya maudhui haya ya kielimu yawezekane.

### Utakachojifunza

Kozi hii inachunguza falsafa ya usanifu na misingi ya kihisabati iliyo nyuma ya Simplicity, lugha ya scripting ya kizazi kijacho iliyowezeshwa kwenye [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) mnamo Julai 2025. Inafuata mfululizo kamili wa makala tano na imepangwa katika sehemu kuu mbili za maudhui:

1. **Misingi ya Simplicity** — Kwa nini ukokotoaji wa blockchain unahitaji lugha tofauti kimsingi, njia tatu za kuchanganya operesheni (mfuatano, sambamba, sharti), na kombineta tisa za msingi zinazounda lugha kamili kihisabati
2. **Kutoka Aina za Data hadi Programu** — Kujenga mantiki ya boolean, arithmetiki, na SHA-256 kutoka kanuni za kwanza; kuelewa athari za upande za Failure na Reader zinazowezesha mwingiliano wa blockchain; na kujifunza jinsi programu zinavyowekwa kama ahadi kwenye anwani za Taproot kupitia Commitment Merkle Roots na kukombolewa kwa data ya witness

### Mahitaji ya awali

Hii ni kozi ya **kiwango cha mtaalamu** (takriban saa 10). Unapaswa kuwa na uelewa wa:
- Dhana za msingi za scripting ya Bitcoin (uthibitishaji wa muamala hufanya nini)
- Dhana za msingi za programu (aina, functions, composition)
- Ufahamu fulani wa nukuu za kihisabati unasaidia lakini si lazima. Tutaanzisha kila kitu kadri tunavyoendelea

### Rasilimali muhimu

- **Makala asilia**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) na Dr. Russell O'Connor kwenye Delving Bitcoin
- **Hazina ya Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — code chanzi na uthibitisho rasmi wa Rocq
- **Tovuti rasmi**: [simplicity-lang.org](https://simplicity-lang.org/) — nyaraka na rejea ya SimplicityHL
- **Blogu ya Blockstream**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — muhtasari wa kiufundi

Uko tayari kuzama katika mojawapo ya vipande maridadi zaidi vya uhandisi wa Bitcoin? Twende!

## Simplicity ni nini?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Ikiwa unaingia kwenye kozi hii bila msingi wa Simplicity, sura hii itakuelekeza kabla hatujazama kwenye sehemu ya kina.

### Simplicity kwa kifupi

Simplicity ni **lugha ya smart contract asilia ya Bitcoin**, inayofanya kazi kwenye Liquid Network leo. Ilifikiriwa kwanza na Dr. Russell O'Connor karibu 2012 na kuelelezwa kwa kina katika karatasi yake ya 2017 *Simplicity: A New Language for Blockchains*, iliwezeshwa kwenye Liquid Network mnamo Julai 2025 baada ya miaka ya uthibitishaji rasmi na maendeleo.

Tofauti na Solidity ya Ethereum, ambayo ni lugha ya mikataba ya kiwango cha juu na Turing-complete, Simplicity ni ndogo kimakusudi. Ina:
- **Viundaji vitatu vya aina** (unit, sum, product)
- **Kombineta tisa** (operesheni za msingi na kanuni za utungaji)
- **Hakuna loops, hakuna recursion, hakuna kumbukumbu badilifu**

Kutokana na primitives hizi pekee, unaweza kujenga ukokotoaji wowote unaohitaji kwa uthibitishaji wa muamala, kutoka mantiki ya boolean hadi hashing kamili ya SHA-256.

### Unaweza kufanya nini na Simplicity leo?

Simplicity tayari inaendesha programu halisi kwenye Liquid Network. Iliyo mashuhuri zaidi ni [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), soko la options lisilotumia oracle ambapo watumiaji hufanya biashara ya call options kwenye L-BTC wakitumia USDt kama dhamana (mkataba wa msingi pia unaunga mkono puts). Miradi mingine hai ya Simplicity ni pamoja na [Swaption](https://swaption.io/) na SideSwap (options) na [Deadcat](https://github.com/Resolvr-io/deadcat) ya open-source na Resolvr (masoko ya utabiri). Zaidi ya DeFi, Simplicity inawezesha masharti ya juu ya matumizi kama vile vaults, covenants, na miundo changamano ya multisig ambayo isingewezekana au ingekuwa si salama katika Bitcoin Script.

### Kozi hii ni nini — na si nini

Hii **si** mafunzo ya vitendo ya kuandika code. Hutaandika programu za Simplicity hapa. Ikiwa unatafuta hilo, angalia:
- [simplicity-lang.org](https://simplicity-lang.org/) — nyaraka rasmi na lugha ya kiwango cha juu SimplicityHL
- [Hazina ya Simplicity GitHub](https://github.com/BlockstreamResearch/simplicity) — utekelezaji wa rejea, mifano, na uthibitisho wa Rocq
- [Chapisho la blogu la Blockstream](https://blog.blockstream.com/en-simplicity-github/) kuhusu kuanza

Kile kozi hii **inahusu**: **chaguo za kifalsafa na kiufundi** nyuma ya usanifu wa Simplicity. Kwa nini lugha hii iliundwa kwa namna hii? Kwa nini kombineta tisa tu? Kwa nini hakuna recursion? Kwa nini ni muhimu kwamba mfumo wa aina unaunganishwa na sequent calculus ya Gentzen?

Ifikirie kama kuelewa **kwa nini injini ilijengwa kwa namna hii** badala ya kujifunza kuendesha gari.

### Hii ni kwa ajili ya nani?

Kozi hii inafaa kwa:
- **Watengenezaji wa itifaki** wanaotaka kuelewa misingi ya Simplicity kabla ya kuandika code
- **Watafiti wa Bitcoin** wanaovutiwa na uthibitishaji rasmi na mkabala wa nadharia ya aina
- **Wanasayansi wa kompyuta** wanaotamani kujua uhusiano kati ya sequent calculus na ukokotoaji wa blockchain
- **Bitcoiners wa kiwango cha juu** wanaotaka kwenda zaidi ya uelewa wa juu juu wa uwezo wa scripting wa Liquid

Ikiwa istilahi kama "sum types", "combinators", au "sequent calculus" ni mpya kabisa kwako, usijali, tunaeleza kila kitu kutoka mwanzo. Lakini uwe tayari kwa safari nzito ya kihisabati.

### Kutoka makala hadi kozi

Mfululizo asilia wa "Delving Simplicity" wa Dr. O'Connor umepangwa kama makala tano za kiufundi. Kozi hii inapanga upya na kufafanua nyenzo hizo kuwa njia ya kujifunza inayoendelea pamoja na maswali ya kupima uelewa wako njiani. Mawazo, ufafanuzi, na uthibitisho ni wake, na tumebadilisha umbizo kwa ajili ya elimu iliyopangwa.

# Misingi ya Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Njia za Msingi za Kuchanganya Ukokotoaji

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Sasa kwa kuwa Simplicity imewezeshwa kwenye Liquid Network, ningependa kufanya uchunguzi wa kina wa falsafa na usanifu wa lugha ya Simplicity.

Uthibitishaji wa miamala ya Bitcoin ni matumizi tofauti sana na usanifu wa lugha za kawaida za programu. Gharama ya nafasi ya block ni ya juu, kwa hivyo programu zinahitaji kuwa fupi. Programu katika miamala ya Bitcoin huwa zinatekelezwa kwenye input moja tu na kila mtu hutekeleza programu kwenye input ileile. Pia, mhusika anayeidhinisha muamala tayari anajua matokeo ya ukokotoaji mapema: kwamba muamala ni halali.

Kwa kawaida mhusika anayeidhinisha atatekeleza ukokotoaji wenye gharama kubwa zaidi ili kupata data ya witness inayothibitisha uhalali wa muamala, ilhali programu zinazoendeshwa kwenye blockchain zinahitaji kuangalia uhalali wa data ya witness. Kukagua uhalali mara nyingi ni nafuu zaidi kuliko kuthibitisha uhalali.

Tumeunda Simplicity tukizingatia changamoto hizi za kipekee za usanifu wa lugha. Kwa mfano, Simplicity inahitaji matawi yasiyotekelezwa yapogolewe ili yasionekane kwenye blockchain. Hatua za preprocessing zimeundwa kwa uangalifu ili kuonyesha uchangamano wa muda wa (takriban) mstari kulingana na ukubwa wa programu ya Simplicity. Uchambuzi tuli hutumiwa badala ya "gas", ambayo haiwezi kukokotolewa bila kutekeleza code kwa namna iliyowekwa, ili maelezo ya modeli ya utekelezaji yasiwe muhimu kwa consensus. Hakuna ugawaji badilifu wa kumbukumbu wakati wa utekelezaji. Na kadhalika.

Kabla ya kuzama katika maelezo ya usanifu wa Simplicity, nataka kuanza mfululizo huu kwa falsafa ya programu kuhusu njia za jumla za kuchanganya vipande vya msingi ili kuunda utendaji mpya.

### Utungaji

Tuseme mtu anabuni lugha ya miamala inayoweza kupangwa kwa blockchain kama Bitcoin. Hasa, programu zinaweza kufikia tu data ya muamala na data ya UTXO ya inputs, na utekelezaji huamua tu uhalali wa muamala (jambo linaloruhusu matokeo ya utekelezaji kuwekwa kwenye cache). Tuseme mtu anaanza na seti fulani ya operesheni za msingi zinazoweza kutekeleza kazi mbalimbali kama ukokotoaji wa msingi, kusoma na/au kuchakata data kutoka kwenye muamala, na uthibitishaji wa saini. Kila operesheni hutumia aina fulani ya input (huenda tupu) na kurudisha aina fulani ya output. Ni njia gani tunaweza kutumia kuchanganya operesheni hizi za msingi kuwa operesheni changamano zaidi?

### Utungaji wa Mfuatano

![Utungaji wa Mfuatano](assets/en/001.webp)

Mbinu ya msingi zaidi ya utungaji ni utungaji wa mfuatano. Ikiwa tuna operesheni mbili za msingi, moja ambayo aina ya data ya output yake inalingana na aina ya data ya input ya nyingine, basi tunaweza kuchanganya operesheni hizi mbili kuwa operesheni mpya ya pamoja. Operesheni hii mpya huendesha operesheni hizi mbili za msingi kwa mfuatano, ikichukua kama input input ya operesheni ya kwanza, ikipitisha output ya operesheni hiyo ya kwanza kwenye input ya operesheni ya pili, na hatimaye kurudisha output ya operesheni hiyo ya pili.

Bila shaka, hatuhitaji kujizuia kuchanganya operesheni za msingi tu. Sasa kwa kuwa tuna operesheni za pamoja, tunaweza pia kuchanganya hizo kwa kutumia utungaji wa kifunction.

Katika hisabati, utungaji huu wa mfuatano mara nyingi huitwa tu "composition", na mtu anaweza kufikiri kuwa hii ndiyo njia pekee ya kutunga vitu. Hata hivyo, tuna njia nyingine za kutunga operesheni.

### Utungaji Sambamba

![Utungaji Sambamba](assets/en/002.webp)

Tuseme tuna operesheni mbili, zinaweza kuwa operesheni za msingi au changamano, na zote zinachukua aina ileile ya input. Njia ya pili ya msingi ya kutunga operesheni hizi mbili ni kuzitekeleza zote kwenye input ileile. Hii inaitwa utungaji sambamba, na aina ya output ni "product" ya aina za outputs za operesheni asilia na ina jozi ya outputs hizo mbili.

Ingawa huu unaitwa utungaji "sambamba", na operesheni hizo mbili zinaweza kimsingi kutekelezwa sambamba, utekelezaji sambamba si hitaji la kiutendaji. Tunaweza kutekeleza utungaji sambamba "kwa mfuatano" kwa kutekeleza operesheni moja kwanza kisha operesheni ya pili. Hatubebi uzito wa maelezo ya jinsi utungaji sambamba unavyotekelezwa mradi output iwe ileile.

### Utungaji wa Masharti

![Utungaji wa Masharti](assets/en/003.webp)

Utungaji wa masharti ni dual ya utungaji sambamba. Katika hali hii tuna operesheni mbili zinazozalisha output ileile, na tunazitunga kwa kuchagua mojawapo itekelezwe. Input ya operesheni hii ya pamoja ni "sum" au "tagged union" ya aina za inputs za operesheni asilia. Katika tukio hili tag, "Left" au "Right", ni bit moja katika data ya input inayobainisha ni aina gani ya data inayobebwa, na hivyo ni ipi kati ya operesheni mbili inaweza kutekelezwa.

Utungaji wa masharti hufanya kazi vivyo hivyo hata wakati input ni sum ya aina mbili zinazofanana. Aina ya sum bado ina tag, na thamani ya tag hiyo huamua ni ipi kati ya operesheni mbili itatekelezwa.

### Utungaji katika Bitcoin Script

Kuna njia nyingi za kutekeleza aina hizi tatu za utungaji katika lugha mbalimbali za programu. Katika Bitcoin Script, utungaji wa mfuatano hutekelezwa (takriban) kwa kuunganisha routines mbili (hii ndiyo sababu Bitcoin Script huitwa lugha ya programu ya concatenative) kwa kuwa output ya routine moja huachwa kwenye stack ili itumiwe na routine inayofuata. Utungaji sambamba hupatikana kwa kutumia operesheni za duplicate na swap kuendesha stack ili routines mbili ziweze kuendeshwa kwenye input ileile. Mambo si ya moja kwa moja kabisa kwa sababu kile tunachokiita "product" ya aina kwa kawaida hutekelezwa kwa kutumia items kadhaa za stack. Tunatumaini unaweza kuona wazo la jumla.

Bila shaka, utungaji wa masharti hutekelezwa na `OP_IF` ambayo hutawi kulingana na thamani iliyo kwenye stack. Katika hali hii item ya juu ya stack hucheza nafasi ya tag, na kwa kawaida item au items zinazofuata kwenye stack ni za "aina" tofauti zinazotegemea thamani ya tag. Kwa kila hali, aina za items za stack zinaweza kufaa kuchakatwa tu na mojawapo ya matawi katika `OP_IF`. Hata hivyo baada ya kufikia `OP_ENDIF` items za stack lazima ziwe na "aina" thabiti kiasi kwamba script iliyobaki inaweza kuendelea bila kujali tawi gani lilichukuliwa awali.

### Utungaji katika Simplicity

Tuliunda Simplicity kwa kombineta zinazotekeleza moja kwa moja aina hizi tatu za utungaji. Pamoja na kombineta chache zaidi kusaidia operesheni nyingine za msingi zinazohusiana na aina za product na sum, lugha ya msingi ya Simplicity huishia kuwa na kombineta tisa zinazotosha kueleza ukokotoaji wowote finiti. Tutajadili hili kwa kina zaidi katika sura inayofuata.

### Aina ya Nne ya Utungaji

Kabla ya kumaliza tunapaswa kutaja kuwa kuna angalau aina moja zaidi ya utungaji inayopatikana katika Computer Science, ambayo ni "recursive composition". Katika recursive composition operesheni moja hurudiwa mara nyingi.

Kumbuka kwamba Bitcoin Script haiungi mkono recursive composition, na vivyo hivyo, tumeondoa waziwazi recursion isiyo na kikomo katika usanifu wa Simplicity. Hoja yetu ni kwamba ukokotoaji wa kurudia usio na kikomo ni bora kutekelezwa kwa kutumia recursive covenants zinazokokotoa juu ya miamala mingi. Hii inaruhusu watumiaji kuepuka vikwazo vya nafasi ya block na standardness na kutabiri vizuri zaidi gharama za muamala.

Hata hivyo, kuna njia za kutumia vibaya kipengele cha delegation cha Simplicity ili kutoa kitu kinachofanana na recursive composition isiyo na kikomo, ambacho tunaweza kujadili baadaye katika mfululizo huu.

### Hitimisho

Tulipitia aina tatu kuu za utungaji kwa kubadilisha operesheni za msingi kuwa operesheni changamano:

- utungaji wa mfuatano
- utungaji sambamba
- utungaji wa masharti

Tulijadili jinsi aina hizi za utungaji zinavyotekelezwa katika Bitcoin Script, na tukadokeza jinsi zilivyoathiri usanifu wa lugha ya Simplicity. Tulibainisha kwamba aina ya nne ya utungaji, recursive composition, imeondolewa mahsusi katika Simplicity na Bitcoin Script.

Katika sura inayofuata tutaeleza kombineta tisa zinazounda kiini cha lugha ya Simplicity, jinsi zinavyotumika kutekeleza moja kwa moja aina hizi tatu za utungaji, na jinsi hili linavyounda lugha kamili ya kueleza ukokotoaji wowote finiti.

## Ukamilifu wa Kombineta wa Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

Katika sura hii tunaanzisha lugha ya msingi ya Simplicity na kuonyesha kwamba lugha hiyo ni kamili, ikimaanisha kuwa ukokotoaji wowote finiti unaweza kuonyeshwa ndani yake.

### Aina za Simplicity

Simplicity inaunga mkono wajenzi watatu wa msingi wa aina. Aina ya product `A × B` inawakilisha outputs za utungaji sambamba, ilhali aina ya sum `A + B` (tagged union) hushughulikia inputs za utungaji wa masharti. Aina ya tatu ni aina ya unit.

### Aina ya Unit

Aina ya unit, inayoashiriwa `𝟙` au `ONE`, ina thamani moja tu: tuple tupu `⟨⟩` au `()`. Aina hii ya data ya zero-bit haibebi taarifa yoyote.

### Aina ya Sum

Aina ya sum `A + B` huchanganya aina mbili kwa tag zinazoonyesha "left" au "right." Thamani huandikwa kama `σᴸ(a)` au `inl(a)` kwa thamani zenye tag ya kushoto na `σᴿ(b)` au `inr(b)` kwa thamani zenye tag ya kulia. Tag hubaki tofauti hata wakati wa kuchanganya aina zinazofanana.

#### Aina ya Boolean

Aina `𝟙 + 𝟙`, inayoashiriwa `𝟚` au `TWO`, inawakilisha aina ya one-bit yenye thamani mbili. Kwa kawaida, `σᴸ⟨⟩` inawakilisha false/zero, ilhali `σᴿ⟨⟩` inawakilisha true/one.

### Aina ya Product

Aina za product `A × B` zina jozi za thamani zilizoandikwa kama `⟨a, b⟩` au `(a, b)`. Aina `𝟚 × 𝟚` ina thamani nne, tofauti na thamani nne katika `𝟚 + 𝟚`.

### Expressions za Msingi za Simplicity

Operesheni huashiriwa kama `f : A ⊢ B`, ikimaanisha aina ya input `A` na aina ya output `B`. Simplicity ni "first-order" — haina aina za function.

### Operesheni Mbili za Msingi

Lugha ya msingi hutoa operesheni mbili za msingi:

**Identity (`iden`).** Operesheni ya identity hupitisha input yake bila kubadilisha:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Operesheni ya unit hutupa input yake na kurudisha tuple tupu:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Hizi huunda familia zenye operesheni moja kwa kila aina.

### Kombineta Tatu za Utungaji

Utungaji wa mfuatano hutumia `comp f g` (huandikwa `f ⨾ g` au `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Utungaji sambamba hutumia `pair f g` (huandikwa `f ▵ g` au `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Utungaji wa masharti hutumia `case f g : (A + B) × C ⊢ D`, ukitoa matawi ufikiaji wa mazingira ya pamoja `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Kwa nini utungaji wa masharti una umbo hili — sum iliyounganishwa na mazingira ya pamoja `C` — badala ya `copair f g : A + B ⊢ C` rahisi zaidi inayochagua tu tawi? Kwa sababu `copair` tupu haiwezi kueleza **distribution**: function `dist : (A + B) × C ⊢ A × C + B × C` inayosukuma input ya pamoja kwenye tawi lolote linalochukuliwa. Kwa kujenga mazingira `C` moja kwa moja ndani ya `case`, Simplicity inapata utungaji wa masharti *na* distribution kutoka kombineta moja — mojawapo ya maamuzi muhimu ya usanifu yanayoweka lugha ya msingi kuwa kombineta tisa tu.

### Kombineta Nne Zaidi

Utumiaji wa product hutumia `take` na `drop`:

**take** huchomoa elementi ya kushoto:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** huchomoa elementi ya kulia:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Uzalishaji wa sum hutumia `injl` na `injr`:

**injl** hufunga kwa tag ya kushoto:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** hufunga kwa tag ya kulia:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Kombineta Tisa za Msingi

Kwa jumla, Simplicity ina kombineta tisa haswa za msingi:

| Kombineta | Kusudi |
|---|---|
| `iden` | Kupitisha input |
| `unit` | Kutupa input |
| `comp` | Utungaji wa mfuatano |
| `pair` | Utungaji sambamba |
| `case` | Utungaji wa masharti |
| `take` | Kuchomoa kushoto kutoka product |
| `drop` | Kuchomoa kulia kutoka product |
| `injl` | Kuingiza upande wa kushoto wa sum |
| `injr` | Kuingiza upande wa kulia wa sum |

### Simplicity na Sequent Calculus

Usanifu wa Simplicity unatokana na kipande cha conjunctive-disjunctive cha sequent calculus ya Gentzen. Kwa usahihi zaidi, ni lahaja ya *functional interpretation* ya sequent calculus, ambayo yenyewe inafanana na correspondence ya Curry-Howard kati ya natural deduction na lambda calculus. Kanuni za kombineta zinaonyesha "aina ndogo katika premises kuliko conclusions," zikiliwezesha Bit Machine — mkalimani wa abstract stack machine wa Simplicity — kupunguza kunakili data wakati wa utekelezaji.

### Thamani si Expressions

Expressions za Simplicity huashiria operesheni, si thamani. Nukuu `scribe b : A ⊢ B` inawakilisha expression ya kipekee inayorudisha kila mara thamani `b`, ikitumika kama urahisi wa nukuu badala ya kombineta. Hii inafanana na Bitcoin Script, ambapo operesheni kama `OP_1` husukuma thamani badala ya kuzionyesha moja kwa moja.

### Nadharia ya Ukamilifu ya Simplicity

Tukiwa na kombineta zote tisa, tunajuaje kwamba hatukosi kitu — kwamba hizi tisa kweli zinatosha? Nadharia ya Ukamilifu ya Simplicity inajibu hili: kwa function yoyote kati ya aina (finiti) za Simplicity, expression fulani ya Simplicity huiashiria. Uthibitisho ni wa kijenzi — unaonyesha jinsi ya kujenga expression:

1. **Vunja input**: Kwa kutumia expressions za `case` zilizopachikwa, vunja kikamilifu input yoyote ya aina yoyote katika bits zake zinazoiunda
2. **Jenga lookup table**: Kwa kila input inayowezekana, tumia `scribe` kuzalisha output inayolingana
3. **Unganisha**: Cases zilizopachikwa na scribes pamoja huunda lookup table kubwa inayotekeleza function

Nadharia hii imethibitishwa rasmi katika proof assistant Rocq (zamani Coq). Uthibitisho ni sehemu ya hazina rasmi ya Simplicity na umekaguliwa na mashine kwa usahihi.

Ingawa nadharia ya ukamilifu inahakikisha kwamba kombineta tisa za Simplicity zinaweza kueleza function yoyote kati ya aina (finiti) za Simplicity, expressions zinazotokana na ujenzi wa lookup-table ni kubwa kupita kiasi kwa matumizi ya vitendo. Function kwenye inputs za 256-bit ingehitaji lookup table yenye entries 2²⁵⁶. Hii ndiyo sababu sura zinazofuata zinalenga kujenga expressions bora zinazotumia muundo wa ukokotoaji, badala ya kulazimisha kila kitu kupitia lookup tables.

### Hitimisho

Lugha ya msingi ya Simplicity inajumuisha mfumo wa aina na kombineta zinazowezesha ukokotoaji wowote finiti. Ingawa nadharia ya Ukamilifu inahakikisha uwezo wa kujieleza, expressions zinazotokana na ujenzi wa jumla ni kubwa kupita kiasi kwa matumizi ya vitendo. Maendeleo ya vitendo ya Simplicity yanahusisha kutumia muundo wa ukokotoaji kupata expressions fupi. Sura zinazofuata zinachunguza miundo ya data, mwingiliano wa miamala, na kombineta za ziada.

# Kutoka Aina za Data hadi Programu

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Kujenga Aina za Data

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

Katika sura zilizopita, tulionyesha jinsi seti ya msingi ya kombineta za Simplicity inavyotosha kutekeleza ukokotoaji wowote safi ulio finiti. Sura hii inaonyesha jinsi ya kujenga miundo ya data na ukokotoaji wa vitendo kutoka primitives hizi — kwa njia ileile kompyuta zinavyojengwa kutoka logic gates.

### Mantiki ya Boolean

Aina ya Boolean, inayoashiriwa `𝟚`, ni sawa na `𝟙 + 𝟙` na ina thamani mbili: `σᴸ⟨⟩` (false) na `σᴿ⟨⟩` (true). Kwa kutumia kombineta za msingi, waendeshaji wa mantiki ya Boolean wanaweza kujengwa.

#### Operesheni ya And

Operesheni ya kimantiki `and : 𝟚 × 𝟚 ⊢ 𝟚` huchukua bits mbili na kurudisha bit moja. Utekelezaji hutawi kwenye bit ya kwanza: ikiwa false, rudisha false; vinginevyo, rudisha bit ya pili.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Kujaribu kwa `⟨false, false⟩`:

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

Kujaribu kwa `⟨true, true⟩`:

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

#### Operesheni Nyingine za Mantiki

Operesheni `not` inahitaji kombineta msaidizi:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

`iden ▵ unit : A ⊢ A × 𝟙` ya awali huongeza "mazingira" tupu kwenye input, ikiwezesha kombineta `case` kutumika. Matumizi ya `take` katika matawi mawili hutupa mazingira haya tupu ili kutekeleza `f` au `g`.

Operesheni nyingine za kimantiki za Boolean:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bit Adders

"Half-adder" huchukua bits mbili na kuziongeza, ikizalisha output ya bits mbili: bit ya carry na bit ya sum.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

"Full-adder" huongeza bits tatu, ikizalisha output ya bits mbili. Input hutumia tuple iliyopachikwa `(𝟚 × 𝟚) × 𝟚`.

Kwa tuples zilizopachikwa, nukuu fupi hutumiwa:

- `O f` huashiria `take f`
- `I f` huashiria `drop f`
- `H` huashiria `iden`

Kwa mfano, `I O H` humaanisha `drop (take iden) : A × (B × C) ⊢ B`, ikichomoa thamani ya kati. Nukuu hii hukumbusha tarakimu za binary: unapofikiria tuples zilizopachikwa kama miti ya binary, nukuu inawakilisha tarakimu za binary zilizogeuzwa za nafasi za mti. Expressions hizi huunda indices za De Bruijn kwa Simplicity.

**Kumbuka:** Nukuu za `I`, `O`, na `H` hutumika tu kwa subexpressions zinazoundwa pekee na `take`, `drop`, na `iden`.

Full-adder hutunga half-adders mbili, ikichukua `or` ya kimantiki ya bits za carry:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

Katika mstari wa kwanza, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` huendesha half-adder kwenye bits mbili za kwanza, ikihifadhi bit ya mwisho.

Katika mstari wa pili, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` huhifadhi bit ya kwanza (carry-out ya half-adder ya kwanza) na kuendesha half-adder kwenye bits mbili za mwisho.

Katika mstari wa mwisho, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` huchukua OR ya kimantiki ya bits mbili za kwanza (carry-outs za half-adders zote mbili) na kurudisha bit ya sum-out ya half-adder ya pili.

Hili linaonyesha programu ya Simplicity: kutumia nukuu za `I`, `O`, na `H` kurejelea bits za data, kuunda "mazingira" yanayofaa kwa kuita functions nyingine kupitia utungaji wa mfuatano.

Watumiaji hawafafanui operesheni za kiwango cha chini moja kwa moja. Baadaye mfululizo huu unajadili jets za standard library zinazotekeleza functions za kawaida. Watumiaji wa mwisho hawatarajiwi kupanga programu moja kwa moja katika Simplicity, sawa na Bitcoin Script. Badala yake, lugha za kiwango cha juu kama SimplicityHL huzalisha code ya Simplicity, zikisimamia "mazingira" ya subexpression na kutafsiri variables zenye majina kuwa mifuatano inayofaa ya `take` na `drop`.

### Vectors

Vectors zenye urefu uliowekwa hufafanuliwa kwa kuunda products zilizorudiwa za aina `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Hizi zinaweza kuandikwa kama `A^2`, `A^4`, `A^8`, n.k.

Vectors hufafanuliwa tu kwa urefu ambao ni powers of two. Powers nyingine zinahitaji kuchagua conventions za kuweka mabano.

Kwa expression `f : A ⊢ B`, pairing inayorudiwa "huimap" juu ya vectors zenye urefu uliowekwa:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Kwa function `f : A × B ⊢ B`, iteration au "folding" juu ya vectors zenye urefu uliowekwa:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Kuna tofauti nyingi. Kwa `f : A × B ⊢ C`, "zip" juu ya vectors zilizooanishwa kwa `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Kwa `f : (A × B) × C ⊢ C`, fold juu ya vectors zilizooanishwa kwa `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Kuchanganya `map` na `fold-right` huunda kombineta zinazokusanya: `f : A × C ⊢ C × B` hutoa `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Lahaja nyingi zaidi zinawezekana.

#### Maneno ya Bits Nyingi

Vector ya bits hutoa integers za bits nyingi. Kwa mfano, `𝟚³²` ni aina ya neno la 32-bit. `𝟚²⁵⁶` ni aina ya neno la 256-bit, inayofaa kwa hashes na operesheni za kriptografia.

Kwa kutumia full-adder, lahaja ya operesheni za vector hufafanua "ripple carry adder" juu ya maneno ya bits nyingi:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` huchukua nambari mbili za binary za n-bit na carry-input ya bit moja, ikirudisha bendera ya carry-out ya bit moja na sum ya n-bit.

#### SHA-256

Kwa kufafanua kwa recursion operesheni za arithmetiki kwenye maneno ya bits nyingi — subtraction, multiplication, division — na operesheni za kimantiki za bit-wise kama logical AND, OR, XOR, na kuchanganya hizi mara kwa mara, hata function ya compression ya block ya SHA-256 inaweza kujengwa:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

Compression ya SHA-256 imefafanuliwa rasmi kwa kutumia Simplicity ndani ya proof assistant Rocq (zamani Coq), ikiwa na uthibitisho rasmi kwamba utekelezaji wa `sha256-hash-block` ni sahihi.

Compression huenda polepole sana kama Simplicity ghafi. Jets hutekeleza functions za kawaida kama compression ya SHA-256 kwa native code. Utekelezaji safi wa Simplicity hutumika kama specifications rasmi kwa jets.

### Aina za Option

Aina za option hutokana na kuchukua sum pamoja na aina ya unit:

```
Option A ≔ 𝟙 + A
```

Aina `Option A` inaweza kuandikwa kama `A?` au `𝕊 A` (ambapo `𝕊` humaanisha "successor"). Functions hu-map juu ya aina za option:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Kombineta za monadic kama bind zinaweza kufafanuliwa:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffers za Urefu Badilika

"Buffers" ni aina za vectors zilizojazwa kwa sehemu:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Aina `Xᑉ⁸` hupanuka kuwa `(1 + X⁴) × ((1 + X²) × (1 + X))`. Kuichukulia hii kama polynomial na kuipanua hutoa `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Ikiitafsiri kama aina, inawakilisha sum ya tuples zote zinazowezekana za X hadi 7, pamoja na tuple tupu. Hii ndiyo hasa aina ya orodha zenye urefu chini kabisa ya 8.

Kama vectors, operesheni za mapping na folding zinaweza kufafanuliwa juu ya buffers. Operesheni za stack ni pamoja na `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` na `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` huongeza item kwenye mwisho wa buffer, ikirudisha vector kamili ikiwa overflow inatokea. `pop-<n` huondoa item, ikirudisha buffer ndogo zaidi na item iliyoondolewa, kwa hiari ikirudisha nothing ikiwa buffer asilia ilikuwa tupu.

Ufafanuzi wa `push-<n`, kwa recursion:

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

Simplicity ghafi huwa vigumu kufuata baada ya viwango fulani vya uchangamano. Watumiaji wa mwisho hutumia lugha za kiwango cha juu kama SimplicityHL zinazozalisha expressions hizi za kimatamshi.

### Hitimisho

Sura hii ilionyesha jinsi ya kujenga operesheni za kimantiki kutoka bits. Kutoka humo, arithmetiki ya kiwango cha bit iliibuka, ikiwezesha kufikiri kuhusu utekelezaji. Aina za vector ziliendelezwa, zikionyesha iteration juu ya maneno ya bits nyingi kwa ufafanuzi wa arithmetiki. Kuendelea, operesheni za kriptografia kama SHA-256 na uthibitishaji wa saini za Schnorr zinaweza kufafanuliwa kwa kutumia kombineta za Simplicity pekee — zote kwa kweli zimefafanuliwa kwa kutumia Simplicity.

Sura hii si mwongozo kamili wa aina zote za data na operesheni zinazoweza kujengwa katika Simplicity, bali inaonyesha kufikia utendaji wa vitendo ndani ya vikwazo vya Simplicity. Licha ya aina zilizo na mipaka finiti, vectors muhimu, aina za buffer, na operesheni zinazofanya iteration juu ya miundo hii zinaweza kufafanuliwa.

Specifications halisi za operesheni za standard library hutofautiana kidogo na ufafanuzi hapa. Kwa mfano, full-adder hutumia XOR ya njia 3 na function ya mantiki ya "majority" badala ya half-adders mbili.

Kwa vitendo, programu za Simplicity hutumia jets kwa operesheni za arithmetiki na kriptografia. Hata hivyo, jets hubadilisha expressions tu. Kombineta zinazofanya iteration juu ya buffers na vectors haziwezi kubadilishwa na jets, na huonekana katika programu halisi za Simplicity. Ingawa badala ya kuzitumia moja kwa moja, watumiaji wa mwisho hutumia lugha za kiwango cha juu kama SimplicityHL zinazozalisha expressions kama hizo.

Kombineta zilizofafanuliwa kwa recursion huonekana kukua kwa ukubwa wa expression kwa namna ya exponential. Hili si tatizo. Wakati wa serialization, expressions husimbwa kama DAGs (directed acyclic graphs) badala ya trees. Uwakilishi halisi hukua kwa mstari tu.

Kufikia sasa, ukokotoaji safi pekee ndio ulizingatiwa. Mwingiliano na data ya muamala kwa kazi kama kutia saini miamala unahitaji njia fulani ya kufanya programu zishindwe ikiwa saini si halali. Sura inayofuata inajadili side-effects katika Simplicity.

## Athari Mbili za Upande

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

Katika sura zilizopita, tulionyesha jinsi ya kujenga baadhi ya miundo ya data na ukokotoaji kwa kutumia seti ya msingi ya kombineta za Simplicity. Kama tulivyobainisha, kombineta za msingi zinatosha kutekeleza ukokotoaji wowote safi ulio finiti. Hili linazua swali: ni nini kingine kinaweza kufikiwa? Tunaweza kuongeza athari za upande za ziada kwenye expressions zetu.

Kuna aina mbalimbali za athari za upande zinazowezekana kwa expressions: kusasisha state, kuandika kwenye logi, kurusha exception, kusoma kutoka mazingira, kuita continuation, n.k. Athari za upande zinazopatikana katika Simplicity zitategemea matumizi.

Kwa matumizi ya Bitcoin na Liquid, kwa sasa tuna athari mbili za upande: athari ya Failure, ambayo ni athari ya exception ambapo exception ina aina `𝟙`, na athari ya Reader inayoruhusu data kutoka mazingira ya muamala kufikiwa. Kombineta zetu za msingi ni "safi"; hazina athari za upande. Hata hivyo, jets zinaweza kuanzisha primitives mpya ambazo zina athari za upande.

### Jets zenye Athari

Tutazungumza zaidi kuhusu jets baadaye katika kozi hii, lakini hapa tunaanzisha jets chache za mfano kuonyesha athari zake za upande.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` ni jet kwa expression inayochukua x-only pubkey, ujumbe wa 256-bit, na saini ya Schnorr, na hairudishi chochote! Kulingana na aina yake, inapaswa kutenda sawa na `unit`. Tofauti iko katika athari ya upande ya jet: ikiwa uthibitishaji wa saini unashindwa, basi ukokotoaji mzima hukatizwa kwa kurusha exception (ya aina ya unit). Hii ni athari ya Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` ni jet ya msingi kabisa ya kueleza athari ya Failure. Ikiwa input ya `verify` ni `false`, ukokotoaji mzima hukatizwa, kwa kurusha exception. Ikiwa input ni `true`, hakuna kinachorudishwa, lakini ukokotoaji unaweza kuendelea.

#### Hashes za Muamala

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` inaonekana kuwa function ya constant, kwa kuwa kuna thamani moja tu ya input inayowezekana: tuple tupu. Hata hivyo, jet hii husoma kutoka mazingira ya muamala na huzalisha hash ya data ya muamala inayofanana na message digest ya `SIGHASH_ALL` inayotumika katika uthibitishaji wa saini wa Bitcoin Script. Huu ni mfano wa athari ya Reader: thamani inayorudishwa hutegemea mazingira ya muamala ambamo jet inatekelezwa. Kuna jets nyingine kadhaa za hashing zinazohash subsets mbalimbali za data ya mazingira ya muamala ili kusaidia kujenga message digests maalum kwa saini.

#### Jets za Introspection

`input-sequence : 𝟚³² ⊢ 𝟚³²?` ni function inayochukua index ya input na kurudisha sequence number ya muamala kwa input hiyo, kwa hiari ikirudisha nothing ikiwa index iko nje ya mipaka. Tena, thamani ya output si function safi ya index ya input, bali operesheni hutumia athari ya Reader kufikia mazingira ya muamala ili kubainisha thamani ya output. Kuna jets nyingine kadhaa za introspection zinazorejesha vipande mbalimbali vya data ya mazingira ya muamala.

### Kuainisha Athari

Si athari zote za upande zimeumbwa sawa. Athari nyingine za upande hutenda kwa ustaarabu zaidi kuliko nyingine. Tunaweza kuainisha athari kulingana na jinsi zinavyofaa kwa transformations za programu.

#### Athari za Commutative

Athari ya commutative ni ile ambapo, ikiwa unabadilisha outputs za expressions mbili, unaweza kubadilisha expressions zenyewe kwa usalama bila kubadilisha athari ya expression. Fikiria `swap = I H ▵ O H : A × B ⊢ B × A`. Ikiwa `f ▵ g ⨾ swap = g ▵ f` kwa kila expression `f` na `g` zenye athari za upande, basi athari hizo ni commutative.

Kusoma data ya muamala kutoka mazingira ni athari ya commutative kwa sababu matokeo ya kusoma kutoka mazingira ni yaleyale, bila kujali tunatekeleza usomaji kwa mpangilio gani.

Kwa jumla, kurusha exception si athari ya commutative. Ikiwa `f` inarusha exception fulani `e₁` na `g` inarusha exception nyingine `e₂`, basi ni exception gani inarushwa kutoka jozi ya `f` na `g` hutegemea mpangilio ambao zinatekelezwa.

Hata hivyo, katika hali maalum ya athari ya Failure, ambamo exception ya aina ya unit pekee ndiyo inaweza kurushwa, athari ni commutative. Bila kujali ni ipi kati ya `f` au `g` inarusha exception, exception inayotokana itakuwa ileile, kwa sababu kuna thamani moja tu ya exception inayowezekana.

#### Athari za Idempotent

Athari ya idempotent ni ile ambapo, ikiwa unaduplicate output ya expression, unaweza kuduplicate expression yenyewe kwa usalama bila kubadilisha athari ya expression. Fikiria `dup = iden ▵ iden : A ⊢ A × A`. Ikiwa `f ⨾ dup = dup ⨾ f ▵ f` kwa kila `f` yenye athari za upande, basi athari hizo ni idempotent.

Kusoma data ya muamala kutoka mazingira ni athari ya idempotent. Kurusha exception pia ni athari ya idempotent. Ingawa ni moja tu kati ya expressions mbili zilizoduplicate ndiyo itatekelezwa, exception yoyote inayorushwa na `dup ⨾ f ▵ f` itakuwa sawa na exception inayorushwa na `f ⨾ dup`.

Hata hivyo, kuandika kwenye logi kunaweza kusiwe idempotent, kwa kuwa kuduplicate athari kungesababisha ujumbe wa logi kuonekana mara mbili. Hata hivyo, ikiwa logi ina _set_ ya ujumbe badala ya _list_ ya ujumbe, basi athari itakuwa idempotent (na commutative) kwa sababu kuingiza kwenye set ni operesheni ya idempotent yenyewe.

#### Athari za Unitary

Athari ya unitary ni ile ambapo, ikiwa unatupa output ya expression, unaweza kutupa expression yenyewe kwa usalama bila kubadilisha athari za expression. Ikiwa daima ni kweli kwamba `f ⨾ unit = unit` kwa kila `f` yenye athari za upande, basi athari zako ni unitary.

Kusoma data kutoka mazingira ni mojawapo ya aina chache za athari za unitary. Ikiwa matokeo ya kusoma data ya muamala kutoka mazingira yanatupwa, expression nzima inayofanya usomaji inaweza kutupwa.

Athari ya failure si unitary. Ikiwa `f` inarusha exception basi `f ⨾ unit` pia itafanya hivyo; utekelezaji hata hautafika kwenye kombineta `unit` kabla ya ukokotoaji kukatizwa. Kwa upande mwingine, `unit` kwa wazi isingerusha exception yoyote, kwa hivyo athari za `f ⨾ unit` na `unit` zingekuwa tofauti.

Kwa muhtasari, hivi ndivyo athari zilizojadiliwa hapo juu zinavyokabiliana na sifa hizi tatu:

| Athari | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (mazingira ya muamala) | ✓ | ✓ | ✓ |
| Failure (exception ya aina ya unit) | ✓ | ✓ | ✗ |
| Writer (logi kama set) | ✓ | ✓ | ✗ |
| Exceptions za jumla (aina yoyote) | ✗ | ✓ | ✗ |

### Athari Zinazoruhusiwa katika Simplicity

Kadri sifa za aina ya athari zinavyokuwa na tabia nzuri zaidi, ndivyo optimizer ya Simplicity inavyopata nafasi zaidi ya kubadilisha programu zinazotumia athari hizo. Kwa ubora tungetaka kuruhusu tu athari zenye sifa zote tatu: commutative, idempotent, na unitary. Hii ingeruhusu optimizer kufanya aina yoyote ya transformation ya programu inayotaka. Hata hivyo, kusoma kutoka mazingira ndiyo athari pekee inayokidhi sifa zote tatu.

Badala yake tunadai kwamba athari za Simplicity ziwe commutative na idempotent. Athari zote mbili tunazotumia katika Simplicity, athari ya Failure na athari ya Reader, ni commutative na idempotent. Hii huruhusu darasa kubwa la optimizations kufanywa kwenye code ya Simplicity.

Hata hivyo, transformation ya "discard" iliyoelezwa hapo juu, inayojaribu kubadilisha `f ⨾ unit` kuwa `unit`, au transformation yoyote inayofanana hairuhusiwi ikiwa `f` inaweza kuzalisha athari ya Failure. Kwa kweli, fikiria ikiwa `f` ilikuwa na dai la `bip0340-verify`. Ingekuwa janga kujaribu ku-optimize ukaguzi huo uondolewe.

### Kwa Nini Kuruhusu Athari za Upande Kabisa?

Kwa nini Simplicity inaruhusu athari za upande kabisa? Je, haingekuwa bora ikiwa kila programu ingechukua muamala mzima kama input na kurudisha output ya Boolean inayoamua kama muamala ni halali au la?

#### Uthibitishaji wa Batch

Sababu moja tuliyo nayo athari ya Failure ni kusaidia [batch verification](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) ya saini za Schnorr. Katika batch verification, ukaguzi mwingi wa saini za Schnorr unawekwa pamoja kwa namna ambayo ikiwa ukaguzi wowote mmoja wa saini unashindwa, basi batch nzima inashindwa.

Utaratibu huu wa batching huboresha ufanisi ikilinganishwa na kuthibitisha kila saini moja moja. Hasara ni kwamba ikiwa batch verification inashindwa, basi hatujui ni ukaguzi gani mahususi wa saini au ukaguzi upi ulishindwa.

Kwa kutumia athari ya upande ya failure, `bip0340-verify` huhakikisha kwamba ikiwa ukaguzi wa saini unashindwa, muamala mzima unashindwa. Ikiwa `bip0340-verify` badala yake ingerudisha `𝟚`, aina ya Boolean, kwa success au failure, basi ukaguzi wa saini unaoshindwa bado ungeweza kupelekea tawi ambapo script inafaulu. Katika hali kama hiyo tungehitaji kujua kama saini mahususi ni halali au la, na hivyo tusingeweza kufaidika na batch verification.

#### Data ya Muamala Iliyokokotolewa Mapema

Tatizo katika Bitcoin Script ya awali lilikuwa kwamba function ya hashing iliyotumiwa kuunda message digests kwa saini ilikuwa ya mstari kulingana na ukubwa wa muamala. Kwa kawaida kila input huunda angalau message digest moja kwa uthibitishaji wa saini, kwa hivyo kwa ujumla kiasi cha hashing kilikuwa quadratic kulingana na ukubwa wa muamala.

Tatizo hili lilirekebishwa katika Segwit na iterations za baadaye za Bitcoin Script kwa kufafanua upya message digests ili ziweze kukokotolewa kwa muda constant kwa kila ukaguzi wa saini. Hii hutegemea kuwa na `PrecomputedTransactionData`, ambayo hukokotoa mapema hashes za data ya muamala mara moja na kisha kushirikiwa na ukokotoaji wa sighash wa kila input. Jets za transaction hashing za Simplicity hutegemea aina ileile ya data ya muamala iliyokokotolewa mapema ili kuhakikisha jets zinaendeshwa kwa muda constant.

Tuseme `sig-all-hash` haikutumia athari ya Reader. Tuseme kwa namna fulani tulifanikiwa kujenga aina ya Simplicity kwa mazingira ya muamala. Tuiite `TxEnv`, ili `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` iwe aina ya jet. Ufafanuzi kama huo ungehitaji jet ya `sig-all-hash` iweze kukokotoa hash ya muamala wowote, si tu muamala inayohusika nao. Programu za Simplicity zingeweza kunakili `TxEnv` iliyotolewa na kupitisha nakala iliyorekebishwa kwake kwa `sig-all-hash`. Katika hali kama hiyo `sig-all-hash` isingeweza kutegemea `PrecomputedTransactionData`, na tungerudi kwenye kuhitaji muda wa mstari katika data yoyote ya muamala iliyopitishwa kwenye toleo hili la `sig-all-hash`.

Kwa sababu `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` hutumia athari ya Reader kufikia data ya muamala, hupata ufikiaji _tu_ wa mazingira ya muamala yaliyowekwa. Kwa sababu hiyo, utekelezaji wa jet unaweza kutumia `PrecomputedTransactionData` kwa usalama na kufanya kazi kwa muda constant.

### Cross-Input Signature Aggregation

Ingawa si Liquid wala Bitcoin zinazounga mkono [cross-input signature aggregation](https://hrf.org/latest/cisa-research-paper/) kwa wakati huu, tungependa kuangalia kwamba Simplicity inaweza kuendana nayo wakati muda ukifika.

Ingawa maelezo hayajakamilishwa, tunawazia half-aggregation ikitekelezwa kwa kutumia athari ya Writer. Yaani, jet mpya yenye aina kama `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` ingechukua ufunguo wa umma, message digest, na `r`-component ya saini ya Schnorr (saini ya Schnorr inajumuisha `r`-component na `s`-component) na kuiandika kwenye logi ya muamala kabla ya kuendelea na utekelezaji. Kisha, mahali pengine katika muamala au pamoja na muamala, aggregate `s`-component kwa saini zote za Schnorr zilizo-half-aggregated ingetolewa. Muamala ungekuwa halali tu wakati aggregate `s`-component kama hiyo imetolewa kwa funguo zote, ujumbe, na `r`-components zilizorekodiwa kwenye logi.

Ili kukidhi mahitaji ya Simplicity, athari hii ya Writer inahitaji kuwa idempotent na commutative. Hili linaweza kuhakikishwa kwa kuitazama logi ya writer kama set ya tuples za key, message, `r`-component. Hili linafanya kazi kwa sababu operesheni za set ni idempotent na commutative. Kuitazama logi kama set ya values kungeendana na algoriti ya uthibitishaji wa half-aggregation.

### Hitimisho

Katika sura hii tuliangalia kuongeza athari za upande kwenye ukokotoaji ambao Simplicity inaweza kufanya. Tuliainisha aina mbalimbali za athari kulingana na jinsi zinavyotenda vizuri kwa heshima na aina mbalimbali za transformation ya programu. Tuliamua kuweka athari za Simplicity kwenye zile ambazo ni commutative na idempotent.

Athari mbili tunazotumia kwa matumizi ya Bitcoin na Liquid ni athari ya Reader, kwa kufikia mazingira ya muamala, na athari ya Failure, kwa kukatiza na kushindisha programu. Jets nyingine hutumia operesheni primitive ambapo aina hizi za athari za upande zinaweza kutokea.

Athari ya Failure huamua output ya programu ya Simplicity: programu ama inashindwa, na kufanya muamala kuwa batili, au programu inafaulu. Athari ya Reader hutoa aina moja ya input kwa programu ya Simplicity: mazingira yaliyo na data ya muamala. Lakini pia tunahitaji kutoa inputs nyingine, kama saini za kidijitali, kwa programu za Simplicity.

Katika sura inayofuata tutaangalia programu za Simplicity ni nini, jinsi zinavyogeuzwa kuwa anwani, na jinsi tunavyoongeza inputs nyingine, kama saini, kwenye programu za Simplicity.

## Programu na Anwani

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

Katika sura iliyopita tulieleza athari mbili za upande zinazotumiwa katika Simplicity: athari ya Failure, inayoamua kufaulu au kushindwa kwa programu, na athari ya Reader, inayotoa ufikiaji wa mazingira ya muamala. Sasa tunageukia swali la vitendo: programu ya Simplicity ni nini hasa, na inakuwaje anwani kwenye blockchain?

### Programu za Simplicity

Programu ya Simplicity hufafanuliwa kama expression ya Simplicity ya aina `𝟙 ⊢ 𝟙`. Saini hii ya aina inamaanisha programu haichukui input yenye maana (thamani ya unit tu) na haizalishi output yenye maana (thamani ya unit tu). Athari ya Reader hunasa input ya mazingira ya muamala, ilhali athari ya Failure huonyesha success au failure. Athari hizi hushughulikia I/O badala ya aina za Simplicity zenyewe.

### Commitment Merkle Root

Badala ya kuhifadhi programu kamili on-chain, Bitcoin hutumia commitments — mazoea yanayoanzia Pay-to-Script-Hash (P2SH). Simplicity hutumia Commitment Merkle Root (CMR).

Kila kombineta hupokea tag ya SHA-256 inayotokana na muundo: `Simplicity␟Commitment␟[identifier]`, ambapo `␟` inawakilisha ASCII code 31 (unit separator).

Kila tag ni hash ya SHA-256 ya pre-image string inayolingana iliyoorodheshwa hapa chini:

| Kombineta | Pre-image ya tag (ASCII string) |
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

Expression ya Simplicity kisha huhashwa kwa recursion kuwa CMR ya 256-bit kwa kukokotoa midstate ya SHA-256 yenye tag kwa kila kombineta pamoja na CMRs za hoja zake (andika `#ᶜ(e)` kwa CMR ya expression `e`, na `∥` kwa concatenation ya bytes):

| Kombineta | Kanuni ya CMR |
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

Kombineta za binary (`comp`, `pair`, `case`) huunganisha CMRs za watoto wote wawili; kombineta za unary (`take`, `drop`, `injl`, `injr`) huunganisha CMR ya mtoto wake mmoja baada ya padding ya bytes 32 za `0x00`; na majani nullary (`iden`, `unit`) huhash tag yake pekee. Conventions mbili hufanya hili kuwa rahisi kukokotoa: midstates za SHA-256 hutumiwa ili **kila expression ihitaji angalau call moja tu kwa function ya compression ya SHA-256** (tukidhani midstate hadi tags za constant imekokotolewa mapema), na wajenzi wenye hoja moja huweka prefix ya hoja yao kwa bytes 32 za padding ya `0x00`, jambo linaloruhusu precomputation ya ziada kidogo kwa implementations zinazoitaka.

Kwa kombineta `unit` — constructor ya nullary isiyo na sub-expressions za hoja — kanuni hii inakuwa mahsusi `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, ambapo `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (tag inaingizwa mara mbili). CMR inayotokana kwa programu trivial ya `unit` ni:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Kwa muhimu, CMR hai-commit kwa aina za expressions za Simplicity, ikitegemea badala yake type inference wakati wa redemption.

### Anwani

Anwani hutumia utaratibu wa Taproot wa BIP-0341 huku CMRs zikiwa committed chini ya TapLeaf version `0xbe`. Mchakato unahusisha:

1. Kukokotoa TapLeaf tagged hash inayochanganya version byte, urefu wa CMR, na CMR yenyewe
2. Kutweak internal public key (kwa kutumia NUMS point wakati hakuna key-spend path inayotakiwa)
3. Kugeuza kuwa umbizo la bech32m
4. Kuongeza checksums zinazofaa

Wakati hakuna key-spend path inayotakiwa, internal public key huwekwa kuwa **NUMS** ("Nothing-Up-My-Sleeve") point: curve point iliyochaguliwa kimakusudi ili hakuna anayejua discrete logarithm yake — kwa maneno mengine, point isiyo na private key inayolingana. Kwa sababu hakuna mtu anayeweza kamwe kuzalisha saini kwa ajili yake, key-spend path haiwezi kutumika kwa uthibitisho, na output inaweza kutumiwa *tu* kupitia committed Simplicity script path. Katika matumizi halisi, NUMS point hii inapaswa kufanywa random kama inavyopendekezwa na BIP-0341, ili outputs zisizo na key-spend path zisitofautishwe na outputs za kawaida za Taproot (faida ya faragha).

#### Kutoka Simplicity hadi Anwani

Tupitie derivation nzima kwa programu rahisi zaidi inayowezekana: `unit : 𝟙 ⊢ 𝟙`, no-op inayofaulu kila wakati.

**1. Tag ya kombineta.** Kwanza kokotoa tag ya `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Ingiza tag mara mbili ili kupata CMR ya programu:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf hash.** Weka prefix ya CMR kwa TapLeaf version ya Simplicity `0xbe` na urefu wa CMR `0x20` (bytes 32), kisha chukua Elements TapLeaf tagged hash (tagged hash ni `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Kwa leaf hii moja tu hakuna TapBranches, kwa hivyo hash hii tayari ni root ya TapTree.

**4. TapTweak.** Kwa kuwa hatutaki key-spend path, tunatumia BIP-0341 NUMS point kama internal key na kuitweak kwa root ya TapTree:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Ufunguo wa output.** Tweak internal key kwenye curve, `output_pk = lift_x(internal_pk) ⊕ t·G` (arithmetiki ya elliptic-curve imefupishwa hapa), ikitoa output key ya x-only `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Anwani ya Bech32m.** Simba output key ya x-only, weka prefix `p` (herufi ya SegWit v1 witness-version), ongeza prefix inayoweza kusomwa na binadamu ya Liquid-testnet `tex1`, na ambatisha checksum ya Bech32m. Anwani ya mwisho ni:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Hiyo ilikuwa kazi nyingi — lakini mengi yake yanaamriwa na Taproot yenyewe, si Simplicity.

### Expressions za Witness

Aina mpya ya kombineta hushughulikia ukosefu wa input kwa programu za Simplicity: expression ya witness. Kombineta `witness` huruhusu data ya saini na nyenzo nyingine za witness kuunganishwa kwenye programu.

```
      w : B
-----------------
witness w : A ⊢ B
```

Semantiki ya expression ya witness ni ya moja kwa moja: inapuuza input yake na kurudisha tu thamani `w` (ambayo inaweza kuwa ya aina yoyote ya Simplicity), yaani `⟦witness w⟧(a) = w`. Hii haiongezi **uwezo mpya wa kujieleza** — kwa nadharia ya ukamilifu, Simplicity tayari inaweza kujenga function yoyote ya constant kama hiyo (kumbuka macro ya `scribe` kutoka sura zilizopita). Hoja ya kombineta `witness` iko kabisa katika **CMR** yake: thamani `w` **huondolewa** kwenye CMR ya expression, kwa hivyo anwani inaweza kukokotolewa kabla ya `w` kujulikana, na `w` hutolewa wakati wa redemption.

Chaguo hili la usanifu linaunga mkono pruning — matawi ya masharti yasiyotekelezwa hayahitaji kufichuliwa on-chain, pamoja na expressions zake za witness zinazohusiana. Wakati tawi limepogolewa, verifier anahitaji tu CMR ya subtree iliyopogolewa, si maudhui yake halisi.

### Thamani za Witness

Inaweza kuonekana kama kikwazo kwamba expression ya witness inaweza kushikilia tu *thamani*, na si expression ya Simplicity ya jumla zaidi. Lakini programu za blockchains zinazotegemea UTXO hutekelezwa mara moja tu. Hakuna haja ya kupitisha sub-expression nzima kwenye node ya witness: mtumiaji anaweza kuendesha sub-expression hiyo mwenyewe, off-chain, na kunakili output yake kwenye thamani ya witness ili kupata matokeo yaleyale kabisa.

(Baadaye katika kozi hii tutakutana na kombineta `disconnect`, inayotenda sana kama expression ya witness ambayo *huchukua* expression nzima ya Simplicity kama hoja yake.)

Usanifu mbadala ungeingiza data yote ya witness kama hoja kwa programu ya kiwango cha juu ya Simplicity. Expressions za witness hupendelewa kwa sababu mbili. Kwanza, **pruning**: matawi yasiyotekelezwa ya expressions za `case` hayafichuliwi kamwe on-chain, na expressions zozote za witness ndani ya matawi hayo hupogolewa pamoja nazo. Pili, **locality**: expressions za witness huturuhusu kuweka kila thamani ya witness mahali hasa inapotumika, badala ya kuipitisha chini kutoka input ya kiwango cha juu ya programu.

### Type Inference

Kwa kuwa CMRs hazijumuishi types katika commitment, mfumo wa aina hujengwa upya wakati wa redemption. Algoriti ya type inference ya Simplicity huamua aina ndogo zaidi kwa kila subexpression kulingana na muundo wa kombineta. Kwa usahihi zaidi, inference hukokotoa aina *principal* (ya jumla zaidi) ya kila subexpression; variables zozote za aina zinazobaki free kisha huwekwa kuwa aina ya unit `𝟙`, jambo linalotoa aina ya kipekee na ndogo zaidi kwa programu.

### Hitimisho

Katika sura hii tulithibitisha kwamba programu za Simplicity ni expressions za aina `𝟙 ⊢ 𝟙`, tukaeleza jinsi Commitment Merkle Roots zinavyojengwa kutoka hashes za SHA-256 zenye tag za kila kombineta, na tukaonyesha jinsi CMRs zinavyogeuzwa kuwa anwani za on-chain kupitia BIP-0341 Taproot. Tulianzisha expressions za witness kama utaratibu wa kutoa data ya saini na inputs nyingine wakati wa kutumia bila kufanya commitment kwa thamani zake wakati wa kuunda anwani.

# Sehemu ya Mwisho

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Mapitio na Ukadiriaji

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Mtihani wa Mwisho

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Hitimisho

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
