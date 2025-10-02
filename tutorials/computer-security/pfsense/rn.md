---
name: pfSense
description: Gushiramwo Pfsense
---
![cover](assets/cover.webp)



___



*Iyi nyigisho ishingiye ku bintu vy’umwimerere vya Florian BURNEL vyasohowe kuri [IT-Connect](https://www.it-connect.fr/). Uruhusha [CC KURI-NC 4.0](ku rubuga rwacu/uruhusha/ku-NC/4.0/). Hariho amahinduka akomeye yagizwe mu nyandiko y’intango y’umwanditsi kugira ngo inyigisho igere ku gihe.*



___



![Image](assets/fr/027.webp)



## I. Ugushikiriza



pfSense ni ubuhinga bwo gukoresha buntu, bufise inkomoko yuguruye, buhindura mudasobwa iyo ari yo yose, server yihariye canke igikoresho c’ubuhinga bwa hardware mu buryo bukora cane, bushobora guhindurwa cane. Ishingiye kuri FreeBSD kandi izwi cane kubera ubuhinga bwayo buhamye kandi bukomeye, pfSense imaze imyaka irenga cumi n’itanu ishiraho ingingo ngenderwako y’ibihome vy’umuriro vy’inkomoko yuguruye ku bucuruzi, ubutegetsi bwo mu karere n’abakoresha bo mu rugo basaba.



Ibikorwa vyayo nyamukuru vyarateye imbere cane uko imyaka yagenda irarenga, kandi vyarateye imbere uko habaho verisiyo nshasha. Kugeza ubu, pfSense itanga:





- Uburongozi bushitse, bushingiye ku rubuga rwa Interface Interface rwa none, rusanzwe kandi rutekanye.
- Igihome c’umuriro gikora neza cane gifise ubufasha bwa NAT buteye imbere (harimwo NAT-T) n’uburongozi bw’amategeko y’ibice.
- Infashanyo y’ivy’ubuhinga bwa none, ishoboza gukoranya canke gusubiramwo amahuzu ya Internet.
- Serveri ya DHCP n’ivy’ugutanga amakuru.
- Ugushikira cane kubera CARP protocol ku bijanye n’ugutsindwa n’ubushobozi bwo gutunganya amatsinda ya pfSense.
- Uburinganire bw'umuzigo hagati y'amahuza menshi canke amaserveri.
- Infashanyo yuzuye ya VPN: IPsec, OpenVPN na WireGuard (isubirira L2TP, ubu ntaco imaze).
- Urugi rwo gutunganirizwa rwo gucungera ukwinjira kw'abashitsi, cane cane mu bidukikije vya bose canke mu mahoteli.



pfSense kandi ifise uburyo bwo kwagura amapaki butuma vyoroha kwongerako ibintu biteye imbere nk’umuvugizi w’ibintu bibonerana (Squid), ukuyungurura URL canke IDS/IPS (Snort canke Suricata) bivuye ku rubuga rwa Interface.



pfSense itangazwa ku bikoresho vy'ibice 64 gusa, bihuye n'impanuro za FreeBSD ziriho ubu. Ishobora gushirwa ku bikoresho bisanzwe (PCs, rack servers) canke ku bikoresho vy’ubuhinga buke nk’ibikoresho vya Netgate canke amasandugu amwe amwe y’ubuhinga buke x86, afise ububasha bwinshi cane kuruta amasandugu ya kera ya Alix.



Ubwa nyuma, birabereye kwibuka ko pfSense isaba nibura interfaces zibiri z’urubuga rw’umubiri: imwe yerekeye zone y’inyuma (WAN) n’iyindi yerekeye urubuga rw’imbere (LAN). Bivanye n’ingene ibikorwa remezo vyawe bikomeye (DMZ, VLAN, WAN nyinshi), vyoshobora gukenerwa izindi interfaces nyinshi kugira ngo ukoreshe neza ubushobozi bwavyo.



## II. Gukuraho ishusho



Verisiyo nshasha ya pfSense, igihe nandika iyi nyigisho, ni 2.8 (yasohotse muri Ruheshi 2025). Ushobora gukuraho ishusho ya ISO canke dosiye yo gushiramwo ihuye n'ibidukikije vyawe vy'ibikoresho vy'ubuhinga bwa none ku rubuga rwemewe:





- [Kuvanaho pfSense](ku rubuga/)



Urubuga rwo gukuraho ruraguha uburenganzira bwo guhitamwo:





- Ubwubatsi (muri rusangi **AMD64** ku bikoresho vyose vy’ubuhinga bwa none).
- Ubwoko bw’ishusho (**Igikoresho co gushiramwo USB Memstick** co gushiramwo biciye ku nkoni ya USB, **Igikoresho co gushiramwo ISO** co guturira canke guhindura mu buryo bw’impwemu).
- Indorerwamo yo gukuraho iri hafi, kugira ngo ushiremwo umuvuduko mwiza.



Ku bipfuza gukoresha pfSense mu bidukikije vy’ivy’impwemu (Proxmox, VMware ESXi, Ivy’impwemu...), ishusho ya **OVA** na yo iraboneka. Iyi mashini y’ivy’impwemu yiteguye gukoreshwa iratuma umuntu ashobora gushiramwo ibintu vyinshi be n’ugutunganya ibintu mu ntango. Urabe ko gusa utunganya ibikoresho vyatanzwe (CPU, RAM, interfaces z’urubuga) bivanye n’umuzigo witezwe n’ubuhinga bwawe bw’urubuga.



Imbere yo gushiramwo, turagusavye gusuzuma ubutungane bwa dosiye yavanwe mu kugenzura **SHA256** itangwa kuri paji yemewe yo gukuraho. Ivyo bituma iyo shusho itahindurwa canke ngo yononekare.



## III. Gushiramwo



Muri aka karorero, ugushiraho bikorwa ku mashini ikoresha VirtualBox. Uburyo buguma ari bumwe cane ku mashini y’umubiri canke ku yindi hypervisor iyo ari yo yose, kiretse ku bijanye n’ugucungera ibikoresho vy’ukuri.



### 1. Ibisabwa bikeyi ku bikoresho



Ku bijanye n'ugushiraho, turagusaba:





- 1 GB RAM n’iyirengeye (**2 GB canke n’ibindi ni vyiza kugira ngo ushobore gukoresha izindi mpapuro canke ubufasha bwa ZFS**).
- 8 GB y'umwanya kuri disk (20 GB canke irenga ni vyiza ku mitunganyirize iteye imbere, cane cane iyo uriko urashiramwo ububiko bwa proxy, IDS/IPS canke ibitabo vy'ido n'ido).
- Nibura interfaces zibiri z’uruja n’uruza (imwe ya WAN, iyindi ya LAN). Mu VirtualBox, wongere ku mirongo ya VM imbere yo gutangura.



### 2. Gutangura



Gutera ishusho ISO yakuweho nk'umuduga w'amaso mu VirtualBox, canke winjize urufunguzo rwa USB nimba uriko urashiramwo ku mashini igaragara. Mu gutangura, urutonde rwo gutangura ruraboneka:



Niwaba udahisemwo amahitamwo yose, pfSense izotangura ubwayo n'amahitamwo y'imbere inyuma y'amasegonda make. Kanda urufunguzo "**Enter**" kugira ngo utangure gutangura bisanzwe.



![Image](assets/fr/027.webp)



Igihe menu nyamukuru ibonetse, uce ukanda ningoga kuri buto ya "**I**" kugira ngo utangure gushiramwo.



![Image](assets/fr/001.webp)



### 3. Amagenamiterere y'intango



Igishushanyo ca mbere kigufasha gushinga amaparametere makeyi y'akarere, nk'ugushiramwo imyandikire n'ugushiramwo inyuguti. Ivyo bikoresho birakenewe mu bihe vyihariye (ama klavye atari ayasanzwe, amasanamu y’uruhererekane, indimi zo mu buseruko). Ku bikoresho vyinshi, gumana agaciro mburabuzi maze uhitemwo "**Emera aya magenamiterere**".



![Image](assets/fr/002.webp)



### 4. Guhitamwo uburyo bwo gushiramwo



Hitamwo "**Gushiramwo vyihuse/Biyoroshe**" kugira ngo ukoreshe ugushiramwo kwikoresha n'amahitamwo akenewe. Ubu buryo burafuta disiki yatowe maze bugatunganya pfSense n'ugucapura mburabuzi.



![Image](assets/fr/003.webp)



Hazoboneka imburi, yerekana ko amakuru yose ari kuri disiki azokurwaho. Wemeze na "**Ni vyiza**".



Ico gikoresho gica gikopa amadosiye akenewe kuri disiki. Bivanye n’ibikoresho vyawe, ivyo bishobora gutwara kuva ku masegonda makeyi gushika ku minota mikeyi.



### 5. Guhitamwo nyamukuru



Igihe uwushiramwo akusavye guhitamwo ubwoko bw'intanga, usige "**Standard Kernel**" yatowe. Iyi kernel rusangi irabereye neza cane ku bikorwa bisanzwe, haba kuri PC, server canke VM.



### 6. Iherezo ryo gushiramwo no gusubira gutangura



Igihe gushiramwo, hitamwo "**Reboot**" kugira ngo wongere ufungure imashini yawe ku nkuru yawe nshasha ya pfSense.



**Iciyumviro gihambaye**: ukureho ishusho ya ISO canke uce urufunguzo rwa USB rwo gushiramwo imbere yo gusubira gufungura, kugira ngo wirinde gusubira gufungura porogarama y’ugushiramwo igihe uzosubira gufungura.



## IV. Gutangura pfSense ku ncuro ya mbere



Ku ntango ya mbere, pfSense itegerezwa gutunganirizwa kumenya no gutanga neza imirongo yayo y’urubuga (WAN, LAN, DMZ, VLANs, n’ibindi). Kumenya neza amakarata yawe y’urubuga ni ngombwa kugira ngo wirinde amakosa yose yo gutunganya yoshobora kukubuza gushika ku rubuga rwa Interface canke gutuma uruhome rwawe rw’umuriro rudakora.



Igihe pfSense itanguye, iramenya ubwayo kandi igatanga urutonde rw’imirongo yose y’urubuga iriho, yerekana MAC Address kuri buri imwe. Ivyo bituma vyoroha kubitandukanya.



### 1. VLANs



Ikibazo ca mbere kijanye n’ugutunganya ama VLAN. Kuri iyi ntambwe, ku bijanye n’imiterere y’ishimikiro, ntituzoba turiko turakoresha VLAN iyo ari yo yose. Rero kanda urufunguzo "**N**" kugira ngo usimbuke iyi ntambwe.



![Image](assets/fr/004.webp)



### 2. WAN na LAN Interface Assignment.



pfSense rero iragusaba gusobanura Interface izokoreshwa kuri WAN (ugukoresha Internet). Ushobora guhitamwo hagati ya:





- Injira izina rya Interface n'amaboko (ni vyiza ku bidukikije vy'ukuri).
- Koresha ukumenya kwihuta ukanda "**A**". Iyi nzira ni ngirakamaro ku nzira y'umushitsi, igihe cose intsinga zawe z'urubuga zihuye kandi amahuza akora.



![Image](assets/fr/005.webp)



Muri aka karorero, turatunganya WAN n’amaboko. Injira izina nyaryo rya Interface. Ku rubaho rwa Intel, izina rizoba kenshi "**em0**" munsi ya FreeBSD, ariko rishobora guhinduka bivanye n'ibikoresho. Nk'akarorero, ikarita ya Realtek izogaragara kenshi nka "**re0**".



![Image](assets/fr/006.webp)



Subiramwo iyo nzira nyene kugira ngo usobanure Interface LAN. Aha, dukoresha "**em1**".



pfSense yemeza ko Interface LAN ikoresha firewall na NAT kugira ngo ikingire urubuga rwawe rw’imbere no gucunga ubuhinduzi bwa Address.



Niba ufise izindi nzira z’umubiri, urashobora gutunganya izindi nzira z’inyongera (DMZ, Wi-Fi, VLANs zihariye) kuri iyi ntambwe. Interface yose yumvikana isaba ikarita y’urubuga ihuye canke Interface y’ukuri. Ku bijanye n’ugutunganya ivy’intango, tuzokwifatanya na WAN na LAN.



Igihe ibikorwa bimaze kurangira, pfSense yerekana incamake itomoye y’uguhuza hagati y’imirongo y’umubiri n’ibikorwa vyahawe. Wemeze na "**Y**".



### 3. Igikoresho ca PfSense



Iyo iyo ntambwe irangiye, pfSense console menyu nyamukuru iraboneka. Itanga uburyo bwinshi bw’ingirakamaro bwo gukoresha uburongozi butaziguye, nko gusubiramwo ijambobanga ry’urubuga, gusubira gufungura, gusubira gushiramwo imiterere canke gusubira gutanga interfaces.



![Image](assets/fr/007.webp)



Uzobona kandi incamake y'imiterere y'urubuga, harimwo IP ya Interface LAN Address, akenshi **192.168.1.1**. Iyi ni Address uzokenera kwinjira mu mucukumbuzi wawe kugira ngo ushikire urubuga rw'ubuyobozi rwa Interface.



**Iciyumviro**: Niba urubuga rwawe rw'imbere rukoresha urutonde rwa Address rutandukanye, hitamwo "**2)** Shiraho Interface(s) IP Address" mu rutonde kugira ngo ushireho IP Address ibereye ibidukikije vyawe.



Ku mburabuzi, iyo Interface WAN yawe ihuye n'agasanduku canke modem itunganijwe na DHCP, pfSense izoca ibona IP ya bose Address. Ushobora rero kwungukira ku gukoresha Internet ubwo nyene mu gufatanya umukiriya na pfSense Interface LAN.



## V. Ukwinjira ubwa mbere ku rubuga rwa Interface



Igihe igikorwa ca mbere co gutangura kirangiye kandi imirongo y’urubuga ikaba yaratunganijwe, urashobora gushika ku rubuga rwa pfSense rwa Interface kugira ngo uheze kandi utunganye neza imirongo yawe.



### 1. Uguhuza kwa mbere



Huza mudasobwa ku nzira ya LAN (canke LAN ya Interface y’ukuri iri muri hypervisor yawe) hanyuma uyihe IP Address mu rutonde rumwe iyo bikenewe (ku buryo busanzwe, pfSense ihita itanga Address biciye kuri DHCP kuri LAN).



Mu mucukumbuzi wawe, genda kuri Address yerekanwa na konsole (ku buryo busanzwe `https://192.168.1.1`). Zirikana ko pfSense isaba HTTPS mbere no ku guhuza kwa mbere - rero witege imburi y'icete c'ukwisinya, ushobora kwirengagiza mu kwongerako ikintu kidasanzwe.



Igishushanyo co kwinjira kiraboneka. Ivyemezo mburabuzi ni:




- Izina ry'ukoresha:** `umuyobozi`
- Ijambobanga:** `pfsense`



Ivyo bimenyetso bizohindurwa mu gihe c'umuhinga w'imiterere y'intango.



## VI. Gutegura Umupfumu



Ku guhuza kwa mbere, pfSense iragusaba gukurikira **Umuhinga wo gutegura**. Turagusavye cane ko uyikoresha kugira ngo umenye neza ko ibipimo vyose vy’ingenzi bisobanuwe neza.



### 1. Ivyagezwe rusangi



Urashobora:




- Sobanura izina ry'umushitsi n'indangarubuga y'aho hantu (akarorero: `pfsense` na `lan.local`).
- Sigura abakozi ba DNS maze uhitemwo nimba pfSense ikwiye gukoresha DNS ya ISP yawe canke igikorwa co hanze (Cloudflare, OpenDNS, Quad9...).



### 2. Akarere k'isaha



Erekana isaha y'urubuga rwawe kugira ngo inyandiko n'ingengabihe bihure (nk'akarorero `Uburayi/Paris`).



### 3. Itunganywa rya WAN



Gutunganya ihuriro rya WAN:




- Ivyategekanijwe ni **DHCP** (bihagije nimba uri inyuma y'agasanduku).
- Niba ufise IP idahinduka, shiramwo amaparametere (IP idahinduka, mask, irembo, DNS) n’amaboko.
- Niba ari ngombwa, sobanura ivyemezo vya VLAN canke PPPoE (bisanzwe kuri bamwe mu ba ISP).



### 4. Itunganywa rya LAN



Umupfumu asaba guhindura urubuga rwa LAN rwa mbere. Nimba ufise umugambi wihariye wo gutorera umuti, ubu ni igihe co kuwuhindura.



### 5. Guhindura ijambobanga ry'umuyobozi



Gukingira pfSense yawe mu gushinga ijambobanga rikomeye ry'ukoresha `admin`.



## VII. Gusuzuma no kuvugurura



Mbere yo gukoresha uruhome rwawe, urabe neza ko ufise verisiyo nshasha ya:





- Genda kuri **Sisitemu > Guhindura**.
- Hitamwo umurongo wo guhindura (kenshi **Ushikamye**).
- Suzuma ko hariho ibintu bishasha maze ubishire mu ngiro.



Ni iciyumviro ciza gukoresha amatangazo y'ivugurura kugira ngo ukomeze umenye ivy'umutekano.



## VIII. Kubika imiterere



Imbere yo guhindura ibintu bikomeye, shira mu ngiro ingingo ngenderwako y'ububiko:





- Genda kuri **Isuzuma > Gusubizaho no Gusubizaho**.
- Gukuraho kopi y'imiterere y'ubu (`config.xml`).
- Bibike ahantu hatagira umutekano (ibinyamakuru vyo hanze vy’ibanga).



Ku bidukikije bihambaye cane, zirikana ububiko bw’imiterere bwite kuri server yo hanze canke biciye ku nyandiko ya porogarama.



## IX. Ibikorwa vyiza inyuma yo gushiramwo



Kugira ngo uheze igikorwa cawe n’amahoro yo mu mutima:





- Guhindura amategeko y'uruhome rw'umuriro**: ku buryo busanzwe, pfSense yemera uruja n'uruza rwose rusohoka kuri LAN kandi igahagarika uruja n'uruza rwinjira kuri WAN. Uhindure ayo mategeko nk’uko bisabwa.
- Gutegura uburyo bwo gushika ku rubuga rwa Interface ukoresheje WAN gusa biciye kuri VPN canke n’amategeko ya IP.
- Gushoboza amatangazo**: gutegura umukozi wa SMTP kugira ngo yakire imburi (ibinanirwa, ivyagezwe, amakosa).
- Shiraho **ivyagutse** vy’ingirakamaro: nk’akarorero, IDS/IPS (Ivyuma, Suricata), ivy’ugucungera DNS (pfBlockerNG).



Uruhome rwawe rwa pfSense ubu rurakora, rwiteguye kurinda urubuga rwawe. Kubera ubushobozi bwayo bwo guhinduranya n’umuryango ukora, ufise igikoresho gikomeye, gishobora guhindurwa gishobora guhura n’ivyo uzokenera muri kazoza (multi-WAN, VLAN, VPN y’urubuga ku rubuga, urubuga rw’inyagano, n’ibindi).



Raba inyandiko zizwi ([docs.netgate.com](https://docs.netgate.com/pfsense/ru/latest/)) ubudasiba kugira ngo ubone ibintu bishasha kandi urabe neza ko imiterere yawe iri ku gihe kandi itekanye.