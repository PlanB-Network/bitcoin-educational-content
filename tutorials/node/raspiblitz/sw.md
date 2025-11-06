---
name: RaspiBlitz
description: Mwongozo wa kusanidi RaspiBlitz yako
---

![image](assets/0.webp)


RaspiBlitz ni Njia ya Umeme ya kukufanya-wewe-mwenyewe (LND na/au Umeme wa Msingi) inayoendesha pamoja na Bitcoin-Fullnode kwenye RaspberryPi (1TB SSD) na onyesho zuri kwa usanidi na ufuatiliaji kwa urahisi.


RaspiBlitz inalengwa hasa kwa kujifunza jinsi ya kuendesha nodi yako mwenyewe iliyogatuliwa kutoka nyumbani - kwa sababu: Si Njia yako, Si Kanuni zako. Gundua na uendeleze mfumo wa ikolojia unaokua wa Lightning Network kwa kuwa sehemu yake kamili. Ijenge kama sehemu ya warsha au kama mradi wa wikendi wewe mwenyewe.


![video](https://youtu.be/DTHlSPMz3ns)

RASPIBLITZ - Jinsi ya Kuendesha Umeme na Bitcoin Full node kwa kipindi cha BTC


# Mwongozo wa Kuweka Raspiblitz wa Parman


Raspiblitz ni mfumo bora wa kuendesha Node ya Bitcoin na programu zinazohusiana. Ninapendekeza hii na Node ya MyNode kwa watumiaji wengi (iwe bora kuwa na nodes mbili kwa upungufu wa hatari). Faida kuu ni kwamba Node ya Raspiblitz ni "Free Open Source Software", tofauti na MyNode au Umbrel. [Kwa nini hilo ni muhimu? Vlad Costa anaeleza.](https://bitcoin-takeover.com/why-bitcoin-free-open-source-software-matters/amp/?__twitter_impression=true) Pia unaweza kuendesha Raspiblitz kwa muunganisho wa WiFi badala ya ethernet – hapa kuna [mwongozo wa ziada](https://armantheparman.com/headless-wifi/) kwa hilo. (Sijapata njia ya kufanya hivyo na MyNode).


Unaweza kununua node iliyopangwa tayari na skrini ndogo iliyounganishwa, au unaweza kuijenga mwenyewe (huhitaji skrini).


[Mwongozo kwenye ukurasa wa GitHub](https://github.com/rootzoll/raspiblitz) ni bora, lakini huenda ukawa na maelezo mengi sana kwa mtumiaji mwenye uzoefu wa wastani. Maelekezo yangu yatakuwa mafupi zaidi na natumai rahisi kufuata.


Kimsingi, mchakato huu ni sawa sana na mchakato wa kusanidi [node ya MyNode](https://armantheparman.com/mynode-bitcoin-node-easy-setup-guide-raspberry-pi/) kwa kutumia Raspberry Pi 4. Mwongozo wa Raspiblitz unapendekeza ununue skrini, lakini kwa kweli huhitaji moja, na mimi nisingependekeza. Hata huhitaji kibodi au kipanya cha ziada. Ingia tu kwenye menyu ya terminal ya kifaa kupitia kompyuta iliyo kwenye mtandao wa nyumbani huo huo, na utumie amri ya ssh kwa kutumia terminal. Hii inawezekana na Linux/Mac (rahisi) na ni ngumu kidogo na Windows.


## Hatua ya 1: Nunua vifaa.


Unahitaji vifaa sawa ambavyo unahitaji kuendesha nodi ya MyNode. Unaweza kujaribu moja au nyingine, tofauti pekee ni data kwenye kadi ndogo ya SD.



- Raspberry Pi 4, kumbukumbu ya 4Gb au 8Gb (4Gb ni nyingi)
- Raspberry Pi Power (Muhimu Sana! Usichukue generic, umakini)
- Kesi kwa Pi. (Kipochi cha FLIRC kinapendeza. Kipochi kizima ni bomba la joto na huhitaji feni, ambayo inaweza kuwa na kelele)
- 32 Gb microSD kadi (unahitaji moja, lakini chache ni muhimu.)
- Msomaji wa kadi ya kumbukumbu (kompyuta nyingi hazitakuwa na slot kwa kadi ya microSD).
- Hifadhi ya nje ya SSD 1Tb Hard.
- Kebo ya ethaneti (ili kuunganisha kwenye kipanga njia chako cha nyumbani).


Huna haja ya kufuatilia (au keyboard au kipanya)


Kumbuka: Hili ni gari lisilo sahihi la Hard: Hii ni kiendeshi cha nje cha Hard kinachobebeka. Sio SSD. SSD ni muhimu. Hii ndio sababu ni nafuu (Bei katika AUD)


![image](assets/1.webp)


Hii ndio aina sahihi ya kupata:


![image](assets/2.webp)


Hii ni haraka, lakini ni ghali sana:


![image](assets/3.webp)


## Hatua ya 2: Pakua Picha ya Raspiblitz


Nenda kwenye [tovuti ya GitHub ya Raspiblitz](https://github.com/rootzoll/raspiblitz), na upate kiungo cha “download image”:


![image](assets/4.webp)


Hash ya sha-256 ya faili lililopakuliwa imetolewa kwenye tovuti. Itabadilika kila sasisho. Ikiwa huelewi hii inahusu nini, unapaswa kuelewa, kwa hivyo niliandika [mwongozo ambao unaweza kusoma hapa.](https://armantheparman.com/gpg/)


![image](assets/5.webp)


## Hatua ya 3: Thibitisha Picha


Kabla ya kuendelea, ikiwa hujui njia yako karibu na mfumo wa faili kwenye mstari wa amri, ni rahisi kujifunza, na unapaswa.


Hapa kuna [video yenye msaada kwa Linux, lakini pia inatumika kwa Mac](https://youtu.be/id3DGvljhT4?list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK).


Kwa Windows, hapa kuna [mafunzo rahisi](https://www.youtube.com/watch?v=MBBWVgE0ewk&t=1s).


_SASISHO: Uthibitishaji wa pgp/gpg sasa unapatikana. Utahitaji ufunguo wa umma wa Openoms. [Hapa](http://parman.org/downloadable/openoms.txt) ndio ulipo (huenda ukahitaji hali fiche ili kiungo kifanye kazi – http, sio https)_
Mac/Linux


Subiri faili ikamilishe kupakua (muhimu!), kisha ukiwa na terminal wazi, nenda mahali ulipopakua faili, na uandike amri ifuatayo:

```bash
shasum -a 256 xxxxxxxxxxxxxx
```


ambapo `xxxxxxxxxxxxxx` ni jina la faili ambayo umepakua hivi punde. Ikiwa hauko kwenye saraka ambapo faili hiyo iko, lazima uchapishe njia kamili.


Kompyuta inafikiri kwa sekunde 20 au hivyo. Angalia kuwa faili ya pato inalingana na ile iliyopakuliwa kutoka kwa wavuti katika hatua ya awali. Ikiwa ni sawa, unaweza kuendelea.

Windows


Fungua haraka ya amri na uende mahali faili inapakuliwa, na uandike amri hii:


```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```


ambapo `xxxxxxxxxxxxxx` ni jina la faili ambayo umepakua hivi punde. Ikiwa hauko katika mkurugenzi ambapo faili hiyo iko, lazima uchapishe njia kamili.


Kompyuta inafikiri kwa sekunde 20 au hivyo. Angalia kuwa faili ya pato inalingana na ile iliyopakuliwa kutoka kwa wavuti katika hatua ya awali. Ikiwa ni sawa, unaweza kuendelea.


## Hatua ya 4: Flash kadi ya SD


Unaweza kutumia Balena Etcher kufanya hivi. [Ipakue hapa](https://www.balena.io/etcher/).


Etcher inajieleza mwenyewe kutumia. Ingiza kadi yako ndogo ya SD na uangaze programu ya Raspiblitz (faili.img) kwenye kadi ya SD.


![image](assets/6.webp)


![image](assets/7.webp)


![image](assets/8.webp)


![image](assets/9.webp)


Mara baada ya kumaliza, hifadhi haisomeki tena. Unaweza kupata hitilafu kutoka kwa mfumo wa uendeshaji, na gari linapaswa kutoweka kutoka kwa desktop. Vuta kadi.


## Hatua ya 5: Sanidi Pi na ingiza kadi ya SD


Sehemu (kesi haijaonyeshwa):


![image](assets/10.webp)


![image](assets/11.webp)


Unganisha kebo ya ethaneti, na kiunganishi cha kiendeshi cha Hard (hakina nguvu bado). Epuka kuunganisha kwenye milango ya USB ya rangi ya samawati iliyo katikati. Ni USB 3. Tumia mlango wa USB 2, ingawa hifadhi inaweza kuwa na uwezo wa USB 3 (inayotegemewa zaidi).


![image](assets/12.webp)


Kadi ndogo ya SD huenda hapa:


![image](assets/13.webp)


Hatimaye, unganisha nguvu:


![image](assets/14.webp)


## Hatua ya 6: Pata IP Address ya Pi


Kamwe hauhitaji kifuatiliaji na Raspiblitz. Hata hivyo, unahitaji kompyuta nyingine kwenye mtandao wa nyumbani. Ikiwa wewe ni Pi hujaunganishwa na ethaneti, na unataka kutegemea WiFi, kupata IP kunahitaji ujuzi fulani wa kompyuta. Haiwezi kukusaidia, samahani. Unahitaji muunganisho wa ethaneti. (Tatizo linatokana na kuhitaji ufikiaji wa kifuatiliaji na mfumo wa uendeshaji ili kuunganisha WiFi na kuingiza nenosiri.)


Angalia kipanga njia chako, kwa orodha ya IP zote za vifaa vyote vilivyounganishwa.


Niliandika 192.168.0.1 kwenye Kivinjari (maelekezo ambayo yalikuja na kipanga njia changu), nikaingia, na niliweza kuona kifaa changu na IP 192.168.0.191. Kumbuka anwani hizi za IP hazionekani kwa umma kwenye mtandao (hupitia kipanga njia kwanza), ni vitambulisho tu vya vifaa kwenye mtandao wako wa nyumbani.


Kupata IP ni muhimu.


**Kumbuka:** unaweza kutumia terminal kwenye Mac au Linux ili kupata IP Address ya vifaa vyote vilivyounganishwa vya Ethaneti kwenye mtandao wa nyumbani kwa kutumia amri ya “arp -a”. Matokeo sio mazuri kama yale ambayo kipanga njia kitaonyesha, lakini habari yote unayohitaji iko. Ikiwa haijulikani ni ipi, fanya majaribio na makosa.


## Hatua ya 7: SSH kwenye Pi


Kumbuka kuweka kadi ya SD kwenye Pi kabla ya kuiwasha. Subiri dakika chache, na kisha kwenye Linux/Mac nyingine, fungua terminal.


Kwa Mac/Linux, katika aina ya terminal:


```bash
ssh admin@You_Pi's_IP_address
```


Kwa Windows, utahitaji kusakinisha [putty](http://putty.org/) ili kuingia kwenye Pi kwa ssh. Andika amri ile ile kama hapo juu.


Mara ya kwanza unapofanya hivi, au wakati wowote unapobadilisha OS ya Pi kwa kubadili kadi ya SD, unaweza kupata au usipate hitilafu hii...


![image](assets/15.webp)


Njia ya kurekebisha ni kwenda mahali faili "inayojulikana_hosts" iko (inakuambia katika ujumbe wa makosa), na kuifuta. Amri ni "rm known_hosts"


Kisha, rudia amri ya ssh kuingia. Hii itafanyika...


![image](assets/16.webp)


Andika ndiyo (neno kamili) ili kuendelea.


Ikifanikiwa, utaulizwa nenosiri. Hii sio ya kompyuta yako, lakini raspiblitz. Nenosiri la kawaida ni "raspiblitz", na utalibadilisha baadaye. Dirisha la terminal litageuka kuwa bluu na utakuwa na chaguzi za menyu kama menyu za zamani za DOS. Sogeza kwa kutumia vitufe vya vishale au kipanya.


![image](assets/17.webp)


Fuata mawaidha, weka manenosiri yako, na kisha itatambua kiendeshi chako cha Hard na kukupa chaguo la kuiumbiza ikihitajika.


Kisha utaulizwa ikiwa unataka kunakili data ya Blockchain kutoka kwa chanzo kingine au kuipakua tena. Kuinakili ni mchakato wa kujifunza na maagizo ni mazuri kabisa, na ni vizuri kuyaweka vizuri….


![image](assets/18.webp)


Njia rahisi lakini ya polepole ni kupakua mnyororo mzima kutoka mwanzo…


![image](assets/19.webp)


Maandishi mengi yatamulika kwenye skrini ya terminal. Unaweza kukosea kama mchakato wa upakuaji wa Blockchain, lakini inaonekana kama, kwangu, inazalisha ufunguo wa faragha wa mawasiliano.


Kisha chaguzi za umeme zinaonekana.


![image](assets/20.webp)


Tengeneza nenosiri jipya ili kufunga mwanga wako wa Wallet, kisha Wallet mpya itaundwa na utapewa maneno 24 ya kuandika...


![image](assets/21.webp)


Hakikisha umeiandika na kuiweka salama. Nilisikia mtu mmoja ambaye hakufanya hivyo kwa sababu hakuwa na mipango ya kutumia umeme, lakini mwaka mmoja baadaye aliamua kuutumia, na kufungua njia. Kisha kutambua maneno yake hayakuwa yameungwa mkono, na nakumbuka haikuwezekana kutoa maneno tena kutoka kwenye kifaa, ilibidi afunge chaneli zake zote na kuanza tena. Aliondoka nayo, lakini wengine wanaweza wasiwe na bahati sana.


Kufuatia hili, dakika chache za maandishi husonga chini ya dirisha la terminal. Kisha…


![image](assets/22.webp)


Utaondolewa kwenye kipindi cha ssh. Ingia tena, wakati huu kwa nenosiri lako jipya, nenosiri A. Ukishaingia utaombwa nenosiri C ili kufungua Wallet yako ya umeme.


Sasa tunasubiri. Tuonane baada ya wiki 2. Unaweza kufunga terminal, haifanyi chochote kwa Pi, ni dirisha la mawasiliano tu.


![image](assets/23.webp)


Ikiwa kwa sababu yoyote ile, unataka kuzima Pi kabla ya Blockchain kumaliza kupakua, ni sawa mradi tu uifanye vizuri. Blockchain itaendelea kupakua pale ilipoishia mara tu utakapounganisha tena.


Gonga CTRL+c ili kuondoka kwenye skrini ya bluu. Utakuwa unapata terminal ya Linux ya Pi. Hapa unaweza kuandika "menyu" ambayo hupakia skrini ifuatayo, na kutoka hapo unaweza kuzima Pi.


![image](assets/24.webp)


MWISHO wa mwongozo


Kwa hivyo kuanzia sasa nodi yako iko tayari kwenda. Ikiwa bado utasaidia kupata chaguo zaidi, rejelea github kwa mafunzo zaidi na mwongozo https://github.com/raspiblitz/raspiblitz#feature-documentation
