---
name: Ntopng
description: Overvåk nettverket ditt med ntopng
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Florian Duchemin publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det kan ha blitt gjort endringer i den opprinnelige teksten



___



## I. Presentasjon



**Enten det er for å sjekke nettverkets flyt, få et klart bilde av bruken eller for ytelsesstatistikk, er overvåking av nettverksflyt en viktig del av et bedriftsnettverk**. Den bidrar til å forutse endringer i infrastrukturen og til å sikre brukernes brukskvalitet (også kjent som QoE for *Quality of Experience*, i motsetning til QoS).



Det finnes mange teknikker og programvare/protokoller for å gjøre dette. Netflow, for eksempel, som er utviklet av Cisco, kan brukes til å hente ut IP-strømningsstatistikk fra en Interface, men bruken er begrenset til kompatibelt utstyr.



I denne veiledningen skal jeg derfor introdusere **Ntop** og vise deg hvordan du kan bruke det i infrastrukturen din for å holde et øye med nettverksbruken.



Ntop er en programvare med åpen kildekode som kan installeres på alle Linux-maskiner. Den er gratis og kan samle inn følgende data:





- Utnyttelse av båndbredde
- Viktigste kunder
- De viktigste destinasjonene
- Protokoller som brukes
- Brukte applikasjoner
- Porter som brukes
- Og så videre.



Den har nå skiftet navn til **Ntopng (New Generation)**, og tilbyr mange grunnleggende funksjoner gratis. Det finnes også en kommersiell versjon som gjør det mulig å eksportere konfigurerte varsler til programvare av SIEM-typen, eller filtrere trafikk med regler som defineres direkte fra proben.



## II. Forutsetninger



Installasjonen av en Ntop-sonde varierer avhengig av utstyr og miljø. Jeg kommer derfor ikke til å gi deg en trinnvis veiledning her, men vil skissere de ulike mulighetene.



### A. Innebygd modus



Hvis du har en pfSense-, OPNSense- eller Endian-brannmur i produksjon, eller til og med en Linux-arbeidsstasjon med NFTables, er det gode nyheter! Du kan installere Ntopng direkte og begynne å overvåke grensesnittene dine.



Fordelen med denne teknikken er at den ikke krever ekstra maskinvare. På den annen side øker det ressursutnyttelsen, så sørg for at du har tilstrekkelig maskinvare eller en VM av tilstrekkelig størrelse (minst 2 kjerner og 2 GB RAM).



### B. TAP / SPAN-modus



En **tap** er **en nettverksenhet som dupliserer trafikken som passerer gjennom den, og sender den til en annen enhet.** Fordelen med denne enheten er at den ikke krever noen endringer i den eksisterende infrastrukturen, og at den kan plasseres hvor som helst for å overvåke spesifikke nettverksdeler, eller mellom kjernesvitsjen og edge-ruteren for å analysere trafikk til/fra Internett.



Den store ulempen med denne typen utstyr er kostnadene. I dagens Gigabit-nettverk kan ikke en passiv avlyttingskran fange opp nettverkstrafikken på riktig måte, så du trenger en aktiv enhet som koster rundt 200 euro (minimum).



**SPAN**-modus, også kjent som **portspeiling**, brukes av en svitsj til å videresende trafikk fra én port til en annen. Dette er min klart foretrukne metode, siden den er enkel å sette opp og, i likhet med tap, lar deg overvåke en del av nettverket eller hele nettverket når du vil. Det er imidlertid to ulemper: Svitsjen må integrere denne funksjonen, og bruken av den kan øke prosessorbelastningen på svitsjen.



### C. Rutermodus



Det er fullt mulig å montere en ruter under Linux og installere ntopng på den. Den eneste ulempen med denne metoden er at den vil endre nettverket ditt, enten den interne adresseringen eller adresseringen mellom den "ekte" ruteren din og den du legger til.



Merk: for lesere av artikkelen [Lag en Wifi-ruter med Raspberry Pi og RaspAP] (https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) er det fullt mulig å installere ntopng på din Rpi for å få nøyaktig statistikk!



### D. Bro-modus



Et interessant alternativ er å bruke **en Linux-maskin i bromodus**, som plasseres mellom to stykker utstyr og gjør det mulig å fange opp all trafikk uten å måtte gripe inn i konfigurasjonen av infrastrukturen eller utstyret. Ettersom en gammel maskin kan gjøre jobben, kan denne metoden også være rimelig. Merk at for å være optimal bør enheten ha tre nettverkskort, to i bromodus, ett for tilgang til Interface og SSH. Det er mulig å bruke bare to kort, men da vil også enhetens administrasjonstrafikk bli fanget opp...



Så det er **denne siste modusen jeg kommer til å bruke**. Av praktiske årsaker vil jeg bruke virtuelle maskiner til demonstrasjonen, men metoden er den samme for bruk på fysiske maskiner.



## III. Klargjøring av sonde med Interface-bro



For proben valgte jeg en **Debian 11**-maskin med minimal installasjon.



Første trinn, alltid det samme, oppdater:



```
apt-get update && apt-get upgrade
```



Deretter installerer du pakken **bridge-utils**, som gjør det mulig for oss å opprette broen vår:



```
apt-get install bridge-utils
```



Når du har installert den, er det første du må merke deg det nåværende navnet på nettverkskortene våre. Under Debian kan dette navnet ha flere former, og vi trenger det for konfigurasjonen.



En enkel **ip add**-kommando vil returnere en utdata med denne informasjonen:



![Image](assets/fr/016.webp)



Her ser jeg tre grensesnitt:





- Lo**: Dette er loopback Interface; det er en virtuell Interface som "looper" over utstyret. I utgangspunktet brukes denne Interface-en, hvis Address er 127.0.0.1 (selv om en hvilken som helst Address i 127.0.0.0/8 duger, ettersom dette området er reservert for dette formålet), til å kontakte selve utstyret. Hvis du har installert et nettsted på arbeidsstasjonen din (for eksempel ved hjelp av WAMPP), har du sannsynligvis brukt "*localhost*" Address en eller annen gang for å vise nettstedet som ligger på din egen maskin. Dette vertsnavnet er knyttet til Address 127.0.0.1 og dermed til Interface-loopbacken.
- ens33**: dette er min første Interface, som mottok en Address her fra DHCP-en min
- ens36**: min andre Interface



Nå som jeg har all informasjonen, kan jeg endre filen */etc/network/interfaces* for å opprette broen min. Slik ser den ut for øyeblikket (kan variere):



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



Den første delen gjelder min loopback Interface, som jeg ikke vil røre, etterfulgt av Interface ens33. Modifikasjonene innebærer å legge til min andre Interface (ens36) og konfigurere broen med disse to grensesnittene:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Her er noen forklaringer på disse første endringene:





- auto *Interface***: vil automatisk "starte" Interface ved oppstart av systemet
- iface *Interface* inet manual**: for å bruke Interface uten noen IP Address. Som nøkkelordet "static" for å definere en statisk IP Address eller "dhcp" for å bruke dynamisk adressering



Modifikasjonene fortsetter:



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



Her igjen, noen forklaringer:





- iface br0 inet static**: her har jeg definert min Interface-bro (*br0*) med en statisk Address.
- Address, nettmaske, gateway**: informasjon om kortadressering
- bridge_ports**: grensesnitt som skal inkluderes i broen
- bridge_stp**: Spanning Tree-protokollen brukes ved sammenkobling av svitsjer for å oppdage redundante koblinger og unngå looper. Siden en bro kan settes inn mellom to nettverksbaner, kan den være kilden til en sløyfe, og derfor er det mulig å aktivere denne protokollen. Jeg trenger den ikke her, så jeg deaktiverer den.



Lagre endringene, og start nettverket på nytt:



```
systemctl restart networking
```



For å kontrollere endringene viser du resultatet av kommandoen **ip** add på nytt:



![Image](assets/fr/021.webp)


Du kan tydelig se **den nye Interface "*br0*" med IP Address som jeg har tilordnet den ** Du kan forresten også se at de to fysiske grensesnittene mine faktisk er "UP", men ikke har noen IP Address.



## IV. Installere NtopNG



Nå som proben vår er i stand til å sniffe trafikk mellom nettverket mitt og ruteren, gjenstår det bare å installere ntopng. For å gjøre dette må du først endre filen */etc/apt/sources.list* og legge til **contrib** på slutten av hver linje som begynner med **deb** eller **deb-src**.



Som standard inneholder pakkekildene kun DFSG (*Debian Free Sotftware Guidelines*) kompatible pakker, identifisert med nøkkelordet **main**. Du kan også legge til disse kildene:





- contrib**: pakker som inneholder DFSG-kompatibel programvare, men som bruker avhengigheter som ikke er en del av **main**-grenen
- non-free**: inneholder pakker som ikke er DFSG-kompatible



Eksempel på en linje i /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Så jeg legger bare til ordet **contrib** i slike linjer.



Resten av trinnene er listet opp på [NtopNG]-nettstedet (https://packages.ntop.org/apt/), der du, for Debian 11, må legge til Ntop-kildene for fremtidig installasjon. Dette tillegget er automatisert ved å bruke en:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Deretter kommer selve installasjonsfasen:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Den første kommandoen sletter hurtigbufferen til apt-pakkebehandleren. Den andre vil oppdatere pakkelisten, og den tredje vil installere NtopNG.



Etter installasjonen er **NtopNG-programvaren direkte tilgjengelig på port 3000 på Debian-maskinen**. Så for meg er det `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



NtopNG hjemmeside



Standard innlogging og passord vises, så alt du trenger å gjøre er å skrive dem inn!



## V. Bruk av NtopNG



Når du logger inn for første gang, blir du først bedt om å endre standard administratorpassord og språk. Dessverre er ikke fransk en av dem.



Så kommer du til dashbordet:



![Image](assets/fr/023.webp)



NtopNG-dashbordet



Ikke bli vant til denne! Hvis du legger merke til den gule boksen øverst på skjermen, vil du se setningen: "*Lisensen utløper om 04:57*". Som standard starter installasjonen en prøveversjon av fullversjonen av NtopNG, men for en (svært) begrenset tid. Når denne "nedtellingen" er nådd, aktiveres *fellesskapsversjonen*, og dashbordet endres:



![Image](assets/fr/024.webp)



Nytt dashbord for NtopNG-fellesskapet



Det første du må gjøre er å **sjekke at riktig Interface lytter**. Øverst i venstre hjørne finner du en nedtrekksliste over tilgjengelige grensesnitt som lar deg velge den Interface vi er interessert i her: br0



![Image](assets/fr/025.webp)



Interface utvalg



Det nye vinduet viser "Top Flaw Talkers", dvs. de enhetene som kommuniserer mest. Her har jeg bare to stasjoner som vises:



![Image](assets/fr/026.webp)



**Kildevertene vises til venstre, destinasjonene til høyre ** På denne måten kan du visualisere hver verts bruk av total båndbredde og få en oversikt over nettverkstrafikken. Det er ikke dårlig, men vi kan gå enda lenger...



Hvis jeg for eksempel klikker på "*Hosts*", får jeg opp en graf som viser strømforbruket for sending og mottak for hver enkelt host i nettverket mitt. Her kan jeg for eksempel se at 192.168.1.37 alene står for 80 % av trafikken min:



![Image](assets/fr/027.webp)



Hvis jeg klikker på IP Address for den aktuelle verten, blir jeg omdirigert til en sammendragsside:



![Image](assets/fr/028.webp)



Jeg kan for eksempel se at det er en VMWare-maskin (ved å gjenkjenne JA-et til min MAC Address), at den heter DESKTOP-GHEBGV1 (så det er helt sikkert en Windows-vert) OG jeg har **statistikk over mottatte og sendte pakker, samt datamengden**.



Du vil også legge merke til en ny meny øverst i dette sammendraget. Jeg foreslår at du klikker på "**Apps**" for å se hva som driver så mye trafikk:



![Image](assets/fr/017.webp)


Ha, det ser ut til at vi har et svar! På grafen til venstre ser vi at 76,6 % av trafikken kommer fra ... Windows Update**, så denne verten laster ned oppdateringer!



NtopNG bruker en teknologi som kalles DPI for *Deep Packet Inspection*, noe som gjør det mulig å kategorisere hver nettverksflyt og definere applikasjonen (eller familien av applikasjoner) bak den.



For å demonstrere dette starter jeg en YouTube-video på verten min:



![Image](assets/fr/018.webp)



**Trafikken ble umiddelbart gjenkjent og kategorisert!



Merk: Av åpenbare grunner kan denne typen programvare føre til personvernproblemer, så vær forsiktig med å bruke den under de rette forholdene. Merk også at det er mulig å **anonymisere resultatene**, alternativet finnes i **Innstillinger > Preferanser > Diverse** og heter "**Mask Host IP Address**".



## VI. Oppdagelser og varsler



NtopNG kan også sende ut sikkerhetsvarsler om visse feeds. Disse finner du i **Alerts**-menyen i banneret til venstre. Her har jeg for eksempel totalt 2851 varsler, fordelt på ulike alvorlighetsgrader: Varsel, Advarsel og Feil.



![Image](assets/fr/019.webp)



La oss ta en titt på de høykritiske varslene, jeg har 17 av dem!



Ved å klikke på denne figuren får du opp detaljene i varslene. Det er ikke noe alarmerende her, det er en falsk positiv, nedlastingen av oppdateringer blir kategorisert som en binær filoverføring i en HTTP-strøm, noe som faktisk kan bety et angrep.



![Image](assets/fr/020.webp)



Men siden jeg bruker gratisversjonen, kan jeg ikke ekskludere domener eller verter som er kilden til varsler, så du må holde et øye med dem for å unngå å gå glipp av noe mye mer bekymringsfullt. NtopNG vil generate-varsler i tilfelle:





- Nedlasting av binærfiler via HTTP
- Mistenkelig DNS-trafikk
- Bruk av en ikke-standard port
- Deteksjon av SQL-injeksjon
- Skripting på tvers av nettsteder (XSS)
- Og så videre.



## VII. Konklusjon



I denne opplæringen har vi sett **hvordan vi setter opp en probe med NtopNG**, slik at vi kan **analysere nettverkstrafikken** for å visualisere protokollbruk og belegget på hver vert, men også oppdage mistenkelig trafikk.



Dessverre kan jeg ikke dekke alle funksjonene og mulighetene i denne artikkelen, men du er velkommen til å utforske dem!



Denne løsningen kan implementeres på permanent basis i en bedriftsinfrastruktur. NtopNG kan også eksportere resultater til en InfluxDB-database, slik at du kan lage dine egne dashbord med et tredjepartsverktøy som Graphana.