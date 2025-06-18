---
name: SimpleX Chat
description: Ensimmäinen postilaatikko ilman käyttäjätunnusta
---
![cover](assets/cover.webp)



Vuonna 2021 lanseerattu SimpleX on ilmainen pikaviestisovellus, jonka lähestymistapa yksityisyyteen on täysin erilainen. Toisin kuin WhatsApp, Signal ja muut keskitetyt viestipalvelut, SimpleX erottuu käyttäjähallinnallaan: siinä ei ole käyttäjätunnuksia, salanimiä, numeroita tai näkyviä julkisia avaimia. Tämä tunnisteiden täydellinen puuttuminen tekee käyttäjien korreloimisen käytännössä mahdottomaksi ja takaa korkean yksityisyyden suojan.



Toisin kuin useimmat sovellukset, jotka vaativat tilin tai puhelinnumeron, SimpleX:n avulla voit aloittaa keskustelut jakamalla linkin tai hetkellisen QR-koodin. Jokainen linkki luo ainutlaatuisen salatun kanavan, eivätkä kontaktit voi löytää tai ottaa yhteyttä lähettäjään ilman nimenomaista Exchange:ta. Viestit salataan alusta loppuun, ja ne kulkevat välityspalvelimien kautta, jotka poistavat ne lähettämisen jälkeen, eivätkä näe lähettäjää, vastaanottajaa tai niiden avaimia.



![Image](assets/fr/01.webp)



Verkkoarkkitehtuuri on täysin hajautettu ja liittovaltioton: palvelimet eivät tunne toisiaan, ne eivät pidä globaalia hakemistoa eivätkä ylläpidä käyttäjäprofiileja. Mikä parasta, kukin käyttäjä voi ottaa käyttöön ja käyttää omaa relepalvelinta, joka on kuitenkin yhteentoimiva julkisen verkon palvelinten kanssa.



SimpleX on täysin avointa lähdekoodia (asiakkaat, protokollat ja palvelimet), ja se on saatavilla Android-, iOS-, Linux-, Windows- ja macOS-käyttöjärjestelmille. Sen paikallinen tallennus on salattu ja siirrettävissä, joten voit siirtää profiilin laitteesta toiseen ilman keskitettyä palvelinta.



SimpleX yhdistää kaikki viestisovellusten klassiset ominaisuudet. Sen ergonomia ei kuitenkaan ole yhtä sujuva kuin WhatsAppin tai Signalin. Sen käyttö voi myös olla rajoittavampaa, etenkin yhteystietoja lisättäessä. Mielestäni se on siis relevantti vaihtoehto WhatsAppille tai Signalille käyttäjille, joille luottamuksellisuus on tärkeintä ja jotka ovat tästä syystä valmiita tekemään joitakin myönnytyksiä päivittäisessä käyttömukavuudessa.



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



## Asenna SimpleX Chat -sovellus



SimpleX Chat on saatavilla kaikilla alustoilla. Voit ladata sovelluksen suoraan puhelimesi sovelluskaupasta:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



Androidissa on myös mahdollista [asentaa APK:n kautta](https://github.com/simplex-chat/simplex-chat/releases).



Tässä ohjeessa keskitymme mobiiliversioon, mutta huomaa, että [myös työpöytäversiot ovat saatavilla](https://simplex.chat/downloads/) (MacOS, Linux ja Windows). Työpöytäversio on mahdollista yhdistää olemassa olevaan mobiilikäyttäjäprofiiliin, mutta jotta tämä synkronointi toimisi, molempien laitteiden on oltava yhteydessä samaan lähiverkkoon.



![Image](assets/fr/02.webp)



## Luo tili SimpleX Chatissa



Kun käynnistät sovelluksen ensimmäisen kerran, napsauta "*Luo profiilisi*" -painiketta.



![Image](assets/fr/03.webp)



Valitse käyttäjätunnus, joka voi olla oikea nimesi tai salanimi, ja napsauta sitten "*Luo*".



![Image](assets/fr/04.webp)



Määritä seuraavaksi taajuus, jolla sovellus tarkistaa uudet viestit. Jos puhelimesi akun kesto ei ole ongelma, voit vastaanottaa viestejä reaaliajassa valitsemalla "*Instant*". Jos haluat säästää akkua ja estää sovellusta toimimasta taustalla, valitse "*Kun sovellus on käynnissä*": saat viestejä vain silloin, kun sovellus on auki. Mahdollinen kompromissi on valita määräaikaistarkistus 10 minuutin välein.



Kun olet tehnyt valintasi, napsauta "*Käytä keskustelua*".



![Image](assets/fr/05.webp)



Olet nyt yhteydessä SimpleX Chatiin ja valmis aloittamaan keskustelun.



![Image](assets/fr/06.webp)



## SimpleX Chatin määrittäminen



Pääset ensin asetuksiin napsauttamalla profiilikuvaasi oikeassa alakulmassa ja valitsemalla sitten "*Asetukset*".



![Image](assets/fr/07.webp)



Oletusasetukset sopivat yleensä useimmille käyttäjille. Suosittelen kuitenkin, että menet "*Database passphrase & export*" -valikkoon. Täältä voit viedä SimpleX-tilin tietokannan varmuuskopiointia varten.



Voit myös muuttaa passphrase:ta, jota käytetään tämän tietokannan salaamiseen. Oletusarvoisesti se luodaan satunnaisesti ja tallennetaan paikallisesti laitteeseesi. Voit halutessasi määritellä oman passphrase:n ja poistaa paikallisen passphrase-varmuuskopion: sinun on sitten syötettävä se manuaalisesti joka kerta, kun avaat sovelluksen, sekä siirryttäessäsi toiseen laitteeseen.



**Huomaa**: Jos valitset tämän vaihtoehdon, passphrase:n katoaminen johtaa kaikkien SimpleX-profiilien ja -viestien pysyvään katoamiseen.



![Image](assets/fr/08.webp)



Suosittelen myös, että menet "*Turva ja tietosuoja*" -valikkoon, jossa voit aktivoida "*SimpleX Lock*" -vaihtoehdon. Tämä suojaa pääsyn sovellukseen lukituskoodilla.



![Image](assets/fr/09.webp)



Lopuksi, "*ilmoitukset*" ja "*Näkymä*" -valikoissa voit mukauttaa SimpleX Chatin mieltymyksiisi sopivaksi.



![Image](assets/fr/10.webp)



## Lähetä viestejä SimpleX Chatin avulla



Jos haluat muodostaa yhteyden toiseen henkilöön SimpleX:ssä, sinulla on kaksi vaihtoehtoa:




- Käytä kertakäyttöistä linkkiä;
- Käytä uudelleenkäytettävää staattista Address:ää.



Staattisen Address:n avulla kuka tahansa, joka tietää sen, voi ottaa sinuun yhteyttä SimpleX:ssä. Se on pysyvä Address, jota voi käyttää useita kertoja eri henkilöiden toimesta ilman aikarajoitusta. Juuri tämä pysyvyys tekee siitä alttiimman roskapostille. Toisin kuin muissa viestisovelluksissa, SimpleX Address:n poistaminen riittää kuitenkin estämään kaiken roskapostin ilman, että se vaikuttaa olemassa oleviin keskusteluihin. Itse asiassa Address:ta käytetään vain alustavan yhteyden muodostamiseen, eikä sitä enää tarvita, kun Exchange on alkanut.



Kertakäyttölinkkejä sen sijaan voi kuka tahansa käyttäjä käyttää vain kerran. Kun yhteyshenkilö on kerran käyttänyt linkin, linkki mitätöityy. Sinun on luotava uusi generate-linkki jokaista uutta yhteyttä varten.



### Staattisella Address:lla



Jos haluat käyttää Address:tä, napsauta Interface:n vasemmassa alakulmassa olevaa profiilikuvaasi ja valitse sitten "*Luo SimpleX Address*". Napsauta sitten uudelleen "*Luo SimpleX Address*".



![Image](assets/fr/11.webp)



Uudelleenkäytettävä Address on nyt luotu. Voit jakaa sen ihmisille, jotka haluavat ottaa sinuun yhteyttä, joko näyttämällä heille QR-koodia tai lähettämällä heille linkin.



![Image](assets/fr/12.webp)



Napsauta painiketta "*Address-asetukset*". Tässä voit määrittää Address:een liittyvät käyttöoikeudet. "*Jaa yhteystietojen kanssa*" -vaihtoehto tekee Address:n näkyväksi SimpleX-profiilissasi. Yhteyshenkilösi voivat tällöin tutustua siihen ja lähettää sen eteenpäin muille henkilöille, jotka haluavat ottaa sinuun yhteyttä.



"*Automaattinen hyväksyminen*"-vaihtoehto hyväksyy automaattisesti Address:n kautta saapuvat yhteydet. Tämä tarkoittaa, että kuka tahansa, jolla on Address, voi nähdä profiilisi ja lähettää sinulle viestin, ellet aktivoi "*Accept incognito*"-vaihtoehtoa. Tämä piilottaa nimesi ja profiilikuvasi, kun uusi yhteys muodostetaan, ja korvaa ne satunnaisella salanimellä, joka on erilainen jokaiselle keskustelukumppanille.



![Image](assets/fr/13.webp)



### Uudelleenkäytettävällä linkillä



Toinen tapa luoda yhteys henkilöön on luoda kertaluonteinen linkki. Tee tämä napsauttamalla Interface:n oikeassa alakulmassa olevaa kynäkuvaketta ja valitsemalla sitten "*Luo 1-kertainen linkki*".



Jos yhteyshenkilösi on lähettänyt sinulle linkin, skannaa tai liitä se napsauttamalla "*Skannaa / liitä linkki*".



![Image](assets/fr/14.webp)



SimpleX luo sitten kertakäyttöisen linkin. Voit välittää sen yhteyshenkilöllesi millä tahansa tavalla: fyysisellä Exchange:llä, muilla viesteillä jne.



![Image](assets/fr/15.webp)



Voit myös valita, minkä profiilin haluat liittää tähän kutsulinkkiin. Voit tehdä niin napsauttamalla profiiliasi heti QR-koodin alapuolella. Voit sitten :




- valitse jokin olemassa olevista profiileistasi (seuraavassa osassa kerrotaan, miten voit luoda useita profiileja);
- tai valitse "*Incognito*"-tila, joka piilottaa nimesi ja profiilikuvasi ja antaa kirjeenvaihtajallesi satunnaisesti luodun salanimen.



Tässä valitsen "*Incognito*"-tilan.



![Image](assets/fr/16.webp)



Yhteyshenkilöni käytti linkkiä. Hän ei puolestaan aktivoinut "*Incognito*"-tilaa, minkä vuoksi näen hänen profiilinsa nimen "*Bob*". Toisaalta Bob ei näe oikeaa nimeäni "*Loïc Morel*", vaan satunnaisen salanimen, tässä tapauksessa "*RealSynergy*".



![Image](assets/fr/17.webp)



Voisin aloittaa keskustelun heti, mutta haluaisin ensin varmistaa, että puhun Bobin kanssa enkä jonkun pahantahtoisen henkilön kanssa, joka on saattanut siepata linkin tai tehdä MITM-hyökkäyksen.



Tarkistamme tätä varten turvallisuuslinkin **sovelluksen ulkopuolella**. Tämä on tärkeää, koska MITM-hyökkäyksen sattuessa sisäinen tarkistus vaarantuisi. Käytä siis toista suojattua viestijärjestelmää tai vielä parempi, tarkista koodit henkilökohtaisesti.



Napsauta chatissa Bobin kuvaa ja sitten "*Varmenna turvakoodi*". Bobin on tehtävä sama omalla puolellaan.



![Image](assets/fr/18.webp)



Jos työskentelet etänä, vertaa koodeja toisessa suojatussa viestijärjestelmässä (niiden on oltava identtiset). Tai vielä parempi, jos voit tavata kasvotusten, skannaa kontaktisi QR-koodi napsauttamalla "*Skannaa koodi*".



![Image](assets/fr/19.webp)



Jos vahvistus onnistuu, yhteyshenkilön nimen viereen ilmestyy kilpi ja valintamerkki. Tämä on varmuus siitä, että vaihdat tietoja Bobin kanssa. Jos vahvistus ei onnistu, näyttöön tulee "*Väärä turvakoodi!*" -ilmoitus.



![Image](assets/fr/20.webp)



Voit nyt vapaasti käyttää Exchange-viestejä, puheluita ja tiedostoja Bobin kanssa sen mukaan, mitä oikeuksia olet asettanut tälle keskustelulle.



## Mukauta SimpleX Chat -profiileja



Yksi SimpleX:n tehokkaimmista ominaisuuksista on mahdollisuus hallita useita täysin erillisiä käyttäjäprofiileja, joita kaikkia voi käyttää samalta paikalliselta tililtä. Näin voit erottaa eri identiteetit siististi toisistaan ilman, että viestien hallinta vaikeutuu.



Voit esimerkiksi luoda :




- Profiili, jossa on oikea nimesi ja oikea valokuva ammatillisia vaihtoja varten;
- Profiili, jossa on oikea nimesi ja hauska kuva perheesi vaihtoa varten;
- Profiili, jossa on väärennetty valokuva ja salanimi henkilökohtaisia keskusteluja varten;
- Toinen pseudonyymiprofiili tuntemattomien kanssa keskustelemista varten.



Niin me aiomme tehdä tässä. Aloitan määrittelemällä pääprofiilini, joka on yhdistetty oikeaan henkilöllisyyteeni. Napsautan profiilikuvaani oikeassa alakulmassa ja sitten käyttäjänimeäni.



![Image](assets/fr/21.webp)



Sitten klikkaan profiilikuvaani vaihtaakseni sen ja lisätäkseni uuden.



![Image](assets/fr/22.webp)



Jos haluat lisätä muita profiileja, napsauta "*Jutteluprofiilisi*" -valikkoa.



![Image](assets/fr/23.webp)



Täällä näet kaikki profiilisi. Klikkaa "*Lisää profiili*" luodaksesi uuden profiilin.



![Image](assets/fr/24.webp)



Valitse sitten uuden profiilisi tiedot: nimi, valokuva jne. Tässä käytän salanimeä ja erilaista kuvaa piilottaakseni todellisen henkilöllisyyteni tietyissä keskusteluissa.



![Image](assets/fr/25.webp)



Voit piilottaa profiilin pitämällä sormea alhaalla. Tämä tekee siitä näkymättömän sovelluksessa, samoin kuin kaikista siihen liittyvistä keskusteluista. Voit myös mykistää sen, jos haluat lopettaa ilmoitusten vastaanottamisen.



![Image](assets/fr/26.webp)



Kun olet luonut profiilit, voit hallita niitä itsenäisesti. Valitse etusivulta vain aktiivinen profiili, jonka haluat näyttää.



![Image](assets/fr/27.webp)



Kun luot kutsulinkkiä tai staattista Address:a, voit nyt valita, minkä profiilin haluat liittää siihen. Jos esimerkiksi valitsen profiilin "*Satoshi Nakamoto*" generate-linkkiä varten ja lähetän sen Alicelle, hän näkee vain pseudonyymin henkilöllisyyteni "*Satoshi Nakamoto*", mutta ei saa koskaan tietää oikeaa henkilöllisyyttäni "*Loïc Morel*". Jos taas annan hänelle linkin oikeasta profiilistani, hän ei voi mitenkään linkittää pseudonyymiin profiiliini.



![Image](assets/fr/28.webp)



Onneksi olkoon, olet nyt vauhdissa SimpleX-viestinnän kanssa, joka on erinomainen vaihtoehto WathsAppille!



Suosittelen myös tätä toista opetusohjelmaa, jossa esittelen Threeman, toisen mielenkiintoisen vaihtoehdon viestisovelluksellesi:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74