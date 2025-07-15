---
name: pfSense
description: Inaweka Pfsense
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Florian BURNEL yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Mabadiliko makubwa yamefanywa kwa maandishi asilia ya mwandishi ili kusasisha mafunzo.*



___



![Image](assets/fr/027.webp)



## I. Uwasilishaji



pfSense ni mfumo wa uendeshaji wa chanzo huria usiolipishwa ambao hubadilisha kompyuta yoyote, seva iliyojitolea au kifaa cha maunzi kuwa kipanga njia cha utendakazi wa juu, kinachoweza kusanidiwa sana na ngome. Kulingana na FreeBSD na maarufu kwa usanifu wake thabiti na thabiti wa mtandao, pfSense imekuwa ikiweka kiwango cha ngome huria za biashara, serikali za mitaa na watumiaji wa nyumbani wanaodai kwa zaidi ya miaka kumi na tano.



Kazi zake kuu zimebadilika sana kwa miaka mingi, na zimeimarishwa kwa kila toleo jipya. Hadi sasa, pfSense inatoa:





- Utawala kamili na wa kati kupitia mtandao wa kisasa, angavu na salama wa Interface wa Interface.
- Ngome yenye utendakazi wa hali ya juu yenye usaidizi wa hali ya juu wa NAT (ikiwa ni pamoja na NAT-T) na udhibiti wa sheria punjepunje.
- Usaidizi asilia wa WAN nyingi, kuwezesha ujumlishaji au kutohitajika tena kwa miunganisho ya Mtandao.
- Seva ya DHCP iliyounganishwa na relay.
- Upatikanaji wa juu shukrani kwa itifaki ya CARP kwa kushindwa na uwezekano wa kusanidi makundi ya pfSense.
- Kusawazisha mzigo kati ya miunganisho kadhaa au seva.
- Usaidizi kamili wa VPN: IPsec, OpenVPN na WireGuard (inabadilisha L2TP, sasa imepitwa na wakati).
- Lango la ndani linaloweza kusanidiwa kwa udhibiti wa ufikiaji wa wageni, haswa katika mazingira ya umma au hoteli.



pfSense pia ina mfumo wa kifurushi unaoweza kupanuliwa ambao hurahisisha kuongeza vipengele vya kina kama vile proksi ya uwazi (Squid), uchujaji wa URL au IDS/IPS (Snort au Suricata) moja kwa moja kutoka kwa wavuti ya Interface.



pfSense inasambazwa kwa majukwaa ya 64-bit pekee, kulingana na mapendekezo ya sasa ya FreeBSD. Inaweza kusakinishwa kwenye maunzi ya kawaida (Kompyuta, seva za rack) au kwenye majukwaa yaliyopachikwa yenye nguvu ya chini kama vile vifaa vya Netgate au visanduku fulani vya hali ya chini x86, ambavyo vina nguvu zaidi kuliko visanduku vya zamani vya Alix.



Mwishowe, inafaa kukumbuka kuwa pfSense inahitaji angalau miingiliano miwili ya mtandao halisi: moja iliyowekwa kwa ukanda wa nje (WAN) na moja iliyowekwa kwa mtandao wa ndani (LAN). Kulingana na utata wa miundombinu yako (DMZ, VLAN, WAN nyingi), miingiliano kadhaa ya ziada inaweza kuhitajika ili kutumia kikamilifu uwezo wake.



## II. Pakua picha



Toleo la hivi punde thabiti la pfSense, wakati wa kuandika mafunzo haya, ni 2.8 (lililotolewa Juni 2025). Unaweza kupakua picha ya ISO au faili ya usakinishaji iliyorekebishwa kwa mazingira ya maunzi yako moja kwa moja kutoka kwa tovuti rasmi :





- [Pakua pfSense](https://www.pfsense.org/download/)



Lango la upakuaji hukuruhusu kuchagua :





- Usanifu (kwa ujumla **AMD64 ** kwa vifaa vyote vya kisasa).
- Aina ya picha (**Sakinisha USB Memstick** kwa ajili ya kusakinisha kupitia USB stick, **ISO Installer** kwa kuchoma au uhariri pepe).
- Kioo cha upakuaji kilicho karibu zaidi, ili kuboresha kasi ya uhamishaji.



Kwa wale wanaotaka kupeleka pfSense katika mazingira ya kipeperushi (Proxmox, VMware ESXi, VirtualBox...), picha ya **OVA** inapatikana pia. Mashine hii pepe iliyo tayari kutumika hurahisisha usakinishaji na usanidi wa awali. Hakikisha tu umerekebisha rasilimali zilizotengwa (CPU, RAM, violesura vya mtandao) kulingana na mzigo unaotarajiwa na topolojia ya mtandao wako.



Kabla ya usakinishaji, tunapendekeza uangalie uadilifu wa faili iliyopakuliwa kwa kuthibitisha **SHA256** iliyotolewa kwenye ukurasa rasmi wa upakuaji. Hii inahakikisha kuwa picha haijabadilishwa au kuharibiwa.



## III. Ufungaji



Katika mfano huu, usakinishaji unafanywa kwenye mashine ya kawaida inayoendesha VirtualBox. Utaratibu unasalia kuwa sawa kwenye mashine halisi au hypervisor nyingine yoyote, isipokuwa kwa usimamizi wa kifaa pepe.



### 1. Mahitaji ya chini ya vifaa



Kwa usambazaji wa kawaida, tunapendekeza:





- 1 GB RAM** kiwango cha chini (GB 2 au zaidi inapendekezwa ili kuwezesha vifurushi vya ziada au usaidizi wa ZFS).
- Nafasi ya diski ya GB 8** (GB 20 au zaidi inapendekezwa kwa usanidi wa hali ya juu zaidi, haswa ikiwa unasakinisha akiba ya seva mbadala, IDS/IPS au kumbukumbu za kina).
- Angalau miingiliano miwili ya mtandao pepe** (moja ya WAN, moja ya LAN). Katika VirtualBox, waongeze kwenye mipangilio ya VM kabla ya kuanza.



### 2. Kuanzisha kisakinishi



Panda picha ya ISO iliyopakuliwa kama kiendeshi dhahania cha macho kwenye VirtualBox, au weka kitufe cha USB ikiwa unasakinisha kwenye mashine halisi. Wakati wa kuanza, menyu ya boot inaonekana:



Ikiwa hutachagua chaguo zozote, pfSense itaanza kiotomatiki na chaguo-msingi baada ya sekunde chache. Bonyeza kitufe cha "**Enter**" ili kuanzisha uanzishaji wa kawaida.



![Image](assets/fr/027.webp)



Wakati menyu kuu inaonekana, bonyeza haraka kitufe cha "**I**" ili kuanzisha usakinishaji.



![Image](assets/fr/001.webp)



### 3. Mipangilio ya kisakinishi cha awali



Skrini ya kwanza hukuruhusu kuweka vigezo vichache vya kikanda, kama vile fonti ya kuonyesha na usimbaji wa herufi. Mipangilio hii ni muhimu katika hali maalum (kibodi zisizo za kawaida, skrini za mfululizo, lugha za mashariki). Kwa usakinishaji mwingi, weka thamani chaguo-msingi na uchague "**Kubali Mipangilio hii**".



![Image](assets/fr/002.webp)



### 4. Uchaguzi wa mode ya ufungaji



Chagua "**Haraka/Rahisi Kusakinisha**" ili kuendesha usakinishaji wa kiotomatiki na chaguo zinazopendekezwa. Njia hii hufuta diski iliyochaguliwa na kusanidi pfSense na ugawaji chaguo-msingi.



![Image](assets/fr/003.webp)



Onyo linaonekana, linaonyesha kwamba data yote kwenye diski itafutwa. Thibitisha kwa "**Sawa**".



Kisha kisakinishi kinakili faili zinazohitajika kwenye diski. Kulingana na maunzi yako, hii inaweza kuchukua kutoka sekunde chache hadi dakika chache.



### 5. Uchaguzi wa msingi



Wakati kisakinishi kinakuhimiza kuchagua aina ya kernel, acha "**Standard Kernel**" iliyochaguliwa. Kerneli hii ya jumla inafaa kabisa kwa uwekaji wa kawaida, iwe kwenye Kompyuta, seva au VM.



### 6. Mwisho wa ufungaji na kuanzisha upya



Mara usakinishaji utakapokamilika, chagua "**Washa upya**" ili kuwasha upya mashine yako kwenye mfano wako mpya wa pfSense.



**Dokezo muhimu**: ondoa picha ya ISO au ukata ufunguo wa usakinishaji wa USB kabla ya kuwasha upya, ili kuepuka kuanzisha upya programu ya usakinishaji utakapowasha tena.



## IV. Kuanzisha pfSense kwa mara ya kwanza



Wakati wa kuanza kwa mara ya kwanza, pfSense lazima isanidiwe ili kutambua na kugawa kwa usahihi violesura vyake vya mtandao (WAN, LAN, DMZ, VLAN, n.k.). Utambulisho makini wa kadi zako za mtandao ni muhimu ili kuepuka hitilafu zozote za usanidi ambazo zinaweza kukunyima ufikiaji wa wavuti ya Interface au kufanya ngome yako isifanye kazi.



Inapozinduliwa, pfSense hutambua kiotomatiki na kuorodhesha violesura vyote vinavyopatikana vya mtandao, ikionyesha MAC Address kwa kila moja. Hii inafanya iwe rahisi kutofautisha kati yao.



### 1. VLAN



Swali la kwanza linahusu usanidi wa VLAN. Katika hatua hii, kwa usanidi wa kimsingi, hatutawasha VLAN zozote. Kwa hivyo bonyeza kitufe cha "**N**" ili kuruka hatua hii.



![Image](assets/fr/004.webp)



### 2. WAN na LAN Interface Assignment



pfSense kisha inakuhimiza kufafanua ni Interface gani itatumika kwa WAN (ufikiaji wa Mtandao). Unaweza kuchagua kati ya:





- Weka jina la Interface wewe mwenyewe (linapendekezwa kwa mazingira pepe).
- Tumia utambuzi wa kiotomatiki kwa kubonyeza "**A**". Chaguo hili ni muhimu kwa seva pangishi halisi, mradi nyaya za mtandao wako zimeunganishwa na viungo vinatumika.



![Image](assets/fr/005.webp)



Katika mfano huu, sisi husanidi kwa mikono WAN. Ingiza jina halisi la Interface. Kwa bodi ya Intel, jina mara nyingi litakuwa "**em0**" chini ya FreeBSD, lakini linaweza kutofautiana kulingana na maunzi. Kwa mfano, kadi ya Realtek mara nyingi itaonyeshwa kama "**re0**".



![Image](assets/fr/006.webp)



Rudia operesheni sawa ili kufafanua Interface LAN. Hapa, tunatumia "**em1**".



pfSense inathibitisha kuwa Interface LAN huwasha ngome na NAT ili kulinda mtandao wako wa ndani na kudhibiti tafsiri ya Address.



Ikiwa una miingiliano mingine ya kimwili, unaweza kusanidi miingiliano ya ziada (DMZ, Wi-Fi, VLAN maalum) katika hatua hii. Kila Interface yenye mantiki inahitaji kadi ya mtandao inayolingana au Interface ya mtandaoni. Kwa usanidi wa awali, tutajifungia kwa WAN na LAN.



Baada ya kazi kukamilika, pfSense huonyesha muhtasari wa wazi wa mawasiliano kati ya miingiliano ya kimwili na majukumu uliyopewa. Thibitisha kwa "**Y**".



### 3. PfSense console



Wakati hatua hii imekamilika, orodha kuu ya pfSense console inaonekana. Inatoa chaguzi kadhaa muhimu kwa usimamizi wa moja kwa moja, kama vile kuweka upya nenosiri la wavuti, kuwasha upya, kupakia upya usanidi au kugawa upya violesura.



![Image](assets/fr/007.webp)



Pia utaona muhtasari wa mipangilio ya sasa ya mtandao, ikijumuisha IP Address ya Interface LAN, kwa kawaida **192.168.1.1**. Hii ndiyo Address utahitaji kuingiza katika kivinjari chako ili kufikia mtandao wa utawala wa Interface.



**Kumbuka**: Ikiwa mtandao wako wa ndani unatumia masafa tofauti ya Address, chagua "**2)** Weka Interface(s) IP Address" kwenye menyu ili kukabidhi IP Address inayofaa mazingira yako.



Kwa chaguomsingi, ikiwa Interface WAN yako imeunganishwa kwenye kisanduku au modemu iliyosanidiwa na DHCP, pfSense itapata IP ya umma Address kiotomatiki. Kwa hivyo unapaswa kufaidika kutokana na ufikiaji wa mtandao mara moja kwa kuunganisha mteja kwenye pfSense Interface LAN.



## V. Ufikiaji wa kwanza kwa wavuti ya Interface



Mara tu uanzishaji wa awali utakapokamilika na violesura vya mtandao kusanidiwa, unaweza kufikia wavuti ya Interface ya pfSense ili kukamilisha na kurekebisha usanidi wako.



### 1. Muunganisho wa awali



Unganisha kompyuta kwenye lango la LAN (au LAN pepe ya Interface kwenye hypervisor yako) na uikabidhi IP Address katika masafa sawa ikihitajika (kwa chaguo-msingi, pfSense inasambaza kiotomatiki Address kupitia DHCP kwenye LAN).



Katika kivinjari chako, nenda kwa Address iliyoonyeshwa na kiweko (kwa chaguo-msingi `https://192.168.1.1`). Kumbuka kuwa pfSense inahitaji HTTPS hata kwa muunganisho wa kwanza - kwa hivyo tarajia onyo la cheti cha kujiandikisha, ambacho unaweza kupuuza kwa kuongeza ubaguzi.



Skrini ya kuingia inaonekana. Vitambulisho chaguo-msingi ni:




- Jina la mtumiaji:** `admin`
- Nenosiri:** `pfsense`



Vitambulisho hivi vitarekebishwa wakati wa mchawi wa usanidi wa awali.



## VI. Mchawi wa Kuanzisha



Kwenye muunganisho wa kwanza, pfSense inakuomba ufuate **Mchawi wake wa Kuweka**. Tunapendekeza sana uitumie ili kuhakikisha kuwa vigezo vyote muhimu vimefafanuliwa kwa usahihi.



### 1. Vigezo vya jumla



Unaweza:




- Bainisha jina la mwenyeji na kikoa cha ndani (mfano: `pfsense` na `lan.local`).
- Bainisha seva za DNS na uchague ikiwa pfSense inapaswa kutumia DNS ya ISP yako au huduma ya nje (Cloudflare, OpenDNS, Quad9...).



### 2. Eneo la wakati



Onyesha saa za eneo la tovuti yako ili kumbukumbu na ratiba zilingane (k.m. `Ulaya/Paris`).



### 3. Usanidi wa WAN



Sanidi muunganisho wa WAN :




- Chaguomsingi hadi **DHCP** (inatosha ikiwa uko nyuma ya kisanduku).
- Ikiwa una IP iliyowekwa, ingiza vigezo (IP tuli, mask, lango, DNS) kwa manually.
- Ikiwa ni lazima, fafanua uthibitishaji wa VLAN au PPPoE (kawaida na baadhi ya ISPs).



### 4. usanidi wa LAN



Mchawi unapendekeza kubadilisha subnet ya LAN chaguo-msingi. Ikiwa una mpango mahususi wa kushughulikia, sasa ndio wakati wa kuurekebisha.



### 5. Badilisha nenosiri la msimamizi



Linda pfSense yako kwa kuweka mara moja nenosiri dhabiti kwa mtumiaji `admin`.



## VII. Uthibitishaji na sasisho



Kabla ya kupeleka ngome yako, hakikisha una toleo jipya zaidi la:





- Nenda kwa **Mfumo > Sasisha **.
- Chagua kituo cha sasisho (kawaida **Imara**).
- Angalia masasisho na uyatumie.



Ni vyema kuwasha arifa za sasisho ili kukufahamisha kuhusu viraka vya usalama.



## VIII. Inahifadhi usanidi



Kabla ya kufanya mabadiliko yoyote makubwa, tekeleza sera ya kuhifadhi nakala:





- Nenda kwenye **Uchunguzi > Hifadhi Nakala na Rejesha**.
- Pakua nakala ya usanidi wa sasa (`config.xml`).
- Iweke mahali salama (midia iliyosimbwa kwa njia fiche).



Kwa mazingira muhimu ya dhamira, zingatia nakala rudufu ya usanidi otomatiki kwenye seva ya nje au kupitia hati iliyoratibiwa.



## IX. Mbinu bora baada ya ufungaji



Kumaliza utumaji wako kwa amani ya akili:





- Rekebisha sheria za ngome**: kwa chaguo-msingi, pfSense inaruhusu trafiki yote inayotoka kwenye LAN na kuzuia trafiki inayoingia kwenye WAN. Rekebisha sheria hizi kama inavyotakiwa.
- Sanidi ufikiaji salama wa mbali**: ikihitajika, wezesha ufikiaji wa mtandao wa Interface kutoka kwa WAN kupitia VPN pekee au kwa vizuizi vya IP.
- Washa arifa**: sanidi seva ya SMTP ili kupokea arifa (kushindwa, masasisho, hitilafu).
- Sakinisha viendelezi muhimu**: kwa mfano, IDS/IPS (Snort, Suricata), proksi (Squid), uchujaji wa DNS (pfBlockerNG).



Ngome yako ya ulinzi ya pfSense sasa iko na inafanya kazi, iko tayari kulinda mtandao wako. Shukrani kwa unyumbufu wake na jumuiya inayofanya kazi, una zana yenye nguvu, inayoweza kubadilika ambayo inaweza kukabiliana na mahitaji yako ya baadaye (WAN nyingi, VLAN, VPN ya tovuti hadi tovuti, lango la wafungwa, n.k.).



Angalia hati rasmi ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) mara kwa mara ili kugundua vipengele vipya na uhakikishe kuwa usanidi wako umesasishwa na ni salama.