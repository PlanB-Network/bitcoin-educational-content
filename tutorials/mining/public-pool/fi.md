---
name: Julkinen Allas
description: Johdanto Julkiseen Altaaseen
---

![signup](assets/cover.webp)

**Julkinen Allas** ei ole mikä tahansa allas; se on myös tunnettu nimellä **Solo Allas**. Jos louhijasi onnistuu louhimaan lohkon, saat koko lohkopalkkion, jota ei jaeta muiden altaan osallistujien tai itse altaan kanssa.

**Julkinen Allas** tarjoaa ainoastaan **lohkomallin** louhijallesi, jotta se voi suorittaa työnsä, ilman että sinun tarvitsee omistaa **Bitcoin-nodeta** ja ohjelmistoa, joka kommunikoi louhijasi kanssa. Koska et yhdistä laskentatehoasi muiden osallistujien kanssa, onnistumismahdollisuutesi louhia lohko ovat selvästi matalat, mikä tekee siitä eräänlaisen lottojärjestelmän, jossa joskus onnekas henkilö voittaa päävoiton.

![signup](assets/1.webp)

**Julkisen Altaan** **Dashboardilla** on silti joitakin tilastoja, kuten altaan **Kokonaislaskentateho** sekä erityyppisten louhijoiden jakautuminen, jotka ovat yhteydessä altaaseen.

![signup](assets/2.webp)

Ensimmäisillä riveillä näemme **Bitaxe**n, jossa on 1323 **Bitaxe**a yhteensä 649TH/s. **Bitaxe** on **avoin lähdekoodi** -projekti, joka mahdollistaa sirun yksinkertaisen uudelleenkäytön **ASICista** kuten **Antminer S19** avoimen lähdekoodin elektroniikkalevyllä, jotta voidaan tehdä erittäin pieni louhija, 0.5TH/s 15W:lla. Tätä louhijaa käytämme esimerkkinä tässä oppaassa.

## Lisää **Työntekijä** 👷‍♂️

![signup](assets/cover.webp)

Sivun yläosasta voit kopioida altaan osoitteen **stratum+tcp://public-pool.io:21496**.

Seuraavaksi **käyttäjä**-kenttään, syötä **Bitcoin**-osoite, joka sinulla on.

Jos sinulla on useita louhijoita, voit syöttää kaikille niille saman osoitteen, jotta niiden **laskentatehot** yhdistyvät ja näkyvät yhtenä louhijana. Voit myös erottaa ne antamalla kullekin erillisen nimen. Tee tämä yksinkertaisesti lisäämällä **.työntekijännimi** **Bitcoin**-osoitteen perään.

Lopuksi **salasana**-kenttään käytä **‘x’**.

Esimerkki: Jos **Bitcoin**-osoitteesi on **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** ja haluat nimetä louhijasi **« Brrrr »**, sinun tulisi syöttää seuraavat tiedot louhijasi käyttöliittymään:

- **URL** : stratum+tcp://public-pool.io:21496
- **KÄYTTÄJÄ** : **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Salasana** : **‘x’**
Jos louhijasi on **Bitaxe**, kentät ovat hieman erilaiset, mutta tiedot pysyvät samoina:
- **URL**: public-pool.io (tässä sinun täytyy poistaa alkuosa **‘stratum+tcp://’** ja loppuosa **‘:21496’**, jotka ilmoitetaan porttikentässä)
- **Portti**: 21496
- **Käyttäjä**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Salasana**: **‘x’**
![signup](assets/3.webp)
Muutaman minuutin kuluttua louhinnan aloittamisesta, voit nähdä tietosi **Public Pool** -sivustolla etsimällä osoitettasi.

## Dashboard

![signup](assets/4.webp)

Kun olet yhdistänyt **Public Pool**iin, pääset käsiksi **Dashboardiisi** etsimällä **Bitcoin**-osoitettasi, jonka syötit **Käyttäjä**-kenttään. Tässä tapauksessa se on **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

**Dashboardilla** näytetään erilaisia tietoja sekä datastasi että verkosta.

![signup](assets/5.webp)

Sinulla on **Network Hash Rate**, joka vastaa **Bitcoin**-verkon kokonaistyötehoa.

**Network Difficulty** osoittaa vaikeustason, joka on saavutettava lohkon vahvistamiseksi.

Ja **Your Best Difficulty** on korkein vaikeustaso, jonka olet saavuttanut. Jos, onnenkantamoisella 🍀, saavutat verkon vaikeustason, voitat koko lohkopalkkion... 100 lohkon jälkeen. Sinun täytyisi odottaa 100 lohkoa ennen kuin voisit käyttää ne.

Sinulla on myös **Block Height**, joka on viimeksi louhitun lohkon numero sekä sen paino ilmaistuna WU:ssa, maksimin ollessa 4,000,000.

Alla voit nähdä kaikkien laitteidesi tilastot erikseen, jos olet antanut niille er distinct nimen lisäämällä **.name** **Bitcoin**-osoitteesi perään **Käyttäjä**-kentässä.