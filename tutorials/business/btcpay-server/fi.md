---
name: BTCPay-palvelin
description: BTC-maksujen vastaanottaminen ilman välikäsiä
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server on Nicolas Dorierin luoma ilmainen, avoimen lähdekoodin ohjelmistopaketti, joka mahdollistaa bitcoin-maksujen hyväksymisen ilman välikäsiä. Se on suunniteltu tarjoamaan itsenäisyyttä ja taloudellista riippumattomuutta, ja se asennetaan omalle palvelimelle ja tarjoaa täydellisen tapahtumien hallinnan laskutuksesta on-chain- tai Lightning Network-maksujen validointiin ja kirjanpitoon. Se integroituu helposti verkkokauppasivustoihin (WooComerce, Shopify jne.) tai sitä voidaan käyttää fyysisten myymälöiden maksupäätteenä (*POS*).



BTCPay Server on epäilemättä edistyksellisin ratkaisu kauppiaille, jotka haluavat hyväksyä bitcoinin. Se on kattavin ja vankin ohjelmisto turvallisuuden, riippumattomuuden ja luottamuksellisuuden kannalta. Toisaalta se on myös monimutkaisin asentaa ja ylläpitää. On olemassa myös yksinkertaisempia vaihtoehtoja: jotkut ovat täysin säilyttäjiä, kuten OpenNode, kun taas toiset tarjoavat mielenkiintoisen kompromissin helppokäyttöisyyden ja riippumattomuuden välillä, kuten sveitsiläinen Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Tämän ohjeen tarkoituksena on opastaa sinua askel askeleelta BTCPay Serverin asennuksessa, konfiguroinnissa ja käytössä, jotta voit ottaa käyttöön turvallisen ja riippumattoman maksuinfrastruktuurin Bitcoin:n eetoksen mukaisesti.



## BTCPay-palvelimen ominaisuudet



Keskitetyt Bitcoin-myyntipistoratkaisut, kuten esimerkiksi *OpenNode*, ovat helppokäyttöisiä, mutta ne ovat riippuvaisia kolmannen osapuolen yrityksestä, koska niitä ei voi itse isännöidä ja ne ovat useimmissa tapauksissa patentoituja. Vaikka ne helpottavat maksujen perustamista, niihin liittyy välityspalkkioita ja ne altistavat käyttäjänsä suuremmille riskeille kuin BTCPay Serverin kaltainen ratkaisu sekä varojen säilytyksen että luottamuksellisuuden osalta.



BTCPay Server on tarkoitettu online- tai fyysisille kauppiaille, yhdistyksille ja voittoa tavoittelemattomille organisaatioille, jotka haluavat vastaanottaa lahjoituksia bitcoineina. Se on myös ihanteellinen ratkaisu projektin omistajille ja kehittäjille, jotka haluavat suoraa tukea yhteisöltään.



BTCPay Serverin erityispiirteisiin kuuluvat:




- sen **täydellinen riippumattomuus**,
- **KYC**-menettelyn puuttuminen,
- varojen täysi valvonta**,
- **alustamaksujen poistaminen**.



Kun sinusta tulee oma maksuprosessorisi, et ole enää riippuvainen keskitetystä kolmannesta osapuolesta sinun ja asiakkaidesi välillä. Voit hyväksyä maksuja suoraan bitcoineina ja generate-maksulaskuja. Näin varmistetaan, ettei kukaan muu voi kieltää sinua tai yritystäsi. Toimit sekä pankin että maksujen käsittelijän roolissa, eikä sinun tarvitse maksaa välittäjälle palkkioita jokaisesta tapahtumasta.



**on-chain**-verkon transaktiomaksut säilyvät, mutta niitä voidaan alentaa käyttämällä **Liquid**- tai **Lightning**-verkkoa.



Lisäksi :




- Täysin muokattava käyttöliittymä ja laskut;
- Oma **Tor**-tuki parantaa luottamuksellisuutta;
- Tuki **crowdfunding**-, **POS**- ja **maksupainikkeille**;
- Yhteensopiva monien valuuttojen kanssa ;
- Bitcoin suorat ja vertaisverkkomaksut ;
- Yksityisten avainten täydellinen hallinta;
- Parannettu yksityisyys ;
- Parannettu turvallisuus ;
- Itsehallinnoitu ohjelmisto ;
- Tuki **SegWit**:lle** ja **Lightning-verkolle** ;
- Sisäinen, solmupohjainen salkku, johon on integroitu laitteistosalkkuja.



## BTCPay-palvelimen asentaminen ja konfigurointi



### Hosting-tilan valitseminen



BTCPay Server voidaan asentaa useilla eri tavoilla. Tarpeistasi ja resursseistasi riippuen on kolme päävaihtoehtoa:




- Kolmannen osapuolen isännöimä BTCPay-palvelin**: käytät alustaa, joka isännöi palvelua puolestasi. Se on yksinkertaista, mutta ei yleensä ilmaista.
- BTCPay-palvelin, joka on itse isännöity pilvipalvelimella** (esim. [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) tai jonkin muun palveluntarjoajan kautta). Tämä on suositeltava ratkaisu useimmille aloitteleville kauppiaille.
- BTCPay Server asennettuna omalle laitteistollesi (paikallisesti)** : tietokoneeseen, mini-PC:hen tai Umbreliin. Tämä menetelmä on teknisempi, mutta tarjoaa täydellisen riippumattomuuden.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Aloittelevalle kauppiaalle **käyttöönotto pilvipalvelimella** on paras kompromissi itsenäisyyden, yksinkertaisuuden ja turvallisuuden välillä ilman, että hänen tarvitsee hallita koko teknistä infrastruktuuria.



BTCPay Server voidaan ottaa nopeasti käyttöön useilta hosting-palveluntarjoajilta. Niiden joukossa **Voltage** erottuu vertailuratkaisuna käyttäjille, jotka tarvitsevat **luotettavan**, **ammattimaisen** ja **valtiollisen** infrastruktuurin.



### Luo BTCPay-palvelininstanssi Voltageen



**Voltage** on avaimet käteen -periaatteella toimiva Bitcoin- ja Lightning-hostausalusta, jonka avulla voit ottaa heti käyttöön oman BTCPay-palvelimesi ilman monimutkaisia konfiguraatioita tai palvelimen ylläpitoa.



Käy [virallinen Voltage-sivusto](https://voltage.cloud).



![capture](assets/fr/03.webp)



Luo **käyttäjätili**, jolla on voimassa oleva sähköpostiosoite ja vahva salasana.



![capture](assets/fr/04.webp)



Voltage tarjoaa **ilmaisen 7 päivän kokeilujakson**. Huomaa, että 7 päivän ilmaisen kokeilujakson jälkeen sinua pyydetään tekemään **25 dollarin kuukausittainen** kiinteä tilaus, jotta voit jatkaa **solmujesi pitämistä aktiivisena**.



Kun olet luonut Voltage-tilisi ja kirjautunut sisään ensimmäistä kertaa, sinut ohjataan etusivulle, jossa on kaksi pääosiota:




- **Infrastruktuuri**-osio Lightning-solmujen, Bitcoin Core:n, BTCPay Serverin ja muiden Bitcoin-palvelujen hallintaa varten pilvipalvelussa;
- ja **Maksut**-osio, jonka avulla voit käyttää Voltagen API Lightningia Bitcoin-maksujen integroimiseksi räätälöityihin sovelluksiin.



Jos haluat ottaa käyttöön **BTCPay Server**-instanssin, napsauta **Access infrastructure**. Täällä voit luoda, hallita ja valvoa kaikkia palveluitasi, mukaan lukien Bitcoin-solmua ja BTCPay Serveriä.



#### Luo ryhmä



Ennen kuin voit ottaa palvelun käyttöön, alusta pyytää sinua **luomaan ryhmän**. **Ryhmä** (työtila) on työtila, joka kokoaa yhteen kaikki Bitcoin- ja Lightning-palvelusi (esim. solmu, BTCPay-palvelin, explorer jne.). Se on vähän kuin kansio, joka sisältää eri projektisi.



![capture](assets/fr/05.webp)



Tässä oppaassa luomamme ryhmän nimi on **Genesis**. Voit halutessasi lisätä profiilikuvan. Kun tämä on tehty, napsauta **Luo**-painiketta. Voit kutsua muita käyttäjiä liittymään ryhmään ja jopa muuttaa ryhmän nimeä, jos haluat.



Ryhmän etusivulla näkyy useita vaihtoehtoja:




- Lightning-solmut** : kokonaisen Lightning-solmun käyttöönotto (LND) ;
- Bitcoin Core Nodes** : käynnistääksesi kokonaisen Bitcoin-solmun ;
- BTCPay-palvelin** : isännöi käyttövalmista BTCPay-instanssia;
- Nostr-tilit**: Nostr-tunnusten hallintaan.



Aktivoi **kaksoistodennus (2FA)** tilisi ja palvelujesi suojaamiseksi (painike näkyy punaisena, jos se on poistettu käytöstä).



![capture](assets/fr/06.webp)



Valitse vaihtoehdoista **BTCPay Server** ja sitten **Launch a BTCPay Store**.



![capture](assets/fr/07.webp)



Voltage pyytää sinua sitten **luomaan ja konfiguroimaan BTCPay-palvelimen** valitsemalla **palvelun nimen** (1) ja ottamalla Lightning-maksut käyttöön (2).



Tarvitset Lightning-solmun, jos päätät hyväksyä Lightning-maksuja.



Jos sinulla ei vielä ole Bitcoin- tai Lightning-solmua, Voltage ehdottaa, että luot sellaisen automaattisesti.



Napsauta **Luo salamasolmu** (3) .



![capture](assets/fr/08.webp)



Kun pääset solmun luomiskäyttöliittymään, sinua pyydetään valitsemaan **standardin** ja **ammattilaisen** ulkoasun välillä.



Voit luoda todellisen solmun (**Mainnet**) tai testisolmun (**Testnet**). Napsauta sitten **Jatka**-painiketta.



![capture](assets/fr/09.webp)



Tässä ohjeessa käytetään vakiosuunnitelmaa. Syötä **solmun nimi**, **salasana** ja paina **Luo**-painiketta.



![capture](assets/fr/10.webp)



Muutaman hetken kuluttua solmusi on toiminnassa ja voit avata vapaan kanavan, jonka vastaanottokapasiteetti on 500 000 sats.



![capture](assets/fr/11.webp)



Hieman alempana oikealla löydät kaikki tarvittavat tiedot solmusta!



![capture](assets/fr/12.webp)



Nyt kun Lightning-solmumme on toiminnassa, palataan BTCPay-palvelimen asentamiseen. Voit nyt napsauttaa **Create BTCPay**-painiketta.



![capture](assets/fr/13.webp)



Avautuu sivu, jossa on oletuskirjautumistietosi ja viesti, jossa kehotetaan vaihtamaan alkuperäinen salasana. Kun olet tehnyt tämän, napsauta **Login Now** -painiketta päästäksesi käyttöliittymään.



![capture](assets/fr/14.webp)



Juuri noin! BTCPay-palvelimesi on valmis käytettäväksi. Sinut ohjataan suoraan BTCPay-palvelimesi kirjautumissivulle.



![capture](assets/fr/15.webp)



Kun olet kirjautunut sisään, määritä ensimmäinen **kauppa**:





- Anna sille **nimi**.





- Valitse ** oletusvaluutta** (EUR, USD, CFA jne.).





- Valitse **valuuttakurssin tarjoaja** (esim. CoinGecko).



![capture](assets/fr/16.webp)



Tämän jälkeen sinut ohjataan kauppasi kojelautaan. Kojelaudan käyttöliittymässä huomaat, että **Luo myymäläsi**-painike on merkitty vihreällä, koska tämä vaihe on jo suoritettu.



![capture](assets/fr/17.webp)



Hieman alempana on painikkeet **Konfiguroi wallet** ja **Konfiguroi Lightning-solmu**. Meidän tapauksessamme olemme jo yhdistäneet Lightning-solmuun, joka toimii jännitteellä. Meidän ei siis tarvitse tehdä sitä tässä.



Siirrytään portfolion määrittämiseen. Napsauta **Salkun määrittäminen**-painiketta.



Koska olemme vasta aloittamassa BTCPay Serverin käyttöä, yhdistetään olemassa oleva wallet. Paina siis **Yhdistä olemassa oleva salkku**.



![capture](assets/fr/18.webp)



Tämän jälkeen sinun on valittava **tuontimenetelmä**. Valitse käytettävissä olevista vaihtoehdoista **Syötä laajennettu julkinen avain**.



![capture](assets/fr/19.webp)



Yhdistämällä olemassa olevan wallet:n voit vastaanottaa maksuja **suoraan tähän ulkoiseen wallet:een** ilman, että BTCPay-palvelin pääsee käsiksi yksityiseen avaimeesi. Joten vaikka palvelin hakkeroitaisiin tai julkinen avain (`xpub`) vaarantuisi, hyökkääjä voisi nähdä tapahtumahistoriasi, mutta hänellä ei olisi **mahdollisuutta päästä käsiksi varoihisi**.



Kun napsautat **Syötä laajennettu julkinen avain** -painiketta, sinut **ohjataan** sivulle, jossa sinun on annettava tämä avain.



Haetaan nyt **laajennettu julkinen avain**.



### Bitcoin wallet:n liittäminen



Jotta voit vastaanottaa maksuja, sinun on liitettävä Bitcoin wallet myymälääsi. Tätä varten sinulla on useita vaihtoehtoja:





- Laitesalkku** (Ledger, Trezor, Coldcard ...) ;





- Ohjelmistovalikoima** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- BTCPay Server** sisäinen wallet (ei suositella, koska se ei ole yhtä turvallinen ja varasi ovat enemmän alttiina palvelimen hakkeroinnin yhteydessä).



Tässä oppaassa käytämme **ohjelmistosalkkua**, joka on helpommin käytettävissä alkukonfigurointia varten. Voit valita useista yhteensopivista sovelluksista: **Electrum**, **Phoenix**, **Zeus**, **Muun** jne.



Käytämme esittelyssä **Electrum**. Avaa **Electrum**, napsauta **Portfolio** ja sitten **Tiedot** :



![capture](assets/fr/20.webp)



Seuraavaksi kopioi **pääkäyttäjän julkinen avain (xpub)**.



![capture](assets/fr/21.webp)



Kun olet kopioinut julkisen yleisavaimen, liitä se BTCPay Server -sivulla olevaan kenttään.



![capture](assets/fr/22.webp)



Vahvistuksen jälkeen sinut ohjataan kauppasi kojelautaan.



![capture](assets/fr/23.webp)



### Luo myyntipiste (PoS)



Kun olet perustanut myymälän ja portfolion, voit nyt perustaa **myyntipisteen (PoS)** ja aloittaa Bitcoin-maksujen vastaanottamisen suoraan asiakkailtasi.



Tämä **BTCPay Serverin** integroitu ominaisuus on ihanteellinen **kauppiaille, käsityöläisille, ravintoloitsijoille tai palveluntarjoajille**, jotka haluavat hyväksyä Bitcoin:n **ilman verkkosivuja** tai erityisiä teknisiä taitoja.



### Mikä on myyntipiste?



**PoS** on **yksinkertaistettu POS-liitäntä**, joka toimii **Bitcoin-maksupäätteenä**.


Sen avulla voit :




- Luo **tuotteiden tai palveluiden valikko**, jossa on kiinteät hinnat.
- Luo **pikalasku, jossa on skannattava QR-koodi**.
- Jaa **Maksun URL-osoite**, jota voi käyttää älypuhelimella, tabletilla tai tietokoneella.



Toisin sanoen PoS muuttaa BTCPay-palvelimesi **suoraksi myyntiliittymäksi**, jossa jokainen maksu vastaanotetaan **omaasi Bitcoin wallet:een** ilman välikäsiä.



### PoS:n määrittäminen



Klikkaa BTCPayn kojelaudassa **PLUGINS** ja sitten **Point of sale**.



Napsauta sitten **Luo uusi PoS-sovellus**. Tämä toiminto lisää **uusen sovelluksen** BTCPay-kauppaasi, aivan kuin asentaisit sisäisen minimyyntisivuston.



Sivu avautuu sovelluksen luomista varten. Määritä **sovelluksen nimi**: tämä on sisäinen nimi, joka näkyy vain kojelaudalla (esim. _Shoe Shop_).



Klikkaa **Luo** vahvistaaksesi.



![capture](assets/fr/24.webp)



Luomisen jälkeen sinut ohjataan myyntipisteen **Tarkat määritykset -sivulle**.



### Mukauta myyntikäyttöliittymääsi



Tällä sivulla voit määritellä PoS:n keskeiset osat:





- Sovelluksen nimi** (sisäinen hallinnointinimi, voidaan muuttaa milloin tahansa).





- Näytön otsikko** (mitä asiakkaasi näkevät sivun yläosassa).





- Myyntipisteen tyyli** (**Kuvaus**-tila sopii palveluihin, kuten hiustenleikkauksiin tai aterioihin, kun taas **Tuotekatalogi**-tila on ihanteellinen useita tuotteita tarjoaville myymälöille).





- Näytä valuutta** (valitse **XOF**, **EUR** tai **USD** tavanomaisten hintojen mukaan).





- Tuoteluettelo** (lisää tuotteesi, kuvaukset ja hinnat tähän).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Tallenna ja testaa PoS



Kun olet saanut asetukset valmiiksi, tallenna asetukset napsauttamalla **Tallenna** ja sitten **Katsele** esikatsellaksesi PoS:ää.



Näet sivun, jossa esitellään tuotteesi, ja jokainen painike vastaa tuotetta tai palvelua.



Heti kun asiakas valitsee tuotteen :



1. BTCPay luo automaattisesti Bitcoin- tai Lightning**-laskun.



2. Näyttöön ilmestyy **QR-koodi**.



3. Asiakkaat voivat **skannata ja maksaa suoraan** Bitcoin wallet:llä.




![capture](assets/fr/27.webp)



### Lopputulos



Sinulla on nyt täydellinen **Bitcoin-myyntipiste**, jonka voit :





- Avaa älypuhelimesta tai tabletista myymälässäsi ;





- Näyttö näytöllä asiakkaan skannattavaksi ;





- Tai jaa julkisella **URL**:lla, kuten yksinkertaistetun tilaussivun kautta.



Jokaisen maksun yhteydessä summa hyvitetään automaattisesti **omaasi BTCPay wallet:ään** ilman välikäsiä tai kolmannen osapuolen maksuja.


Tämä tekee PoS:stä **yksittäisen Bitcoin-maksupäätteen**.




## Jokapäiväinen käyttö



Suosittelemme, että teet **testauksen** ennen todellisten maksujen lunastamista, jotta voit tarkistaa, että kaikki toimii oikein.



### Testaa maksu





- Luo lasku** PoS-käyttöliittymästäsi (esimerkiksi 1 satoshi-tuote tai pieni summa).





- Skannaa näytön QR-koodi** Bitcoin- tai Lightning wallet -laitteella (kuten **Phoenix**, **Muun** tai **Wallet tai Satoshi**).




![capture](assets/fr/28.webp)





- Vahvista maksu** wallet:ssäsi: maksutapahtuma lähetetään välittömästi.





- Palaa BTCPay-palvelimelle**: lasku näkyy luettelossa **maksettu**.



![capture](assets/fr/29.webp)



Onnittelut! Myyntipisteesi on nyt **toimiva**. Voit alkaa vastaanottaa Bitcoin-maksuja asiakkailtasi yksinkertaisesti, nopeasti ja ilman välikäsiä.



### Luo lasku asiakkaalle



Valitse **Laskut**-valikosta **Uusi lasku**.



![capture](assets/fr/30.webp)



Syötä **summa** ja **paikallinen valuutta** (BTCPay laskee automaattisesti vastaavan summan BTC:nä) sekä muut tuotetiedot.



![capture](assets/fr/31.webp)



Jaa **QR-koodi** tai **URL** asiakkaan kanssa.



![capture](assets/fr/32.webp)



### Seuraa vastaanotettuja maksuja



Edelleen **Laskut**-valikossa näet luettelon kaikista tapahtumista.


Mahdolliset tilat ovat :





- Vireillä**: maksua ei ole vielä vahvistettu.





- Maksettu**: maksu vahvistettu.





- Vanhentunut**: lasku, jota ei ole maksettu eräpäivään mennessä.



### Asiakkaan hyvittäminen



Valitse korvattava lasku **Laskut**-valikosta.



![capture](assets/fr/33.webp)



Napsauta **Refund** ja syötä asiakkaan antama Bitcoin-osoite.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Raportit ja tietojen vienti



BTCPay Serverin avulla voit **viedä tapahtumia** (CSV- tai Excel-muodossa). Tämä on erittäin käytännöllistä kirjanpidon ja kassan seurannan kannalta.



![capture](assets/fr/36.webp)



Napsauta **Raportti**-valikossa **Vie**: kaikki tapahtumat tallennetaan CSV-tiedostoon, jota voit sitten tarkastella paikallisesti.



## Turvallisuus ja parhaat käytännöt



BTCPay Serverin antama itsenäisyys (täysi määräysvalta varoistasi) on todellinen vahvuus. Mutta tämän vapauden myötä tulee myös suurempi vastuu turvallisuudesta. Hallitsemalla omia maksujasi otat oman pankkisi roolin. Siksi on ehdottoman tärkeää ottaa käyttöön parhaat käytännöt varojen, tietojen ja infrastruktuurin suojaamiseksi. Tässä ovat tärkeimmät huomioon otettavat seikat.



### Turvallinen pääsy palvelimelle





- Käytä vahvaa salasanaa: yhdistele isoja ja pieniä kirjaimia, numeroita ja erikoismerkkejä. Vältä olemassa olevan salasanan uudelleenkäyttöä.
- Aktivoi kaksitekijätodennus (2FA), jotta pääset BTCPay-käyttöliittymään.
- Päivitä säännöllisesti käyttöjärjestelmäsi, BTCPay Server -instanssisi ja riippuvuussuhteesi (Docker, Bitcoin-solmu, Lightning-solmu...). Päivitykset korjaavat usein tietoturva-aukkoja.



### Yksityisten avainten hallinta ja varmuuskopiointi





- Tallenna yksityiset avaimesi ja siemenlausekkeet offline-tilassa fyysiselle tietovälineelle (paperille tai metallille).
- Käytä mieluiten wallet-laitteistoa wallet.
- Pidä varmuuskopioista useita kopioita erillisissä, suojatuissa fyysisissä paikoissa.



### Turvalliset maksut ja luottamuksellisuus





- Käytä Tor-verkkoa tai VPN:ää piilottaaksesi palvelimesi IP-osoitteen ja suojellaksesi yksityisyyttäsi.
- Poista tarpeettomat portit käytöstä palvelimesta ja rajoita SSH-yhteydet vain luotettaviin osoitteisiin.
- Aktivoi HTTPS (SSL-sertifikaatti) kaikille yhteyksille BTCPayn verkkokäyttöliittymään.
- Älä koskaan jaa hallintaliittymää sellaisten henkilöiden kanssa, joilla ei ole Bitcoin-salkunhallinnan koulutusta.



### Salama-verkon parhaiden käytäntöjen käyttöönotto



Myymäläsi on liitetty Voltage**:ssa isännöidyn **Lightning-solmun yhteyteen, mikä yksinkertaistaa huomattavasti verkon teknistä hallintaa. On kuitenkin edelleen tärkeää noudattaa **hyviä valvonta- ja turvallisuuskäytäntöjä**:





- Tallenna Voltage-solmun API**-kirjautumis- ja pääsyavaimet (joiden avulla BTCPay voi muodostaa yhteyden).
- Suojaa Voltage-tilisi** kaksitekijätodennuksella ja vahvalla salasanalla.
- Seuraa solmujen ja kanavien tilaa** Voltage-kojelaudalta: tämä auttaa sinua havaitsemaan mahdolliset poikkeamat tai epäsynkronoinnin.
- Vältä API**-tunnisteidesi jakamista tai paljastamista julkisesti (esim. sivuston koodissa).
- Siirtymistapauksessa riittää, että **konfiguroit BTCPayn ja Voltagen välisen linkin uudelleen**: kanavaa ei tarvitse sulkea manuaalisesti.



Voltagen avulla voit hyödyntää **turvallista, korkeasti saatavilla olevaa** ja **automaattisesti varmuuskopioitua** infrastruktuuria ja säilyttää samalla **täyden määräysvallan Lightning-maksuistasi**.



### Sisäisten menettelyjen organisointi ja jäsentäminen





- Määrittele selkeä käyttöoikeuksien hallintakäytäntö: kuka voi luoda laskun, tarkastella maksuja, käyttää solmua jne.
- Dokumentoi varmuuskopiointi- ja palautusmenettelyt, jotta voit reagoida nopeasti häiriötilanteessa.
- Testaa säännöllisesti varmuuskopioiden palauttaminen varmistaaksesi, että ne toimivat oikein.
- Kouluta henkilöstöäsi tai yhteistyökumppaneitasi perusturvallisuuteen liittyvissä asioissa: valppaus tietojenkalastelua vastaan, turvallisten salasanojen käyttö ja luottamuksellisuuden kunnioittaminen.



### Valvoa ja luoda jatkuva ylläpito





- Seuraa jatkuvasti palvelimesi toimintaa loki- tai seurantatyökalujen avulla.
- Suunnittele säännöllinen tietoturvatarkastus: tarkista päivitykset, käyttöoikeudet, varmuuskopiot ja tapahtumien yhdenmukaisuus.



Onnittelut! Olet päässyt tämän ohjeen loppuun. Voit nyt tutustua BTCPay Serveriin itsenäisesti, mikä helpottaa kauppasi hallintaa.



Jos haluat lisätietoja, suosittelen, että osallistut Bitcoin:n integroimisesta yritykseesi järjestettävään täydelliseen koulutukseen:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a