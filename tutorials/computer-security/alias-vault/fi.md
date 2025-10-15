---
name: Alias Vault
description: Tehokas työkalu salasanojen, kaksitekijätodennuksen ja peitenimien hallintaan (sisäänrakennetulla sähköpostipalvelimella) - Myös itse isännöitynä!
---

![cover](assets/cover.webp)



Verkkosivujen yksityisyys ja tietoturva on aihe, johon kaikkien on kiinnitettävä erityistä huomiota liiketoiminnasta riippumatta.



Nämä kysymykset ovat lisäksi osa jatkuvassa myllerryksessä olevaa maailmaa: yhä useammat kehittäjät osallistuvat aiheeseen ja tuovat toteutuksia vakiintuneisiin ratkaisuihin ja uusiin tuotteisiin.



Näin on **Leendert de Borst** ja hänen `Alias Vault`, vallankumouksellinen työkalu (ensimmäinen laatuaan), jonka avulla voit hallita ja tallentaa salasanoja, käyttää salasanatietueita verkkopalveluiden tunnistautumiseen, hallinnoida kaksitekijätodennusta, mutta mikä tärkeintä, generate:n todelliset _salasanat_, kaikki yhdessä Interface:ssa.



**Mutta Alias Vault ei lopu tähän**.



## Tärkeimmät ominaisuudet



Alias Vault toimii pilvipalvelimessa kehittäjän palvelimilla tai omassa infrastruktuurissaan, ja tähän vaihtoehtoon on saatavilla Docker-tiedostoja ja -kuva, jotka voi asentaa sciptin avulla. Web Interface:n lisäksi laajennuksia on saatavilla kaikille suosituille selaimille sekä mobiilisovelluksia iOS:lle ja Androidille; jälkimmäisen voi ladata myös F-Droidista ohittaen virallisen Google-kaupan.



Yhdessä Interface Alias Holvi on:




- Ilmainen ja avoin lähdekoodi**
- Salasanahallinta**, joka tallentaa kaikki monimutkaiset salasanat. Selainlaajennuksen avulla salasanahallinta täydentää kirjautumiset verkkosivuille
- 2FA**, tukemaan kaksitekijätodennusta
- Alias manager, jossa on upotettu sähköpostipalvelin**: Pikemminkin se luo varsinaiset alter-egot, jotka sisältävät etunimen, sukunimen, sukupuolen, käyttäjätunnuksen, salasanan ja syntymäpäivän (jos nämä tiedot vaaditaan).



Pakettiin kuuluu laaja ja perusteellinen dokumentaatio, joka auttaa uusia tulokkaita löytämään tämän tehokkaan työkalun.



## Ei henkilötietoja!



Se alkaa, kuten aina, [aliasvault.net](aliasvault.net) -sivustolta. Kuten mainittu, Alias Vaultia voi käyttää omalla palvelimella tai kehittäjän pilvipalvelusta, jotta siihen voi tutustua ennen siirtymistä itse isännöityyn ratkaisuun.



Sivustolla on todella silmäänpistävä ja hyvin ylläpidetty grafiikka, mutta kunnon jutut tulevat vasta, kun alat päästä käsiksi niihin: **luo tili**.



![img](assets/en/01.webp)



Valtavaksi yllätykseksesi huomaat, että Alias Vault ei kysy henkilökohtaisia tietoja: kaikki mitä tarvitset tilin luomiseen on mikä tahansa lempinimi, sinulle tuttu sana, kunhan se on käytettävissä. Hyväksy käyttöehdot, valitse sana ja jatka.



![img](assets/en/02.webp)



Aseta nyt **`master-salasana`**, joka on koko uuden järjestelmäsi tärkein tieto. Tämän yhden salasanan avulla olet itse asiassa ainoa, joka voi käyttää tiliäsi tai palauttaa sen, koska se pitää `holvisi` salattuna palvelimella, joka isännöi tietojasi.



![img](assets/en/03.webp)



Fakta: Olet luonut oman salasanahallinnan ja alias-hallinnan, mutta et ole antanut omaa toimivaa, yksityistä sähköpostiosoitettasi Address.



![img](assets/en/04.webp)



Alias Vault toivottaa sinut tervetulleeksi turvalliseen, uuteen, henkilökohtaiseen mutta myös tyhjään tilaan. Ja nyt alamme asuttaa sitä hieman.



Jos sinulla on jo salasanahallintaohjelma, voit tuoda tiedoston käyttämästäsi palvelimesta arvioidaksesi eroja muihin palveluntarjoajiin tai ehkä poistaa alias-hallintaohjelman, jotta voit hallita kaikkea yhdellä sovelluksella.



![img](assets/en/05.webp)



Alias Vault on erittäin yksinkertainen: sinulla on yksi pääsivu, joka on `Home`, ja kaksi valikkoa:




- `Credentials`: jonka avulla voit luoda ja hallita identiteettejä ja peitenimiä
- `Email`: Saapuneet viestit, josta voit tarkistaa saapuvat viestit luomillesi peitenimille.



![img](assets/en/06.webp)



Olemme kiinnostuneita ensimmäisen aliaksen luomisesta, joten siirry sivun oikeaan yläkulmaan ja valitse _+Uusi alias_.



![img](assets/en/07.webp)



Aluksi valikko näyttää Alias Vaultin filosofian mukaisesti vähäiseltä. Voit tutustua tämän toiminnon ominaisuuksiin napsauttamalla _Create via advanced mode_.



![img](assets/en/08.webp)



Ensimmäisen näytön yläosassa voit tuoda salasanatiedot, joita käytät jo palveluissa, joihin sinulla on tilaus tai joita käytät useimmiten verkossa.



Jos olet ottanut kaksitekijätodennuksen käyttöön jossakin (tai kaikissa) edellä mainituista palveluista, voit hallita tätä Layer-lisäturvaa Alias Holvissa tuomalla "salaisen avaimen". Alias Vault luo pääsyn edellyttämän `TOTP:n`.



![img](assets/en/09.webp)



**Varoitus**: Jos haluat käyttää oikeaa Address:ta, jolla olet aiemmin luonut tilejä, napsauta _Enter custom domain_, jotta voit asettaa oikean verkkotunnuksen `@` jälkeen.



![img](assets/en/14.webp)



Tämän näytön alaosa on hauskin. Napsauta _Generate Random Alias_ ja Alias Vault luo sinulle erillisiä identiteettejä eri tarpeisiin, joista jokaisella on oma postilaatikkonsa, erittäin vahvatasoiset salasanat, joita täydennetään muilla tiedoilla, kuten sukupuolella, syntymäajalla ja sopivalla lempinimellä.



![img](assets/en/10.webp)



Voit muuttaa salasanan luomiseen vaikuttavia asetuksia, kuten valita vain pienet kirjaimet ja poistaa moniselitteiset merkit.



![img](assets/en/11.webp)



Voit käyttää Alias Vaultin ehdottamaa alias-sähköpostia tai vaihtaa verkkotunnuksia, jos napsautat vastaavaa pudotusvalikkoa.



![img](assets/en/12.webp)



Ennen kuin käytät tätä sähköpostia kirjautumispalveluun, voit testata sen toimivuutta lähettämällä viestin omasta Address:stä juuri luotuun postilaatikkoon.



![img](assets/en/13.webp)



**⚠️ VAROITUS**: Sähköpostien vastaanottaminen on mahdollista Alias Vaultin sisäänrakennetun palvelimen ansiosta, mutta sen avulla voit vain vastaanottaa sähköposteja etkä vastata tai käyttää sähköpostilaatikkoa `alias`-palvelun "perinteisillä" toiminnoilla. Näin ollen se eroaa huomattavasti Simple Loginista, Addystä ja muista alustoista, jotka on tarkoitettu yksinomaan tämäntyyppiseen palveluun. Simple Loginin esimerkkiä varten voit tutustua omaan opetusohjelmaan:



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Jos haluat poistaa testinä luodun aliaksen, sinun tarvitsee vain kirjautua sisään `Kotiin`, sitten `Luottotiedot` ja napsauttaa identiteettiä, jonka haluat poistaa. Oikeaan yläkulmaan ilmestyy _Poista_-komento, jonka jälkeen voit jatkaa.



![img](assets/en/16.webp)



## Selaimen laajennus



Tarpeistasi riippuen voit turvautua selainlaajennukseen, joka löytyy yleisimmin käytetyistä selaimista.



![img](assets/en/15.webp)



Se asennetaan kuten kaikki muutkin laajennukset, joten en puutu tähän yksityiskohtaan.



Selainlaajennus helpottaa kirjautumista verkkopalveluihin tai uusien peitenimien luomista tarpeen mukaan: jos palvelu on tallennettu Alias Holvin tietueisiin, automaattinen täyttö tekee tarvittavan.



![img](assets/en/17.webp)



Ainoa varotoimi on varmistaa, että Alias Holvi on aktiivinen. Sovelluksessa on nimittäin oletusasetus, jonka mukaan se pysähtyy, kun se on ollut jonkin aikaa käyttämättömänä. Tämä on erittäin hyödyllinen ominaisuus, **jos sinun on esimerkiksi poistuttava tietokoneen luota ja estettävä jotakuta muuta käyttämästä tilejäsi**. Yksinkertaistetun menettelyn avulla voit kirjautua sisään uudelleen syöttämällä "pääsalasanan", jos edellinen istunto on vielä välimuistissa. Uloskirjautumisaika on yksi parametreista, joita voit mukauttaa lyhentämällä tai pidentämällä sitä mieltymystesi mukaan.



## Mobiilisovellus



Kuten kaikista tämäntyyppisistä sovelluksista, Alias Vaultista on versio mobiililaitteille sekä Android- että iOS-ympäristöissä. Androidille voit ladata sovelluksen osoitteesta [F-Droid](https://f-droid.org/packages/net.aliasvault.app/).



Tätä kirjoitettaessa (elokuun lopulla 2025) mobiilisovellus pitää "automaattista täyttämistä" kokeellisena ominaisuutena, joka ei toimi kuin hyvin harvojen sivustojen kanssa. Kunnes se on täysin toteutettu, Alias Vaultin käyttäminen mobiililaitteessa edellyttää tietojen kopiointia/liittämistä.



Kun olet ladannut sovelluksen kaupasta, kirjaudut sisään yksinkertaisesti syöttämällä verkkosovelluksessa luodun käyttäjän ja "pääsalasanan".



![img](assets/en/18.webp)



Kun avaat holvisi, sinulta kysytään, haluatko ottaa käyttöön biometrisesti valvotun pääsyn, joka on ylimääräinen Layer-turvatoiminto, jolla estetään muita käyttämästä salasanojasi, jos puhelimesi sattuu olemaan heidän kädessään.



![img](assets/en/19.webp)



Jos päätät ottaa käyttöön biometrisen tarkistuksen, tee se vain. Jos ohitat tämän vaiheen ja muutat mielesi, voit määrittää sen myös myöhemmin _Asetukset_-valikosta.



Kun olet kirjautunut sisään, jo luodut tiedot synkronoidaan uudelleen.



![img](assets/en/20.webp)



Mobiilisovellus voidaan ohjata omalla palvelimella sijaitsevan holvin linkkiin.



![img](assets/en/22.webp)



Seuraavassa jaksossa käsittelemme lyhyesti juuri itse isännöityä versiota Address.



## Self-Hosting: täysi määräysvalta tietojesi suhteen



Alias Vault ei ole reilusti sanottuna ensimmäinen salasanahallintajärjestelmä, jonka avulla voit ottaa palvelun käyttöön infrastruktuurissasi. On muitakin, mutta joissakin on rajoituksia tai ne ovat osittain suljetun lähdekoodin tuotteita.



Tilaisuus on ainutlaatuinen: **Lopeta riippuvuus ulkoisista palveluntarjoajista tai pilvipalvelimista, mutta käytä omaa paikallista palvelinta salasanojen, peitenimien ja kaikkeen liittyviin erittäin arkaluonteisiin tietoihin vartiointiin ja hallintaan**. Alias Vaultin avulla voit myös antaa sähköpostipalvelun osoittaa omalle sähköpostipalvelimellesi, mikä lisää luottamuksellisuutta.



On aika kääntyä [documentation](https://docs.aliasvault.net/installation/) puoleen saadaksesi selville, miten edetä Alias Vaultin omassa isännöinnissä.



![img](assets/en/23.webp)



Alias Vault toimii Docker Composella, joten Linuxista ja Dockerista tarvitaan vain vähän kokemusta. Voit aloittaa perusasennuksen ja täydentää sitä edistyneemmillä ratkaisuilla.



Palvelimesi on oltava 64-bittisessä koneessa, jossa on Linux-jakelu, 1 Gt RAM-muistia ja vähintään 16 Gt tallennustilaa; Dockerin (CE) version on oltava vähintään 20.10 tai uudempi, kun taas Docker Compose vaatii version 2.0 tai uudemman.



Päätin kokeilla Alias Vaultia ohuella asiakkaalla, johon on asennettu DietPi jakeluna, Debian Bookworm -pohja, joka on optimoitu olennaisiin asioihin ja jossa on jo käynnissä `Docker` ja `Docker Compose`.



Ensin, jotta saisit järjestystä, luo hakemisto kotiisi, avaa `terminal` ja liitä komento asennusskriptin suorittamiseksi.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Kun asennus on valmis, löydät käyttöoikeustietosi:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Tarkista hakemiston sisältö asennuksen jälkeen.



![img](assets/en/29.webp)



Voit käynnistää Alias Holvin komennolla:



```` Launch-Alias-Vault


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Salausta ja turvallisuutta koskevat näkökohdat



![img](assets/en/32.webp)



Lanedirtin sivustolla, dokumentaatiossa ja Githubissa ilmoittamien tietojen mukaan Alias Vaultin avulla **kaikki Alias Vaultiin sijoitetut tiedot (komponentit) pysyvät tiukasti sidottuina laitteeseen, salattuina ja saavuttamattomissa kenelle tahansa, joka ei tiedä `master-salasanaa`**.



Pääsalasana on siis koko holvin peruselementti. Kun se on syötetty, sitä käsitellään `Argon2id`-algoritmilla, joka on Hard-muistissa oleva avainten johdannaistoiminto, jotta salaisuus ei pääse poistumaan laitteesta.



Kaikki pysyy piilossa jopa pilvipalvelun tai hosting-palvelun hallinnoijalta. Hallintapaneelista ei itse asiassa pääse käsiksi käyttäjän tietoihin, voit vain tietää, ovatko he luoneet peitenimiä, vastaanottaneet sähköposteja ja vähän muuta.



Kaikki tallennettu sisältö salataan ja puretaan pääsalasanasta johdetuilla salausavaimilla. **Palvelimelle tallennetaan vain salattua tietoa, mikään ei näy tavallisena tekstinä**. Jos käyttäjä unohtaa tai kadottaa `master-salasanansa`, siihen liittyvä tili menetetään peruuttamattomasti, koska palvelin ei pääse käsiksi selkotekstisisältöön.



Itse isännöidyssä versiossa on skripti, joka nollaa `master-salasanan`, mutta tämä ei estä tietojen menetystä.



![img](assets/en/33.webp)



Koska Alias Holvi on _Beta_-vaiheessa, sinulla voi olla vaikeuksia päästä siihen käsiksi, jos muutat/päivität pääsalasanan. Suosittelen, että valitset sen alusta alkaen tukevaksi ja monimutkaiseksi, jotta voit kokeilla palvelua ja lopulta päättää, haluatko käyttää sitä. Jos sinulla on vaikeuksia päästä pilvipalveluun salasanan päivittämisen jälkeen, ota yhteyttä Alias Vaultin tukeen.



Jos haluat täydellisen käsityksen Alias Vaultin arkkitehtuurista ja tietoturvasta, suosittelen, että tutustut [tähän sivuun](https://docs.aliasvault.net/architecture/), jossa on yksityiskohtaisia tietoja sen toiminnan taustalla olevasta salakirjoituksesta.



## Tiekartta


Kehittäjien tarkoituksena on tehdä Alias Vaultista kypsä ja vakaa vuoden 2025 loppuun mennessä, jotta sen tulevat käyttöominaisuudet voidaan määritellä.



Alias Vault on ja pysyy aina avoimen lähdekoodin ja ilmaisena, mutta ei luultavasti rajattomasti kuten beta-versiossa. Joitakin maksullisia ominaisuuksia ollaan toteuttamassa, kuten on jo ilmoitettu.



Tarjolla on tiimi-/perhesuunnitelmia ja tuki laitteistoavaimille, joista jälkimmäinen on tarkoitettu FIDO2- tai WebAuth-todennukseen.



## Kuka tarvitsee Alias Holvin



**Tämmöinen työkalu on ihanteellinen kaikille, joille yksityisyys verkossa on tärkeintä**.



Henkilöllisyytesi on mitä todennäköisimmin verkkoliiketoimintasi ytimessä, ja se on suojattava kaikin keinoin, jotta **tämä** tieto voidaan pitää poissa palveluilta, yrityksiltä ja välittäjiltä, jotka ovat valmiita tekemään mitä tahansa saadakseen käsiinsä verkkokäyttäytymisesi.



Alias Vault antaa sinulle takaisin täydellisen hallinnan valtakirjoistasi ja vähentää tai poistaa kokonaan tarpeen luottaa kolmansien osapuolten vartiointiin ja salaukseen kaikkein arkaluonteisimmissa tiedoissasi.



Alias Vaultin arkkitehtuuri ja salausmahdollisuudet sopivat erinomaisesti suvereeneille yksityishenkilöille, pienille ja keskisuurille yrityksille, kehitystiimeille ja kaikille **avoimen lähdekoodin** sovellusten harrastajille. Jos kuulut johonkin näistä kategorioista: pidä hauskaa Alias Vaultin löytämisessä.