---
name: UTXO:n merkitseminen
description: Kuinka merkitä UTXO:si oikein?
---
![cover](assets/cover.webp)

Tässä oppaassa opit kaiken tarvittavan UTXO:iden merkitsemisestä Bitcoin-lompakossasi sekä kolikoiden hallinnasta. Aloita teoreettisesta osiosta ymmärtääksesi nämä käsitteet kunnolla, ennen kuin siirryt käytännön osaan, jossa tutkimme, kuinka konkreettisesti käyttää merkintöjä pääasiallisessa Bitcoin-lompakko-ohjelmistossa.

## Mikä on UTXO:n merkitseminen?
"Merkitseminen" on tekniikka, joka sisältää annotaation tai merkinnän liittämisen tiettyyn UTXO:on Bitcoin-lompakossa. Nämä annotaatiot tallennetaan paikallisesti lompakko-ohjelmiston toimesta eivätkä ne koskaan siirry Bitcoin-verkon yli. Merkitseminen on siis henkilökohtaisen hallinnan työkalu.

Esimerkiksi, jos saan UTXO:n P2P-transaktiosta Bisq:n kautta Charlesilta, voisin merkitä sen `Bisq P2P Osto Charles`.

Merkitseminen mahdollistaa UTXO:n alkuperän tai tarkoitetun määränpään muistamisen, mikä yksinkertaistaa varojen hallintaa ja optimoi käyttäjän yksityisyyttä. Merkitseminen muuttuu vieläkin merkityksellisemmäksi, kun sitä yhdistetään "kolikoiden hallinnan" toiminnallisuuteen. Kolikoiden hallinta on vaihtoehto hyvissä Bitcoin-lompakoissa, joka antaa käyttäjälle mahdollisuuden manuaalisesti valita, mitkä tarkat UTXO:t käytetään syötteinä luotaessa transaktiota.

Lompakon käyttäminen, jossa on kolikoiden hallinta yhdessä UTXO:n merkitsemisen kanssa, mahdollistaa käyttäjien tarkasti erottaa ja valita UTXO:t transaktioihinsa, välttäen näin UTXO:iden yhdistämisen eri lähteistä. Tämä käytäntö vähentää riskejä, jotka liittyvät Common Input Ownership Heuristic (CIOH) -oletukseen, joka ehdottaa transaktion syötteiden yhteisomistusta, mikä voi vaarantaa käyttäjän yksityisyyden.

Palatakseni esimerkkiini KYC-vapaasta UTXO:sta Bisq:sta; haluan välttää sen yhdistämisen UTXO:on, joka tulee esimerkiksi säännellyltä vaihtoalustalta, joka tuntee henkilöllisyyteni. Asettamalla erillisen merkinnän KYC-vapaalle UTXO:lleni ja KYC UTXO:lleni, pystyn helposti tunnistamaan, minkä UTXO:n kulutan syötteenä tyydyttääkseni kulutuksen, käyttäen kolikoiden hallinnan toiminnallisuutta.

## Kuinka merkitä UTXO:si oikein?
Ei ole olemassa yleispätevää menetelmää UTXO:iden merkitsemiseen, joka sopisi kaikille. Sinun tehtäväsi on määritellä merkintäjärjestelmä, jotta voit helposti löytää tiesi lompakossasi.
Merkitsemisen keskeinen kriteeri on UTXO:n lähde. Sinun tulisi yksinkertaisesti ilmoittaa, miten tämä kolikko saapui lompakkoosi. Onko se vaihtoalustalta? Asiakkaan maksama lasku? Vertaisverkkovaihto? Vai edustako se vaihtorahaa ostoksesta? Näin ollen, voisit määritellä:
- `Nosto Exchange.com`;
- `Maksu Asiakas David`;
- `P2P Osto Charles`;
- `Vaihtoraha sohvaostoksesta`.
![labelling](assets/en/1.webp)
UTXO-hallintasi tarkentamiseksi ja lompakkosi varojen erottelustrategioiden noudattamiseksi, voisit rikastaa merkintöjäsi lisäindikaattorilla, joka heijastaa näitä erotteluja. Jos lompakkosi sisältää kaksi UTXO-kategoriaa, joita et halua sekoittaa, voisit integroida merkinnän merkintöihisi erottaaksesi nämä ryhmät selkeästi.

Nämä erottelumerkit riippuvat omista kriteereistäsi, kuten ero KYC UTXO:n (tunnistaa henkilöllisyytesi) ja KYC-vapaan (anonyymi) tai ammatillisten ja henkilökohtaisten varojen välillä. Ottaen aiemmin mainitut merkintäesimerkit, tämä voitaisiin kääntää seuraavasti:
- `KYC - Nosto Exchange.com`;
- `KYC - Maksu Asiakas David`;
- `EI KYC - P2P Osto Charles`;
- `EI KYC - Vaihtoraha sohvaostoksesta`.
![merkintä](assets/en/2.webp)Muista, että hyvä merkintä on sellainen, jonka ymmärrät tarvittaessa. Jos Bitcoin-lompakkosi on pääasiassa säästöjä varten, voi olla, että merkinnät ovat hyödyllisiä sinulle vasta vuosikymmenten päästä. Varmista siis, että ne ovat selkeitä, tarkkoja ja kattavia.

On myös suositeltavaa säilyttää kolikon merkintä läpi kaikkien transaktioiden. Esimerkiksi tehdessäsi KYC-vapaata UTXO-konsolidaatiota, varmista, että merkitset tuloksena olevan UTXOn ei pelkästään `konsolidaatio`, vaan nimenomaan `KYC-vapaa konsolidaatio`, jotta kolikon alkuperästä säilyy selkeä jälki.

Lopuksi, merkinnän päiväystä ei ole pakko lisätä. Useimmat lompakko-ohjelmistot näyttävät jo transaktion päivämäärän, ja tämän tiedon voi aina hakea lohkoketjun tutkijasta sen TXID:n avulla.

## Opas: Merkintöjen tekeminen Specter Desktopissa

Yhdistä ja avaa lompakkosi Specter Desktopissa, sitten valitse `Osoitteet`-välilehti.

![merkintä](assets/notext/3.webp)
Täällä näet kaikkien osoitteidesi luettelon sekä niissä lukittuna olevat bitcoinit. Oletuksena osoitteet tunnistetaan niiden indeksin perusteella `Merkintä`-sarakkeessa. Merkinnän muuttamiseksi, klikkaa sitä, syötä haluamasi merkintä ja vahvista klikkaamalla sinistä ikonia.
![merkintä](assets/notext/4.webp)

Merkintäsi ilmestyy sitten osoitteidesi luetteloon.

![merkintä](assets/notext/5.webp)

Voit myös antaa merkinnän etukäteen, kun jaat vastaanotto-osoitteesi lähettäjälle. Tehdäksesi tämän, `Vastaanota`-välilehdellä, merkitse merkintäsi omistetussa kentässä.

![merkintä](assets/notext/6.webp)

## Opas: Merkintöjen tekeminen Electrumissa

Electrum-lompakossa, kirjauduttuasi lompakkoosi, klikkaa transaktiota, jolle haluat antaa merkinnän `Historia`-välilehdeltä.

![merkintä](assets/notext/7.webp)

Uusi ikkuna avautuu. Klikkaa `Kuvaus`-kenttää ja kirjoita merkintäsi.

![merkintä](assets/notext/8.webp)

Kun merkintä on syötetty, voit sulkea tämän ikkunan.

![merkintä](assets/notext/9.webp)

Merkintäsi on onnistuneesti tallennettu. Löydät sen `Kuvaus`-välilehdeltä.

![merkintä](assets/notext/10.webp)

`Kolikot`-välilehdellä, josta voit suorittaa kolikoiden hallintaa, merkintäsi löytyy `Merkintä`-sarakkeesta.

![merkintä](assets/notext/11.webp)

## Opas: Merkintöjen tekeminen Green Walletissa

Green Wallet -sovelluksessa, pääset lompakkoosi ja valitse transaktio, jolle haluat antaa merkinnän. Sitten, klikkaa pientä kynäikonia merkitäksesi merkintäsi.

![merkintä](assets/notext/12.webp)

Kirjoita merkintäsi, sitten klikkaa vihreää `Tallenna`-painiketta.

![merkintä](assets/notext/13.webp)

Löydät merkintäsi sekä transaktiosi yksityiskohdista että lompakkosi kojelaudalta.

![merkintä](assets/notext/14.webp)

## Opas: Merkintöjen tekeminen Samourai Walletissa

Samourai Walletissa on erilaisia menetelmiä, joilla voit antaa merkinnän transaktiolle. Ensimmäiseksi, avaa lompakkosi ja valitse transaktio, jolle haluat lisätä merkinnän. Paina sitten `Lisää`-painiketta, joka sijaitsee `Muistiinpanot`-laatikon vieressä.

![merkintä](assets/notext/15.webp)
Kirjoita merkintäsi ja vahvista klikkaamalla sinistä `Lisää`-painiketta.
![merkintä](assets/notext/16.webp)

Löydät merkintäsi tapahtumasi tiedoista, mutta myös lompakkosi kojelaudalta.

![merkintä](assets/notext/17.webp)
Toista menetelmää varten, klikkaa kolmea pientä pistettä näytön oikeasta yläkulmasta, sitten `Näytä käyttämättömät tapahtuman tulosteet` -valikkoa.
![merkintä](assets/notext/18.webp)

Täältä löydät kattavan listan kaikista lompakossasi olevista UTXOista. Näytetty lista koskee talletustiliäni, mutta tämä toimenpide voidaan toistaa Whirlpool-tilien osalta navigoimalla omistetusta valikosta.

Klikkaa sitten UTXOa, jonka haluat merkitä, seurattuna `Lisää`-painikkeesta.

![merkintä](assets/notext/19.webp)

Kirjoita merkintäsi ja vahvista klikkaamalla sinistä `Lisää`-painiketta. Löydät sitten merkintäsi sekä tapahtumasi tiedoista että lompakkosi kojelaudalta.

![merkintä](assets/notext/20.webp)

## Opas: Merkintöjen tekeminen Sparrow Wallet -lompakossa

Sparrow Wallet -ohjelmistolla on mahdollista tehdä merkintöjä useilla tavoilla. Yksinkertaisin menetelmä on lisätä merkintä etukäteen, kun ilmoitat vastaanotto-osoitteen lähettäjälle. Tätä varten `Vastaanota`-valikossa, klikkaa `Merkintä`-kenttää ja kirjoita valitsemasi merkintä. Tämä säilytetään ja on pääsykelpoinen ohjelmistossa heti, kun bitcoineja vastaanotetaan osoitteeseen.

![merkintä](assets/notext/21.webp)

Jos unohdit merkitä osoitteesi vastaanoton yhteydessä, voit silti lisätä merkinnän myöhemmin `Tapahtumat`-valikon kautta. Klikkaa vain tapahtumaasi `Merkintä`-sarakkeessa, sitten kirjoita haluamasi merkintä.

![merkintä](assets/notext/22.webp)

Sinulla on myös mahdollisuus lisätä tai muokata merkintöjäsi `Osoitteet`-valikon kautta.

![merkintä](assets/notext/23.webp)

Lopuksi, voit tarkastella merkintöjäsi `UTXO:t`-valikossa. Sparrow Wallet lisää automaattisesti sulkuihin merkintäsi taakse tulosteen luonteen, mikä auttaa erottamaan vaihtorahasta saadut UTXOt suoraan vastaanotetuista.

![merkintä](assets/notext/24.webp)