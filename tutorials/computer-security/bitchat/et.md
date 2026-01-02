---
name: Bitchat
description: Detsentraliseeritud, internetivaba sõnumite edastamine tasuta suhtlemiseks
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*BTC Sessionsi videoõpetus näitab teile, kuidas Bitchat!* seadistada ja kasutada


Bitchat sündis kiire prototüüpimise käigus, kus [@jack](https://primal.net/jack) arendas esialgse kontseptsiooni välja nädalavahetuse kodeerimissessiooni ajal. [@calle](https://primal.net/calle) liitus projektiga varsti pärast seda, et töötada koos välja Androidi rakendus. Jack juhib praegu iOS-versiooni arendamist, samas kui calle jälgib Androidi versiooni paljude teiste toetajate abiga.


## Sissejuhatus: Vestlus vabalt, ilma võrkudeta


Kujutage ette sõnumite saatmist, kui internet läheb katki, loodusõnnetuse ajal või kohtades, kus sidepidamine on piiratud. Bitchat teeb selle võimalikuks. See on detsentraliseeritud, võrdõigusvõrgupõhine sõnumirakendus, mis jätab keskserverid vahele, lastes seadmetel omavahel otse suhelda, täiesti offline, kasutades Bluetoothi ja võrgusilma võrku. Bitchat on loodud privaatsust ja vastupidavust silmas pidades ning sobib ideaalselt kasutamiseks piirkondades, kus traditsiooniline ühendus on ebausaldusväärne või kättesaamatu - näiteks katastroofistsenaariumide ajal, kaugetes kohtades või neile, kes soovivad vältida jälgimist. Bitchat kasutab krüptograafiat, et tagada, et iga sõnum on otsast lõpuni krüpteeritud, kontrollitud ja võltsimiskindel.


Selles õpetuses näitame, kuidas Bitchat töötab ja kuidas saate seda kasutada tõeliselt privaatseks, offline-kõlblikuks suhtluseks.


## 🚀 Peamised omadused


Bitchat võimaldab offline-sõnumite saatmist nende [funktsioonide] kaudu (https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Platvormiülene ühilduvus**: Täielik protokolli ühilduvus iOS-i ja Androidi vahel.
- Detsentraliseeritud võrk**: Automaatne vastastikune avastamine ja mitmevahetussõnumite edastamine Bluetooth Low Energy (BLE) kaudu
- End-to-End krüpteerimine**: X25519 võtmevahetus + AES-256-GCM privaatsõnumite jaoks
- Kanalipõhised vestlused**: Teemapõhine grupisõnumite saatmine valikulise parooliga
- Store & Forward**: Sõnumid salvestatakse vahemällu võrguühenduseta eakaaslaste jaoks ja edastatakse, kui nad uuesti ühendust võtavad
- Privaatsus kõigepealt**: Ei kontosid, ei telefoninumbreid, ei püsivaid identifikaatoreid
- IRC-stiilis käsud: Tuttav `/join, /msg, /who` stiilis kasutajaliides.
- Sõnumite säilitamine**: Vabatahtlik kogu kanalit hõlmav sõnumite salvestamine, mida kontrollivad kanali omanikud
- Hädaolukorra pühkimine**: Kolme koputusega logo, et kustutada kohe kõik andmed
- Kaasaegne Androidi kasutajaliides**: Jetpack Compose koos materjalidisainiga 3
- Tumedad/heledad teemad**: Terminali inspireeritud esteetika, mis vastab iOS versioonile
- Aku optimeerimine**: Kohanduv skaneerimine ja energiajuhtimine


## 1️⃣ Kuidas Bitchat töötab - lihtsalt


Bitchat võimaldab teil saata sõnumeid läheduses asuvatele telefonidele otse Bluetoothi kaudu (`BLE` nagu allpool), ilma interneti- või mobiilsidesignaalita. Kui alustate vestlust, teevad telefonid turvalise käepigistuse, et luua teie vestluse jaoks unikaalne ajutine krüpteerimisvõti. Iga sõnum on kaitstud otsast lõpuni krüpteerimisega ja iga sõnumi puhul kasutatakse uut võtit, et tagada varasemate sõnumite turvalisus isegi siis, kui teie telefon on hiljem ohustatud. Lõpuks jagab rakendus sõnumid väikesteks tükkideks ja segab need juhuslike fiktiivsete andmetega, et varjata teie sõnumitegevust. Otseste seadmetevaheliste vestluste puhul töötab see ainult kuni ~100 m raadiuses. See on nagu krüpteeritud märkmete edastamine rahvarohkes ruumis - seadmed sosistavad üksteisele otse, purustades võtmed pärast iga sõnumit.


Bitchat võimaldab teil liituda ka asukohapõhiste jututubadega, kasutades Nostr protokolli ja `#geohashes`. Geohash on lühike kood, näiteks `#u33d`, mis tähistab konkreetset geograafilist piirkonda, alates ühest naabruskonnast kuni terve linna või piirkonnani. Saate `teleportida` ükskõik millisesse geohashi jututuppa üle maailma, lihtsalt sisestades selle tagi. Teie sõnumid saadetakse läbi detsentraliseeritud releevõrgu, mis kaitseb teie täpset asukohta. Lisaks sellele antakse teile iga kord, kui liitute geohash-ruumiga, uus ajutine identiteet, mis lisab teie asukohapõhistele vestlustele täiendavat privaatsust.


Täpsemaid tehnilisi üksikasju leiate [ametlikust teabelehes] (https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Paigaldamine ja seadistamine


### Kust saada Bitchat


Saate paigaldada Bitchat läbi:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (iOS-seadmetele)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (Android-seadmetele)


Androidi kasutajatel on ka alternatiivseid võimalusi:



- Lae APK otse [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) lehelt või
- Paigaldage läbi Nostr-ga ühilduva [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Märkus**: see õpetus keskendub peamiselt Androidi rakendusele. IOS versioon võib erineda


### Seadistamisprotsess


Pärast paigaldamist avage Bitchat, et näha seda algset õiguste ekraani. Siin on, mida peate tegema:


1. **Vajalikud õigused:**


   - Bluetooth-ühendus** (Bitchat'i kasutajate avastamiseks läheduses)
   - Täpne asukoht** (Android nõuab seda Bluetooth-funktsiooniks)
   - Teated** (privaatsõnumite teavituste saamiseks)

2. **Aku optimeerimise väljalülitamine**:


   - See võimaldab Bitchat taustal käivitada
   - Säilitab pidevalt võrgusilmaühendusi


Puudutage valikut `Lubade andmine`, järgige `prompts` ja `Aku optimeerimise väljalülitamine`, et liikuda järgmisele ekraanile.


![image](assets/en/02.webp)


Tere tulemast Bitchati põhiekraanile. Hakkame orienteeruma:


### Seaded


Esimesed asjad kõigepealt. Seadete menüü saab avada koputades `Bitchat logo`.  Saadaval on järgmised valikud:



- Määrake "välimus" (süsteem/valgus/tume).
- lubage geohash'ile rämpsposti tõkestamiseks `Proof of work` (valikuline)
- Privaatsuse suurendamiseks lülitage sisse `Tor`.


![image](assets/en/16.webp)


### Määrake oma identiteet


Puudutage üleval olevat välja `bitchat/anonXXXXXX`, et valida oma kasutajanimi. Nii näevad teised teid nii Bluetooth- kui ka internetirežiimil. Näiteks võite muuta "anon2022" enda valitud kasutajanimeks.


![image](assets/en/03.webp)


### Valige võrgukanalid


Kasutage menüüd `#lokatsioonikanalid` (paremal pool kasutajanime), et vahetada ühendustüüpide vahel:



- BLE Mesh***: Bluetoothi vaikimisi režiim (ilma internetita, 10 kuni 50 meetri kaugus)
- #geohashes**: Interneti-võimelised geograafilised kogukonnad, mis kasutavad [Nostr protokolli](https://nostr.com/)


Kui valite režiimi `#geohashes`, integreerub Bitchat Nostr protokolliga, et võimaldada geograafilisi kogukondi. Teie sõnumid avaldatakse pigem `detsentraliseeritud Nostr releedele` kui Bitchati peer-to-peer võrgustikule, mis võimaldab laiemaid, kuid asukoha järgi filtreeritud vestlusi. Oluline on, et teie Bitchati identiteedivõtmed allkirjastavad autentimise säilitamiseks krüptograafiliselt kõik Nostr sündmused, samas kui geohash-märgised (nagu `#u4pruyd` naabruskonna jaoks) filtreerivad sõnumeid teie valitud täpsusastmele. See tähendab, et saate osaleda kohalikes aruteludes ilma täpseid koordinaate avaldamata, kuigi selleks on vaja internetiühendust.


![image](assets/en/04.webp)


### Jälgige eakaaslasi

litsents: CC-BY-SA-V4

Peer loendur näitab kasutajaid:



- Lähedal (BLE Mesh) või
- Teie geohash tsoonis (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Ülemaailmne vestlus ja privaatsõnumid


Bitchat pakub kahte erinevat suhtlusrežiimi, mis vastavad erinevatele vajadustele:



- Avalikud kanalid:** Avatud vestlusteks teistega. Saate ühendust luua kas kohaliku BLE-võrgustiku kaudu lähedalasuvate kasutajate jaoks või globaalse #geohash'i kaudu internetipõhiste, asukohapõhiste kogukondade jaoks.
- Privaatsõnumid:** Turvalisteks, üks-ühele vestlusteks. Need loovad otsese, krüpteeritud ühenduse, et hoida teabevahetus konfidentsiaalsena.


Mõlema režiimi mõistmine aitab teil vestlustes orienteeruda.


### Avalikud kanalid: Ühenduse keskus


Menüü "Asukohakanalid" (üleval paremal) kontrollib teie avalikku nähtavust. Valides `mesh` ühendab teid kõigi lähedal asuvate kasutajatega BLE võrgusilma kaudu, tavaliselt 10-50 meetri raadiuses asuvate seadmetega. See loob avatud foorumi, kus sõnumid edastatakse kõigile, kes on raadiuspiirkonnas, mis on ideaalne sündmustest teatamiseks või kohalike hoiatuste edastamiseks.


Laiema geograafilise ulatuse saavutamiseks valige ükskõik milline `#geohash` silt, et liituda internetipõhiste kogukondadega, mis on filtreeritud asukoha järgi. Need kanalid kasutavad Nostr protokolli releed, mis võimaldavad suhtlust üle linnade või piirkondade, säilitades samas asukohapõhise asjakohasuse. Teie sõnumid ilmuvad teistele samas kanalis osalejatele otseülekandes, kusjuures uued osalejad näevad liitumisel automaatselt hiljutisi sõnumeid.


![image](assets/en/06.webp)


### Eravestlused: Turvaline ja krüpteeritud


Privaatse vestluse alustamiseks puudutage ühe puudutusega otse mis tahes kasutajanime, mis on kuvatud "Peers Overview" (Peers Overview), ning võite ka puudutada tärni ikooni, et märkida kasutaja lemmikuks, mis hoiab ta teie kontaktide nimekirjas nähtavana ka siis, kui ta on võrguühenduseta.


![image](assets/en/07.webp)


Bitchat algatab automaatselt oma "turvakäepigistuse", kui alustate privaatset vestlust. Seadmed vahetavad ajutisi võtmeid, et luua spetsiaalselt teie vestluse jaoks krüpteeritud tunnel. See protsess tagab, et kõik teie sõnumid ja jagatud failid jäävad tänu pidevale otsast lõpuni krüpteerimisele konfidentsiaalseks. Privaatsõnumid toetavad teksti ja failide jagamist.


![image](assets/en/08.webp)


## 4️⃣ Lisafunktsioonid


Tegevuste paneelile pääseb koheselt ligi, kui sisestada `/` ükskõik kus Bitchat'is. See avab käskude menüü kiirtehingute jaoks.



- Halda ühendusi**: `Blokeeri kasutajad` või `Poolte blokeeringu tühistamine`
- Kanalite juhtimisseadmed**: `Kanalite näitamine` või `Kanalite liitumine/loomine`
- Sotsiaalne suhtlemine**: "Saada soe kallistus" või "lüüa forelliga" 🎣
- Vestluse hooldus**: `Clear chat sõnumeid`
- Privaatsustööriistad**: "Vaata, kes on võrgus" või "Saada privaatsõnum"


Käsklused täidetakse kohe - nagu `/block Satoshi`, et vaigistada kriitikuid või `/hug Hal`, et levitada positiivsust 🫂.


![image](assets/en/09.webp)


## 5️⃣ Kanali loomine


Bitchati kanalid võimaldavad organiseeritud suhtlust teemade, asukohtade või kogukondade ümber. Oma kanalite loomiseks järgige seda töövoogu:


### Samm 1: Loo kanal


Kanali loomiseks kirjuta `/j` või `/join`, millele järgneb `kanali nimi` suvalises vestluses (nt `/j <kanali nimi>`). Pärast loomist ilmub uus `ikoon ⧉`, mis näitab uut kanalit. Teised kasutajad saavad liituda, sisestades sama käsu (nt `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Samm 2: Seadete konfigureerimine


Lisaks vaikimisi käskudele on kanalis saadaval järgmised seaded:



- `/save` sõnumite salvestamiseks lokaalselt
- `/transfer` kanali omandiõiguse üleandmiseks ja
- `/pass`, et muuta kanali parooli.


Privaatsete kogukondade puhul võimaldab see käsk paroolikaitset, nõudes heakskiidetud liikmetelt enne liitumist kohandatud parooli sisestamist.


## 6️⃣ Paanikarežiim


Räägime nüüd sellest "paanikarežiimist": kolmekordne koputamine "Bitchat logo" algatab kõigi kohalike sõnumite ja andmete täieliku pühkimise rakenduses. See on teie ülim privaatsuskaitse, mis sobib ideaalselt olukordadesse, mis nõuavad kohest diskreetsust.


**Tähtis meeldetuletus:** _Paanikarežiim on püsiv. Kui see on aktiveeritud, ei saa andmeid taastada. Kasutage ettevaatlikult._


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Geohash-kanalid võimaldavad sihtotstarbelisi vestlusi, mis põhinevad pigem "geograafilistel asukohtadel" kui traditsioonilistel võrguühendustel. See funktsioon muudab bitchati asukohatundlikuks suhtlusvahendiks, mis sobib ideaalselt kohalikuks koordineerimiseks, kogukonna loomiseks ja asukohaspetsiifilisteks aruteludeks.


### Kuidas `#geohashes` töötab


Süsteem jagab maailma ruutudeks, kasutades [Geohash-süsteemi](https://en.wikipedia.org/wiki/Geohash), kus iga märk hashis tähistab suuremat täpsust:



- Tase 4** (nt "u33d"): Katab umbes 25 km × 25 km - ideaalne kogu linna hõlmavate arutelude jaoks
- Tase 6** (nt `u33d8z`): Katab umbes 1,2 km × 1,2 km - naabruskonna täpsus
- Tase 8** (nt `u33d8z1k`): Katab ligikaudu 150 m × 150 m - tänavasegmendi täpsus


Täppisvalik tasakaalustab privaatsust ja kasulikkust: kõrgemad tasemed loovad eksklusiivsemad tsoonid, kuid paljastavad teie asukoha täpsemalt.


### Liitumine `#geohash` kanalitega


1. Juurdepääs menüüle `#paiknemiskanalid`.

2. Valige soovitud täpsusaste ja sisestage `#geohash` (nt #u33d)

3. Koputage nuppu `Teleport`, et liituda `#kohakanaliga`.


![image](assets/en/12.webp)


Alternatiivina võite puudutada `kaardi ikooni`, et kasutada kaardivaadet täpsusastme määramiseks ja puudutada `valida`, et liituda `#koha kanaliga`.


![image](assets/en/13.webp)


**Tähtis meeldetuletus**: _#geohash-funktsioon nõuab aktiivset internetiühendust - erinevalt BLE võrgusüsteemist, mis töötab Bluetooth'i kaudu võrguühenduseta


## 8️⃣ Heatmaps


Heatmaps on lahe viis Bitchati sündmuste ja kanalite avastamiseks kogu maailmas. [Bitmap] (https://bitmap.lat/) visualiseerib ja jälgib anonüümseid, asukohapõhiseid sõnumeid Nostr võrgus, kuvades efektseid Nostr sündmusi. Vaadake ja liituge asukohaspetsiifiliste kanalite ja vestlustega.


![image](assets/en/15.webp)


## 🎯 Kokkuvõte


Bitchat võimaldab turvalist, detsentraliseeritud suhtlust stsenaariumide jaoks, kus traditsiooniline sõnumivahetus ebaõnnestub. See on võimeline töötama ilma interneti infrastruktuurita, kasutades BLE-võrgustikku, mis muudab selle sobivaks protestide, katastroofipiirkondade ja äärealade jaoks, kus ühendus on piiratud või tsenseeritud. Rakendus tagab privaatsuse efemerse võtme krüpteerimise, geohash-põhiste asukohakanalite ja paanikarežiimi andmete kustutamise abil.


Rakendus on veel arenduse algstaadiumis, kuid see on juba praegu paljulubav. Kasutajad peaksid ootama aeg-ajalt vigu ja teatama probleemidest [GitHub](https://github.com/permissionlesstech/bitchat-android/issues) kaudu. Parandused on plaanis, sealhulgas `ecash` integratsioon privaatsete rakendusesiseste tehingute jaoks, kasutades Cashu protokolli.


![image](assets/en/14.webp)


## 📚 Bitchat Resources


[Github](https://github.com/permissionlesstech) | [Veebileht ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)