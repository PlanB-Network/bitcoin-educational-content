---
name: ThunderHub
description: Interface Urubuga rwo gucunga urudodo rw'umuravyo LND.
---
![cover](assets/cover.webp)



## Imenyekanisha



ThunderHub ni **umuyobozi w’inkomoko yuguruye w’ibice vy’umuravyo (LND)**, itanga Interface ishobora gukoreshwa n’igikoresho cose canke umucukumbuzi.



**Ibiranga cane:**




- Gukurikirana**: Imbonerahamwe y'isi yose y'imibare, imirongo, amafaranga, imibare y'inzira
- Ubuyobozi**: Gufungura/funga imihora, kwishura/gusohoka, guhuza imihora
- Inyungu**: LNURL infashanyo, guhindura biciye kuri Boltz, Amboss ububiko
- Interface yishuye**: Ihuye n'ibikoresho vy'amatelefone ngendanwa, ibikoresho vy'amaboko n'ibikoresho vy'ibiro bifise insasanuro z'umwiza/umuco



ThunderHub ifatanya mu buryo bworoshe na **Umutaka**, **Inguvu**, **RaspiBlitz** na **MyNode**, bikorohereza uburongozi bwa misi yose bw'uruzitiro rwawe.



**ThunderHub irabereye cane cane abakoresha barondera Interface ikora neza kugira ngo bashobore gucunga imihora yabo, kugenzura amafaranga (rebalancing), kugenzura amafaranga no gushiramwo ibikorwa vy’abandi nka Amboss. Umutekano uremezwa biciye ku nzira yo mu karere canke Tor.**



Niba utaragira urudodo rw'umuravyo, turagusavye gukurikiza inyigisho yacu ya LND Umbrel:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Gushiramwo



ThunderHub ishobora gushirwa mu buryo butandukanye, bivanye n’aho ukoresha Lightning node. Waba ukoresha umuti w’urufunguzo (Umutaka, Inguvu, RaspiBlitz, MyNode, Start9, n’ibindi) canke gushiramwo n’amaboko, ThunderHub akenshi iraboneka ata nguvu nyinshi. Aha hepfo, turadondora uburyo bubiri busanzwe: biciye ku Umbrel App Store, no biciye ku gushiramwo n’amaboko (bikoreshwa kuri server canke ku gukwiragiza kwikorera).



### Gushiramwo biciye ku Mutaka



Umbrel ishiramwo ThunderHub mu **App Store** yayo, bituma gushiramwo vyoroha cane. Nta nkenerwa y’umurongo w’amabwirizwa canke gutunganya n’amaboko: vyose bikorwa biciye ku Interface Umbrel. Kurikiza gusa izi ntambwe:





- Gufungura urupapuro rwa Umbrel**: Huza n'urubuga rwa Interface rw'uruzitiro rwawe rwa Umbrel (nk'akarorero `http://umbrel.local` ku rubuga rwawe rwo mu karere, canke biciye kuri `.onion` Address nimba uriko urakoresha Tor).
- Ushobora gushika ku iduka ry'amaporogarama**: Mu rutonde rwa Umbrel, fyonda ku "Iduka ry'amaporogarama" (canke "Iporogarama"). Rondera **ThunderHub** mu rutonde rw'ibikoresho biriho.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- Gushiramwo ThunderHub**: Fyonda kuri porogarama ya ThunderHub, hanyuma ukande kuri buto yo gushiramwo. Wemeze nimba ari ngombwa. Umbrel izokwikurako maze ikoreshe ThunderHub ku nzira yawe.





- Gutanguza porogaramu**: Iyo gushiramwo birangiye (amasegonda mirongo make), ThunderHub iraboneka kuri paji yawe y’intango. Fyonda kuri iyo kimenyetso kugira ngo uyifungure. ThunderHub itanguye mu mucukumbuzi wawe.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Igihambaye:** Iyo ThunderHub ifunguwe ubwa mbere, ihita yerekana **ijambobanga ry'imbere** rikenewe kugira ngo winjire. **Turaguhanura cane ngo:**




- Bika iri jambobanga ubwo nyene** mu mucungerezi w'ijambobanga ryawe
- Kopa **kugira ngo ukoreshe mu ntambwe ikurikira**
- Suzuma "Ntusubire kwerekana ibi" ijambobanga rimaze kubikwa



![Page de connexion de ThunderHub](assets/fr/03.webp)



Uzoca uja kuri paji yo kwinjira, aho utegerezwa kwinjiza ijambobanga wakopiye mu ntambwe ya mbere kugira ngo ufungure Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel yitwararika gutanga ThunderHub n’amakuru y’ihuriro rya LND (icemezo ca TLS, macaroon y’ubuyobozi, n’ibindi) mu nyuma, rero ntukeneye gukora ibindi bikoresho vy’inyongera. Mu gukanda guke gusa, uzoba ufise ThunderHub iriko irakora ku nzira yawe ya Umbrel.



### Gushiramwo n'amaboko (kwiyakira, hatarimwo Umutaka)



Ku bakoresha hanze ya Umbrel (nk'akarorero kuri server y'umuntu ku giti ciwe, Raspberry Pi ifise RaspiBlitz canke *ugushiraho*), gushiramwo ThunderHub bisaba intambwe nkeyi z'inyongera. Aha hepfo turadondora ugushiraho kuva ku ntango n’ugutunganya, hakurikijwe [inyandiko zemewe za ThunderHub](https://docs.thunderhub.io).



#### Gushiramwo



**Ibisabwa:** Raba neza ko sisitemu yawe ihuye n'ibisabwa bikeyi hakurikijwe [ugutegura inyandiko](https://docs.thunderhub.io/gutegura):




- Node.js** verisiyo 18 canke hejuru
- npm** yashizweho
- Ugushika ku madosiye y'ukwemeza LND :
  - LND Icemezo ca TLS (`tls.icemezo`)
  - LND ubuyobozi bw'imakaroni (`ubuyobozi.imakaroni`)
  - LND gRPC serivisi Address (izina ry'umushitsi:icuma) (mburabuzi `127.0.0.1:10009` mu karere)



**1. Kugarura kode ya ThunderHub:** Gukora ububiko bwa GitHub bw'umugambi nk'uko bivugwa muri [inyandiko zo gushiramwo](https://docs.thunderhub.io/gushiraho):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. shiraho ibivako maze wubake porogaramu:**



```bash
npm install
npm run build
```



Aya mabwirizwa ashiramwo ibice vyose bisabwa hanyuma agakoranya porogarama (ThunderHub yanditswe mu rurimi rwa TypeScript/React).



**3. Ivugurura nyuma:** ThunderHub itanga uburyo bwinshi bwo kuvugurura muri kazoza:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Gutunganya (Gutunganya)



**1. Dosiye y'imiterere nyamukuru:** Rema dosiye `.env.local` ku muzi wa dosiye ya ThunderHub kugira ngo uhindure imiterere (ivyo bizokubuza imiterere yawe kwandikwako mu gihe c'ivugurura). Ibihinduka nyamukuru nk'uko [inyandiko zo gutegura](https://inyandiko.thunderhub.io/gutegura):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Itunganywa rya konti za Serveri:** Rema dosiye ya YAML yerekanwa muri `ACCOUNT_CONFIG_PATH` :



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Ukwinjira kure:** Kugira ngo uhuze n'uruzitiro rwa kure rwa LND, wongere kuri `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Umutekano:** Ku ntango ya mbere, ThunderHub **ihita** ihisha `masterPassword` n'amajambo y'ibanga yose ya konti muri dosiye ya YAML, kugira ngo wirinde kugira amajambo y'ibanga mu nyandiko zitomoye kuri server.



**5. Gutangura Inkuba:**



```bash
npm start
```



Ku mburabuzi, umukozi yumviriza ku nzira 3000. Ushobora gushika ku `http://localhost:3000` (canke `http://ip-umukozi:3000` uvuye ku rubuga rw'aho hantu).



**6. Ubundi buryo bwa Docker:** ThunderHub itanga amashusho yemewe ya Docker:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Paje yo kwinjira muri ThunderHub iraboneka. Hitamwo konti yatunganijwe maze winjize ijambobanga kugira ngo ugere ku rubuga.



**Gushiramwo ku bindi bikoresho:** Ivyiyumviro vy'ubuhinga bwa node (RaspiBlitz, MyNode, Start9, n'ibindi) muri rusangi bitanga ubufasha bwa ThunderHub biciye ku nzira zavyo z'uburongozi.



**Ku bindi bisobanuro:** Raba inyandiko zose zizwi :




- Gushiramwo:** [inyandiko.inkuba.io/ishirwaho](https://inyandiko.inkuba.io/ishirwaho)
- Itunganywa:** [inyandiko.inkuba.io/gutegura](https://inyandiko.inkuba.io/gutegura)



Ivyo bikoresho biradondora neza amahitamwo ateye imbere nk’amakonti ya SSO, ama macaroons yashizwemwo amakuru, ugutunganya TOR n’ibindi vyinshi.



Iyo ThunderHub imaze gushirwaho kandi ikaba ishobora gukoreshwa, uba witeguriye gukoresha ibintu vyose birimwo. Mu gice gikurikira, turaza kuraba Interface ThunderHub n’ibice vyayo bitandukanye, kugira ngo tubayobore mu gukoresha kwayo.



## Interface ikiganiro



Interface ThunderHub itunganijwe ikikuje urutonde nyamukuru (akenshi rwerekanwa mu nkingi yo ku ruhande rw’ibubamfu) rugizwe n’ibice vyinshi vy’ingenzi. Imwe yose ihuye n’umuce wo gucunga urudodo rwawe rw’Umuravyo. Reka tubiciremwo kimwe kimwe:





- Ingoro** - Ingoro tab ifise dashboard rusangi (insiguro y'uruzitiro rwawe n'ibikorwa vyihuta).
- Dashboard** - Dashboard ishobora guhindurwa n'ibikoresho n'ibipimo biteye imbere.
- Peers** - Uburongozi bw'abagenzi bw'umuravyo (uguhuza n'izindi nzira).
- Imirongo** - Uburongozi burambuye bw'imirongo y'umuravyo.
- Rebalance** - Igikoresho co gupima imirongo (ukwishyura kw’uruziga).
- Ibikorwa** - Amateka y’ukwishura kw’umuravyo (ibikorwa vya LN).
- Imbere** - Imibare y'inzira (amahera ashikirizwa n'uruzitiro rwawe).
- Uruzitiro** - Igitigiri ca Node-22 Wallet (Igitigiri ca 22 BTC: UTXOs, ibikorwa).
- Amboss** - Ukwifatanya na Amboss (ugukurikirana node, gusubiza inyuma, n'ibindi).
- Ibikoresho** - Ibikoresho bitandukanye (ibisubizo, ubutumwa bushizweko umukono, amakaroni, raporo, n’ibindi).
- Guhindura** - On-Chain/Imiravyo guhindura ibikorwa biciye ku Boltz.
- Stats** - Imibare iteye imbere n'ibipimo vy'imikorere y'imirongo.



*(Iciyumviro: Bivanye n'uko ThunderHub ikoresha, ibice bimwebimwe bishobora kuba bifise imitwe itandukanye gatoyi canke ibindi bintu vy'inyongera, ariko ingingo ngenderwako rusangi ziguma ari zimwe)*



### Inzu (Igikoresho rusangi co kugenzura)



ThunderHub's **Home** tab ni paji y'intango iboneka umaze kwinjira.Irimwo **General Dashboard**, itanga **insiguro y'isi yose** y'ingene urudodo rwawe rwa Lightning rumeze kandi itanga ivyiyumviro **ibikorwa vyihuta** ku bikorwa vya misi yose. Ehe ivyo uzosanga:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- Imibare n'ubushobozi:** Hejuru kuri paji, ThunderHub yerekana imibare yawe iriho. Aha uzobona mu bisanzwe umubare wa On-Chain (Bitcoin On-Chain muri Wallet y’urudodo, ugereranywa n’umuravyo Anchor ⚓) n’umubare w’umuravyo (ubushobozi bw’imirongo yawe, ugereranywa n’umuravyo Bolt ⚡). Ivyo biguha iciyumviro c’amahera ufise muri On-Chain na Lightning. Niba ufise amakonti canke imihora myinshi, urabe neza ko uri ku nzira nziza (nk’akarorero Mainnet vs Testnet).





- Imibare nyamukuru:** Dashboard ishobora kwerekana ibipimo bimwebimwe vyo kw'isi yose ku bijanye n'uruzitiro rwawe - nk'akarorero, umubare w'imirongo yuguruye, umubare w'abagenzi bahuye, amafaranga y'inzira yaronkejwe (niba ari ngombwa), n'ibindi.





- Ibikorwa vyihuta:** Ku rubuga rw’ibikoresho rufise amabuto yo gukora vyihuse ibikorwa bikunze gukorwa cane, ataco ukeneye guca mu bimenyetso. Ivyo bikorwa vyihuta birimwo:





- Ghost**: Gushinga umuravyo Address usanzwe biciye kuri Amboss.
- Donate**: Gutanga intererano biciye ku Muravyo.
- Injira/Genda kuri**: Huza kuri konti yawe ya Amboss (Ihuza vuba) hanyuma ugende ubwo nyene kuri Amboss.space kugira ngo ubone amakuru y’urudodo rwawe.
- Address**: Injira umuravyo Address kugira ngo ukore amahera.
- Gufungura**: Gufungura umurongo mushasha w'umuravyo. Gukanda bifungura urupapuro rwo kwinjiza URI y’uruzitiro rwa kure rwo gufungurirako umurongo, umubare n’amahera, nimba bishoboka, amahera menshi cane ya On-Chain azokoreshwa.
- Decode**: Gusobanura umuravyo Invoice canke LNURL kugira ngo ubone ido n’ido imbere y’uko uriha.
- LNURL**: Gukora LNURLs ku kwishura canke gukura amahera y'umuravyo.
- Injira muri LnMarkets**: Injira muri LnMarkets kugira ngo ukore ubucuruzi.



Ivyo bikorwa vyihuta biratuma ushobora gukora ibikorwa bikunze gukorwa cane uhereye kuri paji y’intango, utabwirizwa guca mu bice bitandukanye vyo muri Interface.



Muri make, dashboard ya ThunderHub iraguha **ukwihweza ningoga** ku node yawe kandi ikagufasha gukora ibikorwa bikunda gukorwa (kohereza/kwakira, gufungura umurongo) ukoresheje gukanda rimwe. Ni intango nziza y’uburongozi bwa misi yose.



### Urubaho



Igice ca **Dashboard** gitandukanye n'igice c'Ingoro kandi gitanga urupapuro rwo hejuru, rushobora guhindurwa. Iki gice kigufasha gukora imbonerahamwe ihinduwe n'ibikoresho vyihariye bivanye n'ivyo ukeneye nk'umukoresha w'urudodo.





- Ibikoresho bishobora guhindurwa:** Bitandukanye n’urupapuro rw’Imbere, rufise uburyo buhoraho, Dashboard iragufasha guhitamwo neza neza Elements uzogaragaza n’ingene uzoyitunganya.



![Dashboard sans widgets activés](assets/fr/06.webp)



Niba ata bikoresho bishobojwe, uzobona "Nta bikoresho bishobojwe!" ubutumwa bufise buto ya "Ivyagezwe" kugira ngo ugere ku mirongo ngenderwako y'uguhindura.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



Mu mirongo, ushobora guhitamwo mu bikoresho vyinshi vyatunganijwe mu mice: "Umuravyo - Amakuru", "Umuravyo - Imeza", "Umuravyo - Igishushanyo", n'ibindi. Igikoresho cose gishobora gukoreshwa canke gukurwaho n'ubuto "Show/Hide".



![Bas de la page des paramètres](assets/fr/08.webp)



Mu mpera z'amasetingi, uzosanga ubuto "Ku Dashboard" kugira ngo usubire ku dashboard n'ubuto "Reset Widgets" kugira ngo usubiremwo ikigaragaza mbere.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Iyo umaze gutunganya, urupapuro rwawe rushobora kwerekana ibishushanyo n’ibipimo bitandukanye: Ibishushanyo vy’ukwishyura kw’umuravyo, umubare w’amafagitire yasohowe, imibare y’imbere, amafaranga asigaye, n’ibindi.





- Ivyiyumviro biteye imbere:** Ushobora gushika ku biharuro vyinshi ku mikorere y'uruzitiro rwawe, n'ibishushanyo n'amakuru y'igihe nyaco.





- Incamake ishobora guhindurwa:** Guhindura ikigaragaza kugira ngo kijane n'uko uri umukoresha asanzwe canke umukoresha w'umwuga arongoye imirongo myinshi y'inzira.





- Modular Interface:** Wongere canke ukureho ibikoresho nk'uko bisabwa: ibiharuro vy'imbere, ibipimo vy'amahera, imburi z'ubuzima bw'imirongo, n'ibindi.



Iki gice ni ngirakamaro cane cane ku bakoresha bateye imbere bipfuza gukurikirana ibipimo vyihariye canke kuronka icegeranyo c'ubuhinga c'umurongo wabo w'umuravyo. Irashigikira igice c’Ingoro mu gutanga uburenganzira bwinshi bwo guhindura no kugenzura ingene amakuru yerekanwa.



### Abagenzi



Igice ca **Peers** kigaragaza urutonde rw'ibihimba vyose vya Lightning ubu bihuye n'ivyawe nk'abagenzi. **peer** ni ihuriro ry'urudodo ku rudodo kuri Lightning Network. Igikoresho cawe gishobora guhuzwa n'urunganwe mbere ata muhora wuguruye (nk'akarorero, gusa ku makuru y'urusaku rwa Exchange ku rubuga), canke vy'ukuri umurongo wose wuguruye ubwo nyene uvuga urunganwe rwuguruye.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Mu rutonde rw'urunganwe, uzobona :





- Inkingi z’amakuru:** Interface yerekana amakuru y’ingirakamaro nk’imiterere y’uguhuza, ubwoko bw’ihuriro (clearnet canke Tor), ping, satoshis yakiriwe/yoherejwe n’ingero y’amakuru yahinduwe.
- Yongerako umugenzi: ThunderHub ishobora kugufasha kwifatanya n'umugenzi mushasha biciye ku buto **"Ongera"** buri hejuru iburyo. Uzokenera kwinjiza URI y'urudodo (uburyo `<urufunguzo_rwa bose>@<urufunguzo>`). Igihe yemejwe, ThunderHub yohereza itegeko `lncli guhuza` rihuye. Nimba iyo node iri kuri interineti kandi ishobora gushikwako, izokwongerwa ku rutonde rw’urunganwe rwawe.



### Imirongo



**Imirongo** ni umutima w'uburongozi bw'imirongo ya Lightning. Birashoboka ko ari co gice uzokwihweza kenshi. Igaragaza **imirongo yawe yose ya Lightning** n'ibisobanuro vyayo, kandi ikagufasha gukora ibikorwa vy'uburongozi kuri iyo mirongo.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Ehe ivyo uzosanga kuri paji y'Imirongo:





- Urutonde rw’imirongo:** Umurongo wose wuguruye (canke wuguruye/wufunga) urarurwa ku rutonde, akenshi ufise izina ry’uruzitiro rwo kure, ubushobozi bwose bw’umurongo, n’umurongo w’ibara werekana ugusangira kw’amahera yo mu karere n’ayo kure. ThunderHub ikoresha kode y’ibara (kenshi ubururu/Green) canke ijana kugira ngo yerekane uburinganire bw’imirongo: nk’akarorero, ubururu ku mugabane wawe wo mu karere, Green ku mugabane wo kure. Iyo umurongo uringaniye neza (50/50), umurongo uzoba igice c’ibara rimwe rimwe. Ivyo bituma ubona mu kanya nk’ako gukubita imirongo idahuye (ubururu bwose = hafi bwose bwo mu karere, Green yose = hafi yose yo kure).





- Inkingi z’amakuru:** Interface yerekana inkingi z’ido n’ido harimwo Ivyiyumviro, Ibikorwa Biriho, Amakuru y’Abagenzi, Indangamuntu y’Umurongo, Ubushobozi, Ibikorwa, Amahera n’Imibare n’Ikigaragaza Ivy’Itunga.





- Ivyerekanywe:** Igikoresho co mu mfuruka yo hejuru iburyo kigufasha guhindura ivyerekanwa vy'umurongo kugira ngo bihure n'ivyo ukunda.





- Status:** Uzobona kandi ibimenyetso vy'imimerere - nk'akarorero. `Ikora` (umurongo ufunguye kandi urakora), `Offline` (umugenzi uracitse, rero umurongo ntukoreshwa mu gihe gito), `Urindiriye` (ku gufungura canke gufunga birindiriye kwemezwa na On-Chain).





- Ibikorwa ku muhora:** Ku muhora wose, ThunderHub itanga amabuto y'ibikorwa (kenshi mu buryo bw'ibishushanyo):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- Guhindura amafaranga:** Interface "Itegeko ry'umurongo" rigufasha guhindura imirongo yose: Amafaranga y'ishimikiro, Igiciro c'amafaranga (mu ppm), CLTV Delta, Max HTLC na Min HTLC. Ivyo bigufasha guhindura amategeko yawe y’amahera ku giti cawe ku muhora, n’intumbero yo gukwegera (canke guca intege) uruja n’uruza rw’inzira. *(Iciyumviro: ThunderHub ntabwo isubirira igikoresho co gucunga amafaranga, ariko ku guhindura amafaranga n'amaboko birakora cane)*
- Gufunga Umurongo (**Gufunga**): Interface "Ugufunga Umurongo" iguha amahitamwo hagati ya **gufunga kw'ubufatanye** (ivya kera) canke **gufunga ku nguvu** (**Gufunga ku nguvu**) mu gusobanura ibirego (mu Sats/vByte). **Igihambaye:** wama uhitamwo gufunga amakoperative iyo bishoboka, kugira wirinde ugucererwa kw’amahera ya On-Chain n’amahera menshi. ThunderHub izokubwira nimba uwo mugenzi ari kuri internet (ugukorana birashoboka) canke atarivyo. Mu gihe co gufunga inguvu, menya neza ko wemeza kuko ivyo bidashobora gusubirwamwo kandi bizotuma haba ugucuruza gukomeye n’igihe (muri rusangi amabarabara 144 canke umusi umwe kuri Bitcoin Mainnet).
- Gufungura umurongo mushasha:** Kugira ngo ufungure umurongo mushasha, fyonda ku nzira iri hejuru iburyo kuri paji y'imirongo, hanyuma uhitemwo "Gufungura". Ushobora rero gutanguza umurongo ku mugenzi mushasha canke asanzweho. Ivyiza vyo gukoresha iyi paji ni uko ufise urutonde rw’imirongo yawe isanzwe imbere yawe, ivyo bishobora kugufasha guhitamwo aho wofungura imirongo mishasha.



Muri make, igice c'Imirongo kiguha **ububasha bwiza ku nzira yose**. Aha niho utwara amafaranga, ugafata ingingo y’imirongo uzogumya canke uzofunga, ugashinga imirongo yawe y’inzira. ThunderHub itanga Interface igaragara kuri ivyo bikorwa bihambaye vyo gucunga node.



### Gusubiramwo uburinganire



Igipande ca **Rebalance** kigenewe **uguringaniza imirongo**. Guringaniza (canke *gusubiramwo*) birimwo gusubira gutunganya ugusangira amafaranga hagati y'imihora yawe isohoka n'injira, mu gutanga **ukwishyura kw'uruziga** kuva kuri imwe mu mihora yawe uja ku yindi mihora yawe, biciye ku Lightning Network. Ivyo bigufasha, utazanye amahera mashasha, guhindura amahera kuva ku muhora wuzuye cane ukaja ku muhora wuzuye cane, bikaba bituma imihora yawe iba ngirakamaro (umuhora uringaniye urashobora kohereza no kwakira amahera).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub yorohereza cane iyo nzira, iyo itaba ari iyo gukora, ivyo bikaba vyari kurambira ku murongo w’amabwirizwa. Ehe ingene wokoresha igice ca Rebalance:





- Imbonerahamwe y’imirongo y’intango:** Iyo winjiye muri Rebalance, ThunderHub yerekana urutonde rw’imirongo yawe, n’ikimenyetso c’uburinganire kuri buri imwe (bisa n’ivyo kuri paji y’imirongo). Ushobora guca ubona imirongo idafise uburinganire. ThunderHub ishobora gutoranya imirongo mu buryo bwo kwongerekana kw’uburinganire, kugira ngo imirongo idafise uburinganire cane igaragare hejuru y’urutonde (0.0 bisobanura ko ari iyo mu karere canke iyo kure).





- Guhitamwo bagenzi:** Interface ituma vyoroha guhitamwo bagenzi basohoka n’abaza kugira ngo basubire gufatanya.





- Amaparametere:** Ushobora gushinga :
  - **Igiciro kinini cane** (mu Sats na ppm) wifuza kwishura
  - **Igiciro co gusubira gupima** n'amahitamwo "Idahinduka" canke "Iciyumviro"
- Nodes zo kwirinda** igihe ukoresha inzira
- Igihe co kugerageza** co kurondera inzira





- Hitamwo **isoko** umurongo: Ubanze uhitemwo **isohoka (isoko)** umurongo, ni ukuvuga umurongo ufise amahera menshi cane yo mu karere kugira ngo uvemwo. Mu bikorwa, uwu ni umuhora aho umugabane wawe wo mu karere uri hejuru (> 50%). Reka twiyumvire umurongo wa A ufise Satss 1.000.000, 900.000 muri zo zikaba ari izo mu karere - ni umuntu mwiza wo kohereza Satss ahandi. Mu gufyonda kuri iyi nzira A nk'"isohoka", ThunderHub irayishirako ikimenyetso nk'inkomoko.





- Hitamwo **umurongo w’intumbero**: Hanyuma, hitamwo **umurongo winjira (intumbero)** ukeneye kwakira amahera. Mu bisanzwe, uwu uzoba ari umuhora aho ari ukundi - amahera menshi ari ku ruhande rwa kure (nk'akarorero 100.000 gusa Satss zo mu karere ku 1.000.000). ThunderHub, iyo umurongo w’inkomoko umaze gutorwa, izotoranya iyindi mirongo mu buryo buhindutse (ugugabanya uburinganire) kugira ngo ifashe mu kumenya imirongo yuzuzanya cane. Hitamwo umurongo wa B ufise umwanya ku ruhande rw’aho hantu. ThunderHub izoca yerekana neza imirongo ibiri yatowe (inkomoko A n’intumbero B).





- Gushinga amafaranga n'ukwihanganira:** Urupapuro ruguha uburenganzira bwo kwinjira :





  - **Igiciro** kizosubirwamwo (mu Sats). Akenshi, duhitamwo umubare ungana n'uwo woshobora gutuma imirongo yose igira uburinganire ku \~50/50. ThunderHub ishobora kwuzuza imbere igice c'ubushobozi burenze ubw'umurongo w'inkomoko, nk'akarorero.
  - **Amahera menshi cane** wifuza kwishura kuri iyo operation (ntibikenewe). Iryo shirahamwe rigaragazwa muri Sats (igiciro cose c’inzira y’uruziga). Iyo uyisiga ubusa, ThunderHub izorondera inzira ataco ifatiye ku giciro, ivyo muri rusangi ntivyiza (ni vyiza gushinga umupaka, nk’akarorero 10 Sats ku bijanye n’ugusubiramwo gatoyi, canke ppm nyinshi).





- Rondera Inzira:** Fyonda kuri buto kugira uronke inzira. ThunderHub ibaza LND kugira ngo ibaze inzira iva ku muhora wawe w’inkomoko uciye ku rubuga uja ku muhora wawe bwite w’intumbero. Iyo ibonye inzira ishoboka ihuye n’ingingo zawe z’amahera, irayerekana n’ibintu vy’ido n’ido vy’ibihembo n’igiciro c’amahera. Nk’akarorero, vyoshobora kwerekana ko yaronse inzira y’amaguru 3 ifise umubare wose w’amashanyarazi 2 Sats.





- Tangira gusubiramwo:** Niba unezerewe n'inzira yashikirijwe, fyonda ku **Umurongo w'Umubano**. ThunderHub izoca itangura kwishura biciye kuri LND. Iyo kwishura bishitse, uzobona itangazo ry’uko bishitse, kandi imirongo A na B izogira amafaranga ahinduwe mu gihe nyaco. ThunderHub izohindura ikimenyetso c’uburinganire bw’izo nzira (mu vyiza izoba ari icatsi kibisi kuruta uko yari imbere, yerekana uburinganire bwiza).





- Guhindura n'ugusubiramwo:** Niba ata nzira ibonetse ku kugerageza kwa mbere (canke iyo izimvye cane), ushobora guhindura amaparametere:





  - Gerageza umubare mutoyi (rimwe na rimwe ugusubiramwo igice kiraca mu gihe umubare munini ushobora kunanirwa).
  - Wongere amahera menshi buhoro buhoro, ariko urabe ko udashobora kwishura amahera menshi kuruta ayo akwiye.
  - Koresha buto **Rondera iyindi nzira**, nimba iriho, kugira ngo ugerageze ubundi buryo.
  - Gerageza iyindi nzira ibiri nimba vy’ukuri ibintu bifatanye.



ThunderHub ituma iyo nzira **igaragara cane kandi igaragara**. Mu ntambwe 4 gusa (hitamwo umurongo usohoka, hitamwo umurongo winjira, umubare, kwemeza), urashobora gukora ivyo vyahora bisaba amabwirizwa agoranye y’amaboko. Ico gikoresho ni ikintu c’agaciro kanini mu kubungabunga urudodo ruri ku rugero rwiza, mu gutuma urushiriza gukora neza mu bijanye n’inzira n’ubumenyi bwawe (vyoroshe kohereza no kwakira amahera ku mihora yawe yose).



Ubwa nyuma, menya ko gusubiramwo uburinganire bifata amafaranga y’inzira (yishurwa ku nzira zo hagati), rero ni **ishoramari** kugira ngo nzira yawe ibe nziza cane. Ukoreshe neza, nk’akarorero kugira ngo ushigikire umurongo w’ibikorwa ukoresha kenshi (inbound liquidity) canke kugira ngo ushire mu rugero umurongo munini w’inzira. ThunderHub iragufasha gukora ivyo **mu buryo bworoshe kandi bubereye**.



### Ibicuruzwa



Igice ca **Ibikorwa** muri ThunderHub gihuye n'amateka y'ibikorwa vya **Lightning** vy'uruzitiro rwawe, ni ukuvuga amahera n'amafagitire yishuwe canke yakiriwe biciye ku mihora. Ni ubwoko bw’itangazo ry’ibikorwa vyawe vya LN.



![Historique des transactions Lightning](assets/fr/14.webp)



Muri iyi tab uzosanga :





- Invoice graph:** Mu mfuruka yo hejuru iburyo, graph yerekana iterambere ry’amafagitire yaronse uko igihe kigenda kirarenga, bikagufasha kubona mu ciyumviro igikorwa c’urudodo rwawe.





- Urutonde rw'ibihe vy'ibikorwa vyose vya Lightning vyakozwe *kuva* canke *ku* node yawe. Inyinjizo yose ishobora kwerekana :





  - Ubwoko bw’ibikorwa: **ukwishyura kwoherejwe** (ukwishyura gusohoka) canke **ukwishyura kwakiriwe** (ukwinjira, biciye ku Invoice yishuwe).
  - Amahera ari muri Sats.
  - Itariki/isaha.
  - Indangamuntu y’ukwishura (Hash canke ishusho y’imbere ya RHash) canke igitekerezo (niba wongeyeko inyandiko kuri Invoice).
  - Igihugu: **vyarangiye**, canke bishoboka **biriko birakorwa**/*vyananiwe* (nk'akarorero, ukwishyura kurindiriye gutorwa umuti, ariko muri rusangi LND ibikora ningoga, rero nta "bitegerejwe" bike hano ugereranyije n'ibikorwa vya On-Chain).



Muri make, igice c'Imigenderanire gikora nk'igitabo cawe c'ibikorwa vya LN**. Ni ngirakamaro cane mu kugenzura ko amahera yaciyemwo, amafaranga angahe yatwaye, canke gukurikirana amateka y’amahera yawe ya Lightning. Mu gufatanya n’igice c’Imbere (ikidondaguwe gikurikira), uzobona neza amahera yaciye mu nzira yawe.



### Imbere



Igipande ca **Forwards** kigenewe igikorwa ca **guca** c'umurongo wawe, ni ukuvuga amafaranga **aca** mu mihora yawe (igihe ukora nk'umurongo w'umuhuza kuri Lightning Network). Niba ukoresha urudodo rwawe nk'urudodo rw'inzira, iki ni igice gihambaye co gukurikirana ibikorwa vyawe.



![Statistiques de routage Lightning](assets/fr/15.webp)



Mu vyo imbere, ThunderHub itanga :





- Amayunguruzo n'amahitamwo y'iyerekanwa:** Hejuru iburyo, amayunguruzo aragufasha gutoranya amakuru ku musi/indwi/ukwezi/umwaka, maze ugahitamwo hagati y'iyerekanwa ry'ibishushanyo canke ry'imbonerahamwe.





- Ubutumwa bw'igikorwa:** Nimba ata nzira yakozwe mu kiringo catowe, Interface yerekana "Nta nzira y'imbere muri iki kiringo", nk'uko vyerekanwa muri aka karorero.





- **Imbonerahamwe y'ivyo biherutse gushikirizwa**: ikintu cose cinjijwe gihuye n'ukwishyura kwashikirijwe **biciye ku nzira yawe. Ku mukinyi wese w'imbere, muri rusangi tubona :





  - Timestamp,
  - amahera yarungitswe (mu Sats), .
  - **amahera yaronse** kuri iyi nzira y’imbere (mu Sats, iri ni ryo tandukaniro hagati y’ivyo waronse ku muhora winjira n’ivyo wohereje ku muhora usohoka),
  - imirongo yinjira n'isohoka ikoreshwa (kenshi imenyekana n'izina ry'urunganwe canke ID y'umurongo).
  - status (mu bisanzwe *vyarangiye*, canke kunanirwa iyo umukinyi w'imbere ananiwe mu nzira).





- Imibare yose hamwe**: ThunderHub ibara kandi igaragaza hejuru kuri paji imibare yose hamwe n'imibare mu kiringo kinaka (nk'amasaha 24 aheze, canke imisi 7, n'ibindi, rimwe na rimwe bishobora guhindurwa).



Muri make, igice c'Imbere gitanga **insiguro y'igihe nyaco y'igikorwa c'inzira y'umuravyo wawe**. Ivyo bifatanijwe n’ibice vy’Imirongo n’Ivy’Ugusubiramwo, bica bikora umugwi wuzuye wo gutuma urudodo rwawe rugenda neza: Imirongo/Ivy’Ugusubiramwo kugira ngo ubone amahera, Imbere kugira ngo wihweze ibisubizo (imigenderanire n’inyungu).



### Uruzitiro



Igice ca **Uruzitiro** gihuye n’uburongozi bwa Bitcoin On-Chain Wallet bw’uruzitiro rwawe rwa LND. Iyi Interface iragufasha kubona no gucunga amahera ya Bitcoin, akoreshwa mu gufungura imihora canke kwakira amahera ava ku mihora yugaye.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



Mu ruzitiro, uzosanga :





- Igiharuro On-Chain:** Kigaragaza igiharuro cose ca BTC kiri muri Wallet LND.





- Urutonde rwa UTXO:** Raba ibisohoka vyose bitakoreshejwe (UTXO) n’umubare, ivyemezo, Address n’imiterere y’ibisohoka vyose.





- Amateka y'ibikorwa:** Imbonerahamwe y'ibikorwa vyose vya Bitcoin n'ubwoko (binjira/bisohoka), itariki, umubare, amafaranga, ivyemezo, igice co gushiramwo, amaderesi na txid.



### Ambosi



ThunderHub ifatanya n’urubuga rwa **Amboss** (amboss.space), rutanga amakuru arambuye ku bijanye n’ibihimba vya Lightning, isoko ry’amahera, n’ibintu vy’ingirakamaro nk’ugucungera umurongo w’amazi n’ugukurikirana ukuboneka.



![Intégration Amboss avec ses options](assets/fr/17.webp)



Muri ThunderHub, igice ca Amboss kiguha uburenganzira bwo **guhuza** urudodo rwawe na konti yawe ya Amboss:





- Ghost Address:** Shiraho **Umuravyo Address** w’umuntu ku giti ciwe ku bijanye n’uruzitiro rwawe, ushobore kworohereza amahera yinjira.





- Ivyiyumviro vy’imirongo vyikora:** Igikoresho c’ibendera c’ivy’imirongo y’ivyuma** (amadosiye ya SCB) kuri Amboss. Gukoresha **Amboss Auto Backup = Ego** mu mategeko kugira ngo uhite wohereza amakuru mashasha y'ububiko bw'ibintu igihe cose uhinduye imirongo. Iyo habayeho ukunanirwa, uzoshobora gusubirana amahera yawe biciye kuri iyo nkuru y’inyuma.





- Ivyiyumviro vy'ubuzima:** Gukoresha **Ivyiyumviro vy'ubuzima vya Amboss = Ego** kugira ngo node yawe yohereze ama pings adasanzwe kuri Amboss. Uzoronka imburi iyo urudodo rwawe rusa n'urutari ku murongo.





- Ibindi biranga:** Gusunika uburinganire bwite, **Ugushiramwo Magma/Hydro** (isoko ry’amahera), no kuronka imibare y’ibikorwa vy’ido n’ido.



Ubufatanye bwa Amboss bwongerako **umutekano Layer** w’ingenzi ufise ububiko bw’inyuma bwikora n’ugukurikirana ukuboneka, ushobora kuronka uhereye kuri ThunderHub.



### Ibikoresho



Igice ca **Ibikoresho** gikoranya ibikoresho bitandukanye vy'ubuhinga bwo gucunga urudodo rwawe. Aha niho hari Elements nyamukuru:



![Interface des outils disponibles](assets/fr/18.webp)





- Ivyiyumviro:** Gucungera n'amaboko ivy'imirongo yawe (SCB). ThunderHub iragufasha **gukuraho dosiye yuzuye y'ububiko** y'imirongo yawe (uburyo "Gukuraho imirongo yose -> Gukuraho"). Bika iyi dosiye `channel-all.bak` ahantu heza - ni ngombwa kugira ngo ubone amahera yawe iyo habaye impanuka. Ushobora kandi **kwinjiza** dosiye y'ububiko igihe usubiye gukoresha urudodo.





- Ivy’Ibarabara:** Igikoresho co kwohereza hanze raporo z’ivy’imari harimwo amafaranga yaronse/yishuwe n’ibiharuro vyarungitswe mu kiringo kinaka.
- Ubutumwa bwashizweko umukono:** Sinya canke usuzume ubutumwa n'urudodo rwawe kugira ngo werekane Ownership y'urudodo rwawe rwa Lightning biciye ku mukono w'ibanga.
- Macaroons (Igice c'Imikate):** Gucungera LND** macaroons kugira ngo ureme uburyo bwo kuronka. Interface "Bakery" ishobora kugufasha guhitamwo neza uruhusha rwose: "Kwongerako canke gukuraho Abagenzi", "Rema Aderesi z'Uruhererekane", "Rema Amafagitire", "Rema Macaroons", "Gukura Imfunguruzo", "Kuronka Imfunguruzo zo Kwinjiramwo", "Kuronka Amafagitire y'Uruhererekane", "Get Get", "Get Invoice". Abagenzi", "Ishura amafagitire", "Gukuraho Ids z'Ukwinjira", "Kohereza ku Maderesi y'Uruzitiro", "Gushirako umukono ku bytes", "Gushirako umukono ku butumwa", "Hagarika daemon", "Gusuzuma umukono wa bytes", "Gusuzuma ubutumwa", n'ibindi. Uruhusha rwose rushobora gukoreshwa ku giti cawe n'ubuto "Ego/Oya" kugira ngo ureme macaroon igenewe umuntu.
- Amakuru ya sisitemu:** Kwerekana verisiyo ya Wallet na RPCs zakoreshejwe.



Muri make, igice c'Ibikoresho gihuza ibikorwa vy'uburongozi biteye imbere - gucungera, gucungera amafaranga, umutekano n'ugucungera uburyo bwo gukoresha - mu Interface imwe.



### Guhanahana



Igipande ca ThunderHub **Swap** kigufasha guhindura satoshis z’umuravyo ku Bitcoin On-Chain biciye ku nzira ya Boltz. Ivyo ni ngirakamaro mu "gutera" amazi y'umuravyo arenga ku muhora ata gufunga umurongo.



![Interface de swap via Boltz](assets/fr/19.webp)



Inzira ni yoroshe:





- Amafaranga**: Sigura amafaranga azohindurwa
- Address**: Injira Bitcoin kwakira Address
- Ishirwa mu ngiro**: ThunderHub ivugana na Boltz kugira ngo ikore Exchange



**Inyungu:**




- Ibikorwa bitagira ububiko (nta bubiko bw'amahera)
- Zigama imirongo yawe isanzweho
- Yoroshe gukoresha yunze ubumwe Interface



Boltz isaba komisiyo ntoyi kandi wewe uriha amahera asanzwe y’ugucuruza Bitcoin. ThunderHub yerekana ibiciro vyose imbere y’uko yemezwa.



### Imibare



Igice ca **Stats** ca ThunderHub gitanga **imibare iteye imbere** ku nzira yawe ya Lightning kugira ngo usesengure ibikorwa no gutuma inzira igenda neza.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Iki gice ni ngombwa mu gutuma amafaranga yawe agenda neza, kumenya inzira ziroraniwe no gutegura ukwaguka kw’uruzitiro rwawe.



## Iciyumviro



**ThunderHub** yarishizeho nk'igikoresho gihambaye co gukoresha neza urudodo rw'umuravyo **LND**. Iyi Interface y’ubu itanga ibikorwa vyose vy’ingenzi: gucunga imirongo, kwishura, gukurikirana, ifise ibintu biteye imbere nk’ugusubiramwo uburinganire n’ugushiramwo Amboss.



**Ivyiza nyamukuru:**




- Interface iraryoshe kandi igaragara
- Ibikoresho bikomeye (gusubiza uburinganire, guhindura Boltz, gusubiza inyuma vyikora)
- Ihuye n'umutaka, umuriro, RaspiBlitz n'ibindi bimenyetso



ThunderHub ikoresha demokarasi mu bijanye n’uburongozi bw’imirongo y’umuravyo, igatuma ivyo mbere vyasaba amabwirizwa y’ubuhinga asobanutse bishoboka. Waba uri umutanguzi canke umukoresha w'umuhinga, ThunderHub iragufasha gucunga neza urudodo rwawe rwa Lightning biciye ku nzira ya none, yuzuye Interface.



## Ubutunzi



**Amahuza yemewe:**




- Urubuga rwemewe:** [inkuba.io](https://inkuba.io)
- Inyandiko:** [inyandiko.inkuba.io](https://inyandiko.inkuba.io)
- Kode y'inkomoko ya GitHub:**