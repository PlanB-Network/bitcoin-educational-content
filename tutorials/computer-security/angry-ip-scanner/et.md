---
name: Angry IP Scanner
description: Lihtne viis oma võrgu skaneerimiseks
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian BURNELi originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___



## I. Esitlus



Kuidas skaneerida Windowsi võrku ühendatud masinate jaoks kiiresti ja lihtsalt? Vastus on Angry IP Scanner. See avatud lähtekoodiga projekt võimaldab teil hõlpsasti skaneerida võrku, kasutades lihtsasti kasutatavat graafilist Interface.



Seda tööriista saavad kasutada üksikisikud oma kohaliku võrgu **skaneerimiseks**, aga ka IT-spetsialistid samal eesmärgil. Tõestuseks, et **see tööriist on väga praktiline**, on seda juba kasutanud **mitmed küberkurjategijate grupid** ettevõtte võrkude skaneerimiseks (samamoodi nagu Nmap). Heaks näiteks on [lunavararühm RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Tegemist on endiselt korraliku tarkvaraga, kuid nagu muude võrgu- ja turvalisusele suunatud tööriistade puhul, võib selle kasutamist kuritarvitada.



Siinkohal kasutame seda **Windows 11** peal, kuid seda on täiesti võimalik kasutada ka teistes **Windows'i** versioonides, samuti **Linux'is** ja **macOS'is**.



**Angry IP** Scanner on vähem põhjalik kui Nmap, kuid on siiski huvitav kiireks, põhiliseks võrguanalüüsiks, aga ka seetõttu, et see on kõigile kättesaadav. See **tuvastab võrguga ühendatud hosts** ning tuvastab **host-nimed** ja **avatud pordid**.



Kui soovite minna kaugemale, vaadake Nmapi õpetust:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Alustamine Angry IP Scanneriga



### A. Laadige alla ja installige Angry IP Scanner



Angry IP Scanner'i uusimat versiooni saate alla laadida rakenduse ametlikul veebisaidil või GitHubist. Me kasutame viimast võimalust. Klõpsake alloleval lingil ja laadige alla EXE-versioon: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Käivitage käivitatav fail, et jätkata installimist. Paigaldamise ajal ei ole midagi erilist teha.



![Image](assets/fr/013.webp)



### B. Käivitage esialgne võrgu skaneerimine



Esimesel käivitamisel võtke aega, et lugeda juhiseid aknas "**Alustamine**", et saada rohkem teavet tööriista tööpõhimõtete kohta. Muide, seal on mitu terminit, millega tuleb arvestada:





- **Feeder**: moodul, mis vastutab skaneeritavate IP-aadresside nimekirjade koostamise eest juhuslikust IP-piirkonnast või IP-aadresside nimekirja sisaldavast failist.
- **Fetcher**: moodulite kogum, mille abil saab teavet võrgus olevate hostide kohta. Näiteks on olemas fetcherid MAC-aadresside tuvastamiseks, portide skaneerimiseks, hostinimede tuvastamiseks või HTTP-päringute saatmiseks.



![Image](assets/fr/018.webp)



IP-alavõrgu skaneerimiseks sisestage lihtsalt **alguse IP Address** ja **lõpu IP Address** väljale "**IP-piirkond**" (vastasel juhul muutke tüüpi paremal). Seejärel klõpsake nuppu "**Start**".



![Image](assets/fr/019.webp)



Mõnikümmend sekundit hiljem on tulemus nähtav tarkvara Interface-s. **Ja iga analüüsitud vahemiku IP Address puhul näete, kas Angry IP Scanner on tuvastanud hosti või mitte.** Ekraanile ilmub ka kokkuvõte, mis näitab aktiivsete hostide arvu (antud juhul 6) ja avatud porti omavate hostide arvu.



![Image](assets/fr/020.webp)



Siin näeme host nimega "**OPNsense.local.domain**", mis on seotud IP Address "**192.168.10.1**" ja millele pääseb ligi **ports 80** ja **443** (HTTP ja HTTPS). Parempoolne hiireklõps hostil annab juurdepääsu lisakäskudele, nagu pinging, trace route ja brauseri avamine selle IP Address kaudu.



![Image](assets/fr/012.webp)



### C. Lisage skaneerimispordid



Vaikimisi skaneerib **Angry IP Scanner** 3 porti: **80** (HTTP), **443** (HTTPS) ja **8080**. Saate rakenduse eelistustest lisada rohkem skaneeritavaid porte. Klõpsake menüüs "**Tööriistad**" ja seejärel vahekaardil "**Portid**".



Siin saate muuta portide nimekirja valiku "**Portide valik**" abil. Saate **märgistada konkreetseid, komaga eraldatud pordinumbreid või portide vahemikke**. Allpool esitatud näites on lisatud kaks porti: **445** (SMB) ja **389** (LDAP). Kui soovite skaneerida pordid vahemikus 1-1000, sisestage "**1-1000**". Ei ole määratud, kas portide skaneerimine toimub TCP, UDP või mõlemas.



![Image](assets/fr/021.webp)



Kui käivitate skannimise uuesti, saate tõenäoliselt uut teavet. Allpool toodud näites ütleb Angry IP Scanner, et tänu skaneeritavate portide uuele konfiguratsioonile on hostidel "**SRV-ADDS-01**" ja "**SRV-ADDS-02**" avatud pordid 389 ja 445.



![Image](assets/fr/022.webp)



**Märkus**: menüüst "**Skanner**" saate skaneerimistulemusi eksportida tekstifaili.



Kui soovite skaneerimist edasi viia, klõpsake menüüs "**Tööriistad**" ja seejärel "**Fetchers**". See lisab skaneerimisele "võimeid". Lihtsalt valige noppija ja viige see aktiveerimiseks vasakule. See lisab skannimise tulemusele täiendava veeru.



![Image](assets/fr/014.webp)



Allpool on näidatud funktsioonid "**NetBIOS info**" ja "**Web tuvastamine**". Esimene funktsioon annab lisateavet, näiteks masina MAC Address ja domeeninime, teine funktsioon aga kuvab veebilehe pealkirja (mis võib anda märku veebiserveri või rakenduse tüübist).



![Image](assets/fr/011.webp)



Lõpuks saate eelistustest muuta ka meetodit, mida kasutatakse "**ping**" puhul, s.t. arvestada, kas host on aktiivne või mitte. Kuna mõned hostid ei reageeri pingutustele, võimaldab see teil proovida teisi meetodeid (UDP-pakett, TCP-portprobe, ARP, UDP + TCP kombinatsioon jne).



## III. Kokkuvõte



Lihtne ja tõhus: Angry IP Scanner tuvastab võrku ühendatud hostid ja võimaldab teil konfigureerida portide skaneerimist. Valikute poolest ei ole see nii paindlik kui Nmap ja ei lähe nii kaugele, kuid kiireks skaneerimiseks on see hea algus.



Kui soovite kasutada **Nmapi** koos graafilise Interface-ga, saate kasutada **rakendust Zenmap** (vt ülevaade allpool).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d