---
name: Blixt Wallet
description: Jinsi ya kuanza kutumia node yenye nguvu ya LN kwenye simu yako?
---
![cover](assets/cover.webp)


Mwongozo huu umetolewa kwa watumiaji wote wapya wanaotaka kuanza kutumia Bitcoin Lightning Network (LN) kwa CHANZO WAZIRI BILA MALIPO, NJIA KAMILI ISIYO YA UTUNZI.


Kwa kutumia [Blixt Wallet](https://blixtwallet.com/), nodi kamili ya LN kwenye simu yako ya mkononi, popote ulipo.


Iwapo hukuwahi kutumia Bitcoin Lightning Network, kabla ya kuanza, [tafadhali soma mlinganisho huu rahisi wa maelezo kuhusu Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## MAMBO MUHIMU:



- Blixt ni node ya kibinafsi, SI njia ya uelekezaji! Kumbuka hilo : Hiyo ina maana kwamba, chaneli zote za LN katika Blixt hazitatangazwa kwenye grafu ya LN (zinazoitwa chaneli za kibinafsi). Hiyo inamaanisha, NODE HII HAITAFANYA ROUTTING ya malipo ya wengine kupitia node ya Blixt. Njia hii ya Blixt SI ya kuelekeza, narudia. Kimsingi ni kuweza kudhibiti chaneli zako za LN na kufanya malipo yako ya LN kwa faragha, wakati wowote unapohitaji. Njia hii ya Blixt, ni muhimu kuwa mtandaoni na kusawazishwa TU KABLA ya kwenda kufanya miamala yako. Ndiyo sababu utaona ikoni juu inayoonyesha hali ya usawazishaji. Inachukua muda mfupi tu, kulingana na muda ulioiweka nje ya mtandao.



- Blixt inatumia LND (aezeed) kama Wallet backend, kwa hivyo usijaribu kuingiza aina zingine za pochi za Bitcoin ndani yake. [Hapa umeelezea aina za mbegu za Wallet Mnemonic](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Na hii hapa [orodha pana zaidi ya aina zote za pochi](https://walletsrecovery.org/). Kwa hivyo ikiwa hapo awali ulikuwa na nodi ya LND, unaweza kuleta seed na backup.channels kwenye Blixt, [kama inavyofafanuliwa katika mwongozo huu](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Mwishoni mwa mwongozo huu utapata sehemu maalum yenye ["vidokezo na mbinu"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt viungo muhimu - vione mwishoni mwa mwongozo huu, tafadhali alamisho.


---

## Blixt - Mawasiliano ya Kwanza


Kwa hivyo… Mama wa Darth aliamua kuanza kutumia LN na Blixt. Uamuzi mgumu, lakini busara. Blixt ni ya watu mahiri na wale ambao wanataka kujifunza zaidi, matumizi ya kina ya LN.


![blixt](assets/en/01.webp)


Darth amuonya mama yake:


"*Mama, ukianza kutumia Njia ya Blixt LN, utahitaji kwanza kujua Lightning Network ni nini na jinsi inavyofanya kazi, angalau katika kiwango cha msingi. [Hapa nimeweka pamoja orodha rahisi ya nyenzo kuhusu Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Tafadhali zisome kwanza.*".


Mama wa Darth alisoma nyenzo na akafanya hatua yake ya kwanza: kusakinisha Blixt kwenye kifaa chake kipya kabisa cha Android. Blixt inapatikana pia kwa iOS na macOS (desktop). Lakini hizo si za Mama wa Darth... Hata hivyo, inashauriwa kutumia toleo jipya zaidi la Android, angalau 9 au 10 kwa uoanifu na matumizi bora zaidi. Kuendesha node kamili ya LN kwenye kifaa cha mkononi si kazi rahisi na inaweza kuchukua nafasi (min 600MB) na kumbukumbu.


Mara tu unapofungua Blixt, skrini ya "Karibu" itakupa chaguzi kadhaa:


![blixt](assets/en/02.webp)


Kwenye kona ya juu kulia, utaona nukta 3 zinazoamilisha menyu na:



- "Wezesha Tor" - mtumiaji anaweza kuanza na mtandao wa Tor, haswa ikiwa alitaka kurejesha nodi ya zamani ya LND ambayo ilikuwa ikiendeshwa na marafiki wa Tor pekee.
- "Weka node ya Bitcoin" - ikiwa mtumiaji anataka kuunganisha kwenye node yake moja kwa moja, kusawazisha vizuizi kupitia Neutrino, anaweza kuifanya mara moja kutoka kwa skrini inayokaribishwa. Chaguo hili pia ni nzuri ikiwa muunganisho wako wa mtandao au Tor, sio thabiti sana kuunganishwa na nodi chaguo-msingi ya Bitcoin (node.blixtwallet.com).
- Hivi karibuni itaongezwa lugha hapo, ili mtumiaji aanze moja kwa moja na lugha inayostarehesha. Iwapo ungependa kuchangia mradi huu wa programu huria kwa tafsiri katika lugha zingine, [tafadhali jiunge hapa](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### CHAGUO A - Unda Wallet mpya


Ukichagua "kuunda Wallet mpya", utaelekezwa kwingine moja kwa moja hadi kwenye skrini kuu ya Blixt Wallet.


Hii ni "cockpit" yako na pia ni "Main LN Wallet", kwa hivyo fahamu, itakuonyesha tu salio la LN Wallet yako. Onchain Wallet inaonyeshwa tofauti (tazama C).


![blixt](assets/en/03.webp)


A - Blixt inazuia aikoni ya kiashiria cha usawazishaji. Hili ndilo jambo muhimu zaidi kwa node ya LN: kusawazishwa na mtandao. Ikiwa ikoni hiyo bado inafanya kazi, inamaanisha kuwa node yako HAIKO TAYARI! Kwa hivyo kuwa na subira, maalum kwa usawazishaji wa kwanza. Inaweza kuchukua hadi dakika 6-8, kulingana na kifaa chako na muunganisho wa intaneti.


Unaweza kuibofya na kuona hali ya usawazishaji:


![blixt](assets/en/04.webp)


Pia unaweza kubofya kitufe cha "Onyesha Kumbukumbu ya LND" (A) ikiwa ungependa kuona na kusoma maelezo zaidi ya kiufundi ya logi ya LND, kwa wakati halisi. Ni muhimu sana kwa utatuzi na kujifunza zaidi jinsi LN inavyofanya kazi.


B - Hapa unaweza kufikia Mipangilio yote ya Blixt, na ni mingi! Blixt inatoa vipengele na chaguzi nyingi tajiri za kudhibiti nodi yako ya LN kama mtaalamu. Chaguo hizo zote zimefafanuliwa kwa kina katika “[Ukurasa wa Vipengele vya Blixt](https://blixtwallet.github.io/features#blixt-options) - Menyu ya Chaguzi”.


C - Hapa unayo menyu ya "magic drawer", [pia imefafanuliwa kwa kina hapa](https://blixtwallet.github.io/features#blixt-drawer). Hapa kuna "Onchain Wallet" (B), Vituo vya Lightning (C), address, ikoni ya hali ya Vituo (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Je, ni menyu ya usaidizi, iliyo na viungo vya ukurasa wa Maswali Yanayoulizwa Mara kwa Mara / Miongozo, msanidi wa mawasiliano, ukurasa wa Github na kikundi cha usaidizi cha Telegraph.


E - Onyesha BTC yako ya kwanza ya Address, ambapo unaweza kuweka jaribio lako la kwanza la Sats. HII NI LAZIMA! Ukiweka moja kwa moja kwenye hiyo Address, inafungua kituo cha LN kuelekea Njia ya Blixt. Hiyo inamaanisha utaona Sats yako uliyoweka, ikiingia kwenye muamala mwingine wa onchain (tx), kwa ajili ya kufungua kituo hicho cha LN. Unaweza kuangalia hiyo kwenye Blixt onchain Wallet (ona nukta C), ukibofya kwenye menyu ya TX ya juu kulia.


![blixt](assets/en/06.webp)


Kama unavyoona kwenye Rekodi ya Muamala ya Onchain, hatua ni za kina sana zikionyesha mahali Sats inaenda (amana, fungua, funga chaneli).


MAPENDEKEZO:


Baada ya kupima hali kadhaa, tulifikia hitimisho kwamba ni bora zaidi kufungua njia kati ya 1 na 5 M Sats. Vituo vidogo vinaelekea kuisha haraka na kulipa % ya juu zaidi ya ada ikilinganishwa na chaneli kubwa zaidi.


F - Onyesha salio lako kuu la Lightning Wallet. Hii si jumla ya salio lako la Blixt Wallet, inawakilisha tu Sats uliyo nayo katika Vituo vya Lightning, vinavyopatikana kutuma. Kama ilivyoonyeshwa hapo awali, Onchain Wallet ni tofauti. Kumbuka kipengele hiki. Wallet ya onchain ni tofauti kwa sababu muhimu: hutumiwa hasa kwa kufungua / kufunga njia za LN.


Sawa, kwa hivyo sasa Mama wa Darth aliweka Sats kwenye hiyo onchain Address inayoonyeshwa kwenye skrini kuu. Inapendekezwa kuwa unapofanya hivyo, kuweka programu yako ya Blixt mtandaoni na kufanya kazi kwa muda, hadi BTC tx ichukuliwe na wachimbaji kwenye kizuizi cha kwanza.


Baada ya hapo inaweza kuchukua hadi dakika 20-30 hadi ithibitishwe kikamilifu na kituo kifunguliwe na utakiona kwenye Droo ya Uchawi - Vituo vya Lightning kama inavyotumika. Pia nukta ndogo ya rangi iliyo juu ya droo, ikiwa ni Green itaonyesha kuwa chaneli yako ya LN iko mtandaoni na iko tayari kutumika kutuma Sats kupitia LN.


Address na ujumbe wa kukaribisha unaoonyeshwa utatoweka. Hakuna haja tena ya kufungua kituo kiotomatiki sasa. Unaweza pia kuzima chaguo katika menyu ya Mipangilio.


Ni wakati wa kuendelea, kujaribu vipengele vingine na chaguo ili kufungua vituo vya LN.


Sasa, hebu tufungue chaneli nyingine na rika lingine la node. Blixt community put togheter [orodha ya nodi nzuri za kuanza kutumia na Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Utaratibu wa kufungua kituo cha LN katika Blixt**


Hii ni rahisi sana, chukua hatua chache tu na uvumilivu kidogo:



- Nimefika kwenye [Jumuiya ya Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) orodha ya programu zingine
- Chagua node na ubofye kiungo cha jina lake, itafungua ukurasa wake wa Amboss
- Bofya ili kuonyesha msimbo wa QR wa nodi ya URI Address


![blixt](assets/en/07.webp)


Fungua Blixt na uende kwenye droo ya juu - Njia za Lightning na ubofye kitufe cha "+".


![blixt](assets/en/08.webp)


Sasa, bofya kwenye (A) kamera ili kuchanganua msimbo wa QR kutoka ukurasa wa Amboss na maelezo ya nodi yatajazwa. Ongeza kiasi cha Sats kwa kituo unachotaka kisha uchague kiwango cha ada kwa tx. Unaweza kuiacha kiotomatiki (B) kwa uthibitisho wa haraka au uirekebishe kwa kutelezesha kitufe. Unaweza pia kubonyeza nambari kwa muda mrefu na kuihariri upendavyo.


Usiweke chini ya 1 sat/vbyte ! Kwa kawaida ni bora kushauriana na [ada za Mempool](https://Mempool.space/) kabla ya kufungua kituo na uchague ada inayofaa.


Imefanywa, sasa bonyeza tu kitufe cha "fungua kituo" na usubiri uthibitisho 3, ambao kawaida huchukua dakika 30 (takriban block 1 kila dakika 10).


Baada ya kuthibitishwa, utaona chaneli ikitumika katika sehemu yako ya "Njia za Lightning".


---

## Blixt - Mawasiliano ya Pili


Sawa kwa hivyo sasa tuna kituo cha LN chenye ukwasi wa OUTBOUND pekee. Hiyo inamaanisha kuwa tunaweza TUMA pekee, bado hatuwezi KUPOKEA Sats zaidi ya LN.


![blixt](assets/en/09.webp)


Kwa nini? Je, ulisoma miongozo iliyoonyeshwa mwanzoni? Hapana? Rudi na uzisome. Ni muhimu sana kuelewa jinsi chaneli za LN zinavyofanya kazi.


![blixt](assets/en/10.webp)


Kama unavyoona katika mfano huu, chaneli hufunguliwa kwa amana ya kwanza, usiwe na ukwasi mwingi wa INBOUND (“Inaweza kupokea”) lakini uwe na ukwasi mwingi OUTBOUND (“Inaweza kutuma”).


Kwa hivyo ni chaguo gani unazo, ikiwa unataka kupokea zaidi Sats juu ya LN?



- Tumia kiasi cha Sats kutoka kwa chaneli iliyopo. Ndiyo, LN ni mtandao wa malipo wa Bitcoin, unaotumiwa hasa kutumia Sats yako kwa haraka, kwa bei nafuu, kwa faragha na kwa urahisi. LN SI njia ya kushikia, kwa kuwa unayo onchain Wallet.



- Badilisha Sats, urudi kwenye onchain Wallet yako, ukitumia huduma ya kubadilishana nyambizi. Kwa njia hii hautumii Sats yako, lakini unairudisha kwa onchain yako mwenyewe Wallet. Hapa unaweza kuona kwa undani baadhi ya mbinu, katika [Ukurasa wa Miongozo ya Blixt](https://blixtwallet.github.io/guides).



- Fungua kituo cha INBOUND kutoka kwa mtoa huduma yeyote wa LSP. Hapa kuna onyesho la video kuhusu jinsi ya kutumia LNBig LSP kwa kufungua chaneli inayoingia. Hiyo inamaanisha, utalipa ada ndogo kwa chaneli TUPU (upande wako) na utaweza kupokea Sats zaidi kwenye chaneli hiyo. Ikiwa wewe ni mfanyabiashara anayepokea zaidi ya matumizi, hilo ni chaguo nzuri. Pia ikiwa unanunua Sats zaidi ya LN, kwa kutumia Robosati au LN Exchange nyingine yoyote.



- Fungua chaneli ya Dunder, iliyo na nodi ya Blixt au mtoaji wowote wa Dunder LSP. Kituo cha Dunder ni njia rahisi ya kupata ukwasi wa INBOUND, lakini wakati huo huo unaweka kiasi cha Sats kwenye chaneli hiyo. Pia ni nzuri kwa sababu itafungua kituo kwa [UTXO](https://en.Bitcoin.it/wiki/UTXO) ambayo haitoki kwenye Blixt Wallet yako. Hiyo inaongeza faragha. Pia ni nzuri kwa sababu, ikiwa huna Sats kwenye onchain Wallet, ili kufungua chaneli ya kawaida ya LN, lakini unayo kwenye LN Wallet nyingine, unaweza tu kulipa kutoka kwa hiyo Wallet nyingine kupitia LN ufunguzi na amana (upande wako) ya kituo hicho cha Dunder. [Maelezo zaidi jinsi Dunder inavyofanya kazi na jinsi ya kuendesha seva yako mwenyewe hapa](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Hapa kuna hatua za kuwezesha kufungua kituo cha Dunder:



- Nenda kwa Mipangilio, katika sehemu ya "Majaribio" washa kisanduku cha "Wezesha Dunder LSP".
- Mara baada ya kufanya hivyo, nenda nyuma hadi sehemu ya "Lightning Network" na utaona kwamba ilionekana chaguo "Weka Dunder LSP Server". Huko, kwa chaguo-msingi imewekwa "https://dunder.blixtwallet.com" lakini unaweza kuibadilisha na mtoa huduma mwingine yeyote wa Dunder LSP Address. [Hii hapa ni orodha ya jumuiya ya Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) iliyo na nodi zinazoweza kukupa chaneli za Dudner LSP kwa Blixt yako.
- Sasa unaweza kwenda kwenye skrini kuu na ubonyeze kitufe cha "Pokea". Kisha fuata utaratibu huu [imeelezwa katika mwongozo huu](https://blixtwallet.github.io/guides#guide-lsp).


Sawa, kwa hivyo baada ya chaneli ya Dunder kuthibitishwa (itachukua dakika chache) utaishia na kuwa na chaneli 2 za LN: moja ilifunguliwa mwanzoni kwa majaribio ya kiotomatiki (kituo A) na moja ikiwa na ukwasi zaidi wa ndani, iliyofunguliwa na Dunder (kituo B).


![blixt](assets/en/12.webp)


Vizuri, sasa wewe ni vizuri kwenda, kutuma na kupokea Sats ya kutosha juu ya LN !


HERI YA Bitcoin LIGHTNING!


---

## Blixt - Mawasiliano ya Tatu


Kumbuka, katika sura ya kwanza "ADDRESS ya Kwanza" kulikuwa na chaguo 2 kwenye skrini ya Karibu:


- [Chaguo A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Unda mpya Wallet
- Chaguo B - Rejesha Wallet


Kwa hiyo sasa hebu tujadili jinsi ya kurejesha Blixt Wallet au node nyingine yoyote iliyoanguka ya LND. Hili ni la kiufundi zaidi, lakini tafadhali zingatia. Sio ngumu hivyo.


### OPTION B - Rejesha Wallet


Hapo awali niliandika mwongozo mahususi kuhusu [jinsi ya kurejesha nodi ya Umbrel iliyoanguka](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), ambapo nilitaja pia mbinu ya kutumia Blixt kama mchakato wa kurejesha haraka, kwa kutumia faili ya seed + channel.backup kutoka Umbrel.


Pia niliandika mwongozo jinsi ya kurejesha node yako ya Blixt au kuhamisha Blixt yako hadi kifaa kingine, [hapa](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Lakini hebu tueleze kwa hatua rahisi mchakato huu. Kama unavyoona kwenye picha hapo juu, kuna mambo 2 unapaswa kufanya ili kurejesha nodi yako ya awali ya Blixt/LND:



- kisanduku cha juu ndipo inabidi ujaze maneno yote 24 kutoka kwa seed yako (node ya zamani / iliyokufa)
- chini kuna chaguo mbili za vitufe vya kuingiza / kupakia faili ya chelezo cha channel., iliyohifadhiwa hapo awali kutoka kwa nodi yako ya zamani ya Blixt/LND. Inaweza kutoka kwa faili ya ndani (unaipakia kwenye kifaa chako hapo awali) au inaweza kutoka kwa Hifadhi ya Google / eneo la mbali la iCloud. Blixt wana chaguo hili la kuhifadhi nakala rudufu ya vituo vyako moja kwa moja kwenye hifadhi ya Google / iCloud. Angalia maelezo zaidi katika [Ukurasa wa Vipengele vya Blixt](https://blixtwallet.github.io/features#blixt-options).


Hata hivyo, kutaja, ikiwa hapo awali hukuwa na chaneli zozote za LN zilizofunguliwa, hakuna haja ya kupakia faili yoyote ya chelezo cha channels. Ingiza tu maneno 24 seed na ubonyeze kitufe cha kurejesha.


Usisahau kuamilisha Tor, kutoka kwenye menyu ya vitone 3 vya juu, kama tulivyoeleza katika sehemu ya Chaguo A. Ndivyo ilivyokuwa wakati ulikuwa na Tor TU na hukuweza kuwasiliana naye kupitia clearnet (kikoa/IP). Vinginevyo sio lazima.


Kipengele kingine muhimu ni kuweka node maalum ya Bitcoin kutoka kwenye orodha hiyo ya juu. Kwa chaguo-msingi inasawazisha blocks kutoka kwa node.blixtwallet.com (modi ya neutrino) lakini unaweza kuweka node nyingine yoyote ya Bitcoin ambayo hutoa usawazishaji wa neutrino.


Kwa hivyo mara tu unapojaza chaguo hizo, na kugonga kitufe cha kurejesha, Blixt itaanza kwanza kusawazisha block kupitia Neutrino kama tulivyoelezea katika sura ya Mawasiliano ya Kwanza. Kwa hivyo kuwa na subira na uangalie mchakato wa kurejesha kwenye skrini kuu, kwa kubofya kwenye ikoni ya kusawazisha.


![blixt](assets/en/14.webp)


Kama unavyoona katika mfano huu, inaonyesha kuwa block za Bitcoin zimesawazishwa kwa 100% (A) na mchakato wa kurejesha uko kwenye kozi (B). Hiyo inamaanisha kuwa chaneli za LN uliokuwa nazo hapo awali, zitafungwa na pesa zitarejeshwa kwenye Blixt onchain wallet yako.


Utaratibu huu unachukua muda! Kwa hivyo tafadhali, kuwa na subira na ujaribu kuweka Blixt yako hai na mtandaoni. Usawazishaji wa awali unaweza kuchukua hadi dakika 6-8 na vituo vya kufunga vinaweza kuchukua hadi dakika 10-15. Kwa hivyo ni bora kuwa na kifaa chaji vizuri.


Mara tu mchakato huu unapoanza, unaweza kuangalia katika Droo ya Kiajabu - Vituo vya Umeme, hali ya kila moja ya chaneli zako za awali, zinazoonyesha kuwa ziko katika hali ya "inasubiri kufungwa". Mara tu kila kituo kinapofungwa, unaweza kuona tx ya kufunga kwenye onchain wallet (angalia Magic Drawer - Onchain), na ufungue logi ya menyu ya tx.


![blixt](assets/en/15.webp)


Pia itakuwa vizuri kuangalia na kuongeza kama hawapo, wenzako wa awali uliokuwa nao katika nodi yako ya zamani ya LN. Kwa hivyo nenda kwenye menyu ya Mipangilio, chini hadi "Lightning Network" na uweke chaguo "Onyesha Wenzake wa Umeme".


![blixt](assets/en/16.webp)


Ndani ya sehemu hiyo utaona wenzako ambao umeunganishwa nao kwa wakati huo na unaweza kuongeza zaidi, bora kuongeza zile ulizokuwa nazo hapo awali. Nenda tu kwenye Ukurasa wa Amboss, tafuta lakabu za node zako au node ID na changanua URI ya node zao.


![blixt](assets/en/17.webp)


Kama unavyoweza kwenye picha hapo juu, kuna mambo 3:


A - inawakilisha node ya clearnet Address URI (kikoa/IP)


B - inawakilisha node ya kitunguu cha Tor Address URI (.onion)


C - ni msimbo wa QR wa kuchanganua kwa kutumia kamera yako ya Blixt au kitufe cha kunakili.


Njia hii ya Address URI lazima uiongeze kwenye orodha ya programu zingine. Kwa hivyo fahamu haitoshi tu node alias jina au nodeID.


Sasa unaweza kwenda kwenye Droo ya Kichawi (menyu ya juu kushoto) - Njia za Lightning, na unaweza kuona ni urefu gani wa block ya ukomavu pesa zitarejeshwa kwenye onchain yako address.

![blixt](assets/en/18.webp)


Nambari hiyo ya block 764272 ndipo pesa zitatumika katika Bitcoin onchain yako address. Na inaweza kuchukua hadi block 144 kutoka kwa block ya 1 hadi vitakapotolewa[Kwa hivyo angalia hiyo katika Mempool](https://Mempool.space/).


Na ndivyo hivyo. Subiri tu kwa subira hadi vituo vyote vifungwe na pesa zirudishwe kwenye onchain yako Wallet.


👉 **Njia ya kurejesha siri :**


Kuna njia nyingine ya kurejesha node yako ya Blixt LND bila hata kufunga chaneli. Lakini imefichwa kutoka kwa watumiaji wa kawaida wa noob, kwa sababu njia hii ni ya wale tu wanaojua wanachofanya.


Iwapo utahitaji kuhamisha node yako iliyopo (inayofanya kazi) ya Blixt kwa kifaa kingine kipya, bila kufunga chaneli zilizopo za LN, itabidi ufanye hatua hizi:



- Tunadhani kwamba tayari umehifadhi Blixt Wallet seed (maneno 24 aezeed)
- Kwenye kifaa cha zamani, nenda kwenye "Mipangilio" - sehemu ya kurekebisha - "database ya Compact LND". Hatua hii ni ya hiari lakini inapendekezwa ikiwa unataka ukubwa mdogo wa faili ya channel.db. Kawaida ni kubwa kabisa, kulingana na shughuli yako ya nodi. Hii itaanzisha tena Blixt na kusawazisha saizi ya faili ya db.
- Mara baada ya kuanza upya, nenda kwa "Mipangilio" na ubadilishe jina lako la kawaida la pak kuwa "Hampus". Hii itawasha chaguo zilizofichwa, kwa watumiaji wa hali ya juu pekee.
- Nenda chini hadi sehemu ya "Debug" na utaona chaguo jipya "Hamisha faili ya channel.db". ONYO! Mara tu unapotuma utumaji huu, nodi iliyopo ya Blixt LN itazimwa kwenye kifaa hiki cha zamani na itasafirisha hifadhidata yote ya node (channel.db) tayari kuletwa kwenye kifaa kipya.
- Faili hii ya db itahifadhiwa kwenye folda iliyoteuliwa kwenye kifaa chako cha zamani (Hati au Vipakuliwa) na kutoka hapo utalazimika kuihamisha kama ilivyo kwenye kifaa chako kipya. Unaweza kutumia kwa mfano [LocalSend FOSS app](https://github.com/localsend/localsend) kuhamisha faili moja kwa moja kati ya vifaa.
- Kwa wakati huu Blixt yako ya zamani LAZIMA ibaki imefungwa. USIFUNGUE TENA!
- Mara tu unapohamisha faili ya channel.db hadi kwenye kifaa kipya, anza usakinishaji mpya wa Blixt na uchague "Rejesha Wallet" katika skrini ya kwanza.
- Kwenye kitufe ambapo inasema "Chagua faili ya SCB" bonyeza kwa muda mrefu (SIO kubofya rahisi!) kisha utaona chaguo la kuchagua faili ya channel.db ambapo unaihifadhi ndani ya kifaa kipya. Ukibonyeza tu kitufe hicho kitatumia kwa chaguo-msingi faili ya SCB (iliyo na njia za kufunga), haifanyi kazi kwa chelezo kamili za chaneli za moja kwa moja.
- Weka maneno 24 seed kisha ubofye "Rejesha"
- Utaona kwamba Blixt itaanza kusawazisha na Neutrino. Unaweza kutazama kumbukumbu za kusawazisha pia.
- KUMBUKA! Jaribu kuweka Blixt wazi wakati wote kwenye awamu hii! Usiruhusu iendelee kulala au funga skrini ya programu. Hiyo inaweza kukatiza usawazishaji wa awali na itabidi uifanye tena. Subiri kwa subira, haichukui zaidi ya dakika chache.
- Mara tu ulandanishi wa block za awali utakapokamilika, itachanganua kwa haraka anwani zako za awali za wallet na kisha vituo vyako vitarejea mtandaoni, vikiwa hai na vyema.
- Kwa bahati mbaya historia ya malipo ya awali na address haziwezekani (bado) kurejeshwa. Lakini hiyo sio muhimu sana hata hivyo.


Na KIMEMALIZA! Sasa una node ya Blixt LN iliyorejeshwa kikamilifu. Inaweza kufanya kazi pia na chelezo zingine za LND (Umbrel, Raspiblitz n.k) ikiwa ulihifadhi ipasavyo faili ya channel.db. Kwa hivyo Blixt inaweza kuokoa node yoyote iliyokufa ya LND.


---

## Blixt - Mawasiliano ya Nne


Sura hii inahusu ubinafsishaji na ujue vizuri zaidi Njia ya Blixt. Sitaeleza vipengele vyote vinavyopatikana, ni vingi sana na tayari vilielezwa katika [Ukurasa wa Vipengele vya Blixt](https://blixtwallet.github.io/features).


Lakini nitaonyesha baadhi ya zile muhimu kwenda mbele kwa kutumia Blixt yako na uwe na uzoefu mzuri.


### A - Jina (NameDesc)


![blixt](assets/en/19.webp)


[The NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) ni kanuni ya kuwasilisha "jina la mpokeaji" katika ankara za BOLT11.


Hili linaweza kuwa jina lolote na linaweza kubadilishwa wakati wowote.


Chaguo hili ni muhimu sana katika hali mbalimbali, unapotaka kutuma jina pamoja na maelezo ya Invoice, ili mpokeaji apate kidokezo kutoka kwa nani alipokea hizo Sats. Hili ni la hiari kabisa na pia katika skrini ya malipo, mtumiaji anatakiwa kutia alama kwenye kisanduku kinachoonyesha kutuma jina la utani.


Huu hapa ni mfano wa jinsi unavyoweza kuonekana unapotumia [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Huu ni mfano mwingine unaotuma kwa programu nyingine ya Wallet inayotumia NameDesc:


![blixt](assets/en/21.webp)


### B - Sanduku ya Lightning


Kuanzia v0.6.9-420 [iliyotangazwa hivi majuzi](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), Blixt alianzisha kipengele kipya chenye nguvu cha Lightning Address katika Blixt.


Kipengele hiki kipya ni chaguo la kuingia, hakijawashwa kwa chaguomsingi!


Kwa sasa Kisanduku chaguomsingi cha LN kinaendeshwa na seva ya Blixt na kutoa @blixtwallet.com LN Address. Lakini MTU YEYOTE aliye na node ya umma ya LND anaweza kuendesha seva ya Sanduku ya Lightning na kutoa LN Address kwa kikoa chake, kujilinda.


Hivi sasa, seva ya Blixt inasambaza tu malipo yanayotumwa kwa anwani za LN @blixtwallet.com kwa watumiaji wa Blixt ambao huweka LN address yao. Watumiaji lazima waweke node yao ya Blixt Wallet katika "hali inayoendelea" ili kupokea malipo haya kwenye anwani zao za @blixtwallet.com LN.

Tazama katika maelezo ya toleo onyesho la video kuhusu jinsi ya kusanidi LN Address yako katika Blixt.


LN Address hii iliyotekelezwa katika programu ya Blixt Wallet, ni kama gumzo kupitia LN, papo hapo na ya kufurahisha, ambayo pia inasaidia [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (kuongeza jina la utani kwenye malipo). Unaweza kuongeza katika orodha ya anwani zako zote za kawaida za LN unazotumia mara kwa mara na uwe nazo kwa ajili ya kupiga gumzo. Sasa Blixt inaweza kuchukuliwa kuwa programu kamili ya gumzo ya LN 😂😂.


Kipengele kingine muhimu ni usaidizi kamili kutoka kwa LUD-18 (ambayo pia [Stacker.News](https://stacker.news/r/DarthCoin) na wengine wanaitumia).


![blixt](assets/en/22.webp)


Kama unavyoona kwenye picha ya skrini iliyo hapo juu, kutuma kutoka kwa akaunti ya Stacker News, ilionyesha vyema nembo + LN Address + ujumbe. Njia hiyo hiyo hufanya kazi kwa kutuma kutoka kwa Blixt, unaweza kuambatisha Blixt LN Address yako au kuongeza tu jina la pak (lililowekwa hapo awali katika mipangilio ya Blixt) au hata zote mbili.


Chaguo hili kutoka kwa LUD-18 linaweza kuwa muhimu pia kwa huduma za usajili, ambapo mtumiaji anaweza kutuma lakabu maalum (SI jina la node yako au jina lako halisi!) na kulingana na hilo unaweza kusajiliwa au kupokea tena ujumbe maalum au chochote kingine. Kuambatisha jina lak ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ maoni ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) kwenye malipo ya LN kunaweza kuwa na kesi nyingi za matumizi!


Huu hapa ni msimbo wa [Lightning Box](https://github.com/hsjoberg/lightning-box) ikiwa unaiendesha kwa ajili yako mwenyewe, kwa ajili ya familia yako na marafiki, kwenye nodi yako mwenyewe.


Hapa pia unaweza kuendesha [seva ya Dunder ya LSP](https://github.com/hsjoberg/dunder-lsp) ya node za simu za Blixt na kutoa ukwasi kwa watumiaji wa Blixt ikiwa una nodi nzuri ya umma ya LN (inafanya kazi na LND pekee).


### C - Cheleza Njia za LN na maneno ya seed


Hiki ni kipengele muhimu sana!


Baada ya kufungua au kufunga chaneli ya LN unapaswa kufanya nakala rudufu. Inaweza kufanywa kwa mikono kuhifadhi faili ndogo kwenye kifaa cha ndani (folda ya kupakua kawaida) au kutumia Hifadhi ya Google au akaunti ya iCloud.


![blixt](assets/en/23.webp)


Nenda kwa Mipangilio ya Blixt - sehemu ya Wallet. Hapo unayo chaguzi za kuhifadhi data zote muhimu kwa Blixt Wallet yako:



- "Onyesha Mnemonic" - itaonyesha maneno 24 seed ili kuyaandika
- "Ondoa Mnemonic kwenye kifaa" - hii ni hiari na uitumie tu ikiwa unataka kuondoa maneno ya seed kwenye kifaa chako. Hii HAITAfuta Wallet yako, seed pekee. Lakini fahamu! Hakuna njia ya kuzirejesha ikiwa hukuziandika kwanza.
- "Hamisha nakala rudufu ya kituo" - chaguo hili litahifadhi faili ndogo kwenye kifaa chako cha ndani, kwa kawaida kwenye folda ya "vipakuliwa", kutoka ambapo unaweza kuichukua na kuihamisha nje ya kifaa chako, kwa uhifadhi salama.
- "Thibitisha nakala rudufu ya kituo" - hii ni chaguo nzuri ikiwa unatumia Hifadhi ya Google au iCloud kuangalia uadilifu wa nakala rudufu iliyofanywa kwa mbali.
- " Hifadhi rudufu ya kituo cha hifadhi ya Google" - itahifadhi faili ya chelezo kwenye hifadhi yako ya kibinafsi ya Google. Faili imesimbwa kwa njia fiche na kuhifadhiwa katika hifadhi tofauti kuliko faili zako za kawaida za google. Kwa hivyo hakuna wasiwasi ambao unaweza kusomwa na mtu yeyote. Kwa vyovyote vile faili hiyo haina maana kabisa bila maneno ya seed, kwa hivyo hakuna mtu anayeweza kuchukua pesa zako kutoka kwa faili hiyo pekee.


Ningependekeza kwa sehemu hii yafuatayo:



- tumia kidhibiti cha nenosiri ili kuhifadhi salama seed yako na faili chelezo. KeePass au Bitwarden ni nzuri sana kwa hilo na inaweza kutumika kwenye majukwaa mengi na kujipangisha mwenyewe au nje ya mtandao.
- FANYA HUDUMA KILA WAKATI unapofungua au kufunga kituo. Faili hiyo inasasishwa na maelezo ya vituo. Hakuna haja ya kuifanya baada ya kila muamala uliyofanya kwenye LN. Hifadhi rudufu ya kituo haihifadhi maelezo hayo, inahifadhi hali ya kituo pekee.


![blixt](assets/en/24.webp)


---

## Blixt - Vidokezo na Mbinu


### KESI YA 1 - MATATIZO YA KUSAwazisha


"_Blixt yangu haisawazishi... Blixt yangu haionyeshi salio... Blixt yangu haiwezi kufungua vituo... Nilijaribu kuirejesha kwenye kifaa kingine... nk_"


Matatizo haya yote huanza kwa sababu KIFAA CHAKO HAKITANDIKIWI VIZURI. Tafadhali elewa kipengele hiki muhimu: Blixt ni nodi ya simu ya LND, inayotumia Neutrino kusawazisha/kusoma vizuizi.



- Haya hapa ni maelezo ya kiufundi kidogo kutoka [Bitcoin Magazine](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Hizi hapa ni nyenzo zaidi za kiufundi kutoka [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Hivi ndivyo unavyoweza kuwezesha Neutrino kwenye node yako ya nyumbani na kutoa vichujio vya block vya node ya simu yako, kutoka. [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


KUMBUSHO: Kutumia Neutrino juu ya clearnet ni salama kabisa, IP au xpub yako haivujishwi. Unasoma tu block kutoka kwa node ya mbali kwa kutumia Neutrino. Ni hayo tu. Mengine yote yanafanywa kwenye kifaa chako cha karibu.


Kwa hivyo HAKUNA HAJA ya kuitumia na Tor. Tor itaongeza utulivu mkubwa kwenye mchakato wako wa kusawazisha na itafanya Blixt yako kutokuwa thabiti sana. Ikiwa unataka kutumia Tor, hakikisha unafanya nini na uwe na muunganisho mzuri na uvumilivu. Kesi sawa ya kutumia VPN. Kuwa mwangalifu ni muda gani wa kusubiri unapewa kutoka kwa VPN hiyo.


Unaweza kujaribu muda wa kusubiri wa seva ya neutrino kwa kuipiga kwa urahisi, kutoka kwa Kompyuta au kutoka kwa simu yako.


![blixt](assets/en/25.webp)


Hii ni ping ya kawaida kwa seva ya neutrino europe.blixtwallet.com, hii inaonyesha kwamba muunganisho ni mzuri sana na muda wa majibu wa wastani wa 50ms na TTL wa 51. Muda wa kujibu unaweza kutofautiana lakini sio sana. TTL lazima iwe thabiti.


Ikiwa maadili haya ni ya juu kuliko 100-150ms basi mchakato wako wa kusawazisha utakoma au mbaya zaidi, inaweza kusababisha chaneli kufungwa na wenzao ! Usipuuze kipengele hiki.


Bila usawazishaji unaofaa, pia huwezi kuona salio sahihi au chaneli zako za LN hazitaingia mtandaoni na kufanya kazi. Haijalishi una giga ultra terra mbps ngapi una kasi ya kupakua HAIJALISHI. Inajalisha majibu ya wakati na TTL (wakati wa kuishi).


Hii ni kama kesi ya jumla kwa watumiaji wa LATAM. Sijui nini kinatokea huko chini lakini nyie mna muunganisho mbaya na pings za zaidi ya 200ms ambazo zinaweza kutatiza usawazishaji wowote.


Kwa hivyo ni suluhisho gani kwa watumiaji hawa waliokata tamaa?



- acha kutumia Blixt na Tor. Haifai kabisa
- unaweza kutumia VPN lakini uchague kwa busara na ufuatilie wakati wote wa ping. Tumia moja iliyo karibu na eneo lako la kijiografia. Umbali unamaanisha muda zaidi wa kujibu ms, kumbuka.
- chagua kwa busara wenzako wa neutrino, hapa kuna orodha ya seva za neutrino za umma zinazojulikana:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Njia nyingine ni kuchagua moja kutoka kwa orodha hii ya node zinazotangaza "vichujio kompakt" (BIP157 / neutrino) - [Kichujio cha Neutrino Ukurasa wa Bitnodi](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Chagua moja ambayo iko karibu na eneo lako la kijiografia.


Njia nyingine (njia bora) ni kuunganishwa na node ya jumuiya ya karibu, inayoendeshwa na rafiki au kikundi unachokijua, na inatoa muunganisho wa neutrino. [Haya hapa ni maagizo ya jinsi ya kufanya hivyo.](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Node zao hazitaathiriwa kwa njia yoyote, zinahitaji tu muunganisho thabiti na wa umma.


Kuna haja ya seva nyingi za Neutrino katika eneo la LATAM, kwa usawazishaji bora na wa haraka. Kwa hivyo tafadhali jipange, pamoja na jumuiya ya eneo lako la Bitcoin, na uamue ni nani na wapi anaendesha Bitcoin Core + Neutrino kwa matumizi yako mwenyewe. Na IP ya umma tu inatosha. Ikiwa huna ufikiaji wa IP ya umma, unaweza kutumia IP ya VPS na kutengeneza handaki ya waya kwenye node yako ya nyumbani. Kwa njia hiyo unaelekeza trafiki yote kwa IP yako ya ndani ya VPS, bila kufichua habari yoyote ya kibinafsi kuhusu node yako ya nyumbani.


### KESI YA 2 - USIMALIZE KUSAwazisha


"_Blixt yangu ina muunganisho mzuri na seva ya neutrino lakini imekwama kusawazisha._"


#### Seva ya Wakati


Wakati mwingine watu hutumia vifaa anuwai vya zamani au hawajaunganishwa vizuri kwenye seva ya wakati. Neutrino inasawazisha sawa hadi ifikie vizuizi halisi ambavyo havilingani na saa halisi za ndani. Utaona kwenye kumbukumbu ya Blixt LND hitilafu ikisema kwamba "muhuri wa muda wa kuzuia ni mbali na siku zijazo" au kitu kinachohusiana na "kichwa usipitishe ukaguzi wa akili".


Marekebisho ya haraka: weka wakati na tarehe sahihi ya kifaa chako na uwashe tena Blixt.


#### Nafasi ya chini kwenye kifaa


Wakati mwingine kwa kutumia kifaa cha zamani, na nafasi ya chini, inaweza kufikia kikomo cha kizingiti na kukwama. Hakika kwa zaidi unatumia nodi hii ya simu ya LND, faili za neutrino zinakuwa kubwa na pia faili ya channel.db.


Marekebisho ya haraka: Nenda kwenye Chaguo za Blixt - Sehemu ya Utatuzi - Chagua "komesha LND na ufute faili za Neutrino". Itaanzisha upya programu na kuanza usawazishaji mpya. Wakati mwingine urekebishaji huu wa haraka unaweza kurekebisha pia data iliyoharibika. Kumbuka kwamba itachukua muda, kati ya dakika 1 na 3 kusawazisha upya kikamilifu. HAUFUTI fedha au chaneli zilizopo, lakini ndiyo, baada ya kusawazisha upya kunaweza kusababisha kuchanganuliwa upya kwa anwani zako za Bitcoin na hiyo inaweza kuchukua muda zaidi.


Hatua inayofuata ni kuangalia ni data ngapi bado inashughulikiwa. Unaweza kuona hili katika maelezo ya Programu ya Android - data. Ikiwa bado ni kubwa kuliko 400-500MB, unaweza kubandika faili za LND. Kwa hiyo nenda kwa Chaguzi za Blixt - sehemu ya Debug - Chagua "Compact DB LND". Anzisha tena programu ya Blixt ikiwa haifanyi kiotomatiki. Mchanganyiko unafanyika wakati wa kuanza na ni mara moja tu. Sasa utaona kuwa data ya Blixt haijashughulikiwa zaidi.


#### Hali inayoendelea


Wakati mwingine watu hawafungui Blixt kwa muda mrefu, kwa hivyo ni ya zamani sana kusawazisha. Lakini wanatarajia kusawazishwa mara moja wanapoifungua.


Tafadhali kuwa na subira, na uangalie gurudumu la juu linalozunguka. Hiari unaweza kwenda kwa Chaguzi - Tazama Maelezo ya Node na uone ikiwa imesawazishwa kwa minyororo na kusawazishwa kwa grafu iliyo alama "kweli". Bila hiyo "kweli" kutaja huwezi kutumia Blixt ipasavyo, huwezi kuona salio kwa usahihi, huwezi kuona chaneli za LN mtandaoni, huwezi kufanya malipo.


Marekebisho ya haraka: Kuna chaguo thabiti la "kudumisha hai" nodi yako ya Blixt. Nenda kwa Chaguzi - Majaribio - Chagua "Amilisha Hali ya Kudumu". Hiyo itaanzisha upya Blixt yako na itaweka huduma ya LND katika hali inayoendelea, aka itakuwa hai kila wakati na kuweka usawazishaji wako mtandaoni, hata ukibadilisha hadi programu nyingine au funga Blixt kwa urahisi (usilazimishe kufunga au kuua kazi). Unaweza kuiweka kama hiyo siku nzima ikiwa uko kwenye muunganisho thabiti na unahitaji kutumia Blixt mara kadhaa. Haitatumia betri nyingi sana.


### KESI YA 3 - NATAKA KUHAMIA KWENYE KIFAA KINGINE


SAWA kuhusu hali hii niliandika mwongozo wa kina kwenye [Ukurasa wa Maswali Yanayoulizwa Mara kwa Mara](https://blixtwallet.github.io/faq#blixt-restore): yenye chaguo 2, haraka (kufunga chaneli kwa kushirikiana kabla ya kuhama) na polepole (lazimisha kufunga chaneli kwa sababu kifaa cha zamani kimekufa).


Lakini nataka kurudia hapa mambo kadhaa muhimu na kuongeza utaratibu mpya wa "siri".


KUMBUSHO:



- Daima fanya nakala ya hali ya vituo vyako (SCB) BAADA ya kila wakati unapofungua au kufunga kituo. Inachukua sekunde chache tu kuifanya.
- Usiweke faili za SCB za zamani, ili usichanganyike na kuzirejesha. Hazina maana kabisa na zinaweza kusababisha utaratibu wa adhabu ikiwa utaziweka. Tumia toleo la mwisho la faili ya SCB kila wakati ikiwa utaendelea kurejesha.
- Hifadhi faili ya SCB (ni maandishi yaliyosimbwa kwa njia fiche yenye kiendelezi .bin) nje ya kifaa chako, mahali salama. Unaweza kutumia [LocalSend](https://github.com/localsend/localsend) kuhamisha faili hii kwenye Kompyuta au kifaa kingine.
- Hifadhi pia seed ya Blixt Wallet yako mahali salama, kwa mfano kidhibiti cha nenosiri cha nje ya mtandao / USB iliyosimbwa.


Njia ya siri: Jinsi ya kuhamisha nodi ya Blixt bila kufunga vituo vilivyopo. Kwa hili utahitaji kusoma kwa makini sehemu ya awali "Mawasiliano ya Tatu" katika mwongozo huu kuhusu "Rejesha Wallet".


Utaratibu huu SI WA NOOBS, ni kwa watumiaji wa hali ya juu tu! Ndio maana haijafunguliwa sana na ninapendekeza kuifanya tu kwa usaidizi kutoka kwa Blixt devs au usaidizi wangu. Tafadhali usipuuze ushauri huu.


### KESI YA 4 - NINI WATUMIA WENZAKE KUFUNGUA VITUO?


Kama nilivyoandika katika [Ukurasa wa miongozo ya Blixt](https://blixtwallet.github.io/guides) kuna njia nyingi za kufungua vituo kwa kutumia nodi hii ya simu ya LND. Lakini baadhi ya vipengele muhimu ningependa kukukumbusha hapa:



- wazi na node za LSP zinazojulikana na marafiki waliothibitishwa na jamii. [Angalia orodha hapa](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- usifungue na node za Tor tu. Hizo hazina thamani na utapata masuala tu ya kutoweza kufanya malipo. Haijalishi ni mzuri kiasi gani rafiki yako "mkimbiaji wa nodi" na node ya Tor kwenye msitu, haitakupa njia bora zaidi za nodi ya kibinafsi ya rununu. Hufungui chaneli na mtu kwa sababu ni rafiki yako. Hii sio Facebook! Unafungua kituo cha: njia nzuri, ada ndogo, upatikanaji.
- hakuna haja ya kufungua tani ya shit ya njia ndogo, 2-3 au max 4, lakini kwa kiasi kizuri cha Sats. Usifungue njia ndogo, hazina maana kabisa. Chini ya 200k kwa simu ya mkononi haina matumizi mengi.
- kumbuka LSP zinazotoa chaneli zinazoingia na JIT (kwa wakati tu). Hizo ni muhimu sana kwa sababu hauitaji kutumia UTXO zako zozote, unaweza kulipa chaneli ya ufunguzi kwa pesa ambazo tayari unazo kwenye pochi zingine za LN, ukiweka mrundikano na kuzitayarisha ili chaneli kubwa ifunguke. Unapaswa kutumia chaneli hizi za JIT kwa faida yako. [Nimefafanua katika mwongozo huu](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) chaguo zaidi kwa wenzao kwa nodi za faragha kama vile Blixt. Pia [hapa katika mwongozo huu uliochapishwa kwenye SN](https://stacker.news/items/679242/r/DarthCoin) Nilieleza jinsi ya kudhibiti ukwasi wa nodi za kibinafsi za simu.


---

## Hitimisho


Sawa, kuna vipengele vingine vingi vya kushangaza ambavyo Blixt hutoa, nitakuruhusu uvigundue kimoja baada ya kingine na ufurahie.


Programu hii haithaminiwi sana, hasa kwa sababu haiungwi mkono na ufadhili wowote wa VCs, inaendeshwa na jumuiya, jenga kwa upendo na shauku kwa Bitcoin na Lightning Network.


Node hii ya simu ya LN, Blixt ni chombo chenye nguvu sana mikononi mwa watumiaji wengi, ikiwa wanajua jinsi ya kuitumia vizuri. Hebu fikiria, unatembea duniani kote na nodi ya LN katika mfuko wako na hakuna mtu atakayeijua.


Na bila kuzungumza juu ya vipengele vingine vyote vya tajiri vinavyokuja, ambavyo ni programu chache sana au hakuna programu zingine za Wallet zinaweza kutoa.


Wakati huo huo hapa kuna viungo vyote kuhusu Njia hii ya Umeme ya Bitcoin:



- [Blixt Ukurasa Rasmi](https://blixtwallet.com/)
- [Blixt ukurasa wa Github](https://github.com/hsjoberg/blixt-Wallet/)
- [Ukurasa wa Vipengele vya Blixt](https://blixtwallet.github.io/features) - ikifafanua moja baada ya nyingine kila kipengele na utendakazi.
- [Ukurasa wa Blixt Maswali Yanayoulizwa Mara kwa Mara](https://blixtwallet.github.io/faq) - Orodha ya Maswali na Majibu na utatuzi wa Blixt
- [Ukurasa wa Miongozo ya Blixt](https://blixtwallet.github.io/guides) - maonyesho, mafunzo ya video, miongozo ya ziada na kesi za utumiaji za Blixt
- Pakua: [Duka la Google Play](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK ya kupakua moja kwa moja](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Kikundi cha telegram kwa usaidizi wa moja kwa moja](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Ukurasa wa ufadhili wa Geyser](https://geyser.fund/project/blixt) - toa Sats jinsi unavyopenda kusaidia mradi
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - gumzo lisilojulikana la LN
- [Onyesho la Blixt - video ya matangazo](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Kalenda](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - video ya matangazo (unaweza kujaribu matumizi yako ya 1-7 ya GW7)
- [Kipeperushi cha A4 kinachoweza kuchapishwa chenye hatua za kwanza kwa kutumia Blixt, katika lugha mbalimbali](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt pia inatoa onyesho kamili la utendaji](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) pamoja na tovuti yake au kwenye tovuti maalum ya toleo, ili kuwa na majaribio kamili ya matumizi, kabla ya kuanza kutumia katika ulimwengu halisi.


---
**KANUSHO:**


*Silipwi au kuungwa mkono kwa njia yoyote na wasanidi programu hii. Niliandika mwongozo huu kwa sababu niliona kuwa nia ya programu hii ya Wallet inaongezeka na watumiaji wapya bado hawaelewi jinsi ya kuanza nayo. Pia kusaidia Hampus (dev kuu) na hati kuhusu kutumia nodi hii Wallet.*


*Sina nia nyingine yoyote ya kutangaza programu hii ya LN, zaidi ya kusukuma mbele matumizi ya Bitcoin na LN. Hii ndiyo njia pekee!*


---
