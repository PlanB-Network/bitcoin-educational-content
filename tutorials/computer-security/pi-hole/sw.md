---
name: Pi-Hole
description: Kizuia tangazo cha mtandao wako wote
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Florian Duchemin yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Huenda mabadiliko yamefanywa kwa maandishi asilia.*



___



## I. Uwasilishaji



Sote tumeifanya mara tu tulipoanzisha kivinjari tunachopenda: sakinisha **blocker** (kizuia tangazo). Hata hivyo, unapotumia kivinjari cha TV au kifaa cha Android, n.k... Ni jambo gumu zaidi kupata kitu kinachofanya kazi. Na ikiwa kuna kifaa zaidi ya moja ndani ya nyumba, vizuri, unapaswa kurudia operesheni kwa kila kivinjari!



Katika somo hili, tutatatua tatizo rahisi**: toa kizuia tangazo kwa mashine zote kwenye mtandao wetu na uidhibiti katikati.**



Ili kufanya hivyo, tutatumia zana iliyotengenezwa kwa kusudi hili: **Pi-Hole**



Pi-Hole ni shimo la kuzama la DNS. Itatumia maombi ya DNS yaliyotolewa na vifaa vyako ili kuthibitisha au kukataa trafiki, hivyo kukulinda dhidi ya anwani na vikoa vinavyojulikana kuwa vinasambaza utangazaji, programu hasidi na kadhalika.



DNS inasimama kwa Mfumo wa Jina la Kikoa. Kwa hivyo jina la kikoa ni nini? Naam, "it-connect.fr" ni mfano mmoja tu. Jina la kikoa ni kitambulisho cha kipekee cha nyenzo moja au zaidi, kwa kawaida husimamiwa na huluki moja.



Jina la mashine pamoja na jina la kikoa linaitwa FQDN kwa *Jina la Kikoa Lililohitimu Kamili*. Inakuruhusu kufikia mashine maalum kwa "kuiita" tu. Kwa mfano, unapoandika "www.trucmachin.com", unaita mashine "www", ambayo ni ya kikoa "trucmachin.com".



Isipokuwa kwamba kompyuta zetu hazielewi lugha ya kibinadamu, wanachoelewa ni mfumo wa mfumo wa binary, kwa hivyo wanahitaji IP Address, ambayo ni sawa na nambari ya simu, ili kufikia tovuti.



Kwa hivyo kila wakati unapoingiza jina la tovuti kwenye kivinjari chako, au kubofya kiungo, kompyuta yako kwanza huuliza seva ya DNS kwa IP Address inayolingana na jina hilo.



**Pi-Hole kisha itakagua maombi haya (kuna mamia yao kila siku!) na kuzuia kiotomatiki yale yanayojulikana kupangisha matangazo au hata faili hasidi.



## II. Inaweka Pi-Hole



Kwa jina kama Pi-Hole, unaweza kudhania kwamba unahitaji Raspberry-Pi... Lakini hiyo si kweli kabisa. **Pi-Hole inaweza kusakinishwa kwenye kompyuta yoyote ya Linux (Debian, Fedora, Rocky, Ubuntu, n.k.)



Kwa upande mwingine, unahitaji kuzingatia kwamba **kifaa hiki kitalazimika kutumia masaa 24 kwa siku kwa sababu rahisi: hakuna DNS, hakuna mtandao!** Raspberry kwa hiyo ni wazo nzuri, kwani hutumia karibu hakuna nishati.



Ili kusakinisha, unganisha kwa mashine yako ya Linux kupitia SSH na uweke amri ifuatayo kama "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Kumbuka**: katika hali ya kawaida, haipendekezi "kudukua" hati bila kwanza kujua inachofanya. Ikiwa huna uhakika, nenda kwenye ukurasa na kivinjari au upakue maudhui kama faili.
>


> **Kumbuka: kwenye matoleo madogo ya Debian 11, Curl haijasakinishwa, kwa hivyo unahitaji kuisakinisha wewe mwenyewe na **apt-get install curl** amri kabla ya kuandika amri iliyo hapo juu.

Mara tu hati itakapoendeshwa, safu ya majaribio itafanywa, na usakinishaji wenyewe utajishughulikia yenyewe:



![Image](assets/fr/019.webp)



Inaweka Pi-Hole



Baada ya usakinishaji kukamilika, utapelekwa kwenye skrini hii:



![Image](assets/fr/020.webp)



Skrini ya kuanza ya Pi-Hole



> **Kumbuka**: ikiwa unatumia DHCP kwenye mashine yako, utapata ujumbe wa onyo kuhusu hili. Bila shaka, kwa matumizi sahihi, tunapendekeza sana kwamba ugawanye IP fasta kwa mashine yako.

Kufuatia skrini hii, utapata ujumbe machache wa habari, na kisha utachukuliwa kwa mchawi wa usanidi, ambao utakuuliza kwanza ni seva gani ya DNS Pi-Hole itakayosambaza maombi. Kwa upande wangu, nimechagua Quad9, ambayo ina hati ya faragha ya mtumiaji.



![Image](assets/fr/021.webp)



Uchaguzi wa DNS - Pi-Hole



> **Kumbuka: ikiwa uko katika kampuni, kuna uwezekano kuwa seva yako ya sasa ya DNS ndiyo kidhibiti cha kikoa cha Saraka Inayotumika. Lakini usijali, unaweza baadaye kutaja kielekeza upya chenye masharti kwa kikoa unachochagua. Kwa kawaida, utaweza kuelekeza upya ombi lolote kuhusu kikoa chako cha ndani kwa seva yako ya DNS.

Utagundua kuwa baadhi ya chaguo ni pamoja na chaguo la DNSSEC. Kimsingi, itifaki ya DNS si salama (haikuundwa kwa kuzingatia hili wakati huo). DNSSEC hutatua tatizo hili kwa kuongeza Layer ya usalama kupitia usimbaji fiche na kutia saini kwa ubadilishanaji, kama ilivyoelezwa katika makala sambamba: [DNS Security](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Kizuizi chochote cha matangazo kinategemea orodha moja au zaidi kufanya kazi yake. Pi-Hole inakuja na orodha moja kama kawaida, kwa hivyo iteue na uiongeze zaidi baadaye.



![Image](assets/fr/022.webp)



Njoo swali kuhusu wavuti ya Interface, usakinishaji wake ni wa hiari, kwani chombo kina safu yake ya amri ya usimamizi na taswira. Lakini Interface hii ni ya kupendeza na imefanywa vizuri, kwa hivyo ninapendekeza usakinishe kwa wakati mmoja:



![Image](assets/fr/023.webp)



Ikiwa unasakinisha Pi-Hole kwenye mashine ambayo tayari ina seva ya Wavuti, unaweza kujibu "hapana" kwa swali lifuatalo. Tafadhali kumbuka, hata hivyo, kwamba PHP na moduli kadhaa zinahitajika kwa hili kufanya kazi. Vinginevyo, **lighttpd itasakinishwa na moduli zote muhimu **.



![Image](assets/fr/024.webp)



Kisha unaulizwa ikiwa ungependa kurekodi maombi ya DNS. **Ikiwa ungependa kuhifadhi historia, weka hii kuwa ndiyo; vinginevyo, weka hili kuwa hapana, lakini utapoteza baadhi ya utendakazi** (tazama skrini inayofuata).



![Image](assets/fr/025.webp)



Kwa wavuti yake ya Interface, Pi-Hole hutumia utendaji wa aina yake yenyewe iitwayo FTLDNS, ambayo hutoa API na kutoa takwimu kutoka kwa maombi ya DNS. Chaguo hili la kukokotoa linaweza kujumuisha hali ya "faragha" ambayo hufunika vikoa vilivyoombwa, wateja walio nyuma ya ombi, au zote mbili. Inafaa ikiwa unataka kufanya ufuatiliaji bila kukiuka faragha ya watu, au ikiwa tu unataka kuzingatia kanuni zinazofaa katika kesi ya matumizi kwenye mtandao wa umma.



![Image](assets/fr/026.webp)



Uchaguzi wa maisha ya kibinafsi



Mara tu swali hili la mwisho litakapojibiwa, hati itafanya kile kinachostahili: kupakua hazina za GitHub na kusanidi Pi-Hole. Mwishoni mwa usakinishaji, skrini ya muhtasari itaonyeshwa na maelezo muhimu:



![Image](assets/fr/027.webp)



Skrini ya muhtasari wa usakinishaji



Andika neno la siri la wavuti la Interface na maelezo ya mtandao. Sasa ni wakati wa kusanidi huduma ya DHCP katika eneo letu la sasa.



## III. Mpangilio wa DHCP



Ili kufanya kazi, Pi-Hole inahitaji "kusuluhisha" maombi ya DNS kutoka kwa wateja, kwa hivyo lazima wajue kuwa ndiyo ya kuwatumia. Kuna njia kadhaa za kufanya hivi:





- Rekebisha mipangilio ya DNS katika seva yako ya DHCP (k.m. Sanduku lako)
- Zima seva hii na utumie ile iliyotolewa na Pi-Hole
- Rekebisha kila kifaa wewe mwenyewe ili kutumia Pi-Hole kama DNS



Mimi binafsi huchagua suluhisho la kwanza. Uwezekano ni **una seva ya DHCP ulipo** (kawaida kisanduku chako). Kwa hivyo hakuna haja ya kujisumbua.



Kwa kuwa kuna idadi kubwa ya uwezekano, kati ya masanduku ya waendeshaji tofauti (ambayo sijui kuhusu wote) na wale ambao wana router yao wenyewe, sitatoa picha ya skrini kwa marekebisho haya. Kwa vyovyote vile, utahitaji kwenda kwenye mipangilio ya DHCP na urekebishe kigezo cha "DNS" ili kujumuisha IP Address ya Pi-Hole yako.



Mara hii imefanywa, ikiwa vifaa vyovyote vimewashwa hapo awali, vitakuwa vimehifadhi mipangilio ya zamani, kwa hivyo utahitaji kuanzisha upya ombi la usanidi.



Kwenye vituo vya kazi vya Windows, na haraka ya amri:



```
ipconfig /renew
```



Kwenye kituo cha kazi cha Linux:



```
dhclient
```



Kwa vifaa vingine vyote, lazima zizimwe na kuwashwa tena.



Kwa hivyo wanapaswa kupata vigezo sahihi, kuangalia:



```
ipconfig /all
```



Katika sehemu ya DNS, unapaswa kuwa na Address ya Pi-Hole yako, kwa upande wangu 192.168.1.42 :



![Image](assets/fr/029.webp)



## IV. Kwa kutumia mtandao wa Interface wa Pi-Hole



Ili kuwezesha usimamizi, **Pi-Hole** inanufaika kutoka kwa wavuti iliyoundwa vizuri ya Interface Interface. Inafaa kwa mtumiaji na inapatikana, hukuruhusu:





- Tazama idadi ya maombi, maombi yaliyozuiwa, n.k. kwa wakati halisi.
- Dhibiti Orodha yako iliyoidhinishwa na Orodha iliyoidhinishwa
- Ongeza maingizo tuli, lakabu, n.k.
- Ongeza orodha
- Na kazi nyingine nyingi!



Kwa upande wangu, nitaongeza orodha ya kuzuia. Kama ilivyoelezwa hapo juu, orodha moja tu iliwekwa kwa wakati mmoja na Soft. Kuna orodha nyingi za tovuti za matangazo, lakini ni bora kuchagua angalau moja mahususi kwa nchi unayoishi. Mojawapo ya orodha zinazojulikana zaidi ni **EasyList**, na mojawapo ni mahususi kwa Ufaransa: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Ili kuiongeza, kwanza unganisha kwa msimamizi wa Interface: **http://<ip_du_PiHole>/admin**



Nenosiri la msimamizi tayari limetolewa (angalia picha ya skrini ya mwisho wa usakinishaji), kwa hivyo unachohitaji kufanya ni kuliingiza ili kufikia Interface :



![Image](assets/fr/030.webp)



Interface kutoka Pi-Hole



Tunaweza kuona, kwa mfano, kwamba kuna wateja wawili waliounganishwa kwenye Pi-Hole, kwamba imeshughulikia maombi 442 na kwamba 8 kati ya haya yamezuiwa. Grafu hizi zinaweza kuwa chanzo kizuri cha habari, haswa katika muktadha wa kitaaluma.



Ili kuongeza orodha yetu, nenda kwenye menyu za "**Usimamizi wa Kikundi**" na "**Orodha za Matangazo**":



![Image](assets/fr/031.webp)



Tunaweza kuona orodha yetu ya kwanza "**StevenBlack**", ili kuongeza yetu, nakili kiungo nilichokupa hapo juu na uiingiza kwenye uwanja "**Address**", kwa maelezo, ninachagua kuweka jina la orodha:



![Image](assets/fr/032.webp)



Kuongeza orodha katika Pi-Hole



Kilichobaki ni kubofya "**Ongeza**" ili kuiongeza. Ili kuiwasha, tunahitaji kufanya hatua ya ziada ya "kuonya" Pi-Hole kuchukua orodha hii. Ili kufanya hivi:





- Ama tumia laini ya amri iliyojengwa ndani
- Ama mtandao wa Interface



Binafsi nilichagua ya pili, kwa sababu ikiwa umeangalia kwa uangalifu, kiunga cha hati ya PHP ambayo hufanya sasisho iko moja kwa moja kwenye ukurasa ambao tuko (neno "mtandaoni"). Kwa hivyo unachotakiwa kufanya ni kubofya juu yake, ambayo itakupeleka kwenye ukurasa na chaguo moja tu:



![Image](assets/fr/033.webp)



Ukurasa utaonyesha matokeo ya hati mara moja kukamilika, ikimaanisha kuwa orodha imezingatiwa (isipokuwa ujumbe wa makosa utaonyeshwa, bila shaka).



Kama ilivyotangazwa mwanzoni mwa mafunzo haya, Pi-Hole pia hukuruhusu **kuzuia vikoa vinavyojulikana kusambaza programu hasidi. Ili kuimarisha kipengele hiki, ninapendekeza pia uongeze orodha ya kikoa iliyosasishwa mara kwa mara inayosambazwa na Abuse.ch**, ambayo itaimarisha kwa kiasi kikubwa usalama wa mtandao wako, unaopatikana katika [hii Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Unaweza, bila shaka, kuongeza orodha zozote unazofikiri zinafaa, au kudhibiti orodha yako iliyoidhinishwa mwenyewe kupitia menyu ya orodha iliyoidhinishwa.



## Vipimo vya V. Pi-Hole



Sasa kwa kuwa kila kitu kiko sawa, unachotakiwa kufanya ni kujaribu suluhisho ili kuhakikisha kuwa linafanya kazi vizuri.



Kwa mfano, nitajaribu kufikia kikoa *http://admin.gentbcn.org/* ambacho kiko kwenye orodha ya Abuse.ch kwa sababu kinajulikana kupangisha programu hasidi:



![Image](assets/fr/034.webp)



Ni wazi, nimezuiwa mahali fulani. Ili kuhakikisha kuwa ni Pi-Hole ambayo imefanya kazi hiyo, tunaweza kuangalia kumbukumbu ya hoja kwenye wavuti ya Interface "Logi ya Maswali" ili kuona kuwa ni kizuizi kutoka kwa ingizo la orodha:



![Image](assets/fr/035.webp)



## VI. Hitimisho



Katika somo hili, tumekuonyesha jinsi ya kusanidi seva ya DNS ambayo sio tu inaondoa matangazo mengi kwa faraja yako ya kuvinjari, lakini pia huongeza **Layer ya usalama kwa kuzuia hadaa na vikoa vinavyoeneza programu hasidi**.



Yote bila malipo na ya kiuchumi ikiwa imewekwa kwenye Raspberry-Pi (kwa suala la matumizi ya nguvu).