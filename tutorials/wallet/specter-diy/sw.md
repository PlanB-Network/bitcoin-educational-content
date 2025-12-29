---
name: Specter DIY
description: Mwongozo wa kusanidi kwa Specter DIY
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunks kuandika code. Tunajua kwamba lazima mtu aandike programu ili kutetea faragha, na kwa kuwa hatuwezi kupata faragha isipokuwa sote tufanye hivyo, tutaiandika.

*Manifesto ya Cypherpunk - Eric Hughes - 9 Machi 1993*


Wazo la mradi ni kujenga vifaa vya wallet kutoka kwa vipengele vya nje ya rafu.

Ijapokuwa tuna ubao wa upanuzi ambao huweka kila kitu katika hali nzuri na kukusaidia kuzuia kutengenezea, tutaendelea kusaidia na kudumisha upatanifu na vipengee vya kawaida.


![image](assets/fr/01.webp)


Pia tunataka kuweka mradi kuwa rahisi ili uweze kufanya kazi kwenye seti nyingine yoyote ya vipengele na mabadiliko madogo. Labda unataka kutengeneza vifaa vya wallet kwenye usanifu tofauti (RISC-V?), na modem ya sauti kama njia ya mawasiliano - unapaswa kuwa na uwezo wa kuifanya. Inapaswa kuwa rahisi kuongeza au kubadilisha utendakazi wa Specter na tunajaribu kutoa moduli za kimantiki kadri tuwezavyo.


Misimbo ya QR ni njia chaguomsingi ya Specter kuwasiliana na mwenyeji. Misimbo ya QR ni rahisi sana na huruhusu mtumiaji kudhibiti utumaji data - kila msimbo wa QR una uwezo mdogo sana na mawasiliano hufanyika moja kwa moja. Na ni airgapped - huna haja ya kuunganisha wallet kwa kompyuta wakati wowote.


Kwa hifadhi ya siri tunaauni hali ya agnostic (wallet husahau siri zote inapozimwa), hali ya kutojali (huhifadhi siri katika flash ya kidhibiti kidogo cha programu) na ushirikiano wa secure element unakuja hivi karibuni.


Lengo letu kuu ni kuweka saini nyingi na pochi zingine za maunzi, lakini wallet pia inaweza kufanya kazi kama mtu aliyetia sahihi moja. Tunajaribu kuifanya ilingane na Bitcoin Core ambapo tunaweza - PSBT kwa miamala ambayo haijasainiwa, vielezi vya wallet vya kuagiza/kusafirisha pochi nyingi. Ili kuwasiliana na Bitcoin Core kwa urahisi zaidi pia tunashughulikia [programu ya Eneo-kazi la Specter](https://github.com/cryptoadvance/specter-desktop) - seva ndogo ya chupa ya chatu inayozungumza na nodi yako ya Bitcoin Core.


Firmware nyingi zimeandikwa katika MicroPython ambayo inafanya msimbo kuwa rahisi kukagua na kubadilisha. Tunatumia maktaba ya [secp256k1](https://github.com/bitcoin-core/secp256k1) kutoka Bitcoin Core kwa hesabu za curve duaradufu na [LittlevGL](https://lvgl.io/) maktaba ya GUI.


## Kanusho


Mradi umekomaa kwa kiasi kikubwa, kwa kiwango ambacho kiwango cha usalama cha Specter-DIY sasa kinalinganishwa na pochi za vifaa vya kibiashara kwenye soko. Tulitekeleza programu salama ya bootloader ambayo inathibitisha uboreshaji wa programu dhibiti, kwa hivyo unaweza kuwa na uhakika kwamba programu dhibiti iliyotiwa sahihi pekee ndiyo inaweza kupakiwa kwenye kifaa baada ya usanidi wa awali. Hata hivyo, tofauti na vifaa vya kutia sahihi vya kibiashara, kipakiaji kisimamizi lazima kisakinishwe na mtumiaji na hakijawekwa katika kiwanda cha mchuuzi wa kifaa. Kwa hivyo, zingatia zaidi wakati wa usakinishaji wa programu dhibiti wa awali na uhakikishe kuwa umethibitisha saini za PGP na uwashe programu dhibiti kutoka kwa kompyuta salama.


Ikiwa kitu hakitafanikiwa fungua tatizo hapa au uulize swali katika [kundi letu la Telegramu](https://t.me/+VEinVSYkW5TUl5Ai).


## Orodha ya ununuzi ya Specter-DIY


Hapa tunaelezea nini cha kununua, na katika kusanyiko sehemu inayofuata tunaelezea jinsi ya kuiweka pamoja na maelezo machache kuhusu bodi - jumpers za nguvu, bandari za USB nk.


### Bodi ya ugunduzi


Sehemu kuu ya kifaa ni bodi ya wasanidi programu:



- Bodi ya wasanidi wa STM32F469I-DISCO (yaani kutoka kwa [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) au [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Kebo ndogo ** USB
- Kebo ya kawaida ya MicroUSB ili kuwasiliana kupitia USB


Hiari lakini inapendekezwa:


- [Waveshare kichanganuzi cha msimbo wa QR](https://www.waveshare.com/barcode-scanner-module.htm) chenye vichwa virefu vya pini kama vile [hizi](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) au [hizi](https://www.amazon.com/gp/product/B015KA0RRU/) ili kuunganisha kichanganuzi kwenye ubao (vichwa 4 vya pini vinahitajika).


Kwa sasa tunafanyia kazi ubao wa kiendelezi unaojumuisha nafasi ya smartcard, kichanganuzi cha msimbo wa QR, betri na kipochi cha 3d, lakini haijumuishi sehemu kuu - ubao wa uvumbuzi ambao unahitaji kuagiza kando. Kwa njia hii shambulio la mnyororo wa usambazaji bado sio suala kwani vipengee muhimu vya usalama hununuliwa kutoka kwa duka la kielektroniki la nasibu.


Unaweza kuanza kutumia Specter hata bila vijenzi vyovyote vya ziada, lakini utaweza kuwasiliana nayo kupitia USB au sehemu ya kadi ya SD iliyojengewa ndani. Kutumia Specter juu ya USB inamaanisha kuwa haijawekwa hewani kwa hivyo unapoteza mali muhimu ya usalama.


### Kichanganuzi cha QR


Kwa kichanganuzi cha msimbo wa QR una chaguo kadhaa.


**Chaguo la 1. Limependekezwa.** Kichanganuzi kizuri kabisa kutoka Waveshare ($40)


[Kichanganuzi cha Waveshare](https://www.waveshare.com/barcode-scanner-module.htm) - utahitaji kutafuta njia ya jinsi ya kuiweka vizuri, labda utumie aina fulani ya ngao ya Arduino Prototype na bata.


Hakuna soldering inahitajika, lakini ikiwa una ujuzi wa soldering unaweza kufanya njia ya wallet kuwa nzuri zaidi;)


**Chaguo la 2.** Kichanganuzi kizuri sana kutoka kwa Microe lakini ghali sana (150$):


[Bofya Msimbo Pau](https://www.mikroe.com/barcode-click) + [Adapter](https://www.mikroe.com/arduino-uno-click-shield)


**Chaguo la 3.** Kichanganuzi kingine chochote cha QR


Unaweza kupata scanners za bei nafuu nchini Uchina. Ubora wao mara nyingi sio mzuri sana, lakini unaweza kuchukua nafasi. Labda hata ESPCamera ingefanya kazi hiyo. Unahitaji tu kuunganisha nguvu, UART (pini D0 na D1), na uanzishe hadi D5.


**Chaguo la 4.** Hakuna kichanganuzi.


Basi unaweza tu kutumia Specter na USB / SD Kadi.


Isipokuwa ukitengeneza moduli yako ya mawasiliano inayotumia kitu kingine badala ya misimbo ya QR - modem ya sauti, bluetooth au chochote kingine. Mara tu inaweza kuanzishwa na kutuma data kwa serial unaweza kufanya chochote unachotaka.


### Vipengele vya hiari


Ukiongeza benki ndogo ya umeme au betri na chaja/booster ya umeme, wallet yako itatosheka kabisa ;)



## Mkutano wa Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Inaunganisha kichanganuzi cha Msimbo Pau wa Waveshare


Firmware ya wallet itakuwekea kichanganuzi mara ya kwanza, kwa hivyo hakuna usanidi wa mwongozo unaohitajika.


Hivi ndivyo unavyounganisha kichanganuzi kwenye ubao:


![image](assets/fr/02.webp)


Kwa urahisi unaweza kununua ngao ya Protype ya Arduino na solder na kuweka kila kitu juu yake (yaani [hii](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Usimamizi wa nguvu


Kwenye upande wa juu wa ubao kuna jumper ambayo inafafanua ambapo itachukua nguvu. Unaweza kubadilisha nafasi ya kirukaji na uchague chanzo cha nishati kuwa mojawapo ya milango ya USB au pini ya VIN na uunganishe betri ya nje hapo (inapaswa kuwa 5V).


### Sehemu ya ndani ya DIY


Angalia folda ya [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Kuwa mbunifu!


Kusanya Specter-DIY yako mwenyewe na ututumie picha (fanya ombi la kuvuta au uwasiliane nasi).


Angalia [Nyumba ya sanaa](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) iliyo na Specters zilizokusanywa na jumuiya!




## Inasakinisha msimbo uliokusanywa


Pamoja na salama bootloader ufungaji wa awali wa firmware ni tofauti kidogo. Uboreshaji ni rahisi na hauhitaji kuunganisha maunzi wallet kwenye kompyuta.


![video](https://youtu.be/eF4cgK_L6T4)


### Inamulika programu dhibiti ya awali


**Kumbuka** Iwapo hutaki kutumia jozi kutoka kwa matoleo angalia [hati ya bootloader](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) inayofafanua jinsi ya kuikusanya na kuisanidi ili kutumia funguo zako za umma badala ya zetu.



- Ikiwa unasasisha kutoka matoleo yaliyo chini ya `1.4.0` au unapakia programu dhibiti kwa mara ya kwanza, tumia `initial_firmware_<version>.bin` kutoka kwa ukurasa wa [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Thibitisha saini ya faili ya `sha256.signed.txt` dhidi ya [ufunguo wa PGP wa Stepan](https://stepansnigirev.com/ss-specter-release.asc)
 - Thibitisha heshi ya `initial_firmware_<version>.bin` dhidi ya heshi iliyohifadhiwa katika `sha256.signed.txt`
- Ikiwa unasasisha kutoka kwa bootloader tupu au unaona ujumbe wa hitilafu ya bootloader kwamba programu dhibiti si halali, angalia sehemu inayofuata - Firmware ya Specter iliyosainiwa ya Flashing.
- Hakikisha kuwa kiruka nguvu cha ubao wako wa uvumbuzi kiko katika nafasi ya STLK
- Unganisha ubao wa ugunduzi kwenye kompyuta yako kupitia kebo ya **USB mini** iliyo juu ya ubao.
    - Ubao unapaswa kuonekana kama diski inayoweza kutolewa inayoitwa `DIS_F469NI`.
- Nakili faili ya `initial_firmware_<version>.bin` kwenye mzizi wa mfumo wa faili `DIS_F469NI`.
- Wakati ubao umekamilika kuangaza firmware bodi itajiweka upya na kuwasha upya bootloader. Bootloader itaangalia firmware na boot kwenye firmware kuu. Ukiona ujumbe wa hitilafu ambao hakuna firmware inayopatikana - fuata maagizo ya sasisho na upakie firmware kupitia kadi ya SD.
- Sasa unaweza kubadili kiruka nguvu mahali unapoipenda na uwashe ubao kutoka kwa powerbank au betri.


Kumulika programu dhibiti ya awali kupitia kunakili-bandika faili ya `.bin` wakati mwingine hushindwa - mara nyingi kwa sababu ya kebo, au ukiunganisha kifaa kupitia kitovu cha USB. Katika kesi hii unaweza kujaribu mara chache zaidi (kawaida hufanya kazi katika majaribio 2-3).


Ikishindikana kila wakati unaweza kutumia [stlink](https://github.com/stlink-org/stlink/releases/latest) zana ya chanzo-wazi. Isakinishe na uandike kwenye terminal yako: `st-flash andika <path/to/initial_firmare.bin> 0x8000000`. Kawaida hufanya kazi ya kuaminika zaidi.


### Inaboresha programu dhibiti



- Pakua `specter_upgrade_<version>.bin` kutoka kwa [toleo](https://github.com/cryptoadvance/specter-diy/releases).
- Nakili binary hii kwenye mzizi wa kadi ya SD (iliyoumbizwa FAT, 32 GB max)
 - Hakikisha faili moja tu ya `specter_upgrade***.bin` iko kwenye saraka ya mizizi
- Ingiza kadi ya SD kwenye nafasi ya SD ya ubao wa uvumbuzi na uwashe nguvu ubaoni
- Bootloader itawasha firmware na itakujulisha itakapokamilika.
- Washa upya ubao - utaona kiolesura cha Specter-DIY sasa, itakupendekeza uchague PIN yako


Wakati wowote toleo jipya limetoka, pakua tu `specter_upgrade_<version>.bin` kutoka kwa matoleo, idondoshe kwenye kadi ya SD na upate toleo jipya la kifaa kama katika hatua ya awali. Bootloader itahakikisha programu dhibiti iliyosainiwa pekee ndiyo inaweza kupakiwa kwenye ubao.


### Jinsi ya kujua toleo la firmware


Nenda kwenye menyu ya `Mipangilio ya Kifaa` - itaonyesha nambari ya toleo chini ya kichwa cha skrini.


## Tumia Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Usalama wa Specter-DIY


### Vifaa


Onyesho linadhibitiwa na programu ya MCU.


Ushirikiano wa kipengele salama bado haupo - kwa sasa siri pia zimehifadhiwa kwenye MCU kuu. Lakini unaweza kutumia wallet bila kuhifadhi siri - unahitaji kuingiza maneno yako ya kurejesha kila wakati. Kwa nini kukumbuka muda mrefu wa passphrase ikiwa unaweza kukumbuka mnemonic nzima?


Kifaa hutumia mweko wa nje kuhifadhi baadhi ya faili (QSPI), lakini faili zote za watumiaji hutiwa saini na wallet na kuangaliwa zinapopakiwa.


Utendaji wa kuchanganua QR uko kwenye kidhibiti kidogo tofauti kwa hivyo uchakataji wa picha zote hufanyika nje ya MCU muhimu kwa usalama. Kwa sasa USB na kadi ya SD bado inadhibitiwa na MCU kuu, kwa hivyo usitumie kadi ya SD na USB ikiwa ungependa kupunguza eneo la mashambulizi.


### Ulinzi wa PIN (uthibitishaji wa mtumiaji)


Wakati wa boot ya kwanza siri ya kipekee inatolewa kwenye MCU kuu. Siri hii inakuwezesha kuthibitisha kuwa kifaa hakijabadilishwa na kibaya - unapoingiza msimbo wa PIN unaona orodha ya maneno ambayo yatabaki sawa wakati siri iko.


Msimbo wako wa PIN pamoja na siri hii ya kipekee hutumiwa kwa generate ufunguo wa kusimbua kwa funguo zako za Bitcoin (kama utazihifadhi). Kwa hivyo ikiwa mvamizi ataweza kukwepa skrini ya PIN, utembuaji bado hautafaulu.


Ikiwa umefunga firmware (TODO: ongeza kiungo cha maelekezo hapa) itafunga kwa ufanisi siri pia, hivyo ikiwa mshambuliaji ataangaza firmware tofauti kwenye ubao siri itafutwa na utaweza kuitambua unapoanza kuingiza msimbo wa PIN - mlolongo wa maneno utakuwa tofauti.


### Kizazi cha maneno ya kurejesha


Hii ni moja ya sehemu muhimu zaidi za wallet - hadi generate ufunguo salama. Ili kufanya hivyo vizuri tunatumia vyanzo vingi vya entropy:



- TRNG ya microcontroller. Inamilikiwa, imeidhinishwa na pengine nzuri lakini hatuiamini
- Skrini ya kugusa. Kila wakati unapogusa skrini tunapima mahali na wakati ambapo mguso huu ulifanyika (katika tiki za microcontroller saa 180MHz).
- Maikrofoni zilizojengwa ndani - bado. Ubao una maikrofoni mbili, kwa hivyo maunzi ya wallet yanaweza kukusikiliza na kuchanganya data hii kwenye bwawa la entropy.


Entropy hii yote inaharakishwa pamoja na kubadilishwa kuwa kifungu chako cha urejeshi. Entropy inayosababishwa daima ni bora kuliko vyanzo vyovyote vya mtu binafsi.


### Kiwango cha juu mantiki - pochi


Specter hufanya kazi kama hifadhi kuu. Ina funguo za faragha za HD ambazo zinaweza kuhusika katika pochi. Pochi hufafanuliwa na maelezo yao. Tunaunga mkono maandishi madogo pia.


Kila wallet ni ya mtandao fulani. Hii ina maana kwamba ikiwa ulileta wallet kwenye `testnet` haitapatikana kwenye `mainnet` au `regtest` - unahitaji kubadili hadi mtandao huu na kuleta wallet tofauti.


### Uthibitishaji wa miamala


Sheria zifuatazo zinatumika kwa miamala ambayo wallet itatia saini:



- ikiwa pembejeo mchanganyiko kutoka kwa pochi tofauti zitapatikana mtumiaji huonywa ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- matokeo ya mabadiliko yanaonyesha jina la wallet wanayotumwa
- ili kutumia maandishi mengi au maandishi madogo kwanza unahitaji kuleta wallet kwa kuongeza kifafanuzi cha wallet (zaidi ya QR, USB au kadi ya SD)


## Usaidizi wa maelezo


Vifafanuzi vyote vya kawaida vya Bitcoin hufanya kazi. Kando na hayo tunayo viendelezi vichache:


### Matawi mengi katika maelezo


Ili kuhifadhi nafasi katika misimbo ya QR tunaruhusu kuongeza vifafanuzi vyenye matawi mengi kwa mkupuo mmoja. Iwapo ungependa kutumia `wpkh(xpub/0/*)` kwa ajili ya kupokea anwani na `wpkh(xpub/1/*)` kwa anwani za kubadilisha unaweza kuzichanganya katika kifafanuzi kimoja: `wpkh(xpub/{0,1}/*)` - wallet itachukulia faharasa ya kwanza ya `{}` seti ya sehemu kama anwani ya pili ya kupokea anwani.


Unaweza pia kutaja zaidi ya matawi mawili, na faharisi za matawi zinaweza kuwa tofauti kwa watia saini tofauti, kwa hivyo maelezo haya ni ya kushangaza sana lakini ni halali kabisa:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Hapa kwa kupokea nambari ya anwani 17 wallet itatumia hati kutoka `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


Sharti pekee ni kwamba idadi ya faharisi katika seti zote ni sawa (3 katika kesi hapo juu).


### Mito chaguomsingi


Iwapo kifafanuzi kina funguo kuu za umma lakini hakina viambajengo vya kadi-mwitu, chimbuko chaguomsingi `/{0,1}/*` kitaongezwa kwa vitufe vyote vilivyopanuliwa katika kifafanuzi. Ikiwa angalau moja ya xpub ina chimbuko la kadi-mwitu kifafanuzi hakitabadilishwa.


Kifafanuzi `wpkh(xpub)` kitabadilishwa kuwa `wpkh(xpub/{0,1}/*)`.


### Hati ndogo


Specter hutumia hati ndogo, lakini haitumii utungaji wa sera-hadi-mini (kwa sababu ni ghali sana). Tunakagua baadhi ya nakala, kwa hivyo ni hati `B` pekee zinazoruhusiwa kwenye kiwango cha juu na hoja zote katika hati ndogo lazima ziwe na sifa kulingana na [spec](http://bitcoin.sipa.be/miniscript/).


Unaweza kutumia [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) kwa generate kifafanuzi kutoka kwa sera na kisha kuiingiza kwa wallet.


Kwa mfano, sera "Ninaweza kutumia sasa, au katika siku 100 mke wangu anaweza kutumia" inaweza kubadilishwa kuwa wallet kama hivyo:


Sera: `au(9@pk(xpubA),na(wakubwa(14400),pk(B)))` (ufunguo wangu una uwezekano wa mara 9)


Hati ndogo: `au_d(pk(xpubA),na_v(v:pkh(xpubB),ya zamani(14400)))`


Descriptor: `wsh(au_d(pk(xpubA),na_v(v:pkh(xpubB),mzee(14400))))`


Kwa vile hapa hatuna vinyago vyovyote vya kadi-mwitu vitoleo chaguomsingi vya `/{0,1}/*` vitaambatishwa kwa xpub.



---

Leseni ya MIT


Hakimiliki (c) 2019 cryptoadvance


---