---
name: Utangulizi wa Cryptography rasmi
goal: Utangulizi wa kina wa sayansi na mazoezi ya kriptografia.
objectives: 

  - Gundua misimbo ya Beale na mbinu za kisasa za kriptografia ili kuelewa dhana za kimsingi na za kihistoria za usimbaji fiche.
  - Chunguza katika nadharia ya nambari, vikundi, na nyuga ili kufahamu dhana muhimu za hisabati msingi wa kriptografia.
  - Soma msimbo wa mtiririko wa RC4 na AES kwa ufunguo wa 128-bit ili kupata maelezo kuhusu algoriti za kriptografia linganifu.
  - Chunguza mfumo wa kificho wa RSA, usambazaji wa ufunguo, na vitendaji vya Hash ili kugundua usimbaji fiche usiolinganishwa.

---
# Kuzama kwa kina katika kriptografia

Ni vigumu kupata nyenzo nyingi ambazo hutoa msingi mzuri wa kati katika elimu ya cryptography.

Kwa upande mmoja, kuna risala ndefu, rasmi, zinazoweza kufikiwa tu na wale walio na usuli dhabiti katika hisabati, mantiki, au taaluma nyingine rasmi. Kwa upande mwingine, kuna utangulizi wa hali ya juu sana ambao huficha maelezo mengi sana kwa mtu yeyote ambaye angalau ana hamu ya kujua.

Utangulizi huu wa kriptografia unatafuta kunasa hali ya kati. Ingawa inapaswa kuwa na changamoto na maelezo ya kina kwa mtu yeyote mpya kwa cryptography, sio shimo la sungura la risala ya kawaida ya msingi.

+++
# Utangulizi

<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Maelezo mafupi

<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Kitabu hiki kinatoa utangulizi wa kina wa sayansi na mazoezi ya usimbaji fiche. Inapowezekana inazingatia dhana, badala ya ufafanuzi rasmi wa nyenzo.

> Kozi hii inatokana na [repo la JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Sawa kwake. Yaliyomo bado hayajakamilika na ni hapa tu kuonyesha jinsi tunavyoweza kuiunganisha ikiwa JWburger itakubali.
### Motisha na malengo

Ni vigumu kupata nyenzo nyingi ambazo hutoa msingi mzuri wa kati katika elimu ya cryptography.

Kwa upande mmoja, kuna risala ndefu, rasmi, zinazoweza kufikiwa tu na wale walio na usuli dhabiti katika hisabati, mantiki, au taaluma nyingine rasmi. Kwa upande mwingine, kuna utangulizi wa hali ya juu sana ambao huficha maelezo mengi sana kwa mtu yeyote ambaye angalau ana hamu ya kujua.

Utangulizi huu wa kriptografia unatafuta kunasa hali ya kati. Ingawa inapaswa kuwa na changamoto na maelezo ya kina kwa mtu yeyote mpya kwa cryptography, sio shimo la sungura la risala ya kawaida ya msingi.

### Watazamaji walengwa

Kuanzia kwa wasanidi programu hadi kwa walio na udadisi wa kiakili, kitabu hiki ni muhimu kwa mtu yeyote ambaye anataka zaidi ya ufahamu wa juu juu wa cryptography. Ikiwa lengo lako ni kusimamia uga wa cryptography, basi kitabu hiki pia ni mahali pazuri pa kuanzia.

### Miongozo ya kusoma

Kitabu kwa sasa kina sura saba: "Cryptography ni nini?" (Sura ya 1), "Misingi ya Hisabati ya Cryptography I" (Sura ya 2), "Misingi ya Hisabati ya Cryptography II" (Sura ya 3), "Symmetric Cryptography" (Sura ya 4), "RC4 na AES" (Sura ya 5), ​​"Cryptography Asymmetric" (Sura ya 6), na "Mfumo wa RSA wa 7)" (Sura ya 7). Sura ya mwisho, "Cryptography in Practice," bado itaongezwa. Inaangazia programu mbali mbali za kriptografia, ikijumuisha usalama wa Layer wa usafirishaji, uelekezaji wa vitunguu, na mfumo wa thamani wa Bitcoin wa Exchange.

Isipokuwa una usuli dhabiti katika hisabati, nadharia ya nambari pengine ndiyo mada ngumu zaidi katika kitabu hiki. Ninatoa muhtasari wake katika Sura ya 3, na pia inaonekana katika ufafanuzi wa AES katika Sura ya 5 na mfumo wa siri wa RSA katika Sura ya 7.

Ikiwa unatatizika sana na maelezo rasmi katika sehemu hizi za kitabu, ninapendekeza utatue kwa usomaji wa hali ya juu mara ya kwanza.

### Shukrani

Kitabu chenye ushawishi mkubwa zaidi katika kuunda hiki kimekuwa _Introduction to Modern Cryptography_ cha Jonathan Katz na Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Kozi inayoandamana nayo inapatikana kwenye Coursera inayoitwa "Cryptography."

Vyanzo vikuu vya ziada ambavyo vimesaidia katika kuunda muhtasari katika kitabu hiki ni Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar na Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) na [kozi inayotokana na kitabu cha Paar inayoitwa “Introduction to Cryptography”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); na Bruce Schneier, Applied Cryptography, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons).

Nitataja tu habari mahususi na matokeo ninayochukua kutoka kwa vyanzo hivi, lakini nataka kukiri deni langu la jumla kwao hapa.

Kwa wale wasomaji ambao wanataka kutafuta ujuzi wa juu zaidi juu ya cryptography baada ya utangulizi huu, ninapendekeza sana kitabu cha Katz na Lindell. Kozi ya Katz kwenye Coursera inapatikana zaidi kuliko kitabu.

### Michango

Tafadhali angalia [faili ya michango katika hazina](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) kwa baadhi ya miongozo ya jinsi ya kusaidia mradi.

### Nukuu

**Masharti muhimu:**

Maneno muhimu katika primers huletwa kwa kuwafanya ujasiri. Kwa mfano, utangulizi wa msimbo wa Rijndael kama neno muhimu utaonekana kama ifuatavyo: **Rijndael cipher**.

Istilahi muhimu zimefafanuliwa kwa uwazi, isipokuwa kama ni majina sahihi au maana yake ni dhahiri kutokana na mjadala.

Ufafanuzi wowote kawaida hutolewa baada ya kuanzishwa kwa neno muhimu, ingawa wakati mwingine ni rahisi zaidi kuacha ufafanuzi hadi hatua ya baadaye.

**Maneno na vishazi vilivyosisitizwa:**

Maneno na misemo husisitizwa kupitia italiki. Kwa mfano, neno "Kumbuka nenosiri lako" linaweza kuonekana kama ifuatavyo: *Kumbuka nenosiri lako*.

**Taarifa rasmi:**

Nukuu rasmi inahusu vigeu, vigeu vya nasibu, na seti.


- Vigeu: Kawaida hivi huonyeshwa kwa herufi ndogo (k.m., "x" au "y"). Wakati mwingine huwa na herufi kubwa kwa uwazi (k.m., "M" au "K").
- Vigezo vya nasibu: Hizi huonyeshwa kila mara kwa herufi kubwa (k.m., "X" au "Y").
- Seti: Hizi huonyeshwa kila mara kwa herufi kubwa, kubwa (k.m., **S**)

# Cryptography ni nini?

<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Sifa za Beale

<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

Wacha tuanze uchunguzi wetu katika uwanja wa cryptography na moja ya vipindi vya kupendeza na vya kuburudisha katika historia yake: ile ya maandishi ya Beale. [1]

Hadithi ya maandishi ya Beale, kwa maoni yangu, ina uwezekano mkubwa wa kuwa hadithi kuliko ukweli. Lakini inadaiwa ilitokea kama ifuatavyo.

Katika Majira ya baridi ya 1820 na 1822, mtu mmoja aitwaye Thomas J. Beale alikaa katika nyumba ya wageni inayomilikiwa na Robert Morriss huko Lynchburg (Virginia). Mwishoni mwa kukaa kwa pili kwa Beale, alimpa Morriss sanduku la chuma na karatasi za thamani kwa ajili ya kuhifadhi.

Miezi michache baadaye, Morriss alipokea barua kutoka kwa Beale ya Mei 9, 1822. Ilisisitiza thamani kubwa ya yaliyomo ya sanduku la chuma na ilihusiana na maagizo fulani kwa Morriss: ikiwa hakuna Beale au washirika wake yeyote aliyekuja kudai sanduku, anapaswa kuifungua kwa usahihi miaka kumi tangu tarehe ya barua (yaani, Mei 9, 1832). Baadhi ya karatasi za ndani zingeandikwa kwa maandishi ya kawaida. Wengine kadhaa, hata hivyo, "hawangeeleweka bila usaidizi wa ufunguo." "Ufunguo" huu, basi, ungewasilishwa kwa Morriss na rafiki asiyejulikana wa Beale mnamo Juni 1832.

Licha ya maagizo ya wazi, Morriss hakufungua sanduku mnamo Mei 1832 na rafiki wa ajabu wa Beale hakuwahi kutokea mnamo Juni mwaka huo. Haikuwa hadi 1845 kwamba mwenye nyumba ya wageni hatimaye aliamua kufungua sanduku. Ndani yake, Morriss alipata barua inayoelezea jinsi Beale na washirika wake waligundua dhahabu na fedha huko Magharibi na kuzika, pamoja na vito kadhaa, kwa usalama. Kwa kuongeza, kisanduku kilikuwa na **matini tatu**: yaani, maandishi yaliyoandikwa kwa msimbo ambayo yanahitaji **ufunguo wa kriptografia**, au siri, na algoriti inayoambatana ili kufungua. Mchakato huu wa kufungua maandishi ya siri hujulikana kama **decryption**, huku mchakato wa kufunga unajulikana kama **usimbaji fiche**. (Kama ilivyofafanuliwa katika Sura ya 3, neno cipher linaweza kuchukua maana mbalimbali. Katika jina "Beale ciphers", ni kifupi cha matini kisifa.)

Nakala tatu za msimbo ambazo Morriss alipata katika kisanduku cha chuma kila moja ina msururu wa nambari zilizotenganishwa na koma. Kwa mujibu wa maelezo ya Beale, maandishi haya tofauti hutoa eneo la hazina, yaliyomo ya hazina, na orodha ya majina yenye warithi halali wa hazina na hisa zao (habari za mwisho zinafaa ikiwa Beale na washirika wake hawakuja kudai sanduku).

Morris alijaribu kufuta maandishi hayo matatu kwa miaka ishirini. Hii ingekuwa rahisi na ufunguo. Lakini Morriss hakuwa na ufunguo na hakufanikiwa katika majaribio yake ya kurejesha maandishi asilia, au **maandishi wazi** kama yanavyoitwa kwa kawaida katika cryptography.

Akikaribia mwisho wa maisha yake, Morriss alipitisha kisanduku kwa rafiki yake mwaka wa 1862. Rafiki huyu baadaye alichapisha kijitabu mwaka wa 1885, chini ya jina bandia la J.B. Ward. Ilijumuisha maelezo ya historia (inayodaiwa) ya kisanduku, maandishi matatu, na suluhisho ambalo alikuwa amepata kwa maandishi ya pili. (Inavyoonekana, kuna ufunguo mmoja kwa kila maandishi, na sio ufunguo mmoja unaofanya kazi kwenye maandishi yote matatu kama vile Beale anavyoonekana kuwa alipendekeza katika barua yake kwa Morriss.)

Unaweza kuona maandishi ya pili katika *Kielelezo 2* hapa chini. [2] Ufunguo wa maandishi haya ni Azimio la Uhuru la Marekani. Utaratibu wa kusimbua unakuja kwa kutumia sheria mbili zifuatazo:


- Kwa nambari yoyote n katika maandishi ya siri, tafuta neno la nth katika Azimio la Uhuru la Marekani
- Badilisha nambari n na herufi ya kwanza ya neno ulilopata

*Kielelezo 1: Beale cipher no. 2*

![Figure 1: Beale cipher no 2.](assets/Figure1-1.webp "Figure 1: Beale cipher no. 2")

Kwa mfano, nambari ya kwanza ya kifungu cha pili ni 115. Neno la 115 la Azimio la Uhuru “limeanzishwa,” kwa hiyo herufi ya kwanza ya andiko la msingi ni “i.” Nakala ya siri haionyeshi moja kwa moja nafasi ya maneno na herufi kubwa. Lakini baada ya kuchambua maneno machache ya kwanza, unaweza kuhitimisha kimantiki kwamba neno la kwanza la maandishi wazi lilikuwa tu "mimi." (Mafungu ya madai yanaanza na kishazi “Nimeweka katika kaunti ya Bedford.”)

Baada ya kusimbua, ujumbe wa pili unatoa maelezo ya kina ya hazina hiyo (dhahabu, fedha, na vito), na unapendekeza kwamba ilizikwa katika vyungu vya chuma na kufunikwa na mawe katika Kaunti ya Bedford (Virginia). Watu wanapenda fumbo zuri, kwa hivyo juhudi kubwa zimetumika katika kusimbua misimbo mingine miwili ya Beale, hasa ile inayoelezea eneo la hazina. Hata waandishi mbalimbali maarufu wa maandishi wamejaribu mikono yao juu yao. Walakini, kufikia sasa, hakuna mtu ambaye ameweza kusimbua maandishi mengine mawili ya siri.

**Maelezo:**

[1] Kwa muhtasari mzuri wa hadithi, ona Simon Singh, *The Code Book*, Fourth Estate (London, 1999), uk. 82-99. Filamu fupi ya hadithi ilitengenezwa na Andrew Allen mwaka wa 2010. Unaweza kupata filamu, "Thomas Beale Cipher," [kwenye tovuti yake](http://www.thomasbealecipher.com/).

[2] Picha hii inapatikana kwenye ukurasa wa Wikipedia kwa maandishi ya Beale.

## cryptography ya kisasa

<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Hadithi za kupendeza kama vile misimbo ya Beale ndizo ambazo wengi wetu tunahusisha na kriptografia. Hata hivyo, kriptografia ya kisasa inatofautiana kwa angalau njia nne muhimu kutoka kwa aina hizi za mifano ya kihistoria.

Kwanza, usimbaji fiche wa kihistoria umehusika tu na **usiri** (au usiri). [3] Maandishi ya siri yangeundwa ili kuhakikisha kuwa wahusika fulani pekee ndio wangeweza kujua habari iliyo katika maandishi ya wazi, kama ilivyokuwa kwa maandishi ya Beale. Ili mpango wa usimbaji fiche utekeleze madhumuni haya vyema, usimbaji fiche wa maandishi ya siri lazima ufanyike ikiwa una ufunguo.

Fiche za kisasa zinahusika na anuwai ya mada kuliko usiri tu. Mandhari haya yanajumuisha kimsingi (1) **uadilifu wa ujumbe**—yaani, kuhakikisha kwamba ujumbe haujabadilishwa; (2) **uhalisi wa ujumbe**—yaani, kuhakikishia kwamba ujumbe umetoka kwa mtumaji fulani; na (3) **kutokataa**—yaani, kuhakikisha kwamba mtumaji hawezi kukataa kwa uwongo baadaye kwamba alituma ujumbe. [4]

Tofauti muhimu ya kukumbuka ni, kwa hivyo, kati ya **mpango wa usimbaji fiche** na **mpango wa kriptografia**. Mpango wa usimbuaji unahusika tu na usiri. Ingawa mpango wa usimbaji fiche ni mpango wa kriptografia, kinyume chake si kweli. Mpango wa kriptografia unaweza pia kutumikia mada zingine kuu za usimbaji fiche, ikijumuisha uadilifu, uhalisi, na kutokataa.

Mandhari ya uadilifu na uhalisi ni muhimu kama usiri. Mifumo yetu ya kisasa ya mawasiliano isingeweza kufanya kazi bila hakikisho kuhusu uadilifu na uhalisi wa mawasiliano. Kutokataa pia ni jambo muhimu sana, kama vile mikataba ya kidijitali, lakini haihitajiki sana katika utumizi wa kriptografia kuliko usiri, uadilifu na uhalisi.

Pili, mifumo ya usimbaji fiche ya kitambo kama vile misimbo ya Beale kila mara inahusisha ufunguo mmoja ambao ulishirikiwa kati ya wahusika wote husika. Hata hivyo, mipango mingi ya kisasa ya kriptografia inahusisha si moja tu, lakini funguo mbili: ** faragha ** na ** ufunguo wa umma **. Ingawa ya kwanza inapaswa kubaki ya faragha katika maombi yoyote, ya pili kwa kawaida ni maarifa ya umma (kwa hivyo, majina yao husika). Katika nyanja ya usimbaji fiche, ufunguo wa umma unaweza kutumika kusimba ujumbe, huku ufunguo wa faragha unaweza kutumika kusimbua.

Tawi la kriptografia linaloshughulika na mipango ambapo wahusika wote hushiriki ufunguo mmoja hujulikana kama **simetriki kriptografia**. Kitufe kimoja katika mpango kama huo kawaida huitwa **ufunguo wa faragha** (au ufunguo wa siri). Tawi la kriptografia ambalo linashughulika na mipango inayohitaji jozi ya ufunguo wa faragha-umma inajulikana kama **usimeta wa ulinganifu**. Matawi haya wakati mwingine pia hujulikana kama **ufunguo wa siri wa ufunguo wa kibinafsi** na **usimbuaji wa ufunguo wa umma**, mtawalia (ingawa hii inaweza kuibua mkanganyiko, kwani mifumo ya ufunguo wa siri ya ufunguo wa umma pia ina funguo za faragha).

Ujio wa cryptography asymmetric mwishoni mwa miaka ya 1970 imekuwa moja ya matukio muhimu zaidi katika historia ya cryptography. Bila hivyo, mifumo yetu mingi ya kisasa ya mawasiliano, ikijumuisha Bitcoin, isingewezekana, au angalau isingewezekana sana.

Muhimu zaidi, usimbaji fiche wa kisasa si somo la kipekee la miundo ya kriptografia ya ulinganifu na assymetric (ingawa hiyo inashughulikia sehemu kubwa). Kwa mfano, usimbaji fiche pia unahusika na chaguo za kukokotoa za Hash na jenereta za nambari za uwongo, na unaweza kuunda programu kwenye viasili hivi ambavyo havihusiani na ulinganifu wa ufunguo wa assymetric.

Tatu, mbinu za usimbaji fiche za kitambo, kama zile zinazotumiwa katika maandishi ya Beale, zilikuwa za sanaa zaidi kuliko sayansi. Usalama wao unaotambulika uliegemezwa sana na mawazo kuhusu ugumu wao. Kwa kawaida wangetiwa viraka wakati shambulio jipya kwao lilipojulikana, au kuachwa kabisa ikiwa shambulio hilo lilikuwa kali sana. Fiche za kisasa, hata hivyo, ni sayansi kali yenye mbinu rasmi, ya kihisabati ya kuendeleza na kuchambua mifumo ya kriptografia. [5]

Hasa, vituo vya kisasa vya usimbaji fiche huzingatia **uthibitisho rasmi wa usalama**. Uthibitisho wowote wa usalama wa mpango wa kriptografia unaendelea katika hatua tatu:

1. Taarifa ya **ufafanuzi wa siri wa usalama**, yaani, malengo ya usalama na tishio linaloletwa na mshambuliaji.

2. Taarifa ya mawazo yoyote ya hisabati kuhusiana na utata wa kimahesabu wa mpango. Kwa mfano, mpango wa kriptografia unaweza kuwa na jenereta ya nambari ya uwongo. Ingawa hatuwezi kuthibitisha haya yapo, tunaweza kudhani kuwa yapo.

3. Ufafanuzi wa kihisabati **uthibitisho wa usalama** wa mpango kwa misingi ya dhana rasmi ya usalama na mawazo yoyote ya kihisabati.

Nne, ilhali usimbaji fiche wa kihistoria ulitumiwa kimsingi katika mazingira ya kijeshi, umekuja kupenyeza shughuli zetu za kila siku katika enzi ya kidijitali. Iwe unafanya benki mtandaoni, unachapisha kwenye mitandao ya kijamii, unanunua bidhaa kutoka Amazon ukitumia kadi yako ya mkopo, au unamdokezea rafiki Bitcoin, cryptography ni sine qua non ya enzi yetu ya kidijitali.

Kwa kuzingatia vipengele hivi vinne vya usimbaji fiche wa kisasa, tunaweza kubainisha **cryptography** ya kisasa kama sayansi inayohusika na ukuzaji na uchanganuzi rasmi wa mifumo ya kriptografia ili kupata taarifa za kidijitali dhidi ya mashambulizi ya wapinzani. [6] Usalama hapa unapaswa kueleweka kwa mapana kama kuzuia mashambulizi ambayo yanaharibu usiri, uadilifu, uthibitishaji, na/au kutokataliwa katika mawasiliano.

Siri za siri zinaonekana vyema kama taaluma ndogo ya **security**, ambayo inahusika na kuzuia wizi, uharibifu na matumizi mabaya ya mifumo ya kompyuta. Kumbuka kwamba maswala mengi ya usalama wa mtandao yana muunganisho mdogo au sehemu tu kwa cryptography.

Kwa mfano, ikiwa kampuni ina seva za bei ghali ndani ya nchi, inaweza kuwa na wasiwasi wa kulinda maunzi haya dhidi ya wizi na uharibifu. Ingawa hili ni suala la usalama wa mtandao, halihusiani kidogo na usimbaji fiche.

Kwa mfano mwingine, **mashambulizi ya hadaa** ni tatizo la kawaida katika enzi yetu ya kisasa. Mashambulizi haya yanajaribu kuwahadaa watu kupitia barua-pepe au chombo kingine cha ujumbe ili kutoa taarifa nyeti kama vile manenosiri au nambari za kadi ya mkopo. Ingawa kriptografia inaweza kusaidia mashambulizi ya ulaghai ya Address kwa kiwango fulani, mbinu ya kina inahitaji zaidi ya kutumia tu usimbaji fiche.

**Maelezo:**

[3] Kwa hakika, utumizi muhimu wa mifumo ya kriptografia imehusika na usiri. Watoto, kwa mfano, mara nyingi hutumia mifumo rahisi ya kriptografia kwa "kufurahisha". Usiri sio wasiwasi sana katika kesi hizo.

[4] Bruce Schneier, *Cryptography Iliyotumika*, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons), uk. 2.

[5] Tazama Jonathan Katz na Yehuda Lindell, *Utangulizi wa Siri ya Kisasa*, CRC Press (Boca Raton, FL: 2015), esp. uk. 16–23, kwa maelezo mazuri.

[6] Taz. Katz na Lindell, ibid., p. 3. Nadhani sifa zao zina masuala fulani, kwa hivyo wasilisha toleo tofauti kidogo la taarifa yao hapa.

## Fungua mawasiliano

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Usimbaji fiche wa kisasa umeundwa ili kutoa uhakikisho wa usalama katika **mazingira huria**. Ikiwa chaneli yetu ya mawasiliano imelindwa vyema hivi kwamba wasikilizaji hawana nafasi ya kudanganya au hata kutazama tu ujumbe wetu, basi kriptografia ni ya kupita kiasi. Njia zetu nyingi za mawasiliano, hata hivyo, hazina ulinzi wa kutosha hivi.

Msingi wa mawasiliano katika ulimwengu wa kisasa ni mtandao mkubwa wa nyaya za fiber optic. Kupiga simu, kutazama televisheni, na kuvinjari wavuti katika kaya ya kisasa kwa ujumla hutegemea mtandao huu wa nyaya za nyuzi macho (asilimia ndogo inaweza kutegemea satelaiti pekee). Ni kweli kwamba unaweza kuwa na miunganisho tofauti ya data nyumbani kwako, kama vile kebo ya coaxial, laini ya kidijitali ya wanaojisajili (asymmetric), na kebo ya fiber optic. Lakini, angalau katika ulimwengu uliostawi, viunzi hivi tofauti vya data hujiunga haraka nje ya nyumba yako hadi kwenye nodi katika mtandao mkubwa wa nyaya za fiber optic ambazo huunganisha ulimwengu mzima. Vighairi ni baadhi ya maeneo ya mbali ya ulimwengu ulioendelea, kama vile Marekani na Australia, ambapo trafiki ya data bado inaweza kusafiri umbali mkubwa kupitia nyaya za kawaida za simu.

Haiwezekani kuzuia washambuliaji watarajiwa kutoka kufikia mtandao huu wa nyaya na miundomsingi inayotumika. Kwa hakika, tayari tunajua kwamba data zetu nyingi hunaswa na mashirika mbalimbali ya kitaifa ya kijasusi katika makutano muhimu ya Mtandao. [7] Hii inajumuisha kila kitu kuanzia jumbe za Facebook hadi anwani za tovuti unazotembelea.

Ingawa data ya uchunguzi kwa kiwango kikubwa inahitaji adui mwenye nguvu, kama vile wakala wa kitaifa wa ujasusi, washambuliaji walio na rasilimali chache wanaweza kujaribu kwa urahisi kuchungulia kwa kiwango cha karibu zaidi. Ingawa hii inaweza kutokea katika kiwango cha kugonga nyaya, ni rahisi sana kukatiza mawasiliano yasiyotumia waya.

Data nyingi za mtandao wetu wa karibu—iwe ni nyumbani kwetu, ofisini, au kwenye mkahawa—sasa husafiri kupitia mawimbi ya redio hadi kwenye sehemu za ufikiaji zisizo na waya kwenye vipanga njia vya moja kwa moja, badala ya kupitia nyaya halisi. Kwa hivyo mshambulizi anahitaji rasilimali kidogo ili kuzuia trafiki yoyote ya karibu nawe. Hii inahusu hasa kwa vile watu wengi hufanya kidogo sana kulinda data inayosafirishwa kwenye mitandao yao ya ndani. Zaidi ya hayo, washambuliaji watarajiwa wanaweza pia kulenga miunganisho yetu ya mtandao wa simu, kama vile 3G, 4G, na 5G. Mawasiliano haya yote yasiyotumia waya ni shabaha rahisi kwa washambuliaji.

Kwa hivyo, wazo la kuweka mawasiliano siri kwa kulinda njia ya mawasiliano ni matarajio ya udanganyifu kwa sehemu kubwa ya ulimwengu wa kisasa. Kila kitu tunachojua kinahitaji ubishi mkali: unapaswa kudhani kila wakati kuwa mtu anasikiliza. Na kriptografia ndio zana kuu tunayopaswa kupata usalama wa aina yoyote katika mazingira haya ya kisasa.

**Maelezo:**

[7] Angalia, kwa mfano, Olga Khazan, "Mazoezi ya kutisha, ya muda mrefu ya kugonga nyaya chini ya bahari", *The Atlantic*, Julai 16, 2013 (inapatikana katika [The Atlantic] Atlantiki](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Misingi ya Hisabati ya Crystalgraphy 1

<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Vigezo bila mpangilio

<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Cryptography inategemea hisabati. Na ikiwa unataka kujenga zaidi ya uelewa wa juu juu wa cryptography, unahitaji kuridhika na hisabati hiyo.

Sura hii inatanguliza hisabati nyingi za kimsingi utakazokutana nazo katika kujifunza kriptografia. Mada hizo ni pamoja na viambajengo vya nasibu, utendakazi wa modulo, utendakazi wa XOR, na uwongo. Unapaswa kufahamu nyenzo katika sehemu hizi kwa uelewa wowote usio wa juu juu wa kriptografia.

Sehemu inayofuata inahusika na nadharia ya nambari, ambayo ni ngumu zaidi.

### Vigezo bila mpangilio

Tofauti nasibu kawaida huonyeshwa kwa herufi kubwa isiyokolea. Kwa hivyo, kwa mfano, tunaweza kuzungumza kuhusu kigezo cha nasibu $X$, kigezo cha nasibu $Y$, au kigezo cha nasibu $Z$. Hii ndio nukuu nitakayotumia pia kutoka hapa kuendelea.

** Tofauti nasibu** inaweza kuchukua thamani mbili au zaidi zinazowezekana, kila moja ikiwa na uwezekano fulani chanya. Thamani zinazowezekana zimeorodheshwa katika **seti ya matokeo**.

Kila wakati ** sampuli ** ya kutofautisha bila mpangilio, unachora thamani fulani kutoka kwa matokeo yake yaliyowekwa kulingana na uwezekano uliobainishwa.

Wacha tugeuke kwa mfano rahisi. Tuseme mabadiliko ya X ambayo yanafafanuliwa kama ifuatavyo:


- X ina matokeo yaliyowekwa $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

Ni rahisi kuona kuwa $X$ ni kigezo cha nasibu. Kwanza, kuna thamani mbili au zaidi zinazowezekana ambazo $X$ inaweza kuchukua, yaani $1$ na $2$. Pili, kila thamani inayowezekana ina uwezekano chanya wa kutokea wakati wowote unapofanya sampuli ya $X$, yaani $0.5$.

Kinachohitaji kutofautishwa bila mpangilio ni matokeo yaliyowekwa na uwezekano mbili au zaidi, ambapo kila uwezekano una uwezekano chanya wa kutokea wakati wa sampuli. Kimsingi, basi, kutofautisha bila mpangilio kunaweza kufafanuliwa kidhahiri, bila muktadha wowote. Katika kesi hii, unaweza kufikiria "sampuli" kama kuendesha jaribio la asili ili kubaini thamani ya kigezo cha nasibu.

Tofauti $X$ hapo juu ilifafanuliwa kidhahiri. Kwa hivyo, unaweza kufikiria kuchukua sampuli ya kigezo cha $X$ hapo juu kama kugeuza sarafu ya haki na kugawa "2" katika hali ya vichwa na "1" katika kesi ya mikia. Kwa kila sampuli ya $X$, unageuza sarafu tena.

Vinginevyo, unaweza pia kufikiria kuchukua sampuli ya $X$, kama kupeleka hati ya haki na kugawa "2" endapo mhusika atapata $1$, $3$, au $4$, na kuweka "1" iwapo mtu ataleta $2$, $5$, au $6$. Kila wakati unapotoa sampuli ya $X$, unakunja faili tena.

Kwa kweli, jaribio lolote la asili ambalo lingekuwezesha kufafanua uwezekano wa thamani zinazowezekana za $X$ hapo juu linaweza kufikiria kuhusiana na mchoro.

Mara kwa mara, hata hivyo, vigeu vya nasibu havitambuliwi tu kidhahiri. Badala yake, seti ya maadili yanayowezekana ya matokeo ina maana dhahiri ya ulimwengu halisi (badala ya nambari tu). Kwa kuongeza, thamani hizi za matokeo zinaweza kubainishwa dhidi ya aina fulani ya majaribio (badala ya majaribio yoyote ya asili na maadili hayo).

Hebu sasa tuchunguze mfano wa kutofautiana $X$ ambayo haijafafanuliwa kidhahiri. X inafafanuliwa kama ifuatavyo ili kubainisha ni timu gani kati ya mbili itaanzisha mchezo wa soka:


- $X$ ina matokeo {nyekundu inaanza, blue inaanza}
- Geuza sarafu fulani $C $: tails = "nyekundu huanza"; vichwa = "bluu inaanza"

$$
Pr [X = \text{red kicks off}] = 0.5
$$

$$
Pr [X = \text{blue kicks off}] = 0.5
$$

Katika kesi hii, seti ya matokeo ya X hutolewa kwa maana halisi, ambayo ni timu gani inayoanza kwenye mchezo wa mpira wa miguu. Kwa kuongeza, matokeo yanayowezekana na uwezekano wake unaohusishwa huamuliwa na jaribio halisi, ambalo ni kugeuza sarafu fulani $C$.

Ndani ya majadiliano ya usimbaji fiche, vigeu vya nasibu kwa kawaida huletwa dhidi ya seti ya matokeo yenye maana ya ulimwengu halisi. Huenda ikawa seti ya barua pepe zote zinazoweza kusimbwa, zinazojulikana kama nafasi ya ujumbe, au seti ya vitufe vyote ambavyo wahusika wanaotumia usimbaji wanaweza kuchagua, vinavyojulikana kama nafasi muhimu.

Vigezo vya nasibu katika mijadala ya usimbaji fiche, hata hivyo, kwa kawaida hazifafanuliwa dhidi ya jaribio fulani mahususi la asili, lakini dhidi ya jaribio lolote ambalo linaweza kutoa ugawaji wa uwezekano unaofaa.

Vigezo vya nasibu vinaweza kuwa na ugawaji wa uwezekano wa kipekee au unaoendelea. Vigeu vya nasibu vilivyo na **usambazaji wa uwezekano wa kipekee**—yaani, vigeu tofauti visivyo na mpangilio—vina idadi maalum ya matokeo yanayowezekana. Tofauti isiyo ya kawaida $X$ katika mifano yote miwili iliyotolewa hadi sasa ilikuwa tofauti.

**Vigeu vinavyoendelea bila mpangilio** vinaweza kuchukua thamani katika kipindi kimoja au zaidi. Unaweza kusema, kwa mfano, kwamba mabadiliko ya nasibu, baada ya sampuli, itachukua thamani yoyote halisi kati ya 0 na 1, na kwamba kila nambari halisi katika muda huu ina uwezekano sawa. Ndani ya muda huu, kuna maadili yanayowezekana kabisa.

Kwa mijadala ya kriptografia, utahitaji tu kuelewa tofauti tofauti za nasibu. Majadiliano yoyote ya vigeu vya nasibu kutoka hapa kuendelea, kwa hivyo, yanapaswa kueleweka kama yanarejelea viwezo tofauti vya nasibu, isipokuwa kama ilivyoelezwa vinginevyo.

### Kuchora vigeu vya nasibu

Thamani zinazowezekana na uwezekano unaohusishwa wa utofautishaji nasibu unaweza kuonyeshwa kwa urahisi kupitia grafu. Kwa mfano, zingatia utofauti wa nasibu $X$ kutoka sehemu iliyotangulia na seti ya matokeo ya $\{1, 2\}$, na $Pr [X = 1] = 0.5$ na $Pr [X = 2] = 0.5$. Kwa kawaida tungeonyesha tofauti nasibu katika umbo la grafu ya upau kama ilivyo katika *Mchoro 1*.

*Kielelezo cha 1: Tofauti isiyo ya kawaida X*

![Figure 1: Random variable X.](assets/Figure2-1.webp)

Pau pana katika *Kielelezo 1* bila shaka haimaanishi kupendekeza kwamba kigezo cha nasibu $X$ kinaendelea. Badala yake, pau zimefanywa kwa upana ili kuvutia zaidi (mstari moja kwa moja tu hutoa taswira isiyoeleweka zaidi).

### Vigezo vya sare

Katika usemi "kubadilika bila mpangilio," neno "nasibu" linamaanisha tu "uwezekano". Kwa maneno mengine, inamaanisha kuwa matokeo mawili au zaidi ya kutofautisha yanatokea na uwezekano fulani. Matokeo haya, hata hivyo, *si lazima* yawe na uwezekano sawa (ingawa neno "nasibu" linaweza kuwa na maana hiyo katika miktadha mingine).

**kigeu cha sare** ni kisa maalum cha kigezo cha nasibu. Inaweza kuchukua thamani mbili au zaidi zote zikiwa na uwezekano sawa. Tofauti nasibu $X$ iliyoonyeshwa katika *Kielelezo 1* kwa hakika ni kigezo kimoja, kwani matokeo yote mawili yanawezekana yanawezekana kwa $0.5$. Walakini, kuna anuwai nyingi za nasibu ambazo sio mifano ya anuwai sawa.

Fikiria, kwa mfano, tofauti ya nasibu $Y$. Ina matokeo yaliyowekwa {1, 2, 3, 8, 10} na usambazaji wa uwezekano ufuatao:

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Ingawa matokeo mawili yanayowezekana yana uwezekano sawa wa kutokea, yaani $1$ na $8$, $Y$ pia inaweza kuchukua thamani fulani zenye uwezekano tofauti kuliko $0.25$ wakati wa sampuli. Kwa hivyo, wakati $Y$ kwa kweli ni tofauti ya nasibu, sio tofauti sawa.

Taswira ya mchoro ya $Y$ imetolewa katika *Kielelezo 2*.

*Kielelezo cha 2: Utofauti wa nasibu Y*

![Figure 2: Random variable Y.](assets/Figure2-2.webp "Figure 2: Random variable Y")

Kwa mfano wa mwisho, zingatia utofauti wa nasibu Z. Una matokeo yaliyowekwa {1,3,7,11,12} na usambazaji wa uwezekano ufuatao:

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Unaweza kuiona ikionyeshwa kwenye *Kielelezo 3*. Tofauti isiyo ya kawaida Z ni, tofauti na Y, tofauti inayofanana, kwani uwezekano wote wa thamani zinazowezekana wakati wa sampuli ni sawa.

*Kielelezo cha 3: Tofauti isiyo ya kawaida Z*

![Figure 3: Random variable Z.](assets/Figure2-3.webp "Figure 3: Random variable Z")

### Uwezekano wa masharti

Tuseme kwamba Bob anakusudia kuchagua siku moja kutoka kwa mwaka wa kalenda uliopita. Je, tunapaswa kuhitimisha nini ni uwezekano wa siku iliyochaguliwa kuwa katika Majira ya joto?

Maadamu tunafikiri mchakato wa Bob utakuwa sawa, tunapaswa kuhitimisha kuwa kuna uwezekano wa 1/4 wa Bob kuchagua siku katika Majira ya joto. Huu ni **uwezekano usio na masharti** wa siku iliyochaguliwa nasibu kuwa katika Majira ya joto.

Tuseme sasa kwamba badala ya kuchora kwa usawa siku ya kalenda, Bob anachagua tu kwa usawa kutoka kati ya siku hizo ambazo halijoto ya mchana katika Ziwa la Crystal (New Jersey) ilikuwa nyuzi joto 21 au zaidi. Kwa kuzingatia maelezo haya ya ziada, tunaweza kuhitimisha nini kuhusu uwezekano kwamba Bob atachagua siku katika Majira ya joto?

Tunapaswa kutoa hitimisho tofauti na hapo awali, hata bila maelezo yoyote maalum (k.m., halijoto ya saa sita mchana kila siku mwaka wa kalenda uliopita).

Tukijua kwamba Crystal Lake iko New Jersey, bila shaka hatungetarajia halijoto ya saa sita mchana kuwa nyuzi joto 21 au zaidi wakati wa Majira ya baridi. Badala yake, kuna uwezekano mkubwa wa kuwa siku ya joto katika Masika au Mapumziko, au siku mahali fulani katika Majira ya joto. Kwa hivyo, kujua halijoto ya adhuhuri katika Ziwa la Crystal katika siku iliyochaguliwa ilikuwa nyuzi joto 21 au zaidi, uwezekano kwamba siku iliyochaguliwa na Bob ni katika Majira ya joto unakuwa mkubwa zaidi. Huu ni **uwezekano wa masharti** wa siku iliyochaguliwa nasibu kuwa katika Majira ya joto, ikizingatiwa kuwa halijoto ya mchana katika Crystal Lake ilikuwa nyuzi joto 21 au zaidi.

Tofauti na mfano uliopita, uwezekano wa matukio mawili pia unaweza kuwa hauhusiani kabisa. Katika hali hiyo, tunasema kwamba wao ni **kujitegemea**.

Tuseme, kwa mfano, kwamba sarafu fulani ya haki imetua vichwa. Kwa kuzingatia ukweli huu, kuna uwezekano gani wa kunyesha kesho? Uwezekano wa masharti katika kesi hii unapaswa kuwa sawa na uwezekano usio na masharti kwamba kunyesha kesho, kwani kugeuza sarafu kwa ujumla haina athari yoyote kwa hali ya hewa.

Tunatumia "|" ishara ya kuandika taarifa za uwezekano wa masharti. Kwa mfano, uwezekano wa tukio $A$ kutokana na kwamba tukio $B$ limepita unaweza kuandikwa kama ifuatavyo:

$$
Pr[A|B]
$$

Kwa hivyo, wakati matukio mawili, $A$ na $B$, yanajitegemea, basi:

$$
Pr[A|B] = Pr[A] \text{ and } Pr[B|A] = Pr[B]
$$

Hali ya uhuru inaweza kurahisishwa kama ifuatavyo:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Matokeo muhimu katika nadharia ya uwezekano yanajulikana kama **Bayes Theorem**. Kimsingi inasema kuwa $Pr[A|B]$ inaweza kuandikwa upya kama ifuatavyo:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Badala ya kutumia uwezekano wa masharti na matukio maalum, tunaweza pia kuangalia uwezekano wa masharti unaohusika na viambishi viwili au zaidi vya nasibu juu ya seti ya matukio yanayowezekana. Tuseme vigezo viwili vya nasibu, $X$ na $Y$. Tunaweza kuashiria thamani yoyote inayowezekana ya $X$ kwa $x$, na thamani yoyote inayowezekana ya $Y$ kwa $y$. Tunaweza kusema, basi, kwamba anuwai mbili za nasibu ni huru ikiwa taarifa ifuatayo inashikilia:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

kwa $x$ na $y$ zote.

Hebu tufafanue zaidi maana ya kauli hii.

Tuseme kwamba seti za matokeo ya $X$ na $Y$ zimefafanuliwa kama ifuatavyo: **X** = $\{x_1, x_2, \ldots, x_i, \lddots, x_n\}$ na **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\} (Ni kawaida kuashiria seti za maadili kwa herufi kubwa zenye uso mkuu.)

Sasa tuseme umetoa sampuli ya $Y$ na uone $y_1$. Taarifa iliyo hapo juu inatuambia kwamba uwezekano wa sasa kupata $x_1$ kutoka kwa sampuli $X$ ni sawa kabisa na kama hatukuwahi kuona $y_1$. Hii ni kweli kwa $y_i$ yoyote ambayo tungeweza kupata kutoka kwa sampuli yetu ya awali ya $Y$. Hatimaye, hii ni kweli si kwa $x_1$ pekee. Kwa $x_i$ yoyote, uwezekano wa kutokea hauathiriwi na matokeo ya sampuli ya $Y$. Yote hii pia inatumika kwa kesi ambapo $X$ inachukuliwa kwanza.

Wacha tumalizie mjadala wetu juu ya hoja ya kifalsafa zaidi. Katika hali yoyote ya ulimwengu halisi, uwezekano wa tukio fulani daima hutathminiwa dhidi ya seti fulani ya habari. Hakuna "uwezekano usio na masharti" kwa maana yoyote kali sana ya neno.

Kwa mfano, tuseme nimekuuliza uwezekano kwamba nguruwe wataruka ifikapo 2030. Ingawa sikupi habari zaidi, unajua mengi kuhusu ulimwengu ambayo yanaweza kuathiri uamuzi wako. Hujawahi kuona nguruwe wakiruka. Unajua kwamba watu wengi hawatarajii kuruka. Unajua kwamba hawajajengwa kwa kweli kuruka. Na kadhalika.

Kwa hivyo, tunapozungumza kuhusu "uwezekano usio na masharti" wa tukio fulani katika muktadha wa ulimwengu halisi, neno hilo linaweza kuwa na maana tu ikiwa tunalichukulia kumaanisha kitu kama "uwezekano bila maelezo yoyote ya wazi". Uelewa wowote wa "uwezekano wa masharti" unapaswa, basi, kueleweka kila wakati dhidi ya kipande fulani cha habari.

Kwa mfano, naweza kukuuliza uwezekano kwamba nguruwe wataruka ifikapo 2030, baada ya kukupa ushahidi kwamba baadhi ya mbuzi nchini New Zealand wamejifunza kuruka baada ya miaka michache ya mafunzo. Katika kesi hii, labda utarekebisha uamuzi wako wa uwezekano kwamba nguruwe wataruka ifikapo 2030. Kwa hivyo uwezekano kwamba nguruwe wataruka ifikapo 2030 ni masharti juu ya ushahidi huu kuhusu mbuzi huko New Zealand.

## Operesheni ya moduli

<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

Usemi wa msingi zaidi na **operesheni ya modulo** ni ya aina ifuatayo: $x \mod y$.

Tofauti $x$ inaitwa gawio na tofauti $y$ kigawanyiko. Ili kufanya operesheni ya modulo na mgawanyiko mzuri na mgawanyiko mzuri, unaamua tu salio la mgawanyiko.

Kwa mfano, zingatia usemi $25 \mod 4$. Nambari 4 inaingia kwenye nambari 25 jumla ya mara 6. Salio la mgawanyiko huo ni 1. Kwa hivyo, $25 \mod 4$ ni sawa na 1. Vivyo hivyo, tunaweza kutathmini vielezi vilivyo hapa chini:


- $29 \mod 30 = 29$ (kama 30 inaingia 29 jumla ya mara 0 na salio ni 29)
- $42 \mod 2 = 0$ (kama 2 inaingia katika 42 jumla ya mara 21 na salio ni 0)
- $12 \mod 5 = 2$ (kama 5 inaingia 12 jumla ya mara 2 na salio ni 2)
- $20 \mod 8 = 4$ (na 8 inaingia katika 20 jumla ya mara 2 na salio ni 4)

Wakati mgao wa faida au kigawanyo ni hasi, utendakazi wa modulo unaweza kushughulikiwa tofauti na lugha za programu.

Hakika utakutana na kesi zilizo na gawio hasi katika cryptography. Katika kesi hii, mbinu ya kawaida ni kama ifuatavyo.


- Kwanza tambua thamani ya karibu zaidi *ya chini kuliko au sawa na* mgao ambao kigawanyaji hugawanya na salio la sifuri. Piga thamani hiyo $p$.
- Ikiwa gawio ni $x$, basi matokeo ya uendeshaji wa modulo ni thamani ya $x - p $.

Kwa mfano, tuseme kwamba mgao wa faida ni $–20$ na kigawanyaji 3. Thamani ya karibu zaidi ya chini kuliko au sawa na $–20$ ambayo 3 inagawanywa kwa usawa ni $–21$. Thamani ya $x – p$ katika kesi hii ni $–20 – (–21)$. Hii ni sawa na 1 na, kwa hivyo, $–20 \mod 3$ ni sawa na 1. Vivyo hivyo, tunaweza kutathmini vielezi vilivyo hapa chini:


- $–8 \mod 5 = 2$
- $–19 \mod 16 = 13$
- $–14 \mod 6 = 4$

Kuhusu nukuu, kwa kawaida utaona aina zifuatazo za misemo: $x = [y \mod z]$. Kwa sababu ya mabano, operesheni ya modulo katika kesi hii inatumika tu kwa upande wa kulia wa usemi. Ikiwa $y$ ni sawa na 25 na $z$ ni sawa na 4, kwa mfano, basi $x$ inatathmini hadi 1.

Bila mabano, utendakazi wa modulo hufanya kazi kwa *pande zote mbili* za usemi. Tuseme, kwa mfano, usemi ufuatao: $x = y \mod z$. Ikiwa $y$ ni sawa na 25 na $z$ ni sawa na 4, basi tunachojua ni kwamba $x \mod 4$ inatathmini hadi 1. Hii inalingana na thamani yoyote ya $x$ kutoka kwa seti $\{\ldets,–7, -3, 1, 5, 9,\ldots\}$.

Tawi la hisabati ambalo linahusisha utendakazi wa modulo kwenye nambari na misemo hurejelewa kwa **hesabu ya moduli**. Unaweza kufikiria tawi hili kama hesabu kwa kesi ambazo mstari wa nambari sio mrefu sana. Ingawa kwa kawaida tunakutana na utendakazi wa modulo kwa nambari kamili (chanya) ndani ya usimbaji fiche, unaweza pia kufanya shughuli za modulo kwa kutumia nambari zozote halisi.

### Sifa ya kuhama

Uendeshaji wa modulo mara nyingi hupatikana ndani ya cryptography. Kwa mfano, hebu tuchunguze mojawapo ya mipango maarufu ya usimbaji wa kihistoria: msimbo wa kuhama.

Hebu kwanza tufafanue. Tuseme kamusi *D* inayosawazisha herufi zote za alfabeti ya Kiingereza, kwa mpangilio, na seti ya nambari $\{0, 1, 2, \ldets, 25\}$. Chukua nafasi ya ujumbe **M**. **shift cipher** basi, ni mpango wa usimbaji fiche unaofafanuliwa kama ifuatavyo:


- Chagua kwa usawa ufunguo $k$ kati ya nafasi muhimu **K**, ambapo **K** = $\{0, 1, 2, \ldets, 25\}$ [1]
- Simba ujumbe kwa njia fiche $m \katika \mathbf{M}$, kama ifuatavyo:
    - Tenganisha $m$ kwa herufi zake binafsi $m_0, m_1, \ldots, m_i, \lddots, m_l$
    - Badilisha kila $m_i$ kuwa nambari kulingana na *D*
    - Kwa kila $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Badilisha kila $c_i$ kuwa herufi kulingana na *D*
    - Kisha unganisha $c_0, c_1, \lddots, c_l$ ili kutoa maandishi ya siri $c$
- Simbua maandishi ya siri $c$ kama ifuatavyo:
    - Badilisha kila $c_i$ kuwa nambari kulingana na *D*
    - Kwa kila $c_i$, $m_i = [(c_i – k) \mod 26]$
    - Badilisha kila $m_i$ kuwa herufi kulingana na *D*
    - Kisha unganisha $m_0, m_1, \lddots, m_l$ ili kutoa ujumbe asili $m$

Opereta wa modulo katika shifti ya kisifa huhakikisha kwamba herufi zinazunguka, ili herufi zote za maandishi ya siri zifafanuliwe. Kwa mfano, fikiria matumizi ya neno "MBWA" la kuhama.

Tuseme kwamba umechagua ufunguo kwa usawa kuwa na thamani ya 17. Herufi "O" ni sawa na 15. Bila utendakazi wa modulo, kuongezwa kwa nambari hii ya barua pepe na ufunguo kunaweza kuwa nambari ya maandishi ya siri 32. Hata hivyo, nambari hiyo ya maandishi ya siri haiwezi kugeuzwa kuwa herufi ya ciphertext, kwa kuwa alfabeti ya Kiingereza ina herufi 26 pekee. Uendeshaji wa modulo huhakikisha kwamba nambari ya maandishi ya siri ni 6 (matokeo ya $32 \mod 26$), ambayo ni sawa na herufi ya maandishi ya siri "G".

Usimbuaji wote wa neno "MBWA" na thamani kuu ya 17 ni kama ifuatavyo.


- Ujumbe = MBWA = D,O,G = 3,15,6
- $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
- $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
- $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
- $c = UGX$

Kila mtu anaweza kuelewa kwa njia angavu jinsi kiashiria cha shift kinavyofanya kazi na pengine kuitumia wenyewe. Ili kuendeleza ujuzi wako wa cryptography, hata hivyo, ni muhimu kuanza kuwa na urahisi zaidi na urasimishaji, kwani mipango itakuwa ngumu zaidi. Kwa hivyo, kwa nini hatua za msimbo wa mabadiliko zilirasimishwa.

**Maelezo:**

[1] Tunaweza kufafanua kauli hii hasa, kwa kutumia istilahi kutoka sehemu iliyotangulia. Acha kigezo kimoja cha $K$ kiwe na $K$ kama seti yake ya matokeo yanayowezekana. Kwa hivyo:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...na kadhalika. Sampuli ya kutofautisha sare $K$ mara moja ili kutoa ufunguo fulani.

## Operesheni ya XOR

<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Data yote ya kompyuta inachakatwa, kuhifadhiwa na kutumwa kwenye mitandao kwa kiwango cha biti. Miradi yoyote ya kriptografia ambayo inatumika kwa data ya kompyuta pia hufanya kazi katika kiwango kidogo.

Kwa mfano, tuseme umeandika barua-pepe kwenye ombi lako la barua-pepe. Usimbaji fiche wowote unaotuma hautokei kwenye herufi za ASCII za barua pepe yako moja kwa moja. Badala yake, inatumika kwa uwakilishi kidogo wa barua na alama nyingine katika barua pepe yako.

Operesheni muhimu ya kihisabati ya kuelewa kwa usimbaji fiche wa kisasa, kando na utendakazi wa modulo, ni utendakazi wa **XOR**, au "operesheni ya kipekee au". Operesheni hii inachukua kama pembejeo biti mbili na kutoa kama pato kidogo nyingine. Operesheni ya XOR itaashiriwa tu kama "XOR". Inatoa 0 ikiwa biti mbili ni sawa na 1 ikiwa biti mbili ni tofauti. Unaweza kuona uwezekano nne hapa chini. Alama $\oplus$ inawakilisha "XOR" :


- $0 \plus 0 = 0$
- $0 \plus 1 = 1$
- $1 \plus 0 = 1$
- $1 \plus 1 = 0$

Ili kutoa mfano, tuseme kuwa una ujumbe $m_1$ (01111001) na ujumbe $m_2$ (01011001). Uendeshaji wa XOR wa jumbe hizi mbili unaweza kuonekana hapa chini.


- $m_1 \plus m_2 = 01111001 \plus 01011001 = 00100000$

Mchakato ni moja kwa moja. Wewe kwanza XOR bits kushoto zaidi ya $m_1$ na $m_2$. Katika kesi hii hiyo ni $0 \plus 0 = 0$. Wewe kisha XOR jozi ya pili ya bits kutoka kushoto. Katika kesi hii hiyo ni $1 \plus 1 = 0$. Unaendelea na mchakato huu hadi utakapofanya operesheni ya XOR kwenye sehemu za kulia zaidi.

Ni rahisi kuona kwamba utendakazi wa XOR ni wa kubadilika, yaani $m_1 \oplus m_2 = m_2 \oplus m_1$. Kwa kuongeza, operesheni ya XOR pia ni ya ushirika. Hiyo ni, $(m_1 \plus m_2) \plus m_3 = m_1 \plus (m_2 \plus m_3)$.

Operesheni ya XOR kwenye safu mbili za urefu mbadala inaweza kuwa na tafsiri tofauti, kulingana na muktadha. Hatutajishughulisha hapa na shughuli zozote za XOR kwenye nyuzi za urefu tofauti.

Operesheni ya XOR ni sawa na kesi maalum ya kufanya operesheni ya modulo kwenye uongezaji wa biti wakati kigawanyiko ni 2. Unaweza kuona usawa katika matokeo yafuatayo:


- $(0 + 0) \mod 2 = 0 \plus 0 = 0$
- $(1 + 0) \mod 2 = 1 \plus 0 = 1$
- $(0 + 1) \mod 2 = 0 \plus 1 = 1$
- $(1 + 1) \mod 2 = 1 \plus 1 = 0$

## Udanganyifu

<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Katika mjadala wetu wa vigezo vya nasibu na sare, tulichora tofauti maalum kati ya "nasibu" na "sare". Tofauti hiyo kwa kawaida hudumishwa katika mazoezi wakati wa kuelezea vigeu vya nasibu. Hata hivyo, katika muktadha wetu wa sasa, tofauti hii inahitaji kupunguzwa na "nasibu" na "sare" hutumiwa sawa. Nitaelezea kwa nini mwishoni mwa sehemu.

Kuanza, tunaweza kuita mfuatano wa jozi wa urefu $n$ **nasibu** (au **uniform**), ikiwa ilikuwa ni matokeo ya kuchukua sampuli ya kigezo kimoja $S$ ambacho kinapa kila mfuatano wa binary wa urefu kama $n$ uwezekano sawa wa uteuzi.

Tuseme, kwa mfano, seti ya mifuatano yote miwili yenye urefu wa 8: $\{0000\ 0000, 0000\ 0001, \ldets, 1111\ 1111\}$. (Ni kawaida kuandika mfuatano wa biti 8 katika robo mbili, kila moja inaitwa **nibble**.) Hebu tuite seti hii ya mifuatano **$S_8$**.

Kwa ufafanuzi ulio hapo juu, tunaweza, basi, kuita mfuatano wa binary wa urefu wa 8 bila mpangilio (au sare), ikiwa ilikuwa ni matokeo ya kuchukua sampuli ya tofauti inayofanana $S$ ambayo inatoa kila mfuatano katika **$S_8$** uwezekano sawa wa uteuzi. Ikizingatiwa kuwa seti **$S_8$** inajumuisha $2^8$ Elements, uwezekano wa uteuzi baada ya sampuli utalazimika kuwa $1/2^8$ kwa kila mfuatano kwenye seti.

Kipengele muhimu cha kubahatisha kwa kamba ya binary ni kwamba inafafanuliwa kwa kurejelea mchakato ambao ilichaguliwa. Umbo la mfuatano wowote wa binary peke yake, kwa hivyo, hauonyeshi chochote kuhusu kubahatisha kwake katika uteuzi.

Kwa mfano, watu wengi kimaumbile wana wazo kwamba mfuatano kama $1111\ 1111$ haungeweza kuchaguliwa kwa nasibu. Lakini hii ni uwongo wazi.

Kufafanua tofauti inayofanana $S$ juu ya nyuzi jozi zote za urefu wa 8, uwezekano wa kuchagua $1111\ 1111$ kutoka kwa seti **$S_8$** ni sawa na ule wa mfuatano kama vile $0111\ 0100$. Kwa hivyo, huwezi kusema chochote kuhusu nasibu ya kamba, kwa kuchambua tu kamba yenyewe.

Tunaweza pia kuzungumza juu ya mifuatano nasibu bila kumaanisha mahususi mifuatano ya binary. Tunaweza, kwa mfano, kuzungumzia mfuatano wa nasibu wa hex $AF\ 02\ 82$. Katika hali hii, mfuatano ungechaguliwa bila mpangilio kutoka kwa seti ya mifuatano yote ya heksi yenye urefu wa 6. Hii ni sawa na kuchagua bila mpangilio mfuatano wa binary wa urefu wa 24, kwani kila tarakimu ya heksi inawakilisha biti 4.

Kwa kawaida usemi "kamba nasibu", bila sifa, hurejelea mfuatano uliochaguliwa nasibu kutoka kwa seti ya mifuatano yote yenye urefu sawa. Hivi ndivyo nilivyoeleza hapo juu. Mfuatano wa urefu $n$ unaweza, bila shaka, pia kuchaguliwa bila mpangilio kutoka kwa seti tofauti. Moja, kwa mfano, ambayo inajumuisha tu sehemu ndogo ya mifuatano yote ya urefu $n$, au labda seti inayojumuisha mifuatano ya urefu tofauti. Katika hali hizo, hata hivyo, hatungeirejelea kama "kamba nasibu", bali "kamba ambayo imechaguliwa nasibu kutoka kwa baadhi ya seti **S**".

Dhana kuu ndani ya cryptography ni ile ya pseudorandomness. **Mfuatano wa uwongo** wa urefu wa $n$ unaonekana *kana kwamba* ni tokeo la sampuli ya kigezo kimoja $S$ ambacho kinatoa kila mfuatano katika **$S_n$** uwezekano sawa wa uteuzi. Kwa kweli, hata hivyo, mfuatano huo ni matokeo ya kuchukua sampuli ya kigezo kimoja cha $S'$ ambacho hufafanua tu usambazaji wa uwezekano—sio lazima uwe na uwezekano sawa wa matokeo yote yanayowezekana—kwenye kikundi kidogo cha **$S_n$**. Jambo muhimu hapa ni kwamba hakuna mtu anayeweza kutofautisha kati ya sampuli kutoka $S$ na $S'$, hata ukichukua nyingi kati yao.

Tuseme, kwa mfano, tofauti ya nasibu $S$. Seti yake ya matokeo ni **$S_{256}$**, hii ni seti ya nyuzi jozi zote za urefu wa 256. Seti hii ina $2^{256}$ Elements. Kila kipengele kina uwezekano sawa wa uteuzi, $1/2^{256}$, baada ya sampuli.

Kwa kuongeza, tuseme kigezo cha nasibu $S'$. Seti yake ya matokeo inajumuisha tu $2^{128}$ mifuatano ya jozi ya urefu wa 256. Ina usambazaji wa uwezekano juu ya mifuatano hiyo, lakini usambazaji huu si lazima ufanane.

Tuseme kwamba sasa nilichukua 1000 za sampuli kutoka $S$ na 1000 za sampuli kutoka $S'$ na kukupa seti mbili za matokeo. Ninakuambia ni seti gani ya matokeo inahusishwa na kutofautisha bila mpangilio. Ifuatayo, mimi huchukua sampuli kutoka kwa moja ya anuwai mbili za nasibu. Lakini wakati huu sikuambii ni sampuli gani isiyo ya kawaida. Ikiwa $S'$ zilikuwa pseudorandom, basi wazo ni kwamba uwezekano wako wa kufanya nadhani sahihi ya ni kigezo kipi nilichotoa sampuli sio bora kuliko $1/2$.

Kwa kawaida, mfuatano wa uwongo wa urefu wa $n$ unatolewa kwa kuchagua bila mpangilio mfuatano wa ukubwa $n - x$, ambapo $x$ ni nambari kamili chanya, na kuitumia kama kiingizio cha algoriti ya upanuzi. Mfuatano huu wa nasibu wa ukubwa $n – x$ unajulikana kama **seed**.

Kamba za uwongo ni dhana kuu ya kufanya usimbaji fiche kuwa wa vitendo. Fikiria, kwa mfano, misimbo ya mtiririko. Kwa msimbo wa mtiririko, ufunguo uliochaguliwa kwa nasibu huchomekwa kwenye algoriti ya upanuzi ili kutoa mfuatano mkubwa zaidi wa uwongo. Mfuatano huu wa uwongo kisha unaunganishwa na maandishi wazi kupitia utendakazi wa XOR ili kutoa maandishi ya siri.

Iwapo hatukuweza kutoa aina hii ya mfuatano wa uwongo kwa msimbo wa mtiririko, basi tungehitaji ufunguo ambao ni mrefu kama ujumbe kwa usalama wake. Hii sio chaguo la vitendo sana katika hali nyingi.

Dhana ya uwongo iliyojadiliwa katika sehemu hii inaweza kufafanuliwa rasmi zaidi. Pia inaenea kwa miktadha mingine. Lakini hatuhitaji kuingia kwenye mjadala huo hapa. Unachohitaji kuelewa kwa angavu kwa sehemu kubwa ya kriptografia ni tofauti kati ya kamba ya nasibu na pseudorandom. [2]

Sababu ya kuacha tofauti kati ya "nasibu" na "sare" katika mjadala wetu inapaswa pia kuwa wazi. Kwa mazoezi, kila mtu hutumia neno pseudorandom kuashiria mfuatano unaoonekana **kana kwamba** ni matokeo ya kuchukua sampuli ya kigezo kimoja $S$. Kwa kusema kweli, tunapaswa kuita mfuatano kama huo "sare ya uwongo," tukitumia lugha yetu kutoka hapo awali. Kwa vile neno "pseudo-uniform" ni fujo na halitumiwi na mtu yeyote, hatutalitambulisha hapa kwa uwazi. Badala yake, tunaacha tu tofauti kati ya "nasibu" na "sare" katika muktadha wa sasa.

**Maelezo**

[2] Iwapo ungependa kupata maelezo rasmi zaidi kuhusu masuala haya, unaweza kushauriana na Katz na Lindell *Introduction to Modern Cryptography*, esp. sura ya 3.

# Misingi ya Hisabati ya Crystalgraphy 2

<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

## Nadharia ya nambari ni nini?

<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>

Sura hii inashughulikia mada ya juu zaidi juu ya misingi ya hisabati ya kriptografia: nadharia ya nambari. Ingawa nadharia ya nambari ni muhimu kwa kriptografia linganifu (kama vile Rijndael Cipher), ni muhimu sana katika mpangilio wa kriptografia ya ufunguo wa umma.

Ikiwa unapata maelezo ya nadharia ya nambari kuwa ngumu, ningependekeza usomaji wa hali ya juu mara ya kwanza. Unaweza kurudi kwake wakati wowote baadaye.

___

Unaweza kubainisha **nadharia ya nambari** kama somo la sifa za nambari kamili na utendaji wa hisabati unaofanya kazi na nambari kamili.

Fikiria, kwa mfano, kwamba nambari zozote mbili $a$ na $N$ ni **coprimes** (au **primes**) ikiwa kigawanyo chao kikubwa zaidi ni sawa na 1. Tuseme sasa nambari kamili $N$. Je, ni tarakimu ngapi ndogo zaidi ya $N$ ambazo ni nakala zilizo na $N$? Je, tunaweza kutoa kauli za jumla kuhusu majibu ya swali hili? Hizi ni aina za kawaida za maswali ambayo nadharia ya nambari hutafuta kujibu.

Nadharia ya kisasa ya nambari inategemea zana za algebra ya kufikirika. Sehemu ya **aljebra abstract** ni taaluma ndogo ya hisabati ambapo vitu vikuu vya uchanganuzi ni vitu dhahania vinavyojulikana kama miundo ya aljebra. **muundo wa aljebra** ni seti ya Elements iliyounganishwa na operesheni moja au zaidi, ambayo hukutana na axioms fulani. Kupitia miundo ya aljebra, wanahisabati wanaweza kupata maarifa kuhusu matatizo mahususi ya hisabati, kwa kujiondoa kutoka kwa maelezo yao.

Uga wa aljebra abstract wakati mwingine pia huitwa algebra ya kisasa. Unaweza pia kukutana na dhana ya **hisabati ya kufikirika** (au **hisabati safi**). Neno hili la mwisho si marejeleo ya aljebra ya kufikirika, bali ina maana ya utafiti wa hisabati kwa ajili yake binafsi, na si kwa kuangalia tu matumizi yanayowezekana.

Seti kutoka aljebra dhahania zinaweza kushughulika na aina nyingi za vitu, kutoka kwa mabadiliko ya kuhifadhi umbo kwenye pembetatu ya usawa hadi muundo wa mandhari. Kwa nadharia ya nambari, tunazingatia tu seti za Elements ambazo zina nambari kamili au vitendakazi vinavyofanya kazi na nambari kamili.

## Vikundi

<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Dhana ya msingi katika hisabati ni ile ya seti ya Elements. Seti kawaida huonyeshwa kwa ishara za sifa na Elements ikitenganishwa na koma.

Kwa mfano, seti ya nambari zote ni $\{…, -2, -1, 0, 1, 2, …\}$. Miduara hapa inamaanisha kuwa muundo fulani unaendelea katika mwelekeo fulani. Kwa hivyo seti ya nambari zote pia inajumuisha $3, 4, 5, 6$ na kadhalika, na vile vile $-3, -4, -5, -6$ na kadhalika. Seti hii ya nambari zote kwa kawaida huashiriwa na $\mathbb{Z}$.

Mfano mwingine wa seti ni $\mathbb{Z} \mod 11$, au seti ya nambari zote modulo 11. Tofauti na seti nzima ya $\mathbb{Z}$, seti hii ina nambari maalum ya Elements, yaani $\{0, 1, \ldets, 9, 10\}$.

Kosa la kawaida ni kufikiria kuwa seti ya $\mathbb{Z} \mod 11$ ni $\{-10, -9, \ldets, 0, \ldets, 9, 10\}$. Lakini hii sivyo, kwa kuzingatia jinsi tulivyofafanua operesheni ya modulo hapo awali. Nambari kamili hasi zilizopunguzwa na modulo ya 11 kwenye $\{0, 1, \ldets, 9, 10\}$. Kwa mfano, usemi $-2 \mod 11$ unakaribia kufikia $9$, huku usemi $-27 \mod 11$ ukikaribia $5$.

Dhana nyingine ya msingi katika hisabati ni ile ya operesheni ya binary. Hii ni operesheni yoyote ambayo inachukua mbili Elements kutoa ya tatu. Kwa mfano, kutoka kwa hesabu za kimsingi na aljebra, ungefahamu shughuli nne za kimsingi za mfumo wa jozi: kujumlisha, kutoa, kuzidisha na kugawanya.

Dhana hizi mbili za msingi za hisabati, seti na uendeshaji wa mfumo wa jozi, hutumiwa kufafanua dhana ya kikundi, muundo muhimu zaidi katika aljebra ya kufikirika.

Hasa, tuseme operesheni ya binary $\circ$. Kwa kuongeza, tuseme seti fulani ya Elements **S** iliyo na utendakazi huo. Yote "vifaa" inamaanisha hapa ni kwamba operesheni $\circ$ inaweza kufanywa kati ya Elements zozote mbili kwenye seti **S**.

Mchanganyiko $\langle \mathbf{S}, \circ \rangle$, basi, ni **kundi** ikiwa inakidhi masharti manne maalum, yanayojulikana kama axioms za kikundi.

1. Kwa $a$ na $b$ zozote ambazo ni Elements ya $\mathbf{S}$, $a \circ b$ pia ni kipengele cha $\mathbf{S}$. Hii inajulikana kama **hali ya kufungwa**.

2. Kwa $a$, $b$, na $c$ zozote ambazo ni Elements ya $\mathbf{S}$, ni hali ambayo $(a \circ b) \circ c = a \circ (b \circ c)$. Hii inajulikana kama **hali ya ushirika**.

3. Kuna kipengele cha kipekee $e$ katika $\mathbf{S}$, hivi kwamba kwa kila kipengele $a$ katika $\mathbf{S}$, mlinganyo ufuatao unashikilia: $e \circ a = a \circ e = a$. Kwa vile kuna kipengele kimoja tu kama $e$, kinaitwa **kipengele cha utambulisho**. Hali hii inajulikana kama **hali ya utambulisho**.

4. Kwa kila kipengele $a$ katika $\mathbf{S}$, kuna kipengele $b$ katika $\mathbf{S}$, kiasi kwamba mlinganyo ufuatao unashikilia: $a \circ b = b \circ a = e$, ambapo $e$ ni kipengele cha utambulisho. Kipengele $b$ hapa kinajulikana kama **kipengele kinyume**, na kwa kawaida huashiriwa kama $a^{-1}$. Hali hii inajulikana kama **hali kinyume** au **hali ya kutobadilika**.

Hebu tuchunguze vikundi mbele kidogo. Onyesha seti ya nambari zote kwa $\mathbb{Z}$. Seti hii ikiunganishwa na nyongeza ya kawaida, au $\langle \mathbb{Z}, + \rangle$, inafaa kwa uwazi ufafanuzi wa kikundi, kwani hukutana na viambishi vinne vilivyo hapo juu.

1. Kwa $x$ na $y$ zozote ambazo ni Elements ya $\mathbb{Z}$, $x + y$ pia ni kipengele cha $\mathbb{Z}$. Kwa hivyo $\langle \mathbb{Z}, + \rangle$ inakidhi hali ya kufungwa.

2. Kwa $x$, $y$, na $z$ zozote ambazo ni Elements ya $\mathbb{Z}$, $(x + y) + z = x + (y + z)$. Kwa hivyo $\langle \mathbb{Z}, + \rangle$ hukutana na hali ya ushirika.

3. Kuna kipengele cha utambulisho katika $\langle \mathbb{Z}, + \rangle$, yaani 0. Kwa $x$ yoyote katika $\mathbb{Z}$, inashikilia kwamba: $0 + x = x + 0 = x$. Kwa hivyo $\langle \mathbb{Z}, + \rangle$ inakidhi hali ya utambulisho.

4. Hatimaye, kwa kila kipengele $x$ katika $\mathbb{Z}$, kuna $y$ ili $x + y = y + x = 0$. Ikiwa $x$ walikuwa 10, kwa mfano, $y$ ingekuwa $-10$ (katika hali ambayo $x$ ni 0, $y$ pia ni 0). Kwa hivyo $\langle \mathbb{Z}, + \rangle$ hukutana na hali ya kinyume.

Muhimu zaidi, kwamba seti ya nambari kamili na nyongeza hujumuisha kikundi haimaanishi kuwa inajumuisha kikundi chenye kuzidisha. Unaweza kuthibitisha hili kwa kujaribu $\langle \mathbb{Z}, \cdot \rangle$ dhidi ya viambishi vinne vya vikundi (ambapo $\cdot$ inamaanisha kuzidisha kawaida).

Axioms mbili za kwanza ni dhahiri zinashikilia. Kwa kuongeza, chini ya kuzidisha kipengele cha 1 kinaweza kutumika kama kipengele cha utambulisho. Nambari kamili $x$ ikizidishwa na 1, ambayo hutoa $x$. Walakini, $\langle \mathbb{Z}, \cdot \rangle$ haifikii hali ya kinyume. Hiyo ni, hakuna kipengele cha kipekee $y$ katika $\mathbb{Z}$ kwa kila $x$ katika $\mathbb{Z}$, ili $x \cdot y = 1$.

Kwa mfano, tuseme kwamba $x = 22$. Ni thamani gani $y$ kutoka kwa seti $\mathbb{Z}$ iliyozidishwa na $x$ ingeweza kutoa kipengele cha 1 cha utambulisho? Thamani ya $1/22$ ingefanya kazi, lakini hii haiko katika seti ya $\mathbb{Z}$. Kwa kweli, unaingia kwenye tatizo hili kwa nambari yoyote $x$, zaidi ya maadili ya 1 na -1 (ambapo $y$ italazimika kuwa 1 na -1 mtawalia).

Ikiwa tuliruhusu nambari halisi kwa seti yetu, basi shida zetu hupotea kwa kiasi kikubwa. Kwa kipengele chochote $x$ katika seti, kuzidisha kwa $1/x$ hutoa mavuno 1. Kwa vile visehemu hujumuishwa katika seti ya nambari halisi, kinyume kinaweza kupatikana kwa kila nambari halisi. Isipokuwa ni sifuri, kwani kuzidisha kwa sifuri kamwe hakutatoa kipengele cha 1 cha utambulisho. Kwa hivyo, seti ya nambari halisi zisizo sifuri zilizo na kuzidisha kwa hakika ni kikundi.

Baadhi ya vikundi hutimiza masharti ya tano ya jumla, inayojulikana kama **hali ya mawasiliano**. Hali hii ni kama ifuatavyo:


- Tuseme kikundi $G$ na seti **S** na opereta binary $\circ$. Tuseme kuwa $a$ na $b$ ni Elements kati ya **S**. Ikiwa ni kwamba $a \circ b = b \circ a$ kwa Elements $a$ na $b$ zozote mbili katika **S**, basi $G$ inakidhi hali ya mawasiliano.

Kikundi chochote kinachotimiza masharti ya mawasiliano kinajulikana kama **kikundi chenye mabadiliko**, au **kikundi cha Abelian** (baada ya Niels Henrik Abel). Ni rahisi kuthibitisha kuwa seti ya nambari halisi juu ya kujumlisha na seti ya nambari kamili juu ya kuongeza ni vikundi vya Abelian. Seti ya nambari kamili juu ya kuzidisha sio kikundi hata kidogo, kwa hivyo ipso facto haiwezi kuwa kikundi cha Abelian. Seti ya nambari zisizo sifuri halisi juu ya kuzidisha, kwa kulinganisha, pia ni kikundi cha Abelian.

Unapaswa kuzingatia mikataba miwili muhimu juu ya nukuu. Kwanza, ishara "+" au "×" mara nyingi zitatumika kuashiria shughuli za kikundi, hata wakati Elements sio, kwa kweli, nambari. Katika hali hizi, hupaswi kufasiri ishara hizi kama nyongeza ya kawaida ya hesabu au kuzidisha. Badala yake, ni shughuli zilizo na mfanano wa dhahania tu na shughuli hizi za hesabu.

Isipokuwa unarejelea mahsusi kujumlisha au kuzidisha hesabu, ni rahisi zaidi kutumia alama kama vile $\circ$ na $\diamond$ kwa shughuli za kikundi, kwani hizi hazina miunganisho iliyokita mizizi sana kiutamaduni.

Pili, kwa sababu hiyo hiyo ambayo "+" na "×" hutumiwa mara nyingi kwa kuonyesha shughuli zisizo za hesabu, utambulisho wa Elements wa vikundi mara nyingi huonyeshwa na "0" na "1", hata wakati Elements katika vikundi hivi sio nambari. Isipokuwa unarejelea kipengele cha utambulisho cha kikundi kilicho na nambari, ni rahisi zaidi kutumia alama isiyoegemea upande wowote kama vile “$e$” ili kuonyesha kipengele cha utambulisho.

Seti nyingi tofauti na muhimu sana za maadili katika hisabati zilizo na shughuli fulani za binary ni vikundi. Programu za kriptografia, hata hivyo, hufanya kazi tu na seti za nambari kamili au angalau Elements ambazo zinafafanuliwa na nambari kamili, ambayo ni, ndani ya kikoa cha nadharia ya nambari. Kwa hivyo, seti zilizo na nambari halisi isipokuwa nambari kamili hazitumiki katika programu za kriptografia.

Wacha tumalizie kwa kutoa mfano wa Elements ambao unaweza "kuelezewa na nambari kamili", ingawa sio nambari kamili. Mfano mzuri ni pointi za curves elliptic. Ingawa sehemu yoyote kwenye kiwiko cha duaradufu ni dhahiri si nambari kamili, uhakika kama huo kwa hakika unafafanuliwa na nambari mbili kamili.

Mikondo ya mviringo, kwa mfano, ni muhimu kwa Bitcoin. Jozi yoyote ya kawaida ya Bitcoin ya ufunguo wa kibinafsi na wa umma huchaguliwa kutoka kwa seti ya pointi ambazo zinafafanuliwa na curve ifuatayo ya mviringo:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(idadi kuu kubwa zaidi chini ya $2^{256}$). $x$-coordinate ni ufunguo wa faragha na $y$-coordinate ni ufunguo wako wa umma.

Shughuli katika Bitcoin kwa kawaida huhusisha kufunga matokeo kwa funguo moja au zaidi za umma kwa njia fulani. Thamani kutoka kwa miamala hii inaweza, basi, kufunguliwa kutengeneza saini za kidijitali kwa funguo za faragha zinazolingana.

## Vikundi vya baiskeli

<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Tofauti kuu tunayoweza kuchora ni kati ya **kikomo** na **kikundi kisicho na kikomo**. Ya kwanza ina nambari ya mwisho ya Elements, wakati ya mwisho ina idadi isiyo na kipimo ya Elements. Nambari ya Elements katika kikundi chochote chenye kikomo inajulikana kama **mpangilio wa kikundi**. Fiche zote za kimatendo zinazohusisha matumizi ya vikundi hutegemea vikundi vyenye ukomo (nambari-kinadharia).

Ndani ya usimbaji fiche wa ufunguo wa umma, aina fulani ya vikundi vya Kiabeli vilivyo na kikomo vinavyojulikana kama vikundi vya mzunguko ni muhimu sana. Ili kuelewa vikundi vya mzunguko, kwanza tunahitaji kuelewa dhana ya udhihirisho wa kipengele cha kikundi.

Tuseme kikundi $G$ chenye operesheni ya kikundi $\circ$, na hiyo $a$ ni kipengele cha $G$. Usemi $a^n$, basi, unapaswa kufasiriwa kama kipengele $a$ pamoja na chenyewe jumla ya mara $n - 1$. Kwa mfano, $a^2$ ina maana $a \circ a$, $a^3$ ina maana $a \circ a \circ a$, na kadhalika. (Kumbuka kwamba ufafanuzi hapa si lazima uwe ufafanuzi katika maana ya kawaida ya hesabu.)

Hebu tugeukie mfano. Tuseme kwamba $G = \langle \mathbb{Z} \mod 7, + \rangle$, na kwamba thamani yetu ya $a$ ni sawa na 4. Katika kesi hii, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Vinginevyo, $a^4$ ingewakilisha $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Baadhi ya vikundi vya Abelian vina Elements moja au zaidi, ambayo inaweza kutoa kundi lingine la Elements kupitia upanuzi unaoendelea. Elements hizi huitwa **jenereta** au **primitive Elements**.

Darasa muhimu la vikundi kama hivyo ni $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, ambapo $N$ ni nambari kuu. Alama $\mathbb{Z}^*$ hapa inamaanisha kuwa kikundi kina nambari kamili zisizo sifuri na chanya chini ya $N$. Kundi kama hilo, kwa hiyo, daima lina $ N - 1 $ Elements.

Fikiria, kwa mfano, $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Kikundi hiki kina Elements zifuatazo: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Mpangilio wa kundi hili ni 10 (ambayo kwa hakika ni sawa na $11 - 1$).

Hebu tuchunguze kufafanua kipengele cha 2 kutoka kwa kikundi hiki. Hesabu za hadi $2^{12}$ zimeonyeshwa hapa chini. Kumbuka kuwa katika upande wa kushoto wa mlingano, kipeo kinarejelea upanuzi wa kipengele cha kikundi. Katika mfano wetu mahususi, hii kwa kweli inahusisha ufafanuzi wa hesabu kwenye upande wa kulia wa equation (lakini inaweza pia kuhusisha, kwa mfano, nyongeza). Ili kufafanua, nimeandika operesheni inayorudiwa, badala ya fomu ya kielelezo upande wa kulia.


- $2^1 = 2 \mod 11$
- $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
- $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
- $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
- $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
- $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
- $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
- $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
- $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
- $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
- $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11 $
- $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 1$ 1$

Ukiangalia kwa makini, unaweza kuona kwamba kufanya ufafanuzi kwenye kipengele cha 2 kwa mizunguko kupitia Elements yote ya $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ kwa mpangilio ufuatao: 2, 4, 8, 5, 10, 9, 7, 3, 6, eleza $2, {1} iliendelea baada ya $2 $. hupitia Elements zote tena na kwa mpangilio sawa. Kwa hivyo, kipengele cha 2 ni jenereta katika $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Ingawa $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ ina jenereta nyingi, sio Elements zote za kikundi hiki ni jenereta. Fikiria, kwa mfano, kipengele cha 3. Kupitia maelezo 10 ya kwanza, bila kuonyesha mahesabu magumu, hutoa matokeo yafuatayo:


- $3^1 = 3 \mod 11$
- $3^2 = 9 \mod 11$
- $3^3 = 5 \mod 11$
- $3^4 = 4 \mod 11$
- $3^5 = 1 \mod 11$
- $3^6 = 3 \mod 11$
- $3^7 = 9 \mod 11$
- $3^8 = 5 \mod 11$
- $3^9 = 4 \mod 11$
- $3^{10} = 1 \mod 11$

Badala ya kuendesha baiskeli kupitia thamani zote katika $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, upanuzi wa kipengele cha 3 husababisha tu sehemu ndogo ya maadili hayo: 3, 9, 5, 4, na 1. Baada ya ufafanuzi wa tano, maadili haya huanza kujirudia.

Sasa tunaweza kufafanua **kikundi cha mzunguko** kama kikundi chochote kilicho na angalau jenereta moja. Hiyo ni, kuna angalau kipengele kimoja cha kikundi ambacho unaweza kuzalisha kikundi kingine cha Elements kwa njia ya ufafanuzi.

Huenda umeona katika mfano wetu hapo juu kwamba $2^{10}$ na $3^{10}$ ni sawa na $1 \mod 11$. Kwa kweli, ingawa hatutafanya hesabu, ubainishaji kwa 10 wa kipengele chochote katika kikundi $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ itatoa $1 \mod 11$. Kwa nini hali iko hivi?

Hili ni swali muhimu, lakini inachukua kazi fulani kujibu.

Kuanza, chukulia nambari mbili chanya $a$ na $N$. Nadharia muhimu katika nadharia ya nambari inasema kwamba $a$ ina modulo ya kinyume cha kuzidisha $N$ (yaani, nambari kamili $b$ ili $a \cdot b = 1 \mod N$) ikiwa na ikiwa tu kigawanyiko kikubwa zaidi cha kawaida kati ya $a$ na $N$ ni sawa na 1. Hiyo ni, ikiwa $a$ na $N$ ni coprimes.

Kwa hivyo, kwa kikundi chochote cha nambari kamili kilicho na moduli ya kuzidisha $N$, ni nakala ndogo tu zilizo na $N$ ndizo zimejumuishwa kwenye seti. Tunaweza kuashiria hii iliyowekwa na $\mathbb{Z}^c \mod N$.

Kwa mfano, tuseme $N$ ni 10. Nambari kamili 1, 3, 7, na 9 pekee ndizo zilizo na 10. Kwa hivyo seti $\mathbb{Z}^c \mod 10$ inajumuisha $\{1, 3, 7, 9\}$ pekee. Huwezi kuunda kikundi chenye modulo kamili ya 10 ya kuzidisha kwa kutumia nambari kamili nyingine kati ya 1 na 10. Kwa kundi hili mahususi, vinyume ni jozi 1 na 9, na 3 na 7.

Katika hali ambapo $N$ yenyewe ni ya kwanza, nambari zote kamili kutoka 1 hadi $N - 1$ ni nakala zilizo na $N$. Kundi kama hilo, kwa hivyo, lina agizo la $ N - 1 $. Kwa kutumia nukuu yetu ya awali, $\mathbb{Z}^c \mod N$ ni sawa na $\mathbb{Z}^* \mod N$ wakati $N$ ni ya kwanza. Kikundi tulichochagua kwa mfano wetu wa awali, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, ni mfano mahususi wa aina hii ya vikundi.

Kisha, chaguo za kukokotoa $\phi(N)$ hukokotoa nambari ya malipo hadi nambari $N$, na inajulikana kama **kitendakazi cha Euler's Phi**. [1] Kulingana na **Nadharia ya Euler**, wakati wowote nambari kamili $a$ na $N$ ni coprimes, zifuatazo hushikilia:


- $a^{\phi(N)} \mod N = 1 \mod N$

Hii ina maana muhimu kwa darasa la vikundi $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ ambapo $N$ ndio msingi. Kwa vikundi hivi, upanuzi wa kipengele cha kikundi huwakilisha ufafanuzi wa hesabu. Hiyo ni, $a^{\phi(N)} \mod N$ inawakilisha utendakazi wa hesabu $a^{\phi(N)} \mod N$. Kwa vile kipengele chochote $a$ katika vikundi hivi vya kuzidisha ni coprime na $N$, inamaanisha kuwa $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.

Nadharia ya Euler ni matokeo muhimu sana. Kuanza, inadokeza kwamba Elements zote katika $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ zinaweza tu kuzunguka kupitia idadi ya thamani kwa ubainishi unaogawanyika katika $N - 1$. Kwa upande wa $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, hii ina maana kwamba kila kipengele kinaweza tu kuzunguka kupitia 2, 5, au 10 Elements. Kikundi huthamini ambacho kipengele chochote hupitia baada ya upanuzi hujulikana kama **mpangilio wa kipengele**. Kipengele kilicho na utaratibu sawa na utaratibu wa kikundi ni jenereta.

Zaidi ya hayo, nadharia ya Euler inadokeza kwamba tunaweza kujua kila wakati matokeo ya $a^{N - 1} \mod N$ kwa kikundi chochote $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ ambapo $N$ ni bora. Hii ni hivyo bila kujali jinsi mahesabu halisi yanaweza kuwa magumu.

Kwa mfano, tuseme kikundi chetu ni $\mathbb{Z}^* \mod 160,481,182$ (ambapo 160,481,182 hakika ni nambari kuu). Tunajua kwamba nambari zote 1 hadi 160,481,181 lazima ziwe Elements za kikundi hiki, na kwamba $\phi(n) = 160,481,181$. Ingawa hatuwezi kufanya hatua zote katika hesabu, tunajua kwamba misemo kama vile $514^{160,481,181}$, $2,005^{160,481,181}$, na $256,212^{160,481,181}$ lazima zote zitathminiwe hadi $1,2,8.

**Maelezo:**

[1] Chaguo za kukokotoa hufanya kazi kama ifuatavyo. Nambari kamili $N$ inaweza kujumuishwa katika bidhaa ya msingi. Tuseme kwamba $N$ fulani imeainishwa kama ifuatavyo: $p_1^{e1} \cdot p_2^{e2} \cdot \ldets \cdot p_m^{em}$ ambapo $p$ zote ni nambari kuu na $e$ zote ni nambari kamili zaidi kuliko au sawa na 1. Kisha:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Fomula ya utendakazi ya Euler ya Phi ya uwekaji alama mkuu wa $N$.

## Viwanja

<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Kundi ni muundo msingi wa aljebra katika aljebra abstract, lakini kuna mengi zaidi. Muundo mwingine pekee wa aljebra unaohitaji kuufahamu ni ule wa **uwanja**, haswa ule wa **uga wenye kikomo**. Aina hii ya muundo wa aljebra hutumiwa mara kwa mara katika usimbaji fiche, kama vile Kiwango cha Juu cha Usimbaji fiche. Mwisho ni mpango mkuu wa usimbuaji wa ulinganifu ambao utakutana nao katika mazoezi.

Sehemu inatokana na dhana ya kikundi. Hasa, **sehemu** ni seti ya Elements **S** iliyo na waendeshaji binary wawili $\circ$ na $\diamond$, ambayo inatimiza masharti yafuatayo:

1. Seti **S** iliyo na $\circ$ ni kikundi cha Abelian.

2. Seti **S** iliyo na $\diamond$ ni kikundi cha Abelian kwa "isiyo ya sifuri" Elements.

3. Seti **S** iliyo na waendeshaji wawili inakidhi kile kinachojulikana kama hali ya usambazaji: Tuseme $a$, $b$, na $c$ ni Elements ya **S**. Kisha **S** iliyo na waendeshaji wawili hukutana na mali ya ugawaji wakati $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Kumbuka kuwa, kama ilivyo kwa vikundi, ufafanuzi wa uwanja ni wa kufikirika sana. Haifanyi madai yoyote kuhusu aina za Elements katika **S**, au kuhusu utendakazi $\circ$ na $\diamond$. Inasema tu kwamba uga ni seti yoyote ya Elements yenye shughuli mbili ambazo masharti matatu hapo juu yanashikilia. (Kipengele cha "sifuri" katika kundi la pili la Abelian kinaweza kufasiriwa kidhahiri.)

Kwa hivyo ni nini kinachoweza kuwa mfano wa shamba? Mfano mzuri ni seti ya $\mathbb{Z} \mod 7$, au $\{0, 1, \lddots, 7\}$ iliyofafanuliwa juu ya nyongeza ya kawaida (badala ya $\circ$ hapo juu) na kuzidisha kawaida (badala ya $\diamond$ hapo juu).

Kwanza, $\mathbb{Z} \mod 7$ inatimiza masharti ya kuwa kikundi cha Abelian baada ya kuongezwa, na inatimiza masharti ya kuwa kikundi cha Abelian juu ya kuzidisha ikiwa utazingatia tu Elements isiyo ya sufuri. Pili, mchanganyiko wa kuweka na waendeshaji wawili hukutana na hali ya kusambaza.

Inafaa sana kuchunguza madai haya kwa kutumia thamani fulani. Hebu tuchukue thamani za majaribio 5, 2, na 3, baadhi ya Elements iliyochaguliwa bila mpangilio kutoka kwa seti $\mathbb{Z} \mod 7$, ili kukagua uga $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Tutatumia maadili haya matatu kwa mpangilio, inavyohitajika ili kuchunguza hali fulani.

Hebu tuchunguze kwanza ikiwa $\mathbb{Z} \mod 7$ iliyo na nyongeza ni kikundi cha Abelian.

1. **Hali ya kufungwa**: Hebu tuchukue 5 na 2 kama maadili yetu. Katika hali hiyo, $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Kwa kweli hii ni kipengele cha $\mathbb{Z} \mod 7$, kwa hivyo matokeo yanaendana na hali ya kufungwa.

2. **Hali ya ushirika**: Hebu tuchukue 5, 2, na 3 kama maadili yetu. Katika hali hiyo, $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Hii inalingana na hali ya ushirika.

3. **Hali ya utambulisho**: Hebu tuchukue 5 kama thamani yetu. Katika hali hiyo, $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Kwa hivyo 0 inaonekana kuwa kipengele cha utambulisho cha nyongeza.

4. **Hali ya kinyume**: Zingatia kinyume cha 5. Inahitajika kuwa $[5 + d] \mod 7 = 0$, kwa thamani fulani ya $d$. Katika hali hii, thamani ya kipekee kutoka $\mathbb{Z} \mod 7$ ambayo inakidhi hali hii ni 2.

5. **Hali ya mawasiliano**: Hebu tuchukue 5 na 3 kama maadili yetu. Katika hali hiyo, $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Hii inalingana na hali ya mawasiliano.

Seti ya $\mathbb{Z} \mod 7$ iliyo na nyongeza inaonekana wazi kuwa ni kikundi cha Abelian. Hebu sasa tuchunguze ikiwa $\mathbb{Z} \mod 7$ iliyo na kuzidisha ni kikundi cha Abelian kwa Elements zote zisizo na sufuri.

1. **Hali ya kufungwa**: Hebu tuchukue 5 na 2 kama maadili yetu. Katika hali hiyo, $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Hiki pia ni kipengele cha $\mathbb{Z} \mod 7$, kwa hivyo matokeo yanaendana na hali ya kufungwa.

2. **Hali ya ushirika**: Hebu tuchukue 5, 2, na 3 kama maadili yetu. Katika hali hiyo, $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Hii inalingana na hali ya ushirika.

3. **Hali ya utambulisho**: Hebu tuchukue 5 kama thamani yetu. Katika hali hiyo, $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Kwa hivyo 1 inaonekana kuwa kipengele cha utambulisho cha kuzidisha.

4. **Hali ya kinyume**: Zingatia kinyume cha 5. Inahitajika kuwa $[5 \cdot d] \mod 7 = 1$, kwa thamani fulani ya $d$. Thamani ya kipekee kutoka $\mathbb{Z} \mod 7$ ambayo inakidhi hali hii ni 3. Hii inalingana na hali ya kinyume.

5. **Hali ya mawasiliano**: Hebu tuchukue 5 na 3 kama maadili yetu. Katika hali hiyo, $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Hii inalingana na hali ya mawasiliano.

Seti ya $\mathbb{Z} \mod 7$ inaonekana kukidhi sheria za kuwa kikundi cha Abelian inapounganishwa na ama kuongeza au kuzidisha juu ya Elements isiyo ya sufuri.

Hatimaye, seti hii pamoja na waendeshaji wote inaonekana kukidhi hali ya usambazaji. Wacha tuchukue 5, 2, na 3 kama maadili yetu. Tunaweza kuona kwamba $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Sasa tumeona kuwa $\mathbb{Z} \mod 7$ iliyo na kujumlisha na kuzidisha hukutana na misemo ya sehemu yenye kikomo wakati wa kujaribu na thamani fulani. Bila shaka, tunaweza pia kuonyesha kwamba kwa ujumla, lakini si kufanya hivyo hapa.

Tofauti kuu ni kati ya aina mbili za nyanja: nyuga zenye mwisho na zisizo na kikomo.

**sehemu isiyo na kikomo** inajumuisha sehemu ambayo seti **S** ni kubwa sana. Seti ya nambari halisi $\mathbb{R}$ iliyo na nyongeza na kuzidisha ni mfano wa uga usio na kikomo. **Sehemu yenye kikomo**, inayojulikana pia kama **uga wa Galois**, ni sehemu ambayo seti **S** ina kikomo. Mfano wetu hapo juu wa $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ ni sehemu yenye kikomo.

Katika kriptografia, tunavutiwa kimsingi na sehemu zenye ukomo. Kwa ujumla, inaweza kuonyeshwa kuwa sehemu yenye kikomo ipo kwa baadhi ya seti ya Elements **S** ikiwa na tu ikiwa ina $p^m$ Elements, ambapo $p$ ni nambari kuu na $m$ nambari chanya kubwa kuliko au sawa na moja. Kwa maneno mengine, ikiwa mpangilio wa seti fulani **S** ni nambari kuu ($p^m$ ambapo $m = 1$) au nguvu fulani kuu ($p^m$ ambapo $m > 1$), basi unaweza kupata waendeshaji wawili $\circ$ na $\diamond$ kiasi kwamba masharti ya uga yatimizwe.

Ikiwa sehemu fulani ya kikomo ina nambari kuu ya Elements, basi inaitwa **uga kuu**. Ikiwa nambari ya Elements katika uwanja wa mwisho ni nguvu kuu, basi shamba linaitwa **uga wa upanuzi**. Katika kriptografia, tunavutiwa na sehemu kuu na ugani. [2]

Sehemu kuu kuu za kupendeza katika kriptografia ni zile ambapo seti ya nambari zote hubadilishwa kwa nambari kuu, na waendeshaji ni kuongeza na kuzidisha kawaida. Darasa hili la sehemu zenye ukomo zitajumuisha $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z}\mod na kadhalika. Kwa sehemu yoyote kuu $\mathbb{Z} \mod p$, seti ya nambari kamili za sehemu hii ni kama ifuatavyo: $\{0, 1, \ldets, p – 2, p – 1\}$.

Katika cryptography, tunavutiwa pia na sehemu za upanuzi, haswa sehemu zozote zilizo na $2^m$ Elements ambapo $m > 1$. Sehemu kama hizo zenye ukomo, kwa mfano, hutumiwa katika Sifa ya Rijndael, ambayo ni msingi wa Kiwango cha Juu cha Usimbaji Fiche. Ingawa sehemu kuu ni angavu kiasi, sehemu hizi za kiendelezi za msingi 2 pengine si za mtu yeyote asiyefahamu aljebra ya kufikirika.

Kuanza, ni kweli kwamba seti yoyote ya nambari kamili iliyo na $2^m$ Elements inaweza kupewa waendeshaji wawili ambao wangefanya mchanganyiko wao kuwa sehemu (ilimradi $m$ ni nambari kamili chanya). Walakini, kwa sababu uwanja upo haimaanishi kuwa ni rahisi kugundua au ni rahisi sana kwa matumizi fulani.

Inavyobainika, sehemu za kiendelezi zinazotumika za $2^m$ katika usimbaji fiche ni zile zinazofafanuliwa juu ya seti fulani za semi za aina nyingi, badala ya seti fulani ya nambari kamili.

Kwa mfano, tuseme kwamba tulitaka sehemu ya kiendelezi yenye $2^3$ (yaani, 8) Elements katika seti. Ingawa kunaweza kuwa na seti nyingi tofauti zinazoweza kutumika kwa sehemu za ukubwa huo, seti moja kama hiyo inajumuisha polynomia zote za kipekee za fomu $a_2x^2 + a_1x + a_0$, ambapo kila mgawo $a_i$ ni 0 au 1. Kwa hivyo, seti hii **S** inajumuisha Elements ifuatayo:

1. $0$: Kesi ambapo $a_2 = 0$, $a_1 = 0$, na $a_0 = 0$.

2. $1$: Kesi ambapo $a_2 = 0$, $a_1 = 0$, na $a_0 = 1$.

3. $x$: Kesi ambapo $a_2 = 0$, $a_1 = 1$, na $a_0 = 0$.

4. $x + 1$: Kesi ambapo $a_2 = 0$, $a_1 = 1$, na $a_0 = 1$.

5. $x^2$: Kesi ambapo $a_2 = 1$, $a_1 = 0$, na $a_0 = 0$.

6. $x^2 + 1$: Kesi ambapo $a_2 = 1$, $a_1 = 0$, na $a_0 = 1$.

7. $x^2 + x$: Kesi ambapo $a_2 = 1$, $a_1 = 1$, na $a_0 = 0$.

8. $x^2 + x + 1$: Kesi ambapo $a_2 = 1$, $a_1 = 1$, na $a_0 = 1$.

Kwa hivyo **S** itakuwa seti $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Ni shughuli gani mbili zinazoweza kufafanuliwa juu ya seti hii ya Elements ili kuhakikisha mchanganyiko wao ni uwanja?

Operesheni ya kwanza kwenye seti **S** ($\circ$) inaweza kufafanuliwa kama modulo ya kawaida ya polinomia ya kuongeza polinomia. Unachohitajika kufanya ni kuongeza polima kama kawaida, na kisha weka modulo ya 2 kwa kila mgawo wa polimanomia inayotokana. Hapa kuna baadhi ya mifano:


- $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
- $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
- $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

Operesheni ya pili kwenye seti **S** ($\diamond$) ambayo inahitajika kwa kuunda shamba ni ngumu zaidi. Ni aina ya kuzidisha, lakini sio kuzidisha kawaida kutoka kwa hesabu. Badala yake, lazima uone kila kipengele kama vekta na uelewe operesheni kama kuzidisha kwa vekta hizo mbili modulo polynomial isiyoweza kurekebishwa.

Hebu kwanza tugeuke kwenye wazo la polynomial isiyoweza kupunguzwa. **polynomia isiyoweza kupunguzwa** ni ile ambayo haiwezi kuhesabiwa (kama vile nambari kuu haiwezi kujumuishwa katika vijenzi vingine zaidi ya 1 na nambari kuu yenyewe). Kwa madhumuni yetu, tunavutiwa na polynomials ambazo haziwezi kupunguzwa kwa heshima na seti ya nambari zote. (Kumbuka kwamba unaweza kuangazia polima fulani kwa, kwa mfano, nambari halisi au changamano, hata kama huwezi kuzihesabu kwa kutumia nambari kamili.)

Kwa mfano, zingatia polynomial $x^2 - 3x + 2$. Hii inaweza kuandikwa upya kama $(x – 1)(x – 2)$. Kwa hivyo, hii haiwezi kupunguzwa. Sasa zingatia polynomial $x^2 + 1$. Kwa kutumia nambari kamili tu, hakuna njia ya kuongeza usemi huu. Kwa hivyo, hii ni polynomial isiyoweza kupunguzwa kwa heshima na nambari kamili.

Ifuatayo, hebu tugeuke kwenye dhana ya kuzidisha vector. Hatutachunguza mada hii kwa kina, lakini unahitaji tu kuelewa kanuni ya msingi: Mgawanyiko wowote wa vekta unaweza kufanyika mradi tu mgao una digrii ya juu kuliko au sawa na ile ya kigawanyaji. Ikiwa mgao una digrii ya chini kuliko kigawanyaji, basi gawio haliwezi kugawanywa tena na mgawanyiko.

Kwa mfano, zingatia usemi $x^6 + x + 1 \mod x^5 + x^2$. Hii inapunguza kwa uwazi zaidi kwani kiwango cha mgao, 6, ni cha juu kuliko kiwango cha kigawanyaji, 5. Sasa zingatia usemi $x^5 + x + 1 \mod x^5 + x^2$. Hii pia inapunguza zaidi, kwani kiwango cha gawio, 5, na kigawanyaji, 5, ni sawa.

Hata hivyo, sasa zingatia usemi $x^4 + x + 1 \mod x^5 + x^2$. Hii haipunguzi zaidi, kwani kiwango cha mgao, 4, ni cha chini kuliko kiwango cha kigawanyaji, 5.

Kwa msingi wa maelezo haya, sasa tuko tayari kupata operesheni yetu ya pili ya seti $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Tayari nimesema kwamba operesheni ya pili inapaswa kueleweka kama modulo ya kuzidisha vekta baadhi ya polynomial irreducible. Polynomia hii isiyoweza kupunguzwa inapaswa kuhakikisha kuwa operesheni ya pili inafafanua kikundi cha Abelian juu ya **S** na inaambatana na hali ya usambazaji. Kwa hivyo hiyo polynomial irreducible inapaswa kuwa nini?

Kwa vile vekta zote katika seti ni za digrii 2 au chini, polimanomia isiyoweza kurekebishwa inapaswa kuwa ya shahada ya 3. Ikiwa kuzidisha yoyote kwa vekta mbili katika seti kutatoa polimanomia ya digrii 3 au zaidi, tunajua kwamba modulo ya upolinomia ya shahada ya 3 daima hutoa polynomial ya digrii 2 au chini zaidi. Hii ndivyo hali ilivyo kwa sababu polimanomia yoyote ya shahada ya 3 au zaidi daima inaweza kugawanywa na aina nyingi za shahada ya 3. Kwa kuongezea, ile polynomia inayofanya kazi kama kigawanyiko lazima isiweze kupunguzwa.

Inabadilika kuwa kuna polynomia nyingi zisizoweza kurekebishwa za digrii 3 ambazo tunaweza kutumia kama kigawanyiko chetu. Kila moja ya polima hizi hufafanua sehemu tofauti kwa kushirikiana na seti yetu **S** na modulo ya nyongeza ya 2. Hii inamaanisha kuwa una chaguo nyingi unapotumia sehemu za kiendelezi $2^m$ katika kriptografia.

Kwa mfano wetu, tuseme kwamba tutachagua polynomial $x^3 + x + 1$. Kwa kweli hii haiwezi kupunguzwa, kwa sababu huwezi kuihesabu kwa kutumia nambari kamili. Kwa kuongeza, itahakikisha kwamba kuzidisha yoyote ya Elements mbili kutatoa polynomial ya digrii 2 au chini.

Wacha tuchunguze mfano wa operesheni ya pili kwa kutumia polynomial $x^3 + x + 1$ kama kigawanyo ili kuonyesha jinsi inavyofanya kazi. Tuseme kwamba unazidisha Elements $x^2 + 1$ na $x^2 + x$ katika seti yetu **S**. Basi, tunahitaji kuhesabu usemi $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Hii inaweza kurahisishwa kama ifuatavyo:


- $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
- $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
- $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Tunajua kwamba $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ inaweza kupunguzwa kwani mgao wa faida una digrii ya juu (4) kuliko kigawanyaji (3).

Kuanza, unaweza kuona kwamba usemi $x^3 + x + 1$ huenda katika $x^4 + x^3 + x^2 + x$ jumla ya mara $x$. Unaweza kuthibitisha hili kwa kuzidisha $x^3 + x + 1$ na $x$, ambayo ni $x^4 + x^2 + x$. Kama neno la mwisho ni la kiwango sawa na mgao, yaani 4, tunajua hii inafanya kazi. Unaweza kuhesabu sehemu iliyosalia ya mgawanyiko huu kwa $x$ kama ifuatavyo:


- $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
- $[x^3] \mod x^3 + x + 1 =$
- $x^3$

Kwa hivyo baada ya kugawanya $x^4 + x^3 + x^2 + x$ kwa $x^3 + x + 1$ jumla ya mara $x$, tuna salio la $x^3$. Je, hii inaweza kugawanywa zaidi kwa $x^3 + x + 1$?

Intuitively, inaweza kuvutia kusema kwamba $x^3$ haiwezi tena kugawanywa kwa $x^3 + x + 1$, kwa sababu neno la mwisho linaonekana kuwa kubwa. Walakini, kumbuka mjadala wetu juu ya mgawanyiko wa vekta hapo awali. Ilimradi mgao una digrii kubwa zaidi au sawa na kigawanyaji, usemi unaweza kupunguzwa zaidi. Hasa, usemi $x^3 + x + 1$ unaweza kuingia katika $x^3$ mara 1 haswa. Salio imehesabiwa kama ifuatavyo:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Huenda unashangaa kwa nini $(x^3) - (x^3 + x + 1)$ inatathmini hadi $x + 1$ na si $-x - 1$. Kumbuka kwamba operesheni ya kwanza ya uwanja wetu imefafanuliwa modulo 2. Kwa hivyo, uondoaji wa vekta mbili hutoa matokeo sawa kabisa na nyongeza ya vekta mbili.

Ili kujumlisha kuzidisha kwa $x^2 + 1$ na $x^2 + x$: Unapozidisha maneno hayo mawili, unapata digrii 4 polynomial, $x^4 + x^3 + x^2 + x$, ambayo inahitaji kupunguzwa modulo $x^3 + x + 1$. Digrii ya 4 ya polynomial inaweza kugawanywa kwa $x^3 + x + 1$ haswa $x + 1$ mara. Salio baada ya kugawanya $x^4 + x^3 + x^2 + x$ na $x^3 + x + 1$ haswa $x + 1$ mara ni $x + 1$. Hakika hiki ni kipengele katika seti yetu $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Kwa nini sehemu za upanuzi zilizo na msingi 2 juu ya seti za polynomia, kama ilivyo kwenye mfano hapo juu, zinaweza kuwa muhimu kwa usimbaji fiche? Sababu ni kwamba unaweza kuona coefficients katika polynomia za seti kama hizo, ama 0 au 1, kama Elements ya nyuzi za binary zenye urefu fulani. Seti **S** katika mfano wetu hapo juu, kwa mfano, inaweza kutazamwa badala yake kama seti **S** inayojumuisha mifuatano yote ya urefu wa 3 (000 hadi 111). Operesheni kwenye **S**, basi, inaweza pia kutumika kutekeleza shughuli kwenye mifuatano ya binary na kutoa mfuatano wa binary wenye urefu sawa.

**Maelezo:**

[2] Sehemu za upanuzi zinakuwa kinyume sana. Badala ya kuwa na Elements ya nambari kamili, wana seti za polynomials. Kwa kuongeza, shughuli zozote zinafanywa modulo baadhi ya polynomial irreducible.

## Kikemikali algebra katika mazoezi

<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Licha ya lugha rasmi na mukhtasari wa majadiliano, dhana ya kikundi haipaswi kuwa ngumu kueleweka. Ni seti tu ya Elements pamoja na operesheni ya binary, ambapo utendaji wa operesheni hiyo ya binary kwenye Elements hizo hukutana na masharti manne ya jumla. Kikundi cha Abelian kina hali ya ziada tu inayojulikana kama mawasiliano. Kikundi cha mzunguko, kwa upande wake, ni aina maalum ya kikundi cha Abelian, ambacho kina jenereta. Sehemu ni muundo changamano zaidi kutoka kwa dhana ya msingi ya kikundi.

Lakini ikiwa wewe ni mtu mwenye mwelekeo kivitendo, unaweza kujiuliza katika hatua hii: Ni nani anayejali? Je, kujua baadhi ya seti ya Elements na opereta ni kikundi, au hata Kiabeli au kikundi cha mzunguko, kuna umuhimu wowote wa ulimwengu? Je, kujua kitu ni shamba?

Bila kujitosa kwa undani zaidi, jibu ni "ndiyo". Vikundi viliundwa kwa mara ya kwanza katika karne ya 19 na mwanahisabati wa Kifaransa Evariste Galois. Alizitumia kufikia hitimisho kuhusu kusuluhisha milinganyo ya polinomia ya shahada ya juu kuliko tano.

Tangu wakati huo dhana ya kikundi imesaidia kutoa mwanga juu ya matatizo kadhaa katika hisabati na kwingineko. Kwa msingi wao, kwa mfano, mwanafizikia Murray-Gellman aliweza kutabiri kuwepo kwa chembe kabla ya kuzingatiwa katika majaribio. [3] Kwa mfano mwingine, wanakemia hutumia nadharia ya kikundi kuainisha maumbo ya molekuli. Wanahisabati hata wametumia dhana ya kikundi kufanya hitimisho kuhusu kitu halisi kama karatasi ya ukutani!

Kuonyesha kimsingi kuwa seti ya Elements iliyo na opereta fulani ni kikundi, inamaanisha kuwa kile unachokielezea kina ulinganifu fulani. Sio ulinganifu katika maana ya kawaida ya neno, lakini kwa fomu ya kufikirika zaidi. Na hii inaweza kutoa ufahamu mkubwa katika mifumo na matatizo fulani. Mawazo changamano zaidi kutoka kwa aljebra ya kufikirika hutupa tu maelezo ya ziada.

Muhimu zaidi, utaona umuhimu wa vikundi na sehemu za nadharia ya nambari katika mazoezi kupitia matumizi yao katika kriptografia, haswa ufunguo wa ufunguo wa umma. Tayari tumeona katika mjadala wetu wa nyanja, kwa mfano, jinsi nyanja za ugani zinavyotumika katika Rijndael Cipher. Tutafanyia mfano huo katika *Sura ya 5*.

Kwa majadiliano zaidi kuhusu aljebra ya kufikirika, ningependekeza mfululizo bora wa video kuhusu aljebra ya kufikirika na Socratica. [4] Ningependekeza hasa video zifuatazo: "Abstract algebra ni nini?", "Ufafanuzi wa kikundi (umepanuliwa)", "Ufafanuzi wa pete (umepanuliwa)", na "Ufafanuzi wa shamba (umepanuliwa)." Video hizi nne zitakupa ufahamu wa ziada katika mengi ya majadiliano hapo juu. (Hatukujadili pete, lakini uwanja ni aina maalum ya pete.)

Kwa majadiliano zaidi juu ya nadharia ya kisasa ya nambari, unaweza kushauriana na majadiliano mengi ya juu juu ya cryptography. Ningetoa kama mapendekezo Utangulizi wa Jonathan Katz na Yehuda Lindell kwa Uandishi wa Kisasa au Christof Paar na Uelewa wa Cryptography wa Jan Pelzl kwa majadiliano zaidi. [5]

**Maelezo:**

[3] Tazama [Video ya YouTube](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Abstract Algebra](https://www.socratica.com/subject/abstract-algebra)

[5] Katz na Lindell, *Utangulizi wa Siri za Kisasa*, 2nd edn, 2015 (CRC Press: Boca Raton, FL). Paar na Pelzl, *Kuelewa Cryptography*, 2010 (Springer-Verlag: Berlin).

# Ulinganifu wa Crystalgraphy

<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice na Bob

<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Mojawapo ya matawi makuu mawili ya kriptografia ni kriptografia linganifu. Inajumuisha mipango ya usimbaji fiche pamoja na mipango inayohusika na uthibitishaji na uadilifu. Hadi miaka ya 1970, usimbaji fiche wote ungekuwa na mifumo linganifu ya usimbaji fiche.

Mjadala mkuu unaanza kwa kuangalia mifumo ya usimbaji fiche linganifu na kufanya tofauti muhimu kati ya siphra za mtiririko na herufi za kuzuia. Basi, tunageukia misimbo ya uthibitishaji wa ujumbe, ambayo ni mipango ya kuhakikisha uadilifu na uhalisi wa ujumbe. Hatimaye, tunachunguza jinsi mifumo linganifu ya usimbaji fiche na misimbo ya uthibitishaji wa ujumbe inaweza kuunganishwa ili kuhakikisha mawasiliano salama.

Sura hii inajadili mifumo mbalimbali ya kriptografia linganifu kutoka kwa mazoezi katika kupita. Sura inayofuata inatoa ufafanuzi wa kina wa usimbaji fiche kwa kutumia msimbo wa mtiririko na msimbo wa kuzuia kutoka kwa mazoezi, yaani RC4 na AES mtawalia.

Kabla ya kuanza mjadala wetu juu ya ulinganifu wa kriptografia, ninataka kutoa maoni kwa ufupi juu ya vielelezo vya Alice na Bob katika sura hii na inayofuata.

___

Katika kuonyesha kanuni za usimbaji fiche, mara nyingi watu hutegemea mifano inayohusisha Alice na Bob. Nitafanya hivyo pia.

Hasa kama wewe ni mgeni katika usimbaji fiche, ni muhimu kutambua kwamba mifano hii ya Alice na Bob inakusudiwa tu kutumika kama vielelezo vya kanuni za kriptografia na miundo katika mazingira yaliyorahisishwa. Kanuni na miundo, hata hivyo, inatumika kwa anuwai pana zaidi ya miktadha ya maisha halisi.

Yafuatayo ni mambo matano muhimu ya kukumbuka kuhusu mifano inayowahusisha Alice na Bob katika usimbaji fiche:

1. Zinaweza kutafsiriwa kwa urahisi kuwa mifano na aina nyingine za watendaji kama vile makampuni au mashirika ya serikali.

2. Zinaweza kupanuliwa kwa urahisi ili kujumuisha waigizaji watatu au zaidi.

3. Katika mifano, Bob na Alice kwa kawaida huwa washiriki hai katika kuunda kila ujumbe na katika utumiaji wa mifumo ya kriptografia kwenye ujumbe huo. Lakini kwa kweli, mawasiliano ya kielektroniki kwa kiasi kikubwa yanajiendesha. Unapotembelea tovuti kwa kutumia usalama wa usafiri wa Layer, kwa mfano, kriptografia yote kwa kawaida hushughulikiwa na kompyuta yako na seva ya wavuti.

4. Katika muktadha wa mawasiliano ya kielektroniki, "ujumbe" unaotumwa kwenye njia ya mawasiliano kwa kawaida ni pakiti za TCP/IP. Hizi zinaweza kuwa za barua pepe, ujumbe wa Facebook, mazungumzo ya simu, uhamisho wa faili, tovuti, upakiaji wa programu, na kadhalika. Sio ujumbe kwa maana ya jadi. Walakini, waandishi wa maandishi mara nyingi watarahisisha ukweli huu kwa kusema kwamba ujumbe ni, kwa mfano, barua pepe.

5. Mifano kwa kawaida hulenga mawasiliano ya kielektroniki, lakini pia inaweza kupanuliwa kwa njia za kitamaduni za mawasiliano kama vile barua.

## Mipango ya usimbaji linganifu

<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Tunaweza kufafanua kwa urahisi **mpango wa usimbaji linganifu** kama mpango wowote wa kriptografia wenye algoriti tatu:

1. **algorithm ya kutengeneza ufunguo**, ambayo hutoa ufunguo wa faragha.

2. ** algoriti ya usimbaji fiche**, ambayo huchukua ufunguo wa faragha na maandishi wazi kama ingizo na kutoa maandishi ya siri.

3. **algorithm ya kusimbua**, ambayo huchukua ufunguo wa faragha na maandishi ya siri kama pembejeo na kutoa maandishi asilia.

Kwa kawaida mpango wa usimbaji fiche—iwe ulinganifu au ulinganifu—hutoa kiolezo cha usimbaji fiche kulingana na kanuni msingi, badala ya vipimo kamili.

Kwa mfano, fikiria Salsa20, mpango wa usimbaji fiche linganifu. Inaweza kutumika kwa urefu wa vitufe vya 128- na 256-bit. Chaguo kuhusu urefu wa ufunguo huathiri baadhi ya maelezo madogo ya algoriti (idadi ya miduara katika algoriti iwe kamili).

Lakini mtu hawezi kusema kwamba kutumia Salsa20 na ufunguo wa 128-bit ni mpango tofauti wa usimbuaji kuliko Salsa20 na ufunguo wa 256-bit. Algorithm ya msingi inakaa sawa. Ni wakati tu kanuni ya msingi inabadilika ndipo tunaweza kusema kuhusu mifumo miwili tofauti ya usimbaji fiche.

Miradi ya usimbaji fiche linganifu kwa kawaida ni muhimu katika aina mbili za matukio: (1) Zile ambazo mawakala wawili au zaidi wanawasiliana kutoka mbali na wanataka kuweka yaliyomo katika mawasiliano yao kuwa siri; na (2) zile ambazo wakala mmoja anataka kuweka yaliyomo kwenye ujumbe kuwa siri kwa muda wote.

Unaweza kuona taswira ya hali (1) katika *Mchoro 1* hapa chini. Bob anataka kutuma ujumbe $M$ kwa Alice kwa mbali, lakini hataki wengine waweze kuusoma ujumbe huo.

Bob kwanza anasimba ujumbe kwa njia fiche $M$ kwa ufunguo wa faragha $K$. Yeye, basi, hutuma maandishi ya siri $C$ kwa Alice. Alice akishapokea maandishi ya siri, anaweza kusimbua kwa kutumia kitufe cha $K$ na kusoma maandishi mafupi. Kwa mpango mzuri wa usimbaji fiche, mvamizi yeyote anayekatiza maandishi ya siri $C$ hapaswi kujifunza chochote cha umuhimu halisi kuhusu ujumbe $M$.

Unaweza kuona taswira ya hali (2) katika *Mchoro 2* hapa chini. Bob anataka kuwazuia wengine kutazama taarifa fulani. Hali ya kawaida inaweza kuwa kwamba Bob ni mfanyakazi anayehifadhi data nyeti kwenye kompyuta yake, ambayo si watu wa nje au wenzake wanapaswa kusoma.

Bob husimba ujumbe kwa njia fiche $M$ kwa wakati mmoja $T_0$ kwa ufunguo $K$ ili kutoa maandishi ya siri $C$. Kwa wakati $T_1$ anahitaji ujumbe tena, na anaondoa maandishi ya siri $C$ kwa ufunguo $K$. Mshambulizi yeyote ambaye huenda alipata maandishi ya siri $C$ wakati huo huo hakupaswa kupata chochote muhimu kuhusu $M$ kutoka kwayo.

*Kielelezo 1: Usiri katika nafasi*

![Figure 1: Secrecy across space](assets/Figure4-1.webp "Figure 1: Secrecy across space")

*Kielelezo 2: Usiri kwa wakati wote*

![Figure 2: Secrecy across time](assets/Figure4-2.webp "Figure 2: Secrecy across time")

## Mfano: Sifa ya kuhama

<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Katika Sura ya 2, tulikumbana na shift cipher, ambayo ni mfano wa mpango rahisi sana wa usimbaji fiche linganifu. Hebu iangalie tena hapa.

Tuseme kamusi *D* inayosawazisha herufi zote za alfabeti ya Kiingereza, kwa mpangilio, na seti ya nambari $\{0,1,2,\dots,25\}$. Chukulia seti ya jumbe zinazowezekana **M**. Shift cipher, basi, ni mpango wa usimbuaji unaofafanuliwa kama ifuatavyo:


- Chagua bila mpangilio ufunguo $k$ kati ya seti ya vitufe vinavyowezekana **K**, ambapo **K** = $\{0,1,2,\dots,25\}$
- Simba ujumbe kwa njia fiche $m \in$ **M**, kama ifuatavyo:
    - Tenganisha $m$ kwa herufi zake binafsi $m_0, m_1,\dots, m_i, \dots, m_l$
    - Badilisha kila $m_i$ kuwa nambari kulingana na *D*
    - Kwa kila $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Badilisha kila $c_i$ kuwa herufi kulingana na *D*
    - Kisha unganisha $c_0, c_1,\dots, c_l$ kutoa maandishi ya siri $c$
- Simbua maandishi ya siri $c$ kama ifuatavyo:
    - Badilisha kila $c_i$ kuwa nambari kulingana na *D*
    - Kwa kila $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Badilisha kila $m_i$ kuwa herufi kulingana na *D*
    - Kisha unganisha $m_0, m_1,\dots, m_l$ ili kutoa ujumbe asili $m$

Kinachofanya shift cipher kuwa mpango wa usimbaji fiche linganifu ni kwamba ufunguo sawa hutumiwa kwa usimbaji fiche na mchakato wa kusimbua. Kwa mfano, tuseme kwamba unataka kusimba ujumbe "MBWA" kwa njia fiche kwa kutumia shift cipher, na kwamba umechagua "24" kama ufunguo bila mpangilio. Kusimba ujumbe kwa ufunguo huu kunaweza kutoa "BME". Njia pekee ya kurejesha ujumbe asili ni kwa kutumia ufunguo sawa, "24", kwa mchakato wa usimbuaji.

Hii Shift cipher ni mfano wa **cipher monoalfabeti badala ya cipher**: mpango wa usimbaji fiche ambapo alfabeti ya maandishi ya sifumbo imerekebishwa (yaani, alfabeti moja pekee inatumiwa). Kwa kuchukulia kwamba algoriti ya usimbaji fiche ni ya kubainisha, kila kirai katika matini mbadala inaweza kuhusisha zaidi ishara moja katika maandishi wazi.

Hadi miaka ya 1700, utumizi mwingi wa usimbaji fiche uliegemea pakubwa sipheri mbadala za alfabeti, ingawa mara nyingi hizi zilikuwa ngumu zaidi kuliko Shift cipher. Unaweza, kwa mfano, kuchagua herufi kwa nasibu kutoka kwa alfabeti kwa kila herufi asilia chini ya kikwazo kwamba kila herufi hutokea mara moja tu katika alfabeti ya maandishi ya siri. Hiyo inamaanisha kuwa utakuwa na funguo 26 za kibinafsi zinazowezekana, ambazo zilikuwa kubwa katika enzi ya kompyuta ya awali.

Kumbuka kuwa utakutana na neno **cipher** sana katika usimbaji fiche. Fahamu kuwa neno hili lina maana mbalimbali. Kwa kweli, ninajua angalau maana tano tofauti za neno hilo ndani ya cryptography.

Katika baadhi ya matukio inarejelea mpango wa usimbaji fiche, kama inavyofanya katika Shift cipher na monoalfabeti badala ya cipher. Hata hivyo, neno hili pia linaweza kurejelea mahususi algoriti ya usimbaji, ufunguo wa faragha, au maandishi ya siri ya mpango wowote kama huo wa usimbaji.

Mwishowe, neno cipher pia linaweza kurejelea algoriti ya msingi ambayo unaweza kuunda mifumo ya kriptografia. Hizi zinaweza kujumuisha algoriti mbalimbali za usimbaji fiche, lakini pia aina nyingine za mifumo ya kriptografia. Maana hii ya neno inakuwa muhimu katika muktadha wa herufi za kuzuia (ona sehemu ya “Block Ciphers” hapa chini).

Unaweza pia kukutana na masharti ya **kunakili** au **kufafanua**. Maneno haya ni visawe tu vya usimbaji fiche na usimbuaji.

## Mashambulizi ya nguvu ya kikatili na kanuni ya Kerckhoff

<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Shift cipher ni mpango usio salama sana wa usimbaji linganifu, angalau katika ulimwengu wa kisasa. [1] Mshambulizi anaweza kujaribu kusimbua maandishi yoyote ya siri kwa kutumia vitufe vyote 26 vinavyowezekana ili kuona ni matokeo gani yanayoeleweka. Aina hii ya shambulio, ambapo mshambuliaji anaendesha baiskeli tu kupitia funguo ili kuona kinachofanya kazi, inajulikana kama **shambulio la nguvu** au **utafutaji wa ufunguo kamili**.

Ili mpango wowote wa usimbaji fiche kutimiza dhana ndogo ya usalama, ni lazima uwe na seti ya vitufe vinavyowezekana, au **nafasi ya vitufe**, ambayo ni kubwa sana hivi kwamba mashambulizi ya nguvu hayawezi kutekelezeka. Mipango yote ya kisasa ya usimbaji fiche inakidhi kiwango hiki. Inajulikana kama **kanuni ya kutosha ya nafasi muhimu**. Kanuni sawa hutumika katika aina tofauti za mifumo ya kriptografia.

Ili kuhisi ukubwa wa nafasi muhimu katika mifumo ya kisasa ya usimbaji fiche, tuseme kwamba faili imesimbwa kwa ufunguo wa 128-bit kwa kutumia kiwango cha juu cha usimbaji fiche. Hii inamaanisha kuwa mshambulizi ana seti ya funguo $2^{128}$ ambazo anahitaji kupitia kwa shambulio la kinyama. Nafasi ya 0.78% ya kufaulu kwa mkakati huu itahitaji mshambuliaji kuzunguka takriban $2.65 \mara 10^{36}$ funguo.

Tuseme tunadhania kwamba mshambulizi anaweza kujaribu vitufe vya $10^{16}$ kwa sekunde (yaani, funguo za quadrillion 10 kwa sekunde). Ili kujaribu 0.78% ya funguo zote katika nafasi muhimu, shambulio lake lingedumu $2.65 \mara 10^{20}$ sekunde. Hii ni takriban miaka trilioni 8.4. Kwa hivyo hata shambulio la nguvu la kikatili na adui mwenye nguvu isiyo na maana sio kweli na mpango wa kisasa wa usimbuaji wa 128-bit. Hii ndiyo kanuni ya kutosha ya nafasi muhimu inayotumika.

Je, msimbo wa kuhama ni salama zaidi ikiwa mshambuliaji hajui algoriti ya usimbaji fiche? Labda, lakini sio sana.

Kwa hali yoyote, kriptografia ya kisasa, daima inadhani kuwa usalama wa mpango wowote wa usimbaji fiche unategemea tu kuweka siri ya ufunguo wa kibinafsi. Mshambulizi daima huchukuliwa kuwa anajua maelezo mengine yote, ikiwa ni pamoja na nafasi ya ujumbe, nafasi muhimu, nafasi ya maandishi ya siri, algoriti ya uteuzi muhimu, algoriti ya usimbaji fiche, na algoriti ya usimbuaji.

Wazo kwamba usalama wa mpango wa usimbaji fiche linganifu unaweza tu kutegemea usiri wa ufunguo wa faragha unajulikana kama **Kanuni ya Kerckhoffs**.

Kama ilivyokusudiwa awali na Kerckhoffs, kanuni hiyo inatumika tu kwa mipango ya usimbaji linganifu. Toleo la jumla zaidi la kanuni hiyo, hata hivyo, linatumika pia kwa aina nyingine zote za kisasa za mifumo ya kriptografia: Muundo wowote wa mpango wa kriptografia haufai kuhitajika kuwa siri ili uwe salama; usiri unaweza kuenea tu kwa baadhi ya mifuatano ya habari, kwa kawaida ufunguo wa faragha.

Kanuni ya Kerckhoffs ni muhimu kwa cryptography ya kisasa kwa sababu nne. [2] Kwanza, kuna idadi ndogo tu ya mipango ya kriptografia kwa aina fulani za programu. Kwa mfano, programu nyingi za kisasa za usimbaji linganifu hutumia misimbo ya Rijndael. Kwa hivyo usiri wako kuhusu muundo wa mpango ni mdogo sana. Kuna, hata hivyo, kubadilika zaidi katika kutunza ufunguo fulani wa faragha kwa siri ya siri ya Rijndael.

Pili, ni rahisi kuchukua nafasi ya safu fulani ya habari kuliko mpango mzima wa kriptografia. Tuseme kwamba wafanyakazi wa kampuni wote wana programu sawa ya usimbaji fiche, na kwamba kila wafanyakazi wawili wana ufunguo wa faragha wa kuwasiliana kwa siri. Maelewano muhimu ni shida katika hali hii, lakini angalau kampuni inaweza kuweka programu na ukiukaji kama huo wa usalama. Ikiwa kampuni ilikuwa inategemea usiri wa mpango huo, basi uvunjaji wowote wa usiri huo ungehitaji kuchukua nafasi ya programu zote.

Tatu, kanuni ya Kerckhoffs inaruhusu kusawazisha na utangamano kati ya watumiaji wa mifumo ya kriptografia. Hii ina faida kubwa kwa ufanisi. Kwa mfano, ni vigumu kufikiria jinsi mamilioni ya watu wangeweza kuunganisha kwa usalama kwenye seva za wavuti za Google kila siku, ikiwa usalama huo ulihitaji kuweka mifumo ya siri kuwa siri.

Nne, kanuni ya Kerckhoff inaruhusu uchunguzi wa umma wa miradi ya kriptografia. Uchunguzi wa aina hii ni muhimu kabisa ili kufikia mipango salama ya kriptografia. Kwa kielelezo, kanuni kuu ya msingi katika kriptografia linganifu, misimbo ya Rijndael, ilikuwa ni matokeo ya shindano lililoandaliwa na Taasisi ya Kitaifa ya Viwango na Teknolojia kati ya 1997 na 2000.

Mfumo wowote unaojaribu kufikia **usalama kwa kutokujulikana** ni ule unaotegemea kuweka maelezo ya muundo na/au utekelezaji wake kuwa siri. Katika kriptografia, huu utakuwa mfumo mahususi ambao unategemea kuweka maelezo ya muundo wa mpango wa kriptografia kuwa siri. Kwa hivyo usalama kwa kutokujulikana ni kinyume kabisa na kanuni ya Kerckhoffs.

Uwezo wa uwazi ili kuimarisha ubora na usalama pia unaenea kwa upana zaidi hadi kwa ulimwengu wa kidijitali kuliko tu kriptografia. Usambazaji wa Linux wa chanzo huria na huria kama vile Debian, kwa mfano, kwa ujumla huwa na faida kadhaa juu ya wenzao wa Windows na MacOS katika suala la faragha, uthabiti, usalama, na kubadilika. Ingawa hiyo inaweza kuwa na sababu nyingi, kanuni muhimu zaidi pengine ni, kama Eric Raymond alivyosema katika insha yake maarufu "The Cathedral and the Bazaar," kwamba "kupewa mboni za macho za kutosha, mende wote hawana kina." [3] Ni hekima hii ya kanuni ya aina ya umati ndiyo iliyoipa Linux mafanikio yake muhimu zaidi.

Mtu hawezi kamwe kusema bila utata kwamba mpango wa siri ni "salama" au "usio salama." Badala yake, kuna dhana mbalimbali za usalama kwa mifumo ya kriptografia. Kila **ufafanuzi wa usalama wa kriptografia** lazima ubainishe (1) malengo ya usalama, pamoja na (2) uwezo wa mshambulizi. Kuchanganua mipango ya kriptografia dhidi ya dhana moja au zaidi mahususi ya usalama hutoa maarifa kuhusu matumizi na vikwazo vyake.

Ingawa hatutachunguza maelezo yote ya dhana mbalimbali za usalama wa kriptografia, unapaswa kujua kwamba mawazo mawili yanapatikana kila mahali kwa dhana zote za kisasa za usalama zinazohusu mifumo linganifu na isiyolinganishwa (na kwa namna fulani kwa maandishi mengine ya awali ya kriptografia):


- Maarifa ya mshambuliaji kuhusu mpango huo yanapatana na kanuni ya Kerckhoffs.
- Mshambulizi hawezi kufanya shambulio la kikatili kwenye mpango. Hasa, mifano ya vitisho ya fikra za usalama kwa kawaida haziruhusu mashambulizi ya kikatili, kwa vile huchukulia kuwa haya si jambo linalofaa kuzingatiwa.

**Maelezo:**

[1] Kulingana na Seutonius, sifa ya kuhama yenye thamani kuu ya 3 ilitumiwa na Julius Caesar katika mawasiliano yake ya kijeshi. Kwa hivyo A ingekuwa D, B kila wakati E, C daima F, na kadhalika. Toleo hili mahususi la msimbo wa kuhama, kwa hivyo, limejulikana kama **Caesar Cipher** (ingawa si kirai kwa maana ya kisasa ya neno, kwani thamani kuu ni thabiti). Sifa ya Kaisari inaweza kuwa salama katika karne ya kwanza KK, ikiwa maadui wa Roma hawakujua sana usimbaji fiche. Lakini ni wazi haingekuwa mpango salama sana katika nyakati za kisasa.

[2] Jonathan Katz na Yehuda Lindell, _Utangulizi wa Siri ya Kisasa_, CRC Press (Boca Raton, FL: 2015), p. 7f.

[3] Eric Raymond, "The Cathedral and the Bazaar," karatasi iliwasilishwa katika Linux Kongress, Würzburg, Ujerumani (Mei 27, 1997). Kuna idadi ya matoleo yanayofuata yanayopatikana pamoja na kitabu. Manukuu yangu yametoka ukurasa wa 30 katika kitabu: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux na Open Source by an Accident Revolution_, iliyorekebishwa edn. (2001), O'Reilly: Sebastopol, CA.

## Tiririsha misimbo

<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Miradi ya usimbaji fiche linganifu imegawanywa kwa kawaida katika aina mbili: **ciphers mkondo** na **block ciphers**. Tofauti hii kwa kiasi fulani inasumbua, hata hivyo, kwani watu hutumia maneno haya kwa njia isiyolingana. Katika sehemu chache zijazo, nitaweka tofauti katika njia ninayofikiria ni bora zaidi. Unapaswa kufahamu, hata hivyo, kwamba watu wengi watatumia maneno haya kwa kiasi fulani tofauti na nilivyoweka.

Hebu tugeukie kwanza kwa mtiririko wa ciphers. **cipher ya mtiririko** ni mpango wa usimbaji fiche linganifu ambapo usimbaji fiche una hatua mbili.

Kwanza, mfuatano wa urefu wa maandishi wazi hutolewa kupitia ufunguo wa kibinafsi. Kamba hii inaitwa ** keystream **.

Ifuatayo, mkondo wa ufunguo huunganishwa kihisabati na maandishi wazi ili kutoa maandishi ya siri. Mchanganyiko huu kawaida ni operesheni ya XOR. Kwa usimbuaji, unaweza tu kubadili operesheni. (Kumbuka kwamba $A \oplus B = B \plus A$, katika kesi $A$ na $B$ ni mifuatano midogo. Kwa hivyo mpangilio wa utendakazi wa XOR katika msimbo wa mtiririko haujalishi kwa matokeo. Sifa hii inajulikana kama **commutativity**.)

Sifa ya kawaida ya mtiririko wa XOR inaonyeshwa kwenye *Mchoro 3*. Kwanza unachukua ufunguo wa faragha $K$ na kuutumia kwa generate mkondo wa ufunguo. Mtiririko wa ufunguo, basi, umejumuishwa na maandishi wazi kupitia operesheni ya XOR kutoa maandishi ya siri. Wakala yeyote anayepokea maandishi ya siri anaweza kusimbua kwa urahisi ikiwa ana ufunguo $K$. Anachohitaji kufanya ni kuunda mkondo wa ufunguo mradi tu maandishi ya siri kulingana na utaratibu uliobainishwa wa mpango na XOR kwa maandishi ya siri.

*Kielelezo cha 3: Sifa ya mkondo wa XOR*

![Figure 3: An XOR stream cipher](assets/Figure4-3.webp "Figure 3: An XOR stream cipher")

Kumbuka kuwa mpango wa usimbaji fiche kwa kawaida huwa ni kiolezo cha usimbaji fiche chenye kanuni sawa ya msingi, badala ya maelezo mahususi. Kwa kiendelezi, cipher ya mtiririko kwa kawaida ni kiolezo cha usimbaji fiche ambacho unaweza kutumia vitufe vya urefu tofauti. Ingawa urefu wa ufunguo unaweza kuathiri baadhi ya maelezo madogo ya mpango, hautaathiri muundo wake muhimu.

Shift cipher ni mfano wa cipher mkondo rahisi sana na isiyo salama. Kwa kutumia herufi moja (ufunguo wa kibinafsi), unaweza kutoa mfuatano wa herufi urefu wa ujumbe (mkondo muhimu). Mtiririko huu muhimu, basi, umeunganishwa na maandishi wazi kupitia operesheni ya modulo ili kutoa maandishi ya siri. (Operesheni hii ya modulo inaweza kurahisishwa kwa operesheni ya XOR wakati wa kuwakilisha herufi katika biti).

Mfano mwingine maarufu wa msimbo wa mtiririko ni **Vigenere cipher**, baada ya Blaise de Vigenere ambaye aliikuza kikamilifu mwishoni mwa karne ya 16 (ingawa wengine walikuwa wamefanya kazi nyingi iliyotangulia). Ni mfano wa **polyalfabeti badala ya cipher**: mpango wa usimbaji fiche ambapo alfabeti ya maandishi ya kisifa ya ishara ya maandishi hubadilika kulingana na nafasi yake katika maandishi. Kinyume na kisifa mbadala cha alfabeti, alama za maandishi-siri zinaweza kuhusishwa na zaidi ya alama moja ya maandishi wazi.

Kadiri usimbaji fiche ulivyozidi kupata umaarufu katika Renaissance Ulaya, ndivyo pia **uchambuzi wa siri**—yaani, uvunjaji wa maandishi ya siri—hasa, kwa kutumia **uchambuzi wa masafa**. Mwisho huo unatumia kanuni za kitakwimu katika lugha yetu ili kuvunja maandishi ya maandishi, na iligunduliwa na wasomi wa Kiarabu tayari katika karne ya tisa. Ni mbinu inayofanya kazi vizuri hasa na maandishi marefu. Na hata sifa za kisasa zaidi za uwekaji herufi moja hazikutosha tena dhidi ya uchanganuzi wa marudio kufikia miaka ya 1700 huko Uropa, haswa katika mipangilio ya kijeshi na usalama. Vigenere cipher ilipotoa maendeleo makubwa katika usalama, ikawa maarufu katika kipindi hiki na ilienea mwishoni mwa miaka ya 1700.

Kuzungumza kwa njia isiyo rasmi, mpango wa usimbuaji hufanya kazi kama ifuatavyo:

1. Chagua neno lenye herufi nyingi kama ufunguo wa faragha.

2. Kwa ujumbe wowote, tumia shift cipher kwa kila herufi ya ujumbe ukitumia herufi inayolingana katika neno kuu kama shift.

3. Iwapo umepitia neno muhimu lakini bado hujaweka msimbo wa maandishi wazi, tena tumia herufi za neno kuu kama msimbo wa kubadilisha herufi zinazolingana katika salio la maandishi.

4. Endelea na mchakato huu hadi ujumbe wote uwe umesimbwa.

Ili kutoa mfano, tuseme ufunguo wako wa faragha ni "DHAHABU" na unataka kusimba ujumbe "CRYPTOGRAPHY". Katika hali hiyo, ungeendelea kama ifuatavyo kulingana na cipher ya Vigenère:


- $c_0 = [(2 + 6) \mod 26] = 8 = I$
- $c_1 = [(17 + 14) \mod 26] = 5 = F$
- $c_2 = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Kwa hivyo, maandishi ya maandishi $c$ = "IFJSZCRUGDSB".

Mfano mwingine maarufu wa msimbo wa mtiririko ni **pedi ya wakati mmoja**. Ukiwa na pedi ya wakati mmoja, unaunda tu mfuatano wa biti nasibu mradi tu ujumbe wa maandishi wazi na utoe maandishi ya siri kupitia utendakazi wa XOR. Kwa hivyo, ufunguo wa faragha na mkondo wa ufunguo ni sawa na pedi ya wakati mmoja.

Wakati sipheri za Shift na Vigenere cipher hazina usalama sana katika enzi ya kisasa, pedi ya wakati mmoja ni salama sana ikiwa inatumiwa kwa usahihi. Pengine matumizi maarufu zaidi ya pedi ya wakati mmoja ilikuwa, angalau hadi miaka ya 1980, kwa simu ya simu ya **Washington-Moscow **. [4]

Simu hiyo ya dharura ni kiunga cha mawasiliano ya moja kwa moja kati ya Washington na Moscow kwa masuala ya dharura ambayo yaliwekwa baada ya Mgogoro wa Kombora la Cuba. Teknolojia kwa miaka mingi imebadilika. Hivi sasa, inajumuisha kebo ya optic ya moja kwa moja ya nyuzi pamoja na viungo viwili vya satelaiti (kwa upunguzaji), ambayo huwezesha barua pepe na ujumbe wa maandishi. Kiungo kinaishia katika maeneo mbalimbali nchini Marekani. Pentagon, White House, na Raven Rock Mountain zinajulikana mwisho. Kinyume na maoni ya watu wengi, simu hiyo haijawahi kuhusisha simu.

Kwa asili, mpango wa pedi wa wakati mmoja ulifanya kazi kama ifuatavyo. Washington na Moscow zingekuwa na seti mbili za nambari za nasibu. Seti moja ya nambari za nasibu, iliyoundwa na Warusi, ilihusu usimbaji fiche na usimbuaji wa ujumbe wowote katika lugha ya Kirusi. Seti moja ya nambari nasibu, iliyoundwa na Wamarekani, ilihusu usimbaji fiche na usimbuaji wa ujumbe wowote katika lugha ya Kiingereza. Mara kwa mara, nambari nyingi zaidi za nasibu zingewasilishwa kwa upande mwingine na wasafirishaji wanaoaminika.

Washington na Moscow, basi, ziliweza kuwasiliana kwa siri kwa kutumia nambari hizi za nasibu kwa kuunda pedi za wakati mmoja. Kila wakati ulipohitaji kuwasiliana, ungetumia sehemu inayofuata ya nambari nasibu kwa ujumbe wako.

Ingawa ni salama sana, pedi ya mara moja inakabiliwa na vikwazo muhimu vya kiutendaji: ufunguo unahitaji kuwa mrefu kama ujumbe na hakuna sehemu ya pedi ya wakati mmoja inayoweza kutumika tena. Hii ina maana kwamba unahitaji kufuatilia ulipo kwenye pedi ya wakati mmoja, kuhifadhi idadi kubwa ya biti, na bits za Exchange nasibu na wenzako mara kwa mara. Kwa hivyo, pedi ya wakati mmoja haitumiwi mara kwa mara katika mazoezi.

Badala yake, misimbo kuu ya mtiririko inayotumiwa katika mazoezi ni **cipheri za mtiririko bandia**. Salsa20 na lahaja inayohusiana kwa karibu inayoitwa ChaCha ni mifano ya misimbo ya mkondo ya uwongo inayotumika sana.

Ukiwa na misimbo hii ya mtiririko wa uwongo, kwanza unachagua bila mpangilio ufunguo wa K ambao ni mfupi kuliko urefu wa maandishi wazi. Kitufe cha nasibu kama hiki K kawaida huundwa na kompyuta yetu kwa msingi wa data isiyotabirika ambayo inakusanya kwa wakati, kama vile wakati kati ya ujumbe wa mtandao, harakati za panya, na kadhalika.

Ufunguo huu wa nasibu $K$ kisha unaingizwa kwenye kanuni ya upanuzi ambayo huunda mtiririko wa ufunguo wa uwongo kwa muda mrefu kama ujumbe. Unaweza kubainisha kwa usahihi muda ambao mtiririko wa vitufe unahitaji kuwa (k.m., biti 500, biti 1000, biti 1200, biti 29,117, na kadhalika).

Mkondo wa msimbo wa pseudorandom unaonekana *kana kwamba* ulichaguliwa nasibu kabisa kutoka kwa seti ya mifuatano yote yenye urefu sawa. Kwa hivyo, usimbaji fiche kwa mkondo wa ufunguo wa pseudorandom huonekana kana kwamba umefanywa na pedi ya mara moja. Lakini hiyo ni, bila shaka, sivyo.

Kwa vile ufunguo wetu wa faragha ni mfupi kuliko mkondo muhimu na kanuni zetu za upanuzi zinahitaji kubainishwa ili mchakato wa usimbaji/usimbuaji ufanye kazi, si kila mkondo muhimu wa urefu huo ungeweza kusababisha matokeo kutoka kwa operesheni yetu ya upanuzi.

Tuseme, kwa mfano, kwamba ufunguo wetu wa faragha una urefu wa biti 128 na kwamba tunaweza kuuingiza kwenye algoriti ya upanuzi ili kuunda mkondo wa ufunguo mrefu zaidi, tuseme biti 2,500. Kwa vile algoriti yetu ya upanuzi inahitaji kubainishwa, algoriti yetu inaweza angalau kuchagua $1/2^{128}$ masharti yenye urefu wa biti 2,500. Kwa hivyo mtiririko wa ufunguo kama huo haungeweza kuchaguliwa kwa nasibu kabisa kutoka kwa kamba zote za urefu sawa.

Ufafanuzi wetu wa msimbo wa mtiririko una vipengele viwili: (1) mkondo muhimu mradi tu maandishi wazi yanatolewa kwa usaidizi wa ufunguo wa faragha; na (2) mkondo huu muhimu umeunganishwa na maandishi wazi, kwa kawaida kupitia utendakazi wa XOR, ili kutoa maandishi ya siri.

Wakati mwingine watu hufafanua sharti (1) kwa ukali zaidi, kwa kudai kwamba mkondo wa ufunguo lazima hasa uwe uwongo. Hii ina maana kwamba si siphero ya shift, wala pedi ya wakati mmoja haitachukuliwa kuwa misimbo ya mtiririko.

Kwa maoni yangu, kufafanua hali (1) kwa upana zaidi hutoa njia rahisi ya kupanga mipango ya usimbuaji. Zaidi ya hayo, ina maana kwamba si lazima tuache kuita mpango mahususi wa usimbaji fiche msimbo wa mtiririko kwa sababu tu tunafahamu kuwa hautegemei mitiririko muhimu ya pseudorandom.

**Maelezo:**

[4] Crypto Museum, "Washington-Moscow hotline," 2013, inapatikana katika [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Zuia misimbo

<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Njia ya kwanza ambayo **block cipher** inaeleweka kwa kawaida ni kama kitu cha awali zaidi kuliko cipher mtiririko: Kanuni ya msingi ambayo hufanya mabadiliko ya kuhifadhi urefu kwenye mfuatano wa urefu unaofaa kwa usaidizi wa ufunguo. Algorithm hii inaweza kutumika kuunda mifumo ya usimbaji fiche na labda aina zingine za mifumo ya kriptografia.

Mara kwa mara, block cipher inaweza kuchukua mifuatano ya ingizo ya urefu tofauti kama vile biti 64, 128, au 256, pamoja na vitufe vya urefu tofauti kama vile biti 128, 192 au 256. Ingawa baadhi ya maelezo ya algorithm yanaweza kubadilika kulingana na vigezo hivi, kanuni ya msingi haibadiliki. Ikiwa ilifanya hivyo, tungezungumza juu ya herufi mbili tofauti za block. Kumbuka kuwa matumizi ya istilahi ya msingi ya algorithm hapa ni sawa na ya mifumo ya usimbaji fiche.

Taswira ya jinsi block cipher inavyofanya kazi inaweza kuonekana kwenye *Mchoro 4* hapa chini. Ujumbe $M$ wa urefu wa $L$ na ufunguo $K$ hutumika kama maingizo kwenye Cipher ya Block. Inatoa ujumbe $M'$ wa urefu $L$. Ufunguo hauhitaji kuwa na urefu sawa na $M$ na $M'$ kwa misimbo mingi ya kuzuia.

*Kielelezo 4: Sifa ya block*

![Figure 4: A block cipher](assets/Figure4-4.webp "Figure 4: A block cipher")

Cipher block peke yake sio mpango wa usimbaji fiche. Lakini block cipher inaweza kutumika pamoja na **njia mbalimbali za utendakazi** ili kutoa mifumo tofauti ya usimbaji fiche. Njia ya utendakazi huongeza tu shughuli zingine za ziada nje ya msimbo wa kuzuia.

Ili kuonyesha jinsi hii inavyofanya kazi, tuseme block cipher (BC) ambayo inahitaji mfuatano wa 128-bit na ufunguo wa faragha wa 128-bit. Kielelezo cha 5 hapa chini kinaonyesha jinsi msimbo huo wa kuzuia unaweza kutumika na **modi ya kitabu cha msimbo wa kielektroniki** (**Modi ya ECB**) ili kuunda mpango wa usimbaji fiche. (Duaradufu upande wa kulia zinaonyesha kuwa unaweza kurudia muundo huu mradi tu inahitajika).

*Mchoro wa 5: Sifa ya kuzuia yenye modi ya ECB*

![Figure 5: A block cipher with ECB mode](assets/Figure4-5.webp "Figure 5: A block cipher with ECB mode")

Mchakato wa usimbaji fiche wa kitabu cha msimbo wa kielektroniki na kisifa cha kuzuia ni kama ifuatavyo. Angalia ikiwa unaweza kugawanya ujumbe wako wa maandishi katika vizuizi 128-bit. Ikiwa sivyo, ongeza ** pedi ** kwa ujumbe, ili matokeo yanaweza kugawanywa sawasawa na saizi ya block ya bits 128. Hii ni data yako iliyotumiwa kwa mchakato wa usimbaji fiche.

Sasa gawanya data katika vipande vya mifuatano ya biti-128 ($M_1$, $M_2$, $M_3$, na kadhalika). Endesha kila mfuatano wa biti 128 kupitia msimbo wa kuzuia ukitumia ufunguo wako wa biti-128 ili kutoa vipande 128 vya maandishi ya siri ($C_1$, $C_2$, $C_3$, na kadhalika). Visehemu hivi, vinapounganishwa tena, huunda maandishi kamili ya siri.

Usimbaji fiche ni mchakato wa kurudi nyuma, ingawa mpokeaji anahitaji njia fulani inayotambulika ya kuondoa pedi yoyote kutoka kwa data iliyosimbwa ili kutoa ujumbe wa maandishi asilia.

Ingawa ni moja kwa moja, block cipher yenye modi ya kitabu cha kielektroniki haina usalama. Hii ni kwa sababu husababisha **usimbaji fiche wa kuamua**. Mifuatano yoyote miwili ya data inayofanana ya biti-128 imesimbwa kwa njia ile ile. Habari hiyo inaweza kutumika.

Badala yake, mpango wowote wa usimbaji fiche ulioundwa kutoka kwa block cipher unapaswa kuwa **uwezekano**: yaani, usimbaji fiche wa ujumbe wowote $M$, au sehemu yoyote maalum ya $M$, kwa ujumla inapaswa kutoa matokeo tofauti kila wakati. [5]

**Modi ya mnyororo wa kuzuia sifumbo** (**Modi ya CBC**) huenda ndiyo hali inayotumiwa zaidi na msimbo wa kuzuia. Mchanganyiko, ikiwa unafanywa vizuri, hutoa mpango wa usimbaji fiche unaowezekana. Unaweza kuona taswira ya hali hii ya uendeshaji katika *Mchoro 6* hapa chini.

*Kielelezo 6: Sifa ya kuzuia yenye modi ya CBC*

![Figure 6: A block cipher with CBC mode](assets/Figure4-6.webp "Figure 6: A block cipher with CBC mode")

Tuseme saizi ya block ni bits 128 tena. Kwa hivyo ili kuanza, utahitaji tena kuhakikisha kuwa ujumbe wako asilia wa maandishi unapokea pedi zinazohitajika.

Kisha, wewe XOR sehemu ya kwanza ya 128-bit ya maandishi yako wazi na **vekta ya uanzishaji** ya biti-128. Matokeo huwekwa kwenye block cipher ili kutoa maandishi ya siri kwa block ya kwanza. Kwa block ya pili ya biti 128, wewe kwanza XOR maandishi wazi na ciphertext kutoka block ya kwanza, kabla ya kuiingiza kwenye block cipher. Unaendelea na mchakato huu hadi uwe umesimba ujumbe wako wote wa maandishi wazi.

Ukimaliza, unatuma ujumbe uliosimbwa kwa njia fiche pamoja na vekta ya uanzishaji ambayo haijasimbwa kwa mpokeaji. Mpokeaji anahitaji kujua vekta ya uanzishaji, vinginevyo hawezi kusimbua maandishi ya siri.

Ujenzi huu ni salama zaidi kuliko modi ya kitabu cha msimbo wa kielektroniki unapotumiwa kwa usahihi. Unapaswa, kwanza, kuhakikisha kuwa vekta ya uanzishaji ni mfuatano wa nasibu au uwongo. Kwa kuongeza, unapaswa kutumia vekta tofauti ya uanzishaji kila wakati unapotumia mpango huu wa usimbaji fiche.

Kwa maneno mengine, vekta yako ya uanzishaji inapaswa kuwa Nonce nasibu au pseudorandom, ambapo **Nonce** inasimamia "nambari inayotumika mara moja tu." Ukidumisha mazoezi haya, basi modi ya CBC yenye msimbo wa kuzuia huhakikisha kuwa vizuizi vyovyote viwili vinavyofanana kwa ujumla vitasimbwa kwa njia fiche tofauti kila wakati.

Hatimaye, hebu tuelekeze usikivu wetu kwa **modi ya maoni ya pato** (**Modi ya OFB**). Unaweza kuona taswira ya hali hii katika *Mchoro 7*.

*Kielelezo cha 7: Sifa ya kuzuia yenye modi ya OFB*

![Figure 7: A block cipher with OFB mode](assets/Figure4-7.webp "Figure 7: A block cipher with OFB mode")

Ukiwa na modi ya OFB pia unachagua vekta ya uanzishaji. Lakini hapa, kwa kizuizi cha kwanza, vekta ya uanzishaji imeingizwa moja kwa moja kwenye kisifa cha kuzuia na ufunguo wako. Biti-128 zinazotokana, basi, zinachukuliwa kama mkondo muhimu. Mtiririko huu wa ufunguo umewekwa XOR kwa maandishi wazi ili kutoa maandishi ya siri ya kizuizi. Kwa vizuizi vifuatavyo, unatumia mkondo muhimu kutoka kwa kizuizi kilichotangulia kama ingizo kwenye msimbo wa kuzuia na kurudia hatua.

Ukiangalia kwa makini, kilichoundwa hapa kutoka kwa msimbo wa kuzuia kwa modi ya OFB ni msimbo wa mtiririko. Wewe generate sehemu muhimu za mtiririko wa biti 128 hadi upate urefu wa maandishi wazi (kutupa biti ambazo huhitaji kutoka sehemu ya mwisho ya mkondo-msingi ya 128-bit). Wewe, basi, XOR mkondo muhimu na ujumbe wako wa maandishi wazi ili kupata maandishi ya siri.

Katika sehemu iliyotangulia juu ya misimbo ya mtiririko, nilisema kwamba unazalisha mkondo wa ufunguo kwa usaidizi wa ufunguo wa kibinafsi. Ili kuwa sawa, sio lazima tu kuunda na ufunguo wa kibinafsi. Kama unavyoona katika hali ya OFB, mtiririko wa vitufe unatolewa kwa usaidizi wa ufunguo wa faragha na vekta ya uanzishaji.

Kumbuka kuwa kama ilivyo kwa modi ya CBC, ni muhimu kuchagua pseudorandom au Nonce nasibu kwa vekta ya uanzishaji kila wakati unapotumia block cipher katika modi ya OFB. Vinginevyo, mfuatano wa ujumbe wa biti 128 uliotumwa katika mawasiliano tofauti utasimbwa kwa njia ile ile. Hii ni njia mojawapo ya kuunda usimbaji fiche unaowezekana kwa kutumia msimbo wa mtiririko.

Baadhi ya misimbo ya mtiririko hutumia tu ufunguo wa faragha kuunda mtiririko muhimu. Kwa hizo misimbo ya mtiririko, ni muhimu utumie Nonce nasibu ili kuchagua ufunguo wa faragha kwa kila tukio la mawasiliano. Vinginevyo, matokeo ya usimbaji fiche na misimbo hiyo ya mtiririko pia yatakuwa ya kuamua, na kusababisha maswala ya usalama.

Sifa ya block ya kisasa maarufu zaidi ni **Rijndael cipher**. Ilikuwa ingizo lililoshinda kati ya mawasilisho kumi na tano kwa shindano lililofanywa na Taasisi ya Kitaifa ya Viwango na Teknolojia (NIST) kati ya 1997 na 2000 ili kuchukua nafasi ya kiwango cha zamani cha usimbaji fiche, **kiwango cha usimbaji data** (**DES**).

Cipher ya Rijndael inaweza kutumika kwa vipimo tofauti kwa urefu muhimu na ukubwa wa kuzuia, pamoja na njia tofauti za uendeshaji. Kamati ya shindano la NIST ilipitisha toleo dogo la msimbo wa Rijndael—yaani, moja inayohitaji ukubwa wa blok 128 na urefu muhimu wa biti 128, biti 192, au biti 256—kama sehemu ya **kiwango cha juu cha usimbaji fiche** (**AES**). Hiki ndicho kiwango kikuu cha usimbaji fiche wa ulinganifu. Ni salama sana hata NSA inaonekana iko tayari kuitumia na funguo za 256-bit kwa nyaraka za siri za juu. [6]

Sifa ya block ya AES itaelezwa kwa kina katika *Sura ya 5*.

**Maelezo:**

[5] Umuhimu wa usimbaji fiche unaowezekana ulisisitizwa kwanza na Shafi Goldwasser na Silvio Micali, "Usimbaji fiche unaowezekana," _Journal of Computer and System Sciences_, 28 (1984), 270–99.

[6] Angalia NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).

## Kuondoa mkanganyiko

<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Mkanganyiko kuhusu tofauti kati ya herufi block na cipher mtiririko hutokea kwa sababu wakati mwingine watu wataelewa neno block cipher kama likirejelea haswa *block cipher yenye njia ya block ya usimbaji fiche*.

Zingatia aina za ECB na CBC katika sehemu iliyotangulia. Hizi zinahitaji haswa data ili usimbaji fiche iweze kugawanywa na saizi ya kizuizi (ikimaanisha unaweza kutumia pedi kwa ujumbe asili). Kwa kuongeza, data katika njia hizi pia inaendeshwa na block cipher moja kwa moja (na sio tu kuunganishwa na matokeo ya operesheni ya kuzuia cipher kama katika hali ya OFB).

Kwa hivyo, vinginevyo, unaweza kufafanua **block cipher** kama mpango wowote wa usimbaji fiche, unaofanya kazi kwenye vizuizi vya urefu usiobadilika wa ujumbe kwa wakati mmoja (ambapo kizuizi chochote lazima kiwe kirefu kuliko baiti, vinginevyo kitaanguka na kuwa cipher ya mtiririko). Data ya usimbaji fiche na maandishi ya siri lazima igawanywe sawasawa katika ukubwa huu wa kizuizi. Kwa kawaida, ukubwa wa block ni 64, 128, 192, au 256 bits kwa urefu. Kinyume chake, misimbo ya mtiririko inaweza kusimba ujumbe wowote katika vipande vya biti moja au baiti kwa wakati mmoja.

Kwa ufahamu huu mahususi zaidi wa block cipher, unaweza kweli kudai kuwa mifumo ya kisasa ya usimbaji fiche ni mtiririko au block cipher. Kuanzia hapa na kuendelea, nitamaanisha neno block cipher kwa maana ya jumla isipokuwa kubainishwa vinginevyo.

Majadiliano kuhusu hali ya OFB katika sehemu iliyotangulia pia yanaibua hoja nyingine ya kuvutia. Baadhi ya sifa za mtiririko zimeundwa kutoka kwa herufi za kuzuia, kama vile Rijndael kwa kutumia OFB. Baadhi kama Salsa20 na ChaCha hazijaundwa kutoka kwa herufi za kuzuia. Unaweza kuita hii ya mwisho **ciphers mkondo wa awali**. (Kwa kweli hakuna neno sanifu la kurejelea misimbo ya mtiririko kama huu.)

Watu wanapozungumza kuhusu manufaa na hasara za mtiririko wa siphero na herufi za kuzuia, kwa kawaida wanalinganisha misimbo ya awali ya mtiririko na mbinu za usimbaji fiche kulingana na herufi za kuzuia.

Ingawa unaweza kuunda msimbo wa mtiririko kwa urahisi kutoka kwa block cipher, kwa kawaida ni vigumu sana kuunda aina fulani ya ujenzi kwa njia ya kuzuia ya usimbaji fiche (kama vile modi ya CBC) kutoka kwa misimbo ya awali ya mkondo.

Kutokana na mjadala huu, sasa unapaswa kuelewa *Kielelezo 8*. Inatoa muhtasari wa mipango ya usimbaji fiche linganifu. Tunatumia aina tatu za mbinu za usimbaji fiche: herufi za mtiririko wa awali, misimbo ya nyuma ya mtiririko wa misimbo, na kuzuia misimbo katika hali ya kuzuia (pia huitwa "block ciphers" kwenye mchoro).

*Kielelezo cha 8: Muhtasari wa mifumo ya usimbaji linganifu*

![Figure 8: Overview of symmetric encryption schemes](assets/Figure4-8.webp "Figure 8: Overview of symmetric encryption schemes")

## Misimbo ya uthibitishaji wa ujumbe

<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Usimbaji fiche unahusika na usiri. Lakini cryptography pia inahusika na mada pana, kama vile uadilifu wa ujumbe, uhalisi, na kutokataa. Inayoitwa **misimbo ya uthibitishaji wa ujumbe** (MACs) ni miundo muhimu ya kriptografia linganifu ambayo inasaidia uhalali na uadilifu katika mawasiliano.

Kwa nini ni kitu chochote, lakini usiri unahitajika katika mawasiliano? Tuseme kwamba Bob anamtumia Alice ujumbe kwa kutumia usimbaji fiche usioweza kuvunjika. Mshambulizi yeyote anayekatiza ujumbe huu hataweza kujua maarifa yoyote muhimu kuhusu yaliyomo. Walakini, mshambuliaji bado ana angalau vekta zingine mbili za uvamizi zinazopatikana kwake:

1. Angeweza kukatiza maandishi ya siri, kubadilisha yaliyomo, na kutuma maandishi ya siri yaliyobadilishwa kwa Alice.

2. Angeweza kuzuia ujumbe wa Bob kabisa na kutuma maandishi yake mwenyewe yaliyoundwa.

Katika visa hivi vyote viwili, mshambulizi anaweza asiwe na maarifa yoyote kuhusu yaliyomo kutoka kwa maandishi (1) na (2). Lakini bado anaweza kusababisha uharibifu mkubwa kwa njia hii. Hapa ndipo misimbo ya uthibitishaji wa ujumbe inakuwa muhimu.

Misimbo ya uthibitishaji wa ujumbe hufafanuliwa kwa urahisi kama mifumo ya ulinganifu ya kriptografia yenye algoriti tatu: algoriti ya uundaji muhimu, algoriti ya kuunda lebo, na kanuni ya uthibitishaji. MAC salama huhakikisha kuwa vitambulisho **haviwezi kusahaulika** kwa mvamizi yeyote—yaani, hawawezi kuunda lebo kwenye ujumbe ambao huthibitisha, isipokuwa wawe na ufunguo wa faragha.

Bob na Alice wanaweza kukabiliana na upotoshaji wa ujumbe fulani kwa kutumia MAC. Tuseme kwa sasa kwamba hawajali usiri. Wanataka tu kuhakikisha kwamba ujumbe uliopokelewa na Alice ni kweli kutoka kwa Bob na haujabadilishwa kwa njia yoyote.

Mchakato umeonyeshwa kwenye *Kielelezo 9*. Ili kutumia **MAC** (Msimbo wa Uthibitishaji wa Ujumbe), wangetumia kwanza generate ufunguo wa faragha $K$ ambao unashirikiwa kati yao wawili. Bob huunda lebo $T$ kwa ujumbe kwa kutumia ufunguo wa faragha $K$. Kisha anatuma ujumbe huo pamoja na tag ya ujumbe kwa Alice. Kisha anaweza kuthibitisha kwamba Bob ndiye aliyetengeneza lebo hiyo, kwa kutumia ufunguo wa faragha, ujumbe, na lebo kupitia kanuni ya uthibitishaji.

*Kielelezo cha 9: Muhtasari wa mifumo ya usimbaji linganifu*

![Figure 9: Overview of symmetric encryption schemes](assets/Figure4-9.webp "Figure 9: Overview of symmetric encryption schemes")

Kwa sababu ya **kutoweza kusamehewa**, mshambuliaji hawezi kubadilisha ujumbe $M$ kwa njia yoyote au kuunda ujumbe wake mwenyewe kwa kutumia lebo halali. Hii ni hivyo, hata kama mshambuliaji atatazama lebo za jumbe nyingi kati ya Bob na Alice zinazotumia ufunguo sawa wa faragha. Mara nyingi, mshambuliaji anaweza kumzuia Alice kupokea ujumbe $M$ (tatizo ambalo kriptografia haiwezi Address).

MAC inahakikisha kwamba ujumbe uliundwa na Bob. Uhalisi huu, moja kwa moja unamaanisha uadilifu wa ujumbe-yaani, ikiwa Bob ameunda baadhi ya ujumbe, basi, ipso facto, haukubadilishwa kwa njia yoyote na mshambuliaji. Kwa hivyo kuanzia hapa na kuendelea, wasiwasi wowote wa uthibitishaji unapaswa kueleweka kiotomatiki kuashiria wasiwasi wa uadilifu.

Ingawa nimetoa tofauti kati ya uhalisi wa ujumbe na uadilifu katika mjadala wangu, pia ni kawaida kutumia maneno hayo kama visawe. Wao, basi, hurejelea wazo la jumbe ambazo zote mbili ziliundwa na mtumaji fulani na hazijabadilishwa kwa njia yoyote. Kwa mtazamo huu, misimbo ya uthibitishaji wa ujumbe mara nyingi pia huitwa **misimbo ya uadilifu ya ujumbe**.

## Usimbaji fiche ulioidhinishwa

<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Kwa kawaida, ungetaka kuhakikisha usiri na uhalisi katika mawasiliano na, kwa hivyo, mipango ya usimbaji fiche na mifumo ya MAC kwa kawaida hutumiwa pamoja.

**mpango wa usimbaji ulioidhinishwa** ni mpango unaochanganya usimbaji fiche na MAC kwa njia salama sana. Hasa, inapaswa kukidhi viwango vya kutoweza kusamehewa na vile vile dhana dhabiti sana ya usiri, ambayo ni sugu kwa **mashambulizi ya maandishi yaliyochaguliwa**. [7]

Ili mpango wa usimbaji fiche ustahimili mashambulizi ya maandishi-siri yaliyochaguliwa, ni lazima utimize viwango vya **kutokuharibika**: yaani, urekebishaji wowote wa maandishi ya siri unaofanywa na mshambulizi unapaswa kutoa maandishi ya siri batili au yale ambayo yanasimbua kwa maandishi wazi yasiyohusiana na ya awali. [8]

Kwa vile mpango wa usimbaji fiche ulioidhinishwa huhakikisha kwamba maandishi ya siri yaliyoundwa na mshambulizi daima ni batili (kwa vile lebo haitathibitishwa), inakidhi viwango vya upinzani dhidi ya mashambulizi ya maandishi yaliyochaguliwa. Jambo la kufurahisha ni kwamba unaweza kuthibitisha kuwa mpango ulioidhinishwa wa usimbaji fiche unaweza kuundwa kila wakati kutokana na mchanganyiko wa MAC isiyoweza kusahaulika na mpango wa usimbaji fiche ambao unakidhi dhana yenye nguvu kidogo ya usalama, inayojulikana kama **chosen-plaintext-attack security**.

Hatutachunguza maelezo yote ya kuunda mifumo ya usimbaji iliyothibitishwa. Lakini ni muhimu kujua maelezo mawili ya ujenzi wao.

Kwanza, mpango wa usimbaji ulioidhinishwa hushughulikia kwanza usimbaji fiche na kisha kuunda lebo ya ujumbe kwenye maandishi ya siri. Inabadilika kuwa mbinu zingine—kama vile kuchanganya maandishi ya siri na lebo kwenye maandishi wazi, au kwanza kuunda lebo na kisha kusimba maandishi wazi na lebo—si salama. Kwa kuongeza, shughuli zote mbili zina ufunguo wao wa faragha uliochaguliwa kwa nasibu, vinginevyo usalama wako umehatarishwa sana.

Kanuni iliyotajwa hapo juu inatumika kwa ujumla zaidi: *unapaswa kutumia vitufe mahususi kila wakati unapochanganya miundo msingi ya kriptografia*.

Mpango wa usimbaji ulioidhinishwa umeonyeshwa kwenye *Mchoro 10*. Bob kwanza huunda maandishi ya siri $C$ kutoka kwa ujumbe $M$ kwa kutumia ufunguo uliochaguliwa nasibu $K_C$. Kisha huunda lebo ya ujumbe $T$ kwa kuendesha maandishi ya siri na ufunguo tofauti uliochaguliwa bila mpangilio $K_T$ kupitia algoriti ya kutengeneza lebo. Nakala ya siri na tagi ya ujumbe hutumwa kwa Alice.

Sasa Alice anakagua kwanza ikiwa lebo hiyo ni halali kwa kuzingatia maandishi ya siri $C$ na ufunguo $K_T$. Ikiwa ni halali, basi anaweza kusimbua ujumbe kwa kutumia kitufe cha $K_C$. Sio tu kwamba anahakikishiwa dhana kali sana ya usiri katika mawasiliano yao, lakini pia anajua ujumbe uliundwa na Bob.

*Kielelezo 10: Mpango wa usimbaji uliothibitishwa*

![Figure 10: An authenticated encryption scheme](assets/Figure4-10.webp "Figure 10: An authenticated encryption scheme")

Je, MAC zinaundwaje? Ingawa MAC zinaweza kuundwa kupitia mbinu nyingi, njia ya kawaida na bora ya kuziunda ni kupitia **vitendaji vya kriptografia Hash**.

Tutaanzisha vitendaji vya kriptografia Hash kwa kina zaidi katika *Sura ya 6*. Kwa sasa, fahamu tu kuwa **Hash chaguo za kukokotoa** ni chaguo za kukokotoa zinazoweza kukokotwa kwa ufanisi ambazo huchukua maingizo ya ukubwa usio na mpangilio na hutoa matokeo ya urefu usiobadilika. Kwa mfano, kazi maarufu ya Hash **SHA-256** (algorithm salama ya Hash 256) daima hutoa pato la 256-bit bila kujali ukubwa wa pembejeo. Baadhi ya vitendaji vya Hash, kama vile SHA-256, vina programu muhimu katika usimbaji fiche.

Aina ya kawaida ya lebo inayozalishwa kwa njia ya kriptografia ya Hash ni msimbo wa uthibitishaji wa ujumbe unaotegemea Hash** (HMAC). Mchakato umeonyeshwa kwenye *Mchoro 11*. Sherehe hutoa vitufe viwili tofauti kutoka kwa ufunguo wa faragha $K$, ufunguo wa ndani $K_1$ na ufunguo wa nje $K_2$. Maandishi ya wazi $M$ au maandishi ya siri $C$ basi huharakishwa pamoja na ufunguo wa ndani. Matokeo $T'$ basi huharakishwa kwa ufunguo wa nje ili kutoa lebo ya ujumbe $T$.

Kuna palette ya kazi za Hash ambazo zinaweza kutumika kuunda HMAC. Chaguo za kukokotoa za Hash zinazotumika zaidi ni SHA-256.

*Kielelezo 11: HMAC*

![Figure 11: HMAC](assets/Figure4-11.webp "Figure 11: HMAC")

**Maelezo:**

[7] Matokeo mahususi yaliyojadiliwa katika sehemu hii yanatoka kwa Katz na Lindell, ukurasa wa 131–47.

[8] Kitaalamu, ufafanuzi wa mashambulio yaliyochaguliwa ya maandishi ya misimbo ni tofauti na dhana ya kutoweza kuharibika. Lakini unaweza kuonyesha kwamba dhana hizo mbili za usalama ni sawa.

## Salama vikao vya mawasiliano

<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Tuseme kwamba pande mbili ziko kwenye kikao cha mawasiliano, kwa hivyo wanatuma ujumbe mwingi huku na huko.

Mpango wa usimbaji fiche ulioidhinishwa humruhusu mpokeaji ujumbe kuthibitisha kwamba uliundwa na mshirika wake katika kipindi cha mawasiliano ( mradi tu ufunguo wa faragha haujavuja). Hii inafanya kazi vizuri vya kutosha kwa ujumbe mmoja. Kwa kawaida, hata hivyo, pande mbili zinatuma ujumbe huku na huko katika kipindi cha mawasiliano. Na katika mpangilio huo, mpango wa usimbaji ulioidhinishwa wazi kama ilivyoelezwa katika sehemu iliyotangulia haukosi katika kutoa usalama.

Sababu kuu ni kwamba mpango wa usimbaji ulioidhinishwa hautoi hakikisho lolote kwamba ujumbe huo pia ulitumwa na wakala aliyeuunda ndani ya kipindi cha mawasiliano. Fikiria vijidudu vitatu vifuatavyo vya kushambulia:

1. **Shambulio la kurudia**: Mshambulizi anatuma tena maandishi ya siri na lebo ambayo alinasa kati ya watu wawili katika hatua ya awali.

2. **Kupanga upya mashambulizi**: Mshambulizi hukatiza ujumbe mbili kwa nyakati tofauti na kuzituma kwa mpokeaji kwa mpangilio wa kinyume.

3. **Shambulio la kutafakari**: Mshambulizi anatazama ujumbe uliotumwa kutoka A hadi B, na pia kutuma ujumbe huo kwa A.

Ingawa mshambulizi hana ufahamu wa maandishi ya siri na hawezi kuunda maandishi potofu, mashambulizi yaliyo hapo juu bado yanaweza kusababisha uharibifu mkubwa katika mawasiliano.

Tuseme, kwa mfano, kwamba ujumbe fulani kati ya pande hizo mbili unahusisha uhamisho wa fedha za kifedha. Mashambulizi ya marudio yanaweza kuhamisha pesa mara ya pili. Mpango wa usimbaji ulioidhinishwa wa vanilla hauna ulinzi dhidi ya mashambulizi kama hayo.

Kwa bahati nzuri, aina hizi za mashambulizi zinaweza kupunguzwa kwa urahisi katika kipindi cha mawasiliano kwa kutumia **vitambulishi** na **viashiria vya wakati jamaa**.

Vitambulishi vinaweza kuongezwa kwenye ujumbe wa maandishi kabla ya usimbaji fiche. Hii inaweza kuzuia mashambulizi yoyote ya kutafakari. Kiashiria cha wakati wa jamaa kinaweza, kwa mfano, kuwa nambari ya mlolongo katika kipindi fulani cha mawasiliano. Kila mhusika huongeza nambari ya mfuatano kwenye ujumbe kabla ya usimbaji fiche, ili mpokeaji ajue ujumbe ulitumwa kwa utaratibu gani. Hii inaondoa uwezekano wa kuagiza tena mashambulizi. Pia huondoa mashambulizi ya kurudiwa. Ujumbe wowote utakaotumwa na mshambulizi kwenye mstari utakuwa na nambari ya zamani ya mfuatano, na mpokeaji atajua hatauchakata tena.

Ili kuonyesha jinsi vipindi salama vya mawasiliano hufanya kazi, tuseme tena Alice na Bob. Wanatuma jumla ya jumbe nne huku na huko. Unaweza kuona jinsi mpango wa usimbaji fiche ulioidhinishwa wenye vitambulishi na nambari za mfuatano ungefanya kazi hapa chini katika *Mchoro 11*.

Kipindi cha mawasiliano huanza kwa Bob kutuma maandishi ya siri $C_{0,B}$ kwa Alice yenye lebo ya ujumbe $T_{0,B}$. Nakala ya siri ina ujumbe, pamoja na kitambulisho (BOB) na nambari ya mlolongo (0). Lebo $T_{0,B}$ inaundwa kwa maandishi yote ya siri. Katika mawasiliano yao yanayofuata, Alice na Bob wanadumisha itifaki hii, wakisasisha nyuga inapohitajika.

*Kielelezo 12: Kikao salama cha mawasiliano*

![Figure 12: A secure communication session](assets/Figure4-12.webp "Figure 12: A secure communication sessesion")

# RC4 na AES

<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## Msimbo wa mkondo wa RC4

<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

Katika Sura hii, tutajadili maelezo ya mpango wa usimbaji fiche kwa kutumia msimbo wa kisasa wa mkondo wa primitive, RC4 (au "Rivest cipher 4"), na msimbo wa kisasa wa kuzuia, AES. Ingawa RC4 cipher imeacha kutumika kama njia ya usimbaji fiche, AES ndiyo kiwango cha usimbaji fiche wa kisasa wa ulinganifu. Mifano hii miwili inapaswa kutoa wazo bora la jinsi usimbaji fiche wa ulinganifu unavyofanya kazi chini ya kofia.

___

Ili kuwa na hisia ya jinsi misimbo ya kisasa ya mkondo wa uwongo hufanya kazi, nitazingatia msimbo wa mkondo wa RC4. Ni msimbo wa utiririshaji wa uwongo ambao ulitumika katika itifaki za usalama za sehemu ya kufikia pasiwaya ya WEP na WAP na pia katika TLS. Kwa vile RC4 ina udhaifu mwingi uliothibitishwa, imeanguka katika kutopendezwa. Kwa hakika, Kikosi Kazi cha Uhandisi wa Mtandao sasa kinakataza matumizi ya vyumba vya RC4 kwa mteja na programu za seva katika matukio yote ya TLS. Walakini, inafanya kazi vizuri kama mfano ili kuonyesha jinsi cipher ya mkondo wa zamani inavyofanya kazi.

Kuanza, kwanza nitaonyesha jinsi ya kusimba ujumbe wa maandishi wazi kwa njia fiche ya mtoto RC4. Tuseme ujumbe wetu wa maandishi ni "SUPU." Usimbaji fiche kwa kutumia msimbo wa RC4 wa mtoto, basi, unaendelea kwa hatua nne.

### Hatua ya 1

Kwanza, fafanua safu **S** yenye $S[0] = 0$ hadi $S[7] = 7$. Mkusanyiko hapa unamaanisha tu mkusanyo wa thamani unaoweza kubadilika uliopangwa na faharasa, pia huitwa orodha katika baadhi ya lugha za programu (k.m., Python). Katika kesi hii, faharasa huanzia 0 hadi 7, na maadili pia huanzia 0 hadi 7. Kwa hivyo **S** ni kama ifuatavyo:


- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Thamani hapa si nambari za ASCII, lakini ni uwakilishi wa thamani ya desimali ya mifuatano ya baiti 1. Kwa hivyo thamani 2 inaweza kuwa $0000 \ 0011$. Urefu wa safu **S** ni, kwa hivyo, ka 8.

### Hatua ya 2

Pili, fafanua safu muhimu **K** ya urefu wa baiti 8 kwa kuchagua ufunguo kati ya baiti 1 na 8 (bila sehemu za baiti zinazoruhusiwa). Kwa vile kila baiti ni biti 8, unaweza kuchagua nambari yoyote kati ya 0 na 255 kwa kila baiti ya ufunguo wako.

Tuseme tutachagua ufunguo wetu **k** kama $[14, 48, 9]$, ili uwe na urefu wa baiti 3. Kila faharisi ya safu yetu muhimu, basi, imewekwa kulingana na thamani ya desimali ya kipengele hicho cha ufunguo, kwa mpangilio. Ikiwa unapitia ufunguo wote, anza tena mwanzoni, mpaka umejaza nafasi 8 za safu muhimu. Kwa hivyo, safu yetu kuu ni kama ifuatavyo.


- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Hatua ya 3

Tatu, tutabadilisha safu **S** kwa kutumia safu ya ufunguo **K**, katika mchakato unaojulikana kama **kuratibu vitufe**. Mchakato ni kama ifuatavyo katika pseudocode:


- Unda vigeu **j** na **i**
- Weka tofauti $j = 0$
- Kwa kila $i$ kutoka 0 hadi 7:
    - Weka $j = (j + S[i] + K[i]) \mod 8$
    - Badilisha $S[i]$ na $S[j]$

Mabadiliko ya safu **S** yamenaswa na *Jedwali la 1*.

Kuanza, unaweza kuona hali ya awali ya **S** kama $[0, 1, 2, 3, 4, 5, 6, 7]$ na thamani ya awali ya 0 kwa **j**. Hii itabadilishwa kwa kutumia safu muhimu $[14, 48, 9, 14, 48, 9, 14, 48]$.

Kwa kitanzi huanza na $i = 0$. Kulingana na pseudocode yetu hapo juu, thamani mpya ya **j** inakuwa 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Kwa kubadilisha $S[0]$ na $S[6]$, hali ya **S** baada ya raundi 1 inakuwa $[6, 1, 2, 3, 4, 5, 0, 7]$.

Katika safu inayofuata, $i = 1$. Kupitia kwa kitanzi tena, **j** inapata thamani ya 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Kubadilisha $S[1]$ na $S[7]$ kutoka hali ya sasa ya **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, hutoa $[6, 7, 2, 3, 4, 5, 0, 1]$ baada ya raundi ya 2.

Tunaendelea na mchakato huu hadi tutoe safu ya mwisho chini kwa safu **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Jedwali la 1: Jedwali kuu la kuratibu*

| Mzunguko | mimi | j |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |

| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |

|         |     |     |     |      |      |      |      |      |      |      |      |

| Awali |     | 0 |     | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| 1 | 0 | 6 |     | 6 | 1 | 2 | 3 | 4 | 5 | 0 | 7 |

| 2 | 1 | 7 |     | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 3 | 2 | 2 |     | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 4 | 3 | 3 |     | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 5 | 4 | 3 |     | 6 | 7 | 2 | 0 | 3 | 5 | 4 | 1 |

| 6 | 5 | 6 |     | 6 | 4 | 2 | 0 | 3 | 7 | 5 | 1 |

| 7 | 6 | 1 |     | 6 | 4 | 2 | 0 | 3 | 7 | 5 | 2 |

| 8 | 7 | 2 |     | 6 | 4 | 1 | 0 | 3 | 7 | 5 | 2 |

### Hatua ya 4

Kama hatua ya nne, tunatoa **mkondo muhimu**. Huu ni mfuatano wa pseudorandom wa urefu sawa na ujumbe tunaotaka kutuma. Hii itatumika kusimba ujumbe asilia “SOUP” kwa njia fiche. Kwa vile mtiririko wa ufunguo unahitaji kuwa mrefu kama ujumbe, tunahitaji moja ambayo ina baiti 4.

Njia kuu inatolewa na pseudocode ifuatayo:


- Unda vigezo **j**, **i**, na **t**.
- Weka $j = 0$.
- Kwa kila $i$ ya maandishi wazi, kuanzia $i = 1$ na kwenda hadi $i = 4$, kila baiti ya mkondo muhimu inatolewa kama ifuatavyo:
    - $j = (j + S[i]) \mod 8$
    - Badilisha $S[i]$ na $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - Baiti ya $i^{th}$ ya mtiririko muhimu = $S[t]$

Unaweza kufuata mahesabu katika *Jedwali 2*.

Hali ya awali ya **S** ni $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Kuweka $i = 1$, thamani ya **j** inakuwa 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Kisha tunabadilisha $S[1]$ na $S[4]$ ili kuleta mabadiliko ya **S** katika safu mlalo ya pili, $[6, 3, 1, 0, 4, 7, 5, 2]$. Thamani ya **t** basi ni 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Hatimaye, byte ya mtiririko wa ufunguo ni $S[7]$, au 2.

Kisha tunaendelea kutengeneza baiti zingine hadi tuwe na baiti nne zifuatazo: 2, 6, 3, na 7. Kila moja ya baiti hizi inaweza kutumika kusimba kila herufi ya maandishi wazi, "SOUP".

Kuanza, kwa kutumia jedwali la ASCII, tunaweza kuona kwamba "SOUP" iliyosimbwa na maadili ya desimali ya mifuatano ya msingi ya baiti ni "83 79 85 80". Mchanganyiko na mkondo muhimu "2 6 3 7" hutoa "85 85 88 87", ambayo hukaa sawa baada ya operesheni ya modulo 256. Katika ASCII, maandishi "85 85 88 87" ni sawa na "UUXW".

Nini kitatokea ikiwa neno la kusimba lilikuwa refu kuliko safu **S**? Katika hali hiyo, safu **S** inaendelea kubadilika kwa namna hii iliyoonyeshwa hapo juu kwa kila baiti **i** ya maandishi wazi, hadi tuwe na idadi ya baiti kwenye mkondo muhimu sawa na idadi ya herufi katika maandishi wazi.

*Jedwali la 2: Uzalishaji wa mkondo muhimu*

| mimi | j | t | Mkondo mkuu | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |

| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |

|     |     |     |           |      |      |      |      |      |      |      |      |

|     | 0 |     |           | 6 | 4 | 1 | 0 | 3 | 7 | 5 | 2 |

| 1 | 4 | 7 | 2 | 6 | 3 | 1 | 0 | 4 | 7 | 5 | 2 |

| 2 | 5 | 0 | 6 | 6 | 3 | 7 | 0 | 4 | 1 | 5 | 2 |

| 3 | 5 | 1 | 3 | 6 | 3 | 7 | 1 | 4 | 0 | 5 | 2 |

| 4 | 1 | 7 | 2 | 6 | 4 | 7 | 1 | 3 | 0 | 5 | 2 |

Mfano ambao tumeujadili hivi punde ni toleo lisilo na maji la **RC4 mkondo wa cipher**. Cipher halisi ya mtiririko wa RC4 ina safu **S** ya urefu wa baiti 256, si baiti 8, na ufunguo ambao unaweza kuwa kati ya baiti 1 na 256, si kati ya baiti 1 na 8. Safu ya funguo na mitiririko ya funguo zote hutolewa kwa kuzingatia urefu wa baiti 256 wa safu ya **S**. Hesabu zinakuwa ngumu zaidi, lakini kanuni zinabaki sawa. Kwa kutumia ufunguo sawa, [14,48,9], wenye msimbo wa kawaida wa RC4, ujumbe wa maandishi wazi "SOUP" umesimbwa kwa njia fiche kama 67 02 ed df katika umbizo la hexadecimal.

Cipher ya mtiririko ambayo mtiririko muhimu husasisha bila kutegemea ujumbe wa maandishi wazi au maandishi ya siri ni **cipher ya mtiririko inayosawazishwa**. Mkondo wa ufunguo unategemea tu ufunguo. Ni wazi kwamba RC4 ni mfano wa msimbo wa mtiririko unaosawazisha, kwa kuwa mkondo wa ufunguo hauna uhusiano na maandishi wazi au maandishi ya siri. Sifa zetu zote za mtiririko za awali zilizotajwa katika sura iliyotangulia, ikijumuisha sipher ya shift, sifa ya Vigenère, na pedi ya wakati mmoja, pia zilikuwa za aina zinazolingana.

Kinyume chake, **cipher ya mkondo isiyolingana** ina mkondo wa ufunguo ambao unatolewa na ufunguo na awali wa Elements wa maandishi ya siri. Aina hii ya cipher pia inaitwa **sifa inayojisawazisha**.

Muhimu, mkondo wa ufunguo unaozalishwa na RC4 unapaswa kushughulikiwa kama pedi ya mara moja, na huwezi kutoa mtiririko wa vitufe kwa njia sawa kabisa wakati ujao. Badala ya kubadilisha ufunguo kila wakati, suluhu ya vitendo ni kuchanganya ufunguo na **Nonce** ili kutoa mkondo wa kati.

## AES yenye ufunguo wa 128-bit

<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Kama ilivyotajwa katika sura iliyotangulia, Taasisi ya Kitaifa ya Viwango na Teknolojia (NIST) ilifanya shindano kati ya 1997 na 2000 ili kubainisha kiwango kipya cha usimbaji fiche linganifu. **Rijndael cipher** imekuwa ingizo la ushindi. Jina ni mchezo wa maneno kwenye majina ya waundaji wa Ubelgiji, Vincent Rijmen na Joan Daemen.

Cipher ya Rijndael ni **block cipher**, kumaanisha kuwa kuna algoriti ya msingi, ambayo inaweza kutumika kwa vipimo tofauti vya urefu muhimu na ukubwa wa block. Unaweza, basi, kuitumia na njia tofauti za uendeshaji ili kuunda mipango ya usimbuaji.

Kamati ya shindano la NIST ilipitisha toleo dogo la msimbo wa Rijndael—yaani toleo linalohitaji ukubwa wa bloku 128 na urefu muhimu wa biti 128, biti 192 au biti 256—kama sehemu ya **Kiwango cha Juu cha Usimbaji Fiche (AES)**. Toleo hili lililobanwa la sifa ya Rijndael pia linaweza kutumika chini ya njia nyingi za utendakazi. Uainisho wa kiwango ni kile kinachojulikana kama **Kiwango cha Juu cha Usimbaji Fiche (AES)**.

Ili kuonyesha jinsi cipher ya Rijndael inavyofanya kazi, msingi wa AES, nitaonyesha mchakato wa usimbuaji kwa ufunguo wa 128-bit. Ukubwa wa ufunguo una athari kwa idadi ya miduara iliyoshikiliwa kwa kila kizuizi cha usimbaji fiche. Kwa funguo 128-bit, raundi 10 zinahitajika. Na biti 192 na biti 256, ingekuwa raundi 12 na 14, mtawaliwa.

Kwa kuongeza, nitafikiri kwamba AES inatumiwa katika **ECB-mode**. Hii hurahisisha maelezo kidogo na haijalishi kwa algoriti ya Rijndael. Ili kuwa na uhakika, hali ya ECB si salama kiutendaji kwa sababu inaongoza kwa usimbaji fiche wa kubainisha. Hali salama inayotumiwa zaidi na AES ni **CBC** (Mnyororo wa Kuzuia Msimbo).

Hebu tuite ufunguo $K_0$. Ujenzi ulio na vigezo vilivyo hapo juu, basi, unaonekana kama katika *Mchoro 1*, ambapo $M_i$ inawakilisha sehemu ya ujumbe wa maandishi 128 na $C_i$ kwa sehemu ya maandishi ya 128. Padding huongezwa kwa maandishi wazi kwa kizuizi cha mwisho, ikiwa maandishi wazi hayawezi kugawanywa sawasawa na saizi ya kizuizi.

*Mchoro wa 1: AES-ECB yenye ufunguo wa 128-bit*

![Figure 1: AES-ECB with a 128-bit key](assets/Figure5-1.webp "Figure 1: AES-ECB with a 128-bit key")

Kila sehemu ya maandishi ya biti 128 hupitia raundi kumi katika mpango wa usimbaji fiche wa Rijndael. Hii inahitaji ufunguo tofauti wa duru kwa kila raundi ($K_1$ hadi $K_{10}$). Hizi hutolewa kwa kila mzunguko kutoka kwa ufunguo asili wa 128-bit $K_0$ kwa kutumia **algorithm ya upanuzi muhimu**. Kwa hivyo, kwa kila kifungu cha maandishi kusimbwa kwa njia fiche, tutatumia ufunguo asilia $K_0$ pamoja na funguo kumi tofauti za duara. Kumbuka kwamba funguo hizi 11 hutumiwa kwa kila kizuizi cha 128-bit cha maandishi wazi ambacho kinahitaji usimbaji fiche.

Algorithm muhimu ya upanuzi ni ndefu na ngumu. Kufanya kazi kupitia hiyo kuna faida kidogo ya didactic. Unaweza kuangalia kupitia algorithm muhimu ya upanuzi peke yako, ikiwa unataka. Mara tu vitufe vya duara vinapotolewa, misimbo ya Rijndael itabadilisha kizuizi cha kwanza cha biti 128 cha maandishi wazi, $M_1$, kama inavyoonekana katika *Mchoro 2*. Sasa tutapitia hatua hizi.

*Mchoro wa 2: Udanganyifu wa $M_1$ kwa sifa ya Rijndael:*

**Mzunguko wa 0:**


- XOR $M_1$ na $K_0$ kuzalisha $S_0$

---
**Duru n kwa n = {1,...,9}:**


- XOR $S_{n-1}$ na $K_n$
- Ubadilishaji wa Byte
- Safu za Badilisha
- Changanya Safu
- XOR $S$ na $K_n$ kuzalisha $S_n$

---
**Mzunguko wa 10:**


- XOR $S_9$ na $K_{10}$
- Ubadilishaji wa Byte
- Safu za Badilisha
- XOR $S$ na $K_{10}$ ili kuzalisha $S_{10}$
- $S_{10}$ = $C_1$

### Mzunguko wa 0

Mzunguko wa 0 wa msimbo wa Rijndael ni wa moja kwa moja. Safu ya $S_0$ inatolewa na operesheni ya XOR kati ya maandishi wazi ya 128-bit na ufunguo wa faragha. Yaani


- $S_0 = M_1 \pamoja na K_0$

### Mzunguko wa 1

Katika raundi ya 1, safu $S_0$ inaunganishwa kwanza na kitufe cha duara $K_1$ kwa kutumia operesheni ya XOR. Hii inazalisha hali mpya ya $S$.

Pili, operesheni ya **Byte badala** inafanywa kwa hali ya sasa ya $S$. Inafanya kazi kwa kuchukua kila baiti ya safu ya $S$ ya baiti 16 na kuibadilisha na baiti kutoka kwa safu inayoitwa **Sanduku la S* la Rijndael**. Kila baiti ina mabadiliko ya kipekee, na hali mpya ya $S$ inatolewa kama matokeo. Kisanduku cha S cha Rijndael kinaonyeshwa kwenye *Kielelezo 3*.

*Kielelezo cha 3: S-Box ya Rijndael*

|     | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 0A | 0b | 0C | 0D | 0E | 0F |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 00 | 63 | 7C | 77 | 7b | F2 | 6b | 6F | C5 | 30 | 01 | 67 | 2B | FE | D7 | AB | 76 |

| 10 | CA | 82 | C9 | 7D | FA | 59 | 47 | F0 | AD | D4 | A2 | AF | 9C | A4 | 72 | C0 |

| 20 | B7 | FD | 93 | 26 | 36 | 3F | F7 | CC | 34 | A5 | E5 | F1 | 71 | D8 | 31 | 15 |

| 30 | 04 | C7 | 23 | C3 | 18 | 96 | 05 | 9A | 07 | 12 | 80 | E2 | EB | 27 | B2 | 75 |

| 40 | 09 | 83 | 2C | 1A | 1b | 6E | 5A | A0 | 52 | 3b | D6 | B3 | 29 | E3 | 2F | 84 |

| 50 | 53 | D1 | 00 | ED | 20 | FC | B1 | 5B | 6A | CB | KUWA | 39 | 4A | 4C | 58 | CF |

| 60 | D0 | EF | AA | FB | 43 | 4D | 33 | 85 | 45 | F9 | 02 | 7F | 50 | 3C | 9F | A8 |

| 70 | 51 | A3 | 40 | 8F | 92 | 9D | 38 | F5 | BC | B6 | DA | 21 | 10 | FF | F3 | D2 |

| 80 | CD | 0C | 13 | EC | 5F | 97 | 44 | 17 | C4 | A7 | 7E | 3D | 64 | 5D | 19 | 73 |

| 90 | 60 | 81 | 4F | DC | 22 | 2A | 90 | 88 | 46 | EE | B8 | 14 | DE | 5E | 0b | DB |

| A0 | E0 | 32 | 3A | 0A | 49 | 06 | 24 | 5C | C2 | D3 | AC | 62 | 91 | 95 | E4 | 79 |

| B0 | E7 | C8 | 37 | 6D | 8D | D5 | 4E | A9 | 6C | 56 | F4 | EA | 65 | 7A | AE | 08 |

| C0 | BA | 78 | 25 | 2E | 1C | A6 | B4 | C6 | E8 | DD | 74 | 1F | 4b | BD | 8b | 8A |

| D0 | 70 | 3E | B5 | 66 | 48 | 03 | F6 | 0E | 61 | 35 | 57 | B9 | 86 | C1 | 1D | 9E |

| E0 | E1 | F8 | 98 | 11 | 69 | D9 | 8E | 94 | 9b | 1E | 87 | E9 | CE | 55 | 28 | DF |

| F0 | 8C | A1 | 89 | 0D | BF | E6 | 42 | 68 | 41 | 99 | 2D | 0F | B0 | 54 | BB | 16 |

S-Box hii ni sehemu moja ambapo aljebra dhahania inatumika katika misimbo ya Rijndael, haswa **Nga za Galois**.

Kuanza, unafafanua kila kipengele cha baiti 00 kupitia FF kama vekta 8-bit. Kila vekta kama hii ni kipengele cha **uga wa Galois GF(2^8)** ambapo polimanomia isiyoweza kurekebishwa kwa uendeshaji wa modulo ni $x^8 + x^4 + x^3 + x + 1$. Sehemu ya Galois iliyo na maelezo haya pia inaitwa **Uga wa Rijndael Finite**.

Ifuatayo, kwa kila kipengele kinachowezekana kwenye shamba, tunaunda kile kinachoitwa **Nyberg S-Box**. Katika kisanduku hiki, kila baiti imechorwa kwenye **inverse yake ya kuzidisha** (yaani, ili bidhaa yao iwe sawa na 1). Kisha tunapanga thamani hizo kutoka kwa Nyberg S-box hadi S-Box ya Rijndael kwa kutumia **mabadiliko ya kushikamana**.

Operesheni ya tatu kwenye safu ya **S** ni ya **safu mlalo za mabadiliko**. Inachukua hali ya **S** na kuorodhesha baiti zote kumi na sita kwenye matrix. Kujazwa kwa matrix huanza upande wa kushoto wa juu na kufanya kazi kwa njia yake kwa kwenda kutoka juu hadi chini na kisha, kila wakati safu imejaa, na kuhamisha safu moja kulia na juu.

Mara tu matriki ya **S** imeundwa, safu mlalo nne huhamishwa. Safu ya kwanza inakaa sawa. Safu ya pili inasonga moja kwenda kushoto. Ya tatu inasonga mbili kwenda kushoto. Ya nne inasonga tatu kwenda kushoto. Mfano wa mchakato umetolewa katika *Kielelezo 4*. Hali ya asili ya **S** inaonyeshwa juu, na hali ya matokeo baada ya uendeshaji wa safu za mabadiliko imeonyeshwa chini yake.

*Mchoro wa 4: Operesheni ya kubadilisha safu mlalo*

| F1 | A0 | B1 | 23 |

|------|------|------|-------|

| 59 | EF | 09 | 82 |

| 97 | 01 | B0 | CC |

| D4 | 72 | 04 | 21 |

| F1 | A0 | B1 | 23 |

|------|------|------|-------|

| EF | 09 | 82 | 59 |

| B0 | CC | 97 | 01 |

| 21 | D4 | 72 | 04 |

Katika hatua ya nne, **Nga za Galois** zinaonekana tena. Kuanza, kila safu wima ya **S** inazidishwa na safu wima ya 4 x 4 inayoonekana katika *Mchoro 5*. Lakini badala ya kuwa kuzidisha kwa matrix ya kawaida, ni kuzidisha kwa vekta **modulo ya polinomia isiyoweza kupunguzwa**, $x^8 + x^4 + x^3 + x + 1$. Migawo ya vekta inayotokana inawakilisha biti za kibinafsi za baiti.

*Kielelezo 5: Changanya safu wima matrix*

| 02 | 03 | 01 | 01 |

|------|------|------|-------|

| 01 | 02 | 03 | 01 |

| 01 | 01 | 02 | 03 |

| 03 | 01 | 01 | 02 |

Kuzidisha safu wima ya kwanza ya **S** yenye matrix 4 x 4 hapo juu hutoa matokeo katika *Mchoro 6*.

*Kielelezo 6: Kuzidisha safu ya kwanza:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Kama hatua inayofuata, masharti yote kwenye matrix yatalazimika kugeuzwa kuwa polynomials. Kwa mfano, F1 inawakilisha baiti 1 na itakuwa $x^7 + x^6 + x^5 + x^4 + 1$, na 03 inawakilisha baiti 1 na itakuwa $x + 1$.

Kisha kuzidisha zote kunafanywa **modulo** $x^8 + x^4 + x^3 + x + 1$. Hii inasababisha kuongezwa kwa polynomia nne katika kila seli nne za safu. Baada ya kutekeleza nyongeza hizo **modulo 2**, utaishia na polima nne. Kila moja ya polima hizi inawakilisha mfuatano wa biti 8, au baiti 1, ya **S**. Hatutafanya hesabu hizi zote hapa kwenye tumbo kwenye *Mchoro 6* kwani ni pana.

Mara safu wima ya kwanza inapochakatwa, safu wima zingine tatu za **S** tumbo huchakatwa kwa njia ile ile. Hatimaye, hii itatoa matrix yenye byte kumi na sita ambayo inaweza kubadilishwa kuwa safu.

Kama hatua ya mwisho, safu **S** imeunganishwa na kitufe cha pande zote tena katika operesheni ya **XOR**. Hii inazalisha jimbo $S_1$. Yaani


- $S_1 = S \plus K_0$

### Raundi ya 2 hadi 10

Raundi ya 2 hadi 9 ni marudio tu ya raundi ya 1, *mutatis mutandis*. Raundi ya mwisho inaonekana sawa na duru zilizopita, isipokuwa kwamba hatua ya **mchanganyiko wa safu** imeondolewa. Hiyo ni, raundi ya 10 inatekelezwa kama ifuatavyo:


- $S_9 \pamoja na K_{10}$
- Ubadilishaji wa Byte
- Safu za Badilisha
- $S_{10} = S \plus K_{10}$

Hali $S_{10}$ sasa imewekwa kuwa $C_1$, biti 128 za kwanza za maandishi ya siri. Kuendelea kupitia vizuizi vya maandishi 128-bit vilivyosalia kunatoa maandishi kamili ya siri **C**.

### Shughuli za msimbo wa Rijndael

Je, ni hoja gani nyuma ya shughuli tofauti zinazoonekana katika misimbo ya Rijndael?

Bila kuingia katika maelezo, mipango ya usimbaji fiche inatathminiwa kwa misingi ya kiwango kinacholeta mkanganyiko na uenezaji. Ikiwa mpango wa usimbaji fiche una kiwango cha juu cha **mkanganyiko**, inamaanisha kuwa maandishi ya siri yanaonekana tofauti sana na maandishi wazi. Iwapo mpango wa usimbaji fiche una kiwango cha juu cha **uenezaji**, inamaanisha kuwa mabadiliko yoyote madogo kwenye maandishi wazi yanazalisha maandishi ya siri tofauti kabisa.

Sababu ya utendakazi nyuma ya misimbo ya Rijndael ni kwamba hutoa kiwango cha juu cha mkanganyiko na mtawanyiko. Kuchanganyikiwa kunazalishwa na operesheni ya ubadilishaji wa Byte, wakati uenezaji hutolewa na safu za mabadiliko na shughuli za safu wima.

# Asymmetric Cryptography

<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Tatizo kuu la usambazaji na usimamizi

<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Kama ilivyo kwa kriptografia linganifu, mifumo isiyolinganishwa inaweza kutumika ili kuhakikisha usiri na uthibitishaji. Kwa kulinganisha, hata hivyo, mipango hii hutumia funguo mbili badala ya moja: ufunguo wa kibinafsi na wa umma.

Tunaanza uchunguzi wetu kwa ugunduzi wa kriptografia isiyolinganishwa, haswa matatizo ambayo yalichochea. Ifuatayo, tunajadili jinsi mipango ya asymmetric ya usimbaji fiche na uthibitishaji inavyofanya kazi kwa kiwango cha juu. Basi, tunatanguliza utendakazi wa Hash, ambazo ni muhimu katika kuelewa mipango ya uthibitishaji linganifu, na pia zina umuhimu katika miktadha mingine ya kriptografia, kama vile misimbo ya uthibitishaji ya ujumbe unaotegemea Hash tuliyojadili katika Sura ya 4.

___

Tuseme kwamba Bob anataka kununua koti jipya la mvua kutoka kwa Jim's Sporting Goods, muuzaji wa rejareja wa bidhaa za michezo mtandaoni na mamilioni ya wateja nchini Amerika Kaskazini. Huu utakuwa ununuzi wake wa kwanza kutoka kwao na anataka kutumia kadi yake ya mkopo. Kwa hivyo, Bob atahitaji kwanza kufungua akaunti na Bidhaa za Michezo za Jim, ambayo inahitaji kutuma maelezo ya kibinafsi kama vile Address yake na maelezo ya kadi ya mkopo. Basi, anaweza kupitia hatua zinazohitajika ili kununua koti la mvua.

Bidhaa za Michezo za Bob na Jim zitataka kuhakikisha kuwa mawasiliano yao ni salama katika mchakato huu wote, ikizingatiwa kuwa Mtandao ni mfumo wazi wa mawasiliano. Watataka kuhakikisha, kwa mfano, kwamba hakuna mshambulizi anayeweza kubaini kadi ya mkopo ya Bob na maelezo ya Address, na kwamba hakuna mshambuliaji anayeweza kurudia ununuzi wake au kuunda bandia kwa niaba yake.

Mpango wa hali ya juu wa usimbaji fiche kama ulivyojadiliwa katika sura iliyotangulia bila shaka unaweza kufanya mawasiliano kati ya Bidhaa za Michezo za Bob na Jim kuwa salama. Lakini kuna vizuizi vya wazi vya utekelezaji wa mpango kama huo.

Ili kuonyesha vizuizi hivi vya vitendo, tuseme kwamba tuliishi katika ulimwengu ambao tu zana za ulinganifu wa kriptografia zilikuwepo. Je, Bidhaa za Michezo za Jim na Bob, basi, zingeweza kufanya nini ili kuhakikisha mawasiliano salama?

Chini ya hali hizo, wangekabiliwa na gharama kubwa za kuwasiliana kwa usalama. Kwa kuwa Mtandao ni mfumo wazi wa mawasiliano, hawawezi tu Exchange seti ya funguo juu yake. Kwa hivyo, Bob na mwakilishi wa Bidhaa za Michezo za Jim watahitaji kutengeneza Exchange muhimu ana kwa ana.

Uwezekano mmoja ni kwamba Bidhaa za Michezo za Jim huunda maeneo maalum muhimu ya Exchange, ambapo Bob na wateja wengine wapya wanaweza kurejesha seti ya funguo kwa mawasiliano salama. Hii bila shaka itakuja kwa gharama kubwa za shirika na kupunguza kwa kiasi kikubwa ufanisi ambao wateja wapya wanaweza kufanya manunuzi.

Vinginevyo, Bidhaa za Michezo za Jim zinaweza kumtumia Bob jozi ya funguo na mjumbe anayeaminika sana. Huenda hii inafaa zaidi kuliko kupanga maeneo muhimu ya Exchange. Lakini hii bado inaweza kuja kwa gharama kubwa, haswa ikiwa wateja wengi watafanya ununuzi mmoja au machache tu.

Kisha, mpango wa ulinganifu wa usimbaji fiche ulioidhinishwa pia hulazimisha Bidhaa za Michezo za Jim kuhifadhi seti tofauti za funguo kwa wateja wao wote. Hii itakuwa changamoto kubwa ya vitendo kwa maelfu ya wateja, achilia mbali mamilioni.

Ili kuelewa hatua hii ya mwisho, tuseme Bidhaa za Michezo za Jim humpa kila mteja jozi sawa ya funguo. Hii ingemruhusu kila mteja—au mtu mwingine yeyote anayeweza kupata jozi hii ya funguo—kusoma na hata kudhibiti mawasiliano yote kati ya Bidhaa za Michezo za Jim na wateja wake. Unaweza, basi, vile vile usitumie cryptography hata kidogo katika mawasiliano yako.

Hata kurudia seti ya funguo kwa wateja wengine tu ni mazoezi mabaya ya usalama. Mshambulizi yeyote anayetarajiwa anaweza kujaribu kutumia kipengele hicho cha mpango (kumbuka kwamba washambuliaji wanadhaniwa kujua kila kitu kuhusu mpango lakini funguo, kwa mujibu wa kanuni ya Kerckhoffs.)

Kwa hivyo, Bidhaa za Michezo za Jim zingelazimika kuhifadhi jozi ya funguo kwa kila mteja, bila kujali jinsi jozi hizi muhimu zinasambazwa. Hii inatoa wazi matatizo kadhaa ya vitendo.


- Bidhaa za Michezo za Jim zingelazimika kuhifadhi mamilioni ya jozi za funguo, seti moja kwa kila mteja.
- Funguo hizi zingepaswa kulindwa ipasavyo, kwani zingekuwa shabaha ya hakika ya wadukuzi. Ukiukaji wowote wa usalama utahitaji kurudiwa kwa ubadilishanaji wa ufunguo wa gharama kubwa, ama katika maeneo maalum muhimu ya Exchange au kwa mjumbe.
- Mteja yeyote wa Bidhaa za Michezo za Jim atalazimika kuhifadhi kwa usalama jozi ya funguo nyumbani. Hasara na wizi utatokea, unaohitaji marudio ya kubadilishana muhimu. Wateja pia watalazimika kupitia mchakato huu kwa maduka mengine yoyote ya mtandaoni au aina nyingine za huluki wanazotaka kuwasiliana na kufanya nazo miamala kupitia Mtandao.

Changamoto hizi kuu mbili ambazo zimeelezwa hivi punde zilikuwa maswala ya kimsingi hadi mwishoni mwa miaka ya 1970. Yalijulikana kama **tatizo kuu la usambazaji** na **tatizo kuu la usimamizi**, mtawalia.

Matatizo haya yalikuwa yamekuwepo, bila shaka, na mara nyingi yaliunda maumivu ya kichwa katika siku za nyuma. Vikosi vya kijeshi, kwa mfano, vingelazimika kusambaza mara kwa mara vitabu vyenye funguo kwa ajili ya mawasiliano salama kwa wafanyakazi katika uwanja huo kwa hatari na gharama kubwa. Lakini matatizo haya yalikuwa yakizidi kuwa mabaya zaidi huku ulimwengu ukizidi kuingia katika mawasiliano ya masafa marefu, ya kidijitali, hasa kwa mashirika yasiyo ya kiserikali.

Ikiwa matatizo haya hayangetatuliwa katika miaka ya 1970, ununuzi bora na salama katika Bidhaa za Michezo za Jim haungekuwepo. Kwa hakika, sehemu kubwa ya ulimwengu wetu wa kisasa wenye utumiaji wa barua-pepe unaofaa na salama, huduma za benki mtandaoni, na ununuzi huenda zikawa njozi tu. Kitu chochote kinachofanana na Bitcoin hakingeweza kuwepo hata kidogo.

Kwa hivyo, nini kilitokea katika miaka ya 1970? Je, inawezekana vipi kwamba tunaweza kufanya ununuzi papo hapo mtandaoni na kuvinjari kwa usalama Wavuti ya Ulimwenguni Pote? Je, inawezekana vipi kwamba tunaweza kutuma Bitcoins mara moja kote ulimwenguni kutoka kwa simu zetu mahiri?

## Maelekezo mapya katika kriptografia

<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Kufikia miaka ya 1970, matatizo muhimu ya usambazaji na usimamizi yalikuwa yamechukua usikivu wa kikundi cha waandishi wa habari wa kitaaluma wa Marekani: Whitfield Diffie, Martin Hellman, na Ralph Merkle. Wakiwa na mashaka makali kutoka kwa wenzao walio wengi, walijitosa kutafuta suluhu la jambo hilo.

Angalau motisha moja ya msingi kwa mradi wao ilikuwa mtazamo kwamba mawasiliano ya wazi ya kompyuta yangeathiri sana ulimwengu wetu. Kama Diffie na Helmann wanavyosema mnamo 1976,

> Ukuzaji wa mitandao ya mawasiliano inayodhibitiwa na kompyuta huahidi mawasiliano rahisi na ya bei nafuu kati ya watu au kompyuta za pande tofauti za ulimwengu, ikichukua nafasi ya barua na safari nyingi na mawasiliano ya simu. Kwa programu nyingi anwani hizi lazima ziwe salama dhidi ya usikilizaji na udungaji wa ujumbe haramu. Kwa sasa, hata hivyo, ufumbuzi wa matatizo ya usalama uko nyuma ya maeneo mengine ya teknolojia ya mawasiliano. *Kificho cha kisasa hakiwezi kukidhi mahitaji, kwa kuwa matumizi yake yataleta usumbufu mkubwa kwa watumiaji wa mfumo, na hivyo kuondoa faida nyingi za usindikaji wa simu.* [1]
Uimara wa Diffie, Hellman, na Merkle ulizaa matunda. Uchapishaji wa kwanza wa matokeo yao ulikuwa karatasi ya Diffie na Helmann mnamo 1976 yenye kichwa "Maelekezo Mapya katika Uandikaji wa siri." Ndani yake, waliwasilisha njia mbili za asili kwa Address usambazaji muhimu na shida kuu za usimamizi.

Suluhisho la kwanza walilotoa lilikuwa *itifaki ya ufunguo-Exchange* ya mbali, yaani, seti ya sheria za Exchange za funguo moja au zaidi za ulinganifu juu ya njia isiyo salama ya mawasiliano. Itifaki hii sasa inajulikana kama *funguo ya Diffie-Helmann Exchange* au *funguo ya Diffie-Helmann-Merkle Exchange*. [2]

Kwa ufunguo wa Diffie-Helmann Exchange, pande mbili kwanza Exchange baadhi ya taarifa hadharani kwenye chaneli isiyo salama kama vile Mtandao. Kwa msingi wa habari hiyo wao, basi, kwa kujitegemea huunda ufunguo wa ulinganifu (au jozi ya funguo za ulinganifu) kwa mawasiliano salama. Ingawa pande zote mbili huunda funguo zao kwa kujitegemea, maelezo waliyoshiriki hadharani huhakikisha kwamba mchakato huu muhimu wa uundaji hutoa matokeo sawa kwa wote wawili.

Muhimu zaidi, ingawa kila mtu anaweza kutazama taarifa ambayo inabadilishwa hadharani na wahusika kwenye chaneli isiyo salama, ni pande mbili pekee zinazohusika na taarifa ya Exchange zinazoweza kuunda funguo za ulinganifu kutoka kwayo.

Hii, bila shaka, inaonekana kinyume kabisa. Vyama viwili vya Exchange vinawezaje kupata habari hadharani ambayo ingewaruhusu tu kuunda funguo za ulinganifu kutoka kwayo? Kwa nini mtu mwingine yeyote anayetazama habari Exchange hangeweza kuunda funguo sawa?

Inategemea hisabati nzuri bila shaka. Kitufe cha Diffie-Helmann Exchange hufanya kazi kupitia njia moja ya kukokotoa na mlango wa kukamata. Wacha tujadili maana ya maneno haya mawili kwa zamu.

Tuseme kwamba umepewa baadhi ya chaguo za kukokotoa $f(x)$ na matokeo $f(a) = y$, ambapo $a$ ni thamani fulani ya $x$. Tunasema kwamba $f(x)$ ni **kitendakazi cha njia moja** ikiwa ni rahisi kukokotoa thamani $y$ inapopewa $a$ na $f(x)$, lakini haiwezekani kimahesabu kukokotoa thamani $a$ inapotolewa $y$ na $f(x)$. Jina ** kazi ya njia moja **, bila shaka, inatokana na ukweli kwamba kazi hiyo ni ya vitendo tu kuhesabu katika mwelekeo mmoja.

Baadhi ya vitendaji vya njia moja vina kile kinachojulikana kama **trapdoor**. Ingawa haiwezekani kukokotoa $a$ kutokana na $y$ na $f(x)$ pekee, kuna taarifa fulani $Z$ ambayo hufanya kukokotoa $a$ kutoka $y$ kuwezekana kwa njia ya hesabu. Sehemu hii ya habari $Z$ inajulikana kama **trapdoor**. Vitendaji vya njia moja ambavyo vina mlango wa trap vinajulikana kama **vitendaji vya trapdoor**.

Hatutachunguza maelezo ya ufunguo wa Diffie-Helmann Exchange hapa. Lakini kimsingi kila mshiriki huunda habari fulani, ambayo sehemu yake inashirikiwa hadharani na ambayo baadhi yake hubaki kuwa siri. Kila mhusika, basi, huchukua taarifa yake ya siri na taarifa ya umma inayoshirikiwa na upande mwingine kuunda ufunguo wa faragha. Na kwa kiasi fulani kimiujiza, pande zote mbili zitaishia na ufunguo sawa wa kibinafsi.

Mhusika yeyote anayezingatia tu taarifa iliyoshirikiwa hadharani kati ya wahusika wawili katika kitufe cha Diffie Helmann Exchange hawezi kuiga hesabu hizi. Wangehitaji habari ya kibinafsi kutoka kwa mmoja wa pande hizo mbili ili kufanya hivyo.

Ingawa toleo la msingi la ufunguo wa Diffie-Helmann Exchange lililowasilishwa katika karatasi ya 1976 si salama sana, matoleo ya kisasa ya itifaki ya kimsingi bado yanatumika leo. Muhimu zaidi, kila itifaki muhimu ya Exchange katika toleo la hivi punde zaidi la itifaki ya usalama ya usafiri ya Layer (toleo la 1.3) kimsingi ni toleo lililoboreshwa la itifaki iliyowasilishwa na Diffie na Hellman mwaka wa 1976. Itifaki ya usalama ya Layer ndiyo itifaki kuu ya kubadilishana habari kwa usalama iliyoumbizwa kulingana na itifaki ya kiwango cha uhamishaji wa maandishi ya Wavuti.

Muhimu, ufunguo wa Diffie-Helmann Exchange sio mpango wa ulinganifu. Kwa kusema kweli, bila shaka ni mali ya eneo la ufunguo wa ulinganifu wa siri. Lakini kwa vile ufunguo wa Diffie-Helmann wa Exchange na usimbaji fiche usiolinganishwa hutegemea utendakazi wa njia moja wa nadharia ya nambari na milango ya trapdoor, kwa kawaida hujadiliwa pamoja.

Njia ya pili ambayo Diffie na Helmann walitoa kwa Address shida kuu ya usambazaji na usimamizi katika karatasi yao ya 1976, bila shaka, kupitia kriptografia isiyolinganishwa.

Kinyume na uwasilishaji wao wa ufunguo wa Diffie-Hellman Exchange, walitoa tu mtaro wa jumla wa jinsi mipango ya kriptografia isiyolinganishwa inavyoweza kutengenezwa kwa njia dhahiri. Hawakutoa kazi yoyote ya njia moja ambayo inaweza kutimiza haswa masharti yanayohitajika kwa usalama wa kuridhisha katika mipango kama hiyo.

Utekelezaji wa vitendo wa mpango usiolinganishwa, hata hivyo, ulipatikana mwaka mmoja baadaye na waandishi watatu tofauti wa kitaaluma wa kuandika fiche na wanahisabati: Ronald Rivest, Adi Shamir, na Leonard Adleman. [3] Mfumo wa siri walioanzisha ulijulikana kama **RSA cryptosystem** (baada ya majina yao ya mwisho).

Vitendo vya kukokotoa vya mlango wa mtego vinavyotumika katika usimbaji fiche usiolinganishwa (na ufunguo wa Diffie Helmann Exchange) zote zinahusiana na matatizo mawili kuu **kikokotoo cha Hard**: uainishaji msingi na ukokotoaji wa logariti tofauti.

**Uainishaji mkuu** unahitaji, kama jina linamaanisha, kugawanya nambari kamili katika vipengele vyake kuu. Tatizo la RSA kwa mbali ni mfano unaojulikana zaidi wa mfumo wa siri unaohusiana na sababu kuu.

**tatizo la logarithm tofauti** ni tatizo linalotokea katika vikundi vya mzunguko. Kwa kuzingatia jenereta katika kikundi fulani cha mzunguko, inahitaji hesabu ya kipeo cha kipekee kinachohitajika ili kutoa kipengele kingine katika kikundi kutoka kwa jenereta.

Miradi mahususi ya msingi wa logariti hutegemea aina mbili kuu za vikundi vya mzunguko: vikundi zidishi vya nambari kamili na vikundi ambavyo vinajumuisha vidokezo kwenye mikondo ya duaradufu. Kitufe cha asili cha Diffie Helmann Exchange kama inavyowasilishwa katika "Maelekezo Mapya katika Crystalgraphy" hufanya kazi na kikundi cha kuzidisha cha mzunguko cha nambari kamili. Kanuni za saini za kidijitali za Bitcoin na mpango wa sahihi wa Schnorr ulioletwa hivi majuzi (2021) zote zinatokana na tatizo la logarithm maalum kwa kikundi fulani cha mzunguko wa curve elliptic.

Ifuatayo, tutageuka kwa muhtasari wa hali ya juu wa usiri na uthibitishaji katika mpangilio wa asymmetric. Kabla ya kufanya hivyo, hata hivyo, tunahitaji kufanya maelezo mafupi ya kihistoria.

Sasa inaonekana kuwa ni sawa kwamba kikundi cha waandishi wa maandishi wa Uingereza na wanahisabati wanaofanya kazi katika Makao Makuu ya Mawasiliano ya Serikali (GCHQ) walikuwa wamegundua kwa kujitegemea ugunduzi uliotajwa hapo juu miaka michache mapema. Kundi hili lilikuwa na James Ellis, Clifford Cocks, na Malcolm Williamson.

Kulingana na akaunti zao wenyewe na ile ya GCHQ, ni James Ellis ambaye alibuni kwanza dhana ya ufunguo wa siri wa umma mwaka wa 1969. Eti, Clifford Cocks kisha kugundua mfumo wa siri wa RSA mwaka wa 1973, na Malcolm Williamson dhana ya Diffie Helmann muhimu Exchange mwaka wa 1974. asili ya siri ya kazi iliyofanywa katika GCHQ.

**Maelezo:**

[1] Whitfield Diffie na Martin Hellman, “Maelekezo mapya katika usimbaji fiche,” _IEEE Transactions on Information Theory_ IT-22 (1976), uk. 644–654, katika uk. 644.

[2] Ralph Merkle pia anajadili itifaki kuu ya Exchange katika "Mawasiliano salama juu ya njia zisizo salama", _Mawasiliano ya Chama cha Mashine za Kompyuta_, 21 (1978), 294-99. Ingawa Merkle aliwasilisha karatasi hii mbele ya karatasi na Diffie na Hellman, ilichapishwa baadaye. Suluhisho la Merkle si salama kwa kiasi kikubwa, tofauti na la Diffie-Hellman.

[3] Ron Rivest, Adi Shamir, na Leonard Adleman, "Mbinu ya kupata sahihi za kidijitali na mifumo ya siri ya ufunguo wa umma", _Mawasiliano ya Chama cha Mashine ya Kompyuta_, 21 (1978), uk. 120–26.

[4] Historia nzuri ya uvumbuzi huu imetolewa na Simon Singh, _The Code Book_, Fourth Estate (London, 1999), Sura ya 6.

## Usimbaji fiche usio na usawa na uthibitishaji

<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Muhtasari wa **usimbaji fiche usiolinganishwa** kwa usaidizi wa Bob na Alice umetolewa katika *Mchoro 1*.

Alice kwanza huunda jozi ya funguo, zinazojumuisha ufunguo mmoja wa umma ($K_P$) na ufunguo mmoja wa faragha ($K_S$), ambapo "P" katika $K_P$ inawakilisha "umma" na "S" katika $K_S$ kwa "siri". Kisha anasambaza ufunguo huu wa umma kwa uhuru kwa wengine. Tutarudi kwa maelezo ya mchakato huu wa usambazaji baadaye kidogo. Lakini kwa sasa, chukulia kwamba mtu yeyote, ikiwa ni pamoja na Bob, anaweza kupata ufunguo wa umma wa Alice $K_P$ kwa usalama.

Wakati fulani baadaye, Bob anataka kuandika ujumbe $M$ kwa Alice. Kwa vile inajumuisha habari nyeti, anataka yaliyomo yabaki kuwa siri kwa kila mtu isipokuwa Alice. Kwa hivyo, kwanza Bob anasimba ujumbe wake kwa njia fiche $M$ akitumia $K_P$. Kisha anatuma maandishi yanayotokana na $C$ kwa Alice, ambaye anaondoa usimbaji fiche $C$ kwa $K_S$ ili kutoa ujumbe asili $M$.

*Kielelezo cha 1: Usimbaji fiche usiolingana*

![Figure 1: Asymmetric encryption](assets/Figure6-1.webp "Figure 1: Asymmetric encryption")

Adui yeyote anayesikiliza mawasiliano ya Bob na Alice anaweza kuona $C$. Pia anajua $K_P$ na kanuni ya usimbaji fiche $E(\cdot)$. Muhimu hata hivyo, maelezo haya hayamruhusu mvamizi kusimbua kwa urahisi maandishi ya siri $C$. Usimbaji fiche unahitaji $K_S$ haswa, ambayo mvamizi hana.

Mipango ya usimbaji linganifu kwa ujumla inahitaji kuwa salama dhidi ya mshambulizi ambaye anaweza kusimba kwa njia fiche ujumbe wa maandishi wazi (unaojulikana kama usalama wa shambulio la maandishi ya siri iliyochaguliwa). Hata hivyo, haijaundwa kwa madhumuni ya wazi ya kuruhusu uundaji wa maandishi kama hayo halali na mshambuliaji au mtu mwingine yeyote.

Hii ni tofauti kabisa na mpango wa usimbaji fiche usiolinganishwa, ambapo madhumuni yake yote ni kuruhusu mtu yeyote, ikiwa ni pamoja na washambuliaji, kutoa maandishi sahihi ya siri. Kwa hivyo, mipango ya usimbaji fiche isiyolinganishwa inaweza kuwekwa lebo kama **ciphers nyingi za ufikiaji**.

Ili kuelewa vizuri zaidi kile kinachotokea, fikiria kwamba badala ya kutuma ujumbe kwa njia ya kielektroniki, Bob alitaka kutuma barua halisi kwa usiri. Njia moja ya kuhakikisha usiri itakuwa kwa Alice kutuma kufuli salama kwa Bob, lakini weka ufunguo ili kuifungua. Baada ya kuandika barua yake, Bob angeweza kuweka barua hiyo kwenye sanduku na kuifunga kwa kufuli ya Alice. Angeweza, basi, kutuma kisanduku kilichofungwa na ujumbe kwa Alice ambaye ana ufunguo wa kukifungua.

Ingawa Bob ana uwezo wa kufunga kufuli, yeye wala mtu mwingine yeyote anayeingilia kisanduku anaweza kutendua kufuli ikiwa ni salama kabisa. Alice pekee ndiye anayeweza kuifungua na kuona yaliyomo kwenye barua ya Bob kwa sababu ana ufunguo.

Mpango wa usimbaji fiche usiolinganishwa ni, takribani, ni toleo la dijitali la mchakato huu. Kufuli ni sawa na ufunguo wa umma na ufunguo wa kufuli ni sawa na ufunguo wa kibinafsi. Kwa sababu kufuli ni ya dijitali, hata hivyo, ni rahisi zaidi na si ghali sana kwa Alice kuisambaza kwa mtu yeyote ambaye anaweza kutaka kumtumia ujumbe wa siri.

Kwa uthibitishaji katika mpangilio wa ulinganifu, tunatumia **saini za dijitali**. Hizi, kwa hivyo, zina kazi sawa na misimbo ya uthibitishaji wa ujumbe katika mpangilio wa ulinganifu. Muhtasari wa sahihi za dijitali umetolewa katika *Kielelezo 2*.

Bob kwanza huunda jozi ya funguo, zinazojumuisha ufunguo wa umma ($K_P$) na ufunguo wa faragha ($K_S$), na kusambaza ufunguo wake wa umma. Anapotaka kutuma ujumbe ulioidhinishwa kwa Alice, kwanza huchukua ujumbe wake $M$ na ufunguo wake wa faragha ili kuunda **saini ya dijitali** $D$. Kisha Bob anamtumia Alice ujumbe wake pamoja na sahihi ya dijiti.

Alice anaingiza ujumbe, ufunguo wa umma, na sahihi ya dijiti kwenye **algorithm ya uthibitishaji**. Kanuni hii hutoa **kweli** kwa sahihi sahihi, au **false** kwa sahihi batili.

Sahihi ya dijiti ni, kama jina linavyodokeza, ni sawa na dijiti ya sahihi iliyoandikwa kwenye barua, mikataba, na kadhalika. Kwa kweli, sahihi ya dijiti huwa salama zaidi. Kwa juhudi fulani, unaweza kughushi sahihi iliyoandikwa; mchakato uliorahisishwa na ukweli kwamba sahihi zilizoandikwa mara nyingi hazijathibitishwa kwa karibu. Sahihi salama ya kidijitali, hata hivyo, ni kama msimbo salama wa uthibitishaji wa ujumbe, **haiwezekani kusahaulika**: yaani, ukiwa na mpango salama wa sahihi wa dijiti, hakuna mtu anayeweza kuunda sahihi kwa ujumbe ambao unapitisha utaratibu wa uthibitishaji, isipokuwa kama ana ufunguo wa faragha.

*Kielelezo cha 2: Uthibitishaji wa Asymmetric*

![Figure 2: Asymmetric authentication](assets/Figure6-2.webp "Figure 2: Asymmetric authentication")

Kama ilivyo kwa usimbaji fiche usiolinganishwa, tunaona utofauti wa kuvutia kati ya sahihi dijitali na misimbo ya uthibitishaji wa ujumbe. Kwa hili la mwisho, algoriti ya uthibitishaji inaweza tu kuajiriwa na mmoja wa wahusika walio na mawasiliano salama. Hii ni kwa sababu inahitaji ufunguo wa faragha. Katika mpangilio wa ulinganifu, hata hivyo, mtu yeyote anaweza kuthibitisha sahihi ya dijitali $S$ iliyotengenezwa na Bob.

Haya yote hufanya saini za dijiti kuwa zana yenye nguvu sana. Inaunda msingi, kwa mfano, wa kuunda saini kwenye mikataba ambayo inaweza kuthibitishwa kwa madhumuni ya kisheria. Ikiwa Bob angetia saini kwenye Contract katika Exchange hapo juu, Alice anaweza kuonyesha ujumbe $M$, Contract, na sahihi $S$ kwa mahakama ya sheria. Mahakama ya sheria inaweza, basi, kuthibitisha saini kwa kutumia ufunguo wa umma wa Bob. [5]

Kwa mfano mwingine, saini za dijiti ni kipengele muhimu cha usambazaji salama wa programu na sasisho za programu. Aina hii ya uthibitishaji wa umma haiwezi kamwe kuundwa kwa kutumia misimbo ya uthibitishaji wa ujumbe pekee.

Kama mfano wa mwisho wa nguvu za sahihi za dijiti, zingatia Bitcoin. Mojawapo ya maoni potofu ya kawaida kuhusu Bitcoin, haswa kwenye media, ni kwamba miamala imesimbwa kwa njia fiche: sio. Badala yake, miamala ya Bitcoin hufanya kazi na sahihi za kidijitali ili kuhakikisha usalama.

Bitcoins zipo katika makundi yanayoitwa matokeo ya muamala ambayo hayajatumika (au **UTXO's**). Tuseme unapokea malipo matatu kwenye Bitcoin Address fulani kwa bitcoins 2 kila moja. Kitaalam sasa huna bitcoins 6 kwenye hiyo Address. Badala yake, una bati tatu za bitcoins 2 ambazo zimefungwa na shida ya kriptografia inayohusishwa na hiyo Address. Kwa malipo yoyote utakayofanya, unaweza kutumia bechi moja, mbili au zote tatu, kulingana na kiasi unachohitaji kwa muamala.

Uthibitisho wa Ownership juu ya matokeo ya malipo ambayo hayajatumika huonyeshwa kupitia sahihi moja au zaidi za dijiti. Bitcoin hufanya kazi kwa usahihi kwa sababu sahihi za dijiti kwenye matokeo ya miamala ambayo haijatumika haziwezi kutekelezeka kwa kimahesabu, isipokuwa kama una taarifa za siri zinazohitajika ili kuzitengeneza.

Kwa sasa, miamala ya Bitcoin inajumuisha kwa uwazi maelezo yote ambayo yanahitaji kuthibitishwa na washiriki katika mtandao, kama vile asili ya matokeo ya miamala ambayo hayajatumika yaliyotumika katika muamala. Ingawa inawezekana kuficha baadhi ya taarifa hizo na bado kuruhusu uthibitishaji (kama vile fedha mbadala za siri kama vile Monero hufanya), hii pia husababisha hatari fulani za usalama.

Kuchanganyikiwa wakati mwingine hutokea juu ya sahihi za dijiti na saini zilizoandikwa zilizonaswa kidijitali. Katika hali ya mwisho, unanasa picha ya sahihi yako iliyoandikwa na kuibandika kwenye hati ya kielektroniki kama vile Contract ya ajira. Hii, hata hivyo, si sahihi ya dijitali kwa maana ya kriptografia. Nambari ya mwisho ni nambari ndefu ambayo inaweza kutolewa tu kwa kuwa na ufunguo wa kibinafsi.

Kama ilivyo katika mpangilio wa vitufe vya ulinganifu, unaweza pia kutumia usimbaji fiche usiolinganishwa na mipango ya uthibitishaji kwa pamoja. Kanuni zinazofanana zinatumika. Kwanza kabisa, unapaswa kutumia jozi tofauti za funguo za kibinafsi na za umma kwa usimbaji fiche na kutengeneza saini za kidijitali. Kwa kuongeza, unapaswa kwanza kusimba ujumbe kwa njia fiche na kisha kuuthibitisha.

Muhimu, katika programu nyingi kriptografia isiyolinganishwa haitumiki katika mchakato mzima wa mawasiliano. Badala yake, kwa kawaida itatumika tu kwa *funguo za ulinganifu za Exchange* kati ya wahusika ambao watawasiliana nao.

Hivi ndivyo hali, kwa mfano, unaponunua bidhaa mtandaoni. Kwa kujua ufunguo wa umma wa muuzaji, anaweza kukutumia ujumbe uliotiwa sahihi kidijitali ambao unaweza kuthibitisha kwa uhalisi wake. Kwa msingi huu, unaweza kufuata mojawapo ya itifaki nyingi za kubadilishana vitufe vya ulinganifu ili kuwasiliana kwa usalama.

Sababu kuu ya marudio ya mbinu iliyotajwa hapo juu ni kwamba kriptografia isiyolinganishwa haifai sana kuliko kriptografia linganifu katika kutoa kiwango fulani cha usalama. Hii ni sababu moja kwa nini bado tunahitaji usimbaji wa ufunguo linganifu karibu na usimbaji fiche wa umma. Kwa kuongezea, usimbaji fiche wa vitufe vya ulinganifu ni wa asili zaidi katika programu maalum kama vile mtumiaji wa kompyuta kusimba data yake mwenyewe.

Kwa hivyo saini za dijiti na usimbaji fiche wa ufunguo wa umma Address hufanyaje haswa usambazaji muhimu na shida kuu za usimamizi?

Hakuna jibu moja hapa. Siri ya ulinganifu ni zana na hakuna njia moja ya kuajiri zana hiyo. Lakini acheni tuchukue mfano wetu wa awali kutoka kwa Bidhaa za Michezo za Jim ili kuonyesha jinsi masuala kwa kawaida yangeshughulikiwa katika mfano huu.

Kuanza, Bidhaa za Michezo za Jim huenda zingekaribia **mamlaka ya cheti**, shirika linaloauni usambazaji wa ufunguo wa umma. Mamlaka ya cheti ingesajili baadhi ya maelezo kuhusu Bidhaa za Michezo za Jim na kuipa ufunguo wa umma. Basi, itatuma cheti cha Bidhaa za Michezo za Jim, kinachojulikana kama **cheti cha **TLS/SSL**, huku ufunguo wa umma wa Jim's Sporting ukiwa umetiwa saini kidijitali kwa kutumia ufunguo wa umma wa mamlaka ya cheti. Kwa njia hii, mamlaka ya cheti inathibitisha kwamba ufunguo mahususi wa umma ni mali ya Bidhaa za Michezo za Jim.

Ufunguo wa kuelewa mchakato huu na vyeti vya TLS/SSL ni kwamba, ingawa kwa ujumla hutakuwa na ufunguo wa umma wa Jim's Sporting Goods uliohifadhiwa popote kwenye kompyuta yako, funguo za umma za mamlaka ya cheti zinazotambuliwa kwa hakika zimehifadhiwa katika kivinjari chako au katika mfumo wako wa uendeshaji. Hizi zimehifadhiwa katika kile kinachoitwa **vyeti mizizi**.

Kwa hivyo, Bidhaa za Michezo za Jim zinapokupa cheti chake cha TLS/SSL, unaweza kuthibitisha sahihi ya dijitali ya mamlaka ya cheti kupitia cheti cha mizizi katika kivinjari chako au mfumo wa uendeshaji. Ikiwa sahihi ni halali, unaweza kuwa na uhakika kiasi kwamba ufunguo wa umma kwenye cheti hakika ni wa Bidhaa za Michezo za Jim. Kwa msingi huu, ni rahisi kuweka itifaki ya mawasiliano salama na Bidhaa za Michezo za Jim.

Usambazaji muhimu sasa umekuwa rahisi zaidi kwa Bidhaa za Michezo za Jim. Sio Hard kuona kuwa usimamizi muhimu pia umerahisishwa sana. Badala ya kuhifadhi maelfu ya funguo, Bidhaa za Michezo za Jim zinahitaji tu kuhifadhi ufunguo wa faragha unaoiruhusu kuweka sahihi za ufunguo wa umma kwenye cheti chake cha SSL. Kila wakati mteja anapofika kwenye tovuti ya Jim's Sporting Goods, anaweza kuanzisha kipindi salama cha mawasiliano kutoka kwa ufunguo huu wa umma. Wateja pia hawahitaji kuhifadhi taarifa yoyote (isipokuwa funguo za umma za mamlaka ya cheti zinazotambulika katika mfumo wao wa uendeshaji na kivinjari).

**Maelezo:**

[5] Miradi yoyote inayojaribu kufikia kutokataa, mada nyingine tuliyojadili katika Sura ya 1, kwa msingi wake itahitajika kuhusisha sahihi za kidijitali.

## Kazi za Hash

<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Vitendaji vya Hash vinapatikana kila mahali katika usimbaji fiche. Sio mipango ya ulinganifu au ulinganifu, lakini huanguka katika kategoria ya kriptografia kwa njia yao wenyewe.

Tayari tulikutana na vipengele vya Hash katika Sura ya 4 kwa kuunda ujumbe wa uthibitishaji unaotegemea Hash. Pia ni muhimu katika muktadha wa sahihi za kidijitali, ingawa kwa sababu tofauti kidogo: Sahihi za dijiti kwa kawaida hutengenezwa kwa thamani ya Hash ya baadhi ya ujumbe (uliosimbwa kwa njia fiche), badala ya ujumbe halisi (uliosimbwa). Katika sehemu hii, nitatoa utangulizi wa kina zaidi wa kazi za Hash.

Hebu tuanze na kufafanua kazi ya Hash. ** Chaguo za kukokotoa za Hash** ni chaguo za kukokotoa zinazoweza kutengenezeka kwa ufanisi ambazo huchukua ingizo za ukubwa usiobadilika na kutoa matokeo ya urefu usiobadilika.

**Kitendakazi cha kriptografia cha Hash** ni chaguo za kukokotoa za Hash tu ambacho ni muhimu kwa programu katika usimbaji fiche. Toleo la kitendakazi cha siptografia Hash kwa kawaida huitwa **Hash**, **Hash-thamani**, au **muhtasari wa ujumbe**.

Katika muktadha wa uandishi wa maandishi, "kitendaji cha Hash" kwa kawaida kinarejelea kazi ya kriptografia ya Hash. Nitapitisha mazoezi hayo kuanzia hapa na kuendelea.

Mfano wa kazi maarufu ya Hash ni **SHA-256** (salama Hash algorithm 256). Bila kujali ukubwa wa ingizo (k.m., biti 15, biti 100, au biti 10,000), chaguo hili la kukokotoa litatoa thamani ya 256-bit Hash. Hapo chini unaweza kuona mifano michache ya matokeo ya kazi ya SHA-256.

“Hujambo”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

"Cryptografia inafurahisha": `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Matokeo yote ni biti 256 zilizoandikwa katika umbizo la heksadesimali (kila tarakimu ya heksi inaweza kuwakilishwa na tarakimu nne za binary). Kwa hivyo hata kama ungeingiza kitabu cha Tolkien cha *The Lord of the Rings* kwenye chaguo za kukokotoa za SHA-256, matokeo yangeendelea kuwa biti 256.

Chaguo za kukokotoa za Hash kama vile SHA-256 hutumika katika nyanja mbalimbali katika usimbaji fiche. Ni mali gani zinazohitajika kutoka kwa kazi ya Hash inategemea muktadha wa programu fulani. Kuna sifa mbili kuu zinazohitajika kwa ujumla za vitendaji vya Hash katika kriptografia: [6]

1. Mgongano-upinzani

2. Kujificha

Chaguo za kukokotoa za Hash $H$ inasemekana kuwa **inastahimili mgongano** ikiwa haiwezekani kupata thamani mbili, $x$ na $y$, kama vile $x \neq y$, bado $H(x) = H(y)$.

Vitendaji vya Hash vinavyostahimili mgongano ni muhimu, kwa mfano, katika uthibitishaji wa programu. Tuseme ungependa kupakua toleo la Windows la Bitcoin Core 0.21.0 (programu ya seva ya usindikaji wa trafiki ya mtandao wa Bitcoin). Hatua kuu unazopaswa kuchukua, ili kuthibitisha uhalali wa programu, ni kama ifuatavyo.

1. Kwanza unahitaji kupakua na kuleta funguo za umma za mchangiaji mmoja au zaidi Bitcoin Core kwenye programu ambayo inaweza kuthibitisha sahihi za kidijitali (k.m. Kleopetra). Unaweza kupata funguo hizi za umma [hapa](https://github.com/Bitcoin/Bitcoin/blob/master/contrib/builder-keys/keys.txt). Inapendekezwa kwamba uthibitishe programu ya Bitcoin Core kwa kutumia vitufe vya umma kutoka kwa wachangiaji wengi.

2. Kisha, unahitaji kuthibitisha funguo za umma ulizoingiza. Angalau hatua moja unayopaswa kuchukua ni kuthibitisha kuwa funguo za umma ulizopata ni sawa na zilizochapishwa katika maeneo mengine mbalimbali. Unaweza, kwa mfano, kushauriana na kurasa za kibinafsi za wavuti, kurasa za Twitter, au kurasa za Github za watu ambao funguo zao za umma ulileta. Kwa kawaida ulinganisho huu wa funguo za umma hufanywa kwa kulinganisha Hash fupi ya ufunguo wa umma unaojulikana kama alama ya vidole.

3. Kisha, unahitaji kupakua inayoweza kutekelezwa kwa Bitcoin Core kutoka [tovuti] yao (www.bitcoincore.org). Kutakuwa na vifurushi vinavyopatikana vya Linux, Windows, na mifumo ya uendeshaji ya MAC.

4. Kisha, unapaswa kutafuta faili mbili za kutolewa. Ya kwanza ina SHA-256 Hash rasmi ya kitekelezo ulichopakua pamoja na heshi juu ya vifurushi vingine vyote vilivyotolewa. Faili nyingine ya toleo itakuwa na sahihi kutoka kwa wachangiaji mbalimbali juu ya faili ya kutolewa yenye heshi za kifurushi. Faili hizi zote mbili za kutolewa zinapaswa kupatikana kwenye tovuti ya Bitcoin Core.

5. Kisha, utahitaji kukokotoa SHA-256 Hash ya kitekelezo ulichopakua kutoka kwa tovuti ya Bitcoin Core kwenye kompyuta yako mwenyewe. Wewe, basi, linganisha matokeo haya na yale ya kifurushi rasmi cha Hash kwa inayoweza kutekelezwa. Wanapaswa kuwa sawa.

6. Hatimaye, itabidi uthibitishe kuwa sahihi moja au zaidi za kidijitali kwenye faili ya toleo na heshi rasmi za kifurushi zinalingana na funguo moja au zaidi za umma ulizoingiza (matoleo ya Bitcoin Core si mara zote yametiwa saini na kila mtu). Unaweza kufanya hivyo na programu kama vile Kleopetra.

Mchakato huu wa uthibitishaji wa programu una faida mbili kuu. Kwanza, inahakikisha kwamba hakukuwa na makosa katika uwasilishaji wakati wa kupakua kutoka kwa tovuti ya Bitcoin Core. Pili, inahakikisha kwamba hakuna mvamizi ambaye angeweza kukufanya upakue msimbo uliorekebishwa, hasidi, ama kwa kudukua tovuti ya Bitcoin Core au kwa kuzuia trafiki.

Je, mchakato wa uthibitishaji wa programu hapo juu unalinda vipi dhidi ya masuala haya?

Iwapo ulithibitisha kwa bidii funguo za umma ulizoingiza, basi unaweza kuwa na uhakika kabisa kwamba funguo hizi ni zao na hazijaingiliwa. Kwa kuzingatia kwamba sahihi za kidijitali hazina uwezo wa kusahaulika, unajua kwamba ni wachangiaji hawa pekee wangeweza kuweka sahihi ya dijiti kupitia heshi rasmi za kifurushi kwenye faili ya toleo.

Tuseme saini kwenye faili ya toleo uliyopakua angalia. Sasa unaweza kulinganisha thamani ya Hash uliyokokotoa ndani ya nchi kwa Windows inayoweza kutekelezeka uliyopakua na ile iliyojumuishwa kwenye faili ya toleo iliyotiwa saini ipasavyo. Kama unavyojua chaguo la kukokotoa la SHA-256 Hash haliwezi kustahimili msururu wa tani, ulinganishaji unamaanisha kuwa utekelezaji wako ni sawa kabisa na utekelezo rasmi.

Hebu sasa tugeuke kwenye mali ya pili ya kawaida ya kazi za Hash: ** kujificha **. Chaguo lolote la kukokotoa la Hash $H$ linasemekana kuwa na sifa ya kufichwa ikiwa, kwa $x$ yoyote iliyochaguliwa nasibu kutoka kwa safu kubwa sana, haiwezekani kupata $x$ ukipewa $H(x)$ pekee.

Hapo chini, unaweza kuona matokeo ya SHA-256 ya ujumbe nilioandika. Ili kuhakikisha unasibu wa kutosha, ujumbe ulijumuisha mfuatano wa wahusika uliozalishwa bila mpangilio mwishoni. Ikizingatiwa kuwa SHA-256 ina mali ya kuficha, hakuna mtu ambaye angeweza kufafanua ujumbe huu.


- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Lakini sitakuacha ukiwa na mashaka hadi SHA-256 iwe dhaifu. Ujumbe wa asili nilioandika ulikuwa kama ifuatavyo:


- "Huu ni ujumbe wa nasibu sana, au aina fulani ya nasibu. Sehemu hii ya mwanzo sivyo, lakini nitamalizia na baadhi ya wahusika nasibu ili kuhakikisha ujumbe usiotabirika sana. XLWz4dVG3BxUWm7zQ9qS".

Njia ya kawaida ambayo utendakazi wa Hash na sifa ya kuficha hutumiwa ni katika usimamizi wa nenosiri (upinzani wa mgongano pia ni muhimu kwa programu hii). Huduma yoyote nzuri ya mtandaoni inayotegemea akaunti kama vile Facebook au Google haitahifadhi manenosiri yako moja kwa moja ili kudhibiti ufikiaji wa akaunti yako. Badala yake, watahifadhi tu Hash ya nenosiri hilo. Kila wakati unapojaza nenosiri lako kwenye kivinjari, Hash huhesabiwa kwanza. Hash pekee ndiyo inatumwa kwa seva ya mtoa huduma na ikilinganishwa na Hash iliyohifadhiwa kwenye hifadhidata ya nyuma. Sifa iliyofichwa inaweza kusaidia kuhakikisha kuwa wavamizi hawawezi kuirejesha kutoka kwa thamani ya Hash.

Udhibiti wa nenosiri kupitia heshi, bila shaka, hufanya kazi tu ikiwa watumiaji watachagua manenosiri magumu. Sifa ya kuficha huchukulia kuwa x huchaguliwa nasibu kutoka kwa safu kubwa sana. Kuchagua manenosiri kama vile "1234", "mypassword", au tarehe yako ya kuzaliwa hakutatoa usalama wowote wa kweli. Orodha ndefu za manenosiri ya kawaida na heshi zao zipo ambazo washambulizi wanaweza kutumia ikiwa watapata Hash ya nenosiri lako. Aina hizi za mashambulizi hujulikana kama **mashambulizi ya kamusi**. Iwapo washambuliaji wanajua baadhi ya maelezo yako ya kibinafsi, wanaweza pia kujaribu kukisia kwa ufahamu. Kwa hivyo, daima unahitaji manenosiri marefu, salama (ikiwezekana mifuatano mirefu, isiyo na mpangilio kutoka kwa kidhibiti nenosiri).

Wakati mwingine programu inaweza kuhitaji chaguo za kukokotoa za Hash ambazo zina ukinzani wa mgongano na kujificha. Lakini hakika si mara zote. Mchakato wa uthibitishaji wa programu tuliojadili, kwa mfano, unahitaji tu kwamba kazi ya Hash ionyeshe upinzani wa mgongano, kujificha sio muhimu.

Ingawa upinzani wa mgongano na kujificha ni sifa kuu zinazotafutwa za vitendaji vya Hash katika usimbaji fiche, katika programu fulani aina nyingine za sifa zinaweza pia kuhitajika.

**Maelezo:**

[6] Istilahi ya "kujificha" si lugha ya kawaida, lakini imechukuliwa hasa kutoka kwa Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, na Steven Goldfeder, *Bitcoin na Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Sura ya 1.

# Mfumo wa siri wa RSA

<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Tatizo la uainishaji

<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Ingawa usimbaji fiche linganifu kwa kawaida huwa angavu kwa watu wengi, kwa kawaida sivyo ilivyo kwa usimbaji fiche usiolinganishwa. Ingawa una uwezekano wa kustareheshwa na maelezo ya kiwango cha juu yanayotolewa katika sehemu zilizopita, pengine unashangaa ni nini hasa utendaji wa njia moja na jinsi hasa hutumika kuunda miundo linganifu.

Katika sura hii, nitaondoa baadhi ya fumbo linalozunguka kriptografia isiyolinganishwa, kwa kuangalia kwa undani zaidi mfano maalum, ambao ni mfumo wa siri wa RSA. Katika sehemu ya kwanza, nitaanzisha tatizo la factorization ambalo tatizo la RSA linategemea. Katika mapenzi, basi, funika idadi ya matokeo muhimu kutoka kwa nadharia ya nambari. Katika sehemu ya mwisho, tutaweka maelezo haya pamoja ili kueleza tatizo la RSA, na jinsi hii inaweza kutumika kuunda mifumo ya kriptografia isiyolinganishwa.

Kuongeza kina hiki kwenye mjadala wetu sio kazi rahisi. Inahitaji kutambulisha nadharia na mapendekezo kadhaa ya nadharia ya nambari. Lakini usiruhusu hisabati ikukatishe tamaa. Kushughulikia mjadala huu kutaboresha kwa kiasi kikubwa uelewa wako wa ni nini msingi wa kriptografia isiyolinganishwa na ni uwekezaji unaofaa.

Wacha sasa tugeukie kwanza shida ya uainishaji.

___

Wakati wowote unapozidisha nambari mbili, sema $a$ na $b$, tunarejelea nambari $a$ na $b$ kama **vigezo**, na matokeo kama **bidhaa**. Kujaribu kuandika nambari $N$ katika kuzidisha vipengele viwili au zaidi kunaitwa **factorization** au **factoring**. [1] Unaweza kuita tatizo lolote linalohitaji hili kuwa **tatizo la uanzishaji**.

Takriban miaka 2,500 iliyopita, mwanahisabati wa Uigiriki Euclid wa Alexandria aligundua nadharia kuu kuhusu uainishaji wa nambari kamili. Inajulikana kama **nadharia ya kipekee ya uanzishaji ** na inasema yafuatayo:

**Nadharia 1**. Kila nambari kamili $N$ ambayo ni kubwa kuliko 1 inaweza kuwa nambari kuu, au inaweza kuonyeshwa kama bidhaa ya sababu kuu.

Sehemu yote ya mwisho ya kauli hii inamaanisha ni kwamba unaweza kuchukua nambari yoyote isiyo ya kawaida $N$ kubwa kuliko 1, na kuiandika kama kuzidisha nambari kuu. Ifuatayo ni mifano kadhaa ya nambari kamili zisizo za msingi zilizoandikwa kama bidhaa ya sababu kuu.


- $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
- $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
- $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Kwa nambari zote tatu zilizo hapo juu, kuhesabu vipengele vyake kuu ni rahisi kiasi, hata kama umepewa $N$ pekee. Unaanza na nambari kuu ndogo zaidi, yaani 2, na uone ni mara ngapi nambari kamili $N$ inaweza kugawanywa nayo. Kisha unaendelea na kujaribu mgawanyiko wa $N$ kwa 3, 5, 7, na kadhalika. Utaendelea na mchakato huu hadi nambari yako kamili $N$ iandikwe kama bidhaa ya nambari kuu pekee.

Chukua, kwa mfano, nambari kamili 84. Hapo chini unaweza kuona mchakato wa kuamua sababu zake kuu. Katika kila hatua, tunachukua kipengele kikuu kidogo kilichosalia (upande wa kushoto) na kubainisha muda uliosalia wa kuhesabiwa. Tunaendelea hadi muda uliosalia pia ni nambari kuu. Katika kila hatua, uboreshaji wa sasa wa 84 unaonyeshwa upande wa kulia kabisa.


- Jambo kuu = 2: muda uliobaki = 42 ($84 = 2 \cdot 42$)
- Jambo kuu = 2: muda uliobaki = 21 ($84 = 2 \cdot 2 \cdot 21$)
- Jambo kuu = 3: muda uliobaki = 7 ($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
- Kwa vile 7 ni nambari kuu, matokeo yake ni $2 \cdot 2 \cdot 3 \cdot 7$, au $2^2 \cdot 3 \cdot 7$.

Tuseme sasa hiyo $N$ ni kubwa sana. Je, itakuwa vigumu kiasi gani kupunguza $N$ katika vipengele vyake kuu?

Hiyo inategemea $N$. Tuseme, kwa mfano, hiyo $N$ ni 50,450,400. Ingawa nambari hii inaonekana ya kutisha, hesabu sio ngumu sana na inaweza kufanywa kwa mkono kwa urahisi. Kama hapo juu, unaanza tu na 2 na fanya njia yako kuendelea. Chini, unaweza kuona matokeo ya mchakato huu kwa njia sawa na hapo juu.


- 2: 25,225,200 ($50,450,400 = 2 \cdot 25,225,200$)
- 2: 12,612,600 ($50,450,400 = 2^2 \cdot 12,612,600$)
- 2: 6,306,300 ($50,450,400 = 2^3 \cdot 6,306,300$)
- 2: 3,153,150 ($50,450,400 = 2^4 \cdot 3,153,150$)
- 2: 1,576,575 ($50,450,400 = 2^5 \cdot 1,576,575$)
- 3: 525,525 ($50,450,400 = 2^5 \cdot 3 \cdot 525,525$)
- 3: 175,175 ($50,450,400 = 2^5 \cdot 3^2 \cdot 175,175$)
- 5: 35,035 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35,035$)
- 5: 7,007 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7,007$)
- 7: 1,001 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1,001$)
- 7: 143 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
- 11: 13 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
- Kwa vile 13 ni nambari kuu, matokeo yake ni $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Kutatua tatizo hili kwa mkono huchukua muda. Kompyuta, bila shaka, inaweza kufanya haya yote kwa sehemu ndogo ya sekunde. Kwa kweli, kompyuta inaweza mara kwa mara hata kuweka nambari kamili kubwa katika sehemu ya sekunde.

Kuna, hata hivyo, tofauti fulani. Tuseme kwamba kwanza tunachagua nambari kuu mbili kubwa sana. Ni kawaida kuweka lebo hizi $p$ na $q$, na nitapitisha mkataba huo hapa.

Kwa uthabiti, wacha tuseme $p$ na $q$ zote ni primes 1024-bit, na kwamba zinahitaji angalau biti 1024 ili kuwakilishwa (kwa hivyo biti ya kwanza lazima iwe 1). Kwa hivyo, kwa mfano, 37 haiwezi kuwa moja ya nambari kuu. Kwa hakika unaweza kuwakilisha 37 na bits 1024. Lakini kwa uwazi *huhitaji* hizi biti nyingi kuiwakilisha. Unaweza kuwakilisha 37 kwa mfuatano wowote ambao una biti 6 au zaidi. (Katika biti 6, 37 itawakilishwa kama $100101$).

Ni muhimu kufahamu jinsi $p$ na $q$ ni kubwa ikiwa imechaguliwa chini ya masharti yaliyo hapo juu. Kama mfano, nimechagua nambari kuu ya nasibu ambayo inahitaji angalau biti 1024 kwa uwakilishi hapa chini.


- 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,9352,16. ,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624 9,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836807 558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,69

Tuseme sasa baada ya kuchagua kwa nasibu nambari kuu $p$ na $q$, tutazizidisha ili kupata nambari kamili $N$. Nambari kamili ya mwisho, kwa hivyo, ni nambari ya biti 2048 ambayo inahitaji angalau biti 2048 kwa uwakilishi wake. Ni nyingi, kubwa zaidi kuliko $p$ au $q$.

Tuseme utaipa kompyuta $N$ pekee, na uitake itafute vipengele viwili kuu vya 1024 bit $N$. Uwezekano kwamba kompyuta itagundua $p$ na $q$ ni mdogo sana. Unaweza kusema kuwa haiwezekani kwa madhumuni yote ya vitendo. Hii ni hivyo, hata kama ungeajiri kompyuta kuu au hata mtandao wa kompyuta kuu.

Kuanza, tuseme kwamba kompyuta inajaribu kutatua tatizo kwa kuendesha baisikeli kupitia nambari 1024-bit, ikijaribu katika kila kisa kama ni kuu na ikiwa ni sababu za $N$. Seti ya nambari kuu zitakazojaribiwa basi ni takriban $1.265 \cdot 10^{305}$. [2]

Hata ukichukua kompyuta zote kwenye sayari na kuzifanya zijaribu kutafuta na kujaribu nambari kuu za 1024-bit kwa njia hii, nafasi 1 kati ya bilioni moja ya kupata kipengee kikuu cha $N$ inaweza kuhitaji muda wa kuhesabu muda mrefu zaidi kuliko umri wa Ulimwengu.

Sasa katika mazoezi kompyuta inaweza kufanya vizuri zaidi kuliko utaratibu mbaya ulioelezwa hapo juu. Kuna algoriti kadhaa ambazo kompyuta inaweza kutumia ili kuainishwa haraka zaidi. Hoja, hata hivyo, ni kwamba hata kwa kutumia algorithms hizi bora zaidi, kazi ya kompyuta bado haiwezi kutekelezeka. [3]

Muhimu zaidi, ugumu wa uainishaji chini ya masharti yaliyoelezwa hapo juu unategemea dhana kwamba hakuna algoriti zinazofaa kwa kukokotoa mambo makuu. Kwa kweli hatuwezi kuthibitisha kwamba kanuni bora haipo. Hata hivyo, dhana hii inakubalika sana: licha ya juhudi kubwa zilizochukua mamia ya miaka, bado hatujapata algoriti yenye ufanisi wa kimahesabu.

Kwa hivyo, shida ya uanzishaji, chini ya hali fulani, inaweza kudhaniwa kuwa shida ya Hard. Hasa, wakati $p$ na $q$ ni nambari kuu kubwa sana, bidhaa zao $N$ si vigumu kuhesabu; lakini uainishaji uliopewa tu $N$ hauwezekani.

**Maelezo:**

[1] Factorization inaweza pia kuwa muhimu kwa kufanya kazi na aina zingine za vitu vya hisabati kuliko nambari. Kwa mfano, inaweza kuwa muhimu kuangazia misemo ya aina nyingi kama vile $x^2 - 2x + 1$. Katika mjadala wetu, tutazingatia tu uainishaji wa nambari, haswa nambari kamili.

[2] Kulingana na **nadharia ya nambari kuu**, idadi ya primes chini ya au sawa na $N$ ni takriban $N/\LN(N)$. Hii inamaanisha kuwa unaweza kukadiria idadi ya primes za urefu wa bits 1024 kwa:

$$ \frac{2^{1024}}{\LN(2^{1024})} - \frac{2^{1023}}{\LN(2^{1023})} $$

...ambayo ni sawa na takriban $1.265 \mara 10^{305}$.

[3] Vile vile ni kweli kwa matatizo tofauti ya logarithm. Kwa hivyo, kwa nini ujenzi wa asymmetric hufanya kazi na funguo kubwa zaidi kuliko miundo ya kriptografia linganifu.

## Idadi ya matokeo ya kinadharia

<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Kwa bahati mbaya, tatizo la uainishaji haliwezi kutumika moja kwa moja kwa mifumo ya kriptografia isiyolinganishwa. Hata hivyo, tunaweza kutumia tatizo ngumu zaidi lakini linalohusiana na athari hii: tatizo la RSA.

Ili kuelewa tatizo la RSA, tutahitaji kuelewa idadi ya nadharia na mapendekezo kutoka kwa nadharia ya nambari. Haya yamewasilishwa katika sehemu hii katika vifungu vitatu: (1) mpangilio wa N, (2) modulo isiyobadilika ya N, na (3) nadharia ya Euler.

Baadhi ya nyenzo katika vifungu hivyo vitatu tayari vimewasilishwa katika *Sura ya 3*. Lakini nitaelezea tena nyenzo hiyo kwa urahisi.

### Amri ya N

Nambari kamili $a$ ni **coprime** au **mkuu jamaa** yenye nambari kamili $N$, ikiwa kigawanyo kikuu cha kawaida kati yao ni 1. Ingawa 1 ni kwa makubaliano si nambari kuu, ni nakala ya kila nambari kamili (kama $-1$).

Kwa mfano, fikiria kesi wakati $a = 18$ na $N = 37$. Haya ni madhambi waziwazi. Nambari kamili kubwa zaidi inayogawanyika katika 18 na 37 ni 1. Kwa kulinganisha, zingatia kesi wakati $a = 42$ na $N = 16$. Hizi ni wazi sio coprimes. Nambari zote mbili zinagawanywa na 2, ambayo ni kubwa kuliko 1.

Sasa tunaweza kufafanua mpangilio wa $N$ kama ifuatavyo. Tuseme $N$ ni nambari kamili zaidi ya 1. **mpango wa N** basi, ni nambari ya nakala zote zilizo na $N$ hivi kwamba kwa kila $a$, masharti yafuatayo yanashikilia: $1 \leq a < N$.

Kwa mfano, ikiwa $N = 12$, basi 1, 5, 7, na 11 ndizo malipo pekee ambayo yanakidhi mahitaji yaliyo hapo juu. Kwa hivyo, mpangilio wa 12 ni sawa na 4.

Tuseme kwamba $N$ ni nambari kuu. Kisha nambari yoyote ndogo kuliko $N$ lakini kubwa au sawa na 1 ni coprime nayo. Hii inajumuisha Elements zote katika seti ifuatayo: $\{1,2,3,....,N - 1\}$. Kwa hivyo, wakati $N$ ni ya kwanza, mpangilio wa $N$ ni $N - 1$. Hii imeelezwa katika pendekezo la 1, ambapo $\phi(N)$ inaashiria mpangilio wa $N$.

**Pendekezo 1**. $\phi(N) = N - 1$ wakati $N$ ni ya kwanza

Tuseme hiyo $N$ si ya msingi. Unaweza, basi, kuhesabu mpangilio wake kwa kutumia **Kitendakazi cha Phi cha Euler**. Ingawa kukokotoa mpangilio wa nambari kamili ni moja kwa moja, utendaji wa Euler wa Phi huwa muhimu haswa kwa nambari kubwa zaidi. Pendekezo la kazi ya Phi ya Euler imeelezwa hapa chini.

**Nadharia 2**. Acha $N$ iwe sawa na $p_1^{e_1} \cdot p_2^{e_2} \cdot \lddots \cdot p_i^{e_i} \cdot \lddots \cdot p_n^{e_n}$, ambapo seti $\{p_i\}$ hujumuisha mara ngapi sababu kuu na sababu kuu za $e N$ kila moja. $p_i$ hutokea kwa $N$. Kisha,

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldets \cdot p_n^{e_n - 1} \cdot (p_$n - 1)$

**Nadharia ya 2** inaonyesha kuwa ukishagawanya $N$ yoyote isiyo ya msingi katika vipengele vyake kuu mahususi, ni rahisi kukokotoa mpangilio wa $N$.

Kwa mfano, tuseme $N = 270$. Hii ni wazi sio nambari kuu. Kutenganisha $N$ katika vipengele vyake kuu kunatoa usemi: $2 \cdot 3^3 \cdot 5$. Kulingana na kazi ya Euler's Phi, mpangilio wa $N$ basi ni kama ifuatavyo:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdoti (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 2 +$ 4 = $ 4 = 4 = $ 1

Tuseme kinachofuata kuwa $N$ ni bidhaa ya matoleo mawili ya awali, $p$ na $q$. **Nadharia ya 2** hapo juu, basi, inasema kwamba mpangilio wa $N$ ni kama ifuatavyo:

$$p^{1 - 1} \cdoti (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

Hili ni tokeo kuu la tatizo la RSA hasa, na limeelezwa katika **Pendekezo la 2** hapa chini.

**Pendekezo la 2**. Ikiwa $N$ ni bidhaa ya matoleo mawili ya awali, $p$ na $q$, mpangilio wa $N$ ni bidhaa $(p - 1) \cdot (q - 1)$.

Kwa mfano, tuseme $N = 119$. Nambari hii kamili inaweza kujumuishwa katika nambari kuu mbili, ambazo ni 7 na 17. Kwa hivyo, utendakazi wa Euler wa Phi unapendekeza kwamba mpangilio wa 119 ni kama ifuatavyo:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

Kwa maneno mengine, nambari kamili 119 ina coprime 96 katika safu kutoka 1 hadi 119. Kwa kweli, seti hii inajumuisha nambari zote kuanzia 1 hadi 119, ambazo si zidishi za 7 au 17.

Kuanzia hapa na kuendelea, hebu tuashiria seti ya coprimes ambayo huamua mpangilio wa $N$ kama $C_N$. Kwa mfano wetu ambapo $N = 119$, seti $C_{119}$ ni kubwa mno kuorodheshwa kabisa. Lakini baadhi ya Elements ni kama ifuatavyo:

$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Moduli ya invertibility N

Tunaweza kusema kwamba nambari kamili $a$ ni **modulo inayoweza kubadilika N**, ikiwa kuna angalau nambari moja kamili $b$ kiasi kwamba $a \cdot b \mod N = 1 \mod N$. Nambari kamili kama hiyo $b$ inarejelewa kama **inverse** (au **kinyume kizidishi**) cha $a$ kutokana na kupunguzwa kwa modulo $N$.

Tuseme, kwa mfano, kwamba $a = 5$ na $N = 11$. Kuna nambari nyingi ambazo unaweza kuzidisha 5, ili $5 \cdot b \mod 11 = 1 \mod 11$. Fikiria, kwa mfano, nambari kamili 20 na 31. Ni rahisi kuona kwamba nambari zote mbili kamili ni kinyume cha 5 kwa modulo ya 11 ya kupunguza.


- $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
- $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Ingawa 5 ina inverses nyingi za kupunguza modulo 11, unaweza kuonyesha kwamba ni kinyume kimoja tu chanya cha 5 kilichopo ambacho ni chini ya 11. Kwa kweli, hii si ya kipekee kwa mfano wetu mahususi, lakini matokeo ya jumla.

**Pendekezo la 3**. Ikiwa nambari kamili $a$ inaweza kugeuzwa modulo $N$, lazima iwe hivyo kwamba kinyume kimoja chanya cha $a$ ni chini ya $N$. (Kwa hivyo, kinyume hiki cha kipekee cha $a$ lazima kitoke kwenye seti $\{1, \dots, N - 1\}$).

Hebu tuashiria kinyume cha kipekee cha $a$ kutoka **Pendekezo 3** kama $a^{-1}$. Kwa kesi wakati $a = 5$ na $N = 11$, unaweza kuona kwamba $a^{-1} = 9$, kutokana na kwamba $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Ona kwamba unaweza pia kupata thamani 9 ya $a^{-1}$ katika mfano wetu kwa kupunguza tu ubadilishaji mwingine wowote wa $a$ kwa modulo 11. Kwa mfano, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Kwa hivyo wakati wowote nambari kamili $a > N$ inabadilika modulo $N$, basi $a \mod N$ lazima pia iwe modulo inayoweza kubadilika $N$.

Si lazima iwe hivyo kwamba kinyume cha $a$ kinapatikana modulo ya kupunguza $N$. Tuseme, kwa mfano, kwamba $a = 2$ na $N = 8$. Hakuna $b$, au $a^{-1}$ yoyote haswa, kiasi kwamba $2 \cdot b \mod 8 = 1 \mod 8$. Hii ni kwa sababu thamani yoyote ya $b$ daima itatoa kizidisho cha 2, kwa hivyo hakuna mgawanyiko wa 8 unaoweza kutoa salio ambalo ni sawa na 1.

Je, tunajuaje kama nambari kamili $a$ ina kinyume cha $N$ fulani? Kama unavyoweza kuwa umeona katika mfano hapo juu, kigawanyo kikuu cha kawaida kati ya 2 na 8 ni cha juu kuliko 1, yaani 2. Na hii ni kielelezo cha matokeo ya jumla yafuatayo:

**Pendekezo la 4**. Tofauti ipo ya nambari kamili $a$ kutokana na kupunguza modulo $N$, na hasa kinyume chanya cha kipekee chini ya $N$, ikiwa tu ikiwa kigawanyiko kikuu cha kawaida kati ya $a$ na $N$ ni 1 (yaani, ikiwa ni nakala).

Kwa kesi wakati $a = 5$ na $N = 11$, tulihitimisha kuwa $a^{-1} = 9$, kutokana na kwamba $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Ni muhimu kutambua kwamba kinyume pia ni kweli. Hiyo ni, wakati $a = 9$ na $N = 11$, ni kesi kwamba $a^{-1} = 5$.

### Nadharia ya Euler

Kabla ya kuhamia tatizo la RSA, tunahitaji kuelewa nadharia moja muhimu zaidi, yaani **nadharia ya Euler**. Inasema yafuatayo:

**Nadharia 3**. Tuseme nambari mbili kamili $a$ na $N$ ni coprimes. Kisha, $a^{\phi(N)} \mod N = 1 \mod N$.

Hii ni matokeo ya kushangaza, lakini yanachanganya kidogo mwanzoni. Hebu tugeukie mfano ili kuielewa.

Tuseme kwamba $a = 5$ na $N = 7$. Kwa kweli hizi ni nakala kama nadharia ya Euler inahitaji. Tunajua kwamba mpangilio wa 7 ni sawa na 6, ikizingatiwa kuwa 7 ni nambari kuu (ona **Pendekezo 1**).

Nadharia ya Euler inasema nini sasa ni kwamba $5^6 \mod 7$ lazima iwe sawa na $1 \mod 7$. Chini ni mahesabu ya kuonyesha kwamba hii ni kweli.


- $5^6 \ mod 7 = 15,625 \ mod 7 = 1 \ mod N$

Nambari kamili ya 7 imegawanywa katika 15,624 jumla ya mara 2,233. Kwa hivyo, salio la kugawanya 16,625 kwa 7 ni 1.

Kisha, kwa kutumia kipengele cha Euler's Phi, **Theorem 2**, unaweza kupata **Pendekezo 5** hapa chini.

**Pendekezo la 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ kwa nambari zozote chanya $a$ na $b$.

Hatutaonyesha kwa nini hii ni kesi. Lakini kumbuka tu kwamba tayari umeona ushahidi wa pendekezo hili kwa ukweli kwamba $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ wakati $p$ na $q$ ni msingi, kama ilivyoelezwa katika **Pendekezo 2**.

Nadharia ya Euler kwa kushirikiana na **Pendekezo la 5** ina maana muhimu. Angalia kinachotokea, kwa mfano, katika maneno hapa chini, ambapo $a$ na $N$ ni coprimes.


- $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
- $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
- $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Kwa hivyo, mchanganyiko wa nadharia ya Euler na **Pendekezo la 5** huturuhusu kukokotoa idadi ya misemo. Kwa ujumla, tunaweza kufupisha maarifa kama katika **Pendekezo la 6**.

**Pendekezo la 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Sasa tunapaswa kuweka kila kitu pamoja katika hatua ngumu ya mwisho.

Kama vile $N$ ilivyo na agizo $\phi(N)$ ambalo linajumuisha Elements ya seti ya $C_N$, tunajua kwamba nambari kamili $\phi(N)$ lazima pia iwe na agizo na seti ya coprimes. Wacha tuweke $\phi(N) = R$. Kisha tunajua kwamba pia kuna thamani ya $\phi(R)$ na seti ya coprimes $C_R$.

Tuseme kwamba sasa tutachagua nambari kamili $e$ kutoka kwa seti $C_R$. Tunajua kutoka **Pendekezo la 3** kwamba nambari hii kamili $e$ ina kinyume kimoja cha kipekee cha kinyume chini ya $R$. Hiyo ni, $e$ ina kinyume kimoja cha kipekee kutoka kwa seti $C_R$. Hebu tuite hii kinyume $d$. Kwa kuzingatia ufafanuzi wa kinyume, hii inamaanisha kuwa $e \cdot d = 1 \mod R$.

Tunaweza kutumia tokeo hili kutoa taarifa kuhusu nambari yetu kamili ya $N$. Hii imefupishwa katika **Pendekezo la 7**.

**Pendekezo la 7**. Tuseme kwamba $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Kisha kwa kipengele chochote $a$ cha seti $C_N$ lazima iwe hivyo $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Sasa tuna matokeo yote ya kinadharia yanayohitajika ili kueleza tatizo la RSA kwa uwazi.

## Mfumo wa siri wa RSA

<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Sasa tuko tayari kueleza tatizo la RSA. Tuseme umeunda seti ya vigeu vinavyojumuisha $p$, $q$, $N$, $\phi(N)$, $e$, $d$, na $y$. Piga seti hii $\Pi$. Imeundwa kama ifuatavyo:

1. generate matoleo mawili ya nasibu $p$ na $q$ ya ukubwa sawa na kukokotoa bidhaa zao $N$.

2. Kokotoa mpangilio wa $N$, $\phi(N)$, kwa bidhaa ifuatayo: $(p - 1) \cdot (q - 1)$.

3. Chagua $e > 2$ kiasi kwamba ni ndogo zaidi na inalingana na $\phi(N)$.

4. Kokotoa $d$ kwa kuweka $e \cdot d \mod \phi(N) = 1$.

5. Chagua thamani ya nasibu $y$ ambayo ni ndogo na ya thamani hadi $N$.

Tatizo la RSA linajumuisha kupata $x$ kama vile $x^e = y$, huku ikipewa tu sehemu ndogo ya habari kuhusu $\Pi$, yaani vigeuzo $N$, $e$, na $y$. Wakati $p$ na $q$ ni kubwa sana, kwa kawaida inashauriwa kuwa na ukubwa wa biti 1024, tatizo la RSA linafikiriwa kuwa Hard. Unaweza kuona sasa kwa nini hii ni kesi kutokana na mjadala hapo juu.

Njia rahisi ya kukokotoa $x$ wakati $x^e \mod N = y \mod N$ ni kwa kukokotoa tu $y^d \mod N$. Tunajua $y^d \mod N = x \mod N$ kwa hesabu zifuatazo:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Shida ni kwamba hatujui thamani $d$, kwani haijatolewa kwenye shida. Kwa hivyo, hatuwezi kukokotoa $y^d \mod N$ moja kwa moja ili kutoa $x \mod N$.

Tunaweza, hata hivyo, kukokotoa $d$ kwa njia isiyo ya moja kwa moja kutoka kwa mpangilio wa $N$, $\phi(N)$, kama tunavyojua $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Lakini kwa kudhani shida haitoi dhamana ya $\phi(N)$ pia.

Hatimaye, agizo linaweza kuhesabiwa kwa njia isiyo ya moja kwa moja kwa kutumia vipengele vikuu $p$ na $q$, ili hatimaye tuweze kukokotoa $d$. Lakini kwa kudhaniwa, thamani $p$ na $q$ pia hazijatolewa kwetu.

Kusema kweli, hata kama tatizo la uainishaji ndani ya tatizo la RSA ni Hard, hatuwezi kuthibitisha kwamba tatizo la RSA pia ni Hard. Kunaweza kuwa na njia zingine za kutatua shida ya RSA kuliko kupitia uainishaji. Walakini, inakubaliwa kwa ujumla na kudhaniwa kuwa ikiwa shida ya uainishaji ndani ya shida ya RSA ni Hard, kwamba shida ya RSA yenyewe pia ni Hard.

Ikiwa tatizo la RSA ni kweli Hard, basi hutoa kazi ya njia moja na trapdoor. Chaguo za kukokotoa hapa ni $f(g) = g^e \mod N$. Kwa ujuzi wa $f(g)$, mtu yeyote angeweza kukokotoa thamani $y$ kwa $g = x$ fulani. Walakini, haiwezekani kukokotoa thamani fulani $x$ kutokana tu na kujua thamani $y$ na chaguo za kukokotoa $f(g)$. Isipokuwa ni wakati unapewa kipande cha habari $d$, mlango wa trap. Katika hali hiyo, unaweza kuhesabu tu $y^d$ kutoa $x$.

Wacha tupitie mfano maalum ili kuelezea shida ya RSA. Siwezi kuchagua tatizo la RSA ambalo linaweza kuzingatiwa kuwa Hard chini ya masharti yaliyo hapo juu, kwani nambari zitakuwa ngumu. Badala yake, mfano huu ni wa kuonyesha jinsi tatizo la RSA kwa ujumla linavyofanya kazi.

Kuanza, tuseme umechagua nambari kuu mbili za nasibu 13 na 31. Kwa hivyo $p = 13$ na $q = 31$. Bidhaa $N$ ya primes hizi mbili ni sawa na 403. Tunaweza kuhesabu kwa urahisi utaratibu wa 403. Ni sawa na $ (13 - 1) \cdot (31 - 1) = 360 $.

Ifuatayo, kama inavyoelekezwa na hatua ya 3 ya tatizo la RSA, tunahitaji kuchagua coprime kwa 360 ambayo ni kubwa kuliko 2 na chini ya 360. Si lazima kuchagua thamani hii nasibu. Tuseme kwamba tutachagua 103. Hiki ni nakala ya 360 kama kigawanyo chake kikuu cha kawaida na 103 ni 1.

Hatua ya 4 sasa inahitaji tuhesabu thamani $d$ kiasi kwamba $103 \cdot d \mod 360 = 1$. Hili si kazi rahisi kwa mkono wakati thamani ya $N$ ni kubwa. Inahitaji kwamba tutumie utaratibu unaoitwa **algorithm iliyopanuliwa ya Euclidean**.

Ingawa sionyeshi utaratibu hapa, inatoa thamani 7 wakati $e = 103$. Unaweza kuthibitisha kwamba jozi ya thamani 103 na 7 inatimiza masharti ya jumla $e \cdot d \mod \phi(n) = 1$ kupitia hesabu zilizo hapa chini.


- $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Muhimu, kutokana na *Pendekezo la 4*, tunajua kwamba hakuna nambari nyingine kamili kati ya 1 na 360 kwa $d$ itatoa matokeo kwamba $103 \cdot d = 1 \mod 360$. Zaidi ya hayo, pendekezo hili linamaanisha kuwa kuchagua thamani tofauti ya $e$, kutatoa thamani tofauti ya kipekee ya $d$.

Katika hatua ya 5 ya tatizo la RSA, inatubidi kuchagua kiasi kamili chanya $y$ ambayo ni coprime ndogo ya 403. Tuseme kwamba tutaweka $y = 2^{103}$. Udhihirisho wa 2 kwa 103 hutoa matokeo hapa chini.


- $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$

Tatizo la RSA katika mfano huu sasa ni kama ifuatavyo: Umepewa $N = 403$, $e = 103$, na $y = 349 \mod 403$. Sasa unapaswa kukokotoa $x$ kiasi kwamba $x^{103} = 349 \mod 403$. Hiyo ni, lazima upate kuwa thamani ya asili kabla ya udhihirisho na 103 ilikuwa 2.

Ingekuwa rahisi (angalau kwa kompyuta) kukokotoa $x$ ikiwa tungejua kwamba $d = 7$. Katika hali hiyo, unaweza tu kuamua $x$ kama ilivyo hapo chini.


- $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$

Shida ni kwamba haujapewa habari ambayo $d = 7$. Unaweza, bila shaka, kuhesabu $d$ kutokana na ukweli kwamba $103 \cdot d = 1 \mod 360$. Shida ni kwamba pia haupewi habari kwamba agizo la $N = 360$. Hatimaye, unaweza pia kukokotoa mpangilio wa 403 kwa kukokotoa bidhaa ifuatayo: $(p - 1) \cdot (q - 1)$. Lakini pia hukuambiwa kuwa $p = 13$ na $q = 31$.

Bila shaka, kompyuta bado inaweza kutatua tatizo la RSA kwa mfano huu kwa urahisi, kwa sababu nambari kuu zinazohusika si kubwa. Lakini wakati primes inakuwa kubwa sana, inakabiliwa na kazi isiyowezekana.

Sasa tumewasilisha tatizo la RSA, seti ya masharti ambayo ni Hard, na hisabati ya msingi. Je, yoyote kati ya haya inasaidia vipi na kriptografia isiyolinganishwa? Hasa, tunawezaje kugeuza ugumu wa tatizo la RSA chini ya hali fulani kuwa mpango wa usimbaji fiche au mpango wa sahihi wa dijitali?

Mbinu mojawapo ni kuchukua tatizo la RSA na kujenga skimu kwa njia iliyonyooka. Kwa mfano, tuseme kwamba umetoa seti ya vijiti $\Pi$ kama ilivyoelezwa kwenye tatizo la RSA, na uhakikishe kuwa $p$ na $q$ ni kubwa vya kutosha. Unaweka ufunguo wako wa umma sawa na $(N, e)$ na kushiriki habari hii na ulimwengu. Kama ilivyoelezwa hapo juu, unaweka thamani za $p$, $q$, $\phi(n)$, na $d$ siri. Kwa kweli, $d$ ni ufunguo wako wa faragha.

Mtu yeyote anayetaka kukutumia ujumbe $m$ ambao ni kipengele cha $C_N$ anaweza kuusimba kwa njia fiche kama ifuatavyo: $c = m^e \mod N$. (Nakala ya siri $c$ hapa ni sawa na thamani $y$ katika tatizo la RSA.) Unaweza kusimbua ujumbe huu kwa urahisi kwa kukokotoa tu $c^d \mod N$.

Unaweza kujaribu kuunda mpango wa sahihi wa dijiti kwa njia ile ile. Tuseme unataka kumtumia mtu ujumbe $m$ na sahihi ya dijitali $S$. Unaweza tu kuweka $S = m^d \mod N$ na kutuma jozi $(m,S)$ kwa mpokeaji. Mtu yeyote anaweza kuthibitisha sahihi ya dijiti kwa kuangalia tu kama $S^e \mod N = m \mod N$. Mshambulizi yeyote, hata hivyo, atakuwa na wakati mgumu sana kuunda $S$ halali kwa ujumbe, ikizingatiwa kuwa hana $d$.

Kwa bahati mbaya, kugeuza kile kilicho peke yake shida ya Hard, shida ya RSA, kuwa mpango wa kriptografia sio moja kwa moja. Kwa mpango wa moja kwa moja wa usimbaji fiche, unaweza kuchagua tu nakala za $N$ kama ujumbe wako. Hiyo haituachi na jumbe nyingi zinazowezekana, hakika haitoshi kwa mawasiliano ya kawaida. Kwa kuongeza, ujumbe huu unapaswa kuchaguliwa kwa nasibu. Hiyo inaonekana kuwa haiwezekani. Hatimaye, ujumbe wowote ambao umechaguliwa mara mbili utatoa maandishi ya siri sawa. Hili halifai sana katika mpango wowote wa usimbaji fiche na halifikii dhana yoyote kali ya kisasa ya usalama katika usimbaji fiche.

Matatizo yanazidi kuwa mabaya zaidi kwa mpango wetu wa moja kwa moja wa sahihi wa kidijitali. Kwa hali ilivyo, mvamizi yeyote anaweza kughushi sahihi za dijitali kwa urahisi kwa kuchagua kwanza thamani ya $N$ kama sahihi na kisha kukokotoa ujumbe halisi unaolingana. Hii inavunja wazi hitaji la kutoweza kusamehewa.

Hata hivyo, kwa kuongeza uchangamano wa werevu, tatizo la RSA linaweza kutumiwa kuunda mpango salama wa usimbaji wa ufunguo wa umma pamoja na mpango salama wa sahihi wa dijitali. Hatutaingia katika maelezo ya ujenzi huo hapa. [4] Muhimu, hata hivyo, utata huu wa ziada haubadilishi tatizo la msingi la RSA ambalo mipango hii imejikita.

**Maelezo:**

[4] Angalia, kwa mfano, Jonathan Katz na Yehuda Lindell, _Utangulizi wa Uandishi wa Kisasa_, CRC Press (Boca Raton, FL: 2015), uk. 410–32 kuhusu usimbaji fiche wa RSA na uk. 444–41 kwa sahihi za kidijitali za RSA.

# Hitimisho

<partId>e538fb79-bf28-40cd-a5c3-badf864d8567</partId>

## Ukaguzi na Ukadiriaji

<chapterId>366d6fd0-ceb2-4299-bf37-8c6dfcb681d5</chapterId>

<isCourseReview>true</isCourseReview>
## Mtihani wa Mwisho

<chapterId>44882d2b-63cd-4fde-8485-f76f14d8b2fe</chapterId>

<isCourseExam>true</isCourseExam>
## Hitimisho

<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>

<isCourseConclusion>true</isCourseConclusion>