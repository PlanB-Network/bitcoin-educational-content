---
name: Ibitoke bike
description: Umuyobozi wa telefone ngendanwa ku nzira yawe y'umuravyo
---

![cover](assets/cover.webp)



Muri iyi nyigisho, uzomenya ingene woshiramwo no gutunganya BitBanana kuri Android kugira ngo ushobore kugenzura node yawe ya Lightning ukoresheje telefone yawe. Turabona ingene wohuza porogarama n’ibikorwa remezo vyawe biriho (Umbrel, RaspiBlitz, myNode, canke node iyo ari yo yose ya LND/Core Lightning), ukore amahera y’umuravyo, ucunge imirongo yawe uri kure, urabe amafaranga winjiza mu nzira, kandi ukore ububiko bw’imiterere yawe. Uzomenya kandi ivyerekeye uburyo bwiza bwo gukingira uburenganzira bwo gushika ku nzira yawe, n’ingene igereranywa na Zeus, uburyo buzwi cane.



## Kumenyesha BitIbitoke



BitBanana ni porogaramu y’amatelefone ngendanwa ya Android ihindura telefone yawe ngendanwa ikaba urupapuro rwuzuye rwo kugenzura kure urudodo rwawe rwa Lightning. Udakunze ama wallets ya Lightning, ashiramwo urudodo rw’aho hantu kuri telefone, BitBanana ikoresha ubuhinga bwo gukoresha kure 100%: iyo porogarama nta satoshi ifise kandi ihuza gusa n’ibikorwa remezo vyawe biriho.



Yateguwe na Michael Wünsch afise uruhusha rwa MIT, iyo porogarama itanga icemezo c’uguserukira abantu bose ata makuru y’umuntu ku giti ciwe akoranirizwa hamwe n’inyubako zishobora gusubirwamwo zigenzurwa. BitBanana ishigikira LND na Core Lightning biciye ku ma URI asanzwe (`lndconnect://` na `clngrpc://`), bikorohereza cane imiterere y'intango. Iryo koraniro kandi ryemera LndHub na Nostr Wallet Connect ku bakoresha batagira urudodo rw’umuntu ku giti ciwe, naho nyene izo nzira zikora mu buryo bw’ububiko n’ibikorwa bike.



Iryo koraniro ritanga uburenganzira bwo gukoresha ibikorwa vyose bihambaye vy’uruzitiro rwawe: kohereza no kwakira amahera (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), gucunga umurongo w’umuravyo (gufungura, gufunga, guhindura amafaranga, gusubira gupima), gucunga ibiceri biteye imbere, n’ugucungera umuyagankuba. BitBanana kandi ishira mu ngiro ivyicaro vyinshi vy’umutekano bikomeye: gufunga biometric, uburyo bwo kwihisha, PIN y’ivyihutirwa, n’ugushigikira Tor kavukire kugira ngo amahuzu ntamenyekane.



## Imbuga zishigikiwe n'ugushiraho



### Gushiramwo



BitBanana iboneka gusa kuri Android 8.0 canke irengeye. Iryo koraniro ntiririho kuri iOS, kandi nta verisiyo itegekanijwe. Ivyo bifise aho bigarukira bisigurwa n’amateka y’uwo mugambi: BitBanana ni yo yakurikiye Zap Android, mu ntango yateguwe na Michael Wünsch, yahisemwo kubandanya igikorwa ciwe akoresheje izina ryiwe bwite. Zap yari umuryango w’ibikoresho bitandukanye (Zap Android, Zap iOS, Zap Desktop) vyateguwe n’abatanga intererano batandukanye bafise amakode atandukanye. BitBanana iriko irakurikirana ishami rya Android gusa.



Ikindi, iOS ecosystem iratanga ingorane zikomeye z’amategeko n’ubuhinga ku bikorwa vya Lightning bitagira ububiko. Mu mwaka w'2023, Apple yaranse guhindura Zeus kubera "ukurenga ku ruhusha", mu mwaka w'2024, Phoenix Wallet yaravuye muri App Store ya Amerika mu gihe hariho ukudakeka kw'amategeko ku bijanye n'abatanga serivisi za Lightning. Izo nzitizi zisigura igituma benshi mu bakora Lightning bakunda Android, itanga politike yuguruye cane ku bikorwa bitagira ububiko.



Uburyo butatu bwo gushiramwo Android buraboneka: Google Play Store (5000+ gushiramwo, guhindura ubwavyo), F-Droid (inyubako zishobora gusubirwamwo, kugenzura kode y’inkomoko), canke APK y’amaboko iva kuri GitHub.



![BitBanana](assets/fr/01.webp)



Urubuga rwemewe rwa bitbanana.app (ibubamfu) rwirata "100% Ukwirinda n'amakuru ZERO". Igishushanyo co hagati kirerekana uburyo butatu bwo gukuraho: F-Droid (ni vyiza), Google Play, na APK. Igishushanyo kiri iburyo kirerekana uruhusha rw’amatangazo y’imburi zo kwishura.



Iryo koraniro risaba uruhusha: urubuga (uguhuza node), kamera (amakode ya QR), NFC (LNURL), ibikorwa vyo mu nyuma (amatangazo), biometrics (umutekano), na WireGuard VPN. Nta bakurikirana, nta makuru yegeranywa. Gushoboza ijambobanga canke gufunga biometric kugira ngo ushobore gushikamwo.



## Imiterere y'intango



### Guhuza n'umurongo wa LND



Kugira ngo uhuze BitBanana n’urudodo rwawe rwa LND (Umutaka, RaspiBlitz, urudodo rwanje), rondera URI canke kode ya QR irimwo aderesi, icemeza TLS n’inyama z’ukwemeza.



Kuri iyi nyigisho, turiko turakoresha urudodo rwa LND biciye ku mutaka. Kubindi bisobanuro, raba inyigisho yacu yihariye :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Ku rubuga rwa Lightning Node, genda kuri menyu iri hejuru iburyo maze uhitemwo "Huza wallet".



![BitBanana](assets/fr/04.webp)



Hitamwo **gRPC (Tor)** kugira ngo uhuze biciye kuri Tor (ni vyiza). Kode ya QR n’ibindi (Umushitsi .igitunguru, Icibutso 10009, Macaroon) biragaragazwa.



![BitBanana](assets/fr/02.webp)



Muri BitBanana, kanda "GUHUZA NODE", ushireko kode ya QR canke ushireko URI. Wemerere kamera, hanyuma usuzume aderesi .onion yerekanwa imbere yo kwemeza.



**Umuco w'ishimikiro** guhuza



Niwakoresha Core Lightning (CLN) aho gukoresha LND, inzira iguma ari imwe, URI `clngrpc://` irimwo ivyemezo vya TLS bihurikiyeko. Core Lightning ishigikira BOLT12 (ibitanga), ishoboza gukoresha invoice n'ukwishura gusubiramwo bitaboneka kuri LND.



**Ihuzwa ata nzira y'umuntu ku giti ciwe (LNbits/yakira)**



Niba udafise urudodo rw’umuravyo, BitBanana irashobora kwifatanya n’ibikorwa vyakira abashitsi biciye kuri LndHub (umurongo ukoreshwa na BlueWallet na LNbits) canke Nostr Wallet Guhuza (NWC). Iyumvire: ubu buryo bukora mu buryo bwo kubika (servisi irakira amahera yawe) n’ibikorwa bike. Ntuzoshobora gucunga imirongo canke gutunganya amafaranga y’urugendo, kandi uzoshobora gusa kohereza no kwakira amafaranga y’umuravyo.



Ku bindi bisobanuro ku LNbits canke Nostr Wallet Connect, urashobora kuraba inyigisho zacu zitandukanye:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Gukoresha buri musi



### Interface nyamukuru



Igishushanyo c’imbere kigaragaza umubare wawe w’umuravyo, n’urutonde ruri hejuru ibubamfu rutanga uburenganzira bwo gushika ku bice bikurikira: Imirongo, Inzira, Ikimenyetso/Igenzura, Amanode, Abahuza, Amategeko, Gusubiza inyuma. Igishushanyo c'isaha (hejuru iburyo) kigurura amateka y'ibikorwa. Ubuto "Send" na "Receive" buri musi buragufasha kohereza no kwakira ama satoshis yawe.



![BitBanana](assets/fr/05.webp)



### Imiravyo na on-chain vyishyurwa



![BitBanana](assets/fr/10.webp)



**Ohereza amahera:** Kanda buto ya "Ohereza" uri ku rubuga rw'intango. Igikoresho co kwishura (ibubamfu) kiguha uburenganzira bwo gushiramwo aderesi canke amakuru y'ukwishura mu kibanza "Address canke amakuru y'ukwishura", hakaba hariho igikoresho co gupima QR hejuru iburyo kugira ngo ubone amakode. Ushobora kandi guhitamwo umuntu ubitse mu gice c’Ibintu kugira ngo wirinde gucapura igihe cose.



BitBanana yemera mu buryo bw’ubwenge uburyo bwose bwo kwishura: invoice za kera z’umuravyo (imirongo y’inyuguti itangura na `lnbc`), umuravyo Address (uburyo bwa imeyili nk’ubwo `utilisateur@domaine.com`), LNURL-amakode y’ukwishura ku kwishura guhinduka, LNURL-gukuraho ataco akora, ku rufunguzo rwa bose rwa Lightning ata n'inyandiko y'imbere. Porogaramu ihita ikora ingingo zikenewe za LNURL mu nyuma.



Iyo invoice imaze gushirwako, BitBanana yerekana amakuru yose: umubare nyawo, amafaranga y’urugendo agereranywa, insobanuro y’ukwishurwa (niba itangwa n’uwuyironka), n’itariki invoice izoherako. Inyuma y’ukwemezwa, amahera arungikwa biciye ku mihora yawe ya Lightning. Ushobora rero kubona inzira yafashwe hop ku hop n’amahera vyishyuwe vy’ukuri mu makuru y’ugucuruza.



**Kwakira amahera:** Kanda kuri buto ya "Kwakira". Igihitamwo (igicapo c'iburyo) kigufasha guhitamwo hagati ya Lightning (ukwishyura ubwo nyene biciye ku mihora yawe) na On-Chain. Ku bijanye n’ikimenyetso c’uko Lightning igura, shiramwo amahera wipfuza muri satoshis (canke usige kuri 0 kugira ngo ureme invoice ata n’imwe idahinduka kugira ngo uwuyitanga ashobore kuyiheza), hanyuma wongereko insobanuro y’ubusa kugira ngo iboneke kuri invoice. BitBanana ica itanga invoice y’umuravyo irimwo kode ya QR yo gucapura. Ushobora kandi gukopa iyo fagitire nk’inyandiko maze ukayirungika kuri e-mail. Igihe nyene umuntu yishuye, itangazo ry’ugusunika riragumenyesha maze iyo nzira igaca iboneka ubwo nyene muri kahise n’ibintu vyose birimwo.



### Imirongo n'inzira



![BitBanana](assets/fr/06.webp)



Igice ca "Imirongo" kigaragaza ubushobozi bwawe bwo kohereza/kwakira kandi kigatanga urutonde rw'imirongo yawe ifise amashusho yihariye. Buri nzira yerekana amahera yayo agabanywa hagati y’amahera yo mu karere n’ayo kure. Kora ku murongo kugira ngo ubone amakuru yose n’ibikorwa (gufunga, guhindura amafaranga y’inzira). Utudodo dutatu turi hejuru iburyo dutanga uburenganzira bwo gukoresha "Rebalance" kugira ngo wongere ushiremwo amahera y'imirongo yawe. Buto "+" ifungura umurongo mushasha.



Igice c’Inzira (igicapo co hagati) kigaragaza amafaranga yinjiye mu gutanga amakuru hakurikijwe igihe (1D, 1W, 1M, 3M, 6M, 1Y) n’amateka y’ivyoherezwa kugira ngo ukore neza ingamba zawe.



Sign/Verify (igicapo c'iburyo) kigufasha gusinya/kugenzura ubutumwa mu buryo bw'ibanga kugira ngo werekane ko ugenzura node.



### Ivyiyumviro vyinshi n'imirongo



![BitBanana](assets/fr/07.webp)



**Manage Nodes**: itanga urutonde rw'ibice vyawe, n'amabuto yo kwongerako n'amaboko, gucapura QR, canke guhindura hagati y'ibice. Cane cane, ushobora gushinga ubwoko butandukanye bw’uguhuza ku nzira imwe: LAN, VPN canke Tor.



**Gucungera Abagenzi**: ibika abagenzi bawe ba Lightning kugira ngo wishyure vuba.



**Imiterere**: guhindura amafaranga, ururimi, amashusho. Igice c’umutekano n’ubuzima bwite: Gufunga porogarama (PIN/biometrics), Guhisha uburinganire (uburyo bwo kwihisha), Tor (ukumenyekana kwa IP). Gutunganya ibiciro, abatohoji b'amabarabara, abagereranya amafaranga y'ibihe.



## Inyungu n'aho bigarukira



**Ibihambaye:**




- Ugutembera kwose: kugenzura urudodo rwawe rw'umuravyo uri aho hose
- Ibikorwa vyose: kwishura (LNURL, Umuravyo Address, BOLT 12), gucunga umurongo, kugenzura ibiceri, iminara y’ibarabara, ama-node menshi
- Umutekano: PIN/biometrics, uburyo bwo kwiba, PIN y'ivyihutirwa, Tor kavukire, guhagarika ifoto
- Ubuntu, inkomoko yuguruye (MIT), nta makomisiyo, nta kwegeranya amakuru



**Imipaka:**




- Bisaba umuravyo ukora (canke LNbits mu buryo bwo kubika)
- Nta verisiyo ya iOS yateguwe
- Gukingira uburenganzira bwo gukoresha telefone ni ikintu gihambaye cane (umuyobozi wa macaroon = uburenganzira bwo gukoresha node yose)



## Ibikorwa vyiza



**Umutekano:**




- Gukoresha PIN/ibiyometrike gufunga (kubuza kwinjira ata wemerewe ku nzira)
- Gushiraho PIN y'Ivyihutirwa (ikuraho amakuru y'agaciro mu gihe habaye uguhatirwa)
- Ntukigere usangira URI yawe yo kwinjira canke macaroon
- Uburyo bwo kwiba mu bidukikije vy'urwanko



**Injira:**




- VPN mesh (Urugero rw'umurizo, ZeroTier): ni ugusenyera ku mugozi umwe hagati y'umuvuduko n'umutekano
- Tor: ibanga ryinshi, igihe kinini
- Clearnet: kwirinda kiretse bikenewe (ugushirwa ahabona kwa IP, gufungura ivyuho)



### Gusubiza inyuma no gusubizaho



Ubwa nyuma, hariho "Backup" menu, ishobora kugufasha kubika ama configurations yawe kugira ngo telefone wimuke canke usubire gushiramwo.



![BitBanana](assets/fr/08.webp)



**Igihambaye:** Ivyo gusubiza inyuma NTIBIRIMWO seed canke ibisubizo vy'imirongo (bizokorwa ku node). Irimwo: imiterere y’ibihimba (amaderesi, ivyemezo, amakaroni), amakete, abahuza, amaparametere. Buto ya Restore iragufasha kwinjiza ububiko busanzweho. Kwemeza birakenewe imbere yo kubika.



![BitBanana](assets/fr/09.webp)



Injira ijambobanga ry’ibanga (ibarabara ry’iburyo). Sisitemu ifungura igihitamwo dosiye (igicapo c'ibubamfu) kugira ngo ubike `BitBananaBackup_2025-XX-XX.dat`. Kwemeza "Igisubizo cakozwe".



**Umutekano:** Bika ivy’inyuma bifise amakuru (igicu c’umuntu ku giti ciwe, USB, NAS). Ntukigere usangira amadosiye canke amajambobanga. Gerageza gusubizaho ubudasiba. Ivyo bikoresho bisubiza amahuzu, si amahera.



## BitBanana na Zewu: Ni igiki gitandukanye?



Niba uriko urarondera porogarama zo kuri telefone ngendanwa zo gucunga urudodo rwa Lightning, birashoboka ko uzohura na Zeus, uburyo buzwi cane bwo gusubirira BitBanana. Udakunze BitBanana, yibanda gusa ku kugenzura kure y’uruzitiro ruriho, Zeus ifata uburyo burengeye ubw’abandi, itanga uburyo bubiri bwo gukora: uruzitiro rwa Lightning rwinjijwe mu buryo butaziguye mu gikorwa (uburyo bwinjijwemwo bufise LND) n’uguhuza kure n’uruzitiro rw’inyuma nka Bitna,.



Ivyo bikoresho bibiri bituma Zeus ikwegera cane cane abatangura bipfuza kugerageza Lightning ata bikorwa remezo vy’imbere. Uburyo bushizwemwo burashoboza gutangura ubwo nyene n’uruzitiro rwuzuye rwo kugendagenda, mu gihe abakoresha bateye imbere bashobora guhindukira bakaja ku guhuza kure iyo uruzitiro rwabo bwite rumaze gutunganirizwa. Zeus kandi irashigikira LND na Core Lightning ku bijanye n’uguhuza kure, nka BitBanana.



Ikindi ciza gikomeye ca Zeus ni uko ishobora gukoreshwa ku mbuga zitandukanye (iOS na Android), mu gihe BitBanana iguma ikoreshwa kuri Android gusa. Zeus kandi ishiramwo ibikorwa remezo vya Olympus LSP kugira ngo bishobore kwakira amahera ya Lightning biciye ku nzira zijanye n’igihe, uburyo bwo kugurisha ku bacuruzi, n’uburyo bwo guhindura amahera kugira ngo umuntu ashobore gucunga amahera.



Ariko rero, BitBanana iragumya inkomezi zayo zidasanzwe: interface yoroshe, ibereye, ubumenyi bwiza bw’abakoresha (UX) kubera ko yibanda cane ku gukoresha kure, n’uburyo bwo kwigisha bufise insobanuro zijanye n’ivyo umuntu avuga. Zeus itanga ibikorwa vyinshi, ariko bikaba bifise igiciro c’interface igoye cane. Iryo koraniro riguma ryiza cane cane ku bakoresha bipfuza kugenzura urudodo gusa bari kure, ata bikorwa vyo kurinda.



Kugira ngo umenye vyinshi ku vyerekeye Zewu, raba inyigisho zikurikira:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Iciyumviro



BitBanana ihindura telefone yawe y’ubuhinga bwa none Android ikaba urupapuro rwuzuye rwa Lightning, itanga ubuhinga butagira uko bungana ku bakoresha ama node. Iryo koraniro rifise ibikorwa vyose: ukwishura (imiterere yose), gucunga imirongo, kugenzura ibiceri, iminara y’ibarabara, ama-node menshi, afise umutekano wongerekanye (PIN/biometrics, Tor, PIN y’ivyihutirwa).



BitBanana igira ubusegaba bwose, nta makuru yegeranya kandi ntiyigera ihungabanya ibanga canke ubugenzuzi bw’amahera yawe. Kode y’inkomoko yuguruye (MIT) iremeza ko haba uguseruka.



## Ubutunzi



### Inyandiko zemewe




- [Urubuga rwa BitBanana](urubuga rwa BitBanana.app)
- [Inyandiko zuzuye](inyandiko.bitbanana.app)
- [Kode y'inkomoko ya GitHub]



### Gushiramwo




- [Iduka ry'imikino ya Google](ububiko/porogaramu/ibisobanuro?id=porogaramu.michaelwuensch.bitbanana)
- [F-Cold](imbuga z'ibitoke)