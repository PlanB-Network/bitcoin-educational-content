---
name: pfSense
description: Pfsense'i paigaldamine
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian BURNELi originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Autori originaaltekstis on tehtud olulisi muudatusi, et õpetus oleks ajakohane.*



___



![Image](assets/fr/027.webp)



## I. Esitlus



pfSense on tasuta, avatud lähtekoodiga operatsioonisüsteem, mis muudab mis tahes arvuti, spetsiaalse serveri või riistvaralise seadme suure jõudlusega, hästi konfigureeritavaks ruuteriks ja tulemüüriks. FreeBSD-l põhinev ja oma stabiilse ja töökindla võrguarhitektuuri poolest tuntud pfSense on juba üle viieteistkümne aasta kehtestanud avatud lähtekoodiga tulemüüride standardid ettevõtetele, kohalikele asutustele ja nõudlikele kodukasutajatele.



Selle põhifunktsioonid on aastate jooksul märkimisväärselt edasi arenenud ja neid on iga uue versiooniga täiustatud. Praeguseks pakub pfSense:





- Täielik tsentraliseeritud haldamine kaasaegse, intuitiivse ja turvalise Interface veebi Interface kaudu.
- Suure jõudlusega stateful tulemüür, millel on täiustatud NAT-tugi (sh NAT-T) ja granuleeritud reeglite haldamine.
- Native multi-WAN tugi, mis võimaldab internetiühenduste koondamist või koondamist.
- Integreeritud DHCP-server ja relee.
- Kõrge kättesaadavus tänu CARP-protokollile, mis võimaldab ümberlülitamist ja pfSense'i klastrite konfigureerimist.
- Koormuse tasakaalustamine mitme ühenduse või serveri vahel.
- Täielik VPN-tugi: IPsec, OpenVPN ja WireGuard (asendades L2TP, mis on nüüdseks vananenud): IPsec, OpenVPN ja WireGuard.
- Konfigureeritav kinnine portaal külaliste juurdepääsu kontrollimiseks, eriti avalikus või hotellikeskkonnas.



pfSense'il on ka laiendatav paketisüsteem, mis võimaldab hõlpsasti lisada täiustatud funktsioone, nagu läbipaistev proxy (Squid), URL-filtreerimine või IDS/IPS (Snort või Suricata) otse Interface veebist.



pfSense'i levitatakse ainult 64-bitiste platvormide jaoks, mis on kooskõlas praeguste FreeBSD soovitustega. Seda saab installeerida standardsele riistvarale (arvutid, rack-serverid) või väikese võimsusega varjatud platvormidele, nagu Netgate'i seadmed või teatud madala profiiliga x86-kastid, mis on palju võimsamad kui vanemad Alix-kastid.



Lõpuks tasub meeles pidada, et pfSense vajab vähemalt kahte füüsilist võrguliidest: üks on määratud välisvõrgule (WAN) ja teine sisevõrgule (LAN). Sõltuvalt teie infrastruktuuri keerukusest (DMZ, VLAN, mitu WANi) võib selle võimaluste täielikuks ärakasutamiseks olla vajalik mitu lisaliidest.



## II. Pildi allalaadimine



Selle õpetuse kirjutamise ajal on pfSense'i viimane stabiilne versioon 2.8 (avaldatud juunis 2025). ISO-kujutise või teie riistvarakeskkonnale kohandatud paigaldusfaili saate alla laadida otse ametlikust veebisaidist:





- [Download pfSense](https://www.pfsense.org/download/)



Allalaadimisportaal võimaldab teil valida:





- Arhitektuur (üldiselt **AMD64** kõigi kaasaegsete seadmete puhul).
- Pildi tüüp (**Installer USB Memstick** USB-pulga kaudu paigaldamiseks, **ISO Installer** põletamiseks või virtuaalseks redigeerimiseks).
- Lähim allalaadimispeegel, et optimeerida ülekandekiirust.



Neile, kes soovivad pfSense'i kasutusele võtta virtualiseeritud keskkonnas (Proxmox, VMware ESXi, VirtualBox...), on saadaval ka **OVA** kujutis. See kasutusvalmis virtuaalmasin lihtsustab oluliselt paigaldamist ja esialgset seadistamist. Veenduge vaid, et kohandate eraldatud ressursse (protsessor, RAM, võrguliidesed) vastavalt eeldatavale koormusele ja võrgutopoloogiale.



Enne paigaldamist soovitame kontrollida allalaetud faili terviklikkust, kontrollides ametlikul allalaadimislehel esitatud **SHA256**. Sellega tagatakse, et kujutist ei ole muudetud ega rikutud.



## III. Paigaldamine



Selles näites toimub paigaldamine virtuaalmasinasse, kus töötab VirtualBox. Protseduur jääb füüsilises masinas või mõnes muus hüperviisoris rangelt samaks, välja arvatud virtuaalse seadme haldamine.



### 1. Minimaalsed nõuded riistvarale



Standardse kasutuselevõtu puhul soovitame:





- vähemalt 1 GB RAM** (lisapakettide või ZFS-toe võimaldamiseks on soovitatav 2 GB või rohkem).
- 8 GB kettaruumi** (20 GB või rohkem on soovitav keerukamate konfiguratsioonide puhul, eriti kui paigaldate proxy vahemälu, IDS/IPS või üksikasjalikud logid).
- Vähemalt kaks virtuaalset võrguliidest** (üks WAN-i ja üks LAN-i jaoks). VirtualBoxis lisage need enne käivitamist VM-i seadistustesse.



### 2. Paigaldaja käivitamine



Paigaldage allalaetud ISO-kujutis virtuaalse optilise kettana VirtualBoxi või sisestage USB-mälu, kui installite füüsilisele masinale. Käivitamisel ilmub käivitamismenüü:



Kui te ei vali ühtegi valikut, käivitub pfSense mõne sekundi pärast automaatselt vaikimisi seadistustega. Vajutage klahvi "**Enter**", et alustada tavapärast käivitamist.



![Image](assets/fr/027.webp)



Kui ilmub peamenüü, vajutage kiiresti nuppu "**I**", et alustada paigaldamist.



![Image](assets/fr/001.webp)



### 3. Esialgse paigaldaja seaded



Esimesel ekraanil saate määrata mõned piirkondlikud parameetrid, näiteks kuvatava kirjastiili ja tähemärkide kodeerimise. Need seaded on kasulikud erijuhtudel (mittestandardsed klaviatuurid, jadaekraanid, idamaade keeled). Enamiku paigalduste puhul jätke vaikeväärtused alles ja valige "**Accept these Settings**".



![Image](assets/fr/002.webp)



### 4. Paigaldusrežiimi valik



Valige "**Kiire/lihtne paigaldus**", et käivitada automaatne paigaldus soovitatud valikutega. See meetod kustutab valitud ketta ja konfigureerib pfSense'i vaikimisi partitsioneerimisega.



![Image](assets/fr/003.webp)



Ilmub hoiatus, mis näitab, et kõik kettal olevad andmed kustutatakse. Kinnitage "**OK**".



Seejärel kopeerib paigaldaja vajalikud failid kettale. Sõltuvalt teie riistvarast võib see võtta aega mõnest sekundist kuni mõne minutini.



### 5. Tuumade valik



Kui paigaldaja palub teil valida tuumaliigi, jätke valikuks "**Standardne tuum**". See üldine tuum sobib ideaalselt standardseks kasutuselevõtuks, olgu see siis arvutis, serveris või VM-is.



### 6. Paigaldamise lõpp ja taaskäivitamine



Kui paigaldus on lõpetatud, valige "**Reboot**", et taaskäivitada masin uues pfSense'i instantsis.



**Tähtis märkus**: eemaldage ISO-kujutis või ühendage paigaldamise USB-mälu enne taaskäivitamist lahti, et vältida paigaldusprogrammi taaskäivitamist järgmisel käivitamisel.



## IV. PfSense'i esmakordne käivitamine



Esmakordsel käivitamisel tuleb pfSense'i konfigureerida nii, et see tuvastaks ja määraks õigesti oma võrguliidesed (WAN, LAN, DMZ, VLANid jne). Teie võrgukaartide hoolikas tuvastamine on oluline, et vältida konfiguratsioonivigu, mis võivad jätta teid ilma juurdepääsust Interface veebile või muuta teie tulemüüri kasutamiskõlbmatuks.



Käivitamisel tuvastab pfSense automaatselt kõik olemasolevad võrguliidesed ja loetleb need, näidates igaühele MAC Address. See muudab nende eristamise lihtsaks.



### 1. VLANid



Esimene küsimus puudutab VLANide konfigureerimist. Selles etapis ei aktiveeri me põhikonfiguratsiooni puhul ühtegi VLANi. Seega vajutage klahvi "**N**", et see samm vahele jätta.



![Image](assets/fr/004.webp)



### 2. WAN ja LAN Interface Assignment



seejärel palub pfSense teil määrata, millist Interface kasutatakse WANi (Interneti-ühendus) jaoks. Saate valida järgmiste valikute vahel:





- Sisestage Interface nimi käsitsi (soovitatav virtuaalsete keskkondade puhul).
- Kasutage automaatset tuvastamist, vajutades "**A**". See valik on kasulik füüsilisel hostil, tingimusel, et teie võrgukaablid on ühendatud ja lingid on aktiivsed.



![Image](assets/fr/005.webp)



Selles näites konfigureerime WANi käsitsi. Sisestage Interface täpne nimi. Inteli plaadi puhul on nimi FreeBSD all sageli "**em0**", kuid see võib sõltuvalt riistvarast erineda. Näiteks Realteki kaardi puhul kuvatakse sageli "**re0**".



![Image](assets/fr/006.webp)



Korrake sama toimingut Interface LANi määramiseks. Siinkohal kasutame "**em1**".



pfSense kinnitab, et Interface LAN aktiveerib nii tulemüüri kui ka NATi, et kaitsta teie sisevõrku ja hallata Address tõlkimist.



Kui teil on muid füüsilisi liideseid, saate selles etapis konfigureerida täiendavaid liideseid (DMZ, Wi-Fi, konkreetsed VLANid). Iga loogiline Interface vajab vastavat võrgukaarti või virtuaalset Interface. Esialgseks konfiguratsiooniks piirdume WANi ja LANiga.



Kui määramine on lõpule viidud, kuvab pfSense selge kokkuvõtte füüsiliste liideste ja määratud rollide vahelisest vastavusest. Kinnitage "**Y**".



### 3. PfSense konsool



Kui see samm on lõpetatud, ilmub pfSense'i konsooli peamenüü. See pakub mitmeid kasulikke võimalusi otseseks haldamiseks, näiteks veebiparooli lähtestamine, taaskäivitamine, konfiguratsiooni uuesti laadimine või liideste ümberjaotamine.



![Image](assets/fr/007.webp)



Samuti näete kokkuvõtet praegustest võrguseadetest, sealhulgas Interface LANi vaikimisi IP Address, tavaliselt **192.168.1.1.1**. See on Address, mille peate sisestama oma brauserisse, et pääseda Interface haldusvõrku.



**Märkus**: Kui teie sisevõrk kasutab teistsugust Address vahemikku, valige menüüst "**2)** Set Interface(s) IP Address", et määrata teie keskkonnale sobiv IP Address.



Kui teie Interface WAN on vaikimisi ühendatud DHCP-konfigureeritud kasti või modemiga, küsib pfSense automaatselt avaliku IP-aadressi Address. Seega peaksite saama kasu kohesest Interneti-ühendusest, kui ühendate kliendi pfSense Interface LANiga.



## V. Esimene juurdepääs Interface veebile



Kui esialgne käivitamine on lõpule viidud ja võrguliidesed konfigureeritud, saate juurdepääsu pfSense'i Interface veebile, et viimistleda ja peenhäälestada oma konfiguratsiooni.



### 1. Esialgne ühendus



Ühendage arvuti LAN-porti (või hüperviisori virtuaalsesse Interface LAN-i) ja määrake talle vajadusel samas vahemikus IP Address (vaikimisi jaotab pfSense automaatselt Address DHCP kaudu LAN-i).



Mine oma brauseris konsooli poolt näidatud Address (vaikimisi `https://192.168.1.1`). Pange tähele, et pfSense nõuab HTTPS-i isegi esimese ühenduse puhul - seega oodake hoiatust isesigneeritud sertifikaadi kohta, mida saate ignoreerida, lisades erandi.



Ilmub sisselogimisekraan. Vaikimisi kasutajatunnused on:




- Kasutajanimi:** `admin`
- Parool:** `pfsense`



Neid identifikaatoreid muudetakse esialgse konfiguratsioonivõti käigus.



## VI. Viisardiga seadistamine



Esimesel ühendamisel palub pfSense teil järgida selle **seadistamise juhti**. Soovitame tungivalt kasutada seda, et kõik olulised parameetrid oleksid õigesti määratletud.



### 1. Üldised parameetrid



Saate:




- Määrake hostinimi ja kohalik domeen (näiteks: `pfsense` ja `lan.local`).
- Määrake DNS-serverid ja valige, kas pfSense peaks kasutama teie Interneti-teenusepakkuja DNS-i või välist teenust (Cloudflare, OpenDNS, Quad9...).



### 2. Ajavöönd



Märkige oma saidi ajavöönd, et logid ja ajakava oleksid järjepidevad (nt "Euroopa/Pariis").



### 3. WAN konfiguratsioon



WAN-ühenduse konfigureerimine:




- Vaikimisi on **DHCP** (piisav, kui olete kasti taga).
- Kui teil on fikseeritud IP, sisestage parameetrid (staatiline IP, mask, värav, DNS) käsitsi.
- Vajaduse korral määratlege VLAN või PPPoE-autentimine (levinud mõne ISP puhul).



### 4. LANi konfiguratsioon



Nõustaja soovitab muuta vaikimisi LANi alamvõrku. Kui teil on konkreetne aadressiplaan, on nüüd aeg seda kohandada.



### 5. Administraatori parooli muutmine



Kaitske oma pfSense'i, määrates kohe tugeva parooli kasutajale `admin`.



## VII. Kontrollimine ja ajakohastamine



Enne tulemüüri kasutuselevõttu veenduge, et teil on uusim versioon:





- Mine **Süsteem > Uuendamine**.
- Valige uuenduskanal (tavaliselt **Stabiilne**).
- Kontrollige uuendusi ja rakendage neid.



On hea mõte lubada uuendusteateid, et hoida teid kursis turvaparandustega.



## VIII. Konfiguratsiooni salvestamine



Enne suuremate muudatuste tegemist rakendage varunduspoliitikat:





- Mine **Diagnostika > Varundamine ja taastamine**.
- Laadige alla praeguse konfiguratsiooni koopia (`config.xml`).
- Hoidke seda turvalises kohas (krüpteeritud väline andmekandja).



Ärikriitiliste keskkondade puhul tuleks kaaluda konfiguratsiooni automaatset varundamist välises serveris või programmeeritud skripti abil.



## IX. Parimad tavad pärast paigaldamist



Et lõpetada oma kasutuselevõtt rahulikult:





- Muuda tulemüüri reegleid**: vaikimisi lubab pfSense kogu väljaminevat liiklust LAN-is ja blokeerib sissetuleva liikluse WAN-is. Kohandage neid reegleid vastavalt vajadusele.
- Konfigureerige turvaline kaugjuurdepääs**: vajaduse korral lubage juurdepääs Interface veebile WANist ainult VPN-i kaudu või IP-piirangutega.
- Teavituste lubamine**: konfigureerige SMTP-server, et saada teateid (tõrked, uuendused, vead).
- Paigaldage kasulikud laiendused**: näiteks IDS/IPS (Snort, Suricata), proxy (Squid), DNS-filtreerimine (pfBlockerNG).



Teie pfSense'i tulemüür on nüüd töökorras ja valmis kaitsma teie võrku. Tänu selle paindlikkusele ja aktiivsele kogukonnale on teil võimas ja skaleeritav vahend, mis suudab kohaneda teie tulevaste vajadustega (multi-WAN, VLAN, site-to-site VPN, captive portal jne).



Tutvuge regulaarselt ametliku dokumentatsiooniga ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)), et avastada uusi funktsioone ja veenduda, et teie konfiguratsioon on ajakohane ja turvaline.