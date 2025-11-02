---
name: BTCPAY SERVER - Umutaka
description: Gushiramwo no gukoresha BTCPAY SERVER kuri Umbrel kugira ngo wemere Bitcoin na Lightning
---

![cover](assets/cover.webp)



Mu bidukikije vya Bitcoin, kwemera kwishura bigereranya ingorane ikomeye ku bacuruzi n’abacuruzi. Inyishu za kera, zaba izo mu mabanki (amakarata y’inguzanyo, Stripe, PayPal) canke mbere Bitcoin (BitPay, Coinbase Commerce), zitegeka abahuza bafata amahera menshi, bagakorakoranya amakuru yawe y’ubudandaji y’agaciro, kandi bashobora BLOCK canke bagacengera amafaranga yawe ku bushake bwabo. Ukwo kwisunga guhushanye n’ingingo ngenderwako z’ishimikiro za Bitcoin zo kwegereza ubutegetsi abaturage, ibanga n’ubusegaba bw’ivy’ubutunzi.



BTCPAY SERVER iriko iraseruka nk’inyishu y’inkomoko yuguruye y’iki kibazo. Iyi nzira yo kwishura yitunganije ihindura uruzitiro rwawe rwa Bitcoin mu bikorwa remezo vy’umwuga, ata muntu wo hagati, ata mahera y’inyongera yo kwishura kandi ata gusenyura ubuzima bwite. Yateguwe n’umuryango w’abaterankunga wo kw’isi yose kuva mu 2017, BTCPAY SERVER iragufasha kwakira amahera ya Bitcoin n’aya Lightning ataco ushize mu bipapuro vyawe, ugakomeza kugenzura neza amahera yawe ibihe vyose.



Mu migenzo, gushiramwo BTCPAY SERVER bisaba ubuhinga buhanitse: Gutunganya server ya Linux, kumenya Docker, gucunga icemeza SSL n’umutekano w’urubuga. Umbrel ihindura ubu buryo n'ugushiramwo gukanda rimwe gusa bifatanye na Bitcoin na LIGHTNING NODE yawe. Ukwo kworohereza ibintu bituma ivyo mbere vyari bigenewe abahinga bazi utuntu n’utundi bishikira umuntu wese.



**Ivyiza gutahura**: BTCPAY SERVER kuri Umbrel ikora ku buryo busanzwe ku rubuga rwawe rwo mu karere gusa. Ushobora gukora amafagitire, kwemera kwishura Lightning na Bitcoin, no gucunga ubuhinga bwawe bwo guharura amafaranga ukoresheje igikoresho cose gifatanye n’urubuga rwawe rwo muhira (mudasobwa, telefone ngendanwa, tablette). Iyi ntunganyo ni nziza cane mu gutanga amafaranga y’ibikorwa vy’umuntu ku giti ciwe, gucunga amahera y’amaso mu yandi, canke gukoresha BTCPAY SERVER uhereye ku rubuga rwawe rwo mu karere. Ku rundi ruhande, kugira ngo BTCPAY SERVER ishire mu iduka ryo kuri internet rishobora gukoreshwa na bose kuri Internet, bizokenerwa ko habaho iyindi ntunganyo ishobora gushikirizwa abantu bose (iki kibazo tuzokivuga ku mpera y’inyigisho).



Iyi nyigisho iragutwara mu gushiramwo BTCPAY SERVER yose kuri Umbrel, gutunganya Bitcoin Wallet na LIGHTNING NODE yawe, guhingura no kwishura invoice, no gucunga raporo y’ivy’itunganywa ry’amafaranga. Uzomenya ingene wokoresha neza BTCPAY SERVER ku rubuga rwawe rwo mu karere, hanyuma tuzovuga ibijanye n’ingene woyigaragaza ku mugaragaro nimba ushaka kuyishira ku rubuga rw’ubudandaji rwo kuri interineti.



## Ibisabwa



Kugira ngo ukurikire iyi nyigisho, ukeneye kugira Umbrel ishizwemwo neza kandi ikatunganirizwa neza. Niba utarabikora, raba inyigisho yacu ku bijanye no gushiramwo Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Igikoresho cawe ca Bitcoin core kigomba kuba gihuye neza na Blockchain (100% mu gikorwa ca Umbrel ca Bitcoin). Ukwo gukorana kw’intango akenshi gutwara hagati y’imisi 3 n’indwi 2, bivanye n’ibikoresho vyawe n’uburyo ukoresha Internet.



Kugira ngo wemere amahera y’umuravyo ako kanya, uzokenera kandi gushiramwo LND (Lightning Network Daemon) kuri Umbrel. Raba inyigisho yacu ku gushiramwo no gutunganya LND kuri Umbrel nimba ushaka gukoresha iki gikoresho.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Reka nibura 50 GB z’umwanya w’ubuntu kuri disiki ya BTCPAY SERVER, amakuru yayo n’amakuru ya Lightning. Internet ihamye biciye ku nzira ya Ethernet iraremeshwa cane kugira ngo ntihagire uwucika.



## Gushiramwo BTCPAY SERVER ku Mutaka



Kuva ku Mutaka Interface (`umutaka.local`), genda kuri App Store urondere "BTCPAY SERVER" mu rwego rwa Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Fyonda Shiraho. Umbrel ica isuzuma ko Bitcoin core na LND zishizweho, hanyuma igatangura gukoresha (iminota 2-5).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Iyo umaze gushiramwo, fungura iyo porogarama. Uzokenera gukora konti y'umuyobozi ifise ivyemezo bikomeye.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Konti yawe imaze gushirwaho, BTCPAY SERVER izoca ikubwira ubwo nyene gushinga iduka ryawe rya mbere. Hitamwo izina ry’umwuga maze uhitemwo amafaranga y’ishingiro (EUR, USD canke BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Ushike kuri BTCPAY SERVER ku rubuga rwawe rw'aho uba



BTCPAY SERVER ushobora kuyironka ukoresheje igikoresho cose kiri ku rubuga rwawe rwo mu karere (WiFi canke Ethernet). Ushobora gushika kuri :



```url
http://umbrel.local
```



Canke ushire kuri :



```url
http://umbrel.local:3003
```



**Ushobora gushika kure ukoresheje Tailscale**: Kugira ngo ushikire BTCPAY SERVER uri aho hose kw'isi, koresha Tailscale. Iyi VPN itekanye iragufasha kwifatanya na Umbrel yawe nk’aho woba uri ku rubuga rwawe rwo mu karere. Raba inyigisho yacu yerekeye Tailscale ku Mutaka.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Gutunganya ibitabo vyawe vya Bitcoin



Kugira ngo wemere kwishura, ukeneye gutunganya Bitcoin Wallet. BTCPAY SERVER yerekana amahitamwo y’imiterere mu gicapo.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Kugira ngo utunganye Wallet Bitcoin, genda kuri "Ibikapu" > "Bitcoin".



Ufise uburyo bubiri: gukora igitabu gishasha mu buryo butaziguye muri BTCPay, canke ushiremwo igitabo ca kera. Ku bijanye no kwinjiza ibintu hanze, hari uburyo bwinshi:




- Huza Hardware Wallet** (ni vyiza): Injira imfunguruzo zawe za bose biciye ku gikorwa ca Vault
- Injira dosiye Wallet** (ni vyiza): Shira dosiye yoherejwe hanze ivuye mu bitabo vyawe
- Injira urufunguzo rwa bose rwagutse**: Injira XPub/YPub/ZPub yawe n'amaboko
- Gucapura kode ya QR ya Wallet** : Gucapura kode ya QR kuva ku nkoko y'ubururu, ububiko bwa Cobo, pasiporo canke Spectre DIY
- Injira Wallet seed** (ntivyiza) : Injira amajambo yawe y'ugusubirana y'amajambo 12 canke 24



![Options de création de portefeuille](assets/fr/06.webp)



Ku bw'iyi nyigisho, tugiye gukora Hot Wallet nshasha: urufunguzo rw'ibanga rero ruzobikwa kuri server yacu ya Umbrel. Muri ivyo, turaguhanura cane ko wokwimurira amahera ubudasiba kuri Cold Wallet kugira wirinde kubika amahera menshi kuri server.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Iyo imaze gutunganirizwa, BTCPAY SERVER yemeza ko Wallet yawe yiteguriye kwemera amahera ya On-Chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Gukoresha Lightning Network



Kugira ngo wemere amahera y’umuravyo ako kanya, genda kuri Wallets > Umuravyo. Hanyuma, nk'uko node yawe ya LND isanzwe iri mu kibanza cayo kuri Umbrel, gusa ukande kuri buto ya "Bika" kugira ngo wemeze isano hagati ya BTCPAY SERVER yawe na LIGHTNING NODE yawe.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Rema kandi wishyure amafagitire



Mu Interface BTCPAY SERVER, genda kuri Inyemezabuguzi > Rema Invoice. Injira umubare, wongereko insobanuro y’ubuhinga, hanyuma ukande Rema.



![Création d'une nouvelle facture](assets/fr/10.webp)



Ushobora rero gukanda kuri buto ya "Checkout" kugira ngo ugaragaze Invoice. BTCPay rero itanga Invoice ifise kode ya QR imwe (BIP21) irimwo Bitcoin Address n’umuravyo Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Umukiriya wawe arashobora gucapura kode ya QR akoresheje Wallet iyo ari yo yose ihuye.



![Page de paiement avec QR code](assets/fr/12.webp)



Iyo imaze kwishurwa, Invoice iba "Settled" mu masegonda make kuri Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Ubuyobozi bw'ukwishyura no gukurikirana



Mu gice ca "Gutanga raporo", "Ifagitire", uzosangamwo amateka yose y'amafagitire yawe, n'itariki, umubare, uko ameze n'uburyo bwo kwishura. Ushobora kuyirungika hanze iyo bisabwe.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Ububiko buboneza



BTCPAY SERVER iragufasha gucunga amaduka menshi afise amaparametere atandukanye. Iduka ryose riserukira ikigo c’ubudandaji gitandukanye: iduka ry’ubudandaji ryo kuri interineti, ahantu h’ugurisha, canke amafaranga y’ibikorwa.



Mu mirongo y’iduka, uzosangamwo ibice bihambaye vyinshi:



![Paramètres du magasin](assets/fr/15.webp)





- Amategeko rusangi**: Izina ry’iduka, amafaranga y’ishingiro (BTC, EUR, USD), igihe co guhera kw’iherezo rya Invoice (iminota 15), umubare w’ivyemezo vya Blockchain bisabwa
- Ibiciro**: Gutunganya inkomoko z'ibiciro vya Exchange n'uguhindura kwa fiat/Bitcoin
- Uko Usohora**: Guhindura ukuntu amapaji yawe yo gusohoka asa (ikimenyetso, amabara, ubutumwa bwihariye)
- Amagenamiterere ya imeyili**: Gutunganya amatangazo ya imeyili ku vyerekeye amahera yakiriwe
- Ibimenyetso vy'Ukwinjira**: API token uburongozi bw'ubudandaji bwo kuri interineti (WooCommerce, Shopify, n'ibindi)
- Abakoresha**: Gucungera uburenganzira bw'abakoresha bwo kwinjira mu bubiko n'ingero zitandukanye z'uburenganzira (Nyene, Umushitsi)
- Webhooks**: Itunganywa ry'urubuga kugira ngo rihuze mu gihe nyaco n'ubuhinga bwawe bwo guharura amafaranga canke ubuhinga bwa ERP



BTCPAY SERVER kandi itanga igice c’Ibikoresho kugira ngo yongere ibikorwa n’ubudandaji bwo kuri interineti, uburyo bwo kugurisha n’ibindi bikoresho.



![Gestion des plugins](assets/fr/16.webp)



## Inyungu n'imipaka y'ikoreshwa ry'aho hantu



**Ivyiza vya BTCPAY SERVER ku Mutaka** :




- Ubusegaba bwose: ubugenzuzi bwihariye bw'imfunguruzo n'amahera y'ibanga, nta wundi muntu ashobora guhagarika canke gucengera amahera yawe
- Ivyo kuzigama vyinshi: igiciro c’urubuga rwa Bitcoin gusa (amasenti makeyi ku Lightning) n’ibice 2-3% ku bikoresho vya kera
- Ibanga ryinshi: nta kwandikisha, kugenzura akaranga canke gusangira amakuru n'amashirahamwe y'abandi
- Ubwubatsi bufise inkomoko yuguruye buratanga icemezo c'uguseruka, ugusuzuma n'ubuzima buramba biciye mu muryango munini w'abahinguzi
- Gushiramwo biroroshe biciye ku Mutaka, ata buhinga buhanitse bukenewe



**Imipaka ihambaye** :




- Ihuriro ryo mu karere gusa**: BTCPAY SERVER kuri Umbrel ishobora gushikwako gusa ukoresheje urubuga rwawe rwo muhira. Ibereye ku gutanga amafaranga amaso mu yandi, ibikorwa vy’ukwikorera canke ubucuruzi buto buto, ariko ntibibereye ku maduka yo kuri internet ashobora gukoreshwa na bose kuri Internet.
- Inshingano yuzuye y'ubuhinga: gutunganya urudodo, gucungera ubudasiba, gukurikirana ubufatanye
- Uburongozi bw'amahera y'umuravyo: gufungura no gucunga imihora ifise ubushobozi buhagije bwo kwinjira
- Infashanyo igarukira ku nyandiko z'abanyagihugu n'amahuriro, bisaba kwigenga kuruta igisata c'ubudandaji gifasha abakiriya



Ukwo guhagarika LAN ni intambamyi nyamukuru yo gushiramwo BTCPAY SERVER mu iduka ry’ubudandaji ryo kuri interineti, aho abakiriya bakeneye kuba bashoboye gushika ku mapaji yo kwishura aho bari hose kuri Internet.



## Ibikorwa vyiza n'umutekano



Gukoresha ububiko bwa Umbrel bwikora no kubika kopi ku bimenyeshamakuru vyo hanze (inkoni ya USB, disiki ya Hard, igicu gipfutse). Bika imbuto zawe za Bitcoin (amajambo yo gukira) ahantu hatagira umutekano, hatandukanye n’abandi ku mubiri. Bika dosiye ya LND channel.backup kugira ngo umuravyo ushobore gusubirana.



Gukurikirana ubudasiba uguhuza kwa Bitcoin core, imirongo y’umuravyo n’inyishu ya BTCPAY SERVER. Igerageza ryoroshe ry’indwi ku yindi: generate no kwishura amafaranga y’amasatoshi makeyi. Gumana Umbrel ku gihe (ibice vy’umutekano, ivyiza). Kora backup imbere y’uko uhindura ibintu bikomeye. Kugira ngo ukoreshe mu buryo bw’umwuga, zirikana ugukurikirana hanze (UptimeRobot) n’imburi z’ubutumwa bwo kuri e-mail/SMS.



## Erekana BTCPAY SERVER ku mugaragaro ku iduka ryo kuri internet



Kugira ngo ushire BTCPAY SERVER mu bubiko bw’ubudandaji bushingiye ku rubuga (WooCommerce, Shopify, n’ibindi), abakiriya bawe barakeneye kuba bashoboye gushika ku mapaji y’ukwishura aho bari hose, atari gusa bavuye ku rubuga rwawe rwo mu karere.



**Umuti: Umuyobozi w'Igihugu ca Nginx**



Ushobora gushikiriza BTCPAY SERVER ku mugaragaro ukoresheje Umuyobozi w’Igihugu ca Nginx (uboneka mu Bubiko bw’Ibikoresho vya Umbrel). Uyu muti usaba :




- Izina ry'indangarubuga (ry'imbere canke ry'ubuntu biciye kuri DuckDNS, Nta-IP, Afraid.org)
- Gutunganya ivyuho vy'imbere (ivyuho 80 na 443) kuri router yawe
- Gushiramwo Nginx Proxy Manager, icungera ubwo nyene ivyemezo vya SSL



Ivyo bituma server yawe ibona Internet kandi bisaba ko wiyubara cane (amajambo y’ibanga akomeye, 2FA, guhindura ibintu bihoraho). Tuzoba turiko turategura inyigisho yihariye idondora neza iyo nzira yuzuye.



## Iciyumviro



BTCPAY SERVER kuri Umbrel ifatanya ububasha bw’uruzitiro rwa Bitcoin n’ukworohereza kwa Umbrel kugira ngo ireme ibikorwa remezo vy’ukwishura vy’umwuga vyishikira bose. Ubwo busegaba bw’ivy’amahera buzana n’inshingano yo kubibungabunga, ariko Umbrel yorosha cane umuzigo w’ibikorwa ugereranyije n’ivyiza: gukuraho amafaranga yo gukora, kurinda ubuzima bwite bwawe, kunanira gucengera no kugenzura vyose amafaranga yawe.



Ikoreshwa ry’urubuga rwo mu karere rirasanzwe rifise ibikorwa vyinshi: gutanga amafaranga y’ibikorwa vy’ukwikorera, kwishura amaso mu yandi, amaduka matomato y’umubiri, canke gusa kwiga no kugerageza Bitcoin na Lightning mu kibanza kigenzurwa. Ku bikenewe mu bucuruzi bwo kuri interineti bisaba gushirwa ahabona na bose, umuti wa Nginx Proxy Manager urahari, ariko usaba ibindi bikoresho vy’ubuhinga, ivyo tuzobidondora mu nyigisho yihariye.



Waba uriko urakora ubucuruzi, umugambi mushasha canke uriko uragerageza gusa, BTCPAY SERVER kuri Umbrel itanga ubwigenge bwuzuye mu vy’amahera. Inzira itangura n’iduka rya mbere, Invoice ya mbere, amahera ya mbere yakiriwe ataco akora mu bikorwa remezo vyawe vy’ubusegaba.



## Ubutunzi



### Inyandiko zemewe




- [Urubuga rwemewe rwa BTCPAY SERVER](btcpayserver.org)
- [Inyandiko zuzuye za BTCPAY SERVER](inyandiko.btcpayserver.org)
- [GitHub BTCPAY SERVER](imbuga ya github.com/umukozi wo kwishura/umukozi wo kwishura)
- [Inyandiko z'umurizo](https://umurizo.com/kb)


### Umuryango n'infashanyo




- [Ihuriro BTCPAY SERVER](urubuga rwo guhanahana amakuru)
- [Umutaka w'ihuriro](https://umuryango.getumutaka.com)
- [Igikoresho co kwishura kuri BTCP]