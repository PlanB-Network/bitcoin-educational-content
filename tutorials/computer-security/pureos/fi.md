---
name: PureOS
description: Linux-jakelu, jonka avulla voit hallita digitaalista elämääsi.
---

![cover](assets/cover.webp)



Henkilökohtaisten tietojen suojaaminen digitaaliaikana on jokaisen internetin käyttäjän ensisijainen tavoite. Yritykset, organisaatiot ja jopa käyttöjärjestelmät ovat hyödyllisiä tietolähteitä profiilin ja elämäntyylin määrittelyssä. Oikean käyttöjärjestelmän valinta on ensimmäinen askel yksityisyyden vahvistamisessa verkossa. Tässä opetusohjelmassa tutustumme PureOS:ään, yksityisyyteen keskittyvään Linux-jakeluun.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## PureOS:n käytön aloittaminen



PureOS on Purismin kehittämä Debian-pohjainen käyttöjärjestelmä. PureOS sopii sekä IT-ammattilaisille että käyttäjille, jotka etsivät yksinkertaista ja helppokäyttöistä jakelua. Se on ainutlaatuinen siinä mielessä, että se on *vapaa ohjelmisto*, ja se keskittyy käyttäjiensä henkilötietojen suojaamiseen luomalla Debianin tarjoamiin yksityisyyteen, vapauteen, turvallisuuteen ja vakauteen perustuvan kehyksen.



### Miksi valita PureOS?





- Yksinkertainen, intuitiivinen Interface**: GNOME tarjoaa selkeän Interface-työpöydän, joka on suunniteltu helppokäyttöiseksi myös niille, jotka eivät tunne komentoriviä.





- Ilmainen**: kuten useimmat Linux-jakelut, PureOS on täysin ilmainen käyttää. Kuukausitilaus on kuitenkin saatavilla kehittäjien tukemiseksi.





- Turvallisuus ja vakaus**: PureOS:n arkkitehtuuri ja käyttötapa tekevät siitä erittäin turvallisen jakelun, joka takaa tietosuojan ja järjestelmän vakauden.





- Dokumentaatio ja aktiivinen yhteisö**: PureOS:llä on selkeä, helppokäyttöinen dokumentaatio ja sitoutunut, reagoiva yhteisö, jonka avulla on helppo ratkaista ongelmia ja oppia järjestelmä askel askeleelta.



## Asennus ja konfigurointi



PureOS:n asentaminen ja konfigurointi tietokoneeseen edellyttää seuraavia minimalistisia ominaisuuksia:




- Vähintään 8 Gt:n kokoinen USB-levy järjestelmän flashaamista varten.
- 4 GB RAM-MUISTIA.
- 30 Gt vapaata tilaa Hard-levyllä.



Siirry [PureOS:n viralliselle verkkosivustolle] (https://pureos.net/) ja lataa käyttöjärjestelmän ISO-kuva koneesi arkkitehtuurin mukaan.



Käynnistääksesi PureOS-asennuksen sinun on luotava käynnistettävä USB-levy käyttämällä flash-ohjelmistoa, kuten [Balena Etcher](https://www.balena.io/etcher).



Kolmessa yksinkertaisessa vaiheessa saat USB-tikun käynnistettyä PureOS-käyttöjärjestelmän.





- Kytke USB-muistitikku ja suorita ladattu Balena-ohjelmisto.
- Valitse sitten PureOS-ISO-kuva
- Valitse USB-muistitikku lähtölaitteeksi, napsauta sitten **Flash**-painiketta ja odota, että prosessi päättyy.



![0_01](assets/fr/01.webp)



Kun USB-levy on käynnistetty, käynnistä tietokone, johon haluat asentaa PureOS:n, uudelleen.



Kun käynnistät koneen, pääset BIOSiin painamalla `ESC`, `F9` tai `F11` -näppäintä koneestasi riippuen. Valitse käynnistyslaitteeksi USB-muistitikku ja vahvista se painamalla `ENTER`.



### Käynnistysnäyttö



PureOS tarjoaa useita vaihtoehtoja käyttöjärjestelmän käynnistämiseen. Valitse **Testaa tai asenna PureOS** -vaihtoehto käynnistääksesi käyttöjärjestelmän asennuksen.



![0_02](assets/fr/02.webp)



Aseta kieli ja näppäimistöasettelu, jota haluat käyttää tietokoneessa.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Salli tai kiellä pääsy **maantieteelliseen sijaintiisi** sovelluksille, jotta ne voivat antaa alueeseesi perustuvia henkilökohtaisia suosituksia.



![0_05](assets/fr/05.webp)



Voit muodostaa yhteyden olemassa olevaan **NextCloud**-tiliisi hakeaksesi tietoja, jotka liittyvät toisessa järjestelmässä käyttämääsi toimistopakettiin.



![0_06](assets/fr/06.webp)



Ohje annetaan, mutta voit sulkea ikkunan, jos haluat ohittaa tämän vaiheen.



![0_08](assets/fr/08.webp)



### Asennuksen käynnistäminen



Napsauta **Activities**-valikkoa ja tutustu järjestelmään esiasennettuihin sovelluksiin ja työkaluihin. Aloita asennus napsauttamalla **Install PureOS**



![0_09](assets/fr/09.webp)



Aseta järjestelmän kieli ja näppäimistöasettelu tarpeen mukaan ja määritä sitten Hard:n levyn osiointitila.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Sinulla on kaksi vaihtoehtoa Hard-levyn osiointiin:




- Poista levy**: Poistaa kaikki Hard-levyltä jo olemassa olevat tiedot, kun haluat asentaa PureOS:n kokonaan.



![0_14](assets/fr/14.webp)





- Manuaalinen osiointi** omien pisteytysten luomiseksi



⚠️ Kun luot manuaalisesti osioita käyttöjärjestelmääsi varten, varmista, että varaat vähintään 2 Gt:n osion PureOS-käyttöä varten ja toisen osion tietoja varten.



![0_15](assets/fr/15.webp)



Aktivoi **levyn salaus**, jos haluat suojata tietosi. Anna vahva, monimutkainen salasana.



Liitä käyttäjä käyttöjärjestelmään määrittelemällä käyttäjänimi ja vähintään 20 merkin pituinen aakkosnumeerinen salasana tietojesi turvallisuuden vahvistamiseksi.



![0_16](assets/fr/16.webp)



Tarkista tekemäsi asetukset ja muuta niitä tarvittaessa.



![0_17](assets/fr/17.webp)



Napsauta **Asenna** ja sitten **Asenna nyt** vahvistaaksesi, että PureOS on asennettu tietokoneellesi.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Kun asennus on valmis, käynnistä tietokone uudelleen valitsemalla **Restart now** -ruutu ja vahvista sitten:




- Kieli.
- Näppäimistön asettelu.
- NextCloud-tilisi (valinnainen).



![0_25](assets/fr/25.webp)



## Päivitykset



Ennen kuin aloitat PureOS:n käytön, on tärkeää päivittää järjestelmäsi. Näin voit hyödyntää uusimpia ominaisuuksia ja tietoturvakorjauksia ja varmistaa paremman vakauden.





- Päivitys Interface-kuvauksen kautta**:


Avaa **Ohjelmisto**-sovellus ja siirry sitten **Päivitykset**-välilehdelle. Käytettävissä olevat päivitykset näytetään automaattisesti. Napsauta **Lataus** ja sitten **Asenna**, kun lataus on valmis.





- Päivitys päätelaitteen kautta**:


Avaa terminaali ja kirjoita seuraava komento päivittääksesi käytettävissä olevien pakettien luettelon:



```shell
sudo apt update
```



Syötä salasanasi ja vahvista. Asenna sitten päivitykset:



```shell
sudo apt full-upgrade
```



## PureOS kehitystä varten



PureOS ei oletusarvoisesti sisällä kaikkia kehitystyössä tarvittavia työkaluja.


Voit asentaa ne nopeasti seuraavalla komennolla:



```shell
sudo apt install build-essential git curl
```



Tämä asentaa **Git**- ja **Curl**-käännöstyökalut, jotka ovat hyödyllisiä useimmissa kehitysympäristöissä.



## PureOS-ympäristö



PureOS erottuu edukseen innovatiivisella lähestymistavallaan todelliseen konvergenssiin: yksi käyttöjärjestelmä takaa sujuvan ja saumattoman toiminnan useilla eri laitteilla, kuten kannettavilla tietokoneilla, tableteilla, minitietokoneilla ja älypuhelimilla.



PureOS-sovellukset on suunniteltu mukautuviksi: ne mukautuvat automaattisesti näytön kokoon ja syöttötilaan (kosketus tai näppäimistö/hiiri). Esimerkiksi GNOME-verkkoselain mukauttaa dynaamisesti Interface:nsa tarjotakseen optimaalisen käyttökokemuksen sekä mobiili- että työpöytälaitteissa.



PureOS sisältää myös **LibreOffice**-toimistopaketin, joka sisältää:





- Writer**: täydellinen tekstinkäsittelyohjelma asiakirjojen luomiseen ja muokkaamiseen.
- Calc**: tehokas taulukkolaskentaohjelma tietojen ja laskelmien hallintaan.
- Impress**: työkalu ammattimaisten esitysten luomiseen.



Tämän ilmaisen paketin avulla voit työskennellä tehokkaasti ilman riippuvuutta teollisoikeudellisista ohjelmistoista.



PureOS tarjoaa yhtenäisen, turvallisen ja joustavan ympäristön, joka perustuu 100-prosenttisesti avoimen lähdekoodin jakeluun, joka takaa täydellisen hallinnan ja yksityisyyden tiukan kunnioittamisen. Sen todellinen konvergenssi helpottaa sellaisten sovellusten luomista, jotka ovat yhteensopivia erityyppisten laitteiden, kuten tietokoneiden, tablettien ja älypuhelinten kanssa, ilman monimutkaisia mukautuksia.



PureOS yksinkertaistaa sovelluskehitystä, testausta ja käyttöönottoa turvallisessa ympäristössä, sillä se tarjoaa natiivin pääsyn tärkeimpiin työkaluihin, vankat paketinhallintajärjestelmät ja runsaan avoimen lähdekoodin ekosysteemin. Sen vakaa arkkitehtuuri ja Commitment-luottamuksellisuus tekevät siitä luotettavan alustan erilaisiin käyttötarkoituksiin, kuten Blockchain-kehitykseen, nopeaan prototyyppien kehittämiseen tai tuotantoympäristöihin.



Tutustu kursseihimme tietoturvan vahvistamisesta ja digitaalisen yksityisyytesi suojaamisesta.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1