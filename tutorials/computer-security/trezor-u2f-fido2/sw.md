---
name: "Trezor U2F & FIDO2"
description: Imarisha usalama wako mtandaoni ukitumia Trezor
---
![cover](assets/cover.webp)



Vifaa vya Trezor ni pochi za maunzi zilizoundwa awali kulinda Bitcoin Wallet, lakini pia zinaangazia chaguo za kina za uthibitishaji thabiti kwenye wavuti. Shukrani kwa upatanifu wao na itifaki za **U2F** na **FIDO2**, zinakuwezesha kupata ufikiaji salama wa akaunti zako za mtandaoni bila kutegemea manenosiri pekee.



Itifaki ya U2F (*Universal 2nd Factor*) ilianzishwa na Google na Yubico mwaka wa 2014, kisha kusawazishwa na Muungano wa FIDO. Huwezesha kipengele cha pili cha uthibitishaji halisi (2FA) kuongezwa wakati wa kuingia. Mara baada ya kuanzishwa, pamoja na nenosiri la kawaida, watumiaji lazima waidhinishe kila jaribio la kuunganisha kwenye akaunti yao kwa kubofya kitufe kwenye Trezor yao. Katika muktadha huu, Trezor inafanya kazi kwa njia sawa na Yubikey.



Njia hii inategemea kriptografia isiyolinganishwa: hakuna data ya siri inayosambazwa, na hivyo kufanya mashambulizi ya kuhadaa ili kupata maelezo ya kibinafsi au udukuzi kutofaa. U2F sasa inaungwa mkono na huduma nyingi za mtandaoni.



Mbali na U2F, ambayo huwezesha uthibitishaji wa vipengele viwili, Trezors pia inaunga mkono FIDO2 (* Utambulisho wa Haraka Mkondoni 2.0*), mageuzi ya U2F. Hii ni itifaki sanifu ya uthibitishaji kutoka 2018, ambayo huongeza mantiki ya U2F na inalenga kuchukua nafasi ya nywila kabisa. Inategemea vipengele viwili: *WebAuthn* (upande wa kivinjari) na *CTAP2* (upande wa ufunguo wa kimwili). FIDO2 huwezesha uthibitishaji wa "usio na nenosiri": watumiaji hujitambulisha pekee kupitia kifaa chao cha Trezor, ambacho hufanya kama ishara ya kipekee ya kriptografia, bila nenosiri la ziada. Itifaki hii sasa inaoana na idadi ya huduma za mtandaoni, hasa zile zinazolenga biashara.



Kando na utendakazi wa "bila nenosiri", FIDO2 pia huwezesha uthibitishaji wa vipengele viwili kwa njia sawa na U2F.



FIDO2 pia inatanguliza dhana ya vitambulisho vya mkazi, yaani, vitambulisho vilivyohifadhiwa moja kwa moja kwenye Trezor, ambavyo vinajumuisha uunganisho wa ufunguo wa faragha na maelezo ya utambulisho wa mtumiaji. Utaratibu huu huwezesha uthibitishaji bila nenosiri kweli: chomeka tu Trezor yako na uthibitishe ufikiaji, bila kuingiza kitambulisho au nenosiri. Kinyume chake, sifa zisizo za ukaaji, ambazo ni za kawaida zaidi, huhifadhi ufunguo wa kibinafsi tu kwenye kifaa; kitambulisho cha mtumiaji kinasalia kuhifadhiwa kwenye upande wa seva, na kwa hiyo lazima iingizwe katika kila muunganisho. Tutaangalia jinsi ya kuzihifadhi kwa Trezor yako baadaye.



Katika somo hili tutagundua jinsi ya kuwezesha U2F au FIDO2 kwa uthibitishaji wa vipengele viwili, na kisha jinsi ya kusanidi FIDO2 kufikia akaunti zako bila nenosiri, moja kwa moja na Trezor yako.



**Kumbuka:** U2F inaoana na miundo yote ya Trezor, lakini FIDO2 inatumika tu kwenye Safe 3, Safe 5, na Model T, si Model One.



## Kutumia U2F/FIDO2 kwa 2FA kwenye Trezor



Kabla ya kuanza, hakikisha kuwa umeweka Bitcoin Wallet yako kwenye Trezor yako. Ni muhimu kuhifadhi Mnemonic yako kwa usahihi, kwa vile vitufe vinavyotumika kwa U2F na FIDO2 katika uthibitishaji wa vipengele viwili vimetokana na Mnemonic hii. Trezor yako ikipotea au kuharibika, unaweza kurejesha ufikiaji wa funguo zako kwa kuingiza maneno yako ya Mnemonic kwenye kifaa kingine cha Trezor (kumbuka kuwa kwa vitambulisho vya FIDO2 katika hali ya "*password*", seed pekee haitoshi, kama tutakavyoona katika sehemu zinazofuata).



Unganisha Trezor yako kwenye kompyuta yako na uifungue.



![Image](assets/fr/01.webp)



Fikia akaunti unayotaka kulinda kwa uthibitishaji wa vipengele viwili. Kwa mfano, nitatumia akaunti ya Bitwarden. Kwa kawaida utapata chaguo la 2FA katika mipangilio ya huduma, chini ya vichupo vya "*uthibitishaji*", "*usalama*", "*ingia*" au "*nenosiri*".



![Image](assets/fr/02.webp)



Katika sehemu inayotolewa kwa uthibitishaji wa vipengele viwili, chagua chaguo la "*Nenosiri*" (neno linaweza kutofautiana kulingana na tovuti unayotumia).



![Image](assets/fr/03.webp)



Mara nyingi utaulizwa kuthibitisha nenosiri lako la sasa.



![Image](assets/fr/04.webp)



Ipe ufunguo wako wa usalama jina ili kutambulika kwa urahisi, kisha ubofye "*Ufunguo wa Kusoma*".



![Image](assets/fr/05.webp)



Maelezo ya akaunti yako yataonekana kwenye skrini ya Trezor. Gusa skrini au bonyeza kitufe ili kuthibitisha. Pia utaombwa kuthibitisha PIN yako.



![Image](assets/fr/06.webp)



Sajili ufunguo huu wa usalama.



![Image](assets/fr/07.webp)



Kuanzia sasa na kuendelea, unapotaka kuunganisha kwenye akaunti yako, pamoja na nenosiri lako la kawaida, utaombwa kuunganisha Trezor yako.



![Image](assets/fr/08.webp)



Kisha unaweza kubofya skrini yako ya Trezor ili kuthibitisha uthibitishaji.



![Image](assets/fr/09.webp)



Faida ya kutumia Hardware Wallet Trezor kwa uthibitishaji wa vipengele viwili ni kwamba unaweza kurejesha funguo zako kwa urahisi kutokana na maneno ya Mnemonic. Kando na hifadhi hii ya msingi, unaweza pia kutumia msimbo wa dharura unaotolewa na kila huduma ambapo umewasha 2FA. Nambari hii ya kuthibitisha dharura hukuwezesha kuunganisha kwenye akaunti yako ukipoteza ufunguo wako wa usalama. Kwa hivyo inachukua nafasi ya 2FA kwa unganisho ikiwa ni lazima.



Kwenye Bitwarden, kwa mfano, unaweza kufikia msimbo huu kwa kubofya "*Angalia msimbo wa uokoaji*".



![Image](assets/fr/10.webp)



Ninapendekeza kwamba uweke msimbo huu mahali tofauti na unapohifadhi nenosiri lako kuu, ili kuzuia zisiibiwe pamoja. Kwa mfano, ikiwa nenosiri lako limehifadhiwa katika kidhibiti cha nenosiri, weka msimbo wako wa dharura wa 2FA kwenye karatasi, tofauti.



Mbinu hii hukupa viwango viwili vya kuhifadhi nakala katika tukio la kupoteza Trezor yako kwa uthibitishaji wa 2FA: hifadhi rudufu ya kwanza kwa kutumia maneno ya Mnemonic kwa akaunti zako zote, na ya pili mahususi kwa kila akaunti iliyo na misimbo ya dharura. Hata hivyo, ni muhimu **kutochanganya jukumu la Mnemonic na lile la msimbo wa dharura**:




- Kishazi cha Mnemonic chenye maneno 12 au 24 hukupa ufikiaji sio tu kwa funguo zinazotumiwa kwa 2FA kwenye akaunti zako zote, lakini pia kwa bitcoins zako zilizolindwa na Trezor yako;
- Msimbo wa dharura hukuruhusu kukwepa kwa muda ombi la 2FA kwenye akaunti inayohusika (katika mfano huu, kwenye Bitwarden pekee).



## Kutumia FIDO2 kwenye Trezor



Mbali na uthibitishaji wa vipengele viwili, FIDO2 pia huwezesha uthibitishaji wa "usio na nenosiri", yaani bila kuingiza nenosiri wakati wa kuingia kwenye tovuti. Unganisha tu Trezor yako kwenye kompyuta yako ili kufikia akaunti yako salama kwa njia hii. Hivi ndivyo jinsi ya kusanidi kipengele hiki.



Kabla ya kuanza, hakikisha kuwa umeweka Bitcoin Wallet yako kwenye Trezor yako. Ni muhimu kuhifadhi Mnemonic, kwani vitambulishi vya FIDO2 "*isiyo na nenosiri*" vimesimbwa kwa njia fiche na seed yako (tutajua jinsi ya kuhifadhi vitambulishi hivi kwa usahihi katika sehemu inayofuata).



Unganisha Trezor kwenye kompyuta yako na uifungue.



![Image](assets/fr/01.webp)



Fikia akaunti unayotaka kulinda katika hali ya "*password*". Nitatumia akaunti ya Bitwarden kama mfano. Chaguo hili kawaida hupatikana katika mipangilio ya huduma, mara nyingi chini ya kichupo cha "*uthibitishaji*", "*usalama*" au "*nenosiri*".



Kwa Bitwarden, kwa mfano, chaguo linapatikana chini ya kichupo cha "**Nenosiri kuu**". Bofya "**Washa**" ili kuamilisha uthibitishaji kupitia FIDO2.



![Image](assets/fr/11.webp)



Mara nyingi utaulizwa kuthibitisha nenosiri lako.



![Image](assets/fr/12.webp)



Maelezo ya akaunti yako yataonekana kwenye skrini ya Trezor. Gusa skrini au bonyeza kitufe ili kuthibitisha. Utahitaji pia kuthibitisha PIN yako.



![Image](assets/fr/13.webp)



Kwenye tovuti, ongeza jina ili kukumbuka ufunguo wako wa usalama, kisha ubofye "*Washa*".



![Image](assets/fr/14.webp)



Kisha utaulizwa kujitambulisha ili kuangalia kuwa ufunguo unafanya kazi vizuri.



![Image](assets/fr/15.webp)



Kuanzia sasa, unapoingia kwenye akaunti yako, haitakuwa muhimu tena kuingiza barua pepe yako Address au kuingia. Bonyeza tu kwenye kitufe ili kujithibitisha kwa ufunguo halisi kwenye fomu ya kuingia.



![Image](assets/fr/16.webp)



Thibitisha muunganisho kwenye Trezor yako kwa kuweka PIN yako ya Hardware Wallet.



![Image](assets/fr/17.webp)



Utaunganishwa kwenye akaunti yako bila kulazimika kuingiza nenosiri lako.



![Image](assets/fr/18.webp)



**Tafadhali kumbuka kuwa hata ukiwezesha uthibitishaji wa "*usio na nenosiri*" kupitia FIDO2 kwenye Trezor yako, nenosiri kuu la akaunti yako ya mtandaoni bado litakuwa halali kwa madhumuni ya kuingia**



## Hifadhi hati zako za FIDO2 (wakazi wa vitambulisho)



Ikiwa unatumia FIDO2 au U2F kwa uthibitishaji wa vipengele viwili, yaani, kuingia katika akaunti zinazohitaji nenosiri pamoja na uthibitishaji wa 2FA kupitia Trezor yako, basi kifungu cha maneno cha Mnemonic pekee kitapata ufikiaji wa funguo zako. Hata hivyo, ikiwa unatumia FIDO2 katika hali ya "*isiyo na nenosiri*" kama ilivyoelezwa katika sehemu iliyotangulia, itakuwa muhimu kutengeneza nakala ya vitambulisho vyako vya FIDO pamoja na kuhifadhi nakala ya maneno yako ya Mnemonic ambayo husimba vitambulisho hivi kwa njia fiche.



Ili kufanya hivyo, utahitaji kompyuta iliyo na Python iliyosanikishwa. Fungua terminal na uendesha amri ifuatayo ili kusakinisha programu muhimu ya Trezor:



```shell
pip3 install --upgrade trezor
```



Unganisha Trezor yako kwenye kompyuta kupitia USB na uifungue kwa kutumia PIN yako.



![Image](assets/fr/01.webp)



Ili kupata orodha ya vitambulisho vya FIDO2 vilivyohifadhiwa kwenye Trezor, endesha amri ifuatayo:



```shell
trezorctl fido credentials list
```



Thibitisha uhamishaji kwenye Trezor yako.



![Image](assets/fr/19.webp)



Maelezo yako ya kuingia kwa FIDO2 yataonyeshwa kwenye terminal yako. Kwa mfano, kwa akaunti yangu ya Bitwarden, nilipata habari hii:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Nakili na uhifadhi habari hii yote kwenye faili ya maandishi. Hakuna hatari kubwa inayohusishwa na hifadhi hii, zaidi ya kufichua kuwa unatumia huduma hizi na FIDO2. "*Kitambulisho cha Utambulisho*" kimesimbwa kwa njia fiche kwa kutumia seed ya Wallet yako, kumaanisha kuwa mvamizi anayepata hifadhi hii hataweza kuunganisha kwenye akaunti zako, lakini tambua tu kuwa unatumia akaunti hizi. Ili kusimbua vitambulisho hivi, unahitaji seed katika Wallet yako.



Kwa hivyo unaweza kuunda nakala kadhaa za faili hii ya maandishi, na kuzihifadhi katika sehemu tofauti, kwa mfano ndani ya kompyuta yako, kwenye huduma ya kupangisha faili na kwenye midia ya nje kama vile kifimbo cha USB. Hata hivyo, kumbuka kuwa nakala hii haijasasishwa kiotomatiki, kwa hivyo utahitaji kuisasisha kila wakati unapoweka muunganisho mpya wa "*password*" na Trezor yako.



Sasa hebu fikiria umevunja Trezor yako. Ili kupata kitambulisho chako cha FIDO2, utahitaji kwanza kurejesha Wallet yako kwa kutumia maneno yako ya Mnemonic kwenye kifaa kipya cha Trezor kinachooana na FIDO2.



Mara tu urejeshaji utakapokamilika, ili kuingiza vitambulisho vyako vya FIDO2 kwenye kifaa kipya, endesha amri ifuatayo kwenye terminal yako:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Badilisha tu `<CREDENTIAL_ID>` kwa vitambulishi vyako. Kwa mfano, katika kesi yangu, hii ingetoa:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor yako itakuelekeza kuleta kitambulisho chako cha FIDO2. Thibitisha kwa kubonyeza skrini.



![Image](assets/fr/20.webp)



Kuingia kwako kwa FIDO2 sasa kunafanya kazi kwenye Trezor yako. Rudia utaratibu huu kwa kila moja ya vitambulisho vyako.



Hongera, sasa uko katika kasi ya kutumia Trezor yako na U2F na FIDO2! Ikiwa umepata mafunzo haya kuwa ya manufaa, ningeshukuru sana ikiwa utaacha kidole gumba cha Green hapa chini. Tafadhali jisikie huru kushiriki mafunzo haya kwenye mitandao yako ya kijamii. Asante sana!



Ningependekeza pia mafunzo haya mengine, ambayo tunaangalia suluhisho lingine la uthibitishaji wa U2F na FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e