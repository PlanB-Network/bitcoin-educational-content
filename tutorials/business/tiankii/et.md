---
name: Tiankii
description: Lightning tööriistade pakett jaemüüjatele ja tarbijatele
---

![cover](assets/cover.webp)



Bitcoin ökosüsteemis on maksete vastuvõtmine reaalajas endiselt suur väljakutse ettevõtete ja üksikisikute jaoks. Traditsioonilised lahendused nõuavad sageli kõrgetasemelisi tehnilisi teadmisi, keerukat infrastruktuuri, mida tuleb hooldada, või nõuavad, et raha oleks vahendajate käes. Selline olukord takistab Bitcoin massilist kasutuselevõttu igapäevase valuutana, vaatamata Lightning Network tehnoloogiliste edusammude lubadusele.



2021. aastal sündinud salvadorlaste ettevõte Tiankii reageerib sellele probleemile, pakkudes ligipääsetavat, modulaarset Bitcoin infrastruktuuri. Selle asemel, et sundida vastu võtma suletud ökosüsteemi, pakub Tiankii omavahel ühendatud vahendite paketti, mis võimaldab igaühel integreerida Bitcoin Lightning oma ettevõttesse, ohverdamata seejuures kontrolli oma vahendite üle.



## Mis on Tiankii?



### Päritolu ja filosoofia



Tiankii, mis tähendab Nahuatl keeles "kõigile ligipääsetav vabaõhuturg", on El Salvadori esimene 100% Bitcoin start-up. Ettevõtte asutas Darvin Otero pärast seda, kui Bitcoin võeti vastu riigi seaduslikuks maksevahendiks, ning selle eesmärk on muuta Bitcoin väärtuse säilitamisest igapäevaste ostude tegemiseks kasutatavaks valuutaks. Erinevalt hoiuplatvormidest kasutab Tiankii mittekaitstavat lähenemisviisi, mille puhul kasutajad säilitavad kontrolli oma vahendite üle, kusjuures infrastruktuur toimib ainult tehnilise vahendajana.



### Tehniline arhitektuur



Tiankii on positsioneeritud Bitcoin-as-a-Service infrastruktuuri pakkujana, mis põhineb Lightning Network-l. See teise kihi tehnoloogia võimaldab peaaegu koheseid tehinguid tühiste kuludega, mis teeb võimalikuks mikromaksed ja igapäevased ostud.



Arhitektuur põhineb kolmel sambal:



**Välk esmakordselt**: Süsteemselt eelistada Lightning-võrku selle kiiruse ja madalamate kulude tõttu, säilitades samal ajal on-chain tehingutoetuse suurte summade puhul.



**Avatud standardid**: LNURLi kasutamine maksetaotluste automatiseerimiseks, Lightning Address loetavate e-kirjade ID-de jaoks ja Bolt Card koostalitlusvõimeliste NFC-maksete jaoks.



**wallet-agnostiline modulaarsus**: Võimalus ühendada erinevaid Lightning portfelle (LNbits, Blink, BlueWallet) või oma sõlme, pakkudes maksimaalset paindlikkust sõltuvalt nõutavast oskusteabe ja autonoomia tasemest.



## Tiankii ökosüsteemi tööriistad



### Bitcoin POS - kauplusesisene makseterminal



Rakendus muudab nutitelefoni või tahvelarvuti Lightning-terminaliks. Kaupmees sisestab summa kohalikus vääringus ja rakendus genereerib Lightning QR-koodi või aktsepteerib Bolt kaarti. Tehingud krediteeritakse koheselt ilma komisjonitasuta, automaatne konverteerimine enam kui 150 valuutas, jootraha haldamine ja müügiajalugu.



### Kaupmehe armatuurlaud - ühtne müügijuhtimine



Interface veebi tsentraliseeritud, et ühendada oma wallet Lightning, jälgida tehinguid reaalajas, väljastada arveid ja generate raamatupidamisaruandeid. Platvorm koondab kõik kanalid: kaupluses tehtavad maksed (POS), online-müük (e-kaubanduse pistikprogrammid) või API integratsioonid. Maksed koonduvad valitud wallet-le.



### Bitcoin kontaktivaba kaart (Bolt kaart)



NFC Bolt kaart on Tiankii peamine uuendus Bitcoin demokratiseerimisel üldsuse jaoks. See toimib nagu kontaktivaba pangakaart ja võimaldab teil Bitcoin Lightning'i ostude eest tasuda lihtsalt ühilduvale terminalile koputades.



Erinevalt traditsioonilistest hoiustamislahendustest järgib see kaart avatud standardit, mis tagab koostalitlusvõime. Kasutajad saavad seda IBI rakenduse kaudu siduda oma wallet-ga, säilitades seega oma isiklikud võtmed ja täieliku kontrolli seotud vahendite üle. Maksmine võtab aega vaid ühe sekundi, ilma et oleks vaja võtta välja nutitelefoni või omada makse ajal aktiivset internetiühendust.



See lahendus on eriti kaasav inimestele, kes ei ole nutitelefonidega tuttavad, pakkudes ligipääsetavat juurdepääsu Bitcoin majandusele.



### IBI rakendus - Interface individuaalne Bitcoin



IBI rakendus (individuaalne Bitcoin Interface) on mõeldud üksikisikutele, kes soovivad kasutada Bitcoin Lightning'i igapäevaselt. Selle peamine eelis seisneb personaalse Address Lightning'i genereerimises, mis on e-kirjas loetav makse identifikaator (näide: alice@ibi.me).



See tunnus lihtsustab oluliselt maksete vastuvõtmist: iga tehingu jaoks ei ole vaja generate uut arvet koostada, saatja saab lihtsalt sisestada Lightning-aadressi. Kasutajaliides võimaldab teil ka hallata oma Bolt kaarti (aktiveerimine, deaktiveerimine, kululimiidid), ühendada erinevaid Lightning'i rahakotte ja teha makseid QR-koodide skaneerimise teel.



### E-kaubanduse pistikprogrammid



Valmis integratsioonid WooCommerce'ile, Shopify'ile ja Cloudbedsile. Installeeritakse minutitega, et lisada Bitcoin Lightning kassasse. Eelised: null komisjonitasu (vs. 2-3% krediitkaardid), kohene arveldamine, ülemaailmne juurdepääs, tagasimaksete kõrvaldamine. Maksed saabuvad otse kaupmehe ühendatud wallet-le.



### Bitcoin API ja arendusvahendid



Tiankii SDK võimaldab integreerida Bitcoin Lightningi olemasolevatesse rakendustesse ilma oma sõlme säilitamata. API tegeleb arvete loomise, maksete kontrollimise ja masspostitamisega Google Cloudis asuva töökindla infrastruktuuri kaudu. Command Center täiendab pakkumist organisatsioonidele Address Lightningiga kohandatud domeenide, massimaksete ning NFC-terminalide ja kaartide tsentraliseeritud haldamise kohta.



## Paigaldamine ja esimesed sammud



### Olulised eeldused



Tiankii kasutamine ei nõua keerulisi tehnilisi eeldusi. Rakendused töötavad nutitelefoni, tahvelarvuti või arvuti veebibrauseri kaudu. Rakenduse installeerimine ei ole vajalik: IBI-le või kaupmehe juhtpaneelile juurdepääsuks on vaja vaid internetiühendust ja värsket brauserit.



**Erikasutajatele (IBI rakendus)**: wallet Lightning ei ole vajalik. Konto loomisel konfigureerib Tiankii automaatselt toimiva Address Lightning'i [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html) kaudu, mis on noodita rakendus, mis kasutab taustal Liquid võrku. Saate kohe makseid vastu võtta ja saata ilma tehnilise konfiguratsioonita. See lahendus lihtsustab tunduvalt juurdepääsu algajatele, jäädes samal ajal isekasutatavaks.



**Müüjatele (kaupmehe armatuurlaud)** : Olemasoleva wallet Lightning'i ühendamine on kohustuslik, et kasutada müügiterminale ja võtta vastu makseid. Tiankii toetab mitmeid lahendusi: mobiilseid rahakotte (Blink, Strike), isehostitud lahendusi (LNbits, LND/CLN node) või veebikassasid (Alby). Üksikasjalikud ühendusjuhendid on saadaval selle õpetuse rubriigis "Ressursid".



### Eraklientidele: IBI App



**Konto loomine



Konto loomiseks minge aadressile accounts.ibi.me. Sellel lehel saate valida kahe kontotüübi vahel: "Isiklik kasutamine" individuaalseks kasutamiseks või "Ärikasutus" äriliseks kasutamiseks. Valige "Isiklik kasutamine", et pääseda ligi Bitcoin maksete vastuvõtmise ja saatmise vahenditele.



![Choix du type de compte](assets/fr/01.webp)



Pärast "Isikliku kasutamise" valimist suunatakse teid registreerimise lõpuleviimiseks automaatselt aadressile go.ibi.me. Seda saab teha e-posti, telefoninumbri või Google'i, Microsofti või Twitteri konto abil. Pärast loomist saate kohe juurdepääsu oma IBI-liidesele, kus teie Lightning Address on juba töökorras.



![Création du compte](assets/fr/02.webp)



**Interface peamine**



IBI kasutajaliides näitab teie saldot satoshides ja kohalikus vääringus (USD). Kolm nuppu võimaldavad teil suhelda: "Receive" maksete vastuvõtmiseks, "Scan" QR-koodi skaneerimiseks ja "Send" satoshide saatmiseks.



![Interface IBI](assets/fr/03.webp)



**Makse saamine**



Satoshide vastuvõtmiseks vajutage "Vastuvõtmine". Rakendus genereerib automaatselt QR-koodi ja kuvab teie isikustatud Address Lightning (nom@ibi.me formaadis). Jagage seda aadressi või QR-koodi saatjaga: raha saabub koheselt teie IBI kontole.



![Réception avec Lightning Address](assets/fr/04.webp)



Kui teie saldo on krediteeritud, saate neid satoshisid kasutada maksete tegemiseks.



**Saatke makse**



Satoshide saatmiseks vajutage nuppu "Saada". Saate kas skannida Lightning QR-koodi või sisestada otse Lightning Address sihtkoha.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Sisestage soovitud summa satoshides, kontrollige samaväärset summat kohalikus vääringus ja kinnitage makse.



![Confirmation du montant](assets/fr/07.webp)



Edukateade kinnitab saadetist koos üksikasjadega: saadetud summa, tehingutasu ja saaja.



![Paiement réussi](assets/fr/08.webp)



**Kontohaldus



Seadetes saate hallata oma Bitcoin NFC-kaarte (Bolt Cards). Kasutajaliides võimaldab teil aktiveerida, deaktiveerida või määrata oma kaartide kasutuspiirangud.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Kaupmeeste jaoks: Kaupmehe armatuurlaud ja POS



**Ürituskonto loomine



Konto loomiseks minge aadressile accounts.ibi.me. Kaupmehe tööriistadele juurdepääsuks valige "Ärikasutus". Seda tüüpi konto avab juurdepääsu kaupmehe juhtpaneelile ja müügiterminalidele.



Pärast "Ärikasutuse" valimist suunatakse teid automaatselt kaupmehe armatuurlauale (pay.tiankii.com). See viib teid ärijuhtimise kasutajaliidesesse, kus on tulude jälgimine, tehingud ja maksevahendid. Maksete vastuvõtmise alustamiseks peate kõigepealt ühendama oma wallet Lightning'i, klõpsates lehe ülaosas olevale lingile (vt pildil olevat noolt).



![Dashboard marchand](assets/fr/11.webp)



**wallet Lightning** ühendus



Oluline samm müügipunkti aktiveerimisel: ühendage wallet Lightning maksete vastuvõtmiseks. Kasutajaliides pakub mitmeid ühendamisvõimalusi. Pange tähele, et mõned valikud (Bitcoin Onchain ja Lightning Network) on veel arendamisel ja kuvatakse kasutajaliideses halliks tõmmatud.



![Options de connexion wallet](assets/fr/12.webp)



Selles õpetuses kasutame Lightning Address ühendust, mis ühildub Chivo, Blink Wallet ja Strike'iga. Sisestage oma Lightning Address (nom@domaine.com formaat), näiteks LN Markets, Alby või mõni muu ühilduv tarnija.



![Saisie de la Lightning Address](assets/fr/13.webp)



Kui olete sisse loginud, on teie konto töökorras. Nüüd saate pääseda kassasse või pöörduda tagasi armatuurlauale, et konfigureerida muid seadeid.



![Connexion réussie](assets/fr/14.webp)



*makse lingid** *Makse lingid



Menüü "Maksetööriistad" annab juurdepääsu menüüle "Maksetaotlus", mis võimaldab teil luua ja hallata makseühendusi. See funktsioon on kasulik isikupärastatud makselinkide loomiseks, mida saadetakse e-kirja või sõnumi teel: annetused, üksikmaksed, mitmemakse või isegi maksumüürid sisu kaitsmiseks. Saate luua eri tüüpi linke, mis sobivad teie ettevõtte vajadustele.



![Liens de paiement](assets/fr/15.webp)



**Müügiterminali konfiguratsioon**



Kaupluses tehtavate maksete vastuvõtmiseks avage menüü "Müügiterminal" jaotisest "Maksetööriistad". Selles jaotises saate luua ja hallata oma müügiterminale (terminalide arv sõltub teie paketist, vt allpool Freemium vs. Business-paketid). Vajutage "Open", et avada POS-liides oma brauseris.



![Gestion des terminaux](assets/fr/16.webp)




**Müügi genereerimine**



Kassaterminalis kuvatakse numbriline klahvistik müügisumma sisestamiseks. Sisestage summa kohalikus vääringus (nt 500 sats vastab 630,74 ARSile) ja vajutage kinnitamiseks "OK".



![Saisie du montant](assets/fr/17.webp)



Rakendus genereerib koheselt Lightning QR-koodi ja Lightning Address maksmiseks. Kliendid saavad skannida QR-koodi oma wallet-ga või kasutada oma Bolt kaarti NFC-terminalis.



![QR code de paiement](assets/fr/18.webp)



Niipea kui makse on laekunud, ilmub kinnitusekraan, kus kuvatakse saadud summa kohalikus vääringus ja satoshides. Saate saata kviitungi e-posti teel, printida pileti või alustada kohe uut müüki.



![Paiement encaissé](assets/fr/19.webp)



**Monitooring ja juhtimine**



Kõik tehingud registreeritakse teie kaupmehe armatuurlaual. Teil on täielik jälgimine tulude kohta perioodide kaupa, müügi koguarv ja üksikasjalik ajalugu teie raamatupidamise jaoks.



Seadete kasutajaliides pakub mitmeid konfiguratsioonivahelehti. Vahekaardil "Üldised seaded" saate hallata oma kaupmehe profiili ja teateid. Vaheleht "Kasutajad" võimaldab teil lisada ja hallata oma meeskonna juurdepääsu kaupmehe juhtpaneelile (mitme kasutaja haldamine vastavalt teie plaanile). Vahekaart "Development Workspace" annab juurdepääsu API võtmetele täiustatud integratsioonide jaoks, samal ajal kui "Subscription" võimaldab teil hallata oma tellimust.



![Paramètres du compte marchand](assets/fr/20.webp)



**Freemium vs Business plaanid



Tiankii pakub kaupmehe armatuurlaua jaoks kaks paketti. **Freemium** pakett (tasuta) sobib alustavatele ettevõtjatele, kellel on järgmised piirangud: üks müügikoht, üks kasutaja, igakuine maht piiratud 1000 USA dollariga ja puudub juurdepääs e-kaubanduse ühendustele. **Business** plaan (0,5% tasu tehingu kohta) pakub piiramatut arvu terminalide, piiramatut arvu kasutajate, piiramatut mahtu, juurdepääsu WooCommerce/Shopify/Cloudbeds pistikprogrammidele ja eksklusiivseid WhatsApp-teavitusi.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Eelised ja piirangud



### Tähtsündmused



**Seltskonnatöötaja**: Te säilitate oma isiklikud võtmed ja täieliku kontrolli oma rahaliste vahendite üle. Ei ole ohtu, et konto külmutatakse või kolmanda osapoole platvormi pankrotistub.



**Ühenduslikkus**: Lightning Address kui e-posti aadress, NFC-maksed lihtsa puudutusega, intuitiivne kasutajaliides, mille puhul ei ole vaja tehnilisi teadmisi.



**Täielik ökosüsteem**: Tööriistad kõikidele profiilidele (üksikisikud, jaemüüjad, arendajad) koos modulaarsete integratsioonidega, mis sobivad teie vajadustele.



**Erialane vastavus**: PCI-DSS vastavus, Salvadori regulatiivsete nõuete täitmine: turvaline pilvehosting, PCI-DSS vastavus, Salvadori regulatiivsete nõuete täitmine.



### Piirangud



**Välkpiirangud**: Nõuab pidevat wallet ühendust, suurte mahtude likviidsuse haldamine, rikke oht, kui vastuvõtja on võrguühenduseta. Tiankii leevendab neid aspekte integreeritud LSPdega.



**SaaS-sõltuvus**: Kui Tiankii ei ole kättesaadav, on arvete koostamine ajutiselt võimatu (teie rahalised vahendid jäävad turvaliseks).



**Privaatsus**: Tiankii saab jälgida tehingu metaandmeid (summad, kuupäevad). Vähem privaatne kui isehostitud lahendus, näiteks BTCPay Server.



## Kokkuvõte



Tiankii näitab, kuidas hästi kavandatud infrastruktuur võib kõrvaldada tehnilised tõkked, mis takistavad Bitcoin massilist kasutuselevõttu igapäevase valuutana. Kombineerides Lightning Network võimsuse mittekasutatava lähenemisviisi ja kättesaadavate vahenditega, pakub ökosüsteem tasakaalustatud teed finantssuveräänsuse ja kasutusmugavuse vahel.



Kaupmeeste jaoks pakub Tiankii võimalust vähendada oluliselt tehingukulusid ja samal ajal pääseda ligi uuele kliendibaasile. Tarbijate jaoks muudavad Lightning Address ja NFC-kaardid Bitcoin praktiliseks valuutaks, ilma tehnilise keerukuseta.



Kuigi Bitcoin laialdane kasutuselevõtt on endiselt väljakutse, mis nõuab haridust ja aega, näitavad sellised infrastruktuurid nagu Tiankii, et tehnilised vahendid on juba olemas. Bitcoin maksete lihtsustamine ei ole enam kaugem visioon, vaid reaalsus, mis on kättesaadav kõigile, kes soovivad seda teha.



## Ressursid



### Ametlikud dokumendid




- [Tiankii ametlikul kodulehel](https://tiankii.com)
- [Tiankii abikeskus](https://help.tiankii.com)
- [IBI taotlus](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Command Center](https://cc.ibi.me)



### Wallet ühendusjuhendid




- [Connect LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Ühendus




- [Lightning Network Plus](https://lightningnetwork.plus) - Välkkiirte õppevahend
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salvador'i ringmajanduse algatus Bitcoin



### Seotud tööriistad




- [Blink Wallet](https://blink.sv) - Wallet Lightning ühilduv soovituslik
- [LNbits](https://lnbits.com) - Iseseisev wallet lahendus
- [Standard Bolt Card](https://github.com/boltcard) - NFC-kaartide tehnilised näitajad