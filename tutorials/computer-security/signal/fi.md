---
name: Signaali
description: Ilmaise itseäsi vapaasti
---
![cover](assets/cover.webp)



Signal on päästä päähän salattu viestisovellus, joka on suunniteltu tarjoamaan hyvää luottamuksellisuutta oletusarvoisesti. Jokainen viesti, puhelu ja tiedosto on suojattu Signal-protokollalla, joka on tunnustettu yhdeksi vankimmista viestiprotokollista. Sitä käyttävät uudelleen monet muut sovellukset, kuten WathsApp, Facebook Messenger, Skype ja Google Messages RCS-viestintään.



Signalin lanseerasi vuonna 2014 Moxie Marlinspike (salanimi), ja sitä on vuodesta 2018 lähtien kehittänyt Signal Foundation, voittoa tavoittelematon järjestö, joka on perustettu Brian Actonin (WhatsAppin toinen perustaja) tuella.



![Image](assets/fr/01.webp)



WhatsAppiin verrattuna Signal erottuu avoimuudellaan: sovelluksen koodi, sekä asiakas- että palvelinpuolen koodi, on täysin avointa lähdekoodia. Tämän ansiosta kuka tahansa voi tarkastaa sen ja erityisesti tarkistaa, että salausta sovelletaan mainostetulla tavalla.



Signal perustuu kuitenkin puhelinnumeron käyttöön, mikä on sen suurin heikkous anonymiteetin suhteen muihin ratkaisuihin verrattuna. Tästä huolimatta sovellus on mielestäni yksi luotettavimmista turvallisuuden ja luottamuksellisuuden kannalta, koska se on täysin avoin arkkitehtuuri ja laajalti hyväksytty salausprotokolla, ja siksi se on testattu ja tarkastettu, toisin kuin muut marginaalisemmat sovellukset.



| Sovellus             | E2EE 1:1       | E2EE ryhmät    | Anonyymi rekisteröinti | Avoimen lähdekoodin asiakaslisenssi | Avoimen lähdekoodin palvelinlisenssi | Hajautettu palvelin      | Luomisvuosi       |
| -------------------- | -------------- | -------------- | ---------------------- | ----------------------------------- | ------------------------------------ | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                      | ❌                                   | ❌                                    | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                      | ❌                                   | ❌                                    | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (valinnainen) | ❌                      | ❌                                   | ❌                                    | ❌                        | 2011              |
| Telegram             | 🟡 (valinnainen) | ❌              | 🟡                     | ✅                                   | ❌                                    | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                      | ❌                                   | ❌                                    | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                      | ✅                                   | ✅                                    | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                      | ✅                                   | ❌                                    | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                      | ✅                                   | ✅                                    | 🟡 (federoitu)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                      | ✅                                   | N/A                                  | 🟡 (sähköpostin kautta) | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                      | ✅                                   | ✅                                    | 🟡 (federoitu)          | 2014              |
| Session              | ✅              | ✅              | ✅                      | ✅                                   | ✅                                    | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                      | ✅                                   | ✅                                    | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                      | ✅                                   | ❌                                    | 🟡(ei hakemistoa)       | 2019              |
| Keet                 | ✅              | ✅              | ✅                      | ❌                                   | N/A                                  | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                      | ✅                                   | N/A                                  | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                      | ✅                                   | N/A                                  | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                      | ✅                                   | N/A                                  | ✅                        | 2013              |

*E2EE = End-to-end-salaus*




## Asenna Signal-sovellus



Signal on saatavilla kaikilla alustoilla. Voit ladata sovelluksen suoraan puhelimesi sovelluskaupasta:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



Androidissa on myös mahdollista [asentaa APK:n kautta](https://github.com/signalapp/Signal-Android/releases).



Tässä ohjeessa keskitymme mobiiliversioon, mutta huomaa, että [myös työpöytäversiot ovat saatavilla](https://signal.org/fr/download/) (MacOS, Linux ja Windows). Sinun on kuitenkin ensin otettava käyttöön mobiilisovellus, ennen kuin voit synkronoida tilisi työpöytäversion kanssa.



## Luo tili Signalissa



Kun käynnistät sovelluksen ensimmäistä kertaa, napsauta "*Jatka*"-painiketta.



![Image](assets/fr/02.webp)



Kirjoita puhelinnumerosi ja napsauta sitten "*Seuraava*".



![Image](assets/fr/03.webp)



Saat vahvistuskoodin tekstiviestillä. Syötä tämä koodi Signal-sovellukseen.



![Image](assets/fr/04.webp)



Valitse PIN-koodi Signal-tilisi suojaamiseksi. Tämä koodi salaa tietosi, ja sen avulla voit palauttaa tilisi käyttöoikeuden, jos laitteesi katoaa. Siksi on tärkeää valita vankka PIN-koodi, joka on mahdollisimman pitkä ja satunnainen, ja pitää siitä luotettava muistiinpano.



![Image](assets/fr/05.webp)



Vahvista PIN-koodi toisen kerran.



![Image](assets/fr/06.webp)



Voit nyt muokata käyttäjäprofiiliasi. Valitse valokuva, anna nimesi tai lempinimesi. Tässä vaiheessa voit myös määritellä, kuka voi löytää sinut Signalissa numerosi kautta. Valitse "*Kaikki*", jos haluat olla näkyvissä, tai "*Kenenkään*", jos haluat pysyä jäljittämättömänä puhelinnumeron kautta (sinut voidaan tällöin lisätä vain "*Käyttäjätunnuksella*"). Kun olet tehnyt valintasi, napsauta "*Seuraava*".



![Image](assets/fr/07.webp)



Olet nyt yhteydessä Signaliin ja valmis Exchange-viesteihin.



![Image](assets/fr/08.webp)



## Signal-tilin määrittäminen



Napsauta vasemmassa yläkulmassa olevaa profiilikuvaasi päästäksesi sovellusasetuksiin.



![Image](assets/fr/09.webp)



"*Tili*"-valikossa voit hallita profiiliasetuksiasi. Suosittelen pitämään oletusasetukset. Voit myös aktivoida "*Rekisteröintilukko*"-vaihtoehdon, joka suojaa tilisi tietyntyyppisiltä hyökkäyksiltä. Tämä valikko sisältää myös vaihtoehdot, joita tarvitset siirtääksesi tilisi uuteen laitteeseen.



![Image](assets/fr/10.webp)



Kun napsautat uudelleen profiilikuvaasi asetuksissa, pääset profiilisi mukauttamisvaihtoehtoihin. Suosittelen, että asetat "*Käyttäjätunnus*": näin voit ottaa yhteyttä muihin ihmisiin paljastamatta puhelinnumeroasi.



![Image](assets/fr/11.webp)



Valitsemalla "*QR-koodi tai linkki*" saat tiedot, jotka sinun on jaettava jonkun kanssa, joka haluaa lisätä sinut Signaliin.



![Image](assets/fr/12.webp)



Valikko "*Privacy*" on erityisen tärkeä. Täältä löydät vaihtoehtoja, joilla voit hallita numerosi näkyvyyttä, viestien hallintaa yhteystietojesi kanssa sekä erilaisia sovellukselle myönnettyjä valtuutuksia.



![Image](assets/fr/13.webp)



Tutustu myös vapaasti "*Esittely*", "*Juttelut*" ja "*Ilmoitukset*" -valikoihin, jotta voit räätälöidä Interface:n ja sovelluksen toiminnan henkilökohtaisten tarpeidesi mukaan.



## Connect-työpöytäsovellus



Kun haluat yhdistää työpöytäsovelluksen, asenna ohjelmisto ensin tietokoneellesi (katso tämän ohjeen ensimmäinen osa). Siirry sitten puhelimessasi kohtaan Asetukset ja avaa "*Linkatut laitteet*" -osio.



![Image](assets/fr/14.webp)



Napsauta "*Linkitä uusi laite*" -painiketta.



![Image](assets/fr/15.webp)



Käynnistä ohjelmisto tietokoneella ja skannaa sitten puhelimella näytössä näkyvä QR-koodi. Jos haluat tuoda keskustelusi, valitse "*Viestihistorian siirto*" -vaihtoehto.



![Image](assets/fr/16.webp)



Laitteesi on nyt täysin synkronoitu.



![Image](assets/fr/17.webp)



## Viestien lähettäminen Signalilla



Jos haluat viestiä jonkun kanssa Signalissa, sinun on ensin lisättävä hänet yhteystiedoksi. Vaihtoehtoja on useita: voit lisätä hänet puhelinnumeron kautta (jos henkilö on aktivoinut mahdollisuuden löytyä tällä tavoin) tai käyttämällä hänen Signal-tunnustaan.



Napsauta Interface:n oikeassa alakulmassa olevaa kynäkuvaketta.



![Image](assets/fr/18.webp)



Minun tapauksessani haluan lisätä henkilön käyttäjänimen mukaan. Joten klikkaan "*Haku käyttäjänimen* mukaan".



![Image](assets/fr/19.webp)



Voit sitten joko liittää sen kirjautumistunnuksen tai skannata sen QR-koodin.



![Image](assets/fr/20.webp)



Lähetä hänelle viesti yhteydenottoa varten.



![Image](assets/fr/21.webp)



Keskustelu ilmestyy tämän jälkeen etusivulle. Jos henkilö hyväksyy yhteydenottopyyntösi, näet hänen nimensä ja profiilikuvansa.



![Image](assets/fr/22.webp)



Onneksi olkoon, olet nyt vauhdissa Signal-viestien käytössä, joka on loistava vaihtoehto WathsAppille! Jos löysit tämän opetusohjelman hyödylliseksi, olisin hyvin kiitollinen, jos jättäisit Green peukalon alle. Voit vapaasti jakaa tätä opetusohjelmaa sosiaalisissa verkostoissa. Kiitos paljon!



Suosittelen myös tätä toista opetusohjelmaa, jossa esittelen sinulle Proton Mailin, joka on paljon yksityisyydensuojaystävällisempi vaihtoehto Gmailille:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2