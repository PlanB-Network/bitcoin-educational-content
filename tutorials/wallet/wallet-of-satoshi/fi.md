---
name: Wallet ja Satoshi
description: Yksinkertaisin huoltajien Wallet, jolla pääsee alkuun
---
![cover](assets/cover.webp)

_Tämän ohjeen on kirjoittanut_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Satoshi:n Wallet:n lataaminen, käyttöönotto ja käyttö


Satoshi:n Wallet on Lightning Network Wallet, huoltajuus, ja se on hyvin helppokäyttöinen.

Kurssilla [BTC105 - Finding Now] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5) sitä käytetään Redeem Lightning Network-seteliin.


**Aina muista**: ei avaimia, ei kolikoita


Säilytettävät lompakot eivät anna käyttäjille täyttä määräysvaltaa varoihinsa. Niitä ei yleensä suositella, paitsi aloittelijoille. WoS:ää tulisi käyttää siirtymäkauden Wallet:nä tai taskurahojen säilyttämiseen, ei pitkäaikaiseen rahastojen kartuttamiseen.


---

Satoshi:n Wallet (WoS) on säilytyspalvelu, mutta sillä on tietty maine. Voimme kohtuullisesti turvautua esimerkiksi WoS:n kaltaiseen välineeseen lisätaksemme kykyämme saada likviditeettiä. Delegoimme WoS:lle tilapäisesti "likaisen työn" eli kanavien likviditeetin hallinnan puolestamme. Kun tietty määrä on saavutettu, tyhjennämme WoS:n On-Chain:n ei-vartioitavaan Wallet:ään.


**WARNING⚠️: On suositeltavaa lukea opetusohjelma kokonaisuudessaan ennen kuin jatkat****


### Satoshi:n Wallet:n lataaminen


Mene Play Storeen ja lataa WoS


![image](assets/it/01.webp)


**Huomaa:** WoS ladataan vain virallisista kaupoista. Jos laitteen käyttöjärjestelmä on ohjelmoitu, ennen WoS:n avaamista käyttöjärjestelmä suorittaa tarkistuksen. Vahvistusvaiheen jälkeen valitse _Open_.


![image](assets/it/02.webp)


Satoshi:n Wallet avautuu seuraavaan näyttöön, ja on napsautettava _Start_


![image](assets/it/03.webp)


### WoS-tilin rekisteröinti


Tässä vaiheessa Wallet on jo toiminnassa, mutta turvallisuuden lisäämiseksi asetamme kirjautumistunnuksen: sitä tarvitaan varojen palauttamiseen, jos laitteeseen tulee toimintahäiriö tai se katoaa. Valitse siksi vasemmassa yläkulmassa oleva valikko.


![image](assets/it/04.webp)


Koko valikkoikkuna avautuu, jossa sinun on asetettava yksinomaan valuutta (Wallet Satoshi:n oletusarvoisesti esittää Yhdysvaltain dollaria viitevaluuttana) ja teemaväri (vaalea/tumma), maun mukaan. Älä käytä muita komentoja.


Koska WoS on säilytysväline, emme voi varmuuskopioida Wallet:a Mnemonic-lauseella, mutta voimme antaa WoS:lle mahdollisuuden periä varojamme takaisin, jos mobiililaite katoaa tai sitä ei käytetä, klikkaamalla _Login/Register_

Näyttöön tulee ikkuna, jossa meitä pyydetään syöttämään sähköpostiosoite Address. Se voi olla **Proton-sähköposti** (suositellaan), mutta sen on oltava toimiva, sillä sen avulla voimme saada Wallet:ssä olevat varat takaisin, jos matkapuhelin katoaa, varastetaan tai vahingoittuu.


![image](assets/it/08.webp)


Satoshi:n Wallet on lähettänyt viestin ilmoitettuun sähköpostilaatikkoon.


![image](assets/it/09.webp)


Postilaatikossa on kaksi sanaa, jotka meidän on kirjoitettava uudelleen sovelluksen osoittamaan tilaan.


- älä aktivoi kääntäjää: sanat ovat ja niiden on pysyttävä englanniksi**
- kirjoita nämä kaksi sanaa uudelleen kiinnittäen huomiota isoihin ja pieniin kirjaimiin**


![image](assets/it/10.webp)


Kun olet kirjoittanut kaksi sanaa, napsauta _OK_.


![image](assets/it/11.webp)


Tuloksena pitäisi olla kuva, joka näkyy yläreunassa ja jossa on tarkistusmerkki tarkistusta varten.


![image](assets/it/12.webp)


kun asetukset-osiossa punainen _Login/Register_-palkki näyttää nyt käyttäjän Address-sähköpostin.


![image](assets/it/13.webp)


### Maksujen vastaanottaminen


Jos haluat vastaanottaa WoS:lla, napsauta _Vastaanottaa_, jolloin näyttöön tulee joukko komentoja.


![image](assets/it/14.webp)


Voit saada


- gW-30-Address kautta **a**
- gW-32:n kautta asettamalla Invoice:n **b**
- on chain (WoS tukee Bitcoin-verkkoa, mutta maksullisilla sukellusvenevaihdoilla) **c**
- skannaamalla LNurl-p **d** QR-koodi


![image](assets/it/15.webp)


### Invoice:n luominen


Napsauta _Vastaanottaa_ ja valitse komento, jossa on Lightning Network-symboli.


![image](assets/it/16.webp)


Näyttöön tulee Invoice:n luomisvalikko, jossa napsautetaan _Add Amount_ (Lisää summa), jolloin voidaan kirjoittaa tarkka summa ja lisätä kuvaus, tässä esimerkissä "My first Invoice" (Ensimmäinen Invoice).


![image](assets/it/17.webp)


Näppäimistöllä asetamme summan.


![image](assets/it/18.webp)


ja saada sitten maksun Invoice:lle. Saatu maksu näyttää tältä:


![image](assets/it/19.webp)


### Keräys POS-asemalta


Satoshi:n Wallet:ssä on oletusominaisuus, joka tekee siitä erityisen sopivan kauppiaille: POS. Katsotaanpa, miten se aktivoidaan.


Valitse päänäytöstä oikeassa yläkulmassa oleva valikko.


![image](assets/it/20.webp)


Valitse sitten _Myyntipiste_.


![image](assets/it/21.webp)


WoS:n uusimmassa versiossa varmista, että valitset _Keypad_.


![image](assets/it/22.webp)

ja kirjoita sitten määrä näppäimistöllä, seuraavassa esimerkissä 10 senttiä / 118 Sats. Lisää keräyksen kuvaus, tässä tapauksessa "toinen kassalla". Suuri Green-painike syttyy, ja sitä on napsautettava

![image](assets/it/23.webp)


gW-43 Invoice:n ja näyttää sen esimerkiksi asiakkaalle.


![image](assets/it/24.webp)


Myös tämä maksu peritään!


![image](assets/it/25.webp)


### Maksujen lähettäminen


Yksinkertaisuus on WoS:n päänäytön vahvuus. Jos haluat maksaa Invoice:n, klikkaa _Send_


![image](assets/it/26.webp)


Ensimmäisellä käyttökerralla WoS pyytää lupaa käyttää kameraa


![image](assets/it/27.webp)


Tästä hetkestä lähtien kamera aktivoituu


![image](assets/it/28.webp)


Invoice:n kehystäminen osoittaa, että maksua on pyydetty 210 Sats:n suuruisena. Lisäksi luetaan kuvaus, jos pyynnön esittäjä on antanut sellaisen. Tämä ruutu on yhteenveto ja myös vahvistuspyyntö: WoS "pyytää valtuutusta" maksun lähettämiseen, joka myönnetään klikkaamalla Green _Send_-painiketta


![image](assets/it/29.webp)


Kun maksu saapuu määränpäähänsä, WoS ilmoittaa siitä tällä näytöllä


![image](assets/it/30.webp)


Klikkaamalla päänäytöltä _Historiaa_ (aivan saldon alapuolella) saat näkyviin luettelon tapahtumista


![image](assets/it/31.webp)


#### WoS-tilin palauttaminen


Nyt katsotaan, miten WoS asennetaan uuteen laitteeseen; tämä on hyödyllistä myös silloin, kun Wallet on varastettu tai kadonnut tai kun matkapuhelinta, johon Wallet oli aiemmin asennettu, ei voida käyttää. Kun olet asentanut sen uudelleen, sinun on toistettava äsken selostettu tilin rekisteröintimenettely yhdellä muunnelmalla: aiemmin määritetyllä sähköpostilla kirjautumista koskevan pyynnön lopussa WoS tulee näkyviin seuraavasti:


![image](assets/it/33.webp)


Viesti varoittaa meitä siitä, että sähköpostiviesti on lähetetty, jossa kerrotaan, miten tili aktivoidaan uudelleen. Sinun on avattava sähköpostilaatikkosi.


**TÄRKEÄÄ**: avaa sähköposti tietokoneelta tai joka tapauksessa muulta laitteelta kuin siltä, jolla aiot palauttaa WoS-tilin. Saapuneista sähköposteista löytyy viesti, jossa näytetään QR-koodi, jota kehystetään


![image](assets/it/34.webp)


Kun QR-koodi on kehystetty, WoS:n pääsivulla näkyy palautettu tili, saldo ja historia.