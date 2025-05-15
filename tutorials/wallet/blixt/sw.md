---
name: Blixt

description: Simu ya LN Nodi Wallet
---

![presentation](assets/blixt_intro_en.webp)


## Sehemu yenye nguvu ya BTC/Umeme mfukoni mwako, popote ulipo


Ningependa kukujulisha kwa nodi mpya ya simu ya BTC/LN yenye kuvutia na yenye nguvu na Wallet – Blixt. Jina linatokana na Kiswidi na linamaanisha "umeme".

Iwapo hukuwahi kutumia Bitcoin Lightning Network, kabla ya kuanza, tafadhali soma [mfano huu rahisi wa maelezo kuhusu Lightning Network (LN)](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport).


## MAMBO MUHIMU:


### 1. Blixt ni nodi ya kibinafsi, SI njia ya uelekezaji! Kumbuka hilo.


Hiyo inamaanisha, chaneli zote za LN katika Blixt hazitatangazwa kwenye grafu ya LN (inayoitwa njia za kibinafsi). Hiyo inamaanisha, NODE HII HAITAFANYA ROUTTING ya malipo ya wengine kupitia nodi ya Blixt. [Soma zaidi kuhusu vituo vya faragha na vya umma hapa](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).


Njia ya rununu ya Blixt SI ya kuelekeza, narudia. Kimsingi ni kuweza kudhibiti chaneli zako za LN na kufanya malipo yako ya LN kwa faragha, wakati wowote unapohitaji.


Nodi ya simu ya Blixt, ni muhimu kuwa mtandaoni na kusawazishwa KABLA tu ya kufanya miamala yako. Ndiyo sababu utaona ikoni juu inayoonyesha hali ya usawazishaji. Inachukua muda mfupi tu, kulingana na muda ulioiweka nje ya mtandao na kusawazisha tena grafu ya LN.


### 2. Blixt inatumia LND (aezeed) kama Wallet backend, kwa hivyo usijaribu kuleta aina nyingine za pochi za Bitcoin ndani yake.


[Hapa umefafanua aina za pochi](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Kwa hivyo ikiwa hapo awali ulikuwa na nodi ya LND, unaweza kuleta seed na chelezo.channels kwenye Blixt, [kama inavyofafanuliwa katika mwongozo huu](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).


### 3. Blixt viungo muhimu (tafadhali alamisho):



- [Hazina ya Blixt Github](https://github.com/hsjoberg/blixt-Wallet) | [Matoleo ya Github](https://github.com/hsjoberg/blixt-Wallet/releases) (pakua faili ya apk moja kwa moja)
- [Ukurasa wa Vipengele vya Blixt](https://blixtwallet.github.io/features) - inaelezea moja baada ya nyingine kila kipengele na utendakazi.
- [Ukurasa wa Blixt Maswali Yanayoulizwa Mara kwa Mara](https://blixtwallet.github.io/faq) - Orodha ya Maswali na Majibu na utatuzi wa Blixt
- [Ukurasa wa Miongozo ya Blixt](https://blixtwallet.github.io/guides) - maonyesho, mafunzo ya video, miongozo ya ziada na kesi za utumiaji za Blixt
- [Kipeperushi cha A4 kinachoweza kuchapishwa](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) yenye hatua za kwanza kwa kutumia Blixt, katika lugha mbalimbali.
- Blixt pia inatoa onyesho kamili la utendaji sawa kwenye [tovuti yake](https://blixtwallet.com) au kwenye [toleo la wavuti](https://blixt-Wallet-git-master-hsjoberg.vercel.app/), ili kufanya majaribio kamili ya matumizi, kabla ya kuanza kutumia Blixt katika ulimwengu halisi.
- [Ukurasa wa ufadhili wa Geyser](https://geyser.fund/project/blixt) - toa Sats jinsi unavyopenda kusaidia mradi
- [Kikundi cha usaidizi cha telegramu](https://t.me/blixtwallet)


# Vipengele muhimu vinavyopatikana


## Nodi ya Neutrino


Blixt huunganisha kwa chaguo-msingi kwa seva ya Blixt ili kusawazisha vizuizi na faharasa na Neutrino (Njia ya SPV ya Uthibitishaji wa Malipo Rahisishwa), lakini mtumiaji pia anaweza kuunganisha kwenye nodi yake mwenyewe. Inashangaza kuona kwamba kusawazisha nodi ya SPV inachukua chini ya dakika 5, kwa upande wangu kwenye Android 11, kuwa tayari kutumia Full node Wallet (On-Chain na LN).


## Kamilisha Njia Isiyo ya Utunzaji


Mtumiaji anaweza kudhibiti chaneli zake kwa kutumia Interface iliyo rahisi kutumia na maelezo ya kutosha yanayoonyeshwa ili kuwa na matumizi mazuri. Katika menyu ya droo ya juu kushoto, unaweza kwenda kwa njia za Umeme ili kuanza kufungua na nodi zingine, unavyotaka. Usisahau kuwezesha Tor katika mipangilio. Ni bora zaidi kwa faragha na pia kwa sababu kama nodi ya rununu, ukibadilisha muunganisho wako wa intaneti / clearnet IP mara kwa mara, programu zingine zinaweza kutatizwa. Ukiwa na URI ya nodi ya Tor, utakuwa na kitambulisho sawa cha kibinafsi kila wakati bila kujali eneo / IP yako.


## Hifadhi nakala / Rudisha Njia ya LND


Kipengele chenye nguvu, rahisi kudhibiti na muhimu ni kurejesha nodi zingine za LND zilizokufa, kwa orodha ya maneno 24 ya seed na faili ya chelezo. [Huu hapa ni mwongozo wa jinsi ya kurejesha nodi za Umbrel zilizokufa katika Blixt ikiwa ni SHTF.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)


Mtumiaji pia ana chaguo la kuhifadhi nakala rudufu ya kituo cha Blixt kwenye Hifadhi ya Google na/au hifadhi ya ndani kwenye kifaa chake cha mkononi (ili kuihamisha baadaye mahali salama, mbali na simu yako).


Mchakato wa kurejesha ni rahisi sana: ingiza neno la 24 seed, ongeza faili ya chelezo (iliyonakiliwa hapo awali kwenye kumbukumbu ya rununu), na ubofye kurejesha. Itachukua muda kusawazisha na kuchanganua vizuizi vyote vya miamala yako ya awali. Vituo vitafungwa kiotomatiki na pesa zitarejeshwa kwa On-Chain Wallet yako (angalia menyu ya droo ya juu kushoto - On-Chain).


**Kumbuka** Ikiwa hapo awali ulikuwa na chaneli zilizofunguliwa na nodi yako ya zamani nyuma ya Tor, lazima kwanza uwashe chaguo la Tor (na uanze upya programu) kutoka kwa mipangilio ya menyu. Kwa njia hii, utaratibu wa kufunga hautashindwa na / au chaguo la kufunga la kulazimishwa halitatumika.


Kumbuka kuweka chelezo chaneli zako za LN baada ya kufungua na/au kufunga chaneli. Inachukua sekunde chache tu kuwa salama. Baadaye, unaweza kuhamisha faili chelezo hadi mahali salama mbali na kifaa chako cha mkononi.

Ili kujaribu seed yako katika hali ya urejeshaji, kabla ya kuongeza pesa, tumia tu seed ya maneno 24 sawa (aezeed) katika BlueWallet. Ikiwa BTC Address iliyozalishwa ni sawa katika Blixt, ni vizuri kwenda. Hakuna haja ya kutumia BlueWallet baada ya hapo, unaweza kufuta tu Wallet iliyojaribiwa kwa urejesho.


## Tor iliyojengwa ndani


Mara tu ukiiwasha, programu itaanza tena nyuma ya mtandao wa Tor. Kuanzia hatua hii, unaweza kuona katika mipangilio ya menyu kitambulisho chako cha nodi na kitunguu Address, ili nodi zingine ziweze kufungua njia kwa nodi yako ndogo ya rununu ya Blixt. Au tuseme una nodi yako mwenyewe nyumbani na unataka kuwa na chaneli ndogo na nodi yako ya rununu ya Blixt. Mchanganyiko kamili.


## Dunder LSP - Mtoa Huduma ya Ukwasi


Kipengele rahisi na cha ajabu ambacho kinawapa watumiaji wapya uwezo wa kuanza kukubali BTC kwenye Lightning Network mara moja, bila hitaji la kuweka fedha za On-Chain na kisha kufungua vituo vya LN.


Kwa watumiaji wapya, hii ni habari njema kwa sababu wanatakiwa kuwa na uwezo wa kuanzia mwanzo, moja kwa moja kwenye LN. Ili kufanya hivyo, tengeneza tu LN Invoice kutoka skrini kuu kwenye kitufe cha "kupokea", ingiza kiasi, maelezo, nk, na ulipe kutoka kwa Wallet nyingine. Blixt itafungua chaneli ya hadi 400k Sats kwa kila shughuli inayopokelewa. Unaweza kufungua chaneli nyingi ikiwa ni lazima.


Kesi ya kupendeza na muhimu ni kama ifuatavyo: tuseme kiasi chako cha kwanza ulichopokea ni 200k. Blixt itafungua chaneli ya 400k Sats na tayari 200k (ondoa ada za kufungua) kwa upande wako, lakini kwa kuwa bado una "nafasi" ya 200k inapatikana, unaweza kupokea zaidi. Kwa hivyo malipo yanayofuata, tuseme 100k, yatatumwa moja kwa moja kupitia kituo hiki, bila ada za ziada, na bado una nafasi ya 100k ili kupokea zaidi.


Lakini ukichagua kupokea, tuseme, 300k kwa malipo ya tatu, itafungua chaneli nyingine mpya ya 400k na kusukuma hizi 300k kando yako.


Ikiwa kuna maombi mengi, node ya Blixt inaweza kurekebisha uwezo wa kituo wakati wa ufunguzi.


## Ufunguzi wa Kituo Kiotomatiki


Katika mipangilio, mtumiaji anaweza kuamsha chaguo hili na kuwa na huduma ya kiotomatiki inayofungua njia na nodi bora na njia kulingana na usawa unaopatikana katika On-Chain Wallet ya programu ya Blixt. Hiki ni kipengele cha manufaa kwa watumiaji wapya ambao hawana uhakika ni nodi gani ya kufungua kituo na/au jinsi ya kufungua chaneli ya LN. Ni kama majaribio ya kiotomatiki ya LN.


**Kumbuka:** chaguo hili hutumika mara moja pekee, unapounda Blixt Wallet yako mpya, na huwashwa kwa chaguomsingi. Kwa hivyo ikiwa mtumiaji mpya atachanganua msimbo wa On-Chain QR kwenye skrini kuu na kuweka Sats yake ya kwanza kwenye Address hiyo, Blixt itafungua kiotomatiki kituo na hizo Sats, kwa kutumia nodi ya umma ya Blixt.


## Huduma zinazoingia za Liquidity


Kipengele maalumu kwa wafanyabiashara wanaohitaji ukwasi zaidi UNAOINGIA, rahisi kutumia. Ili kufanya hivyo, chagua tu mmoja wa watoa huduma za ukwasi kutoka kwenye orodha, lipa kiasi unachotaka kwa kituo, na upe kitambulisho cha nodi yako, na kutoka hapo, kituo kitafungua kwa nodi yako ya Blixt.


## Orodha za Mawasiliano


Kipengele muhimu ikiwa unataka kuwa na orodha ya kudumu ya wapokeaji ambao unafanya nao biashara mara nyingi. Orodha hii inaweza kujumuisha LNURLs, anwani za umeme, au maelezo ya malipo tuli/ ankara za siku zijazo. Kwa sasa, orodha hii haiwezi kuhifadhiwa nje ya programu, lakini kuna mipango ya kuwa na chaguo la kuihamisha.


## LNURL na Umeme Address


Usaidizi kamili wa LNURL. Unaweza kulipa kwa LNURL, LN-auth, LN-chan ombi kwa kutumia LNURL.

Unaweza kutuma kwa LN Address yoyote na pia kuiongeza kwenye orodha yako ya anwani.

Pia kuanzia mistari. 0.6.9 inapatikana ili kupokea kwa aina yako mwenyewe ya LN Address _@blixtwallet.com_, kupitia [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box) kipengele.


## Keysend


Kipengele chenye nguvu sana ambacho pochi chache za rununu zina. Unaweza kutuma/kusukuma fedha moja kwa moja kupitia chaneli au kuelekeza kwenye nodi nyingine, na kuongeza ujumbe ikiwa ni lazima. Ni kama gumzo la siri juu ya LN. Kipengele hiki ni muhimu sana kwa kuonyesha ujumbe kwenye bango la Amboss.space ([hapa kuna mwongozo kwenye ubao huu wa Amboss](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).


## Kusaini ujumbe


Zana muhimu sana ya kusaini ujumbe kwa ufunguo wa faragha wa nodi ya Blixt, ujumbe wa uthibitishaji, na kadhalika. Pochi chache sana za rununu zina kipengele hiki, karibu hakuna.


## Malipo ya Vituo Vingi - Malipo ya Njia Nyingi (MPP)


Kipengele muhimu kwa malipo ya LN, kinachokuruhusu kugawa malipo ya LN katika sehemu nyingi, kwenye vituo vingi. Ni njia nzuri ya kusawazisha ukwasi kwenye mtandao na kuboresha faragha.


## Kivinjari cha Umeme


Msururu wa huduma za watu wengine na LN, iliyopangwa ndani ya kivinjari rahisi, kinachofikika na kinachofaa mtumiaji. Pia ni njia nzuri ya kukuza biashara zinazokubali BTC kwenye LN. Hiki ni kipengele ambacho kitaendelezwa zaidi katika siku zijazo. Kwa sasa, haifanyi kazi nyuma ya Tor, kwa hivyo kuvinjari programu hizi itakuwa wazi (clearnet).


## Wachunguzi wa logi


Hii ni zana yenye nguvu ya kuangalia kumbukumbu za LND na hali ya nodi yako kwa ujumla. Kuna chaguo la kuhifadhi faili ya kumbukumbu. Ni muhimu sana kuwa na kumbukumbu hizi karibu ikiwa utahitaji usaidizi wa msanidi katika kutambua masuala fulani.


## Usalama


Unaweza kuweka katika mipangilio ya programu, kwa usalama zaidi wa Wallet/nodi yako, uwezekano wa kuanzisha programu kwa msimbo wa PIN na/au alama ya vidole.


## On-Chain Wallet


Kipengele hiki kimefichwa kidogo, kwenye menyu ya droo iliyo upande wa juu kushoto. Kwa kuwa haitumiwi mara kwa mara na mtumiaji wa LN, haionekani kwenye skrini kuu. Lakini hiyo ni sawa, unaweza kuwa nayo kwenye Wallet tofauti ambapo unaweza kudhibiti anwani na kutazama kumbukumbu ya muamala, kwa kuleta seed yako kwenye Sparrow kwa mfano. Labda katika siku zijazo, Blixt Wallet pia itajumuisha kipengele cha kusimamia UTxOs. Lakini kwa sasa, tumia On-Chain Wallet TU kufungua au kufunga vituo kwenye LN.


## Vipengele maalum



- Pamoja na mistari. 0.6.9 ilianzishwa "hali inayoendelea" inayoruhusu mtumiaji kuendesha Blixt kama nodi ya mtandaoni ya LN kila wakati, na kufanya huduma za LND zikiwa hai na LN Wallet tayari kupokea/kutuma wakati wowote.
- Vituo Rahisi vya Taproot - ruhusu kufungua chaneli za Taproot kwa faragha zaidi na vipengele vya kina
- Vituo vya uthibitishaji sifuri kwa kutumia Blixt Dunder LSP
- Kipakiaji cha kasi ("Ulandanishi wa kituo cha LN") - Hii inamaanisha kuwa vituo vyote vitasawazishwa haraka wakati wa kuanza, kwa utaftaji bora zaidi. Ingawa inakera kidogo kwamba lazima uone skrini ya kusawazisha mwanzoni, itahakikisha kuwa Wallet inajua kuhusu vituo vyote na malipo yatakuwa ya haraka na ya kuaminika zaidi.
- Imetafsiriwa katika lugha 25+!


## "Mayai ya Pasaka"


Ndiyo, katika programu ya Blixt, kuna baadhi ya vipengele vilivyofichwa, vitu vidogo vinavyofanya programu kupendeza, kuwezesha vitendo vya kufurahisha/kuvutia na majibu.

Kidokezo: jaribu kubofya mara mbili kwenye nembo ya Blixt kwenye droo 🙂 nitakuruhusu ugundue mengine.


# Blixt Kuanza Mwongozo wa Hatua kwa Hatua


**Kidokezo:** kama mtumiaji mpya wa LN, ukianza kutumia Njia ya Blixt LN, utahitaji kwanza kujua Lightning Network ni nini na jinsi inavyofanya kazi, angalau katika kiwango cha msingi. [Hapa tunaweka pamoja orodha rahisi ya nyenzo kuhusu Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Tafadhali zisome kwanza.


Kuendesha nodi kamili ya LN kwenye kifaa cha mkononi si kazi rahisi na inaweza kuchukua nafasi (min 600MB) na kumbukumbu. Tunapendekeza kuwa na kifaa kizuri cha mkononi, kilichosasishwa na kutumia angalau Android 11 kama OS.


Mara tu unapofungua Blixt, skrini ya "Karibu" itakupa chaguzi kadhaa:


![Demo Blixt 01](assets/blixt_t01.webp)


Kwenye kona ya juu kulia, utaona nukta 3 zinazoamilisha menyu na:



- "Wezesha Tor" - mtumiaji anaweza kuanza na mtandao wa Tor, haswa ikiwa alitaka kurejesha nodi ya zamani ya LND ambayo ilikuwa ikiendeshwa na marafiki wa Tor pekee.
- "Weka nodi ya Bitcoin" - ikiwa mtumiaji anataka kuunganishwa na nodi yake moja kwa moja, kusawazisha vizuizi kupitia Neutrino, anaweza kuifanya mara moja kutoka kwa skrini ya kukaribisha. Chaguo hili pia ni nzuri ikiwa muunganisho wako wa mtandao au Tor, sio thabiti sana kuunganishwa na nodi ya Bitcoin (node.blixtwallet.com).


## Hatua ya Kwanza - Unda Wallet mpya


Ukichagua "kuunda Wallet mpya", utaelekezwa kwingine moja kwa moja kwenye skrini kuu ya Blixt Wallet.


Hiki ni "cockpit" yako na pia ni "Main LN Wallet", kwa hivyo fahamu, itakuonyesha tu salio la LN Wallet yako. Onchain Wallet inaonyeshwa kando (tazama C).


![Demo Blixt 02](assets/blixt_t02.webp)


A - Blixt inazuia aikoni ya kiashiria cha usawazishaji. Hili ndilo jambo muhimu zaidi kwa nodi ya LN: kusawazishwa na mtandao. Ikiwa ikoni hiyo bado inafanya kazi, inamaanisha kuwa nodi yako HAIKO TAYARI! Kwa hivyo kuwa na subira, maalum kwa usawazishaji wa kwanza. Inaweza kuchukua hadi dakika 6-8, kulingana na kifaa chako na muunganisho wa intaneti.


Unaweza kuibofya na kuona hali ya usawazishaji:


![Demo Blixt 03](assets/blixt_t03.webp)


Pia unaweza kubofya kitufe cha "Onyesha Kumbukumbu ya LND" (A) ikiwa ungependa kuona na kusoma maelezo zaidi ya kiufundi ya batli ya LND, kwa wakati halisi. Ni muhimu sana kwa utatuzi na kujifunza zaidi jinsi LN inavyofanya kazi.


B - Hapa unaweza kufikia Mipangilio yote ya Blixt, na ni mingi! Blixt inatoa vipengele na chaguzi nyingi tajiri za kudhibiti nodi yako ya LN kama mtaalamu. Chaguo hizo zote zimefafanuliwa kwa kina katika [“Ukurasa wa Vipengele vya Blixt - Menyu ya Chaguzi”](https://blixtwallet.github.io/features#blixt-options).


C - Hapa unayo menyu ya "Droo ya Uchawi", ambayo pia imeelezewa kwa undani hapa. Hapa kuna "Onchain Wallet" (B), Vituo vya Umeme (C), Anwani, ikoni ya hali ya Vituo (A), Keysend (D).


![Demo Blixt 04](assets/blixt_t04.webp)


D - Je, ni menyu ya usaidizi, iliyo na viungo vya ukurasa wa Maswali Yanayoulizwa Mara kwa Mara / Miongozo, msanidi wa mawasiliano, ukurasa wa Github na kikundi cha usaidizi cha Telegraph.


E - Onyesha BTC yako ya kwanza ya Address, ambapo unaweza kuweka jaribio lako la kwanza la Sats. HII NI LAZIMA! Ukiweka moja kwa moja kwenye hiyo Address, inafungua kituo cha LN kuelekea Njia ya Blixt. Hiyo inamaanisha utaona Sats yako uliyoweka, ikiingia kwenye muamala mwingine wa onchain (tx), kwa ajili ya kufungua kituo hicho cha LN. Unaweza kuangalia hiyo kwenye Blixt onchain Wallet (angalia nukta C), ukibofya kwenye menyu ya TX ya juu kulia.


![Demo Blixt 05](assets/blixt_t05.webp)


Kama unavyoona kwenye Rekodi ya Muamala ya Onchain, hatua hizo ni za kina sana zinaonyesha mahali Sats inaenda (amana, fungua, funga chaneli)


**Pendekezo:** baada ya kujaribu hali kadhaa, tulifikia hitimisho kwamba ni bora zaidi kufungua njia kati ya 1 na 5 M Sats. Vituo vidogo vinaelekea kuisha haraka na kulipa % ya juu zaidi ya ada ikilinganishwa na chaneli kubwa zaidi.


F - Onyesha salio lako kuu la Umeme Wallet. Hii SI jumla ya salio lako la Blixt Wallet, inawakilisha tu Sats uliyo nayo katika Vituo vya Umeme, vinavyopatikana kutuma. Kama ilivyoonyeshwa hapo awali, Onchain Wallet ni tofauti. Kumbuka kipengele hiki. Onchain Wallet ni tofauti kwa sababu muhimu: hutumiwa hasa kwa kufungua / kufunga njia za LN.


Sawa, sasa umeweka Sats kwenye hiyo onchain Address inayoonyeshwa kwenye skrini kuu. Inapendekezwa kuwa unapofanya hivyo, kuweka programu yako ya Blixt mtandaoni na kufanya kazi kwa muda, hadi BTC tx ichukuliwe na wachimbaji kwenye kizuizi cha kwanza.


Baada ya hapo inaweza kuchukua hadi dakika 20-30 hadi ithibitishwe kikamilifu na kituo kifunguliwe na utakiona kwenye Droo ya Uchawi - Vituo vya Umeme kama inavyotumika. Pia nukta ndogo ya rangi iliyo juu ya droo, ikiwa ni Green itaonyesha kuwa chaneli yako ya LN iko mtandaoni na iko tayari kutumika kutuma Sats kupitia LN.


Address na ujumbe wa kukaribisha unaoonyeshwa utatoweka. Hakuna haja tena ya kufungua kituo kiotomatiki sasa. Unaweza pia kuzima chaguo katika menyu ya Mipangilio.


Ni wakati wa kuendelea, kujaribu vipengele vingine na chaguo ili kufungua vituo vya LN.


Sasa, hebu tufungue chaneli nyingine na rika lingine la nodi. Jumuiya ya Blixt ikiweka pamoja [orodha ya nodi nzuri za kuanza kutumia na Blixt.](https://github.com/hsjoberg/blixt-Wallet/issues/1033)


### Utaratibu wa kufungua chaneli ya kawaida isiyotangazwa (ya faragha) ya LN katika nodi yako ya rununu ya Blixt.


Hii ni rahisi sana, chukua hatua chache tu na uvumilivu kidogo:



- Nenda kwenye [orodha ya Jumuiya ya Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) ya marafiki wazuri
- Chagua nodi na ubofye kiungo cha jina lake, itafungua ukurasa wake wa Amboss
- Bofya ili kuonyesha msimbo wa QR wa nodi ya URI Address


![Demo Blixt 06](assets/blixt_t06.webp)


Sasa, fungua Blixt na uende kwenye droo ya juu - Njia za Umeme na ubofye kitufe cha "+".


![Demo Blixt 07](assets/blixt_t07.webp)


Sasa, bofya kwenye (A) kamera ili kuchanganua msimbo wa QR kutoka ukurasa wa Amboss na maelezo ya nodi yatajazwa. Ongeza kiasi cha Sats kwa chaneli unayotaka kisha uchague kiwango cha ada kwa tx. Unaweza kuiacha kiotomatiki (B) kwa uthibitisho wa haraka au uirekebishe kwa kutelezesha kitufe. Unaweza pia kubonyeza nambari kwa muda mrefu na kuihariri upendavyo.


Usiweke chini ya 1 sat/vbyte ! Kwa kawaida ni bora [kushauriana na ada za Mempool](https://Mempool.space/) kabla ya kufungua kituo na kuchagua ada inayofaa.


Imefanywa, sasa bonyeza tu kitufe cha "fungua kituo" na usubiri uthibitisho 3, ambao kawaida huchukua dakika 30 (takriban block 1 kila dakika 10).


Baada ya kuthibitishwa, utaona chaneli ikitumika katika sehemu yako ya "Njia za Umeme".


## Hatua ya Pili - Pata Ukwasi zaidi wa Ndani


Sawa kwa hivyo sasa tuna kituo cha LN chenye ukwasi wa OUTBOUND pekee. Hiyo inamaanisha kuwa tunaweza TUMA pekee, bado hatuwezi KUPOKEA Sats zaidi ya LN. Kwa nini? Je, ulisoma miongozo iliyoonyeshwa mwanzoni? Hapana? Rudi na uzisome. Ni muhimu sana kuelewa jinsi njia za LN zinavyofanya kazi.


![Demo Blixt 08](assets/blixt_t08.webp)


Kama unavyoona katika mfano huu, chaneli hufunguliwa kwa amana ya kwanza, usiwe na ukwasi mwingi wa INBOUND (“Inaweza kupokea”) lakini uwe na ukwasi mwingi OUTBOUND (“Inaweza kutuma”).


Kwa hivyo ni chaguo gani unazo, ikiwa unataka kupokea zaidi Sats juu ya LN?



- Tumia kiasi cha Sats kutoka kwa chaneli iliyopo. Ndiyo, LN ni mtandao wa malipo wa Bitcoin, unaotumiwa hasa kutumia Sats yako kwa haraka, kwa bei nafuu, kwa faragha na kwa urahisi. LN SI njia ya kushikia, kwa kuwa unayo onchain Wallet.
- Badilisha Sats, urudi kwenye onchain Wallet yako, ukitumia huduma ya kubadilishana nyambizi. Kwa njia hii hautumii Sats yako, lakini unairudisha kwa onchain yako mwenyewe Wallet. Hapa unaweza kuona kwa undani baadhi ya mbinu, katika [Ukurasa wa Miongozo ya Blixt](https://blixtwallet.github.io/guides).
- Fungua kituo cha INBOUND kutoka kwa mtoa huduma yeyote wa LSP. Hili hapa ni onyesho la video kuhusu [jinsi ya kutumia LNBig LSP kufungua kituo kinachoingia](https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). Hiyo inamaanisha, utalipa ada ndogo kwa chaneli TUPU (upande wako) na utaweza kupokea Sats zaidi kwenye chaneli hiyo. Ikiwa wewe ni mfanyabiashara anayepokea zaidi ya matumizi, hilo ni chaguo nzuri. Pia ikiwa unanunua Sats zaidi ya LN, kwa kutumia Robosati au LN Exchange nyingine yoyote.
- Fungua chaneli ya Dunder, iliyo na nodi ya Blixt au mtoaji wowote wa Dunder LSP. Kituo cha Dunder ni njia rahisi ya kupata ukwasi wa INBOUND, lakini wakati huo huo unaweka kiasi cha Sats kwenye chaneli hiyo. Pia ni nzuri kwa sababu itafungua kituo kwa kutumia [UTXO](https://en.Bitcoin.it/wiki/UTXO) ambayo haitoki kwenye Blixt Wallet yako. Hiyo inaongeza faragha.

Pia ni nzuri kwa sababu, ikiwa huna Sats kwenye onchain Wallet, ili kufungua chaneli ya kawaida ya LN, lakini unayo kwenye LN Wallet nyingine, unaweza tu kulipa kutoka kwa hiyo Wallet nyingine kupitia LN ufunguzi na amana (upande wako) ya kituo hicho cha Dunder. [Maelezo zaidi jinsi Dunder inavyofanya kazi na jinsi ya kuendesha seva yako mwenyewe hapa.](https://github.com/hsjoberg/dunder-lsp)


![Demo Blixt 09](assets/blixt_t09.webp)


Hapa kuna hatua za kuwezesha kufungua kituo cha Dunder:



- Nenda kwa Mipangilio, katika sehemu ya "Majaribio" washa kisanduku cha "Wezesha Dunder LSP".
- Mara baada ya kufanya hivyo, nenda nyuma hadi sehemu ya "Lightning Network" na utaona kwamba ilionekana chaguo "Weka Dunder LSP Server". Huko, kwa chaguo-msingi imewekwa "https://dunder.blixtwallet.com" lakini unaweza kuibadilisha na mtoa huduma mwingine yeyote wa Dunder LSP Address. [Hii hapa ni orodha ya jumuiya ya Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) yenye nodi zinazoweza kutoa chaneli za Dudner LSP kwa Blixt yako.
- Sasa unaweza kwenda kwenye skrini kuu na ubonyeze kitufe cha "Pokea". Kisha fuata utaratibu huu ulioelezewa [katika mwongozo huu]( https://blixtwallet.github.io/guides#guide-lsp).


Sawa, kwa hivyo baada ya chaneli ya Dunder kuthibitishwa (itachukua dakika chache) utaishia na kuwa na chaneli 2 za LN: moja ilifunguliwa mwanzoni kwa majaribio ya kiotomatiki (kituo A) na moja ikiwa na ukwasi zaidi wa ndani, iliyofunguliwa na Dunder (kituo B).


![Demo Blixt 10](assets/blixt_t10.webp)


Vizuri, sasa wewe ni vizuri kwenda, kutuma na kupokea Sats ya kutosha juu ya LN !


## Hatua ya Tatu - Rejesha Utaratibu wa Nodi


Kwa hiyo sasa hebu tujadili jinsi ya kurejesha Blixt Wallet au node nyingine yoyote ya LND iliyoanguka. Hili ni la kiufundi zaidi, lakini tafadhali zingatia. Sio hiyo Hard.


**Kikumbusho:** hapo awali niliandika mwongozo mahususi wenye chaguo nyingi [jinsi ya kurejesha nodi ya LND iliyoharibika](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), ambapo nilitaja pia mbinu ya kutumia Blixt kama mchakato wa kurejesha haraka, kwa kutumia faili yako ya GW.4-deadup1. Pia niliandika mwongozo jinsi ya kurejesha nodi yako ya Blixt au kuhamisha Blixt yako hadi kifaa kingine, [hapa](https://blixtwallet.github.io/faq#blixt-restore).


![Demo Blixt 11](assets/blixt_t11.webp)


Lakini hebu tueleze kwa hatua rahisi mchakato huu. Kama unavyoona kwenye picha hapo juu, kuna mambo 2 unapaswa kufanya ili kurejesha nodi yako ya awali ya Blixt/LND:



- kisanduku cha juu ni pale inabidi ujaze maneno yote 24 kutoka kwa seed yako (nodi ya zamani / iliyokufa)
- chini kuna chaguo mbili za vitufe vya kuingiza / kupakia faili ya chelezo cha channel., iliyohifadhiwa hapo awali kutoka kwa nodi yako ya zamani ya Blixt/LND. Inaweza kutoka kwa faili ya ndani (unaipakia kwenye kifaa chako hapo awali) au inaweza kutoka kwa Hifadhi ya Google / eneo la mbali la iCloud. Blixt wana chaguo hili la kuhifadhi nakala rudufu ya vituo vyako moja kwa moja kwenye hifadhi ya Google / iCloud. Angalia maelezo zaidi katika [Ukurasa wa Vipengele vya Blixt](https://blixtwallet.github.io/features#blixt-options).


Hata hivyo, kutaja, ikiwa hapo awali hukuwa na chaneli zozote za LN zilizofunguliwa, hakuna haja ya kupakia faili yoyote ya chelezo cha channels. Ingiza tu maneno 24 seed na ubonyeze kitufe cha kurejesha.


Usisahau kuamilisha Tor, kutoka kwenye menyu ya vitone 3 vya juu, kama tulivyoelezea katika sura ya "Hatua ya Kwanza" ya mwongozo huu. Ndivyo ilivyokuwa wakati ulikuwa na Tor TU na hukuweza kuwasiliana naye kupitia clearnet (kikoa/IP). Vinginevyo sio lazima.


Kipengele kingine muhimu ni kuweka nodi maalum ya Bitcoin kutoka kwenye orodha hiyo ya juu. Kwa chaguo-msingi inasawazisha vizuizi kutoka node.blixtwallet.com (modi ya neutrino) lakini unaweza kuweka nodi nyingine yoyote ya Bitcoin ambayo hutoa usawazishaji wa neutrino.


Kwa hivyo mara tu unapojaza chaguo hizo, na kugonga kitufe cha kurejesha, Blixt itaanza kwanza kusawazisha vizuizi kupitia Neutrino kama tulivyoelezea katika sura ya "Hatua ya Kwanza" ya mwongozo huu. Kwa hivyo kuwa na subira na uangalie mchakato wa kurejesha kwenye skrini kuu, kwa kubofya kwenye ikoni ya kusawazisha.


![Demo Blixt 12](assets/blixt_t12.webp)


Kama unavyoona katika mfano huu, inaonyesha kuwa vizuizi vya Bitcoin vimesawazishwa kwa 100% (A) na mchakato wa kurejesha uko kwenye kozi (B). Hiyo inamaanisha kuwa chaneli za LN uliokuwa nazo hapo awali, zitafungwa na pesa zitarejeshwa kwenye Blixt onchain Wallet yako.


Utaratibu huu unachukua muda! Kwa hivyo tafadhali, kuwa na subira na ujaribu kuweka Blixt yako hai na mtandaoni. Usawazishaji wa awali unaweza kuchukua hadi dakika 6-8 na vituo vya kufunga vinaweza kuchukua hadi dakika 10-15. Kwa hivyo ni bora kuwa na kifaa chaji vizuri.


Mara tu mchakato huu unapoanza, unaweza kuangalia katika Droo ya Kiajabu - Vituo vya Umeme, hali ya kila moja ya chaneli zako za awali, zinazoonyesha kuwa ziko katika hali ya "inasubiri kufungwa". Mara tu kila kituo kinapofungwa, unaweza kuona tx ya kufunga kwenye onchain Wallet (ona Magic Drawer - Onchain), na ufungue logi ya menyu ya tx.


![Demo Blixt 13](assets/blixt_t13.webp)


Pia itakuwa vizuri kuangalia na kuongeza kama hawapo, wenzako wa awali uliokuwa nao katika nodi yako ya zamani ya LN. Kwa hivyo nenda kwenye menyu ya Mipangilio, chini hadi "Lightning Network" na uweke chaguo "Onyesha Wenzake wa Umeme".


![Demo Blixt 14](assets/blixt_t14.webp)


Ndani ya sehemu hiyo utaona wenzako ambao umeunganishwa kwa wakati huo na unaweza kuongeza zaidi, bora kuongeza zile ulizokuwa nazo hapo awali. Nenda tu kwenye ukurasa wa Amboss, tafuta lakabu za nodi rika au nodi ID na uchanganue URI ya nodi zao.


![Demo Blixt 15](assets/blixt_t15.webp)


Kama unavyoweza kwenye picha hapo juu, kuna mambo 3:


A - inawakilisha nodi ya clearnet Address URI (kikoa/IP)


B - inawakilisha nodi ya kitunguu cha Tor Address URI (.onion)


C - ni msimbo wa QR wa kuchanganua kwa kutumia kamera yako ya Blixt au kitufe cha kunakili.


Njia hii ya Address URI lazima uiongeze kwenye orodha ya programu zingine. Kwa hivyo fahamu haitoshi tu nodi alias jina au nodeID.


Sasa unaweza kwenda kwenye Droo ya Kichawi (menyu ya juu kushoto) - Njia za Umeme, na unaweza kuona ni urefu gani wa kizuizi cha ukomavu pesa zitarejeshwa kwenye onchain yako Address.


![Demo Blixt 16](assets/blixt_t16.webp)


Nambari hiyo ya kizuizi 764272 ndipo pesa zitatumika katika Bitcoin onchain yako Address. Na inaweza kuchukua hadi vitalu 144 kutoka kwa kizuizi cha 1 hadi vitakapotolewa. Kwa hivyo angalia hiyo katika [Mempool](https://Mempool.space/).


Na ndivyo hivyo. Subiri tu kwa subira hadi vituo vyote vifungwe na pesa zirudishwe kwenye onchain yako Wallet.


## Hatua ya Nne - Kubinafsisha


Sura hii inahusu ubinafsishaji na ujue vizuri zaidi Njia ya Blixt. Sitaeleza vipengele vyote vinavyopatikana, ni vingi sana na tayari vilielezwa katika [Ukurasa wa Vipengele vya Blixt](https://blixtwallet.github.io/features).


Lakini nitaonyesha baadhi ya zile muhimu kwenda mbele kwa kutumia Blixt yako na uwe na uzoefu mzuri.


### A - Jina (NameDesc)


![Demo Blixt 17](assets/blixt_t17.webp)


[The NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) ni kanuni ya kuwasilisha "jina la mpokeaji" katika ankara za BOLT11.


Hili linaweza kuwa jina lolote na linaweza kubadilishwa wakati wowote.


Chaguo hili ni muhimu sana katika hali mbalimbali, unapotaka kutuma jina pamoja na maelezo ya Invoice, ili mpokeaji apate kidokezo kutoka kwa nani alipokea hizo Sats. Hili ni la hiari kabisa na pia katika skrini ya malipo, mtumiaji anatakiwa kutia alama kwenye kisanduku kinachoonyesha kutuma jina la utani.


Huu hapa ni mfano wa jinsi unavyoweza kuonekana unapotumia [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![Demo Blixt 18](assets/blixt_t18.webp)


Huu ni mfano mwingine unaotuma kwa programu nyingine ya Wallet inayotumia NameDesc:


![Demo Blixt 19](assets/blixt_t19.webp)


### B - Cheleza Njia za LN na maneno ya seed


Hiki ni kipengele muhimu sana!


Baada ya kufungua au kufunga chaneli ya LN unapaswa kufanya nakala rudufu. Inaweza kufanywa kwa mikono kuhifadhi faili ndogo kwenye kifaa cha ndani (folda ya kupakua kawaida) au kutumia Hifadhi ya Google au akaunti ya iCloud.


![Demo Blixt 20](assets/blixt_t20.webp)


Nenda kwa Mipangilio ya Blixt - sehemu ya Wallet. Hapo unayo chaguzi za kuhifadhi data zote muhimu kwa Blixt Wallet yako:



- "Onyesha Mnemonic" - itaonyesha maneno 24 seed ili kuyaandika
- "Ondoa Mnemonic kwenye kifaa" - hii ni hiari na uitumie tu ikiwa unataka kuondoa maneno ya seed kwenye kifaa chako. Hii HAITAfuta Wallet yako, seed pekee. Lakini fahamu! Hakuna njia ya kuzirejesha ikiwa hukuziandika kwanza.
- "Hamisha nakala rudufu ya kituo" - chaguo hili litahifadhi faili ndogo kwenye kifaa chako cha ndani, kwa kawaida kwenye folda ya "vipakuliwa", kutoka ambapo unaweza kuichukua na kuihamisha nje ya kifaa chako, kwa uhifadhi salama.
- "Thibitisha nakala rudufu ya kituo" - hii ni chaguo nzuri ikiwa unatumia Hifadhi ya Google au iCloud kuangalia uadilifu wa nakala rudufu iliyofanywa kwa mbali.
- "Nakala ya nakala ya kituo cha hifadhi ya Google" - itahifadhi faili ya chelezo kwenye hifadhi yako ya kibinafsi ya Google. Faili imesimbwa kwa njia fiche na kuhifadhiwa katika hifadhi tofauti kuliko faili zako za kawaida za google. Kwa hivyo hakuna wasiwasi ambao unaweza kusomwa na mtu yeyote. Kwa vyovyote vile faili hiyo haina maana kabisa bila maneno ya seed, kwa hivyo hakuna mtu anayeweza kuchukua pesa zako kutoka kwa faili hiyo pekee.


Ningependekeza kwa sehemu hii yafuatayo:



- tumia kidhibiti cha nenosiri ili kuhifadhi salama seed yako na faili chelezo. [KeePass](https://keepass.info/) au Bitwarden ni nzuri sana kwa hilo na inaweza kutumika kwenye majukwaa mengi na mwenyeji binafsi au nje ya mtandao.
- FANYA HUDUMA KILA WAKATI unapofungua au kufunga kituo. Faili hiyo inasasishwa na maelezo ya vituo. Hakuna haja ya kuifanya baada ya kila shughuli uliyofanya kwenye LN. Hifadhi rudufu ya kituo haihifadhi maelezo hayo, inahifadhi hali ya kituo pekee.


![Demo Blixt 21](assets/blixt_t21.webp)


## Hitimisho


Sawa, kuna vipengele vingine vingi vya kushangaza ambavyo Blixt hutoa, nitakuruhusu uvigundue kimoja baada ya kingine na ufurahie.


Programu hii haithaminiwi sana, hasa kwa sababu haiungwi mkono na ufadhili wowote wa VCs, inaendeshwa na jumuiya, jenga kwa upendo na shauku kwa Bitcoin na Lightning Network.


Node hii ya simu ya LN, Blixt ni chombo chenye nguvu sana mikononi mwa watumiaji wengi, ikiwa wanajua jinsi ya kuitumia vizuri. Hebu fikiria, unatembea duniani kote na nodi ya LN mfukoni mwako na hakuna mtu atakayeijua.


Na bila kuzungumza juu ya vipengele vingine vyote vya tajiri vinavyokuja, ambavyo ni programu chache sana au hakuna programu zingine za Wallet zinaweza kutoa.


Natumai unafurahiya kuitumia. Binafsi, ninaipenda na ni muhimu sana kwangu (tazama hapa kesi ya utumiaji ambapo hii Wallet ni zana nzuri).


HERI YA Bitcoin UMEME!


Naomba ₿ITCOIN Iwe Nawe!


**Kanusho:** Silipwi wala kuungwa mkono kwa njia yoyote na wasanidi programu hii. Niliandika mwongozo huu kwa sababu niliona kuwa nia ya programu hii ya Wallet inaongezeka na watumiaji wapya bado hawaelewi jinsi ya kuanza nayo. Pia kusaidia Hampus (dev kuu) na nyaraka kuhusu kutumia nodi hii Wallet. Sina nia nyingine yoyote ya kutangaza programu hii ya LN, zaidi ya kusukuma mbele matumizi ya Bitcoin na LN. Hii ndiyo njia pekee!