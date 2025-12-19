---
name: Mostro
description: KYC-utagira Bitcoin P2P urubuga rwo guhanahana amakuru biciye ku Muravyo na Nostr
---

![cover](assets/cover.webp)



Ni gute uronka canke ugurisha ama bitcoins ataco uhinduye ku busegaba bwawe bw’ivy’ubutunzi? Ivyuma vy’ubuhinga bwa none bishiraho uburyo bwo gukora KYC buteye ubwoba bugaragaza amakuru yawe bwite, n’ubushobozi bwo guhagarika konti yawe canke gucungera Leta.



**Mostro P2P** itanga uburyo bundi bwo gufatanya Lightning Network, umurongo wa Nostr n’amafagitire yo gufata. Igishasha caco gikomeye: uburyo bwo gushiramwo amafaranga yawe aho amafaranga yawe aguma ari munsi y’ububasha bwawe mu kiringo cose c’uguhindura, bikakuraho ingorane zo kwiba, gusenyuka kw’ubucuruzi canke gufatwa ku bushake.



## None Mostro P2P ni iki?



Mostro P2P ni ubuhinga bwo guhanahana amakuru bwa Bitcoin bwakozwe na **grunch**, umuhinga mu bijanye n’ubuhinga bwa Telegram bot **lnp2pbot** bwatangujwe mu 2021. kunanirwa** gushobora gucengera n’intwaro.



Mostro aserukira **iterambere ry’ivyo vyiyumviro ry’abantu benshi**: mu gusubirira Telegram n’umurongo wa **Nostr** (uruja n’uruza rw’imirongo y’amakuru itangazwa), Mostro irakuraho iyo ngorane y’urutonde. Iryo tegeko rifatanya Lightning Network ku bijanye n’ugucuruza ubwo nyene, Nostr ku bijanye n’uguhanahana amakuru adashobora gucengera, na **gufata amafagitire** kugira ngo haboneke ubuhinga bwo gucungera amafaranga vy’ukuri butagiramwo ububiko.



### Ubwubatsi bw'ubuhinga



Mostro akora biciye mu bice bitatu:




- Daemon Mostrod**: ahuza ibiganiro hagati y’abakoresha na Lightning Network.
- Umuravyo** node: irema amafagitire yo gufata (~24h escrow y'ibanga)
- Abaguzi ba Mostro**: imirongo y'abakoresha (CLI, Telefone ngendanwa, Urubuga)



Amategeko asohorwa kuri Nostr nk’ibintu vya bose (ubwoko 38383), mu gihe ubudandaji bw’abantu ku giti cabo burungikwa biciye ku butumwa bushingiye ku mpera kugeza ku mpera (NIP-59, NIP-44). Instance ya Mostro yose isobanura amafaranga yayo (muri rusangi hagati ya 0,3% na 1%) n’imipaka y’ugucuruza (kuva ku bihumbi bikeyi gushika ku bihumbi amajana vyinshi vya sats, bivanye n’instance).



### Inyungu zifata ingingo



**Ishobora guhangana n’ugucengera**: Nta leta ishobora gufunga Mostro igihe cose ama relays ya Nostr azoba ariho ahantu kanaka kw’isi. Udakunze lnp2pbot ishobora gushikirwa n’ingorane biciye kuri Telegram, Mostro yemera guhanahana amakuru **bidashobora gucengera**.



**Escrow non-custodial**: Amafagitire y’umuravyo afunga ama bitcoins yawe ataco uyarungitse ubuziraherezo. Amahera yawe aguma ari munsi y’ububasha bwawe kandi agasubirwamwo ubwo nyene iyo habaye ingorane (~24h).



**Ibanga kubera umugambi**: Uburyo bubiri buraboneka kugira ngo bujane n’ivyo ukeneye. Uburyo bw’Izina** buhuza izina ryawe n’urufunguzo rwawe rwa Nostr kugira ngo wubake ukwizigira kuramba. Uburyo bwihariye bushitse** bukunda kutamenyekana n'imfunguruzo z'igihe gito zikoreshwa rimwe.



## Ibirango nyamukuru



**Imenyekanisha ry’abantu bose**: Amategeko yose asohorwa kuri Nostr biciye ku bikorwa vyashizweko umukono mu buryo bw’ibanga. Ivyiyumviro vy’abantu ku giti cabo birungikwa biciye ku butumwa bushingiye ku mpera kugeza ku mpera, bikaba vyemeza ko haba ibanga ryose.



**Uburyo bw’izina**: Inyenyeri 5 n’ibara ry’isubiramwo ribitswe ubudasiba kuri Nostr. Biguha uburenganzira buhoro buhoro kwubaka izina nk’umucuruzi wo kwizigirwa.



**Ubukemurampaka bushingiye ku ntara**: Iyo habaye impaka, umukemurampaka atagira aho abogamiye asuzuma ibimenyamenya agafata ingingo ashingiye ku ngingo ziboneka. Buri ntambara ivyara token yihariye kugira ngo umuntu ashobore gukurikirana.



**Uguhindura amafaranga**: Gushigikira amafaranga menshi ya fiat biciye ku nzira y’uguhindura amafaranga yadio.io. Yemera amafaranga yoherezwa na SEPA, PayPal, Revolut, amafaranga, n’uburyo bwose bwemejwe hagati y’ababiri.



## Abakiriya ba Mostro barahari



Mostro itanga abakiriya babiri b’ingenzi bakora ku bijanye n’uguhindura kwawe kwa P2P.



### Mostro CLI - Umukiriya w'umurongo w'itegeko



**Mostro CLI** ni umukiriya akuze kandi akora cane. Yanditswe muri Rust, itanga urutonde rw’ibintu vyose vya Mostro biciye ku nzira y’amabwirizwa. Ihuye na macOS, Linux na Windows.



**Ivy'ingenzi bigenzura** :




- `abarongozi`: Erekana amategeko yose ariho
- `neworder` : Rema itegeko rishasha ryo kugura canke kugurisha
- `gufata` / `gufata kugura`: Gufata canke kugurisha itegeko
- `fiatsent`: Kwemeza kohereza kwishura kwa fiat
- `rekura`: Rekura escrow maze uheze guhindura
- `getdm`: Reba ubutumwa butaziguye
- `igiciro` : Suzuma uwo mufatanije inyuma y'uguhinduranya



Ni vyiza ku bakoresha ubuhinga, ubuhinga bwo kwikoresha n’ibidukikije bisaba umutekano mwinshi.



### Mostro telefone ngendanwa - Porogaramu ya telefone ngendanwa



**Mobile app** iri muri verisiyo ya alpha irashoboza gucuruza P2P uhereye kuri telefone yawe. Igishushanyo gisanzwe Interface gifise ubuhinga bwo kugendagenda, kuraba amategeko, amayunguruzo ateye imbere n’ibiganiro vyinjijwe kugira ngo uvugane n’abo mukorana.



Iboneka kuri **Android** (biciye kuri APK kuri GitHub), ni ihitamwo ryiza ku bakoresha bakunda ukworohereza no gucuruza rimwe na rimwe kuri telefone ngendanwa.



### Urubuga rwa Mostro - Urubuga rwa Interface (ruriko rurategurwa)



Interface urubuga rwa JavaScript ruteye imbere ruriko rurategurwa. Igenewe gutanga ubumenyi bushitse bw’abakoresha n’ubudandaji bwinshi n’imikorere y’uburongozi bw’ibiharuro. Ushobora gushikako biciye ku mucukumbuzi ata gushiramwo bisabwa.



## Gushiramwo no gutunganya



Iyi nyigisho izoguyobora mu gushiramwo no gukoresha abakozi babiri bakuru ba Mostro: CLI na porogarama yo kuri telefone ngendanwa.



### Ibisabwa vy'ingenzi



Imbere y'uko utangura, uzokenera :





- Lightning Network** wallet ikora ifise amahera ahagije (canke ihuye n’umuravyo)
 - Ivyiza: Phoenix, Umuyaga, Wallet ya Satoshi...
 - Nibura amasatoshi 1000 y'amahera yo kugerageza



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Urufunguzo rwihariye rwa Nostr** (imiterere `nsec1...`)
 - Rema urufunguzo rw'ubudandaji rwihariye kuri [nostrkeygen.com](https://nostrkeygen.com/)
 - Ivy'ingenzi**: Ntukigere ukoresha urufunguzo rwawe rwa Nostr
 - Bika urufunguzo rwawe rw'ibanga ahantu heza (umucungerezi w'ijambobanga)





- Ihitamwo ariko ni ngirakamaro**: VPN canke Tor guhuza kugira ngo upfuke aderesi yawe ya IP



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Gushirwaho kwa Mostro CLI



#### Ku macOS



**Intambwe ya 1: Rust igenzura**



Suzuma ko Rust yashizweho (verisiyo 1.64+ irakenewe):



```bash
rustc --version
```



Niba Rust itashizweho :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Intambwe ya 2: Gukora clone y'ububiko**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Intambwe ya 3: Gutunganya**



Kopa kandi uhindure :



```bash
cp .env-sample .env
```



Gufungura `.env` maze utunganye amagenamiterere yawe:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Igihambaye ku bijanye n’uguhuza CLI/Mobile**: Kugira ngo ushikire amategeko amwe kuri CLI no kuri app ya telefone ngendanwa, utegerezwa gukoresha **Mostro Pubkey imwe** na **relays za Nostr imwe** muri abo bakiriya bompi. Suzuma ivyo bintu mu Mirongo iri kuri porogarama ya telefone ngendanwa.



![Configuration .env](assets/fr/02.webp)



**Intambwe ya 4: Gushiramwo**



Gukoranya no gushiramwo CLI :



```bash
cargo install --path .
```



Gukoranya bifata iminota 1-2. Ivyo `mostro-cli` bizoshirwa muri `~/.imitwaro/ibinogo/`.



![Installation du CLI](assets/fr/03.webp)



**Intambwe ya 5: Suzuma**



Suzuma ko vyose bikora:



```bash
mostro-cli --help
```



Ushobora kubona urutonde rw’amategeko yose.



![Vérification avec --help](assets/fr/04.webp)



#### Kuri Linux (Ubuntu/Debiyani)



Gushiramwo bisa na macOS, vyongeweko :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Hanyuma ukurikize intambwe ya 3 na 4 mu gice ca macOS.



#### Ku madirisha



Mbere na mbere ushiremwo Rust biciye kuri [rustup.rs](https/rustup.rs/), hanyuma ukoreshe PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Itunganywa rimwe: kopira `.env-sample` kuri `.env` maze wuzuze amaparametere yawe.



### Gushiramwo telefone ngendanwa ya Mostro



#### Kuri Android



**Intambwe ya 1**: Genda kuri [paji y’ibisohoka vya GitHub] maze ushireko dosiye **app-release.apk** (nk’ibilometero 65).



![Page GitHub Releases](assets/fr/10.webp)



**Intambwe ya 2: Iyo umaze gukuraho, fungura dosiye APK muvyo washizeko. Android izogusaba kwemerera gushiramwo ibintu bivuye kuri iyi nzira.



![Téléchargement et installation APK](assets/fr/11.webp)



**Intambwe ya 3**: Kurikiza amashusho yo kwinjira mu ndege, yerekana ibikorwa:




- Gucuruza Bitcoin mu mwidegemvyo - nta KYC** : Gucuruza ata kugenzura akaranga kubera Nostr
- Ubuzima bwite ku buryo busanzwe**: Hitamwo hagati y'uburyo bw'icubahiro n'uburyo bw'ubuzima bwite bushitse
- Umutekano ku ntambwe yose**: Uburinzi n'amafagitire atagira ububiko



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Intambwe ya 4**: Bandanya winjira mu bwato kugira ngo ubone :




- Ikiganiro gipfutse neza**: Uguhanahana amakuru gupfutse kuva ku mpera kugeza ku mpera
- Fata igiciro**: Suzuma igitabu c'amategeko maze uhitemwo igiciro
- Ntushobora kuronka ivyo ukeneye?** : Rema urutonde rwawe



![Suite onboarding](assets/fr/13.webp)



**Intambwe ya 5: Iyo onboarding irangiye, app ica itanga imfunguruzo zibiri za Nostr. Genda kuri menu (☰) hanyuma **Account** kugira ubike **Amajambo y'Ibanga** yawe (ijambo ryo gusubirana). Ni kuri iyi screen kandi ufise uburenganzira bwo guhindura uburyo bw’ubuzima bwite bwavuzwe imbere.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Igihambaye**: Andika ijambo ryawe ryo gukira ahantu hatagira umutekano (umucungerezi w’ijambobanga, impapuro zitekanye).



### Imiterere y'umutekano yambere



Uko ukoresha urubuga urwo ari rwo rwose :





- Urufunguzo rwihariye**: Koresha akaranga ka Nostr katandukanye ku bucuruzi
- Amafaranga make**: Tangura n’amahera ari munsi ya sats 10.000 kugira ngo utangure
- Ivyuma vyinshi**: Gutegura ivyuma 3-5 bitandukanye mu karere
- Uburinzi bw'urubuga**: Gukoresha VPN canke Tor kugira ngo uhishe aderesi yawe ya IP
- Wallet itekanye**: Gukoresha ugufunga kwihuta kw'umuravyo wawe wallet



## Koresha na CLI



Iki gice kirerekana ugugura amafaranga y’ama bitcoins biciye kuri Mostro CLI hakurikijwe ivy’ugukoresha mu buzima nyakuri.



### Intambwe ya 1: Gutanga urutonde rw'amategeko ariho



Itegeko rya `listorders` ryerekana amategeko yose akora:



```bash
mostro-cli listorders
```



Uzobona imbonerahamwe irimwo amakuru y’itegeko ryose: ID, ubwoko (ugugura/kugurisha), umubare, amafaranga, uburyo bwo kwishura.



![Liste des ordres disponibles](assets/fr/05.webp)



Muri aka karorero, itegeko ryo kugurisha amayero 5 biciye kuri Revolut riraboneka (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Intambwe ya 2: Gufata itegeko



Kugira ngo ugure aya mafaranga, fata itegeko na `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro azogusaba gutanga **invoice y'umuravyo** kugira ngo ubone BTC. Igitigiri nyaco kiri mu masatoshi kiragaragazwa (aha: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Intambwe ya 3: Tanga invoice yawe y'umuravyo



Gutanga inyemezabuguzi y'umuravyo kuva kuri wallet yawe (Phoenix, Breez, n'ibindi) ku giciro nyaco, hanyuma uyirungike :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Uwo murongo wemeza ivyo wohereje maze ukakubwira ngo urindire ko uwugurisha ariha invoice y’uguhagarika imbere y’uko ukoresha iyo escrow.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Intambwe ya 4: Baza uwugurisha



Igihe escrow imaze gukoreshwa, koresha `dmtouser` kugira ngo usabe amakuru y'ukwishyura ku mugurisha:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Intambwe ya 5: Gutora inyishu



Suzuma ubutumwa butaziguye kugira ngo ubone inyishu y'umugurisha:



```bash
mostro-cli getdm
```



Uwugurisha aguha ID yiwe yo kwishura (aha Revtag yiwe: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Intambwe ya 6: Gutanga amahera ya fiat



Wohereze amahera biciye ku buryo mwemeranije (Revolut muri aka karorero) ku makuru yo guhamagara yatanzwe. **Bika inyandiko zose zishigikira** (amafoto, ibimenyetso vy’ibikorwa).



### Intambwe ya 7: Wemeze ko wishuye



Igihe umaze kwishura, umenyeshe Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Intambwe ya 8: Kwakira ama bitcoins



Uwugurisha akimara kwemeza ko yakiriye fiat maze akarekura escrow n’itegeko rya `release`, ubwo nyene uraronka bitcoins zawe ku nsiguro y’umuravyo watanze.



### Intambwe ya 9: Gusuzuma



Gupima umuguzi kugira ngo agire ico aterereye ku ruhara rwiza:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Amabwirizwa ngirakamaro



**Gukuraho itegeko** (mbere y'uko rifatwa) :


```bash
mostro-cli cancel -o <order-id>
```



**Rema urutonde rushasha rwo kugurisha** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Gufungura impaka** :


```bash
mostro-cli dispute -o <order-id>
```



## Koresha na porogaramu ngendanwa



Iki gice kirerekana ugurisha amafaranga y’ama bitcoins biciye kuri Mostro Mobile mu gukurikirana uburyo bwo gukoresha amafaranga nyakuri.



### Interface nyamukuru



Porogaramu ifise uturongo 3:





- Igitabo c'amategeko**: Suzuma amategeko ariho yo kugura (GURISHA BTC) no kugurisha (GURISHA BTC)
- Ubucuruzi bwanje**: Raba amategeko yawe akora n'aya kera
- Chat**: Vugana n'abo mukorana ukoresheje imibare



![Interface principale](assets/fr/14.webp)



### Itunganywa ry'impanuro



Imbere yo gucuruza, ushireho ibintu bikeyi biciye ku rutonde (☰) > **Ivyagezwe** :





- Umuravyo Address** (ntibikenewe): Kugira ngo uronke amahera ataco uhinduye
- Ivyuma**: Wongereko ivyuma vyinshi vya Nostr kugira ngo ushobore kwihangana (nk'akarorero `wss://nos.lol`, `wss://ivyuma.damus.io`)
- Mostro Pubkey**: Suzuma urufunguzo rwa bose rw'inkuru ya Mostro uriko urakoresha



![Paramètres de l'application](assets/fr/16.webp)



**Igihambaye ku bijanye n’uguhuza CLI/Mobile**: Niba ukoresha CLI na app ya telefone ngendanwa, ushireho **ivyo nyene Nostr relays na Mostro Pubkey** muri abo bakiriya bompi. Ata n'iyi ntunganyo isa, ntuzobona amategeko amwe aboneka ku nzira zompi. Ivyo bikoresho na Mostro Pubkey biboneka mu Mitunganyirize (ifoto iri hejuru) bitegerezwa guhura n'ivyo muri dosiye yawe ya CLI `.env'.



### Intambwe ya 1: Rema itegeko ryo kugurisha



Kanda buto y'icatsi kibisi **"+"** iri hasi iburyo, hanyuma uhitemwo **GURISHA** (ubuto butukura).



![Boutons de création d'ordre](assets/fr/17.webp)



Uzuza urupapuro rw'irema :



1. **Ifaranga**: Hitamwo amafaranga wipfuza kwakira (EUR, USD, n’ibindi)


2. **Igiciro** : Shiramwo igiciro mu fiat (nk'akarorero 1 gushika kuri 3 EUR)


3. **Uburyo bwo kwishura** : Hitamwo uburyo (nk'akarorero "Revolut")


4. **Ubwoko bw'igiciro**: Hitamwo "Igiciro c'isoko".


5. **Igiciro**: Guhindura igiciro (guhindura kuva kuri -10% gushika kuri +10%, ni vyiza: 0% kugira ngo ugurishe vuba)



Kanda **Submit** kugira ngo utangaze itegeko ryawe.



### Intambwe ya 2: Kwemeza gusohoka



Itegeko ryawe ryasohotse ubu! Izomara amasaha 24. Ushobora kuyikuraho igihe cose imbere y'uko umuguzi ayifata mu gushitsa itegeko rya `cancel`.



![Ordre publié](assets/fr/18.webp)



Urutonde ruboneka mu **Ubucuruzi bwanje** rufise ikibanza "Ritegerejwe" n'ikimenyetso "Waremwe nawe".



### Intambwe ya 3: Umuguzi afata ivyo wasavye



Iyo umuguzi afashe ivyo wasavye, uraronka itangazo. Raba ido n'ido muri **Ubucuruzi bwanje**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Ivyigwa bihambaye**: Ubu utegerezwa **kwishura invoice y’ugufata** yerekanwa kugira ngo ufunge amafaranga yawe (aha 4674 sats ku 1-5 EUR) mu escrow. Ufise **iminota 15 maximum** ahandi ho uguhindura bizosubirwamwo.



Kopa invoice y’uguhagarika maze uyihe ukoresheje wallet yawe y’umuravyo (Phoenix, Breez, n’ibindi).



### Intambwe ya 4: Vugana n'uwuguze



Igihe escrow imaze gukora, kanda **CONTACT** kugira ngo ufungure ikiganiro gipfutse n’umuguzi.



Uwuguze (aha "anonyme-gloriaZhao") azoguhamagara kugira ngo akubwire amakuru y'ukwishura kwawe. Ndagusavye wishure n'amakuru yawe (Revtag, IBAN, n'ibindi).



![Chat avec l'acheteur](assets/fr/20.webp)



### Intambwe ya 5: Kwakira amahera ya fiat



Rindira gushika ubonye amahera ya fiat muri konti yawe ya Revolut (canke ubundi buryo mwemeranije). **Suzuma neza**:




- Igitigiri nyaco
- Uwohereje
- Ivyerekeye iyo bisabwe



Uwuguze azokumenyesha biciye kuri chat ko yohereje amahera. Mostro izokwerekana kandi ubutumwa bwemeza ko fiat yagurungikiye.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Intambwe ya 6: Rekura ivy'ububiko



Uhejeje **kwemeza ko wakiriye** amahera ya fiat kuri konti yawe, ukande kuri buto y'icatsi kibisi **RELEASE** hanyuma wemeze ko woherereje satss ku muguzi.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoins zica zirungikwa ku muguzi biciye ku nsiguro yiwe y’umuravyo.



### Intambwe ya 7: Suzuma ivyo wihweza



Inyuma yo gusohoka, kanda **RATE** kugira ngo ushiremwo umuguzi. Hitamwo kuva kuri 1 gushika ku nyenyeri 5 (aha 5/5) hanyuma ukande **Submit Rating**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Ivyo guhinduranya biraheze!



### Gura ama bitcoins ukoresheje porogaramu ya telefone ngendanwa



Inzira yo **kugura** ama bitcoins ni nk’iyo ariko irahinduka:



1. Suzuma **Igitabo c'amategeko** > **GUGURA BTC** kugira ngo ubone amategeko y'ugurisha


2. Fyonda ku rutonde rushimishije kugira ngo ubone ido n'ido


3. Kanda **Fata itegeko**


4. Tanga invoice yawe y’umuravyo (yavuye muri wallet yawe)


5. Rindira ko uwugurisha akoresha escrow


6. Baza uwugurisha uciye kuri **CONTACT** kugira ngo umenye uko wokwishura


7. Wohereze fiat amahera (bika ikimenyamenya)


8. Uwugurisha arekura escrow inyuma yo kugenzura


9. Uronke ama bitcoins ubwo nyene ku giciro cawe c'umuravyo


10. Tanga igiharuro ku bagurisha (inyenyeri 1-5)



### Gucungera ingorane



**Gukuraho itegeko**: Mu **My Trades**, ukande itegeko ryawe hanyuma ukande kuri buto ya **CANCEL** (iraboneka gusa imbere y'uko rifatwa).



**Gufungura impaka**: Iyo habaye ukutumvikana, kanda **IMPAKARA** mu ndondoro y'urutonde. Shirako ibimenyamenya vyose (amafoto y'ibiganiro, ibisobanuro vy'ibikorwa vya banki).



## Inyungu n'aho bigarukira



### Inyungu



**Ubusegaba bw’ivy’amahera**: Ama bitcoins yawe ntazokwigera ava mu bubasha bwawe butaziguye kubera uburyo bwo gufata invoice, bikuraho ingorane zo gusenyuka kw’amahera canke ubusuma bw’amahera.



**Censor-resistant**: Nta butegetsi bushobora gufunga urubuga canke gucengera amategeko yawe. Uwo murongo urakora igihe cose amarelay ya Nostr ariko arakora.



**Ukumenyekana kw’izina ryawe**: Urufunguzo rwa Nostr rw’izina ry’uruyeri ni rwo rwonyene rukumenya, ata KYC canke amakuru y’ibanga. Ivy’itumanaho ry’iherezo kugeza ku mpera.



**Uguhinduranya ukwishura**: Uburyo bwo kwishura bwose bwemejwe burashoboka (uguhindura, gukoresha ama apps kuri telefone ngendanwa, amahera, guhinduranya).



### Ivyo bigarukira



**Iterambere ry’imbere**: Ivyigwa vy’intango n’inyigisho z’ubuhinga bisabwa.



**Ivyuma bifise aho bigarukira**: Umubare muto w’amategeko, cane cane ku mafaranga menshi canke amafaranga adasanzwe.



**Ibisabwa mu vy'ubuhinga**: Gutahura ivy'ishimikiro ku vyerekeye Lightning na Nostr birakenewe.



**Inshingano y’umuntu ku giti ciwe**: Nta nkunga ihuriweko iyo habaye ingorane, birakenewe kwiyubara.



## Iciyumviro



Mostro P2P iserukira ubundi buryo bwiza bwo guhindura amafaranga y’ubudandaji, ihuriza hamwe Lightning Network, Nostr n’ubudandaji bwikora kugira ngo ubucuruzi bushizwe ahantu hamwe vy’ukuri. Naho yateguwe vuba kandi ikaba ifise amahera make, iyo nzira irasanzwe itanga ubusegaba bw’ivy’ubutunzi, ukurwanya ugucengera n’ukutamenyekana.



Ku ba bitcoiners bakunda kwigenga n’ibanga, Mostro ni uburyo bushoboka bukwiye gutohozwa butera imbere. Ubwubatsi bwayo bushizwe ahantu hamwe buratanga icemezo c’iterambere ry’abanyagihugu aho gutera imbere mu vy’ubudandaji, bikaba vyemeza inzira y’akazoza k’uguhinduranya Bitcoin ku buntu vy’ukuri.



## Ubutunzi



### Inyandiko zemewe




- [Urubuga rwemewe rwa Mostro](urubuga rwa Mostro)
- [Inyandiko z'ubuhinga](https://mostro.urubuga/inyandiko-icongereza/urutonde.html)
- [Ishirahamwe rya Mostro](https://ishirahamwe rya Mostro)



### Kode y'inkomoko n'iterambere




- [Ububiko nyamukuru bwa GitHub](imbuga ngurukanabumenyi)
- [Umukiriya w'urubuga](github.com/MostroP2P/urubuga-mostro)
- [Umukiriya CLI](imbuga ngurukanabumenyi)



### Umugyango




- [Itegeko rya Nostr](urubuga rwa nostr.com)
- [Inyigisho za Lightning Network](https://umuravyo.urubuga)