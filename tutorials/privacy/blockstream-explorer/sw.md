---
name: Blockstream Explorer
description: Chunguza safu kuu ya Bitcoin na Liquid Network
---

![cover](assets/cover.webp)



Blockstream Explorer ni mradi unaowezesha uchunguzi wa miamala na hali ya kimataifa ya itifaki ya Bitcoin, pamoja na [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid iliyotengenezwa na kampuni ya Blockstream.



Ilianzishwa mwaka wa 2014 na Blockstream, kampuni iliyoanzishwa na Adam Back, mgunduzi wa [blockstream.info](https://blockstream.info) unalenga kutoa miundombinu thabiti ya Bitcoin, kuhakikisha utangamano na ufuatiliaji wa shughuli kati ya tabaka (on-chain na Liquid), huku ukiimarisha usalama na faragha ya mtumiaji.



Katika somo hili, tutaangalia ni nini kinachoitofautisha, huduma zake, na jinsi inavyotoa ufuatiliaji usio na mshono wa uendeshaji na hali ya tabaka za Bitcoin za on-chain na Liquid.



## Anza kutumia Blockstream Explorer



### Nenda kwenye kituo kikuu



Unapoenda kwa kichunguzi cha Blockstream.info, kwenye "**Dashibodi**", mlolongo mkuu wa itifaki ya Bitcoin huchaguliwa kwa chaguo-msingi. Kutoka kwa kiolesura hiki, unayo muhtasari wa:





- Saizi kuu ya mnyororo: Vitalu vilivyochimbwa hivi majuzi.



![blocks](assets/fr/01.webp)



Sehemu hii inatoa taarifa kuhusu vitalu vya hivi majuzi vilivyochimbwa, muhuri wa muda, idadi ya miamala iliyojumuishwa katika kila kizuizi, saizi ya kilobaiti (kB) na kipimo cha kila kizuizi katika vitengo vya uzito (**WU** = *Vitengo vya Uzito*). Kipimo hiki cha mwisho ni cha manufaa, kwa vile hutuwezesha kutathmini uboreshaji wa kizuizi, ikizingatiwa kwamba kila sehemu ya msururu mkuu ni `4,000,000 WU`, au `4,000 kWU`.





- Shughuli za hivi majuzi.



![transactions](assets/fr/02.webp)



Sehemu ya muamala hutoa maelezo kuhusu kitambulisho cha kipekee cha muamala, thamani ya bitcoin inayohusika, saizi ya baiti pepe (vB) - ambayo inawakilisha jumla ya data zote (ingizo na pato) - na kiwango cha ada husika. Kwa mfano, muamala wenye ukubwa wa `153 vB` kwa kiwango cha `2 sat/vB` utatozwa ada ya `306 satoshi`.



### Utafutaji wa maji



Kutoka kwa menyu ya "**Vizuizi**", unaweza kufuatilia historia ya msururu mzima hadi kwenye kizuizi cha mwisho kilichochimbwa.



![blocs](assets/fr/03.webp)



Kwa kubofya kizuizi maalum, unaweza kupata maelezo zaidi kuhusu habari na shughuli zilizojumuishwa ndani yake. Kwa mfano, kwa block 919330: utaona heshi ya block. Unaweza pia kuelekea kwenye kizuizi kilichotangulia, kwani kila kizuizi kilichochimbwa (mbali na Genesis) kimeunganishwa na kilichotangulia, na kubakiza heshi ya mtangulizi wake.



![metadata](assets/fr/04.webp)



Kwa kubofya kitufe cha **"Maelezo "**, unaweza kupata maelezo zaidi kuhusu kizuizi hiki, kama vile hali yake, ambayo inathibitisha kuwa kimeongezwa kwenye mnyororo mkuu uliobaki na kuenezwa. Pia una ugumu ambapo kizuizi hiki kinachimbwa: ugumu huu unawakilisha nguvu ya kompyuta inayohitajika kutatua tatizo la kriptografia ya mining na hurekebishwa kila vitalu vya 2016 (kama wiki 2).



![details](assets/fr/05.webp)



Chini ya sehemu hii ya maelezo, tunapata shughuli zote zilizojumuishwa kwenye kizuizi hiki.



Muamala wa kwanza kabisa kwenye block unaitwa **transaction coinbase**. Inatumika kutenga zawadi ya mchimbaji mining (ada zote zinazohusiana na miamala iliyojumuishwa kwenye kizuizi na ruzuku ya kizuizi). Bitcoins zilizoundwa na shughuli hii zinaweza tu kutumika mara tu vitalu vingine 100 mfululizo vimechimbwa. Kwa maneno mengine, ili kuweza kuzitumia, mchimbaji atalazimika kusubiri uzalishaji wa block **919430**. Hiki kinajulikana kama [*"kipindi cha ukomavu "*](https://planb.academy/fr/resources/glossary/maturity-period).



Coinbase ni shughuli maalum: ndiyo pekee isiyo na pembejeo halisi, kwani haitumii bitcoins yoyote kutoka kwa shughuli ya awali.




![coinbase](assets/fr/06.webp)



Shughuli nyingine zote zimegawanywa katika sehemu mbili: pembejeo na matokeo.



Ili bitcoins zitumike kama pembejeo katika shughuli mpya, mwanzilishi wa muamala lazima athibitishe umiliki wake kwa kutoa saini inayolingana na hati mahususi. Kila kipande cha bitcoins (UTXO) kina hati inayohitaji saini mahususi ambayo ufunguo wa faragha wa mmiliki pekee ndio unaweza kutoa. Maandishi haya ni ***scriptSig*** (katika ASM), yaliyoandikwa katika Hati ya Bitcoin, na yanaweza kuwa ya aina mbalimbali. Katika mfano huu, tunaweza kuona kwamba UTXO zilizotumiwa zilikuwa za aina ya P2SH kwa pato la aina ya P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Unaweza kufuatilia historia ya UTXO maalum kwa kutumia heuristics. Tunakualika ugundue mbinu tofauti za Bitcoin na njia za kuimarisha usiri wa miamala yako kwenye Bitcoin :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Hebu tuchukue mfano wa gharama zinazotoka za muamala huu. Kwa kubofya kitambulisho cha muamala, tunaelekezwa kwenye sehemu ya **Miamala** kwenye ukurasa wa maelezo ya muamala.



![transaction](assets/fr/08.webp)



Kutoka kwa ukurasa huu, unaweza kujua ni kizuizi kipi muamala ulijumuishwa. Kulingana na aina ya anwani iliyotumika, muamala unaweza kuboresha data yake (*virtual byte*) na kwa hivyo ulipe ada kidogo za muamala. Muamala huu, kwa mfano, uliokoa 53% ya ada kwa kutumia umbizo asili la SegWit Bech32 la anwani inayoanza na `bc1q`.



![trx_details](assets/fr/09.webp)



## Safu ya Liquid



Liquid Network ni [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) na suluhisho la chanzo huria cha kiwango cha 2 cha itifaki ya Bitcoin. Hasa, inawezesha shughuli za haraka na za siri zaidi za bitcoin.



Kwenye kichunguzi cha Blockstream.info, bofya kitufe cha **"Liquid"** ili kubadili mtandao wa Liquid.



![liquid](assets/fr/10.webp)



Kubofya kwenye moja ya shughuli tunazotaka kufuatilia, tunaona kwamba kiasi cha bitcoin chunk kinabadilishwa na maneno "**Siri**". Kwenye mtandao huu, miamala inaweza kuwa ya siri, kwa hivyo hatuwezi kuona kiasi cha kila UTXO, ndani au nje ya muamala.



![liquid_trx](assets/fr/11.webp)



Hata hivyo, tunaona kwamba kanuni na taratibu zilizopo kwenye safu kuu ya itifaki ya Bitcoin ni sawa: scripts za kufunga bitcoin na ufuatiliaji wa UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network pia hutoa rasilimali za dijitali zisizo na amana ambazo zinaweza kutumiwa na mashirika. Katika menyu ya **"Vipengee"**, utapata orodha ya vipengee vilivyosajiliwa, jumla yake na kikoa ambacho vinahusiana nacho.



![assets](assets/fr/13.webp)



Kwa kila kipengee, unaweza kufuatilia historia ya suala na kuchoma miamala (kufuta jumla iliyo katika mzunguko).



![assets_trxs](assets/fr/14.webp)




## Chaguo zaidi



Kichunguzi cha Blockstream.info pia kinajumuisha taswira na ufuatiliaji wa miamala kwenye Testnet, Bitcoin, on-chain na Liquid Network.



![testnet](assets/fr/15.webp)



Unapoenda kwenye mtandao wa Testnet, hutumii bitcoins halisi, lakini una vipengele vyote vilivyoelezwa hapo juu.



![liquid_testnet](assets/fr/16.webp)



Mtandao huu una urefu wa mnyororo tofauti, ambao unaweza kuunganisha na kupima uendeshaji wa taratibu za Bitcoin na Liquid.





- Sehemu ya API imejitolea kwa mtu yeyote anayetaka kujumuisha vitendaji fulani vya Kivinjari kwenye programu yao wenyewe. Kupitia API hii unaweza kuhoji mlolongo mkuu wa tabaka tofauti (on-chain na Liquid), kufuatilia shughuli na kujua ada za wastani za shughuli katika block, kwa mfano.



![api](assets/fr/17.webp)



Sasa uko tayari kutumia uwezo kamili wa Blockstream Explorer wa kuuliza maswali kuhusu blockchains kwenye tabaka za on-chain na Liquid. Tunatumahi kuwa umepata mafunzo haya kuwa ya kuelimisha, na kupendekeza mafunzo yetu juu ya mvumbuzi mwingine wa Bitcoin:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f