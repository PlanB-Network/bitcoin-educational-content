---
name: YubiKey 2FA
description: Ni gute twokoresha urufunguzo rw’umutekano w’umubiri?
---
![cover](assets/cover.webp)


Muri iki gihe, ubuhinga bwo kwemeza ko umuntu ari uwundi (2FA) bwacitse ikintu gihambaye cane kugira ngo umuntu ashobore gukingira amakonti yo kuri Internet kugira ngo ntabe uwushobora kuyaronka ata wemerewe. Kubera ko ibitero vyo kuri Internet vyiyongera, kwizigira ijambobanga gusa kugira ngo ukingire amakonti yawe rimwe na rimwe ntibihagije.


2FA izana Layer y’inyongera y’umutekano mu gusaba uburyo bugira kabiri bwo kwemeza umuntu uretse ijambobanga rya kera. Ukwo kugenzura gushobora gufata uburyo butandukanye, nk’akarorero kode yoherezwa biciye kuri SMS, kode ihinduka ivuye kuri porogarama yihariye, canke gukoresha urufunguzo rw’umutekano rw’umubiri. Gukoresha 2FA biragabanya cane ingorane zo guhungabanya amakonti yawe, mbere n’igihe ijambo banga ryawe ryibwe.


Mu yindi nyigisho, narasiguye ingene woshiraho no gukoresha porogarama ya TOTP 2FA:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Aha, turabona ingene wokoresha urufunguzo rw’umutekano w’umubiri nk’ikintu ca kabiri co kwemeza amakonti yawe yose.


## Urufunguzo rwo gukingira umubiri ni uruhe?


Urufunguzo rw’umutekano w’umubiri ni igikoresho gikoreshwa mu kwongereza umutekano w’amakonti yawe yo kuri Internet biciye ku kwemeza ibintu bibiri (2FA). Ivyo bikoresho akenshi bisa n’utufunguruzo dutoduto twa USB dutegerezwa kwinjizwa mu nzira ya orodinateri kugira ngo umuntu asuzume ko ari we vy’ukuri ariko aragerageza kwifatanya.

![SECURITY KEY 2FA](assets/notext/01.webp)

Iyo winjiye muri konti irindwa na 2FA maze ugakoresha urufunguzo rw’umutekano w’umubiri, ntutegerezwa gusa kwinjiza ijambobanga ryawe risanzwe ariko kandi utegerezwa kwinjiza urufunguzo rw’umutekano w’umubiri muri mudasobwa yawe maze ukanda buto kugira ngo wemeze ko ari umunyakuri. Ubwo buryo rero bwongerako Layer y’umutekano, kuko naho umuntu yoshobora kuronka ijambobanga ryawe, ntazoshobora kwinjira muri konti yawe ata rufunguzo afise ku mubiri.


Urufunguzo rw’umutekano w’umubiri rurakora cane cane kuko rufatanya ubwoko bubiri butandukanye bw’ibintu vy’ukwemeza: ikimenyamenya c’ubumenyi (ijambobanga) n’ikimenyamenya c’uko umuntu afise (urufunguzo rw’umubiri).


Ariko rero, ubwo buryo bwa 2FA na bwo burafise ingorane. Ica mbere, utegerezwa kwama ufise urufunguzo rw’umutekano ruriho nimba wipfuza gukoresha amakonti yawe. Ushobora gukenera kuyishira ku rufunguzo rwawe. Ica kabiri, bitandukanye n’ubundi buryo bwa 2FA, gukoresha urufunguzo rw’umutekano rw’umubiri birimwo amahera y’intango kuko utegerezwa kugura ako gakoresho gatoyi. Igiciro c’imfunguruzo z’umutekano muri rusangi gihinduka hagati y’amayero 30 n’amayero 100 bivanye n’ibintu vyatowe.


## Ni urufunguzo uruhe rwo gukingira umubiri wohitamwo?


Kugira ngo uhitemwo urufunguzo rwawe rw’umutekano, utegerezwa kwitwararika ibintu vyinshi.

Mbere na mbere, urakeneye kugenzura amategeko ashigikiwe n’ico gikoresho. Nibura, ndahanura guhitamwo urufunguzo rushigikira OTP, FIDO2, na U2F. Ivyo bintu akenshi birashirwa ahabona n’abahinguzi mu ndondoro z’ibintu. Kugira ngo ugenzure ko urufunguzo rumwe rumwe ruhuye, urashobora kandi gusura [dongleauth.com](https://www.dongleauth.com/dongles/).

Vyongeye, urabe neza ko urufunguzo rujanye n’ubuhinga bwawe bwo gukoresha, naho nyene amashirahamwe azwi cane nka Yubikey muri rusangi ashigikira ubuhinga bwose bukoreshwa cane.


Ushobora kandi guhitamwo urufunguzo ushingiye ku bwoko bw’ibikoresho biri kuri mudasobwa yawe canke kuri telefone yawe. Nk’akarorero, nimba mudasobwa yawe ifise gusa ivyuho vya USB-C, nuhitemwo urufunguzo rufise urufunguzo rwo gufatanya USB-C. Hariho kandi imfunguruzo zitanga uburyo bwo gukorana biciye ku Bluetooth canke NFC.

![SECURITY KEY 2FA](assets/notext/02.webp)

Ushobora kandi kugereranya ibikoresho bishingiye ku bintu vy’inyongera bifise nk’amazi n’ubushobozi bwo guhangana na Dust, hamwe n’imiterere n’ubunini bw’urufunguzo.


Ku bijanye n’ibimenyetso vy’urufunguzo rw’umutekano, Yubico ni yo izwi cane n’ibikoresho vyayo [vy’urufunguzo rwa YubiKey](https://www.yubico.com/), ivyo jewe ubwanje nkoresha kandi ndabihanura. Google kandi itanga igikoresho gifise [Urufunguzo_rw’umutekano rwa Titan](https://iduka.google.com/fr/igicuruzwa/urufunguzo_rw’umutekano_rwa Titan). Ku bijanye n’ubundi buryo bwo gukoresha ubuhinga bufunguye, [SoloKeys](bitari OTP) na [NitroKey](nitrokey) ni uburyo bushimishije, ariko sinigeze ngira amahirwe yo kubigerageza.


## Ni gute twokoresha urufunguruzo rw’umutekano w’umubiri?


Iyo umaze kwakira urufunguzo rwawe rw’umutekano, nta n’ugutegura kwihariye bisabwa. Urufunguzo mu bisanzwe ruba rwiteguye gukoreshwa iyo rwakiriwe. Ushobora guca uyikoresha kugira ngo ukingire amakonti yawe yo kuri Internet ashigikira ubwo bwoko bw’ukwemeza. Nk’akarorero, nzokwereka ingene wokingira konti yanje ya Proton mail ukoresheje uru rufunguzo rw’umutekano rw’umubiri.

![SECURITY KEY 2FA](assets/notext/03.webp)

Uzosanga uburyo bwo gukoresha 2FA mu mirongo ya konti yawe, kenshi munsi y'igice ca "*Ijambobanga*" canke "*Umutekano*". Fyonda ku gasandugu canke kuri buto ishobora kugufasha gukoresha 2FA ukoresheje urufunguzo rw’umubiri.

![SECURITY KEY 2FA](assets/notext/04.webp)

Ushire urufunguzo rwawe muri mudasobwa yawe.

![SECURITY KEY 2FA](assets/notext/05.webp)

Kora kuri buto iri ku rufunguzo rwawe rw’umutekano kugira ngo wemeze.

![SECURITY KEY 2FA](assets/notext/06.webp)

Injira izina kugira ngo wibuke urufunguzo wakoresheje.

![SECURITY KEY 2FA](assets/notext/07.webp)

Kandi aho urafise, urufunguzo rwawe rw’umutekano rwarongerewe neza ku bijanye n’ukwemeza 2FA kwa konti yawe.

![SECURITY KEY 2FA](assets/notext/08.webp)

Mu karorero kanje, nigerageza gusubira kwifatanya na konti yanje ya Proton mail, nzobanza gusabwa kwandika ijambobanga ryanje hamwe n’izina ryanje ry’ukoresha. Ico ni co kintu ca mbere co kwemeza ko ari uwuriho.

![SECURITY KEY 2FA](assets/notext/09.webp)

Hanyuma, nsabwa gushiramwo urufunguzo rwanje rw’umutekano ku kintu ca kabiri co kwemeza.

![SECURITY KEY 2FA](assets/notext/10.webp)

Inyuma y’aho, nkeneye gukora kuri buto iri ku rufunguzo rw’umubiri kugira ngo nemeze ko ari ivy’ukuri, maze nca nsubira gukora kuri konti yanje y’ubutumwa bwa Proton.

![SECURITY KEY 2FA](assets/notext/11.webp)

Subiramwo iki gikorwa ku makonti yose yo kuri interineti wipfuza gukingira muri ubwo buryo, cane cane ku makonti ahambaye nk’amakonti yawe ya imeyili, abacungezi b’ijambobanga ryawe, ibikorwa vyawe vyo kubika mu gicu no kuri interineti, canke amakonti yawe y’ivy’amahera.