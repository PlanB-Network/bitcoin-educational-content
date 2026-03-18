---
name: ArkadeOS
description: Täielik juhend Arkade portfelli ja Ark protokolli kohta
---

![cover](assets/cover.webp)



Bitcoin võrgu ees seisab suur väljakutse: skaleeritavus. Kuigi põhikiht (1. kiht) pakub võrratut turvalisust ja detsentraliseeritust, suudab see töödelda vaid piiratud arvu tehinguid sekundis. Lightning Network on kujunenud paljulubavaks teise kihi (2. kiht) lahenduseks, mis võimaldab kiireid ja odavaid makseid. Lightning seab aga oma piirangud: kanalite haldamine, vajadus sissetuleva likviidsuse järele ja tehniline keerukus, mis võib uusi kasutajaid eemale peletada.



See on **Ark**, uue 2. kihi protokolli taustaks, mille eesmärk on pakkuda lihtsustatud kasutajakogemust ilma suveräänsust ohverdamata. **ArkadeOS** (ehk Arkade) on selle protokolli esimene suurem rakendus, mis pakub järgmise põlvkonna Bitcoin portfelli.



See õpetus juhatab teid läbi Arkade maailma. Uurime, kuidas Arkade protokoll töötab, kuidas paigaldada ja konfigureerida Arkade wallet ning kuidas seda kasutada bitcoinide koheseks saatmiseks ja vastuvõtmiseks, konfidentsiaalselt ja ilma tavaliste Lightning Network hõõrdumisteta.



## Argi protokolli mõistmine



Enne Arkade'i kasutamisse sukeldumist on oluline mõista selle aluseks oleva Ark-protokolli põhimõisteid. Ark ei ole eraldi plokiahela, vaid Bitcoin peal asuv intelligentne koordineerimismehhanism.



### VTXO kontseptsioon


Arki keskmes on **VTXO** (Virtual UTXO). VTXO on UTXO, mida ei ole veel avaldatud Bitcoin plokiahelas: see eksisteerib väljaspool põhiahelat (off-chain), kuid on tagatud plokiahelas eelnevalt allkirjastatud tehingutega.



Erinevalt tsentraliseeritud börsil olevast saldost kuulub VTXO tegelikult teile. Teil on krüptograafiline tõend, mis võimaldab teil igal ajal nõuda vastavaid reaalseid bitcoine plokiahelas, isegi kui Ark server kaob. VTXOd võimaldavad teil väärtust koheselt kasutajate vahel üle kanda, ootamata plokkide kinnitusi.



### ASP (Ark Service Provider) roll


Ark protokoll töötab klient-server mudelil. Serveri nimi on **ASP** (Ark Service Provider). ASP täidab dirigendi rolli:




- See tagab võrgu jaoks vajaliku likviidsuse.
- See koordineerib kasutajate vahelisi tehinguid.
- See organiseerib arvelduse "voorud" plokiahelas.



Oluline on märkida, et ASP on **mittekaitstav**. See ei hoia kunagi teie isiklikke võtmeid ega saa teie raha varastada. Selle roll on puhtalt tehniline ja logistiline. Kui ASP tsenseerib teie tehinguid või läheb katki, saate alati oma raha tagasi saada ühepoolse väljumismenetluse kaudu.



### Ringid ja privaatsus


Tehingud Ark'is lõpetatakse partiidena, mida nimetatakse **Roundideks**. Aeg-ajalt (nt iga paari sekundi tagant) kogub ASP kõik pooleliolevad tehingud kokku ja ankurdab need Bitcoin plokiahelas üheks optimeeritud tehinguks.


Sellel mehhanismil on kaks olulist eelist:




- Skaleeritavus**: Üks on-chain tehing võib valideerida tuhandeid off-chain makseid, mis vähendab oluliselt kasutajate kulusid.
- Konfidentsiaalsus**: Iga voor toimib **CoinJoin**. Kõigi osalejate vahendid segatakse enne uute VTXOde vormis ümberjaotamist ühisesse reservi. See katkestab sideme saatja ja saaja vahel, muutes maksete jälgimise väljastpoolt tuleva vaatleja jaoks äärmiselt keeruliseks, kui mitte võimatuks.



## ArkadeOS esitlus



ArkadeOS on konkreetne rakendus, mis teeb Ark-protokolli üldsusele kättesaadavaks. See on Ark Labs'i poolt välja töötatud terviklik ökosüsteem, mis koosneb portfellist (Wallet), serverist (Operator) ja arendajatööriistadest.



Lõppkasutaja jaoks on Arkade elegantse ja intuitiivse veebi wallet (PWA - Progressive Web App) kujul. See peidab VTXOde ja voorude krüptograafilise keerukuse tuttava kasutajaliidese taha. Arkade'i abil on teil aadress vastuvõtmiseks, nupp saatmiseks ja tehingute ajalugu, nagu klassikalises wallet-s, kuid Arkade'i vahetu ja konfidentsiaalsuse võimsusega.



## Paigaldamine ja konfigureerimine



Kuna Arkade on progressiivne veebirakendus, on seda eriti lihtne paigaldada ja see ei pruugi hõlmata traditsioonilisi rakenduste poode.



### Juurdepääs ja paigaldamine


Saate Arkade'ile ligi otse igast moodsast veebibrauserist (Chrome, Safari, Brave) arvutis või mobiilis.





- Külastage rakenduse ametlikku veebisaiti: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Teid tervitavad mitmed sissejuhatavad ekraanid, mis tutvustavad teile Arkade'i põhimõisteid: Bitcoin uus ökosüsteem, isehalduse tähtsus ja partiitehingute eelised.



![arkade onboarding](assets/fr/02.webp)





- Androidis (Chrome/Brave)** : Vajutage brauseri menüüd (kolm punkti) ja valige "Install application" või "Add to home screen".
- IOS-is (Safari)**: Vajutage jagamisnuppu (nelinurk ülespoole suunatud noolega) ja valige "Avakuval".



Kui Arkade on installitud, käivitub see nagu loomulik rakendus, täisekraanil ja ilma aadressiribata.



### Portfelli loomine


Esimesel käivitamisel palutakse teil konfigureerida oma portfell.





- Klõpsake **"Create New Wallet"**.



![create wallet](assets/fr/03.webp)





- wallet luuakse koheselt. Erinevalt traditsioonilistest Bitcoin rahakottidest ei kasuta **Arkade 12- või 24-sõnalist taastamislauset**. Selle asemel genereerib Arkade automaatselt **privaatvõtme** Nostr (nsec) formaadis, mida kasutatakse teie wallet varundamiseks ja taastamiseks. Ärge unustage seda võtit kohe salvestada (vt järgmine lõik).





- Seejärel kuvatakse ekraan "Teie uus wallet on elus!", mis kinnitab, et wallet on kasutusvalmis. Klõpsake **"GO TO WALLET "**, et pääseda põhiliidesesse.



Kui olete oma wallet-sse jõudnud, viiakse teid Arkade'i põhiliidesesse. Siit leiate oma saldo, nupud raha saatmiseks ja vastuvõtmiseks ning vahekaardi "Apps", mis annab juurdepääsu integreeritud rakendustele, nagu Boltz (Lightning exchange), LendaSat ja LendaSwap (laenutusteenused) ning Fuji Money (sünteetilised varad).



![wallet interface](assets/fr/04.webp)



### Ühendus ASP-ga


Vaikimisi on portfell automaatselt konfigureeritud ühenduma ametliku Arkade Labs ASP-ga. Saate kontrollida, millise serveriga olete ühendatud, minnes **Settings** > **About**, kus näete serveri aadressi (praegu `https://arkade.computer`).



Arkade praeguses versioonis (Beta) ei ole võimalik ASP-serverit käsitsi muuta. Rakendus ühendub automaatselt ametliku Arkade Labs ASP-ga. Tulevikus on kasutajatel võimalik valida erinevate ASP-de vahel vastavalt oma eelistustele, kuid see funktsioon ei ole veel saadaval.



### Privaatvõtme varundamine


**Arkade kasutab varundus- ja taastamismeetodina Nostr (nsec) formaadis privaatvõtit. Privaatvõtme varundamiseks :





- Minge põhiekraanilt **Settings**.
- Valige **"Varundamine ja privaatsus "**.
- Näete oma **privaatvõtit**, mis kuvatakse formaadis `nsec...`. See pikk tähemärkide jada on teie ainus vahend wallet taastamiseks.
- Vajutage **"COPY NSEC TO CLIPBOARD "**, et kopeerida oma privaatne võti.
- Hoidke seda võtit turvalises kohas**: kirjutage see paberile, hoidke seda turvalises paroolihalduris või kasutage mõnda muud teile sobivat varundusmeetodit.
- Arkade pakub ka valikut **"Enable Nostr backups "**. See funktsioon kasutab Nostr-protokolli (detsentraliseeritud võrk), et automaatselt varundada teatud andmeid teie wallet-st krüpteeritud kujul Nostr-redelitesse. See hõlbustab sünkroniseerimist mitme seadme vahel ja pakub lihtsamat taastamist teie wallet olekust.



**Tähtis**: Nostr varukoopiad on ainult **komfortne** funktsioon. Need ei asenda teie nsec-võtme varukoopiaid. Nostr-varundused ei taga andmete püsivat säilitamist. Teie nsec privaatne võti jääb teie ainukeseks garanteeritud vahendiks oma vahendite taastamiseks.



![backup private key](assets/fr/05.webp)




## Arkade kasutamine



Kui olete oma wallet seadistanud, olete valmis uurima Arkade'i võimalusi. Kasutajaliides on loodud nii, et see ühendab sujuvalt Bitcoin eri tüüpi makseid (On-chain, Lightning, Ark).



### Raha saamine



Oma portfelli rahastamiseks vajutage **"Saada "**. Arkade pakub kolme vastuvõtumeetodit:





- Argi makse**: Kui saatja kasutab samuti Arkade'i, jagage oma Ark-aadressi, et teha kohene, konfidentsiaalne ja praktiliselt tasuta ülekanne.
- Hoiustamine (pardaleminek)**: Kasutage Bitcoin aadressi (`bc1p...`), et võtta vastu klassikaline wallet või vahetus. Enne raha konverteerimist VTXOdeks tuleb oodata kinnitust (~10 min).
- Välgivahetus**: Looge Lightning-arve ja tasuge see välise wallet Lightningiga. Raha saabub koheselt automaatse vahetuse kaudu.



![receive amount](assets/fr/06.webp)



Kviitungi ekraanil kuvatakse kõik olemasolevad valikud: QR-kood, Ark-aadress, Bitcoin (BIP21) aadress ja Lightning-arve. Lightning-maksete puhul hoidke rakendus tehingu ajal avatud.



![receive confirmation](assets/fr/07.webp)



### Raha saatmine



Raha saatmiseks vajutage **"Saada "** ja sisestage saaja aadress või skannige QR-kood. Arkade tuvastab automaatselt, millist tüüpi makse on vaja:





- Ark** makse: Arka-aadressile on ülekanne kohene, privaatne ja praktiliselt tasuta (0 SATS-tasu). Saaja ei pea olema võrgus.
- Välk** makse: Skaneerige Lightning-arve (`lnbc...`) ja Arkade teeb automaatselt vahetuse. ASP maksab arve teie eest ja debiteerib teie Arkade'i saldot.
- Maksmine ahelas**: Või `bc1p...`), Arkade algatab "Koostööväljundi", mis lisatakse järgmisesse on-chain vooru.



Kontrollige üksikasju ekraanil "Tehingu allkirjastamine", seejärel kinnitage **"TAP TO SIGN "**.



![send payment](assets/fr/08.webp)



**Toimivuspiirang (beeta)**: VTXO-d, mis on loodud vähem kui 24 tundi tagasi, ei saa kasutada on-chain väljundite jaoks. Kui teil tekib viga, oodake, kuni teie VTXOd on "küpsed".



**on-chain väljundi konfidentsiaalsus**: Allpool toodud näide näitab [Ark väljunditehingut mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Me jälgime jaotatud sisendit 4 erinevasse väljundisse, nagu CoinJoin. Välise vaatleja jaoks on võimatu kindlaks teha, milline summa millisele kasutajale kuulub.



![transaction ark mempool](assets/fr/11.webp)



## Täiustatud funktsioonid



### VTXO aegumise haldamine


Ark-protokolli tehniline omadus on see, et VTXOde eluiga on **piiratud**. See ajapiirang on omane protokolli ülesehitusele. Aegumistähtaeg on iga ASP-serveri poolt konfigureeritav; Arkade Labs'i ametlikul ASP-l on see ajavahemik umbes **4 nädalat (≈30 päeva)**.



**See piirang võimaldab Ark serveril tõhusalt hallata likviidsust ja puhastada mitteaktiivsete kasutajate VTXO-d. Pärast aegumist saab Ark server tehniliselt nõuda VTXO-puus allesjäänud vahendeid.



**VTXOde aktiivsena hoidmiseks tuleb neid "värskendada" enne nende kehtivuse lõppemist. Värskendamine seisneb uues "voorus" osalemises, kus teie VTXO-d vahetatakse uue täieliku kehtivusajaga (≈30 päeva Arkade Labs ASP-l) uute VTXO-de vastu.



Arkade portfell haldab seda protsessi automaatselt: rakendus jälgib pidevalt teie VTXOde staatust ja värskendab neid automaatselt paar päeva enne nende aegumist. Kui avate rakenduse regulaarselt (vähemalt kord nädalas), hoitakse teie VTXO-d automaatselt aktiivsed.



**Kui te ei ava oma portfelli kauem kui 4 nädalat, aeguvad teie VTXO-d. Kuid te ei kaota oma vahendeid: teil on võimalus neid tagasi saada **ükspoolse väljumise** kaudu (vt järgmine lõik). See menetlus on kulukam ja aeglasem, kuid see tagab, et teie vahendid on endiselt taastatavad.



Vajadus avada rakendus regulaarselt teeb Arkade'ist **"Hot Wallet"**, mis on mõeldud igapäevaseks kulutamiseks, mitte pikaajalise säästmise jaoks. Bitcoinide säilitamiseks ilma neid pikemaajaliselt kasutamata eelistage külma wallet riistvara.



**Kontrollige oma VTXOde staatust**: VTXOde olekut saate jälgida jaotises **Settings** > **Advanced** (Seadistused** > **täiustatud**). Vaadake "Järgmine uuendamine", et näha, millal toimub järgmine automaatne uuendamine, ja "Virtuaalsed mündid", et näha kõigi oma VTXOde üksikasjalikku nimekirja koos nende kehtivusaja lõppemisega.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (ühepoolne lahkumine)



Ühepoolne väljumine on Ark-protokolli **põhiline krüptograafiline garantii**, mis tagab, et saate oma raha tagasi, isegi kui ASP kaob, tsenseerib teie tehinguid või keeldub koostööst. Tehniliselt on teie VTXOd **eelsignitud Bitcoin tehingud**, mis kuuluvad teile. Absoluutses hädaolukorras saate neid tehinguid Bitcoin plokiahelas edastada, et oma raha ilma kellegi loata tagasi saada.



**Kuidas see toimib? Protsess toimub kahes etapis. Esimene, **Trükkimine**: te edastate järjestikku eelallkirjastatud tehingud, mis moodustavad teie VTXOd tehingupuus. Seejärel **Finaliseerimine**: kui ajamäärad on lõppenud (tavaliselt 24 tundi), kogute oma bitcoinid standardaadressilt.



**Täielik staatus Arkade'is**: Hetkel ei ole veel nuppu ega lihtsat kasutajaliidest ühepoolse väljundi jaoks. See funktsionaalsus nõuab praegu Arkade SDK kasutamist ja TypeScript programmeerimise tehnilisi teadmisi.



**Kaasa kui menetlus ei ole nupuvajutusega kättesaadav, on krüptograafiline garantii olemas. Teie VTXOd sisaldavad eelnevalt allkirjastatud tehinguid, mis kuuluvad seaduslikult teile. Just see tehniline garantii teeb Arkist **mittekaitstava** protokolli: isegi halvima stsenaariumi korral jäävad teie vahendid tehniliselt taastatavaks. Arkade tulevastes versioonides lisatakse tõenäoliselt lihtsustatud kasutajaliides.



## Eelised ja piirangud



Et panna Arkade õigesse konteksti, võtame kokku selle praegused tugevused ja nõrkused.



### Tähtsündmused




- Kasutajakogemus (UX)**: Ei kanalihaldust, sissetulevat võimsust ega keerulisi kanali varundusi nagu Lightningiga. Lihtsalt paigaldage ja kasutage.
- Privaatsus** : Vaikimisi CoinJoin arhitektuur pakub palju kõrgemat anonüümsuse taset kui standard on-chain või Lightning tehingud.
- Koostalitlusvõime**: Makske mis tahes Bitcoin QR-koodiga (On-chain või Lightning) ühest liidesest.



### Piirangud




- Noor protokoll**: Ark on väga uus tehnoloogia. Võib esineda vigu. Soovitatav on mitte kasutada Ark'i selliste summade salvestamiseks, mille kadumine oleks kriitiline.
- ASP-sõltuvus**: Kuigi süsteem ei ole sõltuv, sõltub selle voolavus ASP kättesaadavusest. Kui kõrvalsüsteem ei ole kättesaadav, ei saa te enam koheselt tehinguid teha (ainult väljastada oma on-chain vahendeid).
- Ainult Hot Wallet** : Vajadus avada rakendus regulaarselt VTXOde värskendamiseks ei sobi külma ladustamise puhul (Cold Storage).



## Võrdlus: Arkade vs Lightning vs Cashu



Et paremini mõista Arkade'i positsiooni, võrdleme seda kahe teise suurema skaleeritavuslahendusega.




| Kriteerium | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Mudel** | Serveri (ASP) poolt koordineeritud jagatud UTXO | Maksekanalite P2P-võrk | Panga (Mint) väljastatud pimemärgid |
| **Haldus** | **Mitte-halduslik** (võtmed on teil) | **Mitte-halduslik** (võtmed on teil) | **Halduslik** (vahendid on Mindi käes) |
| **Privaatsus** | **Kõrge** (Natiivne CoinJoin, avalikkusele pime) | **Keskmine** (Sibulruutimine, kuid kanalid nähtavad) | **Väga kõrge** (Pime isegi Mindi jaoks) |
| **Skaleeritavus** | Suurepärane (Massiivne on-chain batching) | Suurepärane (Lõputud off-chain tehingud) | Suurepärane (Lihtsad serveriallkirjad) |
| **Kogemus** | Lihtne (lähedane on-chain rahakotile) | Keeruline (kanalite haldus, likviidsus) | Väga lihtne (nagu digitaalne sularaha) |
| **Peamine risk** | ASP kättesaadavus ja aegumine | Kanalite haldus ja varukoopiad | Usaldus Mindi vastu (varguse oht) |

**Arkade** on ideaalne kompromiss: Cashu lihtsus ja konfidentsiaalsus, kuid Lightning'i suveräänsus (mittehooldus).



## Toetus ja abi



Kui teil tekib Arkade'i kasutamisel probleeme või küsimusi, pakub rakendus mitmeid tugivõimalusi:





- Minge **Settings** > **Support**.
- Leiad mitu võimalust:
  - Klienditugi**: Saage abi oma portfelliga, teatage vigadest või esitage küsimusi.
  - Turvaline vestlus**: Teie vestlused on turvalised ja privaatsed, kusjuures ajalugu säilib ka seansside vahel.
  - Veateated**: Teatage kõikidest tekkinud probleemidest, sealhulgas nende reprodutseerimise sammud.
  - Jälgige edusamme**: Jälgige kogu aeg oma tugipiletite ja vestluste kulgu.



![support](assets/fr/10.webp)



Arkade meeskond on aktiivne ka Telegramis @arkade_os kanali kaudu, et pakkuda tuge ja integratsioonivõimalusi.



## Oluline märkus: rakendus on beeta-staadiumis



**⚠️ Arkade on praegu mainnet Bitcoin** avalikus beetasüsteemis. Kuigi rakendus töötab reaalsete bitcoinidega, on oluline rakendada teatud ettevaatusabinõusid.



### Soovitused kasutamiseks




- Kasutage väikeseid koguseid**: Vältige suurte summade salvestamist Arkade'ile. Kasutage seda wallet oma igapäevaste kulutuste jaoks ja hoidke oma säästud külmas wallet riistvaras.
- Võimalikud vead ja piirangud**: Arkade võib esineda vigu või ootamatut käitumist, nagu iga aktiivses arenduses oleva rakenduse puhul. Teatage kõigist probleemidest integreeritud toe kaudu.
- Kiire areng** : Rakendust ja protokolli täiustatakse pidevalt. Mõned funktsioonid võivad muutuda või lisanduda tulevastes versioonides.



### Praegused teadaolevad piirangud




- 24-tunnine viivitus VTXOs** : Äsja loodud VTXOsid ei saa kohe kasutada on-chain väljundite jaoks.
- ASP unikaalne**: ASP-serveri muutmine rakenduses ei ole veel võimalik.
- Tehniline ühepoolne väljund**: Lihtsustatud liides ühepoolse väljundi jaoks veel puudub (nõuab SDK-d).



Arkade Labsi meeskond töötab aktiivselt selle nimel, et neid piiranguid tulevastes versioonides leevendada.



## Kokkuvõte



ArkadeOS kujutab endast suurt läbimurret Bitcoin ökosüsteemis. Rakendades Ark-protokolli, tõestab see, et on võimalik ühildada kasutamise lihtsus Bitcoin aluspõhimõtetega: ära usalda, kontrolli.



Kuigi Arkade on veel lapsekingades, pakub see põnevat pilguheitu sellest, milline võiks olla Bitcoin maksete tulevik: kohene, privaatne ja kõigile ligipääsetav ilma tehniliste eeldusteta. See on ideaalne vahend teie igapäevaste kulutuste jaoks, täiendades teie turvalist säästulahendust (Cold Wallet).



Soovitame teil katsetada Arkade'i väikeste kogustega, et seda uut protokolli enda jaoks avastada. Ökosüsteem areneb kiiresti ja Arkade on selle innovatsiooni esirinnas.



## Ressursid



Lisateavet leiate ametlikest allikatest:





- Arkade** veebisait: [arkadeos.com](https://arkadeos.com)
- Dokumentatsioon**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Ark** protokoll: [ark-protocol.org](https://ark-protocol.org)
- Allikakood** : [GitHub Arkade](https://github.com/arkade-os)