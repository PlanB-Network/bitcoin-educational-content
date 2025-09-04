---
name: WireGuard
description: WireGuard VPN:n määrittäminen Debianissa ja Windowsissa
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian BURNELin alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___



## I. Esittely



Tässä oppaassa opimme, miten konfiguroit VPN:n, joka perustuu WireGuardiin, ilmaiseen, avoimen lähdekoodin VPN-ratkaisuun, joka parantaa suorituskykyä tietoturvaa unohtamatta.



WireGuard on suhteellisen tuore ratkaisu, joka on ollut saatavilla vakaana versiona maaliskuusta 2020 lähtien, ja sillä on ollut kunnia olla integroituna suoraan **Linux-ytimeen versiosta 5.6** lähtien. Tämä ei estä sitä käyttämästä sitä vanhemmista Linux-jakeluista, jotka käyttävät eri versiota ytimestä. Verrattuna OpenVPN:n ja IPSecin kaltaisiin ratkaisuihin WireGuard on yksinkertaisempi käyttää ja paljon nopeampi, kuten näemme tämän artikkelin lopussa.



Joitakin WireGuardia koskevia keskeisiä seikkoja:





- Yksinkertainen, kevyt ja erittäin tehokas!
- Vain UDP-toiminto (mikä voi olla haitta tiettyjen palomuurien läpi kuljettaessa)
- Toimii pikemminkin peer-to-peer- kuin asiakas-palvelin-mallilla
- Tunnistautuminen avaimella Exchange, samalla periaatteella kuin SSH yksityisillä/julkisilla avaimilla
- Useiden algoritmien käyttö: symmetrinen salaus ChaCha20:lla, viestin todennus Poly1305:llä sekä muut algoritmit, kuten Curve25519, BLAKE2 ja SipHash24
- Tukee sekä IPv4- että IPv6-verkkoja
- Monialustainen: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (ja toteutettu ProtonVPN:ssä)
- Vain 4 000 koodiriviä, kun muissa ratkaisuissa koodirivejä on satoja tuhansia



Kryptografian osalta käytetyt algoritmit on valittu käsin, tarkastettu useilla eri tavoilla ja tutkittu alan erikoistuneiden turvallisuustutkijoiden toimesta.



Hankkeen virallinen verkkosivusto: [wireguard.com](https://www.wireguard.com/)



Oletko vakuuttunut tästä ratkaisusta tämän johdannon lukemisen jälkeen? Ei muuta kuin lukemaan eteenpäin!



## II. Laboratorion WireGuard-kaavio



Ennen kuin esittelen WireGuardin käyttöönottoa koskevan laboratorion, sinun on hyvä tietää, että voit kuvitella **käyttäväsi WireGuardia kahden etäinfrastruktuurin yhdistämiseen**, mutta myös **liittääksesi etäasiakkaan infrastruktuuriin, kuten yritysverkkoon tai kotiverkkoon**. Tämä on samassa hengessä kuin OpenVPN:n kanssa, kuten näimme äskettäin opetusohjelmassa "[OpenVPN on Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Jos WireGuardia ei ole asennettu suoraan reitittimeen tai palomuuriin, kuten OpenWRT:n kanssa on mahdollista, sinun on määritettävä porttien välitys, jotta virtaus saavuttaa WireGuardin parin.



![Image](assets/fr/034.webp)



Nyt kerron teille laboratoriostani ja siitä, mitä aiomme tehdä tänään.



Aion käyttää Debian 11 -konetta WireGuard-palvelimena ja Windows-asiakasta WireGuard VPN -asiakkaana. On tosin hieman harhaanjohtavaa puhua asiakas-palvelin-suhteesta, koska **WireGuard toimii "peer-to-peer "** -mallilla. Se on hieman harhaanjohtava nimitys, kun yrität luoda "client-to-site"-yhteyttä. Sanotaan sen sijaan, että minulla on kaksi paria tai **kaksi WireGuard-yhteyspistettä**, jos haluat: toinen Debian 11:ssä ja toinen Windowsissa.



Nämä kaksi paria voivat kommunikoida keskenään molempiin suuntiin, mikä tarkoittaa, että Windows-koneestani pääsen Debian 11 -koneen etälähiverkkoon ja päinvastoin: kaikki riippuu tunnelin ja WireGuard-vertaisverkon palomuurin konfiguraatiosta.



Tässä esimerkissä keskityn seuraavaan tapaukseen: **Haluan päästä kotiverkkooni yhdistetystä Windows Peer 1 -tietokoneestani yritysverkkoon, jotta pääsen yrityksen palvelimille WireGuard VPN-tunnelin kautta**. Tämä antaa seuraavan kaavion:



![Image](assets/fr/035.webp)



IP-osoitteiden osalta tämä antaa:





- Kotiverkko**: 192.168.1.0/24
- Yritysverkko**: 192.168.100.0/24
- WireGuard-tunneliverkko**: 192.168.110.0/24


+ Peer 1:n (Windows) IP Address tunnelissa: 192.168.110.2/24


+ Peer 2:n (Debian) IP Address tunnelissa: 192.168.110.121/24



Siinä kaikki! Aloitetaan konfigurointi!



**Huomaa: oletusarvoisesti WireGuard toimii UDP-tilassa **portissa 51820**.



## III WireGuard-palvelimen asennus ja konfigurointi



Käytän tässä ohjeessa Windows-koneesta termiä "asiakas" ja Debian-koneesta termiä "palvelin", koska vaikka kyseessä on vertaisverkkopalvelu, se tuntuu mielekkäämmältä.



### A. WireGuardin asentaminen Debian 11:een



WireGuardin asennuspaketti on saatavilla Debian 11:n virallisissa arkistoissa, joten meidän tarvitsee vain päivittää pakettien välimuisti ja asentaa se:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



WireGuard-palvelinosa asennetaan, samoin kuin erilaisia työkaluja, jotka antavat pääsyn hyödyllisiin komentoihin kokoonpanon hallintaa varten.



### B. Interface WireGuardin asentaminen



Käyttämällä **komentoa "wg "** meidän on luotava generate yksityinen avain ja julkinen avain: ne ovat välttämättömiä kahden parin, eli palvelimen ja asiakkaan (joka tarvitsee myös avainparin), välisessä todennuksessa.



Luomme yksityisen avaimen "**/etc/wireguard/wg-private.key**" ja julkisen avaimen "**/etc/wireguard/wg-public.key**" tällä komentosarjalla:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Julkisen avaimen arvo palautetaan konsoliin. WireGuardin konfigurointitiedostoon on **lisättävä yksityisen avaimen arvo**. Voit hakea tämän arvon syöttämällä alla olevan komennon ja kopioimalla arvon:



```
sudo cat /etc/wireguard/wg-private.key
```



On aika luoda konfiguraatiotiedosto osoitteeseen "**/etc/wireguard/**". Voimme esimerkiksi nimetä tämän tiedoston nimeksi "**wg0.conf**", jos ajattelemme, että WireGuardiin liitetty Interface-verkko on "wg0", samalla periaatteella kuin esimerkiksi "eth0".



```
sudo nano /etc/wireguard/wg0.conf
```



Tähän tiedostoon on ensin lisättävä seuraava sisältö (palaamme täydentämään sitä myöhemmin):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Jaksoa `[Interface]` käytetään palvelinosan ilmoittamiseen. Tässä on joitakin tietoja:





- Address**: VPN-tunnelissa olevan Interface WireGuardin IP Address (eri aliverkko kuin etälähiverkko)
- SaveConfig**: konfiguraatio tallennetaan (ja suojataan) niin kauan kuin Interface on aktiivinen
- ListenPort**: WireGuardin kuunteluportti. Tässä tapauksessa 51820 on oletusportti, mutta voit muokata sitä
- PrivateKey**: palvelimen yksityisen avaimen arvo (*wg-private.key*)



Tallenna tiedosto ja sulje se. Komennolla "**wg-quick**" voimme käynnistää tämän Interface:n määrittämällä sen nimen (wg0, koska tiedoston nimi on wg0.conf):



```
sudo wg-quick up wg0
```



Jos luetat Debian 11 -palvelimesi IP-osoitteet, näet uuden Interface:n nimeltä "wg0", jonka IP Address on määritelty konfigurointitiedostossa:



```
ip a
```



![Image](assets/fr/027.webp)



Samassa hengessä voimme näyttää Interface:n "wg0"-konfiguraation komennolla "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Lopuksi meidän on aktivoitava Interface wg0 WireGuardin automaattinen käynnistys:



```
sudo systemctl enable wg-quick@wg0.service
```



Jätämme toistaiseksi sivuun WireGuardin palvelinpuolen konfiguroinnin.



### C. Ota käyttöön IP-tiedonsiirto



Jotta Debian 11 -koneemme voi **reitittää paketteja eri verkkojen välillä (kuten reititin)**, eli VPN-verkon ja paikallisverkon välillä, meidän on otettava käyttöön [IP Forwarding] (https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Oletusarvoisesti tämä ominaisuus on poistettu käytöstä.



Muokkaa tätä asetustiedostoa:



```
sudo nano /etc/sysctl.conf
```



Lisää seuraava direktiivi tiedoston loppuun ja tallenna:



```
net.ipv4.ip_forward = 1
```



Siinä kaikki.



### D. Ota IP-maskeri käyttöön



Jotta palvelimemme reitittää paketit oikein ja jotta Windows-kone pääsee etälähiverkkoon, meidän on aktivoitava IP Masquerade Debian-palvelimessamme. Tämä on eräänlainen NAT-aktivointi. Suoritan tämän konfiguroinnin Linux-palomuurissa UFW:n kautta, jota olen tottunut käyttämään ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Jos sinulla ei vielä ole UFW:tä ja haluat asentaa sen (voit käyttää myös Nftablesia), aloita asentamalla:



```
sudo apt install ufw
```



Ensinnäkin sinun on otettava SSH käyttöön, jotta et menetä etäpalvelimen hallintaa (mukauta porttinumeroa):



```
sudo ufw allow 22/tcp
```



UDP-portti 51820 on myös hyväksyttävä, koska käytämme sitä WireGuardia varten (mukauta jälleen porttinumero):



```
sudo ufw allow 51820/udp
```



Seuraavaksi jatkamme IP-masquerade-ominaisuuksien määrittämistä. Tätä varten meidän on haettava lähiverkkoon liitetyn Interface:n nimi. Jos et tiedä nimeä, suorita "ip a" nähdäksesi kortin nimen. Minun tapauksessani se on kortti "**ens192**".



![Image](assets/fr/036.webp)



Käytämme tätä tietoa. Muokkaa seuraavaa tiedostoa:



```
sudo nano /etc/ufw/before.rules
```



Lisää nämä rivit tiedoston loppuun, jotta voit **aktivoida Interface ens192:n IP-masquerade** (mukauta Interface:n nimi) paikallisen palomuurin NAT-taulukon POSTROUTING-merkkijonoon:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Kuvassa näkyy:



![Image](assets/fr/037.webp)



Pidä tämä asetustiedosto auki ja jatka seuraavaan vaiheeseen. 😉 



### E. WireGuardin Linux-palomuurin konfigurointi



Samassa konfigurointitiedostossa ilmoitetaan edelleen yritysverkko "192.168.100.0/24", jotta voimme ottaa siihen yhteyttä. Tässä on kaksi lisättävää sääntöä (mieluiten "*# ok icmp code for FORWARD*" -kohdan jälkeen, jotta säännöt voidaan ryhmitellä yhteen):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Jos haluat valtuuttaa vain yhden isännän, esimerkiksi "192.168.100.11", se on helppoa:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Nyt voit tallentaa tiedoston ja sulkea sen. Jäljellä on enää UFW:n aktivointi ja palvelun uudelleenkäynnistys, jotta muutokset tulevat voimaan:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Debian-palvelimen kokoonpanon ensimmäinen osa on nyt valmis.



## IV. WireGuard-asiakasohjelma Windowsille



WireGuard-asiakasohjelma on saatavilla Windowsille, macOS:lle, Androidille jne... Tämä on loistava uutinen. Kaikki lataukset ovat saatavilla tällä sivulla: [WireGuard Client](https://www.wireguard.com/install/). Tässä esimerkissä aion asentaa asiakkaan Windowsissa. Jos haluat asentaa WireGuard-asiakkaan Linuxissa, noudata samaa periaatetta kuin luodessasi wg0.conf-tiedoston Debian-koneeseen (ilman NATia jne.).



### A. WireGuardin Windows-asiakasohjelman asentaminen



Kun olet ladannut suoritettavan tiedoston tai MSI-paketin, asennus on suoraviivaista: käynnistä vain asennusohjelma, ja... voilà, se on valmis! 🙂 !



![Image](assets/fr/038.webp)



### B. Luo WireGuard-profiili



Aloita avaamalla ohjelmisto uuden tunnelin luomiseksi. Napsauta tätä varten "**Lisää tunneli**"-painikkeen oikealla puolella olevaa nuolta ja napsauta "**Lisää tyhjä tunneli**"-painiketta.



![Image](assets/fr/028.webp)



Määritysikkuna avautuu. Aina kun uusi tunnelikokoonpano luodaan, WireGuard luo kyseiselle kokoonpanolle ominaisen yksityisen/julkisen avainparin. **Tässä konfiguraatiossa meidän on ilmoitettava "peer" eli etäpalvelin:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Meidän on täydennettävä tämä konfiguraatio, erityisesti ilmoitettava Interface:n IP Address (*Address*), mutta myös ilmoitettava etä-WireGuard-palvelin [Peer]-lohkon kautta. Alla olevan kuvan pitäisi muistuttaa sinua Linux-palvelimen puolella luomastamme konfigurointitiedostosta.



Aloitetaan lohkosta `[Interface]` lisäämällä IP Address "**192.168.110.2**"; muista, että palvelimella on IP Address "**192.168.110.121**" tässä verkkosegmentissä. Näin saadaan:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Seuraavaksi meidän on ilmoitettava "Peer"-lohko, jolla on kolme ominaisuutta, mikä johtaa tähän kokoonpanoon:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



Kuvissa:



![Image](assets/fr/029.webp)



** Muutama selitys [Peer]-lohkosta:





- PublicKey**: tämä on WireGuard Debian 11 -palvelimen julkinen avain (saat sen arvon komennolla "*sudo wg*")
- AllowedIPs**: nämä ovat IP-osoitteita / aliverkkoja, joihin pääsee tämän WireGuard VPN -verkon kautta, tässä tapauksessa WireGuard VPN:n oma aliverkko (*192.168.110.0/24*) ja etälähiverkko (*192.168.100.0/24*)
- Endpoint**: tämä on Debian 11 -isäntäkoneen IP Address, koska tämä on WireGuard-yhteyspisteemme (sinun on määritettävä julkinen IP Address)



Kirjoita lopuksi nimi kenttään "**Name**" (ilman välilyöntejä) ja kopioi ja liitä asiakkaan julkinen avain, sillä meidän on ilmoitettava se palvelimella. Napsauta "**Register**".



### C. Ilmoita asiakas WireGuard-palvelimelle



On aika palata Debian-palvelimelle ja ilmoittaa "**Peer**", eli Windows-tietokoneemme, WireGuard-konfiguraatiossa. Ensinnäkin meidän on **pysäytettävä Interface "wg0"**, jotta voimme muuttaa sen konfiguraatiota:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Muokkaa seuraavaksi aiemmin luotua asetustiedostoa:



```
sudo nano /etc/wireguard/wg0.conf
```



Tässä tiedostossa lohkon `[Interface]` jälkeen on ilmoitettava lohko `[Peer]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Tämä [Peer]-lohko sisältää Windows 10 -tietokoneen julkisen avaimen (**PublicKey**) ja tietokoneen Interface:n IP Address:n (**AllowedIPs**): palvelin kommunikoi tässä WireGuard-tunnelissa vain ottaakseen yhteyttä Windows-asiakkaaseen, mistä johtuu arvo "**192.168.110.2/32**".



Tiedosto täytyy vain tallentaa (*CTRL+O, sitten Enter ja sitten CTRL+X Nanossa*). Käynnistä Interface "wg0" uudelleen:



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Voit tarkistaa, että vertaisvertaisilmoitus toimii, käyttämällä tätä komentoa:



```
sudo wg show
```



Kun etäisäntä on muodostanut WireGuard-yhteyden, sen IP Address siirretään "päätepiste"-arvoon.



![Image](assets/fr/033.webp)



Lopuksi suojaamme konfiguraatiotiedostot root-käyttäjän pääsyn rajoittamiseksi:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Ensimmäinen WireGuard-yhteys



Nyt kun kokoonpano on valmis, voimme käynnistää sen Windows-tietokoneesta. Napsauta "**WireGuard**"-asiakasohjelmassa "**Activate**"-painiketta: yhteys muuttuu "Off"-asetuksesta "On"-asetukseksi, mutta se ei tarkoita, että se toimii. Kaikki riippuu siitä, onko konfiguraatiosi oikea vai ei. **Kun yhteys on muodostettu, kaksi konettamme kommunikoivat kummallekin puolelle määritetyn Interface WireGuardin kautta!



![Image](assets/fr/030.webp)



Ongelmatilanteessa tämä näkyy "**Logbook**"-välilehdellä. Molemmat isännät lähettävät Exchange-paketteja säännöllisesti tarkistaakseen yhteyden tilan, mistä johtuvat "*Vastaanottaa keepalive-pakettia vertaisohjelmalta 1*"-viestit.



![Image](assets/fr/031.webp)



Jos WireGuardin "**Journal**"-välilehdellä näkyy alla olevan kaltainen viesti, sinun on tarkistettava, että molempien osapuolten ilmoittamat julkiset avaimet ovat oikein.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Etätietokoneestani voin pingata palvelimen puolella olevan Interface WireGuardin IP Address:n sekä etäverkossa olevan isäntäkoneen.



![Image](assets/fr/032.webp)



### E. Suorituskyky: WireGuard



Pystyin WireGuard VPN:ään liitetystä etätietokoneestani käyttämään tiedostopalvelinta ja siirtämään tiedoston [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/) kautta nähdäkseni siirtonopeuden. **WireGuardin avulla maksimissaan noin 45 Mb/s, mikä on hienoa, koska käytän WiFiä



![Image](assets/fr/025.webp)



Samoissa olosuhteissa, mutta tällä kertaa OpenVPN-yhteyden kautta (UDP:nä) ja samalla toiminnolla, läpäisykyky on täysin erilainen: noin 3 MB/s. Ero on ilmeinen!



![Image](assets/fr/026.webp)



Tämä on mielenkiintoista, sillä jos esimerkiksi vaihdat WiFi-yhteydestä 4G/5G-yhteyteen, yhteyden muodostaminen uudelleen on niin nopeaa, ettei keskeytystä huomaa.



### F. Bonus: koko tunnelin WireGuard



Nykyisessä kokoonpanossa osa liikenteestä kulkee VPN:n kautta ja osa asiakkaan Internet-yhteyden kautta, mukaan lukien Internet-selailu. Jos haluamme siirtyä WireGuardin **täyden tunnelin tilaan**, jolloin kaikki kulkee VPN-tunnelin kautta, meidän on tehtävä muutama muutos kokoonpanoon.....



Ensin sinun on asennettava resolvconf-paketti:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Kun tämä on tehty, sinun on muutettava Debian-koneen "wg0.conf"-profiilia: pysäytä Interface, muuta sitä ja käynnistä uudelleen.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Seuraavaksi **[Interface]-lohkossa lisätään käytettävä DNS-palvelin**. Minun tapauksessani se on laboratorioni verkkotunnusohjain, mutta voisimme myös asentaa Bind9:n Debian-koneeseen, jotta meillä olisi paikallinen resolveri.



```
DNS = 192.168.100.11
```



Tallenna tiedosto ja käynnistä sitten Interface uudelleen:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Lopuksi Windows 10 -työaseman tunnelin kokoonpanossa sinun on muutettava "AllowedIPs"-osiota siten, että kaiken on kuljettava tunnelin läpi. Korvaa:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Kirjoittanut:



```
AllowedIPs = 0.0.0.0/0
```



Näet, että tämä aktivoi myös vaihtoehdon "**Kill switch*".



![Image](assets/fr/040.webp)



Lopuksi käytin tätä täyttä tunnelia hyväkseni suorittaakseni pienen virtaustestin, jonka tulokset on esitetty alla:



![Image](assets/fr/039.webp)



WireGuardin konfigurointi on melko yksinkertainen ja helppo ymmärtää ja ennen kaikkea ylläpitää. **WireGuardia pidetään VPN:ien tulevaisuutena**, joten meidän on parasta pitää sitä silmällä! Näemme myös, että suorituskyvyn kannalta hyöty on merkittävä, mikä on WireGuardin valtava etu OpenVPN:ään verrattuna.



Lisäasiakirjat:





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Mies - Komento wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**WireGuard VPN on toiminnassa! Onnittelut!