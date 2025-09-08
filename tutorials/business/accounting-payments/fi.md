---
name: Bitcoin:n seuranta liiketoimintana

description: Opi helposti ja nopeasti tilittämään Bitcoin-maksut pienyrityksessä.
---

![cover](assets/cover.webp)


## Johdanto


Tämän ohjeen tavoitteena on antaa pienyrityksen, mieluiten kaupan, katukaupan tai muun kaupallisen toiminnan omistajalle mahdollisuus hyväksyä Bitcoin maksuna ja elää sen kanssa yksinkertaisella tavalla. Kohderyhmänä on yrityksen omistaja, joka hoitaa kaupallista toimintaa itsenäisesti ja luottaa joihinkin työntekijöihin.


### Kuuluisia esimerkkejä


Joillakin maailman alueilla on yhteisöjä, jotka voidaan määritellä "kiertäviksi", joissa väestö sekä hyväksyy Bitcoin:n että käyttää sitä laajalti maksamaan palveluista kaupallisessa toiminnassa. Jopa kauppiaat ovat tehneet tavarantoimittajiensa kanssa sopimuksia siitä, että ne maksavat tavaroista Bitcoin:lla, kun asiakkaat ovat maksaneet ne Bitcoin:lla.


## Bitcoin:n hyväksyminen


Seuraava askel on hyväksyä Bitcoin suoraan yrityksessäsi; yksinkertaisin tapa tehdä tämä on asentaa ja konfiguroida Lightning Network (LN) Wallet välittömien maksujen vastaanottamista varten, jolloin asiakkaat voivat maksaa samalla alennettuja transaktiomaksuja.


Yksinkertaisuuden vuoksi käytämme esimerkkinä Satoshi:n Wallet:tä. Asenna ja määritä se seuraavien ohjeiden mukaisesti:


https://planb.network/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Kun olet noudattanut opasta, olet valmis hyväksymään Bitcoin:n maksutapana: avaa mobiilisovellus ja napsauta "Vastaanota"-painiketta ja syötä sitten käyttäjän maksettavaksi tuleva summa (yleensä paikallisessa valuutassa) generate:een tai Invoice:een.


**Pro-vinkki**: lisäämällä huomautuksen Invoice:ään ennen sen luomista voit helposti yhdistää maksun tiettyyn tapahtumaan (esim. 1 kg omenoita myydään 900 Sats:llä). Manuaalisesti lisätyt huomautukset eivät näy vastapuolelle, joten ne ovat vain sisäisessä käytössä.


### Lisäasetukset


Hieman edistyneempi konfiguraatio on Wallet:n Satoshi:n Point of Sale -ominaisuuden käyttäminen, johon pääsee sovelluksesta napsauttamalla oikeassa yläkulmassa olevaa hampurilaisvalikkoa:


![image](assets/en/01.webp)


Tämä on toinen kahdesta tavasta käyttää Point of Sale -toimintoa. Toinen tapa on oma [Wallet of Satoshi PoS-sovellus] (https://www.walletofsatoshi.com/pos.)


Point of Sale -ominaisuuden käytöstä on kolme etua:


- ainoa vastaanottotoiminto, joka sopii erinomaisesti siihen, että työntekijät voivat kerätä maksuja asiakkailta ilman, että he voivat käyttää näitä varoja;
- mahdollistaa hintojen ja tuotteiden luettelon luomisen myymälääsi, joten voit luoda salamalaskuja valitsemalla ostetut tuotteet;
- lataa myyntiraportit CSV-muodossa.


Lisätietoja on Satoshi - Myyntipisteen Wallet:tä koskevassa oppaassa:


https://planb.network/tutorials/business/point-of-sale/wallet-of-satoshi-pos-efc9f266-cb21-49a8-94a8-5fe15a82eb07

## Asetus


Bitcoin:ta koskeva sääntely vaihtelee suuresti maasta toiseen. Joissakin maissa säännökset ovat selkeitä ja tiukkoja, kun taas toisissa maissa ne ovat epäselvempiä ja epämääräisempiä. Monet maat vaativat hallussasi olevan Bitcoin:n ilmoittamista (sekä yksityishenkilönä että yrityksenä) verovalvontaa tai verotusta varten.


## Ratkaisu kauppiaille


Riippumatta maasi lainsäädännöstä pienyrittäjän yksinkertaisin toimenpide on muuntaa vastaanotetut bitcoinit paikalliseksi valuutaksi heti niiden vastaanottamisen jälkeen. Näin voit välttää komplikaatioita, jotka liittyvät Bitcoin:n hyväksymiseen, ilmoittamiseen ja kirjanpitoon kaupallisessa toiminnassasi.


**Huomautus**: Joissain yrityksissä ei välttämättä ole paperisia asiakirjoja, jotka liittyvät asiakkaan ja myyjän väliseen liiketoimintaan, joten yrityksen omistajan kannalta se on vielä helpompaa ja välittömämpää!


Tarkastellaan tämän ratkaisun etuja ja haittoja:


### Edut


Tämän yksinkertaisen lähestymistavan avulla voit välttää useita ongelmia: se poistaa tarpeen KYC (Know Your Customer) -menettelyjen käyttöönotosta maksuna vastaanotettujen Bitcoins-rahojen osalta, mikä on erittäin haitallinen käytäntö yksilöiden yksityisyyden ja turvallisuuden kannalta; ja se pitää kirjanpitotoimet muuttumattomina, koska Bitcoins-rahoja ei tarvitse kirjata.


Sinun ei tarvitse käyttää veroneuvojasi kanssa ylimääräistä aikaa ja rahaa näiden ansioiden seurantaan, sillä ne ovat yhtä suuria kuin muutkin ansiot.


### Haitat


Bitcoin-tapahtumien määrän kasvaessa käteisen lisääminen kassaan voi käydä mahdottomaksi, koska esimerkiksi käytettävissä oleva käteinen raha ei välttämättä kata kaikkia Bitcoin-tuloja. Tämä on kuitenkin epätodennäköinen skenaario useimmille liikkeenomistajille, jotka alkavat hyväksyä Bitcoin:tä. Toinen mahdollinen ongelma joissakin Euroopan maissa on se, että liiketoimintasi tyyppi saattaa estää sinua hyväksymästä käteistä asiakkaille tarjottujen tavaroiden ja palvelujen maksutapana. Tällaisissa tapauksissa ehdotettu ratkaisu ei enää riitä.


## Bitcoin-raportti


Kuten olemme nähneet, Bitcoin:n hyväksyminen on helppoa ilman, että otetaan käyttöön uusia kirjanpitomenettelyjä, jotka vahingoittavat yksityisyyden suojaa; olisi kuitenkin suositeltavaa ylläpitää rinnakkaista kirjanpitojärjestelmää Bitcoin-virran seuraamiseksi. Älä huoli, se voi olla niin yksinkertaista kuin haluat, kunhan ymmärrät, kuinka monta bitcoinia Wallet:ään tulee ja lähtee.


**Huomio**: "Huomautus"-kentän täyttäminen, kun asiakkaalle luodaan LN Invoice, helpottaa Bitcoin-kirjanpidon päivittämistä huomattavasti. Sama koskee myös LN-maksun suorittamista toimittajille. Ihannetapauksessa jokaiseen tapahtumaan liittyy maksuhuomautus.


## Päätelmä


Bitcoin:n hyväksyminen on vain ensimmäinen askel. Kaupallisessa toiminnassa on olennaista seurata toimintoja uhraamatta yksilön yksityisyyttä ja vapautta. Ja kuten olemme nähneet, yksinkertainen ratkaisu ratkaisee monia ongelmia ja tyydyttää kaikkia liiketoimen osapuolia - sekä yritystä että asiakasta.