---
name: Cashu.me
description: Cashu.me juhend ecash'i kasutamiseks
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Siin on BTC Sessionsi videojuhend, mis näitab, kuidas seadistada ja kasutada Cashu.me Bitcoin Wallet, mis annab teile juurdepääsu lihtsatele, odavatele ja privaatsetele Bitcoin tehingutele - ilma rakenduspoe vajaduseta!*


Selles õpetuses uurime Cashu.me'i, brauseripõhist Wallet privaatseid Bitcoin makseid, mis kasutavad Chaumian ecash'i. Enne kui me sukeldume, tutvustame lühidalt ecash'i ja selle toimimist.


## Sissejuhatus e-kassasse


Kujutage ette, et teil on digitaalne raha, mis toimib täpselt nagu füüsilised arved taskus - see on privaatne, kohene ja kasutatav ilma vahendajateta. Just seda võimaldab ecash: digitaalne makseviis, mis toob füüsilise sularaha privaatsuse tagasi digitaalsesse maailma. Erinevalt onchain-Bitcoin-st, mis salvestab iga tehingu avalikus Ledger-s, mis on kõigile nähtav, loob ecash privaatseid märke, mis esindavad tegelikku Bitcoin väärtust, hoides samal ajal teie kulutamisharjumused konfidentsiaalsetena.


Mõelge e-raha kui teie seadmesse salvestatud digitaalseid instrumendid - kui need on teie käes, siis on need teie omandis, nagu füüsiline sularaha. Neid märke annavad välja usaldusväärsed teenused, mida nimetatakse "Müntideks" ja mis hoiavad nende aluseks olevaid Bitcoin varusid. Kui kasutate e-kassat, ei edasta te oma tehinguid kogu võrku. Selle asemel vahetate privaatseid märke otse teistega, luues maksekogemuse, mis tundub rohkem nagu kellelegi sularaha üleandmine kui traditsiooniline digitaalne makse.


Cashu on vaba ja avatud lähtekoodiga Chaumian ecash protokoll, mis on loodud Bitcoin jaoks. Tehnoloogia põhineb David Chaumi 1980ndatel aastatel tehtud teedrajavatel krüptograafilistel uuringutel, mis kasutavad privaatsuse tagamiseks "pimedaid allkirju". Kui saate ecash-märke, allkirjastab rahapaja need, ilma et teaksite, kus neid järgmisena kulutatakse - see on oluline omadus, mis takistab tehingute jälgimist. Oluline on, et ecash ei asenda Bitcoin, vaid täiendab seda, lahendades mõned kriitilised probleemid, mis tulenevad Bitcoin arhitektuurinõuetest. See pakub füüsilise sularaha pakutavat privaatsust (mis puudub Bitcoin läbipaistval Ledger-l) ja võimaldab koheseid mikrotehinguid ilma Blockchain tasude või kinnituse hilinemiseta.


Ecash integreerub sujuvalt Lightning Network-ga. Kasutate Lightningit Bitcoin sissemakse tegemiseks rahapajasse (konverteerides Bitcoin väärtuse Ecash-märkideks) ja hilisemaks väljavõtmiseks (konverteerides märgid tagasi kulutatavaks Lightningi saldoks). Koos moodustavad nad võimsa kombinatsiooni: Bitcoin pakub turvalist arveldust Layer, Lightning võimaldab kiireid tehinguid ja võrgu koostalitlusvõimet ning ecash lisab privaatsuse Layer, mis muudab digitaalsed maksed taas tõeliselt privaatseks.


## Cashu.me


Cashu.me on "progressiivne veebirakendus (PWA)", mis rakendab Cashu protokolli - spetsiaalne Chaumian ecashi rakendamine, mis on mõeldud Bitcoin jaoks. PWA-na töötab see otse teie brauseris, ilma et see nõuaks paigaldamist rakenduspoodidest, kuigi lihtsama juurdepääsu tagamiseks saate selle `installida` oma seadmesse. Selline veebipõhine lähenemine tagab laialdase ühilduvuse kõigis operatsioonisüsteemides, säilitades samal ajal turvalisuse pigem krüptograafiliste protokollide kui platvormipiirangute kaudu.


## 🎉 Peamised omadused


Sukeldume funktsioonidesse ja uurime, mida Cashu.me pakub:



- Chaumian ecash on Lightning**: Kasutab pimesi allkirju, nii et rahapajad ei saa jälgida kasutajate saldosid või tehinguajalugu
- Märgiste omavahetus**: Te kontrollibite ecash-märke lokaalselt oma seed fraasiga
- seed fraasi varundused**: 12-sõnaline taastamise fraas Wallet taastamiseks
- Rahapaja sõltumatus**: Töötab mitme sõltumatu rahapoega - te ei ole lukustatud ühe teenusepakkuja külge
- Kohesed, tasuta tehingud**: Sama rahapaja raames toimuvad maksed sekunditega ja ilma tasudeta
- Privaatsust säilitav arhitektuur**: Rahapajad ei näe, kes kellega tehinguid teeb
- Offline-ekraam**: Märgiste saatmine/vastuvõtmine kohaliku ülekandeprotokolli, näiteks NFC, QR-koodi, Bluetoothi jne kaudu ilma internetiühenduseta
- Avastage Nostr** kaudu ecash-mündid: Leidke ja kontrollige usaldusväärseid rahapaigutusi Nostr-protokolli kaudu
- Vahetage e-raha mündi** vahel: See tähendab, et saate nende vahel väärtust üle kanda.
- Kaugjuhtige oma Wallet seadet Nostr Wallet Connect (NWC)** abil: Ühendage teiste rakendustega, nagu Nostr Client, ja alustage NWC kaudu zappimist


Kriitiline kompromiss on "usaldus": kuigi te kontrollite žetoonide endi üle, peate usaldama rahapajaid, et nad hoiavad nende aluseks olevaid Bitcoin varusid. Nagu Cashu dokumentatsioonis öeldakse:


> ...Rahapaja haldab Lightning-infrastruktuuri ja hoiab satoshisid rahapaja ecash-kasutajate jaoks. Kasutajad peavad usaldama rahapaja Redeem nende e-raha, kui nad soovivad Lightningile üle minna.

- Cashu dokumentatsioon, [üldised ohutus- ja privaatsusküsimused](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


See muudab ecash'i Bitcoin enda eestkostja lahenduseks, kuigi teil säilib täielik kontroll žetoonide üle.


## 1️⃣ Esialgne seadistamine


① Alustage oma brauseris külastades [Wallet.cashu.me](https://Wallet.cashu.me). Kuna Cashu.me on `PWA`, ei pea te seda rakenduspoodidest alla laadima, vaid avage sait lihtsalt otse oma brauseris. Lihtsamaks juurdepääsuks saate selle valikuliselt paigaldada oma seadme avakuvale.


② PWA installimiseks puudutage brauseris menüü nuppu ⋮ ja valige "Lisa avakuvale". Pärast paigaldamist sulgege brauseri vahekaart ja käivitage Cashu.me oma seadme avakuval. Tervitusekraanil koputage jätkamiseks valikut `Next`.


③ Turvalisus on kriitilise tähtsusega. Hoidke oma seed fraasi turvaliselt paroolihalduris või veel parem, kirjutage see paberile. See 12-sõnaline taastamisfraas on teie ainus võimalus raha tagasi saada, kui kaotate juurdepääsu sellele seadmele. Puudutage ikooni 👁️, et avada oma seed fraas, kirjutage hoolikalt üles kõik 12 sõna järjekorras ja seejärel märkige ruut "Olen selle üles kirjutanud". Jätkamiseks puudutage valikut `Järgmine` ja märkige järgmisel ekraanil ruut, et kinnitada, et nõustute `tingimustega`.


![image](assets/en/01.webp)


Pärast seadistamise lõpetamist peate ühendama `Mint`iga. Nostr-kogukonna poolt soovitatud müntide vaatamiseks puudutage valikut `ADD MINT`, millele järgneb `DISCOVER MINTS`. Täiendavaks kontrollimiseks saate vaadata mündi hinnanguid aadressil [bitcoinmints.com](bitcoinmints.com).


Järgmisena koputage nuppu "Kliki miinimummüntide sirvimiseks", et näha täielikku nimekirja. Valige mündi, kopeerides selle URL, sisestades selle URL-väljale ja andes sellele äratuntava nime. Selle näite puhul kasutame:


URL: `https://mint.minibits.cash/Bitcoin`

Nimi: minibits


![image](assets/en/02.webp)


Protsessi lõpetamiseks puudutage valikut `ADD MINT`. Kinnitusekraanil veenduge, et usaldate selle mündi operaatorit, seejärel koputage uuesti valikut `ADD MINT`. Minibits piparmünt ilmub nüüd teie Avakuvale. Kui teie Wallet on seadistatud, peate seda enne tehingute tegemist rahastama.


![image](assets/en/03.webp)


## 2️⃣ Teie Wallet rahastamine


Cashu.me pakub oma Wallet rahastamiseks kaks erinevat meetodit. Kui koputate Avakuval nuppu `Võta`, näete võimalusi raha saamiseks kas `RAHA` või `VALGUSTUS` kaudu.


![image](assets/en/04.webp)


### Rahastamine LIGHTNINGi kaudu


Esimene võimalus on rahastada Wallet Lightning Invoice kaudu. "Valige rahapaja", kui olete lisanud erinevaid rahapajaid, ja määrake "summa (Sats)", mida soovite saada. Seejärel koputage `LOODA Invoice.` Nüüd kuvatakse QR-kood, mida saate skaneerida teise välk Wallet või saate lihtsalt `Kopeerida` Invoice ja kleepida teise Wallet, et maksta ja rahastada oma cashu.me Wallet.


![image](assets/en/05.webp)


### E-raha saamine


Ecash-meetod võimaldab teil saada žetoone otse teiselt ecash Wallet-lt. Alustage, vajutades nuppu `Vaata` ja valides valiku `ECASH`. Te saate `Paste` või `Scan` või kasutada `NFC`, et esitada Cashu token teiselt Wallet-lt. Kui valite kleepimise, sisestage teisest Wallet-st kopeeritud token string, `Amount` ja `Mint` kuvatakse automaatselt. Tehingu lõpetamiseks puudutage valikut `RECEIVE` ja Sats ilmub teie Wallet-sse. Pange tähele, et teie saldo on nüüd jaotatud mitme mündi vahel. Näiteks võib teil olla 1000 Sats oma Minibits-mündis ja veel 1000 Sats Coinos-mündis. Selline eraldamine erinevate mündiühikute vahel on Cashu arhitektuuri oluline aspekt.


![image](assets/en/06.webp)


### Vahetus mündi vahel


Kui te ei usalda enam mõnda lisatavat rahapaja, pakub cashu.me võimalust "vahetada" raha ühelt rahapajailt teisele. Liikuge vahekaardile "Mints" ja kerige allapoole, kuni näete "Multimintide vahetamine" (Multimint Swaps). Valige rippmenüüdest rahapaja `FROM` ja `TO` ning sisestage summa, mida soovite üle kanda. Puudutage valikut `SWAP`, et žetoonid mündi vahel liigutada. See toimub Lightning-tehingu kaudu, seega peate jätma ruumi võimalike Lightning-tasude jaoks. Minu näites piisas 1 sat.


![image](assets/en/07.webp)


## 3️⃣ Raha saatmine


Sats saatmiseks pakub Cashu.me kahte võimalust. Saata kas "sularaha" või "välklambi" kaudu. Vaatame mõlemat võimalust.


### Saatmine välklambi kaudu


Lightning'i kaudu saatmiseks järgige järgmisi samme:


1. Puudutage avakuval valikut `SEND` ja valige `Valgustus`

2. Rakendus palub teil sisestada "Lightning Invoice" või "Address". Te võite sisestada Invoice/Address otse või kasutada selle visuaalseks jäädvustamiseks QR-koodi skaneerimise võimalust, seejärel kinnitage `ENTER`

3. Valige rippmenüüst rahapaja, millest soovite maksta, ja koputage kinnitamiseks valikut "MAKSE". **Märkus**: seadete -> "Eksperimentaalne" all on ka võimalus kasutada "Multinut", mis võimaldab teil maksta korraga mitme mündi arveid.

4. Pärast edukat lõpetamist näete makse kinnitust ja teie saldost mahaarvatud summat.


![image](assets/en/08.webp)


### Saatmine ecash'i kaudu


E-raha saatmine on sarnaselt lihtne.


1. Koputage nuppu "SEND" ja valige seekord valik "ECASH".

2. "Valige mündi" ja sisestage "summa", mille soovite saata Sats-s ja koputage kinnitamiseks "SENDA"

3. See loob "animeeritud QR-koodi", mida saate kohandada, reguleerides kiiruse ja suuruse parameetreid. Igaüks saab seda QR-koodi skaneerida, et Redeem kohe Sats või te võite puudutada COPY, et saata token string kellelegi teisele alternatiivsete kanalite kaudu, nagu Bluetooth, NFC või tavaline sõnumite saatmine.

4. Ma avan teise Wallet. Sisestage lõikelauast ja valige teises Wallet-s `Receive ecash`.


![image](assets/en/09.webp)


## 4️⃣ Lisafunktsioonid


Lisaks põhilistele saatmis- ja vastuvõtufunktsioonidele pakub Cashu.me võimsaid lisafunktsioone, mis suurendavad teie Bitcoin kogemust Nostr ökosüsteemis.


### Nostr Wallet Connect


Nostr Wallet Connect (`NWC`) muudab teie suhtlemist Nostr rakendustega, luues sujuva ühenduse teie Wallet ja sotsiaalsete rakenduste vahel. See protokoll võimaldab sellistel rakendustel nagu [Damus](https://damus.io/) või [Primal](https://primal.net/home) taotleda makseid otse Nostr-relade kaudu, ilma et peaksite rakendusest lahkuma.


NWC seadistamine Cashu.me's:


1. Minge vasakpoolses ülemises menüüs "Seadistused"

2. Kerige jaotisele "NOSTR Wallet CONNECT" ja koputage nuppu "Enable"

3. Seejärel määrate toetuse, et määrata kindlaks maksimaalne summa, mida taotlused võivad kulutada oma Wallet-st.

4. Pärast seadistamist saate kopeerida ühendusstringi ja kleepida selle mis tahes Nostr-kliendisse, mis toetab `NWC`, võimaldades kohese zapping- ja tipping-funktsionaalsuse.


![image](assets/en/10.webp)


### Lightning Address kaudu npub.cash


Cashu.me integreerub [npub.cash](https://npub.cash/), et pakkuda teile Lightning Address, mis töötab sujuvalt koos Nostr-protokolliga. Siin saate registreeruda ja nõuda oma kasutajanime, esitades oma Nostr `nsec`, mis maksab 5000 Sats ja toetab npub.cash projekti, või võite kasutada mis tahes Nostr-i avalikku võtit (`npub`) ilma registreerimiseta.


Kõigepealt minge menüüsse "Seaded" ja koputage npub.cashiga "Lightning Address lubamine". See loob generate npub.cash Address kasutades vaikimisi teie Wallet seed fraasist tuletatud `npub` stringi.


Teise võimalusena külastage [seda veebilehte](https://npub.cash/username), et taotleda kohandatud kasutajanimi, kasutades oma Nostr `nsec`, mis annab teile isikupärastatud Lightning Address nagu username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Kokkuvõte


Cashu.me pakub privaatseid Bitcoin makseid, mis toimivad nagu füüsiline sularaha - koheselt ja peer-to-peer, ilma et teie tehingute ajalugu avalikustataks. Mina isiklikult hindan selle PWA-arhitektuuri, sest see toimib ilma rakenduste poe piiranguteta. Kombineerides Bitcoin turvalisust, Lightningi kiirust ja ecash'i privaatsust, pakub Wallet kasutusviise, mis võivad suurendada Bitcoin igapäevast kasutuselevõttu.


Kuigi teil on täielik kontroll oma e-kassatähiste üle, kuna te ise hoiustate neid, pidage meeles, et rahapajad tegutsevad usaldusväärsete kolmandate osapooltena, kes hoiavad Bitcoin varusid. Võimalus kasutada mitut rahapaja ja vahetada nende vahel pakub paindlikkust, säilitades samal ajal privaatsuse.


Tänu sellistele funktsioonidele nagu NWC ja npub.cash aadressid on Cashu.me atraktiivne Wallet variant sotsiaalsetele klientidele, kes hindavad privaatsust ja suveräänsust suuremate tehnoloogiliste piirangute asemel.


## 📚 Ressursid


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)