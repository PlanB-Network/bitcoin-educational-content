---
name: WireGuard
description: WireGuard VPN-i seadistamine Debianis ja Windowsis
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian BURNELi originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___



## I. Esitlus



Selles õpetuses õpime, kuidas konfigureerida VPN-i, mis põhineb WireGuardil, tasuta, avatud lähtekoodiga VPN-lahendusel, mis suurendab jõudlust, unustamata seejuures turvalisust.



WireGuard on suhteliselt hiljutine lahendus, mis on stabiilse versioonina saadaval alates 2020. aasta märtsist ning on olnud au integreerida otse **Linuxi kernelisse alates versioonist 5.6**. See ei takista selle kättesaadavust vanematest Linuxi distributsioonidest, mis kasutavad teistsugust tuuma versiooni. Võrreldes selliste lahendustega nagu OpenVPN ja IPSec, on WireGuard lihtsam kasutada ja palju kiirem, nagu me selle artikli lõpus näeme.



Mõned põhipunktid WireGuardi kohta:





- Lihtne, kerge ja ülitõhus!
- Ainult UDP-töö (mis võib olla ebasoodne teatud tulemüüride läbimisel)
- Töötab pigem peer-to-peer kui klient-server mudelil
- Autentimine võtme Exchange abil, samal põhimõttel nagu SSH privaatse/avaliku võtmega
- Mitmete algoritmide kasutamine: sümmeetriline krüpteerimine ChaCha20 abil, sõnumi autentimine Poly1305 abil, aga ka teiste, nagu Curve25519, BLAKE2 ja SipHash24
- Toetab nii IPv4 kui ka IPv6
- Multiplatvorm: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (ja rakendatud ProtonVPN-is)
- Ainult 4000 rida koodi, võrreldes sadade tuhandete teiste lahendustega



Krüptograafilise osa puhul on kasutatud erinevaid algoritme, mis on käsitsi valitud, mitmel viisil auditeeritud ja mida on uurinud selle valdkonna spetsialiseerunud turbeuurijad.



Projekti ametlik veebileht: [wireguard.com](https://www.wireguard.com/)



Kas olete pärast selle sissejuhatuse lugemist selles lahenduses veendunud? Siis ei jää üle muud, kui lugeda edasi!



## II. Labori WireGuard diagramm



Enne kui ma tutvustan oma laboratooriumi WireGuardi seadistamiseks, peaksite te teadma, et võite ette kujutada, et saate **kasutada WireGuardit kahe kauginfrastruktuuri ühendamiseks**, aga ka **ühendada kaugkliendi infrastruktuuriga, näiteks ettevõtte võrgu või koduvõrguga**. See on samas vaimus nagu OpenVPNi puhul, nagu me nägime hiljuti õpetuses "[OpenVPN Synologyl](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Kui WireGuard ei ole seadistatud otse ruuterisse või tulemüüri, nagu on mõeldav OpenWRT puhul, peate seadistama pordi edastamise, et voog jõuaks WireGuardi paarini.



![Image](assets/fr/034.webp)



Nüüd räägin teile oma laborist ja sellest, mida me täna üles seame.



Ma kavatsen kasutada Debian 11 masinat WireGuardi serverina ja Windowsi klienti WireGuardi VPN-kliendina. Kuigi on veidi eksitav rääkida kliendi ja serveri suhtest, sest **WireGuard töötab "peer-to-peer "** mudelil. See on veidi ekslik, kui püüate luua "klient-paik" ühendust. Ütleme selle asemel, et mul on kaks paari või **kahe WireGuardi ühenduspunkti**, kui soovite: üks Debian 11 all ja teine Windows'i all.



Need kaks paari saavad omavahel suhelda mõlemas suunas, mis tähendab, et minu Windows-masinast saan juurdepääsu Debian 11 masina kauglokaalile ja vastupidi: kõik sõltub tunneli konfiguratsioonist ja WireGuard'i vastasmüürist.



Selles näites keskendun ma järgmisele juhtumile: **Mina tahan oma koduvõrku ühendatud Windows Peer 1-st pääseda ettevõtte võrku, et pääseda WireGuard VPN-tunneli kaudu ettevõtte serveritesse**. See annab järgmise diagrammi:



![Image](assets/fr/035.webp)



IP-aadresside osas annab see:





- Koduvõrk**: 192.168.1.0/24
- Ettevõtte võrgustik**: 192.168.100.0/24
- WireGuard-tunnelivõrk**: 192.168.110.0/24


+ Peer 1 (Windows) IP Address tunnelis: 192.168.110.2/24


+ Peer 2 (Debian) IP Address tunnelis: 192.168.110.121/24



See on kõik, mis vaja! Läheme konfigureerimise juurde!



**Märkus: vaikimisi töötab WireGuard UDP-režiimis **port 51820**.



## III WireGuard serveri paigaldamine ja konfigureerimine



Ma kasutan selles õpetuses terminit "klient" Windowsi masina kohta ja "server" Debiani masina kohta, sest kuigi tegemist on peer-to-peer süsteemiga, tundub see tähenduslikum.



### A. WireGuardi paigaldamine Debian 11-le



WireGuardi paigalduspakett on saadaval ametlikus Debian 11 repositooriumis, seega tuleb vaid pakettide vahemälu uuendada ja paigaldada:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



Installeeritakse WireGuard'i serveri osa koos mitmesuguste tööriistadega, mis võimaldavad juurdepääsu kasulikele käskudele konfiguratsiooni haldamiseks.



### B. Interface WireGuard'i paigaldamine



Kasutades **käsku "wg "** peame generate privaatvõtme ja avaliku võtme: see on oluline kahe paari, st serveri ja kliendi (kes vajab samuti võtmepaari) vaheliseks autentimiseks.



Me loome privaatvõtme "**/etc/wireguard/wg-private.key**" ja avaliku võtme "**/etc/wireguard/wg-public.key**" selle käsureaga:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Avaliku võtme väärtus tagastatakse konsooli. WireGuard'i konfiguratsioonifailis tuleb **lisada meie privaatvõtme väärtus**. Selle väärtuse saamiseks sisestage alljärgnev käsk ja kopeerige väärtus:



```
sudo cat /etc/wireguard/wg-private.key
```



On aeg luua konfiguratsioonifail "**/etc/wireguard/**". Näiteks võime nimetada selle faili "**wg0.conf**", kui arvame, et WireGuardiga seotud Interface võrk on "wg0", näiteks samal põhimõttel nagu "eth0".



```
sudo nano /etc/wireguard/wg0.conf
```



Selles failis peame kõigepealt lisama järgmise sisu (tuleme hiljem tagasi, et seda täiendada):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Sektsiooni `[Interface]` kasutatakse serveriosa deklareerimiseks. Siin on mõned andmed:





- Address**: Interface WireGuardi IP Address VPN-tunnelis (erinev alamvõrgustik eemal asuvast LANist)
- SaveConfig**: konfiguratsioon salvestatakse (ja kaitstakse) seni, kuni Interface on aktiivne
- ListenPort**: WireGuard'i kuulav port. Antud juhul on vaikimisi port 51820, kuid võite seda kohandada
- PrivateKey**: meie serveri privaatvõtme väärtus (*wg-private.key*)



Salvestage fail ja sulgege see. Käsu "**wg-quick**" abil saame käivitada selle Interface, määrates selle nime (wg0, kuna faili nimi on wg0.conf):



```
sudo wg-quick up wg0
```



Kui te loetlete oma Debian 11 serveri IP-aadressid, näete uut Interface nimega "wg0", mille IP Address on määratud konfiguratsioonifailis:



```
ip a
```



![Image](assets/fr/027.webp)



Samas vaimus saame kuvada Interface "wg0" konfiguratsiooni käsuga "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Lõpuks peame aktiveerima meie Interface wg0 WireGuardi automaatse käivitamise:



```
sudo systemctl enable wg-quick@wg0.service
```



Jätame praegu kõrvale WireGuardi serveripoolse konfiguratsiooni.



### C. IP-edastuse lubamine



Selleks, et meie Debian 11 masin oleks võimeline **suundama pakette erinevate võrkude vahel (nagu ruuter)**, st VPN-võrgu ja kohaliku võrgu vahel, tuleb meil lubada [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Vaikimisi on see funktsioon välja lülitatud.



Muutke seda konfiguratsioonifaili:



```
sudo nano /etc/sysctl.conf
```



Lisage faili lõppu järgmine direktiiv ja salvestage:



```
net.ipv4.ip_forward = 1
```



See on kõik, mis on olemas.



### D. IP maskeeringu lubamine



Selleks, et meie server saaks pakette korrektselt suunata ja et Windows'i masinale oleks kauglooks kättesaadav, peame aktiveerima IP Masquerade'i meie Debian serveris. See on omamoodi NAT-i aktiveerimine. Ma teen selle konfiguratsiooni Linuxi tulemüüris läbi UFW, mida ma olen harjunud kasutama ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Kui teil ei ole veel UFW-d ja te soovite selle seadistada (võite kasutada ka Nftables'i), alustage:



```
sudo apt install ufw
```



Kõigepealt tuleb lubada SSH, et mitte kaotada kontrolli kaugserveri üle (kohandada pordi number):



```
sudo ufw allow 22/tcp
```



UDP port 51820 peab samuti olema lubatud, kuna me kasutame seda WireGuard'i jaoks (kohandage jällegi portnumbrit):



```
sudo ufw allow 51820/udp
```



Järgmisena jätkame IP-maskeri võimaldamiseks vajaliku konfiguratsiooniga. Selleks peame hankima kohaliku võrguga ühendatud Interface nime. Kui te ei tea nime, käivitage "ip a", et näha kaardi nime. Minu puhul on see kaart "**ens192**".



![Image](assets/fr/036.webp)



Me kasutame seda teavet. Redigeerige järgmist faili:



```
sudo nano /etc/ufw/before.rules
```



Lisage need read faili lõppu, et **võimaldada IP masquerade Interface ens192** (kohandage Interface nime) meie kohaliku tulemüüri NAT-tabeli POSTROUTING stringi sees:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Pildil on:



![Image](assets/fr/037.webp)



Hoidke see konfiguratsioonifail avatud ja jätkake järgmise sammuga 😉 



### E. Linuxi tulemüüri konfiguratsioon WireGuardile



Ikka samas konfiguratsioonifailis deklareerime ettevõtte võrgu "192.168.100.0/24", et saaksime sellega ühendust võtta. Siin on kaks reeglit, mis tuleb lisada (ideaalis pärast "*# ok icmp code for FORWARD*" sektsiooni, et reeglid oleksid grupeeritud):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Kui soovite autoriseerida ainult ühte host'i, näiteks "192.168.100.11", on see lihtne:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Nüüd saate faili salvestada ja sulgeda. Meie muudatuste rakendamiseks on vaja vaid UFW aktiveerida ja teenus taaskäivitada:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Debiani serveri seadistamise esimene osa on nüüd valmis.



## IV. WireGuard klient Windowsile



WireGuardi klient on saadaval Windows, macOS, Android jne... See on suurepärane uudis. Kõik allalaadimised on saadaval sellel leheküljel: [WireGuard Client](https://www.wireguard.com/install/). Selles näites seadistan kliendi Windowsis. WireGuardi kliendi seadistamiseks Linuxis järgige sama põhimõtet, mis Debian masina wg0.conf faili loomisel (ilma kogu NAT-i jne.).



### A. WireGuard Windowsi kliendi paigaldamine



Kui olete käivitatava faili või MSI-paketi alla laadinud, on paigaldamine lihtne: lihtsalt käivitage paigaldaja ja... voilà, valmis! 🙂 !



![Image](assets/fr/038.webp)



### B. Looge WireGuard-profiil



Alustage uue tunneli loomiseks tarkvara avamisega. Selleks klõpsake nupu "**Lisata tunnel**" paremal pool asuvat noolt ja vajutage nupule "**Lisata tühi tunnel**".



![Image](assets/fr/028.webp)



Avaneb konfiguratsiooniaken. Iga kord, kui luuakse uus tunneli konfiguratsioon, genereerib WireGuard selle konfiguratsiooni jaoks spetsiaalse privaatse/avaliku võtmepaari. **Selles konfiguratsioonis tuleb deklareerida "peer", st kaugserver:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Me peame selle konfiguratsiooni lõpule viima, eelkõige deklareerima IP Address sellel Interface-l (*Address*), aga ka deklareerima kauge WireGuard'i serveri [Peer] ploki kaudu. Allpool olev pilt peaks teile meenutama konfiguratsioonifaili, mille me lõime Linuxi serveri poolel.



Alustame blokist `[Interface]`, lisades IP Address "**192.168.110.2**"; pidage meeles, et serveril on selles võrgusegmendis IP Address "**192.168.110.121**". See annab:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Järgmisena peame deklareerima "Peer" ploki kolme omadusega, mille tulemuseks on järgmine konfiguratsioon:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



Piltidel:



![Image](assets/fr/029.webp)



** Mõningad selgitused [Peer] ploki kohta:





- PublicKey**: see on WireGuard Debian 11 serveri avalik võti (selle väärtuse saate kätte käsuga "*sudo wg*")
- AllowedIPs**: need on IP-aadressid / alamvõrgud, mis on kättesaadavad selle WireGuard VPN võrgu kaudu, käesoleval juhul minu WireGuard VPN-i (*192.168.110.0/24*) ja minu kauglokaalvõrgu (*192.168.100.0/24*) alamvõrk
- Endpoint**: see on Debian 11 host'i IP Address, kuna see on meie WireGuard'i ühenduspunkt (peate määrama avaliku IP Address)



Lõpuks sisestage nimi väljale "**Name**" (ilma tühikuteta) ning kopeerige ja kleepige kliendi avalik võti, kuna meil on vaja seda serveris deklareerida. Vajutage nupule "**Registreeri**".



### C. Kliendi deklareerimine WireGuard serveris



On aeg naasta Debian serverisse, et deklareerida "**Peer**", st meie Windowsi arvuti, WireGuard'i konfiguratsioonis. Kõigepealt peame **peatama Interface "wg0"**, et muuta tema konfiguratsiooni:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Seejärel muutke eelnevalt loodud konfiguratsioonifaili:



```
sudo nano /etc/wireguard/wg0.conf
```



Selles failis tuleb pärast `[Interface]-plokki deklareerida `[Peer]-plokk:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



See [Peer] plokk sisaldab Windows 10 arvuti avalikku võtit (**PublicKey**) ja arvuti Interface IP Address (**AllowedIPs**): server suhtleb selles WireGuard-tunnelis ainult Windows-kliendiga ühenduse võtmiseks, sellest ka väärtus "**192.168.110.2/32**".



Jääb vaid faili salvestamine (*CTRL+O, seejärel Enter, seejärel CTRL+X Nano kaudu*). Käivitage uuesti Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Et kontrollida, et peer-deklaratsioon töötab, saate kasutada seda käsku:



```
sudo wg show
```



Kui kaugkasutatav host on seadistanud oma WireGuard-ühenduse, viiakse selle IP Address üles "lõpp-punkti" väärtusele.



![Image](assets/fr/033.webp)



Lõpuks kindlustame konfiguratsioonifailid, et piirata juurkasutaja juurdepääsu:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Esimene WireGuard ühendus



Nüüd, kui konfiguratsioon on valmis, saame selle käivitada Windowsi arvutist. Selleks klõpsake "**WireGuard**" kliendis nupule "**Activate**": ühendus **muutub "Off"-st "On "**, kuid see ei tähenda, et see hakkab tööle. Kõik sõltub sellest, kas teie konfiguratsioon on õige või mitte. **Kui ühendus on loodud, suhtlevad meie kaks masinat Interface WireGuard'i kaudu, mis on konfigureeritud mõlemal poolel!



![Image](assets/fr/030.webp)



Probleemi korral on see nähtav vahekaardil "**Logiraamat**". Mõlemad hostid saadavad regulaarselt Exchange pakette, et kontrollida ühenduse staatust, sellest ka sõnumid "*Receiving keepalive packet from peer 1*" (*Võtab keepalive packet from peer 1*).



![Image](assets/fr/031.webp)



Kui WireGuardi vahekaardil "**Journal**" kuvatakse selline teade nagu allpool, peate kontrollima, et mõlemal poolel deklareeritud avalikud võtmed on õiged.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Ma saan oma kaugarvutist pingida oma Interface WireGuard'i IP Address serveripoolt ja ka minu kauglokaalvõrgus asuvat vastuvõtjat.



![Image](assets/fr/032.webp)



### E. Tulemuslikkus: OpenVPN vs WireGuard



Oma kaugarvutist, mis on ühendatud minu WireGuard VPN-iga, sain juurdepääsu failiserverile ja edastada faili [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/) kaudu, et näha ülekandekiirust. **WireGuardiga saavutan ma maksimaalselt umbes 45 Mb/s, mis on suurepärane, kuna ma olen WiFi võrgus



![Image](assets/fr/025.webp)



Samades tingimustes, kuid seekord OpenVPN-ühenduse (UDP-s) kaudu, on läbilaskevõime täiesti erinev: umbes 3 MB/s. Erinevus on ilmne!



![Image](assets/fr/026.webp)



See on huvitav, sest kui te näiteks vahetate WiFi-ühendusest 4G/5G-ühenduse vastu, toimub taasühendus nii kiiresti, et katkestust ei ole näha.



### F. Boonus: täielik tunneli WireGuard



Praeguse konfiguratsiooni puhul liigub osa liiklusest läbi VPN-i ja ülejäänud osa läbi kliendi internetiühenduse, sealhulgas interneti sirvimise. Kui me tahame lülituda WireGuardi **täieliku tunneli režiimi**, nii et kõik liigub läbi VPN-tunneli, peame tegema mõned muudatused oma konfiguratsioonis.....



Kõigepealt tuleb installeerida pakett "resolvconf":



```
sudo apt-get update
sudo apt-get install resolvconf
```



Kui see on tehtud, peate muutma profiili "wg0.conf" Debianis: peatage Interface, muutke seda ja käivitage uuesti.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Järgmisena **lisandame blokis `[Interface]` kasutatava DNS-serveri**. Minu puhul on see minu labori domeenikontroller, kuid me võime ka Debian'i masinale paigaldada Bind9, et saada kohalik resolver.



```
DNS = 192.168.100.11
```



Salvestage fail, seejärel käivitage Interface uuesti:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Lõpuks tuleb Windows 10 tööjaama tunneli konfiguratsioonis muuta jaotist "AllowedIPs" nii, et see näitaks, et kõik peab läbima tunneli. Asendage:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Autor:



```
AllowedIPs = 0.0.0.0/0
```



Näete, et see võimaldab ka valikut "**Tapa lüliti*".



![Image](assets/fr/040.webp)



Lõpuks kasutasin seda täielikku tunnelit ära, et teha väike voolukatsetus, mille tulemused on esitatud allpool:



![Image](assets/fr/039.webp)



WireGuard'i konfiguratsioon on üsna lihtne ja arusaadav ning ennekõike hooldatav. **WireGuardi peetakse VPNide tulevikuks**, nii et meil on parem sellel silma peal hoida! Samuti näeme, et eelis on märkimisväärne jõudluse osas, mis on WireGuardi suur eelis OpenVPN-i ees.



Täiendav dokumentatsioon:





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - käsk wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



** Teie WireGuard VPN on käivitatud ja töötab! Palju õnne!