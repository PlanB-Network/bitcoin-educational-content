---
name: "Trezor U2F & FIDO2"
description: Komeza umutekano wawe wo kuri internet ukoresheje Trezor .
---
![cover](assets/cover.webp)



Ivyuma vya Trezor ni ibikoresho vy’ubuhinga bwa none vyagenewe gukingira Bitcoin Wallet, ariko kandi birafise uburyo buteye imbere bwo kwemeza ko ari ukuri ku rubuga. Kubera ko zihuye n’amategeko **U2F** na **FIDO2**, zituma ushobora gushika ku makonti yawe yo kuri internet ataco wizigiye gusa amajambo y’ibanga.



Iryo tegeko rya U2F (*Ikintu ca 2 c’isi yose*) ryashizweho na Google na Yubico mu 2014, hanyuma rishirwa ku rugero rumwe n’ishirahamwe rya FIDO. Bituma umuntu ashobora kwongerako ikintu ca kabiri co kwemeza ko ari we (2FA) iyo yinjiye.Igihe kimaze gukoreshwa, uretse ijambobanga rya kera, abakoresha bategerezwa kwemeza igihe cose bagerageza kwifatanya na konti yabo bakanda buto iri kuri Trezor yabo. Muri ivyo, Trezor ikora mu buryo busa n’ubw’i Yubikey.



Ubwo buryo bushingiye ku buhinga bwo gukingira amakuru ataco buvuze: nta makuru y’ibanga arungikwa, ivyo bikaba bituma ibitero vy’ubuhendanyi canke vy’ugufata amakuru bitagira akamaro. Ubu U2F ishigikiwe n’ibikorwa vyinshi vyo kuri internet.



Uretse U2F, ishoboza kwemeza umuntu mu buryo bubiri, Trezors irashigikira kandi FIDO2 (*Ikimenyetso c’uko umuntu yihuta kuri Internet 2.0*), ni ugutera imbere kwa U2F. Iyi ni porotokole y’ukwemeza ivy’ukuri kuva mu 2018, yagura ubuhinga bwa U2F kandi ikaba igamije gusubirira burundu amajambo y’ibanga. Ishingiye ku bice bibiri: *WebAuthn* (uruhande rw'umucukumbuzi) na *CTAP2* (uruhande rw'urufunguzo rw'umubiri). FIDO2 ishoboza kwemeza "ata jambobanga": abakoresha bimenyekanisha gusa biciye ku gikoresho cabo ca Trezor, gikora nk'igikoresho kidasanzwe c'ibanga token, ata jambobanga ry'inyongera. Ubu iyo porotokole irahuye n’ibikorwa vyinshi vyo kuri internet, cane cane ivyo vyerekeye ikigo.



Uretse ibikorwa vya "passwordless", FIDO2 na yo irashoboza kwemeza ibintu bibiri mu buryo busa na U2F.



FIDO2 kandi itanga iciyumviro c'ivyemezo vy'abanyagihugu, ni ukuvuga ibimenyetso bibitswe mu buryo butaziguye muri Trezor, birimwo urufunguzo rw'ibanga rushoboza gukorana n'amakuru y'ikimenyetso c'ukoresha. Ubu buryo burashoboza vy’ukuri kwemeza ata jambobanga: gusa ushiremwo Trezor yawe maze wemeze ko ushobora kuyironka, utashizemwo ID canke ijambobanga. Ku rundi ruhande, ivyemezo vy’ubudasa, ari vyo bimenyerewe cane, bibika urufunguzo rw’ibanga gusa mu gikoresho; ID y'ukoresha iguma ibitswe ku ruhande rwa server, kandi rero itegerezwa kwinjira ku guhuza kwose. Tuzorabira ingene wozikiza ukoresheje Trezor yawe mu nyuma.



Muri iyi nyigisho tuzobona ingene wokoresha U2F canke FIDO2 ku bijanye n’ugushingira intahe ibintu bibiri, hanyuma ingene wotunganya FIDO2 kugira ngo ushobore gushika ku makonti yawe ata jambobanga, ukoresheje Trezor yawe.



**Iciyumviro:** U2F ihuye n’ibikoresho vyose vya Trezor, ariko FIDO2 ikoreshwa gusa kuri Safe 3, Safe 5, na Model T, atari Model One.



## Gukoresha U2F/FIDO2 ku 2FA ku giti



Imbere y’uko utangura, urabe neza ko washizeho Bitcoin Wallet yawe kuri Trezor yawe. Ni ngombwa kubika neza Mnemonic yawe, kuko imfunguruzo zikoreshwa kuri U2F na FIDO2 mu kwemeza ibintu bibiri zikomoka kuri iyi Mnemonic. Iyo Trezor yawe yazimiye canke yononekaye, urashobora gusubira kuronka imfunguruzo zawe mu kwinjiza ijambo ryawe rya Mnemonic ku kindi gikoresho ca Trezor (menya ko ku vyemezo vya FIDO2 biri mu buryo bwa "*passwordless*", seed yonyene ntihagije, nk'uko tuzobibona mu bice bikurikira).



Huza Trezor yawe na mudasobwa yawe maze uyifungure.



![Image](assets/fr/01.webp)



Ushobora gushika kuri konti ushaka gukingira ukoresheje ivyemezo bibiri. Nk’akarorero, ngiye gukoresha konti ya Bitwarden. Ubusanzwe uzosanga uburyo bwa 2FA mu mitunganyirize ya serivisi, munsi y'ibice "*kwemeza*", "*umutekano*", "*kwinjira*" canke "*ijambobanga*".



![Image](assets/fr/02.webp)



Mu gice kigenewe kwemeza ibintu bibiri, hitamwo "*Passkey*" (ijambo rishobora guhinduka bivanye n'urubuga uriko urakoresha).



![Image](assets/fr/03.webp)



Akenshi uzosabwa kwemeza ijambobanga ryawe ry’ubu.



![Image](assets/fr/04.webp)



Ha urufunguzo rwawe rw'umutekano izina kugira ngo rumenyekane bitagoranye, hanyuma ukande kuri "*Soma Urufunguzo*".



![Image](assets/fr/05.webp)



Amakuru yerekeye konti yawe azoboneka ku rubuga rwa Trezor. Kora ku gicapo canke ukande kuri buto kugira ngo wemeze. Uzosabwa kandi kwemeza kode yawe ya PIN.



![Image](assets/fr/06.webp)



Kwandika uru rufunguzo rw’umutekano.



![Image](assets/fr/07.webp)



Kuva ubu, iyo ushaka kwifatanya na konti yawe, uretse ijambobanga ryawe risanzwe, uzosabwa kwifatanya na Trezor yawe.



![Image](assets/fr/08.webp)



Ushobora rero gukanda igicapo cawe ca Trezor kugira ngo wemeze ko ari ukuri.



![Image](assets/fr/09.webp)



Inyungu yo gukoresha Hardware Wallet Trezor ku kwemeza ibintu bibiri ni uko ushobora gusubirana imfunguruzo zawe bitagoranye biciye ku nsiguro ya Mnemonic. Uretse iyo backup y’ishimikiro, urashobora kandi gukoresha kode y’ivyihutirwa itangwa na buri serivisi aho wakoresheje 2FA. Iyi kode y’ivyihutirwa iragufasha kwifatanya na konti yawe iyo utakaje urufunguzo rwawe rw’umutekano. Isubirira rero 2FA ku bijanye n’uguhuza iyo bikenewe.



Ku Bitwarden, nk'akarorero, ushobora gushika kuri iyi kode ukanda kuri "*Raba kode yo gusubiza*".



![Image](assets/fr/10.webp)



Ndagusavye ko wobika iyo kode ahantu hatandukanye n’aho ubika ijambo banga ryawe nyamukuru, kugira ngo ntizibe hamwe. Nk’akarorero, nimba ijambobanga ryawe ribitswe mu mucungerezi w’ijambobanga, ubike kode yawe y’ivyihutirwa ya 2FA ku mpapuro, itandukanye.



Ubu buryo buraguha ingero zibiri z’ububiko mu gihe woba watakaje Trezor yawe ku bijanye n’ukwemeza kwa 2FA: ububiko bwa mbere ukoresheje ijambo Mnemonic ku makonti yawe yose, n’ubwa kabiri bwihariye kuri konti yose ifise amakode y’ivyihutirwa. Ariko rero, birahambaye **kudatera uruhara uruhara rwa Mnemonic n’urw’itegeko ry’ivyihutirwa**:




- Iryo jambo ry’amajambo 12 canke 24 Mnemonic riguha uburenganzira bwo kuronka atari gusa imfunguruzo zikoreshwa kuri 2FA kuri konti zawe zose, ariko kandi n’ama bitcoins yawe akingiwe na Trezor yawe ;
- Kode y’ivyihutirwa iraguha uburenganzira bwo guca mu gihe gito gusaba 2FA kuri konti yerekeye gusa (muri aka karorero, kuri Bitwarden gusa).



## Gukoresha FIDO2 ku gicapo



Uretse kwemeza ibintu bibiri, FIDO2 irashoboza kandi kwemeza "ata jambobanga", ni ukuvuga ata jambobanga winjiza igihe winjiye ku rubuga. Gusa n’ushobora gufatanya Trezor yawe na mudasobwa yawe kugira ngo ushikire konti yawe itekanye muri ubu buryo. Ehe ingene wotunganya iki kintu.



Imbere y’uko utangura, urabe neza ko washizeho Bitcoin Wallet yawe kuri Trezor yawe. Ni vyiza kubika Mnemonic, kuko ibimenyetso vya FIDO2 "*passwordless*" bishizwe mu nzira na seed yawe (tuzomenya ingene twobika neza ivyo bimenyetso mu gice gikurikira).



Huza Trezor na mudasobwa yawe maze uyifungure.



![Image](assets/fr/01.webp)



Ushobora gushika kuri konti wipfuza gukingira mu buryo bwa "*passwordless*". Nzokoresha konti ya Bitwarden nk’akarorero. Iryo hitamwo risanzwe riboneka mu mitunganyirize ya serivisi, kenshi munsi y'agace ka "*kwemeza*", "*umutekano*" canke "*ijambobanga*".



Ku Bitwarden, nk'akarorero, uburyo bwo guhitamwo buraboneka munsi y'agace ka "*Ijambobanga ry'umukuru*". Fyonda kuri "*Turn on*" kugira ngo ukoreshe ivyemezo biciye kuri FIDO2.



![Image](assets/fr/11.webp)



Akenshi uzosabwa kwemeza ijambobanga ryawe.



![Image](assets/fr/12.webp)



Amakuru yerekeye konti yawe azoboneka ku rubuga rwa Trezor. Kora ku gicapo canke ukande kuri buto kugira ngo wemeze. Uzokenera kandi kwemeza kode yawe ya PIN.



![Image](assets/fr/13.webp)



Ku rubuga, wongereko izina kugira wibuke urufunguzo rwawe rw'umutekano, hanyuma ukande kuri "*Turn on*".



![Image](assets/fr/14.webp)



Uzoca usabwa kwimenyekanisha kugira ngo umenye nimba urufunguzo rukora neza.



![Image](assets/fr/15.webp)



Kuva ubu, iyo winjiye muri konti yawe, ntibizoba bigikenewe ko winjiza email yawe Address canke ngo winjire. Fyonda gusa kuri buto kugira ngo wiyemeze ukoresheje urufunguzo rw’umubiri ruri ku rupapuro rwo kwinjira.



![Image](assets/fr/16.webp)



Wemeze ko uhuye na Trezor yawe mu kwinjiza PIN yawe ya Hardware Wallet.



![Image](assets/fr/17.webp)



Uzoba uriko urahuzwa na konti yawe utabwirizwa kwinjiza ijambo banga ryawe.



![Image](assets/fr/18.webp)



**Urabona ko naho woba ukoresheje "*passwordless*" authentication biciye kuri FIDO2 kuri Trezor yawe, ijambobanga ry'ingenzi rya konti yawe yo kuri internet rizoguma rikora ku ntumbero zo kwinjira**



## Bika ivyemezo vyawe vya FIDO2 (abatuye mu vyemezo)



Niba ukoresha FIDO2 canke U2F ku kwemeza ibintu bibiri, ni ukuvuga kwinjira muri konti zisaba ijambobanga ryongeyeko kwemeza 2FA biciye kuri Trezor yawe, rero ijambo Mnemonic ryonyene rizogusubiza uburenganzira bwo gushika ku mfunguruzo zawe. Ariko rero, nimba uriko urakoresha FIDO2 mu buryo bwa "*passwordless*" nk'uko vyavuzwe mu gice ca mbere, bizoba ngombwa ko ukora kopi y'amakuru yawe ya FIDO uretse no gukora backup y'ijambo ryawe rya Mnemonic ripfuka ayo makuru.



Kugira ubikore, uzokenera mudasobwa irimwo Python. Gufungura terminal maze ukoreshe itegeko rikurikira kugira ngo ushiremwo porogaramu ya Trezor ikenewe:



```shell
pip3 install --upgrade trezor
```



Huza Trezor yawe na mudasobwa biciye kuri USB hanyuma uyifungure ukoresheje kode yawe ya PIN.



![Image](assets/fr/01.webp)



Kugira ngo ubone urutonde rw'ibimenyetso vya FIDO2 bibitswe kuri Trezor, koresha iri tegeko:



```shell
trezorctl fido credentials list
```



Wemeze ivyoherezwa hanze kuri Trezor yawe.



![Image](assets/fr/19.webp)



Amakuru yawe yo kwinjira muri FIDO2 azogaragara kuri terminal yawe. Nk’akarorero, kuri konti yanje ya Bitwarden, naronse aya makuru:



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



Kopa kandi ubike aya makuru yose muri dosiye y’inyandiko. Nta ngorane ikomeye ijana n'iyi nzira y'ububiko, uretse guhishura ko uriko urakoresha izo serivisi na FIDO2. "*Credential ID*" ipfutse hakoreshejwe seed ya Wallet yawe, bisobanura ko uwutera aronka iyo backup atazoshobora kwifatanya na konti zawe, ariko akamenya gusa ko uriko urakoresha izo konti. Kugira ngo ushobore gufungura izo ID, ukeneye seed muri Wallet yawe.



Ushobora rero gukora kopi nyinshi z’iyi dosiye y’inyandiko, maze ukazibika ahantu hatandukanye, nk’akarorero mu karere kawe kuri mudasobwa yawe, kuri servisi yo kwakira dosiye no ku bikoresho vyo hanze nk’inkoni ya USB. Ariko rero, uzirikane ko iyo backup idahinduka, rero uzokenera kuyisubiramwo igihe cose ushizeho ubufatanye bushasha "*passwordless*" na Trezor yawe.



None reka twiyumvire ko wavunye Trezor yawe. Kugira ngo ubone amakuru yawe ya FIDO2, uzobanza gusubira kuronka Wallet yawe ukoresheje ijambo ryawe rya Mnemonic ku gikoresho gishasha ca Trezor gihuye na FIDO2.



Igihe ugusubirana kwarangiye, kugira ngo ushiremwo ibimenyetso vyawe vya FIDO2 ku gikoresho gishasha, koresha iri tegeko rikurikira muri terminal yawe:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Subiriza gusa `<CREDENTIAL_ID>` na kimwe mu bimenyetso vyawe. Nk’akarorero, ku bijanye nanje, ivyo vyotanga:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor yawe izogusaba kwinjiza ikimenyetso cawe ca FIDO2. Wemeze mu gukanda ku gicapo.



![Image](assets/fr/20.webp)



Injira yawe ya FIDO2 ubu irakora kuri Trezor yawe. Subiramwo iyo nzira kuri buri kimwe mu bimenyetso vyawe.



Urakoze cane, ubu uriko urakoresha Trezor yawe ufise U2F na FIDO2! Niwaba wabonye ko iyi nyigisho ari ngirakamaro, noshima cane iyo usiga urukumu rwa Green aha hepfo. Turagusavye ntutinye gusangiza abandi iyi nyigisho ku mbuga zawe zo gusangirirako amakuru. Murakoze cane!



Nashaka kandi gusaba iyi yindi nyigisho, aho turaba uwundi muti wo kwemeza U2F na FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e