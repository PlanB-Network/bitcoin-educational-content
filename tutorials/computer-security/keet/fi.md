---
name: Keet
description: Vertaisverkkokeskustelu
---
![cover](assets/cover.webp)



Keet on pikaviestisovellus, joka on suunniteltu toimimaan ilman palvelimia. Holepunchin (Tetherin ja Bitfinexin rahoittama yritys) vuonna 2022 lanseeraama sovellus perustuu täysin vertaisverkkoon, ja siinä on radikaalisti hajautettu lähestymistapa: viestit, puhelut ja tiedostot vaihdetaan suoraan käyttäjien välillä ilman välikäsiä.



Keet salaa kaiken viestinnän päästä päähän eikä pyydä henkilötietoja. Rekisteröityminen on anonyymiä, eikä puhelinnumeroa tai sähköpostia tarvita. Tekstiviestien vaihtamisen lisäksi Keet tarjoaa erittäin laadukkaita videopuheluita sekä rajoittamatonta tiedostojen jakamista. Sovellusta voidaan siis käyttää hybridinä sekä henkilökohtaiseen että ammatilliseen käyttöön.



![Image](assets/fr/01.webp)



Tällä hetkellä (huhtikuussa 2025) Keet ei ole täysin avointa lähdekoodia. Osa lähdekoodista on saatavilla [Holepunchin GitHub-repositoriossa](https://github.com/holepunchto), erityisesti kryptografiset ja verkkokomponentit, mutta asiakas Interface ei vielä ole. Holepunch on kuitenkin ilmoittanut aikovansa tehdä koko sovelluksesta lopulta avoimen lähdekoodin. Riippuen siitä, milloin löydät tämän opetusohjelman, tämä on ehkä jo tehty.




| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| **Keet**             | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end-salaus*



## Asenna Keet



Keet on saatavilla kaikilla alustoilla. Voit ladata sovelluksen suoraan puhelimesi sovelluskaupasta:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



Androidissa on myös mahdollista [asentaa APK:n kautta](https://github.com/holepunchto/keet-mobile-releases/releases).



Tässä ohjeessa keskitymme mobiiliversioon, mutta huomaa, että [tietokoneversiot ovat myös saatavilla](https://keet.io/) (MacOS, Linux ja Windows). On myös mahdollista synkronoida tilisi useilla laitteilla.



## Luo tili Keetissä



Ensimmäisellä käynnistyskerralla voit jättää esittelynäytöt huomiotta.



![Image](assets/fr/02.webp)



Napsauta "*Olen uusi käyttäjä*" -painiketta.



![Image](assets/fr/03.webp)



Hyväksy käyttöehdot ja napsauta sitten "*Pika-asennus*".



![Image](assets/fr/04.webp)



Valitse nimi tai lempinimi ja napsauta sitten "*Valmis asetukset*".



![Image](assets/fr/05.webp)



Profiilisi on nyt luotu. Klikkaa "*Viimeistele asetukset*" uudelleen viimeistelläksesi.



![Image](assets/fr/06.webp)



Voit muokata profiiliasi milloin tahansa "*Profiili*"-välilehdeltä.



## Tallenna Keet-tilisi



Ensimmäinen asia, jonka voit tehdä uudella Keet-tililläsi, on tallentaa palautuslauseesi. Tämä on 24 sanan sarja, jonka avulla voit palauttaa pääsyn tilillesi, jos laite katoaa tai vaihtuu. Tämä lauseke antaa täyden pääsyn tiliisi kenelle tahansa, joka tietää sen, joten on tärkeää tehdä luotettava varmuuskopio eikä koskaan paljastaa sitä.



Tee tämä napsauttamalla Interface:n oikeassa alakulmassa olevaa "*Profiili*"-välilehteä.



![Image](assets/fr/07.webp)



Siirry sitten "*Asetukset*"-valikkoon.



![Image](assets/fr/08.webp)



Valitse "*Turva ja tietosuoja*".



![Image](assets/fr/09.webp)



Napsauta sitten "*Palautuslause*".



![Image](assets/fr/10.webp)



Paina "*View phrase*" -painiketta näyttääksesi palautuslauseesi. Kopioi se huolellisesti ja säilytä se turvallisessa paikassa.



![Image](assets/fr/11.webp)



## Viestien lähettäminen Keetillä



Jotta voit kommunikoida Keetissä, sinun on luotava "*Rooms*". Tee tämä klikkaamalla Interface:n oikeassa yläkulmassa olevaa kynäkuvaketta.



![Image](assets/fr/12.webp)



Valitse "*Uusi ryhmäkeskustelu*".



![Image](assets/fr/13.webp)



Valitse nimi ja kuvaus "*huoneelle*" ja napsauta sitten "*Luo ryhmäkeskustelu*".



![Image](assets/fr/14.webp)



"*huone*" on nyt luotu. Kutsu osallistujia klikkaamalla oikeassa yläkulmassa olevaa "*+*"-kuvaketta.



![Image](assets/fr/15.webp)



Määritä oikeudet, jotka myönnät uusille jäsenille kutsulinkin kautta, sekä linkin voimassaoloaika. Napsauta sitten "*generate invite*".



![Image](assets/fr/16.webp)



Keet lähettää generate:lle linkin, jonka kautta voit liittyä "*huoneeseesi*". Voit joko kopioida sen ja jakaa sen tai antaa sen QR-koodin skannattavaksi niille ihmisille, jotka haluat kutsua.



![Image](assets/fr/17.webp)



Voit nyt aloittaa viestien ja multimediatiedostojen vaihdon. Voit käynnistää puhelun napsauttamalla oikeassa yläkulmassa olevaa puhelinkuvaketta.



![Image](assets/fr/18.webp)



Tästä ryhmästä voit myös lähettää yksityisviestejä tietylle jäsenelle. Napsauta ryhmän profiilikuvaa ja valitse sitten haluamasi jäsen "*Jäsenet*"-osiosta.



![Image](assets/fr/19.webp)



Napsauta "*Lähetä DM-pyyntö*" -painiketta ja kirjoita viestisi.



![Image](assets/fr/20.webp)



Kun DM-pyyntö on hyväksytty, löydät tämän yhteyshenkilön etusivulta, jossa voit keskustella hänen kanssaan yksityisesti.



![Image](assets/fr/21.webp)



## Synkronoi tilisi useilla laitteilla



Nyt kun osaat käyttää Keetiä ja sinulla on tili, voit synkronoida sen myös toiseen laitteeseen, kuten tietokoneeseen. Voit tehdä tämän avaamalla sovelluksen matkapuhelimessasi, napsauttamalla sitten "*Profiili*" ja siirtymällä "*Asetukset*".



![Image](assets/fr/22.webp)



Siirry sitten "*Minut laitteet*" -valikkoon.



![Image](assets/fr/23.webp)



Napsauta "*Lisää laite*". Keet generate antaa linkin uuden laitteen synkronoimiseksi. Kopioi tämä linkki.



![Image](assets/fr/24.webp)



Asenna Keet toiseen laitteeseesi. Valitse aloitusnäytöltä "*Olen nykyinen käyttäjä*" -vaihtoehto.



![Image](assets/fr/25.webp)



Napsauta sitten "*Link device*".



![Image](assets/fr/26.webp)



Liitä ensimmäisen laitteen antama linkki ja napsauta sitten "*Aloita synkronointi*".



![Image](assets/fr/27.webp)



Hyväksy yhteys ensimmäisessä laitteessa napsauttamalla "*Vahvista linkkilaitteet*".



![Image](assets/fr/28.webp)



Viimeistele prosessi toisella laitteella napsauttamalla "*Link devices*".



![Image](assets/fr/29.webp)



Pääset nyt käsiksi kaikkiin "*huoneeseesi*" ja keskusteluihisi tästä uudesta laitteesta.



![Image](assets/fr/30.webp)



Onneksi olkoon, olet nyt vauhdissa Keet-viestien käytössä, joka on loistava vaihtoehto WathsAppille! Jos löysit tämän opetusohjelman hyödylliseksi, olisin hyvin kiitollinen, jos jättäisit Green peukalon alle. Voit vapaasti jakaa tätä opetusohjelmaa sosiaalisissa verkostoissa. Kiitos paljon!



Suosittelen myös tätä toista opetusohjelmaa, jossa esittelen sinulle Proton Mailin, joka on paljon yksityisyydensuojaystävällisempi vaihtoehto Gmailille :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2