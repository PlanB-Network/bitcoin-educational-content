---
name: Virsik
description: Täielik juhend Peach'i kasutamise ja bitcoinide P2P vahetamise kohta
---
![cover](assets/cover.webp)

![peach](https://youtu.be/ziwhv9KqVkM)

## Sissejuhatus

KYC-vabad peer-to-peer (P2P) börsid on kasutajate konfidentsiaalsuse ja finantsautonoomia säilitamiseks hädavajalikud. Need võimaldavad otsetehinguid üksikisikute vahel ilma isikusamasuse kontrollimiseta, mis on oluline nende jaoks, kes hindavad privaatsust. Teoreetiliste mõistete põhjalikumaks mõistmiseks vaadake kursust BTC204:

https://planb.network/courses/btc204
### 1. Mis on virsik?

Peach on P2P-vahetusplatvorm, mis võimaldab kasutajatel osta ja müüa bitcoine ilma KYC-ta. See pakub intuitiivset kasutajaliidest ja täiustatud turvaelemente. Võrreldes teiste lahendustega, nagu Bisq, HodlHodl ja Robosat, paistab Peach silma oma kasutusmugavuse ja madalate tasude poolest.

### 2. Privaatsus ja andmete kogumine

**Milliseid andmeid kogub Peach?

Peach püüab salvestada oma kasutajate kohta võimalikult vähe andmeid. Siin on ülevaade tema serveritesse salvestatud andmetest:


- Teie unikaalse rakenduse identifikaatori (AdID) hash
- Teie makseandmete hash
- Teie krüpteeritud vestlused
- Tehinguandmed, et tagada, et anonüümsed kasutajad ei ületa kauplemislimiiti (kasutatud makseviiside liigid, ostu- ja müügisummad)
- Aadressid, mida kasutatakse deposiitkontolt saatmiseks ja vastuvõtmiseks
- Kasutusandmed (Firebase & Google Analytics), ainult teie nõusolekul

Meeldetuletuseks: hash on andmed, mis on sarnaselt krüpteerimisele muudetud tundmatuseni. Samad andmed annavad alati ühe ja sama hashi, mis võimaldab tuvastada duplikaate ilma algandmeid tundmata.

*Lisateavet hashimise kohta saate sellest kursusest:*

https://planb.network/courses/cyp201
**Kes saab minu makseandmeid näha?


- Ainult teie vastaspool näeb teie makseandmeid
- Andmed edastatakse Peach serverite kaudu, kuid need on täielikult krüpteeritud otsast lõpuni
- Vaidluse korral on teie makse üksikasjad ja vestluste ajalugu määratud Peach vahendajale nähtavad

## Paigaldamine ja konfigureerimine

### 1. Installige rakendus Peach

![Installation de Peach](assets/fr/01.webp)


- Lae taotlus alla [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/).
- Järgige seadme paigaldusjuhiseid.
- Paigaldamise ajal palutakse teil valida, kas soovite jagada teatud andmeid, et täiustada Peach rakendust (pilt 1)
- Järgmisel ekraanil (pilt 2) on kaks võimalust:
 - Kui olete uus kasutaja, klõpsake "Uus kasutaja", et luua uus profiil
 - Kui teil on juba konto, kasutage "Restore", et taastada oma olemasolev profiil
- Kui teil on soovituskood, saate selle sisestada siia.
- Olemasoleva konto taastamiseks (pilt 3) on vaja :
 - Teie varundatud fail
 - Parool selle faili dekrüpteerimiseks

### 2. Ülevaade põhiekraanidest

Peach'i rakendus on korraldatud nelja peamise ekraani ümber, millele pääseb ligi alumisest navigatsiooniribast:

![Navigation dans l'application](assets/fr/02.webp)


- Avaleht** : Peakuva bitcoinide ostmiseks ja müümiseks. Siin saate luua uusi tehinguid ja pääseda ligi olemasolevatele pakkumistele.
- Rahakott**: Teie integreeritud Bitcoin rahakott, mis võimaldab teil :
 - Kontrollige oma saldot
 - Bitcoinide vastuvõtmine
 - Bitcoinide saatmine
 - Vaadake oma tehingute ajalugu
- Ametid** : Teie kaubanduse halduskeskus, kust leiate :
 - Teie praegused tehingud
 - Teie vahetuste täielik ajalugu
 - Iga tehingu staatus
- Seaded** : Teie konto konfiguratsiooni keskus :
 - Halda oma makseviise
 - Konfigureerige oma varukoopiaid
 - Kohandage oma eelistusi
 - Juurdepääs abile ja toetusele

### 3. Konfigureerige oma makseviisid

![Accès aux paramètres de paiement](assets/fr/03.webp)

Juurdepääs makseviisidele vahekaardil Seaded (pilt 8)

**Online maksed

![Configuration des paiements en ligne](assets/fr/04.webp)


- Uue makseviisi lisamiseks klõpsake nupule
- Valige oma valuuta
- Valige oma eelistatud makseviis

*Saadaolevad makseviisid:*

***Pangaülekanded saadaval: ***


- SEPA (standard- või kiirkorras)
- Täitke oma SEPA pangaandmed

***Online rahakotid aktsepteeritud :***


- Olenevalt riigist on saadaval mitu võimalust (Revolut, Paypal, Wise, Strike jne)
- Järgige juhiseid oma sisselogimisandmete lisamiseks

***Kinkekaart, mida saab kasutada :***


- Amazon
- Sisestage kaardi väljaandjariik ja muud vajalikud andmed

***Maksevõimalused riigisiseselt:***

Riigipõhised maksesüsteemid :


- Satispay (Itaalia)
- MB Way (Portugal)
- Bizum (Hispaania)
- Kiiremad maksed (Ühendkuningriik)

***Personaalsed maksed:***

![Configuration des paiements en personne](assets/fr/05.webp)


- Valige "Meetup"
- Seejärel valige oma kohtumine nimekirjast

### Kasutusjuhend


- Saate luua mitu makseviisi samaaegselt
- Mida rohkem meetodeid lisate, seda laiemad on pakkumised, millele teil on juurdepääs
- Palun kontrollige enne registreerimist, et teie andmed oleksid õiged
- Saate oma makseviise igal ajal muuta või kustutada

**Turvalisuse märkus**: Teie makseteave on krüpteeritud ja seda jagatakse ainult teie vahetuspartneriga tehingu ajal.

### 4. Kuidas kindlustada oma portfelli

**Pärsikakonto mõistmine

Peach-konto ei ole traditsiooniline sisselogimise ja parooliga konto. See on fail, mida hoitakse lokaalselt teie telefonis, mis tähendab, et Peach ei pea teie andmeid säilitama ega teadma teie identiteeti: teie olete kontrolli all. See fail sisaldab kõiki teie andmeid, alates bitcoini rahakoti võtmetest kuni maksete üksikasjadeni.

Selline lähenemisviis tagab suurema konfidentsiaalsuse, kuid eeldab ka suuremat vastutust. Telefoni kaotamine ilma varukoopiana tähendab juurdepääsu kaotamist teie Peach-kontole ja rahalistele vahenditele. Seega on väga oluline teha sellest failist varukoopia ja kaitsta seda tugeva parooliga.

**Loo oma varukoopiaid**

![Accéder aux sauvegardes](assets/fr/13.webp)


- Juurdepääs seadetele avakuva all paremal oleval vahekaardil
- Valige seadete menüüst valik "varukoopiad"

![Processus de sauvegarde](assets/fr/06.webp)

Saadaval on kahte tüüpi varukoopia:

**Konto faili salvestamine (pilt 14)**


- Klõpsake nuppu "Loo uus varukoopia"
- Looge tugev parool, et krüpteerida oma varundusfaili
- Hoidke seda faili turvalises kohas

Failide varukoopia taastab teie täieliku Peach'i konto, sealhulgas :


- Teie portfell
- Teie makseviisid
- Vestluse ajalugu
- Makseandmed
- Tehingute ajalugu koos vastaspoole andmetega

**Tagastamislause salvestamine (pilt 15)**


- Järgige juhiseid, et kuvada oma taastamislauset
- Kirjuta sõnad hoolikalt õiges järjekorras üles
- Hoidke seda varukoopiat turvalises kohas, mis ideaalis erineb kontofailist

Taastamislause taastab ainult :


- Juurdepääs oma kontole
- Teie bitcoin raha

Te kaotate :


- Vestluse ajalugu
- Makseandmed
- Vastaspoole andmed tehinguajaloos

Optimaalse turvalisuse tagamiseks soovitame teil teha mõlemat tüüpi varukoopiaid.

## Bitcoinide ostmine ja müümine

### 1. Kuidas osta Bitcoine

![Création et vue des offres](assets/fr/07.webp)


- Vajutage avakuval nupule "Osta" (pilt 16)
- Konfigureerige oma ostu vastavalt oma eelistustele (pilt 17)
- Sirvige saadaval olevate pakkumiste nimekirja (pilt 18)

![Sélection et confirmation d'achat](assets/fr/08.webp)


- Valige teile sobiv pakkumine (pilt 19)
- Tehke makse kokkulepitud viisil
- Kinnitage makse rakenduses ja hinnake tehingut (pilt 20)

![Réception des bitcoins](assets/fr/09.webp)


- Jälgige oma tehingu staatust
- Kontrollige bitcoinide kättesaamise kinnitust
- Rahalised vahendid on saadaval teie virsikuportfellis

### 2. Kuidas müüa Bitcoine

![Création d'un ordre de vente](assets/fr/10.webp)


- Konfigureerige oma müügipakkumine (pilt 24)
- Rahastage tehingut, saates bitcoinid ettenähtud aadressile (pilt 25)
- Oodake tehingu kinnitust (pilt 26)
- Teie pakkumine on nüüd ostjatele nähtav (pilt 27)

![Attente du paiement](assets/fr/11.webp)


- Jälgige oma pakkumise staatust
- Oodake ostjalt maksekinnitust
- Kontrollida tehingu üksikasju

![Finalisation de la vente](assets/fr/12.webp)


- Kontrollida makse staatust
- Kinnitage makse laekumist
- Hinnake tehingut
- Bitcoins vabastatakse ostjale automaatselt

**Nipid edukaks tehinguks**


- Vastake kiiresti oma vastaspoole sõnumitele
- Kontrollige hoolikalt makse üksikasju
- Ärge kartke kasutada vahendusteenust, kui teil on probleem

**Turvalisuse märkus**: Ära kunagi kinnita makse kättesaamist enne, kui oled veendunud, et makse on sinu kontole laekunud.

## Eelised ja puudused

### Virsiku eelised


- KYC ei ole nõutav**: Säilitab kasutaja konfidentsiaalsuse.
- Puudub juurdepääs pangaandmetele**: Peachil ei ole juurdepääsu teie pangaandmetele ega teie identiteedile.
- Intuitiivne kasutajaliides**: Lihtne kasutada ka edasijõudnud kasutajatele.
- Avatud lähtekood** : Lähtekood on avalik ja kogukonna poolt kontrollitav.

### Virsiku puudused


- Piiratud likviidsus**: Väiksem kauplemismaht kui väljakujunenud platvormidel.
- Regulatiivne risk** : Rakendust haldab Šveitsi ettevõte. Seetõttu kohaldatakse selle suhtes Šveitsi eeskirju, mis võivad areneda ja rakendust potentsiaalselt tsenseerida.

## Kasulikud ressursid


- Prantsuse selgitav video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Kiirkäsijuhend: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)