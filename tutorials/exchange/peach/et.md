---
name: Peach
description: Täielik juhend Peach kasutamise ja bitcoinidega kauplemise kohta P2P-s
---

![cover](assets/cover.webp)





## Sissejuhatus



KYC-vabad peer-to-peer (P2P) vahetused on kasutajate konfidentsiaalsuse ja finantsautonoomia säilitamiseks hädavajalikud. Need võimaldavad otsetehinguid üksikisikute vahel ilma isikusamasuse kontrollimise vajaduseta, mis on oluline nende jaoks, kes hindavad privaatsust. Teoreetiliste mõistete põhjalikumaks mõistmiseks vt kursus BTC204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Mis on Peach?



Peach on P2P vahetusplatvorm, mis võimaldab kasutajatel osta ja müüa bitcoine ilma KYC-ta. See pakub intuitiivset kasutajaliidest ja täiustatud turvaelemente. Võrreldes teiste lahendustega, nagu Bisq, HodlHodl ja Robosat, paistab Peach silma oma kasutusmugavuse poolest.


multisignature eskrovisüsteem (2-2) tagab tehingute ajal rahaliste vahendite turvalisuse. Peach toetab erinevaid makseviise ja omab mainesüsteemi, mis suunab kauplejate tegevust. Nagu tavaliselt P2P platvormide puhul, on seetõttu oluline säilitada hea maine, et säilitada usaldusväärsus teiste kauplejate suhtes.



### 2. Privaatsus ja kogutud andmed



**Milliseid andmeid Peach kogub?



Peach püüab salvestada oma kasutajate kohta võimalikult vähe andmeid. Siin on ülevaade meie serveritesse salvestatud andmetest:





- hash teie kordumatu taotluse identifikaator (AdID)
- hash teie makseandmete kohta
- Teie krüpteeritud vestlused
- Tehinguandmed, et tagada, et anonüümsed kasutajad ei ületa kauplemislimiiti (kasutatud makseviiside liigid, ostu- ja müügisummad)
- Address, mida kasutatakse deposiitkontolt saatmiseks ja vastuvõtmiseks
- Kasutusandmed (Firebase & Google Analytics), ainult teie nõusolekul



Meeldetuletuseks, hash on andmed, mis on sarnaselt krüpteerimisele muudetud tundmatuseni. Samad andmed annavad alati sama hash, mis võimaldab tuvastada dubleeringuid ilma algandmeid tundmata.



*Täpsema selgituse saamiseks hashingi kohta võtke see kursus:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Kes saab minu makseandmeid näha?





- Ainult teie vastaspool näeb teie makseandmeid
- Andmed edastatakse Peach serverite kaudu, kuid need on täielikult krüpteeritud otsast lõpuni
- Vaidluse korral on teie makse üksikasjad ja vestluste ajalugu nähtav määratud Peach vahendajale



## Paigaldamine ja konfigureerimine



### 1. Peach rakenduse paigaldamine



![Installation de Peach](assets/fr/01.webp)





- Laadige taotlus alla aadressilt [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). IOS-i puhul peate kõigepealt installima rakenduse [testflight](https://apps.apple.com/us/app/testflight/id899247664).
- Järgige seadme paigaldusjuhiseid.
- Paigaldamise ajal palutakse teil valida, kas soovite jagada teatud andmeid, et täiustada Peach rakendust. (pilt 1)
- Järgmisel ekraanil (pilt 2) on kaks võimalust:
 - Kui olete uus kasutaja, klõpsake "Uus kasutaja", et luua uus profiil
 - Kui teil on juba konto, kasutage "Restore", et taastada oma olemasolev profiil
- Kui teil on soovituskood, saate selle sisestada siia.
- Olemasoleva konto taastamiseks (pilt 3) on vaja :
 - Teie varundatud fail
 - Parool selle faili dekrüpteerimiseks



### 2. Ülevaade põhiekraanidest



Peach rakendus on korraldatud nelja peamise ekraani ümber, millele pääseb ligi alumisest navigatsiooniribast:



![Navigation dans l'application](assets/fr/02.webp)





- Kodu (4)** : Peakuva, kust saate valida, kas soovite osta või müüa, luua uusi tehinguid ja pääseda ligi olemasolevatele pakkumistele:
 - luua pakkumisi kahe alloleva nupuga (luua osta / luua müüa)
 - kasutada ära teiste kasutajate loodud olemasolevaid pakkumisi, kasutades selleks kahte allpool olevat nuppu ("Osta"/"Müü").





- Wallet (5)** : Teie integreeritud bitcoin wallet, mis võimaldab teil :
 - Kontrollige oma saldot
 - Bitcoinide vastuvõtmine
 - Envoyer bitcoinid (koos mündi kontrolliga)
 - Vaadake oma tehingute ajalugu
 - Müügi rahastamine





- Tehingud (6)**: teie praegused ja varasemad lepingud kolme vahekaardi all:
 - Pooleliolevad ostud
 - Käimasolev müük
 - Teie vahetuste ajalugu





- Seaded (7)** : Konfigureerimiskeskuse jaoks
 - Vaadake oma profiili (maine, märgid, piirangud jne.)
 - Turvalisuse haldamine (varundamine, pin)
 - Halda oma makseviise
 - Võtke ühendust tugiteenusega
 - Keele muutmine
 - jne.



### 3. Konfigureerige oma makseviisid



![Accès aux paramètres de paiement](assets/fr/03.webp)



Saate oma makseviise hallata seadetes (pilt 8)



Peach pakub online-makseid ja isiklikke makseid (ainult registreeritud kohtumistel).



**Online maksed



**Tähtis:**


kasutajate kaitsmiseks nõuab Peach, et rahaliste vahendite allikas vastaks reklaamitud allikale. Kauplejad peavad enda kaitseks tagama, et see on nii.



![Configuration des paiements en ligne](assets/fr/04.webp)



Meetodi lisamine :




- Klõpsake vahekaardil "online" nupule "lisa valuuta/meetod"
- Valige oma valuuta
- Valige oma eelistatud makseviis



*Saadaolevad makseviisid:*



***Pangaülekannete puhul: ***




- SEPA (standard- või kiirkorras)
- Täitke oma SEPA pangaandmed.



***Online wallet on aktsepteeritud :***




- Olenevalt riigist on saadaval mitu võimalust (Revolut, Paypal, Wise, Strike jne)
- Järgige juhiseid oma sisselogimisandmete lisamiseks



*kinkekaart kasutatav:*** kinkekaart kasutatav:*** kinkekaart kasutatav:*** kinkekaart kasutatav:*** kinkekaart kasutatav:*** kinkekaart kasutatav:*** kinkekaart kasutatav:***




- Amazon, Steam jne.
- Sisestage kaardi väljaandjariik ja muud vajalikud andmed



***Maksevõimalused riigisiseselt:***


Riigipõhised maksesüsteemid :




- Satispay (Itaalia)
- MB Way (Portugal)
- Bizum (Hispaania)
- Kiiremad maksed (Ühendkuningriik)
- jne.



***Privaatsete maksete puhul: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Valige "Meetup" (pilt 12)
- Seejärel valige oma kohtumine nimekirjast (pilt 13)



### Kasutusjuhend





- Saate lisada mitu makseviisi
- Mida rohkem meetodeid lisate, seda laiemad on pakkumised, millele teil on juurdepääs
- Kontrollige oma andmete õigsust enne registreerimist
- Saate oma makseviise igal ajal muuta või kustutada



**Turvalisuse märkus**: Teie makseandmed on krüpteeritud ja neid jagatakse ainult teie vahetuspartneriga tehingu ajal, välja arvatud vaidluse korral, kus Peach vahendajal on samuti juurdepääs.



### 4. Kuidas kindlustada oma portfelli



**Kaasluse mõistmine Peach kontol



Peach kontol ei ole kasutajanime ega parooli. See on fail, mida hoitakse lokaalselt teie telefonis, mis tähendab, et Peach ei pea teie andmeid säilitama ega teadma teie isikut: teie olete kontrolli all. See fail sisaldab kõiki teie andmeid: sealhulgas 12 bitcoini taastamissõna, PGP-võtmed, makseandmed jne. Seega on väga oluline see fail salvestada ja kaitsta seda __robust__ parooliga.



Selline lähenemisviis tagab teatava konfidentsiaalsuse ning jätab vastutuse andmete ja varukoopiate haldamise eest kasutaja kätte. Telefoni kaotamine ilma varukoopiana tähendab juurdepääsu kaotamist teie Peach kontole ja rahalistele vahenditele.



**Loo oma varukoopiaid**






- Juurdepääs seadetele avakuva paremal allosas olevalt vahekaardilt
- Valige seadete menüüst valik "varukoopiad"



![Processus de sauvegarde](assets/fr/06.webp)



Saadaval on kahte tüüpi varukoopia:



**Konto faili salvestamine (pilt 14)**




- Klõpsake nuppu "Loo uus varukoopia"
- Looge **tugev** parool, et krüpteerida oma varundusfaili
- Saatke see fail sellisesse kohta, mis tagab selle redundantsuse telefoni kadumise korral.



Failide varukoopia taastab teie täieliku Peach konto, sealhulgas :




- Teie portfell
- Teie makseviisid
- Makseandmed
- Tehingute ajalugu koos vastaspoolte ja nendega peetud vestluste üksikasjadega



**Tagastamislause salvestamine (pilt 15)**




- Järgige juhiseid, et kuvada oma taastamislauset
- Kirjuta sõnad hoolikalt õiges järjekorras üles
- Hoidke seda varukoopiat turvalises kohas, mis ideaalis erineb kontofailist



Taastamislause võimaldab taastada :




- Teie maine, teie ametid
- Teie bitcoin raha



Aga **ei** järgmist:




- Teie praegused ja varasemad vestlused
- Makseandmed
- Vastaspoole andmed tehinguajaloos




## Bitcoinide ostmine ja müümine



### 1.a Kuidas osta bitcoine: Võtke pakkumine müüa



Ostja esimene refleks peaks olema vaadata müügipakkumisi, mida on juba rahastatud bitcoin'idega.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Vajutage avakuval nupule "Osta" (pilt 16)
- Seejärel saate sirvida nimekirja bitcoin'idest, mis on pandud depoosüsteemi ja on valmis müügiks (pilt 17). Saate näha summat, hinda (protsentides võrreldes KYC-turuga), makseviise ja aktsepteeritud valuutasid.
- Kasutage pakkumiste sorteerimiseks ja järjestamiseks filtreid (pilt 18).
- Märkus: filtrite lehe allosas olev nupp võimaldab teil saada teate, kui teie filtritele vastav pakkumine on avaldatud; ja nupp "reset", mis lihtsalt kustutab kõik filtrid (pilt 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Vaadake teile sobivat pakkumist ja saatke vahetusnõue (pilt 19)
- Võite esitada mitu vahetustaotlust ja esimene positiivne pakkumine tühistab teie teised taotlused.
- Tehke makse kokkulepitud viisil.


**Märkus:** Raha allikas peab vastama sellele, mille määrasite makseviisi lisamisel.




- Kinnitage oma makse taotluses kohe, kui see on tehtud**.
- Oodake, kuni müüja saab makse kätte ja deklareerige see sellisena (pilt 20)
- Ja lõpuks, hinnake oma kogemust müüjaga (pilt 21)



![Réception des bitcoins](assets/fr/09.webp)





- Jälgige oma tehingu staatust
- Kontrollige bitcoinide kättesaamise kinnitust
- Fondid on saadaval teie Peach portfellis (pilt 22 ja 23)



### 1.b Kuidas osta bitcoine: Loo pakkumine



Kui te ei leia sobivat müügipakkumist, võite koostada ostupakkumise. Kuna see ei seo selles etapis ühtegi bitcoini, on teil väiksem võimalus leida vahetuspartner, eriti kui teie kogemus ja maine on kehv või olematu. Selle probleemi lahendamiseks on oluline, et pakkumise loomisel teeksite *kõrge preemiapakkumise*, et motiveerida müüjaid teie pakkumist valima. Jätkame:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Vajutage avakuval nupule "Loo ostupakkumine" (pilt 24)
- Lisage makseviis, kui te pole seda veel teinud, ja sisestage oma eelistused (kogus, lisatasu jne) (pilt 25).


Valik "kohe" võimaldab teil automaatselt kauplemisavalduse vastu võtta.




 - Jätkamiseks klõpsa uuesti "loo pakkumine"
- Kui see on loodud, on müüjate kord tulla teie juurde vahetustaotlusega. Võite rakenduse muretult sulgeda ja sellest väljuda.
- Kui te ei saa ühtegi taotlust, saate preemiat muuta. Pidage meeles: suurem preemia motiveerib müüjaid teie pakkumist otsima (pilt 26).
- Oma pakkumise leiate vahekaardilt "Osta", mis omakorda asub aknas "Exchange" (joonis 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Kui saate ostupäringu (joonis 28) (ja kui te ei ole viipekaubandust deaktiveerinud joonisel 25), võtke kauplemine vastu pärast müüja maine kontrollimist. Kui kiirkaubandus on aktiveeritud, hüpake otse pildile 29.
- Müüja peab seejärel bitcoini paigutama depoosüsteemi ("fund the safe"). (pilt 29)
- Seejärel makske müüjale joonisel 30 näidatud sihtkohas oma isikliku pangasüsteemi kaudu. Ärge lohistage kursorit "Olen teinud makse" enne, kui olete seda teinud!
- Saate müüjaga suhelda sõnumite süsteemi kaudu (P2P krüpteeritud). Probleemi korral saate avada vaidluse, klõpsates paremas ülemises nurgas oleval ikoonil (pilt 31). Seejärel astub arutelusse Peach vahendaja.



![Offre de vente completée](assets/fr/12.webp)





- Kui müüja on raha kätte saanud, teatab ta sellest ja depoosüsteem vabastab bitcoini, mis on teel teie wallet-sse (vaikimisi GroupHug'i, Peach tehingu grupeerimissüsteemi kaudu, mis töötab kord päevas),
- Hinda oma kogemust müüjaga



See on kõik!



**Märkus uutele ostjatele:** müüjad lähtuvad oma tehingutest ostjate maine põhjal ja kipuvad vältima pakkumisi ostjatelt, kellel ei ole veel ühtegi tehingut tehtud. Esimesel juhul on lihtsam luua mainet, võttes vastu olemasolevaid müügipakkumisi.




### 2.a Kuidas müüa bitcoine: Looge müük



Kiireim ja lihtsaim viis Peach kaudu müümiseks on **loomine müügipakkumine**.



![Création d'un ordre de vente](assets/fr/13.webp)





- Klõpsake avalehel "Loo müügipakkumine" (pilt 32)
- Seadistage oma pakkumine, veenduge, et sisestate makseviisi ja õiged parameetrid


saate ka :




  - luua mitu identset pakkumist
  - aktiveerida "kohene vahetus", nii et esimesena saabuv ostja saab lepingu vastu võtta (ilma teie kinnitamiseta) ja jätkata maksmist.
  - valida tagasimakse aadress
  - rahastada oma wallet Peach pagasiruumi
- Rahastage tehingut, saates bitcoinid ettenähtud aadressile (pilt 34)
- Oodake tehingu kinnitust. Kui see on tehtud, on teie pakkumine turul nähtav.



![Attente du paiement](assets/fr/14.webp)





- Oodake, et ostja teie pakkumise vastu võtaks. Kaaluge preemia (%) suurendamist, kui soovite asju kiirendada (pilt 36)
- Kui olete saanud vahetustaotluse, kontrollige ostja mainet. Otsustage ise, kas profiil sobib teile, ja klõpsake "aktsepteerida", kui see on nii. (37)
- Nüüd on ostja kord teha makse tema pangast teie pangale. Seejärel edastab ta makse teile. Ärge kartke ostjaga vestluses ühendust võtta.
- pärast seda, kui olete kontrollinud, et teie pank on raha kätte saanud*, vabastage raha, vajutades nupule "olen saanud makse" (pilt 38). Ärge kunagi kinnitage makse laekumist enne, kui olete kontrollinud, et makse on teie kontole laekunud.
- Hinnake tehingut
- Bitcoin vabastatakse automaatselt ostjale,



Nii ongi!



**Turvalisuse märkus ja näpunäited eduka tehingu tegemiseks:**




 - Jälgige ostja andmeid ja kontrollige, kas raha päritolu vastab Peach-s kirjeldatud päritolule Kui raha päritolu ei vasta teatatud päritolule, minge vestlusse ja avage vaidlus (pilt 39) ning saatke raha tagasi selle päritolule.
 - Järgige kollase kassi juhiseid.
 - Vastake kiiresti oma vastaspoole sõnumitele
 - olla ettevaatlik ostja suhtumise suhtes, eriti kui tegemist on vähese kogemusega profiiliga
 - Ärge kartke kasutada vahendusteenust, kui teil on probleem



### 2.b Kuidas müüa bitcoine: võta pakkumist



Samuti on võimalik vaadata ja valida ostupakkumisi. Peate olema eriti ettevaatlik, sest siin on kõige rohkem pettureid.



![Prendre une offre d'achat](assets/fr/15.webp)





- Klõpsake avalehel nupule "Müük" (pilt 40)
- Kasutage filtreid, et vaadata ja valida kõige atraktiivsemaid pakkumisi (pilt 41)



![vérification de la réputation](assets/fr/16.webp)





- enne kauplemisavalduse esitamist soovitame hinnata ostja profiili sobivust. Võite klõpsata pakkumisel ja seejärel kasutaja ID-l, et näha tema profiili. Näiteks pildil 42 esitatud pakkumist võiks pidada "riskantseks" (uus kasutaja, suhteliselt suur summa). "Risk", mida te selle pakkumise vastuvõtmisel võtate, on lihtsalt aja raiskamine, kui te ei tee seda viga, et vabastate bitcoinid, ilma et oleksite raha saanud. Bitcoine saab ikka hoiustada seifis.


Seevastu pildil 43 kujutatud kaupleja on pärit kogenud kauplejalt (pilt 44), kelle ajalugu ei ole vaidlustatud. Seega on see vähem riskantne pakkumine.



![Match avec vendeur](assets/fr/17.webp)





- Kui ostja nõustub teie taotlusega, viib rakendus teid pildile 34, kus saate jätkata kauplemist, nagu allpool kirjeldatud.




## Eelised ja puudused



### Peach eelised





- KYC ei ole nõutav**: Säilitab kasutaja konfidentsiaalsuse.
- Puudub juurdepääs pangaandmetele**: Peach ei pääse ligi teie pangarekvisiitidele ega identiteedile.
- Interface intuitiivne**: Lihtne kasutada edasijõudnud kasutajatele.
- Avatud lähtekood** : Lähtekood on avalik ja kogukonna poolt kontrollitav.



### Peach puudused





- Piiratud Liquidity**: Väiksem kauplemismaht kui rohkem väljakujunenud platvormidel.
- Regulatiivne risk** : Rakendust haldab Šveitsi ettevõte. Seetõttu kohaldatakse selle suhtes Šveitsi eeskirju, mis võivad areneda ja rakendust potentsiaalselt tsenseerida.



## Kasulikud ressursid





- Prantsuse selgitav video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Kiirkäsijuhend: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (ettevaatust petturitega, administraatorid ei kirjuta teile kunagi esmalt privaatsõnumit)