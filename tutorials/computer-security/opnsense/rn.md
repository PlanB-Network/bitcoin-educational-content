---
name: OPNsense
description: Ni gute noshiramwo no gutunganya uruhome rw’umuriro rwa OPNsense?
---
![cover](assets/cover.webp)



___



*Iyi nyigisho ishingiye ku bintu vy’umwimerere vya Florian BURNEL vyasohowe kuri [IT-Connect](https://www.it-connect.fr/). Uruhusha [CC KURI-NC 4.0](ku rubuga rwacu/uruhusha/ku-NC/4.0/). Birashoboka ko hari ivyo bahinduye mu canditswe c’intango.*



___



## I. Ugushikiriza



Muri iyi nyigisho, tuzoba turiko turaraba uruhome rw’umuriro rwa OPNsense. Turaza kuraba ibiranga cane, ibisabwa, n’ingene woshiramwo uwo muti ushingiye kuri FreeBSD.



Imbere yo gutangura, ukwiye kumenya ko **OPNsense na pfSense vyose ari ibihome vy’umuriro vy’inkomoko yuguruye** bishingiye kuri FreeBSD. Turashobora kuvuga ko pfSense ari umuvukanyi mukuru wa OPNsense, kuko iyo ya nyuma ari Fork yaremwe mu 2015. Ubwa nyuma, birahambaye kugaragaza ko kuva mu 2017, **OPNsense yahindukiye ikoresha HardenedBSD aho gukoresha FreeBSD**. HardenedBSD ni verisiyo ya FreeBSD, ifise ibintu vyiza vy'umutekano



OPNsense igaragara kubera umukoresha wayo wa none Interface na **ugusubiramwo kenshi**. Nkako, urutonde rwa OPNsense rwo guhindura ibintu rurimwo ibintu bibiri bikomeye bisohoka mu mwaka, ivyo bikaba bihindurwa inyuma y’indwi zibiri canke zirenga (bigatuma habaho ibintu bitobito bisohoka). Ivyo bikurikirana biraryoshe cane ugereranije na pfSense, nitwaba turavye ama versions y’abanyagihugu y’ivyo bisubizo.



![Image](assets/fr/050.webp)



## II. Ibirango vya OPNsense



OPNsense ni ubuhinga bwo gukoresha bugenewe gukora nk’uruhome rw’umuriro n’uruhome rw’umurongo, naho nyene ibintu vyabwo ari vyinshi kandi bishobora kwagurwa hakoreshejwe gushiramwo izindi mpapuro. Ibereye gukoreshwa mu guhingura, ikoreshwa cane cane mu gucungera umutekano w’urubuga no mu gucunga uruja n’uruza.



### A. Ibiranga nyamukuru



Aha niho hari bimwe mu bintu nyamukuru vya OPNsense:





- Firewall na NAT**: OPNsense itanga ubuhinga buteye imbere bwo gukingira umuriro n’ugucungera, hamwe n’ubushobozi bwo guhindura urubuga rwa Address (NAT).





- DNS/DHCP**: OPNsense ishobora gutunganirizwa gucunga ibikorwa vya DNS na DHCP ku rubuga. Ishobora gukora nk’umukozi wa DHCP, ariko kandi ishobora gukoreshwa nk’umukozi wa DNS ku mashini ziri ku rubuga rw’aho hantu. Dnsmasq nayo nyene irashizwemwo ku buryo busanzwe.





- VPN**: OPNsense ishigikira amategeko menshi ya VPN, harimwo IPsec, OpenVPN na WireGuard, bishoboza gukorana n’abantu mu buryo butekanye kugira ngo umuntu ashobore gushika kure ku bibanza vy’akazi vy’amatelefone ngendanwa canke gukorana n’ibindi bikoresho.





- Urubuga rwa interineti**: OPNsense irimwo urubuga rwo kugenzura no kuyungurura uburyo bwo gukoresha Internet. Ishobora kandi gukoreshwa mu gucungera ibirimwo no gucunga uburyo bwo gushika ku rubuga.





- Uburongozi bw’uburebure bw’uruja n’uruza (QoS)**: OPNsense itanga uburyo bwo gucunga uburyo bwo gukoresha (QoS) kugira ngo ushire imbere uruja n’uruza rw’uruja n’uruza rw’urubuga no gucunga neza uburebure bw’uruja n’uruza rw’uruja n’uruza.





- Captive portal**: iki gikoresho kigufasha gucunga uburyo abakoresha bashobora gushika ku rubuga biciye kuri paji y’ukwemeza (ishingiro ryo mu karere, amafaranga, n’ibindi). Ni ikintu gisanzwe gikoreshwa ku nzira za Wi-Fi za bose.





- IDS/IPS**: OPNsense ihuriza hamwe Suricata kugira ngo itange ibikorwa vyo kumenya no kwirinda (IDS/IPS) kugira ngo ikingire urubuga ibitero.





- Ugushikira cane (CARP)**: OPNsense ishigikira CARP (*Itegeko ry’Igihugu ry’Igihugu*) ku kuronka cane hagati y’ibihome vyinshi vya OPNsense, bigatuma igikorwa kiguma gikora mbere n’igihe ibikoresho bishobora gusenyuka.





- Gutanga raporo no kugenzura**: OPNsense itanga ibikoresho vyo gutanga raporo no kugenzura mu gihe nyaco kugira ngo ukurikirane ibikorwa vy’urubuga (na NetFlow) no kumenya ingorane zishobora kubaho, bivuye ku kurema ibitabo. Ivyo birimwo n’ibishushanyo. Igikoresho ca Monit kiri muri OPNsense kandi gishobora kugenzura uruhome rw’umuriro ubwarwo.



### B. Ibindi bikoresho



Ivyo ni incamake gusa y’ibintu bitangwa na OPNsense. Ikindi, **urutonde rw'amapaki** rushobora gushikwako n'ubuyobozi bwa OPNsense Interface ruragufasha **gutunganya uruhome rw'umuriro n'ibindi bikoresho**. Ivyo birimwo umukiriya wa ACME, umukozi wa Wazuh, igikorwa ca NTP Chrony, na Caddy nk’umuvugizi w’inyuma.



![Image](assets/fr/051.webp)



## III. Ibisabwa vya OPNsense



Mbere na mbere, ukeneye gufata ingingo y’aho uzoshira OPNsense. Hariho inyishu nyinshi zishoboka, harimwo no gushiramwo kuri:





- Igikoresho co gucungera nk'imashini y'ivy'impwemu, yaba Hyper-V, Proxmox, VMware ESXi, n'ibindi.
- Imashini nk'uburyo *bw'ivyuma*. Ivyo bishobora kuba mini PC ikora nk’uruhome rw’umuriro.



Ushobora kandi kugura **igikoresho ca OPNsense gishobora gushirwa ku ruhande** biciye ku iduka ryacu ryo kuri internet.



Ukeneye kwitwararika ibikoresho bisabwa kugira ngo ukoreshe OPNsense. Ivyo biradondaguwe kuri [iyi paji y’inyandiko](https://inyandiko.opnsense.org/igitabu/ibikoresho.html).



**Ibikoresho bikeyi n'ivyiza vyo gukoresha:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Ubwa nyuma, **ivyo usaba ku bijanye n'ibikoresho vyawe bivana cane cane n'umubare w'amahuza azocungirwa**, rero n'ivyo usaba ku bijanye n'uburebure bw'uruja n'uruza**. Ikindi, ukeneye **kuguma mu muzirikanyi ibikorwa bizokora kandi bikoreshwe** (proxy, gutahura intrusion, etc...) kuko bishobora kuba bikeneye CPU na/canke RAM.



Uzokenera kandi ishusho ya ISO y’ugushiraho OPNsense, ushobora kuyikura kuri [urubuga rwemewe](https://opnsense.org/download/). Kugira ngo ushire kuri VM, hitamwo "**dvd**" nk'ubwoko bw'ishusho kugira uronke ishusho ISO (kandi uyikore ivyo ukunda...). Kugira ngo ushiremwo biciye ku rufunguzo rwa USB rushobora gutangura, hitamwo "**vga**" kugira uronke dosiye "**.img**".



![Image](assets/fr/048.webp)



Uzokenera kandi mudasobwa yo gutwara no gupima OPNsense.



## IV. Imiterere y'intumbero



Intumbero yacu ni





- Gukora urubuga rw’imbere rw’ivy’ubuhinga (192.168.10.0/24 - LAN), rushobora gushika kuri Internet biciye ku ruhome rw’umuriro rwa OPNsense. Ku gukoresha mu gukora, ivyo bishobora kuba urubuga rwawe rwo mu karere, umugozi na/canke Wi-Fi.
- Gukoresha no gutunganya **NAT** kugira ngo VMs ziri mu rubuga rw'imbere zishobore gukoresha Internet
- Gukoresha no gutunganya umukozi wa DHCP kuri **OPNsense** kugira ngo ushire ahabona imiterere ya IP ku mashini zo muri kazoza zihuye n'urubuga rw'imbere
- Gutegura **uruhome rw'umuriro** kugira ngo rwemerere gusa LAN isohoka gushika kuri WAN mu HTTP (80) na HTTPS (443).
- Gutegura **uruhome rw’umuriro** kugira ngo LAN y’ukuri ikoreshe OPNsense nk’umutorera umuti wa DNS (53).



Niba ukoresha urubuga rwa Hyper-V, ivyo bizokuronsa ibi bikurikira:



![Image](assets/fr/033.webp)



## V. Gushiramwo uruhome rw'umuriro rwa OPNsense



### A. Gutegura urufunguzo rwa USB rushobora gufungurwa



Intambwe ya mbere ni ugutegura ibikoresho vyo gushiramwo: **urufunguzo rwa USB rushobora gufungurwa rufise OPNsense**. Ivyo ni ubusabe nimba uriko urakora mu bidukikije vy'ukuri, ariko uko biri kwose ukeneye gukuraho ishusho ya ISO y'ugushiraho OPNsense.



Uhejeje gukuraho, uronka **ububiko burimwo ishusho mu buryo bwa ".img "**. Ushobora **gukora USB stick ishobora gufunguka** ifise ibikorwa bitandukanye, harimwo **balenaEtcher**: yoroshe cane gukoresha. Ikindi, iyo porogarama izomenya ishusho iri mu bubiko, rero ntubwirizwa kuyikuramwo imbere y’igihe.





- [Gukuraho balenaEtcher](https://igitabu.balena.io/)



Iyo porogarama imaze gushirwamwo, uhitemwo ishusho yawe, urufunguzo rwawe rwa USB hanyuma ukande kuri "Flash! Rindira gato."



![Image](assets/fr/049.webp)



Ubu rero urateguye gushiramwo.



### B. Gushiramwo Sisitemu ya OPNsense



Gutangura imashini yakira OPNsense. Ushobora kubona urupapuro rw’akabazo rusa n’ururi aha hepfo. Mu masegonda makeyi, igicapo kizoboneka mw’idirisha. Reka iyo nzira igende...



![Image](assets/fr/019.webp)



Ishusho ya OPNsense ishirwa ku mashini, kugira ngo sisitemu ishobore gukoreshwa mu buryo bwa "**live**", ni ukuvuga ibitswe mu bubiko bw'igihe gito.



![Image](assets/fr/025.webp)



Hanyuma uzoshika ku Interface isa n’iyi iri musi. Injira ukoresheje "**umushiramwo**" n'ijambobanga "**opnsense**". Iyumvire ko klavye ari **QWERTY** muri iki gihe. Muri iki gihe, tuzotangura **ugushiramwo OPNsense**.



![Image](assets/fr/026.webp)



Umupfumu mushasha araboneka ku mugaragaro. Intambwe ya mbere ni uguhitamwo uburyo bwo gukoresha klavye bujanye n’ivyo ukoresha. Ku klavye AZERTY, hitamwo **"Igifaransa (imfunguruzo z'inyuguti)"** mu rutonde, hanyuma ukande kabiri.



![Image](assets/fr/027.webp)



Intambwe ya kabiri ni uguhitamwo igikorwa co gukora. Aha, tugiye gukora ugushiraho dukoresheje **uburyo bwa dosiye ZFS**. Ishire ku murongo wa "**Shiraho (ZFS)**" maze wemeze na **Injira**.



![Image](assets/fr/028.webp)



Mu ntambwe ya gatatu, uhitemwo "**stripe**" kuko imashini yacu ifise **disk imwe gusa**: nta redundancy ishoboka yo gukingira ububiko bw'uruhome rw'umuriro n'amakuru yayo. Ivyo birahambaye canecane iyo ushize ku mashini igaragara kugira ngo ukingire ukunanirwa kw’ibikoresho vya disiki, biciye ku ngingo ngenderwako ya RAID.



![Image](assets/fr/029.webp)



Mu ntambwe ya kane, ushobora gukanda **Enter** kugira ngo wemeze.



![Image](assets/fr/030.webp)



Ubwa nyuma, wemeze uhisemwo "**EGO**" hanyuma ukande urufunguzo **Enter**.



![Image](assets/fr/031.webp)



None uzobwirizwa kurindira OPNsense iriko irashirwaho... Ivyo bifata nk'iminota 5.



![Image](assets/fr/032.webp)



Igihe installation irangiye, turashobora guhindura ijambobanga "**root**" imbere yo gusubira gufungura. Hitamwo "**Ijambobanga ry'umuzi**", ukande **Enter** hanyuma winjize ijambobanga "**umuzi**" incuro zibiri.



![Image](assets/fr/020.webp)



Ubwa nyuma, uhitemwo "**Ushiremwo**" hanyuma ukande **Injira**. Fata aka karyo **ukureho disk muri DVD drive ya VM**. Mu mitunganyirize ya VM, ushobora kandi gushiramwo boot ya mbere kuri disk.



![Image](assets/fr/021.webp)



Iryo mashini ry’ivy’impwemu rizosubira gukora kandi rishiremwo ubuhinga bwa OPNsense kuri disk, kuko twamaze kuyishiramwo. Injira ukoresheje konti "umuzi" muri console, n'ijambobanga ryawe rishasha (ahandi ho, ijambobanga ry'imbere ni "**opnsense**").



### D. Guhuza imirongo y'urubuga



Igishushanyo kigaragara aha hepfo kizoboneka. Hitamwo "**1**" hanyuma ukande **Enter** kugira ngo ufatanye amakarita y'urubuga rw'imashini n'imirongo ya OPNsense.



![Image](assets/fr/022.webp)



Ubwa mbere, umupfumu aragusaba gutunganya amahuza n’ama VLAN. Sobanura "**n**" kugira ngo wanke, kandi igihe cose, wemeze inyishu yawe ukoresheje **Enter**. Inyuma y'aho, ukeneye gushiramwo izo nzira zibiri "**hn0**" na "**hn1**" kuri **WAN** na **LAN**. Mu ngingo ngenderwako, "**hn0**" ihuye na WAN n'iyindi Interface ihuye na LAN.



Ehe uko bigenda:



![Image](assets/fr/023.webp)



Ubu dufise:





- Interface **LAN** ifatanye n'ikarita y'urubuga "**hn1**" hamwe n'iyi IP Address, ni ukuvuga **192.168.1.1/24**.
- Interface **WAN** ifatanye n'ikarita y'urubuga "**hn0**" kandi ifise IP Address yaronswe biciye ku **DHCP** ku rubuga rw'aho hantu (bivuye ku muhinduzi wacu w'inyuma).



Ku mburabuzi, ubuyobozi bwa OPNsense Interface bushobora gushikwako gusa buvuye kuri LAN Interface, kubera imvo zigaragara z’umutekano. Utegerezwa rero kwifatanya na Interface LAN y’uruhome rw’umuriro kugira ngo ukore uburongozi. Niba ivyo bidashoboka, urashobora gukoresha OPNsense mu gihe gito ukoresheje WAN. Ivyo birimwo guhagarika igikorwa c’uruhome rw’umuriro.



Kugira ngo ubikore, hindukira mu buryo bw'igikoko biciye ku mahitamwo ya "**8**" hanyuma ukoreshe itegeko rikurikira:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Ushobora gushika ku buryo bwo gucunga OPNsense Interface



Ubuyobozi bwa OPNsense Interface bushobora gushikwako biciye kuri HTTPS, hakoreshejwe IP Address ya **LAN** Interface (canke WAN). Mucukumbuzi yawe izogutwara kuri paji yo kwinjira. Injira ukoresheje konti "root" n'ijambobanga wahisemwo mbere.



![Image](assets/fr/034.webp)



Rindira amasegonda make... Uzosabwa gukurikira umupfumu kugira ngo ukore ivy'ishimikiro. Fyonda "**Ibikurikira**" kugira ngo ukomeze.



![Image](assets/fr/036.webp)



Intambwe ya mbere ni ugusobanura izina ry’umushitsi, izina ry’itongo, guhitamwo ururimi no gusobanura server(s) ya DNS izokoreshwa mu gutorera umuti amazina. Gukomeza "**Enable Resolver**" bizotuma uruhome rw'umuriro rukoreshwa nk'umutorera umuti wa DNS, ivyo bizoba ngirakamaro ku mashini ziri muri LAN yacu y'ukuri.



![Image](assets/fr/037.webp)



Bandanya ku ntambwe ikurikira. Umupfumu aguha uburenganzira bwo **gusobanura umukozi wa NTP wo guhuza itariki n'isaha**, naho hariho umukozi asanzwe atunganijwe ku buryo busanzwe. Ikindi, ni ngombwa guhitamwo isaha ihuye n’aho uri (kiretse iyo ufise ibisabwa bidasanzwe).



![Image](assets/fr/038.webp)



Hanyuma haza intambwe ihambaye: **gutunganya WAN ya Interface**. Ubu, yatunganijwe muri DHCP kandi izoguma muri ubu buryo bwo gutunganya, kiretse wipfuza gushinga IP idahinduka Address.



![Image](assets/fr/039.webp)



Naho biri kuri paji y'imiterere ya Interface WAN, ukeneye gukuraho "**Guhagarika gushika ku nzira z'ibanga biciye kuri WAN**" nimba inzira iri ku ruhande rwa WAN ikoresha aderesi y'ibanga. Ivyo birashobora kuba ari ko biri iyo uriko urakoresha Lab, kandi ivyo bishobora kukubuza gukoresha Internet.



![Image](assets/fr/040.webp)



Igikurikira, ushobora **gusobanura ijambobanga "umuzi "**, ariko ivyo ni ubusabe kuko twamaze kubikora.



![Image](assets/fr/041.webp)



Bandanya gushika kw'iherezo kugira ngo utangure gusubiramwo ivy'imiterere. Niba ukeneye kubandanya ugenzura biciye kuri WAN, subiramwo itegeko riri hejuru iyo iyo nzira irangiye.



![Image](assets/fr/042.webp)



Ivyo ni vyo vyose birimwo!



![Image](assets/fr/035.webp)



### E. Gutunganya DHCP



Intumbero yacu ni ugukoresha umukozi wa OPNsense DHCP kugira ngo dusangire ama aderesi IP kuri LAN y’ukuri. Kugira ivyo tubikore, dukeneye gushika kuri iyi menyu:



```
Services > ISC DHCPv4 > [LAN]
```



**Nk'uko mubibona, DHCP irasanzwe ikoreshwa kuri LAN ** Niba udakunda iyi service, ukwiye kuyizimya. Naho nyene yamaze gukoreshwa kandi dushaka kuyikoresha, birahambaye ko dusubiramwo uko itunganijwe.



Niba bisabwa, urashobora guhindura urutonde rw'amaderesi IP azokwiragizwa: **192.168.10.10** gushika kuri **192.168.10.245**, bivanye n'ivyo ukoresha ubu.



![Image](assets/fr/046.webp)



Turashobora kandi kubona ko ivyicaro "**abakozi ba DNS**", "**Irembo**", "**Izina ry'indangarubuga**", n'ibindi, ari ubusa ku buryo busanzwe. Nkako, hariho iragi ry'amahitamwo amwamwe n'agaciro k'ivyo bibanza bitandukanye. Nk’akarorero, ku bijanye n’umurongo wa DNS, IP Address ya Interface LAN izokwiragizwa, bishoboze uruhome rw’umuriro rwa OPNsense gukoreshwa nk’umutorera umuti wa DNS.



Bika ivyagezwe umaze guhindura ivyo ari vyo vyose, nimba bikenewe.



![Image](assets/fr/047.webp)



Kugira ngo ugerageze server ya DHCP, ukeneye gufatanya imashini n’urubuga rwa LAN rwa firewall yawe.



Iyi mashini itegerezwa kuronka IP Address kuri server ya OPNsense DHCP, kandi imashini yacu itegerezwa kuba ifise uburenganzira bwo gushika ku rubuga. Internet itegerezwa gukora. Urashobora kubona ko iyo uzimye igikorwa c’uruhome rw’umuriro kugira ngo ushikire OPNsense ukoresheje WAN, ivyo bizozimya NAT, bikubuze gushika ku rubuga.



**Iciyumviro**: ubu ubukode bwa DHCP buboneka ku buyobozi bwa OPNsense Interface. Kugira ngo ubikore, genda aha hantu hakurikira: **Ibikorwa > ISC DHCPv4 > Amakodesha**.



![Image](assets/fr/045.webp)



### F. Gutunganya amategeko ya NAT n'uruhome rw'umuriro



Inkuru nziza ni uko ubu dushobora gushika ku buyobozi bwa OPNsense Interface tuvuye kuri LAN.



```
https://192.168.1.10
```



Tumaze kwinjira muri OPNsense, reka tubone uko NAT itunganywa. Genda aha hantu: **Uruhome rw'umuriro > NAT > Isohoka**. Aha ushobora guhitamwo hagati y'uguhingura amategeko ya NAT asohoka (default) n'uguhingura n'amaboko.



Hitamwo uburyo bwikora biciye ku "**Ivyaruka vyikora vy'amategeko ya NAT asohoka**" hanyuma ukande kuri "**Bika**" (mu ngingo ngenderwako, iyi ntunganyo ni yo isanzwe ikora). Mu buryo bwikora, OPNsense ubwayo irema itegeko rya NAT kuri buri nzira yawe.



![Image](assets/fr/043.webp)



Kugeza ubu, mudasobwa zose zifatanye n'urubuga rwa LAN "**192.168.10.0/24**" zirashobora gukoresha Internet ataco zibujijwe. Ariko rero, intumbero yacu ni uguhagarika uburenganzira bwo gukoresha WAN ku masezerano ya HTTP na HTTPS, hamwe na DNS kuri Interface LAN y’uruhome rw’umuriro.



Turakeneye rero gukora amategeko y'uruhome rw'umuriro... Suzuma muri menyu nk'uko bikurikira: **Uruhome rw'umuriro > Amategeko > LAN**.



**Kubera ko hariho amategeko abiri yemerera uruja n'uruza rwose rwa LAN, muri IPv4 na IPv6**. Nimuzimye ayo mategeko abiri mu gufyonda ku mwampi Green uri ibubamfu cane, ku ntango y’umurongo umwumwe wose.



Hanyuma ureme amategeko mashasha atatu yo kwemerera **urubuga rwa LAN** (ni ukuvuga "**urubuga rwa LAN**") ku:





- gushika ku ntumbero zose ukoresheje **HTTP**.
- gushika aho uja hose ukoresheje **HTTPS**.
- gusaba **OPNsense** kuri **Interface LAN** yayo (ni ukuvuga "**LAN Address**"), biciye ku **Itegeko rya DNS** (ivyo bisigura gukoresha uruhome rw'umuriro nk'DNS), ahandi ho wemerere umutorera umuti wawe wa DNS biciye ku IP Address yayo.



Ivyo bitanga igisubizo gikurikira:



![Image](assets/fr/044.webp)



Igisigaye ni ugukanda kuri "**Apply changes**" kugira ngo uhindure amategeko mashasha y'uruhome rw'umuriro ku gukora. **Iyumvire ko imigenderanire yose itemerewe izobuzwa ku buryo busanzwe.**



Ico gikoresho ca LAN gishobora gukoresha Internet, gikoresheje HTTP na HTTPS. Ibindi bimenyetso vyose bizobuzwa.



![Image](assets/fr/018.webp)



## IV. Iciyumviro



Niwakurikiza iyi nzira, uzoshobora gushiramwo OPNsense maze utangure ubwo nyene. OPNsense itanga ibintu vyinshi vyo gukingira no gucunga neza uruja n’uruza rw’urubuga rwawe, kandi irabereye gukoreshwa mu bibanza vy’umwuga.



Iyi installation ni intango gusa: ntutinye gutohoza menus no gutunganya ibindi bikoresho kugira ngo OPNsense ihure n’ivyo ukeneye.