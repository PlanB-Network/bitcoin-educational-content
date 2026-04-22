---
name: Porogaramu Bitcoin.
goal: Ubake ububiko bw'ibitabu bwose bwa Bitcoin kuva mu ntango maze utahure imishinge y'ubuhinga bwa Bitcoin
objectives: 

 - Gushira mu ngiro imibare y'umurima n'imigenderanire y'umugongo muri Python
 - Kubaka no gusesangura ibikorwa vya Bitcoin mu buryo bwa porogaramu
 - Rema aderesi za testnet no gutangaza amafaranga kuri interineti
 - Kumenya neza imishinge y'imibare ishingiye ku citegererezo c'umutekano wa Bitcoin

---
# Urugendo rwo mu nyandiko n'amaporogarama ya Bitcoin


Iryo shure rikomeye ry’imisi ibiri, ryigishwa na Jimmy Song, rigutwara mu mishinge y’ubuhinga bwa Bitcoin mu kwubaka ububiko bw’ibitabu bwose bwa Bitcoin kuva mu ntango. Gutangura n'imibare y'ingenzi y'ibibanza bifise impera n'imirongo y'imirongo, uzotera imbere biciye mu gusesangura ibikorwa, gushitsa inyandiko, no guhanahana amakuru ku rubuga. Biciye mu myimenyerezo yo gukora amakode mu makaye ya Jupyter, uzokwikorera aderesi yawe y’urubuga rwo kugerageza, wubake amafaranga n’amaboko, maze uyamenyeshe ku rubuga—ivyo vyose mu gihe uzoba uriko uraronka ugutahura gukomeye kw’ingingo ngenderwako z’ubuhinga bwo gukora amakode zituma Bitcoin itekanye kandi idashobora kwizigirwa.


Nimwinovore urugendo!

Iciyumviro: Amavidewo y'iri somo aboneka mu congereza gusa.

+++

# Imenyekanisha


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Incamake y'amashure


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Murakaze mu nyigisho PRO 202 _**Gutegura porogarama ya Bitcoin**_, urugendo rukomeye rugutwara kuva ku mibare y’ibarabara gushika ku kwubaka no gutangaza amakuru nyayo kuri Bitcoin’s Testnet.


Muri iri shure, uzogenda wubaka ububiko bw’ibitabu bwa Bitcoin muri Python mu gihe uronka ubuhinga bwo gukingira amakuru, ubuhinga bwo gukora amakuru, n’ubuhinga bwo gukora amakuru bikenewe kugira ngo wiyumvire neza ibijanye n’umutekano wa Bitcoin be n’ingene ikora. Uburyo bwa PRO 202 burakora neza cane: iciyumviro cose gica gishirwa mu ngiro mu makaye ya Jupyter, kugira ngo inyigisho n’itegeko bikomeze.


### Ivyiyumviro vy’ingenzi vy’imibare vya Bitcoin.


Iki gice ca mbere gishinga intahe y’imibare idakenewe cane. Uzoshira mu ngiro ibikorwa vy’imibare y’umurima n’ivy’imirongo y’imirongo (itegeko ry’umugwi, kwongerako, gukubita kabiri, ugukubita kw’imirongo...) — ibisabwa kugira ngo ECDSA ibeho. Intumbero ni zibiri: gutahura imiterere y’aligebra ituma imikono y’ubuhinga bwa none ishoboka no kwubaka ibikoresho vy’ukwizigirwa vya Python vyo kuyakoresha.


Uzoheza ushire mu ngiro ibice vya ECDSA: gukora urufunguzo, guhindura amajambo, gukora hashing, gukora umukono, no kugenzura. Iki gice gihuza ata guca ku ruhande inyigisho n’ibikorwa, kigashimika ku ndondoro y’ugushirwa mu ngiro n’ubukomezi bw’akarorero k’umutekano kashingiyeko.


### Bitcoin Ibikorwa vyo mu mutima


Mu gice ca kabiri, uzocapura imiterere y’isoko rya Bitcoin: UTXOs, inputs/outputs, urutonde, inyandiko, encodings, n’ibindi. Uzokwandika kode yo kwubaka, gusinya, no kugenzura amafaranga, uronke ugutahura neza ivyo hash ikora n’igituma.


Inyuma, uzoshira mu ngiro umukozi mutoyi _Script_, usuzume opcodes z'ingenzi, kandi wemeze inzira zo gukoresha. Intumbero ni ukugutuma ushoboye kugenzura inyifato y’ugucuruza, gusuzuma ukunanirwa kw’ugushingira intahe, no gutekereza ku bijanye n’umutekano w’ingingo ngenderwako zo gukoresha amahera.


### Bitcoin Urubuga rw'Ibikorwa vy'Imbere


Mu gice ca gatatu, uzoshira amafaranga muri sisitemu yagutse: imiterere y’amabuye, imitwe, ingorane, n’uburyo bwa Proof-of-Work. Uzokora ubutumwa bwa porotokole, imitwe y'amabuye, n'ibiti vya Merkle.


Ubwa nyuma, uzokwiga ivy'uguhanahana amakuru hagati y'abandi, gutuma ubutumwa bugenda neza, n'ugushiraho SegWit.


Nk’uko bigenda ku nyigisho yose yo kuri Plan ₿ Academy, igice ca nyuma kirimwo isuzuma ryagenewe gukomeza ugutahura kwawe. Ni mwiteguye guhishura ibikorwa vy’imbere vya Bitcoin no kwandika kode iyiha ubushobozi? Reka dutangure!










# Ivyiyumviro vy'ingenzi vy'imibare vya Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Imibare yo gushirwa mu ngiro kwa Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Ishingiro rya porogaramu ya Bitcoin: Imiterere nyamukuru y'imibare


Iyi nyigisho ihuriza hamwe imibare y’ingenzi iri inyuma y’imirongo y’ubuhinga bwa Bitcoin mu gukora neza cane. Ivyiyumviro birasigurwa, vyerekanywe n’ingero, hanyuma bikashirwa mu ngiro mu gitabu ca Jupyter. Iciyumviro kirongora ni coroshe: utahura vy’ukuri gusa ikintu ca kera c’ubuhinga bwa none iyo umaze kugishiramwo kode. Mu misi ibiri yose, abanyeshure generate testnet baratanga amaderesi, bubaka kandi bagatangaza amakuru, maze amaherezo bagakorana n’urubuga ata bashakashatsi b’amabuye. Ivyo vyose bisaba umushinge ukomeye mu bibanza bifise aho bigarukira no mu bigobe vy’imirongo y’imirongo.


### Ivyatsi bifise impera: Moteri y'imibare y'ubuhinga bwo gukingira amakuru


Igihugu gifise impera F(p) ni uburyo bw'imibare busobanurwa n'umubare w'intango p, urimwo ibintu 0 gushika kuri p–1. Ivyatsi vy'intango bituma ikintu cose kitari zero gifise igihinduka kandi [ibikorwa](https://planb.academy/resources/glossary/transaction-tx) vyose biguma mu mwanya. Imibare izunguruka ikoresheje modulo p mu kwongerako, gukurako no gukubita. Python's `pow(base, exp, mod)` ishoboza gukoresha neza ibiharuro, bihambaye ku biharuro binini bikoreshwa mu bikorwa vy'ukuri vy'ibanga.


#### Inyifato yo gukuza

Gukubitisha ikintu cose kitari zero k n'ibintu vyose vyo mu murima w'intango bituma habaho uguhinduka kw'umurima. Iyi nzira itanga icemezo c’uguhuza kandi igakingira intege nke z’imiterere, igatuma ivyumba vy’imbere biba vyiza cane ku bijanye n’uguhingura urufunguzo rw’urufunguzo n’[imikono y’ubuhinga bwa none](https://planb.academy/resources/glossary/digital-signature).


#### Ugucapura n’Iciyumviro gito ca Fermat

Ugucapura gushirwa mu ngiro biciye ku bihinduka vy’ugukubita. Iciyumviro gitoyi ca Fermat kivuga yuko .

n^(urupapuro-1) ≡ 1 (uburyo p),

rero igihinduka ni n^(p–2). Inyuguti ishigikira ibi ataco ihinduye na `pow(n, -1, p)`. Ivyo bikorwa biguma biboneka mu mirongo ngenderwako y’ubuhinga bwa [ECDSA](https://planb.academy/resources/glossary/ecdsa) na Bitcoin.


### Ivyuma bigoramye: Ivyubatswe bitagira umurongo ku bijanye n'umutekano w'urufunguzo rwa bose


Ivyiyumviro vy’uruzitiro bikurikira ingano y2 = x3 + ax + b. Bitcoin ikoresha secp256k1, isobanurwa ngo y2 = x3 + 7 hejuru y’umurima ufise impera. Uturongo turi ku nzira y’umurongo w’uruzitiro dukora umugwi w’imibare munsi y’ukwongerako uturongo. Umurongo uca mu ntumbero zibiri P na Q uca ku nzira y’umurongo ku ntumbero ya gatatu R; yerekana R ku ruhande rw’umurongo wa x bitanga P + Q. Uwo murongo ni uwufatanya kandi urimwo ikintu c’akaranga: akarongo kari ku butagira urugero.


Gutera kabiri akarongo bikoresha umurongo w’uruzitiro aho gukoresha umurongo w’uruzitiro, n’ugutemba gukomoka ku nkuru y’uruzitiro. Naho izo formule zirimwo uguharura ku mibare nyayo, zica zitandukanye kandi zikaba zitagira aho zigarukira iyo umurongo usobanuwe ku kibanza gifise impera—ni co kintu gikoreshwa muri Bitcoin.


### Kuva ku mibare gushika ku buhinga bwa Bitcoin


Ivyatsi bifise impera bitanga imibare igaragara, ihinduka; elliptic curves zitanga ubuhinga butagira umurongo aho guharura k·P vyoroshe ariko kuyihindura ntibishoboka mu kubara. Gufatanya ivyo vyose bitanga umushinge w’imfunguruzo za Bitcoin za bose/z’abikorera ku giti cabo, imikono ya ECDSA, n’umutekano w’ibikorwa. Gutahura ivyo bintu vy’ishimikiro bitegura abanyeshure gushira mu ngiro imfunguruzo, amafaranga n’imikono ata guca ku ruhande—ata bintu bitari vyo canke ibikoresho vyo hanze.


## Ugupfuka kw'ibara ry'agahama

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Iki gice kiratanga amabara y’uruzitiro asobanuwe ku bibanza bifise impera kandi kigasigura igituma ari vyo bikora umugongo w’imibare w’ubuhinga bwa Bitcoin. Naho imirongo y’imirongo y’imirongo y’imirongo y’imibare nyayo isa n’iyiryoshe kandi ikomeza, gukoresha izo nkuru nyene ku kibanza gifise impera bituma habaho urutonde rw’uturongo dutandukanye kandi dutatanye. Naho hariho itandukaniro ry’ivyo umuntu abona, amafomula yose yo kwongerako uturongo, amabara y’imirongo n’amategeko y’aligebra yitwararika kimwe nyene—imibare gusa ni yo ihinduka imibare y’ibice. Bitcoin ikoresha umurongo y2 = x3 + 7 (secp256k1), uzigama uburinganire n’inyifato idashingiye ku murongo bihambaye ku mutekano w’[ubuhinga bwo gukingira amakuru](https://planb.academy/resources/glossary/cryptography).


### Gusuzuma ingingo n'ugushirwa mu ngiro kw'umurima ufise impera


Intumbero iri ku nzira y’umurongo w’umurongo w’ibarabara iyo amakoordinate yayo ahaza n’ingero y’umurongo iri munsi ya modulo p. Kugenzura akarongo nka (73.128) kuri F133 bisaba kugenzura ko y2 mod p ingana na x3 + 7 mod p. Gushira mu ngiro ivyo muri kode birimwo guhingura amashure y'ibintu vy'umurima bifise impera n'ibiharuro vy'imirongo. Operator overloading ituma imibare yose—ugushiramwo, gukubita, gutera imbere, kugabanya—ikora ubwayo modulo p. Ivyo bintu bitaboneka bimaze kubaho, ibikorwa vy’ubuhinga bwa none vy’ubuhinga bwa none biraca bigororoka kwandika no kwiyumvirako.


#### Imiterere y'Itsinda n'Iyongera ry'Ingingo

Ivyiyumviro vy’umurongo w’uruzitiro bikora umugwi w’imibare uri munsi y’ukwongerwako. Iryo tsinda rihaza ugufunga, ugufatanya, akaranga (akarongo ku butagira urugero), n’ibihinduka (ugutekereza ku nzira ya x). Inyubakwa z’ubuhinga bw’ubuhinga bw’ubuhinga bw’ubuhinga ziremeza ivyo bintu, zigatuma ugukubita kw’ibiharuro (P yongerwako incuro nyinshi) gusobanurwa neza. Aya mategeko y’umugwi ashoboza ubuhinga bwo gukingira amakuru y’uruzitiro rw’uruzitiro kandi agatuma habaho inyifato idahinduka, ishobora gutegekanirwa mu gihe c’ibikorwa vy’inyuguti zisubirwamwo.


### Imigwi y'ingendo n'ikibazo ca logarithme itandukanye


Guhitamwo akarongo k’umuyagankuba G ku nzira y’umurongo bituma dushobora generate umugwi w’inzinguzingu: G, 2G, 3G, ..., nG = 0. Izo ntumbero zisa n’izitari mu murongo kandi zidashobora kumenyekana, mbere n’igihe zivugwa zikurikirana. Ukwo kudashobora kumenya imbere y’igihe ni kwo gutuma habaho umushinge w’ingorane y’ubuhinga bwa logarithme butandukanye: guharura P = sG biroroshe, ariko kumenya s kuva kuri P ni ikintu kidashoboka mu kubara ku migwi minini. Iyi nzira imwe ni yo ituma urufunguzo rwa bose rutekanye. Scalars ([imfunguruzo z’ibanga](https://planb.academy/resources/glossary/private-key)) zandikwa mu nyuguti ntoyi; uturongo ([imfunguruzo za bose](https://planb.academy/resources/glossary/public-key)) mu nyuguti nini.


#### Gukubitisha neza Scalar

Kugira ngo sG ibare neza, ibikorwa bikoresha ubuhinga bwo guharura kabiri no kwongerako: gucapura igishushanyo c’ibiharuro bibiri, gutera kabiri akarongo ku ntambwe yose, no kwongerako G gusa iyo bit ari 1. Ivyo bigabanya kubara kuva ku kwongerako O(n) gushika kuri O(log n), bikaba bishoboza ibikorwa vy’ubuhinga bwa cryptographic scalar mbere n’ibiharuro65.


#### Igicapo ca secp256k1 muri Bitcoin


Bitcoin ikoresha umurongo secp256k1, usobanurwa na y2 = x3 + 7 hejuru y’umurima w’intango aho p = 2256 − 232 − 977. Intumbero y’umuyagankuba G ifise amakoordinate adahinduka yatowe hakoreshejwe uburyo bw’imibare (“nta kintu kiri hejuru y’ukuboko kwanje”). Urutonde rw’umugwi n ni umubare munini w’intango wegereye 2256, bikaba bigaragaza ko akarongo kose katari zero kavyara umugwi umwe. Ingano ya 2256 (~1077) ni nini cane mu vy’inyenyeri, bituma gukoresha imfunguruzo z’ibanga zidashoboka. Mbere n’amaordinateri akomeye cane amajana n’amajana akora imyaka amajana n’amajana ntazogabanya mu buryo bufise insiguro ikibanza c’ingenzi.


### Imfunguruzo za bose, imfunguruzo z'ibanga, n'urutonde rwa SEC


Urufunguzo rw’ibanga ni scalar s y’imburakimazi; urufunguzo rwa bose ni P = sG. Kubera ko gutorera umuti ingorane y’uruzitiro rutandukanye bidashoboka, P irashobora gusangizwa ata guhishura s. Imfunguruzo za bose zitegerezwa gukurikirana kugira ngo zirungikwe hakoreshejwe uburyo bwa SEC. Uburyo bwa SEC butashizwemwo bukoresha amabayiti 65: intango 0x04 + x‐ihuriro + y‐ihuriro. Uburyo bukoreshwa gusa ama bytes 33: intango 0x02 canke 0x03 (bivanye n’uburinganire bwa y) + x‐coordinate. Bitcoin mu ntango yakoresha imfunguruzo zidapfutse ariko ubu ikunda imfunguruzo zipfutse kugira ngo zikore neza.


#### Bitcoin Address Irema


Aderesi za Bitcoin ni hashes z'imfunguruzo za bose, si imfunguruzo zitagiramwo ivyatsi ubwazo. Kugira ngo generate aderesi, ushireho urufunguzo rwa bose mu buryo bwa SEC, ushireho hash160 (SHA‐256 hanyuma RIPEMD‐160), ushireho imbere y’imbere y’urubuga (0x00 kuri mainnet, 0x6F kuri testnet), ushireho umubare w’isuzuma ukoresheje SHA‐256 mbere, ukoresheje Ishingiro58. Ukwo gushiramwo amakuru gukuraho inyuguti zidasobanutse kandi bikaba bishiramwo n’umubare w’ibintu bigenzurwa kugira ngo ntihagire amakosa yo kwandika. Intambwe nyinshi z’umuyoboro zinyegeza urufunguzo rwa bose gushika hakoreshejwe amahera, zongerako ikimenyetso c’urubuga, kandi zigatuma umuntu ashobora gusoma amaderesi, kandi adashobora gukora amakosa.


# Bitcoin Ibikorwa vyo mu mutima

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Gusesangura ubucuruzi n'imikono ya ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Gutahura ECDSA: Ishirahamwe ry'umukono wa Bitcoin


Bitcoin yizigiye ECDSA, umugambi w’umukono ushingiye ku nzira y’umurongo utanga umutekano ukomeye ufise ubunini bw’urufunguzo buto cane kuruta RSA. Umutekano wayo uva ku kibazo c’umurongo w’uruzitiro rw’uruzitiro: hatanzwe P = eG, guharura P biroroshe, ariko gukura e kuri P ntibishoboka mu kubara. Ubu butaringanire burashoboza gukingira urufunguzo rwa bose mu gihe urufunguzo rw’ibanga ruguma rutekanye.


#### DER Gushiramwo imikono ya ECDSA


Bitcoin ikoresha imikono ya ECDSA ikoresheje uburyo bwa DER:


- 0x30 (ikimenyetso c'urutonde)
- uburebure bwa byte
- 0x02 + uburebure + R bytes
- 0x02 + uburebure + S bytes


Ivyo vyongera amafaranga, bikagwiza umukono w’amabayiti 64 gushika ku mabayiti ~71–72. [Taproot](https://planb.academy/resources/glossary/taproot) irakuraho ubwo bushobozi mu kwemera imikono ya [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol) y’ubunini butahinduka.


### Ivyemezo vyo gusinya n'uburyo bwo gusinya


Imikono ya ECDSA ishingiye ku nsiguro y’ukwiyemeza: UG + VP = KG. Uwushira umukono ahitamwo agaciro ka U na V katari zero, n’agaciro ka [nonce](https://planb.academy/resources/glossary/nonce) K, kerekana ubumenyi bw’urufunguzo rw’ibanga ataco ahishuriye. Ubutumwa burashirwa muri Z, K idasanzwe iravuka, R ni x‐coordinate ya KG, na S = (Z + RE)/K. Umukono ni uwo mubiri (R, S). Umutekano uva cane ku gukoresha K yihariye, itamenyekana—iyo K yongeye gukoreshwa canke igasohoka, urufunguzo rw’ibanga rurahungabana. Ivyiyumviro vy’ubu bikoresha uruvyaro rwa K (RFC 6979) kugira ngo ntihagire ukunanirwa kwa RNG.


#### Igenzura ry'umukono

Hatanzwe Z, (R, S), n’urufunguzo rwa bose P, umugenzuzi abara U = Z/S na V = R/S, hanyuma akagenzura nimba x‐coordinate ya UG + VP ingana na R. Ivyo birakora kubera ko aligebra y’igenzura isubira kwubaka KG ataco ikeneye urufunguzo rw’ibanga. Guhingura imikono vyosaba gutorera umuti ingorane y’igitabu c’ivya kera canke guca igikorwa ca hash.


#### Imikono ya Schnorr n'ivyo mu mateka


Imikono ya Schnorr irasukuye mu biharuro kandi irashigikira ibiranga gukoranya, ariko yararonse uburenganzira igihe Bitcoin yatangura. ECDSA yaratanze ubundi buryo ku buntu, naho nyene bwari butoroshe cane kandi bufise imikono myinshi. Igihe uburenganzira bwo gukoresha ibintu bwari bwarangiriye, Bitcoin yongeyeko imikono ya Schnorr biciye kuri Taproot, itanga imikono idahinduka y’amabayiti 64 n’ubuzima bwite bwiza. ECDSA iguma ishigikiwe kubera uguhuza kw’iragi.



### Imiterere y'Ibikorwa n'Ivyinjira/Ibisohoka


Igurisha rya Bitcoin rigizwe na:


- verisiyo (bytes 4, iherezo rito)
- Urutonde rw'injiza
- Urutonde rw'ibisohoka
- Igihe co gufunga (amabayiti 4)


Injiza zivuga [UTXOs](https://planb.academy/resources/glossary/utxo) za kera n'urutonde rw'ibikorwa vyazo n'urutonde rw'isohoka, kandi zirimwo [inyandiko](https://planb.academy/resources/glossary/script) yo gufungura (scriptSig) n'umubare w'urutonde ukoreshwa ku gufunga igihe canke RBF. Ibisohoka bigaragaza umubare (8 bytes) n'inyandiko yo gufunga (scriptPubKey), bisobanura ivyangombwa vyo gukoresha. Amaderesi ya Bitcoin ni ibimenyetso vy’izo nyandiko.


#### Igishushanyo ca UTXO

Bitcoin ikurikirana ibisohoka bitakoreshejwe aho gukurikirana amafaranga asigaye kuri konti. UTXO zitegerezwa gukoreshwa zose—gukoresha igice ntibishoboka. Kugira ngo ukoreshe BTC 1 uvuye kuri 100 BTC UTXO, igikorwa gitegerezwa kubamwo igisohoka c’ihinduka. Kwibagirwa umusaruro w’ihinduka bihindura ibisigaye bikaba amahera y’umucukuzi.


#### Urutonde rw'ibikorwa n'ugusesangura


Ibikorwa bikoresha uburyo bubiri bukomeye. Inyuma y'umurima wa verisiyo, umubare w'ibintu vyinjijwe. Ivyo winjiza birimwo:


- imbere tx hash (amabayiti 32)
- urutonde rw'ibisohoka (bytes 4)
- inyandiko (varstr)
- urutonde (amabayiti 4)


Ivyasohoka birimwo umubare w'amabayiti 8 n'urufunguzo rw'inyandiko (varstr). Igihe co gufunga kigenzura igihe igikorwa co gucuruza kizoba gifise akamaro. Urutonde rukoresha urutonde rw'imibare myinshi. Abasesangura bafungura ama bytes mu buryo bukurikirana kandi bagashinga amashure yihariye ku vyinjizwa, ibisohoka, n'inyandiko.


### Amafaranga, Ihinduka, n'Ugukomera


Amafaranga araboneka:

amafaranga = umubare(agaciro k’inyungu) – umubare(agaciro k’isohoka).

Agaciro kose katatanzwe kaba amahera, bigatuma ihinduka ryiza ry’ubwubatsi bw’umusaruro riba ngombwa. Imbere ya [SegWit](https://planb.academy/resources/glossary/segwit), imikono yaremeza ko umuntu ashobora guhindura S kugira ngo abe N-S vyatuma haba ugucuruza gushasha gufise akamaro gafise ID itandukanye. Bitcoin ubu ishira mu ngiro itegeko rya low‐S, kandi SegWit itandukanya imikono n’ibara rya txid, igatuma IDs zigumaho kandi zishoboza amasezerano y’urugero rwa kabiri nka [Lightning](https://planb.academy/resources/glossary/lightning-network).


## Bitcoin inyandiko n'ukwemeza ibikorwa

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script ni ururimi ruto, rushingiye ku rutonde rw’amasezerano y’ubwenge rusobanura ingene ibiceri bishobora gukoreshwa. Igisohoka cose gifise scriptPubKey (inyandiko yo gufunga) kandi igisohoka cose gifise scriptSig (inyandiko yo gufungura). Bompi hamwe baragira porogarama itegerezwa gusuzuma ko ari “ukuri” kugira ngo amahera akoreshwa abe ay’ukuri. Script ntabwo ari Turing-complete kugira ngo inzira zose zo gukora zibe zishobora gutegekanirwa kandi zibe zoroshe kwemezwa ku rubuga rwose.


### Inyandiko y'imikorere n'Icitegererezo c'Ishirwa mu ngiro


Inyandiko ni urutonde rw'ibintu vy'amakuru n'amakode y'ibikorwa. Amakuru asunika (imikono, imfunguruzo za bose, ama hashes) ashirwa ku kirundo, mu gihe opcodes zitangura na `OP_` zihindura ikirundo. Inyuma y'ugushirwa mu ngiro, ikintu co hejuru kigomba kuba kitari zero kugira ngo kigende neza. Ingero: `OP_DUP` isubiramwo ikintu co hejuru, `OP_HASH160` ikoresha SHA256 hanyuma RIPEMD160, na `OP_CHECKSIG` igenzura umukono ku giciro c’isoko n’urufunguzo rwa bose, isunika 1 ku bijanye n’ukuri, 0 ku bijanye n’ukudakora. Amategeko yo gusesangura atandukanya amakuru atagiramwo ivyatsi (uburebure-bwa mbere) n'amakode y'ibikorwa (arabwa hejuru n'agaciro ka byte), kandi imashini ntoyi y'ivy'impwemu irabikora mu buryo butegekanijwe ku nzira yose.


### P2PK na P2PKH: Uburyo bwo kwishura


Igishushanyo ca mbere, kwishura-urufunguzo rwa bose (P2PK), rwafunga ibiceri ataco bimaze ku rufunguzo rwa bose rwuzuye: scriptPubKey ni `<pubKey> OP_CHECKSIG`, kandi scriptSig ni umukono gusa. Biroroshe ariko ntibitwara umwanya kandi bigaragaza urufunguzo rwa bose imbere y’uko ibiceri bikoreshwa.


#### P2PKH n'amaderesi

Ivyishura-ku-Rufunguzo-Rusa-Hash (P2PKH) bitera imbere ivyo mu gufunga ku 20‐byte hash y'urufunguzo rwa bose. Urufunguzo rw'inyandiko ni `OP_DUP OP_HASH160 <urufunguzo_rw'inyandiko> OP_EQUALVERIFY OP_CHECKSIG`, kandi inyandikoSig itanga `<umukono> <urufunguzo rw'inyandiko>`. Ishirwa mu ngiro rigenzura ko urufunguzo rwa bose rwatanzwe rujanye n'agaciro kagenewe hanyuma rugasuzuma umukono. Ivyo bihisha urufunguzo rwa bose gushika rumaze umwanya, bikagabanya ubunini, kandi bikajanye n’uburyo bumenyerewe bw’aderesi “1...” mainnet.


### Kwemeza ubucuruzi n'ugushira umukono


Igikoresho cemeza ubucuruzi kigomba kumenya neza:

1) Injiza yose yerekana igisohoka kiriho, kitakoreshejwe.

2) Agaciro k’ivyo vyose bishizwemwo ≥ agaciro k’ivyo vyose bisohotse (itandukaniro ni amafaranga).

3) Buri scriptSig ifungura neza scriptPubKey yayo ivugwa.


Gusuzuma umukono bisaba kwubaka ubutumwa nyabwo bwashizweko umukono, bwitwa sighash. Ku ECDSA ya kera, kwemeza gukuraho ubusa scriptSigs zose, gusubirira scriptSig y’inyungu y’ubu n’inyandikoPubKey ihuye, kwongerako ubwoko bwa hash bwa 4‐byte (kenshi `SIGHASH_ALL`), maze ugasubirira kabiri igisubizo. Uwo mubare w’ibice 256 ni wo `OP_CHECKSIG` ikoresha. Ubwoko bundi bwa hash (nk'akarorero, `SINGLE`, `NONE`, bufise canke butafise `ANYONECANPAY`) burahindura ibice vy'ibikorwa vy'ubudandaji vyemejwe, bikaba bishoboza gukoresha ibintu nk'ugufashanya canke ibikorwa vy'ubudandaji vyerekanwa bimwe bimwe, ariko ntibikoreshwa cane mu bikorwa.


#### Hashing y'ibice bine na SegWit

Kubera ko ikintu cose cinjijwe mu gucuruza kw’iragi gisaba ibara ryaco ry’ibara ry’agahama ku mibumbe irimwo ibintu vyose vyinjijwe, igihe co kwemeza gishobora gukura mu buryo bwa quadratique n’umubare w’ibintu vyinjijwe. Ibikorwa vyinshi vy’inyungu vyinshi vyari vyaratumye habaho ugucererwa kw’ugushingira intahe. SegWit yahinduye ubuhinga bwo kubara sighash kugira ngo ihishe ibice vyasangiwe no kugabanya ubugoyagoye ku gihe c’umurongo, itera imbere mu gupima no gutuma ibitero vyo kwanka ibikorwa bikomera.


### Ivyigwa vy'Inyandiko n'Ivyigwa vy'Umutekano


Ivyanditswe birashobora guserura ibirenze cane “umukono umwe urafungura ivyo biceri.” Ivyo bigaragazwa n’ibiharuro vy’inyandiko mu gushiramwo ibintu bitari vyo—ingorane z’imibare, ingorane z’imbere y’amashusho, canke mbere n’ibihembo vy’ugutombora—aho umuntu wese atanga amakuru akwiriye ashobora gukoresha ivyo biceri. Ariko rero, ibisohoka bishingiye gusa ku makuru ya bose (nta mikono) birashobora gushikirwa n’ugukora kw’abacukuzi: iyo umuti ubereye ubonetse muri [mempool](https://planb.academy/resources/glossary/mempool), [umucukuzi](https://planb.academy/resources/glossary/miner) wese arashobora kuwukopa maze akarungika amahera yishurwa kuri we nyene.


Icigwa ngirakamaro ni uko amasezerano y’isi nyakuri hafi y’igihe cose arimwo ivy’ugusuzuma imikono, mbere n’igihe arimwo ivyiyumviro bikomeye cane nk’ivy’amasinyatire menshi, ivy’igihe, canke ivy’amasinyatire. Imikono ibohera umuti ku ruhande runaka, ikazigama inkurikizi kandi ibuza abandi kwiba amahera. Gutahura urugero rwa Script, uburyo busanzwe, n’imitego idasanzwe ni ngombwa mu guhingura amasezerano y’ubwenge ya Bitcoin no gutekereza ku kuntu amafaranga yemezwa ku rubuga.


## Ubwubatsi bw'Ibikorwa n'Ukwishura-Ku-Inyandiko Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Inyubakwa Bitcoin Ibikorwa na P2SH


Bitcoin ubucuruzi bw’inyubako y’ibiraro ubumenyi bw’amasezerano y’ivyiyumviro n’ugushirwa mu ngiro kw’ibikorwa. Igikoresho gihitamwo UTXOs zo gukoresha, cubaka ibisohoka bifise inyandiko zo gufunga, kigakora imikono ku kintu cose cinjijwe, kandi kigashira mu rutonde vyose mu buryo nyabwo ama node yiteze. Ivyo bisaba gutahura ivy’uguhingura sighash, inyifato ya Script, n’ugukosora amafaranga n’uguhindura.


### Ubwubatsi bw'ibanze


Buri nzira y’ugucuruza yerekana igisohoka ca kera ca txid n’urutonde. Ivyasohoka bigaragaza amafaranga mu satoshis no mu nyandiko zo gufunga. Itandukaniro hagati y’ivyo vyose vyinjizwa n’ivyo vyose bisohoka ni amahera. Kugira ngo umuntu ashire umukono ku vyo winjije, verisiyo yahinduwe y’ivyo akora irakurikirana, sighash yayo iraharurwa, urufunguzo rw’ibanga na rwo rugashirwako umukono. Ivyo bivako umukono n'urufunguzo rwa bose bikora ScriptSig. Igihe ikintu cose cinjijwe gishizweko umukono, igikorwa c’ubudandaji gishobora gutangazwa ku rubuga.


### Ibikorwa vy'imikono myinshi


Bare multisig ikoresha `OP_CHECKMULTISIG` kugira ngo isaba imikono m-of-n. Kubera ikibazo c'imbere y'igihe, OP_CHECKMULTISIG ifungura ikintu c'inyongera, gisaba `OP_0` y'intango muri ScriptSig. Bare multisig irakora ariko ntikora neza: imfunguruzo zose za bose zigaragara on-chain, bituma scriptPubKeys iba nini, zizimvye, kandi zigoye gushiramwo nk’amaderesi. Ivyo bibujijwe ni vyo vyatumye habaho ubuhinga bwo kwishura-ku-script-hash.


#### P2SH Ubwubatsi

P2SH ihisha inyandiko zikomeye inyuma ya HASH160 y'amabayiti 20. Urufunguzo rw'inyandiko rwashizweho: `OP_HASH160 <20-byte hash> OP_EQUAL`. Inyandiko y’ugucungura iri mu nyuma—irimwo multisig, timelocks, canke ibindi bintu—ihishurirwa gusa kandi igashirwa mu ngiro igihe umuntu akoresha amahera. Uwurungitse abona gusa hash, mu gihe uwuronka acungera inyandiko y’ugucungura mu bwiherero. Ivyo bigabanya ubunini bwa on-chain, bituma umuntu agira ubuzima bwiwe bwite, kandi bituma ababirungika bashobora gukora amasezerano agoranye ata mutwaro.


### P2SH Gukoresha n'ugushirwa mu ngiro


Kugira ngo ukoreshe igisohoka ca P2SH, ScriptSig itegerezwa kubamwo amakuru akenewe yo gufungura *ushizemwo* inyandiko yo gucungura ubwayo. Kwemeza bibera mu ntambwe zibiri:

1) HASH160(gucungura_inyandiko) itegerezwa guhura n'inyandikoPubKey hash.

2) Inyuma yo kugenzura, inyandiko yo gucungura irashirwa mu ngiro n’amakuru yatanzwe.


Igihe utanga imikono y'inyandiko ya P2SH, igikorwa ca sighash gikoresha inyandiko yo gucungura mu kibanza c'inyandikoPubKey. Umuntu wese ashirako umukono ategerezwa kuba afise inyandiko yuzuye yo gucungura ku mikono y’ukuri ya generate. Aderesi za P2SH zikoresha verisiyo ya byte 0x05 kuri mainnet (“amaderesi 3...”) na 0xC4 kuri testnet (“amaderesi 2...”).


#### Ivyiyumviro vy'umutekano


Gutakaza inyandiko yo gucungura bisigura gutakaza amahera: gukoresha amahera bisaba imfunguruzo z’ibanga n’inyandiko yo gucungura ubwayo. Abaje muri Multisig bategerezwa kugenzura ko imfunguruzo zabo za bose zishizwemwo neza imbere y’uko bemera amahera. P2SH ishigikira inyubakwa ziteye imbere nka multisig, timelocks, na hashlocks, ariko amakosa mu nzira y’inyandiko ashobora gufunga amahera ubudasiba, rero kugerageza kuri testnet ni ngombwa.


P2SH iratuma umuntu agira ubuzima bwite mu guhisha uko akoresha amahera gushika igihe akoresha amahera ya mbere, ariko iyo inyandiko yo gucungura ibonetse on-chain, iraboneka ubudasiba. Naho ari ukwo, inyungu zo kugabanya ubunini, gusubira inyuma, no gufashwa n’amasezerano vyatumye P2SH iba ikintu gihambaye, bigira ico bikoze ku vyo gusubiramwo mu nyuma nka SegWit na Taproot.


# Bitcoin Urubuga rw'Ibikorwa vy'Imbere

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Amabuye ya Bitcoin na Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin ibuza amafaranga y'imigwi kandi ikayakingira ikoresheje [proof of work](https://planb.academy/resources/glossary/proof-of-work). Buri bubiko burimwo [umutwe](https://planb.academy/resources/glossary/block-header) w’amabayiti 80 hamwe n’urutonde rw’ibikorwa. Naho igiciro c’inguvu kiremereye co gukora igice gifise akamaro, kugenzura kimwe birahenda: kubika imitwe yose ~900k bisaba gusa ~72 MB, bikaba vyemerera mbere n’ibikoresho bitobito kugenzura neza proof of work y’uruzitiro.


### Ibikorwa vya Coinbase n'Impembo z'Ibubiko


Buri block itangura n’ugucuruza kumwe nyakwe kwa [Coinbase](https://planb.academy/resources/glossary/coinbase-transaction)—uburyo bumwe rudende bitcoin nshasha yinjira mu nzira. Ifise hash ya prev-tx ifise zero n’urutonde rwa 0xffffffff, biyimenyesha mu buryo budasanzwe. Iyo nkunga yatanguye kuri 50 BTC kandi igabanywamwo ibice bibiri buri mabarabara 210.000 (50, 25, 12,5, 6,25, 3,125, ...). Abacukuzi b’[amabuye](https://planb.academy/resources/glossary/block) y’agaciro na bo nyene barashiramwo amahera yo gucuruza. Kubera ko nonce ya 4‐byte ari nto cane ku ASIC za none, abacukuzi barahindura amakuru mu gucuruza kwa Coinbase kugira ngo bahindure umuzi wa [Merkle](https://planb.academy/resources/glossary/merkle-tree) maze bareme ikibanza co gushaka congereweko. [BIP34](https://planb.academy/resources/glossary/bip) isaba gushiramwo uburebure bw’ibarabara mu nyandiko ya Coinbase kugira ngo umenye neza ko Coinbase txid yose ari iyo kwihariza.


### Imirima y'umutwe w'ibarabara n'ikimenyetso ca Soft Fork


Umutwe w'amabayiti 80 urimwo:


- verisiyo (amabayiti 4)
- hash y'imbere (bayiti 32)
- Umuzi wa Merkle (amabayiti 32)
- ikidodo c'igihe (bytes 4)
- ibice ([ingorane](https://planb.academy/resources/glossary/difficulty) intego, 4 bytes)
- noce (amabayiti 4)


Igitigiri c’amaverisiyo carahindutse uburyo bwo gutanga ikimenyetso biciye ku BIP9, bituma abacukuzi bashobora guhuza ukwitegura kwa [soft-fork](https://planb.academy/resources/glossary/soft-fork). Ikimenyetso c'igihe ni agaciro k'igihe ca Unix 32‐bit kandi kizokenera guhindurwa hafi y'umwaka wa 2106.


#### Bits Umurima n'Intego

Igihugu c'ibice gishiramwo intumbero mu buryo bukomeye: intumbero = umubare × 256^(igiharuro−3). Hashes z'ububiko zifise akamaro zitegerezwa kuba ziri munsi y'iyi ntumbero. Kubera ko hashes zisobanurwa nk'imibare yose y'iherezo rito, hashes zibereye akenshi ziboneka n'ibiharuro vyinshi bikurikira iyo zigaragajwe mu hex.


### Ingorane, Kwemeza, n'Impinduka


Ingorane isobanurwa nk’intumbero_y’inyuma / intumbero_y’ubu, igaragaza ingene mining ikomeye cane uno musi ugereranyije n’ingorane yoroshe cane. Kwemeza bisaba gusa kugereranya hash y'umutwe n'intumbero-ihendutse cane ugereranije na mining.


Igihe cose mu mwaka w’2016, Bitcoin irahindura ingorane kugira ngo igere ku bihe vy’iminota ~10. Iryo hinduka rigereranya igihe nyaco c’amabarabara y’umwaka w’2016 aheze n’indwi zibiri zitezwe. Imipaka ibuza guhindura ibintu gushika mu rugero rwa kane. Ibintu bikomeye vyabaye mw’isi nyakuri—nk’uguhagarika mining kw’Ubushinwa—vyerekanye ko ubu buryo bushobora guhangana n’igihe igipimo ca hash cagabanutse cane kandi ingorane zigahindurwa zija hasi kugira ngo zisubize inyuma.


### Infashanyo y'Igice n'Igitigiri cose Supply


Infashanyo ku burebure h ibarwa nk’iyi: infashanyo = 5_000_000_000 >> (h // 210_000). Ivyo bituma urutonde rwo guca igice ruja ku bijanye n’ugutanga ~21 miliyoni BTC. Gucapura urutonde rw’ibiharuro (50 + 25 + 12,5 + ...) × 210.000 bisigura igipfukisho. Abacukuzi bashobora gusaba infashanyo ntoyi kuruta iyo bemerewe ariko ntibazokwigera basaba infashanyo nyinshi, canke iyo block ikaba itagira akamaro. Uko infashanyo zigabanuka kubera ibice bikurikirana, amafaranga y’ugucuruza aba igice gihambaye cane c’amahera abacukuzi baronka n’umutekano w’uruja n’uruza rw’igihe kirekire.


## Itumatumanako n'ibiti vya Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Ubwubatsi bw'urubuga


Bitcoin’s [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) network ikora nk’uburyo bw’urusaku bwegerejwe aho ama node atanga amakuru n’amabuye ata kwizigirana. Ivyuma bishasha biratangura mu guhura n’imbuto za DNS zifise amakode akomeye zibungabungwa n’abahinguzi b’ingenzi. Izo mbuto za DNS zigarura IPs z’abagenzi bakora, zituma nodes zishobora kumenya urubuga hanyuma zigasaba abagenzi b’inyongera biciye kuri getaddr. Gukorana n’abandi si ikintu gihambaye cane ku bijanye n’[uguhurizako](https://planb.academy/resources/glossary/consensus), rero ugushirwa mu ngiro gushobora gutandukanywa igihe cose amategeko y’uguhurizako azoguma atahindutse.


### Ubutumwa buteye n'ugufata ukuboko


Ubutumwa bwose bwa Bitcoin P2P bukoresha ibahasha ridahinduka: agaciro k’ubupfumu k’amabayiti 4 (F9BEB4D9 kuri mainnet), itegeko rya ASCII ry’amabayiti 12, uburebure bw’umuzigo w’amabayiti 4 (hacksumstsh y’iherezo ry’amabayiti 4), uburebure bw’umuzigo w’amabayiti 4 n’umubare w’amabayiti 4). umuzigo w’inyungu. Amategeko asanzwe arimwo verisiyo, verack, inv, getdata, tx, ububiko, getheaders, imitwe, ping, na pong.


Ugufatanya ukuboko gutangura iyo urudodo ruhuza rwohereje ubutumwa bwa verisiyo. Uwuronka asubiza na verack na version yayo bwite. Iyo impande zompi zimaze guhanahana ubwo butumwa bubiri, iyo nzira irakora kandi ama node ashobora gutangura gutanga amakuru n’amakuru.


### Ibiti vya Merkle n'imizi ya Merkle


Bitcoin ibika umuzi umwe wa Merkle w’amabayiti 32 mu mutwe w’ibara ryose nk’ukwiyemeza ku bikorwa vyose biri muri ibara. Ibikorwa vy’ubudandaji birashirwako (hash256), bikajanywa, bikajanywa, bigasubirwamwo gushika hash imwe isigaye. Iyo urugero rufise igiharuro kidasanzwe, hash ya nyuma irasubirwamwo. Imbere, [hashes](https://planb.academy/resources/glossary/hash-function) ni big‐endian, mu gihe amakuru y’ibice vy’uruhererekane akoresha little‐endian, bisaba guhindura imbere n’inyuma y’ubwubatsi bw’igiti.


#### Ivyemezo vya Merkle na SPV

Ivyemezo vya Merkle bituma umuntu ashobora kugenzura ko igikorwa co gucuruza kiri mu gice ata gukuraho igice cose. Ikimenyamenya gifise ama hashes y’abavukanyi ku nzira ija ku muzi. Abaguzi ba SPV bafise uburemere buke babika gusa imitwe y’amabuye kandi basaba ivyo bimenyamenya ku bice vyuzuye. Kubera ko igiti ca Merkle gikura mu buryo bwa logarithme, kwemeza ko gishizwe mu gice gifise ibihumbi vy’ibikorwa bisaba amajana makeyi gusa y’ama byte.


Taproot iragura iki ciyumviro mu gushinga amategeko y’ugukoresha amahera ku giti c’inyandiko ca Merklized (MAST), ihishura gusa ishami ryakozwe hamwe n’ikimenyamenya ca Merkle. Ivyo bituma umuntu akora neza kandi akagira ubuzima bwiwe bwite.


### Imikorere y'urubuga n'uguhuza


Nodes zikoresha getdata kugira ngo zisabe ibikorwa canke amabuye, zigaragaza ubwoko bw'ID (1=tx, 2=ububiko, 3=ububiko bwayunguruwe, 4=ububiko bukomeye) hamwe n'ikimenyetso c'amabayiti 32. Ku bijanye n’uguhuza uruzitiro, amanode yohereza getheaders n’intango y’ibarabara, yakira imitwe igera kuri 2000 mu kwishura. Buri mutwe ugarutse ni 80 bytes ukurikiwe n'igiharuro c'ibikorwa vy'ubuhendanyi ca zero.


Gusuzuma neza amabuye yakiriwe bisaba gusuzuma kabiri:

1. Igiharuro c’ibarabara kigomba kuba kiri munsi y’intumbero yakodejwe mu kibanza c’ibice.

2. Umuzi wa Merkle ubazwe mu bikorwa vyose (n’ugukoresha neza endianness) utegerezwa guhura n’umuzi w’umutwe.


Iyo ivyo bintu vyose bishobotse ni ho gusa urudodo rwemera iyo nzira, ivyo bikaba vyerekana ingingo ngenderwako ya Bitcoin y’uko “ntiwizigire, usuzume”.


## Uguhanahana amakuru n'Icabona gitandukanye

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Iki kiganiro gihuza ubuhinga buteye imbere bwa P2P n’Icabona gitandukanye, kigaragaza ingene porogarama ya Bitcoin yo muri iki gihe ikorana ata guca ku ruhande n’ibihimba vy’umubiri mu gihe ikoresha imiterere y’ugucuruza izi SegWit. Abahinguzi bariga kugarura amabuye, gupima amafaranga akenewe, no kwubaka amafaranga bakoresheje gusa ubuhinga bwo guhanahana amakuru ku rubuga rwa interineti—nta bashakashatsi b’amabuye basabwa.


### Gusubirana n'ubuzima bwite bushingiye ku bubiko


[Amasakoshi](https://planb.academy/resources/glossary/wallet) ategerezwa kumenya amahera yinjira mu gucapura amabuye y'ibisohoka bihuye n'inyandikoPubKey yabo. Kugarura amabuye yose birakingira ubuzima bwite kurusha gusaba amafaranga y’umuntu ku giti ciwe, ivyo bikaba bitanga ibimenyetso bikomeye ku bikorwa vy’abakoresha. Mbere n’ibisabwa vy’amabuye bishobora gusohoka amakuru ku minyororo y’ijwi ritoyi, bikaba bituma amayunguruzo y’amabuye (BIP158) aba ari ngirakamaro ku bakiriya b’umuco bazigama ubuzima bwite. Amayunguruzo ashobora gutanga ivyiza vy’ibinyoma ariko ntiyigere atanga ivyiza vy’ibinyoma, bikaba vyemerera abaguzi gukuraho gusa amabuye ashobora kuba afise akamaro ata guhishura amaderesi yihariye.


### Trustless Ihuriro ry'urubuga


`get_block` yerekana ikoreshwa ryiza ry'urubuga: kohereza getdata, kwakira ububiko, hanyuma wigenga ugenzure umuzi wayo wa Merkle na proof of work. Igipande cemerwa gusa iyo hash y'umutwe yakiriwe ihuye n'hash yasavye kandi umuzi wayo wa Merkle waharuwe uhuye n'umutwe. Ivyo birimwo “ntiwizere, usuzume,” kugira ngo mbere n’abo mu runganwe rw’ububisha badashobora guhenda amanode ngo yemere amakuru yahinduwe.


#### Kugarura amafaranga kuva mu mabuye

Ibikorwa vy’ibarabara bishobora gusuzumwa kugira ngo bihure n’inyandikoPubKeys hakoreshejwe ugusubiramwo kworoshe. Ivyo bikoresho bikora ubudasiba uko amabuye mashasha ashika, bigaragaza ko ari vyo bifise ibisohoka biciye mu kwemeza amakuru y’ibanga aho kwizigira API z’abandi.


### Intumbero n'imiterere ya SegWit


Icabona gitandukanye (SegWit) carashizeho uburyo bwo gukorana n’ibindi bihugu mu gukuraho amakuru y’umukono mu biharuro vya txid. Ivyo vyatumye habaho imirongo y’ubudandaji yizigirwa kandi vyatumye Lightning Network ikora. SegWit nayo yongeye ubushobozi bw’amabuye ikoresheje “uburemere bw’amabuye”: amanode ya kera aracariko arabona amabuye ≤1 MB, mu gihe amanode yavuguruwe yemeza gushika kuri 4 MB harimwo n’amakuru y’ivyabona. Porogarama z’ivyabona zahinduwe (v0–v1 gushika ubu) zirema inzira y’ugusubiramwo itunganijwe ku bwoko bw’inyandiko zo muri kazoza.


#### P2WPKH (Ivyabona vya Yehova-125)


P2WPKH isubirira iragi ry’imiterere ya P2PKH n’inyandiko y’amabayiti 22: OP_0 + push20 + hash160(urufunguzo rwa pub). Gukoresha amahera bijana umukono n’urufunguzo rwa pubkey mu kibanza c’icabona gitandukanye.


- Pre‐SegWit nodes: raba “umuntu wese ashobora gukoresha,” ubifate nk’ibibereye.
- Ivyiyumviro vy’inyuma ya SegWit: menya OP_0 + 20‐byte hash no kwemeza hakoreshejwe amakuru y’ivyabona.


Ukwo gutandukanya gutuma umuntu agira ubugoyagoye kandi bikagabanya amahera. Umushingantahe akoresha igiharuro c’ibintu bitandukanye gikurikiwe n’umukono n’urufunguzo rwa pubkey.


#### P2SH-P2WPKH (Inyuma-Ihuye SegWit)


Kugira ngo amasakoshi ya kera ashobore kohereza kuri aderesi za SegWit, inyandiko za P2WPKH zirashobora kuzingwa muri P2SH.


- urufunguzo rw'inyandiko: rusanzwe P2SH hash160 (inyandiko yo gucungura)
- inyandikoSig: inyandiko yo gucungura (porogaramu ya P2WPKH)
- icabona: umukono + urufunguzo


Ivyagezwe vy'ukwemeza:

1. Ivyuma vy’imbere ya BIP16 vyemeza ko redeemScript ari ngirakamaro.

2. Ivyuma vy’inyuma ya BIP16 birabisuzuma, bikasiga OP_0 + hash ku rutonde.

3. Ama node ya SegWit akora ivyemezo vy’ivyabona vyuzuye.


#### P2WSH ku nyandiko zigoye


P2WSH ikoresha SegWit ku nyandiko nyinshi n'iziteye imbere mu kwiyemeza SHA256 (inyandiko) aho gukoresha hash160. Igiharuro c'ivyabona vy'ibimenyetso vyinshi 2 kuri 3:


- Ikintu ubusa (SUZUMA MULTISIG ikibazo)
- ikimenyetso1
- sig2.
- inyandiko y'icabona (inyandiko y'ibimenyetso vyinshi)


140 SegWit nodes zigenzura SHA256 (inyandiko y'icabona) ihuye n'inyandikoPubKey hash hanyuma zigakora. Gukoresha SHA256 na 32‐byte hash bituma umuntu ashobora gutandukanya P2WSH na P2WPKH kandi bikomeza umutekano.


#### P2SH-P2WSH (Uguhuza gukomeye)


Ivyanditswe bikomeye vya SegWit birashobora kandi kuba bizingiwe na P2SH:


- inyandiko: gucungura inyandiko (OP_0 + 32‐byte hash)
- icabona: imikono + icabonaScript


Kwemeza bica mu mayaruka atatu y'amategeko nk'uko biri kuri P2SH‐P2WPKH. Ivyo bipfukisho vyari bihambaye ku bikorwa vya Lightning vya kera vyari bikeneye multisig ata n’umwe ashobora gukora. Naho P2WSH kavukire ari yo ikundwa muri iki gihe, uburyo buzingiye buratuma habaho uguhuza n’ibindi bikoresho vya kera vya wallet.


### Ingaruka za SegWit


SegWit yatanzwe:


- Indangamuntu z'ubucuruzi zidahinduka
- amafaranga make biciye ku makuru y'ivyabona yagabanutse
- Uburemere bw'ububiko burengeye ubw'ububiko
- guhuza n'ibice vya kera
- inzira isukuye yo gusubiramwo Taproot n'ibindi bizoza


Ivyo bikoresho hamwe n’ugukorana kw’urubuga rutagira icizigiro, ni vyo bifasha mu guteza imbere Bitcoin y’ubu.



# Igice ca nyuma


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Amasuzuma n'Ibipimo


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Ikizame canyuma


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Iciyumviro



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>