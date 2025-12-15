---
name: Seedkeeper x SeedSigner
description: Je, ninawezaje kutumia Mtunza mbegu kwa SeedSigner yangu?
---

![cover](assets/cover.webp)



*Shukrani kwa timu ya [Satochip](https://satochip.io/) kwa kukubali kutumia tena [video zao](https://www.youtube.com/@satochip/videos) katika mafunzo haya. Shukrani pia kwa [Mwongozo wa Crypto](https://www.youtube.com/@CryptoGuide/) kwa fork yake ya programu dhibiti ya SeedSigner, kuwezesha usaidizi wa smartcards



---

SeedSigner ni maunzi ya wallet ambayo unajikusanya kutoka kwa maunzi ya kawaida, kwa kawaida karibu na Raspberry Pi Zero. wallet hii inaitwa "*stateless*": tofauti na miundo mingine mingi kwenye soko (Coldcard, Trezor, Ledger, n.k.), haihifadhi data yoyote kwenye kumbukumbu ya kudumu, na inafanya kazi moja kwa moja kutoka kwa RAM. Kwa hivyo, seed ya kwingineko yako haihifadhiwi kwenye SeedSigner. Kila wakati unapowasha upya, utahitaji kuijaza ili kuwezesha kifaa kutia sahihi katika miamala yako. Njia ya kawaida ni kuhifadhi seed yako kama msimbo wa QR, ambayo unachanganua kila wakati unapoitumia (*SeedQR*).



Mbinu hii, hata hivyo, inatoa hatari kubwa: seed lazima ibaki kupatikana kwa maandishi wazi ili iweze kuchanganuliwa. Katika tukio la wizi au uvamizi, mshambulizi anaweza kuikamata kwa urahisi na kuiba bitcoins zako.



Ili kuondokana na udhaifu huu, SeedSigner inaweza kuunganishwa na [**Seedkeeper**](https://satochip.io/product/seedkeeper/), kadi mahiri iliyotengenezwa na Satochip. Hii huwezesha misemo ya mnemonic (au siri nyingine) kuhifadhiwa katika secure element inayolindwa na msimbo wa PIN. Appleti ya Mtunza mbegu ni chanzo huria, na secure element yake ina uthibitisho wa EAL6+. Ikitumiwa pamoja na SeedSigner, inatoa kipengele cha usalama kinachovutia sana: funguo zako zitabaki kusimamiwa nje ya mtandao, unatia sahihi miamala yako kwenye skrini inayoaminika, na seed inalindwa kimwili katika smartcard inayostahimili mashambulizi ya kimwili.



Unachohitaji kukamilisha usakinishaji ni vitu vifuatavyo:




- Vifaa vya kawaida vinavyohitajika kwa SeedSigner ya kawaida: Raspberry Pi Zero, skrini ya Waveshare inchi 1.3, kamera inayooana na kadi ya microSD (utapata maelezo zaidi katika mafunzo ya SeedSigner hapa chini);
- SeedSigner extension kit, inapatikana [kwenye duka rasmi la Satochip](https://satochip.io/product/seedsigner-extension-kit/), ambayo hukuwezesha kusoma na kuandika kwa smartcard moja kwa moja kutoka kwa SeedSigner yako. Chaguo jingine ni kutumia kisoma kadi mahiri cha nje, ambacho kinaweza kuunganishwa kwa kebo kwenye bandari ndogo ya USB kwenye Raspberry Pi. Walakini, sijajaribu suluhisho hili mwenyewe;
- Mlinzi wa Mbegu, au pengine kadi mahiri tupu ambayo kwayo unaweza kusakinisha programu-jalizi ya Seedkeeper (kifaa cha upanuzi kinachouzwa na Satochip tayari kinajumuisha smartcard tupu).



![Image](assets/fr/01.webp)



Mafunzo haya yanashughulikia matukio mawili:




- Ikiwa tayari una jalada la Bitcoin linalodhibitiwa kupitia SeedSigner yako, sakinisha programu dhibiti mpya. Kisha unaweza kuendelea kutumia wallet yako iliyopo, wakati huu ukitumia Seedkeeper kwa usalama zaidi.
- Ikiwa bado huna Bitcoin wallet inayohusishwa na SeedSigner yako, utahitaji kufuata hatua **5** na **6** za mafunzo yaliyotajwa hapa chini. Sehemu hizi zinaelezea jinsi ya generate maneno ya kukumbukwa kwa SeedSigner, yahifadhi kupitia *SeedQR*, na kisha kuunganisha hii wallet na Sparrow Wallet ili kuidhibiti. Sitaingia katika taratibu hizi hapa na **Ninachukulia kuwa tayari unayo Bitcoin wallet inayofanya kazi, iliyosanidiwa na Sparrow na SeedSigner yako**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Sakinisha firmware



Ili kutumia SeedSigner yako na Mtunza Mbegu, unahitaji kusakinisha programu mbadala, tofauti na ile ya SeedSigner asili, ili kusaidia usomaji wa kadi mahiri. Kwa hili, [ninapendekeza kutumia fork kutoka "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Pakua [toleo jipya zaidi la picha](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) inayolingana na muundo wa Raspberry Pi unaotumia.



![Image](assets/fr/02.webp)



Ikiwa tayari huna, pakua programu ya [Balena Etcher] (https://etcher.balena.io/), kisha uendelee kama ifuatavyo:




- Ingiza kadi ya microSD kwenye kompyuta yako;
- Uzinduzi Etcher;
- Chagua faili ya `.zip` ambayo umepakua hivi punde;
- Chagua kadi ya microSD kama lengo;
- Bofya kwenye `Mweko!`.



![Image](assets/fr/03.webp)



Subiri hadi mchakato ukamilike: microSD yako sasa iko tayari kutumika. Sasa unaweza kuendelea na kuunganisha kifaa chako.



Kwa maelezo zaidi juu ya usakinishaji wa programu dhibiti na uthibitishaji wa programu (hatua ninayopendekeza sana uchukue), angalia mafunzo yafuatayo:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Kukusanya kisoma kadi mahiri



![video](https://youtu.be/jqE8HDMCImA)



Anza kwa kusakinisha kamera kwenye Raspberry Pi Zero, ukiiingiza kwa makini kwenye pini ya kamera na kuifunga kwa kichupo cheusi. Kisha weka Pi kwenye sehemu ya chini ya kipochi, hakikisha kwamba milango imelinganishwa na fursa zinazolingana.



![Image](assets/fr/04.webp)



Kisha ambatisha kisoma kadi mahiri kwenye pini za GPIO za Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Telezesha kifuniko cha plastiki juu ya kisoma kadi mahiri hadi kiweke vizuri.



![Image](assets/fr/06.webp)



Kisha ongeza skrini kwenye pini za GPIO za kiendelezi.



![Image](assets/fr/07.webp)



Hatimaye, ingiza kadi ya microSD iliyo na firmware kwenye bandari ya upande kwenye Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Sasa unaweza kuunganisha SeedSigner yako kupitia bandari ndogo ya USB ya Raspberry Pi Zero, au kupitia mlango wa USB-C wa kiendelezi. Chaguzi zote mbili zinafanya kazi. Subiri sekunde chache kwa kuanza, kisha unapaswa kuona skrini ya kukaribisha ikionekana.



![Image](assets/fr/09.webp)



Kwa maelezo zaidi juu ya usanidi wa awali wa SeedSigner yako, ninapendekeza mafunzo yafuatayo:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Onyesha kadi mahiri kwa kutumia applet ya Seedkeeper (si lazima)



![video](https://youtu.be/NF4HemyEcOY)



Ikiwa tayari unamiliki Mtunza Mbegu, unaweza kuruka hatua hii na kwenda moja kwa moja hadi hatua ya 4. Katika sehemu hii, tutaangalia jinsi ya kusakinisha programu-jalizi ya Mtunza mbegu kwenye kadi mahiri tupu (njia ya DIY).



Ili kuanza, fungua menyu ya `Zana > Zana za Smartcard` kwenye SeedSigner yako.



![Image](assets/fr/10.webp)



Kisha chagua `Vyombo vya DIY > Sakinisha Applet`.



![Image](assets/fr/11.webp)



Ingiza smartcard yako kwenye kisomaji cha SeedSigner, chip kitazama chini, kisha uchague kichupo cha `SeedKeeper`.



![Image](assets/fr/12.webp)



Tafadhali kuwa na subira wakati wa usakinishaji: mchakato unaweza kuchukua makumi kadhaa ya sekunde.



![Image](assets/fr/13.webp)



Mara tu applet imesakinishwa kwa ufanisi, unaweza kuendelea hadi hatua ya 4.



![Image](assets/fr/14.webp)



## 4. Hifadhi SeedQR iliyopo kwenye Mkulima



![video](https://youtu.be/X-vmFHU9Ec8)



Kwa kuwa sasa Mtunza mbegu wako anafanya kazi, unaweza kuhifadhi kumbukumbu yako ya Bitcoin wallet kwenye kadi mahiri. Ili kuanza, washa SeedSigner yako kama kawaida, kisha changanua *SeedQR* ya wallet yako ili kuipakia kwenye kifaa. Mara baada ya seed kuingizwa, chagua tu `Nimemaliza`.



![Image](assets/fr/15.webp)



seed inapopakiwa, fikia menyu ya `Backup Seed`.



![Image](assets/fr/16.webp)



Kisha ingiza Seedkeeper yako kwenye kiendeshi cha SeedSigner, na uchague chaguo la `To SeedKeeper`.



![Image](assets/fr/17.webp)



Kisha SeedSigner itakuuliza uweke PIN msimbo wa Mkulima wako. Kwa vile hii ni kadi tupu, hakuna msimbo bado umefafanuliwa. Weka msimbo wowote ili kuruka hatua hii, kisha uthibitishe.



![Image](assets/fr/18.webp)



SeedSigner hugundua kuwa Mtunza mbegu bado hajaanzishwa (yaani, hakuna nenosiri lililowekwa). Bofya `Naelewa` ili kuendelea.



![Image](assets/fr/19.webp)



Sasa chagua PIN yako mpya ya Seedkeeper, kati ya herufi 4 na 16. Kwa usalama ulioongezwa, chagua msimbo mrefu na nasibu: ndicho kikwazo pekee kinacholinda ufikiaji wa kimwili kwa maneno yako ya kumbukumbu.



Kumbuka kuhifadhi PIN hii mara tu inapoundwa, ama katika kidhibiti kinachotegemewa cha nenosiri, au kwa njia tofauti ya kimwili kulingana na mkakati wako. Katika kesi ya pili, hakikisha kuwa huhifadhi kifaa chenye PIN mahali pamoja na Mtunza mbegu wako, vinginevyo ulinzi hautatumika. Ni muhimu kuwa na nakala mbadala: **Bila PIN hii, hutaweza kufikia seed yako, na bitcoins zako zitapotea**.



![Image](assets/fr/20.webp)



Kisha unaweza kufafanua `Lebo` inayohusishwa na kishazi chako cha kumbukumbu. Lebo hii ni muhimu ikiwa utahifadhi siri kadhaa kwenye Mtunza mbegu, ili uweze kuzitambua kwa urahisi.



![Image](assets/fr/21.webp)



Maneno yako ya kumbukumbu sasa yamehifadhiwa kwenye smartcard.



![Image](assets/fr/22.webp)



Kwa upande wa mkakati wa usalama, mbinu kadhaa zinawezekana, kulingana na mahitaji yako na kiwango cha mfiduo wa hatari. Binafsi, ninapendekeza uhifadhi angalau nakala 2 za seed yako:




- Hii ni mara ya kwanza kwa kadi mahiri, ambazo unaweza kuziweka kwa urahisi kwa shughuli za kila siku, kama vile kuthibitisha anwani au kutia saini miamala. Njia hii ni ya vitendo (kama tutakavyoona katika sehemu ya 5) na inasalia kuwa salama kutokana na ulinzi unaotolewa na msimbo wa PIN, ili uweze kuifanya ipatikane bila hatari kubwa;
- Nakala ya pili ya kifungu chako cha maneno cha mafumbo ambacho hakijasimbwa, kinachotumika kama hifadhi rudufu ya mwisho ya kwingineko yako, itatumika tu katika tukio la hasara au wizi wa Mlinzi wa Mbegu. Kwa vile toleo hili halijasimbwa, ni lazima liwekwe mahali tofauti, salama zaidi, ili kuzuia maelewano ya wakati mmoja ya nakala 2.



Kulingana na mkakati wako wa ulinzi na wasifu wa hatari, unaweza pia kunakili seed kwenye Watunza mbegu kadhaa tofauti, au kuunda nakala kadhaa halisi za kumbukumbu. Ili kujifunza zaidi kuhusu mazoea haya, angalia mafunzo yafuatayo:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Kupakia seed kutoka kwa Mtunza Mbegu



![video](https://youtu.be/ms0Iq_IyaoE)



Sasa unaweza kutumia Seedkeeper wako kupakia maneno yako ya kumbukumbu kwenye SeedSigner mwanzoni, na hivyo kusaini miamala yako ya Bitcoin. Ili kuanza, washa SeedSigner yako kwa kuichomeka, kisha ufungue menyu ya `Seeds`.



![Image](assets/fr/23.webp)



Kisha chagua chaguo la `Kutoka kwa SeedKeeper`.



![Image](assets/fr/24.webp)



Ingiza Seedkeeper yako kwenye kisoma kadi mahiri, kisha uweke PIN yako ili kuifungua. Thibitisha ingizo lako kwa kubofya kitufe cha uthibitishaji chini kulia, `KEY3`.



![Image](assets/fr/25.webp)



Mtunza mbegu anaweza kuwa na siri kadhaa, kwa hivyo SeedSigner kisha inakuomba uchague ile unayotaka kupakia. Lebo iliyoonyeshwa inalingana na jina ulilofafanua katika hatua ya 4. Ikiwa, kama ilivyo kwangu, umesajili seed moja tu, chaguo moja tu litapatikana.



![Image](assets/fr/26.webp)



seed yako sasa imepakiwa. Hakikisha kuwa hii ndiyo wallet sahihi kwa kulinganisha alama ya vidole inayoonyeshwa kwenye skrini na ile iliyobainishwa katika mipangilio yako ya Sparrow Wallet. Alama hii ya vidole pia ilitolewa wakati wallet ilipoundwa mara ya kwanza.



Ikiwa unatumia passphrase, unaweza kuitumia katika hatua hii (ona sehemu ya 6 ya mafunzo haya). Vinginevyo, bonyeza tu kwenye `Done`.



![Image](assets/fr/27.webp)



Kisha unaweza kutumia wallet yako kama kawaida: angalia anwani zako za kuletewa na utie sahihi miamala, kama vile ulivyotumia SeedSigner ya kawaida. Ili kujua zaidi jinsi ya kuitumia, angalia mafunzo maalum:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Kutumia Mtunza mbegu mwenye passphrase BIP39



Je, unatumia passphrase kulinda kwingineko yako ya Bitcoin? Unaweza pia kuisajili katika Mtunza mbegu wako, pamoja na seed yako. Suluhisho hili litakuwezesha kupakia kwa haraka wallet yako kwenye SeedSigner, bila kulazimika kuingiza mwenyewe passphrase kwenye vitufe vidogo kila wakati unapoitumia.



Ninaona njia hii ya kuvutia hasa, kwani inakuwezesha kufaidika na manufaa ya usalama ya passphrase, huku ikiondoa vikwazo vinavyohusiana na matumizi yake ya kila siku. Hapa kuna mfano wa usanidi ambao ningependekeza:




- Weka seed yako na passphrase kwenye Mtunza Mbegu, umelindwa na msimbo thabiti wa PIN (hii ni muhimu). Hifadhi rudufu hii itakuwezesha kutumia wallet yako kwa urahisi kila siku. Ukipenda, unaweza kunakili habari hii kwa Mtunza Mbegu wa pili;
- Pia weka nakala wazi ya mnemonic yako na passphrase, kwenye karatasi au chuma. Hii ndiyo chaguo lako la mwisho ikiwa utapoteza Mkulima wako au PIN yake. Hakikisha kuhifadhi nakala hizi katika maeneo tofauti, ili zisiweze kuathiriwa kwa wakati mmoja.



Katika usanidi huu, ikiwa mtu atapata mkono wako kwenye maandishi yako ya kawaida ya kumbukumbu peke yake, hataweza kuiba chochote bila kujua passphrase (mradi, bila shaka, ni nguvu ya kutosha kuhimili mashambulizi ya kikatili). Kinyume chake, mtu akigundua passphrase yako katika maandishi wazi, itasalia kuwa isiyoweza kutumika bila kishazi sambamba cha mnemonic.



Hatimaye, mtu akifanikiwa kupata ufikiaji wa kimwili kwa Mtunza mbegu wako aliye na seed na passphrase, hataweza kutoa chochote bila kujua PIN code. Tofauti na passphrase, msimbo huu hauwezi kulazimishwa kwa ukatili, kwani smartcard hujifunga kiotomatiki baada ya majaribio 5 batili.



Kwa hivyo usalama wa usanidi huu unategemea mambo mawili muhimu:




- **passphrase yenye nguvu**: lazima iwe ndefu, nasibu na iwe na aina mbalimbali za wahusika. Ugumu wake sio shida kwako, kwani itabidi uiingize mara moja kwenye kibodi wakati wa uanzishaji; baadaye, itasambazwa na Mtunza Mbegu;
- **Msimbo thabiti wa PIN** wa Mtunza mbegu: pia bila mpangilio na unajumuisha herufi 16.



Ili kusanidi usanidi huu, anza kwa kupakia passphrase yako kwenye SeedSigner kwa njia ya kawaida. Unaweza kufuata utaratibu ulioelezewa katika somo hili:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Mara tu kwingineko yako iliyo na passphrase imepakiwa kwa usahihi kwenye SeedSigner, fungua menyu ya `Seeds` na uchague alama ya miguu inayolingana na kwingineko hii. Kumbuka kwamba nyayo hii inatofautiana na ile ya kwingineko bila passphrase.



![Image](assets/fr/28.webp)



Kisha ubofye `Backup Seed`, ingiza Kiweka Mbegu kwenye kiendeshi, na uchague `To SeedKeeper`.



![Image](assets/fr/29.webp)



Weka PIN yako ili kumfungulia Mtunza mbegu, kisha weka lebo kwa siri hii. Unaweza kuacha alama ya kidole kama lebo ili kudumisha aina fulani ya ukanusho unaokubalika, au sema kwa uwazi `Nenosiri Wallet`, kwa mfano.



![Image](assets/fr/30.webp)



Malipo yako ya passphrase sasa yamesajiliwa kwenye Seedkeeper.



![Image](assets/fr/31.webp)



Wakati mwingine unapoanzisha, ingiza tu Mtunza mbegu wako kwenye hifadhi, kisha uende kwenye `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Weka PIN yako ili kufungua smartcard, kisha uchague wallet inayolingana na passphrase yako.



![Image](assets/fr/33.webp)



Angalia passphrase na chapa yako ya wallet, kisha uthibitishe.



![Image](assets/fr/34.webp)



Sasa unaweza kufikia kwingineko yako ukitumia passphrase na kutia sahihi miamala yako kama kawaida kwenye SeedSigner.



## 7. Chaguzi za ziada



Katika menyu ya `Zana > Zana za Smartcard`, utapata chaguzi kadhaa za kudhibiti Mkulima wako:





- Katika menyu ya `Zana za Kawaida`, unaweza:
 - Angalia uhalisi wa kadi;
 - Badilisha nambari ya PIN;
 - Badilisha lebo zinazohusishwa na siri zako;
 - Lemaza kitendakazi cha NFC (inapendekezwa ikiwa unatumia kisomaji cha chipu pekee);
 - Rejesha mipangilio ya kiwandani.





- Katika menyu ya `SeedKeeper Functions`, unaweza:
 - Angalia orodha ya siri zilizosajiliwa;
 - Hifadhi siri mpya;
 - Futa siri iliyopo;
 - Hifadhi au pakia vifafanuzi vyako (utendaji muhimu kwa portfolios za multi-sig).





- Katika menyu ya `Zana za DIY`, unaweza:
 - Kukusanya applet ya Mtunza mbegu;
 - Sakinisha applet kwenye kadi tupu;
 - Futa applet ya Mtunza mbegu ili kuiweka upya na kuifanya iwe wazi tena.



Sasa unajua jinsi ya kutumia Seedkeeper kucheleza kwingineko yako kwa usalama pamoja na SeedSigner.



Ikiwa usanidi huu umekushawishi, usisite kuunga mkono miradi inayowezesha:




- Kwa kununua kifaa chako moja kwa moja [kwenye tovuti ya Satochip](https://satochip.io/shop/);
- Kwa kutoa [mchango kwa mradi wa SeedSigner](https://seedsigner.com/donate/);
- Kwa kujiandikisha kwenye [Kituo cha YouTube cha Mwongozo wa Crypto](https://www.youtube.com/@CryptoGuide/), inayoendeshwa na mtu ambaye anahifadhi hazina ya GitHub inayopangisha programu dhibiti iliyorekebishwa.