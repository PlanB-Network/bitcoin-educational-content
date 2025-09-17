---
name: Electrum Airgap
description: Ensimmäinen askel kohti turvallisuutta, cold wallet Electrumilla
---
![cover](assets/cover.webp)



## Cold Wallet



Tässä opetusohjelmassa selitän, miten voit tehdä ensimmäisen airgap-signointilaitteesi, joka on irrotettu Internetistä, vaikka sinulla ei olisi omaa Hardware Wallet:ää. Tarvitset vain kaksi tietokonetta:




- vanha laite estetään ikuisesti muodostamasta yhteyttä Internetiin;
- päivittäisessä käytössä oleva tietokone.



Tämä konfiguraatio mahdollistaa suuremman tietoturvan kuin klassinen Hot Wallet: vanha tietokone, jolla ei ole verkkoyhteyttä, säilyttää yksityiset avaimesi, joita ei koskaan paljasteta Internetissä, vaan ne tallennetaan offline-tilassa ("airgap" tai "Cold").



Sen sijaan asennat Wallet-näytön ("watch-only") päivittäiseen tietokoneeseesi, joka on liitetty verkkoon ja jonka avulla voit esimerkiksi tarkistaa saldot ja valmistella kuittitapahtumia.



## Wallet Airgap: Mitä ja miten



Suorittamalla tämän oppaan vaiheet asennamme kaksi Software Wallet Electrumia kahteen eri tietokoneeseen ja luomme lopulta kaksi lompakkoa, joissa on eri avainsäilöt: Wallet airgap käyttää Wallet HD:n koko hierarkiaa, kun taas Wallet display luodaan julkisen pääavaimen avulla.



Nämä kaksi lompakkoa eroavat toisistaan hyvin paljon. Ainoa yhteinen piirre on, kuten tulemme näkemään, osoitteet:




- gW-13 airgap-tietokoneessa voi vain allekirjoittaa, mutta koska se on irrotettu verkosta, se ei tiedä käytettyjä saldoja ja osoitteita;
- gW-12 voi päivittäisessä tietokoneessa vain valmistella ja levittää tapahtumia, mutta ei voi hävittää menoja, jos yksityisiä avaimia ei ole.



## Alustava valmistelu



Jos haluat ladata Electrumin, suosittelen, että noudatat tämän ohjeen ensimmäisiä vaiheita:



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Lataamisen jälkeen tarkista aina julkaisu ennen sen asentamista ja siirry sitten "One Server" -konfiguraatioon, kuten löydät ohjeen kohdasta `Start with a Dummy Wallet`.



"Yksi palvelin" -määritystoiminto on tarpeen vain päivittäiseen tietokoneeseen asennetulle Wallet:lle, koska toinen tietokone on aina offline-tilassa.



Seuraavat toiminnot edellyttävät harjoittelua kahdella eri tietokoneella (ja lompakoilla), joten - mukavuuden ja keskittymisen vuoksi - päätin asettaa Wallet:n airgapin vaaleaan teemaan, kun taas Wallet:n näytössä on tumma teema.



## Wallet Ilmaraon luominen



Kun olet ladannut ja vahvistanut Electrumin latauksen, ota kopio suoritettavasta tiedostosta ja siirrä se tietokoneellesi offline-tilassa. Käynnistä se sitten ja asenna Electrum.



Käynnistä Electrum kaksoisklikkaamalla: tietokone, jossa käytät tätä Wallet:ää, on offline-tilassa, jätä verkkoasetukset huomiotta ja siirry Wallet:n luomiseen, jota tässä oppaassa kutsumme nimellä `airgap`.



![image](assets/en/01.webp)



Valitse _Vakiolompakko_.



![image](assets/en/02.webp)



Valitse sitten _Luo uusi siemen_, jotta ohjelmisto generate saa Mnemonic:n.



![image](assets/en/03.webp)



Kirjoita 12 generate-sanaa Electrumista tarkasti paperille ja jatka tarkistusvaiheeseen syöttämällä sanat uudelleen järjestyksessä, kun Electrum sitä pyytää.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Kun Wallet:n luominen on valmis, aseta monimutkainen salasana (`Strong`) salataksesi Wallet-tiedoston airgap-laitteessa. Tämä vaihe on hyvin arkaluonteinen ja tärkeä, koska nyt valittu salasana estää pääsyn Wallet:een, jolla on dispositiivinen valta ja joka voi käyttää varoja ja allekirjoittaa tapahtumia.



![image](assets/en/06.webp)



Kun napsautat _Finish_, Wallet määritellään ja se näkyy näytöllä. Verkkoyhteyden merkkivalo, eli oikeassa alakulmassa oleva värillinen piste, on tietenkin punainen, koska tietokoneesta on katkaistu verkkoyhteys eikä Wallet voi paljastaa verkkonäppäimiä.



![image](assets/en/07.webp)



## Visualisoinnin luonti Wallet



Nyt kun Wallet:lläsi on yksityiset offline-avaimet, sinun on perustettava näyttö Wallet tai "watch-only", jonka avulla voit tarkastella saldoa ja valmistella kuittitapahtumia, jotta voit jatkaa Sats:n keräämistä turvallisesti.



Valitse offline-laitteessa sijaitsevasta Wallet:sta _Wallet_ -> _Information_ -valikko



![image](assets/en/08.webp)



Näyttöön avautuu ikkuna, joka sisältää kaikki Wallet-tietosi, ja voit tarkistaa `derivaatiopolun` ja `master-sormenjäljen`, esimerkiksi merkitä ne Mnemonic-lauseen sanojen viereen (erittäin suositeltavaa).



![image](assets/en/09.webp)



Muista, että otat nämä tiedot tietokoneesta, johon ei ole yhteyttä, joten sinun on kopioitava/liitettävä `zpub` tekstitiedostoon ja tallennettava se USB-tikulle.



Nyt voit siirtyä tietokoneeseen, joka on yhteydessä Internetiin, käynnistää Electrumin ja luoda uuden Wallet:n.



Valitse _File_-valikosta _New/Restore_.



![image](assets/en/10.webp)



Uusi Wallet on vain katseltavissa, joten tässä oppaassa sitä kutsutaan vain katseltavaksi.



![image](assets/en/12.webp)



Valitse seuraavassa näytössä _Standardi lompakko_ ja jatka valitsemalla _Seuraava_.



![image](assets/en/13.webp)



Ole varovainen avainsäilön valinnassa: luodaksesi näytön Wallet valitse _Käytä pääavainta_. Jatka sitten valitsemalla _Seuraava_.



![image](assets/en/14.webp)



Liitä tähän Wallet:sta offline-tilassa kopioitu `zpub`, jonka toit tähän tietokoneeseen usb-tietovälineen kautta.



![image](assets/en/15.webp)



Aseta lopuksi myös tälle Wallet:lle vahva salasana, joka voi olla erilainen kuin vastaavalle Cold:lle valittu salasana.



Näyttöön ilmestyy Wallet ja varoitus. Viestissä muistutetaan, että kyseessä on vain näyttöön tarkoitettu Wallet ja että et voi käyttää siihen liittyviä varoja.



**Note Well**: **sinulla on siis aina oltava yksityiset avaimet, jotta voit hävittää tämän Wallet:n UTXO:t**. Hyvän varmuuskopiointijärjestelmän avulla sinun ei ole vaikeaa pitää Bitcoinejasi täysin hallussasi.



![image](assets/en/16.webp)



Tämä varoitus tulee näkyviin joka kerta, kun avaat tämän Wallet:n. Napsauta _Ok_ ja siirry tarkistusvaiheeseen.



## Kahden Wallet:n todentaminen



Kuten tämän oppaan alussa opimme, Wallet-ilmasäleikkö ja sen näyttö Wallet ovat kaksi salkkua, joilla on eri ominaisuudet, mutta **jakavat samat osoitteet**.



Jos tarkastelemme näitä kahta lompakkoa vierekkäin, huomaamme, että Wallet-ilmavälissä on "seed"-symboli, kun taas pelkän kellon kohdalla sitä ei ole. Jo tämä yksityiskohta auttaa sinua muistamaan, että Wallet-näytössä Wallet:ssä ei ole yksityisiä avaimia.



![image](assets/en/17.webp)



Tarkan ensimmäisen tarkistuksen tekeminen edellyttää kuitenkin, että valitset molemmista lompakoista valikon "Osoitteet": koska ne käyttävät samoja osoitteita, osoiteluettelon pitäisi olla sama molemmissa.



![image](assets/en/18.webp)



⚠️ **HUOMIO**: **Ei voi olla välivaihtoehtoa; osoitteiden on oltava samat. Jos ne eroavat toisistaan, kaikki tähän mennessä tehty työ on poistettava ja aloitettava alusta**.



Nyt voit tehdä kaksi eri tarkistusta. Yritä ensin poistaa nämä kaksi lompakkoa ja palauttaa ne tyhjästä, kumpikin sopivalla tietokoneella. Jos teet tämän tarkistuksen, näytön Wallet menettelyt ovat samat kuin edellä esitetyt.



Wallet:n ilmavälin osalta sinun on kuitenkin valittava `keystore`-näytössä _I already have a seed_ (Minulla on jo siemen_) ja syötettävä sanat kopioimalla ne paperivarmistuskopiostasi.



Kun "no-load" -kokeilujakso on päättynyt, voit yrittää tehdä pienen summan transaktion ja käyttää sen välittömästi.



## Tapahtumien vastaanottaminen ja kuluttaminen



Jos haluat aloittaa Electrum-ilmaisimen käytön, voit tehdä kuittitapahtuman pienellä summalla ja käyttää sen sitten omaan Address:ään. Sen jälkeen voit tutustua menettelyyn ja varmistaa, että hallitset varoja täysin.



**Huomautus**: En suosittele, että talletat suuren summan varoja Wallet:een ennen kuin olet varma, että pystyt suorittamaan kaikki operaatiot sujuvasti.



Jäljempänä selostetut vaiheet saattavat ensi silmäyksellä vaikuttaa monimutkaisilta. Älä anna sen masentaa itseäsi: kun olet kokeillut niitä ensimmäisen kerran, huomaat, että niiden suorittaminen vie vain muutaman minuutin.



Varojen vastaanottaminen edellyttää, että käytät Wallet-näyttöä, joka sijaitsee Internetiin liitetyssä tietokoneessasi. Valikosta `Vastaanottaa` klikkaa _Create request_, jotta Electrum generate on ensimmäinen käytettävissä oleva Address ja käyttää sitä lähettää meille muutaman Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Kun tapahtuma on siirretty, voit jo nähdä, että - kuten on luonnollista - se näkyy vain Wallet-näytössä eikä Wallet-ilmarakenteessa.



![image](assets/en/21.webp)



Kun maksutapahtumasi on saanut jonkin verran vahvistusta, voit valmistella kuluja ja kokeilla allekirjoitusta Wallet-verkon ulkopuolelta. Valmistele sitten tapahtuma watch-only ja tarkista se painamalla _Preview_ (esikatselu)



![image](assets/en/22.webp)



Saat näkyviin edistyneen tapahtumaikkunan, josta näet sen:




- tapahtumaa ei ole allekirjoitettu (`Tila: Allekirjoittamaton);
- `Sign`- ja `Broadcast`-komennot on estetty.



Ainoa asia, jonka voit tehdä, on viedä transaktio sellaisenaan, viedä se Wallet-ilma-aukkoon ja allekirjoittaa se.



Aseta USB-muistitikku tietokoneeseen ja valitse vasemmassa alakulmassa olevasta valikosta _Jaa_.



![image](assets/en/23.webp)



Valitse sen jälkeen _Tallenna tiedostoon_.



![image](assets/en/24.webp)



Tallenna tapahtuma usb-tikulle.



Huomaat, että Electrum antaa tiedostolle nimen, jonka ensimmäiset numerot ovat transaction ID, ja tiedostopääte on `.PSBT` eli `Partially Signed Bitcoin Transaction`.



Pura mediatiedosto `.PSBT`-tiedostolla ja liitä se tietokoneeseen offline-tilassa.



Valitse nyt Wallet:n ilmarajasta _Tools_-valikko, sitten _Load transaction_ ja sen jälkeen From file_.



![image](assets/en/25.webp)



Valitse tiedostonhallinnassa tiedosto `.PSBT` sen sijainnista.



![image](assets/en/29.webp)



Verkon ulkopuolinen tietokoneohjelmisto avaa automaattisesti edistyneen tapahtuman ikkunan, joka on täysin samanlainen kuin Wallet:n näytöllä. Tila on `Unsigned`, mutta erona on, että `Sign`-komento on tässä aktiivinen. Ja juuri se sinun on suoritettava.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Nyt kun tapahtuma on allekirjoitettu, muista, että Wallet on offline-koneessa. Siksi - vaikka komento "Broadcast" olisi aktiivinen - Wallet ei pysty levittämään tapahtumaa Bitcoin-verkkoon.



Nyt sinun on toistettava allekirjoitetun tapahtuman vieminen usb-muistitikulle, jotta voit tuoda sen Internetiin liitettyyn tietokoneeseen ja levittää sitä.



Valitse vasemmasta alavalikosta uudelleen _Jaa_ ja sitten _Tallenna tiedostoon_.



![image](assets/en/28.webp)



Nyt tiedostolla on eri tiedostopääte: **PSBT`:n sijaan nyt tapahtumalla on tiedostopääte `.txn`. Tästä lähtien Electrum antaa sinun tunnistaa allekirjoitetut transaktiot allekirjoittamattomista**.



![image](assets/en/30.webp)



Jotta tapahtuma siirtyisi lopullisesti eteenpäin, ota usb-tikku pois offline-tietokoneesta ja aseta se tietokoneeseen, joka on yhteydessä Internetiin.



Toista Watch-only-ohjelmasta tuontimenettely, eli valitse _Tools_-valikosta _Load transaction_ ja lopuksi _From file_.



![image](assets/en/31.webp)



Electrum avaa sinulle transaktioikkunan, joka eroaa huomattavasti aiemmin tässä Wallet:ssa näytetystä ikkunasta, sillä se on nyt allekirjoitettu (`Status: Signed`) ja `Broadcast`-komento on käytettävissä.



Viimeinen toimenpide, joka sinun on tehtävä, on juuri tämä:



![image](assets/en/32.webp)



## Päätelmät



Testit on nyt suoritettu. Jos seurasit opasta ja sait samat tulokset, olet luonut Electrumilla kahdella eri tietokoneella Wallet Cold:n, jota voit käyttää airgap-muodossa bitcoinien tallentamiseen.



Ainoat asiat, joihin sinun on kiinnitettävä erityistä huomiota, ovat kaksi:


1) **ei koskaan Wallet-ilma-aukkoa generate-vastaanotto-osoitteisiin**. Koska se on offline-tilassa, se tarjoaa sinulle aina ensimmäistä Address:ta, joka on sama kuin se, jota juuri käytit testitapahtuman tekemiseen;



![image](assets/en/33.webp)



kuten yllä olevasta kuvasta näkyy, offline Wallet ei tunne omaa Address-historiaansa. Se on tältä osin täysin sokea. **Ainut tehtävä, jonka se voi tehdä puolestasi, on tallentaa offline-avaimesi ja allekirjoittaa transaktiosi**_.



2) Käytä vain tähän tarkoitukseen varattua USB-muistitikkua, **eikä käytä usein käyttämääsi tietovälinettä**. Jokapäiväiset välineet joutuvat todennäköisemmin verkkohyökkäyksen kohteeksi, ja tahattomasti voit hyökätä jopa tietokoneeseen, jota pidät irrotettuna verkosta. USB-muistitikulla, jota käytät vain tähän tarkoitukseen, on hyvin vähän mahdollisuuksia ottaa yhteyttä tietokoneeseen verkossa, varsinkin jos olet hodler, jonka ei tarvitse kuluttaa, mikä vähentää virusten, haittaohjelmien jne. vastaanottamisen ja sitten lähettämisen todennäköisyyttä.