---
name: BTCPay Serverin päivittäminen
description: Asenna tietoturvapäivitys BTCPay Server -instanssiisi ja uusi ne tunnistetiedot, joilla on merkitystä
---

![cover](assets/cover.webp)

Kun ylläpidät omaa maksuprosessoriasi, olet samalla myös oma tietoturvatiimisi. Kun BTCPay Serverin ylläpitäjät julkaisevat tietoturvajulkaisun, kukaan ei korjaa instanssiasi puolestasi: päivitys, sen varmistaminen ja sitä seuraava tunnistetietojen uusiminen ovat sinun tehtäviäsi.

Tämä ohje käy läpi koko menettelyn riippumatta siitä, miten otit BTCPay Serverin käyttöön: käynnissä olevan version tarkistaminen, päivityksen asentaminen omalle käyttöönottotavallesi, sen varmistaminen että päivitys todella meni läpi, sekä niiden salaisuuksien uusiminen, jotka hyökkääjä on voinut kaapata instanssisi ollessa haavoittuvainen.

Jos et ole vielä ottanut BTCPay Serveriä käyttöön, aloita asennusohjeesta:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Elokuun 2026 kriittinen haavoittuvuus

⚠️ **Kriittinen tietoturvavaroitus (7. elokuuta 2026):** BTCPay Serveriä koskevaa kriittistä haavoittuvuutta hyödynnetään parhaillaan aktiivisesti, ja se voi johtaa varojen menetykseen. Päivitä instanssisi välittömästi **versioon 2.4.2** polun `Admin Dashboard > Server > Maintenance > Update` kautta ja tarkista sen jälkeen, että alatunnisteessa lukee `2.4.2`. Jos et pysty päivittämään heti, sammuta BTCPay Server. Päivityksen jälkeen sinun on myös uusittava kokonaan macaroons-tunnisteesi ja `macaroons.db`-tiedostosi, uusittava kokonaan kaikkien muiden Lightning-taustajärjestelmien tunnistautumismerkkijonot sekä, mikäli olet luonut kuuman on-chain-lompakon BTCPay Serverin sisällä, siirrettävä kyseiset varat ja luotava lompakko uudelleen. Integraattoreiden tulee lisäksi päivittää NBXplorer versioon 2.6.10. Lähde: [BTCPay Server 2.4.2 -julkaisutiedot](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Versio 2.4.2 julkaistiin 7. elokuuta 2026. Julkaisutietojen mukaan se korjaa kriittisen haavoittuvuuden, jota jo hyödynnettiin todellisissa hyökkäyksissä ja josta ilmoittivat `brunoerg` ja `benthecarman` Bitcoin Red Team -työn kautta. Sama julkaisu korjaa myös TOTP-kaksitekijätodennuksen ohituksen Greenfield Basic -todennuksen kautta ja poistaa Greenfield Basic -todennuksen oletusarvoisesti käytöstä viisi minuuttia tilin luomisen jälkeen.

Ilmauksesta "hyödynnetään aktiivisesti" seuraa kaksi asiaa:

- **Päivittäminen ei ole vapaaehtoista eikä sitä pidä aikatauluttaa ensi viikolle.** Korjaamaton instanssi, johon pääsee internetistä, on joko päivitettävä tai sammutettava.
- **Päivittäminen ei yksin riitä.** Jos instanssisi vaarantui ennen kuin asensit korjauksen, hyökkääjällä voi jo olla kopiot Lightning-tunnistetiedoistasi ja kaikesta kuuman lompakon avainmateriaalista, jonka BTCPay Server loi sinulle. Nämä salaisuudet pysyvät voimassa päivityksen jälkeenkin, kunnes uusit ne. Alla oleva uusimista käsittelevä osio on se, jonka ihmiset jättävät väliin — ja juuri se osio todella suojaa varojasi.

## Vaihe 1 — Selvitä, mitä versiota käytät

Kirjaudu BTCPay Serveriisi ja katso **minkä tahansa sivun alatunnistetta**: versiomerkkijono näkyy siellä. Voit myös avata `Admin Dashboard > Server > Maintenance`, joka näyttää nykyisen version ja päivityksen hallintapainikkeet.

Jos instanssisi tarjoaa Greenfield API:n, myös `GET /api/v1/server/info` palauttaa version.

Kaikki alle `2.4.2` olevat versiot ovat haavoittuvia.

## Vaihe 2 — Päivitä

### Itse isännöity Docker-käyttöönotto (vakioasennus)

Tämä kattaa virallisen Docker-käyttöönoton, eli sen, jonka saat BTCPay Serverin dokumentaatiosta, LunaNoden yhden napsautuksen asentimesta ja useimmista VPS-asennuksista.

Yksinkertaisin tapa on verkkokäyttöliittymä:

1. Mene kohtaan `Admin Dashboard > Server > Maintenance`.
2. Napsauta **Update**.
3. Odota, että kontit ladataan ja käynnistetään uudelleen. Käyttöliittymä ei ole käytettävissä muutaman minuutin ajan.

Jos verkkokäyttöliittymä ei ole tavoitettavissa tai haluat mieluummin nähdä lokit, tee se SSH:n yli:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Oletusasennuksessa `$BTCPAY_BASE_DIRECTORY` on `/root`, joten hakemisto on `/root/btcpayserver-docker`. Skripti lataa uusimmat imaget, luo kontit uudelleen ja tulostaa lopputuloksena olevat versiot.

Docker-käyttöönotto toimittaa NBXplorerin BTCPay Serverin rinnalla, joten vakiopäivitys nostaa myös NBXplorerin suositeltuun versioon `2.6.10`. Jos ajat NBXploreria erikseen — tyypillistä integraattoreille ja räätälöidyille kokonaisuuksille — päivitä se erikseen.

### Umbrel

Avaa Umbrel-kojelauta, mene **App Storeen**, etsi BTCPay Server ja asenna päivitys, jos sellainen on tarjolla.

⚠️ **Tärkeää:** app-storen paketit ovat Umbrel-tiimin uudelleenpakkaamia, ja ne voivat olla tunteja tai päiviä alkuperäistä julkaisua jäljessä. Tarkista versio BTCPay Serverin alatunnisteesta päivityksen jälkeen. Jos se on edelleen alle `2.4.2`, **pysäytä sovellus** Umbrel-kojelaudalta ja odota paketoitua julkaisua sen sijaan, että jättäisit haavoittuvan instanssin käyntiin.

Erillinen Umbrel-ohje käsittelee itse sovellusta:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Sama logiikka: päivitä BTCPay Server StartOS-kaupasta ja varmista sitten versio alatunnisteesta. Jos paketoitu versio ei ole vielä `2.4.2`, pysäytä palvelu siihen asti kun se on.

### Hallinnoitu ja kolmannen osapuolen isännöinti

Jos joku muu ylläpitää instanssiasi (isännöintipalvelun tarjoaja, yhdistys, kaverin palvelin), tarvitset silti vahvistuksen. Kysy ylläpitäjältä alatunnisteessa näkyvä versiomerkkijono ja kysy nimenomaisesti, onko alla kuvattu päivityksen jälkeinen tunnistetietojen uusiminen tehty. "Päivitimme" ei ole sama vastaus kuin "uusimme macaroonisi".

## Vaihe 3 — Varmista, että päivitys todella meni läpi

Lataa BTCPay Serverin käyttöliittymä uudelleen ja lue versio alatunnisteesta. Siinä on luettava `2.4.2` tai uudempi.

Älä luota siihen, että päivityskomento päättyi ilman virhettä: resursseiltaan rajallisilla koneilla imagen lataus voi epäonnistua huomaamatta ja jättää aiemman kontin käyntiin. Lue versio, joka kerta.

## Vaihe 4 — Uusi tunnistetietosi

Tämä on se vaihe, joka muuttaa tilan "korjattu" tilaksi "turvassa". Koska haavoittuvuutta hyödynnettiin ennen korjauksen julkaisua, käsittele jokaista instanssisi hallussa ollutta salaisuutta sellaisena, jonka hyökkääjä voi tietää.

### Lightning: LND

Luo uudelleen macaroonit **ja** `macaroons.db`-tiedosto. Pelkkien macaroon-tiedostojen poistaminen ei riitä — LND johtaa macaroonit `macaroons.db`-tiedostoon tallennetusta juuriavaimesta, joten vanhan macaroonin kopion hallussaan pitävä hyökkääjä säilyttää pääsyn siihen asti, kunnes kyseinen tietokanta luodaan uudelleen.

Menettely on seuraava: pysäytä LND, poista `macaroons.db` ja `*.macaroon`-tiedostot verkon hakemistosta (mainnetissä `data/chain/bitcoin/mainnet/` LND:n datahakemiston sisällä), käynnistä sitten LND uudelleen ja avaa sen lukitus, jolloin ne luodaan uudelleen. Ota hakemistosta ensin varmuuskopio ja paritä uudelleen kaikki sovellukset, jotka käyttivät vanhoja macarooneja — BTCPay Server itse, Zeus, Thunderhub, RTL, Alby ja kaikki itse kirjoittamasi skriptit.

Jos LND on myös internetiin avattuna, tarkista samalla sen TLS-varmenne ja kaikki `lnd.conf`-tunnistetiedot.

### Lightning: muut taustajärjestelmät

Kaikkien, jotka tunnistautuvat solmullesi merkkijonolla, on saatava uusi merkkijono:

- **Core Lightning**: luo uudelleen rune tai yhteyden käyttämät pääsytunnistetiedot.
- **Phoenixd**: vaihda HTTP-salasana.
- **LNbits ja vastaavat**: kumoa ja luo uudelleen admin- ja invoice-avaimet.
- **Etäsolmun yhteysmerkkijonot**, jotka on tallennettu BTCPay Serverin kaupan asetuksiin: kirjoita ne uudelleen uusilla salaisuuksilla.

### BTCPay Serverin sisällä luotu kuuma on-chain-lompakko

Jos annoit BTCPay Serverin luoda sinulle on-chain-lompakon — sen sijaan että olisit liittänyt laitelompakon tai tuonut xpub:n, jonka avaimet eivät ole koskaan koskeneet palvelinta — kyseinen seed on ollut koneella.

Pidä sitä palaneena:

1. Luo uusi lompakko, mieluiten laitelompakolla, jotta avaimet eivät enää koskaan ole palvelimella.
2. Siirrä varat vanhasta lompakosta uuteen.
3. Korvaa kaupan asetuksissa oleva derivaatioskeema uudella lompakolla.
4. Älä koskaan käytä vanhaa seediä uudelleen.

Watch-only-kokoonpanot (xpub tai laitelompakko) eivät tarvitse tätä: yksityiset avaimet eivät ole koskaan olleet palvelimella. Juuri tämän vuoksi asennusohje suosittelee niitä.

### BTCPay Server -tilit ja API-avaimet

Kun kerran olet asialla:

- Vaihda instanssin jokaisen käyttäjätilin salasana.
- Kumoa ja luo uudelleen kaikki Greenfield-**API-avaimet**.
- Rekisteröi kaksitekijätodennus uudelleen, koska 2.4.2 korjaa 2FA-ohituksen.
- Avaa `Admin Dashboard > Server > Users` ja tarkista, ettei odottamattomia tilejä ole.
- Käy läpi viimeaikaiset **maksusuoritukset**, **pull payments** ja **hyvitykset** ja etsi kirjauksia, joita et ole itse luonut.
- Käy läpi webhookisi ja niiden salaisuudet.

## Vaihe 5 — Pysy ajan tasalla seuraavaa varten

Tietoturvajulkaisut auttavat vain niitä ylläpitäjiä, jotka kuulevat niistä:

- Seuraa [BTCPay Serverin julkaisuja GitHubissa](https://github.com/btcpayserver/btcpayserver/releases) — GitHub voi lähettää sinulle sähköpostia repositorion jokaisesta uudesta julkaisusta.
- Seuraa projektin tiedotuskanavia ja [virallista blogia](https://blog.btcpayserver.org/).
- Pidä instanssisi versiossa, jonka voit päivittää nopeasti: mitä enemmän olet jäljessä, sitä tuskallisempaa hätäpäivitys on.

Itse isännöinti antaa sinulle suvereniteetin maksuihisi. Tämän suvereniteetin hinta on juuri tämä: julkaisutietojen lukeminen ja se, että olet itse se joka korjaa.
