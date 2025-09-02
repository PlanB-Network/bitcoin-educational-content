---
name: be-BOP
description: Praktiline juhend oma äri rahaks muutmiseks be-BOPi abil
---

![cover-bebop](assets/cover.webp)



**be-BOP** on e-kaubanduse platvorm, mis on mõeldud ettevõtjatele, kes soovivad müüa internetis ja väljaspool, täiesti iseseisvalt, võttes samal ajal vastu makseid Bitcoin, pangakonto kaudu ja sularahas. Lahendus on kasulik ka igat tüüpi organisatsioonidele, kes soovivad koguda annetusi või teenida raha oma erinevate tegevuste eest.



Lahendus on lihtne, kerge ja autonoomne. See võimaldab luua veebipoe isegi keskkonnas, kus traditsioonilised finantsteenused on piiratud või puuduvad. **be-BOP** on tõepoolest kavandatud nii, et see toimib tõhusalt nii pankade juurdepääsuga kui ka ilma nendeta, kasutades Bitcoin maksetaristut.



Selles õpetuses võtame teid samm-sammult läbi:





- Loo oma esimene veebipood koos **be-BOP**iga
- Isikupärastage oma vitriin ja tooted
- Konfigureerige olemasolevad makseviisid
- Mõista parimaid tavasid tõhusaks müügiks internetis koos **be-BOP**iga



See õpetus ei nõua edasijõudnute tehnilisi oskusi. See on suunatud nii arendajatele kui ka käsitöölistele, kaupmeestele, ühistutele või ettevõtjatele, kes soovivad alustada digitaalset kaubandust suveräänselt ja paindlikult.



## Be-BOPi paigaldamise eeldused oma serverisse



Enne be-BOPi paigaldamist veenduge, et teil on olemas järgmine tehniline infrastruktuur. Need Elements on platvormi nõuetekohaseks toimimiseks hädavajalikud:



### S3-ühilduv salvestusruum



be-BOP kasutab failide (näiteks tootepiltide) haldamiseks salvestussüsteemi. Selleks on vaja juurdepääsu S3-teenusele, näiteks:





- [MinIO](https://min.io/) isehostitud
- Amazon S3 (AWS)
- Scaleway objektide säilitamine



Peate konfigureerima ämbri ja esitama järgmise teabe:





- S3_BUCKET**: ämbri nimi
- S3_ENDPOINT_URL**: juurdepääsulink teie S3-teenusele
- S3_KEY_ID** ja S3_KEY_SECRET: teie juurdepääsukoodid
- S3_REGION**: teie S3-teenuse piirkond



### MongoDB andmebaas ReplicaSet režiimis



be-BOP kasutab MongoDB-d kaupluse, kasutajate, toodete ja muude andmete salvestamiseks.



Teil on kaks võimalust:





- Installi MongoDB lokaalselt, kusjuures **ReplicaSet-režiim on lubatud**
- Kasutage veebipõhist teenust nagu **MongoDB Atlas**



Teil on vaja järgmisi muutujaid:





- MONGODB_URL**: andmebaasiühendus Address
- MONGODB_DB**: andmebaasi nimi



## Node.js keskkond



be-BOP töötab koos Node.jsiga. Veenduge, et teil on **Node.js** versioon 18 või uuem ja **Corepack** aktiveeritud (vajalik paketihaldurite nagu pnpm haldamiseks). Käsk, mida tuleb käivitada, on `corepack enable`



### Git LFS paigaldatud



Mõnda ressurssi (näiteks suuri pilte) hallatakse Git LFS-i (Large File Storage) kaudu. Veenduge, et Git LFS on teie masinale installeeritud käsuga `git lfs install`. Kui need eeltingimused on paigas, olete valmis järgmise sammu juurde: be-BOPi allalaadimine ja konfigureerimine.



**Märkus:** Tarkvara kasutuselevõtu tehniline juhend on saadaval eraldi juhendmaterjalina.



## Super-Admin konto loomine



Kui be-BOP esimest korda käivitatakse, luuakse **Superadministraatori** konto. Sellel kontol on kõik back-office-funktsioonide haldamiseks vajalikud õigused. Konto loomiseks järgige järgmisi samme:





- Mine aadressile `yourresiteweb/admin/login`
- Looge turvalise sisselogimise ja parooliga super-administraatori konto



See konto annab teile juurdepääsu kõikidele back-office-funktsioonidele. Pärast loomist saate sisse logida, sisestades oma kasutajanime ja parooli.



![login](assets/fr/001.webp)



## Back-Office'i konfiguratsioon ja turvalisus



Enne Interface tagasisideühenduse konfigureerimist peate looma unikaalse Hash. See pakub kaitset pahatahtlike osalejate vastu, kes üritavad varastada teie Interface administraatori ühenduslinki.



Hash loomiseks minge aadressile `/admin/Settings`. Määrake turvalisusele pühendatud sektsioonis (nt "Admin Hash") unikaalne string (Hash). Pärast registreerimist muudetakse back-office'i URL-i (nt `/admin-yourhash/login`), et piirata juurdepääsu volitamata isikutele.



![hash-login](assets/fr/002.webp)



2.2. Aktiveerige hooldusrežiim (vajaduse korral)



Ikka /admin/Settings, (Settings > General via Interface graphics) check the "enable maintenance mode" option at the bottom of the page.



![maintenance-mode](assets/fr/003.webp)



Vajaduse korral saate määrata volitatud IPv4-aadresside loetelu (komadega eraldatud), et võimaldada hoolduse ajal juurdepääsu eesruumile. Tagakontor jääb administraatoritele kättesaadavaks.



![ip-bebop](assets/fr/004.webp)



## Side seadistamine



Selleks, et be-BOP saaks saata teateid (nt tellimuste, registreerimiste või süsteemisõnumite kohta), peate konfigureerima vähemalt ühe kommunikatsioonimeetodi. Võimalikud on kaks võimalust: e-post (SMTP) või Nostr.



### SMTP-konfiguratsioon (e-post)



be-BOP saab saata e-kirju SMTP-serveri kaudu. Selleks on vaja kehtivaid SMTP-tunnuseid, mida sageli pakub e-posti teenus (nt Mailgun, Gmail jne).



Siin on see, mida peate teadma:



SMTP_HOST: SMTP server Address (nt smtp.mailgun.org)



SMTP_PORT: kasutatav port (sageli 587 või 465)



SMTP_USER: teie kasutajanimi (tavaliselt e-posti Address)



SMTP_PASSWORD: teie parool või API võti



SMTP_FROM: e-posti Address, mis ilmub saatjana




### Nostr konfiguratsioon



be-BOP võimaldab teil saata teateid Nostr-protokolli, detsentraliseeritud sõnumiinfrastruktuuri kaudu. Selleks on vaja generate või Supply Nostr privaatvõtit (NSEC). Seda võtit saate generate otse be-BOPi Interface kaudu, Nostrile pühendatud jaotises. Kui need Elements on õigesti konfigureeritud, saab be-BOP automaatselt sõnumeid ja hoiatusi teie kasutajatele saata.



## Ühilduvad makseviisid



be-BOP ühildub mitme makselahendusega, mis võimaldab teil pakkuda oma klientidele suuremat paindlikkust. Siin on, mida vajate teile sobivaima makseviisi seadistamiseks.



### Bitcoin Onchain



be-BOP võimaldab teil lihtsalt ja turvaliselt vastu võtta Bitcoin makseid otse Blockchain (On-Chain).



**Konfigureerimise sammud:**





- Minge menüüsse **Maksmise seaded**
- On-Chain makseparameetritele juurdepääsuks klõpsake **Bitcoin Noodeless**.
- Täitke järgmised väljad:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Vihje:** Laiendatud avaliku võtme (Zpub) saamiseks võite vaadata oma Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter jne.) täiustatud seadeid. Veenduge, et teie Wallet on **ei ole ainult lugemiseks**, kui kavatsete kasutada tehingulugu.



### Lightning Network



be-BOP saab tänu Lightning Network-le vastu võtta ka koheseid Bitcoin makseid. Praegu on saadaval kaks konfiguratsioonivõimalust:



**Phoenixd**



Mine menüüsse "Maksmise seaded", klõpsa "Phoenixd"



![phoenixd](assets/fr/006.webp)



Seejärel peate sisestama **parooli või token autentimise**, mis ühendab teid oma Phoenixd-instantsiga, Acinqi poolt välja töötatud backendiga, mis võimaldab teil hallata Lightning-makseid oma sõlme abil, kuid ilma maksekanalite haldamise keerukuseta.



**Swiss Bitcoin Pay**



Kui te ei soovi Lightning-sõlme ise hallata, siis **Swiss Bitcoin Pay** on kasutusvalmis ja hõlpsasti konfigureeritav lahendus, mis on ideaalne Lightning-maksete vastuvõtmise alustamiseks ilma keerulise infrastruktuurita.



Konfigureerimise sammud:





- Klõpsake menüüs "Maksesätted" nupule "Swiss Bitcoin Pay"
- Logige sisse oma Šveitsi Bitcoin Pay kontole (või looge see, kui teil veel ei ole).
- Sisestage Šveitsi Bitcoin Pay poolt antud API võti, seejärel klõpsake "Salvesta"



Kui be-BOP on seadistatud, esitab be-BOP automaatselt generate Lightning arveid oma klientidele ja saate makseid otse oma Swiss Bitcoin Pay kontole. See lahendus on ideaalne kasutajatele, kes soovivad vältida isikliku sõlme tehnilist keerukust, võttes samal ajal vastu kiireid ja odavaid makseid.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Lisaks Bitcoin võimaldab be-BOP võtta vastu ka sularahamakseid PayPal'i kaudu, mis on tuntud ja laialdaselt kasutatav rahvusvaheline lahendus.



Konfigureerimise sammud:





- Mine menüüsse "Maksmise seaded"
- Klõpsake nupule `PayPal
- Sisestage oma Paypal'i kontole (arendaja sektsioon) "Kliendi ID" ja "Saladus"
- Valige valitud valuuta (nt **USD**, **EUR**, **XOF** jne)
- Klõpsake nuppu `save



![paypal](assets/fr/008.webp)



**Märkus:** Teil peab olema PayPal ärikonto, et generate neid identifikaatoreid kasutada. Saate neid [arendaja] portaali kaudu (https://developer.paypal.com)



### SumUp



Tarkvara integreerib nüüd **SumUp** makselahenduse, mis võimaldab teil krediitkaardimakseid lihtsalt, turvaliselt ja tõhusalt vastu võtta. Selle funktsionaalsuse kasutamiseks on vaja esmast konfiguratsiooni. Järgnevalt on esitatud järgnevad sammud, mis on nummerdatud selge ja järkjärgulise rakendamise jaoks:





- Alustage oma **API võtme** sisestamisega, mis on konfidentsiaalne võti, mille SumUp andis teile arendajakonto loomisel. See loob turvalise ühenduse teie SumUp-konto ja tarkvara vahel.
- Täitke väli "Kaupmehe kood" unikaalse koodiga, mis identifitseerib teie ettevõtte SumUp platvormil. See kood on oluline tehingute seostamiseks teie ettevõttega.
- Väljal "Valuuta" valige peamine valuuta, mida kasutate oma tehingute tegemiseks (nt **EUR**, **USD**, **CDF** jne).
- Kui kõik väljad on õigesti täidetud, klõpsake seadete salvestamiseks nupule "Salvesta". Seejärel loob süsteem lingi teie SumUp-kontoga ja teie tarkvara on valmis makseid vastu võtma.



![payment-sumup](assets/fr/009.webp)



Pärast seda konfiguratsiooni on **SumUp** integratsioon aktiivne ja toimiv, võimaldades teil kiiresti raha välja võtta ja jälgida oma tehinguid otse tarkvarast.



### Triibud



be-BOP pakub ka täielikku integratsiooni **Stripe'iga**, mis on üks populaarsemaid online-makseplatvorme. Stripe võimaldab teil vastu võtta online-makseid krediitkaardi, digitaalse Wallet ja mitmete teiste makseviiside kaudu. Siin on, kuidas seda aktiveerida:





- Sisestage Stripe'i armatuurlaual esitatud **salajane võti**.
- Täitke väli **avalik võti**, mille pakub samuti Stripe.
- Valige **põhivaluuta**.
- Salvestage konfiguratsioon, seejärel klõpsake nuppu "Salvesta".



![payment-stripe](assets/fr/010.webp)



⚠️ **Pöörake tähelepanu:** On oluline teada teie tegevuse suhtes kohaldatavat käibemaksurežiimi (nt: müük müüja riigi käibemaksuga, õigustatud käibemaksuvabastus või müük ostja riigi käibemaksumääraga), et õigesti konfigureerida **be-BOP** arvete esitamise võimalusi.



## Valuuta konfiguratsioon



**be-BOP** pakub täiustatud valuutahaldust ja on kohandatud mitme valuuta keskkondadele ja spetsiifilistele raamatupidamisnõuetele. Et tagada finantstehingute ja aruandluse järjepidevus, on oluline, et süsteemis kasutatavad erinevad valuutad oleksid nõuetekohaselt konfigureeritud. Järgnevalt on esitatud selle konfiguratsiooni järgimiseks vajalikud sammud:





- Valige **peavaluuta** (`Main currency`)
- Valige "Teisene valuuta"
- Määratlege **viitvaluuta** (`Hinna võrdlusvaluuta`)
- Märkige "Arvestusvaluuta"



Kui kõik valuutad on õigesti konfigureeritud, tagab tarkvara mitme valuuta tehingute automaatse ja täpse konverteerimise, säilitades samal ajal range raamatupidamisliku järjepidevuse.



![settings-currencies](assets/fr/011.webp)



## Taastamisjuurdepääsu konfigureerimine e-posti või Nostr kaudu



Veenduge veel `/admin/settings` mooduli **ARM** kaudu, et super-admin konto sisaldab **email Address** või **recovery pub**, mis hõlbustab protseduuri, kui te unustate oma salasõna.



![settings-users](assets/fr/012.webp)



## Keele seaded



Tarkvara pakub mitmekeelsust, et kohaneda rahvusvahelise publikuga ja parandada kasutajakogemust. Mitmekeelsete funktsioonide aktiveerimiseks on oluline konfigureerida olemasolevad keeled ja määratleda **eelistuskeel**.



![settings-languages](assets/fr/13.webp)



## Interface ja identiteedi konfiguratsioon be-BOPis



**be-BOP** pakub disaineritele kõiki vahendeid, mida nad vajavad veebisaidi kujundamiseks. Esimene samm on avada seadete jaotis `/Admin > Merch > Layout`. Alustage **Top Bar**, **Navbar** ja **Footer** konfigureerimisest.



### Le Top Bar



Konfiguratsioon **Top Bar** võimaldab teil isikupärastada oma tarkvara visuaalset identiteeti, kuvades põhiteavet kohe Interface esimesel real. See tugevdab kaubamärgi äratundmist ja annab kasutajatele selge konteksti.



#### Konfigureerimise sammud:





- Sisestage väljale `Brändi nimi` oma ettevõtte, organisatsiooni või toote nimi. See nimi ilmub Interface ülaosas ja esindab teie peamist visuaalset identiteeti.
- Märkige veebisaidi pealkiri**: valitud pealkiri peaks kokku võtma platvormi eesmärgi. See pealkiri võib ilmuda päises või brauseri vahekaardil.
- Lisa veebisaidi kirjeldus**: siia sisestate oma algatuse lühikirjelduse. See kirjeldus aitab kasutajatele konteksti luua ja seda saab kasutada ka SEO eesmärkidel.



Kui see teave on sisestatud, kuvatakse **Topbaril** teie lahenduse selge, professionaalne ja ühtne esitus.



#### Lingid ülemisel ribal



Ülemise riba sektsioon "Lingid" võimaldab teil lisada otseteed olulistele lehekülgedele teie rakenduses või välistel veebilehtedel. Need lingid kuvatakse otse ülemisel ribal, pakkudes kasutajatele kiiret ja struktureeritud juurdepääsu.



#### Konfigureerimise sammud:





- Sisestage lingi nimi (Tekst)**: sisestage lahtrisse "Tekst" lingi nimi või märgistus, nagu see kuvatakse (nt Avaleht, Kontakt, Abi...).
- Märkige link Address (Url)**: sisestage väljal `Url` sihtlehe (sisemine või väline) täielik Address.
- Vajaduse korral lisage muid linke**: iga konfiguratsioonirea võimaldab teil lisada täiendava lingi, kasutades välju "Tekst" ja "URL".
- Salvesta lingid**: kui kõik lingid on sisestatud, klõpsake nende salvestamiseks nupule "Lisa ülemise riba link".



Selline konfiguratsioon võimaldab teil pakkuda selget, sujuvat ja kättesaadavat navigeerimist oma veebisaidi eri jaotiste või täiendavate ressursside vahel.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



Jaotises **Navbar** saate konfigureerida oma be-BOPi põhinavigatsioonimenüüd, mis tavaliselt asub Interface küljel või ülaosas. See menüü juhatab kasutajaid rakenduse erinevatele lehekülgedele ja funktsioonidele. Linkide konfigureerimine on lihtne ja intuitiivne. See toimib järgmiselt:





- Sisestage lingi nimi (`Text`)**: alustage konfiguratsioonireal lahtri `Text` täitmisega. See vastab navigatsiooniribal kuvatava lingi nimele (näited: *Dashboard*, *Users*, *Settings*...).
- Sisestage link Address (`Url`)**: lahtri `Text` kõrval on väli `Url`. Sellele väljale sisestage selle lehekülje Address, kuhu link peaks ümber suunama. See võib olla sisemine marsruut või link välisele lehele.
- Vajaduse korral lisage mitu linki**: esimese rea all on saadaval uued väljad "Tekst" ja "URL", kuhu saab lisada nii palju linke kui vaja. Iga rida tähistab täiendavat navigatsioonilinki.
- Salvesta lingid**: kui oled sisestanud kõik Elements, klõpsa nupule "Lisa navigatsiooniriba link", et salvestada ja kuvada tulemused navigatsiooniribal.



Selline konfiguratsioon võimaldab tõhusalt struktureerida juurdepääsu tarkvara eri osadele, parandades ergonoomikat ja kasutajakogemust.



![navbar](assets/fr/015.webp)



### Alumine osa



Jaotises **Jalapealkiri** saate kohandada oma tarkvara jalapealkirja, lisades sinna kasulikku teavet või linke. Enne linkide konfigureerimist alustage konkreetse valiku aktiveerimisest:





- Sildi "Powered by be-BOP "** kuvamise lubamine: aktiveerige nupp "Powered by be-BOP", et kuvada see silt jalusesse.
- Sisestage lingi nimi (`Text`)**: täitke väli `Text`, mis vastab lingi sõnastusele jaluses (näited: *Tingimused*, *Privaatsus*, *Kontakt*...).
- Märkige link Address (`Url`)**: sisestage väljal `Url` sihtlehe Address (sisemine või väline).
- Vajaduse korral lisage rohkem linke**: kasutage lisaridu, et luua nii palju linke kui soovite.
- Linkide salvestamine**: klõpsake linkide salvestamiseks nupule "Lisa jaluslehe link".



![footer](assets/fr/016.webp)



### Visuaalne isikupärastamine



**⚠️ Ärge unustage heledate ja tumedate teemade logode ning favicon'i seadistamist, kasutades** `Admin > Merch > Pildid`.



Siin on, kuidas kohandada oma saidi välimust ja tunnetust:



#### Mine Piltide sektsiooni



Menüü `Admin` > `Merch` > `Pildid`.



#### Lisa uus pilt



Klõpsake nupule "Uus pilt".



#### Valige kohalik fail



Klõpsake nuppu "Vali failid", seejärel valige oma Hard kettalt pilt.



#### Valige imporditav fail



Tehke topeltklõps imporditaval pildil (hele logo, tume logo või favicon).



#### Pildi nimetamine



Täitke väli `Pildi nimi`.



#### Pildi lisamine



Klõpsake impordi lõpetamiseks nuppu "Lisa".



![pictures](assets/fr/017.webp)



### Müüja identiteedi seadistamine



#### Identiteedi seaded



See jaotis, millele pääseb ligi menüüst `Admin > Identity` (või `Settings > Identity`), võimaldab teil konfigureerida oma ettevõtte haldus- ja juriidilist teavet.



#### Õiguslik teave





- Ärinimi**: ettevõtte ametlik nimi.
- Äriühingu ID**: juriidiline tunnus või registreerimisnumber (RCCM, SIRET...).



#### Äri Address





- Tänav**: posti Address (tänav, number...).
- Riik**: riik.
- Riik**: provints või piirkond.
- Linn**: linn.
- Postiindeks**: postiindeks.



#### Kontaktandmed





- E-post**: professionaalne e-post Address.
- Telefon**: ettevõtte telefoninumber.



#### Pangakonto





- Kontoomaniku nimi**: kontoomaniku nimi.
- Kontoomanik Address**: kontoomaniku Address.
- IBAN**: Rahvusvaheline pangakonto number.
- BIC**: SWIFT/BIC-kood.



![bank-account](assets/fr/019.webp)



#### Arveldamine





- Andmete eeltäitmiseks klõpsake nuppu "Täida kaupluse põhiteabega".
- Very-top-right issuer information**: väli juriidilise/maksualase teabe jaoks, mis on arvetel nähtav.
- Muudatuste salvestamiseks klõpsake nuppu `Update`.



**Märkus:** saate sisestada ka lisateavet, mis kuvatakse Invoice-l vastavalt teie vajadustele.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Füüsiline kauplus Address



Füüsilise kaupluse omanike jaoks lisage spetsiaalne täielik Address jaotises `Admin > Settings > Identity` või spetsiaalses jaotises. See võimaldab seda kuvada ametlikel dokumentidel ja vajaduse korral jaluses.



![seller-id](assets/fr/021.webp)



## Tootejuhtimine



### Uue toote loomine



Toote lisamiseks või muutmiseks minge menüüsse `Admin > Kaup > Tooted`. Täitke järgmised väljad:



#### Põhiteave





- Toote nimi**: toote nimi (nt *BOP T-särk piiratud tiraažiga*).
- Lutsu**: URL-i identifikaator ilma tühikuteta (nt `tshirt-bop-edition-limitee`).
- Alias** *(valikuline)*: kasulik kiireks lisamiseks korvi spetsiaalse välja kaudu.



![product-config](assets/fr/028.webp)



#### Hinnakujundus





- Hinnasumma**: toote hind (nt "25.00").
- Hind Valuuta**: valuuta (EUR, USD, BTC jne).
- Eritooted**:
  - see on tasuta toode.
  - see on tasuline toode.



#### Toote valikud





- Üksiktoode (standalone)**: ühe tellimuse kohta on võimalik ainult üks lisa (nt annetus, sissepääsupilet).
- Variatsioonidega toode**:
  - Ärge kontrollige `Standalone`.
  - Kontrollida `Toode on kerge varieeruvusega (ei ole varude erinevus)`.
  - Lisa:
    - Nimi** (nt *Size*),
    - Väärtused** (nt: S, M, L, XL),
    - Vajaduse korral hinnavahe** (nt: "+ 2 USD" XL-i puhul).



![product-details](assets/fr/029.webp)



## Varude haldamine



### Täiustatud valikud toote loomisel (varu, tarne, piletid jne)



#### Piiratud varuga toode



Kui teie toode ei ole saadaval piiramatus koguses, märkige "Tootel on piiratud varud". See aktiveerib ülejäänud koguste automaatse jälgimise. Kui see märkeruut on märgitud, ilmub väli, mis näitab **saavutatav varu**.



Süsteem haldab:





- Reserveeritud varud** → tooted korvis, mille eest ei ole veel tasutud
- Müüdud varud** → juba ostetud tooted



**Korvi broneerimise aeg**: Kui klient lisab toote oma ostukorvi, on see "reserveeritud" piiratud ajaks. Seda aega saate muuta aadressil: (väärtus minutites): `Admin > Config > Cart reservation` (väärtus minutites)



#### Toode, mis tuleb tarnida?



Märkige "Tootel on füüsiline komponent, mis tarnitakse kliendi Address-le". See on kasulik kõigi füüsiliselt saadetavate toodete puhul (raamatud, t-särgid jne)



#### Muud võimalused





- Pilet**: märkige, kui toode on pilet üritusele
- Broneering**: kontrollige, kas tegemist on broneeringuajaga (nt: seanss, kohtumine)



![product-options](assets/fr/030.webp)



### Tegevuse seaded (alt)



Selles jaotises määratakse kindlaks, **kuidas** ja **kuidas** saab toodet vaadata ja osta:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Märkige ainult need kanalid, mida soovite kasutada.



## CMS lehekülgede ja vidinate loomine ja kohandamine



### Kohustuslikud CMS leheküljed



Mine menüüsse `Admin > Kaup > CMS`. Näete nimekirja olemasolevatest lehekülgedest ja saate lisada uusi lehekülgi käsuga **Add CMS page**.



CMS leheküljed on olulised:





- Teavitage oma külastajaid (nt kasutustingimused)
- Järgida seadusi (nt privaatsuspoliitikat)
- Selgitage teatavaid kaupluse omadusi (nt IP-kogumine, 0% käibemaks)



Te võite lisada muid lehekülgi vastavalt vajadusele:





- Meist / Kes me oleme
- Toetage meid / annetused
- KKK
- Kontakt
- jne.



**Nipp: klõpsake igal lingil või ikoonil, et muuta iga lehekülje **sisu**, **pealkirja** või **soe nähtavust**.



### Kujundus ja graafika Elements



Mine: `Admin > Merch > Layout`. Saate kohandada oma saidi visuaalset Elements:



![product-options](assets/fr/032.webp)



#### Top Bar





- Muuda või kustuta linke (EX: HOME, ABOUT US,...)
- Navigeerimine veebisaidi põhiosade vahel



#### Navbar (peamine navigatsiooniriba)





- Esineb halli ala ülemise tulba all
- Sisaldab kiiret juurdepääsu: `Konfig`, `Maksmise seaded`, `Tehingud`, `Sõlmede haldamine`, `Vidinad` jne.
- Ainult direktorid



#### Footer





- Saab muuta menüüst `Admin > Merch > Layout`
- Sisaldab: kontaktandmed, kasulikud lingid, õiguslikud teated...



#### Kohandage visuaalset kujundust



Mine: `Admin > Kaup > Pildid`



Saate:





- Muuda **pealogo**
- Muuda või lisa kujundust **pildid**



#### Saidi kirjeldus



Samuti on võimalik muuta "Piltide" all, see võimaldab teil kuvada **summareid või loosungeid** päises või jaluses, sõltuvalt teemast.



**Märkus:** see võimaldab teil kohandada välimust vastavalt teie brändi identiteedile (haridus-, kaubandus- või kogukonna-).



### Vidinate integreerimine CMS-i lehtedesse



Vidinad** rikastavad teie CMS-i lehekülgi dünaamilise või visuaalse Elements-ga.



#### Vidinate loomine



Mine: `Admin > Vidinad`



Näiteid saadaval olevatest vidinatest:





- Väljakutsed**: väljakutsed või missioonid
- Sildid**: kategooriad või märksõnad
- Liugurid**: pildikarussellid
- Spetsifikatsioonid**: Spetsifikatsioonide tabelid
- Vormid**: vormid (kontakt, tagasiside jne.)
- Tagasiarvamised**: taimerid
- Galeriid**: pildigaleriid
- Edetabelid**: kasutajate edetabelid



![widgets](assets/fr/033.webp)



#### Integreerimine CMS-i lehtedesse



Kasutage oma CMS-lehtede sisus **shortcodes**:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Parameetrid**:





- `slug`: unikaalne vidina identifikaator
- `display=img-1`: tootespetsiifiline pilt
- `Laius`, `Kõrgus`, `Fit`: pildi mõõtmed ja stiil
- autoplay=3000`: aeg millisekundites kahe slaidi vahel



**Eelised**:





- Lihtne sisestada (kopeeri ja kleebi)
- Dünaamiline: kõik vidina muudatused kajastuvad automaatselt
- Arendajat ei ole vaja



## Tellimuste haldamine ja aruandlus



### Tellimuse jälgimine



Varasemate tellimuste vaatamiseks ja haldamiseks minge aadressile: `Admin > Tehingud > Tellimused`



Siit leiate **täieliku nimekirja teie saidil tehtud tellimustest**.



![orders](assets/fr/034.webp)



#### Visualiseerimine ja otsing



Interface võimaldab teil otsida ja filtreerida tellimusi mitme kriteeriumi alusel:





- järjekorranumber: järjekorranumber
- toote varjunimi: toote identifikaator või nimi
- makse Mean": kasutatud makseviis (kaart, krüpto jne)
- `Email`: kliendi e-posti aadress



Need filtrid hõlbustavad kiiret otsingut ja sihipärast haldamist.



#### Iga tellimuse üksikasjad



Klõpsates tellimusel, saate juurdepääsu täielikule failile, mis sisaldab:





- Tellitud tooted
- Klientide teave
- Tarne Address (vajaduse korral)
- Kõik tellimusega seotud märkused



#### Võimalikud toimingud tellimuse puhul



Saate:





- Tellimuse kinnitamine (kui see on pooleli)
- Tellimuse tühistamine (probleemi või kliendi soovi korral)
- Lisada **märgised** (sisemise korralduse jaoks)
- Konsulteerida / lisada **siseseid märkusi**



**Märkus:** see osa on oluline hea logistika ja kliendisuhete jaoks.



### Aruandlus ja eksport



Müügi- ja maksestatistikale juurdepääsuks:


administraator > Seaded > Aruandlus



![reporting](assets/fr/035.webp)



Siit leiate ülevaate oma ettevõttest **kuulisi ja aastaseid aruandeid**.



#### Aruande sisu



Aruanded on jagatud osadeks:





- Tellimuse üksikasjad**: tellimuste arv, staatus (kinnitatud, tühistatud, pooleliolev), areng
- Toote üksikasjad**: müüdud tooted, kogused, populaarsed tooted
- Maksete üksikasjad**: kogutud summad, jaotus makseviiside kaupa



#### Andmete eksport



Iga sektsioon sisaldab nuppu **Export CSV**, mis võimaldab teil:





- Andmete allalaadimine CSV-vormingus
- Avage need Excelis, Google Sheetsis jne.
- Arhiveerimine haldus- või raamatupidamislikuks kasutamiseks
- Kasutage neid sisearuannete jaoks



**Märkus:** sobib ideaalselt tulemuste jälgimiseks, raamatupidamiseks ja esitlusteks.



## Nostr Messaging'i konfiguratsioon (valikuline)



![nostr-config](assets/fr/036.webp)



Platvorm toetab **Nostr**-protokolli teatavate täiustatud funktsioonide jaoks:





- Detsentraliseeritud teated
- Sisselogimine ilma paroolita
- Interface kerge manustamine



### Nostri privaatvõtme genereerimine ja lisamine



Mine:


admin > Node Management > Nostr





- Kui teil ei ole nsec'i, klõpsake nuppu **Loo nsec**.
- Süsteem saab generate seda automaatselt.
- Alternatiivina võite kasutada olemasolevat võtit (nt Damus või Amethyst).



Järgmine:





- Kopeeri võti `nsec`
- Lisa see oma faili `.env.local` (või `.env`): ```env NOSTR_PRIVATE_KEY=YourNsecIciKey



### Nostriga aktiveeritud funktsioonid



Pärast konfigureerimist on saadaval mitu funktsiooni:



**Teavitused Nostr** kaudu





- Saada teateid tellimuste, maksete või süsteemi sündmuste kohta
- Administraatoritele või kasutajatele



**Interface kerge administratsioon**





- Juurdepääs Nostr-kliendi kaudu
- Võimaldab kiiret, mobiilisõbralikku haldamist



**Liitumine ilma paroolita**





- Logi sisse turvalise lingi kaudu (saadetakse Nostr kaudu)
- Suurem kasutajate ohutus ja sujuvus



## Disain ja teema kohandamine



Et kohandada oma poe välimust oma graafilise põhimääruse järgi, minge aadressile: `Admin > Merch > Theme`



Siit leiate kõik võimalused kohandatud teema **loomiseks** ja **konfigureerimiseks**.



### Teema loomine



![theme](assets/fr/037.webp)



Teema loomisel või muutmisel saate määrata:





- Värvid**: nuppude, taustade, teksti, linkide jne jaoks.
- Kirjatüübid**: kirjatüüpide valik pealkirjade, lõigete ja menüüde jaoks
- Graafilised stiilid**: piirid, marginaalid, vahekaugused, plokkide kuju



### Kohandatavad sektsioonid



Saidi iga osa saab reguleerida iseseisvalt:





- Pealkiri**: ülemine navigatsiooniriba
- Body**: peamine sisu
- Alumine osa**: lehekülje alumine osa



**Märkus:** selline granulaarsus tagab järjepidevuse saidi visuaalsete kujunduste ja teie brändi identiteedi vahel.



### Teema aktiveerimine



Kui teema on konfigureeritud:





- Klõpsake nuppu **Salvesta**
- Aktiveerige see poe **peateemana**



**Märkus:** aktiivne teema on see, mis on külastajatele nähtav.



## E-posti mallide konfigureerimine



Platvorm võimaldab teil personaliseerida kasutajatele automaatselt saadetavaid e-kirju. Mine: seaded > Seaded > Mallid`



![emails-templates](assets/fr/038.webp)



### Mallide loomine / redigeerimine



Iga e-kiri (tellimuse kinnitus, unustatud parool jne) on:





- Teema**: e-kirja teema (nt "Teie tellimus on kinnitatud")
- HTML Body**: E-kirjas kuvatav HTML-sisu



**Märkus:** saate sisestada teksti, pilte, linke jne. vastavalt vajadusele.



### Dünaamiliste muutujate kasutamine



E-kirjade dünaamiliseks muutmiseks sisestage muutujaid nagu:





- `{Tellimusnumber}}`: asendatakse tegeliku tellimuse numbriga
- `{invoiceLink}}`: link Invoice-le
- `{websiteLink}}`: Teie veebilehe URL



**Märkus:** need sildid asendatakse automaatselt, kui need saadetakse.



### Täiustatud nõuanded





- Loo e-kirju, mis on **vastav**, et neid oleks lihtne lugeda mobiilseadmetes
- Lisage **tegevusnupud** (maksmine, allalaadimine, tellimuse jälgimine)
- Testige oma e-kirju, saates need enne avaldamist iseendale



## Konkreetsete siltide ja vidinate konfigureerimine



### Siltide haldamine



Sildid saab kasutada oma sisu struktureerimiseks ja rikastamiseks. Nendele juurdepääsuks: `Admin > Vidinad > Silt`



![tags-config](assets/fr/039.webp)



### Sildi loomine



Täitke järgmised väljad:





- Sildi nimi**: kuvatud sildi nimi
- Slug**: unikaalne identifikaator (ilma tühikute ja aktsentideta)
- Siltide perekond**: rühmitab sildid kategooriate kaupa



![targsconfig](assets/fr/040.webp)



#### Olemasolevad perekonnad:





- loojad": autorid või tootjad
- jaemüüjad: müüjad või müügipunktid
- "Ajaline": perioodid või kuupäevad
- sündmused: seotud sündmused



### Vabatahtlikud väljad



Neid välju saab kasutada sildi rikastamiseks, nagu oleks tegemist sisulehega:





- Pealkiri
- Alapealkiri
- Lühike** sisu
- Täielik sisu** (prantsuse keeles)
- CTA-d** (tegevusnupud)



### Siltide kasutamine



Sildid võivad olla:





- Toodetele eraldatud
- Integreeritud CMS-i lehtedesse sildiga: [Tag=slug?display=var-1]



## Allalaaditavate failide konfigureerimine



Et pakkuda oma klientidele allalaaditavaid dokumente: `Admin > Kaup > Failid`



### Faili lisamine



1. Klõpsake **Uue fail**


2. Teavita:




   - Faili nimi** (nt *Installatsioonijuhend*)
   - Üleslaetav fail** (PDF, pilt, Word...)



**Märkus:** Pärast lisamist genereerib platvorm automaatselt **püsiva lingi**.



### Kasutades linki



Selle lingi saab seejärel sisestada:





- CMS** lehekülg (tekstilink või nupp)
- **e-maili klient** (malli kaudu)
- **tootelehe** (nt kasutusjuhendi allalaadimine)



See on ideaalne *kasutajaraamatute, tehniliste juhendite, tootelehtede...* esitamiseks ilma välise hostimise vajaduseta.



## Nostr-bot



Platvorm pakub täiustatud integratsiooni **Nostr**-protokolliga automaatse bot'i kaudu.



Mine: sõlme haldamine > Nostr



### Peamised omadused



#### Relee haldamine





- Lisage või eemaldage boti poolt kasutatavad **relaisid**
- Optimeerida saadetud sõnumite **saavutatavust** ja **lukust**



#### Automaatne sissejuhatav sõnum





- Aktiveeri automaatne sõnum **esimesel kasutajakontaktil**
- Sobib ideaalselt:
  - Teenuse esitlemine
  - Saada kasulik link (nt KKK, kontakt, tellimus)



#### Teie `npub'i sertifitseerimine





- Lisage **logo** ja **avalik nimi**
- Link **kinnitatud veebidomeenile**
- Suurendab teie Nostri identiteedi usaldusväärsust ja tuntust



### Nostr-boti kasutusjuhtumid





- **Tellimuse kinnituste** saatmine teile
- Automaatne reageerimine **sündmustele (nt uus tellimus)**
- Klientide vahelise **detsentraliseeritud suhtluse loomine**



## Tõlke siltide ülekoormamine



be-BOP on mitmekeelne (FR, EN, ES...), kuid saate tõlkeid kohandada vastavalt oma vajadustele.



Selleks minge aadressile: seadistused > Keel



### Laadimine ja redigeerimine



Tõlkefailid on JSONis. Saate:





- Allalaadimine** keelefailid
- Olemasolevate tekstide muutmine**
- Lisage** oma tõlked



Link originaalfailidele:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Näide:** asendage `Add to cart` sõnadega `Ajouter au panier` või `Acheter`.



## Meeskonnatöö ja müügipunkt (POS)



### Kasutaja ja juurdepääsuõiguste haldamine



#### Rollide loomine



Mine: `Admin > Seaded > ARM`



Rolli loomiseks klõpsake **Loo roll** (nt `Superadmin`, `POS`, `Pileti kontrollija`).



Iga roll sisaldab:





- kirjutamisjuurdepääs**: kirjutamisjuurdepääs
- lugemisjuurdepääs**: lugemisjuurdepääs
- keelatud juurdepääs**: lõigudevahelised lõigud



#### Kasutaja loomine



Samas menüüs `Admin > Settings > ARM` lisage kasutaja:





- sisselogimine
- alias
- e-posti taastamine
- (valikuline) `recovery npub` Nostr kaudu ühenduse loomiseks



Määrake eelnevalt määratletud roll.



![pos-users](assets/fr/045.webp)



Ainult lugemisõigusega** kasutajad näevad menüüd *kriitiliselt* ja ei saa sisu muuta.



## Müügipunkti (POS) konfiguratsioon



### POS-rolli määramine



Et anda kasutajale juurdepääs kassale, määrake roll "Müügipunkt (POS)": `Admin > Config > ARM`



Ta saab ühendust turvalise URL-i kaudu: `/pos` või `/pos/touch`



### POS-spetsiifilised funktsioonid



Be-BOP pakub Interface, mis on pühendatud füüsilisele müügile (kauplus, üritus jne).



#### Kiire lisamine aliase kaudu



Väljal `/cart` on väli, mis võimaldab teil lisada toote:





- Skaneerides **joonekoodi** (ISBN, EAN13)
- Sisestades **toote varjunime** käsitsi



**Märkus:** toode lisatakse automaatselt ostukorvi.



#### Maksevahendid



POS toetab:





- Liik
- Krediitkaart
- Lightning Network (krüpto)
- Muud vastavalt konfiguratsioonile



Saadaval on kaks täiustatud valikut:





- Käibemaksuvabastus**: kohaldatakse põhjenduse korral (valitsusvälised organisatsioonid, välismaalased...)
- Kinkesoodustus**: erakorraline allahindlus koos kohustusliku märkusega



#### Kliendipoolne kuva



URL `/pos/session` on mõeldud **sekundaarse ekraani** (HDMI, tahvelarvuti...) jaoks:



Plakat:





- Valmistatavad tooted
- Kogusumma
- Makseviis
- Kohaldatud allahindlused



**Märkus:** klient jälgib tellimust otseülekandes, samas kui müüja registreerib selle `/pos`.



### POS kokkuvõte



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Täname teid selle õpetuse hoolika jälgimise eest.