---
name: Tailscale
description: Inyigisho y'umurizo iteye imbere
---
![cover](assets/cover.webp)



## 1. Intangamarara



Tailscale ni VPN y’uruvyaro rukurikira irema urubuga rw’urusenga rwuzuye hagati y’ibikoresho vyawe. Bituma ushobora gufatanya imashini ziri kure nk’aho zoba ziri ku rubuga rumwe rw’aho hantu, ata n’ivyo gutunganya bikomeye canke gufungura icuma.



Ku bijanye no kwiyakira, Tailscale iha igikoresho cose IP y’ibanga idahinduka mu rubuga rw’ivy’impwemu, itanga uburenganzira bwo gushika ku bikorwa vyawe mbere n’igihe IP yawe ya bose ihindutse. Ivyo bisigura ko ushobora gucunga ama server yawe uri kure, utashize ibikorwa vyawe kuri Internet.



**Ibikorwa nyamukuru:**




- Gucungera umukozi w'umuntu ku giti ciwe ari hanze
- Gucungera umutaka/imiravyo vyihuta kurusha Tor
- Ukwinjira mu mutekano kuri Raspberry Pi canke NAS
- Kwihuza n'ibikorwa vyawe biciye kuri SSH canke HTTP ata mitunganyirize y'urubuga igoranye



Ubwo buryo bwibanda ku kworoha buratuma abakira abashitsi bashobora kuronka ibikorwa vyabo ata nkomanzi, bakirinda imitego ya VPN za kera.



## 2. Uko Tailscale ikora



Udakunze VPNs za kera, zijana uruja n’uruza rwose biciye kuri server nyamukuru, Tailscale irema uruja n’uruza rw’urusenga aho ibikoresho bivugana ataco bimaze. Serveri nyamukuru ikora gusa ivyerekeye kwemeza n’ugukwiragiza urufunguzo, itabona amakuru y’abakoresha.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Ishusho 1: VPN ya kera ifise ubuhinga bwa hub-and-spoke aho uruja n'uruza rwose ruca kuri server ya mbere*



Hashingiwe kuri WireGuard, igikoresho cose kiratanga imfunguruzo zaco z’ubuhinga bwo gukingira amakuru. Serveri y’uguhuza ibikorwa itanga imfunguruzo za bose ku bihimba, ivyo bikaba bica bishinga imigende y’iherezo n’iherezo hagati yavyo. Kugira ngo umuntu ashobore guca mu bihome vy’umuriro, Tailscale ikoresha NAT traversal kandi, nk’uburyo bwa nyuma, DERP relays zibungabunga ububiko.



![VPN maillé (mesh)](assets/fr/02.webp)


*Ishusho ya 2: Urubuga rw'urusenga rw'umurizo aho ibikoresho bivugana ataco bihinduye*



Ivyiyumviro vyose bikoreshwa na WireGuard. Tailscale ibona gusa metadata (amahuza) ariko ntiyigera ibona ibirimwo mu guhanahana. Kugira ngo ubusegaba bube bwinshi, Headscale irashoboza umukozi w’uguhuza ibikorwa kwiyakira.



**Umutekano n'ibanga:** Kubera WireGuard, amakuru yose yo kuri Tailscale arashirwa mu nzira y'ibanga. Tailscale ntishobora gusoma uruja n'uruza rwawe - ibikoresho vyawe vyonyene nivyo bifise imfunguruzo z'ibanga zikenewe. Servisi ibona gusa amakuru: aderesi za IP, amazina y’ibikoresho, ibimenyetso vy’igihe co guhuza n’ibitabo vy’uguhuza (ata birimwo).



Ariko rero, iyo nyubakwa iva kuri Tailscale Inc. ku bijanye n’uguhuza urubuga. Kugira ngo ukureho ukwo kwisunga, Headscale itanga uburyo bundi bwo gukoresha inkomoko yuguruye bushobora kugufasha kwikorera server y’ubugenzuzi mu gihe ukoresha abaguzi ba Tailscale bazwi, gutyo ugatanga ubusegaba bwose ku bikorwa remezo vy’urubuga rwawe, ku giciro c’imiterere y’ubuhinga.



**Kugira ngo ubone insiguro ido n’ido y’imikorere y’imbere ya Tailscale, harimwo n’ugucungera indege, guca mu nzira ya NAT n’uguhinduranya DERP, turagusavye ingingo nziza cane [Uko Tailscale ikora](https://tailscale.com/blog/how-tailscale-works) ku rubuga rwemewe. Iki kiganiro kirasigura mu buryo bwimbitse ivyiyumviro vy’ubuhinga bituma Tailscale igira ububasha bwinshi cane.**



## 3. Gushiramwo Umurizo



Tailscale ikoreshwa ku bikoresho bikoreshwa cane (amadirisha, macOS, Linux, iOS, Android). Gushiramwo bivugwa ko "vyihuta kandi vyoroshe" ku mbuga zose. Reka dutangure turabe Interface n’ingene wokora konti, hanyuma tuje ku buryo bwo kuyishiramwo ku bidukikije bitandukanye.



### 3.1 Gukora konti y'umurizo



Genda kuri [https://tailscale.com/](https://tailscale.com/) ukande kuri buto ya "Tangira" iri hejuru iburyo kuri iyo paji.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Urupapuro rw'intango rwa Tailscale rurasigura iciyumviro kandi rutanga intango y'ubuntu*



Kugira ngo ukoreshe Tailscale, ubanza gukora konti biciye ku muntu atanga akaranga:



![Page de connexion Tailscale](assets/fr/04.webp)


*Ihitamwo ry'uwutanga akaranga ko kwifatanya na Tailscale (Google, Microsoft, GitHub, Apple, n'ibindi)*



Uhejeje kwinjira, Tailscale izogusaba amakuru yerekeye uko ushaka gukoresha:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Ifomu kugira utahure neza ikoreshwa ryawe (ry'umuntu ku giti ciwe canke ry'umwuga)*



Umaze gukora konti yawe, ushobora gushiramwo Tailscale ku bikoresho vyawe:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale iragufasha gushiramwo porogaramu kuri sisitemu zitandukanye*



### 3.2 Gushiramwo ku mbuga zitandukanye





- Ku Windows na macOS: Ushobora gusa gukuraho porogarama y’ibishushanyo ku rubuga rwemewe rwa Tailscale maze ukayishiramwo (dosiye .msi kuri Windows, dosiye .dmg kuri Mac). Iyo imaze gushirwamwo, iyo porogarama itanguza igishushanyo Interface kigufasha kwifatanya (biciye mu mucukumbuzi) na konti yawe ya Tailscale kugira ngo wemeze ko iyo mashini ari iyo.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Huza MacBook n'urubuga rw'inyuma*



![Connexion réussie](assets/fr/09.webp)


*Kwemeza ko igikoresho gifatanye n'urubuga rwa Tailscale*





- Kuri Linux (Debian, Ubuntu, n'ibindi): Ufise amahitamwo menshi. Uburyo bworoshe ni ugukoresha inyandiko yemewe yo gushiramwo: nk'akarorero, kuri Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Iyi nyandiko izokwongerako ububiko bwa Tailscale buzwi maze ishiremwo iyo package. Ushobora kandi [kwongerako n'amaboko ububiko bwa APT](https://pkgs.tailscale.com) canke ukoreshe amapaki asanzwe ya Snap canke apt. Iyo imaze gushirwaho, daemon `tailscaled` izokora inyuma. Uzoca ukenera **kwemeza urudodo** (raba Interface CLI vs urubuga aha hepfo). Ku bindi bimenyetso (Fedora, Arch...), iyo mpapuro iraboneka kandi biciye ku bubiko busanzwe canke inyandiko yo gushiramwo rusangi. Ku mukozi atagira umutwe, koresha CLI: nk'akarorero `sudo tailscale up --auth-key <key>` niba ukoresha urufunguzo rwo kwemeza rwakozwe mbere, canke gusa `tailscale up` ku kwinjira mu buryo bukorana (bizotanga URL yo gusura kugira ngo wemeze igikoresho).





- Ku bikoresho bishingiye kuri ARM (Raspberry Pi, n’ibindi): Muri rusangi turi kuri Linux, rero uburyo bumwe nk’ubwo haruguru (inyandiko canke umuzigo). Zirikana ko Tailscale ishigikira ubuhinga bwa ARM32/ARM64 ata ngorane. Abakoresha benshi bashiraho Tailscale kuri Raspberry Pi OS biciye ku apt canke ku bimenyetso vy’uburemere buke (DietPi, n’ibindi) kugira ngo bashobore gushika ku Pi yabo hose.





- Ku iOS na Android: Tailscale itanga **ivyemewe** ibikoresho vyo kuri telefone ngendanwa. Gusa shiramwo *Tailscale* mu [Iduka ry'Iporogarama](iOS) canke [Iduka ry'Imikino](Iduka ry'Imikino](id.



![Installation sur iPhone](assets/fr/11.webp)


*Intambwe zo gushiramwo Tailscale kuri iPhone: ikaze, ubuzima bwite, amatangazo, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Ihuze na tailnet, uhitemwo konti maze uyishire kuri iPhone*



Iyo app imaze gushirwamwo, ku gutangura kwa mbere izogusaba kwemeza biciye ku mutanga wahisemwo (Google, Apple ID, Microsoft, n’ibindi, bivanye n’ico uriko urakoresha kuri Tailscale) - ni uburyo bumwe nk’ubwo ku zindi nzira, akenshi ni ugusubira ku rubuga rwa OAuth. Inyuma y’ivyo, porogarama ya telefone ngendanwa irarema VPN (kuri iOS uzokenera kwemera iyongeweko y’imiterere ya VPN). Iyo app ishobora rero gukora inyuma, ikaguha uburenganzira bwo gukoresha tailnet yawe uri aho hose. *Ibuka:* kuri mobile, ushobora kugira **VPN imwe ikora gusa ku gihe** - rero urabe ko udafise iyindi VPN ihuriweko igihe kimwe, canke Tailscale ntizoshobora gushinga iyayo. Kuri Android, ushobora gushinga urutonde rw'akazi rutandukanye nimba ushaka gutandukanya ikoreshwa rimwe rimwe (nk'akarorero urutonde rufise Tailscale rukora kuri porogaramu).



### 3.3 Kwongera ibikoresho vyinshi no kwemeza



Igihe igikoresho cawe ca mbere gifatanye, Tailscale iragusaba kwongerako ibindi bikoresho ku rubuga rwawe:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface yerekana igikoresho ca mbere gifatanye kandi kirindiriye ibindi bikoresho*



Umaze kwongerako ibikoresho vyinshi, ushobora kumenya ko bishobora kuvugana:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Kwemeza ko ibikoresho bishobora kuvugana n'ibindi biciye kuri ping*



Tailscale rero itanga ivyiyumviro vy'inyongera kugira ngo wongere ubumenyi bwawe:



![Suggestions de configuration](assets/fr/14.webp)


*Ivyiyumviro vyo gushinga DNS, gusangira ibikoresho no gucunga uburyo bwo kuronka*



### 3.4 Urubaho rw'ubuyobozi



Ubuyobozi bw'urubuga buragufasha kuraba no gucunga ibikoresho vyawe vyose bihuye:



![Tableau de bord des machines](assets/fr/15.webp)


*Urutonde rw'ibikoresho bihuye n'ibiranga n'aho bimeze*



**Urubuga rwa Interface vs Interface CLI:** Tailscale itanga uburyo bubiri bwuzuzanya bwo gukorana n'urubuga: **uburongozi bw'urubuga rwa Interface** na **umukiriya w'umurongo w'amabwirizwa (CLI)**.





- Urubuga rwa Interface (Igikoresho c'Umuyobozi)**: ushobora kuronka kuri [https://injira.tailscale.com](https://injira.tailscale.com), iyi konsole y'urubuga ni yo nzira nyamukuru y'urubuga rwawe rwa Tailscale. Iratanga urutonde rw’ibikoresho vyose (*Imashini*), uko biri kuri interineti/ku rubuga rwa interineti, aderesi zavyo za IP za Tailscale, n’ibindi. Aha ushobora **gucunga ibikoresho** (guhindura izina, guhera kw'imfunguruzo, kwemerera inzira, guhagarika urudodo), **gucunga abakoresha** (mu bijanye n'imiteguro), no gusobanura amategeko y'umutekano (ACLs). Aha niho kandi utunganya amahitamwo y'isi yose nka MagicDNS, ama tags, canke imfunguruzo z'ukwemeza (imfunguruzo z'ukwemeza imbere ya generate ku kwongerako ibikoresho vy'ubuhinga). Interface web ni ngirakamaro cane mu kuronka icegeranyo no gukoresha amahinduka azokwiragizwa biciye kuri server y'uguhuza ku nzira zose. *Akarorero:* Gukoresha **inzira y'uruja n'uruza** canke **uruzitiro rwo gusohoka** bikorwa n'ugukanda rimwe muri console, iyo uruzitiro ruvugwa rumaze kwimenyekanisha ko ari rwo.





- Umurongo w'itegeko rya Interface (CLI):** Itegeko rya `umurizo` riboneka muri CLI ku gikoresho cose aho Umurizo ushizwe. Iyi CLI iraguha uburenganzira bwo gukora vyose mu karere: gufatanya (`tailscale up`), gusuzuma uko ibintu vyifashe (`tailscale status` kugira ngo ubone abo mu runganwe rwawe bahuye), gukosora (`tailscale ping <ip>`), n'ibindi. Hari mbere n'ibiranga **vy'umwihariko kuri CLI** canke biteye imbere kuruta, nk'akarorero:





  - `umurizo hejuru --kwamamaza-inzira=192.168.0.0/24` kwamamaza inzira y'urubuga,
  - `umurizo wo hejuru -- kwamamaza-isohoka-uruzitiro` kugira ngo ushireho imashini yawe nk'uruzitiro rwo gusohoka,
  - `umurongo w'umurizo --kwemera-inzira=ukuri` (canke `--isohoka-urudodo=<IP>`) kugira ngo ukoreshe inzira canke ukoreshe urudodo rwo gusohoka,
  - `umurizo ip -4` kugira ngo ugaragaze IP y'umurizo w'igikoresho,
  - `ugufunga/ugufungura` (niba ukoresha *tailnet-lock*, ikintu c'umutekano giteye imbere),
  - canke `dosiye y'umurizo yohereze <node>` kugira ngo ukoreshe **Taildrop** (dosiye yoherezwa hagati y'ibikoresho).


CLI ni ngirakamaro cane ku ma server atagira ibishushanyo vya Interface, no ku kwandika ibikorwa bimwe bimwe. **Itandukaniro mu gukoresha:** Ivyiyumviro vyinshi vy'ishimikiro bishobora gukorwa biciye ku rubuga canke biciye ku CLI. Nk'akarorero, kwongerako igikoresho bikorwa mu gusaba biciye kuri console, canke mu gukoresha `tailscale up` ku gikoresho no kwemeza biciye ku rubuga. Navyo, guhindura izina ry'igikoresho bishobora gukorwa biciye kuri console canke n'`umurongo w'umurizo --izina ry'umushitsi`. **Mu ncamake**, urubuga rwa console ni rwiza cane ku bijanye n’uburongozi bw’urubuga rw’isi yose (na cane cane ku mashini/abakoresha benshi), mu gihe CLI ari nziza cane ku bijanye no kugenzura neza imashini yatanzwe, inyandiko z’ubuhinga, canke gukoresha kuri sisitemu idafise GUI.



## 4. Gukoresha Umurizo ku Mutaka



Umbrel ni urubuga ruzwi cane rwo kwiyakira (cane cane rukoreshwa ku bice vya Bitcoin/Lightning n’ibindi bikorwa vy’ukwiyakira, biciye ku App Store yayo). Kugira ngo ushiremwo no gutunganya Umbrel, turagusavye gukurikira inyigisho zacu:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Gukoresha Umbrel na Tailscale hamwe ni ikintu gishimishije cane, kuko Umbrel ikoresha mu buryo bworoshe igice ca Tailscale. Ehe ingene Tailscale ifatanya na Umbrel n'ico izana:



### 4.1 Gushiramwo umutaka no kuwutunganya





- Gushiramwo Tailscale ku Mutaka:** Umutaka ufise porogaramu yemewe y’umurizo muri App Store yayo. Gushiramwo ntivyoba vyoroshe:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Urupapuro rw'ikoreshwa ry'umurizo mu iduka ry'ikoreshwa rya Umbrel*



Uvuye ku rubuga rwa Interface, fungura App Store, urondere **Tailscale** hanyuma ukande *Install*. Haciye amasegonda makeyi, iyo porogarama irashirwa ku Mutaka. Iyo uyifunguye, Umbrel yerekana urupapuro ruguha uburenganzira bwo guhuza urudodo rwawe na Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Igishushanyo c'ihuriro ry'umurizo muri Interface ya Umbrel*



Gusa **kanda kuri "Injira "**, bizokujana kuri paji y'ukwemeza Tailscale:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Huza na Tailscale biciye ku muntu atanga akaranga*



Ushobora kwemeza biciye kuri konti yawe ya Tailscale (Google/GitHub/n'ibindi) canke winjize imeyili yawe. Mu bisanzwe, kuri Umbrel, Interface iragusaba gusura [https://injira.tailscale.com](https://injira.tailscale.com) maze winjire - ivyo vyemeza ko porogarama ya Umbrel Tailscale ari iyo.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Ivyemezo vy'uko igikoresho ca Umbrel gifatanye n'urubuga rwa Tailscale*



Iyo umaze gukora, Umutaka wawe uri "mu" mu rubuga rwawe rwa Tailscale maze ukaboneka kuri console yawe ufise izina (nk'akarorero *umutaka*). Ushobora rero gukanda kuri IP Address y’ibikoresho vyawe kugira ngo uyikope, ubone IPv6 Address canke MagicDNS yawe ifatanye n’igikoresho cawe.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Igikoresho c'ubuyobozi c'umurizo kigaragaza ibikoresho vyinshi bihuye, harimwo n'umutaka*




### 4.2 Ushobora gushika kure ku bikorwa vya Umbrel



Umbrel imaze gufatanya na Tailscale, **ushobora gushika kuri Interface Umbrel n’ibikoresho bikoreshwa kuri yo, uri aho hose, nk’aho woba uri ku rubuga rw’aho uba**. Ivyo ni bimwe mu vyiza nyamukuru kuruta Tor.



Ugushikira biroroshe cane: aho gukoresha `umbrel.local` (ikora gusa ku rubuga rwawe rwo mu karere), ukoresha IP ya Umbrel yawe Address (`http://100.x.y.z`) uhereye ku gikoresho cose gifatanye n'urubuga rwawe rwo mu karere. Ivyo bikora aho woba uri canke ukoresha internet iyihe (4G, Wi-Fi ya bose, network y’amashirahamwe).



**Ingero z'ibikorwa vyakiriwe na Umbrel bishobora gushikwako biciye ku rugero rw'umurizo:**





- Interface umutaka mukuru**: Shika ku rubuga rwawe rw'umutaka wanditse `http://100.x.y.z` mu mucukumbuzi wawe
- Bitcoin node**: Gucungera node yawe ya Bitcoin ata guhagarara, reba guhuza n'imibare
- Igikoresho c'umuravyo**: Koresha ThunderHub, RTL canke ibindi bikoresho vyo gucunga umuravyo bifise inyishu ihita
- Mempool**: Raba ibikorwa vya Bitcoin na Mempool ata gucererwa kwa Tor
- noStrudel**: Shika ku bikorwa vyawe vya Nostr vyakiriwe ku Mutaka



**Huza ama wallets yo hanze na Bitcoin yawe canke nodes z'umuravyo biciye ku Tailscale:**



Tailscale kandi ishobora gutuma amasakoshi yawe ya Bitcoin na Lightning ashizwe ku bindi bikoresho ashobora gufatanya n’uruzitiro rwawe rwa Umbrel:





- Sparrow wallet (Bitcoin)**: Iyi Wallet Bitcoin yo hanze ishobora kwifatanya na server yawe y'umuyagankuba ukoresheje IP Address:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Gutunganya umukozi w'umuyagankuba w'ibanga muri Sparrow wallet ukoresheje IP ya Umbrel Address*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Urutonde rw'amazina y'ibanga y'abakozi ba Electrum muri Sparrow n'umutaka IP Address*



Soma ubuyobozi bwacu bwose bwo gutunganya Sparrow wallet n'uruzitiro rwawe rwa Bitcoin:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (Umuravyo)**: Uyu Muravyo ugendagenda Wallet ushobora gufatanya n’urudodo rwawe rw’Umuravyo kuri Umbrel. Aho gutunganya iherezo nk'`.onion', gusa ushireho IP y'umurizo w'umutaka wawe n'icuma ca Lightning API. Iryo huriro rizoba ry’aho nyene ugereranyije na Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Gutunganya Zeus kugira ngo yifatanye n'umurongo w'umuravyo biciye ku nzira y'umurizo* IP Address



Kugira ngo utunganye Zeus n'urudodo rwawe rw'umuravyo, raba inyigisho yacu ido n'ido:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Kugira ngo umenye vyinshi ku vyerekeye Lightning Network n’ingene ikora kuri Umbrel, genda kuri:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Inyungu kuri Tor



Umbrel itanga uburyo bwo gushika kure biciye kuri Tor (mu gutanga aderesi `.onion` ku bikorwa vyayo vy'urubuga). Naho Tor ifise akamaro ko kuba ibanga (kutamenyekana) kandi idasaba kwiyandikisha, benshi mu bakoresha basanze **Tor igenda buhoro kandi idashikamye** mu gukoresha buri musi (amapaji arafunguka buhoro, igihe kigahera, n'ibindi) - *"Umbrel via Tor is so slow "* bamwe baridodomba.



Tailscale itanga muri rusangi **ukwihuta, guhagarara gato** guhuza, nk'uko umuduga unyura ataco uhinduye (canke biciye ku nzira yihuta) aho guca mu nzira 3 za Tor. Ikindi, Tailscale itanga ubumenyi bw'"urubuga rw'aho hantu": IPs z'ibanga zirakoreshwa, kandi ibikorwa bishobora gufatwa ku ikarita ataco bimaze (nk'akarorero, umuvuduko w'urubuga rwa SMB kuri \100.x.y.z).



Ivyo bivuzwe, Tor irafise akamaro ko kuba yegerejwe kandi "ivuye mu gasandugu" kuri Umbrel, mu gihe Tailscale irimwo kwizigira uwundi muntu (canke kwakira umutwe). Tor nayo ni ngirakamaro ku gukoresha ata mukiriya (kuva ku mucukumbuzi wa Tor uwo ari we wese, ushobora kuraba Umbrel UI, mu gihe Tailscale isaba umukiriya ashizwe ku gikoresho co gukoresha).



**Mu guca irya n’ino**, ku gukoresha mu buryo bukorana (Lightning wallets, interfaces z’urubuga zikunda gukoreshwa), Tailscale itanga ihumure n’umuvuduko bishimishije ugereranyije na Tor, ku giciro c’ugushingira ku bintu bikeyi vyo hanze. Abantu benshi bahitamwo gukoresha *vyompi*: Tailscale ku musi ku musi, na Tor nk’igisubizo canke gusangira uburenganzira n’umuntu batamutumiye muri VPN yabo.



### 4.4 Umutekano



Mu gukoresha Tailscale na Umbrel, urinda gushiramwo Umbrel kuri Internet. Igikoresho ca Umbrel gishobora gushikirwa gusa n’ibindi bikoresho vyawe vyemewe biri mu ruzitiro rw’inyuma, bikagabanya cane igitero (nta port yugururiye abanyamahanga, nta ngorane yo gutera kuri servisi y’urubuga biciye kuri Internet).



Ivyiyumviro birashizwe mu mfuruka (WireGuard) vyongeye ku mfuruka iyo ari yo yose ibikorwa vyawe biriko birakora (nk’akarorero mbere na HTTP yo mu mutima iri mu mugende). Ushobora gukoresha Tailscale ACLs kugira ngo, nk'akarorero, ubuze igikoresho kinaka c'umurizo gushika kuri Umbrel nimba ushaka gucapura urubuga. Umbrel ubwayo ntibona itandukaniro - yiyumvira ko iriko irakorera abantu bo mu karere.



---

Kugira ngo usozere iki gice, gushiramwo Tailscale kuri Umbrel bisaba gusa gukanda bike kandi **bitera imbere cane mu kuronka** urudodo rwawe rwitunganije. Uzoshobora gutwara Umbrel n’ibikorwa vyayo uri aho hose, ata nkomanzi kandi neza, nk’aho woba uri i muhira. Iyi ni umuti w’ingirakamaro cane cane ku bikorwa vy’igihe nyaco (Lightning) bishikirwa n’uguhagarara kwa Tor, canke muri rusangi ku muntu wese yikorera arondera ubufatanye bworoshe bw’ibanga. Vyose ata port n’imwe yerekana ku gasandugu kawe, kandi ata n’ugutunganya urubuga kugoranye.



## 5. Uburongozi buteye imbere n'ikoreshwa



### 5.1 Ibirango biteye imbere vy'umurizo



**Uburongozi bw'urubuga:** Console y'uburongozi (login.tailscale.com) iragufasha gucunga ibikoresho vyawe, kubona amahuzwa no gutunganya amategeko yo kwinjira.



**MagicDNS:** Itorera umuti amazina y'ibikoresho (nk'akarorero `raspberrypi.tailnet.ts.net`) kugira ngo wirinde gufata mu mutwe aderesi za IP.



**ACL na access control:** Sigura neza uwushobora gushika ku kintu kiri mu rubuga rwawe biciye ku mategeko ya JSON, vyiza cane mu gutandukanya ibikoresho bimwebimwe canke kubuza gushika ku bikorwa bimwebimwe.



**Device Sharing** igufasha gutumira umuntu ngo akoreshe imashini yihariye atamuhaye uburenganzira bwo gukoresha urubuga rwawe rwose.



**Subnet Router:** Imashini ya Tailscale ishobora gukora nk’irembo ry’urubuga rwose, igatuma umuntu ashobora gushika ku bikoresho bitagira Tailscale (IoT, amacapiro, n’ibindi) biciye ku mashini imwe itunganijwe.



**Exit Node:** Koresha imashini nk'irembo rya Internet kugira ngo usohoke n'IP yayo. Ni ngirakamaro kuri Wi-Fi ya bose canke guca ku nzira y’ubutaka.



**Taildrop:** Uburyo butekanye bwo gukoresha AirDrop, bushobora kugufasha guhindura amadosiye hagati y’ibikoresho vyawe vya Tailscale, uko vyoba biri kwose canke aho biri kwose. Udakunze AirDrop, ikoreshwa gusa mu bidukikije vya Apple no mu kuba hafi, Taildrop ikora hagati y’ibikoresho vyawe vyose (Windows, Mac, Linux, Android, iOS), naho vyoba biri mu bihugu bitandukanye. Amadosiye arungikwa ataco akora hagati y’ibikoresho bifise ubuhinga bwo gukingira amakuru kuva ku mpera kugeza ku mpera, ataco biciye kuri server nyamukuru. Koresha umurongo w'itegeko `dosiye y'umurizo cp` canke igishushanyo ca Interface bivanye n'uburyo bwawe.



### 5.2 Kugereranya n'ibindi bisubizo



**Vs OpenVPN:** Tailscale yoroshe cane gutunganya (nta ports zo gufungura, nta gucunga icemeza) ariko birimwo kwisunga servisi y’uwundi muntu. OpenVPN iragenzurwa neza, ariko isaba ubuhinga bwinshi.



**Nk’umuhiganwa ataco akora, ZeroTier ikorera kuri Layer 2 (Ethernet), ishoboza gutangaza/gutangaza vyinshi, mu gihe Tailscale ikorera kuri Layer 3 (IP). ZeroTier itanga uburyo bwinshi bwo guhindura urubuga, mu gihe Tailscale ikunda gukoresha neza.**



**Vs Tor:** Tor itanga ubutamenyekana Tailscale idatanga, ariko iragenda buhoro cane. Tor irashizwe ahantu hamwe kandi ntibisaba konti, mu gihe Tailscale yihuta kandi itanga ubumenyi bumeze nk’ubwa LAN.



**Igitabo ca Vs WireGuard:** Tailscale ikoresha ubuhinga bwose bwo gucunga urufunguzo n'uguhuza ivyo WireGuard raw isaba ko ukora n'amaboko. Ni WireGuard + uburongozi bworoshe Layer.



Mu gusozera, Tailscale yishize ahantu nk’umuti w’iki gihe, woroshe, ubereye gukoresha umuntu ku giti ciwe n’imigwi mito mito. Ku ba purists b’ubugenzuzi bwose, Headscale itanga ubundi buryo bwo kwiyakira.



## 6. Insozero



**Ivyiza vya Tailscale:** Tailscale itanga inyungu nyinshi zo kwiyakira:





- Ukworoha n'ubushobozi** - Gushiramwo vyihuse ku mbuga zose ata n'imiterere y'urubuga igoye. Ivy’ugutwara abantu bikurikira inzira igororotse cane hagati y’amamashini yawe (P2P mesh), n’ubushobozi bw’umurongo wa WireGuard kandi nta server yo hagati yo guhagarika ubushobozi bwo gukora.
- Umutekano n’uguhinduranya** - Gushiramwo amakuru kuva ku mpera kugeza ku mpera, kugabanya uburebure bw’igitero, n’ibintu biteye imbere (ACL, SSO/MFA authentication). Ikora mbere inyuma ya NATs canke uriko uragenda, n’ama subnet routers n’ama exit nodes kugira ngo uhuze n’ivyo ukeneye.



**Imipaka:** Kandi uzirikane:





- Ivyerekeye hanze** - Mu buryo bwayo busanzwe, iyo serivisi yizigira ibikorwa remezo vya Tailscale Inc. Ivyo bishobora gukurwaho biciye ku Headscale (uburyo bwo kwiyakira).
- Ibindi bigoranye** - Kode y’inkomoko yugaye igice, imipaka ya verisiyo y’ubuntu ku mikoreshereze imwe imwe iteye imbere, nta gushigikira Layer 2 (gutangaza/gutangaza vyinshi), n’ugukenera gukoresha Internet kugira ngo umuntu ashobore gukorana n’abandi.



**Tailscale ni nziza ku bantu ku giti cabo n’imigwi mito mito, abahinguzi bakeneye kuronka ibikoresho bitandukanye, abatangura VPN n’abakoresha telefone ngendanwa. Ku masosiyete asaba ubugenzuzi bwose, ibindi bisubizo nka Headscale canke WireGuard bishobora kuba vyiza.**



**Gushaka Headscale ku bijanye n'ukwiyakira, API na DevOps (Terraform), canke ubundi buryo nka Innernet (bisa ariko vy'ukwiyakira) na Netmaker.**



Tailscale ni igikoresho gihambaye co kwiyakira, bivuye ku kworoha kwaco n’ubushobozi bwaco, bituma ibikorwa remezo vyawe vy’ibanga bishobora gushikirwa nk’aho vyoba biri mu gicu, mu gihe uguma ugenzura i muhira.



## 7. Ibikoresho vy'ingirakamaro



### Inyandiko zemewe





- Ikigo c'inyandiko z'umurizo**: [docs.tailscale.com](https://docs.tailscale.com) - Inyandiko z'icongereza zishitse, ubuyobozi bwo gushiramwo, inyigisho n'ibimenyetso vy'ubuhinga.
- Uko Umurizo ukora**: [Uko Umurizo ukora](https://tailscale.com/blog/ingene-umurizo-ukora) - Ingingo idondora neza ingene Umurizo ukora imbere.
- Impinduka**: [umurizo.com/impinduka](https://imirizo.com/impinduka) - Gukurikirana ivyagezwe n'ibintu bishasha.



### Inyobora ngirakamaro





- Ivyigwa vya Homelab**: [Ivyigwa vyo mu nzu] - Ivyigwa vyihariye vyo kwiyakira.
- Gutegura Igikoresho co Gusohoka**: [Igikoresho co Gusohoka](https://Igikoresho co Gusohoka) - Inyobora ido n'ido yo gutunganya Igikoresho co Gusohoka.
- Koresha **Taildrop**: [umurizo.com/kb/1106/umurizo](https://umurizo.com/kb/1106/umurizo) - Kwimurira amadosiye hagati y'ibikoresho vya Tailscale.



### Ibigereranyo





- Umurizo n’ibindi bisubizo**: [umurizo.com/gereranya](https://umurizo.com/gereranya) - Igereranyo ry’ido n’ido n’ibindi bisubizo vya VPN n’ivy’urubuga (ZeroTier, OpenVPN, n’ibindi).



### Umugyango





- Reddit**: [r/Ikigereranyo c'Umurizo](https://www.reddit.com/r/Ikigereranyo c'Umurizo/) - Ibiganiro, ibibazo n'ibisubizo.
- GitHub**: [github.com/umurizo/umurizo](https://github.com/umurizo/umurizo) - Kode y'inkomoko y'umukiriya, aho wokurikirana iterambere no gutanga raporo y'ingorane.
- Discord**: [amatati.gg/umurongo w'umurizo](https://amatati.gg/umurongo w'umurongo) - Umuryango w'abakoresha n'abategura.



Tailscale ihora itanga ibintu bishasha n’ibintu bishasha. Raba [urubuga rwabo rwemewe](https://tailscale.com/blog/) kugira ngo ubone amakuru mashasha n’ivyigwa.