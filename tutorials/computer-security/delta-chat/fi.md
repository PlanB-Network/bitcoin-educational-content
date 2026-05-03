---
name: Delta Chat
description: Käytännön opas hajautettuun viestinvälitystyökaluun
---

![image](assets/cover.webp)




## Johdanto - Chatin hallinta ja yksityisyys



Viime vuosina on puhuttu enenevässä määrin Chat Control -säädösehdotuksesta, jonka tarkoituksena on ottaa käyttöön yksityisviestien automaattinen skannaus suurimmilla viestintäalustoilla. Tavoitteena on torjua laitonta sisältöä, mutta ongelmana on, että tämä mekanismi merkitsisi itse asiassa massavalvontaa, joka heikentäisi päästä päähän -salausta ja siten kaikkien käyttäjien, ei vain rikoksentekijöiden, yksityisyyttä.



Todellinen vaara on, että chateista tulee valvottuja ympäristöjä, joissa jokainen viesti, kuva tai liitetiedosto voidaan tutkia ennen kuin se edes saavuttaa vastaanottajan. Tässä kohtaa on yksi mahdollinen ratkaisu: keskitetyistä alustoista on siirryttävä hajautettuihin viestijärjestelmiin, jotka eivät ole riippuvaisia yhdestä palveluntarjoajasta ja joita ei voida helposti valvoa.



Yksi tällainen ratkaisu esitellään tässä oppaassa: Delta Chat. Kypsä ja jo käyttökelpoinen työkalu.




## Miksi Delta Chat ja miten se toimii



Delta Chat on jo nyt erittäin hyvä viestiratkaisu jokapäiväiseen käyttöön: erittäin hyödyllinen keskusteluun ystävien, perheenjäsenten ja muiden ihmisten kanssa, aivan kuin WhatsAppin todellinen vastine.



Se on täysin sähköpostiin perustuva hajautettu viestijärjestelmä. Se hyödyntää periaatteessa perinteisen sähköpostin infrastruktuuria, mutta rakentaa sen päälle modernin pikaviestimen käyttöliittymän ja -kokemuksen. Ensi silmäyksellä tämä saattaa vaikuttaa hieman improvisoidulta, mutta se toimii itse asiassa erittäin hyvin ja on yllättävän vankka. Voit käyttää ChatMail-nimisiä erillisiä sähköpostipalvelimia, mutta se voi myös toimia saumattomasti tavallisten sähköpostipalvelimien kanssa. Tämä tarkoittaa, että voit halutessasi kirjautua sisään olemassa olevalla tilillä ilman, että sinun tarvitsee luoda mitään uutta.



Toinen kohokohta on tuki WebXDC:ille, jotka ovat pieniä verkkosovelluksia, joita voidaan käyttää suoraan keskusteluissa, kuten Telegram:n minisovelluksia. Tärkeä ero on, että näillä sovelluksilla ei ole Internet-yhteyttä, joten ne eivät voi seurata käyttäjää tai lähettää tietoja ulkoisesti.



Turvallisuuden kannalta Delta Chat käyttää todennettua päästä päähän -salausta, joka perustuu PGP:hen, mutta jossa on nykyaikaisia laajennuksia, joiden ansiosta se on suojatasoltaan verrattavissa Signal:een. Ainoa nykyinen puute on Perfect Forward Secrecy, mutta se on kehittyvä näkökohta.



Koska Delta Chat perustuu yksinomaan sähköpostiin, se välttää sen kokonaan:




- pakolliset puhelinnumerot
- Keskitetyt tunnukset
- yhteen palveluun liittyvät rekisteröinnit



Juuri tämä tekee tästä työkalusta erittäin vastustuskykyisen Chat Controlin kaltaisille invasiivisille asetuksille.




## Asennus



[Delta Chatin] (https://delta.chat/download) virallisilla verkkosivuilla voit siirtyä latausosioon. Linuxissa se on saatavilla kätevästi Flathubin kautta, mutta paketteja on myös Archille, NixOS:lle, Snap:lle ja itsenäisille versioille.



![image](assets/it/01.webp)



Se on saatavana myös seuraaviin tarkoituksiin:




- [F-Droid] (https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS] (https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- ja muita kauppoja...



Jos etsit opasta F-Droid:n asentamiseen, tämä opetusohjelma saattaa auttaa sinua:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Yksi erittäin tärkeä asia: työpöytäversiot eivät vaadi puhelinta. Toisin kuin WhatsAppissa tai SimpleX Chat:ssä, sinun ei tarvitse rekisteröityä ensin matkapuhelimesta. Voit luoda profiilisi suoraan tietokoneella tai siirtää sen toisesta laitteesta.




## Profiilin luominen



Kun sovellus on avattu, Delta Chat kysyy, haluatko luoda uuden profiilin vai käyttää olemassa olevaa.



![image](assets/it/02.webp)



Luomalla uuden profiilin voit syöttää:




- nimi
- kuva (valinnainen)



ChatMail-palvelinta ehdotetaan oletusarvoisesti, mutta se on mahdollista:




- valitse toinen ChatMail-palvelin
- käytä klassista sähköpostitiliä
- määrittää IMAP ja SMTP manuaalisesti
- rekisteröityä toisen käyttäjän kutsukoodilla



Muutaman sekunnin kuluttua profiili on valmis ja voit aloittaa sovelluksen käytön.



![image](assets/it/03.webp)




## Interface ja keskustelu



Käyttöliittymä on hyvin yksinkertainen ja suoraviivainen:




- Laiteviestit, jotka ovat paikallista viestintää
- Tallennetut viestit, jotka ovat samanlaisia kuin Telegram:ssä ja synkronoitavissa laitteiden välillä



![image](assets/it/04.webp)



Lisää yhteyshenkilö yksinkertaisesti:




- QR-koodin näyttäminen
- Skannaa toisen henkilön
- Kutsu linkin kautta (jaa kutsulinkki).



![image](assets/it/05.webp)



Kun yhteys on muodostettu, päästä päähän -salaus määritetään automaattisesti. Chatin käyttöliittymä on hyvin samanlainen kuin WhatsAppin:




- teksti- ja ääniviestit
- valokuvat, videot ja tiedostot
- vastaukset viesteihin
- reaktiot
- ponnahdusviestit
- mukautettavat ilmoitukset.



![image](assets/it/06.webp)



## WebXDC: sovellukset keskusteluissa:



Delta Chat mahdollistaa WebXDC:n eli keskusteluihin upotettujen pienten sovellusten käytön. Tässä on lyhyt luettelo hyödyllisimmistä tunnistetuista sovelluksista:




- tutkimukset
- piirustuspöydät
- tilapäiset yksityiset keskustelut
- pelit, joissa on jaetut chat-pisteet



Myös monimutkaisempia pelejä voidaan aloittaa, mikä osoittaa tämän työkalun joustavuuden.



![image](assets/it/07.webp)



## Ryhmät, kanavat ja lisäominaisuudet



Voit luoda ryhmiä, käyttää tarroja (erityisesti työpöydillä) ja aktivoimalla kokeiluvaihtoehdot jopa kanavia, jotka muistuttavat Telegram:n kanavia.



Lisäasetuksissa voit ottaa käyttöön:




- äänipuhelut (vielä kokeiluvaiheessa)
- kehittynyt sähköpostiprofiilin hallinta
- täydelliset varmuuskopiot.



![image](assets/it/08.webp)



## Monilaite ja varmuuskopiointi



Delta Chat tukee täysin useita laitteita:




- voit lisätä toisen laitteen QR-koodilla
- voit suorittaa täyden siirron varmuuskopioinnin kautta.



Löydät chatit, ryhmät ja koko historian muutamassa sekunnissa uudelleen ilman riippuvuutta keskitetystä palvelimesta.



![image](assets/it/09.webp)




## Päätelmä



Aikana, jolloin yksityisen viestinnän valvonnasta puhutaan yhä enemmän, Delta Chat tarjoaa konkreettisen vastauksen: hajautettua, salattua viestinvälitystä, joka on todella käyttökelpoista joka päivä.



Se on ratkaisu, joka kaikista kokeilemistani ratkaisuista on vakuuttanut minut eniten yksinkertaisuutensa, yksityisyytensä ja vapautensa puolesta. Jos haluat, voit ottaa minuun yhteyttä myös Delta Chatissa seuraavan [kutsulinkki](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats) kautta



Jos pidit tästä oppaasta, voit tukea minua lahjoittamalla ja jättämällä peukalon ylös. Ja muista: vain käyttämällä ja tutkimalla Delta Chatia sekä mobiililaitteella että työpöydällä voit todella tutustua sen täyteen toiminnallisuuteen.



Seuraavaan kertaan.