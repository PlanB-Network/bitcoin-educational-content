---
name: Satochip x SeedSigner
description: Jinsi ya kutumia Satochip na SeedSigner yako?
---

![cover](assets/cover.webp)



*Shukrani kwa [Mwongozo wa Crypto](https://www.youtube.com/@CryptoGuide/) kwa fork yake ya programu dhibiti ya SeedSigner kwa usaidizi wa smartcard, ambayo tutatumia katika mafunzo haya.



---

Satochip ni maunzi mahiri ya umbizo la kadi ya wallet yenye kipengele cha usalama kilichoidhinishwa na EAL6+, mojawapo ya viwango vya juu zaidi vya usalama. Imeundwa na kuzalishwa na kampuni ya Ubelgiji ya jina moja: Satochip.



Bei ya takriban €25, Satochip inajitokeza kutoka kwa shindano kwa thamani yake bora ya pesa. Shukrani kwa chip yake salama, inatoa upinzani dhidi ya mashambulizi ya kimwili. Zaidi ya hayo, msimbo wake wa chanzo cha applet ni chanzo huria kabisa, umepewa leseni chini ya *AGPLv3*.



Kwa upande mwingine, muundo wake unaweka vikwazo fulani vya kazi. Upungufu kuu wa Satochip ni kukosekana kwa skrini iliyojumuishwa: kwa hivyo watumiaji lazima wasaini shughuli bila upofu, wakitegemea skrini ya kompyuta zao pekee.



Ili kuondokana na udhaifu huu, usanidi wa kuvutia hasa ni kuitumia kwa kushirikiana na SeedSigner. Katika usanidi huu, mawasiliano hayafanyiki tena moja kwa moja kati ya kompyuta na Satochip, lakini kupitia ubadilishanaji wa msimbo wa QR kati ya kompyuta na SeedSigner. SeedSigner kisha hufanya kama skrini ya uaminifu: inaonyesha habari ya kusainiwa, wakati saini yenyewe inafanywa na Satochip. Tofauti na matumizi ya kawaida ya SeedSigner (au hata tumia pamoja na Seedkeeper), seed haipakizwi kwenye SeedSigner. Kwa hivyo SeedSigner inakuwa skrini ya Satochip, ikiondoa hatari zinazohusiana na kutia sahihi bila upofu.



Ikiwa tunatazama tatizo kwa njia nyingine, kutumia SeedSigner na Satochip inajaza pengo kubwa katika SeedSigner: uwezo wa kuhifadhi na kutumia seed ndani ya secure element.



Kwa maoni yangu, usanidi huu hutoa faida kadhaa juu ya pochi za kawaida za vifaa:




- Satochip inagharimu takriban €25, na kwa kuwa applet ni chanzo huria, unaweza kuisakinisha mwenyewe kwenye smartcard tupu. Kisha unahitaji kuongeza gharama ya vipengele vya SeedSigner na kiendelezi cha kusoma smartcards: kulingana na mahali unaponunua maunzi haya, jumla inapaswa kuwa kati ya €70 na €100.
- Programu zote zinazohusika katika usanidi ni chanzo-wazi: programu dhibiti ya SeedSigner na applet ya Satochip.
- Unafaidika na kipengele cha usalama kilichoidhinishwa.
- Usanidi unaweza kufanywa kwa DIY kabisa, bila kutumia maunzi yaliyokusudiwa kwa uwazi kwa matumizi ya Bitcoin, ambayo inaweza kutoa aina ya kukanusha na kupinga vitisho fulani vya nje (pamoja na, kulingana na nchi, shinikizo la serikali). Hili pia ni suluhisho la kuvutia ikiwa ufikiaji wa pochi za vifaa vya kibiashara umezuiwa au hauwezekani katika eneo lako.




## 1. Nyenzo zinazohitajika



Ili kutekeleza usanidi huu, utahitaji vitu vifuatavyo:




- Vifaa vya kawaida vinavyohitajika na SeedSigner ya kawaida:
 - Raspberry Pi Zero na pini za GPIO,
 - 1.3" skrini ya wimbi la wimbi,
 - kamera inayoendana,
 - kadi ya microSD.



![Image](assets/fr/01.webp)





- SeedSigner extension kit, inapatikana [kutoka duka rasmi la Satochip](https://satochip.io/product/seedsigner-extension-kit/), ambayo hukuwezesha kusoma na kuandika kwa smartcard moja kwa moja kutoka kwa SeedSigner yako. Chaguo jingine ni kutumia [kisomaji cha kadi mahiri cha nje](https://satochip.io/product/chip-card-reader/), ambacho kinaweza kuunganishwa kwa kebo kwenye mlango wa Micro-USB kwenye Raspberry Pi. Walakini, sijajaribu suluhisho hili mwenyewe;
- [Satochip](https://satochip.io/product/satochip/), au badala yake [kadi mahiri tupu](https://satochip.io/product/card-for-diy-project/) ambayo kwayo programu ya applet ya Satochip (kifaa cha upanuzi kinachouzwa na Satochip tayari kinajumuisha smartcard tupu). Seti ya kiendelezi ya Satochip pia inaweza kutumia umbizo la [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Kwa hivyo unaweza kuchagua umbizo hili ukipenda.



![Image](assets/fr/02.webp)



Kwa maelezo zaidi juu ya vifaa vinavyohitajika ili kuunganisha SeedSigner, tafadhali rejelea Sehemu ya 1 ya mafunzo haya mengine:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Sakinisha firmware



Ili kutumia SeedSigner yako na Satochip, unahitaji kusakinisha programu dhibiti mbadala, tofauti na ile ya SeedSigner asili, ili kusaidia usomaji wa kadi mahiri. Kwa hili, [Ninapendekeza kutumia fork kutoka "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Pakua [toleo jipya zaidi la picha](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) inayolingana na muundo wa Raspberry Pi unaotumia.



![Image](assets/fr/03.webp)



Ikiwa tayari huna, pakua programu ya [Balena Etcher] (https://etcher.balena.io/), kisha uendelee kama ifuatavyo:




- Ingiza kadi ya microSD kwenye kompyuta yako;
- Uzinduzi Etcher;
- Chagua faili ya `.zip` ambayo umepakua hivi punde;
- Chagua kadi ya microSD kama lengo;
- Bofya kwenye `Mweko!`.



![Image](assets/fr/04.webp)



Subiri hadi mchakato ukamilike: microSD yako sasa iko tayari kutumika. Sasa unaweza kuendelea na kuunganisha kifaa chako.



Kwa maelezo zaidi juu ya usakinishaji wa programu dhibiti na uthibitishaji wa programu (hatua ninayopendekeza sana uchukue), angalia mafunzo yafuatayo:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Kukusanya kisoma kadi mahiri



Anza kwa kusakinisha kamera kwenye Raspberry Pi Zero, ukiiingiza kwa makini kwenye pini ya kamera na kuifunga kwa kichupo cheusi. Kisha weka Pi kwenye sehemu ya chini ya kipochi, hakikisha kwamba milango imelinganishwa na fursa zinazolingana.



![Image](assets/fr/05.webp)



Kisha ambatisha kisoma kadi mahiri kwenye pini za GPIO za Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Telezesha kifuniko cha plastiki juu ya kisomaji kadi mahiri hadi kiweke vizuri.



![Image](assets/fr/07.webp)



Kisha ongeza skrini kwenye pini za GPIO za kiendelezi.



![Image](assets/fr/08.webp)



Hatimaye, ingiza kadi ya microSD iliyo na firmware kwenye bandari ya upande kwenye Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Sasa unaweza kuunganisha SeedSigner yako kupitia bandari ndogo ya USB ya Raspberry Pi Zero, au kupitia mlango wa USB-C wa kiendelezi. Chaguzi zote mbili zinafanya kazi. Subiri sekunde chache kwa kuanza, kisha unapaswa kuona skrini ya kukaribisha ikionekana.



![Image](assets/fr/10.webp)



Kwa maelezo zaidi juu ya usanidi wa awali wa SeedSigner yako, ninapendekeza uangalie sehemu ya 4 ya mafunzo yafuatayo:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Onyesha kadi mahiri kwa kutumia applet ya Satochip (si lazima)



Ikiwa tayari unamiliki Satochip, unaweza kuruka hatua hii na kwenda moja kwa moja hadi hatua ya 4. Katika sehemu hii, tutaangalia jinsi ya kusakinisha applet ya Satochip kwenye smartcard tupu (njia ya DIY). Applet ni programu ndogo inayoendeshwa kwenye smartcard ambayo hutuwezesha kudhibiti vitendaji maalum.



Ili kuanza, fungua menyu ya `Zana > Zana za Smartcard` kwenye SeedSigner yako.



![Image](assets/fr/11.webp)



Kisha chagua `Vyombo vya DIY > Sakinisha Applet`.



![Image](assets/fr/12.webp)



Ingiza kadi yako mahiri kwenye kisomaji cha SeedSigner, huku chipu ikitazama chini, na uchague applet ya `Satochip`.



![Image](assets/fr/13.webp)



Tafadhali kuwa na subira wakati wa usakinishaji: mchakato unaweza kuchukua makumi kadhaa ya sekunde.



![Image](assets/fr/14.webp)



Mara tu applet imesakinishwa kwa ufanisi, unaweza kuendelea hadi hatua ya 4.



![Image](assets/fr/15.webp)




## 5. Kuunda na kuokoa seed



### 5.1. Tengeneza seed



Kwa kuwa sasa maunzi na programu yako yote inafanya kazi vizuri, unaweza kuendelea kuunda kwingineko yako ya Bitcoin. Ili kufanya hivyo, chomeka SeedSigner yako, kisha generate seed yako kama ilivyo kwa SeedSigner ya kawaida, ama kwa kukunja kete au kwa kupiga picha:




- Nenda kwenye menyu ya `Zana > Kamera / Dice Rolls`;
- Kisha fuata mchakato wa kizazi cha entropy kulingana na njia iliyochaguliwa;
- Hatimaye, cheleza seed kwenye vyombo vya habari vya kimwili na uangalie chelezo kwa uangalifu.



![Image](assets/fr/16.webp)



Ikiwa ungependa kuona maelezo ya utaratibu huu, tafadhali fuata sehemu ya 5 ya mafunzo haya:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Kuokoa seed kwa Mtunza Mbegu



Mara baada ya seed kuzalishwa, huu ndio wakati pekee inakaa kwenye RAM ya SeedSigner. Kwa upande wangu, ninataka kuihifadhi kwenye [Seedkeeper](https://satochip.io/product/seedkeeper/), bidhaa nyingine ya Satochip iliyoundwa kuhifadhi siri. Nitatumia kifaa hiki kama suluhu la mwisho, endapo nitapoteza Satochip yangu.



Mbinu mbadala iliyochaguliwa hapa inategemea mapendeleo yako, lakini ni muhimu kuwa na angalau nakala moja ya maneno yako ya kumbukumbu, ama kwenye vyombo vya habari (karatasi au chuma) au, kama hapa, kwa Mtunza Mbegu. Unaweza pia kuzidisha idadi ya chelezo kama inavyohitajika. Kwa habari zaidi juu ya mikakati ya kuhifadhi kwingineko, ninapendekeza usome mafunzo haya:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ili kuhifadhi nakala ya seed yako kwenye Mtunza mbegu, nenda moja kwa moja kwenye menyu ya `Backup Seed`.



![Image](assets/fr/17.webp)



Kisha ingiza Mtunza mbegu wako kwenye kisoma kadi mahiri, na uchague `To SeedKeeper`.



![Image](assets/fr/18.webp)



Weka PIN yako ili kuifungua.



![Image](assets/fr/19.webp)



Chagua `Lebo` ili kutambua kwa urahisi siri zako tofauti zilizohifadhiwa kwenye Seedkeeper. Unaweza, kwa mfano, kuweka tu alama ya wallet au kuonyesha wazi `Mbegu`. Chaguo inategemea upendeleo wako na hatari.



![Image](assets/fr/20.webp)



Iwapo mkakati wako wa kuhifadhi unategemea Mtunza mbegu huyu pekee, ninapendekeza ufanye jaribio tupu la urejeshaji sasa, kisha ulinganishe alama za vidole ili uhakikishe kuwa nakala rudufu inafanya kazi.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Nambari ya PIN ya Mlinzi wa mbegu inapaswa kuwa ndefu na bila mpangilio iwezekanavyo, ili kuzuia majaribio ya kinyama iwapo kadi itaathiriwa. Unapaswa pia kuweka nakala rudufu ya msimbo huu wa PIN, iliyohifadhiwa mahali tofauti na Mtunza mbegu. Bila PIN hii, hutaweza kufikia kumbukumbu zilizohifadhiwa katika Mtunza mbegu, na bitcoins zako zitapotea kabisa.



### 5.3. Okoa seed kwenye Satochip



Kwa kuwa sasa kwingineko yako imetolewa, kuhifadhiwa na kuthibitishwa, tutaihamisha hadi kwenye Satochip. Ili kufanya hivyo, hakikisha kuwa seed imepakiwa kwenye RAM ya SeedSigner. Kisha nenda kwa `Zana > Zana za Smartcard > Kazi za Satochip`.



![Image](assets/fr/21.webp)



Ingiza Satochip yako kwenye kisoma kadi mahiri, kisha uchague `Anzisha kwa kutumia Seed`.



![Image](assets/fr/22.webp)



Kifaa kinakuhimiza kuingiza msimbo wa PIN wa Satochip; kwa kuwa kadi ni mpya na haijaanzishwa, bado hakuna PIN. Weka msimbo wowote ili kuruka hatua hii (siyo ya kuzuia).



![Image](assets/fr/23.webp)



SeedSigner itagundua kuwa Satochip yako haijaanzishwa. Bofya `Naelewa` ili kuthibitisha.



![Image](assets/fr/24.webp)



Kisha unaweza kuweka msimbo wa PIN wa Satochip, kutoka kwa vibambo 4 hadi 16. Ili kuimarisha usalama wa wallet yako, chagua msimbo mrefu na nasibu: ndio ulinzi pekee dhidi ya ufikiaji wa kimwili kwa maneno yako ya kumbukumbu.



Kumbuka kuhifadhi PIN hii mara tu inapoundwa, ama katika kidhibiti salama cha nenosiri au kwa njia ya kawaida, kulingana na mkakati wako wa kibinafsi. Katika kesi ya pili, hakikisha kuwa hauhifadhi kifaa kilicho na PIN katika sehemu sawa na Satochip yako, vinginevyo ulinzi hautakuwa na maana. Ni muhimu kuwa na nakala mbadala: **Bila PIN hii, hutaweza kufikia seed yako, na bitcoins zako zitapotea milele**.



![Image](assets/fr/25.webp)



SeedSigner kisha inakuuliza ni seed gani ya kuingiza kwenye Satochip. Chagua ile ambayo alama yake ya vidole inalingana na kwingineko ambayo umeunda hivi punde.



![Image](assets/fr/26.webp)



seed yako sasa imeingizwa kwenye Satochip.



![Image](assets/fr/27.webp)



Sasa unaweza kuzima SeedSigner yako.



Ikiwa ungependa kutumia passphrase BIP39 ili kuimarisha usalama wa wallet yako, tafadhali angalia sehemu ya 6 ya mafunzo haya:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Ingiza wallet kwenye Sparrow



Kwa kuwa sasa jalada lako limeanza kutumika, tutaleta taarifa zake za umma ("*duka la vitufe*") kwenye Sparrow Wallet au programu nyingine ya usimamizi wa kwingineko. Programu hii itatumika kuunda, kusambaza na kufuatilia miamala yako. Hata hivyo, haitaweza kuzitia sahihi, kwa kuwa ni Satochip pekee (na chelezo zozote) hushikilia funguo za faragha zinazohitajika kwa operesheni hii.



### 6.1 Kutayarisha SeedSigner na Satochip



Ingiza kadi ya microSD iliyo na mfumo wa uendeshaji, kisha uwashe SeedSigner yako. Kwa sasa, haiwezi kufanya lolote, kwani bado haijui seed yako. Itabidi uanze kwa kuingiza Satochip kwenye kisoma kadi mahiri, kwa kuwa ndicho kinachoshikilia seed yako.



Kutoka kwa Skrini ya Nyumbani, fikia menyu ya `Zana > Zana za Smartcard > Kazi za Satochip`.



![Image](assets/fr/28.webp)



Kisha bonyeza `Hamisha Xpub`.



![Image](assets/fr/29.webp)



Chagua aina ya kwingineko. Kwa upande wetu, ni kwingineko moja: chagua `Sig Moja`.



![Image](assets/fr/30.webp)



Inayofuata inakuja uchaguzi wa kiwango cha uandishi. Chagua ya hivi punde: `Native SegWit`.



![Image](assets/fr/31.webp)



Hatimaye, chagua `Mratibu`, yaani, programu ya usimamizi wa kwingineko unayotaka kutumia. Hapa, tutakuwa tukitumia Sparrow Wallet.



![Image](assets/fr/32.webp)



Ujumbe wa onyo unaonekana: hii ni kawaida kabisa. Ufunguo uliopanuliwa wa umma (`xpub`) hukuruhusu kutazama anwani zote zinazotokana na seed yako (kwenye akaunti ya kwanza). Hata hivyo, haitoi ufikiaji wa pesa zako: ufichuzi wake utahatarisha faragha yako, lakini sio usalama wa bitcoins zako. Kwa maneno mengine, inakuwezesha kuchunguza mizani yako, lakini si kuitumia.



Bofya kwenye `Naelewa`.



![Image](assets/fr/33.webp)



Kisha weka PIN yako ya Satochip ili kuifungua. Huu ndio msimbo uliofafanua na kuhifadhi katika hatua ya 5.



![Image](assets/fr/34.webp)



Hatimaye, bofya `Hamisha Xpub` ikiwa umeridhika na taarifa iliyoonyeshwa.



![Image](assets/fr/35.webp)



SeedSigner kisha hutengeneza xpub yako katika mfumo wa msimbo unaobadilika wa QR, ulio na data yote unayohitaji ili kudhibiti kwingineko yako katika Sparrow Wallet. Unaweza kurekebisha mwangaza wa skrini kwa kutumia kijiti cha furaha ili kurahisisha kuchanganua msimbo wa QR.



### 6.2 Kuagiza kwingineko mpya kwenye Sparrow Wallet



Hakikisha kwamba programu ya Sparrow Wallet imesakinishwa kwenye kompyuta yako. Ikiwa hujui jinsi ya kuipakua, angalia uhalisi wake na usakinishe kwa usahihi, angalia mafunzo yetu kamili juu ya somo:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kwenye kompyuta yako, fungua Sparrow Wallet, kisha kwenye upau wa menyu, bofya `Faili → Ingiza Wallet`.



![Image](assets/fr/36.webp)



Tembeza chini hadi `SeedSigner`, kisha uchague `Scan...`. Kamera yako ya wavuti itawashwa: changanua msimbo unaobadilika wa QR unaoonyeshwa kwenye skrini yako ya SeedSigner.



![Image](assets/fr/37.webp)



Weka jina kwa kwingineko yako, kisha ubofye kwenye `Unda Wallet`. Sparrow itakuuliza uweke nenosiri ili kufunga ufikiaji wa ndani kwa wallet hii. Chagua nenosiri thabiti: hulinda data yako katika Sparrow (funguo za umma, anwani, lebo na historia ya muamala). Hata hivyo, nenosiri hili halihitajiki kurejesha wallet katika siku zijazo: tu maneno yako ya mnemonic (na labda passphrase yako) itakuwa.



Ninapendekeza kwamba uhifadhi nenosiri hili kwenye kidhibiti cha nenosiri, ili kuepuka kulipoteza.



![Image](assets/fr/38.webp)



Hifadhi yako ya vitufe imeingizwa kwa ufanisi.



![Image](assets/fr/39.webp)



Sasa hakikisha kwamba `alama ya vidole kuu` iliyoonyeshwa katika Sparrow Wallet inalingana na ile iliyopatikana hapo awali kwenye SeedSigner yako.



SeedSigner kisha itakuuliza uchanganue anwani ya kupokea bila mpangilio kutoka kwa Sparrow wallet yako ili kuthibitisha uhalali wa uagizaji.



![Image](assets/fr/40.webp)



Satochip yako (kupitia SeedSigner) na Sparrow Wallet sasa zimeunganishwa kwa usalama. Sparrow hufanya kazi kama kiolesura kamili cha usimamizi, ilhali Satochip inasalia kuwa kifaa pekee chenye uwezo wa kusaini miamala yako. Sasa uko tayari kupokea na kutuma bitcoins katika usanidi usio na hewa kabisa.



![Image](assets/fr/41.webp)



## 7. Kupokea na kutuma bitcoins



Satochip yako na Sparrow Wallet sasa zimesanidiwa kufanya kazi pamoja. Katika sehemu hii, tutaelezea hatua kwa hatua jinsi ya kupokea na kutuma bitcoins katika hali hii.



### 7.1 Kupokea bitcoins



#### 7.1.1 Kuzalisha anwani ya mapokezi



Kwenye kompyuta yako, fungua Sparrow Wallet na ufungue `Satochip-SeedSigner` wallet yako kwa kutumia nenosiri lako. Angalia ikiwa programu imeunganishwa kwenye seva (kiashiria chini kulia). Kisha, kwenye upau wa kando, bofya kwenye `Pokea`.



![Image](assets/fr/42.webp)



Anwani mpya ya Bitcoin inaonekana. Utapata:




- Anwani katika umbizo la maandishi (kuanzia na `bc1q...` ikiwa unatumia P2WPKH, kama katika mfano huu);
- Msimbo wa QR unaohusishwa;
- Sehemu ya `Lebo`, ambayo ni muhimu kwa kufuatilia miamala yako.



Ninapendekeza sana uongeze lebo kwa kila risiti ya bitcoin katika wallet yako. Hii itakusaidia kutambua kwa urahisi asili ya kila UTXO na kudhibiti vyema faragha yako. Ili kujua zaidi kuhusu somo hili muhimu, angalia mafunzo maalum kuhusu Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Ili kuongeza lebo, ingiza tu jina katika sehemu ya `Lebo`, kisha uthibitishe.



Kwa mfano:



```txt
Label : Sale of the Raspberry Pi Zero
```



Anwani yako sasa inahusishwa na lebo hii katika sehemu zote za Sparrow.



![Image](assets/fr/43.webp)



#### 7.1.2 uthibitishaji wa Address kwenye SeedSigner



Kabla ya kuwasilisha anwani yako ya kupokea kwa mlipaji, ni muhimu kuangalia kuwa ni ya seed yako. Hatua hii inahakikisha kwamba Satochip yako itaweza kutia saini miamala inayohusishwa na anwani hii. Pia huzuia mashambulizi yanayoweza kutokea ambapo Sparrow ingeonyesha anwani ya ulaghai. Kumbuka kwamba Sparrow inaendeshwa kwenye mazingira yasiyo salama (kompyuta yako), ambayo eneo lake la mashambulizi ni kubwa zaidi kuliko la Satochip yako, ambayo imetengwa kabisa. Hii ndiyo sababu hupaswi kamwe kuamini kwa upofu anwani zinazoonyeshwa kwenye Sparrow kabla ya kuziangalia kwenye maunzi yako ya wallet.



Katika Sparrow, bofya kwenye msimbo wa QR wa anwani ili kuikuza: kisha itaonyeshwa skrini nzima.



![Image](assets/fr/44.webp)



Kwenye SeedSigner yako, weka Satochip kwenye kisomaji, kisha kutoka kwenye menyu kuu, chagua `Scan`. Changanua msimbo wa QR unaoonyeshwa kwenye kompyuta yako, kisha uchague `Tumia kadi ya Satochip`.



![Image](assets/fr/45.webp)



Kisha thibitisha aina ya hati iliyotumiwa (katika kesi hii, `Native SegWit`), weka msimbo wa PIN wa Satochip ili kuifungua, na uthibitishe maelezo ya `xpub`.



![Image](assets/fr/46.webp)



Ikiwa anwani iliyochanganuliwa inalingana na ile inayotokana na seed yako, SeedSigner itaonyesha ujumbe: `Address Imethibitishwa`.



![Image](assets/fr/47.webp)



Kisha unaweza kuwa na uhakika kwamba anwani ni ya kwingineko yako.



#### 7.1.3 Kupokea fedha



Sasa unaweza kutuma anwani hii kwa njia ya maandishi au kupitia msimbo wake wa QR kwa mtu au idara inayohitaji kukutumia satss. Muamala ukishatangazwa kwenye mtandao, utaonekana kwenye kichupo cha `Miamala` cha Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Tuma bitcoins



Kutuma bitcoins na usanidi wa Satochip-SeedSigner kunahusisha hatua 3:




- Uumbaji wa shughuli katika Sparrow;
- Kutia saini muamala huu kwenye Satochip, kupitia SeedSigner;
- Hatimaye, shughuli hiyo inatangazwa kwenye mtandao kutoka Sparrow.



Mabadilishano yote kati ya vifaa hivi viwili hufanyika kupitia misimbo ya QR pekee.



#### 7.2.1 Kuunda shughuli katika Sparrow



Katika Sparrow Wallet, unaweza kuunda muamala kwa kubofya kichupo cha `Tuma` kwenye upau wa upande wa kushoto. Hata hivyo, napendelea kutumia kichupo cha `UTXOs`, ambacho hukuruhusu kufanya mazoezi ya *Coin Control*. Mbinu hii inatoa udhibiti sahihi juu ya UTXO zilizotumiwa, ili kupunguza maelezo yaliyofichuliwa wakati wa shughuli zako za malipo.



Katika kichupo cha `UTXOs`, chagua sarafu unazotaka kutumia, kisha ubofye `Tuma Zilizochaguliwa`.



![Image](assets/fr/49.webp)



Kisha jaza sehemu za muamala:




- Katika `Lipa kwa`, bandika anwani ya mpokeaji au changanua msimbo wake wa QR kwa kutumia aikoni ya kamera ;
- Katika `Lebo`, ongeza lebo ili kufuatilia gharama hii;
- Katika `Kiasi`, weka kiasi kitakachotumwa;
- Hatimaye, chagua kiwango cha malipo kulingana na hali za sasa za mtandao (makadirio yanapatikana katika [mempool.space](https://mempool.space/)).



Mara baada ya kukamilisha sehemu zote, kagua maelezo kwa makini, kisha ubofye `Unda Muamala >>`.



![Image](assets/fr/50.webp)



Angalia maelezo ya muamala mara ya mwisho kwa usahihi, kisha ubofye `Maliza Muamala kwa Kutia Saini`.



![Image](assets/fr/51.webp)



Muamala sasa uko tayari, lakini bado haujatiwa saini. Ili kuonyesha [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) kama msimbo wa QR, bofya `Onyesha QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Kusaini muamala na Satochip



Washa SeedSigner yako na uweke Satochip yako kama kawaida. Kutoka kwa skrini ya kwanza, chagua `Scan`, kisha uchanganua msimbo wa QR unaoonyeshwa kwenye Sparrow.



![Image](assets/fr/53.webp)



Teua chaguo la `Tumia Satochip card`.



![Image](assets/fr/54.webp)



Weka PIN yako ili kufungua smartcard.



![Image](assets/fr/55.webp)



SeedSigner inagundua kuwa hii ni PSBT na inaonyesha muhtasari wa shughuli:




   - Kiasi kilichotumwa,
   - Anwani za lengwa,
   - Gharama zinazohusiana za manunuzi.



Bofya kwenye `Maelezo ya Kagua` na uchunguze taarifa zote moja kwa moja kwenye skrini ya SeedSigner. Mambo muhimu zaidi ya kuangalia ni kiasi kilichotumwa, anwani lengwa na ada za miamala.



![Image](assets/fr/56.webp)



Ikiwa kila kitu kiko sawa, chagua `Idhinisha PSBT` ili kutia sahihi muamala kwa kutumia Satochip.



![Image](assets/fr/57.webp)



Sahihi ikishakamilika, SeedSigner hutengeneza msimbo mpya wa QR ulio na shughuli iliyotiwa saini, tayari kuchanganuliwa na Sparrow.



#### 7.2.3 Kutangaza muamala kutoka Sparrow



Sasa kwa kuwa shughuli hiyo imesainiwa na kuthibitishwa, kilichobaki ni kuitangaza kwenye mtandao wa Bitcoin ili mchimbaji aweze kuijumuisha kwenye kizuizi. Katika Sparrow, bofya `Scan QR`.



![Image](assets/fr/58.webp)



Wasilisha msimbo wa QR unaoonyeshwa kwenye SeedSigner yako (ile iliyo na shughuli iliyotiwa saini) kwenye kamera ya wavuti. Sparrow itaonyesha maelezo yote ya muamala. Hakikisha kuwa maelezo yote ni sahihi, kisha ubofye "Muamala wa Matangazo" ili kuyatangaza kwenye mtandao wa Bitcoin.



![Image](assets/fr/59.webp)



Muamala wako sasa umetumwa kwa mtandao. Unaweza kufuata uthibitisho wake katika kichupo cha `Shughuli` cha Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Rudisha wallet yako



Kama tulivyoona katika sehemu zilizopita, kulingana na mkakati wako wa usalama, kuna njia kadhaa za kuhifadhi nakala ya maneno yako ya kurejesha akaunti pamoja na Satochip yako :




- Kwa kutumia *SeedQR* ya kawaida na SeedSigner;
- Kwa kurekodi maneno ya mnemonic kwenye njia ya kimwili;
- Au kwa kuihifadhi kwa Mtunza Mbegu, kama ilivyoelezwa katika sehemu ya 5.2.



Kwa hali yoyote, kuna hali 2 kuu ambazo unahitaji kuingilia kati: kupoteza Satochip au kupoteza kwa SeedSigner. Hebu tuangalie jinsi ya kuitikia katika kila moja ya matukio haya.



### 8.1. Rejesha wallet yako ukitumia Satochip



Ikiwa bado una Satochip yako lakini SeedSigner yako imevunjwa au imepotea, hali ni rahisi kudhibiti, kwa kuwa wallet yako bado iko kwenye Satochip.



Chaguo bora ni kupendekeza vipengele muhimu na kujenga upya SeedSigner mpya kutoka mwanzo. Kwa vile hiki ni kifaa "kisicho na hali", haijalishi ikiwa unatumia SeedSigner sawa au nyingine: mradi tu unaweza kuingiza Satochip yako, kila kitu kitafanya kazi kawaida.



Ikiwa hutaki kuunda tena, unaweza pia kutumia Satochip yako kwa njia ya kawaida, yaani moja kwa moja kutoka kwa kompyuta yako, bila kupitia SeedSigner. Njia hii inafanya kazi kikamilifu, lakini inapunguza sana usalama wa Bitcoin wallet yako: unapoteza utengaji wa "*hewa-pengo*" na lazima sasa utie sahihi kwa upofu, kwa kuwa SeedSigner ilifanya kazi kama skrini inayoaminika. Hata hivyo, hili linaweza kuwa suluhu la muda katika dharura, au ikiwa huwezi kujenga upya SeedSigner.



Ili kufanya hivyo, utahitaji kadi mahiri ya USB au kisomaji cha NFC. Fungua wallet unayotaka kurejesha katika Sparrow, kisha uende kwenye kichupo cha `Mipangilio` na ubofye `Badilisha`.



![Image](assets/fr/61.webp)



Ingiza Satochip yako kwenye kisoma kadi mahiri kilichounganishwa kwenye kompyuta, kisha ubofye `Leta` karibu na `Satochip`.



![Image](assets/fr/62.webp)



Hatimaye, weka PIN yako ya smartcard ili kuifungua. Kisha utaweza kufikia wallet yako, uunde miamala na utie sahihi moja kwa moja ukitumia Satochip iliyounganishwa.



### 8.2. Rejesha kwingineko yako na SeedSigner



Hali nyingine, nyeti zaidi ni wakati unapoteza ufikiaji wa Satochip yako iliyo na seed: iwe imevunjwa, imepotea, imeibiwa, au umesahau msimbo wake wa PIN. Ikiwa Satochip yako imeibiwa au kupotoshwa, tunapendekeza kwamba, mara tu ufikiaji wa pesa zako umerejeshwa, uhamishe bitcoins zako mara moja kwa wallet mpya kabisa, iliyotengenezwa kwa seed tofauti. Hii inahakikisha kwamba mshambulizi anayewezekana hawezi kamwe kufikia satss yako.



Ili kupata tena ufikiaji wa kwingineko yako na kuhamisha pesa zako, pakia seed yako kwenye SeedSigner. Kulingana na media mbadala uliyotumia, una chaguzi kadhaa:





- Weka kirai chako cha mafumbo wewe mwenyewe katika menyu ya `Mbegu > Weka maneno 12 ya seed`.



![Image](assets/fr/63.webp)





- Changanua *SeedQR* yako kwa kubofya kitufe cha `Scan` kwenye ukurasa wa nyumbani.



![Image](assets/fr/64.webp)





- Au pakia seed yako kutoka kwa Mtunza Mbegu, kupitia menyu ya `Seeds > From SeedKeeper` (hii ndiyo njia ninayotumia kwenye mafunzo haya). Utahitaji tu kuweka PIN ya Mtunza Mbegu na uchague siri itakayotumika kama seed kwenye SeedSigner.



![Image](assets/fr/65.webp)



Mara tu seed inapopakiwa kwenye SeedSigner, kwa njia yoyote utakayotumia, utaweza kutia sahihi katika shughuli moja au zaidi ya kuchanganua ili kuhamisha bitcoins zako hadi kwenye wallet mpya, isiyoathiriwa. Ili kujua jinsi ya kufanya hivyo, angalia sehemu ya 7.2 ya mafunzo yafuatayo:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Sasa unajua jinsi ya kutumia Satochip kudhibiti kwingineko yako ya Bitcoin kwa usalama pamoja na SeedSigner.



Ikiwa usanidi huu umekushawishi, usisite kusaidia miradi inayowezesha:




- Kwa kununua kifaa chako moja kwa moja [kwenye tovuti ya Satochip](https://satochip.io/shop/);
- Kwa kutoa [mchango kwa mradi wa SeedSigner](https://seedsigner.com/donate/);
- Kwa kujiandikisha kwenye [Kituo cha YouTube cha Mwongozo wa Crypto](https://www.youtube.com/@CryptoGuide/), inayoendeshwa na mtu ambaye anahifadhi hazina ya GitHub inayopangisha programu dhibiti iliyorekebishwa tuliyotumia katika mafunzo haya.