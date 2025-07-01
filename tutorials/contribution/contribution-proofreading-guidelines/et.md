---
name: Korrektuuri juhised
description: Millised on olulised tegurid, mida tuleb Plan ₿ Network korrektuuris silmas pidada?
---
![github](assets/cover.webp)


Tere tulemast selle õpetuse juurde, mis käsitleb Plan ₿ Network sisu korrektuurimisel järgitavaid suuniseid. Meil on hea meel, et jagate meie missiooni tõlkida Bitcoin materjale võimalikult paljudesse keeltesse, et aidata inimestel saada teada, kuidas see toimib ja kuidas seda igapäevaelus kasutada.


Kõigepealt annab Plan ₿ Network [avalik repositoorium] (https://github.com/PlanB-Network/Bitcoin-educational-content) panustamine teile võimaluse kirjutada õpetusi, parandada olemasolevat sisu või isegi teha ettepanekuid uue keele lisamiseks platvormile. Et rohkem teada saada, liitu kõigepealt meie [Telegram Group](https://t.me/PlanBNetwork_ContentBuilder) ja kirjuta lühike tutvustus enda ja keelte kohta, mida sa oskad.


Käesolev juhendmaterjal on pühendatud kaastöötajatele, kes soovivad sisu korrigeerida. Enamik neist ei tea palju [Githubist](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ega [Markdown keelest](https://www.markdownguide.org/basic-syntax/), mida me repositooriumis kasutame, seega on oluline jagada mõningaid teadmisi sellest, millele nad peavad selle ülesande täitmisel tähelepanu pöörama.


Ma lõin selle pärast seda, kui olin kogunud kõige levinumad probleemid, millega korrektorid oma ülesannete täitmisel kokku puutuvad. Võite vabalt soovitada rohkem, sest see võib aidata teisi parandada.


Enne spetsiifikatesse sukeldumist tuleks kõigepealt lugeda seda õpetust praktiliste tegevuste kohta, mida Githubis rakendada, forkides Plan ₿ Network repositooriumi, tehes muudatusi ja saates PR-i:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6

## Mis on korrektuur?


Korrektuur on kirjaliku teksti lõplik läbivaatamine, mille käigus tuvastatakse ja parandatakse grammatika-, õigekirja-, kirjavahemärgistamise ja vormindamise vead. Sellega tagatakse, et tekst on enne avaldamist või esitamist selge, sidus ja vigadeta.


Seda tüüpi ülesannete lahendamisel on oluline järgida originaalkeele (EN või FR) tähendust, kuid veenduda, et tekst oleks lõplikus keeles võimalikult sujuv emakeeleõppija jaoks.


## Esimesed sammud enne Plan ₿ Network korrektuuri tegemist


Enne uue korrektuuriülesande alustamist teatage sellest [Telegrammi grupis](https://t.me/PlanBNetwork_ContentBuilder) või teavitage oma Plan ₿ Network koordinaatorit, kes avab selleks ettenähtud [issue](https://github.com/orgs/PlanB-Network/projects/3). Kui saate teema lingi, kommenteerige lihtsalt, et alustate selle sisu korrektuuriülesandega.

See süsteem võimaldab koordinaatoril jälgida edusamme repo sees ja võimaldab korrektori poolt sisu "nõuda", vältides sellega kellegi teise topeltpüüdlusi.

Väljaandes ise leiate lingid, mis viivad teid otse sisu kontrollimiseks. Saate nendele otse klikkida või veelgi parem, võite minna tagasi oma enda forkeeritud repo juurde ja töötada otse sealt edasi.


Kõigepealt, pea ALATI meeles, et SYNC sa repo, on "dev" filiaali. Nii on sisu alati uuendatud, enne kui alustate mis tahes tüüpi ülesannet, ja te ei tekita konflikte vana ja uue materjali vahel. Klõpsake kindlasti "Sync Fork" ja "Update branch".



![REVIEW](assets/en/1.webp)



Pärast edukat sünkroniseerimist saate otse juurdepääsu huvipakkuvale sisule ja teha uue haru kinnituse, nagu on näidatud selles [õpetuses](https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). Vastasel juhul saate avada uue haru, kus töötada, klõpsates "Branches", nagu allpool näidatud.



![REVIEW](assets/en/2.webp)



Sellel uuel lehel leiate kõik juba avatud filiaalid pealkirja "Teie filiaalid" all. See jaotis on väga kasulik, sest see võimaldab teil hõlpsasti leida koha, kus te olete mingit sisu muutnud. Kui soovite avada uue haru, võite klõpsata lehe paremas ülemises nurgas oleval nupul "New Branch" (Uus haru).


![REVIEW](assets/en/3.webp)



Seejärel avaneb hüpikaken, kuhu tuleb sisestada uue haru nimi. Allpool esitatud juhul valisin selle nimeks "BTC101-FR". Nii jääb mulle alati meelde, et seda konkreetset haru tuleb kasutada prantsuse keele kursuse BTC101 korrektuuri tegemiseks ja **ei kasuta seda ühegi teise ülesande jaoks**.


Soovitan teil teha sama: avage kindlasti uus haru alati, kui teil on vaja alustada uut ülesannet.



![REVIEW](assets/en/4.webp)



Pärast selle uue haru loomist klõpsake seda kindlasti eelmisel lehel "Teie harud" ja alustage tööd konkreetse sisuga seotud *.md* failiga (minu puhul klõpsan ma kaustas "kursused" ja alamkataloogis BTC101, et otsida fr.md). Kõik selle konkreetse failiga seotud kommiteerimised peavad olema kommiteeritud (salvestatud) sama haru sees.


## Originaalkeel või tõlge?


Kui teete sisu korrektuuri, on oluline alati kontrollida selle ingliskeelset (või prantsuskeelset) originaalversiooni. Olge teadlik, et me tõlgime tehisintellekti keeletööriistade abil, seega ei pruugi sihtkeele esitus olla sujuv või lõpplugejale hästi arusaadav.


Seega võite vabalt teha tekstis kohandusi ja muuta vajadusel lauseid. Meie eesmärk on suurendada voolavust, kuid alati järgida algset tähendust. Kui teil tekib kahtlusi, kuidas mingit sõna käsitleda, küsige kindlasti tõlkekoordinaatorilt.


LLM-vahendid võivad tõlkida mõned Bitcoin-ga seotud sõnad sõna-sõnalt, näiteks Lightning Network, millest itaalia keeles saaks "Rete Fulmine".


Eriti kehtib see juhul, kui tegemist on väga tehniliste sõnadega. Sellistel juhtudel on soovitav parema selguse huvides säilitada ingliskeelne originaalsõna sihtkeeles, välja arvatud juhul, kui teie keelereeglid nõuavad iga sõna tõlkimist. Sel teisel juhul uurige alati, kas keegi teine teie Bitcoin kogukonnas on selle sõna juba tõlkinud ja seda kasutatakse nüüd laialdaselt.



- Üks lahendus võiks olla kontrollida [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page) sihtkeeles, et näha, kas sõna on tõlgitud või mitte. Kui ei ole, siis jätke sõna inglise keelde.



- Igal juhul oleks minu soovitus lisada EN-sõna siiski ja seejärel vastav tähendus sihtkeeles ümmarguste sulgude sees, järgides skeemi EN (LANG), või vastupidi. Ex. Address (indirizzo) või indirizzo (Address).



- Teine hea lahendus on säilitada ET originaalsõna/fraas, seejärel luua hüperlink, mis suunab ümber [sõnastik](https://planb.network/en/resources/glossary) planb.network'ile. Selleks tuleb sõna/fraas sisestada nurksulgude sisse ja link ümmarguste sulgude sisse, nagu on näha alljärgnevas näites:


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


Lõpptulemusena (pilt allpool) ei visualiseerita kogu linki ja sõna muutub klikitavaks.


![REVIEW](assets/en/5.webp)



Pange tähele, et sõnastiku link, mille võtate veebilehelt, sisaldab keelekoodi pärast sõna "network" (näide: ``https://planb.network/en/resources/glossary/UTXO``-> siin on keelekood "en"). Sellisel juhul eemaldage lingilt keelekood, nagu nägite ülaltoodud kastis. Nii viib süsteem lugeja automaatselt tema määratud keelde.


Repo sisu on täis selliseid hüperlinke nagu need ülaltoodud. Nüüd, kui te teate, mida need tähendavad, veenduge, et te ei kustuta ühtegi autori poolt insterted linki.


Teine asi, mis on seotud sõnade esitamisega, on järgmine. Kui te leiate tekstis sõna "Plan ₿ Network", jätke see sellisel algsel kujul. Ärge tõlkige sõna "plaan" ega sõna "võrk". Peale selle ärge kasutage Plan ₿ Network tutvustamisel artiklit "The" ja **tähelepanu sellele kui kaubamärgile**.


Sama kehtib ka "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", mis tuleks samuti säilitada algsel kujul.


Üks viimane märkus selle lõigu juurde: nagu eespool öeldud, kasutame sisu tõlkimiseks tehisintellekti vahendeid ja seejärel palume "inimese" sekkumist, et kõik oleks sujuv ja hästi korrektuuritud.


Kui te korrektuuri kasutate enamiku teksti puhul tehisintellekti, märkame seda kindlasti, sest oleme tuttavad tüüpiliste lausekonstruktsioonidega, mida tehisintellekt genereerib. Kui me avastame, et tuginesite korrektuuris ainult tehisintellektile, ilma et oleksite teinud olulisi muudatusi, võib Sats lõplik tasu väheneda poole võrra!


## Pealkirjade struktuur


Markdown-keeles algavad pealkirjad (ja lõike pealkirjad) kõik Hash märgiga ``#``. Hash märkide arv vastab pealkirja tasemele. Näiteks kolmanda taseme pealkirjas on teksti ees kolm numbrimärki (nt `### Minu pealkiri`).


Kursustel tutvustatakse kõige olulisemaid osi ühe Hash märgiga, samas kui allosad võivad olla kahest kuni nelja Hash märgiga. Õpikutes kasutame tavaliselt ainult kahe Hash märgiga pealkirju.



![REVIEW](assets/en/6.webp)


Veenduge, et **KUNAGI** ei kustutaks Hash märke enne pealkirja, sest muidu tekivad probleemid teksti struktuuriga.


Samal ajal **ei** muuda chapterID osa, mida näete ülaloleval pildil, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` või videoviiteid nagu ``::::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8b8cc8::::``.


Kui me sisestame ``#`` enne pealkirja, muutub see automaatselt kursuse eelvaates paksuks, seega vältige pealkirjade paksuks muutmist parandamise ajal.


Pealegi on kursuste EN-keeles ühe või kahe ``#``-ga pealkirjades kõik sõnad algavad suurtähtedega, samas kui kolme või neljaga algavad pealkirjad seda reeglit tavaliselt ei järgi. Kui võimalik, veenduge, et teie sihtkeele pealkirjad järgiksid seda struktuuri.


## Kursuste esialgne osa


Iga sisu alguses on järgmised staatilised väiketähtedega sõnad: "nimi", "kirjeldus", "eesmärgid". Veebisait kasutab neid sisu enda dekodeerimiseks ja need on **sellele alati jäetud**. Sellest tulenevalt EI TOHI neid tõlkida, sest vastasel juhul tekitab sisu sünkroniseerimisprobleeme. Kontrollige kindlasti ainult koolonile järgnevat osa, mille AI tõlgib automaatselt.



![REVIEW](assets/en/7.webp)



Hoidke selles samas esialgses osas formaat nii, nagu see on. Ärge lisage teksti algusesse midagi. Nt. vältige "tt" lisamist enne kriipsu, nagu alloleval pildil!



![REVIEW](assets/en/8.webp)


## Soovitused formaadi kohta


Allpool on toodud mõned näited vorminguprobleemide kohta, millele sihtkeeles sisu korrektuurimisel tähelepanu pöörata.



- Pöörake tähelepanu veidratele kirjavahemärkidele nagu `\*\*` või ``**``, mis võivad kujutada rasvase sümboli halba esitust. Allpool oleval pildil näete, et tärnid on ainult sõna paremal pool, mis näeb imelik välja.


![REVIEW](assets/en/9.webp)



Kontrollige alati ingliskeelset originaalteksti, et näha, kas rasvane tekst peaks seal olema. Sellisel juhul piisab, kui lisada lihtsalt kaks tärni sõna algusesse, et see oleks veebilehel korrektselt kuvatud. Tegelikult tuleb markdown-keeles rasvase teksti esitamiseks lisada kaks tärni ``**`` nii sõna/lause ette kui ka järele (vt näide allpool).



![REVIEW](assets/en/10.webp)




- Samad probleemid võivad tekkida selliste sümbolitega nagu $ ja `` ``.

Kontrollige kindlasti originaalkeele faili (sageli EN või FR), et näha, kus need sümbolid peaksid olema. Selles küsimuses võite alati küsida abi koordinaatorilt.



- Kui leiate tsitaate, uurige kindlasti internetis, et leida õige tõlge teie keeles. Tsitaadid sisestatakse tavaliselt pärast sümbolit ``>``.



![REVIEW](assets/en/11.webp)


## Viktoriini korrektuur


Kas teadsite, et saate ka viktoriiniküsimusi igas kursuses parandada? Näiteks kui soovite IT-õppeaine BTC101 viktoriiniküsimusi korrektuurida, võite avada spetsiaalse haru ja järgida seda teed: "kursused" -> "BTC101" -> "viktoriin" Sealt leiate kõik igale küsimusele pühendatud kaustad koos sellega seotud keelefailiga _yml_-vormingus.


Veenduge veel kord, et olete spetsiaalselt selleks otstarbeks avatud filiaalis ja teavitage alati koordinaatorit.


Pärast küsimuse läbivaatamist veenduge, et te muudate "läbivaadatud" staatuse "vale" asemel "tõeseks", nagu on näidatud alloleval pildil.


![REVIEW](assets/en/12.webp)


## Muud parimad tavad


Kui teil on vaja otsida konkreetseid sõnu teksti sees, võite klõpsata klahvile ``CTRL+F`` ja ilmub sektsioon Find-replace. See osa on väga kasulik, kui teil on vaja hüpata teksti konkreetse osa juurde või kui teil on vaja asendada konkreetseid sõnu/lauseid partiidena, ilma kogu sisu kerimata.



![REVIEW](assets/en/13.webp)



Kui kasutate funktsiooni "Asenda kõik", on oluline kontrollida tulemusi kaks korda, et veenduda, et ka linke ei ole muudetud. Näiteks kui soovite muuta sõna "Bitcoin" sõnaks "Bitkoin" (mis võib mõnes keeles olla vajalik), saate funktsiooni "replace all" abil tõhusalt uuendada kõiki tekstis olevaid juhtumeid. Kuid pidage meeles, et see tööriist muudab ka kõiki seda sõna sisaldavaid linke, mis võib põhjustada ümbersuunamisprobleeme.


Alljärgnevas näites kasutas korrektor ülaltoodud funktsiooni, et asendada "Satoshi" sõnaga "Satoshi(Sats)", ning muutis ka lingi, mis sisaldas seda sõna ise. Selle tulemusena muutus link kehtetuks.


![REVIEW](assets/en/14.webp)


Kui autor lisab lingi, mis viitab Plan ₿ Network kursusele, loob veebisait automaatselt "kaardi", mis näitab seotud pisipilti. Sellest tulenevalt veenduge alati, et teksti ja lingi enda vahele jääks tühik, vastasel juhul võib veebilehel ilmneda järgmine viga.


![REVIEW](assets/en/15.webp)




Lõpetuseks, teine parim tava, mida tuleks rakendada, kui olete oma korrektuuriülesande lõpetanud ja PR-i saatnud, on minna tagasi algsesse, koordinaatori poolt avatud küsimusse ja kommenteerida seda sõnadega "Korrektuur on tehtud". Veenduge, et lisate sinna ka oma PR-linki.


## Kokkuvõte


Kokkuvõtteks võib öelda, et kui olete teadlik tavalistest korrektuurivigadest, aitab see teil tõesti parandada oma oskusi sisu kontrollimisel. On lihtne jätta tähelepanuta selliseid asju nagu kontekst või järjepidevus, seega võib nende vigade tabamine teha suurt vahet. Pidage alati meeles, et algaja võib neid kursusi ja õpetusi lugeda, seega on meie kohustus tagada, et nad saaksid neist täielikult aru.


Aitäh, et lugesid selle õpetuse läbi, ja nautige oma korrektuuri teekonda!