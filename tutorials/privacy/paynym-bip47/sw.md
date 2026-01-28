---
name: BIP47 - PayNym
description: Tumia nambari ya malipo inayoweza kutumika tena kwenye Ashigaru
---
![cover](assets/cover.webp)



Hitilafu mbaya zaidi ya faragha unayoweza kufanya kwenye Bitcoin ni kutumia anwani tena. Kila mara anwani ile ile inapopokea malipo kadhaa, miamala hii huunganishwa, na hivyo kuupa ulimwengu ramani ya miamala yako. Kwa hivyo inapendekezwa sana kuwa kila wakati uweke generate anwani ya kipekee kwa kila risiti. Lakini kwa programu zingine za Bitcoin, hii sio jambo rahisi.



BIP47, iliyopendekezwa na Justus Ranvier mwaka 2015, inatoa jibu la kifahari kwa tatizo hili. Inatanguliza dhana ya **msimbo wa malipo unaoweza kutumika tena**: kitambulisho cha kipekee kinachowezesha idadi isiyo na kikomo ya malipo ya onchain bitcoin kupokelewa, bila kutumia anwani tena. Shukrani kwa utaratibu wa kriptografia kulingana na ubadilishanaji wa ECDH (*Diffie-Hellman kwenye mikunjo ya duaradufu*), kila malipo kwa msimbo sawa husababisha anwani tupu, mahususi kwa uhusiano kati ya mtumaji na mpokeaji.



![Image](assets/fr/01.webp)



Kanuni hii ya BIP47 inatekelezwa hasa na **PayNym**, mfumo ulioundwa awali na Samourai Wallet na sasa kuchukuliwa na Ashigaru. Katika somo hili, tutaangalia jinsi ya kuwezesha PayNym yako, kubadilishana misimbo ya malipo na mwandishi na kufanya miamala bila kutumia tena anwani.



Sitaingia katika utendakazi wa kina wa BIP47 hapa. Ikiwa ungependa kuzama zaidi katika somo, tafadhali rejelea sura ya 6.6 ya kozi yangu ya mafunzo ya BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Masharti



Ili kufuata mafunzo haya, unachohitaji ni wallet kwenye programu ya Ashigaru. Ikiwa hujui jinsi ya kupakua, kuthibitisha, kusakinisha programu au kuunda wallet, ninapendekeza upate mafunzo haya kwanza:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Omba PayNym



Hatua ya kwanza ni kudai PayNym yako. Operesheni hii inahitaji kufanywa mara moja kwa kila wallet. Inahusisha msimbo wako wa malipo wa BIP47 unaotokana na seed yako (`PM...`) na kitambulisho cha kipekee mahususi kwa utekelezaji wa PayNym. Kitambulisho hiki kifupi na kinachosomeka zaidi kinaweza kutumwa kwa wanahabari wako ili kuwezesha ubadilishanaji, bila kulazimika kushiriki msimbo mrefu na kamili wa BIP47.



Ili kufanya hivyo, bofya picha yako ya PayNym iliyo juu kushoto mwa kiolesura, kisha kwenye msimbo wako wa malipo `PM...`.



![Image](assets/fr/02.webp)



Kisha ubofye vitone vitatu vidogo kwenye kona ya juu kulia, na uchague `Dai PayNym`.



![Image](assets/fr/03.webp)



Thibitisha kwa kubofya kitufe cha `DAI YAKO PAYNYM`.



![Image](assets/fr/04.webp)



Onyesha upya ukurasa: Kitambulisho chako cha PayNym sasa kinaonyeshwa chini ya picha yako, juu kidogo ya nambari yako ya malipo ya BIP47.



![Image](assets/fr/05.webp)



PayNym yako sasa inatumika na iko tayari kutumika kwa miamala yako ya kwanza ya BIP47.



## Ungana na mwasiliani



Kuna aina mbili za muunganisho kati ya PayNym: **fuata** na **unganisha**. Operesheni ya `kufuata` haina malipo kabisa. Inaanzisha kiungo kati ya PayNym mbili kupitia Soroban, itifaki ya mawasiliano iliyosimbwa kwa msingi wa Tor iliyotengenezwa na timu ya Samourai na kupitishwa na Ashigaru. Kiungo hiki huwezesha watumiaji wawili wanaofuatana kubadilishana taarifa kwa faragha, hasa kuratibu shughuli shirikishi kama vile Stowaway au StonewallX2, ambayo tutaangalia katika mafunzo mengine. Hatua hii ni mahususi kwa PayNym na si sehemu ya itifaki ya BIP47.



![Image](assets/fr/06.webp)



Uendeshaji wa uunganisho (`unganisha`), kwa upande mwingine, unahitaji muamala wa on-chain. Inajumuisha kutekeleza shughuli ya arifa kama inavyofafanuliwa katika BIP47. Muamala huu wa Bitcoin una metadata katika matokeo ya `OP_RETURN`, ambayo huanzisha njia iliyosimbwa kwa njia fiche kati ya mlipaji na mpokeaji. Kutoka kwa kituo hiki, mlipaji ataweza kupata anwani za kipekee za generate za kupokea kwa kila malipo, na mpokeaji ataarifiwa kuhusu malipo haya, na ataweza kuweka generate funguo za faragha zinazohusiana na anwani ili kutumia pesa hizi baadaye.



Muamala huu wa arifa una gharama: ada ya mining na 546 sats iliyotumwa kwa anwani ya arifa ya mpokeaji ili kuashiria muunganisho. Baada ya muunganisho kuanzishwa, karibu idadi isiyo na kikomo ya malipo inaweza kufanywa kupitia BIP47.



Kwa kifupi:




- kufuata": bila malipo, huanzisha mawasiliano yaliyosimbwa kwa njia fiche kupitia Soroban, muhimu kwa zana shirikishi za Ashigaru;
- `Unganisha`: inatozwa, hufanya shughuli ya arifa ya BIP47 ili kuwezesha kituo kati ya mlipaji na mpokeaji.



Ili kutumia PayNym, lazima kwanza *uifuate. Hii ni hatua ya kwanza kabla ya kuanzisha muunganisho wa BIP47. Hebu tuseme unataka kutuma malipo ya mara kwa mara kwa PayNym `+instinctiveoffer10`.



Nenda kwenye ukurasa wako wa PayNym kwenye Ashigaru, kisha ubofye kitufe cha `+` kilicho chini kulia mwa kiolesura.



![Image](assets/fr/07.webp)



Kisha unaweza kubandika msimbo kamili wa malipo wa mpokeaji, au uchanganue msimbo wake wa QR.



![Image](assets/fr/08.webp)



Ikiwa una kitambulisho chake cha PayNym pekee, nenda kwa [Paynym.rs](https://paynym.rs/) ili kupata msimbo wa QR unaohusishwa na msimbo wake wa malipo.



![Image](assets/fr/09.webp)



Baada ya kuchanganua msimbo wa QR, bofya kitufe cha `FUATA` ili kufuata PayNym.



![Image](assets/fr/10.webp)



Kitendo cha `FOLLOW` kinatosha kwa shughuli shirikishi (*cahoots*). Hata hivyo, ili kutuma malipo ya BIP47, unahitaji kuanzisha muunganisho: bofya `CONNECT` ili kutekeleza shughuli ya arifa.



![Image](assets/fr/11.webp)



Muamala wa arifa basi hutangazwa kwenye mtandao. Subiri hadi iwe na angalau uthibitisho mmoja kabla ya kufanya malipo yako ya kwanza.



![Image](assets/fr/12.webp)



## Fanya malipo ya BIP47



Sasa umeunganishwa na mpokeaji na unaweza kutuma malipo kwa anwani ya kipekee, inayozalishwa kiotomatiki kwa kutumia itifaki ya BIP47, bila kubadilishana mapema na mpokeaji.



Kutoka kwa ukurasa wako mkuu wa PayNym, bofya mtu ambaye ungependa kumtumia malipo.



![Image](assets/fr/13.webp)



Katika sehemu ya juu ya kulia ya kiolesura, bofya kwenye ikoni ya mshale.



![Image](assets/fr/14.webp)



Weka kiasi kitakachotumwa. Huna haja ya kuingiza anwani ya kupokea: itatolewa kiotomatiki kwa kutumia itifaki ya BIP47.



![Image](assets/fr/15.webp)



Angalia kwa uangalifu maelezo ya muamala, ikijumuisha ada, kisha uburute mshale wa kijani kibichi chini ya skrini ili kutia sahihi na kutangaza muamala.



![Image](assets/fr/16.webp)



Muamala umetumwa.



![Image](assets/fr/17.webp)



Katika mfano huu, malipo yalifanywa kwa pochi yangu nyingine ya PayNym. Kwa hivyo naweza kuona kwamba imefika kwenye Ashigaru wallet yangu nyingine, bila anwani yoyote kubadilishwa kwa mikono: kitambulisho cha PayNym pekee ndicho kilitumika.



![Image](assets/fr/18.webp)



Sasa unajua jinsi ya kutumia misimbo ya malipo inayoweza kutumika tena ya BIP47 kutokana na utekelezaji wa PayNym kwenye programu ya Ashigaru. Sasa unaweza kushiriki nambari hii ya malipo na mtu yeyote anayetaka kukutumia malipo (hasa malipo ya mara kwa mara). Unaweza pia kuchapisha Kitambulisho chako cha PayNym kwenye tovuti yako au mitandao ya kijamii ili kupokea michango.



Ili kuongeza ujuzi wako wa itifaki hii, kuelewa kwa undani jinsi inavyofanya kazi na athari zake kwa usiri, ninapendekeza sana uchukue kozi yangu ya BTC 204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c