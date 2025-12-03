---
name: Dana Wallet
description: Minimalistlik portfell vaikivate maksete jaoks (BIP-352)
---

![cover](assets/cover.webp)



Bitcoin aadresside korduvkasutamine on üks otsesemaid ohte kasutajate konfidentsiaalsusele. Kui saaja kasutab ühte aadressi mitme makse vastuvõtmiseks, võib iga vaatleja jälgida kõiki sellega seotud tehinguid ja rekonstrueerida nende finantsajalugu. See probleem mõjutab eelkõige sisuloojaid, heategevusorganisatsioone või aktiviste, kes soovivad avalikult näidata annetusaadressi, ilma et nende või nende annetajate privaatsus oleks ohus.



Dana Wallet vastab sellele probleemile elegantse lahendusega: Silent Payments. See minimalistlik, avatud lähtekoodiga wallet, mis käivitati 2024. aastal, genereerib korduvkasutatava staatilise aadressi, tagades samal ajal, et iga saadud makse jõuab eraldi aadressile plokiahelas. Saatja ei vaja eelnevat suhtlemist saajaga ja ükski väline vaatleja ei saa üksikuid tehinguid omavahel siduda. Plokiahelas näevad need maksed välja nagu täiesti tavalised Taproot tehingud.



Dana Wallet on saadaval Mainnet ja Signet, kuid arendajad peavad seda endiselt eksperimentaalseks ja soovitavad mitte paigutada raha, mida te ei ole valmis kaotama. Selles õpetuses kasutame Signeti versiooni, et avastada Silent Payments ilma reaalsete rahaliste vahenditega riskimata.



## Mis on Dana Wallet?



### Filosoofia ja eesmärgid



Dana Wallet võtab kasutusele "SP-first" lähenemisviisi: wallet genereerib ainult vaikimisi makseid ja aktsepteerib ainult seda tüüpi makseid. Selle rakendusega ei saa luua klassikalist Bitcoin aadressi (pärand, SegWit või Taproot standard). See tahtlik piirang võimaldab teil täielikult keskenduda BIP-352 protokolli õppimisele, ilma et muud funktsioonid teid häiriksid. Lihtsustatud kasutajaliides eelistab tahtlikult kasutusmugavust valikute rohkuse asemel, muutes tööriista kättesaadavaks isegi on-chain konfidentsiaalsuse kontseptsioonidega mitte kursis olevatele kasutajatele.



Projekt on täielikult avatud lähtekoodiga ning selle mobiililiidese jaoks on kasutatud Flutterit ja sisemise krüptograafilise loogika jaoks Rust. Selline arhitektuur ühendab endas sujuvat kasutajakogemust ja optimaalset jõudlust intensiivsete skaneerimistoimingute jaoks.



### Kuidas toimivad vaikivad maksed?



Vaiksed maksed (BIP-352) põhinevad keerukal krüptograafilisel mehhanismil, mis kasutab Elliptic Curve Diffie-Hellmani võtit Exchange (ECDH). Saaja genereerib staatilise aadressi (algusega `sp1...` mainnet puhul või `tsp1...` Signet'is), mis koosneb kahest erinevast avalikust võtmest: skaneerimisvõti ($B_{scan}$) sissetulevate maksete tuvastamiseks ja kulutamisvõti ($B_{spend}$) saadud vahendite kulutamiseks. Selline eraldamine võimaldab hoida kulutamisvõtit wallet riistvaras, samal ajal kui skaneerimisvõtit kasutatakse ühendatud seadmes.



Kui saatja soovib teha makse, kombineerib tema wallet oma sisendite privaatvõtmete summa vastuvõtja avaliku skaneerimisvõtmega, et arvutada jagatud ECDH-saladus. See saladus genereerib krüptograafilise "tweak'i", mis lisatakse saaja kulutuste võtmele ja loob selle tehingu jaoks unikaalse Taproot aadressi.



Vastuvõtja saab seda arvutust reprodutseerida, kasutades oma privaatset skaneerimisvõtit ja tehingus nähtavaid avalikke võtmeid (Diffie-Hellmani matemaatiline omadus). See võimaldab tal tuvastada ja kulutada raha ilma eelneva suhtluseta saatjaga.



Selline lähenemisviis pakub mitmeid eeliseid:




- Saaja konfidentsiaalsus**: iga makse jõuab erinevale aadressile
- Saatja konfidentsiaalsus**: makseid ühendava püsiva tunnuse puudumine
- Ei ole kolmanda osapoole serverit**: protokoll toimib autonoomselt
- Eristamatud tehingud**: Vaikivad maksed näevad välja nagu tavalised Taproot tehingud



Peamine puudus on skaneerimiskulud: vastuvõtja peab analüüsima iga uut Taproot tehingut, et tuvastada talle mõeldud tehingud.



Kui soovite rohkem teada saada vaikivate maksete tehnilisest toimimisest, siis soovitame BTC204 kursust Bitcoin konfidentsiaalsuse kohta, mis sisaldab vaikivatele maksetele pühendatud peatükki:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Toetatud platvormid



Dana Wallet on saadaval Androidi rakendusena. APK-d saab alla laadida arendajate poolt pakutava F-Droidi repositooriumi kaudu, Obtainiumi kaudu või otse GitHubist. Linuxi kasutajatele on tehniliselt võimalik Flutteri rakendus töölauale kompileerida.



Rakendus ei ole saadaval iOS-is ega ametlikes poodides (Google Play, App Store), mis peegeldab selle eksperimentaalset staatust ja keskendumist tehnilisele sihtrühmale.



## Paigaldamine



### Olulised eeldused



Dana Wallet installimiseks Androidile on vaja Androidi seadet, mille turvasätetes on lubatud valik "Tundmatud allikad". Kontot või registreerimist ei ole vaja.



### Lisa F-Cold tagatisraha



Soovitatav meetod on lisada Dana Wallet spetsiaalne F-Droid repositoorium. Mine aadressile `fdroid.silentpayments.dev`, kust leiad repositooriumi lingi ja QR-koodi skaneerimiseks. Repositooriumis on praegu 3 rakendust: Mainnet versioon, Development ja Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Paigaldamine F-Droidi kaudu



Avage oma Android-seadmes rakendus F-Droid, seejärel avage paremal allosas asuva ikooni kaudu seaded. Rakenduse allikate haldamiseks valige "Repositooriumid". Uue repositooriumi lisamiseks vajutage nuppu "+", seejärel skannige QR-koodi või kleepige link "https://fdroid.silentpayments.dev/fdroid/repo". Kui repositoorium on lisatud, näete Dana Wallet kolme versiooni, mis on saadaval. Valige "Dana Wallet - Bookmark" ja vajutage "Install".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Esialgne konfiguratsioon



### Portfelli loomine



Esmakordsel käivitamisel kuvab Dana Wallet tervitusekraani, mis tutvustab tema missiooni: "Saada ja saada annetusi ilma vahendajateta". Jätkamiseks vajutage nuppu "Alusta". Järgmisel ekraanil esitatakse rakenduse kolm peamist eelist:




- Mugavad annetused**: alustage annetuste vastuvõtmist mõne sekundiga
- Privaatsus vaikimisi**: ei ole vaja servereid ega keerulist infrastruktuuri
- E-posti sarnane kogemus**: bitcoinide saatmine ja vastuvõtmine on sama lihtne kui e-kiri



Olemasoleva portfelli taastamiseks saate valida "Restore" või uue portfelli loomiseks "Create new wallet". Vajutage "Create new wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Seejärel genereerib rakendus taastamislause, mille peaksite hoolikalt üles märkima füüsilisel andmekandjal. Võtke kasutusele head varundustavad isegi reaalset väärtust mitteomavate testvahendite puhul.



### Interface ja parameetrid



Kui portfoolio on loodud, jõuate põhiliidesesse, mis on jagatud kaheks vahekaardiks: "Transact" ja "Settings".



Vahekaardil **Tehingud** kuvatakse teie bitcoinide saldo (ja selle konverteerimine dollariteks), hiljutiste tehingute nimekiri ja kaks tegevusnuppu: "Maksa" raha saatmiseks ja vastuvõtunupp (allalaadimise ikoon).



Vahekaardil **Settings** on neli võimalust:




- Näita seed fraasi**: kuvab teie taastamise fraasi turvaliseks säilitamiseks
- Fiat-valuuta muutmine**: näidisvaluuta muutmine (vaikimisi USD)
- Set backend url**: Blindbiti serveri URL-i konfigureerimine (vt järgmine lõik)
- Wipe wallet**: pühib wallet täielikult seadmest



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Blindbit server



Dana Wallet kasutab vaikivate maksete tuvastamiseks indekseerimisserverit nimega **Blindbit**. Selle toimimise mõistmine on oluline rakenduse usaldusmudeli hindamiseks.



**Miks on meil vaja serverit?



Vaikiva makse tuvastamiseks peab teie wallet teoreetiliselt skaneerima kõiki Taproot tehinguid igas plokis ja tegema iga tehingu kohta krüptograafilise arvutuse (ECDH). Mobiiltelefonis oleks see operatsioon liiga arvutuslik ja ribalaiust nõudev.



Blindbit server lahendab selle probleemi, arvutades eelnevalt vahepealsed andmed (mida nimetatakse "tweaks") kõigi Taproot tehingute jaoks. Seejärel laeb teie wallet need tweakid (33 baiti tehingu kohta) alla ja teostab lõpliku arvutuse **lokaalselt**, et kontrollida, kas makse kuulub teile.



**Valvatud konfidentsiaalsus**



Erinevalt tavalisest Electrum serverist, kus te avaldate oma aadressid, ei tea Blindbit server, millised maksed teile kuuluvad. Ta esitab kõigile kasutajatele samad andmed ja lõpliku kontrolli teostab teie telefon. Seega säilib teie konfidentsiaalsus serveri suhtes.



**Vaikimisi server



Dana Wallet kasutab avalikku serverit `silentpayments.dev/blindbit/signet` (Signeti puhul) või `silentpayments.dev/blindbit/mainnet` (Mainnet puhul). Seda URL-aadressi saate seadetes muuta, kui majutate oma serverit.



**Host oma Blindbit server**



Kasutajatele, kes soovivad täielikku sõltumatust, on võimalik majutada oma Blindbit Oracle'i serverit. Selleks on vaja :




- Täielik Bitcoin tuumasõlm **mittekõrvaline** (mitte-pruned)
- Blindbit Oracle'i paigaldamine (saadaval GitHubis: `setavenger/blindbit-oracle`)
- Umbes 10 GB täiendavat kettaruumi
- Tehnilised oskused (Go koostamine, serveri konfigureerimine)



Umbreli või Start9 jaoks ei ole veel ühtegi pakendatud rakendust saadaval. Paigaldamine jääb esialgu manuaalseks. See valdkond on aktiivses arengus ja tulevikus võivad tekkida kättesaadavamad lahendused.



## Igapäevane kasutamine



### Raha saamine



Bitcoinide vastuvõtmiseks vajutage põhiekraanil nuppu vastuvõtmine (allalaadimise ikoon). Dana Wallet kuvab seejärel Bookmarkil teie täieliku Silent Payment aadressi formaadis `tsp1q...`. Kasutajaliides pakub mitmeid võimalusi:




- Näita QR-koodi**: kuvab oma aadressi QR-koodi lihtsaks skaneerimiseks
- Jaga**: aadressi jagamine telefoni rakenduste kaudu
- Copy**: kopeerib aadressi lõikelauale



Nagu ekraanil näidatud, saate seda aadressi avalikult jagada oma suhtlusvõrgustikes, ilma et see kahjustaks teie privaatsust.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Esimeste testvahendite saamiseks Signetist kasutage spetsiaalset Silent Payments'i kraanikaussi, mis on kättesaadav aadressil `silentpayments.dev/faucet/signet`. Kopeerige oma aadress `tsp1...`, kleepige see faucet'i väljale ja kinnitage taotlus. Oodake ploki kaevandamist (umbes 10 minutit Signetil).



### Saada makse



Raha saatmiseks vajutage põhiekraanil nuppu "Maksa". Ilmub ekraan "Vali saaja(d)", kus on kolm võimalust saaja määramiseks:




- Makseteabe käsitsi sisestamine
- Paste from clipboard**: aadressi kleepimine lõikelauast
- Skaneeri QR-kood**: skaneeri aadressi sisaldav QR-kood



Kui saaja aadress on kinnitatud, saate ekraanil "Sisestage summa" sisestada saadetava summa satoshides. Teie olemasolev saldo kuvatakse võrdluseks. Jätkamiseks vajutage nuppu "Edasi tasu valimiseks".



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Järgmisel ekraanil kuvatakse kolm tasandit, sõltuvalt nõutavast kiireloomulisusest:




- Kiire** (10-30 minutit): kiire kinnituse eest makstakse kõrgemat tasu
- Normaalne** (30-60 minutit): mõõdukad kulud
- Aeglane** (1+ tund): miinimumtasu mitte-kiireloomuliste tehingute eest



Pärast tasu taseme valimist esitatakse kinnitusekraanil "Valmis saatmiseks?" kokkuvõte kõigist üksikasjadest: sihtkoha aadress, summa, hinnanguline aeg ja tehingutasu. Kontrollige seda teavet hoolikalt, seejärel vajutage tehingu saatmiseks nuppu "Saada".



Pärast saatmist ilmub tehing teie ajaloos olekuga "Kinnitamata", kuni see lisatakse blokki. Teie saldot ajakohastatakse vastavalt.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Eelised ja piirangud



### Tähtsündmused





- Pedagoogiline**: lihtsustatud kasutajaliides, mis keskendub õppimisele Vaiksed maksed
- Kahesuunaline**: toetab nii saatmist kui ka vastuvõtmist, erinevalt teistest portfellidest
- Avatud lähtekood**: täielikult auditeeritav kood GitHubis
- Spetsiaalne Faucet**: lihtsustab testide rahastamise saamist
- Ilma kontota**: ei nõuta registreerimist ega isikuandmeid



### Piirangud, millega tuleb arvestada





- Eksperimentaalne**: auditeerimata tarkvara, Mainnet puhul kasutada ettevaatlikult
- Piiratud platvorm**: peamiselt Android, iOS-versioon puudub
- Vähendatud funktsionaalsus**: puudub mündikontroll, puuduvad allkontod, puudub Lightning
- Intensiivne skaneerimine**: maksete tuvastamine kulutab märkimisväärseid ressursse



## Parimad tavad



### seed ohutus



Isegi väärtusetu taustaga Signeti testide puhul suhtuge oma taastamislausesse tõsiselt. Kasutage seadetes valikut "Näita seed fraasi", et kirjutada see hoolikalt üles. Hea tava kohaselt säilitage Signeti ja Mainnet jaoks täiesti eraldi rahakotid: ärge kunagi kasutage seed, mis on loodud testimiseks, wallet-l, mis on mõeldud reaalsete vahendite vastuvõtmiseks.



### Hoiatus eksperimentaalse staatuse kohta



Dana Wallet arendajad peavad seda endiselt eksperimentaalseks. Nagu nad selgelt väidavad: "Ärge kasutage vahendeid, mida te ei taha kaotada". Õppimise eesmärgil valige Signet versioon. Kui kasutate Mainnet versiooni, piirduge token summadega.



### Varundamine ja taastamine



Silent Payments'i fondi tagasinõudmiseks on vaja wallet, mis ühildub BIP-352 protokolliga. Tavaline wallet ei saa plokiahelat skaneerida, et taastada teie UTXO Silent Payments. Hoidke Dana Wallet paigaldatud või kasutage olemasoleva wallet taastamiseks esimesel käivitamisel valikut "Restore".



## Võrdlus BIP-47 ja PayJoinga



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Vaikne makse kaotab BIP-47 teatamistehingu kallima skaneerimise hinnaga. PayJoin lahendab teistsuguse probleemi (sisendkorrelatsioon) ja seda saab kombineerida vaikivate maksetega.



## Kokkuvõte



Dana Wallet on väärtuslik õppevahend, mille abil saab õppida vaikseid makseid riskivabas keskkonnas. Selle minimalistlik lähenemine võimaldab teil mõista BIP-352 protokolli põhilisi mehhanisme, ilma et teid häiriksid kõrvalised funktsioonid. Signetiga eksperimenteerides saavutate praktilise arusaama sellest paljutõotavast tehnoloogiast Bitcoin tehingu konfidentsiaalsuse tagamiseks.



Vaikne makse on oluline samm edasi kasutusmugavuse ja eraelu puutumatuse austamise ühitamisel. Kogukonna entusiasm ja esimesed integratsioonid erinevatesse rahakottidesse (Cake Wallet, BitBox02, BlueWallet saatmiseks) viitavad tulevikule, kus annetusaadressi avaldamine ei ohusta enam omaniku finantsprivaatsust.



## Ressursid



### Ametlikud dokumendid




- Dana Wallet GitHubi repositoorium: https://github.com/cygnet3/danawallet
- F-Cold tagatisraha: https://fdroid.silentpayments.dev
- Vaikiv maksekeskkonna sait: https://silentpayments.xyz
- Spetsifikatsioon BIP-352: https://bips.dev/352



### Signet testimisvahendid




- Faucet Vaiksed maksed: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Blindbit server (isehostitav)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle