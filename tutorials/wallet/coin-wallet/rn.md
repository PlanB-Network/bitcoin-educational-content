---
name: Coin Wallet
description: Inyigisho yerekeye Coin Wallet n'uburyo bwo kwongereza ubuzima bwite n'umutekano
---

![cover](assets/cover.webp)


Iyi nyigisho ivuga kuri [Coin Wallet](https://coin.space/) - ubuhinga bwo kwikingira wallet ku bikoresho vy’amaboko, n’ingene wokwongerera umutekano n’ubuzima bwite igihe ukoresha porogarama za wallet zigendanwa.



## Ivyerekeye Coin Wallet.


**Coin Wallet** ni porogaramu yigenga / idashobora kwizigamira, ifunguye, yakozwe n’umugwi w’abakunzi ba Bitcoin mu 2015. Yatanguye nk’iporogarama y’urubuga, ikurikirwa n’iporogarama ya iOS mu 2017, n’iporogarama ya Android mu 2020 kuri Google Play, Samsungla Stoy, iraboneka Ingoro y'Ibikoresho.


Inyungu nyamukuru:


- Ubwubatsi butajanye n'ububiko
- Mu buryo bushitse [kode y'inkomoko yuguruye](https://github.com/Ikibanza c'Igiceri/Ikibanza c'Igiceri/blob/umukuru/URUHUSHA)
- Igishushanyo coroshe kandi gisukuye
- Yibanze ku ntumbero nyamukuru - kubika neza amafaranga y'ibanga, ata bintu bidakenewe
- Gushigikira imbuga zitandukanye: telefone ngendanwa (iOS na Android), mudasobwa, urubuga
- RBF (Gusubiriza-N'amafaranga) gufasha - kwihutisha amafaranga afashe igihe cose
- Ivyuma 2FA bifise [Urufunguzo rwa Yubi] (bikorana-na-urufunguzo rwa Yubi/urutonde/igiceri-wallet/) / Urufunguzo rwa FIDO2
- Infashanyo ya Tor yubatswemwo – inzira y'uruja n'uruza rwose biciye ku rubuga rwa Tor kugira ngo ubone ubuzima bwite



## 1️⃣ Gushiramwo Coin Wallet

Coin Wallet iraboneka ku mbuga zose zikomeye.



- [Iduka ry'amaporogarama ya iOS](iporogarama.



- [Urukino rwa Google](urukino.google.com/ububiko/porogaramu/ibisobanuro?id=com.ikibanza c'amafaranga.porogaramu)



- [Android (Iduka ry'Inyenyeri)](ububiko bw'Inyenyeri.samsung.com/Ibisobanuro/Iduka ry'Inyenyeri.



- [Android (Ikibanza c'Ibikoresho vya Huawei)](Ikibanza c'Ibikoresho vya Huawei)



- [Android (Ugushika Hasi)](Igiceri-wallet.ru.Gushika Hasi.com/Android)



- [APK ya android](ibiceri.ikibanza/api/v3/gukuraho/apk-ya android/ikintu cose)



- [Ihuza ryose ry'isohoka](https://github.com/Ikibanza c'Igiceri/Ikibanza c'Igiceri/ibisohoka)


Ishobora kandi gukoreshwa kuri mudasobwa (Windows, Linux, macOS), nk’urubuga rwo ku rubuga no kuri Tor.


![image](assets/en/01.webp)


## 2️⃣ Gukora Wallet no gushinga PIN


wallet iremwa hakoreshejwe passphrase – urutonde rw’amajambo 12 atandukanijwe n’ibibanza, ruvuye mu [urutonde rw’amajambo 2048]

Coin Wallet ifasha amajambo y’ibanga y’amajambo 12, 15, 18, 21 canke 24 yashizwe mu bindi bikoresho.


passphrase ni uburyo umuntu ashobora gusoma bw’urufunguzo rw’ibanga rwa mbere. Bitegerezwa gukizwa ata nkomanzi. passphrase ni vyo vyose bikenewe kugira ngo umuntu ashobore gushika canke asubizeho wallet. Iyo passphrase itakaye, wallet n’amahera yose biratakara ubuziraherezo. passphrase ntitegerezwa kwigera isangira. Coin Wallet ntibika imfunguruzo kuri server iyo ari yo yose canke ku rutonde rw’amakuru.


**Mbega passphrase y'amajambo 12 iratekanye?**

Kubera amajambo 2048 ashoboka kuri buri kibanza, hariho 204812 ≈ 1039 imigwi — itanga ~128 bits z'umutekano, zigereranywa n'imfunguruzo z'ibanga za Bitcoin. Uwo murongo ubonwa cane ko uhagije.


![image](assets/en/02.webp)


Inyuma y’aho passphrase yanditswe kandi yemejwe, iyo porogarama isaba gushinga **PIN** y’imirongo 4 kugira ngo umuntu ashobore kuyironka buri musi. Kugira ngo bibe vyiza cane, urashobora gukoresha ubuhinga bwo kwemeza umuntu (ugutahura urutoke canke mu maso) aho gukoresha PIN.


![image](assets/en/03.webp)



Nta konti, nta gusubirana kw’urufunguzo, nta gusubiramwo passphrase, kandi nta guhindura amafaranga. Umutekano ni inshingano y’uwukoresha.


Kugira ngo ubone ingene wozigama ijambo ry'ikirundi:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Ijambo ry'ibanga + PIN. Igihe Bikoreshwa n’Uko Bikoreshwa .


**passphrase isabwa ryari?**

Muri ivyo bihe bidasanzwe gusa:


- Gushinga wallet ku gikoresho gishasha
- Gusubira gushiramwo porogaramu Coin Wallet
- Gukuraho amakuru ya porogaramu/umucukumbuzi (Ububiko bwo mu karere)
- Gukuraho urufunguzo rw'ibikoresho kuri konti
- Kwinjiza PIN mbi incuro zitatu (porogaramu irafunga kubera umutekano)


Mu gukoresha buri musi, PIN y'imirongo 4 irahagije kugira ngo ufungure wallet.


**Ijambobanga + PIN: Uko bikora**

passphrase ni urufunguzo rw’ibanga rw’ukuri kandi rukora ku gikoresho cose.

Kubera ko kwandika amajambo 12–24 igihe cose vyoba bigoye, Coin Wallet ikoresha PIN y’imirongo 4 kugira ngo umuntu ashobore gushika ku gikoresho kiriho ubu.

PIN yoroshe yonyene ntitekanye bihagije kugira ngo ikingire urufunguzo nyamukuru ataco ihinduye, rero ntiyigera ikoreshwa mu gupfuka. Aho:



- PIN yoherezwa kuri server maze igahindurwa n'ibara rirerire ry'ibanga token.
- Iyi token irafungura urufunguzo nyamukuru rwashizwe mu mfuruka rwabitswe ku gikoresho gusa.


Iyo PIN yinjijwe nabi incuro zitatu, server irafuta burundu token. Urufunguzo rwabitswe aho hantu ntirushobora gukoreshwa, kandi uburyo bwonyene bwo kugarura wallet ni ukwinjiza passphrase y'umwimerere.

Iyi design itanga uburyo bwo gusubira inyuma be n’uburinzi bukomeye bwo gusubira inyuma.



## 4️⃣ Kwakira ₿itcoin - Ubwoko bwa Address n'ubuzima bwite


Coin Wallet ishigikira uburyo bwose butatu bwa aderesi za Bitcoin:



- SegWit y’imvukira (Bech32)** – itangura na **bc1q** – amafaranga make cane, ni vyiza
- Igihugu-53 (P2SH)** – gitangura na **3**
- Iragi (P2PKH)** – ritangura na **1**


![image](assets/en/04.webp)


**Kubera iki aderesi ihinduka inyuma y'ugushiramwo amahera yose?**

Ivyo ni ibigamije kandi birinda ubuzima bwite. Igihe cose ibiceri vyakiriwe, Coin Wallet ica itanga aderesi nshasha idakoreshwa. Iyo iyo aderesi nyene yongera gukoreshwa (nk’akarorero, ku mushahara w’ukwezi), umuntu wese yoshobora gucapura mu buryo bworoshe amafaranga yose yinjira ku rubuga rwa blockchain maze akamenya amafaranga yose yinjira.


Aderesi za kera ziguma zikora ibihe vyose – urashobora kuzironka – ariko gukoresha aderesi nshasha igihe cose ni uburyo bwiza bwo gukingira ubuzima bwite.


**Uko woronka Bitcoin:**

1. Gufungura igiceri

2. Kanda kuri **Kwakira**

3. Hitamwo ubwoko bw’aderesi wipfuza (vyiza ni **bc1q** – `Igihugu SegWit`)

4. Erekana kode ya QR canke ukope aderesi maze uyirungikire uwuyitanga .


**Ihitamwo - Mecto (ku kwishura umuntu):**

Kuri iyo nkuru nyene y'ukwakira hariho ubuto `Mecto`.

Iyo uyifunguye:


- Uzosabwa kwinjiza **izina ry'ibanga** (gravatar)
- Aho uri ubu + aderesi y'ukwakira irasangizwa n'abandi bakoresha Coin Wallet na bo nyene bafise Mecto
- Bashobora kukuvumbura ku ikarata ntoyi maze bakagurungika ibiceri batanditse canke ngo babikoreshe .


Amakuru aboneka ku bandi bakoresha Mecto gusa kandi aca asubirwamwo inyuma y’isaha 1 (canke ubwo nyene iyo uyazimye).

Mecto ni ubusabe bwose – uyireke nimba ushaka ubuzima bwite bwinshi.


![image](assets/en/05.webp)


## 5️⃣ Kurungika ₿itcoin


Kugira ngo wohereze Bitcoin:


1. Fungurira igiceri → ukande kuri **Ohereza**

2. Shira aderesi canke scanner kode ya QR

3. Shiramwo umubare (canke ukande kuri **Max**)

4. Hitamwo umuvuduko wo gucuruza:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Wemeze ukoresheje PIN yawe y'imirongo 4 → amafaranga yawe aratangazwa


### Uko wokwihutisha ugucuruza ₿itcoin (RBF)


Niwaba wahisemwo amafaranga atevye kandi amafaranga y'ugucuruza akaguma:


1. Genda kuri **Amateka** tab

2. Kanda ku gicuruzwa kirindiriwe

3. Kanda **Kwihutisha** (Subiriza-N'amafaranga)

4. Wemeze → igikorwa kizosubira gutangazwa n’amahera menshi


RBF kwihutisha ubu birashigikiwe:

Bitcoin • Igihuhusi • Uruzitiro rw'ubwenge rwa Binance • Ethereum • Ethereum ya kera • Polygon


Ibindi ku vyerekeye Replace-by-fee (RBF): Ibiganiro/gusubirira-n'amahera/


## 6️⃣ Gusohora imfunguruzo z'ibanga


**Ni ryari mu vy'ukuri ukeneye urufunguzo rw'ibanga?**

(99 % vy’abakoresha ntibagira ico bakora — amajambo 12 passphrase arahagije)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Uko worungika hanze imfunguruzo z'ibanga muri Coin Wallet


1. Gufungura **Bitcoin (BTC)**

2. Genda hasi kuri paji - ukande kuri **Sohora imfunguruzo z'ibanga**

3. Iyi app yerekana aderesi yose ifise balance + urufunguzo rwayo rw’ibanga mu buryo bwa **WIF** (itangura na 5, K, canke L) na code ya QR.


Aderesi zitari ubusa ni zo zonyene ziboneka.


**Urufunguzo rwa WIF rw'akarorero**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k`


**Ico wokora hanyuma (ni vyiza)**


- Gufungura Electrum, Sparrow, igikapu c'ubururu canke ibikoresho vyose wallet
- Injira/Kubura urufunguzo rwihariye
- Amahera yose aca ahita aja ku yindi nzira nshasha itekanye iri munsi ya seed yawe y’ubu.


Ntukigere ubika urufunguzo rw’ibanga mu buryo bwa digitale mu nyandiko rusangi. Amaze gukubura, arashobora gukurwaho ata nkomanzi.


Kugira ngo ubone ubuyobozi bushitse ku mfunguruzo z’ibanga n’inzira z’ugukomokako: [Uko wokorana n’imfunguruzo z’ibanga: Inyobora y’iherezo](https://coin.space/ingene-wokorana-n’imfunguruzo-z’ibanga-uburongozi-bw’iherezo/)



## 7️⃣ Ivyerekeye ubuhinga – BIP39, BIP32 n’inzira z’ugukomoka


Coin Wallet ikurikiza cane ingingo ngenderwako za Bitcoin zikoreshwa hafi n’amasakoshi yose akomeye.


`BIP39` - ingene passphrase iba urufunguzo rw'ibanga


- Umubare w'amajambo mburabuzi: 12
- Amahitamwo passphrase/ijambobanga: nta ("")
- Entropie y'intango: ibice 128 (amajambo 12) → ibice 256 (amajambo 24)
- Gushirwa mu ngiro kw'inkomoko yuguruye:
- Urutonde rw'amajambo: urutonde rw'icongereza rusanzwe rw'amajambo 2048
- Ishigikira kwinjiza amajambo 12, 15, 18, 21 na 24 avuye mu yindi BIP39 wallet yose


`BIP32 + BIP44/BIP49/BIP84` - guhingura amaderesi yose

Kuva ku rufunguzo rumwe rwa mbere, wallet irashobora generate amamiliyaridi y’amaderesi mu buryo butomoye. Ni co gituma ayo majambo 12 nyene yinjijwe muri Electrum, Sparrow, Trezor, Ledger, BlueWallet, n’ayandi azokwerekana neza na neza aderesi n’imibare imwe.


**Inzira z'inkomoko zakoreshejwe muri Coin Wallet ku Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Imbere muri buri nzira:


- `/0` — uruhererekane rw'inyuma (amaderesi werekana kugira ngo uronke amahera)
- `/1` — uruhererekane rw'imbere (hindura amaderesi wallet ikoresha ubwayo)


Kubera ko Coin Wallet ikurikiza izo ngingo ngenderwako za bose ata mpinduka, amahera yawe azoguma ashobora gusubirwamwo mu yindi wallet yose ihuye mbere no mu myaka 10–20–30.


## 8️⃣ Gutuma umuntu adashobora kumenyekana na Tor


**Kubera iki ukoresha Tor muri Coin Wallet**

Tor ihisha aderesi yawe nyayo ya IP ku bihimba vya Bitcoin, ku bindi bice, n’ababibona.

Ivyo vyose bigenda (amafaranga, amafaranga, amahinduka) bica ku rubuga rwa Tor - nta n’amahuza ataco akora, nta IP ivuza.

Ivyo bishirwa mu ngiro mu buryo butaziguye muri kode y’inkomoko y’iporogarama (raba [.env]


Coin Wallet ifise aderesi .onion yihishije kandi, kuva v6.6.3 (Ukuboza 2024), **infashanyo ya Tor yubatswemwo ataco ihinduye muri porogarama ya telefone ngendanwa**.


### Uko woshobora gukoresha Tor kuri Android na iOS


1. **Shiraho Orbot** - porogaramu yemewe y'umugambi wa Tor (ku buntu)


   - Android → [Ikiganiro ca Google] (ibisobanuro? ID=ishirahamwe.torproject.android) / [F-Droid]
   - iPhone / iPad → [Iduka rya porogaramu] (iporogaramu.


2. **Gufungura Orbot → ushireko Tangira**

Hitamwo **Coin Wallet** muri list kugira ngo wallet yonyene ikoreshe Tor (ntibikenewe ariko birakenewe)

Rindira gushika ivuze **"Ihuye"** (amasegonda 10–30)


3. **Gufungura Coin Wallet → Amategeko → Urubuga**

Gufungura **Koresha Tor**


4. **Suzuma uko bimeze**

**Igishushanyo c'igitunguru ca Tor c'umutuku** kiboneka mu murongo wo hejuru → ubu uruja n'uruza rwose ruca muri Tor


![image](assets/en/06.webp)


Ivyo ni vyo - telefone yawe ngendanwa Coin Wallet nta mazina yawe izwi.


Nimwinovore uburongozi bw’ivy’ubuhinga bwa none!


## 📝 Insozero


- umwe mu ba mbere b’ukuri ba Bitcoin wallet bafise amateka y’iterambere y’imyaka 10.

Ni vyoroshe n’ibigirankana kandi biguma vyibanda ku ntumbero yavyo nyamukuru: kubika neza amafaranga yawe y’ibanga.

Nta kwamamaza, nta makuru, nta kwiyandikisha, nta bintu vyo mu kibano, nta vyo gusamaza - gusa ni wallet isukuye, yihuta, yizigama ikora neza neza ivyo igomba gukora.

Coin Wallet ishira imbere ukworohereza n’umutekano - yama ifise, izokwama ifise.


## 📖 Ibikoresho


https://igiceri.ikibanza/


https://gushigikira.igiceri.ikibanza/hc/ru-du


113


https://amabuye y'agaciro.org/


https://github.com/IkibanzaC'Ibiceri/IkibanzaC'Ibiceri/


www.yubico.com/ikorana-na-yubikey/urutonde/igiceri-wallet/


Urutonde rw'amajambo/icongereza.ts


Gukingira-bip39