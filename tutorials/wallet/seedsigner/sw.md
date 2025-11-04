---
name: SeedSigner
description: Vifaa vya DIY, visivyo na uraia, vya bei nafuu na vilivyo na nafasi ya hewa kabisa ya wallet
---

![cover](assets/cover.webp)



SeedSigner ni maunzi huria ya wallet Bitcoin ambayo mtu yeyote anaweza kujitengenezea kwa kutumia vipengele vya kielektroniki vya madhumuni ya jumla ya bei nafuu. Tofauti na bidhaa za kibiashara kama vile Ledger, Coldcard au Trezor, hiki si kifaa kilicho tayari kutumika kilichotengenezwa na kampuni: ni mradi wa jumuiya unaoruhusu mtu yeyote kuunda kifaa chake mwenyewe, kudhibiti kila hatua.



SeedSigner imeundwa kuwa 100% ***hewa-pengo***: haiunganishi kamwe kwenye Mtandao, haina Wi-Fi au Bluetooth (katika kesi ya Raspberry Pi Zero v1.3) na haiunganishwa kamwe kwenye kompyuta ili kubadilishana data. Mawasiliano ni kupitia mfumo wa kubadilishana msimbo wa QR pekee. Kwa maneno madhubuti, programu yako ya usimamizi wa kwingineko (kama vile Sparrow Wallet) huonyesha muamala utakaotiwa saini katika mfumo wa misimbo ya QR; unazichanganua kwa kamera ya SeedSigner, kisha kifaa kitatia sahihi shughuli hiyo kwa kutumia funguo zako za faragha zilizohifadhiwa kwa muda kwenye RAM yake. Hatimaye, hutengeneza misimbo ya QR iliyo na shughuli iliyotiwa saini, ambayo unachanganua kwa programu yako ili kuituma kwa mtandao wa Bitcoin.



![Image](assets/fr/001.webp)



SeedSigner pia haina uraia***. Kwa maneno mengine, haihifadhi seed yako au funguo zako za kibinafsi kabisa, tofauti na pochi zingine za maunzi. Kila wakati unapowasha upya, kumbukumbu yake ni tupu kabisa, isipokuwa ukisanidi kifaa ili kuhifadhi mipangilio yako kwenye kadi ya microSD. Kwa hivyo inabidi uingize tena seed yako kila wakati unapoitumia, njia inayotumika zaidi ni kuihifadhi katika mfumo wa msimbo wa QR, ili kuchanganuliwa inapoanzishwa kwa kutumia kamera ya SeedSigner. Njia hii ya utendakazi hupunguza eneo la shambulio kwa kiasi kikubwa: hata mwizi akiiba kifaa chako, hatapata taarifa yoyote juu yake, kwa kuwa daima huwa tupu kwa chaguo-msingi.



Chaguo jingine la kuhifadhi seed yako na kuitumia kwa SeedSigner ni kutumia kadi mahiri ya *SeedKeeper* pamoja na kisomaji kinachooana. Hili hukupa *Secure Element* imara sana ili kuhifadhi seed yako, huku ukitumia skrini ya SeedSigner kusaini miamala. Lakini usanidi huu ni somo la mafunzo mengine ya kujitolea. Hapa, tutazingatia matumizi ya kimsingi ya SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Mradi wa SeedSigner unachukua nafasi muhimu katika mfumo wa ikolojia wa Bitcoin, kwani inatoa kila mtu, kila mahali ulimwenguni, uwezekano wa kufaidika na usalama wa hali ya juu ili kulinda bitcoins zao. Faida yake kuu iko katika upatikanaji wake: vifaa vinavyohitajika vinaweza kununuliwa kwa chini ya $ 50. Zaidi ya hayo, inawawezesha watu wanaoishi katika nchi zilizowekewa vikwazo kuunda maunzi yao ya wallet kutoka kwa vipengele vya kawaida vya kompyuta, ambavyo ni rahisi kupata na chini ya vikwazo vya udhibiti.



Lakini hata nje ya miktadha hii mahususi, SeedSigner inaweza kuwa chaguo la kuvutia kwako: ni chanzo huria, inafanya kazi bila utaifa na hewa, na inapunguza vienezaji vya mashambulizi vilivyounganishwa na msururu wa usambazaji wa maunzi yako ya wallet.



## 1. Vifaa vinavyohitajika



Ili kuunda SeedSigner yako, utahitaji vifaa vifuatavyo:





- Raspberry Pi Zero
    - Toleo la 1.3 linapendekezwa, kwa kuwa halina Wi-Fi wala Bluetooth, na hivyo kuhakikisha kutengwa kabisa.
 - Matoleo ya W na v2 pia yanaoana, lakini yanajumuisha chipu ya Wi-Fi/Bluetooth. Kwa hiyo ni vyema kuizima kimwili kwa kuondoa moduli ya redio kutoka kwa kadi. Operesheni ni rahisi, lakini inahitaji usahihi (pliers nzuri ni ya kutosha kwa Zero W, wakati kalamu ya moto inahitajika kwa v2 ili kuondoa sahani ya chuma inayoficha moduli). Sitazingatia maelezo katika mafunzo haya, lakini utapata maagizo yote katika hati hii: *[Kuzima WiFi/Bluetooth kwa maunzi](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Tafadhali kumbuka: baadhi ya miundo ya Raspberry Pi Zero inauzwa bila pini za GPIO zilizouzwa awali. Unaweza kununua toleo na pini zilizojumuishwa moja kwa moja (suluhisho rahisi), au ununue pini kando na uziuze mwenyewe (suluhisho ngumu zaidi).
 - Usisahau kujumuisha usambazaji wa umeme wa USB ndogo.



![Image](assets/fr/002.webp)





- Skrini ya Waveshare inchi 1.3 (240×240 px)** (kwa Kifaransa)
    - Ni muhimu kuchagua muundo huu mahususi: skrini zingine zinazofanana zipo, lakini zenye mwonekano tofauti. Bila ufafanuzi wa px 240×240, onyesho halitatumika.
    - Skrini ina vitufe vitatu na kijiti kidogo cha kiolesura cha mtumiaji.



![Image](assets/fr/003.webp)





- Raspberry Pi Zero**-kamera inayolingana
    - Chaguo la 1: kamera ya kawaida yenye mkeka mpana wa dhahabu (angalia uoanifu na nyumba yako).
    - Chaguo la 2: kamera iliyobana zaidi ya "*Zero*", iliyoundwa mahususi kwa Pi Zero.



![Image](assets/fr/004.webp)





- Kadi ya MicroSD**
    - Uwezo unaopendekezwa: kati ya GB 4 na 32.





- Nyumba (ya hiari lakini inapendekezwa)** (si lazima lakini inapendekezwa)** (si lazima lakini inapendekezwa)** (si lazima lakini inapendekezwa)**)
    - Hulinda kifaa na kurahisisha kutumia.
    - Muundo maarufu zaidi ni "*Kipochi cha Kidonge cha Machungwa*", ambacho [faili huria za STL zinapatikana kwa uchapishaji wa 3D](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosure).
    - Sanduku zinapatikana pia kutoka kwa [wauzaji wanaojitegemea waliounganishwa na mradi](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Unaweza kununua vipengele hivi tofauti au, kwa unyenyekevu zaidi, chagua pakiti zilizopangwa tayari ambazo zinajumuisha vifaa vyote muhimu. Binafsi, niliagiza kifurushi changu [kwenye tovuti hii ya Kifaransa](https://bitcoinbazar.fr/), lakini pia utapata orodha ya wachuuzi kwa kila eneo la dunia kwenye [ukurasa wa maunzi wa mradi wa SeedSigner](https://seedsigner.com/hardware/). Ukipendelea kununua vipengele kibinafsi, vinapatikana kwenye majukwaa makuu ya biashara ya mtandaoni au katika maduka maalumu.



## 2. Kuandaa programu



Mara tu unapounganisha maunzi yako, unahitaji kuandaa kadi ya microSD kwa kusakinisha mfumo wa SeedSigner juu yake. Ili kufanya hivyo, nenda kwenye kompyuta yako ya kibinafsi ya kila siku, na uchomekee microSD yako iliyokusudiwa kwa SeedSigner.



### 2.1. Pakua



Nenda kwa [hazina rasmi ya mradi wa GitHub](https://github.com/SeedSigner/seedsigner/releases). Kwenye toleo la hivi punde la programu, pakua :




- Picha ya `.img` inayolingana na muundo wako wa Pi.
- Faili ya `.sha256.txt`.
- Faili ya `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Kabla ya kuanza usakinishaji, hebu tuangalie programu.



### 2.2 Uthibitishaji chini ya Linux na macOS



Anza kwa kuleta ufunguo rasmi wa umma wa mradi wa SeedSigner moja kwa moja kutoka Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminal inapaswa kukuambia kuwa ufunguo umeingizwa au kusasishwa. Kisha, endesha amri ya uthibitishaji kwenye faili ya sahihi (kumbuka kurekebisha amri kulingana na toleo lako, hapa `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Ikiwa kila kitu ni sawa, matokeo yanapaswa kusoma `Sahihi nzuri`. Hii ina maana kwamba faili `.sha256.txt` imetiwa saini na ufunguo ambao umetoka kuleta, na kwamba sahihi ni halali. Puuza ujumbe wa onyo `ONYO: Ufunguo huu haujaidhinishwa kwa saini inayoaminika`: hii ni kawaida, kwa kuwa ni juu yako sasa kuangalia kuwa ufunguo uliotumika ni wa mradi wa SeedSigner.



Ili kufanya hivyo, linganisha herufi 16 za mwisho za alama ya vidole zinazoonyeshwa na zile zinazopatikana kwenye [Keybase.io/SeedSigner](https://keybase.io/seedsigner), kwenye [Twitter rasmi](https://twitter.com/SeedSigner/status/1530555252373704707), au katika faili iliyochapishwa [SeedSigner.com](https://seedsigner.com/keybase.txt). Ikiwa vitambulishi hivi vinalingana haswa, unaweza kuwa na uhakika kwamba ufunguo ni ule wa mradi. Ikiwa una shaka, acha mara moja na uulize jumuiya ya SeedSigner (Telegram, X, GitHub...) kwa usaidizi.



Wakati ufunguo umeidhinishwa, unaweza kuangalia kuwa picha iliyopakuliwa haijarekebishwa (kumbuka kurekebisha amri kulingana na toleo lako, hapa `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Chini ya Linux, amri hii imejengwa ndani.
- Onyo: matoleo ya macOS kabla ya `Big Sur (11)` hayatambui chaguo la `--puuza-kukosa`. Katika kesi hii, iondoe na upuuze maonyo kuhusu kukosa faili.



Matokeo yanayotarajiwa ni `Sawa` karibu na faili ya `.img`. Hii inathibitisha kuwa picha iliyopakiwa ni sawa na ile iliyochapishwa na mradi na haijabadilishwa.



### 2.3 Uthibitishaji wa Windows



Kwenye Windows, utaratibu ni sawa lakini amri ni tofauti. Anza kwa kusakinisha [Gpg4win](https://www.gpg4win.org/) na ufungue programu ya *Kleopatra*. Ingiza ufunguo wa umma wa mradi wa SeedSigner kutoka kwa Keybase ya URL :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Kisha, fungua PowerShell katika folda ambapo faili zako zilizopakuliwa zinapatikana (`Shift` + bofya kulia > `Fungua PowerShell hapa`). Tekeleza amri ifuatayo ili kuangalia saini ya maelezo (kumbuka kurekebisha amri kulingana na toleo lako, hapa `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Ikiwa kila kitu ni sawa, matokeo yanapaswa kusoma `Sahihi nzuri`. Hii ina maana kwamba faili `.sha256.txt` imetiwa saini na ufunguo ambao umetoka kuleta, na kwamba sahihi ni halali. Puuza ujumbe wa onyo `ONYO: Ufunguo huu haujaidhinishwa kwa saini inayoaminika`: hii ni kawaida, kwa kuwa ni juu yako sasa kuangalia kuwa ufunguo uliotumika ni wa mradi wa SeedSigner.



Ili kufanya hivyo, linganisha herufi 16 za mwisho za alama ya vidole zinazoonyeshwa na zile zinazopatikana kwenye [Keybase.io/SeedSigner](https://keybase.io/seedsigner), kwenye [Twitter rasmi](https://twitter.com/SeedSigner/status/1530555252373704707), au katika faili iliyochapishwa [SeedSigner.com](https://seedsigner.com/keybase.txt). Ikiwa vitambulishi hivi vinalingana haswa, unaweza kuwa na uhakika kwamba ufunguo ni ule wa mradi. Ikiwa una shaka, acha mara moja na uulize jumuiya ya SeedSigner (Telegram, X, GitHub...) kwa usaidizi.



Baada ya ufunguo kuthibitishwa, unahitaji kuangalia kuwa faili ya picha haijaharibiwa. Ili kufanya hivyo, tumia amri ifuatayo katika PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Mfano wa Raspberry Pi Zero 2 (kumbuka kurekebisha amri kulingana na toleo lako, hapa `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell kisha hukokotoa heshi SHA256 ya faili yako ya picha. Linganisha heshi hii na thamani inayolingana katika `seedsigner.0.8.6.sha256.txt`.




- Ikiwa maadili haya mawili yanafanana kabisa, hundi imefanikiwa na unaweza kuendelea.
- Ikiwa zinatofautiana, faili imeharibika au imeharibika. Usiitumie, na uanze kupakua tena.



![Image](assets/fr/013.webp)



Uthibitishaji uliofanikiwa unahakikisha kwamba faili yako ya `.img` ni ya kweli (iliyotiwa saini na SeedSigner) na haijabadilishwa (haijabadilishwa). Kisha unaweza kwenda kwa hatua inayofuata kwa usalama.



### 2.4. Flash picha



Ikiwa tayari huna, pakua programu ya [Balena Etcher] (https://etcher.balena.io/), kisha:




- Ingiza kadi ya microSD kwenye kompyuta yako.
- Zindua Etcher.
- Chagua faili ya `.img` iliyopakuliwa na kuthibitishwa.
- Chagua kadi ya microSD kama lengo.
- Bofya kwenye `Mweko!`.



![Image](assets/fr/014.webp)



Subiri hadi mchakato ukamilike: microSD yako iko tayari kutumika. Sasa ni wakati wa kusanyiko!



## 3. Mkusanyiko wa SeedSigner



Baada ya kadi yako ya microSD kutayarishwa na kumulika kwa programu ya SeedSigner, unaweza kuendelea na mkusanyiko wa mwisho. Chukua wakati wako, kwani sehemu zingine ni dhaifu (haswa kitambaa cha meza, kamera na pini za GPIO).



### 3.1 Kuandaa nyumba



Kwanza kabisa, fungua kesi yako. Hakikisha kuwa ni safi na kwamba hakuna plastiki iliyobaki ya uchapishaji ya 3D iliyo katika njia ya viungio vya ndani. Jihadharini na:




- Mahali pa kamera (shimo dogo la duara mbele).
- Ufunguzi wa skrini.
- Vipunguzo vya bandari ndogo za USB za Raspberry Pi Zero na slot ya microSD.



### 3.2 Ufungaji wa kamera



Tafuta kiunganishi cha utepe wa kamera kwenye Raspberry Pi Zero: ni ukanda mwembamba mweusi ulio kando ya ubao, ambao unaweza kuinuliwa kidogo ili kufunguka. Kuinua kwa uangalifu, bila kulazimisha: inapaswa tu kuinua milimita chache.



![Image](assets/fr/015.webp)



Ingiza kifuniko cha kamera. Sehemu ya kahawia/shaba inapaswa kutazama chini. Hakikisha kuwa imekaa imara kwenye kontakt, bila kupotosha.



![Image](assets/fr/016.webp)



Funga upau mweusi ili kufunga kitambaa cha meza (utahisi kubofya kidogo). Angalia kwa upole ikiwa inakaa mahali na haisogei.



![Image](assets/fr/017.webp)



Kisha weka moduli ya kamera kwenye shimo linalofaa kwenye nyumba. Kulingana na mfano, inaweza kuingia moja kwa moja au kuhitaji kamba ndogo ya wambiso ili kushikilia mahali pake. Lens lazima iwe sawa kabisa, inakabiliwa na nje.



### 3.3 Kusakinisha Raspberry Pi Zero



Ikiwa unatumia kesi, ingiza ubao wa Raspberry Pi Zero ndani. Sawazisha bandari kwa uangalifu na fursa zilizotolewa.



Kisha weka onyesho la Waveshare juu ya Raspberry Pi Zero. Pini za GPIO za Pi zinapaswa kushikamana kikamilifu na kiunganishi cha kike cha onyesho. Bonyeza onyesho polepole kwenye pini, ukiweka shinikizo hata kwa kila upande ili kuzuia kuzikunja.



![Image](assets/fr/018.webp)



Ikiwa una kesi, kamilisha mkusanyiko kwa kuongeza jopo la mbele na kijiti cha furaha.



Hatimaye, ingiza kadi ya microSD iliyo na programu iliyomulika kwenye eneo lililowekwa kingo la Raspberry Pi Zero. Hakikisha inabofya mahali pake.



### 3.4 Uanzishaji wa kwanza



Unganisha kebo ya umeme ya USB ndogo kwenye mlango maalum. Subiri kama dakika moja. Nembo ya SeedSigner inapaswa kuonekana, ikifuatiwa na skrini ya nyumbani.



![Image](assets/fr/019.webp)



Kuanza, hakikisha kuwa vipengele mbalimbali vinafanya kazi ipasavyo kwa kwenda kwenye menyu ya `Mipangilio > mtihani wa I/O`.



![Image](assets/fr/020.webp)



Jaribu vitufe vyote na uhakikishe vinajibu kwa usahihi. Kisha ubofye kitufe cha `KEY1` ili kuangalia kama kamera inafanya kazi inavyotarajiwa. Hii itachukua picha.



![Image](assets/fr/021.webp)



### 3.5 Marekebisho ya kamera



Kulingana na jinsi umepachika SeedSigner yako, kamera inaweza kuonyesha picha iliyogeuzwa. Ili kusahihisha hili, nenda kwa `Mipangilio > Kina > Kuzungusha kwa kamera` na uchague mzunguko wa 180° ikihitajika.



![Image](assets/fr/022.webp)



Ikiwa umebadilisha uelekeo wa kamera au ungependa kubadilisha mipangilio mingine (kama vile lugha ya kiolesura) baadaye, utahitaji kuwasha uendelevu wa mipangilio kwenye microSD. Vinginevyo, mipangilio yako itarudi kwa chaguo-msingi kila wakati unapowasha tena, kwani Raspberry Pi Zero haina kumbukumbu inayoendelea.



Ili kufanya hivyo, fungua menyu ya `Mipangilio > Mipangilio inayoendelea`, kisha uchague `Imewezeshwa`.



![Image](assets/fr/023.webp)



Ikiwa kila kitu kitafanya kazi, SeedSigner yako sasa iko tayari kutumika!



## 4. Mipangilio ya SeedSigner



Kabla ya kuunda Bitcoin wallet yako, hebu tuweke mipangilio ya SeedSigner. Kama inavyoendeshwa kwenye Raspberry Pi Zero bila kumbukumbu inayoendelea, mipangilio yake haihifadhiwi kiotomatiki isipokuwa ukiihifadhi kwenye kadi ya microSD. Kwa hivyo hakikisha kuwa umewezesha chaguo hili, vinginevyo mipangilio hii itapotea wakati wa kuwasha upya (angalia hatua ya 3.5).



### 4.1 Ufikiaji wa menyu ya parameta



Anzisha SeedSigner yako na usubiri skrini ya nyumbani kuonekana. Kwa kutumia kijiti cha furaha, nenda kwenye chaguo la `Mipangilio`, kisha uthibitishe kwa kubofya kitufe cha kati. Sasa unaingiza menyu kuu ya mipangilio.



![Image](assets/fr/024.webp)



### 4.2 Kuchagua programu ya usimamizi wa kwingineko



Kisha fikia menyu ya `Mratibu programu`.



![Image](assets/fr/025.webp)



`Mratibu` inarejelea programu ya usimamizi wa kwingineko ambayo SeedSigner yako itawasiliana nayo kupitia misimbo ya QR. Programu hii imewekwa ama kwenye kompyuta yako au kwenye smartphone yako. Itakuwezesha kudhibiti bitcoins zako, lakini bila kupata funguo zako za kibinafsi. SeedSigner inasalia kuwa kifaa pekee chenye uwezo wa kusaini miamala yako.



Toleo la sasa la firmware inasaidia programu kadhaa: Sparrow, Specter, BlueWallet, Nunchuk na Keeper. Katika kesi yangu, ninatumia **Sparrow Wallet **, ambayo ninapendekeza hasa kwa unyenyekevu wake na utendaji tajiri.



Ikiwa hujui jinsi ya kusakinisha, unaweza kufuata mafunzo haya:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Chagua tu programu unayopenda kutoka kwenye menyu.



![Image](assets/fr/026.webp)



### 4.3 Vitengo na onyesho la kiasi



Katika menyu ya `Onyesho la Madhehebu`, unaweza kuchagua kitengo ambacho kiasi kinaonyeshwa:




- `BTC`
- mBTC` (milli-bitcoin, au 0.001 BTC)
- gW-15 (satoshis, au 1/100,000,000 BTC)



Kitengo cha **sats** kwa ujumla ndicho kinachotumika zaidi kwa kiasi kidogo.



![Image](assets/fr/027.webp)



### 4.4 Mipangilio ya hali ya juu



Sasa nenda kwenye menyu ya `Advanced`. Hapa utapata chaguzi kadhaa muhimu:




- gW-17 network`: kurekebishwa ikiwa tu ungependa kutumia SeedSigner kwenye Testnet.
- msongamano wa msimbo wa qR`: hurekebisha kiasi cha maelezo yaliyo katika kila msimbo wa QR. Unaweza kuacha thamani chaguo-msingi, isipokuwa unaona ni vigumu kusoma unapochanganua.
- `Xpub export`: huwezesha au kulemaza utumaji wa ufunguo wako uliopanuliwa wa umma (`xpub`, `ypub`, `zpub`) kwa programu ya usimamizi wa jalada kupitia msimbo wa QR (utendaji ambao tutakuwa tukitumia baadaye, kwa hivyo uiache ikiwashwa kwa sasa).
- `Aina za hati`: inafafanua aina za hati zinazoruhusiwa kufunga bitcoins zako. Huna haja ya kurekebisha kigezo hiki, kwani aina ya hati itawekwa moja kwa moja kuwa Sparrow. Hapa, ni hati tu ambazo SeedSigner imeidhinishwa kudanganya ndizo zinazohusika.



### 4.5 Uchaguzi wa lugha



Hatimaye, katika menyu ya `Lugha`, unaweza kubadilisha lugha ya kiolesura ili kuendana na mapendeleo yako.



![Image](assets/fr/028.webp)



## 5. Kuunda na kuokoa seed



seed (au maneno ya mnemonic) huunda msingi wa kwingineko yako ya Bitcoin. Inatumika kupata funguo na anwani zako za kibinafsi, na hutoa ufikiaji wa pesa zako. SeedSigner inatoa njia kadhaa za kuitengeneza, ambayo tutaangalia katika sehemu hii.



Kabla ya kuanza, vikumbusho vichache muhimu:




- Kifungu hiki cha maneno kinakupa ufikiaji kamili, usio na kikomo wa bitcoins zako zote.** Mtu yeyote aliye na kifungu hiki cha maneno anaweza kuiba pesa zako, hata bila kufikia SeedSigner yako ;
- Kawaida, maneno ya maneno 12 hutumiwa kurejesha wallet katika tukio la kupoteza au wizi wa vifaa vya wallet. Lakini kwa kuwa SeedSigner ni kifaa *isiyo na utaifa*, haisajili seed yako kamwe. Kwa hivyo nakala zako halisi sio nakala rudufu tu, lakini **njia pekee ya kutumia wallet** yako. Ukipoteza nakala hizi, bitcoins zako zitapotea kabisa. Kwa hiyo zihifadhi kwa uangalifu, kwenye vyombo vya habari kadhaa na katika maeneo salama;
- Ikiwa ndio kwanza unaanza, ninakushauri sana usome mafunzo haya kwa ufahamu wa kina wa hatari zinazohusika katika kudhibiti kifungu cha maneno ya kumbukumbu:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Kufikia zana ya kuunda seed



Kutoka kwa skrini ya nyumbani ya SeedSigner, nenda kwenye menyu ya `Zana`.



![Image](assets/fr/029.webp)



Sasa utakuwa generate seed yako. seed ni nambari kubwa ya nasibu. Kadiri inavyotengenezwa kwa nasibu, ndivyo inavyokuwa salama zaidi. SeedSigner inatoa njia mbili za kufanya hivi:




- kamera": seed inatolewa kutokana na kelele inayoonekana ya picha. Unachukua picha ya mazingira nasibu (kitu, mandhari, uso, n.k.) ambayo tofauti za pikseli zinatumika kwa generate entropy. Ni njia ya haraka, lakini haiwezi kuzaliana tena.
- dice Rolls": unakunja kete ili kuunda entropy inayohitajika. Inatumia muda zaidi, lakini inaweza kuzaliana na kwa hivyo inaweza kuthibitishwa. Ukichagua njia hii, fuata ushauri katika mafunzo haya (hakuna haja ya kukokotoa checksum hapa, SeedSigner itashughulikia hilo):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Kuunda seed na picha



Ukichagua mbinu ya picha, bofya `Mpya seed` (na ikoni ya kamera), piga picha na uthibitishe. Kisha chagua urefu wa sentensi yako (maneno 12 au 24), ambayo itaonekana kwenye skrini ili kuokoa. Hatua zifuatazo ni sawa na sehemu ya 5.3.



### 5.3 Kuunda seed na kete



Katika somo hili, tunatumia njia ya **Kete Rolls**. Bofya kwenye `Mpya seed` (na ikoni ya kete).



![Image](assets/fr/030.webp)



Kisha chagua urefu wa kifungu chako cha mnemonic. Maneno 12 tayari yanatoa kiwango cha kutosha cha usalama, kwa hivyo hii ndio chaguo ninalopendekeza.



![Image](assets/fr/031.webp)



Pindua kete zako na uweke nambari zinazopatikana kwa kutumia mshale. Bonyeza kitufe cha katikati ili kuthibitisha kila ingizo. Ikiwa utafanya makosa, unaweza kurudi. Tumia kete kadhaa tofauti ili kupunguza ushawishi wa kete zisizo na usawa. Hakikisha hutazamwa wakati wa operesheni hii.



![Image](assets/fr/032.webp)



Mara tu unapoingiza kurusha zako 50, SeedSigner hutoa sentensi yako. **Fuata maagizo katika somo hili kwa uangalifu ikiwa ndio kwanza unaanza:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Kuonyesha na kuhifadhi seed



Andika kwa uangalifu maneno ya kifungu chako cha mnemonic kwenye usaidizi wa kimwili unaofaa (karatasi au chuma).



![Image](assets/fr/033.webp)



### 5.5 Kukagua nakala rudufu



Ili kuepuka hitilafu zozote za kuhifadhi nakala, SeedSigner inakuuliza uthibitishe nakala yako. Bofya kwenye `Thibitisha`.



![Image](assets/fr/034.webp)



Kisha ingiza neno lililoombwa kulingana na mpangilio wake katika sentensi. Kwa mfano, hapa sina budi kuchagua neno la tatu katika sentensi yangu.



![Image](assets/fr/035.webp)



Ukikosea, SeedSigner itakujulisha, na itabidi uanze tena, ukihakikisha kuwa umezingatia kifungu chako cha maneno ya kukumbuka wakati kinapopewa. Hatua hii ya uthibitishaji inahakikisha kuwa nakala yako ni sahihi na imekamilika. Baada ya kuthibitishwa, skrini itaonyesha `Nakala Imethibitishwa`.



![Image](assets/fr/036.webp)



Kwa jaribio kamili zaidi la urejeshaji, fuata mafunzo haya:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Kuelewa dhana ya "kifaa kisicho na hali



SeedSigner ni kifaa kisicho na kumbukumbu ya kudumu. Hii inamaanisha kuwa seed yako haihifadhiwi ndani ya kifaa (kwa mfano, Ledger, Trezor au Coldcard). Mara tu unapozima nguvu, seed hupotea kabisa kutoka kwa RAM yake. Unapoanzisha upya, SeedSigner inarudi katika hali tupu: basi itabidi uipe seed yako tena, ili iweze kusaini shughuli zako.



Hii inatoa ulinzi muhimu. Tofauti na pochi zingine za maunzi, SeedSigner inategemea Raspberry Pi Zero, ambayo haina ulinzi wa kimwili, ikiwa ni pamoja na *Secure Element*. Lakini kwa kuwa hakuna data nyeti iliyohifadhiwa, hata kifaa kilichoathiriwa hakiwezi kuruhusu mvamizi kutoa funguo zako za faragha au kutumia bitcoins zako.



Kwa upande mwingine, usanifu huu unamaanisha jukumu la ziada: bila chelezo, pesa zako zinapotea kabisa. Ndio maana ninapendekeza ** nakala rudufu **. Tayari una kifungu chako cha maneno ya urejeshi: hii ndiyo hifadhi yako kuu ya muda mrefu, itakayowekwa mahali salama. Sasa tutaunda nakala ya kifungu hiki kwa njia ya **msimbo wa QR**.



Kila wakati unapotumia SeedSigner, unachanganua msimbo huu wa QR kwa kamera ya kifaa ili ipakie kwa muda seed yako kwenye kumbukumbu yake unapotia saini katika miamala yako. Nakala hii ya pili, inayokusudiwa matumizi ya kila siku, lazima pia itunzwe kwa uangalifu mkubwa: mtu yeyote aliye na msimbo huu wa QR ana ufikiaji kamili wa bitcoins zako.


Pia nakushauri uhifadhi msimbo wako wa QR na maneno yako ya kumbukumbu katika sehemu mbili tofauti, ili kuepuka kupoteza kila kitu ikiwa kuna dai.



Hatimaye, njia mbadala ya juu zaidi na salama ni kutumia SeedSigner na **SeedKeeper**, ambayo huhifadhi seed katika secure element. Ili kujua zaidi, angalia mafunzo haya:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Andika alama za vidole muhimu muhimu



Baada ya uthibitishaji kukamilika, SeedSigner huonyesha alama ya kidole ya ufunguo mkuu wa wallet yako. Alama hii ya kidole inatambua wallet yako na inahakikisha kuwa unatumia maneno sahihi ya urejeshi katika siku zijazo. Haionyeshi maelezo yoyote kuhusu funguo zako za faragha, kwa hivyo unaweza kuihifadhi kwa njia ya dijitali kwa usalama. Hakikisha tu kwamba umehifadhi nakala inayoweza kufikiwa na usiwahi kuipoteza.



![Image](assets/fr/037.webp)



Pia ni katika hatua hii ambapo unaweza kuongeza **passphrase BIP39** ili kuimarisha usalama wa wallet yako. Kulingana na mkakati wako wa kuhifadhi nakala, chaguo hili linaweza kufaa, lakini pia linajumuisha hatari: ukipoteza passphrase, ufikiaji wa bitcoins zako utapotea kabisa.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Ikiwa bado haujafahamu dhana ya passphrase, ninakualika usome mafunzo haya ya kina kuhusu mada hii:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Kuhifadhi seed katika umbizo la QR (*SeedQR*)



SeedSigner hukuruhusu kubadilisha seed yako kuwa msimbo wa QR wa karatasi, unaoitwa *SeedQR*. Njia hii hurahisisha upakiaji upya wako wa wallet, kwani huepuka kuandika tena kila neno mwenyewe.



Ili kufanya hivyo, utahitaji karatasi tupu au msimbo wa chuma wa QR unaolingana na urefu wa maneno yako ya kumbukumbu. Ikiwa umenunua kifurushi kamili cha SeedSigner yako, violezo kawaida hujumuishwa. Ikiwa sivyo, unaweza kuzipakua na kuzichapisha (au kuzitoa kwa mkono) hapa:




- [muundo wa maneno 12](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [muundo wa maneno 24](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Muundo thabiti wa maneno 12](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Muundo thabiti wa maneno 24](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Kutoka kwenye skrini yako ya seed, chagua `Backup Seed`.



![Image](assets/fr/039.webp)



Kisha chagua `Hamisha kama SeedQR`.



![Image](assets/fr/040.webp)



Kisha chagua muundo unaotaka (wa kawaida au wa kuunganishwa) kulingana na template ya karatasi inapatikana.



![Image](assets/fr/041.webp)



Bofya `Anza` ili kuanza kuunda *SeedQR*. Kisha SeedSigner itaonyesha mfululizo wa gridi (A1, A2, B1, nk.), kila moja inayolingana na sehemu ya msimbo.



![Image](assets/fr/042.webp)



Tengeneza kwa uangalifu kila kitone cheusi kwenye laha yako, kisha utumie kijiti cha furaha ili kuendelea hadi sehemu inayofuata. Chukua muda wako: upangaji vibaya rahisi unaweza kufanya msimbo wa QR kutotumika.



Vidokezo vichache:




- Anza na penseli ili uweze kusahihisha makosa yoyote, kisha urudi kutumia kalamu nzuri nyeusi mara tu unapomaliza;
- Sehemu inayozingatia vizuri katikati ya mraba ndio unahitaji, hakuna haja ya kuijaza kabisa.



![Image](assets/fr/043.webp)



Kisha ubofye `Thibitisha SeedQR`, na uchanganue msimbo wako wa QR ili uhakikishe kuwa inafanya kazi ipasavyo.



![Image](assets/fr/044.webp)



Ikiwa ujumbe `Mafanikio` utaonyeshwa, *SeedQR* yako ni halali: unaweza kuendelea hadi hatua inayofuata.



![Image](assets/fr/045.webp)



**Weka laha hii kwa madhubuti kama maneno yako ya kurejesha akaunti. Mtu yeyote aliye na msimbo huu wa QR anaweza kuunda upya funguo zako za faragha na kuiba bitcoins zako.**



Hongera, jalada lako la Bitcoin sasa limeanza kutumika! Sasa tutaleta vipengele vyake vya umma katika **Sparrow Wallet** ili kuidhibiti kwa urahisi.



## 6. Ingiza wallet kwenye Sparrow



Baada ya SeedSigner yako kusanidiwa na seed yako kuzalishwa na kuhifadhiwa kwa usahihi, hatua inayofuata ni kuunganisha jalada hili na programu ya usimamizi kama vile Sparrow Wallet. seed yako itasalia nje ya mtandao kila wakati, kwani ni sehemu ya umma pekee ya kwingineko yako itatumwa kwa Sparrow. Hii itawezesha programu kuonyesha anwani zako, miamala na kuunda miamala mpya, bila kuwa na uwezo wa kutumia bitcoins zako. Ili kutumia bitcoins zako, SeedSigner yako italazimika kusaini muamala uliotayarishwa na Sparrow kila wakati.



### 6.1 Kutayarisha Kiashiria cha Mbegu



Ingiza microSD iliyo na mfumo wa uendeshaji, washa SeedSigner yako, kisha pakia seed ambayo umeunda hivi punde kutoka kwa msimbo wako wa QR. Kwenye Skrini ya Nyumbani, chagua `Scan`, kisha changanua SeedQR yako na SeedSigner.



![Image](assets/fr/046.webp)



Hakikisha kuwa alama ya kidole kwenye ufunguo mkuu wako inalingana na alama ya kidole kwenye wallet yako. Ikiwa unatumia passphrase, iingize katika hatua hii.



![Image](assets/fr/047.webp)



Hii inakupeleka kwenye menyu ya kwingineko yako, katika kesi yangu inayoitwa `d4149b27`. Ikiwa umerejea kwenye skrini ya kwanza, chagua `Mbegu`, kisha uchague chapisho linalolingana na kwingineko yako. Kisha bonyeza `Hamisha Xpub`.



![Image](assets/fr/048.webp)



Chagua aina ya kwingineko. Kwa upande wetu, ni kwingineko moja: chagua `Sig Moja`.



![Image](assets/fr/049.webp)



Inayofuata inakuja uchaguzi wa kiwango cha uandishi. Ya hivi karibuni na ya kiuchumi zaidi katika suala la gharama za ununuzi ni `Taproot`. Kwa hiyo nakushauri kuchagua kiwango hiki.



![Image](assets/fr/050.webp)



Ujumbe wa onyo utaonekana. Hii ni kawaida: ufunguo huu wa umma uliopanuliwa (`xpub`) hukuruhusu kutazama anwani zote zinazotokana na seed yako (kwenye akaunti ya kwanza). Haikuruhusu kutumia pesa zako, lakini inafichua muundo wa kwingineko yako. Iwapo itavuja, ni tatizo kwa faragha yako, lakini si kwa usalama wa bitcoins zako: inakuwezesha kuziona, lakini si kuzitumia.



Bofya `Naelewa`, kisha `Hamisha Xpub` ikiwa umeridhika na maelezo yanayoonyeshwa.



SeedSigner kisha hutengeneza xpub yako katika mfumo wa msimbo unaobadilika wa QR ulio na data yote unayohitaji ili kudhibiti kwingineko yako katika Sparrow Wallet.



![Image](assets/fr/051.webp)



Unaweza kutumia kijiti cha kufurahisha kurekebisha mwangaza wa skrini kwa uchanganuzi wa msimbo wa QR kwa urahisi.



### 6.2 Kuagiza kwingineko mpya kwenye Sparrow Wallet



Hakikisha kuwa umesakinisha programu ya Sparrow Wallet kwenye kompyuta yako. Ikiwa hujui jinsi ya kupakua, angalia na usakinishe kwa usahihi, angalia mafunzo yetu kamili juu ya somo:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kwenye kompyuta yako, fungua Sparrow Wallet, kisha kwenye upau wa menyu, bofya `Faili → Leta Wallet`.



![Image](assets/fr/052.webp)



Tembeza chini hadi `SeedSigner`, kisha uchague `Scan...`. Kamera yako ya wavuti itafunguka: changanua msimbo unaobadilika wa QR unaoonyeshwa kwenye skrini yako ya SeedSigner.



![Image](assets/fr/053.webp)



Weka jina kwa kwingineko yako, kisha ubofye `Unda Wallet`. Sparrow itakuuliza uweke nenosiri ili kufunga ufikiaji wa ndani kwa wallet hii. Chagua nenosiri thabiti: hulinda ufikiaji wa data yako ya kwingineko katika Sparrow (funguo za umma, anwani, lebo na historia ya muamala). Nenosiri hili halihitajiki ili kurejesha kwingineko baadaye: maneno yako ya mnemonic pekee (na ikiwezekana passphrase yako) ndiyo yanahitajika kwa madhumuni haya.



Ninapendekeza kwamba uhifadhi nenosiri hili kwenye kidhibiti nenosiri ili kuepuka kulipoteza.



![Image](assets/fr/054.webp)



Hifadhi yako ya vitufe sasa imeingizwa kwa ufanisi.



![Image](assets/fr/055.webp)



Kisha hakikisha kwamba `alama ya vidole kuu` iliyoonyeshwa katika Sparrow inalingana na ile iliyotajwa hapo awali kwenye SeedSigner yako.



SeedSigner yako na Sparrow Wallet sasa zimeunganishwa kwa usalama. Sparrow hufanya kama kiolesura kamili cha usimamizi, ilhali SeedSigner inasalia kuwa kifaa pekee chenye uwezo wa kusaini miamala yako. Sasa uko tayari kupokea na kutuma bitcoins katika usanidi usio na hewa kabisa.



## 7. Kupokea na kutuma bitcoins



SeedSigner yako na Sparrow Wallet sasa zimesanidiwa kufanya kazi pamoja. Katika sehemu hii ya mwisho, tutaangalia jinsi ya kupokea na kutuma bitcoins kwa kutumia usanidi huu.



### 7.1 Kupokea bitcoins



#### 7.1.1 Kuzalisha anwani ya mapokezi



Kwenye kompyuta yako, fungua Sparrow Wallet na ufungue SeedSigner wallet yako kwa kutumia nenosiri lako. Hakikisha programu imeunganishwa kwenye seva (notch chini kulia). Kwenye upau wa kando, bofya kwenye `Pokea`.



![Image](assets/fr/056.webp)



Anwani mpya ya Bitcoin inaonyeshwa. Utaona:




- Anwani ya maandishi (kuanzia na `bc1p...` ikiwa unatumia P2TR kama mimi),
- Nambari ya QR inayolingana,
- Sehemu ya `Lebo` ya kufuatilia miamala yako.



Ninapendekeza sana uongeze lebo kwa kila risiti ya bitcoin kwenye wallet yako. Hii itakuruhusu kutambua kwa urahisi asili ya kila UTXO na kuboresha usimamizi wako wa faragha. Ili kutafakari kwa kina mada hii muhimu, unaweza kuangalia mafunzo maalum kuhusu Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Ili kuongeza lebo, ingiza tu jina katika sehemu ya `Lebo`, kisha uthibitishe.



Kwa mfano:



```txt
Label : Sale of the Raspberry Pi Zero
```



Anwani yako sasa inahusishwa na lebo hii katika sehemu zote za Sparrow.



![Image](assets/fr/057.webp)



#### 7.1.2 uthibitishaji wa Address kwenye Kiashiria cha mbegu



Kabla ya kushiriki anwani yako ya kupokea, ni muhimu sana kuangalia kwamba ni ya seed yako. Hatua hii inahakikisha kwamba SeedSigner yako itaweza kutia sahihi miamala inayohusishwa na anwani hii. Pia hulinda dhidi ya mashambulizi yanayoweza kutokea ambapo Sparrow huonyesha anwani ya ulaghai. Kumbuka kwamba Sparrow inaendeshwa kwenye mazingira yasiyo salama (kompyuta yako), ambayo ina sehemu kubwa ya mashambulizi kuliko SeedSigner yako, ambayo imetengwa kabisa. Ndio maana hupaswi kamwe kuamini kwa upofu anwani za kupokea zinazowasilishwa kwenye Sparrow hadi utakapozithibitisha kwa maunzi yako ya wallet.



Kwenye Sparrow, bofya kwenye msimbo wa QR wa anwani ili kuikuza: kisha itaonyeshwa skrini nzima.



![Image](assets/fr/058.webp)



Kwenye SeedSigner yako, kutoka kwa menyu kuu, chagua `Scan`. Changanua msimbo wa QR unaoonyeshwa kwenye skrini ya kompyuta yako, kisha uchague seed inayolingana na wallet yako (kwa upande wangu, alama ya kidole `d4149b27`).



![Image](assets/fr/059.webp)



Ikiwa anwani iliyochanganuliwa inalingana na ile inayotokana na seed yako, skrini ya SeedSigner itaonyesha ujumbe: `Address Imethibitishwa`.



![Image](assets/fr/060.webp)



Hii inathibitisha kwamba anwani ni ya wallet yako na kwamba unaweza kupokea bitcoins kwa ujasiri kutoka kwayo.



#### 7.1.3 Kupokea fedha



Sasa unaweza kuwasiliana na anwani hii (kwa maandishi au fomu ya msimbo wa QR) kwa mtu au idara inayohitaji kukutumia satss. Muamala ukishatangazwa kwenye mtandao, utaonekana kwenye kichupo cha `Miamala` cha Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Tuma bitcoins



Kutuma bitcoins na SeedSigner ni mchakato wa hatua 3:




- Uundaji wa shughuli katika Sparrow;
- Sahihi ya shughuli kwenye SeedSigner;
- Usambazaji wa mwisho wa muamala kupitia Sparrow.



Ubadilishanaji wote kati ya vifaa hivi viwili hufanywa kwa kutumia misimbo ya QR pekee.



#### 7.2.1 Kuunda shughuli katika Sparrow



Katika Sparrow Wallet, unaweza kubofya kichupo cha `Tuma` kwenye upau wa upande wa kushoto. Walakini, napendelea kutumia kichupo cha `UTXOs`, ambacho hukuruhusu kufanya mazoezi ya "*Coin Control*". Njia hii hukupa udhibiti kamili wa UTXO zinazotumiwa, ili uweze kudhibiti maelezo unayofichua wakati wa muamala.



Katika kichupo cha `UTXOs`, chagua sarafu unazotaka kutumia, kisha ubofye `Tuma Zilizochaguliwa`.



![Image](assets/fr/062.webp)



Kisha jaza sehemu za muamala:




- Katika `Lipa kwa`, bandika anwani ya mpokeaji au ubofye aikoni ya kamera ili kuchanganua msimbo wa QR;
- Katika `Lebo`, ongeza lebo ili kufuatilia gharama hii;
- Katika `Kiasi`, weka kiasi kitakachotumwa;
- Hatimaye, chagua kiwango cha ada kulingana na hali ya sasa ya soko (makadirio yanapatikana katika [mempool.space](https://mempool.space/)).



Mara sehemu zitakapokamilika, angalia maelezo kwa makini, kisha ubofye `Unda Muamala >>`.



![Image](assets/fr/063.webp)



Angalia maelezo ya muamala ili kuhakikisha kuwa kila kitu ni sahihi, kisha ubofye `Maliza Muamala kwa Kutia Saini`.



![Image](assets/fr/064.webp)



Muamala sasa uko tayari, lakini bado haujatiwa saini. Ili kuonyesha [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) kama msimbo wa QR, bofya `Onyesha QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Kusaini muamala na SeedSigner



Washa SeedSigner yako na uchanganue SeedQR yako ili kufikia kwingineko yako, kama kawaida. Kutoka kwa skrini ya kwanza, chagua `Changanua`, kisha uchanganue msimbo wa QR unaoonyeshwa kwenye Sparrow.



![Image](assets/fr/066.webp)



Kisha chagua seed ili kufanana na kwingineko yako.



![Image](assets/fr/067.webp)



SeedSigner hugundua kiotomatiki kuwa hii ni PSBT na kuonyesha muhtasari wa muamala:




   - Kiasi kilichotumwa,
   - Anwani za pato,
   - Gharama zinazohusiana za manunuzi.



Bofya kwenye `Maelezo ya Kagua` na uangalie kwa makini taarifa zote moja kwa moja kwenye skrini ya SeedSigner. Vipengee muhimu zaidi vya kuangalia ni kiasi kilichotumwa, anwani ya mpokeaji na kiasi cha gharama zinazotumika.



![Image](assets/fr/068.webp)



Ikiwa kila kitu kiko sawa, chagua `Idhinisha PSBT` ili kutia sahihi muamala kwa kutumia vitufe vinavyolingana vya faragha.



![Image](assets/fr/069.webp)



Baada ya kusainiwa, SeedSigner hutengeneza msimbo mpya wa QR ulio na shughuli iliyotiwa saini, tayari kuchanganuliwa na Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Kutangaza muamala kutoka Sparrow



Sasa kwa kuwa shughuli hiyo ni halali, inahitaji kutangazwa kwenye mtandao wa Bitcoin, ili kufikia mchimbaji ambaye ataiongeza kwenye kizuizi.



Kwenye Sparrow, bofya `QR Scan`.



![Image](assets/fr/071.webp)



Wasilisha msimbo wa QR unaoonyeshwa na SeedSigner yako (ile ya shughuli iliyotiwa saini) kwenye kamera ya wavuti. Sparrow itasimbua saini na kuonyesha maelezo kamili ya muamala. Fanya ukaguzi wa mwisho kwamba maelezo yote ni sahihi, kisha ubofye Muamala wa Matangazo ili kuyatangaza kwenye mtandao wa Bitcoin.



![Image](assets/fr/072.webp)



Muamala wako sasa umetumwa kwa mtandao wa Bitcoin. Unaweza kufuata maendeleo yake katika kichupo cha `Miamala` cha Sparrow Wallet.



![Image](assets/fr/073.webp)



Sasa umefahamu misingi ya kutumia SeedSigner. Ili kuongeza maarifa yako na kuchunguza matumizi ya hali ya juu zaidi, ninakualika uangalie mafunzo yafuatayo:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Unaweza pia kusaidia ukuzaji wa mradi wa chanzo huria wa SeedSigner kwa kutoa mchango katika bitcoins!](https://seedsigner.com/donate/)**



*Mikopo: baadhi ya picha katika mafunzo haya zinatoka kwa [tovuti rasmi ya mradi wa SeedSigner](https://seedsigner.com/) na [hazina ya GitHub](https://github.com/SeedSigner/seedsigner).*