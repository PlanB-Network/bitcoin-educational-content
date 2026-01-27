---
name: Korrektuuri juhised
description: Millised on olulised tegurid, mida tuleb Plan ₿ Academy's korrektuuri tegemisel silmas pidada?
---

![github](assets/cover.webp)


Tere tulemast selle õpetuse juurde, mis käsitleb **juhiseid, mida tuleb järgida Plan ₿ Akadeemia sisu korrektuurimisel**. Meil on hea meel, et jagate meie missiooni tõlkida Bitcoin materjale võimalikult paljudesse keeltesse, et aidata inimestel saada teada, kuidas see toimib ja kuidas seda oma igapäevaelus kasutada.


Kõigepealt annab teile Plan ₿ Academy [avalik repositoorium](https://github.com/PlanB-Network/bitcoin-educational-content) võimalus kirjutada õpetusi, parandada olemasolevat sisu või isegi teha ettepanekuid uue keele lisamiseks platvormile. Et rohkem teada saada, liitu kõigepealt meie [Telegram Group](https://t.me/PlanBNetwork_ContentBuilder) ja kirjuta lühike tutvustus enda ja keelte kohta, mida sa oskad.


Käesolev juhendmaterjal on pühendatud kaastöötajatele, kes soovivad sisu korrigeerida. Enamik neist ei tea palju [Githubist](https://planb.academy/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ega [Markdown keelest](https://www.markdownguide.org/basic-syntax/), mida me repositooriumi sees kasutame, seega on oluline jagada mõningaid teadmisi selle ülesandega seotud võtmeteguritest.


Allpool olen kogunud kokku kõige levinumad probleemid, millega korrektorid kokku puutuvad. Võite vabalt soovitada rohkem, sest see võib aidata teisi parandada.


Enne spetsiifikatesse sukeldumist tuleb kõigepealt lugeda seda õpetust Githubi praktiliste tegevuste kohta, mida tuleb järgida, forkides Plan ₿ Academy repositooriumi, tehes muudatusi ja saates PR-i:


https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017


## Mis on korrektuur?


Korrektuur on kirjaliku teksti lõplik läbivaatamine, mille käigus tuvastatakse ja parandatakse grammatika-, õigekirja-, kirjavahemärgistamise ja vormindamise vead. Sellega tagatakse, et tekst on enne avaldamist või esitamist selge, sidus ja vigadeta.


Seda tüüpi ülesannete lahendamisel on oluline järgida originaalkeele (EN või FR) tähendust, kuid veenduda, et tekst lõplikus keeles oleks emakeeleõppija jaoks võimalikult sujuv.


Pidage alati meeles, et tõlkimine/kontrolltöö on ÕPPE!


Tegelikult on meie ühine eesmärk harida võimalikult paljusid inimesi Bitcoin kohta, seega on oluline, et materjal, mida nad loevad, oleks sujuv ja selge.

Selles mõttes on kõik Plan ₿ Academy'sse panustajad haridustöötajad!


## Esimesed sammud enne korrektuuri tegemist Plan ₿ Akadeemias


Enne uue korrektuuriülesande alustamist teatage sellest [Telegrammi grupis](https://t.me/PlanBNetwork_ContentBuilder) või teavitage oma kava ₿ Akadeemia koordinaatorit, kes avab selleks ettenähtud [teema](https://github.com/orgs/Plan ₿ Akadeemia/projektid/3). Kui saate küsimuse lingi, lihtsalt **kommenteerige, et alustate** selle sisu korrektuuriga.


See süsteem aitab koordinaatoril jälgida repo sisemist arengut ja võimaldab korrektori poolt sisu "nõuda", vältides sellega kellegi teise topeltpüüdeid.

Teemal ise leiate lingid, mis suunavad teid sisu kontrollimiseks. Võite lihtsalt nendele klõpsata või, mis veelgi parem, võite minna tagasi oma enda forkeeritud repo juurde ja töötada otse sealt edasi. Vaatame, kuidas seda teha saab!


Kõigepealt, **AJALGI ärge unustage oma repo SYNC-i, "dev" haru**. Nii on sisu alati uuendatud, enne kui alustate mis tahes tüüpi ülesannet, ja te ei tekita konflikte vana ja uue materjali vahel. Klõpsake kindlasti "Sync fork" ja "Update branch".



![REVIEW](assets/en/1.webp)



Pärast edukat sünkroniseerimist saate otse juurdepääsu huvipakkuvale sisule ja teha uue haru kinnituse, nagu on näidatud selles [õpetuses](https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017). Vastasel juhul saate avada uue haru, kus töötada, klõpsates "Branches", nagu allpool näidatud.



![REVIEW](assets/en/2.webp)



Sellel uuel lehel leiate kõik juba avatud filiaalid pealkirja "Teie filiaalid" all. See jaotis on väga kasulik, sest see võimaldab teil hõlpsasti leida, kus te olete mingit sisu muutnud. Kui soovite avada uue haru, võite klõpsata lehe paremas ülanurgas nupule "New Branch".



![REVIEW](assets/en/3.webp)



Seejärel avaneb hüpikaken, kuhu tuleb sisestada uue haru nimi. Allpool esitatud juhul valisin selle nimeks "BTC101-FR". Nii jääb mulle alati meelde, et seda konkreetset haru tuleb kasutada prantsuse keele kursuse BTC101 korrektuuri tegemiseks ja **ei kasuta seda ühegi teise ülesande jaoks**.


Soovitan teil teha sama: avage kindlasti uus haru alati, kui teil on vaja alustada uut ülesannet.



![REVIEW](assets/en/4.webp)



Pärast selle uue haru loomist klõpsake seda kindlasti eelmisel lehel "Teie harud" ja alustage tööd konkreetse sisuga seotud *.md* failiga (minu puhul klõpsan ma "kursused" -> "BTC101" -> "fr.md"). Kõik selle konkreetse failiga seotud kommiteerimised tuleb kinnitada (salvestada) sama haru sees.



## Originaalkeel või tõlge?


Kui teete sisu korrektuuri, siis on oluline **selle originaalversiooni inglise (või prantsuse)** alati kontrollida. Pidage meeles, et me tõlgime tehisintellekti keeletööriistade abil, seega ei pruugi sihtkeele esitus olla sujuv või lõpplugejale hästi arusaadav.


Seega võite vabalt teha tekstis kohandusi ja muuta vajadusel lauseid. Meie eesmärk on suurendada voolavust, kuid alati järgida algset tähendust. Kui teil tekib kahtlusi, kuidas mingit sõna käsitleda, küsige kindlasti tõlkekoordinaatorilt.


LLM-vahendid võivad tõlkida mõned Bitcoin-ga seotud sõnad sõna-sõnalt, nagu Lightning Network. Eriti kehtib see juhul, kui tegemist on väga tehniliste sõnadega. Sellistel juhtudel on soovitav parema selguse huvides säilitada ingliskeelne originaalsõna sihtkeeles, välja arvatud juhul, kui teie keelereeglid nõuavad iga sõna tõlkimist.


Teisel juhul **uurige alati, kas keegi teine teie Bitcoin kogukonnas on selle sõna juba tõlkinud** ja kas seda sõna kasutatakse nüüd laialdaselt.



- Üks lahendus võiks olla **kontroll [BitcoinWiki](https://en.bitcoin.it/wiki/Main_Page)** sihtkeeles, et näha, kas sõna on tõlgitud või mitte. Kui ei ole, siis jätke sõna inglise keelde.



- Igal juhul oleks minu soovitus **lisada EN-sõna siiski**, lisades sihtkeele vastava tähenduse ümmarguste sulgude sees, järgides skeemi EN (LANG), või vastupidi. Ex. Address (indirizzo) või indirizzo (aadress).



- Teine hea lahendus on säilitada ET originaalsõna/fraas, seejärel **luuakse hüperlink**, mis suunab ümber [sõnastik](https://planb.academy/en/resources/glossary) planb.networki. Selleks tuleb sõna/fraas sisestada nurksulgude sisse ja link ümmarguste sulgude sisse, nagu on näha alljärgnevas näites:


```
[UTXO](https://planb.academy/resources/glossary/utxo)
```


Lõpptulemusena (pilt allpool) ei visualiseerita kogu linki ja sõna muutub klikitavaks.



![REVIEW](assets/en/5.webp)



Pange tähele, et sõnastiku link, mille võtate veebilehelt, sisaldab keelekoodi pärast sõna "network" (näide: ``https://planb.academy/en/resources/glossary/utxo``-> siin on keelekood "en"). Sellisel juhul **kustutage lingilt keelekood**, nagu nägite ülalpool toodud kastis. Nii viib süsteem lugeja automaatselt tema määratud keelde.


Hoiukoha sisu on täis selliseid hüperlinke nagu eespool kirjeldatud. Nüüd, kui te teate, mida need tähendavad, **jälgige, et mitte kustutada ühtegi algse autori poolt lisatud linki**.



- Teine asi, mis on seotud sõnade esitamisega, on järgmine. Kui te leiate tekstis sõna "Plan ₿ Academy", **jätke see sellisel kujul**. Ärge tõlkige sõna "plaan" ega sõna "võrk". Peale selle EI kasuta artiklit "The", kui esitled Plan ₿ Academy: **Käsitlege seda kui kaubamärki**.



- Sama kehtib ka "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", mis tuleks samuti säilitada algsel kujul.


Üks viimane märkus selle lõigu juurde: nagu eespool öeldud, kasutame sisu tõlkimiseks tehisintellekti vahendeid ja seejärel palume kaastöötajate sekkumist, et kõik oleks sujuv ja hästi korrektuuritud.


Kui te kasutate tehisintellekti enamiku teksti korrektuuriks, märkame seda kindlasti, sest oleme tuttavad tüüpiliste lausekonstruktsioonidega, mida tehisintellekt genereerib. Kui me avastame, et te tuginesite korrektuuris ainult tehisintellektile, ilma et oleksite teinud olulisi muudatusi, võib sats lõplik tasu väheneda poole võrra!



## Pealkirjade struktuur


Markdown-keeles algavad pealkirjad (ja lõike pealkirjad) kõik hash-märgiga ``#``. Räägimärkide arv vastab pealkirja tasemele. Näiteks on kolmanda tasandi pealkirjal kolm numbrimärki enne teksti (nt `### Minu pealkiri`).


Kursustel tutvustatakse kõige olulisemaid osi ühe hash-märgiga, samas kui allosad võivad olla kahest kuni nelja hash-märgiga. Õpikutes kasutame tavaliselt ainult kahe hash-märgiga pealkirju.



![REVIEW](assets/en/6.webp)



Veenduge, et **KUNAGI ei kustutata hash-märke** enne pealkirja, sest muidu tekitab see probleeme teksti struktuuriga.


Samal ajal, **ei tohi muuta** chapterID osa, mida näete ülaloleval pildil, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` või videoviiteid nagu ``::::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8b8cc8::::``.


Kui me sisestame pealkirja ette "#", muutub see automaatselt kursuse eelvaates paksuks, nii et **vältige pealkirjade paksuks muutmist parandamise ajal**.


Kõrvalmärkusena olgu öeldud, et kursuste EN-keeles on **pealkirjad, mida juhatab sisse üks või kaks ``#``, kõik sõnad algavad suurtähtedega**, samas kui pealkirjad, mis algavad kolme või nelja ``#``ga, tavaliselt seda reeglit ei järgi. Kui võimalik, veenduge, et teie sihtkeele pealkirjad järgiksid seda struktuuri.



## Kursuste esialgne osa


Iga sisu alguses on järgmised staatilised väiketähtedega sõnad: "nimi", "kirjeldus", "eesmärgid". Veebisait kasutab neid sisu enda dekodeerimiseks ja need on **sellele alati jäetud**. Sellest tulenevalt EI TOHI neid tõlkida, sest vastasel juhul tekitab sisu sünkroniseerimisprobleeme. Kontrollige kindlasti ainult koolonile järgnevat osa, mille AI tõlgib automaatselt.



![REVIEW](assets/en/7.webp)



Hoidke selles samas esialgses osas formaat nii, nagu see on. Ärge lisage teksti algusesse midagi. Vältige näiteks "tt" lisamist enne kriipsu, nagu alloleval pildil!



![REVIEW](assets/en/8.webp)


## Kuidas käituda kursuse piltidega


Meie kodulehel on nüüd peaaegu iga kursuse kohta tõlgitud pildid!


Kontrollige alati, kas kõik pildid on olemas ja korrektselt kuvatud. Kui te leiate `koodi vaates` sellist rida `![PILT](assets/en/001.webp)`, tähendab see, et seal kuvatakse pilti.


Veenduge, et lisate alati uue rea pildikoodi ja teksti vahele. Näide allpool:


```
WRONG CONFIGURATION:
- to start translating, click on the button `Translate`: ![language](assets/08.webp)
To save, click on `save`!


RIGHT CONFIGURATION:

- to start translating, click on the button `Translate`:

![language](assets/08.webp)

To save, click on `save`!
```



Peale selle ärge unustage lugeda iga pildi sisu. Kui märkate, et piltide sees oleva teksti tõlkimisega on probleeme, teatage sellest oma koordinaatorile ja saate võimaluse neid ka korrektuurida!


Saate pilti visualiseerida Githubi jaotises `Preview` (või meie veebisaidil, avage teises vahekaardis). Seejärel tulge tagasi selle kõrval asuvasse `koodi` sektsiooni, et seda kontrollida.


![REVIEW](assets/en/9.webp)


## Soovitused formaadi kohta


Allpool on toodud mõned näited vorminguprobleemide kohta, millele sihtkeeles sisu korrektuurimisel tähelepanu pöörata.



- Pöörake tähelepanu veidratele kirjavahemärkidele nagu `\*\*` või ``**``, mis võivad kujutada rasvase sümboli halba esitust. Allpool oleval pildil näete, et tärnid on ainult sõna paremal pool, mis näeb imelik välja.



![REVIEW](assets/en/10.webp)



Seega kontrollige alati ingliskeelset originaalteksti, et näha, kas rasvane tekst peaks seal olema. Sellisel juhul lisage lihtsalt kaks tärni sõna algusesse, et see oleks veebilehel õigesti kuvatud. Tegelikult tuleb markdown-keeles **paksuse esitamiseks lisada kaks tärni ``**`` nii enne kui ka pärast sõna/lause** (vt näide allpool).



![REVIEW](assets/en/11.webp)




- Samad probleemid võivad tekkida selliste sümbolitega nagu $ ja `` `` ``.

Kontrollige kindlasti originaalkeele faili (sageli EN või FR), et näha, kus need sümbolid peaksid olema. Selles küsimuses võite alati küsida abi koordinaatorilt.



- Kui leiate tsitaate, uurige kindlasti internetis, et leida õige tõlge oma keelde. Tsitaadid sisestatakse tavaliselt pärast sümbolit ``>``.



![REVIEW](assets/en/12.webp)




## Õppeprogrammide korrektuur


Kui otsustate juhendmaterjale korrektuurida, avab koordinaator spetsiaalse teema **täieliku juhendmaterjali rubriigi** jaoks. Kui olete oma ülesande täitnud, saate dokumenteerida oma edusammud, kommenteerides teemat koos läbivaadatud õpetuste loeteluga: sel viisil saate luua selge jälgimissüsteemi edaspidiseks, mis on oluline, sest uut sisu lisatakse iga kuu. Näite sellise lähenemisviisi kohta näete [siin](https://github.com/PlanB-Network/bitcoin-educational-content/issues/3023#issuecomment-3364923190).


![REVIEW](assets/en/13.webp)


Kuna igakuiselt lisatakse uusi juhendmaterjale, võib teie haru korrektuuri käigus vananeda. Mõned korrektorid on sellele probleemile lähenenud, sünkroniseerides täpselt haru, kus nad töötavad: **paluks seda mitte kunagi teha! Kui te seda teete, siis riskite kaotada kõik selle hetkeni tehtud edusammud!**


Selle asemel peaksite kõigepealt lõpetama oma praeguse fork juhendmaterjalide korrektuuri. Seejärel **sünkroniseerige `dev`** ja looge uus haru, kus keskendute äsja lisatud õpetuste (ainult eelmisest harust puuduolevate) korrektuurile.


Õpikutes on võimalus, et **pildid jäävad tõlkimata**. Kuna enamik õpetusi on **algupäraselt kirjutatud prantsuse või inglise keeles**, leiate tõenäoliselt pilte, mis sisaldavad käske või juhiseid originaalkeeles. Võtame näite hollandikeelsest õpetusest Sparrow, teatades nii teksti kui ka sellega seotud pildi.


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Publieke server_".
```


![REVIEW](assets/en/14.webp)


Nagu näete, viitab pilt selgelt `Public Server`, inglise keeles, samas kui tekstis on mainitud väljend `_Publieke server_`. Sellisel juhul on tegemist sidususe probleemiga, sest lugeja leiab pildi ja teksti vastandamisel vastuolulist teavet.


Selle probleemi lahendamiseks võite sisestada käsu nii, nagu see on pildil (inglise või prantsuse keeles), millele järgneb sulgudes teie keele tõlge , nagu allpool näidatud:


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Public Server_" (Publieke server).
```



## Viktoriini korrektuur


Kas teadsite, et saate ka viktoriiniküsimusi igas kursuses parandada? Näiteks kui soovite IT-õppeaine BTC101 viktoriiniküsimusi korrektuurida, võite avada spetsiaalse haru ja järgida seda teed: "kursused" -> "BTC101" -> "viktoriin". Sealt leiate kõik igale küsimusele pühendatud kaustad koos sellega seotud _yml_-vormingus keelefailiga.


Veenduge veel kord, et olete spetsiaalselt selleks otstarbeks avatud filiaalis ja teavitage alati koordinaatorit.


Oluline on seda tüüpi _yml_ faili korrektuuris meeles pidada, et vältida koolonite ``:`` või jutumärkide lisamist teksti sees. Tegelikult kasutatakse koolonit **ainult** selleks, et eraldada võtmeväärtuspaare nagu "wrong_answers" teistest. Näite näete alloleval pildil:


![REVIEW](assets/en/15.webp)


Pärast küsimuse läbivaatamist veenduge, et te muudate "läbivaadatud" staatuse "vale" asemel "tõeseks", nagu on näidatud alloleval pildil. Veenduge, et **hoidke need staatussõnad inglise keeles**, olenemata sellest, mis keeles te töötate!



![REVIEW](assets/en/16.webp)


Kui staatuse rida "reviewed:true" puudub, siis veenduge, et **lisate selle viktoriini lõppu**.


## Sõnastiku korrektuur


Nii nagu viktoriinide puhul, saate ka sõnastiku korrektuuri teha. Esialgne sõnastik on kirjutatud prantsuse keeles, seega leiate sealt selliseid lauseid nagu: "Prantsuse keeles võib seda väljendit tõlkida..."


Sellisel juhul kohandage lause sihtkeelele või inglise keelele. Näiteks võiksite kirjutada "Inglise keeles on see väljend...".

Kui pealkiri on jäetud inglise keelde, võite kohandada lause oma keelele: "Suahiili keeles on see väljend..."


Lisaks kirjutage pealkirjad kindlasti suurtähtedega.


![REVIEW](assets/en/17.webp)



## Teie PR-i pealkiri ja kirjeldus


Kui sa saadad oma PR-i, oleks hämmastav, kui sa nimetaksid selle sellisel kujul: [KORREKTUUR] SISU NIMI - KEEL:


```
[PROOFREADING] BTC101 - ENGLISH
```


Peale selle võite PR** kommentaaride lahtrisse kirjutada "sulgeb" + selle teema number, mille koordinaator saatis teile, kui alustasite korrektuuritööd, mille ees on ``#``.

Näiteks kui sa just saatsid PR-i koos cyp201 + viktoriinide korrektuuriga, võid kirjutada "sulgeb [#2934](https://github.com/PlanB-Network/bitcoin-educational-content/issues/2934)".


Nii on PR ja probleem omavahel seotud ja kes iganes loeb avalikku Githubi repositooriumi, saab hõlpsasti teavet leida.



## Muud parimad tavad



- Kui teil on vaja otsida konkreetseid sõnu teksti sees, võite klõpsata klahvile ``CTRL+F`` ja ilmub sektsioon Find-replace. See osa on väga kasulik, kui teil on vaja hüpata teksti konkreetse osa juurde või kui teil on vaja asendada konkreetseid sõnu/lauseid partiidena, ilma kogu sisu kerimata.



![REVIEW](assets/en/18.webp)



Kui kasutate funktsiooni "Asenda kõik", on oluline kontrollida tulemusi kaks korda, et veenduda, et ka linke ei ole muudetud. Näiteks kui soovite muuta sõna "Bitcoin" sõnaks "Bitkoin" (mis võib mõnes keeles olla vajalik), saate funktsiooni "replace all" abil tõhusalt uuendada kõiki tekstis olevaid juhtumeid. Kuid pidage meeles, et see tööriist muudab ka kõiki seda sõna sisaldavaid linke, mis võib põhjustada ümbersuunamisprobleeme.


Alljärgnevas näites kasutas korrektor ülaltoodud funktsiooni, et asendada "satoshi" sõnaga "satoshi(sats)", ning muutis ka lingi, mis sisaldab seda sõna ise. Selle tulemusena muutus link kehtetuks.


Kontrollige alati kahekordselt kõiki tekstis olevaid hüperlinke, et veenduda, et need on õiged.



![REVIEW](assets/en/19.webp)




- Kui autor lisab teemale järgides lingi, mis viitab Plan ₿ Academy kursusele või õpetusele (**ei** sulgudes), loob veebileht automaatselt "kaardi", mis näitab seotud pisipilti. Selle tulemusena veenduge alati, et **lisate teksti ja lingi enda vahele uue rea**, vastasel juhul võib veebilehel ilmneda järgmine viga.



![REVIEW](assets/en/20.webp)



## Kokkuvõte


Kokkuvõtteks võib öelda, et kui olete teadlik tavalistest korrektuurivigadest, aitab see teil tõesti parandada oma oskusi sisu kontrollimisel. On lihtne jätta tähelepanuta selliseid asju nagu kontekst või järjepidevus ning nende vigade avastamine võib teha suurt vahet.


Pidage alati meeles, et algaja võib neid kursusi ja õpetusi lugeda, seega on meie kohustus tagada, et nad saaksid sellest täielikult aru. **Korrektorina oled sa õpetaja!**


Nüüd olete valmis alustama kursuste, õppematerjalide, viktoriinide ja sõnastiku sõnade korrektuuriga. Jääge kursis, et alustada ka videote transkriptsioonide kontrollimist!


Aitäh, et lugesid selle õpetuse läbi, ja nautige oma korrektuuri teekonda!