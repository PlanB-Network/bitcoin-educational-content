---
name: Korrektuuri suunised
description: Millised on olulised tegurid, mida tuleb Plan ₿ Network korrektuuris silmas pidada?
---

![github](assets/cover.webp)


Tere tulemast selle õpetuse juurde, mis käsitleb **juhiseid, mida tuleb järgida Plan ₿ Network sisu korrektuurimisel**. Meil on hea meel, et jagate meie missiooni tõlkida Bitcoin materjale võimalikult paljudesse keeltesse, et aidata inimestel saada teada, kuidas see toimib ja kuidas seda igapäevaelus kasutada.


Kõigepealt annab Plan ₿ Network [avalik repositoorium] (https://github.com/PlanB-Network/Bitcoin-educational-content) panustamine teile võimaluse kirjutada õpetusi, parandada olemasolevat sisu või isegi teha ettepanekuid uue keele lisamiseks platvormile. Et rohkem teada saada, liitu kõigepealt meie [Telegram Group](https://t.me/PlanBNetwork_ContentBuilder) ja kirjuta lühike tutvustus enda ja keelte kohta, mida sa oskad.


Käesolev juhendmaterjal on pühendatud kaastöötajatele, kes soovivad sisu korrigeerida. Enamik neist ei tea palju [Githubist](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ega [Markdown keelest](https://www.markdownguide.org/basic-syntax/), mida me repositooriumi sees kasutame, seega on oluline jagada mõningaid teadmisi selle ülesandega seotud võtmeteguritest.


Allpool olen kogunud kokku kõige levinumad probleemid, millega korrektorid kokku puutuvad. Võite vabalt soovitada rohkem, sest see võib aidata teisi parandada.


Enne spetsiifikatesse sukeldumist tuleks kõigepealt lugeda seda õpetust praktiliste tegevuste kohta Githubis, mida tuleb järgida Plan ₿ Network repositooriumi hargnemise, muudatuste tegemise ja PR-i saatmise teel:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6


## Mis on korrektuur?


Korrektuur on kirjaliku teksti lõplik läbivaatamine, mille käigus tuvastatakse ja parandatakse grammatika-, õigekirja-, kirjavahemärgistamise ja vormindamise vead. Sellega tagatakse, et tekst on enne avaldamist või esitamist selge, sidus ja vigadeta.


Seda tüüpi ülesannete lahendamisel on oluline järgida originaalkeele (EN või FR) tähendust, kuid veenduda, et tekst lõplikus keeles oleks emakeeleõppija jaoks võimalikult sujuv.


Pidage alati meeles, et tõlkimine/korrektsioon on ÕPPE!


Tegelikult on meie ühine eesmärk harida võimalikult paljusid inimesi Bitcoin kohta, seega on oluline, et materjal, mida nad loevad, oleks sujuv ja selge.

Selles mõttes on kõik Plan ₿ Network-le kaasaaitajad haridustöötajad!


## Esimesed sammud enne Plan ₿ Network korrektuuri tegemist


Enne uue korrektuuriülesande alustamist teatage sellest [Telegrammi grupis](https://t.me/PlanBNetwork_ContentBuilder) või teavitage sellest oma Plan ₿ Network koordinaatorit, kes avab spetsiaalse [issue](https://github.com/orgs/PlanB-Network/projects/3). Kui saate teema lingi, lihtsalt **kommenteerige, et alustate** selle sisu korrektuuriülesandega.


See süsteem aitab koordinaatoril jälgida repo sisemist arengut ja võimaldab korrektori poolt sisu "nõuda", vältides sellega kellegi teise topeltpüüdeid.

Teemal ise leiate lingid, mis suunavad teid sisu kontrollimiseks. Võite lihtsalt nendele klõpsata või, mis veelgi parem, võite minna tagasi oma enda forkeeritud repo juurde ja töötada otse sealt edasi. Vaatame, kuidas seda teha saab!


Kõigepealt, **AJALGI ärge unustage oma repo SYNC-i, "dev" haru**. Nii on sisu alati uuendatud, enne kui alustate mis tahes tüüpi ülesannet, ja te ei tekita konflikte vana ja uue materjali vahel. Klõpsake kindlasti "Sync Fork" ja "Update branch".



![REVIEW](assets/en/1.webp)



Pärast edukat sünkroniseerimist saate otse juurdepääsu huvipakkuvale sisule ja teha uue haru kinnituse, nagu on näidatud selles [õpetuses](https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). Vastasel juhul saate avada uue haru, kus töötada, klõpsates "Branches", nagu allpool näidatud.



![REVIEW](assets/en/2.webp)



Sellel uuel lehel leiate kõik juba avatud filiaalid pealkirja "Teie filiaalid" all. See jaotis on väga kasulik, sest see võimaldab teil hõlpsasti leida, kus te olete mingit sisu muutnud. Kui soovite avada uue haru, võite klõpsata lehe paremas ülanurgas nupule "New Branch".



![REVIEW](assets/en/3.webp)



Seejärel avaneb hüpikaken, kuhu tuleb sisestada uue haru nimi. Allpool esitatud juhul valisin selle nimeks "BTC101-FR". Nii jääb mulle alati meelde, et seda konkreetset haru tuleb kasutada prantsuse keele kursuse BTC101 korrektuuri tegemiseks ja **ei kasuta seda ühegi teise ülesande jaoks**.


Soovitan teil teha sama: avage kindlasti uus haru alati, kui teil on vaja alustada uut ülesannet.



![REVIEW](assets/en/4.webp)



Pärast selle uue haru loomist klõpsake seda kindlasti eelmisel lehel "Teie harud" ja alustage tööd konkreetse sisuga seotud *.md* failiga (minu puhul klõpsan ma "kursused" -> "BTC101" -> "fr.md"). Kõik selle konkreetse failiga seotud kommiteerimised tuleb kinnitada (salvestada) sama haru sees.



## Originaalkeel või tõlge?


Kui teete sisu korrektuuri, siis on oluline **selle originaalversiooni inglise (või prantsuse)** alati kontrollida. Olge teadlik, et me tõlgime tehisintellekti keeletööriistade abil, seega ei pruugi sihtkeele esitus olla sujuv või lõpplugejale hästi arusaadav.


Seega võite vabalt teha tekstis kohandusi ja muuta vajadusel lauseid. Meie eesmärk on suurendada voolavust, kuid alati järgida algset tähendust. Kui teil tekib kahtlusi, kuidas mingit sõna käsitleda, küsige kindlasti tõlkekoordinaatorilt.


LLM-vahendid võivad tõlkida mõned Bitcoinga seotud sõnad sõna-sõnalt, nagu Lightning Network. Eriti kehtib see juhul, kui tegemist on väga tehniliste sõnadega. Sellistel juhtudel on soovitav parema selguse huvides säilitada ingliskeelne originaalsõna sihtkeeles, välja arvatud juhul, kui teie keelereeglid nõuavad iga sõna tõlkimist.


Teisel juhul **uurige alati, kas keegi teine teie Bitcoin kogukonnas on selle sõna juba tõlkinud** ja kas seda sõna kasutatakse nüüd laialdaselt.



- Üks lahendus võiks olla **kontroll [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page)** sihtkeeles, et näha, kas sõna on tõlgitud või mitte. Kui ei ole, siis jätke sõna inglise keelde.



- Igal juhul oleks minu soovitus **lisada EN-sõna siiski**, lisades sihtkeele vastava tähenduse ümmarguste sulgude sees, järgides skeemi EN (LANG), või vastupidi. Ex. Address (indirizzo) või indirizzo (Address).



- Teine hea lahendus on säilitada ET originaalsõna/fraas, seejärel **luuakse hüperlink**, mis suunab ümber [sõnastik](https://planb.network/en/resources/glossary) planb.networki. Selleks tuleb sõna/fraas sisestada nurksulgude sisse ja link ümmarguste sulgude sisse, nagu on näha alljärgnevas näites:


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


Lõpptulemusena (pilt allpool) ei visualiseerita kogu linki ja sõna muutub klikitavaks.



![REVIEW](assets/en/5.webp)



Pange tähele, et sõnastiku link, mille võtate veebilehelt, sisaldab keelekoodi pärast sõna "network" (näide: ``https://planb.network/en/resources/glossary/UTXO``-> siin on keelekood "en"). Sellisel juhul **kustutage lingilt keelekood**, nagu näete ülalpool toodud kastis. Nii viib süsteem lugeja automaatselt tema määratud keelde.


Hoiukoha sisu on täis selliseid hüperlinke nagu eespool kirjeldatud. Nüüd, kui te teate, mida need tähendavad, **jälgige, et mitte kustutada ühtegi algse autori poolt lisatud linki**.



- Teine asi, mis on seotud sõnade esitamisega, on järgmine. Kui te leiate tekstis sõna "Plan ₿ Network", **jätke see sellisel kujul**. Ärge tõlkige sõna "plaan" ega sõna "võrk". Peale selle ärge kasutage Plan ₿ Network tutvustamisel artiklit "The": **Käsitlege seda kui kaubamärki**.



- Sama kehtib ka "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", mis tuleks samuti säilitada algsel kujul.


Üks viimane märkus selle lõigu juurde: nagu eespool öeldud, kasutame sisu tõlkimiseks tehisintellekti vahendeid ja seejärel palume kaastöötajate sekkumist, et kõik oleks sujuv ja hästi korrektuuritud.


Kui te kasutate tehisintellekti enamiku teksti korrektuuriks, märkame seda kindlasti, sest oleme tuttavad tüüpiliste lausekonstruktsioonidega, mida tehisintellekt genereerib. Kui me avastame, et tuginesite korrektuuris ainult tehisintellektile, ilma et oleksite teinud olulisi muudatusi, võib Sats lõplik tasu väheneda poole võrra!



## Pealkirjade struktuur


Markdown-keeles algavad pealkirjad (ja lõike pealkirjad) kõik Hash märgiga ``#``. Hash märkide arv vastab pealkirja tasemele. Näiteks on kolmanda taseme pealkirjal kolm numbrimärki enne teksti (nt `### Minu pealkiri`).


Kursustel tutvustatakse kõige olulisemaid osi ühe Hash märgiga, samas kui allosad võivad olla kahest kuni nelja Hash märgiga. Õpikutes kasutame tavaliselt ainult kahe Hash märgiga pealkirju.



![REVIEW](assets/en/6.webp)



Veenduge, et **KUNAGI ei kustutata Hash märke** enne pealkirja, sest muidu tekitab see probleeme teksti struktuuriga.


Samal ajal, **ei tohi muuta** chapterID osa, mida näete ülaloleval pildil, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` või videoviiteid nagu ``::::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8b8cc8::::``.


Kui me sisestame pealkirja ette "#", muutub see automaatselt kursuse eelvaates paksuks, nii et **vältige pealkirjade paksuks muutmist parandamise ajal**.


Kõrvalmärkusena olgu öeldud, et kursuste EN-keeles on **pealkirjad, mida juhatab sisse üks või kaks ``#``, kõik sõnad algavad suurtähtedega**, samas kui pealkirjad, mis algavad kolme või nelja ``#``ga, tavaliselt seda reeglit ei järgi. Kui võimalik, veenduge, et teie sihtkeele pealkirjad järgiksid seda struktuuri.



## Kursuste esialgne osa


Iga sisu alguses on järgmised staatilised väiketähtedega sõnad: "nimi", "kirjeldus", "eesmärgid". Veebisait kasutab neid sisu enda dekodeerimiseks ja need on **sellele alati jäetud**. Sellest tulenevalt EI TOHI neid tõlkida, sest vastasel juhul tekitab sisu sünkroniseerimisprobleeme. Kontrollige kindlasti ainult koolonile järgnevat osa, mille AI tõlgib automaatselt.



![REVIEW](assets/en/7.webp)



Hoidke selles samas esialgses osas formaat nii, nagu see on. Ärge lisage teksti algusesse midagi. Vältige näiteks "tt" lisamist enne kriipsu, nagu alloleval pildil!



![REVIEW](assets/en/8.webp)



## Soovitused vormingu kohta


Allpool on toodud mõned näited vorminguprobleemide kohta, millele sihtkeeles sisu korrektuurimisel tähelepanu pöörata.



- Pöörake tähelepanu veidratele kirjavahemärkidele nagu `\*\*` või ``**``, mis võivad kujutada rasvase sümboli halba esitust. Allpool oleval pildil näete, et tärnid on ainult sõna paremal pool, mis näeb imelik välja.



![REVIEW](assets/en/9.webp)



Seega kontrollige alati ingliskeelset originaalteksti, et näha, kas rasvane tekst peaks seal olema. Sellisel juhul lisage lihtsalt kaks tärni sõna algusesse, et see oleks veebilehel õigesti kuvatud. Tegelikult tuleb markdown-keeles **paksuse esitamiseks lisada kaks tärni ``**`` nii enne kui ka pärast sõna/lause** (vt näide allpool).



![REVIEW](assets/en/10.webp)




- Samad probleemid võivad tekkida selliste sümbolitega nagu $ ja `` `` ``.

Kontrollige kindlasti originaalkeele faili (sageli EN või FR), et näha, kus need sümbolid peaksid olema. Selles küsimuses võite alati küsida abi koordinaatorilt.



- Kui leiate tsitaate, uurige kindlasti internetis, et leida õige tõlge oma keelde. Tsitaadid sisestatakse tavaliselt pärast sümbolit ``>``.



![REVIEW](assets/en/11.webp)



## Viktoriini korrektuur


Kas teadsite, et saate ka iga kursuse viktoriiniküsimusi parandada? Näiteks kui soovite IT-õppeaine BTC101 viktoriiniküsimusi korrektuurida, võite avada spetsiaalse haru ja järgida seda teed: "kursused" -> "BTC101" -> "viktoriin". Sealt leiate kõik igale küsimusele pühendatud kaustad koos sellega seotud _yml_-vormingus keelefailiga.


Veenduge veel kord, et olete spetsiaalselt selleks otstarbeks avatud filiaalis ja teavitage alati koordinaatorit.


Pärast küsimuse läbivaatamist veenduge, et te muudaksite "läbivaadatud" staatuse "vale" asemel "tõeseks", nagu on näidatud alloleval pildil.



![REVIEW](assets/en/12.webp)


## Sõnastiku korrektuur


Nii nagu viktoriinide puhul, saate ka sõnastiku korrektuuri teha. Esialgne sõnastik on kirjutatud prantsuse keeles, seega leiate sealt selliseid lauseid nagu: "Prantsuse keeles võib seda väljendit tõlkida..."


Sellisel juhul kohandage see lause oma sihtkeelele või inglise keelele.


## Muud parimad tavad



- Kui teil on vaja otsida konkreetseid sõnu teksti sees, võite klõpsata klahvile ``CTRL+F`` ja ilmub sektsioon Find-replace. See osa on väga kasulik, kui teil on vaja hüpata teksti konkreetse osa juurde või kui teil on vaja asendada konkreetseid sõnu/lauseid partiidena, ilma kogu sisu kerimata.



![REVIEW](assets/en/13.webp)



Kui kasutate funktsiooni "Asenda kõik", on oluline kontrollida tulemusi kaks korda, et veenduda, et ka linke ei ole muudetud. Näiteks kui soovite muuta sõna "Bitcoin" sõnaks "Bitkoin" (mis võib mõnes keeles olla vajalik), saate funktsiooni "replace all" abil tõhusalt uuendada kõiki tekstis olevaid juhtumeid. Kuid pidage meeles, et see tööriist muudab ka kõiki seda sõna sisaldavaid linke, mis võib põhjustada ümbersuunamisprobleeme.


Alljärgnevas näites kasutas korrektor ülaltoodud funktsiooni, et asendada "Satoshi" sõnaga "Satoshi(Sats)", ning muutis ka lingi, mis sisaldab seda sõna ise. Selle tulemusena muutus link kehtetuks.


Kontrollige alati kahekordselt kõiki tekstis olevaid hüperlinke, et veenduda, et need on õiged.



![REVIEW](assets/en/14.webp)




- Kui autor lisab teemale järgneva lingi, mis viitab Plan ₿ Network kursusele või õpetusele (**ei** sulgudes), loob veebisait automaatselt "kaardi", mis näitab seotud pisipilti. Sellest tulenevalt veenduge alati, et **teksti ja lingi enda** vahel on tühik, vastasel juhul võib veebisaidil ilmneda järgmine viga.



![REVIEW](assets/en/15.webp)





- Lõpetuseks, teine parim tava, mida tuleks rakendada, kui olete oma korrektuuriülesande lõpetanud ja PR-i saatnud, on minna tagasi algsesse, koordinaatori poolt avatud küsimusse ja kommenteerida seda sõnadega "Korrektuur on tehtud". **Vältige, et lisate sinna ka oma PR-linki**.



## Kokkuvõte


Kokkuvõtteks võib öelda, et kui olete teadlik tavalistest korrektuurivigadest, aitab see teil tõesti parandada oma oskusi sisu kontrollimisel. Lihtne on jätta tähelepanuta selliseid asju nagu kontekst või järjepidevus ning nende vigade avastamine võib teha suurt vahet.


Pidage alati meeles, et algaja võib neid kursusi ja õpetusi lugeda, seega on meie kohustus tagada, et nad saaksid sellest täielikult aru. Korrektorina oled sa õpetaja!


Aitäh, et lugesid selle õpetuse läbi, ja nautige oma korrektuuri teekonda!