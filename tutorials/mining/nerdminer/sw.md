---
name: Nerdminer
description: Anzisha Mining Bitcoin ukiwa na nafasi ya kushinda karibu na 0
---

![cover](assets/cover.webp)

## Usanidi wa NerdMiner v2 yako


Katika somo hili, tutakuongoza kupitia hatua zinazohitajika ili kusanidi NerdMiner_v2, ambayo ni kifaa cha maunzi (ESP-32 S3) kinachotolewa kwa Bitcoin Mining.

Kwa wazi, nguvu ya kompyuta ya kifaa kama hicho haiwezi kushindana na ASICs ya wachimbaji amateur au wataalamu. Hata hivyo, NerdMiner ni zana bora ya kielimu ya kufanya Bitcoin Mining ionekane. Na ni nani anayejua, kwa bahati (nyingi), unaweza kupata kizuizi na thawabu inayoendana nayo. Kwa wanaodadisi, tutaona katika [Kadirio la uwezekano wa kushinda](#estimation-de-la-probabilite-de-gain) sehemu. Kwa upande wa matumizi ya nguvu, NerdMiner hutumia 0.5W; kwa kulinganisha, taa ya LED hutumia wastani wa mara 20 zaidi.


Kabla ya kupitia hatua tofauti, hebu tuorodhe vifaa muhimu vya kuifanya:



- a [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- a [USB-C power Supply](https://amzn.eu/d/gIOot90)
- kipochi cha 3D: ikiwa una kichapishi cha 3D, unaweza kupakua [faili ya 3D](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) vinginevyo unaweza kuinunua kwenye [Duka la mtandaoni la Silexperience](https://silexperience.company.4747/29/NerdMiner57/29/NerdMiner577).
- Kompyuta iliyo na Kivinjari cha Chrome kilichosakinishwa
- muunganisho wa mtandao
- Bitcoin Address


Unaweza pia kununua vifaa vya NerdMiner vilivyokusanywa mapema kutoka kwa wauzaji kadhaa kama vile:



- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-Miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)


Kwanza, tutaona jinsi ya kuangaza programu kwenye ESP-32 S3, na kisha tutaona jinsi ya kuanzisha upya ili kubadilisha mtandao wa wifi. Hatua hizi ni za watumiaji wa Windows, ikiwa unatumia Mfumo wa Uendeshaji wa Linux, tafadhali tekeleza [hatua za awali](#etapes-preliminaires-pour-utilisateurs-linux) ili kuruhusu utambuzi wa ESP-32 S3 na mfumo wako.


**Usakinishaji wa Programu ya NerdMiner_v2** umerahisishwa sana kutokana na matumizi ya webflasher.


## Hatua ya 1: Maandalizi ya Webflasher


Kwanza, unahitaji kwenda kwenye [kimulika cha mtandaoni cha NM2](https://bitmaker-hub.github.io/diyflasher/).


Kisha chagua firmware inayolingana na ESP-32 yako. Mara nyingi ni chaguo-msingi: T-Display S3. Kisha bonyeza "Flash".


**Kumbuka⚠️ :** ni muhimu utumie kivinjari cha Chrome - kwani hukuruhusu, kwa chaguomsingi, matumizi ya flash na ufikiaji wa milango yako ya USB.


![image](assets/webflasher.webp)


## Hatua ya 2: Kuunganisha ESP-32


Mara tu kiangaza wavuti kinapozinduliwa, dirisha ibukizi litafunguliwa likionyesha bandari tofauti za USB zinazotambuliwa na kivinjari.

Kisha unaweza kuunganisha ESP-32 yako, na mlango mpya utaonyeshwa (katika kesi hii, ni ttyACM0 bandari). Kisha lazima uchague na ubofye "kuunganisha".


![image](assets/flasher-port-serial.webp)


Programu itapakuliwa kwa ESP32 yako katika suala la sekunde.


![image](assets/NM2-sucessfully-installed.webp)


## Hatua ya 3: Usanidi wa NerdMiner


Usanidi wa NerdMiner yako utafanywa kupitia simu mahiri au kompyuta.

Washa WiFi na uunganishe kwenye mtandao wa ndani wa NerdMinerAP. Ikiwa unatumia smartphone, portal ya usanidi itafungua moja kwa moja. Vinginevyo, chapa Address 192.168.4.1 kwenye kivinjari.

Kisha chagua "Sanidi WiFi".


Sasa unaweza kusanidi NerdMiner yako.

Kwanza, anza kwa kuunganisha kwenye mtandao wako wa WiFi kwa kuchagua jina la mtandao wako na kuingiza nenosiri linalohusika.


Kisha unaweza kuchagua Mining pool unayotaka kushiriki. Hakika, ni kawaida katika sekta ya Bitcoin Mining kuunganisha nguvu za kompyuta ili kuongeza nafasi za kupata kizuizi katika Exchange kwa kushiriki zawadi sawia na Hashrate iliyotolewa.

Kwa NerdMiners, unaweza kuchagua kuunganisha kwenye moja ya mabwawa haya:


| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Default Solo and open-source mining pool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Maintained by CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Maintained by djerfy                     |

Mara tu unapochagua bwawa lako la kuogelea, unahitaji kuingiza Bitcoin Address yako ili kupokea zawadi endapo (kipekee) kizuizi kitapatikana.


Pia, chagua saa za eneo lako ili NerdMiner iweze kuonyesha saa kwa usahihi.

Sasa unaweza kubofya "Hifadhi".


![image](assets/wifi-configuration.webp)


Hongera, sasa wewe ni sehemu ya mtandao wa Bitcoin Mining!


## Operesheni ya NerdMiner


Programu ya NerdMinerv2 ina skrini 3 tofauti, ambazo unaweza kufikia kwa kubofya kitufe cha juu upande wa kulia wa skrini yako:



- Skrini kuu hutoa ufikiaji wa takwimu za NerdMiner yako.
- Skrini ya pili hutoa ufikiaji wa saa, Hashrate yako, bei ya Bitcoin, na urefu wa block.
- Skrini ya tatu hutoa ufikiaji wa takwimu kwenye mtandao wa kimataifa wa Bitcoin Mining.

![image](assets/NM2-screens.webp)


Ikiwa unataka kuwasha upya NerdMiner yako, kwa mfano kubadilisha mtandao wa WiFi, unahitaji kubonyeza kitufe cha juu kwa sekunde 5.


Kubonyeza kitufe cha chini mara moja kutazima NerdMiner yako. Kubofya mara mbili kutazungusha uelekeo wa skrini.


### Hatua za awali kwa watumiaji wa Linux


Hapa kuna hatua za Chrome kugundua mlango wako wa serial kwenye Linux.


1. Tambua mlango unaohusishwa:



- Unganisha ESP-32 yako kwenye kompyuta yako.
- Fungua terminal.
- Ingiza amri ifuatayo ili kuorodhesha bandari zote:
  - `dmesg | grep tty`
  - au `ls /dev/tty*`
- Ili kuwa na uhakika wa bandari, unaweza kuendelea kwa kuondoa kwa kurudia amri bila ESP-32 kuunganishwa.


2. Badilisha ruhusa ya mlango unaohusishwa:



- Kwa chaguo-msingi, ufikiaji wa milango ya mfululizo unaweza kuhitaji ruhusa za mizizi, kwa hivyo tutazifanya zipatikane kwa kuongeza mtumiaji wako kwenye kikundi cha `dialout`.
  - `sudo usermod -a -G diaut YOUR_USERNAME`, badilisha `YOUR_USERNAME` na jina lako la mtumiaji.
  - kisha utoke na uingie tena kama mtumiaji huyu, au anza upya mfumo ili kuhakikisha kuwa mabadiliko ya kikundi yanatekelezwa.


Kwa vile sasa ESP-32 yako inatambuliwa na mfumo wako, unaweza kurudi kwenye [hatua ya kwanza](#etape-1-preparation-du-webflasher) kwa usakinishaji wa programu.


## Hitimisho


Na hapo unayo! NerdMiner_v2 yako sasa imesanidiwa na iko tayari kutumika.


Furahia Mining na bahati nzuri iwe upande wako!


### Kukadiria uwezekano wa kushinda


Hebu tufurahie kukadiria uwezekano wa kushinda Block reward. Kadirio hili litakuwa mbaya na linatafuta tu kupata mpangilio wa ukubwa wa uwezekano.

Dimbwi ambalo NerdMiner anaweza kuunganishwa nalo ni "solo Mining pool" ambalo lina maana kwamba bwawa hilo halilinganishi Hashrate ya wachimba migodi wote waliounganishwa bali hufanya kazi tu kama mratibu.

Sasa hebu tuchukulie kwamba NerdMiner yetu ina Hashrate ya takriban 45kH/s.


Tukijua kuwa jumla ya Hashrate ni takriban 450 EH/s (au 4.5 x 10^20 heshi kwa sekunde), tunaweza kuzingatia kwamba uwezekano wa kupata kizuizi kinachofuata ni 1 kati ya mabilioni milioni 100, ambayo ni rahisi sana kutokea. Kwa hivyo pamoja na kuwa zana ya elimu na kitu cha udadisi, NerdMiner inaweza kutumika kama tikiti ya bahati nasibu katika Bitcoin Mining kwa gharama ya chini ya umeme ya 0.5 W--ingawa tumeona hivi punde uwezekano wa kushinda ni mdogo sana. Hata hivyo, kwa nini upinge bahati yako?


### Maelezo ya Ziada


Hapa kuna baadhi ya viungo kama unataka kusoma zaidi kuhusu somo:



- [Ukurasa wa mradi wa NerdMiner_v2](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Kamilisha hati za NerdMiners](https://docs.bitwater.ch/nerd-Miner-v2/)
