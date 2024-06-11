---
name: LN VPN

description: VPN:n asennus
---

![kuva](assets/cover.webp)

LN VPN on mukautettava VPN-palvelu, joka hyväksyy maksut vain lightning-maksuina. Tänään näytän, miten sitä käytetään ja miten voit jättää vähemmän jälkiä selatessasi internetiä.

Laadukkaita VPN-palveluntarjoajia on monia, ja olemme tehneet kattavan arvostelun tässä artikkelissa (hyperlinkki). LN VPN kuitenkin erottuu joukosta, emmekä voineet jättää käyttämättä tilaisuutta esitellä sitä sinulle.

Useimmat VPN-palveluntarjoajat, kuten ProtonVPN ja Mullvad, tarjoavat mahdollisuuden maksaa bitcoineilla, mutta vaativat tilin luomista ja suunnitelman ostamista pidemmäksi tai lyhyemmäksi ajaksi, mikä ei välttämättä sovi kaikkien budjettiin.

LN VPN mahdollistaa VPN:n käytön tarpeen mukaan lyhyimmillään yhden tunnin ajan, kiitos bitcoin-maksujen toteutuksen lightning-verkon kautta. Välittömät ja nimettömät lightning-maksut avaavat uusia mahdollisuuksia mikromaksuille.

> 💡 Tämä opas kuvaa, miten LN VPN:ää käytetään Linux Ubuntu 22.04 LTS -järjestelmässä.

## Edellytykset: Wireguard

Yksinkertaisesti sanottuna Wireguardia käytetään luomaan turvallinen tunneli tietokoneesi ja etäpalvelimen välille, jonka kautta selataan internetiä. Tämän palvelimen IP-osoite näkyy sinun osoitteenasi niin kauan kuin vuokraat sen seuraamalla tätä opasta.

Virallinen Wireguard-asennusopas: https://www.wireguard.com/install/

```
Wireguard-asennus
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Edellytykset: Lightning Bitcoin -lompakko

Jos sinulla ei vielä ole Lightning Bitcoin -lompakkoa, ei huolta, olemme luoneet sinulle erittäin yksinkertaisen oppaan täällä. (LN-opetusosio voi auttaa sinua)

## Vaihe 1: Vuokrasopimuksen tekeminen

Osoitteesta https://lnvpn.com sinun tulee valita VPN-tunnelin poistumis-IP:n maa ja kesto. Kun nämä parametrit on asetettu, klikkaa Maksaa lightningilla.

![kuva](assets/1.webp)

Näytölle ilmestyy lightning-lasku, ja sinun tarvitsee vain skannata se lightning-lompakollasi.

Kun lasku on maksettu, sinun on odotettava muutama sekunti korkeintaan kaksi minuuttia, jotta Wireguard-konfiguraatioasetuksesi luodaan. Jos se kestää hieman kauemmin, älä paniikoi, olemme tehneet tämän toimenpiteen kymmeniä kertoja, ja joskus se vain vie hieman enemmän aikaa.
Seuraava näyttö ilmestyy ja sinun tarvitsee vain klikata "Lataa tiedostona" saadaksesi konfiguraatiotiedoston, jonka nimi näyttää tältä lnvpn-xx-xx.conf, missä "xx" vastaa nykyistä päivämäärää.
![kuva](assets/2.webp)

## Vaihe 2: Tunnelin aktivoiminen

Ensimmäiseksi sinun tulee nimetä edellisessä vaiheessa saatu konfiguraatiotiedosto uudelleen, jotta Wireguard tunnistaa sen automaattisesti.

Mene latauskansioosi joko terminaali-ikkunassa tai tiedostonhallinnassa ja nimeä lnvpn-xx-xx.conf-tiedosto wg0.conf-tiedostoksi näin:

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

Siinä se! Tunneli on aktivoitu!

## Vaihe 3: Tarkistus

Käytä online-palvelua kuten whatismyip varmistaaksesi, että julkinen IP-osoitteesi on nyt se VPN, jonka juuri aktivoit.

## Vaihe 4: Poistaminen käytöstä
Kun vuokra-aikasi päättyy, sinun täytyy katkaista yhteys saadaksesi jälleen pääsyn internetiin. Voit toistaa vaiheet 1–3 aina, kun haluat muodostaa vuokrayhteyden LN VPN:ään.
Poista tunneli käytöstä:

```
    $ sudo ip link delete dev wg0
```

Siinä se on! Nyt tiedät, miten käyttää LN VPN:ää, ainutlaatuista VPN-palvelua!