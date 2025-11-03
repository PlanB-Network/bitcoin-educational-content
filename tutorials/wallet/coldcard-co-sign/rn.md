---
name: COLDCARD - Ikimenyetso
description: Tora igice ca Co-Sign maze ugikoreshe kuri COLDCARD yawe
---

![cover](assets/cover.webp)


*NB: Iyi nyigisho igenewe abantu basanzwe bafise ubumenyi bumwe bumwe ku bijanye n'ama wallet y'amasinya menshi, ibikoresho vya Coinkite, n'amaporogarama nka Sparrow wallet canke Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Kubera iki ColdCard ikora umukono?



Ivyo bigufasha kwongerako **ivyangombwa vyo gukoresha** ku gikoresho cawe ca ColdCard (Q canke Mk4) mu buryo bwa Hardware Security Module (HSM), kugira ngo ukinge amahera yawe mu gihe uguma ufise ubushobozi bwo kuyahindura no kuyagenzura.



Ivyo gukoresha amahera bishobora kuba, nk’akarorero:





- Imipaka ku bunini**: cap umubare w’ama bitcoins ushobora gukoresha mu gucuruza rimwe.
- Imipaka y’umuvuduko:** ufata ingingo y’ingene ushobora gukora ibikorwa vyinshi ku gihe (ku isaha, ku musi, ku ndwi, n’ibindi), bisaba umubare mutoyi w’amabuye hagati yavyo.
- Amaderesi yemejwe mbere:** Kwemerera gusa bitcoins koherezwa ku maderesi yemejwe mbere.
- Ivyemezo bibiri:** Bisaba kwemezwa n’iporogarama y’uwundi muntu 2FA (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) kuri telefone ngendanwa/tablette ikoresha NFC ifise interineti.



**Uko bikora



Mu kwongerako seed ya kabiri ku gikoresho cawe ca ColdCard Mk4 canke Q, citwa "Urufunguzo rw'Itegeko ry'Ikoreshwa", tuzovuga muri iyi nyigisho yose nk'"Urufunguzo rwa C".


Uretse iyi seed y'inyongera, uzosabwa gukora Supply n'imiburiburi urufunguzo rumwe rw'inyongera (XPUB), urwo tuzokwita "Urufunguzo rwo Gusubiza", kugira ngo ureme Wallet Multisig 2-on-N.



Mu ncamake, tugiye gukora Wallet Multisig, kandi igikoresho cawe ca ColdCard kizobamwo imfunguruzo 2 z'ibanga zikenewe kugira ngo ukoreshe amahera, umukuru w'igikoresho seed na "Urufunguzo rw'Itegeko ryo Gukoresha Amahera".



Igihe cose "C Key" isabwe gushirako umukono, ivyangombwa vy'ugukoresha amahera vyavuzwe birakora, kandi ColdCard izoshirako umukono gusa iyo igikorwa gihuye n'ivyo.



Niba wipfuza guheba ivyo bintu vyo gukoresha amahera, urashobora kubigira:




- mu gusinya n'imwe mu mfunguruzo zo gusubiza inyuma n'ukuboko kwa seed, canke imfunguruzo 2 zo gusubiza inyuma bivanye n'ubunini bwa Multisig yawe.
- mu kwinjira mu "Urufunguzo rw'Itegeko ry'Ikoreshwa" canke "Urufunguzo rwa C" mu rutonde rwa "Co-Sign". **Ivyo vya nyuma ntibishobora gusuzumwa ku gikoresho, ahandi ho umuntu wese yoshobora gukuraho amategeko y'ugukoresha amahera yatunganijwe.**




## Gutunganya ikimenyetso ca ColdCard



![video](https://youtu.be/MjMPDUWWegw)



### 1- Gukoresha imikorere



Mbere na mbere, urabe neza ko igikoresho cawe gifise n'imiburiburi verisiyo nshasha ya firmware:




- Mk4: umurongo wa 5.4.2
- IKIBAZO: v1.3.2IKIBAZO




Kuri Mk4 canke ColdCardQ yawe, genda kuri *Ibikoresho biteye imbere > Gusinyana hamwe na ColdCard*.



![Co-Sign](assets/fr/01.webp)



*Mu nyigisho ikurikira, amafoto azofatwa kuri ColdCardQ kugira ngo bibe vyiza, ariko intambwe n'ibifungurwa birasa hagati ya Mk4 na Q.*



Incamake y'imikorere iragaragazwa.


Amajambo akoreshwa mu gusobanura imfunguruzo, tuzosubira gukoresha muri Wallet y’imikono myinshi 2-ku-3 turiko turarema, ni:



Urufunguzo A = Umukuru w'ikarata y'ubukonje seed


Urufunguzo B = Urufunguzo rwo gusubiza inyuma


Urufunguzo C = Urufunguzo rw'Itegeko ry'Ikoreshwa



Fyonda **"Injira "**.



![Co-Sign](assets/fr/02.webp)



Intambwe ikurikira ni uguhitamwo urufunguzo rw'ibanga ruzokora nk'"Urufunguzo rw'Itegeko ry'Ikoreshwa" canke "Urufunguzo C".



Turashobora kubona ko dufise uburyo bwinshi bwo guhitamwo:





- Canke ukande **"ENTER "** kugira ngo generate interuro nshasha ya seed y'amajambo 12.





- Ushobora gukanda kuri **"(1) "** kugira ngo ushiremwo seed y'amajambo 12, canke uhitemwo **"(2) "** kugira ngo ushiremwo seed y'amajambo 24.





- Canke ukande **"(6) "** kugira ngo ushiremwo seed mu bubiko bw'ibikoresho vyawe.



Kubera intumbero z'iyi nyigisho, twafashe ingingo yo kwinjiza amajambo 12 seed asanzweho mu gukanda **"(1) "**. Ivyo bishobora kuba seed BIP39 iyo ari yo yose ufise, kandi bigaragara ko ufise ivy’inyuma.



Koresha klavye yawe kugira ngo winjize amajambo 12 yo muri seed yawe. Ku karorero, tuzohitamwo ijambo ry'ukuri ry'inka x 12. Hanyuma ukande **"ENTER "**.


*NB: iyo udafise backup y'iyi seed, ntuzosubira guhindura ama settings ya "Co-Sign" ku gikoresho cawe, kugira ngo uhindure uko ukoresha amahera*



Igikoresho ca "Co-Sign" ubu kirakoreshwa kuri iyo mashini. Inyuma y'aho tuzokenera guhitamwo uko dukoresha amahera, hanyuma turangize gukora Wallet ifise amasinya menshi.



![Co-Sign](assets/fr/03.webp)



### 2- Hitamwo ingene ukoresha amahera canke "*amategeko y'amahera*".



Aha turadondora ivyangombwa vyo gukoresha amahera bitegerezwa gushitswako igihe **"C Key "** canke **"Spending Policy Key**" ishira umukono ku gikorwa.



Mu **"Gusinya hamwe"**, kanda kuri **"Itegeko ry'Ikoreshwa**".



Ushobora rero guhitamwo ubunini burengeye, ni ukuvuga umubare munini w’amasatoshi ashobora gukoreshwa mu gucuruza rimwe.



Ku karorero, tuzohitamwo ubunini burengeye **21212** satoshis. Fyonda kuri **"ENTER "** kugira ngo wemeze.




![Co-Sign](assets/fr/04.webp)



Turaheza duhitamwo gushinga umuvuduko munini, ni ukuvuga umubare w’ibikorwa igikoresho kizoshobora gusinya ku gihe. Kuri iyi nyigisho, tuzohitamwo umuvuduko utagira aho ugarukira, ni ukuvuga ko ata n’aho ugarukira ku mubare w’ibikorwa.




![Co-Sign](assets/fr/05.webp)



### 3- Rema Wallet Multisig 2-ku-N



Turacari dukeneye guhitamwo urufunguzo rwa gatatu rwa Wallet Multisig yacu, ni ukuvuga **"Urufunguzo rwo Gucungera "** (Urufunguzo B), rwongerako **seed** y'umukuru w'ico gikoresho (Urufunguzo A) n'urufunguzo rwa **"Itegeko ry'Ikoreshwa ry'Amahera "** (Urufunguzo C).



"B Key" yacu izobwirizwa kwinjizwa biciye ku ikarita SD, canke biciye ku kode ya QR mu gihe ca ColdCardQ.


Kugira ivyo tubishikeko, tuzokenera igikoresho ca kabiri ca ColdCard Mk4 canke Q, aho "Urufunguzo B" rwacu rukoreshwa.



Kuri iki gikoresho ca kabiri kirimwo **"Urufunguzo rwawe rwo gucungera "**, vuga ColdCard Mk4 kuri aka karorero, genda uva ku rutonde nyamukuru uja kuri **"Imiterere "**, hanyuma, **"Multisig Wallet"**, hanyuma **"Sohora Xpub "**.


(Nimba igikoresho cawe ca kabiri ari ColdCardQ, uzoba ufise uburenganzira bwo gutanga Xpub yawe hanze biciye kuri kode ya QR, birashoboka).





![Co-Sign](assets/fr/06.webp)





Ku gicapo gikurikira, shiramwo ikarita SD hanyuma ukande kuri buto **"validate "** iri hasi iburyo. Hanyuma ukande kuri **"(1) "** kugira ngo ubike dosiye ku ikarita SD.



Dosiye izobamwo urutoke rw'urufunguzo rwa bose (*urutoke*) mw'izina ryayo, kandi izofata uburyo `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Hanyuma ushire ikarita SD muri "intango" ColdCardQ kugira ngo ushiremwo "Urufunguzo rwacu rwo Gukingira" (urufunguzo B).


Mu nzira ya "ColdCard Co-Signing", uhitemwo "Build 2-of-N", hanyuma ku gicapo gikurikira ukande **"ENTER "**, hanyuma wongere **"ENTER "** kugira ngo ushiremwo "Urufunguzo rwo gukingira" ku ikarita ya SD.



![Co-Sign](assets/fr/08.webp)



Ku gicapo gikurikira, usige "Inomero ya konti" ataco ivuga (kiretse umenye neza ico uriko urakora) hanyuma wongere ukande **"ENTER "**.



![Co-Sign](assets/fr/09.webp)



Ubwa nyuma, turiteguriye gukoresha indege yacu nshasha Wallet Multisig 2-sur-3, igizwe n’ibi bikurikira:



Urufunguzo A= Ikarata y'ubukonje Q umukuru seed


Urufunguzo B= Urufunguzo rwo gusubiza inyuma (rwavuye mu gikoresho ca kabiri ca Coldcard)


Urufunguzo C= Urufunguzo rw'Itegeko ry'Ikoreshwa ry'Imari (niba rikoreshejwe mu gusinya, rishiraho ivyangombwa vy'Ikoreshwa ry'Imari vyategekanijwe)



## Gusinya hamwe na Sparrow wallet



Niba ari ngombwa, raba inyigisho zikurikira kugira ngo umenye neza porogarama ya Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Yohereza hanze Wallet Multisig 2-sur-3 kuri Sparrow wallet



Ubu turakeneye kwohereza Wallet Multisig yacu Sparrow kugira ngo dushobore gushiramwo amasatoshi yacu ya mbere.



Mu bimenyetso nyamukuru vya ColdCardQ yawe, hitamwo **"Ivyagezwe "**, hanyuma **"Ibipapuro vya Multisig "**.


Ivyiyumviro vy'amasakoshi ya Multisig bizwi na ColdCard yawe ubu biragaragazwa, n'umubare w'imfunguruzo zirimwo hano "2/3" (2-sur3). Hitamwo Multisig **"Ikimenyetso c'Ikarata y'Igihugu "** twamaze gukora, hanyuma ukande kuri **"Ikarata y'Igihugu y'Igihugu "**.



![Co-Sign](assets/fr/10.webp)




Ubwa nyuma, hitamwo uburyo buzotuma ushobora kwohereza Wallet kuri Sparrow. Mu gihe cacu, tuzohitamwo ikarita SD, hanyuma rero dufyonde kuri **"(1) "** umaze kwinjiza ikarita SD mu kibanza A c'igikoresho.



![Co-Sign](assets/fr/11.webp)



Hanyuma muri Sparrow wallet, uhitemwo "Injira Wallet".



![Co-Sign](assets/fr/12.webp)



Hanyuma ukande kuri **"Injira dosiye "**. Hanyuma uhitemwo dosiye **"sohora-Coldcard_Co-sign.txt "** ku ikarita yawe ya SD.



![Co-Sign](assets/fr/13.webp)



Ha Wallet yawe izina nk’uko izoboneka muri Sparrow, hanyuma uhitemwo ijambobanga ryo gupfuka Wallet yawe (canke ntabwo).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Ubu turiteguriye kwakira ama satoshis yacu ya mbere no kugerageza ingene dukoresha amahera twashize kuri Wallet yacu.



![Co-Sign](assets/fr/16.webp)



### 2- Kugerageza amategeko y'ikoreshwa ry'amahera yasobanuwe



Nk’ukwibutsa, twari twafashe ingingo y’ubunini burengeye 21212 satoshis ku ndege yacu Wallet Multisig. Ivyo vyasobanura ko igihe cose Urufunguzo rwa Spending Policy (Urufunguzo C) rwasinye igikorwa, urwo rwa nyuma rwoba rufise akamaro gusa iyo amahera yakoreshejwe ari munsi canke angana na 21212 satoshis.



Reka tubigerageze.


Mbere, reka dufyonde ku rubuga rwa "Receive" muri Sparrow maze dushire Satss nkeyi kuri Wallet, izo tuzokoresha muri iyi nyigisho yose.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Rero reka tugerageze gukoresha amahera arenga 21212 yemerewe satoshis mu kwigana igikorwa co gukoresha 50.000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Tumaze gucapura kode ya QR iserukira amafaranga *atashizweko umukono* na ColdCardQ yacu kugira ngo twinjize amafaranga, ivyo nivyo twerekanwa ku rubuga. Ubutumwa bwo kugabisha buratubwira ko ivyangombwa vyo gukoresha amahera bitashitseko. Nitwashira umukono ku bijanye n'ugucuruza uko biri kwose, rero urufunguzo rumwe gusa muri 2 (umukuru wa seed ku gikoresho, ariko si "Urufunguzo C") ni rwo ruzoshira umukono.




![Co-Sign](assets/fr/23.webp)



Aha, tumaze kwinjiza ivy’ugucuruza vyacu muri Sparrow, turashobora kubona ko umukono umwe gusa ari wo washizwe ku bijanye n’ugucuruza.



![Co-Sign](assets/fr/24.webp)




None rero reka dusubiremwo igerageza, ariko ku bijanye n'ugucuruza kwa satoshis 21.000, ni ukuvuga munsi y'ubunini burengeye (21212 Sats) twashizeho kuri iyi Wallet.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Reka tugerageze gusinya kuri iyi nzira dukoresheje ColdCardQ yacu.



Nta ngorane kuri iyi ncuro, nta butumwa bwo kugabisha buboneka, kandi iyo twinjije amafaranga yashizweko umukono muri Sparrow wallet, kuri iyi ncuro amasinyatiro 2 yarashizweko, bituma amafaranga agira akamaro kandi yiteguriye gukwiragizwa.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Gusinyana hamwe na Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Urubuga 2FA n'amaderesi yera



Muri iki gice, tuzokoresha igitabu cacu ca Wallet Multisig Co-Sign na Nunchuk, maze dufate akaryo ko gushiramwo amategeko mashasha yo gukoresha amahera kugira ngo turabe ingene bigenda.



Genda kuri *Ibikoresho biteye imbere > Gusinya kumwe na ColdCard*.


Turasabwa kwinjira muri "Spending Policy Key" yacu, kugira ngo tubone uko dushobora guhindura uko dukoresha amahera. Mu gihe cacu, twinjira 12 x "inyama y'inka".



Twafashe ingingo yo kuguma dufise ubunini bwa 21212 Sats, n'ubunini burengeye "Limit Velocity" kubera imvo ngirakamaro zijanye n'iyi nyigisho. Ku rundi ruhande, tugiye gukoresha **"Whitelist Addresses "** kugira ngo dutegeke amaderesi amahera yacu ashobora gukoreshwako.




![Co-Sign](assets/fr/31.webp)




Scanna ama code ya QR ajanye n'amaderesi (tuzohitamwo 2) wipfuza kwongera ku rutonde rwawe, hanyuma ukande **"ENTER "**. Tumaze kwemeza aderesi zawe mu gukanda **"ENTER "** zikurikirana, turabona ko imipaka ku Bunini n'amaderesi y'abaronka inyungu yashizweho.



![Co-Sign](assets/fr/32.webp)



Ubwa nyuma, kugira ngo tubone ishusho yuzuye y'ubushobozi butangwa na "Co-Sign", reka dukoreshe uburyo bwa "Web 2FA".


Iyi nzira ishobora kugufasha gukoresha porogaramu yubahiriza TOTP RFC-6238 nk’Ivyemezo vya Google / Ente Auth / Ivyemezo vya Proton / Authy 2FA / canke Ivyemezo vya Aegis, kugira ngo wongereko Layer y’umutekano.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Mu majambo nyayo, imbere yo gusinya ku giciro, uzokenera kuzana igikoresho cawe gikoreshwa na NFC, gihuye na internet hafi y’ikarita yawe ya Coldcard. Ivyo bizoca bigutwara kuri paji y’urubuga ya coldcard.com, aho uzosabwa kwinjiza kode y’imirongo 6 y’ivyo usaba. Niwinjiza kode ibereye, urubuga ruzokwereka kode ya QR yo gucapura ColdCardQ, canke kode y’imirongo 8 yo kwinjiza kuri Mk4 yawe, kugira ngo ushobore kwemerera igikoresho cawe gusinya.





![Co-Sign](assets/fr/33.webp)



Uhejeje gucapura kode ya QR yerekanwa mu gikorwa cawe co kwemeza ko ari we, no kwongerako konti yawe ya ColdCard Co-Sign (CCC), uzosabwa kugenzura ko vyose biri ku rutonde mu kwinjiza kode yawe ya 2FA.



Andika ColdCard yawe inyuma y’igikoresho cawe ca NFC.



![Co-Sign](assets/fr/34.webp)



Ku rubuga ruzofunguka, shiramwo kode ya 2FA y’iporogarama ukunda. Hanyuma ushireko scanner ya QR code yerekanwa na ColdCardQ yawe (canke winjize code y’imirongo 8 yerekanwa muri Mk4 yawe).



![Co-Sign](assets/fr/35.webp)




Ubu twashizeho umupaka ku bunini (21212 Sats), amaderesi y’aho umuntu aja n’ukwemeza kabiri.



![Co-Sign](assets/fr/36.webp)



### 2- Yohereza hanze Wallet Multisig 2-ku-3 muri Nunchuk



Reka twohereze hanze Wallet Multisig 2-ku-3 muri Nunchuk kuri iyi ncuro, nk’uko twabigize kuri Sparrow mbere.


Genda kuri *Ivyagezwe > Amasakoshi ya Multisig > 2/3: Ikimenyetso c'Ikarata y'Igihugu > Ikarata y'Igihugu*.



![Co-Sign](assets/fr/10.webp)



Iyi nkuru uhitemwo uburyo bwa NFC bwo kohereza hanze ukanda kuri buto ya ColdcardQ y'izina rimwe **"NFC "**.



![Co-Sign](assets/fr/37.webp)



Muri Nunchuk, nimba uriko urafungura porogaramu ubwa mbere, kanda kuri **"Gusubizaho Wallet iriho"**.



![Co-Sign](assets/fr/38.webp)



Niba usanzwe ufise Wallet muri porogaramu, fyonda ku **"+"** iri hejuru iburyo, hanyuma **"Gusubiza Wallet iriho"**.



![Co-Sign](assets/fr/39.webp)




Hanyuma uhitemwo **"Gusubiza Wallet muri COLDCARD"** hanyuma **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Ubwa nyuma, ushire inyuma ya telefone yawe y’amaboko ku gicapo ca ColdCardQ yawe kugira ngo ushiremwo Wallet biciye kuri NFC.



![Co-Sign](assets/fr/41.webp)



Konti yacu n’ama satoshis mbere yashizwemwo biciye kuri Sparrow wallet vyaragarutse.



![Co-Sign](assets/fr/42.webp)



### 3- Kugerageza amategeko y'ikoreshwa ry'amahera yasobanuwe



Reka noneho tugerageze gukora transaction irenga ku ngingo 2 zo gukoresha amahera twashizeho. **Tuzogerageza gukoresha amafaranga arenga 21212 Sats ku Address itaremejwe.** Reka tugerageze kohereza 22 222 Sats ku Address y'imburakimazi.



![Co-Sign](assets/fr/43.webp)



Igihe iyo transaction imaze gukorwa, ukande ku tudodo dutoduto 3 turi hejuru iburyo kugira ngo uyirungike kuri ColdCard yawe.



![Co-Sign](assets/fr/44.webp)



Hanyuma uhitemwo **"Sohoka hanze biciye kuri BBQR "**, hanyuma ushireko kode ya QR yerekanwa na ColdCardQ yawe.



![Co-Sign](assets/fr/45.webp)



ColdcardQ yawe ica yerekana imburi, uko ugenda ugenda ushika hasi ku rubuga, igasobanura ko iyo nzira y’ugucuruza irenga ku ngingo z’ugukoresha amahera, nk’uko vyitezwe.



**Ibuka ko ico gikoresho kitatubwira ingene umuntu akoresha amahera, kugira ngo uwushobora kudutera ntagerageze gukingira ivyo bibujijwe.**




![Co-Sign](assets/fr/46.webp)



Niwaba ukiriko uremeza ukanda **"ENTER "**, kode ya QR iserukira igikorwa cashizweko umukono iraboneka. Iyo uyishize kuri Nunchuk, urashobora kubona ko umukono umwe gusa washizweko.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Reka dukore neza neza igikorwa nk’ico nyene, ariko ubu n’ugucuruza kwubahiriza umupaka w’ubunini (21212 Sats), kandi ugakoresha ama satoshis kuri imwe muri aderesi 2 twateguye imbere y’igihe.



Turarungika iyo Nunchuk 12121 Sats kuri imwe mu ma aderesi yacu 2. Hanyuma tukarungika iyo nzira mu ColdCard yacu nk’uko twabigize mbere.



![Co-Sign](assets/fr/49.webp)




Tumaze kwinjiza amafaranga atashizweko umukono muri ColdCardQ yacu, reka turabe ivyo tweretswe kuri iyi ncuro.



Imburi yama iriho, ariko kuri iyi ncuro, duhindukiye gushika hasi ku rubuga, turabona ko ari ikibazo co kwemeza ivy’ugucuruza biciye ku 2FA. Ico gikoresho kidusaba kuzana ColdcardQ yacu hafi y’aho dukoresha Internet (telefone ngendanwa canke tablette), ivyo na vyo tukabikora.



![Co-Sign](assets/fr/50.webp)



Kuri telefone yacu y’ubuhinga bwa none, haca hafunguka urubuga, rukadusaba kwinjiza kode yacu ya 2FA, ivyo tukabikora biciye kuri Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





Hanyuma ushireko scanner kuri kode ya QR iboneka kuri paji y’urubuga, kugira ngo wemere ColdCard yawe gusinya ku giciro.


Iryo soko ubu ryashizweko umukono n’imfunguruzo 2 rero rirafise akamaro.



Iyo "Push Tx" ikoreshwa kuri ColdCardQ yawe, urashobora gutangaza iyo nzira ku rubuga rwa interineti ukoresheje gufyonda gusa inyuma ya telefone yawe.



![Co-Sign](assets/fr/52.webp)




Niba udafise "Push tx" ikoreshwa, kanda kuri buto ya "QR" kuri ColdCardQ yawe kugira ngo ugaragaze igikorwa cashizweko umukono nk'ikode ya QR, hanyuma uyishire kuri Nunchuk, mu buryo bumwe nk'uko vyari mu karorero ka mbere.



![Co-Sign](assets/fr/53.webp)



Ico gihe turabona ko hari amasinyatire 2 yashizweho, rero iyo transaction iteguye gutangazwa ku rubuga rwa Bitcoin.



![Co-Sign](assets/fr/54.webp)




Twarashitse ku mpera y’iyi nyigisho, izoguha icegeranyo c’ubushobozi butangwa n’imikorere ya Co-Sign yinjijwe mu bikoresho vya Coinkite ColdCardQ na Mk4, hamwe n’ikoreshwa ryayo biciye mu bikoresho nka Sparrow na Nunchuk.