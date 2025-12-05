---
name: BIP47 - PayNym
description: Koresha kode yo kwishura ishobora gusubirwamwo kuri Ashigaru
---
![cover](assets/cover.webp)



Ikosa ribi cane ry’ubuzima bwite ushobora gukora kuri Bitcoin ni ugusubira gukoresha amaderesi. Igihe cose iyo aderesi imwe ironse amahera menshi, ivyo bihembo birahuzwa, bikaba bituma isi ibona ikarita y’ivyo ukoresha. Ni vyiza rero cane ko wama generate aderesi yihariye ku nkuru yose wakiriye. Ariko ku bikorwa bimwebimwe vya Bitcoin, ivyo si ikintu coroshe.



BIP47, yashikirijwe na Justus Ranvier mu 2015, itanga inyishu nziza cane kuri ico kibazo. Izana iciyumviro ca **kode yo kwishura ishobora gusubirwamwo**: ikimenyetso kidasanzwe gishoboza umubare hafi utagira aho ugarukira w’amahera yishurwa kuri onchain bitcoin, ata kwigera ukoresha aderesi. Biciye ku buryo bwo gukingira amakuru bushingiye ku guhinduranya ECDH (*Diffie-Hellman on elliptic curves*), igihe cose umuntu yishuye kuri kode imwe, agira aderesi y’ubusa, yihariye ku bijanye n’ubucuti buri hagati y’uwurungitse n’uwuronka.



![Image](assets/fr/01.webp)



Iryo hame rya BIP47 rishirwa mu ngiro cane cane na **PayNym**, ubuhinga bwa mbere bwateguwe na Samourai Wallet ubu bukaba bwatwawe na Ashigaru. Muri iyi nyigisho, turaza kuraba ingene wokoresha PayNym yawe, ugahana amakode y’ukwishyura n’umumenyeshamakuru no gukora amafaranga ataco ukoresheje aderesi.



Sinzoja mu bikorwa vy’ido n’ido vya BIP47 hano. Niba wifuza kwihweza cane iyo nkuru, ndagusavye urabe igice ca 6.6 c’amahugurwa yanje ya BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ibisabwa



Kugira ngo ukurikire iyi nyigisho, ivyo ukeneye vyose ni wallet kuri app ya Ashigaru. Niba utazi uko woshobora gukura, gusuzuma, gushiramwo porogarama canke gukora wallet, ndagusavye ko wobanza kuraba iyi nyigisho:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Gusaba PayNym



Intambwe ya mbere ni ugusaba PayNym yawe. Ivyo bikorwa bikeneye gukorwa rimwe gusa kuri wallet. Ifatanya kode yawe yo kwishura BIP47 iva kuri seed yawe (`PM...`) n'ikimenyetso kidasanzwe kijanye n'ugushirwa mu ngiro kwa PayNym. Ico kimenyetso kigufi kandi gishobora gusomwa neza gishobora rero gushikirizwa abaguha amakuru kugira ngo bishobore guhanahana amakuru, ataco bimaze gusangira kode ndende kandi yuzuye ya BIP47.



Kugira ngo ubikore, fyonda ku ishusho yawe ya PayNym iri hejuru ibubamfu bw'ibarabara, hanyuma ukande kuri kode yawe yo kwishura `PM...`.



![Image](assets/fr/02.webp)



Hanyuma ukande ku tudodo dutoduto dutatu turi hejuru iburyo, hanyuma uhitemwo `Claim PayNym`.



![Image](assets/fr/03.webp)



Wemeze ukanda kuri buto ya `KUSABA PAYNYM YAWE`.



![Image](assets/fr/04.webp)



Vugurura urupapuro: ID yawe ya PayNym ubu igaragara munsi y’ishusho yawe, hejuru gato ya kode yawe yo kwishura BIP47.



![Image](assets/fr/05.webp)



PayNym yawe ubu irakora kandi yiteguye gukoreshwa mu bikorwa vyawe vya mbere vya BIP47.



## Huza n'umuntu



Hari ubwoko bubiri bw'ihuriro hagati ya PayNym: **kurikira** na **ihuriro**. Ivyo `gukurikira` ni ubuntu rwose. Ishinga uruja n’uruza hagati ya PayNym zibiri biciye kuri Soroban, ubuhinga bwo guhanahana amakuru bushingiye kuri Tor bwateguwe n’umugwi wa Samourai kandi bwemewe na Ashigaru. Iryo huriro rituma abakoresha babiri bakurikirana bashobora guhana amakuru mu mwiherero, cane cane guhuza ibikorwa vy’ubufatanye nka Stowaway canke StonewallX2, ivyo tuzobiraba mu yindi nyigisho. Iyi ntambwe ni iya PayNym kandi ntabwo iri mu masezerano ya BIP47.



![Image](assets/fr/06.webp)



Igikorwa kijanye n'uguhuza (`guhuza`), ku rundi ruhande, gisaba ugucuruza kwa on-chain. Bigizwe no gukora igikorwa co kumenyesha nk'uko bisobanurwa muri BIP47. Iryo koraniro rya Bitcoin ririmwo amakuru y’imbere mu gisohoka ca `OP_RETURN`, gishinga umurongo w’itumanaho hagati y’uwutanga n’uwuronka. Uhereye kuri uwo muhora, uwuriha azoshobora generate amaderesi yihariye yo kwakira amahera yose yishuye, kandi uwuyakira azomenyeshwa ivyo vyishyurwa, kandi azoshobora generate imfunguruzo z’ibanga zijanye n’ayo maderesi kugira ngo azokoreshe ayo mahera mu nyuma.



Iryo soko ry’imenyekanisha rifise igiciro: amahera ya mining na 546 sats yoherezwa kuri aderesi y’imenyekanisha y’uwuyakira kugira ngo yerekane ko hariho uguhuza. Iyo iyo nzira imaze gushingwa, umubare hafi udahera w’amahera ushobora kwishurwa biciye kuri BIP47.



Muri make:




- follow": ku buntu, ishinga ubutumwa bushingiye ku nzira ya Soroban, ngirakamaro ku bikoresho vya Ashigaru vyo gukorana;
- `Connect`: chargeable, ikora igikorwa co kumenyesha BIP47 kugira ngo ikoreshe umurongo hagati y'uwutanga n'uwuronka.



Kugira ngo ukoreshe PayNym, utegerezwa kubanza *ukuyikurikira*. Iyi ni intambwe ya mbere imbere yo gushinga uruja n’uruza rwa BIP47. Reka tuvuge ko ushaka kohereza amafaranga asubiramwo kuri PayNym `+ivyo utanga10`.



Genda kuri paji yawe ya PayNym kuri Ashigaru, hanyuma ukande kuri buto ya `+` iri musi iburyo bw'ibarabara.



![Image](assets/fr/07.webp)



Ushobora rero gushiramwo kode yuzuye y’ukwishyura kw’uwuronka, canke ugacapura kode yiwe ya QR.



![Image](assets/fr/08.webp)



Niba ufise gusa indangamuntu yiwe y’ukwishura, genda kuri [Paynym.rs](https://paynym.rs/) uronke kode ya QR ijana n’iyindi kode yiwe yo kwishura.



![Image](assets/fr/09.webp)



Umaze gucapura kode ya QR, ukande kuri buto ya `FOLLOW` kugira ukurikire PayNym.



![Image](assets/fr/10.webp)



Igikorwa kijanye n'ugukurikirana` kirahagije ku bikorwa vy'ubufatanye (*cahoots*). Ariko rero, kugira ngo wohereze amafaranga BIP47, ukeneye gushinga uruja n’uruza: ukande kuri `CONNECT` kugira ngo ukore igikorwa co kumenyesha.



![Image](assets/fr/11.webp)



Ivyo bimenyetso bica bimenyeshwa ku rubuga. Rindira gushika ifise n’imiburiburi icemezo kimwe imbere y’uko utanga amahera yawe ya mbere.



![Image](assets/fr/12.webp)



## Gukora BIP47 kwishura



Ubu uhuye n’uwukwakira kandi urashobora kohereza amahera kuri aderesi yihariye, ihita ivugwa hakoreshejwe umurongo wa BIP47, ataco ubanza guhanahana n’uwukwakira.



Kuva kuri page yawe nyamukuru ya PayNym, fyonda ku muntu wipfuza kohereza amahera.



![Image](assets/fr/13.webp)



Hejuru iburyo bw’ibarabara, fyonda ku kimenyetso c’umwampi.



![Image](assets/fr/14.webp)



Injira amahera azorungikwa. Ntukeneye kwinjiza aderesi y'ukwakira: izokwinjira ubwayo hakoreshejwe porotokole ya BIP47.



![Image](assets/fr/15.webp)



Suzuma neza amakuru yerekeye ivyo ugurisha, harimwo n’amahera, hanyuma ukure umwampi w’icatsi kibisi uri musi y’ibarabara kugira ngo ushireko umukono wongere utangaze ivyo ugurisha.



![Image](assets/fr/16.webp)



Ivyo bikorwa vyarungitswe.



![Image](assets/fr/17.webp)



Muri aka karorero, amahera yashizwe ku yindi nkweto yanje ya PayNym. Nshobora rero kubona ko yashitse ku yindi Ashigaru wallet yanje, ata n’aderesi n’imwe yahinduwe n’amaboko: hakoreshejwe ikimenyetso ca PayNym gusa.



![Image](assets/fr/18.webp)



Ubu urazi gukoresha amakode y’ukwishura ashobora gusubirwamwo BIP47 kubera ugushirwa mu ngiro kwa PayNym kuri porogarama ya Ashigaru. Ubu ushobora gusangira iyo kode yo kwishura n’umuntu wese ashaka kukurungikira amahera (na cane cane amahera asubiramwo). Ushobora kandi gutangaza ID yawe ya PayNym ku rubuga rwawe canke ku mbuga ngurukanabumenyi kugira ngo uronke intererano.



Kugira ngo urushirize kumenya neza iyi protocole, utahure mu buryo burambuye ingene ikora n’ingaruka zayo ku bijanye n’ibanga, ndagusavye cane ko wofata inyigisho yanje ya BTC 204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
