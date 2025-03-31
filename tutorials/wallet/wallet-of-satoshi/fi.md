---
name: Satoshi:n Wallet (WoS)
description: Yksinkertaisin Wallet (huoltajuus), josta aloittaa
---
![cover](assets/cover.webp)

_Tämän ohjeen on kirjoittanut_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

# Lataa, määritä ja käytä Satoshi:n Wallet:tä

Wallet Satoshi on Wallet Lightning Network, huoltajuus, erittäin helppokäyttöinen.

Kurssilla [BTC105 - Finding Yourself Now] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5) sitä käytetään Redeem Lightning Network-seteliin.

**muistakaa aina**: ei avaimia, ei kolikoita

Wallet säilytyspalvelut, eivät anna käyttäjille mahdollisuutta luovuttaa varojaan kokonaan. Niitä ei yleensä suositella, paitsi niille, jotka aloittavat tyhjästä. WoS:ää tulisi käyttää Wallet:n yhdyskäytävänä tai taskurahojen säilyttämiseen, ei varojen keräämiseen pitkällä aikavälillä.

---
Satoshi:n Wallet (WoS) on säilytyspalvelu, mutta sillä on tietty maine. Voimme kohtuullisesti turvautua esimerkiksi WoS:n kaltaiseen välineeseen lisätaksemme kykyämme saada likviditeettiä. Delegoimme WoS:lle väliaikaisesti "likaisen työn", eli kanavien likviditeetin hallinnan puolestamme. Kun saavutamme tietyn määrän, tyhjennämme WoSin On-Chain:n Wallet:n ei-vartioimallamme Wallet:llä.

**ATTENZIONE⚠️: On suositeltavaa, että luet ohjeen kokonaisuudessaan ennen kuin jatkat****

## Satoshi:n Wallet:n lataaminen

Mennään Playstore ja lataa WoS

![image](assets/it/01.webp)

**Huomaa:** WoS ladataan vain virallisista kaupoista. Jos laitteen käyttöjärjestelmä on ohjelmoitu, ennen WoSin avaamista suoritetaan käyttöjärjestelmän itsensä suorittama varmennusosa. Kun varmennusvaihe on ohi, valitse _Open_.

![image](assets/it/02.webp)

Satoshi:n Wallet avautuu seuraavaan näyttöön, ja sinun on napsautettava _Start_

![image](assets/it/03.webp)

## Tilin rekisteröiminen WoS:iin

Tässä vaiheessa Wallet on toiminnassa, mutta turvallisuuden lisäämiseksi asetetaan kirjautumistunnus: tätä käytetään varojen palauttamiseen, jos laite vioittuu tai katoaa. Valitse sitten vasemmassa yläkulmassa oleva valikko.

![image](assets/it/04.webp)

Koko valikkoikkuna avautuu, jossa sinun tarvitsee vain asettaa valuutta (Wallet Satoshi:n oletusarvoisesti esittää Yhdysvaltain dollaria viitevaluuttana) ja teemaväri (vaalea/tumma) makusi mukaan. Älä käytä muita säätimiä.

Koska WoS on säilytysväline, emme voi varmuuskopioida Wallet:a Mnemonic-lauseella, mutta voimme kuitenkin antaa WoS:lle mahdollisuuden hakea varojamme, jos mobiililaite on kadonnut tai sitä ei ole käytetty, klikkaamalla _Login/Register_

![image](assets/it/07.webp)

Näyttöön tulee ikkuna, jossa meitä pyydetään antamaan sähköpostiosoite Address. Se voi olla **Proton-sähköposti** (suositellaan), mutta se toimii, koska sen avulla voimme palauttaa Wallet-varat, jos kännykkä on kadonnut/varastettu tai rikkoutunut

![image](assets/it/08.webp)

Satoshi:n Wallet lähetti viestin ilmoitettuun sähköpostilaatikkoon

![image](assets/it/09.webp)

Saapuneissa viesteissä on kaksi sanaa, jotka meidän on syötettävä ja kirjoitettava uudelleen sovelluksen tarjoamaan tilaan


- älä aktivoi kääntäjää: sanat ovat ja niiden pitäisi pysyä englanniksi**
- kirjoita kaksi sanaa uudelleen kiinnittäen huomiota isoihin ja pieniin kirjaimiin**

![image](assets/it/10.webp)

Kun olet kirjoittanut kaksi sanaa, napsauta _OK_

![image](assets/it/11.webp)

Tuloksena on, että ylhäällä näkyy luku, jossa on tarkistusmerkki tarkistusta varten

![image](assets/it/12.webp)

kun taas asetukset-osiossa _Login/Register_-kohdan punainen kaistale näyttää nyt käyttäjän Address-sähköpostin.

![image](assets/it/13.webp)

## Maksujen vastaanottaminen

Voit vastaanottaa WoS:lla napsauttamalla _Vastaanottaa_, jolloin näyttöön tulee joukko komentoja.

![image](assets/it/14.webp)

Voit saada


- gW-30-Address kautta **a**
- gW-32:n kautta, asetus Invoice **b**
- on chain (WoS tukee Bitcoin-verkkoa, mutta maksullisilla sukellusvenevaihdoilla) **c**
- lNurl-p:n QR-koodin kehystäminen **d**

![image](assets/it/15.webp)

## Invoice luominen

Napsauta _Vastaanottaa_ ja valitse komento, jonka symboli on Lightning Network

![image](assets/it/16.webp)

Näyttöön tulee vain Invoice:n luomisvalikko, jossa klikataan _Add Amount_ (Lisää summa), jolloin voidaan kirjoittaa tarkka summa ja lisätä kuvaus, tässä esimerkissä "Ensimmäinen Invoice:ni"

![image](assets/it/17.webp)

Näppäimistön avulla asetamme määrän

![image](assets/it/18.webp)

ja saat sitten Invoice:n maksun. Saatu maksu näyttää tältä:

![image](assets/it/19.webp)

## Keräys POS-asemalta

Satoshi:n Wallet:ssä on oletusarvoisesti mielenkiintoinen ominaisuus, joka tekee siitä erityisen sopivan kauppiaille: POS. Katsotaanpa, miten se aktivoidaan.

Valitse päänäytöstä oikeassa yläkulmassa oleva valikko

![image](assets/it/20.webp)

Valitse sen jälkeen _Myyntipiste_

![image](assets/it/21.webp)

WoS:n viimeisimmässä versiossa on kiinnitettävä huomiota siihen, että valitset _Keypad_:n

![image](assets/it/22.webp)

ja kirjoita sitten määrä näppäimistölle, seuraavassa esimerkissä 18 senttiä / 118 Sats. Lisää keräyksen kuvaus, tässä tapauksessa "toinen kassalla" Suuri Green-painike syttyy, ja sitä on napsauttaa

![image](assets/it/23.webp)

gW-43:n Invoice:ää ja näyttää sen esimerkiksi asiakkaalle.

![image](assets/it/24.webp)

Myös tämä maksu peritään!

![image](assets/it/25.webp)

## Maksujen lähettäminen

Yksinkertaisuus on WoS:n päänäytön vahvuus. Voit maksaa Invoice:n klikkaamalla _Send_

![image](assets/it/26.webp)

Ensimmäisellä käyttökerralla WoS kysyy käyttöoikeuksia kameraa varten

![image](assets/it/27.webp)

Tästä hetkestä lähtien kamera aktivoituu

![image](assets/it/28.webp)

Invoice:n kehyksen perusteella näemme, että 210 Sats:n maksua on pyydetty. Siinä lukee myös kuvaus, jos pyytäjä on asettanut sellaisen. Tämä ruutu on yhteenveto ja myös vahvistuspyyntö: WoS "pyytää lupaa" maksun lähettämiseen, joka myönnetään napsauttamalla Green _Send_-painiketta

![image](assets/it/29.webp)

Kun maksu saapuu määränpäähänsä, WoS ilmoittaa tästä näytöllä

![image](assets/it/30.webp)

Kun klikkaat pääkuvassa _Historiaa_ (saldon alapuolella), saat näkyviin luettelon tapahtumista

![image](assets/it/31.webp)

### WoS-tilin palautus

Nyt katsotaan, miten WoS asennetaan uuteen laitteeseen; tästä on hyötyä myös silloin, kun Wallet on varastettu, kadonnut tai kännykkä, johon Wallet oli aiemmin asennettu, ei toimi. Kun olet asentanut sen uudelleen, sinun on tehtävä juuri selitetty tilin rekisteröintimenettely uudelleen, yhdellä muunnelmalla: aiemmin asetetulla sähköpostilla tehdyn kirjautumispyynnön lopussa WoS näkyy seuraavasti:

![image](assets/it/33.webp)

Viestissä ilmoitetaan, että tilin uudelleenaktivointimenettely on lähetetty sähköpostitse. Postilaatikko on avattava.

**TÄRKEÄÄ**: avaa sähköposti tietokoneelta tai ainakin muulta laitteelta kuin siltä, jolla aiot hakea WoS-tilin. Saapuneista sähköposteista löytyy viesti, jossa näytetään QR-koodi, jonka voi kehystää..

![image](assets/it/34.webp)

Kun QR-koodi on kehystetty, haettu tili näkyy WoS:n pääsivulla saldon ja historian kanssa.