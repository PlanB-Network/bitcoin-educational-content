---
name: Ntopng
description: Fuatilia mtandao wako na ntopng
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Florian Duchemin yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Huenda mabadiliko yamefanywa kwa maandishi asilia.*



___



## I. Uwasilishaji



**Iwe ni kuangalia utendakazi wa mtandao, ili kupata picha kamili ya matumizi au takwimu za utendakazi, ufuatiliaji wa mtiririko wa mtandao ni sehemu muhimu ya mtandao wa biashara**. Husaidia kutarajia mabadiliko kwenye miundombinu na husaidia kuhakikisha ubora wa matumizi kwa watumiaji (pia hujulikana kama QoE kwa *Ubora wa Uzoefu*, tofauti na QoS).



Ili kufanya hivyo, kuna mbinu nyingi na programu/itifaki zinazopatikana. Netflow, kwa mfano, iliyotengenezwa na Cisco, inaweza kutumika kurejesha takwimu za mtiririko wa IP kutoka kwa Interface, lakini matumizi yake yanazuiwa kwa vifaa vinavyotangamana.



Ndio maana katika somo hili nitawaletea **Ntop** na kukuonyesha jinsi ya kuitumia katika miundombinu yako ili kuweka macho kwenye matumizi ya mtandao wako.



Ntop ni programu huria ambayo inaweza kusakinishwa kwenye mashine yoyote ya Linux. Ni bila malipo na inaweza kukusanya data ifuatayo:





- Utumiaji wa Bandwidth
- Wateja wakuu
- Maeneo makuu
- Itifaki zilizotumika
- Maombi yaliyotumika
- Bandari zilizotumika
- Nk.



Sasa imepewa jina la **Ntopng (Kizazi Kipya)**, inatoa huduma nyingi za kimsingi bila malipo. Toleo la kibiashara linapatikana pia, linaloruhusu arifa zilizosanidiwa kutumwa kwa programu ya aina ya SIEM, au trafiki kuchujwa kwa sheria zilizobainishwa moja kwa moja kutoka kwa uchunguzi.



## II. Masharti



Ufungaji wa probe ya Ntop hutofautiana kulingana na vifaa na mazingira. Kwa hivyo sitakupa mwongozo wa hatua kwa hatua hapa, lakini nitaelezea uwezekano mbalimbali.



### A. Hali ya ubaoni



Ikiwa una pfSense, OPNSense au Endian firewall katika uzalishaji, au hata kituo cha kazi cha Linux kilicho na NFTables, habari njema! Unaweza kusakinisha Ntopng moja kwa moja na kuanza kufuatilia miingiliano yako.



Faida ya mbinu hii ni kwamba hauhitaji vifaa vya ziada. Kwa upande mwingine, huongeza utumiaji wa rasilimali, kwa hivyo hakikisha kuwa una vifaa vya kutosha au VM ya saizi ya kutosha (kiwango cha chini cha cores 2 na RAM 2BG).



### B. hali ya TAP / SPAN



**bomba** ni **kifaa cha mtandao ambacho kinarudia trafiki inayopita ndani yake na kuituma kwa kifaa kingine.** Faida ya kifaa hiki ni kwamba haihitaji marekebisho yoyote ya miundombinu iliyopo, na inaweza kuwekwa popote ili kufuatilia sehemu mahususi za mtandao, au kati ya swichi ya msingi na kipanga njia ili kuchanganua trafiki kutoka/kutoka kwenye Mtandao.



Hasara kubwa ya aina hii ya vifaa ni gharama yake. Katika mitandao ya kisasa ya Gigabit, mguso wa hali ya chini hauwezi kunasa trafiki ya mtandao ipasavyo, kwa hivyo unahitaji kifaa kinachotumika cha gharama ya takriban €200 (kiwango cha chini).



Hali ya **SPAN**, inayojulikana pia kama **kuakisi mlango**, inatumiwa na swichi ili kusambaza trafiki kutoka mlango mmoja hadi mwingine. Hii ndiyo njia ninayopendelea zaidi, kwani ni rahisi kusanidi na, kama bomba, hukuruhusu kufuatilia sehemu ya mtandao au mtandao mzima upendavyo. Hata hivyo, kuna vikwazo viwili: kubadili lazima kuunganisha kazi hii, na matumizi yake yanaweza kuongeza mzigo wa processor kwenye kubadili.



### C. Njia ya router



Inawezekana kabisa kuweka kipanga njia chini ya Linux na kusakinisha ntopng juu yake. Upungufu pekee wa njia hii ni kwamba itarekebisha mtandao wako, ama anwani yake ya ndani, au anwani kati ya kipanga njia chako "halisi" na ile unayoongeza.



Kumbuka: kwa wasomaji wa makala [Unda kipanga njia cha Wifi ukitumia Raspberry Pi na RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) inawezekana kabisa kusakinisha ntopng kwenye Rpi yako ili kupata takwimu sahihi!



### D. Hali ya daraja



Njia mbadala ya kuvutia ni kutumia **mashine ya Linux katika hali ya daraja.** Imewekwa kati ya vipande viwili vya vifaa, hii inaruhusu trafiki yote kunaswa bila kulazimika kuingilia kati usanidi wa miundombinu au vifaa vyake. Kwa kuwa mashine ya zamani inaweza kufanya kazi hiyo, gharama ya njia hii pia inaweza kuvutia. Kumbuka kuwa ili kuwa bora, kifaa kinapaswa kuwa na kadi tatu za mtandao, mbili katika hali ya daraja, moja kufikia Interface na SSH. Inawezekana kutumia kadi mbili tu, lakini basi trafiki ya usimamizi wa kifaa pia itanaswa...



Kwa hivyo ni ** hali hii ya mwisho ambayo nitatumia **. Kwa sababu za vitendo, nitakuwa nikitumia mashine za kawaida kwa maandamano, lakini njia inabaki kuwa sawa kwa matumizi ya mashine za kimwili.



## III. Maandalizi ya uchunguzi na daraja la Interface



Kwa uchunguzi, ninachagua mashine ya **Debian 11** katika usakinishaji mdogo.



Hatua ya kwanza, sawa kila wakati, sasisha:



```
apt-get update && apt-get upgrade
```



Kisha sakinisha kifurushi cha **bridge-utils**, ambacho kitaturuhusu kuunda daraja letu:



```
apt-get install bridge-utils
```



Mara tu ikiwa imewekwa, jambo la kwanza kukumbuka ni jina la sasa la kadi zetu za mtandao. Chini ya Debian, jina hili linaweza kuchukua aina kadhaa, na tutalihitaji kwa usanidi.



Amri rahisi ya **ip add** itarudisha pato na habari hii:



![Image](assets/fr/016.webp)



Hapa, naona miingiliano 3:





- Lo**: hii ni kitanzi Interface; ni Interface ya kawaida ambayo "huzunguka" juu ya vifaa. Kimsingi, Interface hii, ambayo Address ni 127.0.0.1 (ingawa Address yoyote katika 127.0.0.0/8 itafanya, kwani masafa haya yamehifadhiwa kwa madhumuni haya) hutumiwa kuwasiliana na kifaa yenyewe. Ikiwa umesakinisha tovuti kwenye kituo chako cha kazi (kwa kutumia WAMPP, kwa mfano), pengine umetumia "*localhost*" Address kwa wakati mmoja au nyingine kuonyesha tovuti iliyopangishwa kwenye mashine yako mwenyewe. Jina hili la mpangishaji linahusishwa na Address 127.0.0.1 na kwa hivyo na kitanzi cha Interface.
- en33**: hii ni Interface yangu ya kwanza, ambayo ilipata Address hapa kutoka kwa DHCP yangu
- en36**: Interface yangu ya pili



Sasa kwa kuwa nina habari yote, ninaweza kurekebisha */etc/network/interfaces* faili ili kuunda daraja langu. Hivi ndivyo inavyoonekana kwa sasa (inaweza kutofautiana):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



Sehemu ya kwanza inahusu kitanzi changu cha Interface, ambacho sitakigusa, ikifuatiwa na Interface en33. Marekebisho yanajumuisha kuongeza Interface yangu ya pili (ens36) na kusanidi daraja na miingiliano hii miwili:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Hapa kuna baadhi ya maelezo ya mabadiliko haya ya kwanza:





- kiotomatiki *Interface***: "itaanzisha" kiotomatiki Interface wakati wa kuwasha mfumo
- iface *Interface* mwongozo wa inet**: kutumia Interface bila IP Address yoyote. Kama neno kuu "tuli" kufafanua IP tuli Address au "dhcp" kutumia kushughulikia kwa nguvu.



Marekebisho yanaendelea:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Hapa tena, maelezo machache:





- iface br0 inet tuli**: hapa nimefafanua daraja langu la Interface (*br0*) na Address tuli.
- Address, barakoa, lango**: maelezo ya anwani ya ubao
- bridge_ports**: miingiliano ya kujumuishwa kwenye daraja
- bridge_stp**: itifaki ya Spanning Tree hutumiwa wakati wa kuunganisha swichi ili kutambua viungo visivyohitajika na kuepuka vitanzi. Kwa kuwa daraja linaweza kuingizwa kati ya njia mbili za mtandao, inaweza kuwa chanzo cha kitanzi, hivyo uwezekano wa kuwezesha itifaki hii. Siitaji hapa, kwa hivyo ninaizima.



Hifadhi mabadiliko na uanze tena mtandao:



```
systemctl restart networking
```



Ili kuangalia mabadiliko, onyesha matokeo ya **ip** ongeza amri tena:



![Image](assets/fr/021.webp)


Unaweza kuona kwa uwazi **Interface yangu mpya "*br0*" na IP Address ambayo nimeikabidhi.** Kwa bahati mbaya, unaweza pia kuona kwamba violesura vyangu viwili vya kimwili ni "JUU", lakini hazina IP Address.



## IV. Inasakinisha NtopNG



Sasa kwa kuwa uchunguzi wetu unaweza kunusa trafiki kati ya mtandao wangu na kipanga njia, kilichobaki kufanya ni kusakinisha ntopng. Ili kufanya hivyo, kwanza rekebisha faili ya */etc/apt/sources.list* na uongeze **changia** mwishoni mwa kila mstari ukianza na **deb** au **deb-src**.



Kwa chaguo-msingi, vyanzo vya kifurushi vina vifurushi vinavyotii DFSG (*Miongozo ya Programu Isiyolipishwa ya Debian*) pekee, vinavyotambuliwa na neno kuu ****. Unaweza pia kuongeza vyanzo hivi:





- mchango**: vifurushi vilivyo na programu inayotii DFSG, lakini kwa kutumia vitegemezi ambavyo si sehemu ya **tawi kuu**
- isiyolipishwa**: ina vifurushi ambavyo haviambatani na DFSG



Mfano wa mstari katika /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Kwa hivyo nitaongeza tu neno **changia** kwenye mistari kama hii.



Hatua zingine zimeorodheshwa kwenye tovuti ya [NtopNG] (https://packages.ntop.org/apt/) ambapo, kwa Debian 11, unahitaji kuongeza vyanzo vya Ntop kwa usakinishaji wa siku zijazo. Nyongeza hii inajiendesha kwa kutumia:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Kisha inakuja awamu halisi ya ufungaji:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Amri ya kwanza inafuta kashe ya meneja wa kifurushi cha apt. Ya pili itasasisha orodha ya kifurushi na ya tatu itasakinisha NtopNG.



Baada ya usakinishaji, **programu ya NtopNG inapatikana moja kwa moja kwenye bandari 3000 ya mashine ya Debian**. Kwa hivyo kwangu ni `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



Ukurasa wa nyumbani wa NtopNG



Kuingia kwa chaguo-msingi na nenosiri huonyeshwa, kwa hivyo unachotakiwa kufanya ni kuziingiza!



## V. Kwa kutumia NtopNG



Unapoingia kwa mara ya kwanza, jambo la kwanza utaombwa kufanya ni kubadilisha nenosiri na lugha ya msimamizi chaguomsingi. Kwa bahati mbaya, Kifaransa sio mmoja wao.



Kisha unafika kwenye dashibodi:



![Image](assets/fr/023.webp)



Dashibodi ya NtopNG



Usimzoee huyu! Ukiona kisanduku cha njano kilicho juu ya skrini, utaona sentensi: "*Leseni itaisha muda wa 04:57*". Kwa chaguo-msingi, usakinishaji huzindua jaribio la toleo kamili la NtopNG, lakini kwa muda mfupi (sana). Pindi tu "hesabu iliyosalia" hii imefikiwa, toleo la *jamii* huwashwa na dashibodi hubadilika:



![Image](assets/fr/024.webp)



Dashibodi mpya ya jumuiya ya NtopNG



Jambo la kwanza la kufanya ni **angalia ikiwa Interface sahihi inasikiza**. Katika kona ya juu upande wa kushoto, orodha kunjuzi ya violesura vinavyopatikana hukuwezesha kuchagua Interface tunayopenda hapa: br0



![Image](assets/fr/025.webp)



Interface uteuzi



Dirisha jipya linaonyesha "Top Flaw Talkers", yaani vifaa vinavyowasiliana zaidi. Hapa nina vituo viwili tu vinavyoonekana:



![Image](assets/fr/026.webp)



**Wapangishi wa vyanzo huonekana upande wa kushoto, marudio upande wa kulia ** Hii hukuruhusu kuibua matumizi ya jumla ya kipimo data kwa kila seva pangishi, na kupata mtazamo wa jumla wa trafiki ya mtandao. Sio mbaya, lakini tunaweza kwenda mbali zaidi ...



Nikibofya "*Wapangishi*", kwa mfano, ninapata grafu inayoonyesha utumaji na upokeaji wa matumizi ya nguvu ya kila seva pangishi kwenye mtandao wangu. Hapa, kwa mfano, naweza kuona kwamba 192.168.1.37 pekee inachangia 80% ya trafiki yangu:



![Image](assets/fr/027.webp)



Nikibofya IP Address ya mwenyeji anayehusika, nitaelekezwa kwenye ukurasa wa muhtasari:



![Image](assets/fr/028.webp)



Ninaweza kuona, kwa mfano, kwamba ni mashine ya VMWare (kwa kutambua NDIYO ya MAC Address yangu), ambayo inaitwa DESKTOP-GHEBGV1 (kwa hakika ni mwenyeji wa Windows) NA nina **takwimu kwenye pakiti zilizopokelewa na kutumwa, pamoja na kiasi cha data**.



Pia utagundua menyu mpya juu ya muhtasari huu. Ninapendekeza ubofye "**Programu**" ili kuona ni nini kinachoendesha msongamano mkubwa wa magari:



![Image](assets/fr/017.webp)


Lo, inaonekana kama tumepata jibu! Kwenye grafu iliyo upande wa kushoto, **tunaona kwamba 76.6% ya trafiki yake inatoka ... Sasisho la Windows**, kwa hivyo seva pangishi inapakua masasisho!



NtopNG hutumia teknolojia inayoitwa DPI kwa *Ukaguzi wa Kifurushi cha Kina*, kuiwezesha kuainisha kila mtiririko wa mtandao na kufafanua programu (au familia ya programu) nyuma yake.



Ili kuonyesha, ninazindua video ya YouTube kwenye mwenyeji wangu:



![Image](assets/fr/018.webp)



**Trafiki ilitambuliwa mara moja na kuainishwa!



Kumbuka: kwa sababu za wazi, aina hii ya programu inaweza kuibua masuala ya faragha, kwa hivyo kuwa mwangalifu kuitumia chini ya hali zinazofaa. Kumbuka pia kwamba inawezekana **kuficha matokeo**, chaguo linaweza kupatikana katika **Mipangilio > Mapendeleo > Misc** na inaitwa "**Mask Host IP Address**".



## VI. Utambuzi na arifa



NtopNG pia ina uwezo wa kutoa arifa za usalama kwenye milisho fulani. Hizi zinaweza kupatikana katika menyu ya **Tahadhari**, kwenye bango la upande wa kushoto. Hapa, kwa mfano, nina jumla ya arifa 2851, zilizogawanywa katika ukali tofauti: Notisi, Onyo na Hitilafu.



![Image](assets/fr/019.webp)



Wacha tuangalie arifa za hali ya juu, ninazo 17 kati yao!



Kubofya kwenye takwimu hii huleta maelezo ya arifa. Hakuna jambo la kutisha hapa, ni maoni chanya ya uwongo, upakuaji wa masasisho yanaainishwa kama uhamishaji wa faili jozi katika mkondo wa HTTP, ambao unaweza kumaanisha shambulio.



![Image](assets/fr/020.webp)



Walakini, ninapotumia toleo lisilolipishwa, siwezi kutenga vikoa au seva pangishi ambazo ndio chanzo cha arifa, kwa hivyo itabidi uziangalie ili kuepuka kukosa kitu kinachotia wasiwasi zaidi. NtopNG itatoa arifa za generate katika tukio la:





- Upakuaji wa faili jozi kupitia HTTP
- Trafiki ya DNS ya kutiliwa shaka
- Kutumia bandari isiyo ya kawaida
- Utambuzi wa sindano ya SQL
- Uandikaji wa Tovuti Mtambuka (XSS)
- Nk.



## VII. Hitimisho



Katika somo hili, tumeona **jinsi ya kusanidi uchunguzi kwa kutumia NtopNG** inayotuwezesha **kuchanganua trafiki ya mtandao wetu** ili kuibua matumizi ya itifaki na umiliki wa kila seva pangishi, lakini pia kugundua trafiki ya kutiliwa shaka.



Kwa bahati mbaya, siwezi kufunika vipengele na uwezekano wote katika makala hii, lakini jisikie huru kuchunguza!



Suluhisho hili linaweza kutekelezwa kwa msingi wa kudumu ndani ya miundombinu ya biashara. NtopNG pia inaweza kuhamisha matokeo kwenye hifadhidata ya InfluxDB, kukuwezesha kuunda dashibodi zako ukitumia zana ya wahusika wengine kama vile Graphana.