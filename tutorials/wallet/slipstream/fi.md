---
name: Slipstream
description: Allekirjoitetun transaktion lähettäminen suoraan louhijalle Slipstreamin avulla, lähettämättä sitä Bitcoin-verkkoon
---

![cover](assets/cover.webp)

Kun allekirjoitat transaktion, se lähetetään yleensä automaattisesti verkon kaikille Bitcoin-solmuille. Sen jälkeen se jää odottamaan louhimista.

Niin kauan kuin se ei kuitenkaan ole lohkossa, hyökkääjä, joka on saanut haltuunsa yksityisen avaimesi, voisi korvata sen ja varastaa varat. Näin on tyypillisesti silloin, kun käytät ColdCard-laitteistolompakkoa.

Louhintayhtiö MARAn Slipstream-työkalulla voit ohittaa transaktion lähettämisen verkkoon: se lähetetään suoraan (ja ainoastaan) louhijalle, jolloin se pysyy yksityisenä eikä paljastu verkossa. Transaktion louhiminen kestää tällöin todennäköisesti pidempään, mutta se on suojassa korvaushyökkäykseltä.

Alla tarjoamme oppaan, jonka avulla [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04)-käyttäjät sekä [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)-lompakon käyttäjät voivat käyttää louhija MARAn Slipstream-työkalua [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) -sivun kautta.

⚠️ **Varoitus**: tämä työkalu on tarkoitettu vain tietyille profiileille, pääasiassa Liana-lompakoille, miniscript-lompakoille ja joillekin multisig-tyypeille. Wizardsardine **kehottaa nimenomaisesti olemaan käyttämättä** sitä lompakoissa, joiden varat ovat jo kriittisessä varkausvaarassa, esimerkiksi niissä, joiden palautuslauseke on luotu satunnaislukugeneraattorin haavoittuvuudelle alttiilla ColdCard-laitteella. Tällaisessa tilanteessa kilpajuoksu hyökkääjää vastaan ratkeaa sekunneissa, ja yhdelle louhijalle lähetetyn transaktion vahvistuminen kestää paljon kauemmin kuin normaalisti verkkoon lähetetyn. Jos tämä koskee sinua, lue ensin oma oppaamme aiheesta:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Liana-käyttäjille

Lianaa ylläpitää Wizardsardine, joka julkaisee [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) -sivun, joten polku on suora: viet yksinkertaisesti allekirjoitetun PSBT-tiedoston sen sijaan, että lähettäisit sen verkkoon.

*Edellytys: sinulla on varoja Liana-lompakossasi.*

### Vaihe 1: Luo transaktiosi Lianalla

Rakenna transaktiosi tavalliseen tapaan lisäämällä siihen kohdeosoite, kuvaus ja summa (tässä lompakon suurin käytettävissä oleva määrä).

Siirtomaksutason asettaminen:

- valitse kolikot, jotka haluat kuluttaa, napsauttamalla vasemmassa alakulmassa olevaa pientä ruutua kohdassa "Coins selection";
- syötä sitten siirtomaksutaso. Muista asettaa siirtomaksut paljon ehdotettua tasoa korkeammiksi, kuten tällä sivulla kuvataan: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Napsauta lopuksi "Next".

![Transaktion rakentaminen Lianassa](assets/fr/01.webp)

### Vaihe 2: Tarkista transaktiosi tiedot

Tarkista transaktiosi tiedot ennen kuin napsautat "Sign"; erityisesti:

- lähetetty summa;
- siirtomaksuihin varattujen satoshien määrä;
- mutta ennen kaikkea osoite, johon lähetät varat (muista tarkistaa osoitteen 5/6 ensimmäistä merkkiä, 5/6 viimeistä merkkiä sekä 5/6 merkkiä osoitteen keskeltä välttääksesi "address poisoning" -hyökkäykset).

![Transaktion tietojen tarkistaminen](assets/fr/02.webp)

### Vaihe 3: Valitse allekirjoittavat lompakot

Valitse seuraavaksi ohjelmisto- ja/tai laitteistolompakot, joilla sinun on allekirjoitettava transaktiosi. Pieni muistutus: 2-of-2-multisig-lompakon tapauksessa tarvitset 2 allekirjoitusta 2:sta.

### Vaihe 4: Vie transaktiosi PSBT-tiedosto

Bitcoin-transaktio on nyt allekirjoitettu asianmukaisilla avaimilla. Älä napsauta "Broadcast", sillä muuten se jaetaan koko verkolle ja, jos käytät ColdCard-laitteistolompakkoa, transaktiosi paljastuu julkisesti ja varasi ovat vaarassa.

Voit nyt napsauttaa "Export" ja tallentaa PSBT-tiedoston paikallisesti tietokoneellesi.

![PSBT-tiedoston vieminen Lianasta](assets/fr/03.webp)

### Vaihe 5: Lähetä transaktio louhijalle outofband.wizardsardine.com-sivun kautta

Nyt vuorossa ovat viimeiset vaiheet. Transaktion lähettämiseksi louhijalle sinun tarvitsee vain ottaa PSBT-tiedosto ja vetää ja pudottaa se sille varatulle alueelle.

![PSBT-tiedoston pudottaminen outofband.wizardsardine.com-sivulle](assets/fr/04.webp)

Transaktio näkyy tämän jälkeen alla olevan kuvan mukaisesti.

![Transaktio jonossa](assets/fr/05.webp)

### Vaihe 6: Lähetä transaktio Slipstreamin kautta

Lopuksi sinun tarvitsee vain napsauttaa "Send", jotta transaktio lähetetään MARAlle Slipstreamin kautta.

![Transaktion lähettäminen Slipstreamin kautta](assets/fr/06.webp)

Muutamassa sekunnissa transaktion tila muuttuu tilasta "Sending" tilaan "Accepted":

![Slipstreamin hyväksymä transaktio](assets/fr/07.webp)

Enää tarvitsee kopioida transaktion tunniste (TXID) ja liittää se [mempool.space](https://mempool.space/) -sivustolle, jotta voit seurata sen louhimista:

![TXID:n hakeminen mempool.space-sivustolta](assets/fr/08.webp)

Huomaa: transaktio näkyy tilassa "Transaction not found" siihen asti, kunnes louhija MARA louhii lohkon ja sisällyttää transaktiosi siihen. Tämä voi kestää useita kymmeniä minuutteja tai jopa tunteja, koska MARAn hallussa on vain noin 4,5 % Bitcoin-verkon hashratesta. Elokuun 4. päivänä 2026 tämä vastaa suunnilleen yhtä louhittua lohkoa 3 tunnin ja 45 minuutin välein.

## Muiden lompakoiden käyttäjille

Jos et käytä [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04)-lompakkoa mutta haluat silti käyttää työkalua, tässä on opas, jossa käytetään 2-of-2-multisig-lompakkoa. Tätä varten käytämme [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)-ohjelmistolompakkoa.

*Edellytys: sinulla on varoja Sparrow-lompakossasi.*

### Vaihe 1: Luo transaktiosi

Luo transaktio multisig-lompakossasi [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)-lompakolla. Muista asettaa siirtomaksut paljon ehdotettua tasoa korkeammiksi, kuten tällä sivulla kuvataan: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Kun olet luonut sen, napsauta "Create Transaction".

![Transaktion luominen Sparrow'ssa](assets/fr/09.webp)

### Vaihe 2: Viimeistele transaktiosi

Transaktion viimeistelemiseksi sinun on nyt allekirjoitettava se. Napsauta tätä varten "Finalize Transaction for Signing".

![Transaktion viimeistely allekirjoitusta varten](assets/fr/10.webp)

### Vaihe 3: Allekirjoita transaktiosi eri avaimillasi

Nyt on aika allekirjoittaa transaktio. Allekirjoita se yksinkertaisesti käyttämälläsi ohjelmisto- tai laitteistolompakolla (tai -lompakoilla).

![Transaktion allekirjoittaminen multisig-avaimilla](assets/fr/11.webp)

### Vaihe 4: Lataa allekirjoitettu transaktio äläkä lähetä sitä verkkoon

Bitcoin-transaktio on nyt allekirjoitettu 2-of-2-multisigimme molemmilla avaimilla. Älä napsauta "Broadcast Transaction", sillä muuten se jaetaan koko verkolle ja, jos käytät ColdCard-laitteistolompakkoa, transaktiosi paljastuu julkisesti ja varasi ovat vaarassa.

![Allekirjoitettu transaktio, valmis mutta ei verkkoon lähetetty](assets/fr/12.webp)

### Vaihe 5: Näytä allekirjoitetun transaktion skripti tai lataa PSBT-tiedosto

Näytä allekirjoitettu Bitcoin-transaktio napsauttamalla nyt "View Final Transaction". Voit sitten kopioida allekirjoitetun Bitcoin-transaktion skriptin:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Allekirjoitetun transaktion skriptin näyttäminen](assets/fr/13.webp)

Jos haluat ladata transaktiotiedoston, voit joko:

- napsauttaa "File" ja sitten "Save transaction…";
- tai napsauttaa oikeassa alakulmassa olevaa verkkoyhteyspainiketta (keltainen painike) ja napsauttaa sitten "Save Final Transaction".

Transaktio tallennetaan tämän jälkeen paikallisesti tietokoneellesi.

![Lopullisen transaktion tallentaminen paikallisesti](assets/fr/14.webp)

### Vaihe 6: Lähetä transaktio louhijalle outofband.wizardsardine.com-sivun kautta

Nyt vuorossa ovat viimeiset vaiheet. Transaktion lähettämiseksi louhijalle sinun tarvitsee vain:

- siirtyä sivulle [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- liittää edellisessä vaiheessa kopioitu allekirjoitetun transaktion skripti ja napsauttaa sitten alla olevaa "ADD TO QUEUE" -painiketta;

![Transaktion skriptin liittäminen työkaluun](assets/fr/15.webp)

- tai ottaa tiedosto ja vetää ja pudottaa se sille varatulle alueelle.

![Transaktiotiedoston pudottaminen työkaluun](assets/fr/16.webp)

Transaktio näkyy tämän jälkeen alla olevan kuvan mukaisesti.

![Transaktio jonossa](assets/fr/17.webp)

Jos viesti kertoo, että transaktiosi syötteiden satoshien kokonaismäärä on tuntematon (ja että siirtomaksujen satoshimäärää ei siksi voida laskea), sinun tarvitsee vain syöttää syötteiden satoshien kokonaismäärä käsin. Löydät sen napsauttamalla transaktiosi näkymää Sparrow'ssa, kaavion keskeltä:

![Syötteiden kokonaismäärä Sparrow'ssa](assets/fr/18.webp)

Syötä tämä määrä (esimerkissämme 15 904 satia) sitten [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) -työkaluun:

![Syötteiden kokonaismäärän syöttäminen käsin](assets/fr/19.webp)

Tarkista lopuksi, että siirtomaksutaso on oikein.

### Vaihe 7: Lähetä transaktio Slipstreamin kautta

Lopuksi sinun tarvitsee vain napsauttaa "Send", jotta transaktio lähetetään MARAlle Slipstreamin kautta.

![Transaktion lähettäminen Slipstreamin kautta](assets/fr/20.webp)

Muutamassa sekunnissa transaktion tila muuttuu tilasta "Sending" tilaan "Accepted":

![Slipstreamin hyväksymä transaktio](assets/fr/21.webp)

Enää tarvitsee kopioida transaktion tunniste (TXID) ja liittää se [mempool.space](https://mempool.space/) -sivustolle, jotta voit seurata sen louhimista:

![TXID:n hakeminen mempool.space-sivustolta](assets/fr/22.webp)

Huomaa: transaktio näkyy tilassa "Transaction not found" siihen asti, kunnes louhija MARA louhii lohkon ja sisällyttää transaktiosi siihen. Tämä voi kestää useita kymmeniä minuutteja tai jopa tunteja, koska MARAn hallussa on vain noin 4,5 % Bitcoin-verkon hashratesta. Elokuun 4. päivänä 2026 tämä vastaa suunnilleen yhtä louhittua lohkoa 3 tunnin ja 45 minuutin välein.
