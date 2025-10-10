---
name: Dojo
description: Njia huria ya Bitcoin ya faragha na uhuru
---

![cover](assets/cover.webp)



*Mafunzo haya yanatokana na [hati rasmi ya Ashigaru](https://ashigaru.rs/docs/), ambayo nimechukua na kuipanua. Nimeandika upya sehemu zote ili kuboresha uwazi, nimeongeza maelezo ya kina zaidi, pamoja na vielelezo kwa wanaoanza, ili kufanya usakinishaji na utumiaji uwe rahisi kueleweka.*



---

Dojo ni programu huria iliyoundwa kufanya kazi kama seva ya nyuma kwa pochi fulani za faragha za Bitcoin, kulingana na nodi ya Bitcoin core. Kihistoria, iliundwa ili kufanya kazi na Samourai Wallet, Wallet ya simu ya mkononi ambayo ilitoa vipengele vya hali ya juu vya faragha kama vile Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet sasa imefungwa kufuatia kukamatwa kwa wasanidi wake, lakini mrithi wake wa jumuiya, **Ashigaru Wallet**, ameendelea kutegemea udhibiti kamili wa watumiaji wa Do. ya data zao wakati wa kutumia Bitcoin.



![Image](assets/fr/01.webp)



Kwa vitendo, Dojo hufanya kama lango kati ya Wallet yako na mtandao wa Bitcoin. Bila Dojo, Wallet ya simu nyepesi italazimika kuuliza maswali kwenye seva za watu wengine ili kupata hali ya UTXO zako na historia yako, au kutangaza miamala yako. Hii inamaanisha utegemezi na uvujaji wa data nyeti kwa seva ya watu wengine (anwani zinazotumika, kiasi, marudio ya malipo, n.k.). Ukiwa na Dojo, unapangisha seva hii mwenyewe, iliyounganishwa moja kwa moja na nodi yako ya Bitcoin. Kwa njia hii, maombi yako yote ya kwingineko yanapitia miundombinu ambayo unadhibiti, bila waamuzi, inayoimarisha usiri na uhuru wako.



## Mahitaji ya kuanzisha Dojo



Kusanidi seva ya Dojo hakuhitaji mashine yenye nguvu zaidi. Mtu yeyote aliye na kompyuta ya kiwango cha kuingia, muunganisho thabiti wa Mtandao na uwezo wa kuiacha ikiwashwa kila wakati (24/7) anaweza kusanidi Dojo inayofanya kazi.



### Chagua aina ya mashine yako



Unaweza kutumia:




- Laptop;
- kompyuta ya mezani;
- Kompyuta ndogo (k.m. Intel NUC, Lenovo Thincentre Tiny...).



Kila chaguo lina faida na hasara zake:




- Bei: Kompyuta ndogo iliyorekebishwa au kompyuta ya mezani mara nyingi itakuwa nafuu kuliko kompyuta ndogo ndogo.
- Footprint: Mini-PC inachukua nafasi kidogo.
- Nguvu ya Supply: kompyuta ya mkononi ina faida ya betri, ambayo inamaanisha kuwa haitazimika katika tukio la kukata nguvu, tofauti na mini-PC.
- Uboreshaji: barbones kwa ujumla hukuruhusu kuongeza kumbukumbu au kubadilisha kwa urahisi diski ya Hard.



Kwa habari zaidi juu ya kuchagua kifaa chako, ninapendekeza uchukue kozi hii:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Vifaa vilivyopendekezwa



Hakuna haja ya kununua mashine mpya. Kompyuta iliyorekebishwa iliyo na vipimo vilivyo hapa chini itatoa utendakazi bora zaidi kuliko vifaa vya kielektroniki vya bodi moja (kama vile Raspberry Pi).



**Maagizo ya chini kabisa:**




- Usanifu wa X86-64 (64-bit processor).
- Kichakataji cha 2 GHz dual-core au haraka zaidi.
- 8 GB RAM kiwango cha chini.
- 2 TB au zaidi NVMe SSD (kuhifadhi Blockchain ya Bitcoin na indexes muhimu).



**Mfumo wa uendeshaji unaopendekezwa: **




- Usambazaji wa msingi wa Debian, kama Ubuntu 24.04 LTS.



**Kifaa kinachopendekezwa:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- nk.



Inawezekana kabisa kuendesha seva ya Dojo kwenye usanidi mwingine wa maunzi. Hata hivyo, ili kupata utendaji bora na matatizo ya kikomo, tunakushauri kufuata mapendekezo hapo juu.



Katika somo hili, nitakuwa nikitumia ThinkCentre Tiny ya zamani yenye kichakataji cha Intel Pentium Dual-Core G4400T, RAM ya GB 8 na SSD ya TB 2.



## 1 - Kusakinisha Ubuntu



*Ikiwa ungependa kusakinisha Dojo kwenye kifaa ambacho tayari kimesanidiwa, unaweza kuruka hatua hii na kuendelea moja kwa moja hadi hatua ya 2.*



Baada ya kuandaa vifaa vilivyochaguliwa, ni wakati wa kufunga mfumo wa uendeshaji. Unaweza kutumia usambazaji wowote wa Debian, lakini ninapendekeza uchague toleo la LTS la Ubuntu, kwani linafaa kabisa kwa madhumuni yetu. Hapa kuna hatua za kufuata:



### 1.1. unda ufunguo wa USB unaoweza kuwashwa



Kutoka kwa kompyuta inayofanya kazi tayari (mashine yako ya kawaida), pakua picha ya Ubuntu LTS ISO [kutoka tovuti rasmi](https://ubuntu.com/download/desktop) (`24.04` wakati wa kuandika, lakini chukua ya hivi punde zaidi ikiwa nyingine inapatikana).



![Image](assets/fr/02.webp)



Weka ufunguo wa USB wa angalau GB 8 kwenye kompyuta hii, kisha uunde ufunguo unaoweza kuwashwa kwa kutumia programu kama vile [Balena Etcher](https://etcher.balena.io/). Chagua picha ya Ubuntu ISO ambayo umepakua hivi punde, chagua kitufe cha USB kama kifaa lengwa, kisha anza mchakato wa kuunda (kuwa mvumilivu, inaweza kuchukua dakika kadhaa).



![Image](assets/fr/03.webp)



Ingiza ufunguo wa USB unaoweza kuwashwa kwenye kompyuta iliyozimwa (ile ambayo ungependa kuendesha Dojo). Anzisha mashine na ubonyeze mara moja **F12** au **F10** kwenye kibodi yako (kulingana na mfano) ili kufikia orodha ya boot. Kisha chagua ufunguo wako wa USB kama kifaa cha kipaumbele katika mpangilio wa kuwasha kompyuta.



![Image](assets/fr/04.webp)



### 1.2. kufunga mfumo wa uendeshaji



Skrini ya nyumbani ya Ubuntu inaonekana. Chagua "Jaribu au Sakinisha Ubuntu*".



![Image](assets/fr/05.webp)



Kisha fuata mchakato wa usakinishaji wa Ubuntu wa kawaida:




- Chagua lugha.
- Chagua aina ya kibodi.
- Ikiwa umeunganishwa kupitia kebo ya RJ45, hakuna haja ya kusanidi Wi-Fi.
- Bofya kwenye "* Sakinisha Ubuntu*" na uangalie chaguo la kusakinisha programu ya tatu (viendeshi vya Wi-Fi, codecs za multimedia, nk).
- Wakati mchawi anauliza aina ya usakinishaji, chagua "* Futa diski na usakinishe Ubuntu*". **Onyo**: operesheni hii itafuta kabisa yaliyomo kwenye diski. Angalia kwa uangalifu kwamba diski uliyochagua inalingana na NVMe SSD iliyokusudiwa kwa Dojo.
- Unda jina rahisi la mtumiaji (k.m. "*loic*").
- Peana jina kwa mashine (k.m. "*dojo-nodi*").
- Weka nenosiri dhabiti na uliweke salama.
- Washa chaguo la "*Omba nenosiri langu kuingia*" ili kuimarisha usalama.
- Onyesha saa za eneo lako, kisha ubofye "*Sakinisha*".
- Subiri usakinishaji ukamilike. Baada ya kukamilika, mfumo utaanza upya kiotomatiki.
- Ondoa ufunguo wa usakinishaji wa USB wakati wa kuanzisha upya kompyuta.



Kwa maelezo zaidi juu ya mchakato wa usakinishaji wa Ubuntu, tafadhali tazama mafunzo yetu yaliyojitolea:



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. sasisho la mfumo



Baada ya boot ya kwanza, fungua terminal kwa kutumia mchanganyiko muhimu ***Ctrl + Alt + T*** na uendesha amri zifuatazo ili kusasisha mfumo:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Ufungaji wa jengo la nje



Ili Dojo ifanye kazi vizuri, matofali fulani ya programu lazima yawepo kwenye mfumo wako. Hizi hutumika kudhibiti hazina za programu, mawasiliano, upunguzaji wa kumbukumbu na utekelezaji wa Dojo ndani ya vyombo vya Docker. Shughuli hizi zote zinafanywa katika terminal.



### 2.1. Maandalizi



Amri ifuatayo inakurudisha kwenye folda yako ya kibinafsi. Hii ni mazoezi mazuri kabla ya kuendesha safu ya usakinishaji.



```bash
cd ~/
```



Kabla ya kusakinisha programu yoyote, hakikisha kwamba hifadhidata ya programu inayopatikana kwenye mashine yako imesasishwa. Hii inaepuka kusakinisha matoleo ya kizamani.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. kufunga huduma



Zana kadhaa zinahitajika kuongezwa kwenye mfumo:




- `apt-transport-https`: hukuruhusu kupakua pakiti kwa usalama kupitia HTTPS
- `ca-vyeti`: inadhibiti vyeti vinavyohitajika kwa miunganisho iliyosimbwa kwa njia fiche
- `curl`: kupata faili kutoka kwa Mtandao
- `gnupg-agent`: kwa usimamizi wa ufunguo wa GPG
- software-properties-common`: hutoa huduma za kudhibiti hazina za APT
- `unzip`: fungua faili katika umbizo la ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Wakati wa ufungaji, mfumo unaweza kukuuliza uthibitisho. Bonyeza kitufe cha "*y*", kisha bonyeza "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. kufunga Torsocks



Torsocks huwezesha amri fulani kutekelezwa kupitia mtandao wa Tor, kuboresha usiri wa mawasiliano.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. sasisha Docker na Docker Compose



Dojo huendesha ndani ya vyombo vya Docker. Hii ina maana kwamba kila huduma imetengwa katika mazingira ya kujitegemea, kurahisisha matengenezo na usalama. Ili kufanya hivyo, unahitaji kufunga Docker na chombo cha Kutunga Docker, ambacho kinakuwezesha kusimamia vyombo kadhaa kwa wakati mmoja.



#### Ongeza ufunguo wa kusaini wa Docker



Docker hutoa ufunguo wake wa saini ya dijiti. Kuiongeza huthibitisha uhalisi wa vifurushi vilivyopakuliwa.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Hazina rasmi ya Docker imeongezwa



Ifuatayo, unahitaji kuwaambia mfumo wapi kupata vifurushi rasmi vya Docker. Amri hii inaongeza hazina mpya kwa usanidi wa kidhibiti kifurushi chako.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Kufunga Docker na Docker Compose



Vipengele kuu vya Docker sasa vinaweza kusanikishwa.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Idhini ya mtumiaji



Kwa chaguo-msingi, amri tu zilizotekelezwa na haki za msimamizi zinaweza kuzindua Docker. Kwa urahisi zaidi, ninapendekeza kuongeza mtumiaji wako wa sasa kwenye kikundi cha "*docker*". Hii hukuruhusu kutumia Docker bila kulazimika kuandika `sudo` kila wakati.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Uundaji wa mtumiaji mmoja (si lazima)



Iwapo ungependa kuboresha usalama wa mfumo wako, ninapendekeza uunde mtumiaji tofauti kwa ajili ya kuendesha Dojo pekee. Utengano huu huzuia hatari: ikiwa tatizo la usalama litatokea katika Dojo, halitahatarisha akaunti yako kuu moja kwa moja.



### 3.1. kuunda akaunti ya mtumiaji



Amri ifuatayo inaunda mtumiaji mpya anayeitwa "*dojo*". Mtumiaji huyu atakuwa na saraka ya nyumbani `/home/dojo` na ufikiaji wa terminal ya bash. Pia itaongezwa kwa kikundi cha sudo ili kuwezesha utekelezaji wa amri za admin.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Kuweka nenosiri



Ni muhimu kuweka nenosiri thabiti kwa akaunti hii. Kwa kweli, unapaswa kutumia kidhibiti cha nenosiri kama vile Bitwarden hadi generate mchanganyiko mrefu, wa Hard-kukisia.



```bash
sudo passwd dojo
```



Kisha mfumo utakuuliza uweke nenosiri ulilochagua, kisha uthibitishe kwa mara ya pili.



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Idhinisha mtumiaji kutumia Docker



Ili kuwezesha mtumiaji "*dojo*" kuzindua vyombo vinavyohitajika ili kuendesha Dojo, ni lazima aongezwe kwenye kikundi cha Doka. Hii inaepuka kutangulia kila amri na `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Anzisha upya mfumo



Ili mabadiliko ya kikundi yaanze, mashine lazima ianzishwe tena.



```bash
sudo reboot
```



### 3.5. Ingia na mtumiaji mpya



Wakati mfumo unaanza upya, ingia kwa kuingia kwa ***dojo*** na nenosiri ulilofafanua awali. Hatua zote zinazofuata lazima zifanywe kutoka kwa akaunti hii maalum.



## 4. Pakua na uangalie Dojo



Kabla ya kusakinisha Dojo, ni muhimu kuhakikisha kuwa faili zimetoka kwa msanidi rasmi na kwamba hazijarekebishwa. Hatua hii inategemea matumizi ya PGP na heshi ili kuthibitisha uhalisi na uadilifu wa faili.



### 4.1. ingiza ufunguo wa PGP wa msanidi



Pakua ufunguo wa umma wa msanidi programu kupitia Tor na uilete kwenye mnyororo wa vitufe wa karibu nawe. Ufunguo huu utatumika kuthibitisha sahihi zinazohusishwa na faili za Dojo.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. pakua toleo jipya zaidi la Dojo



Rejesha kumbukumbu iliyobanwa iliyo na msimbo wa chanzo wa Dojo. Katika mfano huu, toleo la hivi punde zaidi ni `1.27.0`: rekebisha amri kulingana na [toleo jipya zaidi hapa kwenye hazina rasmi ya GitHub](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Pakua alama za vidole na saini



Watengenezaji huchapisha faili inayoorodhesha alama za vidole dijitali za kumbukumbu, pamoja na faili iliyotiwa saini na ufunguo wao wa PGP. Zipakue ili kulinganisha faili zako ndani ya nchi.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Angalia saini ya PGP



Hakikisha kuwa faili ya alama ya vidole imetiwa saini na ufunguo ulioletwa.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Matokeo sahihi yanaonyesha saini halali yenye ufunguo `E53AD419B242822F19E23C6D3033D463D6E544F6` na Address `dojocoder@pm.me` husika. Onyo linaweza kuonekana likisema kwamba ufunguo haujathibitishwa: unaweza kuupuuza.



Ikiwa, kwa upande mwingine, saini ni batili, mara moja uacha mchakato wa ufungaji na uanze tena tangu mwanzo.



![Image](assets/fr/17.webp)



### 4.5. Angalia uadilifu kwenye kumbukumbu



Kokotoa alama ya vidole ya SHA256 ya faili iliyopakuliwa, kisha ufungue faili ya alama ya vidole ili kulinganisha thamani hizo mbili.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Ikiwa alama za vidole mbili zinafanana, unaweza kuwa na uhakika kwamba kumbukumbu haijabadilishwa. Ikiwa ni tofauti, usiende mbali zaidi na ufute faili.



![Image](assets/fr/18.webp)



### 4.6. Dondoo na upange faili



Baada ya uthibitishaji kukamilika, unaweza kufungua kumbukumbu na kuandaa folda iliyowekwa kwa usakinishaji wa Dojo.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Safisha faili zisizo za lazima



Futa faili na kumbukumbu za muda hazihitajiki tena ili kuweka mazingira yako safi.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Usanidi wa Dojo



Dojo ni seva ya nyuma inayoleta pamoja huduma kadhaa ili kuingiliana na kwingineko yako na kudhibiti nodi yako ya Bitcoin. Usanidi wake unaweza kuwa mgumu, lakini mradi hutoa njia iliyorahisishwa ambayo husakinisha kiotomatiki na kusanidi vifaa vifuatavyo:




- Dojo (API kuu)
- Bitcoin core (nodi kamili ya Bitcoin)
- BTC-RPC Explorer (mtandao Block explorer)
- Fulcrum Indexer (uorodheshaji wa haraka wa vitalu na shughuli)
- Seva ya Fulcrum Electrum inapatikana kwenye mtandao wa Tor
- Seva ya Fulcrum Electrum inapatikana kwenye mtandao wa ndani
- Hati za utawala



### 5.1. vitambulisho vya utawala



Ili kupata ufikiaji wa huduma mbalimbali, unahitaji generate vitambulisho kadhaa vya kipekee:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mySQL_USER
- `MYSQL_PASSWORD`
- noODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Vitambulishi hivi **lazima viwe vya kipekee** (hii ni muhimu sana: hupaswi kutumia nenosiri lile lile kwa huduma kadhaa), linalojumuisha nambari, herufi kubwa na herufi ndogo (alphanumeric), na viwe na urefu wa takriban vibambo 40 ili kuhakikisha usalama wa hali ya juu. Kwa mara nyingine tena, ninapendekeza sana matumizi ya meneja wa nenosiri.



### 5.2. Fikia faili za usanidi



Faili za usanidi za Dojo ziko kwenye folda ya `conf/`. Hamisha hadi saraka hii:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Usanidi wa Bitcoin core



Fungua faili ya usanidi ya Bitcoin core na hariri ya maandishi ya nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



Katika faili hii, ingiza vitambulisho vilivyotengenezwa:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Badilisha `kitambulisho chako-hapa` na `nenosiri-yako-hapa` na kuingia kwako mwenyewe (kwa neno la siri dhabiti).***



Unaweza pia kurekebisha saizi ya kumbukumbu ya kache inayotumiwa na Bitcoin core kuboresha utendaji (unaweza kutumia zaidi ikiwa una RAM nyingi):



```
BITCOIND_DB_CACHE=2048
```



Ili kuhifadhi mabadiliko yako na kufunga kihariri :




- bonyeza `Ctrl + X
- chapa `y`
- kisha bonyeza "*Enter*"



### 5.4. Usanidi wa MySQL



Kisha fungua usanidi wa hifadhidata ya MySQL:



```bash
nano docker-mysql.conf.tpl
```



Tafadhali weka maelezo yako ya kuingia:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Badilisha `kitambulisho chako-hapa` na `nenosiri lako-hapa` na kuingia kwako mwenyewe (kwa manenosiri thabiti na ya kipekee).***



Hifadhi kwa njia ile ile (`Ctrl + X`, `y`, "*Ingiza*").



![Image](assets/fr/23.webp)



### 5.5. Usanidi wa kielezo cha Fulcrum



Fungua faili ifuatayo:



```bash
nano docker-indexer.conf.tpl
```



Ongeza vigezo ili kuamilisha Fulcrum na kuiunganisha kwa usahihi kwenye Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Ifuatayo, kuna uwezekano 2, kulingana na usanidi wako. Ikiwa Dojo imesakinishwa kwenye mashine tofauti na kompyuta yako ya kila siku (kwenye mashine maalum, seva...), weka IP yake Address katika mtandao wako wa karibu, kwa mfano :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Ili kujua IP ya ndani ya Address ya mashine yako, fungua terminal nyingine na uweke amri ifuatayo:



```bash
hostname -I
```



Uwezekano wa pili: ikiwa Dojo inaendeshwa moja kwa moja kwenye kompyuta yako ya kibinafsi ya kila siku, weka thamani chaguo-msingi ikiwa tayari iko kwenye faili ya usanidi :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Hifadhi na uondoke kwenye kihariri (`Ctrl + X`, `y`, "*Ingiza*").



### 5.6. Usanidi wa huduma ya nodi



Hatimaye, fungua usanidi wa huduma kuu ya Dojo:



```bash
nano docker-node.conf.tpl
```



Tafadhali weka maelezo yako ya kuingia:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Badilisha `nenosiri-yako-hapa` na kitambulisho chako mwenyewe (kwa manenosiri thabiti na ya kipekee).***



![Image](assets/fr/26.webp)



Kisha washa kiashiria cha ndani:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Hifadhi na uondoke kwenye kihariri (`Ctrl + X`, `y`, "*Ingiza*").



### 5.7. Usimamizi wa kuingia



Mara tu usanidi utakapokamilika, si lazima kuhifadhi vitambulisho vyote vilivyotolewa. Ya pekee ambayo lazima kabisa kuokolewa ni:



```
NODE_ADMIN_KEY
```



Kuingia huku kutakuwezesha kuingia baadaye kwenye zana ya matengenezo ya Dojo. Maingizo mengine yote yanaweza kuondolewa kutoka kwa kidhibiti chako cha nenosiri au madokezo yaliyoandikwa kwa mkono. Zinasalia kufikiwa kutoka kwa faili za usanidi za Dojo iwapo utahitaji kuzirejesha katika siku zijazo.



## 6. Ufungaji wa Dojo



Katika hatua hii, Dojo itasakinishwa na kuanza kutumika kwenye mashine yako. Operesheni itazindua huduma kadhaa (Bitcoin core, indexer ya Fulcrum, backend ya Dojo, nk.) na kuanzisha usawazishaji kamili wa Blockchain Bitcoin. Hii inaweza kuchukua siku kadhaa, kulingana na maunzi yako na muunganisho wa Mtandao.



### 6.1. Angalia kuwa Docker inafanya kazi vizuri



Kabla ya kuanza usakinishaji, hakikisha kuwa Docker inafanya kazi. Endesha amri ifuatayo:



```bash
docker run hello-world
```



Amri hii inapakua na kuzindua chombo kidogo cha majaribio. Ikiwa kila kitu kitafanya kazi kwa usahihi, unapaswa kuona ujumbe sawa na:



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Ikiwa ujumbe huu haujaonyeshwa, anza kwa kuwasha tena mashine yako na:



```bash
sudo reboot
```



Kisha ingia tena kwenye akaunti yako ya **dojo** na utekeleze amri ya jaribio tena. Ikiwa kosa litaendelea, Docker haijasakinishwa kwa usahihi. Katika hali hii, rudi kwenye hatua `2.4.` ya kusakinisha Docker na uangalie kila amri kwa makini.



### 6.2. Nenda kwenye saraka ya usakinishaji ya Dojo



Hati zinazohitajika kwa usakinishaji ziko kwenye folda ya `my-dojo`. Hamisha hadi saraka hii:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Tumia amri ya `ls` ili kuangalia kama faili ya `dojo.sh` ipo. Hii ndiyo script kuu inayoendesha usakinishaji wa Dojo na uzinduzi wa huduma zake zote.



![Image](assets/fr/29.webp)



### 6.3. Anza usakinishaji



Anzisha usakinishaji kwa kuendesha :



```bash
./dojo.sh install
```



Thibitisha usakinishaji kwa kubonyeza `y` na kisha "*Ingiza*".



![Image](assets/fr/30.webp)



Hati hii itakuwa:




- pakua na uzindue vyombo muhimu vya Docker,
- anzisha Bitcoin core na anza kusawazisha Blockchain,
- anzisha kiashiria cha Fulcrum ili kufuatilia shughuli na anwani,
- washa mandhari ya nyuma ya Dojo na API zake.



Utaona mtiririko thabiti wa kumbukumbu zinazosogezwa, zikiwa na marejeleo ya rangi kama vile `bitcoind`, `soroban`, `nodejs` au `fulcrum`. Usogezaji huu unaonyesha kuwa Dojo iko tayari kufanya kazi na inaanza kutekeleza huduma mbalimbali.



![Image](assets/fr/31.webp)



### 6.4. Ondoka kwenye onyesho la kumbukumbu



Kumbukumbu huonekana kwa wakati halisi kwenye terminal yako. Ili kurudi kwenye kidokezo cha amri wakati Dojo inafanya kazi chinichini, andika :



```
Ctrl + C
```



Usijali: kusimamisha onyesho la logi hakuzuii huduma. Docker inaendelea kuendesha Dojo nyuma (ni wazi hauitaji kusimamisha kompyuta ikiwa unataka IBD iendelee).



### 6.5. Kuelewa *Upakuaji wa Kizuizi cha Awali* (IBD)



Inapowashwa, Bitcoin core lazima ipakue na kuthibitisha Blockchain nzima tangu 2009. Hatua hii inaitwa ***Upakuaji wa Kuzuia Awali* (IBD)**. Ni muhimu, kwani huwezesha nodi yako ya Dojo kuthibitisha kila kizuizi cha Bitcoin na muamala kwa kujitegemea.



Muda wa maingiliano haya inategemea mambo kadhaa:




- nguvu ya kichakataji chako na kiasi cha kumbukumbu ya RAM inayopatikana,
- kasi ya diski yako,
- idadi na ubora wa wenzao nodi yako inaunganishwa nao,
- kasi ya muunganisho wako wa Mtandao.



Kwa mazoezi, operesheni hii kwa ujumla huchukua kati ya siku **2 na 7**. Katika kipindi hiki, unaweza kuacha mashine yako ikiendelea kufanya kazi. Kadiri mashine inavyowashwa, ndivyo maingiliano yatakavyokamilishwa kwa haraka. Ninakushauri uangalie hali ya maingiliano mara kwa mara kwa kushauriana na kumbukumbu za Bitcoin core, au kwa kutumia zana ya matengenezo ya Dojo mara moja imewekwa (tazama sehemu inayofuata).



Ili kuongeza maarifa yako ya IBD na, kwa ujumla zaidi, ya uendeshaji na jukumu la nodi yako ya Bitcoin, ninapendekeza uangalie kozi hii:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Ufuatiliaji wa maingiliano



Wakati wa kufunga Dojo kwa mara ya kwanza, unahitaji kusubiri shughuli kuu mbili ili kukamilika kikamilifu: upakuaji kamili wa Blockchain Bitcoin (*IBD*) na indexing ya Blockchain hii na Fulcrum. Kulingana na muunganisho wako na nguvu ya mashine, hii inaweza kuchukua siku kadhaa. Wakati huu, unaweza kufuatilia maendeleo ya mchakato ili kuhakikisha kuwa kila kitu kinaendelea vizuri.



Kuna njia mbili za kufuatilia hali ya maingiliano:




- matumizi ya Zana ya Matengenezo ya Dojo (au DMT), ambayo ni rahisi lakini inatoa maelezo machache wakati wa IBD;
- mashauriano ya moja kwa moja ya kumbukumbu za Dojo kwenye mashine yako, kiufundi zaidi lakini kwa usahihi zaidi.



### 7.1. Angalia kupitia Dojo Maintenance Tool (DMT)



Zana ya Matengenezo ya Dojo ni Interface salama, yenye msingi wa wavuti inayokuruhusu kufuatilia hali ya mtambo wako, na kufanya shughuli fulani. Ndiyo njia rahisi na inayoweza kufikiwa zaidi ya kufuatilia maendeleo ya IBD. Wakati wa awamu ya awali ya maingiliano, taarifa inayoonyeshwa inaweza kuwa na kikomo. Kwa mfano, DMT haionyeshi maendeleo ya kina ya uorodheshaji wa Fulcrum. Kwa upande mwingine, mara ulandanishi utakapokamilika, DMT itaonyesha wazi:




- taa zote kwenye Green;
- kizuizi cha mwisho kilichoidhinishwa kwa kila huduma (Node, Indexer, Dojo DB).



Ili kuipata, unahitaji kujua URL ya DMT yako na uunganishe nayo [kupitia kivinjari cha Tor](https://www.torproject.org/download/). Ili kufanya hivyo, fungua terminal na uende kwenye saraka ya `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Kisha endesha amri ifuatayo:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Kisha utaweza kufikia maelezo yote yanayohusiana na miunganisho ya Dojo yako kupitia Tor. Tunayovutiwa nayo hapa ni URL ifuatayo:



```
Dojo API and Maintenance Tool =
```



Ili kufikia DMT kutoka kwa mashine yoyote kwenye mtandao wowote (hata kwa mbali), fungua Kivinjari cha Tor na uweke URL hii ikifuatiwa na `/admin`. Kwa mfano, ikiwa URL yako ni `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, utahitaji kuingia kwenye upau wa [Tor Browser](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Tafadhali weka Address hii kwa siri kabisa



Kisha utaelekezwa kwenye ukurasa wa uthibitishaji. DMT imeingia kwa kutumia `NODE_ADMIN_KEY` nenosiri ulilotengeneza awali.



![Image](assets/fr/33.webp)



Ukishaingia, unaweza kufikia *Zana ya Matengenezo ya Dojo*! Wakati wa IBD, unaweza kuona maelezo ya "*Uzuiaji wa Hivi Punde*" kwenye menyu ya "*Full node*", ambayo inakuwezesha kujua hali ya sasa ya nodi yako ya Bitcoin.



![Image](assets/fr/34.webp)



Kumbuka kualamisha Address hii kwenye Kivinjari cha Tor kwa urejeshaji rahisi baadaye.



Mara tu Dojo yako ikisawazishwa kikamilifu, unapaswa kuona ukaguzi wa Green ✅ kwenye viashirio vyote kwenye ukurasa wa nyumbani wa DMT.



### 7.2. Uthibitishaji kupitia kumbukumbu za Dojo



Njia ya pili ya kufuatilia maendeleo ya IBD yako ni kushauriana na kumbukumbu za mashine yako moja kwa moja. Mbinu hii inatoa ufuatiliaji sahihi zaidi, wa wakati halisi. Unaweza kuona jinsi Bitcoin core inavyoendelea katika upakuaji wa vizuizi, na jinsi Fulcrum inaviorodhesha.



Unganisha kwenye mashine inayopangisha Dojo yako na ufungue kituo. Amri zote zinafaa kutekelezwa kutoka kwenye saraka ya `my-dojo`. Jiweke kwenye folda hii:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Magogo ya Bitcoin core



Tazama kumbukumbu za Bitcoin core ili kufuatilia maendeleo ya IBD:



```bash
./dojo.sh logs bitcoind
```



Mwanzoni, utaona awamu ya kusawazisha mapema ya vichwa vya kuzuia:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Wakati takwimu hii itafikia 100%, Bitcoin core itaanza upakuaji kamili wa Blockchain. Utaona maendeleo ya IBD. Ili kujua urefu wa kizuizi cha sasa, angalia thamani iliyoonyeshwa na `urefu =`. Unaweza pia kufuata kitufe `progress=`, ambacho kinaonyesha asilimia ya maendeleo ya IBD.



![Image](assets/fr/36.webp)



Kama kawaida, ili kufunga kumbukumbu na kurudi kwa haraka ya amri, tumia mchanganyiko wa `Ctrl + C`.



#### Magogo ya Fulcrum



Bitcoin core inapomaliza kusawazisha mapema kwa kichwa, Fulcrum huanza kuorodhesha Blockchain kadri inavyoendelea. Tazama kumbukumbu zake na:



```bash
./dojo.sh logs fulcrum
```



Kisha utaona urefu wa kizuizi cha mwisho kilichoorodheshwa, kilichoonyeshwa baada ya `urefu:`, pamoja na asilimia ya maendeleo ya kuorodhesha.



![Image](assets/fr/37.webp)



### 7.3. Ufisadi wa hifadhidata ya Fulcrum



Fulcrum ni kiashiria chenye nguvu sana, lakini usakinishaji wake unaweza kuwa mgumu, sio kwa sababu ya usimamizi wake wa hifadhidata dhaifu. Katika tukio la kukatwa kwa nguvu au kuzimwa kwa ghafla kwa mashine wakati wa ulandanishi wa awali, hifadhidata ya kielezo inaweza kuharibika. Unaweza kuona hii, kwa mfano, ikiwa una kumbukumbu zifuatazo:



```bash
fulcrum | The database has been corrupted etc...
```



**Kumbuka:** Aina hii ya hitilafu inapaswa kusahihishwa na toleo lijalo la Fulcrum 2.0.



Hili likitokea kwako, hakuna athari kwa bitcoind (nodi yako ya Bitcoin): IBD yake itaendelea kuendelea bila kutumia Fulcrum. Hata hivyo, hutaweza kutumia Fulcrum hadi utakapofuta data yake iliyoharibika na uanze upya ulandanishi wake tangu mwanzo. Hivi ndivyo inavyofanya kazi:



Acha Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Futa tu chombo cha Fulcrum na ujazo:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Kwa kawaida jina ni `my-dojo_data-fulcrum`, ikiwa sivyo hivyo kwako, rekebisha jina lililorejeshwa kwa amri iliyotangulia.



Kisha uzindue tena Dojo na ujenge upya Fulcrum kuanzia mwanzo:



```bash
./dojo.sh upgrade
```



Kisha unaweza kuangalia kuwa Fulcrum inafanya kazi vizuri kwa kushauriana na magogo:



```bash
docker logs -f fulcrum
```




## 8. Kutumia Zana ya Matengenezo ya Dojo



Pindi fundo lako la Bitcoin linapokuwa limeoanishwa kwa kichwa kinachozunguka na Proof of Work nyingi zaidi, na Blockchain ikiwa imeorodheshwa kwa 100% na Fulcrum, unaweza kuanza kutumia Dojo yako.



Dojo yako inatoa anuwai ya vipengele, vinavyoboreshwa mara kwa mara kwa kila toleo jipya. Kwa maoni yangu, 2 muhimu zaidi ni:




- uwezekano wa kuunganisha Ashigaru Wallet yako ili kutumia nodi yako mwenyewe kushauriana na data ya Blockchain na kutangaza miamala yako,
- na Block explorer, ambayo inakupa ufikiaji wa taarifa kuhusu Blockchain Bitcoin bila kuanika data yako kwa mfano wa nje usiodhibiti.



Hebu tujue jinsi ya kuzitumia.


### 8.1. Unganisha Ashigaru kwenye Dojo yako



Kuunganisha Ashigaru Wallet yako kwenye Dojo yako ni rahisi sana: ukiwa kwenye DMT yako, fungua menyu ya "*Pairing*". Nambari ya QR inaonekana, ambayo unaweza kuchanganua moja kwa moja na programu ya Ashigaru.



![Image](assets/fr/38.webp)



Katika programu ya Ashigaru, mara ya kwanza unapoizindua baada ya kuunda au kurejesha Wallet yako, utaelekezwa kwenye ukurasa wa "*Sanidi seva yako ya Dojo*". Bonyeza "*Changanua QR*", kisha uchanganue msimbo wa QR unaoonyeshwa kwenye DMT yako.



![Image](assets/fr/39.webp)



Kisha bonyeza kitufe cha "*Endelea*".



![Image](assets/fr/40.webp)



Sasa umeunganishwa kwenye Dojo yako.



![Image](assets/fr/41.webp)



### 8.2. Kwa kutumia Block explorer



Dojo husakinisha kiotomatiki Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), ambayo huchota moja kwa moja data kutoka kwa nodi yako ya Bitcoin. Mgunduzi hukuwezesha kufikia taarifa ghafi kutoka Blockchain na Mempool yako kupitia mtandao unaoeleweka kwa urahisi wa Interface. Kwa hivyo unaweza, kwa mfano, kuangalia hali ya shughuli inayosubiri, angalia usawa wa Address au uchunguze muundo wa block kwa urahisi.



Ili kuipata, pata tu Tor Address kutoka kwa kivinjari chako. Ili kufanya hivyo, endesha amri ile ile uliyotumia kupata Address ya DMT yako:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Utaweza kufikia maelezo yako yote ya muunganisho wa Dojo kupitia Tor. Tunayovutiwa nayo hapa ni URL ifuatayo:



```
Block Explorer =
```



Ikiwa tayari umeunganishwa kwenye DMT yako, unaweza pia kupata Address hii kwenye menyu ya "*Pairing*", ndani ya muunganisho wa JSON:



![Image](assets/fr/43.webp)



Ili kufikia kivinjari chako kutoka kwa mashine yoyote kwenye mtandao wowote (hata ukiwa mbali), fungua [Tor Browser](https://www.torproject.org/download/) na uweke URL ambayo umepata tena.



⚠️ **Tafadhali weka Address hii kwa siri kabisa



Kisha utaweza kufikia Block explorer yako mwenyewe.



![Image](assets/fr/44.webp)



*Salio la picha: https://ashigaru.rs/.*



Ili kufuatilia muamala, ingiza tu txid yake kwenye upau wa kutafutia ulio juu kulia.



![Image](assets/fr/45.webp)



*Salio la picha: https://ashigaru.rs/.*



Kuangalia harakati zinazohusiana na Address, endelea kwa njia sawa kwa kuingia Address kwenye bar ya utafutaji.



![Image](assets/fr/46.webp)



*Salio la picha: https://ashigaru.rs/.*



Unaweza pia kuingiza Hash ya block au urefu kwenye upau wa kutafutia ili kuonyesha maelezo.



![Image](assets/fr/47.webp)



*Salio la picha: https://ashigaru.rs/.*



## 9. Matengenezo ya Dojo



### 9.1 Simamisha Dojo yako



Usikatishe nguvu kwa Dojo yako kwa ghafla, kwani hii inaweza kuharibu hifadhidata fulani, haswa kielezo cha Fulcrum. Ikiwa itabidi uizime, kila wakati fanya uzimaji safi wa Dojo, basi, mara tu taratibu zote zimekamilika, zima mashine pia:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Sasisha Dojo yako



Dojo hubadilika mara kwa mara na matoleo mapya hutolewa ili kurekebisha hitilafu, kuboresha uthabiti na kuongeza vipengele. Kwa hivyo ni muhimu [kuangalia mara kwa mara kwa masasisho](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) na kusasisha Dojo yako. Mchakato huo ni sawa na usakinishaji wa awali, lakini unahitaji ubadilishe faili fulani na toleo jipya zaidi linalopatikana, huku ukidumisha usanidi wako. Hapa kuna hatua za kina za kufuata kwa sasisho safi na salama:



Ili kujua toleo la sasa la Dojo yako, endesha amri :



```bash
./dojo.sh version
```



Ingawa hatua hii ni ya hiari, ninapendekeza uanze kwa kusasisha OS yako. Hii inapunguza hatari ya kutopatana na kuhakikisha kuwa tegemezi zinazotumiwa na Dojo zimesasishwa:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Nenda kwenye saraka ya Dojo na usimamishe huduma za sasa:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Kisha anzisha upya mfumo wako ili kupata slate safi:



```bash
sudo reboot
```



Dojo inakuja na faili zilizotiwa sahihi kidijitali. Saini hizi za PGP zinahakikisha kuwa faili zinatoka kwa msanidi na hazijabadilishwa kwa njia yoyote. Ni muhimu kuziangalia kila wakati unaposasisha Dojo, kama ulivyofanya ulipoisakinisha mara ya kwanza. Anza kwa kupakua ufunguo wa umma wa msanidi programu kupitia Tor, kisha uingize:



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Rudi kwenye saraka yako ya kibinafsi:



```bash
cd ~/
```



Pakua toleo jipya zaidi la Dojo kutoka GitHub kupitia Tor. Katika mfano huu, ni toleo la `1.28.0` (ambalo bado halipo wakati wa kuandika: hii ni kutoa mfano tu). Kumbuka kubadilisha faili na kiungo [na toleo unalotaka kusakinisha](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Pia pakua faili iliyo na alama za vidole za PGP na saini (kwa mara nyingine tena, kumbuka kurekebisha toleo katika amri):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Hakikisha kuwa faili ya alama ya vidole iliyopakuliwa imetiwa saini na ufunguo wa msanidi programu:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Matokeo sahihi yanapaswa kuonyesha:



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Onyo kwamba ufunguo haujathibitishwa inaweza kuonekana, lakini hii haina umuhimu wowote. Kwa upande mwingine, ikiwa saini ni batili au inalingana na ufunguo mwingine, usiende zaidi na uanze tena, ukiangalia viungo.



Kisha uhesabu alama ya vidole ya SHA256 ya kumbukumbu na uilinganishe na faili rasmi ya alama ya vidole :



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Ikiwa alama za vidole mbili zinalingana kikamilifu, kumbukumbu ni halisi na ni dhabiti. Ikiwa zinatofautiana, futa faili mara moja na usiendelee.



Ondoa kumbukumbu kwenye saraka yako ya nyumbani:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Kisha nakili yaliyomo kwenye saraka ya Dojo, ukibadilisha ya zamani:



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Uendeshaji huu huweka faili zako za usanidi ziko katika `~/dojo-app/docker/my-dojo/conf`, lakini hubadilisha faili zingine zote na matoleo yaliyosasishwa.



Ili kuweka mazingira yako safi, futa faili zisizo za lazima:



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Rudi kwenye saraka ya hati za Dojo na utekeleze amri ya sasisho:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Amri hii inaamuru Docker kuunda tena picha na faili mpya, kisha kuanzisha upya huduma zote kiotomatiki. Mwishoni mwa mchakato, angalia kumbukumbu ili kuhakikisha kuwa Bitcoin core, Fulcrum na Dojo zote zinafanya kazi kwa usahihi:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Ikiwa huduma zitaanza bila hitilafu na kumbukumbu zinaonyesha vizuizi vinachakatwa, Dojo yako sasa imesasishwa na inafanya kazi.