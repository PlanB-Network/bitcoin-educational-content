---
name: Umbrel Nostr
description: Gutegura no gukoresha porogaramu za Nostr kuri Umbrel
---

![cover](assets/cover.webp)



## Ibisabwa: Gushiramwo umutaka



Umbrel ni urubuga rwuguruye rugufasha kwakira mu buryo bworoshe porogarama za Bitcoin n’ibindi bikorwa kuri server yawe bwite. Ni umuti w’ibintu vyose muri kimwe worohereza cane ukwiyakira ama node ya Bitcoin n’ibikorwa vy’ubuhinga bwa none.



Raba neza ko washizeho Umbrel ukurikije ubuyobozi bwacu bwo gushiramwo:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Intangamarara ya Nostr .



**Nostr** ni umurongo w’urubuga wuguruye, ushizwe ahantu hamwe, wagenewe gukorana n’abandi. Izina ryaryo risobanura _"Ivyanditswe n'ibindi bintu birungikwa n'ibikoresho"_. Iremerera umuntu wese gutangaza ubutumwa (amajambo), bucungiwe nk’ibintu vya JSON, no kubukwiragiza biciye ku maserukira y’ivy’ugutanga ubutumwa aho gukoresha urubuga rwo hagati. Uwukoresha wese afise urufunguzo rubiri rw’ibanga (rwihariye/rwa bose) rukora nk’ikimenyetso: urufunguzo rwa bose (npub) ruramenyesha uwukoresha, urufunguzo rw’ibanga (nsec) na rwo rushoboza ubutumwa gushirwako umukono. Ushimiye kuri iyi nyubakwa ikwiragijwe, **Nostr itanga ubushobozi bwo guhangana n’ugucengera** n’uguhinduranya cane: ushobora gukoresha abakiriya benshi no kwifatanya n’amarelay menshi uko ushaka, utavyifashemwo neza kuri server imwe.



Muri make, Nostr ni umurongo w’itumanaho wegerejwe aho **abaguzi** (ibikorwa vy’abakoresha) bohereza kandi bakira ibintu biciye ku **relayers** (servers). Iryo tegeko ryarakunzwe cane cane n’abanyagihugu ba Bitcoin kuva mu 2023, kubera agaciro karyo ko kwegereza ubutegetsi abaturage n’ubusegaba bw’amakuru.



**Iciyumviro:** Kugira ngo ukoreshe Nostr, uzokenera urufunguzo rwawe rw'ibanga (ruvuye ku mukiriya wa Nostr canke biciye ku nzira yihariye). **Ntukigere usangira urufunguzo rwawe rw'ibanga**, kuko vyotuma umuntu wese akwigira. Bibike ahantu hatagira umutekano kandi ukoreshe ibikoresho vy’uburongozi vy’ingenzi bitekanye (raba Impanuro iri musi).



## Ibisabwa vy'umutaka vya Nostr



Umbrel itanga ubuhinga bw’ibikorwa vy’ubuhinga buhuriweko kugira ngo ukoreshe neza Nostr ku nzira yawe bwite. Tugiye gusobanura neza ikoreshwa ry'amaporogarama nyamukuru ajanye na Nostr: **Igikoresho ca Nostr**, **noStrudel**, **Igikoresho co gupfukama** na **Igikoresho ca Nostr Wallet Connect**. Imwe yose ihuye n'ivyo ikeneye: _Nostr Relay_ ni **umukozi w'ibanga w'ibanga**, _noStrudel_ na _Snort_ ni **abaguzi ba Nostr** (ibikoresho vyo gusoma/gusohora amajambo), mu gihe _Nostr Wallet Connect_ ari igikoresho co guhuza **Lightning No** GW-r yawe.



### Nostr Relay - Igikoresho cawe c'ibanga ku Mutaka



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** ni porogaramu yemewe ya Umbrel yo gukoresha **relay yawe bwite ya Nostr** ku nzira yawe. Intumbero nyamukuru ni ukugira **relay yihariye** kandi yizewe kugira ngo **ukore backup y'ibikorwa vyawe vyose vya Nostr** mu gihe nyaco. Mu yandi majambo, ukoresheje iyo nzira y’umuntu ku giti ciwe uretse izo nzira za bose, urabona ko amajambo yawe yose, ubutumwa bwawe n’ingene wishuye bikopororwa muhira, ataco bihungabanya canke ngo bitakaze amakuru.



**Gushiramwo:** Uvuye mu Bubiko bw'Iporogarama bwa Umbrel (urutonde _Imibano_), shiramwo _Nostr Relay_. Iyo imaze gutangura, iyo porogarama ikora inyuma (service ya docker).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Uzobona urubuga rwayo rwa Interface biciye kuri Umbrel: rutanga amakuru y’ishimikiro kandi, ikiruta vyose, URL y’ivyo ukoresha (hejuru iburyo), uzokenera gukopa kugira ngo ukoreshe. Buto yo guhuza (ikimenyetso c’umubumbe) na yo nyene iraboneka.



**Kugira ngo wungukire ku nzira yawe y'umutaka:**



**Ongera relay ku mukiriya wawe wa Nostr:** Mu gikorwa cawe c'umukiriya (nk'akarorero Damus kuri iOS, Amethyst kuri Android, Snort canke noStrudel kuri Umbrel, n'ibindi), wongereko URL y'iyi relay yawe bwite wakopeye mbere. Ku mburabuzi, umurongo w'umutaka wumviriza ku cambu **4848**. Iyo uyishitse ku rubuga rw'aho hantu, ivyo bitanga URL nka: `ws://ws://umbrel.local:4848` (canke ukoreshe IP y'aho hantu ya Umbrel).



Niba ukoresha Tailscale (raba munsi), ushobora no gukoresha izina ry'ibanga rya MagicDNS DNS (kenshi `umbrel` canke izina ry'ubwite) kugira ngo uyironke aho hose, wama uri ku port 4848.



Niba ukunda Tor, rondera .onion Address ya Umbrel yawe maze uyikoreshe n'icuma 4848 biciye ku mucukumbuzi canke umukiriya ahuye na Tor (raba igice ca Tor)



URL imaze kwongerwa ku ntunganyo y'umukiriya wawe wa Nostr, uhuze n'iyi nzira. Ushobora kubona mu mukiriya wawe ko Umbrel relay ihuriweko (kenshi yerekanwa n’akadomo ka Green canke ibisa n’ivyo).



**Guhuza amateka (ntibikenewe)**: Mu rubuga rwa Interface rwa _Nostr Relay_ kuri Umbrel, fyonda ku **globe** 🌐 icon (iri hejuru kuri paji). Ico gikorwa kizohata relay yawe ya Umbrel kwifatanya n'izindi relay zawe (izo zatunganijwe mu mukiriya wawe) kugira ngo **ushiremwo ibikorwa vyawe vya kera vya bose**. Ivyo bisigura ko amajambo ya kera wasohoye canke wasomye biciye ku binyamakuru vya bose na yo nyene azokurwako maze abikwe ku binyamakuru vyawe vy’ibanga. Urasabwa kurindira ko uguhuza biba.



**Koresha Nostr nk'uko bisanzwe:** Kuva ubu, igikorwa gishasha cose (amakete yasohotse, inyishu, ubutumwa bwihariye bushizwe mu mfuruka, n'ibindi) ukora kuri Nostr kizorungikwa nk'uko bisanzwe ku bimenyetso vya bose **kandi bihuye n'ivyo utanga kuri Umbrel yawe**. Niba umukiriya wawe wa Nostr atunganijwe neza, azorungika ikintu cose ku bimenyeshamakuru vyose (harimwo n'ivyawe). Igikoresho cawe c’ibanga kizokora nk’igikoresho co gusubiza inyuma mu gihe nyaco. Naho hoba hariho ugucika kw’igihe gito, abakiriya bawe bazoshobora gusubira gukorana n’amakuru yabuze mu nyuma biciye kuri iyo relay. Ivyo biguha ububasha bwose ku makuru yawe ya Nostr



Mu nyuma, _Nostr Relay_ ya Umbrel ishingiye ku mugambi w’inkomoko yuguruye **nostr-rs-relay** (ugushirwa mu ngiro kw’amasezerano ya Rust). Ishigikira umurongo wose wa Nostr n’amategeko menshi asanzwe (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, n’ibindi), bikaba vyemeza ko umuntu ashobora gukorana neza n’abaguzi.



### noStrudel - Nostr umukiriya w'abashakashatsi



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** ni umukiriya w'urubuga rwa Nostr akoresha ubushobozi, ni mwiza cane mu gutahura no gutohoza urubuga rwa Nostr mu buryo burambuye. Ni ubwoko bw’isanduku y’umusenyi yo gusuzuma ibintu n’ibindi bimenyetso, no kugerageza ibintu vy’agaciro vy’iyo porotokole. Interface iri mu congereza kandi irafise ubuhinga, bikaba ari vyiza ku bakoresha bazi utuntu n’utundi bashaka kumenya ingene Nostr ikora imbere.



**Gushiramwo:** Gushiramwo _noStrudel_ mu Bubiko bw'Iporogarama bwa Umbrel (urutonde _Imibano_). Iyo imaze gutangura, ushobora kuyironka biciye ku mucukumbuzi wawe kuri Address ya Umbrel yawe (nk'akarorero `http://umbrel.local` canke biciye ku .onion/Tailscale yayo, raba igice co gushikira hanze).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Gutunganya ama relays:** Iyo ufunguye noStrudel, uzobona buto ya "Gutegura ama Relays" mu mfuruka yo hejuru iburyo. Fyondako kugira ngo utunganye ama relays yawe.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Kuri iyi paji, ushireko URL y'umurongo wawe wa Umbrel wakopeye mbere. Ushobora kandi kwongerako ibindi bimenyetso vyashikirijwe n'ikoreshwa. Umaze gutunganya ama relays yawe, ukande kuri "Sign in" iri musi ibubamfu kugira ngo ukomeze.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Ihuza:** noStrudel iraguha uburyo bwinshi bwo guhuza. Mu gihe cacu, tuzohitamwo "Urufunguzo rw'ibanga" maze dushiremwo urufunguzo rwawe rw'ibanga rwa Nostr rwakozwe mbere. Niba utararonka urufunguzo, urashobora gushiramwo urufunguzo rwa [Nostr Connect] (https://chromewebstore.google.com/details/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) kugira ngo ureme kandi/canke ubike urufunguzo rwawe rwa Nostr maze gutyo ntumenyeshe n'ibindi bikoresho vya Nostr.



![Interface principale de noStrudel](assets/fr/07.webp)



Iyo umaze guhuzwa, ushobora gukoresha noStrudel kugira ngo usangire amajambo yawe biciye kuri Nostr. Interface iguha uburenganzira bwo gukoresha :





- Uzuza urupapuro rwa Nostr n'urutonde rw'igihe, amatangazo, ubutumwa, ubushakashatsi bw'umwirondoro
- Ubuyobozi bwo guhanahana amakuru n'imiterere y'ihuriro
- Ibikoresho biteye imbere vyo gusuzuma ibintu n'ibirimwo vya JSON
- Amahitamwo y'imiterere y'igihe c'iyunguruzo na PINs



**Impanuro:** Kuri _noStrudel_, ushobora gushinga _ibiyunguruzo vy'igihe_ canke ugerageze _NIPs zitandukanye (Ibishoboka vyo gushirwa mu ngiro kwa Nostr)_. Nk’akarorero, suzuma ko NIP-05 (ibimenyetso vy’ibimenyetso vy’abantu bose) canke ibintu bishasha bishigikirwa. Ivyo bituma _noStrudel_ iba igikoresho ciza cane co kugerageza mu bidukikije bigenzurwa.



### Snort - Umukiriya wa Nostr wo muri iki gihe ku Mutaka



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** ni uwundi mukiriya w’urubuga rwa Nostr aboneka kuri Umbrel, atanga **Interface** y’ubuhinga bwa none, yihuta kandi idateye akaga yo gukorana n’urubuga rw’imigenderanire rwegerejwe. Udakunze noStrudel, igenewe abakoresha ububasha, _Snort_ igamije gukoresha neza ataco ihinduye ku mikorere. Yubatswe muri React, kandi itanga UX isukuye yibutsa imihora y’ubudandaji ya kera, bikaba bituma ishobora gukoreshwa buri musi.



**Gushiramwo:** Gushiramwo _Snort_ mu Bubiko bw'Iporogarama bwa Umbrel (urutonde _Imibano_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Iyo ufunguye Snort, uzobona ubuto buvuga ngo "Register" mu mfuruka ibubamfu hasi.



![Options de connexion dans Snort](assets/fr/10.webp)



Ushobora guhitamwo kwiyandikisha canke kwifatanya na konti isanzweho (ni co tuzokora muri iyi nyigisho).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort itanga uburyo bwinshi bwo guhuza. Ushobora gukoresha uburyo bwa Nostr Connect bwashizweho mbere canke ubundi buryo buboneka. Iyo umaze gufatanya, uzoshobora gukoresha iyo porogarama mu buryo bushitse.



Interface iva kuri _Snort_ itanga :





- **Ivyashizweho/Ibiganiro/Isi yose** vyerekana kugira ngo ugende hagati y'ivyanditswe vyawe, ibiganiro vy'urudodo, canke ifunguro ry'isi yose
- Ibipande vya **Imenyekanisha**, **Ubutumwa** (DM), **Gushaka**, **Urutonde**, n'ibindi.
- **+** canke _Kwandika_ buto kugira ngo usohore inyandiko nshasha
- Uburongozi bwa **ukwiyandikisha (gukurikira)** na **urutonde**
- Uburongozi bw'ibimenyetso kugira ngo wongereko/ukureho ibimenyeshamakuru no gukurikirana ukuboneka kwavyo



**Ivyiyumviro vy'ugutunganya ivyuma:** Kugira ngo wongereho ivyuma vyawe vya Umbrel, genda kuri Settings - Relays. Injira URL y'ivyo ukoresha (`ws://umbrel:4848` canke uwundi URL bivanye n'ivyo ukora) mu rutonde rwa Snort rw'ivyo ukoresha. Uko niko, Snort izotangaza amajambo yawe ku nzira yawe y’ibanga uretse aya bose.



### Nostr Wallet Huza - Huza umuravyo wawe Wallet na Nostr



**Nostr Wallet Connect (NWC)** ni porogaramu **ihuza urudodo rwawe rwa Umbrel (Umuravyo)** n'ibikorwa vya Nostr bihuye kugira ngo ukore amahera y'umuravyo (nk'akarorero, kohereza _zaps_, ayo mahera make kubera "ugukunda" ibirimwo). Muri iyi nyigisho, turaza kuraba ingene wohuza noStrudel n'uruzitiro rwawe rwa Lightning kugira ngo ushobore kwishura uhereye kuri Interface.



**Gushiramwo no gutunganya:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Shiraho _Nostr Wallet Ihuza_ kuva mw'iduka rya Alby ku Mutaka.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



Muri noStrudel, fyonda ku nkuru yawe iri hejuru iburyo, hanyuma ukande kuri buto ya "manage".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Fyonda kuri "Umuravyo" hanyuma "uhuze Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Mu mahitamwo yo guhuza, hitamwo "Umbrella".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Fyonda kuri "Huza" kugira ngo uhite urungikwa ku gihe cawe co Guhuza Umbrel Nostr Wallet.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Kuri paji ya Nostr Wallet, ushobora :




   - Sigura ingengo y'imari yawe nini
   - Kwemeza uburenganzira
   - Gushinga igihe co guhera kw'ihuriro


Fyonda kuri "connect" kugira ngo uheze.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Uca urungikwa kuri noStrudel n'ubutumwa bwo kwemeza: ubu urashobora zap isi yose ukoresheje node yawe ya Wallet/LND!



Ushimira NWC, **amahera yawe y'umuravyo biciye kuri Nostr** (zaps zo guhemba ivyo wanditse, _Agaciro ku gaciro_ amahera, n'ibindi) atangura ku **node yawe bwite**. Ntugikeneye gukoresha amafaranga yawe biciye ku bikorwa vyo hanze canke gucapura QR kuri telefone yawe igihe cose. Ubumenyi bw'abakoresha burarushirizwa cane, mu gihe buguma _butagira ububiko_ kandi bufise ubuzima bwite.



Niba ushaka kumenya ingene woshiraho node yawe ya Lightning kuri Umbrel, ndagusavye urabe iyi yindi nyigisho yuzuye:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Gutunganya n'umutekano biteye imbere



Gukoresha Umbrel na Nostr hamwe ku rugero rwo hejuru bisaba kwitwararika cane **umutekano** na **uguhuza**. Aha hariho impanuro nkeyi z’ingene wokingira configuration yawe no kuyironka neza, aho uri hose.



### Ukwinjira hanze gutekanye: Tor na Tailscale



Kubera imvo z'umutekano, Umbrel yawe ishobora gushikwako gusa ku rubuga rwawe rwo mu karere (kandi biciye kuri Tor). Kugira ngo ukoreshe Nostr kure y’i muhira, ufise inyishu zibiri ukunda: **Tor** (ugushikira ata mazina biciye ku rubuga rw’igitunguru) na **Tailscale** (urusenga rwa VPN rw’ibanga).





- Ushobora gushikako biciye kuri Tor:** Umbrel ihita itunganya **Serivisi ya Tor (.onion)** ku rubuga rwayo rwa Interface n'ibikorwa vyayo. Ivyo bisigura ko ushobora gushika kuri Interface Umbrel (harimwo *noStrudel* canke *Snort*) uri aho hose, ukoresheje umucukumbuzi wa Tor, utagaragaje IP yawe ya bose. *Tor ikoreshwa mu gushika ku bikorwa vyawe vya Umbrel uri hanze y'urubuga rwawe rwo mu karere, utashize igikoresho cawe kuri Internet ([Gushiraho Tor kuri sisitemu yawe - Inyobora - Umbrel Umuryango](https://umuryango.umbrel.com/t/gushiraho-ku-sisitemu-yawe/7509#:~:text=Urubuga%3A%20https%3A%2F%2Fwww)).* Kugira ngo ukoreshe iyi nzira, genda kuri Umbred settings maze utore kode yawe ya QRonion'. Ku mucukumbuzi wa Tor, genda kuri iyi .onion Address: uzoronka Interface imwe n'iyo mu karere. Ushobora rero gukoresha ama apps yawe ya Nostr nk’uko biri i muhira.


**Nostr relay via Tor:** Niba wipfuza ko relay yawe ya Nostr ishobora gushikirwa biciye kuri Tor n'abaguzi bawe (canke abagenzi bemerewe), ivyo birashoboka. Umbrel ntitanga .onion Address ya relay ataco ihinduye, ariko kuko ikoresha ku port 4848, ushobora :





    - Koresha .onion Address ya UI Umbrel maze utunganye umukiriya wawe kugira ngo yihuze biciye kuri iyi Interface (ntibishoboka kuri WebSocket),





- Canke **gushikiriza port 4848 nk'igikorwa c'igitunguru gitandukanye. Ivyo bisaba gukoresha Tor config kuri Umbrel (igenewe abakoresha bateye imbere bashobora gukoresha SSH). Canke, wiyumvire ** Tor tunnel **ku yindi server ihindura inzira kuri Umbrel: ariko, ku gukoresha ku giti cawe, biroroshe gukoresha Tailscale.**





- Ushobora gushikako biciye ku rugero rw’umurizo: **[urugero rw’umurizo](https://tailscale.com/) ni umuti w’urusenga rwa VPN urema uruja n’uruza rw’ibanga hagati y’ibikoresho vyawe na Umbrel. Inyungu: ikora nk’aho woba uri kuri LAN, ariko kuri Internet, ipfutse kandi ata n’ibintu bikomeye bikoreshwa.** Tailscale iha Umbrel yawe IP idahinduka n’izina ry’itongo ry’ibanga, utitaye ku kibanza c’urubuga rwayo **([Tailscale | Umbrel App Iduka](https://porogarama.umutaka.com/porogarama/urugero rw'umurizo#:~:umwandiko=Urugero rw'umurizo%20ni%20zero%20config%20VPN,yasubiwemwo%20kandi%20yizewe%20igereranyo))**. Mu bikorwa, umaze gushiramwo Tailscale kuri Umbrel (kuva muri Umbrel App Store, urutonde rwa *Imihora*) **na** ku bikoresho vyawe (telefone ngendanwa, PC...), uzoshobora gushika kuri Umbrel uciye kuri Address nka `100.x.y.z` (Tailscale nka IP) `umutaka.umurizo123.ts.urusenga`.


ku Nostr_, Tailscale ni ngirakamaro cane: telefone yawe ngendanwa, iyo ifise Tailscale ikora, izoshobora kwifatanya na `ws://umbrel:4848` (bishimira MagicDNS) canke itanguye kwifatanya na IP ya Tailscale n’icuma 4848 kugira ngo ukoreshe iyo relay. Aba clients nka Damus canke Amethyst bazobona Umbrel yawe nk’aho yoba iri ku rubuga rumwe rw’aho hantu. **Impanuro:** Gushoboza **MagicDNS** mu Tailscale kugira ngo ukoreshe izina ry'umushitsi `umbrel` aho gufata mu mutwe IP. Ivyo bituma ushobora gukorana neza n’ivyo ukoresha mbere n’igihe uriko uragenda ([Ivyo ukoresha Nostr | Umbrel App Store](https.


Ikindi, Tailscale iragufasha gushika ku Mutaka wa Interface (kandi rero _noStrudel/Snort_ abaguzi b'urubuga) biciye ku mucukumbuzi woroshe, ukoresheje IP y'ibanga canke izina ry'indangarubuga ryatanzwe. Nta nkenerwa y'umucukumbuzi wa Tor, kandi umuvuduko wo gutanga amakuru muri rusangi ni mwiza kurusha biciye ku rubuga rwa Tor.




**Iciyumviro: Tor na Tailscale ntibihuye. Ushobora kuguma ukoresha Tor kugira ngo uyikoreshe ata mazina canke ibikorwa vyihariye, kandi ukoreshe Tailscale ku musi ku musi kubera ko yoroshe. Muri ivyo bihe vyose, ntukeneye gufungura port kuri router yawe, ivyo bikaba bikomeza umutekano.**



### Gukingira umurongo wawe wa Nostr (ibikorwa vyiza)



Niba ukira urugendo rwa Nostr kuri Umbrel, cane cane mu gihe giteye imbere, urabe ko ukoresha ingendo nziza nkeyi:





- Relay y’ibanga canke ibujijwe: Ku buryo busanzwe, relay yawe ya Umbrel ni iy’ibanga (ntimenyeshwa ku mugaragaro) kandi, iyo uyishitseko gusa uciye kuri Tailscale canke LAN yawe, izoguma idashobora gushikwako n’abanyamahanga. **Gumana ibanga ry'iyi nzira.** Ntuyitangaze ku mbuga za Nostr za bose kiretse ushaka kwakira abandi bakoresha ku bushake, ivyo bikaba ari ikindi kibazo (ugucungera, uburebure bw'uruja n'uruza, n'ibindi). Kugira ngo ukoreshe ubwawe, turagusavye ko ushobora gushikira wewe nyene, kandi nimba bikenewe, ugashikira abagenzi n’imiryango bakeyi wizigira.





- Urutonde rwera / Auth: Ishirwa mu ngiro rya nostr-rs-relay rishigikira uburyo bwo kwemeza **NIP-42** hamwe n' *urutonde rwera* rw'imfunguruzo za bose. Mu gukoresha aya mahitamwo, ushobora guhagarika ubutumwa bwawe kugira ngo **bwemere gusa ibintu vyashizweko umukono n'imfunguruzo zimwe zimwe (izawe)**, canke ko abaguzi bategerezwa kwemeza kugira ngo bamenyeshe. Gushinga ibi bisaba guhindura dosiye y'imiterere ya `config.toml` mu Umbrel (biciye muri SSH mu gikoresho ca Docker). Ni ugukoresha neza, ariko nk'akarorero ushobora gutanga urutonde rw'amatangazo yemerewe (`pubkey_whitelist`). Uko niko naho umuntu yovumbura relay yawe, ntaco azoshobora gutangaza ng’aho iyo atari kuri list.





- Ivyagezwe n'ugucungera:** Gumana umutaka wawe na _Nostr Relay_ app bishasha. Ivyavuguruwe bishobora kubamwo ivyiza (nk'ugukoresha neza ubutumwa butari bwo) n'ugukosora umutekano. Ku Mutaka, genda urabe muri App Store ubudasiba kugira ngo ubone ivyahinduwe kuri _Nostr Relay_, hanyuma ubikoreshe uko bikenewe.





- Gukurikirana n’imipaka:** Gumana ijisho ku kuntu relay yawe ikoreshwa. Iyo uyifunguriye abandi, urabe neza umuzigo (CPU/RAM storage) uri kuri Umbrel yawe, kuko relay ishobora kwirundanira ningoga amakuru menshi. nostr-rs-relay itanga **imipaka n'ububiko** bishobora guhindurwa (`imipaka` mu config, nk'umubare w'ibintu ku segonda, ubunini bw'ibintu, gukuraho ibintu vya kera...). Ku bijanye n'ikoreshwa ry'ibanga, kumbure ntuzokenera gukora kuri ivyo, ariko menya neza ko ivyo bipimo biriho nimba ubikeneye ([nostr-rs-relay/config.toml ku mukuru - scsibug/nostr-rs-relay - GitHub](https://github.com.





- Gukingira imfunguruzo za Nostr:** Iyi ngingo yaramaze kuvugwa, ariko ni ngirakamaro cane: ntukigere winjiza imfunguruzo zawe z’ibanga za Nostr muri Interface utizigira bimwe bishitse. Ahubwo, koresha ivyungura umucukumbuzi canke ibikoresho vyo hanze (nk’ivya Nostr *signers* ku matelefone atandukanye) kugira ngo ushire umukono ku bikorwa bihambaye. Kuri Umbrel, abaguzi bawe b'urubuga nka *Snort* na *noStrudel* barashobora gukora batazi urufunguzo rwawe rw'ibanga, biciye kuri NIP-07. Nukoreshe aka karyo kugira ngo uhuze ihumure n’umutekano.




Mu gukurikiza izi mpanuro, ugushiramwo urudodo rwa Umbrel na Nostr bizoba bikomeye **kandi** bitekanye. Uzogira ibidukikije vyose: uruzitiro rwa Bitcoin rwo kwishura Lightning, uruzitiro rw’ibanga rwa Nostr rw’ubusegaba bw’amakuru, n’abaguzi b’urubuga rwa Nostr bakora cane kugira ngo bashobore kugendera kuri uru rubuga rushasha rw’imigenderanire. Nimwinovore gutembera muri Nostr n'umutaka!