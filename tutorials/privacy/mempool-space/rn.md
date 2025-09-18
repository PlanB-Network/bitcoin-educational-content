---
name: Mempool
description: Gutohoza ibidukikije vyose vya Bitcoin.
---

![cover](assets/cover.webp)



Iryo tegeko rya Bitcoin ni urubuga rw’izina ry’uruyeri, rwigenga, rwuguruye kugira ngo umuntu agire inama. Abagize (nodes), ni ukuvuga mudasobwa zifise urugero rwa porogaramu ya Bitcoin, zifise uburenganzira bwo kuronka amakuru yose yasohowe kuri Bitcoin. Ariko mu myaka ya mbere ya Bitcoin, iyo porotokole ntiyari ishobora gushikira abantu benshi nk’uko iri muri iki gihe.


Mu misi ya mbere ya Bitcoin, vyari ngombwa gukoresha node ya Bitcoin kugira ngo umuntu ashobore kuronka ibikoresho bikwiye (bitcoin-cli) vyo kubaza urubuga akoresheje imirongo y’amabwirizwa.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Haciye rero hatanguzwa imigambi yo kwagura umuryango wa Bitcoin, bigatuma umuntu wese adafise node kandi/canke adafise ubuhinga bukenewe.



Muri iyi nyigisho, turaza kuraba umugambi wa **Mempool.space**, ibiwuranga n'ingaruka wagize ku bidukikije vya Bitcoin.



## Mempool.ikirere ni iki?



**Mempool.space** ni umugenzuzi w’inkomoko yuguruye atanga amakuru ngirakamaro ku bijanye n’ibikorwa, amafaranga y’ibikorwa, amabuye n’abacukuzi ku nzira zitandukanye z’amasezerano ya Bitcoin. Yatangujwe mu mwaka w’2020, izana iterambere rikomeye mu bumenyi bw’abakoresha biciye ku bishushanyo biserukira, ibishushanyo bigenda neza n’ibikoresho bitagiramwo ibintu vyinshi.



Kugira ngo umuntu atahure uwo mugambi, Mempool (memory pool) ni ikibanza c’ubuhinga bwa none aho amafaranga yose arindiriye kwemezwa ku rubuga rwa Bitcoin abikwa. Mempool ni nk'"icumba co kurindiriramwo" aho amafaranga y'i Bitcoin arindiriye kwemezwa. Buri mudasobwa iri ku rubuga (node) irafise icumba cayo co kurindiriramwo, ivyo bikaba bisigura igituma amafaranga yose akoreshwa ataboneka ku bantu bose igihe kimwe.



Ingaruka nyamukuru y’urubuga mu bidukikije vya Bitcoin ni uko rugufasha kuronka amakuru atandukanye mu bice vy’ukwibuka vy’ibihimba vyinshi biri kuri Bitcoin ataco ukeneye gukoresha. Mempool.space ni ububiko bwo kuraba no kurondera imihora y'amasezerano ya Bitcoin.



Ikoreshwa ryinshi mu bidukikije n’uko Mempool.space ari open source vyatumye ishobora gushirwa mu bikoresho vyinshi vy’ukwakira abantu. Ubu ushobora kugira urugero rwawe rwa Mempool.space ku nzira yawe bwite. Raba inyigisho yacu ku gutunganya Mempool.space ku nzira yawe ya Umbrel iri musi.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Ivy'ishimikiro vya Mempool.ikibanza



Nk'uko vyavuzwe haruguru, [Mempool.space](https://Mempool.space) ni umugenzuzi w'amasezerano ya Bitcoin ashobora kugufasha kugenzura ibikorwa vyawe n'ugukwiragira kwavyo ku rubuga rwa Bitcoin wahisemwo mu gihe nyaco, uhereye ku gishushanyo ca Interface.



Mempool.space ishigikira imirongo myinshi y’amasezerano ya Bitcoin.


Mu murongo w'ibikubiyemo, uzosanga imirongo ikurikira:




- Mainnet**: Urubuga nyamukuru rwa Bitcoin aho amafaranga nyayo ya Bitcoin aba.
- Signet**: Urubuga rwo kugerageza rukoresha imikono ya digitale kugira ngo rwemeze amabuye ataco bisaba ibikoresho bisabwa n’urubuga nyamukuru.
- Testnet 3**: Urubuga rwo kugerageza no gutegura rudafise ingorane ku masezerano ya Bitcoin.
- Testnet 4**: Verisiyo nshasha ya Testnet 3 izana ugushikama gukomeye n’amategeko mashasha y’uguhuriza ku bidukikije vy’igerageza.



![reseaux](assets/fr/01.webp)



Ku rupapuro rw’intango, ibubamfu muri Green, uzobona amabarabara ashoboka yo muri kazoza (imigwi y’ibikorwa) yiteguriye kwemezwa no gushirwa (gucukurwa) mu rubuga rwa Bitcoin. Mu mpande zose, buri minota cumi hacukurwa ibuye: ubike ayo makuru, kuko azodufasha mu nyuma mu gutera imbere kwacu.


Mu rangi y’umutuku, ku ruhande rw’iburyo, uzosanga amabuye aherutse gucukurwa kuri Bitcoin, umubare w’amabuye ya nyuma yacukuwe ugereranya uburebure bw’uruzitiro buriho ubu.



![blocs](assets/fr/02.webp)



Igice ca **Amafaranga y'Ibikorwa** ni igiharuro c'amafaranga y'ibikorwa. Uko amafaranga agenewe igikorwa cawe aba menshi, ni ko bishoboka cane ko igikorwa cawe cokwongerwa ku gice gikurikira giteguye gucukurwa.


Amafaranga y'ugucuruza agereranya igiciro Miner izogutwara kugira ngo winjize ugucuruza kwawe mu gice c'abashaka gutora Mining. Bisobanurwa n’igipimo ca sat/vB (Satoshi/Virtual Bytes) kigereranya umubare w’ama satoshis uriha ku kibanza igikorwa cawe kizofata mu gice c’abashaka gutora.



⚠️ IGIHARURWA: Iyo habayeho ukuzura kwa Mempool, abacukuzi bashira imbere ibikorwa bitanga igipimo ciza ca Satoshi/vByte. Uko igikorwa cawe kiremera (kinini), niko kizokenera gushirwamwo satoshis nyinshi ningoga.



![fees-visualizer](assets/fr/03.webp)



Igice ca **Mempool Goggles** kigufasha kwiyumvira ikibanza gifatwa n’ugucuruza.



![mempool](assets/fr/04.webp)



Ibarabara ricukurwa hafi buri minota cumi kubera ubugoyagoye bwa Proof of Work abacukuzi bategerezwa gutanga kugira ngo bongereko ibarabara ryabo ry’abashaka gucukura ku ruhererekane rw’amabarabara bacukurwa. Ico kibazo kirahinduka buri **2016 blocks**, kingana n’indwi nka **2**. Ushobora kubona ingene iyo ngorane itera imbere hano.



![difficulty](assets/fr/05.webp)



Kwongerwako igice gishasha ku ruhererekane nyamukuru bituma Miner y’igice cemejwe ironka impembo igizwe n’igice kidahinduka (kigabanywamwo igice buri mabuye 210.000**, bingana n’imyaka nka 4** mu gihe c’uguca ibice) n’amahera y’ugucuruza.



![halving](assets/fr/06.webp)



## Ushike ku makuru y'ubucuruzi bwawe



Mu murongo w’ugushaka Mempool.space, ushobora kwinjiza Bitcoin Address yawe canke transaction ID yawe kugira ngo umenye vyinshi ku bijanye n’amateka yawe.



![search](assets/fr/07.webp)



Kuri paji y'ibisobanuro vy'ibikorwa, uzosanga amakuru rusangi yerekeye ibikorwa vyawe:




- Status**: Yemejwe iyo yongewe ku gice, ntiyemejwe iyo urindiriye muri Mempool.
- Amafaranga y’ugucuruza**.
- Igihe kigereranywa co gushika (ETA)**: Igihe kigereranywa kizotwara kugira ngo amafaranga yawe yongererwe ku gice. Iharurwa hakurikijwe igipimo gifise amahera ajanye n’ivyo bikorwa.



![general-txinfo](assets/fr/08.webp)



Igice ca **Flow** kirerekana igicapo c'ibice vy'ibikorwa vyawe.



Ivyinjizwa (imbere ya UTXO), bikoreshwa mu gucuruza kwawe, n’ibisohoka biha ababironka uburenganzira bwo gukoresha ama bitcoins ava ku gisohoka cose mu kwerekana umukono usabwa ku bijanye n’amahera bakoresha.



![flow](assets/fr/09.webp)



Ibindi bisobanuro ku ma aderesi akoreshwa biraboneka mu gice ca **Inputs & Outputs**.



![address](assets/fr/10.webp)



Tora imigambi itandukanye y’ugucuruza Bitcoin kugira ngo wongere ibanga ryawe.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ihutishe amafaranga yawe



Mu bidukikije vya Bitcoin, umuce wo kwemeza ibikorwa vy’ubudandaji n’abacukuzi ufitaniye isano n’amahera y’ibikorwa ajanye n’iryo bikorwa. Abacukuzi bashira imbere ibikorwa vy’ubudandaji bifise igipimo kinini c’amahera (satoshis/vBytes), ivyo bishobora gutuma ibikorwa vyawe bigira akamaro iyo utarishe amahera akwiriye yemerwa n’abacukuzi. Ivyo ukora vyofata muri Mempool urindiriye block yemera igipimo c’amahera yayo.



Ikintu ciza, hari uburyo bubiri buboneka ku rubuga rwa Bitcoin kugira ngo wihutishe kwemeza amafaranga yawe.





- RBF** - Replacement By Fee: Uburyo bugufasha gukoresha amafaranga nk’ayo ukoresha mu gukoresha amafaranga make, ariko ubu mu kwongera amafaranga y’amafaranga kugira ngo wihutishe kwemeza. Ivyo ukoresha bishasha bizokwerekanwa ningoga kandi bishirwe mu gice, bihindure ivy’amahera make.



Ushobora gukora igikorwa co gusubirira amafaranga n’amasakoshi yemera ubu buryo. Nk’akarorero, raba ikiganiro cacu kivuga ibijanye n’ubururu Wallet Wallet.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- CPFP** - Child pay for parent: Uburyo bwahumekewe na RBF, ariko ku ruhande rw’uwukira. Iyo igikorwa uriko urakira kibujijwe muri Mempool, urafise uburenganzira bwo gukoresha amafaranga (UTXOs) y’ico gikorwa, naho nyene kitari bwaremejwe, mu gutanga amahera menshi kuri ico gikorwa gishasha kugira ngo amafaranga y’agaciro - y’igikorwa reci -ura muri wewe abacukuzi kugira ngo bashire ivyo bicuruzwa vyose mu gice.



⚠️ Igiciro ca mbere kigomba gushirwa mu gice kugira ngo igiciro ca kabiri gishobore kwemezwa.



Nimba ayo majambo yose asa n’ay’ubuhinga cane, ndagusavye [murabe urutonde rw’amajambo rwacu](https://planb.network/resources/glossary), rurimwo insobanuro z’amajambo yose y’ubuhinga ajanye na Bitcoin n’ibidukikije vyayo.



Uretse ubu buryo, Mempool.space, kubera ubucuti ifise n’abacukuzi barenga 80% bari ku rubuga rwa Bitcoin, iragufasha kandi kwihutisha ibikorwa vyawe vyose **bitaremejwe**, mbere n’ivyo bidakoresha RBF, mu kwishura amahera abacukuzi bari muri GW-xt- yawe. block yiteguye gucukurwa.



Ku rupapuro rw’ibisobanuro vy’ibikorwa, fyonda ku buto **Accelerate**, hanyuma ubandanye kwishura umugenzi wawe abacukuzi.



![accelerate-section](assets/fr/11.webp)


## Abana bato



Miner yerekeza ku muntu arongoye imine, ni ukuvuga mudasobwa ikora mu nzira ya Mining, igizwe no kugira uruhara muri Proof-of-Work. Miner ihuriza hamwe amafaranga ategerejwe muri Mempool yiwe kugira ngo akore umugwi w’abashaka gutora. Ica irondera Hash ibereye, iri munsi canke ingana n’ico ishaka, ku mutwe w’iyi block mu guhindura nonces zitandukanye. Iyo aronse Hash ibereye, atangaza ivyuma vyiwe ku rubuga rwa Bitcoin maze akabishira mu mufuko impembo y’amahera ijana, igizwe n’infashanyo y’ivyuma (uguhingura ama bitcoins mashasha ex-nihilo), n’amahera y’ugucuruza.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Abacukuzi ni nk'aba "validators" bagenzura bagashira hamwe amafaranga mu bice. Kugira ngo bongereko igice gishasha ku rubuga rwa Bitcoin, bategerezwa gutorera umuti uruzitiro rutoroshe rw’imibare (Proof-of-Work). Miner wa mbere azotorera umuti uruzitiro aronka impembo ya Bitcoin (block grant + amafaranga y’ibikorwa biri muri block).



Ingorane y’iyi Proof of Work irakurikiranirwa hafi, bikagufasha kwiyumvira ingene ububasha bwo gukoresha ubuhinga bwa none busabwa abacukuzi b’amabuye y’agaciro bugenda buratera imbere. Uzosanga mu bice bikurikira :





- Igereranyo ry’impera zose zaronswe n’abacukuzi mu gihe c’uguhindura ingorane za nyuma, hamwe n’igereranyo ry’i Halving ikurikira y’infashanyo y’amabuye, ibaho buri mabuye 210.000 (nk’imyaka 04).



![rewards](assets/fr/12.webp)



Ico kibazo kirahindurwa buri mabarabara y’umwaka w’2016 (nk’indwi zibiri). Ni ibihuye n’igihe abacukuzi bafata kugira ngo bashike kuri Miner buri mabarabara yo mu 2016.


Iyo igihe abacukuzi bafata kiri munsi y’iminota 10, ingorane irarushirizaho, ivyo bikaba vyerekana ko vyari vyoroshe ku bacukuzi kwemeza amabuye ya Miner. Ku rundi ruhande, iyo igihe gisanzwe umuntu afata kirenze iminota 10, ingorane iragabanuka.



![mining-pool](assets/fr/13.webp)





- Imigwi y’abacukuzi: Kubera ingorane ziri muri ivyo, umugwi w’abacukuzi barakorana kugira ngo bafashe mu kurondera Proof of Work kuri Bitcoin, mu co twita **pool**. Iyo ivyuma bicukuwe n’umugwi, impembo ironswa igabanywa hakurikijwe ijana ry’uguterimbere mu kurondera umuti w’igice ca Miner imwe imwe, ni ukuvuga umusanzu mu bushobozi bwo guharura mu kurondera Proof-of-Work, canke hakurikijwe uburyo bwo guhembwa bwemejwe n’ubufatanye.





![mining](assets/fr/14.webp)



## Ibikorwa remezo vya Lightning Network



Mempool ntitanga amakuru gusa ku bikorwa remezo vy’uruja n’uruza rwa Bitcoin (uruzitiro rukuru). Ishiramwo kandi ibikoresho vyo kubona no gutohoza ivy’ugushiramwo umuravyo wa Bitcoin.



Mu gice ca **Umuravyo**, ushobora kubona amahuzu yose ariho hagati y'ibihimba vy'Umuravyo.



![network-stats](assets/fr/15.webp)



Iyi Interface itanga amakuru ku :





- Imibare ya Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **IGIHARURWA**: Ubushobozi bw’umurongo wo kwishura bugaragaza amafaranga menshi cane node ishobora kohereza ku yindi node mu gihe c’ugucuruza kwa Lightning.





- Ivyuma vy’umuravyo bitangwa bivanye n’uwutanga ubuhinga bwa Internet (hosting service) kandi bivanye n’ubushobozi bw’umuhora wo kwishura.



![distribution](assets/fr/17.webp)





- Amateka y’ubushobozi bwose bwa Lightning Network.


Uzosanga kandi urutonde rw’izo node hakurikijwe ubushobozi bw’imihora yazo yo kwishura.



![ranking](assets/fr/18.webp)



## Ibindi bishushanyo



Mempool.space ni urubuga rwiza rwo kunezerererwa gukorana n’imirongo y’amasezerano ya Bitcoin. Ivyo bishushanyo ntibitanga amakuru abonetse gusa kugira ngo bigufashe gufata ingingo y’igihe co gukora amafaranga, ariko kandi biratanga n’ibipimo vy’ukuri bigufasha kubona, mu gihe nyaco, inkomezi n’ubuzima bw’urubuga rwa Bitcoin n’ibikorwa remezo vy’umuravyo bifitaniye isano.



Mu gice ca **Ibishushanyo**, ushobora kubona amakuru y'ingenzi yerekeye urubuga rwa Bitcoin:




- Uguhinduka kw’ubunini bwa Mempool: Ushobora kwihweza ingene ubunini bwa Mempool buhinduka, ivyo bikaba bishobora kwerekana ibihe vy’ibikorwa vyinshi canke bike ku rubuga.



![graphs](assets/fr/19.webp)






- Iterambere ry’ibikorwa n’amahera y’ibikorwa ku rubuga rwatowe: Mu gukurikirana uguhinduka kw’ibikorwa ku segonda, urashobora kwitega ibihe vy’ugucumbagira canke ibikorwa bike, maze ugatuma amahera yawe y’ibikorwa agenda neza. Iyi graphe iraguha iciyumviro ku bushobozi bw’urubuga bwo gukorana n’ingero y’ibikorwa.



![graphs](assets/fr/20.webp)



Ubu ko washitse ku mpera y’urugendo rwawe kuri Mempool.space, ube umugenzuzi wawe bwite kandi ukurikirane amafaranga yawe mu gihe nyaco. Turagusavye uronke aha hepfo ingingo yacu ku bijanye n'umugenzuzi wa Bitcoin **Ikidengeri ca bose**.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1