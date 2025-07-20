---
name: Tox
description: Avaa keskustelut ilman välikäsiä hajautetussa Tox-protokollassa
---
![cover](assets/cover.webp)



Loppuun asti tapahtuva salaus on monien viestisovellusten, kuten WhatsAppin ja Telegramin, tarjoama palvelu. Salaus tarkoittaa tässä sitä, että ennen kuin lähettäjä lähettää viestin, se suojataan kryptografisella lukolla, johon vain vastaanottajalla on avain. Tänään lähdemme tutustumaan täysin hajautettuun, päästä päähän salattuun viestisovellukseen, joka perustuu Blockchain:n kaltaisiin periaatteisiin ja tarjoaa turvallista, päästä päähän salattua viestintää ilman välikäsiä: Tox Chat.



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
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end-salaus*



## Mikä on Tox?



Tox on ilmainen (avoimen lähdekoodin), hajautettu viestintäprotokolla, joka käyttää *Networking and Cryptography Library* (NaCl) -tekniikkaa ja salausalgoritmien yhdistelmiä varmistaakseen käyttäjiensä turvallisuuden ja luottamuksellisuuden. Toxin avulla voit Exchange-tekstiviestejä, soittaa ääni- ja videopuheluita, jakaa tiedostoja ja näytön ystävien kanssa turvallisesti, hajautetusti ja ilman välikäsiä.



Tox-protokollan käyttämä teknologia muistuttaa vertaisverkkoja, kuten lohkoketjuja, mikä suosii protokollan infrastruktuurin hajauttamista. Toisin kuin sosiaaliset verkostot ja päästä päähän salatut viestisovellukset, Tox Chat -sovellus perustuu hajautettuun protokollaan, jossa ei ole keskuspalvelinta. Kaikki käyttäjät kommunikoivat välittäjävapaassa, sensuurin kestävässä vertaisverkossa. Viestintää varten kukin käyttäjä tunnistetaan yksilöllisellä tunnisteella (ToxID), joka saadaan hänen julkisesta avaimestaan, joka tallennetaan hajautettuun Hash -taulukkoon.



## Liity Toxiin



Voit käyttää Tox-protokollaa pikaviestiohjelmalla, jonka voit ladata [Tox Chat -sivustolta](https://tox.chat).



![download](assets/fr/01.webp)



Käyttöjärjestelmästäsi riippuen voit ladata ja asentaa Tox-asiakkaan, joka vastaa :





- aTox: [aTox](https://github.com/evilcorpltd/aTox), Kotlin-kielellä kirjoitettu Tox-asiakasohjelma, joka on saatavilla vain Androidissa



![aTox](assets/fr/02.webp)





- qTox: Qt Frameworkiin (C++) perustuva [avoimen lähdekoodin](https://github.com/TokTok/qTox) Tox-asiakasohjelma, joka on saatavilla Windowsille, Linuxille ja MacOsille.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) on C-kielellä kirjoitettu Tox-asiakasohjelma, joka toimii järjestelmissä, joissa on komentoriviliittymä.



![Toxic](assets/fr/04.webp)



Tässä oppaassa käytämme qTox-asiakkaita Windowsissa ja aToxia kommunikointiin.



## QToxin käytön aloittaminen



Kun olet ladannut sen, asenna Tox-asiakasohjelma ja luo profiili.



![qTox-acount](assets/fr/05.webp)



Onneksi olkoon, olet juuri liittynyt Tox-protokollaan. Löydät profiilitietosi qTox-ohjelmistosta klikkaamalla käyttäjänimeäsi.



![profil](assets/fr/06.webp)



Löydät erityisesti Tox-tunnuksesi, jonka voit tallentaa QR-koodina ja jakaa ihmisille, jotka haluavat ottaa sinuun yhteyttä.



Vie Tox-profiilitiedostosi, jotta sinulla on varmuuskopio profiilistasi ja yhteystiedoistasi, joita voit käyttää palauttamiseen. Napsauta **Vie**-painiketta ja valitse sitten varmuuskopiotiedoston polku.



![export](assets/fr/07.webp)



Lisää ystäviä, tuo yhteystietoja ja hallitse saamiasi ystäväpyyntöjä **Lisää** -valikosta.



![friends](assets/fr/08.webp)



Voit tavoittaa minut esimerkiksi tämän Tox-tunnuksen kautta: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Kun ystäväpyyntö on lähetetty, vastaanottajan on hyväksyttävä tai hylättävä pyyntösi, ennen kuin voit ottaa häneen yhteyttä.



![request](assets/fr/09.webp)



Tox-asiakasohjelma sisältää kaikki pikaviestisovellusten tarjoamat vaihtoehdot:





- Videopuhelut





- Äänipuhelut





- Tiedostojen jakaminen





- hymiöt



![chat](assets/fr/10.webp)



### Vertaisryhmät



Tox-asiakkaiden avulla voit myös kommunikoida ryhmän kanssa täysin hajautetusti: näitä kutsutaan konferensseiksi. Luo uusi konferenssi **Ryhmät** -valikossa tai tutustu saamiisi konferenssikutsuja koskevaan luetteloon.



![conferences](assets/fr/11.webp)



Kun konferenssi on luotu, voit kutsua ystäväsi liittymään konferenssiin Tox-asiakkaallasi. Napsauta kaveriluettelossa hiiren kakkospainikkeella sen kaverin käyttäjänimeä, jonka haluat kutsua. Napsauta **Kutsu konferenssiin** -vaihtoehtoa ja valitse sitten luomasi konferenssin nimi. Voit kutsua ystävän myös luomalla implisiittisesti konferenssin **Luo uusi konferenssi** -vaihtoehdolla.



⚠️ Tox-asiakkaita kehitetään edelleen, joten ohjelmistoa käytettäessä saattaa esiintyä virheitä. Konferenssi- ja videopuhelutoiminnot eivät ole vielä käytettävissä Tox Android -asiakasohjelmassa (aTox).



![invite](assets/fr/12.webp)



### Tiedostonsiirrot



**Tiedostonsiirrot** -valikossa näet lähetettyjen ja yhteystiedoiltasi saamiesi tiedostojen historian.



![files](assets/fr/13.webp)



Voit myös mukauttaa tiedostonjakomäärityksiä jokaista keskustelua varten. Napsauta vastaanottajan käyttäjänimeä hiiren kakkospainikkeella ja valitse "Näytä lisätietoja".



![details](assets/fr/14.webp)



Interface:n tiedoista voit hallita valtuutuksia, jotka myönnät vastaanottajalle :





- Konferenssikutsujen automaattinen hyväksyminen.





- Automaattinen tiedostojen hyväksyminen.





- Keskustelutiedostojen varmuuskopiointipolut.



![permissions](assets/fr/15.webp)



### Lisää parametreja



**Asetukset**-valikossa voit mukauttaa Tox-asiakkaan asetuksia.





- Muuta Tox-asiakkaan peruskieli, määritä tiedostojen varmuuskopiointipolut ja automaattisesti hyväksyttävän tiedoston enimmäiskoko kohdassa **Yleistä**.



![general](assets/fr/16.webp)





- Muokkaa **Interface-käyttäjä**-osiossa viestien fontteja ja kokoja. Voit myös muuttaa Tox-asiakkaasi teemaa.



![ui](assets/fr/17.webp)





- **Tietosuoja**-välilehdellä voit määritellä lyhytaikaiset viestit poistamalla valintaruudun "Säilytä keskusteluhistoria". Voit myös vaihtaa Nospam-koodisi, kun huomaat, että sinua roskapostitetaan kaveripyynnöillä, napsauttamalla "generate satunnainen NoSpam-koodi" -painiketta.



![privacy](assets/fr/18.webp)



### Mikä takaa Toxin luottamuksellisuuden?



Tox-protokollassa käytetään hajautettua Hash-taulukkoa hajautettujen solmujen verkon luomiseen. Jokainen Tox-asiakas on osa DHT-verkkoa ja tallentaa tietoja muista solmuista. Toxin tapauksessa DHT tallentaa IP-osoitteet Toxin julkisiin avaimiin liittyvinä arvoina (Tox ID). Tämän ansiosta Tox-asiakaslaitteen etsiminen on helppoa ilman kyselyä keskuspalvelimelta.



Kuvittele, että kirjoitat käyttäjälle `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F`, jonka nimi on **käyttäjä B**. Tox-asiakas etsii tämän tunnisteen Hash Distributed -taulukosta ja hakee siihen liittyvän IP Address:n. Kun IP Address on löydetty, Tox-asiakas luo suoran, salatun viestintäkanavan **käyttäjän B** koneeseen tai käyttää muita solmuja välittäjinä **käyttäjä B**:n tavoittamiseksi. Salausalgoritmit varmistavat, että viestintäkanavasta riippumatta vain **Käyttäjä B** pystyy lukemaan viestisi sisällön.



Jos olet nauttinut Toxin löytämisestä ja olet ymmärtänyt, miten se on hyödyllinen yksityisyytesi vahvistamisessa, anna tälle ohjeelle peukku ylöspäin. Suosittelemme myös Simple Login -oppaan, jonka avulla voit vastaanottaa ja lähettää sähköposteja nimettömänä.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41