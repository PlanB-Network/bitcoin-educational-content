---
name: pfSense
description: Pfsensen asentaminen
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian BURNELin alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Kirjoittajan alkuperäiseen tekstiin on tehty suuria muutoksia, jotta opetusohjelma olisi ajan tasalla.*



___



![Image](assets/fr/027.webp)



## I. Esittely



pfSense on ilmainen, avoimen lähdekoodin käyttöjärjestelmä, joka muuttaa minkä tahansa tietokoneen, erillisen palvelimen tai laitteistolaitteen suorituskykyiseksi ja hyvin konfiguroitavaksi reitittimeksi ja palomuuriksi. FreeBSD:hen perustuva pfSense on tunnettu vakaasta ja vankasta verkkoarkkitehtuuristaan, ja se on jo yli viidentoista vuoden ajan asettanut standardin avoimen lähdekoodin palomuureille yrityksille, paikallisviranomaisille ja vaativille kotikäyttäjille.



Sen päätoiminnot ovat kehittyneet huomattavasti vuosien varrella, ja niitä on parannettu jokaisen uuden version myötä. Tähän mennessä pfSense tarjoaa :





- Täydellinen, keskitetty hallinta nykyaikaisen, intuitiivisen ja turvallisen Interface-verkkopalvelun kautta Interface.
- Suorituskykyinen tilallinen palomuuri, jossa on kehittynyt NAT-tuki (mukaan lukien NAT-T) ja yksityiskohtainen sääntöjen hallinta.
- Natiivi multi-WAN-tuki, joka mahdollistaa Internet-yhteyksien yhdistämisen tai redundanssin.
- Integroitu DHCP-palvelin ja rele.
- Korkea käytettävyys vikasietoisen CARP-protokollan ja pfSense-klusterien konfigurointimahdollisuuden ansiosta.
- Kuormituksen tasaus useiden yhteyksien tai palvelimien välillä.
- Täysi VPN-tuki: IPsec, OpenVPN ja WireGuard (korvaa L2TP:n, joka on nyt vanhentunut).
- Konfiguroitava captive-portaali vieraiden pääsynvalvontaan erityisesti julkisissa tai hotelliympäristöissä.



pfSense sisältää myös laajennettavan pakettijärjestelmän, jonka avulla on helppo lisätä lisäominaisuuksia, kuten läpinäkyvä välityspalvelin (Squid), URL-suodatus tai IDS/IPS (Snort tai Suricata) suoraan Interface-verkosta.



pfSense jaetaan vain 64-bittisille alustoille FreeBSD:n nykyisten suositusten mukaisesti. Se voidaan asentaa tavallisiin laitteistoihin (PC:t, räkkipalvelimet) tai pienitehoisiin sulautettuihin alustoihin, kuten Netgate-laitteisiin tai tiettyihin matalaprofiilisiin x86-laitteisiin, jotka ovat paljon tehokkaampia kuin vanhemmat Alix-laitteet.



Lopuksi kannattaa muistaa, että pfSense vaatii vähintään kaksi fyysistä verkkoliitäntää: yhden ulkoiselle alueelle (WAN) ja yhden sisäiselle verkolle (LAN). Infrastruktuurisi monimutkaisuudesta riippuen (DMZ, VLAN, useita WAN-verkkoja), sen ominaisuuksien täysimääräinen hyödyntäminen voi vaatia useita ylimääräisiä liitäntöjä.



## II. Lataa kuva



Tämän ohjeen kirjoittamishetkellä pfSensen viimeisin vakaa versio on 2.8 (julkaistu kesäkuussa 2025). Voit ladata ISO-kuvan tai laitteistoympäristöösi sovitetun asennustiedoston suoraan viralliselta verkkosivustolta :





- [Lataa pfSense](https://www.pfsense.org/download/)



Latausportaalin avulla voit valita :





- Arkkitehtuuri (yleensä **AMD64** kaikissa nykyaikaisissa laitteistoissa).
- Kuvatyyppi (**Installer USB Memstick** USB-muistitikun kautta tapahtuvaan asennukseen, **ISO Installer** polttamiseen tai virtuaaliseen muokkaukseen).
- Lähin latauspeili siirtonopeuden optimoimiseksi.



Niille, jotka haluavat ottaa pfSensen käyttöön virtualisoidussa ympäristössä (Proxmox, VMware ESXi, VirtualBox...), on saatavilla myös **OVA**-kuva. Tämä käyttövalmis virtuaalikone yksinkertaistaa asennusta ja alkukonfiguraatiota huomattavasti. Varmista vain, että säädät varatut resurssit (CPU, RAM, verkkoliitännät) odotetun kuormituksen ja verkkotopologian mukaan.



Ennen asennusta suosittelemme tarkistamaan ladatun tiedoston eheyden tarkistamalla **SHA256**, joka on annettu virallisella lataussivulla. Näin varmistetaan, että kuvaa ei ole muutettu tai vioittunut.



## III. Asennus



Tässä esimerkissä asennus suoritetaan VirtualBoxia käyttävään virtuaalikoneeseen. Menettely pysyy täysin samanlaisena fyysisessä koneessa tai muussa hypervisorissa lukuun ottamatta virtuaalilaitteiden hallintaa.



### 1. Vähimmäislaitteistovaatimukset



Standardikäyttöön suosittelemme :





- vähintään 1 Gt RAM-muistia** (2 Gt tai enemmän suositellaan lisäpakettien tai ZFS-tuen mahdollistamiseksi).
- 8 Gt levytilaa** (20 Gt tai enemmän on suositeltava edistyneemmille kokoonpanoille, erityisesti jos asennat välityspalvelimen välimuistin, IDS/IPS-järjestelmän tai yksityiskohtaiset lokit).
- Vähintään kaksi virtuaalista verkkoliitäntää** (yksi WAN:lle ja yksi LAN:lle). Lisää ne VirtualBoxissa VM:n asetuksiin ennen käynnistystä.



### 2. Asennusohjelman käynnistys



Asenna ladattu ISO-kuva virtuaalisena optisena asemana VirtualBoxissa tai aseta USB-muistitikku, jos asennat fyysiseen koneeseen. Käynnistyksen yhteydessä näyttöön tulee käynnistysvalikko:



Jos et valitse mitään vaihtoehtoja, pfSense käynnistyy automaattisesti oletusasetuksilla muutaman sekunnin kuluttua. Paina "**Enter**"-näppäintä käynnistääksesi normaalin käynnistyksen.



![Image](assets/fr/027.webp)



Kun päävalikko tulee näkyviin, paina nopeasti "**I**"-painiketta aloittaaksesi asennuksen.



![Image](assets/fr/001.webp)



### 3. Asennusohjelman alkuasetukset



Ensimmäisessä näytössä voit asettaa muutaman alueellisen parametrin, kuten näytön fontin ja merkkien koodauksen. Nämä asetukset ovat hyödyllisiä erityistapauksissa (ei-standardit näppäimistöt, sarjanäytöt, itämaiset kielet). Useimmissa asennuksissa kannattaa pitää oletusarvot ja valita "**Accept these Settings**".



![Image](assets/fr/002.webp)



### 4. Asennustavan valinta



Valitse "**Nopea/helppo asennus**", jos haluat suorittaa automaattisen asennuksen suositelluilla asetuksilla. Tämä menetelmä poistaa valitun levyn ja konfiguroi pfSensen oletusosioinnilla.



![Image](assets/fr/003.webp)



Näyttöön tulee varoitus, joka ilmoittaa, että kaikki levyllä olevat tiedot poistetaan. Vahvista valinta valitsemalla "**OK**".



Tämän jälkeen asennusohjelma kopioi tarvittavat tiedostot levylle. Laitteistosta riippuen tämä voi kestää muutamasta sekunnista muutamaan minuuttiin.



### 5. Ytimen valinta



Kun asennusohjelma pyytää sinua valitsemaan ytimen tyypin, jätä "**Standard Kernel**" valitsematta. Tämä yleinen ydin soveltuu täydellisesti tavallisiin käyttöönottoihin, olipa kyse sitten tietokoneesta, palvelimesta tai VM:stä.



### 6. Asennuksen päättyminen ja uudelleenkäynnistys



Kun asennus on valmis, valitse "**Reboot**" käynnistääksesi koneesi uudella pfSense-instanssilla.



**Tärkeä huomautus**: poista ISO-kuva tai irrota asennusmuistitikku ennen uudelleenkäynnistystä, jotta asennusohjelma ei käynnistyisi uudelleen seuraavalla käynnistyskerralla.



## IV. PfSensen käynnistäminen ensimmäistä kertaa



Ensimmäisen käynnistyksen yhteydessä pfSense on määritettävä tunnistamaan ja määrittämään oikein verkkoliitännät (WAN, LAN, DMZ, VLANit jne.). Verkkokorttien huolellinen tunnistaminen on tärkeää, jotta vältytään konfigurointivirheiltä, jotka voivat estää pääsyn Interface-verkkoon tai tehdä palomuurista toimimattoman.



Kun pfSense käynnistetään, se tunnistaa automaattisesti kaikki käytettävissä olevat verkkoliitännät ja listaa ne sekä ilmoittaa kunkin MAC Address:n. Näin ne on helppo erottaa toisistaan.



### 1. VLANit



Ensimmäinen kysymys koskee VLANien määritystä. Tässä vaiheessa peruskonfiguraatiota varten emme aktivoi mitään VLANeja. Paina siis "**N**"-näppäintä ohittaaksesi tämän vaiheen.



![Image](assets/fr/004.webp)



### 2. WAN ja LAN Interface Assignment



tämän jälkeen pfSense pyytää sinua määrittämään, mitä Interface:ta käytetään WAN-verkkoon (Internet-yhteys). Voit valita :





- Kirjoita Interface-nimi manuaalisesti (suositellaan virtuaaliympäristöissä).
- Käytä automaattista tunnistusta painamalla "**A**". Tämä vaihtoehto on käyttökelpoinen fyysisessä isännässä, jos verkkokaapelit on kytketty ja linkit ovat aktiivisia.



![Image](assets/fr/005.webp)



Tässä esimerkissä WAN määritetään manuaalisesti. Kirjoita Interface:n tarkka nimi. Intel-kortin nimi on FreeBSD:ssä usein "**em0**", mutta se voi vaihdella laitteistosta riippuen. Esimerkiksi Realtek-kortin nimi on usein "**re0**".



![Image](assets/fr/006.webp)



Toista sama toiminto Interface LAN:n määrittämiseksi. Tässä käytetään "**em1**".



pfSense vahvistaa, että Interface LAN aktivoi sekä palomuurin että NAT:n sisäverkon suojaamiseksi ja Address-käännöksen hallitsemiseksi.



Jos sinulla on muita fyysisiä liitäntöjä, voit määrittää tässä vaiheessa muita liitäntöjä (DMZ, Wi-Fi, tietyt VLANit). Kukin looginen Interface vaatii vastaavan verkkokortin tai virtuaalisen Interface:n. Alustavassa konfiguroinnissa rajoitumme WAN- ja LAN-liittymiin.



Kun määritykset on tehty, pfSense näyttää selkeän yhteenvedon fyysisten liitäntöjen ja määritettyjen roolien välisistä vastaavuuksista. Vahvista "**Y**".



### 3. PfSense-konsoli



Kun tämä vaihe on valmis, pfSense-konsolin päävalikko tulee näkyviin. Se tarjoaa useita hyödyllisiä vaihtoehtoja suoraa hallintaa varten, kuten web-salasanan palauttamisen, uudelleenkäynnistyksen, kokoonpanon uudelleenlataamisen tai liitäntöjen uudelleenmäärittämisen.



![Image](assets/fr/007.webp)



Näet myös yhteenvedon nykyisistä verkkoasetuksista, mukaan lukien Interface LAN:n oletus IP Address, yleensä **192.168.1.1.1**. Tämä on se Address, joka sinun on syötettävä selaimeesi päästäksesi Interface:n hallintasivustolle.



**Huomautus**: Jos sisäverkkosi käyttää eri Address-aluetta, valitse valikosta "**2)** Set Interface(s) IP Address" määrittääksesi ympäristöösi sopivan IP Address:n.



Jos Interface WAN on kytketty DHCP-konfiguroituun laatikkoon tai modeemiin, pfSense hakee automaattisesti julkisen IP-osoitteen Address. Näin ollen sinun pitäisi hyötyä välittömästä Internet-yhteydestä liittämällä asiakas pfSense Interface LAN:iin.



## V. Ensimmäinen pääsy Interface-verkkoon



Kun alustava käynnistys on suoritettu ja verkkoliitännät määritetty, voit käyttää pfSensen Interface-verkkoa viimeistelläksesi ja hienosäätääksesi kokoonpanosi.



### 1. Alkuperäinen yhteys



Kytke tietokone LAN-porttiin (tai hypervisorissa olevaan virtuaaliseen Interface LAN-porttiin) ja määritä sille tarvittaessa IP Address samalla alueella (oletusarvoisesti pfSense jakaa Address:n automaattisesti DHCP:n kautta LAN:ssa).



Siirry selaimessasi konsolin osoittamaan Address:een (oletusarvoisesti `https://192.168.1.1`). Huomaa, että pfSense vaatii HTTPS:n jopa ensimmäiselle yhteydelle - odota siis itse allekirjoitetun varmenteen varoitusta, jonka voit sivuuttaa lisäämällä poikkeuksen.



Kirjautumisnäyttö tulee näkyviin. Oletusarvoiset tunnukset ovat :




- Käyttäjänimi:** `admin`
- Salasana:** `pfsense`



Näitä tunnuksia muutetaan ohjatun alkukokoonpanon aikana.



## VI. Ohjattu asennus



Kun muodostat ensimmäisen yhteyden, pfSense kehottaa sinua noudattamaan **Ohjattua asennusohjelmaa**. Suosittelemme, että käytät sitä varmistaaksesi, että kaikki olennaiset parametrit on määritetty oikein.



### 1. Yleiset parametrit



Voit :




- Määritä isäntänimi ja paikallinen toimialue (esimerkki: `pfsense` ja `lan.local`).
- Määritä DNS-palvelimet ja valitse, käyttääkö pfSense palveluntarjoajan DNS:ää vai ulkoista palvelua (Cloudflare, OpenDNS, Quad9...).



### 2. Aikavyöhyke



Ilmoita sivustosi aikavyöhyke, jotta lokit ja aikataulut ovat yhdenmukaisia (esim. "Eurooppa/Pariisi").



### 3. WAN-konfiguraatio



Määritä WAN-yhteys :




- Oletusarvo on **DHCP** (riittävä, jos olet laatikon takana).
- Jos sinulla on kiinteä IP-osoite, syötä parametrit (staattinen IP, maski, yhdyskäytävä, DNS) manuaalisesti.
- Määritä tarvittaessa VLAN tai PPPoE-todennus (yleinen joillakin Internet-palveluntarjoajilla).



### 4. LAN-konfiguraatio



Ohjattu toiminto ehdottaa oletusarvoisen lähiverkon aliverkon muuttamista. Jos sinulla on tietty osoitesuunnitelma, nyt on aika mukauttaa se.



### 5. Vaihda järjestelmänvalvojan salasana



Suojaa pfSense asettamalla heti vahva salasana käyttäjälle `admin`.



## VII. Tarkastus ja päivitykset



Varmista ennen palomuurin käyttöönottoa, että sinulla on uusin versio :





- Siirry kohtaan **Järjestelmä > Päivitys**.
- Valitse päivityskanava (yleensä **Stable**).
- Tarkista päivitykset ja sovita ne.



On hyvä idea ottaa käyttöön päivitysilmoitukset, jotta pysyt ajan tasalla tietoturvakorjauksista.



## VIII. Konfiguraation tallentaminen



Ennen kuin teet suuria muutoksia, ota käyttöön varmuuskopiointikäytäntö:





- Siirry kohtaan **Diagnostiikka > Varmuuskopiointi ja palautus**.
- Lataa kopio nykyisestä kokoonpanosta (`config.xml`).
- Säilytä se turvallisessa paikassa (salattu ulkoinen tallennusväline).



Kriittisissä ympäristöissä kannattaa harkita automaattista konfiguraation varmuuskopiointia ulkoiselle palvelimelle tai ohjelmoidun skriptin avulla.



## IX. Parhaat käytännöt asennuksen jälkeen



Voit lopettaa komennuksesi mielenrauhassa :





- Muokkaa palomuurisääntöjä**: oletusarvoisesti pfSense sallii kaiken lähtevän liikenteen lähiverkossa ja estää saapuvan liikenteen WANissa. Muokkaa näitä sääntöjä tarpeen mukaan.
- Määritä suojattu etäkäyttö**: Ota Interface:n verkkoyhteys käyttöön WAN:sta vain VPN:n kautta tai IP-rajoitusten avulla, jos se on tarpeen.
- Ota ilmoitukset käyttöön**: määritä SMTP-palvelin vastaanottamaan ilmoituksia (epäonnistumiset, päivitykset, virheet).
- Asenna hyödyllisiä laajennuksia**: esimerkiksi IDS/IPS (Snort, Suricata), välityspalvelin (Squid), DNS-suodatus (pfBlockerNG).



PfSense-palomuurisi on nyt toiminnassa ja valmis suojaamaan verkkoasi. Sen joustavuuden ja aktiivisen yhteisön ansiosta sinulla on tehokas, skaalautuva työkalu, joka voi mukautua tuleviin tarpeisiisi (multi-WAN, VLAN, site-to-site VPN, captive portal jne.).



Tutustu säännöllisesti viralliseen dokumentaatioon ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) tutustuaksesi uusiin ominaisuuksiin ja varmistaaksesi, että kokoonpanosi on ajan tasalla ja turvallinen.