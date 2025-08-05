---
name: Pi-Hole
description: Mainosten esto koko verkostossasi
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian Ducheminin alkuperäiseen sisältöön, joka on julkaistu [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___



## I. Esittely



Olemme kaikki tehneet sen heti, kun käynnistämme suosikkiselaimemme: asennamme **mainosestimen** (adblocker). Kuitenkin, kun käytät TV-selainta tai Android-laitetta jne.... On hieman hankalampaa löytää jotain toimivaa. Ja jos talossa on useampi kuin yksi laite, no, sinun täytyy toistaa toimenpide jokaiselle selaimelle!



Tässä opetusohjelmassa ratkaisemme yksinkertaisen ongelman**: tarjoamme mainosten eston kaikille verkkomme koneille ja hallitsemme sitä keskitetysti.**



Käytämme tähän tarkoitukseen kehitettyä työkalua: **Pi-Hole**



Pi-Hole on DNS-nielu. Se käyttää laitteidesi tekemiä DNS-pyyntöjä validoidakseen tai kieltääkseen liikenteen, mikä suojaa sinua osoitteilta ja verkkotunnuksilta, joiden tiedetään levittävän mainoksia, haittaohjelmia ja niin edelleen.



DNS on lyhenne sanoista Domain Name System. Mikä on verkkotunnus? No, "it-connect.fr" on vain yksi esimerkki. Verkkotunnus on yhden tai useamman resurssin yksilöllinen tunniste, jota yleensä hallinnoi yksi taho.



Koneen nimeä ja verkkotunnusta kutsutaan FQDN:ksi (*Fully Qualified Domain Name*). Sen avulla voit tavoittaa tietyn koneen vain "kutsumalla" sitä. Kun esimerkiksi kirjoitat "www.trucmachin.com", kutsut itse asiassa konetta "www", joka kuuluu verkkotunnukseen "trucmachin.com".



Paitsi että tietokoneemme eivät ymmärrä ihmisten kieltä, vaan ne ymmärtävät vain binääritietoja, joten ne tarvitsevat IP Address:n, joka vastaa puhelinnumeroa, tavoittaakseen verkkosivuston.



Aina kun syötät selaimeen verkkosivuston nimen tai napsautat linkkiä, tietokoneesi kysyy ensin DNS-palvelimelta nimeä vastaavaa IP Address:tä.



**Pi-Hole tarkastaa nämä pyynnöt (niitä on satoja joka päivä!) ja estää automaattisesti ne, joiden tiedetään isännöivän mainoksia tai jopa haitallisia tiedostoja



## II. Pi-Holen asentaminen



Kun nimi on Pi-Hole, saatat olettaa, että tarvitset Raspberry-Pi:n.... Mutta se ei ole aivan totta. **Pi-Hole voidaan asentaa mihin tahansa Linux-tietokoneeseen (Debian, Fedora, Rocky, Ubuntu jne.)



Toisaalta sinun on muistettava, että **Tämä laite joutuu toimimaan 24 tuntia vuorokaudessa yksinkertaisesta syystä: ilman DNS:ää ei ole internetiä!** Vadelma on siis hyvä idea, koska se ei kuluta juuri lainkaan energiaa.



Asennusta varten yhdistä Linux-koneeseesi SSH:n kautta ja kirjoita seuraava komento "*root*"-käyttäjänä:



```
curl -sSL https://install.pi-hole.net | bash
```



> **Huomautus**: Normaalioloissa ei ole suositeltavaa "hakkeroida" skriptiä tietämättä ensin, mitä se tekee. Jos et ole varma, käy sivulla selaimella tai lataa sisältö tiedostona.
>


> **Huomaa: Debian 11:n minimaalisissa versioissa Curl ei ole asennettu, joten sinun on asennettava se manuaalisesti komennolla **apt-get install curl** ennen yllä olevan komennon kirjoittamista.

Kun komentosarja on suoritettu, suoritetaan joukko testejä, ja itse asennus hoituu itsestään:



![Image](assets/fr/019.webp)



Asennus Pi-Hole



Kun asennus on valmis, pääset tähän näyttöön:



![Image](assets/fr/020.webp)



Pi-Hole-käynnistysnäyttö



> **Huomautus**: jos käytät DHCP:tä koneellasi, saat tästä varoitusviestin. Tietenkin suosittelemme vahvasti, että määrität koneellesi kiinteän IP-osoitteen, jotta sitä voidaan käyttää oikein.

Tämän näytön jälkeen saat muutaman informaatioviestin, minkä jälkeen pääset ohjatun konfiguroinnin vaiheeseen, jossa kysytään ensin, mille DNS-palvelimelle Pi-Hole välittää pyynnöt. Omalta osaltani olen valinnut Quad9:n, jolla on käyttäjien yksityisyyden suojaa koskeva peruskirja.



![Image](assets/fr/021.webp)



DNS-valinta - Pi-Hole



> **Huomaa: jos olet yrityksessä, nykyinen DNS-palvelimesi on todennäköisesti Active Directory -toimialueen ohjain. Mutta ei hätää, voit myöhemmin määrittää ehdollisen uudelleenohjauksen valitsemallesi toimialueelle. Tavallisesti voit ohjata kaikki paikallista toimialuettasi koskevat pyynnöt DNS-palvelimelle.

Huomaat, että joissakin vaihtoehdoissa on DNSSEC-vaihtoehto. Periaatteessa DNS-protokolla ei ole suojattu (sitä ei aikanaan suunniteltu tätä silmällä pitäen). DNSSEC ratkaisee tämän ongelman lisäämällä Layer-turvallisuuden salauksen ja allekirjoitusten avulla, kuten vastaavassa artikkelissa selitetään: [DNS Security](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Jokainen mainosten estojärjestelmä perustuu yhteen tai useampaan luetteloon tehdäkseen työnsä. Pi-Hole sisältää vakiona yhden listan, joten valitse se ja lisää myöhemmin lisää.



![Image](assets/fr/022.webp)



Tule kysymykseen Interface-verkkoa koskevasta kysymyksestä, sen asentaminen on vapaaehtoista, koska työkalulla on oma komentorivi hallintaa ja visualisointia varten. Mutta tämä Interface on melko miellyttävä ja hyvin tehty, joten suosittelen, että asennat sen samalla:



![Image](assets/fr/023.webp)



Jos asennat Pi-Holen koneelle, jossa on jo Web-palvelin, voit vastata "ei" seuraavaan kysymykseen. Huomaa kuitenkin, että PHP ja useita moduuleja tarvitaan, jotta tämä toimisi. Muussa tapauksessa **lighttpd asennetaan kaikkine tarvittavine moduuleineen**.



![Image](assets/fr/024.webp)



Tämän jälkeen sinulta kysytään, haluatko tallentaa DNS-pyyntöjä. **Jos haluat pitää historiatietoja, aseta tähän kyllä; muuten aseta tähän ei, mutta menetät osan toiminnoista** (katso seuraava ruutu).



![Image](assets/fr/025.webp)



Interface-verkkoa varten Pi-Hole käyttää omaa FTLDNS-toimintoa, joka tarjoaa API:n ja tuottaa tilastoja DNS-pyynnöistä. Tämä toiminto voi sisältää "yksityisyys"-tilan, joka peittää pyydetyt verkkotunnukset, pyynnön takana olevat asiakkaat tai molemmat. Tämä on kätevää, jos haluat tehdä valvontaa loukkaamatta ihmisten yksityisyyttä tai jos haluat yksinkertaisesti noudattaa asiaankuuluvia säännöksiä, jos käytät sitä julkisessa verkossa.



![Image](assets/fr/026.webp)



Yksityisen elämäntavan valinta



Kun tähän viimeiseen kysymykseen on vastattu, skripti tekee sen, mitä sen pitääkin: lataa GitHub-tietovarastot ja konfiguroi Pi-Hole. Asennuksen lopussa näytetään yhteenvetoruutu, jossa on tärkeät tiedot:



![Image](assets/fr/027.webp)



Asennuksen yhteenvetonäyttö



Merkitse muistiin Interface:n verkkosalasana ja verkkotiedot. Nyt on aika määrittää DHCP-palvelu nykyisessä sijainnissamme.



## III. DHCP-konfigurointi



Toimiakseen Pi-Hole joutuu "ratkaisemaan" asiakkaiden DNS-pyynnöt, joten niiden on tiedettävä, että Pi-Hole on se, jolle ne pitää lähettää. Tähän on useita tapoja:





- Muokkaa DNS-asetuksia DHCP-palvelimessa (esim. Boxissa)
- Poista tämä palvelin käytöstä ja käytä Pi-Holen tarjoamaa palvelinta
- Muokkaa manuaalisesti jokainen laite käyttämään Pi-Holea DNS:nä



Itse valitsen ensimmäisen ratkaisun. Todennäköisesti **sinulla on DHCP-palvelin siellä missä olet** (yleensä boxisi). Joten ei tarvitse vaivautua.



Koska eri operaattoreiden laatikoiden (joita en tunne kaikkia) ja niiden, joilla on oma reititin, välillä on paljon mahdollisuuksia, en aio antaa kuvakaappausta näistä muutoksista. Joka tapauksessa sinun on mentävä DHCP-asetuksiin ja muutettava "DNS"-parametri niin, että se sisältää Pi-pistokkeesi IP Address:n.



Kun tämä on tehty, jos jokin laite on kytketty päälle aiemmin, ne ovat säilyttäneet vanhat asetukset, joten sinun on käynnistettävä konfigurointipyyntö uudelleen.



Windows-työasemilla komentorivillä :



```
ipconfig /renew
```



Linux-työasemalla :



```
dhclient
```



Kaikki muut laitteet on kytkettävä pois päältä ja uudelleen päälle.



Heidän pitäisi siis saada oikeat parametrit tarkistettavaksi:



```
ipconfig /all
```



DNS-kentässä pitäisi olla Pi-Aukon Address, minun tapauksessani 192.168.1.42 :



![Image](assets/fr/029.webp)



## IV. Interface web Pi-Hole -verkon käyttö



Hallinnan helpottamiseksi **Pi-Hole** hyötyy hyvin suunnitellusta Interface-verkkopalvelusta Interface. Käyttäjäystävällinen ja helppokäyttöinen, sen avulla voit :





- Tarkastele reaaliaikaisesti pyyntöjen, estettyjen pyyntöjen jne. määrää.
- Hallitse valkoista ja mustaa listaa
- Lisää staattisia merkintöjä, peitenimiä jne.
- Lisää luetteloita
- Ja monia muita toimintoja!



Omalta osaltani aion lisätä estoluettelon. Kuten edellä mainittiin, vain yksi lista asennettiin samaan aikaan kuin Soft. Mainossivustoja varten on olemassa monia listoja, mutta on parasta valita ainakin yksi, joka koskee juuri sitä maata, jossa asut. Yksi tunnetuimmista listoista on **EasyList**, ja yksi niistä on Ranskaa koskeva: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Voit lisätä sen luomalla ensin yhteyden Interface:n ylläpitäjään: **http://<ip_du_PiHole>/admin**



Järjestelmänvalvojan salasana on jo luotu (katso asennuksen lopun kuvakaappaus), joten sinun tarvitsee vain syöttää se päästäksesi Interface:een:



![Image](assets/fr/030.webp)



Interface alkaen Pi-Hole



Näemme esimerkiksi, että Pi-Holeen on kytketty kaksi asiakasta, että se on käsitellyt 442 pyyntöä ja että niistä 8 on estetty. Nämä kuvaajat voivat olla hyvä tietolähde erityisesti ammattikäytössä.



Jos haluat lisätä listamme, siirry "**Ryhmien hallinta**"- ja "**Listat**"-valikkoihin:



![Image](assets/fr/031.webp)



Näemme ensimmäisen luettelomme "**StevenBlack**", lisätäksesi oman, kopioi linkki, jonka annoin sinulle edellä ja lisää se kenttään "**Address**", kuvaus, päätän laittaa luettelon nimen:



![Image](assets/fr/032.webp)



Luettelon lisääminen Pi-Holessa



Sinun tarvitsee vain klikata "**Lisää**" lisätäksesi sen. Sen aktivoimiseksi meidän on suoritettava lisävaihe "varoittaaksemme" Pi-Holea ottamaan tämän luettelon haltuunsa. Voit tehdä tämän :





- Käytä joko sisäänrakennettua komentoriviä
- Joko Interface web



Itse valitsin toisen vaihtoehdon, koska jos olet katsonut tarkkaan, linkki PHP-skriptiin, joka suorittaa päivityksen, on suoraan sivulla, jolla olemme (sana "online"). Sinun tarvitsee siis vain klikata sitä, jolloin pääset sivulle, jossa on vain yksi vaihtoehto:



![Image](assets/fr/033.webp)



Sivu näyttää skriptin tuloksen sen jälkeen, kun se on valmis, mikä tarkoittaa, että luettelo on otettu huomioon (ellei virheilmoitusta tietenkään näytetä).



Kuten tämän ohjeen alussa kerrottiin, Pi-Hole antaa sinulle myös mahdollisuuden **estää verkkotunnukset, joiden tiedetään levittävän haittaohjelmia. Tämän ominaisuuden vahvistamiseksi ehdotan, että lisäät myös Abuse.ch**:n jakaman säännöllisesti päivitetyn verkkotunnusluettelon, joka vahvistaa merkittävästi verkkosi turvallisuutta ja joka on saatavilla osoitteessa [tämä Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Voit tietysti lisätä mitä tahansa luetteloita, joita pidät merkityksellisinä, tai hallita mustaa listaa manuaalisesti mustan listan valikosta.



## V. Pi-Hole-testit



Nyt kun kaikki on valmista, sinun tarvitsee vain testata ratkaisu ja varmistaa, että se toimii oikein.



Yritän esimerkiksi tavoittaa verkkotunnuksen *http://admin.gentbcn.org/*, joka on Abuse.ch-listalla, koska sen tiedetään isännöivän haittaohjelmia:



![Image](assets/fr/034.webp)



Ilmeisesti minut on estetty jossakin. Varmistaaksemme, että Pi-Hole on tehnyt työnsä, voimme tarkistaa kyselylokin Interface-verkon "Query Log" -osasta, että kyseessä on listamerkinnän esto:



![Image](assets/fr/035.webp)



## VI. Päätelmät



Tässä ohjeessa näytämme, miten voit määrittää DNS-palvelimen, joka ei ainoastaan poista suurinta osaa mainoksista selaamismukavuutesi kannalta, vaan myös lisää **turvallisuuden Layer estämällä phishing- ja haittaohjelmia levittävät verkkotunnukset**.



Kaikki ovat ilmaisia ja taloudellisia, jos ne asennetaan Raspberry-Pi:hen (virrankulutuksen kannalta).