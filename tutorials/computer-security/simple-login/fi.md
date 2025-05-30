---
name: Yksinkertainen kirjautuminen
description: Identiteetti suojattu peitenimillä
---
![cover](assets/cover.webp)

## Kirjautuminen = sähköposti = yksityisyyden menetys


Digitaalisessa maailmassa on tullut tavaksi, että jokaisella alustalla, jota haluaa käyttää, on oltava oma tili.

Kukin näistä palveluista vaatii kirjautumisen, johon yleensä liittyy _käyttäjätunnus_ ja _salasana_. Usein käyttäjätunnus on käyttäjän henkilökohtainen sähköpostiosoite.


Kun henkilökohtaista Address-sähköpostia käytetään jokaiseen kirjautumiseen, on helppo kuvitella ensimmäinen seuraus: luottamuksellisuuden menettäminen, joka muuttuu merkittäväksi, jos Address koostuu osoitteesta _name.surname@serviceemail.com_.


Avoimen lähdekoodin työkalujen kehittäjät ovat luoneet joukon sovellussarjoja, jotka on luotu juuri siksi, että käyttäjät saisivat hieman yksityisyyttä takaisin: he kirjautuvat edelleen sisään, mutta käyttävät peitenimeä sen sijaan, että käyttäisivät työkalua, joka paljastaa heidän yksityisen identiteettinsä.


Yksinkertaisin niistä, joita olen itse kokeillut ja testaan edelleen, on [Simple Login](https://simplelogin.io/).


## Alias


Sähköpostin alias korvaa yksinkertaisesti sähköpostisi Address:n _nimi.sukunimi_-osan fiktiivisellä nimellä. Käyttäjän kannalta mikään ei muutu; alias-palvelu välittää sähköpostit tavalliseen Address:een ja tavallisesta Address:stä normaalisti. Jokainen voi jatkaa postilaatikkonsa käyttöä kuten aina, mutta oikean nimen sijaan se näyttää tunnistamattoman käyttäjän nimen. Tämän palvelun on oltava tehokas, ja tähän mennessä Simple Login on osoittautunut juuri sellaiseksi.


Kun vierailet Simple Login -sivustolla ensimmäistä kertaa, sinun on luotava tili (myös täällä!) käyttämällä "virallista" sähköpostia Address. Täällä sinun on annettava sähköpostiosoite, salasana ja ratkaistava captcha.


![image](assets/it/02.webp)


Simple Login lähettää vahvistusviestin ilmoitettuun sähköpostiin Address. Varmennuspainikkeen napsauttamisen sijaan on suositeltavaa kopioida linkki ja liittää se Address-palkkiin.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Simple Login -kojelauta avautuu välittömästi, ja siinä on lyhyt ohje navigointia varten.


![image](assets/it/05.webp)


On huomattava, että Simple Login aktivoi automaattisesti uutiskirjeen tilauksen, joka voidaan poistaa käytöstä asianmukaisesta komennosta.


![image](assets/it/06.webp)


## Asetukset


Voit tutustua palvelun ominaisuuksiin heti _asetuksissa_. Yksinkertainen kirjautuminen alkaa, kun kaikki vaihtoehdot ovat aktiivisia, mukaan lukien _Premium_-vaihtoehdot, jotka ovat käytettävissä 10 päivää. Kun kokeilujakso on ohi, sinulla on mahdollisuus luoda 10 peitenimeä tällä profiililla ja voit yhdistää suoraan Proton-sähköpostisi, sillä sveitsiläinen sähköpostipalveluntarjoaja on ostanut Simple Loginin.


![image](assets/it/07.webp)


Voit asettaa joukon parametreja tai tarkistaa, onko sähköpostisi yksityisyys jo vaarantunut.


![image](assets/it/08.webp)


Lopuksi voit viedä varmuuskopion profiilistasi tai tuoda sen toisesta palveluntarjoajasta.


![image](assets/it/09.webp)


### Työ Sähköposti


Ne, jotka käyttävät sähköpostia henkilökohtaisella verkkotunnuksella työsähköpostina, voivat perustaa yksityisen verkkotunnuksen.


![image](assets/it/10.webp)


Pääpaneelista, valitsemalla _Postilaatikot_, on jopa mahdollista lisätä muita sähköpostiosoitteita ja käyttää myös aliaksia, jotka luodaan vastaavasti. Esimerkiksi tässä ohjeessa päätin luoda profiilin _gmail.com_-postilaatikolla ja liittää siihen _proton.me_ Address.


![image](assets/it/11.webp)


Kun lisäät uuden Address:n, erityisesti jos se kuuluu Proton-palveluntarjoajaan, opastettu menettely osoittaa mahdollisuuden siirtyä _sudo_-tilaan, superkäyttäjäksi. Yksinkertainen kirjautuminen pyytää syöttämään tämän postilaatikon salasanan, jotta voidaan todistaa laillinen Ownership.


⚠️ **En henkilökohtaisesti suosittele tekemään näin**. ⚠️


![image](assets/it/12.webp)


**On parempi päästä sähköpostilaatikkoon -> kopioida vahvistuslinkki ja liittää se URL-palkkiin -> ja saada vahvistus paljastamatta salasanaa.**


![image](assets/it/13.webp)


Kahdesta syötetystä osoitteesta toisesta tulee oletusosoite ja toisesta toissijainen osoite, mutta ne voidaan vaihtaa helposti, ja asetus on helposti tunnistettavissa kojelaudassa.


![image](assets/it/14.webp)


Kun olemme lisänneet toisen sähköpostin Address (valinnainen), katsotaan, mitä voimme tehdä Simple Loginilla.


## Peitenimien luominen


Paneelin ensimmäinen valikkovaihtoehto on _Alias_, jossa voit luoda niitä. Sinulla on mahdollisuus valita generate-peitenimet satunnaisesti napsauttamalla Random Alias -painiketta, joka on seuraavassa kuvassa näkyvä Green-painike. Tämä toiminto luo ainutlaatuisen ja kiehtovan sähköpostin Address.


![image](assets/it/24.webp)


Jos haluat kuitenkin erottaa palvelut toisistaan antamalla niille eri nimet, sinun on valittava _Uusi mukautettu peitenimi_. Näin voit antaa aliakselle haluamasi palvelun nimen (sosiaalinen media, palveluntarjoajat, verkkotapahtumat, sattumalta tavatut tuntemattomat jne.). Loput hoitaa Simple Login.

Huvikseni (mutta en oikeastaan, jos totta puhutaan) päätin luoda pankille peitenimen ja kutsuin sitä nimellä `BANK`. Vaikka on totta, että pankkini tietää minusta kaiken, minusta on huvittavaa kommunikoida heidän kanssaan käyttämällä sähköpostia Address, jota he eivät ymmärrä. Simple Login todellakin luo satunnaisen nimen, joka erotetaan valitsemastamme nimestä `.`-merkillä


Tässä uusi sähköposti Address voi tulla:


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- ja niin edelleen


Voit valita useamman kuin yhden verkkotunnuksen: julkiset verkkotunnukset ovat saatavilla ilmaispaketissa, kun taas muut yksityiset verkkotunnukset (mukaan lukien _@simplelogin.com_) laajentavat niiden käyttäjien valikoimaa, jotka päättävät tilata maksullisen paketin.


![image](assets/it/15.webp)


Kun satunnainen päätteeksi ja verkkotunnus on valittu, voit määrittää, tuleeko tämä uusi (ja outo) Address toimia aliasina vain yhdelle henkilökohtaiselle sähköpostilaatikolle vai kaikille niille. Alias tulee valmiiksi ja aktiiviseksi, kun napsautat _Luo_


![image](assets/it/16.webp)


Uusi Address-sähköposti luotiin, ja se on nyt näkyvissä, valmiina lähetettäväksi (pankkiin!) yksinkertaisesti kopioimalla se.


![image](assets/it/18.webp)


Tässä vaiheessa voit keskittyä luomaan peitenimen jokaista palvelua tai alustaa varten, jota haluat käyttää ja jossa sähköpostiosoite on olennainen parametri tilin luomiseksi.


![image](assets/it/19.webp)


Yksityisyydensuojan ystäville on myös mahdollisuus valita generate-sähköposti Address UUID-protokollaan perustuen (ei tunnistettaviin nimiin), joka luo yksilöllisen 128-bittisen tunnisteen, jota keskitetyt osapuolet eivät hallitse. Tämä ominaisuus, joka on hyödyllinen arkaluonteisille tileille, löytyy _Random Alias_ -valikosta.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Kuten huomaat, tämä on Address-sähköposti, joka vaatii asianmukaista hallintaa.


Jos muutat mielesi etkä enää halua käyttää aliaksia, napsauta kunkin yksittäisen aliaksen _More_-komentoa ja valitse _Delete_.


![image](assets/it/23.webp)


## Alias-hallinta


Peitenimien luominen on helppoa, samoin kuin niiden hallinta, joka vaatii vain hieman huolellisuutta ja kurinalaisuutta. Kaikki liikenne kulkee edelleen sen sähköpostilaatikon kautta, jonka olemme alussa määritelleet viralliseksi sähköpostilaatikoksi. Alustojen ilmoitukset ja tärkeät viestit saapuvat edelleen Gmailiin, Protoniin tai mihin tahansa sähköpostipalveluntarjoajaan.


Tuloksena on kuitenkin se, että olemme säilyttäneet tärkeimmän Address:n, jonka voimme peitenimien luomisesta lähtien vapaasti päättää, kenelle paljastamme sen ja kenelle emme.


Peitenimi toimii sekä vastaanotossa että lähetyksessä: toinen käyttäjä saa todellakin vastauksen osoitteesta alias.preoccupy789@8shield.net, jos tämä on kyseiselle vastaanottajalle valittu salanimi.


## Plussaa


Kaiken kaikkiaan peitenimien käyttö on tehokas tapa suojata henkilöllisyyttä ja yksityisyyttä. Tietojen välittäjät ja verkkosivustot keräävät usein sähköpostiosoitteita käyttäjien tottumusten ja käyttäytymisen seuraamiseksi. Vaikka peitenimi ei tee sinusta täysin jäljittämätöntä, sen johdonmukainen käyttö on myönteinen askel kohti tietojesi suojaamista. Lisäksi "globaalissa digitaalisessa kylässämme", jossa hakkerointi, tietojen myynti ja tietoturvaloukkaukset ovat aivan liian yleisiä, on erittäin todennäköistä, että sähköpostiosoite, jota käytät rekisteröityessäsi eri verkkosivustoille, on jo vaarantunut tai joutunut kohteeksi.


Ainutlaatuinen salanimi, jota käytetään jokaisella sisäänkirjautumisella, **antaa meille välittömästi mahdollisuuden ymmärtää, mikä foorumi lähettää roskapostia (tai pahempaa) postilaatikkoon, koska sähköposti tunnistetaan siihen liittyvän peitenimen perusteella**. Sinulla ei ole aavistustakaan, kuinka paljon roskapostia ja phishingia tulee niin sanotuista luotettavista kanavista, koska ne ovat institutionaalisia, kunnes alat käyttää peitenimeä pankkeihin, postipalveluihin tai tiettyä peitenimeä joihinkin pakollisiin viranomaispalveluihin. Kun roskapostin (tai pahemman) lähettäjä on tunnistettu, tiedät, että kyseinen sivusto on vaarantunut, ja teet kaikki varotoimet suojellaksesi kaikkia tietoja, jotka annat (ajattele luottokortteja!) kyseiselle sivustolle, joka saattaa huomata rikkomuksen viikkoja myöhemmin.


Simple Login -työkalulla on seuraavat ominaisuudet:



- mobiilisovellus (myös F-Droidilta) ja selainlaajennus, jolla voit hallita peitenimiä kaikissa tilanteissa;
- kahden tekijän todennus jokaiselle uudelle salanimelle, mikä lisää riippumattomuutta itse palvelusta;
- PGP-tuki (_Premium-käyttäjille);
- kaikkien alias-tyyppien (mukautettu, satunnainen ja UUID) yksinkertainen luominen;
- alan ilmaisten suunnitelmien joukossa, mahdollisuus käyttää peitenimiä "virallisempien" sähköpostilaatikoiden kanssa. Muut kilpailijat rajoittavat vain yhteen.


## Miinukset


- 10 peitenimeä ei ehkä riitä, jos aiot käyttää Simple Loginia laajasti. Tässä tapauksessa maksullinen paketti, joka on melko edullinen, on hyödyllinen, jos haluat lisätä mahdollisten peitenimien määrää.
- Ei ole mahdollista luoda peitenimeä, jolla on tietty nimi ja verkkotunnus. Valitsemamme nimen perään lisätty satunnainen loppuliite luo Address:n, jota voi parhaimmillaan kuvailla omituiseksi. Perinteiset sosiaaliset mediat kieltäytyvät yleensä myöntämästä tilejä, jotka on luotu tämäntyyppisillä sähköpostiosoitteilla. Nostr korjaa tämän!
- Jos lähetät viestin toiselle henkilölle peitenimen avulla, se päätyy helposti vastaanottajan roskapostikansioon. Ensimmäiseksi on suositeltavaa käyttää salanimeä vastaanottamiseen, aivan kuten tilin luomisen, postituslistalle tilaamisen jne. yhteydessä.