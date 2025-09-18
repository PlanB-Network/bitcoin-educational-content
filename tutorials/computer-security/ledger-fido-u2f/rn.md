---
name: "Ledger U2F & FIDO2"
description: Wongere umutekano wawe wo kuri internet ukoresheje Ledger.
---
![cover](assets/cover.webp)



Ivyo bikoresho vya Ledger ni ibikoresho vy’ubuhinga bwa none vyagenewe gukingira Bitcoin Wallet, ariko kandi birafise uburyo buteye imbere bwo kwemeza ko ari ukuri ku rubuga. Kubera ko zihuye n’amategeko **U2F** na **FIDO2**, zigufasha gukingira amakonti yawe yo kuri interineti mu gushinga ikintu ca kabiri co kwemeza.



Iryo tegeko ryitwa U2F (Ikintu ca 2 c’isi yose) ryashizweho na Google na Yubico mu 2014, hanyuma rishirwa ku rugero rumwe n’ishirahamwe rya FIDO. Bituma umuntu ashobora kwongerako ikintu ca kabiri co kwemeza ko ari we (2FA) igihe yinjira. Iyo kimaze gukoreshwa, uretse ijambobanga rya kera, abakoresha bategerezwa kwemera igihe cose bagerageza kwifatanya na konti yabo bakanda buto iri kuri Ledger yabo. Muri ivyo, Ledger ikora mu buryo busa n’ubw’i Yubikey. U2F mu vy’ukuri ni igice c’ingingo ngenderwako ya FIDO2, kiyikubiyemwo mu gihe izana iterambere rikomeye, harimwo n’ugushigikira ivy’imvukira ku bikoresho vy’ubuhinga bwa none n’uguhinduranya cane mu gucunga urufunguzo rwo kwemeza.



Ubwo buryo bushingiye ku buhinga bwo gukingira amakuru ataco buvuze: nta makuru y’ibanga arungikwa, ivyo bikaba bituma ibitero vy’ubuhendanyi canke vy’ugufata amakuru bitagira akamaro. U2F na FIDO2 ubu zifashwa n’ibikorwa vyinshi vyo kuri internet.



Muri iyi nyigisho, tuzokwereka ingene wokoresha U2F na FIDO2 ku bijanye n'ukwemeza ibintu bibiri ukoresheje Ledger yawe.



**Iciyumviro:** U2F na FIDO2 zishigikirwa ku bikoresho vyose vya Ledger bifise porogarama nshasha: kuva kuri verisiyo 2.1.0 ku Nano X na Nano S classic, no kuva kuri verisiyo 1.1.0 ku Nano S Plus. Ivyitegererezo vya Stax na Flex birahuye neza.



## Shiraho porogaramu y'urufunguzo rw'umutekano Ledger



Niba ukoresha igikoresho ca Ledger, birashoboka ko uzi ko firmware yonyene idafise ibintu vyose bikenewe kugira ngo ushobore gucunga ama wallets y’amahera. Nk'akarorero, kugira ngo ukoreshe Bitcoin Wallet, ukeneye gushiramwo porogarama "*Bitcoin*". Na wewe nyene, kugira ngo ushobore gucunga imfunguruzo za MFA, uzokenera gushiramwo porogarama "*Urufunguzo rw'umutekano*".



Imbere yo gutangura, urabe neza ko washizeho Bitcoin Wallet yawe kuri Ledger yawe. Ni ngombwa kubika neza Mnemonic yawe, kuko imfunguruzo zikoreshwa muri 2FA zikomoka kuri iyi Mnemonic. Iyo Ledger yawe yazimiye canke yononekaye, urashobora gusubira kuronka imfunguruzo zawe mu kwinjiza ijambo ryawe rya Mnemonic ku kindi gikoresho ca Ledger (ubu, ibimenyetso vya FIDO2 biri mu buryo bwa "*passwordless*" ntibirashigikirwa kuri Ledgers, rero nta bimenyetso vy'abatuye biriho).



Huza Ledger yawe na mudasobwa yawe maze uyifungure.



![Image](assets/fr/01.webp)



Kugira ngo ushiremwo iyo porogarama, fungura porogarama [Ledger Live] (https://www.Ledger.com/Ledger-live), hanyuma ugende ku rubuga rwitwa "*My Ledger*". Rondera porogaramu "*Urufunguzo rw'umutekano*" maze uyishire ku gikoresho cawe.



![Image](assets/fr/02.webp)



Porogaramu "*Urufunguzo rw'umutekano*" ubu ikwiye kuboneka iruhande y'izindi porogaramu zashizwe kuri Ledger yawe.



![Image](assets/fr/03.webp)



Fyonda kuri porogarama kugira ngo uyisige yuguruye kugira ngo ubone intambwe zikurikira mu nyigisho.



![Image](assets/fr/04.webp)



## Koresha U2F/FIDO2 ku 2FA na Ledger



Ushobora gushika kuri konti ushaka gukingira ukoresheje ivyemezo bibiri. Nk’akarorero, ngiye gukoresha konti ya Bitwarden. Ubusanzwe uzosanga uburyo bwa 2FA mu mitunganyirize ya serivisi, munsi y'ibice "*kwemeza*", "*umutekano*", "*kwinjira*" canke "*ijambobanga*".



![Image](assets/fr/05.webp)



Mu gice kijejwe kwemeza ibintu bibiri, hitamwo "*Passkey*" (ijambo rishobora guhinduka bivanye n'urubuga uriko urakoresha).



![Image](assets/fr/06.webp)



Akenshi uzosabwa kwemeza ijambobanga ryawe ry’ubu.



![Image](assets/fr/07.webp)



Ha urufunguzo rwawe rw'umutekano izina kugira ngo rumenyekane bitagoranye, hanyuma ukande kuri "*Soma Urufunguzo*".



![Image](assets/fr/08.webp)



Amakuru yerekeye konti yawe azoboneka ku kigaragaza Ledger. Kanda kuri buto ya "*Register*" kugira ngo wemeze (canke buto zompi icarimwe, bivanye n'umuderi uriko urakoresha).



![Image](assets/fr/09.webp)



Urufunguzo rwo kwinjira rwanditswe neza.



![Image](assets/fr/10.webp)



Kwandika uru rufunguzo rw’umutekano.



![Image](assets/fr/11.webp)



Kuva ubu, iyo winjiye muri konti yawe, uretse ijambobanga ryawe risanzwe, uzosabwa gufatanya Ledger yawe.



![Image](assets/fr/12.webp)



Ushobora rero gukanda buto ya "*Log in*" ku kigaragaza cawe ca Ledger kugira ngo wemeze ko ari ukuri (canke buto zompi icarimwe, bivanye n'umuderi uriko urakoresha).



![Image](assets/fr/13.webp)



Inyungu yo gukoresha Hardware Wallet Ledger ku bijanye n’ukwemeza ibintu bibiri ni uko ushobora kugarura imfunguruzo zawe bitagoranye biciye ku nsiguro Mnemonic. Uretse iyo backup y’ishimikiro, urashobora kandi gukoresha kode y’ivyihutirwa itangwa na buri serivisi aho wakoresheje 2FA. Iyi kode y’ivyihutirwa iragufasha kwifatanya na konti yawe iyo utakaje urufunguzo rwawe rw’umutekano. Isubirira rero 2FA ku bijanye n’uguhuza iyo bikenewe.



Ku Bitwarden, nk'akarorero, ushobora gushika kuri iyi kode ukanda kuri "*Raba kode yo gusubiza*".



![Image](assets/fr/14.webp)



Ndagusavye ko wobika iyo kode ahantu hatandukanye n’aho ubika ijambo banga ryawe nyamukuru, kugira ngo ntizibe hamwe. Nk’akarorero, nimba ijambobanga ryawe ribitswe mu mucungerezi w’ijambobanga, ubike kode yawe y’ivyihutirwa ya 2FA ku mpapuro, itandukanye.



Ubu buryo buraguha ingero zibiri z’ububiko mu gihe woba watakaje Ledger yawe kugira ngo wemeze ko ari 2FA: ububiko bwa mbere ukoresheje ijambo Mnemonic ku makonti yawe yose, n’ububiko bwa kabiri bushingiye kuri konti ukoresheje amakode y’ivyihutirwa. Ariko rero, birahambaye **kudatera uruhara uruhara rwa Mnemonic n’urw’itegeko ry’ivyihutirwa**:




- Iryo jambo ry’amajambo 12 canke 24 Mnemonic riguha uburenganzira bwo gukoresha atari gusa imfunguruzo zikoreshwa kuri 2FA kuri konti zawe zose, ariko kandi n’ama bitcoins yawe akingiwe na Ledger yawe ;
- Kode y’ivyihutirwa iraguha uburenganzira bwo guca mu gihe gito gusaba 2FA kuri konti yerekeye gusa (muri aka karorero, kuri Bitwarden gusa).



Urasangwa, ubu uriko urakoresha Ledger yawe ku MFA! Niwaba wabonye ko iyi nyigisho ari ngirakamaro, noshima cane iyo usiga urukumu rwa Green aha hepfo. Turagusavye ntutinye gusangiza abandi iyi nyigisho ku mbuga zawe zo gusangirirako amakuru. Murakoze cane!



Nashaka kandi gusaba iyi yindi nyigisho, aho turaba uwundi muti wo kwemeza U2F na FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e