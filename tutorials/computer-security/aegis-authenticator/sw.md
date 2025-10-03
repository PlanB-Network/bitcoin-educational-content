---
name: Aegis Authenticator
description: Unawezaje kutumia Kithibitishaji cha Aegis ili kulinda akaunti zako kwa uthibitishaji wa pande mbili?
---

![cover](assets/cover.webp)



Leo, uthibitishaji wa vipengele viwili (2FA) ni muhimu ili kupata akaunti za mtandaoni. Mbali na nenosiri, huongeza kipengele cha pili (mara nyingi msimbo wa tarakimu 6) ambao muda wake unaisha baada ya sekunde 30, na kuifanya kuwa vigumu zaidi kwa wadukuzi. Kutumia programu maalum ya TOTP (*Nenosiri la Wakati Mmoja*) ni salama zaidi kuliko SMS, ambayo inaweza kutekwa nyara kwa mashambulizi ya kubadilishana SIM.



Walakini, sio programu zote za uthibitishaji zinaundwa sawa. Masuluhisho mengi ya wamiliki (Kithibitishaji cha Google, Authy, n.k.) huleta matatizo: ni ya umiliki na ya siri (haiwezekani kukagua usalama wao), wakati mwingine hujumuisha vifuatiliaji vya utangazaji, haitoi nakala rudufu za misimbo yako, na inaweza hata kuzuia kusafirisha akaunti zako ili kukufungia kwenye mfumo wao wa ikolojia.



Kithibitishaji cha Aegis, kwa upande mwingine, kinajiwasilisha kama mbadala huru na ya kimaadili kwa programu hizi. Aegis ni programu isiyolipishwa, salama na ya chanzo huria ya kudhibiti tokeni zako za uthibitishaji wa hatua mbili kwenye Android. Ukuzaji wake huangazia vipengele muhimu ambavyo programu zingine hazitoi, ikiwa ni pamoja na usimbaji fiche thabiti wa data ya ndani na uwezekano wa kuhifadhi nakala salama. Yote kwa yote, Aegis inatoa suluhisho la ndani, linaloweza kukaguliwa la uthibitishaji wa pande mbili, bora kwa yeyote anayetaka kuhifadhi udhibiti kamili wa misimbo yao ya 2FA.



## Tunakuletea Kithibitishaji cha Aegis



Aegis Authenticator ni programu huria ya 2FA ya Android, iliyotolewa chini ya leseni ya GPL v3. Inajulikana kwa falsafa yake ya "faragha kwa muundo": programu inafanya kazi nje ya mtandao kabisa na haihitaji muunganisho wa huduma ya mbali. Kwa hivyo, tokeni zako zitasalia kuhifadhiwa ndani ya kifaa chako, katika salama salama ambayo wewe peke yako unashikilia ufunguo.



### Vipengele muhimu



**Vault iliyosimbwa kwa njia fiche:** misimbo yako yote ya OTP imehifadhiwa katika vault iliyosimbwa kwa njia fiche ya AES-256 (hali ya GCM), inayolindwa na nenosiri kuu lililofafanuliwa na mtumiaji. Unaweza kufungua kabati hili kupitia nenosiri au data ya kibayometriki (alama ya vidole, utambuzi wa uso) kwa urahisi zaidi. Kwa kukosekana kwa nenosiri, data haitasimbwa - kwa hivyo tunapendekeza sana uweke moja.



**Shirika la kina:** Aegis huweka akaunti zako nyingi za 2FA zikiwa zimepangwa vyema. Unaweza kupanga maingizo yako kwa alfabeti au kwa mpangilio upendao, ukiyapanga kulingana na kategoria (k.m. Binafsi, Kazi, Jamii) kwa urejeshaji rahisi, na uweke kila ingizo aikoni iliyobinafsishwa. Upau wa utafutaji umejumuishwa ili kupata huduma au akaunti mara moja kwa jina.



**Nakala rudufu za ndani zilizosimbwa kwa njia fiche:** Ili kuhakikisha hutawahi kupoteza ufikiaji wa akaunti zako, Aegis hutoa nakala rudufu za kiotomatiki za salama yako. Hizi zimesimbwa (kupitia nenosiri) na zinaweza kuhifadhiwa katika eneo la chaguo lako (hifadhi ya ndani, folda ya wingu, nk). Programu inaweza pia kuhamisha hifadhidata ya akaunti yako mwenyewe, katika muundo uliosimbwa au ambao haujasimbwa kama inavyohitajika. Kuleta akaunti kutoka kwa programu zingine za 2FA ni rahisi vivyo hivyo (Aegis inaweza kuagiza kutoka kwa Authy, Kithibitishaji cha Google, FreeOTP, naOTP, n.k.).



**Usalama na faragha:** programu iko nje ya mtandao kabisa kwa chaguomsingi. Haihitaji ruhusa za mtandao - kumaanisha kuwa haitumii data kwa ulimwengu wa nje, na haina vifuatiliaji matangazo au moduli za uchanganuzi wa tabia. Aegis haionyeshi matangazo, na haihitaji akaunti ya mtumiaji: mara tu inaposakinishwa, inatumika bila usajili. Kwa vile msimbo wake wa chanzo uko hadharani kwenye GitHub, jumuiya inaweza kuikagua kwa uhuru, ikihakikisha kutokuwepo kwa utendaji mbaya au uliofichwa.



**Interface ya kisasa:** Aegis inachukua Muundo nadhifu wa Nyenzo, unaotumia mandhari meusi (ikiwa ni pamoja na hali ya AMOLED) na hata mwonekano wa hiari wa kigae ili kuonyesha misimbo yako kama gridi. Interface haina vitu vingi, haina vichekesho, na inazuia kunasa skrini ya misimbo kama hatua ya usalama.



## Ufungaji



Kwa vile Kithibitishaji cha Aegis ni chanzo huria, watengenezaji wake wanapendelea njia za usambazaji zinazofaa kwa faragha. Kuna njia mbili kuu za kuiweka:



### Kupitia F-Droid (inapendekezwa)



Njia salama na rahisi ni kupitia F-Droid, hifadhi mbadala isiyolipishwa. Ikiwa F-Droid bado haijasakinishwa kwenye simu yako, anza kwa kuipakua kutoka kwa tovuti rasmi [F-Droid.org](https://f-droid.org). Kisha:





- Fungua F-Droid na uhakikishe kuwa umesasisha hazina zako ili kupata orodha ya hivi punde ya programu
- Tafuta "Aegis Authenticator" katika F-Droid. Programu rasmi inapaswa kuonekana (mchapishaji: Maendeleo ya Beem)
- Anza usakinishaji kwa kubonyeza Sakinisha. Kwa vile Aegis ni mojawapo ya programu zilizothibitishwa na F-Droid, unafaidika kutokana na upakuaji unaotegemewa na salama.



Kusakinisha kupitia F-Droid kunatoa faida ya kupokea masasisho ya kiotomatiki ya programu punde tu yanapotolewa. Zaidi ya hayo, F-Droid inahakikisha kwamba programu haina vipengele vya umiliki visivyohitajika.



### Kupitia GitHub (APK iliyosainiwa)



Ikiwa ungependa kusakinisha programu bila kupitia dukani, unaweza kupakua APK rasmi moja kwa moja kutoka kwa ukurasa wa mradi wa GitHub. Kwenye hazina ya Aegis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), nenda kwenye sehemu ya Matoleo ambapo matoleo thabiti yanachapishwa.





- Pakua toleo jipya zaidi la APK
- Kabla ya kusakinisha APK, hakikisha kuwa umeidhinisha usakinishaji wa programu kutoka vyanzo visivyojulikana kwenye kifaa chako (katika Mipangilio ya Android)
- APK iliyotolewa kwenye GitHub imetiwa sahihi na msanidi programu kwa ufunguo sawa na kwenye F-Droid



Baada ya usakinishaji wa mwongozo, programu itafanya kazi sawasawa. Tafadhali kumbuka kuwa masasisho hayatakuwa kiotomatiki: utahitaji kuangalia GitHub mara kwa mara kwa matoleo mapya.



### Google Play Store dhidi ya F-Droid



Kithibitishaji cha Aegis kinapatikana kwenye Duka la Google Play na F-Droid, kukupa chaguo la mbinu ya usakinishaji:



**Duka la Google Play:**




- ✅ Masasisho ya kiotomatiki yaliyojumuishwa kwenye mfumo wa Android
- ✅ Usanikishaji rahisi, unaojulikana
- ✅ APK iliyotiwa saini sawa na kwenye vituo vingine



**F-Droid (inapendekezwa) :**




- ✅ Duka la bure na la wazi
- ✅ Ujenzi unaoweza kuzalishwa tena na kuthibitishwa
- ✅ Hakuna huduma ya Google inayohitajika
- ✅ Heshima kwa falsafa ya programu ya bure



Chaguo kati ya chaguo hizi mbili inategemea mapendeleo yako kuhusu mfumo ikolojia wa Google. Ikiwa ungependa unyenyekevu, Soko la Google Play ni bora. Ikiwa unataka mbinu ya ufaragha zaidi, isiyotegemea huduma za Google, F-Droid ndilo chaguo bora zaidi.



## Usanidi wa kwanza



Wakati Aegis inapozinduliwa kwa mara ya kwanza, utaratibu wa usanidi wa awali unapendekezwa ili kupata usalama wa nambari yako ya 2FA:



![Configuration initiale Aegis](assets/fr/01.webp)



*Mchakato wa awali wa usanidi wa Aegis: skrini ya kukaribisha, chaguo za usalama, ufafanuzi mkuu wa nenosiri na ukamilisho*



### Weka nenosiri kuu



Aegis atakuuliza kwanza uchague nenosiri kuu. Nenosiri hili litatumika kusimba tokeni zako zote za uthibitishaji zilizohifadhiwa kwenye vault. Tunapendekeza sana uweke nenosiri dhabiti na la kipekee ambalo wewe pekee utalijua.



**⚠️ Onyo:** usisahau nenosiri hili - ukilipoteza, misimbo yako ya 2FA iliyosimbwa kwa njia fiche haitaweza kufikiwa (hakuna mlango wa nyuma). Aegis atakuuliza uweke nenosiri mara mbili kwa uthibitisho.



### Washa ufunguaji wa kibayometriki (si lazima)



Ikiwa kifaa chako cha Android kina kisoma alama za vidole au kihisi kingine cha kibayometriki, Aegis itakuomba uwashe kipengele cha kufungua kibayometriki. Chaguo hili ni la hiari lakini linatumika sana: hukuruhusu kufungua programu haraka ukitumia alama ya kidole au uso wako, badala ya kuandika nenosiri kila wakati.



Kumbuka kuwa bayometriki ni manufaa zaidi: nenosiri lako kuu bado linahitajika ikiwa bayometriki zimebadilishwa au kifaa kimewashwa upya.



### Gundua mipangilio ya programu



Mara tu ukiwa ndani ya programu (Interface kuu mwanzoni haina kitu), jitambue na chaguo zinazopatikana za usanidi. Fikia mipangilio kupitia menyu kunjuzi iliyo upande wa juu kulia wa skrini (vidoti tatu wima), kisha uchague "Mipangilio".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface kuu Aegis tupu mwanzoni, ufikiaji wa menyu ya vigezo na muhtasari wa chaguzi zinazopatikana*



Menyu ya mipangilio ya Aegis inaunganisha pamoja sehemu kadhaa muhimu:





- **Mwonekano**: Badilisha mandhari kukufaa (nyepesi, giza, AMOLED), lugha na mipangilio mingine inayoonekana
- **Tabia**: Sanidi tabia ya programu unapoingiliana na orodha ya maingizo
- **Vifurushi vya ikoni**: dhibiti na uingize vifurushi vya ikoni ili kubinafsisha mwonekano na hisia za akaunti zako
- **Usalama**: Mipangilio ya usimbaji fiche, kufungua kibayometriki, kufunga kiotomatiki na vigezo vingine vya usalama
- **Hifadhi rudufu**: Sanidi hifadhi rudufu za kiotomatiki hadi eneo upendalo
- **Ingiza na Hamisha**: Ingiza nakala rudufu kutoka kwa programu zingine za uthibitishaji na uhamishe kihifadhi chako cha Aegis
- **Kumbukumbu ya ukaguzi**: Rekodi ya kina ya matukio yote muhimu katika programu



Shirika hili wazi hukuruhusu kusanidi Aegis kulingana na mapendeleo yako na mahitaji ya usalama.



## Ongeza akaunti ya 2FA



Aegis ikiwa imesanidiwa, wacha tuendelee kwenye mambo muhimu: kuongeza akaunti zako za vipengele viwili. Mchakato ni rahisi, na Aegis inatoa mbinu kadhaa za kuunganisha misimbo yako ya uthibitishaji.



### Njia tatu zinazopatikana za kuongeza



Kutoka kwa Aegis Interface kuu, bonyeza kitufe cha **+** chini kulia ili kufikia chaguo za kuongeza. Una chaguzi tatu:





- **Changanua msimbo wa QR**: Changanua moja kwa moja msimbo wa QR unaoonyeshwa na huduma ya wavuti
- **Changanua picha**: Changanua msimbo wa QR kutoka kwa picha iliyohifadhiwa kwenye kifaa chako
- **Ingiza wewe mwenyewe**: Weka maelezo ya akaunti ya 2FA wewe mwenyewe



### Mfano wa vitendo: kusanidi Bitwarden



Wacha tuchukue mfano halisi wa uanzishaji wa 2FA kwenye Bitwarden ili kuonyesha mchakato:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Mfano wa kuwezesha 2FA kwenye Bitwarden: Mtandao wa Interface wenye chaguo za uthibitishaji na mapendekezo ya Aegis*





- **Kuingia na kufikia mipangilio**: Ingia kwenye akaunti yako ya Bitwarden na ufikie mipangilio, kichupo cha "Usalama"
- **Sehemu ya watoa huduma**: Nenda kwenye sehemu ya "Watoa huduma" na ubofye "Dhibiti" katika sehemu ya "Programu ya Kithibitishaji"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Kamilisha mchakato wa kuongeza akaunti: Msimbo wa QR unaonyeshwa na huduma, ufunguo wa siri unaonekana na msimbo wa uthibitishaji umeingizwa*





- Changanua msimbo wa **QR**: Dirisha ibukizi hufunguliwa kwa msimbo wa QR na ufunguo wa siri
- Katika **Aegis**: Tumia "Changanua msimbo wa QR" ili kunasa maelezo kiotomatiki
- **Uthibitishaji**: Weka msimbo wa tarakimu 6 unaozalishwa na Aegis katika sehemu ya "Msimbo wa uthibitishaji"
- **Amilisha**: Bofya "Washa" ili kukamilisha kuwezesha



### Ongeza maelezo wewe mwenyewe



Ukipendelea au huwezi kuchanganua msimbo wa QR, tumia chaguo la "Ingiza wewe mwenyewe". Fomu hukuruhusu kuingia:



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Mchakato wa kuongeza akaunti mpya ya 2FA: Interface tupu, ongeza chaguo, fomu ya kuingiza mwenyewe na akaunti imeongezwa kwa mafanikio*





- **Jina**: Jina la huduma (k.m. Bitwarden, GitHub...)
- **Mtoaji**: Mtoaji (mara nyingi hufanana na jina)
- **Kikundi**: Hiari, kupanga akaunti zako kwa kategoria
- **Kumbuka**: Maoni ya kibinafsi kwenye akaunti hii
- **Siri**: Ufunguo wa siri unaotolewa na huduma (umefichwa na chaguo-msingi)
- **Kina**: Vigezo vya hali ya juu (algorithm, kipindi, idadi ya tarakimu)



Mara tu akaunti imeongezwa, inaonekana kwenye orodha yako ikiwa na msimbo wake wa sasa na kiashirio cha wakati kinachoonyesha muda uliosalia kabla ya kusasishwa.



### Utangamano wa jumla



Aegis inaoana na huduma zote zinazotumia viwango vya TOTP na HOTP, ikijumuisha takriban tovuti zote zinazotoa 2FA: mitandao ya kijamii, benki, wasimamizi wa nenosiri, mifumo ya crypto, n.k.



### Shirika la kuingilia



Mara tu unapoongeza akaunti kadhaa, utathamini zana za shirika za Aegis:





- **Upangaji maalum:** Kwa chaguo-msingi, akaunti zimeorodheshwa kwa mpangilio wa kialfabeti, lakini unaweza kubadilisha mpangilio wewe mwenyewe.
- **Vikundi na kategoria:** Unda vikundi ili kutenganisha akaunti zako za kibinafsi na akaunti yako ya biashara, au vikundi kulingana na aina ya huduma (benki, barua pepe, mitandao ya kijamii, n.k.)
- **Aikoni zilizogeuzwa kukufaa:** Aegis inajaribu kukabidhi ikoni inayofaa kiotomatiki ikiwa inapatikana, vinginevyo unaweza kuchagua kutoka kwa ikoni nyingi za kawaida au kuleta picha.
- **Utafutaji wa haraka:** Upau wa kutafutia ulio juu hukuwezesha kuandika herufi chache ili kuchuja maingizo yanayolingana papo hapo.



Kwa kugusa ingizo, msimbo wa OTP unaonyeshwa kwa ukubwa kamili (ikiwa ulifichwa) na unaweza kuinakili kwenye ubao wa kunakili kwa kubonyeza kwa muda mrefu - rahisi kwa kuibandika kwenye programu unayotaka kuunganisha.



## Usalama na chelezo



Kwa usalama katika moyo wa Aegis, ni muhimu kuelewa jinsi misimbo yako ya 2FA inalindwa, na jinsi ya kuhakikisha uendelevu wao kukitokea tatizo.



### Usanifu wa usalama



**Usimbaji fiche thabiti**: Nambari zako zote za kuthibitisha zimehifadhiwa katika salama iliyosimbwa kwa kutumia algoriti ya **AES-256 katika hali ya GCM**, pamoja na nenosiri lako kuu. Utoaji wa ufunguo unatokana na **kuficha**, inayotoa ulinzi ulioimarishwa dhidi ya mashambulizi ya nguvu ya kikatili.



**Kufungua kwa usalama** : Nenosiri kuu linahitajika ili kusimbua data yako. Biometriska (si lazima) hutumia **Duka la Ufunguo Secure la Android** na TEE (Mazingira Yanayoaminika ya Utekelezaji) ili kulinda ufunguo wa usimbaji fiche.



**Ruhusa ndogo**: Aegis hufanya kazi nje ya mtandao kwa chaguomsingi, ikihitaji ufikiaji wa kamera pekee (Scan QR), bayometriki na vibrator. Hakuna data inayokusanywa au kushirikiwa.



### Chaguo za chelezo



Aegis inatoa mikakati kadhaa ya chelezo ili kuendana na mahitaji tofauti ya usalama na urahisi:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface imekamilika ikiwa na akaunti iliyoongezwa, arifa ya chelezo, mipangilio ya kuhifadhi nakala kiotomatiki na mikakati ya kuhifadhi*



**1. Nakala za kiotomatiki za ndani **




- Sanidi folda lengwa la chaguo lako
- Masafa yanayoweza kubinafsishwa (baada ya kila mabadiliko, kila siku, n.k.)
- Faili zilizosimbwa kwa njia fiche zinazolindwa na nenosiri (.aesvault)
- Inatumika na folda zilizosawazishwa (Nextcloud, Dropbox, nk)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Mchakato wa kuchagua folda ya chelezo: kichunguzi cha faili, folda lengwa na idhini ya ufikiaji*



**2. Android** chelezo za wingu




- Ujumuishaji wa hiari na mfumo wa chelezo wa Android
- Inapatikana kwa salama zilizosimbwa pekee (usalama umehifadhiwa)
- Hifadhi nakala ya uwazi na data nyingine ya Android
- Urejeshaji kiotomatiki kwenye ubadilishaji wa kifaa



**3. Mwongozo** usafirishaji




- Hamisha unapohitajika kupitia **Mipangilio > Ingiza na Hamisha**
- Chaguo la umbizo lililosimbwa (lililopendekezwa) au wazi
- Inafaa kwa uhamiaji au nakala rudufu za mara kwa mara



### Mazoea mazuri ya usalama





- Weka matoleo kadhaa ya **chelezo** ili kuzuia ufisadi
- Mara kwa mara **jaribu** nakala zako kwa kujaribu kurejesha
- Hifadhi misimbo yako ya uokoaji inayotolewa na huduma kando
- **Nenosiri lako kuu** bado linahitajika hata kwa hifadhi rudufu za wingu
- **Linda nenosiri lako kuu**: tumia nenosiri dhabiti la kipekee lililohifadhiwa kwenye kidhibiti nenosiri
- Sasisha programu yako **ukitumia viraka vya hivi punde zaidi vya usalama**
- Washa kipengele cha kufunga kiotomatiki katika mipangilio ili kupata ufikiaji salama wa programu
- Zima picha za skrini (chaguo-msingi) ili kuzuia misimbo yako kuzuiwa
- **Tumia bayometriki kwa uangalifu**: pendelea manenosiri kwa ufikiaji muhimu



## Kulinganisha na maombi mengine



Aegis hujipanga vipi dhidi ya programu zingine maarufu za uthibitishaji?



### Aegis dhidi ya Kithibitishaji cha Google



**Egis :**




- ✅ Chanzo wazi na kinachoweza kukaguliwa
- ✅ Hifadhi rudufu iliyosimbwa ndani
- ✅ Shirika la hali ya juu (vikundi, ikoni, utaftaji)
- ✅ Hakuna mkusanyiko wa data
- ❌ Android pekee



**Kithibitishaji cha Google :**




- ✅ Inapatikana kwenye Android na iOS
- ✅ Usawazishaji wa Wingu (tangu 2023)
- ❌ Msimbo wa chanzo uliofungwa
- ❌ Utendaji mdogo
- ❌ Uwezo wa kukusanya data ya Google



### Aegis dhidi ya Authy



**Egis :**




- ✅ Chanzo wazi
- ✅ Hakuna akaunti inayohitajika
- ✅ Uhamishaji wa msimbo unawezekana
- ✅ Jumla ya udhibiti wa data
- ❌ Hakuna usawazishaji asili wa vifaa vingi



**Haki:**




- ✅ Usawazishaji wa vifaa vingi
- ✅ Inapatikana kwenye Android na iOS
- ❌ Msimbo wa chanzo uliofungwa
- ❌ Inahitaji nambari ya simu
- ❌ Haiwezi kuhamisha misimbo
- ❌ Maombi ya Kompyuta ya mezani yaliondolewa Machi 2024



Aegis huwafaa watumiaji wa Android wanaothamini uwazi, usalama wa ndani na udhibiti kamili wa data zao. Njia mbadala kama vile Authy zinafaa zaidi ikiwa unahitaji kabisa maingiliano ya kiotomatiki ya vifaa vingi.




## Hitimisho



Kithibitishaji cha Aegis ni suluhisho bora kwa wale wanaotafuta programu ya 2FA ya ufaragha, salama na ya uwazi. Mbinu yake ya chanzo huria, pamoja na usimbaji fiche thabiti na Interface nadhifu, huifanya kuwa chaguo la kwanza la kupata akaunti zako za mtandaoni.



Ingawa inatumika tu kwa Android na inakosa mawingu asilia ya kusawazisha, Aegis hurekebisha zaidi mapungufu haya kwa falsafa yake ya "faragha kwa muundo" na udhibiti kamili wa data. Kwa watumiaji wanaojali kuhusu faragha yao ya kidijitali, Aegis inatoa njia mbadala inayoaminika na yenye nguvu kwa suluhu kuu za umiliki sokoni.



Usalama wa akaunti zako za mtandaoni si lazima utegemee nia njema ya makampuni ya kibiashara. Ukiwa na Aegis, unaweka udhibiti wa misimbo yako ya uthibitishaji, katika salama ya dijitali ambayo wewe pekee ndiye unashikilia ufunguo.



## Rasilimali



### Tovuti rasmi




- **Tovuti rasmi**: [getaegis.app](https://getaegis.app/) - Wasilisho na upakuaji wa programu
- **Msimbo wa chanzo**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Hazina Rasmi ya GitHub
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Usakinishaji kupitia duka lisilolipishwa



### Nyaraka za kiufundi




- **Hati za Vault**: [Muundo wa kuba](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Maelezo ya kiufundi ya usimbaji fiche na usanifu salama
- **Maswali Yanayoulizwa Mara Kwa Mara**: [getaegis.app/#faq](https://getaegis.app/#faq) - Majibu ya maswali yanayoulizwa mara kwa mara
- **Wiki ya mradi**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Hati kamili za mtumiaji