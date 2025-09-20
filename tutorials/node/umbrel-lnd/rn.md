---
name: Umbrel LND
description: Inyigisho ziteye imbere ku gushiramwo no gutunganya Lightning Network Daemon (LND) kuri Umbrel
---
![cover](assets/cover.webp)




## Imenyekanisha



Iyi nyigisho iteye imbere iragutwara intambwe ku yindi mu gushiramwo, gutunganya no gukoresha porogarama ya Lightning Node (LND) ku nzira yawe ya Umbrel. Uzokwiga ingene wofungura imirongo, gucunga amafaranga yawe no guhuza node yawe n’iporogarama yo kuri telefone ngendanwa.



## 1. Ibisabwa: gukora Bitcoin Umutaka node



Imbere yo gukoresha Lightning, ukeneye kugira urudodo rwa Bitcoin rukora neza kuri Umbrel. Ivyo birimwo gushiramwo Umbrel (ku Raspberry Pi, NAS canke iyindi mashini) no gukorana neza na Blockchain Bitcoin.



Kugira ngo ushireho Umbrel kandi utunganye urudodo rwawe rwa Bitcoin, turagusavye gukurikiza inyigisho yacu yihariye :



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Raba neza ko urudodo rwawe rwa Bitcoin ruri ku gihe kandi rukora neza, kuko Lightning Network ari rwo ruyizigira ku bikorwa vyose vya off-chain.



## 2. Intangamarara y’igitabu Lightning Network



Lightning Network ni umurongo wa kabiri wa Layer wagenewe kwihutisha no kugabanya igiciro c’ibikorwa vya Bitcoin mu kubikora hanze ya Blockchain nyamukuru.



Mu majambo nyayo, Lightning ikoresha uruja n’uruza rw’imihora yo kwishura hagati y’ibice: abakoresha babiri bafungura umurongo mu kubuza On-Chain BTC (ugucuruza kwa mbere), hanyuma bagashobora guca bashobora kwishura Exchange muri uwo muhora. Ivyo bikoresho vya off-chain ntivyandikwa kuri Blockchain, ni co gituma vyihuta cane kandi hafi ataco bimaze.



Ivyishyurwa bishobora guca mu nzira nyinshi (biciye ku nzira zihuza) kugira ngo bishike ku muntu wese abikira ku rubuga, bikaba bishoboza urugero hafi rudafise aho rugarukira rw’ugutanga amafaranga ako kanya. Lightning rero itanga amafaranga yihuta cane, atari menshi, meza cane mu kwishura buri musi canke amafaranga make, mu gihe iremesha umuzigo kuri Blockchain Bitcoin.



Kugira ngo ikore, urudodo rwa Lightning rutegerezwa kuba rufatanye ubudasiba n’urubuga kandi rugakorana n’izindi node za Lightning. Hariho ubuhinga butandukanye bwo gukoresha porogarama (LND, Core Lightning, Eclair, n’ibindi), vyose bikaba bihuye. Umbrel ikoresha LND (Lightning Network Daemon) nk’igice c’ikoreshwa ryayo ryemewe ry’Umuco. Iyi nyigisho yibanze kuri LND.



Kugira ngo ubone intangamarara yuzuye y'inyigisho za Lightning Network, turagusavye gufata inyigisho yacu yihariye :



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Iryo shure rizoguha ubumenyi bushitse ku vyiyumviro nyamukuru vya Lightning Network, imbere y’uko ugenda wimenyereza n’urudodo rwawe rwa LND.



## 3. Kubera iki LND yikira?



Gukoresha node yawe bwite ya Lightning (LND) kuri Umbrel biguha ubusegaba bwose ku mahera yawe n’imihora yawe, ugereranyije n’imiti y’ububiko canke y’ububiko buke.



### Kugereranya inyishu z'umuravyo :



**Imirongo y'ibisubizo (nk'akarorero: Wallet ya Satoshi)** :




- Ama bitcoins yawe y'umuravyo acungiwe n'uwundi muntu yizigirwa
- Biroroshe gukoresha, ntaco bigoranye mu vy'ubuhinga
- Uwukoresha arafise amafranga yawe kandi ashobora gukurikirana amafaranga yawe
- Utanga ubugenzuzi n'ubuzima bwite



**Ibikoko vy'abaguzi bitari ibicuruzwa (nk'akarorero Phoenix, Breez)** :




- Abakoresha bagumana imfunguruzo zabo z’ibanga gutyo Ownership ya BTC yabo
- Nta burongozi bushitse bw'urudodo - porogaramu icungera imirongo iri inyuma
- Gusenyera ku mugozi umwe hagati y'ukworoha n'ubusegaba
- Kuva ku bikorwa remezo vy'abaguzi kugira ngo haboneke amafaranga
- Imipaka y'ubuhinga (telefone imwe y'ubuhinga ntishobora gutuma abandi bishurwa)



**Igikoresho ca LND (Umukata)** :




- Ubusegaba burengeye ubundi bwose: BTC zawe za On-Chain na off-chain ziri munsi y’ububasha bwawe bwose
- Nta wundi muntu afise uruhara mu gufungura imihora canke mu gucunga amahera yawe
- Ukwongerekana kw'ubuzima bwite (imirongo yawe n'ibikorwa vyawe bimenyekana kuri wewe gusa n'abo musangiye igitsina)
- Umwidegemvyo wo gukoresha: kwifatanya n'ibikorwa vyawe bwite n'amasakoshi yawe
- Ubushobozi bwo gutuma abandi bakoresha amafaranga (amahera make)
- Kwongerera inshingano z'ubuhinga (gucungera, gucunga amafaranga, gusubiza inyuma)



Muri make, self-hosting LND iraguha ububasha bwinshi, ariko isaba ubuhinga bwinshi. Ni uguhuza hagati y’uburyohe n’ubusegaba.



## 4. Intambwe ku yindi inyigisho



### 4.1 Gushiramwo no gutunganya porogaramu ya Lightning Node kuri Umbrel



Igihe umutaka wawe (Bitcoin) umaze gukorana, kurikiza izi ntambwe :



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Shiraho porogaramu ya Lightning Node mu gice ca "App Store" c'Umutaka wa Interface.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) izoshirwa ku Mutaka wawe nk’igikorwa. Iyo uyifunguye ubwa mbere, uzobona ubutumwa bwo kukumenyesha ko Lightning ari ubuhinga bwo kugerageza.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Ushobora guhitamwo hagati yo kurema urudodo rushasha canke kugarura urudodo ruvuye mu bubiko/seed. Ku bijanye no gushiramwo ubwa mbere, hitamwo gukora urudodo rushasha. Porogarama ya Lightning Node izo generate ijambo 24 ry’amajambo Mnemonic (seed Lightning yawe): iyandike witonze cane (vyiza cane iyo utari ku murongo, ku mpapuro), kuko izokoreshwa mu kugarura amahera yawe ya Lightning iyo bikenewe.



**Iciyumviro:** Ku verisiyo za Umbrel za vuba, gushiramwo porogarama ya Lightning bitanga iri jambo 24 seed (node ​​ya Bitcoin Umbrel ubwayo ntiyigira).



![Interface principale de Lightning Node](assets/fr/04.webp)



Inyuma yo gutangura, uzoshika ku Interface nyamukuru ya Lightning Node.



![Paramètres de l'application](assets/fr/05.webp)



Mu mitunganyirize ya porogaramu, uzosanga amahitamwo menshi ahambaye:




   - Raba ID y'urudodo rwawe (indangamuntu yihariye y'urudodo rwawe)
   - Guhuza Wallet yo hanze (Guhuza Wallet)
   - Reba amajambo y'ibanga
   - Kugera ku mitunganyirize iteye imbere
   - Gusubiza imirongo
   - Gukuraho dosiye y'ububiko bw'umurongo
   - Gushoboza ububiko bwihuta
   - Gutunganya ububiko biciye kuri Tor (Ububiko kuri Tor)



Aya mahitamwo ni ngombwa ku mutekano n’uburongozi bw’uruzitiro rwawe rwa Lightning. Raba neza ko ukoresha ama backups yikora kandi amajambo yawe y’ibanga akaguma ari meza.



**Ibikoresho vy'ingirakamaro:**




- [Umuryango w'umutaka](https://community.umbrel.com) - Ihuriro ry'ibiganiro ry'abakoresha kugira ngo basangire ingorane n'imiti yerekeye umutaka n'ibidukikije vyawo


> - [Iduka ry'amaporogarama y'umuravyo - Igikoresho c'umuravyo (LND)](https://apps.umbrel.com/app/lightning) - Insobanuro y'ibiranga porogarama y'umuravyo ku Mutaka
> - [Inyandiko za LND - Gutangura vuba](https://inyandiko.umuravyo.ubuhinga/ibikoresho-vy'urubuga-rw'umuravyo/LND/gukoresha-LND) - Inyandiko zemewe za LND

### 4.2 Gufungura umurongo w'umuravyo



LND imaze gukora, urashobora gufungura umurongo wawe wa mbere wa Lightning. Kugira uronke uburyo bwiza bwo gufatanya na:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) ni umushakashatsi wo kurondera uturongo twizewe two gufungura imirongo.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Nk’akarorero, [urudodo rwa ACINQ] (urudodo rwa ACINQ) ni urudodo rwemewe rw’imibare n’ubushobozi bwo gukoresha amahera.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Ku bw’iyi nyigisho, tuzofungura umurongo ufise [Swiss Bitcoin Pay]( Amakuru asabwa kugira ngo umuntu ashobore gukorana (pubkey@ip:port) aratangwa kuri paji yabo ya Amboss.



Kugira ngo ufungure umurongo :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Ku rupapuro rw'intango rwa Lightning Node, kanda kuri buto ya "+ FUNGURA UMUGORORO"



![Configuration du canal](assets/fr/10.webp)



Muri paji y'imiterere y'umurongo :




   - Gushiramwo indangamuntu y'uruzitiro yakopiwe kuri Amboss (uburyo: pubkey@ip:icuma)
   - Sigura umubare w'ubushobozi bw'umurongo (ibice bimwe bimwe nka ACINQ bifise ubuke, nk'akarorero 400k Sats)
   - Guhindura amafaranga yo gufungura iyo bikenewe



![Canal en cours d'ouverture](assets/fr/11.webp)



Igihe amafaranga amaze gutumwa, umurongo uzoboneka nk'uwufunguye kuri paji y'intango. Rindira kwemezwa kw’isoko rya On-Chain.



![Détails du canal](assets/fr/12.webp)



Fyonda kuri iyo channel kugira ubone ibisobanuro vyayo:




   - Uko bimeze ubu
   - Ubushobozi bwose
   - Gusenyuka kw'amahera (yinjira/isohoka)
   - Urufunguzo rwa bose rwa node ya kure
   - N'ayandi makuru y'ubuhinga .



### Gukoresha Lightning Network+ kugira uronke amafaranga yinjira



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ iraboneka muri Umbrel App Store kugira ngo vyorohe kuronka amahera yinjira.



![Interface principale de LN+](assets/fr/14.webp)



Interface nyamukuru itanga uburyo butatu buhambaye:




- "Ivy'uguhindura amafaranga: reba amashimwe y'uguhindura ariho
- "Mfungurire": cungurura amahinduka ushobora guhabwa
- "Ku nyandiko": gushika ku nyandiko



![Message d'erreur LN+](assets/fr/15.webp)



Iciyumviro: Niba utarafungura umurongo, uzobona ubu butumwa bw'ikosa iyo ukanda kuri "Open For Me".



![Liste des swaps disponibles](assets/fr/16.webp)



Paje ya "Liquidity Swaps" yerekana amashimwe yose y'uguhindura aboneka ku rubuga.



![Swaps éligibles](assets/fr/17.webp)



"Open For Me" iyungurura gusa izo swaps node yawe ihuye n'ibisabwa.



![Détails d'un swap](assets/fr/18.webp)



Akarorero k'ibisobanuro vy'uguhindura :




- Itunganywa rya Pentagon (abaje mu nama 5)
- Ubushobozi bwa 300k Sats ku muhora
- Ibisabwa: nibura imirongo 10 yuguruye ifise ubushobozi bwose hamwe bwa 1M Sats
- Ibibanza biriho: 4/5.



### 4.3 Guhuza n'iporogaramu yo kuri telefone ngendanwa (Zeus)



Kugira ngo ushobore kugenzura node yawe ya Lightning uri kure (telefone ngendanwa), urashobora gukoresha Zeus (porogarama y’inkomoko yuguruye iboneka kuri iOS/Android).



**Imiterere ya Zewu n'umutaka :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Raba neza ko urudodo rwawe rwa Umbrel rushobora gushikwako (ku buryo busanzwe biciye kuri Tor).


Mu Mutaka wa Interface, fungura porogarama ya Lightning Node, hanyuma ukande kuri buto ya "Huza Wallet" nk'uko vyerekanwa n'umwampi.



![Page de connexion avec QR code](assets/fr/20.webp)



Kode ya QR iraboneka, irimwo amakuru yawe yo gukoresha LND mu buryo bwa lndconnect. Iyi kode ya QR irafise amakuru menshi cane, rero ntukekeranye kuyigwiza kugira ngo uyisome neza.



![Configuration initiale de Zeus](assets/fr/21.webp)



Kuri telefone yawe :




   - Gufungura Zewu
   - Ku rupapuro rw'intango, kanda kuri "Imiterere iteye imbere" kugira ngo uhuze urudodo rwawe rw'umuravyo
   - Mu mirongo, hitamwo "Rema canke uhuze Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



Muri Zewu:




   - Hitamwo "LND (IRUHUKO)" nk'ubwoko bw'ihuriro
   - Ushobora gucapura kode ya QR (uburyo bushimikijwe) canke ukinjiramwo amakuru n’amaboko. (Ntukekeranye gutera imbere kuri code QR ya Umbrel, kuko irakomeye cane)
   - Ivy'ingenzi: fungura "Koresha Tor" nimba Umutaka wawe ushobora gushikwako gusa biciye kuri Tor (ivya kera)
   - Bika imiterere



Zeus yawe ubu ihuye n’uruzitiro rwawe rwa Umbrel kandi iraguha uburenganzira bwo kwishura Lightning, kuraba imirongo yawe, amafaranga yawe, n’ibindi, mu gihe uguma wigenzura rwose.



**Amahitamwo yo guhuza ateye imbere:**



Ku mburabuzi, uruja n’uruza rwa Zeus ↔ Umutaka ruca kuri Tor. Kugira ngo ushobore gukorana vyihuta, hari uburyo bubiri:



**Umuravyo Uhuza (LNC)** :




   - Uburyo bwo guhuza bwa Lightning Labs
   - Shiraho porogaramu y'umuravyo kuri Umbrel (harimwo no kuronka LNC)
   - generate kode ya QR y'ihuriro mu Kibanza c'Umuravyo (Ihuza → Ihuza Zeus biciye kuri LNC)
   - Scan muri Zeus (hitamwo "LNC" nk'ubwoko bw'ihuriro)



**Ikigereranyo c'umurizo wa VPN**:




   - Biroroshe-gutunganya urusenga VPN
   - Shiraho Tailscale kuri Umbrella (Iduka rya App) no kuri telefone yawe ngendanwa
   - Huza Zewu biciye ku IP yihariye y'umurizo aho gukoresha Tor Address



Ivyo bihitamwo si ngombwa, kandi umuti wa Tor + Zeus urakora neza kenshi.



> **Ibikoresho vy'ingirakamaro:**
> - [Inyandiko za Zewu - Ihuza ry'umutaka](https://umuryango.umutaka.com/t/zeus-LN-mobile/7619) - Inyobora yemewe yo guhuza Zewu n'umutaka
> - [Zewu GitHub] (Zewu LN/Zewu) - Umugambi wa Zewu w'inkomoko yuguruye
> - [Umuryango w'Umutaka - Guhuza Zewu biciye ku Murizo](https://umuryango.umutaka.com/t/ingene-wokoresha-umurizo-n'umutaka/6782) - Inyobora yo guhuza Zewu n'Umutaka ukoresheje Umurizo

## 5. Umutekano n’ingene wobikora neza



Gucungera urudodo rw’umuravyo rwikorera bisaba kwitwararika cane umutekano.



### Ububiko n'umutekano w'uruzitiro rwawe



**Ubwoko bw'ingenzi bw'ibisubizo**



Umutaka wawe w'umuravyo usaba ubwoko bubiri bw'ububiko:



**Interuro ya seed (amajambo 24)**




- Gusubiza amafaranga On-Chain
- Ni ngombwa gusubira kurema umuravyo wawe Wallet
- Ku bubiko butekanye cane (butari kuri interineti, ku mpapuro)



**Ububiko bw'umurongo udahinduka (SCB)** dosiye




- Birimwo amakuru y'umurongo w'umuravyo
- Bishoboza gufunga umurongo ku nguvu iyo habaye impanuka
- Ivy'ingenzi:** Ntukigere ubika dosiye `channel.db` n'amaboko (ingorane z'ibihano)



**Uburyo bwo gusubiza inyuma n'amaboko**



Kubika imirongo yawe n'amaboko :


1. Shira kuri menu ya Lightning Node (utudodo dutatu "⋮" iruhande ya "+ Gufungura umurongo")


2. Gukuraho dosiye y'ububiko bw'umurongo


3. Gusohora SCB nshasha inyuma y'uguhindura umurongo wose


4. Bika SCB neza (ibinyamakuru bifise amakuru, kopi iri hanze y’aho hantu)



**Umutaka** uburyo bwo gusubiza inyuma bwikora



Umbrel ifise ubuhinga buhambaye bwo gucungera amakuru :



*Ukurinda amakuru:*




- Ugushiramwo amakuru ku ruhande rw'umukiriya imbere yo gutanga
- Kurungika biciye ku rubuga rwa Tor
- Amakuru yongeweko n'ukuzuza mu buryo butari bwo
- Urufunguzo rw'ibanga rwihariye ku gikoresho cawe



*Umutekano wongerewe:*




- Gusubiza inyuma ubwo nyene ku mahinduka y'imiterere
- Decoy" gusubiza inyuma mu bihe bidasanzwe
- Hisha amahinduka y'ubunini bw'ububiko
- Uburinzi bwo gusesangura umwanya



*Inzira yo gusubizaho:*




- Indangamuntu n'urufunguzo biva ku Mutaka wawe seed
- Gusubizaho vyose birashoboka hakoreshejwe amajambo Mnemonic gusa
- Gusubiza ubwavyo amakuru aherutse gusubirwamwo
- Kugarura imirongo n'amakuru



### Gusubizaho impanuka



Niba node yawe yazimiye (ibikoresho vyananiwe, ikarita SD yononekaye) :




- Gusubira gushiramwo umutaka
- Injira amajambo yawe y'amajambo 24 seed muri porogaramu y'umuravyo
- Injira muri dosiye ya SCB mu gihe co kugarura



LND izohamagara umufatanyabikorwa wese w’imirongo yawe ya kera kugira ngo ayifunge kandi asubize umugabane wawe w’amahera ya On-Chain. Ivyo bibanza bizopfungwa ubuziraherezo (bizosubira gufungurwa nivyaba ngombwa).



### Kuboneka n'uburinzi bw'ubuhendanyi



Ivyiza ni uko wosiga urudodo rwawe kuri Internet kenshi bishoboka. Mu gihe umuntu amara igihe kirekire ataboneka:




- Umugenzi w'umubisha yoshobora kugerageza gutangaza umurongo wa kera
- Umuravyo utanga "igihe c'imyiyerekano" (nk'indwi 2 kuri LND)
- Nimba uzomara igihe kirekire uri kure, shiraho Watchtower .



**Imiterere ya Watchtower:**




- Mu miterere ya LND, wongereko URL ya server yizewe ya Watchtower
- Ushobora gukoresha igikorwa ca Leta canke ugashiramwo Watchtower yawe bwite.




Kugira ngo umenye vyinshi ku bijanye no gutunganya no gukoresha iminara y'ibarabara, turagusavye kuraba inyigisho yacu yihariye :



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Ibindi bikorwa vyiza





- Ivyagezwe vya porogaramu:** Gumana Umbrel na LND bigezweho (ivy'umutekano)
- Uburinzi bw'ibikoresho:** Koresha uburyo buhamye (Raspberry Pi ifise SSD, mini-PC) na UPS
- Umutekano w'urubuga:** Gumana imiterere ya Tor, hindura ijambobanga ry'umuyobozi wa Umbrel (imbere: "moneyprintergobrrr")
- Ububiko:** Gushoboza ububiko bwa disiki niba bishoboka



## 6. Ibindi bikoresho



Umbrel's Lightning Node app itanga ivy'ingenzi vyo gucunga imirongo yawe, ariko ibikoresho vy'abandi bitanga ibikorwa vy'ubuhinga buhanitse.



### Inkuba



Interface uburyo bwo gucunga umuravyo bushingiye ku rubuga rwa none bushobora gushirwako biciye ku iduka ry’amaporogarama rya Umbrel.



**Utuntu dutandukanye:**




- Igihe nyaco co kubona imirongo (ubushobozi, uburinganire)
- Ibikoresho vyo gusubiramwo uburinganire
- Gushigikira inzira nyinshi zo gutanga amafaranga (MPP)
- Kode ya QR y'uruvyaro LNURL
- Ubuyobozi bw'ibikorwa On-Chain



ThunderHub ni nziza cane mu kugenzura urudodo rw’inzira rukora no gukora ugusubiramwo kworoshe.



### Gutwara umuravyo (RTL)



Interface urubuga rujanye n’ibikorwa vyinshi vy’umuravyo (LND, Umuravyo w’ishimikiro, Eclair).



**Ibihambaye:**




- Ubuyobozi bw'imirongo myinshi
- Imbonerahamwe zishingiye ku mirongo
- Gushigikira uguhinduranya ubwato bwo munsi y'amazi (Umuravyo Loop)
- 2-ibintu vy'ukwemeza
- Gusohora/kwinjiza umurongo w'ububiko



RTL ni "icumu ry'ingabo z'Ubusuwisi" ryuzuye ryo gukoresha urudodo rw'umuravyo rufise uburyo bushingiye ku bahinga.



### Ibindi bikoresho vy'ingirakamaro





- Umuravyo Shell**: Umurongo w'itegeko (lncli) biciye ku mucukumbuzi
- BTC RPC Umugenzuzi & Mempool**: Gukurikirana Blockchain
- LNmetrics & Torq**: Isesengura ry'imikorere y'inzira
- Amboss & 1ML**: "Uburongozi bw'imibano" bw'uruzitiro rwawe (amazina y'ibanga, abo mubonana, isesengura ry'urubuga)



Ivyo bikoresho birashobora gushirwa mu gukanda guke gusa biciye ku Umbrel App Store, ata n’imwe igoye.



**Ibikoresho vy'inyongera:**




- [Inkuba.io - Ibiranga](https://inkuba.io) - Incamake y'ibiranga ThunderHub
- [Amakuru y'ugutwara umuravyo (RTL)](https://www.amakuru y'ugutwara umuravyo/) - Inyandiko za RTL
- [Dawidi Kaspar - Gusubira gufatanya biciye ku rubuga rwa ThunderHub] (https://blog.davidkaspar.com) - Inyobora ngirakamaro yo gusubira gufatanya
- [Inyigisho "Gucungera Ivyuma vy'Imiravyo"](https://github.com/openoms/ugucungera Ivyuma vy'Imiravyo) - Inyandiko ziteye imbere ku bakoresha ububasha



## Iciyumviro



Gukoresha node yawe bwite ya LND kuri Umbrel ni intambwe ihambaye mu bijanye n’ubusegaba bw’ivy’ubutunzi. Naho bisaba uruhara rw’abahinga kuruta umuti wo kubungabunga, inyungu mu bijanye no kugenzura, ubuzima bwite no kugira uruhara n’umwete muri Lightning Network ni nyinshi cane.



Mu gukurikiza iyi nzira, ubu ushobora gushiramwo LND, gufungura imirongo, gucunga amahera yawe no gushika ku nzira yawe uri kure. Niwiyumve ko ushobora gutohoza buhorobuhoro ibintu biteye imbere be n’ibindi bikoresho uko urushiriza kumenya ibidukikije.



Ibuka ko umutekano w’amahera yawe uvana n’ingene wirinda be n’ingene ukora. Fata umwanya wo gutahura umuce wose imbere y’uko ukora amahera menshi.