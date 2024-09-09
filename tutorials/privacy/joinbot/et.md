---
name: JoinBot
description: JoinBot'i mõistmine ja kasutamine
---

![DALL·E – samurai robot punases metsas, 3D renderdus](assets/cover.webp)

***HOIATUS:** Pärast Samourai Wallet'i asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil **ei ole JoinBot teenus enam saadaval**. Praeguse seisuga ei ole võimalik seda tööriista kasutada. Siiski on võimalik teostada Stonewall X2 tehinguid, kuid selleks on vaja leida koostööpartner ja vahetada käsitsi PSBT-sid. Sõltuvalt juhtumi arengust võidakse see teenus järgnevatel kuudel taaskäivitada.*

_Jälgime selle juhtumi arenguid ning sellega seotud tööriistade arenguid tähelepanelikult. Kinnitame, et uuendame seda õpetust, kui saabub uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

JoinBot on uus tööriist, mis on lisatud Samourai Wallet'i komplekti viimase uuendusega 0.99.98f tuntud Bitcoin'i rahakott tarkvaras. See võimaldab teil hõlpsasti teha koostööd tehinguid, et optimeerida oma privaatsust, ilma et peaksite partnerit otsima.

*Tänu suurepärasele Fanis Michalakis'ele idee eest kasutada DALL-E'd pisipildi jaoks!*

## Mis on koostööd tehing Bitcoin'is?

Bitcoin põhineb jaotatud ja läbipaistval kontoraamatul. Igaüks on võimeline jälgima selle elektroonilise rahasüsteemi kasutajate tehinguid. Teatud privaatsustaseme tagamiseks võivad Bitcoin'i kasutajad teha tehinguid spetsiifilise struktuuriga, et lisada nende tõlgendamisse usutavat eitamist.

Idee ei ole otseselt teabe varjamine, vaid selle segamine teiste seas. Seda eesmärki kasutatakse Coinjoins tehingutes, mis katkestavad mündi ajaloo Bitcoin'is ja muudavad selle jälgimise keerukaks. Selle tulemuse saavutamiseks tuleb tehingus luua mitu sama summa sisendit ja väljundit.

Sisendid on Bitcoin'i tehingu sisendid ja väljundid esindavad väljundeid. Tehing tarbib oma sisendid, et luua uued väljundid, muutes mündi kulutamise tingimusi. See mehhanism võimaldab bitcoine kasutajate vahel liigutada.
Arutlen seda üksikasjalikult selles artiklis: Bitcoin'i Tehingu Meehanism: UTXO, Sisendid ja Väljundid.

Üks viis jälgede segamiseks Bitcoin'i tehingus on teha koostööd tehing. Nagu nimigi ütleb, hõlmab see kokkulepet mitme kasutaja vahel, igaüks neist sisestab tehingusse summa bitcoine sisendina ja saab summa väljundina.

Nagu varem mainitud, on koostööd tehingu kõige tuntum struktuur Coinjoin. Näiteks Coinjoin Whirlpool protokollil hõlmavad tehingud 5 osalejat sisendite ja väljunditena, igaühega sama bitcoini summa.

![Diagramm Coinjoin tehingust Whirlpool'is](assets/1.webp)

Välisvaatleja ei suuda sellest tehingust teada, milline väljund kuulub millisele kasutajale sisendina. Kui võtame näiteks kasutaja #4 (lilla), saame ära tunda nende sisendi UTXO, kuid me ei tea, milline viiest väljundist tegelikult nende oma on. Algset teavet ei varjata, vaid pigem segatakse grupi sees.
Kasutaja on võimeline eitama teatud UTXO omamist väljundina. Seda nähtust nimetatakse "usutavaks eitamiseks" ja see võimaldab konfidentsiaalsust läbipaistvas Bitcoin'i tehingus.

Coinjoin'i kohta lisateabe saamiseks selgitan KÕIKE selles pikas artiklis: CoinJoin'i mõistmine ja kasutamine Bitcoin'is.
Kuigi Coinjoin on UTXO jälitamise katkestamisel väga tõhus, ei sobi see otseseks kulutamiseks. Tõepoolest, selle struktuur nõuab eelnevalt määratud summa sisendite ja sama väärtusega väljundite (miinus kaevandamistasud) kasutamist. Siiski on Bitcoinil kulutamistehing kriitiline hetk privaatsuse jaoks, kuna see loob sageli füüsilise seose kasutaja ja nende ahelasisese tegevuse vahel. Seetõttu tundub privaatsusvahendite kasutamine kulutamiseks hädavajalik. On olemas ka teisi koostööpõhiseid tehingustruktuure, mis on spetsiaalselt ette nähtud tegelike maksetehingute jaoks.
## StonewallX2 tehing

Samourai Walletis pakutavate kulutamisvahendite hulgas on koostööpõhine tehing StonewallX2. See on mini Coinjoin kahe kasutaja vahel, mis on mõeldud makseks. Väljastpoolt vaadates võib see tehing pakkuda mitmeid võimalikke tõlgendusi. Seega pakub see kasutajale usutavat eitamisvõimalust ja seeläbi konfidentsiaalsust.

See StonewallX2 koostööpõhise tehingu seadistus on saadaval Samourai Walletis ja Sparrow Walletis. See tööriist on kahe tarkvara vahel interoperatiivne.

Selle mehhanism on üsna lihtne mõista. Siin on, kuidas see praktikas toimib:

> - Kasutaja soovib teha makse bitcoiinides (näiteks kaupmehele).
> - Nad taastavad tegeliku maksesaaja (kaupmehe) vastuvõtu aadressi.
> - Nad koostavad spetsiifilise tehingu mitme sisendiga: vähemalt üks kuulub neile ja üks välisele koostööpartnerile.
> - Tehingul on 4 väljundit, sealhulgas 2 sama summa eest: üks kaupmehe aadressile makseks, üks muutusena, mis naaseb kasutajale, üks sama väärtusega väljund, mis läheb koostööpartnerile, ja teine väljund, mis samuti naaseb koostööpartnerile.

Näiteks siin on tüüpiline StonewallX2 tehing, milles ma tegin makse 50,125 satsi eest. Esimene sisend 102,588 satsi tuleb minu Samourai rahakotist. Teine sisend 104,255 satsi tuleb minu koostööpartneri rahakotist:

![StonewallX2 tehingu diagramm](assets/2.webp)

Me võime täheldada 4 väljundit, sealhulgas 2 sama summa eest, et segada jälgi:

> - 50,125 satsi, mis lähevad minu makse tegelikule saajale.
> - 52,306 satsi, mis esindavad minu muutust ja seega naasevad aadressile minu rahakotis.
> - 50,125 satsi, mis naasevad minu koostööpartnerile.
> - 53,973 satsi, mis naasevad minu koostööpartnerile.
>   Tehingu lõppedes taastatakse koostööpartneri algne saldo (miinus kaevandamistasud) ja kasutaja on kaupmehele maksnud. See lisab tehingule olulise hulga entroopiat ja katkestab vaieldamatud seosed makse saatja ja saaja vahel.

StonewallX2 tehingu tugevus seisneb selles, et see täielikult tõrjub ühe empiirilise reegli, mida ahelanalüütikud kasutavad: sisendite ühine omandiõigus mitme sisendiga tehingus. Teisisõnu, enamikul juhtudel, kui me täheldame Bitcoin tehingut mitme sisendiga, võime eeldada, et kõik need sisendid kuuluvad samale isikule. Satoshi Nakamoto oli juba oma Valges Raamatus tuvastanud selle probleemi kasutaja privaatsuse jaoks:

> "Lisakaitsemeetmena võiks iga tehingu jaoks kasutada uut võtmepaari, et hoida neid seostumast ühise omanikuga. Siiski on seos vältimatu mitme sisendiga tehingute puhul, mis paratamatult paljastavad, et nende sisendid kuulusid samale omanikule."

See on üks paljudest empiirilistest reeglitest, mida ahelanalüüsis kasutatakse aadressiklasterite koostamiseks. Selle heuristika kohta lisateabe saamiseks soovitan lugeda Samourai neljaosalist artiklite sarja, mis tutvustab teemat suurepäraselt.
StonewallX2 tehingu tugevus seisneb selles, et välisvaatleja arvab, et tehingu erinevad sisendid kuuluvad ühele omanikule. Tegelikkuses on need kaks erinevat kasutajat, kes teevad koostööd. Makse analüüs viib seega eksiteele ja kasutaja privaatsus on kaitstud.
Väliselt ei saa StonewallX2 tehingut eristada Stonewall tehingust. Ainus oluline erinevus nende vahel on see, et Stonewall ei ole koostööpõhine. See kasutab ainult ühe kasutaja UTXO-sid. Siiski, nende struktuurid kontoraamatus on Stonewall ja StonewallX2 täiesti identsed. See võimaldab veelgi rohkem tõlgendusi selle tehingu struktuuri kohta, kuna välisvaatleja ei suuda öelda, kas sisendid pärinevad samalt isikult või kahest koostööd tegevast isikust.

Lisaks on StonewallX2 eelis Stowaway-tüüpi PayJoini ees see, et seda saab kasutada igas olukorras. Tegelik makse saaja ei anna tehingule sisendeid. Seega saab StonewallX2 kasutada maksmiseks ükskõik millisele kaupmehele, kes aktsepteerib Bitcoini, isegi kui kaupmees ei kasuta Samourai või Sparrow'd.
Teisest küljest on selle tehingu struktuuri peamine puudus see, et see nõuab koostööpartnerit, kes on nõus kasutama oma bitcoine sinu makse tegemiseks. Kui sul on bitcoinist sõpru, kes on valmis sind igas olukorras aitama, siis see ei ole probleem. Kuid, kui sa ei tunne ühtegi teist Samourai Walleti kasutajat või kui keegi ei ole saadaval koostööks, siis oled ummikus.

Selle probleemi lahendamiseks lisas Samourai meeskond hiljuti oma rakendusele uue funktsiooni: JoinBot.

# Mis on JoinBot?

JoinBoti põhimõte on lihtne. Kui sa ei leia kedagi, kellega teha koostööd StonewallX2 tehingu jaoks, saad teha koostööd JoinBotiga. Praktikas teed sa tegelikult koostööd otse Samourai Walletiga.

See teenus on väga mugav, eriti algajatele kasutajatele, kuna see on saadaval 24/7. Kui sa pead tegema kiire makse ja soovid teha StonewallX2, ei pea sa enam võtma ühendust sõbraga või otsima veebist koostööpartnerit. JoinBot aitab sind.

Teine JoinBoti eelis on see, et see pakub sisendina ainult postmix Whirlpooli UTXO-sid, mis parandab sinu makse privaatsust. Lisaks, kuna JoinBot on alati võrgus, peaksid sa tegema koostööd UTXO-dega, millel on suured potentsiaalsed Anonsetid.

Ilmselgelt on JoinBotil mõned kompromissid, mida tuleks märkida:

> Nagu klassikalise StonewallX2 puhul, on sinu koostööpartner tingimata teadlik kasutatud UTXO-dest ja nende sihtkohast. JoinBoti puhul teab Samourai selle tehingu detaile. See ei pruugi tingimata olla halb asi, kuid seda tuleks meeles pidada.
> Rämpsposti vältimiseks nõuab Samourai 3,5% teenustasu tegeliku tehingu summast, maksimaalse piiriga 0,01 BTC. Näiteks, kui ma saadan tegeliku makse 100 kilosatsiga JoinBoti kaudu, on teenustasu summa 3 500 satsi.
> JoinBoti kasutamiseks peab sinu rahakotis olema vähemalt kaks omavahel mitteseotud ja saadaolevat UTXO-d.
> Klassikalise StonewallX2 puhul jagatakse kaevandustasud võrdselt kahe koostööpartneri vahel. JoinBotiga pead ilmselgelt maksma kogu kaevandustasu ise.
Selleks, et JoinBot tehing oleks täpselt sama nagu klassikaline StonewallX2 või Stonewall tehing, tehakse teenustasude maksmine täiesti eraldi tehinguna. Samourai poolt algselt makstud kaevandamistasude poole tagastamine toimub selle teise tehingu käigus. Et oma privaatsust lõpuni optimeerida, tehakse tasude arveldamine Stowaway (PayJoin) struktureeritud tehingu abil.

## Kuidas kasutada JoinBoti?

JoinBot tehingu sooritamiseks peab teil olema Samourai Wallet. Saate selle alla laadida siit või Google Playstore'ist.

Erinevalt enamikust Samourai poolt välja töötatud tööriistadest ei ole Sparrow Wallet veel JoinBoti rakendamist teatanud. Seega on see tööriist saadaval ainult Samourais.

Avastage samm-sammult, kuidas sooritada StonewallX2 tehingut JoinBotiga selles videos:

![Kuidas kasutada Joinboti](https://youtu.be/80MoMz2Ne5g)

Siin on tehingu diagramm, mille me just videos sooritasime:

![Minu StonewallX2 tehingu diagramm JoinBotiga.](assets/3.webp)

Me näeme 5 sisendit:

> - 3 sisendit 100 kilosatsi ulatuses Samouraist (JoinBot).
> - 2 sisendit minu isiklikust rahakotist, 3,524 satsi ja 1.8 megasati ulatuses.

Tehingu 4 väljundit on järgmised:

> - 1 väljund 212,452 satsi ulatuses tegelikule makse saajale.
> - Teine sama suur summa, mis läheb tagasi Samourai aadressile.
> - 1 vahetus, mis läheb samuti tagasi Samouraile 87,302 satsi ulatuses. See esindab nende sisendite kogusumma (300,000 satsi) ja segadust tekitava väljundi (212,452 satsi) vahe, miinus kaevandamistasud.
> - 1 vahetus, mis läheb tagasi teisele aadressile minu rahakotis. See esindab minu sisendite kogusumma ja tegeliku makse vahe, miinus kaevandamistasud.

Meenutuseks, kaevandamistasud ei esinda tehingu väljundeid. Need lihtsalt esindavad sisendite kogusumma ja väljundite kogusumma vahet.

## Järeldus

JoinBot on täiendav tööriist, mis lisab Samourai kasutajatele rohkem valikuid ja vabadust. See võimaldab teha koostööd StonewallX2 tehingu otse Samouraiga kui kaastöötajaga. Selline tehing aitab parandada kasutaja privaatsust.

Kui saate sooritada klassikalise StonewallX2 tehingu sõbraga, soovitan siiski seda tööriista kasutada. Kuid kui olete ummikus ja ei leia makse tegemiseks ühtegi kaastöötajat, teadke, et JoinBot on teiega koostööd tegemas 24/7.

**Välised ressursid:**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin