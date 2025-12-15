---
name: Imishingi y'ikoranabuhanga rya kriptografiya rya none
goal: Intangamarara y’ivy’ubuhinga n’imigenzo y’ubuhinga bwo gukingira amakuru.
objectives:
- Gutohoza amajambo y’ibanga ya Beale n’uburyo bwo gukora amakuru y’ubuhinga bwa none kugira ngo utahure ivyiyumviro vy’ishimikiro n’ivy’amateka vy’ubuhinga bwo gukora amakuru.
- Injira mu vyiyumviro vy’imibare, imigwi, n’ivyigwa kugira ngo umenye neza ivyiyumviro nyamukuru vy’imibare bishingiye ku buhinga bwo gukingira amakuru.
- Iga RC4 stream cipher na AES n’urufunguzo rw’ibice 128 kugira ngo umenye ivyerekeye ubuhinga bwo gukingira amakuru buhuye.
- Itohoza ry’ubuhinga bwa RSA, ugukwirakwiza urufunguzo, n’ibikorwa vya Hash kugira ngo utohoze ubuhinga bwo gukingira butaringaniye.
---
# Kwibandanya mu buryo bw'inyuma bwo gushira ibanga

Muri iki gisomo, tuzasuzuma ibintu by'ingenzi by'uburyo bw'inyuma bwo gushira ibanga mu buryo busobanutse kandi bworoshye, nta mahugurwa akomeye y'imibare akenewe. Mu bice byose, uziga ibitekerezo ngenderwako nko gushira ibanga ku buryo bw'urufunguzo rumwe n'urw'abantu, imikorere ya hash, umukono wa digitale, guhanahana urufunguzo, n'amahame y'ukuri. Mu nzira, tuzahuza utudomo ku bikorwa bifatika nko kohereza ubutumwa bwizewe, TLS, kubika ijambo ry'ibanga, no kwemeza umwirondoro.

Ibikubiye mu gisomo byateguwe abiga ku rwego rwose kandi biringaniza ubwenge hamwe n'ubujyakuzimu buhagije bwo guhaza amatsiko. Teganya urugendo rwibanze kandi rushimishije. Igihe kirangiye, uzumva uburyo n'impamvu uburyo bw'inyuma bwo gushira ibanga bukora n'uko ubukoresha mu buryo bwizewe.
+++
# Imenyekanisha

<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>


## Incamake y'amashure

<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Murakaze mu nyigisho ya CYP302!


Iki gitabu kiratanga intangamarara yimbitse ku buhinga n’imigenzo y’ubuhinga bwo gukingira amakuru. Aho bishoboka ryibanda ku vyiyumviro, aho kwibanda ku gusobanura ibintu mu buryo bubereye.


Ivyo birimwo inyigisho vyakuwe mu gitabu no mu gitabu c’ububiko [JWBurgers](https://github.com/JWBurgers/Intangamarara_y’Ivy’Ivy’Imibano). Naho umwanditsi yayo yemeye ku buntu ko ikoreshwa mu vy’inyigisho, uburenganzira bwose bw’ubwenge buraguma ku muremyi w’intango.


**Iciyumviro n'intumbero**


Biragoye kuronka ibikoresho vyinshi bitanga ikibanza ciza co hagati mu nyigisho y’ubuhinga bwo gukingira amakuru.


Ku ruhande rumwe, hariho ibitabu birebire kandi bimenyerewe, mu vy’ukuri bishobora gushikirwa gusa n’abafise ubumenyi bukomeye mu vy’imibare, mu vy’ubwenge canke mu yindi nyigisho izwi. Ku rundi ruhande, hariho intangamarara zo ku rugero rwo hejuru cane zihisha vy’ukuri ibintu vyinshi cane ku muntu wese afise n’imiburiburi ugushaka kumenya.


Iyi ntangamarara y’ubuhinga bwo gukingira amakuru irondera gufata ahantu hagati. Naho vyoba bigoye kandi bifise ido n’ido ku muntu wese mushasha mu vy’ubuhinga bwo gupfuka amakuru, si co kinogo c’inkwavu c’igitabu c’ishimikiro gisanzwe.



**Abateze amatwi**


Kuva ku bahinga gushika ku bashaka kumenya vyinshi, iki gitabu ni ngirakamaro ku muntu wese yipfuza ibirenze ugutahura kw’imbere kw’ivy’ubuhinga bwo gukingira amakuru. Nimba intumbero yawe ari ukumenya neza ivy’ubuhinga bwo gukingira amakuru, rero iki gitabu na co nyene ni intango nziza.



**Ingingo ngenderwako zo gusoma**


Ubu ico gitabu kirimwo ibice indwi: "Cryptography ni iki?" (Igice ca 1), "Ishingiro ry'Imibare ry'Ivy'Imibare I" (Igice ca 2), "Ishingiro ry'Imibare ry'Imibare II" (Igice ca 3), "Imibare y'Imibare" (Igice ca 4), "RC4 na AES" (Igice ca 5), ​​"Imibare y'Imibare" (Igice ca 6), "Imibare y'Imibare" (Igice ca 6). Ikigabane ca nyuma, "Ivy'ugushiramwo amakuru mu bikorwa", kizoguma congereweko. Ishimikiye cane ku bikorwa bitandukanye vy’ubuhinga bwa none, harimwo umutekano wo gutwara Layer, inzira y’ibitunguru, n’agaciro ka Bitcoin Exchange.


Keretse iyo ufise ubumenyi bukomeye mu vy’imibare, birashoboka ko inyigisho y’imibare ari yo nsiguro igoye kuruta izindi zose muri iki gitabu. Ndatanga icegeranyo cavyo mu kigabane ca 3, kandi biraboneka no mu gusobanura AES mu kigabane ca 5 na RSA cryptosystem mu kigabane ca 7.


Nimba vy’ukuri uriko urashikirwa n’ingorane z’ibintu vy’ido n’ido biri muri ivyo bice vy’igitabu, ndagusavye ko wovyishimira ku rugero rwo hejuru igihe uzoba uriko urabisoma ubwa mbere.



**Ivyo gushimira**


Igitabo cakoze cane mu guhingura iki ni igitabu ca Jonathan Katz na Yehuda Lindell, Ikinyamakuru CRC (Boca Raton, FL), 2015.


Amasoko nyamukuru y’inyongera yafashije mu kurema icegeranyo kiri muri iki gitabu ni Simon Singh, _Igitabo c’Itegeko_, Igihugu ca kane (Londres, 1999); Christof Paar na Jan Pelzl, _Gutahura ubuhinga bwo gupfuka amakuru_, Springer (Heidelberg, 2010) na [inyigisho ishingiye ku gitabu ca Paar citwa “Intango y’ubuhinga bwo gupfuka amakuru”] na Bruce Schneier, Ivy’Ikoranabuhanga ry’Ivy’Imibano, Igitabo ca 2, 2015 (Indianapolis, IN: John Wiley n’Abahungu Biwe).


Nzovuga gusa amakuru yihariye cane n’ivyavuyemwo nkura muri izo nzira, ariko nshaka kwemera umwenda rusangi mfise kuri zo hano.


Ku basomyi bipfuza kurondera ubumenyi buteye imbere ku bijanye n’ubuhinga bwo gupfuka amakuru inyuma y’iyi ntangamarara, ndabahimiriza cane igitabu ca Katz na Lindell. Ivyigwa vya Katz kuri Coursera birashoboka cane kuruta igitabu.



**Impano**


Turagusavye urabe [dosiye y'intererano iri mu bubiko](https://github.com/JWBurgers/Intango_y'Ivy'Igitabu/blob/master/Intererano.md) kugira ngo ubone amabwirizwa amwamwe yerekeye ingene woshigikira umugambi.



**Ikimenyetso**


**Amajambo nyamukuru:**


Amajambo nyamukuru ari mu bitabu vy’intango aratanguzwa mu kuyagira amajambo ateye ubwoba. Nk’akarorero, ugushiraho ijambo ry’ibanga rya Rijndael nk’ijambo ry’ingenzi vyosa n’ibi bikurikira: **Ijambo ry’ibanga rya Rijndael**.


Amajambo nyamukuru arasobanurwa neza, kiretse iyo ari amazina bwite canke insobanuro yayo igaragara mu kiganiro.


Insobanuro iyo ari yo yose akenshi itangwa iyo umuntu ashizeho ijambo ry’ingenzi, naho rimwe na rimwe vyoba vyiza umuntu asiga iyo nsobanuro gushika mu yindi nkuru.



**Amajambo n'amajambo ashimikiyeko:**


Amajambo n’imirongo birashimikwako biciye ku nyuguti zisongoye. Nk'akarorero, ijambo "Ibuka ijambobanga ryawe" ryoba risa n'iri: *Ibuka ijambobanga ryawe*.



**Inyandiko isanzwe:**


Ivyanditswe bimenyerewe ahanini vyerekeye ibihinduka, ibihinduka bitari vyo, n'imigwi.



- Ibihinduka: Ivyo akenshi vyerekanywe n'urudome ruto (nk'akarorero, "x" canke "y"). Rimwe na rimwe zicandikwa n'inyuguti nini kugira ngo zisobanuke neza (nk'akarorero, "M" canke "K").
- Ibihinduka bitari vyo: Ivyo vyama vyerekanywe n'inyuguti nini (nk'akarorero, "X" canke "Y")
- Ivyiyumviro: Ivyo vyama vyerekanywe n'inyuguti zikomeye, zikomeye (nk'akarorero, **S**)


Ni mwiteguye gutohoza isi iryoshe cane y’ubuhinga bwo gukingira amakuru? Reka tugende!


# Ivy’ugushiramwo amakuru ni iki?

<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>


## Ivyanditswe vya Beale

<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>


Reka dutangure itohoza ryacu ku bijanye n’ubuhinga bwo gukingira amakuru n’ikimwe mu bice biteye umunezero kandi biteye umunezero mu mateka yavyo: ivy’amabanga ya Beale. [1]


Inkuru y’aba Beale ciphers, mu vyiyumviro vyanje, ishobora kuba ari inkuru y’ibinyoma kuruta uko ari ukuri. Ariko ngo vyaciye bigenda gutya.


Mu rushana rwo mu 1820 no mu 1822, umugabo yitwa Thomas J. Beale yaraye mu nzu y’abashitsi yari iya Robert Morriss i Lynchburg (muri Virginie). Beale amaze guhera igihe ca kabiri, yarahaye Morriss agasandugu k’icuma karimwo impapuro z’agaciro zo kubika.


Haciye amezi makeyi, Morriss yararonse ikete ryavuye kuri Beale ryo ku wa 9 Rusama 1822. Ryashimikiye cane ku gaciro kanini k’ibintu vyari muri ako gasandugu k’icuma, rikaba ribwira Morriss amabwirizwa amwamwe: nimba Beale canke uwo ari we wese mu bo bari kumwe na we yigeze aza gusaba ako gasandugu, yari akwiye kurifungura neza na neza kuva ku wa Rusama is the ten of 1822. 1832). Zimwe mu mpapuro zari muri iyo mpapuro zoba zanditswe mu nyandiko zisanzwe. Ariko rero, izindi zitari nke zoba “zitashobora gutahurwa ata mfashanyo y’urufunguzo.” Uwo “rufunguzo” rero woshikirijwe Morriss n’umugenzi wa Beale atavuzwe izina muri Ruheshi 1832.


Naho Morriss yari afise amabwirizwa asobanutse, ntiyafunguye ako gasandugu muri Rusama 1832 kandi umugenzi wa Beale w’akabanga ntiyigeze aza muri Ruheshi uwo mwaka. Mu 1845 ni ho uwo nyen’inzu y’abashitsi amaherezo yafata ingingo yo gufungura iyo sandugu. Muri iyo nkuru, Morriss yasanze aka gatabo kasigura ingene Beale n’abo bari kumwe bavumbuye inzahabu n’ifeza hanze y’Uburengero maze bakabihamba, hamwe n’amabuye y’agaciro amwamwe, kugira ngo babizigame. Ikindi, ako gasandugu karimwo **inyandiko zitatu z’ibanga**: ni ukuvuga inyandiko zanditswe muri kode zisaba **urufunguzo rw’ibanga**, canke ibanga, n’ubuhinga bujana n’ivyo kugira ngo zifungurwe. Uwo murongo wo gufungura inyandiko y’ibanga uzwi nka **decryption**, mu gihe uburyo bwo gufunga buzwi nka **encryption**. (Nk'uko vyasiguwe mu kigabane ca 3, ijambo cipher rishobora gufata insobanuro zitandukanye. Mw'izina "Beale ciphers", ni insiguro ngufi y'ivyanditswe vy'ibanga.)


Ivyo vyanditswe bitatu vy’ibanga Morriss yasanze mu gasandugu k’icuma, kimwe cose gifise urutonde rw’imibare itandukanijwe n’ibimenyetso vy’inyuguti. Dukurikije ivyo Beale yanditse, ivyo bitabo vy’ubuhinga bwa none biratanga ukwavyo aho iryo tunga ryari riri, ibirimwo, be n’urutonde rw’amazina afise uburenganzira bwo kuragwa iryo tunga n’imigabane yabo (ayo makuru ya nyuma akaba ari ngirakamaro mu gihe Beale n’abo bari kumwe boba batigeze baza gusaba iyo sandugu).


Morris yaragerageje gusobanura amajambo atatu y’ibanga mu myaka mirongo ibiri. Ivyo vyari kuba vyoroshe iyo umuntu afise urufunguruzo. Ariko Morriss ntiyari afise urufunguzo kandi ntiyashoboye kugerageza gusubira kuronka ivyanditswe vy’intango, canke **ivyanditswe vy’intango** nk’uko vyitwa mu buryo busanzwe mu vy’ubuhinga bwo gupfuka amakuru.


Morriss yari hafi gupfa, iyo sandugu yarayihaye umugenzi wiwe mu 1862. Uwo mugenzi wiwe yaciye asohora agatabu mu 1885, yitwa J.B. Ward. Yarimwo insobanuro y’amateka (avugwa) y’ico kigega, ivyanditswe bitatu vy’ibanga, be n’umuti yari yararonse ku nyandiko ya kabiri y’ibanga. (Ibiboneka ko hariho urufunguzo rumwe ku nyandiko imwe imwe yose y’ibanga, kandi nta rufunguzo rumwe rukora ku nyandiko zose zitatu z’ibanga nk’uko Beale asa n’uwabivuze mu ntango mw’ikete yandikiye Morriss.)


Ushobora kubona igisomwa ca kabiri c'ibanga mu *Ishusho ya 2* iri musi. [2] Urufunguzo rw’ico gitabu c’ibanga ni Itangazo ry’Ukwikukira kwa Leta Zunze Ubumwe za Amerika. Uburyo bwo gukuraho amakuru buva ku gukurikiza aya mategeko abiri akurikira:



- Ku mubare uwo ari wo wose n uri mu nyandiko y’ibanga, nurondere ijambo rya n mu Itangazo ry’Ukwikukira kwa Leta Zunze Ubumwe za Amerika .
- Subiriza umubare n urudome rwa mbere rw'ijambo wabonye



*Ishusho ya 1: Igiharuro ca Beale no. 2*


![Figure 1: Beale cipher no 2.](assets/en/001.webp "Figure 1: Beale cipher no. 2")



Nk’akarorero, igiharuro ca mbere c’inyandiko ya kabiri y’ibanga ni 115. Ijambo rya 115 ryo mu Itangazo ry’Ukwikukira ni “rashinzwe,” rero urudome rwa mbere rw’inyandiko y’ibanga ni “i.” Ivyo bitabo ntivyerekana ata guca ku ruhande ikibanza kiri hagati y’amajambo n’inyuguti nini. Ariko umaze gusobanura amajambo makeyi ya mbere, urashobora guca ubona mu buryo bubereye yuko ijambo rya mbere ryo mu nyandiko yoroshe ryari “jewe” gusa. (Ico canditswe gitomoye gitangura n’amajambo ngo “Nashize amahera mu ntara ya Bedford.”)


Inyuma y’ugusobanura, ubutumwa bwa kabiri buratanga ido n’ido ry’ibintu biri muri ubwo butunzi (inzahabu, ifeza n’amabuye y’agaciro), kandi bukaba buvuga ko bwahambwe mu nkono z’icuma kandi bugapfukwa n’ibitandara mu ntara ya Bedford (Virginia). Abantu barakunda akabanga keza, ni co gituma hagizwe utwigoro twinshi two gusobanura izindi nkuru zibiri za Beale, canecane iyo idondora aho iryo tunga riri. Mbere n’abahinga mu vy’ubuhinga bwa none batandukanye baragerageje kubikorako. Ariko rero, gushika ubu, nta n’umwe yashoboye gusobanura ibindi vyanditswe bibiri vy’ibanga.



**Ivyiyumviro:**


[1] Kugira ngo ubone incamake nziza y’iyo nkuru, raba Simon Singh, *Igitabo c’Itegeko*, Igihugu ca kane (Londres, 1999), urupapuro rwa 82-99. Sinema ngufi y’iyo nkuru yakozwe na Andrew Allen mu 2010. Ushobora gusanga iyo filime, “Igitabu ca Thomas Beale,” [ku rubuga rwayo](http://www.thomasbealecipher.com/).


[2] Iyi shusho iri kuri paji ya Wikipedia ku bijanye n’ibiharuro vya Beale.



## Ubuhinga bwa none

<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>


Inkuru z’amabara nk’izo mu binyamakuru vya Beale ni vyo benshi muri twebwe twifatanya n’ubuhinga bwo gukingira amakuru. Yamara, ubuhinga bwo gupfuka amakuru bwo muri iki gihe buratandukanye n’ubwo bwoko bw’ingero z’akahise n’imiburiburi mu buryo bune buhambaye.


Ica mbere, mu mateka, ubuhinga bwo gukora amakuru y’ibanga bwari bujanye n’ibanga gusa (canke ibanga). [3] Ivyanditswe vy’ibanga vyoremwa kugira ngo abantu bamwebamwe bonyene bashobore kumenya amakuru ari mu vyanditswe vy’ibanga, nk’uko vyari vyifashe ku nyandiko z’ibanga za Beale. Kugira ngo umugambi wo gushiramwo amakuru ushobore gukora neza iyo ntumbero, gufungura amakuru y’ibanga bikwiye gushoboka gusa iyo ufise urufunguzo.


Ivy’ubuhinga bwa none vy’ugushiramwo amakuru y’ibanga vyerekeye insanganyamatsiko nyinshi kuruta ibanga gusa. Izo nsiguro zirimwo ahanini (1) **ubutungane bw’ubutumwa**—ni ukuvuga kwizera ko ubutumwa butahinduwe; (2) **ukuri kw’ubutumwa**—ni ukuvuga kwizigira ko ubutumwa bwavuye vy’ukuri ku muntu kanaka; na (3) **ukutavyihoza**—ni ukuvuga kwizeza ko uwurungitse ubutumwa adashobora guhakana mu binyoma mu nyuma ko yohereje ubutumwa. [4]


Itandukaniro rihambaye ryo kuguma mu muzirikanyi ni, rero, hagati ya **umugambi wo gushiramwo amakuru** n’**umugambi wo gushiramwo amakuru**. Igishushanyo co gushiramwo amakuru y’ibanga kijanye n’ibanga gusa. Naho umugambi wo gupfuka ari umugambi wo gupfuka, ikinyuranyo si co. Igishushanyo c’ubuhinga bwo gukingira amakuru gishobora kandi gufasha izindi nsanganyamatsiko nyamukuru z’ubuhinga bwo gukingira amakuru, harimwo ubunyankamugayo, ukuri, n’ukudahakana.


Insanganyamatsiko z’ubunyankamugayo n’ukuri zirahambaye nk’uko nyene ibanga rihambaye. Uburyo bwacu bwo guhanahana amakuru bwo muri iki gihe ntibwoshobora gukora ata n’ivyemezo ku bijanye n’ubunyankamugayo n’ukuri kw’ivy’itumanaho. Kudahakana na vyo nyene ni ikintu gihambaye, nk’amasezerano y’ubuhinga bwa none, ariko ntibikenewe cane mu bikorwa vy’ubuhinga bwa none kuruta ibanga, ubunyankamugayo, n’ukuri.


Ubwa kabiri, imigambi ya kera yo gupfuka amakuru nk'iyo Beale ciphers yama irimwo urufunguzo rumwe rwasangiwe n'ababifisemwo uruhara bose. Ariko rero, imigambi myinshi y'ubuhinga bwa none y'ubuhinga bwa none ntikoresha urufunguzo rumwe gusa, ahubwo rufise urufunguzo rubiri: **urufunguzo rw'ibanga** n'**urufunguzo rwa bose**. Naho ivya mbere bikwiye kuguma ari ivy'ibanga mu bikorwa vyose, ivya nyuma ni ubumenyi bwa bose (ni co gituma, amazina yabo). Mu bijanye n'ugupfuka, urufunguzo rwa bose rurashobora gukoreshwa mu gupfuka ubutumwa, mu gihe urufunguzo rw'ibanga rushobora gukoreshwa mu gufungura.


Ishami ry’ubuhinga bwo gukingira amakuru rikorana n’imigambi aho abafise uruhara bose basangira urufunguzo rumwe rizwi nka **ubuhinga bwo gukingira amakuru buringaniye**. Urufunguzo rumwe muri uwo mugambi akenshi rwitwa **urufunguzo rw’ibanga** (canke urufunguzo rw’ibanga). Ishami ry'ubuhinga bwo gukingira amakuru rikorana n'imigambi isaba urufunguzo rw'ibanga n'urwa bose rizwi nka **ubuhinga bwo gukingira amakuru butaringaniye**. Aya mashami rimwe na rimwe yitwa kandi **urufunguzo rw’ibanga** na **urufunguzo rwa bose**, uko bigenda (naho ivyo bishobora gutuma habaho urujijo, kuko imigambi y’urufunguzo rwa bose na yo nyene ifise urufunguzo rw’ibanga).


Kuza kw’ubuhinga bwo gukingira amakuru atagira aho bugarukira mu mpera z’imyaka ya 1970, ni kimwe mu bintu bihambaye cane vyabaye mu mateka y’ubuhinga bwo gukingira amakuru. Iyo itabaho, ubuhinga bwacu bwinshi bwo guhanahana amakuru bwo muri iki gihe, harimwo na Bitcoin, ntibwoshoboka, canke n’imiburiburi ntibwoba bushoboka cane.


Igihambaye ni uko ubuhinga bwo gukingira amakuru bwo muri iki gihe atari inyigisho gusa y’imigambi y’ubuhinga bwo gukingira amakuru y’ingenzi (naho ivyo bifata igice kinini c’ivyo). Nk’akarorero, ubuhinga bwo gukingira amakuru burareba kandi ibikorwa vya Hash be n’ibikoresho bitanga imibare y’ibinyoma, kandi urashobora kwubaka ibikorwa kuri ivyo bikoresho vya kera bitajanye n’ubuhinga bwo gukingira amakuru y’urufunguzo rw’urufunguzo ruringaniye canke rudahuye.


Ica gatatu, imigambi ya kera yo gushiramwo amakuru, nk’iyo yakoreshwa mu bitabu vya Beale, yari ubuhinga kuruta ubuhinga. Umutekano bari babona wari ushingiye ahanini ku vyo babona mu mutima ku bijanye n’ukuntu vyari bikomeye. Mu bisanzwe, vyoba vyarashizweko amabara iyo umuntu amenye ko hari igitero gishasha co kubatera, canke bikakurwaho burundu iyo igitero cari gikomeye cane. Ariko rero, ubuhinga bwo gupfuka amakuru bwo muri iki gihe ni ubuhinga bukomeye bufise uburyo busanzwe, bushingiye ku mibare bwo gutegura no gusuzuma imigambi y’ubuhinga bwo gupfuka amakuru. [5]


Mu buryo bwihariye, ubuhinga bwa none bwo gukingira amakuru bushingiye ku **bimenyamenya vy’umutekano** bimenyerewe. Ikimenyamenya cose c’umutekano w’umugambi w’ubuhinga bwo gukingira amakuru gica mu ntambwe zitatu:


1. Invugo y’**insobanuro y’umutekano mu buryo bw’ibanga**, ni ukuvuga urutonde rw’intumbero z’umutekano n’akaga gaterwa n’uwutera.

2. Invugo y’ivyiyumviro vyose vy’imibare ku bijanye n’uburemere bw’imibare bw’umugambi. Nk’akarorero, umugambi wo gukingira amakuru woshobora kubamwo umubare w’ibinyoma. Naho tutashobora kwemeza ko ivyo biriho, turashobora kwiyumvira ko biriho.

3. Gusobanura **ikimenyamenya c’umutekano** c’umugambi gishingiye ku ciyumviro gisanzwe c’umutekano n’ivyiyumviro vyose vy’imibare.


Ica kane, naho mu mateka ubuhinga bwo gukingira amakuru bwakoreshwa canecane mu bikorwa vy’igisirikare, bwaje gushika mu bikorwa vyacu vya misi yose mu gihe c’ubuhinga bwa none. Waba uriko urakoresha banki kuri internet, ushira ku mbuga ngurukanabumenyi, ugura ikintu kuri Amazon ukoresheje ikarita yawe y’inguzanyo, canke utanga amahera y’umugenzi Bitcoin, cryptography ni sine qua non y’iki gihe cacu c’ubuhinga bwa none.


Hakurikijwe iyo mice ine y’ubuhinga bwa none bwo gukingira amakuru, twoshobora gutanga ibimenyetso vy’ubuhinga bwa none **ubuhinga bwo gukingira amakuru** nk’ubuhinga bujanye n’ugutegura no gusuzuma imigambi y’ubuhinga bwa none kugira ngo amakuru y’ubuhinga bwa none akingirwe ibitero vy’abansi. [6] Umutekano aha ukwiye gutahurwa cane nk’ugukingira ibitero vyonona ibanga, ubutungane, ukwemeza, n’/canke ukudahakana mu guhanahana amakuru.


Cryptography ibonwa neza nk’igice c’ubuhinga bwa **cybersecurity**, kikaba kijejwe gukingira ubusuma, kwonona no gukoresha nabi ubuhinga bwa mudasobwa. Zirikana ko ivyiyumviro vyinshi bijanye n’umutekano wo kuri Internet bifitaniye isano ritoyi canke bifitaniye isano ritoyi gusa n’ubuhinga bwo gukingira amakuru.


Nk’akarorero, nimba ishirahamwe rifise amaserver azimvye mu karere kacu, ryoshobora kwitwararika gukingira ivyo bikoresho kugira ngo ntivyibwe canke ngo vyononekare. Naho ivyo ari ikibazo c’umutekano wo kuri internet, ntaco bihuriyeko n’ubuhinga bwo gukingira amakuru.


Nk’akarorero, **ibitero vy’ubuhendanyi** ni ingorane isanzwe mu bihe vyacu vya none. Ivyo bitero bigerageza guhenda abantu biciye kuri e-mail canke ubundi buryo bwo gutanga ubutumwa kugira ngo bahebe amakuru y’agaciro nk’amajambo y’ibanga canke inomero z’ikarata y’inguzanyo. Naho ubuhinga bwo gukingira amakuru bushobora gufasha ibitero vy’ubuhendanyi vya Address ku rugero runaka, uburyo bwo gukora ibintu vyose busaba ibirenze gukoresha ubuhinga bumwebumwe bwo gukingira amakuru.



**Ivyiyumviro:**


[3] Kugira ngo tuvuge ukuri, ibikorwa bihambaye vy’imigambi y’ubuhinga bwa none vyari vyerekeye ibanga. Nk’akarorero, abana barakoresha kenshi imigambi yoroshe y’ubuhinga bwo gukingira amakuru kugira ngo “banezerwe”. Ibanga si ikintu gitera amaganya vy’ukuri muri ivyo bihe.


[4] Bruce Schneier, *Ivyuma vy’ubuhinga bwa none*, igitabu ca 2, 2015 (Indianapolis, IN: Yohani Wiley n’abahungu biwe), rup. 2.


[5] Raba igitabu ca Jonathan Katz na Yehuda Lindell, *Intango y’ubuhinga bwo gukingira amakuru mu buryo bugezweho*, ikinyamakuru ca CRC (Boca Raton, FL: 2015), esp. 16–23, kugira ngo ubone insobanuro nziza.


[6] Raba n’ibindi. Katz na Lindell, aho nyene, rup. 3. Ngira ngo ukuntu bavuga birafise ibibazo, rero n’ushireho uburyo butandukanye gatoyi bw’ivyo bavuze hano.



## Gufungura guhanahana amakuru

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>


Ivyuma vy’ubuhinga bwa none vy’ubuhinga bwa none vyagenewe gutanga umutekano mu bidukikije **vy’itumanaho ryuguruye**. Nimba umuhora wacu wo guhanahana amakuru urinzwe neza cane ku buryo abatwumviriza badashobora gukoresha canke mbere no kwihweza ubutumwa bwacu gusa, rero ubuhinga bwo gukingira amakuru burarengeye urugero. Ariko rero, inzira nyinshi dukoresha mu guhanahana amakuru ntizirindwa neza gutyo.


Umugongo w’ivy’itumanaho mw’isi ya none ni urusobe runini rw’imirongo y’amatara. Guhamagara kuri telefone, kuraba televiziyo no guca ku rubuga mu rugo rwo muri iki gihe muri rusangi bishingiye kuri iyo nzira y’imirongo y’amatara (igice gitoyi coshobora kwizigira gusa ku bikoresho vy’inyenyeri). Ni ukuri ko ushobora kuba ufise amakuru atandukanye mu nzu yawe, nk’umugozi w’ibarabara, umurongo w’abaguzi (asymétrique) digitale, n’umugozi w’ibarabara. Ariko, n’imiburiburi mu bihugu vyateye imbere, izo nzira zitandukanye z’amakuru zica zifatanya ningoga hanze y’inzu yawe zigafatanya n’uruzitiro runini rw’imirongo y’amatara ihuza isi yose. Ivyo bitari vyo ni uturere tumwetumwe turi kure cane two mu bihugu vyateye imbere, nka muri Leta Zunze Ubumwe za Amerika no muri Ostraliya, aho amakuru yoshobora kandi kugenda kure cane akoresheje intsinga za telefone z’umuringa za kera.


Ntivyoshoboka ko abashobora gutera babuzwa gushika ku mubiri kuri iyo nzira y’imirongo n’ibikorwa remezo biyifasha. Nkako, turazi ko amakuru yacu menshi afatwa n’inzego zitandukanye z’ubutasi z’igihugu ku mahuriro ahambaye ya Internet.[7] Ivyo birimwo vyose kuva ku butumwa bwa Facebook gushika ku ma aderesi y’urubuga usura.


Naho gucungera amakuru ku rugero runini bisaba umwansi akomeye, nk’ikigo c’igihugu c’ubutasi, abatera bafise uburyo buke gusa barashobora kugerageza bitagoranye gucungera ku rugero rwo mu karere. Naho ivyo bishobora kuba ku rugero rwo gutera amawaya, biroroshe cane gufata gusa amakuru ata nsinga.


Amakuru menshi y’urubuga rwacu rwo mu karere—yaba mu mihana yacu, ku biro canke mu kafe—ubu aragenda biciye ku mipfunda ya radiyo aja ku bibanza bikoreshwamwo amakuru ata nsinga ku nzira zikoreshwa vyose muri kimwe, aho guca ku nsinga ziboneka. Rero uwutera akeneye ubutunzi buke kugira ngo afate umuduga uwo ari wo wose wo mu karere kawe. Ivyo birababaje cane kuko abantu benshi bakora bike cane kugira ngo bakingire amakuru agendagenda ku mbuga zabo zo mu karere. Ikindi, abashobora kudutera barashobora no gutera imihora yacu y’ubuhinga bwa none, nka 3G, 4G, na 5G. Ivyo vyose bikoreshwa mu guhanahana amakuru ata nsinga, ni ikintu gisanzwe gishobora guterwa n’abatera.


Ku bw’ivyo, iciyumviro co kugumiza ibanga ry’ivy’uguhanahana amakuru mu kurinda umuhora w’ivy’uguhanahana amakuru ni icipfuzo c’ukwihenda kitagira icizigiro ku bantu benshi bo mw’isi ya none. Ivyo tuzi vyose biratuma umuntu agira ubwoba bukomeye: ukwiye kwama wiyumvira ko hari uwuriko arakwumviriza. Kandi cryptography ni co gikoresho nyamukuru dufise kugira ngo turonke ubwoko bwose bw’umutekano muri iki gihe ca none.



**Ivyiyumviro:**


[7] Raba nk’akarorero, Olga Khazan, “Ikintu giteye ubwoba, kimaze igihe kirekire co gutera intsinga zo mu mazi”, *The Atlantic*, 16 Nyakanga 2013 (uboneka kuri [The Atlantic](umugenzo-uteye ubwoba-wamaze igihe kirekire-wo-gutera-insinga-zi-mu-kiyaga/277855/)).



# Ishingiro ry'imibare ry'ubuhinga bwo gupfuka 1

<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>



## Ibihinduka bidasanzwe

<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>


Ivy’ugushiramwo amakuru bishingiye ku biharuro. Kandi nimba ushaka kwubaka ibirenze ugutahura kw’inyuma kw’ivy’ubuhinga bwo gukingira amakuru, urakeneye kumenya neza iyo mibare.


Iki gice kiratanga vyinshi mu biharuro vy’ishimikiro uzohura navyo mu kwiga ubuhinga bwo gukora amabanga. Ivyo biganiro birimwo ibihinduka bitari vyo, ibikorwa vya modulo, ibikorwa vya XOR, n’ibikorwa vy’imburakimazi. Ukwiye kumenya neza ibintu biri muri ivyo bice kugira ngo utahure neza ubuhinga bwo gukingira amakuru ataco buvuze.


Igice gikurikira kivuga ibijanye n’inyigisho y’imibare, iyo na yo ikaba ari ingorane nyinshi kuruta.


### Ibihinduka bidasanzwe


Ihinduka ry'imburakimazi rigaragazwa n'urudome rudakomeye, rukomeye. Rero, nk’akarorero, twovuga ivyerekeye umuhinduzi w’imburakimazi $X$, umuhinduzi w’imburakimazi $Y$, canke umuhinduzi w’imburakimazi $Z$. Iyi ni yo notation nzokoresha kandi kuva ngaha gushika hanze.


**Ihinduka ry'imburakimazi** rishobora gufata agaciro kabiri canke garenga gashoboka, umwe wese afise ubushobozi bumwe bumwe bwiza. Ivyiza bishoboka biri mu rutonde rw'ibisubizo.


Igihe cose **sample** umuhinduzi w'imburakimazi, ukura agaciro kanaka kuva ku ngaruka zayo hakurikijwe ibishoboka vyasobanuwe.


Reka duhindukire tuje ku karorero koroshe. Twibaze ko umuhinduzi X asobanurwa gutya:



- X ifise igisubizo $\{1,2\}$


$$
Pr[X = 1] = 0.5
$$


$$
Pr[X = 2] = 0.5
$$


Biroroshe kubona ko $X$ ari umuhinduzi w’imburakimazi. Ica mbere, hariho agaciro kabiri canke karenga $X$ ishobora gufata, ni ukuvuga $1$ na $2$. Ubwa kabiri, agaciro kose gashoboka karafise amahirwe meza yo kubaho igihe cose ufashe nk’akarorero $X$, ni ukuvuga $0.5$.


Ivyo umuhinduzi w’imburakimazi asaba vyose ni igisubizo gifise ubushobozi bubiri canke burenga, aho ubushobozi bwose bufise ubushobozi bwiza bwo kubaho iyo umuntu afashe ivyerekanwa. Mu ngingo ngenderwako rero, igihinduka c’imburakimazi gishobora gusobanurwa mu buryo butaboneka, ata n’aho kija. Muri ivyo, woshobora kwiyumvira ko “gutora” ari ugukora igerageza ry’ibisanzwe kugira ngo umenye agaciro k’igihinduka c’imburakimazi.


Ihinduka $X$ riri hejuru ryasobanuwe mu buryo butaboneka. Ushobora rero kwiyumvira gufata urugero rw’igihinduka $X$ kiri hejuru nk’uguhindura Coin ibereye maze ugatanga “2” ku bijanye n’imitwe na “1” ku bijanye n’imirizo. Ku citegererezo cose ca $X$, usubira guhindura Coin.


Canke, woshobora kandi kwiyumvira gufata ivyerekanwa vya $X$, nk’ugutera urupfu rubereye maze ugatanga “2” mu gihe urupfu rushobora gutera $1$, $3$, canke $4$, ugatanga “1” mu gihe urupfu rushobora gutera $2$, $5$, canke $6$. Igihe cose ukoresheje $X$, usubira gutera die.


Mu vy’ukuri, igerageza ryose ry’ibidukikije ryogufasha gusobanura ibishoboka vy’agaciro gashoboka ka $X$ haruguru rirashobora kwiyumvirwa ku bijanye n’igishushanyo.


Ariko rero, kenshi na kenshi, ibintu bihinduka ata co bimaze ntibishirwamwo gusa mu buryo butaboneka. Ahubwo, umugwi w’agaciro k’ivyavuyemwo bishoboka ufise insobanuro itomoye y’ukuri (aho kuba nk’imibare gusa). Ikindi, ivyo bipimo vy’ivyavuyemwo vyoshobora gusobanurwa bishingiye ku bwoko bumwe bumwe bw’igerageza (aho kuba nk’igerageza iryo ari ryo ryose ry’ibisanzwe rifise ivyo bipimo).


Reka ubu turimbure akarorero k'umuhinduzi $X$ adasobanuwe mu buryo butaboneka. X isobanurwa gutya kugira ngo hamenyekane mu migwi ibiri itanguye umukino w’umupira w’amaguru:



- $X$ ifise igisubizo {umutuku uratangura,ubururu uratangura}
- Guhindura Coin $C$ yihariye: imizi = “umutuku uratera”; imitwe = “ubururu buratera”


$$
Pr [X = \text{red kicks off}] = 0.5
$$


$$
Pr [X = \text{blue kicks off}] = 0.5
$$


Muri ivyo, umugwi w’ivyavuyemwo wa X utanga insobanuro nyayo, ni ukuvuga ikipe itangura mu rukino rw’umupira w’amaguru. Ikindi, ingaruka zishoboka n’ibishoboka bijana navyo bigenwa n’igerageza nyaryo, ni ukuvuga guhindura Coin $C$ yihariye.


Mu biganiro vy’ubuhinga bwo gukingira amakuru, ibintu bihinduka bitari vyo akenshi bishirwamwo ku bijanye n’ivyavuyemwo bifise insobanuro y’ukuri. Bishobora kuba ari umugwi w’ubutumwa bwose bushobora gushirwa mu mfuruka, uzwi nk’umwanya w’ubutumwa, canke umugwi w’imfunguruzo zose abakoresha iyo mfunguruzo bashobora guhitamwo, uzwi nk’umwanya w’imfunguruzo.


Ibintu bihinduka mu buryo butari bwo mu biganiro ku bijanye n’ubuhinga bwo gukingira amakuru, n’aho biri ukwo, akenshi ntibisobanurwa bishingiye ku ngeragezo imwe imwe y’ibidukikije, ariko bishingiye ku ngeragezo iyo ari yo yose yoshobora gutanga ugusangira kw’ibishoboka gukwiriye.


Ibihinduka bishobora kugira ivyiyumviro bitandukanye canke bikomeza. Ibihinduka vy’imburakimazi bifise **ugusangira kw’ibishoboka bitandukanye**—ni ukuvuga ibihinduka vy’imburakimazi bitandukanye—bifise umubare w’ingaruka zishoboka zidasanzwe. Ihinduka ry’imburakimazi $X$ mu ngero zompi zatanzwe gushika ubu ryari ritandukanye.


**Ibihinduka bikomeza** bishobora gufata agaciro mu gihe kimwe canke vyinshi. Ushobora kuvuga, nk'akarorero, ko umuhinduzi w'imburakimazi, iyo ufashe ivyitegererezo, uzofata agaciro nyako ako ari ko kose hagati ya 0 na 1, kandi ko umubare nyawo wose muri iki kiringo ushobora kuba ungana. Muri ico kiringo, hariho agaciro gashoboka katagira uko kangana.


Ku biganiro vy’ubuhinga bwa none, uzokenera gusa gutahura ibihinduka bitandukanye. Ikiganiro cose c’ibihinduka vy’impfagusa kuva ng’aha gushika hanze, rero, gikwiye gutahurwa nk’aho kijanye n’ibihinduka vy’impfagusa bitandukanye, kiretse iyo bivuzwe ukundi.



### Gushushanya ibihinduka bidasanzwe


Ivyiza bishoboka n'ibishoboka bifitaniye isano n'umuhinduzi w'imburakimazi bishobora kubonwa mu buryo bworoshe biciye ku gicapo. Nk’akarorero, rimbura umuhinduzi w’imburakimazi $X$ wo mu gice c’imbere ufise umugwi w’ivyavuyemwo $\{1, 2\}$, na $Pr [X = 1] = 0.5$ na $Pr [X = 2] = 0.5$. Twoshobora kwerekana mwene iyo mpinduka mu buryo bw'igishushanyo c'imirongo nk'uko biri mu *Ishusho 1*.


*Ishusho 1: Ihinduka ry'impfagusa X*


![Figure 1: Random variable X.](assets/en/002.webp)


Ivyo bipande vyagutse biri mu *Igishushanyo 1* biragaragara ko bidasobanura ko umuhinduzi w’imburakimazi $X$ mu vy’ukuri abandanya. Ahubwo, iyo mirongo irakorwa mu buryo bwagutse kugira ngo umuntu abone neza (umurongo gusa ugororotse uratuma umuntu abona neza cane).



### Ibihinduka bimwe


Mu mvugo “ihinduka ry’imburakimazi”, ijambo “ihinduka ry’imburakimazi” risobanura gusa “ibishoboka”. Mu yandi majambo, bisigura gusa ko ingaruka zibiri canke zirenga zishoboka z’igihinduka zibaho n’ibishoboka bimwebimwe. Ivyo bivako, ariko, *ntibitegerezwa* kuba bingana (naho ijambo “random” rishobora vy’ukuri kugira iyo nsobanuro mu bindi bihe).


**Ihinduka rimwe** ni ikibazo kidasanzwe c'ihinduka ry'imburakimazi. Ishobora gufata agaciro kabiri canke karenga kose gafise ubushobozi bungana. Ihinduka ry’imburakimazi $X$ ryerekanywe mu *Ishusho 1* ni ihinduka rimwe, kuko ivyo bishoboka vyose bishika n’ibishoboka $0.5$. Ariko rero, hariho ibihinduka vyinshi vy’imburakimazi bitari ingero z’ibihinduka bimwe.


Rimbura nk’akarorero igihinduka c’imburakimazi $Y$. Ifise umugwi w'ivyavuyemwo {1, 2, 3, 8, 10} n'ugusangira kw'ibishoboka bikurikira:


$$
\Pr[Y = 1] = 0.25
$$


$$
\Pr[Y = 2] = 0.35
$$


$$
\Pr[Y = 3] = 0.1
$$


$$
\Pr[Y = 8] = 0.25
$$


$$
\Pr[Y = 10] = 0.05
$$



Naho vy’ukuri ingaruka zibiri zishoboka zifise ubushobozi bungana bwo kubaho, ni ukuvuga $1$ na $8$, $Y$ na yo nyene irashobora gufata agaciro kamwe kamwe gafise ubushobozi butandukanye n’ubw’amadolari 0.25$ iyo umuntu afashe ivyerekanwa. Ni co gituma, naho $Y$ ari umuhinduzi w’imburakimazi vy’ukuri, si umuhinduzi w’ibintu bimwe.


Igishushanyo c' $Y$ kiraboneka mu *Ishusho ya 2*.


*Ishusho ya 2: Ihinduka ry'impfagusa Y*


![Figure 2: Random variable Y.](assets/en/003.webp "Figure 2: Random variable Y")


Ku karorero ka nyuma, rimbura umuhinduzi w’imburakimazi Z. Ufise umugwi w’ivyavuyemwo {1,3,7,11,12} n’ugusangira kw’ibishoboka bikurikira:


$$
\Pr[Z = 2] = 0.2
$$


$$
\Pr[Z = 3] = 0.2
$$


$$
\Pr[Z = 9] = 0.2
$$


$$
\Pr[Z = 11] = 0.2
$$


$$
\Pr[Z = 12] = 0.2
$$


Ushobora kuyibona yerekanwa ku *Ishusho ya 3*. Ihinduka ry’imburakimazi Z ni, bitandukanye na Y, ihinduka rimwe, kuko ibishoboka vyose vy’agaciro gashoboka iyo umuntu afashe ivyitegererezo bingana.



*Ishusho ya 3: Ihinduka ry'impfagusa Z*


![Figure 3: Random variable Z.](assets/en/004.webp "Figure 3: Random variable Z")



### Ibishoboka bishingiye ku vyangombwa


Twibaze ko Bob ifise umugambi wo guhitamwo mu buryo bumwe umusi umwe wo mu mwaka wa nyuma w’ikirangamisi. Ni igiki dukwiye gushika ku ciyumviro c’uko umusi watowe woba uri mu Ci?


Igihe cose twiyumvira ko uburyo bwa Bob buzoba bumwe vy’ukuri, dukwiye gushika ku ciyumviro c’uko hariho 1/4 y’ibishoboka ko Bob ihitamwo umusi mu ci. Ivyo ni **ibishoboka bitagira aho bigarukira** vy’uko umusi watowe mu buryo bw’impfagusa uri mu Ci.


Twibaze ubu ko aho gucapura umusi w’ikirangamisi mu buryo bumwe, Bob ihitamwo gusa mu buryo bumwe muri iyo misi ubushuhe bwo ku muhingamo ku kiyaga Crystal (New Jersey) bwari degre 21 canke zirenga. Hakurikijwe ayo makuru y’inyongera, twoshika ku ciyumviro iki ku bijanye n’uko Bob izohitamwo umusi mu Ci?


Mu vy’ukuri dukwiye gushika ku nsozero itandukanye n’iyo twari dufise mbere, mbere ata yandi makuru yihariye (nk’akarorero, ubushuhe bwo ku muhingamo buri musi mu mwaka w’ikirangamisi uheze).


Kubera ko tuzi ko ikiyaga Crystal kiri muri New Jersey, nta gukeka ko tutokwitega ko ubushuhe bwo ku manywa buzoba ari degre 21 canke zirenga mu Rushana. Ahubwo, birashoboka cane ko uba umusi ushushe mu Ci canke mu mpera z’umwaka, canke umusi ahantu kanaka mu Ci. Ku bw’ivyo, kumenya ko ubushuhe bwo ku muhingamo ku kiyaga ca Crystal ku musi watowe bwari degre 21 canke zirenga, ubushobozi bwo kuba umusi watowe na Bob woba uri mu Ci buraba bwinshi cane. Ivyo ni **ibishoboka** vy’uko umusi watowe mu buryo bw’impfagusa uba mu Ci, kubera ko ubushuhe bwo ku muhingamo ku kiyaga ca Crystal bwari degre 21 canke zirenga.


Mu buryo butandukanye n’akarorero ka mbere, ibishoboka vy’ibintu bibiri na vyo nyene birashobora kuba bitagira isano ryose. Muri ivyo, tuvuga ko ari **abigenga**.


Nk’akarorero, dufate ko indege imwe imwe y’ubutungane yitwa Coin yaguye ku butaka. None, turavye ivyo, ni ibiki bishoboka ko ejo imvura izogwa? Ivyo bishobora kuba bifise ivyangombwa muri iki gihe bikwiye kuba bimwe n’ivyo bishobora gushika bitagira ivyangombwa vy’uko imvura izogwa ejo, kuko uguhinduka kwa Coin muri rusangi ntaco bihindura ku bihe.


Dukoresha "|" ikimenyetso co kwandika amajambo y’ibishoboka afise ivyangombwa. Nk'akarorero, ubushobozi bw'ikintu $A$ bushingiye ku kintu $B$ cabaye bushobora kwandikwa gutya:


$$
Pr[A|B]
$$


Rero, iyo ibintu bibiri, $A$ na $B$, vyigenga, rero:


$$
Pr[A|B] = Pr[A] \text{ and } Pr[B|A] = Pr[B]
$$


Ivyangombwa vyo kwikukira bishobora kworoshwa gutya:


$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$



Igisubizo nyamukuru mu vyiyumviro vy'ibishoboka kizwi nka **Iciyumviro ca Bayes**. Mu bisanzwe ivuga ko $Pr[A|B]$ ishobora gusubirwamwo gutya:



$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$



Aho gukoresha ibishoboka bishingiye ku bintu bimwebimwe, turashobora kandi kuraba ibishoboka bishingiye ku bintu bishingiye ku bintu bibiri canke birenze bihinduka bitari vyo ku rutonde rw’ibintu bishoboka. Twibaze ko hariho ibintu bibiri bihinduka, $X$ na $Y$. Turashobora kwerekana agaciro kose gashoboka ka $X$ na $x$, n'agaciro kose gashoboka ka $Y$ na $y$. Twovuga rero ko ibihinduka bibiri vy’imburakimazi vyigenga nimba aya majambo akurikira ari yo:


$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$


ku $x$ yose na $y$.


Reka tubone neza gatoyi ico iri jambo risobanura.


Twibaze ko ibisubizo vy’ibiharuro vya $X$ na $Y$ bisobanurwa gutya: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ na **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_i, \ldots, y_i, \ldots, y_i, \ldots, y. (Ni ibisanzwe kwerekana imigwi y'agaciro n'inyuguti zikomeye, zikomeye.)


None dufate ko ufata akarorero ka $Y$ maze ukihweza $y_1$. Iryo jambo riri hejuru ritubwira ko ubushobozi bwo kuronka ubu $x_1$ mu gutora $X$ ari kimwe nyene n’aho twoba tutarigeze twihweza $y_1$. Ivyo ni ukuri ku $y_i$ iyo ari yo yose twari gushobora gukura mu nkuru yacu ya mbere ya $Y$. Ubwa nyuma, ivyo ni ukuri si kuri $x_1$ gusa. Ku $x_i$ iyo ariyo yose, ubushobozi bwo kubaho ntibugira ico bukoze ku ngaruka y'ugutora $Y$. Ivyo vyose birakora no ku gihe $X$ ari yo ibanza gufatwa nk’akarorero.


Reka dusozere ikiganiro cacu ku ciyumviro c’ubuhinga bwa filozofiya gatoyi. Mu bintu vyose vy’ukuri, ubushobozi bw’ikintu kinaka buma busuzumwa hakurikijwe amakuru kanaka. Nta “bishoboka ataco bimaze” mu busobanuro ubwo ari bwo bwose bukomeye cane bw’iryo jambo.


Nk’akarorero, dufate ko nagusavye ko ingurube zishobora kuguruka mu 2030. Naho nta yandi makuru nguha, biragaragara ko uzi vyinshi ku bijanye n’isi bishobora gutuma ubona ibintu mu buryo bubereye. Ntimwigeze mubona ingurube ziguruka. Urazi ko abantu benshi batazokwitega ko baguruka. Urazi ko mu vy’ukuri zitari zubatswe kugira ngo ziguruke. N’ibindi.


Ni co gituma, iyo tuvuze “ibishoboka bitagira aho bigarukira” vy’ikintu kinaka mu gihe c’isi nyakuri, iryo jambo mu vy’ukuri rishobora kugira insobanuro gusa iyo turifata nk’aho risobanura ikintu nk’“ibishoboka ata yandi makuru asobanutse”. Gutahura kwose kw’“ibishoboka bishingiye ku bintu” rero, kwama gutahurwa gushingiye ku makuru amwamwe yihariye.


Nk’akarorero, noshobora kubabaza ko ingurube zishobora kuguruka mu mwaka w’2030, maze kubaha ikimenyamenya c’uko impene zimwezimwe zo muri Nouvelle-Zélande zarize kuguruka inyuma y’imyaka mikeyi zimenyerejwe. Muri ivyo, birashoboka ko uzohindura urubanza rwawe ku bijanye n’uko ingurube zizoguruka mu 2030. Rero ko ingurube zizoguruka mu 2030 bishingiye kuri iki kimenyamenya kijanye n’impene zo muri Nouvelle-Zélande.



## Ibikorwa vya modulo

<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>


### Module


Invugo y'ishimikiro cane ifise **igikorwa ca modulo** ni iyo mu buryo bukurikira: $x \mod y$.


Ihinduka $x$ ryitwa umugabane kandi ihinduka $y$ ryitwa umugabane. Kugira ngo ukore igikorwa ca modulo gifise umugabane mwiza n’umugabane mwiza, umenya gusa igice gisigaye c’umugabane.


Nk’akarorero, rimbura imvugo $25 \mod 4$. Umubare 4 uja mu mubare 25 incuro 6 zose hamwe. Igisigaye c’uwo mugabane ni 1. Ni co gituma, $25 \mod 4$ ingana na 1. Mu buryo busa n’ubwo, turashobora gusuzuma imvugo zikurikira:



- $29 \mod 30 = 29$ (nk'uko 30 ija muri 29 yose hamwe incuro 0 kandi igisigaye ni 29)
- $42 \mod 2 = 0$ (nk'uko 2 ija muri 42 yose hamwe incuro 21 kandi igisigaye ni 0)
- $12 \mod 5 = 2$ (nk'uko 5 yinjira muri 12 yose hamwe incuro 2 igisigaye ni 2)
- $20 \mod 8 = 4$ (nk'uko 8 ija muri 20 yose hamwe incuro 2 igisigaye ni 4)


Iyo umugabane canke umugabane ari mubi, ibikorwa vya modulo bishobora gukorwa mu buryo butandukanye n’indimi zo gukora porogarama.


Uzohura ata gukeka n’ibibazo bifise umugabane mubi mu vy’ubuhinga bwo gukingira amakuru. Muri ivyo bihe, uburyo busanzwe bwo kubikora ni ubu:



- Mbere menya agaciro ka hafi *kari hasi canke kangana* n’umugabane umugabane agabanyamwo n’igisigaye ca zero. Hamagara ako gaciro $p$.
- Iyo umugabane ari $x$, rero igisubizo c’igikorwa ca modulo ni agaciro ka $x – p$.


Nk’akarorero, dufate ko umugabane ari $–20$ kandi umugabane ari 3. Agaciro ka hafi cane kari munsi canke kangana na $–20$ aho 3 igabanywamwo kimwe ni $–21$. Agaciro ka $x – p$ muri iki gihe ni $–20 – (–21)$. Ivyo bingana na 1 kandi, rero, $–20 \mod 3$ bingana na 1. Mu buryo busa n’ubwo, turashobora gusuzuma imvugo zikurikira:



- $–8 \mod 5 = 2$
- $-19 \Ihinduka 16 = 13$
- $-14 \mod 6 = 4$


Ku bijanye n'ugushiramwo amajambo, uzobona ubwoko bw'imvugo zikurikira: $x = [y \mod z]$. Kubera ibifunga, igikorwa ca modulo muri iki gihe gikoreshwa gusa ku ruhande rw'iburyo rw'imvugo. Niba $y$ ingana na 25 na $z$ ingana na 4, nk'akarorero, rero $x$ isuzuma kuri 1.


Ata n'ibifunga, igikorwa ca modulo gikora ku *mpande zompi* z'imvugo. Twibaze nk’akarorero, imvugo ikurikira: $x = y \mod z$. Niba $y$ ingana na 25 na $z$ ingana na 4, rero ico tuzi ni uko $x \mod 4$ isuzuma kuri 1. Ivyo bihuye n’agaciro ako ari ko kose ka $x$ kavuye mu mugwi $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.


Ishami ry'imibare rikoresha ibikorwa vy'imibare n'imvugo ryitwa **imibare y'imibare**. Ushobora kwiyumvira iryo shami nk’imibare ku bibazo aho umurongo w’imibare udafise uburebure butagira uko bungana. Naho mu bisanzwe duhura n'ibikorwa vya modulo ku mibare (nziza) mu buhinga bwo gukingira, ushobora kandi gukora ibikorwa vya modulo ukoresheje imibare nyayo iyo ari yo yose.


### Ihinduka ry'ibanga


Igikorwa kijanye n’ivyo bita modulo gikunda guhura n’abantu mu bijanye n’ubuhinga bwo gukingira amakuru. Kugira ngo tubone akarorero, reka turimbure imwe mu nzira zizwi cane zo gupfuka amakuru mu mateka: ni ukuvuga ubuhinga bwo guhindura amakuru.


Reka tubanze tubisigure. Twibaze ko inkoranyamagambo *D* ingana inyuguti zose z’inyuguti z’icongereza, mu buryo zikurikirana, n’umugwi w’imibare $\{0, 1, 2, \ldots, 25\}$. Niwiyumvire umwanya w'ubutumwa **M**. **Shift cipher** ni, rero, umugambi wo gupfuka usobanurwa gutya:



- Hitamwo mu buryo bumwe urufunguzo $k$ mu mwanya w'urufunguzo **K**, aho **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Gushiramwo ubutumwa $m \mu \mathbf{M}$, nk'uko bikurikira:
    - Gutandukanya $m$ mu ndome zayo z'umuntu ku giti ciwe $m_0, m_1, \ldots, m_i, \ldots, m_l$
    - Guhindura buri $m_i$ mu mubare hakurikijwe *D*
    - Ku buri $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Guhindura buri $c_i$ mu nyuguti hakurikijwe *D*
    - Hanyuma ushire hamwe $c_0, c_1, \ldots, c_l$ kugira ngo ubone inyandiko y'ibanga $c$ .
- Gusobanura umwandiko w'ibanga $c$ nk'uko bikurikira:
    - Guhindura $c_i$ yose mu mubare hakurikijwe *D*
    - Ku buri $c_i$, $m_i = [(c_i – k) \mod 26]$
    - Guhindura buri $m_i$ mu nyuguti hakurikijwe *D*
    - Hanyuma ushire hamwe $m_0, m_1, \ldots, m_l$ kugira ngo ubone ubutumwa bw'intango $m$ .


Igikoresho ca modulo mu gipfukisho c'ihinduka kiratuma amajambo azunguruka, kugira ngo amajambo yose y'igipfukisho asobanurwe. Kugira ngo tubone akarorero, rimbura ukuntu ijambo “IMBWA” rikoreshwa.


Dufate ko wahisemo igufunguzo rifise agaciro ka $17$. Inyuguti “O” ingana na $14$. Ni hatabayeho igikorwa ca modulo, guteranya ino n’umubare w’inyandiko isanzwe n’igufunguzo vyotanga umubare w’inyandiko ibishe $31$. Ariko uwo mubare ntiwoshobora guhinduka inyuguti ibishe, kuko inyuguti z’icongereza ari $26$ gusa. Igikorwa ca modulo kiratanga ko umubare w’inyandiko ibishe ari $5$ (ingaruka za $31 \mod 26$), bingana n’inyuguti ibishe “F”.


Ijambo “IMBWA” ryose rifise agaciro k’urufunguzo rwa 17 ni iri:



**Ubutumwa = DOG = D,O,G = 3,14,6**
- $c_0 = [(3 + 17) \uburyo 26] = [(20) \uburyo 26] = 20 = U$
$c_1 = [(14 + 17) \mod 26] = [(31) \mod 26] = 5 = F$
- $c_2 = [(6 + 17) \uburyo 26] = [(23) \uburyo 26] = 23 = X$
*c = UFX*


Umuntu wese arashobora gutahura neza ingene shift cipher ikora kandi kumbure akayikoresha we nyene. Ariko rero, kugira ngo utere imbere mu bumenyi bwawe mu vy’ubuhinga bwo gukingira amakuru, birahambaye ko utangura kumenya neza ivy’ugushiramwo amakuru mu buryo butegekanijwe, kuko imigambi izorushiriza kugorana. Ni co gituma intambwe z’uguhindura cipher zari zategekanijwe.



**Ivyiyumviro:**


[1] Turashobora gusobanura neza neza iyo mvugo, dukoresheje amajambo yo mu gice ca mbere. Reka umuhinduzi umwe $K$ agire $K$ nk'umugwi wayo w'ingaruka zishoboka. Rero:


$$
Pr[K = 0] = \frac{1}{26}
$$


$$
Pr[K = 1] = \frac{1}{26}
$$


...n'ibindi. Igishushanyo c'umuhinduzi umwe $K$ rimwe kugira ngo ubone urufunguzo runaka.



## Ibikorwa vya XOR

<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>


Amakuru yose yo muri mudasobwa aratunganirizwa, akabikwa, kandi akarungikwa ku nzira ku rugero rw’ibice. Ivyiyumviro vyose vy’ubuhinga bwo gukingira amakuru bikoreshwa ku makuru ya mudasobwa na vyo nyene bikora ku rugero rwa bit.


Nk’akarorero, dufate ko wanditse ubutumwa bwo kuri e-mail mu gitabu cawe co gukoresha e-mail. Ivyo ukoresha vyose ntibiboneka ku nyuguti za ASCII z’imeli yawe ataco ihinduye. Ahubwo, rikoreshwa ku bijanye n’uguserukira amajambo n’ibindi bimenyetso biri muri e-mail yawe.


Igikorwa n’ingenzi c’imibare co gutahura ku bijanye n’ubuhinga bwa none, uretse igikorwa ca modulo, ni ic’igikorwa ca **XOR**, canke igikorwa “c’umwihariko canke”. Iyi nzira ifata nk'inputs ibice bibiri igatanga nk'isohoka ikindi bit. Ibikorwa vya XOR bizokwerekanwa gusa nka "XOR". Bitanga 0 iyo izo nkuru zibiri zimwe na 1 iyo izo nkuru zibiri zitandukanye. Ushobora kubona ivyo bintu bine bishoboka aha hepfo. Ikimenyetso $\oplus$ giserukira "XOR" :



- $0 \yongera 0 = 0$
- $0 \yongera 1 = 1$
- $1 \yongera 0 = 1$
- $1 \yongera 1 = 0$


Kugira ngo tubone ingero, dufate ko ufise ubutumwa $m_1$ (01111001) n’ubutumwa $m_2$ (01011001). Ibikorwa vya XOR vy’ubu butumwa bubiri birashobora kubonwa aha hepfo.



- $m_1 \ukwongerako m_2 = 01111001 \ukwongerako 01011001 = 00100000$


Inzira y’ivyo bikorwa iragororotse. Ubanza XOR ibice vy'ibubamfu cane vya $m_1$ na $m_2$. Muri iki gihe ivyo ni $0 \wongeyeko 0 = 0$. Uca ukora XOR y'ibice bibiri biva ibubamfu. Muri iki gihe ivyo ni $1 \wongeyeko 1 = 0$. Ubandanya iyo nzira gushika ukoze igikorwa ca XOR ku bice vy'iburyo cane.


Biroroshe kubona ko igikorwa ca XOR ari igihinduranya, ni ukuvuga ko $m_1 \oplus m_2 = m_2 \oplus m_1$. Ikindi, igikorwa ca XOR na co nyene kirafatanya. Ni ukuvuga, $(m_1 \m_2) \m_3 = m_1 \m_2 \m_3)$.


Igikorwa kijanye n'igikorwa ca XOR ku mirongo ibiri y'uburebure butandukanye gishobora kugira insobanuro zitandukanye, bivanye n'aho kiri. Ntituzokwitwararika hano ibikorwa vyose vya XOR ku mirongo y’uburebure butandukanye.


Igikorwa kijanye na XOR kingana n’ikibazo kidasanzwe co gukora igikorwa ca modulo ku kwongerako ibice iyo umugabanyi ari 2. Ushobora kubona ukungana mu bisubizo bikurikira:



- $(0 + 0) \mod 2 = 0 \kwongerako 0 = 0$
- $(1 + 0) \mod 2 = 1 \kwongerako 0 = 1$
- $(0 + 1) \mod 2 = 0 \kwongerako 1 = 1$
- $(1 + 1) \mod 2 = 1 \kwongerako 1 = 0$


## Ububeshi bw'imburakimazi

<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>


Mu kiganiro cacu ku bihinduka vy’imburakimazi n’ivy’imburakimazi, twashizeho itandukaniro ryihariye hagati y’“ihinduka ry’imburakimazi” n’“ihinduka ry’imburakimazi”. Ukwo gutandukanya gukomezwa mu bikorwa igihe umuntu adondora ibintu bihinduka ataco bimaze. Ariko rero, mu gihe cacu c’ubu, iyo ntandukaniro irakeneye gukurwaho maze “random” na “uniform” bikakoreshwa mu buryo bumwe. Nzobasigurira igituma mu mpera y’igice.


Kugira ngo dutangure, turashobora kwita urudodo rwa kabiri rw’uburebure $n$ **random** (canke **uniform**), nimba rwari ingaruka y’ugutora urugero rw’umuhinduzi umwe $S$ utanga urudodo rwa kabiri rwose rw’uburebure nk’ubwo $n$ ubushobozi bungana bwo guhitamwo.


Twibaze nk'akarorero, umugwi w'imirongo yose y'ibice bibiri ifise uburebure bwa 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Ni ibisanzwe kwandika urudodo rw'ibice 8 mu bice bibiri bine, kimwe cose citwa **nibble**.) Reka twite iyi nkuru y'imirongo **$S_8$**.


Kubera insobanuro iri hejuru, turashobora rero kwita urudodo rw'ibice bibiri vy'uburebure bwa 8 random (canke rumwe), nimba rwari ingaruka y'ugutora urugero rw'umuhinduzi umwe $S$ utanga urudodo rwose muri **$S_8$** ubushobozi bungana bwo guhitamwo. Kubera ko umugwi **$S_8$** urimwo $2^8$ Elements, ubushobozi bwo guhitamwo ku bijanye n'ugutora ivyitegererezo bwobaye $1/2^8$ ku rudodo rwose ruri muri uwo mugwi.


Ikintu nyamukuru ku bijanye n’uguhinduka kw’urudodo rw’ibice bibiri ni uko rusobanurwa hakurikijwe uburyo rwatowemwo. Uburyo bw’urudodo urwo ari rwo rwose rw’ibice bibiri ku bwarwo, rero, nta co buhishura ku bijanye n’ukuntu ruhinduka mu buryo butari bwo mu guhitamwo.


Nk'akarorero, abantu benshi bafise iciyumviro c'uko urudodo nka $1111\ 1111$ rutashobora gutorwa mu buryo bw'impfagusa. Ariko ivyo biragaragara ko ari ibinyoma.


Gusobanura umuhinduzi umwe $S$ ku mirongo yose y'ibice bibiri vy'uburebure bwa 8, ubushobozi bwo guhitamwo $1111\ 1111$ mu mugwi **$S_8$** ni kimwe n'ubw'umurongo nka $0111\ 0100$. Gutyo, nta co ushobora kuvuga ku bijanye n’ukuntu urudodo rugenda ruhinduka, mu gusuzuma gusa urudodo ubwarwo.


Turashobora kandi kuvuga imirongo y’imburakimazi ata nsobanuro yihariye y’imirongo ibiri. Twoshobora, nk'akarorero, kuvuga urudodo rw'imirongo itandatu $AF\ 02\ 82$. Muri iki gihe, urudodo rwari gutorwa mu buryo bw’impfagusa mu rwego rw’imirongo yose y’uburebure bwa 6. Ivyo bihwanye no guhitamwo mu buryo bw’impfagusa urudodo rw’uburebure bwa 24, kuko umubare wose w’imirongo itandatu ugereranya ibice 4.


Mu bisanzwe imvugo “urudodo rw’imburakimazi”, ata n’umwe afise ubushobozi, yerekeza ku rudodo rwatowe mu buryo bw’imburakimazi mu rwego rw’imirongo yose ifise uburebure bumwe. Uko ni ko nabidondoye haruguru. Urudodo rw'uburebure $n$ rushobora, birumvikana, na rwo nyene gutorwa mu buryo bw'impfagusa mu mugwi utandukanye. Imwe, nk’akarorero, iyo gusa igizwe n’umugwi mutoyi w’imirongo yose y’uburebure $n$, canke kumbure umugwi urimwo imirongo y’uburebure butandukanye. Ariko muri ivyo bihe, ntitwovyita “urudodo rw’imburakimazi”, ahubwo twovyita “urudodo rutoranijwe mu buryo bw’imburakimazi mu rutonde rumwe rumwe **S**”.


Iciyumviro nyamukuru kiri mu vy’ubuhinga bwo gukingira amakuru ni ic’ubuhinga bwo gukingira amakuru. **Urudodo rw'ibinyoma** rw'uburebure $n$ ruboneka *nk'aho* rwari ingaruka y'ugutora urugero rw'umuhinduzi umwe $S$ utanga urudodo rwose muri **$S_n$** ubushobozi bungana bwo guhitamwo. Ariko rero, mu vy'ukuri, urudodo ni ingaruka y'ugutora urugero rw'umuhinduzi umwe $S'$ asobanura gusa ugusangira kw'ibishoboka—si ngombwa ko haba uwufise ibishoboka bingana ku ngaruka zose zishoboka-ku gice c'ibishoboka **$S_n$**. Iciyumviro gihambaye cane aha ni uko ata n’umwe ashobora vy’ukuri gutandukanya ivyerekanwa biva kuri $S$ na $S’$, naho woba ufata vyinshi muri vyo.


Twibaze nk’akarorero, umuhinduzi w’imburakimazi $S$. Igisubizo caco ni **$S_{256}$**, iki ni igisubizo c'imirongo ibiri yose y'uburebure 256. Iyi nkuru ifise $2^{256}$ Elements. Ikintu cose gifise ubushobozi bungana bwo guhitamwo, $1/2^{256}$, ku bijanye n'ugutora.


Ikindi, dufate ko umuhinduzi w'imburakimazi $S'$. Ivyiza vyayo birimwo gusa $2^{128}$ imirongo ibiri y'uburebure 256. Ifise ugusangira kw'ibishoboka kuri iyo mirongo, ariko iyo nsangira si ngombwa ko iba imwe.


Twibaze ko ubu mfashe 1000s z’ibigereranyo bivuye kuri $S$ n’1000s vy’ibigereranyo bivuye kuri $S'$ nkaguha izo seti zibiri z’ivyavuyemwo. Ndababwira umugwi w’ivyavuyemwo ufitaniye isano n’umuhinduzi uwuhe w’imburakimazi. Igikurikira, mfata akarorero muri kimwe muri ivyo bibiri bihinduka ataco bimaze. Ariko kuri iyi nshuro sinbabwira umuhinduzi w’imburakimazi nkoresha nk’akarorero. Iyo $S'$ iba pseudorandom, rero iciyumviro ni uko ubushobozi bwawe bwo gutekereza ku buryo bubereye ku bijanye n'umuhinduzi w'imburakimazi nafashe nk'akarorero ntabwo ari mwiza kuruta $1/2$.


Mu bisanzwe, urudodo rw’uburebure bwa $n$ rukorwa mu guhitamwo urudodo rw’ubunini $n – x$, aho $x$ ari umubare wose mwiza, no kurukoresha nk’inyungu y’ubuhinga bwo kwagura. Uyu murongo w’ubunini $n – x$ uzwi kw’izina rya **seed**.


Imirongo y’ibinyoma ni iciyumviro nyamukuru co gutuma ubuhinga bwo gukingira amakuru bukora. Nk’akarorero, rimbura ibijanye n’amajambo y’uruzi. Hakoreshejwe uruzi cipher, urufunguzo rwatowe mu buryo bw’impfagusa rushirwa mu nzira y’ukwagura kugira ngo ruvemwo urudodo runini cane rw’imburakimazi. Uwo murongo w'ibinyoma uca ufatanywa n'inyandiko rusangi biciye ku gikorwa ca XOR kugira ngo haboneke inyandiko y'ibanga.


Iyo tutashobora gukora ubwo bwoko bw’urudodo rw’ibinyoma rw’uruzi, rero twokenera urufunguzo rurerure nk’ubutumwa ku bw’umutekano warwo. Ivyo si uburyo bukora cane mu bihe vyinshi.


Iciyumviro c’ubuhendanyi buvugwa muri iki gice gishobora gusobanurwamwo mu buryo bubereye. Rirashika no mu bindi bihe. Ariko ntidukwiye kwinjira cane muri ico kiganiro ngaha. Ivyo ukeneye gutahura vyose mu vy’ukuri ku bijanye n’ubuhinga bwo gukingira amakuru ni itandukaniro hagati y’urudodo rw’imburakimazi n’urudodo rw’imburakimazi. [2]


Imvo yo gukuraho itandukaniro hagati y’“imburakimazi” n’“imwe” mu kiganiro cacu na yo nyene ubu ikwiye gusobanuka. Mu bikorwa, umuntu wese akoresha ijambo pseudorandom kugira yerekane urudodo ruboneka **nk'aho** rwari ingaruka y'ugutora ivyerekanwa vy'umuhinduzi umwe $S$. Mu kuvuga ataco twirengagije, dukwiye kwita mwene uwo murongo “impuzu y’ikinyoma,” dufata ururimi rwacu rwa kera. Kubera ko ijambo “pseudo-uniforme” ari iry’agahomerabunwa kandi nta n’umwe rikoresha, ntituzorishira aha kugira ngo risobanuke neza. Ahubwo, turareka gusa itandukaniro riri hagati ya “random” na “uniform” mu gihe c’ubu.



**Ivyiyumviro**


[2] Niba ushaka gusobanura neza ivyo bintu, urashobora kuraba igitabu ca Katz na Lindell *Intangamarara y’Ivy’Imibano y’Igihugu*, esp. igice ca 3.



# Ishingiro ry'imibare ry'ubuhinga bwo gupfuka 2

<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>



## Ivyiyumviro vy’imibare ni iki?

<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>


Iki gice kivuga ku ciyumviro giteye imbere cane ku bijanye n’imishinge y’imibare y’ubuhinga bwo gukingira amakuru: inyigisho y’imibare. Naho inyigisho y'imibare ari ngirakamaro ku bijanye n'ubuhinga bwo gukingira amakuru (nk'uko biri muri Rijndael Cipher), irahambaye cane mu bijanye n'ubuhinga bwo gukingira amakuru y'urufunguzo rwa bose.


Niba uriko urabona ko ido n’ido ry’inyigisho y’imibare rigoye, nogusaba gusoma ku rugero rwo hejuru ku ncuro ya mbere. Ushobora kwama ugaruka kuri vyo mu nyuma.


___


Ushobora gutanga ibiranga **inyigisho y'imibare** nk'inyigisho y'imiterere y'imibare yose n'imikorere y'imibare ikorana n'imibare yose.


Rimbura nk’akarorero ko imibare ibiri iyo ari yo yose $a$ na $N$ ari **coprimes** (canke **primes relatives**) nimba umugabane wayo munini cane ungana na 1. Dufate ubu umubare wuzuye $N$. Ni imibare ingahe y’intege ntoyi kuruta $N$ ari coprimes zifise $N$? Twoba dushobora gutanga amajambo rusangi ku bijanye n’inyishu z’ico kibazo? Ivyo ni vyo bibazo bimenyerewe inyigisho y’imibare irondera kwishura.


Ivyiyumviro vy'imibare vya none vyishimikije ibikoresho vy'aligebra itaboneka. Igisata ca **aligebra itaboneka** ni igice c’imibare aho ibintu nyamukuru vyo gusesangura ari ibintu bitaboneka bizwi nk’imibumbe y’aligebra. **Igishushanyo c'aligebra** ni umugwi wa Elements ufatanye n'igikorwa kimwe canke vyinshi, bihuye n'ibintu bimwebimwe vy'ukuri. Biciye mu mibumbe y'imibare, abahinga mu vy'imibare barashobora kuronka ubumenyi ku bibazo vy'imibare vyihariye, mu gukuraho ibintu bitari vyo.


Ubuhinga bwa aligebra butaboneka rimwe na rimwe bwitwa kandi aligebra ya none. Ushobora kandi guhura n’iciyumviro c’**imibare itaboneka** (canke **imibare isukuye**). Iri jambo rya nyuma ntirivuga aligebra itaboneka, ahubwo risobanura kwiga imibare kubera yo ubwayo, kandi atari gusa n’ijisho ry’ivyo bishobora gukoreshwa.


Ivyiyumviro biva mu buhinga bw'ibintu bishobora gukorana n'ubwoko bwinshi bw'ibintu, kuva ku mpinduka zizigama imiterere ku mfuruka zitatu zingana gushika ku mirongo y'uruhome. Ku bijanye n’inyigisho y’imibare, turimbura gusa imigwi ya Elements irimwo imibare yose canke ibikorwa bikorana n’imibare yose.



## Amatsinda

<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>


Iciyumviro nyamukuru mu biharuro ni ic'umugwi wa Elements. Igitigiri gisanzwe kigaragazwa n’ibimenyetso vy’ugushima bifise Elements itandukanijwe n’ibimenyetso vy’ugushimira.


Nk'akarorero, umugwi w'imibare yose ni $\{..., -2, -1, 0, 1, 2, ...\}$. Ivyo bimenyetso vy’uruzitiro biri aha bisigura ko hariho urugero runaka rubandanya mu nzira kanaka. Rero umugwi w’imibare yose yuzuye na wo nyene urimwo $3, 4, 5, 6$ n’ibindi, hamwe n’amadolari-3, -4, -5, -6$ n’ibindi. Iyi mibare yose igaragazwa na $\mathbb{Z}$.


Akandi karorero k'umugwi ni $\mathbb{Z} \mod 11$, canke umugwi w'imibare yose modulo 11. Bitandukanye n'umugwi wose $\mathbb{Z}$, uwo mugwi urimwo gusa umubare w'iherezo wa Elements, ni ukuvuga $\{0, 1, \ldots, 9}\$1.


Ikosa risanzwe ni ukwiyumvira ko umugwi $\mathbb{Z} \mod 11$ mu vy'ukuri ari $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Ariko ivyo si ko biri, turavye uburyo twasobanuye igikorwa ca modulo mbere. Imibare yose idasanzwe igabanywa na modulo 11 izingira kuri $\{0, 1, \ldots, 9, 10\}$. Nk'akarorero, imvugo $-2 \mod 11$ izunguruka $9$, mu gihe imvugo $-27 \mod 11$ izunguruka $5$.


Ikindi ciyumviro nyamukuru mu biharuro ni ic'igikorwa c'ibice bibiri. Ivyo ni igikorwa cose gifata Elements zibiri kugira ngo umuntu akore ica gatatu. Nk’akarorero, uhereye ku mibare n’imibare y’ishimikiro, woba umenyereye ibikorwa bine vy’ishimikiro vy’ibiharuro bibiri: kwongerako, gukurako, gukubita n’ugugabanya.


Ivyo vyiyumviro bibiri vy’ishimikiro vy’imibare, imigwi n’ibikorwa bibiri, bikoreshwa mu gusobanura iciyumviro c’umugwi, umubumbe w’ingenzi kuruta iyindi yose muri aligebra itaboneka.


Mu buryo bwihariye, dufate ko hariho igikorwa c'ibice bibiri $\circ$. Ikindi, dufate ko hariho umugwi w’indege Elements **S** zifise iyo nzira. Ivyo vyose “bifise” bisigura aha ni uko igikorwa $\circ$ gishobora gukorwa hagati y’ibice bibiri vyose vya Elements biri mu mugwi **S**.


Ihuriro $\langle \mathbf{S}, \circ \rangle$ ni, rero, **umugwi** iyo rihuye n'ibintu bine vyihariye, bizwi nk'ibihimba vy'umugwi.


1. Ku $a$ na $b$ vyose ari Elements vya $\mathbf{S}$, $a \circ b$ na vyo nyene ni ikintu ca $\mathbf{S}$. Ivyo bizwi nka **ivyangombwa vyo gufunga**.

2. Ku $a$, $b$, na $c$ iyo ari yo yose ari Elements ya $\mathbf{S}$, ni uko $(a \uruziga b) \uruziga c = a \uruziga (b \uruziga c)$. Ivyo bizwi kw’izina rya **ivyangombwa vy’ubumwe**.

3. Hariho ikintu kidasanzwe $e$ muri $\mathbf{S}$, ku buryo ku kintu cose $a$ kiri muri $\mathbf{S}$, ihangana rikurikira rifata: $e \circ a = a \circ e = a$. Kubera ko hariho ikintu kimwe gusa nk'ico $e$, citwa **ikintu c'akaranga**. Ivyo bimenyekana nk’**ivyangombwa vy’akaranga**.

4. Ku kintu cose $a$ kiri muri $\mathbf{S}$, hariho ikintu $b$ kiri muri $\mathbf{S}$, ku buryo iyi nsiguro ifata: $a \circ b = b \circ a = e$, aho $e$ ari ikintu c’akaranga. Igikoresho $b$ aha kizwi nka **igikoresho gihinduka**, kandi gisanzwe kigaragazwa nk' $a^{-1}$. Ivyo bimenyekana nk’**ivy’uguhinduka** canke **ivy’uguhinduka**.


Reka dusuzume imigwi gatoyi. Erekana umugwi w'imibare yose n' $\mathbb{Z}$. Iryo tsinda ryifatanijwe n'inyongezo rusangi, canke $\langle \mathbb{Z}, + \rangle$, rihuye neza n'insobanuro y'umugwi, kuko rihuye n'ivyo bine bivugwa haruguru.


1. Ku $x$ yose na $y$ ari Elements ya $\imibarebb{Z}$, $x + y$ na yo ni ikintu ca $\imibarebb{Z}$. Rero $\angle \mathbb{Z}, + \angle$ ihuye n'ivyangombwa vyo gufunga.

2. Ku $x$, $y$, na $z$ iyo ari yo yose ari Elements ya $\imibarebb{Z}$, $(x + y) + z = x + (y + z)$. Rero $\angle \mathbb{Z}, + \angle$ ihura n'ivyangombwa vy'ubufatanye.

3. Hariho ikintu c'akaranga muri $\angle \mathbb{Z}, + \rangle$, ni ukuvuga 0. Ku $x$ iyo ari yo yose iri muri $\mathbb{Z}$, ni ukuvuga ko: $0 + x = x + 0 = x$. Rero $\angle \mathbb{Z}, + \angle$ ihuye n'ivyangombwa vy'akaranga.

4. Ubwa nyuma, ku kintu cose $x$ kiri muri $\mathbb{Z}$, hariho $y$ kugira ngo $x + y = y + x = 0$. Iyo $x$ iba 10, nk'akarorero, $y$ yoba $-10$ (mu gihe $x$ ari 0, $y$ na yo nyene ni 0). Rero $\angle \mathbb{Z}, + \angle$ ihuye n'ivyangombwa bihinduka.


Igihambaye ni uko umugwi w’imibare yose ifise ukwongerako ugize umugwi ntibisigura ko ugize umugwi ufise ugukubita. Ushobora kugenzura ivyo mu kugerageza $\langle \mathbb{Z}, \cdot \rangle$ ku bimenyetso bine vy'imigwi (aho $\cdot$ bisobanura ugukubita kw'imirongo).


Ivyo bimenyetso bibiri vya mbere biragaragara ko ari vyo. Ikindi, mu gihe c’ugukubita ikintu 1 gishobora gukora nk’ikintu c’akaranga. Umubare wose $x$ ukubye 1, ni ukuvuga gutanga $x$. Ariko rero, $\rangle \mathbb{Z}, \cdot \rangle$ ntizihuye n'ivyangombwa bihinduka. Ni ukuvuga ko ata kintu kidasanzwe $y$ muri $\mibarebb{Z}$ kuri $x$ yose iri muri $\mibarebb{Z}$, ku buryo $x \cdot y = 1$.


Nk’akarorero, dufate ko $x = 22$. Ni agaciro akahe $y$ kavuye mu mugwi $\mathbb{Z}$ kagwijwe na $x$ koshobora gutanga ikintu c'akaranga 1? Agaciro ka $1/22$ kokora, ariko ivyo ntibiri mu mugwi $\mathbb{Z}$. Nkako, ushobora guhura n'iki kibazo ku mubare wose $x$, uretse agaciro ka 1 na -1 (aho $y$ yoba 1 na -1).


Iyo twemereye imibare nyayo ku bijanye n’umugwi wacu, rero ingorane zacu ahanini zirazimangana. Ku kintu cose $x$ kiri mu rutonde, gukubita $1/x$ bitanga 1. Nk’uko imice ishirwa mu rutonde rw’imibare nyayo, inverse irashobora kuronka ku mubare nyawo wose. Ivyo bidasanzwe ni zero, kuko ugukubita kwose kuri zero kutazokwigera gutanga ikintu c’akaranga 1. Ni co gituma, umugwi w’imibare nyayo itari zero ifise ugukubita ni umugwi vy’ukuri.


Hari imigwi ihura n’itegeko rusangi rya gatanu, rizwi kw’izina rya **itegeko ry’uguhinduranya**. Ivyo bitegekanijwe ni ibi bikurikira:



- Twibaze ko umugwi $G$ ufise umugwi **S** n'umukoresha wa kabiri $\circ$. Twibaze ko $a$ na $b$ ari Elements ya **S**. Niba ari uko $a \circ b = b \circ a$ ku bibiri vyose Elements $a$ na $b$ biri muri **S**, rero $G$ ihura n'ivyangombwa vy'uguhinduranya.


Itsinda ryose rihuye n’ivyo guhinduka rizwi kw’izina rya **itsinda ry’ihinduka**, canke **itsinda rya Abeli** (inyuma ya Niels Henrik Abel). Biroroshe kugenzura ko umugwi w'imibare nyayo ku kwongerako n'umugwi w'imibare yose ku kwongerako ari imigwi ya Abeli. Itsinda ry'imibare yose ku gukubita si umugwi na gato, rero ipso facto ntishobora kuba umugwi wa Abelian. Itsinda ry'imibare nyayo itari zero ku gukubita, mu buryo butandukanye, na ryo nyene ni umugwi wa Abelian.


Ukwiye kwumviriza amakoraniro abiri ahambaye yerekeye ugushiramwo amajambo. Ica mbere, ibimenyetso “+” canke “×” bizokoreshwa kenshi kugira ngo bigereranye ibikorwa vy’imigwi, mbere n’igihe Elements atari, mu vy’ukuri, imibare. Muri ivyo bihe, ntukwiye gusobanura ivyo bimenyetso nk’ugushiramwo canke gukubita kw’imibare bisanzwe. Ahubwo ni ibikorwa bifise gusa ugusa n’ivyo bikorwa vy’imibare.


Keretse iyo uriko uravuga cane cane kwongerako canke gukubita, biroroshe gukoresha ibimenyetso nka $\circ$ na $\diamond$ ku bikorwa vy'imigwi, kuko ivyo bidafise insobanuro zishingiye cane ku mico kama.


Ubwa kabiri, kubera iyo mvo nyene “+” na “×” zikoreshwa kenshi mu kwerekana ibikorwa bitari ivy’imibare, akaranga Elements k’imigwi gakunda kugaragazwa na “0” na “1”, mbere n’igihe Elements muri iyo migwi atari imibare. Keretse iyo uriko uravuga ikintu c’akaranga c’umugwi ufise imibare, biroroshe gukoresha ikimenyetso kitagira aho kigarukira nka “$e$” kugira ngo werekane ikintu c’akaranga.


Ivyiyumviro vyinshi bitandukanye kandi bihambaye cane mu biharuro bifise ibikorwa bimwebimwe vy’ibice bibiri ni imigwi. Ariko rero, ibikorwa vy’ubuhinga bwa cryptography bikora gusa n’imigwi y’imibare yose canke n’imiburiburi Elements idondorwa n’imibare yose, ni ukuvuga mu rwego rw’inyigisho y’imibare. Ku bw’ivyo, amatsinda afise imibare nyayo atari imibare yose ntakoreshwa mu bikorwa vy’ubuhinga bwo gupfuka amakuru.


Reka duheze dutanga akarorero ka Elements ishobora “gusobanurwa n’imibare yose”, naho nyene atari imibare yose. Akarorero keza ni uturongo tw’ibigobe vy’uruzitiro. Naho akarongo ako ari ko kose kari ku nzira y’umurongo w’uruzitiro atari umubare wose, mwene ako karongo karadondorwa vy’ukuri n’imibare ibiri yuzuye.


Nk'akarorero, imirongo y'uruzitiro ni ngirakamaro kuri Bitcoin. Urufunguzo rwose rwa Bitcoin rw'ibanga n'urwa bose rutorwa mu rwego rw'ibiharuro bisobanurwa n'uruzitiro rukurikira:


$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$


(umubare munini w'intango uri munsi ya $2^{256}$)


Ibikorwa muri Bitcoin mu bisanzwe birimwo gufunga ibisohoka ku rufunguzo rumwe canke nyinshi za bose mu buryo bumwe. Agaciro kava muri ivyo bikorwa gashobora rero gufungurwa hakoreshejwe imikono ya digitale n’imfunguruzo z’ibanga zihuye.




## Imigwi y'ingendo

<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>


Itandukaniro rinini dushobora gushiramwo ni hagati ya **umugwi utagira iherezo** n’umugwi **utagira iherezo**. Irya mbere rifise umubare utagira iherezo wa Elements, mu gihe irya kabiri rifise umubare utagira iherezo wa Elements. Umubare wa Elements mu mugwi uwo ari wo wose ufise impera uzwi nka **urutonde rw'umugwi**. Ivyiyumviro vyose vy’ubuhinga bwo gukingira amakuru birimwo gukoresha imigwi bishingiye ku migwi ifise impera (y’imibare-y’inyigisho).


Mu nzira y'urufunguzo rwa bose, umugwi kanaka w'imigwi ya Abelian ifise impera izwi nk'imigwi y'inzinguzingu ni ngirakamaro cane. Kugira ngo dutahure imigwi y’ingendo, turakeneye ubwa mbere gutahura iciyumviro c’ugutera imbere kw’ibintu vy’imigwi.


Twibaze ko umugwi $G$ ufise igikorwa c'umugwi $\circ$, kandi uwo $a$ ari ikintu ca $G$. Invugo $a^n$ rero ikwiye gusobanurwamwo nk’ikintu $a$ gifatanijwe na co ubwaco incuro $n – 1$ zose hamwe. Nk’akarorero, $a^2$ bisobanura $a \uruzitiro a$, $a^3$ bisigura $a \uruzitiro a$, n’ibindi. (Urabona ko ugushira ahabona atari ngombwa ko ari ugushira ahabona mu buryo bw’imibare busanzwe.)


Reka duhindukire tuje ku karorero. Twibaze ko $G = \angle \mathbb{Z} \mod 7, + \angle$, kandi ko agaciro kacu ka $a$ kangana na 4. Muri iki gihe, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Canke, $a^4$ yoba iserukira $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.


Imigwi imwimwe y’Ababeli irafise Elements imwe canke myinshi, ishobora gutanga iyindi migwi yose Elements biciye mu kubandanya gutera imbere. Izo Elements zitwa **amageneratore** canke **Elements za kera**.


Itsinda rihambaye ry'iyo migwi ni $\angle \mathbb{Z}^* \mod N, \cdot \rangle$, aho $N$ ari umubare w'intango. Igiharuro $\mathbb{Z}^*$ aha bisigura ko iryo tsinda ririmwo imibare yose itari zero, nziza iri munsi ya $N$. Mwene uwo mugwi rero, wama ufise $N – 1$ Elements.


Rimbura nk'akarorero, $G = \ururimi \imibarebb{Z}^* \mod 11, \cdot \ururimi$. Iri tsinda rifise Elements zikurikira: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Urutonde rw’iri tsinda ni 10 (ari vyo vy’ukuri bingana n’amadolari 11 – 1$).


Reka dusuzume gutera imbere igice ca 2 kivuye muri iri tsinda. Ivyo biharuro gushika kuri $2^{12}$ vyerekanywe aha hepfo. Zirikana ko ku ruhande rw’ibubamfu rw’ingero, igiharuro kivuga igiharuro c’ibintu vy’umugwi. Mu karorero kacu, ivyo vy’ukuri birimwo ugushiramwo imibare ku ruhande rw’iburyo rw’ingero (ariko vyari gushobora no kubamwo, nk’akarorero, kwongerako). Kugira ngo nsobanure neza, nanditse igikorwa gisubirwamwo, aho kwandika urupapuro rw’igiharuro ku ruhande rw’iburyo.



- $2^1 = 2 \ihindurwa 11$
- $2^2 = 2 \cdot 2 \umuhinduzi 11 = 4 \umuhinduzi 11$
- $2^3 = 2 \cdome 2 \cdome 2 \mod 11 = 8 \mod 11$
- $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
- $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
- $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
- $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
- $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
- $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
- $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = $1 1
- $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 =$1 \mod
- $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 =\4d \4 11$


Niwaraba neza, urashobora kubona ko gukora igiharuro ku kintu ca 2 gica mu nzira zose za Elements za $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ mu buryo bukurikira: 2, 4, 8, 5, 10, 9^2,{06,}ter. gukomeza gutera imbere kw’ingendo z’ikintu 2 biciye mu Elements zose kandi mu buryo bumwe. Ni co gituma, ikintu 2 ari umuyagankuba mu $\ururimi \mathbb{Z}^* \mod 11, \cdot \ururimi$.


Naho $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ ifise amageneratore menshi, si Elements zose z'iri tsinda ari amageneratore. Rimbura nk’akarorero ikintu ca 3. Guca mu bipimo 10 vya mbere vy’ugutera imbere, utagaragaje imibare igoye, bivamwo ibi bikurikira:



- $3^1 = 3 \ihindurwa 11$
- $3^2 = 9 \ihindurwa 11$
- $3^3 = 5 \Ihinduka 11$
- $3^4 = 4 \Ihinduka 11$
- $3^5 = 1 \mod 11$
- $3^6 = 3 \Ihinduka 11$
- $3^7 = 9 \Ihinduka 11$
- $3^8 = 5 \Ihinduka 11$
- $3^9 = 4 \Ihinduka 11$
- $3^{10} = 1 \mod 11$


Aho guca mu mibare yose iri muri $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, gutera imbere kw'ikintu 3 bijana gusa ku gice c'ivyo bipimo: 3, 9, 5, 4, na 1. Inyuma y'ugusubiramwo ivyo bipimo vya gatanu, a.


Ubu turashobora gusobanura **umugwi w'ingendo** nk'umugwi wose ufise n'imiburiburi umuyagankuba umwe. Ni ukuvuga ko hariho n’imiburiburi ikintu kimwe c’umugwi ushobora gukuramwo uwundi mugwi wose Elements biciye mu gutera imbere.


Ushobora kuba warabonye mu karorero kacu kari hejuru ko $2^{10}$ na $3^{10}$ vyose bingana $1 \mod 11$. Nkako, naho tutazokora imibare, gutera 10 ikintu cose kiri mu mugwi $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ bizotanga $1 \mod 11$. Ni kubera iki ari ukwo biri?


Iki ni ikibazo gihambaye, ariko bisaba igikorwa kugira ngo umuntu ashobore kuvyishura.


Kugira ngo dutangure, dufate ko hari imibare ibiri nziza $a$ na $N$. Iciyumviro gihambaye mu vyiyumviro vy’imibare kivuga ko $a$ ifise modulo inverse y’ugukubita $N$ (ni ukuvuga umubare wose $b$ kugira ngo $a \cdot b = 1 \mod N$) iyo kandi gusa iyo umugabane munini cane hagati ya $a$ na $N$ ungana na 1. Ni ukuvuga iyo $a$ na $N$ ari coprimes.


Rero, ku mugwi uwo ari wo wose w'imibare yose ifise modulo y'ugukubita $N$, ni coprimes ntoyi gusa zifise $N$ zishirwa mu mugwi. Turashobora kwerekana iyo nkuru na $\imibarebb{Z}^c \mod N$.


Nk’akarorero, dufate ko $N$ ari 10. Imibare yose 1, 3, 7, na 9 ni yo yonyene ihuye na 10. Rero umugwi $\mathbb{Z}^c \mod 10$ urimwo gusa $\{1, 3, 7, 9\}$. Ntushobora kurema itsinda rifise imibare yose y'ugukubita modulo 10 ukoresheje iyindi mibare yose iri hagati ya 1 na 10. Kuri iri tsinda, ibihinduka ni bibiri 1 na 9, na 3 na 7.


Mu gihe $N$ ubwayo ari umubare w’imbere, imibare yose kuva kuri 1 gushika kuri $N – 1$ ni coprimes na $N$. Mwene uwo mugwi rero, ufise urutonde rwa $N – 1$. Dukoresheje inyandiko yacu ya kera, $\imibarebb{Z}^c \mod N$ ingana na $\imibarebb{Z}^* \mod N$ iyo $N$ ari umubare w'intango. Itsinda twahisemwo ku karorero kacu ka mbere, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, ni urugero rwihariye rw'iri tsinda ry'imigwi.


Inyuma y’aho, igikorwa $\phi(N)$ giharura umubare w’ibiharuro gushika ku mubare $N$, kandi kizwi nka **igikorwa ca Euler’s Phi**. [1] Dushingiye ku **Itegeko rya Euler**, igihe cose imibare ibiri $a$ na $N$ ari coprimes, ibi bikurikira biraba:



- $a^{\phi(N)}\uburyo N = 1 \uburyo N$


Ivyo birafise akamaro kanini ku mugwi w'imigwi $\rangle \mathbb{Z}^* \mod N, \cdot \rangle$ aho $N$ ari umubare w'intango. Kuri iyo mirwi, ugushiramwo ibintu vy'imigwi bigereranya ugushiraho ivy'imibare. Ni ukuvuga ko $a^{\phi(N)} \mod N$ igereranya igikorwa c'imibare $a^{\phi(N)} \mod N$. Nk’uko ikintu cose $a$ muri iyo mirwi y’ugukubita gifatanya na $N$, bisigura ko $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.


Iciyumviro ca Euler ni igisubizo gihambaye vy’ukuri. Kugira ngo dutangure, bisigura ko Elements zose ziri muri $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ zishobora gusa guca mu mubare w’agaciro biciye ku gutera imbere kugabanya muri $N – 1$. Mu gihe c'ururimi 11, ibi bisigura ko ikintu cose gishobora guca muri 2, 5, canke 10 Elements gusa. Itsinda ritanga agaciro ko ikintu cose gica mu gihe c'ugukuraho rizwi nka **urutonde rw'ikintu**. Ikintu gifise urutonde rungana n’urutonde rw’umugwi ni umuyagankuba.


Ikindi, igiharuro ca Euler kivuga ko dushobora kwama tumenya igisubizo ca $a^{N – 1} \mod N$ ku mugwi uwo ari wo wose $\rangle \mathbb{Z}^* \mod N, \cdot \rangle$ aho $N$ ari umubare w’intango. Ivyo ni ko biri ata kuraba ingene imibare nyayo yoba igoye.


Nk’akarorero, dufate ko umugwi wacu ari $\mathbb{Z}^* \mod 160.481.182$ (aho 160.481.182 ari umubare w’intango vy’ukuri). Turazi ko imibare yose yuzuye kuva kuri 1 gushika kuri 160.481.181 itegerezwa kuba Elements y’iri tsinda, kandi ko $\phi(n) = 160.481.181$. Naho tutashobora gutera intambwe zose mu biharuro, turazi ko imvugo nka $514^{160.481.181}$, $2.005^{160.481.181}$, na $256.212^{160.481.181}$ zose zitegerezwa gusuzuma $\mo,61,1.


**Ivyiyumviro:**


[1] Ico gikorwa gikora gutya. Umubare wose $N$ ushobora gufatwa mu gice c'imibare y'intango. Twibaze ko $N$ imwe imwe ifatwa nk’uko bikurikira: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ aho $p$ zose ari imibare y’intango kandi $e$ zose ari imibare yose irengeye canke ingana na 1.


$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$


Igishushanyo c'imikorere ya Euler Phi c'ugucapura kwa mbere kwa $N$.



## Imirima

<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>


Itsinda ni umubumbe w’ishimikiro w’aligebra mu aligebra itaboneka, ariko hariho n’izindi nyinshi. Iyindi mibumbe y'aligebra ukeneye kumenya ni iyo **umurima**, cane cane iyo **umurima ufise impera**. Ubwo bwoko bw'imiterere y'aligebra burakoreshwa kenshi mu gupfuka amakuru, nk'uko biri mu rugero rwo gupfuka amakuru rwo mu rwego rwo hejuru. Ico ca nyuma ni co gikorwa nyamukuru co gushiramwo amakuru y’uburinganire uzohura na co mu bikorwa.


Umurima ukomoka ku ciyumviro c’umugwi. Mu buryo bwihariye, **umurima** ni umugwi wa Elements **S** ufise ibikoresho bibiri $\circ$ na $\diamond$, bihuye n'ibi bikurikira:


1. Itsinda **S** rifise $\circ$ ni umugwi wa Abeli.

2. Itsinda **S** rifise $\diamond$ ni umugwi wa Abelian ku “kitari zero” Elements.

3. Itsinda **S** rifise ibikoresho bibiri rihuye n’ico bita ivyangombwa vy’ugusangira: Dufate ko $a$, $b$, na $c$ ari Elements ya **S**. Hanyuma **S** ifise ibikoresho bibiri ihura n'umutungo w'ugusangira igihe $a \uruziga (b \uruziga c) = (a \uruziga b) \uruziga (a \uruziga c)$.


Zirikana ko, nk’uko biri ku mirwi, insobanuro y’umurima ari ikintu kitaboneka cane. Ntaco ivuga ku bwoko bwa Elements muri **S**, canke ku bikorwa $\circ$ na $\diamond$. Ivuga gusa ko umurima ari umugwi uwo ari wo wose wa Elements ufise ibikorwa bibiri ivyo bintu bitatu biri hejuru bikora. (Ikintu “zero” kiri mu mugwi wa kabiri wa Abeli ​​gishobora gusobanurwamwo ibintu bitaboneka.)


None akarorero k’umurima koshobora kuba akahe? Akarorero keza ni umugwi $\mathbb{Z} \mod 7$, canke $\{0, 1, \ldots, 7\}$ usobanuwe hejuru y'ukwongerako gusanzwe (mu kibanza ca $\circ$ hejuru) n'ugukubita gusanzwe (mu kibanza ca $\diamond$ hejuru).


Mbere, $\mathbb{Z} \mod 7$ ihuye n'ivyangombwa vyo kuba umugwi wa Abeli ​​ku kwongerako, kandi ihuye n'ivyangombwa vyo kuba umugwi wa Abeli ​​ku gukubita iyo uzirikanye gusa Elements itari zero. Ubwa kabiri, uguhuza umugwi n’abakoresha babiri bihuye n’ivyo gutanga.


Ni vyiza mu vy’inyigisho gutohoza ivyo vyiyumviro dukoresheje ingingo ngenderwako zimwe zimwe. Reka dufate agaciro k’igerageza 5, 2, na 3, bimwe bimwe vyatowe mu buryo bw’impfagusa Elements bivuye mu mugwi $\mathbb{Z} \mod 7$, kugira ngo dusuzume umurima $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Tuzokoresha izo nzira zitatu mu buryo bukurikiranye, nk’uko bikenewe kugira ngo turondere ibintu vyihariye.


Reka tubanze turabe nimba $\mathbb{Z} \mod 7$ ifise ivyungura ari umugwi wa Abeli.


1. **Ivyangombwa vyo gufunga**: Reka dufate 5 na 2 nk’agaciro kacu. Muri ivyo, $[5 + 2] \umubare 7 = 7 \umubare 7 = 0$. Ivyo ni ikintu ca $\mathbb{Z} \mod 7$, rero igisubizo gihuye n'ivyo gufunga.

2. **Ivyangombwa vy’ubufatanye**: Reka dufate 5, 2, na 3 nk’agaciro kacu. Muri ivyo, $[(5 + 2) + 3] \umuhinduzi 7 = [5 + (2 + 3)] \umuhinduzi 7 = 10 \umuhinduzi 7 = 3$. Ivyo bihuye n’ivyo umuntu ashobora gukorana n’abandi.

3. **Ivyangombwa vy’akaranga**: Reka dufate 5 nk’agaciro kacu. Muri ivyo, $[5 + 0] \umubare 7 = [0 + 5] \umubare 7 = 5$. Rero 0 isa n'ikintu c'akaranga co kwongerako.

4. **Ivyabaye bihinduka**: Rimbura ibihinduka vya 5. Bikenewe ko ari uko $[5 + d] \mod 7 = 0$, ku gaciro kamwe ka $d$. Muri iki gihe, agaciro kadasanzwe kuva kuri $\mathbb{Z} \mod 7$ gahuye n'ivyo ni 2.

5. **Ivyangombwa vy’uguhindura**: Reka dufate 5 na 3 nk’agaciro kacu. Muri ivyo, $[5 + 3] \umubare 7 = [3 + 5] \umubare 7 = 1$. Ivyo bihuye n’ivyo guhinduranya.


Itsinda $\mathbb{Z} \mod 7$ rifise ivyungura risa n'iry'umugwi wa Abeli. Reka ubu turabe nimba $\mathbb{Z} \mod 7$ ifise ugukubita ari umugwi wa Abelian ku bitari zero Elements vyose.


1. **Ivyangombwa vyo gufunga**: Reka dufate 5 na 2 nk’agaciro kacu. Muri ivyo, $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Ivyo navyo ni ikintu ca $\mathbb{Z} \mod 7$, rero igisubizo gihuye n'ivyo gufunga.

2. **Ivyangombwa vy’ubufatanye**: Reka dufate 5, 2, na 3 nk’agaciro kacu. Muri ivyo, $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Ivyo bihuye n’ivyo umuntu ashobora gukorana n’abandi.

3. **Ivyangombwa vy’akaranga**: Reka dufate 5 nk’agaciro kacu. Muri ivyo, $[5 \cdome 1] \mod 7 = [1 \cdome 5] \mod 7 = 5$. Rero 1 isa n'aho ari ikintu c'akaranga co gukubita.

4. **Ivyabaye bihinduka**: Rimbura ibihinduka vya 5. Bikenewe ko $[5 \cdot d] \mod 7 = 1$, ku gaciro kamwe ka $d$. Agaciro kadasanzwe kava kuri $\mathbb{Z} \mod 7$ gahuye n'ivyo ni 3. Ivyo bihuye n'ivyo bihinduka.

5. **Ivyangombwa vy’uguhindura**: Reka dufate 5 na 3 nk’agaciro kacu. Muri ivyo, $[5 \cdome 3] \mod 7 = [3 \cdome 5] \mod 7 = 15 \mod 7 = 1$. Ivyo bihuye n’ivyo guhinduranya.


Itsinda $\mathbb{Z} \mod 7$ risa n'irihuye n'amategeko yo kuba umugwi wa Abelian iyo rifatanijwe n'ukwongerako canke gukubita kuri Elements itari zero.


Ubwa nyuma, iyo seti ifatanijwe n’abakoresha bompi isa n’ihuye n’ivyo gutanga. Reka dufate 5, 2, na 3 nk’agaciro kacu. Turashobora kubona ko $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.


Ubu twabonye ko $\mathbb{Z} \mod 7$ ifise ubuhinga bwo kwongerako n’ugukubita ihuye n’ivy’ukuri vy’umurima ufise impera igihe ugerageza n’agaciro kadasanzwe. Ego ni ko, ivyo turashobora no kubigaragaza muri rusangi, ariko ntituzobigira ngaha.


Itandukaniro nyamukuru riri hagati y’ubwoko bubiri bw’imirima: imirima ifise iherezo n’iyitagira iherezo.


**Ikibanza kitagira iherezo** kirimwo ikibanza aho umugwi **S** ari munini utagira iherezo. Itsinda ry'imibare nyayo $\mathbb{R}$ ifise ubuhinga bwo kwongera n'ugukubita ni akarorero k'umurima utagira iherezo. **Ikibanza gifise iherezo**, kizwi kandi nka **Ikibanza ca Galois**, ni ikibanza aho umugwi **S** ufise iherezo. Akarorero kacu kari hejuru ka $\ururimi \mathbb{Z} \mod 7, +, \cdot \ururimi$ ni umurima ufise impera.


Mu vy’ubuhinga bwo gupfuka amakuru, dukunda canecane ibice bifise aho bigarukira. Muri rusangi, birashobora kwerekanwa ko hariho umurima ufise impera ku mugwi umwe wa Elements **S** iyo kandi gusa iyo ufise $p^m$ Elements, aho $p$ ari umubare w’intango na $m$ umubare wuzuye mwiza uruta canke ungana n’umwe. Mu yandi majambo, iyo urutonde rw'umugwi umwe **S** ari umubare w'intango ($p^m$ aho $m = 1$) canke ububasha bumwe bumwe bw'intango ($p^m$ aho $m > 1$), rero urashobora gusanga abakozi babiri $\circ$ na $\diamond$ ku buryo ivyangombwa vy'umurima bishitse.


Iyo hari umurima ufise impera ufise umubare w'intango wa Elements, rero witwa **umurima w'intango**. Nimba umubare wa Elements mu murima ufise impera ari ububasha bwa mbere, rero uwo murima witwa **umurima w'ukwagura**. Mu vy’ubuhinga bwo gukingira amakuru, turakunda ivy’imbere n’ivy’inyuma. [2]


Ivyiyumviro nyamukuru vy'inyungu mu buhinga bwo gukingira amakuru ni ivyo aho umugwi w'imibare yose uhindurwa n'umubare w'intangamarara, kandi abakoresha ni ugushiramwo n'ugukubita. Iryo tsinda ry'ibibanza bifise impera ryoba ririmwo $\imibarebb{Z}\mod 2$, $\imibarebb{Z}\mod 3$, $\imibarebb{Z}\mod 5$, $\imibarebb{Z}\mod 7$, $\imibarebb{Z}\mod 11$, $\}mo,bb{1 Ku kibanza cose c’intango $\mathbb{Z} \mod p$, umugwi w’imibare yose y’ikibanza ni uwu: $\{0, 1, \ldots, p – 2, p – 1\}$.


Mu bijanye n’ubuhinga bwo gukingira amakuru, turakunda kandi ibice vy’ukwagura, cane cane ibice vyose bifise $2^m$ Elements aho $m > 1$. Nk’akarorero, ivyo bibanza bifise impera birakoreshwa mu gitabu ca Rijndael Cipher, kikaba ari co gishingiyeko Itegeko ry’Igitabu c’Ibimenyetso vy’Ibimenyetso. Naho ivyicaro vy'intango bishobora gutahurwa, ivyo bice vy'ivyagutse vy'ishimikiro 2 birashoboka ko atari ivy'umuntu wese atamenyereye aligebra itaboneka.


Kugira ngo dutangure, ni ukuri ko umugwi wose w'imibare yose ufise $2^m$ Elements ushobora guhabwa abakozi babiri botuma ihuriro ryabo rihinduka umurima (igihe cose $m$ ari umubare wose mwiza). Yamara, kuba hariho umurima ntibisigura ko woroshe kuwuvumbura canke ko ushobora gukoreshwa canecane ku bikorwa bimwebimwe.


Nk'uko bigaragara, cane cane ibice vy'ukwaguka vy'amadolari 2^m$ mu buhinga bwo gukingira amakuru ni ivyo bisobanurwa ku migwi yihariye y'imvugo z'imibare myinshi, aho kuba imigwi imwe imwe y'imibare yose.


Nk'akarorero, dufate ko twipfuza umwanya wo kwagura ufise $2^3$ (i.e., 8) Elements mu rwego. Naho hoba hariho imigwi myinshi itandukanye ishobora gukoreshwa ku mirima y'ubunini nk'ubwo, imwe muri iyo migwi irimwo amabara menshi yihariye yose y'uburyo $a_2x^2 + a_1x + a_0$, aho umubare wose $a_i$ ari 0 canke 1. Ni co gituma, iri tsinda **S** ririmwo ibi bikurikira Elements:


1. $0$: Igihe $a_2 = 0$, $a_1 = 0$, na $a_0 = 0$.

2. $1$: Igihe $a_2 = 0$, $a_1 = 0$, na $a_0 = 1$.

3. $x$: Ikibazo aho $a_2 = 0$, $a_1 = 1$, na $a_0 = 0$.

4. $x + 1$: Ikibazo aho $a_2 = 0$, $a_1 = 1$, na $a_0 = 1$.

5. $x^2$: Ikibazo aho $a_2 = 1$, $a_1 = 0$, na $a_0 = 0$.

6. $x^2 + 1$: Ikibazo aho $a_2 = 1$, $a_1 = 0$, na $a_0 = 1$.

7. $x^2 + x$: Ikibazo aho $a_2 = 1$, $a_1 = 1$, na $a_0 = 0$.

8. $x^2 + x + 1$: Ikibazo aho $a_2 = 1$, $a_1 = 1$, na $a_0 = 1$.


Rero **S** yoba ari umugwi $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Ni ibihe bikorwa bibiri bishobora gusobanurwa kuri iyi seti ya Elements kugira ngo bimenyekane ko ihuriro ryavyo ari umurima?


Igikorwa kibanza ku rutonde **S** ($\circ$) gishobora gusobanurwamwo nk'inyongera y'ibiharuro vyinshi modulo 2. Ico ubwirizwa gukora n'ukwongerako ibiharuro vyinshi nk'uko wobigira mu bisanzwe, hanyuma ugakoresha modulo 2 kuri buri kimwe mu biharuro vy'ibiharuro vyinshi bivako. Dore ingero zimwe zimwe:



- $
- $[(x^2 + x) + (x)] \uburyo 2 = [x^2 + 2x] \uburyo 2 = x^2$
- $


Igikorwa kigira kabiri ku rutonde **S** ($\diamond$) gikenewe kugira ngo ureme umurima kiragoye cane. Ni ubwoko bw’ugukubita, ariko si ugukubita gusanzwe kuva ku mibare. Ahubwo, utegerezwa kubona ikintu cose nk’umurongo maze ugatahura igikorwa nk’ugukubita kw’izo nzira zibiri modulo polynomial idashobora kugabanywa.


Reka tubanze duhindukire ku ciyumviro c’inyuguti nyinshi zidashobora kugabanywa. **Irreducible polynomial** ni iyo idashobora guhindurwa (nk'uko umubare w'intango udashobora guhindurwa mu bice bitari 1 n'umubare w'intango ubwawo). Kubera intumbero zacu, turakunda ama polynomial adashobora kugabanywa ku bijanye n’umugwi w’imibare yose. (Iyumvire ko ushobora gushobora guharura ibiharuro bimwebimwe ukoresheje, nk'akarorero, imibare nyayo canke igoye, n'aho woba udashobora kuyaharura ukoresheje imibare yose.)


Nk’akarorero, rimbura igiharuro c’ibiharuro vyinshi $x^2 - 3x + 2$. Ivyo bishobora gusubirwamwo nk’ $(x – 1)(x – 2)$. Ivyo rero si ibidashobora kugabanywa. Ubu rero rimbura igiharuro c’inyuguti nyinshi $x^2 + 1$. Ukoresheje imibare yose gusa, nta buryo bwo kwongera gupima iyi mvugo. Rero, iyi ni polynomial idashobora kugabanywa ku bijanye n'imibare yose.


Igikurikira, reka duhindukire ku ciyumviro c’ugukubita kw’ibiharuro. Ntituzokwihweza iki ciyumviro mu buryo bwimbitse, ariko ukeneye gusa gutahura itegeko ry’ishimikiro: Ugucapura kwose kw’imirongo bishobora kubaho igihe cose umugabane ufise urugero rurengeye canke rungana n’urw’umugabanyi. Iyo umugabane ufise urugero rutoyi kuruta umugabane, rero umugabane ntushobora kuzosubira kugabanywa n’umugabane.


Nk’akarorero, rimbura imvugo $x^6 + x + 1 \mod x^5 + x^2$. Ivyo biragabanya cane uko urugero rw’umugabane, 6, rusumba urugero rw’umugabane, 5. Ubu rero rimbura imvugo $x^5 + x + 1 \mod x^5 + x^2$. Ivyo na vyo nyene biragabanya cane, kuko urugero rw’umugabane, 5, n’umugabane, 5, bingana.


Ariko rero, ubu rero rimbura imvugo $x^4 + x + 1 \mod x^5 + x^2$. Ivyo ntibigabanya cane, kuko urugero rw'umugabane, 4, ruri hasi y'urugero rw'umugabane, 5.


Hashingiwe kuri ayo makuru, ubu turiteguriye kurondera igikorwa cacu ca kabiri c’umugwi $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.


Naramaze kuvuga ko igikorwa ca kabiri gikwiye gutahurwa nk’ugukubita kwa vecteur modulo bimwe bimwe bidashobora kugabanywa. Iyi polynomial idashobora kugabanywa ikwiye gutuma igikorwa ca kabiri gisobanura umugwi wa Abelian hejuru ya **S** kandi kikaba gihuye n’ivyangombwa vy’ugusangira. None iyo polynomial idashobora kugabanywa ikwiye kuba iyihe?


Nk’uko amavecteur yose ari muri iyo nkuru ari yo mu rwego rwa 2 canke hasi, igiharuro c’ingero idashobora kugabanywa gikwiye kuba c’ingero ya 3. Iyo ugukubita kwose kw’ingero zibiri ziri muri iyo nkuru gutanga igiharuro c’ingero ya 3 canke irenga, turazi ko modulo igiharuro c’ingero ya 3 cama gitanga igiharuro c’ingero ya 2 canke hasi. Ivyo ni ko biri kubera ko igiharuro cose c’ingero ya 3 canke irenga cama kigabanwa n’igiharuro c’urugero rwa 3. Ikindi, igiharuro gikora nk’umugabanyi gitegerezwa kuba kidashobora kugabanywa.


Bica bigaragara ko hariho amapolynomial menshi adashobora kugabanywa y’urugero rwa 3 twoshobora gukoresha nk’umugabanyi wacu. Imwe muri izo polynomial isobanura umurima utandukanye mu gufatanya n’umugwi wacu **S** n’ukwongerako modulo 2. Ivyo bisigura ko ufise amahitamwo menshi iyo ukoresheje umurima w’ukwagura $2^m$ mu buhinga bwo gukingira amakuru.


Ku karorero kacu, dufate ko duhisemwo igiharuro c’inyuguti nyinshi $x^3 + x + 1$. Ivyo vy’ukuri ntibishobora kugabanywa, kuko ntushobora kubigira factor ukoresheje imibare yose. Ikindi, bizotuma ugukubita kwose kw’ama Elements abiri kuzotanga umubare w’ibiharuro vyinshi w’ingero 2 canke hasi.


Reka dukore biciye ku karorero k’igikorwa ca kabiri dukoresheje umubare w’ibiharuro vyinshi $x^3 + x + 1$ nk’umugabanyi kugira ngo tugaragaze ingene bikora. Twibaze ko uguze Elements $x^2 + 1$ na $x^2 + x$ mu mugwi wacu **S**. Twebwe rero, turakeneye kubara invugo $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Ivyo bishobora kworoshwa gutya:



- $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
- $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
- $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$


Turazi ko $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ ishobora kugabanywa kuko umugabane ufise urugero rwo hejuru (4) kuruta umugabane (3).


Kugira ngo utangure, urashobora kubona ko imvugo $x^3 + x + 1$ ija muri $x^4 + x^3 + x^2 + x$ incuro $x$ zose hamwe. Ivyo ushobora kubigenzura mu kugwiza $x^3 + x + 1$ na $x$, ni ukuvuga $x^4 + x^2 + x$. Kubera ko ijambo rya nyuma riri ku rugero rumwe n’umugabane, ni ukuvuga 4, turazi ko ivyo bikora. Ushobora kubara igisigaye c'iyi nzira y'ugucapura na $x$ nk'uko bikurikira:



- $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x+1 =$
- $[x^3] \mod x^3 + x + 1 =$
- $x^3$


Rero tumaze kugabanya $x^4 + x^3 + x^2 + x$ na $x^3 + x + 1$ incuro $x$ zose hamwe, turonka igisigazwa ca $x^3$. Ivyo vyoshobora gusubira kugabanywa na $x^3 + x + 1$?


Mu buryo bw’ugutahura, vyoshobora gukwegera kuvuga ko $x^3$ itagishobora kugabanywa na $x^3 + x + 1$, kuko ijambo rya nyuma risa n’irinini. Ariko rero, nimwibuke ikiganiro twagiranye ku bijanye n’ugucapura ama vecteur imbere y’aho. Igihe cose umugabane ufise urugero runini canke rungana n’umugabane, iyo mvugo irashobora kurushiriza kugabanywa. Mu buryo bwihariye, imvugo $x^3 + x + 1$ ishobora kuja muri $x^3$ incuro 1 nyayo. Ivyo bisigaye biharurwa gutya:


$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$


Ushobora kuba wibaza igituma $(x^3) - (x^3 + x + 1)$ isuzuma ku $x + 1$ atari $-x - 1$. Ibuka ko igikorwa ca mbere c’umurima wacu gisobanurwamwo modulo 2. Ni co gituma gukuraho ama vecteur abiri bitanga igisubizo kimwe nyene n’ukwongerako ama vecteur abiri.


Kugira ngo ushire mu ncamake ugukubita kwa $x^2 + 1$ na $x^2 + x$: Iyo ugutije izo nkuru zibiri, ubona igiharuro c’ingero ya 4, $x^4 + x^3 + x^2 + x$, gikeneye kugabanywa modulo $x^3 + x + 1$. Igiharuro c’ingero ya 4 kigabanwa n’incuro $x^3 + x + 1$ neza na neza $x + 1$. Igisigaye inyuma yo kugabanya $x^4 + x^3 + x^2 + x$ na $x^3 + x + 1$ neza na neza $x + 1$ incuro ni $x + 1$. Ivyo ni ikintu kiri mu mugwi wacu $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.


Ni kuki ivyicaro vy’ukwagura bifise urufatiro rwa 2 ku migwi y’ibiharuro vyinshi, nk’akarorero kari hejuru, vyoba ngirakamaro ku bijanye n’ubuhinga bwo gukingira amakuru? Impamvu ni uko ushobora kubona ibiharuro biri mu biharuro vyinshi vy’ivyo bice, vyaba 0 canke 1, nk’uko Elements y’imirongo ibiri ifise uburebure bumwe. Itsinda **S** mu karorero kacu kari hejuru, nk'akarorero, ryoshobora gufatwa nk'itsinda **S** ririmwo imirongo yose y'ibice bibiri y'uburebure bwa 3 (000 gushika kuri 111). Ibikorwa biri kuri **S**, rero, birashobora no gukoreshwa mu gukora ibikorwa kuri izo nzira zibiri no gutanga inzira ibiri y'uburebure bumwe.


**Ivyiyumviro:**


[2] Ivyuma vy’ukwagura bica bihinduka bihushanye cane n’ubwenge. Aho kugira Elements y’imibare yose, bafise imigwi y’imibare myinshi. Ikindi, ibikorwa vyose bikorwa modulo zimwe zimwe zidashobora kugabanywa.



## Aligebra idasanzwe mu bikorwa

<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>


Naho ururimi rusanzwe n’ikiganiro kidasanzwe, iciyumviro c’umugwi ntigikwiye kuba kigoye cane gutahura. Ni gusa umugwi wa Elements hamwe n’igikorwa c’ibice bibiri, aho ubushobozi bw’ico gikorwa c’ibice bibiri kuri izo Elements buhuye n’ibintu bine rusangi. Itsinda rya Abeli ​​rifise gusa ikintu c’inyongera kizwi nka commutativité. Itsinda ry’inzinguzingu na ryo nyene ni ubwoko budasanzwe bw’itsinda ry’Abeli, ni ukuvuga iryo rifise umuyagankuba. Umurima ni gusa inyubakwa igoye cane iva ku ciyumviro c’ishimikiro c’umugwi.


Ariko nimba uri umuntu afise impengamiro yo gukora, woshobora kwibaza muri iki gihe uti: Ni nde abizi? Mbega kumenya umugwi umwe wa Elements ufise umukoresha ni umugwi, canke mbere umugwi wa Abelian canke w’ingendo, vyoba bifise akamaro nyakuri mw’isi? Mbega kumenya ikintu ni umurima?


Ata kwinjira mu ndondoro nyinshi, inyishu ni “egome”. Imigwi yatangujwe ubwa mbere mu kinjana ca 19 n’umuhinga mu vy’imibare w’Umufaransa yitwa Evariste Galois. Yarazikoresheje kugira ngo ashike ku nsozero zijanye n’ugutorera umuti ingano z’ibiharuro vyinshi zifise urugero rwo hejuru rw’itanu.


Kuva ico gihe, iciyumviro c’umugwi carafashije gutanga umuco ku ngorane zitari nke zo mu biharuro n’ahandi. Nk’akarorero, ashingiye kuri ivyo bintu, umuhinga mu vya fizike yitwa Murray-Gellman yarashoboye kumenya imbere y’igihe ko hariho ikintu imbere y’uko kibonwa vy’ukuri mu ngeragezwa. [3] Ku kindi kigereranyo, abahinga mu vy’ubuhinga bwa shimi bakoresha inyigisho y’imigwi kugira ngo bashire mu migwi imiterere y’ibihimba. Abahinga mu vy’imibare barakoresheje mbere iciyumviro c’umugwi kugira ngo bashike ku nsozero ku kintu gikomeye cane nk’urupapuro rwo ku ruhome!


Mu vy’ukuri kwerekana ko umugwi wa Elements ufise umukoresha umwe ari umugwi, bisigura ko ivyo uriko uradondora bifise uburinganire bumwe bumwe. Si uguhuza mu buryo busanzwe bw’iryo jambo, ahubwo mu buryo butaboneka cane. Kandi ivyo birashobora gutanga ubumenyi buhambaye ku bijanye n’imirongo ngenderwako n’ingorane zimwezimwe. Ivyiyumviro bikomeye cane biva mu buhinga bwa algèbre bitaboneka biraduha gusa amakuru y’inyongera.


Ikiruta vyose, uzobona akamaro k’imigwi y’ivyiyumviro vy’imibare n’ibice mu bikorwa biciye mu gukoresha kwavyo mu buhinga bwo gukingira amakuru, cane cane ubuhinga bwo gukingira amakuru y’urufunguzo rwa bose. Twaramaze kubona mu kiganiro cacu c’imirima, nk’akarorero, ingene imirima y’ukwagura ikoreshwa muri Rijndael Cipher. Uwo murongo tuzowukora mu *Gice ca 5*.


Kugira ngo mugire ibindi biganiro ku bijanye n’ubuhinga bwa algèbre abstrait, nobabwira ko mwosoma urutonde rwiza cane rw’amasanamu yerekeye algèbre abstrait rwanditswe na Socratique. [4] Nashaka canecane gusaba amavidewo akurikira: “Algèbre abstrait ni iki?”, “Insobanuro y’umugwi (yagutse)”, “Insobanuro y’impeta (yagutse)”, na “Insobanuro y’umurima (yagutse).” Aya mavidewo ane azoguha ubumenyi bw’inyongera ku vyinshi mu biganiro biri hejuru. (Ntitwavuga ivy’impeta, ariko umurima ni ubwoko budasanzwe bw’impeta gusa).


Kugira ngo uronke ibindi biganiro ku vyerekeye inyigisho y’imibare yo muri iki gihe, urashobora kuraba ibiganiro vyinshi biteye imbere ku bijanye n’ubuhinga bwo gukingira amakuru. Nashaka gutanga nk’impanuro igitabu ca Jonathan Katz na Yehuda Lindell citwa Intangamarara y’Ivy’Ubuhinga bwo Gushiramwo Amabanga canke igitabu ca Christof Paar na Jan Pelzl citwa Gutahura Ugushiramwo Amabanga kugira ngo tugire ibindi biganiro. [5]


**Ivyiyumviro:**


[3] Raba [Ividewo yo kuri YouTube] (v=NOMUnMuxDZY&feature=youtu.be)


[4] Socratique, [Igitabu c'Aligebra](https://www.socratique.com/ikiganiro/igitabu-c'Aligebra)


[5] Katz na Lindell, *Intango y’Ivy’Ubuhinga bwo Gukingira Amakuru*, igitabu ca 2, 2015 (Ikinyamakuru ca CRC: Boca Raton, FL). Paar na Pelzl, *Gutahura ubuhinga bwo gukingira amakuru*, 2010 (Igitabu c’i Berlin).




# Ububiko bw'ibanga buhuye

<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>



## Alice na Bob

<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>


Imwe mu mashami abiri akomeye y’ubuhinga bwo gukingira amakuru ni ubuhinga bwo gukingira amakuru buhuye. Harimwo imigambi yo gupfuka amakuru hamwe n’imigambi yerekeye ukumenya neza n’ubunyankamugayo. Gushika mu myaka ya 1970, ubuhinga bwo gupfuka amakuru bwose bwari kuba bugizwe n’imigambi y’ugupfuka amakuru ihuye.


Ikiganiro nyamukuru gitangura no kuraba imigambi y’ugushiramwo amakuru y’uruzi n’ugushiramwo amakuru y’uruzi. Twebwe rero, duhindukira tukaja ku makode y’ukwemeza ubutumwa, ari yo migambi yo kumenya neza ko ubutumwa ari ubw’ukuri kandi ko ari ubw’ukuri. Ubwa nyuma, turatohoza ingene imigambi yo gupfuka amakuru n’amakode y’ukwemeza ubutumwa bishobora guhurizwa hamwe kugira ngo habeho uguhanahana amakuru ata nkomanzi.


Iki gice kivuga ku migambi itandukanye y’ubuhinga bwo gukingira amakuru kuva ku bikorwa mu guca. Ikigabane gikurikira kiratanga insobanuro ido n’ido y’ugushiramwo amakuru n’ubuhinga bwo gushiramwo amakuru n’ubuhinga bwo gushiramwo amakuru buva ku bikorwa, ni ukuvuga RC4 na AES.


Imbere y’uko dutangura ikiganiro cacu ku bijanye n’ubuhinga bwo gukingira amakuru mu buryo buhuye, ndashaka gutanga amajambo makeyi ku bijanye n’ibigereranyo vya Alice na Bob biri muri iki kigabane be n’ibindi bikurikira.


___


Mu kwerekana ingingo ngenderwako z’ubuhinga bwo gukingira amakuru, abantu akenshi bizigira ingero zijanye na Alice na Bob. Nanje nzobigira.


Cane cane iyo uri mushasha mu vy’ubuhinga bwo gupfuka amakuru, birahambaye kumenya ko izo ngero za Alice na Bob zigamije gusa gukora nk’ingero z’ingingo ngenderwako n’inyubako z’ubuhinga bwo gupfuka amakuru mu kibanza coroshe. Ariko rero, ingingo ngenderwako n’inyubako birakoreshwa mu bintu vyinshi cane vy’ubuzima nyakuri.


Ibi bikurikira ni ingingo zitanu z’ingenzi zo kuguma mu muzirikanyi ku bijanye n’ingero zijanye n’ivy’ubuhinga bwa none:


1. Bishobora guhindurwa bitagoranye mu ngero n’ubundi bwoko bw’abakozi nk’amashirahamwe canke amashirahamwe ya leta.

2. Bishobora kwaguka bitagoranye kugira ngo bibemwo abakinyi batatu canke barenga.

3. Mu ngero, Bob na Alice ni abagira uruhara cane mu kurema ubutumwa bumwe bumwe no mu gukoresha imigambi y’ubuhinga bwo gukingira ubutumwa kuri ubwo butumwa. Ariko mu vy’ukuri, ahanini ubuhinga bwo guhanahana amakuru bukoreshwa n’ubuhinga bwa none. Iyo usuye urubuga ukoresheje umutekano wa transport Layer, nk’akarorero, ubuhinga bwo gukingira amakuru bukoreshwa na mudasobwa yawe be na server y’urubuga.

4. Mu bijanye n’itumanaho ry’ubuhinga bwa none, “ubutumwa” bwoherezwa biciye ku nzira y’itumanaho akenshi ni amapakete ya TCP/IP. Ivyo bishobora kuba ivy’ubutumwa bwo kuri e-mail, ubutumwa bwo kuri Facebook, ikiyago co kuri telefone, ukwimurira amadosiye, urubuga, gushiramwo porogarama n’ibindi. Si ubutumwa mu buryo bwa kera. Naho ari ukwo, abahinga mu vy’amakuru y’ibanga bazokworohereza kenshi ivyo mu kuvuga yuko ubutumwa ari, nk’akarorero, ubutumwa bwo kuri e-mail.

5. Ingero zisanzwe zishimika ku guhanahana amakuru biciye ku buhinga bwa none, ariko zishobora no kwaguka ku buryo bwa kera bwo guhanahana amakuru nk’amakete.



## Imigambi y'ububiko buhuye

<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>


Turashobora gusobanura neza **umugambi wo gushiramwo amakuru ugereranijwe** nk'umugambi wose wo gushiramwo amakuru ufise ubuhinga butatu:


1. **Algorithme y’uguhingura urufunguzo**, itanga urufunguzo rw’ibanga.

2. **Algorithme y’ugushiramwo amakuru**, ifata urufunguzo rw’ibanga n’inyandiko yoroshe nk’inyungu n’isohoka ry’inyandiko y’ibanga.

3. **Algorithme dedecryption**, ifata urufunguzo rw’ibanga n’inyandiko y’ibanga nk’inyungu igasohora inyandiko y’intango.


Mu bisanzwe umugambi wo gushiramwo amakuru—waba ari uwuringaniye canke utaringaniye—utanga urugero rw’ugushiramwo amakuru rushingiye ku nzira nyamukuru, aho gutanga amakuru nyayo.


Nk’akarorero, rimbura Salsa20, umugambi wo gupfuka amakuru ugereranijwe. Ishobora gukoreshwa n’uburebure bw’urufunguzo rw’ibice 128 n’ibice 256. Ihitamwo ryerekeye uburebure bw'urufunguzo rigira ingaruka ku bintu bimwebimwe bitobito vy'ubuhinga (umubare w'ibice mu buhinga kugira ngo ube nyawo).


Ariko umuntu ntashobora kuvuga ko gukoresha Salsa20 n’urufunguzo rw’ibice 128 ari umugambi wo gupfuka utandukanye n’uwa Salsa20 n’urufunguzo rw’ibice 256. Ivyiyumviro nyamukuru biguma ari uko biri. Igihe gusa ubuhinga nyamukuru buhindutse niho twovuga vy’ukuri imigambi ibiri itandukanye yo gupfuka.


Ivyiyumviro vy’ugushiramwo amakuru bihuye n’ibindi birafasha cane mu bihe vy’ubwoko bubiri: (1) Ivyo abakozi babiri canke barenga bariko baravugana bari kure kandi bashaka ko ibirimwo mu vyo bavugana biguma ari ibanga; na (2) izo aho umukozi umwe ashaka ko ibirimwo ubutumwa biguma ari ibanga mu kiringo cose.


Ushobora kubona ishusho y’ivyo (1) mu *Ishusho 1* iri musi. Bob ishaka kohereza ubutumwa $M$ kuri Alice mu ntambwe ndende, ariko ntishaka ko abandi bashobora gusoma ubwo butumwa.


Bob ibanza gupfuka ubutumwa $M$ n'urufunguzo rw'ibanga $K$. Na we rero, yohereza inyandiko y'ibanga $C$ kuri Alice. Alice amaze kwakira inyandiko y’ibanga, arashobora kuyisohora akoresheje urufunguzo $K$ maze agasoma inyandiko y’ibanga. Hamwe hariho umugambi mwiza wo gupfuka, umuterabwoba wese afata amajambo y’ibanga $C$ ntashobora kumenya ikintu na kimwe gihambaye nyaco ku butumwa $M$.


Ushobora kubona ishusho y’ivyo (2) mu *Ishusho ya 2* iri musi. Bob ishaka kubuza abandi kuraba amakuru amwamwe. Ibintu bisanzwe vyoshobora kuba ari uko Bob ari umukozi abika amakuru y’agaciro kuri mudasobwa yiwe, ayo makuru ata n’umwe yo hanze canke abo bakorana bakwiye kuyasoma.


Bob ipfuka ubutumwa $M$ ku gihe $T_0$ n'urufunguzo $K$ kugira ngo ivemwo inyandiko y'ibanga $C$. Igihe $T_1$ arasubira gukenera ubutumwa, maze agaca afungura inyandiko y'ibanga $C$ n'urufunguzo $K$. Umuntu wese yoba yarahuye n’inyandiko y’ibanga $C$ muri ico gihe ntiyari akwiye gushobora gukuramwo ikintu gihambaye ku bijanye na $M$.



*Ishusho ya 1: Ibanga mu kirere*


![Figure 1: Secrecy across space](assets/en/005.webp "Figure 1: Secrecy across space")



*Ishusho ya 2: Ibanga mu gihe cose*



![Figure 2: Secrecy across time](assets/en/006.webp "Figure 2: Secrecy across time")




## Akarorero: Igiharuro c'ihinduka

<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>


Mu kigabane ca 2, twahuye n’igiharuro c’ihinduka, kikaba ari akarorero k’umugambi woroshe cane wo gupfuka amakuru. Reka tuvyitegereze hano.


Twibaze ko inkoranyamagambo *D* ingana inyuguti zose zo mu nyuguti z’icongereza, mu buryo zikurikirana, n’umugwi w’imibare $\{0,1,2,\dots,25\}$. Niwiyumvire ubutumwa bushoboka **M**. Igiharuro c'uguhindura ni, rero, umugambi wo gupfuka usobanurwa gutya:



- Hitamwo mu buryo butari bwo urufunguzo $k$ mu rutonde rw'urufunguzo rushoboka **K**, aho **K** = $\{0,1,2,\utudomo,25\}$
- Gushiramwo ubutumwa $m \in$ **M**, nk'uko bikurikira:
    - Itandukanye $m$ mu nyuguti zayo zimwe zimwe $m_0, m_1,\utudomo, m_i, \utudomo, m_l$
    - Guhindura buri $m_i$ mu mubare hakurikijwe *D*
    - Ku buri $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Guhindura buri $c_i$ mu nyuguti hakurikijwe *D*
    - Hanyuma ushire hamwe $c_0, c_1,\utudomo, c_l$ kugira ngo ubone inyandiko y'ibanga $c$
- Gusobanura umwandiko w'ibanga $c$ nk'uko bikurikira:
    - Guhindura $c_i$ yose mu mubare hakurikijwe *D*
    - Ku buri $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Guhindura buri $m_i$ mu nyuguti hakurikijwe *D*
    - Hanyuma ushire hamwe $m_0, m_1,\utudomo, m_l$ kugira ngo ubone ubutumwa bw'intango $m$ .


Igituma shift cipher iba umugambi wo gupfuka ugereranijwe ni uko urufunguzo rumwe rukoreshwa mu gupfuka no gukuraho. Nk'akarorero, dufate ko ushaka gupfuka ubutumwa “DOG” ukoresheje shift cipher, kandi ko wahisemwo "24" nk'urufunguzo. Gushiramwo ubutumwa n’urwo rufunguzo vyotuma haba “BME”. Uburyo bumwe rudende bwo kugarura ubutumwa bw'umwimerere ni ugukoresha urufunguzo rumwe, "24", ku bijanye n'igikorwa co gufungura.


Iyi Shift cipher ni akarorero k'**cipher y'ugusubirira inyuguti imwe**: umugambi wo gupfuka aho inyuguti y'inyandiko y'ibanga igumaho (i.e., inyuguti imwe gusa ikoreshwa). Dufashe ko ubuhinga bwo gusobanura ari ubw'itegeko, ikimenyetso cose mu nyandiko y'ibanga y'isubirizwa gishobora gushika ku kimenyetso kimwe mu nyandiko y'ibanga.


Kugeza mu myaka ya 1700, ibikorwa vyinshi vyo gushiramwo amakuru vyishingikirije cane ku majambo y'ibanga y'inyuguti imwe, naho kenshi ayo majambo yari akomeye cane kuruta amajambo y'ibanga y'ihinduka. Nk’akarorero, woshobora guhitamwo urudome rumwe mu nyuguti z’inyuguti ku rudome rwose rw’inyandiko y’intango mu gihe urudome rumwe rumwe ruboneka rimwe gusa mu nyuguti z’inyandiko z’ibanga. Ivyo bisigura ko woba ufise imfunguruzo z’ibanga 26 zishoboka, zari nini cane mu gihe c’imbere ya mudasobwa.


Zirikana ko uzohura n’ijambo **cipher** cane mu vy’ubuhinga bwo gukingira amakuru. Menya ko iri jambo rifise insobanuro zitandukanye. Nkako, ndazi n’imiburiburi insobanuro zitanu zitandukanye z’iryo jambo mu bijanye n’ubuhinga bwo gukingira amakuru.


Mu bihe bimwebimwe ryerekeza ku mugambi wo gupfuka, nk’uko bigenda mu gupfuka Shift no mu gusubirira inyuguti imwe. Ariko rero, iryo jambo rishobora kandi kwerekeza ku buryo budasanzwe ku bijanye n’ubuhinga bwo gupfuka, urufunguzo rw’ibanga canke gusa amajambo y’ibanga y’uwo mugambi uwo ari wo wose wo gupfuka.


Ubwa nyuma, ijambo cipher rishobora kandi kwerekeza ku nzira nyamukuru ushobora gukoresha mu kwubaka imigambi y’ubuhinga bwo gukora amakuru. Ivyo bishobora kubamwo ubuhinga butandukanye bwo gupfuka amakuru, ariko kandi n’ubundi bwoko bw’imigambi yo gupfuka amakuru. Ubwo busobanuro bw’iryo jambo buraba ngirakamaro mu bijanye n’amajambo y’ububiko (raba igice kivuga ngo “Amajambo y’ububiko” aha hepfo).


Ushobora kandi guhura n'amajambo **gusobanura** canke **gusobanura**. Aya majambo ni amajambo amwe gusa asobanura gupfuka no gufungura.



## Ibitero vy’inkomezi z’agahomerabunwa n’ingingo ngenderwako ya Kerckhoff

<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>


Igiharuro c’ihinduka ni umugambi wo gukingira amakuru udatekanye cane, n’imiburiburi mw’isi ya none. [1] Umuntu atera yoshobora gusa kugerageza gukuraho inyandiko iyo ari yo yose y’ibanga afise imfunguruzo zose 26 zishoboka kugira ngo abone igisubizo gifise insiguro. Ubwo bwoko bw’igitero, aho uwutera aba ariko aragendagenda gusa mu mfunguruzo kugira ngo abone ico gikora, buzwi kw’izina rya **igitero c’inguvu z’agahomerabunwa** canke **ugushaka imfunguruzo zishitse**.


Kugira ngo umugambi wose wo gupfuka ushitse ku ciyumviro gitoyi c'umutekano, utegerezwa kuba ufise urutonde rw'imfunguruzo zishoboka, canke **keyspace**, ari nini cane ku buryo ibitero vy'inguvu z'agahomerabunwa bidashoboka. Ivyiyumviro vyose vyo gupfuka amakuru vyo muri iki gihe birahuye n’ico kigereranyo. Ni **ingingo ngenderwako y’ikibanza c’urufunguzo gihagije**. Ingingo ngenderwako nk’iyo nyene irakoreshwa canecane mu bwoko butandukanye bw’imigambi y’ubuhinga bwo gukingira amakuru.


Kugira ngo ubone ubunini bw’umwanya munini w’urufunguzo mu migambi yo gupfuka amakuru yo muri iki gihe, dufate ko dosiye yashizwemwo urufunguzo rw’ibice 128 hakoreshejwe ubuhinga bwo gupfuka amakuru buteye imbere. Ivyo bisigura ko umuterabwoba afise urutonde rw'imfunguruzo z'amadolari 2^{128}$ akeneye gucamwo kugira ngo atere inguvu z'agahomerabunwa. Amahirwe yo kuroranirwa 0.78% n'iyi nzira yosaba ko uwutera agendagenda mu mfunguruzo zishika $2.65 \incuro 10^{36}$.


Twibaze ko twiyumvira ko umuterabwoba ashobora kugerageza imfunguruzo $10^{16}$ ku segonda (ni ukuvuga imfunguruzo 10 quadrillion ku segonda). Kugira ngo agerageze 0.78% y'imfunguruzo zose ziri mu kibanza c'imfunguruzo, igitero ciwe cobwirizwa kumara $2.65 \incuro 10^{20}$ amasegonda. Ivyo ni nk’imyaka amamiliyaridi 8,4. Rero mbere n’igitero c’inkomezi z’agahomerabunwa gikorwa n’umwansi w’ububasha buteye isoni ntibishoboka iyo umuntu akoresheje umugambi wo gukingira amakuru w’ibice 128 wo muri iki gihe. Iyi ni yo ngingo ngenderwako y’ikibanza ihagije iriko irakina.


Mbega shift cipher yoba itekanye cane iyo uwuyitera atazi ubuhinga bwo gupfuka? Kumbure, ariko si vyinshi.


Uko biri kwose, ubuhinga bwa none bwo gukingira amakuru, buhora bwiyumvira ko umutekano w’umugambi uwo ari wo wose wo gukingira amakuru ushingiye gusa ku kugumya ibanga ry’urufunguzo rw’ibanga. Uwutera umuntu yama yiyumviriwe ko azi ibindi vyose, harimwo n’aho ubutumwa buri, aho urufunguzo ruri, urufunguzo rw’ibanga, uburyo bwo guhitamwo urufunguzo, uburyo bwo gupfuka, n’uburyo bwo gufungura.


Iciyumviro c’uko umutekano w’umugambi wo gupfuka amakuru ushobora kwizigira gusa ibanga ry’urufunguzo rw’ibanga kizwi nka **Ingingo ya Kerckhoffs**.


Nk’uko Kerckhoffs yabishaka mu ntango, iyo ngingo ngenderwako ikoreshwa gusa ku migambi y’ugushiramwo amakuru y’ibintu bihuye. Ariko rero, ingingo ngenderwako rusangi irakora no ku yindi migambi yose yo muri iki gihe y’ubuhinga bwo gukora amakuru y’ibanga: Igishushanyo cose c’ubuhinga bwo gukora amakuru y’ibanga ntigitegerezwa gusaba ko kiba ibanga kugira ngo kibe gitekanye; ibanga rishobora gushika gusa ku mirongo (s) y'amakuru, cane cane urufunguzo rw'ibanga.


Ingingo ngenderwako y’i Kerckhoffs ni yo ihambaye cane mu bijanye n’ubuhinga bwo gukingira amakuru mu gihe ca none kubera imvo zine. [2] Ica mbere, hariho gusa umubare mutoyi w’imigambi y’ubuhinga bwo gukingira amakuru ku bwoko bumwe bumwe bw’ibikorwa. Nk’akarorero, ubuhinga bwinshi bwo gukoresha ubuhinga bwa none bukoresha ubuhinga bwa Rijndael. Rero ibanga ryawe ku bijanye n’umugambi w’umugambi ni rito cane. Ariko rero, hariho uburyo bwinshi bwo guhinduranya mu kuzigama urufunguzo rw’ibanga rw’ibanga ry’ibanga rya Rijndael.


Ubwa kabiri, biroroshe gusubirira urudodo rw’amakuru amwamwe kuruta umugambi wose wo gukora amakuru y’ibanga. Twibaze ko abakozi bo mw’ishirahamwe bose bafise porogarama imwe yo gupfuka amakuru, kandi ko abakozi babiri bose bafise urufunguruzo rw’ibanga rwo kuvugana n’abandi mu ibanga. Ivyiza vy’ingenzi ni ikibazo muri iki gihe, ariko n’imiburiburi iyo sosiyete yoshobora kuguma ifise porogarama n’ivyo bihungabanya umutekano. Iyo iyo sosiyete yizigiye ibanga ry’uwo mugambi, rero ukurenga kuri iryo banga kwosaba ko basubiriza porogarama zose.


Ica gatatu, ingingo ngenderwako ya Kerckhoffs iremeza ko habaho uguhuza n’uguhuza hagati y’abakoresha imigambi y’ubuhinga bwo gukora amakuru. Ivyo birafise inyungu nyinshi cane ku bijanye n’ugukora neza. Nk’akarorero, biragoye kwiyumvira ingene abantu amamiliyoni boshobora kwifatanya n’urubuga rwa Google buri musi, nimba ubwo mutekano busaba ko imigambi y’ubuhinga bwa none iguma ari ibanga.


Ica kane, ingingo ngenderwako ya Kerckhoff iremeza ko abantu bose bashobora gusuzuma imigambi y’ubuhinga bwo gukora amakuru y’ibanga. Ubwo bwoko bw’isuzuma burakenewe cane kugira ngo umuntu ashike ku migambi y’ubuhinga bwo gukingira amakuru itekanye. Nk'akarorero, ubuhinga nyamukuru bwo gukora amakuru y'ibanga, ubuhinga bwa Rijndael, bwavuye mu mahiganwa yateguwe n'Ikigo c'Igihugu c'Ivyagezwe n'Ikoranabuhanga hagati ya 1997 na 2000.


Uburyo bwose bugerageza gushika ku **umutekano biciye mu mwijima** ni ubwo bwishingikiriza ku kugumiza ibanga ido n’ido ry’imiterere yabwo n’/canke ingene bushirwa mu ngiro. Mu bijanye n’ubuhinga bwo gukingira amakuru, ivyo vyoba ari uburyo bwishingikirije ku kuguma ari ibanga ry’ibintu vy’ido n’ido vy’umugambi w’ugukingira amakuru. Rero umutekano biciye ku mwijima uratandukanye cane n’ingingo ngenderwako ya Kerckhoffs.


Ubushobozi bwo gufungura bwo gukomeza uburyo n’umutekano na bwo burashika cane mw’isi ya digitale kuruta ubuhinga bwo gukingira amakuru gusa. Nk’akarorero, ibikoresho vya Linux vy’ubuntu kandi vyuguruye nka Debian, muri rusangi birafise ivyiza vyinshi kuruta ibindi bikoresho vya Windows na MacOS mu bijanye n’ubuzima bwite, ugushikama, umutekano, n’uguhinduranya. Naho ivyo bishobora kuba bifise imvo nyinshi, ingingo ngenderwako ihambaye kuruta izindi zose kumbure ari, nk’uko Eric Raymond yabivuze mu kiganiro ciwe kizwi cane citwa “The Cathedral and the Bazaar,” ko “iyo umuntu afise amaso ahagije, ibikoko vyose ntibigira igitutu.” [3] Ubwo bwenge bw’ingingo ngenderwako y’ubwoko bw’amasinzi ni bwo bwatumye Linux iroranirwa cane.


Umuntu ntashobora kwigera avuga ata gukeka ko umugambi w'ubuhinga bwo gukingira amakuru "utekanye" canke "udatekanye." Ahubwo, hariho ivyiyumviro bitandukanye vy’umutekano ku migambi y’ubuhinga bwo gukora amakuru y’ibanga. Buri **insobanuro y’umutekano w’ubuhinga bwa none** itegerezwa gusobanura (1) intumbero z’umutekano, hamwe n’(2) ubushobozi bw’uwutera. Gusuzuma imigambi y’ubuhinga bwa none ugereranije n’iciyumviro kimwe canke vyinshi vy’umutekano bitanga ubumenyi ku bijanye n’ingene ikoreshwa be n’aho igarukira.


Naho tutazokwinjira mu ndondoro zose z’ivyiyumviro bitandukanye vy’umutekano w’ubuhinga bwa none, ukwiye kumenya ko hariho ivyiyumviro bibiri biri hose ku vyiyumviro vyose vy’ubuhinga bwa none vyerekeye umutekano w’ubuhinga bwa none bijanye n’imigambi y’uburinganire n’ubudasa (kandi mu buryo bumwe bumwe ku bindi bihimba vy’ubuhinga bwa none):



- Ubumenyi bw’uwo muterabwoba ku bijanye n’uwo mugambi burahuye n’ingingo ngenderwako ya Kerckhoffs.
- Uwutera ntashobora gutera inguvu z’agahomerabunwa kuri uwo mugambi. Mu buryo bwihariye, ivyerekanwa vy’iterabwoba vy’ivyiyumviro vy’umutekano vy’ubuhinga bwa none ntivyemera mbere ibitero vy’inguvu z’agahomerabunwa, kuko vyiyumvira ko ivyo atari vyo bihambaye.



**Ivyiyumviro:**


[1] Nk’uko Seutonius abivuga, igiharuro c’urufunguzo (shift cipher) gifise agaciro k’urufunguzo kadahinduka ka 3, ni co cakoreshwa na Julius Caesar mu guhanahana amakuru yiwe y’igisirikare. Rero A yokwama ari D, B yama ari E, C yama ari F, n’ibindi. Iyi verisiyo yihariye y’ibara ry’ihinduka, rero, ryamenyekanye kw’izina rya **Caesar Cipher** (naho mu vy’ukuri atari ibara mu busobanuro bwa none bw’iryo jambo, kuko agaciro k’urufunguzo kagumaho). Igitabu ca Kayisari gishobora kuba cari gifise umutekano mu kinjana ca mbere imbere ya Kristu, nimba abansi b’Uburoma batamenyereye cane gukingira. Ariko biragaragara ko atari umugambi utekanye cane mu bihe vya none.


[2] Jonathan Katz na Yehuda Lindell, _Intango y’Ivy’Ikinyamakuru c’Igihugu_, Ikinyamakuru ca CRC (Boca Raton, FL: 2015), urupapuro rwa 10. 7f.


[3] Ikete rya Eric Raymond, “Ingoro y’Imana n’Isoko,” ryashikirijwe mw’Ikoraniro ry’Ivya Linux, i Würzburg, mu Budagi (27 Rusama 1997). Hariho insiguro zitari nke zakurikiyeho ziboneka be n’igitabu. Ivyo navuze ni ivyo ku rupapuro rwa 30 rw’igitabu: Eric Raymond, _Ikatederali n’Isoko: Ivyiyumviro ku Linux n’Isoko ry’Igihugu ry’Umunyagihugu w’Impinduka_, vyasubiwemwo edn. (2001), O’Reilly: Igisagara ca Sebastopoli, muri Californie.



## Amajambo y'uruzi

<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>


Ivyiyumviro vy'ugushiramwo amakuru bihuye bigabanywamwo ubwoko bubiri: **ibiharuro vy'uruzi** na **ibiharuro vy'amabuye**. Ariko rero, iyo ntandukaniro iratera ingorane, kuko abantu bakoresha ayo majambo mu buryo budahuye. Mu bice bikeyi bikurikira, nzoshiraho itandukaniro mu buryo mbona ko ari bwo bwiza. Ariko rero, urakwiye kumenya ko abantu benshi bazokoresha ayo majambo mu buryo butandukanye n’ubwo nashizeho.


Reka tubanze duhindukire ku ma ciphers y’uruzi. **stream cipher** ni umugambi wo gushiramwo amakuru ugereranijwe aho gushiramwo amakuru agizwe n'intambwe zibiri.


Ica mbere, urudodo rungana n’uburebure bw’inyandiko yoroshe rusohoka biciye ku rufunguzo rw’ibanga. Uyu murongo witwa **umurongo w'urufunguzo**.


Inyuma y’aho, umurongo w’urufunguzo urafatanywa mu biharuro n’inyandiko yoroshe kugira ngo haboneke inyandiko y’ibanga. Iryo huriro ni igikorwa ca XOR. Ku bijanye no gukuraho amakuru, ushobora guhindura gusa igikorwa. (Ibuka ko $A \oplus B = B \oplus A$, mu gihe $A$ na $B$ ari imirongo y'ibice. Rero urutonde rw'igikorwa ca XOR mu nzira y'uruzi ntaco rumaze ku gisubizo. Uwo muco uzwi nka **uguhinduranya**.)


Igiharuro c'umugezi wa XOR kigaragara mu *Ishusho 3*. Ubanza gufata urufunguzo rw’ibanga $K$ ukarukoresha kugira ngo generate urufunguzo. Urufunguzo rero, rufatanywa n'inyandiko rusangi biciye ku gikorwa ca XOR kugira ngo haboneke inyandiko y'ibanga. Umukozi wese yakira amajambo y’ibanga ashobora kuyafungura bitagoranye iyo afise urufunguzo $K$. Ico akeneye gukora n’uguhingura urufunguzo rw’urufunguzo igihe cose inyandiko y’ibanga hakurikijwe uburyo bwategekanijwe bw’umugambi maze akayi XOR n’inyandiko y’ibanga.



*Ishusho ya 3: Igiharuro c'umugezi wa XOR*


![Figure 3: An XOR stream cipher](assets/en/007.webp "Figure 3: An XOR stream cipher")


Nimwibuke ko umugambi wo gushiramwo amakuru ari nk'akarorero k'ugushiramwo amakuru n'ubuhinga bumwe, aho kuba ivyerekeye nyavyo. Mu kwagura, uruzi cipher ni nk'akarorero k'ububiko aho ushobora gukoresha imfunguruzo z'uburebure butandukanye. Naho uburebure bw’urufunguzo bushobora kugira ico bukoze ku bintu bimwebimwe bitobito vyo muri uwo mugambi, ntibuzogira ico bukoze ku buryo bwawo bw’ingenzi.


Igiharuro c’uguhindura ni akarorero k’igiharuro c’uruzi coroshe cane kandi kidatekanye. Ukoresheje urudome rumwe (urufunguzo rw’ibanga), urashobora gutanga uruhererekane rw’inyuguti zingana n’uburebure bw’ubutumwa (urufunguzo). Uwo murongo w'urufunguzo rero, ufatanywa n'inyandiko rusangi biciye ku gikorwa ca modulo kugira ngo haboneke inyandiko y'ibanga. (Iyi nzira ya modulo ishobora kworoshwa ikaba igikorwa ca XOR igihe ugereranya inyuguti mu bice).


Akandi karorero kazwi cane k’uruzitiro rw’umugezi ni **uruzitiro rwa Vigenere**, inyuma ya Blaise de Vigenere yaruteye imbere bimwe bishitse mu mpera z’ikinjana ca 16 (naho abandi bari barakoze ibikorwa vyinshi vy’imbere y’aho). Ni akarorero k'**inyuguti nyinshi zo gusubirira inyuguti**: umugambi wo gupfuka aho inyuguti z'inyuguti z'ikimenyetso c'inyandiko rusangi zihinduka bivanye n'aho ziri mu nyandiko. Mu buryo butandukanye n’inyandiko y’inyandiko y’inyandiko imwe, ibimenyetso vy’inyandiko y’inyandiko bishobora gufatanywa n’ikimenyetso c’inyandiko y’inyandiko yoroshe kirenze kimwe.


Uko ubuhinga bwo gushiramwo amakuru bwagenda burakundwa cane mu Buraya bwo mu gihe c'Ivugurura, ni ko n'ugusesangura amakuru—ni ukuvuga gucapura amajambo y'ibanga—cane cane, hakoreshejwe **ugusesangura incuro**. Iryo rya nyuma rikoresha imibare idasanzwe mu rurimi rwacu kugira ngo rimene amajambo y'ibanga, kandi ryavumbuwe n'intiti z'ikinyaarabu zisanzwe ziri mu kinjana ca cenda. Ni ubuhinga bukora neza cane cane ku nyandiko ndende. Kandi mbere n'ibiharuro vy'inyuguti imwe vy'ubuhinga bwa none ntivyari bigihagije ku bijanye n'ugusesangura incuro mu myaka ya 1700 mu Buraya, cane cane mu vy'igisirikare no mu vy'umutekano. Uko igiharuro ca Vigenere catanga iterambere rikomeye mu bijanye n'umutekano


Mu kuvuga mu buryo butamenyerewe, umugambi wo gupfuka amakuru ukora gutya:


1. Hitamwo ijambo ry’inyuguti nyinshi nk’urufunguzo rw’ibanga.

2. Ku butumwa ubwo ari bwo bwose, shiraho urudome rwo guhindura urudome rwose rw’ubutumwa ukoresheje urudome rujanye n’iryo jambo ry’ingenzi nk’urudome rwo guhindura.

3. Niba waraciye mw’ijambo ry’ingenzi ariko ukaba utaramenya neza igisomwa gisanzwe, wongere ukoreshe inyuguti z’ijambo ry’ingenzi nk’inyuguti zihuye n’izo nyandiko zisigaye.

4. Mubandanye muri iyo nzira gushika ubutumwa bwose bushizwe mu mfuruka.


Nk'akarorero, dufate ko urufunguzo rwawe rw'ibanga ari "GOLD" kandi ushaka gupfuka ubutumwa "CryptoGRAPHY". Iyo bimeze gutyo, wobandanya gutya ukurikije igiharuro ca Vigenère:



- $c_0 = [(2 + 6) \umuhinduzi 26] = 8 = I$
- $c_1 = [(17 + 14) \mod 26] = 5 = F$
- $c_2 = [(24 + 11) \umuhinduzi 26] = 9 = J$
- $c_3 = [(15 + 3) \umuhinduzi 26] = 18 = S$
- $c_4 = [(19 + 6) \umuhinduzi 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \umuhinduzi 26] = 17 = R$
- $c_7 = [(17 + 3) \umuhinduzi 26] = 20 = U$
- $c_8 = [(0 + 6) \uburyo 26] = 6 = G$
- $c_9 = [(15 + 14) \umuhinduzi 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$


Gutyo, inyandiko y'ibanga $c$ = "IFJSZCRUGDSB".


Ikindi kigereranyo kizwi cane c'uruzi cipher ni **pad y'igihe kimwe**. Na pad y'igihe kimwe, ushobora gusa kurema urudodo rw'ibice vy'imburakimazi nk'ubutumwa bw'inyandiko rusangi maze ugatanga inyandiko y'ibanga biciye ku gikorwa ca XOR. Ku bw’ivyo, urufunguzo rw’ibanga n’urufunguzo rw’urufunguzo bingana n’igipapuro c’igihe kimwe.


Naho Shift cipher na Vigenere ciphers zidatekanye cane mu bihe vya none, pad y’igihe kimwe iratekanye cane iyo ikoreshejwe neza. Kumbure igikorwa camenyekanye cane c’ivyo bikoresho vy’igihe kimwe cari, n’imiburiburi gushika mu myaka ya 1980, ku **umurongo w’i Washington-Moscow**. [4]


Uwo murongo w’ubuhinga ni umurongo w’itumanaho hagati ya Washington na Moscou ku bibazo vyihutirwa washizweho inyuma y’ingorane y’imizinga ya Cuba. Ivy’ubuhinga bwa none vyarahindutse uko imyaka yagenda irarenga. Ubu, irimwo umugozi w’amatara utaziguye be n’amahuza abiri y’inyenyeri (kugira ngo umuntu ashobore gukoresha ubutumwa bwo kuri interineti), ivyo bikaba bituma umuntu ashobora gukoresha ubutumwa bwo kuri e-mail n’ubutumwa bwo mu nyandiko. Iryo huriro rihera mu bibanza bitandukanye muri Amerika. Pentagon, Inzu y’Ubwami, n’Umusozi Raven Rock ni vyo bimenyekana ko ari vyo bihera. Mu buryo butandukanye n’ivyo abantu benshi biyumvira, iyo nzira y’ubutumwa ntiyigeze ikoresha amatelefone.


Mu vy’ukuri, umugambi w’igihe kimwe wo gukoresha pad warakoze gutya. Washington na Moscou zompi zogira imibare ibiri y’imburakimazi. Igitigiri kimwe c’imibare y’imburakimazi, cakozwe n’Abarusiya, cari kijanye n’ugushiramwo no gufungura ubutumwa bwose bwo mu rurimi rw’ikirusiya. Igitigiri kimwe c’imibare y’imburakimazi, cakozwe n’Abanyamerika, cari kijanye n’ugushiramwo no gukuraho ubutumwa bwose bwo mu rurimi rw’icongereza. Rimwe na rimwe, imibare myinshi y’imburakimazi yoshikirizwa ku rundi ruhande n’abarungika ubutumwa bizigirwa.


Washington na Moscou rero vyarashoboye kuvugana mu mpisho bikoresheje iyo mibare y’imburakimazi yo guhingura amapadi akoreshwa rimwe gusa. Igihe cose woba ukeneye kuvugana, wokoresha igice gikurikira c’imibare y’imburakimazi ku bw’ubutumwa bwawe.


Naho igipapuro co gukoresha rimwe gifise umutekano mwinshi cane, gifise utunenge dukomeye: urufunguruzo rukeneye kuba rurerure nk’ubutumwa kandi nta gice c’ico gipapuro co gukoresha rimwe gishobora gusubira gukoreshwa. Ivyo bisigura ko ukeneye kuguma ukurikirana aho uri mu gitabu c’igihe kimwe, ukabika umubare munini w’ibice, n’ibice vy’imburakimazi vya Exchange n’abagenzi bawe rimwe na rimwe. Ivyo bituma iyo pad y’igihe kimwe idakoreshwa kenshi mu bikorwa.


Ahubwo, amajambo y’uruzi akoreshwa cane mu bikorwa ni **amajambo y’uruzi y’ibinyoma**. Salsa20 n’iyindi nzira ifitaniye isano cane yitwa ChaCha ni ingero z’ibiharuro vy’uruzi vy’ibinyoma bikoreshwa cane.


Na izo pseudorandom stream ciphers, ubanza guhitamwo urufunguzo K rugufi kuruta uburebure bw'inyandiko rusangi. Mwene ukwo rufunguzo K rw’imburakimazi akenshi ruremwa na mudasobwa yacu ishingiye ku makuru atamenyekana ayo yegeranya uko igihe kigenda kirarenga, nk’igihe kiri hagati y’ubutumwa bwo ku rubuga, ukuntu imbeba yinyiganza, n’ibindi.


Urufunguzo rw'imburakimazi $K$ rero rwinjira mu nzira yo kwagura irema urufunguzo rw'imburakimazi nk'ubutumwa. Ushobora gusobanura neza igihe umurongo w'urufunguzo ukeneye kuba (nk'akarorero, ibice 500, ibice 1000, ibice 1200, ibice 29.117, n'ibindi).


Uruzitiro rw'urufunguzo rw'ibinyoma rugaragara *nk'aho* rwatowe mu buryo butari bwo mu rwego rw'imirongo yose ifise uburebure bumwe. Ku bw’ivyo, gupfuka amakuru hakoreshejwe urufunguzo rw’urufunguzo rw’ibinyoma bisa n’aho vyakozwe hakoreshejwe urufunguzo rw’igihe kimwe. Ariko ivyo, birumvikana ko atari ko biri.


Kubera ko urufunguzo rwacu rw’ibanga ari rugufi kuruta urufunguzo kandi ubuhinga bwacu bwo kwagura bukeneye kuba ubw’agaciro kugira ngo uburyo bwo gupfuka/gukuraho urufunguzo bukore, si urufunguzo rwose rw’ubwo burebure bwihariye rwari gushobora gushika nk’igisubizo kiva mu gikorwa cacu co kwagura.


Twibaze nk’akarorero ko urufunguzo rwacu rw’ibanga rufise uburebure bw’ibice 128 kandi ko dushobora kurushira mu buhinga bwo kwagura kugira ngo dukore urufunguzo rurerure cane, tuvuge ko rw’ibice 2.500. Nk'uko ubuhinga bwacu bwo kwagura bukeneye kuba ubugenzuzi, ubuhinga bwacu burashobora guhitamwo $1/2^{128}$ imirongo ifise uburebure bw'ibice 2.500. Rero mwene iyo nzira y’urufunguzo ntishobora kwigera itorwa mu buryo butari bwo mu mirongo yose y’uburebure bumwe.


Insobanuro yacu y’uruzitiro rw’uruzitiro rufise imice ibiri: (1) uruzitiro rw’urufunguzo igihe cose umwandiko usanzwe uvutse ufashijwe n’urufunguzo rw’ibanga; kandi (2) iyo nzira y’urufunguzo ifatanijwe n’inyandiko yoroshe, mu bisanzwe biciye ku gikorwa ca XOR, kugira ngo haboneke inyandiko y’ibanga.


Rimwe na rimwe abantu barasobanura neza cane ivyangombwa (1), mu kwemeza ko umurongo w’urufunguzo utegerezwa kuba ari pseudorandom. Ivyo bisigura ko ata cipher y’uguhindura, canke iyo pad y’igihe kimwe yobonwa ko ari cipher y’uruzi.


Mu kubona kwanje, gusobanura ivyangombwa (1) mu buryo bwagutse cane bitanga uburyo bworoshe bwo gutunganya imigambi yo gupfuka. Ikindi, bisigura ko tudategerezwa guhagarika kwita umugambi kanaka wo gupfuka amakuru ngo ni umugezi kubera gusa twize ko mu vy’ukuri udashingiye ku nzira z’urufunguzo z’ibinyoma.


**Ivyiyumviro:**


[4] Ingoro y’ivya kera y’ivy’ubuhinga bwa none, “Umurongo w’ivy’ubuhinga bwa none wo muri Washington-Moscow,” 2013, ushobora kuyironka ku rubuga rwa Crypto.




## Ububiko bw'amabanga

<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>


Uburyo bwa mbere **block cipher** itahurwa cane ni nk'ikintu c'intango kuruta cipher y'umugezi: Algorithme nyamukuru ikora ihinduka ry'uburebure ku murongo w'uburebure bukwiye ifashijwe n'urufunguzo. Iyi algorithme ishobora gukoreshwa mu guhingura imigambi yo gupfuka amakuru kumbure n’ubundi bwoko bw’imigambi yo gupfuka amakuru.


Kenshi, igiharuro c’amabara gishobora gufata imirongo y’inyungu y’uburebure butandukanye nk’ibice 64, 128 canke 256, hamwe n’imfunguruzo z’uburebure butandukanye nk’ibice 128, 192 canke 256. Naho ibintu bimwebimwe vyo muri algorithme bishobora guhinduka bivanye n’ivyo bihinduka, algorithme nyamukuru ntihinduka. Iyo bishika, twovuga ama ciphers abiri atandukanye y’amabuye. Zirikana ko ikoreshwa ry'amajambo y'ishimikiro y'ubuhinga hano ari co kimwe n'iry'imigambi yo gupfuka.


Igishushanyo c'ingene block cipher ikora gishobora kubonwa ku *Ishusho ya 4* iri musi. Ubutumwa $M$ bw'uburebure $L$ n'urufunguzo $K$ bikora nk'inyungu ku cipher ya Block. Isohora ubutumwa $M'$ bw'uburebure $L$. Urufunguzo ntirukeneye kuba rungana n'uburebure bwa $M$ na $M'$ ku bimenyetso vyinshi vy'amabuye.


*Ishusho ya 4: Igiharuro c'ibarabara*


![Figure 4: A block cipher](assets/en/008.webp "Figure 4: A block cipher")


Igiharuro c'amabuye ubwaco si umugambi wo gupfuka. Ariko block cipher ishobora gukoreshwa n'uburyo butandukanye bwo gukora kugira ngo haboneke imigambi itandukanye yo gupfuka. Uburyo bwo gukora bwongerako gusa ibindi bikorwa hanze y'ibanga ry'ibarabara.


Kugira ngo tubone ingene ivyo bikora, dufate ko hariho urufunguzo rw’ibanga (BC) rusaba urudodo rw’injiza rw’ibice 128 n’urufunguzo rw’ibanga rw’ibice 128. Igishushanyo ca 5 kiri musi kirerekana ingene iyo cipher y’ibarabara ishobora gukoreshwa n’**uburyo bw’igitabu c’amakode y’ubuhinga bwa none** (**uburyo bwa ECB**) kugira ngo haboneke umugambi wo gupfuka. (Imirongo y’uruzitiro iri iburyo yerekana ko ushobora gusubiramwo iyo nzira igihe cose bikenewe).


*Ishusho ya 5: Igiharuro c'ibarabara gifise uburyo bwa ECB*


![Figure 5: A block cipher with ECB mode](assets/en/009.webp "Figure 5: A block cipher with ECB mode")


Uburyo bwo gupfuka igitabu c’amakode y’ubuhinga bwa none hakoreshejwe ubuhinga bwa block cipher ni ubu. Raba nimba ushobora gucapura ubutumwa bwawe bw’inyandiko rusangi mu bice vy’ibice 128. Niba atarivyo, wongereko **padding** ku butumwa, kugira ngo igisubizo gishobore kugabanywa neza n'ubunini bw'ibice 128. Aya ni amakuru yawe akoreshwa mu nzira yo gushiramwo amakuru.


Ubu rero, ugabanye amakuru mu bice vy’imirongo y’ibice 128 ($M_1$, $M_2$, $M_3$, n’ibindi). Gukoresha urudodo rwose rw'ibice 128 biciye mu nzira y'ububiko n'urufunguzo rwawe rw'ibice 128 kugira ngo ukore ibice vy'ibice 128 vy'inyandiko y'ububiko ($C_1$, $C_2$, $C_3$, n'ibindi). Ivyo bice, iyo bisubiye guhurizwa hamwe, bica bigira igisomwa cuzuye c’ibanga.


Gukuraho ni uburyo bwo guhindura, naho uwuronka ubutumwa akeneye uburyo buzwi bwo gukuraho ubutumwa bwose buva mu makuru yasobanuwe kugira ngo asohore ubutumwa bw’inyandiko y’umwimerere.


Naho bigoranye, igitabu c’amakode y’ubuhinga bwa none nta mutekano gifise. Ivyo ni kubera ko bishikana ku **gushiramwo amakuru y’ibintu**. Imirongo ibiri yose isa n’iyo y’amakuru y’ibice 128 irashirwa mu buryo bumwe nyene. Ayo makuru arashobora gukoreshwa nabi.


Ahubwo, umugambi wose wo gupfuka wubakiwe mu gipfukisho c'amabuye ukwiye kuba **ushobora kubaho**: ni ukuvuga, gupfuka ubutumwa bwose $M$, canke igice ico ari co cose c'i $M$, muri rusangi bikwiye gutanga ingaruka zitandukanye igihe cose. [5]


**Uburyo bwo gukorana n'uruzitiro rw'amabuye** (**uburyo bwa CBC**) ni bwo buryo busanzwe bukoreshwa cane n'uruzitiro rw'amabuye. Ivyo bihuriweko, iyo bikozwe neza, bivamwo umugambi wo gupfuka amakuru y’ibishoboka. Ushobora kubona ishusho y'ubwo buryo bwo gukora mu *Ishusho ya 6* iri musi.


*Ishusho ya 6: Igishushanyo c'ububiko gifise uburyo bwa CBC*


![Figure 6: A block cipher with CBC mode](assets/en/010.webp "Figure 6: A block cipher with CBC mode")


Twibaze ko ubunini bw’ibarabara ari 128 bits. Rero kugira ngo utangure, wosubira gukenera kwizigira ko ubutumwa bwawe bw’intango bwo mu nyandiko zisanzwe buronka ivyiza bikenewe.


Hanyuma, ukora XOR igice ca mbere c'ibice 128 c'inyandiko yawe isanzwe n'**umurongo w'intango** w'ibice 128. Ico gisubizo gishirwa mu gipfukisho c'ibarabara kugira ngo haboneke inyandiko y'ibarabara y'ibarabara rya mbere. Ku gice ca kabiri c'ibice 128, ubanza XOR umwandiko usanzwe n'inyandiko y'ibanga ivuye mu gice ca mbere, imbere y'uko uyishira mu gice c'ibanga. Ubandanya iyo nzira gushika umaze gushiramwo ubutumwa bwawe bwose bw’inyandiko rusangi.


Iyo uhejeje, wohereza ubutumwa bushizwemwo amakuru hamwe n’umurongo w’intango utashizwemwo amakuru ku wubwakira. Uwuronka amakuru arakeneye kumenya umurongo w’intango, ahandi ho ntashobora gusobanura amajambo y’ibanga.


Iyi nyubakwa iratekanye cane kuruta uburyo bwo gukoresha igitabu c’amakode y’ubuhinga bwa none iyo ikoreshejwe neza. Ushobora, ubwa mbere, kumenya neza ko umurongo w'intango ari urudodo rw'imburakimazi canke rw'imburakimazi. Ikindi, ushobora gukoresha umurongo w'intango utandukanye igihe cose ukoresheje iyi nzira yo gupfuka.


Mu yandi majambo, umurongo wawe w'intango ugomba kuba Nonce, aho **Nonce** ihagarariye "umubare ukoreshwa rimwe gusa." Niwagumya iyo ngeso, rero uburyo bwa CBC bufise igiharuro c'amabara buratuma amabara abiri yose asa n'ayanditswe rusangi azoshirwa mu buryo butandukanye igihe cose.


Ubwa nyuma, reka twibande kuri **uburyo bwo gutanga inyishu** (**uburyo bwa OFB**). Ushobora kubona ishusho y'ubu buryo mu *Ishusho 7*.


*Ishusho ya 7: Igishushanyo c'ibarabara gifise uburyo bwa OFB*


![Figure 7: A block cipher with OFB mode](assets/en/011.webp "Figure 7: A block cipher with OFB mode")


Na OFB mode uhitamwo kandi umurongo w'intango. Ariko hano, ku gice ca mbere, umurongo w'intango winjira mu gice c'ibanga n'urufunguzo rwawe. Ivyo biva muri 128-bits rero, bifatwa nk’urufunguzo. Uyu murongo w'urufunguzo ni XORed n'inyandiko rusangi kugira ngo uvemwo inyandiko y'ibanga y'ibarabara. Ku bice bikurikira, ukoresha urufunguzo ruva ku gice c'imbere nk'inyungu mu gice c'inyuma maze ugasubiramwo intambwe.


Niwaraba neza, ico mu vy’ukuri caremwe hano kivuye ku cipher y’amabuye n’uburyo bwa OFB ni cipher y’umugezi. Wewe generate ibice vy'urufunguzo vy'ibice 128 gushika ufise uburebure bw'inyandiko y'urufunguzo (uguta ibice udakeneye bivuye ku gice ca nyuma c'urufunguzo rw'ibice 128). Wewe rero, XOR umurongo w'urufunguzo n'ubutumwa bwawe bw'inyandiko rusangi kugira ngo ubone inyandiko y'ibanga.


Mu gice ca mbere ku bijanye n’amaciphers y’uruzi, naravuze ko utanga urufunguzo rw’urufunguzo ufashijwe n’urufunguzo rw’ibanga. Kugira ngo tuvuge ukuri, ntibitegerezwa gusa kuremwa n’urufunguzo rw’ibanga. Nk'uko ushobora kubibona mu buryo bwa OFB, urufunguzo rusohoka rufashijwe n'urufunguzo rw'ibanga hamwe n'urufunguzo rw'intango.


Zirikana ko nk’uko biri ku buryo bwa CBC, birahambaye guhitamwo pseudorandom canke random Nonce ku bijanye n’umurongo w’intango igihe cose ukoresheje ububiko bw’ibarabara mu buryo bwa OFB. Ahandi ho, iyo nzira nyene y’ubutumwa bw’ibice 128 yoherejwe mu nzira zitandukanye zo guhanahana amakuru izoshirwa mu buryo bumwe. Ubu ni uburyo bumwe bwo gukora ububiko bw'ibishoboka n'ububiko bw'umugezi.


Hariho ama ciphers y'uruzi akoresha gusa urufunguzo rw'ibanga kugira ngo akore urufunguzo rw'uruzi. Ku bijanye n’izo nzira, birahambaye ko ukoresha Nonce kugira uhitemwo urufunguzo rw’ibanga ku nkuru yose y’uguhanahana amakuru. Ahandi ho, ivyavuye mu gushiramwo amakuru n’izo nzira z’amazi na vyo nyene bizoba ari ivy’uguhitamwo, bikajana ku bibazo vy’umutekano.


Igiharuro c'amabuye gikundwa cane muri iki gihe ni **igiharuro ca Rijndael**. Ni co cari igitabu catsinze mu bitabo cumi na bitanu vyashikirijwe mu mahiganwa yatunganijwe n’Ikigo c’Igihugu c’Ivy’Imirongo Ngenderwako n’Ikoranabuhanga (NIST) hagati y’umwaka wa 1997 n’uwa 2000 kugira ngo gisubirire ingingo ngenderwako y’ugushiramwo amakuru ya kera, ari yo **ingingo ngenderwako y’ugushiramwo amakuru** (**DES**).


Igiharuro ca Rijndael gishobora gukoreshwa n’ibisobanuro bitandukanye ku burebure bw’urufunguzo n’ubunini bw’ibice, be no mu buryo butandukanye bwo gukora. Komite y’amarushanwa ya NIST yemeye uburyo buke bw’ururimi rwa Rijndael—ni ukuvuga ururimi rusaba ubunini bw’ibice 128 n’uburebure bw’urufunguzo bushobora kuba 128, 192 canke 256—nk’igice c’**itegeko ry’ugushiramwo amakuru** (**AES**). Ivyo ni vyo vy'ukuri bishingiyeko ingingo ngenderwako y'ibikorwa vy'ugushiramwo amakuru bihuye. Ni umutekano mwinshi ku buryo mbere na NSA bisa n’uko yiteguye kuyikoresha n’imfunguruzo z’ibice 256 ku nyandiko z’ibanga rikomeye. [6]


Igikoresho ca AES block cipher kizosigurwa mu buryo burambuye mu *Gice ca 5*.



**Ivyiyumviro:**


[5] Akamaro k'ugushiramwo amakuru y'ibishoboka kabanza gushimikwako na Shafi Goldwasser na Silvio Micali, “Ugushiramwo amakuru y'ibishoboka,” _Ikinyamakuru c'ubuhinga bwa mudasobwa n'ubuhinga bwa sisitemu_, 28 (1984), 270–99.


[6] Raba NSA, "Igitabu c'ubudandaji c'umutekano w'igihugu", [porogarama/imigambi ya iad/cnsafmsu-).




## Gukuraho urujijo

<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>


Ivyo bitera urujijo ku bijanye n’itandukaniro hagati y’ibiharuro vy’amabuye n’ibiharuro vy’uruzi bivyuka kubera ko rimwe na rimwe abantu bazotahura ijambo igiharuro c’amabuye nk’aho ryerekeza canecane kuri *ibiharuro vy’amabuye bifise uburyo bwo gupfuka*.


Rimbura uburyo bwa ECB na CBC mu gice ca mbere. Ivyo bisaba cane cane ko amakuru yo gupfuka ashobora kugabanywa n'ubunini bw'ibarabara (bisobanura ko ushobora gukoresha padding ku butumwa bw'intango). Ikindi, amakuru ari muri izo nzira na yo nyene akoreshwa n’ibarabara ry’ibarabara ataco rihinduye (kandi ntafatanywa gusa n’igisubizo c’igikorwa c’ibarabara nk’uko biri mu buryo bwa OFB).


Ni co gituma, mu buryo bundi, ushobora gusobanura **block cipher** nk'umugambi uwo ari wo wose wo gupfuka, ukora ku ma block y'uburebure butahinduka bw'ubutumwa ku gihe (aho block iyo ari yo yose itegerezwa kuba irenze byte, ahandi ho isenyuka ikaba cipher y'umugezi). Amakuru yose yo gupfuka n'inyandiko yo gupfuka bitegerezwa gucapura bimwe muri ubu bunini bw'ibarabara. Mu bisanzwe, ubunini bw’ibarabara ni 64, 128, 192 canke 256 mu burebure. Mu buryo butandukanye n’ubwo, uruzi cipher rushobora gupfuka ubutumwa bwose mu bice vy’agace kamwe canke byte ku gihe.


Hamwe n'uku gutahura gutomoye kw'ibanga ry'amabara, urashobora vy'ukuri kuvuga ko imigambi y'ubuhinga bwa none yo gupfuka ari amabara y'uruzi canke amabara. Kuva ng’aha gushika hanze, nzovuga ijambo block cipher mu buryo rusangi kiretse iyo bigaragajwe ukundi.


Ikiganiro ku buryo bwa OFB mu gice ca mbere na co nyene kiravyura ikindi ciyumviro gishimishije. Hariho ama ciphers y’uruzi yubatswe n’ama ciphers y’amabuye, nka Rijndael afise OFB. Bimwe nka Salsa20 na ChaCha ntivyaremwe bivuye mu ma ciphers y’ama block. Ushobora kwita ivyo vya nyuma **ibiharuro vy'uruzi rwa kera**. (Mu vy’ukuri nta jambo ry’urugero ryerekeza kuri mwene izo nkuru z’uruzi.)


Iyo abantu bavuga ivyiza n’ibibi vy’ibiharuro vy’uruzi n’ibiharuro vy’amabuye, mu bisanzwe baba bariko bagereranya ibiharuro vy’uruzi vya kera n’imigambi yo gupfuka ishingiye ku biharuro vy’amabuye.


Naho ushobora kwama wubaka mu buryo bworoshe uruzi cipher ukoresheje cipher y'amabuye, biragoye cane kwubaka ubwoko bumwe bw'inyubako n'uburyo bw'amabuye y'ugushiramwo amakuru (nk'uburyo bwa CBC) ukoresheje uruzi rw'umugezi rwa kera.


Muri iki kiganiro, ubu rero mukwiye gutahura *Igishushanyo ca 8*. Itanga icegeranyo ku migambi y’ugushiramwo amakuru y’uburinganire. Turakoresha ubwoko butatu bw’imigambi yo gushiramwo amakuru: amakuru y’uruzi rwa kera, amakuru y’uruzi rw’amabuye, n’amajambo y’uruzi mu buryo bw’amabuye (na yo yitwa “amajambo y’uruzi” mu kigereranyo).


*Igishushanyo ca 8: Incamake y'imigambi y'ugushiramwo amakuru y'uburinganire*


![Figure 8: Overview of symmetric encryption schemes](assets/en/012.webp "Figure 8: Overview of symmetric encryption schemes")



## Ubutumwa bwo kwemeza kode

<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>


Gushiramwo amakuru y’ibanga bifitaniye isano n’ibanga. Ariko kandi, ubuhinga bwo gupfuka amakuru bujanye n’insanganyamatsiko zagutse, nk’ubutungane bw’ubutumwa, ukuri n’ukutavyihakana. Ivyo vyitwa **amakode y’ukwemeza ubutumwa** (MACs) ni imigambi y’ubuhinga bwo gukingira amakuru y’urufunguzo rwo gushigikira ukuri n’ubunyankamugayo mu guhanahana amakuru.


Ni kuki ikintu cose, kiretse ibanga gikenewe mu kuvugana? Twibaze ko Bob yohereza ubutumwa kuri Alice ikoresheje ubuhinga bwo gukingira amakuru butashobora gusenyuka. Umuntu wese azotera ubu butumwa ntazoshobora kumenya neza ibirimwo. Ariko rero, uwo mutera aracari n’imiburiburi n’ibindi bikoresho bibiri vyo kumutera:


1. Yarashobora gufata amajambo y'ibanga, agahindura ibirimwo, maze akarungika ayo majambo yahinduwe kuri Alice.

2. Yashobora guhagarika ubutumwa bwa Bob bwose maze akarungika ubutumwa bwiwe bwite.


Muri ivyo bihe vyose bibiri, uwutera yoshobora kutagira ubumenyi na bumwe ku bijanye n’ibirimwo bivuye mu nyandiko z’ibanga (1) na (2). Ariko yari agishobora kwonona cane muri ubwo buryo. Aho ni ho amakode y’ukwemeza ubutumwa aba ahambaye.


Amakode y’ukwemeza ubutumwa asobanurwa mu buryo busanzwe nk’imigambi y’ubuhinga bwo gukingira amakuru ifise ubuhinga butatu: ubuhinga bwo guhingura urufunguzo, ubuhinga bwo guhingura ibimenyetso, n’uburyo bwo kugenzura. MAC itekanye ituma ama tags **existentially unforgeable** ku muntu wese atera—ni ukuvuga ko adashobora gukora neza tag ku butumwa bugenzura, kiretse afise urufunguzo rw’ibanga.


Bob na Alice zishobora kurwanya ugukoresha nabi ubutumwa bumwe bumwe hakoreshejwe MAC. Twibaze ko muri ako kanya batavyitaho ku bijanye n’ibanga. Bashaka gusa kumenya neza ko ubutumwa Alice yaronse bwavuye kuri Bob vy’ukuri kandi ko butahindutse mu buryo na bumwe.


Ivyo bigenda vyerekanywe ku *Ishusho ya 9*. Kugira ngo bakoreshe **MAC** (Kode y’Ivyemezo vy’Ubutumwa), bobanza generate urufunguzo rw’ibanga $K$ rusangiwe hagati yabo bompi. Bob irema ikimenyetso $T$ c'ubutumwa ikoresheje urufunguzo rw'ibanga $K$. Araheza arungika ubutumwa hamwe n'ikimenyetso c'ubutumwa kuri Alice. Ashobora rero kugenzura ko Bob vy’ukuri yakoze iyo tag, mu gukoresha urufunguzo rw’ibanga, ubutumwa, n’iyo tag biciye ku nzira yo kugenzura.


*Igishushanyo ca 9: Incamake y'imigambi y'ugushiramwo amakuru y'uburinganire*


![Figure 9: Overview of symmetric encryption schemes](assets/en/013.webp "Figure 9: Overview of symmetric encryption schemes")


Kubera **ukudashobora guhindurwa**, uwutera ntashobora guhindura ubutumwa $M$ mu buryo ubwo ari bwo bwose canke ngo areme ubutumwa bwiwe bwite bufise ikimenyetso gibereye. Ivyo ni ko biri, naho uwutera yoba yihweje ama tags y’ubutumwa bwinshi buri hagati ya Bob na Alice bukoresha urufunguzo rumwe rw’ibanga. Ivyinshi, uwutera yoshobora kubuza Alice kwakira ubutumwa $M$ (ikibazo cryptography idashobora Address).


MAC iremeza ko ubutumwa bwaremwe na Bob. Ubwo bunyakuri, buca busobanura ubutungane bw’ubutumwa—ni ukuvuga, nimba Bob yaremye ubutumwa bumwe bumwe, rero, ipso facto, ntibwahinduwe mu buryo na bumwe n’umuterabwoba. Rero kuva ng’aha gushika hanze, ivyiyumviro vyose vy’ukwemeza umuntu bikwiye gutahurwa ubwo nyene ko bisobanura ivyiyumviro vy’ubunyankamugayo.


Naho nashizeho itandukaniro hagati y’ukuri kw’ubutumwa n’ubunyankamugayo mu kiganiro canje, birasanzwe kandi gukoresha ayo majambo nk’amajambo amwe. Ivyo rero vyerekeye iciyumviro c’ubutumwa bwompi bwaremwe n’umuntu kanaka kandi butahinduwe mu buryo na bumwe. Muri iyo mpwemu, amakode y’ukwemeza ubutumwa akenshi yitwa kandi **amakode y’ubutungane bw’ubutumwa**.



## Ububiko bwemejwe

<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>


Mu bisanzwe, woshima kwemeza ibanga n’ukuri mu guhanahana amakuru kandi, rero, imigambi yo gushiramwo amakuru n’imigambi ya MAC ikoreshwa hamwe.


**Igishushanyo co gushiramwo amakuru yemejwe** ni igishushanyo gifatanya amakuru na MAC mu buryo butekanye cane. Mu buryo bwihariye, ritegerezwa guhura n'ingingo mfatirwako z'ukudashobora guhindurwa kw'ubuzima hamwe n'iciyumviro gikomeye cane c'ibanga, ni ukuvuga ikintu gishobora guhangana n'ibitero vy'amajambo yatoranijwe. [7]


Kugira ngo umugambi wo gupfuka ushobore guhangana n’ibitero vy’inyandiko zitoranijwe, utegerezwa guhura n’ingingo mfatirwako z’**ukudashobora guhinduka**: ni ukuvuga ko uguhindura kwose kw’inyandiko y’ibanga n’umuterabwoba gukwiye gutanga inyandiko y’ibanga idafise akamaro canke ishobora gukuraho inyandiko y’ibanga idafitaniye isano n’inyandiko y’umwimerere. [8]


Nk’uko umugambi wo gupfuka amakuru wemewe utuma inyandiko y’ibanga yaremwe n’umuterabwoba yama ari ubusa (nk’uko iyo tag itazosuzumwa), irahuye n’ingingo mfatirwako zo kurwanya ibitero vy’inyandiko y’ibanga yatowe. Ikintu gitangaje, ushobora kwemeza ko umugambi wo gushiramwo amakuru yemewe ushobora kwama uremwa uhereye ku guhuza MAC idashobora guhindurwa n’umugambi wo gushiramwo amakuru uhuye n’iciyumviro kidakomeye cane c’umutekano, kizwi nka **umutekano w’igitero c’inyandiko-gitomoye**.


Ntituzokwinjira mu bintu vyose bijanye no kwubaka imigambi y’ugushiramwo amakuru yemewe. Ariko birahambaye kumenya ibintu bibiri vyerekeye ukuntu vyubatswe.


Ubwa mbere, umugambi wo gushiramwo amakuru yemejwe ubanza gukorana n’ugushiramwo amakuru hanyuma ugakora ikimenyetso c’ubutumwa ku nyandiko y’ibanga. Bica bigaragara ko ubundi buryo—nk’ugufatanya inyandiko y’ibanga n’ikimenyetso kiri ku nyandiko isanzwe, canke kubanza gukora ikimenyetso hanyuma ugashiramwo ikimenyetso c’ibanga n’ico kimenyetso—bidatekanye. Ikindi, izo nzira zompi zifise urufunguzo rwazo rw’ibanga rwatoranijwe mu buryo bw’impfagusa, ahandi ho umutekano wawe urashobora guhungabana cane.


Iryo hame ryavuzwe haruguru rirakora muri rusangi: *ukwiye kwama ukoresha imfunguruzo zitandukanye igihe uhuza imigambi y’ishimikiro y’ubuhinga bwo gukingira amakuru*.


Igishushanyo co gushiramwo amakuru yemejwe kirerekanwa ku *Ishusho ya 10*. Bob ibanza gukora igisomwa c'ibanga $C$ kivuye mu butumwa $M$ ikoresheje urufunguzo rwatowe mu buryo bw'impfagusa $K_C$. Araheza arema ubutumwa $T$ mu gukoresha ciphertext n'urufunguzo rutandukanye rwatowe mu buryo bw'impfagusa $K_T$ biciye mu nzira yo guhingura ubutumwa. Ivyo bimenyetso vyompi n'ubutumwa bwoherezwa kuri Alice.


Alice ubu ibanza gusuzuma nimba ikimenyetso gifise akamaro gihawe inyandiko y'ibanga $C$ n'urufunguzo $K_T$. Niba ari ukuri, arashobora gusobanura ubutumwa akoresheje urufunguzo $K_C$. Si uko gusa yizezwa ko hariho ibanga rikomeye cane mu guhanahana amakuru yabo, ariko kandi arazi ko ubutumwa bwaremwe na Bob.


*Ishusho ya 10: Umugambi wo gupfuka amakuru yemejwe*


![Figure 10: An authenticated encryption scheme](assets/en/014.webp "Figure 10: An authenticated encryption scheme")


None ama MAC aremwa gute? Naho MACs zishobora kuremwa biciye mu buryo bwinshi, uburyo busanzwe kandi bukora neza bwo kuziremwa ni biciye mu **imikorere ya Hash y’ubuhinga bwa none**.


Tuzozana ibikorwa vy'ubuhinga bwa cryptography Hash mu buryo burambuye mu *Igice ca 6*. Ubu, menya gusa ko **igikorwa ca Hash** ari igikorwa gishobora kubarwa neza gifata ivyinjijwe vy'ubunini butari bwo kandi kigatanga ibisohoka vy'uburebure butahinduka. Nk’akarorero, igikorwa gikundwa cane ca Hash **SHA-256** (ubuhinga bwa Hash butekanye 256) cama gitanga igisohoka c’ibice 256 ataco kivuze ku bunini bw’ivyo winjije. Ibikorwa bimwebimwe vya Hash, nka SHA-256, birafise ibikorwa vy’ingirakamaro mu gukora amakuru y’ibanga.


Ubwoko busanzwe bw'ikimenyetso gikozwe n'igikorwa c'ubuhinga bwa Hash ni **kode y'ukwemeza ubutumwa bushingiye kuri Hash** (HMAC). Ivyo bigenda vyerekanywe ku *Ishusho ya 11*. Ishirahamwe ritanga imfunguruzo zibiri zitandukanye zivuye ku rufunguzo rw'ibanga $K$, urufunguzo rw'imbere $K_1$ n'urufunguzo rw'inyuma $K_2$. Inyandiko rusangi $M$ canke inyandiko y'ibanga $C$ rero irashirwa hamwe n'urufunguzo rw'imbere. Igisubizo $T'$ gica gifatanywa n'urufunguzo rw'inyuma kugira ngo kivemwo ubutumwa $T$.


Hariho paleti y’ibikorwa vya Hash bishobora gukoreshwa mu guhingura HMAC. Ikoreshwa cane rya Hash ni SHA-256.



*Ishusho ya 11: HMAC*


![Figure 11: HMAC](assets/en/015.webp "Figure 11: HMAC")


**Ivyiyumviro:**


[7] Ivyiza vyihariye vyavuzwe muri iki gice ni ivyo Katz na Lindell, urupapuro rwa 131–47.


[8] Mu buryo bw’ubuhinga, insobanuro y’ibitero vy’inyandiko z’ibanga zitoranijwe itandukanye n’iciyumviro c’ukudashobora guhinduka. Ariko urashobora kwerekana ko ivyo vyiyumviro bibiri vy’umutekano bingana.




## Igihe co guhanahana amakuru gitekanye

<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>


Twibaze ko abantu babiri bari mu kiganiro co kuvugana, rero bagarungika ubutumwa bwinshi basubira inyuma.


Igishushanyo c’ugushiramwo amakuru yemejwe kiratuma uwuronka ubutumwa ashobora kugenzura ko bwaremwe n’uwo bari kumwe mu gihe c’uguhanahana amakuru (igihe cose urufunguzo rw’ibanga rutarasohoka). Ivyo birakora neza bihagije ku butumwa bumwe. Ariko rero, mu bisanzwe, abantu babiri bariko bararungika ubutumwa mu gihe c’uguseruranira akari ku mutima. Kandi muri iyo nzira, umugambi wo gukingira amakuru usanzwe nk’uko wavuzwe mu gice c’imbere urabura mu gutanga umutekano.


Imvo nyamukuru ni uko umugambi wo gushiramwo amakuru yemejwe udatanga icemezo c’uko ubutumwa mu vy’ukuri bwarungitswe n’umukozi yaburemye mu kiringo c’uguhanahana amakuru. Rimbura ibi bintu bitatu bikurikira:


1. **Replay attack**: Uwutera asubira kohereza ciphertext n’ikimenyetso yafashe hagati y’abantu babiri mu gihe ca kera.

2. **Re-ordering attack**: Uwutera afata ubutumwa bubiri mu bihe bitandukanye akaburungikira uwuburonka mu buryo buhindutse.

3. **Igitero co kwiyumvira**: Uwutera abona ubutumwa buvuye kuri A buja kuri B, kandi akaburungikira A.


Naho uwutera ata bumenyi afise ku bijanye n’inyandiko y’ibanga kandi adashobora guhingura inyandiko z’ibanga zitari zo, ivyo bitero biri hejuru birashobora kwonona cane mu bijanye n’itumanaho.


Nk’akarorero, dufate ko ubutumwa bumwebumwe buri hagati y’abo babiri bujanye n’ugutanga amahera y’amahera. Igitero co gusubiramwo coshobora gutuma ayo mahera yoherezwa ubugira kabiri. Igishushanyo co gupfuka amakuru yemejwe n’ivy’ukuri ntaco gishobora kwikingira mwene ivyo bitero.


Igishimishije, ubwo bwoko bw’ibitero burashobora kugabanywa bitagoranye mu kiganiro co guhanahana amakuru hakoreshejwe **ibimenyetso** na **ibimenyetso vy’igihe gihuye**.


Ibirango bishobora kwongerwa ku butumwa bw'inyandiko rusangi imbere y'uko bushirwa mu nzira. Ivyo vyobuza ibitero vyose vyo kwiyumvira. Nk’akarorero, ikimenyetso c’igihe gishobora kuba umubare w’urutonde mu gihe kinaka co guhanahana amakuru. Buri ruhande rwongerako inomero y’urutonde ku butumwa imbere y’uko bushirwa mu nzira, ku buryo uwuburonka amenya urutonde rw’ubutumwa bwarungitswe. Ivyo bica bikuraho ubushobozi bwo gusubira gutegeka ibitero. Bikuraho kandi ibitero vyo gusubiramwo. Ubutumwa bwose umutera azorungika ku murongo buzoba bufise inomero ya kera y’urutonde, kandi uwuburonka azomenya ko atazosubira gukora ubwo butumwa.


Kugira ngo tubone ingene ibihe vyo guhanahana amakuru bitekanye bikora, dufate kandi Alice na Bob. Barungika ubutumwa bune bwose hamwe baja n’inyuma. Ushobora kubona ingene umugambi wo gupfuka amakuru yemejwe ufise ibimenyetso n'imibare y'urutonde wokora aha hepfo mu *Ishusho 11*.


Igihe co guhanahana amakuru gitangura na Bob yohereza ubutumwa bw'ibanga $C_{0,B}$ kuri Alice bufise ubutumwa $T_{0,B}$. Ico canditswe c’ibanga kirimwo ubutumwa, hamwe n’ikimenyetso (Bob) be n’inomero y’urutonde (0). Igiharuro $T_{0,B}$ gikorwa ku nyandiko yose y'ibanga. Mu biganiro vyabo vyakurikiye, Alice na Bob barabungabunga iyo porotokole, bagasubiramwo amatongo uko bikenewe.



*Ishusho ya 12: Igihe co guhanahana amakuru mu mutekano*


![Figure 12: A secure communication session](assets/en/016.webp "Figure 12: A secure communication sessesion")







# RC4 na AES

<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>





## Igiharuro c'umugezi wa RC4

<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>


Muri iki Gice, tuzovuga ku ndondoro y'umugambi wo gupfuka amakuru ukoresheje uruzitiro rw'uruzi rwa kera rw'ubu, RC4 (canke "Rivest cipher 4"), n'uruzitiro rw'uruzi rwa kera rw'ubu, AES. Naho RC4 cipher yaguye mu ntambara nk’uburyo bwo gupfuka, AES ni yo nzira y’ugupfuka y’ubuhinga bwa none. Izo ngero zibiri zikwiye gutanga iciyumviro ciza c’ingene ubuhinga bwo gukingira amakuru bukora munsi y’igipfukisho.


___


Kugira ngo nshobore gutahura ingene ama ciphers y’umugezi w’ubu pseudorandom akora, nzoshimika ku ma cipher y’umugezi wa RC4. Ni pseudorandom stream cipher yakoreshejwe mu mirongo ngenderwako y’umutekano w’aho umuntu ashobora gushika ata nsinga ya WEP na WAP be no muri TLS. Nk’uko RC4 ifise intege nke nyinshi zigaragara, yaraguye mu ntambara. Nkako, Ishirahamwe ry’Ivy’Ingenzi ya Internet ubu rirabuza gukoresha amasuite ya RC4 n’ibikoresho vy’abaguzi n’ivy’abakozi mu bihe vyose vya TLS. Naho ari ukwo, birakora neza nk’akarorero ko kwerekana ingene igiharuro c’uruzi rwa kera gikora.


Kugira ngo ntangire, nzobanza kwerekana ingene woshiramwo ubutumwa busanzwe n’uruyoya rwa RC4. Twibaze ko ubutumwa bwacu bwo mu nyandiko zisanzwe ari “ISUPU.” Gushiramwo amakuru n’uruyoya rwacu RC4 cipher, rero, bigenda mu ntambwe zine.


### Intambwe ya 1


Mbere, sobanura urutonde **S** rufise $S[0] = 0$ gushika kuri $S[7] = 7$. Urutonde hano rusobanura gusa ihuriro ry'agaciro rihinduka ryatunganijwe n'urutonde, ryitwa kandi urutonde mu ndimi zimwe zimwe zo gukora porogarama (nk'akarorero, Python). Muri iki gihe, urutonde ruva kuri 0 gushika kuri 7, kandi agaciro na ko kuva kuri 0 gushika kuri 7. Rero **S** ni uku:



- $S = [0, 1, 2, 3, 4, 5, 6, 7]$


Agaciro hano si imibare ya ASCII, ariko ni agaciro k'icumi k'imirongo y'amabayiti 1. Rero agaciro ka 2 koba kangana n’amadolari 0000 \ 0011$. Uburebure bw'urutonde **S** ni, rero, 8 bytes.


### Intambwe ya 2


Ubwa kabiri, sobanura urufunguzo **K** rw'uburebure bwa bytes 8 mu guhitamwo urufunguzo ruri hagati ya bytes 1 na 8 (ata mice ya bytes yemerewe). Nk'uko byte yose ari 8 bits, ushobora guhitamwo umubare uwo ari wo wose uri hagati ya 0 na 255 kuri byte yose y'urufunguzo rwawe.


Twibaze ko duhisemwo urufunguzo rwacu **k** nka $[14, 48, 9]$, kugira ngo rube n’uburebure bwa bytes 3. Buri rutonde rw'urufunguzo rwacu, rero, rushirwaho hakurikijwe agaciro k'icumi k'ico kintu c'urufunguzo, mu buryo bubereye. Niwaca mu rufunguzo rwose, wongere utangure mu ntango, gushika wuzuje ibibanza 8 vy’urutonde rw’urufunguzo. Ni co gituma, urufunguzo rwacu rukurikira:



- $K = [14, 48, 9, 14, 48, 9, 14, 48]$


### Intambwe ya 3


Ica gatatu, tuzohindura urutonde **S** dukoresheje urutonde rw'urufunguzo **K**, mu buryo buzwi nka **ugutegura urufunguzo**. Ivyo bigenda ni ibi bikurikira muri pseudocode:



- Rema ibihinduka **j** na **i**
- Gushinga umuhinduzi $j = 0$
- Ku $i$ yose kuva kuri 0 gushika kuri 7:
    - Gushiraho $ j = (j + S [je] + K [je]) \ mod 8 $
    - Guhindura $S[i]$ na $S[j]$


Ihinduka ry'urutonde **S** rifatwa na *Imbonerahamwe 1*.


Kugira ngo utangure, ushobora kubona ikibanza c'intango ca **S** nk' $[0, 1, 2, 3, 4, 5, 6, 7]$ n'agaciro k'intango ka 0 kuri **j**. Ivyo bizohindurwa hakoreshejwe urutonde rw'urufunguzo $[14, 48, 9, 14, 48, 9, 14, 48]$.


Igiharuro ca for gitangura na $i = 0$. Dushingiye ku pseudocode yacu iri hejuru, agaciro gashasha ka **j** kaba 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Guhindura $S[0]$ na $S[6]$, ikibanza ca **S** inyuma y'urugendo 1 kiba $[6, 1, 2, 3, 4, 5, 0, 7]$.


Mu murongo ukurikira, $i = 1$. Mu guca mu nzira ya for kandi, **j** ironka agaciro ka 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Guhindura $S[1]$ na $S[7]$ kuva ku gihe ca **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, bitanga $[6, 7, 2, 3, 4, 5, 0, 1]$ inyuma y'urugendo rwa 2.


Turabandanya n’iyi nzira gushika dusohoye umurongo wa nyuma uri hasi ku bijanye n’urutonde **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.



*Imbonerahamwe 1: Imbonerahamwe y'ingenzi*


| Round   | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Initial |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Intambwe ya 4


Nk’intambwe ya kane, turatanga **umurongo w’ifunguro**. Iyi ni urudodo rw’ibinyoma rw’uburebure bungana n’ubutumwa dushaka gutanga. Ivyo bizokoreshwa mu gupfuka ubutumwa bw’intango “SOUP.” Nk’uko keystream ikeneye kuba ndende nk’ubutumwa, turakeneye imwe ifise 4 bytes.


Urufunguzo rusohoka n'iyi pseudocode ikurikira:



- Rema ibihinduka **j**, **i**, na **t**.
- Gushinga $j = 0$.
- Ku $i$ yose y’inyandiko rusangi, gutangura na $i = 1$ gushika kuri $i = 4$, byte yose y’umurongo w’urufunguzo isohoka gutya:
    - $j = (j + S[je]) \mod 8$
    - Guhindura $S[i]$ na $S[j]$.
    - $t = (S[je] + S[j]) \mod 8$
    - I^{th}$ byte y'urufunguzo = $S[t]$


Ushobora gukurikira imibare iri mu *Imbonerahamwe ya 2*.


Igihugu c’intango ca **S** ni $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Gushinga $i = 1$, agaciro ka **j** kaba 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Turaheza tugahinduranya $S[1]$ na $S[4]$ kugira ngo tubone ihinduka rya **S** mu murongo wa kabiri, $[6, 3, 1, 0, 4, 7, 5, 2]$. Agaciro ka **t** rero ni 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Ubwanyuma, byte y'urufunguzo ni $S[7]$, canke 2.


Turaheza tukabandanya gukora izindi bytes gushika turonse izo bytes zine zikurikira: 2, 6, 3, na 7. Imwe muri izo bytes ishobora gukoreshwa mu gupfuka urudome rwose rw'inyandiko rusangi, "SOUP".


Kugira ngo dutangure, dukoresheje imbonerahamwe ya ASCII, turashobora kubona ko “SOUP” ikodeshejwe n’agaciro k’icumi k’imirongo y’amabyte iri munsi ari “83 79 85 80”. Gufatanya n’umurongo w’urufunguzo “2 6 3 7” bitanga “85 85 88 87”, biguma ari uko biri inyuma y’igikorwa ca modulo 256. Mu rurimi rwa ASCII, inyandiko y’ibanga “85 85 88 87” ingana n’ijambo “UUXW”.


Bigenda gute iyo ijambo ryo gupfuka ryari rirerire kuruta urutonde **S**? Muri ivyo, urutonde **S** ruguma ruhinduka muri ubu buryo bwerekanwa haruguru kuri byte yose **i** y'inyandiko rusangi, gushika dufise umubare w'ama byte mu ruzitiro rw'urufunguzo ungana n'umubare w'inyuguti ziri mu nyandiko rusangi.



*Imbonerahamwe ya 2: Uruvyaro rw'urufunguzo*


| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     |     |     |           |      |      |      |      |      |      |      |      |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |
| 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Akarorero twamaze kuvuga ni akarorero gusa k'amazi y'**RC4 stream cipher**. Igiharuro nyaco ca RC4 gifise **S** y’uburebure bwa bytes 256, atari bytes 8, n’urufunguzo rushobora kuba hagati ya bytes 1 na 256, atari hagati ya bytes 1 na 8. Igiharuro c'urufunguzo n'imirongo y'urufunguzo vyose bica bisohoka hakurikijwe uburebure bwa 256-byte bw'igiharuro ca **S**. Ivyo biharuro birarushiriza kuba bikomeye cane, mugabo ingingo ngenderwako ziguma ari zimwe. Ukoresheje urufunguzo rumwe, [14,48,9], n'urufunguzo rwa RC4 rusanzwe, ubutumwa bw'inyandiko rusangi "SOUP" burashirwa mu buryo bw'inyuguti 67 02 ed df mu buryo bw'inyuguti cumi n'itandatu.


Igiharuro c'uruzi aho urufunguzo rw'urufunguzo ruhindurwa rudashingiye ku butumwa bw'inyandiko rusangi canke inyandiko y'uruzitiro ni **igiharuro c'uruzi gihuye**. Urufunguzo ruva gusa ku rufunguzo. Biragaragara ko RC4 ari akarorero k’uruzitiro rw’uruzitiro rujanye n’igihe, kuko uruzitiro rw’urufunguzo nta sano rufise n’inyandiko rusangi canke inyandiko y’uruzitiro. Ivyiyumviro vyacu vyose vy’uruzi rwa kera twavuze mu kigabane c’imbere, harimwo n’ivy’uguhindura, ivy’i Vigenère, n’ivy’igihe kimwe, na vyo nyene vyari vy’ubwoko bw’ivy’ugukorana.


Mu buryo butandukanye n’ubwo, **uruzitiro rw’uruzitiro rudahuye** rufise uruzitiro rw’urufunguzo ruterwa n’urufunguzo n’urufunguzo rwa Elements rw’imbere rw’inyandiko y’uruzitiro. Ubwo bwoko bw’ibanga bwitwa kandi **ibanga ryikorana**.


Igihambaye ni uko umurongo w’urufunguzo ukoreshwa na RC4 ukwiye gufatwa nk’urufunguzo rw’igihe kimwe, kandi ntushobora gukora umurongo w’urufunguzo mu buryo bumwe nyene mu gihe gikurikira. Aho guhindura urufunguzo igihe cose, umuti ngirakamaro ni ugufatanya urufunguzo na **Nonce** kugira ngo haboneke bytestream.




## AES ifise urufunguzo rw'ibice 128

<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>


Nk’uko twabibonye mu kigabane ca mbere, ikigo c’igihugu c’ubuhinga n’ubuhinga (NIST) caragize ihiganwa hagati y’umwaka wa 1997 n’uwa 2000 kugira ngo kimenye ingingo nshasha yo gushiramwo amakuru mu buryo buhuye. Igiharuro ca **Rijndael** ni co cahindutse igiharuro catsinze. Izina ni urukino rw’amajambo ku mazina y’abaremyi b’Ababirigi, Vincent Rijmen na Joan Daemen.


Igiharuro ca Rijndael ni **igiharuro c'amabuye**, bisobanura ko hariho ubuhinga nyamukuru, bushobora gukoreshwa n'ibisobanuro bitandukanye ku burebure bw'urufunguzo n'ubunini bw'amabuye. Ushobora rero kuyikoresha n’uburyo butandukanye bwo gukora kugira ngo wubake imigambi yo gupfuka.


Komite y’amarushanwa ya NIST yemeje uburyo buke bw’inyandiko ya Rijndael—ni ukuvuga iyo isaba ubunini bw’ibice 128 n’uburebure bw’urufunguzo bushobora kuba ibice 128, ibice 192 canke ibice 256—nk’igice c’Itegeko ry’Igihugu ry’Igihugu ry’Igihugu **Advanced Encryption Standard** (A) Iyi verisiyo y’ibanga ry’i Rijndael irashobora kandi gukoreshwa mu buryo bwinshi bwo gukora. Ivyerekeye iyo ngingo ni ivyo bita **Ikigereranyo c'Igikoresho co Gushiramwo Amabanga (AES)**.


Kugira ngo nerekane ingene cipher ya Rijndael ikora, umushinge wa AES, nzokwerekana ingene umuntu ashobora gushiramwo urufunguzo rw’ibice 128. Ingano y’urufunguzo iragira ingaruka ku mubare w’ibice bifatwa ku gice cose c’ububiko. Ku mfunguruzo z’ibice 128, bisaba ko umuntu akora ibice 10. Iyo hariho ibice 192 n’ibice 256, vyobaye ari ibice 12 n’ibice 14, uko bikurikirana.


Ikindi, nzokwiyumvira ko AES ikoreshwa mu **ECB-mode**. Ivyo bituma gusobanura vyoroha gatoyi kandi ntaco bimaze ku bijanye n’ubuhinga bwa Rijndael. Kugira ngo tubone neza, uburyo bwa ECB ntibutekanye mu bikorwa kuko bujana mu gupfuka amakuru y’ibintu. Uburyo bwo gukingira bukoreshwa cane na AES ni **CBC** (Ugufatanya amabuye y’agaciro).


Reka twite urufunguzo $K_0$. Ubwubatsi bufise ivyo bipimo biri hejuru, rero, busa n’uko buri mu *Ishusho 1*, aho $M_i$ ihagarariye igice c’ubutumwa bw’inyandiko rusangi bw’ibice 128 na $C_i$ igice c’inyandiko y’ibanga y’ibice 128. Padding yongerwa ku nyandiko rusangi y'ibarabara rya nyuma, iyo inyandiko rusangi idashobora kugabanywa ku rugero rumwe n'ubunini bw'ibarabara.



*Ishusho ya 1: AES-ECB ifise urufunguzo rw'ibice 128*


![Figure 1: AES-ECB with a 128-bit key](assets/en/017.webp "Figure 1: AES-ECB with a 128-bit key")


Igipande cose c’inyandiko c’ibice 128 gica mu bice cumi mu mugambi wo gupfuka amakuru wa Rijndael. Ivyo bisaba urufunguzo rw'uruziga rwitandukanye ku ruzitiro rwose ($K_1$ gushika kuri $K_{10}$). Ivyo bikoreshwa ku nzira yose bivuye ku rufunguzo rw'intango rw'ibice 128 $K_0$ hakoreshejwe **urufunguzo rwo kwagura algorithm**. Ni co gituma, ku gice cose c’inyandiko kizoshirwa mu nzira, tuzokoresha urufunguzo rw’intango $K_0$ hamwe n’urufunguzo cumi rutandukanye rw’uruziga. Zirikana ko izo mfunguruzo nyene 11 zikoreshwa ku gice cose c’inyandiko y’ibice 128 gisaba gushirwamwo amakuru.


Urufunguzo rwo kwagura ni rurerure kandi ruragoye. Gukora biciye muri ryo nta nyungu nyinshi zifise mu vy’inyigisho. Ushobora kuraba mu nzira yo kwagura urufunguzo wewe nyene, niwabishaka. Igihe imfunguruzo zikikuje zimaze gusohoka, igiharuro ca Rijndael kizokoresha igice ca mbere c'inyandiko y'ibice 128, $M_1$, nk'uko bigaragara ku *Ishusho 2*. Ubu rero tuzoca muri izo ntambwe.


*Ishusho ya 2: Gukoresha $M_1$ n'ibara rya Rijndael:*


**Urugendo rwa 0:**


- XOR $M_1$ na $K_0$ kugira ngo uvemwo $S_0$


---

**Zikuza n kuri n = {1,...,9}:**


- XOR $S_{n-1}$ na $K_n$
- Gusubirira byte
- Guhindura imirongo
- Vanga inkingi
- XOR $S$ na $K_n$ kugira ngo bivemwo $S_n$


---

**Igice ca 10:**


- XOR $S_9$ na $K_{10}$
- Gusubirira byte
- Guhindura imirongo
- XOR $S$ na $K_{10}$ kugira ngo uvemwo $S_{10}$
- $S_{10}$ = $C_1$



### Uruzingu rwa 0


Igizunguruko 0 c’igiharuro ca Rijndael kiragororotse. Igishushanyo $S_0$ gikorwa n'igikorwa ca XOR hagati y'inyandiko y'ibice 128 n'urufunguzo rw'ibanga. Ni ukuvuga,



- $S_0 = M_1 \ukwongerako K_0$


### Urugendo rwa 1


Mu nzira ya 1, urutonde $S_0$ rubanza gufatanywa n'urufunguzo rw'inzira $K_1$ hakoreshejwe igikorwa ca XOR. Ivyo bituma habaho igihugu gishasha c’amadolari S$.


Ubwa kabiri, igikorwa co **gusubirira byte** gikorwa ku gihe c'ubu ca $S$. Ikora mu gufata byte yose y’urutonde rw’amabayiti 16 $S$ hanyuma ikayisubiriza byte ivuye mu rutonde rwitwa **Rijndael’s S-box**. Byte yose irafise ihinduka ryihariye, kandi igihugu gishasha ca $S$ kirasohoka nk'inyishu. S-box ya Rijndael yerekanwa ku *Ishusho ya 3*.


*Ishusho ya 3: Igikapu ca Rijndael*


|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
| 50  | 53  | D1  | 00  | ED  | 20  | FC  | B1  | 5B  | 6A  | CB  | BE  | 39  | 4A  | 4C  | 58  | CF  |
| 60  | D0  | EF  | AA  | FB  | 43  | 4D  | 33  | 85  | 45  | F9  | 02  | 7F  | 50  | 3C  | 9F  | A8  |
| 70  | 51  | A3  | 40  | 8F  | 92  | 9D  | 38  | F5  | BC  | B6  | DA  | 21  | 10  | FF  | F3  | D2  |
| 80  | CD  | 0C  | 13  | EC  | 5F  | 97  | 44  | 17  | C4  | A7  | 7E  | 3D  | 64  | 5D  | 19  | 73  |
| 90  | 60  | 81  | 4F  | DC  | 22  | 2A  | 90  | 88  | 46  | EE  | B8  | 14  | DE  | 5E  | 0B  | DB  |
| A0  | E0  | 32  | 3A  | 0A  | 49  | 06  | 24  | 5C  | C2  | D3  | AC  | 62  | 91  | 95  | E4  | 79  |
| B0  | E7  | C8  | 37  | 6D  | 8D  | D5  | 4E  | A9  | 6C  | 56  | F4  | EA  | 65  | 7A  | AE  | 08  |
| C0  | BA  | 78  | 25  | 2E  | 1C  | A6  | B4  | C6  | E8  | DD  | 74  | 1F  | 4B  | BD  | 8B  | 8A  |
| D0  | 70  | 3E  | B5  | 66  | 48  | 03  | F6  | 0E  | 61  | 35  | 57  | B9  | 86  | C1  | 1D  | 9E  |
| E0  | E1  | F8  | 98  | 11  | 69  | D9  | 8E  | 94  | 9B  | 1E  | 87  | E9  | CE  | 55  | 28  | DF  |
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |


Iyi S-Box ni ahantu hamwe aho aligebra itaboneka iza mu rukino mu gitabu ca Rijndael, cane cane **Imirima ya Galois**.


Kugira ngo utangure, usobanura ikintu cose gishoboka ca byte 00 gushika kuri FF nk'umurongo w'ibice 8. Buri rwego nk’urwo ni ikintu c’**umurima wa Galois GF(2^8)** aho umubare w’ibiharuro vyinshi udashobora kugabanywa w’igikorwa c’ibiharuro vyinshi ari $x^8 + x^4 + x^3 + x + 1$. Itongo rya Galois rifise ivyo bimenyetso ryitwa kandi **Itongo ry’Iherezo rya Rijndael**.


Igikurikira, ku kintu cose gishoboka kiri mu murima, dukora ico bita **Nyberg S-Box**. Muri aka gasandugu, byte yose igaragazwa ku **inverse yayo y'ugukubita** (i.e., kugira ngo igicuruzwa cabo kingana na 1). Turaheza tugaca dukora ikarita y’izo nkuru kuva ku gasandugu ka S ka Nyberg gushika ku gasandugu ka S ka Rijndael dukoresheje **uguhindura kwa affine**.


Igikorwa kigatatu ku **S** ni igikorwa ca **shift rows**. Ifata igihugu ca **S** maze igatanga urutonde rw'ama bytes cumi n'atandatu yose ari mu matrix. Ukwuzuza kw’ibarabara gutangura hejuru ibubamfu maze gukora inzira yavyo mu kuva hejuru gushika hasi hanyuma, igihe cose inkingi yuzuye, ugahindura inkingi imwe iburyo ukaja hejuru.


Igihe matrix ya **S** imaze kwubakwa, imirongo ine irahindurwa. Umurongo wa mbere uguma ari uko nyene. Umurongo wa kabiri ujana umwe ibubamfu. Uwugira gatatu agenda abiri aja ibubamfu. Uwugira kane agenda atatu aja ibubamfu. Akarorero k’ingene ivyo bigenda karaboneka mu *Igishushanyo ca 4*. Igihugu c'intango ca **S** kigaragazwa hejuru, n'igisubizo inyuma y'igikorwa c'imirongo y'uguhindura kigaragazwa munsi yaco.


*Ishusho ya 4: Guhindura imirongo*


| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |
| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


Mu ntambwe ya kane, **imirima ya Galois** irasubira kugaragara. Kugira ngo dutangure, inkingi yose y’umurongo wa **S** igwizwa n’inkingi y’umurongo wa 4 x 4 ubona ku *Ishusho ya 5*. Ariko aho kuba ugukubita kw’amabara asanzwe, ni ugukubita kw’amabara **modulo umubare w’amabara udashobora kugabanywa**, $x^8 + x^4 + x^3 + x + 1$. Ivyo bivako bigereranya ibice vy'umubiri vy'umubiri.


*Ishusho ya 5: Inkingi zivanzwe*


| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   |
| 03   | 01   | 01   | 02   |

Gukubitisha inkingi ya mbere y'umurongo wa **S** n'umurongo wa 4 x 4 uri hejuru bitanga igisubizo kiri mu *Ishusho 6*.


*Igishushanyo ca 6: Gukubita kw'inkingi ya mbere:*


$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$


Nk’intambwe ikurikira, amajambo yose ari muri matrix yobwirizwa guhindurwa amajambo menshi. Nk’akarorero, F1 igereranya byte 1 kandi yoba $x^7 + x^6 + x^5 + x^4 + 1$, na 03 igereranya byte 1 kandi yoba $x + 1$.


Ivyo gukubita vyose rero bikorwa **modulo** $x^8 + x^4 + x^3 + x + 1$. Ivyo bituma habaho kwongerako amapolynomial ane muri buri nzira ine y’inkingi. Uhejeje gukora izo nyongera **modulo 2**, uzoheza ubone ama polynomial ane. Imwe muri izo nkuru zigereranya urudodo rw'ibice 8, canke byte 1, ya **S**. Ivyo biharuro vyose ntituzobikora hano ku matrix iri *Igishushanyo ca 6* kuko ari vyinshi.


Iyo inkingi ya mbere imaze gutunganirizwa, izindi nkingi zitatu z’umurongo wa **S** ziratunganirizwa mu buryo nk’ubwo nyene. Amaherezo, ivyo bizotuma haba matrix ifise bytes cumi n’itandatu ishobora guhindurwa urutonde.


Nk'intambwe ya nyuma, urutonde **S** rufatanywa n'urufunguzo rw'uruziga kandi mu gikorwa ca **XOR**. Ivyo bivamwo Leta $S_1$. Ni ukuvuga,



- $S_1 = S \ yongeyeko K_0$


### Ivyiyumviro vya 2 gushika ku vya 10


Ivyiyumviro vya 2 gushika ku vya 9 ni ugusubiramwo gusa ivyigwa vya mbere, *mutatis mutandis*. Igice ca nyuma gisa cane n’ibindi vyabanje, kiretse ko intambwe ya **mix columns** ikurwaho. Ni ukuvuga ko urugendo rwa 10 rushirwa mu ngiro gutya:



- $S_9 \ukwongerako K_{10}$
- Gusubirira byte
- Guhindura imirongo
- $S_{10} = S \ivyongeyeko K_{10}$


Igihugu $S_{10}$ ubu gishizwe kuri $C_1$, ibice 128 vya mbere vy'inyandiko y'ibanga. Gukomeza mu bice bisigaye vy'inyandiko y'ibice 128 bitanga inyandiko yuzuye **C**.


### Ibikorwa vy'ibanga rya Rijndael


Ni igiki gituma habaho ibikorwa bitandukanye biboneka mu gitabu ca Rijndael?


Ata kwinjira mu ndondoro, imigambi yo gushiramwo amakuru isuzumwa ishingiye ku rugero itera urujijo n’ugukwiragira. Iyo umugambi wo gushiramwo amakuru ufise urugero runini rw'**urujijo**, bisigura ko inyandiko y'ibanga isa n'itandukanye cane n'inyandiko y'ibanga. Iyo umugambi wo gupfuka ufise urugero rwo hejuru rw'**ugukwiragira**, bisigura ko uguhinduka gutoyi kwose ku nyandiko rusangi gutuma habaho inyandiko y'ubupfumu itandukanye cane.


Iciyumviro c’ibikorwa biri inyuma y’ivyo bimenyetso vya Rijndael ni uko bizana urugero runini rw’uguvurungana n’ugukwiragira. Ivyo bitera urujijo biva ku gikorwa co gusubirira Byte, mu gihe ugukwiragira biva ku mirongo y’uguhindura n’ibikorwa vy’inkingi z’uguvanga.


# Ububiko bw'ibanga budahuye

<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>



## Ikibazo nyamukuru co gukwiragiza no kurongora

<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>


Nk’uko biri ku bijanye n’ubuhinga bwo gukingira amakuru, imigambi idahuye irashobora gukoreshwa kugira ngo habeho ibanga n’ukwemeza. Ariko rero, mu buryo butandukanye n’ubwo, izo migambi zikoresha urufunguzo rubiri aho gukoresha rumwe: urufunguzo rw’ibanga n’urw’abantu bose.


Turatangura itohoza ryacu n’ukuvumbura ubuhinga bwo gukingira amakuru butagira aho bugarukira, cane cane ingorane zatumye bubaho. Inyuma y’aho, turaganira ku kuntu imigambi y’ugushiramwo amakuru n’ugushingira intahe ivy’ukuri ikora ku rugero rwo hejuru. Twebwe rero, dushiramwo ibikorwa vya Hash, ari vyo bifasha gutahura imigambi y’ukwemeza ivy’ukuri, kandi bifise akamaro mu bindi bice vy’ubuhinga bwo gukingira amakuru, nk’ivy’amakode y’ukwemeza ubutumwa bushingiye kuri Hash twavuganye mu kigabane ca 4.


___



Twibaze ko Bob ashaka kugura ikoti rishasha ry’imvura kuri Jim’s Sporting Goods, ikigo kigurisha ibintu vyo gukina ku rubuga rwa interineti gifise abakiriya amamiliyoni muri Amerika y’Uburaruko. Ivyo bizoba ari vyo vya mbere abaguriye kandi ashaka gukoresha ikarita yiwe y’inguzanyo. Rero, Bob azobanza gukora konti muri Jim’s Sporting Goods, ivyo bikaba bisaba kohereza amakuru yiwe bwite nk’amakuru yiwe Address n’ayo ikarita y’inguzanyo. Arashobora rero guca mu ntambwe zikenewe kugira ngo agure iyo mpuzu y’imvura.


Bob na Jim’s Sporting Goods bazoshaka kumenya neza ko ubutumwa bwabo butekanye muri iyo nzira yose, bazirikanye ko Internet ari uburyo bwo guhanahana amakuru bufunguye. Bazoshaka kumenya neza, nk’akarorero, ko ata muntu yoshobora gutera ashobora kumenya neza ikarata y’inguzanyo ya Bob n’amakuru yerekeye Address, kandi ko ata muntu yoshobora gutera ashobora gusubiramwo ivyo yaguze canke ngo akore ivy’ibinyoma mw’izina ryiwe.


Igishushanyo c’ugushiramwo amakuru y’ukuri nk’uko vyavuzwe mu kigabane c’imbere coshobora ata gukeka gutuma amakuru hagati ya Bob na Jim’s Sporting Goods agira umutekano. Ariko biragaragara ko hariho intambamyi ngirakamaro zo gushitsa uwo mugambi.


Kugira ngo tubone ingero y’izo ntambamyi ngirakamaro, dufate ko twabaye mw’isi aho hari ibikoresho vyo gupima amakuru bihuye gusa. None Jim’s Sporting Goods na Bob vyoshobora gukora iki kugira ngo abantu bavugane ata nkomanzi?


Muri ivyo bihe, bobaye bakeneye amahera menshi kugira ngo bashobore kuvugana ata nkomanzi. Kubera ko Internet ari uburyo bwo guhanahana amakuru bufunguye, ntibashobora gusa Exchange urutonde rw’imfunguruzo kuri yo. Ku bw’ivyo, Bob n’uwuserukira Jim’s Sporting Goods bazokenera gukora Exchange y’urufunguzo ubwabo.


Imwe mu nzira zishoboka ni uko Jim’s Sporting Goods irema ibibanza bidasanzwe vy’imfunguruzo za Exchange, aho Bob n’abandi bakiriya bashasha bashobora kuronka urutonde rw’imfunguruzo zo guhanahana amakuru ata nkomanzi. Biragaragara ko ivyo vyotuma habaho amahera menshi mu bijanye n’ugutegura ibintu kandi bikagabanya cane ubushobozi abakiriya bashasha bashobora gukoresha mu kugura ibintu.


Canke rero, Jim’s Sporting Goods irashobora kohereza Bob imfunguruzo zibiri n’umuntu yizigirwa cane. Ivyo birashoboka ko ari vyiza kuruta gutunganya ibibanza nyamukuru vya Exchange. Ariko ivyo vyobaye bifise amahera menshi canecane iyo abakiriya benshi baguze ikintu kimwe canke bikeyi gusa.


Inyuma y’aho, umugambi w’ugushiramwo amakuru y’ukuri na wo nyene uhatira Jim’s Sporting Goods kubika imfunguruzo zitandukanye ku bakiriya babo bose. Ivyo vyoba ari ingorane ikomeye cane ku bakiriya ibihumbi n’ibihumbi, reka tuvuge amamiliyoni.


Kugira ngo utahure iyo ngingo ya nyuma, dufate ko Jim’s Sporting Goods iha umukiriya wese imfunguruzo zibiri zibiri. Ivyo vyotuma umukiriya wese—canke uwundi wese yoshobora kuronka izo mfunguruzo zibiri—asoma mbere n’ugukoresha nabi amakuru yose hagati ya Jim’s Sporting Goods n’abakiriya bayo. Woshobora rero kutakoresha ubuhinga bwo gukingira amakuru na gato mu guhanahana amakuru.


Mbere no gusubiramwo urutonde rw’imfunguruzo ku bakiriya bamwebamwe gusa ni umugenzo uteye ubwoba wo gucungera umutekano. Umuntu wese yoshobora gutera yoshobora kugerageza gukoresha ico kintu kiri muri uwo mugambi (wibuke ko abatera biyumvirwa ko bazi vyose ku bijanye n’uwo mugambi kiretse imfunguruzo, bihuye n’ingingo ngenderwako ya Kerckhoffs.)


Rero, Jim’s Sporting Goods yobwirizwa kubika imfunguruzo zibiri ku mukiriya wese, ata kuraba ingene izo mfunguruzo zibiri zigabanywa. Ivyo birerekana neza ingorane zitari nke ngirakamaro.



- Jim’s Sporting Goods yobwirizwa kubika amamiliyoni y’imfunguruzo zibiri, imwe ku mukiriya wese.
- Izo mfunguruzo zoba zitegerezwa gukingirwa neza, kuko zoba ari ikintu abasuma bashobora gutera. Uguhungabanya umutekano kwose kwosaba ko umuntu asubiramwo uguhinduranya imfunguruzo zizimvye, haba ku bibanza bidasanzwe vy’imfunguruzo Exchange canke biciye ku nzira y’ubutumwa.
- Umukiriya wese wa Jim’s Sporting Goods yobwirizwa kubika neza imfunguruzo zibiri i muhira. Gutakaza n’ubusuma bizoba, bisaba ko haba ugusubiramwo uguhinduranya urufunguruzo. Abakiriya bobwirizwa kandi guca muri iyo nzira ku yandi maduka yose yo kuri Internet canke ayandi mashirahamwe bipfuza kuvugana no gukorana na yo biciye kuri Internet.


Izo ngorane zibiri nyamukuru twahejeje kudondora zari ivyiyumviro vy'ishimikiro cane gushika mu mpera z'imyaka ya 1970. Zari zizwi nk'**ingorane yo gukwiragiza urufunguzo** n'**ingorane y'uburongozi bw'urufunguzo**, uko zikurikirana.


Birumvikana ko izo ngorane zari zama zihari, kandi kenshi zatuma umuntu agira umutwe mu bihe vya kera. Nk’akarorero, ingabo z’igisirikare zobwirizwa kwama zitanga ibitabu birimwo imfunguruzo kugira ngo zishobore kuvugana n’abakozi bo mu gisirikare ata nkomanzi, ivyo bikaba vyari gushobora gutwara ingorane nyinshi be n’amahera menshi. Ariko izo ngorane zariko zirarushiriza kuba mbi uko isi yariko iratera imbere mu bijanye n’uguhanahana amakuru ku ntambwe ndende, ku mbuga ngurukanabumenyi, cane cane ku bigo bitagira Leta.


Iyo izo ngorane zitatorwa umuti mu myaka ya 1970, birashoboka ko ugusumira neza kandi gutekanye kuri Jim’s Sporting Goods ntikwari kubaho. Nkako, igice kinini c’isi yacu yo muri iki gihe gifise ubuhinga bwo gukoresha ubutumwa bwo kuri Internet bukora kandi butekanye, ubuhinga bwo gukoresha banki kuri Internet be n’ugusuma, kumbure vyoba ari ibintu vy’ibinyoma gusa biri kure. Ikintu cose mbere gisa na Bitcoin nticari gishobora kubaho na gato.


None, mu myaka ya 1970 vyagenze gute? Bishoboka gute ko dushobora guca tugura ibintu kuri Internet ubwo nyene maze tukaja ku rubuga rwa Internet ata nkomanzi? Bishoboka gute ko dushobora guca twohereza Bitcoins kw’isi yose dukoresheje amatelefone yacu y’ubwenge?



## Amabwirizwa mashasha mu buhinga bwo gukingira amakuru

<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>


Mu myaka ya 1970, ingorane z’ingenzi zo gukwiragiza n’iz’uburongozi zari zafashe umutima w’umugwi w’abahinga mu vy’ubuhinga bw’amabanga y’Abanyamerika: Whitfield Diffie, Martin Hellman na Ralph Merkle. Kubera ko benshi mu bagenzi babo bariko barakekeranya cane, baragira ubwoba bwo kurondera umuti wo kubitorera umuti.


N’imiburiburi ikintu kimwe nyamukuru catumye bagira ico gikorwa ni ukubona imbere y’igihe yuko uguhanahana amakuru kuri orodinateri gufunguye kwogira ico gukoze cane kw’isi yacu. Nk’uko Diffie na Helmann babivuga mu 1976, .


> Guteza imbere ubuhinga bwo guhanahana amakuru bugenzurwa na orodinateri birasezerana ko abantu canke orodinateri zo mu mpande zitandukanye z’isi zizoshobora guhura ata ngorane kandi zitazimvye, ivyo bikaba bizosubirira ubutumwa bwinshi n’ingendo nyinshi n’ivy’itumanaho. Ku bikorwa vyinshi ivyo bimenyetso bitegerezwa gukingirwa kugira ngo ntibatege amatwi canke ngo ntibashiremwo ubutumwa butemewe n’amategeko. Ariko rero, muri iki gihe, umuti w’ingorane z’umutekano urasigaye inyuma cane y’ibindi bice vy’ubuhinga bwo guhanahana amakuru. *Ivyuma vy’ubuhinga bwa none ntibishobora gushitsa ibisabwa, kuko gukoresha ubuhinga bwavyo vyotera ingorane zikomeye abakoresha iyo sisitemu, ku buryo vyokuraho ivyiza vyinshi vyo gukoresha ubuhinga bwa teleprocessing.* [1]

Ugushikama kwa Diffie, Hellman na Merkle kwaravuyemwo ivyiza. Igitabo ca mbere c’ivyo bavuyemwo ni igitabu canditswe na Diffie na Helmann mu 1976 citwa “Ivyiyumviro bishasha mu bijanye n’ugukora amakuru y’ibanga.” Muri ryo, barashize ahabona uburyo bubiri bw’intango kuri Address ugusangira kw’ingenzi n’ingorane z’uburongozi bw’ingenzi.


Umuti wa mbere batanze wari *key-Exchange protocol* yo kure, ni ukuvuga amategeko agenga Exchange y’urufunguzo rumwe canke nyinshi zihuye ku muhora w’itumanaho udatekanye. Ubu iyo porotokole izwi kw'izina rya *urufunguzo rwa Diffie-Helmann Exchange* canke *urufunguzo rwa Diffie-Helmann-Merkle Exchange*. [2]


Kubera urufunguzo rwa Diffie-Helmann Exchange, abantu babiri babanza Exchange amakuru amwamwe ku mugaragaro ku muhora udatekanye nka Internet. Bashingiye kuri ayo makuru rero, bigenjeje neza, barahingura urufunguruzo ruringaniye (canke urufunguruzo rubiri ruringaniye) kugira ngo bashobore guhanahana amakuru ata nkomanzi. Naho abo bompi barema imfunguruzo zabo ku giti cabo, amakuru basangiye ku mugaragaro aratuma iyo nzira yo kurema imfunguruzo itanga ingaruka imwe kuri bompi.


Igihambaye ni uko naho umuntu wese ashobora kwihweza amakuru ahindurwa ku mugaragaro n’abafatanyabikorwa ku muhora udatekanye, ababuranyi babiri bonyene bariko baragira uruhara mu makuru Exchange ni bo bashobora kuyahinguramwo imfunguruzo zihuye.


Birumvikana ko ivyo bisa n’ibiteye kubiri n’ubwenge rwose. Ni gute imigambwe ibiri Exchange yoshobora gutanga amakuru amwamwe ku mugaragaro yotuma bo bonyene bashobora kuyihinguramwo imfunguruzo zihuye? Ni kuki uwundi muntu wese yihweza amakuru Exchange atashobora kurema izo mfunguruzo nyene?


Bishingiye ku biharuro vyiza bimwe bimwe vy’ukuri. Urufunguzo rwa Diffie-Helmann Exchange rukora biciye ku gikorwa c’inzira imwe gifise urugi rw’umutego. Reka tuganire ku nsobanuro y’ayo majambo abiri.


Twibaze ko wahawe igikorwa $f(x)$ n’igisubizo $f(a) = y$, aho $a$ ari agaciro kadasanzwe ka $x$. Tuvuga ko $f(x)$ ari **igikorwa c’inzira imwe** nimba vyoroshe kubara agaciro $y$ iyo uhawe $a$ na $f(x)$, ariko mu buryo bw’ubuhinga ntibishoboka kubara agaciro $a$ iyo uhawe $y$ na $f(x)$. Izina **igikorwa c’inzira imwe**, birashoboka ko rikomoka ku kuba mwene ico gikorwa ari ngirakamaro gusa mu kubara mu nzira imwe.


Hariho ibikorwa vy'inzira imwe bifise ico bita **umuryango w'umutego**. Naho mu vy’ukuri bidashoboka kubara $a$ bihawe $y$ na $f(x)$ gusa, hariho amakuru amwamwe $Z$ atuma kubara $a$ kuva kuri $y$ bishoboka mu buryo bw’ubuhinga. Iryo tangazo $Z$ rizwi kw'izina rya **umuryango w'umutego**. Imikorere y'inzira imwe ifise urugi rw'umutego izwi nka **imikorere y'umuryango w'umutego**.


Ntituzokwinjira mu ndondoro y’urufunguzo rwa Diffie-Helmann Exchange hano. Ariko mu vy’ukuri uwuriko aragira uruhara wese ararema amakuru amwamwe, igice kimwe kigasangizwa abantu bose, ayandi na yo akaguma ari ibanga. Buri ruhande rero rufata amakuru yabo y’ibanga n’amakuru ya bose asangiye n’uwundi kugira ngo rukore urufunguzo rw’ibanga. Kandi mu buryo bumwe bw’igitangaza, abo bompi bazoheza bafise urufunguruzo rumwe rw’ibanga.


Ishirahamwe ryose ryihweza gusa amakuru asangiye ku mugaragaro hagati y’iryo shirahamwe ryompi mu rufunguzo rwa Diffie Helmann Exchange ntirishobora gusubiramwo ivyo biharuro. Bazokenera amakuru y’ibanga ava kuri umwe muri abo babiri kugira ngo babikore.


Naho urufunguzo rwa Diffie-Helmann Exchange rwashikirijwe mu kinyamakuru co mu 1976 rudatekanye cane, nta gukeka ko urufunguzo rw’ishimikiro rw’urufunguzo rwa Diffie-Helmann ruca rukoreshwa n’ubu. Ikiruta vyose, itegeko ryose ry’ingenzi rya Exchange riri muri verisiyo nshasha y’itegeko ry’umutekano ry’ivy’ugutwara abantu n’ibintu (verisiyo 1.3) ni ryo ry’itegeko ry’umutekano ry’ivy’ugutwara abantu n’ibintu ryashikirijwe na Diffie na Hellman mu 1976. (http), ni co kigereranyo co guhanahana ibirimwo ku rubuga.


Igihambaye ni uko urufunguzo rwa Diffie-Helmann Exchange atari umugambi utaringaniye. Mu kuvuga ataco twirengagije, birashoboka ko ari mu rwego rw’ubuhinga bwo gukingira urufunguzo rw’urufunguzo ruringaniye. Ariko nk’uko urufunguzo rwa Diffie-Helmann Exchange n’ubuhinga bwo gukingira amakuru butagira aho bugarukira bishingiye ku bikorwa vy’imibare y’inzira imwe bifise inzugi z’imitego, biraganirwako hamwe.


Uburyo bwa kabiri Diffie na Helmann bahaye Address ingorane nyamukuru yo gukwiragiza no gucunga mu mpapuro zabo zo mu 1976, bwari, birumvikana, biciye ku buhinga bwo gukingira amakuru butagira aho bugarukira.


Mu buryo butandukanye n’uko bashikirije urufunguzo rwa Diffie-Hellman Exchange, batanze gusa imirongo rusangi y’ingene imigambi y’ubuhinga bwo gukingira amakuru idahuye yoshobora kwubakwa. Ntibatanga igikorwa na kimwe c’inzira imwe coshobora gushitsa mu buryo budasanzwe ibisabwa kugira ngo umuntu agire umutekano ubereye muri iyo migambi.


Ariko rero, ugushirwa mu ngiro kw’umugambi w’ubudasa kwabonetse haciye umwaka n’abahinga batatu batandukanye bo mu vy’inyigisho z’ubuhinga bwa none n’abahinga mu vy’imibare: Ronald Rivest, Adi Shamir na Leonard Adleman. [3] Ubuhinga bwo gukingira amakuru bashizeho bwaciye bumenyekana kw’izina rya **RSA cryptosystem** (inyuma y’amazina yabo y’uruvyaro).


Imikorere y’umuryango w’umutego ikoreshwa mu gupima amakuru atagira uburinganire (n’urufunguzo rwa Diffie Helmann Exchange) yose ifitaniye isano n’ibibazo bibiri nyamukuru **ibibazo vy’ubuhinga bwa Hard**: uguharura kw’ibiharuro vy’intango n’uguharura kw’ibiharuro vy’ibiharuro bitandukanye.


**Gucapura umubare w'intango** bisaba, nk'uko izina ribivuga, gucapura umubare wose mu bice vy'intango vyawo. Ikibazo ca RSA ni akarorero kazwi cane k’ubuhinga bwo gukingira amakuru bujanye n’ugucapura kw’ibice vy’imbere.


**Ikibazo ca logarithme itandukanye** ni ikibazo kiba mu migwi y'ingendo. Hatanzwe umuyagankuba uri mu mugwi w’ingendo kanaka, bisaba kubara igiharuro kidasanzwe gikenewe kugira ngo umuntu ashobore gutanga ikindi kintu kiri muri uwo mugwi kivuye mu muyagankuba.


Ivyiyumviro bishingiye kuri logarithme zitandukanye bishingiye ku bwoko bubiri nyamukuru bw’imigwi y’inzinguzingu: imigwi y’ugukubita y’imibare yose n’imigwi irimwo uturongo turi ku mirongo y’imirongo y’imirongo. Urufunguzo rwa Diffie Helmann rw’intango Exchange nk’uko rwerekanwa mu “Imirongo mishasha mu gukora amakuru y’ibanga” rukorana n’umugwi w’imibare yose igwiza. Bitcoin’s digital signing algorithm n’umugambi w’umukono wa Schnorr (2021) uherutse gushirwaho, vyose bishingiye ku ngorane y’imibare y’imirongo y’imirongo y’imirongo y’imirongo y’imirongo.


Igikurikira, tuzohindukira tuje ku nsiguro y’urugero rwo hejuru y’ibanga n’ukwemeza mu gihe c’uburinganire. Ariko rero, imbere y’uko tubigira, turakeneye kwandika muri make ivyerekeye kahise.


Ubu bisa n’ibishoboka ko umugwi w’abahinga mu vy’amabanga n’imibare bo mu Bwongereza bakorera ku cicaro gikuru ca Leta kijejwe itumanaho (GCHQ) bari bavumbuye ivyo bintu twavuze haruguru imyaka mikeyi imbere y’aho. Iryo tsinda ryari rigizwe na James Ellis, Clifford Cocks na Malcolm Williamson.


Dushingiye ku nkuru zabo bwite n’iza GCHQ, ni James Ellis yabanje gutegura iciyumviro co gukoresha urufunguzo rwa bose mu 1969. Bivugwa ko Clifford Cocks yaciye avumbura uburyo bwo gukoresha urufunguzo rwa RSA mu 1973, Malcolm Williamson na we akabona iciyumviro c’urufunguzo rwa Diffie Helmann Exchange mu 1973. bivugwa ko bitamenyekanye gushika mu 1997, kubera ibanga ry’igikorwa cakozwe muri GCHQ.



**Ivyiyumviro:**


[1]. 644.


[2] Ralph Merkle kandi aravuga ku masezerano y'ingenzi ya Exchange mu gitabu “Ivy'itumanaho bitekanye ku nzira zidatekanye”, _Ivy'itumanaho ry'Ishirahamwe ry'Ivyuma vy'Ibarabara_, 21 (1978), 294–99. Naho Merkle mu vy’ukuri yashizeho uru rupapuro imbere y’urupapuro rwa Diffie na Hellman, rwasohowe mu nyuma. Umuti wa Merkle ntutekanye cane, utandukanye n’uwa Diffie-Hellman.


[3] Ron Rivest, Adi Shamir, na Leonard Adleman, “Uburyo bwo kuronka imikono y’ubuhinga bwa none n’ubuhinga bwo gukoresha ubuhinga bwa none”, _Ivy’itumanaho ry’ishirahamwe ry’ubuhinga bwa none_, 21 (1978), urupapuro rwa 120–26.


[4] Amateka meza y'ivyo bintu vyavumbuwe atangwa na Simon Singh, _Igitabo c'Itegeko_, Igihugu ca kane (Londres, 1999), Igice ca 6.





## Ububiko butaringaniye n'ukwemeza

<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>


Incamake y'**ugushiramwo amakuru ataco akora** bifashijwe na Bob na Alice iraboneka mu *Igishushanyo 1*.


Alice ibanza kurema urufunguzo rubiri, rugizwe n’urufunguzo rumwe rwa bose ($K_P$) n’urufunguzo rumwe rw’ibanga ($K_S$), aho “P” muri $K_P$ ihagarariye “rwa bose” na “S” muri $K_S$ ihagarariye “ibanga”. Araheza akagabira abandi urwo rufunguzo rwa bose ata co yishisha. Tuzosubira ku ndondoro y’ivyo bikorwa vyo gutanga ibitabu haciye igihe gitoyi. Ariko ubu, wiyumvire ko umuntu wese, harimwo na Bob, ashobora kuronka urufunguzo rwa bose rwa Alice $K_P$.


Mu nyuma, Bob ashaka kwandika ubutumwa $M$ kuri Alice. Kubera ko harimwo amakuru y’agaciro, ashaka ko ibirimwo biguma ari ibanga kuri bose kiretse Alice. Rero, Bob abanza gupfuka ubutumwa bwiwe $M$ akoresheje $K_P$. Araheza arungika igisomwa c’ibanga $C$ kuri Alice, na we agaca afungura $C$ akoresheje $K_S$ kugira ngo asohore ubutumwa bw’intango $M$.


*Ishusho ya 1: Ububiko budahuye*


![Figure 1: Asymmetric encryption](assets/en/018.webp "Figure 1: Asymmetric encryption")



Umwansi wese yumviriza mu vyo Bob na Alice bavuga arashobora kwihweza $C$. Arazi kandi $K_P$ n'ubuhinga bwo gupfuka $E(\cdot)$. Ariko ikintu gihambaye ni uko ayo makuru adatuma uwutera ashobora gusobanura neza inyandiko y’ibanga $C$. Gukuraho amakuru bisaba cane cane $K_S$, iyo uwutera atagira.


Ivyiyumviro vy’ugushiramwo amakuru bihuye muri rusangi bikeneye gukingirwa n’umuterabwoba ashobora gushiramwo amakuru y’inyandiko rusangi (bizwi nk’umutekano w’igitero c’inyandiko zitowe). Ariko rero, ntivyateguwe n’intumbero itomoye yo kwemera ko uwutera canke uwundi muntu uwo ari we wese ashobora kurema mwene izo nyandiko zifise akamaro.


Ivyo bitandukanye cane n’umugambi wo gupfuka amakuru ataco akora, aho intumbero yawo yose ari iyo kwemerera umuntu wese, harimwo n’abatera, gutanga amakuru y’ubupfumu afise akamaro. Ivyiyumviro vy'ugushiramwo amakuru ataringaniye birashobora rero kwandikwa nk'**ibiharuro vy'ugushikira vyinshi**.


Kugira ngo utahure neza ibiriko biraba, wiyumvire ko aho kohereza ubutumwa biciye ku buhinga bwa none, Bob yashaka kohereza ikete ry’umubiri mu mpisho. Uburyo bumwe bwo kumenya ko haba ibanga ni uko Alice yorungika urufunguzo rutekanye kuri Bob, ariko akaguma afise urufunguzo rwo kurufungura. Bob amaze kwandika ikete ryiwe, yari gushobora gushiramwo iryo kete mu gasandugu akarifunga n’urufunguzo rwa Alice. Yashobora rero kohereza iyo sandugu yugarijwe irimwo ubutumwa kuri Alice afise urufunguruzo rwo kuyifungura.


Naho Bob ashobora gufunga iyo ngufuri, we canke uwundi muntu wese afata iyo sandugu ntashobora gukuraho iyo ngufuri nimba vy’ukuri ifise umutekano. Alice niwe wenyene ashobora kuyifungura akabona ibirimwo mw’ikete rya Bob kuko niwe afise urufunguzo.


Igishushanyo c’ugushiramwo amakuru ataco kivuze ni, mu kuvuga mu buryo busanzwe, uburyo bwa digitale bw’iyi nzira. Urufunguzo rw’ingufu rusa n’urufunguzo rwa bose kandi urufunguzo rw’ingufu rusa n’urufunguzo rw’ibanga. Ariko rero, kubera ko iyo ngufuri ari iya digitale, biroroshe cane kandi ntibitwara amahera menshi cane ko Alice ayitanga ku muntu wese yoshobora gushaka kumurungikira ubutumwa bw’ibanga.


Ku bijanye n'ukwemeza mu buryo butaringaniye, dukoresha **imikono y'imibare**. Ivyo rero, bifise igikorwa kimwe n'amakode y'ukwemeza ubutumwa mu nzira y'uburinganire. Incamake y'imikono y'ubuhinga bwa none iraboneka mu *Igishushanyo ca 2*.


Bob abanza kurema urufunguzo rubiri, rugizwe n'urufunguzo rwa bose ($K_P$) n'urufunguzo rw'ibanga ($K_S$), hanyuma agatanga urufunguzo rwiwe rwa bose. Iyo ashaka kohereza ubutumwa bwemewe kuri Alice, abanza gufata ubutumwa bwiwe $M$ n'urufunguzo rwiwe rw'ibanga kugira ngo akore **umukono w'inyandiko** $D$. Bob aca arungikira Alice ubutumwa bwiwe hamwe n’umukono wa digitale.


Alice yinjiza ubutumwa, urufunguzo rwa bose, n'umukono wa digitale mu **ubuhinga bwo kugenzura**. Iyi algorithme itanga **ukuri** ku musinya ukora, canke **ikinyoma** ku musinya udakora.


Umukono wa digitale ni, nk’uko izina ryawo rivyerekana neza, ungana n’umukono wa digitale ku makete, ku masezerano n’ibindi. Nkako, umukono wo kuri interineti akenshi uratekanye cane. Ugize utwigoro tumwetumwe, urashobora kwihenda mu gushirako umukono wanditse; igikorwa corohereza abantu kubera ko kenshi imikono yanditswe idasuzumwa neza. Ariko rero, umukono w’inyandiko utekanye, ni, nk’uko nyene kode y’ubutumwa itekanye, **udashobora guhindurwa**: ni ukuvuga, n’umugambi w’umukono w’inyandiko utekanye, nta n’umwe ashobora gukora umukono w’ubutumwa buca mu buryo bwo kugenzura, kiretse afise urufunguzo rw’ibanga.


*Ishusho ya 2: Ivyemezo bitaringaniye*


![Figure 2: Asymmetric authentication](assets/en/019.webp "Figure 2: Asymmetric authentication")



Nk’uko biri ku bijanye n’ugushiramwo amakuru atari yo, turabona itandukaniro riryoshe hagati y’imikono ya digitale n’amakode y’ukwemeza ubutumwa. Ku bijanye n’ivyo vya nyuma, ubuhinga bwo kugenzura bushobora gukoreshwa gusa n’umwe mu bagize uburenganzira bwo guhanahana amakuru ataco akora. Ivyo ni kubera ko bisaba urufunguzo rw’ibanga. Mu gihe c'uburinganire, ariko, umuntu wese arashobora kugenzura umukono wa digitale $S$ wakozwe na Bob.


Ivyo vyose bituma imikono ya digitale iba igikoresho gikomeye cane. Ni ryo shingiro, nk’akarorero, ryo gushinga imikono ku masezerano ashobora kugenzurwa ku bw’intumbero zijanye n’amategeko. Iyo Bob aba yashize umukono kuri Contract muri Exchange iri hejuru, Alice irashobora kwereka ubutumwa $M$, Contract, n’umukono $S$ ku rubanza. Urukiko rurashobora rero kugenzura umukono rukoresheje urufunguzo rwa bose rwa Bob. [5]


Ku kindi kigereranyo, imikono ya digitale ni ikintu gihambaye mu bijanye no gukwiragiza porogarama zitekanye be n’ugukwiragiza porogarama zishasha. Ubwo bwoko bwo kugenzura abantu bose ntibwoshobora kwigera buremwa hakoreshejwe gusa amakode y'ubutumwa bwo kwemeza.


Nk'akarorero ka nyuma k'ububasha bw'imikono y'ubuhinga bwa none, rimbura Bitcoin. Kimwe mu vyiyumviro bitari vyo bikunze gufatwa ku bijanye na Bitcoin, cane cane mu binyamakuru, ni uko amafaranga akoreshwa mu buryo butari bwo: ntabwo ari ko biri. Ahubwo, amafaranga y’ubudandaji ya Bitcoin akorana n’imikono ya digitale kugira ngo umuntu agire umutekano.


Bitcoins ziriho mu bice vyitwa ibisohoka mu bikorwa bitakoreshejwe (canke **UTXO’s**). Twibaze ko uronka amahera atatu ku Bitcoin Address yihariye ku bitcoins 2 kuri imwe yose. Ubu nta bitcoins 6 ufise kuri iyo Address. Ahubwo, ufise ibice bitatu vy’ama bitcoins 2 yugarijwe n’ingorane y’ubuhinga bwa none ijana n’iyo Address. Ku bijanye n’ukwishura kwose, urashobora gukoresha kimwe, bibiri canke vyose bitatu muri ivyo bice, bivanye n’ingene ukeneye amahera.


Ikimenyamenya ca Ownership ku biva mu bikorwa bitakoreshejwe akenshi vyerekanywe biciye ku musinya umwe canke myinshi y’ubuhinga bwa none. Bitcoin ikora neza cane kubera ko imikono y’ibanga y’ukuri ku biva mu bikorwa vy’ubudandaji bitakoreshejwe idashoboka gukora, kiretse iyo ufise amakuru y’ibanga asabwa kugira ngo uyakore.


Ubu, amafaranga y’ibikorwa vya Bitcoin arashiramwo mu buryo buboneye amakuru yose akeneye gusuzumwa n’abagira uruhara mu rubuga, nk’inkomoko y’ibiva mu bikorwa vy’ubudandaji bitakoreshejwe vyakoreshejwe mu gucuruza. Naho bishoboka guhisha amwe muri ayo makuru kandi akaguma yemerera kugenzura (nk’uko amafaranga amwe amwe y’ubuhinga bwa none nka Monero abigira), ivyo na vyo nyene biratuma haba ingorane zidasanzwe z’umutekano.


Rimwe na rimwe haraduka urujijo kubera imikono ya digitale n’imikono yanditswe ifashwe mu buryo bwa digitale. Mu gihe ca nyuma, ufata ishusho y’umukono wawe wanditse ukawushira ku nyandiko yo mu buhinga bwa none nk’iyitwa Contract y’akazi. Ariko rero, ivyo si umukono w’ibarabara mu buryo bw’ubuhinga bwa none. Ico ca nyuma ni umubare muremure gusa ushobora gusohoka gusa mu kuba umuntu afise urufunguzo rw’ibanga.


Nk'uko biri mu nzira y'urufunguzo rw'urugero, urashobora kandi gukoresha imigambi y'ububiko n'ukwemeza hamwe. Ingingo ngenderwako nk’izo nyene zirakora. Mbere na mbere, ushobora gukoresha urufunguzo rutandukanye rw’ibanga n’urwa bose kugira ngo ushiremwo amakuru no gukora imikono ya digitale. Ikindi, ukwiye kubanza gupfuka ubutumwa hanyuma ukabushingira intahe.


Igihambaye ni uko mu bikorwa vyinshi, ubuhinga bwo gukingira amakuru butagira aho bugarukira butakoreshwa mu gihe cose c’uguhanahana amakuru. Ahubwo, mu bisanzwe izokoreshwa gusa ku *Exchange symmetric keys* hagati y'abazovugana.


Nk’akarorero, ni ko bigenda iyo ugura ibintu kuri Internet. Kumenya urufunguzo rwa bose rw’umucuruzi, arashobora kukurungikira ubutumwa bushizweko umukono ushobora kugenzura ko ari ubw’ukuri. Kuri ivyo, urashobora gukurikiza imwe mu mirongo ngenderwako myinshi yo guhana imfunguruzo zihuye kugira ngo uvugane ata nkomanzi.


Imvo nyamukuru ituma uburyo bwavuzwe haruguru bukoreshwa kenshi ni uko ubuhinga bwo gukingira amakuru butaringaniye bukora neza cane kuruta ubuhinga bwo gukingira amakuru butaringaniye mu gutanga urugero runaka rw’umutekano. Iyi ni yo mpamvu imwe ituma tugikeneye ubuhinga bwo gukingira urufunguzo rw’urufunguzo ruringaniye iruhande y’ubuhinga bwo gukingira urufunguzo rwa bose. Ikindi, ubuhinga bwo gupfuka amakuru y’urufunguzo ruringaniye ni ikintu gisanzwe cane mu bikorwa vy’umwihariko nk’uwukoresha mudasobwa apfuka amakuru yiwe bwite.


None ni gute nyabuna imikono ya digitale n’ugushiramwo urufunguzo rwa bose Address bitera ingorane zo gukwiragiza urufunguzo n’ugucungera urufunguzo?


Nta n’inyishu imwe iri aha. Asymétrique cryptography ni igikoresho kandi nta buryo bumwe bwo gukoresha ico gikoresho. Ariko reka dufate akarorero kacu ka mbere kavuye muri Jim’s Sporting Goods kugira ngo twereke ingene ibibazo vyoshobora gutorwa muri aka karorero.


Kugira ngo utangure, Jim’s Sporting Goods yoshobora kwegera **ubuyobozi bw’ivyemezo**, ishirahamwe rifasha mu gutanga urufunguzo rwa bose. Ikigo kijejwe gutanga icemezo cokwandika amakuru amwamwe yerekeye Jim’s Sporting Goods kikagiha urufunguzo rwa bose. Ivyo rero vyorungikira Jim’s Sporting Goods icemeza, kizwi nka **icete ca TLS/SSL**, n’urufunguzo rwa Jim’s Sporting Goods rwashizweko umukono hakoreshejwe urufunguzo rwa bose rw’ubuyobozi bw’icemeza. Muri ubwo buryo, ubuyobozi bw’icemezo bwemeza ko urufunguzo runaka rwa bose ari urwa Jim’s Sporting Goods vy’ukuri.


Urufunguruzo rwo gutahura iyo nzira n’ivyemezo vya TLS/SSL ni uko, naho muri rusangi utazogira urufunguzo rwa bose rwa Jim’s Sporting Goods rubitswe ahantu hose kuri mudasobwa yawe, urufunguzo rwa bose rw’abajejwe ivyemezo vyemewe rubitswe vy’ukuri mu mucukumbuzi wawe canke muri sisitemu yawe ikoresha. Ivyo bibikwa mu vyitwa **ivyemezo vy'imizi**.


Ku bw’ivyo, igihe Jim’s Sporting Goods iguha icemeza ko ari TLS/SSL, urashobora kugenzura umukono w’umukuru w’icemezo biciye ku cete c’umuzi mu mucukumbuzi wawe canke muri sisitemu yawe. Nimba iyo sinyatire ari yo, urashobora kwemera udakeka ko urufunguzo rwa bose ruri ku cete ari urw’ikigo Jim’s Sporting Goods. Kuri ivyo, biroroshe gushinga umurongo wo guhanahana amakuru ata nkomanzi na Jim’s Sporting Goods.


Ugutanga ivy’ingenzi ubu vyaciye vyoroshe cane ku bikoresho vya Jim’s Sporting Goods. Si Hard kubona ko uburongozi bw’ingenzi na bwo nyene bwacitse bworoshe cane. Aho kubika ibihumbi vy’imfunguruzo, Jim’s Sporting Goods ikeneye gusa kubika urufunguzo rw’ibanga ruyifasha gukora imikono ku rufunguzo rwa bose ku cete cayo ca SSL. Igihe cose umukiriya aza ku rubuga rwa Jim’s Sporting Goods, barashobora gushinga urubuga rwo guhanahana amakuru rutekanye bakoresheje urufunguzo rwa bose. Abakiriya na bo nyene ntibakeneye kubika amakuru ayo ari yo yose (uretse imfunguruzo za bose z’inzego z’ivyemezo zemewe muri sisitemu yabo yo gukoresha no mu mucukumbuzi wabo).


**Ivyiyumviro:**


[5] Imigambi yose igerageza gushika ku kudahakana, iyo yindi nsiguro twavuganye mu kigabane ca 1, izokenera ku mushinge wayo gushiramwo imikono y’ubuhinga bwa none.




## Ibikorwa vya Hash

<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>


Ibikorwa vya Hash biri hose mu vy’ubuhinga bwo gukingira amakuru. Si imigambi y’uburinganire canke y’uburinganire, ariko igwa mu rwego rw’ubuhinga bw’ibanga mu buryo bwayo bwite.


Twaramaze guhura n’ibikorwa vya Hash mu kigabane ca 4 n’uguhingura ubutumwa bwo kwemeza bushingiye kuri Hash. Birahambaye kandi mu bijanye n’imikono ya digitale, naho nyene kubera imvo itandukanye gatoyi: Imikono ya digitale ikoreshwa canecane ku gaciro ka Hash k’ubutumwa bumwe bumwe (bushizwemwo), aho gukorwa ku butumwa nyabwo (bushizwemwo). Muri iki gice, nzotanga intangamarara yimbitse cane y’ibikorwa vya Hash.


Reka dutangure n’ugusobanura igikorwa ca Hash. **Hash function** ni igikorwa cose gishobora kubarwa neza gifata ivyinjijwe vy'ubunini butari bwo kandi kigatanga ibisohoka vy'uburebure butahinduka.


**Ibikorwa vya Hash vy'ubuhinga bwo gukingira amakuru** ni igikorwa ca Hash gusa gifise akamaro ku bikorwa vyo gukingira amakuru. Igisohoka c'igikorwa ca Hash c'ubuhinga bwa none citwa **Hash**, **agaciro ka Hash**, canke **ubutumwa bujanye n'inyandiko**.


Mu bijanye n’ubuhinga bwo gukingira amakuru, “igikorwa ca Hash” mu bisanzwe kivuga igikorwa ca Hash co gukingira amakuru. Nzokwemera uwo mugenzo kuva ng’aha gushika hanze.


Akarorero k'igikorwa ca Hash gikundwa cane ni **SHA-256** (ubuhinga bwa Hash butekanye 256). Utitaye ku bunini bw'inyungu (nk'akarorero, ibice 15, ibice 100, canke ibice 10.000), iyi nzira izotanga agaciro k'ibice 256 Hash. Aha hepfo ushobora kubona ingero nke z'ibisohoka vy'igikorwa ca SHA-256.


“Muraho”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`


“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`


“Ugushiramwo amakuru y’ibanga biraryoshe”:


Ivyo vyose bivako ni ibice 256 vy’ukuri vyanditswe mu buryo bw’imirongo itandatu (umubare wose w’imirongo itandatu ushobora guserurwa n’imirongo ine y’imirongo ibiri). Rero naho woba warashize igitabu ca Tolkien *Umukama w’Impeta* mu gikorwa ca SHA-256, igisohoka coba kikiri 256 bits.


Ibikorwa vya Hash nka SHA-256 bikoreshwa ku ntumbero zitandukanye mu gukora amakuru y’ibanga. Ivyo bikoresho bisabwa ku gikorwa ca Hash vy'ukuri bivana n'aho igikorwa kinaka gikoreshwa. Hariho ibintu bibiri nyamukuru vyipfuzwa muri rusangi ku bikorwa vya Hash mu gukora amakuru y’ibanga: [6]


1. Uguhangana n'ugutombora

2. Kwihisha


Igikor ca Hash $H$ kivugwa ko **kidashobora gutombora** iyo bidashoboka kuronka agaciro kabiri, $x$ na $y$, ku buryo $x \neq y$, yamara $H(x) = H(y)$.


Ibikorwa vya Hash bishobora guhangana n’ugutomboka birahambaye, nk’akarorero, mu kugenzura porogarama. Twibaze ko wipfuza gukura kuri Windows Bitcoin core 0.21.0 (porogarama ya server yo gukora uruja n’uruza rw’urubuga rwa Bitcoin). Intambwe nyamukuru wobwirizwa gutera, kugira ngo ugenzure ko iyo porogarama yemewe, ni izi:


1. Ubanza gukura no kwinjiza imfunguruzo za bose z’umuntu umwe canke benshi mu batererano Bitcoin core muri porogarama ishobora kugenzura imikono ya digitale (nk’akarorero Kleopetra). Ushobora gusanga izo mfunguruzo za bose [hano] Ni vyiza ko ugenzura porogarama ya Bitcoin core ukoresheje imfunguruzo za bose zivuye ku batererano benshi.

2. Inyuma, ukeneye kugenzura imfunguruzo za bose washizemwo. Nibura intambwe imwe ukwiye gutera ni ukugenzura ko imfunguruzo za bose wabonye ari zimwe n’izo zasohowe mu bindi bibanza bitandukanye. Ushobora, nk’akarorero, kuraba amapaji y’urubuga bwite, amapaji ya Twitter, canke amapaji ya Github y’abantu washizemwo imfunguruzo zabo za bose. Mu bisanzwe uku kugereranya imfunguruzo za bose bikorwa mu kugereranya Hash ngufi y’urufunguzo rwa bose ruzwi nk’ikimenyetso c’urutoke.

3. Hanyuma, ukeneye gukuraho igikorwa ca Bitcoin core ku rubuga rwabo (www.bitcoincore.org). Hazoba hariho amapaki azokoreshwa kuri Linux, Windows, na MAC.

4. Igikurikira, ubwirizwa kurondera amadosiye abiri asohoka. Irya mbere ririmwo SHA-256 Hash yemewe y’ibikorwa mwaronse hamwe n’ama hashes ku bindi bikoresho vyose vyasohotse. Iyindi dosiye yo gusohora izoba irimwo imikono y'abaterankunga batandukanye ku dosiye yo gusohora n'ama hashes y'amapaki. Izo dosiye zompi zo gusohora zikwiye kuba ziri ku rubuga rwa Bitcoin core.

5. Hanyuma, wokenera kubara SHA-256 Hash y’igitabu ca executable wakuye ku rubuga rwa Bitcoin core kuri mudasobwa yawe bwite. Wewe rero, ugereranye iki ciyumviro n’ico ku bijanye n’ivyo mu gisata ca Hash ku bijanye n’ivyo gukora. Na bo nyene bakwiye kuba ari bamwe.

6. Ubwa nyuma, wobwirizwa kugenzura ko umukono umwe canke myinshi ya digitale kuri dosiye y’isohoka n’ama hashes y’amapaki yemewe vy’ukuri ihuye n’urufunguzo rumwe canke nyinshi za bose wazanye (isohorwa rya Bitcoin core ntiryama rishirwako umukono na bose). Ivyo ushobora kubikora ukoresheje porogarama nka Kleopetra.


Uwo murongo wo kugenzura porogarama ufise ivyiza bibiri nyamukuru. Ica mbere, biratuma ata makosa yabaye mu gutangaza igihe umuntu yariko arakura ku rubuga rwa Bitcoin core. Ubwa kabiri, biratuma ata n’umwe akugirira nabi yari gushobora kugutuma ukura kuri interineti kode yahinduwe kandi iteye akaga, haba mu gutera urubuga rwa Bitcoin core canke mu gufata uruja n’uruza.


Ni gute nyabuna uburyo bwo kugenzura porogarama buri hejuru bukingira ivyo bibazo?


Niwaba warasuzumye n’umwete imfunguruzo za bose wazanye, rero urashobora kwemera neza ko izo mfunguruzo ari izabo kandi ko zitagira ico zikoze. Kubera ko imikono ya digitale ifise ubudashobora guhindurwa, urazi ko abo batererano bonyene bari gushobora gukora umukono wa digitale ku ma hashes yemewe y’amapaki ku dosiye y’isohoka.


Twibaze ko imikono iri kuri dosiye y’isohoka waronse isohotse. Ubu ushobora kugereranya agaciro ka Hash waharuriye mu karere ka Windows executable waronse n’ako kari muri dosiye y’isohoka yashizweko umukono neza. Nk’uko mubizi SHA-256 Hash function ni collion resistant, match bisigura ko executable yawe ari kimwe nyene n’executable yemewe.


Reka noneho duhindukire ku kintu ca kabiri rusangi c'ibikorwa vya Hash: **kwihisha**. Igikorwa cose ca Hash $H$ kivugwa ko gifise ubushobozi bwo kwihisha iyo, ku $x$ iyo ari yo yose yatowe mu buryo bw'impfagusa kuva mu rutonde runini cane, bidashoboka kuronka $x$ iyo gusa ihawe $H(x)$.


Hasi, urashobora kubona igisohoka ca SHA-256 c’ubutumwa nanditse. Kugira ngo ubutumwa bube buhagije, bwarimwo uruhererekane rw’inyuguti zavutse mu buryo butari bwo ku mpera. Kubera ko SHA-256 ifise ubushobozi bwo kwihisha, nta n’umwe yoshobora gusobanura ubwo butumwa.



- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`


Ariko sinzobasiga mu gahinda gushika SHA-256 igoyagoya. Ubutumwa bw’intango nanditse bwari ubu:



- "Ubu ni ubutumwa busanzwe, canke busanzwe. Iki gice c'intango si co, ariko nzoheza n'inyuguti zimwe zimwe zidasanzwe kugira ngo menye neza ko ubutumwa butamenyekana cane. XLWz4dVG3BxUWm7zQ9qS".


Uburyo busanzwe Hash ikora n’umutungo wo kwihisha ikoreshwa ni mu gucunga ijambobanga (collision-resistance na yo nyene irahambaye kuri iyi porogarama). Ivyo vyose bishingiye kuri konti yawe yo kuri internet nka Facebook canke Google ntibizobika amajambo y’ibanga yawe kugira ngo ushobore gushika kuri konti yawe. Ahubwo bazobika gusa Hash y’iryo jambobanga. Igihe cose wuzuje ijambobanga ryawe ku mucukumbuzi, Hash irabanza kubarwa. Iyo Hash yonyene yoherezwa kuri server y’uwutanga serivisi maze igagereranywa na Hash ibitswe mu rutonde rw’amakuru rw’inyuma. Ivyo bikoresho vy’ukwihisha birashobora gufasha kumenya neza ko abatera badashobora kubigarura ku gaciro ka Hash.


Gucungera ijambobanga biciye ku hashes, birashoboka, bikora gusa iyo abakoresha mu vy’ukuri bahisemwo amajambobanga agoye. Igikoresho co kwihisha ciyumvira ko x itoranywa mu buryo butari bwo mu rutonde runini cane. Guhitamwo amajambo y’ibanga nka “1234”, “mypassword”, canke itariki y’amavuko yawe ntibizoguha umutekano nyawo. Urutonde rurerure rw’amajambo banga asanzwe n’ama hashes yayo arahari abatera bashobora gukoresha iyo bashobora kuronka Hash y’ijambo banga ryawe. Ubwo bwoko bw’ibitero buzwi kw’izina rya **ibitero vy’inkoranyamagambo**. Nimba abagutera bazi ibintu bimwebimwe vyerekeye wewe, boshobora kandi kugerageza gutekereza ku bintu bimwebimwe. Ni co gituma, wama ukeneye amajambo banga maremare kandi atekanye (vyiza ni imirongo miremire, idasanzwe iva ku mucungerezi w’amajambo banga).


Rimwe na rimwe igikorwa coshobora gukenera igikorwa ca Hash gifise ubushobozi bwo guhangana n’ugutombora n’ukwihisha. Ariko nta gukeka ko atari imisi yose. Uburyo bwo kugenzura porogarama twavuganye, nk’akarorero, busaba gusa ko igikorwa ca Hash kigaragaza ubushobozi bwo guhangana n’ugutomboka, kwihisha si ikintu gihambaye.


Naho ubushobozi bwo guhangana n’ugutomboka n’ukwihisha ari vyo bintu nyamukuru bironderwa mu bikorwa vya Hash mu bijanye n’ubuhinga bwo gukingira amakuru, mu bikorwa bimwebimwe ubundi bwoko bw’ibintu na vyo nyene vyoshobora kuba vyiza.



**Ivyiyumviro:**


[6] Amajambo “kwihisha” si ururimi rusanzwe, ariko yakuwe cane cane kuri Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, na Steven Goldfeder, *Bitcoin n’ubuhinga bw’amahera y’amahera*, Ikinyamakuru ca kaminuza ya Princeton (Princeton, 2016), igice ca 1.



# Ubuhinga bwa RSA

<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>




## Ikibazo c'ugutanga

<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>


Naho ubuhinga bwo gukingira amakuru buringaniye busanzwe busanzwe ku bantu benshi, ivyo si ko biri ku buhinga bwo gukingira amakuru butaringaniye. Naho woba ushobora kuba uryohewe n’insobanuro yo ku rwego rwo hejuru yatanzwe mu bice vyabanje, ushobora kuba uriko uribaza neza na neza ibikorwa vy’inzira imwe n’ingene nyavyo bikoreshwa mu kwubaka imigambi idahuye.


Muri iki gice, nzokuraho bimwe mu bitangaje bikikuje ubuhinga bwo gukingira amakuru butagira aho bugarukira, mu kuraba cane akarorero kamwe kamwe, ni ukuvuga ubuhinga bwo gukingira amakuru bwa RSA. Mu gice ca mbere, nzobabwira ingorane y’ugucapura (factorization) ingorane ya RSA ishingiyeko. In will rero, izovuga ivyiza bitari bike biva ku ciyumviro c’imibare. Mu gice ca nyuma, tuzoshira hamwe ayo makuru kugira ngo dusigure ingorane ya RSA, n’ingene ivyo bishobora gukoreshwa mu guhingura imigambi y’ubuhinga bwa cryptography asymétrique.


Kwongera ubwo burebure ku kiganiro cacu si igikorwa coroshe. Bisaba gushiramwo ivyiyumviro n’ivyiyumviro bikeyi cane vyerekeye imibare. Ariko ntureke ngo imibare ikubuze. Gukora muri iki kiganiro bizokwongereza cane ugutahura kwawe ku bijanye n’ivyo ari vyo bishingiyeko ubuhinga bwo gukingira amakuru atagira aho bugarukira kandi ni ishoramari ryiza.


Reka noneho tubanze tuje ku ngorane y’ugukora factoring.


___



Igihe cose uguze imibare ibiri, tuvuge $a$ na $b$, tuvuga imibare $a$ na $b$ nk'**ibiharuro**, igisubizo na co kikaba **igisubizo**. Kugerageza kwandika umubare $N$ mu gukubita kw’ibice bibiri canke birenze vyitwa **uguteranya** canke **uguteranya**. [1] Ushobora kwita ingorane iyo ari yo yose isaba ivyo **ingorane yo gucapura**.


Haciye nk'imyaka 2.500, umuhinga mu vy'imibare w'Umugiriki yitwa Euclid wo muri Alegizandiriya yavumbuye iciyumviro nyamukuru kijanye n'ugucapura imibare yose. Mu bisanzwe yitwa **itegeko ry’ugucapura ridasanzwe** kandi rivuga ibi bikurikira:


**Iciyumviro ca 1**. Umubare wose $N$ uruta 1 ni umubare w'intango, canke ushobora kuvugwa nk'igisubizo c'ibiharuro vy'intango.


Igice ca nyuma c’iri jambo cose gisobanura ni uko ushobora gufata umubare wose utari umubare w’intango $N$ uruta 1, ukawundika nk’ugukubita kw’imibare y’intango. Aha hepfo hari ingero nyinshi z’imibare yose idasanzwe yanditswe nk’igisubizo c’ibiharuro vy’intango.



- $18 = 2 \cakadomo 3 \cakadomo 3 = 2 \cakadomo 3^2$
- $84 = 2 \cakadomo 2 \cakadomo 3 \cakadomo 7 = 2^2 \cakadomo 3 \cakadomo 7$
- $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$


Ku mibare yose itatu iri hejuru, kubara ibiharuro vyayo vy’intango biroroshe cane, naho woba wahawe $N$ gusa. Utangura n’umubare mutoyi cane w’intango, ni ukuvuga 2, maze ukabona incuro umubare wose $N$ ugabanywa na wo. Uca uja kugerageza ukuntu $N$ igabanywa na 3, 5, 7, n’ibindi. Ubandanya iyo nzira gushika umubare wawe wose $N$ wanditswe nk'igisubizo c'imibare y'intango gusa.


Fata nk’akarorero umubare wose 84. Aha hepfo urashobora kubona ingene umenya ibice vyawo vy’intango. Ku ntambwe yose, dukuraho umubare w’intango mutoyi cane usigaye (ibubamfu) maze tugaca tumenya ijambo ry’intango risigaye rizofatwa. Turabandanya gushika ijambo risigaye na ryo nyene ari umubare w’intango. Ku ntambwe yose, igiharuro c’ubu ca 84 kigaragazwa iburyo cane.



- Igiharuro ca mbere = 2: ijambo ry'amasigarira = 42 ($84 = 2 \cdot 42$)
- Umubare w'intango = 2: ijambo ry'amasigarira = 21 ($84 = 2 \cakarongo 2 \cakarongo 21$)
- Umubare w'intango = 3: ijambo ry'amasigarira = 7 ($84 = 2 \cakarongo 2 \cakarongo 3 \cakarongo 7$)
- Kubera ko 7 ari umubare w'intango, igisubizo ni $2 \cdot 2 \cdot 3 \cdot 7$, canke $2^2 \cdot 3 \cdot 7$.


Twibaze ubu ko $N$ ari nini cane. None vyoba bigoye gute kugabanya $N$ mu bice vyayo vy’intango?


Ivyo vy’ukuri bivana na $N$. Twibaze nk'akarorero, iyo $N$ ari 50.450.400. Naho uwo mubare usa n’uwuteye ubwoba, ivyo biharuro ntibigoye gutyo kandi birashobora gukorwa n’amaboko bitagoranye. Nk’uko vyavuzwe haruguru, utangura gusa na 2 ugakora inzira yawe uja imbere. Aha hepfo, urashobora kubona ivyavuye muri iyo nzira mu buryo busa n’ubwo twavuze haruguru.



- 2: 25.225.200 (amadolari 50.450.400 = 2 \cdot 25.225.200$)
- 2: 12.612.600 (amadolari 50.450.400 = 2^2 \cdot 12.612.600$)
- 2: 6.306.300 (amadolari 50.450.400 = 2^3 \cdot 6.306.300$)
- 2: 3.153.150 (amadolari 50.450.400 = 2^4 \cdot 3.153.150$)
- 2: 1.576.575 (amadolari 50.450.400 = 2^5 \cdot 1.576.575$)
- 3: 525.525 (amadolari 50.450.400 = 2^5 \cdot 3 \cdot 525.525$)
- 3: 175.175 (amadolari 50.450.400 = 2^5 \cdoti 3^2 \cdoni 175.175$)
- 5: 35.035 (amadolari 50.450.400 = 2^5 \cdoti 3^2 \cdoti 5 \cdoti 35.035$)
- 5: 7.007 (amadolari 50.450.400 = 2^5 \cdoti 3^2 \cdoti 5^2 \cdoti 7.007$)
- 7: 1.001 (amadolari 50.450.400 = 2^5 \cdoti 3^2 \cdoti 5^2 \cdoti 7 \cdoti 1.001$)
- 7: 143 (amadolari 50.450.400 = 2^5 \cdoti 3^2 \cdoti 5^2 \cdoni 7^2 \cdoti 143$)
- 11: 13 (amadolari 50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
- Kubera ko 13 ari umubare w'intango, igisubizo ni $2^5 \cdoti 3^2 \cdoti 5^2 \cdoti 7^2 \cdoti 11 \cdoti 13$.


Gutorera umuti iyo ngorane n’amaboko birafata umwanya. Birumvikana ko orodinateri yoshobora gukora ivyo vyose mu gace gatoyi k’isegonda. Nkako, orodinateri irashobora mbere kenshi gucapura imibare myinshi cane mu gace k’isegonda.


Ariko rero, hariho ibintu bimwebimwe bidasanzwe. Twibaze ko tubanje guhitamwo mu buryo bw’impfagusa imibare ibiri nini cane y’intango. Ni ibisanzwe gushiramwo amazina kuri izo $p$ na $q$, kandi nzokwemera iyo nzira hano.


Kugira ngo tubone neza, reka tuvuge ko $p$ na $q$ zompi ari ibiharuro vy’intango vy’ibice 1024, kandi ko vy’ukuri bisaba nibura ibice 1024 kugira ngo bishobore guserurwa (rero ibice vya mbere bitegerezwa kuba 1). Rero, nk’akarorero, 37 ntishobora kuba imwe mu mibare y’intango. Ushobora vy’ukuri guserukira 37 n’ibice 1024. Ariko biragaragara ko *udakeneye* ivyo bice vyinshi kugira ngo ubiserukire. Ushobora guserukira 37 n'urudodo urwo ari rwo rwose rufise ibice 6 canke birenze. (Mu bice 6, 37 vyogereranywa n’amadolari 100101$).


Ni ngombwa gutahura ingene $p$ na $q$ ari binini iyo bitowe hakurikijwe ivyo bivugwa haruguru. Nk’akarorero, nahisemwo umubare w’intango ukeneye nibura ibice 1024 kugira ngo ugaragazwe aha hepfo.



- 14.752.173.874.503.595.484.930.006.383.670.759.559.764.562.721.397.166.747.289.220.945.457.9372. ,048.198.854.920.097.085.690.793.755.254.946.188.163.753.506.778.089.706.699.671.722.089.715.604. 9.594.106.189.662.669.156.149.028.900.805.928.183.585.427.782.974.951.355.515.394.807.209.8386,47. 558.332.897.443.152.653.214.483.870.992.618.171.825.921.582.253.023.974.514.209.142.520.026.808.


Twibaze ubu tumaze guhitamwo mu buryo bw’impfagusa imibare y’intango $p$ na $q$, tuyigwiza kugira ngo turonke umubare wose $N$. Iyi integer ya nyuma rero, ni umubare w'ibice 2048 usaba nibura ibice 2048 kugira ngo ugaragazwe. Ni kinini cane, kinini cane kuruta $p$ canke $q$.


Twibaze ko uha mudasobwa $N$ gusa, ukayisaba kurondera ibice bibiri vy’intango vy’ibice 1024 vya $N$. Ivyo mudasobwa ishobora kubona $p$ na $q$ ni bike cane. Ushobora kuvuga ko bidashoboka ku ntumbero zose zikora. Ivyo ni ko biri, naho woba ukoresha orodinateri nini cane canke mbere n’uruja n’uruza rw’urudandazwa rwinshi cane.


Kugira ngo dutangure, dufate ko mudasobwa igerageza gutorera umuti ingorane mu guca mu mibare 1024 y’ibice, igerageza muri buri gihe nimba ari imibare y’intango be n’uko ari imibare y’ibice $N$. Igitigiri c'imibare y'intango izogeragezwa rero ni nk'amadolari 1.265 \cdot 10^{305}$. [2]


Naho wofata mudasobwa zose zo kuri iyi si ukazigerageza kurondera no kugerageza imibare y’intango y’ibice 1024 muri ubwo buryo, amahirwe 1 muri miliyaridi yo kuronka neza umubare w’intango w’amadolari N$ vyosaba igihe kirekire cane co kubara kuruta imyaka Isanzure ry’ikirere rifise.


Ubu mu bikorwa, orodinateri irashobora gukora neza kuruta uburyo buteye isoni twahejeje kudondora. Hariho ubuhinga bwinshi mudasobwa ishobora gukoresha kugira ngo ize ku bijanye n’ugucapura vyihuse. Ariko rero, ikintu nyamukuru ni uko naho umuntu yokoresha izo nzira zikora neza cane, igikorwa ca orodinateri kiracari kidashoboka. [3]


Igihambaye ni uko ingorane yo gucapura mu bihe twahejeje kudondora ishingiye ku ciyumviro c’uko ata buhinga bwo kubara ibiharuro vy’intango bukora neza. Ntidushobora mu vy’ukuri kwemeza ko ata algorithme ikora neza iriho. Naho ari ukwo, ivyo vyiyumviro birashoboka cane: naho hari utwigoro twinshi twagizwe mu myaka amajana, ntituraronka ubuhinga nk’ubwo bwo gukoresha ubuhinga bwo guharura.


Ku bw’ivyo, ingorane y’ugucapura, mu bihe bimwebimwe, irashobora kwiyumvirwa ko ari ingorane ya Hard. Mu buryo bwihariye, iyo $p$ na $q$ ari imibare y’intango nini cane, igicuruzwa cabo $N$ ntikigoye kubara; ariko gucapura gusa guhabwa $N$ ntaco bimaze.



**Ivyiyumviro:**


[1] Gucapura birashobora kandi kuba bihambaye mu gukorana n’ubundi bwoko bw’ibintu vy’imibare atari imibare. Nk'akarorero, birashobora kuba vyiza guharura invugo z'inyuguti nyinshi nka $x^2 - 2x + 1$. Mu kiganiro cacu, tuzokwibanda gusa ku gucapura imibare, cane cane imibare yose.


[2] Dushingiye ku **itegeko ry’imibare y’intango**, umubare w’imibare y’intango uri munsi canke ungana na $N$ ni nk’$N/\LN(N)$. Ibi bisigura ko ushobora kwegeranya umubare w'ibiharuro vy'uburebure 1024 bits na:


$$ \frac{2^{1024}}{\LN(2^{1024})}


...bingana n'amadolari 1.265 \incuro 10^{305}$.


[3] Ni ko biri no ku bibazo vy’ubuhinga bwa logarithme butandukanye. Ni co gituma inyubakwa zidahuye zikorana n’imfunguruzo nini cane kuruta inyubakwa zidahuye zikorana n’imfunguruzo.




## Ibisubizo vy'imibare

<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>


Ikibabaje, ingorane y’ugukorana n’ibindi ntishobora gukoreshwa ataco ihinduye ku migambi y’ubuhinga bwo gukora amakuru y’ibanga. Ariko rero, turashobora gukoresha ingorane ikomeye cane ariko ifitaniye isano n’ivyo: ingorane ya RSA.


Kugira ngo dutahure ingorane ya RSA, tuzokenera gutahura umubare w’ibiharuro n’ivyifuzo biva ku vyiyumviro vy’imibare. Ivyo birerekanwa muri iki gice mu bice bitatu: (1) urutonde rwa N, (2) modulo N y’uguhinduka, na (3) igiharuro ca Euler.


Bimwe mu bintu biri muri ivyo bice bitatu vyaramaze gushirwa mu *Gice ca 3*. Ariko aha nzosubiramwo ivyo bintu kugira ngo bibe vyiza.



### Urutonde rwa N .


Umubare wose $a$ ni **coprime** canke **umubare w'intangamarara** ufise umubare w'intangamarara $N$, iyo umugabane munini rusangi hagati yavyo ari 1. Naho 1 ku buryo busanzwe atari umubare w'intangamarara, ni coprime y'umubare wose w'intangamarara (nk'uko biri $-1$).


Nk’akarorero, rimbura igihe $a = 18$ na $N = 37$. Ivyo biragaragara ko ari ama coprimes. Umubare munini cane ugabanya 18 na 37 ni 1. Mu buryo butandukanye n’ubwo, rimbura igihe $a = 42$ na $N = 16$. Ivyo biragaragara ko atari coprimes. Iyo mibare yompi igabanywa na 2, ari yo isumba 1.


Ubu turashobora gusobanura urutonde rwa $N$ nk’uko bikurikira. Twibaze ko $N$ ari umubare wose uruta 1. **urutonde rwa N** ni, rero, umubare w'ibifatanya vyose bifise $N$ ku buryo ku bifatanya vyose $a$, iki gikurikira kibaho: $1 \leq a < N$.


Nk’akarorero, nimba $N = 12$, rero 1, 5, 7, na 11 ni zo zonyene zihuye n’ivyo bisabwa haruguru. Rero, urutonde rwa 12 rungana na 4.


Twibaze ko $N$ ari umubare w’intango. Hanyuma umubare wose muto kuruta $N$ ariko munini canke ungana na 1 ni coprime nawo. Ivyo birimwo Elements zose ziri mu rutonde rukurikira: $\{1,2,3,....,N - 1\}$. Ni co gituma iyo $N$ ari umubare w’imbere, urutonde rwa $N$ ni $N - 1$. Ivyo bivugwa mu ciyumviro ca 1, aho $\phi(N)$ yerekana urutonde rwa $N$.


**Iciyumviro ca 1**. $\phi(N) = N - 1$ iyo $N$ ari umubare w'imbere


Twibaze ko $N$ atari prime. Ushobora rero kubara urutonde rwayo ukoresheje **igikorwa ca Euler’s Phi**. Naho kubara urutonde rw’umubare mutoyi w’intege bitoroshe, igikorwa ca Euler’s Phi kiraba gihambaye cane ku mibare minini y’intege yose. Iciyumviro c’igikorwa ca Euler’s Phi kivugwa aha hepfo.


**Iciyumviro ca 2**. Reka $N$ ingane na $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, aho umugwi $\{p_i wa $}$ ugizwe n'umubare $\{p_i wa\}$ $e_i$ yerekana incuro umubare w'intango $p_i$ uba kuri $N$. None,


$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot ($1)


**Iciyumviro ca 2** kirerekana ko iyo umaze gucapura $N$ iyo ari yo yose itari iya mbere mu bice vyayo vy’intango bitandukanye, biroroshe kubara urutonde rwa $N$.


Nk’akarorero, dufate ko $N = 270$. Biragaragara ko ivyo atari umubare w’intango. Gucapura $N$ mu bice vyayo vy'intango bitanga imvugo: $2 \cdot 3^3 \cdot 5$. Dushingiye ku gikorwa ca Euler’s Phi, urutonde rwa $N$ rero ni uru:


$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 =$1 \1


Twibaze ko $N$ ari umusaruro w’ibiharuro bibiri vy’intango, $p$ na $q$. **Iciyumviro ca 2** kiri hejuru rero, kivuga ko urutonde rwa $N$ ari uru:


$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$


Ivyo ni igisubizo nyamukuru ku kibazo ca RSA cane cane, kandi kivugwa mu **Iciyumviro ca 2** kiri aha hepfo.


**Iciyumviro ca 2**. Nimba $N$ ari umusaruro w'ibiharuro bibiri vy'intango, $p$ na $q$, urutonde rwa $N$ ni umusaruro $(p - 1) \cdot (q - 1)$.


Kugira ngo tubone ingero, dufate ko $N = 119$. Uwo mubare wose ushobora guca mu biharuro bibiri vy’intango, ni ukuvuga 7 na 17. Ku bw’ivyo, igikorwa ca Euler’s Phi kivuga ko urutonde rwa 119 ari uru:


119 = (7 - 1) = 6 16 = 96


Mu yandi majambo, umubare wose 119 ufise 96 coprimes kuva kuri 1 gushika kuri 119. Mu vy'ukuri, uru rutonde rurimwo imibare yose kuva kuri 1 gushika kuri 119, atari incuro za 7 canke 17.


Kuva hano, reka tugaragaze umugwi w’ibiharuro bigena urutonde rwa $N$ nka $C_N$. Ku karorero kacu aho $N = 119$, umugwi $C_{119}$ ni munini cane ku buryo udashobora gushirwa ku rutonde rwose. Ariko bimwe muri Elements ni ibi bikurikira:


$$C_{119} = \{1, 2, \utudomo 6, 8 \utudomo 13, 15, 16, 18, \utudomo 33, 35 \utudomo 96\}$$


### Uguhinduka modulo N


Turashobora kuvuga ko umubare wose $a$ ari **umubare N** uhinduka, iyo hariho n'imiburiburi umubare wose $b$ ku buryo $a \cdot b \mod N = 1 \mod N$. Umubare wose nk'uwo $b$ witwa **inverse** (canke **inverse y'ugukubita**) ya $a$ igabanywa na modulo $N$.


Twibaze nk’akarorero ko $a = 5$ na $N = 11$. Hariho imibare myinshi yuzuye ushobora gukubita 5, kugira ngo $5 \cdot b \mod 11 = 1 \mod 11$. Rimbura, nk'akarorero, imibare 20 na 31. Biroroshe kubona ko iyo mibare yose ari inverses ya 5 ku kugabanya modulo 11.



- $5 \cdot 20 \umuhinduzi 11 = 100 \umuhinduzi 11 = 1 \umuhinduzi 11$
- $5 \cdot 31 \umuhinduzi 11 = 155 \umuhinduzi 11 = 1 \umuhinduzi 11$


Naho 5 ifise inverse nyinshi zigabanya modulo 11, urashobora kwerekana ko inverse imwe gusa nziza ya 5 iriho iri munsi ya 11. Mu vy’ukuri, ivyo si vyo vyonyene ku karorero kacu bwihariye, ariko ni igisubizo rusangi.


**Iciyumviro ca 3**. Niba umubare wose $a$ ari modulo $N$ ihinduka, bitegerezwa kuba ari uko nyene umubare umwe w'inhindurwa nziza wa $a$ ari muto kuri $N$. (Rero, iyo mpinduka yihariye ya $a$ itegerezwa kuva ku mugwi $\{1, \utudomo, N - 1\}$).


Reka tugaragaze inverse yihariye ya $a$ iva kuri **Iciyumviro 3** nk' $a^{-1}$. Ku bijanye n’igihe $a = 5$ na $N = 11$, ushobora kubona ko $a^{-1} = 9$, uhereye ku kuba $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.


Urabona ko ushobora kandi kuronka agaciro 9 ka $a^{-1}$ mu karorero kacu mu kugabanya gusa uwundi muvuduko wose wa $a$ na modulo 11. Nk'akarorero, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Rero igihe cose umubare wose $a > N$ ari modulo $N$ ihinduka, rero $a \mod N$ na yo itegerezwa kuba modulo $N$ ihinduka.


Si ngombwa ko inverse ya $a$ ibaho reduction modulo $N$. Twibaze nk’akarorero ko $a = 2$ na $N = 8$. Nta $b$, canke $a^{-1}$ iyo ari yo yose, ku buryo $2 \cdot b \mod 8 = 1 \mod 8$. Ibi ni kubera ko agaciro kose ka $b$ kazokwama gatanga umubare wa 2, rero nta kugabanya na 8 gushobora gutanga igisigaye kingana na 1.


Ni gute nyabuna tumenya ko umubare umwe wose $a$ ufise inverse y’umubare $N$ watanzwe? Nk’uko mushobora kuba mwabibonye mu karorero kari hejuru, umugabane munini cane hagati ya 2 na 8 ni uwurengeye 1, ni ukuvuga 2. Kandi ivyo mu vy’ukuri ni ikigereranyo c’igisubizo rusangi gikurikira:


**Iciyumviro ca 4**. Inverse iriho y'umubare wose $a$ uhawe modulo y'ugugabanya $N$, kandi cane cane inverse nziza yihariye iri munsi ya $N$, iyo kandi gusa iyo umugabane munini hagati ya $a$ na $N$ ari 1 (ni ukuvuga, iyo ari coprimes).


Ku bijanye n’igihe $a = 5$ na $N = 11$, twaciye dufata ingingo y’uko $a^{-1} = 9$, kubera ko $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Ni vyiza kumenya ko ivyo bihushanye n’ivyo na vyo nyene ari ukuri. Ni ukuvuga ko iyo $a = 9$ na $N = 11$, ni uko $a^{-1} = 5$.



### Iciyumviro ca Euler


Imbere yo kuja ku kibazo ca RSA, turakeneye gutahura ikindi ciyumviro kimwe gihambaye cane, ari co **Iciyumviro ca Euler**. Ivuga ibi bikurikira:


**Iciyumviro ca 3**. Twibaze ko imibare ibiri yuzuye $a$ na $N$ ari coprimes. Hanyuma, $a^{\phi(N)} \mod N = 1 \mod N$.


Ivyo ni ingaruka zitangaje, ariko mu ntango biratera urujijo gatoyi. Reka duhindukire tuje ku karorero kugira ngo tubitahure.


Twibaze ko $a = 5$ na $N = 7$. Ivyo ni coprimes vy’ukuri nk’uko theorem ya Euler isaba. Turazi ko urutonde rwa 7 rungana na 6, kubera ko 7 ari umubare w’intango (raba **Iciyumviro 1**).


Ico igiharuro ca Euler kivuga ubu ni uko $5^6 \mod 7$ itegerezwa kuba ingana na $1 \mod 7$. Aha hepfo hariho imibare yerekana ko ivyo ari ukuri vy’ukuri.



- $5^6 \uburyo 7 = 15.625 \uburyo 7 = 1 \uburyo N$


Umubare wose 7 ugabanywamwo 15.624 vyose hamwe bikaba ari incuro 2.233. Rero, igisigaye co kugabanya 16.625 na 7 ni 1.


Igikurikira, ukoresheje igikorwa ca Euler’s Phi, **Iciyumviro ca 2**, urashobora gukuramwo **Iciyumviro ca 5** kiri aha hepfo.


**Iciyumviro ca 5**. $\phi(a \cdot b) = \phi(a) \cdot \cdot \phi(b)$ ku mibare yose nziza $a$ na $b$.


Ntituzokwerekana igituma ari ukwo biri. Ariko gusa menya ko umaze kubona ibimenyamenya vy'ico ciyumviro kubera ko $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ igihe $p$ na $q$ ari ibiharuro vy'intango, nk'uko bivugwa muri **Iciyumviro 2**.


Iciyumviro ca Euler gifatanijwe n’**Iciyumviro ca 5** gifise insiguro zihambaye. Raba ibiba, nk'akarorero, mu mvugo zikurikira, aho $a$ na $N$ ari coprimes.



- $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
- $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
- $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$


Ni co gituma, gufatanya ivyiyumviro vya Euler n’ivyo **Iciyumviro ca 5** bituma dushobora gusa kubara umubare w’imvugo. Muri rusangi, turashobora gucapura mu ncamake ubumenyi nk'uko biri mu **Iciyumviro ca 6**.


**Iciyumviro ca 6**. $a^x \uburyo N = a^{x \uburyo \phi(N)}$


None rero dutegerezwa gushiramwo vyose mu ntambwe ya nyuma y’uruyeri.


Nk'uko $N$ ifise urutonde $\phi(N)$ rurimwo Elements y'umugwi $C_N$, turazi ko umubare wose $\phi(N)$ nawo utegerezwa kuba ufise urutonde n'umugwi w'ibiharuro. Reka dushireho $\phi(N) = R$. Hanyuma turamenya ko hariho kandi agaciro ka $\phi(R)$ n'umugwi w'ibifatanya $C_R$.


Twibaze ko ubu duhisemwo umubare wose $e$ mu mugwi $C_R$. Turazi bivuye ku **Iciyumviro ca 3** ko uwo mubare wose $e$ ufise gusa inverse imwe yihariye y’insobanuro nziza iri munsi ya $R$. Ni ukuvuga, $e$ ifise inverse imwe yihariye iva ku mugwi $C_R$. Reka tuvyite inverse $d$. Hakurikijwe insobanuro y’igihinduka, ivyo bisigura ko $e \cdot d = 1 \mod R$.


Turashobora gukoresha iki gisubizo kugira ngo dukore imvugo yerekeye umubare wacu w'umwimerere $N$. Ivyo bivugwa mu ncamake mu **Iciyumviro ca 7**.


**Iciyumviro ca 7**. Twibaze ko $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Hanyuma ku kintu cose $a$ c'umugwi $C_N$ bitegerezwa kuba ari uko $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.


Ubu turafise ibisubizo vyose vy’imibare bikenewe kugira ngo tuvuge neza ingorane ya RSA.



## Ubuhinga bwa RSA

<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>


Ubu turiteguye kuvuga ingorane ya RSA. Twibaze ko urema umugwi w’ibihinduka birimwo $p$, $q$, $N$, $\phi(N)$, $e$, $d$, na $y$. Hamagara iyi nkuru $\Pi$. Iremwa gutya:


1. generate ibiharuro bibiri vy’intango $p$ na $q$ vy’ubunini bungana maze ubare umusaruro wavyo $N$.

2. Harura urutonde rwa $N$, $\phi(N)$, n’igisubizo gikurikira: $(p - 1) \cdot (q - 1)$.

3. Hitamwo $e > 2$ kugira ngo ibe nto kandi ihurire na $\phi(N)$.

4. Harura $d$ ukoresheje $e \cdot d \mod \phi(N) = 1$.

5. Hitamwo agaciro k’imburakimazi $y$ ari gatoyi kandi koprime na $N$.


Ikibazo ca RSA gishingiye ku kurondera $x$ ku buryo $x^e = y$, mu gihe gusa umuntu atanga amakuru yerekeye $\Pi$, ni ukuvuga ibihinduka $N$, $e$, na $y$. Iyo $p$ na $q$ ari binini cane, kenshi na kenshi ni vyiza ko bifise ubunini bw'ibice 1024, ingorane ya RSA yiyumviriwe ko ari Hard. Urashobora kubona ubu igituma ari ukwo biri uhereye ku kiganiro twamaze kuvuga.


Uburyo bworoshe bwo kubara $x$ igihe $x^e \mod N = y \mod N$ ni uguharura gusa $y^d \mod N$. Turazi $y^d \mod N = x \mod N$ biciye ku biharuro bikurikira:


$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$


Ikibazo ni uko tutazi agaciro ka $d$, kuko katatanzwe mu kibazo. Ni co gituma tutashobora guharura ata guca ku ruhande $y^d \mod N$ kugira ngo turonke $x \mod N$.


Ariko rero, twoshobora guharura mu buryo butaziguye $d$ dufatiye ku rutonde rwa $N$, $\phi(N)$, nk’uko tuzi ko $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Ariko mu kwiyumvira ingorane na yo nyene ntitanga agaciro ka $\phi(N)$.


Ubwa nyuma, urutonde rwoshobora kubarwa mu buryo butaziguye hakoreshejwe ibiharuro vy’intango $p$ na $q$, kugira ngo amaherezo dushobore kubara $d$. Ariko mu vyiyumviro, agaciro ka $p$ na $q$ na ko nyene ntitwaduhawe.


Mu kuvuga ataco twirengagije, naho ingorane yo gukora mu kibazo ca RSA yoba ari Hard, ntidushobora kwemeza ko ingorane ya RSA na yo ari Hard. Hariho n’ubundi buryo bwo gutorera umuti ingorane ya RSA atari ugukoresha ubuhinga bwa factoring. Ariko rero, muri rusangi vyemerwa kandi vyiyumvirwa ko iyo ingorane y'ugushiramwo ibintu mu ngorane ya RSA ari Hard, iyo ngorane ya RSA ubwayo na yo nyene ni Hard.


Nimba ingorane ya RSA ari Hard vy’ukuri, rero itanga igikorwa c’inzira imwe gifise urugi rw’umutego. Ivyo bikorwa aha ni $f(g) = g^e \mod N$. Umuntu wese afise ubumenyi bwa $f(g)$, yoshobora kubara mu buryo bworoshe agaciro $y$ ku $g = x$ kanaka. Ariko rero, biragoye cane kubara agaciro kanaka $x$ gusa mu kumenya agaciro $y$ n’igikorwa $f(g)$. Ivyo bidasanzwe ni iyo uhawe amakuru $d$, urugi rw’umutego. Muri ivyo, ushobora gusa kubara $y^d$ kugira ngo ushireho $x$.


Reka tugende mu karorero kadasanzwe kugira ngo tubone ingorane ya RSA. Sinshobora guhitamwo ingorane ya RSA yofatwa ko ari Hard mu gihe c’ivyo bivugwa haruguru, kuko imibare yoba idashobora gukoreshwa. Ahubwo, aka karorero ni ugushira ahabona gusa ingene ingorane ya RSA ikora muri rusangi.


Kugira ngo utangure, dufate ko uhisemwo imibare ibiri y’intango 13 na 31. Rero $p = 13$ na $q = 31$. Igiharuro $N$ c’izo nkuru zibiri z’intango kingana na 403. Turashobora kubara bitagoranye urutonde rwa 403. Kingana na $(13 - 1) \cdot (31 - 1) = 360$.


Igikurikira, nk’uko bitegekanijwe n’intambwe ya 3 y’ingorane ya RSA, turakeneye guhitamwo coprime ya 360 iruta 2 kandi iri munsi ya 360. Ntidutegerezwa guhitamwo ako gaciro mu buryo bw’impfagusa. Twibaze ko duhisemwo 103. Iyi ni coprime ya 360 nk'uko umugabane wayo munini rusangi na 103 ari 1.


Intambwe ya 4 ubu isaba ko tubara agaciro $d$ ku buryo $103 \cdot d \mod 360 = 1$. Ivyo si igikorwa coroshe n'amaboko iyo agaciro ka $N$ ari kanini. Bisaba ko dukoresha uburyo bwitwa **ubuhinga bwa Euclide bwagutse**.


Naho ntagaragaza uburyo bwo kubikora hano, bitanga agaciro ka 7 iyo $e = 103$. Ushobora kugenzura ko umugwi w'agaciro 103 na 7 vy'ukuri uhuye n'ivyangombwa rusangi $e \cdot d \mod \phi(n) = 1$ biciye mu biharuro biri aha hepfo.



- $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$


Igihambaye, duhawe *Iciyumviro ca 4*, turazi ko ata wundi mubare wose uri hagati ya 1 na 360 ku $d$ uzotanga igisubizo c'uko $103 \cdot d = 1 \mod 360$. Ikindi, iciyumviro kivuga ko guhitamwo agaciro gatandukanye ka $e$, bizovamwo agaciro kadasanzwe gatandukanye ka $d$.


Mu ntambwe ya 5 y'ikibazo ca RSA, dutegerezwa guhitamwo umubare wose mwiza $y$ ariwo coprime ntoyi ya 403. Dufate ko dushizeho $y = 2^{103}$. Guteranya 2 na 103 bitanga igisubizo kiri aha hepfo.



- $2^{103} \mod 403 = 10.141.204.801.825.835.211.973.625.643.008 \mod 403 = 349 \mod 403$


Ikibazo ca RSA muri aka karorero ubu ni aka: Uhabwa $N = 403$, $e = 103$, na $y = 349 \mod 403$. Ubu rero ubwirizwa kubara $x$ ku buryo $x^{103} = 349 \mod 403$. Ni ukuvuga, utegerezwa gusanga agaciro k'intango imbere yo gutera imbere na 103 kari 2.


Vyoba vyoroshe (ku mudasobwa n’imiburiburi) kubara $x$ iyo tumenya ko $d = 7$. Muri ivyo, woshobora gusa kumenya $x$ nk'uko biri aha hepfo.



- $x = y^7 \mod 403 = 349^7 \mod 403 = 630.634.881.591.804.949 \mod 403 = 2 \mod 403$


Ikibazo ni uko utaronse amakuru ko $d = 7$. Ushobora, birumvikana, kubara $d$ uhereye ku kuba $103 \cdot d = 1 \mod 360$. Ikibazo ni uko nawe nyene utahabwa amakuru ko urutonde rwa $N = 360$. Ubwa nyuma, woshobora kandi kubara urutonde rwa 403 mu kubara igicuruzwa gikurikira: $(p - 1) \cdot (q - 1)$. Ariko kandi ntubwirwa ko $p = 13$ na $q = 31$.


Ego ni ko, orodinateri yoshobora gutorera umuti ingorane ya RSA y’aka karorero mu buryo bworoshe cane, kubera ko imibare y’intango irimwo si myinshi. Ariko iyo imibare y’intango ibaye nini cane, ihura n’igikorwa hafi kidashoboka.


Ubu twashize ahabona ingorane ya RSA, urutonde rw’ibintu bishobora gutuma iba Hard, n’imibare iri inyuma. Ni gute ivyo vyose bifasha mu bijanye n’ubuhinga bwo gukingira amakuru ataco buvuze? Mu buryo bwihariye, twohindura gute ubukomezi bw’ingorane ya RSA mu bihe bimwebimwe bukaba umugambi wo gupfuka canke umugambi wo gusinya mu buryo bwa digitale?


Uburyo bumwe ni ugufata ingorane ya RSA tukagira imigambi mu buryo bugororotse. Nk'akarorero, dufate ko washizeho umugwi w'ibihinduka $\Pi$ nk'uko vyavuzwe mu kibazo ca RSA, maze ubone ko $p$ na $q$ ari binini bihagije. Ushiraho urufunguzo rwawe rwa bose rungana na $(N, e)$ maze ugasangira aya makuru n'isi yose. Nk'uko vyavuzwe haruguru, ugumya ibanga ry'agaciro ka $p$, $q$, $\phi(n)$, na $d$. Nkako, $d$ ni urufunguzo rwawe rw’ibanga.


Umuntu wese ashaka kukurungikira ubutumwa $m$ ari co kintu ca $C_N$ yoshobora gusa kubupfuka gutya: $c = m^e \mod N$. (Inyandiko y'ibanga $c$ hano ingana n'agaciro $y$ mu kibazo ca RSA.) Ushobora gusobanura ubu butumwa mu buryo bworoshe mu kubara gusa $c^d \mod N$.


Ushobora kugerageza gukora umugambi w’umukono w’ibarabara mu buryo nk’ubwo nyene. Twibaze ko ushaka kohereza umuntu ubutumwa $m$ bufise umukono wa digitale $S$. Ushobora gusa gushinga $S = m^d \mod N$ maze ukarungika umugwi $(m,S)$ ku wuwuronka. Umuntu wese ashobora kugenzura umukono wa digitale gusa mu kugenzura nimba $S^e \mod N = m \mod N$. Ariko rero, uwutera wese yogira igihe kigoye vy’ukuri co kurema $S$ ibereye ku butumwa, kubera ko badafise $d$.


Ikibabaje, guhindura ikibazo ca Hard, ikibazo ca RSA, mu mugambi w’ubuhinga bwo gukingira amakuru si ivyo bigororotse. Ku bijanye n'umugambi w'ugushiramwo amakuru, ushobora guhitamwo gusa coprimes za $N$ nk'ubutumwa bwawe. Ivyo ntibidusiga ubutumwa bwinshi bushoboka, ata gukeka ko butahagije kugira ngo umuntu ashobore kuvugana n’abandi mu buryo busanzwe. Ikindi, ubwo butumwa butegerezwa gutorwa mu buryo bw’impfagusa. Ivyo bisa n’ibidashoboka. Ubwa nyuma, ubutumwa bwose butowe incuro zibiri buzotanga inyandiko imwe nyene y’ibanga. Ivyo ntivyipfuzwa cane mu mugambi uwo ari wo wose wo gupfuka kandi ntibihuye n’iciyumviro gikomeye c’ubuhinga bwa none c’umutekano mu gupfuka.


Ibibazo birarushiriza kuba bibi ku mugambi wacu w’umukono w’ibarabara ugororotse. Nk’uko bimeze, uwutera uwo ari we wese arashobora guhingura amasinyatire y’ivyuma mu buryo bworoshe mu guhitamwo gusa coprime ya $N$ nk’amasinyatire hanyuma agaharura ubutumwa bw’intango buhuye. Ivyo bica bica ku rugero rutomoye igisabwa c’ukudashobora kubaho.


Naho biri ukwo, mu kwongerako ubukerebutsi bukeyi, ingorane ya RSA irashobora gukoreshwa mu guhingura umugambi wo gukingira urufunguzo rwa bose hamwe n’umugambi wo gushirako umukono w’ibarabara. Ntituzokwinjira mu ndondoro y’izo nyubakwa ngaha. [4] Ariko ikintu gihambaye ni uko iyo nzira y’ugusobanuka y’inyongera idahindura ingorane nyamukuru y’ishimikiro ya RSA iyo migambi ishingiyeko.



**Ivyiyumviro:**


[4] Raba nk’akarorero, Jonathan Katz na Yehuda Lindell, _Intango y’Ivy’Ugushiramwo Amakuru y’Igihugu_, Ikinyamakuru CRC (Boca Raton, FL: 2015), urupapuro rwa 410–32 ku bijanye n’ugushiramwo amakuru y’uruzitiro rwa RSA n’urupapuro rwa 444–41 ku bijanye n’imikono ya RSA.




# Igice ca nyuma

<partId>e538fb79-bf28-40cd-a5c3-badf864d8567</partId>


## Amasuzuma n'Ibipimo

<chapterId>366d6fd0-ceb2-4299-bf37-8c6dfcb681d5</chapterId>

<isCourseReview>true</isCourseReview>

## Ikizame canyuma

<chapterId>44882d2b-63cd-4fde-8485-f76f14d8b2fe</chapterId>

<isCourseExam>true</isCourseExam>

## Iciyumviro

<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>

<isCourseConclusion>true</isCourseConclusion>