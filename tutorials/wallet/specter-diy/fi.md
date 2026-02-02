---
name: Specter DIY
description: Specter DIY:n asennusopas
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunks kirjoittavat koodia. Tiedämme, että jonkun on kirjoitettava ohjelmia yksityisyyden puolustamiseksi, ja koska yksityisyyttä ei saada, jos me kaikki emme tee sitä, me kirjoitamme sitä.

*Cypherpunk:n manifesti - Eric Hughes - 9. maaliskuuta 1993*


Hankkeen ideana on rakentaa wallet-laitteisto valmiista komponenteista.

Vaikka meillä on laajennuskortti, joka tuo kaiken mukavaan muotoon ja auttaa sinua välttämään juottamista, tuemme ja ylläpidämme edelleen yhteensopivuutta vakiokomponenttien kanssa.


![image](assets/fr/01.webp)


Haluamme myös pitää projektin joustavana niin, että se voi toimia missä tahansa muussa komponenttikokonaisuudessa pienin muutoksin. Ehkä haluat tehdä wallet-laitteiston eri arkkitehtuurilla (RISC-V?), jossa on äänimodeemi viestintäkanavana - sinun pitäisi pystyä tekemään se. Specterin toiminnallisuutta pitäisi olla helppo lisätä tai muuttaa, ja pyrimme abstrahoimaan loogisia moduuleja niin paljon kuin mahdollista.


QR-koodit ovat Specterin oletusarvoinen tapa kommunikoida isännän kanssa. QR-koodit ovat melko käteviä ja antavat käyttäjälle mahdollisuuden hallita tiedonsiirtoa - jokaisella QR-koodilla on hyvin rajallinen kapasiteetti ja viestintä tapahtuu yksisuuntaisesti. Ja se on ilmakytketty - sinun ei tarvitse liittää wallet:a tietokoneeseen missään vaiheessa.


Salaisuuksien tallentamista varten tuemme agnostic-tilaa (wallet unohtaa kaikki salaisuudet, kun se kytketään pois päältä), holtitonta tilaa (tallentaa salaisuudet sovelluksen mikrokontrollerin flash-muistiin) ja secure element-integraatio on tulossa pian.


Keskitymme ensisijaisesti usean allekirjoituksen käyttöön muiden laitteistolompakoiden kanssa, mutta wallet voi toimia myös yksittäisenä allekirjoittajana. Yritämme tehdä siitä yhteensopivan Bitcoin Core -ohjelman kanssa mahdollisuuksien mukaan - PSBT allekirjoituksettomia transaktioita varten, wallet-kuvaajat monisignaattorilompakoiden tuontia/vientiä varten. Helpottaaksemme kommunikaatiota Bitcoin Coren kanssa työskentelemme myös [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - pienen python-flask-palvelimen, joka puhuu Bitcoin Core -solmun kanssa.


Suurin osa laiteohjelmistosta on kirjoitettu MicroPython-kielellä, joten koodia on helppo tarkastaa ja muuttaa. Käytämme Bitcoin Coren [secp256k1](https://github.com/bitcoin-core/secp256k1) -kirjastoa elliptisten käyrien laskentaan ja [LittlevGL](https://lvgl.io/) -kirjastoa graafiseen käyttöliittymään.


## Vastuuvapauslauseke


Hanke on kehittynyt merkittävästi, ja Specter-DIY:n turvallisuustaso on nyt verrattavissa markkinoilla oleviin kaupallisiin laitteistolompakoihin. Toteutimme suojatun käynnistyslataajan, joka tarkistaa laiteohjelmiston päivitykset, joten voit olla varma, että laitteeseen voidaan ladata vain allekirjoitettuja laiteohjelmia alkuasennuksen jälkeen. Toisin kuin kaupallisissa allekirjoittamislaitteissa, käyttäjän on kuitenkin asennettava käynnistyslatausohjelma manuaalisesti, eikä sitä aseteta laitteen valmistajan tehtaalla. Ole siis erityisen tarkkaavainen laiteohjelmiston alkuasennuksen aikana ja varmista, että olet tarkistanut PGP-allekirjoitukset ja flashannut laiteohjelmiston suojatulta tietokoneelta.


Jos jokin ei toimi, avaa ongelma täällä tai kysy kysymys [Telegram-ryhmässä](https://t.me/+VEinVSYkW5TUl5Ai).


## Specter-DIY:n ostoslista


Tässä kuvaamme, mitä kannattaa ostaa, ja seuraavassa osassa kerromme, miten se kootaan, ja kerromme muutaman huomautuksen piirilevystä - virtalähteet, USB-portit jne.


### Löytötaulu


Laitteen tärkein osa on kehittäjälevy:



- STM32F469I-DISCO-kehityslevy (esim. [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) tai [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Mini**USB-kaapeli
- Tavallinen MicroUSB-kaapeli USB-yhteyttä varten


Valinnainen mutta suositeltava:


- [Waveshare QR-koodiskanneri](https://www.waveshare.com/barcode-scanner-module.htm) pitkillä nastapäätteillä kuten [nämä](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) tai [nämä](https://www.amazon.com/gp/product/B015KA0RRU/) skannerin liittämiseksi piirilevyyn (tarvitaan 4 nastapäätettä).


Työstämme parhaillaan laajennuslevyä, joka sisältää älykorttipaikan, QR-koodin skannerin, akun ja 3d-tulostetun kotelon, mutta se ei sisällä pääosaa - löytölevyä, joka sinun on tilattava erikseen. Näin toimitusketjuun kohdistuvat hyökkäykset eivät edelleenkään ole ongelma, sillä turvallisuuden kannalta kriittiset komponentit ostetaan satunnaisesta elektroniikkaliikkeestä.


Voit aloittaa Specterin käytön jopa ilman lisäkomponentteja, mutta voit kommunikoida sen kanssa USB:n tai sisäänrakennetun SD-korttipaikan kautta. Specterin käyttäminen USB:n kautta tarkoittaa, että se ei ole ilmakytketty, joten menetät tärkeän tietoturvaominaisuuden.


### QR-skanneri


QR-koodin skanneria varten sinulla on useita vaihtoehtoja.


**Vaihtoehto 1. Suositeltava.** Waveshare tarjoaa erittäin hyvän skannerin (40$)


[Waveshare-skanneri](https://www.waveshare.com/barcode-scanner-module.htm) - sinun on keksittävä, miten se kiinnitetään nätisti, ehkäpä käyttämällä jonkinlaista Arduino Prototype -kilpeä ja teippiä.


Juottamista ei tarvita, mutta jos sinulla on juottamistaitoja, voit tehdä wallet:stä paljon hienomman ;)


**Vaihtoehto 2.** Erittäin hieno skanneri Mikroelta, mutta melko kallis (150$):


[Viivakoodin napsautus](https://www.mikroe.com/barcode-click) + [Sovitin](https://www.mikroe.com/arduino-uno-click-shield)


**Vaihtoehto 3.** Mikä tahansa muu QR-skanneri


Kiinasta löytyy halpoja skannereita. Niiden laatu ei useinkaan ole kovin hyvä, mutta voit ottaa riskin. Ehkä jopa ESPcamera voisi toimia. Sinun tarvitsee vain kytkeä virta, UART (nastat D0 ja D1) ja liipaisu D5:een.


**Vaihtoehto 4.** Ei skanneria.


Silloin voit käyttää Specteria vain USB/SD-kortin kanssa.


Ellet sitten rakenna omaa viestintämoduulia, joka käyttää QR-koodien sijasta jotain muuta - audiomodeemia, bluetoothia tai mitä tahansa muuta. Heti kun se voidaan laukaista ja lähettää tietoja sarjaportilla, voit tehdä mitä haluat.


### Valinnaiset komponentit


Jos lisäät pienen virtapankin tai akun ja virtalaturin/boosterin, wallet:stä tulee täysin itsenäinen ;)



## Specter-DIY:n kokoaminen



![video](https://youtu.be/1H7FqG_FmCw)


### Waveshare-viivakoodiskannerin yhdistäminen


wallet:n laiteohjelmisto määrittää skannerin puolestasi ensimmäisellä käyttökerralla, joten manuaalista esiasetusta ei tarvita.


Näin kytket skannerin piirilevyyn:


![image](assets/fr/02.webp)


Yksinkertaisuuden vuoksi voit ostaa Arduino Protype kilpi ja juottaa ja asentaa kaiken siihen (esim. [tämä](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Virranhallinta


Piirilevyn yläpuolella on hyppääjä, joka määrittelee, mistä se ottaa virtaa. Voit vaihtaa hyppääjän asentoa ja valita virtalähteeksi yhden USB-portista tai VIN-nastan ja kytkeä ulkoisen pariston sinne (sen pitäisi olla 5 V).


### Kotelo DIY:tä varten


Tutustu [liitteet](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures) -kansioon.


### Ole luova!


Kokoa oma Specter-DIY ja lähetä meille kuvat (tee pull request tai ota meihin yhteyttä).


Tutustu [Galleriaan](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md), jossa on yhteisön kokoamia Specterejä!




## Käännetyn koodin asentaminen


Suojatun käynnistyslataajan kanssa laiteohjelmiston alkuasennus on hieman erilainen. Päivitykset ovat helpompia, eikä laitteistoa wallet tarvitse liittää tietokoneeseen.


![video](https://youtu.be/eF4cgK_L6T4)


### Alkuperäisen laiteohjelmiston flashaus


**Huomautus** Jos et halua käyttää julkaisuista saatavia binäärejä, tutustu [bootloader documentation](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md), jossa kerrotaan, miten se käännetään ja konfiguroidaan käyttämään omia julkisia avaimiasi meidän avaimiemme sijasta.



- Jos päivität alle `1.4.0`-versiosta tai lataat laiteohjelmiston ensimmäistä kertaa, käytä [releases](https://github.com/cryptoadvance/specter-diy/releases) -sivulta löytyvää `initial_firmware_<version>.bin`-tiedostoa.
 - Tarkista tiedoston `sha256.signed.txt` allekirjoitus [Stepanin PGP-avaimella](https://stepansnigirev.com/ss-specter-release.asc) perusteella
 - Tarkista `initial_firmware_<version>.bin`:n hash-arvo verrattuna `sha256.signed.txt`-tiedostoon tallennettuun hash-arvoon
- Jos päivität tyhjästä käynnistyslatauslaitteesta tai näet käynnistyslatauslaitteen virheilmoituksen, jonka mukaan laiteohjelmisto ei ole kelvollinen, tutustu seuraavaan osioon - Allekirjoitetun Specter-firmaohjelmiston flashaus.
- Varmista, että havaintokortin virtajumpperi on asennossa STLK
- Kytke havaintokortti tietokoneeseen kortin yläosassa olevalla **miniUSB**-kaapelilla.
    - Levyn pitäisi näkyä irrotettavana levynä nimeltä "DIS_F469NI".
- Kopioi tiedosto `initial_firmware_<version>.bin` tiedosto tiedostojärjestelmän `DIS_F469NI` juureen.
- Kun laiteohjelmiston flashaus on valmis, laite nollaa itsensä ja käynnistyy uudelleen käynnistyslatausohjelmaan. Bootloader tarkistaa laiteohjelmiston ja käynnistyy päälaiteohjelmistoon. Jos näet virheilmoituksen, että laiteohjelmistoa ei löydy - noudata päivitysohjeita ja lataa laiteohjelmisto SD-kortin kautta.
- Nyt voit kytkeä virtakytkimen haluamaasi kohtaan ja syöttää piirilevylle virtaa virtalähteestä tai akusta.


Alkuperäisen laiteohjelmiston flashaaminen kopioimalla ja liittämällä `.bin`-tiedosto ei aina onnistu - usein johtuen kaapelista tai jos laite liitetään USB-keskittimen kautta. Tällöin voit yrittää vielä muutaman kerran (yleensä se onnistuu 2-3 yrityksellä).


Jos se ei aina onnistu, voit käyttää [stlink](https://github.com/stlink-org/stlink/releases/latest) avoimen lähdekoodin työkalua. Asenna se ja kirjoita terminaaliin: 0x8000000". Se toimii yleensä paljon luotettavammin.


### Laiteohjelmiston päivittäminen



- Lataa `specter_upgrade_<versio>.bin` [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Kopioi tämä binääritiedosto SD-kortin juureen (FAT-muotoinen, enintään 32 Gt)
 - Varmista, että juurihakemistossa on vain yksi `specter_upgrade***.bin`-tiedosto
- Aseta SD-kortti löytöalustan SD-korttipaikkaan ja kytke aluksella virta päälle
- Bootloader flashaa laiteohjelmiston ja ilmoittaa, kun se on valmis.
- Käynnistä kortti uudelleen - näet Specter-DIY-käyttöliittymän nyt, se ehdottaa sinulle PIN-koodin valintaa


Aina kun uusi versio ilmestyy, lataa `specter_upgrade_<version>.bin` julkaisuista, siirrä se SD-kortille ja päivitä laite kuten edellisessä vaiheessa. Bootloader varmistaa, että vain allekirjoitettu firmware voidaan ladata levylle.


### Kuinka selvittää laiteohjelmiston versio


Mene `Laitteen asetukset` -valikkoon - näytön otsikon alla näkyy versionumero.


## Käytä Specter-DIY wallet:tä



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Specter-DIY:n turvallisuus


### Laitteisto


Näyttöä ohjaa sovelluksen MCU.


Turvallisen elementin integrointi ei ole vielä valmis - tällä hetkellä salaisuudet tallennetaan myös pää-MCU:hun. Voit kuitenkin käyttää wallet:ta ilman salaisuuden tallentamista - sinun on syötettävä palautuslauseke joka kerta. Miksi muistaa pitkä passphrase, jos voit muistaa koko muistisäännön?


Laite käyttää ulkoista flash-muistia joidenkin tiedostojen tallentamiseen (QSPI), mutta wallet allekirjoittaa kaikki käyttäjätiedostot ja tarkistaa ne ladattaessa.


QR-skannaustoiminto on erillisessä mikrokontrollerissa, joten kaikki kuvankäsittely tapahtuu turvallisuuskriittisen MCU:n ulkopuolella. Tällä hetkellä USB:tä ja SD-korttia hallinnoi edelleen pää-MCU, joten älä käytä SD-korttia ja USB:tä, jos haluat vähentää hyökkäyspintaa.


### PIN-suojaus (käyttäjän todennus)


Ensimmäisen käynnistyksen aikana pää-MCU:ssa luodaan yksilöllinen salaisuus. Tämän salaisuuden avulla voit varmistaa, että laitetta ei ole korvattu haitallisella laitteella - kun syötät PIN-koodin, näet luettelon sanoista, jotka pysyvät samoina salaisuuden voimassaoloaikana.


PIN-koodia ja tätä yksilöllistä salaisuutta käytetään generate avainten Bitcoin purkuavaimen muodostamiseen (jos tallennat ne). Jos hyökkääjä siis pystyisi ohittamaan PIN-koodin näytön, salauksen purku ei onnistuisi.


Jos olet lukinnut laiteohjelmiston (TODO: lisää ohjeet linkki tänne), se lukitsee tehokkaasti myös salaisuuden, joten jos hyökkääjä väläyttää eri laiteohjelmiston levylle, salaisuus pyyhkiytyy pois ja voit tunnistaa sen, kun alat syöttää PIN-koodia - sanat sekvenssi on erilainen.


### Elvytyslausekkeen luominen


Tämä on yksi wallet:n tärkeimmistä osista - generate:lle avain turvallisesti. Jotta tämä onnistuisi hyvin, käytämme useita entropian lähteitä:



- Mikrokontrollerin TRNG. Patentoitu, sertifioitu ja luultavasti hyvä, mutta me emme luota siihen
- Kosketusnäyttö. Aina kun kosketat näyttöä, mittaamme näytön sijainnin ja hetken, jolloin kosketus tapahtui (mikrokontrollerin tikit 180 MHz:n taajuudella).
- Sisäänrakennetut mikrofonit - ei vielä. Levyssä on kaksi mikrofonia, joten laitteisto wallet voi kuunnella sinua ja sekoittaa nämä tiedot entropia-altaaseen.


Kaikki tämä entropia yhdistetään ja muunnetaan palautuslausekkeeksi. Tuloksena saatava entropia on aina parempi kuin mikään yksittäinen lähde.


### Korkean tason logiikka - lompakot


Specter toimii avainvarastona. Se säilyttää yksityisiä HD-avaimia, jotka voivat olla mukana lompakoissa. Lompakot määritellään niiden kuvaajien avulla. Tuemme myös miniskriptejä.


Jokainen wallet kuuluu tiettyyn verkkoon. Tämä tarkoittaa, että jos tuot wallet:n `testnetissä`, se ei ole käytettävissä `mainnet:ssa` tai `regtestissä` - sinun on vaihdettava tähän verkkoon ja tuotava wallet erikseen.


### Tapahtumien todentaminen


Seuraavia sääntöjä sovelletaan liiketoimiin, jotka wallet allekirjoittaa:



- jos eri lompakoista peräisin olevia sekalaisia syötteitä havaitaan, käyttäjää varoitetaan ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- muutostulosteet näyttävät sen wallet:n nimen, johon ne lähetetään
- jos haluat käyttää multisig- tai miniskriptiä, sinun on ensin tuotava wallet lisäämällä wallet-kuvaaja (QR:n, USB:n tai SD-kortin kautta)


## Kuvaajien tuki


Kaikki normaalit Bitcoin-kuvaajat toimivat. Sen lisäksi meillä on muutama laajennus:


### Useita haaroja kuvaajissa


Säästääksemme tilaa QR-koodeissa sallimme useamman haaran kuvaajien lisäämisen kerralla. Jos haluat käyttää `wpkh(xpub/0/*)` vastaanotto-osoitteita ja `wpkh(xpub/1/*)` muutososoitteita varten, voit yhdistää ne yhdeksi kuvaajaksi: `wpkh(xpub/{0,1}/*)` - wallet käsittelee `{}`-joukon osan ensimmäistä indeksiä vastaanotto-osoitteiden haarana ja toista haaraa muutososoitteina.


Voit myös määrittää useampia kuin kaksi haaraa, ja haarojen indeksit voivat olla erilaisia eri kanssakirjoittajille, joten tämä kuvaaja on hyvin outo mutta täysin pätevä:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Tässä tapauksessa wallet käyttää osoitteen numero 17 vastaanottamiseen komentosarjaa `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


Ainoa vaatimus on, että kaikkien sarjojen indeksien määrä on sama (3 edellä mainitussa tapauksessa).


### Oletusarvoiset johdannaiset


Jos kuvaaja sisältää julkisia yleisavaimia mutta ei jokerimerkkijohdannaisia, oletusjohdannainen `/{0,1}/*` lisätään kaikkiin kuvaajan laajennettuihin avaimiin. Jos ainakin yhdessä xpubissa on jokerimerkkijohdannainen, kuvaajaa ei muuteta.


Kuvaaja `wpkh(xpub)` muunnetaan muotoon `wpkh(xpub/{0,1}/*)`.


### Miniskripti


Specter tukee miniscriptiä, mutta se ei tue policy-to-miniscript-kääntämistä (koska se on aivan liian kallista). Suoritamme joitakin tarkistuksia miniskriptille, joten vain `B`-skriptit ovat sallittuja ylimmällä tasolla ja kaikilla ali-miniskriptien argumenteilla on oltava [spec](http://bitcoin.sipa.be/miniscript/) mukaiset ominaisuudet.


Voit käyttää [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) generate-kuvaajaa käytännöstä ja tuoda sen sitten wallet:een.


Esimerkiksi käytäntö "voin käyttää nyt tai 100 päivän kuluttua vaimoni voi käyttää" voidaan muuntaa wallet:ksi seuraavasti:


Politiikka: (avaimeni on 9-kertaisesti todennäköisempi)


Miniskripti: pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Koska tässä tapauksessa meillä ei ole mitään jokerimerkkijohdoksia, xpubiin liitetään oletusarvoiset johdokset `/{0,1}/*`.



---

MIT-lisenssi


Tekijänoikeus (c) 2019 cryptoadvance


---