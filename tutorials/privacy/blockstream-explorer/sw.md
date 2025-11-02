---
name: BLOCKSTREAM Explorer
description: Gundua Layer kuu ya Bitcoin na Liquid Network
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer ni mradi unaowezesha uchunguzi wa miamala na Global State ya itifaki ya Bitcoin, pamoja na [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid iliyotengenezwa na kampuni ya BLOCKSTREAM.



Ilianzishwa mwaka wa 2014 na BLOCKSTREAM, kampuni iliyoanzishwa na Adam Back, [BLOCKSTREAM.info](https://BLOCKSTREAM.info) mgunduzi inalenga kutoa miundombinu thabiti ya Bitcoin, kuhakikisha utengamano na ufuatiliaji wa miamala kati ya tabaka (On-Chain na Liquid), huku ikiimarisha usalama wa mtumiaji na faragha.



Katika somo hili, tunawasilisha kinachoifanya kuwa tofauti, huduma zake, na jinsi inavyotoa ufuatiliaji usio na mshono wa uendeshaji na hali ya tabaka za Bitcoin za On-Chain na Liquid.



## Kuanza na BLOCKSTREAM



### Nenda kwenye kituo kikuu



Unapoenda kwa kichunguzi cha BLOCKSTREAM.info, kwenye "**Dashibodi**", kituo kikuu cha itifaki cha Bitcoin kinachaguliwa kwa chaguo-msingi. Kutoka kwa Interface hii, una muhtasari wa:





- Saizi kuu ya mnyororo: Vitalu vilivyochimbwa hivi majuzi.



![blocks](assets/fr/01.webp)



Sehemu hii inatoa taarifa kuhusu vitalu vilivyochimbwa hivi karibuni, Timestamp, idadi ya miamala iliyojumuishwa katika kila BLOCK, ukubwa wa kilobaiti (kB) na kipimo cha kila BLOCK katika vitengo vya uzito (**WU** = *Vitengo vya Uzito*). Kipimo hiki cha mwisho ni cha manufaa, kwani hutuwezesha kutathmini uboreshaji wa BLOCK, ikizingatiwa kwamba kila BLOCK ya msururu mkuu inadhibitiwa na `4,000,000 WU`, au `4,000 kWU`.





- Shughuli za hivi majuzi.



![transactions](assets/fr/02.webp)



Sehemu ya muamala hutoa maelezo kuhusu kitambulisho cha kipekee cha muamala, thamani ya Bitcoin inayohusika, ukubwa katika baiti pepe (vB) - ambayo inawakilisha jumla ya data zote (ingizo na pato) - na kiwango cha malipo kinachohusishwa. Kwa mfano, muamala wenye ukubwa wa `153 vB` kwa kiwango cha `2 sat/vB` utatozwa `306 satoshi`.



### Utafutaji wa maji



Kutoka kwa menyu ya "**Vizuizi**", unaweza kufuatilia historia ya msururu mzima hadi kwenye BLOCK ya mwisho iliyochimbwa.



![blocs](assets/fr/03.webp)



Kwa kubofya BLOCK mahususi, unaweza kupata maelezo zaidi kuhusu taarifa na miamala iliyojumuishwa humo. Kwa mfano, kwa BLOCK 919330: una Hash ya BLOCK. Unaweza pia kwenda kwenye BLOCK iliyotangulia, kwani kila BLOCK inayochimbwa (mbali na Genesis) imeunganishwa na ile ya awali, ikibakiza Hash ya mtangulizi wake.



![metadata](assets/fr/04.webp)



Kwa kubofya kitufe cha **"Maelezo "**, unaweza kupata maelezo zaidi kuhusu BLOCK hii, kama vile hali yake, ambayo inathibitisha kuwa imeongezwa kwenye msururu mkuu uliobaki na kuenezwa. Pia una ugumu ambapo BLOCK inachimbwa: ugumu huu unawakilisha nguvu ya kompyuta inayohitajika kutatua tatizo la kriptografia ya Mining na hurekebishwa kila vitalu vya 2016 (kama wiki 2).



![details](assets/fr/05.webp)



Chini ya sehemu hii ya maelezo, tunapata miamala yote iliyojumuishwa katika BLOCK hii.



Muamala wa kwanza kabisa katika BLOCK unaitwa **muamala coinbase**. Inatumika kutenga zawadi ya Miner ya Mining (ada zote zinazohusiana na miamala iliyojumuishwa kwenye BLOCK na ruzuku ya BLOCK). Bitcoins zilizoundwa na shughuli hii zinaweza tu kutumika mara tu vitalu vingine 100 mfululizo vimechimbwa. Kwa maneno mengine, kuwa na uwezo wa kuzitumia, Miner itabidi kusubiri uzalishaji wa BLOCK ** 919430 **. Hiki kinajulikana kama [*"kipindi cha ukomavu "*](https://planb.network/fr/resources/glossary/maturity-period).



Coinbase ni shughuli maalum: ndiyo pekee isiyo na pembejeo halisi, kwani haitumii bitcoins yoyote kutoka kwa shughuli ya awali.




![coinbase](assets/fr/06.webp)



Shughuli nyingine zote zimegawanywa katika sehemu mbili: pembejeo na matokeo.



Ili bitcoins zitumike kama pembejeo katika shughuli mpya, mwanzilishi wa muamala lazima athibitishe umiliki wake kwa kutoa saini inayolingana na hati mahususi. Kila kipande cha bitcoins (UTXO) kina hati inayohitaji saini mahususi ambayo ufunguo wa faragha wa mmiliki pekee ndio unaweza kutoa. Maandishi haya ni ***scriptSig*** (katika ASM), yaliyoandikwa katika Hati ya Bitcoin, na yanaweza kuwa ya aina mbalimbali. Katika mfano huu, tunaweza kuona kwamba UTXO zilizotumiwa zilikuwa za aina ya P2SH hadi pato la aina ya P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Unaweza kufuatilia historia ya UTXO maalum kwa kutumia heuristics. Tunakualika ugundue mbinu tofauti za Bitcoin na jinsi ya kuimarisha usiri wa miamala yako ya Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Hebu tuchukue mfano wa gharama za muamala huu zinazotoka. Kwa kubofya kitambulisho cha muamala, tunaelekezwa kwenye sehemu ya **Miamala** kwenye ukurasa wa maelezo ya muamala.



![transaction](assets/fr/08.webp)



Kutoka kwa ukurasa huu, unaweza kujua ni BLOCK gani muamala ulijumuishwa. Kulingana na aina ya Address iliyotumika, muamala unaweza kuboresha data yake (*virtual byte*) na kwa hivyo ulipe ada kidogo za muamala. Muamala huu, kwa mfano, uliokoa 53% ya ada kwa kutumia umbizo asilia la SegWit BECH32 Address linaloanza na `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid mipako



Liquid Network ni [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) na kiwango cha 2 cha chanzo huria cha suluhu la itifaki ya Bitcoin. Hasa, inawezesha shughuli za haraka na za siri zaidi za Bitcoin.



Kwenye kichunguzi cha BLOCKSTREAM.info, bofya kitufe cha **"Liquid"** ili kubadili Liquid Network.



![liquid](assets/fr/10.webp)



Kubofya kwenye mojawapo ya shughuli tunazotaka kufuata, tunaona kwamba kiasi cha vipande vya Bitcoin vinabadilishwa na maneno "**Siri**". Kwenye mtandao huu, miamala inaweza kuwa ya siri, kwa hivyo hatuwezi kuona kiasi cha kila UTXO, ndani au nje ya muamala.



![liquid_trx](assets/fr/11.webp)



Hata hivyo, tunaona kwamba kanuni na taratibu zilizopo kwenye Layer kuu ya itifaki ya Bitcoin ni sawa: hati za kufunga za Bitcoin na ufuatiliaji wa UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network pia hutoa rasilimali za kidijitali zisizo na amana ambazo zinaweza kutumiwa na mashirika. Katika menyu ya **"Vipengee"**, utapata orodha ya vipengee vilivyosajiliwa, jumla yake na kikoa ambacho vinahusiana nacho.



![assets](assets/fr/13.webp)



Kwa kila kipengee, unaweza kufuatilia historia ya suala na kuchoma miamala (kufuta jumla iliyo katika mzunguko).



![assets_trxs](assets/fr/14.webp)




## Chaguo zaidi



Kichunguzi cha BLOCKSTREAM.info pia kinajumuisha taswira na ufuatiliaji wa miamala kwenye Testnet, Bitcoin, On-Chain na Liquid Network.



![testnet](assets/fr/15.webp)



Unapoenda kwenye mtandao wa Testnet, hutumii bitcoins halisi, lakini una vipengele vyote vilivyoelezwa hapo juu.



![liquid_testnet](assets/fr/16.webp)



Mtandao huu una urefu wa mnyororo tofauti, ambao unaweza kuunganisha na kupima uendeshaji wa taratibu za Bitcoin na Liquid.





- Sehemu ya API imejitolea kwa mtu yeyote anayetaka kujumuisha vitendaji fulani vya Kivinjari kwenye programu yao wenyewe. Kupitia API hii unaweza kuhoji mlolongo mkuu wa tabaka tofauti (On-Chain na Liquid), kufuatilia shughuli na kujua ada za wastani za shughuli katika BLOCK, kwa mfano.



![api](assets/fr/17.webp)



Sasa uko tayari kutumia uwezo kamili wa BLOCKSTREAM Explorer kuuliza blockchains kwenye tabaka za On-Chain na Liquid. Tunatumahi kuwa umepata mafunzo haya kuwa ya kuelimisha, na kupendekeza mafunzo yetu kwenye Kichunguzi kingine cha Bitcoin:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f