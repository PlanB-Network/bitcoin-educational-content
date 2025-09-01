---
name: Graylog
description: Keskitä ja analysoi lokit helposti
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian BURNELin alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___



## Graylogin käyttöönotto Debian 12:ssa



### I. Esittely



Graylog on avoimen lähdekoodin "lokinieluratkaisu", joka on suunniteltu keskittämään, tallentamaan ja analysoimaan koneiden ja verkkolaitteiden lokitietoja reaaliajassa. Tässä ohjeessa opimme, miten Graylogin ilmainen versio asennetaan Debian 12 -koneeseen!



Tietojärjestelmässä jokainen **palvelin**, olipa se sitten **Linux**- tai **Windows**-käyttöjärjestelmä, ja jokainen **verkkolaite** (kytkin, reititin, palomuuri jne...) ** tuottaa omat lokinsa**, jotka tallennetaan paikallisesti. Kun lokit tallennetaan paikallisesti jokaiseen koneeseen, tapahtumien analysointi ja korrelaatio on hyvin vaikeaa... Tässä kohtaa **Graylog** astuu kuvaan. Se toimii **lokinieluna**, mikä tarkoittaa, että **kaikki koneesi lähettävät sille lokinsa** (esimerkiksi syslogin kautta). Graylog sitten **varastoi ja indeksoi nämä lokit** ja antaa sinulle mahdollisuuden tehdä maailmanlaajuisia hakuja ja luoda hälytyksiä.



Graylog on analyysi- ja valvontatyökalu, joka helpottaa epäilyttävän käyttäytymisen ja erilaisten ongelmien (vakaus, suorituskyky jne.) tunnistamista.




![Image](assets/fr/034.webp)



**Huomaa: ilmainen versio, **Graylog Open**, ei ole SIEM, kuten Wazuh on, varsinkin kun siitä puuttuu todelliset tunkeutumisen havaitsemistoiminnot.



### II. Edellytykset



**Stack Graylog** perustuu **moneen komponenttiin**, jotka meidän on asennettava ja konfiguroitava. Tässä asennamme kaikki komponentit samalle palvelimelle, mutta on mahdollista luoda useisiin solmuihin perustuvia klustereita ja jakaa roolit useille palvelimille. Tässä ohjeessa asennamme **Graylog 6.1**, joka on tähän mennessä uusin versio.





- MongoDB 7**, Graylogin nykyinen suositeltu versio (vähintään 5.0.7, enintään 7.x)
- OpenSearch**, Amazonin luoma avoimen lähdekoodin Fork Elasticsearchista (vähintään 1.1.x, enintään 2.15.x)
- OpenJDK 17**



**Graylog-palvelin** toimii **Debian 12**:lla, mutta asennus on mahdollista myös muihin jakeluihin, myös Dockerin kautta. Virtuaalikoneessa on **8 Gt RAM-muistia** ja **256 Gt levytilaa**, jotta resursseja riittää kaikille komponenteille (muutoin tämä voi vaikuttaa merkittävästi suorituskykyyn). Annan tämän kuitenkin karkeana ohjeena, sillä **Graylog-arkkitehtuurin mitoitus riippuu käsiteltävän tiedon määrästä**. Graylog voi käsitellä 30 MB tai 300 MB dataa päivässä, samoin kuin 300 GB dataa päivässä.... Se on **skaalautuva ratkaisu**, joka pystyy käsittelemään **teratavun lokitietoja** (ks. [tämä sivu](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Lähde: Graylog



Ennen konfiguroinnin aloittamista määritä Graylog-koneelle staattinen IP Address ja asenna uusimmat päivitykset. Muista asettaa paikallisen koneen aikavyöhyke ja määrittää NTP-palvelin päivämäärän ja ajan synkronointia varten. Tässä on suoritettava komento:



```
sudo timedatectl set-timezone Europe/Paris
```



**Huomaa: **OpenSearchin asennus on valinnainen**, jos käytät sen sijaan **Graylog Data Nodea**.



### III Graylogin vaiheittainen asennus



Aloitetaan päivittämällä pakettivälimuisti ja asentamalla työkalut, joita tarvitsemme tulevaa varten.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. MongoDB:n asentaminen



Kun tämä on tehty, aloitamme MongoDB:n asentamisen. Lataa MongoDB-tietovarastoa vastaava GPG-avain:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Lisää sitten MongoDB 6 -arkisto Debian 12 -koneeseen:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Seuraavaksi päivitämme pakettivälimuistin ja yritämme asentaa MongoDB:n:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



MongoDB:tä ei voida asentaa, koska jokin riippuvuus puuttuu: **libssl1.1**. Meidän on asennettava tämä paketti manuaalisesti ennen kuin voimme jatkaa, koska Debian 12:n arkistoissa ei ole sitä.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Lataamme DEB-paketin nimeltä "**libssl1.1_1.1.1.1f-1ubuntu2.23_amd64.deb**" (uusin versio) komennolla **wget** ja asennamme sen komennolla **dpkg**. Tämä tuottaa seuraavat kaksi komentoa:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Käynnistä MongoDB-asennus uudelleen:



```
sudo apt-get install -y mongodb-org
```



Käynnistä sitten MongoDB-palvelu uudelleen ja anna sen käynnistyä automaattisesti, kun Debian-palvelin käynnistetään.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Kun MongoDB on asennettu, voimme siirtyä seuraavan komponentin asentamiseen.



#### B. OpenSearchin asentaminen



Siirrytään OpenSearchin asentamiseen palvelimelle. Seuraava komento lisää OpenSearch-pakettien allekirjoitusavaimen:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Lisää sitten OpenSearch-tietovarasto, jotta voimme ladata paketin **apt**:lla jälkikäteen:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Päivitä pakettien välimuisti:



```
sudo apt-get update
```



Asenna sitten OpenSearch** ja huolehdi siitä, että **määrität oletussalasanan instanssisi Admin**-tilille. Tässä salasana on "**IT-Connect2024!**", mutta korvaa tämä arvo vahvalla salasanalla. **Vältä heikkoja salasanoja**, kuten "**P@ssword123**", ja käytä vähintään **8 merkkiä**, joissa on vähintään yksi merkki jokaista tyyppiä (pienaakkoset, isot kirjaimet, numerot ja erikoismerkit), muuten asennuksen lopussa tulee virhe. **Tämä on edellytys OpenSearch 2.12.**:sta lähtien



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Ole kärsivällinen asennuksen aikana...



Kun olet valmis, tee hetki minimikokoonpano. Avaa konfigurointitiedosto YAML-muodossa:



```
sudo nano /etc/opensearch/opensearch.yml
```



Kun tiedosto on avattu, aseta seuraavat asetukset:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Tämä OpenSearch-konfiguraatio on suunniteltu yhden solmun perustamiseen. Seuraavassa on joitakin selityksiä käyttämistämme eri parametreista:





- cluster.name: graylog**: tämä parametri nimeää OpenSearch-klusterin nimellä "**graylog**".
- node.name: ${HOSTNAME}**: solmun nimi asetetaan dynaamisesti vastaamaan paikallisen Linux-koneen nimeä. Vaikka meillä on vain yksi solmu, on tärkeää nimetä se oikein.
- path.data: /var/lib/opensearch**: tämä polku määrittää, minne OpenSearch tallentaa tietonsa paikallisella koneella, tässä tapauksessa "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: tämä polku määrittelee, minne OpenSearchin lokitiedostot tallennetaan, tässä tapauksessa "**/var/log/opensearch**".
- discovery.type: single-node**: tämä parametri määrittää OpenSearchin toimimaan yhden solmun kanssa, minkä vuoksi valitaan vaihtoehto "**single-node**".
- network.host: 127.0.0.1**: tämä määritys varmistaa, että OpenSearch kuuntelee vain Interface:n paikallista silmukkaa, mikä riittää, koska se on samalla palvelimella kuin Graylog.
- action.auto_create_index: false**: poistamalla automaattisen indeksin luomisen käytöstä OpenSearch ei luo automaattisesti indeksiä, kun dokumentti lähetetään ilman olemassa olevaa indeksiä.
- plugins.security.disabled: true**: tämä vaihtoehto poistaa OpenSearchin tietoturva-lisäosan käytöstä, mikä tarkoittaa, että todennusta, pääsynhallintaa tai tiedonsiirron salausta ei käytetä. Tämä asetus säästää aikaa Graylogin käyttöönotossa, mutta sitä tulisi välttää tuotannossa (katso [tämä sivu](https://opensearch.org/docs/1.0/security-plugin/index/)).



Jotkin vaihtoehdot ovat jo olemassa, joten sinun tarvitsee vain poistaa "#" niiden aktivoimiseksi ja ilmoittaa sitten arvosi. Jos et löydä vaihtoehtoa, voit ilmoittaa sen suoraan tiedoston lopussa.



![Image](assets/fr/023.webp)



Tallenna ja sulje tämä tiedosto.



#### C. Määritä Java (JVM)



OpenSearchin käyttämä Java-virtuaalikone on määritettävä, jotta voit säätää, kuinka paljon muistia palvelu voi käyttää. Muokkaa seuraavaa asetustiedostoa:



```
sudo nano /etc/opensearch/jvm.options
```



Tässä käytetyllä kokoonpanolla **OpenSearch aloittaa 4 Gt:n muistilla ja voi kasvattaa sitä 4 Gt:iin**, joten muistin määrä ei vaihtele käytön aikana. Tässä kokoonpanossa otetaan huomioon, että virtuaalikoneessa on yhteensä **8 Gt RAM-muistia**. Molemmilla parametreilla on oltava sama arvo. Tämä tarkoittaa rivien:



```
-Xms1g
-Xmx1g
```



Näillä riveillä:



```
-Xms4g
-Xmx4g
```



Tässä on kuva tehtävästä muutoksesta:



![Image](assets/fr/022.webp)



Sulje tämä tiedosto tallennuksen jälkeen.



Lisäksi meidän on tarkistettava Linux-ytimen "**max_map_count**"-parametrin asetukset. Se määrittelee prosessikohtaisesti kartoitettujen muistialueiden rajan, jotta sovelluksemme tarpeet voidaan täyttää. **OpenSearch**, kuten Elasticsearch**, suosittelee tämän arvon asettamista arvoon "262144" muistinhallintavirheiden välttämiseksi.



Periaatteessa juuri asennetussa Debian 12 -koneessa arvo on jo oikea. Mutta tarkistetaanpa. Suorita tämä komento:



```
cat /proc/sys/vm/max_map_count
```



Jos saat muun arvon kuin "**262144**", suorita seuraava komento, muuten se ei ole tarpeen.



```
sudo sysctl -w vm.max_map_count=262144
```



Lopuksi ota OpenSearchin automaattinen käynnistys käyttöön ja käynnistä siihen liittyvä palvelu.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Jos näytät järjestelmän tilan, sinun pitäisi nähdä Java-prosessi, jolla on 4 Gt RAM-muistia.



```
top
```



![Image](assets/fr/029.webp)



Seuraava askel: kauan odotettu Graylogin asennus!



#### D. Graylogin asentaminen



Jos haluat **asentaa Graylog 6.1**:n uusimman version, suorita seuraavat 4 komentoa **ladataksesi ja asentaaksesi Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Kun tämä on tehty, meidän on tehtävä joitakin muutoksia Graylogin kokoonpanoon ennen kuin yritämme käynnistää sen.



Aloitetaan määrittämällä nämä kaksi vaihtoehtoa:





- password_secret**: tätä parametria käytetään määrittelemään avain, jota Graylog käyttää käyttäjien salasanojen tallentamisen suojaamiseen (suolausavaimen tapaan). Tämän avaimen on oltava **yksilöllinen** ja **sattumanvarainen**.
- root_password_sha2**: tämä parametri vastaa Graylogin oletussalasanaa. Se tallennetaan Hash SHA-256 -muodossa.



Aloitamme luomalla 96-merkkisen avaimen parametriin **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Kopioi palautettu arvo ja avaa sitten Graylogin asetustiedosto:



```
sudo nano /etc/graylog/server/server.conf
```



Liitä avain parametriin **password_secret** seuraavasti:



![Image](assets/fr/027.webp)



Tallenna ja sulje tiedosto.



Seuraavaksi sinun on määritettävä salasana oletusarvoisesti luotavalle "**admin**"-tilille. Määritystiedostoon on tallennettava salasanan Hash, mikä tarkoittaa, että se on laskettava. Alla olevassa esimerkissä annetaan salasanan "**LogsWells@**" Hash: sovita arvo omaan salasanaasi.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Kopioi saatu arvo tulosteeksi (ilman väliviivaa rivin lopussa).



Avaa Graylogin asetustiedosto uudelleen:



```
sudo nano /etc/graylog/server/server.conf
```



Liitä arvo **root_password_sha2**-vaihtoehtoon seuraavasti:



![Image](assets/fr/026.webp)



Aseta konfiguraatiotiedostossa "**http_bind_address**"-vaihtoehto. Määritä "**0.0.0.0.0:9000**", jotta Graylogin Interface-verkkoa voidaan käyttää portissa **9000** minkä tahansa palvelimen IP Address:n kautta.



![Image](assets/fr/024.webp)



Aseta sitten "**elasticsearch_hosts**"-vaihtoehdon arvoksi `http://127.0.0.1:9200` ilmoittaaksesi paikallisen OpenSearch-instanssimme. Tämä on välttämätöntä, koska emme käytä **Graylog Data Node** -solmua. Ja ilman tätä vaihtoehtoa ei ole mahdollista mennä pidemmälle...



![Image](assets/fr/025.webp)



Tallenna ja sulje tiedosto.



Tämä komento aktivoi Graylogin niin, että se käynnistyy automaattisesti seuraavalla käynnistyskerralla, ja käynnistää välittömästi Graylog-palvelimen.



```
sudo systemctl enable --now graylog-server
```



Kun tämä on tehty, yritä muodostaa yhteys Graylogiin selaimella. Syötä palvelimen IP Address (tai nimi) ja portti 9000.



**Tiedoksi:**



Vielä vähän aikaa sitten alla olevan kaltainen todennusikkuna ilmestyi, kun kirjauduit ensimmäistä kertaa Graylogiin. Sinun piti syöttää käyttäjätunnuksesi "**admin**" ja salasanasi. Ja sitten huomasit epämiellyttävän yllättäen, että yhteys ei toiminut.



![Image](assets/fr/031.webp)



Oli tarpeen palata Graylog-palvelimen komentoriville ja tarkastella lokitietoja. Silloin näimme, että **ensimmäistä yhteyttä** varten on tarpeen **käyttää väliaikaista salasanaa**, joka on määritetty lokitiedoissa.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Tämän jälkeen sinun piti yrittää uudelleen yhteyttä käyttäjällä "**admin**" ja väliaikaisella salasanalla, ja tämän jälkeen voit kirjautua sisään!



**Tämä ei enää pidä paikkaansa. Sinun tarvitsee vain kirjautua sisään admin-tililläsi ja komentorivillä määritetyllä salasanalla



![Image](assets/fr/033.webp)



**Tervetuloa Graylogin Interface:aan!



![Image](assets/fr/019.webp)



#### E. Graylog: luo uusi järjestelmänvalvojan tili



Sen sijaan, että käyttäisit Graylogin luomaa hallintatiliä, voit luoda oman henkilökohtaisen hallintatilisi. Napsauta "**Järjestelmä**"-valikkoa, sitten "**Käyttäjät ja tiimit**" ja napsauta "**Luo käyttäjä**"-painiketta. Täytä sitten lomake ja määritä tilillesi järjestelmänvalvojan rooli.



![Image](assets/fr/020.webp)



Henkilökohtainen tili voi sisältää lisätietoja, kuten etu- ja sukunimen ja sähköpostin Address, toisin kuin alkuperäinen ylläpitäjätili. Lisäksi tämä takaa paremman jäljitettävyyden, kun kukin henkilö työskentelee nimetyllä tilillä.



## Lähetä lokit Graylogiin rsyslogin avulla



### I. Esittely



Tässä toisessa osassa opimme, miten Linux-kone määritetään lähettämään lokinsa Graylog-palvelimelle. Tätä varten asennamme ja konfiguroimme Rsyslogin järjestelmään.



### II. Graylogin määrittäminen vastaanottamaan Linux-lokeja



Aloitamme konfiguroimalla Graylogin. Tässä on kolme vaihetta:





- Luodaan **Syöttö**, jonka avulla Linux-koneet voivat **lähettää Syslog-lokit UDP:n kautta**.
- Uuden **indeksin** luominen kaikkien Linux-lokien tallentamista ja **indeksointia varten**.
- Luodaan **Stream**, joka **reitittää** Graylogin vastaanottamat lokit uuteen Linux-indeksiin.



#### A. Syslogin syötteen luominen



Kirjaudu sisään Graylog Interface:een, napsauta valikosta "**System**" ja sitten "**Inputs**". Valitse avattavasta luettelosta "**Syslog UDP**" ja napsauta sitten painiketta "**Launch new input**". On myös mahdollista luoda TCP-syslog-syöttö, mutta se edellyttää TLS-varmenteen käyttöä: tämä on turvallisuuden kannalta eduksi, mutta sitä ei käsitellä tässä artikkelissa.



![Image](assets/fr/001.webp)



Ohjattu toiminto ilmestyy näytölle. Aloita antamalla tälle syötteelle nimi, esimerkiksi "**Graylog_UDP_Rsyslog_Linux**", ja valitse portti. Oletusarvoisesti portti on "**514**", mutta voit muokata sitä. Tässä on valittu portti "**12514**".



![Image](assets/fr/016.webp)



Voit myös valita vaihtoehdon "**Tallenna koko viesti**" tallentaaksesi koko lokiviestin Graylogiin. Napsauta "**Käynnistä syöttö**".



![Image](assets/fr/017.webp)



Uusi tulo on luotu ja on nyt aktiivinen. Graylog voi nyt vastaanottaa Syslog-lokeja portissa 12514/UDP, mutta sovelluksen konfigurointi on vielä kesken.



![Image](assets/fr/018.webp)


**Huomaa: yhtä Inputia voidaan käyttää useiden Linux-koneiden lokien tallentamiseen.



#### B. Luo uusi Linux-indeksi



Meidän on luotava Indeksi Graylogiin Linux-koneiden lokien tallentamista varten. Graylogin **indeksi** on tallennusrakenne, joka sisältää vastaanotetut lokit eli vastaanotetut viestit. Graylog käyttää tallennuskoneena OpenSearchia, ja viestit indeksoidaan nopeiden ja tehokkaiden hakujen mahdollistamiseksi.



Napsauta Graylogissa valikosta "**Järjestelmä**" ja sitten "**Indeksit**". Napsauta avautuvalla uudella sivulla "**Luo indeksisarja**".



![Image](assets/fr/005.webp)



Anna tälle indeksille nimi, esimerkiksi "**Linux Index**", ja lisää kuvaus ja etuliite ennen vahvistamista. Tässä **tallennamme kaikki Linux-lokit tähän indeksiin**. On myös mahdollista luoda erityisiä indeksejä vain tiettyjen lokien tallentamiseksi (vain [SSH]-lokit (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), verkkopalvelulokit jne.).



![Image](assets/fr/006.webp)



Nyt meidän on luotava uusi stream, joka ohjaa viestit tähän indeksiin.



#### C. Luo virta



Voit luoda uuden streamin napsauttamalla Graylogin päävalikossa kohtaa "**Streams**". Napsauta sitten oikealla olevaa "**Luo stream**"-painiketta. Nimeä virta avautuvassa ikkunassa esimerkiksi "**Linux Stream**" ja valitse "**Index Set**" -kenttään indeksi "**Linux Index**". Vahvista valintasi.



**Huomaa: tätä virtaa vastaavat viestit sisällytetään myös "**Default Stream**"-virtaan, ellet valitse "**Remove matches from 'Default Stream'**"-vaihtoehtoa.



![Image](assets/fr/002.webp)



Napsauta sitten höyryasetuksissa "**Add stream rule**" -painiketta lisätäksesi uuden viestien reitityssäännön. Jos et löydä tätä ikkunaa, napsauta valikossa "**Streams**" ja sitten streamiäsi vastaavalla rivillä "**More**" ja sitten "**Manage Rules**".



Valitse "**match input**"-tyyppi ja valitse aiemmin luotu **Rsyslog input in UDP**. Vahvista valinta "**Luo sääntö**"-painikkeella. Kaikki uuteen syötteeseemme tulevat viestit lähetetään nyt Linux-indeksiin.



![Image](assets/fr/003.webp)



Uuden Streamisi pitäisi näkyä luettelossa ja sen pitäisi olla tilassa "**Running**". Viestin kaistanleveys näyttää "**0 msg/s**", koska emme tällä hetkellä lähetä lokitietoja Rsyslog UDP-sisääntuloon. Voit tarkastella virran lokeja klikkaamalla sen nimeä.



![Image](assets/fr/004.webp)



**Kaikki on valmiina Graylogin puolella**. Seuraava vaihe on Linux-koneen konfigurointi.



### III. Rsyslogin asentaminen ja konfigurointi Linuxissa



Kirjaudu Linux-koneeseen joko paikallisesti tai etäyhteydellä ja käytä käyttäjätiliä, jolla on oikeudet korottaa sen oikeuksia (sudon kautta). Muussa tapauksessa käytä suoraan root-tiliä.



#### A. Rsyslog-paketin asentaminen



Aloita päivittämällä pakettien välimuisti ja asentamalla paketti nimeltä "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Tarkista sitten palvelun tila. Useimmissa tapauksissa se on jo käynnissä.



```
sudo systemctl status rsyslog
```



#### B. Rsyslogin määrittäminen



Rsyslogilla on pääasetustiedosto, joka sijaitsee täällä:



```
/etc/rsyslog.conf
```



Lisäksi hakemistoa "**/etc/rsyslog.d/**" käytetään Rsyslogin muiden asetustiedostojen tallentamiseen. Pääkonfiguraatiotiedostossa on Include-direktiivi, jolla tuodaan kaikki tässä hakemistossa sijaitsevat "**.conf**"-tiedostot. Tämä mahdollistaa Rsyslogin konfigurointiin tarkoitettujen lisätiedostojen käytön muuttamatta päätiedostoa.



Tässä hakemistossa latausjärjestys on määritettävä numeroin, koska tiedostot ladataan aakkosjärjestyksessä. Numeerisen etuliitteen lisäämisen avulla voit hallita useiden asetustiedostojen välistä prioriteettia. Tässä meillä on vain yksi ylimääräinen tiedosto, joten se ei ole ongelma.



Tässä hakemistossa luodaan tiedosto nimeltä "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Lisää tähän tiedostoon tämä rivi:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Tätä riviä tulkitaan seuraavasti:





- `*.*`: tarkoittaa kaikkien Linux-koneen Syslog-lokien lähettämistä Graylogiin.
- `@`: osoittaa, että siirto tapahtuu UDP:nä. Sinun on määritettävä "**@@@**" vaihtaaksesi TCP:hen.
- `192.168.10.220:12514`: ilmoittaa Graylog-palvelimen Address:n ja portin, johon lokit lähetetään (vastaa Input).
- `RSYSLOG_SyslogProtocol23Format`: vastaa Graylogiin lähetettävien viestien muotoa.



Kun olet valmis, tallenna tiedosto ja käynnistä Rsyslog uudelleen.



```
sudo systemctl restart rsyslog.service
```



Tämän jälkeen ensimmäisten viestien pitäisi saapua Graylog-palvelimelle!



### IV. Linux-lokien näyttäminen Graylogissa



Graylogista voit klikata "**Streams**" ja valita uuden streamin nähdäksesi siihen liittyvät viestit. Vaihtoehtoisesti voit klikata "**Haku**" ja valita Steamisi ja käynnistää haun.



Seuraavassa on joitakin Interface:n keskeisiä ominaisuuksia:



**1** - Valitse ajanjakso, jolta viestit näytetään. Oletusarvoisesti näytetään viimeisten 5 minuutin viestit.



**2** - Valitse näytettävä virta (näytettävät virrat).



**3** - Ota käyttöön viestiluettelon automaattinen päivitys (esimerkiksi 5 sekunnin välein). Muuten se on staattinen ja sinun on päivitettävä se manuaalisesti.



**4** - Napsauta suurennuslasia käynnistääksesi haun sen jälkeen, kun olet muuttanut ajanjaksoa, virtaa tai suodatinta.



**5** - Syöttöpalkki hakusuodattimien määrittämistä varten. Tässä määrittelen "**source:srv\-docker**" näyttääkseni vain sen uuden koneen lokit, johon olen juuri asentanut Rsyslogin.



Linux-kone lähettää lokit:



![Image](assets/fr/015.webp)



### V. SSH-yhteyden epäonnistumisen tunnistaminen



Graylogin vahvuus on sen kyky indeksoida lokit ja mahdollistaa hakujen tekeminen eri kriteerien mukaan: lähdekone, Timestamp, viestin sisältö jne... Voisimme etsiä epäonnistuneiden SSH-yhteyksien tunnistamista.



Yritä muodostaa yhteys etäkoneelta (esimerkiksi Graylog-palvelimelta) Linux-palvelimeen, johon olet juuri määrittänyt Rsyslogin. Esimerkiksi:



```
ssh [email protected]
```



Syötä sitten tarkoituksella väärä **käyttäjätunnus** ja **salasana**, jotta **generate yhteysvirheitä**. Tiedostossa "**/var/log/auth.log**" tämä aiheuttaa generate-lokiviestejä, jotka muistuttavat seuraavia:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Nämä viestit pitäisi löytyä Graylogista.



Käytä Graylogissa seuraavaa hakusuodatinta näyttääksesi vain vastaavat viestit:



```
message:Failed password AND application_name:sshd
```



Jos sinulla on useita palvelimia ja haluat analysoida tietyn palvelimen lokit, määritä sen nimi lisäksi:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Tässä on yleiskatsaus tuloksista koneella, jolla tuotin useita yhteysvirheitä eri vuorokaudenaikoina:



![Image](assets/fr/009.webp)



Epäonnistuneita yhteysyrityksiä tehdään koneelta, jonka IP Address on "**192.168.10.199**". Jos haluat lisätietoja tämän isännän toiminnasta, voit **haku tämän IP Address**. Graylog tulostaa kaikki lokit, joissa viitataan tähän IP Address:een, kaikilla isännillä (joille lokien lähettäminen on määritetty).



Tässä tapauksessa käytettävä suodatin voi olla:



```
message:"192.168.10.199"
```



Saamme lisää tuloksia (ei yllättävää, koska emme suodata SSH-sovellusta):



![Image](assets/fr/008.webp)



### VI. Päätelmät



Tämän ohjeen avulla sinun pitäisi pystyä määrittämään Linux-kone lähettämään lokinsa Graylog-palvelimelle. Näin voit keskittää Linux-asemien lokit lokinieluun!



Jos haluat mennä vielä pidemmälle, harkitse kojelautojen ja hälytysten luomista, jotta saat ilmoituksen, kun poikkeama havaitaan.



![Image](assets/fr/007.webp)