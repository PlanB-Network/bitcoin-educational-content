---
name: be-BOP
description: Inyobora ngirakamaro yo gutuma ubucuruzi bwawe bugira amahera ukoresheje be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** ni urubuga rw’ubudandaji rwo kuri internet rwagenewe abacuruzi bipfuza kugurisha kuri internet no hanze yayo, mu kwigenga kwose, mu gihe bemera kwishura mu Bitcoin, biciye kuri konti ya banki no mu mafaranga. Umuti ni ngirakamaro kandi ku bwoko bwose bw’ishirahamwe ryipfuza gukoranya intererano canke gukoresha amahera mu bikorwa vyaryo bitandukanye.



Umuti ni woroshe, woroshe kandi wigenga. Bituma habaho iduka ryo kuri Internet, mbere no mu bidukikije aho ibikorwa vy’ivy’ubutunzi vya kera bifise aho bigarukira canke bitaboneka. Nkako, **be-BOP** yarateguwe kugira ngo ikore neza ifise canke idafise uburenganzira bwo gukoresha amabanki, ikoresheje Bitcoin nk’ibikorwa remezo vyo kwishura.



Muri iyi nyigisho, tuzogutwara intambwe ku yindi muri:





- Rema iduka ryawe rya mbere kuri internet ukoresheje **be-BOP**
- Guhindura ivyerekanwa vyawe n'ibicuruzwa vyawe
- Kugena uburyo bwo kwishura buboneka
- Gutahura uburyo bwiza bwo kugurisha neza kuri internet ukoresheje **be-BOP**



Iyi nyigisho ntisaba ubuhinga buhanitse. Igenewe abaterambere hamwe n’abahinguzi b’ibintu, abacuruzi, amakoperative canke abacuruzi bipfuza gutangura ubudandaji bw’ubuhinga bwa none mu buryo bwigenga kandi bukomeye.



## Ibisabwa vyo gushiramwo be-BOP kuri server yawe bwite



Imbere y’uko utangura gushiramwo be-BOP, urabe neza ko ufise ibikorwa remezo vy’ubuhinga bikurikira. Izo Elements ni nkenerwa kugira ngo urubuga rukore neza:



### S3-ububiko buhuye



be-BOP ikoresha uburyo bwo kubika amadosiye (nk'amashusho y'ibicuruzwa). Ivyo bisaba ko umuntu ashobora gukoresha ubuhinga bwa S3, nka:





- [MiniIO](https://min.io/) yiyakira
- Amazoni S3 (AWS)
- Ububiko bw'ibintu



Uzokenera gutunganya indobo maze ugatanga aya makuru akurikira:





- S3_INDOBO**: izina ry'indobo
- S3_IMPERA_URL**: ukwinjira ku rubuga rwawe rwa S3
- S3_URUPFUZO_ID** na **S3_URUPFUZO_IBANGA**: amakode yawe yo kwinjira
- S3_REGION**: akarere ka serivisi yawe ya S3



### Ububiko bw'amakuru bwa MongoDB mu buryo bwo gusubiramwo



be-BOP ikoresha MongoDB mu kubika ububiko, umukoresha, igicuruzwa n'ibindi bimenyetso.



Ufise uburyo bubiri:





- Shiraho MongoDB mu karere n'**Uburyo bwa ReplicaSet bushobojwe**
- Koresha serivisi yo kuri internet nka **Igitabu ca MongoDB**



Uzokenera ibi bikurikira:





- MONGODB_URL**: ihuriro ry'urutonde rw'amakuru Address.
- MONGODB_DB**: izina ry'urutonde



## Node.js ibidukikije



be-BOP ikorana na Node.js. Raba neza ko ufise **Node.js** verisiyo 18 canke irenga kandi **Corepack** ikoreshwa (bikenewe kugira ngo ushobore gucunga abarongozi b'amapaki nka pnpm). Itegeko ryo gukoresha ni `corepack ishoboza`



### Git LFS yashizweho



Hariho ibikoresho (nk’amashusho manini) bicungirwa biciye ku Git LFS (Ububiko bwa dosiye nini). Raba neza ko ufise Git LFS ishizwe ku mashini yawe ukoresheje itegeko rya `git lfs install`. Ivyo bisabwa bimaze gushirwaho, uba witeguye kuja ku ntambwe ikurikira: gukuraho no gutunganya be-BOP.



**Iciyumviro:** Inyobora y'ubuhinga bwo gukoresha porogarama iraboneka mu nyigisho itandukanye.



## Gukora konti y'umuyobozi mukuru



Igihe ca mbere nyene be-BOP itanguzwa, haca hashirwaho konti ya **Super Admin**. Iyi konti irafise uburenganzira bwose busabwa kugira ngo umuntu ashobore gucunga ibikorwa vyo mu biro vy’inyuma. Kugira ngo ufungure konti, ukurikize izi ntambwe:





- Genda kuri `urubuga rwawe/umuyobozi/kwinjira`
- Rema konti y'umuyobozi mwiza cane ufise ijambobanga ry'injira ry'umutekano



Iyi konti izoguha uburenganzira bwo gukoresha ibikorwa vyose vyo mu biro vy’inyuma. Iyo imaze kuremwa, urashobora kwinjira winjiza izina ryawe n’ijambobanga ryawe.



![login](assets/fr/001.webp)



## Ibiro vy'inyuma n'umutekano



Imbere yo gutunganya uruja n'uruza rwa Interface, ukeneye gukora Hash yihariye. Ivyo bitanga uburinzi ku bakozi b’ububisha bagerageza kwiba uruja n’uruza rw’ihuriro ry’umuyobozi wawe wa Interface.



Kugira ngo ureme Hash, genda kuri `/umuyobozi/Ivyagezwe`. Mu gice kijejwe umutekano (nk'akarorero "Umuyobozi Hash"), sobanura urudodo rudasanzwe (Hash). Iyo umaze kwandikisha, URL y'ibiro vy'inyuma izohindurwa (nk'akarorero `/admin-yourhash/login`) kugira ngo abantu batarekuriwe ntibashobore kuyironka.



![hash-login](assets/fr/002.webp)



2.2. Gukoresha uburyo bwo kwitaho (niba ari ngombwa)



Naho biri muri /admin/Settings, (Ivyagezwe > Rusangiye biciye ku bishushanyo vya Interface) reba uburyo bwo "gushoboza uburyo bwo kwitaho" buri musi y'urupapuro.



![maintenance-mode](assets/fr/003.webp)



Niba bisabwe, urashobora gutanga urutonde rw’amaderesi IPv4 yemerewe (atandukanijwe n’ibimenyetso) kugira ngo ushobore gushika ku biro vy’imbere mu gihe co gusanasana. Ibiro vy’inyuma biguma bishobora gushikirwa n’abarongozi.



![ip-bebop](assets/fr/004.webp)



## Gutegura ivy'itumanaho



Kugira ngo be-BOP ishobore kohereza amatangazo (nk'akarorero ku mategeko, ukwiyandikisha canke ubutumwa bwa sisitemu), ukeneye gutunganya nibura uburyo bumwe bwo guhanahana amakuru. Hariho uburyo bubiri: ubutumwa bwo kuri e-mail (SMTP) canke Nostr.



### Itunganywa rya SMTP (imeyili)



be-BOP ishobora kohereza ubutumwa kuri serveri ya SMTP. Uzokenera ivyemezo vya SMTP vyemewe, akenshi bitangwa na serivisi ya e-mail (nk'akarorero Mailgun, Gmail, n'ibindi).



Ehe ivyo ukwiye kumenya:



SMTP_HOST: Serveri ya SMTP Address (nk'akarorero smtp.ubutumwa.org)



SMTP_PORT: icuma co gukoresha (kenshi 587 canke 465)



SMTP_USER: izina ryawe ry'ukoresha (kenshi ni imeyili Address)



SMTP_IJAMBOBAnga: ijambobanga ryawe canke urufunguzo rwa API



SMTP_FROM: imeyili Address izoboneka nk'uwuyirungitse




### Nostr gutunganya



be-BOP iragufasha kohereza amatangazo biciye ku nzira ya Nostr, ibikorwa remezo vy’ubutumwa vy’abantu bose. Kugira ngo ubikore, ukeneye generate canke Supply urufunguzo rw’ibanga rwa Nostr (NSEC). Ushobora generate uru rufunguzo ataco ukoresheje Interface ya be-BOP, mu gice cagenewe Nostr. Iyo izo Elements zitunganijwe neza, be-BOP izoshobora kwirungikira ubutumwa n’imburi ku bakoresha bawe.



## Uburyo bwo kwishura buhuye



be-BOP ihuye n’imiti myinshi yo kwishura, bikagufasha guha abakiriya bawe uburenganzira bwo guhindura ibintu. Ehe ivyo ukeneye kugira ngo ushireho uburyo bwo kwishura bubereye wewe.



### Bitcoin Ku mugozi



be-BOP iragufasha kwemera amahera ya Bitcoin ataco uhinduye kuri Blockchain (On-Chain), mu buryo bworoshe kandi butekanye.



**Intambwe zo gutunganya:**





- Genda kuri **Imiterere y'Ukwishura**
- Fyonda kuri **Bitcoin Nodeless** kugira ngo ubone amategeko y'ukwishyura On-Chain.
- Uzuza ibi bikurikira:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Impanuro:** Kugira ngo uronke urufunguzo rwawe rwa bose rwagutse (Zpub), ushobora kuraba amasetingi ateye imbere ya Bitcoin Wallet yawe (Sparrow wallet, BlueWallet, Spectre, n’ibindi). Raba neza ko Wallet yawe **itasomwa gusa** nimba ushaka gukoresha amateka y’ibikorwa.



### Lightning Network



be-BOP irashobora kandi kwemera kwishura Bitcoin ubwo nyene kubera Lightning Network. Amahitamwo abiri yo gutunganya araboneka ubu:



**Fenikisi**



Genda kuri `Imiterere y'Ukwishura`, ukande kuri `Phoenixd`



![phoenixd](assets/fr/006.webp)



Uzoca ukenera kwinjiza **ijambobanga canke ivyemezo vya token** biguhuza n’instance yawe ya Phoenixd, backend yateguwe na Acinq ishobora kugufasha gucunga amahera ya Lightning ukoresheje node yawe bwite, ariko ata ngorane zo gucunga inzira zo kwishura.



**Ubusuwisi Bitcoin bwishyura**



Niba udashaka gucunga node ya Lightning wewe nyene, **Swiss Bitcoin Pay** ni umuti witeguye gukoreshwa, woroshe gutunganya kandi ni mwiza cane wo gutangura kwemera amahera ya Lightning ata bikorwa remezo bikomeye.



Intambwe zo gutunganya:





- Mu "Imiterere y'Ukwishura", kanda kuri `Swiss Bitcoin Pay`
- Injira muri konti yawe ya Swiss Bitcoin Pay (canke uyikoreshe nimba udasanzwe ufise).
- Injira urufunguzo rwa API rwatanzwe na Swiss Bitcoin Pay, hanyuma ukande kuri "Bika".



Iyo imaze gushirwaho, be-BOP izoca itanga invoice za generate Lightning ku bakiriya bawe, kandi uzoronka amahera ataco uhinduye kuri konti yawe ya Bitcoin Pay y’Ubusuwisi. Uyu muti ni mwiza ku bakoresha bashaka kwirinda ubuhinga butoroshe bw’urudodo rw’umuntu ku giti ciwe mu gihe bemera kwishura vyihuta kandi bihenda.



![swissbtcpay](assets/fr/007.webp)



### Paypali



Uretse Bitcoin, be-BOP iragufasha kandi kwemera kwishura amahera biciye kuri PayPal, umuti uzwi cane kandi ukoreshwa cane kw’isi yose.



Intambwe zo gutunganya:





- Genda kuri `Imiterere y'Ukwishura`
- Fyonda kuri `PayPal
- Muri konti yawe ya Paypal (igice c'abahinguzi), shiramwo `Indangamuntu y'umukiriya` n'ibanga`
- Hitamwo ifaranga ukunda (nk'akarorero **USD**, **EUR**, **XOF**, n'ibindi)
- Fyonda kuri `bika



![paypal](assets/fr/008.webp)



**Iciyumviro:** Utegerezwa kuba ufise konti y’ubucuruzi ya PayPal kugira ngo generate ivyo bimenyetso. Ushobora kubironka biciye ku rubuga [rw'abahinguzi] (https://abahinguzi.paypal.com)



### Incamake



Ubu iyo porogarama irimwo umuti wo kwishura **SumUp**, bigufasha kwemera kwishura ku ikarita y’inguzanyo mu buryo bworoshe, butekanye kandi bubereye. Kugira ngo umuntu yungukire kuri iyo nzira, bisaba ko abanza gutunganya ibintu. Ehe intambwe zo gukurikira, zifise inomero kugira ngo zishirwe mu ngiro zitomoye kandi zitera imbere:





- Tangana winjiza **Urufunguzo rwawe rwa API**, urufunguzo rw'ibanga rwatanzwe na SumUp igihe wakora konti yawe y'umuhinguzi. Ishiraho ubucuti butekanye hagati ya konti yawe ya SumUp na porogarama.
- Uzuza `Kode y'Umucuruzi` n'ikode yihariye igaragaza ubucuruzi bwawe mu rubuga rwa SumUp. Iyi kode ni nkenerwa mu gufatanya amafaranga n’ubucuruzi bwawe.
- Mu kibanza ca `Ifaranga`, hitamwo ifaranga nyamukuru ukoresha mu bikorwa vyawe (nk'akarorero **EUR**, **USD**, **CDF**, n'ibindi).
- Igihe vyose vyuzuzwa neza, fyonda ku buto `Bika` kugira ngo ubike ivyo washizeho. Uwo murongo uzoca ushinga uruja n’uruza na konti yawe ya SumUp, kandi porogarama yawe izoba yiteguriye kwemera amahera.



![payment-sumup](assets/fr/009.webp)



Inyuma y’iyi ntunganyo, **SumUp** integration izoba ikora kandi ikora, biguhe uburenganzira bwo gukura amahera ningoga no gukurikirana amafaranga yawe ukoresheje porogarama.



### Umurongo



be-BOP kandi itanga ubufatanye bushitse na **Stripe**, imwe mu nzira zizwi cane zo kwishura kuri internet. Stripe iragufasha kwemera kwishura kuri internet ukoresheje ikarita y’inguzanyo, Wallet ya digitale n’ubundi buryo bwinshi bwo kwishura. Ehe ingene woyikoresha:





- Injira **urufunguzo rw'ibanga** rwatanzwe mu rubuga rwa Stripe.
- Uzuza **Urufunguzo rwa bose**, na rwo rutangwa na Stripe.
- Hitamwo **ifaranga ry'ingenzi**.
- Bika imiterere, hanyuma ukande `Bika`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Ibuka:** Ni ngombwa kumenya uburyo bwo gutanga IVA bujanye n'igikorwa cawe (nk'akarorero: ugurisha hakurikijwe IVA mu gihugu c'ugurisha, gusonerwa hakurikijwe imvo n'imvano, canke ugurisha ku rugero rw'IVA mu gihugu c'umuguzi) kugira ngo ushobore gutunganya neza uburyo bwo gutanga invoice muri **be-OP.



## Itunganywa ry'amafaranga



**be-BOP** itanga uburyo bwo gucunga amafaranga buteye imbere kandi ihuye n’ibidukikije vy’amafaranga menshi n’ibisabwa vy’ubuhinga bw’ibarabara. Kugira ngo ibikorwa vy’ivy’ubutunzi n’ugutanga raporo bibe bihuye, birahambaye ko amafaranga atandukanye akoreshwa muri iyo nzira atunganywa neza. Dore intambwe zo gukurikira kuri iyi ntunganyo:





- Hitamwo **ifaranga ry'ingenzi** (`Ifaranga ry'ingenzi`)
- Hitamwo `Ifaranga rya kabiri
- Sigura **ifaranga ry'ishingiro** (`Igiciro c'ifaranga ry'ishingiro`)
- Erekana `Ifaranga ry'Ibarabara



Amafaranga yose amaze gutunganirizwa neza, iyo porogarama ituma amafaranga menshi ahindurwa mu buryo bwihuse kandi ata co buhinduye, mu gihe nyene iguma ikora neza mu bijanye n’ivy’ibara ry’amafaranga.



![settings-currencies](assets/fr/011.webp)



## Gutunganya uburyo bwo gusubirana biciye kuri email canke Nostr



Naho uri muri `/admin/settings`, biciye ku **ARM** module, urabe neza ko konti y’umuyobozi mukuru irimwo **email Address** canke **pub yo gusubirana**, gutyo bikorohereze uburyo iyo wibagiwe ijambobanga ryawe.



![settings-users](assets/fr/012.webp)



## Imyandikire y'ururimi



Iyi porogarama itanga ubushobozi bwo kuvuga indimi nyinshi kugira ngo imenyere abantu bo kw’isi yose no kwongereza ubumenyi bw’abayikoresha. Kugira ngo ukoreshe indimi nyinshi, birahambaye ko utunganya indimi ziriho no gusobanura **ururimi rwa mbere**.



![settings-languages](assets/fr/13.webp)



## Interface n'imiterere y'akaranga muri be-BOP



**be-BOP** itanga abahinguzi b’urubuga ibikoresho vyose bakeneye kugira ngo bashobore guhingura urubuga. Intambwe ya mbere ni ugufungura igice ca `/Umuyobozi > Ibicuruzwa > Imiterere` mu mitunganyirize. Tangana n'ugutunganya **Umurongo wo hejuru**, **Umurongo wo kugenda** na **Umurongo wo hasi**.



### Le Top Bar



**Top Bar** iragufasha guhindura akaranga ka porogaramu yawe mu kugaragaza amakuru y'ingenzi kuva ku murongo wa mbere wa Interface. Ivyo bikomeza kwemerwa kw’ibara kandi bikaba bitanga ikibanza gitomoye ku bakoresha.



#### Intambwe zo gutunganya:





- Mu kibanza `Izina ry'ikigo`, shiramwo izina ry'ishirahamwe ryawe, ishirahamwe canke igicuruzwa. Iri zina rizoboneka hejuru y’igitabu ca Interface kandi rizoserukira akaranga kawe nyamukuru k’ivyo ubona.
- Erekana umutwe w’urubuga**: umutwe watowe ukwiye kuvuga mu ncamake intumbero y’urubuga. Uwo mutwe ushobora kuboneka mu mutwe canke mu gice c’umucukumbuzi.
- Yongerako insobanuro y’urubuga**: aha niho winjiza insobanuro ngufi y’umugambi wawe. Iyi ndondoro ifasha gushiramwo igikoresho ku bakoresha kandi ishobora no gukoreshwa ku ntumbero za SEO.



Aya makuru amaze kwinjira, **Top Bar** izokwerekana uburyo butomoye, bw’umwuga kandi buhuye bw’umuti wawe.



#### Amahuza ari mu murongo wo hejuru



Igice ca `Amahuza` co ku Murongo wo Hejuru kigufasha kwongerako inzira ngufi ku mapaji ahambaye mu gikorwa cawe canke ku mbuga zo hanze. Aya mahuza yerekanwa mu buryo butaziguye mu Murongo wo Hejuru, agaha abakoresha bawe uburenganzira bwo kuronka ivyo bintu vyihuta kandi bitunganijwe.



#### Intambwe zo gutunganya:





- Injira izina ry'ihuriro (Ivyanditswe)**: mu mwanya `Ivyanditswe`, shiramwo izina canke ikimenyetso c'ihuriro uko rizoboneka (nk'akarorero Inzu, Uwo guhamagara, Imfashanyo...).
- Erekana ihuriro Address (Url)**: mu mwanya wa `Url`, shiramwo Address yuzuye ya paji y'intumbero (imbere canke hanze).
- Yongerako ayandi mahuza nimba bikenewe**: umurongo wose w'imiterere ushobora kugufasha kwongerako iyindi mahuza ukoresheje `Ivyanditswe` na `Url`.
- Bika amahuza**: amahuza yose amaze kwinjira, ukande kuri buto ya "Ongera amahuza yo hejuru" kugira ngo uyabike.



Iyi ntunganyo iragufasha gutanga uburyo butomoye, bugenda neza kandi bushoboka biciye mu bice bitandukanye vy’urubuga rwawe canke mu bikoresho vy’inyongera.



![settings-topbar](assets/fr/014.webp)



### Ibarabara rya La Nav



Igice ca **Navbar** kigufasha gutunganya urutonde rw'ibintu vy'ingenzi vya be-BOP yawe, akenshi biri ku ruhande canke hejuru ya Interface. Iyi menyu iyobora abakoresha ku mapaji atandukanye y’iyi porogarama n’ibikorwa vyayo. Gutunganya amahuza ni vyoroshe kandi birashoboka. Ehe uko bigenda:





- Injira izina ry'ihuriro (`Ivyanditswe`): ku murongo w'imiterere, tangura wuzuze `Ivyanditswe` umwanya. Ivyo bihuye n’izina ry’ihuriro ryerekanywe mu murongo w’ivy’ugugenderamwo (ingero: *Dashboard*, *Abakoresha*, *Ivyagezwe*...).
- Injira ihuriro Address (`Url`): iruhande y'umwanya `Ivyanditswe`, uzosanga umwanya `Url`. Muri iki kibanza, shiramwo Address y’urupapuro iyo nzira ikwiye kujako. Ivyo bishobora kuba inzira yo mu mutima canke uruja n'uruza rw'inyuma.
- Yongerako amahuza menshi nimba bisabwa**: munsi y'umurongo wa mbere, hariho ivyicaro bishasha `Ivyanditswe` na `Url` vyo kwongerako amahuza menshi nk'uko bisabwa. Umurongo wose ugereranya uruja n’uruza rw’inyongera rwo kugenderamwo.
- Bika amahuzu**: umaze kwinjiza Elements zose, ukande kuri buto ya `Add nav bar link` kugira ngo ubike kandi ugaragaze ibisubizo mu murongo w'urugendo.



Ivyo bituma habaho ugutunganya neza uburyo bwo gushika ku bice bitandukanye vya porogarama, bigatuma umuntu ashobora gukoresha neza ubuhinga bwo gukora neza.



![navbar](assets/fr/015.webp)



### Ikirenge



Igice ca **Footer** kigufasha guhindura footer ya porogaramu yawe, ukongerako amakuru ngirakamaro canke amahuza. Mbere yo gutunganya amahuza, tangura ukoresheje uburyo bwihariye:





- Gushoboza kwerekana ikimenyetso "Ikoreshwa na be-BOP": gukoresha buto ya `Iyerekanwa Ikoreshwa na be-BOP` kugira ngo ugaragaze iki kimenyetso mu gice co hasi.
- Injira izina ry'ihuriro (**Ivyanditswe**): wuzuze ahantu **Ivyanditswe**, bihuye n'amajambo y'ihuriro ari mu gice co hasi (ingero: *Amabwirizwa*, *Ibanga*, *Umuntu*...).
- Erekana ihuriro Address (`Url`): mu mwanya wa `Url`, shiramwo Address ya paji y'intumbero (imbere canke hanze).
- Yongerako ayandi mahuza nimba bisabwa**: koresha imirongo y'inyongera kugira ngo ureme amahuza menshi uko ushaka.
- Bika amahuza**: fyonda ku buto "Ongera amahuza y'inyuma" kugira ngo ubike amahuza.



![footer](assets/fr/016.webp)



### Guhindura umuntu ku giti ciwe



**⚠️ Ntimwibagire gushinga ibimenyetso vy'insanganyamatsiko z'umuco n'umwiza, hamwe n'ikimenyetso ca favicon, biciye kuri** `Admin > Ibicuruzwa > Amafoto`.



Ehe ingene wohindura ukuntu urubuga rwawe rusa n'uko rumeze:



#### Genda mu gice c'amafoto



Ububiko `Umuyobozi` > `Ibicuruzwa` > `Amafoto`.



#### Kwongerako ishusho nshasha



Fyonda kuri `Ishusho nshasha`.



#### Hitamwo dosiye yo mu karere



Fyonda kuri `Hitamwo amadosiye`, hanyuma uhitemwo ishusho kuri disiki yawe ya Hard.



#### Hitamwo dosiye yo kwinjiza



Fyonda kabiri ku ishusho uzozana (ikimenyetso c’umuco, ikimenyetso c’umwiza canke favicon).



#### Kwita ishusho izina



Uzuza `Izina ry'ishusho` umwanya.



#### Kwongera ishusho



Fyonda `Ongera` kugira ngo uheze kwinjiza.



![pictures](assets/fr/017.webp)



### Gutegura akaranga k'umugurisha



#### Amagenamiterere y'akaranga



Ushobora kuronka amakuru y'uburongozi n'amategeko y'ishirahamwe ryawe.



#### Amakuru y'amategeko





- Izina ry'ubucuruzi**: izina ry'ishirahamwe ryemewe.
- Indangamuntu y’ubucuruzi**: ikimenyetso c’ubucuruzi canke inomero y’iyandikwa (RCCM, SIRET...).



#### Ubucuruzi Address





- Ibarabara**: iposita Address (ibarabara, inomero...).
- Igihugu**: igihugu.
- Leta**: intara canke akarere.
- Igisagara**: igisagara.
- Kode ya ZIP**: kode ya posita.



#### Amakuru yo guhamagara





- Imeli**: imeli y'umwuga Address.
- Telefone**: inomero ya telefone y’ishirahamwe.



#### Konti ya banki





- Izina ry'uwufise konti**: izina ry'uwufise konti.
- Uwufise konti Address**: Address y'uwufise.
- IBAN**: Inomero ya Konti ya Banki Mpuzamakungu.
- BIC**: Kode y'IKIMENYETSO/BIC.



![bank-account](assets/fr/019.webp)



#### Gutanga amafaranga





- Fyonda kuri `Uzuza amakuru y'iduka ry'ingenzi` kugira ngo wuzuze amakuru.
- Amakuru y'uwutanga amakuru yo hejuru cane**: umwanya w'amakuru y'amategeko/imisoro aboneka ku mafagitire.
- Fyonda `Update` kugira ngo ubike ivyo wahinduye.



**Iciyumviro:** ushobora kandi kwinjiza amakuru y’inyongera azogaragazwa kuri Invoice, bivanye n’ivyo ukeneye.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Iduka ry'umubiri Address



Ku bafise ububiko bw’umubiri, wongereko Address yuzuye mu `Umuyobozi > Amategeko > Indangamuntu` canke igice kigenewe. Ivyo bizotuma ishobora kugaragara ku nyandiko zizwi no mu gice co hasi iyo bikenewe.



![seller-id](assets/fr/021.webp)



## Ubuyobozi bw'ibicuruzwa



### Guhingura igicuruzwa gishasha



Genda kuri `Umuyobozi > Ibicuruzwa > Ibicuruzwa` kugira ngo wongereko canke uhindure igicuruzwa. Uzuza ibi bikurikira:



#### Amakuru y'ishimikiro





- Izina ry'igicuruzwa**: izina ry'igicuruzwa (nk'akarorero *T-shirt ya BOP ishobora gukoreshwa mu buryo buke*).
- Slug**: Indangamuntu ya URL ata myanya (nk'akarorero `ishati-bop-igitabu-gifise umupaka`).
- Alias** *(ntibikenewe)*: ni ngirakamaro mu kwongera vuba ku giseke biciye mu murima wihariye.



![product-config](assets/fr/028.webp)



#### Ibiciro





- Igiciro**: igiciro c'igicuruzwa (nk'akarorero `25.00`).
- Igiciro Amafaranga**: amafaranga (EUR, USD, BTC, n’ibindi).
- Ibintu bidasanzwe**:
  - iki ni igicuruzwa c’ubuntu.
  - iki ni igicuruzwa co kwishura ivyo ushaka.



#### Amahitamwo y'ibicuruzwa





- Igicuruzwa kimwe (`kigenga`)**: kwongerako kimwe gusa gishoboka ku bijanye n'itegeko (nk'akarorero, intererano, itike yo kwinjira).
- Igicuruzwa gifise ubudasa**:
  - Ntusuzume `Ihagaze`.
  - Suzuma `Igicuruzwa gifise ubudasa buke (nta tandukaniro ry'ububiko)`.
  - Kongerako:
- Izina** (nk'akarorero *Ingano*),
- Agaciro** (nk'akarorero: S, M, L, XL),
- Ibiciro bitandukanye** nimba bishoboka (nk'akarorero: `+2 USD` kuri XL).



![product-details](assets/fr/029.webp)



## Ubucungezi bw'ububiko



### Amahitamwo ateye imbere igihe urema igicuruzwa (Ibikoresho, Gushikana, Amatike, n'ibindi)



#### Igicuruzwa gifise ububiko buke



Niba igicuruzwa cawe kitaboneka mu bwinshi butagira aho bugarukira, reba `Igicuruzwa gifise ububiko buke`. Ivyo bituma habaho ugukurikirana kw’ibintu bisigaye. Iyo aka gasandugu kashizweko akamenyetso, umwanya uraboneka werekana **ibintu biriho**.



Ubuhinga buracungera:





- Ibintu vyabitswe** → ibintu biri mu biseke bitarahembwa
- Ibintu vyagurishijwe** → ibintu vyaramaze kugurwa



**Igihe co kubika igiseke**: Iyo umukiriya yongeyeko igicuruzwa mu giseke ciwe, "kibikwa" igihe gito. Ushobora guhindura iki gihe muri: `Umuyobozi > Itunganywa > Gucungera igare` (agaciro mu minota)



#### Igicuruzwa kizoshikirizwa?



Suzuma `Igicuruzwa gifise igice c'umubiri kizorungikwa ku Address y'umukiriya`. Ivyo ni ngirakamaro ku bicuruzwa vyose vyoherezwa mu buryo bw’umubiri (ibitabu, ama-t-shirt, n’ibindi)



#### Ayandi mahitamwo





- Tike**: shira akamenyetso nimba igicuruzwa ari itike y'umusi mukuru
- Gufata umwanya**: reba nimba aha ari ahantu ho gufata umwanya (nk'akarorero: igihe, umubonano)



![product-options](assets/fr/030.webp)



### Amagenamiterere y'ibikorwa (hasi)



Iki gice kigena **aho** n'ingene** igicuruzwa gishobora kurabwa no kugurwa:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Suzuma gusa imirongo wipfuza gukoresha.



## Guhingura no guhindura uko ushaka amapaji ya CMS n'ibikoresho



### Paje za CMS zitegekanijwe



Genda kuri `Umuyobozi > Ibicuruzwa > CMS`. Uzobona urutonde rw'amapaji asanzweho kandi ushobora kwongerako ayandi mashasha ukoresheje **Ongera paji ya CMS**.



Paje za CMS ni ngirakamaro kuri:





- Menyesha abashitsi bawe (nk'akarorero amabwirizwa y'ikoreshwa)
- Kubahiriza itegeko (nk'akarorero politike y'ubuzima bwite)
- Sigura ibiranga ububiko bumwe bumwe (nk'akarorero IP, 0% IVA)



Ushobora kwongerako izindi paji nk'uko bisabwa:





- Ivyacu / Abo turi
- Mudushigikire / Intererano
- IBIBAZO bibazwa
- Guhanahana amakuru
- n'ibindi.



**Impanuro: Fyonda kuri buri nzira canke icon kugira ngo uhindure ibirimwo, umutwe, canke ukuntu seo igaragara kuri buri paji.**



### Ubuhinga n'igishushanyo Elements



Genda kuri: `Umuyobozi > Ibicuruzwa > Imiterere`. Ushobora guhindura Elements y'urubuga rwawe:



![product-options](assets/fr/032.webp)



#### Ibarabara ryo hejuru





- Guhindura canke gukuraho amahuza (EX: INZO, IVYACU,...)
- Kugendagenda hagati y'ibice nyamukuru vy'urubuga



#### Navbar (umurongo nyamukuru wo kugenderamwo)





- Iboneka mu karere k'umweru kari munsi y'umurongo wo hejuru
- Birimwo ukwinjira vuba kuri: `Itunganywa`, `Imiterere y'Ukwishura`, `Imigenderanire`, `Uburongozi bw'Imirongo`, `Ibikoresho`, n'ibindi.
- Abarongozi gusa



#### Hasi





- Bishobora guhindurwa bivuye kuri `Umuyobozi > Ibicuruzwa > Imiterere`
- Birimwo: amakuru yo guhamagara, amahuza ngirakamaro, amatangazo y'amategeko..



#### Guhindura amashusho



Genda kuri: `Umuyobozi > Ibicuruzwa > Amafoto`



Urashobora:





- Guhindura **ikimenyetso nyamukuru**
- Guhindura canke wongereko imiterere **amashusho**



#### Insobanuro y'urubuga



Ishobora kandi guhindurwa mu `Amashusho`, ishobora kugaragaza **incamake canke insiguro** mu mutwe canke mu mpera, bivanye n'insanganyamatsiko.



**Iciyumviro:** ivyo bigufasha guhindura ukuntu usa n’akaranga k’ibara ryawe (ivy’inyigisho, ivy’ubudandaji canke ivy’abanyagihugu).



### Kwinjiza ibikoresho muri paji za CMS



**Ibikoresho** bitunganya amapaji yawe ya CMS n'inguvu canke amashusho Elements.



#### Guhingura ibikoresho



Genda kuri: `Umuyobozi > Ibikoresho`



Ingero z'ibikoresho biriho:





- Ingorane**: ingorane canke ubutumwa
- Tags**: ivyiciro canke amajambo y'ingenzi
- Ivyerekanwa**: amashusho y'ibinyabuzima
- Ibisobanuro**: Imbonerahamwe z'ibisobanuro
- Amafishi**: amafishi (uguhamagara, inyishu, n'ibindi)
- Guharura**: ibihe
- Amabarabara**: amabarabara y'amashusho
- Imbonerahamwe**: urutonde rw'abakoresha



![widgets](assets/fr/033.webp)



#### Kwinjira muri paji za CMS



Koresha **amakode magufi** mu birimwo kuri paji zawe za CMS:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Ivyagezwe ubu**:





- `slug`: ikimenyetso c'igikoresho kidasanzwe
- `igaragaza=img-1`: ishusho yihariye y'igicuruzwa
- `ubwaguke`, `uburebure`, `uburinganire`: ishusho ingano n'imiterere
- kwikina=3000`: igihe mu ms hagati y'ibice bibiri



**Ivyiza**:





- Biroroshe kwinjiza (gukopa no gushiramwo)
- Impinduka: ihinduka ryose ku gikoresho rihita rigaragara
- Nta muhinguzi asabwa



## Uburongozi bw'amategeko no gutanga raporo



### Gukurikirana amategeko



Kugira ngo ubone kandi ucunge amategeko ya kera, genda kuri: `Umuyobozi > Ibikorwa > Amategeko`



Aha uzosanga **urutonde rw'amategeko yose** yashizwe ku rubuga rwawe.



![orders](assets/fr/034.webp)



#### Gushushanya n'ugushakashaka



Interface iragufasha kurondera no kuyungurura amategeko hakurikijwe ingingo nyinshi:





- Umubare w'itegeko: umubare w'itegeko
- izina ry'igicuruzwa: ikimenyetso c'igicuruzwa canke izina
- kwishura Bisobanuro": uburyo bwo kwishura bukoreshwa (ikarita, crypto, n'ibindi)
- `Imeyili`: imeyili y'umukiriya



Izo nyunguruzo zifasha gushakisha vyihuse no gucunga neza.



#### Ibisobanuro vy'itegeko ryose



Mu gufyonda ku rutonde, ushobora kuronka dosiye yuzuye irimwo:





- Ibintu vyasabwe
- Amakuru y'abaguzi
- Gushikana Address (niba bishoboka)
- Ivyanditswe vyose bijanye n'itegeko



#### Ibikorwa bishoboka kuri itegeko



Urashobora:





- Wemeze itegeko (niba ritegerejwe)
- Gukuraho itegeko (mu gihe habaye ingorane canke ibisabwa n'umukiriya)
- Yongerako **ibimenyetso** (kubera imitunganirize yo mu mutima)
- Raba / wongereko **ibisobanuro vyo mu mutima**



**Iciyumviro:** iki gice ni ngombwa kugira ngo habeho neza ivy'ubuhinga n'imigenderanire n'abaguzi.



### Gutanga raporo no kwohereza hanze



Kugira ngo ubone imibare y'ugurisha n'ugutanga:


umuyobozi > Amagenamiterere > Gutanga raporo



![reporting](assets/fr/035.webp)



Aha uzosanga icegeranyo c'ubucuruzi bwawe, mu buryo bwa **raporo z'ukwezi n'iz'umwaka**.



#### Raporo y'ibirimwo



Izo raporo zigabanywemwo ibice:





- Ibisobanuro vy'amategeko**: umubare w'amategeko, ikibanza (vyemejwe, vyasubiwemwo, birindiriwe), iterambere
- Ibisobanuro vy'ibicuruzwa**: ibicuruzwa vyagurishijwe, ubwinshi, ibicuruzwa bikundwa
- Ivyerekeye kwishura**: amafaranga yashizwe hamwe, agabanywa hakurikijwe uburyo bwo kwishura



#### Ukwohereza amakuru hanze



Buri gice gifise ubuto **Export CSV**, bushobora kugufasha:





- Gukuraho amakuru mu buryo bwa CSV
- Bifungure muri Excel, impapuro za Google, n'ibindi.
- Ububiko bwo gukoresha mu butegetsi canke mu vy'ubuhinga
- Bikoreshe kuri raporo zo mu mutima



**Iciyumviro:** ni vyiza ku gukurikirana ibikorwa, guharura no gutanga ibiganiro.



## Nostr Ubutumwa bwo gutunganya (ubusabe)



![nostr-config](assets/fr/036.webp)



Urubuga rushigikira **Nostr** porotokole ku bikorwa bimwe bimwe biteye imbere:





- Amatangazo yegerejwe
- Injira ata jambobanga
- Interface ubuyobozi bw'umuco



### Guhingura no kwongerako urufunguzo rwihariye rwa Nostr



Genda kuri:


umuyobozi > Ubuyobozi bw'inzira > Nostr





- Fyonda kuri **Rema nsec** nimba udafise.
- Uwo murongo urashobora generate ubwo nyene.
- Canke, ushobora gukoresha urufunguzo ruriho (nk'akarorero ruvuye kuri Damus canke Amethyst).



Igikurikira:





- Kopa urufunguzo rwa `nsec`
- Wongere kuri dosiye yawe `.env.local` (canke `.env`): ``` env NOSTR_URUPFUZO_RW'IBANGA=Urufunguzo rwawe rwaNsecIci



### Ibirango vyakoreshejwe na Nostr



Iyo bimaze gutunganirizwa, ibikorwa vyinshi biraboneka:



**Imenyekanisha biciye kuri Nostr**





- Wohereze imburi ku mategeko, kwishura canke ibikorwa vya sisitemu
- Ku barongozi canke abakoresha



**Ubuyobozi bw'umuco Interface**





- Bishobora kuronka biciye ku mukiriya wa Nostr
- Bishoboza gucungera vyihuta, bikoreshwa kuri telefone ngendanwa



**Uguhuza ata jambobanga**





- Injira ku nzira itekanye (yoherejwe kuri Nostr)
- Umutekano mwinshi w'abakoresha n'uguhinduka



## Guhingura no guhindura insanganyamatsiko



Kugira ngo uhindure ubusabe bw'iduka ryawe n'igitabu cawe c'ibishushanyo, genda kuri: `Umuyobozi > Ibicuruzwa > Insiguro`



Aha uzosanga amahitamwo yose yo **guhingura** no **gutunganya** insanganyamatsiko y'umuntu ku giti ciwe.



### Guhingura insanganyamatsiko



![theme](assets/fr/037.webp)



Igihe urema canke uhindura insanganyamatsiko, ushobora gusobanura:





- Amabara**: ku buto, inyuma, umwandiko, amahuza, n'ibindi.
- Imyandikire**: uguhitamwo imyandikire y'imitwe, ibice, ibikubiyemo
- Uburyo bw'ibishushanyo**: imbibe, impande, ikibanza, imiterere y'amabuye



### Ibice bishobora guhindurwa



Igice cose c'urubuga gishobora guhindurwa kigizwe n'ibintu:





- Umutwe**: umurongo wo hejuru wo kugenderamwo
- Umubiri**: ibirimwo nyamukuru
- Insi**: hasi kuri paji



**Iciyumviro:** ubu buhinga buratuma habaho uguhuza hagati y'ibishushanyo vy'urubuga n'akaranga k'ikimenyetso cawe.



### Gukora kw'insanganyamatsiko



Igihe insiguro imaze gutunganirizwa:





- Fyonda kuri **Bika**
- Bikoreshe nk'iduka **insanganyamatsiko nyamukuru**



**Iciyumviro:** insiguro ikora ni iyo izoboneka ku bashitsi.



## Gutunganya ibigereranyo vya imeyili



Iryo koraniro rituma ushobora guhindura uko ushaka ama email yoherezwa ku bakoresha. Genda kuri: `Umuyobozi > Amagenamiterere > Ivyitegererezo`



![emails-templates](assets/fr/038.webp)



### Gukora / guhindura ibigereranyo



Imeli yose (kwemeza itegeko, ijambobanga ryibagiwe, n'ibindi) ifise:





- Insiguro**: insiguro y'imeli (nk'akarorero "Itegeko ryawe ryemejwe")
- Umubiri wa HTML**: Ibiri muri HTML vyerekanywe muri imeyili



**Iciyumviro:** ushobora kwinjiza umwandiko, amashusho, amahuzu, n'ibindi, nk'uko bisabwa.



### Gukoresha ibihinduka



Kugira ngo imeyili zibe zihinduka, shiramwo ibihinduka nka:





- `{Igitigiri c'Itegeko}}`: gisubirijwe n'Igitigiri c'Itegeko nyaco
- `{Ihuza ry'inyemezabuguzi}}`: ihuza kuri Invoice
- `{urubuga}}`: URL y'urubuga rwawe



**Iciyumviro:** izo tags zica zisubirizwa iyo zirungitswe.



### Impanuro ziteye imbere





- Rema imeyili **zisubiza** kugira ngo usome neza ku bikoresho vy'amaboko
- Yongerako **amabuto y'ibikorwa** (kwishura, gukuraho, gukurikirana urutonde)
- Gerageza ama email yawe mu kuyarungikira wewe nyene imbere y'uko asohoka



## Gutunganya ibimenyetso vyihariye n'ibikoresho



### Ubuyobozi bw'inyandiko



Ama tags ashobora gukoreshwa mu gutunganya no gutunganya ibirimwo. Kugira ngo ubironke: `Umuyobozi > Ibikoresho > Ikimenyetso`



![tags-config](assets/fr/039.webp)



### Gukora ikimenyetso



Uzuza ibi bikurikira:





- Izina ry'ikimenyetso**: izina ry'ikimenyetso ryagaragajwe
- Slug**: ikimenyetso kidasanzwe (nta myanya canke inyuguti)
- Umuryango w'ibimenyetso**: amatsinda y'ibimenyetso hakurikijwe urwego



![targsconfig](assets/fr/040.webp)



#### Imiryango iboneka:





- abahinguzi`: abanditsi canke abahinguzi
- abagurisha: abagurisha canke aho bagurisha
- `Igihe`: ibihe canke amatariki
- Ivyabaye: ivyabaye bifitaniye isano



### Ibibanza vy'amahitamwo



Ibi bibanza bishobora gukoreshwa mu gutunganya ikimenyetso nk'aho yoba ari paji y'ibirimwo:





- Umutwe
- Insiguro
- Bigufi** ibirimwo
- Ibirimwo vyose** (mu gifaransa)
- CTAs** (amabuto y'ibikorwa)



### Gukoresha ibimenyetso



Ama tags ashobora kuba:





- Bigenewe ibicuruzwa
- Yinjijwe muri paji za CMS n'ikimenyetso: [Ikimenyetso=slug?iyerekanwa=var-1]



## Kugena amadosiye ashobora gukurwako



Gutanga inyandiko zishobora gukurwa ku bakiriya bawe: `Umuyobozi > Ibicuruzwa > Amadosiye`



### Kwongera dosiye



1. Fyonda kuri **Dosiye nshasha**


2. Kumenyesha:




- Izina rya dosiye** (nk'akarorero *Inyigisho yo gushiramwo*)
- Dosiye yo gushiramwo** (PDF, ishusho, Ijambo...)



**Iciyumviro:** iyo yongeweko, urubuga ruca rutanga **ihuriro rihoraho**.



### Gukoresha ihuriro



Iyi nzira ishobora rero kwinjizwa muri:





- CMS** urupapuro (nk'ihuriro ry'inyandiko canke ubuto)
- **Umukiriya w'iposita** (biciye ku citegererezo)
- **Urupapuro rw'igicuruzwa** (nk'akarorero gukuraho n'amaboko)



Ni vyiza cane mu gutanga *ibitabo vy'abakoresha, ubuyobozi bw'ubuhinga, amakete y'ibicuruzwa...* ataco ukeneye kwakira abashitsi bo hanze.



## Nostr-robo



Iryo koraniro ritanga ubufatanye buteye imbere n’umurongo wa **Nostr**, biciye ku gikoresho citwa bot.



Genda kuri: Ubuyobozi bw'uruzitiro > Nostr



### Ibirango nyamukuru



#### Ubuyobozi bwo guhanahana





- Yongerako canke ukureho **relays** zikoreshwa na bot
- Gutuma ubutumwa bwoherejwe bushika ku bantu no kwizigirwa



#### Ubutumwa bw'intangamarara bwikora





- Gukoresha ubutumwa bwihuta ku **ugukorana kwa mbere kw'ukoresha**
- Ivyiza kuri:
  - Gutanga umurimo wawe
  - Wohereze ihuriro ry'ingirakamaro (nk'akarorero ibibazo bibazwa, guhamagara, gusaba)



#### Icemezo ca `npub yawe





- Wongereko **ikimenyetso** n'izina rya bose**
- Ihuza ku **urubuga rwagenzuwe**
- Yongera kwizerwa n'ukwemerwa kw'akaranga kawe ka Nostr



### Ibibazo vy'ikoreshwa rya Nostr-bot





- Kugurungikira **ivyemezo vy'amategeko**
- Inyishu yihuta ku **ivyabaye (nk'akarorero urutonde rushasha)**
- Gukora **ugukorana n'abaguzi kwegerejwe**



## Gushiramwo cane ubuhinduzi



be-BOP ni indimi nyinshi (FR, EN, ES...), ariko urashobora guhindura ubuhinduzi bujanye n’ivyo ukeneye.



Kugira ngo ubikore, genda kuri: `Ivyagezwe > Ururimi`



### Gushiramwo no guhindura



Amadosiye y'ubuhinduzi ari muri JSON. Urashobora:





- Gukuraho **amadosiye y'ururimi**
- Guhindura** ivyanditswe biriho
- Wongereko **ubuhinduzi bwawe bwite**



Ihuza n'amadosiye y'umwimerere:


[ubuhinduzi](ubuhinduzi](ubuhinduzi]



**Akarorero:** subiriza `Ongera ku igare` na `Umufasha` canke `Umufasha`.



## Gukorana n'abandi n'aho bagurisha (POS)



### Ubuyobozi bw'uburenganzira bw'ukoresha n'uburyo bwo kuronka



#### Guhingura uruhara



Genda kuri: `Umuyobozi > Amagenamiterere > ARM`



Fyonda kuri **Rema uruhara** kugira ngo ureme uruhara (nk'akarorero `Umuyobozi Mukuru`, `POS`, `Umugenzuzi w'amatike`).



Uruhara rwose rurimwo:





- kwandika uburenganzira**: kwandika uburenganzira
- gusoma uburenganzira**: gusoma uburenganzira
- Ukwinjira bibujijwe**: ibice biri hagati



#### Irema ry'ukoresha



Muri iyo menyu nyene `Umuyobozi > Amagenamiterere > ARM`, wongeremwo umukoresha afise:





- kwinjira
- izina
- gusubiza imeyili
- (Ihitamwo) `gusubiza npub` ku guhuza biciye kuri Nostr



Gutanga uruhara rwasobanuwe mbere.



![pos-users](assets/fr/045.webp)



**Abakoresha basoma gusa** bazobona menus ziri mu *italic* kandi ntibazoshobora guhindura ibirimwo.



## Igikoresho co kugurisha (POS) imiterere



### Gutanga uruhara rwa POS



Kugira ngo uhe umukoresha uburenganzira bwo gukoresha POS, ushire uruhara `Ikibanza co kugurisha (POS)` muri: `Umuyobozi > Config > ARM`



Ashobora kwihuza biciye kuri URL itekanye: `/pos` canke `/pos/kora`



### Ibirango vyihariye vya POS



Be-BOP itanga Interface yihariye ku kugurisha ibintu (iduka, ibirori, n’ibindi).



#### Kwongera vuba biciye ku izina ry'ibanga



Mu `/cart`, umwanya ushobora kuguha uburenganzira bwo kwongerako igicuruzwa:





- Mu gucapura **kode y'umurongo** (ISBN, EAN13)
- Mu kwinjiza **izina ry'igicuruzwa** n'amaboko



**Iciyumviro:** igicuruzwa kica kija mu giseke.



#### Uburyo bwo kwishura



POS irashigikira:





- Ubwoko
- Ikarata y'inguzanyo
- Lightning Network (ibanga)
- Abandi bivanye n'imiterere



Amahitamwo abiri ateye imbere araboneka:





- Gusonerwa IVA**: bikoreshwa ku mvo (imiryango itegamiye kuri Leta, abanyamahanga...)
- Igabanuka ry'ingabirano**: igabanuka ridasanzwe n'ibitekerezo vy'ingorane



#### Igaragaza ku ruhande rw'umukiriya



URL `/pos/igihe` igenewe **igicapo ca kabiri** (HDMI, igikoresho...):



Icapa:





- Ibicuruzwa biriko birategurwa
- Umubare wose hamwe
- Uburyo bwo kwishura
- Ibiciro vyagabanutse vyakoreshejwe



**Iciyumviro:** umukiriya akurikira itegeko ry'ubuzima, mu gihe uwugurisha arindika kuri `/pos`.



### Incamake ya POS



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Murakoze gukurikira neza iyi nyigisho.