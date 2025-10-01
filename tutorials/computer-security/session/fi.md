---
name: Session
description: Lähetä salattuja viestejä, ei metatietoja
---
![cover](assets/cover.webp)



Session on vuonna 2020 luotu salattu viestisovellus, joka on suunniteltu tarjoamaan perinteistä viestinvälitystä korkeampi luottamuksellisuuden taso. Sen kehitti ensin *Oxen Privacy Tech Foundation*, sitten *Session Technology Foundation*.



Sessionilla on joitakin mielenkiintoisia teknisiä ominaisuuksia: viestien päästä päähän -salaus, hajautettu verkko, joka on organisoitu takaamaan käytettävyys ja redundanssi, sekä Torista inspiraationsa saanut sipulireititys. Toisin kuin WathsApp tai Signal, jotka vaativat puhelinnumeron rekisteröitymistä varten, Session ei pyydä mitään henkilökohtaisia tietoja (ei numeroa, ei sähköpostiosoitetta, vain pari kryptografista avainta).



Sessionin avulla voit lähettää viestejä, tiedostoja, ääniviestejä, äänipuheluita sekä jopa 100 jäsenen ryhmiä (ja yhteisöjä sen jälkeen) ja samalla minimoida metatietovuodot.



![Image](assets/fr/01.webp)



Istunto on suunnattu ennen kaikkea käyttäjille, joille luottamuksellisuus on ensisijaisen tärkeää. Tämä viestipalvelu on vakava vaihtoehto WhatsAppille, ja sen arkkitehtuuri on suunniteltu kestämään nykyaikaisia valvontamalleja.



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
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end-salaus*



## Asenna istuntosovellus



Istunto on saatavilla kaikilla alustoilla. Voit ladata sovelluksen suoraan puhelimesi sovelluskaupasta:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



Androidissa on myös mahdollista [asentaa APK:n kautta](https://github.com/session-foundation/session-android/releases).



Tässä ohjeessa keskitymme mobiiliversioon, mutta huomaa, että [tietokoneversiot ovat myös saatavilla](https://getsession.org/download) (MacOS, Linux ja Windows). Myöhemmin tarkastelemme, miten tili voidaan synkronoida useiden laitteiden välillä.



## Luo tili Sessionissa



Ensimmäisellä käynnistyskerralla napsauta "*Luo tili*".



![Image](assets/fr/02.webp)



Valitse profiilisi näyttönimi. Tämä voi olla salanimi tai oikea nimesi.



![Image](assets/fr/03.webp)



Tämän jälkeen sinun on valittava kahden ilmoituksenhallintatilan välillä:





- Nopea tila (**Firebase Cloud Messaging/Apple Push Notification Service**): voit vastaanottaa viesti-ilmoituksia lähes reaaliajassa Googlen tai Applen (järjestelmästäsi riippuen) tarjoamien ilmoituspalvelujen ansiosta. Jotta tämä toimisi, IP Address ja yksilöllinen ilmoitustunnus lähetetään Googlelle tai Applelle, ja istuntotilin tunnus rekisteröidään myös STF-palvelimelle (Torin kautta). Tässä tilassa metatietoja paljastuu (tosin vain vähän), mutta se ei vaaranna viestien sisältöä tai yhteystietoja, eikä todellista toimintaasi voida jäljittää. Tämä tila on siis tehokkaampi reagointikyvyn kannalta, mutta se on riippuvainen keskitetystä infrastruktuurista ja hieman tehottomampi luottamuksellisuuden kannalta.





- Hidas tila (**taustakysely**): istuntosovellus pysyy aktiivisena taustalla ja kyselee säännöllisesti verkosta uusia viestejä. Tämä toimintatapa takaa luottamuksellisemman tiedonsiirron kuin ensimmäinen toimintatapa, sillä tietoja ei välitetä kolmannen osapuolen palvelimille; Google, Apple tai STF-palvelimet eivät saa mitään tietoja. Toisaalta tässä tilassa on kaksi haittaa: ilmoitukset voivat viivästyä (jopa useita minuutteja), ja energiankulutus on yleensä suurempi, koska sovellus toimii taustalla.



![Image](assets/fr/04.webp)



Olet nyt yhteydessä istuntosovellukseen ja voit aloittaa viestien vaihdon.



![Image](assets/fr/05.webp)



## Tallenna istuntotilisi



Ennen kuin aloitat Sessionin käytön, sinun on ensin tallennettava tilisi, jotta voit palauttaa sen, jos menetät laitteesi. Tee tämä napsauttamalla "*Tallenna palautussalasana*" -kohdan vieressä olevaa "*Jatka*"-painiketta.



![Image](assets/fr/06.webp)



Istunto näyttää tämän jälkeen Mnemonic-lauseen. Kopioi se huolellisesti ja säilytä se turvallisessa paikassa. Tämä lauseke antaa täyden pääsyn Session-tilillesi, joten on tärkeää, ettet paljasta sitä. Tarvitset sitä päästäksesi tilillesi toisella laitteella, varsinkin jos nykyinen puhelimesi katoaa tai vaihdetaan.



![Image](assets/fr/07.webp)



Tämä lause toimii samalla tavalla kuin Bitcoin-salkuissa käytetyt Mnemonic-lauseet. Siksi suosittelen, että tutustut tähän toiseen opetusohjelmaan, jossa selitän parhaat käytännöt Mnemonic-lauseen tallentamiseen:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Huomaa**: Toisin kuin Bitcoin-salkuissa käytetyt Mnemonic-lauseet, Session-salkussa **jokainen sana on ehdottomasti tallennettava kokonaisuudessaan**. Neljä ensimmäistä kirjainta ei riitä!



## Istuntosovelluksen määrittäminen



Pääset sovellusasetuksiin napsauttamalla Interface:n vasemmassa yläkulmassa olevaa profiilikuvaasi. Täällä voit lisätä profiilikuvan.



![Image](assets/fr/08.webp)



"*Privacy*"-valikossa voit ottaa käyttöön tai poistaa käytöstä erilaisia ominaisuuksia (varo, jotkut niistä voivat paljastaa IP Address:n). Suosittelen myös "*Lock App*" -vaihtoehdon aktivoimista, joka edellyttää todennusta sovelluksen käyttämiseksi.



![Image](assets/fr/09.webp)



Valikossa "*Hälytys*" voit valita "*Nopea tila*" ja "*Hidas tila*" (katso oppaan aiemmat osat). Voit myös mukauttaa ilmoituksia mieltymystesi mukaan.



![Image](assets/fr/10.webp)



Mene lopuksi "*Appearance*"-valikkoon ja sovita Interface omaan makuusi. "*Palautussalasana*"-valikossa voit hakea Mnemonic-lauseesi, jos haluat tehdä uuden varmuuskopion.



![Image](assets/fr/11.webp)



## Viestien lähettäminen istunnon avulla



Jos haluat ottaa yhteyttä muihin henkilöihin, klikkaa etusivun "*+*"-painiketta.



![Image](assets/fr/12.webp)



Valittavana on useita vaihtoehtoja. Jos haluat luoda ryhmän tai liittyä siihen, valitse "*Luo ryhmä*" tai "*Liity yhteisöön*".



![Image](assets/fr/13.webp)



Jos haluat jonkun lisäävän sinut yhteystiedoksi, voit pyytää häntä skannaamaan istuntotunnuksesi QR-koodina.



![Image](assets/fr/14.webp)



Jos haluat lähettää kirjautumisesi etänä, klikkaa "*Kutsu ystävä*". Voit sitten kopioida istuntotunnuksesi ja lähettää sen toisen viestintäkanavan kautta. Voit myös hakea nämä tiedot napsauttamalla profiilikuvaasi etusivulta.



![Image](assets/fr/15.webp)



Jos sinulla on toisen henkilön istuntotunnus ja haluat lisätä sen, klikkaa "*Uusi viesti*".



![Image](assets/fr/16.webp)



Voit sitten liittää sen tunnisteen tekstiin tai skannata sen suoraan, jos sinulla on QR-koodi.



![Image](assets/fr/17.webp)



Lähetä sitten ensimmäinen viesti tälle henkilölle.



![Image](assets/fr/18.webp)



Kun henkilö hyväksyy pyyntösi, hänen käyttäjätunnuksensa ilmestyy näkyviin, ja voit keskustella hänen kanssaan vapaasti.



![Image](assets/fr/19.webp)



## Synkronoi työpöytäohjelmisto



Jos haluat synkronoida tilisi tietokoneellasi, sinun on asennettava ohjelmisto. [Lataa se viralliselta verkkosivustolta](https://getsession.org/download). Suosittelen tarkistamaan sen aitouden ja eheyden ennen asennusta.



![Image](assets/fr/20.webp)



Ensimmäisellä käynnistyskerralla napsauta "*Minulla on tili*".



![Image](assets/fr/21.webp)



Kirjoita Mnemonic-lauseesi ja jätä jokaisen sanan väliin välilyönti.



![Image](assets/fr/22.webp)



Voit nyt käyttää keskusteluja tietokoneeltasi.



![Image](assets/fr/23.webp)



Onneksi olkoon, olet nyt oppinut käyttämään Session-viestintää, joka on erinomainen vaihtoehto WathsAppille!



Suosittelen myös tätä toista opetusohjelmaa, jossa esittelen Threeman, toisen mielenkiintoisen vaihtoehdon viestisovelluksellesi:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74