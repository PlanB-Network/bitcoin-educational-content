---
name: Nmap
description: Master Nmap ya ramani ya mtandao na uchanganuzi wa uwezekano wa kuathirika
---

![cover](assets/cover.webp)



*Mafunzo haya yanatokana na maudhui asili ya Mickael Dorigny yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Mabadiliko yamefanywa kwa maandishi asilia.*



___



Karibu kwenye mafunzo haya ya utangulizi kwa Nmap, yaliyoundwa kwa ajili ya mtu yeyote anayetaka kujua zana hii nzuri ya kuchanganua mtandao. Kusudi ni kukupa maarifa ya kimsingi unayohitaji kutumia Nmap kwa ufanisi siku hadi siku.



Nmap ni zana yenye matumizi mengi, inayotumiwa sana na wataalamu wa IT, mtandao na usalama wa mtandao kwa ajili ya uchunguzi, ugunduzi wa mtandao na ukaguzi wa usalama. Mafunzo haya yanalenga wale ambao ni wapya kwa nyanja hizi na wangependa kujifunza misingi ya Nmap. Ujuzi wa kimsingi wa mfumo na usimamizi wa mtandao unapendekezwa.



Utajifunza misingi ya Nmap, jinsi ya kufanya ukaguzi wa mlango, kutambua seva pangishi zinazotumika kwenye mtandao, kugundua matoleo ya huduma na mifumo ya uendeshaji, kufanya ukaguzi wa uwezekano wa kuathiriwa na mengine mengi. Kila sehemu inajumuisha maelezo ya kina na mifano ya vitendo ili kukusaidia kutumia vyema Nmap katika miktadha mbalimbali.



Kufikia mwisho wa somo hili, utakuwa na ufahamu thabiti wa Nmap na utaweza kuitumia vyema ili kuboresha usalama na usimamizi wa mitandao yako. Furahia usomaji wako.



## 1 - Utangulizi wa Nmap: Nmap ni nini?



### I. Uwasilishaji



Katika sehemu hii ya kwanza, tutaangalia zana ya kuchanganua mtandao wa Nmap. Tutaangalia Elements muhimu unayohitaji kujua kuhusu zana hii na jinsi inavyofanya kazi kwa ujumla. Hii itatusaidia kuelewa vyema mafunzo mengine yote.



### II. Tunakuletea zana ya Nmap



Nmap, ya _Network Mapper_, ni zana isiyolipishwa na huria inayotumika kwa **ugunduzi wa mtandao, ukaguzi wa ramani na usalama**. Inaweza pia kutumika kwa kazi zingine kama vile ** orodha ya mtandao, uchunguzi au usimamizi**.



Inaweza kubainisha kama wapangishi kwenye mtandao unaolengwa wanatumika na wanaweza kufikiwa, huduma za mtandao zipi zinafichuliwa, matoleo na teknolojia zinatumika, na maelezo mengine muhimu ya uchanganuzi. Nmap inaweza kutumika kuchanganua huduma moja kwenye mashine mahususi, au katika maeneo makubwa ya mtandao, hadi kwenye Mtandao mzima.



Nguvu za Nmap ni nyingi:





- Yenye nguvu na rahisi**: Nmap inaweza kuchanganua mitandao mikubwa na kutumia mbinu za juu za utambuzi. Inaauni UDP, TCP, ICMP, IPv4 na IPv6, na inaweza kutambua toleo, uchanganuzi wa kuathirika au mwingiliano mahususi wa itifaki. Usanifu wake ni wa msimu, shukrani haswa kwa hati za NSE (Nmap Scripting Engine), ambazo tutaziangalia baadaye katika somo hili.
- Urahisi wa kutumia**: hati rasmi ni nyingi na za ubora wa juu zaidi. Rasilimali nyingi za jumuiya zinapatikana pia kukusaidia kuanza.
- Umaarufu na maisha marefu**: Nmap imekuwa rejeleo katika uwanja wake tangu 1998. Toleo la sasa, wakati wa sasisho hili, ni 7.95. Ingawa zana zingine zipo kwa kazi mahususi, Nmap inasalia kuwa lazima iwe nayo kwa uchoraji ramani na uchanganuzi wa mtandao.



**Nmap kwenye sinema**



Nmap ni mojawapo ya zana chache za usalama ambazo zimepata sifa mbaya miongoni mwa umma kwa ujumla. Inaonekana katika filamu ya _Matrix Reloaded_, katika tukio la nembo ambapo Trinity huitumia kuingilia mfumo:



![nmap-image](assets/fr/01.webp)



matrix: Tukio lililopakiwa upya lililo na Nmap



Anaonekana pia katika kazi zingine za sinema.



**Maoni



Kama msimamizi wa mfumo na kisha mkaguzi wa usalama wa mtandao na pentester, **mimi hutumia Nmap karibu kila siku** na **ninapendekeza** mara kwa mara kwa wasimamizi wa mfumo wanaotaka kuimarisha udhibiti wao wa mitandao na kuboresha uwezo wao wa uchunguzi.



### III. Uendeshaji wa hali ya juu



Nmap inapatikana kwa Linux, Windows na macOS. Imeandikwa hasa katika C, C++ na Lua (kwa hati za NSE). Inatumika zaidi kwenye safu ya amri, ingawa violesura vya michoro kama vile Zenmap vinapatikana pia. Hata hivyo, tunakushauri sana kuanza na mstari wa amri ili kuelewa vizuri jinsi inavyofanya kazi.



Mfano rahisi:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Amri hii itaelezewa kwa undani baadaye. Katika somo hili, tutakuwa tukitumia Nmap kwenye Linux, lakini matumizi yake yanafanana kwenye mifumo mingine. Chini ya Windows, Nmap inategemea **Npcap** maktaba (ikichukua nafasi ya WinPcap iliyopitwa na wakati) kunasa na kuingiza pakiti za mtandao.



Nmap inatumika kama binary ya kawaida, kama vile `ls` au `ip`. Baadhi ya vipengele vya kina vinaweza kuhitaji haki za juu, kwani wakati mwingine zana hubadilisha pakiti kwa njia zisizo za kawaida ili kuibua hisia mahususi kwenye mifumo inayolengwa (hasa kwa ajili ya huduma au utambuzi wa kuathirika).



### IV. Madhara ya kutumia Nmap



Kabla ya kutumia Nmap, ni muhimu kufahamu athari zake kwenye mitandao na mifumo:





- Inaweza kutuma **maelfu au hata mamilioni ya pakiti** kwa muda mfupi, ambayo inaweza kujaza miundomsingi fulani ya mtandao.
- Inaweza generate **pakiti mbovu au zisizo za kawaida**, zinazoweza kutatiza vifaa fulani (hasa mifumo ya viwandani).
- Inaweza kutoa **tabia kama ya uvamizi**, ambayo inaweza kusababisha arifa katika mifumo ya usalama (ngome, IDS/IPS, n.k.).



Kwa ujumla, **Nmap ni zana inayozungumza sana**, kwani inazalisha trafiki nyingi ili kutoa habari nyingi iwezekanavyo. Kwa hivyo inashauriwa kuelewa kikamilifu jinsi inavyofanya kazi kabla ya kuitumia kwenye mazingira nyeti au ya uzalishaji.



### V. Hitimisho



Sehemu hii inatanguliza Nmap na sifa zake kuu. Tumeona kuwa ni zana muhimu, yenye nguvu na inayoweza kunyumbulika ya ramani ya mtandao. Tumejadili pia jinsi inavyofanya kazi na tahadhari unazohitaji kuchukua unapoitumia, ili kuweka eneo la sehemu zifuatazo za mafunzo.



## 2 - Kwa nini utumie Nmap?



### I. Uwasilishaji



Katika sehemu hii, tutaangalia matumizi makuu ya zana ya kuchanganua mtandao wa Nmap. Tutaona kuwa ni zana ambayo hutumiwa sana katika miktadha na taaluma nyingi, na kwamba kuwa nayo kwenye kisanduku chako cha vidhibiti na kujua jinsi ya kuisimamia hakika ni ujuzi muhimu.



### II. Kutumia Nmap kwa uchunguzi na usimamizi



Nmap inaweza kutumika kwa uchunguzi wa mtandao na, kwa upana zaidi, kwa ufuatiliaji. Kwa njia sawa na ambayo ping inaweza kutumika kubainisha kama wapangishi wawili wanawasiliana, Nmap inaweza kutumika kubainisha kwa haraka ikiwa seva pangishi inatumika, au kama huduma fulani inafanya kazi. Shukrani kwa [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"), tunaweza kupata data sahihi kuhusu muda wa kujibu wa mwenyeji, njia inayochukuliwa na pakiti, jibu linalotolewa na huduma mahususi, n.k.



Amri ifuatayo na matokeo yanaweza kutumika, kwa mfano, ili kujua kwa haraka kama seva ya wavuti kwenye seva pangishi **192.168.1.18** inatumika na inajibu ipasavyo:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Tumia Nmap kupata hali ya huduma ya wavuti kutoka kwa seva ya mbali.*



Kwa hivyo, kutumia Nmap huenda zaidi kuliko "mtihani wa ping" maarufu wakati wa utatuzi au awamu za utambuzi. Tutaona baadaye kuwa kuna mbinu kadhaa zinazotumiwa na Nmap kutambua ni huduma gani inayosikilizwa kwenye mlango fulani, ikiwa ni pamoja na toleo lake.



### III. Kutumia Nmap kwa ramani ya mtandao



Kama _Network Mapper_, ramani ya mtandao ndio lengo kuu la zana hii. Inaweza kutumika ndani ya mtandao wa ndani, au katika mitandao mingi, subneti na VLAN, kuorodhesha seva pangishi na huduma zote zinazoweza kufikiwa. Nmap hufanya kazi hii kuwa ya haraka na bora zaidi kuliko njia yoyote ya mwongozo.



Kwa mfano, amri ifuatayo inaweza kutumika kutambua kwa haraka wapangishi amilifu kwenye mtandao wa **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Kumbuka: chaguo la `-sP` limepitwa na wakati na nafasi yake imechukuliwa na `-sn`.*



![nmap-image](assets/fr/03.webp)



*Kutumia Nmap kugundua wapangishaji wanaoweza kufikiwa kwenye mtandao*



Tutaona baadaye kuwa kuna mbinu kadhaa zinazotumiwa na Nmap ili kubaini kama mwenyeji anaweza kuchukuliwa kuwa "anayefanya kazi", hata kama haionyeshi huduma zozote.



### IV. Kutumia Nmap kutathmini sera ya uchujaji



Nmap ina faida ya kuwa ukweli: matokeo yake yanawezesha kupata matokeo halisi, tofauti na hati yoyote ya usanifu au sera ya uchujaji. Ni zana muhimu ya kutathmini ufanisi wa utenganishaji wa mfumo wa habari, kwani hukuruhusu **kuthibitisha ikiwa sera ya uchujaji inatumika**.



Katika mtandao wa ushirika, utendaji bora unaamuru kwamba mifumo igawanywe kulingana na jukumu, umuhimu au eneo. Sheria za uchujaji (mara nyingi hutekelezwa kupitia ngome) lazima zizuie mawasiliano kati ya kanda. Lakini usanidi huu mara nyingi ni ngumu na hukabiliwa na makosa.



Kwa hiyo, ili kuthibitisha kwamba sera imeheshimiwa, hakuna kitu kinachoshinda mtihani halisi. Kwa mfano, unaweza kuangalia kuwa huduma nyeti za usimamizi (SSH, WinRM, MSSQL, MySQL, n.k.) hazipatikani kutoka kwa eneo la mtumiaji.



Matumizi ya **Nmap kujaribu sera ya uchujaji** yanapaswa kuwa ya utaratibu kabla ya sera kama hiyo kuwekwa katika uzalishaji. Kwa bahati mbaya, hundi hii mara nyingi hupuuzwa.



Katika uzoefu wangu, makosa mengi ya usanidi hayatambuliki kwa kukosekana kwa vipimo vya uthibitisho. Hitilafu rahisi katika anuwai ya IP au uangalizi wa sheria unaweza kuacha eneo linalodaiwa kuwa limetengwa katika hatari.



### V. Kutumia Nmap kwa ukaguzi wa usalama na majaribio ya kupenya



Nmap ina **vipengele vingi muhimu vya tathmini ya usalama**, majaribio ya kupenya (pentest), na kwa bahati mbaya pia kwa washambuliaji.



Vipengele vya ugunduzi wa mtandao ni muhimu kwa mshambulizi, ambaye anahitaji kuelewa topolojia ya mtandao baada ya maelewano ya awali. Lakini Nmap inatoa mengi zaidi ya haya: inaunganisha injini ya uandishi, **nyingi ambazo zimejitolea kutambua uwezekano wa kuathirika**.



Kwa mfano, amri hii inaweza kutumika kuangalia kama huduma ya FTP inaruhusu muunganisho usiojulikana, bila kulazimika kuunganishwa mwenyewe:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Kutumia hati ya NSE kuangalia uthibitishaji wa FTP bila jina kupitia Nmap.*



Ugunduzi wa uwezekano wa Nmap ni mojawapo ya hatua za kwanza za ukaguzi au jaribio la kupenya. Hukuwezesha kutambua kwa haraka pointi fulani dhaifu na kuboresha juhudi zako za uchanganuzi.



Lakini jihadhari: **zana za kuchanganua uwezekano wa kuathiriwa zina kikomo**. Nmap inashughulikia sehemu ya vitisho pekee, na haihakikishi kuwa mfumo uko salama ikiwa hakuna matatizo yanayotambuliwa. Kwa hivyo ni muhimu **kuelewa jinsi hati zilivyotumia kazi** na sio kutegemea tu uamuzi wao.



### VI. Hitimisho



Tumeona kuwa ujuzi wa Nmap unaweza kushughulikia matukio mbalimbali ya utumiaji, kutoka kwa uchunguzi na ufuatiliaji hadi uchoraji wa ramani, tathmini ya sera ya usalama na uchanganuzi wa uwezekano wa kuathirika. Katika sehemu inayofuata, tutashuka hadi nitty-gritty na kusakinisha Nmap.




## 3 - Kusakinisha na kusanidi Nmap



### I. Uwasilishaji



Katika sehemu hii, tutajifunza jinsi ya kusakinisha zana ya kuchanganua mtandao wa Nmap kwenye Linux na Windows OS. Mwishoni mwa sehemu hii, tutakuwa na kila kitu tunachohitaji ili kuanza kutumia Nmap kwa moduli za siku zijazo. Hatimaye, tutaona ni mapendeleo gani inaweza kuhitaji inapotumiwa na kwa nini.



### II. Inasakinisha Nmap chini ya Linux



Nmap iliundwa awali ili kuendeshwa kwenye mifumo ya uendeshaji ya GNU/Linux. Kama matokeo, na shukrani kwa maisha marefu na umaarufu wake, utaipata katika hazina zote rasmi za usambazaji mkubwa wa Unix. Katika mafunzo haya, nitakuwa nikitumia mfumo wa uendeshaji unaotegemea Debian [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Lakini unaweza kuitumia kwa njia sawa kabisa kutoka kwa Debian ya kawaida, CentOS, Red Hat au chochote!



Chini ya Debian, ili kuangalia kuwa Nmap iko kwenye hazina zako za sasa, unaweza kutumia amri ifuatayo:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Jibu hapa linaonyesha wazi kuwa kifurushi cha "nmap" kipo kwenye hazina (hapa, zile za Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux"). Kuanzia sasa na kuendelea, unaweza kusakinisha Nmap kupitia amri za kawaida za usakinishaji, hakuna kitu cha kupokonya silaha kwa sasa 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Ili kuangalia kuwa Nmap imesakinishwa kwa usahihi, tutaonyesha toleo lake:



```
nmap --version
```



Hapa kuna matokeo yanayotarajiwa:



![nmap-image](assets/fr/05.webp)



matokeo ya kuonyesha toleo la sasa la Nmap._



Kumbuka uwepo katika onyesho hili la maktaba ya "libpcap" (_Packet Capture Library_) na toleo lake. Pia inatumiwa na Wireshark, "libpcap" inatumiwa na Nmap kuunda na kuendesha pakiti na kusikiliza trafiki ya mtandao.



### III Kufunga Nmap kwenye Windows



Ili kusakinisha kwenye mfumo wa uendeshaji wa Windows, anza kwa kupakua jozi kutoka kwa tovuti rasmi (na hakuna nyingine!):





- Ukurasa wa upakuaji wa Nmap kwenye tovuti rasmi: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Kisha utahitaji kupakua binary inayoitwa `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



nmap kwa usakinishaji wa ukurasa wa upakuaji wa binary wa Windows



Mara tu ukiwa na binary hii kwenye mfumo wako, iendeshe tu ili kusakinisha Nmap. Huu ni usakinishaji wa moja kwa moja, na unaweza kuacha chaguo zote kama chaguo-msingi.



Reflex yangu ni kutengua kisanduku cha "zenmap (GUI Frontend)". Hii ni picha ya Interface ya Nmap ambayo siitumii na haitashughulikiwa katika mafunzo haya, lakini jisikie huru kuijaribu mara tu unapofahamu zana ya mstari wa amri ya Nmap!



![nmap-image](assets/fr/07.webp)



kwa hiari kuteua Zenmap wakati wa kusakinisha Nmap kwenye Windows



Mwishoni mwa usakinishaji wa Nmap, usakinishaji wa pili unapendekezwa: ule wa maktaba ya "Npcap":



![nmap-image](assets/fr/08.webp)



usakinishaji wa maktaba ya "Npcap" wakati wa kusakinisha Nmap chini ya Windows



Hii ndiyo maktaba ambayo Nmap inategemea kusimamia mawasiliano ya mtandao, yaani, kujenga, kutuma na kupokea pakiti za mtandao. Labda tayari umekutana na maktaba hii ikiwa unatumia Wireshark kwenye Windows, kwani inaitumia pia na inahitaji usakinishaji.



Kama ilivyo kwa Linux, unaweza kuthibitisha kuwa Nmap imesakinishwa kwa kufungua Command Prompt au terminal ya [Powershell] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") na kuandika amri ifuatayo:



```
nmap --version
```



Hapa kuna matokeo yanayotarajiwa:



![nmap-image](assets/fr/09.webp)



matokeo ya kuonyesha toleo la sasa la Nmap._



Nmap sasa imesakinishwa kwenye Windows. Unaweza kuitumia kwa njia sawa kabisa na kwenye Linux, kwa kufuata mafunzo haya.



### IV. Haki za ndani zinazohitajika ili kutumia Nmap



Lakini kwa njia, unapotumia Nmap, **je ni muhimu kuwa na marupurupu ya juu ya ndani kwenye mfumo?** Jibu ni: **inategemea**.



Katika hali yake ya kimsingi, yaani, bila kwenda mbali sana katika kutumia chaguzi zake, Nmap haihitaji haki za upendeleo. Walakini, hivi karibuni utagundua kuwa ni bora kutumia Nmap katika muktadha wa upendeleo ("mizizi" chini ya Linux, "msimamizi" au sawa chini ya Windows) ili kuweza kuitumia kwa uwezo wake kamili, kwa hatari ya kupata ujumbe wa makosa kama huu:



![nmap-image](assets/fr/10.webp)



ujumbe wa makosa chini ya Linux wakati chaguzi za Nmap zinahitaji haki za mizizi._



Iwe kwenye Linux au Windows, kuna hali nyingi ambapo Nmap itakuuliza upate ufikiaji wa upendeleo. Sababu kuu ni kama ifuatavyo (orodha isiyo kamili):





- Kuunda pakiti za mtandao "mbichi"**: Nmap ina uwezo wa anuwai ya mbinu za kuchanganua, ikiwa ni pamoja na upotoshaji wa pakiti wa hali ya juu na ujenzi. Hivi ndivyo hali ilivyo, kwa mfano, tunapotaka kufanya uchanganuzi wa TCP SYN, ambao hauheshimu desturi ya _Three-way handshake_ ya ubadilishanaji wa TCP. Ili kufanya hivyo, Nmap inahitaji kutumia vitendaji isipokuwa zile asili za mifumo ya uendeshaji, ambayo inajua tu jinsi ya kuheshimu utendaji mzuri katika mawasiliano ya mtandao (inatoa wito kwa maktaba za "Npcap" na "libcap" zilizoonekana hapo juu). Ni kwa sababu Nmap haifanyi mambo kwa njia "ya kawaida" ambayo inaweza kupata habari fulani kuhusu OS, huduma na udhaifu fulani.





- Sikiliza trafiki ya mtandao**: baadhi ya chaguo za Nmap huihitaji isikilize mtandao ili kupata taarifa fulani. Kitendo hiki kinachukuliwa kuwa nyeti kwenye mifumo ya uendeshaji, kwani pia hukuruhusu kusikiliza mawasiliano ya programu zingine kwenye mfumo. Kama vile Wireshark, Nmap inahitaji mapendeleo maalum kufanya hivi, ambayo ni rahisi kupata kwa kuwa moja kwa moja kwenye kipindi cha bahati.





- Kusikiliza kwenye bandari za upendeleo**: kwenye mifumo ya uendeshaji, bandari kutoka 0 hadi 1024 (TCP pamoja na UDP) zinasemekana kuwa za upendeleo, i.e. zimehifadhiwa kwa matumizi maalum sana na kwa hivyo zinalindwa. Ingawa hii ni sababu ya kizamani leo, bado ni muhimu kuwa na mapendeleo fulani ya kusikiliza kwenye bandari hizi, ambayo Nmap inaweza kufanya kulingana na jinsi itatumika.





- Kutuma pakiti za UDP:** Vile vile, kusikiliza programu ya mtandao kwenye bandari za UDP (itifaki isiyo na uraia) kunahitaji haki za upendeleo kwenye mifumo ya uendeshaji. Kwa hivyo, kikao cha upendeleo kitahitajika ikiwa ungependa kufanya uchunguzi wa UDP, ambao Nmap italazimika kusikiliza jibu ili kuchanganua majibu ya skanisho zake.




Ili kuwa sahihi zaidi, inawezekana, angalau chini ya Linux, kuendesha Nmap na kazi zake zote na chaguo bila kuwa mzizi. Hii inafanikiwa kwa kutoa _capabilities_ haki kwa mfumo wa jozi. Walakini, hii inahitaji ujanja wa hali ya juu na inaweza isiwe ya vitendo kama kuendesha Nmap moja kwa moja na upendeleo. Pia, mbinu hii si ya kawaida na inaweza kusababisha matatizo ya usalama ikiwa imesanidiwa vibaya.



Hata hivyo, huku ni kuondoka kidogo kutoka kwa mafunzo yetu ya Nmap, kwa hivyo tutaachana nayo kwa sasa.



Kwa mafunzo haya mengine, chukulia kuwa Nmap kila wakati inaendeshwa kama "mizizi" (kutoka kwa ganda kama "mizizi" au kupitia amri ya "sudo"), au kwenye terminal ya msimamizi chini ya Windows, hata ikiwa hii haijaonyeshwa. Vinginevyo, unaweza kupata tofauti ndogo lakini dhahiri kutoka kwa mafunzo.



### V. Hitimisho



Ni hayo tu! Nmap sasa imesakinishwa kwenye mfumo wetu wa uendeshaji na iko tayari kutumika, bila kuhitaji usanidi zaidi. Sehemu hii inahitimisha utangulizi na uwasilishaji wa Nmap. Natumai imefanya vinywa vyenu vinywe maji, na kwamba mna hamu ya kuanza kufanya mazoezi.



Kwa umakini zaidi, sasa tuna wazo bora zaidi la zana ya kutengeneza ramani ya Nmap ni nini na matumizi yake ya kawaida ni nini, pamoja na mapungufu yake. Hebu tuendelee!




## 4 - TCP na UDP huchanganua bandari kwa kutumia Nmap



### I. Uwasilishaji



Katika sehemu hii, tutajifunza jinsi ya kufanya upekuzi wetu wa kwanza kwenye mlango kwa kutumia zana ya kuchanganua mtandao wa Nmap. Tutaona jinsi ya kuitumia kuunda orodha ya huduma za mtandao zilizofichuliwa kwa seva pangishi, iwe kwa kutumia itifaki za TCP au UDP.



Kuanzia sasa na kuendelea, kumbuka kuchanganua seva pangishi pekee katika mazingira yaliyodhibitiwa ambayo unayo idhini ya wazi.





- Kama ukumbusho: [Msimbo wa Adhabu: Sura ya Tatu: Hushambulia mifumo ya kiotomatiki ya kuchakata data](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Ikiwa huna moja ya kukabidhi **, ninapendekeza suluhu zifuatazo za bure, ambazo ni jambo pekee!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Jukwaa la mafunzo la Udukuzi, Hack The Box kila mara hukupa mifumo hatarishi ili uweze kushambulia unavyoona inafaa. Mifumo mia kadhaa inapatikana, lakini dimbwi jipya la mashine 20 hutolewa bila malipo mwaka mzima, na ufikiaji kupitia OpenVPN VPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Mfumo huu unatoa mifumo mingi hatarishi kimakusudi kwa upakuaji, ambayo inaweza kutumika kupitia VirtualBox (pia suluhu isiyolipishwa) au njia nyinginezo. Mara baada ya kupakuliwa, hakuna haja ya VPN - kila kitu ni cha ndani.




Pia, uko huru **kuunda mashine pepe** kwenye mfumo wako wa uendeshaji unaoupenda na usakinishe huduma mbalimbali juu yake kama malengo ya majaribio. Faida hapa itakuwa kwamba utaweza pia kuona kile kinachotokea kwenye upande wa seva wakati wa kuchanganua, haswa kwa Wireshark, na kuwa na mkono kwenye ngome ya ndani tunapofanya majaribio ya hali ya juu zaidi.



Hebu tupate vitendo!



### II. Inachanganua bandari za TCP za mwenyeji kupitia Nmap



#### A. Uchanganuzi wa bandari wa TCP wa kwanza kwa Nmap



Sasa tutafanya ukaguzi wetu wa kwanza kupitia Nmap. Lengo letu hapa ni rahisi: tunataka kujua ni huduma zipi zinazofichuliwa na seva ya wavuti ambayo tumetumia hivi punde, ili kuona kama kuna jambo lolote lisilotarajiwa, kama vile huduma ya usimamizi ambayo haifai kufikiwa, au kufichuliwa kwa mlango wa programu ambayo tulifikiri kuwa ilisitishwa.



Katika mfano wangu, mwenyeji atakayechanganuliwa ana IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Hapa kuna matokeo yanayowezekana. Tunaona kurudi kwa Nmap ya kawaida na habari nyingi:



![nmap-image](assets/fr/11.webp)



matokeo ya uchunguzi rahisi wa TCP uliofanywa na Nmap._



Kwa kuangalia matokeo haya kwa haraka, tunaelewa kuwa bandari TCP/22 na TCP/80 zinaweza kufikiwa na seva pangishi hii.



Kwa chaguo-msingi, na usipoiambia, Nmap itachanganua tu bandari za TCP.



#### B. Kuelewa matokeo ya uchunguzi rahisi wa Nmap



Hebu tuende hatua zaidi, hata hivyo, ili kuelewa pato hili: kila mstari ni muhimu, kwanza kujua nini kimefanywa hivi karibuni, na pili kutafsiri vizuri matokeo ya scan wenyewe.



Mstari wa kwanza kimsingi ni ukumbusho wa toleo la skanisho na tarehe (muhimu kwa ukataji miti na kuweka kumbukumbu baada ya yote!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Mstari wa pili unaonyesha mwanzo wa matokeo ya skanisho kwa mwenyeji "debian.home (192.168.1.19)". Habari hii itakuwa muhimu tunapoanza kuchanganua wapangishaji kadhaa kwa wakati mmoja:



```
Nmap scan report for debian.home (192.168.1.19)
```



Mstari wa tatu unatuambia kuwa mwenyeji anayehusika ni "Juu", yaani amilifu:



```
Host is up (0.00022s latency).
```



Hatimaye, Nmap inatufahamisha kwamba bandari 998 za TCP zilizotambuliwa kama zimefungwa hazionyeshwa kwenye:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Hii inatuokoa karibu mistari 1,000 ya pato inaonekana kama:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Asante kwa kutuepusha na hili!



Kwa nini bandari 998 "zimefungwa"? Kuongeza lango 2 zilizo wazi hufanya 1000, na hiyo ndiyo idadi ya milango ambayo Nmap itachanganua katika usanidi wake chaguomsingi, si bandari za TCP 65535 zilizopo! Tutaona baadaye kuwa hii inaweza kubinafsishwa kabisa na kwa urahisi. Lakini ikiwa seva pangishi inayolengwa ina huduma inayosikiza kwenye mlango wa kigeni, utambulisho huu wa "chaguo-msingi" hautafichua.



Kufuatia habari hii, tunapata kinachovutia zaidi: jedwali lililopangwa kulingana na safu tatu "PORT - STATE - SERVICE":





- Safu wima ya kwanza ya "PORT" inaonyesha tu lango/itifaki inayolengwa, na ni muhimu hapa kuangalia ikiwa ni mlango wa TCP (`<port>/tcp`) au UDP (`<port>/udp`).





- Safu ya "STATE" inaonyesha hali ya huduma ya mtandao iliyogunduliwa kwenye bandari hii na kuamuliwa na Nmap kwa misingi ya jibu lililopatikana. Hii inaweza kuwa "wazi", "imefungwa", "iliyochujwa" au "haijulikani". Tutaona baadaye jinsi Nmap inavyotofautisha kati ya majimbo haya tofauti.





- Safu wima ya "SERVICE" inaonyesha huduma iliyofichuliwa kwenye bandari inayohusika. Tafadhali kumbuka, hata hivyo, kwamba hatujatumia chaguo zinazotumika za ugunduzi wa huduma hapa. Nmap inategemea rejeleo la ndani kati ya bandari/itifaki na huduma inayodaiwa kupewa: faili "/etc/services"




Ukiangalia faili ya "/etc/services" kwenye mfumo wa Linux, utapata kiungo cha "port/protocol - service" sawa na ile iliyoonyeshwa na Nmap:



![nmap-image](assets/fr/12.webp)



hutoa yaliyomo kwenye faili ya "/etc/services" chini ya Linux._



Ni muhimu kuelewa kwamba, kwa sasa, Nmap haijagundua huduma yoyote inayoendelea. Kwa mfano, haingewezekana kutambua huduma ya SSH nyuma ya bandari ya TCP/80 ikiwa hivi ndivyo ilivyokuwa. Kwa hivyo umuhimu wa kujua jinsi ya kutumia chaguo sahihi - inakuja hivi karibuni!



Kujua jinsi ya kutafsiri matokeo ya Nmap ni sehemu muhimu ya kusimamia zana. Habari njema ni kwamba matokeo haya yatakuwa sawa, chaguzi zozote utakazotumia.



#### C. Chini ya kofia: uchambuzi wa mtandao kupitia Wireshark



Ukiangalia kwa karibu kile kinachotokea kwenye mtandao wa Interface wa mwenyeji anayechanganua seva, au kwenye seva yenyewe, vitendo vya Nmap vitakuwa wazi zaidi. Hiyo ndiyo tutafanya hapa.



Ninachoweza kukuonyesha hapa ni sehemu tu ya kile kinachoonekana kwenye Wireshark. Ikiwa ungependa kwenda mbali zaidi, jisikie huru kujinasa mtandaoni wakati wa kuchanganua, kisha uvinjari kile ambacho kimenaswa.



Katika jaribio hili, mwenyeji wangu wa skanisho (192.168.1.18) na mwenyeji wangu lengwa (192.168.1.19) wako kwenye mtandao mmoja wa ndani.



Nmap huanza kwa kubaini kama mwenyeji anayelengwa anatumika kwenye mtandao wa ndani kwa kutuma ombi la ARP. Ikipokea jibu, inajua kuwa seva pangishi inatumika na inaanza kuchanganua mtandao wake:



![nmap-image](assets/fr/13.webp)



_Ombi la ARP lililotolewa na Nmap ili kubaini kama mwenyeji lengwa yupo kwenye mtandao wa ndani._



Ikiwa seva pangishi itakayochanganuliwa iko kwenye mtandao wa mbali, Nmap huanza kwa kutuma ombi la ping na kujaribu kufikia baadhi ya milango inayoonekana mara kwa mara (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



ombi la ping lililotolewa na Nmap ili kubaini ikiwa mwenyeji anayelengwa anapatikana kwenye mtandao wa mbali



Ikipata jibu kwa jaribio lolote kati ya haya, inazingatia lengo kuwa amilifu.



Mara baada ya Nmap kuamua kuwa lengo lake linatumika, itajaribu kutatua jina la kikoa chake na seva ya DNS iliyosanidiwa kwenye kadi ya mtandao:



![nmap-image](assets/fr/15.webp)



azimio la dNS kwenye lengo la skanisho la Nmap



Sasa kwa kuwa Nmap imetambua lengo lake na inajua kuwa ni amilifu, inaanza uchunguzi wake wa bandari wa TCP:



![nmap-image](assets/fr/16.webp)



Usambazaji wa pakiti za tCP SYN na mapokezi ya RST/ACK wakati wa kuchanganua Nmap



Ili kufanya hivyo, katika kila bandari ya TCP katika safu yake chaguomsingi, **itatuma pakiti za TCP SYN na kusubiri jibu**. Katika picha ya skrini hapo juu, inapokea pakiti za TCP RST/ACK kutoka kwa seva iliyochanganuliwa, ikimaanisha "songa mbele, hakuna kitu cha kuona hapa" - kwa maneno mengine, bandari hizi zimefungwa. Kama tulivyoona katika matokeo, hii itakuwa kesi kwa bandari nyingi zilizochanganuliwa. Isipokuwa mbili:



![nmap-image](assets/fr/17.webp)



jibu kwa pakiti ya TCP SYN iliyotumwa kwenye mlango wa 22, inayotumika kwenye shabaha ya kuchanganua



Katika picha ya skrini iliyo hapo juu, tunaona pakiti ya TCP SYN/ACK iliyotumwa na mwenyeji lengwa**. Bandari inatumika na inaonyesha huduma. Nmap inakubali kupokea jibu, kisha hukatisha muunganisho (TCP RST/ACK). **Hivi ndivyo ilivyojua kuwa bandari TCP/22 ilikuwa hai**.



Tumeona hapa kwamba Nmap inaheshimu "Three Way Handshake" inapochanganua mtandao wa TCP. Kwa sababu za utendaji, inawezekana kuuliza si kujibu kurudi kwa seva, na hivyo kuokoa pakiti elfu kadhaa wakati wa skanning mtandao mkubwa. Lakini tutaangalia chaguo hizi na uboreshaji baadaye katika mafunzo.



Sasa tuna wazo bora la jinsi ya kufanya uchunguzi wa TCP na kile kinachotokea wakati unafanywa. Tumeona pia kuwa, kwa chaguo-msingi, Nmap hufanya uchunguzi wa bandari wa TCP kwenye idadi ndogo ya bandari.



### III. Inachanganua bandari za UDP kwa kutumia Nmap



#### A. Uchanganuzi wa kwanza wa bandari ya UDP na Nmap



Sasa hebu tuone jinsi ya kuchanganua bandari za UDP za mwenyeji. Kama tulivyoona, kwa chaguo-msingi Nmap itachanganua milango ya TCP kila wakati. Hii inaweza kumaanisha kukosa habari nyingi ikiwa hatujui.



Kama ukumbusho, kwa madhumuni ya jaribio hili, mwenyeji wangu wa kuchanganua (192.168.1.18) na mwenyeji wangu lengwa (192.168.1.19) wako kwenye mtandao sawa wa karibu.



```
nmap -sU 192.168.1.19
```



Hapa, urejeshaji uliopatikana una umbizo sawa na la uchanganuzi wa TCP, lakini huduma amilifu zinazoonyeshwa ziko katika `<port>/UDP`, kama ilivyoombwa!



![nmap-image](assets/fr/18.webp)



matokeo ya uchanganuzi rahisi wa UDP uliofanywa na Nmap._



Chaguo la "-sU" linatumika kumwambia Nmap kuwa unataka kufanya kazi kwenye UDP, badala ya TCP kama chaguo-msingi.



Kwa njia, labda utagundua kuwa Nmap inahitaji haki za "mizizi" kwa uchanganuzi wa UDP, kama ilivyotajwa hapo awali kwenye mafunzo.



kumbuka: Kwa kuwa matoleo ya hivi punde zaidi ya Nmap, inashauriwa kila wakati kuendesha skana za UDP kwa upendeleo wa msimamizi ili kuhakikisha matokeo ya kuaminika, kwani baadhi ya vipengele vinahitaji ufikiaji ghafi wa soketi za mtandao._



Uchanganuzi wa UDP unaweza kuchukua muda mrefu sana (sekunde 1100 kuchanganua bandari 1000 kwa mfano wangu), kwa sababu ya kukosekana kwa "Three Way Handshake" katika UDP, ambayo inamaanisha kuwa Nmap itasubiri kurudi kwa kila pakiti ya UDP iliyotumwa, na itaamua bandari kuwa "imefungwa" ikiwa tu hakuna kurudi baada ya muda fulani (muda wa kuisha). Jibu hili kutoka kwa wapangishi waliochanganuliwa si la kimfumo na mara nyingi hupunguzwa kulingana na idadi ya majibu kwa sekunde, ili kuepuka mashambulizi fulani ya ukuzaji. Hii ni tofauti na TCP, ambapo kuna jibu la papo hapo kutoka kwa seva pangishi iliyochanganuliwa, ikiwa mlango umefunguliwa au umefungwa. Tutaona baadaye jinsi ya kuboresha hii.



Ugumu wa pili wa UDP ni **kwamba huduma hazijibu kila mara kwa pakiti zinazoingia**, kwa urahisi kabisa kwa sababu hii si lazima kila wakati na ni kanuni ya UDP. Wakati hali ikiwa hivi, na hakuna "bandari isiyoweza kufikiwa" ya ICMP inapokewa, huduma hiyo inatiwa alama kama "wazi|iliyochujwa" na Nmap, kama inavyoonyeshwa kwenye picha ya skrini hapo juu.



#### B. Chini ya kofia: uchambuzi wa mtandao kupitia Wireshark



Kama ilivyo kwa uchunguzi wetu wa TCP, hebu tuangalie kwa karibu kile kinachotokea katika kiwango cha mtandao wakati wa kuchanganua UDP kwa kutumia uchanganuzi wa Wireshark. Tabia ya Nmap katika kubaini kama mwenyeji yuko hai ni sawa.



Tofauti pekee ya kweli wakati wa kuchanganua UDP ni kwamba Nmap haitasubiri "Three Way Handshake", kwa kuwa utaratibu huu haupo katika UDP (itifaki isiyo na uraia):



![nmap-image](assets/fr/19.webp)



Usambazaji wa pakiti za uDP na mapokezi ya ICMP (bandari haipatikani) wakati wa kuchanganua Nmap



Tunaweza kuona kwenye picha ya skrini iliyo hapo juu kwamba Nmap itatuma idadi kubwa ya pakiti za UDP, na kupokea kwa nyingi kati ya hizo pakiti ya ICMP "Lengwa lisilofikiwa (Mlango haupatikani)" kwa kujibu. Hili ni jambo la kawaida, kwa kuwa ni jibu lifaalo linalofafanuliwa na [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") wakati bandari ya UDP haiwezi kufikiwa:



![nmap-image](assets/fr/20.webp)



dondoo kutoka RFC 1122._



Wacha tuangalie kwa karibu kunasa huku kwa Wireshark, ambayo inaonyesha ** hali tatu zinazowezekana** katika UDP:



![nmap-image](assets/fr/21.webp)



kunasa mtandao wakati wa kuchanganua UDP kwenye bandari tofauti na Nmap._



Kesi hizo tatu ni kama ifuatavyo:





- Exchange ya kwanza imeundwa na pakiti No. 3, 4 na 8, 9. Nmap hutuma pakiti za UDP kwenye mlango wa kawaida wa SNMP na kwa hivyo **hutengeneza pakiti zinazotii itifaki mapema**. Kisha hupata jibu kutoka kwa seva (pakiti no. 8 na 9). Matokeo: Nmap imepokea jibu, huduma "imefunguliwa".





- Exchange ya pili inajumuisha pakiti 6 na 7. Nmap hutuma pakiti "tupu" ya UDP (bila muundo wa itifaki) kwenye bandari ya UDP/165, na inapokea pakiti ya ICMP kwa kujibu: "Lengo halipatikani (Bandari haipatikani)". Matokeo: Nmap imepokea jibu (hasi), mwenyeji yuko juu, lakini huduma ambayo ilijaribu kufikia haifanyi kazi kwenye bandari hii, ambayo itawekwa alama kuwa "imefungwa".





- Exchange ya mwisho ina pakiti no. 12: Nmap hutuma pakiti "tupu" ya UDP kwenye bandari ya UDP/1235. Hakuna jibu, hata kukataa kwa uwazi kutoka kwa seva pangishi iliyochanganuliwa. Matokeo: Nmap inatia alama bandari kuwa "imefunguliwa|iliyochujwa", kwa kuwa haiwezi kutambua kama hii ni kwa sababu ya kuwepo kwa ngome, iliyosanidiwa kutojibu, au kwa huduma inayotumika ya UDP ambayo haileti jibu hata hivyo (si lazima katika UDP).




Hapa kuna matokeo yaliyoonyeshwa na Nmap kufuatia kesi hizi tatu:



![nmap-image](assets/fr/22.webp)



matokeo ya uwezekano wa uchunguzi wa UDP uliofanywa kupitia Nmap._



Sasa tuna wazo bora la jinsi ya kufanya uchanganuzi wa UDP na nini hasa hufanyika inapofanywa. Kufikia sasa tumekuwa tukitumia Nmap kwa njia rahisi sana, bila kuamua ni bandari zipi za kuchanganua, lakini hiyo inakaribia kubadilika!



### IV. Kuchanganua mlango vizuri kwa kutumia Nmap



#### A. Kikumbusho cha tabia chaguomsingi ya Nmap



Kama tulivyoona, Nmap yenyewe huchagua nambari na milango ya kuchanganua ikiwa hutabainisha chaguo zozote. Huu ndio usanidi wa "chaguo-msingi" unaotumiwa na Nmap wakati haujaiambia la kufanya. Chaguzi hizi chaguomsingi zimeundwa ili kutoa wazo la lango kuu lililofichuliwa, hizi zikichaguliwa kwa mara kwa mara ya kufichua (lango la kawaida au la mara kwa mara) badala ya kwa mpangilio wa nambari (mlango 1, 2, 3, n.k.) na pia kuzuia kuanza kuchanganua milango 65535 ikiwa hutabainisha chaguo zinazofaa, ambazo zitakuwa ndefu sana na neno neno kwa hali ya matumizi "chaguo-msingi".



**Bandari hizi huchaguliwaje?



Lango 1000 zilizochanganuliwa katika hali chaguo-msingi huchaguliwa kulingana na marudio ya kutokea. Takwimu hizi hudumishwa na Nmap na kusasishwa kwa njia sawa na binary yenyewe na hati zake (moduli). Unaweza kutazama takwimu hizi mwenyewe katika faili ya "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



imetolewa kutoka kwa faili "/usr/shares/nmap/nmap-services"._



Hapa, katika safu ya tatu, tunaona kile kinachoonekana kama uwezekano (kati ya 0 na 1) au usambazaji wa asilimia. Huu ni mzunguko wa kutokea kwa kila jozi ya bandari/itifaki. Tunaweza kuona kwamba bandari zinazojulikana zaidi (FTP, SSH, TELNET na SMTP katika dondoo hili) zina thamani ya juu zaidi kuliko nyingine.



#### B. Bainisha kwa usahihi milango lengwa ya uchanganuzi wa Nmap



Hata hivyo, katika ulimwengu wa kweli, huenda tukahitaji kuchanganua lango mahususi pekee, au bandari kadhaa, au safu mahususi ya bandari. Nmap hurahisisha kufanya hivyo, kwa njia moja kwa skanisho za UDP na TCP.



** Changanua bandari maalum kupitia Nmap**



Ikiwa tunataka kuchanganua mlango mmoja, na sio 1000, tunaweza kubainisha mlango huu kupitia chaguo la Nmap la "-p" au "---port":



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Kwa hivyo, uchanganuzi utakuwa wa haraka zaidi na Nmap itatoa tu pakiti zinazohitajika ili kutambua kama seva pangishi inatumika, na kisha kama mlango uliobainishwa unaweza kufikiwa. Hii inaokoa muda ikiwa ungependa tu kufanya jaribio la haraka ili kuona kama huduma ya wavuti kwenye tovuti yako ya maonyesho bado iko.



** Changanua bandari nyingi kupitia Nmap**



Kwa njia hiyo hiyo, tunaweza kutaja bandari kadhaa kwa Nmap, kwa kutumia chaguo sawa na kuunganisha bandari zilizoainishwa na koma:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Bila kujali agizo, Nmap itaangalia bandari hizi zote, na zile tu zilizo kwenye seva pangishi inayolengwa. Utagundua katika matokeo ya Nmap kuwa ** inatuambia kwa uwazi bandari zote na hali zao **, hata kama "zimefungwa". Tofauti na tabia chaguo-msingi, ambapo matokeo haya kamili yangechukua nafasi nyingi sana:



![nmap-image](assets/fr/24.webp)



*Matokeo ya uchunguzi wa Nmap TCP kwenye bandari zilizoonyeshwa.*



**Changanua anuwai ya bandari



Ikiwa idadi ya milango unayotaka kuchanganua ni kubwa mno, unaweza kubainisha kulingana na masafa, kwa mfano:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Kwa kweli, unaweza kuchanganya na kulinganisha unavyoona inafaa, kwa mfano:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Uchanganuzi wa bandari wa TCP na UDP



Unaweza pia kufanya uchanganuzi wa UDP na TCP kwa wakati mmoja, kwenye bandari zilizochaguliwa:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Utagundua katika mfano huu wa mwisho uwepo wa "U:" kuashiria bandari ya UDP na "T:" kuashiria lango la TCP. Hapa kuna matokeo yanayowezekana ya aina hii ya skanisho:



![nmap-image](assets/fr/25.webp)



*Matokeo ya uchunguzi wa bandari wa TCP na UDP kwa kutumia Nmap.*



Sasa hiyo ni njia ya kuvutia ya kubinafsisha uchanganuzi wako!



** Changanua bandari zote



Hatimaye, inawezekana kubainisha masafa makubwa zaidi au madogo zaidi kwa Nmap. Tumeona kuwa orodha chaguo-msingi iliyochaguliwa na Nmap ina bandari 1000. Tunaweza pia kuuliza bandari 100 zinazoongoza mara kwa mara, au 200 za juu, kwa kutumia chaguo la "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Hatimaye, tunaweza kuiomba ichanganue bandari zote zinazowezekana (zote 65535), kwa kutumia nukuu ya "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Mwisho utachukua muda mrefu zaidi, haswa na UDP, lakini utahakikisha hutakosa bandari zozote zilizo wazi.



*Kumbuka: Chaguo la "-p-" ndiyo njia inayopendekezwa ya kuchanganua milango yote ya TCP. Kwa uchunguzi wa UDP, inashauriwa kuweka kikomo cha idadi ya milango kwa sababu za utendakazi, kwa kuwa uchanganuzi kamili wa bandari zote za UDP unaweza kuchukua muda mrefu sana.*



Baadaye katika mafunzo, tutaona jinsi ya kuongeza kasi ya uchanganuzi wa Nmap ili kukidhi mahitaji yetu, ambayo yatakuwa muhimu sana kwa uchanganuzi kwenye bandari zote za TCP na UDP.



### V. Hitimisho



Katika sehemu hii, hatimaye tumepata mazoezi ya moja kwa moja, kwa hivyo sasa tunajua **jinsi ya kutumia Nmap kwa njia ya msingi kuchanganua bandari za TCP na UDP za mwenyeji**. Pia tumeangalia kwa kina kile kinachotokea katika kiwango cha mtandao na **jinsi Nmap huamua ikiwa mlango wa TCP au UDP unatumika au la**. Hatimaye, tunajua jinsi ya kuchagua milango vizuri tunayotaka kuchanganua na **chaguo-msingi za Nmap hufanya nini**. Katika kile kinachofuata, tutatumia tena maarifa haya na kuyatumia kuchanganua mtandao mzima, ikijumuisha ramani ya kimataifa na ugunduzi wa mtandao.




## 5 - Ramani ya mtandao na ugunduzi na Nmap



### I. Uwasilishaji



Katika sehemu hii, tutajifunza jinsi ya kutumia zana ya kuchanganua mtandao wa Nmap kuweka ramani ya mtandao wako. Tutaona jinsi inavyoweza kuwa na ufanisi katika kazi hii, kupitia chaguzi zake mbalimbali. Hatimaye, tutaangalia njia tofauti za kubainisha shabaha za skanisho zetu kwa Nmap.



Hasa, tutakuwa tukitumia tulichojifunza katika sehemu iliyotangulia kuhusu jinsi Nmap huamua kama seva pangishi inatumika na inapatikana.



Kama ilivyotajwa katika utangulizi wa Nmap, huyu ni Ramani wa Mtandao. Kwa hivyo, ndiyo zana bora zaidi ya kuunda orodha ya wapangishi wanaoweza kufikiwa kwenye mtandao, iwe wa ndani au wa mbali.



**Kurudi kwa mwandishi:**



Kwa kweli, kama mkaguzi wa cybersecurity na pentester, mimi hutumia Nmap kwa utaratibu wakati wa kufanya majaribio ya kupenya ndani ili kujua nilipo, majirani zangu ni akina nani kwenye mtandao wa ndani na mitandao mingine inapatikana, pamoja na mifumo iliyo juu yao. Kusudi langu ni rahisi: kuweka ramani ya mtandao, kuamua saizi ya mfumo wa habari na, haswa, kuchora uso wake wa shambulio.



Upangaji ramani wa mtandao unaweza pia kuwa muhimu katika muktadha wa uchunguzi wa mtandao, usimamizi, ramani ya vipengee (una uhakika kabisa kuwa IS yako inaundwa na kile kilicho katika Orodha Amilifu pekee au katika Orodha yako ya GLPI/OCS? Inaweza pia kutumiwa kutambua uwepo wa Shadow IT kwenye mfumo wako wa taarifa.



### II. Kwa kutumia Nmap kuchanganua masafa ya mtandao



#### A. Kugundua mtandao kwa kuchanganua Nmap



Sasa tungependa kuongeza gia na kuchanganua mtandao wetu wote wa karibu. Hakuna kinachoweza kuwa rahisi zaidi: tunachohitaji kufanya ni kutumia tena amri tulizoziona katika sehemu iliyopita, lakini taja CIDR badala ya IP rahisi Address.



CIDR (**Uelekezaji wa Kikoa Isiyo na Daraja**) ni nukuu "ya kawaida" ya kubainisha masafa ya mtandao na kiwango chake (kwa kutumia barakoa). Kwa mfano, "192.168.0.0/24" ni "tafsiri" ya nukuu ya mask ya desimali "255.255.255.0".



Ili kutumia Nmap kwa kubainisha CIDR, tunaweza kuitumia kama ifuatavyo:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Pia inawezekana, kama ilivyo kwa milango katika sehemu iliyotangulia, kubainisha wapangishi wengi, mitandao mingi, au masafa:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Huu hapa ni mfano wa matokeo ambayo tunaweza kupata tunapochanganua kwenye mtandao:



![nmap-image](assets/fr/26.webp)



matokeo ya uchunguzi wa Nmap ili kuweka mitandao kadhaa ramani



Hasa, tunaona majeshi kadhaa yanayofanya kazi, na kila sehemu ya mwenyeji huanza na mstari kama huu:



```
Nmap scan report for <name> (<IP>)
```



Hii inaturuhusu kuona kwa uwazi ni mwenyeji gani matokeo yafuatayo yanarejelea. Mstari wa mwisho pia ni muhimu:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Tunajua kwamba, kwenye mitandao iliyochanganuliwa, Nmap iligundua wapangishi 5 amilifu.



#### B. Chini ya kofia: uchambuzi wa mtandao kupitia Wireshark



Sasa tutaangalia kwa karibu kile kinachotokea katika kiwango cha mtandao wakati wa ugunduzi wa mtandao uliofanywa kupitia Nmap.



Kama tulivyoona katika sehemu iliyotangulia, kwa chaguo-msingi Nmap itatumia itifaki ya ARP kugundua kuwepo kwa wapangishi kwenye mtandao wa ndani:



![nmap-image](assets/fr/27.webp)



aRP pakiti zilizonaswa wakati wa kuchanganua mtandao wa ndani kwa kutumia Nmap na chaguo-msingi zake



Kwa hivyo inaweza kugundua karibu wapangishi wote kwenye mtandao wa ndani, kwa kuwa jibu la ombi la ARP kwa ujumla hutolewa na wapangishi wote wanaofanya kazi kwenye mtandao na halionekani kuwa ya kutiliwa shaka kwa njia yoyote.



Kwa mitandao ya mbali, Nmap hutumia mchanganyiko wa mbinu:



![nmap-image](assets/fr/28.webp)



Pakiti za iCMP na TCP zilizonaswa wakati wa kuchanganua mtandao wa mbali kwa kutumia Nmap na chaguo-msingi zake



Ili kuwa sahihi zaidi, Nmap hutumia pakiti ya mwangwi ya ICMP (kesi ya kawaida ya pinging) na pakiti ya ICMP Timestamp, ambayo kawaida hutumika kukokotoa nyakati za usafiri wa pakiti. Inatumai kupata jibu kutoka kwa wapangishaji kwenye mitandao ya mbali.



Lakini kuna zaidi ya hilo. Unaweza kuona kwenye picha ya Wireshark hapo juu kwamba vifurushi vya **TCP SYN** hutumwa kwa utaratibu kwenye bandari za TCP/443 za kila seva pangishi kwenye mitandao itakayochanganuliwa, pamoja na pakiti za **TCP ACK** kwenye mlango wa TCP/80.



**Kwa nini utume pakiti za TCP kwenye bandari kama sehemu ya ugunduzi wa mtandao?



Kutuma pakiti ya SYN kwenye mlango fulani huruhusu Nmap **kuamua ikiwa huduma inasikilizwa kwenye mlango huo**. Ikiwa seva pangishi itajibu pakiti ya SYN yenye pakiti ya SYN/ACK, hii inaonyesha kuwa inatumika na kwamba huduma inasikilizwa kwenye mlango huo. Nmap kwa hivyo inajaribu bahati yake kwenye huduma hii, **hata kama hakuna jibu la ping limepatikana**.



Kutuma kifurushi cha ACK kwenye mlango fulani huruhusu Nmap **kuamua ikiwa ngome iko kwenye seva pangishi hiyo**. Ikiwa seva pangishi itajibu pakiti ya ACK iliyo na pakiti ya RST (Weka Upya), hii inaonyesha kuwa ngome-mtandao huenda iko kwenye seva pangishi hiyo na inazuia trafiki isiyoombwa. Kwa hivyo mwenyeji husaliti uwepo wake kwenye mtandao, hata ikiwa haijajibu maombi mengine.



Ni muhimu kutambua, hata hivyo, kwamba utambuzi wa firewall kwa kutumia mbinu hii hauwezi kuaminika kikamilifu katika matukio yote. Baadhi ya wapangishi wanaweza kujibu generate RST kwa sababu zingine isipokuwa uwepo wa ngome, kama vile huduma mahususi au usanidi wa mfumo wa uendeshaji. Kwa kuongeza, firewalls za kisasa zinaweza kusanidiwa kutojibu majaribio ya ugunduzi wa aina hii.



Sasa tumetoka mbali na tunaweza kutekeleza ugunduzi wa kimsingi wa mtandao. Sasa tutaangalia chaguo chache zaidi ambazo zitatupa udhibiti mkubwa wa tabia ya Nmap.



### III. Ugunduzi wa mtandao bila kukagua mlango kwa kutumia Nmap



Kama unavyoweza kuwa umeona, kwa chaguo-msingi Nmap **hufanya uchanganuzi wa mlango baada ya ugunduzi wake wa seva pangishi amilifu**, ambayo huongeza idadi kubwa ya pakiti na kusubiri majibu kwa uchanganuzi wetu. Ikiwa una wapangishi 5 kwenye mtandao wako, Nmap itajaribu kuangalia hali ya karibu bandari 5,000, ambayo itachukua muda mrefu zaidi.



Hata hivyo, inawezekana kutumia chaguo za Nmap kufanya **ugunduzi pekee wa wapangishi amilifu** kwenye mtandao, bila kugundua huduma zao.



Iwapo tunataka tu kujua ni seva pangishi zinazoweza kufikiwa, bila taarifa yoyote kuhusu huduma na milango inayofichua, basi tunaweza kutumia chaguo la "-sn" kutekeleza **changanuzi pekee kwa kutumia ICMP Echo (ping) na maombi ya ARP**. Kwa maneno mengine, zima utambazaji wa bandari kabisa:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Hapa kuna matokeo ya ugunduzi wa mtandao wa Nmap uliofanywa bila skanning ya bandari:



![nmap-image](assets/fr/29.webp)



Matokeo ya ugunduzi wa mtandao bila kukagua mlango kwa kutumia Nmap.



Tayari tumetaja vikwazo vinavyowezekana vya kutumia ICMP pekee kwa ugunduzi wa mwenyeji (kwa mitandao ya mbali). Ndiyo maana Nmap pia hutumia hila chache ambazo zinaweza kusaliti uwepo wa ngome au huduma mahususi kwa wapangishaji. Kwa usaidizi wa chaguo, tunaweza kutumia tena mbinu hizi na hata kuzipanua, bila kulazimika kuanza tena na uchunguzi kamili wa mlango wa kila seva pangishi iliyogunduliwa.



Ili kufanya hivyo, tutatumia chaguo za "-PS" (TCP SYN) na "-PA" (TCP ACK), ambazo zitaturuhusu kubainisha bandari tunazotaka kujiunga nazo kama sehemu ya ugunduzi wetu wa mwenyeji, pamoja na chaguo la "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Uchanganuzi huu tayari unahakikisha kuwa ugunduzi wa seva pangishi ni kamili zaidi kuliko kwa chaguo-msingi.



Tunaanza kupata amri za kina kabisa, kwa kutumia chaguo nyingi. Hii ni kwa sababu tunajua jinsi Nmap inavyofanya kazi na vikwazo vya chaguo zake "chaguo-msingi", ambazo wakati mwingine zinaweza kutufanya tupoteze muda au kukosa Elements muhimu. Hiyo ndiyo hatua nzima ya kuchukua wakati kuisimamia!



Kwa undani chaguzi za agizo letu la mwisho:





- "`-sn`: huzima utambazaji mlangoni kwa kila seva pangishi amilifu iliyogunduliwa na Nmap.





- "`-PP`: huwezesha mwangwi wa ICMP (ping scan) kwa ugunduzi wa mwenyeji.





- "`-PS <PORT>`": tuma kifurushi cha TCP SYN kwenye lango/milango iliyoonyeshwa ili kugundua huduma yoyote inayoendelea inayosaliti uwepo wa seva pangishi ambayo haijajibu ping.





- "`-PA <PORT>`": tuma pakiti ya TCP ACK kwenye lango (za) iliyoashiriwa ili kugundua ngomemote inayofanya kazi inayosaliti uwepo wa seva pangishi ambayo haijajibu ping.




Katika mfano hapo juu, ninataja bandari ninazozingatia kuwa zinazofichuliwa mara kwa mara katika muktadha wangu wa Nmap kwa chaguo la "-PS". Lango hizi tofauti zitajaribiwa kwa kila seva pangishi, si ili kuona kama huduma anayopangisha inatumika kweli, lakini ili kuona ikiwa hii inaruhusu sisi kugundua seva pangishi ambayo haijajibu ICMP Echo yetu wakati ingali inatumika (kupitia jibu kutoka kwa huduma au ngome ya mwenyeji).



Hivi ndivyo inavyoweza kuonekana katika kunasa mtandao iliyochukuliwa wakati wa kuchanganua vile, katika kesi hii dondoo kwenye seva pangishi inayolengwa:



![nmap-image](assets/fr/30.webp)



vifurushi vilivyotumwa na Nmap wakati wa ugunduzi wa hali ya juu wa mtandao, bila skanning mlangoni



Tunapata pakiti zetu za TCP SYN, TCP ACK yetu kwenye bandari TCP/80 na mwangwi wetu wa ICMP. Nmap itafanya majaribio haya yote kwa kila seva pangishi inayolengwa na ugunduzi wetu wa mtandao.



### IV. Kutumia faili ya mali kulenga na Nmap



Kubainisha malengo kunaweza kuthibitisha kwa haraka kuwa changamano katika mifumo ya taarifa ya maisha halisi, ambayo wakati mwingine inaweza kujumuisha dazeni au mamia ya mitandao, subneti na VLAN. Hii ndio sababu ni rahisi kutumia faili kama chanzo cha Nmap kuliko kuzitaja moja baada ya nyingine kwenye safu ya amri.



Kuanza, tengeneza faili rahisi iliyo na kiingilio kimoja kwa kila mstari:



![nmap-image](assets/fr/31.webp)



faili iliyo na lengo moja (mwenyeji au mtandao) kwa kila mstari



Ifuatayo, tunaweza kutumia chaguo zote za Nmap zinazoonekana kufikia sasa na kubainisha chaguo la "-iL <path/file>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap basi itajumuisha katika uchanganuzi wake shabaha zote zilizomo kwenye faili yetu.



Ikiwa unataka kuwa na uhakika kwamba malengo yako yote yatazingatiwa, unaweza kutumia chaguo la "-sL -n". Nmap basi itafasiri CIDR na seva pangishi kwenye faili na kukuonyesha, bila kutuma pakiti zozote kwenye mtandao:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Hii inahakikisha kuwa orodha ya seva pangishi zitakazochanganuliwa ni sahihi.



Kidokezo kimoja muhimu cha mwisho ningependa kushiriki nawe masuala **mwenyeji au kutengwa kwa mtandao kama sehemu ya uchanganuzi**. Hitaji hili la kuwatenga seva pangishi linaweza kuwa muhimu katika matukio kadhaa, hasa ikiwa tunataka kuwa na uhakika kwamba **kipengele nyeti cha mfumo wa taarifa hakijakatizwa au kukatizwa na utafutaji wetu**.



Mifano ya mara kwa mara ya mahitaji hayo ni wakati kampuni inamiliki viwanda (PLC) au vifaa vya afya. Vifaa vile wakati mwingine hutengenezwa vibaya, na sio lengo la kupokea pakiti zilizopangwa vibaya, au nyingi sana. Kwa sababu za wazi za kupatikana au hatari ya biashara/binadamu, ni vyema kuwatenga kwenye majaribio.



Ili kutenga anwani za IP au mitandao kutoka kwa skana yetu, tunaweza kutumia chaguo la "--exclude" la Nmap, kwa mfano:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



Katika mfano huu, ninachanganua mtandao "192.168.1.0/24" lakini bila kujumuisha mwenyeji "192.168.1.140" iliyoko hapo. Hakuna pakiti zitatumwa na Nmap kwa mpangishi huyu. Mfano mwingine na kutengwa kwa subnet:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Vile vile, mimi huchambua mtandao mkubwa "10.0.0.0/16", lakini mtandao "10.0.100.0/24" hautapigwa. Tena, ninapendekeza kutumia chaguo la "-sL -n" ili kupata mtazamo wazi sana wa majeshi ambayo yatachanganuliwa na ambayo yataondolewa kwenye skanisho, hasa ikiwa unafanya kazi katika muktadha nyeti.



### V. Ugunduzi wa mtandao na utambazaji mlangoni



Sasa tunaweza kuchanganya yale ambayo tumejifunza katika sehemu hii na yale tuliyojifunza katika sehemu iliyotangulia kuhusu chaguo za skanisho la mlango. Kwa chaguo-msingi, tumeona kuwa Nmap itachanganua milango 1000 ya mara kwa mara kwenye kila seva pangishi inayotumika itakayogundua. Tumeona jinsi ya kuzuia tabia hii ikiwa hatuitaki, lakini tunaweza kuidhibiti kikamilifu, na hata kuipanua ikiwa inafaa mahitaji yetu.



Kwa mfano, amri ifuatayo itaangalia uwepo wa huduma ya kusikiliza kwenye bandari TCP/22 kwenye kila seva pangishi iliyochanganuliwa:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap itafanya ugunduzi wa mtandao kwanza ili kuorodhesha wapangishi wanaotumika, na kwa kila mmoja wao, hakikisha kuwa kuna huduma kwenye bandari TCP/22.



Kwa njia hiyo hiyo, tunaweza kufanya uchanganuzi kamili wa bandari zote za TCP kwa kila seva pangishi iliyogunduliwa kwenye mtandao wa "192.168.0.0/24", bila kujumuisha seva pangishi "192.168.0.4" kwa mfano:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Uko huru kuchanganya chaguo zote ambazo tumejifunza kufikia sasa ili kukidhi mahitaji yako mwenyewe.



### VI. Hitimisho



Katika sehemu hii, tumeona jinsi ya kutumia Nmap kuweka ramani ya mtandao kwa kutumia chaguo mbalimbali. Sasa tuna uelewa mzuri wa shabaha za skanisho zetu, pamoja na tabia ya ukaguzi wa mlango wa Nmap na mbinu ya kugundua seva pangishi. Na muhimu zaidi, tunajua tabia na vikwazo vya Nmap ni nini, na jinsi ya kutumia chaguo zake kuu kwenda mbali zaidi.



Katika sehemu inayofuata, tutaangalia taratibu na chaguo za kugundua matoleo ya huduma na mifumo ya uendeshaji iliyochanganuliwa na Nmap.




## 6 - Kugundua matoleo ya huduma na mfumo wa uendeshaji kwa kutumia Nmap



### I. Uwasilishaji



Katika sehemu hii, tutajifunza jinsi ya kutumia Nmap kugundua na kugundua kwa usahihi matoleo ya huduma na mifumo ya uendeshaji inayotumiwa na wapangishi waliochanganuliwa. Tutaangalia kwa kina jinsi Nmap hutimiza kazi hii, na pia katika mapungufu ya zana ili kuelewa na kutafsiri vyema matokeo yake.



Kama tulivyoona katika sehemu zilizopita za mafunzo haya, kwa chaguo-msingi, Nmap haitaangalia ni huduma gani inayofichuliwa kwenye milango inayochanganua na kufikiria kuwa imefunguliwa. Kwa hivyo ikiwa unasikiliza huduma ya wavuti kwenye bandari TCP/22, Nmap itaendelea kuripoti kuwa imefunguliwa, lakini kama huduma ya `SSH`. Hii ni kwa sababu hutumia [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) kwenye mfumo wako kutafuta uhusiano kati ya bandari/itifaki na jina la huduma (faili ya `/etc/services/`).



Katika hali nyingi, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) itakupa taarifa sahihi, kwa kuwa ni nadra katika mazingira ya uzalishaji kupata visa kama hivyo. Hata hivyo, hali zilizosalia zitakuwa hali ambapo huduma ya kawaida ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, n.k.) itafichuliwa kwenye lango lisilo la kawaida (k.m. 2022 kwa huduma ya SSH), katika hali ambayo Nmap haitapata inayolingana katika hifadhidata yake ya karibu, haitalingana na uhalisia ulio karibu nawe, au itakosa uhalisia mmoja.



Kwa bahati nzuri, Nmap inatoa chaguo na mbinu sahihi sana za kugundua ni huduma gani hasa inaweza kuwa imejificha nyuma ya mlango wazi. Hata ina hifadhidata ya maswali na saini ili kutambua teknolojia na matoleo halisi. Mbali na huduma, Nmap pia inaweza kutambua teknolojia inayotumiwa na toleo lake.



Hiyo ndiyo tutakuwa tukiangalia katika sehemu hii.



### II. Jinsi ya kugundua teknolojia au toleo



#### A. Kikumbusho cha jinsi ya kutambua teknolojia au toleo



Kutambua teknolojia na toleo kunahusisha kurejesha jina la huduma, CMS, programu au usikilizaji wa programu kwenye mlango unaolengwa. Kwa mfano, ukurasa wa wavuti unasimamiwa na CMS (`WordPress`), inayoendeshwa na huduma ya wavuti (`Apache`, IIS, Nginx) na kupangishwa na seva (Linux au Windows). Lakini unajuaje ni huduma gani ya wavuti inayoendesha?



Mbinu ya kitamaduni ya kupata habari hii ni _banner grabbing_, ambayo inajumuisha kupata mahali ambapo huduma inayohusika inaonyesha habari hii na kusoma data. Mara nyingi sana, katika usanidi au uchakataji wao chaguomsingi, huduma huonyesha jina lao na hata toleo lao kama jibu la kwanza baada ya muunganisho.



![nmap-image](assets/fr/32.webp)



onyesha toleo mara tu muunganisho wa TCP unapoanzishwa na huduma ya FTP



Hapa tunaona kwamba muunganisho rahisi wa TCP kwa huduma hii kupitia `telnet` husababisha pakiti ya TCP iliyo na teknolojia na toleo lake.



Mara tu unapopata wazo la aina ya huduma unayoshughulika nayo, unaweza pia kutuma amri au maombi mahususi kwa huduma hiyo ili kutoa taarifa kutoka kwayo. Maombi/amri hizi pia zinaweza kutumwa kwa upofu (bila kuwa na uhakika kuwa ni aina sahihi ya huduma), kwa matumaini kwamba mojawapo itachochea majibu kutoka kwa huduma inayohusika.



Katika hali zingine, za hali ya juu zaidi, inahitajika kutuma pakiti maalum ili kusababisha athari, kama vile hitilafu, ambayo itatoa maelezo ya kina juu ya toleo au teknolojia iliyotumiwa.



Kama unavyoweza kufikiria, Nmap itatumia mbinu hizi zote kujaribu na kutambua aina halisi ya huduma inayopangishwa kwenye bandari, pamoja na jina la teknolojia na toleo lake.



#### B. Kuelewa Majaribio na Mechi za Nmap



Ili kutekeleza ukaguzi huu wote kwenye kila bandari iliyochanganuliwa, Nmap hutumia hifadhidata ya ndani ambayo husasishwa mara kwa mara (kama vile mfumo wa jozi au moduli zake). Hili ni faili la maandishi la mistari elfu kadhaa: `/usr/share/nmap/nmap-service-probes`.



Faili hii ina maingizo mengi, yote yamepangwa kwa miongozo miwili mikuu:





- `Probe`: huu ndio ufafanuzi wa pakiti ambayo Nmap itatuma katika jaribio la kuibua hisia kutoka kwa huduma ili kutambuliwa. Fikiria kama jaribio la kipofu kama _Hello? Lebo ya Guten? Hujambo? Um... Buenos Dias labda?_. Mara tu huduma inayolengwa inapopokea uchunguzi inaelewa (yaani kuzungumza itifaki sahihi), itajibu Nmap, ambayo itakuwa na uthibitisho wa aina ya huduma hiyo.





- Mechi": haya ni matamshi ya kawaida ambayo Nmap hutumika kwa jibu lililopatikana. Ikiwa kutuma ombi la HTTP GET kumesababisha jibu kutoka kwa huduma, itatumia misemo mingi ya kawaida kwa jibu hili ili kutambua uwepo wa, kwa mfano, neno `Apache`, `Nginx`, `Microsoft IIS`, n.k.




Kuna maagizo mengine machache kwa kesi maalum, lakini yale kuu ya kuelewa jinsi Nmap inavyofanya kazi na kubinafsisha matumizi yake ni haya. Ili kufanya nadharia hii kuwa sehemu thabiti zaidi, hapa kuna mfano:



![nmap-image](assets/fr/33.webp)



mfano wa Uchunguzi katika faili ya `/usr/share/nmap/nmap-service-probes` ya Nmap



Katika mstari wa kwanza wa mfano huu, tunaona Uchunguzi ulio rahisi kuelewa unaoitwa `GetRequest`. Hiki ni kifurushi cha TCP kilicho na ombi tupu la HTTP GET kwa mzizi wa huduma ya wavuti kwa kutumia HTTP/1.0, ikifuatiwa na mlisho wa laini na laini tupu.



Laini ya `bandari` inaiambia Nmap ni mlango gani wa kutuma Uchunguzi huu. Hii hukuruhusu kutanguliza majaribio na kuokoa muda.



Hatimaye, tuna mifano miwili ya `mechi`. Ya kwanza, kwa mfano, itaainisha huduma ya wavuti iliyochanganuliwa kuwa `ajp13` ikiwa usemi wa kawaida ulio katika mstari huu unalingana na jibu la huduma lililopokelewa.



Ili kukusaidia kuelewa jinsi Probes zinaweza kuonekana, hii hapa ni orodha ya baadhi ya Majaribio utakayopata kwenye faili hii (kuna 188 kwa jumla wakati wa kuandika mafunzo haya).



![nmap-image](assets/fr/34.webp)



mfano wa Uchunguzi kadhaa unaotumiwa na Nmap na uliopo kwenye faili `/usr/share/nmap/nmap-service-probes`._



Mbili za kwanza (zinazoitwa `NULL` na `GenericLines`) zinavutia sana hapa, kwani zinatuma tu pakiti tupu ya TCP au iliyo na kivunja mstari. Huduma za seva mara nyingi hujitangaza kwa usahihi punde tu muunganisho unapopokelewa, bila hatua yoyote maalum, amri au ombi kutoka kwa mteja.



Hapa kuna kesi ya _match_ ngumu zaidi:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Usemi kamili wa kawaida unapatikana hapa kati ya `m|` na `|`, ambayo inaweka mipaka ya usemi wowote wa kawaida katika faili hili. Tafadhali chukua muda kusoma mfano huu wote. Utagundua uteuzi katika usemi wa kawaida: `([\d.]+)`, unaotumika kutenga toleo. Mfano huu pia unafafanua Elements nyingine kama vile jina la bidhaa `p/nginx/`, toleo lililorejeshwa `v/$1/` na CPE yenye toleo `cpe:/a:igor_sysoev:nginx:$1/`.



CPE (Kuhesabu kwa Mfumo wa Kawaida) ni mfumo sanifu wa uandishi unaotumiwa kutambua na kuelezea programu na maunzi. Muundo huu huwezesha usimamizi bora zaidi wa udhaifu na usanidi wa usalama, na zaidi ya yote njia iliyounganishwa ya kuziwakilisha, bila kujali bidhaa inayohusika. Hapa kuna mifano miwili ya CPE: `cpe:/o:microsoft:windows_8.1:r1` na `cpe:/a:apache:http_server:2.4.35`



Hapa tunabainisha kwa uwazi aina zao `o` kwa Mfumo wa Uendeshaji, `a` kwa programu, mchuuzi, bidhaa na matoleo.



Kwa hivyo, katika tukio la _match_ na mojawapo ya vielezi hivi vya kawaida, tutapata sio tu jina la huduma, lakini pia toleo lake na CPE halisi, ili kurahisisha kupata CVE zinazoathiri toleo hili. Utapata habari hii katika matokeo ya kawaida ya Nmap, na utaona kuwa ni muhimu sana kwa madhumuni mengine ambayo tutashughulikia katika sehemu chache.



Sintaksia halisi ya _matches_ na, kwa ujumla zaidi, ya maagizo katika faili ya `/usr/share/nmap/nmap-service-probes` haishii hapo, na inaweza kuonekana kuwa changamano ikiwa hujazoea kuendesha Nmap na matokeo yake. Hata hivyo, unapaswa kukumbuka kuwepo kwake na utendakazi wa jumla, ambao utakusaidia baadaye unapotaka kuelewa au kutatua matokeo, kubinafsisha uchanganuzi au hata kuchangia katika ukuzaji wa Nmap.



### III. Kutumia Nmap kugundua matoleo



Sasa tutatumia _Probe_ na _Match_ mechanics hii yote changamano kupitia chaguo rahisi: `-sV`. Hii inaambia Nmap tu: jaribu kujua ni huduma zipi na matoleo ya bandari ambayo umeweka wazi.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Hapa kuna mfano kamili wa matokeo ya amri kama hii:



![nmap-image](assets/fr/35.webp)



matokeo ya ugunduzi wa toleo la Nmap la programu zilizofichuliwa kwenye mtandao



Hapa tunaweza kuona kwamba Nmap imeweza kutambua matoleo yote ya huduma za mtandao zilizofichuliwa na lengo hili, na kuonyesha maelezo haya katika safu mpya ya `VERSION`. Inawezekana kuona habari sahihi kabisa, hata chini ya mfumo wa uendeshaji, ikiwa habari hii ni sehemu ya saini iliyorejeshwa.



Ili kuelewa kwa undani kile kinachotokea wakati wa kuchanganua uwezekano wa kuathiriwa, tunaweza kutumia chaguo la `--version-trace`. Hii itatoa mwonekano wa hali ya utatuzi, kuonyesha _Probe_ ambayo ilisababisha ugunduzi:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Kwa hivyo, tutakuwa na habari nyingi za kutatua. Jaribu kutambua mistari inayoanza na `Service Scan Hard match`. Kisha utaona mistari kama hii:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Tunaweza kuona kwa uwazi ni _Probes_ gani zilitumika kugundua teknolojia na toleo (katika kesi hii `NULL` na `GetRequest` _Probes_), pamoja na maelezo yaliyopatikana.



### IV. Kudhibiti vipimo na usahihi wa utambuzi



Sasa tutarudi kwenye maagizo katika faili ya `/usr/share/nmap/nmap-service-probes` ambayo hatukuiangalia hapo awali:



![nmap-image](assets/fr/36.webp)



inachunguza maelekezo ya `rarity` katika faili ya `/usr/share/nmap/nmap-service-probes`._



Maagizo haya yanatumika kuonyesha upungufu (yaani kipaumbele/uwezekano) unaohusishwa na _Probe_. Dokezo hili kutoka 1 hadi 9 hukuruhusu kudhibiti ukamilifu wa uchanganuzi unaofanywa na Nmap wakati wa kutuma _Probes_. Katika mfumo wa "notation" wa Nmap, nadra ya 1 hutoa taarifa katika idadi kubwa ya matukio, ambapo nadra ya 8 au 9 inawakilisha kesi maalum sana, maalum kwa usanidi au huduma ambayo haipatikani sana.



Ili kuwa wazi zaidi, katika hali chaguo-msingi, Nmap itatuma kwa kila huduma ili kutambuliwa _Probes_ ambazo zina nadra kutoka 1 hadi 7. Ili kukupa wazo bora la usambazaji wa _Probes_ kwa _rarity_, hii ndiyo hesabu yao:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Inaweza kuonekana kuwa isiyoeleweka, kuna `adimu` zaidi ya 8 na 9 kuliko zingine. Hii ni hasa kwa sababu Rarity 1 Probes ni za kawaida na hufanya kazi katika hali nyingi, bila kujali huduma (kumbuka `NULL` Probe ambayo hutuma pakiti tupu ya TCP). Ingawa Majaribio changamano zaidi yanakaribia kuwa ya kipekee kwa kila huduma.



Iwapo tunataka kudhibiti Maswali tunayotaka kutumia katika uchanganuzi wa toleo letu, tunaweza kutumia chaguo la `--version-intensity`. Hapa kuna mifano miwili:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Ili kumaliza kuhusu somo hili, hapa kuna mfano wa _Probe_ 9 na 8:



![nmap-image](assets/fr/37.webp)



mifano ya Uchunguzi kwa nadra 8 na 9 katika faili `/usr/share/nmap/nmap-service-probes`._



_Probes_ hizi mbili hugundua seva za Quake1 na Quake2 (mchezo wa video). Kuvutia kwa upande wa nostalgic, lakini hakuna uwezekano wa kuwa na matumizi mengi katika maisha ya kila siku.



Kulingana na mahitaji yako ya usahihi au kasi, kumbuka kuwa kanuni hii ya `rarity` ipo na inaweza kuathiri matokeo.



### V. Kutumia Nmap kugundua mifumo ya uendeshaji



Sasa tutaangalia jinsi Nmap inaweza kutusaidia kugundua mifumo ya uendeshaji ya seva pangishi iliyochanganuliwa na kutambuliwa kwenye mtandao. Ili kufanya hivyo, tumia chaguo la Nmap `-O` (kwa `OS Scan`) chaguo.



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Hapa kuna mfano wa matokeo. Hapa, Nmap inatuambia labda ni Mfumo wa Uendeshaji wa Linux, na inatupa takwimu mbalimbali kuhusu toleo lake halisi.



![nmap-image](assets/fr/38.webp)



ugunduzi wa uwezekano wa kutambuliwa kwa mfumo wa uendeshaji na Nmap



Ili kufanikisha hili, Nmap itatumia mbinu nyingi zinazofanya kazi kwa njia sawa na _Probes_ na _Matches_ kwa ajili ya kutambua teknolojia na matoleo. Tofauti kuu ni kwamba Nmap itatumia vigezo vya "kiwango cha chini" vya ICMP, TCP, UDP na itifaki zingine. Hapa kuna mifano miwili ya majaribio ya kugundua mfumo wa uendeshaji wa Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



mifano ya majaribio yaliyofanywa na Nmap kugundua OS ya Windows 11



Hebu tukubaliane nayo, majaribio haya ni magumu sana kutafsiri, na hatutajaribu kuyaelewa kwa kina katika muktadha wa mafunzo ya utangulizi ya Nmap. Ikiwa ungependa kuchimba zaidi katika mada, faili iliyo na maelezo haya ni `/usr/share/nmap/nmap-os-db`.



Walakini, unahitaji kufahamu kuwa ugunduzi wa OS ni uwezekano ulioanzishwa na Nmap kuliko uhakika.



### VI. Hitimisho



Katika sehemu hii, tumejifunza jinsi ya kutumia chaguo za Nmap ili kugundua teknolojia, matoleo na mifumo ya uendeshaji ya seva pangishi na huduma zilizochanganuliwa. Sasa tuna ufahamu mzuri wa jinsi Nmap inavyoendelea kupata habari hii kwa mbali. Tumekagua pia chaguo za kudhibiti kitenzi na usahihi wa majaribio, pamoja na mapungufu ya zana kwenye mada haya.



Katika sehemu inayofuata, tutajifunza jinsi ya kutumia hati za NSE za Nmap kufanya uchanganuzi wa usalama wa mfumo wetu wa habari. Chukua wakati wa kusoma tena sehemu za mwisho ikiwa unahitaji, na usisite kufanya mazoezi na kuzama ndani ya chombo mwenyewe ili kufahamu vyema yale ambayo tumejifunza kufikia sasa.




## 7 - Uchambuzi wa usalama: kugundua udhaifu



### I. Uwasilishaji



Katika sehemu hii, tutajifunza jinsi ya kutumia zana ya kuchanganua mtandao wa Nmap ili kugundua na kuchanganua udhaifu kwenye malengo ya utafutaji wetu. Hasa, tutaangalia chaguo mbalimbali zinazopatikana ili kukamilisha kazi hii, na kujifunza mipaka ya uwezo wa chombo ili kuelewa vizuri na kutafsiri matokeo yake.



Katika sehemu hii ya kwanza, tutaangalia kichanganuzi cha uwezekano wa Nmap, na kuona jinsi ya kutumia chaguo msingi za kutambua uwezekano. Katika sehemu zifuatazo, tutaangalia kwa undani jinsi kipengele hiki kinavyofanya kazi, na jinsi kinaweza kubinafsishwa.



### II. Kutumia Nmap kugundua udhaifu



Sasa tunataka kutumia kichanganuzi cha mtandao cha Nmap ili kugundua udhaifu katika huduma na mifumo ya mfumo wetu wa taarifa. Hii inamaanisha kuwa pamoja na kugundua seva pangishi zinazoendelea, kuorodhesha huduma zilizofichuliwa na kugundua matoleo na teknolojia, Nmap itatafuta udhaifu.



Ili kufanikisha hili, Nmap inategemea hati za NSE (_Nmap Scripting Engine_), ambazo zinaweza kuonekana kama moduli zinazowezesha mbinu ya majaribio.



Kwa chaguo sahihi, tutaiuliza Nmap kutumia hati zake mbalimbali za NSE kwenye kila huduma iliyogunduliwa, na kutuwezesha kugundua:





- Makosa ya usanidi;





- Toleo la ziada na la juu zaidi na uvumbuzi wa OS;





- Udhaifu unaojulikana (CVEs) ;





- Vitambulisho dhaifu;





- Tabia ya Elements ya maambukizi ya programu hasidi;





- Kunyimwa uwezekano wa huduma;





- Nk.




Kama unavyoona, hati za NSE huongeza kwa kiasi kikubwa uwezo wa Nmap kulingana na shughuli za mtandao inazoweza kufanya. Na hii kufanya kazi za juu zaidi kuliko hapo awali. Habari njema ni kwamba, kama kawaida, vipengele hivi vinaweza kutumika kupitia chaguo na katika muktadha chaguo-msingi. Hivi ndivyo tutakavyoona baadaye.



### III. Mfano wa skanning ya mazingira magumu



Hati za NSE zinaweza kutumika unapotumia Nmap kuchanganua mlango mmoja kwenye seva pangishi, huduma zote kwenye seva pangishi hiyo au huduma zote zinazotambuliwa kwenye mitandao kadhaa. Kwa hivyo tunaweza kutumia chaguzi ambazo tutaona katika miktadha yote ambayo tumesoma hadi sasa.



Ili kuwezesha uchanganuzi wa uwezekano wa kuathiriwa kupitia uchanganuzi wa Nmap, tunahitaji kutumia chaguo la `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Kumbuka kwamba kwa chaguo-msingi, ikiwa hutabainisha chochote, Nmap itachanganua tu bandari 1000 zinazojulikana zaidi. Haitatambua udhaifu kwenye milango ya kigeni ambayo malengo yako yanaweza kufichua.



Kabla ya kutumia utendakazi huu kwenye mfumo wa taarifa za uzalishaji, ninakualika uendelee kusoma mafunzo. Katika sehemu zifuatazo, tutaangalia jinsi ya kudhibiti vyema athari na aina za majaribio yatakayoendeshwa.



Kwa kutumia tena yale ambayo tumejifunza hapo awali, tunaweza, kwa mfano, kuwa wa kina zaidi na kuchanganua bandari zote za TCP za lengo:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Hapa kuna matokeo ya skanisho ya Nmap kwa kutumia hati za NSE:



![nmap-image](assets/fr/40.webp)



mfano wa matokeo ya uchanganuzi wa uwezekano wa kuathirika kwa mwenyeji kupitia Nmap._



Hapa tunaona onyesho la maelezo ya ziada ya kuvutia katika muktadha wa uchanganuzi wa uwezekano:





- Huduma ya FTP inaweza kufikiwa bila kujulikana, na haijalindwa na uthibitishaji. Hati ya NSE inayosimamia uthibitishaji huu inatuambia hivyo, na hata inaonyesha sehemu ya muundo wa mti wa huduma ya FTP. Hapa tunaona kwamba tunaweza kufikia saraka ya `C` ya mfumo wa Windows!





- Hati ya NSE inayosimamia urejeshaji wa huduma ya wavuti ya hali ya juu inaonyesha kichwa cha ukurasa, ikitupa wazo bora la huduma ya wavuti inapangisha nini.





- Pia tuna uchanganuzi mdogo wa usanidi wa huduma ya SMB (hati `smb2-time`, `smb-security-mode` na `smb2-security-mode`). Taarifa inaonyeshwa tofauti kidogo, baada ya matokeo ya skanning ya mtandao, ili iwe rahisi kusoma. Hasa, habari hii inaonyesha kutokuwepo kwa saini za SMB Exchange. Udhaifu huu wa usanidi huruhusu lengo kutumika katika shambulio la Relay ya SMB, dosari kubwa ya usalama ambayo mara nyingi hutumiwa katika majaribio ya uvamizi/uvamizi wa mtandaoni.




Bila shaka, huu ni mfano mmoja tu. Nmap ina hati za NSE kwa huduma nyingi, zinazolenga udhaifu mbalimbali. Tutaangalia kwa karibu uwezekano huu katika sehemu inayofuata.



Ili kuhitimisha utangulizi huu wa uchanganuzi wa hatari, hapa kuna amri kamili ya ugunduzi wa mtandao, uchunguzi wa mlango wa TCP, ugunduzi wa toleo na uwezekano:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Hapa kuna amri ambayo inaanza kuonekana kama kesi za utumiaji za Nmap za kweli!



### IV. Kuelewa mapungufu ya Nmap katika uchanganuzi wa mazingira magumu



Hebu tuseme wazi: Nmap haina uwezo wa kufanya jaribio kamili la kupenya la mfumo wako wa taarifa, au kuiga operesheni ya Timu Nyekundu. Ina vikwazo kadhaa ambavyo unahitaji kufahamu ikiwa hutakiwi kuwa na hisia za uwongo za usalama:





- Ufikiaji mdogo**: ingawa hati za Nmap za NSE zina nguvu, ufikiaji wao wa majaribio unaweza kuwa mdogo ikilinganishwa na zana zingine maalum za kugundua athari. Baadhi ya udhaifu hauwezi kufunikwa na hati za NSE zinazopatikana, kama vile udhaifu wa Active Directory, kufichua data nyeti au matukio ya kina zaidi ya programu za wavuti zinazoweza kuathirika.





- Utata wa mazingira magumu**: aina fulani za athari zinaweza kuwa vigumu kutambua kwa kutumia hati za NSE kutokana na uchangamano wake. Kwa mfano, udhaifu unaohitaji mwingiliano changamano na huduma ya mbali hauwezi kutambuliwa vyema na Nmap (kama ilivyo kwa ruhusa nyingi katika kushiriki faili au dosari ya udhibiti wa ruhusa katika programu ya wavuti).





- Ugunduzi wa hali tuli**: Nmap inaangazia uchanganuzi unaoendelea ili kugundua udhaifu, kumaanisha kuwa inaweza isitambue kwa njia inayofaa uwezekano wa udhaifu bila kuanzisha muunganisho unaotumika na wapangishi lengwa. Udhaifu ambao haujidhihirishi wakati wa uchanganuzi unaoendelea unaweza kukosa (kama ilivyo kwa udungaji wa msimbo kwenye programu ya wavuti).





- Utegemezi wa masasisho**: [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) ya hati za NSE inaendelea kubadilika, lakini kunaweza kuwa na kuchelewa kati ya ugunduzi wa athari mpya na kuongezwa kwa hati inayolingana na Nmap. Kwa hivyo, Nmap huenda isisasishwe kila wakati na udhaifu wa hivi punde.





- Chanya zisizo za kweli na hasi za uwongo**: kama ilivyo kwa zana yoyote ya usalama, hati za Nmap za NSE zinaweza kutoa chanya za uwongo (tahadhari za uwezekano wa kuathiriwa) au hasi za uwongo (udhaifu halisi haujatambuliwa). Hili ni jambo la kuzingatia wakati wa kuchambua matokeo ya Nmap.




Kwa hivyo ni muhimu kuelewa ni nini Nmap hufanya na haifanyi, na vivyo hivyo kujua jinsi ya kutafsiri matokeo yake. Hasa, tumeona katika somo hili lote kwamba chaguo-msingi zinaweza kutufanya tukose Elements muhimu ambayo inaweza kufichuliwa kwa matumizi makini.



Iwe wewe ni msimamizi wa mfumo wa mtandao, mhandisi wa usalama au hata CISO, kwa kutumia Nmap hukupa muhtasari wa hali ya usalama ya mfumo wa taarifa. Hii ni hatua ya kwanza muhimu katika kupata mfumo, ambao unaweza kufanywa mara kwa mara na timu ya IT. Hata hivyo, haipaswi kuchukua nafasi ya uingiliaji kati na ushauri wa wataalamu [wa usalama mtandao] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), ambao wataweza kufichua udhaifu kwa kina zaidi kuliko Nmap.



### V. Hitimisho



Katika sehemu hii ya kwanza ya Moduli ya 3, tumeanzisha uchanganuzi wa uwezekano wa kuathiriwa kupitia Nmap. Sasa tunajua jinsi ya kutumia chaguo kuu kufanya kazi hii, lakini pia tunajua mipaka ya zoezi hilo. Katika sehemu inayofuata, tutakuwa tukiangalia kwa makini utendakazi huu, kwa kutumia hati za NSE kupanua nguvu za Nmap mara kumi.



## 8 - Kutumia hati za NSE za Nmap



### I. Uwasilishaji



Katika sehemu hii, tutachunguza kwa kina hati za NSE (_Nmap Scripting Engine_). Hasa, tutaangalia kwa nini wao ni mojawapo ya uwezo mkubwa wa zana hii, jinsi wanavyofanya kazi na jinsi ya kuvinjari na kutumia hati nyingi zilizopo.



Sehemu hii inafuatia kutoka kwa mafunzo yaliyotangulia, ambamo tulijifunza jinsi ya kutumia vipengele vya kuchanganua uwezekano wa Nmap kwa njia ya msingi. Sasa tutaangalia kwa undani jinsi [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) inavyofanya kazi katika suala hili, ili kwa mara nyingine tena tuweze kufanya uchanganuzi sahihi zaidi na unaodhibitiwa.



### II. Dhana ya hati za Nmap NSE



Hati za NSE za Nmap hukuruhusu kupanua uwezo wake kwa njia inayonyumbulika sana. Zimeandikwa katika LUA, lugha ya uandishi ambayo ni rahisi kushughulikia na kufikia kuliko C au C# inayotumiwa na Nmap. Faida ya kutumia hati ya LUA iliyo na Nmap badala ya zana ya kusimama pekee ni kwamba huturuhusu kufaidika na kasi ya utekelezaji ya Nmap na vipengele vya kawaida (mwenyeji, bandari na ugunduzi wa toleo, n.k.).



Hati hizi zimepangwa kwa kategoria, na hati moja inaweza kuwa ya zaidi ya kategoria moja:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Kitaalam, kategoria ambazo hati ni mali zinaonyeshwa moja kwa moja kwenye msimbo wake.



![nmap-image](assets/fr/41.webp)



Kategoria za hati za nSE `ftp-anon`._



Mfano huu unaonyesha sehemu ya msimbo wa hati ya NSE `ftp-anon.nse`, ambayo tuliona utekelezaji wake katika sehemu iliyotangulia.



### III. Orodhesha hati zilizopo za NSE



Kwa chaguo-msingi, hati za NSE za Nmap ziko katika saraka ya `/usr/share/nmap/scripts/`, bila muundo maalum wa mti au daraja. Hapa kuna muhtasari wa yaliyomo kwenye saraka hii:



![nmap-image](assets/fr/42.webp)



hutoa yaliyomo kwenye saraka ya `/usr/share/nmap/scripts/` iliyo na hati za NSE._



Saraka hii ina zaidi ya hati 5,000 za NSE. Mara nyingi, sehemu ya kwanza ya jina la hati huwa na itifaki au kategoria ambayo ni mali yake. Hii hutuwezesha kupanga orodha, kwa mfano, ikiwa tunataka kuorodhesha hati zote zinazolenga huduma ya FTP:



![nmap-image](assets/fr/43.webp)



orodha ya hati za NSE za Nmap zilizo na majina yanayoanza na `ftp-`._



Nmap haitoi chaguo la kuvinjari na kuorodhesha hati zake za NSE; unaweza kutumia amri `--script-help` ikifuatiwa na jina la kategoria au neno:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Walakini, matokeo yatakuwa jina la kila hati na maelezo yake, ambayo sio sawa ikiwa utaftaji utaleta maandishi kadhaa:



![nmap-image](assets/fr/44.webp)



matokeo ya kutumia amri ya `--script-help` ya Nmap



Kwa maoni yangu, njia bora zaidi ni kutumia amri za Linux za kawaida kwenye saraka ya `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Jisikie huru kuvinjari msimbo wa moduli zinazozungumza nawe, ili kuelewa vyema jinsi hati ya NSE inavyofanya kazi.



### IV. Kwa kutumia hati za NSE za Nmap



Sasa tutajifunza jinsi ya kufanya uchanganuzi wa uwezekano wa kuathiriwa kwa kuchagua kwa makini hati za NSE ambazo tunavutiwa nazo.



#### A. Chagua hati kulingana na kategoria



Kuanza, tunaweza kuchagua kutekeleza hati zote za kitengo maalum. Tunahitaji kuashiria kategoria hii au kategoria hizi kwa Nmap kwa hoja `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Amri hii ya kwanza ni sawa na amri ya `nmap -sC`. Kwa chaguo-msingi, Nmap itachagua hati katika kategoria ya `chaguo-msingi, lakini hiyo ni kwa ajili ya hoja tu. Amri inayofuata, kwa mfano, itatumia maandishi yote katika kitengo cha `ugunduzi`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Kama tulivyoona, baadhi ya kategoria huturuhusu kutambua kwa haraka kile ambacho hati zinazohusiana za NSE hufanya (`ugunduzi`, `vuln`, `exploit`), huku zingine zikifafanua kiwango cha hatari, ugunduzi au uthabiti wa jaribio lililofanywa. Iwapo tuko katika muktadha nyeti na hatuelewi vyema vitendo tofauti vinavyofanywa na uteuzi wetu wa hati, tunaweza kuchagua kuchanganya chaguo ili kuchagua tu hati zile zilizo katika kategoria za `ugunduzi` na `salama`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Iwapo unataka kabisa na kwa udhahiri kuwatenga hati kutoka kwa kategoria za `dos` na `intrusive`, unaweza kutumia nukuu ifuatayo:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Tafadhali kumbuka kuwa kubainisha masharti ya kutengwa kama ilivyo hapo juu kutasababisha matumizi ya kategoria nyingine zote ambazo hazijatengwa waziwazi. Ili kuwa wa haki, tunaweza kutaja, kwa mfano:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Hii hapa ni baadhi ya mifano ya jinsi ya kushughulikia hati za NSE kulingana na kategoria, haswa wakati wa kutumia Nmap kwa uchanganuzi wa kuathirika katika miktadha ya maisha halisi.



#### B. Chagua hati kama kitengo



Tunaweza pia kuchagua kufanya jaribio moja mahususi wakati wa uchanganuzi, jaribio linalolingana na hati ya NSE. Ili kufanya hivyo, tunahitaji kutaja jina la hati katika parameter ya `-script <jina>`. Kuchukua mfano wa hati ya `ftp-anon.nse`:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Kisha tunapata matokeo sahihi sana:



![nmap-image](assets/fr/45.webp)



matokeo ya kutumia hati ya NSE `ftp-anon` kwenye mlango wa FTP kupitia Nmap._



Tunaona matokeo ya kuendesha hati ya `ftp-anon` kwenye mlango wa 21, na hakuna mlango mwingine, kwa sababu tulibainisha chaguo la `-p 21`. Pia tungeweza kufanya uchunguzi wa msingi wa mlango, kwa kutekeleza hati ya `ftp-anon` ya NSE kwenye huduma za FTP zilizogunduliwa pekee:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Kwa hivyo, Nmap pia ingetekeleza jaribio hili la muunganisho lisilojulikana ikiwa ingepata huduma ya FTP kwenye mlango mwingine.



Kwa maelezo mafupi ya kile hati ya NSE hufanya, unaweza kutumia chaguo la `--script-help` lililotajwa hapo juu:



![nmap-image](assets/fr/46.webp)



msaada wa kuonyesha matokeo ya hati ya NSE `sshv1`._



Kwa kifupi, kwa mara nyingine tena tunaweza kutumia tena chaguo zote za ugunduzi wa mtandao, huduma, matoleo na teknolojia ambazo tumetumia hadi sasa!



#### C. Kusimamia hoja za hati



Wakati wa kutumia Nmap, utakutana na hati fulani za NSE ambazo zinahitaji hoja za ingizo ili kufanya kazi ipasavyo. Sasa tutaangalia jinsi ya kupitisha hoja kwa hati hizi kupitia chaguzi za Nmap.



Kama mfano, hebu tuchukue hati ya `ssh-brute`, ambayo hukuruhusu kufanya shambulio la kikatili kwenye huduma ya SSH.



Shambulio la kawaida la kikatili linajumuisha kujaribu manenosiri kadhaa (wakati mwingine mamilioni) katika jaribio la kuthibitisha kwa akaunti mahususi. Kwa kujaribu manenosiri mengi, mshambuliaji huweka dau juu ya uwezekano kwamba mtumiaji ametumia nenosiri dhaifu katika kamusi ya nenosiri iliyotumiwa kwa shambulio hilo.



Hati hii ina chaguo "chaguo-msingi", ambazo tunaweza kubinafsisha ili kuendana na muktadha wetu. Katika muktadha wa shambulio hili, kwa mfano, tunaweza kutoa Nmap orodha ya watumiaji na kamusi ya nenosiri itakayotumika. Ninavyojua, haiwezekani kuorodhesha kwa urahisi hoja zinazohitajika kwa hati, kwa hivyo njia ya kuaminika zaidi ni kutembelea tovuti rasmi ya Nmap. Kiungo cha moja kwa moja kwa hati ya hati ya NSE kinaweza kupatikana kwa kujibu chaguo la `--script-help`:



![nmap-image](assets/fr/47.webp)



matokeo ya kuonyesha usaidizi wa hati ya NSE `ssh-brute` iliyo na kiunga cha nmap.org._



Kwa kubofya kiungo kilichoonyeshwa, tunafika kwenye ukurasa huu wa tovuti wa tovuti [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



orodha ya hoja zinazoweza kupitishwa kwa hati ya NSE ya `ssh-brute` ya NSE



Hapa tuna mtazamo wazi wa hoja zinazoweza kutumika, kuu katika muktadha wetu ni `passdb` (faili iliyo na orodha ya manenosiri) na `userb` (faili iliyo na orodha ya watumiaji). Hati hapa inarejelea maktaba za ndani za Nmap, kwani mbinu hizi za nguvu za kikatili na chaguo zinazohusiana zinaunganishwa ili kutumika kwa usawa katika hati kadhaa (`ssh-brute`, `mysql-brute`, `mssql-brute`, n.k.) na kwa hivyo zitakuwa na hoja zaidi au chini ya sawa:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Kama unavyoona katika amri hii ya mwisho, tunaweza kubainisha hoja zinazohitajika kwa hati ya Nmap kwa kutumia `--scripts-args key=value,key=value` chaguo. Hapa kuna matokeo yanayowezekana ya matokeo ya Nmap wakati wa kutekeleza nguvu ya kikatili ya SSH kupitia hati ya `ssh-brute` NSE:



![nmap-image](assets/fr/49.webp)



matokeo ya utekelezaji wa SSH bruteforce kupitia Nmap._



Kama unavyoona, maelezo yanayotolewa na hati za NSE hutanguliwa na `NSE: [jina la hati]` katika pato shirikishi (toleo la mwisho), na kuifanya iwe rahisi kupata. Ndani ya onyesho la kawaida la matokeo ya Nmap, tuna muhtasari tu unaoonyesha ikiwa vitambulishi dhaifu vimegunduliwa (pamoja na manenosiri, kumbuka).



Ili kuchukua hatua mbele zaidi, na kukukumbusha kuwa haya yote yanaweza kutumika pamoja na chaguo zote ambazo tayari tumeziangalia, hapa kuna amri ambayo itagundua mtandao wa `10.10.10.0/24`, kuchanganua bandari za TCP mara nyingi zaidi za 2000 na kuendesha utafutaji wa ufikiaji usiojulikana kwenye huduma za FTP na kampeni ya nguvu kwenye huduma za SSH:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Huu ni mfano mmoja tu wa maandishi mengi yanayopatikana na chaguzi zao. Lakini sasa tuna wazo bora zaidi la jinsi ya kupata hati za NSE, iwe zinahitaji hoja na jinsi ya kupitisha hoja hizi kwa Nmap.



### V. Hitimisho



Katika sehemu hii, tumejifunza jinsi ya kutumia hati za NSE za Nmap kutekeleza kazi mbalimbali. Ninakualika uchukue muda kugundua kategoria tofauti za hati na hati zenyewe, ili kuona ni majaribio mangapi yanayoweza kufanya otomatiki.



Kwa sehemu kadhaa sasa, tumekuwa tukikusanya chaguo za juu zaidi za ugunduzi, uchanganuzi na kuhesabu. Kufikia sasa, unapaswa kufahamu kuwa matokeo ya Nmap na onyesho la matokeo linaanza kuwa pana sana, wakati mwingine hata kitenzi kikuu kwa terminal yetu. Katika sehemu inayofuata, tutajifunza jinsi ya kusimamia matokeo haya, haswa kwa kuihifadhi katika faili katika miundo mbalimbali.






## 9 - Kusimamia data ya matokeo ya Nmap




### I. Uwasilishaji



Katika sehemu hii, tutaangalia towe linalotolewa na Nmap, na haswa katika chaguzi mbalimbali za uumbizaji towe hili. Tutaona kwamba Nmap inaweza kutoa umbizo la towe kadhaa ili kukidhi mahitaji tofauti, na kwamba hii pia ni mojawapo ya uwezo mkubwa wa zana hii.



Kwa chaguo-msingi, Nmap inatoa mwonekano wa kina wa matokeo ya skanisho na majaribio inayofanya. Hii inajumuisha seva pangishi na huduma zilizochanganuliwa, zinazogunduliwa kuwa zinaweza kufikiwa, maelezo mahususi ya milango iliyo wazi, hali na toleo lao. Kwa kuongeza, maelezo ya hati za NSE zinapatikana pia katika matokeo ya mwisho. Walakini, pato hili linaweza kuwa kubwa haraka, hata ikiwa na umbizo wazi la habari, ambayo inaweza kufanya iwe ngumu kupata habari sahihi katika matokeo.



### II. Kusimamia umbizo la towe la Nmap



#### A. Hifadhi matokeo ya kuchanganua katika faili ya maandishi



Ili kurahisisha mambo, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) hurahisisha sana kuhifadhi matokeo yake katika faili ya maandishi. Hii inaweza kuwa muhimu kwa kuweka kwenye kumbukumbu, kulinganisha na majaribio mengine, lakini pia kwa kuvinjari matokeo haya kwa zana maalum za kuchakata maneno au lugha za hati, kama vile maandishi ya Sublime, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, a's output, nk. tumia `-oN <filename>` chaguo ("N" katika "kawaida"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Haishangazi basi, kwani Nmap itaonyesha pato lake la kawaida kwenye terminal yetu, lakini pia kwenye faili iliyoainishwa.



#### B. generate Towe la Nmap katika umbizo lililofupishwa



Pia kuna umbizo la towe la pili katika mtindo wa "maandishi" ambao unaweza kufasiriwa kwa urahisi na mwanadamu: umbizo la "greppable".



Umbizo hili liliundwa ili kutoa mwonekano "uliofupishwa" wa matokeo ya Nmap, yaliyoundwa kwa njia ya kuwezesha uchakataji wake kwa zana kama vile `grep`. Wacha tuangalie mfano wa aina hii ya pato:



![nmap-image](assets/fr/50.webp)



kuchanganua mtandao wa nmap na kutoa katika umbizo la "greppable"._



Hapa, nimefanya ugunduzi wa mtandao na vile vile uchunguzi wa bandari na uchanganuzi wa teknolojia na matoleo kwenye mtandao /24, kisha nikahifadhi matokeo katika faili katika umbizo la "greppable". Ninaishia na faili iliyo na mistari 2 kwa kila mwenyeji anayefanya kazi:





- Mstari wa kwanza unaniambia kuwa mwenyeji kama huyo na kama ni _Up_;





- Mstari wa pili unaniambia ni bandari zipi zimechanganuliwa, hali zao na teknolojia na maelezo ya toleo yaliyopatikana katika umbizo mahususi: `<port>/<status/<protocol>//<service>//<version>/,`




Uumbizaji huu wenye kikomo maalum huruhusu uchakataji wa haraka kwa zana za kuchakata maneno kama vile `grep`, au lugha za hati na programu. Amri ifuatayo, kwa mfano, huniwezesha kupata taarifa kwa urahisi kuhusu mwenyeji `10.10.10.5` katika kesi ya uchanganuzi mkubwa uliofanywa na Nmap ambao matokeo yake itakuwa vigumu kuvinjari:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Kinyume chake, naweza pia kuorodhesha majeshi yote ambayo yana bandari 21 wazi kwa urahisi, kwani bandari na IP ziko kwenye mstari huo huo:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Ili kutoa matokeo kama haya ya generate, tunahitaji kutumia `-oG <filename>.gnmap` chaguo ("G" katika "grep"). Kwa mazoea, mimi hutumia kiendelezi cha `.gnmap` hapa kwa faili kama hiyo, lakini jisikie huru kutumia chochote unachopenda:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Umbizo hili linaweza kutumika kwa madhumuni mbalimbali na ni muhimu hasa kwa uandishi/upangaji wa haraka. Hata hivyo, inaelekea kuachwa ili kupendelea umbizo ambalo tutaangalia baadaye.



kumbuka: umbizo la `-oG` greppable limeacha kutumika rasmi tangu Nmap 7.90. Bado inaweza kutumika kwa utangamano. Bado inaweza kutumika kwa madhumuni ya uoanifu, lakini inashauriwa utumie XML au umbizo la kawaida kwa usanidi wowote au uchanganuzi wa kiotomatiki._



#### Umbizo la C. XML la pato la Nmap



Umbizo la mwisho linalostahili kutajwa katika mafunzo haya ni XML. Tofauti na fomati mbili zilizopita, hii haikuundwa kusomwa na wanadamu, lakini na zana au maandishi mengine.



XML (_eXtensible Markup Language_) ni lugha ya alama inayotumiwa kuhifadhi na kusafirisha data, ikitoa muundo wa daraja kupitia lebo maalum.



Ndani ya Nmap, umbizo la XML linatumika kwa ripoti za kina za generate kuhusu uchanganuzi uliofanywa, ikijumuisha maelezo kuhusu seva pangishi, bandari na udhaifu uliogunduliwa, pamoja na maelezo ya ziada ambayo hayajaonyeshwa katika toleo la kawaida la Nmap.



Ili generate faili towe katika umbizo la XML, tunahitaji kutumia chaguo `-oX` ("O" kutoka "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Matokeo yake ni pato la kawaida la Nmap kwenye terminal yako, na pia faili katika umbizo la XML katika saraka yako ya sasa.



Bila shaka, umbizo la XML halijaundwa kusomwa na kufasiriwa na wanadamu. Walakini, ikiwa unataka kufanya uandishi au uchanganuzi wa kiotomatiki kwenye umbizo hili la matokeo ya Nmap, bado unahitaji kuwa na wazo la lebo na muundo unaotumika. Kwa mfano, hii hapa ni sehemu ya maudhui ya faili ya XML iliyoundwa na Nmap, ambayo inaonyesha matokeo ya skanisho ya mpangishi 1:



![nmap-image](assets/fr/51.webp)



mfano wa rekodi ya XML kwa seva pangishi 1 wakati wa kuchanganua Nmap



Kuna habari nyingi hapa, na tunavutiwa sana na bandari mbili zilizo wazi:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Tunaelewa kuwa umbizo hili litawezesha uchanganuzi wa matokeo kiotomatiki, kwa kuwa kila taarifa imepangwa vizuri katika lebo maalum, iliyopewa jina au sifa. Hasa, tunapata kipande cha habari ambacho hatujapata hapo awali: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Tulitaja kwa ufupi CPE katika sehemu ya 2 ya moduli ya 2, na maelezo haya yanabainishwa katika mechi zinazolingana wakati wa kutambua toleo. Nmap hutumia huduma zake, teknolojia na mbinu za kugundua matoleo ili kupata CPE inayohusika.



Hii huturuhusu kutumia tena habari hii na hifadhidata na programu zinazoitumia. Ninafikiria haswa hifadhidata ya NVD, ambayo inarejelea CVEs. Kwa kila CVE, ina CPE zilizoathiriwa na mazingira magumu. Huu hapa ni mfano wa CVE kuhusu `a:microsoft:internet_information_services:7.5` kutoka kwa hifadhidata ya NVD:



![nmap-image](assets/fr/52.webp)



uwepo wa CPE katika maelezo ya CVE katika hifadhidata ya NVD



Sasa tuna uelewa mzuri zaidi wa manufaa ya umbizo hili, ambalo linatoa muundo ulio wazi kabisa wa taarifa na lina data yote iliyokusanywa au kuchakatwa na Nmap.



Kama reflex, mimi huhifadhi kwa utaratibu skana zangu za Nmap katika fomati zote tatu mara moja. Hili linawezekana kwa chaguo la `-oA <name>` ("A" kwa "Zote"), ambalo litaunda faili ya `<jina>.nmap`, faili ya `<jina>.xml` na `<jina>.gnmap`. Kwa njia hii nina hakika sitakosa chochote ninapohitaji kurejea matokeo.



Ukiwa na miundo hii mitatu, unapaswa kuwa na kila kitu unachohitaji ili kuhifadhi na hatimaye kuchakata matokeo ya Nmap kwa njia ya kiotomatiki. Tutakuwa tukitumia umbizo la XML tena katika sehemu inayofuata, tunapoangalia kutumia Nmap na zana zingine za usalama.



#### III. Inazalisha ripoti ya HTML kutoka kwa uchunguzi wa Nmap



Umbizo la XML linatoa uwezekano mwingi, si haba ule wa kutumika kama msingi wa kutoa ripoti katika umbizo la HTML, ambayo itakuwa ya kupendeza zaidi kuvinjari.



Ili kubadilisha faili ya Nmap katika umbizo la XML kuwa ukurasa wa wavuti, tutatumia zana ya `xsltproc`, ambayo tutahitaji kusakinisha kwanza:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Mara tu chombo hiki kitakaposakinishwa, kipe tu faili ya XML ya kubadilishwa na jina la ripoti ya HTML kuzalishwa:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Kwa hivyo, tutakuwa na muundo wetu mzima wa kuchanganua, na hata rangi chache na viungo vinavyoweza kubofya katika jedwali la yaliyomo!



![nmap-image](assets/fr/53.webp)



dondoo kutoka kwa ripoti ya skanisho ya Nmap katika umbizo la HTML iliyotolewa na xsltproc._



Kwa upana, faili ya XML iliyohifadhiwa na Nmap ina rejeleo la faili nyingine katika umbizo la XSL:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Ubadilishaji hadi HTML kwa hivyo ni chaguo la kukokotoa lililotolewa na kuwezeshwa na Nmap, `xsltproc` ikiwa ni zana ya kawaida na inayotambulika ya kutekeleza kazi hii (ambayo haitoki kwenye kitengo cha zana cha Nmap).



XSLT (_Extensible Stylesheet Language Transformations_) ni kikundi kidogo cha XSL ambacho huruhusu data ya XML kuonyeshwa kwenye ukurasa wa wavuti na "kubadilishwa", sambamba na mitindo ya XSL, kuwa taarifa inayosomeka, iliyoumbizwa katika umbizo la HTML.



chanzo: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Kiwango cha maelezo katika ripoti ni sawa na kile cha umbizo la XML la Nmap na cha juu zaidi ya kile cha toleo la kawaida la mwisho (_interactive output_).



### IV. Kusimamia kiwango cha verbosity cha Nmap



Sasa tutaangalia chaguo chache za Debugger Nmap au kufuatilia maendeleo yake.



Chaguo la kwanza tunalopaswa kutaja ni chaguo la `-v`, ambalo huongeza kitenzi cha Nmap. Hapa kuna mfano:



![nmap-image](assets/fr/54.webp)



pato la kitenzi cha nmap kwa kutumia chaguo la `-v`._



Kwenye uchanganuzi unaolenga seva pangishi na milango mingi, kifaa cha kutoa matokeo kitakuwa vigumu kutumia kutokana na kiasi cha taarifa kinachoonyeshwa. Kwa sababu hii, chaguo hili linapaswa kutumiwa pamoja na chaguzi zilizoonekana hapo awali, ambazo hukuruhusu kuhifadhi pato la kawaida la Nmap kwenye faili. Taarifa zinazohusiana na matumizi ya kitenzi hazitajumuishwa kwenye faili hii ya towe. Kama unavyoona kutoka kwa mfano hapo juu, kitenzi hiki hukuruhusu kufuatilia vitendo na uvumbuzi wa Nmap kwa uwazi na moja kwa moja. Kwa uchanganuzi wa muda mrefu ambapo onyesho la data linaweza kuwa polepole kuja, hii inaepuka kutoona shughuli ya sasa ya Nmap na kujua kuwa mambo yanaendelea na kwa kasi gani. Ili kuongeza kitenzi kwa kiwango zaidi, unaweza kutumia chaguo la `-vv`.



Ili kufuatilia zaidi shughuli za Nmap wakati wa kuchanganua, unaweza kutumia chaguo la `--packet-trace`. Kwa chaguo la `-v`, tunapata kumbukumbu ya moja kwa moja ya bandari zote zilizofunguliwa zilizogunduliwa na Nmap, ambapo kwa chaguo hili, tunapata laini ya kumbukumbu kwa kila pakiti inayotumwa kwenye mlango. Kwa kawaida hii hutoa pato la kitenzi, lakini inaruhusu ufuatiliaji wa kina wa shughuli za Nmap, hapa kuna mfano:



![nmap-image](assets/fr/55.webp)



ufuatiliaji wa kina wa shughuli za Nmap kupitia `--packet-trace`._



Tena, maelezo haya hayatarekodiwa katika faili ya towe inayotolewa na Nmap ikiwa chaguzi za `-oN`, `-oG`, `-oX` au `-oA` zitatumika.



Hatimaye, Nmap pia inatoa chaguo mbili za utatuzi: `-d` na `-dd`. Chaguo hizi hufanya kazi sawa na chaguo la `-v` kitenzi, lakini ongeza maelezo ya ziada ya kiufundi, kama vile muhtasari wa vigezo vya kiufundi mwanzoni mwa uchanganuzi:



![nmap-image](assets/fr/56.webp)



chaguzi za muda zinaonyeshwa katika mwonekano wa utatuzi wa Nmap



Katika sehemu chache zinazofuata, tutaangalia chaguzi za "Timing" ni nini na kwa nini inafaa kuzijua.



Hatimaye, ikiwa unataka tu kuwa na muhtasari wa kimsingi, wa sanisi wa maendeleo ya uchanganuzi wa Nmap, unaweza kutumia chaguo la `--stats-kila 5s`. "5s" hapa inamaanisha sekunde 5 na inaweza kurekebishwa ili kukidhi mahitaji yako. Haya ndiyo masafa ambayo tutapokea maoni kutoka kwa Nmap kuhusu maendeleo yake:



![nmap-image](assets/fr/57.webp)



habari iliyoonyeshwa na chaguo la Nmap `--stats-every`



Hasa, tunaweza kupata asilimia ya maendeleo, pamoja na dalili ya awamu ambayo iko: awamu ya ugunduzi wa seva pangishi kupitia [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), awamu ya ugunduzi wa bandari za TCP zilizofichuliwa, n.k. Maelezo haya pia yanaweza kupatikana katika toleo la mwisho kwa kubonyeza "Enter" wakati wa kuchanganua.



Hata hivyo, Nmap si nzuri sana katika kukadiria muda ambao kazi itachukua, si haba kwa sababu haijui mapema ni wapangishi na huduma ngapi italazimika kuchanganua.



### V. Hitimisho



Katika sehemu hii, tumeangalia chaguo kadhaa za kuhifadhi matokeo ya utambazaji wa Nmap katika umbizo tofauti za faili. Hii itakusaidia sana, kwani katika miktadha halisi, matokeo ya kuchanganua yanaweza kuchukua mamia au hata maelfu ya mistari! Tumeona pia jinsi ya kuongeza kiwango cha verbosity ya Nmap kwa madhumuni ya utatuzi au kupata ripoti ya maendeleo ya kuchanganua.



Umbizo la XML litakuwa muhimu sana katika sehemu inayofuata, ambapo tutaangalia zana chache zinazoweza kufanya kazi na matokeo ya Nmap.




## 10 - Kutumia Nmap na zana zingine za usalama



### I. Uwasilishaji



Katika sehemu hii, tutaangalia baadhi ya matumizi ya kawaida ya Nmap na zana zingine za usalama zisizolipishwa na huria. Hasa, tutatumia yale ambayo tumejifunza katika sehemu zilizopita ili kuboresha zaidi nguvu na ufanisi wa Nmap.



Uwezo wa kuhifadhi matokeo ya uchanganuzi wa Nmap katika XML hufanya data iendane na zana zingine nyingi. Kwa vile karibu lugha zote za programu na hati leo zina maktaba zenye uwezo wa kuchanganua XML, hii hurahisisha zaidi kuchakata data hii. Zana kadhaa, hasa zile zinazolengwa kuelekea usalama unaokera, zina utendakazi wa kuchakata umbizo la XML linalotolewa na Nmap. Hebu tuangalie kwa karibu.



Nitataja zana chache za kukera bila kuelezea kwa undani jinsi zinatumiwa au jinsi zinavyofanya kazi. Nitachukulia kuwa msomaji anafahamu matumizi yao ya kimsingi na kwamba tayari yanafanya kazi. Sehemu hii itawavutia sana wataalamu wa [cybersecurity] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), watu walio katika mafunzo au wale ambao wameamua kutafakari kwa kina zaidi somo hili.



### II. Inaleta matokeo ya Nmap kwenye Metasploit



Zana ya kwanza tutakayoangalia ya kutumia tena data ya Nmap katika utafiti unaokera wa usalama na uwezekano wa kuathirika ni Metasploit.



Metasploit ni mfumo wa kunyonya na kushambulia. Ni suluhisho la bure na chombo kinachotambulika ambacho kina idadi kubwa ya moduli zilizoandikwa katika Ruby au Python. Haya huwezesha udhaifu kutumiwa, mashambulizi kutekelezwa, milango ya nyuma kuzalishwa, upigaji simu kudhibitiwa (C&C au kipengele cha Mawasiliano na Udhibiti) na kila kitu kutumika kwa usawa.



Hasa, mfumo huu wa uendeshaji unaojulikana na unaotumika sana unaweza kufanya kazi na postgreSQL [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) ambamo wapangishi, bandari, huduma, taarifa za uthibitishaji na mengineyo huhifadhiwa.





- Hati Rasmi za Metasploit: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Hapa ndipo Nmap na matokeo yake yanapotumika, kwani umbizo la XML la matokeo ya Nmap linaweza kuingizwa kwa urahisi kwenye hifadhidata ya Metasploit ili kujaza hifadhidata yake ya wapangishi na huduma, ambayo inaweza kisha kuteuliwa kwa haraka kama shabaha za shambulio hili au lile.



Mara moja kwenye ganda langu la kuingiliana la Metasploit, naanza kwa kuunda nafasi ya kazi, aina ya nafasi maalum kwa mazingira yangu ya siku hiyo:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Mara tu nafasi yangu ya kazi imeundwa, tunahitaji kudhibitisha kuwa mawasiliano na hifadhidata inafanya kazi:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Hatimaye, tunaweza kutumia amri ya Metasploit `db_import` kuleta skanisho yetu ya Nmap katika umbizo la XML:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Hapa kuna matokeo ya kutekeleza amri hizi zote:



![nmap-image](assets/fr/58.webp)



ingiza skanisho ya Nmap katika umbizo la XML kwenye hifadhidata ya Metasploit



Hapa unaweza kuona kwamba kila mwenyeji huingizwa, pamoja na huduma zake. Data hii inaweza kisha kuonyeshwa kupitia amri `services` au `services -p <port>` kwa huduma maalum:



![nmap-image](assets/fr/59.webp)



orodha ya huduma zilizoagizwa kutoka kwa faili ya XML hadi kwenye hifadhidata ya Metasploit



Hatimaye, tunaweza kutumia tena data hii kwa haraka na kwa urahisi katika moduli ya shukrani kwa chaguo la `-R`, ambalo "litabadilisha" orodha ya huduma zilizopatikana kama ingizo la maagizo ya `RHOSTS`, ambayo hutumika kubainisha malengo ya shambulio hilo kufanywa. Huu hapa ni mfano wa moduli ya `ssh_login`, ambayo hukuwezesha kutekeleza mashambulizi ya kikatili kwenye huduma za [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



tumia chaguo la `services -R` kuleta huduma zilizobainishwa kama lengo la shambulio hilo



Huu ni mfano mdogo tu wa kile kinachoweza kufanywa na data ya Nmap katika Metasploit, lakini inakupa wazo dogo la jinsi maelezo haya yanaweza kutumika tena kwa haraka na kwa urahisi kama sehemu ya jaribio la kupenya, skanning ya kuathirika au shambulio la mtandao. Inafaa pia kutaja kuwa Nmap inaweza kuendeshwa moja kwa moja kutoka kwa Metasploit ili kuleta matokeo kwenye hifadhidata (amri `db_nmap`), mada nyingine ya kupendeza ya kushughulikia!



### III. Kutumia Nmap na kichanganuzi cha wavuti cha Aquatone



Zana ya pili ambayo ningependa kutambulisha katika sehemu hii kuhusu kutumia tena matokeo ya Nmap kwa uchanganuzi unaokera wa usalama na uwezekano wa kuathirika ni Aquatone.



Aquatone ni kichanganuzi cha wavuti kilichoundwa kuchunguza kwa ufanisi programu za wavuti kwenye mtandao. Inatoa vipengele vya kina vya ugunduzi wa huduma za wavuti, kitambulisho cha kikoa kidogo, uchanganuzi wa bandari na uwekaji alama za vidole kwenye programu ya wavuti. Zote zimewasilishwa kwa uwazi na kwa ufupi katika HTML, JSON na ripoti za maandishi kwa uchanganuzi rahisi wa usalama wa wavuti.



Kama ilivyo kwa Metasploit, Aquatone inaweza kuchakata umbizo la XML la Nmap moja kwa moja na kuitumia kama shabaha ya kuchanganua. Hasa, inaweza kutoa wapangishi na huduma zinazovutia pekee (huduma za wavuti) kutoka kwa data yote ambayo ripoti ya Nmap inaweza kuwa nayo.





- Kiungo cha zana: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Ili kutumia pato la XML la Nmap na Aquatone, tuma faili ya XML kwenye bomba ambalo litatumiwa na Aquatone. Hapa kuna mfano:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Ambapo Aquatone kwa kawaida hufanya ugunduzi wa bandari kwa wapangishaji kupata huduma za wavuti, katika muktadha huu itategemea tu matokeo ya Nmap, ambayo tayari imefanya operesheni hii, hivyo kuokoa muda:



![nmap-image](assets/fr/61.webp)



kutumia matokeo ya Nmap katika umbizo la XML na `aquatone`._



Kwa taarifa yako, hapa kuna dondoo kutoka kwa ripoti iliyotolewa na Aquatone:



![nmap-image](assets/fr/62.webp)



mfano wa ripoti ya `aquatone`



Binafsi, mara nyingi mimi hutumia Aquatone kupata muhtasari wa haraka wa aina za tovuti zilizopo kwenye mtandao, shukrani haswa kwa utendakazi wake wa picha ya skrini.



Hapa tena, kuwa na ripoti kamili ya Nmap katika umbizo la XML huokoa muda na kurahisisha kutumia tena katika zana nyingine.



### IV. Hitimisho



Mifano hii miwili inaonyesha wazi kwamba umbizo la XML la Nmap hurahisisha zana zingine kutumia matokeo yake, kwani ni umbizo la data lililoundwa, na rahisi kutumia. Kuna zana zingine nyingi zinazoweza kuchakata matokeo haya, kama vile zana za kuripoti otomatiki, uwakilishi wa picha au vichanganuzi changamano zaidi vya kuathiriwa.



Bila shaka, unaweza pia kutengeneza hati na zana zako mwenyewe katika Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) au lugha nyingine yoyote iliyo na maktaba ya uchanganuzi ya XML ili kudanganya na kutumia tena data ya matokeo ya Nmap unavyoona inafaa.



Sehemu hii inatuleta hadi mwisho wa moduli ya mafunzo juu ya matumizi ya hali ya juu zaidi ya Nmap, haswa kwa uchanganuzi wa hatari kupitia hati za NSE.



Sehemu inayofuata ya mafunzo italenga, miongoni mwa mambo mengine, juu ya mbinu bora zaidi za ziada, za kiufundi zaidi na vidokezo kuhusu uchanganuzi mahususi ambao Nmap inaweza kutekeleza. Pia tutaangalia chaguo za uboreshaji wa utendakazi, ambazo ni muhimu sana wakati wa kuchanganua mitandao mikubwa.




## 11 - Kuboresha utendaji wa skanning ya mtandao



### I. Uwasilishaji



Katika sura hii, tutajifunza jinsi ya kuongeza kasi ya uchanganuzi wa mtandao unaofanywa na Nmap kwa kutumia chaguo mbalimbali mahususi. Hasa, tutajifunza zaidi kuhusu utendakazi wa ndani wa Nmap, kutoka kwa usimamizi _timeout_ hadi usanidi uliohifadhiwa mapema wa zana.



Sasa kwa kuwa tumeangalia vyema vipengele vya Nmap, wacha tukabiliane na mnyama huyo na nguvu zake. Ikiwa umewahi kutumia chombo kwenye mitandao mikubwa, labda umeona kwamba baadhi ya scanning inaweza kuchukua muda mrefu, licha ya nguvu ya chombo. Na kwa sababu nzuri: amri rahisi ya `nmap` yenye chaguo chache inaweza generate mamilioni ya pakiti zinazolenga mamia ya maelfu ya mifumo na huduma zinazowezekana.



Zaidi ya hayo, baadhi ya usanidi wa vifaa vya mtandao unaweza kuweka kimakusudi kasi ya polepole (idadi ya pakiti kwa sekunde), katika hatari ya kukataa pakiti zako au kupiga marufuku IP yako Address kwa sababu za usalama.



Kulingana na muktadha, inaweza kuwa na manufaa kujaribu na kuboresha haya yote, kama tutakavyoona katika sura hii.



Kwa hali yoyote, unaweza kuangalia maadili chaguo-msingi ya vigezo tutakavyoangalia, na pia ikiwa chaguo utakazotumia zimezingatiwa kwa usahihi, kupitia utatuzi wa Nmap (chaguo `-d` lililoonekana katika sura iliyotangulia):



![nmap-image](assets/fr/63.webp)



tazama chaguzi za Muda kupitia chaguo la Nmap `-d`._



### II. Kudhibiti kasi ya utafutaji wa Nmap



#### A. Kusimamia usambamba



Kwa chaguo-msingi, Nmap hutumia ulinganifu katika uchanganuzi wake ili kuziboresha, na vigezo vyote inavyotumia vinaweza kurekebishwa kupitia chaguo mbalimbali. Walakini, hali ambazo ni muhimu kurekebisha vigezo hivi ni nadra sana, kwa hivyo hatutazizingatia kwa undani katika somo hili:





- `--min-hostgroup/max-hostgroup <size>`: ukubwa wa vikundi sambamba vya kuchanganua seva pangishi.





- `--min-parallelism/max-parallelism <numprobes>`: usawazishaji wa Vichunguzi.





- `--scan-delay/--max-scan-dey <time>`: hurekebisha ucheleweshaji kati ya Probes.




Jua tu kuwa zipo na zinaweza kutumika.



#### B. Kusimamia idadi ya pakiti kwa sekunde



Kwa chaguo-msingi, Nmap yenyewe hurekebisha idadi ya pakiti kwa sekunde inazotuma kulingana na majibu ya mtandao. Lakini inawezekana kulazimisha mpangilio huu kwa kufafanua thamani ya juu na/au ya chini kufuata kulingana na idadi ya pakiti kwa sekunde. Mpangilio huu unafanywa kwa kutumia chaguo `--min-rate <number>` na `--max-rate <number>` ambapo `number` inawakilisha idadi ya pakiti kwa sekunde. Mfano:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Chaguzi hizi hukuruhusu kurekebisha kasi ya skana kulingana na mahitaji yako maalum, ama kuharakisha mchakato au kupunguza kikomo cha data kinachotumiwa. Kesi ya mwisho (kupunguza kasi ya skana) ndio ambayo itakuongoza kwa chaguzi hizi, haswa ikiwa utapata latency ya mtandao unapotumia Nmap (ambayo ni nadra sana).



### III. Kudhibiti hitilafu za muunganisho na muda wa kuisha



Kigezo kingine ambacho tunaweza kucheza nacho ili kuboresha kasi ya utafutaji wa Nmap (au kuhakikisha usahihi zaidi) masuala _timeout_ na _retry_.



Kwa _timeouts_, huu ndio muda wa **no majibu kuisha** ambapo Nmap itaacha kusubiri jibu na kuzingatia huduma au seva pangishi haiwezi kufikiwa. Kwa _jaribu tena_, hii ni **idadi ya majaribio mfululizo katika operesheni** ambayo Nmap itafanya kabla ya kuendelea.



Kama ilivyo kwa ulinganifu, usimamizi wa _timeout_ na _retry_ unaweza kutumika kwa seva pangishi au awamu za ugunduzi wa huduma:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: inabainisha muda wa kurudi na kurudi wa Exchange. Tena, kigezo hiki kinahesabiwa na kubadilishwa kwa kuruka wakati wa tambazo. Kuna uwezekano kwamba utahitaji kuitumia, kwani Nmap huhesabu wakati huu kwa kuruka kulingana na majibu ya mtandao.





- `--max-retries <number>`: hupunguza idadi ya utumaji upya wa pakiti wakati wa kuchanganua mlangoni. Kwa chaguo-msingi, Nmap inaweza kwenda hadi majaribio 10 kwa huduma moja, hasa ikiwa inapata muda wa kusubiri au hasara katika kiwango cha mtandao, lakini katika hali nyingi ni moja tu inafanywa.





- `--host-timeout <time>`: inabainisha muda wa juu zaidi ambao Nmap itatumia kwa seva pangishi kwa shughuli zake zote, ikiwa ni pamoja na kutafuta mlango, kutambua huduma, na shughuli nyingine zozote zinazohusiana na seva pangishi. Iwapo muda huu wa muda utapitwa bila jibu lolote au **kukamilika kwa utendakazi**, Nmap itaachana na seva pangishi hii bila kuonyesha matokeo yoyote kuihusu, na kuendelea na inayofuata katika orodha yake. Hii hukuruhusu kudhibiti muda wa juu zaidi ambao Nmap hutumia kwa seva pangishi fulani, kuepuka kukwama kwa wapangishi waliokaidi na kuboresha muda wa jumla wa kuchanganua.




Katika kazi yangu ya kila siku, mimi hutumia chaguzi za `--max-retries` na `--host-timeout` ili kuboresha utafutaji wangu:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Vigezo hivi vinatoa unyumbulifu zaidi wa kurekebisha tabia ya skanisho kwa mahitaji maalum na hali ya mtandao. Hata hivyo, unahitaji kufahamu athari zao katika suala la mzigo kwenye wapangishi waliochanganuliwa na uwezekano wa kupoteza usahihi.



### IV. Matumizi ya usanidi ulioandaliwa



Chaguo mbalimbali ambazo tumeona katika sura hii zinaweza kutumika kibinafsi au kama sehemu ya usanidi ulio tayari kutolewa na Nmap. Chaguo linalowezesha _templates_ hizi (violezo vya usanidi) kutumika ni `-T <nambari>` au `-T <jina>`. Kuna viwango 5 vya _templates_:



```
-T<0-5>: Set timing template (higher is faster)
```



Kwa chaguomsingi, Nmap hutumia _template_ 3 (_normal_), ambayo kwa ujumla inatosha.



Kwa upande wangu, kwa ujumla mimi hufanya kazi katika miktadha ambayo ninahitaji kuwa haraka sana (huku nikibaki kamili iwezekanavyo) na mimi hutumia chaguo la `-T4` mara kwa mara.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Hivi ndivyo maelezo ya utatuzi ya skanisho hii yanatuonyesha:



![nmap-image](assets/fr/64.webp)



matumizi ya usanidi wa `-T4` wakati wa kuchanganua Nmap



### V. Hitimisho



Katika sura hii, tumeangalia mbinu na chaguo mbalimbali unazoweza kutumia ili kudhibiti nguvu, uchokozi na utendakazi wa Nmap. Chaguo hizi ni muhimu sana wakati wa kuchanganua mitandao mikubwa, na mara chache zaidi kwa madhumuni ya siri.



Katika sura inayofuata, tutaangalia mbinu chache bora za kutumia Nmap na kuhakikisha usalama wake.




## 12 - Usalama wa data na usiri unapotumia Nmap



### I. Uwasilishaji



Katika sura hii, tutaangalia mbinu kadhaa nzuri zitakazochukuliwa kuhusiana na usalama na, zaidi ya yote, usiri wa data zinazozalishwa, kuchakatwa na kuhifadhiwa na Nmap.



Matumizi ya Nmap ndani ya mfumo wa habari yanaweza kuainishwa kwa haraka kama kitendo cha kukera. Kwa hivyo, tahadhari kadhaa zinahitajika kuchukuliwa ili kuchukua hatua ndani ya mfumo wa kisheria, huku kikihakikisha usalama wa malengo yaliyokusudiwa, data iliyokusanywa na mfumo unaotumika kwa skanning.



### II. Kupata idhini zinazofaa



Kabla ya kuchanganua mtandao au mfumo, hakikisha umepata uidhinishaji unaofaa. Mifumo ya kuchanganua uwezekano wa kuathiriwa (`hati za NSE`) bila idhini inaweza kuwa kinyume cha sheria, na inaweza kuwa na madhara ya kisheria, hasa ikiwa usalama wa mfumo wa taarifa si sehemu ya kutuma kwako rasmi.





- Kama ukumbusho: [Msimbo wa Adhabu: Sura ya Tatu: Hushambulia mifumo ya kiotomatiki ya kuchakata data](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Inalinda data nyeti



Matokeo yanayotolewa na Nmap yanaweza kuchukuliwa kuwa nyeti, hasa yanapokuwa na taarifa kuhusu udhaifu katika mfumo wa taarifa ambao unaweza kutumiwa na mshambulizi. Lakini pia inapohusu mifumo ambayo haiwezi kufikiwa na kila mtu (k.m. mifumo nyeti, ya viwandani, ya afya au [chelezo] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Tumeona pia kwamba, kulingana na hati za NSE zinazotumiwa, matokeo ya uchunguzi wa NSE ya [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) yanaweza pia kuwa na vitambulishi.



Kwa hivyo, mtu mwenye nia mbaya ambaye ataweza kupata matokeo haya ya skanisho atakuwa na ramani ya mfumo wa habari na habari nyingi za kiufundi, bila kufanya vitendo hivi mwenyewe, kwa hatari ya kugunduliwa.



Kwa hivyo ni muhimu kuwa mwangalifu kutokusanya au kuhifadhi habari nyeti kwa njia isiyofaa unapotumia Nmap, ikijumuisha, lakini sio tu, yafuatayo:





- Usimbaji data ya towe: ikiwa unahitaji kuhifadhi au kusambaza matokeo ya utafutaji wako wa Nmap, hakikisha umeyasimba ili kulinda usiri wa data. Hii itazuia udukuzi usioidhinishwa wa taarifa nyeti. Kwa hakika, data inapaswa kusimbwa kwa njia fiche mara tu inapoondoka kwenye mfumo unaotumika kuchanganua (kumbukumbu ya ZIP iliyosimbwa kwa njia fiche kwa nenosiri dhabiti ni mwanzo mzuri sana).





- Sanidi vidhibiti vya ufikiaji: hakikisha kwamba watu walioidhinishwa pekee ndio wanaoweza kufikia matokeo ya utafutaji wako wa Nmap ambapo yatahifadhiwa. Weka vidhibiti vinavyofaa vya ufikiaji ili kulinda taarifa nyeti dhidi ya ufikiaji usioidhinishwa.





- Kuwa mwangalifu wakati wa kushughulikia data: wakati wa kuhamisha, kunakili au kuchakata data ya kuchanganua, hakikisha kuwa unaweka usalama wa data chini ya udhibiti mkali. Hii inamaanisha: usiziache zikiwa katika saraka ya `Pakua` ya kituo cha kazi kilichounganishwa kwenye Mtandao, usiziruhusu zipitie programu yako ya ndani ya faili ya HTTP Exchange, usiache Notepad yako wazi bila kufunga kituo cha kazi wakati wa mapumziko yako ya chakula cha mchana, n.k.




### IV. Kudhibiti upekuzi mkali



Kama tulivyoona katika somo hili lote, Nmap inaweza kuwa ya kitenzi katika kiwango cha mtandao. Inaweza pia kutuma pakiti ambazo hazijaumbizwa ipasavyo, na ambazo haziheshimu kabisa muundo wa itifaki katika fremu za mtandao na pakiti inazozalisha. Vitendo hivi vyote vinaweza kuwa na athari kwa mifumo na huduma fulani, wakati mwingine hadi kusababisha malfunction au kueneza kwa rasilimali za mfumo na mtandao.



Ili kuepuka matukio yoyote, unahitaji kufahamu tabia ya Nmap na kujua jinsi ya kuirekebisha ili kuendana na muktadha ambamo inatumiwa, kwa kutumia chaguo mbalimbali zilizojadiliwa katika somo hili. Hatutatumia Nmap kwa njia ile ile kwenye mfumo wa taarifa ulio na [vifaa] (https://www.it-connect.fr/actualites/actu-materiel/) kama ilivyo kwa mtandao wa mtumiaji unaoundwa na mifumo ya Windows inayolindwa na ngome ya ndani au katika msingi wa mtandao.



Tunatumahi, masomo mbalimbali katika mafunzo haya yamekufundisha jinsi ya kujua na kuchambua tabia ya Nmap, lakini njia bora ya kujifunza ni kwa kufanya. Kwa hivyo hakikisha kuwa unafahamu chaguo za Nmap utakazotumia.



### V. Kulinda mfumo wa skanning



Katika sura ya kwanza, tuliona kwamba katika hali nyingi, Nmap inahitaji kuendeshwa kama `mzizi` au msimamizi wa ndani. Hii ni kwa sababu hufanya shughuli za mtandao, wakati mwingine kwa kiwango cha chini kabisa, kupitia maktaba za mtandao, ambazo zinahitaji ruhusa za juu na hatari kutoka kwa mtazamo wa uthabiti wa mfumo au usiri wa programu zingine.



Kwa hivyo, Nmap inaweza kuonekana kama sehemu nyeti ya mfumo ambao imesakinishwa. Hakikisha unatumia toleo jipya zaidi la Nmap, kwani matoleo ya zamani yanaweza kuwa na athari za kiusalama zinazojulikana. Kwa kutumia toleo la kisasa, unaweza kupunguza hatari zinazohusiana na kutumia zana.



Ikiwa umechagua kutumia Nmap si kupitia kipindi kama `root`, lakini kwa kutoa haki maalum kwa mtumiaji aliyebahatika ili awe na kila kitu anachohitaji kutumia Nmap (`sudo` au _capabilities_), fahamu kuwa Nmap inaweza kutumika kama sehemu ya mwinuko kamili wa fursa:



![nmap-image](assets/fr/65.webp)



mwinuko wa marupurupu ya Nmap kupitia `sudo`._



Hapa, ninatumia amri ya Nmap kupitia `sudo`, lakini hii inaniruhusu kupata ganda linaloingiliana kama `mzizi` kwenye mfumo, ambalo halikuwa lengo la asili.



Pia haifai sana kusakinisha Nmap kwenye mifumo ambayo haijaundwa kufanya uchanganuzi wa mtandao. Ninafikiria haswa seva au vituo vya kazi. Kwa upande mmoja, hii ingeongeza vekta inayoweza kuinua upendeleo, lakini juu ya yote ingempa mvamizi ufikiaji rahisi wa zana inayokera.



Hatimaye, usalama wa mfumo unaotumiwa kwa skanning lazima uhakikishwe kwa upana zaidi, ili isiwe yenyewe kuwa vector kwa kuingilia au kuvuja habari. Kama msimamizi wa mfumo, ni bora kutumia mfumo maalum, ambao una muda mfupi wa kuishi, badala ya kituo chako cha kazi.



### VI. Hitimisho



Kwa kumalizia, hakikisha umeifahamu vyema Nmap kabla ya kuitumia katika hali halisi ya maisha au uzalishaji, na uwe macho wakati wa kuchakata na kudhibiti matokeo yake. Itakuwa ni huruma kusababisha uharibifu, kuvuja data au kuwezesha maelewano, wakati mbinu ya awali inalenga kuboresha usalama wa kampuni yako.



## 13 - Uchanganuzi wa bandari kupitia TCP: SYN, Unganisha na FIN



### I. Uwasilishaji



Katika sura hii na inayofuata, tutaangalia kwa karibu aina tofauti za TCP scan zinazopatikana katika Nmap, tukianza na zile zinazotumika sana: SYN, Connect na FIN scans.



Kama unaweza kuwa umegundua, Nmap inatoa chaguzi kadhaa kwa skana za TCP:



![nmap-image](assets/fr/66.webp)



mbinu za kuchanganua zinazopatikana katika Nmap._



Wazo hapa ni kuelezea baadhi ya njia hizi, ili kukusaidia kuelewa tofauti zao, faida zao na mapungufu yao. Utaona kwamba, kulingana na muktadha au kile unachotaka kujua, ni bora kuchagua chaguo moja au nyingine.



### II. Uchanganuzi wa TCP SYN au "Uchanganuzi wa Nusu Fungua



Aina ya kwanza ya uchanganuzi wa TCP tutakayoangalia ni `TCP SYN Scan`, pia inajulikana kama `Half Open Scan`. Iwapo unakumbuka uhakiki wa mtandao tuliofanya baada ya ukaguzi wetu wa kwanza kwenye mlango, hii ndiyo aina ya uchanganuzi unaotumiwa kwa chaguomsingi na [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) inapoendeshwa kwa haki za mizizi.



Tafsiri itakusaidia kuelewa jinsi skanning hii inavyofanya kazi. Kwa hakika, kichanganuzi cha TCP SYN kitatuma pakiti ya TCP SYN kwa kila mlango unaolengwa, ambayo ni pakiti ya kwanza kutumwa na mteja (anayeomba kuanzisha muunganisho) kama sehemu ya _Three way handshake_ TCP maarufu. Kwa kawaida, ikiwa lango limefunguliwa kwenye seva inayolengwa, ikiwa na huduma inayoendeshwa nyuma yake, seva itatuma tena pakiti ya TCP SYN/ACK ili kuthibitisha SYN ya mteja na kuanzisha muunganisho wa TCP. Jibu hili litachukua muundo wa pakiti ya TCP iliyo na alama za SYN na ACK zilizowekwa kuwa 1, na kutuwezesha kuthibitisha kuwa mlango umefunguliwa na unaongoza kwa huduma.



Kwa upande mwingine, lango limefungwa, seva itatutumia pakiti ya `TCP` iliyo na alama za RST na ACK zilizowekwa kuwa 1 ili kusimamisha ombi la muunganisho, kwa hivyo tutajua kuwa hakuna huduma inayoonekana kuwa amilifu nyuma ya mlango huu:



![nmap-image](assets/fr/67.webp)



Mchoro wa tabia wa tCP SYN Scan kwa milango iliyo wazi na iliyofungwa



Ili kupata mwonekano kamili wa `TCP SYN Scan`, nilichanganua lango la TCP/80 kwa seva pangishi ambayo ilikuwa na seva ya wavuti inayotumika kwenye mlango huu. Kuchanganua mtandao kwa kutumia Wireshark, tunaweza kuona mtiririko ufuatao (chanzo cha skanisho: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



kunasa mtandao wakati wa kuchanganua TCP SYN kwa mlango wazi



Kwenye mstari wa kwanza, tunaona kwamba chanzo cha kutambaza kinatuma pakiti ya TCP kupangisha `10.10.10.203` kwenye bandari TCP/80. Katika pakiti hii ya TCP, bendera ya SYN imewekwa kuwa 1 ili kuonyesha kuwa hili ni ombi la kuanzisha muunganisho wa TCP.



Kisha, kwenye mstari wa pili, tunaona kwamba lengo linajibu kwa `TCP SYN/ACK`, kumaanisha kwamba inakubali kuanzisha muunganisho na kwa hivyo kupokea mitiririko kwenye bandari TCP/80. Kwa hivyo tunaweza kubaini kuwa bandari TCP/80 imefunguliwa na kwamba seva ya wavuti iko kwenye seva iliyochanganuliwa.



Mwenyeji wetu kisha anarejesha pakiti ya RST ili kufunga muunganisho, na kuruhusu seva pangishi iliyochanganuliwa kutodumisha muunganisho wazi wa TCP akisubiri jibu. Katika kesi ya uchanganuzi kwenye bandari nyingi, kutofunga miunganisho ya TCP kunaweza kusababisha kukataliwa kwa huduma, kujaza idadi ya miunganisho inayosubiri kujibiwa ambayo seva inaweza kudumisha (ona [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



Katika Wireshark, utaweza kuona hali ya alama za TCP kwa kila jaribio tunalofanya. Hii itaonyesha ikiwa pakiti ni SYN, SYN/ACK, ACK, n.k.:



![nmap-image](assets/fr/69.webp)



tazama bendera za TCP za pakiti huko Wireshark (TCP SYN hapa)



Kinyume chake, nilifanya jaribio sawa kati ya mashine hizo mbili, lakini wakati huu nikichanganua mlango wa TCP/81 ambao hakuna huduma inayotumika (chanzo cha skanisho: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



kunasa mtandao wakati wa kuchanganua TCP SYN kwa mlango uliofungwa



Kipangishi kilichochanganuliwa hurejesha `TCP RST/ACK` kwa kujibu `TCP SYN` yangu wakati mlango haujafunguliwa.



Kama ilivyotajwa, wakati wa kuendesha Nmap kutoka kwa terminal iliyobahatika, TCP SYN Scan ndio modi chaguo-msingi, na inaweza kulazimishwa kupitia chaguo la `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




`TCP SYN Scan` ndiyo skanisho inayotumika sana kwa sababu za kasi. Kwa upande mwingine, kushindwa kwa mteja kukamilisha _Three Way Handshake_ (yaani kutotuma ACK baada ya seva SYN/ACK) kunaweza kuonekana kutiliwa shaka kama kutazingatiwa mara nyingi sana kwenye seva au kutoka kwa chanzo sawa kwenye mtandao. Hakika, tabia ya kawaida ya mteja baada ya kupokea pakiti ya TCP SYN/ACK kwa kujibu TCP SYN ni kutuma `kukiri` (ACK) na kisha kuanzisha Exchange.



Walakini, haitoi skana ya haraka zaidi, kwani haisumbui kutuma ACK kwa kila jibu chanya. Faida ya SYN Scan ni kasi yake, kwa kuwa pakiti moja tu inatumwa kwa kila bandari ili kuchunguzwa, kwa gharama ya nafasi kubwa ya kugundua.



Kwa kuongeza, uchunguzi wa TCP SYN unaweza kutambua kama mlango unachujwa (kilindwa) na ngome. Kwa hakika, ngome iliyo mbele ya seva pangishi inayolengwa inaweza kutambuliwa kwa jinsi inavyotenda inapopokea pakiti ya TCP SYN kwenye mlango unaopaswa kulinda. Haitajibu tu. Walakini, kama tulivyoona, katika hali zote mbili (mlango wazi au uliofungwa), kuna jibu kutoka kwa seva pangishi. Tabia hii ya tatu itafichua uwepo wa ngome kati ya seva pangishi iliyochanganuliwa na mashine inayochanganua. Haya ndio matokeo ambayo Nmap inaweza kurudi wakati lango lililochanganuliwa linachujwa na ngome:



![nmap-image](assets/fr/71.webp)



onyesho la nmap wakati wa kuchanganua mlango uliochujwa



Tunaporekodi mtandao wakati wa kuchanganua, tunaweza kuona kwamba hakuna jibu linalotolewa:



![nmap-image](assets/fr/72.webp)



kunasa mtandao wakati wa uchanganuzi wa TCP SYN kwa mlango uliochujwa na ngome



Tofauti kati ya lango lililofungwa na lango lililochujwa ni kama ifuatavyo: lango lililochujwa ni lango lililolindwa na ngome, ilhali lango lililofungwa ni lango ambalo hakuna huduma inayoendeshwa na kwa hivyo haiwezi kuchakata pakiti zetu za TCP. Baadhi ya aina za uchanganuzi wa TCP, kama vile kichanganuzi cha TCP SYN, zinaweza kutambua kama mlango unachujwa, ilhali aina nyinginezo haziwezi.



### III. TCP Connect scan au Full Open scan



Aina ya pili ya uchunguzi wa TCP ni `TCP Connect scan`, inayojulikana pia kama _Full Open Scan_. Inafanya kazi kwa njia sawa na utambazaji wa TCP SYN, lakini wakati huu hurejesha `TCP ACK` baada ya jibu chanya kutoka kwa seva (SYN/ACK). Hii ndiyo sababu inaitwa `Full Open', kwani muunganisho unafunguliwa kikamilifu na kuanzishwa kwenye kila lango linalofunguliwa wakati wa kuchanganua, hivyo basi kuheshimu TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



tCP Connect Scan tabia mchoro kwa milango wazi na kufungwa



Hivi ndivyo vinavyoweza kuonekana ukipitia mtandao wakati wa `TCP Connect scan` inayolenga mlango wazi:



![nmap-image](assets/fr/74.webp)



kunusa mtandao wakati wa kuchanganua TCP Connect kwa mlango wazi



Tunaweza kuona kwamba pakiti ya kwanza ya TCP iliyotumwa ni `TCP SYN` iliyotumwa na mteja, na seva itajibu kwa `TCP SYN/ACK`, ikionyesha kuwa mlango umefunguliwa na unapangisha huduma inayotumika. Ili kuiga mteja halali kila wakati, Nmap itatuma `TCP ACK` kwa seva. Kinyume chake, wakati wa kuchanganua mlango uliofungwa:



![nmap-image](assets/fr/75.webp)



kukamata mtandao wakati wa kuchanganua TCP Connect kwa mlango uliofungwa



Kumbuka kuwa jibu la seva kwa pakiti yetu ya `SYN` kwa mara nyingine tena ni pakiti ya `TCP RST/ACK`, kwa hivyo tunaweza kukisia kuwa lango limefungwa na hakuna huduma zinazoendeshwa juu yake.



Unapotumia Nmap, chaguo `-sT` (`scan Connect`) hutumika kutekeleza Uchanganuzi wa TCP Connect. Tafadhali kumbuka kuwa Nmap inapotumiwa kutoka kwa kikao kisicho na haki, hii ndio hali ya skanati ya TCP chaguo-msingi:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



`TCP Connect Scan` huiga ombi halali zaidi la muunganisho, na tabia inayofanana kwa karibu zaidi na mteja wa lambda, kwa hivyo ni vigumu kutambua uchanganuzi kwenye idadi iliyopunguzwa ya milango. Hata hivyo, ni polepole, kwani inaanzisha kabisa kila muunganisho wa TCP kwenye bandari zilizo wazi za mashine iliyochanganuliwa.



Uchunguzi wa Nmap wa bandari 10,000 bado utaendelea kugunduliwa kwa urahisi ikiwa ugunduzi wa uvamizi wa mtandao na huduma za ulinzi (IDS, IPS, EDR) zimesakinishwa. Mshambulizi anapotaka kuweka wasifu wa chini, ataelekea kuzingatia idadi ndogo ya bandari zilizochaguliwa kimkakati, kama vile 445 (SMB) au 80 (HTTP), ambazo mara nyingi hufunguliwa kwenye seva na kuwasilisha udhaifu wa kawaida.



Kwa kuwa TCP Connect Scan inatarajia jibu katika visa vyote viwili, inaweza pia kutambua uwepo wa ngome ambayo inaweza kuwa inachuja milango kwenye seva pangishi inayolengwa.



### IV. TCP FIN scan au "Stealth Scan



`TCP FIN Scan`, pia inajulikana kama _Stealth Scan_, hutumia tabia ya mteja kuzima muunganisho wa TCP ili kugundua mlango ulio wazi.



Katika TCP, mwisho wa kipindi humaanisha kutuma pakiti ya TCP iliyo na alama ya FIN iliyowekwa kuwa 1. Katika Exchange ya kawaida, seva inasitisha mawasiliano yote na mteja (hakuna jibu). Ikiwa seva haina muunganisho amilifu wa TCP na mteja, itatuma `RST/ACK`. Kwa hivyo tunaweza kutofautisha kati ya milango iliyo wazi na iliyofungwa kwa kutuma pakiti za `TCP FIN` kwa seti ya milango:



![nmap-image](assets/fr/76.webp)



tCP FIN mchoro wa tabia ya kuchanganua kwa bandari zilizo wazi na zilizofungwa



Nilinasa mtandao tena wakati wa _Stealth scan_ na hivi ndivyo unavyoona wakati lango lililochanganuliwa limefunguliwa:



![nmap-image](assets/fr/77.webp)



kunasa mtandao wakati wa kuchanganua TCP FIN kwa mlango wazi



Tunaweza kuona kwamba mteja hutuma pakiti moja au mbili ili kuzima muunganisho wa TCP na kwamba seva haijibu. Inakubali tu mwisho wa muunganisho na inaacha kuwasiliana.



Hivi ndivyo tunaona sasa tunapochanganua mlango uliofungwa:



![nmap-image](assets/fr/78.webp)



kunasa mtandao wakati wa kuchanganua TCP FIN kwa mlango uliofungwa



Tunaona kwamba seva hurejesha pakiti ya `TCP RST/ACK`, kwa hivyo kuna tofauti katika tabia kati ya mlango ulio wazi na uliofungwa, na tunaweza kuorodhesha milango iliyo wazi kwenye seva kwa kutuma pakiti ya TCP FIN. Kwa kutumia Nmap, chaguo la `-sF` (`scan FIN`) linatumika kutekeleza Uchanganuzi wa TCP FIN:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan haifanyi kazi kwenye vipangishi vya Windows, kwa sababu Mfumo wa Uendeshaji huelekea kupuuza pakiti za TCP FIN zinapotumwa kwenye milango ambayo haijafunguliwa. Kwa hivyo ukiendesha TCP FIN Scan kwenye seva pangishi ya Windows, utapata hisia kwamba bandari zote zimefungwa.



Ndiyo maana ni muhimu kufahamu mbinu kadhaa za skanning, na kuelewa tofauti kati yao.



Kwa kuwa kwa vyovyote vile TCP FIN haitasubiri jibu, haitaweza kutambua uwepo wa ngome kati ya seva pangishi inayolengwa na chanzo cha tambazo.



Hapa kuna mfano wa matokeo ya skanisho ya TCP FIN ya Nmap:



![nmap-image](assets/fr/79.webp)



matokeo ya uchunguzi wa TCP FIN na Nmap._



Kwa kweli, jibu lisilo la kawaida kutoka kwa seva pangishi kwenye mlango fulani linaweza kumaanisha kuwa bandari imechujwa, lakini pia ni wazi na inafanya kazi.



Uchanganuzi huu unarejelewa kama "uficho", kwani hausababishi trafiki nyingi kwenye generate na kwa ujumla hausababishi ukataji miti katika mifumo inayolengwa. Inaweza kutumika kugundua bandari kwa busara kwenye mtandao bila kuinua kengele zozote. Walakini, kama ilivyotajwa hapo juu, ufanisi wake unaweza kutofautiana kulingana na mfumo unaolengwa, na vile vile uamuzi wake kulingana na usanidi wa vifaa vya usalama.



### V. Hitimisho



Sana kwa sura ya kwanza kati ya mbili za aina tofauti za uchanganuzi za TCP zinazotolewa na Nmap! Katika sura inayofuata, tutaangalia aina za uchunguzi wa XMAS, Null na ACK TCP, ambazo hufanya kazi kwa njia tofauti ili kugundua milango iliyo wazi kwenye seva pangishi.





## 14 - Uchanganuzi wa bandari kupitia TCP: XMAS, Null na ACK



### I. Uwasilishaji



Katika sehemu hii, tutaendelea kuchunguza mbinu mbalimbali za kuchanganua za TCP zinazotolewa na Nmap. Hapa tutaangalia mbinu za `XMAS`, `Null` na `ACK`, ambazo hutumia vipengele mahususi vya TCP kupata taarifa kwenye bandari na huduma zinazofunguliwa kwa lengo fulani.



### II. TCP XMAS scan



XMAS Scan TCP si ya kawaida kidogo kwa kuwa haiigi tabia ya kawaida ya mtumiaji au mashine kwenye mtandao hata kidogo. Kwa hakika, XMAS Scan itatuma pakiti za TCP zenye bendera `URG` (Haraka), `PSH` (Push), na `FIN` (Maliza) zimewekwa kuwa 1, ili kukwepa ngome fulani au mbinu za kuchuja.



Jina XMAS linatokana na ukweli kwamba kuona bendera hizi kwenye si kawaida. Wakati bendera zote tatu zimewekwa kwa wakati mmoja katika pakiti ya TCP, inaonekana kama mti wa Krismasi uliowaka:



![nmap-image](assets/fr/80.webp)



Bendera za tCP zinazotumika katika uchanganuzi wa XMAS



Bila kuingia kwa undani kuhusu jukumu la bendera hizi hapa, ni muhimu kujua kwamba unapotuma pakiti iliyo na bendera hizi tatu, huduma inayotumika nyuma ya mlango unaolengwa haitarejesha pakiti zozote. Kwa upande mwingine, ikiwa bandari imefungwa, tutapokea pakiti ya TCP RST/ACK. Sasa tutaweza kutofautisha kati ya tabia ya mlango wazi na uliofungwa wakati wa kuorodhesha bandari kwenye mashine:



![nmap-image](assets/fr/81.webp)



Mchoro wa tabia wa tCP XMAS Scan kwa bandari zilizo wazi na zilizofungwa



Bado inafuata mantiki sawa, uchunguzi wa mtandao kwenye mlango wa TCP/80 wa seva pangishi iliyo na seva ya wavuti inayotumika inaonyesha tabia ifuatayo wakati wa kutambua mlango ulio wazi (chanzo cha skani `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



kunasa mtandao wakati wa kuchanganua TCP XMAS kwa mlango wazi



Tunaweza kuona kwamba chanzo cha kuchanganua hutuma pakiti mbili za TCP XMAS (zenye bendera `FIN`, `PSH` na `URG` zimewekwa kuwa 1) ili kupangisha `10.10.10.203` na kwamba hakuna urejeshaji kutoka kwa lengwa, kuonyesha kwamba mlango umefunguliwa. Kinyume chake, wakati wa kutekeleza `TCP XMAS Scan` kwenye mlango uliofungwa, matokeo yafuatayo yanazingatiwa:



![nmap-image](assets/fr/83.webp)



kunasa mtandao wakati wa kuchanganua TCP XMAS kwa mlango uliofungwa



Jibu kwa kifurushi chetu cha TCP basi ni `TCP RST/ACK`, kuonyesha kwamba mlango wa kuingilia umefungwa. Ili kutumia mbinu hii na Nmap, chaguo `-sX` (`changanua XMAS`) hukuruhusu kutekeleza Uchanganuzi wa TCP XMAS:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Ni muhimu kutambua kuwa kichanganuzi cha TCP XMAS hakiwezi kutambua ngome ambazo zinaweza kuwa kati ya lengwa na mashine ya kuchanganua, tofauti na aina zingine za uchanganuzi kama vile TCP SYN au Unganisha. Hakika, ngome inayotumika kati ya wapangishaji wawili itahakikisha kuwa hakuna urejeshaji wa TCP unaofanywa ikiwa mlango unaolengwa unachujwa (yaani, kulindwa na ngome). Katika tukio la kutojibu, kwa hiyo haiwezekani kujua ikiwa bandari inalindwa na firewall au wazi na hai. Unapaswa pia kufahamu kwamba, kama vile TCP FIN scan, baadhi ya programu au mifumo ya uendeshaji kama vile Windows inaweza kupotosha matokeo ya aina hii ya scan.



kumbuka: usaidizi wa uchanganuzi wa XMAS/FIN/NULL kwenye matoleo ya hivi majuzi ya Windows unasalia kuwa mdogo, na matokeo yanaweza kutofautiana kwenye aina hii ya lengo. (Sasisho 2025)_



### III. TCP Null Scan



Kinyume na uchanganuzi wa TCP XMAS, TCP Null scan itatuma pakiti za kuchanganua za TCP na alama zote zimewekwa kuwa 0. Hii pia ni tabia ambayo haitapatikana kamwe katika Exchange ya kawaida kati ya mashine, kwani kutuma pakiti ya TCP bila bendera haijabainishwa katika RFC inayoelezea itifaki ya TCP. Hii ndiyo sababu inaweza kugunduliwa kwa urahisi zaidi.



Kama vile kichanganuzi cha TCP XMAS, uchanganuzi huu unaweza kutatiza ngome fulani au moduli za kuchuja, na kuruhusu pakiti kupita:



![nmap-image](assets/fr/84.webp)



Mchoro wa tabia wa tCP Null Scan kwa bandari zilizo wazi na zilizofungwa



Hapa kuna kile kinachoweza kuonekana kwenye mtandao wakati wa skanati ya TCP Null kwenye bandari iliyo wazi:



![nmap-image](assets/fr/85.webp)



kukamata mtandao wakati wa utaftaji wa Null wa TCP kwa mlango wazi



Mashine ya kuchanganua hutuma pakiti isiyo na alama (`[<None>]` katika Wireshark) bila jibu lolote kutoka kwa seva. Kinyume chake, wakati bandari inayolengwa imefungwa:



![nmap-image](assets/fr/86.webp)



kunasa mtandao wakati wa utaftaji wa Null wa TCP kwa mlango uliofungwa



Ili kufanya uchanganuzi wa Null wa TCP na Nmap, tumia tu chaguo la `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Kwa kuwa jibu lango limefunguliwa na ngome inapotumika (hakuna maoni ya seva katika hali zote mbili) ni sawa, TCP Null scan haiwezi kutambua kuwepo kwa ngome. Zaidi ya hayo, ngome inaweza hata kupotosha matokeo kwa kupendekeza kuwa lango limefunguliwa, kwa kuwa haijibu pakiti za TCP bila bendera, ingawa bandari imechujwa. Haya ni maelezo muhimu kufahamu unapotumia michanganuo ambayo haiwezi kutofautisha lango lililo wazi na lililochujwa (lililolindwa na ngome), kama vile `TCP Null`, `XMAS` au `FIN` scans, ili kusalia sawa katika tafsiri ya matokeo yaliyopatikana.



### IV. TCP ACK Scan



Uchanganuzi wa TCP ACK hutumiwa kutambua uwepo wa ngome kwenye seva pangishi inayolengwa au kati ya lengwa na chanzo cha tambazo.



Tofauti na utafutaji mwingine, uchunguzi wa TCP ACK haujaribu kutambua ni milango ipi iliyofunguliwa kwenye seva pangishi, lakini kama mfumo wa uchujaji unatumika, unaojibu kwa kila mlango kwa `kuchujwa` au `hakuchujwa`. Baadhi ya uchunguzi wa TCP, kama vile `TCP SYN` au `TCP Connect`, unaweza kufanya zote mbili kwa wakati mmoja, ilhali zingine, kama vile `TCP FIN` au `TCP XMAS`, haziwezi kubainisha uwepo wa uchujaji hata kidogo. Hii ndio sababu skanisho ya TCP ACK inaweza kuwa muhimu:



![nmap-image](assets/fr/87.webp)



tCP ACK Changanua mchoro wa tabia kwa milango iliyochujwa na ambayo haijachujwa



Tutatumia chaguo la `-sA` la Nmap kutekeleza aina hii ya uchanganuzi. Haya ndiyo matokeo ya uchunguzi wa TCP ACK ikiwa lango limechujwa, i.e. limezuiwa na kulindwa na ngome:



![nmap-image](assets/fr/88.webp)



onyesho la nmap wakati TCP ACK Scan._



Mfano wa matokeo kwa mwenyeji aliye na ngome na moja bila. Nmap hurejesha `iliyochujwa` kwenye milango TCP/80 na TCP/81 ya seva pangishi `10.10.10.203`. Kwenye uchanganuzi wa mtandao kupitia Wireshark, tabia ni kama ifuatavyo.



![nmap-image](assets/fr/89.webp)



kunasa mtandao wakati wa uchanganuzi wa TCP ACK kwa mlango ambao haujachujwa na ngome



Mashine inayolengwa hairudishi chochote ikiwa ngome iko.



Ili kuzindua uchanganuzi huu na Nmap, tumia chaguo la `-sA` (`changanua ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Hitimisho



Tumeangalia mbinu tatu tofauti za kuchanganua kupitia TCP pamoja na zile ambazo tayari zimewasilishwa. Mbinu hizi tofauti zitatumika katika hali na miktadha mahususi, haswa katika muktadha wa majaribio ya kupenya au utendakazi wa Timu Nyekundu, wakati ambapo mawazo ya busara yanakuwepo.



## 15 - Nmap CheatSheet - Muhtasari wa maagizo ya mafunzo



### I. Uwasilishaji



Huu hapa ni muhtasari mfupi wa amri nyingi za Nmap na kesi za matumizi, ili uweze kuzipata kwa haraka na kuzitumia tena katika matumizi ya kila siku.



### II. Nmap: CheatSheet IT-Connect



Hapa kuna cheatsheet ya amri iliyotolewa. Ukurasa huu hurahisisha kupata matumizi ya kawaida ya Nmap.





- Uchanganuzi wa bandari




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Inagundua wapangishi wanaoendelea




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



kumbuka: Chaguo la `-sP` limepitwa na wakati kwa miaka kadhaa na linapaswa kubadilishwa na `-sn`. (Sasisho 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Utambuzi wa toleo




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- Maandishi ya NSE: kutafuta udhaifu




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Usimamizi wa matokeo ya Nmap




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Uboreshaji wa utendaji




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Aina za skanisho za TCP




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Natumaini kupata amri hizi kuwa muhimu. Usisahau kurekebisha shabaha ya uchanganuzi wako kwa muktadha wako na kurejelea hati rasmi ili kudhibiti kikamilifu majaribio yaliyofanywa.



### III. Hitimisho



Mafunzo ya Nmap sasa yamekamilika. Sasa una mambo ya msingi unayohitaji kutumia zana hii ya kina na yenye nguvu. Tunakushauri sana kufanya mazoezi kwenye mazingira yanayodhibitiwa (Hack The Box, VulnHub, mashine pepe) kabla ya kuitumia katika uzalishaji.



Mengi yanasalia kuchunguzwa kuhusu utendaji kazi wa ndani wa chombo na vipengele vya juu. Hata hivyo, umilisi wa amri na dhana zilizowasilishwa hapa zitakuwezesha kutumia Nmap kwa kujiamini na umuhimu.