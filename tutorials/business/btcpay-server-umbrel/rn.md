---
name: BTCPay Server - Umbrel
description: Gushiramwo no gukoresha Server ya BTCPay ku Mutaka kugira ngo wemere Bitcoin n'Umuravyo
---

![cover](assets/cover.webp)



Mu bidukikije vya Bitcoin, kwemera kwishura bigereranya ingorane ikomeye ku bacuruzi n’abacuruzi. Inyishu za kera, zaba izo mu mabanki (amakarata y’inguzanyo, Stripe, PayPal) canke mbere Bitcoin (BitPay, Coinbase Commerce), zitegeka abahuza bafata amahera menshi, bagakorakoranya amakuru yawe y’ubudandaji y’agaciro, kandi bagashobora guhagarika canke gucengera amafaranga yawe uko bashaka. Ukwo kwisunga guhushanye n’ingingo ngenderwako z’ishimikiro za Bitcoin zo kwegereza ubutegetsi abaturage, ibanga n’ubusegaba bw’ivy’ubutunzi.



BTCPay Server iriko iraseruka nk’inyishu y’inkomoko yuguruye y’iki kibazo. Iyi nzira y’ukwishura yitunganije ihindura uruzitiro rwawe rwa Bitcoin mu bikorwa remezo vy’umwuga, ata muntu wo hagati, ata mahera y’inyongera yo kwishura kandi ata gusenyura ubuzima bwite. Yateguwe n’umuryango w’abaterankunga kw’isi yose kuva mu 2017, BTCPay Server iragufasha kwakira amahera ya Bitcoin na Lightning ataco uhinduye mu bipapuro vyawe, ugakomeza kugenzura neza amahera yawe ibihe vyose.



Mu migenzo, gushiramwo BTCPay Server bisaba ubuhinga buhanitse: Gutunganya server ya Linux, kumenya neza Docker, gucunga icemeza SSL n’umutekano w’urubuga. Umbrel ihindura ubu buryo n’ugushiramwo ibintu bimwe bimwe bifatanye n’uruzitiro rwawe rwa Bitcoin n’urw’umuravyo. Ukwo kworohereza ibintu bituma ivyo mbere vyari bigenewe abahinga bazi utuntu n’utundi bishikira umuntu wese.



**Ivyiza gutahura**: BTCPay Server kuri Umbrel ikora ku buryo busanzwe ku rubuga rwawe rwo mu karere gusa. Ushobora gukora invoice, kwemera kwishura Lightning na Bitcoin, no gucunga ubuhinga bwawe bwo guharura amafaranga ukoresheje igikoresho cose gifatanye n’urubuga rwawe rwo muhira (mudasobwa, telefone ngendanwa, tablette). Iyi ntunganyo ni nziza cane mu gutanga amafaranga y’ibikorwa vy’umuntu ku giti ciwe, gucunga amafaranga y’amaso mu yandi, canke gukoresha Server ya BTCPay ukoresheje urubuga rwawe rwo mu karere. Ku rundi ruhande, kugira ngo BTCPay Server ishire mu bubiko bwo kuri internet bushobora gukoreshwa na bose kuri Internet, bizokenerwa ko habaho iyindi ntunganyo ishobora gukoreshwa na bose (tuzovuga kuri iki kibazo mu mpera y’inyigisho).



Iyi nyigisho iragutwara mu gushiramwo Server ya BTCPay kuri Umbrel, gutunganya node yawe ya Bitcoin wallet na Lightning, guhingura no kwishura invoice, no gucunga raporo y’ivy’itunganywa ry’amafaranga. Uzobona ingene ukoresha neza BTCPay Server ku rubuga rwawe rwo mu karere, hanyuma turabe inyishu zo kugaragaza abantu bose nimba ushaka kuyifatanya n’urubuga rw’ubudandaji.



## Ibisabwa



Kugira ngo ukurikire iyi nyigisho, ukeneye kugira Umbrel ishizwemwo neza kandi ikatunganirizwa neza. Niba utarabikora, raba inyigisho yacu ku bijanye no gushiramwo Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Igikoresho cawe ca Bitcoin Core gitegerezwa kuba gihuye neza n’uruzitiro rw’amabuye (100% mu gikorwa ca Bitcoin ca Umbrel). Ukwo gukorana kw’intango akenshi gutwara hagati y’imisi 3 n’indwi 2, bivanye n’ibikoresho vyawe n’uburyo ukoresha Internet.



Kugira ngo wemere amahera y’umuravyo ako kanya, uzokenera kandi gushiramwo LND (Lightning Network Daemon) kuri Umbrel. Raba inyigisho yacu yo gushiramwo no gutunganya LND kuri Umbrel nimba ushaka gukoresha iki gikoresho.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Kwemerera nibura 50 GB y’umwanya w’ubuntu kuri disiki ya BTCPay Server, amakuru yayo n’amakuru ya Lightning. Internet ihamye biciye ku nzira ya Ethernet ni ngirakamaro cane kugira ngo ntihagire uwucika.



## Gushiramwo Serveri ya BTCPay ku Mutaka



Kuva ku rubuga rwa Umbrel (`umbrel.local`), genda muri App Store maze urondere "Server ya BTCPay" mu rwego rwa Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Fyonda Shiraho. Umbrel ihita isuzuma ko Bitcoin Core na LND vyashizwemwo, hanyuma igatangura gukoresha (iminota 2-5).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Iyo umaze gushiramwo, fungura iyo porogarama. Uzokenera gukora konti y'umuyobozi ifise ivyemezo bikomeye.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Konti yawe imaze gukorwa, BTCPay Server izoca ikubwira ngo ushireho iduka ryawe rya mbere. Hitamwo izina ry’ubucuruzi hanyuma uhitemwo amafaranga y’ishingiro (EUR, USD canke BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Ushike kuri Server ya BTCPay ku rubuga rwawe rw'aho uba



Server ya BTCPay ishobora gukoreshwa n’igikoresho cose kiri ku rubuga rwawe (WiFi canke Ethernet). Ushobora gushika kuri :



```url
http://umbrel.local
```



Canke ushire kuri :



```url
http://umbrel.local:3003
```



**Ukwinjira kure ukoresheje Tailscale**: Kugira ngo ushikire Server ya BTCPay uri aho hose kw’isi, koresha Tailscale. Iyi VPN itekanye iragufasha kwifatanya na Umbrel yawe nk’aho woba uri ku rubuga rwawe rwo mu karere. Raba inyigisho yacu yerekeye Tailscale ku Mutaka.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Gutunganya ibitabo vyawe vya Bitcoin



Kugira ngo wemere kwishura, ukeneye gutunganya Bitcoin wallet. BTCPay Server yerekana amahitamwo y'imiterere mu rutonde rw'ibikoresho.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Kugira ngo utunganye wallet Bitcoin, genda kuri "Ibikapu" > "Bitcoin".



Ufise uburyo bubiri: gukora igitabu gishasha mu buryo butaziguye muri BTCPay, canke ushiremwo igitabu kiriho. Ku bijanye no kwinjiza ibintu hanze, hari uburyo bwinshi:




- Huza ibikoresho wallet** (ni vyiza): Injira imfunguruzo zawe za bose biciye ku gikorwa ca Vault
- Injira dosiye wallet** (ni vyiza): Shira dosiye yoherejwe hanze ivuye mu bitabo vyawe
- Injira urufunguzo rwa bose rwagutse**: Injira XPub/YPub/ZPub yawe n'amaboko
- Gucapura kode ya QR ya wallet** : Gucapura kode ya QR kuva ku nkoko y'ubururu, ububiko bwa Cobo, pasiporo canke Spectre DIY
- Injira wallet seed** (ntivyiza) : Injira amajambo yawe yo gusubirana y'amajambo 12 canke 24



![Options de création de portefeuille](assets/fr/06.webp)



Ku bw'iyi nyigisho, tugiye gukora Hot wallet nshasha: urufunguzo rw'ibanga rero ruzobikwa kuri server yacu ya Umbrel. Muri ivyo, turaguhanura cane ko wokwimurira amahera ubudasiba kuri wallet ikaze kugira ngo wirinde kubika amahera menshi kuri server.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Iyo imaze gutunganirizwa, BTCPay Server yemeza ko wallet yawe yiteguriye kwemera amahera ya on-chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Gukoresha Lightning Network



Kugira ngo wemere amahera y’umuravyo ako kanya, genda kuri Wallets > Umuravyo. Hanyuma, nk'uko node yawe ya LND isanzwe iri mu kibanza kuri Umbrel, gusa ukande kuri buto ya "Bika" kugira ngo wemeze ko hariho isano hagati ya Server yawe ya BTCPay n'node yawe ya Lightning.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Rema kandi wishyure amafagitire



Mu kigaragaza Server ya BTCPay, genda kuri Invoice > Rema Invoice. Injira umubare, wongereko insobanuro y’ubuhinga, hanyuma ukande Rema.



![Création d'une nouvelle facture](assets/fr/10.webp)



Ushobora rero gukanda kuri buto ya "Checkout" kugira ngo ubone invoice. BTCPay ica itanga invoice irimwo kode ya QR imwe (BIP21) irimwo aderesi ya Bitcoin n’invoice ya Lightning.



![Détails de la facture générée](assets/fr/11.webp)



Umukiriya wawe arashobora gucapura kode ya QR n’iyindi yose ihuye na wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Iyo umaze kwishura, iyo fagitire iba "Settled" mu masegonda makeyi kuri Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Ubuyobozi bw'ukwishyura no gukurikirana



Mu gice ca "Gutanga raporo", "Ifagitire", uzosanga amateka yuzuye y'amafagitire yawe n'itariki, umubare, uko ameze n'uburyo bwo kwishura. Ushobora kuyirungika hanze iyo bisabwe.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Ububiko buboneza



BTCPay Server iragufasha gucunga amaduka menshi afise amaparametere atandukanye. Iduka ryose riserukira ikigo c’ubudandaji gitandukanye: iduka ry’ubudandaji ryo kuri interineti, ahantu h’ugurisha, canke amafaranga y’ibikorwa.



Mu mirongo y’iduka, uzosangamwo ibice bihambaye vyinshi:



![Paramètres du magasin](assets/fr/15.webp)





- Amategeko rusangi**: Izina ry’iduka, amafaranga y’ishingiro (BTC, EUR, USD), igihe c’uguhera kw’inyemezabuguzi (iminota 15), umubare w’ivyemezo vy’uruhererekane bisabwa
- Ibiciro**: Gutunganya inkomoko z'ibiciro vy'amahera n'uguhindura fiat/Bitcoin
- Uko Usohora**: Guhindura ukuntu amapaji yawe yo gusohoka asa (ikimenyetso, amabara, ubutumwa bwihariye)
- Amagenamiterere ya imeyili**: Gutunganya amatangazo ya imeyili y'amahera yakiriwe
- Ivyerekana **: Uburongozi bw'ibimenyetso vya API ku bijanye n'ubudandaji bwo kuri interineti (WooCommerce, Shopify, n'ibindi)
- Abakoresha**: Gucungera uburenganzira bw'abakoresha bwo kwinjira mu bubiko n'ingero zitandukanye z'uburenganzira (Nyene, Umushitsi)
- Webhooks**: Itunganywa ry'urubuga kugira ngo rihuze mu gihe nyaco n'ubuhinga bwawe bwo guharura amafaranga canke ubuhinga bwa ERP



BTCPay Server kandi itanga igice c’Ibikoresho kugira ngo yongere ibikorwa n’ubudandaji bwo kuri interineti, uburyo bwo kugurisha n’ibindi bikoresho.



![Gestion des plugins](assets/fr/16.webp)



## Inyungu n'imipaka y'ikoreshwa ry'aho hantu



**Ivyiza vya Server ya BTCPay ku Mutaka** :




- Ubusegaba bwose: ubugenzuzi bwihariye bw'imfunguruzo n'amahera y'ibanga, nta wundi muntu ashobora guhagarika canke gucengera amahera yawe
- Ivyo kuzigama vyinshi: igiciro c’urubuga rwa Bitcoin gusa (amasenti makeyi ku Lightning) n’ibice 2-3% ku bikoresho vya kera
- Ibanga ryinshi: nta kwandikisha, kugenzura akaranga canke gusangira amakuru n'amashirahamwe y'abandi
- Ubwubatsi bufise inkomoko yuguruye buratanga icemezo c'uguseruka, ugusuzuma n'ubuzima buramba biciye mu muryango munini w'abahinguzi
- Gushiramwo biroroshe biciye ku Mutaka, ata buhinga buhanitse bukenewe



**Imipaka ihambaye** :




- Urubuga rwo mu karere gusa**: Server ya BTCPay kuri Umbrel ishobora gukoreshwa gusa ukoresheje urubuga rwawe rwo muhira. Ni vyiza ku gutanga amafaranga amaso mu yandi, ibikorwa vy’ukwikorera canke ubucuruzi buto buto, ariko ntibibereye ku maduka yo kuri internet ashobora gushikirwa na bose.
- Inshingano yuzuye y'ubuhinga: gucungera urudodo, gucungera ubudasiba, gukurikirana ubufatanye
- Uburongozi bw'amahera y'umuravyo: gufungura no gucunga imihora ifise ubushobozi buhagije bwo kwinjira
- Infashanyo igarukira ku nyandiko z’abanyagihugu n’amahuriro, bisaba kwigenga kuruta igisata c’ubudandaji gifasha abakiriya



Uwo murongo w’urubuga rwo mu karere ni wo nzitizi nyamukuru yo gushiramwo BTCPay Server mu iduka ry’ubudandaji ryo kuri interineti, aho abakiriya bakeneye kuba bashoboye gushika ku mapaji y’ukwishura aho bari hose kuri Internet.



## Ibikorwa vyiza n'umutekano



Gukoresha ububiko bwa Umbrel bwikora no kubika kopi ku bimenyeshamakuru vyo hanze (inkoni ya USB, disiki ikomeye, igicu gipfutse). Bika imbuto zawe za Bitcoin (amajambo yo gukira) ahantu hatagira umutekano, hatandukanye n’abandi ku mubiri. Gusubiza inyuma dosiye ya LND y’umurongo.gusubiza inyuma kugira ngo umuravyo ubone gukira.



Gukurikirana ubudasiba uguhuza kwa Bitcoin Core, imirongo y’umuravyo n’inyishu ya Server ya BTCPay. Ikigeragezo coroshe c’indwi ku yindi: generate no kwishura amafaranga y’amasatoshi makeyi. Gumana Umbrel ku gihe (ibice vy’umutekano, ivyiza). Kora backup imbere y’uko uhindura ibintu bikomeye. Kugira ngo ukoreshe mu vy’umwuga, zirikana ugukurikirana hanze (UptimeRobot) n’imburi z’ubutumwa bwo kuri e-mail/SMS.



## Gushira ahabona BTCPay Server ku bubiko bwo kuri internet



Kugira ngo ushire BTCPay Server mu bubiko bw’ubudandaji bushingiye ku rubuga (WooCommerce, Shopify, n’ibindi), abakiriya bawe barakeneye kuba bashoboye gushika ku mapaji y’ukwishura aho bari hose, atari urubuga rwawe rwo mu karere gusa.



**Umuti: Umuyobozi w'Igihugu ca Nginx**



Ushobora gushikiriza Server ya BTCPay ku mugaragaro ukoresheje Umuyobozi w’Igihugu ca Nginx (uboneka mu Bubiko bw’Ibikoresho vya Umbrel). Uyu muti usaba :




- Izina ry'indangarubuga (ry'imbere canke ry'ubuntu biciye kuri DuckDNS, Nta-IP, Afraid.org)
- Gutunganya ivyuho vy'imbere (ivyuho 80 na 443) kuri router yawe
- Gushiramwo Nginx Proxy Manager, icungera ubwo nyene ivyemezo vya SSL



Ivyo bituma server yawe ibona Internet kandi bisaba ko wiyubara cane (amajambo y’ibanga akomeye, 2FA, guhindura ibintu bihoraho). Tuzoba turiko turategura inyigisho yihariye idondora neza iyo nzira yuzuye.



## Iciyumviro



BTCPay Server kuri Umbrel ifatanya ububasha bw’urudodo rwa Bitcoin n’uburyo bworoshe bwa Umbrel kugira ngo ireme ibikorwa remezo vy’ukwishura vy’umwuga vy’umwuga vyishikira bose. Ubwo busegaba bw’ivy’amahera buzana n’inshingano yo kubibungabunga, ariko Umbrel yorosha cane umuzigo w’ibikorwa ugereranyije n’ivyiza: gukuraho amafaranga yo gukora, kurinda ubuzima bwite bwawe, kunanira gucengera no kugenzura vyose amafaranga yawe.



Ikoreshwa ry’urubuga rwo mu karere rirasanzwe rifise ibikorwa vyinshi: gutanga amafaranga y’ibikorwa vy’ukwikorera, kwishura umuntu ku giti ciwe, amaduka matomato y’umubiri, canke gusa kwiga no kugerageza Bitcoin na Lightning mu kibanza gicunzwe. Ku bikenewe mu bucuruzi bwo kuri interineti bisaba gushirwa ahabona na bose, umuti wa Nginx Proxy Manager urahari, ariko usaba ibindi bikoresho vy’ubuhinga, ivyo tuzobidondora mu nyigisho yihariye.



Waba uriko urakora ubucuruzi, umugambi mushasha canke uriko uragerageza gusa, BTCPay Server kuri Umbrel itanga ubwigenge bwose bw’amahera. Inzira itangura n’iduka ryawe rya mbere, invoice yawe ya mbere, amahera yawe ya mbere waronse ataco uhinduye mu bikorwa remezo vyawe vy’ubutegetsi.



## Ubutunzi



### Inyandiko zemewe




- [Urubuga rwemewe rwa Serveri ya BTCPay](https://serveri ya BTCPay.org)
- [Inyandiko z'umukozi wa BTCPay](https://inyandiko.btcpay.org)
- [GitHub BTCPay Serveri](https://github.com/umukozi w'amahera/umukozi w'amahera)
- [Inyandiko z'umurizo](https://umurizo.com/kb)


### Umuryango n'infashanyo




- [Ihuriro rya BTCPay Server](https://ikiganiro.btcpay.org)
- [Umutaka w'ihuriro](https://umuryango.getumutaka.com)
- [Igikoresho co kwishura kuri BTCP]