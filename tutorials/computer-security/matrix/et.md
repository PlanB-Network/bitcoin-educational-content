---
name: Maatriks
description: Juhend Matrixi, turvalise, avatud ja detsentraliseeritud sideplatvormi mõistmiseks, konfigureerimiseks ja kasutamiseks.
---

![cover](assets/cover.webp)



## Mis on Matrix?



Matrix on **detsentraliseeritud suhtlusprotokoll**, mis on loodud selleks, et võimaldada sõnumite, failide ja audio/videokõnede vahetamist kasutajate ja rakenduste vahel, sõltumata kesksest ettevõttest. Erinevalt traditsioonilistest sõnumivahetusplatvormidest on Matrix **avatud infrastruktuur**, mis on võrreldav e-postiga: igaüks võib ise valida serveri või hallata seda, säilitades samal ajal võimaluse vahetada teavet ülejäänud võrguga.



Maatriksit eristavad kolm põhiprintsiipi:



### Protokoll, mitte rakendus



Matrix ei ole selline rakendus nagu WhatsApp või Telegram.


See on standardiseeritud keel, mida saavad kasutada paljud rakendused.


Teisisõnu, mitmesugused Element tarkvara, FluffyChat, Cinny, Nheko ja teised pakuvad juurdepääsu samale Matrixi võrgule.



See tagab täieliku vabaduse: rakenduse muutmine ilma kontaktide kaotamiseta, liideste mitmekesisus, sõltumatus ühest tarnijast.



![capture](assets/fr/03.webp)



### Detsentraliseeritud, föderatiivne võrk



Matrixi struktuur põhineb **föderatsioonil**, mudelil, milles mitu sõltumatut serverit teevad omavahel koostööd.


Iga server (nimega _homeserver_) võib võõrustada kasutajaid, jututubasid ja sünkroonida sõnumeid teiste võrgus olevate serveritega.


Seega :





- ükski üksus ei kontrolli kogu süsteemi;
- server võib kaduda, ilma et see mõjutaks ülejäänud võrku;
- iga organisatsioon või üksikisik saab hallata oma ruumi.



See mudel tagab **kõrge vastupidavuse** ja peegeldab tehnoloogilise suveräänsuse väärtusi.



![capture](assets/fr/03.webp)



### Turvaline, krüpteeritud süsteem



Matrix toetab **lõppkrüpteerimist (E2EE)** privaatse teabevahetuse ja krüpteeritud rühmade jaoks.


Sõnumeid saavad lugeda ainult osalejad, mitte vaheserverid.


Selline lähenemine võimaldab suhelda ilma, et vahetuste sisu oleks kolmandale osapoolele avatud, säilitades samas protokolli läbipaistvuse ja võimaluse oma serveri majutamiseks.



![capture](assets/fr/05.webp)



### Ainulaadne koostalitlusvõime



Üks Matrixi peamisi eeliseid on tema võime tegutseda **sillana erinevate sidesüsteemide vahel**. Tänu _sildadele_ on võimalik ühendada :





- Telegram
- WhatsApp
- Signal
- Sõnumitooja
- Slack
- Discord
- IRC, XMPP jne.



See võimaldab ühendada mitmel platvormil hajutatud kogukondi, säilitades samal ajal kontrolli infrastruktuuri üle.



![capture](assets/fr/06.webp)



## Kuidas Matrix töötab?



Selles osas tutvustatakse Matrixi võrgu sisemist struktuuri, et mõista, kuidas kasutajad, serverid ja rakendused selles detsentraliseeritud ökosüsteemis omavahel suhtlevad. Matrix põhineb kolmel olulisel elemendil: _koduserverid_, identiteedid ja _kliendid_, mida kasutatakse suhtlemiseks.



### Servereid: homeserverid



Matrix töötab sõltumatutel serveritel, mida nimetatakse _homeserveriteks_.


Iga koduserver haldab :





- kasutajakontod, mida ta majutab,
- eravestlused ja salongid, milles need kasutajad osalevad,
- sünkroniseerimine teiste võrguserveritega.



Kõik Matrixi võrku ühendatud kodukasutajad vahetavad automaatselt sõnumeid ja sündmusi ühisest elutoast. Näiteks:





- serveris A registreeritud kasutaja saab vestelda serveris B asuva kasutajaga,
- salong võib olla jaotatud kümnete serverite vahel,
- keegi ei saa kontrollida salongi või kogukonda tervikuna.



See mudel on väga paindlik ja võimaldab igal organisatsioonil või üksikisikul hallata oma infrastruktuuri.



### Maatriksi tunnused



Igal kasutajal on unikaalne identifikaator, mida nimetatakse **MXID** (_Matrix ID_), mis näeb välja nagu aadress:



```bash
@nomdutilisateur:serveur.xyz
```



See koosneb järgmistest elementidest:





- kasutajanimi, mille ees on **@**
- selle serveri nimi, kus konto loodi, millele eelneb **:**



Näited:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



See identifikaator võimaldab suhtlemist mis tahes teise Matrixi kasutajaga, olenemata sellest, millisest serverist see pärineb.



### Maatrikskliendid (rakendused)



Matrixi kasutamiseks tuleb teil luua ühendus rakendusega nimega **klient Matrix**.



Tuntuimad on :





- Element (veeb, mobiilne, töölauaarvuti)
- FluffyChat (mobiilne)
- Cinny (minimalistlik veebi/lauaarvuti)
- Nheko (töölaud)



Need rakendused on vaid liidesed :





- sõnumite vaatamiseks,
- saata teksti, pilte või faile,
- liituda või luua messid,
- teha audio/videokõnesid.



Kõik rakendused suhtlevad serveritega sama standardiseeritud protokolli kaudu.



### Ruumid ja privaatsõnumid (DM)



Matrixis toimub vahetus **ruumides** :





- ruum võib olla avalik või privaatne
- sinna mahub kaks inimest või tuhandeid
- seda saab jagada mitme serveri vahel
- sellel on unikaalne identifikaator, mis algab tähega **!**



Erasõnumid on lihtsalt kahe osalejaga jututubades, mida sageli nimetatakse **DM (Direct Messages)**.



Salongide sünkroniseerimine toimub osalevate serverite vahel reaalajas, tagades õmblusteta kogemuse, säilitades samal ajal detsentraliseerituse.



## Miks kasutada Matrixi?



Matrix ei ole lihtsalt alternatiiv tsentraliseeritud sõnumivahetussüsteemidele: see on tehnoloogia, mis vastab tegelikele vajadustele digitaalse suveräänsuse, turvalisuse ja koostalitlusvõime osas. On palju põhjusi, miks üha rohkem inimesi, ettevõtteid ja asutusi valivad suhtlemiseks selle protokolli.



### Võta tagasi kontroll oma kommunikatsiooni üle



Enamik sõnumiplatvorme töötab tsentraliseeritud mudelil: üks mängija kontrollib servereid, juurdepääsu, andmeid ja kasutuseeskirju. See mudel tähendab täielikku sõltuvust tarnijast.


Matrix kasutab teistsugust lähenemist.


Igaüks võib valida, kus ta oma kontot haldab, või isegi oma serveri kasutusele võtta. Ükski üksus ei ole võimeline kasutajat blokeerima, nõudma pealetükkivat tuvastamist või kehtestama poliitika muutmist.


Selline arhitektuur annab autonoomia tagasi nii üksikisikutele kui ka organisatsioonidele. Kommunikatsioon ei põhine enam usaldusel ettevõtte vastu, vaid avatud, dokumenteeritud ja kontrollitaval protokollil.



### Turvaline, krüpteeritud side



Matrix toetab privaatsete vestluste ja rühmade läbivat krüpteerimist. See mehhanism tagab, et ainult osalejad saavad sõnumeid lugeda, isegi kui need läbivad kolmanda osapoole servereid föderatsioonis.



Protokollis kasutatakse Megolm/Olm algoritmi, mis on loodud spetsiaalselt tugeva turvalisuse tagamiseks hajutatud, mitme seadmega keskkondades.



See võimaldab :





- kaitsta tundlikke vestlusi,
- vältida volitamata juurdepääsu (isegi vastuvõtva serveri poolt),
- säilitada konfidentsiaalsus pikemas perspektiivis.



Krüpteerimine ei ole valikuvõimalus: see on protokolli põhikomponent.



### Ei sõltu enam ühest rakendusest



Matrix ei ole rakendus, vaid protokoll.



Selline klientide mitmekesisus tagab :





- individuaalsetele vajadustele kohandatud valik,
- võimalus kasutada Matrixi mis tahes tüüpi seadmes,
- ei sõltu ühest tarkvarast.



Kui klient ei sobi või lõpetab oma tegevuse, valige lihtsalt teine klient: konto jätkab tööd tavapäraselt.



### Erinevate kogukondade koondamine ja ühendamine



Föderatsioon võimaldab erinevatel serveritel töötada koos, kuid neid hallata iseseisvalt.


Seega :





- organisatsioon saab hallata oma koduserverit,
- üksikisikud saavad liituda avalike serveritega,
- kõik saavad omavahel suhelda, nagu oleksid nad ühel ja samal platvormil.



Selline paindlikkus võimaldab luua igale vajadusele kohandatud suhtlusruume: meeskonnad, ühendused, kogukonnad, institutsioonid või avatud lähtekoodiga projektid.



Matrix on eriti populaarne tehnilistes ringkondades, aktivistide kollektiivides, teadlastes, valitsustes ja üha enam ka Bitcoin kogukondades.



### Ainulaadne koostalitlusvõime sõnumside maastikul



Üks Matrixi peamisi eeliseid on selle võime **laiendada** vahetusi tänu sildadele, mis on võimelised ühendama :





- WhatsApp
- Telegram
- Signal
- Slack
- Discord
- IRC
- XMPP
- ja paljud teised platvormid



Matrixist saab seega kommunikatsiooni ühendav kiht, mis ühendab mitmeid eri rakenduste kaudu hajutatud kogukondi.



Selline koostalitlusvõime vähendab killustatust ja lihtsustab koostööd.



### Vaba, avatud ja jätkusuutlik protokoll



Matrixi protokoll on täielikult avatud lähtekoodiga ja läbipaistvalt välja töötatud.


See tagab mitmeid eeliseid:





- standardi pidev areng,
- võimalus, et igaüks saaks koodi kontrollida,
- sõltumatus kaubanduslikest või poliitilistest muutustest,
- pikaajaline vastupidavus.



Erinevalt patenteeritud sõnumsüsteemidest ei sõltu Matrixi tulevik ühest ettevõttest, vaid ülemaailmsest kogukonnast ja avatud standardist.



## Kuidas luua Matrixi konto?



Matrixi konto loomine on lihtne ja ei nõua tehnilisi oskusi. Kasutajad saavad liituda olemasoleva serveriga, luua sisselogimise ja alustada kohe vestlust. Selles jaotises kirjeldatakse põhilisi samme.



### Valige server (avalik või privaatne)



Matrix on föderatiivne võrk: seal on arvukalt servereid (homeservereid), mida haldavad erinevad organisatsioonid, kogukonnad või üksikisikud. Serveri valik määrab ainult selle, _mis_ kontot majutatakse, kuid ei takista suhtlemist kogu võrguga.


**Kaks võimalust on saadaval:**



### - Kasutage avalikku serverit



See on kõige lihtsam lahendus.


Näiteid populaarsetest serveritest:





- _matrix.org_ (tuntuim)
- _envs.net_
- temaatilised kogukonna serverid (tehnoloogia, privaatsus, avatud lähtekood...)



Need serverid sobivad algajatele kasutajatele, kes soovivad kiiresti registreeruda.



### - Kasutage privaatserverit



Sobib ideaalselt :





- organisatsioon,
- perekond,
- avatud lähtekoodiga projekt,
- töömeeskond,
- või suveräänseks, iseseisvaks kasutamiseks.



Sellisel juhul peab keegi haldama serverit (Synapse, Dendrite, Conduit...).


Olenemata sellest, millise serveri te valite, saavad kasutajad tänu föderatsioonile omavahel suhelda.



### Konto loomine samm-sammult



Kuna Matrix on avatud protokoll, saavad sellele juurdepääsu mitmed rakendused.


Nagu eespool kirjeldatud, pakuvad nad erinevaid liideseid ja funktsioone sõltuvalt nõuetest:





- Element**: kõige täiuslikum klient, mis on saadaval kõigil platvormidel.
- FluffyChat**: lihtne, kaasaegne ja ideaalne mobiiltelefonidele.
- Nheko**: kerge, ergonoomiline klient arvutitele.
- SchildiChat**: Elementi variant ergonoomiliste parandustega.
- NeoChat**: integreeritud KDE ökosüsteemi.



Kliendi valik ei mõjuta kontot: kõik töötavad mis tahes Matrixi serveriga.



### Klassikalised sammud :





- Avage valitud rakendus. Meie puhul teeme seda [Element](app.element.io).
- Valige "Loo konto".



![cover-kali](assets/fr/10.webp)



Lihtsuse huvides võite luua Matrixi konto, kasutades **Google'i, Facebooki, Apple'i, GitHubi või GitLabi**. Need teenused teavad ainult, et nende kontot on kasutatud Matrixile juurdepääsuks: seda nimetatakse **sotsiaalseks ühenduseks**.



Suurema konfidentsiaalsuse tagamiseks saate registreeruda ka käsitsi, valides **kasutajanime**, **salasõna** ja **siaadressi**.



Sõltuvalt valitud serverist võib olla vajalik **captcha** ja **kasutustingimuste** aktsepteerimine.



Kui registreerimine on kinnitatud, saadetakse kinnitav e-kiri.


Klõpsake lihtsalt lingil, et aktiveerida oma konto ja pääseda veebirakendusse (Element), et liituda oma esimeste Matrixi vestlustega.



![cover-kali](assets/fr/11.webp)



Teil on nüüd konto ja te kasutate Elementi veebiversiooni.



## Lisage oma esimene kontakt



Selleks, et kellegagi Matrixis suhelda, on vaja teada vaid tema täielikku identifikaatorit, mida nimetatakse **Matrix ID**.



Näide:



`@alice:matrix.org @bened:monserveur.bj`



### Lisa kontakt



Sõprade kutsumiseks grupivestlusse klõpsake paremas ülanurgas oleval "i" ringil. See avab parempoolse paneeli. Klõpsake nupule "Inimesed", et kuvada selles ruumis olevate liikmete nimekiri: praegu peaksite olema kohal ainult teie.



![cover-kali](assets/fr/12.webp)



Klõpsake inimeste loendi ülaosas nupule "Kutsu sellesse ruumi" ja avaneb üleskutse, mille abil saate oma sõpru Matrixi kutsuda. Kui nad on juba Matrixi sisse logitud, sisestage nende Matrixi ID. Kui nad ei ole, sisesta nende e-posti aadress ja nad kutsutakse liituma.



Sõprade süsteemi ei ole: kontakt on lihtsalt inimene, kellega on avatud vestlus.



![cover-kali](assets/fr/13.webp)



Kutsutud isik saab kutse kas vastu võtta või sellest keelduda. Kui ta võtab kutse vastu, peaksite nägema, et ta liitub ruumiga. Mida rohkem, seda parem!



![cover-kali](assets/fr/14.webp)



### Oma serveri seadistamine



Matrix tuleb omaette, kui seda kasutatakse koos isikliku serveriga.


Oma koduserveri kasutuselevõtt võimaldab teil :





- säilitada täielik kontroll andmete üle,
- määratleda oma kasutuseeskirjad,
- hostida mitmeid kontosid (sõbrad, meeskond, kogukond),
- ja tagada maksimaalne vastupidavus piirangute või tsensuuri korral.



**Võimalikud lahendused:**





- Synapse**: ajalooline ja kõige täielikum rakendamine.
- Dendrite**: kergem, võimsam ja mõeldud protokolli tuleviku jaoks.
- Conduit**: minimalistlik variant, mida on lihtne kasutusele võtta.



**Eeldused:**





- domeeninimi,
- masin või VPS,
- minimaalne süsteemi administreerimise oskus.



Isegi kui see nõuab veidi seadistamist, muudab oma serveri haldamine Matrixi suveräänseks ja vastupidavaks tööriistaks.



### Oma esimestel messidel osalemine



Matrix tugineb suuresti _ruumidele_ (eluruumidele).


Toimuvad avalikud, era-, kogukonna-, tehnilised, kohalikud ja rahvusvahelised messid.



**Kolm võimalust salongiga liitumiseks:**



1. **Kutselink** (sageli "matrix.to" URL-i kujul).


2. **Salongi nime otsimine** taotluses.


3. **Etendades kogu saate ID**, nt :


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Pärast liitumist käitub jututuba nagu klassikaline uudistegrupp, kus on sõltuvalt kasutatavast kliendist olemas ajalugu, krüpteerimine, failid, reaktsioonid ja audio-/videokõned.



![capture](assets/fr/09.webp)



## Edasi minna



Kui olete põhitõed omandanud, pakub Matrix hulgaliselt edasijõudnute võimalusi. Kas soovite ühendada teisi sõnumsüsteeme, majutada oma serverit või korraldada kogukonda, ökosüsteem on väga rikkalik.



### Sillad (WhatsApp, Telegram, Signal jne)



Sild ühendab Matrixi teiste sõnumivahetussüsteemidega.


Selle abil saate saata ja vastu võtta sõnumeid :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discord
- Slack**
- IRC** (IRC)
- ja paljud teised



### Mida sildade abil saab teha





- Tsentraliseeri kõik oma vestlused Matrixis
- Avatud liidese loomine, et suhelda omatavate teenustega
- Halda mitmeplatvormilist kogukonda ühest kohast



Mõned sillad on ametlikud, teised kogukonnapõhised.


Sõltuvalt osakonnast võivad nad nõuda :





- isiklik server,
- täiendav konfiguratsioon,
- või olemasoleva avaliku silla kasutamine.



### Matrixi kasutamine Bitcoin organisatsiooni, kogukonna või projekti jaoks



Matrix ei ole ainult isiklik vahend.


Seda saab kasutada töörühmade struktureerimiseks, kohalike kogukondade korraldamiseks või projektikommunikatsiooni haldamiseks.



**Kasutamisnäited:**





- Avatud lähtekoodiga kogukonnad
- Bitcoin ja Lightning ökosüsteemi projektid
- Üliõpilaste või arendajate rühmad
- Kodanikuorganisatsioonid
- Sõltumatu meedia
- Kohalikud rühmad ja ühendused



**Miks on see huvitav?





- 100% avatud lähtekoodiga** tööriist
- Suveräänne ja detsentraliseeritud** side
- Ruumid, mis on jaotatud **ruumidesse**, **alagruppidesse**, **privaatruumidesse** jne.
- Integreerige Nextcloudi, GitLabi, Mattermosti või kohandatud robotitega
- Õiguste ja modereerimise peenhäälestatud haldamine



Matrix saab siis kommunikatsioonisambaks igale struktuurile, mis soovib jääda sõltumatuks suurtest tsentraliseeritud platvormidest.



## Kokkuvõte



Matrix kujutab endast kaasaegset, avatud ja turvalist lahendust reaalajas suhtlemiseks, pakkudes detsentraliseeritud alternatiivi traditsioonilistele platvormidele. Tänu oma föderatiivsele arhitektuurile ja täiustatud krüpteerimisprotokollidele võimaldab see kasutajatel säilitada kontrolli oma andmete üle, nautides samal ajal sujuvat ja koostalitlusvõimelist kogemust. Olenemata sellest, kas Matrix on mõeldud isiklikuks, professionaalseks või kogukondlikuks kasutamiseks, pakub see töökindlat ja skaleeritavat raamistikku tänapäeva vajadustele kohandatud suhtluskeskkondade loomiseks.



Lisateavet ja kõiki Matrixi pakutavaid funktsioone saate lugeda ametlikust dokumentatsioonist, mis on saadaval siin :


[https://matrix.org/docs/](https://matrix.org/docs/)