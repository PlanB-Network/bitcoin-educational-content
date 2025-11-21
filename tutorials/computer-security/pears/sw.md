---
name: Pears
description: Je, ninawezaje kusakinisha na kutumia programu kwenye Pears?
---

![cover](assets/cover.webp)



Katika somo hili, tutajifunza jinsi ya kuendesha programu kwenye **Pears**, teknolojia ya peer-to-peer (P2P) iliyotengenezwa na **Holepunch** na kusaidiwa na **Tether**. Kusudi ni rahisi: kufanya uwezekano wa kusambaza na kutumia programu za wavuti bila kutegemea miundombinu yoyote ya kati (hakuna seva, hakuna wapangishi, hakuna wapatanishi). Kwa maneno mengine, hata kama mtoa huduma wa wingu atafunga au nchi itazuia kikoa, programu huishi kati ya programu zingine za mtandao.



## 1. Pears ni nini?



Pears ni mazingira ya wakati wa utekelezaji, zana ya ukuzaji na jukwaa la kusambaza kwa programu za programu kati ya marafiki. Zana hii ya chanzo huria huwezesha kuunda, kushiriki na kuendesha programu bila seva au miundombinu, moja kwa moja kati ya watumiaji. Kwa maneno madhubuti, hii inamaanisha kuwa badala ya kukaribisha programu kwenye seva kuu, kila mtumiaji anakuwa nodi ya mtandao, akishiriki sehemu ya programu na data na wenzao wengine. Mfumo mzima huunda mtandao uliosambazwa, huku kila mfano ukishirikiana ili kuweka huduma ipatikane.



![Image](assets/fr/01.webp)



Njia hii inategemea seti ya matofali ya programu ya kawaida iliyoundwa na Holepunch:




- Hypercore**: kumbukumbu iliyosambazwa ambayo huhakikisha uthabiti wa data na usalama bila hifadhidata kuu.
- Hyperbee**: faharasa juu ya Hypercore, kwa ajili ya kupanga na kuvinjari data kwa ufanisi.
- Hyperdrive**: mfumo wa faili uliosambazwa unaotumiwa kuhifadhi na kusawazisha faili za programu kati ya programu zingine.
- Hyperswarm** na **HyperDHT**: safu za mtandao zinazowezesha ugunduzi na muunganisho kati ya programu zingine ulimwenguni kote, bila seva kuu.
- Secretstream**: itifaki ya usimbaji fiche ya E2E ili kulinda ubadilishanaji kati ya wenzao wawili.



Kwa kuchanganya vipengele hivi, Pears hufanya iwezekanavyo kuunda programu za uhuru, zilizosimbwa na kusambazwa, ambapo kila mtumiaji anashiriki kikamilifu kwenye mtandao. Usanifu huu uliogatuliwa huondoa gharama za miundombinu, hatari za udhibiti na SPOF (*Hati Moja ya Kushindwa*).



## 2. Asili na falsafa ya mradi



Pears inatengenezwa na Holepunch, kampuni iliyoanzishwa na Mathias Buus na Paolo Ardoino (Mkurugenzi Mtendaji Mkuu wa Tether na CTO ya Bitfinex), kwa dhamira ya kupanua mantiki ya rika-kwa-rika zaidi ya Bitcoin. Matarajio yao ni kujenga "Mtandao wa Peer-to-Rika", ambapo kila programu inaweza kufanya kazi bila idhini, bila seva, na bila waamuzi. Holepunch tayari iko nyuma ya **Keet**, programu kamili ya P2P ya mikutano ya video na kutuma ujumbe.



*Mafunzo haya ya usakinishaji wa Pears yamegawanywa katika sehemu kadhaa kulingana na mfumo wako wa uendeshaji. Nenda moja kwa moja kwenye sehemu inayolingana na mazingira yako ili kufuata maagizo yanayofaa :*




- Linux (Debian)** → Sehemu **3**
- Windows** → Sehemu **4**
- macOS** → Sehemu **5**



## 3. Jinsi ya kusakinisha Pears kwenye Linux (Debian)



Kusakinisha Pears kwenye mfumo wa Debian ni rahisi kiasi, lakini kunahitaji sharti chache, ambazo tutaeleza kwa undani katika sehemu hii.



### 3.1. sasisha mfumo



Kwanza kabisa, ni muhimu kuhakikisha kuwa mfumo wako umesasishwa.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. kufunga utegemezi



Pears hutegemea maktaba fulani za mfumo, haswa `libatomic1`, inayotumiwa na wakati wa utekelezaji wa JavaScript. Isakinishe kwa amri ifuatayo:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. sakinisha Node.js na npm kupitia NVM



Pears inasambazwa kupitia *npm*, kidhibiti kifurushi cha *Node.js*. Ingawa Pears haitegemei moja kwa moja *Node.js* kufanya kazi, ni muhimu kwa usakinishaji. Mbinu inayopendekezwa ya kusakinisha *Node.js* kwenye Linux ni *NVM* (*Kidhibiti cha Toleo la Node*), ambayo inakuruhusu kudhibiti matoleo kadhaa ya Node kwa sambamba.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Kisha pakia upya terminal yako ili kuwezesha *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Angalia kuwa *NVM* imewekwa:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Kisha sakinisha toleo thabiti la *Node.js* (k.m. LTS ya sasa):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Angalia usakinishaji wa *Node.js* na *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Kusakinisha Pears na npm



Baada ya *npm* kupatikana, unaweza kusakinisha Pears CLI duniani kote kwenye mfumo wako. Hii itakuruhusu kuendesha amri ya `pear` kutoka saraka yoyote.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Anzisha Pears



Baada ya usakinishaji, endesha tu amri ifuatayo kwenye terminal yako:



```bash
pear
```



Wakati wa uanzishaji wa kwanza, Pears itaunganishwa kwenye mtandao wa rika-kwa-rika ili kupakua vipengele muhimu. Mchakato huu hauhitaji seva kuu: faili zinapatikana moja kwa moja kutoka kwa wenzao wengine.



![Image](assets/fr/10.webp)



Mara tu upakuaji utakapokamilika, endesha amri tena ili kuangalia kuwa kila kitu kinafanya kazi:



```bash
pear
```



![Image](assets/fr/11.webp)



Ikiwa kila kitu kimewekwa kwa usahihi, Msaada wa Pears utaonyeshwa na orodha ya amri zinazopatikana.



### 3.6. Kujaribu Pears na Keet



Ili kuhakikisha kuwa Pears inafanya kazi kikamilifu, unaweza kuzindua programu ya P2P ambayo tayari inapatikana kwenye mtandao, kama vile Keet, programu huria ya Holepunch ya kutuma ujumbe na mikutano ya video.



```bash
pear run pear://keet
```



Amri hii hupakia programu ya Keet moja kwa moja kutoka kwa mtandao wa Pears, bila kupitia seva kuu. Ikiwa Keet itazinduliwa kwa usahihi, usakinishaji wako wa Pears utafanya kazi kikamilifu.



![Image](assets/fr/12.webp)



Mfumo wako wa Linux sasa uko tayari kuendesha na kukaribisha programu-tumizi za peer-to-peer na Pears.



## 4. Jinsi ya kufunga Pears kwenye Windows



Kusakinisha Pears kwenye Windows ni rahisi tu kama kwenye Linux, lakini inahitaji zana chache maalum.



*Ikiwa unatumia Linux, unaweza kuruka hadi hatua ya 6.*



### 4.1. fungua PowerShell katika hali ya msimamizi



Kwanza kabisa, endesha PowerShell na haki za msimamizi:




- Bonyeza kwenye menyu ya Mwanzo;
- Chapa PowerShell ;
- Bonyeza kulia kwenye "*Windows PowerShell*" ;
- Chagua "*Run kama msimamizi*".



![Image](assets/fr/15.webp)



### 4.2. pakua NVS



Pears imesakinishwa kupitia *npm*, kidhibiti kifurushi cha *Node.js*. Kwenye Windows, mbinu inayopendekezwa na Holepunch ni kutumia *NVS* (*Node Version Switcher*), ambayo ni thabiti zaidi kuliko *NVM* kwenye mfumo huu.



Katika PowerShell, endesha amri ifuatayo ili kusakinisha toleo jipya zaidi la *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. sakinisha Node.js



Baada ya usakinishaji, anzisha upya PowerShell na ingiza amri ifuatayo:



```powershell
nvs
```



Unapaswa kuona orodha ya matoleo yanayopatikana ya *Node.js*. Chagua ya kwanza kwa kubonyeza kitufe cha `a` kwenye kibodi yako.



![Image](assets/fr/17.webp)



*Node.js* imesakinishwa.



![Image](assets/fr/18.webp)



### 4.4. Angalia mitambo



Hakikisha *Node.js* na *npm* zinapatikana:



```powershell
node -v
npm -v
```



Amri zote mbili lazima zirudishe nambari ya toleo.



![Image](assets/fr/19.webp)



### 4.5. Kufunga Pears na npm



Mara tu *Node.js* na *npm* zinapatikana, sakinisha **Pears CLI** kimataifa kwenye mfumo wako:



```powershell
npm install -g pear
```



Hii itasakinisha `pear` binary katika saraka yako ya kimataifa ya *npm*.



![Image](assets/fr/20.webp)



### 4.6. Angalia na uanzishe Pears



Mara tu usakinishaji ukamilika, endesha:



```powershell
pear
```



Katika uzinduzi wa kwanza, Pears itapakua kiotomatiki vipengee muhimu kutoka kwa mtandao wa rika-kwa-rika. Mchakato huu unaweza kuchukua muda mfupi.



![Image](assets/fr/21.webp)



Ikiwa kila kitu kimeenda vizuri, unapaswa kuona skrini ya usaidizi ya CLI Pears na orodha ya amri ndogo zinazopatikana (kukimbia, seed, maelezo...).



### 4.7. Kujaribu Pears na Keet



Ili kuhakikisha kuwa Pears inafanya kazi kikamilifu, unaweza kuzindua programu ya P2P ambayo tayari inapatikana kwenye mtandao, kama vile Keet, programu huria ya Holepunch ya kutuma ujumbe na mikutano ya video.



```bash
pear run pear://keet
```



Amri hii hupakia programu ya Keet moja kwa moja kutoka kwa mtandao wa Pears, bila kupitia seva kuu. Ikiwa Keet itazinduliwa kwa usahihi, usakinishaji wako wa Pears utafanya kazi kikamilifu.



![Image](assets/fr/22.webp)



Mfumo wako wa Windows sasa uko tayari kufanya kazi na kukaribisha programu-tumizi za peer-to-peer na Pears.



## 5. Je, ninawekaje Pears kwenye macOS?



Kufunga Pears kwenye macOS ni sawa na kuiweka kwenye Linux, lakini inahitaji marekebisho machache maalum kwa mazingira ya Apple. Wacha tugundue hatua hizi pamoja.



*Ikiwa unatumia Linux au Windows na tayari umesakinisha Pears, unaweza kuendelea moja kwa moja hadi **hatua ya 6**.*



### 5.1. Angalia mahitaji ya mfumo



Kabla ya kusakinisha, tafadhali hakikisha kuwa *Vyombo vya Mstari wa Amri ya Xcode* vipo kwenye mfumo wako. Kifurushi hiki hutoa zana muhimu za ujumuishaji za _Node.js_ na tegemezi zake.



Ili kufanya hivyo, fungua terminal kwa njia ya mkato ya kibodi `Cmd + Space bar`, kisha chapa `Terminal` na ubonyeze kitufe cha `Enter`. Kisha unaweza kuingiza amri hii kwenye terminal ili kuzindua usakinishaji:



```bash
xcode-select --install
```



Ikiwa zana tayari zimewekwa kwenye mfumo wako, macOS itakujulisha.



### 5.2. kufunga NVM



Pears inasambazwa kupitia *npm*, kidhibiti kifurushi cha *Node.js*. Ingawa Pears haitegemei moja kwa moja *Node.js* kufanya kazi, ni muhimu kwa usakinishaji. Njia inayopendekezwa ya kusakinisha *Node.js* kwenye macOS ni *NVM* (*Kidhibiti cha Toleo la Node*), ambayo hukuruhusu kudhibiti matoleo kadhaa ya Node kwa sambamba.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Kisha pakia upya terminal yako ili kuwezesha *NVM* :



```bash
source ~/.zshrc
```



Ikiwa unatumia *bash* badala ya *zsh*, run :



```bash
source ~/.bashrc
```



Kisha angalia kuwa *NVM* imewekwa:



```bash
nvm --version
```



Terminal inapaswa kurudisha toleo la *NVM* lililosakinishwa kwenye mfumo wako.



### 5.3. sakinisha Node.js na npm



Kisha sakinisha toleo thabiti la *Node.js* (k.m. LTS ya sasa):



```bash
nvm install --lts
```



Mara tu usakinishaji ukamilika, angalia matoleo yaliyosakinishwa:



```bash
node -v
npm -v
```



Amri zote mbili lazima zirudishe nambari ya toleo.



### 5.4 Kuweka Pears na npm



Baada ya *npm* kupatikana, unaweza kusakinisha Pears CLI kimataifa kwenye mfumo wako. Hii itakuruhusu kuendesha amri ya `pear` kutoka saraka yoyote.



```bash
npm install -g pear
```



### 5.5. Anzisha Pears



Baada ya usakinishaji, endesha tu amri ifuatayo kwenye terminal yako:



```bash
pear
```



Wakati wa uanzishaji wa kwanza, Pears itaunganishwa kwenye mtandao wa rika-kwa-rika ili kupakua vipengele muhimu. Mchakato huu hauhitaji seva kuu: faili zinapatikana moja kwa moja kutoka kwa wenzao wengine.



Mara tu upakuaji utakapokamilika, endesha amri tena ili kuangalia kuwa kila kitu kinafanya kazi:



```bash
pear
```



Ikiwa kila kitu kimewekwa kwa usahihi, Msaada wa Pears utaonyeshwa na orodha ya amri zinazopatikana.



### 5.6. Kujaribu Pears na Keet



Ili kuhakikisha kuwa Pears inafanya kazi kikamilifu, unaweza kuzindua programu ya P2P ambayo tayari inapatikana kwenye mtandao, kama vile Keet, programu huria ya Holepunch ya kutuma ujumbe na mikutano ya video.



```bash
pear run pear://keet
```



Amri hii hupakia programu ya Keet moja kwa moja kutoka kwa mtandao wa Pears, bila kupitia seva kuu. Ikiwa Keet itazinduliwa kwa usahihi, usakinishaji wako wa Pears utafanya kazi kikamilifu.



Mfumo wako wa macOS sasa uko tayari kutumika na kukaribisha programu-tumizi za rika-kwa-rika na Pears.



## 6. Je, ninawezaje kutumia programu kwenye Pears?



Mara tu Pears inapoanza na kufanya kazi, unaweza kuendesha utumizi wa chaguo lako moja kwa moja kwa amri ifuatayo:



```bash
pear run pear://[KEY]
```



Badilisha tu `[KEY]` na ufunguo wa programu unayotaka kutumia.



![Image](assets/fr/13.webp)



Ili kujifunza jinsi ya kuendesha jukwaa letu la Plan ₿ Academy kwenye Pears, angalia mafunzo haya ya kina :



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Na ili kujua jinsi ya kutumia programu ya kutuma ujumbe ya Keet ambayo umezindua hivi punde kwenye Pears, angalia mafunzo haya:



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b