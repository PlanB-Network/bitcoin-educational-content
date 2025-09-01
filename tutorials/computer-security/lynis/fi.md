---
name: Lynis
description: Suorita Linux-koneen tietoturvatarkastus Lynisin avulla
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Fares CHELLOUGin alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___



## I. Esittely



**Tässä ohjeessa opettelemme, miten Linux-koneen tietoturvatarkastus tehdään Lynisin avulla! Niille teistä, jotka eivät tunne **Lynistä,** se on pieni komentorivin apuohjelma, joka analysoi palvelimesi kokoonpanon ja antaa suosituksia koneesi tietoturvan **parantamiseksi.**



Lynis on avoimen lähdekoodin työkalu CISOFY:ltä, joka on erikoistunut **järjestelmän valvontaan ja kovettamiseen**. Jos haluat edetä Linuxin ja suosittujen palveluiden (SSH, Apache2 jne.) kovettamisessa, Lynis on liittolaisesi! Lynis ei ainoastaan kerro, mikä menee pieleen, vaan antaa myös suosituksia, jotka ohjaavat sinua oikeaan suuntaan (ja säästävät aikaa).



**Lynis** toimii useimpien Linux-jakeluiden kanssa, mukaan lukien: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis on suunnattu Linux/UNIX-käyttäjille, mutta se on myös **macOS**-yhteensopiva. Erittäin nopea asentaa, pakettitasolla ei ole riippuvuuksien hallintaa.



Sitä käytetään moniin eri tarkoituksiin:





- Turvallisuusauditoinnit
- Vaatimustenmukaisuuden testaus (PCI, HIPAA ja SOX)
- Kovemmat järjestelmäkokoonpanot
- Haavoittuvuuden havaitseminen



Työkalua käyttävät laajalti erilaiset käyttäjät, kuten järjestelmänvalvojat, IT-tarkastajat ja pentesterit. Analyyseissä työkalu perustuu standardeihin, kuten **CIS Benchmark, NIST, NSA, OpenSCAP** ja **Debianin, Gentoon, Red Hatin** virallisiin suosituksiin.



Projekti on saatavilla tässä Address:ssa **Githubissa**:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Lataa Lynis CISOFY:stä](https://cisofy.com/lynis/#download)



Tässä vaiheittaisessa ohjeessa käytän **VPS:ää, jossa on Debian 12**, ja keskityn SSH-osioon, koska haluan tarkistaa sen kokoonpanon ja parantaa sitä.



## II. Lataus ja asennus



Lynisin voi ladata ja asentaa usealla eri tavalla. Valitse haluamasi alla olevasta luettelosta.



### A. Asennus Debianin arkistoista



Tämän asennustavan avulla voit käyttää komentoa **lynis** mistä tahansa järjestelmässä, toisin kuin lähdekoodista asennettaessa, jossa sinun on oltava hakemistossa.



Ota yhteys palvelimeen SSH:n kautta ja asenna Lynis seuraavilla komennoilla:



```
sudo apt-get update
sudo apt-get install lynis -y
```



Saat tämän:



![Image](assets/fr/024.webp)



### B. Lataa viralliselta verkkosivustolta



Voit myös ladata sen Cisofyn verkkosivustolta:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Saat tämän:



![Image](assets/fr/032.webp)



Seuraavaksi puramme arkiston seuraavalla komennolla:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Saat tämän:



![Image](assets/fr/020.webp)



Siirrytään **lynis**-kansioon:



```
cd lynis
```



Voimme tarkistaa päivitykset seuraavalla komennolla:



```
./lynis update info
```



Saat tämän:



![Image](assets/fr/023.webp)



### C. Lataa GitHubista



Lataamme **Lyniksen** virallisesta GitHub-arkistosta seuraavalla komennolla (*git*:n on oltava koneellasi):



```
git clone https://github.com/CISOfy/lynis.git
```



Saat tämän:



![Image](assets/fr/060.webp)



## III. Lynisin käyttö



Lynis on koneellamme, joten opettelemme käyttämään sitä!



### A. Tärkeimmät hallintalaitteet ja vaihtoehdot



Voit näyttää käytettävissä olevat komennot kirjoittamalla seuraavan komennon:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



Saat tämän:



![Image](assets/fr/039.webp)



Lisäksi saat seuraavat vaihtoehdot:



![Image](assets/fr/040.webp)



Voit näyttää kaikki käytettävissä olevat komennot kirjoittamalla seuraavan komennon:



```
sudo lynis show
```



Saat tämän:



![Image](assets/fr/022.webp)



Jos haluat näyttää kaikki vaihtoehdot, sinun on kirjoitettava:



```
sudo lynis show options
```



Saat tämän:



![Image](assets/fr/021.webp)



Tämän artikkelin loppuosassa opettelemme käyttämään tiettyjä vaihtoehtoja.



### B. Järjestelmän tarkastuksen suorittaminen



Pyydämme **Lynisiä** tarkastamaan järjestelmämme ja korostamaan, mikä on oikein konfiguroitu ja mitä voitaisiin parantaa. Tee tämä kirjoittamalla seuraava komento:



```
sudo lynis audit system
# ou
./lynis audit system
```



Jos et ole kirjautuneena pääkäyttäjänä tätä komentoa suorittaessasi, työkalu suoritetaan oletusarvoisesti kirjautuneen käyttäjän oikeuksilla. Joitakin testejä ei suoriteta tässä yhteydessä:



![Image](assets/fr/052.webp)



Tässä luetellaan testit, joita ei suoriteta tässä tilassa:



![Image](assets/fr/051.webp)



Kun komento on suoritettu, analyysi alkaa. Odota hetki.



Tarkastuksen lopussa saat tämän (näemme, että **Lynis** on tunnistanut oikein **Debian 12** -järjestelmän ja käyttää analyysissä **Debian-lisäosaa**):



![Image](assets/fr/017.webp)



Seuraavaksi Lynis luettelee joukon kohtia, jotka vastaavat kaikkea sitä, mitä hän on tarkistanut järjestelmästämme. Tämä on järjestetty luokittain, kuten tulemme näkemään. On myös syytä huomata, että suositusten korostamiseen käytetään värikoodia:





- Punainen**, kun kriittistä Elements:tä tai parhaita käytäntöjä ei noudateta (esimerkiksi puuttuva paketti), eli palvelimesi ei noudata tätä kohtaa
- Keltainen** suosituksen ehdotuksille tai osittaiselle noudattamiselle (sanotaan, että tällä värillä korostetun kohdan noudattaminen on plussaa (ei-prioriteetti))
- Green** kohdissa, joissa palvelinkokoonpano on vaatimustenmukainen
- Valkoinen**, kun neutraali



Täältä näemme, että Lynis suosittelee **fail2ban**-asennusta:



![Image](assets/fr/057.webp)



Osiossa "**Boot and services**" (käynnistys ja palvelut**) näemme, että *systemd:n* kautta tapahtuvaa palvelusuojausta voitaisiin parantaa. Positiivista on, että Grub2 on läsnä eikä ongelmia ole:



![Image](assets/fr/029.webp)



Sitten on osiot "**Ydin**" ja "**Muisti ja prosessit**":



![Image](assets/fr/037.webp)



Seuraavaksi osio "**Käyttäjät, ryhmät ja todennus**". Työkalu ilmoittaa meille varoituksesta, joka koskee hakemiston "**/etc/sudoers.d**" käyttöoikeuksia. Tällä hetkellä emme tiedä enempää, mutta voimme nähdä, mikä suositus on analyysin lopussa.



![Image](assets/fr/049.webp)



Seuraavassa kerrotaan, mitä löydät kohdista "**Shells", "Files Systems" ja "USB Devices "**. Näemme muun muassa, että liitäntäpisteitä koskevia ehdotuksia on olemassa ja että USB-laitteet ovat tällä hetkellä sallittuja tällä koneella.



![Image](assets/fr/048.webp)



Seuraavaksi jaksot: "Tässä ilmoitetaan, että paketit, joita ei enää käytetä, voidaan poistaa ja että automaattisten päivitysten hallintaan ei ole apuohjelmaa.



![Image](assets/fr/058.webp)



Näemme, että palomuuri on aktivoitu (ja kyllä, iptables on käytössä!). Lisäksi näemme, että se on löytänyt käyttämättömiä sääntöjä ja että Apache-verkkopalvelin on asennettu.



![Image](assets/fr/055.webp)



Tämän jälkeen analysoidaan itse verkkopalvelin, koska palvelu on tunnistettu.



Näemme, että se on löytänyt **Nginx**-konfiguraatiotiedostot ja että SSL/TLS-osassa **salakirjoitukset** on määritetty käyttämällä protokollaa, joka olisi turvaton. Toisaalta Lynisin mukaan lokien hallinta on oikein.



![Image](assets/fr/038.webp)



SSH-palvelu on läsnä VPS-palvelimellani. Lynis analysoi sen kokoonpanon. On sanottava, että SSH:n turvallisuutta voidaan helposti parantaa! Palaamme tähän alueeseen yksityiskohtaisesti, kun olemme saaneet suositukset.



![Image](assets/fr/026.webp)



Tässä ovat osiot **"SNMP-tuki", "Tietokannat", "PHP", "Squid-tuki", "LDAP-palvelut", "Kirjaaminen ja tiedostot "**.



Yksi todella tärkeä ehdotus lokien hallinnasta: on erittäin suositeltavaa, ettet säilytä lokeja paikallisesti koneellasi. Jos koneen turmelee hyökkääjä, on todennäköistä, että hän yrittää poistaa jälkensä... Meidän on siis ulkoistettava lokit.



![Image](assets/fr/050.webp)



Täällä meillä on haavoittuvien palveluiden, tilinhallinnan, ajastettujen tehtävien ja NTP-synkronoinnin tarkastus.On ilmoitettu, että taso on alhainen bannerissa ja tunnistusosassa: tämä on ymmärrettävää, jos näytät järjestelmän version, se antaa viitteitä mahdolliselle hyökkääjälle. Tämä on oletusasetus.



Olisi mielenkiintoista aktivoida **auditd**, jotta saisimme lokit **teknisen** analyysin varalta. Myös **NTP** tarkistetaan, koska lokien tehokkaan haun kannalta on suotavaa, että järjestelmät ovat ajantasalla, mikä helpottaa hakua.



![Image](assets/fr/036.webp)



Tämän jälkeen Lynis tarkastelee kryptografista Elements:a, virtualisointia, kontteja ja tietoturvakehyksiä. Jotkin osiot ovat tyhjiä, koska niissä ei ole vastaavuutta analysoitavan koneen kanssa. Näemme kuitenkin, että minulla on kaksi vanhentunutta SSL-varmentetta enkä ole aktivoinut **SELinuxia**.



![Image](assets/fr/027.webp)



Tässäkin on parantamisen varaa: ei ole virustorjunta- tai haittaohjelmien skanneria, ja meillä on ehdotuksia tiedostojen käyttöoikeuksista.



![Image](assets/fr/028.webp)



Seuraavaksi Lynis keskittyy Linux-ytimen konfiguroinnin tiukentamiseen (mukaan lukien IPv4-pinon säännöt) sekä Linux-koneen "Home"-hakemistojen hallintaan.



![Image](assets/fr/035.webp)



Olemme tulleet analyysin loppuun... Tämä viimeinen kohta osoittaa, että ClamAV:n ottaminen tähän koneeseen olisi meille kaikki kaikin puolin hyödyllistä.



![Image](assets/fr/030.webp)



## IV. Suositukset



Tarkastuksen jälkeen on aika lukea ja analysoida suositukset. Täältä saamme suositukset ja selitykset jokaiselle Lynisin suorittamalle testille.



Otetaan esimerkiksi SSH-suositukset. **Kustakin suosituksesta löydät suositellun parametrin ja linkin, joka selittää turvallisuuskohdan ** Voit itse päättää asiayhteydestäsi ja käyttötarkoituksestasi riippuen.



Tarkastellaan muutamia esimerkkejä suosituksista, jotka vastaavat suoraan tarkastuksessa esiin tuotuja seikkoja....



### A. Esimerkkejä suosituksista





- Kuten aiemmin nähtiin, NTP on tärkeä lokien aikaleimauksessa:



![Image](assets/fr/043.webp)





- Lynis ehdottaa myös **apt-listbugs**-paketin asentamista, jotta saat tietoa kriittisistä virheistä pakettien asennuksen aikana **apt.** kautta



![Image](assets/fr/041.webp)





- Työkalu ehdottaa, että asennamme **needrestartin, jotta voimme** nähdä, mitkä prosessit käyttävät kirjaston vanhaa versiota ja ne on käynnistettävä uudelleen.



![Image](assets/fr/054.webp)





- Tässä ehdotuksessa ehdotetaan **fail2ban**:n asentamista estämään automaattisesti isännät, jotka eivät onnistu todennuksessa (erityisesti brute force).



![Image](assets/fr/044.webp)





- Järjestelmäpalveluiden suojaamiseksi hän suosittelee, että suoritamme sinisen komennon jokaiselle koneemme palvelulle.



![Image](assets/fr/056.webp)





- Hän ehdottaa, että kaikille suojattujen tilien salasanoille asetetaan voimassaolon päättymispäivämäärät.



![Image](assets/fr/031.webp)





- Tässä ehdotuksessa ehdotetaan, että salasanan iälle asetetaan vähimmäis- ja enimmäisarvot. Näin varmistetaan muun muassa, että salasanat vaihdetaan säännöllisesti.



![Image](assets/fr/042.webp)





- Suosittelemme käyttämään erillisiä osioita, jotta yhden osion levytilaongelmat eivät vaikuttaisi.



![Image](assets/fr/047.webp)





- Tässä suosituksessa ehdotetaan USB-tallennusvälineiden ja firewiren poistamista käytöstä tietovuodon estämiseksi



![Image](assets/fr/033.webp)





- Voit täyttää tämän suosituksen yksinkertaisesti asentamalla ja määrittämällä esimerkiksi **unnatended-upgrade**.



![Image](assets/fr/053.webp)



### B. Suositeltujen pakettien asentaminen



Parantaaksemme järjestelmän kokoonpanoa asennamme koneelle joitakin paketteja: joitakin Lynisin suosittelemia ja joitakin itse suosittelemiani.



Sinulla on hyvä perusta työskentelylle, kunhan käytät hieman aikaa niiden konfigurointiin. Tätä varten kannattaa tutustua IT-Connect-sivustoon, muihin verkkoartikkeleihin ja työkalujen dokumentaatioon.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Joitakin tietoja asennetuista paketeista:





- Clamav** on virustorjuntaohjelma.
- unattend-upgrades** mahdollistaa päivitysten automaattisen hallinnan ja jopa koneen uudelleenkäynnistyksen tai vanhojen pakettien automaattisen poistamisen, se on täysin konfiguroitavissa.
- rkhunter** on anti-rootkit, joka skannaa tiedostojärjestelmän.
- Fail2ban** käyttää lokitiedostojasi sen mukaan, mitä annat sen lukea, ja se toimii **iptables**:n kanssa esimerkiksi kieltääkseen IP-osoitteet, jotka yrittävät "murtaa" palvelimesi SSH:lla.



### C. SSH:ta koskevat suositukset



Katsotaanpa SSH-suosituksia. Ne on lueteltu alla. Älä huoli, selitämme heti, miten konfiguraatiota voidaan parantaa.



![Image](assets/fr/034.webp)



Katsotaanpa tarkemmin nykyistä **SSH**-konfiguraatiotani tiedostossa:**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Jäljempänä ehdotettua kokoonpanoa voidaan vielä optimoida, mutta se antaa hyvän perustan. *Huomaa, että olen poistanut useita kommentteja luettavuuden parantamiseksi*.



Me:





- Vaihda SSH-yhteysportti (unohda oletusarvo 22)
- Nosta lokien sanamäärää **INFOsta VERBOSEen**
- Aseta **LoginGraceTime** arvoksi **2 minuuttia**



Jos yhteystietoja ei syötetä kahden minuutin kuluessa, yhteys katkaistaan.





- Aktivoi **strictModes**



Määrittää, pitääkö "sshd" tarkistaa käyttäjän tiedostojen tilat ja omistaja sekä käyttäjän kotihakemisto ennen yhteyden vahvistamista. Tämä on yleensä toivottavaa, koska joskus aloittelijat jättävät hakemistonsa tai tiedostonsa vahingossa täysin kaikkien saataville. Oletusarvo on "yes".





- Aseta **MaxAuthtries** arvoksi 3



Tämä on epäonnistuneiden todennusyritysten määrä ennen kuin tiedonsiirto suljetaan.





- Aseta **MaxSessions** arvoksi 2



Tämä edustaa samanaikaisten istuntojen enimmäismäärää.





- Ota julkisen avaimen todennus käyttöön



```
PubkeyAuthentication yes
```





- Säilytä salasanan todennus:



```
PasswordAuthentication yes
```



Kielletään tyhjät salasanat ja **Kerberos**-todennus sekä **suora pääkäyttäjätodennus**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Varmista, että sinulla on "**PermitRootLogin no", jos se on yhtä suuri kuin "yes", se on "absolute evil "**.





- Kielletään TCP-yhteyden uudelleenohjaus



```
AllowTcpForwarding no
```



Ilmaisee, sallitaanko TCP-uudelleenohjaukset, ja oletusasetus on "kyllä". Huomaa: TCP-uudelleenohjausten poistaminen käytöstä ei paranna turvallisuutta, jos käyttäjillä on pääsy komentotulkkiin, koska he voivat edelleen asettaa omia uudelleenohjaustyökalujaan.





- X11-uudelleenohjauksen kieltäminen



```
X11Forwarding no
```



Ilmaisee, hyväksytäänkö X11-uudelleenohjaukset, oletusasetus on "no". Huomaa: vaikka X11-uudelleenohjaukset olisi poistettu käytöstä, se ei lisää turvallisuutta, koska käyttäjät voivat silti asettaa omia uudelleenohjauksiaan. X11-uudelleenohjaus poistetaan automaattisesti käytöstä, jos **KäytäLogin** on valittu.





- Asettaa asiakkaan ja sshd:n välisen viestinnän aikakatkaisun



```
ClientAliveInterval  300
```



Määrittää sekunteina aikakatkaisun, jonka jälkeen sshd-palvelu lähettää viestin, jossa pyydetään vastausta asiakkaalta, jos asiakkaalta ei saada tietoja. Oletusarvoisesti tämä vaihtoehto on asetettu arvoon "0", mikä tarkoittaa, että näitä viestejä ei lähetetä asiakkaalle. Vain SSH-protokollan versio 2 tukee tätä vaihtoehtoa.



```
ClientAliveCountMax 0
```



[sshd:n dokumentaation (*man-sivu*)](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html) mukaan tämä vaihtoehto tarkoittaa seuraavaa: "Asettaa **sshd**:n pidätysviestien (ks. edellä) määrän, joka lähetetään ilman asiakkaan vastausta. Jos tämä kynnysarvo saavutetaan, kun pidätysviestejä on lähetetty, **sshd** katkaisee asiakkaan yhteyden ja lopettaa istunnon. On tärkeää huomata, että nämä pidätysviestit eroavat huomattavasti **KeepAlive**-vaihtoehdosta (jäljempänä). Yhteyden pitoviestit lähetetään salatun tunnelin kautta, joten niitä ei voi väärentää. **KeepAlive**:n mahdollistama TCP-tason yhteydenpito on väärennettävissä. Yhteydenpidon mekanismi on kiinnostava silloin, kun asiakkaan tai palvelimen on tiedettävä, onko yhteys käyttämättömänä."





- Estä tietojen paljastuminen poistamalla **motd, banner, lastlog** käytöstä



```
PrintMotd no
```



Määrittää, näyttääkö sshd tiedoston "/etc/motd" sisällön, kun käyttäjä kirjautuu sisään interaktiivisessa tilassa. Joissakin järjestelmissä tämä sisältö voidaan näyttää myös komentotulkissa /etc/profile-tiedoston tai vastaavan tiedoston kautta. Oletusarvo on "yes".



```
Banner none
```



On syytä huomata, että joillakin lainkäyttöalueilla viestin lähettäminen ennen todentamista voi olla oikeussuojan edellytys. Määritellyn tiedoston sisältö lähetetään etäkäyttäjälle ennen kuin yhteysvaltuutus annetaan. Tämä vaihtoehto on määritettävä, sillä oletusarvoisesti viestiä ei näytetä.



Kuvissa tämä antaa:



![Image](assets/fr/019.webp)



### D. Auditointipisteet



Älkäämme myöskään unohtako tarkistaa **Lynisin tarkastuksen pisteet**! Näemme, että **Karkaistumisarvoni on 63** ja että raporttitiedosto on nähtävissä osoitteessa "**/var/log/lynis-report.dat**". On myös tiedosto "**/var/log/lynis.log**".



**Mikä korkeampi pistemäärä, sen parempi! Sinun on siis parannettava kokoonpanoasi, jotta saavutat mahdollisimman korkean pistemäärän, mutta samalla koneesi ja isännöidyt palvelut voivat toimia normaalisti (mikä tarkoittaa toiminnallisten testien suorittamista).



![Image](assets/fr/046.webp)



Katsotaanpa tuloksia toisella palvelimellani, jonka kovettamiseen käytin hieman enemmän aikaa! On siis normaalia, että pisteet ovat korkeammat (**76**).



![Image](assets/fr/045.webp)



## V. Lynis automaattinen suunnittelu



**Lynis** tarjoaa myös mahdollisuuden suorittaa tarkistukset ajastetun tehtävän kautta. Käytössä on itse asiassa **"--cronjob "** -vaihtoehto, joka suorittaa kaikki Lynis-testit ilman validointia tai käyttäjän toimenpiteitä. Voit sitten hyvin yksinkertaisesti luoda skriptin, joka ajaa **Lynis**:n ja laittaa tulosteet aikaleimalla varustettuun tiedostoon, jossa on kyseisen palvelimen nimi. Tässä on tällainen tiedosto, jonka voit laittaa */etc/cron.daily*-kansioon:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



Muuttuja **"AUDITOR_NAME "** on yksinkertaisesti muuttuja, jonka asetamme **Lynis**:n **"--auditori "** -vaihtoehdossa, jotta tämä nimi näkyy raportissa:



![Image](assets/fr/059.webp)



Luomme myös muutaman kontekstimuuttujan, jotka auttavat meitä järjestämään itseämme paremmin, kuten isännän nimen ja päivämäärän, joiden perusteella raportti nimetään ja aikaleimataan, sekä sen kansion polun, johon haluamme laittaa raporttimme.



## VI. Päätelmät



Lynis on erittäin käytännöllinen työkalu, joka auttaa sinua säästämään aikaa ja olemaan tehokkaampi, kun haluat tietää enemmän Linux-palvelimen kokoonpanon tilasta, erityisesti tietoturvan osalta. Älä kuitenkaan unohda, että jokainen muutos on testattava ennen sen käyttöönottoa tuotannossa ottaen huomioon oma käyttö ja konteksti.



Et luultavasti aio soveltaa samaa konfiguraatiota VPS:lle, joka on alttiina verkolle, jossa tarvitset vain yhden SSH-yhteyden (koska olet ainoa henkilö, joka muodostaa yhteyden), toisin kuin **bastion** tai **scheduler**, jotka tarvitsevat useita **SSH.**-yhteyksiä



Kun olet saanut kokoonpanon, joka sopii sinulle suojauksen kannalta, on suositeltavaa ottaa käyttöön automaatiotyökalu, jotta sinun ei tarvitse tehdä tehtäviä uudelleen manuaalisesti, sillä se olisi aikaa vievää ja virhealtista. Voit esimerkiksi käyttää **: Puppet, Chef, Ansible jne...**



Älä unohda viestiä tiimiesi kanssa ennen käyttöönottoa: sinun on saatava heidät ymmärtämään, miksi teet nämä muutokset, etkä vain kertomaan heille, että teet ne. Loppujen lopuksi tavoitteena on hyvien käytäntöjen siirtäminen eteenpäin, mikä lisää onnistumismahdollisuuksia.



Lopuksi voit myös verrata **Lynistä** muihin työkaluihin, joita on useita. Jos haluat siirtyä kohti keskitettyä hallintaa säilyttäen samalla avoimen lähdekoodin, suosittelen [Wazuh]-työkalua (https://wazuh.com/).



**Tämä opetusohjelma on ohi, pidä hauskaa Lynisin kanssa!