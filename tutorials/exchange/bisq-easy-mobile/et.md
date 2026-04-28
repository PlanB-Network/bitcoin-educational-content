---
name: Bisq Easy Mobile
description: Peer-to-peer kauplemisprotokoll uutele bitcoini kasutajatele - ei mingeid vahendajaid, ei mingit KYC-i.
---
![cover](assets/cover.webp)


## Sissejuhatus


[Bisq Easy](https://bisq.network/bisq-easy/) kauplemisprotokoll on mõeldud [Bisq 2](https://github.com/bisq-network/bisq2) jaoks, mis on [Bisq v1](https://github.com/bisq-network/bisq) järeltulija. Bisq 2 toetab mitmeid kaubandusprotokolle, privaatsusvõrke ja identiteete. See hõlbustab Bitcoin ostmist null kaubandustasuga ja ilma tagatisraha nõudeta. See on mõeldud uutele Bitcoin ostjatele, kes otsivad võimalust, mis ei ole seotud isikukoodiga, kuid keda soovivad tõhusalt sisse viia kogenud ja asjatundlikud müüjad, kes on tuttavad Bisq platvormiga.


Praegu on Bisq Easy ainus Bisq 2 kaubandusprotokoll. Tulevikus on kavas rohkem kaubandusprotokolle. Lisateavet Bisq 2 kohta leiate sellest juhendmaterjalist:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

See lühijuhend on täienduseks eespool toodud õpetusele Bitcoin ostmise kohta rakenduse [Bisq Easy Mobile] (https://github.com/bisq-network/bisq-mobile) ja Lightning abil.


## 1️⃣ Alustamine


Alustamiseks laadige Bisq Easy Mobile alla [allalaadimisleheküljelt](https://bisq.network/downloads/). Soovitatav on kontrollida allalaadimist. Kontrollimisjuhised on saadaval ka [allalaadimislehel](https://bisq.network/downloads/). Pärast installimist peate nõustuma `Kasutamislepinguga`. Seejärel looge avalik profiil, mis koosneb `nimest` ja avatarist (mida esindab `roboti ikoon`). Bisq Easy abil saate luua ka mitu kasutaja profiili ühes kliendis. Pärast lühikest initsialiseerimist jõuate `Kodukuvale`. Rakendus toob välja õppematerjali otse pealehel. Puudutage valikut `Open Trade Guide`, et tutvuda värskeima teabega.


![image](assets/en/01.webp)


Kaubanduse juhend selgitab kõike asjakohast lihtsate sammudega:



- Kuidas kaubelda Bisq Easy'ga
- Kuidas kauplemisprotsess toimib
- Mida ma pean teadma kaubanduseeskirjade kohta.


Teine oluline osa on **"Kui turvaline on Bisq Easy'ga kauplemine? "**


![image](assets/en/08.webp)


Märkige märkeruut "Olen lugenud ja aru saanud" ja koputage nuppu "Lõpeta".


![image](assets/en/02.webp)


## 2️⃣ Andmete varundamine


Enne kui alustame, teeme mõned majapidamisülesanded ja loome oma andmesalvestusfaili "varukoopia". Mine `More` > `Backup & Restore`, et salvestada oma profiili ja kauplemisajalugu. Kui kaotate oma seadme ilma varukoopiana, ei ole teie maine ja käimasolevad tehingud taastatavad. Andke `Password`, et krüpteerida oma varukoopia.


![image](assets/en/11.webp)


## 3️⃣ Pakkumised


Avakuvalt "Avakuva" on kaks võimalust pakkumistele navigeerimiseks. Puudutage ekraani keskel valikut "Tutvu pakkumistega" või koputage alumise menüüst valikut "Pakkumised". Valige sealt valuuta, millega soovite kaubelda.


![image](assets/en/03.webp)


Erinevalt [Bisq 1] (https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), mis nõuab tagatist, tugineb Bisq Easy tagatiseks üksnes müüja mainele. Kuigi selline lähenemisviis võimaldab ostjatel esimest korda osta Bitcoin ilma eelneva omandiõiguseta, on see suur usaldus müüja suutlikkuse suhtes tarnida Bitcoin pärast fiat-maksete saamist. Seetõttu on Bisq Easy turvamudel optimeeritud ainult väikeste kauplemissummade jaoks ning riskide minimeerimiseks on tehingud piiratud 600 USA dollari ekvivalendiga tehingu kohta. Valige jaotises `Offerbook` filtrid makseviiside ja arvelduste jaoks Lightning või Bitcoin (on-chain).


![image](assets/en/04.webp)


Pärast "filtrite" rakendamist valige sobiv pakkumine usaldusväärselt kaubanduspartnerilt. Kuvatakse müüja eelnevalt valitud makseviis ja arveldusviis (`Lightning` või `on-chain`). Enne jätkamist veenduge, et need vastavad teie eelistustele. Valime siinkohal Lightning ⚡ võimaluse.


![image](assets/en/05.webp)


Vaadake kaubanduse üksikasjad läbi ja kinnitage need, vajutades nuppu `Kinnitage pakkumise vastuvõtmine`. Seejärel ilmub hüpikaken, mis kinnitab, et olete pakkumise edukalt vastu võtnud. Koputage valikut Näita kauplemist jaotises "Avatud tehingud". Liigutage jaotises Open Trades oma `Lightning invoice` ja puudutage selle jagamiseks valikut `Sendage müüjale`. Oodake nüüd müüja maksekonto andmeid. Müüjatel võib vastamine aega võtta. Vaadake perioodiliselt tagasi, et saada uuendusi vestlusaknas.


![image](assets/en/06.webp)


Saatke lühike tervitus vestluses. Müüja jagab makse üksikasjad, kui nad tulevad online


![image](assets/en/09.webp)


Kui olete saanud müüjalt vajalikud makseandmed, jätkake makse sooritamist. Seejärel vajutage nuppu `Kinnitage, et olete makse sooritanud`, seejärel oodake kannatlikult kättesaamise kinnitust. ️ ⌛️


Lõpuks, kui müüja kinnitab makse laekumist, peate ka teie kinnitama Bitcoin kättesaamist. Sellega on ostu sooritatud, kasutades Bisq lihtsas režiimis. Palju õnne! Nüüd võite vajutada nuppu `kaubanduse sulgemine`.


![image](assets/en/10.webp)


## 4️⃣ Vaidluste lahendamine Bisq Easy


Kui teie kauplemisega läheb midagi valesti, võivad nii ostjad kui ka müüjad taotleda vahendamistoetust.


**Mida vahendajad saavad teha:**

- Aidata hõlbustada edukat kaubavahetuse lõpuleviimist

- Fiat-, altcoin- ja Bitcoin-maksete kontrollimine

- Vajaduse korral tehingu tühistamine

- Teatada moderaatoritele tõsistest reeglite rikkumistest võimalike kasutamiskeeldude saamiseks


**Konsequentsid petturlike müüjate puhul:**

Sõltuvalt nende maine tüübist:



- BSQ võlakirja maine**: DAO võib konfiskeerida nende võlakirjaga BSQ'd
- Sibula Address maine**: Nende Bisq 1 sibula aadress võib olla keelatud


**Tähtis märkus:** Kuna kogu maine on seotud teie kasutajaprofiiliga, keelab keeld teie maine täielikult.


## 5️⃣ Loo oma pakkumine


Olemasolevate pakkumiste vastuvõtmise asemel saate luua oma ostupakkumise ja lasta müüjatel tulla teie juurde. See on õige valik, kui te ei leia turul, kus soovite kaubelda, ühtegi sobiva preemia või makseviisiga pakkumist, kuigi peate ootama, kuni müüja selle vastu võtab.


Pakkumiste ekraanil puudutage rohelist ikooni "+" paremas alumises nurgas. Seejärel valige "Osta Bitcoin" ja valige oma fiat-valuuta.


Määrake oma kaubandusparameetrid:



- Fikseeritud summa või vahemik**: Valige, kui palju soovite kulutada.
- Makseviis**: Valige olemasolevatest võimalustest
- Arveldus**: Vali välk ⚡ või ₿ on-chain


Vaadake oma andmed üle ja puudutage valikut "Loo pakkumine". Teie pakkumine ilmub nüüd "Pakkumiste raamatusse".


![image](assets/en/07.webp)


*Märkus: Bisq Easy ostjana ei ole teil vaja mainet - see on peamine eelis. Müüjad kannavad mainenõuet ja riski, mistõttu nad küsivad lisatasu. Teie pakkumine peab lihtsalt olema piisavalt atraktiivse hinnaga, et mainekad müüjad seda kaaluksid.*


Kui see on avaldatud, oodake jaotises "Pakkumisraamat". Kui müüja võtab teie pakkumise vastu, saate teate. Avage kauplemine jaotises `Open Trades`, kus müüja ja teie saate vahetada oma makseandmeid. Saatke müüjale oma Bitcoin aadress või Lightning arve. Pärast fiat'i saatmist kinnitage makse. Kui müüja kinnitab kättesaamist, vabastab ta Bitcoin, et kauplemine lõpule viia.


## 🎯 Kokkuvõte


Bisq Easy võimaldab Bitcoin ostu ilma tagatiseta, lahendades klassikalise kana-muna probleemi uute ostjate jaoks. Kompromiss on selge: te toetute müüja mainele, mitte lukustatud rahalistele vahenditele. Selline usaldusel põhinev lähenemisviis selgitab tüüpilist 5-15% preemiat, millega hüvitatakse mainekatele müüjatele nende investeeringud usalduse loomisesse ja toetuse pakkumisse. Kuigi süsteem piirab võimalike kahjude piiramiseks tehinguid väikeste summadega, jääge alati kindla mainehinnanguga müüjate juurde. Uustulnukatele, kes on valmis neid tingimusi aktsepteerima, pakub Bisq Easy lihtsat sisenemisvõimalust Bitcoin-sse.


## 📚 Bisq Lihtne mobiilne ressurss 📚 Bisq Lihtne mobiilne ressurss


[Github](https://github.com/bisq-network/bisq-mobile) | [Veebileht ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)