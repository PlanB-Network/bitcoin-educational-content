---
name: VirtualBox
description: Sakinisha VirtualBox kwenye Windows 11 na uunde VM yako ya kwanza
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Florian Burnel yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Huenda mabadiliko yamefanywa kwa maandishi asilia.*



___




## I. Uwasilishaji



Katika somo hili, tutajifunza jinsi ya kusakinisha VirtualBox kwenye Windows 11 ili kuunda mashine pepe, iwe ya kutumia Windows 10, Windows 11, Windows Server au usambazaji wa Linux (Debian, Ubuntu, Kali Linux, n.k.).



Mafunzo haya ya utangulizi kwa VirtualBox yatakusaidia kuanza na suluhu hii ya uboreshaji wa chanzo huria iliyotengenezwa na Oracle, ambayo ni bila malipo kabisa. Baadaye, mafunzo mengine yatawekwa mtandaoni ili kukupeleka ndani zaidi katika somo.



Linapokuja suala la uboreshaji wa kituo cha kazi, iwe kwa madhumuni ya majaribio kama sehemu ya mradi au wakati wa masomo yako ya TEHAMA, VirtualBox ni suluhisho zuri. Pia ni mbadala wa masuluhisho mengine kama vile Hyper-V, ambayo imeunganishwa kwenye Windows 10 na Windows 11 (pamoja na Windows Server), na VMware Workstation (inayotozwa) / VMware Workstation Player (bila malipo kwa matumizi ya kibinafsi).



Usanidi wangu: **kituo cha kazi cha Windows 11 ambapo nitasakinisha VirtualBox**, lakini unaweza kusakinisha VirtualBox kwenye Windows 10 (au toleo la zamani), na pia kwenye Linux. Kuhusu mashine pepe, VirtualBox inasaidia mifumo mbalimbali, ikiwa ni pamoja na Windows (k.m. Windows 10, Windows 11, Windows Server 2022, nk.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, nk), BSD (PfSense) na macOS.



## II. Pakua VirtualBox ya Windows 11



Ili kupakua VirtualBox kwa usakinishaji kwenye mashine ya Windows, kuna Address moja tu nzuri: [tovuti rasmi ya VirtualBox](https://www.virtualbox.org/wiki/Downloads) katika sehemu ya "**Vipakuliwa**". Bofya tu kwenye "Wapangishi wa Windows" ili kuanza kupakua hii inayoweza kutekelezwa, ambayo ni zaidi ya MB 100 kwa ukubwa.



![Image](assets/fr/025.webp)



## III. Kufunga VirtualBox kwenye Windows 11



### A. Inasakinisha VirtualBox



Kusakinisha VirtualBox** ni moja kwa moja, na mchakato ni sawa kwa matoleo yote ya Windows. Anza kwa kuzindua VirtualBox inayoweza kutekelezwa ambayo umepakua, kisha ubofye "**Inayofuata**".



![Image](assets/fr/026.webp)



Ufungaji huu unaweza kubinafsishwa, lakini ninapendekeza usakinishe vipengele vyote: ambayo ni kesi na uteuzi wa chaguo-msingi. Katika picha hapa chini, unaweza kuona Elements anuwai, pamoja na:





- Usaidizi wa USB wa VirtualBox** ili kuwezesha VirtualBox kutumia vifaa vya USB
- VirtualBox Bridged Network** ili kuunganisha usaidizi wa mtandao katika hali ya "Bridge" (mashine pepe inaweza kuunganisha moja kwa moja kwenye mtandao wako wa karibu)
- VirtualBox Host-only Network** ili kujumuisha usaidizi wa mtandao katika hali ya "Mpangishi-Pekee" (mashine pepe inaweza tu kuwasiliana na seva pangishi yako ya Windows 11 na mashine zingine pepe katika hali hii)



Bofya "**Inayofuata**" ili kuendelea.



![Image](assets/fr/001.webp)



Bofya "**Ndiyo**", ukikumbuka kwamba **mtandao utakatizwa kwa muda kwenye mashine yako ya Windows 11**, huku VirtualBox ikifanya marekebisho ya mtandao ili kusaidia aina tofauti za mtandao, ikiwa ni pamoja na hali ya Bridge.



![Image](assets/fr/002.webp)



Ukishathibitisha, usakinishaji utaanza... Na arifa ya "**Je, unataka kusakinisha programu ya kifaa hiki?**" itaonekana. Angalia chaguo la "**amini programu kutoka kwa Oracle Corporation**" na ubofye "**Sakinisha**". VirtualBox inahitaji kusakinisha viendeshi kadhaa kwenye kompyuta yako.



![Image](assets/fr/003.webp)



Usakinishaji sasa umekamilika! Angalia chaguo "**Anzisha Oracle VM VirtualBox 6.1.34 baada ya kusakinisha**" na ubofye "**Bofya**" ili kuzindua programu.



![Image](assets/fr/004.webp)



### B. Ongeza pakiti ya ugani



Bado kwenye tovuti rasmi ya VirtualBox (angalia kiungo kilichotangulia), unaweza kupakua kifurushi rasmi cha kiendelezi, kinachopatikana chini ya sehemu ya "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" kwa kubofya kiungo cha "**Mifumo yote inayotumika **". Pakiti hii itakuwezesha kuongeza utendaji wa ziada kwa VirtualBox: sio lazima kuiongeza, lakini inaweza kuwa na manufaa! Kwa mfano, inajumuisha usaidizi wa USB 3.0 katika VM, usaidizi wa kamera ya wavuti na usimbaji fiche wa diski.



Fungua VirtualBox, bonyeza "**Faili**" na kisha kwenye "**Mipangilio**" kwenye menyu.



![Image](assets/fr/005.webp)



Bofya kwenye "**Viendelezi**" upande wa kushoto (1), kisha kwenye kitufe cha "****" upande wa kulia (2) ili **kupakia kifurushi cha kiendelezi cha VirtualBox** ambacho umepakua (3).



![Image](assets/fr/006.webp)



Thibitisha kwa kubofya kitufe cha "**Usakinishaji**".



![Image](assets/fr/007.webp)



Bofya "**Sawa**": kifurushi rasmi cha kiendelezi sasa kimesakinishwa kwenye mfano wako wa VirtualBox!



![Image](assets/fr/008.webp)



Wacha tuendelee kwenye uundaji wa mashine yetu ya kwanza ya mtandaoni.



## IV. Kuunda VirtualBox VM yako ya kwanza



Ili kuunda mashine mpya pepe kwenye VirtualBox, bofya tu kitufe cha "**Mpya**" ili kuzindua kichawi cha kuunda VM. Kwa kuwa hii ni mara ya kwanza umeanzisha VirtualBox, ningependa kukupa maelezo machache zaidi kuhusu Interface na vitufe vingine.





- Mipangilio**: usanidi wa jumla wa VirtualBox (folda chaguo-msingi ya VM, usimamizi wa sasisho, lugha, mitandao ya NAT, viendelezi, n.k.)
- Ingiza**: leta kifaa pepe katika umbizo la OVF
- Hamisha**: Hamisha mashine iliyopo katika umbizo la OVF ili kuunda kifaa pepe
- Ongeza**: ongeza mashine pepe iliyopo kwenye orodha yako ya VirtualBox, katika umbizo la kawaida la VirtualBox (.vbox) au umbizo la XML.



Upande wa kushoto, sehemu ya "**Zana**" inatoa ufikiaji wa **vitendaji vya hali ya juu, haswa kwa kudhibiti mtandao pepe, lakini pia kwa kudhibiti uhifadhi wa VM**. Chini ya ingizo la "**Zana**", mashine zako pepe zitaongezwa baadaye.



![Image](assets/fr/009.webp)



### Mchakato wa kuunda A. VM



**Kama ukumbusho, VirtualBox inasaidia mifumo mingi ya uendeshaji, ikijumuisha Windows, Linux na BSD. Katika mfano huu, nitaunda mashine pepe ya Windows 11. Sehemu kadhaa zinahitaji kujazwa:





- Jina**: jina la mashine (hili ndilo jina litakaloonyeshwa kwenye VirtualBox)
- Folda ya mashine**: mahali pa kuhifadhi mashine ya kawaida, ukijua kuwa folda ndogo iliyo na jina la VM itaundwa mahali hapa.
- Aina**: aina ya mfumo wa uendeshaji, kulingana na OS unayotaka kusakinisha
- Toleo**: toleo la mfumo unaotaka kusakinisha, katika kesi hii Windows 11, kwa hivyo "**Windows11_64**"



Bofya "**Inayofuata**" ili kuendelea.



![Image](assets/fr/010.webp)



Kulingana na mfumo wa uendeshaji uliochagua katika hatua ya awali, **VirtualBox hutoa mapendekezo juu ya rasilimali za kugawia mashine pepe**. Hapa, tunazungumza juu ya RAM unayotaka kutenga kwa VM. Wacha tuchukue GB 4, kwa sababu hii inapendekezwa kwa Windows 11, lakini ikiwa huna rasilimali, taja 2 GB badala yake. **Endelea



**Kumbuka**: rasilimali zilizogawiwa kwa mashine pepe zinaweza kurekebishwa baadaye.



![Image](assets/fr/011.webp)



Kuhusu diski ya Hard inayohusika, tunaanza kutoka mwanzo, kwa hivyo tunahitaji kuchagua "**Unda diski ya Hard sasa**" ili VM iwe na nafasi ya kuhifadhi ili kusakinisha mfumo wa uendeshaji na kuhifadhi data. Bonyeza "** Unda **".



![Image](assets/fr/012.webp)



VirtualBox inasaidia fomati tatu tofauti za diski za Hard, ambayo ni tofauti kubwa ikilinganishwa na suluhisho zingine kama vile VMware na Hyper-V. Kuna fomati tatu za kuchagua kutoka:





- VDI**, umbizo rasmi la VirtualBox
- VHD**, ambayo ni umbizo rasmi la Hyper-V, ingawa umbizo jipya la VHDX linatumika mara nyingi zaidi siku hizi
- VMDX** ni umbizo rasmi la VMware kwa VMware Workstation na VMware ESXi



Ili kuunda mashine pepe ambayo itatumika tu kwenye mfano huu wa VirtualBox, chagua "**VDI**". Kwa upande mwingine, ikiwa diski pepe ya Hard itaambatishwa kwa seva pangishi ya Hyper-V baadaye, inaweza kuwa wazo nzuri kuanza na umbizo la VHD ili kuepuka kuibadilisha. Bonyeza "**Next**".



![Image](assets/fr/013.webp)



**Diski pepe inaweza kuwa ya nguvu au isiyobadilika kwa ukubwa **. Wakati inabadilika, faili inayowakilisha **diski pepe (hapa faili ya .vdi) itakua data inapoandikwa kwenye diski** hadi ifikie ukubwa wake wa juu zaidi, lakini haitapungua ikiwa data itafutwa. Kinyume chake, wakati ni wa ukubwa wa kudumu, ** nafasi ya hifadhi ya jumla imetengwa mara moja (na kwa hiyo imehifadhiwa) **, ambayo inaruhusu utendaji wa juu kidogo, lakini inachukua muda mrefu wakati disk virtual inapoundwa kwanza.



Binafsi, kwa majaribio ya mashine pepe na VirtualBox, ninaona hali ya "**Dynamically zilizotengwa **" inatosha.



![Image](assets/fr/014.webp)



**Hatua inayofuata ni kutaja ukubwa wa disk virtual **, kwa kuzingatia kwamba kwa default, disk itahifadhiwa kwenye saraka ya VM (hii inaweza kubadilishwa katika hatua hii). Nimeonyesha ukubwa wa GB 64 ili kuzingatia mahitaji ya Windows 11, lakini hapa tena, saizi ndogo inaweza kupewa. Bonyeza "** Unda **" ili kuunda VM!



![Image](assets/fr/015.webp)



Kwa wakati huu, VM iko kwenye orodha yetu, imesanidiwa, lakini mfumo wa uendeshaji haujasakinishwa. Tunahitaji kukamilisha usanidi wa VM kabla ya kuianzisha.



### B. Kukabidhi picha ya ISO kwa VirtualBox VM



Ili kusakinisha Windows 11, au mfumo mwingine wowote, tunahitaji vyanzo vya usakinishaji. Mara nyingi, tunatumia picha ya disk katika muundo wa ISO ili kufunga mfumo wa uendeshaji. **Ni muhimu kupakia picha ya Windows 11 ya ISO kwenye kiendeshi chetu cha DVD cha VM



Bofya kwenye VM kwenye orodha ya VirtualBox (1), kisha kwenye kitufe cha "**Configuration**" (2), ambayo inatoa ufikiaji wa usanidi wa jumla wa mashine hii ya mtandaoni. Menyu hii inatumika kudhibiti rasilimali (k.m. kuongeza RAM, kusanidi CPU, n.k.). Bofya kwenye "**Hifadhi**" upande wa kushoto (3), kwenye kiendeshi cha DVD ambapo inasema "**Tupu**" kwa sasa (4) kisha ubofye ikoni yenye umbo la DVD (5) na "**Chagua faili ya diski**".



![Image](assets/fr/016.webp)



Chagua picha ya ISO ya mfumo wa uendeshaji unaotaka kusakinisha, kisha ubofye Sawa. Hii ndio ninayopata:



![Image](assets/fr/017.webp)



Kaa katika sehemu ya "**Configuration**" ya VM, bado nina mambo machache ya kueleza.



### Muunganisho wa mtandao wa C. VM



Nenda kwenye sehemu ya "**Mtandao**" iliyo upande wa kushoto. Sehemu hii hukuwezesha kudhibiti mtandao wa mashine pepe: idadi ya violesura vya mtandao pepe (hadi 4 kwa VM), MAC Address, na hali ya ufikiaji wa mtandao (NAT, ufikiaji wa daraja, mtandao wa ndani, n.k.). **Kama ungependa mashine yako pepe ipate ufikiaji wa Mtandao, chagua "NAT" au "Ufikiaji wa Daraja"**, lakini hali hii ya pili inahitaji seva ya DHCP ili itumike kwenye mtandao wako, au itabidi usanidi IP Address wewe mwenyewe.



Kumbuka: Nitarudi kwenye sehemu ya mtandao kwa undani zaidi katika makala maalum.



![Image](assets/fr/018.webp)



### D. Idadi ya vichakataji mtandaoni



Kama kompyuta halisi, mashine pepe inahitaji RAM, diski ya Hard na kichakataji kufanya kazi. Tulipounda VM, unaweza kuwa umegundua kuwa mchawi haukujumuisha usanidi wa kichakataji. Hata hivyo, hii inaweza kusanidiwa wakati wowote kupitia kichupo cha "**Mfumo**", kisha "**Kichakata**", ambapo unaweza kuchagua idadi ya vichakataji pepe.



Kumbuka: chaguo la "**Wezesha VT-x/AMD-v lililowekwa**" linahitajika kwa uboreshaji uliowekwa.



Kwa upande wangu, mashine ya kawaida ina wasindikaji 2 wa kawaida:



![Image](assets/fr/019.webp)



**Usisite kuangalia sehemu zingine za menyu ya usanidi.



### E. Boot ya kwanza na usakinishaji wa OS



Kuanzisha mashine ya kawaida, chagua tu kwenye hesabu na ubofye kitufe cha "**Anza**". Dirisha la pili litafungua, kutoa muhtasari wa kuona wa VM.



![Image](assets/fr/020.webp)



Lo, ninapata hitilafu mbaya na mashine yangu ya mtandaoni haitaanza! Kosa ni "Kuingia kumeshindwa kwa mashine ya kawaida ..." na maelezo yafuatayo:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Kwa kweli, hii ni kawaida kwa sababu **kipengele cha uboreshaji hakijawezeshwa kwenye kompyuta yangu**! Ili kurekebisha tatizo hili, unahitaji kuanzisha upya kompyuta yako ili kufikia BIOS na kuwezesha virtualization.



![Image](assets/fr/021.webp)



Bila kusubiri, ninawasha upya kompyuta yangu na **bonyeza kitufe cha "SUPPR" ili kufikia BIOS** (ufunguo unaweza kutofautiana kulingana na mashine, na inaweza kuwa F2, kwa mfano) ya ubao wa mama wa ASUS. Ili kuamilisha uboreshaji, "Njia ya SVM" lazima iwezeshwe katika kesi yangu. Hapa tena, kutoka kwa ubao wa mama hadi mwingine, kutoka kwa mtengenezaji mmoja hadi mwingine, jina linaweza kubadilika. Tafuta chaguo za kukokotoa zinazorejelea **AMD-V** (kwa AMD CPU) au **Intel VT-x** (kwa Intel CPU).



![Image](assets/fr/022.webp)



Mara hii imefanywa, hifadhi urekebishaji na uanze upya mashine ya kimwili ... Wakati huu, **VirtualBox inaweza kuanzisha mashine ya kawaida ** na kupakia picha ya Windows ISO ili kufunga mfumo wa uendeshaji! 🙂



![Image](assets/fr/023.webp)



Kwenye mwenyeji wetu wa Windows 11, ambapo VirtualBox imewekwa, tunaweza kuona kwamba folda ya mashine ya Windows 11 ina faili mbalimbali.





- Faili ya VBOX** (katika umbizo la XML) inayolingana na usanidi wa VM (RAM, CPU, n.k.)
- Faili ya VBOX-PREV** ni chelezo ya usanidi uliopita
- Faili ya VDI** inalingana na diski halisi ya Hard katika hali ya nguvu, kwa hiyo kwa sasa ni GB 13 tu, ambapo ukubwa wake wa juu ni 64 GB.
- Faili ya NVRAM** ina hali ya BIOS ya mashine pepe, ambayo ni sawa na kumbukumbu isiyo tete ya mashine halisi.



![Image](assets/fr/024.webp)



## V. Hitimisho



**VirtualBox sasa iko kwenye mashine yetu ya kimwili ya Windows 11! Kilichosalia ni kunufaika nayo na kuunda mashine pepe!** Nitarudi kusakinisha Windows 11 katika VirtualBox VM katika makala nyingine. Kwa Windows 10, Windows Server au usambazaji wa Linux (Ubuntu, Debian, n.k.), hebu tukuongoze!