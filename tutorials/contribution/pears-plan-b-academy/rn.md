---
name: Gahunda ₿ Ishure - Porogaramu y'amapera
description: Ni gute woshiramwo no gukoresha porogarama ya Plan ₿ Academy kuri Pears?
---

![cover](assets/cover.webp)


Kumbure urazi ko Plan ₿ Academy ari yo nzira nini kuruta izindi zo gukoresha amakuru y’inyigisho yihariye Bitcoin, ihuriza hamwe amashure, inyigisho, n’ibihumbi vy’ibikoresho vy’ubuhinga bufunguye. Mu ntango, Plan ₿ Academy yari urubuga. Ariko none vyogenda gute iyo utagishobora kuyironka mu buryo busanzwe, nk’akarorero iyo habaye ugucengera?


Muri iyi nyigisho, tuzomenya ingene twokoresha urubuga rwa **Plan ₿ Academy** mu buryo bushobora guhangana n’ugucengera vy’ukuri dukoresheje **Pears**, ubuhinga bwo gukorana n’abandi (P2P) bwateguwe na **Holepunch** kandi bushigikiwe na **Tether**.


Pears ni porogaramu ituma dushobora gukoresha urubuga rwa Plan ₿ Academy tutari twizigiye urubuga rwo hagati. Muri iyi nyigisho, tuzoshira Pears kuri mudasobwa yawe kugira ngo ushobore gushika kuri Plan ₿ Academy biciye ku Pears.


Intumbero ya Pears ni yoroshe: gutuma bishoboka gukwiragiza no gukoresha porogarama z’urubuga ataco bishingiye ku bikorwa remezo vyose bihurikiye hamwe (nta ba server, nta ba host, nta bahuza). Mu yandi majambo, naho umuhinga mu vy’igicu yofunga canke igihugu kigahagarika urubuga, iyo porogarama irabandanya kuba mu bagenzi b’urubuga. Ubwo buryo buratuma urubuga rwacu rw’inyigisho, Plan ₿ Academy, ruguma rushikira kw’isi yose, ata n’akantu na kamwe kananiwe.


---

**IBIBAZO:**



- Gushiramwo Amapera;



- Gukoresha itegeko rikurikira kugira ngo utangure porogaramu ya Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Amapera ni iki?


Amapera ni igihe kimwe ibidukikije vy'igihe co gukora, igikoresho co gutegura, n'urubuga rwo gukoresha ibikorwa vy'urunganwe. Ico gikoresho gifise inkomoko yuguruye kigufasha kwubaka, gusangira no gukoresha porogarama ata serveri canke ibikorwa remezo, ataco uhinduye hagati y’abakoresha. Mu majambo y’ibikorwa, ivyo bisigura ko aho kwakira porogarama kuri server nyamukuru, umukoresha wese aba urudodo mu rubuga: basangira igice c’iporogarama n’amakuru n’abandi bagenzi babo. Ubuhinga bwose bukora uruja n’uruza rw’ibintu aho instance yose ikorana kugira ngo iyo service ikomeze gushikwako.


![Image](assets/fr/01.webp)


Ubu buryo bushingiye ku bice vy’ubuhinga bwa none vyateguwe na Holepunch:



- Hypercore**: igitabo gikwiragijwe gituma amakuru aguma ahuye n’umutekano ata rutonde rw’amakuru rwo hagati.
- Hyperbee**: urutonde rwubakiwe hejuru ya Hypercore rutuma amakuru atunganizwa neza kandi agabazwa neza.
- Hyperdrive**: ni uburyo bwo kubika no guhuza amadosiye y’ibikorwa hagati y’urunganwe.
- Hyperswarm** na **HyperDHT**: ibice vy’urubuga bishoboza kuvumbura n’uguhuza kw’isi yose ata server nyamukuru.
- Secretstream**: uburyo bwo gukingira amakuru hagati y’urunganwe.


Mu gufatanya ivyo bihimba, Pears irashoboza kurema porogarama zigenga, zifise amakuru, kandi zikwiragizwa, aho umukoresha wese agira uruhara n’umwete mu rubuga. Ubwo buhinga bwo kwubaka bushizwe ahantu hamwe burakuraho amafaranga y’ibikorwa remezo, ingorane zo gucengera, n’ama SPOF (*Single Points of Failure*).


Amapera yateguwe na Holepunch, ishirahamwe ryashinzwe na Mathias Buus na Paolo Ardoino (umuyobozi mukuru wa Tether n’umuyobozi mukuru wa Bitfinex), rifise intumbero yo kwagura ubuhinga bwo gukorana n’abandi birenze Bitcoin. Icipfuzo cabo ni co kwubaka “*Internet y’urunganwe*,” aho porogarama yose ishobora gukora ata ruhusha, ata server, kandi ata bahuza. Holepunch iramaze kuba inyuma ya **Keet**, porogaramu y’amasanamu n’ubutumwa yuzuye P2P.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Iyi nyigisho yo gushiramwo Pears igizwe n'ibice vyinshi bivanye n'uko ukoresha system yawe. Genda nyene kuri iyo ihuye n’aho uba kugira ngo ukurikize amabwirizwa akwiriye:*



- Linux (Debiyani)** → Igice ca **2**
- Amadirisho** → Igice **3**
- macOS** → Igice ca **4**


## 2. Ni gute umuntu yoshira amapera kuri Linux (Debian)?


Gushiramwo Pears kuri Debian ni ikintu coroshe ariko bisaba ibintu bikeyi, ivyo tuzobidondora muri iki gice.


### 2.1. Kuvugurura sisitemu


Imbere y’ibindi vyose, birahambaye ko uraba neza ko ubuhinga bwawe buri ku gihe.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Gushiramwo ibivako


Amapera yizigira amasomero amwe amwe, harimwo `libatomic1`, akoreshwa na moteri y'igihe co gukora ya JavaScript. Uyishiremwo n'itegeko rikurikira:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Gushiramwo Node.js na npm biciye kuri NVM


Amapera akwiragizwa biciye kuri *npm*, umuyobozi w'amapaki *Node.js*. Naho Pears idashingiye kuri *Node.js* kugira ikore, irakenewe kugira ngo ishiremwo. Uburyo bwiza bwo gushiramwo *Node.js* kuri Linux ni muri *NVM* (*Umucungerezi wa verisiyo za Node*), bigufasha gucunga verisiyo nyinshi za Node iruhande n'uruhande.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Hanyuma, wongere ushiremwo terminal yawe kugira ngo ukoreshe *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Suzuma ko *NVM* yashizweho neza:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Inyuma, shiramwo verisiyo ihamye ya *Node.js* (nk'akarorero, verisiyo ya LTS iriho ubu):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Genzura ko *Node.js* na *npm* vyashizweho neza:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Shiraho amapera na npm


Iyo *npm* ibonetse, urashobora gushiramwo Pears CLI kw'isi yose kuri system yawe. Ibi bigufasha gukoresha itegeko `pear` uhereye ku bubiko bwose.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Gutanguza amapera


Inyuma yo gushiramwo, ukoreshe itegeko rikurikira muri terminal yawe:


```bash
pear
```


Mu gutangura kwa mbere, Pears izokwifatanya n’urubuga rw’abagenzi kugira ngo ibone ibice bikenewe. Iyi nzira ntiyizigira kuri server iyo ari yo yose — amadosiye afatwa ataco akora ku bandi bagenzi.


![Image](assets/fr/10.webp)


Igihe gukuraho, wongere ukoreshe itegeko kugira ngo wemeze ko vyose bikora:


```bash
pear
```


![Image](assets/fr/11.webp)


Niba vyose vyashizweho neza, urutonde rw’imfashanyo rwa Pears ruzoboneka rufise urutonde rw’amabwirizwa ariho.


### 2.6. Igerageza ry'amapera na Keet


Kugira ngo umenye neza ko Pears ikora neza, urashobora gutanguza porogarama ya P2P iriho iri ku rubuga, nka Keet, porogarama y’ubutumwa n’amakoraniro y’amasanamu yuguruye yateguwe na Holepunch.


```bash
pear run pear://keet
```


Iri tegeko rishira porogaramu ya Keet ataco ihinduye ku rubuga rwa Pears, ata gukoresha umukozi wa mbere. Iyo Keet itanguye neza, bisigura ko installation yawe ya Pears ikora neza.


![Image](assets/fr/12.webp)


Sisitemu yawe ya Linux ubu yiteguye gukoresha no kwakira porogaramu z'urunganwe n'urunganwe na Pears.


## 3. Uko woshiramwo amapera kuri Windows 1.1.


Gushiramwo Pears kuri Windows biroroshe nk’uko biri kuri Linux ariko bisaba ibikoresho bikeyi vyihariye.


*Niba ukoresha Linux kandi umaze gushiramwo Pears, ushobora guca uja ku **Intambwe ya 5**.*


### 3.1. Gufungura PowerShell nk'umuyobozi


Mbere, fungura PowerShell n'uburenganzira bw'umuyobozi:



- Fyonda ku rutonde rw’Itanguriro;
- Ubwoko “Igikoko c’Inguvu”;
- Fyonda iburyo kuri "*Idirisha ry'Inguvu*";
- Hitamwo "*Gukoresha nk'umuyobozi*".


![Image](assets/fr/15.webp)


### 3.2. Gukuraho NVS


Amapera ashirwaho biciye kuri *npm*, umuyobozi w'amapaki *Node.js*. Kuri Windows, uburyo Holepunch yasavye ni ugukoresha *NVS* (*Igihinduzi c'Imirongo*), kikaba gikomeye kuruta *NVM* kuri iyi sisitemu.


Muri PowerShell, koresha iri tegeko kugira ngo ushiremwo verisiyo nshasha ya *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Gushiramwo Node.js


Inyuma yo gushiramwo, subiramwo PowerShell, hanyuma winjize itegeko rikurikira:


```powershell
nvs
```


Ushobora kubona urutonde rw'ibiriho *Node.js*. Hitamwo iya mbere ukanda urufunguzo `a` kuri klavye yawe.


![Image](assets/fr/17.webp)


*Node.js* ubu irashizweho.


![Image](assets/fr/18.webp)


### 3.4. Kugenzura ivyo washizeho


Raba neza ko *Node.js* na *npm* bishoboka:


```powershell
node -v
npm -v
```


Amategeko yose akwiye kugarura inomero ya verisiyo.


![Image](assets/fr/19.webp)


### 3.5. Shiraho amapera na npm


Igihe *Node.js* na *npm* zizoba zibonetse, shiraho **Pears CLI** kw'isi yose kuri sisitemu yawe:


```powershell
npm install -g pear
```


Ibi bishiramwo `pear` mu bubiko bwawe bw'isi yose *npm*.


![Image](assets/fr/20.webp)


### 3.6. Suzuma kandi utangurize amapera


Igihe gushiramwo birangiye, genda:


```powershell
pear
```


Mu gutangura kwa mbere, Pears izoca ikura ibihimba bisabwa ku rubuga rw’abagenzi. Ivyo bishobora gutwara umwanya mutoyi.


![Image](assets/fr/21.webp)


Niba vyose vyagenze neza, ushobora kubona urutonde rw’imfashanyo rwa Pears CLI rufise urutonde rw’amabwirizwa mato mato ariho (run, seed, info...).


### 3.7. Igerageza ry'amapera na Keet


Kugira ngo umenye neza ko Pears ikora neza, urashobora gutanguza porogarama ya P2P iriho iri ku rubuga, nka Keet — porogarama y’ubutumwa n’amakoraniro y’amasanamu yuguruye yateguwe na Holepunch.


```bash
pear run pear://keet
```


Iri tegeko rishiramwo porogaramu ya Keet iva ku rubuga rwa Pears, ata gukoresha umukozi wo hagati. Iyo Keet itanguye neza, bisigura ko installation yawe ya Pears ikora neza.


![Image](assets/fr/22.webp)


Sisitemu yawe ya Windows ubu yiteguye gukoresha no kwakira porogaramu z’urunganwe n’urunganwe na Pears.


## 4. Uko woshiramwo Pears kuri macOS .


Gushiramwo Pears kuri macOS bisa na Linux ariko bisaba guhindura bikeyi ku bidukikije vya Apple. Reka tugende muri izo ntambwe turi kumwe.


*Niba ukoresha Linux canke Windows kandi umaze gushiramwo Pears, ushobora guca uja ku **Intambwe ya 5**.*


### 4.1. Suzuma ibisabwa kuri sisitemu


Imbere yo gushiramwo, urabe neza ko *Ibikoresho vy'Umurongo w'Itegeko rya Xcode* vyashizwe kuri sisitemu yawe. Iyi package itanga ibikoresho vy'ubwubatsi bikenewe vya *Node.js* n'ibiyishingiyeko.


Kugira ngo ubikore, fungura urubuga ukoresheje inzira ngufi `Cmd + Space bar`, wandike `Ikibanza`, hanyuma ukande `Enter`. Hanyuma, ukoreshe itegeko rikurikira muri terminal kugira ngo uyishiremwo:


```bash
xcode-select --install
```


Niba ivyo bikoresho bimaze gushirwa kuri sisitemu yawe, macOS izobikumenyesha.


### 4.2. Shiraho NVM


Amapera akwiragizwa biciye ku *npm*, umuyobozi w'amapaki *Node.js*. Naho Pears idashingiye kuri *Node.js* kugira ikore, irakenewe kugira ngo ishiremwo. Uburyo bushimikijwe bwo gushiramwo *Node.js* kuri macOS ni *NVM* (*Umucungerezi wa Verisiyo ya Node*), bushobora kugufasha gucunga verisiyo nyinshi za Node icarimwe.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Hanyuma wongere ushiremwo terminal yawe kugira ngo ukoreshe *NVM*:


```bash
source ~/.zshrc
```


Niwakoresha *bash* aho gukoresha *zsh*, genda:


```bash
source ~/.bashrc
```


Ibikurikira, suzuma ko *NVM* yashizweho neza:


```bash
nvm --version
```


Terminal yawe ikwiye kugaragaza verisiyo ya *NVM* yashizweho.


### 4.3. Gushiramwo Node.js na npm


Inyuma, shiramwo verisiyo ihamye ya *Node.js* (nk'akarorero, verisiyo ya LTS iriho ubu):


```bash
nvm install --lts
```


Igihe gushiramwo, suzuma verisiyo zashizweho:


```bash
node -v
npm -v
```


Amategeko yose akwiye kugarura inomero ya verisiyo.


### 4.4. Shiraho amapera na npm


Iyo *npm* ibonetse, urashobora gushiramwo Pears CLI kw'isi yose kuri system yawe. Ivyo bizokuronsa uburenganzira bwo gukora itegeko rya `pear` uhereye ku bubiko bwose.


```bash
npm install -g pear
```


### 4.5. Gutanguza amapera


Inyuma yo gushiramwo, ukoreshe itegeko rikurikira muri terminal yawe:


```bash
pear
```


Mu gutangura kwa mbere, Pears ifatanya n’urubuga rw’abagenzi kugira ngo ikureho ibihimba bikenewe. Iyi nzira ntibisaba umukozi wo hagati — amadosiye afatwa ataco akora ku bandi bagenzi.


Igihe umaze gukuraho, subira ukoreshe itegeko kugira ngo ugenzure ko vyose bikora:


```bash
pear
```


Niba vyose vyashizweho neza, urutonde rw’imfashanyo rwa Pears ruzoboneka n’urutonde rw’amabwirizwa ariho.


### 4.6. Igerageza ry'amapera na Keet


Kugira ngo umenye neza ko Pears ikora neza, urashobora gutanguza porogarama ya P2P isanzwe iri ku rubuga, nka Keet, porogarama y’ubutumwa n’amakoraniro y’amasanamu ivuye muri Holepunch.


```bash
pear run pear://keet
```


Iri tegeko rishiramwo porogarama ya Keet ataco ihinduye ku rubuga rwa Pears, ata gukoresha server ya mbere. Iyo Keet itanguye neza, bisigura ko installation yawe ya Pears ikora neza.


Sisitemu yawe ya macOS ubu yiteguye gukoresha no kwakira porogaramu z’urunganwe n’urunganwe n’amapera.


## 5. Uko wokoresha umugambi ₿ Academy ku mapera


Igihe Pears imaze gushirwaho kandi ikaba iriko irakora, urashobora gutanguza urubuga rwa **Plan ₿ Academy** biciye ku rubuga rwa P2P. Gusa ukoreshe iri tegeko rikurikira muri terminal yawe (iryo tegeko nyene rikora kuri Linux, Windows, na macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Igihe gushiramwo, Plan ₿ Academy izofungura mu bidukikije vyawe vya Pears, yiteguye gukoreshwa nk’urubuga rw’intango — ariko ataco yizigiye kuri server nyamukuru.


![Image](assets/fr/14.webp)


## 6. Uko wotegura imbuto ₿ Ishure ku mapera


Mu rubuga rwa Pears, ku *seed* igikorwa bisigura gusubira kugitanga ku bandi bagenzi bawe ukoresheje imashini yawe bwite. Mu bikorwa, iyo seed Plan ₿ Academy, mudasobwa yawe iba isoko y’amakuru atuma abandi bakoresha bashobora gukuraho porogarama ata kwizigira server nyamukuru.


Ubu buryo burakomeza ukwihangana n’uguhangana n’ugucengera kw’ikoreshwa ryacu ku rubuga rwa Pears. Uko urunganwe rwa seed rugenda rurarushiriza, ni ko rurushiriza kuboneka no gushirwa ahantu hose, naho nyene hariho ama node y’intango yoba atari ku murongo.


Kugira ngo ufashe mu gukwiragiza Plan ₿ Academy, ukoreshe gusa iri tegeko rikurikira:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Igihe cose iri tegeko rizoba rikora, igikoresho cawe kizogira uruhara mu gukwiragiza amadosiye y’ikoreshwa. Iyo ufunze terminal, igikorwa co gusangira kirahagarara.


Kugira ngo ukomeze gutera imbuto inyuma yo gusubira gutangura, ushobora gukoresha itegeko mu nyuma canke ugakora igikorwa ca sisitemu — nk’akarorero, igikorwa ca sisitemu kuri Linux, LaunchAgent kuri macOS, canke igikorwa categekanijwe kuri Windows. Ubu buryo buratuma igikorwa ca Plan ₿ Academy gisubira gutera imbuto igihe sisitemu itangura.


Murakoze gutanga umusanzu mu gukwiragiza Plan ₿ Academy on Pears mu buryo butandukanye no gufasha gutuma uburezi bwa Bitcoin bushobora guhangana n’ugucengera vy’ukuri!