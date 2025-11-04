---
name: Amapera
description: Ni gute noshiramwo no gukoresha porogarama kuri Pears?
---

![cover](assets/cover.webp)



Muri iyi nyigisho, tuzomenya ingene twokoresha porogarama kuri **Pears**, ubuhinga bwo gukorana n'abandi (P2P) bwateguwe na **Holepunch** kandi bushigikiwe na **Tether**. Intumbero ni yoroshe: gutuma bishoboka gukwiragiza no gukoresha porogarama z’urubuga ata kwizigira ibikorwa remezo vyose bihurikiye hamwe (nta ba serveri, nta ba host, nta bahuza). Mu yandi majambo, naho umuhinga mu bijanye n’igicu yofunga canke igihugu kigahagarika urubuga, iyo porogarama irabandanya kubaho hagati y’abagenzi b’urubuga.



## 1. Amapera ni iki?



Amapera ni ibidukikije vy’igihe co gukora, igikoresho co gutegura n’urubuga rwo gukoresha ibikorwa vy’urunganwe. Ico gikoresho gifunguye kiratuma bishoboka kwubaka, gusangira no gukoresha porogarama ata server canke ibikorwa remezo, ataco bimaze hagati y’abakoresha. Mu majambo nyayo, ivyo bisigura ko aho kwakira porogarama kuri server nyamukuru, umukoresha wese aba urudodo rw’urubuga, agasangira igice c’iporogarama n’amakuru n’abandi bagenzi biwe. Ubuhinga bwose bukora uruja n’uruza rw’ibintu, instance yose igakorana kugira ngo iyo service igume ishobora gushikira abantu.



![Image](assets/fr/01.webp)



Ubu buryo bushingiye ku matafari y’ubuhinga bwa none yateguwe na Holepunch:




- Hypercore**: igitabo gikwiragijwe gitanga icemezo c’uko amakuru ahuye n’umutekano ata rutonde rw’amakuru rwo hagati.
- Hyperbee**: indexer iri hejuru ya Hypercore, kugira ngo amakuru ashobore gutunganirizwa neza no kuyarondera.
- Hyperdrive**: uburyo bwa dosiye busanzwe bukoreshwa mu kubika no guhuza amadosiye y'ibikorwa hagati y'urunganwe.
- Hyperswarm** na **HyperDHT**: ibice vy’urubuga bishobora kuvumbura no guhuza hagati y’urunganwe kw’isi yose, ata server nyamukuru.
- Secretstream**: umurongo w’ububiko bwa E2E kugira ngo ukingire ubutumwa hagati y’abantu babiri.



Mu guhuza ivyo bihimba, Pears iratuma bishoboka kurema porogarama zigenga, zifise amakuru y’ibanga kandi zikwiragizwa, aho umukoresha wese agira uruhara n’umwete mu rubuga. Ubwo buhinga bwo kwubaka bushizwe ahantu hamwe burakuraho amafaranga y’ibikorwa remezo, ingorane zo gucengera n’ama SPOF (*Single Point of Failure*).



## 2. Inkomoko na filozofiya y'umugambi



Amapera ariko arategurwa na Holepunch, ishirahamwe ryashinzwe na Mathias Buus na Paolo Ardoino (umuyobozi mukuru wa Tether n’umuyobozi mukuru wa Bitfinex), rifise intumbero yo kwagura ubuhinga bwo gukorana n’abandi birenze Bitcoin. Icipfuzo cabo ni co kwubaka "Internet y'abagenzi", aho porogaramu yose ishobora gukora ata wemerewe, ata server, kandi ata bahuza. Holepunch iramaze kuba inyuma ya **Keet**, porogaramu yuzuye ya P2P yo gukora inama n’ubutumwa ku mavidewo.



*Iyi nyigisho yo gushiramwo Pears igizwe n'ibice vyinshi bivanye n'uko ukoresha system yawe. Genda nyene ku gice gihuye n'ibidukikije vyawe kugira ngo ukurikize amabwirizwa akwiriye :*




- Linux (Debiyani)** → Igice ca **3**
- Amadirisho** → Igice ca **4**
- macOS** → Igice ca **5**



## 3. Uko woshiramwo amapera kuri Linux (Debian)



Gushiramwo Pears kuri sisitemu ya Debian birasanzwe, ariko bisaba ibisabwa bikeyi, ivyo tuzobidondora muri iki gice.



### 3.1. kuvugurura sisitemu



Mbere na mbere, birahambaye ko uraba neza ko ubuhinga bwawe buri ku gihe.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. gushiramwo ibivako



Amapera yizigira amasomero amwe amwe, cane cane `libatomic1`, akoreshwa n'igihe co gukoresha JavaScript. Uyishiremwo n'itegeko rikurikira:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. gushiramwo Node.js na npm biciye kuri NVM



Amapera akwiragizwa biciye ku *npm*, umuyobozi w'amapaki *Node.js*. Naho Pears itavana ataco ihinduye kuri *Node.js* kugira ikore, ni ngombwa kugira ngo ishirwemwo. Uburyo bushimikijwe bwo gushiramwo *Node.js* kuri Linux ni *NVM* (*Umucungerezi wa verisiyo za Node*), bushobora kugufasha gucunga verisiyo nyinshi za Node mu buryo bumwe.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Hanyuma wongere ushiremwo terminal yawe kugira ngo ukoreshe *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Suzuma ko *NVM* yashizweho:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Hanyuma ushiremwo verisiyo idahinduka ya *Node.js* (nk'akarorero LTS iriho ubu):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Suzuma *Node.js* na *npm* gushirwaho:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Gushiramwo amapera na npm



Iyo *npm* ibonetse, urashobora gushiramwo Pears CLI kw'isi yose kuri system yawe. Ivyo bizokuronsa uburenganzira bwo gukoresha itegeko rya `pear` uhereye ku bubiko bwose.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Gutanguza amapera



Inyuma yo gushiramwo, ukoreshe itegeko rikurikira muri terminal yawe:



```bash
pear
```



Ku ntango ya mbere, Pears izokwifatanya n’urubuga rw’abagenzi kugira ngo ibone ibice bikenewe. Iyi nzira ntibisaba umukozi wa mbere: amadosiye abonwa ataco akoresheje ku bandi bagenzi.



![Image](assets/fr/10.webp)



Igihe umaze gukuraho, wongere ukoreshe itegeko kugira ngo umenye ko vyose biriko birakora:



```bash
pear
```



![Image](assets/fr/11.webp)



Niba vyose vyashizweho neza, Pears Help izogaragara n'urutonde rw'amabwirizwa ariho.



### 3.6. Kugerageza amapera na Keet



Kugira ngo umenye ko Pears ikora neza, urashobora gutanguza porogarama ya P2P isanzwe iri ku rubuga, nka Keet, porogarama ya Holepunch yo gutanga ubutumwa n’amakoraniro y’amasanamu.



```bash
pear run pear://keet
```



Iri tegeko rishira porogaramu ya Keet ataco ihinduye ku rubuga rwa Pears, itaciye kuri server nyamukuru. Iyo Keet itanguye neza, installation yawe ya Pears irakora neza.



![Image](assets/fr/12.webp)



Sisitemu yawe ya Linux ubu yiteguye gukoresha no kwakira porogaramu z'urunganwe n'urunganwe na Pears.



## 4. Uko woshiramwo Pears kuri Windows 1.1.



Gushiramwo Pears kuri Windows biroroshe nk’uko biri kuri Linux, ariko bisaba ibikoresho bikeyi bidasanzwe.



*Niba ukoresha Linux, ushobora guca ku ntambwe ya 6.*



### 4.1. gufungura PowerShell mu buryo bw'umuyobozi



Mbere na mbere, koresha PowerShell n'uburenganzira bw'umuyobozi :




- Fyonda ku rutonde rw’Itanguriro;
- Ubwoko bw'Igikoko c'Inguvu ;
- Fyonda iburyo kuri "*Idirisha ry'Inguvu*" ;
- Hitamwo "*Gukoresha nk'umuyobozi*".



![Image](assets/fr/15.webp)



### 4.2. gukuraho NVS



Amapera ashirwaho biciye kuri *npm*, umuyobozi w'amapaki *Node.js*. Kuri Windows, uburyo Holepunch yasavye ni ugukoresha *NVS* (*Igihinduzi c'Imirongo*), kikaba gikomeye kuruta *NVM* kuri iyi sisitemu.



Mu PowerShell, koresha iri tegeko kugira ngo ushiremwo verisiyo nshasha ya *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. gushiramwo Node.js



Inyuma yo gushiramwo, subiramwo PowerShell maze winjize itegeko rikurikira:



```powershell
nvs
```



Ushobora kubona urutonde rw'ibiriho *Node.js*. Hitamwo iya mbere ukanda urufunguzo `a` kuri klavye yawe.



![Image](assets/fr/17.webp)



*Node.js* irashizweho.



![Image](assets/fr/18.webp)



### 4.4. Suzuma ivyo washizeho



Raba neza ko *Node.js* na *npm* bishoboka:



```powershell
node -v
npm -v
```



Amategeko yose ategerezwa kugarura inomero ya verisiyo.



![Image](assets/fr/19.webp)



### 4.5. Gushiramwo amapera na npm



Igihe *Node.js* na *npm* zizoba zibonetse, shiramwo **Pears CLI** kw'isi yose kuri sisitemu yawe:



```powershell
npm install -g pear
```



Ibi bizoshiramwo `pear` binary mu bubiko bwawe bw'isi yose *npm*.



![Image](assets/fr/20.webp)



### 4.6. Suzuma kandi utangure amapera



Igihe gushiramwo birangiye, genda :



```powershell
pear
```



Ku gihe c’ugutangura kwa mbere, Pears izoca ikura ibihimba bikenewe ku rubuga rw’abagenzi. Ivyo bishobora gutwara umwanya mutoyi.



![Image](assets/fr/21.webp)



Niba vyose vyagenze neza, ushobora kubona igicapo c'imfashanyo ca CLI Pears kirimwo urutonde rw'amabwirizwa mato mato ariho (run, seed, info...).



### 4.7. Kugerageza amapera na Keet



Kugira ngo umenye ko Pears ikora neza, urashobora gutanguza porogarama ya P2P isanzwe iri ku rubuga, nka Keet, porogarama ya Holepunch yo gutanga ubutumwa n’amakoraniro y’amasanamu.



```bash
pear run pear://keet
```



Iri tegeko rishira porogaramu ya Keet ataco ihinduye ku rubuga rwa Pears, itaciye kuri server ya mbere. Iyo Keet itanguye neza, installation yawe ya Pears irakora neza.



![Image](assets/fr/22.webp)



Sisitemu yawe ya Windows ubu yiteguye gukoresha no kwakira porogaramu z’urunganwe n’urunganwe na Pears.



## 5. Noshiramwo gute Pears kuri macOS?



Gushiramwo Pears kuri macOS bisa n’ugushira kuri Linux, ariko bisaba guhindura bikeyi bishingiye ku bidukikije vya Apple. Reka tuvumbure izo ntambwe turi kumwe.



*Niba ukoresha Linux canke Windows kandi umaze gushiramwo Pears, ushobora guca ku **intambwe ya 6**.*



### 5.1. Suzuma ibisabwa



Imbere yo gushiramwo, urabe neza ko *Ibikoresho vy'Umurongo w'Itegeko rya Xcode* biri kuri sisitemu yawe. Iyi package itanga ibikoresho bikenewe vyo gukoranya _Node.js_ n'ibiyishingiyeko.



Kugira ngo ubikore, fungura urubuga rufise inzira ngufi ya klavye `Cmd + Space bar`, hanyuma wandike `Terminal` hanyuma ukande urufunguzo `Enter`. Ushobora rero kwinjiza iri tegeko muri terminal kugira ngo utangure gushiramwo:



```bash
xcode-select --install
```



Niba ibikoresho bimaze gushirwa kuri sisitemu yawe, macOS izobikumenyesha.



### 5.2. shiraho NVM



Amapera akwiragizwa biciye kuri *npm*, umuyobozi w'amapaki *Node.js*. Naho Pears itavana ataco ihinduye kuri *Node.js* kugira ikore, ni ngombwa kugira ngo ishiremwo. Uburyo bushimikijwe bwo gushiramwo *Node.js* kuri macOS ni *NVM* (*Umucungerezi wa Verisiyo ya Node*), bushobora kugufasha gucunga verisiyo nyinshi za Node mu buryo bumwe.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Hanyuma wongere ushiremwo terminal yawe kugira ngo ukoreshe *NVM* :



```bash
source ~/.zshrc
```



Niba ukoresha *bash* aho gukoresha *zsh*, genda :



```bash
source ~/.bashrc
```



Hanyuma usuzume ko *NVM* ishizwemwo:



```bash
nvm --version
```



Terminal ikwiye gusubiza verisiyo ya *NVM* yashizwe kuri sisitemu yawe.



### 5.3. gushiramwo Node.js na npm



Hanyuma ushiremwo verisiyo idahinduka ya *Node.js* (nk'akarorero LTS iriho ubu):



```bash
nvm install --lts
```



Igihe gushiramwo birangiye, suzuma verisiyo zashizweho:



```bash
node -v
npm -v
```



Amategeko yose ategerezwa kugarura inomero ya verisiyo.



### 5.4 Gushiramwo amapera na npm



Iyo *npm* ibonetse, urashobora gushiramwo Pears CLI kw'isi yose kuri system yawe. Ivyo bizokuronsa uburenganzira bwo gukoresha itegeko rya `pear` uhereye ku bubiko bwose.



```bash
npm install -g pear
```



### 5.5. Gutanguza amapera



Inyuma yo gushiramwo, ukoreshe itegeko rikurikira muri terminal yawe:



```bash
pear
```



Ku ntango ya mbere, Pears izokwifatanya n’urubuga rw’abagenzi kugira ngo ikureho ibice bikenewe. Iyi nzira ntibisaba umukozi wa mbere: amadosiye abonwa ataco akoresheje ku bandi bagenzi.



Igihe umaze gukuraho, wongere ukoreshe itegeko kugira ngo umenye ko vyose biriko birakora:



```bash
pear
```



Niba vyose vyashizweho neza, Pears Help izogaragara n'urutonde rw'amabwirizwa ariho.



### 5.6. Kugerageza amapera na Keet



Kugira ngo umenye ko Pears ikora neza, urashobora gutanguza porogarama ya P2P isanzwe iri ku rubuga, nka Keet, porogarama ya Holepunch yo gutanga ubutumwa n’amakoraniro y’amasanamu.



```bash
pear run pear://keet
```



Iri tegeko rishira porogaramu ya Keet ataco ihinduye ku rubuga rwa Pears, itaciye kuri server nyamukuru. Iyo Keet itanguye neza, installation yawe ya Pears irakora neza.



Sisitemu yawe ya macOS ubu yiteguye gukoresha no kwakira porogaramu z’urunganwe n’urunganwe n’amapera.



## 6. Nokoresha gute porogarama iri ku Mapera?



Igihe Pears imaze gukora, ushobora gukoresha porogaramu uhisemwo ukoresheje itegeko rikurikira:



```bash
pear run pear://[KEY]
```



Subiriza gusa `[KEY]` n'urufunguzo rw'ikoreshwa wipfuza gukoresha.



![Image](assets/fr/13.webp)



Kugira ngo umenye ingene wokoresha urubuga rwacu rwa Plan ₿ Academy kuri Pears, raba iyi nyigisho yuzuye :



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Kandi kugira umenye ingene ukoresha ubutumwa bwa Keet uherutse gutanguza kuri Pears, raba iyi nyigisho :



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b