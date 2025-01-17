---
name: Seed Signer

description: Seed signerin asennus
---

![cover](assets/cover.webp)

## Materiaali:

1. Raspberry Pi Zero (versio 1.3)

Raspberry Pi Zero

Täysin ilmaraollisen ratkaisun varmistamiseksi, varmista että käytät versiota 1.3, jossa ei ole WiFiä tai Bluetoothia, mutta mikä tahansa Raspberry Pi 2/3/4 tai Zero malli toimii.

Huom: Raspberry Pi:t eivät yleensä tule kiinnitetyillä nastoilla; nastat täytyy joko juottaa kiinni, tai vaihtoehtoisesti voidaan käyttää jotain, jota kutsutaan "GPIO Hammeriksi".
GPIO Hammer

Jos juottamisesi ei ole aivan huippuluokkaa, tai sinulla ei vielä ole juotoskolvia, voit käyttää "GPIO Hammeria" vaihtoehtona juottamiselle.

2. Chapeau LCD WaveShare 1,3 tuumaa 240 × 240 pikselin näytöllä

WaveShare LCD Hat

Waveshare 1.3″ 240×240 pxl LCD

Huom: Valitse Waveshare-näyttö huolellisesti; varmista, että ostat mallin, jossa on 240×240 pikselin resoluutio.
lisätietoja

3. Pi Zero -yhteensopiva kameramoduuli

Raspberry Pi Camera

Aokin / AuviPal 5MP 1080p OV5647 Sensori Videokameramoduuli; muut merkit, joissa on OV5647 sensorimoduuli, toimivat myös, mutta eivät välttämättä ole yhteensopivia Orange Pill -kotelon kanssa.

Huom: Tarvitset kameran nauhakaapelin, joka on nimenomaan yhteensopiva Raspberry Pi Zeron kanssa.

4. MicroSD-kortti, jossa on vähintään 4 Gt kapasiteettia

laajat resurssit: https://seedsigner.com/explainers/

## Ohjelmisto:

Ohjelmiston asennus

1. Lataa uusin “seedsigner_x_x_x.img.zip” tiedosto
   uusin julkaisu

2. Pura “seedsigner_x_x_x.img.zip” tiedosto

3. Käytä Balena Etcheria tai vastaavaa työkalua kirjoittaaksesi puretun .img kuvatiedoston microsd-kortille
   BALENA ETCHER

4. Asenna microsd-kortti SeedSigneriin.
   SeedSigner GPG Julkinen Avain
   seedsigner_pubkey.gpg

## Video-opas

_opas otettu Southerbitcoinerilta, luonut Cole_

### Videoiden kokoelma, joka kattaa SeedSignerin: avoimen lähdekoodin, DIY Hardware Wallet/Signing laitteen

![image](assets/1.webp)

SeedSigner on Bitcoin Signing Device, jonka voit rakentaa alusta alkaen. Kuulostaa vaikealta, mutta tämän 4 osan sarjan pitäisi auttaa sinua :) Suosittelen, että katsot ensin osan 1 ja 2, sitten päätät haluatko käyttää desktopia (katso osa 3) tai mobiililaitetta (katso osa 4).

Kaikki mitä tarvitset tietää on alla. Muita hyödyllisiä linkkejä sisältävät SeedSignerin verkkosivusto, heidän Github, heidän Keybase, uusin julkaisu ja laitteistovaatimukset.

### Osa 1: Kuinka rakentaa SeedSigner:

Tässä videossa näytän, kuinka ladata ja varmistaa SeedSigner-ohjelmisto, mitä osia tarvitaan, ja kuinka koota SeedSignerisi.

![video](https://youtu.be/mGmNKYOXtxY)

### Osa 2: SeedSignerin testaaminen
Ennen kuin käytin SeedSigneriani, tein muutamia testejä varmistaakseni, ettei se tehnyt mitään pahantahtoista. Ajattelin jakaa tämänkin vaiheen. Tässä on, miten voit varmistaa, että SeedSigner vie oikean lompakon (xpub), miten voit tarkistaa SeedSignerin nopanheittojen matematiikan, ja miten voit tarkistaa SeedSignerin bip-85 lapsisiemenet.
![video](https://youtu.be/34W1IyTyXZE)

### Osa 3: Kuinka käyttää SeedSigneria Sparrow Walletin kanssa (desktop)

SeedSigner pystyy generoimaan siemeniä ja allekirjoittamaan bitcoin-siirtoja. Mutta yksinään se ei pysty rakentamaan siirtoja. Sinun on käytettävä lompakon "koordinaattoria" SeedSignerin kanssa. Näin käytät Sparrow Walletia SeedSignerin kanssa:

![video](https://youtu.be/IQb8dh-VTOg)

Osa 4: Kuinka käyttää SeedSigneria Blue Walletin kanssa (mobile)

SeedSigner pystyy generoimaan siemeniä ja allekirjoittamaan bitcoin-siirtoja. Mutta yksinään se ei pysty luomaan siirtoja. Sinun on käytettävä lompakon "koordinaattoria" SeedSignerin kanssa. Näin käytät Blue Walletia SeedSignerin kanssa:

![video](https://youtu.be/x0Ee35Ct0r4)

Nämä ovat kaikki SeedSigner-oppaat toistaiseksi! Kerro minulle, jos luulet, että jotain puuttuu. Nämä ovat listallani mahdollisiksi videoiksi:

> SeedSignerin kokonaisarvostelu. Onko se hyvä valinta allekirjoituslaitteeksi? Hyvät/huonot puolet?

> Kuinka käyttää Bip-85:ttä SeedSignerin kanssa
> Kuinka olla setä Jim SeedSignerin kanssa

Piditkö näitä hyödyllisinä? Harkitse tipin lähettämistä tulevien videoiden rahoittamiseksi:
https://www.southernbitcoiner.com/donate/