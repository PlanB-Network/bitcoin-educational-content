---
name: Blitz Wallet
description: Agasanduku ka Bitcoin koroshe cane.
---

![cover](assets/cover.webp)

Uburambe bw'umukoresha ni kimwe mu bintu bihambaye iyo uhisemwo agasanduku ka Bitcoin. Muri iki cigishwa, turabamenyesha Blitz Wallet, agasanduku gashira ukorohereza hagati mu buryo bwako: kubera integuro ya protocol ya **Spark**, Blitz ikaguha kimwe mu masanduku ya Bitcoin yoroshe cane kandi yuzuye ku isoko, hamwe n'amahera yishurwa vuba kandi ata gucungera ibintu vy'ikoranabuhanga.

## Blitz Wallet ni iki?

Blitz Wallet ni agasanduku ka Bitcoin ka **self-custodial** kandi ka **open source**, kashingiye ku bwigenge bwawe n'uburambe bw'umukoresha bworoshe kandi bwumvikana neza.

[Blitz Wallet](https://blitz-wallet.com/) ni porogaramu ya telefone ihari kuri Android (Play Store) na iOS (App Store).

Bitandukanye n'amasanduku ya Lightning asanzwe ahitaji gucungera inzira z'amahera n'amazi yinjira, Blitz Wallet ishingiye kuri **protocol ya Spark** kugira ikure iyo ngorane y'ikoranabuhanga. Igishoboka: amahera yishurwa vuba kuva kuri satoshi ya mbere yakiriwe, ata gushiraho ikintu na kimwe imbere y'igihe. Intumbero ya Blitz ni ugutuma amahera ya bitcoin yoroshe nk'iporogaramu isanzwe yo kwishura, ata na rimwe ugahungabanya self-custody y'amahera yawe.

Blitz Wallet ishigikira kandi **aderesi zisomeka** mu buryo bwa `umukoresha@domaine.com` (biciye kuri LNURL), bikemera kohereza bitcoin nk'imeyili yoroshe, ata gukoresha invoices ndende canke QR codes kuri buri gikorwa.

## Gutegera protocol ya Spark

Imbere yo guca ku bikorwa, birashimishije gutegera ikoranabuhanga rituma Blitz Wallet ikora munsi y'igipfukisho: **protocol ya Spark**.

### Spark ni iki?

Spark ni protocol ya urwego rw'inyuma ya open source yubatswe kuri Bitcoin, yateguwe n'umugwi wa Lightspark. Ikemera gukora ibikorwa vuba kandi ku giciro gito, mu gihe iziganira self-custody ya bitcoin zawe.

Bitandukanye na Lightning Network ishingiye ku **nzira z'amahera** hagati y'imigwi ibiri, Spark ikoresha ikoranabuhanga ryitwa **statechain** (urunigi rw'imimerere). Ingingo y'ishingiro ni iyi: aho gukwega bitcoin kuri blockchain kuri buri gikorwa, Spark ihererekanya **uburenganzira bwo gukoresha** kuva ku mukoresha umwe gushika ku wundi, ata gukwiragira on-chain.

### Bikora gute?

Kugira utegere Spark mu buryo bworoshe, nimuze twiyumvire ko gukoresha bitcoin kuri Spark bisaba gukuza igikino c'ibipande bibiri:
- Igipande kimwe gifashwe n'umukoresha (urugero, Alice).
- Igipande kigira kabiri gifashwe n'umugwi w'abakoresha witwa **Spark Entity (SE)**.

Ni uguhuriza hamwe ibipande bibiri bihuye gusa bituma ushobora gukoresha bitcoin.

Iyo Alice ashaka kohereza bitcoin ziwe kuri Bob, ng'iki igishoboka: igikino gishasha gikorwa hamwe hagati ya Bob na SE. Igikino kiguma gifise ishusho imwe, ariko ibipande bikigize birahinduka. Ubu, ni igipande ca Bob gihuye n'ica SE. Igipande ca kera ca Alice gicika kidashoborwa gukoreshwa, kuko SE yahanaguye igipande cayo gihuye. Ubunyagasanduku bwa bitcoin bwahinduwe amaboko, **ata gikorwa na kimwe kuri blockchain**.

Bob ashobora gusubiramo uwo mwuga nyene wohereza izo bitcoin kuri Carol, n'ibindi n'ibindi. Buri guhererekanya gukora mu gusimbuza ibipande vy'igikino, atari mu gukwega amahera on-chain.

### Kubera iki ari safi?

Ikibazo gikwiye kiribuka: bigenda gute SE itahanaguye vy'ukuri igipande cayo ca kera?

Spark Entity si inzego imwe: ni umugwi w'abakoresha bigenga. Igipande ca SE ntikirashikwa n'umukoresha umwe. Gusimbuza igikino bisaba ugufashanya kw'abakoresha benshi. Bihagije ko **umukoresha umwe ari umwizigirwa** mu gihe c'uguhererekanya kugira abuze gusubira kwongera igikino ca kera. Nta mukoresha n'umwe wenyene ashobora kubika mu mpisho igikino ca kera gikora canke kugisubirako mu nyuma.

Vyongeye, Spark iriko uburyo bwo gusohoka ku ruhande rumwe: ushobora buri gihe gusubira kuronka bitcoin zawe on-chain ata gufashanya na SE. Ubu buryo bw'ubusanganirizo ni igice ntahinduka c'isanzure ya Spark, kandi buremeza ko utaja bwigere gushingira ku mukubukanyi kugira uronke amahera yawe.

### Spark na Lightning Network

Spark na Lightning ntibapfa: ni **ibikurikiranye**. Blitz Wallet irunganya vyompi, bikakwemera kwunguka ivyiza vya kimwe cose.

|                               | **Spark**                    | **Lightning Network**  |
| ----------------------------- | ---------------------------- | ---------------------- |
| **Ikoranabuhanga**            | Statechains (iminyororo y'imimerere) | Inzira z'amahera |
| **Gucungera inzira**          | Ntibisabwa                   | Birasabwa              |
| **Amazi yinjira**             | Ntibisabwa                   | Birasabwa              |
| **Ibikorwa vya vuba**         | Ego                          | Ego                    |
| **Self-custody**              | Ego                          | Ego                    |
| **Kwihuza na Lightning**      | Ego (biciye kuri atomic swaps) | Kamere              |

Lightning Network iguma ari protocol nziza cane y'amahera yishurwa vuba, ariko ishira imbibe z'ikoranabuhanga (gucungera inzira, amazi yinjira, nodi kuri interineti...) bishobora guhagarika abatangura. Spark ikura izo mbibe mu gihe iguma ihuza na Lightning.

## Kwinjiza no gushiraho

Muri iki cigishwa, twishingiye ku gice ca Android ca Blitz Wallet, ariko ibikorwa vyose bierekanwe hepfo birakora kandi kuri iOS.

![installation](assets/fr/01.webp)

Blitz Wallet ikaba ari agasanduku ka self-custody, ufise amahitamwo hagati yo **gukora agasanduku gashasha** canke **kwinjiza amajambo yo gusubira kuronka** (amajambo 12 canke 24) y'agasanduku kahari.

Hano, dutangura n'igukora agasanduku gashasha. Raba hepfo impanuro zacu ku kubika amajambo yawe yo gusubira kuronka:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **BIHAMBAYE**: Ayo majambo 12 canke 24 yo gusubira kuronka ni **urufunguzo rwonyene rwo gushikira bitcoin zawe**. Blitz ni agasanduku ka self-custodial: nta Blitz nta Spark ifise uburyo bwo gushikira amajambo yawe yo gusubira kuronka canke amahera yawe. Utabuze ayo majambo, uzobura buhere gushikira bitcoin zawe. Ntuyasangire n'umuntu n'umwe: uwo ari we wese ayafise arashobora gukoresha bitcoin zawe.

Hanyuma kora **PIN** kugira ucungire gushikira agasanduku kawe.

![setup-wallet](assets/fr/02.webp)

## Gutangura na Blitz

Gukora ibikorwa na Blitz biroroshe kuruta amasanduku menshi ya Bitcoin. Ishusho ni nto kandi ishingiye ku bikorwa bitatu nyamukuru: kohereza, guskanisha no kwakira.

### Kwakira bitcoin

Kugira wakire bitcoin ku gasanduku kawe ka Blitz, fyonda kuri ikone ya **"Umwampi wo hasi"** (↓), andika umubare mu satoshi ushaka kwakira, ongerako insiguro y'ubushake, hanyuma agasanduku kazotera invoice ushobora gusangira n'uwohereza.

⚠️ **ICIYUMVIRO**: Satoshi (canke "sat") ni igipimo gitoya cane ca bitcoin: **1 bitcoin = 100 000 000 satoshi**.

Kimwe mu bihambaye vya Blitz Wallet ni uko ishigikira imitandao n'amaprotocol menshi y'umurwi wa Bitcoin:

- **Lightning Network**: Kimwe mu bitwikiro vya Bitcoin bikemera gukora amahera mato vuba cane n'amafaranga mato cane. Bikwiye amahera mato ya buri musi.

- **Bitcoin (on-chain)**: Blockchain nyamukuru ya protocol ya Bitcoin, ikwiye ibikorwa vy'amahera menshi aho umutekano mwinshi cane n'iherezo ari ibitangira.

- **Liquid Network**: Sidechain (urunigi rw'iruhande) ya Bitcoin yateguwe na Blockstream, ikemera ibikorwa vya vuba kandi vy'ibanga ikoresha Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Mu buryo busanzwe, Blitz ikora invoice ya Lightning, ariko urashobora guhitamwo umutandao ushaka kwakira satoshi zawe mu gufyonda kuri buto ya **"Choose format"**.

![receive-sats](assets/fr/03.webp)

### Gukora kontakte

Blitz Wallet irorohereza kohereza bitcoin kenshi biciye mu buryo bwayo bwa kontakte.

Mu menyu ya **Contacts**, urashobora kwandika amazina y'abakoresha Blitz canke aderesi za Lightning (LNURL) ukorana kenshi.

Ushobora rero kohereza satoshi kuri izo aderesi mu mafyondeko makeyi, ata guskanisha QR code canke kwandika ku kuboko aderesi buri gihe.

### Kohereza bitcoin

Uretse uburyo busanzwe bwo kohereza bitcoin (guskanisha QR code, kwandika aderesi ku kuboko), Blitz itanga amahitamwo menshi akora:

- **Kuva ku cifoto** (*From Image*): Injiza QR code kuva mu birango vyawe vy'amafoto.
- **Kuva kw'ikopiye** (*From Clipboard*): Omeka aderesi canke invoice yakopiywe imbere y'aho.
- **Kwandika ku kuboko** (*Manual Input*): Andika ku buryo butaziguye aderesi ya Bitcoin, invoice ya Lightning canke aderesi isomeka (urugero `umukoresha@walletofsatoshi.com`).
- **Kuva ku kontakte zawe**: Hitamwo uwakira yanditswe imbere y'aho kugira wohereze mu mafyondeko makeyi.

Mu menyu ya **Wallet**, fyonda kuri buto ya **"Umwampi wo hejuru"** (↑), hitamwo uburyo bwawe bwo kohereza, andika umubare wo kohereza, ongerako insiguro hanyuma wemeze igikorwa.

Umubare muto wo kohereza ubu ni **satoshi 1 000**.

![send-bitcoin](assets/fr/05.webp)

## Iduka rya Blitz

Hejuru y'ibikorwa vyo guhererekanya bitcoin, Blitz Wallet irunganya iduka ushobora gukoreshamo bitcoin zawe kugura amabanga ya numerique ku buryo butaziguye kuva muri porogaramu.

Kuva ku menyu nyamukuru, fyonda ku gice ca **Store** kugira ushike kw'iduka. Uzosanga kandi uburyo bwo gushika kuri platiforme ya **Bitrefill** ikemera kugura amakarata y'ingabirano kuva ku bacuruzi ibihumbi n'ibihumbi kw'isi yose, ku buryo butaziguye mu bitcoin.

- **Ubwenge bw'ikoranabuhanga**: Shikira modele za nyuma z'AI izalisha (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) hanyuma wishure amakredi yawe ku buryo butaziguye mu satoshi. Amapake menshi ahari hisunzwe ivyo ukeneye (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **SMS z'ibanga**: Ohereza hanyuma wakire SMS ahantu hose kw'isi ata guhishura inomero yawe ya telefone y'umwihariko. Ubwo buhanga burishurwa mu satoshi kuri buri butumwa bwoherejwe.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Kinga ubuzima bwawe bwite kuri interineti mu kwiyandikisha ku bwishyu bwa VPN WireGuard (bw'indwi, bw'ukwezi canke bw'igice c'umwaka), bushobora kwishurwa mu bitcoin ku buryo butaziguye kuva mw'iduka rya Blitz. Uzokenera gusa gupakura porogaramu ya kliyansi ya WireGuard ku cuma cawe kugira uyikoreshe.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet inyuma y'igipfukisho: kuja kure

Inyuma y'ukorohereza gukoresha Blitz Wallet hihishije isanzure y'ikoranabuhanga yiyumviriywe neza ihuriza hamwe urwego rwinshi rw'umurwi wa Bitcoin.

### Ugutandukanya umutahe wawe

Blitz Wallet icungera umutahe wawe mu buryo butomoye mu gutandukanya amahera yawe hagati y'amaprotocol atandukanye hisunzwe ivyo ukeneye. Iyo umutahe wawe uri munsi ya satoshi 500 000, Blitz ikoresha **Liquid Network** n'atomic swaps kugira iguhe uburambe bworoshe kandi ikemere ibikorwa kuri Lightning Network n'amahera mato.

Ubu buryo buremeza itanguriro ryoroshe ku bakoresha bashasha, ata bo gukena gutegera uburyo buri munsi. Urashobora kuraba ugutandukanya kw'umutahe wawe hagati y'urwego rutandukanye mu menyu ya **Amashirwe > Balance Info**.

![balance](assets/fr/09.webp)

### Uburyo bwa Lightning (bw'ubushake)

Mu buryo busanzwe, Blitz Wallet ikoresha Liquid Network na protocol ya Spark kugira iguhe uburambe bworoshe ata gushiraho ikoranabuhanga. Ariko, Blitz ikaguha ubushobozi bwo gukoresha **uburyo bwa Lightning** buzofungura ku buryo bwikora inzira y'amahera iyo ushitse ku mutahe wa **satoshi 500 000** (0.005 BTC).

Kugira ukoreshe uburyo bwa Lightning, ja mu **Amashirwe**, hanyuma mu gice c'**Amashirwe y'ikoranabuhanga**, fyonda ku gihitamwo ca **Node Info**.

![enable-lightning](assets/fr/10.webp)

Kubera protocol ya Spark, iki gikorwa ni **c'ubushake**: Spark ikemera kare gukora amahera ahuza na Lightning ata gukena gufungura inzira canke gucungera amazi yinjira. Uburyo bwa Lightning kamere buguma ari ngirakamaro ku bakoresha batahura bashaka kugira nodi yabo ya Lightning mu porogaramu.

### Ikibanza co kugurisha (PoS)

Blitz Wallet irunganya ubushobozi bw'**ikibanza co kugurisha** bukemera abacuruzi kwakira amahera ya bitcoin ku buryo butaziguye kuva muri porogaramu.

Mu menyu ya **Amashirwe > Point-of-sale**, urashobora gushiraho:

- Inomero y'agasanduku y'iduka ryawe
- Ifaranga ry'igihugu ry'aho ukurikirana ibiciro
- Amabwirizwa y'abakozi bawe
- Ihitamwo ry'amahera yo gushimira ku bakiriya bawe

Abakiriya bawe bakeneye gusa guskanisha QR code yakorwa kugira bishure mu bitcoin, vuba cane.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Ivyakoreshejwe mu kwandika iki cigishwa:
- Blog ya [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
