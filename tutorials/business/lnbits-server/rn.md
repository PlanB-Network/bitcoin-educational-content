---
name: Serveri y'ibice vya LN
description: Gushiramwo no gutunganya umukozi wa LNbits yikorera kuri Ubuntu VPS na Phoenixd canke kuri Umbrel
---

![cover](assets/cover.webp)



LNbits ni urubuga rwuguruye ruhindura urubuga rwose rw’inyuma rw’umuravyo (LND, Core Lightning, Phoenixd) mu rubuga rw’ibikorwa rwuzuye. Iyi nzira yishingira iragufasha gucunga ibitabo vyinshi vya Lightning wiherereye, gushiramwo ibibanza vyo kugurishako, guhingura uburyo bwo gutanga canke ibikorwa vyo gutanga amafaranga, mu gihe uguma ugenzura amahera yawe yose.



Iyi nyigisho ivuga uburyo bubiri bwo gushiramwo: **VPS Ubuntu na Phoenixd** (umuti woroshe udafise node ya Bitcoin yuzuye) na **Umbrel** (ugushiramwo node yawe ya LND iriho). Udakunze inyigisho rusangi ya LNbits ya Plan ₿ Academy, ivuga ku vyiyumviro n’ivyo kwagura, iyi nsiguro yibanda ku buryo bwo gushiramwo ubuhinga intambwe ku yindi.



## LNbits ni iki?



LNbits ni uburyo bwo guharura amafaranga bw’umuravyo bwateguwe muri Python (FastAPI) bufatanya n’inyuma busanzweho (LND, Umuravyo w’ishimikiro, Phoenixd). Udakunze ama node ya Lightning, LNbits itanga uburyo bwo gucungera ibiharuro vyinshi vyihariye bifise imfunguruzo zavyo bwite za API. Ushobora gukora ama sub-accounts y’umuryango wawe, abakozi canke imigambi yawe, utabahaye uburenganzira bwo kuronka amahera yawe yose.



Ubwubatsi butandukanye bubika amakuru muri SQLite (imbere) canke PostgreSQL (uguhingura), mu gihe amahera aguma acungiwe n'inyuma yawe ya Lightning. Ukwo gutandukanya gutuma ushobora gutwara: ushobora kuva kuri Phoenixd ukaja kuri LND utatakaje amakuru yawe y’abakoresha.



## Ibirango nyamukuru



LNbits itanga **uburyo bwo kwagura** butandukanye: TPoS (aho ugurisha), Paywall (ugutanga amahera mu birimwo), Ivyabaye (ugutanga amatike), LndHub (server ya BlueWallet), Amakarata ya Bolt (Ukwishura kwa NFC), Ugutanga Ukwishura (ugukwiragiza ubwavyo), n’Umucungerezi w’Ukoresha (ugucungera abakoresha n’ukwemeza).



**Dashboard** yerekana amafaranga y'igihe nyaco, amateka y'ibikorwa n'ibikoresho vyo gutanga amafaranga. wallet yose ifise URL yihariye irimwo imfunguruzo zayo za API, zituma umuntu ashobora kuyironka ata kwinjira mu buryo busanzwe. Urutonde rw’urufunguzo rwa API rw’urugero rutatu** (umuyobozi, invoice, gusoma gusa) rutanga ubugenzuzi bw’uruhusha rwo gukorana n’abandi mu buryo butekanye.



LNbits ikoresha **LNURL** (LNURL-kwishura, LNURL-gukuraho, LNURL-kwemeza) kandi ishigikira **Lightning Address**, igatanga icemeza ko ihuye n’ibipapuro vy’umuravyo vy’ubu kandi igafasha gukoresha ibikorwa vy’umwuga.



## Imbuga zishigikiwe



**Ubuntu VPS**: Umuti woroshe udafise urudodo rwuzuye rwa Bitcoin. Ibisabwa: vCPU 1, RAM 1-2 GB, Ubuntu 22.04 LTS, Inyuguti 3.10+, Git, UV. HTTPS + izina ry'indangarubuga rikenewe kugira ngo abantu bose bamenyekane (ibikorwa vya LNURL).



**Umutaka**: Biroroshe gushiramwo ukoresheje App Store. Ivyangombwa: urudodo rw’umutaka rukora rufise LND n’imirongo yuguruye. Itunganywa ryikora.



Aha hepfo hariho amahuza ku nyigisho zacu z’Umutaka n’Umutaka LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Gushiramwo kuri Ubuntu VPS na Phoenixd



### Intambwe ya 1: Gukingira umukozi wa VPS



**Imbere yo gushiramwo ikintu cose**, ukeneye gukingira server yawe ya Ubuntu VPS hakurikijwe amategeko y'ubuhinga. Iyi ntambwe ni **ihambaye cane** kugira ngo ukinge ibikorwa remezo vyawe n'amahera yawe ya Lightning.



Aha niho hari uburongozi burambuye bwo kugufasha gutangura: **[Itunganywa rya mbere rya serveri ya Ubuntu - Intambwe ku yindi](https://danielpcostas.



Iyi nkuru ivuga ku mitunganyirize y’abakoresha, SSH itekanye, uruhome rw’umuriro (UFW), fail2ban, guhindura ibintu vyihuta, n’imigenzo myiza yo gucungera umutekano wa sisitemu.



### Intambwe ya 2: Gushiramwo Phoenixd



Igihe server yawe itekanye, ukeneye gushiramwo no gutunganya Phoenixd. Plan ₿ Academy itanga inyigisho zijanye n'ugushiraho, uguhingura seed n'ugutunganya ibikorwa vya systemd :



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Igihe Phoenixd izoba iriko irakora (suzuma na `./phoenix-cli getinfo`), shiramwo ijambobanga rya **HTTP** muri `~/.



### Gushiraho LNbits



Gushiramwo UV no gukora LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Gutunganya inyuma ya Phoenixd:


```bash
cp .env.example .env && nano .env
```



Kwongera kuri `.inv` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Igerageza na `uv gukoresha lnbits --umushitsi 0.0.0.0 --icuma 5000` hanyuma ureme umurimo wa sisitemu na `Ishaka=phoenixd.umurimo`.



## Gutegura mbere n'ugukoresha ubwambere



### Gukoresha umukoresha mukuru



Gukoresha ikigaragara c'umuyobozi muri `.env` :


```
LNBITS_ADMIN_UI=true
```



Gusubira gutangura LNbits (`sudo systemctl gusubira gutangura lnbits`) no kugarura ID y'umukoresha mukuru:


```bash
cat ~/lnbits/data/.super_user
```



Genda kuri `http://<IP-VPS>:5000/wallet?usr=<ID y'Umukoresha Mukuru>` ku bijanye n'uburongozi. "Server" ishobora kugufasha gutunganya inkomoko z'amahera, ivyungura n'amakonti y'abakoresha.



### Gukora konti itekanye



**Igihambaye ku gushikiriza abantu bose**: Niba uriko urashikiriza urugero rwawe rwa LNbits ku izina ry'urubuga rwa bose rishobora gushikirizwa kuri Internet, ni **bihambaye cane** guhagarika uguhingura amakonti y'abakoresha ku buntu.



Kuva ku nzira y'ubuyobozi bwa SuperUser, genda kuri "Ivyagezwe" hanyuma uja ku gice ca "Ubuyobozi bw'Ukoresha". Aho uzosanga "Kwemerera kurema abakoresha bashasha".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Kubera iyerekanwa rya bose rifise izina ry'indangarubuga** :




- Utegerezwa guhagarika** uburyo bwo "Kwemera kurema abakoresha bashasha"
- Ata n’ubwo burinzi, umuntu wese ari kuri Internet arashobora gufungura konti kuri instance yawe .
- Umuntu atera yoshobora gukora amakonti agakoresha amahera y'uruzitiro rwawe rwa Lightning ataco uzi .
- Uzokenera kurema konti z'abakoresha n'amaboko ukoresheje ikigaragara ca SuperUser



**Ku gukoresha mu karere gusa** :




- Iyi nzira ntaco imaze iyo urugero rwawe rushobora gushikwako gusa mu karere (http://localhost:5000)
- Ariko rero, guhagarika iyo nzira ni uburyo bwiza bwo kwirinda muri rusangi .



Iyo imaze gutunganirizwa, umuyobozi wa SuperUser wenyene niwe ashobora gukora konti nshasha z'abakoresha biciye ku nzira ya "Abakoresha". Ubu buryo buratanga ububasha bwose ku bashobora gushika ku bikorwa remezo vyawe vya Lightning no gukoresha amahera yawe.



### Gufungura umurongo wambere



Phoenixd ihita icungera imirongo biciye ku nzira y’amahera. Gutanga inyemezabuguzi y'umuravyo ~30,000 sats uvuye kuri LNbits maze uyihe uhereye ku yindi wallet. Phoenixd ica ifungura umurongo kuri ACINQ. Amafaranga yo gufungura (~20-23k sats) arakurwako, amahera asigaye (~7-10k sats) aboneka inyuma y’ukwemezwa kwa on-chain.



Suzuma uko bimeze na `./phoenix-cli kuronka amakuru`. Hanyuma wiyumvire guhagarika amahera yikora (`ukwikoresha=off` muri `phoenix.conf`) kugira ngo ugenzure ugufungura kw'imirongo.



### Iyerekanwa rya bose na HTTPS



**Igihambaye**: HTTPS ni ngombwa kugira ngo yerekanwe ku bantu bose (umutekano w'urufunguzo rwa API + uguhuza kwa LNURL). Siga iyi ntambwe kugira ngo ukoreshe mu karere gusa.



**Caddy (irasabwa)**: SSL yikora. `sudo apt shiramwo -y caddy`, guhindura `/ n'ibindi/ caddy/ dosiye ya caddy` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Gusubira gutangura: `sudo systemctl gusubira gutangura caddy`.



**Nginx** : Ugucungera cane. Shiraho `nginx icemezo ca python3-icemezo ca nginx`, ureme `/n'ibindi/nginx/imbuga-ziboneka/lnbits` :


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Gukoresha: `sudo ln -s /n'ibindi/nginx/imbuga-ziboneka/lnbits /n'ibindi/nginx/imbuga-zishobojwe/ && sudo nginx -t && sudo systemctl gusubira gushiramwo nginx && sudo certbot --nginx -d urubuga rwawe.com`



Kwongera kuri `.env`: `KWEMERA_IPS=*`



## Gushiramwo umutaka



### Gushiraho bivuye kuri App Store



Genda ku bubiko bw'amaporogarama y'umutaka, urondere "LNbits", hanyuma ukande kuri "Shiraho".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umutaka uhita ugenzura ibikenewe. LNbits isaba Umuravyo (LND) kugira ngo ikore. Niba node yawe ya Lightning isanzwe ikora, fyonda ku "Shiraho LNbits" kugira ngo wemeze.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel ikuraho ishusho ya Docker, ihita itunganya amahuzu na LND, igatangura igikoresho (iminota 2-5). Gushiraho ibintu vyose bibera inyuma.



### Imiterere y'intango y'Umukoresha Mukuru



Ku gutangura kwa mbere, LNbits iragusaba gukora konti y'umuyobozi wa SuperUser. Injira izina ry'ukoresha n'ijambobanga ry'umutekano kugira ngo ukinge ukwinjira ku rubuga rw'ubuyobozi.



![Configuration SuperUser](assets/fr/03.webp)



**Igihambaye**: Iyi konti ya SuperUser ifise uburenganzira bwose ku nkuru yawe ya LNbits. Hitamwo ijambobanga rikomeye maze urizigame.



Iyo umaze gukora konti, uca uja ku rubuga nyamukuru rw'ubuyobozi. Umbrel yaramaze gushinga LND nk'isoko yawe y'amahera - amahera yose Lightning yishura azoca mu nzira zawe zisanzwe.



### Ukwinjira ku kigaragara c'umuyobozi



Mu ruhande rw'ibubamfu, fyonda ku "Settings" kugira ngo ubone urutonde rw'uburongozi rwose.



![Interface Settings](assets/fr/04.webp)



Igice ca "Ubuyobozi bw'amasakoshi" kigaragaza amakuru y'ingenzi yerekeye imiterere yawe:




- Inkomoko y'amahera** : LndBtcRestWallet (uguhuza n'umurongo wawe w'umutaka wa LND)
- Node Balance** : Amafaranga yose ari mu mihora yawe y'umuravyo
- Igitigiri c’amafaranga LNbits**: Amafaranga agenewe ubuhinga bwa LNbits (mu ntango 0 sats)



Ubu ushobora gukoresha ataco uhinduye amahera y'uruzitiro rwawe rwa Umbrel ku bikoresho vyose vya LNbits urema. Nta yindi ntunganyo ikenewe - LNbits irakora.



### Ubuyobozi bw'abakoresha



Kimwe mu bintu bikomeye cane vya LNbits ni ubushobozi bwayo bwo kurema abakoresha benshi bigenga, umwe wese afise ijambobanga ry’ukwemeza n’amasakoshi yitandukanije. Iyi nyubakwa ituma bishoboka kuronka akamaro k’amahera y’uruzitiro rwawe rwa Umbrel mu gihe utanga amakonti mato mato yitandukanije rwose ku bikorwa bitandukanye: ubucuruzi, umuryango, abakozi, imigambi, n’ibindi.



Mu rutonde rw'inyuma, fyonda ku "Abakoresha" kugira ngo ushikire uburongozi bw'abakoresha. Fyonda kuri "REMA KONTI" kugira ngo wongereko uwundi muntu.



![Gestion des utilisateurs](assets/fr/05.webp)



Uzuza urupapuro rwo kurema umukoresha:




- Izina ry'ukoresha**: Izina ry'ukoresha ryo kwinjira (akarorero: "satoshi")
- Gushinga Ijambobanga**: Gukoresha iyi nzira kugira ngo ushireho ijambobanga ry'ukwemeza
- Ijambobanga** na **Ijambobanga ryo gusubiramwo**: Shiraho ijambobanga ry'uyu mukoresha



![Création utilisateur satoshi](assets/fr/06.webp)



Ivyatsi vy'amahitamwo (Urufunguzo rwa bose rwa Nostr, Imeyili, Izina rya mbere, Izina ry'umuryango) bishobora gusigara ubusa kugira ngo haboneke imiterere mikeyi. Fyonda kuri "REMA KONTI" kugira ngo wemeze.



![Confirmation utilisateur créé](assets/fr/07.webp)



Uwukoresha wawe mushasha ubu araboneka ku rutonde rw'abakoresha afise ikimenyetso ciwe kidasanzwe n'izina ryiwe ry'ukoresha.



![Liste des utilisateurs](assets/fr/08.webp)



**Iciyumviro gihambaye**: Umuntu wese ashobora kwinjira yigenga rwose akoresheje ijambo banga ryiwe. Umuyobozi wa SuperUser aguma afise ububasha bwose biciye ku nzira y'ubuyobozi.



### Ubuyobozi bw'ukoresha wallet



None ko umukoresha wa "satoshi" yaremwe, ukeneye kumuha Umuravyo wa wallet. Fyonda ku kimenyetso ca wallet (ikimenyetso ca kabiri) c'uwukoresha, hanyuma kuri "REMA IKIGANIRO GISHASHA".



![Gestion des wallets](assets/fr/09.webp)



Agasanduku k'ikiganiro karagusaba gutanga izina rya wallet. Injira izina ridondora (nk'akarorero "Wallet Ya Satoshi") hanyuma uhitemwo amafaranga yerekanwa (CUC, USD, EUR, n'ibindi).



![Création wallet](assets/fr/10.webp)



Fyonda kuri "REMA". LNbits ihita itanga umuravyo ukora wallet kuri uyu mukoresha.



![Confirmation wallet créé](assets/fr/11.webp)



Ubu urabona amasakoshi abiri ariho: wallet "LNbits wallet" yaremwe ubwayo, n'iyindi "Wallet ya Satoshi". Kugira ngo worohereze ubumenyi bw’ukoresha, urashobora gukuraho wallet mburabuzi ukanda ku kimenyetso co gukuraho (igitereko c’ibikoresho vy’isuku gitukura).



![Wallet final unique](assets/fr/12.webp)



Uwukoresha "satoshi" ubu afise wallet imwe, igaragara neza. Buri muntu wese akoresha wallet akora yigenga mu gihe akoresha amahera y’urudodo rwawe rwa LND ruri munsi.



**Iciyumviro nyamukuru**: Izo nkweto zose zisangira amahera y’isi yose y’uruzitiro rwawe rwa Umbrel. Ntushobora kurema imirongo mishasha ya Lightning kuri buri wallet - LNbits ikora nk'uruzitiro rw'ubuhinga rw'ubuhinga rucungera ugutanga amafaranga mu bikorwa remezo vyawe vya Lightning biriho. Ubwo ni bwo bubasha bw’ubuhinga bwa LNbits bufise wallet nyinshi.



### Ukoresha kwinjira



Sohoka muri konti ya SuperUser (ikimenyetso kiri hejuru iburyo) maze usubire kuri paji yo kwinjira ya LNbits. Ubu ushobora kwinjira ukoresheje amakuru y'umukoresha mushasha.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Injira izina ry'ukoresha ("satoshi") n'ijambobanga ryasobanuwe mbere, hanyuma ukande kuri "LOGIN". Uwukoresha aronka uburenganzira bwo gukoresha wallet yiwe bwite, yitandukanije n’ivyo ubuyobozi bukora.



### Interface kuva ku mukoresha wa wallet



Iyo umuntu amaze kwinjira, ashobora gushika ku rubuga rwiwe rwose rwa wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Ibiranga ikigaragaza :




- Igiciro kiri muri iki gihe**: Kigaragazwa muri sats no mu mafaranga yatowe (CUC muri aka karorero)
- Ibikorwa vy'ingenzi**: GUSHIRAHO UBUSABA, GUREMA IFAKIRIZO, ikimenyetso ca QR (gucapura vuba)
- Amateka y'ibikorwa** : Urutonde rw'amahera yose yishuwe n'ivyo yakiriye
- Uruhande rw'iburyo**: Gutunganya no gushikira



### Uburyo bwo gukoresha telefone ngendanwa kuri wallet



Igipande co ku ruhande rw'iburyo kiratanga ikintu gihambaye cane: gukoresha telefone ngendanwa kuri wallet. Gufungura igice ca "Mobile Access" kugira ngo ubone amahitamwo ariho.



![Mobile Access](assets/fr/15.webp)



LNbits itanga uburyo bwinshi bwo gukoresha iyi wallet kuri telefone ngendanwa:



**Ihitamwo rya 1: Porogaramu zihuye kuri telefone ngendanwa




- Kuvana **Zewu** canke **Isakoshi y'ubururu** kuri App Store canke kuri Google Play
- Gukoresha **LndHub** kwagura mu LNbits kuri iyi wallet
- Scan kode ya QR ya LndHub ukoresheje porogarama yo kuri telefone ngendanwa kugira ngo uhuze wallet



**Ihitamwo rya 2: Ushobora gushikako biciye ku mucukumbuzi wa telefone ngendanwa**




- QR code yerekanwa muri "Export kuri telefone ufise QR Code" irimwo URL yuzuye ya wallet ifise ivyemezo vy'ukuri
- Scan iyi kode ya QR kuri telefone yawe kugira ngo ufungure wallet mu mucukumbuzi wawe wa telefone ngendanwa
- Kwongera urupapuro ku mugaragaro w'inzu kugira ngo uyironke ningoga



**Umutekano uhambaye**: Iyi URL irimwo imfunguruzo za API kugira ngo ushobore gushika kuri wallet. Ntukigere ubisangiza abandi ku mugaragaro. Fata iyi kode ya QR nk'uko wobifata ku mfunguruzo zawe z'ibanga za Bitcoin - umuntu wese ashobora gucapura iyi kode ya QR aronka uburenganzira bwo gukoresha wallet.



Iyi nzira y’amatelefone ngendanwa ihindura instance yawe ya LNbits Umbrel ikaba server nyayo ya Lightning wallet kuri wewe n’abagenzi bawe, mu gihe uguma ufise ubusegaba bwose ku mahera yawe kubera node yawe yitunganije.



### Gusangira uburenganzira bw'ukoresha



Ikoreshwa ry'ingenzi ry'iyi ntunganyo y'abakoresha benshi ni **gusangira ama wallets n'umuryango wawe canke uruziga rwa hafi**. Umaze kurema umukoresha afise wallet yihariye (nk'akarorero "satoshi" mu karorero kacu), urashobora gusangira ayo makuru yo kwinjira n'abagize urugo rwawe wizigira.



**Umutekano wo gushika ku Umbrel**: Gushika ku nkuru yawe ya LNbits kuri Umbrel birakingiwe, kuko bishobora gushikwako gusa :




- Ku rubuga rwawe rwo mu karere** : Abagize urugo rwawe bahuye ku rubuga rumwe rwa WiFi/Ethernet barashobora gushika ku nkuru
- Biciye kuri VPN**: Niwakoresha VPN nka Tailscale itunganijwe kuri server yawe ya Umbrel, abakoresha bemerewe barashobora kuronka uburenganzira bwo gushika kure



Iyi nzira ibiri y'uburinzi (ukwinjira ku rubuga + kwemeza umukoresha) ituma uburyo bwo "Kwemera kurema abakoresha bashasha" butagira akamaro kanini kuri Umbrel. Abantu basanzwe bafise uburenganzira bwo gukoresha urubuga rwawe canke VPN ni bo bonyene bashobora gushika ku rubuga rwo kwinjira.



**Ivyiyumviro bisanzwe**: Ukora konti ya "papa", konti ya "mama", konti ya "ubucuruzi" n'ibindi. Buri munywanyi wese afise umuravyo wiwe wallet, mu gihe yungukira ku bushobozi bwo gusangira bw’uruzitiro rwawe rwa Umbrel. Gusa gusangira izina ry’ukoresha n’ijambobanga - uwukoresha ashobora rero kwifatanya n’igikoresho cose kiri ku rubuga rwawe rwo mu karere canke biciye kuri VPN yawe ya Tailscale. Raba inyigisho yacu yihariye y'umurizo kugira uronke ibindi bisobanuro:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Gutahura ivyagutse biriho



Subira ku kigaragaza ca SuperUser maze winjire ku rutonde rwa "Ivyagutse" biri ku ruhande rw'ibubamfu kugira ngo ubone ibidukikije vyose vy'ivyagutse vya LNbits.



![Extensions disponibles](assets/fr/16.webp)



LNbits itanga urutonde rw'ibintu vyinshi bihindura urugero rwawe mu rubuga rw'ibikorwa vy'umuravyo:





- Igikapu c'umuziki**: Uburyo bw'umuziki bukoreshwa na sats (Ukwishura kwa Spotify)
- Amatike yo gufasha**: Uburyo bwo gufasha bwishyurwa (uronke satss kugira wishure ibibazo)
- TPoS**: Igikoresho co kugurisha gitekanye, gigendagenda c'abaguzi
- Umuyobozi w'abakoresha**: umukoresha ateye imbere n'ubuyobozi bwa wallet (ivyo twamaze gukoresha)
- Ivyabaye**: Ugurisha no kwemeza amatike y'ivyo birori
- LNURLDevices**: Ubuyobozi bw'aho ugurisha, ama ATM, ama switch ahuye
- SMTP**: Gushoboza abakoresha kohereza imeyili no kuronka satss
- Boltcards**: Gutegura amakarata ya NFC yo kwishura
- NostrNip5**: Rema aderesi za NIP5 z'intara zawe
- Splitpayments**: Ugusangira kwishura hagati y'amasakoshi menshi



Igikoresho cose gikoreshwa n’ugukanda rimwe gusa kuri iyi interface. Ivyungura vyerekanwa ko "FREE" ni ubuntu, mu gihe bimwe bimwe biboneka mu buryo bwa "PAID". Raba urutonde kugira ngo umenye izo zihuye n’ivyo ukeneye - haba mu bucuruzi, mu bijanye no kurongora umuryango, canke mu kugerageza ubushobozi bwa Lightning Network.



## Inyungu n'aho bigarukira



**Ivyiza**: Ubusegaba bw’ivy’amahera (ubugenzuzi bwose bw’amahera/imfunguruzo/amakuru), uguhinduranya ubuhinga bw’ubwubatsi (ukwimuka kwa VPS→full node ataco gutakaza), uburyo bwo kwagura ubuhinga, uburyo bwo gukoresha busanzwe.



**Imipaka** : Porogaramu iri muri beta (ukwiyubara ku mahera), umutekano uri munsi y’inshingano y’umuyobozi, URLs zirimwo imfunguruzo za API zihambaye (HTTPS ni ngombwa), uburongozi bw’abakoresha benshi busobanura inshingano yo kubungabunga.



## Ibikorwa vyiza



**Ivyiyumviro**: Ivyemezo vy'Imbuto ya Phoenixd/LND, urutonde rw'amakuru rwa LNbits, amadosiye ya .env. Ikora buri musi, igumye kure ya server, ipfutse. Igerageza rigarukana ubudasiba.



**Gucungera**: Guhora usuzuma ko ata bishasha (LNbits, inyuma y’umuravyo, uburyo bwo gukoresha). Imisi yose suzuma amakuru y’isohorwa imbere y’ivyo guhindura bikomeye.





- Ku Mutaka**: App Store irakumenyesha ubwo nyene ama verisiyo mashasha. Guhuza ivyagutse biciye ku "Gucungera ivyagutse" > "Vugurura vyose". Suzuma SQLite urutonde rw'amakuru rwinjijwe mu Umbrel ububiko bwikora.
- Ku VPS**: Guhindura n'amaboko n'ibice vya cd && git gukurura && uv sync --vyose-vy'inyongera && sudo systemctl gusubira gutangura lnbits`. Gukurikirana inyandiko za sisitemu: `ikinyamakuru ca sudo -u lnbits -f`.



## Iciyumviro



LNbits kwiyakira itanga inzira nyayo y’ubusegaba bw’ivy’ubutunzi bwa Lightning. VPS+Phoenixd itanga umuti woroshe ku bikorwa vyihuta, Umbrel yuzuye n’uruzitiro rwa Bitcoin ruriho. Ubwubatsi bushobora guhindurwa burashoboza gutera imbere kuva ku wallet yoroshe ikoreshwa n’abantu benshi gushika ku bikorwa vy’ubudandaji bikomeye.



Kwiyakira bisigura inshingano: gusubiza inyuma imbuto, kurinda ukuronka, gutangura n’amahera makeyi. Ivyo vyitonderwa, LNbits iba umuti ukomeye w’ubutunzi bwa Lightning, mu gihe izigama ukwegereza ubutegetsi abaturage n’ukwigenga.



## Ubutunzi



### Inyandiko zemewe




- [Inyandiko z'ibice vya LN](inyandiko.ibice vy'inyandiko.org)
- [Ikibanza c'ibice vya LN](ibice vy'ibice/ibice vy'ibice)
- [Ikinyamakuru ca Phoenixd](ubutumwa bwa Phoenixd)
- [Inyigisho yemewe yo gushiramwo](https:



### Abarongozi b'abanyagihugu




- [Imitunganyirize y'intango y'umurongo wa Ubuntu](intambwe-ku-intambwe-y'uburongozi/) na Daniel P. Costas (umutekano wa VPS intambwe ku yindi)
- [Gushiramwo LNbits + Phoenixd kuri Ubuntu VPS](gushiramwo-lnbits-phoenixd-vps-ubuntu/) na Daniel P. Costas (uburongozi bushitse)
- [Serveri ya LNbits kuri Clearnet] (https/Igikoresho c'ibice/ru/) na Axel
- [Ibice vya LN kuri VPS] (Ibice vya LN) na Hannes