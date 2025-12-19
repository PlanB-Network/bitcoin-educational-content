---
name: Raspberry Pi Zero
description: Kuinka rakentaa minimaalinen, eristetty ja edullinen tietokone Raspberry Pi Zeron ja lisävarustepaketin avulla.
---
![cover](assets/cover.webp)



Jos olet ollut Plan ₿ Academy:n sivuilla jonkin aikaa, olet jo oppinut, että yksi eniten suositelluista tietoturva-asetuksista, melkeinpä pakollinen, **on varojen hallinta tallentamalla yksityiset avaimesi offline-tallennukseen**.



Jos et ole vielä tutustunut siihen, löydät tämän oppaan aikana linkkejä avoimen lähdekoodin resursseihin, joiden avulla voit oppia siitä lisää.



Yksityisten avainten hallintaan offline-tilassa tarvitaan siis laite, joka on pysyvästi irrotettu verkosta, olipa kyseessä [laitelompakko](https://planb.academy/resources/glossary/hardware-wallet) tai airgap-tietokone, joka on omistettu tälle erityiselle toiminnolle.



Miten teet sen, jos sinulla ei esimerkiksi ole mahdollisuutta hankkia laitteistoa, joka suorittaa vain tämän tehtävän, mutta et halua luopua tästä turvallisuusvaiheesta?



## Ratkaisu


Entä jos kertoisin, että voit valmistaa offline-laitteen airgap-tietokoneen muodossa, joka on USB-muistitikun kokoinen ja painoinen ja maksaa 35 euroa? Etkö uskoisi sitä?



Jatka lukemista.



Kerron teille lisää: lukekaa se kokonaan läpi. Ehdotettu ratkaisu on halpa, mutta se ei ole aivan helpoin. Ensin saat yleiskäsityksen, sitten päätät sijoittaa osan ajastasi henkilökohtaiseen tutkimukseen ja valita mahdollisimman rauhallisin mielin, jatkatko ja miten.



## Vaatimukset


**1** [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (ilman mitään jälkiliitettä) on perusta vähäisen suorituskyvyn tietokoneen rakentamiseen, mutta ennen kaikkea siitä puuttuvat Wi-Fi- ja Bluetooth-kortit, jotka ovat välttämättömiä tämän harjoituksen tarkoitukseen.





- **Kustannukset**: noin 15,00 tämän oppaan kirjoittamishetkellä (elokuu 2025).
- **Tuotannon jatkuvuus**: Vadelma takaa tuotannon tammikuuhun 2030 asti.



PI Zero ilman Wi-Fi- ja Bluetooth-yhteyksiä on valitettavasti tullut lähes mahdottomaksi. PI Zero W- ja PI Zero 2W -vaihtoehtoja saattaa löytyä helpommin. Tässä tapauksessa voit poistaa yhteystoiminnot käytöstä muuttamalla konfigurointitiedostoa. Käyttöjärjestelmän asentamisen jälkeen sinun on lisättävä nämä kohdat config-tiedostoon:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



tämän oppaan osassa kerrotaan, miten ja missä se tehdään. Jos kuitenkin haluat todella olla varma, löydät verkosta useita ohjeita Wi-Fi-sirun irrottamiseen pienellä leikkurilla, joka soveltuu elektroniikkalevyjen työstämiseen.



**2** Raspberry PI Zeron _starttipakkaus_: kuten Vadelma-maailmassa on tapana, paljaat luut, ilman ulkoista koteloa. Lisäksi näin pienen piirilevyn rajalliset resurssit ehdollistavat liitäntämahdollisuudet ulkomaailmaan.



Kun päätin jatkaa, löysin [tämän kitin](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) täynnä lisävarusteita, jotta PI Zeron koko potentiaali saataisiin hyödynnettyä. Itse asiassa paketti sisältää USB A -> micro USB power Supply, pienen USB-keskittimen, mini-HDMI -> HDMI-sovittimen, kuparisen jäähdytyselementin ja alumiinisen ulkokotelon. Pakkauksen mukana toimitetaan myös ruuvit ja kuusiokoloavain, joita tarvitaan PI Zeron asentamiseen uuteen koteloon.





- **Kustannukset**: 19.99 euroa.



**3** Tämä opetusohjelma ei vaadi suuria budjetteja airgap-tietokoneeseen. Sinun on kuitenkin hyvä tietää, että tarvitset USB-näppäimistön ja -hiiren (ehdottomasti langallinen, vältä Bluetoothia) sekä näytön. Riippuen monitorisi tulosta, saatat tarvita sovittimen mini-HDMI:stä, joka on PI Zeron ainoa saatavilla oleva lähtö. Lopuksi, katso Hard siitä, että meillä kaikilla on jossain talossa ei-johdoton näppäimistö ja hiiri - on aika Dust ne pois.



## Lisäbudjetti



**4** Alkuperäisen Supply:n saa Raspberryltä, ja se maksaa noin 15,00 euroa.



**5** Itse päätin käyttää starttipaketin mukana toimitettua Supply-virtaa, mutta yhdistin sen kuitenkin 3,70 euroa maksavaan USBA → miniUSB-kaapeliin, niin sanottuun `no data`-kaapeliin.



**6** Mikro-SD-kortti, jossa on vähintään 32 Gt:n massamuisti; jos teollinen laatu/taso on parempi.



**7** Tarvitset järjestelmän, USB-micro-SD-sovittimen, kuten kuvassa näkyvä. PI Zerosi käyttöjärjestelmä ja sen muisti toimivat itse asiassa tuolla tietovälineellä.



![img](assets/it/06.webp)



## Käyttöjärjestelmän asennus


Ennen kuin suljet PI Zeron koteloon, suosittelen, että asennat käyttöjärjestelmän. Silloin voit tarkistaa toiminnan ilmaisevan LED-valon heti kättelyssä.



Käyttöjärjestelmän valitsemiseen ja polttamiseen valitsin helpoimman tavan: käytin Raspberryn `PI Imager` -työkalua.



![img](assets/it/01.webp)



Siirry siis [Raspberryn Githubiin](https://github.com/raspberrypi/rpi-imager/releases) ladataksesi Imagerin uusimman julkaisun ja valitse se, joka sopii parhaiten käyttöjärjestelmääsi (v. 1.9.6 kirjoitushetkellä). Huomaat, että jokaisen tiedoston vieressä on myös vastaavan tiedoston tiiviste. Se tulee olemaan hyödyllinen tarkistuksessa.



![img](assets/it/02.webp)



Suosittelen, että tarkistat käyttöjärjestelmän, jota käytät airgap-tietokoneessasi, oman mielenrauhasi vuoksi. Näin saat varmuuden siitä, että käytät laillista (ei haitallista) versiota Imagerista ja näin ollen Raspi OS:stä.



Tee tarkistus heti latauksen jälkeen, kun normaalisti käyttämäsi kone on yhteydessä Internetiin



Avaa sitten Linux-pääte ja valmistele lataus luomalla `raspios`-hakemisto, joka on hyödyllinen sen kanssa työskentelyä varten.



![img](assets/it/19.webp)



Lataa imager Linux-jakelullesi `wget`:llä.



![img](assets/it/20.webp)



Suorita lopuksi tiedosto `sha256sum`-komento ja vertaa Hash:ää Raspberryn Githubissa tarjoamaan tiedostoon.



![img](assets/it/21.webp)



Jos sinulla on Windows, avaa Power Shell ja kirjoita seuraava komento:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Saat Hash:n, jonka on vastattava Raspberry Githubissa julkaistua.



Kun olet vahvistanut latauksen, voit asentaa Imagerin päivittäiseen tietokoneeseesi ja avata sen. Imager on työkalu, jota tarvitset polttaaksesi käyttöjärjestelmän micro SD:lle, josta tulee PI Zeron "järjestelmälevy".



Prosessi on erittäin yksinkertainen: valitse ensin Raspberry-laite, jota aiot käyttää (kiinnitä siis huomiota Raspi Zeron **malliisi**), sitten käyttöjärjestelmän versio ja lopuksi micro SD-kortin kiinnityspiste, johon käyttöjärjestelmä flashataan.



### Ensimmäinen askel



![img](assets/it/03.webp)



### Toinen vaihe



![img](assets/it/07.webp)



**Huomaa hyvin**: valitse `PI OS 32-bit`, joka on ainoa, joka toimii PI Zeron kanssa.



### Kolmas vaihe



![img](assets/it/08.webp)



(Ole hyvin varovainen ja jätä _Exclude System Drive_ valittuna, jotta sinua ei kehoteta asentamaan Raspin käyttöjärjestelmää tietokoneellesi.)



Kun kaikki on asetettu, Imager kysyy, haluatko käyttää mukautettuja asetuksia. Valitse haluamasi tai jatka oletusasetusten käyttöä valitsemalla _No_.



![img](assets/it/09.webp)



Vahvista, että haluat poistaa micro SD:n sisällön



![img](assets/it/10.webp)



Imager alkaa vilkuttaa käyttöjärjestelmää micro SD:lle, ja vierityspalkki ilmoittaa edistymisestä.



![img](assets/it/11.webp)



Lopussa on automaattinen todentaminen, suosittelen, ettet pysäytä sitä.



![img](assets/it/12.webp)



Lopuksi näytölle ilmestyy viesti, ja jos kaikki onnistui, se näyttää kuvassa esitetyltä.



![img](assets/it/13.webp)



Voit nyt todella poistaa microSD-kortin lukijasta ja asettaa sen PI Zeron paikkaan. Käynnistä pieni Raspberry ja tarkkaile LEDiä: odotamme sen olevan vihreä ja vilkkuvan, mikä ilmaisee käyttöjärjestelmän normaalia latautumista, minkä jälkeen sen pitäisi jäädä jatkuvasti palamaan. Jos saat muita merkkejä, esimerkiksi jos LED vilkkuu säännöllisesti tai on punainen, katso usein kysytyt kysymykset tai [tukifoorumin sivut](https://forums.raspberrypi.com/).



## Ensimmäinen kokoonpano


Raspi OS:n ensimmäinen käynnistys on hieman tavallista hitaampi, koska sen on suoritettava useita varsinaisia asennustehtäviä. Mutta jos kaikki on sujunut hyvin, näet tervetuloruudun.



![img](assets/it/14.webp)



Napsauta _Next_ (Seuraava_) asettaaksesi maantieteellisen alueen, erityisesti oikean näppäimistön lataamista varten. Kiinnitä erityistä huomiota jälkimmäiseen.



![img](assets/it/15.webp)



Napsauta _Next_ ja sinua pyydetään luomaan käyttäjä, kirjoita tunnistetietosi muistiin ja säilytä ne hyvin.



![img](assets/it/16.webp)



Ohjattu toiminto pyytää sinua valitsemaan oletusverkkoselaimen Chromiumin ja Firefoxin väliltä; se voi myös kysyä Wi-Fi-verkkoasetuksia, jos käytät Zero W- tai 2W PI:tä. Siirry eteenpäin ja napsauta _Skip_.



Jossain vaiheessa sinua kehotetaan päivittämään sisäinen ohjelmisto ja käyttöjärjestelmä. Valitse _Skip_: tätä harjoitusta varten rakennamme offline-koneen, jonka on pysyttävä offline-tilassa tästä lähtien.



Lopuksi se saattaa pyytää sinua ottamaan käyttöön `ssh`, mutta kieltäydy myös tästä vaiheesta, koska kyseessä on Zero airgap IP.



![img](assets/it/17.webp)



Enää ei ole paljon muuta konfiguroitavaa. Kun olet valmis, käynnistä vadelma uudelleen, jotta muutokset tulevat voimaan.



![img](assets/it/18.webp)



## Uusi tietokoneen ilmarako


Uudelleenkäynnistyksen jälkeen uusi airgap-tietokoneesi on valmis. PI Zero näyttää sinulle uuden työpöydän, jolla voit työskennellä joko graafisen käyttöliittymän tai komentorivin kautta.



![img](assets/it/22.webp)



### Ensimmäiset askeleet PI Zero W:n tai 2W:n osalta


Jos käytät Raspberry PI Zero W- tai 2W-sarjaa, piirilevylläsi on piirit Wi-Fi:tä ja Bluetoothia varten. Ensimmäisen asennuksen aikana ohitit yhteyden määrityksen, joten PI Zero ei ole yhteydessä Internetiin. Nyt voit poistaa nämä kaksi sirua pysyvästi käytöstä ohjelmiston avulla.



Itse asiassa Raspi OS tarjoaa tiedoston `config.txt`, jota voit muokata haluamaksesi. `config` sijaitsee `boot`-osastolla, `firmware`-hakemistossa, ja voit muokata ja tallentaa sitä `root`-oikeuksilla.



Avaa terminaali vasemmassa yläkulmassa olevasta kuvakkeesta, jolloin siitä tulee `root`.(1)



![img](assets/it/23.webp)



(1) Jos Raspi OS ei ole antanut sinun luoda `root`-salasanaa edellisten vaiheiden aikana, suosittelen, että teet sen nyt komennolla `passwd`. Se, että `root`-käyttäjä liikkuu henkilökohtaisesta käyttäjästäsi riippumatta, voi osoittautua erittäin käteväksi palautustilanteissa.



Etsi terminaalista tiedosto `config.txt` ja valmistaudu muokkaamaan sitä `nano`-editorilla.



![img](assets/it/24.webp)



Muokkaus tulisi tehdä koko `config`-kohdan alareunassa, sanojen `[All]` jälkeen. Tässä vaiheessa lisäät opetusohjelman alussa esitetyt `dtoverlay`-komennot.



![img](assets/it/25.webp)



Tallenna, sulje ja käynnistä uudelleen. Seuraavassa vaiheessa siirrymme pikku vadelman tutkimiseen.



## Mitä tältä laitteelta on odotettavissa?


Raspberryn verkkosivuston [teknisten tietojen](https://www.raspberrypi.com/products/raspberry-pi-zero/) mukaan PI Zero:ssa on yksiytiminen BCM2835-prosessori ja 512 MB RAM-muistia, joten se ei vaikuta kovin tehokkaalta.



Koska pääte on kevyempi, käytämme komentoriviä järjestelmän kokoonpanojen tutkimiseen.



Kun käynnistät tietokoneen, näet lyhyen sateenkaarenvärisen näytön, jonka jälkeen tulee Raspberryn tervetuloviesti ja vasemmassa alakulmassa käynnistykseen liittyviä ydinviestejä.



Kun PI OS:n työpöytä tulee näkyviin, avaa terminaali ja kirjoita:



```bash
uname -a
```


Tämä komento näyttää näytöllä parhaillaan käytössä olevan ytimen version ja muita tietoja.



![img](assets/it/26.webp)



Voit myös nähdä tietoja suorittimesta ja laitteistosta kirjoittamalla:



```bash
lscpu
```



![img](assets/it/27.webp)



Katso myös `proc/mem/info`.



![img](assets/it/28.webp)



Saadaksesi selville Debianin version ja julkaisun koodinimen:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Käytä


Vaikka suorituskyky vaikuttaa rajalliselta (paperilla ja verrattuna nykypäivän koneiden tehoon) PI Zero on suorituskykyinen, erityisesti päätelaitteena.





- Ensin voit siirtyä päävalikoihin ja inspiroitua _Add/Remove software_ -paneelista, josta löydät useita apuohjelmia ohjelmointia ja harjoittelua varten. Muista, että voit tehdä tämän myös terminaalista, mutta aina `root`-oikeuksilla.



![img](assets/it/33.webp)





- Voit "adoptoida" tämän offline-laitteen tallentamaan erilaisia luottamuksellisia asiakirjoja, jotka ovat tarvittaessa käytettävissä ilman, että ne ovat koskaan yhteydessä Internetiin.
- Voit käyttää tätä asetusta generate:n GPG-avainten turvalliseen käyttöön.
- Voisit jopa hyödyntää tätä uutta "lelua" airgap-allekirjoituslaitteena, [seuraamalla Arman The Parman ohjeita](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Tuntemieni lompakoiden joukossa ainoa, joka tarjoaa 32-bittisen version, on Electrum. No: Zero IP, kuten me valmistimme sen tässä opetusohjelmassa, antaisi sinulle mahdollisuuden pitää yksityiset avaimet offline-asetukset Wallet airgapille, jonka käsittelimme tässä opetusohjelmassa:



https://planb.academy/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Päätelmät


Asetuksella on luultavasti yksi suuri heikkous: micro SD on väline, joka voi aiheuttaa ongelmia. Se on herkkä kovalle käytölle; ehkä sinulla on jo kokemusta tästä, kun olet käyttänyt sitä puhelimesi kanssa. Kun olet asentanut kaikki ohjelmistot, joita haluat käyttää Zero airgap IP:ssä, tee hyvä varmuuskopio arvokkaasta micro SD:stä käyttämällä käytettävissäsi olevaa Raspi OS -työkalua.



![img](assets/it/34.webp)



Kun tarpeesi kasvavat ja niiden myötä budjettimahdollisuutesi, voit tutkia muita Raspberry- tai vastaavia ratkaisuja. Muistista puheen ollen, esimerkiksi PI 5 tarjoaa mahdollisuuden koota M2 NVME-asema, joka on varmasti kestävämpi kuin microSD.



Älä unohda tehdä muistiinpanoja ja dokumentoida jokaista offline-käyttöön tulevan apuohjelmiston asennusvaihetta. **Ennemmin tai myöhemmin ilmestyy päivitetty Raspi OS**, jota haluat varmasti hyödyntää. Siinä vaiheessa sinun on poistettava kaikki ja tehtävä kaikki alusta (ehkä uudella micro SD:llä 😂).



Juuri tekemämme harjoituksen, olettaen, että se on myös ensimmäinen kokeilusi, muistat vielä pitkään. Aina ei ole mahdollista omistaa laitteistoa `sisäänrakennettuihin` toimintoihin offline, laiminlyömättä huomiota ilmassa olevaan koneeseen, joka on kytkettävä päälle ja tarkistettava aika ajoin.



Sait sen kuitenkin tehtyä, onnittelut! Ja voit ehdottaa tätä ratkaisua kaikille niille, joiden on pidettävä budjettinsa kurissa.