---
name: Bacca
description: Ledgerin määrittäminen ilman Ledger Live -ohjelmistoa
---
![cover](assets/cover.webp)

Jos käytät Ledgeriä, olet luultavasti huomannut, että sinun on käytävä läpi Ledger Live -ohjelmisto, ainakin laitteen alkukonfigurointi, sen aitouden tarkistaminen ja Bitcoin-sovelluksen asentaminen siihen. Tämän konfiguroinnin jälkeen monet Bitcoin-käyttäjät käyttävät kuitenkin mieluummin erikoistuneita Bitcoin-lompakon hallintaohjelmistoja, kuten Sparrow tai Liana, kuin Ledger Livea. Vaikka Ledger valmistaa erinomaisia laitteistolompakoita, jotka sisältävät nopeasti uusimmat Bitcoin-ominaisuudet, niiden ohjelmistoja ei välttämättä ole mukautettu bitcoin-käyttäjien erityistarpeisiin. Ledger Live sisältääkin monia altcoineille suunniteltuja ominaisuuksia, kun taas Bitcoin-lompakon hallintaan tarkoitetut vaihtoehdot ovat rajalliset. Sparrow'n ja Liana'n ongelmana (toistaiseksi) on kuitenkin se, että ne eivät salli Bitcoin-sovelluksen asentamista Ledgeriin.

Voit ohittaa Ledger Liven käytön Ledgerin alkukonfiguroinnin aikana käyttämällä Bacca-työkalua (tai "Ledger Installer"). Tämän ohjelmiston avulla voit asentaa ja päivittää Bitcoin-sovelluksen, tarkistaa Ledgerin aitouden ja jopa myöhemmin päivittää laitteen laiteohjelmiston. Baccan on luonut Antoine Poinsot (Darosior), Chaincode Labsin Bitcoin Core -kehittäjä, [Revaultin ja Lianan] (https://wizardsardine.com/) toinen perustaja ja Pythcoiner.

Tässä ohjeessa näytän, miten tätä työkalua käytetään, jotta voit luopua lopullisesti Ledger Live -ohjelmistosta ja silti nauttia Ledger-laitteista. Se toimii kaikissa laitteissa: Nano S Classic, Nano S Plus, Nano X, Flex ja Stax.

---
*Huomaa, että tämä työkalu on melko uusi, ja sen kehittäjät ilmoittavat, että se on vielä **testausvaiheessa**. He suosittelevat, että sitä käytetään vain testitarkoituksiin, eikä laitteeseen, joka on tarkoitettu oikean Bitcoin-lompakon isännöimiseen, vaikka se onkin mahdollista. Tältä osin suosittelen, että noudatat tämän työkalun kehittäjien suosituksia, jotka on määritelty [heidän GitHub-tietokantansa README-osassa](https://github.com/darosior/ledger_installer).*

---
## Edellytykset

Tarvitset tietokoneellasi kaksi työkalua Baccan käyttöön:


- Git ;
- Ruoste.

Jos olet jo asentanut ne, voit ohittaa tämän vaiheen.

**Linux:**

Linux-jakelussa Git on yleensä esiasennettuna. Voit tarkistaa, onko Git asennettu järjestelmääsi, kirjoittamalla terminaaliin seuraavan komennon :

```bash
git --version
```

Jos Git ei ole asennettuna järjestelmääsi, tässä on komento sen asentamiseksi Debian :

```bash
sudo apt install git
```

Lopuksi asenna Rust-kehitysympäristösi komennolla :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Windows:**

Asenna Git osoitteessa [projektin virallinen verkkosivusto](https://git-scm.com/). Lataa ohjelmisto ja noudata asennusohjeita.

![BACCA](assets/fr/01.webp)

Asenna Rust samalla tavalla [viralliselta verkkosivustolta](https://www.rust-lang.org/tools/install).

![BACCA](assets/fr/02.webp)

**MacOS:**

Jos Git ei ole vielä asennettu järjestelmääsi, avaa terminaali ja suorita seuraava komento asentaaksesi se:

```bash
git --version
```

Jos Gitiä ei ole asennettu järjestelmääsi, avautuu ikkuna, jossa sinulle tarjotaan Xcoden asentamista, joka sisältää Gitin. Jatka asennusta noudattamalla näytön ohjeita.

Asenna Rust suorittamalla seuraava komento:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Bacca asennus

Avaa terminaali ja siirry kansioon, johon haluat tallentaa ohjelmiston, ja suorita seuraava komento:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Siirry ohjelmistohakemistoon:

```bash
cd ledger_installer
```

Käytä sitten Cargoa projektin kääntämiseen ja Baccan graafisen käyttöliittymän suorittamiseen:

```bash
cargo run -p ledger_manager_gui
```

Sinulla on nyt pääsy ohjelmiston käyttöliittymään.

![BACCA](assets/fr/03.webp)

## Kirjanpidon määrittäminen

Jos Ledger on uusi, varmista ennen aloittamista, että olet määrittänyt PIN-koodin ja tallentanut palautuslausekkeen. Et tarvitse Ledger Liveä näihin alkuvaiheisiin. Kytke Ledgeriin virta USB-kaapelilla. Jos et ole varma, miten edetä näissä kahdessa vaiheessa, voit tutustua malliasi koskevan ohjeen alkuun:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a


## Baccan käyttäminen

Liitä Ledger tietokoneeseen ja avaa sen lukitus asettamallasi PIN-koodilla. Baccan pitäisi tunnistaa Ledger automaattisesti.

![BACCA](assets/fr/04.webp)

Vahvista pääkirjan aitous napsauttamalla "*Tarkista*"-painiketta. Sinun on hyväksyttävä yhteys Ledger-laitteessasi jatkaaksesi.

![BACCA](assets/fr/05.webp)

Bacca ilmoittaa sitten, onko Ledgerisi aito. Jos se ei ole aito, se tarkoittaa, että laite on vaarannettu tai että se on väärennös. Tässä tapauksessa lopeta sen käyttö välittömästi.

![BACCA](assets/fr/06.webp)

Valikossa "*Sovellukset*" voit tarkastella luetteloa Ledgeriin jo asennetuista sovelluksista.

![BACCA](assets/fr/07.webp)

Asenna Bitcoin-sovellus napsauttamalla "*Asenna*" ja hyväksy sitten asennus Ledgeriin.

![BACCA](assets/fr/08.webp)

Sovellus on hyvin asennettu.

![BACCA](assets/fr/09.webp)

Jos sinulla ei ole asennettuna Bitcoin-sovelluksen uusinta versiota, Bacca näyttää "*Update*"-painikkeen "*Latest*"-merkin sijasta. Päivitä sovellus yksinkertaisesti napsauttamalla tätä painiketta.

![BACCA](assets/fr/10.webp)

Nyt kun Ledger on konfiguroitu oikein Bitcoin-sovelluksen uusimman version kanssa, olet valmis tuomaan ja käyttämään lompakkoasi hallintaohjelmistoissa, kuten Sparrow tai Liana, ilman, että sinun tarvitsee käydä läpi Ledger Live!

Jos löysit tämän ohjeen hyödylliseksi, olisin kiitollinen, jos jättäisit vihreän peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos paljon!

Suosittelen myös tutustumaan tähän GnuPG:tä käsittelevään oppaaseen, jossa kerrotaan, miten tarkistat ohjelmiston eheyden ja aitouden ennen sen asentamista. Tämä on tärkeä käytäntö erityisesti silloin, kun asennat salkunhallintaohjelmistoja, kuten Liana tai Sparrow :


https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

