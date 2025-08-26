---
name: IP-netwerken van theorie naar praktijk
goal: Beheers de basisprincipes van IP-netwerken om ze beter te kunnen configureren en problemen op te lossen.
objectives: 


  - De architectuur en werking van het TCP/IP-protocol begrijpen
  - De verschillen, voordelen en beperkingen van IPv4 en IPv6 uitleggen
  - Verschillende types IP Address identificeren en onderscheiden
  - IP-adressering configureren en verifiëren op Unix/Linux-systemen
  - De belangrijkste diagnostische tools gebruiken om netwerkproblemen te analyseren en op te lossen


---

# Essentiële vaardigheden voor het navigeren door de IP-wereld


Duik in het hart van de IP-wereld en rust jezelf uit met de kennis om je netwerken te begrijpen en efficiënt te beheren. In deze cursus leer je alles wat je moet weten over computernetwerken op een duidelijke en praktische manier.


Je leert hoe netwerken en IP-adressering werken, hoe je onderscheid maakt tussen IPv4 en IPv6, hoe je de verschillende Address categorieën herkent en gebruikt, en hoe je het belang van het TCP/IP protocol en de verbanden die het legt tussen IP-adressen, fysieke adressen en DNS-namen begrijpt.


NET 302 is vooral gericht op studenten, Linux-gebruikers of gewoon nieuwsgierigen die de basisprincipes van netwerken willen begrijpen en hun autonomie willen versterken in het beheren, oplossen van problemen en optimaliseren van infrastructuren.


Sluit je bij ons aan en zet je kennis om in echte operationele expertise!


___


Deze cursus NET 302 is een aanpassing van de cursus *Netwerkbasis: TCP/IP, IPv4 en IPv6*, geschreven in het Frans door Philippe Pierre en gepubliceerd op [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), onder de Creative Commons Attribution-NonCommercial 4.0 International licentie ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).



Er zijn aanzienlijke wijzigingen aangebracht in de oorspronkelijke versie van Loïc Morel: de tekst is volledig herschreven, uitgebreid en verrijkt om bijgewerkte, diepgaande inhoud te bieden, terwijl de educatieve geest van het oorspronkelijke werk van Philippe Pierre behouden blijft. Ook de diagrammen zijn herzien.


+++


# Inleiding


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Cursusoverzicht


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Deze cursus biedt een complete inleiding tot de grondbeginselen van IP-netwerken. De cursus is onderverdeeld in vier hoofdstukken, die elk een essentieel aspect behandelen voor het begrijpen, configureren en diagnosticeren van problemen in een computernetwerk.


### TCP/IP-protocol


In dit eerste deel leggen we de basis door het concept van netwerken en de geschiedenis van het TCP/IP protocol te verkennen. We bestuderen de belangrijkste componenten: IP, TCP, samen met een korte blik op het IPv5 QoS protocol. We behandelen ook service primitieven om de logica van data Exchange beter te begrijpen.


### IPv4-adressering


Daarna gaan we verder met een module over IPv4-adressering. Je leert hoe IPv4 in de praktijk wordt gebruikt, de verschillende Address typen (private, public, broadcast, etc.), de fundamentele rol van DNS en hoe Ethernet adressen en het ARP protocol werken. Je ontdekt ook NAT (Network Address Translation) en de basis van netwerkconfiguratie.


### IPv6-adressering


Het derde deel richt zich op IPv6-adressering, die nodig is om Address de beperkingen van IPv4 te laten overwinnen. We bespreken de standaarden en definities, Address Assignment binnen een lokaal netwerk, Address blokbeheer en de relatie tussen IPv6 en DNS.


### Diagnostische netwerkprogramma's


We sluiten af met een presentatie van de belangrijkste tools voor netwerkdiagnose. Hiermee kun je storingen analyseren, controleren en oplossen. Dit deel zal worden gestructureerd per laag: Netwerktoegang, Netwerk, Transport en Bovenliggende lagen.


Aan het einde van deze cursus heb je de fundamentele kennis om een netwerkinfrastructuur efficiënt te beheren en mogelijke problemen te diagnosticeren.


Klaar om in de wereld van computernetwerken te duiken? Laten we gaan!


**OPMERKING**: De beschrijvingen zijn gebaseerd op een GNU/Linux CentOS 7 systeem. Netwerkconfiguraties zijn echter grotendeels hetzelfde als je een Debian en een CentOS systeem vergelijkt. We zullen dus geen onderscheid maken. Als er onderscheid wordt gemaakt, geven we dat aan met een specifiek logo.


**N.B.**: Als je tijdens de cursus onbekende termen tegenkomt, raadpleeg dan [de woordenlijst] (https://planb.network/resources/glossary) voor definities.



# TCP/IP-protocollen


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Wat is een netwerk?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



In deze eerste module gaan we dieper in op het TCP/IP protocol, de hoeksteen van moderne digitale communicatie. We bespreken de oorsprong, de fundamentele principes en het adresseringssysteem dat wordt gebruikt en dat essentieel is voor de informatiestroom tussen verbonden apparaten.


We zullen ook de belangrijkste componenten die dit model structureren in detail beschrijven en uitleggen hoe ze samenwerken om een operationeel, betrouwbaar en schaalbaar netwerk te vormen. Maar eerst is het essentieel om terug te keren naar het concept van een netwerk.


Etymologisch verwijst een netwerk naar een reeks punten die met elkaar verbonden zijn en zo een onderling verbonden structuur vormen. In de telecommunicatie en informatica vertaalt deze definitie zich in een groep apparaten (computers, routers, switches, toegangspunten, enz.) die gegevens kunnen uitwisselen via fysieke of draadloze media. Een netwerk maakt dus een continue of intermitterende stroom van informatie mogelijk, afhankelijk van de vereisten, de gebruikte protocollen en de aard van de gebruikte architectuur.


In de loop der tijd zijn er verschillende klassieke topologieën ontwikkeld om te voldoen aan verschillende behoeften op het gebied van kosten, prestaties, veerkracht en onderhoudsgemak. Deze omvatten:


- ringnetwerk,
- boomnetwerk,
- busnetwerk,
- sternetwerk,
- mesh-netwerk.



### Ringnetwerk


In een ringtopologie zijn apparaten met elkaar verbonden in een gesloten lus: elk station is verbonden met het volgende en het laatste is weer verbonden met het eerste. In deze opstelling werkt elk apparaat als een relais dat gegevens doorgeeft aan de volgende link. Afhankelijk van het type netwerk kan informatie in één richting of in beide richtingen circuleren.


Het voordeel van deze opstelling is de eenvoud van de bekabeling en de afwezigheid van afhankelijkheid van centrale apparatuur. De continuïteit van het hele netwerk hangt echter af van de gezondheid van elk afzonderlijk element: het uitvallen van één enkel station kan het hele communicatiesysteem onderbreken. Daarom worden er vaak redundantie- of bypassmechanismen ingebouwd.



![Image](assets/fr/001.webp)



### Boomnetwerk


Het boomnetwerk of de hiërarchische topologie is gemodelleerd naar de structuur van een stamboom. Het bestaat uit opeenvolgende niveaus: een wortelknooppunt bovenaan staat in verbinding met verschillende knooppunten op een lager niveau, die op hun beurt in verbinding kunnen staan met andere knooppunten, enzovoort.


Deze hiërarchische lay-out werkt bijzonder goed voor grote netwerken die een duidelijke verdeling van verantwoordelijkheden en gesegmenteerd beheer nodig hebben. Het maakt het netwerk echter ook kwetsbaar voor het falen van knooppunten op een hoger niveau: het verliezen van de root of een hoofdtak kan hele delen van de infrastructuur afsnijden.



![Image](assets/fr/002.webp)



### Busnetwerk


In een bustopologie delen alle apparaten hetzelfde transmissiemedium, meestal een coaxiale lijn of optische vezel. Elk apparaat is passief verbonden, wat betekent dat het het signaal niet actief wijzigt, en het kan gegevens verzenden of ontvangen via dit gedeelde kanaal.


Het belangrijkste voordeel van de bustopologie zijn de lage installatiekosten dankzij de vereenvoudigde bekabeling.  In oudere op coax gebaseerde implementaties (Ethernet 10BASE2/10BASE5) kan het loskoppelen of verliezen van een enkel station echter al het verkeer onderbreken of zelfs stoppen, omdat de elektrische continuïteit en afsluitingsimpedantie van de bus niet langer gehandhaafd blijven. Het hebben van een enkel fysiek medium is ook een kritieke zwakte: elke onderbreking of fout stopt de communicatie voor het hele netwerk.



![Image](assets/fr/003.webp)



### Sterrennetwerk


De stertopologie, ook bekend als "hub and spoke", is tegenwoordig het meest gebruikelijk, vooral in Ethernetnetwerken thuis en op kantoor. Hier maken alle apparaten verbinding met één centraal apparaat.


Deze lay-out maakt beheer en onderhoud eenvoudig: als een randapparaat uitvalt, blijft de rest van het netwerk onaangetast. Het nadeel is dat het centrale apparaat een single point of failure is: als het uitvalt, stopt de communicatie overal. De kwaliteit van de kabels en de lengte van de verbindingen moeten ook zorgvuldig overwogen worden om goede prestaties te behouden.



![Image](assets/fr/004.webp)



**Noot**: er zijn nog steeds netwerken die georganiseerd zijn in een lineaire, bus-achtige topologie, waar apparatuur achter elkaar is aangesloten. Deze oplossing is weliswaar goedkoop om te implementeren, maar heeft het grote nadeel dat een enkele onderbreking sommige hosts isoleert, waardoor het netwerk in onafhankelijke subsets wordt opgesplitst.


### Netwerk


Het mesh-netwerk is ontworpen voor maximale redundantie: elk apparaat is rechtstreeks verbonden met elk ander apparaat. Dit garandeert continuïteit van de service, zelfs als meerdere links of apparaten uitvallen, omdat het verkeer langs alternatieve paden kan worden omgeleid.


Het nadeel is dat het aantal verbindingen dat tot stand moet worden gebracht snel toeneemt met het aantal terminals. Voor `N` verbindingspunten zijn `N × (N-1) / 2` aparte verbindingen nodig, waardoor deze topologie duur en complex is om te implementeren. Daarom wordt deze topologie vooral gebruikt in kritieke netwerken die een zeer hoge beschikbaarheid vereisen, zoals bepaalde delen van het internet of gevoelige industriële systemen.



![Image](assets/fr/005.webp)



Er bestaan andere variaties, zoals grid- of hyperkubusnetwerken, die ontworpen zijn voor gespecialiseerde behoeften in gedistribueerd computergebruik of parallelle verwerking.


Op wereldschaal is het internet een massieve interconnectie van netwerken met verschillende topologieën, verenigd door een gemeenschappelijke adressering (IPv4 en IPv6) en een verzameling gestandaardiseerde protocollen gedefinieerd door de IETF (*Internet Engineering Task Force*). Deze diversiteit betekent dat het internet geen enkele topologie volgt: de structuur is flexibel, schaalbaar en onafhankelijk van het logische adresseringsschema dat het bruikbaar maakt.



## De oorsprong van TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



De oorsprong van het TCP protocol ligt bij **ARPA** (*Advanced Research Projects Agency*, in 1972 omgedoopt tot "DARPA"), dat in 1966 het **ARPANET** project lanceerde. Het eerste ARPANET-segment ging in oktober 1969 van start en verbond de universiteiten UCLA en Stanford met elkaar. Het doel was om onderzoekscentra met elkaar te verbinden via een pakketgeschakeld netwerk dat zelfs bij een gedeeltelijke uitval van de infrastructuur de communicatie in stand kon houden.


Als onderdeel van deze dynamiek financierde ARPA de Universiteit van Berkeley om de eerste TCP/IP protocollen te integreren in haar BSD Unix systeem. Dit speelde een belangrijke rol in de verspreiding en standaardisatie van het protocol, eerst in de academische wereld en later in de industrie.


**Noot**: in die tijd hadden computerwetenschappers nog geen Linux (dat pas begin jaren 90 zou verschijnen), noch Minix, het onderwijssysteem ontworpen door Andrew Tanenbaum.  De belangrijkste opties waren Unix of, soms, propriëtaire mainframes zoals OpenVMS. Dankzij de flexibiliteit en openheid van Unix, was het een instrument in het verspreiden van de eerste netwerkconcepten.


Strikt genomen is TCP/IP niet één protocol, maar een suite van protocollen gebouwd rond TCP en IP. Het werd bekend omdat het een gestandaardiseerde programmeer-Interface bood voor het uitwisselen van gegevens tussen machines op hetzelfde netwerk. Deze Interface, gebaseerd op primitieven genaamd "sockets", maakte het mogelijk om betrouwbare en flexibele verbindingen te maken en tegelijkertijd essentiële applicatieprotocollen te integreren.


ARPANET is daarom de historische basis van het huidige internet. Het internet is inderdaad een wereldwijd netwerk gebaseerd op het principe van pakketschakeling, waarbij informatie circuleert met behulp van een set gestandaardiseerde protocollen die zorgen voor compatibiliteit en interoperabiliteit tussen heterogene systemen. Deze open architectuur heeft de ontwikkeling en implementatie van talloze diensten en toepassingen mogelijk gemaakt, waaronder:


- e-mails,
- het World Wide Web (www),
- bestandsoverdracht en -deling...


Het bestuur en de evolutie van deze protocollen staan onder toezicht van de ***Internet Architecture Board*** (IAB).

Deze organisatie coördineert technische richtingen via twee hoofdstructuren:


- IRTF** (_Internet Research Task Force_), die langetermijnonderzoek uitvoert naar de evolutie en verbetering van protocollen.
- IETF** (_Internet Engineering Task Force_), die de operationele protocollen die op het internet worden gebruikt, ontwikkelt, standaardiseert en documenteert


De distributie van netwerkbronnen (IP Address reeksen, autonome systeemnummers, hoofddomeinnamen, enz.) wordt internationaal gecoördineerd door **IANA/ICANN**. Het operationele beheer berust op: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Europa, Midden-Oosten, Centraal-Azië), **ARIN**, **APNIC**, **LACNIC** en **AFRINIC**.


Alle TCP/IP-protocolspecificaties zijn vastgelegd in documenten die **RFC** (_Request For Comments_) worden genoemd en die dienen als gezaghebbende technische referenties. RFC's worden voortdurend bijgewerkt en genummerd om de voortdurende evolutie van de protocolsuite weer te geven.


De TCP/IP stack wordt vaak voorgesteld als een stapel van vier functionele lagen, vaak vergeleken met het zeven-Layer **OSI** (_Open Systems Interconnection_) model ontwikkeld door de **ISO** (_International Standards Organization_), dat dient als conceptuele referentie voor netwerken.


De vier lagen van het TCP/IP-model zijn:


- de NETWORK ACCESS Layer, die de protocollen voor de fysieke verbinding en de toegangscontrole voor media levert;
- de INTERNET Layer, die de routering en IP-adressering afhandelt;
- de TRANSPORT Layer, die de betrouwbaarheid en het beheer van gegevensstromen met protocollen zoals TCP of UDP garandeert;
- de APPLICATION Layer, die gebruikers- en softwareprotocollen zoals HTTP, FTP, SMTP en DNS groepeert.



![Image](assets/fr/006.webp)



Vandaag de dag is IPv4 de meest gebruikte versie van IP, maar de 32-bits Address-ruimte heeft duidelijke beperkingen. Dit leidde tot de creatie van IPv6, dat 128-bits adressering gebruikt en vrijwel onbeperkte capaciteit biedt: essentieel voor het ondersteunen van de explosieve groei van verbonden apparaten en het aangaan van de uitdagingen van het internet der dingen, mobiliteit en beveiliging.


Elke Layer van de TCP/IP stack levert specifieke diensten, waardoor het mogelijk is om Address verschillende netwerkbehoeften op een modulaire manier aan te pakken: fysieke transmissie, logische adressering, gegevensintegriteit en diensten op applicatieniveau.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## IPv5 QoS-protocol


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



De header van een IP pakket is een essentiële gegevensstructuur, verdeeld in verschillende velden, elk met een specifieke rol om ervoor te zorgen dat de pakketten correct worden verzonden en verwerkt terwijl ze door het netwerk reizen. Deze velden bevatten de bestemming IP Address (nodig om het pakket te routeren naar de beoogde ontvanger), de headerlengte aangegeven door het IHL (*Internet Header Length*) veld, de totale pakketlengte vastgelegd in het *Total Length veld*, controle- en verificatie-informatie en andere parameters voor het beheren van de communicatiestroom en kwaliteit.


Het allereerste veld in de header heet Version. Deze 4-bits waarde geeft aan welke versie van het IP-protocol het pakket volgt. Het is belangrijk omdat het elke router of tussenliggend apparaat vertelt hoe de ingekapselde gegevens moeten worden geïnterpreteerd en behandeld.


**Opmerking**: Het beheer en de toewijzing van IP-protocolversies vallen onder de verantwoordelijkheid van **IANA**. Een 4-bits veld maakt 16 binaire combinaties mogelijk (waarden 0 tot 15). Tot op heden is hun toewijzing als volgt:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Een daarvan is IPv5, dat, hoewel grotendeels onbekend bij het publiek, al bestond als ST (_Stream Protocol_). IPv5 werd ontwikkeld in de jaren 80 en was bedoeld om te voldoen aan een groeiende behoefte in die tijd: het bieden van "Quality of Service_" (QoS) voor bepaalde gegevensstromen die een continue, stabiele overdracht vereisten, zoals Voice over IP of multimediastromen. Het doel was om end-to-end bandbreedte en prioriteit te garanderen, een concept dat vergelijkbaar is met wat RSVP (_Resource Reservation Protocol_) tegenwoordig biedt voor het dynamisch reserveren van netwerkbronnen op moderne routers.


IPv5 bleef echter experimenteel en werd slechts op een klein aantal netwerkapparaten geïmplementeerd. De beperkte acceptatie, gecombineerd met de snel groeiende behoefte aan meer Address ruimte, bracht internetontwerpers ertoe om direct over te stappen van IPv4 naar IPv6. Dit omzeilde zowel de Address beperkingen van IPv4 als elk risico op verwarring of incompatibiliteit met de experimentele specificaties van IPv5.


Hoewel IPv5 nooit wijdverspreid gebruikt werd, speelde het een belangrijke rol in het vroege denken over QoS en verkeersmanagement. Vandaag de dag is het meer een historische markering dan een werkende standaard.


**Reminder** - Een protocol is een verzameling communicatieregels: gegevensstructuren, algoritmen, pakketformaten en conventies die verschillende apparaten in staat stellen om op een betrouwbare en begrijpelijke manier informatie te Exchange. Een service is de concrete implementatie van een protocol via specifieke programma's (clients, servers) die deze regels volgen en functionaliteit beschikbaar maken voor gebruikers en toepassingen. Een dienst is de concrete implementatie van een protocol door middel van specifieke programma's (clients, servers) die deze regels volgen en de functionaliteit beschikbaar maken voor gebruikers en toepassingen.


We kunnen nu de structuur en werking van het IP-protocol, de essentiële basis van alle netwerkcommunicatie, nader bekijken.



## Het IP-protocol


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definities en algemene informatie


Het IP-protocol, of "***Internet Protocol***", is de ruggengraat van het TCP/IP-model. Het transporteert gegevenspakketten van de ene host naar de andere binnen een netwerk, of het nu lokaal is of de hele wereld omspant. Het heeft twee belangrijke rollen: het beheren van de logische adressering van apparaten en ervoor zorgen dat pakketten worden gerouteerd over vaak heterogene en onderling verbonden netwerken.


Op fysiek niveau vertrouwt transmissie op hardware-interfaces om punt-tot-punt verbindingen tussen knooppunten tot stand te brengen. Het is echter het IP protocol dat end-to-end communicatie mogelijk maakt door elk pakket de informatie te geven die het nodig heeft om door meerdere mogelijke paden naar zijn bestemming te navigeren.


Drie netwerkconfiguraties Elements bepalen hoe een pakket op weg wordt gestuurd:


- IP Address**: identificeert de bestemmingshost op een unieke manier in het netwerk.
- Subnetmasker**: specificeert welk deel van het Address het netwerk identificeert en welk deel de host, wat een logische verdeling in subnetten mogelijk maakt.
- De gateway**: geeft de tussenliggende router aan waar het pakket doorheen moet om een extern netwerk of een ander segment van het lokale netwerk te bereiken.


Op het internet stromen gegevens niet als één continue stroom, maar worden ze verzonden als **datagrammen**: onafhankelijke blokken gegevens, elk ingekapseld met alle informatie die nodig is voor aflevering. Dit is het principe van **packet switching**, waarbij informatie wordt opgesplitst in zelfstandige eenheden die verschillende paden kunnen nemen om dezelfde ontvanger te bereiken.


Naast de payload (*payload*) bevat elk IP datagram een gestructureerde header met velden zoals de bestemming Address, bron Address, type dienst, protocol versienummer en andere controle-informatie die nodig is om de transmissie te beheren.


De theoretische maximale grootte van een IP datagram is **65.536 octetten**, een limiet die wordt bepaald door het totale lengte veld in de header. In de praktijk wordt deze grootte zelden bereikt, omdat de fysieke netwerken die de pakketten dragen (Ethernet, Wi-Fi, glasvezel...) meestal een striktere limiet opleggen, bekend als **MTU** (_Maximum Transmission Unit_). Als een datagram de MTU van de fysieke link overschrijdt, moet het worden opgesplitst in kleinere pakketten, die elk apart worden verzonden en bij aankomst weer worden samengevoegd.


Dit aanpassingsvermogen maakt IP tot een robuust en flexibel protocol dat kan werken met een grote verscheidenheid aan onderliggende technologieën met behoud van universele compatibiliteit tussen heterogene systemen en netwerken.



### Fragmentatie van IP-datagrammen


Wanneer een IP datagram door een netwerk moet waarvan de transmissiecapaciteit kleiner is dan het datagram zelf, moet het **gefragmenteerd** worden zodat het zonder problemen kan reizen. Deze fysieke limiet wordt de **MTU** (Maximum Transmission Unit) genoemd: de grootste framegrootte die door een bepaald netwerk kan gaan zonder gesplitst te worden.


Elke netwerktechnologie legt zijn eigen MTU op, bepaald door de hardware- en protocolkenmerken. Veel voorkomende waarden zijn:


- ARPANET**: 1000 bytes
- Ethernet**: 1500 bytes
- FDDI**: 4470 bytes


Wanneer een datagram de MTU van een netwerksegment waar het doorheen moet overschrijdt, zal routeringsapparatuur het opsplitsen in kleinere **fragmenten** die voldoen aan de limiet. Dit gebeurt meestal wanneer van een netwerk met een hoge MTU wordt overgestapt naar een netwerk met een lagere capaciteit. Bijvoorbeeld, een datagram dat van een FDDI netwerk komt kan gefragmenteerd moeten worden voordat het over een Ethernet segment verstuurd wordt.



![Image](assets/fr/008.webp)



Het fragmentatieproces werkt als volgt:


- De router breekt het datagram in fragmenten die niet groter zijn dan de MTU van het doelnetwerk.
- De grootte van elk fragment is een veelvoud van 8 bytes, omdat het IP protocol deze eenheid gebruikt om de hermontage offset te coderen.
- Elk fragment krijgt zijn eigen IP-header, die de informatie bevat die de uiteindelijke ontvanger nodig heeft om ze in de juiste volgorde weer samen te voegen.


Eenmaal gefragmenteerd reizen de stukken onafhankelijk door het netwerk. Ze kunnen verschillende routes nemen, afhankelijk van routeringstabellen, linkbelasting of uitval. Er is geen garantie dat ze aankomen in de volgorde waarin ze verzonden zijn.


Bij aankomst zorgt de ontvangende machine voor **herassemblage**. Met behulp van de informatie in de headers (gedeelde identifier, offset en fragmentatievlaggen), zet het de fragmenten terug in de juiste volgorde om het originele datagram te reconstrueren voordat het naar de volgende Layer wordt verzonden. Als er ook maar één fragment verloren gaat of beschadigd is, wordt meestal het hele datagram weggegooid, want zonder elk fragment zou het resultaat onvolledig of onbruikbaar zijn.


Hoewel effectief, hebben fragmentatie en hermontage nadelen: extra verwerking voor routers en hosts en een grotere kans op pakketverlies, waardoor er meer heruitzendingen kunnen plaatsvinden. Daarom zijn zorgvuldig MTU-beheer en optimalisatie van pakketgrootte belangrijk voor soepele, efficiënte IP-communicatie.



### Gegevensinkapseling


Om ervoor te zorgen dat gegevens correct door de lagen van het TCP/IP-model worden geleid, speelt het proces van **inkapseling** een sleutelrol. In elk stadium waarin een bericht van de applicatie van de verzender naar de machine van de ontvanger reist, wordt extra informatie, bekend als headers, toegevoegd. Deze headers geven tussenliggende apparaten en softwarelagen de instructies die ze nodig hebben om de gegevens te verwerken, af te leveren en, indien nodig, weer samen te voegen.


Wanneer een bericht wordt verzonden, passeert het de vier lagen van de TCP/IP stack. Bij elke Layer wordt een nieuwe header toegevoegd voor de bestaande gegevens: elke header bevat specifieke metadata, zoals logische of fysieke adressen, communicatiepoorten, volgnummers, foutcontrolevlaggen en alle informatie die nodig is om de transmissie en routering te beheren.


De overdracht verloopt dus volgens een gestructureerd proces:


- De Layer Applicatie creëert het initiële **bericht**, dat de ruwe gegevens bevat.
- De Transport Layer kapselt het in in een **segment**, voegt bron- en bestemmingspoorten, volgnummers en flow-control mechanismen toe.
- Het Internet Layer voegt aan het segment een IP-header toe om een **datagram** te vormen, waarin de IP-adressen van bron en bestemming worden gespecificeerd.
- De Network Access Layer wikkelt het datagram in een **frame**, voegt MAC adressen en integrity check codes (CRC) toe.



![Image](assets/fr/009.webp)



Dit inkapselingsproces garandeert zowel de integriteit en traceerbaarheid van de gegevens als de aanpasbaarheid ervan: wanneer ze van het ene netwerk naar het andere gaan, voorzien de headers apparaten van de informatie die nodig is om de route te kiezen, de geldigheid te controleren of indien nodig fragmentatie uit te voeren.


Bij aankomst wordt het proces omgekeerd: de ontvangende machine krijgt het frame bij de Network Access Layer, die de bijbehorende header leest en verwijdert. Het datagram wordt dan doorgegeven aan de Internet Layer, die de IP header leest en deze op zijn beurt verwijdert om het segment aan de Transport Layer af te leveren. De Transport Layer verwerkt de transportheaders, controleert de integriteit van de stroom en levert tenslotte het **bericht** in zijn oorspronkelijke staat af bij de doelapplicatie.



![Image](assets/fr/010.webp)



De transformatie van de gegevens bij elke Layer kan als volgt worden samengevat:


- Bericht**: blok informatie op de Layer-toepassing.
- Segment**: gegevenseenheid na inkapseling door de Transport Layer.
- Datagram**: vorm aangenomen na de toevoeging van de IP-header door het Internet Layer.
- Frame**: laatste blok dat klaar is voor verzending over het fysieke medium door de Network Access Layer.



![Image](assets/fr/011.webp)



Dit proces, dat essentieel is voor de betrouwbaarheid en universaliteit van internetcommunicatie, zorgt ervoor dat elk stukje data, hoe gefragmenteerd of complex ook, van begin tot eind kan worden getransporteerd terwijl het begrijpelijk en bruikbaar blijft voor de ontvangende machine.



### IP-adressering


Zelfs met pakketschakeling, fragmentatie en inkapseling kan een netwerk niet functioneren zonder een betrouwbaar adresseringssysteem. Om er zeker van te zijn dat elk gegevenspakket de juiste ontvanger bereikt, gebruikt het Internet Layer een unieke identificatie: de **IP Address**.

In IPv4 wordt een IP Address gecodeerd op **32 bits** en geschreven als vier decimale getallen gescheiden door punten, in het bekende N1.N2.N3.N4 formaat (bijvoorbeeld: 192.168.1.12).


Een IP Address bestaat uit twee delen:


- _netid_**: identificeert het netwerk waartoe de host behoort
- _hostid_**: identificeert de specifieke host binnen dat netwerk

Dankzij deze scheiding kan het wereldwijde internet logisch worden gestructureerd in vele onderling verbonden netwerken.


Historisch gezien was het IPv4-systeem gebaseerd op een op klassen gebaseerd schema, gelabeld van A tot E, dat het bereik van Address en hun bedoelde gebruik definieerde. Elke klasse kende een vast aantal bits toe aan het _netid_ en _hostid_, wat een directe invloed had op het mogelijke aantal netwerken en hosts.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Niet alle mogelijke waarden kunnen aan hosts worden toegewezen. Bijvoorbeeld, in een **klasse C** Address biedt de laatste byte 8 bits (256 waarden). Maar twee daarvan zijn gereserveerd:


- 0: identificeert het netwerk zelf
- 255: is de **broadcast** Address, gebruikt om een pakket in één keer naar alle hosts in het netwerk te sturen.

Dan blijven er 254 bruikbare adressen over voor apparaten.


Het aantal beschikbare adressen varieert sterk tussen de klassen: van grote openbare netwerken in klasse A, tot bedrijfsnetwerken in klasse B, tot kleinere lokale netwerken in klasse C.



![Image](assets/fr/013.webp)



Sommige Address bereiken zijn gereserveerd voor privégebruik en worden nooit direct op het internet gerouteerd. Deze staan bekend als **private adressen**, en worden gebruikt binnen organisaties, bedrijven of huizen, en vereisen Address vertaling, meestal NAT (*Network Address Translation*), om het openbare internet te bereiken. Dit zijn:


- Klasse A**: van 10.0.0.0 tot 10.255.255.255
- Klasse B**: van 172.16.0.0 tot 172.31.255.255
- Klasse C**: van 192.168.0.0 tot 192.168.255.255


Wanneer een apparaat met een private Address toegang heeft tot het internet, vervangt een NAT-geschikte router of gateway deze door een geldige publieke Address.


Voorbeeld: Als een host de Address **192.168.7.5** heeft, kunnen we hieruit afleiden:


- 192.168.7.0: netwerk Address
- 192.168.7.1: vaak de lokale router
- 192.168.7.5: de host zelf


Een ander speciaal geval is **127.0.0.1**, bekend als de "***loopback***".

Op Linux systemen wordt het geassocieerd met de Interface **lo**. Met deze Address kan een machine zichzelf Address voor lokaal testen of diagnostiek, zonder via een fysieke Interface te gaan. Het hele **127.0.0.0/8** bereik is gereserveerd voor dit doel.


Om het gebruik van Address te optimaliseren en complexe netwerken te ontwerpen, is het **subnetmask** (_netmask_) essentieel. Dit binaire masker scheidt het _netid_ van het _hostid_ in een IP Address.

Elke klasse heeft een standaard masker:


- 255.0,0,0** voor klasse A,
- 255.255.0.0** voor klasse B,
- 255.255.255.0** voor klasse C.


Een goed netwerkontwerp volgt een basisregel: apparaten die rechtstreeks met elkaar moeten communiceren, moeten zich in hetzelfde netwerk of subnet bevinden. Om een netwerk te segmenteren, gebruiken we subnetting, waarbij we een netwerk opdelen in kleinere subnetten door een specifieker masker te gebruiken.


Voorbeeld van subnetting:

Een **klasse C** netwerk: 192.168.1.0/24 met een standaard masker van 255.255.255.0.

We willen 4 subnetten van elk maximaal 60 hosts.


**Stap 1**: Aantal benodigde adressen per subnet = 60 + 2 gereserveerde adressen (netwerk + broadcast) = 62.


**Stap 2**: Zoek de dichtstbijzijnde macht van 2 ≥ 62. -> 2⁶ = 64.


**Stap 3: Pas het masker aan. Behoud de _netid_ bits en reserveer de benodigde _hostid_ bits. We verkrijgen een binair masker dat, na conversie, **255.255.255.192** geeft.


```
11111111 11111111 11111111 11000000
```


**stap 4**: Bereken de Address bereiken voor elk subnet, variërend met de bits die gereserveerd zijn voor de host.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**stap 5**: Dit creëert vier subnetwerken, die elk tot 62 machines ondersteunen, terwijl het algehele adresseringsschema efficiënt blijft. Het _hostid_ gedeelte wordt gesplitst in een _subnetid_ gedeelte en een host gedeelte.



![Image](assets/fr/016.webp)



Dit fundamentele principe van subnetting blijft onmisbaar in moderne netwerk engineering, en maakt precieze IP toewijzing, betere verkeerscontrole, sterke segment isolatie en schaalbaar netwerkbeheer mogelijk.



### CIDR-adressering


In het begin van de jaren 1990, toen het internet zich snel verspreidde door bedrijven en organisaties, begon het traditionele IP-adresseringssysteem op basis van klassen (A, B, C) zijn grenzen te tonen.

De rigide structuur leidde tot een aanzienlijke verspilling van IP-adressen en maakte routeringstabellen steeds groter, complexer en moeilijker te onderhouden.

Om Address deze problemen op te lossen, werd een flexibelere en efficiëntere methode geïntroduceerd: **CIDR** (_Classless Inter-Domain Routing_). CIDR is geleidelijk de standaard geworden en heeft het oude op klassen gebaseerde systeem grotendeels vervangen.


Het kernidee achter CIDR is de mogelijkheid om verschillende aangrenzende netwerken, vooral klasse C-blokken, te groeperen in een enkele logische eenheid die een **supernet** (_supernet_) wordt genoemd. Met deze aggregatie kan een enkele entry in de routeringstabel meerdere subnetwerken vertegenwoordigen, waardoor het aantal routes dat routers moeten verwerken wordt verminderd en hun prestaties worden verbeterd.


Terwijl klasse C-netwerken aanvankelijk de grootste behoefte hadden aan aggregatie vanwege hun kleinere capaciteit, is het principe ook toegepast op klasse B- en in theorie zelfs klasse A-netwerken, hoewel deze laatste minder beïnvloed worden dankzij hun grote Address-bereik.


Met CIDR verdwijnt het concept van vaste klassen. De Address ruimte wordt behandeld als een continu bereik dat naar behoefte kan worden verdeeld of samengevoegd. CIDR-blokken worden gedefinieerd met subnetmaskers die niet beperkt zijn tot de standaard A-, B- of C-klassen. Een CIDR-blok kan een enkel netwerk vertegenwoordigen of een aaneengesloten set subnetwerken die dezelfde prefix delen.


Een CIDR-blok wordt geschreven in het formaat "Address/prefix", waarbij het getal achter de schuine streep aangeeft uit hoeveel bits het netwerkgedeelte bestaat. Bijvoorbeeld, /17 betekent dat de eerste 17 bits het netwerk identificeren, terwijl de resterende 15 bits hosts identificeren.


Voorbeeld:

Een /17 blok bevat 2^(32-17) adressen dus 2^15 = 32.768 adressen in totaal. Als de twee gereserveerde adressen (netwerk en broadcast) hiervan worden afgetrokken, blijven er 32.766 bruikbare hostadressen over. Hierdoor kunnen netwerkbeheerders de grootte van hun subnetten precies afstemmen op de werkelijke behoeften en onnodige verspilling voorkomen.


Om de grootte van CIDR begrijpelijker te maken, is hier een tabel met veelvoorkomende prefixen en hun equivalente subnetmaskers en bruikbare adressen:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**OPMERKING**: Historisch gezien ontmoedigde RFC 950 het gebruik van subnet nul, voornamelijk om verwarring bij het routeren te voorkomen.  Deze beperking werd verouderd met RFC 1878, die het gebruik ervan volledig toestaat. De oude beperking was vooral te wijten aan de incompatibiliteit met oudere hardware die CIDR niet correct kon verwerken. Moderne apparatuur heeft dit probleem niet.


Het subnet **1.0.0.0** met het subnetmasker **255.255.0.0**, dat ooit dubbelzinnig was met de klasse A netwerkidentifier, is nu bijvoorbeeld perfect geldig en bruikbaar.


**TIP**: voor foutloze subnetberekeningen en snelle conversie van adressen naar CIDR-notatie zijn er handige tools zoals ***ipcalc***. Deze "netwerkcalculator" toont duidelijk Address-verdelingen, beschikbare bereiken en bijbehorende maskers, ideaal voor zowel beheerders als studenten die CIDR leren.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## Het TCP-protocol


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



Het **TCP protocol** (_Transmission Control Protocol_) speelt een centrale rol in het TRANSPORT Layer van het TCP/IP model. Het fungeert als een brug tussen toepassingen en het Internet Layer, en zorgt voor een betrouwbare overdracht van gegevens tussen twee verre machines.

Terwijl het IP protocol eenvoudig pakketten verstuurt zonder levering of volgorde te garanderen, zorgt TCP voor de integriteit en consistentie van de gegevensstroom door deze zonder verlies, in de juiste volgorde en zonder duplicaten af te leveren.


De belangrijkste verantwoordelijkheden van TCP zijn:


- Ontvangen segmenten opnieuw ordenen;
- De gegevensstroom bewaken om congestie te voorkomen;
- Gegevensblokken opsplitsen of opnieuw samenvoegen in geschikte eenheden (segmenten);
- Het opzetten en beëindigen van verbindingen tussen beide uiteinden van de communicatie beheren.


TCP is een verbindingsgeoriënteerd protocol, wat betekent dat het een expliciete, doorlopende relatie opzet tussen client en server. Om dit te doen gebruikt het **volgordenummers** en **bevestigingen**: voor elk verzonden segment wordt een unieke identificatie toegewezen zodat de ontvangende machine zowel de volgorde als de integriteit van de gegevens kan controleren. De ontvanger stuurt dan een bevestigingssegment terug met de **ACK vlag** op 1, wat de ontvangst bevestigt en het volgende verwachte volgnummer aangeeft.



![Image](assets/fr/018.webp)



Om de betrouwbaarheid te verbeteren maakt TCP gebruik van een timer: zodra een segment is verzonden, begint het af te tellen. Als er binnen de timeout-periode geen bevestiging arriveert, zendt de zender het segment automatisch opnieuw uit, in de veronderstelling dat het tijdens het transport verloren is gegaan. Dit automatische heruitzendmechanisme compenseert de verliezen die inherent zijn aan IP netwerken, die kunnen optreden in geval van congestie, routeringsfouten of hardwarestoringen.



![Image](assets/fr/019.webp)



TCP kan duplicaten detecteren en afhandelen. Als een opnieuw verzonden segment aankomt, maar het origineel ook opduikt, gebruikt de ontvanger de volgnummers om het duplicaat te identificeren en alleen de juiste kopie te behouden, waardoor elke dubbelzinnigheid wordt geëlimineerd.


Om dit proces te laten werken, moeten beide machines een gemeenschappelijk begrip hebben van hun initiële volgnummers. Dit wordt gegarandeerd door het volgen van een strikte verbindingsprocedure: aan de ene kant luistert de **server** op een specifieke poort, wachtend op een inkomend verzoek (passieve modus); aan de andere kant initieert de **client** actief de verbinding door een verzoek te sturen naar de server op dezelfde servicepoort.


**OPMERKING**: Een "poort" is een numerieke identificatie (van 0 tot 65.535) die is toegewezen aan een netwerktoepassing op een computer. Het wordt gebruikt om meerdere services te onderscheiden die tegelijkertijd op hetzelfde IP Address draaien. Wanneer een client gegevens verstuurt, geeft hij het poortnummer op zodat het besturingssysteem van de server weet welk programma het moet ontvangen (bijv. 80 voor HTTP, 443 voor HTTPS, 25 voor SMTP). Poorten werken als speciale deuren, sturen verkeer naar binnen en naar buiten, voorkomen verwarring tussen services en staan een fijnmazige toegangscontrole toe door middel van firewalls of filterregels.


De sequentiesynchronisatie Exchange is gebaseerd op het beroemde **"*drie-weg handdruk*"** mechanisme, vergelijkbaar met de manier waarop twee mensen elkaar begroeten om contact te maken. Deze initialisatiefase, die de betrouwbaarheid van TCP garandeert, vindt plaats in 3 fasen:

1. **SYN:** De cliënt stuurt een initieel synchronisatiesegment (**SYN**) met de juiste vlag ingesteld en een initieel volgnummer (bijv. C);

2. **SYN-ACK:** De ontvangende server antwoordt met een bevestigingssegment (**SYN-ACK**), het bevestigt het volgnummer van de cliënt en geeft zijn eigen initiële volgnummer;

3. **ACK:** De client stuurt een laatste bevestiging (**ACK**) ter bevestiging van de ontvangst van het volgnummer van de server, waarmee de synchronisatie is voltooid. De SYN vlag is nu uitgeschakeld en de ACK vlag blijft ingesteld om aan te geven dat de verbinding tot stand is gebracht.



![Image](assets/fr/020.webp)



Dit Exchange protocol zorgt ervoor dat beide partijen dezelfde nummeringsbasis delen voordat de payloadgegevens worden verzonden. Zodra deze synchronisatie is voltooid, wordt de sessie geopend: segmenten kunnen nu in beide richtingen reizen, elk bevestigd bij ontvangst, waardoor maximale betrouwbaarheid van de gegevensstroom wordt gegarandeerd.


Deze ***drievoudige handdruk*** heeft alleen betrekking op het tot stand brengen van een verbinding. Voor het sluiten gebruikt TCP een *vierwegs handdruk*: FIN → ACK → FIN → ACK, die garandeert dat er geen segment in transit verloren gaat voordat de verbinding volledig wordt verbroken.


Hoewel dit proces is ontworpen met het oog op robuustheid en betrouwbaarheid, heeft het ook kwetsbaarheden opgeleverd die misbruikt kunnen worden. Aanvallen zoals **IP Spoofing** zijn er bijvoorbeeld op gericht om deze vertrouwensrelatie te omzeilen of te verstoren door zich voor te doen als een geautoriseerde machine door middel van vervalste volgnummers, waardoor een breuk ontstaat die het mogelijk maakt om de gegevensstroom te onderscheppen of te manipuleren.


Om de risico's van sequentiesynchronisatie te beperken en de netwerkbelasting te beheren, gebruikt het TCP protocol een flow management techniek die bekend staat als "**_Sliding Window_**". Dit systeem regelt hoeveel gegevens er kunnen worden verzonden zonder dat er voor elk segment een onmiddellijke bevestiging nodig is, waardoor onnodige overbelasting van het netwerk wordt verminderd terwijl de betrouwbaarheid goed blijft.


In praktische termen definieert het glijdende venster een reeks volgnummers die vrij kunnen circuleren tussen zender en ontvanger zonder dat elk afzonderlijk segment wordt bevestigd. Als het zendende systeem bevestigingen ontvangt, "schuift" het venster: het schuift naar rechts en maakt zo ruimte voor nieuwe segmenten om verzonden te worden. De grootte van dit venster (cruciaal voor het optimaliseren van de doorvoer en het vermijden van congestie) wordt gespecificeerd in het "*Window*" veld van de TCP header.


**Voorbeeld**: als het initiële volgnummer 3 is en het venster zich uitstrekt tot volgnummer 5, kunnen de segmenten genummerd van 3 tot 5 worden verzonden zonder te wachten op individuele bevestigingen.



![Image](assets/fr/021.webp)



De grootte van het schuifvenster ligt niet vast; het wordt dynamisch aangepast aan de netwerkomstandigheden en de verwerkingscapaciteit van de ontvanger.  Als de ontvanger een grotere hoeveelheid gegevens kan verwerken, geeft hij dit aan via het Window-veld, waardoor de zender het venster kan vergroten. Omgekeerd, in het geval van overbelasting of het risico op verzadiging, kan de ontvanger om een vermindering vragen, de zender zal wachten tot het venster naar voren schuift om extra segmenten te verzenden.


Het protocol voorziet in een symmetrische procedure voor het afsluiten van een TCP verbinding om een nette, ordelijke afsluiting te garanderen. Elke machine kan het afsluiten initiëren door een segment te sturen met de **FIN** vlag op 1, om aan te geven dat het de bedoeling is om de communicatie te beëindigen. Er wordt dan gewacht tot alle in-transit segmenten zijn ontvangen en verdere gegevens worden genegeerd.


Na ontvangst van dit segment stuurt de andere machine een bevestiging, ook gemarkeerd met de FIN vlag. Vervolgens wordt het verzenden van de resterende gegevens voltooid voordat de lokale applicatie wordt geïnformeerd dat de coonectie is afgesloten. Deze dubbele bevestiging zorgt voor een ordelijke afsluiting en minimaliseert het risico op gegevensverlies.


Dit nauwkeurige beheer, dat de flexibele routering van IP combineert met de strikte controle van TCP, wordt vaak geïllustreerd door een diagram waarin de snelheid van het IP-protocol (dat werkt op een **"best effort"** basis, zonder leveringsgarantie) wordt afgezet tegen de betrouwbaarheid van het TCP-protocol (dat de transmissie beheert door middel van bevestigingen en onderhandelde reeksen).



![Image](assets/fr/022.webp)



In sommige gevallen is absolute betrouwbaarheid echter niet de prioriteit: snelheid en eenvoud wel. Dit geldt voor toepassingen zoals live streaming of VoIP, die enig pakketverlies kunnen verdragen zonder de gebruikerservaring ernstig te beïnvloeden. In zulke gevallen wordt de voorkeur gegeven aan **UDP** (_User Datagram Protocol_).


UDP werkt volgens een fundamenteel ander principe dan TCP: het is **verbindingsloos**, wat betekent dat er geen voorafgaande relatie wordt opgebouwd tussen zender en ontvanger. Wanneer een machine pakketten verstuurt via UDP, worden ze in één richting verstuurd; de ontvanger stuurt geen bevestigingen en de zender heeft geen bevestiging dat het bericht is aangekomen. De UDP header is met opzet minimaal en bevat alleen de bronpoort, bestemmingspoort, segmentlengte en een controlesom, zonder ingebouwde bevestiging of controlemechanisme. Zoals altijd worden IP-adressen gedragen door de onderliggende IP-header.


Een veelgebruikte analogie is dat TCP is als een **telefoongesprek**, waarbij een circuit wordt opgezet, gevolgd en gecontroleerd gedurende het gesprek. Het UDP protocol is als het posten van een post**, waarbij de verzender een brief in een brievenbus stopt zonder direct bewijs van aflevering of systematische feedback.


Deze complementariteit tussen TCP en UDP stelt moderne netwerken in staat om zich aan te passen aan verschillende behoeften, door te kiezen voor maximale betrouwbaarheid of prioriteit te geven aan snelheid, afhankelijk van de toepassing.



## Serviceprimitieven


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Gelaagde architectuur en Exchange organisatie


Zoals we gezien hebben, zijn **services** de concrete implementatie van de protocollen die we tot nu toe beschreven hebben. Hoewel het TCP/IP model verschilt van het **OSI** model, wordt dezelfde gelaagde aanpak gebruikt: elke Layer is ontworpen om een specifieke functie uit te voeren en **services** te leveren aan de Layer er direct boven, wat resulteert in een modulaire, robuuste en makkelijk te onderhouden architectuur.


Elke Layer bouwt voort op de mogelijkheden van de laag eronder en voorziet op zijn beurt de Layer erboven van een consistente Interface voor het beheren van gegevens. In deze architectuur heeft elke Layer zijn eigen **datastructuren**, zorgvuldig gedefinieerd om perfecte compatibiliteit met de andere lagen te garanderen. Deze compatibiliteit is essentieel voor een soepele, betrouwbare en duidelijke communicatie van het ene eindpunt naar het andere.


Twee belangrijke aspecten bepalen deze uitwisselingen:


- Verticaal aspect**: de relatie tussen een Layer en de Layer erboven of eronder (van Layer N naar Layer N+1, en omgekeerd).



![Image](assets/fr/023.webp)




- Horizontaal aspect**: de interactie tussen applicaties op afstand, d.w.z. de dialoog tussen een **client** en een **server**, in beide richtingen.



![Image](assets/fr/024.webp)



De gelaagde architectuur volgt het principe dat elke Layer alleen de informatie verwerkt die binnen zijn bereik valt: gegevensstructuren, headers en controlemechanismen verschillen van de ene Layer tot de andere, maar samen vormen ze een samenhangend systeem dat ervoor zorgt dat gegevens geleidelijk naar hun eindbestemming worden geleid.


**Herinnering**: Er wordt specifieke terminologie gebruikt om de data-eenheden te beschrijven die tussen lagen worden uitgewisseld:


- bericht** voor de toepassing Layer,
- segment** voor Transport Layer (TCP),
- datagram** voor Internet Layer (IP),
- frame** voor de Network Access Layer.


De onderstaande tabel vat de termen voor TCP- en UDP-contexten samen:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Serviceprimitieven en data-eenheden


De kern van dit systeem wordt gevormd door **service primitieven**, die fungeren als communicatie-interfaces. Deze primitieven werken als service desks, ze luisteren op gereserveerde specifieke **poorten** en stellen processen in staat om netwerkverbindingen op een gecontroleerde manier tot stand te brengen, te onderhouden en te beëindigen. Terwijl protocollen het formaat en de overdracht van gegevens over het netwerk organiseren, zijn het de **services en hun primitieven** die de verticale link tussen de lagen vormen.


Door het horizontale aspect (communicatie tussen gedistribueerde toepassingen) te combineren met het verticale aspect (interne interacties tussen lagen) levert het TCP/IP-model een complete, schaalbare architectuur. Het overlappen van deze twee perspectieven geeft een duidelijk overzicht van hoe gegevens worden uitgewisseld in gestructureerde netwerkcommunicatie.



![Image](assets/fr/026.webp)



### Deel samenvatting


In dit eerste grote deel hebben we de kernarchitectuur onderzocht die de configuratie en werking van de huidige Internet-verbonden netwerken bepaalt. Deze architectuur is gebaseerd op een **vier-Layer model**, geïnspireerd door het OSI model, en gebouwd rond de **TCP/IP** protocol suite, de ruggengraat van moderne communicatie. We zagen dat TCP, met zijn verbindingsgerichte aanpak, zorgt voor betrouwbare overdrachten, terwijl UDP, lichter en sneller, de voorkeur geniet als snelheid belangrijker is dan betrouwbaarheid.


De goede werking van dit model is afhankelijk van de implementatie van protocollen door middel van **service-primitieven**. Deze zorgen voor de koppeling tussen lagen, waardoor gegevensverwerking kan worden aangepast aan de specifieke vereisten van elk niveau, van transport tot toepassing, inclusief internet- en netwerktoegang. Deze modulaire aanpak maakt het systeem zowel flexibel als robuust.


IP-adressering is een andere hoeksteen van deze infrastructuur. Elk aangesloten apparaat wordt geïdentificeerd door een **uniek IP Address**, genomen uit een Address ruimte georganiseerd in **klassen** (van A tot E). Sommige van deze adressen zijn gereserveerd voor speciale doeleinden, zoals lokale loopback of multicast, terwijl andere, bekend als "privéadressen", niet over het internet worden gerouteerd zonder vertaling (NAT). Deze classificatie maakt een logische, hiërarchische organisatie van netwerken mogelijk.


We hebben ook het concept van **subnetwerken** onderzocht, dat het mogelijk maakt om een netwerk op te delen in segmenten om IP-bronnen beter te beheren en de gegevensstroom te optimaliseren. Hoewel handmatige onderverdeling met behulp van subnetmaskers een belangrijk principe blijft, is het grotendeels gemoderniseerd dankzij **CIDR** (_Classless Inter-Domain Routing_). Deze methode heeft het Address beheer getransformeerd door flexibelere en rationelere toewijzing van IP bereiken mogelijk te maken, terwijl de grootte van routeringstabellen wordt gereduceerd.


Door deze concepten - lagen, protocollen, serviceprimitieven, adressering en subnetting - onder de knie te krijgen, krijg je een solide basis voor het begrijpen van de technische werking van moderne netwerken en voor het efficiënt configureren van een netwerkinfrastructuur om aan de hedendaagse behoeften te voldoen.


In de volgende sectie gaan we dieper in op IPv4-adressering.



# IPv4-adressering


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## IPv4 gebruiken


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



In deze sectie gaan we dieper en bekijken we hoe **IPv4** adressen eigenlijk geïmplementeerd zijn in een echt netwerk. We ontleden hun formaat, de logica erachter en hoe ze verbonden zijn met andere belangrijke netwerk-Elements zoals **DNS-namen**, **MAC-adressen**, **subnetwerken** en **vertaaltechnieken**.


Een IP Address is een unieke numerieke identificatie die is toegewezen aan elk **netwerk Interface** op een apparaat. Het maakt het mogelijk om dit apparaat binnen een netwerk te lokaliseren en het te bereiken om gegevens te verzenden. Bijvoorbeeld een router, server, werkstation, netwerkprinter of zelfs een bewakingscamera heeft minstens één eigen IP Address. De IP Address maakt **routing** mogelijk, d.w.z. het verplaatsen van pakketten van punt A naar punt B, zelfs als deze fysiek ver uit elkaar liggen.


IP-adressen kunnen op twee manieren worden toegewezen:


- Statisch**: Handmatig ingesteld op het apparaat.
- Dynamisch**: Automatisch toegewezen op aanvraag door een DHCP-server (_Dynamic Host Configuration Protocol_). DHCP vereenvoudigt het netwerkbeheer door handmatige configuratie overbodig te maken en nauwkeurige controle mogelijk te maken door middel van reserveringen en leaseduren.


**IPv4**-adressen worden geschreven in een **32-bits** formaat opgedeeld in **vier bytes**. Elke byte bevat 8 bits en staat voor een decimaal getal van 0 tot 255. De 4 bytes worden gescheiden door punten om een duidelijke, leesbare notatie te vormen.


voorbeeld: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Elke bit in een byte heeft een waarde (of "gewicht"): de linkerbit (de meest significante bit) is 128 waard, de volgende 64, dan 32, 16, 8, 4, 2 en 1 voor de rechterbit (de minst significante bit). Op deze manier wordt binair schrift omgezet naar decimaal door de eenvoudige optelling van de ingestelde gewichten.


De onderstaande tabel illustreert deze correspondentie:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Om binair naar decimaal om te zetten, tel je de gewichten op van de bits die op 1 zijn gezet.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

Een IP Address identificeert een enkel **netwerk Interface**, niet het hele apparaat. Een router of firewall met meerdere poorten heeft meerdere interfaces, elk met een eigen IP Address. Eén Interface kan zelfs meerdere IP-adressen hebben (bijvoorbeeld om meerdere virtuele netwerken of diensten te bedienen).


Elk IP pakket bevat twee IP adressen in de header:


- De bron Address (**verzender**)
- De bestemming Address (**ontvanger**)

Routers lezen deze adressen om uit te zoeken wat het beste pad is om het pakket naar de bestemming te sturen. Zonder strikte adresregels zou netwerkverkeer niet correct kunnen worden gerouteerd en zou wereldwijde interconnectie van netwerken onmogelijk zijn.


Een IPv4 Address bestaat uit twee delen:


- NetID**: identificeert het netwerk
- HostID**: identificeert een apparaat binnen dat netwerk

Het **subnetmasker** bepaalt waar het NetID eindigt en het HostID begint, door aan te geven hoeveel bits bij elk deel horen. Hoe langer het NetID, hoe groter het aantal mogelijke subnetten, maar het aantal hosts per subnet neemt overeenkomstig af.


Oorspronkelijk waren IPv4-netwerken onderverdeeld in vijf **klassen**: (A, B, C, D en E). Elke klasse komt overeen met een specifiek NetID-bereik en definieert een vaste granulariteit:


- Klasse A: zeer grote netwerken met een groot aantal hosts
- Klasse B: middelgrote netwerken
- Klasse C: kleine netwerken
- Klasse D: adressen gereserveerd voor multicasting (_multicast_)
- Class E: experimentele adressen, niet gebruikt voor conventionele adressering



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Speciale adressen:


- Netwerk Address**: Identificeert het netwerk zelf (gebruikt in routeringstabellen).
- Broadcast Address**: Stuurt gegevens in één keer naar alle apparaten in het subnet (alle HostID-bits op 1).


De volgende bereiken zijn gereserveerd voor intern gebruik:


- 10.0.0.0/8** (privéklasse A)
- 127.0.0.0/8** (lokale loopback of _loopback_)
- 172.16.0.0 tot 172.31.255.255** (privé klasse B)
- 192.168.0.0 tot 192.168.255.255** (privé Klasse C)


Het adres **127.0.0.1** en, meer in het algemeen, het hele 127.0.0.0/8 bereik wordt gebruikt voor interne testen: elk verzoek dat ernaar gestuurd wordt, verlaat de machine nooit. Dit is handig om te controleren of een lokale netwerkdienst werkt zonder het bredere netwerk erbij te betrekken.


Om beter gebruik te maken van de Address ruimte, splitsen beheerders netwerken vaak op in **subnetten** met behulp van subnetmaskers of **CIDR** notatie (_Classless Inter-Domain Routing_). CIDR maakt nauwkeuriger beheer mogelijk en helpt verspilling van adressen te voorkomen. Tegenwoordig is CIDR essentieel voor het verfijnen van IP-bereiken en het verkleinen van routeringstabellen.


In moderne netwerken wordt IP-adressering meestal gekoppeld aan andere identifiers:



- domeinnaam** geregistreerd in een **DNS** (_Domain Name System_): Het associeert een numerieke IP Address met een mensvriendelijke naam.
- MAC Address**: een fysieke identificatie die in de netwerkkaart is gegraveerd, gebruikt voor lokaal transport (_Ethernet_). Wanneer een IP pakket fysiek verzonden moet worden, matcht de ARP tabel de IP Address met de MAC Address van de bestemming.


Om IPv4 Address tekorten op te vangen en Address beveiliging toe te voegen, gebruiken netwerken vaak Address vertaling (_NAT_). NAT maakt het mogelijk dat veel privé-apparaten een enkel openbaar IP Address delen bij toegang tot het Internet.


**Noot**: Online en ingebouwde OS-hulpprogramma's, zoals de [Grenoble CRIC calculator] (http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), maken het berekenen van subnetten en maskers veel eenvoudiger.

Deze hulpprogramma's helpen om het splitsen van netwerken efficiënt te plannen.


Concluderend, de broadcast Address blijft een praktische functie voor het versturen van hetzelfde bericht naar alle apparaten die verbonden zijn met een segment: dit wordt bereikt door alle bits in het HostID gedeelte op 1 te zetten zodat alle hosts het doelwit zijn.



## De verschillende soorten IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



IPv4-adressen vallen uiteen in twee hoofdcategorieën: openbare adressen, direct toegankelijk op het internet, en privéadressen, bedoeld voor intern gebruik binnen een lokaal netwerk.


Een publieke IPv4 Address is wereldwijd uniek en routeerbaar over het hele internet. Het wordt toegewezen door officiële instanties en is vereist voor publiekgerichte diensten zoals websites, e-mailservers of cloudinfrastructuur.

De wereldwijde uniciteit van deze adressen is essentieel om routeringsconflicten of botsingen te vermijden.


De **IANA** (_Internet Assigned Numbers Authority_), die opereert onder de **ICANN** (_Internet Corporation for Assigned Names and Numbers_), beheert de verdeling van deze IP-bereiken. Concreet verdeelt IANA de IPv4-ruimte in 256 blokken van grootte /8, volgens de CIDR-notatie. Elk blok vertegenwoordigt iets meer dan 16,7 miljoen adressen (2³² / 2⁸).


Deze unicast Address-blokken worden door IANA toevertrouwd aan de **Regional Internet Registries** (RIR's). Deze RIR's zijn verantwoordelijk voor de herverdeling van de adressen op regionaal niveau, volgens de werkelijke behoeften van toegangsproviders, bedrijven of overheden. De unicast Address-ruimte strekt zich uit van de blokken **1/8 tot 223/8**, met gedeeltes die gereserveerd zijn voor speciaal gebruik (onderzoek, documentatie, testen) of die direct zijn toegewezen aan een netwerk of RIR voor herdistributie.


Om na te gaan wie de eigenaar is van een openbaar IP Address, kun je de RIR-databases raadplegen met het **whois** commando, of door gebruik te maken van de webinterfaces die elk register biedt. Deze tools kunnen gebruikt worden om het Address te herleiden naar de organisatie of provider die het gedeclareerd heeft.


Omgekeerd zijn er privé IPv4-adressen, een praktisch antwoord op het tekort aan openbare adressen. Deze adressen, die niet routeerbaar zijn op het internet, zijn gereserveerd voor lokale omgevingen: bedrijfsnetwerken, thuis-LAN's, datacenters of computerclusters. Ze zijn niet uniek wereldwijd: veel privénetwerken kunnen dezelfde IP-bereiken hergebruiken zonder interferentie, zolang ze geïsoleerd blijven of een Address netwerkvertaalapparaat gebruiken om toegang te krijgen tot het internet.


Om een apparaat met een privé IP Address toegang te geven tot het internet, gebruiken netwerken NAT (Network Address Translation). NAT werkt door dynamisch het private Address te vervangen door een publieke, waardoor tientallen (of zelfs honderden) apparaten een enkel publiek IP Address kunnen delen. Deze methode optimaliseert het gebruik van IPv4 ruimte en voegt ook een Layer beveiliging toe door de interne netwerkstructuur te verbergen.


Een andere speciale categorie zijn **ongespecificeerde** adressen. De IPv4-notatie **0.0.0.0** of de IPv6-versie **::/128** betekent "geen specifieke Address". Een dergelijke Address is ongeldig als een netwerk Address bestemming, maar kan lokaal door een host gebruikt worden om "alle interfaces" of "nog geen Address toegewezen" aan te geven. Dit is gebruikelijk in dynamische DHCP Assignment of voor het luisteren op alle serverinterfaces.


IPv6 ondersteunt ook private adressering, maar de standaard beveelt over het algemeen publieke adressering aan om het stapelen van meerdere NAT-lagen te vermijden. De **site-local-adressen** (_site-local_) van het **fec0::/10**-blok werden afgeschaft door **RFC 3879** om redenen van consistentie en beveiliging. Ze werden vervangen door **Unique Local Addresses** (_ULA_) in het **fc00::/7** blok. Met ULA's kunnen privé IPv6-netwerken worden gemaakt met schone interne routering, waarbij gebruik wordt gemaakt van een willekeurig gegenereerde identifier van 40 bits om lokale uniciteit te garanderen.


De uitputting van IPv4 werd officieel bevestigd in 2011. Om de levensduur te verlengen, heeft de internetgemeenschap verschillende strategieën aangenomen:


- Geleidelijke migratie naar **IPv6**
- Wijdverbreid gebruik van **NAT**
- Strenger toewijzingsbeleid van RIR's, waarvoor precieze rechtvaardiging en beheer van Address behoeften nodig zijn
- Terugvordering van ongebruikte of vrijwillig geretourneerde Address-blokken door bedrijven


Deze maatregelen laten zien dat IP-adressering niet alleen een technische uitdaging is, maar ook een kwestie van mondiaal bestuur, die van centraal belang is voor de voortdurende uitbreiding van het internet.



## DNS, een Address map


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Laten we eerlijk zijn, mensen zijn niet goed in het onthouden van lange reeksen getallen, in binaire of decimale vorm. Deze uitdaging wordt nog groter met IP-adressen, die complex kunnen zijn en een enkel IP Address kan soms meerdere adressen maskeren, vooral wanneer technieken zoals NAT of virtuele hosting worden gebruikt.


Om het makkelijker te maken, gebruikt de Application Layer een systeem dat een IP Address koppelt aan een logische, door mensen leesbare naam. Dit is de rol van **DNS** (*Domain Name System*), een enorme, hiërarchische, gedistribueerde directory die leesbare domeinnamen koppelt aan IP-adressen. Het systeem is gebaseerd op een set protocollen en diensten. De meest gebruikte DNS-serversoftware is **BIND** (_Berkeley Internet Name Domain_), een open-source softwarepakket dat verwijst naar een groot deel van de DNS-infrastructuur van het internet.


Het kernidee achter DNS is eenvoudig: voor elke verbonden dienst, of het nu een website, mailserver of een andere netwerkdienst is, is er een record dat een domeinnaam aan een of meer IP-adressen koppelt. Dit werkt in twee richtingen:


- Forward resolution: het vertalen van een naam naar een IP Address.
- Omgekeerde resolutie: het vinden van de domeinnaam die bij een gegeven IP hoort Address.

Dit maakt netwerkadressering bruikbaar voor mensen met behoud van de precisie die routers nodig hebben om gegevens correct te verplaatsen.


Een domeinnaam is altijd hiërarchisch opgebouwd, waarbij elk niveau wordt gescheiden door een punt: de volledige naam wordt **FQDN** (_Fully Qualified Domain Name_) genoemd. Het meest rechtse deel is de **TLD** (_Top Level Domain_) zoals `.com`, `.org` of `.fr`. Het meest linkse deel geeft de host aan, d.w.z. de specifieke machine of dienst die gekoppeld is aan het IP Address.


Het DNS-systeem is ontworpen als een **boom van zones**. Een **zone** is een deel van de domeinnamenruimte dat wordt beheerd door een specifieke DNS-server. Een enkele zone kan meerdere **subdomeinen** bevatten, die op hun beurt kunnen worden gedelegeerd naar andere zones die door verschillende servers worden beheerd. Beheerders zijn verantwoordelijk voor het onderhouden van hun zones: het afhandelen van updates, delegaties en algemeen beheer.


Deze structuur maakt het niet alleen mogelijk om naar een hoofddomein te verwijzen (bijv. `example.com`), maar ook om records voor individuele hosts (`www`, `mail`, `ftp`, etc.) te verfijnen. In de begindagen van netwerken werd deze mapping afgehandeld met statische bestanden zoals (`/etc/hosts` op Unix systemen), maar een dergelijke methode werd al snel onpraktisch voor een snelgroeiend, onderling verbonden Internet.


Het is belangrijk om te begrijpen dat een **DNS-server** slechts een beperkt bereik kan hebben. Het is bijvoorbeeld mogelijk dat de interne DNS-server van een bedrijf niet direct toegankelijk is vanaf het internet. Als deze DNS niet is geconfigureerd om queries door te sturen, of geen vertrouwde relatie heeft met andere servers, zullen sommige queries mislukken: noch de naam, noch het IP Address kan dan buiten de gedefinieerde zone worden opgelost.


DNS speelt ook een rol bij het routeren van e-mail. Een **MX** (_Mail Exchange_) record specificeert bijvoorbeeld de mailservers die verantwoordelijk zijn voor het ontvangen van e-mails voor een bepaald domein. Deze records definiëren prioriteiten (wegingsfactor) en failover-oplossingen. Het zonebestand van een DNS-server moet een **SOA** (_Start Of Authority_) record bevatten, dat de server aanwijst als de officiële informatiebron voor die zone.


Dankzij de hiërarchische, gedistribueerde structuur blijft DNS een hoeksteen van het internet, waardoor gebruikers toegang hebben tot services via duidelijke, memorabele domeinnamen in plaats van lange, technische IP-adressen.


In het volgende hoofdstuk verkennen we een ander fundamenteel concept: **Ethernetadressen**, ook bekend als **MAC-adressen**, die ervoor zorgen dat gegevens worden afgeleverd op de fysieke Layer van lokale netwerken.



## Ethernet-adressen en ARP ontdekken


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definities


Om het datarouteringsprotocol betrouwbaar en consistent te laten werken, is één belangrijk onderdeel essentieel. Als mensen kunnen we een machine gemakkelijk identificeren aan de hand van het IP Address of de naam via DNS. Een machine moet echter ondubbelzinnig het apparaat van bestemming kunnen herkennen om pakketten af te leveren. Om dit te doen, vertrouwt ze op een specifieke hardware identificatie, direct gebruikt door haar netwerk Interface: de MAC Address (_Media Access Control_).


**Noot**: Dit heeft niets te maken met een "fysieke Address" in geheugenarchitectuur. In computers verwijst een fysiek geheugen Address naar een specifieke locatie op de geheugenbus, in tegenstelling tot een virtuele Address die beheerd wordt door het besturingssysteem. Een MAC Address heeft daarentegen uitsluitend betrekking op netwerkhardware.


Een MAC Address wordt permanent en uniek toegewezen door de fabrikant van de apparatuur. De MAC Address identificeert de netwerkkaart ondubbelzinnig, of het nu een computer, smartphone, printer of een ander aangesloten apparaat is. In tegenstelling tot een IP Address, die dynamisch kan veranderen (via een DHCP-server of handmatige configuratie), blijft de MAC Address normaal gesproken hetzelfde gedurende de levensduur van het apparaat, tenzij het opzettelijk wordt gewijzigd.


Elk netwerk Interface, bedraad of draadloos, heeft zijn eigen MAC Address. Deze Address wordt binnen de datalink Layer (Layer 2 van het OSI-model) gebruikt om de hardware Address in elk uitgewisseld netwerkframe in te voegen en te beheren. Dit wordt soms het _Ethernetadres_ of _UAA_ (_Universally Administered Address_) genoemd. Gestandaardiseerd op een lengte van 48 bits, of 6 bytes, wordt het geschreven in hexadecimale notatie, meestal in de vorm van bytes gescheiden door `:` of `-`.


Bijvoorbeeld: `5A:BC:17:A2:AF:15`


In deze structuur identificeren de eerste drie bytes de fabrikant van de netwerkkaart: dit staat bekend als de **OUI** (*Organisationally Unique Identifier*). Deze voorvoegsels, toegekend door de IEEE, worden ook gebruikt in andere hardware adresseringsschema's, zoals Bluetooth en LLDP, om wereldwijde uniciteit te garanderen.


### Een MAC Address wijzigen (MAC Spoofing)


In theorie is de MAC Address ontworpen om vast te blijven, maar er zijn manieren om hem te wijzigen, met name om aan bepaalde behoeften te voldoen of om bepaalde beperkingen te omzeilen. Deze handeling, die vaak _spoofing MAC_ genoemd wordt, houdt in dat de originele hardware Address vervangen wordt door een andere waarde, die op softwareniveau gedefinieerd wordt. Sommige besturingssystemen vergemakkelijken deze wijziging, vooral wanneer de eigenlijke Ethernet Address niet direct door het stuurprogramma gebruikt wordt.


De redenen voor zo'n verandering zijn uiteenlopend. Het kan zijn dat een bepaalde toepassing een specifiek Ethernet Address nodig heeft om correct te functioneren, of om een conflict van identieke adressen op te lossen tussen twee apparaten die hetzelfde lokale netwerk delen.


Het veranderen van de MAC Address kan ook worden gemotiveerd door privacyoverwegingen: door de unieke identificatiecode die op de kaart is gegraveerd te verbergen, verkleinen gebruikers de mogelijkheid dat hun apparaat wordt gevolgd door netwerken of bewakingsdiensten. Deze praktijk is echter niet zonder gevolgen. Het veranderen van een MAC Address kan bepaalde filterapparaten verstoren of vereist dat firewalls opnieuw geconfigureerd worden om de nieuwe hardware toe te laten.


Sommige netwerken, vooral Wi-Fi, gebruiken MAC Address filtering om alleen apparaten met goedgekeurde adressen toe te laten. Hoewel dit een basisniveau van controle toevoegt, is het op zichzelf niet veilig. Een aanvaller kan een geldige MAC Address onderscheppen die al op het netwerk is toegestaan en deze klonen om de beperkingen te omzeilen. Om deze reden moet MAC filtering altijd gecombineerd worden met sterkere beveiligingsmaatregelen.


### MAC/IP correspondentie


Om een lokaal netwerk efficiënt te laten werken, moet er een duidelijke koppeling zijn tussen fysieke adressen (MAC-adressen) en logische adressen (IP-adressen). Zonder deze koppeling kan een computer het IP Address van een bestemming kennen, maar niet weten hoe hij er fysiek gegevens naartoe moet sturen op het lokale netwerk.

Deze toewijzing wordt automatisch uitgevoerd door ARP (_Address Resolution Protocol_).


In de praktijk, wanneer een gebruiker de MAC Address wil weten die overeenkomt met een specifieke IP Address, kan de gebruiker het `arp` hulpprogramma gebruiken. Dit hulpprogramma controleert de lokale ARP-tabel van de machine om bekende overeenkomsten tussen IP-adressen en MAC-adressen op het lokale netwerk weer te geven. Op deze manier is het mogelijk om snel de effectieve link tussen de logische en fysieke lagen te controleren.


Praktisch voorbeeld: als je wilt controleren welke netwerkkaart overeenkomt met het IP Address `192.168.1.5`, gebruik dan het volgende commando:


```bash
arp –a 192.168.1.5
```


De uitvoer toont de bijbehorende fysieke Address (MAC), de aard van de invoer (statisch of dynamisch) en de Interface in kwestie.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Het is belangrijk om te onthouden dat de MAC Address en de IP Address twee totaal verschillende identificaties zijn, die echter nauw bij elkaar aansluiten. De MAC Address wordt door de fabrikant uniek in elke Interface van het netwerk gegraveerd en wordt gebruikt om het apparaat fysiek te identificeren op het lokale netwerk. De IP Address daarentegen is een logische Address die dynamisch of statisch wordt toegewezen, waardoor de machine zich bij het IP-netwerk kan aansluiten en Exchange pakketten buiten het lokale netwerk kan versturen.



- Visueel voorbeeld van MAC Address:


![Image](assets/fr/032.webp)




- Visueel voorbeeld van een IP Address:


![Image](assets/fr/027.webp)



In een bedrijfsomgeving kunnen deze twee adresseringsniveaus niet afzonderlijk functioneren. Wanneer een DHCP-server bijvoorbeeld automatisch een IP Address toewijst, wordt de MAC Address van het apparaat als uitgangspunt gebruikt. De computer stuurt een DHCP broadcast verzoek met daarin zijn MAC Address zodat de server een beschikbare IP Address kan toewijzen aan het juiste apparaat. Zonder deze hardware-identificatie zou de DHCP-server niet weten aan welk apparaat hij de Address moet leveren.


Het ARP-protocol is daarom fundamenteel: het zorgt voor de koppeling tussen IP-adressen en fysieke adressen, waardoor machines een logische bestemming kunnen vertalen naar een daadwerkelijke fysieke bestemming. Wanneer een computer een pakket naar een machine op hetzelfde netwerk moet sturen, raadpleegt hij eerst zijn ARP-tabel om te controleren of het MAC Address van de ontvanger al bekend is. Als dat niet het geval is, zendt hij een ARP-verzoek uit naar alle hosts op het lokale netwerk. De machine die het doel IP Address in dit verzoek herkent, antwoordt door zijn MAC Address op te geven. De verzender schrijft vervolgens dit IP/MAC paar naar zijn ARP cache, om te voorkomen dat hij de operatie elke keer moet herhalen als het verzoek wordt verzonden.


Deze ARP-tabel fungeert als een mini-mapping directory, dynamisch bijgewerkt op een vergelijkbare manier als DNS domeinnamen met IP-adressen associeert. Zonder ARP zou er geen lokale Exchange mogelijk zijn, aangezien de datalink Layer de MAC Address moet kennen om Ethernetframes correct in te kapselen.


Omgekeerd was het RARP protocol (_Reverse Address Resolution Protocol_) ontworpen voor de tegenovergestelde situatie: een machine die alleen zijn MAC Address kent in staat stellen om zijn IP Address te ontdekken. Dit was vaak het geval voor oudere werkstations zonder een lokale Hard schijf, die over het netwerk moesten booten en een IP Address moesten aanvragen. RARP werd uiteindelijk vervangen door **BOOTP** en daarna **DHCP**, die flexibeler en geautomatiseerder zijn.


Deze associatieprotocollen spelen een belangrijke rol bij het routeren. Een router is in wezen een machine met meerdere netwerkinterfaces die verschillende segmenten met elkaar verbindt. Wanneer een router een frame ontvangt, verwerkt hij dit om het IP datagram eruit te halen en onderzoekt hij de IP header om de bestemming te bepalen. Als de bestemming op een direct verbonden netwerk ligt, wordt het datagram direct afgeleverd nadat de header is bijgewerkt. Als de bestemming op een ander netwerk ligt, raadpleegt de router zijn routeringstabel om het beste pad, of _next hop_, naar de bestemming te bepalen.


Dit verdeelt de route in kortere, beter beheersbare segmenten. Elke tussenliggende router kent alleen de volgende stap, niet noodzakelijk de eindbestemming.


**Herinnering:** Directe levering vindt plaats als verzender en ontvanger zich op hetzelfde fysieke netwerk bevinden. Anders is er sprake van indirecte levering via een of meer routers.


De routeringstabel, die handmatig (statische routering) of dynamisch (dynamische routering) beheerd wordt, bevat de informatie die nodig is om te beslissen welke route genomen moet worden. In kleine netwerken volstaat een statische configuratie. In grotere infrastructuren is dynamische routering essentieel om routes automatisch aan te passen wanneer de topologie verandert of een link uitvalt.


De routeringstabel fungeert als een mapping tabel tussen doel-IP adressen en volgende gateways. Meestal worden netwerkidentifiers (_netwerk ID_) opgeslagen in plaats van elke individuele host Address, wat de grootte sterk vermindert.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Met behulp van deze invoer kan de router snel bepalen via welke Interface en naar welk knooppunt elk datagram moet worden gestuurd. In combinatie met ARP voor het oplossen van de overeenkomende MAC-adressen, zorgt dit voor een efficiënte en betrouwbare gegevensoverdracht over het netwerk.


Tot slot omvatten dynamische routeringsprotocollen standaarden zoals RIP (_Routing Information Protocol_), gebaseerd op het afstandsalgoritme, en OSPF (_Open Shortest Path First_), dat de kortste paden in een complexe topologie berekent. Deze protocollen brengen constant Exchange updates uit om routes te optimaliseren, transmissiekosten te verlagen en de bestendigheid tegen uitval of congestie te verbeteren.



## NAT: Address Vertaling


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definitie


Network Address Translation_ (NAT) is een techniek ontwikkeld om Address de geleidelijke uitputting van beschikbare IPv4-adressen tegen te gaan. NAT werd ontworpen als een tijdelijke oplossing vóór de wijdverspreide invoering van IPv6 en stelde bedrijven en individuen in staat om grote aantallen machines te blijven verbinden terwijl ze slechts een beperkte reeks openbare IP-adressen gebruikten.


**Belangrijke herinnering:** de overgang van IPv4 naar IPv6 lost theoretisch het uitputtingsprobleem op door de Address ruimte uit te breiden van 32 bits naar 128 bits, wat een bijna onbeperkt aantal adressen oplevert (2^128). In de praktijk is de overgang echter nog steeds onvolledig en NAT wordt nog steeds veel gebruikt.


Het principe achter NAT is eenvoudig maar zeer effectief: in plaats van een uniek publiek IP Address toe te wijzen aan elk apparaat op het interne netwerk, wordt een enkele routeerbare Address (of een kleine pool van adressen) gebruikt voor alle privéapparaten. De NAT-gateway, vaak geïntegreerd in de router of firewall, vertaalt dan dynamisch het interne IP Address samen met de informatie die nodig is om verkeer correct naar de buitenwereld te routeren, en zorgt ervoor dat antwoorden worden teruggestuurd naar de oorspronkelijke afzender.


Deze aanpak heeft een onmiddellijk voordeel: het verbergt de interne netwerkarchitectuur volledig. Voor een buitenstaander lijken alle verzoeken van werkstations, servers of printers afkomstig te zijn van dezelfde publieke identiteit. Privéadressen, meestal afkomstig uit gereserveerde reeksen (bijvoorbeeld 192.168.x.x of 10.x.x.x), blijven onzichtbaar voor het internet.


Naast het aanpakken van IPv4-schaarste, versterkt NAT ook de beveiliging door een eerste logische barrière te creëren tussen de interne en publieke netwerken. Ongevraagde inkomende communicatie wordt op natuurlijke wijze geblokkeerd, aangezien alleen verbindingen die vanuit het netwerk worden geïnitieerd, profiteren van de noodzakelijke vertaling om antwoorden te ontvangen.



![Image](assets/fr/035.webp)



### Soorten vertalingen


NAT kan op verschillende manieren geïmplementeerd worden om te voldoen aan specifieke behoeften. De twee belangrijkste werkwijzen zijn statische vertaling en dynamische vertaling.


**Statische vertaling** creëert een vaste mapping tussen een privé IP Address en een publieke IP Address. Elk intern apparaat is permanent gekoppeld aan zijn toegewezen openbare Address. Bijvoorbeeld, een intern apparaat geconfigureerd als 192.168.20.1 kan gekoppeld worden aan de routeerbare Address 157.54.130.1. Wanneer een uitgaand pakket het lokale netwerk verlaat, vervangt de router de Address van de bron van het pakket door de openbare Address, en voert de omgekeerde operatie uit voor inkomend verkeer. Deze bidirectionele vertaling is transparant voor de gebruiker.


**Waarschuwing:** Hoewel deze methode het interne netwerk isoleert, lost het het tekort aan publieke IP-adressen niet op, omdat je nog steeds evenveel publieke adressen nodig hebt als er machines zijn om bloot te stellen. Statische vertaling wordt daarom voornamelijk gebruikt wanneer bepaalde interne bronnen bereikbaar moeten blijven van buitenaf (webserver, mailserver...).


**Dynamische vertaling** daarentegen gebruikt een pool van publieke IP-adressen. Wanneer een interne host een verbinding start, wijst de router tijdelijk één van deze publieke adressen toe aan de private Address van de host voor de duur van de sessie. De koppeling is 1-op-1, maar tijdelijk: zodra de verbinding eindigt, wordt de publieke Address beschikbaar voor een ander apparaat. Dynamic NAT vermindert dus het aantal publieke adressen dat nodig is wanneer niet alle machines op hetzelfde moment online zijn, maar het vereist nog steeds een blok externe adressen dat minstens even groot is als het maximum aantal gelijktijdige verbindingen.


**Port translation** (PAT), ook bekend als *NAT overload* of *IP masquerading*, gaat een stap verder: alle private apparaten delen een enkel publiek IP Address (of een heel klein nummer). Om sessies te onderscheiden, wijzigt de gateway niet alleen de bron Address, maar ook de bronpoort. Hij houdt een tabel bij die elk *(private Address, private poort)* paar linkt aan een uniek *(public Address, public poort)* paar. Deze vorm van NAT wordt gebruikt in bijna alle thuisrouters, waardoor tientallen apparaten (computers, smartphones, aangesloten objecten, enz.) hetzelfde publieke IP Address kunnen delen, met behoud van vloeiende communicatie.


NAT verlengt dus de levensduur van IPv4, terwijl het een waardevolle Layer segmentatie en beveiliging toevoegt. Echter, naarmate IPv6 steeds meer gebruikt wordt en de enorme Address ruimte breder wordt, zal de rol van NAT waarschijnlijk afnemen, hoewel het voor compatibiliteits- en controledoeleinden in sommige omgevingen nog steeds gebruikt zal worden om verkeer te segmenteren en te filteren.


### NAT-implementatie


Om de goede werking van de Address vertaling te verzekeren, moet de NAT router of gateway een nauwkeurig register bijhouden van de toewijzingen die tot stand gebracht zijn tussen elke private Address op het interne netwerk en de publieke Address die het gebruikt om met de buitenwereld te communiceren. Deze informatie wordt opgeslagen in de zogenaamde "NAT vertalingstabel", die een centrale rol speelt in het beheren van het netwerkverkeer.


Elke entry in deze tabel verbindt minstens één paar: de interne IP Address van de verzendende machine en de externe IP Address die op het Internet zichtbaar zal zijn. Wanneer een pakket van het privé netwerk naar een publieke bestemming gestuurd wordt, onderschept de NAT router het frame, analyseert de IP en TCP/UDP headers en vervangt dan de privé bron-Address door de publieke Address van de gateway. Op het retourpad onderschept dezelfde gateway het inkomende pakket, controleert de mapping tabel en voert de omgekeerde operatie uit om de stroom om te leiden naar de oorspronkelijke interne IP Address.


Dit dynamische vertalingsprincipe berust op nauwkeurig tabelbeheer: elk item blijft geldig zolang er actief verkeer is om het te rechtvaardigen. Na een configureerbare periode van inactiviteit wordt de entry gewist en kan hij opnieuw gebruikt worden voor nieuwe verbindingen.


voorbeeld van een vereenvoudigde NAT-vertaaltabel:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

In dit voorbeeld, als er voor het tweede item in meer dan een uur (3600 seconden) geen pakket is doorgegeven, wordt het gemarkeerd als herbruikbaar. Omgekeerd duidt een duur van nul op een actieve communicatie, waarbij de toewijzing is vergrendeld.


Hoewel NAT transparant werkt voor de meeste gangbare toepassingen (web browsen, e-mail, bestandsoverdracht, enz.), kan het bijkomende uitdagingen creëren voor bepaalde netwerktoepassingen. Sommige technologieën vertrouwen op het expliciet uitwisselen van IP adressen of poorten in de payload van het pakket. Na het passeren van een NAT gateway wordt deze informatie inconsistent.


Typische voorbeelden van beperkingen zijn:


- Peer-to-peer protocollen (P2P), die rechtstreekse verbindingen tussen apparaten vereisen, worden gehinderd door de NAT barrière, aangezien alle interne machines hetzelfde externe IP Address delen en niet rechtstreeks bereikt kunnen worden zonder specifieke configuratie (zoals *port forwarding* of UPnP);
- Het IPSec protocol, dat gebruikt wordt om netwerkcommunicatie te beveiligen, versleutelt de headers van pakketten. Omdat NAT deze headers moet aanpassen om IP adressen te vervangen, maakt versleuteling dit onmogelijk zonder aanpassingsmechanismen zoals NAT-T (*NAT Traversal*);
- Het X Window protocol, waarmee grafische applicaties op afstand kunnen worden weergegeven op Unix/Linux, werkt zo dat de X server actief TCP verbindingen naar clients stuurt. Deze omkering van de gebruikelijke richting van verbindingen kan worden geblokkeerd door NAT.


In het algemeen zal elk protocol dat expliciet de interne IP Address in de payload van het pakket opneemt, beïnvloed worden, aangezien die Address na vertaling niet langer overeenkomt met de echte, op het internet zichtbare Address.


**Belangrijke opmerking:** Om Address deze problemen op te lossen, bieden sommige NAT routers _Deep Packet Inspection_ (DPI) of _Protocol Helpers_ aan, die de inhoud van pakketten inspecteren om adressen of poortnummers in toepassingsgegevens te identificeren en dynamisch te vervangen. Dit vereist diepgaande kennis van het protocolformaat en kan kwetsbaarheden in de beveiliging creëren of het gebruik van bronnen verhogen.


**Let op:** Hoewel NAT helpt om het interne netwerk te verbergen en binnenkomend verkeer te controleren, is het geen vervanging voor een toegewijde firewall. Translation alleen is geen volledige veiligheidsbarrière: het moet altijd aangevuld worden met duidelijke filterregels om ongevraagd of ongewenst verkeer te blokkeren.


om te illustreren hoe dit in de praktijk werkt, kun je het volgende voorbeeld bekijken:_



![Image](assets/fr/037.webp)



In dit scenario kan een intern werkstation toegang krijgen tot de interne webserver door eenvoudigweg de URL `http://192.168.1.20:80` aan te roepen. Het specificeren van de poort is hier optioneel, aangezien `80` de standaard HTTP poort is.Omgekeerd, als een verzoek van buitenaf komt, zal de gebruiker de publieke Address `http://85.152.44.14:80` invoeren. De NAT router ontvangt het verzoek, raadpleegt zijn mapping tabel en vertaalt automatisch de publieke Address in een private, waarbij de verbinding wordt omgeleid naar `http://192.168.1.20:80`.


Hetzelfde principe geldt voor elke andere server die geautoriseerd is om internetverbindingen te ontvangen, zoals de Extranet server (blauw circuit in het diagram).


**Praktische opmerking:** in gevirtualiseerde omgevingen worden vaak netwerkinterfaces met de naam _virbrX_ (voor _Virtual Bridge X_) gebruikt. Deze virtuele bruggen, in het bijzonder geleverd door de libvirt bibliotheek of de Xen hypervisor, verbinden het virtuele interne netwerk van gastmachines met het fysieke netwerk terwijl NAT wordt toegepast. Ze worden over het algemeen geconfigureerd via scripts in `/etc/sysconfig/network-scripts/`, zoals hieronder getoond voor `virbr0`:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Zodra de virtuele bridge is geïnstalleerd, moet je IP routing inschakelen en poortvertaling configureren met `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Met deze configuratie wordt uitgaand verkeer gerouteerd en NAT vertaling toegepast, waardoor virtuele machines met de buitenwereld kunnen communiceren zonder hun interne IP adressen direct bloot te geven.


In het volgende hoofdstuk zullen we in detail kijken naar IP Address configuratie onder Linux, met zowel eenvoudige als geavanceerde methodes geschikt voor verschillende beheercontexten.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Hoe configureer ik het netwerk met `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Standaardconfiguratie


Na het behandelen van de theoretische basis van netwerken en het begrijpen hoe IP adressen, maskers, routing en vertaling samenwerken, is het tijd om verder te gaan met de praktische configuratie. Op GNU/Linux wordt het instellen van netwerken nu afgehandeld met het **`ip`** commando (_iproute2_ pakket), dat het oudere `ifconfig` vervangt.


met `ip` kunt u op elk moment een IP Address toewijzen of wijzigen, een masker wijzigen, een Interface starten of stoppen, of de status controleren.


**TIPS:** om alle interfaces weer te geven (actief of niet): `ip addr show`


Voorbeeld: een statische Address toewijzen en Interface activeren


Address `192.168.1.2/24` toevoegen aan Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Interface activeren:


```shell
ip link set dev eth0 up
```


Deactiveer dezelfde Interface:


```shell
ip link set dev eth0 down
```


De status van een specifieke Interface weergeven:


```shell
ip addr show dev eth2
```


**Praktische tip:** met `ip`, heeft het toevoegen van een extra Address aan een Interface niet langer een `:1` suffix nodig. Voeg gewoon nog een `ip addr add ...` regel toe:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Activeringsscripts: ifup / ifdown


De `ifup` en `ifdown` utilities lezen statische configuratiebestanden uit `/etc/sysconfig/network-scripts/` (op RHEL, CentOS, Rocky Linux, AlmaLinux...) of `/etc/network/interfaces` (op Debian/Ubuntu) om interfaces netjes op of af te schakelen.


```shell
ifup eth1
ifdown eth2
```


Configuratiebestanden (RHEL-achtig):


- /etc/sysconfig/network**: globale instellingen (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: instellingen specifiek voor elke Interface.


Statisch voorbeeld (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


DHCP-voorbeeld:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Deze modulaire structuur is nog steeds geldig en kan eenvoudig worden geautomatiseerd op huidige systemen.


### Geavanceerde configuratie: bonding


In professionele omgevingen is het doel om dienstcontinuïteit te garanderen en/of bandbreedte te aggregeren. *Bonding* (of *teaming* met _teamd_) mechanismen voorzien in deze behoeften: meerdere fysieke interfaces functioneren als een enkele logische Interface, vaak `bond0` of `team0` genoemd.



![Image](assets/fr/039.webp)



Vereisten:


- Laad de `bonding` module (of gebruik `teamd`) ;
- Zorg dat er minstens twee fysieke interfaces beschikbaar zijn.


#### De verschillende gebruikelijke hechtmethoden:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Instellen met `ip link



- Fysieke interfaces uitschakelen:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Creëer de Interface:


```shell
ip link add bond0 type bond mode balance-alb
```



- Opties configureren na het aanmaken


```shell
ip link set bond0 type bond miimon 100
```



- MAC- en IP-adressen toewijzen:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Slave-interfaces aansluiten:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Breng alles weer naar boven:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Tip:** om een slaaf los te koppelen zonder de verbinding te verbreken: `ip link set eth1 nomaster`


#### Permanente configuratie (RHEL-achtig)


Maak drie bestanden aan in `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Dan:


```shell
systemctl restart network
```


#### Extra IP Address (moderne alias)


Met `ip` kunt u eenvoudig een tweede Address aan hetzelfde apparaat toevoegen:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Om deze alias persistent te maken na een reboot, voeg je een tweede `IPADDR2=...` / `PREFIX2=...` blok toe aan `ifcfg-eth0`, of maak je een nieuwe *NetworkManager* verbinding via `nmcli`.


Dankzij `ip` en verwante commando's (`ip link`, `ip addr`, `ip route`) is netwerkconfiguratie consistenter, scriptbaarder en duidelijker. Bonding is een sleutelcomponent van high-availability architecturen en het toewijzen van meerdere adressen aan een enkele Interface is veel eenvoudiger geworden.


In het volgende hoofdstuk kijken we naar de bijzonderheden en implementatie van IPv6-adressering.


# IPv6-adressering


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: standaarden en definities


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



We gaan nu over naar de volgende generatie van IP-adressering: het IPv6-protocol, oorspronkelijk bekend als IPng (_IP Next Generation_). Dit protocol is ontworpen om de structurele beperkingen van IPv4 te overwinnen en introduceert een enorm uitgebreide adresarchitectuur en talrijke technische optimalisaties.


De beweegredenen voor de invoering van IPv6 zijn uiteenlopend en Address cruciaal voor de evolutie van het internet. Ten eerste moet IPv6 de exponentiële groei van het aantal aangesloten apparaten ondersteunen (een doelstelling die onhaalbaar is met de beperkte Address ruimte van IPv4). Ten tweede wil het protocol de omvang van routeringstabellen verminderen, waardoor uitwisselingen efficiënter worden en de werklast van routers op de lange termijn afneemt.


IPv6 streeft ook naar het vereenvoudigen van bepaalde aspecten van pakketverwerking, het verbeteren van datagram flow en het optimaliseren van overdrachtssnelheden tussen netwerken. Vanuit een beveiligingsstandpunt zijn de AH/ESP headers van het *IPsec* protocol opgenomen in de basisspecificatie en alle IPv6 knooppunten moeten deze kunnen ondersteunen (RFC 6434). Het gebruik ervan blijft echter optioneel: het is aan de beheerder om ze in te schakelen afhankelijk van de context.


Andere doelstellingen zijn een nauwkeuriger behandeling van diensttypes, met name om een betere kwaliteit te garanderen voor real-time toepassingen (VoIP, videoconferenties, enz.). IPv6 is ook ontworpen om flexibeler mobiliteitsbeheer mogelijk te maken: een apparaat kan van toegangspunt veranderen zonder zijn Address te veranderen op een manier die zichtbaar is voor zijn peers.


Tot slot is IPv6 ontworpen om naast bestaande protocollen te bestaan. Hoewel het niet direct binair compatibel is met IPv4, blijft het volledig interoperabel met hogere-Layer protocollen zoals TCP, UDP, ICMPv6 en DNS, evenals met routeringsprotocollen zoals OSPF en BGP, met bepaalde aanpassingen. Voor multicastbeheer gebruikt IPv6 het MLD-protocol (*Multicast Listener Discovery*), dat het functionele equivalent is van IGMP in de IPv4-omgeving.


### Notatieregels


Een van de belangrijkste veranderingen in IPv6 is het formaat van het IP Address zelf. Om Address te maken van het chronische tekort aan IPv4-adressen, is de lengte van de Address verhoogd van 32 bits naar 128 bits, dus 16 bytes. In theorie levert dit een mogelijke Address ruimte op van:


$$3,4 maal 10^{38}$$


Dit garandeert een vrijwel onbeperkte capaciteit voor alle huidige en toekomstige apparatuur.


IPv6-adressen worden heel anders geschreven dan de bekende decimale notatie. Een IPv6 Address bestaat uit acht groepen van 16 bits, geschreven in hexadecimaal en gescheiden door dubbele punten `:`.


Bijvoorbeeld:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Om de notatie te vereenvoudigen kunnen voorloopnullen in elke groep worden weggelaten. Het bovenstaande voorbeeld wordt dan:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Bovendien kan een enkele doorlopende reeks van nulgroepen vervangen worden door::, waardoor de Address nog korter wordt:


```
1987:c02:0:84c2::cf2a:9077
```


**Waarschuwing:** deze regel is strikt: slechts één reeks opeenvolgende nullen kan vervangen worden door `::`. Als een Address meerdere reeksen nullen bevat, wordt alleen de langste gecondenseerd. Dit garandeert zowel uniciteit als leesbaarheid.


**Belangrijk detail:** het `:` teken dat gebruikt wordt om hexadecimale blokken te scheiden kan dubbelzinnigheid veroorzaken in URLs, aangezien `:` ook gebruikt wordt om een service poort aan te geven. Om verwarring te voorkomen moeten IPv6-adressen in URL's omsloten worden door vierkante haken `[ ]`.


Voorbeeld van HTTP toegang tot een specifieke poort voor de Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Wanneer je een IPv4 Address weergeeft in een IPv6 context, kun je een gemengde notatie gebruiken in gestippelde decimale vorm, voorafgegaan door`::`:


```
::192.168.1.5
```


Deze compatibiliteit helpt de overgang tussen de twee protocollen te vergemakkelijken doordat IPv4-blokken kunnen worden opgenomen in de IPv6 Address-ruimte.


**Note:** Om te standaardiseren hoe adressen geschreven worden, definieert RFC 5952 een canoniek formaat met afkortingsregels om meerdere weergaven van dezelfde Address te vermijden. Het opvolgen van deze aanbevelingen helpt misinterpretatie te verminderen en zorgt voor consistente netwerkconfiguraties.


### IPv6 Address types


IPv6 verschilt van zijn voorganger door een brede reeks Address categorieën, elk ontworpen voor specifiek gebruik, terwijl flexibele routering en netwerkbeheer mogelijk zijn. Net als bij IPv4 kunnen adressen globaal, lokaal, gereserveerd of specifiek voor bepaalde overgangsmechanismen zijn.


Een niet-gespecificeerde IPv6 Address wordt weergegeven door `::` of, explicieter, `::0.0.0.0`. Deze speciale vorm wordt gebruikt tijdens het verkrijgen van Address, of als standaardwaarde om de afwezigheid van een Address aan te geven.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *Op een privé LAN heeft het `fd00::/8` voorvoegsel de voorkeur voor het toewijzen van interne adressen die niet routeerbaar zijn op het Internet.*


#### Gereserveerde adressen


Bepaalde IPv6-bereiken zijn expliciet gereserveerd en mogen niet als algemene adressen worden gebruikt. Ze hebben specifieke technische doeleinden:


- `::/128`**: niet-gespecificeerde Address, nooit permanent toegewezen aan een apparaat, maar gebruikt als bron-Address door een machine die op configuratie wacht.
- `::1/128`**: de _loopback_ Address, het directe equivalent van `127.0.0.1` in IPv4, waarmee een machine Address zelf kan bereiken.
- 64:ff9b::/96`**: Gereserveerd voor protocolvertalers om IPv4/IPv6-interconnectie mogelijk te maken, zoals gedefinieerd in RFC 6052.
- `::ffff:0:0/96`**: compatibiliteitsblok voor het representeren van een IPv4 Address in een specifieke IPv6-structuur, vaak intern gebruikt door applicaties.


Deze blokken garanderen interoperabiliteit en vergemakkelijken de migratie tussen de twee protocolversies.


#### Globale unicast-adressen


Globale unicast-adressen vormen het grootste deel van de openbaar routeerbare IPv6-ruimte en vertegenwoordigen ongeveer 1/8e van de Address-ruimte. Sinds 1999 heeft IANA deze blokken, zoals het voorvoegsel `2001::/16`, in CIDR-blokken (van `/23` tot `/12`) toegewezen aan regionale registers, die ze vervolgens herdistribueren naar providers en organisaties.


Sommige reeksen hebben speciale gedocumenteerde toepassingen:


- `2001:2::/48`**: Gereserveerd voor het testen van prestaties en interoperabiliteit (RFC 5180).
- `2001:db8::/32`**: Gereserveerd voor documentatie en voorbeelden (RFC 3849).
- `2002::/16`**: Gebruikt voor het 6to4-mechanisme, waarmee IPv6-verkeer over een IPv4-infrastructuur kan reizen (handig tijdens de overgangsfase tussen de twee protocollen).


**Noot:** een groot deel van de wereldwijde adressen blijft ongebruikt en dient als reserve voor toekomstige groei van het internet.


#### Unieke lokale adressen (ULA)


Unieke lokale adressen (`fc00::/7`) zijn het IPv6-equivalent van IPv4 privéadressen (RFC1918). Ze maken het mogelijk om geïsoleerde interne netwerken te maken zonder risico op conflicten met openbare adressering. In de praktijk is het effectieve voorvoegsel `fd00::/8`, waarbij het 8e bit op 1 wordt gezet om lokaal gebruik aan te geven. Elk ULA-blok bevat een 40-bits pseudo-willekeurige identifier, waardoor Address botsingen worden geminimaliseerd bij het verbinden van afzonderlijke privé-netwerken.


#### Link-lokale adressen


Link-local adressen (`fe80::/64`) worden uitsluitend gebruikt voor communicatie binnen hetzelfde Layer 2 segment (hetzelfde VLAN of switch). Ze worden nooit verder dan de lokale link gerouteerd. Elk netwerk Interface genereert automatisch een link-local Address, vaak afgeleid van zijn MAC Address met behulp van het EUI-64 schema.


**Speciale eigenschap**: dezelfde machine kan dezelfde link-local Address gebruiken op meerdere interfaces, maar de Interface moet gespecificeerd worden bij het communiceren om ambiguïteit te voorkomen.


#### Multicast-adressen


In IPv6 is broadcast vervangen door multicast, een efficiëntere manier om pakketten af te leveren bij een gedefinieerde groep ontvangers. Het multicastbereik wordt voorafgegaan door `ff00::/8`. Dit omvat adressen zoals `ff02::1`, die zich richten op alle knooppunten op de lokale verbinding. Hoewel dit handig is, wordt dit Address niet langer aanbevolen voor toepassingen, omdat het generate ongecontroleerde uitzendingen kan veroorzaken.


Een veelgebruikt gebruik van multicast is het _Neighbor Discovery Protocol_ (NDP), dat ARP vervangt in IPv6. NDP gebruikt specifieke multicast adressen, zoals `ff02::1:ff00:0/104`, om automatisch andere hosts te ontdekken die met dezelfde link verbonden zijn.


Door deze Address-types te combineren, biedt IPv6 een complete set opties om te voldoen aan de behoeften van globale routering, lokale communicatie, IPv4/IPv6-migratie en automatische apparaatconfiguratie, terwijl de transmissie-efficiëntie wordt verbeterd.


### Address reikwijdte


Het bereik van een IPv6 Address definieert het exacte domein waarin het geldig en uniek is. Het begrijpen van dit concept is de sleutel tot het beheersen van pakketroutering en de logische organisatie van een IPv6-netwerk. IPv6-adressen worden over het algemeen gegroepeerd in drie hoofdcategorieën op basis van hun bereik en gebruik: unicast, anycast en multicast.


**Unicast-adressen** komen het meest voor en omvatten verschillende subtypes.

Deze omvatten de _loopback_ (`::1`) Address, waarvan het bereik beperkt is tot de host die hem gebruikt en die gebruikt wordt om de netwerk stack intern te testen zonder verkeer over het fysieke netwerk te sturen.

Dan zijn er link-local adressen (_link-local_), waarvan het bereik beperkt is tot een enkel netwerksegment: ze worden gebruikt voor directe communicatie tussen apparaten op dezelfde fysieke of logische link (bijvoorbeeld een enkele switch of VLAN).

Tenslotte zijn unieke lokale adressen (_ULA_, voor _Unique Local Addresses_) intern binnen een privénetwerk. Ze kunnen worden gerouteerd tussen meerdere privésegmenten maar zijn nooit zichtbaar op het internet.


Conceptueel worden IPv6-adressen vaak voorgesteld als een binaire structuur waarbij de eerste helft (de eerste 64 bits) de netwerkprefix identificeert en de tweede helft (ook 64 bits) uniek de Interface van het apparaat op dat netwerk identificeert. Deze splitsing maakt Address autoconfiguratie eenvoudiger door mechanismen zoals SLAAC (_Stateless Address Autoconfiguration_), die machines in staat stellen om automatisch generate een stabiele Address te kiezen op basis van het MAC Address of een pseudo-willekeurige identificatiecode.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

De IPv6-architectuur volgt het hiërarchische globale routeringsmodel van het huidige internet. Prefix-partitionering stelt regionale registers en netwerkoperators in staat om de Address toewijzing op een gedecentraliseerde manier te beheren, terwijl globale uniciteit gewaarborgd blijft. Binnen dit kader kan dezelfde host tegelijkertijd een globale unicast Address hebben voor internetcommunicatie en een link-lokale Address voor lokale interacties, bijvoorbeeld met de directe omgeving of voor routerzoekberichten.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Anycast-adressen** vertegenwoordigen een tussenliggend concept dat voortbouwt op het unicast-model maar zich in bepaalde gevallen als multicast kan gedragen. Een anycast Address is in wezen een unicast Address toegewezen aan meerdere interfaces verdeeld over verschillende netwerkknooppunten. Wanneer een pakket naar een anycast Address wordt gestuurd, heeft het IPv6-protocol als doel het af te leveren bij een van de hosts die deze Address deelt, meestal degene die het dichtst in de buurt zit qua routeringstopologie. Deze aanpak optimaliseert de verwerkingssnelheid van query's en verbetert de veerkracht van gedistribueerde diensten. Een klassiek voorbeeld zijn de root DNS servers, waar anycast adressering automatisch queries naar het dichtstbijzijnde point of presence leidt.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

In IPv6 vervangen **multicast-adressen** het broadcast-mechanisme, dat te duur en ongeschikt werd geacht voor een wereldwijd netwerk. Een multicast Address identificeert een groep interfaces, typisch over meerdere hosts, die dezelfde pakketten tegelijkertijd willen ontvangen.

Elke multicast Address bevat een speciaal 4-bit _scope_ veld, dat de geografische of logische limiet van de uitzending definieert:


- Een bereik van `1` betekent dat het pakket alleen voor het lokale apparaat is.
- Een scope van `2` beperkt het pakket tot de lokale link: alle apparaten op hetzelfde fysieke of virtuele segment kunnen het ontvangen.
- Een bereik van `5` breidt het bereik uit tot een site, meestal een heel bedrijfsnetwerk.
- Een bereik van `8` breidt het bereik uit naar een organisatie, waardoor levering over alle subnetten van dezelfde entiteit mogelijk is.
- Een bereik van `e` (14 in hexadecimaal) geeft een globaal bereik aan, waardoor de multicastgroep overal op het Internet toegankelijk is als de routeringsinfrastructuur dit ondersteunt.


De structuur van een IPv6 multicast Address omvat:


- een _Flag_ veld (4 bits) specificeert of de groep permanent of tijdelijk is,
- een _Scope_ veld (4 bits) definieert het bereik,
- een identificatieveld (112 bits) dat het multicastgroepnummer identificeert.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Een bekend voorbeeld van IPv6 multicast in actie is het _Neighbor Discovery Protocol_ (NDP). In plaats van ARP te gebruiken zoals in IPv4, vertrouwt NDP op multicastadressen zoals `ff02::1:ff00:0/104` om verzoeken voor het vinden van buren uit te zenden, die alleen gericht zijn op de relevante hosts op dezelfde link.


Door Address scopes zo nauwkeurig te definiëren, structureert IPv6 hoe datastromen worden verzonden, ontvangen en gerouteerd. Deze granulariteit maakt het protocol flexibeler en efficiënter voor het beheren van zowel lokale als globale communicatie, terwijl de nadelen van generalized broadcasting worden vermeden.


## Address Assignment in een lokaal netwerk


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


In dit hoofdstuk bekijken we een van de meest praktische aspecten van de implementatie van IPv6: het toewijzen van IP-adressen aan hosts op een lokaal netwerk. De IPv6 architectuur is ontworpen met het oog op flexibiliteit, zodat elk apparaat generate automatisch zijn eigen Address kan toewijzen, terwijl het nog steeds volledig handmatig geconfigureerd kan worden als dat nodig is.


Een IPv6 lokaal netwerk verdeelt de Address systematisch in twee delen:


- de eerste 64 bits vertegenwoordigen de subnet prefix, meestal geleverd door een router of een Address instantie;
- de resterende 64 bits worden door de host gebruikt om zichzelf uniek te identificeren op dat segment.

Dit model vereenvoudigt routeaggregatie en Address blokbeheer aanzienlijk.


Er worden twee belangrijke benaderingen gebruikt om adressen toe te wijzen aan apparaten:


- Handmatige configuratie, waarbij de beheerder de exacte Address van elke Interface specificeert;
- Automatische configuratie, waarbij apparaten generate of hun eigen adressen dynamisch verkrijgen.


Bij handmatige configuratie wijst de beheerder de volledige IPv6 Address toe aan elke Interface. Bepaalde waarden blijven gereserveerd:


- `::/128`: niet gespecificeerd Address, nooit permanent toegewezen ;
- `::1/128`: loopback Address (_loopback_), IPv4-equivalent: `127.0.0.1`.


In tegenstelling tot IPv4 is er geen _broadcast_ concept; "all neros" of "all ones" combinaties in het hostgedeelte hebben geen speciale betekenis.

Handmatige configuratie is nog steeds nuttig in gecontroleerde omgevingen, maar wordt moeilijk te onderhouden op schaal.


Voor automatische configuratie bestaan verschillende methoden:


- Het **NDP** (_Neighbor Discovery Protocol_) protocol, gespecificeerd door RFC4862, maakt *stateless* auto-configuratie mogelijk. In deze modus ontvangt de host een netwerkprefix van een lokale router, en vult de Address zelf aan met een identificator gebaseerd op zijn MAC Address. Deze methode is eenvoudig te implementeren en vereist geen centrale server.
- Implementaties zoals die in Windows kunnen het hostgedeelte pseudo-willekeurig generate om de privacy te verbeteren door directe blootstelling van het MAC Address te vermijden. Het zichtbaar maken van het MAC Address in IPv6 pakketten kan privacyproblemen opleveren, omdat het het mogelijk maakt om een apparaat over verschillende netwerken te volgen.
- DHCPv6-protocol: Gedefinieerd in RFC3315 en vergelijkbaar met DHCP gebruikt voor IPv4, maakt het een meer gecontroleerde en gecentraliseerde configuratie mogelijk, inclusief leasebeheer, extra opties (DNS, MTU...) en registratie van databases. DHCPv6 kan alleen werken of naast stateless configuratie om aanvullende parameters te bieden zonder het IP Address zelf toe te wijzen.


**Belangrijke opmerking:** Bij de MAC-gebaseerde methode wordt de MAC Address geconverteerd naar een 64-bits identificatie met behulp van het EUI-64-formaat. Dit mechanisme voegt de bytes `FF:FE` toe in het midden van de oorspronkelijke MAC Address (in 48 bits) en inverteert het 7de bit om globale uniciteit aan te geven. Het resultaat is een stabiele Interface identificatie, gebruikt in de volledige IPv6 Address.


Hier is een voorbeeld van hoe je een MAC Address omzet in EUI-64:


![Image](assets/fr/045.webp)



Vanwege de groeiende bezorgdheid over het volgen van apparaten, staan moderne besturingssystemen (met name Linux, Windows 10+, macOS, Android) nu standaard privacy-extensies aan. Deze gebruiken willekeurig gegenereerde Interface identifiers die periodiek worden vernieuwd voor uitgaande verbindingen, terwijl een stabiele identifier wordt behouden voor interne communicatie (zoals DNS of DHCPv6).


Net als bij DHCP in IPv4 kunnen automatisch toegewezen IPv6-adressen twee looptijden hebben, gedefinieerd door DHCPv6-routers of -servers:


- Voorkeurslevensduur*: na deze periode blijft de Address geldig, maar wordt niet meer gebruikt om nieuwe verbindingen te initiëren;
- Geldige levensduur*: wanneer deze tijd verstrijkt, wordt de Address volledig verwijderd uit de Interface-configuratie.


Dit systeem maakt het mogelijk om netwerkveranderingen dynamisch te beheren, bijvoorbeeld om een soepele overgang van de ene ISP naar de andere te garanderen. Door de door routers aangekondigde prefix bij te werken en tegelijkertijd DNS-records aan te passen, kan een IPv6-migratie worden uitgevoerd zonder merkbare onderbreking van de dienstverlening.


**Tip:** Het gecombineerde gebruik van Address en DNS levenscycli maakt het mogelijk om een geleidelijke overgangsstrategie te implementeren, waarbij nieuwe verbindingen overgaan naar een nieuwe topologie, terwijl bestaande verbindingen doorgaan tot hun natuurlijke einde.


Kortom, IPv6 biedt een breed scala aan flexibiliteit voor Address Assignment: handmatige configuratie, stateless of stateful auto-configuratie, DHCPv6 of random generatie. Elke aanpak heeft zijn eigen voordelen en beperkingen en kan worden aangepast aan het vereiste controleniveau, de grootte van het netwerk of privacybehoeften.


## IPv6 Address blokken toewijzen


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Address distributie


Het IPv6 Address toewijzingsschema is gestructureerd om aan twee doelen te voldoen: om wereldwijde Address uniciteit te garanderen en om een logische hiërarchie mogelijk te maken die de aggregatie en vereenvoudiging van routeringstabellen bevordert.

Net als bij IPv4 staat de *Internet Assigned Numbers Authority* (IANA) aan de top van deze hiërarchie. Deze beheert de wereldwijde unicast Address-ruimte en delegeert Address-blokken naar de vijf regionale internetregisters (_RIR_).


De vijf bestaande RIR's zijn:


- ARIN (Noord-Amerika),
- RIPE NCC (Europa, Midden-Oosten, Centraal-Azië),
- APNIC (Azië-Pacific),
- AFRINIC (Afrika),
- LACNIC (Latijns-Amerika en het Caribisch gebied).


IANA wijst IPv6-blokken van verschillende grootte toe aan elke RIR, over het algemeen tussen /23 en /12. Deze aanpak biedt flexibiliteit en zorgt tegelijkertijd voor schaalbaarheid op lange termijn. De RIR's herverdelen op hun beurt deze blokken onder Internet Service Providers (ISP's), grote bedrijven en openbare instellingen.


Sinds 2006 ontvangt elke RIR een IPv6 /12-blok van IANA, een vaste grootte die is ontworpen om een stabiele en voldoende grote reserve voor toekomstige groei te garanderen. RIR's verdelen deze gewoonlijk in /23-, /26- of /29-blokken. ISP's ontvangen meestal /32-blokken, hoewel deze grootte kan variëren afhankelijk van de grootte en het geografische gebied van de ISP. Meestal wijzen ze /48 blokken toe aan klanten. Elke /48 biedt 65.536 verschillende /64 subnetten (een enorme capaciteit vergeleken met IPv4).


**Belangrijke opmerking:** een /32 blok bevat precies 65.536 /48 subblokken. Dit betekent dat elke ISP tienduizenden klanten kan bedienen zonder zijn toewijzing uit te putten. Dankzij de /48 heeft elke klant dan een gigantische hoeveelheid ruimte om zijn eigen interne netwerk te structureren met zoveel /64 segmenten als hij wil.


De typische toewijzingshiërarchie ziet er als volgt uit:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Met deze overvloed aan adressen is NAT (*Network Address Translation*), ooit essentieel in IPv4 om Address tekorten op te vangen, niet langer nodig. Elke host kan een unieke, wereldwijd routeerbare publieke Address hebben, wat end-to-end connectiviteit vereenvoudigt en het gebruik van protocollen zoals IPSec, VoIP of inkomende verbindingen makkelijker maakt.


Om te controleren bij welke organisatie een IPv6 Address hoort, kun je het `whois` commando gebruiken om openbare RIR databases te bevragen. Deze transparantie maakt het mogelijk om de organisatie te identificeren die eigenaar is van een prefix, wat nuttig kan zijn voor netwerk-, analyse- of beveiligingsdoeleinden.


### PA vs PI adressering


Oorspronkelijk was het IPv6-toewijzingsmodel alleen gebaseerd op PA-blokken (*Provider Aggregatable*), wat betekent gekoppeld aan de ISP. In dit model ontvangt een organisatie haar prefix van haar ISP, wat betekent dat bij het veranderen van provider de hele infrastructuur opnieuw genummerd moet worden.


Hoewel de autoconfiguratiefuncties van IPv6 en de levensduur van Address het hernummeren eenvoudiger maken, blijft het lastig voor organisaties met kritieke infrastructuur of meerdere providerverbindingen voor redundantievereisten.


Sinds 2009 maakt het toewijzingsbeleid PI-blokken (*Provider Independent*) mogelijk. Deze blokken (meestal /48 groot) worden door een RIR rechtstreeks toegewezen aan een bedrijf of instelling, onafhankelijk van een ISP. Dit model is met name geschikt voor organisaties die aan *multihoming* doen (d.w.z. tegelijkertijd met meerdere operators verbonden zijn). In Europa bijvoorbeeld beschrijft RIPE-512 het beleid voor PI-toewijzingen.


### Subnetmasker notatie


Net als in IPv4 gebruikt IPv6 CIDR (*Classless Inter-Domain Routing*). Dit bestaat uit het aangeven van het aantal bits waaruit het voorvoegsel bestaat na de Address, met behulp van het `/` teken.


Neem het volgende voorbeeld:


```
2001:db8:1:1a0::/59
```


Dit betekent dat de eerste 59 bits vast zijn en het netwerk identificeren. Alle overige bits (hier 69 bits) kunnen gebruikt worden om subnetten of hosts te identificeren.


Deze notatie heeft dus betrekking op adressen van `2001:db8:1:1a0:0:0:0:0` tot `2001:db8:1:1bf:ffff:ffff:ffff`.


Dit blok omvat dus een set van 8 /64 subnetten, die elk een enorm aantal apparaten kunnen hosten.


CIDR notatie maakt precieze Address ruimteplanning mogelijk, van grootschalige netwerken tot thuisopstellingen en gevirtualiseerde omgevingen, en moedigt route aggregatie aan, waardoor de belasting van routers vermindert en de schaalbaarheid verbetert.


### IPv6-pakketten en headers


Het IPv6 pakketformaat verschilt van IPv4 doordat het zowel eenvoudiger als uitbreidbaar is. Een IPv6 datagram begint altijd met een header van vaste grootte van 40 bytes die alle essentiële routeringsinformatie bevat. Deze gestroomlijnde aanpak, vergeleken met de variabele lengte van de header van IPv4 (van 20 tot 60 bytes), maakt snellere en efficiëntere pakketverwerking door routers mogelijk.


IPv6 verwijdert echter geen functionaliteit: in plaats van het integreren van talloze optionele velden in de hoofdheader, introduceert het een systeem van extensieheaders die direct na de basisheader worden geplaatst. Deze optionele headers maken het mogelijk om gegevens of instructies toe te voegen die specifiek zijn voor bepaalde functies, zonder gewone pakketten onnodig te belasten.


Sommige extensieheaders volgen een vaste structuur, terwijl andere een variabel aantal opties kunnen bevatten. Deze opties zijn gecodeerd als `{Type, Lengte, Waarde}` triplets:


- Het veld "Type" (1 byte) geeft de aard van de optie aan;
- De eerste twee bits van het "Type" specificeren wat routers moeten doen als de optie niet wordt herkend:
 - Negeer de optie en ga door met de behandeling,
 - Laat het datagram vallen,
 - Drop en stuur een ICMP-fout naar de bron.
 - Het datagram zonder kennisgeving laten vallen (in het geval van multicastpakketten).
- Het veld "Length" (1 byte) bepaalt de grootte van het veld "Value", van 0 tot 255 bytes;
- Het veld "Waarde" bevat de gegevens die bij de optie horen.


Hier volgt een overzicht van de verschillende typen extensieheaders die door IPv6 worden gedefinieerd.


#### Hop-per-Hop kop


Deze header wordt, indien aanwezig, altijd direct na de basis header geplaatst. Het bevat informatie die verwerkt moet worden door elke router langs het pad van het pakket, in tegenstelling tot de meeste andere headers, die meestal alleen verwerkt worden door het bestemmingsknooppunt. Typisch gebruik is het signaleren van globale parameters of het aanvragen van specifieke verwerkingsstappen terwijl het pakket door het netwerk reist.


![Image](assets/fr/047.webp)


#### Routing kop


De routing header specificeert een lijst van tussenliggende adressen waar het pakket langs moet. Er zijn twee belangrijke routeringsmodi:


- Strikte routering: het exacte pad is vooraf gedefinieerd
- Losse routering: alleen bepaalde verplichte stappen worden gespecificeerd.


De eerste vier velden van deze rooting header zijn:


- Volgende koptekst**: identificeert het type van de volgende koptekst;
- Routing Type**: definieert de routeringsmethode (meestal `0`);
- Segmenten over**: aantal segmenten dat nog moet worden doorlopen ;
- Address[n]**: lijst van tussenliggende adressen.


Het veld "Segments Left" begint met het totale aantal resterende segmenten en wordt bij elke hop met één verlaagd.


![Image](assets/fr/048.webp)


#### Fragmentatie kop


In IPv6 mag alleen de bronhost een datagram fragmenteren, in tegenstelling tot IPv4 waar routers dit ook konden doen. Alle IPv6 knooppunten moeten pakketten van tenminste 1280 bytes kunnen verwerken. Als een router een pakket tegenkomt dat groter is dan de MTU van de volgende verbinding, stuurt hij een *ICMPv6 Packet Too Big* bericht terug naar de bron, die vervolgens de grootte van zijn transmissies aanpast.


De fragmentatieheader bevat de volgende velden:


- Identification**: unieke datagramidentifier voor hermontage.
- Fragment Offset**: de positie van het fragment binnen het originele datagram.
- M flag**: geeft aan of er meer fragmenten volgen.


![Image](assets/fr/049.webp)


#### Kop authenticatie (AH)


Deze header is ontworpen om communicatie te beveiligen door zowel de authenticiteit van de afzender als de integriteit van de gegevens te verifiëren. Het wordt vaak gebruikt met het IPsec protocol. Met behulp van een authenticatiecode kan de ontvanger bevestigen dat het bericht echt afkomstig is van de verwachte afzender en dat het niet is gewijzigd tijdens het transport.


In het geval van een frauduleuze wijzigingspoging, zal de authenticatiecode niet langer overeenkomen en kan het datagram worden geweigerd. Dit mechanisme beschermt ook tegen replay-aanvallen door onbevoegde duplicaties te detecteren.


![Image](assets/fr/050.webp)


#### Bestemmingsopties koptekst


Deze header is alleen bedoeld voor de uiteindelijke ontvanger van het datagram. Hij kan worden gebruikt om opties of metadata toe te voegen die specifiek zijn voor de toepassing, zonder dat tussenliggende routers er rekening mee houden.


Aanvankelijk was een dergelijke optie niet gedefinieerd in het protocol. Deze header werd echter geïntroduceerd toen IPv6 werd ontworpen, zodat toekomstige uitbreidingen konden worden toegevoegd zonder de algehele pakketstructuur te wijzigen. De null optie wordt bijvoorbeeld alleen gebruikt om de header op te vullen tot een veelvoud van 8 bytes ten behoeve van geheugenuitlijning.


![Image](assets/fr/051.webp)


Het ontwerp van IPv6 pakketten is gebaseerd op een duidelijke scheiding tussen een minimale basiskop en modulaire uitbreidingskoppen. Deze architectuur garandeert zowel standaard verwerkingsprestaties als de flexibiliteit die nodig is om het protocol te ontwikkelen en beveiliging, complexe routering of quality-of-service-mechanismen te integreren, terwijl de compatibiliteit met toekomstige infrastructuren behouden blijft.


## Relatie tussen IPv6 en DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


In moderne netwerken vertaalt het DNS (*Domain Name System*) domeinnamen naar IP-adressen die machines kunnen gebruiken. Met de introductie van IPv6 moest DNS zich aanpassen om 128-bits adressen te ondersteunen en tegelijkertijd achterwaartse compatibiliteit met IPv4 te behouden. Deze coëxistentie is vooral belangrijk in dual-stack omgevingen, waar beide IP-versies tegelijkertijd werken.


### IPv6-specifieke DNS-records


Om een domeinnaam aan een IPv6 Address te koppelen, gebruikt DNS een AAAA (*quad-A*) record, analoog aan het "A" record voor IPv4 adressen. Het AAAA-record koppelt een domeinnaam expliciet aan een IPv6 Address.

Voorbeeld:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Dit record geeft aan dat het domein `ipv6.mydmn.org` doorverwijst naar de IPv6 Address `2001:66c:2a8:22::c100:68b`. Het is mogelijk, en zelfs aanbevolen voor maximale compatibiliteit, om dezelfde domeinnaam aan verschillende IP-adressen te koppelen, zowel IPv4 (via een A-record) als IPv6 (via een AAAA-record). Hierdoor kunnen IPv6-compatibele klanten de voorkeur geven aan IPv6, terwijl IPv4-only klanten ondersteund blijven.


Daarnaast ondersteunt DNS omgekeerde resolutie, wat betekent dat het de domeinnaam kan opzoeken die bij een gegeven IP Address hoort. In het geval van IPv6 maakt deze operatie gebruik van PTR records die in de `ip6.arpa` zone staan. Deze zone is speciaal gereserveerd voor omgekeerde IPv6-omzetting. Voor IPv4 is het de `in-addr.arpa` zone.


### Omgekeerde resolutie


Omgekeerde resolutie van een IPv6 Address volgt een strikt proces:

1) Zet de Address uit in volledige hexadecimale notatie (16 bytes, d.w.z. 32 hexadecimale cijfers).

Voorbeeld:


```shell
2001:66c:2a8:22::c100:68b
```


Wordt:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Draai de volgorde van elk hexadecimaal cijfer (nibble) om, scheid ze met punten en voeg `ip6.arpa` toe:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Deze structuur zorgt voor gestandaardiseerde, unieke reverse lookups in de IPv6 Address ruimte.


**Let op**: DNS-query's kunnen over IPv4 of IPv6 worden verzonden. Het gebruikte transportprotocol heeft geen invloed op het type records dat wordt geretourneerd.

Bijvoorbeeld:


- Een client die via IPv6 verbonden is, kan een IPv4-record aanvragen.
- Een client die via IPv4 verbonden is, kan een IPv6-record aanvragen.

De DNS-server antwoordt simpelweg met de records die hij heeft, ongeacht het transportprotocol van de query.


Wanneer een hostnaam is toegewezen aan zowel IPv4 als IPv6, wordt de keuze van welke Address te gebruiken bepaald door RFC 6724, die een Address selectiealgoritme definieert gebaseerd op factoren zoals prefixvoorkeur, bereik en bereikbaarheid. Standaard wordt over het algemeen de voorkeur gegeven aan IPv6, tenzij dit overschreven wordt door systeem- of netwerkconfiguratie.


**Belangrijke herinnering**: wanneer je een IPv6 Address in een URL (*Uniform Resource Locator*) insluit, moet deze tussen vierkante haakjes (`[]`) staan. Dit voorkomt verwarring tussen de dubbele punt (`:`) in de IPv6 Address en de dubbele punt die de hostnaam scheidt van de poort in de URL.


Geldig voorbeeld:


```shell
http://[2001:db8::1]:8080
```


Dit zorgt ervoor dat de URL correct wordt verwerkt door zowel browsers als webservers.


De integratie van IPv6 in het DNS-systeem vereist daarom nieuwe recordtypes, een strikte methode voor omgekeerde resolutie en nauwkeurige selectie- en opmaakregels om routeringscompatibiliteit en -consistentie te garanderen.


### Deel samenvatting


In dit hoofdstuk hebben we de fundamentele principes van IPv6-adressering onderzocht. We begonnen met het onderzoeken van de structuur van IPv6 Address: de 128-bits lengte, hexadecimale notatie en de vereenvoudigingsregels die worden gebruikt om herhalende reeksen nullen in te korten. Dankzij dit ontwerp kan IPv6 de beperkingen van de Address-ruimte van IPv4 overwinnen en tegelijkertijd schaalbaarheid en een efficiënte hiërarchie garanderen.


Daarna hebben we gekeken naar de verschillende categorieën IPv6-adressen: unicast, anycast en multicast, waarbij we hun bereik, typische gebruik en representatie in de Address-ruimte hebben beschreven.


Vervolgens hebben we de methoden bekeken voor het toewijzen van IPv6-adressen binnen een lokaal netwerk, hetzij door handmatige configuratie, via het DHCPv6-protocol of met behulp van stateless autoconfiguration-mechanismen zoals die worden aangeboden door NDP. Deze benaderingen stellen apparaten in staat om automatisch generate hun eigen Address te maken uit de opgegeven prefix en hun MAC Address (via EUI-64), terwijl ze flexibiliteit bieden in termen van levensduurbeheer en privacy.


We hebben ook gedetailleerd beschreven hoe Address blokken worden toegewezen, te beginnen bij IANA, die ze distribueert naar de vijf RIR's (*Registered Internet Regions*), en vervolgens naar de ISP's, die ze opnieuw distribueren naar hun klanten als subnetten (vaak in /48, waardoor 65536 /64 subnetwerken mogelijk zijn). Het onderscheid tussen _Provider Aggregatable_ (PA) en _Provider Independent_ (PI) blokken helpt bij het beheren van _multihoming_ of provider-wijzigingsscenario's.


We hebben gezien dat DNS zich heeft aangepast aan IPv6 met de introductie van het AAAA-record en dat omgekeerde omzettingsmechanismen nu vertrouwen op de `ip6.arpa`-zone. Belangrijk is dat DNS onafhankelijk blijft van het gebruikte transportprotocol (IPv4 of IPv6), waardoor naadloze interoperabiliteit in een dual-stack omgeving wordt gegarandeerd.


IPv6 is daarom niet slechts een incrementele verbetering ten opzichte van IPv4, maar een compleet herontwerp van het adresseringssysteem, gebouwd om zowel de huidige als de toekomstige uitdagingen van het wereldwijde internet aan te kunnen.


In het laatste deel van deze NET 302 cursus gaan we de praktijk in en richten we ons op hulpmiddelen voor netwerkdiagnose.



# Diagnostische netwerkprogramma's


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Netwerktoegang Layer tools


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


In dit eerste hoofdstuk van het laatste deel over netwerkdiagnostiek richten we ons op hulpmiddelen voor het analyseren van de netwerktoegang Layer van het TCP/IP model. Deze Layer is verantwoordelijk voor directe communicatie tussen apparaten op hetzelfde fysieke netwerk, met name door het gebruik van MAC adressen en fysieke netwerk interfaces zoals Ethernet kaarten of Wi-Fi interfaces.


Het doel hier is om beheerders te voorzien van praktische hulpmiddelen om deze essentiële Layer van low-level connectiviteit te inspecteren, testen en optimaliseren. Deze gereedschappen kunnen worden gebruikt om de juiste werking van interfaces te controleren, problemen met de configuratie van netwerkkaarten op te lossen of anomalieën zoals botsingen, pakketverlies of verbindingsfouten te detecteren.


### IP/MAC-buurthulpprogramma's


#### gereedschap `Arp`


Een van de oudste diagnostische gereedschappen in de Network Access Layer is het `arp` commando. Hoewel het steeds meer vervangen wordt door moderne alternatieven zoals `ip neigh` (die we binnenkort zullen ontdekken). is `Arp` nog steeds aanwezig op veel systemen om de ARP (*Address Resolution Protocol*) cache te bekijken of te manipuleren. Deze cache slaat de toewijzingen op tussen IP adressen en MAC adressen die lokaal bekend zijn op een machine. Met andere woorden, je kunt hiermee bepalen welke fysieke (MAC) Address overeenkomt met een gegeven IP Address op het lokale netwerk.


In de praktijk, wanneer een host een pakket naar een IP Address binnen hetzelfde subnet wil sturen, moet hij eerst de MAC Address van de doelmachine kennen. Deze toewijzing wordt afgehandeld door ARP, dat een verzoek uitzendt op het lokale netwerk en een antwoord ontvangt met de overeenkomstige MAC Address. Dit resultaat wordt dan tijdelijk opgeslagen in een lokale tabel genaamd de MAC Address. Dit resultaat wordt dan tijdelijk opgeslagen in een lokale tabel die de "ARP cache" wordt genoemd, om te voorkomen dat de verzoeken voor elk nieuw pakket worden herhaald.


Gebruik om de inhoud van deze cache te bekijken en de items te controleren die momenteel bekend zijn op de machine:


```bash
arp -a
```


Dit commando geeft een lijst van alle lokaal geregistreerde IP/MAC mappings, over alle interfaces. Elke regel geeft de hostnaam (indien oplosbaar), de IP Address, de overeenkomstige MAC Address en de Interface waar de toewijzing is waargenomen.


Om de weergave te filteren op een specifieke IP Address, geef je deze gewoon op:


```bash
arp -a 192.168.1.5
```


Dit maakt het makkelijk om te controleren of een bepaalde IP Address aanwezig is in de cache, wat kan helpen bij het diagnosticeren van communicatiestoringen tussen twee hosts op hetzelfde netwerk.


Om alleen de ARP entries te tonen die geassocieerd zijn met een specifiek netwerk Interface (bijvoorbeeld een Ethernet kaart met de naam `eth0`), kun je het volgende gebruiken:


```bash
arp -a -i eth0
```


Dit is vooral handig in multi-Interface omgevingen (bekabeld, draadloos, VPN, etc.), waar één host meerdere netwerkadapters kan hebben.


Het `arp` commando is niet beperkt tot alleen-lezen. Het kan ook gebruikt worden om de ARP-cache handmatig te bewerken, een functie van onschatbare waarde in bepaalde geavanceerde scenario's voor probleemoplossing of bij het simuleren van specifieke condities. Je kunt bijvoorbeeld handmatig een IP/MAC toewijzing toevoegen:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Dit commando maakt een statische entry aan in de lokale ARP-tabel, waarbij het IP Address `192.168.1.7` geassocieerd wordt met het MAC Address `00:17:BC:56:4F:25` op de Interface `eth2`. Als er geen Interface wordt opgegeven, gebruikt het systeem automatisch de eerste toepasselijke.


Je kunt ook een entry uit de ARP-cache verwijderen om een fout te corrigeren of om een herontdekking te forceren:


```bash
arp -d 192.168.1.7
```


Dit verwijdert de entry en zorgt ervoor dat de volgende communicatiepoging een nieuw ARP-verzoek uitlokt.


**OPMERKING**: De delete optie accepteert ook een Interface naam, zodat je gerichter een specifiek item kunt verwijderen.


Samengevat biedt het `arp` gereedschap diagnostiek op laag niveau, vooral nuttig in lokale netwerken waar connectiviteitsproblemen vaak terug te voeren zijn op onjuiste of verouderde Address resoluties. Echter, op recente systemen, in het bijzonder met moderne Linux distributies, wordt dit gereedschap in toenemende mate vervangen door het `ip neigh` commando, uit de `iproute2` toolset, dat vergelijkbare functionaliteit biedt in een meer verenigd raamwerk.


#### `Ip buren` gereedschap


Op moderne systemen, met name recente Linux distributies, is het `ip neigh` commando het gereedschap bij uitstek voor het inspecteren en beheren van mappings tussen IP en MAC adressen. Dit commando is onderdeel van de `iproute2` suite, die geleidelijk oudere gereedschappen zoals `arp` vervangt en een meer consistent en flexibel raamwerk biedt voor diagnostiek op de data link Layer.


Het `ip neigh` commando bevraagt de lokale IP neighbor cache, die equivalent is aan de ARP cache voor IPv4 en de NDP (_Neighbor Discovery Protocol_) cache voor IPv6. Deze cache slaat bekende associaties op tussen IP adressen (v4 of v6) en MAC adressen, samen met hun status (geldig, in afwachting, verlopen...).


Het basiscommando om de cache weer te geven is:


```bash
ip neigh
```


Dit geeft een lijst met entry's, met het bestemmings IP Address, het relevante netwerk Interface, de geassocieerde MAC Address (indien beschikbaar), en de status van de entry (bijv. `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).


Voorbeelduitvoer:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Deze regel geeft aan dat de machine een geldige mapping kent tussen IP Address `192.168.1.5` en MAC Address `00:17:BC:56:4F:25` via Interface `eth0`.


Je kunt invoer ook filteren op criteria zoals IP Address, Interface of status. Bijvoorbeeld, om alleen Address `192.168.1.7` op te vragen:


```bash
ip neigh show 192.168.1.7
```


Of om alle ingangen voor Interface `eth1` weer te geven:


```bash
ip neigh show dev eth1
```


Naast raadplegen kan `ip neigh` ook gebruikt worden om de cache handmatig aan te passen. Bijvoorbeeld om een statisch item toe te voegen:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Dit associeert permanent het IP Address `192.168.1.7` met de gespecificeerde MAC Address op Interface `eth1`. De `nud permanent` optie (voor _Neighbor Unreachability Detection_) zorgt ervoor dat de vermelding niet automatisch ongeldig wordt gemaakt.


Omgekeerd, om een cache-item te verwijderen:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Dit dwingt het systeem om de mapping opnieuw op te lossen de volgende keer dat het communiceert met die Address.


**OPMERKING**: Het hulpprogramma `ip neigh` werkt zowel voor IPv4 als IPv6. Voor IPv4 werkt het samen met ARP; voor IPv6 werkt het samen met NDP. Dit biedt een verenigde, consistente aanpak voor het beheren van IP/MAC relaties tussen protocol families, waardoor `ip neigh` de moderne standaard is voor burenbeheer op Linux systemen.


### Hulpmiddelen voor pakketanalyse


Om grondig te analyseren wat er op een computernetwerk gebeurt, hebben beheerders gereedschappen nodig die de pakketten kunnen vastleggen die tussen machines worden uitgewisseld. Twee hulpprogramma's springen eruit als benchmarks: `tcpdump` en `Wireshark`. Deze gereedschappen zijn essentieel voor het diagnosticeren van abnormaal gedrag, het controleren van protocoluitwisselingen of het bestuderen van netwerkbeveiliging door het inspecteren van de inhoud van frames.


#### `ttcpdump`: commandoregelanalyse


`tcpdump` is een zeer krachtig commandoregel-hulpprogramma, ontworpen om pakketten vast te leggen en weer te geven die door een netwerk Interface gaan. Het werkt in realtime en dankzij het lichtgewicht ontwerp kan het gebruikt worden op systemen zonder grafische Interface of met beperkte middelen. Het vertrouwt op de `libpcap` bibliotheek, die hardware-onafhankelijke low-level capture functies biedt.


Een veelgebruikt gebruik van `tcpdump` is het monitoren van de netwerkactiviteit van een machine of netwerksegment, waarbij pakketten gefilterd worden op basis van specifieke criteria. De resultaten kunnen worden omgeleid naar een bestand, zodat het verkeer kan worden gearchiveerd voor latere analyse of opnieuw kan worden afgespeeld in een ander programma, zoals Wireshark.


De algemene opdrachtsyntaxis is:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` schrijft gevangen pakketten naar een bestand in `libpcap` formaat (extensie `.cap` of `.pcap`);
- `-i` specificeert het netwerk Interface om in de gaten te houden (bijvoorbeeld `eth0`, `wlan0`);
- `-s` stelt de maximale hoeveelheid vastgelegde gegevens per pakket in. Met `0` worden alle pakketten vastgelegd;
- `-n` schakelt DNS- en servicenaamomzetting uit, wat de prestaties verbetert.


Met expressiefilters aan het einde van het commando kun je captures beperken tot een subset van verkeer. Je kunt de trefwoorden `host`, `port`, `src`, `dst`, etc. combineren om de selectie te verfijnen.


Voorbeeld: HTTP pakketten (poort 80) van of naar de `192.168.25.24` server vastleggen en opslaan in een `fichier.cap` bestand:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Het resulterende bestand kan later worden geanalyseerd in een grafisch hulpmiddel of opnieuw worden afgespeeld op een ander systeem.


#### Wireshark: geavanceerde visuele analyse


Wireshark, voorheen bekend als *Ethereal*, is een compleet netwerkanalyseprogramma met een grafische Interface. In tegenstelling tot `tcpdump`, biedt het een gestructureerde, gedetailleerde visualisatie van pakketten, inclusief protocol ontleding, stroomgrafieken, verkeersstatistieken en interactieve filters. Het maakt ook gebruik van `libpcap`, wat betekent dat het capture bestanden gegenereerd door `tcpdump` kan openen en verwerken.


Wireshark is beschikbaar op veel besturingssystemen, waaronder Linux en Windows. Om het te installeren heb je beheerdersrechten nodig om toegang te krijgen tot de capture interfaces. Eenmaal gestart, kun je een netwerk Interface selecteren uit het *Capture* menu. Als je op *Start* klikt, begint de real-time pakketopname. Het scherm is verdeeld in drie vensters:


- de lijst met vastgelegde frames ;
- protocol gedecodeerde details,
- ruwe hexadecimale gegevens.



![Image](assets/fr/052.webp)



Wireshark blinkt uit in scenario's waar je complex protocolgedrag moet observeren, applicatiedialogen moet reconstrueren (zoals een HTTP- of DNS-sessie) of de responstijden van services moet bestuderen. Het ondersteunt ook zeer specifieke weergavefilters door gebruik te maken van de speciale syntaxis (anders dan die van `tcpdump`) om alleen op relevante pakketten te focussen.


#### Aanvullende hulpmiddelen


Het is belangrijk om op te merken dat `tcpdump` en Wireshark niet uitwisselbaar zijn: ze hebben elk hun eigen sterke punten. `tcpdump` is beter geschikt voor commandoregelomgevingen, geautomatiseerde scripts en serverinterventies op afstand, terwijl Wireshark ideaal is voor gedetailleerde, interactieve en educatieve verkeersanalyse.


De twee tools kunnen gecombineerd worden: een capture kan gemaakt worden op een remote systeem met `tcpdump`, vervolgens wordt het `.cap` bestand overgezet voor analyse met Wireshark op een lokale machine. Deze aanpak wordt in de praktijk veel gebruikt.


### Interface analyse-instrumenten


Op de Network Access Layer is het vaak nodig om fysieke netwerkinterfaces te ondervragen en te configureren om storingen te diagnosticeren, de prestaties te optimaliseren of de integriteit van de verbinding te controleren. Een van de krachtigste gereedschappen die onder Linux voor dit doel beschikbaar is, is `ethtool`, een commandoregelhulpprogramma dat niet alleen gedetailleerde technische informatie geeft over een Ethernet Interface, maar waarmee je ook enkele parameters in realtime kunt aanpassen.


#### Bekijk de Interface specificaties


Een kernfunctie van `ethtool` is de mogelijkheid om een Interface te bevragen en de huidige karakteristieken weer te geven. Hierdoor kun je controleren:


- verbindingssnelheid (bijv. 100 Mbit/s, 1 Gbit/s of 10 Gbit/s) ;
- onderhandelingsmodus (half- of full-duplex) ;
- of autonegotiatie is ingeschakeld;
- het type poort (koper, glasvezel, enz.) ;
- linkstatus (actief of niet) ;
- ondersteuning voor geavanceerde functies zoals *Wake-on-LAN*.


Deze informatie is vooral nuttig voor het diagnosticeren van problemen gerelateerd aan fysieke connectiviteit of onjuiste onderhandelingsinstellingen tussen de netwerkkaart van de host en de apparatuur waarmee deze verbinding maakt (switch, router, etc.).


Om deze informatie te verkrijgen, voert u simpelweg:


```bash
ethtool enp0s3
```


Dit commando geeft een gedetailleerd rapport over de `enp0s3` Interface, een gebruikelijke naamgevingsconventie op CentOS of RHEL gebaseerde systemen.



![Image](assets/fr/053.webp)



#### Interface parameters dynamisch wijzigen


`ethtool` is niet beperkt tot observatie: het staat je ook toe om bepaalde Interface parameters aan te passen zonder de machine te herstarten. Dit maakt het bijvoorbeeld mogelijk om een specifieke verbindingssnelheid te forceren of functies in te schakelen, afhankelijk van de behoeften van het lokale netwerk.


De `-s` optie wordt gebruikt om dynamisch parameters te configureren zoals:


- verbindingssnelheid (`speed`), expliciet ingesteld (bijv. 1000 voor 1 Gbit/s) ;
- duplexmodus (`duplex`), ofwel `half` of `full` ;
- autonegotiatie in- of uitschakelen (`autoneg`) ;
- inschakelen van *Wake-on-LAN* (`wol`) ;
- poorttype.


Voorbeeld 1: autonegotiation inschakelen op een Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Voorbeeld 2: schakel de functie *Wake-on-LAN* in (om de machine op afstand te laten ontwaken via een magisch pakket):


```bash
ethtool -s enp0s3 wol p
```


In dit voorbeeld geeft de `p` optie aan dat wake-up zal plaatsvinden zodra een *Wake-on-LAN* pakket wordt gedetecteerd. Deze instelling wordt vaak gebruikt in bedrijfsomgevingen om 's nachts updates of onderhoud op afstand uit te voeren.


#### Installatie gereedschap


Het is belangrijk om op te merken dat `ethtool` niet altijd standaard wordt geïnstalleerd. Op Red Hat/CentOS distributies kan het geïnstalleerd worden met het commando:


```bash
yum install -y ethtool
```


Op Debian en Ubuntu is het gelijkwaardige commando:


```bash
sudo apt install ethtool
```


**WAARSCHUWING**: In alle `ethtool` commando's moet de naam van het netwerk Interface direct na de optie gespecificeerd worden (als `-s`). Elke syntaxfout in de plaatsing van de parameters maakt het commando ongeldig of ineffectief.



## Netwerk Layer gereedschap


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Tools voor verkeersanalyse


In netwerkdiagnostiek blijft het `ping` commando een van de eenvoudigste maar krachtigste gereedschappen om de connectiviteit tussen twee machines te testen. Het controleert of een host op afstand bereikbaar is op een bepaald tijdstip, terwijl het ook informatie geeft over latentie, linkstabiliteit en DNS-resolutie.


Het `ping` commando maakt gebruik van het ICMP (*Internet Control Message Protocol*) protocol. Wanneer een gebruiker een `ping` verzoek stuurt, stuurt het systeem een ICMP "Echo Request" pakket naar een IP Address of hostnaam. Als de doelmachine online is en het netwerkpad geldig is, antwoordt het met een ICMP "Echo Reply" pakket. Dit eenvoudige mechanisme kan gebruikt worden om latency te meten en problemen met connectiviteit of naamresolutie op te sporen.


Voorbeeld van een klassiek commando:


```bash
ping 172.17.18.19
```


Typisch antwoord:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


In dit voorbeeld is de naamresolutie automatisch uitgevoerd: het domein `mydmn.org` is geassocieerd met het IP Address `172.17.18.19`, wat bevestigt dat DNS-resolutie correct werkt. Het commando geeft ook technische details zoals:


- iCMP volgnummer (`icmp_seq`), handig om de volgorde van antwoorden te controleren;
- TTL (*Time-To-Live*), die het aantal resterende hops aangeeft voordat het pakket wordt weggegooid;
- rondetijd/vertraging (`time`), uitgedrukt in milliseconden, die een schatting geeft van de linklatentie.


#### Meer gedetailleerde analyse van ICMP-parameters


De TTL is een belangrijk veld in het IP-protocol. Elk datagram wordt geïnitialiseerd met een TTL waarde door de verzender (vaak 64, 128 of 255). Elke router langs het pad verlaagt deze waarde met 1. Als de TTL 0 bereikt voordat het zijn bestemming bereikt, wordt het pakket weggegooid en wordt er een ICMP fout teruggestuurd naar de verzender. Dit mechanisme voorkomt oneindige routeringslussen.


De propagatietijd (*round-trip delay/time*) meet de vertraging voor een pakket om de verzender te verlaten, het doel te bereiken en terug te keren. In de praktijk wordt een vertraging van minder dan 200 ms als acceptabel beschouwd voor een stabiele verbinding. Abnormaal hoge vertragingen kunnen duiden op netwerkcongestie, inefficiënte routering of slechte kwaliteit van de verbinding.


#### Geavanceerd `ping` gebruik


`ping` biedt opties om tests te verfijnen en specifiek netwerkgedrag te observeren.


Om broadcastverzoeken te sturen, kun je de `-b` optie gebruiken om alle hosts op een subnet aan te spreken:

```bash
ping -b 192.168.1.255
```


Dit is handig op lokale netwerken om snel actieve hosts te detecteren of om te testen hoe het netwerk omgaat met broadcast verzoeken. In veel opstellingen blokkeren routers en firewalls echter broadcast pings om versterkingsaanvallen te voorkomen.


Je kunt ook een aangepast interval tussen verzoeken opgeven met de `-i` optie (standaard: 1 seconde):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Dit stuurt 10 ICMP verzoeken met een interval van 0,2 seconden. Dergelijke testen zijn nuttig om latentiefluctuaties over een korte periode te detecteren of om een link licht te belasten om de stabiliteit ervan te evalueren.


### Analysehulpmiddelen voor routeringstabellen


Het `ip route` commando, onderdeel van de `iproute2` suite, is het aanbevolen en standaard gereedschap op moderne Linux systemen voor het inspecteren en beheren van de IP routeringstabel van de kernel. Het vervangt het verouderde `route` commando en biedt een duidelijkere syntax, meer consistentie en uitgebreide ondersteuning voor moderne mogelijkheden (IPv6, meerdere tabellen, namespaces, etc.).


#### De routeringstabel weergeven


Om de huidige routeringstabel weer te geven:


```bash
ip route show
```


Deze uitvoer toont alle routes die bekend zijn bij de kernel, dat wil zeggen, de paden die uitgaande pakketten nemen afhankelijk van hun bestemming.


Voorbeelduitvoer:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Elke lijn stelt een route voor. De belangrijkste velden zijn:


- default**: de standaardroute, gebruikt als er geen meer specifieke route overeenkomt.
- via**: de gateway die gebruikt wordt om de bestemming te bereiken.
- dev**: het gebruikte netwerk Interface.
- proto**: hoe de route is aangemaakt (handmatig, DHCP, kernel, etc.).
- metric**: routekosten, gebruikt om prioriteit te geven aan meerdere mogelijke paden.
- scope**: routebereik (bv. `link` voor een rechtstreeks verbonden route).
- src**: de bron-IP Address die gebruikt wordt voor uitgaande pakketten op deze Interface.


#### Routes toevoegen en verwijderen


Je kunt de routeringstabel ook dynamisch wijzigen, bijvoorbeeld door statische routes toe te voegen of te verwijderen.


Een statische route toevoegen:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Dit configureert een route naar het `192.168.1.0/24` netwerk, via de `192.168.1.1` gateway op Interface `eth0`.


Verwijder deze route:


```bash
ip route del 192.168.1.0/24
```


Dit commando verwijdert de eerder gedefinieerde route.


#### Handige commando's


Hier zijn enkele nuttige varianten voor analyse of scripting:


- `ip -4 route`: geeft alleen IPv4-routes weer;
- `ip -6 route`: geeft alleen IPv6-routes weer;
- `ip route list table main`: geeft de hoofdroutingtabel weer (standaardwaarde) ;
- `ip route get <Address>`: laat zien welke Interface en gateway een pakket naar de gegeven Address zou gebruiken.


Voorbeeld:


```bash
ip route get 8.8.8.8
```


Dit toont de exacte route die een pakket zou nemen om `8.8.8.8` te bereiken.


### Traceergereedschappen


Een van de meest effectieve gereedschappen voor het analyseren van de route die IP pakketten afleggen tussen een bronhost en een doelbestemming is het `traceroute` commando. Het toont stap voor stap het pad dat pakketten volgen en identificeert de tussenliggende routers die ze passeren. In het geval van een storing in een netwerkverbinding of een dienstonderbreking, helpt `traceroute` om de precieze locatie van het probleem te bepalen.


Net als bij het `ping` commando, kan het doel gespecificeerd worden met zijn volledig gekwalificeerde domeinnaam (FQDN) of met zijn IP Address. Bijvoorbeeld:


```bash
traceroute mydmn.org
```


#### Werkingsprincipe


`traceroute` vertrouwt op het TTL (*Time To Live*) veld in de header van IP pakketten. Zoals eerder uitgelegd, is dit veld een teller die door elke router langs het pad wordt verlaagd. Als de TTL nul bereikt, wordt het pakket weggegooid en stuurt de router een ICMP "Time Exceeded" bericht terug naar de afzender. Dit mechanisme voorkomt oneindige lussen in het geval van verkeerde routering.


`traceroute` maakt gebruik van dit gedrag om de routers tussen verzender en ontvanger in kaart te brengen:


- Het stuurt eerst een serie UDP pakketten (meestal drie), met een TTL van 1. De eerste router komt een TTL van 0 tegen, dus hij gooit het pakket weg en antwoordt dan met een ICMP bericht, dat zijn IP Address en responstijd onthult.
- Vervolgens stuurt het nog een serie pakketten met een TTL van 2, waarmee de tweede router wordt onthuld.
- Het proces herhaalt zich totdat de bestemming bereikt is, waarna de host antwoordt met een ICMP Port Unreachable bericht, dat aangeeft dat het eindpunt bereikt is.


Standaard gebruikt `traceroute` UDP pakketten die naar ongebruikte poorten worden gestuurd (meestal beginnend bij 33434), maar kan ook worden geconfigureerd om ICMP (zoals `ping`) of zelfs TCP te gebruiken, afhankelijk van systemen of commandovarianten.


Voorbeelduitvoer:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Elke lijn komt overeen met een router die wordt doorkruist, met maximaal drie tijdmetingen (in milliseconden) die de latentie van de rondreis naar die router aangeven. Deze waarden helpen de prestaties van elk netwerksegment te beoordelen.


#### Resultaat interpretatie


Als een router niet reageert of ICMP-berichten filtert, worden sterretjes `*` weergegeven in plaats van de responstijd. Dit kan erop wijzen:


- een firewall die ICMP-antwoorden blokkeert,
- een apparaat dat is geconfigureerd om niet te reageren, of
- een tijdelijk verbindingsprobleem langs het pad.


Zo identificeert `traceroute` niet alleen de afgelegde route, maar laat het ook punten van abnormale latentie of onderbrekingen zien.


Op sommige systemen kan het equivalente `tracepath` commando gebruikt worden, waarvoor geen root rechten nodig zijn. Gebruik voor IPv6 `traceroute6` of `tracepath6`.


Voorbeeld voor IPv6 traceren:


```bash
traceroute6 ipv6.google.com
```


### Hulpmiddelen voor het controleren van actieve verbindingen


Om actieve netwerkverbindingen te diagnosticeren en netwerkactiviteit op een Linux systeem te monitoren, is het `ss` commando (kort voor _socket statistics_) het moderne referentiegereedschap. Het is onderdeel van de `iproute2` suite en vervangt het nu verdwenen `netstat` en biedt betere prestaties en nauwkeurigere resultaten.


`ss` toont actieve TCP en UDP verbindingen, luisterpoorten, lokale en remote adressen, verbindingsstatussen en geassocieerde processen.


#### Algemeen gebruik


Wanneer het zonder opties wordt uitgevoerd, toont het `ss` commando actieve TCP verbindingen. Basis syntaxis:


```bash
ss [options]
```


Enkele veelgebruikte opties voor het verfijnen van de analyse:


- `-t`: alleen TCP-verbindingen weergeven;
- `-u`: alleen UDP-verbindingen weergeven;
- `-l`: alleen luisterende sockets tonen;
- `-n`: naamomzetting uitschakelen (onbewerkte IP's en poortnummers) ;
- `-p`: elk socket geassocieerd proces weergeven (PID en programmanaam),
- `-a`: toont alle verbindingen, ook de inactieve,
- `-s`: toont socket-statistieken op hoog niveau.


#### Praktijkvoorbeelden


Om alle actieve verbindingen weer te geven die TCP poort 80 (HTTP) gebruiken:


```bash
ss -ant | grep ':80'
```


Dit toont actieve TCP-verbindingen op poort 80. Staten zoals `LISTEN`, `ESTABLISHED`, `TIME-WAIT` geven de huidige status van elke Exchange aan.


Voorbeelduitvoer:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Om alle netwerkverbindingen met bijbehorende processen weer te geven:


```bash
ss -tulnp
```


Om een algemeen overzicht van het socketgebruik te krijgen:

```bash
ss -s
```


Om alleen UDP-verbindingen te filteren:

```bash
ss -unp
```


Deze commando's zijn vooral handig voor het detecteren van verdachte verbindingen, onverwachte luisterpoorten of het monitoren van de activiteit van een specifieke dienst.


## Layer gereedschap transporteren en opbergen


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### DNS-zoekprogramma's


In de bovenste lagen van het TCP/IP-model, vooral bij de toepassing Layer, is het belangrijk om te begrijpen hoe naamresolutie werkt. Met DNS query tools kun je controleren of een domeinnaam correct is geassocieerd met een IP Address, en ook helpen bij het diagnosticeren van DNS server problemen zoals verkeerde configuratie, propagatie vertragingen of onbeschikbaarheid. Deze tools zijn essentieel voor elke netwerkbeheerder of gebruiker die meer wil weten over DNS-uitwisselingen in een IP-omgeving.


#### Het `nslookup` commando


Het eenvoudigste DNS-zoekprogramma is `nslookup`. Het stuurt een query naar een DNS server en retourneert het IP Address geassocieerd met een domeinnaam (of vice versa). Standaard bevraagt het de geconfigureerde DNS server van het systeem, maar je kunt ook een server direct in het commando opgeven.


Voorbeeld van een directe opzoeking:

```bash
nslookup mydmn.org
```


Een specifieke DNS-server opvragen:

```bash
nslookup mydmn.org 192.6.23.4
```


Het verzoek vraagt de DNS server op `192.6.23.4` om de naam `mydmn.org` om te zetten. Dit is vooral handig om te controleren of een bepaalde DNS-server een domeinnaam herkent of om te controleren of de server goed werkt.


#### Het `dig` commando


`dig` (*Domain Information Groper*) is een moderner, completer en flexibeler hulpmiddel dan `nslookup`. Het ondersteunt complexe queries en geeft gedetailleerde informatie over het resolutieproces, de hiërarchie van betrokken servers, het type record dat is teruggestuurd (A, AAAA, MX, TXT, etc.) en eventuele fouten die zijn opgetreden.


Voorbeeld van basisquery:

```bash
dig mydmn.org
```


Een specifieke DNS-server opvragen:

```bash
dig @192.6.23.4 mydmn.org
```


Dit commando controleert de beschikbaarheid van een DNS-record op een gegeven server.

Een van de belangrijkste voordelen van `dig` is dat het de details van het DNS antwoord laat zien, waardoor het erg handig is voor het diagnosticeren van configuratiefouten.


#### Handmatige configuratie van DNS-resolvers


Soms is het nodig om de DNS servers die lokaal gebruikt worden te overschrijven, bijvoorbeeld in testomgevingen of om het gebruik van specifieke servers te forceren. Dit kan gedaan worden door het `/etc/resolv.conf` bestand aan te passen, dat de DNS resolutie-instellingen van het systeem definieert.


Voorbeeldconfiguratie:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- In het veld `search` wordt een domein opgegeven dat automatisch wordt toegevoegd bij het oplossen van korte namen.
- De `nameserver` regels definiëren de DNS servers om te gebruiken, in volgorde van prioriteit.


Op veel moderne distributies (vooral degene die `systemd-resolved` gebruiken) zijn wijzigingen in `/etc/resolv.conf` tijdelijk en kunnen overschreven worden bij het opnieuw opstarten of opnieuw verbinden met het netwerk. Meer permanente methoden zijn het gebruik van `resolvconf`, `systemd-resolved`, of het wijzigen van *NetworkManager* configuraties.


#### Het `host` commando


Een ander eenvoudig maar effectief DNS-hulpmiddel is `host`. Het zet domeinnamen om in IP-adressen (of omgekeerd) en kan helpen bij het diagnosticeren van DNS-fouten of verkeerde configuraties op een netwerk Interface.


Voorbeelden:

```bash
host mydmn.org
```


Omgekeerd zoeken:

```bash
host 192.6.23.4
```


`host` is vooral handig voor snelle controles, vooral wanneer het gebruikt wordt in commandoregelscripts.


Herhaalde of intensieve query's naar DNS-servers van derden zonder toestemming kunnen worden geïnterpreteerd als pogingen tot inbraak of kwaadaardige activiteiten. Onjuist gebruikt, of tegen netwerken die je niet beheert, kunnen deze commando's lijken op verkenningsscans, die vaak een eerste stap in een aanval zijn. Beperk het gebruik ervan altijd tot omgevingen die je beheert of waar je expliciet toestemming voor hebt.


### Tools voor netwerkscanning


Bij het bewaken of beveiligen van een lokaal of wide area netwerk is het cruciaal om actieve apparaten en de diensten die ze aanbieden te identificeren. Dit is precies wat het hulpprogramma `nmap` (*Network Mapper*) doet.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Introductie van `nmap`


`nmap` maakt het mogelijk om gericht één of meerdere hosts te scannen om open poorten, beschikbare services (HTTP, SSH, DNS, etc.) en soms zelfs het type besturingssysteem dat in gebruik is te detecteren. Dankzij de vele opties geeft `nmap` een nauwkeurig overzicht van het blootstellingsoppervlak van een netwerk, wat essentieel is tijdens de audit of hardening fases van infrastructuurbeheer.


Net als het `host` commando, mag `nmap` nooit gebruikt worden op netwerken of infrastructuren waarvan je niet de eigenaar bent, of zonder expliciete autorisatie. Ongeautoriseerde poortscans kunnen gemarkeerd worden als kwaadaardige verkenningspogingen, worden vaak gedetecteerd door beveiligingssystemen (firewalls, IDS/IPS) en kunnen zelfs leiden tot juridische gevolgen.


#### Basisgebruik


Om een specifieke host te scannen en de open poorten te bekijken:

```bash
nmap 192.168.0.1
```


Dit commando scant de 1000 meest gebruikte poorten op host `192.168.0.1` en toont de gebruikte services en protocollen. Als DNS-resolutie is geconfigureerd, kun je ook de hostnaam gebruiken in plaats van het IP Address.


#### Volledige netwerkscan


Een van de voordelen van `nmap` is de mogelijkheid om een hele reeks adressen te scannen met een enkel commando. Dit maakt het bijvoorbeeld makkelijk om snel alle actieve machines op een netwerk te inventariseren:


```bash
nmap 192.168.0.0/24
```


In dit geval worden alle hosts in het bereik `192.168.0.0` tot `192.168.0.255` opgevraagd. Voor elke IP Address geven de resultaten de open poorten, hun status (open, gefilterd, enz.) en, indien mogelijk, de naam van de corresponderende dienst.



![Image](assets/fr/055.webp)



Een beheerder kan op `nmap` vertrouwen voor verschillende taken:


- Actieve hosts** detecteren: identificeren welke machines reageren binnen een subnet;
- Service-inventaris**: zorg ervoor dat alleen de benodigde poorten toegankelijk zijn (principe van de laagste privileges);
- Nalevingscontrole**: open poorten vergelijken met het beveiligingsbeleid van de organisatie;
- Preventie van kwetsbaarheden**: onveilige of verouderde services op kritieke machines opsporen.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Hulpmiddelen voor procesondervraging


Voor een diepgaande analyse van actieve processen en open bestanden, vooral in een netwerkcontext, gebruiken Linux beheerders vaak het `lsof` (*List Open Files*) commando. Ondanks de naam is `lsof` niet beperkt tot traditionele bestanden: op UNIX systemen wordt alles als een bestand beschouwd, inclusief netwerk sockets, apparaten en communicatiekanalen.


Deze tool geeft daarom een dwarsdoorsnede van het systeem door actieve processen, open netwerkpoorten, opgevraagde bestanden en de betrokken gebruikers te correleren.


#### Netwerkanalyse met `lsof`


De `-i` optie beperkt de uitvoer tot netwerkverbindingen (TCP, UDP, IPv4 of IPv6). Dit maakt het makkelijk om te zien welke processen over het netwerk communiceren:


```bash
lsof -i
```


Dit commando geeft een lijst van alle draaiende processen die een netwerksocket gebruiken, met de gebruikte poort, het protocol (TCP/UDP), de status van de verbinding en het PID en de bijbehorende gebruiker.


#### Filteren op IP Address of poort


Je kunt zoekopdrachten verfijnen door een IP Address en een poort op te geven, waardoor een bepaalde netwerkstroom wordt geïsoleerd. Bijvoorbeeld, om een SMTP sessie (poort 25) met een specifieke host te controleren:


```bash
lsof -n -i @192.168.2.1:25
```


Dit toont alleen actieve netwerkverbindingen met host `192.168.2.1` op poort 25, handig voor het diagnosticeren van verdachte activiteit of SMTP flow problemen.


#### Apparaattoegang traceren


Een ander sterk punt van `lsof` is het bijhouden van speciale bestanden zoals schijfpartities. Om bijvoorbeeld te controleren welke processen bestanden hebben geopend op `/dev/sda1`:


```bash
lsof /dev/sda1
```


Dit is handig wanneer een unmount poging mislukt omdat het apparaat nog in gebruik is, of bij het onderzoeken welke applicaties toegang hebben tot een partitie.


#### Kruisanalyse: proces en netwerk


Opties kunnen gecombineerd worden voor precieze inzichten. Bijvoorbeeld om alle netwerkpoorten te zien die geopend zijn door een proces met PID 1521:


```bash
lsof -i -a -p 1521
```


De `-a` optie snijdt criteria (`-i` en `-p`), waardoor de uitvoer wordt beperkt tot alleen netwerkverbindingen van dat proces.


#### Volgen voor meerdere gebruikers


`lsof` kan ook gebruikt worden om activiteit van specifieke gebruikers te analyseren, waarbij alle bestanden die ze hebben geopend worden getoond, optioneel gefilterd op PID:


```bash
lsof -p 1521 -u 500,phil
```


Dit toont de bestanden of netwerkverbindingen die gebruikt worden door gebruiker `phil` of UID 500, beperkt tot proces 1521.


### Sectie Samenvatting


In dit laatste deel hebben we een groot aantal onmisbare hulpmiddelen voor het diagnosticeren, analyseren en beheren van computernetwerken onderzocht. Gestructureerd rond de lagen van het TCP/IP model, verduidelijkt deze studie niet alleen hoe netwerkcommunicatie werkt, maar stelt het ook een rigoureuze methodologie vast voor het identificeren, isoleren en oplossen van potentiële problemen.


Deze tools geven beheerders een samenhangende set technische hefbomen om de gezondheid van het netwerk te bewaken, verkeer te analyseren, verbindingen te controleren en snel in te grijpen bij defecte apparatuur of diensten.


#### Netwerktoegang Layer


Tools die direct inzicht geven in interfaces en frames:


- arp / ip neigh**: inspecteer en wijzig de ARP/NDP cache om IP-MAC associaties te controleren of te corrigeren;
- tcpdump**: commandoregel pakketopname, filterbaar en exporteerbaar;
- Wireshark**: grafische pakketanalyse met diepe protocoldecodering;
- ethtool**: opvragen en aanpassen van fysieke parameters van ethernetkaarten (snelheid, duplex, WoL, enz.).


#### Netwerk Layer


Hulpmiddelen voor het beoordelen van IP-connectiviteit, routing en pakketverkeer:


- ping**: test bereikbaarheid en meet latentie met ICMP;
- ip route**: inspecteer en wijzig de routeringstabel om pakketpaden te controleren;
- traceroute**: hop-voor-hop identificatie van routers langs de route naar een bestemming;
- ss**: gedetailleerde inventaris van TCP/UDP sockets en bijbehorende processen (opvolger van netstat).


#### Transport- en toepassingslagen


Hulpmiddelen voor het diagnosticeren van services en processen:


- nslookup / dig / host**: DNS-query's om naamresolutie te valideren en records te analyseren;
- nmap**: open poorten en blootgestelde services verkennen om het aanvalsoppervlak te beoordelen;
- lsof**: maakt een lijst van bestanden en sockets die door processen zijn geopend, en correleert systeem- en netwerkactiviteit.


De beheersing van deze tools, elk afgestemd op een specifieke fase van het TCP/IP-model, maakt een methodische aanpak mogelijk: beginnend bij de fysieke Layer, via routing naar applicatieservices. Deze keten van expertise stelt beheerders in staat om hun infrastructuur te diagnosticeren, beveiligen en optimaliseren, zodat zowel de prestaties als de beschikbaarheid van het netwerk worden gegarandeerd.


# Laatste deel


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Beoordelingen


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Eindexamen


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusie


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>