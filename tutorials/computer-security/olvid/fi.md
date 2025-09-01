---
name: Olvid
description: Yksityisviestit kaikille
---
![cover](assets/cover.webp)



Olvid on vuonna 2019 lanseerattu ranskalainen pikaviestisovellus, joka on suunniteltu tarjoamaan korkeatasoista turvallisuutta yksityisyydestä tinkimättä. Toisin kuin WhatsApp tai Signal, Olvid ei pyydä rekisteröitymisen yhteydessä mitään henkilökohtaisia tietoja: ei puhelinnumeroa, ei sähköpostia, ei mitään. Käyttäjien välinen tunnistus perustuu avainten Exchange:een, eikä käytössä ole hakemistopalvelinta tai jaettua Address-kirjaa.



Kaikki viestit salataan päästä päähän käyttämällä alkuperäistä salausprotokollaa, joka on suunniteltu suojaamaan myös metatiedot: kukaan ei tiedä, kenelle puhut tai milloin. Asiakaskoodi on avointa lähdekoodia, mutta keskitetty palvelin, jota käytetään salattujen viestien reitittämiseen, on patentoitu ja sijaitsee AWS:ssä.

Olvidin turvallisuusmalli perustuu olennaiseen periaatteeseen: digitaalisten identiteettien luomisessa ei käytetä lainkaan luotettuja kolmansia osapuolia. Toisin kuin useimmat salatut viestintäsovellukset, jotka tukeutuvat keskitettyyn hakemistoon käyttäjien identiteettien hallinnassa, Olvid ei ole riippuvainen yhdestäkään keskitetystä infrastruktuurista viestinnän eheyden takaamiseksi. Tämä arkkitehtuuri poistaa siten hakemiston vaarantumiseen liittyvät riskit.

Olvid käyttää kuitenkin keskitettyä viestien jakelupalvelinta, mutta se on tiukasti rajattu logistiseen rooliin: se huolehtii salattujen viestien asynkronisesta välityksestä. Palvelin ei osallistu salaukseen, eikä tunne käyttäjien todellisia henkilöllisyyksiä tai viestien sisältöä tai metatietoja (paitsi vastaanottajan julkista avainta, joka tarvitaan reititykseen). Siksi palvelinta voidaan pitää oletusarvoisesti vihamielisenä vaarantamatta kokonaisuuden turvallisuutta. Vaikka se joutuisi hyökkäyksen kohteeksi, se ei antaisi pääsyä viestien sisältöön. Olvid siis keskittää viestien jakelun (tehokkuuden ja palvelun laadun vuoksi), mutta varmistaa turvallisuuden, joka on riippumaton tästä infrastruktuurista.


Olvid tarjoaa ilmaisen version ja tilausversion, jonka hinta on 4,99 euroa kuukaudessa. Ilmaisversio tarjoaa täydet toiminnot lukuun ottamatta ääni- ja videopuheluiden soittamista (vaikka niiden vastaanottaminen on mahdollista), eikä se mahdollista tilin synkronointia useiden laitteiden välillä. Jos siis aiot käyttää yksinomaan älypuhelintasi, eikä sinun tarvitse soittaa puheluita, Olvid on erinomainen ratkaisu.



Olvid on Ranskan kyberturvallisuusviranomaisen ANSSI:n sertifioima. Tämä sovellus on erinomainen vaihtoehto perinteisille viestipalveluille (WhatsApp, Facebook Messenger, WeChat...) niille, jotka etsivät yksityisyyttä säilyttäen samalla helppokäyttöisyyden.


| Sovellus             | E2EE 1:1         | E2EE ryhmät      | Anonyymi rekisteröinti | Avoimen lähdekoodin asiakaslisenssi | Avoimen lähdekoodin palvelinlisenssi | Hajautettu palvelin     | Luomisvuosi |
| -------------------- | ---------------- | ---------------- | ---------------------- | ----------------------------------- | ------------------------------------ | ----------------------- | ----------- |
| WhatsApp             | ✅                | ✅                | ❌                      | ❌                                   | ❌                                    | ❌                       | 2009        |
| WeChat               | ❌                | ❌                | ❌                      | ❌                                   | ❌                                    | ❌                       | 2011        |
| Facebook Messenger   | ✅                | 🟡 (valinnainen) | ❌                      | ❌                                   | ❌                                    | ❌                       | 2011        |
| Telegram             | 🟡 (valinnainen) | ❌                | 🟡                     | ✅                                   | ❌                                    | ❌                       | 2013        |
| LINE                 | ✅                | ✅                | ❌                      | ❌                                   | ❌                                    | ❌                       | 2011        |
| Signal               | ✅                | ✅                | ❌                      | ✅                                   | ✅                                    | ❌                       | 2014        |
| Threema              | ✅                | ✅                | ✅                      | ✅                                   | ❌                                    | ❌                       | 2012        |
| Element (Matrix)     | ✅                | ✅                | ✅                      | ✅                                   | ✅                                    | 🟡 (federoitu)          | 2016        |
| Delta Chat           | ✅                | ✅                | ✅                      | ✅                                   | N/A                                  | 🟡 (sähköpostin kautta) | 2017        |
| Conversations (XMPP) | ✅                | ✅                | ✅                      | ✅                                   | ✅                                    | 🟡 (federoitu)          | 2014        |
| Session              | ✅                | ✅                | ✅                      | ✅                                   | ✅                                    | ✅                       | 2020        |
| SimpleX              | ✅                | ✅                | ✅                      | ✅                                   | ✅                                    | ✅                       | 2021        |
| **Olvid**            | **✅**            | **✅**            | **✅**                  | **✅**                               | **❌**                                | 🟡(ei hakemistoa)       | **2019**    |
| Keet                 | ✅                | ✅                | ✅                      | ❌                                   | N/A                                  | ✅                       | 2022        |
| Jami                 | ✅                | ✅                | ✅                      | ✅                                   | N/A                                  | ✅                       | 2005        |
| Briar                | ✅                | ✅                | ✅                      | ✅                                   | N/A                                  | ✅                       | 2018        |
| Tox                  | ✅                | ✅                | ✅                      | ✅                                   | N/A                                  | ✅                       | 2013        |

*E2EE = End-to-end-salaus*



## Asenna Olvid-sovellus



Olvid on saatavilla kaikilla alustoilla. Voit ladata sovelluksen suoraan puhelimesi sovelluskaupasta:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



Androidissa on myös mahdollista [asentaa APK:n kautta](https://www.olvid.io/download/).



Tässä ohjeessa keskitymme mobiiliversioon, mutta huomaa, että [tietokoneversiot ovat myös saatavilla](https://www.olvid.io/download/) (MacOS, Linux ja Windows). Jos valitset maksullisen version, voit synkronoida tilisi useilla laitteilla.



![Image](assets/fr/01.webp)



## Luo tili Olvidissa



Kun käynnistät sovelluksen ensimmäistä kertaa, napsauta "*Olen uusi käyttäjä*" -painiketta.



![Image](assets/fr/02.webp)



Valitse lempinimi tai anna etu- ja sukunimesi.



![Image](assets/fr/03.webp)



Lisää profiilikuva.



![Image](assets/fr/04.webp)



Tilisi on nyt luotu.



![Image](assets/fr/05.webp)



Jotta estät Olvid-tilisi käytön menettämisen, suosittelemme automaattisten varmuuskopioiden käyttöönottoa. Avaa asetukset napsauttamalla Interface:n oikeassa yläkulmassa olevia kolmea pistettä ja valitse sitten "*Asetukset*".

⚠️ **Huomio**: Olvid-version 3.7:stä lähtien profiiliesi ja yhteystietojesi varmuuskopiointimenettelyt on korvattu uudella. Tämä opas esittää vielä vanhan version. Voit tutustua uuteen versioon heidän FAQ:ssaan: [💾 Profiiliesi varmuuskopiointi](https://www.olvid.io/faq/sauvegarder-vos-profils/)

![Image](assets/fr/06.webp)



Siirry valikkoon "*Tallenna näppäimet ja yhteystiedot*".



![Image](assets/fr/07.webp)



Napsauta sitten "*generate varmuuskopioavain*". Tämä avain salaa varmuuskopiot. Jos sinun on palautettava tilisi toisella laitteella eikä sinulla ole enää pääsyä siihen, tarvitset sekä varmuuskopion että tämän avaimen sen salauksen purkamiseen.



![Image](assets/fr/08.webp)



Säilytä tämä avain turvallisessa paikassa. Voit myös tehdä paperikopion.



![Image](assets/fr/09.webp)



Voit sitten valita, haluatko luoda paikallisen varmuuskopion vai automaattisen varmuuskopion pilvipalveluun. Jälkimmäinen vaihtoehto on erittäin suositeltava, jotta voit taata pääsyn Olvid-tiliisi kaikissa olosuhteissa, vaikka kadottaisit puhelimesi.



![Image](assets/fr/10.webp)



Varmista, että "*Automaattisen varmuuskopioinnin ottaminen käyttöön*" -vaihtoehto on valittuna.



![Image](assets/fr/11.webp)



Voit myös tutustua muihin käytettävissä oleviin asetuksiin, joilla voit mukauttaa sovelluksen tarpeittesi mukaiseksi.



![Image](assets/fr/12.webp)



## Viestien lähettäminen Olvidilla



Jotta voit lähettää viestejä, sinun on ensin lisättävä yhteystietoja. Napsauta etusivulta sinistä "*+*"-painiketta.



![Image](assets/fr/13.webp)



Olvid näyttää sitten käyttäjätunnuksesi. Voit sitten välittää sen niille ihmisille, joiden kanssa haluat viestiä, jotta he voivat lisätä sinut yhteystiedoksi.



Voit lisätä henkilön skannaamalla hänen henkilöllisyystodistuksensa kameralla tai liittämällä sen manuaalisesti napsauttamalla kolmea pientä pistettä oikeassa yläkulmassa.



![Image](assets/fr/14.webp)



Kun tunnus on skannattu, voit joko pyytää yhteyshenkilöäsi skannaamaan näytettävän QR-koodin tai lähettää hänelle etäyhteyspyynnön napsauttamalla "*Edän yhteyshenkilö*".



![Image](assets/fr/15.webp)



Yhteys on nyt muodostettu.



![Image](assets/fr/16.webp)



Voit nyt aloittaa viestien ja muun sisällön vaihdon kirjeenvaihtajasi kanssa!



![Image](assets/fr/17.webp)



Etusivulta löydät kaikki keskustelut.



![Image](assets/fr/18.webp)



Toinen välilehti sisältää kaikki yhteystietosi.



![Image](assets/fr/19.webp)



Voit myös luoda ryhmäkeskusteluja.



![Image](assets/fr/20.webp)



Onneksi olkoon, olet nyt vauhdissa Olvid-viestien käytössä, joka on loistava vaihtoehto WathsAppille! Jos löysit tämän opetusohjelman hyödylliseksi, olisin hyvin kiitollinen, jos jättäisit Green peukalon alle. Voit vapaasti jakaa tätä opetusohjelmaa sosiaalisissa verkostoissa. Kiitos paljon!



Suosittelen myös tätä toista opetusohjelmaa, jossa esittelen sinulle Proton Mailin, joka on paljon yksityisyydensuojaystävällisempi vaihtoehto Gmailille:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2