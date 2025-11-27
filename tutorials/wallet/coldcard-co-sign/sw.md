---
name: COLDCARD - Ishara-Mwenza
description: Gundua kipengele cha Co-Sign na ukitumie kwenye COLDCARD yako
---

![cover](assets/cover.webp)


*NB: Mafunzo haya yanalenga watu ambao tayari wana uzoefu wa kutumia pochi zenye saini nyingi, vifaa vya Coinkite na programu kama vile Sparrow wallet au Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Kwa nini ColdCard Co-sign?



Kipengele hiki hukuwezesha kuongeza **masharti ya matumizi** kwenye kifaa chako cha ColdCard (Q au Mk4) kwa njia ya Moduli ya Usalama ya Vifaa (HSM), ili kulinda pesa zako huku ukiendelea kubadilika na kuzidhibiti.



Masharti ya matumizi yanaweza kuwa, kwa mfano:





- Vizuizi kwa ukubwa**: punguza kiwango cha bitcoins unaweza kutumia katika muamala mmoja.
- Vikomo vya kasi:** amua ni shughuli ngapi unaweza kufanya kwa kila kitengo cha muda (kwa saa, siku, wiki, n.k.), inayohitaji idadi ya chini ya vitalu kati yao.
- Anwani zilizoidhinishwa awali:** Ruhusu bitcoins tu kutumwa kwa anwani zilizoidhinishwa awali.
- Uthibitishaji wa vipengele viwili:** Inahitaji uthibitisho kutoka kwa programu ya simu ya mtu mwingine ya 2FA (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) kwenye simu/kompyuta kibao inayotumia NFC yenye ufikiaji wa mtandao.



**Jinsi inavyofanya kazi



Kwa kuongeza seed ya pili kwenye kifaa chako cha ColdCard Mk4 au Q, kinachoitwa "Ufunguo wa Sera ya Matumizi", ambayo tutarejelea katika somo hili lote kama "C Key".


Kando na seed hii ya ziada, utaombwa utumie Supply angalau ufunguo mmoja wa ziada (XPUB), ambao tutauita "Ufunguo wa Hifadhi nakala", ili kuunda Wallet Multisig 2-on-N.



Kwa muhtasari, tutaunda Wallet Multisig, na kifaa chako cha ColdCard kitakuwa na funguo 2 za faragha zinazohitajika ili kutumia pesa, bwana wa kifaa seed na "Ufunguo wa Sera ya Matumizi".



Kila wakati "C Key" inapoombwa kutia sahihi, masharti ya matumizi yaliyobainishwa yatatumika, na ColdCard itasaini tu ikiwa shughuli hiyo itatii.



Ikiwa ungependa kuachana na masharti haya ya matumizi, unaweza kufanya hivyo:




- kwa kutia sahihi na mojawapo ya vitufe vya kuhifadhi nakala na mkono wa seed, au vitufe 2 vya chelezo kulingana na saizi ya Multisig yako.
- kwa kuingiza "Ufunguo wa Sera ya Matumizi" au "Ufunguo C" kwenye menyu ya "Sahihi-Mwili". **Za mwisho haziwezi kushauriwa moja kwa moja kwenye kifaa, vinginevyo mtu yeyote anaweza kughairi masharti ya matumizi yaliyowekwa.**




## Inasanidi Alama Mwenza ya ColdCard



![video](https://youtu.be/MjMPDUWWegw)



### 1- Amilisha utendakazi



Kwanza kabisa, hakikisha kuwa kifaa chako kina angalau toleo la hivi punde la programu dhibiti:




- Mk4: v5.4.2
- S: v1.3.2Q




Kwenye Mk4 au ColdCardQ yako, nenda kwenye *Zana za Kina > Uwekaji Saini Mwenza wa ColdCard*.



![Co-Sign](assets/fr/01.webp)



*Katika mafunzo yafuatayo, picha za skrini zitachukuliwa kwenye ColdCardQ kwa urahisi, lakini hatua na menyu zinafanana kati ya Mk4 na Q.*



Muhtasari wa utendaji unaonyeshwa.


Istilahi inayotumika kuteua funguo, ambazo tutakuwa tukitumia tena katika saini 2-on-3 za Wallet ambazo tunakaribia kuunda, ni:



Kitufe A = Coldcard master seed


Kitufe B = Kitufe cha Hifadhi Nakala


Ufunguo C = Ufunguo wa Sera ya Matumizi



Bonyeza **"INGIA "**.



![Co-Sign](assets/fr/02.webp)



Hatua inayofuata ni kuamua ni ufunguo gani wa faragha utakaofanya kazi kama "Ufunguo wa Sera ya Matumizi" au "Ufunguo C".



Tunaweza kuona kuwa tuna chaguzi kadhaa zilizo wazi kwetu:





- Au bonyeza **"INGIA "** hadi generate sentensi mpya ya seed yenye maneno 12.





- Bofya **"(1) "** ili kuleta seed ya maneno 12 iliyopo, au uchague **"(2) "** ili kuleta seed ya maneno 24 iliyopo.





- Au bonyeza **"(6) "** ili kuleta seed kutoka kwa vault ya kifaa chako.



Kwa madhumuni ya somo hili, tumeamua kuleta seed ya maneno 12 kwa kubofya **"(1) "**. Hii inaweza kuwa seed BIP39 yoyote ambayo tayari unamiliki, na ambayo ni wazi unayo chelezo.



Tumia kibodi yako kuweka maneno 12 ya seed yako. Kwa mfano huu, tutachagua maneno halali ya seed nyama x 12. Kisha ubonyeze **"INGIA "**.


*NB: ikiwa huna nakala rudufu ya seed hii, hutaweza tena kurekebisha mipangilio ya "Co-Sign" kwenye kifaa chako, ili kubadilisha hali yako ya matumizi*



Kipengele cha "Co-Sign" sasa kimewashwa kwenye kifaa. Ifuatayo, tutahitaji kuchagua hali zetu za matumizi, kisha tukamilishe uundaji wa Wallet ya saini nyingi.



![Co-Sign](assets/fr/03.webp)



### 2- Chagua masharti ya matumizi au "*sera za matumizi*"



Hapa tunabainisha masharti ya matumizi ambayo lazima yatimizwe wakati **"Ufunguo C "** au **"Ufunguo wa Sera ya Matumizi**" unatia saini muamala.



Katika **"Menyu ya Kusaini Pamoja "**, bofya **"Sera ya Matumizi**".



Kisha unaweza kuchagua ukubwa wa juu zaidi, yaani, idadi ya juu ya satoshi ambayo inaweza kutumika katika shughuli moja.



Kwa mfano huu, tutachagua upeo wa ukubwa wa **21212** satoshi. Bonyeza **"INGIA "** ili kuthibitisha.




![Co-Sign](assets/fr/04.webp)



Kisha tunachagua kuweka kasi ya juu zaidi, yaani, idadi ya miamala ambayo kifaa kitaweza kutia sahihi kwa kila kitengo cha muda. Kwa mafunzo haya, tutachagua kasi isiyo na kikomo, yaani, hakuna kikomo kwa idadi ya miamala.




![Co-Sign](assets/fr/05.webp)



### 3- Unda Wallet Multisig 2-on-N



Bado tunahitaji kuchagua ufunguo wa tatu wa Wallet Multisig yetu, yaani **"Ufunguo wa Hifadhi nakala"** (Ufunguo B), pamoja na **bwana seed** (Ufunguo A) wa kifaa na **"Ufunguo wa Sera ya Matumizi "** (Ufunguo C).



"B Ufunguo" wetu utalazimika kuingizwa ama kupitia kadi ya SD, au kupitia msimbo wa QR katika kesi ya ColdCardQ.


Ili kufanya hivyo, tutahitaji kifaa cha pili cha ColdCard Mk4 au Q, ambacho "Key B" yetu inatumiwa.



Kwenye kifaa hiki cha pili kilicho na **"Ufunguo wa Hifadhi nakala"**, sema ColdCard Mk4 kwa mfano huu, nenda kutoka kwenye menyu kuu hadi **"Mipangilio "**, kisha, **"Multisig Wallet"**, na hatimaye **"Hamisha Xpub "**.


(Ikiwa kifaa chako cha pili ni ColdCardQ, utakuwa na chaguo la kuhamisha Xpub yako kupitia msimbo wa QR, bila shaka).





![Co-Sign](assets/fr/06.webp)





Kwenye skrini inayofuata, weka kadi ya SD na ubofye kitufe cha **"halalisha "** chini kulia. Kisha bonyeza **"(1) "** ili kuhifadhi faili kwenye kadi ya SD.



Faili itakuwa na alama ya vidole ya ufunguo wa umma (*alama ya vidole*) katika jina lake, na itachukua fomu `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Kisha ingiza kadi ya SD kwenye "awali" ColdCardQ ili kuleta "Ufunguo wetu wa Hifadhi nakala" (ufunguo B).


Katika menyu ya "ColdCard Co-signing", chagua "Jenga 2-of-N", kisha kwenye skrini inayofuata bofya **"INGIA "**, kisha tena **"INGIA "** ili kuleta "Ufunguo wa Hifadhi nakala" kutoka kwa kadi ya SD.



![Co-Sign](assets/fr/08.webp)



Kwenye skrini inayofuata, acha "Nambari ya Akaunti" wazi (isipokuwa unajua unachofanya hasa) na ubofye **"INGIA "** tena.



![Co-Sign](assets/fr/09.webp)



Hatimaye, tuko tayari kutumia Wallet Multisig 2-sur-3 yetu mpya, iliyoundwa kama ifuatavyo:



Ufunguo A= Coldcard Q bwana seed


Ufunguo B= Ufunguo Nakala (ulioingizwa hivi punde kutoka kwa kifaa cha pili cha Coldcard)


Ufunguo C= Ufunguo wa Sera ya Matumizi (ikiwa unatumika kutia saini, huweka masharti ya matumizi yaliyobainishwa)



## Saini pamoja na Sparrow wallet



Ikihitajika, rejelea mafunzo yaliyo hapa chini ili kujifahamisha na programu ya Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Hamisha Wallet Multisig 2-sur-3 hadi Sparrow wallet



Sasa tunahitaji kusafirisha Wallet Multisig yetu hadi Sparrow ili tuweze kuweka satoshi zetu za kwanza huko.



Kutoka kwa menyu kuu ya ColdCardQ yako, chagua **"Mipangilio "**, kisha **"Pochi za Multisig "**.


Seti ya pochi za Multisig zinazojulikana kwa ColdCard yako sasa zinaonyeshwa, na idadi ya vitufe vinavyohusika hapa "2/3" (2-sur3). Chagua Multisig **"Ishara-Mwenza ya ColdCard "** tumeunda hivi punde, kisha ubofye **"Usafirishaji wa ColdCard "**.



![Co-Sign](assets/fr/10.webp)




Hatimaye, chagua njia ambayo itakuruhusu kusafirisha Wallet hadi Sparrow. Kwa upande wetu, tutachagua kadi ya SD, na kwa hivyo bonyeza **"(1) "** baada ya kuingiza kadi ya SD kwenye slot A ya kifaa.



![Co-Sign](assets/fr/11.webp)



Kisha katika Sparrow wallet, chagua "Ingiza Wallet".



![Co-Sign](assets/fr/12.webp)



Kisha bonyeza **"Ingiza Faili "**. Kisha chagua faili **"export-Coldcard_Co-sign.txt "** kwenye kadi yako ya SD.



![Co-Sign](assets/fr/13.webp)



Ipe Wallet yako jina jinsi litakavyoonekana katika Sparrow, na uchague nenosiri la kusimba Wallet yako (au la).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Sasa tuko tayari kupokea satoshi zetu za kwanza na kujaribu masharti ya matumizi ambayo tumetumia kwenye Wallet yetu.



![Co-Sign](assets/fr/16.webp)



### 2- Kujaribu sera za matumizi zilizobainishwa mapema



Kama ukumbusho, tulikuwa tumeamua juu ya ukubwa wa juu wa satoshis 21212 kwa Wallet Multisig yetu. Hii ilimaanisha kwamba kila wakati Ufunguo wa Sera ya Matumizi (Ufunguo C) ulitia sahihi shughuli, ya pili itakuwa halali tu ikiwa kiasi kilichotumiwa kilikuwa chini ya au sawa na satoshis 21212.



Hebu tujaribu.


Kwanza, hebu tubofye kichupo cha "Pokea" katika Sparrow na tudondoshe Satss chache kwenye Wallet, ambayo tutatumia katika mafunzo haya yote.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Kisha hebu tujaribu kutumia zaidi ya 21212 kuruhusiwa satoshi kwa kuiga shughuli ya 50,000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Baada ya kuchanganua msimbo wa QR unaowakilisha *muamala ambao haujasainiwa* na ColdCardQ yetu ili kuleta muamala, haya ndiyo tunayoonyeshwa kwenye skrini. Ujumbe wa onyo unatuambia kuwa masharti ya matumizi hayajafikiwa. Ikiwa tutatia saini shughuli hiyo, basi moja tu ya funguo 2 (bwana seed kwenye kifaa, lakini sio "Ufunguo C") itasaini.




![Co-Sign](assets/fr/23.webp)



Hapa, baada ya kuagiza muamala wetu kwenye Sparrow, tunaweza kuona kwamba ni sahihi moja tu ambayo imetumika kwenye shughuli hiyo.



![Co-Sign](assets/fr/24.webp)




Sasa hebu turudie jaribio, lakini kwa shughuli ya satoshi 21,000, yaani chini ya ukubwa wa juu (21212 Sats) tunaweka kwa Wallet hii.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Hebu tujaribu kutia sahihi muamala huu na ColdCardQ yetu.



Hakuna tatizo wakati huu, hakuna ujumbe wa onyo unaoonekana, na tunapoingiza muamala uliotiwa saini kwenye Sparrow wallet, wakati huu sahihi 2 zimetumika, na kufanya shughuli hiyo kuwa halali na tayari kusambazwa.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Ingia pamoja na Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA & Anwani Zilizoidhinishwa



Katika aya hii, tutatumia Wallet Multisig Co-Sign with Nunchuk, na kuchukua fursa ya kutumia masharti mapya ya matumizi ili kuona jinsi inavyoendelea.



Nenda kwa *Zana Zilizoboreshwa > Uwekaji Saini Mwenza wa ColdCard*.


Tunaombwa kuweka "Ufunguo wetu wa Sera ya Matumizi", ili kufikia menyu inayoturuhusu kubadilisha hali ya matumizi. Kwa upande wetu, tunaingia 12 x "nyama ya ng'ombe".



Tumeamua kuweka ukubwa wa 21212 Sats, na upeo wa juu wa "Kikomo cha Kasi" kwa sababu za vitendo zinazohusiana na mafunzo haya. Kwa upande mwingine, tutatumia menyu **"Anwani za Orodha Zilizoidhinishwa "** ili kulazimisha anwani ambazo pesa zetu zinaweza kutumika.




![Co-Sign](assets/fr/31.webp)




Changanua misimbo ya QR inayohusishwa na anwani (tutachagua 2) ungependa kuongeza kwenye orodha yako iliyoidhinishwa, kisha ubofye **"INGIA "**. Baada ya kuthibitisha anwani zako kwa kubofya **"INGIA "** mfululizo, tunaona kwamba vikomo vya ukubwa na anwani za walengwa vimetumika.



![Co-Sign](assets/fr/32.webp)



Hatimaye, ili kupata picha kamili ya uwezekano unaotolewa na "Co-Sign", hebu tuamilishe chaguo la "Web 2FA".


Kipengele hiki hukuwezesha kutumia programu inayotii TOTP RFC-6238 kama vile Kithibitishaji cha Google / Ente Auth / Kithibitishaji cha Proton / Authy 2FA / au Kithibitishaji cha Aegis, ili kuongeza usalama wa Layer.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Kwa maneno madhubuti, kabla ya kusaini muamala, utahitaji kuleta kifaa chako kilichounganishwa na intaneti kilichowezeshwa na NFC karibu na Coldcard yako. Hii itakupeleka kiotomatiki kwenye ukurasa wa wavuti wa coldcard.com, ambapo utaombwa kuingiza msimbo wa tarakimu 6 wa programu yako. Ukiweka msimbo sahihi, ukurasa wa wavuti utakuonyesha ama msimbo wa QR ili kutafuta ColdCardQ, au msimbo wa tarakimu 8 wa kuweka kwenye Mk4 yako, ili kuidhinisha kifaa chako kutia sahihi.





![Co-Sign](assets/fr/33.webp)



Baada ya kuchanganua msimbo wa QR unaoonyeshwa katika programu yako mbili ya uthibitishaji, na kuongeza akaunti yako ya ColdCard Co-Sign (CCC), utaulizwa kuthibitisha kuwa kila kitu kiko sawa kwa kuweka msimbo wako wa 2FA.



Andika ColdCard yako nyuma ya kifaa chako cha NFC.



![Co-Sign](assets/fr/34.webp)



Kwenye ukurasa wa wavuti unaofunguliwa, weka msimbo wa 2FA wa programu unayoipenda. Kisha changanua msimbo wa QR unaoonyeshwa na ColdCardQ yako (au weka msimbo wa tarakimu 8 unaoonyeshwa kwenye Mk4 yako).



![Co-Sign](assets/fr/35.webp)




Sasa tumeweka kikomo cha ukubwa (21212 Sats), anwani lengwa na uthibitishaji maradufu.



![Co-Sign](assets/fr/36.webp)



### 2- Hamisha Wallet Multisig 2-on-3 hadi Nunchuk



Wacha tusafirisha Wallet Multisig 2-on-3 hadi Nunchuk wakati huu, kama tulivyofanya na Sparrow hapo awali.


Nenda kwenye *Mipangilio > Multisig Wallet > 2/3: Saini Mwenza ya ColdCard > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Wakati huu chagua chaguo la NFC la kusafirisha kwa kubofya kitufe cha ColdcardQ cha jina sawa **"NFC "**.



![Co-Sign](assets/fr/37.webp)



Katika Nunchuk, ikiwa unafungua programu kwa mara ya kwanza, bofya kwenye **"Rejesha iliyopo Wallet"**.



![Co-Sign](assets/fr/38.webp)



Ikiwa tayari una Wallet kwenye programu, bofya kwenye **"+"** iliyo juu kulia, kisha **"Rejesha Wallet iliyopo"**.



![Co-Sign](assets/fr/39.webp)




Kisha chagua **"Rejesha Wallet kutoka COLDCARD "** kisha **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Hatimaye, gusa sehemu ya nyuma ya simu yako mahiri kwenye skrini ya ColdCardQ yako ili kuleta Wallet kupitia NFC.



![Co-Sign](assets/fr/41.webp)



Akaunti yetu na satoshi zilizowekwa awali kupitia Sparrow wallet zimerudi.



![Co-Sign](assets/fr/42.webp)



### 3- Kujaribu sera za matumizi zilizobainishwa mapema



Hebu sasa tujaribu kufanya muamala unaokiuka masharti 2 ya matumizi ambayo tumeweka. **Tutajaribu kutumia zaidi ya 21212 Sats kwa Address ambayo haijaidhinishwa.** Hebu tujaribu kutuma 22 222 Sats kwa Address bila mpangilio.



![Co-Sign](assets/fr/43.webp)



Baada ya muamala kuanzishwa, bofya kwenye vitone 3 vidogo kwenye kona ya juu kulia ili kuisafirisha kwa ColdCard yako.



![Co-Sign](assets/fr/44.webp)



Kisha chagua **"Hamisha kupitia BBQR "**, na uchanganue msimbo wa QR unaoonyeshwa na ColdCardQ yako.



![Co-Sign](assets/fr/45.webp)



ColdcardQ yako kisha inaonyesha onyo ambalo, unaposogeza hadi chini ya skrini, hufafanua kuwa muamala unakiuka masharti ya matumizi, kama inavyotarajiwa.



**Kumbuka kwamba kifaa hakituambii masharti ya matumizi yanayohusika, ili kuzuia mvamizi anayeweza kujaribu kukwepa vikwazo.**




![Co-Sign](assets/fr/46.webp)



Ikiwa bado unathibitisha kwa kubonyeza **"INGIA "**, msimbo wa QR unaowakilisha shughuli iliyotiwa saini inaonekana. Ikiwa utaiingiza kwenye Nunchuk, unaweza kuona kwamba saini moja tu imetumika.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Wacha tufanye operesheni sawa kabisa, lakini wakati huu na muamala unaoheshimu kikomo cha ukubwa (21212 Sats), na kutumia satoshis kwenye mojawapo ya anwani 2 ambazo tumepanga mapema.



Tunatuma Nunchuk 12121 Sats kwa mojawapo ya anwani zetu 2. Kisha tunahamisha muamala kwa ColdCard yetu kama tulivyofanya awali.



![Co-Sign](assets/fr/49.webp)




Baada ya kuleta muamala ambao haujatiwa saini kwenye ColdCardQ yetu, hebu tuone tunachoonyeshwa wakati huu.



Onyo linakuwepo kila wakati, lakini wakati huu, tukisogeza hadi chini ya skrini, tunaona kwamba ni suala la kuhalalisha muamala kupitia 2FA. Kifaa kinatuomba tulete ColdcardQ yetu karibu na terminal yetu ya NFC iliyounganishwa kwenye Mtandao (simu mahiri au kompyuta kibao), ambayo tunafanya.



![Co-Sign](assets/fr/50.webp)



Ukurasa wa wavuti unafungua kwenye simu yetu mahiri, ukituomba tuweke msimbo wetu wa 2FA, ambao tunafanya shukrani kwa Kithibitishaji cha Proton.



![Co-Sign](assets/fr/51.webp)





Kisha changanua msimbo wa QR unaoonekana kwenye ukurasa wa wavuti, ili kuidhinisha ColdCard yako kutia sahihi muamala.


Muamala sasa umetiwa saini na vitufe 2 na kwa hivyo ni halali.



Ikiwa "Push Tx" imewashwa kwenye ColdCardQ yako, unaweza kutangaza muamala moja kwa moja kwenye mtandao kwa kugusa rahisi nyuma ya simu yako mahiri.



![Co-Sign](assets/fr/52.webp)




Iwapo huna "Push tx" iliyoamilishwa, bonyeza kitufe cha "QR" kwenye ColdCardQ yako ili kuonyesha muamala uliotiwa saini kama msimbo wa QR, na uilete kwenye Nunchuk, kwa njia sawa na katika mfano uliopita.



![Co-Sign](assets/fr/53.webp)



Wakati huu tunaona kuwa sahihi 2 zimetumika, kwa hivyo shughuli iko tayari kutangazwa kwenye mtandao wa Bitcoin.



![Co-Sign](assets/fr/54.webp)




Tumefika mwisho wa mafunzo haya, ambayo yatakupa muhtasari wa uwezekano unaotolewa na utendakazi wa Co-Sign iliyojumuishwa katika vifaa vya ColdCardQ na Mk4 vya Coinkite, pamoja na matumizi yake kupitia pochi kama vile Sparrow na Nunchuk.