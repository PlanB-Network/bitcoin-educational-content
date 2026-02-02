---
name: Pop!_OS
description: Opas Linux-jakelun Pop!_OS asentamiseen
---

![cover](assets/cover.webp)



## Johdanto



Pop!OS on Linux-pohjainen käyttöjärjestelmä, jonka on kehittänyt **System76**, yhdysvaltalainen valmistaja, joka on erikoistunut kehittäjille, suunnittelijoille ja edistyneille käyttäjille tarkoitettuihin koneisiin.



Pop!OS on suunniteltu tarjoamaan nykyaikainen, vakaa ja suorituskykyinen ympäristö, ja sen erityispiirteitä ovat yksinkertainen käyttökokemus, tehokkaat työkalut ja vahva keskittyminen tuottavuuteen.



### Kuka on System76?



System76 on vuonna 2005 perustettu yhdysvaltalainen Denverissä toimiva yritys, joka on erikoistunut erityisesti Linuxille suunniteltujen kannettavien tietokoneiden, pöytäkoneiden ja palvelimien valmistukseen.



Toisin kuin perinteiset valmistajat, System76 kehittää koneita, jotka on suunniteltu avoimiksi, korjattaviksi ja ohjelmistovapauteen tähtääviksi.



System76 ei tee vain tietokoneita.



Yritys kehittää myös :




- Pop!OS**, sen oma Linux-pohjainen käyttöjärjestelmä;
- COSMIC**, moderni, suorituskykyinen työpöytäympäristö, jota Pop!OS käyttää;
- Open Firmware**, Corebootiin perustuva avoimen lähdekoodin laiteohjelma;
- työkaluja kehittäjille ja suunnittelijoille.



Tavoitteena on tarjota laadukasta laitteisto- ja ohjelmisto-integraatiota, joka on verrattavissa Applen ekosysteemiin, mutta täysin avoin ja Linux-keskeinen.



## Nykyaikainen, vakaa ja helppokäyttöinen järjestelmä



Pop!OS perustuu Ubuntu:n perustalle, mikä antaa sille erinomaisen vakauden, laajan laitteistoyhteensopivuuden ja pääsyn valtavaan ohjelmistoekosysteemiin.


Se tarjoaa tyylikkään käyttöliittymän, COSMIC-työpöydän, joka on suunniteltu sujuvaksi, intuitiiviseksi ja muokattavaksi myös uusille käyttäjille.



## Ihanteellinen valinta kehittäjille, suunnittelijoille ja vaativille käyttäjille



Pop!OS:ää arvostavat erityisesti :





- kehittäjät (esiasennetut työkalut, edistynyt laatoituksen hallinta),
- käyttäjät, joilla on Nvidian tai AMD:n näytönohjaimet,
- opiskelijoille ja ammattilaisille, jotka etsivät luotettavaa järjestelmää,
- windows-käyttäjille, jotka haluavat tehdä yksinkertaisen siirtymän.



Se sisältää automaattisen laatoituksen, selkeän ohjelmistokeskuksen ja integroidut tuottavuustyökalut, jotka helpottavat päivittäistä käyttöä.



## Pop!OS:n kohokohdat





- Optimoitu suorituskyky** säännöllisten päivitysten ansiosta.
- Saatavana kaksi ISO-versiota**: standard ja Nvidia-optimoitu.
- Parannettu tietoturva** (LUKS-salaus saatavilla asennuksen yhteydessä).
- Interface COSMIC** ergonominen ja moderni.
- Erittäin yhteensopiva** Ubuntu- ja Flatpak-ohjelmistojen kanssa.



## Lataa POP!OS turvallisesti



### 1. Edellytykset



Ennen POP!OS:n lataamista ja asentamista sinun on tehtävä muutamia asioita, jotta asennusympäristö valmistellaan oikein.



### Tarvittavat laitteet





- Yhteensopiva tietokone**: Intel- tai AMD-prosessori, Intel / AMD / Nvidia GPU.
- Vähintään 4 Gt RAM-muistia** (8 Gt suositellaan mukavaan käyttöön).
- vähintään 20 Gt vapaata tilaa** (suositellaan vähintään 40 Gt).
- Vähintään 4 Gt:n USB-tietolevy** asennusmedian luomista varten.



### Internet-yhteys



Vakaa yhteys on hyödyllinen :





- lataa ISO-kuva,
- asenna päivitykset asennuksen jälkeen.



Pop!OS voi toimia ilman yhteyttä, mutta asennus on paljon sujuvampaa Internetin kautta.



### Tietojen varmuuskopiointi



Jos Pop!OS korvaa toisen järjestelmän (Windows, Ubuntu jne.) tai toimii sen rinnalla, on suositeltavaa varmuuskopioida tärkeät tiedostot ennen jatkamista.



### Tarkista Nvidia GPU:n läsnäolo (jos mahdollista)



Jos tietokoneessa on Nvidian näytönohjain, sinun on ladattava erityinen ISO-kuva, joka sisältää Nvidia-ajurit.


Tämä tarkastus on hyvin yksinkertainen:





- tutustumalla tietokoneen teknisiin tietoihin,
- tai etsimällä näytönohjaimen malli järjestelmäasetuksista.



### Lataa viralliselta verkkosivustolta



Pop!OS ISO-kuva on ladattavissa suoraan viralliselta System76-sivulta: [system76.com/pop](https://system76.com/pop/).



Tällä sivulla on aina uusin versio, joka on mukautettu laitteistollesi.



![capture](assets/fr/03.webp)



### Valitse versio: Tai Raspberry Pi (ARM64)



Pop!OS on saatavana kolmena vaihtoehtona:



### Vakioversio



Suositellaan tietokoneille, jotka käyttävät :





- intelin tai AMD:n prosessori;
- integroitu Intelin tai AMD:n näytönohjain;
- aMD Radeon -näytönohjain.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia-versio



Suositellaan Nvidian näytönohjaimilla varustetuille tietokoneille.


Tämä kuva sisältää jo Nvidia-ajurit, mikä helpottaa asennusta ja vähentää grafiikkaongelmia.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Raspberry Pi -versio (ARM64)



Raspberry Pi 4 ja 400 (ARM-prosessori).


Tämä on ARM-arkkitehtuuriin mukautettu versio, joka on tarkoitettu erityisesti näitä minitietokoneita varten.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Luo käynnistettävä USB-levy



Voit käyttää useita työkaluja, kuten Balena Etcher :





- Lataa ja asenna [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Avaa Balena Etcher ja valitse sitten Pop!OS ISO-kuva.
- Valitse USB-muistitikku kohdevälineeksi.
- Napsauta Flash ja odota, että prosessi päättyy.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Pop!OS:n asentaminen ja suojaaminen



### Käynnistäminen USB-muistitikulta





- Sammuta tietokone.
- Kytke USB-levy (joka sisältää Pop!OS:n).
- Käynnistä tietokone. Uusimmissa tietokoneissa järjestelmän pitäisi tunnistaa USB-käynnistysavain automaattisesti. Jos näin ei tapahdu, käynnistä järjestelmä uudelleen pitämällä BIOS/UEFI-käyttönäppäintä painettuna (yleensä F2, F12 tai Delete, merkistä riippuen).
  - Valitse BIOS/UEFI-valikossa USB-levy käynnistyslaitteeksi.
  - Tallenna ja käynnistä uudelleen.



### Asennuksen käynnistäminen



Kun olet valinnut käynnistettävän USB-levyn käynnistyslaitteeksi, tietokone käynnistyy Pop!OS Live -ympäristöön.



Valitse kieli.



![Capture](assets/fr/10.webp)



Valitse sijainti.



![Capture](assets/fr/11.webp)



Valitse kieli näppäimistösyöttöä varten.



![Capture](assets/fr/12.webp)



Valitse näppäimistöasettelu.



![Capture](assets/fr/13.webp)



Valitse `Clean Install` (Puhdas asennus), jos haluat tavallisen asennuksen. Tämä on paras vaihtoehto uusille Linux-käyttäjille, mutta ota huomioon, että se poistaa kaiken kohdeaseman sisällön. Vaihtoehtoisesti voit valita `Try Demo Mode` (Kokeile demotilaa) jatkaaksesi Pop!OS:n testaamista live-ympäristössä.



![Capture](assets/fr/14.webp)



Valitse `Custom (Advanced)` päästäksesi GPartediin. Tämän työkalun avulla voit määrittää lisäominaisuuksia, kuten kaksoiskäynnistyksen, erillisen `/home`-osion luomisen tai `/tmp`-osion sijoittamisen eri asemalle.



Napsauta `Erase and Install` asentaaksesi Pop!OS valitulle asemalle.



![Capture](assets/fr/15.webp)



### Käyttäjätilin määritys



Asennusohjelman seuraavassa osiossa opastetaan sinua luomaan käyttäjätili, jotta voit kirjautua uuteen käyttöjärjestelmään.



Anna koko nimi (tämä voi sisältää minkä tahansa haluamasi tekstin, isoja tai pieniä kirjaimia) sekä käyttäjänimi (jonka on oltava pieni kirjain):



![Capture](assets/fr/16.webp)



Kun tili on luotu, sinua pyydetään asettamaan uusi salasana.



![Capture](assets/fr/17.webp)



### Koko levyn salaus



Järjestelmän levyn salaus ei ole välttämätön, mutta se takaa käyttäjätietojen turvallisuuden siinä tapauksessa, että joku pääsee luvatta fyysisesti käsiksi laitteeseen.



Asema voidaan salata kirjautumissalasanallasi valitsemalla `Salaus-salasana on sama kuin käyttäjätilin salasana`. Voit myös poistaa tämän valintaruudun ja valita alareunasta `Set Password` (Aseta salasana). Jos haluat jättää levyn salausprosessin huomiotta valitsemalla `Don't Encrypt` (Älä salaa).



![Capture](assets/fr/18.webp)



Jos olet valinnut `Set Password`-painikkeen, näet lisäkehotteen, jossa pyydetään asettamaan salaus-salasana.



Siirry asennusohjelman seuraavaan vaiheeseen. Pop!OS aloittaa nyt asennuksen levykkeelle.



![Capture](assets/fr/19.webp)



Kun asennus on valmis, käynnistä tietokone uudelleen ja kirjaudu sisään saadaksesi käyttäjätilin määritysprosessin päätökseen.



Jos olet muuttanut käynnistysjärjestystä siten, että Live USB-levy on etusijalla käynnistyksessä, sammuta tietokone kokonaan ja poista asennus-USB-levy. Jos olet kaksoiskäynnistystilassa, paina asianmukaisia näppäimiä päästäksesi kokoonpanoon ja valitaksesi Pop!OS-asennuksen sisältävän aseman.



![Capture](assets/fr/20.webp)



### NVIDIAn grafiikka



Jos olet asentanut Intel/AMD-ISO-ohjelmiston ja järjestelmässäsi on erillinen NVIDIAn näytönohjain tai jos olet lisännyt sellaisen myöhemmin, sinun on asennettava kortin ohjaimet manuaalisesti, jotta saavutat optimaalisen suorituskyvyn. Asenna ajuri suorittamalla seuraava komento komentoterminaalissa:



```bash
sudo apt install system76-driver-nvidia
```



Voit myös asentaa NVIDIAn grafiikkaohjaimet Pop!_Shopista.



![Capture](assets/fr/20.webp)



## Välttämättömien työkalujen asentaminen



Pop!OS tarjoaa laajan valikoiman ohjelmistoja Pop!Shopin kautta, mutta monet keskeiset työkalut voidaan asentaa myös päätelaitteen kautta `apt`- tai `flatpak`-ohjelmalla. Seuraavassa kerrotaan, miten asennat tärkeimmät työkalut täydellistä työympäristöä varten.



### Päätelaitteen asennus




| Työkalu | Kuvaus | Asennuskomento |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox | Vapaa ja suosittu verkkoselain | `sudo apt install firefox` |
| Brave | Yksityisyyteen keskittyvä verkkoselain | Asennus Pop!_Shopin tai virallisen sivuston kautta |
| Visual Studio Code (VS Code) | Tehokas koodieditori kehittäjille | `flatpak install flathub com.visualstudio.code` |
| Git | Versionhallinta | `sudo apt install git` |
| Flatpak | Vaihtoehtoinen paketinhallinta | `sudo apt install flatpak` |
| VLC | Monipuolinen mediasoitin | `sudo apt install vlc` |
| GNOME Terminal | Oletuspääte | Esiasennettu Pop!OS:ssä |
| Curl | Verkkotiedon siirtotyökalu | `sudo apt install curl` |
| Wget | Tiedostojen lataus HTTP/FTP:n kautta | `sudo apt install wget` |
| Docker | Sovellusten kontitus | Asennus virallisen skriptin tai `apt`:n kautta |
| Node.js | Palvelinpuolen JavaScript-ympäristö | Asennus `apt`:n tai NodeSourcen kautta |
| Python3 | Ohjelmointikieli | `sudo apt install python3 python3-pip` |
| GIMP | Edistynyt kuvankäsittelyohjelma | `sudo apt install gimp` |
| Thunderbird | Sähköpostiohjelma | `sudo apt install thunderbird` |
| Transmission | Kevyt BitTorrent-ohjelma | `sudo apt install transmission-gtk` |
| Htop | Interaktiivinen järjestelmänvalvonta | `sudo apt install htop` |

### Asennus Pop! Shop (graafinen käyttöliittymä)





- Avaa **Pop!_Shop** päävalikosta.
- Etsi haluamasi sovellukset hakupalkin avulla (esimerkiksi "Brave").
- Napsauta **Asenna** kunkin sovelluksen kohdalla.
- Pop!_Shop hallinnoi riippuvuuksia ja päivityksiä automaattisesti.



## Järjestelmäpäivitys



### Vaihtoehto 1: Graafisen käyttöliittymän (GUI) kautta



Pop!OS:ssä on yksinkertainen, intuitiivinen graafinen päivityshallinta.



1. Napsauta **päävalikkoa** (kuvake alhaalla vasemmalla).


2. Avaa **"Pop!_Shop "**.


3. Napsauta Pop!_Shopissa välilehteä **"Päivitykset "**.


4. Järjestelmä tarkistaa automaattisesti, onko päivityksiä saatavilla.


5. Napsauta **"Päivitä kaikki "** aloittaaksesi päivitysten asentamisen.


6. Anna salasanasi, jos sitä pyydetään.


7. Anna prosessin päättyä ja käynnistä se tarvittaessa uudelleen.



### Vaihtoehto 2: Päätelaitteen kautta



Avaa terminaali ja kirjoita :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Käyttäjien hallinta



Suosittelemme käyttämään tavallista käyttäjätiliä, jolla on sudo-oikeudet päivittäisiin toimintoihin.



Uuden käyttäjän luominen :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Kirjaudu ulos ja kirjaudu sitten takaisin sisään tällä uudella käyttäjällä.



### Grafiikkaohjaimen hallinta





- Tarkista Nvidia-korttien osalta, että omat ajurit on asennettu:



```bash
sudo apt install system76-driver-nvidia
```





- AMD/Intel-ohjaimet ovat yleensä oletusarvoisesti mukana.



### Aktivoi palomuuri (UFW)



Pop!OS ei estä verkkoliikennettä oletusarvoisesti. Aktivoi UFW turvallisuuden parantamiseksi:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Määritä automaattiset päivitykset



Järjestelmän pitäminen ajan tasalla ilman manuaalisia toimenpiteitä:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Muokkaa ulkonäköä ja käyttäytymistä





- Avaa **Järjestelmäasetukset** → **Näkymä** ja valitse vaalea tai tumma teema.
- Määritä aktiiviset kulmat, animaatiot ja laajennukset COSMIC Managerin kautta.
- Säädä työpöydän asettelua työnkulun optimoimiseksi.



### Automaattisen varmuuskopioinnin määrittäminen



Pop!OS integroi Deja Dupin kaltaisia työkaluja varmuuskopiointia varten:





- Käynnistä **Backup** valikosta.
- Valitse ulkoinen asema tai verkkopaikka.
- Aikatauluta säännölliset varmuuskopiot.



### Hyödyllisten GNOME/COSMIC-laajennusten asentaminen



Seuraavassa on muutamia suositeltuja laajennuksia, jotka parantavat käyttäjäkokemusta:





- Dash to Dock**: sovelluspalkki aina näkyvissä.
- GSConnect**: synkronointi Androidin kanssa.
- Leikepöydän ilmaisin**: edistynyt leikepöydän hallinta.



Asenna ne :



```bash
sudo apt install gnome-shell-extensions
```



Aktivoi ne sitten asetuksissa.



### Muistin ja swapin hallinnan optimointi



Tarkista vaihtotilanne:



```bash
swapon --show
```



Lisää tarvittaessa swap-kokoa tai määritä swap-tiedosto :



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Lisää se tiedostoon `/etc/fstab` automaattista asennusta varten.



## Pakettien ja arkistojen hallinta



### Pakettien lähteiden ymmärtäminen



Ubuntu:een perustuva Pop!OS käyttää pääasiassa :





- Viralliset Ubuntu**-tietovarastot: useimmat vakaat ohjelmistot.
- System76**-tietovarastot: ajurit, laiteohjelmistot ja erityistyökalut.
- Flatpak**: pääsy monenlaisiin hiekkalaatikkosovelluksiin.
- Snap** (valinnainen): toinen yleinen pakkausmuoto.



---

### PPA-arkistojen lisääminen ja hallinta



Usein päivitettyjen ohjelmistojen asentamiseen voidaan lisätä tiettyjä PPA:ita (Personal Package Archives):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Päätelmä



Pop!OS on moderni ja vakaa Linux-jakelu, joka sopii sekä aloittelijoille että edistyneille käyttäjille.



Intuitiivisen COSMIC-käyttöliittymän ja integroitujen työkalujen ansiosta se tarjoaa sujuvan ja tuottavan käyttökokemuksen, olipa kyse sitten kehittämisestä, luomisesta tai jokapäiväisestä käytöstä.



Tämä opetusohjelma kattaa tärkeimmät vaiheet: valmistelu, lataaminen, asennus, alkuasetukset ja keskeiset työkalut.



Tutustu vapaasti Pop!OS:ään tarkemmin ja muokkaa ympäristöäsi saadaksesi siitä kaiken irti.