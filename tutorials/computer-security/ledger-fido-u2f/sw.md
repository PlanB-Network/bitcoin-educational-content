---
name: "Ledger U2F & FIDO2"
description: Imarisha usalama wako mtandaoni kwa Ledger
---
![cover](assets/cover.webp)



Vifaa vya Ledger ni pochi za maunzi zilizoundwa awali ili kulinda Bitcoin Wallet, lakini pia zinaangazia chaguo za kina za uthibitishaji thabiti kwenye wavuti. Shukrani kwa upatanifu wao na itifaki za **U2F** na **FIDO2**, zinakuwezesha kupata ufikiaji salama wa akaunti zako za mtandaoni kwa kuweka kipengele cha pili cha uthibitishaji.



Itifaki ya U2F (Universal 2nd Factor) ilianzishwa na Google na Yubico mwaka wa 2014, kisha kusanifishwa na Muungano wa FIDO. Huwezesha kipengele cha pili cha uthibitishaji halisi (2FA) kuongezwa wakati wa kuingia. Mara baada ya kuanzishwa, pamoja na nenosiri la kawaida, watumiaji lazima waidhinishe kila jaribio la kuunganisha kwenye akaunti yao kwa kubofya kitufe kwenye Ledger yao. Katika muktadha huu, Ledger inafanya kazi kwa njia sawa na Yubikey. U2F kwa hakika ni kipengele kidogo cha kiwango cha FIDO2, kinachokijumuisha huku ikileta maboresho makubwa, ikiwa ni pamoja na usaidizi asilia kwa vivinjari vya kisasa na unyumbufu mkubwa katika udhibiti wa ufunguo wa uthibitishaji.



Mbinu hizi zinatokana na usimbaji fiche usiolinganishwa: hakuna data ya siri inayosambazwa, na hivyo kufanya mashambulizi ya kuhadaa ili kupata maelezo ya kibinafsi au udukuzi kutofaa. U2F na FIDO2 sasa zinaungwa mkono na huduma nyingi za mtandaoni.



Katika somo hili, tutakuonyesha jinsi ya kuwezesha U2F na FIDO2 kwa uthibitishaji wa vipengele viwili na Ledger yako.



**Kumbuka:** U2F na FIDO2 zinatumika kwenye vifaa vyote vya Ledger vilivyo na programu dhibiti ya hivi majuzi: kutoka toleo la 2.1.0 la Nano X na Nano S classic, na kutoka toleo la 1.1.0 la Nano S Plus. Miundo ya Stax na Flex inaendana kiasili.



## Sakinisha programu ya Ufunguo wa Usalama wa Ledger



Ikiwa unatumia kifaa cha Ledger, labda unajua kwamba firmware pekee haina vipengele vyote vinavyohitajika kusimamia pochi za crypto. Kwa mfano, ili kutumia Bitcoin Wallet, unahitaji kusakinisha programu ya "*Bitcoin*". Vile vile, ili kudhibiti funguo za MFA, utahitaji kusakinisha programu ya "*Ufunguo wa Usalama*".



Kabla ya kuanza, hakikisha kuwa umeweka Bitcoin Wallet yako kwenye Ledger yako. Ni muhimu kuhifadhi Mnemonic yako kwa usahihi, kwani funguo zinazotumiwa kwa 2FA zinatokana na Mnemonic hii. Ikiwa Ledger yako itapotea au kuharibika, unaweza kurejesha ufikiaji wa funguo zako kwa kuweka maneno yako ya Mnemonic kwenye kifaa kingine cha Ledger (kwa sasa, vitambulishi vya FIDO2 katika hali ya "*isiyo na nenosiri*" bado havitumiki kwenye Leja, kwa hivyo hakuna vitambulishi vya wakaazi).



Unganisha Ledger yako kwenye kompyuta yako na uifungue.



![Image](assets/fr/01.webp)



Ili kusakinisha programu, fungua programu ya [Ledger Live] (https://www.Ledger.com/Ledger-live), kisha uende kwenye kichupo cha "*Ledger* yangu". Tafuta programu ya "*Ufunguo wa Usalama*" na uisakinishe kwenye kifaa chako.



![Image](assets/fr/02.webp)



Programu ya "*Ufunguo wa Usalama*" inapaswa sasa kuonekana pamoja na programu zingine zilizosakinishwa kwenye Ledger yako.



![Image](assets/fr/03.webp)



Bofya kwenye programu ili kuiacha wazi kwa hatua zinazofuata kwenye mafunzo.



![Image](assets/fr/04.webp)



## Tumia U2F/FIDO2 kwa 2FA na Ledger



Fikia akaunti unayotaka kulinda kwa uthibitishaji wa vipengele viwili. Kwa mfano, nitatumia akaunti ya Bitwarden. Kwa kawaida utapata chaguo la 2FA katika mipangilio ya huduma, chini ya vichupo vya "*uthibitishaji*", "*usalama*", "*ingia*" au "*nenosiri*".



![Image](assets/fr/05.webp)



Katika sehemu inayotolewa kwa uthibitishaji wa vipengele viwili, chagua chaguo la "*Nenosiri*" (neno linaweza kutofautiana kulingana na tovuti unayotumia).



![Image](assets/fr/06.webp)



Mara nyingi utaulizwa kuthibitisha nenosiri lako la sasa.



![Image](assets/fr/07.webp)



Ipe ufunguo wako wa usalama jina ili kutambulika kwa urahisi, kisha ubofye "*Ufunguo wa Kusoma*".



![Image](assets/fr/08.webp)



Maelezo ya akaunti yako yataonekana kwenye onyesho la Ledger. Bonyeza kitufe cha "*Register*" ili kuthibitisha (au vitufe vyote viwili kwa wakati mmoja, kulingana na muundo unaotumia).



![Image](assets/fr/09.webp)



Ufunguo wa ufikiaji umesajiliwa kwa mafanikio.



![Image](assets/fr/10.webp)



Sajili ufunguo huu wa usalama.



![Image](assets/fr/11.webp)



Kuanzia sasa na kuendelea, unapoingia kwenye akaunti yako, pamoja na nenosiri lako la kawaida, utaulizwa kuunganisha Ledger yako.



![Image](assets/fr/12.webp)



Kisha unaweza kubofya kitufe cha "*Ingia*" kwenye onyesho lako la Ledger ili kuthibitisha uthibitishaji (au vitufe vyote viwili kwa wakati mmoja, kulingana na muundo unaotumia).



![Image](assets/fr/13.webp)



Faida ya kutumia Hardware Wallet Ledger kwa uthibitishaji wa vipengele viwili ni kwamba unaweza kurejesha funguo zako kwa urahisi kutokana na maneno ya Mnemonic. Kando na hifadhi hii ya msingi, unaweza pia kutumia msimbo wa dharura unaotolewa na kila huduma ambapo umewasha 2FA. Nambari hii ya kuthibitisha dharura hukuwezesha kuunganisha kwenye akaunti yako ukipoteza ufunguo wako wa usalama. Kwa hivyo inachukua nafasi ya 2FA kwa unganisho ikiwa ni lazima.



Kwenye Bitwarden, kwa mfano, unaweza kufikia msimbo huu kwa kubofya "*Angalia msimbo wa uokoaji*".



![Image](assets/fr/14.webp)



Ninapendekeza kwamba uweke msimbo huu mahali tofauti na unapohifadhi nenosiri lako kuu, ili kuzuia zisiibiwe pamoja. Kwa mfano, ikiwa nenosiri lako limehifadhiwa katika kidhibiti cha nenosiri, weka msimbo wako wa dharura wa 2FA kwenye karatasi, tofauti.



Mbinu hii hukupa viwango viwili vya uhifadhi iwapo utapoteza Ledger yako kwa uthibitishaji wa 2FA: hifadhi rudufu ya kwanza kwa kutumia maneno ya Mnemonic kwa akaunti zako zote, na chelezo ya pili ya akaunti mahususi kwa kutumia misimbo ya dharura. Hata hivyo, ni muhimu **kutochanganya jukumu la Mnemonic na lile la msimbo wa dharura**:




- Maneno ya Mnemonic yenye maneno 12 au 24 hukupa ufikiaji sio tu kwa funguo zinazotumiwa kwa 2FA kwenye akaunti zako zote, lakini pia kwa bitcoins zako zilizolindwa na Ledger yako;
- Msimbo wa dharura hukuruhusu kukwepa kwa muda ombi la 2FA kwenye akaunti inayohusika (katika mfano huu, kwenye Bitwarden pekee).



Hongera, sasa uko katika kasi ya kutumia Ledger yako kwa MFA! Ikiwa umepata mafunzo haya kuwa ya manufaa, ningeshukuru sana ikiwa utaacha kidole gumba cha Green hapa chini. Tafadhali jisikie huru kushiriki mafunzo haya kwenye mitandao yako ya kijamii. Asante sana!



Ningependekeza pia mafunzo haya mengine, ambayo tunaangalia suluhisho lingine la uthibitishaji wa U2F na FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e