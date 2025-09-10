---
name: Coin Control
description: Anza kutumia Coin Control, chombo muhimu cha kulinda faragha yako kwenye Bitcoin
---
![cover](assets/cover.webp)


*Mafunzo haya yameingizwa kutoka [somo la Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Utangulizi



Uthabiti wa itifaki ya Bitcoin unahakikishwa na dhana kuu rahisi. Miongoni mwa hizi, uwazi unajitokeza: miamala yote ya Bitcoin ni ya umma na inaweza kuthibitishwa kwa urahisi na mtu yeyote. Ingawa kipengele hiki ni msingi wa itifaki, kwa kuwa kinazuia udanganyifu na kuhakikisha uhalisi wa fedha, pia kinaweza kuwakilisha changamoto kwa usiri. **Je, umewahi kujiuliza kama uwazi mkubwa namna hii unaweza kudhuru faragha yako?**



Unapaswa. Ingawa kukusanya Satoshi isiyo ya kyc ni rahisi sana, faragha yako iko hatarini zaidi katika hatua ya matumizi.



### Nini kinatokea unapotumia UTXO



Kutumia Bitcoin sio tu kuhamisha thamani kwa mtu mwingine.



Kwa kutumia moja ya UTXO zako, lazima utimize masharti yaliyowekwa kwa uwazi wa itifaki, kwa sababu una wajibu wa kuthibitisha kuwa unamiliki fedha hizo. Kwa hivyo unajifanya kuwajibika kwa:




- onyesha ufunguo wako wa umma;
- toa saini ya kidijitali.



Kwa hivyo wakati wa matumizi ndio muhimu zaidi: **kutumia Bitcoin ni kitendo cha kufanywa kwa uangalifu na kwa udhibiti mwingi iwezekanavyo**.



## Udhibiti wa Coin



Katika itifaki ya Bitcoin, vipengee kama vile _account_ au _monetary units_ havipo. Wazo la UTXO limeelezewa vyema katika kozi ifuatayo, ambayo ninapendekeza sana:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Ukiwa na Bitcoin unachokusanya na kutumia baadaye ni vitengo vidogo au vikubwa vya akaunti vinavyopimwa katika Satoshi, vinavyowakilishwa na `matokeo ya miamala ambayo hayajatumika`, **UTXO**, pia huitwa `sarafu`. Unapotumia UTXO kuunda shughuli, zinaharibiwa kabisa na UTXO zingine huundwa mahali pao.



Programu Pochi hutengenezwa ili kufanya chaguo hili kiotomatiki, kwa kutumia sarafu "nasibu" zilizochaguliwa, kupitisha algorithms fulani iliyotolewa na itifaki. Kigezo pekee ambacho algoriti hizi hukutana, ni kufidia kiasi kinachohitajika kwa matumizi.



Zinaweza kuchanganya pamoja UTXO za rika tofauti, au kupendelea matumizi mapya zaidi au "zamani zaidi," kulingana na kanuni iliyochaguliwa na wasanidi programu. Pochi bora za Programu, pia zinapanga kumwacha mtumiaji chaguo muhimu.



Mwongozo wa `Coin Control`, ambao unaweza pia kupata unajulikana kama `Coin Selection`, ni kipengele cha baadhi ya Programu za Pochi ambacho hukuruhusu **kuchagua mwenyewe UTXO za kutumia unapounda muamala wako**.



Tuseme tuna Wallet yenye UTXO 3 za 21,000, 42,000 na 63,000 Satoshi, mtawalia.



![img](assets/en/01.webp)



Iwapo itabidi utumie 24,000 Sats na kuruhusu algoriti ifanye uteuzi wa kiotomatiki, Software Wallet nzuri inaweza kuchagua kuchanganya UTXO 1 + UTXO 2 ili kulipa ada za 24k Sats na Miner, na kuunda salio ambalo linarudi kwenye Address ya ndani ya Wallet inayoanza.



![img](assets/en/02.webp)



Baada ya shughuli, hali mpya katika Wallet, kuhesabu UTXO pekee, inaweza kufupishwa kama ifuatavyo.



![img](assets/en/03.webp)



Kwa programu sahihi na ufahamu wako, hata hivyo, ungeweza kufanya tofauti, kwa njia fulani chaguo sahihi zaidi. Kwa mfano, kwa kuchagua tu UTXO2 (kutoka 42,000 Sats).



![img](assets/en/04.webp)



Na hali ya mwisho katika Wallet yako, katika kiwango cha UTXO, ambayo inaonekana tofauti na hapo awali.



![img](assets/en/05.webp)



## Kwa nini coin control ya mikono?



![img](assets/en/06.webp)



Katika mifano miwili hapo juu, salio ni sawa `108,280 Sats`. Baada ya kutumia 24,000 Sats, bila uteuzi wa mwongozo tungekuwa na 2 UTXO katika Wallet; na udhibiti wa mwongozo wa Coin tuna 3 jumla.



Swali tunaloweza kujiuliza ni hili: **kwa nini tufanye yote haya?** Kuna, au kunaweza kuwa, sababu kadhaa kwa nini hatukutumia `UTXO1` **na zote ndizo msingi wa kwa nini—wakati wa kutumia—kuwasha coin control ya mikono ni moja ya mbinu bora za kufuata**.



Kuchagua UTXO hukuruhusu kupendelea vipengele vingine kuliko vingine. Chaguo kweli inategemea malengo unayotaka kufikia.



### Faragha



Moja ya faida kuu, linapokuja suala la udhibiti wa Coin, ni **faragha kubwa zaidi kwa mtumia pesa**. Wacha tuchukue mfano wetu kila wakati: matumizi ya 24,000 Satoshi _bila uteuzi wa mwongozo wa Coin_. Kwa kuwa Blockchain ya Bitcoin ni rekodi ya umma, mwangalizi wa nje anaweza kutangaza, bila kivuli cha shaka, kwamba pembejeo `UTXO1 ya 21,000 Sats` na `UTXO2 ya 42,000 Sats`, pamoja na nyinginezo, `UTXO5 kutoka 38,3*3 ni mali ya mtumiaji sawa **Sats`.



Kwa kuchagua mwenyewe `UTXO2`, kwa upande mwingine, `UTXO1` inasalia kuhifadhiwa kabisa, ikiwa imekaa katika seti ya UTXO ikisubiri kutumiwa kwa wakati ufaao zaidi.



`UTXO1` inaweza kutoka kwa chanzo cha KYC, kama vile malipo yanayopokelewa katika Exchange ya bidhaa na huduma, huku UTXO zingine hazifanyi hivyo. Kuchanganya UTXO-kyc na zingine ambazo ni za siri zaidi kunahatarisha seti ya kutokujulikana ya pesa zisizo za kyc.



**Fedha za KYC zingepelekea bila shaka kutambua utambulisho wa mlipaji. Ikiwa hiyo ingekuwa wallet yako, je, ungependa mtazamaji wa nje aweze kutambua utambulisho wako kwa uhakika wa kiwango hicho cha juu?**



Jaribu basi kuzingatia kwamba Pochi zinazotumia uteuzi wa mwongozo wa UTXO, kwa mfano, huruhusu **kutenganisha UTXO moja au zaidi**, chaguo la kukokotoa la kutumika wakati hali kama hizi zinatokea.



Ingawa nina hakika kwamba pesa za KYC zinapaswa kuwekwa katika Wallet tofauti na Bitcoin iliyonunuliwa bila kyc, ikiwa hii ndiyo kesi yako kutenganisha baadhi ya anwani zako ni usaidizi muhimu, ambao unaweza kunufaika nao kwa kujifunza kuchagua mwenyewe pembejeo za matumizi.



### Kuokoa kwa ada



Kuchagua UTXO sahihi ili kufanya matumizi, **huruhusu uboreshaji wa ada**. Tena kuanzia mfano wetu wa awali, Software Wallet ilichagua UTXO mbili ili kufidia gharama itakayofanywa. UTXO mbili zinamaanisha saini mbili za kuonyeshwa kwa mtandao. Inafuata kwamba shughuli ina "uzito" mkubwa zaidi katika suala la vBytes.



Kutumia udhibiti wa mwongozo wa Coin, kwa upande mwingine, unaweza kuchagua moja tu ambayo ni ya kutosha kufunika kiasi, kuokoa ada kwa kupunguza "uzito" wa shughuli.



Katika nyakati ambazo ada ni kubwa, lakini unalazimika kutumia Bitcoin On-Chain (kwa mfano, kufungua kituo cha Lightning Network), hapo ndipo udhibiti wa Coin unageuka kuwa motisha sahihi ya kiuchumi ya kurejea.



### Mkusanyiko wa mabaki



Unapofanya malipo na kutumia Bitcoin On-Chain, uwezekano wa kupokea mabadiliko karibu daima huwa uhakika. Kila salio yenyewe ni upotezaji mdogo wa faragha, kwani hufichulia mtandao (na hasa kwa mpokeaji wa malipo) Address yako ambayo inaweza kuhusishwa na mchango wako wa chanzo.



Kwa kuzingatia kwamba Wallet HDs generate anwani maalum kwa mabaki, unaweza kuzitambua kwa urahisi na "kutenganisha" mabaki yote ya shughuli mbalimbali zilizofanywa; zikiwa zimefikia kiasi fulani unaweza kuzichagua wewe mwenyewe na kuziunganisha, au ubadilishe hadi Lightning Network (njia ninayopendelea) na kuzichakata ili kurejesha faragha iliyopotea katika matumizi.



### Matumizi kutoka kwa Cold Wallet



Cold Wallet ni chombo ambacho mtu anaweza kupata kiwango kizuri cha usalama, kuhifadhi kiasi chochote cha fedha kuweka kando kwa muda mrefu. Walakini, matukio yasiyotarajiwa yanaweza kutokea, kwa hivyo hitaji linatokea ili kupata mkono juu ya akiba na kukidhi gharama zisizotarajiwa.



Sijui ni wangapi wanaweza kushiriki mbinu yangu, lakini ushauri wangu ni **usiwahi kufanya matumizi moja kwa moja kutoka kwa Cold Wallet, ili kuepuka kupokea mabadiliko kati ya anwani za sawa**. Jifunze kuchagua mwenyewe UTXO zinazohitajika ili kulipia gharama, zihamishe hadi Wallet Hot na uandae muamala wako kutoka kwa za mwisho. Mabadiliko yoyote, basi, unaweza kuirejesha kwa Cold Wallet Address (kama kiasi kinatosha), itumie kwa gharama zingine, au bado itenge kama tulivyoona.



## Uwasilishaji wa vitendo


Baada ya utangulizi wa kiufundi wa `kwanini`, wacha tuone jinsi ya kutekeleza udhibiti wa mwongozo wa Coin ukitumia programu tofauti, kompyuta ya mezani na ya simu. Tutatumia Wallet BIP39 sawa kila wakati, iliyoingizwa katika kila zana iliyochaguliwa, ili kukuonyesha tofauti ndogo kati yao.



## Eneo-kazi la Wallet



### Sparrow



Ikiwa unatumia Sparrow, fungua Wallet yako na uchague _UTXOs_ kutoka kwenye menyu iliyo upande wa kushoto. Utaona orodha ya UTXO zote zinazohusiana na Wallet yako.



Bofya tu na kipanya kwenye mojawapo yao kisha uchague _Send Selected_. Sparrow pia hukuonyesha jumla inayopatikana ya matumizi baada ya uteuzi, karibu kabisa na amri. Sparrow inakuonyesha UTXO iliyochaguliwa kwa kuiangazia kwa rangi ya samawati.



![img](assets/en/07.webp)



Unaweza pia kuchagua zaidi ya moja. Jisaidie na kitufe cha _CTRL_ ili kuchagua UTXO zisizo karibu kwenye orodha.



![img](assets/en/08.webp)



Baada ya kuchagua UTXO kwa mikono, unaweza kuanza kuunda muamala, na Sparrow itakuonyesha vizuri, kielelezo, jinsi inavyoundwa.



![img](assets/en/09.webp)



#### Mgawanyiko wa UTXO



Kutenganisha fedha kunamaanisha "kuzifungia" ndani ya Wallet ili zisitumike kama mchango wa muamala. Sparrow inaruhusu utendakazi huu, ambao daima hupatikana kutoka kwa menyu ya _UTXOs_: unaweka kipanya juu ya UTXO ili "imefungwa" na ubofye kitufe cha kulia cha mouse. Miongoni mwa vipengele vya utaratibu huu itaonekana _Freeze UTXO_. Hivi ndivyo utaweza kutenganisha Sarafu na pochi za Sparrow.



![img](assets/en/29.webp)



### Electrum



Ikiwa eneo-kazi lako la Wallet ni Electrum, unapaswa kujua kwamba unaweza kuchagua UTXO wewe mwenyewe kutoka kwenye menyu ya _Addresses_ au kutoka kwenye menyu ya _Coins_. Katika menyu zote mbili, uteuzi unafanywa kwa kuelekeza kipanya kwenye UTXO inayotakiwa na kuchagua _Ongeza kwa Coin control_ baada ya kubofya kulia.



![img](assets/en/10.webp)



Hata ukiwa na programu hii unaweza kuchagua zaidi ya UTXO moja, ukisaidia na kitufe cha _CTRL_ kwenye kibodi yako ikiwa haziko karibu.



![img](assets/en/11.webp)



Graphically Electrum itakuonyesha uteuzi kwa kuonyesha UTXOs zilizochaguliwa katika Green, wakati bar inaonekana chini, iliyoonyeshwa kwa rangi sawa, kuonyesha usawa unaopatikana baada ya udhibiti wa Coin.



![img](assets/en/12.webp)



Mara tu ukichagua pato, au matokeo, unaweza kuunda muamala wako kama kawaida kutoka kwa menyu ya _Send_.



#### Mgawanyiko wa UTXO



Electrum hutoa utendakazi huu kwa kwenda kwenye menyu ya _Coins_, ambapo utaenda kuchagua UTXO fulani na kisha kuchagua _Freeze_ kwa kubofya kulia. Unaweza "kufungia" Address hata bila pesa kutoka kwa menyu ya _Addresses, au "Coin" ili usiitumie.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk hukuruhusu kuchagua UTXO mwenyewe kutoka kwa menyu kuu mara inapofunguliwa. Zindua Nunchuk na ubofye _Tazama sarafu_.



![img](assets/en/13.webp)



Hii inafungua dirisha ambalo lina UTXO zote kwenye Wallet yako, ambapo unaweza kuchagua moja au zaidi kwa kuamilisha alama ya tiki karibu na kila kiasi. Baada ya kufanya uteuzi wako, endelea na _Create transaction_.



![img](assets/en/14.webp)



Baada ya hapo unaweza kuingia Address lengwa na kuweka kiasi na ada.



![img](assets/en/15.webp)



#### Mgawanyiko wa UTXO



Kwa ajili ya ukamilifu, Nunchuk pia inaruhusu kati ya vipengele vyake, kutenganisha UTXO moja (au zaidi) na hufanya hivyo kwa njia mbili tofauti. Fikia menyu ya _Tazama sarafu_ na uchague mwenyewe kutoka kwa orodha ya sarafu. Kisha ubofye menyu ya _More_ chini kulia: orodha ya chaguo itaonekana, ambayo unaweza kuchagua _Funga sarafu_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Unaweza pia kubofya katika nafasi iliyohifadhiwa kwa ajili ya UTXO, ili kufikia kidirisha cha _Coin details. Hapa amri ya kufunga/kufungua UTXO inayohusika inaonekana kwenye kona ya juu kulia.



![img](assets/en/41.webp)



### Programu ya kuzuia mkondo



Kompyuta ya mezani ya Blockstream App, ambayo hapo awali ilijulikana kama Green, inakuruhusu kuchagua Coin wakati tayari umeanza kufanya muamala. Kwa hivyo, fungua Wallet yako na ubofye _Send_.



![img](assets/en/16.webp)



Bandika fikio la Address kwenye sehemu inayofaa kisha uchague _Mwongozo wa Coin uteuzi_.



![img](assets/en/17.webp)



Hii itafungua dirisha ambapo unaweza kuchagua sarafu moja au zaidi za UTXO. Katika mfano hapa chini, tumechagua sarafu mbili. Baada ya hapo, thibitisha chaguo lako kwa kubofya _Thibitisha Uteuzi wa Coin_.



![img](assets/en/18.webp)



Weka kiasi na ada kisha uendelee kama kawaida na muamala wako.



![img](assets/en/19.webp)



⚠️ N.B. Katika menyu ya _Coins_ ya Green kuna _Funga_/_Fungua_ vitu ambavyo vinaonyesha uwezekano wa kutenganisha UTXO. Kipengele hiki kimeamilishwa tu katika kinachojulikana akaunti za Multisig; pia huwashwa tu kwa kuchagua UTXO ya kiasi kidogo sana, karibu na kizingiti cha `Dust`.



## Wallet ya simu



Pochi pia inaweza kuchaguliwa kutoka kwa rununu, ambayo inaruhusu UTXO kuchaguliwa kwa mikono. Wacha tuone Bluu Wallet kama mfano wa kwanza.



### Bluu Wallet



Ikiwa wewe ni mtumiaji wa Wallet hii, ifungue na ubofye ili kuingiza skrini za udhibiti zinazohusiana na mojawapo ya Wallet zako. Ili kufikia mwongozo wa udhibiti wa Coin lazima uweke awamu ya matumizi, kisha ubofye _Send_.



![img](assets/en/21.webp)



Kwenye skrini inayofuata chagua menyu zilizoonyeshwa na vitone vitatu kwenye kona ya juu kulia. Dirisha la kushuka linafungua na mfululizo wa amri. Chagua ya mwisho: _Coin Control_.



![img](assets/en/22.webp)



Katika hatua hii Bluu Wallet inaonyesha UTXO zako zote. Mbali na kiasi, hutofautishwa graphically na rangi tofauti.



![img](assets/en/27.webp)



Chagua UTXO ili kuchagua kisha chagua _Tumia Coin_.



![img](assets/en/23.webp)



Wallet ya Bluu inakurudisha kwenye dirisha la _Send_ ili kuendelea kutengeneza muamala. Rekebisha kiasi na ada, kisha utachagua _Next_.



![img](assets/en/24.webp)



Katika hatua hii unaweza kumaliza muamala, kama kawaida.



#### Mgawanyiko wa UTXO



Bluu Wallet pia inakuwezesha kutenganisha UTXO, na kuwafanya kutopatikana kwa matumizi ambayo sio kazi mbaya kwa Wallet kutoka kwa simu ya mkononi. Unafikia kidhibiti cha Coin kwa utaratibu uliofafanuliwa hivi punde na, baada ya kuchagua UTXO, chagua _Freeze_ badala ya _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



Toleo la rununu la Nunchuk pia hutoa uwezo kwa mtumiaji kufanya udhibiti wa Coin. Ikiwa unatumia programu hii kutoka kwa simu ya mkononi, ifungue na uende kwenye menyu ya _Wallet_. Kutoka hapo chagua _Tazama sarafu_.



![img](assets/en/30.webp)



Katika dirisha ambapo orodha ya UTXO inaonekana, bofya _Chagua_.



![img](assets/en/38.webp)



Chaguo la kukokotoa linaonekana karibu na kila UTXO. Kama ilivyo katika toleo la eneo-kazi, uteuzi wa mwongozo kwenye simu ya Nunchuk unafanywa kwa kuangalia mraba mdogo karibu na kiasi. Skrini inaonyesha idadi ya UTXO zilizochaguliwa na jumla ya kiasi kinachopatikana. Baada ya kumaliza, bofya ₿ ishara katika kona ya chini kushoto, ambayo ni amri ya kuanza kujenga shughuli.



![img](assets/en/31.webp)



Sasa unaweza kukamilisha muamala, ukichagua kiasi na kubofya _Endelea_.



![img](assets/en/32.webp)



Endelea kama unavyofanya kila mara, kubandika lengwa la Address, maelezo na kubinafsisha mipangilio ya ada.



#### Mgawanyiko wa UTXO



Unaweza pia kutenganisha UTXO na Nunchuk ya rununu. Fikia dirisha la orodha ya sarafu zilizojitolea na uchague kishale karibu na UTXO unayotaka kutenganisha.



![img](assets/en/42.webp)



Utaona nafasi iliyohifadhiwa kwa maelezo ya _Coin_, ambapo unaweza kuchagua _Funga sarafu hii_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper ndio Wallet ya mwisho tutakayoona katika mwongozo huu. Tunaona utendakazi wake ukitumika kwa udhibiti wa Coin kwa kutumia sig moja ya Wallet, ingawa matumizi kama hayo si madhumuni ya programu hii mahususi. Baada ya kusanidi Kilinda kwenye simu yako, izindua na ufungue Wallet iliyo na pesa. Katikati ya skrini kuu bofya _Tazama Sarafu Zote_.



![img](assets/en/34.webp)



Askari anaonyesha muhtasari wa UTXOs. Ili kufikia skrini ya uteuzi bofya _Chagua Ili Kutuma_.



![img](assets/en/35.webp)



Unaweza kuchagua sarafu kwa kuziangalia kwa kubofya amri inayofaa. Ukimaliza, bofya _Send_.



![img](assets/en/36.webp)



Bitcoin Keeper inakupeleka moja kwa moja hadi kwenye menyu ya _Send_, ambapo unaweza kutengeneza muamala kwa kutumia UTXO zilizochaguliwa.



![img](assets/en/37.webp)



## Hardware Wallet



Kila programu ya Pochi inayoonekana katika mwongozo huu inaweza kuwa Interface ya saa pekee kwa mojawapo ya Wallet zako za Maunzi. Inamaanisha kuwa kidhibiti cha Coin cha kifaa cha kuambatisha cheti nje ya mtandao kinatekelezwa kwa hatua zinazoonekana kufikia sasa.



### Mapendekezo ya jumla



Udhibiti wa Coin ni mazoezi madhubuti sana ya kuchagua ingizo lako la muamala. Uteuzi wa mtu mwenyewe ni mzuri zaidi ikiwa, unaponunua/kupokea pesa zako, umeweka lebo ya chanzo cha Satoshi yako vizuri. Ikiwa ungependa kujifunza mbinu hii vizuri, napendekeza mafunzo yafuatayo:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Tumezungumza hapo awali kuhusu `kutenganisha mabaki`. Iwapo ungependa kufunga masalio kwa ajili ya kuchakatwa baadaye na kurejesha faragha (badilisha kwa Layer 2), ni lazima uangalie `kuwekea lebo` kila mara unapopokea. Kati ya Programu za Wallet zinazoonekana kufikia sasa, ni Electrum pekee inayopakwa rangi mabaki ya UTXO ili kuzifanya zionekane mara moja tu. Nyingine, kama vile Sparrow, hukuonyesha mnyororo katika njia ya utokezi wa UTXO mahususi (`m/84'/0'/0'/1/11`).



Ili kutumia mbinu hii kwa ufanisi, kumbuka kila wakati kuongeza maelezo kuhusu mabadiliko unayopokea: mtu uliyemtumia pesa zako (malipo, mafunzo, au nyinginezo), anajua Address inayohusishwa na mabadiliko hayo na anajua kuwa ni yako, kwa kuwa inatoka kwa muamala mliofanya pamoja!