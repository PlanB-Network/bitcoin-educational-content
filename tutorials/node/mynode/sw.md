---
name: Nodi yangu
description: Sanidi Bitcoin MyNode yako
---

![image](assets/0.webp)


[Njia Yangu](https://mynodebtc.com/) ndiyo njia rahisi na yenye nguvu zaidi ya kutumia Bitcoin na nodi ya Umeme! Tunachanganya programu bora zaidi ya programu huria na Interface, usimamizi, na usaidizi ili uweze kutumia Bitcoin na Umeme kwa urahisi, kwa faragha na kwa usalama.


## Aina za usanidi wa Node


Kuna usanidi anuwai wa Node. MyNode ni bora. Kuna programu nyingi zinazokuja nayo, na hata zaidi ikiwa unalipia toleo la malipo. Vinginevyo ni kuchosha sana kupakua programu hizo mwenyewe. MyNode hurahisisha sana kama utakavyoona.


Chaguo mbadala na sawa ni RaspiBlitz. GUI sio nzuri, na programu zinaingiliana sana na programu zinazokuja na MyNode, lakini Raspiblitz ni programu ya bure ya chanzo (FOSS) na MyNode sio kabisa. Tofauti nyingine ni kwamba MyNode inaendeshwa kwenye chombo cha Docker. Ninaona Docker inatisha na Hard kutatua shida. Hili ni shida tu ikiwa utakutana na makosa au mende. Msanidi programu hutoa usaidizi kwa watumiaji wa malipo ya kwanza na kuna kikundi cha gumzo cha Telegraph pia.


RaspiBlitz ni programu nyingi tu zilizosanikishwa kwenye Linux, bila Docker. Kiendeshi cha nje cha Hard kinaweza kuunganishwa kwa urahisi kwenye mashine nyingine ya Linux iliyo na Bitcoin Core, na ukienda, ukihitaji.


Chaguo jingine ni kufunga tu Bitcoin Core na aina ya Electrum Server (kuna kadhaa) kwenye mfumo wa uendeshaji. Nina miongozo ya Linux (Raspberry Pi), Mac, na Windows.


## Orodha ya ununuzi



- Raspberry Pi 4, kumbukumbu ya 4Gb au 8Gb (4Gb ni nyingi)
- Raspberry Pi Power (Muhimu Sana! Usichukue generic, umakini)
- Kesi kwa Pi. Kesi ya FLIRC ni nzuri. Kesi nzima ni kuzama kwa joto na hauitaji shabiki, ambayo inaweza kuwa na kelele
- 16 Gb microSD kadi (unahitaji moja, lakini chache ni muhimu)
- Msomaji wa kadi ya kumbukumbu (kompyuta nyingi hazitakuwa na slot kwa kadi ya microSD).
- Hifadhi ya nje ya SSD 1Tb Hard.

Kumbuka: SSD ni muhimu. usitumie kiendeshi cha nje cha Hard hata kama ni nafuu


- Kebo ya ethaneti (ili kuunganisha kwenye kipanga njia chako cha nyumbani)
- Huna haja ya kufuatilia


## Pakua Picha ya MyNode


Nenda kwenye Kiungo cha tovuti ya MyNode


![image](assets/1.webp)


Bofya `Pakua Sasa`


Pakua toleo la Raspberry Pi 4:


![image](assets/2.webp)


Ni faili kubwa:


![image](assets/3.webp)


Pakua heshi za SHA 256


![image](assets/4.webp)


Fungua terminal kwenye Mac au Linux au Command Prompt kwa Windows. Aina:


```bash
shasum -a 256 DOWNLOADEDFILENAME # <--- Mac/Linux
certUtil -hashfile DOWNLOADEDFILENAME SHA256 # <--- Windows
```


Kompyuta inafikiri kwa sekunde 20 au hivyo. Kisha, angalia kwamba faili ya pato inalingana na ile iliyopakuliwa kutoka kwa tovuti katika hatua ya awali. Ikiwa ni sawa, unaweza kuendelea.

Flash kadi ya SD


## Pakua na usakinishe Balena Etcher. Kiungo


Sikuweza kupata sahihi ya dijitali kwa hili. Ikiwa unajua jinsi gani, tafadhali nijulishe na nitasasisha nakala hii.


Etcher inajieleza kutumia. Weka kadi yako ndogo ya SD na uangaze programu ya Raspberry Pi (faili.img) kwenye kadi ya SD.


![image](assets/5.webp)

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

![image](assets/10.webp)

![image](assets/11.webp)


Mara baada ya kumaliza, hifadhi haisomeki tena. Unaweza kupata hitilafu kutoka kwa mfumo wa uendeshaji, na gari linapaswa kutoweka kutoka kwa desktop. Vuta kadi.


## Sanidi Pi na ingiza kadi ya SD


Sehemu (kesi haijaonyeshwa):


![image](assets/12.webp)

![image](assets/13.webp)


Unganisha kebo ya ethaneti, na kiunganishi cha kiendeshi cha Hard (hakina nguvu bado). Epuka kuunganisha kwenye milango ya USB yenye rangi ya buluu katikati. Ni USB 3. MyNode inapendekeza utumie mlango wa USB 2, ingawa hifadhi inaweza kuwa na uwezo wa USB 3.


![image](assets/14.webp)


Kadi ndogo ya SD huenda hapa:


![image](assets/15.webp)


Hatimaye, unganisha nguvu:


![image](assets/16.webp)


## Pata IP Address ya Pi


Kamwe hauitaji kifuatiliaji na MyNode. Hata hivyo, unahitaji kompyuta nyingine kwenye mtandao wa nyumbani. Ikiwa wewe ni Pi hujaunganishwa na ethaneti, na ungependa kutegemea WiFi, kupata IP kunahitaji ujuzi wa hali ya juu wa kompyuta. Haiwezi kukusaidia, samahani. Unahitaji muunganisho wa ethaneti. (Tatizo linatokana na kuhitaji ufikiaji wa mfuatiliaji na mfumo wa uendeshaji kuunganishwa na WiFi na kuingiza nenosiri).


Angalia kipanga njia chako, kwa orodha ya IP zote za vifaa vyote vilivyounganishwa.


Niliandika 192.168.0.1 kwenye Kivinjari (maelekezo ambayo yalikuja na kipanga njia changu), nikaingia, na nikaweza kuona kifaa cha "MyNode" na IP 192.168.0.18. Kumbuka anwani hizi za IP hazionekani kwa umma kwenye mtandao (hupitia kipanga njia kwanza), ni vitambulishi tu vya vifaa kwenye mtandao wako wa nyumbani.


Kupata IP ni muhimu.


**Kumbuka:** unaweza kutumia terminal kwenye Mac au Linux ili kupata IP Address ya vifaa vyote vilivyounganishwa vya Ethaneti kwenye mtandao wa nyumbani kwa kutumia amri ya “arp -a”. Matokeo sio mazuri kama yale ambayo kipanga njia kitaonyesha, lakini habari yote unayohitaji iko. Ikiwa haijulikani ni ipi, fanya majaribio na makosa.


## SSH kwenye Pi


Una chaguo la kuingia kwenye kifaa kwa mbali kwa amri ya SSH, lakini haihitajiki (ni ikiwa Njia ya RaspiBlitz). Nitakuonyesha jinsi gani, kwani ni rahisi sana.


Fungua kompyuta ya Mac au Linux (kwa Windows, pakua putty, zana ya SSH) na uandike:


```bash
ssh admin@192.168.0.18
```


Tumia IP yako mwenyewe Address. Jina la mtumiaji la kifaa cha MyNode ni "admin" kwa chaguo-msingi. Nenosiri ni "Bolt" kwa chaguo-msingi.


Ikiwa umetumia Pi yako hapo awali na kubadili kadi ndogo ya SD, utapata hitilafu hii:


![image](assets/17.webp)


Unachohitaji kufanya ni kusogeza hadi pale faili ya "inayojulikana_hosts" ilipo na kuifuta. Ni salama. Ujumbe wa makosa unaonyesha njia. Kwangu ilikuwa /Users/MyUserName/.ssh/


Usisahau "." kabla ya ssh, hii inaonyesha kuwa ni saraka iliyofichwa.


Kisha jaribu amri ya ssh tena.


Wakati huu utaona pato hili:


![image](assets/18.webp)


Faili uliyofuta imefutwa na unaongeza alama ya kidole mpya. Andika ndiyo na <enter>.


Utaulizwa kuingiza nenosiri. Ni "Bolt"


Sasa umepata ufikiaji wa terminal kwa MyNode Pi, bila kifuatiliaji, na unaweza kudhibitisha kuwa yote imepakiwa vizuri.


![image](assets/19.webp)


## Fikia kupitia Kivinjari cha Wavuti


Fungua kivinjari. Inahitaji kuwa kompyuta kwenye mtandao wako wa nyumbani, huwezi kufanya hivyo kutoka nje. Kuna njia, lakini ni Hard. Sijaijaribu.


Andika IP Address kwenye dirisha la kivinjari Address. Hii itatokea:


![image](assets/20.webp)


Ingiza nenosiri "Bolt" - ubadilishe baadaye.


Kisha hii itatokea:


![image](assets/21.webp)


Chagua Hifadhi ya Umbizo


![image](assets/22.webp)


Sasa tunasubiri.


Wakati fulani utaulizwa ikiwa ungependa kuweka ufunguo wa bidhaa yako, au utumie "toleo la jumuiya" lisilolipishwa - nitaonyesha toleo la Premium. Ninapendekeza kulipa kwa toleo la malipo ikiwa unaweza kumudu, ni ya thamani sana.


![image](assets/23.webp)


Kisha utaona maendeleo ya vitalu vilivyopakuliwa. Inachukua siku:


![image](assets/24.webp)


Ni salama kuzima mashine wakati wa kupakua ikiwa unahitaji. Nenda kwa mipangilio na utafute kitufe cha kuzima mashine. Usifunge tu kamba, unaweza kuharibu usakinishaji au gari la Hard.


Inahakikisha, mapema, nenda kwa "Mipangilio" na uzima usawazishaji wa haraka. Itaanza upakuaji wa kuzuia mwanzo tangu mwanzo.


![image](assets/25.webp)


Nilitaka kuendelea na kuunda mwongozo, kwa hivyo hapa kuna MyNode nyingine niliyotayarisha hapo awali. Hivi ndivyo ukurasa unavyoonekana wakati Blockchain inasawazishwa, na "programu" kadhaa zimewezeshwa na kusawazishwa:


![image](assets/26.webp)


Kumbuka kuwa Seva ya Electrum inahitaji kusawazishwa pia, kwa hivyo mara tu Bitcoin Blockchain inaposawazishwa, bofya kitufe ili kuanza mchakato huo - inachukua siku moja au mbili. Kila kitu kingine kinawezeshwa kwa dakika chache mara tu unapochagua kuiwasha. Unaweza kubofya vitu na kuchunguza. Hutavunja chochote. Ikiwa kitu kitavunjika (hii ilinitokea, lakini nadhani kwa sababu nilikuwa na sehemu za bei nafuu) itabidi uwaka tena na uanze kupakua tena. Shida niliyo nayo na MyNode ni kwamba ikiwa unahitaji "kuwaka tena" unaishia kuhitaji kuanza usawazishaji wa Blockchain tena kutoka mwanzo. Kuna njia za kiufundi karibu na hili, lakini si rahisi.


Ikiwa unataka kujaribu nodi nyingine pia, sema RaspiBlitz, unahitaji gari la ziada la SSD la Hard, na kadi nyingine ndogo ya SD ili kuangaza. Vinginevyo, ni vifaa sawa, huwezi tu kukimbia MyNode na RaspiBlitz wakati huo huo, ni wazi. Ikiwa unataka kufanya hivyo, ni wakati wa kununua Raspberry Pi nyingine.


Sasa kwa kuwa una nodi inayoendesha, itumie, usiiruhusu ikae tu bila kufanya chochote kwako. Fuata makala yangu (na video) kuhusu jinsi ya kuunganisha Eneo-kazi lako la Electrum Wallet kwenye Seva ya Electrum na Bitcoin Core hapa.