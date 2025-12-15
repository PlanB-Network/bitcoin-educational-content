---
name: LNbits Server
description: LNbits-palvelimen asennus ja konfigurointi Ubuntu VPS:lle Phoenixd:llä tai Umbrelilla
---

![cover](assets/cover.webp)



LNbits on avoimen lähdekoodin web-käyttöliittymä, joka muuttaa minkä tahansa Lightning-taustajärjestelmän (LND, Core Lightning, Phoenixd) täydelliseksi palvelualustaksi. Tämän itse isännöidyn ratkaisun avulla voit hallita useita Lightning-salkkuja erillään, ottaa käyttöön myyntipisteitä, luoda lahjoitusjärjestelmiä tai laskutuspalveluita säilyttäen samalla varojen täydellisen hallinnan.



Tämä opetusohjelma kattaa kaksi asennustapaa: **VPS Ubuntu with Phoenixd** (kevyt ratkaisu ilman täyttä Bitcoin-solmua) ja **Umbrel** (integrointi olemassa olevaan LND-solmuun). Toisin kuin Plan ₿ Academyn yleisessä LNbits-oppaassa, jossa käsitellään käsitteitä ja laajennuksia, tässä oppaassa keskitytään vaiheittaisiin teknisiin asennustoimenpiteisiin.



## Mikä on LNbits?



LNbits on Python-kielellä (FastAPI) kehitetty Lightning-kirjanpitojärjestelmä, joka on yhteydessä olemassa olevaan backendiin (LND, Core Lightning, Phoenixd). Toisin kuin perinteiset Lightning-solmut, LNbits tarjoaa helppokäyttöisen käyttöliittymän useiden eristettyjen salkkujen hallintaan, joilla on omat API-avaimet. Voit luoda alatilejä perheellesi, työntekijöille tai projekteille antamatta heille pääsyä kaikkiin varoihisi.



Riippumaton arkkitehtuuri tallentaa tiedot SQLite- (oletus) tai PostgreSQL-tietokantaan (tuotanto), kun taas varat pysyvät Lightning-taustajärjestelmän hallinnassa. Tämä erottelu takaa siirrettävyyden: voit siirtyä Phoenixd:stä LND:een menettämättä käyttäjätietojasi.



## Tärkeimmät ominaisuudet



LNbits tarjoaa monipuolisen **laajennusjärjestelmän**: LNbNs tarjoaa: TPoS (myyntipiste), Paywall (sisällön rahaksi muuttaminen), Events (lipunmyynti), LndHub (palvelin BlueWalletille), Bolt Cards (NFC-maksut), Split Payments (automaattinen jakelu) ja User Manager (käyttäjähallinta ja todennus).



Näyttötaululla** näytetään reaaliaikaiset saldot, tapahtumahistoria ja laskutustyökalut. Kullakin wallet:llä on yksilöllinen URL-osoite, joka sisältää sen API-avaimet, joten käyttö on mahdollista ilman perinteistä kirjautumista. Kolmiportainen API-avainjärjestelmä** (admin, invoice, read-only) tarjoaa yksityiskohtaista käyttöoikeuksien hallintaa turvallisia integraatioita varten.



LNbits toteuttaa natiivisti **LNURL** (LNURL-pay, LNURL-withdraw, LNURL-auth) ja tukee **Lightning Address**, mikä takaa yhteensopivuuden nykyaikaisten Lightning-lompakoiden kanssa ja helpottaa ammattimaisten palvelujen käyttöönottoa.



## Tuetut alustat



**Ubuntu VPS**: Kevyt ratkaisu ilman täyttä Bitcoin-solmua. Edellytykset: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + verkkotunnus vaaditaan julkista näkyvyyttä varten (LNURL-palvelut).



**Umbrel**: Helppo asennus App Storesta. Edellytys: toimiva Umbrel-solmu, jossa on synkronoitu LND ja avoimet kanavat. Automaattinen konfigurointi.



Alla on linkkejä Umbrel- ja Umbrel LND -oppaisiin:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Asennus Ubuntu VPS Phoenixd:llä



### Vaihe 1: VPS-palvelimen suojaaminen



** Ennen asennusta** sinun on suojattava Ubuntu VPS-palvelimesi alan sääntöjen mukaisesti. Tämä vaihe on **kriittinen** infrastruktuurisi ja Lightning-varojesi suojaamiseksi.



Tässä on yksityiskohtainen opas, jonka avulla pääset alkuun: **[Ubuntu-palvelimen alustava konfigurointi - Vaiheittainen opas](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)**, kirjoittanut Daniel P. Costas.



Tässä oppaassa käsitellään käyttäjien konfigurointia, suojattua SSH:ta, palomuuria (UFW), fail2bania, automaattisia päivityksiä ja hyviä järjestelmäturvakäytäntöjä.



### Vaihe 2: Phoenixd:n asentaminen



Kun palvelimesi on suojattu, sinun on asennettava ja konfiguroitava Phoenixd. Plan ₿ Akatemia tarjoaa kattavan erityisen oppaan, joka kattaa asennuksen, seed:n tuottamisen ja systemd-palvelun konfiguroinnin :



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Kun Phoenixd on toiminnassa (tarkista `./phoenix-cli getinfo`), merkitse muistiin **HTTP-salasana** tiedostosta `~/.phoenix/phoenix.conf` - tarvitset sitä, kun haluat yhdistää LNbitsin Phoenixd:hen.



### LNbitsin käyttöönotto



Asenna UV ja kloonaa LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfiguroi Phoenixd-taustapalvelu:


```bash
cp .env.example .env && nano .env
```



Lisää tiedostoon `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Testaa `uv run lnbits --host 0.0.0.0 --port 5000` ja luo sitten systemd-palvelu komennolla `Wants=phoenixd.service`.



## Alkuasennus ja ensimmäinen käyttö



### SuperUserin aktivointi



Aktivoi järjestelmänvalvojan käyttöliittymä tiedostossa `.env` :


```
LNBITS_ADMIN_UI=true
```



Käynnistä LNbits uudelleen (`sudo systemctl restart lnbits`) ja hae SuperUser ID:


```bash
cat ~/lnbits/data/.super_user
```



Siirry osoitteeseen `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>` hallintapaneelia varten. "Palvelin"-valikossa voit määrittää rahoituslähteet, laajennukset ja käyttäjätilit.



### Turvallinen tilin luominen



**Tärkeää julkisuuden kannalta**: On **kriittisen tärkeää** poistaa käyttäjätilien vapaa luominen käytöstä, jos LNbits-instanssisi on julkisessa verkkotunnuksessa, johon pääsee Internetistä.



Siirry SuperUserin hallintakäyttöliittymästä kohtaan "Asetukset" ja sitten kohtaan "Käyttäjien hallinta". Sieltä löydät kohdan "Salli uusien käyttäjien luominen".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Julkista näyttelyä varten verkkotunnuksella** :




- Sinun on poistettava käytöstä** vaihtoehto "Salli uusien käyttäjien luominen"
- Ilman tätä suojausta kuka tahansa Internetissä voi luoda tilin instanssissasi
- Hyökkääjä voi luoda tilejä ja käyttää Lightning-solmusi likviditeettiä tietämättäsi
- Käyttäjätilit on luotava manuaalisesti SuperUser-käyttöliittymästä



**Vain paikalliseen käyttöön** :




- Tämä vaihtoehto on vähemmän kriittinen, jos instanssisi on käytettävissä vain paikallisesti (http://localhost:5000)
- Tämän vaihtoehdon poistaminen käytöstä on kuitenkin hyvä yleinen turvallisuuskäytäntö



Kun se on määritetty, vain SuperUser-ylläpitäjä voi luoda uusia käyttäjätilejä "Käyttäjät"-käyttöliittymän kautta. Tämä lähestymistapa takaa täydellisen valvonnan sen suhteen, kuka voi käyttää Lightning-infrastruktuuria ja varoja.



### Ensimmäisen kanavan avaaminen



Phoenixd hallinnoi kanavia automaattisesti automaattisen likviditeetin avulla. Luo ~30 000 sats:n Lightning-lasku LNbitsistä ja maksa se toisesta wallet:sta. Phoenixd avaa automaattisesti kanavan ACINQ:lle. Avausmaksu (~20-23k sats) vähennetään, loppusaldo (~7-10k sats) näkyy on-chain vahvistuksen jälkeen.



Tarkista tila komennolla `./phoenix-cli getinfo`. Harkitse sitten automaattisen likviditeetin poistamista käytöstä (`auto-liquidity=off` tiedostossa `phoenix.conf`) kanavien avautumisen hallitsemiseksi.



### Julkinen näyttö ja HTTPS



**Tärkeää**: HTTPS on pakollinen julkista näyttöä varten (API-avainten turvallisuus + LNURL-yhteensopivuus). Ohita tämä vaihe vain paikalliseen käyttöön.



**Caddy (suositeltava)**: automaattinen SSL. `sudo apt install -y caddy`, muokkaa `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Käynnistä uudelleen: `sudo systemctl restart caddy`.



**Nginx** : Enemmän valvontaa. Asenna `nginx certbot python3-certbot-nginx`, luo `/etc/nginx/sites-available/lnbits` :


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Aktivoi: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Lisää tiedostoon `.env`: `FORWARDED_ALLOW_IPS=*`



## Sateenvarjon asennus



### Käyttöönotto App Storesta



Mene Umbrel App Storeen, etsi "LNbits" ja napsauta "Install".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel tarkistaa automaattisesti tarvittavat riippuvuudet. LNbits vaatii toimiakseen Lightning Noden (LND). Jos Lightning-solmusi on jo toiminnassa, vahvista se napsauttamalla "Install LNbits".



![Dépendances LNbits](assets/fr/02.webp)



Umbrel lataa Docker-kuvan, määrittää automaattisesti yhteydet LND:een ja käynnistää kontin (2-5 minuuttia). Asennus tapahtuu kokonaan taustalla.



### SuperUserin alkuperäinen konfigurointi



Ensimmäisellä käynnistyskerralla LNbits pyytää sinua luomaan SuperUser-ylläpitäjätilin. Syötä käyttäjätunnus ja suojattu salasana, joilla suojataan pääsy hallintakäyttöliittymään.



![Configuration SuperUser](assets/fr/03.webp)



**Tärkeää**: Tällä SuperUser-tilillä on täydet oikeudet LNbits-instanssissasi. Valitse vahva salasana ja pidä se turvassa.



Kun olet luonut tilin, pääset automaattisesti päähallintakäyttöliittymään. Umbrel on jo perustanut LND:n rahoituslähteeksi - kaikki Lightning-maksut kulkevat nykyisten kanaviesi kautta.



### Pääsy järjestelmänvalvojan käyttöliittymään



Napsauta vasemmanpuoleisessa valikossa "Asetukset" päästäksesi koko hallintapaneeliin.



![Interface Settings](assets/fr/04.webp)



"Lompakoiden hallinta"-osiossa näytetään tärkeimmät tiedot kokoonpanostasi:




- Rahoituslähde** : LndBtcRestWallet (suora yhteys LND Umbrel-solmuun)
- Solmutasapaino** : Lightning-kanavissasi käytettävissä oleva kokonaislikviditeetti
- LNbits Balance**: LNbits-järjestelmään osoitetut varat (aluksi 0 sats)



Voit nyt hyödyntää suoraan Umbrel-solmusi likviditeettiä kaikissa luomissasi LNbits-lompakoissa. Mitään lisäkonfiguraatioita ei tarvita - LNbits on toiminnassa.



### Käyttäjien hallinta



Yksi LNbitsin tehokkaimmista ominaisuuksista on sen kyky luoda useita itsenäisiä käyttäjiä, joilla kullakin on salasanatodennus ja erilliset lompakot. Tämän arkkitehtuurin ansiosta voit hyödyntää Umbrel-solmusi likviditeettiä ja tarjota samalla täysin eristettyjä alatilejä eri käyttötarkoituksiin: liiketoimintaan, perheeseen, työntekijöihin, projekteihin jne.



Klikkaa sivuvalikossa "Users", jotta pääset käyttäjien hallintaan. Lisää uusi käyttäjä napsauttamalla "CREATE ACCOUNT".



![Gestion des utilisateurs](assets/fr/05.webp)



Täytä käyttäjän luontilomake:




- Käyttäjätunnus**: Käyttäjätunnus (esimerkki: "satoshi")
- Aseta salasana**: Aktivoi tämä vaihtoehto tunnistautumissalasanan asettamiseksi
- Salasana** ja **Salasanan toistaminen**: Aseta tämän käyttäjän salasana



![Création utilisateur satoshi](assets/fr/06.webp)



Valinnaiset kentät (Nostr Public Key, Sähköposti, Etunimi, Sukunimi) voidaan jättää tyhjiksi, jotta määritys olisi mahdollisimman vähäistä. Vahvista klikkaamalla "CREATE ACCOUNT".



![Confirmation utilisateur créé](assets/fr/07.webp)



Uusi käyttäjäsi näkyy nyt käyttäjäluettelossa hänen yksilöllisellä tunnuksellaan ja käyttäjänimellään.



![Liste des utilisateurs](assets/fr/08.webp)



**Tärkeä kohta**: Jokainen käyttäjä voi kirjautua sisään täysin itsenäisesti omalla salasanallaan. SuperUserin ylläpitäjä säilyttää täyden hallinnan hallintakäyttöliittymän kautta.



### Käyttäjän wallet hallinta



Nyt kun "satoshi"-käyttäjä on luotu, sinun on annettava hänelle wallet Lightning. Napsauta kyseisen käyttäjän wallet-kuvaketta (toinen kuvake) ja valitse sitten "CREATE NEW WALLET".



![Gestion des wallets](assets/fr/09.webp)



Valintaikkuna pyytää sinua nimeämään wallet:n. Kirjoita kuvaava nimi (esim. "Wallet Of Satoshi") ja valitse näyttövirta (CUC, USD, EUR jne.).



![Création wallet](assets/fr/10.webp)



Napsauta "CREATE". LNbits luo välittömästi toimivan wallet Lightningin tälle käyttäjälle.



![Confirmation wallet créé](assets/fr/11.webp)



Näet nyt kaksi olemassa olevaa lompakkoa: automaattisesti luotu oletusarvoinen wallet "LNbits wallet" ja uusi "Wallet Of Satoshi". Käyttäjäkokemuksen yksinkertaistamiseksi voit poistaa oletusarvoisen wallet:n klikkaamalla poistokuvaketta (punainen roskakori).



![Wallet final unique](assets/fr/12.webp)



satoshi-käyttäjällä on nyt yksi, selvästi tunnistettava wallet. Kukin wallet-käyttäjä toimii täysin itsenäisesti ja käyttää samalla taustalla olevan LND-solmun likviditeettiä.



**Konsepti**: Kaikki nämä lompakot jakavat Umbrel-solmusi globaalin likviditeetin. Et luo uusia Lightning-kanavia kullekin wallet:lle - LNbits toimii älykkäänä kirjanpitokerroksena, joka hallinnoi varojen jakamista olemassa olevassa Lightning-infrastruktuurissasi. Siinä on LNbitsin multi-wallet-järjestelmän voima.



### Käyttäjän kirjautuminen



Kirjaudu ulos SuperUser-tililtä (kuvake oikeassa yläkulmassa) ja palaa LNbitsin kirjautumissivulle. Voit nyt kirjautua sisään uuden käyttäjän tunnuksilla.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Syötä aiemmin määritetty käyttäjänimi ("satoshi") ja salasana ja napsauta sitten "LOGIN". Käyttäjä pääsee suoraan henkilökohtaiseen wallet:ään, joka on täysin eristetty hallintaliittymästä.



### Interface käyttäjältä wallet



Kun käyttäjä on kirjautunut sisään, hänellä on pääsy koko wallet Lightning -käyttöliittymään.



![Interface wallet utilisateur](assets/fr/14.webp)



Käyttöliittymän ominaisuudet :




- Nykyinen saldo**: Näytetään muodossa sats ja valittuna valuuttana (tässä esimerkissä CUC)
- Tärkeimmät toimet**: PASTE REQUEST, CREATE INVOICE, QR-kuvake (pikaskannaus)
- Tapahtumahistoria** : Täydellinen luettelo kaikista maksuista ja kuiteista
- Oikea sivupaneeli**: Konfigurointi- ja käyttömahdollisuudet



### Mobiilipääsy wallet:een



Oikeanpuoleinen sivupaneeli tarjoaa erityisen käytännöllisen ominaisuuden: wallet:n mobiilikäyttö. Tutustu käytettävissä oleviin vaihtoehtoihin avaamalla "Mobile Access" -osio.



![Mobile Access](assets/fr/15.webp)



LNbits tarjoaa useita tapoja käyttää tätä wallet:ää älypuhelimessa:



**Vaihtoehto 1: Yhteensopivat mobiilisovellukset




- Lataa **Zeus** tai **BlueWallet** App Storesta tai Google Playsta
- Aktivoi **LndHub**-laajennus LNbitsissä tätä wallet:a varten
- Skannaa LndHubin QR-koodi mobiilisovelluksella yhdistääksesi wallet:n



**Vaihtoehto 2: Suora yhteys mobiiliselaimen kautta**




- "Vie puhelimeen QR-koodilla" -kohdassa näkyvä QR-koodi sisältää wallet:n täydellisen URL-osoitteen, jossa on integroitu todennus
- Skannaa tämä QR-koodi älypuhelimellasi avataksesi wallet suoraan mobiiliselaimellasi
- Lisää sivu aloitusnäyttöön nopeaa käyttöä varten



**Tärkeä turvallisuus**: Tämä URL-osoite sisältää API:n avaimet wallet:n täyttä käyttöä varten. Älä koskaan jaa sitä julkisesti. Käsittele tätä QR-koodia kuten Bitcoin:n yksityisiä avaimia - kuka tahansa, joka skannaa tämän QR-koodin, saa täyden pääsyn wallet:een.



Tämä mobiiliominaisuus tekee LNbits Umbrel -instanssistasi todellisen Lightning wallet -palvelimen sinulle ja ystävillesi, mutta säilytät samalla täydellisen määräysvallan varoistasi itse isännöimäsi solmun ansiosta.



### Käyttäjän käyttöoikeuksien jakaminen



Tämän monikäyttäjäkokoonpanon tärkein käyttötapaus on **lompakoiden jakaminen perheen tai lähipiirin kanssa**. Kun olet luonut käyttäjän, jolla on oma wallet-tunnus (esimerkissämme esimerkiksi "satoshi"), voit jakaa nämä kirjautumistiedot luotettavien perheenjäsenten kanssa.



**Käyttäytymisturva Umbrelissa**: Pääsy LNbits-instanssisi Umbrelissa on luonnollisesti suojattu, sillä sitä voi käyttää vain :




- Paikallisessa verkossa** : Samaan WiFi/Ethernet-verkkoon liitetyt kotitaloutesi jäsenet voivat käyttää instanssia
- VPN:n kautta**: Jos käytät VPN:ää, kuten Tailscale, joka on konfiguroitu Umbrel-palvelimelle, valtuutetut käyttäjät voivat saada turvallisen etäyhteyden..



Tämä kaksoissuojaus (verkkoyhteys + käyttäjän todennus) tekee "Salli uusien käyttäjien luominen" -vaihtoehdon vähemmän kriittiseksi Umbrelissa. Vain henkilöt, joilla on jo pääsy verkkoon tai VPN:ään, pääsevät kirjautumisliittymään.



**Tyypillinen skenaario**: Luodaan "isä"-tili, "äiti"-tili, "yritys"-tili ja niin edelleen. Jokaisella perheenjäsenellä on oma erillinen wallet Lightning -tilinsä, mutta hän hyötyy Umbrel-solmusi yhteisestä likviditeetistä. Jaa vain käyttäjätunnus ja salasana - käyttäjä voi sitten muodostaa yhteyden millä tahansa laitteella lähiverkossasi tai Tailscale VPN:n kautta. Katso lisätietoja erillisestä Tailscale-oppaastamme:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Tutustu saatavilla oleviin laajennuksiin



Palaa SuperUser-käyttöliittymään ja avaa vasemmanpuoleisen paneelin "Laajennukset"-valikko tutustuaksesi koko LNbits-laajennusten ekosysteemiin.



![Extensions disponibles](assets/fr/16.webp)



LNbits tarjoaa laajan valikoiman laajennuksia, jotka tekevät instanssistasi todellisen Lightning-palvelualustan:





- Jukebox**: sats-käyttöinen jukebox-järjestelmä (Spotify-maksut)
- Tukiliput**: Maksullinen tukijärjestelmä (saat satss vastaamaan kysymyksiin)
- TPoS**: Turvallinen, mobiili myyntipiste vähittäiskauppiaiden päätelaite
- User Manager**: edistynyt käyttäjien ja wallet:n hallinta (jota olemme juuri käyttäneet)
- Tapahtumat**: Tapahtumalippujen myynti ja vahvistaminen
- LNURLDevices**: Myyntipisteiden hallinta, pankkiautomaatit, kytketyt kytkimet
- SMTP**: Mahdollistaa käyttäjien lähettää sähköposteja ja ansaita satssia
- Boltcards**: NFC-korttien ohjelmointi Lightning tap-to-pay-maksuja varten
- NostrNip5**: Luo NIP5-osoitteita verkkotunnuksillesi
- Jaetut maksut**: Maksujen automaattinen jakaminen useiden lompakoiden välillä



Jokainen laajennus aktivoidaan yhdellä napsautuksella tästä käyttöliittymästä. Laajennukset, joissa on merkintä "ILMAINEN", ovat maksuttomia, kun taas jotkut ovat saatavilla maksullisina versioina. Tutustu luetteloon löytääksesi tarpeisiisi sopivat laajennukset - olipa kyse sitten liiketoiminnasta, perheenhallinnasta tai Lightning Network:n ominaisuuksien kokeilemisesta.



## Edut ja rajoitukset



**Hyötyjä**: Rahoituksellinen riippumattomuus (varojen/avainten/tietojen täydellinen hallinta), arkkitehtuurinen joustavuus (häviötön VPS→full node-siirtyminen), ammattimainen laajennusjärjestelmä, intuitiivinen käyttöliittymä.



**Rajoitukset** : Ohjelmisto on beta-versiossa (varovaisuus määrien suhteen), tietoturva ylläpitäjän vastuulla, arkaluonteisia API-avaimia sisältävät URL-osoitteet (HTTPS pakollinen), usean käyttäjän hallinta edellyttää huoltajan vastuuta.



## Parhaat käytännöt



**Backups**: LNbits-tietokanta, .env-tiedostot. Automatisoidaan päivittäin, pidetään poissa tuotantopalvelimelta, salattu. Testaa palautukset säännöllisesti.



**Kunnossapito**: Tarkista säännöllisesti päivitykset (LNbits, Lightning backend, käyttöjärjestelmä). Tarkista aina julkaisutiedot ennen suuria päivityksiä.





- Sateenvarjolla**: App Store ilmoittaa automaattisesti uusista versioista. Synkronoi laajennukset "Laajennusten hallinta" > "Päivitä kaikki". Tarkista SQLite-tietokannan sisällyttäminen Umbrelin automaattisiin varmuuskopioihin.
- VPS**: Git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Seuraa järjestelmälokeja: `sudo journalctl -u lnbits -f`.



## Päätelmä



LNbitsin omahosting tarjoaa konkreettisen tien Lightningin taloudelliseen riippumattomuuteen. VPS+Phoenixd tarjoaa kevyen ratkaisun nopeisiin palveluihin, Umbrel täydellinen integrointi olemassa olevaan Bitcoin-solmuun. Skaalautuva arkkitehtuuri mahdollistaa kehityksen yksinkertaisesta monikäyttäjä-wallet:sta kehittyneisiin liiketoimintakäyttötapauksiin.



Itsehostaminen merkitsee vastuuta: varmuuskopioi siemenet, suojaa pääsy, aloita vaatimattomilla summilla. Näillä varotoimilla LNbitsistä tulee vankka ratkaisu salamatalouteen, mutta samalla se säilyttää hajautuksen ja itsenäisyyden.



## Resurssit



### Viralliset asiakirjat




- [LNbits Documentation](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [Virallinen asennusopas](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Yhteisön oppaat




- [Ubuntu-palvelimen alustava konfigurointi](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) Daniel P. Costas (VPS-turvallisuus askel askeleelta)
- [LNbits + Phoenixd asennus Ubuntu VPS](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) Daniel P. Costas (täydellinen opas)
- [LNbits-palvelin Clearnetissä](https://ereignishorizont.xyz/lnbits-server/en/) Axelilta
- [LNbits on VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes