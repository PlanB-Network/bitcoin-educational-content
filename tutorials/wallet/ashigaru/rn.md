---
name: Ashigaru
description: fork iva kuri Samourai Wallet kugira ngo ukingire, ucunge kandi uvange amafaranga yawe
---

![cover](assets/cover.webp)



Ashigaru ni porogaramu ya Bitcoin igendagenda wallet ikurikira umugambi wa Samourai Wallet, ariko mu buryo bushasha. Iyi porogaramu yavukiye mu gihe kinaka: muri Ndamukiza 2024, abashinze Samourai Wallet barafashwe n’ubutegetsi bwa Amerika, kandi ama server yabo arafatwa. Naho porogarama ya Samurai ubwayo yagumye ikoreshwa, ubu ntabwo igikoreshwa. Ashigaru ni verisiyo ya fork y’ubuntu ya Samurai Wallet, ibungabungwa n’umugwi utazwi kugira ngo ushireho ubudasiba bw’imikorere ya Samurai no kurinda filozofiya yayo y’intango: kurwanira ubuzima bwite n’ubusegaba bw’abakoresha Bitcoin.



Ashigaru afata vyinshi muri ADN ya Samourai: interface isa n’iyo, uburyo bugaragara bwo kwikingira, inkomoko yuguruye n’ukwibanda ku buzima bwite. Iyo kode ikwiragizwa hakurikijwe uruhusha rwa GNU GPLv3, rutuma umuntu wese ashobora gusuzuma, guhindura canke gusubira gukwiragiza iyo porogarama.



Porogaramu ya Ashigaru ishiramwo ibikoresho vy’ubuhinga bwa none vyo kubungabunga ibanga n’ugucungera ama UTXO yawe:




- Whirlpool**, ni porotokole ya coinjoin ishingiye kuri Zerolink, ishobora kugufasha guca amahuzu y’ivy’ubuhinga hagati y’injira n’isohoka ry’ibikorwa, utatakaje ubusegaba ku mahera yawe.
- PayNym**, ishira mu ngiro amakode yo kwishura ashobora gusubirwamwo (BIP47), ubu iserukira biciye ku buryo bw'ishusho "*Pepehash*".
- Ricochet**, ikintu congeramwo ibisimbuka vyo hagati ku bikorwa kugira ngo bibe bigoye gukurikirana.
- Kandi vy’ukuri ***Coin Control*** kugira uhitemwo, ushireko amazina y’ama UTXO yawe neza na neza.
- Batch Spending***, kugira ngo ugabanye ibiciro mu gukoranya amafaranga menshi mu gikorwa kimwe.
- **Stealth Mode**, ihisha porogarama iri kuri telefone yawe ngendanwa inyuma y’igikoresho co gutera imbere kugira ngo ntiyiboneke mu gihe c’isuzuma ry’umubiri rya telefone yawe.
- Ibikoresho vy’ugukoresha amahera biteye imbere kugira ngo ukoreshe neza ibanga ryawe (payjoin, stonewall...).
- Uburyo bwo gusubizaho bubereye hakoreshejwe ijambobanga BIP39.
- Uburyo bwo gutuma umuntu ahitamwo neza amafaranga y’ugucuruza.



![Image](assets/fr/01.webp)



Ashigaru rero igenewe abakoresha bazi ibibazo bijanye no gukurikirana amafaranga kuri Bitcoin. Waba uri umukoresha azi ubuzima bwite, umuhinga mu vy’ubuhinga bwa bitcoiner yiyemeje kwizigama, canke umuntu afise ingorane zo kwongerekana kw’ugucungera, iyi porogarama ya wallet iraguha ibikoresho ukeneye kugira ngo wongere ugenzure igikorwa cawe kuri Bitcoin.



Ashigaru iraboneka mu buryo bwa telefone ngendanwa biciye kuri app yayo, ivyo tuzobibona muri iyi nyigisho. Ariko kandi irashobora gukoreshwa kuri PC ifise ***Ashigaru Terminal***, ivyo tuzobimenyesha mu nyigisho izoza.



![Image](assets/fr/02.webp)



Muri iyi nyigisho, ndashaka kubamenyesha ikoreshwa ry’ishimikiro rya Ashigaru: gushiramwo, gufatanya na Dojo, gukora backup, kwakira no kohereza bitcoins. Ibikoresho biteye imbere bizokwerekanwa mu zindi nyigisho zihariye.



## 1. Ibisabwa kugira ngo umuntu abe Ashigaru



Iryo koraniro risaba ibintu bikeyi kugira ngo rikore neza. Mbere na mbere, si porogaramu iboneka mu maduka ya kera nka Google Play Store canke App Store. Ishiramwo n'amaboko kuri telefone yawe gusa ivuye muri dosiye yayo `.apk`, ishobora gukurwa ku rubuga rwa Tor. Rero iyo ukoresha iPhone, ubu buryo ntibuzokora: uzokenera igikoresho ca Android.



Kugira ngo ubone dosiye `.apk` biciye kuri Tor, uzokenera umucukumbuzi ashobora gushika ku mbuga za `.onion`. Uburyo bworoshe ni ugushiramwo porogarama ya Tor Browser kuri telefone yawe, ushobora kuyibona muri [Google Play Store] canke uyironka [biciye kuri `.apk`] yayo.



![Image](assets/fr/03.webp)



Amatelefone menshi y’ubuhinga bwa none arabuza gushiramwo porogarama zivuye mu bibanza bitazwi ku buryo busanzwe. Uzokenera gukoresha mu gihe gito iyi nzira ya Tor Browser mu mategeko y'igikoresho cawe kugira ngo wemere gushiramwo. Iyo porogarama imaze gushirwamwo, wibuke guhagarika iyo nzira kugira ngo ukomeze umutekano wa telefone yawe.



Ikindi kintu gihambaye gikenewe kugira ngo ukoreshe Ashigaru ni urudodo rwa Bitcoin Dojo. Kubera imvo z’umutekano n’ubusegaba, ikigo ca Ashigaru ntikibungabunga server imwe yo guhuza porogarama yawe. Rero uzokenera gukoresha instance yawe ya Dojo, canke wihuze n'iyizigirwa.



Dojo ishoboza porogarama yawe ya Ashigaru kuraba amakuru y’ivy’ubuhinga bwa none, kuraba amafaranga y’amaderesi yawe no gutangaza amafaranga yawe ku rubuga rwa Bitcoin.



Kugira umenye vyinshi ku vyerekeye Dojo no kumenya ingene woyishiramwo, ndagutumiye gukurikira iyi nyigisho yihariye :



https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Nimba vy’ukuri udashobora kwikorera Dojo yawe, urashobora gusanga abantu bashaka gusangira inkuru yabo ku buntu kuri [dojobay.pw](https://www.dojobay.pw/mainnet/). Ivyo bishobora kuba umuti w’igihe gito, ariko mu gihe kirekire, ndagusavye gukoresha Dojo yawe bwite kugira ngo ushobore kwizera ubusegaba bwawe n’ibanga ryawe.



## 2. Suzuma kandi ushiremwo porogarama ya Ashigaru .



### 2.1. Gukuraho porogaramu ya Ashigaru



Ku telefone yawe, fungura Tor Browser maze uje kuri [urubuga rwemewe rwa Ashigaru](https://ashigaru.rs/gukuraho/), mu gice ca `Gukuraho`. Hanyuma ukande kuri buto `Download for Android` kugira ngo ubone dosiye yo gushiramwo.



![Image](assets/fr/04.webp)



Imbere yo gushiramwo iyo porogarama ku gikoresho cawe, turaza kugenzura ko ari iyo ukuri be n’uko ataco ihinduye. Iyi ni intambwe ihambaye cane, cane cane iyo ushizeho porogaramu ukoresheje dosiye `.apk'.



### 2.2. Suzuma ubusabe bwa Ashigaru



Subira ku [urubuga rwemewe rwa Ashigaru](https://ashigaru.rs/download/) mu gice ca `Gukuraho`, hanyuma ukope ubutumwa bugaragara munsi y'umutwe `SHA-256 Hash wa dosiye ya APK`. Kopa igice cose, kuva kuri `TANGUZA UBUTUMWA BWASINYWE PGP` gushika kuri `ISOZO RY'UMUSINIRO wa PGP`.



![Image](assets/fr/05.webp)



Naho uri kuri telefone yawe, fungura urupapuro rushasha muri Tor Browser maze uje kuri [igikoresho co kugenzura urufatiro rw’urufunguzo](https://urufatiro rw’urufunguzo.io/verify). Nishire ubutumwa uherutse gukopa mu kibanza catanzwe, hanyuma ukande kuri buto ya `Suzuma`.



![Image](assets/fr/06.webp)



Niba umukono ari uw’ukuri, Keybase izokwerekana ubutumwa bwemeza ko dosiye yashizweko umukono n’abahinguzi ba Ashigaru. Ushobora kandi gukanda ku rubuga rwa `ashigarudev` rwerekanwa na Keybase maze ukagenzura ko urutoke rwabo rw'urufunguzo ruhuye neza na : `A138 06B1 FA2A 676B`.



Ariko iyo habaye ikosa muri iyo ntambwe, bisigura ko iyo sinyatire idafise akamaro. Muri ivyo, **ntushiremwo APK**. Subira utangure kuva mu ntango, canke usabe abarundi ngo bagufashe imbere y’uko ukomeza.



![Image](assets/fr/07.webp)



Keybase yaguhaye hash y’ikoreshwa. Ubu tuzosuzuma ko hash ya dosiye `.apk` mwakuye ihuye n'iyo yagenzuwe kuri Keybase. Kugira ngo ubikore, genda kuri [DOSIYE YA HASH KU RUBUGA](https://dosiye-ya hash.ku rubuga/).



![Image](assets/fr/08.webp)



Fyonda kuri buto ya `BROWSE...` hanyuma uhitemwo dosiye `.apk` yavanwe mu ntambwe ya 2.1.


Hanyuma uhitemwo igikorwa ca hash `SHA-256`, hanyuma ukande `CALCULATE HASH` kugira ngo ubare hash ya dosiye yawe.



![Image](assets/fr/09.webp)



Urubuga ruzokwerekana hash ya dosiye yawe `.apk`. Gereranya n’ivyo mwasuzumye kuri Keybase.io. Iyo izo hashes zibiri zisa, igenzura ry’ukuri n’ubutungane ryarashoboye. Ubu ushobora gukomeza gushiramwo iyo porogarama.



![Image](assets/fr/10.webp)



### 2.3. shiramwo porogaramu ya Ashigaru



Kugira ngo ushiremwo iyo porogarama, fungura umurongo w’amadosiye wo kuri telefone yawe maze uje muri dosiye y’ivyo ushobora gukuraho. Hanyuma ukande kuri dosiye `.apk` uherutse gusuzuma, maze wemeze ko yashizweho iyo usabwe.



![Image](assets/fr/11.webp)



Ashigaru ubu iri kuri telefone yawe.



## 3. Tangira porogaramu maze ureme igitabu ca Bitcoin



Igihe utanguye porogaramu ku ncuro ya mbere, hitamwo `MAINNET`.



![Image](assets/fr/12.webp)



Hanyuma ukande kuri `Tangira`.



![Image](assets/fr/13.webp)



Ubu tuzokora igitabu gishasha ca Bitcoin. Kanda kuri buto ya `Rema wallet nshasha`.



![Image](assets/fr/14.webp)



### 3.1. Rema igitabo ca Bitcoin



Ashigaru asaba igisasu ca passphrase BIP39. Hitamwo passphrase yawe maze uyishire mu bibanza bikwiye. Bitegerezwa kuba birebire kandi bitari vyo uko bishoboka kwose kugira ngo umuntu arwanye igitero c’inguvu z’agahomerabunwa.



Uce ukora backup y’umubiri y’iyi passphrase ubwo nyene. Iyi ni intambwe ihambaye cane: iyo utakaje telefone yawe, **iyo utagifise iyi passphrase, ntuzosubira kuronka ama bitcoins yawe** abitswe na Ashigaru wallet yawe. Iyi passphrase nyene irakoreshwa kandi mu gupfuka dosiye yo gusubizaho wallet.



Niba utazi ico passphrase ari co, canke udatahura neza ingene ikora, ndagusavye cane gusoma iyi nyigisho y’inyongera. Ivyo birahambaye, kuko passphrase ni ikintu gihambaye cane mu mutekano wawe: kudatahura neza uko ikoreshwa vyoshobora gutuma utakaza amahera yawe ubudasiba.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Umaze kwinjira muri passphrase yawe, kanda `IKURIKIRA`.



![Image](assets/fr/15.webp)



Hanyuma uhitemwo kode ya PIN. Iyi kode izokoreshwa mu gufungura Ashigaru wallet yawe, ikayikingira umuntu ata wemerewe kuyironka. Ntaco ihuriyeko n’ugukura kw’imfunguruzo zawe za wallet. Ivyo bisigura ko, naho utazi kode ya PIN, umuntu wese afise ijambo ryawe ry’ukwibuka na passphrase azoshobora gusubira kuronka amafaranga yawe y’ibiceri.



Hitamwo kode ya PIN ndende kandi idasanzwe. Ibuka kubika kopi y’inyuma ahantu hatandukanye na telefone yawe, kugira ngo ntizibe zishobora gufatwa icarimwe.



![Image](assets/fr/16.webp)



Iyo kode ya PIN imaze kuremwa, Ashigaru yerekana ijambo ry’ukwibuka rya wallet yawe. Imburi: iri jambo, rifatanijwe na passphrase yawe, ritanga uburenganzira bwo gushika ku bitcoins zawe. Uwuyifise wese arashobora kwigarurira amahera yawe, naho yoba adashobora gukoresha telefone yawe. Uwo murongo w’amajambo 12 urashobora gukoreshwa mu gusubizaho wallet yawe iyo telefone yawe yatakaye, yibwe canke ivunitse. Ni ngombwa rero ko umuntu ayizigama yitonze cane ku kintu kigaragara (impapuro canke icuma).



Ntukigere ubika iri jambo mu buryo bwa digitale, canke ngo ushire amahera yawe mu kaga ko kwibwa. Bivanye n’ingene ukoresha umutekano, urashobora gukora kopi nyinshi z’umubiri, ariko ntukigere uzigabanya. Amajambo agume mu rutonde rwayo nyarwo, kandi urabe neza ko afise inomero.



Ubwa nyuma, ntukigere ubika mnemonic na passphrase ahantu hamwe. Iyo ivyo vyose bihungabanywa icarimwe, uwutera yoshobora gushika ku wallet yawe.



![Image](assets/fr/17.webp)



Kugira ngo umenye vyinshi ku buryo bwo gukingira amajambo yawe y'ukwibuka, usabwe kuraba iyi nyigisho y'inyongera :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru aca akusaba ko wosubira kwemeza passphrase yawe. Fata aka karyo kugira ngo usuzume ko ivyo ufise vy’umubiri ari ukuri.



![Image](assets/fr/18.webp)



### 3.2. guhuza dojo



Igikurikira ni intambwe yo gufatanya na Dojo yawe. Nk’uko vyasiguwe mu ntangamarara, Ashigaru ategerezwa kuba ahuye na Dojo kugira ngo ashobore gukorana n’urubuga rwa Bitcoin.



Injira muri "Igikoresho co Gucungera" ca Dojo yawe maze ufungure `PAIRING` menu.



![Image](assets/fr/19.webp)



Ku Ashigaru, kanda kuri buto ya `Scan QR`, hanyuma ushireko kode ya QR y’ihuriro yerekanwa na DMT yawe. Hanyuma ukande kuri `Bandanya` kugira ngo wemeze.



![Image](assets/fr/20.webp)



Injira kode yawe ya PIN kugira ngo ufungure wallet. Ivyo bizokujana kuri paji y’uguhuza. Ni ibisanzwe kubona amakosa ya *PayNym* muri iyi ntambwe, kuko wallet ni nshasha. Fyonda gusa kuri `Bandanya`.



![Image](assets/fr/21.webp)



Uzoca uja kuri paji y’intango y’ibitabu vyawe.



![Image](assets/fr/22.webp)



Imbere yo kuja kure, ndagusavye gukora igikorwa co kugerageza gusubirana mu gihe wallet iguma ata bitcoin irimwo. Ivyo bizotuma ushobora kumenya nimba amapapuro yawe y’ububiko akora neza. Kugira umenye ingene bigenda, kurikiza iyi nyigisho:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Gushinga porogarama ya Ashigaru



Kugira ngo ugere ku mirongo y'ikoreshwa, fyonda ku ishusho ya *PayNym* yawe iri hejuru ibubamfu, hanyuma uhitemwo `Imirongo`.



![Image](assets/fr/23.webp)



Aha uzosanga uburyo bwinshi bwo guhindura igikorwa ca Ashigaru n’ivyo ukeneye. Ariko rero, ndagusavye cane gukoresha ibintu 2 bihambaye kuva mu ntango.



Tangana n'ugufungura `Umutekano > Uburyo bwo kwihisha`, hanyuma ukoreshe iyo nzira nimba uyikeneye. Ihisha porogarama ya Ashigaru inyuma y’izina, ikimenyetso n’ibara ry’iporogarama isanzwe ishizwe kuri telefone yawe. Intumbero ni ukubuza umuntu wese kumenya Ashigaru iyo umuntu asuzumye telefone yawe.



![Image](assets/fr/24.webp)



Igikoresho cose c’ikinyoma gishikirizwa gifise uburyo bwihariye bwo gufungura interface nyayo ya Ashigaru. Nk’akarorero, iyo uhisemwo igiharuro, porogarama ya Ashigaru irazimangana ku rubuga rwawe rw’imbere, igasubirizwa n’igiharuro c’ikinyoma. Iyo uyifunguye, ubona interface y’ibarabara ikora, ariko kugira ngo ushikire Ashigaru, ico ubwirizwa gukora n’ugukanda ikimenyetso `=` incuro zitanu vyihuse.



Igiharuro ca kabiri gihambaye co gukoresha ni [**RBF** (*Gusubirira-n’amahera*)](https://umugambi.ishure/ibikoresho/inkoranyajambo/rbf-gusubirira-n’amahera). Iyi option ishobora kwongera igiciro c’ibikorwa iyo bifashe mu mempools kuko igiciro kiri hasi cane. Ushobora kuyikoresha biciye ku `Ibikorwa > Gukoresha ukoresheje RBF`.



![Image](assets/fr/25.webp)



Impanuro: Ushobora guhindura igice c'iyerekanwa ry'ibiharuro vyawe kuva kuri `BTC` gushika kuri `sat` gusa mu gufyonda ku giciro cose kigaragara kuri paji y'intango.



## 5. Kwakira amafaranga y’ibiceri kuri Ashigaru



None ko portfolio yawe iriko irakora, urashobora kwakira satss. Kugira ngo ubikore, kanda kuri buto ya `+` iri musi iburyo bw'ibarabara, hanyuma ukande kuri buto ya `Receive` y'icatsi kibisi.



![Image](assets/fr/26.webp)



Ashigaru aca akwereka aderesi ya mbere y’ukwakira itakoreshejwe muri wallet yawe, kugira ngo ntusubire gukoresha aderesi (ugusubira gukoresha aderesi ni umugenzo mubi cane ku buzima bwite bwawe). Ushobora rero gutuma iyo aderesi umuntu canke igikorwa gikeneye kukurungikira ama bitcoins.



![Image](assets/fr/27.webp)



Iyo iyo nzira imaze gutangazwa ku rubuga, izoca iboneka ubwayo kuri paji y’intango y’iyo porogarama.



![Image](assets/fr/28.webp)



## 6. Wohereze amafaranga y'ibiceri na Ashigaru



None ko ufise ama bitcoins muri Ashigaru wallet yawe, urashobora no kuyarungika. Kugira ngo ubikore, kanda kuri buto ya `+` iri hasi iburyo, hanyuma uhitemwo buto ya `Send` itukura.



![Image](assets/fr/29.webp)



Hanyuma uhitemwo konti wipfuza gukoresha amahera. Kugeza ubu, ntiturakora kuri konti ya `Postmix`, yagenewe coinjoins, ivyo tuzobiraba mu nyigisho izoza. Rero tugiye kohereza amahera avuye kuri konti nyamukuru y’ibiziga.



![Image](assets/fr/30.webp)



Injira amakuru y’ivyo ukoresha: amahera uzorungika be n’aderesi y’uwuzoyakira Bitcoin.



![Image](assets/fr/31.webp)



Mu gufyonda ku tudodo dutoduto dutatu turi mu mfuruka yo hejuru iburyo, hanyuma kuri `Show unspent outputs`, urashobora kandi guhitamwo neza neza UTXO wipfuza gukoresha, kugira ngo wongere ubuzima bwite bwawe.



![Image](assets/fr/32.webp)



Uhejeje kwuzuza ibintu vyose, fyonda ku mwampi w’umweru uri musi y’ibarabara kugira ngo ukomeze.



Uzoca uja kuri paji y’incamake yerekana amakuru yose yerekeye ivyo waguriye. Ibintu vyinshi bihambaye biragaragazwa:




- Mu gice ca `Ico uja`, suzuma ubwa nyuma ko aderesi y'uwakira n'amahera yoherejwe ari ukuri;
- Mu gice ca `Amafaranga`, ushobora kubona igipimo c'amafaranga catowe na Ashigaru, iyo bikenewe, ukagihindura ukanda kuri `MANAGE` ;
- Igipande ca `Ibikorwa` kigaragaza ubwoko bw'ibikorwa ugiye gukora. Aha, turiko turavuga ivy’ugucuruza kworoshe, ariko Ashigaru na yo irashigikira ubundi bwoko bw’ugucuruza bushingiye ku buzima bwite, ivyo tuzobivuga mu buryo burambuye mu nyigisho izoza;
- Igipande c'umutuku `Transaction Alert` kirakugabisha nimba ibikorwa vyawe vyerekana uburyo bushobora kumenyekana n'ibikoresho vyo gusesangura uruhererekane, kandi bishobora gutuma ubuzima bwite bwawe buhungabana. Niwafyonda kuri yo, urashobora kubona ido n’ido. Nk’akarorero, ku bijanye nanje, Ashigaru ambwira ko amahera yoherejwe ari azunguruka (`3000 sats`), bikantuma nshobora guca irya n’ino umusaruro uhuye n’amahera akoreshwa n’ivyo guhindura. Kugira ngo umenye vyinshi ku bijanye n’izo nzira z’ugusesangura uruhererekane, ndagutumiye gukurikirana amahugurwa yanje ya BTC 204 ku bijanye n’Ishure ry’Itegeko ₿ ;
- Ubwa nyuma, urashobora kwongerako ikimenyetso ku vyo ugurisha kugira ngo ukomeze kwandika intumbero yavyo.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Umaze gusuzuma amakuru yose, ukoreshe umwampi w’icatsi kibisi kugira ngo wohereze ama bitcoins. Fata umwampi, hanyuma uwukurure iburyo kugira ngo wemeze ko washizeko.



![Image](assets/fr/33.webp)



Ivyo mwaguriye vyamenyeshejwe ku rubuga rwa Bitcoin.



![Image](assets/fr/34.webp)



## 7. Gusubiza Ashigaru yawe wallet



Gusubirana kw’indege ya Ashigaru wallet bitandukanye gato n’ivyo gukoresha indege ya kera ya Bitcoin wallet, kuko iyo nzira ikoresha uburyo bumwe n’ubw’indege ya Samurai Wallet. Iyo utakaje uburenganzira bwo gukoresha wallet yawe (yaba kubera ko wibagiwe PIN yawe, ukayikuramwo canke ukabura telefone yawe), hari uburyo bwinshi bwo kugarura ama bitcoins yawe.



Niba ugifise uburenganzira bwo gukoresha telefone yawe, canke nimba wari warakoze ububiko bw'iyi dosiye, uburyo bworoshe ni ugukoresha dosiye y'ububiko `ashigaru.txt`. Iyi dosiye irimwo amakuru yose ukeneye kugira ngo usubiremwo igitabo cawe ku nkuru nshasha ya Ashigaru (canke kuri Sparrow Wallet), ariko ipfutse na passphrase wasobanuye mu ntambwe ya 3.1 y'iyi nyigisho. Utegerezwa rero kugira dosiye `ashigaru.txt` na passphrase yawe kugira ngo ukoreshe ubu buryo.



Ukoresheje ivyo bintu bibiri, urashobora, nk'akarorero, gusubizaho ibitabo vyawe kuri Sparrow Wallet.



![Image](assets/fr/35.webp)



Niba udashobora kuronka dosiye `ashigaru.txt`, urashobora gusubira kuronka amahera yawe ukoresheje ijambo ryawe ry'ukwibuka passphrase, nk'uko wobigira ku yindi nkuru yose ya Bitcoin. Ndagusavye gukora ivyo gusubizaho haba ku nkuru nshasha ya Ashigaru, canke ku Sparrow Wallet, kugira ngo ushobore gusubirana mu buryo bworoshe inzira z’inyuma zivuye kuri Whirlpool nimba wariko urakoresha. Canke, ushobora kwinjiza aya makuru mu yindi porogarama yose ihuye na BIP39 winjiza n’amaboko inzira z’inkomoko.



Kugira ngo umenye vyinshi kuri iyo nzira, usabwe kuraba inyigisho yose nanditse ku bijanye no gusubizaho Wallet Samurai wallet. Kubera ko Ashigaru ari fork, uburyo bwo kubikora burasa:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Nk’uko ushobora kubibona, uburyo bwo gusubizaho ukoresha bwose, passphrase ni ngirakamaro. Rero nubone ko uyishigikira witonze. Ushobora kandi gukora kopi nyinshi, bivanye n’ingene ukoresha umutekano.



## 8. Guhindura ubusabe



Kugira ngo uhindure porogarama ya Ashigaru, kuko wayishize muri dosiye `.apk` atari kuri Play Store nk’iporogarama isanzwe, uzokenera gukuraho dosiye nshasha `.apk` ihuye n’iyo yahinduwe, hanyuma uyishiremwo n’amaboko.



Subiramwo intambwe zavuzwe mu gice ca 2 c'iyi nyigisho, kiretse ko iyo ukanda kuri dosiye `.apk` kugira ngo utangure gushiramwo, **telefone yawe Android ikwiye kuguha uburyo bwo `Update`, atari `Install`**.



![Image](assets/fr/41.webp)



Iyi ni ingingo ihambaye cane: iyo Android yerekana `Install` aho kugaragaza `Update`, birashoboka ko uriko urashiramwo verisiyo y’ubuhendanyi. Muri ivyo, uce uhagarika uburyo bwo gushiramwo ubwo nyene.



Nk'uko vyari vyifashe mu gushiramwo ubwa mbere, usabwe kugenzura ukuri n'ubutungane bwa dosiye `.apk` imbere yo gukomeza guhindura.



Kugira ngo umenye igihe verisiyo nshasha izoboneka, rimwe na rimwe nurabe urubuga rwemewe rwa Ashigaru. Nimwizere, Ashigaru ni porogarama ihamye, ikomeje, yarazwe na Samourai Wallet, kandi ivyo guhindura ni bike cane ugereranije n’ibindi bikoresho bikiri bito.



## 9. Gutanga amahera ku mugambi wa Ashigaru



Ashigaru ni umugambi w’inkomoko yuguruye. Niba wifuza gushigikira iterambere ryayo, urashobora gutanga intererano uhereye kuri iyo porogarama biciye kuri PayNym.



Kugira ngo ubikore, fyonda ku PayNym yawe iri hejuru iburyo bw'ibarabara, hanyuma uhitemwo kode yawe yo kwishura itangura na `PM...`.



![Image](assets/fr/36.webp)



Hanyuma ukande kuri buto ya `+` iri musi iburyo bw'ibarabara.



![Image](assets/fr/37.webp)



Hitamwo `Umugambi w'Isoko Yuguruye ya Ashigaru` nk'uwuzokwakira.



![Image](assets/fr/38.webp)



Fyonda kuri buto ya `CONNECT` kugira ngo ushireho umurongo w'itumanaho wa BIP47 (ibindi ku bijanye n'iyi porotokole mu nyigisho iri musi).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Igihe igikorwa co kumenyesha kimaze kwemezwa, urashobora kohereza intererano zawe ku mugambi ukanda ku mwampi mutoyi w’umweru uri hejuru iburyo bw’ibarabara.



![Image](assets/fr/40.webp)



Ubu urazi gukoresha ibintu nyamukuru vyo muri porogarama ya Ashigaru. Mu nyigisho zizoza, turaza kuraba ingene twovyungukirako mu gukoresha amafaranga, hamwe na Whirlpool, ugushirwa mu ngiro kwa coinjoin kwarazwe na Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
