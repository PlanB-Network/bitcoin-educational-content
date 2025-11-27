---
name: Panga ₿ Chuo - Programu ya Pears
description: Jinsi ya kusakinisha na kutumia programu ya Plan ₿ Academy kwenye Pears?
---

![cover](assets/cover.webp)


Labda tayari unajua kwamba Plan ₿ Academy ndiyo hifadhidata kubwa zaidi ya elimu inayotolewa kwa Bitcoin, inayoleta pamoja kozi, mafunzo na maelfu ya rasilimali huria. Hapo awali, Plan ₿ Academy ilikuwa tovuti. Lakini nini kingetokea ikiwa huwezi tena kuipata kama kawaida, kwa mfano katika tukio la udhibiti?


Katika somo hili, tutajifunza jinsi ya kuendesha jukwaa la **Panga ₿ Academy** kwa njia inayostahimili udhibiti wa kweli kwa kutumia **Pears**, teknolojia ya peer-to-peer (P2P) iliyotengenezwa na **Holepunch** na kuungwa mkono na **Tether**.


Pears ni programu inayoturuhusu kuendesha jukwaa la Chuo cha Plan ₿ bila kutegemea tovuti kuu. Katika somo hili, tutasakinisha Pears kwenye kompyuta yako ili kufikia Plan ₿ Academy kupitia Pears.


Lengo la Pears ni rahisi: kuwezesha kusambaza na kutumia programu za wavuti bila kutegemea miundombinu yoyote ya kati (hakuna seva, hakuna wapangishi, hakuna wapatanishi). Kwa maneno mengine, hata kama mtoa huduma wa wingu atazima au nchi itazuia kikoa, programu inaendelea kuishi kati ya wenzao wa mtandao. Mbinu hii inaruhusu jukwaa letu la elimu, Panga ₿ Academy, kuendelea kufikiwa duniani kote, bila hata nukta moja ya kushindwa.


---

**TL;DR:**



- Weka Pears;



- Tekeleza amri ifuatayo ili kuzindua programu ya Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Pears ni nini?


Pears kwa wakati mmoja ni mazingira ya wakati wa utekelezaji, zana ya ukuzaji, na jukwaa la kusambaza kwa programu-tumizi za programu rika. Zana hii ya chanzo huria hukuruhusu kuunda, kushiriki, na kuendesha programu bila seva au miundombinu, moja kwa moja kati ya watumiaji. Kwa maneno ya vitendo, hii inamaanisha kuwa badala ya kukaribisha programu kwenye seva kuu, kila mtumiaji anakuwa nodi kwenye mtandao: wanashiriki sehemu ya programu na data na wenzao wengine. Mfumo mzima huunda mtandao uliosambazwa ambapo kila mfano hushirikiana kuweka huduma kupatikana.


![Image](assets/fr/01.webp)


Mbinu hii inategemea seti ya vifaa vya kawaida vya programu vilivyotengenezwa na Holepunch:



- Hypercore**: kumbukumbu iliyosambazwa ambayo inahakikisha uthabiti wa data na usalama bila hifadhidata kuu.
- Hyperbee**: faharasa iliyojengwa juu ya Hypercore ambayo inaruhusu data kupangwa na kuulizwa kwa ufanisi.
- Hyperdrive**: mfumo wa faili uliosambazwa unaotumiwa kuhifadhi na kusawazisha faili za programu kati ya programu zingine.
- Hyperswarm** na **HyperDHT**: safu za mtandao zinazowezesha ugunduzi wa programu rika na miunganisho duniani kote bila seva kuu.
- Secretstream**: itifaki ya usimbaji fiche kutoka mwisho hadi mwisho ambayo hulinda mawasiliano kati ya programu zingine.


Kwa kuchanganya vipengele hivi, Pears huwezesha uundaji wa programu zinazojiendesha, zilizosimbwa, na kusambazwa, ambapo kila mtumiaji hushiriki kikamilifu katika mtandao. Usanifu huu uliogatuliwa huondoa gharama za miundombinu, hatari za udhibiti na SPOF (*Alama Moja za Kushindwa*).


Pears imeundwa na Holepunch, kampuni iliyoanzishwa na Mathias Buus na Paolo Ardoino (Mkurugenzi Mtendaji Mkuu wa Tether na CTO ya Bitfinex), kwa dhamira ya kupanua mantiki ya rika-kwa-rika zaidi ya Bitcoin. Matarajio yao ni kuunda “*Mtandao wa programu zingine*,” ambapo kila programu inaweza kufanya kazi bila ruhusa, bila seva na bila wapatanishi. Holepunch tayari iko nyuma ya **Keet**, programu kamili ya mikutano ya video ya P2P na ya kutuma ujumbe.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Mafunzo haya ya usakinishaji wa Pears yamegawanywa katika sehemu nyingi kulingana na mfumo wako wa uendeshaji. Nenda moja kwa moja kwa ile inayolingana na mazingira yako ili kufuata maagizo yanayofaa:*



- Linux (Debian)** → Sehemu **2**
- Windows** → Sehemu **3**
- macOS** → Sehemu **4**


## 2. Jinsi ya kufunga Pears kwenye Linux (Debian)?


Kusakinisha Pears kwenye Debian ni rahisi kiasi lakini kunahitaji sharti chache, ambazo tutaeleza kwa undani katika sehemu hii.


### 2.1. Sasisha mfumo


Kabla ya kitu kingine chochote, ni muhimu kuhakikisha kuwa mfumo wako umesasishwa.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Sakinisha vitegemezi


Pears hutegemea baadhi ya maktaba za mfumo, ikiwa ni pamoja na `libatomic1`, inayotumiwa na injini ya muda wa uendeshaji ya JavaScript. Isakinishe kwa amri ifuatayo:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Sakinisha Node.js na npm kupitia NVM


Pears inasambazwa kupitia *npm*, kidhibiti kifurushi cha *Node.js*. Ingawa Pears haitegemei moja kwa moja *Node.js* ili kuendeshwa, inahitajika ili kusakinisha. Njia inayopendekezwa ya kusakinisha *Node.js* kwenye Linux ni kupitia *NVM* (*Kidhibiti cha Toleo la Nodi*), ambayo hukuruhusu kudhibiti matoleo mengi ya Node kando.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Kisha, pakia upya terminal yako ili kuamilisha *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Angalia kuwa *NVM* imewekwa vizuri:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Ifuatayo, sakinisha toleo thabiti la *Node.js* (kwa mfano, toleo la sasa la LTS):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Thibitisha kuwa *Node.js* na *npm* zimesakinishwa ipasavyo:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Sakinisha Pears na npm


Baada ya *npm* kupatikana, unaweza kusakinisha Pears CLI kimataifa kwenye mfumo wako. Hii hukuruhusu kuendesha amri ya `pear` kutoka saraka yoyote.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Anzisha Pears


Baada ya usakinishaji, endesha tu amri ifuatayo kwenye terminal yako:


```bash
pear
```


Wakati wa uzinduzi wa kwanza, Pears itaunganishwa kwenye mtandao wa rika-kwa-rika ili kupakua vipengele muhimu. Mchakato huu hautegemei seva kuu yoyote - faili hutolewa moja kwa moja kutoka kwa programu zingine.


![Image](assets/fr/10.webp)


Mara tu upakuaji ukamilika, endesha amri tena ili kuthibitisha kila kitu kinafanya kazi:


```bash
pear
```


![Image](assets/fr/11.webp)


Ikiwa kila kitu kimewekwa kwa usahihi, menyu ya usaidizi ya Pears itaonekana na orodha ya amri zinazopatikana.


### 2.6. Jaribu Pears na Keet


Ili kuthibitisha kwamba Pears inafanya kazi kikamilifu, unaweza kuzindua programu iliyopo ya P2P inayopatikana kwenye mtandao, kama vile Keet, programu huria ya kutuma ujumbe na mikutano ya video iliyotengenezwa na Holepunch.


```bash
pear run pear://keet
```


Amri hii hupakia programu ya Keet moja kwa moja kutoka kwa mtandao wa Pears, bila kutumia seva kuu. Ikiwa Keet itazinduliwa kwa usahihi, inamaanisha kuwa usakinishaji wako wa Pears unafanya kazi kikamilifu.


![Image](assets/fr/12.webp)


Mfumo wako wa Linux sasa uko tayari kuendesha na kukaribisha programu-tumizi za peer-to-peer na Pears.


## 3. Jinsi ya Kufunga Pears kwenye Windows


Kusakinisha Pears kwenye Windows ni rahisi tu kama kwenye Linux lakini inahitaji zana mahususi.


*Ikiwa unatumia Linux na tayari umesakinisha Pears, unaweza kuruka moja kwa moja hadi **Hatua ya 5**.*


### 3.1. Fungua PowerShell kama Msimamizi


Kwanza, uzindua PowerShell na haki za msimamizi:



- Bonyeza kwenye menyu ya Mwanzo;
- Andika "PowerShell";
- Bonyeza kulia kwenye "*Windows PowerShell*";
- Chagua "*Run kama msimamizi*".


![Image](assets/fr/15.webp)


### 3.2. Pakua NVS


Pears imesakinishwa kupitia *npm*, kidhibiti kifurushi cha *Node.js*. Kwenye Windows, mbinu inayopendekezwa na Holepunch ni kutumia *NVS* (*Node Version Switcher*), ambayo ni thabiti zaidi kuliko *NVM* kwenye mfumo huu.


Katika PowerShell, endesha amri ifuatayo ili kusakinisha toleo jipya zaidi la *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Sakinisha Node.js


Baada ya usakinishaji, anzisha upya PowerShell, kisha ingiza amri ifuatayo:


```powershell
nvs
```


Unapaswa kuona orodha ya matoleo yanayopatikana ya *Node.js*. Chagua ya kwanza kwa kubonyeza kitufe cha `a` kwenye kibodi yako.


![Image](assets/fr/17.webp)


*Node.js* sasa imesakinishwa.


![Image](assets/fr/18.webp)


### 3.4. Thibitisha Usakinishaji


Hakikisha *Node.js* na *npm* zinapatikana:


```powershell
node -v
npm -v
```


Amri zote mbili zinapaswa kurudisha nambari ya toleo.


![Image](assets/fr/19.webp)


### 3.5. Sakinisha Pears na npm


Mara tu *Node.js* na *npm* zinapatikana, sakinisha **Pears CLI** kimataifa kwenye mfumo wako:


```powershell
npm install -g pear
```


Hii inasakinisha `pear` binary katika saraka yako ya kimataifa ya *npm*.


![Image](assets/fr/20.webp)


### 3.6. Thibitisha na Anzisha Pears


Mara tu usakinishaji ukamilika, endesha:


```powershell
pear
```


Wakati wa uzinduzi wa kwanza, Pears itapakua kiotomatiki vipengee vinavyohitajika kutoka kwa mtandao wa rika-kwa-rika. Mchakato huu unaweza kuchukua muda mfupi.


![Image](assets/fr/21.webp)


Ikiwa kila kitu kilikwenda vizuri, unapaswa kuona menyu ya usaidizi ya Pears CLI na orodha ya amri ndogo zinazopatikana (kukimbia, seed, maelezo ...).


### 3.7. Jaribu Pears na Keet


Ili kuthibitisha kwamba Pears inafanya kazi kikamilifu, unaweza kuzindua programu iliyopo ya P2P inayopatikana kwenye mtandao, kama vile Keet - programu huria ya kutuma ujumbe na mikutano ya video iliyotengenezwa na Holepunch.


```bash
pear run pear://keet
```


Amri hii hupakia programu ya Keet moja kwa moja kutoka kwa mtandao wa Pears, bila kutumia seva kuu yoyote. Ikiwa Keet itazinduliwa kwa mafanikio, inamaanisha kuwa usakinishaji wako wa Pears unafanya kazi kikamilifu.


![Image](assets/fr/22.webp)


Mfumo wako wa Windows sasa uko tayari kufanya kazi na kukaribisha programu-tumizi za peer-to-peer na Pears.


## 4. Jinsi ya kusakinisha Pears kwenye macOS


Kufunga Pears kwenye macOS ni sawa na Linux lakini inahitaji marekebisho machache maalum kwa mazingira ya Apple. Hebu tupitie hatua hizi pamoja.


*Ikiwa unatumia Linux au Windows na tayari umesakinisha Pears, unaweza kuruka moja kwa moja hadi **Hatua ya 5**.*


### 4.1. Angalia Mahitaji ya Mfumo


Kabla ya usakinishaji, hakikisha kuwa *Vyombo vya Mstari wa Amri ya Xcode* vimesakinishwa kwenye mfumo wako. Kifurushi hiki hutoa zana muhimu za ujenzi za *Node.js* na tegemezi zake.


Ili kufanya hivyo, fungua terminal kwa kutumia njia ya mkato `Cmd + Space bar`, chapa `Terminal`, na ubonyeze `Enter`. Kisha, endesha amri ifuatayo kwenye terminal ili kuisakinisha:


```bash
xcode-select --install
```


Ikiwa zana tayari zimewekwa kwenye mfumo wako, macOS itakujulisha.


### 4.2. Sakinisha NVM


Pears inasambazwa kupitia *npm*, kidhibiti kifurushi cha *Node.js*. Ingawa Pears haitegemei moja kwa moja *Node.js* kufanya kazi, inahitajika ili kusakinisha. Mbinu inayopendekezwa ya kusakinisha *Node.js* kwenye macOS ni *NVM* (*Kidhibiti cha Toleo la Node*), ambayo hukuruhusu kudhibiti matoleo mengi ya Node kwa wakati mmoja.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Kisha pakia upya terminal yako ili kuamilisha *NVM*:


```bash
source ~/.zshrc
```


Ikiwa unatumia *bash* badala ya *zsh*, endesha:


```bash
source ~/.bashrc
```


Ifuatayo, angalia kuwa *NVM* imewekwa kwa usahihi:


```bash
nvm --version
```


Terminal yako inapaswa kuonyesha toleo la *NVM* lililosanikishwa.


### 4.3. Sakinisha Node.js na npm


Ifuatayo, sakinisha toleo thabiti la *Node.js* (kwa mfano, toleo la sasa la LTS):


```bash
nvm install --lts
```


Mara tu usakinishaji ukamilika, thibitisha matoleo yaliyosakinishwa:


```bash
node -v
npm -v
```


Amri zote mbili zinapaswa kurudisha nambari ya toleo.


### 4.4. Sakinisha Pears na npm


Mara tu *npm* inapopatikana, unaweza kusakinisha Pears CLI duniani kote kwenye mfumo wako. Hii itakuruhusu kutekeleza amri ya `pear` kutoka saraka yoyote.


```bash
npm install -g pear
```


### 4.5. Anzisha Pears


Baada ya usakinishaji, endesha tu amri ifuatayo kwenye terminal yako:


```bash
pear
```


Wakati wa uzinduzi wa kwanza, Pears huunganisha kwenye mtandao wa rika-kwa-rika ili kupakua vipengele muhimu. Mchakato huu hauhitaji seva kuu yoyote - faili hutolewa moja kwa moja kutoka kwa programu zingine.


Mara tu upakuaji utakapokamilika, endesha tena amri ili kuthibitisha kuwa kila kitu kinafanya kazi:


```bash
pear
```


Ikiwa kila kitu kimewekwa kwa usahihi, menyu ya usaidizi ya Pears itaonekana na orodha ya amri zinazopatikana.


### 4.6. Jaribu Pears na Keet


Ili kuthibitisha kwamba Pears inafanya kazi kikamilifu, unaweza kuzindua programu ya P2P ambayo tayari inapatikana kwenye mtandao, kama vile Keet, programu huria ya kutuma ujumbe na video kutoka Holepunch.


```bash
pear run pear://keet
```


Amri hii hupakia programu ya Keet moja kwa moja kutoka kwa mtandao wa Pears, bila kutumia seva kuu. Ikiwa Keet itazinduliwa kwa mafanikio, inamaanisha kuwa usakinishaji wako wa Pears unafanya kazi kikamilifu.


Mfumo wako wa macOS sasa uko tayari kutumika na kukaribisha programu-tumizi za rika-kwa-rika na Pears.


## 5. Jinsi ya Kutumia Mpango ₿ Academy on Pears


Mara tu Pears inaposakinishwa na kuendeshwa, unaweza kuzindua moja kwa moja jukwaa la **Mpango ₿ Academy** kupitia mtandao wa P2P. Endesha tu amri ifuatayo kwenye terminal yako (amri hiyo hiyo inafanya kazi kwenye Linux, Windows, na macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Baada ya upakiaji kukamilika, Panga ₿ Chuo kitafunguliwa ndani ya mazingira yako ya Pears, tayari kutumika kama tovuti asili - lakini bila utegemezi wowote wa seva kuu.


![Image](assets/fr/14.webp)


## 6. Jinsi ya Kupanga Mbegu ₿ Academy on Pears


Katika mtandao wa Pears, hadi *seed* programu-tumizi inamaanisha kuisambaza tena kwa programu zingine kutoka kwa mashine yako mwenyewe. Kwa vitendo, unapopanga seed ₿ Academy, kompyuta yako inakuwa chanzo cha data ambacho huruhusu watumiaji wengine kupakua programu bila kutegemea seva kuu.


Utaratibu huu huimarisha uthabiti na upinzani wa udhibiti wa programu yetu kwenye mtandao wa Pears. Kadiri seed inavyokuwa na programu rika nyingi, ndivyo inavyopatikana zaidi na kugatuliwa, hata kama baadhi ya nodi asili zinakwenda nje ya mtandao.


Ili kusaidia kusambaza Plan ₿ Academy, endesha tu amri ifuatayo:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Mradi amri hii itaendelea kutumika, kifaa chako kitashiriki katika kusambaza faili za programu. Ukifunga terminal, mchakato wa kushiriki utaacha.


Ili kuendelea kupanda baada ya kuanza upya, unaweza kuendesha amri chinichini au kuunda huduma ya mfumo - kwa mfano, huduma ya mfumo kwenye Linux, LaunchAgent kwenye macOS, au kazi iliyoratibiwa kwenye Windows. Mbinu hizi huhakikisha kuwa programu ya Plan ₿ Academy inaanza tena kupanda kiotomatiki wakati mfumo unapowashwa.


Asante kwa kuchangia usambazaji uliogatuliwa wa Plan ₿ Academy on Pears na kusaidia kufanya elimu ya Bitcoin iwe sugu kwa udhibiti!