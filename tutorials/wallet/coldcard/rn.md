---
name: COLDCARD Mk

description: Gukora, gukora backup, no gukoresha urufunguzo rw’ibanga rwa Bitcoin rufise igikoresho ca Coldcard na Bitcoin core.
---

![cover](assets/cover.webp)


_Gukora, gukora ububiko, no gukoresha urufunguzo rw'ibanga rwa Bitcoin rufise igikoresho ca Coldcard na Bitcoin Core_


## Inyigisho yuzuye yo gutanga urufunguzo rw’ibanga ukoresheje Coldcard no kurukoresha biciye ku Interface y’uruzitiro rwawe rwa Bitcoin core!


Mu ntumbero y’ikoreshwa ry’urubuga rwa Bitcoin hariho iciyumviro c’ubuhinga bwo gukingira amakuru ataco akora: urufunguzo rubiri - rumwe rw’ibanga n’urundi rw’abantu bose - rushiramwo amakuru n’ugukuraho amakuru, iciyumviro gituma amakuru aguma ari ay’ibanga.


Ku bijanye na Bitcoin, mu gutanga mwene izo mfunguruzo zibiri z’ibanga n’iza bose, turashobora kubika amafaranga y’ibice (UTXO canke Unspent Transaction Output) maze tugashira umukono ku mafaranga kugira ngo tuyakoreshe.


Ubu, hari ibikoresho vyinshi bishobora gufasha gukora urufunguzo rw’ibanga mu buryo butari bwo no kurubungabunga mu buryo bw’inyandiko hakoreshejwe BIP 39 - urugero rugena ingene ama wallets afatanya ijambo Mnemonic (ijambo seed) n’urufunguzo rwo gupfuka. Kenshi na kenshi, ijambo Mnemonic rigizwe n’amajambo 12 canke 24, ategerezwa gushigikirwa neza kugira ngo umuntu ashobore kugarura Wallet n’amahera yayo.


Muri iki kiganiro, tuzomenya ingene twokoresha urufunguzo rw’ibanga dukoresheje Coldcard Mk4, kimwe mu bikoresho bikoreshwa cane kandi bitekanye kw’isi ya Bitcoin, dukoresheje uburyo bwo gutera amadayisi kugira ngo tubone ko entropie irengeye urugero, n’ingene tworukoresha na Bitcoin core mu ndege ifise ikirere!


**Iciyumviro:🧰** Uronke ibikoresho bikurikira kugira ukoreshe iyo nzira:



- Igikoresho c'ikarita ikonje (Mk3 canke Mk4)
- Ikarata MicroSD (4GB irahagije)
- Umugozi wa USB ukoresha ubushobozi gusa (mini-usb kuri Mk3, usb-c kuri Mk4)
- Imwe canke nyinshi z'uburyo bwiza


## Gutanga ijambo rishasha rya Mnemonic rikoresheje Coldcard


Tuzotangura igikorwa co kurema urufunguzo rw’ibanga kuva mu ntango, twiyumvira ko Coldcard iherutse gufungurwa aho PIN yashizweko (kurikiza intambwe ziri kuri Coldcard mu gihe co gutangura igikoresho).


**Iciyumviro🚨:** Kugira ngo usubiremwo urufunguzo rw'ibanga rwa Coldcard rwamaze gutunganirizwa, kurikiza izi ntambwe:

_Ivyiza/Ibikoresho > Ahantu h'akaga > Ibikorwa vya seed > Gusambura seed > ✓_


**Iciyumviro:** Coldcard yawe izokwibagirwa urufunguzo rw'ibanga ukurikije izi ntambwe. Raba neza ko washizeho neza ijambo ryawe rya Mnemonic nimba ushaka ko uzoshobora kurigarura mu nyuma.


## Intambwe zo gukurikira:


Huza n'ikarata y'ubukonje ukoresheje PIN > Amajambo mashasha ya seed > Amajambo 24 y'uruzitiro


Kora imizingo 100 y’amadayimoni, wandike igisubizo ubonye kuva kuri 1 gushika kuri 6 ku Coldcard inyuma y’imizingo yose. Mu kwimenyereza ubu buryo, urema 256 bytes z’entropie, gutyo ugakunda kurema urufunguzo rw’ibanga rwose. Coinkite kandi itanga ivyangombwa bikenewe kugira ngo umuntu asuzume yigenga uburyo bwabo bwo guhingura entropie.


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


Ivyo bipande 100 vy’amadayimoni bimaze kurangira, ukande ✓ hanyuma wandike amajambo 24 ubonye mu buryo bukurikiranye. Suzuma incuro zibiri hanyuma ukande ✓. Ubwa nyuma, igisigaye ni uguheza ikigeragezo co kugenzura amajambo 24 ari kuri Coldcard, maze voila, urufunguzo rwawe rushasha rw’ibanga ruraremwa!


Inyuma y’aho, uhitemwo nimba ushaka gukoresha canke kutakoresha ibikorwa vya NFC (Mk4) na USB ukurikije intambwe zigaragara. Igihe umaze gushika muri menyu nyamukuru, ubu ni igihe co guhindura porogarama y’ico gikoresho. Genda kuri Advanced/Tools > Upgrade Firmware > Show Version, hanyuma urabe ku rubuga rwemewe kugira ngo wemeze kandi ushiremwo verisiyo nshasha iriho. Ni vyiza guhindura Coldcard kugira ngo ushobore kwungukira ku mutekano mwinshi.


Imbere y’uko ukomeza, birakenewe ko ubona urutoke rw’urufunguzo rwa Master (XFP) rujanye n’urufunguzo rw’ibanga. Aya makuru atuma ushobora kwemezwa ningoga nimba uri muri Wallet ibereye mu gihe co gukira, nk’akarorero. Genda kuri Advanced/Tools > Raba Identity > Master Key Fingerprint (XFP) maze wandike urutonde rw’inyuguti umunani z’inyuguti n’imibare waronse. XFP ishobora kumenyekana ahantu hamwe n’ijambo Mnemonic, si amakuru y’agaciro.


**Iciyumviro:💡** ni vyiza ko ugerageza backup y'amajambo yawe ya Mnemonic muri software itandukanye. Kugira ngo ubikore ata nkomanzi, raba ingingo yacu Suzuma ububiko bwa Bitcoin Wallet n’Imirizo mu minota itarenga 5.


## Ivyiza vy'umutekano: "Ijambo ry'ibanga" (ntibikenewe)


passphrase (ijambo ry’ibanga) ni ikintu ciza cane co kwongera ku ntunganyo ya Wallet kugira ngo wongereko Layer y’umutekano kugira ngo ukinge amafaranga yawe. passphrase ikora nk’ubwoko bw’ijambo rya 25 ku nteruro ya Mnemonic. Iyo imaze kwongerwako, Wallet nshasha rwose iraremwa hamwe n’urufunguzo rw’ibanga be n’invugo Mnemonic ijana na yo. Si ngombwa kwandika ijambo rishasha rya Mnemonic, kuko iryo Wallet rishobora gushikwako mu gufatanya ijambo ry’intango rya Mnemonic n’iryo passphrase ryatowe.


Intumbero ni ugushira ahabona passphrase itandukanye n’ijambo Mnemonic kuko umuterabwoba afise uburenganzira bwo kuronka ivyo bintu vyose bibiri azoronka uburenganzira bwo kuronka ayo mahera. Ku rundi ruhande, uwutera afise uburenganzira bwo gushika kuri kimwe muri ivyo bintu gusa ntazoshobora gushika ku mahera, kandi ni iyo ntumbero yihariye ituma urugero rw’umutekano w’imiterere ya Wallet rutera imbere.


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## Intambwe zo kwongerako passphrase n'ikarita y'ubukonje:


passphrase > Wongereko Amajambo (ni vyiza) > Shiraho. Ico gikoresho kizokwerekana XFP ya Wallet nshasha yavutse iri kumwe na passphrase, ivyo bikaba bikwiye kwandikwa hasi na passphrase kubera izo mpamvu nyene twavuze imbere.


**Impanuro💡** Aha hariho ibindi bikoresho bijanye na passphrase:



- [Aha](ni-passphrase-yawe-irakomeye-bihagije-d687f44c63af) hariho iya mbere ya _Trezor_;
- [Aha](https://blog.coinkite.com/ivyo-ukeneye-kumenya-vyose-ku-majambo-ibanga/) ushobora gusanga iya kabiri na _Coinkite_;
- Kandi [hano](https://armantheparman.com/passphrase/) uzosanga iya nyuma ya _armantheparman_.


## Gutuma hanze Wallet mu Bitcoin core


Ubu Wallet iriteguriye gurungikwa hanze muri porogarama kugira ngo ikoreshe n’urubuga rwa Bitcoin. Muri iyi nsiguro, tuzokoresha Bitcoin core (umurongo wa 24.1).


Raba uburongozi bwacu bwo gushiramwo no gutunganya Bitcoin core:



- Gukoresha urudodo rwawe bwite na Bitcoin core:**
- Gutunganya Tor ku nzira ya Bitcoin core:**


Ubwa mbere, shiramwo ikarita ya micro SD muri Coldcard, hanyuma urungike Wallet ku Bitcoin core ukurikije izi ntambwe: Ivyiza/Ibikoresho > Urungike Wallet > Bitcoin core. Ku ikarita ya micro SD hazokwandikwa amadosiye abiri: Bitcoin-core.sig & Bitcoin-core.txt. Injira ikarata micro SD muri mudasobwa aho Bitcoin core iri, hanyuma ufungure dosiye .txt. Uzobona umurongo "Kuri Wallet n'urutoke rw'urufunguzo rwa mbere." Genzura ko XFP y'inyuguti umunani ihuye n'iyo wabonye igihe wakora urufunguzo rwawe rw'ibanga.'

Imbere yo gukurikiza amabwirizwa ari muri dosiye, reka dutangure gutegura Wallet muri Bitcoin core Interface dukurikije izi ntambwe: genda kuri Dosiye > Rema Wallet. Hitamwo izina rya Wallet yawe (ijambo rihindurwa na "porte-monnaie" muri Core) hanyuma usuzume amahitamwo Guhagarika imfunguruzo z'ibanga, Rema Wallet y'ubusa, n'ibisobanuro vya Wallet nk'uko vyerekanwa ku ishusho iri musi. Hanyuma, ukande kuri buto Rema.


![create a wallet](assets/guide-agora/3.webp)


Wallet imaze kuremwa muri Bitcoin core, genda kuri Window tab > Console maze urabe neza ko Wallet yatowe iri hejuru kuri paji yerekana izina ry’iyo waremye.


Ubu, muri dosiye .txt yasohowe na Coldcard mbere, kopira umurongo utangura n’ibisobanuro vy’ibintu biva hanze, hanyuma uwushire muri console ya Bitcoin core. Inyishu irimwo umurongo "uguterimbere": ukuri gukwiye gusubirwamwo.


![nodes window](assets/guide-agora/4.webp)


Niba inyishu irimwo "ubutumwa": "Ibisobanuro vy'urutonde ntibikwiye kugira ikimenyetso", futa inyandiko "ikimenyetso": "Coldcard xxxx0000" mu murongo wakopiwe muri dosiye .txt, hanyuma ushire umurongo wose muri console ya Bitcoin core.


Niba bikenewe, urashobora kuronka imfashanyo [hano] kuri Coldcard Github.


## Kwemeza ibiva hanze vya Wallet muri Bitcoin core


Kugira ngo igikorwa kibe ciza, birakenewe kwemeza ko Wallet yipfuzwa yinjijwe muri Bitcoin core. Uburyo bworoshe bwo kwemeza ivyo ni ukugenzura ko amaderesi yashizwe muri Coldcard ahuye n'ayashizwe muri Bitcoin core.


Bitcoin core: Kwakira > Rema Address nshasha yo kwakira

Ikarata y’ubukonje: Address Igikoresho co gutohoza > Hitamwo Address utangura na bc1q. Ikarata y'ubukonje Address 'bc1q' ikwiye guhura na Address yerekanwa muri Bitcoin core.

Kwakira no kohereza amafaranga mu buryo bwa 'air-gapped'


Kwakira amafaranga y’ugucuruza ni ikintu coroshe cane; gusa kanda Receive, ushireko ikimenyetso ku gicuruzwa (ntibikenewe ariko ni ngirakamaro), hanyuma Ureme Address nshasha yakira. Hanyuma, igisigaye ni ugusangira Address n’uwayirungitse.


Ubu, ikintu nyamukuru c’iyi Coldcard + Bitcoin core ni ugutuma amafaranga ata Coldcard n’urufunguzo rwayo rw’ibanga bihujwe na internet, uburyo bwitwa air-gapped bukoresha igikorwa ca TBSP (PSBT - Amafaranga ya Bitcoin yashizweko umukono ku gice) ca Bitcoin.

Mu vy’ukuri, dukoresha Bitcoin core Interface kugira ngo twubake igikorwa, ico tuzoca tugirungika hanze biciye ku ikarita ya micro SD tukaja kuri Coldcard kugira ngo dushireko umukono, hanyuma tugasubiza dosiye y’igicuruzwa yashizweko umukono kuri Bitcoin core maze tugatangaza igikorwa ku rubuga. Tubwirizwa kubikora gutyo kuko Wallet yinjijwe muri Bitcoin core nta rufunguzo rw’ibanga ifise, urufunguzo rwa bose gusa (rutuma dushobora generate amaderesi yacu y’ukwakira), rero ntibishoboka ko dushobora gusinya ku giciro gica muri porogarama kugira ngo dukoreshe ama bitcoins yacu.


Imbere yo gukomeza, urabe neza ko amahitamwo akurikira akoreshwa mu Mitunganyirize > Wallet:



- Gushoboza ibiranga ubugenzuzi bwa Coin
- Gukoresha ibiceri bitaremejwe (Ntibikenewe)
- Gushoboza igenzura rya TBPS


![option ](assets/guide-agora/5.webp)


### Intambwe zo kohereza mu buryo bw'umuyaga:


Wohereze > Inputs > uhitemwo UTXO wipfuza, hanyuma winjize Address y'uwuyironka muri Pay to. Amafaranga y’ugucuruza: Hitamwo... > Kugenza > Injira amafaranga y’ugucuruza (Bitcoin core iharura muri Sats/kilobyte aho kubara sat/byte nk’uko bimeze mu bindi bisubizo vyinshi vya Wallet. Rero 4000 Sats/kilobyte = 4 Sats/kilobyte). Rema igikorwa kitashizweko umukono > ubike iyo dosiye ku ikarita yawe ya micro SD hanyuma uyishire muri Coldcard.


Mu Coldcard, kanda Ready to sign, ugenzure amakuru y’ivyo ukoze, hanyuma ukande ✓ hanyuma usubiremwo ikarita ya micro SD muri mudasobwa iyo amadosiye yashizweko umukono amaze gusohoka.


Gusubira muri Bitcoin core, genda kuri Dosiye > Shira TBSP muri dosiye, hanyuma winjize dosiye y'ibikorwa yasinywe .PSBT. Akazu k’Ibikorwa ka PSBT kazoboneka ku rubuga, kazokwemeza ko iyo nzira yashizweko umukono yose kandi ko yiteguriye gutangazwa. Igisigaye ni ugukanda Transaction ya Broadcast.


![PSBT operations](assets/guide-agora/6.webp)


### Iciyumviro


Ihuriro ry’igikoresho ca Coldcard na Bitcoin core, ukoresha node yawe bwite, rirakomeye cane. Wongereko urufunguzo rw’ibanga rwavutse n’imizingo 100 y’amadayimoni n’ijambo ry’ibanga, maze imiterere yawe ya Wallet ikaba igihome gikomeye kandi gikomeye.


Ntutinye kuduhamagara kugira ngo mudusangire ibitekerezo n'ibibazo vyanyu! Intumbero yacu ni ugusangira ubumenyi no kwongera ugutahura kwacu ku musi ku musi.