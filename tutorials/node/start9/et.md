---
name: Start9

description: Tutorial Start9 privaatserveri loomise kohta

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Siin on video õpetus Lõuna Bitcoiner, video juhend, mis näitab teile, kuidas seadistada ja kasutada Start9 / StartOS isiklik server, ja kuidas käivitada Bitcoin node.*


## 1️⃣ Sissejuhatus


### Mis täpselt on Start9?


Start9 on 2020. aastal asutatud ettevõte, mis on kõige paremini tuntud [**StartOS**,](https://github.com/Start9Labs/start-os), personaalsetele serveritele mõeldud Linuxil põhineva operatsioonisüsteemi väljatöötamise poolest. See võimaldab kasutajatel hõlpsasti ise hostida mitmesuguseid tarkvarateenuseid - näiteks Bitcoin ja Lightning-sõlmed, sõnumirakendused või paroolihaldurid -, säilitades samal ajal täieliku kontrolli oma andmete üle ja kaotades sõltuvuse tsentraliseeritud tehnoloogiaplatvormidest. StartOSil on kasutajasõbralik, brauseripõhine kasutajaliides, kureeritud Marketplace teenuste paigaldamiseks ning sisseehitatud privaatsustööriistad, nagu Tor-integratsioon ja kogu süsteemi hõlmav HTTPS-krüpteerimine. Start9 pakub ka riistvaraseadmeid, mis on operatsioonisüsteemiga eeltäidetud, kuigi tarkvara saab paigaldada ühilduvale riistvarale või virtuaalmasinatele (VM).


### Millised võimalused on saadaval?


Start9 pakub nii valmis- kui ka omatehtud kasutuselevõtuvõimalusi. [**Server One**] (https://store.start9.com/collections/servers/products/server-one) ja [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) on ametlikud riistvaralised seadmed, mis on varustatud suure jõudlusega komponentidega: Server One kasutab **AMD Ryzen 7 5825U** protsessorit koos konfigureeritava RAM-i (16 GB-64 GB) ja mälu (2TB-4TB NVMe SSD), samas kui Server Pure on varustatud **Intel i7-10710U**-ga, mis pakub samuti konfigureeritavat RAM-i ja mälu. Mõlemad sisaldavad **eluaegset tehnilist tuge**, kui need ostetakse otse Start9-st. Paindlikkust eelistavate kasutajate jaoks saab StartOSi tasuta paigaldada paljudele olemasolevatele riistvaradele, sealhulgas sülearvutitele, lauaarvutitele, miniarvutitele ja üheplaanilistele arvutitele või VM-i raames.


![image](assets/en/01.webp)


### Millised on erinevused Umbrelist?


StartOS ja Umbrel lihtsustavad mõlemad isehostitava teenuse paigaldamist, kuid erinevad arhitektuuri ja funktsioonide poolest. Umbrel töötab rakenduskihina Debian/Ubuntu süsteemides või VM-des, samas kui Start9 on spetsiaalne operatsioonisüsteem, mis nõuab otsest riistvara või VM-i paigaldamist. Umbrelil on lihvitud, macOSist inspireeritud kasutajaliides, samas kui Start9 seab esikohale funktsionaalse, minimaalse disaini. Umbrel pakub suuremat [rakenduste valikut](https://apps.umbrel.com/), samas kui [Start9 Marketplace](https://marketplace.start9.com/) kompenseerib seda täiustatud tehniliste võimalustega. Start9 lihtsustab juurdepääsu täiustatud seadetele valideeritud kasutajaliidese vormide kaudu, vähendades vajadust käsurea interaktsiooni järele. Samuti on see suurepärane varunduste haldamisel ühe klõpsuga krüpteeritud süsteemi varunduste abil, mis on funktsioon, mis Umbrelil puudub algselt. StartOS pakub sisseehitatud seiretööriistu ja rakendab HTTPS-krüpteerimist kohalikule võrgule juurdepääsuks, mis suurendab turvalisust. Umbrel kasutab lokaalselt krüpteerimata HTTP-d, kuigi mõlemad platvormid toetavad turvalist kaugjuurdepääsu Tor'i kaudu. Umbrel sobib kasutajatele, kes eelistavad rikkalikku rakenduste ökosüsteemi ja lihvitud kasutajaliidest. Start9 on tugev valik neile, kes hindavad turvalisust, konfigureeritavust, varunduskindlust ja täiustatud teenuste haldamist, ilma et see nõuaks käsurea teadmisi. Umbreli ja erinevuste kohta Start9-ga võrreldes saate rohkem teavet selle kursuse kaudu:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ DIY Eeldused: Spetsifikatsioonid: minimaalsed ja soovitatavad näitajad


Põhikasutuseks minimaalsete teenustega on **minimaalsed näitajad** järgmised: **1 vCPU tuum (2,0 GHz+ boost), 4 GB RAM, 64 GB mälu** ja Ethernet-port. See tähendab, et ma soovitan minna sellest kaugemale, eriti kui te kasutate Bitcoin Node'i. Mina isiklikult alustasin 1TB-ga ja mul sai ruum kiiresti otsa. Parem on püüda saavutada **miinimum 2TB salvestusruumi**, koos **neljatuumalise protsessoriga (2,5GHz+)** ja **8GB+ RAMiga**. See muudab jõudluse ja pikaealisuse osas tohutult palju. Kui soovite süveneda, siis siin on ajakohane kogukonna teema [StartOSi käivitamiseks sobiv riistvara](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Laadimine ja püsivara väljalülitamine


Seadistamise alustamiseks külastage [Start9 veebilehte](https://start9.com/) eraldi arvutist ja navigeerige dokumentatsiooni sektsiooni, klõpsates nupul `DOCS`. Sealt pääsete sisse `Flashing Guides`, et leida sobiv StartOSi versioon. Saadaval on kaks võimalust:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


See õpetus käsitleb valikut `x86/ARM`.


Uusima operatsioonisüsteemi versiooni saab alla laadida [Githubi avaldamislehelt](https://github.com/Start9Labs/start-os/releases/latest). [Pre-release](https://github.com/Start9Labs/start-os/releases) versioonid on saadaval ka kasutajatele, kes soovivad uusi funktsioone testida. Lehe allosas, `Assets` all, laadige alla `x86_64` või `x86_64-nonfree.iso`.  Pilt `x86_64-nonfree.iso` sisaldab mittevaba (suletud lähtekoodiga) tarkvara, mis on vajalik Server One'i ja enamiku DIY riistvara jaoks, eriti graafika ja võrguseadmete toe jaoks.


Soovitatav on kontrollida faili terviklikkust, kontrollides selle SHA256-hash'i GitHubis loetletud faili suhtes. Linuxi puhul võib kasutada käsku `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso`, teiste operatsioonisüsteemide puhul on seda dokumentatsioonis kirjeldatud.


Pärast StartOS-kujutise allalaadimist ja kontrollimist tuleb see USB-kettale salvestada. selleks on soovitatav tarkvara `BalenaEtcher`. See on tasuta, avatud lähtekoodiga tööriist operatsioonisüsteemi kujutisfailide kirjutamiseks USB-kettale ja SD-kaardile, mis on saadaval Windowsile, macOSile ja Linuxile. Laadige sobiv versioon alla ametlikust [Balena Etcher'i veebisaidilt](https://www.balena.io/etcher/) ja käivitage paigaldusprogramm. Ühendage siht-USB-ketas või SD-kaart, avage Balena Etcher ja klõpsake `Flash from file`, et valida allalaaditud operatsioonisüsteemi kujutis. Etcher tuvastab automaatselt ühendatud kettad; valige õige sihtmärk, kui neid on mitu. Klõpsake `Flash!`, et alustada kujutise kirjutamist. Etcher valideerib kirjutamisprotsessi lõpetamisel automaatselt. Kui see on lõpetatud, eemaldage ketas ohutult ja kasutage seda seadme käivitamiseks.


![image](assets/en/19.webp)


## 4️⃣ Esialgne seadistamine


Esialgse seadistamise kohta vaadake lehekülge Start9 [dokumentatsioon](https://docs.start9.com/0.3.5.x/) jaotises `KASUTUSJUHEND`, millele järgneb "Alustamine - Esialgne seadistamine".  Kõige ajakohasema teabe saamiseks tuleks tutvuda selle ametliku juhendiga.


Esitatud on kaks võimalust:



- Alusta värskelt
- Taastamisvõimalused


Uue serveri paigaldamiseks valige `Start Fresh`. Kõigepealt ühendage server voolu ja Ethernet-kaabliga. Veenduge, et seadistamiseks kasutatav arvuti on samas kohalikus võrgus. Eemaldage äsja väljalülitatud USB-ketas arvutist ja sisestage see serverisse.


Saate serverit juhtida eemalt mis tahes arvutist samas võrgus. Avage veebibrauser ja navigeerige veebilehele `http://start.local`.


**Märkus**: Kui selle aadressiga tekib ühendusprobleeme, on see sageli tingitud sellest, et koduvõrgud ei suuda lahendada .local domeeninimesid. Probleemi saab lahendada, kui pöörduda otse serverisse selle IP-aadressi kaudu. IP-aadressi saab leida, kui logida sisse ruuteri haldusliidesesse (tavaliselt aadressil `192.168.1.1` või sarnasel aadressil) ja leida seade DHCP-klientide või võrgukaartide nimekirjast. Seejärel sisestage veebilehitsejas täielik IP-aadress (nt `http://192.168.1.105`). Sellega möödub DNS-lahendus. Kui probleemid püsivad, vaadake [üldiste probleemide lehekülge](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) või [võtke ühendust nende kasutajatoega](https://start9.com/contact/)


Tuleks ilmuda StartOSi häälestusekraan. Uue serveri seadistamise alustamiseks klõpsake nuppu `Start Fresh`.


![image](assets/en/03.webp)


Järgmine samm on valida salvestusketas, kuhu StartOSi andmed salvestatakse.


![image](assets/en/04.webp)


Määrake serverile tugev "Parool". Salvestage see Start9 soovituste kohaselt ja klõpsake seejärel nuppu `FINISH`.


![image](assets/en/05.webp)


Ekraanil kuvatakse, et StartOS initsialiseerib ja seadistab serverit. Järgmine samm on `Download address info`, kuna `start.local` aadress on ainult seadistamise eesmärgil ja pärast seda ei tööta.


![image](assets/en/06.webp)


Konfiguratsioonifail sisaldab kahte kriitilist juurdepääsu aadressi: üks "kohtvõrgu (LAN)" ja teine turvalise juurdepääsu jaoks "Tori" kaudu. Mõlemad aadressid tuleks salvestada turvalisse paroolihaldurisse. Järgmine samm on `Trust your Root CA`. Avage uus brauseri vahekaart ja järgige juhiseid, et usaldada Root CA-d ja logida sisse. Root CA sertifikaadi saab ka alla laadida, klõpsates allalaaditud failis `Download certificate`.


## 5️⃣ Usaldage oma juur CA-d


Pärast sertifikaadi allalaadimist peab operatsioonisüsteem usaldama serveri `Root CA`d. Klõpsake `View Instructions` ja leidke juhised konkreetse operatsioonisüsteemi jaoks.


![image](assets/en/07.webp)


Linuxi süsteemi puhul kasutatakse järgmisi käske. Kõigepealt avage terminal ja installige vajalikud paketid:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Navigeerige kataloogi, kuhu sertifikaat alla laaditi, tavaliselt `~/Downloads` . Sooritage need käsud, et lisada sertifikaat operatsioonisüsteemi usalduskaubamajja. Muutke allalaadimiste kausta `cd ~/Downloads`. Looge vajalik kataloog `sudo mkdir -p /usr/share/ca-certificates/start9` abil. Kopeerige sertifikaadifail, asendades `your-filename.crt` tegeliku failinimega, kasutades `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/`. Registreerige sertifikaat püsivalt, lisades selle tee süsteemi konfiguratsiooni käsuga `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`. Lõpuks ehitage usalduskauplus uuesti üles käsuga `sudo update-ca-certificates`. Enne nende käskude täitmist on oluline kasutada tegelikku sertifikaadi failinime ja kontrollida kõiki teekondi. See protsess loob alalise usalduse Start9 serveri HTTPS-ühenduste jaoks.


Edukast paigaldamisest annab märku väljund "1 lisatud". Enamik rakendusi saab seejärel turvaliselt ühendust `https` kaudu. Firefoxi kasutamisel on vaja täiendavat [viimast sammu](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). Chrome'i või Brave'i puhul on vajalik teine [viimane samm](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome), et konfigureerida veebilehitseja nii, et see austaks root CA-d. Testige ühendust, värskendades lehte. Kui probleem püsib, lõpetage ja avage brauser uuesti, enne kui külastate lehte uuesti.


![image](assets/en/08.webp)


## 6️⃣ StartOSi kasutuselevõtmine


Nüüd peaks olema võimalik sisse logida turvalise HTTPS-ühenduse kaudu. Sisestage `Password`, et pääseda `Tervitusekraanile`.


![image](assets/en/09.webp)


See ekraan pakub kasulikke otseteid alustamiseks. Vasakpoolne külgriba sisaldab peamisi menüüpunkte navigeerimiseks.


## 7️⃣ Süsteem


StartOSi vahekaart Süsteemid võimaldab juurdepääsu personaalserveri haldamiseks vajalikele põhilistele süsteemifunktsioonidele. See pakub vahendeid süsteemi hoolduseks, turvalisuseks, diagnostikaks ja konfigureerimiseks, ilma et selleks oleks vaja käsurea teadmisi.


Jaotis "Varukoopiad" võimaldab luua süsteemi täielikke varukoopiaid, sealhulgas teenuste, konfiguratsioonide ja andmete varukoopiaid, mida saab hiljem taastada. See on hädavajalik katastroofide taastamiseks või uuele riistvarale üleminekuks. Varukoopiaid saab salvestada välistele kõvakettadele ja need on krüpteeritud põhiparooliga.


Süsteemi vahekaardil olev jaotis "Haldamine" võimaldab kontrollida süsteemi põhifunktsioone. Kasutajad saavad käsitsi kontrollida ja rakendada StartOSi uuendusi, säilitades kontrolli süsteemi uuendamise protsessi üle. Võimalik on laadida küljelaadetisena kohandatud või kolmanda osapoole teenuseid, mis ei ole ametlikul turul saadaval. Kui server ei ole ühendatud Etherneti kaudu, saab selles jaotises konfigureerida Wi-Fi seadeid. Edasijõudnud kasutajad saavad lubada SSH-juurdepääsu süsteemi haldamiseks terminalitasandil.


![image](assets/en/10.webp)


Jaotises `Insights` saab reaalajas jälgida serveri jõudlust ja tervist, näidates graafikute abil protsessori, RAM-i ja ketta kasutamist. Samuti näitab see süsteemi temperatuuri, mis on kasulik selliste seadmete puhul nagu Raspberry Pi, millel puudub aktiivne jahutus. Kasutusaja ja koormuse keskmised näitajad aitavad hinnata süsteemi stabiilsust ning reaalajas logid on saadaval teenuse või süsteemiprobleemide tõrkeotsinguks.


Tugi" sektsioon pakub juurdepääsu sisseehitatud KKK-dele, ametlikule dokumentatsioonile ja kogukonna tugikanalitele. Sellest sektsioonist saab alla laadida veaprotokolle, mida saab probleemide kiiremaks lahendamiseks Start9 toega jagada.


![image](assets/en/11.webp)


## 8️⃣ Marketplace


Turuplatsi kasutatakse teenuste avastamiseks, paigaldamiseks ja haldamiseks isiklikus serveris. See pakub juurdepääsu sellistele tarkvaradele nagu Bitcoin Core, BTCPay Server ja electrs. StartOS toetab mitut turuplatsi, sealhulgas ametlikku Start9 registrit ja kogukonna juhitud registreid. Neid saab lisada, klõpsates `CHANGE` ja lülitades `Community Registry`, mis pakub juurdepääsu laiemale hulgale teenustele.


![image](assets/en/12.webp)


## 9️⃣ Bitcoin täieliku sõlme paigaldamine


Bitcoin full node paigaldamine StartOS-i annab täieliku suveräänsuse Bitcoin kogemuse üle. See võimaldab tehingute valideerimist ning suurendab eraelu puutumatust ja turvalisust, kaotades sõltuvuse välistest teenustest, mis võivad tegevust logida. Tehingute üle saavutatakse täielik kontroll, võimaldades neid otse võrku edastada. Vaikimisi valik on `Bitcoin Core`, mis integreerub algselt StartOSiga ja võimaldab ühendust selliste rahakottidega nagu Specter, Sparrow või Electrum, et luua isehaldamine. Alternatiiv, `Bitcoin Knots`, on saadaval ka ühenduse registri kaudu.


Bitcoin Core'i installimiseks navigeerige turuplatsile. Leidke vaikimisi registrist teenus Bitcoin Core ja installige see. Pärast paigaldamist ilmub ekraanile "vajab seadistamist", mis nõuab seadistuste lõpuleviimist enne teenuse käivitamist. See ilmneb tavaliselt pärast uuendusi või värsket installimist ja nõuab RPC seadete läbivaatamist. Jätkake vaikimisi seadistusega ja klõpsake nuppu `Save` (Salvesta).


![image](assets/en/13.webp)


Pärast täielikku sünkroniseerimist saab teie sõlme kasutada privaatse backendina selliste rahakottide jaoks nagu Sparrow, mis pakub täiustatud privaatsust ja tehingu valideerimist. Märkimisväärseid summasid salvestavate kasutajate jaoks on siiski oluline mõista selle otsese ühenduse turvalisuse kompromissid. Kui wallet ühendub otse Bitcoin Core'iga, võib see paljastada tundlikke andmeid, sest Bitcoin Core hoiab avalikke võtmeid (xpubs) ja wallet saldosid krüpteerimata vastuvõtvas masinas. Ründaja võib kahjustatud süsteemi kaudu avastada teie varud ja võtta teid sihikule.


Selle riski vähendamiseks ja tugevama turvamudeli saavutamiseks saate luua privaatse Electrum Server. See server tegutseb vahendajana, indekseerides plokiahelat, salvestamata wallet-spetsiifilist teavet. Ühendades oma wallet oma Electrum serveriga, mitte otse Bitcoin Core'iga, takistate wallet juurdepääsu sõlme tundlikele andmetele.


![image](assets/en/14.webp)


## 🔟 Seadistage valijad


`electrs` (Electrum Rust Server) on kiire ja tõhus indekseerija, mis ühendub teie Bitcoin Core sõlme ja võimaldab Electrum-ga ühilduvatel rahakottidel pärida tehinguajalugu ja saldosid reaalajas. Käivitades electrs'i StartOSis, kaotate sõltuvuse kolmanda osapoole Electrum serveritest, parandades oluliselt privaatsust ja turvalisust - teie wallet päringud lähevad otse teie isehostitud sõlme.


Selle seadistamiseks installige esmalt teenus electrs StartOS Marketplace'ist. Süsteem nõuab, et Bitcoin Core oleks enne jätkamist täielikult sünkroonitud. Pärast paigaldamist kinnitage `Needs Config` seaded soovitatud vaikimisi ja electrs alustab plokiahela indekseerimist, mis võib sõltuvalt riistvarast võtta kuni ühe päeva.


![image](assets/en/15.webp)


Kui see on lõpule viidud, saate ühendada rahakotid nagu Sparrow või Specter. Edukas ühendus võimaldab teie wallet sünkroonida otse teie sõlme, pakkudes turvalist, privaatset ja isehostitud Bitcoin kogemust.


## 1️⃣1️⃣ Connect Sparrow Wallet


Sparrow Wallet ühendamiseks oma StartOS-sõlmega, kasutades electrs rakendamist, veenduge esmalt, et Bitcoin Core on täielikult sünkroonitud ja electrs on paigaldatud ja töötab. Avage oma seadmes Sparrow Wallet ja navigeerige menüüsse `File` -> `Settings` -> `Server`. Seejärel valige `Privaatne Electrum Server`. Sisestage URL-väljale `Tor hostname` ja `Port` electrs'i jaoks, mille leiate StartOSist jaotisest `Services` -> `electrs` -> `Properties` (tavaliselt lõpeb `.onion:50001`).


![image](assets/en/16.webp)


Järgmisena aktiveerige Tor, märgistades "Kasuta proksi", määrates proksi aadressiks "127.0.0.1" ja portiks "9050". Klõpsake nuppu `Test Connection` ja oodake mõni hetk. Eduka ühenduse korral kuvatakse kinnitussõnum `Connected to electrs`. Pärast kinnitamist sulgege seaded ja jätkake wallet loomist või taastamist. See seadistus tagab, et teie wallet küsib electrs'i kaudu oma sõlme, tagades täieliku privaatsuse ja usaldusväärse töö.


![image](assets/en/17.webp)


## 🎯 Kokkuvõte


StartOS by Start9 on kasutajasõbralik, privaatsusele keskendunud platvorm, mis on mõeldud selliste oluliste teenuste nagu Bitcoin ja Lightning-sõlmede, rahakottide ja isiklike rakenduste isehostimiseks. See kõrvaldab vajaduse käsurea oskuste järele, pakkudes puhast graafilist kasutajaliidest, automaatseid varukoopiaid, tervisekontrolli ja turvalist juurdepääsu Torile, mis muudab selle ideaalseks ka mittetehnilistele kasutajatele. Selle modulaarne ülesehitus toetab sujuvat integreerimist selliste vahenditega nagu electrs või Sparrow, andes teile täieliku kontrolli oma finants- ja digitaalse suveräänsuse üle. Kuna StartOS keskendub läbipaistvusele, kohalikule kontrollile ja laiendatavusele, annab see kasutajatele võimaluse nõuda tsentraliseeritud platvormidelt tagasi omandiõigus ja juhtida oma privaatset, vastupidavat infrastruktuuri.