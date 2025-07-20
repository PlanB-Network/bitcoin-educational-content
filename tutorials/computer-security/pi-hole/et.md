---
name: Pi-Auk
description: Reklaamblokeerija kogu teie võrgu jaoks
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian Duchemini originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___



## I. Esitlus



Me kõik oleme seda teinud kohe, kui käivitame oma lemmikbrauseri: paigaldame **reklaamblokeerija** (reklaamiblokeerija). Kuid kui kasutame teleribrauserit või Android-seadet jne... On veidi keerulisem leida midagi, mis töötab. Ja kui majas on rohkem kui üks seade, noh, siis tuleb toimingut iga brauseri puhul korrata!



Selles õpetuses lahendame lihtsa probleemi**: pakume reklaamblokeerijat kõigile meie võrgu masinatele ja haldame seda keskselt.**



Selleks kasutame selleks välja töötatud vahendit: **Pi-Hole**



Pi-Hole on DNS-i uputusauk. See kasutab teie seadmete tehtud DNS-päringuid, et kinnitada või keelata liiklus, kaitstes teid seega aadresside ja domeenide eest, mis on teadaolevalt levitavad reklaami, pahavara jne.



DNS tähendab domeeninimede süsteemi. Mis on siis domeeninimi? Noh, "it-connect.fr" on vaid üks näide. Domeeninimi on ühe või mitme ressursi unikaalne identifikaator, mida tavaliselt haldab üks üksus.



Masina nime ja domeeninime nimetatakse FQDN-ks (*Fully Qualified Domain Name*). See võimaldab teil jõuda konkreetse masinaga lihtsalt "helistades" sellele. Näiteks kui kirjutate "www.trucmachin.com", siis tegelikult kutsute masinat "www", mis kuulub domeenile "trucmachin.com".



Ainult et meie arvutid ei mõista inimkeelt, nad mõistavad ainult binaarsust, seega vajavad nad veebisaidile jõudmiseks IP Address, mis on samaväärne telefoninumbriga.



Nii et iga kord, kui sisestate veebilehe nime oma brauserisse või klõpsate lingil, küsib arvuti kõigepealt DNS-serverilt sellele nimele vastavat IP Address.



**Pi-Hole kontrollib neid päringuid (neid on iga päev sadu!) ja blokeerib automaatselt need, mis teadaolevalt sisaldavad reklaami või isegi pahatahtlikke faile



## II. Pi-Hole paigaldamine



Sellise nime nagu Pi-Hole puhul võib õigustatult eeldada, et teil on vaja Raspberry-Pi... Aga see ei ole päris tõsi. **Pi-Hole'i saab paigaldada mis tahes Linuxi arvutisse (Debian, Fedora, Rocky, Ubuntu jne.)



Teisest küljest tuleb meeles pidada, et **see seade peab töötama 24 tundi ööpäevas lihtsal põhjusel: pole DNS-i, pole internetti!** Vaarikas on seega hea mõte, sest see ei tarbi peaaegu üldse energiat.



Paigaldamiseks ühendage lihtsalt oma Linuxi masinaga SSH kaudu ja sisestage järgmine käsk kui "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Märkus**: tavatingimustes ei ole soovitatav "häkkida" skripti, ilma et teaksite kõigepealt, mida see teeb. Kui te ei ole kindel, minge lehele brauseriga või laadige sisu alla failina.
>


> ** Märkus: Debian 11 minimaalsetes versioonides ei ole Curl installeeritud, seega peate selle käsitsi installima käsuga **apt-get install curl** enne ülaltoodud käsu sisestamist.

Kui skript on käivitunud, viiakse läbi rida teste ja paigaldus ise hoolitseb enda eest:



![Image](assets/fr/019.webp)



Pi-Hole paigaldamine



Kui paigaldus on lõpule viidud, kuvatakse see ekraan:



![Image](assets/fr/020.webp)



Pi-Hole stardiekraan



> **Märkus**: kui kasutate oma masinas DHCP-d, saate selle kohta hoiatusteate. Loomulikult soovitame korralikuks kasutamiseks tungivalt määrata oma masinale fikseeritud IP-aadressi.

Pärast seda ekraani saate mõned infosõnumid ja seejärel viiakse teid konfigureerimisviisardisse, mis küsib esmalt, millisele DNS-serverile Pi-Hole päringuid edastab. Mina omalt poolt valisin Quad9, millel on kasutaja privaatsusleping.



![Image](assets/fr/021.webp)



DNS valik - Pi-Hole



> **Märkus: kui olete ettevõttes, on tõenäoline, et teie praegune DNS-server on Active Directory domeeni kontroller. Kuid ärge muretsege, te saate hiljem määrata tingimusliku ümbersuunaja enda valitud domeeni jaoks. Tavaliselt saad suunata kõik oma kohalikku domeeni puudutavad päringud ümber oma DNS-serverile.

Te märkate, et mõned valikud sisaldavad DNSSEC-variandi. Põhimõtteliselt ei ole DNS-protokoll turvaline (see ei olnud omal ajal seda silmas pidades kavandatud). DNSSEC lahendab selle probleemi, lisades Layer turvalisuse krüpteerimise ja allkirjastamise kaudu, nagu on selgitatud vastavas artiklis: [DNS Security](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Iga reklaamblokeerija tugineb oma töö tegemiseks ühele või mitmele nimekirjale. Pi-Hole on standardselt varustatud ühe nimekirjaga, nii et valige see ja lisage hiljem rohkem nimekirju.



![Image](assets/fr/022.webp)



Küsimus Interface veebi kohta, selle paigaldamine on vabatahtlik, kuna tööriistal on oma käsurea haldamiseks ja visualiseerimiseks. Kuid see Interface on üsna meeldiv ja hästi tehtud, nii et ma soovitan seda samal ajal paigaldada:



![Image](assets/fr/023.webp)



Kui paigaldate Pi-Hole'i masinale, millel on juba veebiserver, võite järgmisele küsimusele vastata "ei". Pange aga tähele, et selle toimimiseks on vaja PHP-d ja mitmeid mooduleid. Vastasel juhul paigaldatakse **lighttpd koos kõigi vajalike moodulitega**.



![Image](assets/fr/024.webp)



Seejärel küsitakse, kas soovite DNS-päringuid salvestada. **Kui soovite säilitada ajalugu, seadke selle väärtuseks jah; vastasel juhul seadke selle väärtuseks ei, kuid kaotate siis osa funktsionaalsusest** (vt järgmist ekraani).



![Image](assets/fr/025.webp)



Interface veebi jaoks kasutab Pi-Hole oma funktsiooni FTLDNS, mis pakub API-d ja genereerib DNS-päringutest statistikat. See funktsioon võib sisaldada "privaatsusrežiimi", mis maskeerib taotletud domeenid, taotluse taga olevad kliendid või mõlemad. Praktiline, kui soovite teha järelevalvet ilma inimeste privaatsust rikkumata või kui soovite lihtsalt järgida asjakohaseid eeskirju, kui kasutate seda avalikus võrgus.



![Image](assets/fr/026.webp)



Valik privaatne elustiil



Kui viimasele küsimusele on vastatud, teeb skript seda, mida ta peabki tegema: laadige alla GitHubi repositooriumid ja konfigureerige Pi-Hole. Paigaldamise lõpus kuvatakse kokkuvõttev ekraan olulise infoga:



![Image](assets/fr/027.webp)



Installeerimise kokkuvõttev ekraan



Märkige üles Interface veebiparool ja võrguandmed. Nüüd on aeg konfigureerida DHCP-teenus meie praeguses asukohas.



## III. DHCP konfigureerimine



Pi-Hole peab toimimiseks "lahendama" klientide DNS-päringuid, nii et nad peavad teadma, et see on see, kuhu neid saata. Selleks on mitu võimalust:





- Muutke oma DHCP-serveri DNS-sätteid (nt teie Box)
- Lülita see server välja ja kasuta Pi-Hole poolt pakutavat serverit
- Käsitsi muuta iga seadet, et kasutada Pi-Hole'i kui DNS-i



Mina isiklikult valin esimese lahenduse. Võimalik, et **sellul on DHCP server seal, kus sa oled** (tavaliselt sinu box). Nii et pole vaja vaeva näha.



Kuna võimalusi on väga palju, erinevate operaatorite bokside (mida ma kõiki ei tea) ja nende vahel, kellel on oma ruuter, ei hakka ma nende muudatuste kohta ekraanipilti esitama. Igal juhul pead sa minema DHCP seadistustesse ja muutma parameetrit "DNS", et lisada oma Pi-Hole IP Address.



Kui see on tehtud, siis kui mõni seade on varem sisse lülitatud, on need säilitanud vanad seaded, nii et peate konfiguratsioonitaotluse uuesti käivitama.



Windowsi tööjaamades, käsureaga :



```
ipconfig /renew
```



Linuxi tööjaamas :



```
dhclient
```



Kõigi teiste seadmete puhul tuleb need välja- ja uuesti sisse lülitada.



Nii et nad peaksid saama õiged parameetrid, et kontrollida:



```
ipconfig /all
```



DNS-väljal peaks olema teie Pi-Augu Address, minu puhul 192.168.1.42 :



![Image](assets/fr/029.webp)



## IV. Interface veebi Pi-Hole kasutamine



Haldamise hõlbustamiseks on **Pi-Hole** hästi kavandatud Interface veebi Interface. Kasutajasõbralik ja juurdepääsetav, see võimaldab teil :





- Vaadake päringute arvu, blokeeritud päringuid jne. reaalajas.
- Valge ja musta nimekirja haldamine
- Lisage staatilisi kirjeid, varjunimesid jne.
- Nimekirjade lisamine
- Ja palju muid funktsioone!



Omalt poolt kavatsen lisada blokeerimisnimekirja. Nagu eespool mainitud, paigaldati Soft-ga samal ajal ainult üks nimekiri. Reklaamsaitide jaoks on palju nimekirju, kuid kõige parem on valida vähemalt üks konkreetselt selle riigi jaoks, kus te elate. Üks tuntumaid nimekirju on **EasyList** ja üks neist on spetsiifiline Prantsusmaale: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Selle lisamiseks ühendage kõigepealt Interface administraatoriga: **http://<ip_du_PiHole>/admin**



Administraatori parool on juba loodud (vt installeerimise lõpu ekraanipilti), nii et Interface-le juurdepääsu saamiseks tuleb see vaid sisestada:



![Image](assets/fr/030.webp)



Interface alates Pi-Hole



Näeme näiteks, et Pi-Hole'iga on ühendatud kaks klienti, et see on töödelnud 442 päringut ja et 8 neist on blokeeritud. Need graafikud võivad olla hea teabeallikas, eriti professionaalses kontekstis.



Meie nimekirja lisamiseks minge menüüsse "**Rühma haldamine**" ja "**Liigid**":



![Image](assets/fr/031.webp)



Näeme meie esimest nimekirja "**StevenBlack**", et lisada meie oma, kopeeri link, mille andsin teile eespool ja sisestage see väljale "**Address**", kirjelduse jaoks valin panna nimekirja nime:



![Image](assets/fr/032.webp)



Loetelu lisamine Pi-Hole'is



Selle lisamiseks tuleb vaid klõpsata "**Lisata**". Selle aktiveerimiseks peame tegema täiendava sammu, et "hoiatada" Pi-Hole'i, et ta võtaks selle nimekirja üle. Selleks :





- Kasutage kas sisseehitatud käsurea
- Kas Interface veebi



Mina isiklikult valisin teise, sest kui te olete hoolikalt vaadanud, siis link PHP-skriptile, mis teostab uuenduse, on otse lehel, kus me oleme (sõna "online"). Seega tuleb vaid sellele klõpsata, mis viib teid leheküljele, kus on ainult üks võimalus:



![Image](assets/fr/033.webp)



Pärast lõpetamist kuvatakse leheküljel skripti tulemus, mis tähendab, et nimekiri on arvesse võetud (kui muidugi ei kuvata veateadet).



Nagu selle õpetuse alguses teatati, võimaldab Pi-Hole teil ka **blokeerida domeene, mis on tuntud pahavara levitajana. Selle funktsiooni tugevdamiseks soovitan teil lisada ka Abuse.ch** poolt levitatav regulaarselt uuendatud domeenide nimekiri, mis tugevdab märkimisväärselt teie võrgu turvalisust, mis on saadaval aadressil [see Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Loomulikult saate lisada mis tahes nimekirju, mida peate asjakohaseks, või hallata oma musta nimekirja käsitsi musta nimekirja menüü kaudu.



## V. Pi-aukude testid



Nüüd, kui kõik on paigas, tuleb vaid testida lahendust, et veenduda, et see töötab korralikult.



Näiteks püüan jõuda domeeni *http://admin.gentbcn.org/*, mis on Abuse.ch nimekirjas, sest see on tuntud pahavara vastuvõtjana:



![Image](assets/fr/034.webp)



Ilmselt olen ma kuskil blokeeritud. Et veenduda, et see on Pi-Hole, mis on teinud tööd, saame kontrollida päringulogi Interface veebis "Query Log", et näha, et see on blokeeritud nimekirjakandest:



![Image](assets/fr/035.webp)



## VI. Kokkuvõte



Selles õpetuses oleme näidanud, kuidas seadistada DNS-server, mis mitte ainult ei kõrvalda enamikku reklaame teie sirvimise mugavuse huvides, vaid lisab ka ** Layer turvalisust, blokeerides andmepüügi ja pahavara levitavad domeenid**.



Kõik see on tasuta ja ökonoomne, kui see on paigaldatud Raspberry-Pi-le (energiatarbimise seisukohast).