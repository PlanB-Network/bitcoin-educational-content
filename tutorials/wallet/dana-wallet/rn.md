---
name: Dana Wallet
description: Igitabo c'ibintu bikeyi vy'ukwishyura mu gacerere (BIP-352)
---

![cover](assets/cover.webp)



Gusubira gukoresha amaderesi ya Bitcoin ni kimwe mu bintu bitera ubwoba cane ibanga ry’abakoresha. Iyo uwuronka asangira aderesi imwe kugira ngo aronke amahera menshi, uwubibona wese arashobora gukurikirana amafaranga yose ajanye n’ivyo maze agasubira kwubaka amateka yabo y’ivy’ubutunzi. Ico kibazo kiratera cane cane abahingura ibintu, amashirahamwe y’ubugiraneza canke abaharanira uburenganzira bw’abantu bipfuza kwerekana ku mugaragaro aderesi y’intererano ataco bahungabanya ku buzima bwite bwabo canke ubw’abaterankunga babo.



Dana Wallet yishura kuri iyo ngorane n’umuti mwiza: Ukwishura mu gacerere. Iyi minimalist, open-source wallet, yatangujwe mu 2024, itanga aderesi idahinduka ishobora gusubirwamwo mu gihe yemeza ko amahera yose yaronse ahera ku aderesi itandukanye kuri blockchain. Uwurungitse ntakeneye gukorana n’uwuyakiriye imbere y’igihe, kandi nta muntu wo hanze ashobora guhuza amafaranga y’umuntu ku giti ciwe. Ku blockchain, ivyo vyishyurwa bisa n’ibikorwa bisanzwe vya Taproot.



Dana Wallet iraboneka kuri Mainnet na Signet, ariko abayikoze baracabona ko ari igerageza kandi baragusaba kudashiramwo amahera utari witeguriye gutakaza. Muri iyi nyigisho, tuzokoresha verisiyo ya Signet kugira ngo tubone Silent Payments ataco dushize mu kaga k’amahera nyayo.



## Dana Wallet ni iki?



### Filozofiya n'intumbero



Dana Wallet ikoresha uburyo bwa "SP-first": wallet itanga amaderesi y'Ivyishyurwa vy'Icereje gusa, kandi yemera gusa ubwo bwoko bw'ukwishyura. Ntuzoshobora gukora aderesi ya kera ya Bitcoin (iragi, SegWit canke Taproot) ukoresheje iyi porogaramu. Ukwo kubuzanya n’ibigirankana kuratuma wibanda cane ku kwiga umurongo wa BIP-352 utasamajwe n’ibindi bintu. Igikoresho kitagiramwo ibintu vyinshi gifasha n’ibigirankana gukoresha neza kuruta uburyo bwinshi bwo guhitamwo, bigatuma ico gikoresho gishobora gushikira mbere n’abakoresha bashasha mu vyiyumviro vy’ibanga rya on-chain.



Umugambi wose ni uw’inkomoko yuguruye, wateguwe na Flutter ku bijanye n’ivyo gukoresha telefone ngendanwa na Rust ku bijanye n’ubuhinga bwo gukoresha amakuru y’imbere. Iyi nyubakwa ihuza ubumenyi bw’abakoresha n’ubushobozi bwiza cane ku bikorwa vy’ugupima bikomeye.



### None Ivyishyurwa vy’Icereje bikora gute?



Ivyishyurwa vy’agacerere (BIP-352) bishingiye ku buryo buteye imbere bwo gukingira amakuru hakoreshejwe urufunguzo rwa Diffie-Hellman Exchange (ECDH). Uwuronka aderesi idahinduka (itangura na `sp1...` kuri mainnet canke `tsp1...` kuri Signet) igizwe n'imfunguruzo zibiri zitandukanye za bose: urufunguzo rwo gupima ($B_{scan}$) kugira ngo umenye amahera yinjira, n'urufunguzo rwo gukoresha ($B_{spend receiver}d) kugira ngo ukoreshe fu. Ukwo gutandukanya gutuma bishoboka kuguma urufunguzo rwo gukoresha ku bikoresho vya wallet mu gihe ukoresha urufunguzo rwo gupima ku gikoresho gihuye.



Iyo uwurungitse yipfuza kwishura, wallet yiwe ifatanya umubare w’imfunguruzo z’ibanga z’ivyo yinjije n’urufunguzo rwa bose rw’uwuronka kugira ngo abare ibanga rya ECDH rusangi. Iryo banga rituma habaho "tweak" y'ibanga, iyo yongewe ku rufunguzo rw'amahera y'uwuronka, igatuma habaho aderesi yihariye ya Taproot y'ico gicuruzwa.



Uwuronka arashobora gusubiramwo iyo mibare akoresheje urufunguzo rwiwe rw’ibanga rwo gupima n’urufunguzo rwa bose ruboneka mu gucuruza (umutungo w’imibare wa Diffie-Hellman). Ivyo bimufasha kumenya ayo mahera no kuyakoresha ata n’umwe abanje gukorana n’uwayarungitse.



Ubwo buryo buratanga ivyiza vyinshi:




- Ibanga ry'uwuronka**: ukwishyura kwose guhera kuri aderesi itandukanye
- Ibanga ry'uwohereje**: nta kimenyetso gihoraho gihuza amahera
- Nta serveri y'uwundi muntu**: porotokole ikora yigenga
- Ibikorwa bitandukanye**: Ukwishura mu gacerere bisa n'ibikorwa bisanzwe vya Taproot



Intambamyi nyamukuru ni igiciro co gucapura: uwuronka ategerezwa gusuzuma igikorwa cose gishasha ca Taproot kugira ngo amenye ivyo yagenewe.



Niba wifuza kumenya vyinshi ku bijanye n’ubuhinga bwo kwishura mu gacerere, turagusavye kwiga inyigisho ya BTC204 yerekeye ibanga muri Bitcoin, irimwo igice kijanye n’ukwishyura mu gacerere:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Imbuga zishigikiwe



Dana Wallet iraboneka nk’iporogarama ya Android. APK ishobora gukurwa biciye ku bubiko bwa F-Droid bwihariye bwatanzwe n’abayiteguye, biciye ku Obtainium, canke biciye ku GitHub. Ku bakoresha Linux, birashoboka mu buryo bw’ubuhinga gukoranya porogarama ya Flutter ku biro.



Iyi porogaramu ntiboneka kuri iOS canke biciye mu maduka yemewe (Google Play, App Store), ivyo bikaba vyerekana ko iri mu rwego rw’igerageza kandi ko yibanda ku bantu b’abahinga.



## Gushiramwo



### Ibisabwa vy'ingenzi



Kugira ngo ushire Dana Wallet kuri Android, uzokenera igikoresho ca Android gifise uburyo bwo gukoresha "Isoko zitazwi" mu mirongo y'umutekano. Nta konti canke kwiyandikisha bisabwa.



### Yongerako F-Cold



Uburyo bushimikijwe ni ubwo kwongerako ububiko bwa F-Droid bwa Dana Wallet. Genda kuri `fdroid.silentpayments.dev` aho uzosanga uruja n’uruza rw’ububiko n’ikode ya QR yo gucapura. Ubu ububiko buratanga ibikorwa 3: verisiyo ya Mainnet, Iterambere na Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Gushiramwo biciye kuri F-Droid



Ugurure porogarama ya F-Droid ku gikoresho cawe ca Android, hanyuma ugende kuri Settings biciye ku kimenyetso kiri musi iburyo. Hitamwo "Ibibiko" kugira ngo ucunge inkomoko za porogaramu. Kanda kuri buto ya "+" kugira ngo wongereko ububiko bushasha, hanyuma ushireko kode ya QR canke ushireko `https://fdroid.silentpayments.dev/fdroid/repo`. Ububiko bumaze kwongerwako, uzobona amaverisiyo atatu ya Dana Wallet ariho. Hitamwo "Dana Wallet - Ikimenyetso" hanyuma ukande "Shiraho".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Imiterere y'intango



### Guhingura ububiko



Igihe Dana Wallet itanguzwa ubwa mbere, yerekana igicapo c'akabazo kigaragaza ubutumwa bwayo: "Kohereza no kwakira intererano ata bantu bayihuza". Kanda "Tangura" kugira ngo ukomeze. Igishushanyo gikurikira kirerekana ivyiza bitatu nyamukuru vy’iyi porogarama:




- Intererano zitagira utwigoro**: tangura kwakira intererano mu masegonda makeyi
- Ubuzima bwite ku buryo busanzwe**: nta nkenerwa y'abakozi canke ibikorwa remezo bikomeye
- Ubumenyi bumeze nk'ubwa imeyili**: wohereze kandi wakire bitcoins nk'imeyili



Ushobora guhitamwo hagati ya "Gusubizaho" kugira ngo usubiremwo igitabu cariho canke "Rema wallet nshasha" kugira ngo ureme ikindi gishasha. Kanda "Rema wallet nshasha".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Ico gikoresho gica kizana ijambo ry’ugusubirana, iryo ukwiye kwandika witonze ku gikoresho c’umubiri. Mbere no ku mahera y’ikigeragezo ata co amaze nyakuri, nushireho ingeso nziza zo gusubiza inyuma.



### Interface n'ibipimo



Igihe igitabo kimaze kuremwa, uja ku rubuga nyamukuru, ugabanywemwo ibice bibiri: "Ibikorwa" na "Ivyagezwe".



Igipande ca **Transact** kigaragaza amahera yawe ya bitcoin (n'uguhindura kwayo mu madolari), urutonde rw'amahera uherutse gukoresha, n'ubuto bubiri bw'ibikorwa: "Pay" kugira ngo wohereze amahera, n'ubuto bwo kwakira (ikimenyetso co gukuraho).



**Ivyagezwe** bitanga amahitamwo ane:




- Erekana ijambo seed**: yerekana ijambo ryawe ryo gusubirana kugira ngo ubike
- Guhindura ifaranga rya fiat**: guhindura ifaranga ry'iyerekanwa (USD ku buryo busanzwe)
- Gushinga url y'inyuma**: gutunganya URL ya server ya Blindbit (raba igice gikurikira)
- Guhanagura wallet**: guhanagura wallet yose ku gikoresho



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Serveri y'impumyi



Dana Wallet ikoresha umukozi w’urutonde yitwa **Blindbit** kugira ngo imenye amahera yawe y’uguceceka. Gutahura ingene bikora ni ikintu gihambaye mu gusuzuma uburyo bwo kwizigira bw’ikoreshwa.



**Kubera iki dukeneye umukozi?



Kugira ngo umenye ko hariho Ukwishura mu gacerere, wallet yawe itegerezwa gucapura amafaranga yose ya Taproot muri buri bubiko maze igakora ibara ry’ubuhinga (ECDH) kuri buri bubiko. Ku telefone ngendanwa, iyo nzira yoba ari iyo gukoresha cane ubuhinga bwa none kandi ikaba ikoresha ubuhinga bwinshi cane.



Server ya Blindbit itorera umuti ico kibazo mu kubara imbere y'igihe amakuru yo hagati (yitwa "tweaks") ku bikorwa vyose vya Taproot. wallet yawe ica ikuraho izo tweaks (33 bytes ku giciro) maze igakora igiharuro ca nyuma **mu karere** kugira ngo isuzume nimba amahera ari ayawe.



**Ibanga ryazigamye**



Udakunze server isanzwe ya Electrum aho uhishura amaderesi yawe, server ya Blindbit ntimenya ivyo wishura ari ivyawe. Itanga amakuru amwe ku bakoresha bose, kandi ni telefone yawe ikora igenzura rya nyuma. Ibanga ryawe rero rirazigama ku bijanye n’umukozi.



**Serveri mburabuzi



Dana Wallet ikoresha umukozi wa bose `ibice vy'amahera.dev/ibice vy'impumyi/ikidodo` (ku Signet) canke `ibice vy'amahera.dev/ibice vy'impumyi/mainnet` (ku Mainnet). Ushobora guhindura iyi URL mu mitunganyirize iyo wakira umukozi wawe bwite.



**Wakira server yawe bwite ya Blindbit**



Ku bakoresha bipfuza ubusegaba bwose, birashoboka kwakira umukozi wabo bwite wa Blindbit Oracle. Ivyo bisaba :




- Igikoresho c'ishimikiro ca Bitcoin **kitari inkukuma** (kitari pruned)
- Gushiramwo Impumyi Oracle (iboneka kuri GitHub: `setavenger/Impumyi-Impumyi`)
- Hafi. 10 GB y'umwanya w'inyongera kuri disiki
- Ubuhinga bw'ubuhinga (Genda gukoranya, gutunganya server)



Nta porogaramu ipfutse iraboneka kuri Umbrel canke Start9. Gushiramwo biguma ari ivy’amaboko kugeza ubu. Ivyo ni ivy’ubwihindurize bukora, kandi inyishu zishobora gushikwako zishobora kuza muri kazoza.



## Gukoresha buri musi



### Kwakira amafranga



Kugira ngo uronke ama bitcoins, kanda buto yo kwakira (ikimenyetso co gukuraho) iri ku rubuga nyamukuru. Dana Wallet rero yerekana aderesi yawe yuzuye y’Ukwishura mu gacerere mu buryo bwa `tsp1q...` ku Kimenyetso. Ikigaragara kiratanga amahitamwo menshi:




- Erekana kode ya QR**: yerekana kode ya QR y'aderesi yawe kugira ngo uyikoreshe mu buryo bworoshe
- Share**: sangira aderesi biciye ku maporogarama ya telefone yawe
- Kopa**: kopa aderesi ku rutonde



Nk’uko vyerekanwa ku rubuga, urashobora gusangira iyo aderesi ku mugaragaro ku mbuga zawe zo gusangirirako amakuru ataco uhinduye ku buzima bwite bwawe.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Kugira uronke amafaranga yawe ya mbere yo gupima kuri Signet, koresha uruzitiro rwihariye rwo kwishura mu gacerere ruboneka kuri `silentpayments.dev/faucet/signet`. Kopa aderesi yawe `tsp1...`, uyishire mu kibanza catanzwe ku ruzitiro, hanyuma wemeze ivyo wasavye. Rindira ko ivyuma bicukurwa (nk’iminota 10 kuri Signet).



### Wohereze amahera



Kugira ngo wohereze amahera, kanda kuri buto ya "Pay" iri ku rubuga nyamukuru. "Hitamwo uwuzokwakira" igaragara n'amahitamwo atatu yo gusobanura uwuzokwakira:




- Injira amakuru y'ukwishyura n'amaboko
- Gushiramwo kuva ku rubaho**: kwanika aderesi kuva ku rubaho
- Gucapura kode ya QR**: gucapura kode ya QR irimwo aderesi



Iyo aderesi y'uwuzokwakira imaze kwemezwa, igicapo "Enter amount" kiragufasha kwinjiza amahera uzorungika mu satoshis. Igiciro cawe kiriho kiragaragazwa kugira ngo ukoreshe. Kanda "Bandanya guhitamwo amafaranga" kugira ngo ukomeze.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Igishushanyo gikurikira kirerekana ingero zitatu z’ibirego, bivanye n’ukwihutirwa bisabwa:




- Kwihuta** (iminota 10-30): amafaranga menshi yo kwemeza vyihuse
- Ibisanzwe** (iminota 30-60): ibiciro biringaniye
- Buhoro** (1+ isaha): amafaranga makeyi ku bikorwa bitahutirwa



Amaze guhitamwo urugero rw'amahera, "Witeguye kohereza?" confirmation screen ivuga mu ncamake amakuru yose: aderesi y’aho umuntu aja, amahera, igihe kigereranywa n’amahera yo gukoresha. Suzuma neza aya makuru, hanyuma ukande "Ohereza" kugira ngo wohereze amafaranga.



Iyo umaze kohereza, iyo nzira igaragara muri kahise kawe ifise ikibanza "Ntiyemejwe" gushika ishizwe mu gice. Igiciro cawe kirahindurwa bivanye n’ivyo.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Inyungu n'aho bigarukira



### Ibintu bihambaye





- Pedagogical**: interface yoroshe yibanze ku kwiga kwishura mu gacerere
- Bidirectional**: ifasha kohereza no kwakira, bitandukanye n'ibindi bitabo
- Inkomoko yuguruye**: kode ishobora gusuzumwa kuri GitHub
- Faucet** yihariye: ituma vyoroha kuronka amahera yo gupima
- Ata konti**: nta kwiyandikisha canke amakuru y'ibanga bisabwa



### Intambamyi zo kwiyumvira





- Igerageza**: porogaramu itagenzuwe, ukoreshe witonze kuri Mainnet
- Urubuga rutoyi**: ahanini Android, nta verisiyo ya iOS
- Ibikorwa bigabanutse**: nta kugenzura ibiceri, nta makonti make, nta Muravyo
- Gupima cane**: kumenya ukwishyura bifata ubutunzi bwinshi



## Ibikorwa vyiza



### seed umutekano



Mbere no ku bipimo vya Signet bifise amateka ata co amaze, fata neza ijambo ryawe ryo gukira. Koresha uburyo bwo "Kwerekana ijambo seed" mu mirongo kugira ngo uyandike neza. Nk’akamenyero keza, mugumye mufise amasakoshi atandukanye rwose ya Signet na Mainnet: ntimwigere mukoresha seed yaremewe kugerageza kuri wallet igenewe kwakira amahera nyayo.



### Imburi ku bijanye n'igerageza



Dana Wallet iracari ifatwa nk’igerageza n’abayikoze. Nk'uko babivuga neza: "Ntukoreshe amahera udashaka gutakaza". Kugira ngo wige, hitamwo verisiyo ya Signet. Niba ukoresha verisiyo ya Mainnet, n’ukoreshe amahera ya token.



### Gusubiza inyuma no gusubizaho



Gusubiza amafaranga y’Ivyishyurwa vy’Icereje bisaba wallet ihuye n’umurongo wa BIP-352. wallet isanzwe ntishobora gucapura blockchain kugira ngo ibone UTXO yawe y’Ivyishyurwa Bicereje. Gumana Dana Wallet ishizweho canke ukoreshe "Gusubiza" uburyo bwo gutangura kugira ngo ugarure wallet iriho.



## Igereranyo n’Igitabu-63-47 n’igitabu-62



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Ivyishyurwa vy’agacerere birakuraho igikorwa co kumenyesha BIP-47 ku giciro c’ugupima bizimvye cane. PayJoin itorera umuti ingorane itandukanye (uguhuza kw’injiza) kandi ishobora gufatanywa n’Ivyishyurwa vy’Icereje.



## Iciyumviro



Dana Wallet ni igikoresho c’agaciro co kwigisha co kwiga ivyerekeye Ukwishura mu gacerere mu kibanza kitagira ingorane. Uburyo bwayo bwo gukoresha ibintu bike cane buratuma utahura uburyo nyamukuru bw’itegeko rya BIP-352 utasamajwe n’ibintu bitari vyo. Mu kugerageza Signet, uzotsimbataza ugutahura ngirakamaro kw’iyi tekinoloji itanga umuhango ku bijanye n’ibanga ry’ibikorwa vya Bitcoin.



Silent Payments zigereranya intambwe ikomeye mu guhuza ukworohereza gukoresha n’ukwubaha ubuzima bwite. Ishavu ry’abanyagihugu n’ugushiramwo kwa mbere mu bipapuro bitandukanye (Cake Wallet, BitBox02, BlueWallet yo kohereza) vyerekana kazoza aho gutangaza aderesi y’intererano bitazosubira guhungabanya ubuzima bwite bw’amahera bwa nyen’iyo mpapuro.



## Ubutunzi



### Inyandiko zemewe




- Dana Wallet Ububiko bwa GitHub:
- F-Cold ibiziga:
- Urubuga rw'abanyamuryango b'Ivyishyurwa vy'Iceceka: https://ivyishyurwa vy'Iceceka.xyz
- Ibisobanuro BIP-352:



### Ibikoresho vyo kugerageza ikidodo




- Faucet Ukwishura mu gacerere: https://ukwishyura mu gacerere.dev/uruzitiro/ikidodo
- Ikimenyetso Mempool Umugenzuzi: https://mempool.ikibanza/ikidodo



### Serveri y'impumyi (yikira)




- Igitabu c'impumyi (GitHub):