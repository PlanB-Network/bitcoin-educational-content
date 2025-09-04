---
name: OPNsense
description: Miten asennan ja määrittelen OPNsense-palomuurin?
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian BURNELin alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___



## I. Esittely



Tässä opetusohjelmassa tarkastelemme OPNsensen avoimen lähdekoodin palomuuria. Tarkastelemme sen tärkeimpiä ominaisuuksia, ennakkoedellytyksiä ja sitä, miten tämä FreeBSD-pohjainen ratkaisu asennetaan.



Ennen kuin aloitat, sinun on hyvä tietää, että **OPNsense ja pfSense ovat molemmat avoimen lähdekoodin palomuureja**, jotka perustuvat FreeBSD:hen. Voidaan sanoa, että pfSense on tavallaan OPNsensen isoveli, sillä jälkimmäinen on vuonna 2015 luotu Fork. Lopuksi on tärkeää huomauttaa, että vuodesta 2017 lähtien **OPNsense on siirtynyt käyttämään HardenedBSD:tä FreeBSD:n sijaan**. HardenedBSD on parannettu versio FreeBSD:stä, jossa on kehittyneitä tietoturvaominaisuuksia



OPNsense erottuu edukseen nykyaikaisemman Interface-käyttäjänsä ja **tiheämmän päivitystiheytensä** ansiosta. OPNsensen päivitysaikatauluun sisältyykin kaksi pääjulkaisua vuodessa, jotka päivitetään noin kahden viikon välein (jolloin syntyy pieniä julkaisuja). Tämä seuranta on erittäin mielenkiintoista verrattuna pfSenseen, jos tarkastelemme näiden ratkaisujen yhteisöversioita.



![Image](assets/fr/050.webp)



## II. OPNsensen ominaisuudet



OPNsense on käyttöjärjestelmä, joka on suunniteltu toimimaan palomuurina ja reitittimenä, mutta sen ominaisuuksia on lukuisia ja niitä voidaan laajentaa asentamalla lisäpaketteja. Se soveltuu tuotantokäyttöön, ja sitä käytetään pääasiassa verkon tietoturvaan ja virranhallintaan.



### A. Tärkeimmät ominaisuudet



Seuraavassa on joitakin OPNsensen tärkeimpiä ominaisuuksia:





- Palomuuri ja NAT**: OPNsense tarjoaa kehittyneet tilatietoiset palomuuritoiminnot, joissa on tilatietoinen suodatus sekä verkon Address-käännösominaisuudet (NAT).





- DNS/DHCP**: OPNsense voidaan määrittää hallitsemaan DNS- ja DHCP-palveluja verkossa. Se voi toimia DHCP-palvelimena, mutta sitä voidaan käyttää myös DNS-resolverina lähiverkon koneille. Myös Dnsmasq on oletusarvoisesti integroitu.





- VPN**: OPNsense tukee useita VPN-protokollia, mukaan lukien IPsec, OpenVPN ja WireGuard, mikä mahdollistaa turvalliset yhteydet etäkäyttöön liikkuviin työasemiin tai toimipisteiden väliseen yhteyteen.





- Verkkovälityspalvelin**: OPNsense sisältää web-välityspalvelimen, jolla voidaan valvoa ja suodattaa Internet-yhteyksiä. Sitä voidaan käyttää myös sisällön suodattamiseen ja verkkokäytön hallintaan.





- Kaistanleveyden hallinta (QoS)**: OPNsense tarjoaa QoS (Quality of Service) -hallintaominaisuuksia, joilla voidaan priorisoida verkkoliikennettä ja hallita paremmin verkon kaistanleveyttä.





- Captive portal**: Tämän ominaisuuden avulla voit hallita käyttäjien pääsyä verkkoon todennussivun kautta (paikallinen pohja, tositteet jne.). Tämä ominaisuus otetaan yleisesti käyttöön julkisissa Wi-Fi-verkoissa.





- IDS/IPS**: OPNsense integroi Suricatan tarjoamaan tunkeutumisen havaitsemis- ja estotoimintoja (IDS/IPS) verkon suojaamiseksi hyökkäyksiltä.





- Korkea käytettävyys (CARP)**: OPNsense tukee CARP-protokollaa (*Common Address Redundancy Protocol*) useiden OPNsense-palomuurien välistä korkeaa käytettävyyttä varten, mikä varmistaa, että palvelu pysyy aktiivisena myös laitteistovian sattuessa.





- Raportointi ja seuranta**: OPNsense tarjoaa reaaliaikaisia raportointi- ja seurantatyökaluja verkon suorituskyvyn seuraamiseen (NetFlow:n avulla) ja mahdollisten ongelmien havaitsemiseen lokien luomisen ansiosta. Tämä sisältää grafiikkaa. Monit-työkalu on integroitu OPNsenseen ja mahdollistaa itse palomuurin valvonnan.



### B. Lisäpaketit



Tämä on vain yleiskatsaus OPNsensen tarjoamista ominaisuuksista. Lisäksi OPNsensen hallintasovelluksen Interface:n kautta käytettävissä olevan **pakettiluettelon** avulla voit **rikastuttaa palomuuria lisätoiminnoilla**. Näihin kuuluvat ACME-asiakas, Wazuh-agentti, NTP Chrony -palvelu ja Caddy käänteisenä välityspalvelimena.



![Image](assets/fr/051.webp)



## III. OPNsense-edellytykset



Ensinnäkin sinun on päätettävä, mihin asennat OPNsensen. Mahdollisia ratkaisuja on useita, kuten asennus:





- Hypervisor virtuaalikoneena, olipa kyseessä Hyper-V, Proxmox, VMware ESXi jne.
- Kone on *paljaan metallin* järjestelmä. Tämä voi olla mini-PC, joka toimii palomuurina.



Voit myös ostaa **OPNsense-telineeseen asennettavan laitteen** verkkokaupastamme.



Sinun on otettava huomioon OPNsensen käyttämiseen tarvittavat laitteistoresurssit. Tämä on esitetty yksityiskohtaisesti [tällä dokumentointisivulla](https://docs.opnsense.org/manual/hardware.html).



**Tuotannon vähimmäis- ja suositellut resurssit:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Lopuksi, **resurssivaatimukset riippuvat ennen kaikkea hallinnoitavien yhteyksien määrästä** ja siten **kaistanleveysvaatimuksista**. Lisäksi on **pidettävä mielessä aktivoitavat ja käytettävät palvelut** (välityspalvelin, tunkeutumisen havaitseminen jne...), sillä ne voivat vaatia paljon suorittimen ja/tai RAM-muistia.



Tarvitset myös OPNsensen asennus-ISO-kuvan, jonka voit ladata [viralliselta verkkosivustolta](https://opnsense.org/download/). Jos haluat asentaa VM:ään, valitse kuvatyypiksi "**dvd**" saadaksesi ISO-kuvan (ja tee sillä mitä haluat...). Jos haluat asentaa käynnistettävän USB-levyn kautta, valitse "**vga**"-vaihtoehto saadaksesi "**.img**"-tiedoston.



![Image](assets/fr/048.webp)



Tarvitset myös tietokoneen OPNsensen hallintaa ja testausta varten.



## IV. Kohdekonfiguraatio



Tavoitteenamme on





- Luo sisäinen virtuaaliverkko (192.168.10.0/24 - LAN)**, josta pääsee Internetiin OPNsense-palomuurin kautta. Tuotantokäytössä tämä voi olla lähiverkko, kaapeli ja/tai Wi-Fi.
- Aktivoi ja määritä NAT**, jotta sisäisen virtuaaliverkon VM:t voivat käyttää Internetiä
- Aktivoi ja määritä OPNsensen** DHCP-palvelin jakamaan IP-konfiguraatio sisäiseen virtuaaliverkkoon liitetyille tuleville koneille
- Määritä palomuuri** siten, että se sallii vain lähtevät lähiverkosta WANiin suuntautuvat HTTP- (80) ja HTTPS-virrat (443).
- Määritä palomuuri** sallimaan virtuaalisen lähiverkon käyttää OPNsenseä DNS-resolverina (53).



Jos käytät Hyper-V-alustaa, saat seuraavan esityksen:



![Image](assets/fr/033.webp)



## V. OPNsense-palomuurin asentaminen



### A. Käynnistettävän USB-levyn valmistelu



Ensimmäinen vaihe on asennusmedian valmistelu: **käynnistettävä USB-levy, jossa on OPNsense**. Tämä on tietysti vapaaehtoista, jos työskentelet virtuaaliympäristössä, mutta joka tapauksessa sinun on ladattava OPNsensen asennuksen ISO-kuva.



Latauksen jälkeen saat **arkiston, joka sisältää kuvan ".img "**-muodossa. Voit **luoda käynnistettävän USB-tikun** eri sovelluksilla, kuten **balenaEtcher**: erittäin yksinkertainen käyttää. Lisäksi sovellus tunnistaa arkistossa olevan kuvan, joten sinun ei tarvitse purkaa sitä etukäteen.





- [Lataa balenaEtcher](https://etcher.balena.io/)



Kun sovellus on asennettu, valitse kuvasi, USB-levysi ja napsauta sitten "Flash!" -painiketta Odota hetki.



![Image](assets/fr/049.webp)



Nyt olet valmis asentamaan.



### B. OPNsense-järjestelmän asentaminen



Käynnistä kone, jossa OPNsense sijaitsee. Sinun pitäisi nähdä alla olevan kaltainen tervetulosivu. Muutaman sekunnin ajan ikkunassa näkyy kuvattu näyttö. Anna prosessin kulkea...



![Image](assets/fr/019.webp)



OPNsense-kuva ladataan koneeseen, jotta järjestelmää voidaan käyttää "**elävässä**" tilassa eli väliaikaisesti muistiin tallennettuna.



![Image](assets/fr/025.webp)



Tämän jälkeen pääset alla olevan kaltaiseen Interface:een. Kirjaudu sisään tunnuksella "**installer**" ja salasanalla "**opnsense**". Huomaa, että näppäimistö on tällä hetkellä **QWERTY**. Tässä vaiheessa **käynnistämme OPNsense-asennusprosessin**.



![Image](assets/fr/026.webp)



Näyttöön tulee uusi ohjattu toiminto. Ensimmäinen vaihe on valita kokoonpanoasi vastaava näppäimistöasettelu. Jos kyseessä on AZERTY-näppäimistö, valitse luettelosta vaihtoehto "**French (accent keys)**" ja kaksoisnapsauta sitten**.



![Image](assets/fr/027.webp)



Toisessa vaiheessa valitaan suoritettava tehtävä. Tässä tapauksessa suoritamme asennuksen käyttäen **ZFS-tiedostojärjestelmää**. Asetu riville "**Asennus (ZFS)**" ja vahvista valinta painamalla **Enter**.



![Image](assets/fr/028.webp)



Valitse kolmannessa vaiheessa "**stripe**", koska koneessamme on **vain yksi levy**: palomuurin tallennustilan ja sen tietojen turvaamiseksi ei ole mahdollista käyttää redundanssia. Tämä on erityisen tärkeää, kun asennetaan fyysiseen koneeseen suojaamaan levyn laitteistovian varalta RAID-periaatteella.



![Image](assets/fr/029.webp)



Vahvista neljäs vaihe yksinkertaisesti painamalla **Enter**.



![Image](assets/fr/030.webp)



Vahvista lopuksi valitsemalla "**YES**" ja painamalla sitten **Enter**-näppäintä.



![Image](assets/fr/031.webp)



Nyt sinun on odotettava, että OPNsense asennetaan... Tämä prosessi kestää noin 5 minuuttia.



![Image](assets/fr/032.webp)



Kun asennus on valmis, voimme vaihtaa "**juurisalasanan**" ennen uudelleenkäynnistystä. Valitse "**Root Password**", paina **Enter** ja syötä salasana "**root**" kahdesti.



![Image](assets/fr/020.webp)



Valitse lopuksi "**Complete Install**" ja paina **Enter**. Käytä tätä tilaisuutta hyväksenne **poistamaan levyke VM:n DVD-asemasta**. VM:n asetuksissa voit myös asettaa ensimmäisen käynnistyksen levylle.



![Image](assets/fr/021.webp)



Virtuaalikone käynnistyy uudelleen ja lataa OPNsense-järjestelmän levyltä, koska olemme juuri asentaneet sen. Kirjaudu sisään "root"-tilillä konsolissa ja uudella salasanallasi (muuten oletussalasana on "**opnsense**").



### D. Verkkoliitäntöjen yhdistäminen



Näyttöön tulee alla oleva näyttö. Valitse "**1**" ja paina **Enter** yhdistääksesi koneen verkkokortit OPNsense-liitäntöihin.



![Image](assets/fr/022.webp)



Ohjattu toiminto pyytää sinua ensin määrittämään linkkien yhdistämisen ja VLANit. Kieltäydy antamalla "**n**" ja vahvista vastauksesi joka kerta painamalla **Enter**. Seuraavaksi sinun on määritettävä kaksi liitäntää "**hn0**" ja "**hn1**" **WANiin** ja **LANiin**. Periaatteessa "**hn0**" vastaa WAN:ia ja toinen Interface LAN:ia.



Näin se toimii:



![Image](assets/fr/023.webp)



Meillä on nyt:





- Interface **LAN**, joka on liitetty verkkokorttiin "**hn1**" ja OPNsensen oletus-IP Address:aan, eli **192.168.1.1/24**.
- Interface **WAN** liittyy verkkokorttiin "**hn0**" ja Address:n IP-osoitteeseen, joka on haettu **DHCP**:n kautta paikallisverkossa (ulkoisen virtuaalikytkimen ansiosta).



Oletusarvoisesti OPNsense-hallinta Interface:een pääsee käsiksi vain LAN Interface:stä, ilmeisistä turvallisuussyistä. Sinun on siis muodostettava yhteys palomuurin Interface:n lähiverkkoon, jotta voit suorittaa hallinnan. Jos tämä ei ole mahdollista, voit väliaikaisesti hallinnoida OPNsenseä WAN-verkosta. Tämä edellyttää palomuuritoiminnon poistamista käytöstä.



Voit tehdä tämän siirtymällä komentotilaan "**8**"-vaihtoehdolla ja suorittamalla seuraavan komennon:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Pääsy OPNsense Interface -hallintajärjestelmään



OPNsense Administration Interface:een pääsee käsiksi HTTPS:n kautta käyttämällä LAN** Interface:n (tai WAN:n) IP Address:ää. Selain vie sinut kirjautumissivulle. Kirjaudu sisään aiemmin valitsemallasi "root"-tilillä ja salasanalla.



![Image](assets/fr/034.webp)



Odota muutama sekunti... Sinua pyydetään seuraamaan ohjattua toimintoa peruskonfiguraation suorittamiseksi. Jatka napsauttamalla "**Seuraava**".



![Image](assets/fr/036.webp)



Ensimmäisessä vaiheessa määritetään isäntänimi, verkkotunnus, valitaan kieli ja määritetään DNS-palvelin tai -palvelimet, joita käytetään nimenmääritykseen. Jos pidät "**Enable Resolver**"-vaihtoehdon, palomuuria voidaan käyttää DNS-resolverina, mikä on hyödyllistä virtuaalisen lähiverkon koneille.



![Image](assets/fr/037.webp)



Siirry seuraavaan vaiheeseen. Ohjattu toiminto antaa sinulle mahdollisuuden **määrittää NTP-palvelimen päivämäärän ja ajan synkronointia varten**, vaikka palvelimet on jo määritetty oletusarvoisesti. Lisäksi on tärkeää valita maantieteellistä sijaintiasi vastaava aikavyöhyke (ellei sinulla ole erityisvaatimuksia).



![Image](assets/fr/038.webp)



Sitten tulee tärkeä vaihe: **Interface WAN:n konfigurointi**. Tällä hetkellä se on konfiguroitu DHCP:hen ja pysyy tässä konfigurointitilassa, ellet halua asettaa staattista IP-osoitetta Address:lle.



![Image](assets/fr/039.webp)



Interface:n WAN-konfiguraatiosivulla sinun on poistettava valinta "**Block access to private networks via WAN**" (**Sulje pääsy yksityisiin verkkoihin WAN:n kautta**), jos WAN-puolen verkko käyttää yksityistä osoitteistusta. Näin on todennäköisesti, jos käytät laboratoriota, ja se voi estää pääsyn Internetiin.



![Image](assets/fr/040.webp)



Seuraavaksi voit **määrittää "root "**-salasanan, mutta tämä on valinnaista, koska olemme jo tehneet sen.



![Image](assets/fr/041.webp)



Jatka loppuun asti aloittaaksesi konfiguraation uudelleenlatauksen. Jos haluat jatkaa hallintaa WANin kautta, käynnistä yllä oleva komento uudelleen, kun tämä prosessi on päättynyt.



![Image](assets/fr/042.webp)



Siinä kaikki!



![Image](assets/fr/035.webp)



### E. DHCP-konfigurointi



Tarkoituksenamme on käyttää OPNsensen DHCP-palvelinta IP-osoitteiden jakamiseen virtuaaliseen lähiverkkoon. Tätä varten meidän on päästävä tähän valikkokohtaan:



```
Services > ISC DHCPv4 > [LAN]
```



**Kuten näet, DHCP on jo oletusarvoisesti käytössä lähiverkossa ** Jos et ole kiinnostunut tästä palvelusta, se kannattaa poistaa käytöstä. Vaikka se on jo käytössä ja haluamme käyttää sitä, on tärkeää tarkistaa sen asetukset.



Voit tarvittaessa muuttaa jaettavien IP-osoitteiden aluetta: **192.168.10.10** - **192.168.10.10.245** nykyisten asetusten mukaan.



![Image](assets/fr/046.webp)



Näemme myös, että kentät "**DNS-palvelimet**", "**Gateway**", "**Domain name**" jne. ovat oletusarvoisesti tyhjiä. Itse asiassa näille eri kentille periytyvät automaattisesti tietyt vaihtoehdot ja oletusarvot. Esimerkiksi DNS-palvelimelle jaetaan Interface LAN:n IP Address, jolloin OPNsense-palomuuria voidaan käyttää DNS-resolverina.



Tallenna kokoonpano tarvittaessa muutosten tekemisen jälkeen.



![Image](assets/fr/047.webp)



DHCP-palvelimen testaamiseksi sinun on liitettävä kone palomuurin lähiverkkoon.



Tämän koneen on saatava IP Address OPNsensen DHCP-palvelimelta, ja koneellamme on oltava pääsy verkkoon. Internet-yhteyden on toimittava. Huomaa, että jos olet poistanut palomuuritoiminnon käytöstä OPNsensea varten WAN-verkosta, tämä poistaa NAT:n käytöstä, jolloin et pääse Internetiin.



**Huomautus**: tällä hetkellä myönnetyt DHCP-vuokrasopimukset näkyvät OPNsense-hallinnan Interface:stä. Mene tätä varten seuraavaan paikkaan: **Palvelut > ISC DHCPv4 > Vuokrasopimukset**.



![Image](assets/fr/045.webp)



### F. NAT- ja palomuurisääntöjen määrittäminen



Hyvä uutinen on se, että voimme nyt käyttää OPNsensen hallintalaitetta Interface lähiverkosta.



```
https://192.168.1.10
```



Kun olet kirjautunut OPNsenseen, tutustutaan NAT-konfiguraatioon. Siirry tähän sijaintiin: **Firewall > NAT > Outbound**. Tässä voit valita lähtevien NAT-sääntöjen automaattisen (oletus) ja manuaalisen luomisen välillä.



Valitse automaattinen tila vaihtoehdon "**Automatic generation of outgoing NAT rules**" kautta ja napsauta "**Save**" (periaatteessa tämä asetus on jo aktiivinen). Automaattisessa tilassa OPNsense luo itse NAT-säännön jokaiselle verkollesi.



![Image](assets/fr/043.webp)



Tällä hetkellä kaikki virtuaaliseen lähiverkkoon **192.168.10.0/24** liitetyt tietokoneet voivat käyttää Internetiä rajoituksetta. Tavoitteenamme on kuitenkin rajoittaa pääsy WAN:iin vain HTTP- ja HTTPS-protokolliin sekä DNS:ään palomuurin Interface LAN:ssa.



Meidän on siis luotava palomuurisäännöt... Selaa valikkoa seuraavasti: **Palomuuri > Säännöt > LAN**.



** Oletusarvoisesti on kaksi sääntöä, jotka sallivat kaiken lähtevän lähiverkkoliikenteen, IPv4 ja IPv6**. Poista nämä kaksi sääntöä käytöstä napsauttamalla Green-nuolta aivan vasemmalla, kunkin rivin alussa.



Luo sitten kolme uutta sääntöä, joilla **LAN-verkko** (eli "**LAN-verkko**") valtuutetaan:





- päästä kaikkiin kohteisiin **HTTP**:n avulla.
- päästä kaikkiin kohteisiin **HTTPS**:llä.
- pyytää **OPNsense**:tä **Interface LAN**:ssaan (eli "**LAN Address**") **DNS-protokollan** kautta (tämä tarkoittaa palomuurin käyttämistä DNS:nä), tai muuten valtuuttaa DNS-resolverin IP:n Address:n kautta.



Tästä saadaan seuraava tulos:



![Image](assets/fr/044.webp)



Nyt on enää napsautettava "**Valtaa muutokset**", jotta uudet palomuurisäännöt siirtyvät tuotantoon. **Huomaa, että kaikki virrat, joita ei ole nimenomaisesti valtuutettu, estetään oletusarvoisesti



LAN-kone voi käyttää Internetiä HTTP- ja HTTPS-yhteyden avulla. Kaikki muut protokollat estetään.



![Image](assets/fr/018.webp)



## IV. Päätelmät



Tämän oppaan avulla voit asentaa OPNsensen ja aloittaa heti. OPNsense tarjoaa laajan valikoiman ominaisuuksia verkkoliikenteen tehokkaaseen turvaamiseen ja hallintaan, ja se soveltuu käytettäväksi ammattikäyttöön.



Tämä asennus on vasta alkua: voit vapaasti tutkia valikoita ja määrittää muita ominaisuuksia OPNsensen mukauttamiseksi tarpeisiisi.