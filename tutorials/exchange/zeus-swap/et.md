---
name: Zeus Swap
description: On-Chain ja Lightning Network bitcoinide vaheline Exchange teenus, mis ei ole hooldusteenus
---

![cover](assets/cover.webp)



Bitcoin ökosüsteem on kahetine: põhivõrk (On-Chain) pakub maksimaalset turvalisust, samas kui Lightning Network võimaldab koheseid tehinguid. Selline kahe Layer arhitektuur tekitab praktilise väljakutse: kuidas saab raha tõhusalt nende kahe kihi vahel üle kanda ilma tsentraliseeritud vahendajateta?



Probleem on konkreetne: saate Lightning-makse, kuid soovite seda hoida Cold ladustuses, või vastupidi, teil on On-Chain bitcoinid, kuid vajate Lightning-likviidsust. Traditsioonilised lahendused hõlmavad Lightning-kanalite käsitsi avamist/sulgemist (kulukas ja tehniline) või tsentraliseeritud platvorme, mis nõuavad KYC-i.



Zeus Swap lahendab selle probleemi automaatse, mittevabatahtliku Exchange teenusega. Zeus LSP poolt välja töötatud teenus võimaldab teil konverteerida On-Chain bitcoinid Lightning satoshideks kahesuunaliselt, ilma et te usaldaksite oma raha vahendajale. Protsess kasutab aatomilepinguid (HTLC), mis tagavad, et Exchange kas lõpetab või tühistab.



Uuendus seisneb selle lihtsuses: vaid paar klõpsu Exchange jaoks, mis säilitab teie finantssuveräänsuse, ilma et oleks vaja registreerimist või KYC-i.



## Mis on Zeus Swap?



Zeus Swap on Zeus LSP poolt välja töötatud Exchange likviidsusteenus, mis võimaldab aatomivahetust Bitcoin põhivõrgu ja Lightning Network vahel. See on tehniline infrastruktuur, mis kasutab allveevahetusi ja pöördvahetusi, et hõlbustada kahesuunalist konverteerimist On-Chain BTC ja Lightning satoshide vahel, säilitades samal ajal operatsiooni mittekaitstavuse.



### Tehniline arhitektuur



Zeus Swap kasutab Boltzi avatud lähtekoodiga Bitcoin/Lightning aatomivahetuse tehnoloogiat. Protokollis kasutatakse Hash Time Locked Contracts (HTLC): lepingud, mis lukustavad rahalisi vahendeid kahe vabastamistingimusega (krüptograafilise saladuse avalikustamine või aja lõppemine).



Allveelaeva vahetuse (On-Chain → Lightning) puhul saadab kasutaja bitcoinid Address-le, mis sisaldab Lightning Invoice Hash. Zeus LSP avab need vahendid ainult vastava Invoice maksmisega, paljastades eelpildi, mis avab bitcoinid automaatselt. See mehhanism tagab aatomilisuse.



Pöördvahetuse (Lightning → On-Chain) puhul maksab kasutaja Zeus LSPst Lightning Invoice, mis näitab eelkujutist, mis võimaldab ettevalmistatud Bitcoin tehingu vabastamist siht-Address-le.



Lisateavet selle kohta, kuidas Lightning Network töötab, leiate meie spetsiaalsest kursusest :



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Ärimudel



Zeus LSP tegutseb turutegijana, säilitades On-Chain ja Lightning likviidsust, et täita vahetustehinguid. Swapide puhul kohaldab Zeus muutuvat tasu (tavaliselt 0,1% kuni 0,5% sõltuvalt suunast ja tingimustest) pluss Bitcoin Mining tasu, mis kuvatakse läbipaistvalt enne valideerimist.



Välkteenuse pakkujana optimeerib Zeus kulusid tänu oma kogemustele nõudmisel toimuva kanali avamise, tõhusa marsruutimise ja kohandatud likviidsuslahenduste alal.



### Integratsioon



Zeus Wallet integreerib selle teenuse algselt, võimaldades vahetusi Interface Bitcoin/Lightning'ist lahkumata. See välistab rakenduste vahel kopeerimise ja kleepimise hõõrdumise.



Sõltumatu Interface veeb jääb kõigile rahakottidele kättesaadavaks, tagades maksimaalse paindlikkuse kasutamisel.



## Peamised omadused



### Kahesuunalised vahetused



Zeus Swap pakub kahte tüüpi Exchange:



**Submarine swaps (On-Chain → Lightning)**: süstib Lightning likviidsust oma Bitcoin reservidest, kasulik mobiilse Wallet või Lightning-sõlme toitmiseks ilma kanaleid käsitsi avamata.



**Pöördvahetused (Lightning → On-Chain)**: konverteerige Lightning satoshid On-Chain bitcoinideks, et vältida kulukaid kanali sulgemisi.



### Kasutajaliidesed



**Interface web** (swaps.zeuslsp.com): lihtsustatud kogemus ilma registreerimiseta, juhendatud protsess koos tasude ja staatuse kuvamisega reaalajas.



**Zeus Wallet integratsioon**: otsevahetused rakendusest, arvete ja aadresside automaatne haldamine, käitlusvigade kõrvaldamine.



### Ohutus ja taastumine



Iga vahetus genereerib unikaalse Contract muutumatute parameetritega: Hash Välk, aegumine, tagasimakse Address. Rikke korral automaatne taastumine Address kaudu, mis on ette nähtud Zeus LSP-st sõltumatult.



**Zeus vahetab päästmisvõtme**: On-Chain → Lightning vahetuse ajal genereerib Zeus automaatselt universaalse taastamisvõtme, mis asendab vanad individuaalsed tagastusfailid. See ainulaadne võti töötab igas seadmes ja kõigi sellega loodud vahetuste puhul. On väga oluline laadida see võti alla ja salvestada turvalisse kohta, et saaksite vahetuse ebaõnnestumise korral oma vahendid taastada.



### Võrgu optimeerimine



Zeus Swap kohandab automaatselt aegumistähtaegu ja Mining tasusid vastavalt võrgu tingimustele. Zeuse kasutajad saavad kasutada täiustatud võimalusi: LSP valik, kohandatud viivitused, ühilduvus teiste teenustega (Boltz).



## Paigaldamine ja kasutamine



### Juurdepääsumeetodid



**Interface web** (swaps.zeuslsp.com): universaalne lahendus, mis ühildub kõigi rahakottidega, ei nõua paigaldamist, sobib ideaalselt juhuslikuks kasutamiseks.



**Zeuse rakendus** (iOS/Android): integreeritud kogemus, mis ühendab Wallet ja vahetused, sobib tavakasutajatele.



Vaata meie Zeuse õpetust, et rohkem teada saada selle täieliku Wallet kohta:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Veebikonfiguratsioon



**On-Chain → Välk**: Interface veebis Zeus Swap: Protsess algab swap'i konfigureerimisega. Kasutaja saab kasutada On-Chain ja Lightning väljade vahel olevat noolt, et vahetuse suunda ümber pöörata.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: summa valik (Sats 50,000 → Sats 49,648 pärast tasusid) koos võrgutasude (Sats 302) ja Zeus teenuse (Sats 50) läbipaistva kuvamisega.*



Protsessi käigus pakub Zeus teile universaalse taastamise võtme allalaadimist:



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Allalaadimise dialoog Zeus Swaps Rescue Key jaoks - universaalne võti, mis asendab vanad individuaalsed hüvitusfailid*



Kui teil on juba võti olemas, võimaldab Zeus seda kontrollida:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface olemasoleva Zeus Swaps Rescue Key* kehtivuse kontrollimiseks



Pärast konfigureerimist genereerib Zeus Bitcoin depoo Address ja kuvab juhised :



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Vahetuse lõpetamise lehekülg: QR-kood ja Bitcoin Address 50 000 Satsi saatmiseks, koos meeldetuletusega 24-tunnise kehtivusaja lõppemise kohta*



Seejärel ootab vahetus Bitcoin kinnitust:



![Attente de confirmation](assets/fr/05.webp)



*Staatus "Tehing Mempool-s" - ootab Bitcoin kinnitust, et vahetustehing lõpule viia*



Pärast kinnitamist viiakse vahetus automaatselt lõpule:



![Swap réussi](assets/fr/06.webp)



*Edukuse kinnitamine: 49,648 Sats, mis on saadud Lightning'ile pärast võrgu- ja teenustasude mahaarvamist*



### Zeuse rakenduse kasutamine



**Välk → On-Chain**: Zeus rakendus pakub integreeritud kogemust pöördvahetuseks (Lightning kuni Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Zeuse põhiekraan, kus on näidatud Lightning (69,851 Sats) ja On-Chain (38,018 Sats) saldod, juurdepääs vahetustele külgmenüü kaudu*



![Configuration du swap reverse](assets/fr/08.webp)



*Interface pöördvahetuse loomine: gW-69, koos võrgutasudega (530 Sats) ja teenusega (250 Sats), mis on selgelt näidatud. Kasutajad saavad kas käsitsi sisestada Bitcoin vastuvõtva Address või generate automaatselt Wallet Zeusist nupu "generate On-Chain Address" kaudu.*



![Finalisation du swap mobile](assets/fr/09.webp)



*Lõplikuks muutmise ekraanid: Välk Invoice makseekraan koos "MAKSE KÄESOLEVAGA Invoice", kinnitus eduka välkmakse kohta 9,96 sekundi jooksul ja saldoaruanne koos 49 162 Sats kinnitusele ootava Sats-ga*



### Järelevalve ja turvalisus



Igal vahetusel on unikaalne identifikaator, mida saab jälgida reaalajas. Täielik edusammude kuvamine, automaatsed hoiatused aegumiskuupäevade kohta. Automaatsed laadimissoovitused vastavalt võrgu tingimustele.



## Eelised ja piirangud



### Eelised





- Lihtsus**: Vahetamine paari klikiga vs. manuaalne kanaliga manipuleerimine
- Mittekaitstav**: puudub KYC, puudub konto, vahendeid ei ole kunagi usaldatud kolmandale isikule
- Läbipaistvus**: tasud kuvatakse enne valideerimist selgelt (0,1% kuni 0,5% + miinimumtasu sõltuvalt kasutaja testidest - kontrollige kehtivaid tasusid iga vahetuse puhul)
- Mobiilne integratsioon**: Zeus Wallet emakeelne kogemus



### Piirangud





- Kehtivusaeg**: 24-48h maksimaalselt, ebaõnnestumine, kui Bitcoin ei ole õigeaegselt kinnitatud
- Summapiirangud**: vähemalt 25 000 Sats, Zeus LSP likviidsus sõltub tingimustest
- Jäljed On-Chain**: HTLC skriptid, mis on potentsiaalselt tuvastatavad Blockchain analüüsi abil
- Nõutav kinnitus**: vähemalt 10 minutit Bitcoin kinnitamiseks



## Parimad tavad



### Ajastus ja kulud





- Vaadake Mempool.space madala ülekoormuse aegadel
- Eelistage nädalavahetusi ja tipptundide väliseid kellaaegu, et vähendada Mining kulusid
- Arvutage kasumlikkust: väikesed summad vs. otsene kanali avamine



### Turvalisus





- Kontrollige hoolikalt Bitcoin-aadressid (soovitatav copy-paste)
- Varundage Zeus Swaps Rescue Key**: laadige alla ja säilitage taastamisvõti turvalises kohas
- Dokument: Contract ID, toetus Address, kehtivusaeg
- Kasutage õigeaegse kinnituse saamiseks asjakohaseid Mining tasusid



### Kasutusstrateegia





- Tasakaal On-Chain/Lightning likviidsus vastavalt teie vajadustele
- Zeus Swap ühekordsete kohanduste jaoks, otsekanalid püsivaks vajaduseks



## Võrdlus teiste vahetusteenustega



### Zeus Swap vs Boltz Exchange



Zeus Swap kasutab Boltzi backend-tehnoloogiat, kuid teeb mõned olulised parandused:



**Zeus Swap eelised** :




- Interface ühtlustatud**: loomulik integratsioon Zeusesse Wallet vs Interface veebitehnika Boltz
- WebSocket API**: reaalajas uuendused vs. käsitsi küsitlemine
- Automaatne haldamine**: automaatne arveldamine ja Address haldamine
- Mobiiltelefoni tugi**: ainult nutitelefoni vs. lauaarvuti optimeerimine
- Swaggeri dokumentatsioon**: täielik REST API arendajatele



**Boltz on endiselt eelis** täieliku sõltumatuse ja kasutamise puhul koos mis tahes Bitcoin/Lightning seadistusega.



Zeus Swap muudab tõestatud Boltzi tehnoloogia tavakasutajakogemuseks, mis on võrreldav erinevusega toorprotokolli ja kasutajasõbraliku rakenduse vahel.



### Zeus Swap vs Phoenix/Breez (integreeritud vahetused)



Phoenix ja Breez integreerivad läbipaistvad vahetusfunktsioonid, mis varjavad lõppkasutaja eest tehnilist keerukust. Phoenix kasutab automaatset vahetussüsteemi, mille puhul kasutaja ei tee Bitcoin kihtide vahel selgesõnaliselt vahetust: ta "saadab Bitcoin Address-le" ja rakendus tegeleb vahetusega taustal.



Selline ülimalt lihtsustatud lähenemine sobib ideaalselt algajatele, kuid piirab arusaamist ja operatsioonide kontrolli. Zeus Swap võtab kasutusele rohkem haridusliku filosoofia: kasutajad mõistavad, et nad vahetavad kahe erineva kihi vahel, arendades järk-järgult oma arusaamist kahe Layer Bitcoin ökosüsteemist.



## Tasude ja piirmäärade üksikasjalik võrdlus (2024)



⚠️ **Hoiatus**: Tasud võivad aja jooksul muutuda sõltuvalt turutingimustest ja teenuse uuendustest. Enne vahetuse kinnitamist kontrollige alati Interface-s kuvatavaid tasusid.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap pakub tasakaalu kasutusmugavuse ja tehnilise kontrolli vahel: kättesaadavam kui Boltz, paindlikum kui Phoenix/Breez, kuid rangelt mittekohustuslik lähenemine.



## Kokkuvõte



Zeus Swap kujutab endast olulist uuendust Bitcoin ökosüsteemis, lahendades elegantselt põhivõrgu ja Lightning Network vahelise koostalitlusvõime probleemi. Kombineerides aatomivahetuse krüptograafilise usaldusväärsuse ja kättesaadava kasutajakogemuse, demokratiseerib see teenus Bitcoin dual-Layer haldamist, ilma et see kahjustaks finantssuveräänsuse põhimõtteid.



Zeus Swap'i mittehaldatav arhitektuur, mis on päritud tõestatud Boltz'i tehnoloogiast, tagab, et teie vahendid jäävad kogu swap-protsessi jooksul teie ainukontrolli alla. Selline lähenemisviis järgib Bitcoin vaimu, pakkudes samal ajal kasutusmugavust, mis on vajalik peavoolu kasutuselevõtuks. Hinnakujunduse läbipaistvus ja KYC-protsesside puudumine tugevdavad seda ainulaadset väärtuspakkumist.



Kaasaegse Bitcoin kasutaja jaoks on Zeus Swap strateegiline vahend likviidsuse jaotamise optimeerimiseks vastavalt vajadusele: On-Chain turvaline hoiustamine pikaajaliste säästude jaoks, välkkäibevõimalus igapäevaste kulutuste ja mikrotehingute jaoks. See paindlikkus muudab Bitcoin haldamise tehnilisest piirangust konkurentsieeliseks.



Zeus Swapi edasine areng, mida toetavad kogenud Zeus LSP meeskond ja avatud lähtekoodiga Boltzi kogukond, tõotab edasisi parandusi kulude, töötlemisaegade ja kasutajakogemuse osas. See teenus on osa laiemast Bitcoin infrastruktuuri küpsemise suundumusest, kus tehniline keerukus muutub lõppkasutajale läbipaistvaks.



## Ressursid



### Ametlikud dokumendid




- [Zeus Swap - Veebiportaal](https://swaps.zeuslsp.com)
- [Zeus Wallet - mobiilirakendus](https://zeusln.app)
- [Blog Zeus - Teated ja õpetused](https://blog.zeusln.com)
- [Zeus tehniline dokumentatsioon](https://docs.zeusln.app)



### Ühendus ja toetus




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)