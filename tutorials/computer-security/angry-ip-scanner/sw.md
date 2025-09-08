---
name: Kichunguzi cha IP chenye hasira
description: Njia rahisi ya kuchanganua mtandao wako
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Florian BURNEL yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Huenda mabadiliko yamefanywa kwa maandishi asilia.*



___



## I. Uwasilishaji



Je, unachanganuaje mtandao wa Windows kwa mashine zilizounganishwa haraka na kwa urahisi? Jibu ni Hasira IP Scanner. Mradi huu wa programu huria hukuwezesha kuchanganua mtandao kwa urahisi, kwa kutumia mchoro wa Interface ambao ni rahisi kutumia.



Zana hii inaweza kutumiwa na watu binafsi ili **kuchanganua mtandao wao wa karibu**, lakini pia na wataalamu wa TEHAMA kwa madhumuni sawa. Uthibitisho kwamba **zana hii ni ya vitendo sana**, tayari imetumiwa na **baadhi ya vikundi vya wahalifu wa mtandaoni** kuchanganua mitandao ya mashirika (kwa njia sawa na Nmap). Mfano mzuri ni [kundi la programu ya ukombozi RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Bado ni kipande cha programu cha sauti, lakini kama ilivyo kwa mtandao na zana zingine zinazozingatia usalama, matumizi yake yanaweza kutumiwa vibaya.



Hapa, tutaitumia kwenye **Windows 11**, lakini inawezekana kabisa kuitumia kwenye matoleo mengine ya **Windows**, na pia kwenye **Linux** na **macOS**.



Kina maelezo kidogo kuliko Nmap, **Kichanganuzi cha IP** chenye hasira bado kinavutia kwa uchanganuzi wa haraka na wa kimsingi wa mtandao, lakini pia kwa sababu kinaweza kufikiwa na kila mtu. **Itatambua seva pangishi zilizounganishwa kwenye mtandao** na kutambua **majina ya wapangishaji** na **njia zilizo wazi**.



Ikiwa unataka kwenda zaidi, angalia mafunzo kwenye Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Anza na Kichunguzi cha IP cha Hasira



### A. Pakua na usakinishe Angry IP Scanner



Unaweza kupakua toleo la hivi punde la Kichunguzi cha IP cha Hasira kutoka kwa tovuti rasmi ya programu au kutoka kwa GitHub. Tutatumia chaguo la mwisho. Bofya kwenye kiungo kilicho hapa chini na upakue toleo la EXE: "** ipscan-3.9.1-setup.exe**".





- [Kichunguzi cha IP chenye hasira GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Endesha inayoweza kutekelezwa ili kuendelea na usakinishaji. Hakuna kitu maalum cha kufanya wakati wa ufungaji.



![Image](assets/fr/013.webp)



### B. Tekeleza upekuzi wa awali wa mtandao



Katika uzinduzi wa kwanza, chukua muda kusoma maagizo katika dirisha la "**Anza**" ili upate maelezo zaidi kuhusu jinsi zana inavyofanya kazi. Kwa njia, kuna masharti kadhaa ya kuzingatia:





- Mlisho**: moduli inayohusika na kutoa orodha za anwani za IP zitakazochanganuliwa, kutoka kwa anuwai ya IP isiyo ya kawaida au faili iliyo na orodha ya anwani za IP.
- Fetcher**: seti ya moduli za kurejesha taarifa kuhusu wapangishaji kwenye mtandao. Kuna, kwa mfano, wachukuaji wa kugundua anwani za MAC, skanisho la bandari, kugundua majina ya seva pangishi au kutuma maombi ya HTTP.



![Image](assets/fr/018.webp)



Ili kuchanganua subnet ya IP, ingiza tu **anza IP Address** na **mwisho IP Address** katika sehemu ya "**IP**" (vinginevyo, badilisha aina iliyo upande wa kulia). Kisha bonyeza kitufe cha "** Anza **".



![Image](assets/fr/019.webp)



Sekunde chache baadaye, matokeo yataonekana kwenye programu ya Interface. **Kwa kila IP Address katika safu iliyochanganuliwa, utaona kama Kichunguzi cha IP cha Hasira kimegundua mwenyeji au la.** Muhtasari pia utaonekana kwenye skrini, ukionyesha idadi ya seva pangishi zinazotumika (katika kesi hii 6) na idadi ya seva pangishi zilizo na milango iliyo wazi.



![Image](assets/fr/020.webp)



Hapa, tunaweza kuona kuwepo kwa seva pangishi inayoitwa "**OPNsense.local.domain**", inayohusishwa na IP Address "**192.168.10.1**" na inaweza kufikiwa kwenye **bandari 80** na **443** (HTTP na HTTPS). Kubofya kulia kwenye seva pangishi kunatoa ufikiaji wa amri za ziada, kama vile pinging, kufuatilia njia na kufungua kivinjari kupitia IP hii Address.



![Image](assets/fr/012.webp)



### C. Ongeza milango ya kuchanganua



Kwa chaguomsingi, **Kichunguzi cha IP chenye hasira** kitachanganua milango 3: **80** (HTTP), **443** (HTTPS) na **8080**. Unaweza kuongeza milango zaidi ili kuchanganuliwa kutoka kwa mapendeleo ya programu. Bofya kwenye menyu ya "**Zana**", kisha kwenye kichupo cha "**Bandari**".



Hapa, unaweza kurekebisha orodha ya bandari kupitia chaguo la "**Uteuzi wa bandari **". Unaweza **kuonyesha nambari maalum za mlango zikitenganishwa na koma, au safu za mlango**. Mfano hapa chini unaongeza bandari mbili: **445** (SMB) na **389** (LDAP). Ili kuchanganua bandari kutoka 1 hadi 1000, ingiza "**1-1000**". Haijabainishwa ikiwa ukaguzi wa mlango unafanywa katika TCP, UDP au zote mbili.



![Image](assets/fr/021.webp)



Ukichanganua tena, kuna uwezekano wa kupata taarifa mpya. Katika mfano ulio hapa chini, Angry IP Scanner inaniambia kuwa bandari 389 na 445 zimefunguliwa kwenye seva pangishi "**SRV-ADDS-01**" na "**SRV-ADDS-02**", kutokana na usanidi mpya wa bandari za kuchanganuliwa.



![Image](assets/fr/022.webp)



**Kumbuka**: kutoka kwa menyu ya "** Kichanganuzi**", unaweza kuhamisha matokeo ya kuchanganua kwenye faili ya maandishi.



Iwapo ungependa kuendeleza uchanganuzi zaidi, bofya kwenye menyu ya "**Zana**", kisha ubofye "**Vichochezi**". Hii inaongeza "uwezo" kwenye tambazo. Chagua tu kichota na uisogeze upande wa kushoto ili kuiwasha. Hii itaongeza safu wima ya ziada kwenye matokeo ya tambazo.



![Image](assets/fr/014.webp)



Mfano ulio hapa chini unaonyesha "**Maelezo ya NetBIOS**" na "**Ugunduzi wa Mtandao**". Ya kwanza hutoa maelezo ya ziada kama vile MAC Address ya mashine na jina la kikoa, huku ya pili ikionyesha kichwa cha ukurasa wa wavuti (ambacho kinaweza kutoa ishara fulani ya aina ya seva ya wavuti au programu).



![Image](assets/fr/011.webp)



Hatimaye, kutoka kwa mapendeleo, unaweza pia kubadilisha njia inayotumiwa kwa "**ping**", yaani kuzingatia ikiwa mwenyeji anafanya kazi au la. Kwa kuwa wapangishi wengine hawajibu pings, hii hukuruhusu kujaribu njia zingine (pakiti ya UDP, uchunguzi wa bandari ya TCP, ARP, UDP + TCP mchanganyiko, nk).



## III. Hitimisho



Rahisi na bora: Kichanganuzi cha IP cha Hasira hutambua seva pangishi zilizounganishwa kwenye mtandao, na hukuruhusu kusanidi uchunguzi wa mlango. Kwa upande wa chaguzi, hainyumbuliki kama Nmap, na haiendi mbali, lakini ni mwanzo mzuri wa kuchanganua haraka.



Ikiwa ungependa kutumia **Nmap** na Interface ya mchoro, unaweza kutumia **programu ya Zenmap** (tazama muhtasari hapa chini).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d