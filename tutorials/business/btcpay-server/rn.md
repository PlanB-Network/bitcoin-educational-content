---
name: BTCPay Server
description: Kwemera amahera ya BTC ata bahuza
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server ni porogaramu y’ubuntu, yuguruye, yakozwe na Nicolas Dorier ishobora gutuma amahera yishurwa ku bitcoin yemerwa ata n’umwe ayihuza. Igenewe gutanga ubwigenge n’ubusegaba bw’ivy’amahera, ishira kuri server yayo bwite kandi itanga uburongozi bwose bw’ibikorwa, kuva ku gutanga invoice gushika ku kwemeza amahera yishuwe on-chain canke Lightning Network, n’ugucungera amafaranga. Ifatanya mu buryo bworoshe n’imbuga z’ubudandaji (WooComerce, Shopify, n’ibindi) canke ishobora gukoreshwa nk’aho kwishura amaduka y’umubiri (*POS*).



BTCPay Server nta nkeka ni umuti uteye imbere cane ku bacuruzi bipfuza kwemera bitcoin. Ni porogaramu yuzuye kandi ikomeye cane mu bijanye n’umutekano, ubusegaba n’ibanga. Ku rundi ruhande, ni ryo kandi rigoye cane gushiramwo no kubungabunga. Hariho kandi uburyo bworoshe: bumwe bushobora gucungera, nka OpenNode, mu gihe ubundi butanga uburyo bushimishije bwo gusenyera ku mugozi umwe hagati y’ukworohereza gukoresha n’ubusegaba, nka Swiss Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Intumbero y’iyi nyigisho ni ukukuyobora intambwe ku yindi mu gushiramwo, gutunganya no gukoresha Server ya BTCPay, kugira ngo ushobore gukoresha ibikorwa remezo vy’ukwishura bitekanye kandi vyigenga bihuye n’imico kama ya Bitcoin.



## Ibirango vya Serveri ya BTCPay



Ivyiyumviro vy’ugucuruza vya Bitcoin, nka *OpenNode* nk’akarorero, bitanga uburyo bwo gukoresha, ariko vyizigira ishirahamwe ry’uwundi muntu kuko bidashobora kwiyakira kandi, kenshi na kenshi, ni ivy’umuntu. Naho vyoroha gushinga amahera, birimwo amafaranga y’amakomisiyo kandi bikaba bishira abakoresha bavyo mu bibazo vyinshi kuruta umuti nka BTCPay Server, haba mu bijanye no kubika amahera no mu bijanye n’ibanga.



BTCPay Server igenewe abacuruzi bo kuri internet canke ku mubiri, amashirahamwe n’imiryango idaharanira inyungu yipfuza kwakira intererano mu bitcoins. Ni umuti mwiza kandi ku bafise imigambi n’abayitegura barondera infashanyo itaziguye iva mu kibano cabo.



Ibintu bidasanzwe vya BTCPay Server ni :




- **ukwigenga kwayo kwose**,
- ukubura uburyo bwo gukora **KYC**,
- kugenzura neza amafaranga**,
- **ugukuraho amafaranga y’ibarabara**.



Mu kuba uwugufasha kwishura, ukuraho ukuvyifatamwo kwose ku muntu wa gatatu ari hagati yawe n’abaguzi bawe. Ushobora kwemera kwishura ataco uhinduye mu bitcoins no mu mafagitire y’ukwishyura generate. Ivyo bituma wewe canke ishirahamwe ryawe ata wundi mushobora kubuzwa. Ugira uruhara rwa banki n’urw’ugutanga amahera, utabwirizwa kwishura amakomisiyo ku muntu akora ubuhuza ku bijanye n’ugutanga amahera yose.



Amafaranga yo gukoresha **on-chain** aracariho, ariko ashobora kugabanywa hakoreshejwe urubuga rwa **Liquid** canke **Lightning**.



Kandi :




- Igikoresho gishobora guhindurwa mu buryo bushitse n’amafagitire;
- Infashanyo y’imvukira **Tor** ku bijanye n’ibanga ryongerekanye;
- Gushigikira **ugufasha abantu benshi**, **POS** na **ubuto bwo kwishura**;
- Ihuye n'amafaranga menshi ;
- Bitcoin kwishura ataco akora n’ugutanga amahera y’urunganwe ;
- Gucungera neza imfunguruzo zawe z’ibanga;
- Ubuzima bwite bwongerekanye ;
- Umutekano wongerewe ;
- Porogaramu yishingira ;
- Gushigikira **SegWit** na **Urusobe rw'umuravyo** ;
- Imbere, ibitabo bishingiye ku nzira, n'ugushiramwo ibitabo vy'ibikoresho.



## Gushiramwo no gutunganya Serveri ya BTCPay



### Guhitamwo uburyo bwawe bwo kwakira



BTCPay Server ishobora gushirwa mu buryo butandukanye. Bivanye n’ivyo ukeneye n’ivyo ufise, hariho uburyo butatu nyamukuru:




- BTCPay Server yakiriwe n’uwundi muntu**: ukoresha urubuga rukwakira iyo serivisi. Biroroshe, ariko kenshi si ubuntu.
- Server ya BTCPay yitunganije kuri server y’igicu** (nk’akarorero biciye ku [mutanga amafaranga](https://umutanga amafaranga.com/), [abantu ba Bitcoin](http://abantu ba bitcoin.it/) canke uwundi mutanga amafaranga wese). Uwo ni wo muti usabwa ku bacuruzi benshi bashasha.
- BTCPay Server ishizwe ku bikoresho vyawe bwite (mu karere)** : kuri mudasobwa, mini-PC canke Umbrel. Ubwo buryo burarushiriza kuba ubuhinga, ariko buratanga ubwigenge bwose.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Ku mucuruzi atanguye, **gushira kuri server y’igicu** ni co kintu ciza co gusenyera ku mugozi umwe hagati y’ukwigenga, ukworoha n’umutekano, ataco ukeneye gucunga ibikorwa remezo vyose vy’ubuhinga.



BTCPay Server ishobora gukoreshwa vuba cane ivuye ku mubare w’abatanga uburaro. Muri izo, **Voltage** igaragara nk’umuti w’ikigereranyo ku bakoresha basaba ibikorwa remezo **vyizigirwa**, **vy’umwuga** n’ibikorwa remezo **vy’ubutegetsi**.



### Rema urugero rwa Serveri ya BTCPay ku Muriro



**Voltage** ni urubuga rwo kwakira abashitsi rwa Bitcoin na Lightning rushobora kugufasha guca ukoresha Server yawe ya BTCPay, ata n’ugutunganya canke gusanasana server.



Sura [urubuga rwemewe rw’umuriro](https://umuriro.igicu).



![capture](assets/fr/03.webp)



Rema **konti y'ukoresha** ifise aderesi ya e-mail ibereye n'ijambobanga rikomeye.



![capture](assets/fr/04.webp)



Voltage itanga **ukugerageza kw'imisi 7 ku buntu**. Urashobora kubona ko inyuma y'imisi 7 y'igerageza ryacu ry'ubuntu, uzotumirwa kwiyandikisha ku giciro gihoraho c'**$25 ku kwezi** kugira ngo ukomeze **ugumana nodes zawe zikora**.



Umaze gukora konti yawe ya Voltage maze ukinjira ubwa mbere, uzoca urungikwa kuri paji y’intango, ifise ibice bibiri nyamukuru:




- Igice ca **Ibikorwa remezo** co gucunga ama node y’umuravyo, Bitcoin Core, Server ya BTCPay n’ibindi bikorwa vya Bitcoin mu gicu;
- n'igice ca **Ivyishyurwa** kigufasha gushika ku Muco wa API wa Voltage kugira ngo ushiremwo ivyishyurwa vya Bitcoin mu bikorwa vy'ubuhinga.



Kugira ngo ukoreshe **BTCPay Server** yawe, kanda kuri **Ibikorwa remezo vyo gushikako**. Aha niho ushobora kurema, gucunga no kugenzura ibikorwa vyawe vyose, harimwo node yawe ya Bitcoin na BTCPay Server.



#### Rema itsinda



Imbere y'uko ushobora gukoresha igikorwa, urubuga ruzogusaba **gukora umugwi**. **Itsinda** (ahantu h'akazi) ni ahantu h'akazi hahuriza hamwe ibikorwa vyawe vyose vya Bitcoin na Lightning (nk'akarorero, node, Server ya BTCPay, umushakashatsi, n'ibindi). Ni nk’aho ari dosiye irimwo imigambi yawe itandukanye.



![capture](assets/fr/05.webp)



Kubera intumbero z'iyi nyigisho, umugwi twaremye uzokwitwa **Genesis**. Ushobora kwongerako ifoto yawe iyo ubishaka. Ivyo bimaze gushika, ukande kuri buto **Create**. Ushobora gutumira abandi bakoresha ngo baje muri iryo tsinda, mbere ugahindura izina ry’iryo tsinda niwabishaka.



Kuri paji y'intango y'umugwi, amahitamwo menshi araboneka:




- Ivyuma vy'umuravyo** : gukoresha ivyuma vy'umuravyo vyuzuye (LND) ;
- Ivyuma vy'Ishingiro vya Bitcoin** : gutanguza ivyuma vy'ishimikiro vya Bitcoin ;
- Serveri ya BTCPay** : kwakira inkuru ya BTCPay yiteguye gukoreshwa;
- Konti za Nostr**: gucunga akaranga ka Nostr.



Gukoresha **kwemeza kabiri (2FA)** kugira ngo ukingire konti yawe n’ibikorwa vyawe (ubuto buboneka mu rangi itukura iyo buzimye).



![capture](assets/fr/06.webp)



Fyonda kuri **Server ya BTCPay** mu mahitamwo, hanyuma kuri **Gutanguza Iduka rya BTCPay**.



![capture](assets/fr/07.webp)



Voltage izoca igusaba **guhingura no gutunganya instance yawe ya BTCPay Server** mu guhitamwo **izina rya serivisi** (1) no gushoboza kwishura Lightning (2).



Uzokenera urudodo rw'umuravyo niwafata ingingo yo kwemera amahera y'umuravyo.



Niba udasanzwe ufise node ya Bitcoin canke Lightning, Voltage izogusaba ko uyikora ubwawe.



Fyonda kuri **Rema urudodo rw'umuravyo** (3) .



![capture](assets/fr/08.webp)



Igihe ugeze ku rubuga rwo kurema node, uzosabwa guhitamwo hagati y'imiterere **isanzwe** n'imiterere **y'umwuga**.



Ushobora kurema urudodo nyarwo (**Mainnet**) canke urudodo rwo kugerageza (**Testnet**). Hanyuma ukande kuri buto ya **Bandanya**.



![capture](assets/fr/09.webp)



Kuri iyi nyigisho, reka dukoreshe umugambi usanzwe. Injira **izina ry'urudodo**, **ijambobanga** hanyuma ukande buto ya **Rema**.



![capture](assets/fr/10.webp)



Inyuma y'ibihe bike, node yawe izotangura gukora kandi uzoshobora gufungura umurongo w'ubuntu ufise ubushobozi bwo kwakira 500.000 sats.



![capture](assets/fr/11.webp)



Hanyuma gatoyi iburyo, uzosanga amakuru yose ukeneye ku bijanye n’urudodo rwawe!



![capture](assets/fr/12.webp)



None ko twaronse node yacu ya Lightning, reka dusubire ku gushiramwo server yacu ya BTCPay. Ubu ushobora gukanda kuri buto **Rema BTCPay**.



![capture](assets/fr/13.webp)



Paje izofunguka iriko amakuru yawe y’injira, hamwe n’ubutumwa bugusaba guhindura ijambobanga ryawe rya mbere. Ivyo umaze kubikora, ukande kuri buto ya **Login Now** kugira ngo ushikire interface yawe.



![capture](assets/fr/14.webp)



Ni vyo! Server yawe ya BTCPay irateguwe gukoreshwa. Uzoca urungikwa kuri paji y'injira ya server yawe ya BTCPay.



![capture](assets/fr/15.webp)



Umaze kwinjira, ushireho **ububiko bwawe bwambere**:





- Muyihe **izina**.





- Hitamwo **amafaranga y'imbere** (EUR, USD, CFA, n'ibindi).





- Hitamwo **umutanga igiciro c'amahera** (nk'akarorero CoinGecko).



![capture](assets/fr/16.webp)



Uzoca urungikwa ku rubuga rw’iduka ryawe. Ku rubuga rwa dashboard, uzobona ko ubuto **Rema iduka ryawe** bufise ikimenyetso c'icatsi kibisi, kuko iyi ntambwe yaramaze kurangira.



![capture](assets/fr/17.webp)



Hanyuma gatoyi dufise ubuto **Gutegura wallet** na **Gutegura Lightning node**. Mu gihe cacu, twamaze gufatanya n’umurongo w’umuravyo ukoresha umuriro. Ntituzobwirizwa rero kubikora hano.



Reka tugende ku gutunganya igitabu. Fyonda ku buto **Gutunganya igitabu**.



Ko turiko turatangura na BTCPay Server, reka duhuze wallet iriho. Rero kanda **Huza igitabu kiriho**.



![capture](assets/fr/18.webp)



Utegerezwa rero guhitamwo **uburyo bwo kwinjiza**. Mu mahitamwo ariho, hitamwo **Injira urufunguzo rwa bose rwagutse**.



![capture](assets/fr/19.webp)



Mu guhuza wallet iriho, urashobora kwakira amahera yawe **utaziguye kuri iyi wallet yo hanze**, ata serveri ya BTCPay ishobora gushika ku rufunguzo rwawe rw’ibanga. Rero, naho server yoba yacitse canke urufunguzo rwa bose (`xpub`) rwaciwe, uwutera yoshobora kubona amateka yawe y’ibikorwa, ariko **ntibishoboka ko ashobora kuronka amahera yawe**.



Uhejeje gukanda kuri buto **Injira urufunguzo rwa bose rwagutse**, uzo **subirwamwo** kuri paji aho utegerezwa gutanga urufunguzo.



None reka turonke **urufunguzo rwa bose rwagutse**.



### Guhuza igikoresho ca Bitcoin wallet



Kugira ngo uronke amahera yawe, ukeneye gufatanya Bitcoin wallet n’iduka ryawe. Kugira ngo ubikore, urafise uburyo bwinshi:





- Igitabu c'ibikoresho** (Ledger, Igikoresho co gutera, Ikarata y'ubukonje...) ;





- Ibikoresho vya porogaramu** (Iporogaramu y'ububiko, Ashigaru, Electrum, Sparrow...)





- BTCPay Server** wallet yo mu mutima (ntivyiza, kuko idatekanye cane kandi igaragaza amahera yawe cane iyo umuntu yoba yateye server).



Muri iyi nyigisho, tuzokoresha **software portfolio**, ishobora gushikwako cane ku bijanye n'ugutunganya kw'intango. Ushobora guhitamwo mu bikoresho vyinshi bihuye: **Electrum**, **Phoenix**, ​​**Zewu**, **Muun**, n'ibindi.



Ku bijanye n'iyerekanwa, tuzokoresha **Electrum**. Gufungura **Electrum**, ukande kuri **Igitabo**, hanyuma ukande kuri **Amakuru** :



![capture](assets/fr/20.webp)



Inyuma, kopira **urufunguzo rwa bose (xpub)**.



![capture](assets/fr/21.webp)



Umaze gukopa urufunguzo rwa bose, urushire mu kibanza catanzwe kuri paji ya Serveri ya BTCPay.



![capture](assets/fr/22.webp)



Inyuma yo kugenzura, uzosubira ku rubuga rw’iduka ryawe.



![capture](assets/fr/23.webp)



### Gutanga ahantu h'ugurisha (PoS)



Umaze gushinga iduka ryawe n’ibiharuro vyawe, ubu urashobora gushinga **Point of Sale (PoS)** kugira ngo utangure kwakira amahera ya Bitcoin ataco akoresheje ku bakiriya bawe.



Iyi nzira yunze ubumwe ya **BTCPay Server** ni nziza ku **bacuruzi, abahinguzi b’ibintu, abagurisha canke abatanga ibikorwa** bipfuza kwemera Bitcoin **ata rubuga** canke ubuhinga budasanzwe.



### None ugurisha ni igiki?



**PoS** ni **interface ya POS yoroshe** ikora nk'**Ikibanza co kwishura Bitcoin**.


Biguha uburenganzira bwo :




- Rema **urutonde rw'ibintu canke ibikorwa** n'ibiciro bihoraho.
- Gutanga **invoice y'igihe nyene ifise kode ya QR** kugira ngo uyikoreshe.
- Sangira **URL yo kwishura** ishobora gushikwako biciye kuri telefone ngendanwa, tablette canke mudasobwa.



Mu yandi majambo, PoS ihindura Server yawe ya BTCPay ikaba **interface y’ugurisha ataco uhinduye**, aho amahera yose utanga **mu Bitcoin wallet yawe bwite**, ata bahuza.



### Gutunganya PoS



Mu rubuga rwa BTCPay, ukande kuri **PLUGINS**, hanyuma ukande kuri **Ikibanza co kugurisha**.



Hanyuma ukande kuri **Rema porogarama nshasha ya PoS**. Ico gikorwa congera **porogarama nshasha** ku bubiko bwawe bwa BTCPay, nk'aho woba uriko urashiraho urubuga rwo kugurisha rw'imbere ruto.



Paje irafunguka kugira ngo ureme ubusabe bwawe. Sigura **izina ry'ikoreshwa**: iri ni izina ry'imbere, riboneka gusa ku rubuga rwawe (nk'akarorero _Iduka ry'inkweto_).



Fyonda kuri **Rema** kugira ngo wemeze.



![capture](assets/fr/24.webp)



Iyo umaze kuremwa, uzosubira ku **Paje y'imiterere y'ido n'ido** y'Ikibanza c'Ugurisha.



### Guhindura ubucuruzi bwawe



Kuri iyi paji, ushobora gusobanura ibintu nyamukuru vya PoS yawe:





- Izina ry'ikoreshwa** (izina ry'uburongozi bw'imbere, rishobora guhindurwa igihe cose).





- Erekana umutwe** (ico abakiriya bawe bazobona hejuru kuri paji).





- Uburyo bwo kugurisha** (**Indondora** uburyo burabereye ku bikorwa nk’ugukata imisatsi canke gufungura, mu gihe uburyo bwa **Igitabo c’ibicuruzwa** burabereye ku maduka atanga ibicuruzwa vyinshi).





- Erekana amafaranga** (hitamwo **XOF**, **EUR** canke **USD** bivanye n’ibiciro vyawe bisanzwe).





- Urutonde rw'ibicuruzwa** (wongereko ibicuruzwa vyawe, insobanuro n'ibiciro hano).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Bika kandi ugerageze PoS yawe



Niwaheza gutegura, ukande kuri **Save** kugira ubike ama settings yawe, hanyuma **View** kugira ngo ubone PoS yawe.



Uzobona urupapuro rwerekana ibintu vyawe, buto yose ikaba ihuye n’ikintu canke igikorwa.



Umukiriya akimara guhitamwo igicuruzwa :



1. BTCPay ihita itanga invoice ya Bitcoin canke y’umuravyo**.



2. Ku rubuga hazoboneka **QR code**.



3. Abaguzi barashobora **gucapura no kwishura ataco baciye** bakoresheje Bitcoin wallet yabo.




![capture](assets/fr/27.webp)



### Inyishu yanyuma



Ubu ufise **Bitcoin Point y'Ugurisha** yuzuye ushobora :





- Gufungura ukoresheje telefone ngendanwa canke tablette iri mu iduka ryawe ;





- Erekana ku gicapo kugira ngo umukiriya ashobore gucapura ;





- Canke usangire biciye ku **URL** ya bose, nk'urupapuro rworoshe rwo gusaba.



Igihe cose urishe, ayo mahera aca yinjira muri **BTCPay wallet yawe bwite**, ata bahuza canke amahera y’uwundi muntu.


Ivyo bihindura PoS yawe ikaba **ikibanza co kwishura Bitcoin gihagazeko**.




## Gukoresha buri musi



Imbere yo gutanga amahera yose y’ukuri, turagusavye gukora **ikigeragezo** kugira ngo umenye nimba vyose bikora neza.



### Gerageza kwishura





- Rema invoice** ukoresheje interface yawe ya PoS (nk’akarorero, igicuruzwa ca 1 satoshi canke amahera make).





- Scan kode ya QR iri ku rubuga** ukoresheje Bitcoin canke wallet y’umuco (nk’**Phoenix**, **Muun** canke **Wallet ya Satoshi**).




![capture](assets/fr/28.webp)





- Kwemeza amahera** muri wallet yawe: amahera yoherezwa ubwo nyene.





- Subira kuri Server ya BTCPay**: invoice izoboneka nk'**Yishyuwe** muri list.



![capture](assets/fr/29.webp)



Urakoze cane! Igikoresho cawe co kugurisha ubu **kirakora**. Ushobora gutangura kwakira amahera ya Bitcoin ku bakiriya bawe, mu buryo bworoshe, bwihuta kandi ata bahuza.



### Rema inyemezabuguzi y'umukiriya



Mu **Ifagitire**, kanda kuri **Ifagitire nshasha**.



![capture](assets/fr/30.webp)



Injira **umubare** n’**amafaranga yo mu karere** (BTCPay ihita iharura ibingana muri BTC), hamwe n’ayandi makuru y’ibicuruzwa.



![capture](assets/fr/31.webp)



Sangira **QR code** canke **URL** n'umukiriya.



![capture](assets/fr/32.webp)



### Gukurikirana amafaranga yishuwe



Naho biri muri **Invoices**, uzobona urutonde rw'amahera yose ukoresheje.


Ivyo bishoboka ni :





- Pending**: ukwishyura ntikuraremezwa.





- Yishuwe**: kwishurwa kwemejwe.





- Igihe caheze**: invoice ntiyishuwe ku musi w’itegeko.



### Gusubiza umukiriya



Mu **Invoices**, hitamwo invoice uzosubizwa.



![capture](assets/fr/33.webp)



Fyonda kuri **Refund** hanyuma winjize aderesi Bitcoin yatanzwe n’umukiriya.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Raporo n'amakuru yoherezwa hanze



BTCPay Server iragufasha **gusohora amafaranga yawe** (mu buryo bwa CSV canke Excel). Ivyo birakora cane ku bijanye n’ugukurikirana ivy’ubuhinga bwawe bwo guharura amafaranga n’ivy’ugutanga amafaranga.



![capture](assets/fr/36.webp)



Mu **Raporo**, kanda kuri **Export**: amafaranga yawe yose azobikwa muri dosiye ya CSV, iyo ushobora guca uyibona aho hantu.



## Umutekano n'ibikorwa vyiza



Ukwigenga guhabwa na BTCPay Server (ubusegaba bushitse ku mahera yawe) ni inkomezi nyazo. Ariko uwo mwidegemvyo uzana n’inshingano nyinshi mu bijanye n’umutekano. Mu gucunga ivyo wishura, uba ufata uruhara rwa banki yawe bwite. Ni co gituma ari ngombwa cane gufata uburyo bwiza bwo kurinda amahera yawe, amakuru yawe n’ibikorwa remezo vyawe. Ehe ingingo nyamukuru zo kurimbura.



### Ukwinjira kuri server yawe





- Koresha ijambobanga rikomeye: ushiremwo inyuguti nini n’into, imibare n’inyuguti zidasanzwe. Irinde gusubira gukoresha ijambobanga ryariho.
- Gukoresha ivyemezo bibiri (2FA) kugira ngo ushikire urubuga rwawe rwa BTCPay.
- Uhora uhindura ubuhinga bwawe bwo gukoresha, urugero rwa Server yawe ya BTCPay n’ibindi bigufasha (Docker, urudodo rwa Bitcoin, urudodo rwa Lightning...). Ivyo guhindura kenshi birakosora ubugoyagoye bwo mu mutekano.



### Gucungera no gusubiza inyuma imfunguruzo z'ibanga





- Bika imfunguruzo zawe z’ibanga n’amajambo y’imbuto ata murongo, ku bimenyeshamakuru vy’umubiri (impapuro canke ivyuma).
- Ivyiza ni uko ukoresha ibikoresho vya wallet wallet.
- Bika kopi nyinshi z’ivyo mwabitse, mu bibanza bitandukanye kandi birinzwe.



### Ukwishurwa gutekanye n'ibanga





- Koresha urubuga rwa Tor canke VPN kugira ngo uhishe aderesi IP ya server yawe kandi ukinge ubuzima bwite bwawe.
- Guhagarika ivyuho bidakenewe kuri server yawe no kubuza amahuzwa ya SSH ku ma aderesi yizewe gusa.
- Gukoresha HTTPS (icemezo ca SSL) ku mahuriro yose ku rubuga rwawe rwa BTCPay.
- Ntukigere usangira uburongozi bwawe n’abakozi batamenyerejwe mu bijanye n’uburongozi bw’ibikorwa vya Bitcoin.



### Gushira mu ngiro ingendo nziza ku rubuga rwa Lightning



Iduka ryawe rifatanye n'**Lightning node yakira kuri Voltage**, ivyo bikaba vyorosha cane uburongozi bw'ubuhinga bw'urubuga. Naho biri ukwo, biracari bihambaye kwemera **uburyo bwiza bwo kugenzura no gucungera umutekano**:





- Bika imfunguruzo zo kwinjira no gushika ku nzira ya Voltage node yawe API** (zituma BTCPay ishobora kwifatanya).
- Rinda konti yawe ya Voltage** n’ivyemezo bibiri n’ijambobanga rikomeye.
- Gukurikirana urudodo n'imirongo** kuva ku rubuga rwawe rw'umuriro: ivyo bigufasha kubona ibintu bitari vyo canke ukudakorana.
- Irinde gusangira amakuru yawe ya API** canke kuyashira ahabona ku mugaragaro (nk’akarorero muri kode y’urubuga).
- Mu gihe co kwimuka, **subiramwo gusa uruja n’uruza hagati ya BTCPay na Voltage**: nta murongo ukeneye gupfungwa n’amaboko.



Ukoresheje Voltage, wungukira ku **bikorwa remezo bitekanye, biboneka cane** kandi **bifashwa ubwavyo**, mu gihe uguma ufise **ubusegaba bwose ku mahera yawe ya Lightning**.



### Gutunganya no gutunganya uburyo bwo gukora imbere





- Sigura ingingo ngenderwako zitomoye zo gucunga: ni nde ashobora gukora invoice, kuraba ivyo kwishura, gushika ku nzira, n'ibindi.
- Inyandiko yawe y’ububiko n’uburyo bwo kugarura kugira ngo ushobore gukora ningoga iyo habaye ikintu.
- Ugerageze ubudasiba gusubizaho ama backups yawe kugira ngo umenye neza ko akora neza.
- Toza abakozi bawe canke abo mukorana mu mutekano w’ishimikiro w’ibikorwa: kwiyubara ku bijanye n’ubuhendanyi, gukoresha amajambo y’ibanga atekanye, kwubahiriza ibanga.



### Kugenzura no gushinga ubuzima buhoraho





- Gukomeza gukurikirana ibikorwa vya server yawe ukoresheje ibikoresho vyo gufata canke gukurikirana.
- Gutegura isuzuma ry'umutekano ry'ibihe bidasanzwe: gusuzuma ivyahinduwe, kuronka, gusubiza inyuma n'uguhuza kw'ibikorwa.



Urakoze cane! Washitse ku mpera y’iyi nyigisho. Ubu ushobora gukoresha BTCPay Server wewe nyene, bikagufasha gucunga neza iduka ryawe.



Kugira ngo umenye vyinshi, ndagusavye gufata inyigisho yacu yuzuye ku bijanye no kwinjiza Bitcoin mw’ishirahamwe ryawe:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a