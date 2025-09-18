---
name: Bacca
description: Gutunganya Ledger ata porogaramu ya Ledger Live
---
![cover](assets/cover.webp)


Niwakoresha Ledger, kumbure warasanze utegerezwa guca muri porogarama ya Ledger Live, n’imiburiburi ku bijanye n’ugutunganya igikoresho ca mbere, kugira ngo umenye ko ari ukuri maze uyishireko porogarama ya Bitcoin. Ariko rero, inyuma y’iyi ntunganyo, benshi mu bakoresha ama bitcoin barakunda gukoresha porogarama zidasanzwe zo gucunga Bitcoin Wallet nka Sparrow canke Liana aho gukoresha Ledger Live. Naho Ledger itanga amasakoshi meza cane y’ibikoresho yihuta gushiramwo ibintu bishasha vya Bitcoin, porogarama zabo ntizihuye n’ivyo abakoresha ama bitcoin bakeneye vyihariye. Nkako, Ledger Live irimwo ibintu vyinshi vyagenewe altcoins, mu gihe amahitamwo yagenewe uburongozi bwa Bitcoin Wallet ari make. Ariko ikibazo ca Sparrow na Liana (ubu), ni uko zitakwemerera gushiramwo porogarama ya Bitcoin kuri Ledger.


Kugira ngo ushire kure ivy'ugukoresha Ledger Live mu gihe c'ugutunganya kwa mbere kwa Ledger yawe, ushobora gukoresha igikoresho ca Bacca, (canke "Ledger Installer"). Iyo porogarama iragufasha gushiramwo no guhindura porogarama ya Bitcoin, kugenzura ko Ledger yawe ari iyo ukuri, mbere no guhindura porogarama y’ico gikoresho mu nyuma. Bacca yaremwe na Antoine Poinsot (Darosior), umuhinga mu bijanye n’ubuhinga bwa Bitcoin core muri Chaincode Labs, akaba ari we yashinze Revault na Liana, akaba n’umuhinga mu bijanye n’ubuhinga bwa Pythcoiner.


Muri iyi nyigisho, nzokwereka ingene ukoresha iki gikoresho, kugira ngo ushobore gukora ata porogarama ya Ledger Live ku neza, kandi ukomeze kunezerererwa ibikoresho vya Ledger. Ikora ku bikoresho vyose: Nano S Classic, Nano S Plus, Nano X, Flex na Stax.


---
*Urabona ko iki gikoresho ari gishasha, kandi abagikoze bavuga ko kikiri **mu gihe co kugerageza**. Basaba ko umuntu ayikoresha mu gupima gusa, atari ku gikoresho gigenewe kwakira Bitcoin Wallet nyayo, naho nyene bishoboka. Ku bijanye n’ivyo, ndagusavye gukurikiza impanuro z’abateguye iki gikoresho, zivugwa [ku README y’ububiko bwabo bwa GitHub](https://github.com/darosior/ledger_installer).*


---
## Ibisabwa


Kuri mudasobwa yawe, uzokenera ibikoresho bibiri kugira ukoreshe Bacca:




- Git ;
- Rust.


Niba waramaze kubishiramwo, urashobora gusimbuka iyi ntambwe.


**Linukisi:**


Ku gukwirakwiza kwa Linux, Git muri rusangi irashirwaho mbere. Kugira ngo umenye nimba Git yashizwe kuri sisitemu yawe, ushobora kwandika itegeko rikurikira muri terminal :


```bash
git --version
```


Niba udafise Git ishizwe kuri sisitemu yawe, ng'iri itegeko ryo kuyishira kuri Debian :


```bash
sudo apt install git
```


Ubwa nyuma, kugira ngo ushireho ibidukikije vyawe vy'iterambere rya Rust, koresha itegeko :


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Amadirisho:**


Kugira ngo ushiremwo Git, genda kuri [urubuga rwemewe rw'umugambi](https://git-scm.com/). Gukuraho iyo porogarama hanyuma ukurikize amabwirizwa yo kuyishiramwo.


![BACCA](assets/fr/01.webp)


Bandanya mu buryo nk’ubwo nyene kugira ngo ushiremwo Rust uhereye ku [urubuga rwemewe](https://www.Rust-lang.org/tools/install).


![BACCA](assets/fr/02.webp)


**MacOS:**


Niba Git itarashirwa kuri sisitemu yawe, fungura terminal maze ukoreshe itegeko rikurikira kugira ngo uyishiremwo:


```bash
git --version
```


Iyo Git itashizwe kuri sisitemu yawe, idirisha rizofunguka rigusaba gushiramwo Xcode, irimwo Git. Gukurikiza gusa amabwirizwa ari ku rubuga kugira ngo ukomeze gushiramwo.


Kugira ngo ushiremwo Rust, koresha iri tegeko:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## Gushiramwo Bacca


Ugurure terminal maze uje muri dosiye ushaka kubikamwo porogaramu, hanyuma ukoreshe itegeko rikurikira:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


Kugendagenda ku bubiko bwa porogaramu:


```bash
cd ledger_installer
```


Hanyuma ukoreshe Cargo kugira ngo ukoreshe umugambi maze ukoreshe Bacca GUI:


```bash
cargo run -p ledger_manager_gui
```


Ubu urashobora gukoresha porogarama Interface.


![BACCA](assets/fr/03.webp)


## Gutegura Ledger


Imbere y’uko utangura, nimba Ledger yawe ari nshasha, urabe neza ko washizeho kode ya PIN kandi ukabika ijambo ry’ugusubirana. Ntukeneye Ledger Live kuri izo ntambwe z’intango. Gusa n’ushobora gufatanya Ledger yawe biciye ku nzira ya USB kugira ngo uyihe ubushobozi. Niba utazi neza ingene wogenda muri izo ntambwe zibiri, ushobora kuraba intango y'inyigisho yihariye ku citegererezo cawe:


https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Gukoresha Bacca


Huza Ledger yawe na mudasobwa yawe maze uyifungure ukoresheje kode ya PIN washizeho. Bacca ishobora guca imenya Ledger yawe.


![BACCA](assets/fr/04.webp)


Kugira ngo wemeze ko Ledger yawe ari iyo ukuri, fyonda ku buto "*Suzuma*". Uzokenera kwemerera iyo nzira iri ku gikoresho cawe ca Ledger kugira ngo ikomeze.


![BACCA](assets/fr/05.webp)


Bacca izoca ikumenyesha nimba Ledger yawe ari iyo ukuri. Nimba atari vyo, ivyo vyerekana ko ico gikoresho cakozwe mu kaga, canke ko ari ikinyoma. Muri ivyo, nuce uhagarika kuyikoresha ubwo nyene.


![BACCA](assets/fr/06.webp)


Mu "*Apps*", ushobora kuraba urutonde rw'ibikoresho vyashizwe kuri Ledger yawe.


![BACCA](assets/fr/07.webp)


Kugira ngo ushiremwo porogaramu ya Bitcoin, kanda kuri "*Install*", hanyuma wemerere gushiramwo kuri Ledger yawe.


![BACCA](assets/fr/08.webp)


Iryo koraniro ryashizwemwo neza.


![BACCA](assets/fr/09.webp)


Niba udafise verisiyo nshasha y'iporogarama ya Bitcoin, Bacca izokwerekana ubuto "*Update*" aho kugaragaza ikimenyetso "*Igiherutse*". Fyonda gusa kuri iyi buto kugira ngo uhindure porogarama.


![BACCA](assets/fr/10.webp)


Ubu ko Ledger yawe itunganijwe neza n’uburyo bushasha bw’ikoreshwa rya Bitcoin, urateguriye kwinjiza no gukoresha Wallet yawe kuri porogarama zo gucunga nka Sparrow canke Liana, utabwirizwa guca muri Ledger Live!


Niwaba wabonye ko iyi nyigisho ari ngirakamaro, noshima cane iyo usiga urukumu rwa Green aha hepfo. Ntutinye gusangiza abandi iyi nkuru ku mbuga zanyu zo gusangirirako amakuru. Murakoze cane!


Ndagusavye kandi urabe iyi nyigisho kuri GnuPG, isigura ingene wosuzuma ubutungane n’ukuri kwa porogarama yawe imbere yo kuyishiramwo. Ivyo ni ibikorwa bihambaye cane cane iyo ushizeho porogarama yo gucunga Wallet nka Liana canke Sparrow :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc