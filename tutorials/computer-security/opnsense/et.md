---
name: OPNsense
description: Kuidas paigaldada ja konfigureerida OPNsense'i tulemüüri?
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian BURNELi originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___



## I. Esitlus



Selles õpetuses vaatleme avatud lähtekoodiga tulemüüri OPNsense. Vaatame selle peamisi funktsioone, eeldusi ja seda, kuidas seda FreeBSD-põhist lahendust paigaldada.



Enne alustamist peaksite teadma, et **OPNsense ja pfSense on mõlemad avatud lähtekoodiga tulemüürid**, mis põhinevad FreeBSD-l. Võib öelda, et pfSense on omamoodi OPNsense'i suur vend, kuna viimane on 2015. aastal loodud Fork. Lõpetuseks on oluline märkida, et alates 2017. aastast on **OPNsense läinud üle HardenedBSD-le FreeBSD asemel**. HardenedBSD on FreeBSD täiustatud versioon, millel on täiustatud turvaelemendid



OPNsense paistab silma oma kaasaegsema kasutaja Interface ja **sagedasema uuenduste sageduse** poolest. OPNsense'i uuenduste ajakava hõlmab tõepoolest kaks peamist versiooni aastas, mida uuendatakse umbes iga kahe nädala tagant (mille tulemuseks on väiksemad versioonid). See jälgimine on väga huvitav võrreldes pfSense'iga, kui vaatame nende lahenduste kogukonnaversioone.



![Image](assets/fr/050.webp)



## II. OPNsense'i omadused



OPNsense on operatsioonisüsteem, mis on mõeldud toimima tulemüüri ja marsruuterina, kuigi selle funktsioone on palju ja neid saab laiendada lisapakettide paigaldamisega. Tootmiskasutuseks sobiv, seda kasutatakse peamiselt võrgu turvalisuse ja voogude haldamiseks.



### A. Peamised omadused



Siin on mõned OPNsense'i peamised funktsioonid:





- Tulemüür ja NAT**: OPNsense pakub täiustatud tulemüürifunktsioone koos staatilise filtreerimisega, samuti võrgu Address-tõlkimise (NAT) võimalusi.





- DNS/DHCP**: OPNsense saab seadistada DNS- ja DHCP-teenuste haldamiseks võrgus. See võib toimida DHCP-serverina, kuid seda saab kasutada ka DNS-resolverina kohaliku võrgu masinate jaoks. Dnsmasq on samuti vaikimisi integreeritud.





- VPN**: OPNsense toetab mitmeid VPN-protokolle, sealhulgas IPsec, OpenVPN ja WireGuard, võimaldades turvalisi ühendusi mobiilse tööjaama kaugjuurdepääsuks või saitidevaheliseks ühendamiseks.





- Veebivahendaja**: OPNsense sisaldab veebivahendajat, et kontrollida ja filtreerida juurdepääsu Internetile. Seda saab kasutada ka sisu filtreerimiseks ja võrgule juurdepääsu haldamiseks.





- Ribalaiuse haldamine (QoS)**: OPNsense pakub teenusekvaliteedi (QoS) juhtimise funktsioone, et seada võrguliikluse prioriteedid ja hallata paremini võrgu ribalaiust.





- Kinnipeetav portaal**: see funktsioon võimaldab teil hallata kasutajate juurdepääsu võrku autentimislehe kaudu (kohalik baas, vautšerid jne). See on funktsioon, mida tavaliselt kasutatakse avalike Wi-Fi-võrkude puhul.





- IDS/IPS**: OPNsense integreerib Suricata, et pakkuda sissetungide tuvastamise ja ennetamise (IDS/IPS) funktsioone, et kaitsta võrku rünnakute eest.





- Kõrge kättesaadavus (CARP)**: OPNsense toetab CARP-i (*Common Address Redundancy Protocol*) mitme OPNsense'i tulemüüri vahelise kõrge kättesaadavuse tagamiseks, tagades, et teenus jääb aktiivseks ka riistvararikke korral.





- Aruandlus ja järelevalve**: OPNsense pakub reaalajas aruandlus- ja seirevahendeid võrgu jõudluse jälgimiseks (NetFlow abil) ja võimalike probleemide avastamiseks tänu logide loomisele. See hõlmab ka graafikat. Monit tööriist on integreeritud OPNsense'ile ja võimaldab järelevalvet tulemüüri enda üle.



### B. Täiendavad paketid



See on vaid ülevaade OPNsense'i pakutavatest funktsioonidest. Lisaks sellele võimaldab **pakettide kataloog**, millele on juurdepääs OPNsense'i administreerimise Interface kaudu, **rikastada tulemüüri täiendavate funktsioonidega**. Nende hulka kuuluvad ACME klient, Wazuh agent, NTP Chrony teenus ja Caddy kui pöördproxy.



![Image](assets/fr/051.webp)



## III. OPNsense'i eeldused



Kõigepealt peate otsustama, kuhu te OPNsense'i paigaldate. On mitmeid võimalikke lahendusi, sealhulgas paigaldamine:





- Hüperviisor kui virtuaalne masin, olgu selleks siis Hyper-V, Proxmox, VMware ESXi jne.
- Masin kui *jääkmetallist* süsteem. See võiks olla miniarvuti, mis toimib tulemüürina.



Meie veebipoest saate osta ka **OPNsense'i rack-monteeritava seadme**.



Te peate arvestama OPNsense'i käivitamiseks vajalike riistvararessurssidega. Seda on üksikasjalikult kirjeldatud [sellel dokumentatsiooni leheküljel](https://docs.opnsense.org/manual/hardware.html).



**Miinimum- ja soovitatavad tootmisvahendid:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Lõpuks, ** teie ressursivajadused sõltuvad eelkõige hallatavate ühenduste arvust** ja seega ** teie ribalaiusevajadustest**. Lisaks sellele peate **silmas pidama aktiveeritavaid ja kasutatavaid teenuseid** (proxy, sissetungi tuvastamine jne...), kuna need võivad olla protsessori ja/või RAM-i nõudvad.



Samuti vajate OPNsense'i paigaldamise ISO-kujutist, mille saate alla laadida [ametlikust veebisaidist](https://opnsense.org/download/). VM-i paigaldamiseks valige ISO image'i saamiseks (ja tehke sellega, mida soovite...) image'i tüübiks "**dvd**". Paigaldamiseks käivitatava USB-mäluseadme kaudu valige "**vga**", et saada "**.img**" fail.



![Image](assets/fr/048.webp)



OPNsense'i haldamiseks ja testimiseks on vaja ka arvutit.



## IV. Sihtkonfiguratsioon



Meie eesmärk on





- Looge sisemine virtuaalne võrk (192.168.10.0/24 - LAN)**, mis pääseb OPNsense'i tulemüüri kaudu Internetti. Tootmiskasutuses võib see olla teie kohalik võrk, kaabel ja/või Wi-Fi.
- Aktiveerige ja konfigureerige NAT**, et virtuaalsed virtuaalsed virtuaalvõrgud pääseksid internetti
- Aktiveerige ja konfigureerige OPNsense** DHCP-server, et jagada IP-konfiguratsiooni tulevastele masinatele, mis on ühendatud sisemise virtuaalvõrguga
- Konfigureerige tulemüür** nii, et see lubab ainult väljaminevaid LANi ja WANi vahelisi voogusid HTTP (80) ja HTTPS (443).
- Konfigureerige tulemüür**, et lubada virtuaalsel lähivõrgul kasutada OPNsense'i DNS-resolverina (53).



Kui te kasutate Hyper-V platvormi, annab see teile järgmise kujutise:



![Image](assets/fr/033.webp)



## V. OPNsense'i tulemüüri paigaldamine



### A. Käivitatava USB-mäluseadme ettevalmistamine



Esimene samm on paigalduskandja ettevalmistamine: **Bootitav USB-mäluseade koos OPNsense'iga**. See on muidugi vabatahtlik, kui te töötate virtuaalses keskkonnas, kuid igal juhul peate te alla laadima OPNsense'i paigaldamise ISO-kujutise.



Pärast allalaadimist saate **arhiivi, mis sisaldab pilti ".img "** formaadis. Saate **luua käivitatava USB-pulga** erinevate rakendustega, sealhulgas **balenaEtcher**: väga lihtne kasutada. Veelgi enam, rakendus tunneb arhiivis oleva kujutise ära, nii et te ei pea seda eelnevalt lahti pakkima.





- [Lae alla balenaEtcher](https://etcher.balena.io/)



Kui rakendus on paigaldatud, valige oma pilt, USB-mäluseade ja seejärel klõpsake "Flash! Oodake hetk.



![Image](assets/fr/049.webp)



Nüüd olete valmis paigaldama.



### B. OPNsense süsteemi paigaldamine



Käivitage masin, kus asub OPNsense. Te peaksite nägema allpool esitatud lehele sarnast tervituslehte. Mõne sekundi jooksul on aknas näha näidatud ekraan. Laske protsessil kulgeda...



![Image](assets/fr/019.webp)



OPNsense'i kujutis laaditakse masinasse, nii et süsteemi saab kasutada "**live**"-režiimis, st ajutiselt mällu salvestatud kujul.



![Image](assets/fr/025.webp)



Siis jõuate Interface-ni, mis on sarnane alljärgnevale. Logige sisse kasutajanimega "**installer**" ja parooliga "**opnsense**". Pange tähele, et klaviatuur on hetkel **QWERTY**. Siinkohal **alustame OPNsense'i paigaldusprotsessi**.



![Image](assets/fr/026.webp)



Ekraanile ilmub uus nõustaja. Esimene samm on valida teie konfiguratsioonile vastav klaviatuuri paigutus. AZERTY-klaviatuuri puhul valige nimekirjast valik "**French (accent keys)**", seejärel tehke topeltklõps**.



![Image](assets/fr/027.webp)



Teine samm on sooritatava ülesande valimine. Siinkohal teeme paigalduse, kasutades **ZFS-failisüsteemi**. Asetage end reale "**Install (ZFS)**" ja kinnitage **Enteriga**.



![Image](assets/fr/028.webp)



Kolmandas etapis valige "**riba**", kuna meie masin on varustatud **ainsa kettaga**: tulekindlate salvestusruumide ja nende andmete kaitsmiseks ei ole võimalik kasutada redundantsust. See on eriti oluline füüsilisele masinale paigaldamisel, et kaitsta ühe ketta riistvaralise rikke eest RAID-põhimõtte abil.



![Image](assets/fr/029.webp)



Neljandas etapis vajutage kinnitamiseks lihtsalt **Enter**.



![Image](assets/fr/030.webp)



Lõpuks kinnitage, valides "**Ja**" ja vajutades seejärel klahvi **Enter**.



![Image](assets/fr/031.webp)



Nüüd peate ootama, kuni OPNsense paigaldatakse... See protsess võtab umbes 5 minutit.



![Image](assets/fr/032.webp)



Kui paigaldus on lõpetatud, saame enne taaskäivitamist muuta "**juur**" parooli. Valige "**Root Password**", vajutage **Enter** ja sisestage kaks korda parool "**root**".



![Image](assets/fr/020.webp)



Lõpuks valige "**Täielik paigaldus**" ja vajutage **Enter**. Kasutage seda võimalust, et **heitke ketas VM-i DVD-ajamilt välja**. VM-i seadetes saate määrata ka esimese käivitamise kettale.



![Image](assets/fr/021.webp)



Virtuaalmasin taaskäivitub ja laeb OPNsense'i süsteemi kettalt, sest me oleme selle just paigaldanud. Logige sisse konsooli "root" kontoga ja oma uue parooliga (muidu on vaikimisi parool "**opnsense**").



### D. Võrguliideste ühendamine



Ilmub allpool näidatud ekraan. Valige "**1**" ja vajutage **Enter**, et seostada masina võrgukaardid OPNsense'i liideseid.



![Image](assets/fr/022.webp)



Esmalt palub viisard teil konfigureerida linkide koondamine ja VLANid. Keeldumiseks määrake "**n**" ja kinnitage iga kord oma vastus klahviga **Enter**. Järgmisena peate määrama kaks liidest "**hn0**" ja "**hn1**" **WANile** ja **LANile**. Põhimõtteliselt vastab "**hn0**" WANile ja teine Interface LANile.



See toimib järgmiselt:



![Image](assets/fr/023.webp)



Meil on nüüd:





- Interface **LAN**, mis on seotud võrgukaardiga "**hn1**" ja OPNsense'i vaikimisi IP Address, st **192.168.1.1/24**.
- Interface **WAN**, mis on seotud võrgukaardiga "**hn0**" ja IP Address, mis on saadud **DHCP** kaudu kohalikust võrgust (tänu meie välisele virtuaalsele lülitile).



Vaikimisi on OPNsense'i haldus Interface ilmselgetel turvalisuse kaalutlustel kättesaadav ainult LAN Interface-st. Seetõttu peate administreerimiseks ühenduma tulemüüri Interface LANi. Kui see ei ole võimalik, saate OPNsense'i ajutiselt WANist hallata. See hõlmab tulemüüri funktsiooni väljalülitamist.



Selleks lülituge shell-režiimi valikuga "**8**" ja käivitage järgmine käsk:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Juurdepääs OPNsense Interface juhtimissüsteemile



OPNsense Administration Interface-le saab juurdepääsu HTTPS-i kaudu, kasutades LAN** Interface (või WAN) IP Address. Brauser viib teid sisselogimislehele. Logige sisse varem valitud "root" konto ja parooliga.



![Image](assets/fr/034.webp)



Oodake paar sekundit... Teil palutakse järgida nõustaja juhiseid põhikonfigureerimise teostamiseks. Jätkamiseks klõpsake "**Järgmine**".



![Image](assets/fr/036.webp)



Esimene samm on määrata hostinimi, domeeninimi, valida keel ja määrata DNS-server(id), mida kasutatakse nimede lahendamiseks. Valiku "**Enable Resolver**" säilitamine võimaldab tulemüüri kasutada DNS-resolverina, mis on kasulik meie virtuaalse LANi masinate jaoks.



![Image](assets/fr/037.webp)



Jätkake järgmise sammuga. Nõustaja annab teile võimaluse **määrata NTP-server kuupäeva ja kellaaja sünkroniseerimiseks**, kuigi vaikimisi on serverid juba konfigureeritud. Lisaks on oluline valida teie geograafilisele asukohale vastav ajavöönd (kui teil ei ole erinõudeid).



![Image](assets/fr/038.webp)



Seejärel tuleb oluline samm: **Interface WANi konfigureerimine**. Praegu on see konfigureeritud DHCP-süsteemis ja jääb sellesse konfiguratsioonirežiimi, kui te ei soovi määrata staatilist IP-d Address-le.



![Image](assets/fr/039.webp)



Interface WANi konfiguratsioonilehel tuleb endiselt eemaldada valik "**Blokeerida juurdepääs privaatvõrkudele WANi kaudu**", kui WANi poolne võrk kasutab privaatset adresseerimist. Tõenäoliselt on see nii, kui te kasutate laboratooriumi, ja seega võib see takistada juurdepääsu Internetile.



![Image](assets/fr/040.webp)



Järgmisena saate **määrata "root "** parooli, kuid see on vabatahtlik, sest me oleme seda juba teinud.



![Image](assets/fr/041.webp)



Jätkake lõpuni, et algatada konfiguratsiooni ümberlaadimine. Kui teil on vaja jätkata juhtimise võtmist WAN-i kaudu, käivitage ülaltoodud käsk uuesti, kui see protsess on lõppenud.



![Image](assets/fr/042.webp)



See on kõik, mis vaja!



![Image](assets/fr/035.webp)



### E. DHCP konfiguratsioon



Meie eesmärk on kasutada OPNsense DHCP-serverit IP-aadresside jagamiseks virtuaalses lähivõrgus. Selleks on meil vaja juurdepääsu sellele menüükohale:



```
Services > ISC DHCPv4 > [LAN]
```



**Kui näete, on DHCP juba vaikimisi LAN-is lubatud ** Kui te ei ole sellest teenusest huvitatud, siis lülitage see välja. Kuigi see on juba sisse lülitatud ja me tahame seda kasutada, on oluline selle konfiguratsioon üle vaadata.



Vajaduse korral saate muuta jaotatavate IP-aadresside vahemikku: **192.168.10.10** kuni **192.168.10.10.245**, sõltuvalt praegustest seadetest.



![Image](assets/fr/046.webp)



Samuti näeme, et väljad "**DNS serverid**", "**värav**", "**domeeninimi**" jne. on vaikimisi tühjad. Tegelikult on nende erinevate väljade jaoks olemas teatud valikute ja vaikeväärtuste automaatne pärimine. Näiteks DNS-serveri puhul jagatakse Interface LANi IP Address, mis võimaldab OPNsense'i tulemüüri kasutada DNS-resolverina.



Pärast muudatuste tegemist salvestage vajaduse korral konfiguratsioon.



![Image](assets/fr/047.webp)



DHCP-serveri testimiseks peate ühendama masina oma tulemüüri LAN-võrku.



See masin peab saama OPNsense DHCP-serverist IP Address ja meie masin peab saama juurdepääsu võrgule. Interneti-ühendus peab toimima. Pange tähele, et kui te olete OPNsense'ile WAN-ist juurdepääsuks keelanud tulemüüri funktsiooni, siis lülitab see NAT-i välja, mis takistab juurdepääsu veebile.



**Hoiatus**: hetkel väljastatud DHCP-liisingud on nähtavad OPNsense'i administratsioonis Interface. Selleks minge järgmisesse kohta: **Services > ISC DHCPv4 > Leases**.



![Image](assets/fr/045.webp)



### F. NAT ja tulemüüri reeglite konfigureerimine



Hea uudis on see, et nüüd saame juurdepääsu OPNsense'i administratsioonile Interface LANist.



```
https://192.168.1.10
```



Pärast OPNsense'i sisse logimist avastame NAT-konfiguratsiooni. Mine sellesse asukohta: **Firewall > NAT > Outbound**. Siin saate valida väljaminevate NAT-reeglite automaatse (vaikimisi) ja käsitsi loomise vahel.



Valige automaatne režiim valiku "**Automaatne väljaminevate NAT-reeglite genereerimine**" kaudu ja klõpsake "**Salvesta**" (põhimõtteliselt on see konfiguratsioon juba aktiivne). Automaatrežiimis loob OPNsense ise iga teie võrgu jaoks NAT-reegli.



![Image](assets/fr/043.webp)



Praegu saavad kõik virtuaalsesse LANi "**192.168.10.0/24**" ühendatud arvutid piiranguteta internetti pääseda. Meie eesmärk on aga piirata juurdepääsu WAN-i HTTP ja HTTPS protokollidele, samuti DNS-ile tulemüüri Interface LAN-is.



Seega peame looma tulemüürireeglid... Sirvige menüüd järgmiselt: **Firewall > Rules > LAN**.



**Vaikimisi on olemas kaks reeglit kogu väljamineva LAN-liikluse lubamiseks, IPv4 ja IPv6**. Deaktiveerige need kaks reeglit, klõpsates Green noolt, mis asub kaugel vasakul, iga rea alguses.



Seejärel looge kolm uut reeglit, et lubada **LAN võrgu** (st "**LAN net**"):





- juurdepääs kõikidele sihtkohtadele, kasutades **HTTP**.
- juurdepääs kõikidele sihtkohtadele **HTTPS**.
- taotleda **OPNsense** oma **Interface LAN** (st "**LAN Address**") kaudu **DNS-protokolli** (see tähendab, et peate kasutama tulemüüri DNS-ina), vastasel juhul volitage oma DNS-resolver oma IP Address kaudu.



See annab järgmise tulemuse:



![Image](assets/fr/044.webp)



Kõik, mis jääb, on klõpsata "**Muudatuste rakendamine**", et uued tulemüürireeglid tootmisesse üle viia. **Pöörake tähelepanu sellele, et vaikimisi blokeeritakse kõik voolud, mis ei ole selgesõnaliselt lubatud



LANi masin saab kasutada Internetti, kasutades HTTP- ja HTTPS-ühendust. Kõik muud protokollid on blokeeritud.



![Image](assets/fr/018.webp)



## IV. Kokkuvõte



Kui järgite seda juhendit, saate OPNsense'i paigaldada ja kohe tööle hakata. OPNsense pakub mitmesuguseid funktsioone võrguliikluse tõhusaks turvamiseks ja haldamiseks ning sobib kasutamiseks professionaalsetes keskkondades.



See paigaldus on alles algus: uurige vabalt menüüd ja konfigureerige muid funktsioone, et kohandada OPNsense teie vajadustele.