---
name: LNbits
description: Kauppias kirjanpitoalusta
---
![presentation](assets/lnbits-intro.webp)

# Kirjanpitojärjestelmä

LNbits on täynnä työkaluja, joilla voit hallita ja kanavoida saapuvia ja lähteviä varoja, liittää verkkokauppasi tai jopa laitteita, kuten itse rakentamasi laitteistolompakon tai pankkiautomaatin. Käyttäjätyyppejä ovat mm:


- Lompakon omistajat, jotka haluavat käyttää LNbitsin käyttöliittymänä varojensa hallinnointiin sekä sen lisäominaisuuksiin.
- Online- ja offline-kauppiaat tai palveluntarjoajat, jotka haluavat hyväksyä Bitcoin onchain- ja Lightning Network -maksut.
- Kehittäjät, jotka haluavat rakentaa Lightning Network -sovelluksia.
- Solmujen ylläpitäjät, jotka haluavat integroida solmunsa LNbits-järjestelmään kirjanpitoa varten.
- Kaikilla näillä on erilaiset tarpeet. Rakennamme LNbitsin modulaarisesti, jotta jokainen käyttäjä voi käyttää ominaisuuksiamme itselleen parhaiten sopivalla tavalla.

# Lompakon hallinnoija

LNbits on ilmainen ja avoimen lähdekoodin kirjanpitojärjestelmä - ei node manager. Kanavanhallinta kuuluu Lightning-solmulle, joka on liitetty LNbitsiin rahoituslähteenä kuten LND tai c-lightning. LNbits-järjestelmän superuser- tai admin-käyttäjät ovat vastuussa kirjanpito-ominaisuuksien ja sisäisten laajennusten yleisen käytettävyyden ja konfiguroinnin hallinnasta.

LNbits toimii käyttäjän ja Lightning-solmun välisenä rajapintana, joka tarjoaa yksinkertaisen ja käyttäjäystävällisen tavan hallita maksuvälineverkkoa ja olla vuorovaikutuksessa sen kanssa.

Ajattele LNbitsiä kuin "wordpressin modulaarista kehystä" solmullesi. Helppohoitoinen alusta, joka perustuu laajennuksiin, joita voit yhdistellä lukuisiin käyttötapauksiin.

Ajattele, että LNbits on kuin oma pankkisi taloushallinnon ohjelmisto. Solmusi tarjoaa kanavia, joiden kautta voit maksaa, ja LNbits laajentaa solmusi niin, että voit käyttää useampaa kuin yhtä salamalompakkoa, joka solmusi mukana tulee. Näiden lompakoiden ei välttämättä tarvitse kuulua sinulle itsellesi. Sanotaan, että sinulla LN-solmun ylläpitäjänä on jo tarpeeksi kanavien likviditeettiä ja varoja ja nyt haluat tarjota joitakin bitcoin-pankkipalveluja ystävillesi, perheellesi, omalle kaupallesi tai muille tavallisille kauppiaille.

Tarjoat heille yksinkertaisen tavan avata "pankkitili" solmussasi ilman, että heillä on pääsy muihin solmusi lompakoihin ja kaikkeen solmusi likviditeettiin, mutta vain heidän osaansa. Solmusi (pankki) toimii vain kuljetuspalveluntarjoajana heidän maksuilleen (sisään/ulos).

HUOMAUTUS: kaikki varat, jotka "asiakkaasi" tallettavat LNbits-pankkitileilleen solmussasi, menevät suoraan solmusi LN-kanaviin. Tämä tarkoittaa, että SINÄ olet itse asiassa näiden varojen todellinen omistaja. Sinulla on suuri vastuu heidän varoistaan. Älä ole paha ja karkaa varojen kanssa, älä ole paha ja peri korkeita maksuja. Haluamme vittuilla fiat-pankkiireille, emme vittuilla toisillemme (bitcoinin käyttäjille).

# Demo alusta

Demo löytyy osoitteesta [https://legend.lnbits.com](https://legend.lnbits.com). Se on täysin toimiva, ja sen avulla voi tutustua Lightning-verkkoon sekä LNbitsin ja LNURL:n ominaisuuksiin yleensä. Vaikka emme voi estää sinua käyttämästä sitä, pyydämme kuitenkin, ettet käytä sitä tuotantokäytössäsi. Emme ainoastaan työskentele palvelimilla usein testataksemme uusia ominaisuuksia, vaan haluaisimme myös rohkaista sinua käyttämään omaa solmua ja LNbitsiä suvereenisti. Jos oman solmun pyörittäminen on mielestäsi tällä hetkellä liikaa pyydetty, voit liittää LNbitsin pilvipalveluun, kuten Opennode, Luna tai Votage, tai Telegramin Lightning Tipbotiin vain muutamia mainitakseni.

# LNbits-esite

Haluatko luovuttaa perustietoja kauppiaalle tai rakennusalan ystävällesi ? Olemme erittäin iloisia voidessamme julkistaa ensimmäisen esitteemme kaikkien käyttöön. Koko on maailmanlaajuisesti tyypillinen flyerformaatti, jossa on 6 sivua (2 taittoa) ja jonka leveys on 3508 ja korkeus 2480px.

LNbits kauppiaille: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbitit rakentajille: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Joitakin perusasioita

LNbits perustuu LNURL-protokollaan, mikä tarkoittaa, että pyynnöt ovat voimassa kahdessa muodossa: joko https:// clearnet-linkkinä (itse allekirjoitettuja varmenteita ei sallita) tai http:// v2/v3 onion-linkkinä. Jotta voit tarjota LNbits-palveluja, kuten LNURLp/w QR-koodeja tai NFC-kortteja, joita voidaan käyttää luonnossa, sinun on avattava LNbits clearnetiin (https).

Ennen kuin asennat LNbitsin, varmista, että olet lukenut ja ymmärtänyt seuraavat yleiset oppaat siitä, mikä LNbits on ja mitä mahdollisuuksia se avaa sinulle.


- [LND-opas](https://docs.lightning.engineering/) | LND:n asentaminen
- [LND Config Example](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | LND-asetukset
- [CLN-opas](https://docs.corelightning.org/docs/installation) | CLN:n asentaminen
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Suorita vartiotorni](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Erittäin tärkeää!

Yksityiskohtaisempia oppaita LNbitsin käytöstä tietyissä käyttötapauksissa löydät täältä:


- [Getting Started with LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack-opas
- [ToDos turvallisuutesi varmistamiseksi LNbitsin kanssa](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Yksityiset pankit Lightning Networkissa](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Substack-opas
- [Suorita huoltajan lompakot ystävillesi ja perheellesi](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack-opas
- [LNbits pienelle ravintolalle / hotellille](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack-opas
- [LNbits Streamer copilotin käyttö](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack-opas
- [Aloita NOSTR-markkinat LNbitsillä](https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack-opas
- [LNbitsin käyttö koulujen projekteissa tai festivaalitapahtumissa](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Substack-opas

# Asenna LNbits

## Perusasennusopas

LNbits voidaan asentaa mihin tahansa Linux-käyttöjärjestelmäkoneeseen. Se ei vaadi tehokasta konetta tai palvelinta, vain riittävästi RAM-muistia ja hieman levytilaa tietokannalle. Sitä voidaan käyttää erillään BTC/LN-solmusta (paikallinen tietokone tai etä-VPS) tai yhdessä samassa koneessa solmun kanssa tai jo asennettuna niputettuun solmuohjelmistoon.

Voit valita yleisimpien paketinhallintaohjelmien, kuten poetryn ja nixin, välillä. Oletusarvoisesti LNbits käyttää SQLiteä tietokantana. Voit käyttää myös PostgreSQL:ää, jota suositellaan sovelluksiin, joissa on suuri kuormitus. [Tässä on opas perusasennukseen poetryn tai nixin avulla](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Kaikille, joille tämä on uutta, löydät yksityiskohtaisempia vaiheittaisia oppaita, joilla saat LNbitit toimimaan tietyissä ympäristöissä:


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) jonka Axel
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) jonka Leo

Löydät myös videon [dockerised Setup on a VPS with PostgreSQ, LightningTipBot as a funding source using nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Lisää asennusskenaarioita täällä](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Nippuohjelmistosolmujen osalta katso niiden LNbits-ohjelmistoja koskeva dokumentaatio: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

Kun et ole kiinnostunut teknisistä asioista etkä halua itse isännöidä rahoituslähdettäsi tai lnbittejäsi, voit käyttää [LNbits SaaS-versiota](https://saas.lnbits.com) (Software-as-a-service). Se on periaatteessa kuin LNbits pilvipalveluna, mutta voit itse määritellä rahoituslähteen (esim. solmusi, LNbits-lompakon, LNtipbotin, fakewalletin jne.) ja ympäristömuuttujat - mitä ei useimmiten tehdä muissa pilvipalveluratkaisuissa.

[Tässä on yksityiskohtainen opas siitä, miten LNbits SaaS:ää käytetään tiettyihin käyttötapauksiin](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Rahoituslähteet

LNbits ei ole solmunhallintaohjelmisto vaan LN-keskeinen kirjanpitojärjestelmä LND- tai CLN-rahoituslähteen päällä. Ensimmäisen asennuksen jälkeen voit vierailla LNbitsissäsi osoitteessa http://localhost:5000/.

Voit muuttaa rahoituslähdettä menemällä super-user-URL:iin ja valitsemalla rahoituslähteen "Manage Server" -kohdasta tai muokkaamalla .env-tiedostoa muuttamalla `LNBITS_BACKEND_WALLET_CLASS` haluamaasi lähteeseen, jos asetat `.env`-tiedostossa `adminUI=TRUE`.

Löydät .env-tiedoston lnbits/- tai lnbits/apps/data-kansiosta laajentamalla komentoa listaamaan hakemistosi tiedostot komennolla `ls -a`.

Saatat myös joutua asentamaan lisäpaketteja tai suorittamaan muita asennusvaiheita ja valitsemaan haluamasi rahoituslähteen. Uudelleenkäynnistyksen jälkeen uudet asetukset ovat aktiivisia.

Mitä rahoituslähteitä voin käyttää LNbitsille?

LNbits voi toimia monien salamaverkon rahoituslähteiden päällä. Tällä hetkellä on tuki CoreLightningille, LND:lle, LNbitsille, LNPaylle ja OpenNodelle, ja uusia lisätään säännöllisesti.

On tärkeää valita lähde, jolla on hyvä likviditeetti ja hyvät vertaisverkostot. Jos käytät LNbittejä julkisiin palveluihin, käyttäjiesi maksut voivat vain silloin virrata iloisesti molempiin suuntiin.

Backend-lompakko (rahoituslähde) voidaan konfiguroida käyttämällä seuraavia LNbits-ympäristömuuttujia `.env`-tiedostossa tai pääkäyttäjätililläsi Manage-Server-osiossa.

Jos haluat käyttää .env-versiota, löydät parametrit täältä:

### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-rpc
- Kipinä (c-salama)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon tai Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: portti
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon tai Bech64/Hex

Voit myös käyttää sen sijaan AES-salattua makaronia (lisätietoja) käyttämällä komentoa


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Voit salata makaronisi suorittamalla `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.

### LNbits (toinen LNbits-instanssi)


- Pilvipalvelimella tai omalla kotipalvelimellasi sijaitseva LNbits-instanssi
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! ÄLÄ käytä tätä tuotantoon / kaupallisiin tarkoituksiin, vain testaukseen !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Salama TipBot

Jos haluat muodostaa yhteyden [Lightning Tipbot](https://t.me/LightningTipBot) Telegramista, sinun on asetettava seuraava parametri:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: Avaimen saadaksesi sinun on suoritettava /api yksityisessä keskustelussa LightningTipbotin kanssa Telegramissa kerran.

Katso myös tämä opetusohjelma [LNbitsin ja LightningTipBotin asentaminen vps:n kautta](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### IBEX HUB

Rekisteröidy [täällä](https://ibexpay.ibexmercado.com/onboard) ja hae avaimet/tunnukset sieltä, päätepiste on https://ibexpay-api.ibexmercado.com.

Lisätietoja on [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

Jotta laskun kuuntelu toimisi, sinulla on julkisesti saatavilla oleva URL-osoite LNbitsissäsi ja sinun on luotava [LNPay webhook](https://dashboard.lnpay.co/webhook/), joka osoittaa osoitteeseen `<LNbits-isäntäsi>/wallet/webhook` ja jossa on tapahtuma "Wallet Receive" eikä salaisuutta ole annettu. Asetuksesta `https://mylnbits/wallet/webhook` tulee päätepisteen url, joka saa ilmoituksen kaikista maksuista.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

### OpenNode

Jotta lasku toimisi, sinulla on oltava julkisesti saatavilla oleva URL-osoite LNbitsissäsi. Webhook-asetus on valinnainen.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

### Alby

Alby on selainlaajennus, jossa on LN-lompakkotoiminnot ja LNDHUB-tili, jota voidaan käyttää LNbitsin rahoituslähteenä. [Lisätietoja täällä](https://getalby.com/).

Jotta lasku toimisi, sinulla on oltava julkisesti saatavilla oleva URL-osoite LNbitsissäsi. Manuaalista webhook-asetusta ei tarvita. Voit luoda Alby-käyttötunnuksen täällä: https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

## Lisä- / Vianmääritysoppaat

Tässä on lisäohjeita, jos tarvitset niitä. Laajenna kuvaus klikkaamalla nuolta.

### The Killswitch 🚨

Viime aikoina on ollut niin paljon vaarallisia bugeja paitsi koko alalla myös LNbitsissä, että päätimme tehdä asialle jotain. Voit nyt halutessasi saada varoituksia ja/tai ryhtyä suoriin toimiin, kun haavoittuvuus tai vika, joka voi johtaa varojen menettämiseen, ilmenee uudelleen.

![killswitchn](assets/lnbits-killswitch.webp)

Jos siirryt void-lompakkoon, kaikki instanssin käyttäjätyypit näkevät keltaisen bannerin, jossa normaalisti lukee "LNbits is in Beta" -ilmoitus teeman/kielialueen vieressä oikealla - ja se on ilmeisin vihje siitä, että jotain on tapahtunut. Vilkaise uutta palvelin-välilehteä, joka on korostettu vihreällä ikkunan vasemmassa osassa.

Miten se toimii? Kun killswitch on käytössä, salainen github-arkisto, joka on vain LNbitsin ydintiimin käytettävissä, tarkistetaan X minuutin välein (joka voidaan määrittää). Jos tässä arkistossa julkaistaan haavoittuva vika, se toimii signaalina, joka käynnistää killswitchin kaikissa tilatuissa asennuksissa ja siirtää lnbits-instanssisi käyttämään void-lompakkoa. Jos pilvet ovat hälvenneet ja olet asentanut tietoturvapäivityksen, voit asettaa rahoituslähteeksi solmun, lompakon tai minkä tahansa käyttämäsi uudelleen myös Manage Server -osion kautta. Tässä wikissä on osio rahoituslähteiden vaihtamisesta, jos et tiedä, mitä konfiguroida.

### Ylläpitäjän ja pääkäyttäjän välinen ero

LNbits Admin UI:n avulla voit muuttaa LNbitsin asetuksia LNbitsin etusivun kautta. Se on oletusarvoisesti pois käytöstä, ja kun asetat ensimmäisen kerran `.env`-tiedostossa ympäristön muuttujan `LNBITS_ADMIN_UI=true`, asetukset alustetaan ja niitä käytetään. Siitä eteenpäin käytetään tietokannasta saatavia asetuksia .env-tiedoston asetusten sijasta.

### Super User

Admin-käyttöliittymän avulla otimme käyttöön superkäyttäjän, jolla on pääsy palvelimelle, joten hän voi muuttaa asetuksia, jotka voivat kaataa palvelimen tai tehdä siitä reagoimattoman frontendin ja apin kautta, kuten esimerkiksi muuttaa rahoituslähdettä. Superkäyttäjä on tallennettu vain tietokannan asetustaulukkoon. Kun asetukset on "palautettu oletusasetuksiin" ja käynnistetty uudelleen, uusi pääkäyttäjä luodaan. Lisäsimme myös API-reitteihin sisustajan, joka tarkistaa, onko superkäyttäjä olemassa. Sen ID:tä ei koskaan lähetetä apin ja frontendin kautta, ja se saa vain boolin (kyllä/ei), jos olet superkäyttäjä vai et.

Vain pääkäyttäjä saa brrrr satoshit eri lompakoihin "Top Up" -osion kautta.

Voit myös lähettää superkäyttäjän webhookin kautta toiseen palveluun, kun se on luotu. Lisää tietoa täältä https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

Etupäässä on myös mahdollisuus vaihtaa "luo lompakko" -sivulla näkyvä myymälän kuva avaamalla Hallitse palvelinta -osio ja valitsemalla Teema -> Mukautettu logo.

### Ylläpitäjän käyttäjät

Ympäristömuuttuja: `LNBITS_ADMIN_USERS`, pilkulla erotettu luettelo käyttäjätunnuksista. Admin-käyttäjät voivat muuttaa asetuksia admin-käyttöliittymässä - lukuun ottamatta rahoituslähteen asetuksia, koska tämä vaatisi palvelimen uudelleenkäynnistyksen ja voisi mahdollisesti tehdä palvelimesta saavuttamattoman. Heillä on myös pääsy kaikkiin laajennuksiin, jotka on osoitettu heille kohdassa `LNBITS_ADMIN_EXTENSIONS`.

### Sallitut käyttäjät

Ympäristömuuttuja: `LNBITS_ALLOWED_USERS`, pilkulla erotettu luettelo käyttäjätunnuksista. Määrittelemällä nämä käyttäjät LNbits ei ole enää yleisön käytettävissä. Vain määritellyt käyttäjät ja ylläpitäjät voivat käyttää LNbitsin etusivua.

#### Päivitä LNbits

LNbitsin paikallisen instanssin tavallinen päivitys tapahtuu yksinkertaisesti kopioimalla ja liittämällä seuraavat CLI-komennot:

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

Jos käytät Raspiblitziä tai MyNodea, saatat lisäksi tarvita myös tiedoston

```
sudo systemctl restart lnbits
```

lopussa, koska LNbits toimii palveluna.

Umbrelissa/Citadelissa komennot olisivat seuraavat

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### SQLite to PostgreSQL siirtyminen

Jos sinulla on jo LNbits asennettuna ja käynnissä SQLite-tietokantaan, suosittelemme siirtymistä postgres-tietokantaan, jos aiot käyttää LNbits-tietokantaa mittakaavassa.

Mukana on skripti, joka voi tehdä siirtymisen helposti. Postgres on oltava jo asennettuna, ja käyttäjälle pitäisi olla salasana (katso Postgresin asennusohjeet edellä). Lisäksi LNbits-instanssisi on ajettava kerran Postgresilla tietokantakaavion toteuttamiseksi, ennen kuin siirto voi toimia:

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Toivottavasti nyt kaikki toimii ja siirtyy... Käynnistä LNbits uudelleen ja tarkista, toimiiko kaikki oikein.

#### Tietokannan varmuuskopiointi ja palauttaminen

Tutustu [tähän erittäin yksityiskohtaiseen oppaaseen varmuuskopiointi- ja palautusprosessista](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### LNbits-lompakon rahoittaminen solmusta ei toimi

Jos haluat lähettää satelliitteja samasta solmusta, joka on LNbittien rahoituslähde, sinun on muokattava lnd.conf-tiedostoa.

Sisällytettävät parametrit ovat: `allow-circular-route=1`: `allow-circular-route=1`

Tee se lnd.conf-tiedoston kohdassa Application options. Muuten LND:n käynnistys voi epäonnistua joissakin nippusolmuissa.

HUOMAUTUS: On suositeltavaa käyttää uutta adminUI-laajennusta, jossa on "TopUp"-vaihtoehto varojen lisäämiseksi LNbits-tilille.

#### Virhe 426

Sain virheen: "lnurl on toimitettava julkisesti saatavilla olevan https-verkkotunnuksen tai torin kautta. 426 upgrade required"</summary>

Tämä virhe johtuu yleensä siitä, että ngnix-tunnelin takana oleva LNbits ei välitä LNURL-osoitetta oikein. Pysäytä LNbits ja muokkaa .env-tiedostoa lisäämällä siihen tämä rivi:

`FORWARDED_ALLOW_IPS=*`

Jos käytät ngnix-asennusta, varmista, että nämä otsikot ovat ngnixin konfiguraatiossa:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Verkkovirhe

Sain "https-virhe", verkkovirhe" tai muita, kun skannasin QR</summary>

Huonoja uutisia, tämä on reititysvirhe, jolla voi olla useita syitä. Tarkista ensin QR:n LNURL [Lightning Decoder](https://lightningdecoder.com/) avulla, jos löydät sieltä jotain outoa. Kokeillaan muutamia mahdollisia ongelmia ja niiden ratkaisuja.

LNbits toimii vain Torin kautta, et voi avata sitä julkisella verkkotunnuksella, kuten lnbits.yourdomain.com


- Koska haluat, että asetuksesi pysyvät tällaisina, avaa LNbits-lompakkosi .onion URI:n avulla ja luo se uudelleen. Tällä tavoin QR luodaan siten, että siihen pääsee käsiksi tämän .onion URI:n kautta eli vain torin kautta. Älä luo tätä QR:ää .local URI:llä, koska se ei ole tavoitettavissa internetin kautta - ainoastaan kotilähiverkostostasi.
- Avaa LN-lompakkosovellus, jota käytit QR-koodin skannaamiseen, ja tällä kertaa torin avulla (katso lompakkosovelluksen asetukset). Jos sovellus ei tarjoa toria, voit käyttää sen sijaan Orbotia (Android). Katso asennusosiosta yksityiskohtaiset ohjeet siitä, miten voit avata LNbittisi clearnet/https:lle.

#### Estä muita luomasta lompakoita minun LNbitsillä

Kun käytät LNbittejä clearnetissä, periaatteessa jokainen voi luoda lompakon siihen. Koska solmusi varat on sidottu näihin lompakoihin, haluat ehkä estää sen. Siihen on kaksi tapaa:

Määritä sallitut käyttäjät ja laajennukset `.env`-tiedostossa ([katso env-esimerkki täältä](https://github.com/lnbits/lnbits/blob/main/.env.example)). Tämä toimii vain, jos käytät asetusta `adminUI=FALSE` .env-tiedostossa, muutoin sinun on tehtävä se Manage Server -osiossa -> Users -> Allowed Users. Kaikkia muita ei sen jälkeen sallita.

#### Mukauta laskun voimassaoloaikaa

Nyt voit luoda laskuja, joiden voimassaoloaika on mukautettu. Yhteensopiva backendien kanssa: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet toistaiseksi!

Voit asettaa `LIGHTNING_INVOICE_EXPIRY`-arvon .env-tiedostossasi tai muuttaa kaikkien laskujen oletusarvon AdminUI:n avulla. /api/v1/payments-päätepisteessä on myös uusi kenttä, jossa voit asettaa vanhentumisen JSON-tietoihin.

## Wallet-URL poistettu

### Lompakko demopalvelimella legend.lnbits

Tallenna aina kopio lompakko-URL:stä, Export2phone-QR:stä tai LNDhubista omia lompakoitasi varten turvalliseen paikkaan. LNbits EI VOI auttaa sinua palauttamaan niitä, jos ne ovat kadonneet.

### Lompakko omasta rahoituslähteestäsi/solmusta

Tallenna aina kopio lompakko-URL:stä, Export2phone-QR:stä tai LNDhubista omia lompakoitasi varten turvalliseen paikkaan. Löydät kaikki LNbits-käyttäjät ja lompakko-ID:t LNbits-käyttäjähallinta-laajennuksestasi tai sqlite-tietokannastasi. Voit muokata tai lukea LNbits-tietokantaa menemällä LNbits /data-kansioon ja etsimällä tiedoston nimeltä sqlite.db. Voit avata ja muokata sitä Excelillä tai erityisellä SQL-editorilla, kuten [SQLite browser](https://sqlitebrowser.org/).

Voit myös tyhjentää lompakot cli:n kautta ja tarkastella jokaista lompakkoa tietokannassasi.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

Tulos näyttää jotakuinkin tältä

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

ja haluat laittaa nämä arvot url-osoitteeseen seuraavasti

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Korvaa f8a43fc363ea428db5c53b3559935f1f arvolla, joka tulee ennen nimeä (esimerkissämme f8a43fc363ea428db5c53b3559935f1f) ja 1280ff5910a9c485a782a2376f338b6c on käyttäjäsi, ja sen pitäisi tulla nimen perässä näkyvä arvo. Voit lopettaa sqlite3:n kirjoittamalla

```
.quit
```

#### LNURL salamaosoitteelle päinvastoin

Kokeile tätä [kooderia](https://lnurl-codec.netlify.app/) fiatjafilta tai [tätä](https://lightningdecoder.com/). LNURLp:n maksamiseen tai tarkistamiseen voit käyttää myös [LNurlpay](https://wwww.lnurlpay.com/). Siinä pitäisi olla HTTPS EI HTTP.

#### Määritä kommentti, jonka ihmiset näkevät maksaessaan LNURLp QR:lle

Kun luot LNURL-p:n, kommenttikenttää ei oletusarvoisesti täytetä. Tämä tarkoittaa, että maksuihin ei saa liittää kommentteja.

Jos haluat sallia kommentit, lisää laatikon merkkien pituus, joka voi olla 1-250 merkkiä. Kun laitat sinne numeron, kommenttiruutu näkyy maksuprosessissa. Voit myös muokata jo luotua LNURL-p:tä ja lisätä kyseisen numeron.

![lnbits comments](assets/lnbits-comments.webp)

#### Talletus onchain BTC LNbitsille

On olemassa kaksi tapaa vaihtaa satsit ketjussa olevasta BTC:stä LN BTC:hen (tai LNbitsiksi).

##### Ulkoisen vaihtopalvelun kautta.

Muut käyttäjät, joilla ei ole pääsyä LNb:hen, voivat käyttää vaihtopalvelua, kuten [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) tai [ZigZag](https://zigzag.io/). Tämä on hyödyllistä, jos tarjoat vain LNURL/LN-laskuja LNbits-instanssistasi, mutta maksajalla on vain onchain-satseja, joten hänen on ensin vaihdettava ne omalle puolelleen. Menettely on yksinkertainen: käyttäjä lähettää onchain-btc:tä swap-palveluun ja antaa LNbitsin LNURL/LN-laskun swapin kohteeksi.

##### Onchainin ja Boltzin LNbits-laajennuksen käyttäminen.

Muista, että tämä on erillinen lompakko, ei LN btc, jota LNbits edustaa "lompakkona" LN-rahoituslähteesi yhteydessä. Tätä onchain-lompakkoa voidaan käyttää myös LN btc:n vaihtamiseen (esim. hardwarewalletiin) käyttämällä LNbitsin Boltz- tai Deezy-laajennusta. Jos sinulla on verkkokauppa, joka on linkitetty LNbitsisi LN-maksuja varten, on erittäin kätevää tyhjentää säännöllisesti kaikki LN:n satsit onchainiin. Näin LN-kanavissasi on enemmän tilaa, jotta voit vastaanottaa uusia, tuoreita sateja.

Menettely niille, joilla ei ole bitcoin-laitelompakkoa:


- Käytä Electrum- tai Sparrow-lompakkoa uuden onchain-lompakon luomiseen ja tallenna varmuuskopio siemenestä turvalliseen paikkaan.
- Mene lompakon tietoihin ja kopioi xpub.
- Siirry osoitteeseen LNbits - Onchain-laajennus ja luo uusi watch-only-lompakko kyseisellä xpubilla.
- Siirry osoitteeseen LNbits - Tipjar-laajennus ja luo uusi Tipjar. Valitse LN-lompakon lisäksi myös onchain-vaihtoehto.
- Valinnainen - Mene LNbits - SatsPay-laajennukseen ja luo uusi maksu onchain-btc:lle. Voit valita onchainin ja LN:n tai molemmat. Se luo sitten laskun, jonka voi jakaa.
- Valinnainen - Jos käytät LNbitsin linkitettynä Wordpress + Woocommerce -sivuun, kun luot/linkkaat kellon lompakon LN btc shop -lompakkoon, asiakkaalla on molemmat maksutavat samalla näytöllä.

Kun vastaanotat maksun LNbitsissä, tapahtumaloki näyttää vain tapahtuman jatketun tyypin.

![lnbits payment details](assets/lnbits-payment-details.webp)

Tapahtumien yleiskatsauksessa näet pienen vihreän nuolen, joka osoittaa vastaanotetut varat, ja punaisen nuolen, joka osoittaa lähetetyt varat.

Jos napsautat nuolinäppäimiä, ponnahdusikkunassa näkyvät liitetyt viestit sekä lähettäjän nimi, jos se on annettu.

Määrittää nimi näkymään maksuissa, LNbitsissä tätä ei tällä hetkellä ole mahdollista tehdä - mutta vastaanottaa. Tämä on mahdollista vain, jos lähettäjän LN-lompakko tukee [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) kuten [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

Tämän jälkeen näet peitenimen/salanimen LNbits-tapahtumien tiedot-osiossa (napsauta nuolia). Huomaa, että voit antaa sinne minkä tahansa nimen, eikä se välttämättä liity todelliseen lähettäjän nimeen, jos saat sellaisen.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Tuodaksesi LNbits-tilisi lompakkosovellukseen avaa LNbitsisi haluamallasi tilillä / lompakolla, siirry kohtaan "manage extensions" ja aktivoi LNDHUB-laajennus. Avaa LNDHUB-laajennus, valitse lompakko, jota haluat käyttää, ja skannaa joko "admin"- tai "invoice only"-QR sen mukaan, minkä turvallisuustason haluat kyseiselle lompakolle.

Voit käyttää [Zeus](https://zeusln.app/) tai [Bluewallet](https://bluewallet.io/) lompakkosovelluksina lndhub-tiliä varten, jolloin BW tukee useampaa kuin yhtä lompakkoa.

Kun teet tämän, suosittelemme asettamaan myös LN-verkon URI:n oman solmusi URI:ksi. Jos LNbits-instanssisi on vain Tor, sinun on myös käytettävä näitä sovelluksia, joissa Tor on aktivoitu. Tässäkin tapauksessa sinun on avattava LNbits-sivu Tor.onion-osoitteesi kautta.

Jos sinulla on virhe "unsupported hash type" kun käytät ypubia On-chain-laajennuksessa, tarkista, käyttääkö LNbits-instanssisi python 3.10:tä, [tämä ongelma](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python) voi vaikuttaa siihen. Muokkaa openssl.cnf-tiedostoa stackoverflow-vastauksessa kuvatulla tavalla ja käynnistä LNbits uudelleen.

## Työkalujen valmistus ja rakentaminen LNbitsin avulla

LNbitsillä on kaikenlaisia [avoimia sovellusrajapintoja](https://legend.lnbits.com/docs) ja työkaluja, joilla voi ohjelmoida ja liittää monia eri laitteita lukemattomiin eri käyttötarkoituksiin.

Kun olet uusi rakentamaan, aloita tästä [MakerBits-esittelyt](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) Ben Arcilta, joka kertoo LNbitteihin perustuvien vempaimien rakentamisesta.

### TÄRKEÄÄ:


- LNbits perustuu LNURL-protokollaan, jonka pyynnöt ovat voimassa kahdessa muodossa: joko https:// clearnet-linkkinä (itse allekirjoitettuja varmenteita ei sallita) tai http:// v2/v3 onion-linkkinä. Jotta voit tarjota LNbits-palveluja, kuten LNURLp/w QR-koodeja tai NFC-kortteja, joita voidaan käyttää luonnossa, sinun on avattava LNbits clearnetiin (https).
- Käytä esp32:n virtalähteenä vain DATA-kaapeleita. Kaikki kaapelit eivät tue dataa esp:n virransyötön lisäksi. Et olisi ensimmäinen, jos esp:n mukana tullut kaapeli on pelkkää virtaa käyttävä kaapeli
- Varmista, että USB-keskusta ei käytetä, jos siihen on liitetty muita laitteita. Tämä voi johtaa outoihin vaikutuksiin, joita on vaikea korjata (esim. ei käynnisty tai pysähtyy).
- Toteuttaaksesi esp-projekteja MacOS:n kanssa tarvitset UART-siltaohjaimen. Jos sinulla on ongelmia ajurin kanssa Mac- tai Linux-järjestelmissä, löydät ne täältä tai, jos kyseessä on TTGO-näyttö, tästä. Jos olet windowsissa ja sinulla on ongelmia yhteyden muodostamisessa, varmista, että lataat VANHEMMAN version 11.1.0, koska uudempi ei toimi! Löydät myös sarjapäätteen täältä, jolla voit tarkistaa yhteyden - aseta baudinopeudeksi 115200.
- Vaikka Platform.ion käyttö on paljon mukavampaa (esim. riippuvuudet asennetaan automaattisesti), suosittelemme Arduinon käyttöä kaikille, jotka ovat vasta-alkajia.
- TT-Go näyttö S3: Näytönsuojakalvon kielekkeen väri kertoo, mitä ohjainta (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) on käytetty sen rakentamiseen. Säilytä se, jotta voit debugata, jos ohjelmoit itsesi ja näyttö ei näytä grafiikkaa oikein, esim. värit väärin, peilikuvat tai hajapikselit reunoilla. Jos sinun on joskus tehtävä tämä, on olemassa eeppinen opas eri näyttöjä varten säätämisestä
- Käytä aina pieniä kirjaimia lnurl239xx eikä LNURLl239xx
- Lisäämällä lightning:lnurl1234xyz luodaan QR, joka pyytää avaamaan käyttäjän lompakon tätä laskua varten skannattaessa (viimeksi asennettu salamasovellus iOS: ssä, asetus Androidissa)
- Jos vilkkaat esp32:ta webin kautta, se toimii vain näillä selaimilla (TL:DR Chrome, Edge & Opera).
- Huomioi tämä PIN-OUT-viite esp:lle
- Kun käytät FOSS-ohjelmistoja tai FOS-oppaita, linkitä aina tekijä. Kaikki rakastavat katsella lapsensa kasvua ja se myös käynnistää rakennusketjun, joka on aika mahtavaa katseltavaa :)

Tule [Makerbits Telegram-ryhmään](https://t.me/makerbits), jos tarvitset apua projektin kanssa - me autamme sinua!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Tässä on joitakin projektiluokkia, joita voit rakentaa LNbitsin avulla:


- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Automaatti](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora ja verkkoverkko](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [AUTTAJAT JA RESURSSIT](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Lisää esimerkkejä "Powered by LNbits" -projekteista täällä](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [LNbitsin käyttötapaukset](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)