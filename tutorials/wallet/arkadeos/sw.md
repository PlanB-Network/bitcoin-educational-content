---
name: ArkadeOS
description: Mwongozo kamili wa kwingineko ya Arkade na Ark Protocol
---

![cover](assets/cover.webp)



Mtandao wa Bitcoin unakabiliwa na changamoto kubwa: uboreshaji. Ingawa safu kuu (safu ya 1) inatoa usalama usio na kifani na ugatuaji, inaweza tu kushughulikia idadi ndogo ya miamala kwa sekunde. Lightning Network imeibuka kama suluhisho la kuahidi la safu ya pili (safu ya 2), inayowezesha malipo ya haraka na ya gharama nafuu. Hata hivyo, Umeme huweka vikwazo vyake yenyewe: usimamizi wa chaneli, hitaji la ukwasi unaoingia na utata wa kiufundi ambao unaweza kuzima watumiaji wapya.



Haya ni mandharinyuma ya **Ark**, itifaki mpya ya safu ya 2 iliyoundwa ili kutoa utumiaji uliorahisishwa bila kudhabihu ukuu. **ArkadeOS** (au Arkade) ni utekelezaji mkuu wa kwanza wa itifaki hii, inayotoa kwingineko ya Bitcoin ya kizazi kijacho.



Mafunzo haya yatakuongoza kupitia ulimwengu wa Arkade. Tutachunguza jinsi Ark Protocol inavyofanya kazi, jinsi ya kusakinisha na kusanidi Arkade wallet, na jinsi ya kuitumia kutuma na kupokea bitcoins papo hapo, kwa siri na bila misuguano ya kawaida ya Lightning Network.



## Kuelewa itifaki ya Sanduku



Kabla ya kupiga mbizi katika matumizi ya Arkade, ni muhimu kufahamu dhana muhimu za itifaki ya Safina inayoiendesha. Safina sio blockchain tofauti, lakini utaratibu wa uratibu wa akili juu ya Bitcoin.



### Dhana ya VTXO


Katika msingi wa ark protocol ni **VTXO** (Virtual UTXO). VTXO ni UTXO bado haijachapishwa kwenye blockchain ya Bitcoin: iko nje ya mnyororo mkuu (off-chain) lakini inaungwa mkono na shughuli zilizosainiwa hapo awali kwenye blockchain.



Tofauti na usawa kwenye ubadilishanaji wa kati, VTXO kweli ni yako. Una uthibitisho wa kriptografia unaokuruhusu, wakati wowote, kudai bitcoins halisi zinazolingana kwenye blockchain, hata seva ya Sanduku ikitoweka. VTXO hukuwezesha kuhamisha thamani mara moja kati ya watumiaji bila kusubiri uthibitisho wa kuzuia.



### Jukumu la ASP (Mtoa Huduma ya ark)


Box protocol hufanya kazi kwa mfano wa seva ya mteja. Seva inaitwa **ASP** (Mtoa Huduma ya Safina). ASP ina jukumu la conductor:




- Inatoa ukwasi muhimu kwa mtandao.
- Inaratibu shughuli kati ya watumiaji.
- Inapanga "raundi" za makazi kwenye blockchain.



Ni muhimu kutambua kuwa ASP ni **isiyo ya ulezi**. Haina funguo zako za kibinafsi, na haiwezi kuiba pesa zako. Jukumu lake ni la kiufundi na la vifaa. Ikiwa ASP itadhibiti miamala yako au itapungua, unaweza kurejesha pesa zako kupitia utaratibu wa kutoka upande mmoja.



### Mizunguko na faragha


Shughuli kwenye Jahazi hukamilishwa kwa makundi yanayoitwa **Mizunguko**. Mara kwa mara (k.m. kila baada ya sekunde chache), ASP hukusanya miamala yote ambayo haijashughulikiwa na kuziweka kwenye blockchain ya Bitcoin katika muamala mmoja ulioboreshwa.


Utaratibu huu hutoa faida mbili kuu:




- **Uwezo**: Muamala mmoja wa on-chain unaweza kuthibitisha maelfu ya malipo ya off-chain, na hivyo kupunguza gharama kwa watumiaji kwa kiasi kikubwa.
- **Usiri**: Kila raundi hufanya kama **CoinJoin**. Pesa kutoka kwa washiriki wote huchanganywa katika bwawa la pamoja kabla ya kusambazwa tena katika mfumo wa VTXO mpya. Hii huvunja kiungo kati ya mtumaji na mpokeaji, na kuifanya kuwa vigumu sana, au haiwezekani, kwa mwangalizi wa nje kufuatilia malipo.



## Uwasilishaji wa ArkadeOS



ArkadeOS ni programu madhubuti inayofanya Ark Protocol ipatikane kwa umma kwa ujumla. Imeundwa na Ark Labs, ni mfumo kamili wa ikolojia unaojumuisha jalada (Wallet), server (Opereta) na zana za wasanidi.



Kwa mtumiaji wa mwisho, Arkade huonekana kama wavuti maridadi na angavu wa aina ya wallet (PWA – Programu ya Wavuti Inayoendelea). Inaficha utata wa kriptografia unaohusiana na VTXO na kufanya kazi yote nyuma ya kiolesura kinachojulikana na rahisi kutumia. Ukiwa na Arkade, una anwani ya kupokea, kitufe cha kutuma, na historia ya miamala – kama wallet ya kawaida, lakini ukiwa na uwezo wa usiri na faragha unaotolewa na Ark.



## Ufungaji na usanidi



Kwa vile Arkade ni Programu ya Wavuti Inayoendelea, ni rahisi sana kusakinisha, na haihusishi maduka ya kawaida ya programu.



### Ufikiaji na usakinishaji


Unaweza kufikia Arkade moja kwa moja kutoka kwa kivinjari chochote cha kisasa cha wavuti (Chrome, Safari, Jasiri) kwenye kompyuta au rununu.





- Tembelea tovuti rasmi ya programu: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Utakaribishwa na mfululizo wa skrini za utangulizi zinazokuletea dhana muhimu za Arkade: mfumo mpya wa ikolojia wa Bitcoin, umuhimu wa kujitunza, na manufaa ya miamala ya kundi.



![arkade onboarding](assets/fr/02.webp)





- **Kwenye Android (Chrome/Jasiri)** : Bonyeza menyu ya kivinjari (vidoti tatu) na uchague "Sakinisha programu" au "Ongeza kwenye skrini ya kwanza".
- **Kwenye iOS (Safari)**: Bonyeza kitufe cha kushiriki (mraba chenye kishale cha juu) na uchague "Kwenye skrini ya kwanza".



Mara tu ikiwa imewekwa, Arkade inazindua kama programu asilia, skrini nzima na bila upau wa anwani.



### Uundaji wa kwingineko


Katika uzinduzi wa kwanza, utaulizwa kusanidi kwingineko yako.





- Bonyeza **"Unda Wallet Mpya"**.



![create wallet](assets/fr/03.webp)





- Wallet inaundwa mara moja, tofauti na wallets za kawaida za Bitcoin, **Arkade haitumii kishazi cha urejeshaji cha maneno 12- au 24**. Badala yake, Arkade hutengeneza kiotomatiki **ufunguo wa faragha** katika umbizo la Nostr (nsec), ambalo litatumika kuhifadhi nakala na kurejesha wallet yako. Kumbuka kuhifadhi ufunguo huu mara moja (tazama sehemu inayofuata).





- Utaona "wallet yako mpya inapatikana!" skrini, ikithibitisha kuwa wallet yako iko tayari kutumika. Bonyeza **"NENDA KWENYE MKOBA "** ili kufikia kiolesura kikuu.



Ukiwa kwenye wallet yako, unapelekwa kwenye kiolesura kikuu cha Arkade. Hapa utapata salio lako, vitufe vya kutuma na kupokea pesa, na kichupo cha "Programu" kinachotoa ufikiaji wa programu zilizojumuishwa kama vile Boltz (Lightning exchange), LendaSat na LendaSwap (huduma za ukopeshaji), na Fuji Money (mali ya sintetiki).



![wallet interface](assets/fr/04.webp)



### Uunganisho wa ASP


Kwa chaguo-msingi, kwingineko husanidiwa kiotomatiki ili kuunganishwa kwa ASP rasmi ya Arkade Labs. Unaweza kuangalia ni server gani umeunganishwa kwa kwenda kwa **Mipangilio** > **Kuhusu** ambapo utaona anwani ya seva (kwa sasa ni `https://arkade.computer`).



Katika toleo la sasa la Arkade (Beta), haiwezekani kurekebisha mwenyewe ASP server. Programu inaunganisha kiotomatiki kwa ASP rasmi ya Arkade Labs. Katika siku zijazo, watumiaji wanaweza kuchagua kati ya ASP tofauti kulingana na mapendeleo yao, lakini kipengele hiki bado hakijapatikana.



### Inahifadhi nakala ya ufunguo wako wa faragha


**Arkade hutumia ufunguo wa faragha katika umbizo la Nostr (nsec) kama njia mbadala na ya urejeshaji. Ili kuhifadhi ufunguo wako wa kibinafsi:





- Nenda kwa **Mipangilio** kutoka skrini kuu.
- Chagua **"Chelezo na faragha "**.
- Utaona **ufunguo wako wa faragha** ukionyeshwa katika umbizo la `nsec...`. Mfuatano huu mrefu wa wahusika ndio njia yako pekee ya kurejesha wallet yako.
- Bonyeza **"NAKILI NSEC KWENDA KILIPO "** ili kunakili ufunguo wako wa faragha.
- Weka ufunguo huu mahali salama: uandike kwenye karatasi, uihifadhi kwenye kidhibiti salama cha nenosiri, au tumia njia nyingine yoyote ya kuhifadhi nakala inayokufaa.
- Arkade pia inatoa **"Wezesha chelezo za Nostr "** chaguo. Kipengele hiki hutumia protocol ya Nostr (mtandao uliogatuliwa) ili kuhifadhi nakala kiotomatiki data fulani kutoka kwa wallet yako kwa njia iliyosimbwa kwa njia fiche hadi kwenye relay za Nostr. Hii hurahisisha ulandanishi kati ya vifaa vingi na inatoa urejeshaji rahisi wa hali ya wallet yako.



**Muhimu**: Hifadhi rudufu za Nostr ni kipengele cha **faraja** pekee. Hazibadilishi nakala rudufu ya ufunguo wako wa nsec. Relay za Nostr hazihakikishi uhifadhi wa kudumu wa data. Ufunguo wako wa faragha wa nsec unasalia kuwa njia yako pekee iliyohakikishwa ya kurejesha pesa zako.



![backup private key](assets/fr/05.webp)




## Kutumia Arkade



Mara tu unapoweka wallet yako, uko tayari kuchunguza uwezo wa Arkade. Kiolesura kimeundwa kuunganisha aina tofauti za malipo ya Bitcoin (On-chain, Lightning, Ark) bila mshono.



### Kupokea fedha



Ili kufadhili kwingineko yako, bonyeza **"Pokea"**. Arkade inatoa njia tatu za kupokea:





- **Malipo ya box**: Ikiwa mtumaji pia anatumia Arkade, shiriki address yako ya Ark kwa uhamisho wa papo hapo, wa siri na bila malipo.
- **Amana ya mtandaoni (Bweni)**: Tumia Bitcoin address (`bc1p...`) kupokea kutoka kwa wallet ya kawaida au exchange. Ruhusu uthibitisho (~dakika 10) kabla ya pesa kubadilishwa kuwa VTXO.
- **Lightning exchange**: Tengeneza ankara ya Lightning na ulipe kutoka kwa Lightning wallet ya nje. Pesa hufika papo hapo kupitia ubadilishaji kiotomatiki.



![receive amount](assets/fr/06.webp)



Skrini ya risiti huonyesha chaguo zote zinazopatikana: msimbo wa QR, Ark Address, Bitcoin address ya (BIP21) na Lightning Invoice. Kwa malipo ya Lightning, weka programu wazi wakati wa muamala.



![receive confirmation](assets/fr/07.webp)



### Kutuma fedha



Ili kutuma pesa, bonyeza **"Tuma"** na ubandike address ya mpokeaji au uchanganue msimbo wa QR. Arkade hutambua kiotomati aina ya malipo yanayohitajika:





- **Malipo ya Ark**: Kwa Box address, uhamishaji ni wa papo hapo, wa faragha na bila shaka bila malipo (ada 0 ya SATS). Mpokeaji hahitaji kuwa mtandaoni.
- **Malipo ya Lightning**: Changanua Lightning Invoice (`lnbc...`) na Arkade itabadilisha kiotomatiki. ASP hukulipia ankara na hutoza salio lako la Arkade.
- **Malipo ya mtandaoni**: Kuelekea address ya kawaida ya Bitcoin (`bc1q...` au `bc1p...`), Arkade itaanzisha "Pato la Shirikishi" ambalo litajumuishwa katika awamu inayofuata ya on-chain.



Angalia maelezo kwenye skrini ya "Weka saini ya muamala", kisha uthibitishe kwa **"GUSA ILI KUSAINI"**.



![send payment](assets/fr/08.webp)



**Block ya sasa (Beta)**: VTXO zilizoundwa chini ya saa 24 zilizopita haziwezi kutumika kwa matokeo ya on-chain. Ukikumbana na hitilafu, tafadhali subiri hadi VTXO zako "zimekomaa".



**Usiri wa matokeo ya on-chain**: Mfano ulio hapa chini unaonyesha [muamala wa pato la Ark kwenye mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b7b79b2). Tunaona ingizo lililosambazwa kwa matokeo 4 tofauti, kama CoinJoin. Kwa mtazamaji wa nje, haiwezekani kuamua ni kiasi gani ni cha mtumiaji gani.



![transaction ark mempool](assets/fr/11.webp)



## Vipengele vya hali ya juu



### Usimamizi wa kumalizika kwa VTXO


Kipengele cha kiufundi cha box protocol ni kwamba VTXO zina muda mfupi wa maisha. Kizuizi hiki cha wakati ni asili katika muundo wa protocol. Muda wa mwisho wa matumizi unaweza kusanidiwa na kila server ya ASP; kwenye Arkade Labs ASP rasmi, kipindi hiki ni karibu **wiki 4 (≈ siku 30)**.



**Kizuizi hiki huruhusu server ya Ark kudhibiti kwa ustadi ukwasi na kusafisha VTXO kutoka kwa watumiaji ambao hawatumii. Baada ya kumalizika muda wake,Box server inaweza kudai kitaalam pesa zilizobaki kwenye mti wa VTXO.



Ili kufanya VTXO zako ziendelee kutumika, zinahitaji "kuonyeshwa upya" kabla hazijaisha muda wake. Kuonyesha upya kunajumuisha kushiriki katika "raundi" mpya ambapo VTXO zako karibu na mwisho wa matumizi hubadilishwa kwa VTXO mpya na kipindi kipya cha uhalali kamili (≈ siku 30 kwenye Arkade Labs ASP).



Kwingineko ya Arkade inasimamia mchakato huu kiotomatiki: programu tumizi hufuatilia mara kwa mara hali ya VTXO zako na huzionyesha kiotomatiki siku chache kabla hazijaisha. Mradi tu utafungua programu yako mara kwa mara (angalau mara moja kwa wiki), VTXO zako zitawekwa kiotomatiki.



Usipofungua jalada lako kwa zaidi ya wiki 4, muda wa kutumia VTXO wako utaisha. Hata hivyo, hutapoteza pesa zako: unaendelea na chaguo la kuzirejesha kupitia **kutoka upande mmoja** (angalia sehemu inayofuata). Utaratibu huu ni wa gharama zaidi na polepole, lakini unahakikisha kuwa pesa zako zinaendelea kurejeshwa.



Haja ya kufungua programu mara kwa mara hufanya Arkade kuwa **"Hot Wallet"** iliyoundwa kwa matumizi ya kila siku, si salama kwa akiba ya muda mrefu. Ili kuhifadhi bitcoins bila kuzitumia kwa muda mrefu, pendelea vifaa vya baridi vya wallet.



**Angalia hali ya VTXO zako**: Unaweza kufuatilia hali ya VTXO zako katika **Mipangilio** > **Advanced**. Tazama "Usasishaji Ufuatao" ili kuona usasishaji unaofuata wa kiotomatiki utakapofanyika lini, na "Sarafu Halisi" ili kuona orodha ya kina ya VTXO zako zote pamoja na tarehe ya mwisho wa matumizi.



![vtxo management](assets/fr/09.webp)



### Sortie Unilaterale (Kutoka Moja kwa Moja)



Kuondoka kwa nchi moja moja ni **dhamana ya kimsingi ya kriptografia** ya protocol ya Ark ambayo inakuhakikishia kupata pesa zako, hata kama ASP itatoweka, hukagua miamala yako au kukataa kushirikiana. Kitaalam, VTXO zako ni **miamala ya Bitcoin iliyotiwa saini mapema** ambazo unamiliki. Katika hali ya dharura kabisa, unaweza kutangaza miamala hii kwenye Bitcoin blockchain ili kurejesha pesa zako bila idhini ya mtu yeyote.



**Inafanya kazi vipi?** Mchakato unafanyika katika hatua mbili. Kwanza, **Inafungua**: unatangaza kwa mtiririko shughuli zilizotiwa saini awali zinazounda VTXO zako kwenye mti wa muamala. Kisha **Ukamilishaji**: baada ya muda kufunga saa kuisha (kawaida saa 24), unakusanya bitcoin zako kutoka kwa protocol ya kawaida.



**Hali ya sasa katika Arkade**: Katika toleo la Beta, bado hakuna kitufe au kiolesura rahisi cha toleo la upande mmoja. Utendaji huu kwa sasa unahitaji matumizi ya Arkade SDK na maarifa ya kiufundi ya upangaji wa programu ya TypeScript.



**Hata kama utaratibu haupatikani kwa kugusa kitufe, uhakikisho wa kriptografia upo. VTXO zako zina miamala iliyosainiwa awali ambayo ni yako kihalali. Ni dhamana hii ya kiufundi inayoifanya Ark kuwa itifaki **isiyo ya ulezi**: hata katika hali mbaya zaidi, pesa zako zitasalia zinaweza kurejeshwa kiufundi. Kiolesura kilichorahisishwa pengine kitaongezwa katika matoleo yajayo ya Arkade.



## Faida na mapungufu



Ili kuiweka Arkade katika muktadha unaofaa, wacha tufanye muhtasari wa nguvu na udhaifu wake wa sasa.



### Vivutio




- **Uzoefu wa Mtumiaji (UX)**: Hakuna usimamizi wa kituo, uwezo unaoingia au chelezo changamano kama ilivyo kwa Umeme. Sakinisha tu na utumie.
- **Faragha** : Usanifu chaguomsingi wa CoinJoin unatoa kiwango cha juu zaidi cha kutokujulikana kuliko miamala ya kawaida ya on-chain au Umeme.
- **Mwingiliano**: Lipa msimbo wowote wa Bitcoin QR (On-chain au Lightning) kutoka kwa kiolesura kimoja.



### Vikwazo




- **nascent protocol**: Safina ni teknolojia ya hivi karibuni sana. Hitilafu zinaweza kuwepo. Inashauriwa kutotumia Ark kuhifadhi pesa ambazo hasara yake itakuwa muhimu.
- **Utegemezi wa ASP**: Ingawa sio chini ya ulinzi, mfumo unategemea upatikanaji wa ASP kwa usaidizi. Ikiwa ASP iko nje ya mtandao, huwezi tena kufanya shughuli papo hapo (pekee pesa zako za on-chain).
- **Hot Wallet pekee** : Haja ya kufungua programu mara kwa mara ili kuonyesha upya VTXO haifai kwa hifadhi baridi (Cold Storage).



## Ulinganisho: Arkade vs Umeme dhidi ya Cashu



Ili kuelewa vyema nafasi ya Arkade, wacha tuilinganishe na suluhisho mengine mawili makubwa ya hatari.




| Kigezo | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Mfumo** | UTXO inayoshirikiwa ikiratibiwa na seva (ASP) | Mtandao wa P2P wa njia za malipo | Tokeni ambazo hazionekani zilizotolewa na benki (Mint) |
| **Usimamizi wa Fedha** | **Si wa usimamizi** (una funguo) | **Si wa usimamizi** (una funguo) | **Wa usimamizi** (Mint ina fedha) |
| **Faragha** | **Ya Juu** (CoinJoin ya asili, haionekani kwa umma) | **Ya Kati** (Uelekezaji wa vitunguu, lakini njia zinaonekana) | **Ya Juu Sana** (Haionekani hata kwa Mint) |
| **Uwezo wa kupanuka** | Bora (Ukusanyaji mkubwa on-chain) | Bora (Miamala isiyo na kikomo off-chain) | Bora (Sahihi rahisi za seva) |
| **Uzoefu** | Rahisi (karibu na pochi ya on-chain) | Tata (usimamizi wa njia, ukwasi) | Rahisi sana (kama pesa taslimu ya kidijitali) |
| **Hatari kuu** | Upatikanaji wa ASP na Muda kuisha | Usimamizi wa njia na Nakala rudufu | Imani kwa Mint (hatari ya wizi) |

**Arkade** ndio maelewano bora: usahili na usiri wa Cashu, lakini kwa uhuru (isiyo ya ulinzi) wa Umeme.



## Usaidizi na Usaidizi



Ikiwa utapata shida yoyote au una maswali yoyote unapotumia Arkade, programu hutoa chaguzi kadhaa za usaidizi:





- Nenda kwa **Mipangilio** > **Usaidizi**.
- Utapata chaguzi kadhaa:
  - **Usaidizi kwa wateja**: Pata usaidizi kuhusu kwingineko yako, ripoti hitilafu au uulize maswali.
  - **Soga Salama**: Mazungumzo yako ni salama na ya faragha, na historia hudumishwa kati ya vipindi.
  - **Ripoti za Mdudu**: Ripoti matatizo yoyote unayokumbana nayo, ikiwa ni pamoja na hatua za kuyazalisha tena.
  - **Fuatilia Maendeleo**: Fuatilia tikiti zako za usaidizi na mazungumzo kila wakati.



![support](assets/fr/10.webp)



Timu ya Arkade pia inatumika kwenye Telegram kupitia kituo cha @arkade_os kwa usaidizi na fursa za ujumuishaji.



## Kumbuka muhimu: Maombi katika Beta



**⚠️ Arkade kwa sasa yuko katika toleo la Beta la Umma kwenye mainnet Bitcoin**. Ingawa programu inafanya kazi na bitcoins halisi, ni muhimu kuchukua tahadhari fulani.



### Mapendekezo ya matumizi




- **Tumia kiasi kidogo**: Epuka kuhifadhi pesa nyingi kwenye Arkade. Tumia wallet hii kwa gharama zako za kila siku na uweke akiba yako kwenye maunzi baridi ya wallet.
- **Hitilafu na vikwazo vinavyowezekana**: Kama ilivyo kwa programu yoyote chini ya usanidi amilifu, Arkade inaweza kuwasilisha hitilafu au tabia isiyotarajiwa. Ripoti matatizo yoyote kupitia usaidizi uliojumuishwa.
- **Mageuzi ya haraka** : Programu na itifaki zinaboreshwa kila mara. Baadhi ya vipengele vinaweza kubadilika au kuongezwa katika matoleo yajayo.



### Vikwazo vya sasa vinavyojulikana




- **Kuchelewa kwa saa 24 kwenye VTXO** : VTXO zilizoundwa hivi karibuni haziwezi kutumika mara moja kwa matokeo ya on-chain.
- **ASP ya kipekee**: Bado haiwezekani kubadilisha server ya ASP katika programu.
- **Pato la kiufundi la upande mmoja**: Bado hakuna kiolesura kilichorahisishwa kwa pato la upande mmoja (inahitaji SDK).



Timu ya Arkade Labs inafanya kazi kwa bidii ili kulegeza vikwazo hivi katika matoleo yajayo.



## Hitimisho



ArkadeOS inawakilisha mafanikio makubwa katika mfumo ikolojia wa Bitcoin. Kwa kutekeleza box protocol, inathibitisha kwamba inawezekana kupatanisha usahili wa matumizi na kanuni za kimsingi za Bitcoin: usiamini, thibitisha.



Ingawa bado ni changa, Arkade inatoa muhtasari wa kuvutia wa jinsi malipo ya baadaye ya Bitcoin yanaweza kuwa: papo hapo, ya faragha na kufikiwa na wote bila mahitaji ya kiufundi. Ni zana bora kwa matumizi yako ya kila siku, inayosaidia suluhisho lako salama la kuweka akiba (Cold Wallet).



Tunakuhimiza ujaribu Arkade kwa kiasi kidogo ili kugundua itifaki hii mpya kwa ajili yako mwenyewe. Mfumo wa ikolojia unabadilika haraka, na Arkade iko mstari wa mbele katika uvumbuzi huu.



## Rasilimali



Ili kujua zaidi, wasiliana na rasilimali rasmi:





- **Tovuti ya Arkade**: [arkadeos.com](https://arkadeos.com)
- **Hati**: [docs.arkadeos.com](https://docs.arkadeos.com)
- **Ark** itifaki: [ark-protocol.org](https://ark-protocol.org)
- **Msimbo wa Chanzo** : [GitHub Arkade](https://github.com/arkade-os)
