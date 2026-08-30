---
name: Sparrow Wallet - Multisig
description: Unda pochi yenye saini nyingi kwenye Sparrow
---
![jalada](assets/cover.webp)


Pochi yenye saini nyingi (mara nyingi huitwa "*Multisig*") ni muundo wa pochi ya Bitcoin unaohitaji saini kadhaa za kriptografia, kutoka funguo tofauti, ili kuidhinisha matumizi. Tofauti na pochi ya kawaida ("*singlesig*"), ambapo ufunguo mmoja wa faragha unatosha kufungua UTXO, Multisig inategemea muundo wa **m-of-n**: kati ya funguo _n_ zinazohusishwa na pochi, _m_ lazima zitie saini pamoja kila muamala.


Utaratibu huu huwezesha udhibiti wa pochi kugawiwa kati ya vyombo au vifaa kadhaa. Kwa mfano, katika usanidi wa 2 kati ya 3, seti tatu huru za funguo huzalishwa, lakini mbili tu zinahitajika ili kutoa fedha. Muundo huu hupunguza kwa kiasi kikubwa hatari zinazohusiana na kufichuliwa au kupotea kwa ufunguo: mwizi mwenye ufikiaji wa ufunguo mmoja tu hawezi kufilisi pochi, na mtumiaji anayepoteza mmoja bado anaweza kufikia fedha zake kwa kutumia mbili zilizobaki.


![Picha](assets/fr/01.webp)


Hata hivyo, usalama huu mkubwa huja na uchangamano mkubwa zaidi. Kuweka pochi ya Multisig kunahitaji kulinda vifungu kadhaa vya mnemonic (kimoja kwa kila kipengele cha saini) na funguo za umma zilizopanuliwa ("*xpub*"). Kwa kweli, ikiwa unatumia pochi ya Multisig 2 kati ya 3, ili kurejesha pochi lazima uwe na vifungu vyote vitatu vya mnemonic, au angalau vifungu viwili kati ya vitatu. Lakini ikiwa una vifungu viwili tu kati ya vitatu, pia unahitaji ufikiaji wa *xpubs* zote tatu, bila ambazo haitawezekana kurejesha funguo za umma zinazohitajika ili kufikia bitcoins ambazo zinalinda.


Kwa muhtasari, ili kurejesha pochi ya Multisig, lazima uwe na:


- Au ufikiaji wa vifungu vyote vya mnemonic vinavyohusishwa na kila kipengele cha saini;
- Au uwe na idadi ya chini ya vifungu vya mnemonic inayohitajika na kizingiti ili uweze kutia saini, na pia uwe na ufikiaji wa xpubs za vipengele vyote ili kurejesha funguo muhimu za umma.


![Picha](assets/fr/02.webp)


Usimamizi huu wa nakala za akiba za pochi ya Multisig hurahisishwa na *Output Script Descriptors*, ambazo hukusanya data yote ya umma inayohitajika kufikia fedha. Hata hivyo, utendakazi huu bado haujatekelezwa katika programu zote za usimamizi wa pochi.


Multisig inafaa hasa kwa bitcoiners wanaotafuta usalama ulioimarishwa au usimamizi wa pamoja wa fedha: kampuni, vyama, familia, au watumiaji binafsi wanaoshikilia kiasi kikubwa cha bitcoins. Inaweza kutumiwa kuunda mifumo ya utawala uliogatuliwa, kwa mfano, kugawa mamlaka ya kutia saini kati ya wasimamizi au wanachama kadhaa wa timu.


Katika mafunzo haya, tutajifunza jinsi ya kuunda na kutumia pochi ya kawaida yenye saini nyingi kwa kutumia **Sparrow Wallet**. Ikiwa ungependa kuunda pochi maalum yenye saini nyingi na timelocks, ninapendekeza utumie Liana badala yake:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Mahitaji ya awali


Kwa mafunzo haya, nitakuonyesha jinsi ya kutengeneza Multisig kwa kutumia [programu ya usimamizi wa pochi ya Sparrow Wallet](https://sparrowwallet.com/download/). Ikiwa bado hujasakinisha programu hii, tafadhali fanya hivyo sasa. Ikiwa unahitaji msaada, pia tuna mafunzo ya kina kuhusu kusanidi Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Ili kuweka pochi yenye saini nyingi, utahitaji mikoba tofauti ya maunzi. Kwa Multisig 2 kati ya 3, kwa mfano, unaweza kutumia:


- Trezor Model One;
- Ledger Flex;
- Passport Core.


![Picha](assets/fr/03.webp)


Ni wazo zuri kutumia chapa tofauti za Hardware Wallet katika usanidi wako wa Multisig. Hii huhakikisha kwamba ikiwa modeli fulani inakumbwa na tatizo kubwa, haitaathiri usalama wa jumla wa Multisig yako. Zaidi ya hayo, hukuruhusu kunufaika na faida maalum za kila kifaa. Kwa mfano, katika usanidi wangu:



- Trezor Model One ni open-source kabisa, jambo linalowezesha kuthibitisha uzalishaji wa seed. Hata hivyo, kwa kuwa haina Secure Element, bado iko hatarini kwa mashambulizi ya kimwili;



- Ledger Flex, kwa upande mwingine, inanufaika na firmware miliki isiyoweza kuthibitishwa, lakini inajumuisha Secure Element inayotoa ulinzi bora wa kimwili;



- Passport Core inaunganisha firmware iliyo open-source kikamilifu, Secure Element, na mabadilishano ya misimbo ya QR yaliyo air-gapped. Ni mtiaji saini huru wa tatu anayeweza kuthibitisha anwani na kutia saini PSBTs bila muunganisho wa data wa USB.


Kabla ya kusanidi pochi yako ya Multisig, hakikisha kwamba kila Hardware Wallet imesanidiwa ipasavyo (uzalishaji na uhifadhi wa mnemonic, ufafanuzi wa PIN). Kwa maagizo ya kina, unaweza kushauriana na mafunzo yetu kwa kila Hardware Wallet, kwa mfano:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Kama tutakavyoona baadaye katika mafunzo haya, inawezekana pia kujumuisha katika usanidi wako wa Multisig kipengele ambacho hakihusiani na Hardware Wallet, lakini funguo zake za faragha zimehifadhiwa kwenye PC yako. Njia hii ni dhahiri si salama kama kutumia hardware wallets pekee, lakini inaweza kuwa muhimu katika hali fulani. Kwa mfano, kwa Multisig 2 kati ya 3, unaweza kuchagua hardware wallets mbili na Software Wallet moja.

> ⚠️ **Taarifa ya usalama ya Coldcard MK3:** usiunde seed mpya kwenye MK3 inayotumia firmware ya kabla ya 4.2.0. Seeds zilizozalishwa kwenye firmware ya awali lazima zibadilishwe na fedha zihamishwe. Kwa hivyo mafunzo haya hutumia Passport Core kama mtiaji saini wa marejeo aliye air-gapped.


## Kuunda pochi ya Multisig


Fungua Sparrow Wallet, bofya kichupo cha "*File*", kisha chagua "*New Wallet*".


![Picha](assets/fr/04.webp)


Ipe pochi yako yenye saini nyingi jina, kisha bofya "*Create Wallet*" ili kuthibitisha.


![Picha](assets/fr/05.webp)


Katika menyu kunjuzi ya "*Policy Type*", chagua chaguo la "*Multi Signature*".


![Picha](assets/fr/06.webp)


Katika kona ya juu kulia, sasa unaweza kufafanua jumla ya idadi ya funguo katika Multisig yako, pamoja na idadi ya watiaji saini pamoja wanaohitajika kuidhinisha matumizi. Katika mfano wangu, huu ni mpango wa 2 kati ya 3.


![Picha](assets/fr/07.webp)


Chini ya dirisha, Sparrow Wallet inaonyesha "*Keystore*" tatu. Kila moja inawakilisha seti ya funguo. Hapa, ninatumia hardware wallets tatu, kwa hivyo kila "*Keystore*" inalingana na mojawapo. Sasa tutazisanidi.


Ninaanza na Passport Core. Katika kichupo cha "*Keystore 1*", ninachagua chaguo la "*Airgapped Hardware Wallet*".


![Picha](assets/fr/08.webp)


Kwenye Passport, fungua akaunti unayotaka kutumia, kisha chagua "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport inaonyesha msimbo wa QR unaohuishwa ulio na taarifa za ufunguo wake wa umma.

Katika Sparrow, chagua "*Scan...*" karibu na "*Passport*" na uchanganue msimbo huo wa QR unaohuishwa kwa webcam ya kompyuta yako. Linganisha alama ya kidole ya ufunguo mkuu inayoonyeshwa na Sparrow na ile inayoonyeshwa na Passport, kisha leta keystore.

xpub ya Passport yako sasa imeletwa. Rudia utaratibu unaofaa kwa Ledger Flex na Trezor Model One.


Kwa Ledger Flex, ninachagua "*Keystore 2*", kisha ninabofya "*Connected Hardware Wallet*". Hakikisha Ledger imeunganishwa kwenye kompyuta, imefunguliwa, na kwamba programu ya Bitcoin imefunguliwa.


![Picha](assets/fr/15.webp)


Kisha bofya kitufe cha "*Scan...*".


![Picha](assets/fr/16.webp)


Karibu na jina la hardware wallet yako, bofya "*Import Keystore*".


![Picha](assets/fr/17.webp)


Mtiaji saini wa pili sasa amesajiliwa ipasavyo katika Sparrow Wallet.


![Picha](assets/fr/18.webp)


Ninarudia utaratibu huo huo na Trezor One ili kukamilisha usanidi wa Multisig.


![Picha](assets/fr/19.webp)


Katika usanidi wangu hatuhusishi hali hii, lakini ikiwa unataka kujumuisha saini kupitia software wallet katika Sparrow (hot wallet) ndani ya Multisig yako, bofya tu kitufe cha "*New or Imported Software Wallet*".


Sasa kwa kuwa vifaa vyako vyote vya saini vimeletwa katika Sparrow Wallet, unaweza kukamilisha uundaji wa Multisig kwa kubofya "*Apply*".


![Picha](assets/fr/20.webp)


Chagua nenosiri dhabiti ili kulinda ufikiaji wa pochi yako ya Sparrow Wallet. Nenosiri hili hulinda funguo zako za umma, anwani, lebo na historia ya miamala dhidi ya ufikiaji usioidhinishwa.


Kumbuka kuhifadhi nenosiri hili mahali salama, kama vile kidhibiti cha nenosiri, ili kuepuka kulipoteza.


![Picha](assets/fr/21.webp)


## Kuhifadhi nakala ya akiba ya pochi ya Multisig


Sasa tutahifadhi *Output Script Descriptor* kwenye kifaa huru na kuweka nakala kadhaa zake.


*Descriptor* ina xpubs zote katika pochi yako ya Multisig, pamoja na njia za derivation zinazotumiwa kuzalisha funguo. Kumbuka tulichoona katika Sehemu ya 1: ili kurejesha pochi ya Multisig, lazima uwe na vifungu vya mnemonic **vyote**, au idadi ya chini tu inayohitajika kufikia kizingiti cha saini. Hata hivyo, katika hali hii ya pili, ni muhimu pia kuwa na **xpubs** za watiaji saini wanaokosekana. *Descriptor* ina xpubs zote za Multisig yako.


Ikiwa hili haliko wazi, kumbuka tu hili: ili kurejesha Multisig, unahitaji idadi ya chini ya vifungu vya mnemonic kwa kila Hardware Wallet iliyotumiwa, kulingana na kizingiti (kwa upande wangu: vifungu 2), pamoja na *Descriptor*.


*Descriptor* hii haina funguo za faragha, ina za umma tu. Hii inamaanisha kwamba haitoi ufikiaji wa fedha. Kwa hivyo si muhimu sana kama vifungu vya mnemonic, ambavyo hutoa ufikiaji kamili wa bitcoins zako. Hatari ya *Descriptor* inahusiana tu na usiri: ikiwa itafichuliwa, mtu wa tatu anaweza kuona miamala yako yote, lakini hawezi kutumia fedha zako.


Ninakushauri sana uunde nakala kadhaa za *Descriptor* hii, na uziweke pamoja na kila kifaa cha kutia saini kwenye Multisig yako. Kwa mfano, katika hali yangu, ninachapisha *Descriptor* kwenye karatasi na kuweka nakala moja pamoja na Passport, nyingine pamoja na Trezor, na moja pamoja na Ledger. Pia ninahifadhi *Descriptor* hii kama faili ya PDF kwenye vijiti vitatu vya USB, kila kimoja kikihifadhiwa pamoja na mojawapo ya hardware wallets. Kwa njia hii, ninaongeza uwezekano wangu wa kutowahi kupoteza *Descriptor* hii, na nina uhakika wa kuwa na nakala mbili (moja ya kimwili na moja ya kidijitali) pamoja na kila kifaa.


Mara tu pochi yako ya Multisig imeundwa, Sparrow hukupa *Descriptor* hii kiotomatiki. Bofya kitufe cha "*Save PDF...*" ili kuihifadhi kama maandishi na kama msimbo wa QR.


![Picha](assets/fr/22.webp)


Kisha unaweza kuchapisha PDF hii na kuinakili kwenye vijiti vyako vya USB.


![Picha](assets/fr/23.webp)


Passport hutumia usanidi wa multisig ulioletwa na Sparrow ili kuonyesha na kuthibitisha taarifa muhimu za ufunguo wakati wa mtiririko wa kuoanisha QR na kutia saini. Weka *Descriptor* kwa kujitegemea: bado ni muhimu kurejesha pochi ikiwa mtiaji saini mmoja hapatikani.


Pamoja na kuhifadhi *Descriptor*, usisahau kuzingatia hasa kuhifadhi vifungu vya mnemonic kwa kila kifaa chako cha saini. Ikiwa ndio unaanza, ninapendekeza sana ushauriane na mafunzo haya mengine ili kujifunza jinsi ya kuvihifadhi na kuvisimamia ipasavyo:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Kabla ya kupokea bitcoins zako za kwanza kwenye Multisig yako, **ninakushauri sana ufanye jaribio tupu la urejeshaji**. Andika taarifa fulani za marejeo, kama vile anwani ya kwanza ya kupokea, kisha weka upya hardware wallets zako wakati pochi bado ni tupu. Kisha, jaribu kurejesha pochi yako ya Multisig kwenye Hardware Wallets kwa kutumia nakala zako za karatasi za vifungu vya mnemonic, kisha kwenye Sparrow kwa kutumia *Descriptor*. Hakikisha anwani ya kwanza inayozalishwa baada ya urejeshaji inalingana na ile uliyoandika awali. Ikiwa inalingana, unaweza kuwa na uhakika kwamba nakala zako za karatasi zinaaminika.


Ili kujifunza zaidi kuhusu jinsi ya kufanya jaribio la urejeshaji, ninapendekeza ushauriane na mafunzo haya mengine:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kupokea bitcoins kwenye Multisig yako


Pochi yako sasa iko tayari kupokea bitcoins. Katika Sparrow, bofya kichupo cha "*Receive*".


![Picha](assets/fr/30.webp)


Kabla ya kutumia anwani iliyozalishwa na Sparrow Wallet, chukua muda kuiangalia moja kwa moja kwenye skrini ya hardware wallets zako. Hii itahakikisha kwamba anwani haijabadilishwa, na kwamba vifaa vyako vinashikilia funguo za faragha zinazohitajika kutumia fedha zinazohusiana nayo. Hii hukusaidia kujilinda dhidi ya aina kadhaa za mashambulizi.


Ili kufanya hivyo, bofya "*Display Address*" ili kuonyesha anwani kwenye Trezor au Ledger yako, inapounganishwa kwa kebo.


![Picha](assets/fr/31.webp)


Ukiwa na Passport, chagua akaunti ya multisig na uchague "*Verify Address*". Changanua msimbo wa QR wa anwani ya kupokea inayoonyeshwa na Sparrow. Passport huthibitisha kwenye skrini yake kama anwani hiyo ni ya pochi ya multisig.


Hakikisha anwani inayoonyeshwa kwenye kila hardware wallet inalingana kabisa na ile iliyo katika Sparrow Wallet. Inashauriwa kufanya hili kabla tu ya kushiriki anwani na mlipaji, ili uwe na uhakika wa uadilifu wake.


Kisha unaweza kuipa anwani hii "*Label*", ili kuonyesha asili ya bitcoins zilizopokelewa. Hii ni njia nzuri ya kupanga usimamizi wa UTXOs zako.


![Picha](assets/fr/34.webp)


Mara hii imethibitishwa, unaweza kutumia anwani kupokea bitcoins.


![Picha](assets/fr/35.webp)


## Kutuma bitcoins kwa kutumia Multisig yako


Sasa kwa kuwa umepokea Satss zako za kwanza kwenye pochi yako ya Multisig, unaweza pia kuzitumia! Katika Sparrow, nenda kwenye kichupo cha "*Send*" ili kuunda muamala mpya.


![Picha](assets/fr/36.webp)


Ikiwa unataka kutumia *Coin Control*, yaani kuchagua mwenyewe UTXOs unazotaka kutumia, nenda kwenye kichupo cha "*UTXOs*". Chagua UTXOs unazotaka kutumia, kisha bofya "*Send Selected*". Utaelekezwa kiotomatiki kwenye kichupo cha "*Send*", huku UTXOs zikiwa tayari zimejazwa.


![Picha](assets/fr/37.webp)


Ingiza anwani ya marudio. Anwani nyingi zinaweza kuongezwa kwa kubofya "*+ Add*".


![Picha](assets/fr/38.webp)


Ongeza "*Label*" ili kuelezea kusudi la matumizi haya, ili iwe rahisi kufuatilia miamala yako.


![Picha](assets/fr/39.webp)


Ingiza kiasi kitakachotumwa kwa anwani iliyochaguliwa.


![Picha](assets/fr/40.webp)


Rekebisha kiwango cha ada kulingana na hali za sasa za mtandao. Kwa mfano, tazama [Mempool.space](https://Mempool.space/) ili kuchagua kiwango cha ada kinachofaa.


Baada ya kuangalia vigezo vyote vya muamala, bofya "*Create Transaction*".


![Picha](assets/fr/41.webp)


Ikiwa umeridhika na kila kitu, bofya "*Finalize Transaction for Signing*".


![Picha](assets/fr/42.webp)


Chini ya skrini, utaona kwamba Sparrow inasubiri saini 2. Hii ni kawaida: pochi inayotumiwa hapa ni Multisig 2 kati ya 3.


![Picha](assets/fr/43.webp)


Ninaanza kutia saini kwa Passport yangu. Katika Sparrow, bofya "*Show QR*" ili kuonyesha PSBT (*Partially Signed Bitcoin Transaction*) kama misimbo ya QR iliyohuishwa. Kwenye Passport, chagua akaunti ya multisig na uchague "*Sign with QR Code*", kisha uchanganue msimbo wa QR unaoonyeshwa na Sparrow.


Kwenye skrini ya Hardware Wallet yako, angalia kwa makini vigezo vya muamala: anwani ya mpokeaji, kiasi kilichotumwa, na ada. Mara muamala umethibitishwa, thibitisha ili kuendelea na saini.


Baada ya kuidhinisha muamala, Passport inaonyesha PSBT iliyotiwa saini kama misimbo ya QR iliyohuishwa. Katika Sparrow, bofya "*Scan QR*" na uchanganue misimbo hiyo kwa webcam yako. Saini ya Passport kisha inaongezwa. Sasa ninatumia Ledger kwa saini ya pili inayohitajika: ninaiunganisha na kuifungua, kisha ninabofya "*Sign*" katika Sparrow.


![Picha](assets/fr/48.webp)


Bofya "*Sign*" karibu na jina la Hardware Wallet yako.


![Picha](assets/fr/49.webp)


Mara ya kwanza unapotumia Ledger yako na Multisig hii, Sparrow itakuomba uthibitishe funguo za umma zilizopanuliwa (xpubs) za watiaji saini pamoja. Kama ilivyo kwa Passport, hatua hii hukuzuia kutia saini kwa upofu baadaye. Ili kuthibitisha taarifa hizi, linganisha xpub inayoonyeshwa kwenye skrini ya Ledger na zile zinazotolewa moja kwa moja na hardware wallets zako nyingine.


![Picha](assets/fr/50.webp)


Angalia anwani ya mpokeaji, kiasi kilichohamishwa na ada ya muamala, kisha tia saini muamala.


![Picha](assets/fr/51.webp)


Bonyeza skrini ili kutia saini.


![Picha](assets/fr/52.webp)


Sparrow sasa ina saini mbili zinazohitajika kutoa fedha kutoka kwenye pochi ya Multisig. Angalia muamala mara ya mwisho, na ikiwa kila kitu kiko sawa, bofya "*Broadcast Transaction*" ili kuutangaza kwenye mtandao.


![Picha](assets/fr/53.webp)


Utapata muamala huu katika kichupo cha "*Transactions*" cha Sparrow Wallet.


![Picha](assets/fr/54.webp)


Hongera, sasa unajua jinsi ya kusanidi na kutumia pochi yenye saini nyingi kwenye Sparrow. Ikiwa umepata mafunzo haya kuwa na manufaa, ningeshukuru ukiacha kidole gumba cha kijani hapa chini. Tafadhali jisikie huru kushiriki makala hii kwenye mitandao yako ya kijamii. Asante kwa kushiriki!


Ili kwenda mbali zaidi, ninapendekeza ushauriane na mafunzo haya kuhusu njia nyingine ya kuongeza usalama wa pochi yako ya Bitcoin, passphrase ya BIP39:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
