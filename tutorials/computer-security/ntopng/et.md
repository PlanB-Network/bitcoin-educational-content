---
name: Ntopng
description: Jälgige oma võrku ntopngiga
---
![cover](assets/cover.webp)



___



*See õpetus põhineb Florian Duchemini originaalsel sisul, mis on avaldatud [IT-Connect](https://www.it-connect.fr/). Litsents [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Originaaltekstis võib olla tehtud muudatusi.*



___



## I. Esitlus



**Võrgu voolavuse kontrollimine, selge pildi saamine kasutusest või jõudlusstatistika, on võrguvoogude jälgimine oluline osa ettevõtte võrgust**. See aitab ennetada infrastruktuuri muutusi ja tagada kasutajatele kasutuskvaliteedi (mida nimetatakse ka QoE (Quality of Experience), erinevalt QoS-st).



Selleks on olemas palju tehnikat ja tarkvara/protokolle. Näiteks Cisco poolt välja töötatud Netflow't saab kasutada IP-voogude statistika saamiseks Interface-st, kuid selle kasutamine on piiratud ühilduvate seadmetega.



Seepärast tutvustan selles õpetuses **Ntop** ja näitan teile, kuidas seda oma infrastruktuuris kasutada, et hoida silma peal võrgu kasutamisel.



Ntop on avatud lähtekoodiga tarkvara, mida saab paigaldada mis tahes Linuxi masinale. See on tasuta ja suudab koguda järgmisi andmeid:





- Ribalaiuse kasutamine
- Peamised kliendid
- Peamised sihtkohad
- Kasutatud protokollid
- Kasutatud rakendused
- Kasutatud sadamad
- Jne.



Nüüdseks ümber nimetatud **Ntopng (New Generation)**, pakub see mitmeid põhifunktsioone tasuta. Saadaval on ka kommertsversioon, mis võimaldab konfigureeritud hoiatusteadete eksportimist SIEM-tüüpi tarkvarasse või liikluse filtreerimist otse sondist määratud reeglitega.



## II. Eeltingimused



Ntop-sondi paigaldamine erineb sõltuvalt seadmestikust ja keskkonnast. Seega ei kavatse ma siinkohal anda teile samm-sammult juhendit, vaid kirjeldan erinevaid võimalusi.



### A. Rongisisese režiimi kasutamine



Kui teil on tootmises pfSense, OPNSense või Endian tulemüür või isegi Linuxi tööjaam NFTablesiga, siis on hea uudis! Saate Ntopng otse paigaldada ja alustada oma liideste jälgimist.



Selle tehnika eelis on see, et see ei nõua lisaseadmeid. Teisest küljest suurendab see ressursikasutust, seega veenduge, et teil on piisav riistvara või piisava suurusega VM (vähemalt 2 tuuma ja 2BG RAM).



### B. TAP / SPAN režiim



**Tap** on **võrguseade, mis dubleerib seda läbivat liiklust ja saadab selle teisele seadmele.** Selle seadme eeliseks on see, et see ei nõua olemasoleva infrastruktuuri muutmist ja seda saab paigutada ükskõik kuhu, et jälgida konkreetseid võrgulõike, või tuumiklülituri ja servaruuteri vahele, et analüüsida internetti suunduvat/lähtuvat liiklust.



Seda tüüpi seadmete suur puudus on nende hind. Tänapäeva Gigabit-võrkudes ei saa passiivne pealtkuulaja võrguliiklust korralikult kinni püüda, seega on vaja aktiivset seadet, mis maksab umbes 200 eurot (minimaalselt).



**SPAN**-režiimi, mida tuntakse ka kui **porti peegeldamist**, kasutab lüliti liikluse edastamiseks ühest pordist teise. See on kaugelt eelistatud meetod, kuna seda on lihtne seadistada ja see võimaldab, nagu ka tap, jälgida soovi korral osa võrgust või kogu võrku. Siiski on kaks puudust: lüliti peab selle funktsiooni integreerima ja selle kasutamine võib suurendada lüliti protsessorikoormust.



### C. Marsruuteri režiim



On täiesti võimalik paigaldada ruuter Linuxi alla ja installeerida sellele ntopng. Selle meetodi ainus puudus on see, et see muudab teie võrku, kas selle sisemist adresseerimist või teie "päris" ruuteri ja lisatava ruuteri vahelist adresseerimist.



Märkus: artikli [Loo Wifi ruuter koos Raspberry Pi ja RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) lugejatele on täiesti võimalik paigaldada ntopng oma Rpi, et saada täpset statistikat!



### D. Sidemoodus



Huvitav alternatiiv on kasutada **Linuxi masinat sillarežiimis.** See võimaldab kahe seadme vahele paigutatuna kogu liiklust salvestada, ilma et peaks sekkuma infrastruktuuri või selle seadmete konfiguratsiooni. Kuna vana masin võib seda tööd teha, võib selle meetodi hind olla ka atraktiivne. Pange tähele, et optimaalseks kasutamiseks peaks seadmel olema kolm võrgukaarti, kaks sillarežiimis, üks Interface ja SSH juurdepääsu jaoks. Võimalik on kasutada ka ainult kahte kaarti, kuid siis jääb ka seadme haldusliiklus kinni...



Seega kasutan ma **teda viimast režiimi**. Praktilistel põhjustel kasutan demonstratsiooniks virtuaalmasinaid, kuid meetod jääb samaks ka füüsilistel masinatel kasutamiseks.



## III. Proovide ettevalmistamine Interface silla abil



Sondi jaoks valisin **Debian 11** masina minimaalses paigalduses.



Esimene samm, alati sama, uuendada:



```
apt-get update && apt-get upgrade
```



Seejärel paigaldage **bridge-utils** pakett, mis võimaldab meil luua meie silda:



```
apt-get install bridge-utils
```



Pärast paigaldamist tuleb kõigepealt märkida meie võrgukaartide praegune nimi. Debianis võib see nimi olla mitmel kujul ja me vajame seda konfiguratsiooniks.



Lihtne käsk **ip add** annab selle teabe tagasi:



![Image](assets/fr/016.webp)



Siin näen 3 liideseid:





- Lo**: see on tagasiside Interface; see on virtuaalne Interface, mis "loopib" üle seadmete. Põhimõtteliselt kasutatakse seda Interface, mille Address on 127.0.0.1 (kuigi iga Address 127.0.0.0/8 sobib, kuna see vahemik on selleks otstarbeks reserveeritud), seadmetega enda kontakteerimiseks. Kui te olete oma tööjaama paigaldanud veebilehe (kasutades näiteks WAMPPi), siis olete tõenäoliselt kasutanud "*localhost*" Address ühel või teisel korral, et kuvada oma masinas asuvat saiti. See hostinimi on seotud Address 127.0.0.1 ja seega ka Interface loopbackiga.
- ens33**: see on minu esimene Interface, mis sai Address siin minu DHCP-st
- ens36**: minu teine Interface



Nüüd, kui mul on kogu teave olemas, võin muuta */etc/network/interfaces* faili, et luua oma sild. Praegu näeb see välja järgmiselt (võib erineda):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



Esimene osa puudutab minu loopback Interface, mida ma ei puutu, millele järgneb Interface ens33. Muudatused hõlmavad minu teise Interface (ens36) lisamist ja silla konfigureerimist nende kahe liidese abil:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Siin on mõned selgitused nende esimeste muudatuste kohta:





- auto *Interface***: "käivitab" Interface automaatselt süsteemi käivitamisel
- iface *Interface* inet manual**: Interface kasutamiseks ilma IP Address-ta. Nagu märksõna "static", et määrata staatiline IP Address või "dhcp", et kasutada dünaamilist adresseerimist



Muudatused jätkuvad:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Siinkohal taas mõned selgitused:





- iface br0 inet static**: siin olen määratlenud oma Interface silla (*br0*) koos staatilise Address-ga.
- Address, netmask, gateway**: teave tahvli adresseerimise kohta
- bridge_ports**: liidesed, mis lisatakse sillale
- bridge_stp**: Spanning Tree protokolli kasutatakse lülitite ühendamisel, et tuvastada üleliigseid linke ja vältida silmuseid. Kuna sild võib olla sisestatud kahe võrgutee vahele, võib see olla silmuse allikaks, mistõttu on võimalik selle protokolli lubamine. Mul ei ole seda siin vaja, seega lülitan selle välja.



Salvestage muudatused ja käivitage võrk uuesti:



```
systemctl restart networking
```



Muudatuste kontrollimiseks kuvage uuesti käsu **ip** add tulemus:



![Image](assets/fr/021.webp)


Te näete selgelt **mulle uut Interface "*br0*" koos IP Address-ga, mille ma olen sellele määranud.** Muide, te näete ka, et minu kaks füüsilist liidest on tõepoolest "UP", kuid neil ei ole IP Address.



## IV. NtopNG paigaldamine



Nüüd, kui meie sond on võimeline nuhkima liiklust minu võrgu ja ruuteri vahel, on jäänud vaid ntopng'i paigaldamine. Selleks tuleb kõigepealt muuta faili */etc/apt/sources.list* ja lisada **contrib** iga rea lõppu, mis algab **deb** või **deb-src**.



Vaikimisi sisaldavad pakettide allikad ainult DFSG (*Debian Free Sotftware Guidelines*) nõuetele vastavaid pakette, mis on tähistatud märksõnaga **main**. Neid allikaid saab ka lisada:





- contrib**: paketid, mis sisaldavad DFSG-le vastavat tarkvara, kuid kasutavad sõltuvusi, mis ei ole osa **main** harust
- non-free**: sisaldab pakette, mis ei ole DFSG-konformsed



Näide reast failis /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Nii et ma lihtsalt lisan sellistele ridadele sõna **contrib**.



Ülejäänud sammud on loetletud [NtopNG] saidil (https://packages.ntop.org/apt/), kus Debian 11 puhul peate lisama Ntopi allikad edaspidiseks paigaldamiseks. See lisamine on automatiseeritud, kasutades:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Seejärel tuleb tegelik paigaldusetapp:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Esimene käsk kustutab apt paketihalduri vahemälu. Teine uuendab paketiloendit ja kolmas installib NtopNG.



Pärast installimist on **NtopNG tarkvara otse kättesaadav Debian-masina porti 3000**. Nii et minu jaoks on see `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



NtopNG koduleht



Vaikimisi kasutajanimi ja parool kuvatakse, nii et teil tuleb need vaid sisestada!



## V. NtopNG kasutamine



Esmakordsel sisselogimisel palutakse teil kõigepealt muuta vaikimisi administraatori parooli ja keelt. Kahjuks ei ole prantsuse keel üks neist.



Seejärel jõuate armatuurlauale:



![Image](assets/fr/023.webp)



NtopNG armatuurlaud



Ära harjuta seda! Kui märkate ekraani ülaosas olevat kollast kasti, siis näete seda lauset: "*Litsents aegub 04:57*". Vaikimisi käivitab installimine NtopNG täisversiooni prooviversiooni, kuid (väga) piiratud ajaks. Kui see "tagasiarvestus" on lõppenud, aktiveeritakse *community*-versioon ja armatuurlaud muutub:



![Image](assets/fr/024.webp)



Uus NtopNG kogukonna armatuurlaud



Kõigepealt tuleb **kontrollida, et õige Interface kuulab**. Vasakpoolses ülemises nurgas olevast rippmenüüst saate valida Interface, mis meid siinkohal huvitab: br0



![Image](assets/fr/025.webp)



Interface valik



Uues aknas kuvatakse "Top Flaw Talkers", st seadmed, mis suhtlevad kõige rohkem. Siin on mul ainult kaks jaama, mis kuvatakse:



![Image](assets/fr/026.webp)



**Lähtehaldurid kuvatakse vasakul, sihtkohad paremal ** See võimaldab teil visualiseerida kogu ribalaiuse kasutamist iga halduri poolt ja saada üldine ülevaade võrguliikluse kohta. See ei ole halb, kuid me võime minna kaugemale...



Kui ma klõpsan näiteks "*Hosts*", saan ma graafiku, mis näitab iga minu võrgus asuva host'i saatvat ja vastuvõtvat energiatarbimist. Siin näen näiteks, et ainuüksi 192.168.1.37 moodustab 80% minu liiklusest:



![Image](assets/fr/027.webp)



Kui ma klõpsan kõnealuse vastuvõtja IP Address-l, suunatakse mind kokkuvõtte lehele:



![Image](assets/fr/028.webp)



Ma näen näiteks, et tegemist on VMWare'i masinaga (minu MAC Address-i JA-tuvastuse järgi), et selle nimi on DESKTOP-GHEBGV1 (seega kindlasti Windows host) JA mul on **statistika vastuvõetud ja saadetud pakettide kohta, samuti andmehulk**.



Samuti märkate selle kokkuvõtte ülaosas uut menüüd. Soovitan teil klõpsata "**rakendused**", et näha, mis põhjustab nii palju liiklust:



![Image](assets/fr/017.webp)


Ha, tundub, et meil on vastus! Vasakpoolsel graafikul **näeme, et 76,6% selle liikluse osakaalust on pärit ... Windows Update**, nii et see vastuvõtja laeb uuendusi alla!



NtopNG kasutab tehnoloogiat nimega DPI (*Deep Packet Inspection*), mis võimaldab liigitada iga võrguvoo ja määratleda selle taga oleva rakenduse (või rakenduste perekonna).



Demonstreerimiseks käivitan ma oma hostil YouTube'i video:



![Image](assets/fr/018.webp)



**Liiklus oli koheselt äratuntav ja kategoriseeritud!



Märkus: ilmselgetel põhjustel võib selline tarkvara tekitada privaatsusküsimusi, seega olge ettevaatlik, et kasutada seda õigetes tingimustes. Pange tähele ka seda, et tulemusi on võimalik **anonüümseks muuta**, selle valiku leiate jaotisest **Settings > Preferences > Misc** ja selle nimi on "**Mask Host IP Address**".



## VI. Avastused ja hoiatused



NtopNG on samuti võimeline väljastama turvahoiatusi teatavate söötude kohta. Need leiate vasakpoolse bänneri menüüst **Hoiatused**. Siin näiteks on mul kokku 2851 hoiatust, mis on jaotatud eri raskusastmete järgi: Teade, hoiatus ja viga.



![Image](assets/fr/019.webp)



Vaatame kõrge kriitilisusega hoiatusi, mul on neid 17!



Sellel joonisel klõpsates kuvatakse hoiatuste üksikasjad. Siin ei ole midagi murettekitavat, tegemist on valepositiivsusega, uuenduste allalaadimine on liigitatud binaarfaili ülekandmiseks HTTP-vooga, mis võib tõepoolest tähendada rünnakut.



![Image](assets/fr/020.webp)



Kuna ma kasutan tasuta versiooni, ei saa ma siiski välistada domeene või hoste, mis on hoiatuste allikaks, nii et sa pead neil silma peal hoidma, et mitte jääda ilma millestki palju murettekitavamast. NtopNG generate hoiatusi juhul, kui:





- Binaarfaili allalaadimine üle HTTP
- Kahtlane DNS-liiklus
- Mittestandardse pordi kasutamine
- SQL-süstimise tuvastamine
- Cross-Site Scripting (XSS)
- Jne.



## VII. Kokkuvõte



Selles õpetuses nägime, **kuidas luua NtopNG-ga sondi**, mis võimaldab meil **analüüsida meie võrguliiklust**, et visualiseerida protokollide kasutamist ja iga vastuvõtja hõivatust, kuid ka tuvastada kahtlast liiklust.



Kahjuks ei saa ma selles artiklis kõiki funktsioone ja võimalusi katta, kuid uurige julgelt!



Seda lahendust saab rakendada ettevõtte infrastruktuuris püsivalt. NtopNG saab tulemusi eksportida ka InfluxDB andmebaasi, mis võimaldab teil luua oma armatuurlauad kolmanda osapoole tööriistaga, näiteks Graphana.