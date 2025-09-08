---
name: OPNsense
description: Je, ninawezaje kusakinisha na kusanidi firewall ya OPNsense?
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Florian BURNEL yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Huenda mabadiliko yamefanywa kwa maandishi asilia.*



___



## I. Uwasilishaji



Katika somo hili, tutakuwa tukiangalia ngome ya chanzo huria ya OPNsense. Tutaangalia vipengele vyake kuu, sharti, na jinsi ya kusakinisha suluhisho hili linalotegemea FreeBSD.



Kabla ya kuanza, unapaswa kujua kwamba **OPNsense na pfSense zote ni ngome za chanzo huria** kulingana na FreeBSD. Tunaweza kusema kwamba pfSense ni kaka mkubwa wa aina ya OPNsense, kwani mwisho ni Fork iliyoundwa mnamo 2015. Hatimaye, ni muhimu kusema kwamba tangu 2017, **OPNsense imebadilisha kwa HardenedBSD badala ya FreeBSD**. HardenedBSD ni toleo lililoboreshwa la FreeBSD, lenye vipengele vya juu vya usalama



OPNsense inajulikana kwa mtumiaji wake wa kisasa zaidi Interface na **mwako wa kusasisha mara kwa mara**. Hakika, ratiba ya sasisho ya OPNsense inajumuisha matoleo mawili makubwa kwa mwaka, ambayo husasishwa kila baada ya wiki mbili au zaidi (kusababisha matoleo madogo). Ufuatiliaji huu ni wa kuvutia sana kwa kulinganisha na pfSense, ikiwa tunaangalia matoleo ya jumuiya ya ufumbuzi huu.



![Image](assets/fr/050.webp)



## II. Vipengele vya OPNsense



OPNsense ni mfumo wa uendeshaji ulioundwa kufanya kazi kama ngome na kipanga njia, ingawa vipengele vyake ni vingi na vinaweza kupanuliwa kwa kusakinisha vifurushi vya ziada. Inafaa kwa matumizi ya uzalishaji, hutumiwa hasa kwa usalama wa mtandao na usimamizi wa mtiririko.



### A. Sifa kuu



Hapa kuna baadhi ya vipengele muhimu vya OPNsense:





- Firewall na NAT**: OPNsense hutoa utendakazi wa hali ya juu wa ngome-mtandao na uchujaji wa hali ya juu, pamoja na uwezo wa utafsiri wa mtandao wa Address (NAT).





- DNS/DHCP**: OPNsense inaweza kusanidiwa ili kudhibiti huduma za DNS na DHCP kwenye mtandao. Inaweza kufanya kazi kama seva ya DHCP, lakini pia inaweza kutumika kama kisuluhishi cha DNS kwa mashine kwenye mtandao wa ndani. Dnsmasq pia imeunganishwa na chaguo-msingi.





- VPN**: OPNsense inasaidia itifaki kadhaa za VPN, ikiwa ni pamoja na IPsec, OpenVPN na WireGuard, kuwezesha miunganisho salama ya ufikiaji wa mbali kwa vituo vya kazi vya rununu au unganisho la tovuti.





- Wakala wa wavuti**: OPNsense inajumuisha seva mbadala ya wavuti ili kudhibiti na kuchuja ufikiaji wa Mtandao. Inaweza pia kutumika kuchuja maudhui na kudhibiti ufikiaji wa mtandao.





- Usimamizi wa Bandwidth (QoS)**: OPNsense inatoa vipengele vya usimamizi wa Ubora wa Huduma (QoS) ili kutanguliza trafiki ya mtandao na kudhibiti vyema kipimo data cha mtandao.





- Lango lililofungwa**: kipengele hiki hukuwezesha kudhibiti ufikiaji wa mtumiaji kwa mtandao kupitia ukurasa wa uthibitishaji (msingi wa ndani, vocha, n.k.). Ni kipengele kinachotumika kwa mitandao ya umma ya Wi-Fi.





- IDS/IPS**: OPNsense huunganisha Suricata ili kutoa utendakazi wa kutambua na kuzuia uvamizi (IDS/IPS) ili kulinda mtandao dhidi ya mashambulizi.





- Upatikanaji wa juu (CARP)**: OPNsense inaauni CARP (*Itifaki ya Kawaida ya Upungufu ya Address*) kwa upatikanaji wa juu kati ya ngome nyingi za OPNsense, kuhakikisha kuwa huduma inasalia amilifu hata kukitokea hitilafu ya maunzi.





- Kuripoti na Ufuatiliaji**: OPNsense hutoa zana za kuripoti na ufuatiliaji katika wakati halisi ili kufuatilia utendakazi wa mtandao (kwa NetFlow) na kugundua matatizo yanayoweza kutokea, kutokana na uundaji wa kumbukumbu. Hii ni pamoja na michoro. Zana ya Monit imeunganishwa kwenye OPNsense na kuwezesha usimamizi wa ngome yenyewe.



### B. Vifurushi vya ziada



Huu ni muhtasari tu wa vipengele vinavyotolewa na OPNsense. Kwa kuongezea, **orodha ya kifurushi** inayofikiwa kutoka kwa usimamizi wa OPNsense Interface hukuruhusu **kuboresha ngome kwa utendakazi wa ziada**. Hizi ni pamoja na mteja wa ACME, wakala wa Wazuh, huduma ya NTP Chrony, na Caddy kama proksi ya kurudi nyuma.



![Image](assets/fr/051.webp)



## III. Masharti ya OPNsense



Kwanza kabisa, unahitaji kuamua ni wapi utasakinisha OPNsense. Kuna suluhisho kadhaa zinazowezekana, pamoja na usanikishaji kwenye:





- Hypervisor kama mashine pepe, iwe Hyper-V, Proxmox, VMware ESXi, n.k.
- Mashine kama mfumo wa *chuma-tupu*. Hii inaweza kuwa PC ndogo ambayo hufanya kama ngome.



Unaweza pia kununua **kifaa kinachoweza kupachikwa cha OPNsense** kupitia duka letu la mtandaoni.



Unahitaji kuzingatia rasilimali za maunzi zinazohitajika ili kuendesha OPNsense. Hii imefafanuliwa kwenye [ukurasa huu wa hati](https://docs.opnsense.org/manual/hardware.html).



**Rasilimali za chini na zinazopendekezwa kwa uzalishaji:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Hatimaye, **mahitaji yako ya rasilimali yanategemea zaidi ya yote idadi ya miunganisho itakayodhibitiwa**, na kwa hivyo kwenye **mahitaji yako ya kipimo data**. Kwa kuongeza, unahitaji **kukumbuka huduma ambazo zitawashwa na kutumika** (proksi, ugunduzi wa kuingilia, n.k...) kwani zinaweza kuwa na CPU na/au njaa ya RAM.



Utahitaji pia picha ya ISO ya usakinishaji wa OPNsense, ambayo unaweza kuipakua kutoka [tovuti rasmi](https://opnsense.org/download/). Kwa usakinishaji kwenye VM, chagua "**dvd**" kama aina ya picha ili kupata picha ya ISO (na ufanye unachopenda nayo...). Kwa usakinishaji kupitia ufunguo wa USB unaoweza kuwashwa, chagua chaguo la "**vga**" ili kupata faili ya "**.img**".



![Image](assets/fr/048.webp)



Utahitaji pia kompyuta kwa usimamizi na majaribio ya OPNsense.



## IV. Mpangilio wa lengo



Lengo letu ni





- Unda mtandao pepe wa ndani (192.168.10.0/24 - LAN)**, ambao unaweza kufikia Mtandao kupitia ngome ya OPNsense. Kwa matumizi ya uzalishaji, hii inaweza kuwa mtandao wa ndani, kebo na/au Wi-Fi.
- Washa na usanidi NAT** ili VM katika mtandao pepe wa ndani ziweze kufikia Mtandao
- Washa na usanidi seva ya DHCP kwenye OPNsense** ili kusambaza usanidi wa IP kwa mashine za siku zijazo zilizounganishwa kwenye mtandao pepe wa ndani.
- Sanidi ngome** ili kuruhusu LAN inayotoka tu kwa mtiririko wa WAN katika HTTP (80) na HTTPS (443).
- Sanidi ngome** ili kuruhusu LAN pepe kutumia OPNsense kama kisuluhishi cha DNS (53).



Ikiwa unatumia jukwaa la Hyper-V, hii itakupa uwakilishi ufuatao:



![Image](assets/fr/033.webp)



## V. Kusakinisha ngome ya OPNsense



### A. Inatayarisha ufunguo wa USB unaoweza kuwashwa



Hatua ya kwanza ni kuandaa midia ya usakinishaji: **kitufe cha USB kinachoweza kuwashwa na OPNsense**. Bila shaka hii ni hiari ikiwa unafanya kazi katika mazingira ya mtandaoni, lakini kwa vyovyote vile unahitaji kupakua picha ya ISO ya usakinishaji wa OPNsense.



Baada ya kupakua, utapata **hifadhi iliyo na picha katika umbizo la ".img "**. Unaweza **kuunda fimbo ya USB inayoweza kuwashwa** na programu mbalimbali, ikiwa ni pamoja na **balenaEtcher**: rahisi zaidi kutumia. Zaidi ya hayo, programu itatambua picha kwenye kumbukumbu, kwa hivyo huna haja ya kuipunguza kabla.





- [Pakua balenaEtcher](https://etcher.balena.io/)



Baada ya programu kusakinishwa, chagua picha yako, ufunguo wako wa USB kisha ubofye "Mweko! Subiri kidogo.



![Image](assets/fr/049.webp)



Sasa uko tayari kusakinisha.



### B. Kuweka Mfumo wa OPNsense



Anzisha mashine inayopangisha OPNsense. Unapaswa kuona ukurasa wa kukaribisha sawa na ule ulio hapa chini. Kwa sekunde chache, skrini iliyoonyeshwa itaonekana kwenye dirisha. Acha mchakato uendeshe mkondo wake...



![Image](assets/fr/019.webp)



Picha ya OPNsense imepakiwa kwenye mashine, ili mfumo uweze kufikiwa katika hali ya "**live**", yaani kuhifadhiwa kwa muda kwenye kumbukumbu.



![Image](assets/fr/025.webp)



Kisha utakuja kwa Interface sawa na iliyo hapa chini. Ingia kwa kuingia "**kisakinishaji**" na nenosiri "**opnsense**". Tafadhali kumbuka kuwa kibodi ni **QWERTY** kwa sasa. Katika hatua hii, tutaweza **kuanzisha mchakato wa usakinishaji wa OPNsense**.



![Image](assets/fr/026.webp)



Mchawi mpya huonekana kwenye skrini. Hatua ya kwanza ni kuchagua mpangilio wa kibodi unaolingana na usanidi wako. Kwa kibodi ya AZERTY, chagua chaguo "**Kifaransa (vifunguo vya lafudhi)**" kutoka kwenye orodha, kisha ubofye mara mbili**.



![Image](assets/fr/027.webp)



Hatua ya pili ni kuchagua kazi ya kufanywa. Hapa, tutafanya usakinishaji kwa kutumia **mfumo wa faili wa ZFS**. Jiweke kwenye mstari wa "**Sakinisha (ZFS)**" na uthibitishe na **Ingiza**.



![Image](assets/fr/028.webp)



Katika hatua ya tatu, chagua "**stripe**" kwani mashine yetu ina vifaa vya **diski moja tu**: hakuna upungufu unaowezekana ili kupata hifadhi ya firewall na data yake. Hii ni muhimu hasa wakati wa kufunga kwenye mashine ya kimwili ili kulinda dhidi ya kushindwa kwa vifaa vya disk, kupitia kanuni ya RAID.



![Image](assets/fr/029.webp)



Katika hatua ya nne, bonyeza tu ** Enter ** ili kuthibitisha.



![Image](assets/fr/030.webp)



Hatimaye, thibitisha kwa kuchagua "**NDIYO**" na kisha ubonyeze kitufe cha **Ingiza**.



![Image](assets/fr/031.webp)



Sasa utahitaji kusubiri OPNsense inaposakinishwa... Mchakato huu unachukua kama dakika 5.



![Image](assets/fr/032.webp)



Baada ya usakinishaji kukamilika, tunaweza kubadilisha nenosiri la "**root**" kabla ya kuwasha upya. Chagua "**Nenosiri la Mizizi **", bonyeza ** Ingiza ** na uweke nenosiri "** mizizi **" mara mbili.



![Image](assets/fr/020.webp)



Hatimaye, chagua "**Kamilisha Kusakinisha**" na ubonyeze **Ingiza**. Chukua fursa hii **kutoa diski kutoka kwa kiendeshi cha DVD cha VM**. Katika mipangilio ya VM, unaweza pia kuweka boot ya kwanza kwenye diski.



![Image](assets/fr/021.webp)



Mashine pepe itaanza upya na kupakia mfumo wa OPNsense kutoka kwa diski, kwa kuwa tumeisakinisha hivi punde. Ingia na akaunti ya "mizizi" kwenye console, na nenosiri lako jipya (vinginevyo, nenosiri la msingi ni "**pnsense **").



### D. Kuunganisha violesura vya mtandao



Skrini iliyoonyeshwa hapa chini itaonekana. Chagua "**1**" na ubonyeze **Enter** ili kuhusisha kadi za mtandao za mashine na violesura vya OPNsense.



![Image](assets/fr/022.webp)



Kwanza, mchawi anakuuliza usanidi mkusanyiko wa viungo na VLAN. Bainisha "**n**" ili kukataa, na kila wakati, thibitisha jibu lako kwa **Ingiza**. Ifuatayo, unahitaji kugawa violesura viwili "**hn0**" na "**hn1**" kwa **WAN** na **LAN**. Kimsingi, "**hn0**" inalingana na WAN na Interface nyingine kwa LAN.



Hivi ndivyo inavyofanya kazi:



![Image](assets/fr/023.webp)



Sasa tunayo:





- Interface **LAN** inayohusishwa na kadi ya mtandao ya "**hn1**" na IPNsense chaguo-msingi ya IP Address, yaani **192.168.1.1/24**.
- Interface **WAN** inayohusishwa na kadi ya mtandao ya "**hn0**" na IP Address iliyopatikana kupitia **DHCP** kwenye mtandao wa ndani (shukrani kwa swichi yetu pepe ya nje).



Kwa chaguo-msingi, usimamizi wa OPNsense Interface unapatikana tu kutoka kwa LAN Interface, kwa sababu za wazi za usalama. Kwa hivyo ni lazima uunganishe kwenye ngome ya Interface LAN ili kutekeleza usimamizi. Ikiwa hili haliwezekani, unaweza kusimamia kwa muda OPNsense kutoka kwa WAN. Hii inahusisha kulemaza utendakazi wa ngome.



Ili kufanya hivyo, badilisha kwa hali ya ganda kupitia chaguo la "**8**" na uendesha amri ifuatayo:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Upatikanaji wa mfumo wa usimamizi wa OPNsense Interface



Utawala wa OPNsense Interface unaweza kufikiwa kupitia HTTPS, kwa kutumia IP Address ya LAN** Interface (au WAN). Kivinjari chako kitakupeleka kwenye ukurasa wa kuingia. Ingia na akaunti ya "mizizi" na nenosiri ulilochagua hapo awali.



![Image](assets/fr/034.webp)



Subiri sekunde chache... Utaombwa ufuate mchawi ili kutekeleza usanidi wa kimsingi. Bofya "**Inayofuata**" ili kuendelea.



![Image](assets/fr/036.webp)



Hatua ya kwanza ni kufafanua jina la mwenyeji, jina la kikoa, kuchagua lugha na kufafanua seva za DNS zitakazotumika kwa utatuzi wa jina. Kuweka chaguo la "**Wezesha Kitatuzi**" kutaruhusu ngome kutumika kama kisuluhishi cha DNS, ambacho kitakuwa muhimu kwa mashine katika LAN yetu pepe.



![Image](assets/fr/037.webp)



Endelea hadi hatua inayofuata. Mchawi hukupa chaguo la **kufafanua seva ya NTP kwa ulandanishi wa tarehe na saa**, ingawa tayari kuna seva zilizosanidiwa kwa chaguomsingi. Kwa kuongeza, ni muhimu kuchagua eneo la saa linalolingana na eneo lako la kijiografia (isipokuwa kama una mahitaji maalum).



![Image](assets/fr/038.webp)



Kisha inakuja hatua muhimu: **kusanidi Interface WAN**. Kwa sasa, imesanidiwa katika DHCP na itasalia katika hali hii ya usanidi, isipokuwa ungetaka kuweka IP tuli Address.



![Image](assets/fr/039.webp)



Bado kwenye ukurasa wa usanidi wa Interface WAN, unahitaji kubatilisha uteuzi wa chaguo la "**Zuia ufikiaji wa mitandao ya kibinafsi kupitia WAN**" ikiwa mtandao kwenye upande wa WAN unatumia anwani ya faragha. Hii labda itakuwa hivyo ikiwa unaendesha Maabara, na kwa hivyo inaweza kukuzuia kufikia Mtandao.



![Image](assets/fr/040.webp)



Kisha, unaweza **kufafanua neno la siri la "root "**, lakini hii ni hiari kwa sababu tayari tumeifanya.



![Image](assets/fr/041.webp)



Endelea hadi mwisho ili kuanzisha upakiaji upya wa usanidi. Ikiwa unahitaji kuendelea kuchukua udhibiti kupitia WAN, anzisha upya amri iliyo hapo juu mara tu mchakato huu utakapokamilika.



![Image](assets/fr/042.webp)



Hayo ndiyo yote yaliyopo kwake!



![Image](assets/fr/035.webp)



### Usanidi wa E. DHCP



Lengo letu ni kutumia seva ya OPNsense DHCP kusambaza anwani za IP kwenye LAN pepe. Ili kufanya hivyo, tunahitaji kufikia eneo la menyu hii:



```
Services > ISC DHCPv4 > [LAN]
```



**Kama unavyoona, DHCP tayari imewashwa kwa chaguomsingi kwenye LAN ** Ikiwa hupendi huduma hii, unapaswa kuizima. Ingawa tayari imewashwa na tunataka kuitumia, ni muhimu kukagua usanidi wake.



Ikihitajika, unaweza kubadilisha anuwai ya anwani za IP zitakazosambazwa: **192.168.10.10** hadi **192.168.10.245**, kulingana na mipangilio ya sasa.



![Image](assets/fr/046.webp)



Tunaweza pia kuona kwamba sehemu "**DNS seva**", "**Lango**", "**Jina la kikoa**", n.k., ni tupu kwa chaguomsingi. Kwa kweli, kuna urithi wa moja kwa moja wa chaguo fulani na maadili ya msingi kwa nyanja hizi mbalimbali. Kwa mfano, kwa seva ya DNS, IP Address ya Interface LAN itasambazwa, na hivyo kuwezesha ngome ya OPNsense kutumika kama kitatuzi cha DNS.



Hifadhi usanidi baada ya kufanya mabadiliko yoyote, ikiwa ni lazima.



![Image](assets/fr/047.webp)



Ili kujaribu seva ya DHCP, unahitaji kuunganisha mashine kwenye mtandao wa LAN wa ngome yako.



Mashine hii lazima ipate IP Address kutoka kwa seva ya OPNsense DHCP, na mashine yetu lazima iwe na ufikiaji wa mtandao. Ufikiaji wa mtandao lazima ufanye kazi. Tafadhali kumbuka kuwa ikiwa umelemaza kitendakazi cha ngome ili kufikia OPNsense kutoka kwa WAN, hii itazima NAT, kukuzuia kufikia Wavuti.



**Kumbuka**: ukodishaji uliotolewa kwa sasa wa DHCP unaonekana kutoka kwa usimamizi wa OPNsense Interface. Ili kufanya hivyo, nenda kwenye eneo lifuatalo: **Huduma > ISC DHCPv4 > Ukodishaji**.



![Image](assets/fr/045.webp)



### F. Kusanidi NAT na sheria za ngome



Habari njema ni kwamba sasa tunaweza kufikia utawala wa OPNsense Interface kutoka kwa LAN.



```
https://192.168.1.10
```



Baada ya kuingia kwenye OPNsense, hebu tugundue usanidi wa NAT. Nenda kwenye eneo hili: **Firewall > NAT > Nje **. Hapa unaweza kuchagua kati ya otomatiki (chaguo-msingi) na uundaji wa mwongozo wa sheria za NAT zinazotoka nje.



Chagua hali ya kiotomatiki kupitia chaguo la "**Kizazi otomatiki cha sheria zinazotoka za NAT**" na ubofye "**Hifadhi**" (kimsingi, usanidi huu tayari ndio unaotumika). Katika hali ya kiotomatiki, OPNsense yenyewe huunda sheria ya NAT kwa kila mtandao wako.



![Image](assets/fr/043.webp)



Kwa sasa, kompyuta zote zilizounganishwa kwenye LAN pepe "**192.168.10.0/24**" zinaweza kufikia Mtandao bila kizuizi. Hata hivyo, lengo letu ni kuzuia ufikiaji wa WAN kwa itifaki za HTTP na HTTPS, pamoja na DNS kwenye Interface LAN ya ngome.



Kwa hivyo tunahitaji kuunda sheria za ngome... Vinjari menyu kama ifuatavyo: **Firewall > Kanuni > LAN**.



**Kwa chaguo-msingi, kuna sheria mbili za kuidhinisha trafiki yote ya LAN inayotoka, katika IPv4 na IPv6**. Zima sheria hizi mbili kwa kubofya mshale wa Green upande wa kushoto kabisa, mwanzoni mwa kila mstari.



Kisha unda sheria tatu mpya za kuidhinisha **mtandao wa LAN** (yaani "**LAN net**") kwa:





- fikia maeneo yote kwa kutumia **HTTP**.
- fikia maeneo yote ukitumia **HTTPS**.
- omba **OPNsense** kwenye **Interface LAN** yake (yaani "**LAN Address**"), kupitia **Itifaki ya DNS** (hii inamaanisha kutumia ngome kama DNS), vinginevyo idhinisha kisuluhishi chako cha DNS kupitia IP Address yake.



Hii inatoa matokeo yafuatayo:



![Image](assets/fr/044.webp)



Kilichosalia ni kubofya "**Tekeleza mabadiliko**" ili kubadilisha sheria mpya za ngome ziwe za uzalishaji. **Tafadhali kumbuka kuwa mitiririko yote ambayo haijaidhinishwa kwa njia dhahiri itazuiwa kwa chaguomsingi



Mashine ya LAN inaweza kufikia Mtandao, kwa kutumia HTTP na HTTPS. Itifaki zingine zote zitazuiwa.



![Image](assets/fr/018.webp)



## IV. Hitimisho



Kwa kufuata mwongozo huu, utaweza kusakinisha OPNsense na kuanza mara moja. OPNsense hutoa anuwai ya vipengele ili kulinda na kudhibiti trafiki ya mtandao wako kwa ufanisi, na inafaa kutumika katika mazingira ya kitaaluma.



Usakinishaji huu ni mwanzo tu: jisikie huru kuchunguza menyu na kusanidi vipengele vingine ili kurekebisha OPNsense kulingana na mahitaji yako.