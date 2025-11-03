---
name: Ente Auth
description: Inkomoko yuguruye, iherezo-ku-iherezo ry'ukwemeza 2FA
---
![cover](assets/cover.webp)



Ivyemezo bibiri (2FA) vyacitse ikintu gihambaye cane kugira ngo umuntu ashobore gukingira amakonti yacu yo kuri Internet. Uretse ijambobanga ryawe risanzwe, risaba kode y’igihe gito, akenshi ikaba iterwa n’iporogarama yihariye. Ubwo buryo buzwi kw’izina rya TOTP (Time-Based One-Time Password), buratanga icemezo c’uko naho ijambobanga ryawe ryoba ryarashizwe mu kaga, uwugutera atazoshobora kwinjira muri konti yawe atagira ico kintu ca kabiri, gisubirwamwo buri masegonda 30.



Ariko rero, guhitamwo porogarama nziza yo kwemeza ko umuntu ari uwundi si ikintu c’ubusa. Google Authenticator, naho izwi cane, irafise aho igarukira: kode y’umunyagihugu idashobora gusuzumwa, gukorana n’ibindi ata n’iherezo ry’iherezo, n’ingorane zo gutakaza kode zose iyo habaye ingorane kuri telefone yawe. Ibindi bisubizo, nka Authy, bisaba inomero ya telefone kandi ntibitanga ibanga ryose.



**Ente Auth** igaragara nk’iyindi nzira y’ubuhinga bwa none, itekanye. Iyi porogaramu y’ubuntu, yuguruye, ikoreshwa ku mbuga zitandukanye, yateguwe n’umugwi uri inyuma ya [Ente Photos](https://ente.io), itanga ububiko bw’ibicu bushingiye ku mpera ku mpera n’uguhuza ata nkomanzi hagati y’ibikoresho vyawe vyose. Mu buryo butandukanye n’imiti y’abanyagihugu, Ente Auth iguha ububasha bwose ku makode yawe y’ukwemeza ataco ihinduye ku buzima bwite bwawe.



Muri iyi nyigisho, tuzokwereka intambwe ku yindi ingene woshiramwo no gukoresha Ente Auth, n’igituma uwo muti utandukanye n’abagenzuzi ba kera.



## Gutanga Ente Auth



Ente Auth yateguwe n’umugwi uri inyuma ya Ente Photos, ubuhinga bwo kubika amafoto bushingiye ku mpera kugeza ku mpera kandi bufise ubuzima bwite. Mu buryo bubereye filozofiya ya Ente ("Ente" bisobanura "ivyanje" mu rurimi rw'ikimalayalam, bigereranya ububasha ku makuru yawe), Ente Auth yari yagenewe gusubiza abakoresha ububasha bwose ku makode yabo y'ukwemeza ibintu bibiri.



### Ibirango nyamukuru



**Amakode ya TOTP asanzwe**: Ente Auth itanga amakode y’igihe gito ahuye n’ibikorwa vyinshi (GitHub, Google, Binance, ProtonMail, n’ibindi). Ushobora kwongerako amakonti menshi ya 2FA nk’uko ubikeneye, kandi iyo porogarama ibara amakode ishingiye ku mabanga yatanzwe.



**Iherezo ku mpera y'igicu gipfutse**: Amakode yawe abikwa neza kuri internet. Ni wewe wenyene ushobora kubifungura - urufunguzo rwo kubifungura rukomoka ku jambobanga ryawe kandi ruzwi na wewe gusa. Ente (server) nta bumenyi afise ku mabanga yawe, canke mbere ku mazina ya konti yawe, kuko vyose bishizwe mu nzira ku ruhande rw’umukiriya hakoreshejwe ubuhinga bwo kwubaka ata bumenyi bufise.



**Gukorana n’ibikoresho vyinshi**: Ushobora gushiramwo Ente Auth ku bikoresho vyinshi (smartphone, tablette, mudasobwa) maze ukabona ama code yawe kuri vyose. Impinduka zose zica zikwiragizwa ubwo nyene kandi zica zikwiragizwa ku bindi bikoresho vyawe biciye ku gicu gipfutse, bikaguha ubushobozi bwo guhindura cane ibikorwa vyawe vya misi yose.



**Minimalist, intuitive Interface**: Porogaramu itanga Interface itunganye, yoroshe kwiga mbere n’abatari abahinga mu vy’ubuhinga. Konti za 2FA zigaragazwa n’izina rya serivisi, inzira yawe yo kwinjiramwo na kode y’imirongo 6, ivugururwa mu gihe nyaco. Ente Auth nayo yerekana kode ikurikira amasegonda makeyi imbere y’igihe kugira ngo ntifatwe n’uguhera kw’igihe.



**Inkomoko yuguruye kandi yagenzuwe**: Kode y'inkomoko ya Ente Auth ni [igaragara kuri GitHub](https://github.com/ente-io/auth) iri munsi y'uruhusha rwa AGPL v3.0. Umuhinguzi wese arashobora kuyigenzura kugira ngo asuzume ko ata makosa canke inyifato mbi. Ivyo bikoresho vy’ubuhinga bwa none vyashizwe mu ngiro vyakozweko [igenzura ry’inyuma ryigenga](https://ente.io/blog/cryptography-audit/), ikimenyetso c’uburemere bw’umutekano w’ivyo bikoresho.



### Inyungu n'aho bigarukira



**Inyungu:**




- Ubuzima bwite bushingiye ku guhingura n'ububiko buva ku mpera kugeza ku mpera
- Guhuza neza hagati y'ibikoresho vyawe vyose
- Kode y'inkomoko yuguruye igenzurwa
- Interface igaragara, umukoresha asobanutse Interface.
- Gusubiza inyuma ubwavyo kugira ngo ntutakaze amakode
- Iboneka ku mbuga zose (telefone n'ibiro)



**Imipaka:**




- Ihuriro rya interineti rikenewe kugira ngo bihuzwe
- Abakoresha bateye imbere bashobora guhitamwo 100% inyishu zitari kuri internet nka Aegis (Android gusa)
- Ivya vuba cane bigereranywa n'imiti yashinzwe



## Gushiramwo



Ente Auth iraboneka ku mbuga nyinshi zizwi cane. Ushobora gukura iyo porogarama kuri [urubuga rwemewe](https://ente.io/auth) canke mu maduka yemewe.



![Installation d'Ente Auth](assets/fr/01.webp)



*Paje yo gukuraho Ente Auth ifise ama platforms yose ariho*



### Android


Ufise amahitamwo menshi:




- Iduka rya Google Play**: Rondera "Ente Auth" kugira ngo ushireho
- F-Droid**: Iboneka mu rutonde rw'ibikoresho vya Android, bifise icemezo c'ubwubatsi bugenzuwe kandi nta birimwo vy'umunyagihugu
- Gushiramwo n'amaboko**: Amadosiye ya APK ashobora gukurwa kuri [paji ya GitHub y'umugambi](https://github.com/ente-io/auth/releases) n'imenyekanisha ryinjijwe ry'amaverisiyo mashasha



### iOS (ifone/ipadi)


Shiraho Ente Auth uhereye kuri Apple App Store mu kurondera izina rya porogarama. Iyi porogaramu ya iOS ishobora kandi gukoreshwa kuri Mac zifise ama chips ya Apple Silicon (M1/M2) biciye ku bubiko bwa Mac App Store.



### Mudasobwa (amadirisha, macOS, Linux)


Ente Auth itanga ibikorwa vy'ibiro vy'akavukire. Sura [ente.io/gukuraho](https://ente.io/gukuraho) canke [Igice ca GitHub]





- Windows**: Igikoresho co gushiramwo EXE kiratangwa
- macOS**: Kurura-no-gutera ishusho ya disiki ya DMG mu bikorwa
- Linux**: Uburyo bwinshi buraboneka (Ishusho y'ikoreshwa, .deb kuri Debian/Ubuntu, .rpm kuri Fedora/Inkofero itukura)



**Iciyumviro:** Iyi nyigisho ishingiye kuri Ente Auth v4.4.4 n’izindi zikurikira. Verisiyo za kera zishobora kuba zifise ututandukaniro dutoduto twa Interface.



### Interface Urubuga


Ata gushiramwo, urashobora gushika ku makode yawe biciye kuri [auth.ente.io](https://auth.ente.io) ukoresheje umucukumbuzi uwo ari wo wose. Interface web igarukira ku kuraba amakode (akenewe mu gutorera umuti ingorane), kuko kwongerako amakonti bisaba porogarama yo kuri telefone ngendanwa canke yo kuri mudasobwa kubera imvo z’umutekano.



## Itunganywa rya mbere



### Gukora konti



Iyo utanguye Ente Auth, ufise uburyo bubiri:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Ente Auth igicapo c'inzu n'amahitamwo yo kurema konti*



**Ufise konti (ni vyiza)**: Hitamwo "Rema konti" hanyuma winjize e-mail yawe Address n'ijambobanga. **Igihambaye**: iri jambobanga rikora nk'ijambobanga ry'ingenzi ryo gupfuka amakuru yawe. Hitamwo ijambobanga rikomeye kandi ridasanzwe, kuko ata buryo busanzwe bwo gusubiramwo ata makuru atakaye. Iyo uyishize ahantu hatabereye, amakuru yawe yashizwemwo amakuru azoba atazosubira kuronka.



**Offline mode**: Hitamwo "Koresha ata backups" kugira ngo ukoreshe porogaramu mu karere ata gicu. Muri ubu buryo, amakode yawe aguma ku gikoresho, ariko uzokenera kuyarungika hanze n’amaboko kugira ngo ntuyatakaze.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Uburyo bwo kugenzura imeyili no guhingura urufunguzo rwo gusubiza amajambo 24*



Igenzura ry’iposita rishobora gusabwa kugira ngo ryemeze ko konti yashizweho kandi bishoboze gusubira ku gikoresho gishasha. Ente Auth izoguha kandi urufunguzo rwo gusubiza amajambo 24 (rushingiye ku buryo bwa BIP39). **Ni ngombwa ko ubika urufunguzo** ahantu hatagira umutekano: ni bwo buryo bwonyene bwo kugarura amakuru yawe iyo wibagiwe ijambobanga ryawe.



### Umutekano wo mu karere



Ndabahimiriza cane gushoboza uburinzi bw’aho hantu hakoreshejwe kode canke biometrics. Genda kuri **Ivyagezwe → Umutekano → Igikoresho co gufunga** hanyuma ushireho :





- Gufungura Biometric**: Indangamuntu yo mu maso, urutoke bivanye n'ubushobozi bw'igikoresho cawe
- PIN/ijambobanga ry'ikoreshwa**
- Gufunga kwikora**: nk'akarorero. "Ubwo nyene" canke inyuma y'amasegonda 30 ataco ukora



Ubwo burinzi burabuza umuntu kuronka amakode yawe ata wemerewe iyo aronse uburenganzira bwo kuronka telefone yawe ifunguye. Zirikana ko iyo nzira ari intambamyi y’inyongera: amakuru yawe aguma apfutse kuva ku mpera kugeza ku mpera naho ata n’ubwo burinzi.



## Kwongerako konti za 2FA



### Uburyo busanzwe



Kugira ngo wongereko konti nshasha ya 2FA, reka dufate akarorero nyako ko gukoresha 2FA kuri Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Interface nyamukuru ya Ente Auth yiteguye kwongerako konti ya mbere ya 2FA*



**Uruhande rwa Serivisi (Bull Bitcoin)**: Injira muri konti yawe ya Bull Bitcoin, uje ku mirongo y’umutekano, maze ushoboze kwemeza ibintu bibiri.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Inka Bitcoin* amategeko y'umutekano



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Ihitamwo ryo gushobora kwemeza ibintu bibiri kuri Bull Bitcoin*



Iyo serivisi izoca yerekana kode ya QR kugira ngo ushobore gucapura ukoresheje porogarama yawe yo kwemeza:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*QR code yakozwe na Bull Bitcoin kugira ngo ikoreshe scanner n'ikimenyetso cawe co kwemeza*



**Muri Ente Auth**: Fyonda kuri "Injira urufunguzo rwo gutegura" hanyuma ushireko kode ya QR yerekanwa na Bull Bitcoin. Ente Auth izoca imenya iyo konti maze yuzuze ivyanditswe.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Gutunganya amakuru ya konti ya Bull Bitcoin muri Ente Auth*



Ushobora guhindura izina rya serivisi n’aho winjira kugira ngo bikorohere kuronka. Ivyagezwe vy'imbere (SHA1 algorithm, igihe c'imyaka 30, imibare 6) muri rusangi biragororotse ku buryo busanzwe.



**Ukwemeza ku ruhande rwa serivisi**: Subira kuri Bull Bitcoin winjize kode y'imirongo 6 yashizweho na Ente Auth kugira ngo uheze gukoresha.



![Saisie du code 2FA](assets/fr/09.webp)



*Injira kode yashizweho na Ente Auth kugira ngo wemeze 2FA* ikoreshwa



![2FA activée](assets/fr/10.webp)



*Ivyemezo vy'ugukora neza kwa 2FA kuri Bull Bitcoin*



**Amakode yo gusubiza inyuma**: Bull Bitcoin izoguha amakode yo gusubiza inyuma. **Bibike ahantu hatagira umutekano, bitandukanye n'uwukwemeza.**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Ihitamwo ry'amakode y'ivyihutirwa ya generate ku Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Urutonde rw'amakode yo gusubirana yo kubika ahantu heza*



### Itunganywa n'uburongozi



Ente Auth itanga ibintu vyinshi bikora:



**Quick Copy**: Kanda kuri code kugira ngo uyikope ubwayo ku gicapo.



**Ibikorwa bishingiye ku mirongo**: Kanda kandi ufate (canke ukande iburyo ku biro) kugira ngo uhindure, usibe, usangire canke ushireko ikintu.



**Ibimenyetso n'ugushaka**: Gutunganya amakonti yawe n'ibimenyetso (vy'umuntu ku giti ciwe/ivy'umwuga, hakurikijwe urugero rw'ibikorwa) hanyuma ukoreshe umurongo w'ugushaka kugira ngo ucungurure ningoga.



![Création d'un tag](assets/fr/17.webp)



*Uburyo bwo kurema Tag: urutonde rw'ibivugwa n'ikiganiro co kurema*



![Tag appliqué](assets/fr/18.webp)



*Ikimenyetso "Bitcoin" cashizweho neza kuri konti ya Bull Bitcoin*



**Ibishushanyo vyikora**: Igiharuro cose gishobora kwerekanwa n’ikimenyetso ca serivisi, bivuye ku gushiramwo [Ibishushanyo vyoroshe] vy’ibishushanyo (https://simpleicons.org/).



**Gusangira mu mutekano w’igihe gito**: Ikintu kidasanzwe ca Ente Auth, gusangira mu mutekano bigufasha gutanga kode ya 2FA ku mugenzi wawe utamenyesheje ibanga ry’imbere. generate uruja n’uruza rwuzuye rukora iminota 2, 5 canke 10 - uwuronka abona kode mu gihe nyaco, ariko ntashobora kuyirungika hanze canke gushika ku makuru ya konti. Ubwo buryo ni bwiza cane mu gufasha mu vy’ubuhinga canke mu gukorana mu gihe gito, butanga urugero rw’umutekano rudashoboka n’ugufata ifoto yoroshe canke ubutumwa bwo mu nyandiko.



![Partage sécurisé](assets/fr/19.webp)



*Interface gusangira umutekano w'igihe gito: hitamwo igihe (iminota 5)*



**Gusohora/kwinjiza mu mutekano**: Ente Auth ishobora kugufasha kwohereza hanze amakode yawe mu zindi porogaramu, canke ukayazana uvuye muri Google Authenticator n'ibindi bisubizo. Ivyoherezwa hanze bica muri dosiye canke kode ya QR, bikaba vyemeza ko amakuru yawe ashobora gutwara ataco akora ku mutekano.



**Urufunguzo rwo gusubizaho BIP39**: Porogaramu ihita itanga ijambo ry’ugusubizaho ry’amajambo 24 hakurikijwe ingingo ngenderwako ya BIP39 (Iciyumviro co Guteza imbere Bitcoin), isa n’amasakoshi y’amahera y’amahera. Iri jambo ni ryo rufunguzo rwawe rwo gusubirana, rikagufasha kugarura amakode yawe yose naho woba wibagiwe ijambobanga ryawe ry’ibanze.



## Gutunganya n'imiterere



Ente Auth itanga uburyo bwinshi bwo guhindura ibintu bishobora gushikwako biciye ku mitunganyirize y'ikoreshwa:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Incamake y'ibipimo biri muri Ente Auth*



### Ubuyobozi bwa konti n'amakuru



![Paramètres de sécurité](assets/fr/14.webp)



*Amahitamwo y'umutekano ateye imbere: kugenzura imeyili, kode ya PIN, ibiganiro bikora*



Amagenamiterere y'umutekano araguha uburenganzira bwo :




- Gushoboza kugenzura imeyili ku mahuriro mashasha
- Gukoresha urufunguzo rw'ibanga
- Reba ibihe bikora ku bikoresho vyawe bitandukanye
- Gushinga kode ya PIN canke ubuhinga bwo gupima ubuzima



### Interface n'uburyo bwo kuyikoresha



![Paramètres généraux](assets/fr/15.webp)



*Imirongo ya Interface n'uguhindura ibikorwa*



Amagenamiterere rusangi arimwo :




- Ururimi**: Interface indimi nyinshi
- Iyerekanwa**: Ibishushanyo binini, uburyo bukomeye
- Ubuzima bwite**: Hisha amakode, gushakisha vyihuse
- Telemetry**: Gutanga raporo y'ikosa (bishobora guhagarara)



## Gusubiza inyuma no guhuza



### Uko gupfuka bikora



Iyo wongeyeko konti ifise konti ya Ente ihuye, iyo porogarama ica ihita ipfuka ayo makuru y’agaciro mu karere ikoresheje urufunguzo rwawe nyamukuru (rukomoka ku jambobanga ryawe). Amakuru yashizwemwo amakuru aca yoherezwa kuri server ya Ente kugira ngo abikwe.



Kubera ubu buryo, ububiko bw’amakode yawe bufise igicu gifise amakuru y’iherezo buhoraho. Niwatakaza igikoresho cawe, gusa wongere ushiremwo Ente Auth maze wongere uyihuze: iyo porogarama izokwikurako kandi ifungure amakode yawe yose.



### Guhuza ibikoresho vyinshi



Iyo ukoresheje Ente Auth kuri telefone ngendanwa no kuri mudasobwa, ivyo wongereyeko canke ivyo uhinduye vyose ku gikoresho kimwe biraboneka mu masegonda makeyi ku kindi. Ukwo guhuza bica mu gicu ca Ente, ariko uko amakuru apfutse kuva ku mpera kugeza ku mpera, umukozi abona gusa ibirimwo bipfutse bitasomwa.



![Synchronisation mobile](assets/fr/16.webp)



*Iyerekanwa ry'uguhuza: iyo konti ya Bull Bitcoin ishobora gukoreshwa kuri telefone ngendanwa no kuri mudasobwa*



Gukorana n’ibindi ntaco bimaze: shiramwo Ente Auth kuri telefone yawe, winjiremwo ukoresheje amakuru yawe, maze amakode yawe yose ya 2FA (aha Bull Bitcoin) akaboneka ubwo nyene. Akarorero kari hejuru kerekana uguhuza neza hagati ya desktop na telefone ngendanwa - kode imwe ya Bull Bitcoin iraboneka ku bikoresho vyose bibiri.



Ku bijanye n’ibanga, nta Ente canke uwundi muntu afise uburenganzira bwo kuronka amabanga yawe ya 2FA. Mbere n’amakuru y’inyuma (ibimenyetso, amajambo, amazina y’ibikorwa) arashirwa mu nzira imbere y’uko yoherezwa. Ubu buhinga bwo kwubaka butagira ubumenyi buratuma ari wewe wenyene ushobora gusobanura amakode yawe.



### Ikoreshwa ritari kuri interineti



Gukorana n’ibindi bisaba Internet, ariko Ente Auth ikora neza cane ata n’imwe iri ku gikoresho cose, kuko amakuru yose abikwa aho hantu. Impinduka zitari ku murongo zishirwa ku murongo kandi zigahuzwa igihe nyene uruja n’uruza rusubiyeho.



## Umutekano n'ubuzima bwite



### Ivyemezo vy'ibanga



Ente Auth ishingiye ku gupfuka gukomeye kuva ku mpera kugeza ku mpera n’ubumenyi butagiramwo ubumenyi. Amakode yawe apfutse n’urufunguzo wewe wenyene ufise, ruva ku jambobanga ryawe ry’ingenzi ukoresheje ibikorwa vy’ugukura urufunguzo biteye imbere.



**Ubwubatsi butagira ubumenyi:** Ente ntishobora gushika ku makuru yawe. Mbere n’amakuru (amazina y’ibikorwa, ama tags, ama notes) arashirwa ku ruhande rw’umukiriya imbere y’uko yoherezwa. Ubwo buryo buratuma, iyo habaye igitero ku maserukira yawe canke iyo Leta isaba, Ente ishobora gutangaza gusa amakuru yashizwemwo amakuru adashobora gusomwa ata jambobanga ryawe.



**Ugushiramwo amakuru yo mu karere**: Ivyo gushiramwo amakuru bibera vyose ku gikoresho cawe imbere y’uko birungikwa mu gicu. Server za Ente zironka kandi zibika amakuru yashizwemwo gusa, ivyo bikaba bituma umuntu adashobora kuyaronka ata wemerewe, mbere n’abarongozi b’ibikorwa.



### Guseruka n'igenzura



Kubera ko kode ari [inkomoko yuguruye](https://github.com/ente-io/auth), umuryango urashobora kugenzura ko ata miryango y’inyuma iriho. Ente yaragize [igenzura ryinshi ry’inyuma](https://ente.io/blog/igenzura-ry’ubuhinga/) ryakozwe kugira ngo ryemeze umutekano w’ugushirwa mu ngiro kwayo:





- Cure53** (Ubudage): Igenzura ry'umutekano w'ibikoresho n'ubuhinga bwa none
- Porogaramu y'ikigereranyo** (Ubufaransa): Ubuhinga bwihariye bwo gukora amakuru y'ibanga
- Fallible** (Ubuhinde): Igerageza ryo kwinjira n'isesengura ry'ubugoyagoye



Ivyo bigenzura vyigenga, bikorwa n’amashirahamwe yemewe, biremeza ko ugushirwa mu ngiro kw’ubuhinga bwa none bwa Ente Auth buhuye n’imigenzo myiza y’umutekano kandi ko ata makosa akomeye afise.



### Amabwirizwa y'ubuzima bwite



Ente Auth ikoresha [akarorero k’ingingo ngenderwako y’ubuzima bwite](https://ente.io/ubuzima bwite/) ishingiye ku gukusanya amakuru makeyi. Amakuru akenewe cane kugira ngo iyo serivisi ikore ni yo yonyene abikwa: e-mail yawe Address yo kwemeza no gusubirana konti.



**Nta gukurikirana canke telemetry**: Bitandukanye n'ibikorwa vyinshi, Ente Auth nta n'imwe yegeranya ingero z'ikoreshwa, nta makuru yerekana impanuka, kandi nta makuru y'inyifato. Iryo koraniro rikora ata kwamamaza canke abakurikirana ivy’isesengura.



**Ukurikiza GDPR**: Ente yubahiriza bimwe bishitse Itegeko rusangi ry’Uburayi ryerekeye ugukingira amakuru. Ufise uburenganzira bwo kuronka, gukosora canke gufuta amakuru yawe igihe cose. Gusohora amakuru hanze](https://ente.io/take-control/) ni ugukanda gusa, kandi gukuraho konti yawe ubuziraherezo bikuraho amakuru yawe yose ku maserukira.



**Ububiko bushizwe ahantu hamwe, butekanye**: Amakuru yawe yashizwemwo amakuru asubirwamwo ku bigo 3 bitandukanye, mu bihugu 3 bitandukanye, bikaba vyemeza ko ushobora kuronka amakuru meza mu gihe wirinda kwizigira umurongo umwe w’igicu.



Ubucuruzi bwa Ente bushingiye kuri serivisi ya Ente Photos yishurwa, bikaba bidushoboza gutanga Ente Auth **ku buntu kandi ata n’aho bigarukira** ataco bihinduye ku buzima bwite bwawe mu guhindura amakuru yawe ngo abe amahera. Ubwo buryo buratuma iyo serivisi igumaho ata kwizigira kwamamaza canke gusubira kugurisha amakuru y’umuntu ku giti ciwe.



## Kugereranya n'ibindi bisubizo



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth igaragara nk’imwe mu nzira nkeyi zo guhuza ivyiza vyose: uguserukira kode y’inkomoko, gucungera igicu gipfutse n’uguhuza ibikorwa bitandukanye.



## Ibibazo vy'ikoreshwa ryiza



### Abakoresha ku giti cabo



Ente Auth ni nziza ku bantu bakunda umutekano bakoresha 2FA mu buryo butunganye. Ntuzosubira kwiganyira ku bijanye no gutakaza amakode yawe igihe uhindura telefone, canke ngo uhitemwo hagati y’ivyo ushobora gukoresha n’ivyo ushobora gukora.



### Ikoreshwa ry'umuryango n'ibikoresho vyinshi



Iyi app iraza mu vyo ikoresha iyo ukoresheje ibikoresho vyinshi. Ushobora kubika amakode yawe kuri telefone ngendanwa n’amatablette, canke ugasangira amakode amwe amwe y’umuryango (Netflix, igicu c’umuryango) mu buryo buhuye kandi butekanye.



### Ikoreshwa ry'umwuga



Ku matsinda acungera amakonti y'agaciro, Ente Auth irafasha gukorana mu gihe izigama umutekano, kubera ubuhinga bwayo bwo gusangira buteye imbere bushizwe mu gice ca "Ishirahamwe n'uburongozi".



## Ibikorwa vyiza





- Bika amakode yawe y’ivyihutirwa**: Bika amakode yo gusubirana atangwa na serivisi yose kure ya telefone yawe.





- Koresha ijambobanga ry’ingenzi rikomeye**: Ijambobanga ryawe ry’ingenzi rya Ente Auth ritegerezwa kuba ryihariye kandi rikomeye, kuko ririnda amakode yawe yose.





- Gukoresha uburinzi bwo mu karere**: Gutegura PIN canke biometrics kugira ngo ukinge umuntu ashobora gushika ku mubiri ata wemerewe.





- Ntuhindure birenze urugero**: Irinde guhindura ibintu biteye imbere bishobora gutuma udashobora gukorana neza.





- Gumana porogaramu iri ku gihe**: Ihindura ukosora amakosa y’umutekano kandi igatuma ikora neza.





- Igerageza ryo gusubizaho**: Rimwe na rimwe urabe ko ushobora gusubizaho amakode yawe ku kindi gikoresho.



## Iciyumviro



Ente Auth iserukira umuti w’iki gihe, wuzuye wo kwemeza ibintu bibiri. Mu guhuza umutekano, uguseruka n’ukworohereza gukoresha, iyi porogarama y’inkomoko yuguruye irahuza n’ivyo abakoresha basaba cane bakeneye ataco batakaje ku bijanye n’uburyo bwo gukoresha.



Udakunze inyishu z’abanyagihugu zigufunga mu bidukikije bitaboneka, Ente Auth iraguha ububasha bwo gusubira kugenzura amakuru yawe y’ukwemeza mu gihe ikurinda gutakaza mu mpanuka kubera amakuru yayo y’ububiko.



Waba uri umuntu ku giti ciwe arondera gucungera amakonti yawe bwite, canke umugwi ucungera uburyo bwo gushika ku bucuruzi, Ente Auth ni ihitamwo ryiza ryo guhindura uburyo bwawe bwo gucungera umutekano wa digitale ataco uhinduye ku buzima bwite.



## Ibikoresho n'infashanyo



### Inyandiko zemewe




- Urubuga rwemewe**: [ente.io/uburenganzira]
- Ikigo c'imfashanyo**: [imfashanyo.ente.io/ukwemeza](https://imfashanyo.ente.io/ukwemeza)
- Urubuga rw'ubuhinga**: [ente.io/urubuga](https://ente.io/urubuga)



### Kode y'inkomoko n'uguseruka




- GitHub**: [github.com/injira-io/uburenganzira](ubutumwa bw'ibanga/uburenganzira)
- Igenzura ry'ububiko**: [ente.io/urubuga/igenzura ry'ububiko](https://ente.io/urubuga/igenzura ry'ububiko)



### Umugyango




- Ugutahura**: [ugutahura.gg/z2YVKkycX3](https://ugutahura.gg/z2YVKkyc3)
- Reddit **: [Ikiganiro] (Ikiganiro)