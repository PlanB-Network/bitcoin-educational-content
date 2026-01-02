---
name: Silentium
description: Progressiivne veeb wallet vaikivate maksete toetusega (BIP-352)
---

![cover](assets/cover.webp)



Bitcoin aadresside korduvkasutamine on üks otsesemaid ohte kasutajate konfidentsiaalsusele. Kui saaja kasutab ühte aadressi mitme makse vastuvõtmiseks, võib iga vaatleja jälgida kõiki sellega seotud tehinguid ja rekonstrueerida nende finantsajalugu. See probleem mõjutab eelkõige sisuloojaid, heategevusorganisatsioone või aktiviste, kes soovivad avalikult näidata annetusaadressi, ilma et nende privaatsus oleks ohus.



Silentium vastab sellele probleemile elegantse lahendusega, mis on kättesaadav otse teie brauserist. See avatud lähtekoodiga progressiivne veebirakendus (PWA), mille käivitas mais 2024 Louis Singer, rakendab Silentiumi makseid (BIP-352): taaskasutatav staatiline aadress, kus iga makse jõuab eraldi plokiahela aadressile, ilma eelneva suhtluseta või tehingutevahelise jälgitava seoseta.



**Tähtis hoiatus**: Silentium on eksperimentaalne projekt, mis on Silent Payments'i kergete rahakottide *kontseptsioonitõend*. Seda ei tohiks kasutada igapäevase wallet või märkimisväärsete summade hoidmiseks. Arendajad märgivad selgesõnaliselt:



> Kasutage omal vastutusel.

Pange tähele, et seda wallet saab kasutada testvõrguna või regtestina.



## Mis on Silentium?



### Filosoofia ja eesmärgid



Silentium on tehniline näidis Silent Payments'i rakendamiseks kerges wallet brauseris. Kuigi see toetab ka tavalisi Bitcoin-aadresse, on rõhk Silent Payments'il, et võimaldada kasutajatel selle privaatsustehnoloogiaga lihtsal viisil eksperimenteerida.



### Kuidas toimivad vaikivad maksed?



Vaikne makse (BIP-352) kasutab Elliptic Curve Diffie-Hellmani võtit Exchange (ECDH). Vastuvõtja genereerib staatilise aadressi (`sp1...` mainnet puhul, `tsp1...` testneti puhul), mis koosneb kahest avalikust võtmest: skaneerimisvõti maksete tuvastamiseks ja kulutamisvõti nende kasutamiseks.



Saatja kombineerib oma salajased sisendvõtmed vastuvõtja skaneerimisvõtmega, et arvutada jagatud saladus, mis tekitab krüptograafilise "tweaki". See "tweak", mis lisatakse kulutuste võtmele, loob iga tehingu jaoks unikaalse Taproot aadressi. Vastuvõtja reprodutseerib selle arvutuse oma privaatse skaneerimisvõtmega, et tuvastada ja kulutada raha ilma eelneva suhtluseta.



Eelised: suurem konfidentsiaalsus saatja ja vastuvõtja jaoks, ei vaja kolmanda osapoole serverit, tehinguid ei saa eristada tavapärastest Taproot maksetest. Peamine puudus: plokiahela intensiivne skaneerimine maksete tuvastamiseks.



Vaikivate maksete teoreetilisest toimimisest saate rohkem teada BTC,204 kursuse viimases osas Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Toetatud platvormid



Silentium on progressiivne veebirakendus (PWA), mis on kättesaadav mis tahes kaasaegsest brauserist (mobiil- või lauaarvutist). Kasutage seda otse `app.silentium.dev`, installige see natiivse rakendusena oma brauseri kaudu või juurutage see lokaalselt. Installeerimine toimub otse brauserist, ilma ametlike poodide kaudu minemata.



## Veebirakenduse kasutamine



### Juurdepääs ja paigaldamine



[Mine veebilehitsejast aadressile `https://app.silentium.dev/`](https://app.silentium.dev/). Rakendus laadib koheselt ja kuvab avakuva.



Selle installimiseks iOS-i emakeelse rakendusena vajutage jagamisnuppu (nelinurk ülespoole suunatud noolega) ja valige seejärel "Avakuvale". Androidis pakub brauser tavaliselt otse "Lisa koduekraanile" teavitust. Pärast paigaldamist ilmub Silentium oma spetsiaalse ikooniga ja töötab nagu emakeelne rakendus, kuid vajab tehingute sünkroniseerimiseks internetiühendust.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Portfelli loomine



Esimesel käivitamisel valige "Create Wallet", et luua generate uus portfell, või "Restore Wallet", et taastada olemasolev taastamislause.



Valige "Loo Wallet". Rakendus genereerib 12-sõnalise lause, mille peate hoolikalt üles kirjutama. See fraas on ainus võimalus oma raha tagasi saada. Isegi testnetis võtke kasutusele head varundustavad. Vajutage pärast lause salvestamist "Jätka".



Seejärel palub rakendus teil määrata parool, et tagada juurdepääs wallet-le. Valige tugev parool ja kinnitage see.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Kui fraas on kinnitatud ja parool määratud, jõuate põhiliidesesse.



### Interface põhi- ja parameetrid



Peamine kasutajaliides näitab teie saldot satoshides (esialgu 0 sats), mille allosas on kolm nuppu:




- Sync**: sünkroniseerib wallet plokiahelaga
- Saada**: saada rahalisi vahendeid
- Saada**: bitcoinide saatmiseks



Juurdepääs seadistustele toimub üleval paremal asuva ikooni kaudu (kolm horisontaalset riba). Seadete menüü pakub mitmeid võimalusi:





- Umbes**: teave taotluse kohta
- Varukoopia**: taastamislause varukoopia
- Explorer**: valige blockchain explorer (vaikimisi Mempool) ja Silentiumd server
- Võrk**: võrgu valik (mainnet/testnet)
- Parool**: Muuda parool
- Ümberlaadimine**: wallet ümberlaadimine
- Reset**: täielik lähtestamine
- Teema**: teema muutmine



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Eriti oluline on jaotis **Eksplorer**: see võimaldab valida kasutatava plokiahela eksploreri (vaikimisi Mempool) ja kuvab ka Silentiumd serveri URL-i (mainnet puhul `https://bitcoin.silentium.dev/v1`). Kui te majutate oma Silentiumd-serverit või soovite kasutada testnet'i, siis seadistate need parameetrid siin.



### Raha saamine



Vajutage põhiliideses nuppu "Receive". Vaikimisi kuvab Silentium vaikimisi makse aadressi koos selle QR-koodiga. Aadress algab mainnet puhul `sp1...` või testnetis `tsp1...`.



Saate vaikiva makse ja klassikalise Bitcoin aadressi vahel vahetada, kasutades ekraani allosas asuvat nuppu "Üleminek klassikalisele aadressile" / "Üleminek vaikivale aadressile".



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Kui tehing on edastatud, oodake palun paar minutit. Silentium skaneerib Silentium vaikivate maksete puhul automaatselt plokiahelat teile mõeldud tehingute jaoks. Tehingud ilmuvad enne järkjärgulist kinnitamist staatusega "Kinnitamata".



### Saada makse



Vajutage põhiliideses nuppu "Saada". Saatmise ekraanil küsitakse teilt :



1. **Address**: kleebi vaikiva makse aadress (`sp1...` või `tsp1...`) või klassikaline Bitcoin aadress. Aadressi skaneerimiseks saate kasutada QR-skaneerimise ikooni.


2. **Summa**: sisestage saadetav summa satoshides. Lihtsaks sisestamiseks kuvatakse numbriline klahvistik. Teie olemasolev saldo kuvatakse ülalpool viitamiseks.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Kui olete sisestanud aadressi ja summa, vajutage jätkamiseks nuppu "Jätka". Enne tehingu kinnitamist palub rakendus teil valida soovitud tasu tase.



## wallet iseteenindus



### Miks ise hostida?



Silentiumi kohalik veebimajutus pakub täielikku suveräänsust, koodi kontrollimist, arenduskeskkonda ja vastupidavust ametliku saidi rikete korral.



### Eeltingimused



Node.js (versioon 14+), npm või yarn, Git ja umbes 500 MB kettaruumi.



### Kohalik paigaldus



Kloonige repositoorium ja installige :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Käivitamine ja kasutamine



Käivitage rakendus arendusrežiimis:



```bash
yarn start
```



Mine oma brauseris aadressile `http://localhost:3000`. Optimeeritud tootmisversioon :



```bash
yarn build
```



`build/'s loodud faile saab kasutada nginxi, Apache'i või mis tahes veebiserveriga. Vaikimisi ühendub Silentium avaliku serveriga `bitcoin.silentium.dev`. Muutke seda seadistust parameetrites, et kasutada testnet'i või oma serverit.



## Silentiumd server



### Roll ja toimimine



Silentium kasutab maksete tuvastamise optimeerimiseks **Silentiumd** indekseerimisserverit. Kõigi Taproot tehingute skaneerimine oleks brauseri või mobiiltelefoni jaoks liiga tülikas.



Silentiumd arvutab iga Taproot tehingu jaoks eelnevalt vaheandmed (tweaks). Teie wallet laeb need tweakid alla (paar baiti tehingu kohta) ja teostab lõpliku arvutuse lokaalselt, kontrollides makse omandiõigust. Erinevalt tavapärastest Electrum serveritest ei tea server kunagi teie võtmeid ega saa teie tehinguid tuvastada.



Kompaktsed BIP158-filtrid võimaldavad teie wallet-l määrata, milliseid plokke skaneerida, ilma et teie aadressid paljastuksid, säilitades seega teie konfidentsiaalsuse.



### Avalik server



Avalik server `bitcoin.silentium.dev` (mainnet), mida toetab Vulpem Ventures, pakub lihtsat ja vahetut kogemust. Kuigi konfidentsiaalsus on säilinud, eeldab see lähenemisviis suhtelist usaldust kolmanda osapoole infrastruktuuri suhtes.



### Hosta oma Silentiumd serverit



Täieliku suveräänsuse saavutamiseks majutage oma Silentiumd-serverit. Eeldused: Bitcoin Core mitte-elagged node koos `txindex=1` ja `blockfilterindex=1`, Go 1.21+, 10-20 GB kettaruumi, süsteemi administreerimise oskused.



**Installatsioon:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Konfigureeri keskkonnamuutujate abil (vt täpsemalt repositooriumi `config.md`). Server indekseerib plokiahelat ja avaldab API, mida saab teie wallet-ga pärida.



Praegu ei ole Umbrel või Start9 jaoks pakettlahendusi olemas, mis piirab ligipääsetavust mittetehnilistele kasutajatele.



## Eelised ja piirangud



### Tähtsündmused





- Maksimaalne ligipääsetavus**: kasutamine mis tahes brauserist, ei nõuta rasket paigaldamist
- Multiplatvormiline**: töötab mobiilis (Android/iOS) ja töölaual tänu PWA-tehnoloogiale
- Lihtne isehosting**: kohalik paigaldus võimalik paari käsuga
- Avatud lähtekood**: täielikult auditeeritav kood GitHubis
- Privaatsusele keskendunud**: ei jälgimine, ei analüütika, kohalikud krüptograafilised arvutused
- Eraldiseisev arhitektuur**: selge eraldatus wallet (klient) ja indekseerimisserveri vahel
- Ilma kontota**: ei nõuta registreerimist ega isikuandmeid



### Piirangud, millega tuleb arvestada





- Eksperimentaalne projekt**: ainult kontseptsiooni tõestus, ei ole mõeldud igapäevaseks kasutamiseks ega tootmiseks
- Garantiid puuduvad**: vigade ja haavatavuste oht, võimalik rahaliste vahendite kaotus
- Piiratud tugi**: vähe kasutajatega seotud dokumentatsiooni, väike kogukond, puudub ametlik tugi
- Serverisõltuvus**: nõuab toimivat Silentiumd serverit (avalik või ise majutatud)
- Intensiivne skaneerimine**: Vaikne maksete tuvastamine tarbib ribalaiust
- Vähendatud funktsionaalsus**: ei ole mündikontrolli, ei ole Lightning, ei ole multiallkirju



## Parimad tavad



### seed ohutus



Isegi testnetis suhtuge oma taastumislausesse tõsiselt. Kirjutage see üles ja hoidke seda turvalises kohas. Hoidke eraldi rahakotte testneti ja mainnet jaoks: ärge kunagi kasutage test seed-i wallet-l, mis on mõeldud reaalsete vahendite jaoks.



### Lähtekoodi kontrollimine



Üks isehostimise eeliseid on võimalus kontrollida lähtekoodi enne selle käivitamist. Kui kavatsete kasutada Silentiumit reaalsete vahenditega, võtke aega koodi auditeerimiseks või laske seda teha usaldusväärsel arendajal. Samuti võrrelge autentsuse tagamiseks `app.silentium.dev`i kaudu kasutusele võetud koodi hash'i GitHubi repositooriumi hash'iga.



### Varundamine ja taastamine



Silent Payments'i fondide taastamine eeldab wallet, mis on ühilduv BIP-352 protokolliga. Tavaline wallet ei saa plokiahelat skaneerida, et taastada teie UTXO Silent Payments. Hoidke Silentium installeeritud või veenduge, et teil on juurdepääs mõnele teisele ühilduvale wallet-le (näiteks Cake Wallet või muudele tulevastele implementatsioonidele), et vajaduse korral oma rahalisi vahendeid taastada.



## Kokkuvõte



Silentium pakub ligipääsetavat testimisvõimalust vaikivate maksete mõistmiseks ilma tehniliste takistusteta. Kontseptsioonitõendina demonstreerib see, kuidas seda privaatsustehnoloogiat saab integreerida wallet brauserisse, säilitades samal ajal enesehoidmise. Katsetage testnetis, et avastada seda paljulubavat läbimurret on-chain privaatsuse jaoks.



## Ressursid



### Ametlikud dokumendid




- Silentium GitHub repositoorium (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub repositoorium (server): https://github.com/louisinger/silentiumd
- Veebirakendus: https://app.silentium.dev/
- Vaikiv maksekeskkonna sait: https://silentpayments.xyz
- Spetsifikatsioon BIP-352: https://bips.dev/352



### Artiklid ja ressursid




- Ametlik teade (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Vaiksed maksed: https://bitcoinops.org/en/topics/silent-payments/



### Testnet tööriistad




- Testnet kraan: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet