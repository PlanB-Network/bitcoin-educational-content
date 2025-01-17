---
name: Public Pool
description: Johdanto Public Pooliin
---

![signup](assets/cover.webp)

**Public Pool** ei ole mikä tahansa allas; se on myös tunnettu nimellä **Solo Pool**. Jos louhijasi onnistuu louhimaan lohkon, keräät koko lohkopalkkion, jota ei jaeta muiden altaan osallistujien tai itse altaan kanssa.

**Public Pool** tarjoaa ainoastaan **lohkomallin** louhijallesi, jotta se voi suorittaa tehtävänsä ilman, että sinun tarvitsee omistaa **Bitcoin-nodeta** ja ohjelmistoa, joka kommunikoi louhijasi kanssa. Koska et yhdistä laskentatehoasi muiden osallistujien kanssa, mahdollisuutesi onnistuneesti louhia lohko ovat selvästi matalat, muistuttaen jonkin verran lottojärjestelmää, jossa joskus onnekas yksilö voittaa päävoiton.

![signup](assets/1.webp)

**Public Poolin** **Dashboardilla** näet silti joitakin tilastoja, kuten altaan **kokonaislaskentatehon** sekä erityyppisten louhijoiden jakautumisen, jotka ovat yhteydessä altaaseen.

![signup](assets/2.webp)

Ensimmäisillä riveillä näemme **Bitaxen** 1323 **Bitaxe** yhteydessä, yhteensä 649TH/s. **Bitaxe** on **avoin lähdekoodi** -projekti, joka mahdollistaa sirun yksinkertaisen uudelleenkäytön **ASICista**, kuten **Antminer S19**, avoimen lähdekoodin elektroniikkalevyllä pienen louhijan tekemiseksi, 0.5TH/s 15W:lla. Tätä louhijaa käytämme esimerkkinä tässä oppaassa.

## Työntekijän lisääminen 👷‍♂️

![signup](assets/cover.webp)

Sivun yläosasta voit kopioida altaan osoitteen **stratum+tcp://public-pool.io:21496**.

Seuraavaksi **käyttäjä**-kenttään, syötä **Bitcoin**-osoite, joka sinulla on.

Jos sinulla on useita louhijoita, voit syöttää kaikille niille saman osoitteen, jotta niiden **laskentatehot** yhdistyvät ja näkyvät yhtenä louhijana. Voit myös erottaa ne antamalla kullekin erillisen nimen. Tee tämä yksinkertaisesti lisäämällä **.workername** **Bitcoin**-osoitteen perään.

Lopuksi **salasana**-kenttään käytä **‘x’**.

Esimerkki: Jos **Bitcoin**-osoitteesi on **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’** ja haluat nimetä louhijasi **« Brrrr »**, syöttäisit louhijasi käyttöliittymään seuraavat tiedot:

- **URL**: stratum+tcp://public-pool.io:21496
- **KÄYTTÄJÄ**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Salasana**: **‘x’**
Jos louhijasi on **Bitaxe**, kentät ovat hieman erilaiset, mutta tiedot pysyvät samoina:
- **URL**: public-pool.io (tässä sinun täytyy poistaa alkuosa **‘stratum+tcp://’** ja loppuosa **‘:21496’**, jotka ilmoitetaan porttikentässä)
- **Portti**: 21496
- **Käyttäjä**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- **Salasana**: **‘x’**

![signup](assets/3.webp)
Muutaman minuutin kuluttua louhinnan aloittamisesta, voit nähdä tietosi **Public Pool** -sivustolla etsimällä osoitettasi.

## Koontinäyttö

![signup](assets/4.webp)

Kun olet yhdistänyt **Public Pool**iin, pääset käsiksi **Koontinäyttöösi** etsimällä **Bitcoin**-osoitettasi, jonka syötit **Käyttäjä**-kenttään. Tässä tapauksessa se on **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv’**.

**Koontinäytöllä** näytetään erilaisia tietoja sekä datastasi että verkosta.

![signup](assets/5.webp)

Sinulla on **Verkon Hash Rate**, joka vastaa **Bitcoin**-verkon kokonaistyötehoa.

**Verkon Vaikeusaste** osoittaa vaikeustason, joka on saavutettava lohkon vahvistamiseksi.

Ja **Paras Vaikeusasteesi** on korkein vaikeusaste, jonka olet saavuttanut. Jos sattumalta 🍀 saavutat verkon vaikeusasteen, voitat koko lohkopalkkion... 100 lohkon jälkeen. Sinun täytyisi odottaa 100 lohkoa ennen kuin voisit käyttää ne.

Sinulla on myös **Lohkon Korkeus**, joka on viimeksi louhitun lohkon numero sekä sen paino ilmaistuna WU:ssa, maksimin ollessa 4,000,000.

Alla voit nähdä kaikkien laitteidesi tilastot erikseen, jos olet antanut niille er distinct nimen lisäämällä **.name** **Bitcoin**-osoitteesi perään **Käyttäjä**-kentässä.