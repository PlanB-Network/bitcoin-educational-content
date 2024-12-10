---
name: GnuPG
description: Kuinka varmistaa ohjelmiston eheyden ja aitouden tarkistaminen?
---
![cover](assets/cover.webp)

Ohjelmiston lataamisen yhteydessä on erittäin tärkeää varmistaa, että sitä ei ole muutettu ja että se todella tulee virallisesta lähteestä. Tämä pätee erityisesti Bitcoiniin liittyvään ohjelmistoon, kuten lompakko-ohjelmistoon, joka mahdollistaa pääsyn rahojasi koskevien avainten turvaamisen. Tässä oppaassa näemme, kuinka tarkistaa ohjelmiston eheyden ja aitouden ennen sen asentamista. Käytämme esimerkkinä Sparrow Walletia, joka on bitcoin-käyttäjien suosima lompakko-ohjelmisto, mutta menettely on sama minkä tahansa muun ohjelmiston kohdalla.

Eheyden varmistaminen tarkoittaa ladatun tiedoston muuttumattomuuden tarkistamista vertaamalla sen digitaalista sormenjälkeä (eli sen hajautusarvoa) virallisen kehittäjän antamaan hajautusarvoon. Jos ne täsmäävät, se tarkoittaa, että tiedosto on identtinen alkuperäisen kanssa eikä sitä ole korruptoitunut tai muokattu hyökkääjän toimesta.

Aitouden varmistaminen puolestaan takaa, että tiedosto todella tulee viralliselta kehittäjältä eikä huijarilta. Tämä tehdään tarkistamalla digitaalinen allekirjoitus. Tämä allekirjoitus todistaa, että ohjelmisto on allekirjoitettu legitiimin kehittäjän yksityisellä avaimella.

Jos näitä tarkistuksia ei suoriteta, on olemassa riski asentaa haittaohjelma, joka saattaa sisältää muokattua koodia. Tämä koodi saattaa joko varastaa tietoja, kuten yksityiset avaimet, tai estää pääsyn tiedostoihisi. Tämäntyyppinen hyökkäys on melko yleinen, erityisesti avoimen lähdekoodin ohjelmistojen yhteydessä, joista voidaan jakaa väärennettyjä versioita.

Tämän tarkistuksen suorittamiseen käytämme kahta työkalua: hajautusfunktioita eheyden varmistamiseen ja GnuPG:tä, avoimen lähdekoodin työkalua, joka toteuttaa PGP-protokollan, aitouden varmistamiseen.

## Edellytykset

Jos käytät **Linuxia**, GPG on esiasennettu useimpiin jakeluihin. Jos ei, voit asentaa sen seuraavalla komennolla:

```bash
sudo apt install gnupg
```

**macOS**:lle, jos et ole vielä asentanut Homebrew-paketinhallintaa, tee se seuraavilla komennoilla:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Asenna sitten GPG tällä komennolla:

```bash
brew install gnupg
```
**Windowsille**, jos sinulla ei ole GPG:tä, voit asentaa [Gpg4win](https://www.gpg4win.org/) -ohjelmiston.
![GnuPG](assets/notext/01.webp)

## Asiakirjojen lataaminen

Aloitamme tarvittavien asiakirjojen hankkimisella. Vieraile [Sparrow Walletin virallisella sivustolla kohdassa "*Download*"](https://sparrowwallet.com/download/). Jos haluat tarkistaa toisen ohjelmiston, mene kyseisen ohjelmiston verkkosivustolle.

![GnuPG](assets/notext/02.webp)

Voit myös mennä [projektin GitHub-repositorioon](https://github.com/sparrowwallet/sparrow/releases).

![GnuPG](assets/notext/03.webp)

Lataa asennustiedosto käyttöjärjestelmääsi vastaavalle ohjelmistolle.

![GnuPG](assets/notext/04.webp)

Tarvitset myös tiedoston hajautusarvon, jota kutsutaan usein "*SHA256SUMS*" tai "*MANIFEST*".

![GnuPG](assets/notext/05.webp)

Lataa myös tiedoston PGP-allekirjoitus. Tämä on `.asc`-muodossa oleva asiakirja.

![GnuPG](assets/notext/06.webp)
Varmista, että sijoitat kaikki nämä tiedostot samaan kansioon seuraavia vaiheita varten.
Lopuksi tarvitset kehittäjän julkisen avaimen, jota käytämme PGP-allekirjoituksen vahvistamiseen. Tämä avain on usein saatavilla joko ohjelmiston verkkosivustolta, projektin GitHub-repositoriosta, joskus kehittäjän sosiaalisen median kautta tai erikoistuneilla sivustoilla kuten Keybase. Sparrow Walletin tapauksessa voit löytää kehittäjä Craig Raw'n julkisen avaimen [Keybasesta](https://keybase.io/craigraw). Ladataksesi sen suoraan terminaalista, suorita komento:

```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```

![GnuPG](assets/notext/07.webp)

## Allekirjoituksen Vahvistaminen

Allekirjoituksen vahvistamisen prosessi on sama **Windows**-, **macOS**- ja **Linux**-järjestelmissä. Normaalisti olet jo tuonut julkisen avaimen edellisessä vaiheessa, mutta jos et, tee se komennolla:

```bash
gpg --import [avaimen polku]
```

Korvaa `[avaimen polku]` kehittäjän julkisen avaimen tiedoston sijainnilla.

![GnuPG](assets/notext/08.webp)

Vahvista allekirjoitus seuraavalla komennolla:

```bash
gpg --verify [tiedosto.asc]
```

Korvaa `[tiedosto.asc]` allekirjoitustiedoston polulla. Sparrow'n tapauksessa tämä tiedosto on nimeltään "*sparrow-2.0.0-manifest.txt.asc*" version 2.0.0 osalta.

![GnuPG](assets/notext/09.webp)

Jos allekirjoitus on validi, GPG ilmoittaa tästä sinulle. Voit sitten siirtyä seuraavaan vaiheeseen, sillä tämä vahvistaa tiedoston aitouden.

![GnuPG](assets/notext/10.webp)

## Hashin Vahvistaminen
Nyt kun ohjelmiston aitous on vahvistettu, on myös tarpeellista vahvistaa sen eheys. Vertaamme ohjelmiston hashia kehittäjän tarjoamaan hashiin. Jos ne täsmäävät, se takaa, että ohjelmiston koodia ei ole muutettu.

**Windows**-järjestelmässä avaa terminaali ja suorita seuraava komento:

```bash
CertUtil -hashfile [tiedoston polku] SHA256 | findstr /v "hash"
```

Korvaa `[tiedoston polku]` asennustiedoston sijainnilla.

![GnuPG](assets/notext/11.webp)

Terminaali palauttaa ladatun ohjelmiston hashin.

![GnuPG](assets/notext/12.webp)

Huomaa, että joissakin ohjelmistoissa saattaa olla tarpeen käyttää eri hash-funktiota kuin SHA256. Tässä tapauksessa korvaa komennossa hash-funktion nimi.

Vertaa sitten tulosta vastaavaan arvoon tiedostossa "*sparrow-2.0.0-manifest.txt*".

![GnuPG](assets/notext/13.webp)

Minun tapauksessani näemme, että kaksi hashia täsmäävät täydellisesti.

**macOS**- ja **Linux**-järjestelmissä hashin vahvistusprosessi on automatisoitu. Ei ole tarpeen manuaalisesti tarkistaa kahden hashin vastaavuutta kuten Windowsissa.

Suorita tämä komento **macOS**-järjestelmässä:

```bash
shasum --check [tiedoston nimi] --ignore-missing
```

Korvaa `[tiedoston nimi]` asennustiedoston nimellä. Esimerkiksi Sparrow Walletin tapauksessa:

```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```

Jos hashit täsmäävät, sinun pitäisi nähdä seuraava tulos:

```bash
Sparrow-2.0.0.dmg: OK
```
**Linux**-käyttöjärjestelmässä komento on samankaltainen:
```bash
sha256sum --check [tiedoston nimi] --ignore-missing
```

Ja jos tiivisteet täsmäävät, sinun pitäisi nähdä seuraava tuloste:

```bash
sparrow_2.0.0-1_amd64.deb: OK
```

Voit nyt olla varma, että lataamasi ohjelmisto on sekä aito että ehjä. Voit jatkaa sen asentamista koneellesi.

Jos pidit tätä opasta hyödyllisenä, arvostaisin peukkua ylös alla. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissasi. Suurkiitokset!

Suosittelen myös tutustumaan toiseen oppaaseen VeraCryptista, ohjelmistosta, joka mahdollistaa tallennuslaitteiden salaamisen ja salauksen purkamisen.

https://planb.network/tutorials/others/general/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5