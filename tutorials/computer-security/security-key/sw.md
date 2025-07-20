---
name: YubiKey 2FA
description: Jinsi ya kutumia ufunguo halisi wa usalama?
---
![cover](assets/cover.webp)


Siku hizi, uthibitishaji wa vipengele viwili (2FA) umekuwa muhimu kwa ajili ya kuimarisha usalama wa akaunti za mtandaoni dhidi ya ufikiaji usioidhinishwa. Kwa kuongezeka kwa mashambulizi ya mtandaoni, kutegemea tu nenosiri ili kulinda akaunti zako hakutoshi.


2FA inatanguliza Layer ya ziada ya usalama kwa kuhitaji aina ya pili ya uthibitishaji pamoja na nenosiri la kawaida. Uthibitishaji huu unaweza kuchukua aina mbalimbali, kama vile nambari ya kuthibitisha iliyotumwa kupitia SMS, msimbo unaobadilika unaozalishwa na programu maalum au matumizi ya ufunguo halisi wa usalama. Matumizi ya 2FA kwa kiasi kikubwa hupunguza hatari za akaunti yako kuathiriwa, hata katika tukio la kuibiwa nenosiri lako.


Katika somo lingine, nilielezea jinsi ya kusanidi na kutumia programu ya TOTP 2FA:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Hapa, tutaona jinsi ya kutumia ufunguo halisi wa usalama kama kipengele cha pili cha uthibitishaji wa akaunti zako zote.


## Ufunguo wa usalama halisi ni nini?


Ufunguo halisi wa usalama ni kifaa kinachotumiwa kuimarisha usalama wa akaunti zako za mtandaoni kupitia uthibitishaji wa vipengele viwili (2FA). Vifaa hivi mara nyingi hufanana na vitufe vidogo vya USB ambavyo lazima vichopwe kwenye mlango wa kompyuta ili kuthibitisha kuwa ni mtumiaji halali anayejaribu kuunganisha.

![SECURITY KEY 2FA](assets/notext/01.webp)

Unapoingia katika akaunti iliyolindwa na 2FA na kutumia ufunguo halisi wa usalama, hupaswi tu kuingiza nenosiri lako la kawaida bali pia uweke ufunguo halisi wa usalama kwenye kompyuta yako na ubonyeze kitufe ili kuthibitisha uthibitishaji. Kwa hivyo, njia hii huongeza Layer ya ziada ya usalama, kwa sababu hata mtu akifanikiwa kupata nenosiri lako, hataweza kufikia akaunti yako bila kumiliki ufunguo.


Ufunguo halisi wa usalama ni mzuri sana kwa sababu unachanganya aina mbili tofauti za vipengele vya uthibitishaji: uthibitisho wa maarifa (nenosiri) na uthibitisho wa kumiliki (ufunguo halisi).


Walakini, njia hii ya 2FA pia ina hasara. Kwanza, lazima uwe na ufunguo wa usalama kila wakati ikiwa ungependa kufikia akaunti zako. Huenda ukahitaji kuiongeza kwenye mnyororo wako wa vitufe. Pili, tofauti na mbinu zingine za 2FA, kutumia ufunguo halisi wa usalama hujumuisha gharama ya awali kwani lazima ununue kifaa kidogo. Bei ya funguo za usalama kwa ujumla hutofautiana kati ya €30 na €100 kulingana na vipengele vilivyochaguliwa.


## Ufunguo gani wa usalama wa kimwili wa kuchagua?


Ili kuchagua ufunguo wako wa usalama, vigezo kadhaa lazima zizingatiwe.

Kwanza kabisa, unahitaji kuangalia itifaki zinazoungwa mkono na kifaa. Kwa uchache, ninashauri kuchagua ufunguo unaoauni OTP, FIDO2, na U2F. Maelezo haya kawaida huonyeshwa na watengenezaji katika maelezo ya bidhaa. Ili kuthibitisha uoanifu wa kila ufunguo, unaweza pia kutembelea [dongleauth.com](https://www.dongleauth.com/dongles/).

Pia, hakikisha kuwa ufunguo unaoana na mfumo wako wa uendeshaji, ingawa chapa zinazojulikana kama Yubikey kwa ujumla zinaauni mifumo yote inayotumika sana.


Unapaswa pia kuchagua ufunguo kulingana na aina ya bandari zinazopatikana kwenye kompyuta au smartphone yako. Kwa mfano, ikiwa kompyuta yako ina milango ya USB-C pekee, chagua ufunguo wenye kiunganishi cha USB-C. Baadhi ya funguo pia hutoa chaguzi za uunganisho kupitia Bluetooth au NFC.

![SECURITY KEY 2FA](assets/notext/02.webp)

Unaweza pia kulinganisha vifaa kulingana na vipengele vyake vya ziada kama vile maji na upinzani wa Dust, pamoja na sura na ukubwa wa ufunguo.


Kuhusu chapa muhimu za usalama, Yubico ndiyo inayojulikana zaidi kwa kutumia [vifaa vyake vya YubiKey](https://www.yubico.com/), ambayo mimi binafsi hutumia na kupendekeza. Google pia hutoa kifaa kilicho na [Ufunguo wa Usalama wa Titan](https://store.google.com/fr/product/titan_security_key). Kwa mbadala wa chanzo huria, [SoloKeys](https://solokeys.com/) (isiyo ya OTP) na [NitroKey](https://www.nitrokey.com/products/nitrokeys) ni chaguo za kuvutia, lakini sijawahi kupata fursa ya kuzijaribu.


## Jinsi ya kutumia ufunguo halisi wa usalama?


Baada ya kupokea ufunguo wako wa usalama, hakuna usanidi mahususi unaohitajika. Ufunguo kawaida huwa tayari kutumika baada ya kupokelewa. Unaweza kuitumia mara moja ili kulinda akaunti zako za mtandaoni zinazotumia aina hii ya uthibitishaji. Kwa mfano, nitakuonyesha jinsi ya kulinda akaunti yangu ya barua pepe ya Proton kwa ufunguo huu halisi wa usalama.

![SECURITY KEY 2FA](assets/notext/03.webp)

Utapata chaguo la kuwezesha 2FA katika mipangilio ya akaunti yako, mara nyingi chini ya sehemu ya "*Nenosiri*" au "*Usalama*". Bofya kwenye kisanduku cha kuteua au kitufe kinachokuruhusu kuwezesha 2FA kwa ufunguo halisi.

![SECURITY KEY 2FA](assets/notext/04.webp)

Chomeka ufunguo wako kwenye kompyuta yako.

![SECURITY KEY 2FA](assets/notext/05.webp)

Gusa kitufe kwenye ufunguo wako wa usalama ili kuthibitisha.

![SECURITY KEY 2FA](assets/notext/06.webp)

Weka jina ili kukumbuka ufunguo gani uliotumia.

![SECURITY KEY 2FA](assets/notext/07.webp)

Na hiyo ndiyo, ufunguo wako wa usalama umeongezwa kwa uthibitishaji wa 2FA wa akaunti yako.

![SECURITY KEY 2FA](assets/notext/08.webp)

Katika mfano wangu, nikijaribu kuunganisha tena kwa akaunti yangu ya barua ya Proton, nitaombwa kwanza kuingiza nenosiri langu pamoja na jina langu la mtumiaji. Hii ndiyo sababu ya kwanza ya uthibitishaji.

![SECURITY KEY 2FA](assets/notext/09.webp)

Kisha, ninaombwa kuchomeka ufunguo wangu wa usalama kwa sababu ya pili ya uthibitishaji.

![SECURITY KEY 2FA](assets/notext/10.webp)

Ifuatayo, ninahitaji kugusa kitufe kwenye ufunguo halisi ili kudhibitisha uthibitishaji, na nimeunganishwa tena kwa akaunti yangu ya barua ya Proton.

![SECURITY KEY 2FA](assets/notext/11.webp)

Rudia operesheni hii kwa akaunti zote za mtandaoni unazotaka kulinda kwa njia hii, hasa kwa akaunti muhimu kama vile akaunti zako za barua pepe, wasimamizi wako wa nenosiri, wingu na huduma zako za hifadhi mtandaoni, au akaunti zako za fedha.