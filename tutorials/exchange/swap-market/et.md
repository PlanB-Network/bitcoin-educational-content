---
name: SwapMarket
description: Bitcoin ja Lightning vahetusteenuste agregaator
---

![cover](assets/cover.webp)



Raha ülekandmine Bitcoin on-chain ja Lightning Network vahel nõuab üldiselt kas välkkiirte kanalite käsitsi avamist (tehniline ja kulukas) või tsentraliseeritud vahetusplatvormide kasutamist koos KYC-ga. SwapMarket pakub alternatiivi: usalduseta aatomivahetuslepingud konkurentsivõimeliste pakkujate kaudu, ilma KYC-ta.



Innovatsioon: kuigi teenusepakkujad on vahendajad, tagab HTLC (*Hash Time Locked Contracts*) matemaatiliselt, et teie rahalised vahendid jäävad teie kontrolli alla. Mitme teenusepakkuja (Boltz, ZEUS Swaps, Eldamar, Middle Way) koondamine loob hinnakonkurentsi. Interface veebi avatud lähtekoodiga isehostitav.



## Mis on SwapMarket?



2024. aastal käivitatud avatud lähtekoodiga agregaator SwapMarket toimib Bitcoin/Lightning vahetustehingute pakkujate võrdlejana. Kasutaja võrdleb koheselt tingimusi (tasud, likviidsus, limiidid) ja valib optimaalse pakkuja.



### Tehniline arhitektuur



**Frontend kliendipoolne**: 100% kliendipoolne rakendus (fork Boltz Web App), mis asub GitHubi lehekülgedel. Kood töötab brauseris ilma backend-serverita. Ajalugu salvestatakse lokaalselt (küpsised / vahemälu). Avalik ja auditeeritav lähtekood.



**Pakkuja avastamine** : Kõvakooditud nimekiri failis `src/configs/mainnet.ts`. Uued teenusepakkujad lisatakse Pull Request'i või e-posti teel.



**Sõltumatud tagapooled**: Iga teenusepakkuja kasutab oma Boltz backend'i. Kasutajaliides teeb reaalajas päringuid APIdele, et võrrelda hinnapakkumisi koheselt.



**HTLC aatomivahetused**: Hash Ajakinnitusega lepingud tagavad aatomsuse: kas vahetus toimub või kumbki osapool saab oma vahendid tagasi. Vastaspoole risk matemaatiliselt kõrvaldatud.



### Filosoofia



SwapMarket vähendab tsentraliseerimist, luues konkurentsi pakkujate vahel tasude ja likviidsuse osas. KYC puudub, avatud lähtekoodiga isehostitav kood, sõltumatute operaatorite paljunemine, et vältida üksikuid tõrkepunkte.



## Peamised omadused



### Teenusepakkuja turg



Kasutajaliideses kuvatakse kõik aktiivsed teenusepakkujad: teenusepakkuja nimi, kohaldatavad tasud (protsent ja/või fikseeritud), minimaalsed/maksimaalsed saadaolevad summad ja toetatavad vahetuslepingu tüübid. Rakendus küsib otse iga konfiguratsioonifailis viidatud teenusepakkuja APId, et saada reaalajas hinnapakkumisi. Konkurents teenusepakkujate vahel tagab optimaalsed hinnad, mis on standardvahetuste puhul tavaliselt umbes 0,5%.



### Kahesuunalised vahetused



**Swap-in (on-chain → Lightning)**: Konverteeri on-chain BTC-d Lightning satoshideks. Kasutusjuhtum: mobiilse wallet Lightning'i toitmine, sõlme sissetuleva võimsuse saamine või kohene likviidsus.



**Vahetus (Lightning → on-chain)**: Konverteeri Lightning satoshid on-chain BTC-deks. Kasutusjuhtum: wallet Lightningi tühjendamine külmhoonesse või kihtide vahelise likviidsuse tasakaalustamine.



### Ohutus ja taastumine



**Trustless aatomivahetused**: HTLCd tagavad, et kas vahetus viiakse lõpule täies ulatuses või mõlemad osapooled saavad oma osaluse tagasi. Vastaspoole risk on matemaatiliselt välistatud.



**Maksemehhanism**: Iga vahetus on ajalukk. Kui vahetus ebaõnnestub, makstakse raha automaatselt tagasi pärast tähtaja möödumist. Kasutajal on alati võimalus oma bitcoinid tagasi nõuda.



**Recovery keys**: SwapMarket võimaldab teil eksportida käimasolevate vahetuste taastamisvõtteid. Probleemi korral saab neid võtmeid kasutada vahetuse lõpetamiseks või tühistamiseks mis tahes seadmest.



## Paigaldamine ja juurdepääs



### Interface veeb



SwapMarket ei nõua paigaldamist. Juurdepääs toimub veebilehitseja kaudu, külastades veebilehte https://swapmarket.github.io. Maksimaalse konfidentsiaalsuse tagamiseks kasutage Brave'i, Firefoxi koos jälgimisvastaste laiendustega või LibreWolfi. Tor Browser on soovitatav võrgu anonüümsuse tagamiseks.



Registreerimine, e-posti aadress või isikusamasuse kontrollimine ei ole vajalik.



### Self-hosting (vabatahtlik)



Tehniliste kasutajate jaoks, kes soovivad kaotada igasuguse sõltuvuse ametlikust GitHubi lehekülgede domeenist, saab SwapMarketit käivitada lokaalselt :



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Viia Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Taotlus on kättesaadav aadressil "http://localhost:3000". Self-hosting tagab täieliku kontrolli liidese üle, välistab ametliku domeeni tsensuuri ohu ja võimaldab lähtekoodi auditeerida enne täitmist.



### Esialgne konfiguratsioon



**Wallet Lightning**: Veenduge, et teil on töökorras wallet Lightning (Phoenix, Zeus, BlueWallet jne). Vahetuse jaoks on teil generate Lightning arve. Väljavahetuse puhul maksate Lightning arve.



**Wallet on-chain**: wallet Bitcoin on-chain: Vahetuse jaoks on raha saatmiseks vaja wallet Bitcoin on-chain. Väljavahetuseks valmistage ette Bitcoin vastuvõtuaadress.



**Võimalik konfiguratsioon**: SwapMarket salvestab vahetusajaloo ja eelistused brauseri küpsistesse. Konto loomine ei ole vajalik.



## Juurdepääs seadetele ja päästevõti



Enne esimesi vahetusi soovitame tungivalt alla laadida **Rescue Key**. See päästevõti võimaldab teil taastada oma raha tehnilise probleemi või seadmele juurdepääsu kaotamise korral.



### Juurdepääsuparameetrid



Klõpsake SwapMarketi pealehel kasutajaliidese paremas ülaosas oleval hammasratta ikoonil (⚙️) vahetusvormi kõrval.



![Accès aux paramètres](assets/fr/01.webp)



### Lehekülje seaded



Avaneb lehekülg Seaded, kus kuvatakse mitu seadistusvõimalust:





- Nimetus**: Valik BTC või sats
- Detsimaalne eraldaja**: Kümnendaja eraldaja (, või .)
- Audio-/selveriteated**: Heli- ja brauseriteated
- Päästevõti** : Laadige alla taastamisvõti
- Logid**: Logide vaatamine, allalaadimine või kustutamine



![Page Settings](assets/fr/02.webp)



### Lae alla Rescue Key



Klõpsake nupule **Download**, mis asub nupu "Rescue Key" kõrval.



**Tähtsaid punkte** :




- Päästevõti on **üks-ühele hädaolukorra võti**, mis töötab kõigi teie tulevaste vahetuste puhul
- Hoidke seda võtit **turvalises ja püsivas** kohas (paroolihaldur, digitaalne seif)
- Vahetusprobleemi korral (aja ületamine, tehniline rike) võimaldab see võti teil oma raha tagasi saada



## Vahetuse loomine samm-sammult



### Väljavahetamine: Bitcoin



See esimene näide näitab, kuidas konverteerida Lightning satoshid on-chain bitcoinideks.



**Samm 1: Vahetage konfiguratsioon



Valige pealehel vahetusvorm :




- VALGUS** (ülemine väli): Sisestage summa, mille soovite saata sats Lightning'ina (näide: 30,000 sats)
- BITCOIN** (alumine väli): Summa, mille saate, kuvatakse automaatselt pärast tasude mahaarvamist (näide: 29,320 sats)



Sisestage alumisse lahtrisse oma **vastuvõtva Bitcoin aadress**, kuhu soovite raha saada. Kontrollige seda aadressi hoolikalt.



Vaikimisi teenusepakkuja on tavaliselt Boltz Exchange. Võrgutasud ja teenusepakkuja tasud on selgelt kuvatud.



![Configuration swap-out](assets/fr/03.webp)



**Samm 2: teenusepakkuja valik**



Klõpsake teenusepakkuja rippmenüüs (vaikimisi: "Boltz Exchange"), et kuvada kõik olemasolevad likviidsuse pakkujad.



Avaneb modaalne aken, mis kuvab võrdlustabelit:




- Staatus**: Green indikaator, kui teenuseosutaja on aktiivne
- Alias**: (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Tasu**: Teenusepakkuja poolt kohaldatavad tasud (tavaliselt 0,49% kuni 0,5%)
- Maksimaalne vahetus**: Maksimaalne summa, mis on lubatud vahetuseks



Võrrelge tasusid ja maksimumsummasid ning valige seejärel endale sobiv teenusepakkuja.



**Pöörake tähelepanu**: Teenuseosutaja valimise liides ei näita iga teenuseosutaja **miinimumsummasid**. See teave ilmub ainult vahetuslepingu loomise liideses pärast teenuseosutaja valimist. Minimaalsed ja maksimaalsed summad võivad teenusepakkujate lõikes erineda ja aja jooksul muutuda. **Kontrollige neid piirmäärasid alati oma vahetustehingu tegemise ajal**: kui summa, mida soovite vahetada, on väljaspool teenusepakkuja piirmäärasid, saate valida teise, teie tehingu jaoks sobivama teenusepakkuja.



![Sélection du provider](assets/fr/04.webp)



**Samm 3: Vahetuse loomine ja välkmakse**



Klõpsake kollasel **"LOODA ATOMIVAHETUS "** nupul. SwapMarket koostab generate teile **Välgatusarve** (BOLT11), mille eest saate tasuda oma wallet välgatusest.



Lehel kuvatakse :




- Vahetus ID**: Unikaalne swap-tunnus (näide: J4ymFIMVR6Hm)
- Staatus**: "swap.created" (swap loodud, ootab makseid)
- QR-kood**: Skaneeri seda oma wallet Lightningiga
- Invoice Lightning**: (näide: lnbc300u1p50whiv...gn5dk2szgqkvfkzc): märgijada, mis algab tähega "lnbc" (näide: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Makske see arve oma wallet Lightning (Phoenix, Zeus, BlueWallet jne) abil. Kuvatakse täpne makstav summa (näide: 30 000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Samm 4: Kinnitamine ja heakskiitmine**



Kui Lightning-makse on kinnitatud, saab SwapMarket koheselt teie makse ja teenusepakkuja edastab Bitcoin tehingu teie aadressile.



Staatus muutub **"arve.tasutud "** (arve tasutud) ja kuvatakse kinnitussõnum.



Teie on-chain bitcoinid on saadaval niipea, kui tehing on kinnitatud (tavaliselt mõne minuti kuni mõne tunni jooksul, sõltuvalt teenusepakkuja valitud mining tasudest).



![Confirmation swap-out](assets/fr/06.webp)



Võite klõpsata **"OPEN CLAIM TRANSACTION "**, et vaadata Bitcoin tehingut plokiahelaatori brauseris.



### Vahetus: Bitcoin → Välk



See teine näide näitab, kuidas konverteerida on-chain bitcoinid Lightning satoshideks.



**Samm 1: Vahetage konfiguratsioon



Valige pealehel vahetusvorm :




- BITCOIN** (ülemine väli): Sisestage summa, mida soovite saata sats Bitcoin (näide: 63 400 sats)
- VALGUS** (alumine väli): Pärast lõivude mahaarvamist kuvatakse automaatselt summa, mille saate (näide: 62 884 sats)



Sisestage alumisse lahtrisse Lightning** arve (BOLT11), mis on genereeritud teie wallet Lightningist, või kasutage oma LNURL-aadressi, kui teie wallet seda toetab.



![Configuration swap-in](assets/fr/07.webp)



**Samm 2: päästmisvõtme kontroll**



Pärast klõpsamist nupul **"LOODA ATOMILAHENDUS "** ilmub modaalne aken, milles palutakse teil kontrollida oma päästevõtit.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Kuna olete oma taastamisvõtme juba esialgse seadistamise ajal üles laadinud (vt eelmist jaotist), klõpsake salvestatud võtme importimiseks nupule **"VERIFY EXISTING KEY "** (Olemasoleva võtme kinnitamine).



Valige eelnevalt alla laetud päästevõti fail. Pärast edukat kontrollimist lülitub kasutajaliides automaatselt järgmisele sammule.



**Samm 3: Bitcoin** tagatisraha aadress



SwapMarket genereerib nüüd **üksikliku Bitcoin aadressi**, mis sisaldab teie Lightning-arvega seotud HTLC lepingut.



Lehel kuvatakse :




- Vahetus ID**: Unikaalne identifikaator (näide: 1kGmB6JyGqU4)
- Staatus**: "invoice.set" (arve seatud, ootab maksmist Bitcoin): "invoice.set" (arve seatud, ootab maksmist Bitcoin)
- QR-kood**: Bitcoin depoo aadress
- Bitcoin** aadress: Bc1p..." (näiteks: bc1p5mvtwxapjkds...9d4n9f)
- Hoiatus kollase värviga** : "Veenduge, et teie tehing kinnitatakse ~24 tunni jooksul pärast selle vahetuse loomist!"



See ~24-tunnine ajavahemik on HTLC lepingu **timeout**. Kui teie Bitcoin tehingut ei kinnitata selle aja jooksul, ebaõnnestub vahetus ja te peate kasutama oma raha tagasisaamiseks oma päästmisvõtit.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Saate aadressi kopeerida, klõpsates nupule **"ADRESS "** või skannida QR-koodi otse oma wallet on-chain-ga.



**Samm 4: bitcoinide saatmine**



Saatke oma wallet Bitcoin on-chain-st **täpselt** märgitud summa (nt 63 400 sats) genereeritud aadressile.



**Tähtis**: Kasutage asjakohaseid mining tasusid, et tagada kiire kinnitus. Kui tasu on liiga väike ja tehing jääb mempool'i üle aja (~24h), siis vahetus ebaõnnestub.



Kui tehing on saadetud, tuvastab SwapMarket, et see on mempoolis, ja kuvab :




- Staatus** : "transaction.mempool
- Sõnum**: "Tehing on mempoolis - ootab kinnitust, et vahetustehing lõpule viia"



![Transaction en mempool](assets/fr/10.webp)



**Samm 5: Kinnitus ja välk** vastuvõtt



Niipea, kui Bitcoin tehing saab esimese kinnituse, maksab teenusepakkuja automaatselt teie Lightning-arve. Saate kohe satoshis oma wallet Lightning'ile.



Staatus muutub **"transaction.claim.pending "**, seejärel kuvatakse kinnitussõnum:



![Confirmation swap-in](assets/fr/11.webp)



Teie Lightning satoshis on kohe saadaval teie wallet-s.



## Eelised ja piirangud



### Eelised



**Võitluskomisjon**: Teenusepakkujate koondumine tekitab loomuliku konkurentsi, mis tõmbab tasud alla (0,49% kuni 0,5%).



**Saladuse hoidmine**: Tor brauseriga ühilduv, 100% kliendipoolne kasutajaliides (ei edasta isikuandmeid).



**Mittehooldusõiguslik**: HTLC tagab matemaatiliselt ainukontrolli teie rahaliste vahendite üle. Kas vahetus õnnestub või saate oma bitcoinid tagasi.



**Avatud lähtekoodiga isehostitav**: auditeeritav avalik kood, mida saab kasutada kohapeal, et see oleks maksimaalselt tsensuurikindel.



### Piirangud



**Piiratud likviidsus**: Piiratud arv aktiivseid pakkujaid (Boltz, Eldamar, MiddleWay sõltuvalt perioodist). Maksimaalsed summad võivad olla piiratud.



**Lõppemise aeg**: Aegumine 24h kuni 48h. Kui on-chain tehingut ei kinnitata enne kehtivusaja lõppu, on vajalik käsitsi taastamine.



**Interface tsentraliseerimine**: Kuigi isehostitav, on ametlik liides majutatud GitHubi lehekülgedel. Kui GitHub tsenseerib repo, blokeeritakse juurdepääs swapmarket.github.io kaudu (lahendus: isehostimine).



**on-chain jäljed**: HTLC skriptid on potentsiaalselt tuvastatavad täiustatud plokiahela analüüsi abil.



## Parimad tavad



### Turvaline konfiguratsioon



**LAADIGE Päästevõti alla**: Enne esimesi vahetusi laadige alla oma päästevõti seadetest (vt eespool spetsiaalset jaotist). See unikaalne võti töötab kõigi teie tulevaste vahetuste puhul, võimaldades teil probleemide korral oma raha tagasi saada.



**Kasutage Tori brauserit**: SwapMarketile pääsete oma IP-aadressi varjamiseks maksimaalse konfidentsiaalsuse tagamiseks Tor Browser'i kaudu.



**Võta arvesse isehostimist**: Tehniliste kasutajate jaoks välistab SwapMarket'i enda instantsi kasutamine sõltuvuse ametlikust GitHubi lehekülgede domeenist.



### Vahetuse optimeerimine



**Hoidke silma peal mempoolil**: Kontrollige mempool.space enne vahetust. Valige madala aktiivsusega ajad, et vähendada mining kulusid.



**Kontrollige aadressid**: Vahetuse puhul kontrollige hoolikalt oma vastuvõtuaadressi. Kasutage kopeerimist ja kleepimist ning kontrollige 5 esimest ja 5 viimast märki.



**Katsetage väikeste kogustega**: Alustage minimaalse lubatud kogusega (25 000 kuni 50 000 sats). Suurendage järk-järgult, kui olete protsessi omandanud.



**Dokumenteerige oma vahetused**: Pange kirja iga vahetustehingu ID, lunastamisaadress ja kehtivusaeg. See teave hõlbustab jälgimist ja taastamist tehnilise probleemi korral.



### Kasutusstrateegia



**Balansseeri oma rahavoogusid**: Kasutage SwapMarketit, et kohandada oma jaotust on-chain (säästud, pikaajalised tagatised) ja Lightning (igapäevased kulud, kohesed maksed) vahel vastavalt oma tegelikele vajadustele.



**Kasumlikkuse arvutamine**: Püsiva Lightning'i likviidsusvajaduse korral võrrelge korduvate vahetustehingute kumulatiivseid kulusid võrreldes Lightning'i kanali otsese avamisega. SwapMarket paistab silma ühekordsete kohanduste puhul, mitte tingimata suurte regulaarsete voogude puhul.



## SwapMarket vs Boltz: Mis vahe on?



### Boltz: Boltz: Tehnoloogia vs



**Boltz on avatud lähtekoodiga tehnoloogia** (`boltz-backend` GitHubis), mis rakendab HTLC kaudu Bitcoin, Lightning ja Liquid vahel aatomivahetusi.



**Kriitiline punkt**: Kõik SwapMarket'i pakkujad (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) kasutavad oma Boltz'i backend'i instantsi. Seega on aluseks olev tehnoloogia identne. Haavatavus Boltzi taustsüsteemis mõjutaks potentsiaalselt kõiki teenusepakkujaid, kuid süsteemi avatud lähtekoodiga olemus võimaldab ühenduse auditeerimist.



**Boltz Exchange** on üks teenus, mida haldab Boltzi meeskond, samas kui **SwapMarket** ühendab mitmeid teenusepakkujaid, kes kõik kasutavad Boltzi tehnoloogiat, luues konkurentsivõimelise hinnakeskkonna.



Vaata lähemalt meie Boltzi ja Zeusi vahetuse õpetusi:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Peamised erinevused



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarketi eelised**: Hinnakonkurents, backend-instantside mitmekesistamine, reaalajas võrdlemine.



**Tehnoloogilised alternatiivid** (ei ühildu SwapMarketiga): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Need lahendused kasutavad omaenda allveevahetuse rakendusi.



**Soovitus**: Kasutage lihtsuse huvides Boltz Exchange või SwapMarketit, et optimeerida kulusid konkurentsi kaudu. Mõlemad on ohutuse poolest samaväärsed (HTLC ei ole kohustuslik).



## Kokkuvõte



SwapMarket hõlbustab Bitcoin/Lightning vahetust, koondades mitu pakkujat ühte liidesesse. HTLC arhitektuur tagab, et vahetuslepingud ei ole konfidentsiaalsed, KYC puudumine säilitab konfidentsiaalsuse ja isehaldatav avatud lähtekood tugevdab vastupanu tsensuurile.



Konkurents teenusepakkujate vahel parandab hindu ja mitmekordistab likviidsuse allikaid. Kahe tasandi juhtimise optimeerimiseks (on-chain kokkuhoid, Lightning-kulud) on SwapMarket praktiline vahend, mis säilitab finantssuveräänsuse ja konfidentsiaalsuse.



## Ressursid



### Ametlikud dokumendid




- [SwapMarket - veebirakendus](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Tehniline dokumentatsioon](https://docs.boltz.exchange/)
- [Juhend enesehosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Seotud projektid




- [Boltz Exchange](https://boltz.exchange) - Algne aatomi vahetusteenus
- [ZEUS Swaps](https://zeusln.com) - välkvahetuste pakkuja