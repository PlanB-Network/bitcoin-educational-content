---
name: IP-Netze von der Theorie zur Praxis
goal: Beherrschen Sie die Grundlagen von IP-Netzwerken, um sie besser zu konfigurieren und Fehler zu beheben.
objectives: 


  - Den Aufbau und die Funktionsweise des TCP/IP-Protokolls zu verstehen
  - Erläuterung der Unterschiede, Vorteile und Einschränkungen von IPv4 und IPv6
  - Identifizierung und Unterscheidung zwischen verschiedenen Arten von IP Address
  - Konfigurieren und Überprüfen der IP-Adressierung auf Unix/Linux-Systemen
  - Verwendung der wichtigsten Diagnosetools zur Analyse und Lösung von Netzwerkproblemen


---

# Grundlegende Fähigkeiten für die Navigation in der IP-Welt


Tauchen Sie ein in das Herz der IP-Welt und rüsten Sie sich mit dem Wissen aus, um Ihre Netzwerke zu verstehen und effizient zu verwalten. In diesem Kurs lernen Sie alles, was Sie über Computernetzwerke wissen müssen, auf eine klare und praktische Weise.


Sie werden lernen, wie Netzwerke und IP-Adressierung funktionieren, wie man zwischen IPv4 und IPv6 unterscheidet, wie man die verschiedenen Address-Kategorien identifiziert und verwendet und wie man die volle Bedeutung des TCP/IP-Protokolls und die Verbindungen, die es zwischen IP-Adressen, physischen Adressen und DNS-Namen herstellt, begreift.


NET 302 richtet sich vor allem an Studenten, Linux-Anwender oder einfach Neugierige, die die Grundlagen von Netzwerken verstehen und ihre Selbstständigkeit bei der Verwaltung, Fehlersuche und Optimierung von Infrastrukturen stärken wollen.


Kommen Sie zu uns und verwandeln Sie Ihr Wissen in echtes operatives Know-how!


___


Dieser NET 302 Kurs ist eine Adaption von *Les bases du réseau: TCP/IP, IPv4 et IPv6*, geschrieben von Philippe Pierre auf Französisch und veröffentlicht auf [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), unter Creative Commons Attribution - ShareAlike 4.0 International ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)).



Die ursprüngliche Fassung von Loïc Morel wurde grundlegend überarbeitet: Der Text wurde vollständig neu geschrieben, erweitert und angereichert, um den Inhalt zu aktualisieren und zu vertiefen, wobei der pädagogische Geist des ursprünglichen Werks von Philippe Pierre erhalten blieb. Auch die Diagramme wurden überarbeitet.


+++


# Einführung


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Überblick über den Kurs


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Dieser Kurs bietet eine umfassende Einführung in die Grundlagen von IP-Netzwerken. Er ist in vier Hauptabschnitte gegliedert, die jeweils einen wesentlichen Aspekt für das Verständnis, die Konfiguration und die Diagnose von Problemen in einem Computernetzwerk abdecken.


### TCP/IP-Protokoll


In diesem ersten Teil werden wir die Grundlagen schaffen, indem wir das Konzept der Vernetzung und die Geschichte des TCP/IP-Protokolls erkunden. Wir werden seine Hauptkomponenten untersuchen: IP, TCP und ein kurzer Blick auf das IPv5 QoS-Protokoll. Außerdem werden wir uns mit Dienstprimitiven beschäftigen, um die Logik von Daten-Exchange besser zu verstehen.


### IPv4-Adressierung


Danach folgt ein Modul, das sich mit der IPv4-Adressierung befasst. Sie lernen, wie IPv4 in der Praxis verwendet wird, die verschiedenen Address-Typen (privat, öffentlich, Broadcast usw.), die grundlegende Rolle von DNS sowie die Funktionsweise von Ethernet-Adressen und des ARP-Protokolls. Sie werden auch NAT (Network Address Translation) und die Grundlagen der Netzwerkkonfiguration kennen lernen.


### IPv6-Adressierung


Der dritte Teil befasst sich mit der IPv6-Adressierung, die notwendig ist, um Address die Einschränkungen von IPv4 zu überwinden. Wir werden seine Standards und Definitionen, Address Assignment innerhalb eines lokalen Netzwerks, Address Blockmanagement und die Beziehung zwischen IPv6 und DNS durchgehen.


### Netzwerk-Diagnosetools


Abschließend stellen wir Ihnen die wichtigsten Netzdiagnosetools vor. Diese ermöglichen es Ihnen, Störungen zu analysieren, zu kontrollieren und zu beheben. Dieser Teil wird nach Schichten gegliedert sein: Netzwerkzugang, Netzwerk, Transport und obere Schichten.


Am Ende dieses Kurses verfügen Sie über das grundlegende Wissen, um eine Netzwerkinfrastruktur effizient zu verwalten und mögliche Probleme zu diagnostizieren.


Sind Sie bereit, in die Welt der Computernetzwerke einzutauchen? Los geht's!


**HINWEIS**: Die Beschreibungen basieren auf einem GNU/Linux CentOS 7 System. Die Netzwerkkonfigurationen sind jedoch weitgehend identisch, wenn man ein Debian- mit einem CentOS-System vergleicht. Wir werden also keine Unterscheidung machen. Wenn es einen gibt, werden wir ihn mit einem speziellen Logo versehen.


**N.B.**: Wenn Sie während des Kurses auf unbekannte Begriffe stoßen, schlagen Sie bitte im [Glossar] (https://planb.network/resources/glossary) nach.



# TCP/IP-Protokolle


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Was ist ein Netzwerk?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



In diesem ersten Modul werfen wir einen detaillierten Blick auf das TCP/IP-Protokoll, den Eckpfeiler der modernen digitalen Kommunikation. Wir werden seine Ursprünge, seine grundlegenden Prinzipien und das Adressierungssystem besprechen, das für den Informationsfluss zwischen verbundenen Geräten unerlässlich ist.


Wir werden auch die Hauptkomponenten dieses Modells detailliert beschreiben und erklären, wie sie zusammenwirken, um ein funktionsfähiges, zuverlässiges und skalierbares Netz zu bilden. Doch zunächst ist es wichtig, auf das Konzept eines Netzwerks zurückzukommen.


Etymologisch gesehen bezeichnet ein Netz eine Reihe von Punkten, die miteinander verbunden sind und eine zusammenhängende Struktur bilden. In der Telekommunikation und der Informatik bedeutet diese Definition eine Gruppe von Geräten (Computer, Router, Switches, Access Points usw.), die in der Lage sind, Daten über physische oder drahtlose Medien auszutauschen. Ein Netz ermöglicht somit einen kontinuierlichen oder intermittierenden Informationsfluss, je nach Bedarf, den verwendeten Protokollen und der Art der eingesetzten Architektur.


Im Laufe der Zeit wurden verschiedene klassische Topologien entwickelt, um den unterschiedlichen Anforderungen an Kosten, Leistung, Ausfallsicherheit und Wartungsfreundlichkeit gerecht zu werden. Dazu gehören:


- ringnetz,
- baumnetz,
- busnetz,
- stern-Netzwerk,
- maschennetz.



### Ringnetzwerk


In einer Ringtopologie sind die Geräte in einer geschlossenen Schleife miteinander verbunden: Jede Station ist mit der nächsten verbunden, und die letzte verbindet sich wieder mit der ersten. In diesem Aufbau fungiert jedes Gerät als Relais, das Daten an die nächste Verbindung weiterleitet. Je nach Netzwerktyp können die Informationen nur in eine Richtung oder in beide Richtungen zirkulieren.


Der Vorteil dieser Anordnung liegt in der Einfachheit der Verkabelung und in der fehlenden Abhängigkeit von einer zentralen Einrichtung. Allerdings hängt die Kontinuität des gesamten Netzes vom Zustand jedes einzelnen Elements ab: Der Ausfall einer einzigen Station kann das gesamte Kommunikationssystem unterbrechen. Aus diesem Grund werden häufig Redundanz- oder Bypass-Mechanismen eingesetzt.



![Image](assets/fr/001.webp)



### Baum-Netzwerk


Das Baumnetz bzw. die hierarchische Topologie ist der Struktur eines Stammbaums nachempfunden. Es besteht aus aufeinanderfolgenden Ebenen: Ein Wurzelknoten an der Spitze ist mit mehreren untergeordneten Knoten verbunden, die wiederum mit anderen Knoten verbunden sein können, und so weiter.


Dieser hierarchische Aufbau eignet sich besonders für große Netze, die eine klare Aufteilung der Zuständigkeiten und eine segmentierte Verwaltung erfordern. Allerdings macht es das Netz auch anfällig für den Ausfall übergeordneter Knoten: Der Verlust der Wurzel oder einer Hauptverzweigung kann ganze Abschnitte der Infrastruktur abschneiden.



![Image](assets/fr/002.webp)



### Busnetz


Bei einer Bustopologie teilen sich alle Geräte dasselbe Übertragungsmedium, in der Regel eine Koaxialleitung oder eine optische Faser. Jedes Gerät ist passiv angeschlossen, d. h. es verändert das Signal nicht aktiv und kann Daten über diesen gemeinsamen Kanal senden oder empfangen.


Der Hauptvorteil der Bustopologie sind die niedrigen Installationskosten dank der vereinfachten Verkabelung.  Bei älteren, auf Koaxialkabel basierenden Implementierungen (Ethernet 10BASE2/10BASE5) kann jedoch die Unterbrechung oder der Verlust einer einzelnen Station den gesamten Datenverkehr unterbrechen oder sogar zum Stillstand bringen, da die elektrische Kontinuität und die Abschlussimpedanz des Busses nicht mehr gewährleistet sind. Ein einziges physisches Medium ist auch ein kritischer Schwachpunkt: Jede Unterbrechung oder Störung unterbricht die Kommunikation im gesamten Netz.



![Image](assets/fr/003.webp)



### Star-Netzwerk


Die Sterntopologie, auch bekannt als "Hub and Spoke", ist heute am weitesten verbreitet, vor allem in Heim- und Büro-Ethernet-Netzwerken. Hier sind alle Geräte mit einem einzigen zentralen Gerät verbunden.


Dieses Layout erleichtert die Verwaltung und Wartung: Wenn ein Peripheriegerät ausfällt, bleibt der Rest des Netzes davon unberührt. Der Nachteil ist, dass das zentrale Gerät ein Single Point of Failure ist: Wenn es ausfällt, wird die Kommunikation überall unterbrochen. Auch die Qualität der Kabel und die Länge der Verbindungen müssen sorgfältig bedacht werden, um eine gute Leistung zu gewährleisten.



![Image](assets/fr/004.webp)



**Anmerkung**: Es gibt immer noch Netze, die in einer linearen, busähnlichen Topologie organisiert sind, bei der die Geräte nacheinander angeschlossen werden. Diese Lösung ist zwar kostengünstig, hat aber den großen Nachteil, dass eine einzige Unterbrechung einen Teil der Hosts isoliert und das Netz in unabhängige Untergruppen aufteilt.


### Maschennetz


Das Mesh-Netzwerk ist auf maximale Redundanz ausgelegt: Jedes Gerät ist direkt mit jedem anderen Gerät verbunden. Dies gewährleistet die Kontinuität der Dienste, selbst wenn mehrere Verbindungen oder Geräte ausfallen, da der Datenverkehr über alternative Pfade umgeleitet werden kann.


Der Nachteil besteht darin, dass die Zahl der herzustellenden Verbindungen mit der Zahl der Endgeräte rasch zunimmt. Für `N` Verbindungspunkte sind `N × (N-1) / 2` separate Verbindungen erforderlich, was die Einrichtung dieser Topologie teuer und komplex macht. Sie wird daher hauptsächlich in kritischen Netzen verwendet, die eine sehr hohe Verfügbarkeit erfordern, wie bestimmte Teile des Internets oder empfindliche industrielle Systeme.



![Image](assets/fr/005.webp)



Es gibt noch weitere Varianten, wie z. B. Grid- oder Hypercube-Netze, die für spezielle Anforderungen im Bereich des verteilten Rechnens oder der Parallelverarbeitung konzipiert sind.


Auf globaler Ebene ist das Internet ein massiver Verbund von Netzen mit unterschiedlichen Topologien, die durch eine gemeinsame Adressierung (IPv4 und IPv6) und eine Reihe von standardisierten, von der IETF (*Internet Engineering Task Force*) definierten Protokollen vereinheitlicht werden. Diese Vielfalt bedeutet, dass das Internet keiner einzigen Topologie folgt: Seine Struktur ist flexibel, skalierbar und unabhängig vom logischen Adressierungsschema, das es nutzbar macht.



## Die Ursprünge von TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



Die Ursprünge des TCP-Protokolls liegen bei der **ARPA** (*Advanced Research Projects Agency*, 1972 in "DARPA" umbenannt), die 1966 das Projekt **ARPANET** ins Leben rief. Das erste ARPANET-Segment ging im Oktober 1969 in Betrieb und verband die Universitäten UCLA und Stanford miteinander. Ziel war es, Forschungszentren über ein paketvermitteltes Netz zu verbinden, das die Kommunikation auch bei einem teilweisen Ausfall der Infrastruktur aufrechterhalten konnte.


Im Rahmen dieser Dynamik finanzierte die ARPA die Universität von Berkeley, um die ersten TCP/IP-Protokolle in ihr BSD-Unix-System zu integrieren. Dies spielte eine wichtige Rolle bei der Verbreitung und Standardisierung des Protokolls, zunächst in der akademischen Welt, später auch in der Industrie.


**Anmerkung**: Zu dieser Zeit gab es für Informatiker noch kein Linux (das erst Anfang der 1990er Jahre erscheinen sollte) und auch kein Minix, das von Andrew Tanenbaum entwickelte Bildungssystem.  Die wichtigsten Optionen waren Unix oder manchmal auch proprietäre Großrechner wie OpenVMS. Dank seiner Flexibilität und Offenheit trug Unix maßgeblich zur Verbreitung der ersten Netzwerkkonzepte bei.


Genau genommen handelt es sich bei TCP/IP nicht um ein einzelnes Protokoll, sondern um eine Reihe von Protokollen, die auf TCP und IP aufbauen. Es wurde bekannt, weil es ein standardisiertes Programmier-Interface für den Datenaustausch zwischen Rechnern im gleichen Netz zur Verfügung stellte. Dieses Interface, das auf Primitiven, den so genannten "Sockets", basiert, ermöglichte es, zuverlässige und flexible Verbindungen herzustellen und gleichzeitig wichtige Anwendungsprotokolle zu integrieren.


Das ARPANET ist somit die historische Grundlage des heutigen Internets. Das Internet ist in der Tat ein globales Netz, das auf dem Prinzip der Paketvermittlung beruht und in dem Informationen unter Verwendung einer Reihe von standardisierten Protokollen zirkulieren, die die Kompatibilität und Interoperabilität zwischen heterogenen Systemen gewährleisten. Diese offene Architektur hat die Entwicklung und den Einsatz zahlloser Dienste und Anwendungen ermöglicht, darunter:


- emails,
- das World Wide Web (www),
- dateiübertragung und -freigabe...


Die Verwaltung und Entwicklung dieser Protokolle wird vom ***Internet Architecture Board*** (IAB) überwacht.

Diese Organisation koordiniert die technische Ausrichtung durch zwei Hauptstrukturen:


- IRTF** (_Internet Research Task Force_), die langfristige Forschung zur Entwicklung und Verbesserung von Protokollen betreibt.
- IETF** (_Internet Engineering Task Force_), die die im Internet verwendeten Betriebsprotokolle entwickelt, standardisiert und dokumentiert


Die Verteilung der Netzressourcen (IP Address-Bereiche, autonome Systemnummern, Root-Domain-Namen usw.) wird international von **IANA/ICANN** koordiniert. Die operative Verwaltung stützt sich auf: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Europa, Naher Osten, Zentralasien), **ARIN**, **APNIC**, **LACNIC** und **AFRINIC**.


Alle TCP/IP-Protokollspezifikationen werden in Dokumenten namens **RFC** (_Request For Comments_) festgehalten, die als maßgebliche technische Referenzen dienen. Die RFCs werden laufend aktualisiert und nummeriert, um die ständige Weiterentwicklung der Protokollsuite widerzuspiegeln.


Der TCP/IP-Stack wird häufig als ein Stack aus vier funktionalen Schichten dargestellt, oft verglichen mit dem von der **ISO** (_International Standards Organization_) entwickelten Sieben-Layer-Modell **OSI** (_Open Systems Interconnection_), das als konzeptionelle Referenz für Netzwerke dient.


Die vier Schichten des TCP/IP-Modells sind:


- der NETWORK ACCESS Layer, der die Protokolle für die physische Verbindung und die Medienzugriffskontrolle bereitstellt;
- der INTERNET Layer, der für das Routing und die IP-Adressierung zuständig ist;
- der TRANSPORT Layer, der die Zuverlässigkeit und die Verwaltung der Datenströme über Protokolle wie TCP oder UDP gewährleistet;
- der APPLICATION Layer, in dem Benutzer- und Softwareprotokolle wie HTTP, FTP, SMTP und DNS zusammengefasst sind.



![Image](assets/fr/006.webp)



Die heute am weitesten verbreitete IP-Version ist IPv4, aber ihr 32-Bit-Address-Raum hat klare Grenzen. Dies führte zur Einführung von IPv6, das eine 128-Bit-Adressierung verwendet und eine praktisch unbegrenzte Kapazität bietet: eine wesentliche Voraussetzung für die Unterstützung des explosionsartigen Wachstums vernetzter Geräte und die Bewältigung der Herausforderungen des Internets der Dinge, der Mobilität und der Sicherheit.


Jeder Layer des TCP/IP-Stapels bietet spezifische Dienste, die es ermöglichen, Address verschiedene Netzanforderungen auf modulare Weise zu erfüllen: physikalische Übertragung, logische Adressierung, Datenintegrität und Dienste auf Anwendungsebene.


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

## IPv5 QoS-Protokoll


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



Der Header eines IP-Pakets ist eine wesentliche Datenstruktur, die in mehrere Felder unterteilt ist, von denen jedes eine bestimmte Aufgabe hat, um sicherzustellen, dass die Pakete auf ihrem Weg durch das Netz korrekt übertragen und verarbeitet werden. Zu diesen Feldern gehören die Ziel-IP-Address (die benötigt wird, um das Paket an den vorgesehenen Empfänger weiterzuleiten), die durch das IHL-Feld (*Internet Header Length*) angegebene Header-Länge, die im *Total Length-Feld* aufgezeichnete Gesamtlänge des Pakets, Kontroll- und Überprüfungsinformationen sowie andere Parameter zur Verwaltung des Kommunikationsflusses und der Qualität.


Das allererste Feld im Header heißt Version. Dieser 4-Bit-Wert gibt an, welcher Version des IP-Protokolls das Paket folgt. Er ist wichtig, weil er jedem Router oder Zwischengerät mitteilt, wie die eingekapselten Daten zu interpretieren und zu behandeln sind.


**Anmerkung: Die Verwaltung und Assignment der IP-Protokollversionen wird von **IANA** übernommen. Ein 4-Bit-Feld ermöglicht 16 binäre Kombinationen (Werte 0 bis 15). Ihre aktuellen Assignment sind:



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

Dazu gehört IPv5, das zwar in der Öffentlichkeit weitgehend unbekannt ist, aber bereits als ST (_Stream Protocol_) existierte. IPv5 wurde in den 1980er Jahren entwickelt, um Address einen wachsenden Bedarf zu erfüllen: die Bereitstellung von "_Quality of Service_" (QoS) für bestimmte Datenströme, die eine kontinuierliche, stabile Übertragung erfordern, wie z. B. Voice over IP oder Multimedia-Streams. Ziel war es, eine durchgängige Bandbreite und Priorität zu garantieren, ein Konzept ähnlich dem, das RSVP (_Resource Reservation Protocol_) heute für die dynamische Reservierung von Netzwerkressourcen auf modernen Routern bietet.


IPv5 blieb jedoch experimentell und wurde nur in einer kleinen Anzahl von Netzgeräten implementiert. Seine begrenzte Akzeptanz in Verbindung mit dem schnell wachsenden Bedarf an mehr Address-Speicherplatz veranlasste die Internet-Entwickler, direkt von IPv4 auf IPv6 umzusteigen. Damit wurden sowohl die Address-Beschränkungen von IPv4 als auch das Risiko von Verwechslungen oder Inkompatibilitäten mit den experimentellen Spezifikationen von IPv5 vermieden.


Obwohl IPv5 nie weit verbreitet war, spielte es eine wichtige Rolle bei der Entwicklung der ersten Überlegungen zu QoS und Verkehrsmanagement. Heute ist es eher ein historischer Marker als ein funktionierender Standard.


**Erinnerung** - Ein Protokoll ist ein Satz von Kommunikationsregeln: Datenstrukturen, Algorithmen, Paketformate und Konventionen, die es verschiedenen Geräten ermöglichen, Exchange Informationen zuverlässig und verständlich auszutauschen. Ein Dienst ist die konkrete Umsetzung eines Protokolls durch spezifische Programme (Clients, Server), die diesen Regeln folgen und die Funktionalität für Benutzer und Anwendungen verfügbar machen.


Wir können nun einen genaueren Blick auf den Aufbau und die Funktionsweise des IP-Protokolls werfen, der wesentlichen Grundlage jeder Netzwerkkommunikation.



## Das IP-Protokoll


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definitionen und allgemeine Informationen


Das IP-Protokoll, oder "***Internet Protocol***", ist das Rückgrat des TCP/IP-Modells. Es überträgt Datenpakete von einem Host zu einem anderen innerhalb eines Netzes, unabhängig davon, ob es sich um ein lokales oder ein weltumspannendes Netz handelt. Es hat zwei Hauptaufgaben: die Verwaltung der logischen Adressierung von Geräten und die Weiterleitung von Paketen über oft heterogene und zusammengeschaltete Netze.


Auf der physischen Ebene stützt sich die Übertragung auf Hardware-Schnittstellen, um Punkt-zu-Punkt-Verbindungen zwischen Knoten herzustellen. Es ist jedoch das IP-Protokoll, das eine durchgängige Kommunikation ermöglicht, indem es jedes Paket mit den Informationen ausstattet, die es benötigt, um durch mehrere mögliche Pfade zu seinem Ziel zu navigieren.


Drei Netzkonfigurationen Elements bestimmen, wie ein Paket auf die Reise geschickt wird:


- IP Address**: identifiziert den Zielhost im Netz eindeutig.
- Subnetzmaske**: gibt an, welcher Teil der Address das Netz und welcher Teil den Host identifiziert, was eine logische Unterteilung in Subnetze ermöglicht.
- Das Gateway**: gibt den zwischengeschalteten Router an, den das Paket passieren muss, um ein externes Netz oder ein anderes Segment des lokalen Netzes zu erreichen.


Im Internet fließen die Daten nicht in einem kontinuierlichen Strom, sondern werden als **Datagramme** verschickt: unabhängige Datenblöcke, die jeweils mit allen für die Zustellung erforderlichen Informationen gekapselt sind. Dies ist das Prinzip der **Paketvermittlung**, bei der Informationen in eigenständige Einheiten aufgeteilt werden, die auf verschiedenen Wegen denselben Empfänger erreichen können.


Neben der Nutzlast (*Payload*) enthält jedes IP-Datagramm einen strukturierten Header mit Feldern wie Ziel-Address, Quell-Address, Art des Dienstes, Protokollversionsnummer und anderen Kontrollinformationen, die zur Verwaltung der Übertragung benötigt werden.


Die theoretische Maximalgröße eines IP-Datagramms beträgt **65.536 Oktette**, eine Grenze, die durch das Feld für die Gesamtlänge im Header gesetzt wird. In der Praxis wird diese Größe nur selten erreicht, da die physischen Netze, über die die Pakete übertragen werden (Ethernet, Wi-Fi, Glasfaser...), in der Regel eine strengere Grenze vorgeben, die als **MTU** (_Maximum Transmission Unit_) bekannt ist. Wenn ein Datagramm die MTU der physischen Verbindung überschreitet, muss es in kleinere Pakete aufgeteilt werden, die jeweils separat gesendet und bei der Ankunft wieder zusammengesetzt werden.


Diese Anpassungsfähigkeit macht IP zu einem robusten und flexiblen Protokoll, das mit einer Vielzahl von zugrundeliegenden Technologien betrieben werden kann und gleichzeitig eine universelle Kompatibilität zwischen heterogenen Systemen und Netzen gewährleistet.



### Fragmentierung von IP-Datagrammen


Wenn ein IP-Datagramm ein Netz durchqueren muss, dessen Übertragungskapazität kleiner ist als das Datagramm selbst, muss es **fragmentiert** werden, damit es ohne Probleme übertragen werden kann. Diese physikalische Größenbeschränkung wird als **MTU** (Maximum Transmission Unit) bezeichnet: die größte Rahmengröße, die ein bestimmtes Netz passieren kann, ohne aufgeteilt zu werden.


Jede Netzwerktechnologie hat ihre eigene MTU, die durch ihre Hardware- und Protokolleigenschaften bestimmt wird. Übliche Werte sind:


- ARPANET**: 1000 Bytes
- Ethernet**: 1500 Bytes
- FDDI**: 4470 Bytes


Wenn ein Datagramm die MTU eines Netzsegments, das es durchqueren muss, überschreitet, wird es von der Routing-Ausrüstung in kleinere **Fragmente** aufgeteilt, die die Grenze einhalten. Dies geschieht in der Regel beim Wechsel von einem Netz mit hoher MTU zu einem Netz mit geringerer Kapazität. So muss beispielsweise ein Datagramm, das aus einem FDDI-Netz kommt, möglicherweise fragmentiert werden, bevor es über ein Ethernet-Segment gesendet wird.



![Image](assets/fr/008.webp)



Der Fragmentierungsprozess funktioniert folgendermaßen:


- Der Router zerlegt das Datagramm in Fragmente, die nicht größer als die MTU des Zielnetzes sind.
- Die Größe jedes Fragments ist ein Vielfaches von 8 Byte, da das IP-Protokoll diese Einheit zur Kodierung des Reassembly-Offsets verwendet.
- Jedes Fragment erhält einen eigenen IP-Header, der die Informationen enthält, die der Endempfänger benötigt, um die Fragmente in der richtigen Reihenfolge wieder zusammenzusetzen.


Nach der Fragmentierung reisen die einzelnen Teile unabhängig voneinander durch das Netz. Je nach Routing-Tabellen, Verbindungsauslastung oder Ausfällen können sie unterschiedliche Routen nehmen. Es gibt keine Garantie dafür, dass sie in der Reihenfolge ankommen, in der sie gesendet wurden.


Bei der Ankunft führt der empfangende Rechner eine **Wiederzusammensetzung** durch. Anhand der Informationen in den Kopfzeilen (gemeinsame Kennung, Versatz und Fragmentierungskennzeichen) setzt er die Fragmente in der richtigen Reihenfolge zusammen, um das ursprüngliche Datagramm zu rekonstruieren, bevor er es an den nächsten Layer weiterleitet. Wenn auch nur ein Fragment verloren geht oder beschädigt wird, wird in der Regel das gesamte Datagramm verworfen, da das Ergebnis ohne jedes Stück unvollständig oder unbrauchbar wäre.


Fragmentierung und Reassemblierung sind zwar effektiv, haben aber auch Nachteile: zusätzliche Verarbeitungszeiten für Router und Hosts und ein höheres Risiko von Paketverlusten, was zu mehr Neuübertragungen führen kann. Deshalb sind eine sorgfältige MTU-Verwaltung und die Optimierung der Paketgröße wichtig für eine reibungslose, effiziente IP-Kommunikation.



### Datenkapselung


Um sicherzustellen, dass die Daten korrekt durch die Schichten des TCP/IP-Modells geleitet werden, spielt der Prozess der **Einkapselung** eine Schlüsselrolle. In jeder Phase, in der eine Nachricht von der Anwendung des Absenders zum Rechner des Empfängers übertragen wird, werden zusätzliche Informationen, so genannte Header, hinzugefügt. Diese Header geben den Zwischengeräten und Softwareschichten die Anweisungen, die sie benötigen, um die Daten zu verarbeiten, zu übermitteln und ggf. wieder zusammenzusetzen.


Wenn eine Nachricht gesendet wird, durchläuft sie die vier Schichten des TCP/IP-Stacks. Bei jeder Layer wird den vorhandenen Daten ein neuer Header vorangestellt: Jeder Header enthält spezifische Metadaten wie logische oder physische Adressen, Kommunikationsports, Sequenznummern, Fehlerkontrollflags und alle Informationen, die für die Verwaltung der Übertragung und der Weiterleitung erforderlich sind.


Die Übermittlung erfolgt also nach einem strukturierten Verfahren:


- Die Anwendung Layer erstellt die erste **Nachricht**, die die Rohdaten enthält.
- Der Transport Layer kapselt sie in ein **Segment** ein und fügt Quell- und Zielport, Sequenznummern und Flusskontrollmechanismen hinzu.
- Der Internet-Layer fügt dem Segment einen IP-Header hinzu, um ein **Datagramm** zu bilden, das Quell- und Ziel-IP-Adressen angibt.
- Das Network Access Layer verpackt das Datagramm in einen **Frame** und fügt MAC-Adressen und Integritätsprüfcodes (CRC) hinzu.



![Image](assets/fr/009.webp)



Dieser Verkapselungsprozess gewährleistet sowohl die Integrität und Rückverfolgbarkeit der Daten als auch ihre Anpassungsfähigkeit: Beim Wechsel von einem Netz in ein anderes liefern die Kopfzeilen den Geräten die Informationen, die sie für die Wahl der Route, die Überprüfung der Gültigkeit oder gegebenenfalls für die Fragmentierung benötigen.


Bei der Ankunft wird der Prozess umgekehrt: Der empfangende Rechner erhält den Rahmen beim Netzzugang Layer, der den entsprechenden Header liest und entfernt. Das Datagramm wird dann an den Internet-Layer weitergeleitet, der den IP-Header liest und ihn wiederum entfernt, um das Segment an den Transport-Layer zu liefern. Das Transport-Layer verarbeitet die Transport-Header, prüft die Integrität des Datenstroms und liefert schließlich die **Nachricht** in ihrem ursprünglichen Zustand an die Zielanwendung.



![Image](assets/fr/010.webp)



Die Transformation der Daten bei jedem Layer kann wie folgt zusammengefasst werden:


- Nachricht**: Informationsblock in der Anwendung Layer.
- Segment**: Dateneinheit nach Verkapselung durch den Transport Layer.
- Datagramm**: Form nach Hinzufügung des IP-Headers durch den Internet-Layer.
- Rahmen**: letzter Block, der zur Übertragung über das physikalische Medium durch den Netzzugang Layer bereit ist.



![Image](assets/fr/011.webp)



Dieses Verfahren, das für die Zuverlässigkeit und Universalität der Internetkommunikation unerlässlich ist, stellt sicher, dass alle Daten, egal wie fragmentiert oder komplex sie sind, von einem Ende zum anderen transportiert werden können und dabei für den Empfänger verständlich und nutzbar bleiben.



### IP-Adressierung


Auch wenn Paketvermittlung, Fragmentierung und Verkapselung vorhanden sind, könnte ein Netz ohne ein zuverlässiges Adressierungssystem nicht funktionieren. Um sicherzustellen, dass jedes Datenpaket den richtigen Empfänger erreicht, verwendet das Internet Layer eine eindeutige Kennung: die **IP Address**.

In IPv4 wird ein IP Address auf **32 Bits** kodiert und als vier durch Punkte getrennte Dezimalzahlen im bekannten Format N1.N2.N3.N4 geschrieben (zum Beispiel: 192.168.1.12).


Ein IP Address besteht aus zwei Teilen:


- _netid_**: identifiziert das Netz, zu dem der Host gehört
- _hostid_**: identifiziert den spezifischen Host innerhalb dieses Netzes

Durch diese Trennung kann das globale Internet logisch in viele miteinander verbundene Netze gegliedert werden.


In der Vergangenheit beruhte das IPv4-System auf einem klassenbasierten Schema, das mit A bis E bezeichnet war und den Bereich der Address und deren Verwendungszweck definierte. Jede Klasse wies der _netid_ und _hostid_ eine bestimmte Anzahl von Bits zu, was sich direkt auf die mögliche Anzahl von Netzen und Hosts auswirkte.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Nicht alle möglichen Werte können den Hosts zugeordnet werden. Bei einem Address der **Klasse C** beispielsweise bietet das letzte Byte 8 Bits (256 Werte). Zwei davon sind jedoch reserviert:


- 0: identifiziert das Netz selbst
- 255: ist der **Broadcast** Address, der verwendet wird, um ein Paket an alle Hosts im Netz auf einmal zu senden.

Damit bleiben 254 nutzbare Adressen für Geräte übrig.


Die Anzahl der verfügbaren Adressen ist je nach Klasse sehr unterschiedlich: von großen öffentlichen Netzen in Klasse A über Unternehmensnetze in Klasse B bis hin zu kleineren lokalen Netzen in Klasse C.



![Image](assets/fr/013.webp)



Einige Address-Bereiche sind für die private Nutzung reserviert und werden nie direkt ins Internet geleitet. Diese sind als **private Adressen** bekannt und werden innerhalb von Organisationen, Unternehmen oder Haushalten verwendet und erfordern eine Address-Übersetzung, typischerweise NAT (*Network Address Translation*), um das öffentliche Internet zu erreichen. Diese sind:


- Klasse A**: von 10.0.0.0 bis 10.255.255.255
- Klasse B**: von 172.16.0.0 bis 172.31.255.255
- Klasse C**: von 192.168.0.0 bis 192.168.255.255


Wenn ein Gerät mit einem privaten Address auf das Internet zugreift, wird es von einem NAT-fähigen Router oder Gateway durch einen gültigen öffentlichen Address ersetzt.


Beispiel: Wenn ein Host den Address **192.168.7.5** hat, können wir daraus schließen:


- 192.168.7.0: Netzwerk Address
- 192.168.7.1: oft der lokale Router
- 192.168.7.5: der Host selbst


Ein weiterer Sonderfall ist **127.0.0.1**, bekannt als "***Loopback***".

Auf Linux-Systemen ist er mit dem Interface **lo** verbunden. Dieser Address ermöglicht es einer Maschine, sich für lokale Tests oder Diagnosen selbst zu Address, ohne einen physischen Interface zu durchlaufen. Der gesamte Bereich **127.0.0.0/8** ist für diesen Zweck reserviert.


Um den Address optimal zu nutzen und komplexe Netzwerke zu entwerfen, ist die **Subnetzmaske** (_netmask_) unerlässlich. Diese binäre Maske trennt die _netid_ von der _hostid_ in einem IP-Address.

Jede Klasse hat eine Standardmaske:


- 255.0,0,0** für die Klasse A,
- 255.255.0.0** für Klasse B,
- 255.255.255.0** für Klasse C.


Ein gutes Netzwerkdesign folgt einer Grundregel: Geräte, die direkt miteinander kommunizieren müssen, sollten sich im selben Netzwerk oder Subnetz befinden. Um ein Netz zu segmentieren, verwenden wir das Subnetting, d. h. die Unterteilung eines Netzes in kleinere Subnetze durch Verwendung einer spezifischeren Maske.


Beispiel für Subnetting:

Ein **Klasse C**-Netzwerk: 192.168.1.0/24 mit einer Standardmaske von 255.255.255.0.

Wir wollen 4 Subnetze mit jeweils bis zu 60 Hosts.


**Schritt 1**: Anzahl der benötigten Adressen pro Subnetz = 60 + 2 reservierte Adressen (Netzwerk + Broadcast) = 62.


**Schritt 2**: Finde die nächstliegende Potenz von 2 ≥ 62. -> 2⁶ = 64.


**Schritt 3: Passen Sie die Maske an. Behalten Sie die _netid_ Bits und reservieren Sie die benötigten _hostid_ Bits. Wir erhalten eine binäre Maske, die nach der Umwandlung **255.255.255.192** ergibt.


```
11111111 11111111 11111111 11000000
```


**Schritt 4**: Berechnen Sie die Address-Bereiche für jedes Teilnetz und variieren Sie dabei die für den Host reservierten Bits.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Schritt 5**: Dadurch werden vier Teilnetze geschaffen, die jeweils bis zu 62 Rechner unterstützen, wobei das Adressierungsschema insgesamt effizient bleibt. Der Teil _hostid_ wird in einen Teil _subnetid_ und einen Teil host aufgeteilt.



![Image](assets/fr/016.webp)



Dieses Grundprinzip der Subnetzung ist in der modernen Netztechnik nach wie vor unverzichtbar und ermöglicht eine präzise IP-Zuweisung, eine bessere Kontrolle des Datenverkehrs, eine starke Segmentisolierung und eine skalierbare Netzverwaltung.



### CIDR-Adressierung


In den frühen 1990er Jahren, als sich das Internet in Unternehmen und Organisationen schnell verbreitete, begann das traditionelle IP-Adressierungssystem, das auf Klassen (A, B, C) basierte, seine Grenzen zu zeigen.

Ihre starre Struktur führte zu einer erheblichen Verschwendung von IP-Adressen und machte die Routing-Tabellen immer größer, komplexer und schwieriger zu pflegen.

Um diese Probleme zu lösen, wurde eine flexiblere und effizientere Methode eingeführt: **CIDR** (_Classless Inter-Domain Routing_). CIDR ist allmählich zum Standard geworden und hat das alte klassenbasierte System weitgehend ersetzt.


Der Kerngedanke hinter CIDR ist die Möglichkeit, mehrere benachbarte Netze, insbesondere Blöcke der Klasse C, zu einer einzigen logischen Einheit zusammenzufassen, die als **Supernetz** (_supernet_) bezeichnet wird. Durch diese Zusammenfassung kann ein einziger Eintrag in der Routing-Tabelle mehrere Teilnetze repräsentieren, wodurch sich die Anzahl der von den Routern zu bearbeitenden Routen verringert und ihre Leistung verbessert.


Während die Netze der Klasse C aufgrund ihrer geringeren Kapazität ursprünglich den größten Bedarf an Aggregation hatten, wurde das Prinzip auch auf Netze der Klasse B und theoretisch sogar auf Netze der Klasse A angewandt, wobei letztere aufgrund ihrer großen Address-Reichweite weniger betroffen sind.


Mit CIDR verschwindet das Konzept der festen Klassen. Der Address-Raum wird als kontinuierlicher Bereich behandelt, der nach Bedarf unterteilt oder zusammengefasst werden kann. CIDR-Blöcke werden mit Hilfe von Subnetzmasken definiert, die nicht auf die Standardwerte der Klassen A, B oder C beschränkt sind. Ein CIDR-Block kann entweder ein einzelnes Netz oder einen zusammenhängenden Satz von Teilnetzen mit demselben Präfix darstellen.


Ein CIDR-Block wird im Format "Address/Präfix" geschrieben, wobei die Zahl nach dem Schrägstrich angibt, aus wie vielen Bits sich der Netzwerkteil zusammensetzt. Zum Beispiel bedeutet /17, dass die ersten 17 Bits das Netzwerk identifizieren, während die restlichen 15 Bits die Hosts identifizieren.


Beispiel:

Ein /17-Block enthält 2^(32-17) Adressen, also 2^15 = 32.768 Adressen insgesamt. Zieht man die beiden reservierten Adressen (Netzwerk und Broadcast) ab, bleiben 32.766 nutzbare Hostadressen übrig. So können Netzwerkadministratoren die Größe ihrer Subnetze genau an den tatsächlichen Bedarf anpassen und unnötige Verschwendung vermeiden.


Zum besseren Verständnis der CIDR-Größenordnung finden Sie hier eine Tabelle mit gängigen Präfixen und den entsprechenden Subnetzmasken und nutzbaren Adressen:


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


**HINWEIS**: In der Vergangenheit wurde in RFC 950 von der Verwendung von Subnetz-Null abgeraten, hauptsächlich um Verwirrung beim Routing zu vermeiden.  Diese Einschränkung wurde mit RFC 1878 obsolet, das die Verwendung von Subnetz-Nullen vollständig erlaubt. Die alte Einschränkung war hauptsächlich auf die Unverträglichkeit mit älterer Hardware zurückzuführen, die CIDR nicht korrekt verarbeiten konnte. Moderne Geräte haben dieses Problem nicht.


So ist beispielsweise das Subnetz **1.0.0.0** mit der Subnetzmaske **255.255.0.0**, das früher mit der Netzkennung der Klasse A mehrdeutig war, jetzt vollkommen gültig und verwendbar.


**TIP**: Für fehlerfreie Subnetzberechnungen und die schnelle Umwandlung von Adressen in die CIDR-Notation gibt es praktische Tools wie ***ipcalc***. Dieser "Netzwerkrechner" zeigt übersichtlich Address-Aufschlüsselungen, verfügbare Bereiche und zugehörige Masken an, ideal sowohl für Administratoren als auch für Studenten, die CIDR lernen.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## Das TCP-Protokoll


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



Das **TCP-Protokoll** (_Transmission Control Protocol_) spielt eine zentrale Rolle im TRANSPORT Layer des TCP/IP-Modells. Es fungiert als Brücke zwischen Anwendungen und dem Internet Layer und sorgt für die zuverlässige Übertragung von Daten zwischen zwei entfernten Rechnern.

Während das IP-Protokoll lediglich Pakete sendet, ohne deren Zustellung oder Reihenfolge zu garantieren, gewährleistet TCP die Integrität und Konsistenz des Datenflusses, indem es die Daten verlustfrei, in der richtigen Reihenfolge und ohne Duplikate zustellt.


Zu den Hauptaufgaben von TCP gehören:


- Neuordnung der empfangenen Segmente;
- Überwachung des Datenflusses zur Vermeidung von Überlastungen;
- Aufteilung oder Wiederzusammensetzung von Datenblöcken in geeignete Einheiten (Segmente);
- Verwaltung des Auf- und Abbaus von Verbindungen zwischen beiden Enden der Kommunikation.


TCP ist ein verbindungsorientiertes Protokoll, d. h. es stellt eine explizite, kontinuierliche Beziehung zwischen Client und Server her. Dazu verwendet es **Sequenznummern** und **Bestätigungen**: Für jedes gesendete Segment wird eine eindeutige Kennung vergeben, damit der Empfänger sowohl die Reihenfolge als auch die Integrität der Daten überprüfen kann. Der Empfänger sendet dann ein Bestätigungssegment mit dem **ACK-Flag** auf 1 gesetzt zurück, das den Empfang bestätigt und die nächste erwartete Sequenznummer angibt.



![Image](assets/fr/018.webp)



Um die Zuverlässigkeit zu verbessern, verwendet TCP einen Zeitgeber: Sobald ein Segment gesendet wird, beginnt ein Countdown. Trifft innerhalb der Zeitspanne keine Bestätigung ein, sendet der Absender das Segment automatisch erneut, wobei er davon ausgeht, dass es bei der Übertragung verloren gegangen ist. Dieser Mechanismus der automatischen Neuübertragung gleicht die Verluste aus, die in IP-Netzen bei Überlastung, Routing-Fehlern oder Hardware-Ausfällen auftreten können.



![Image](assets/fr/019.webp)



TCP ist in der Lage, Duplikate zu erkennen und zu behandeln. Wenn ein neu übertragenes Segment eintrifft, aber auch das Original auftaucht, verwendet der Empfänger die Sequenznummern, um das Duplikat zu identifizieren und nur die korrekte Kopie zu behalten, um jede Unklarheit zu beseitigen.


Damit dieses Verfahren funktioniert, müssen beide Rechner eine gemeinsame Vorstellung von ihren anfänglichen Sequenznummern haben. Dies wird durch ein striktes Verbindungsverfahren sichergestellt: Einerseits lauscht der **Server** auf einem bestimmten Port und wartet auf eine eingehende Anfrage (passiver Modus); andererseits initiiert der **Client** aktiv die Verbindung, indem er eine Anfrage an den Server auf demselben Service-Port sendet.


**HINWEIS**: Ein "Port" ist eine numerische Kennung (von 0 bis 65.535), die einer Netzwerkanwendung auf einem Computer zugewiesen wird. Er wird verwendet, um mehrere Dienste zu unterscheiden, die gleichzeitig auf demselben IP Address laufen. Wenn ein Client Daten sendet, gibt er die Portnummer an, damit das Betriebssystem des Servers weiß, welches Programm sie empfangen soll (z. B. 80 für HTTP, 443 für HTTPS, 25 für SMTP). Ports wirken wie spezielle Türen, die den Verkehr hinein- und hinausleiten, Verwechslungen zwischen Diensten verhindern und eine fein abgestufte Zugangskontrolle durch Firewalls oder Filterregeln ermöglichen.


Die Sequenzsynchronisierung Exchange basiert auf dem berühmten **"*Drei-Wege-Handschlag*"**-Mechanismus, ähnlich der Art und Weise, wie sich zwei Menschen zur Kontaktaufnahme begrüßen. Diese Initialisierungsphase, die die Zuverlässigkeit von TCP gewährleistet, erfolgt in 3 Stufen:

1. **SYN:** Der Client sendet ein anfängliches Synchronisierungssegment (**SYN**) mit dem entsprechenden Flag und einer anfänglichen Sequenznummer (z. B. C);

2. **SYN-ACK:** Der Empfangsserver antwortet mit einem Bestätigungssegment (**SYN-ACK**), bestätigt die Sequenznummer des Clients und gibt seine eigene Anfangssequenznummer an;

3. **ACK:** Der Client sendet eine abschließende Bestätigung (**ACK**), die den Empfang der Sequenznummer des Servers bestätigt und die Synchronisierung abschließt. Das SYN-Flag ist nun deaktiviert und das ACK-Flag bleibt gesetzt, was anzeigt, dass die Verbindung hergestellt ist.



![Image](assets/fr/020.webp)



Dieses Exchange-Protokoll stellt sicher, dass beide Parteien vor der Übertragung von Nutzdaten die gleiche Nummerierungsbasis verwenden. Sobald diese Synchronisierung abgeschlossen ist, wird die Sitzung eröffnet: Die Segmente können nun in beide Richtungen übertragen werden, wobei jedes Segment beim Empfang bestätigt wird, was eine maximale Zuverlässigkeit des Datenflusses gewährleistet.


Dieser ***three-way handshake*** betrifft nur den Verbindungsaufbau. Für den Abbau verwendet TCP einen *vierfachen Handshake*: FIN → ACK → FIN → ACK, der garantiert, dass kein Segment im Transit verloren geht, bevor die Verbindung vollständig abgebaut ist.


Obwohl dieser Prozess auf Robustheit und Zuverlässigkeit ausgelegt ist, hat er auch zu ausnutzbaren Schwachstellen geführt. So zielen beispielsweise Angriffe wie **IP Spoofing** darauf ab, diese Vertrauensbeziehung zu umgehen oder zu untergraben, indem sie sich durch gefälschte Sequenznummern als autorisierter Rechner ausgeben und so eine Lücke schaffen, die das Abfangen oder Manipulieren des Datenstroms ermöglicht.


Zur Begrenzung des Risikos des Hijackings der Sequenzsynchronisation und zur Verwaltung der Netzlast verwendet das TCP-Protokoll eine Technik zur Verwaltung des Datenflusses, die als "**_Sliding Window_**" bekannt ist. Dieses System regelt, wie viele Daten gesendet werden können, ohne dass für jedes Segment eine sofortige Bestätigung erforderlich ist, wodurch eine unnötige Überlastung des Netzes vermieden und gleichzeitig eine hohe Zuverlässigkeit gewährleistet wird.


In der Praxis definiert das gleitende Fenster einen Bereich von Sequenznummern, der frei zwischen Sender und Empfänger zirkulieren kann, ohne dass jedes einzelne Segment bestätigt werden muss. Wenn das sendende System Bestätigungen erhält, "gleitet" das Fenster: Es rutscht nach rechts und schafft Platz für neue zu sendende Segmente. Die Größe dieses Fensters (entscheidend für die Optimierung des Durchsatzes bei gleichzeitiger Vermeidung von Überlastungen) wird im Feld "*Window*" des TCP-Headers angegeben.


**Beispiel**: Wenn die anfängliche Sequenznummer 3 ist und das Fenster bis zur Sequenz 5 reicht, können die Segmente mit den Nummern 3 bis 5 gesendet werden, ohne auf einzelne Bestätigungen zu warten.



![Image](assets/fr/021.webp)



Die Größe des Schiebefensters ist nicht festgelegt; sie passt sich dynamisch an die Netzbedingungen und die Verarbeitungskapazität des Empfängers an.  Wenn der Empfänger eine größere Datenmenge verarbeiten kann, zeigt er dies über das Feld Window an und fordert den Sender auf, sein Fenster zu vergrößern. Umgekehrt kann der Empfänger bei Überlastung oder Sättigungsgefahr eine Verkleinerung des Fensters verlangen, und der Sender wartet, bis das Fenster weitergeht, um zusätzliche Segmente zu senden.


Das Protokoll sieht ein symmetrisches Verfahren zum Schließen einer TCP-Verbindung vor, um ein sauberes, geordnetes Herunterfahren zu gewährleisten. Jeder Rechner kann die Schließung einleiten, indem er ein Segment mit dem Flag **FIN** auf 1 setzt und damit seine Absicht, die Kommunikation zu beenden, signalisiert. Dann wird gewartet, bis alle in der Übertragung befindlichen Segmente empfangen worden sind, und alle weiteren Daten werden ignoriert.


Nach dem Empfang dieses Segments sendet der andere Rechner eine Bestätigung, die ebenfalls mit dem FIN-Kennzeichen versehen ist. Anschließend beendet er die Übertragung der verbleibenden Daten, bevor er der lokalen Anwendung mitteilt, dass die Verbindung beendet wurde. Diese doppelte Bestätigung gewährleistet ein geordnetes Herunterfahren und minimiert das Risiko von Datenverlusten.


Diese präzise Verwaltung, die das flexible Routing von IP mit der strikten Kontrolle von TCP kombiniert, wird häufig durch ein Diagramm veranschaulicht, in dem die Geschwindigkeit des IP-Protokolls (das auf **"best effort "**-Basis ohne Zustellungsgarantie arbeitet) der Zuverlässigkeit des TCP-Protokolls (das die Übertragung durch Bestätigungen und ausgehandelte Sequenzen steuert) gegenübergestellt wird.



![Image](assets/fr/022.webp)



In manchen Fällen steht jedoch nicht die absolute Zuverlässigkeit im Vordergrund, sondern Geschwindigkeit und Einfachheit. Dies gilt für Anwendungen wie Live-Streaming oder VoIP, die einen gewissen Paketverlust tolerieren können, ohne dass die Benutzererfahrung ernsthaft beeinträchtigt wird. In solchen Fällen wird **UDP** (_User Datagram Protocol_) bevorzugt.


UDP arbeitet nach einem grundlegend anderen Prinzip als TCP: Es ist **verbindungslos**, d. h. es wird keine vorherige Beziehung zwischen Sender und Empfänger hergestellt. Wenn ein Rechner Pakete über UDP sendet, werden sie nur in eine Richtung übertragen; der Empfänger sendet keine Bestätigungen, und der Sender hat keine Bestätigung, dass die Nachricht angekommen ist. Der UDP-Header ist absichtlich minimal und enthält nur den Quellport, den Zielport, die Segmentlänge und eine Prüfsumme, ohne einen eingebauten Bestätigungs- oder Statuskontrollmechanismus. IP-Adressen werden wie immer durch den zugrunde liegenden IP-Header übertragen.


Eine gängige Analogie ist, dass TCP wie ein **Telefongespräch** ist, bei dem eine Verbindung aufgebaut und während des gesamten Gesprächs verfolgt und kontrolliert wird. Das UDP-Protokoll hingegen ist wie ein **Postbrief**, bei dem der Absender einen Brief in einen Briefkasten wirft, ohne sofortigen Nachweis der Zustellung oder systematische Rückmeldung.


Diese Komplementarität zwischen TCP und UDP ermöglicht es modernen Netzen, sich an eine Vielzahl von Anforderungen anzupassen und je nach Anwendung ein Höchstmaß an Zuverlässigkeit zu erreichen oder der Geschwindigkeit den Vorrang zu geben.



## Dienstprimitive


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Mehrschichtige Architektur und Exchange-Organisation


Wie wir gesehen haben, sind **Dienste** die konkrete Umsetzung der bisher beschriebenen Protokolle. Das TCP/IP-Modell unterscheidet sich zwar vom **OSI**-Modell, verfolgt aber denselben mehrschichtigen Ansatz: Jeder Layer ist für die Ausführung einer bestimmten Funktion und die Bereitstellung von **Diensten** für den direkt darüber liegenden Layer vorgesehen, was zu einer modularen, robusten und leicht zu wartenden Architektur führt.


Jeder Layer baut auf den Fähigkeiten des darunter liegenden auf und stellt wiederum dem darüber liegenden Layer einen konsistenten Interface für die Datenverwaltung zur Verfügung. In dieser Architektur hat jeder Layer seine eigenen **Datenstrukturen**, die sorgfältig definiert sind, um eine perfekte Kompatibilität mit den anderen Schichten zu gewährleisten. Diese Kompatibilität ist eine wesentliche Voraussetzung für eine reibungslose, zuverlässige und klare Kommunikation von einem Endpunkt zum anderen.


Zwei wesentliche Aspekte bestimmen diesen Austausch:


- Vertikaler Aspekt**: die Beziehung zwischen einem Layer und dem darüber oder darunter liegenden (von Layer N zu Layer N+1 und umgekehrt).



![Image](assets/fr/023.webp)




- Horizontaler Aspekt**: die Interaktion zwischen entfernten Anwendungen, d. h. der Dialog zwischen einem **Client** und einem **Server**, in beiden Richtungen.



![Image](assets/fr/024.webp)



Die Schichtenarchitektur folgt dem Prinzip, dass jeder Layer nur die Informationen verarbeitet, die in seinen Bereich fallen: Datenstrukturen, Kopfzeilen und Kontrollmechanismen variieren von einem Layer zum anderen, aber zusammen bilden sie ein kohärentes System, das sicherstellt, dass die Daten schrittweise an ihr endgültiges Ziel geleitet werden.


**Erinnerung**: Zur Beschreibung der zwischen den Schichten ausgetauschten Dateneinheiten wird eine spezielle Terminologie verwendet:


- nachricht** für die Anwendung Layer,
- segment** für den Transport Layer (TCP),
- datagramm** für das Internet Layer (IP),
- rahmen** für den Netzwerkzugang Layer.


In der folgenden Tabelle sind die Begriffe für TCP- und UDP-Kontexte zusammengefasst:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Dienstprimitive und Dateneinheiten


Den Kern dieses Systems bilden **Dienstprimitive**, die als Kommunikationsschnittstellen fungieren. Diese Primitive funktionieren wie Service Desks, die auf reservierten spezifischen **Ports** lauschen und es Prozessen ermöglichen, Netzwerkverbindungen auf kontrollierte Weise aufzubauen, aufrechtzuerhalten und zu beenden. Während Protokolle das Format und die Übertragung von Daten über das Netz organisieren, sind es die **Dienste und ihre Primitive**, die die vertikale Verbindung zwischen den Schichten herstellen.


Durch die Kombination des horizontalen Aspekts (Kommunikation zwischen verteilten Anwendungen) mit dem vertikalen Aspekt (interne Interaktionen zwischen den Schichten) bietet das TCP/IP-Modell eine vollständige, skalierbare Architektur. Die Überschneidung dieser beiden Perspektiven gibt einen klaren Überblick darüber, wie Daten in einer strukturierten Netzkommunikation ausgetauscht werden.



![Image](assets/fr/026.webp)



### Teil Zusammenfassung


In diesem ersten großen Abschnitt haben wir uns mit der Kernarchitektur befasst, die die Konfiguration und den Betrieb der heutigen mit dem Internet verbundenen Netze bestimmt. Diese Architektur basiert auf einem **Vier-Layer-Modell**, das sich am OSI-Modell orientiert und um die **TCP/IP**-Protokollsuite herum aufgebaut ist, dem Rückgrat der modernen Kommunikation. Wir haben gesehen, dass TCP mit seinem verbindungsorientierten Ansatz zuverlässige Übertragungen gewährleistet, während UDP, das leichter und schneller ist, bevorzugt wird, wenn Geschwindigkeit wichtiger ist als Zuverlässigkeit.


Das ordnungsgemäße Funktionieren dieses Modells hängt von der Implementierung von Protokollen durch **Dienstprimitive** ab. Diese stellen die Verbindung zwischen den Schichten sicher und ermöglichen die Anpassung der Datenverarbeitung an die spezifischen Anforderungen jeder Ebene, vom Transport bis zur Anwendung, einschließlich Internet und Netzzugang. Dieser modulare Ansatz macht das System sowohl flexibel als auch robust.


Die IP-Adressierung ist ein weiterer Eckpfeiler dieser Infrastruktur. Jedes angeschlossene Gerät wird durch eine **einzigartige IP Address** identifiziert, die aus einem in **Klassen** (von A bis E) organisierten Address-Raum stammt. Einige dieser Adressen sind für besondere Zwecke reserviert, wie z. B. lokales Loopback oder Multicast, während andere, so genannte "private Adressen", ohne Übersetzung (NAT) nicht über das Internet geleitet werden. Diese Klassifizierung ermöglicht eine logische, hierarchische Organisation der Netze.


Wir haben auch das Konzept der **Subnetze** untersucht, das es ermöglicht, ein Netz in Segmente zu unterteilen, um IP-Ressourcen besser zu verwalten und den Datenfluss zu optimieren. Die manuelle Unterteilung mit Hilfe von Subnetzmasken ist zwar nach wie vor ein wichtiges Prinzip, doch wurde es dank **CIDR** (_Classless Inter-Domain Routing_) weitgehend modernisiert. Diese Methode hat die Address-Verwaltung verändert, da sie eine flexiblere und rationellere Zuweisung von IP-Bereichen ermöglicht und gleichzeitig die Größe der Routing-Tabellen verringert.


Durch die Beherrschung dieser Konzepte - Schichten, Protokolle, Dienstprimitive, Adressierung und Subnetting - erhalten Sie eine solide Grundlage für das Verständnis der technischen Funktionsweise moderner Netzwerke und für die effiziente Konfiguration einer Netzwerkinfrastruktur, die den heutigen Anforderungen entspricht.


Im nächsten Abschnitt werden wir uns die IPv4-Adressierung genauer ansehen.



# IPv4-Adressierung


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Verwendung von IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



In diesem Abschnitt gehen wir näher darauf ein, wie **IPv4**-Adressen tatsächlich in einem realen Netzwerk implementiert sind. Wir werden ihr Format aufschlüsseln, die Logik dahinter und wie sie mit anderen wichtigen Netzwerk-Elements wie **DNS-Namen**, **MAC-Adressen**, **Subnetzwerken** und **Übersetzungstechniken** zusammenhängen.


Ein IP-Address ist eine eindeutige numerische Kennung, die jedem **Netzwerk-Interface** eines Geräts zugewiesen wird. Sie ermöglicht es, dieses Gerät innerhalb eines Netzwerks zu lokalisieren und es zur Datenübertragung zu erreichen. Ein Router, ein Server, eine Arbeitsstation, ein Netzwerkdrucker oder auch eine Überwachungskamera hat beispielsweise mindestens einen eigenen IP-Address. Der IP Address ermöglicht das **Routing**, d. h. die Weiterleitung von Paketen von Punkt A nach Punkt B, auch wenn diese physisch weit voneinander entfernt sind.


IP-Adressen können im Wesentlichen auf zwei Arten zugewiesen werden:


- Statisch**: Manuell auf dem Gerät eingestellt.
- Dynamisch**: Automatische Zuweisung bei Bedarf durch einen DHCP-Server (_Dynamic Host Configuration Protocol_). DHCP vereinfacht die Netzwerkverwaltung, da die Notwendigkeit einer manuellen Konfiguration entfällt und gleichzeitig eine präzise Steuerung durch Reservierungen und Lease-Dauern ermöglicht wird.


**IPv4**-Adressen werden in einem **32-Bit**-Format geschrieben, das in **vier Bytes** unterteilt ist. Jedes Byte enthält 8 Bits und stellt eine Dezimalzahl von 0 bis 255 dar. Die 4 Bytes werden durch Punkte getrennt, um eine klare, lesbare Schreibweise zu gewährleisten.


beispiel: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Jedes Bit in einem Byte hat einen Wert (oder eine "Gewichtung"): das linke Bit (das höchstwertige Bit) hat den Wert 128, das nächste 64, dann 32, 16, 8, 4, 2 und 1 für das rechte Bit (das niedrigstwertige Bit). Auf diese Weise wird die Binärschrift durch einfache Addition der eingestellten Gewichte in die Dezimalschrift umgewandelt.


Die nachstehende Tabelle veranschaulicht diesen Zusammenhang:



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

Zur Umwandlung von Binär- in Dezimalzahlen addiert man die Gewichte der Bits, die auf 1 gesetzt sind.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

Eine IP Address identifiziert ein einzelnes **Netzwerk Interface**, nicht das gesamte Gerät. Ein Router oder eine Firewall mit mehreren Anschlüssen hat mehrere Schnittstellen, jede mit einem eigenen IP-Address. Ein Interface kann sogar mehrere IP-Adressen haben (z. B. um mehrere virtuelle Netze oder Dienste zu bedienen).


Jedes IP-Paket enthält zwei IP-Adressen in seinem Header:


- Die Quelle Address (**Absender**)
- Das Ziel Address (**Empfänger**)

Router lesen diese Adressen, um den besten Weg für das Paket zu finden, bis es das Ziel erreicht. Ohne strenge Adressierungsregeln könnte der Netzverkehr nicht korrekt weitergeleitet werden, und eine globale Zusammenschaltung von Netzen wäre unmöglich.


Ein IPv4 Address besteht aus zwei Teilen:


- NetID**: identifiziert das Netz
- HostID**: identifiziert ein Gerät innerhalb dieses Netzes

Die **Subnetzmaske** bestimmt, wo die NetID endet und die HostID beginnt, und gibt an, wie viele Bits zu jedem Teil gehören. Je länger die NetID ist, desto größer ist die Anzahl der möglichen Subnetze, aber die Anzahl der Hosts pro Subnetz sinkt entsprechend.


Ursprünglich waren die IPv4-Netze in fünf **Klassen** unterteilt: (A, B, C, D und E). Jede Klasse entspricht einem bestimmten NetID-Bereich und definiert eine feste Granularität:


- Klasse A: sehr große Netze mit einer großen Anzahl von Hosts
- Klasse B: mittlere Netzwerke
- Klasse C: kleine Netzwerke
- Klasse D: für Multicasting reservierte Adressen (_multicast_)
- Klasse E: experimentelle Adressen, die nicht für die konventionelle Adressierung verwendet werden



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Besondere Ansprachen:


- Netzwerk Address**: Identifiziert das Netz selbst (wird in Routing-Tabellen verwendet).
- Rundruf Address**: Sendet Daten an alle Geräte im Subnetz auf einmal (alle HostID-Bits auf 1 gesetzt).


Die folgenden Bereiche sind für den internen Gebrauch reserviert:


- 10.0.0.0/8** (Privat Klasse A)
- 127.0.0.0/8** (lokaler Loopback oder _Loopback_)
- 172.16.0.0 bis 172.31.255.255** (private Klasse B)
- 192.168.0.0 bis 192.168.255.255** (privat Klasse C)


Die Adressen **127.0.0.1** und, allgemeiner, der gesamte Bereich 127.0.0.0/8 werden für interne Tests verwendet: Jede Anfrage, die an diese Adresse gesendet wird, verlässt den Rechner nicht. Dies ist nützlich, um zu prüfen, ob ein lokaler Netzwerkdienst funktioniert, ohne das größere Netzwerk einzubeziehen.


Um den Address-Raum besser zu nutzen, teilen Administratoren Netzwerke oft in **Subnetze** auf, indem sie Subnetzmasken oder die **CIDR**-Notation (_Classless Inter-Domain Routing_) verwenden. CIDR ermöglicht eine präzisere Verwaltung und hilft, die Verschwendung von Adressen zu vermeiden. Heute ist CIDR für die Feinabstimmung von IP-Bereichen und die Verringerung der Größe von Routing-Tabellen unerlässlich.


In modernen Netzen ist die IP-Adressierung in der Regel mit anderen Identifikatoren gekoppelt:



- domänenname**, der in einem **DNS** (_Domain Name System_) registriert ist: Es verbindet eine numerische IP Address mit einem menschenfreundlichen Namen.
- MAC Address**: eine in die Netzwerkkarte eingravierte physikalische Kennung, die für den lokalen Transport (_Ethernet_) verwendet wird. Wenn ein IP-Paket physisch übertragen werden muss, gleicht die ARP-Tabelle die IP-Address mit der MAC-Address des Ziels ab.


Um die IPv4 Address-Knappheit zu beheben und ein Layer an Sicherheit hinzuzufügen, verwenden Netzwerke oft Address-Übersetzung (_NAT_). NAT ermöglicht es vielen privaten Geräten, beim Zugriff auf das Internet eine einzige öffentliche IP Address zu nutzen.


**Anmerkung**: Online- und eingebaute Betriebssystem-Tools wie der [Grenoble CRIC Calculator] (http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/) erleichtern die Berechnung von Subnetzen und Masken erheblich.

Diese Dienstprogramme helfen bei der effizienten Planung der Netzaufteilung.


Zusammenfassend lässt sich sagen, dass der Address-Rundruf eine praktische Funktion ist, um dieselbe Nachricht an alle mit einem Segment verbundenen Geräte zu senden: Dies wird erreicht, indem alle Bits im HostID-Teil auf 1 gesetzt werden, so dass alle Hosts angesprochen werden.



## Die verschiedenen Typen von IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



IPv4-Adressen lassen sich in zwei Hauptkategorien einteilen: öffentliche Adressen, die direkt über das Internet zugänglich sind, und private Adressen, die für die interne Nutzung innerhalb eines lokalen Netzes bestimmt sind.


Ein öffentlicher IPv4 Address ist weltweit eindeutig und kann über das Internet geroutet werden. Er wird von offiziellen Behörden zugewiesen und ist für öffentlich zugängliche Dienste wie Websites, E-Mail-Server oder Cloud-Infrastrukturen erforderlich.

Die weltweite Eindeutigkeit dieser Adressen ist wichtig, um Routing-Konflikte oder Kollisionen zu vermeiden.


Die **IANA** (_Internet Assigned Numbers Authority_), die der **ICANN** (_Internet Corporation for Assigned Names and Numbers_) untersteht, verwaltet die Verteilung dieser IP-Bereiche. Konkret unterteilt die IANA den IPv4-Raum in 256 Blöcke der Größe /8 gemäß der CIDR-Notation. Jeder Block entspricht etwas mehr als 16,7 Millionen Adressen (2³² / 2⁸).


Diese Unicast-Address-Blöcke werden von der IANA den **Regionalen Internet-Registern** (RIRs) anvertraut. Diese RIRs sind für die Neuverteilung der Adressen auf regionaler Ebene entsprechend dem tatsächlichen Bedarf von Zugangsanbietern, Unternehmen oder Verwaltungen zuständig. Der Unicast-Address-Raum erstreckt sich von den Blöcken **1/8 bis 223/8**, wobei Teile davon entweder für besondere Zwecke (Forschung, Dokumentation, Tests) reserviert sind oder direkt einem Netz oder RIR zur Weiterverteilung zugewiesen werden.


Um zu prüfen, wem eine öffentliche IP Address gehört, können Sie die RIR-Datenbanken mit dem Befehl **whois** oder die von den einzelnen Registern bereitgestellten Webschnittstellen nutzen. Mit diesen Werkzeugen lässt sich die Address bis zu der Organisation oder dem Anbieter zurückverfolgen, die/der sie angemeldet hat.


Umgekehrt gibt es private IPv4-Adressen, eine praktische Reaktion auf den Mangel an öffentlichen Adressen. Diese Adressen, die nicht über das Internet geroutet werden können, sind für lokale Umgebungen reserviert: Unternehmensnetze, Heim-LANs, Rechenzentren oder Computer-Cluster. Sie sind nicht weltweit einmalig: Viele private Netze können dieselben IP-Bereiche wiederverwenden, ohne dass es zu Störungen kommt, solange sie isoliert bleiben oder ein Netzwerk-Address-Übersetzungsgerät für den Zugang zum Internet verwenden.


Um einem Gerät mit einer privaten IP Address den Zugang zum Internet zu ermöglichen, verwenden Netzwerke NAT (Network Address Translation). NAT funktioniert, indem das private Address dynamisch durch ein öffentliches ersetzt wird, so dass Dutzende (oder sogar Hunderte) von Geräten eine einzige öffentliche IP Address gemeinsam nutzen können. Diese Methode optimiert die Nutzung des IPv4-Speicherplatzes und bietet außerdem ein Layer an Sicherheit, da die interne Netzstruktur verborgen wird.


Eine weitere spezielle Kategorie sind **unspezifizierte** Adressen. Die IPv4-Notation **0.0.0.0** oder ihre IPv6-Version **::/128** bedeutet "kein bestimmter Address". Ein solcher Address ist als Netzwerk-Address-Ziel ungültig, kann aber lokal von einem Host verwendet werden, um "alle Schnittstellen" oder "noch kein Address zugewiesen" anzuzeigen. Dies ist bei dynamischen DHCP-Assignment oder beim Abhören aller Serverschnittstellen üblich.


IPv6 unterstützt auch die private Adressierung, aber der Standard empfiehlt im Allgemeinen die öffentliche Adressierung, um die Überlagerung mehrerer NAT-Schichten zu vermeiden. Die **site-local-Adressen** (_site-local_) des **fec0::/10**-Blocks wurden mit **RFC 3879** aus Konsistenz- und Sicherheitsgründen veraltet. Sie wurden durch **Unique Local Addresses** (_ULA_) ersetzt, die sich im **fc00::/7**-Block befinden. ULAs ermöglichen die Einrichtung privater IPv6-Netze mit sauberem internem Routing, wobei eine zufällig erzeugte 40-Bit-Kennung verwendet wird, um die lokale Eindeutigkeit zu gewährleisten.


Die Erschöpfung von IPv4 wurde im Jahr 2011 offiziell bestätigt. Um seine Lebensdauer zu verlängern, hat die Internet-Gemeinschaft mehrere Strategien entwickelt:


- Schrittweise Umstellung auf **IPv6**
- Weitverbreitete Verwendung von **NAT**
- Strengere Zuteilungspolitik der RIRs, die eine genaue Rechtfertigung und Verwaltung des Address-Bedarfs erfordern
- Rückgewinnung von nicht verwendeten oder freiwillig zurückgegebenen Address-Blöcken durch Unternehmen


Diese Maßnahmen zeigen, dass die IP-Adressierung nicht nur eine technische Herausforderung ist, sondern auch eine Frage der globalen Governance, die für die weitere Expansion des Internets von zentraler Bedeutung ist.



## DNS, ein Address-Verzeichnis


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Seien wir ehrlich: Menschen sind nicht besonders gut darin, sich lange Zahlenfolgen zu merken, egal ob in binärer oder dezimaler Form. Diese Herausforderung wird bei IP-Adressen noch größer, da diese komplex sein können und eine einzige IP Address manchmal mehrere Adressen maskieren kann, insbesondere wenn Techniken wie NAT oder virtuelles Hosting im Spiel sind.


Um die Sache zu vereinfachen, verwendet die Anwendung Layer ein System, das einen IP Address mit einem logischen, von Menschen lesbaren Namen verbindet. Dies ist die Aufgabe von **DNS** (*Domain Name System*), einem massiven, hierarchischen, verteilten Verzeichnis, das lesbare Domänennamen mit IP-Adressen verknüpft. Das System basiert auf einer Reihe von Protokollen und Diensten. Die am weitesten verbreitete DNS-Server-Software ist **BIND** (_Berkeley Internet Name Domain_), ein Open-Source-Softwarepaket, das auf einen Großteil der DNS-Infrastruktur des Internets verweist.


Die Grundidee von DNS ist einfach: Für jeden angeschlossenen Dienst, sei es eine Website, ein Mailserver oder ein anderer Netzwerkdienst, gibt es einen Eintrag, der einen Domänennamen einer oder mehreren IP-Adressen zuordnet. Dies funktioniert in zwei Richtungen:


- Weiterleitungsauflösung: Übersetzung eines Namens in eine IP Address.
- Rückwärtsauflösung: Auffinden des Domänennamens, der mit einer bestimmten IP Address verbunden ist.

Dadurch wird die Netzwerkadressierung für Menschen nutzbar, während die Präzision, die Router für die korrekte Datenübertragung benötigen, erhalten bleibt.


Ein Domänenname ist immer hierarchisch aufgebaut, wobei jede Ebene durch einen Punkt getrennt ist: Der vollständige Name wird **FQDN** (_Fully Qualified Domain Name_) genannt. Der ganz rechte Teil ist die **TLD** (_Top Level Domain_) wie z.B. `.com`, `.org` oder `.fr`. Der linke Teil bezeichnet den Host, d. h. den spezifischen Rechner oder Dienst, der mit dem IP Address verbunden ist.


Das DNS-System ist als **Baum von Zonen** konzipiert. Eine **Zone** ist ein Abschnitt des Domain-Namensraums, der von einem bestimmten DNS-Server verwaltet wird. Eine einzelne Zone kann mehrere **Subdomains** enthalten, die ihrerseits an andere Zonen delegiert werden können, die von verschiedenen Servern verwaltet werden. Administratoren sind für die Verwaltung ihrer Zonen verantwortlich: Sie kümmern sich um Aktualisierungen, Delegierungen und die allgemeine Verwaltung.


Diese Struktur erlaubt nicht nur den Verweis auf eine Hauptdomäne (z.B. `example.com`), sondern auch die Feinabstimmung von Einträgen für einzelne Hosts (`www`, `mail`, `ftp`, usw.). In den Anfängen der Netzwerktätigkeit wurde diese Zuordnung mit statischen Dateien (z. B. `/etc/hosts` auf Unix-Systemen) gehandhabt, aber eine solche Methode wurde für ein schnell wachsendes, vernetztes Internet schnell unpraktisch.


Es ist wichtig zu verstehen, dass ein **DNS-Server** nur einen begrenzten Bereich bedienen kann. Der interne DNS-Server eines Unternehmens kann beispielsweise nicht direkt aus dem Internet erreichbar sein. Wenn dieser DNS nicht für die Weiterleitung von Abfragen konfiguriert ist oder keine vertrauenswürdige Beziehung zu anderen Servern hat, werden einige Abfragen fehlschlagen: Weder der Name noch die IP Address können dann außerhalb der definierten Zone aufgelöst werden.


DNS spielt auch beim E-Mail-Routing eine Rolle. Ein **MX** (_Mail Exchange_)-Eintrag gibt zum Beispiel die Mailserver an, die für den Empfang von E-Mails für eine bestimmte Domäne zuständig sind. Diese Einträge definieren Prioritäten (Gewichtungsfaktor) und Failover-Lösungen. Die Zonendatei eines DNS-Servers muss einen **SOA** (_Start Of Authority_)-Eintrag enthalten, der den Server als offizielle Informationsquelle für diese Zone angibt.


Dank seiner hierarchischen, verteilten Struktur ist das DNS nach wie vor ein Eckpfeiler des Internets, da es den Nutzern den Zugang zu Diensten über eindeutige, einprägsame Domänennamen anstelle langer, technischer IP-Adressen ermöglicht.


Im nächsten Kapitel werden wir uns mit einem weiteren grundlegenden Konzept befassen: **Ethernet-Adressen**, auch bekannt als **MAC-Adressen**, die die Datenübertragung am physikalischen Layer lokaler Netzwerke sicherstellen.



## Erkennung von Ethernet-Adressen und ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definitionen


Damit das Datenweiterleitungsprotokoll zuverlässig und konsistent funktioniert, ist eine Schlüsselkomponente unerlässlich. Als Menschen können wir einen Rechner leicht anhand seiner IP Address oder seines über DNS abgerufenen Namens identifizieren. Ein Rechner muss jedoch in der Lage sein, das Zielgerät eindeutig zu erkennen, um Pakete zuzustellen. Dazu ist er auf eine bestimmte Hardware-Kennung angewiesen, die direkt von seinem Netzwerk Interface verwendet wird: die MAC Address (_Media Access Control_).


**Anmerkung**: Dies hat nichts mit einem "physischen Address" in der Speicherarchitektur zu tun. In der Computertechnik bezieht sich ein physischer Address auf einen bestimmten Speicherplatz auf dem Speicherbus, im Gegensatz zu einem virtuellen Address, der vom Betriebssystem verwaltet wird. Ein MAC-Address hingegen bezieht sich ausschließlich auf die Netzwerkhardware.


Ein MAC Address wird vom Hersteller des Geräts dauerhaft und eindeutig zugewiesen. Der MAC Address identifiziert die Netzwerkkarte eindeutig, egal ob es sich um einen Computer, ein Smartphone, einen Drucker oder ein anderes angeschlossenes Gerät handelt. Im Gegensatz zu einem IP-Address, der sich dynamisch ändern kann (über einen DHCP-Server oder eine manuelle Konfiguration), bleibt der MAC-Address normalerweise während der gesamten Lebensdauer des Geräts gleich, es sei denn, er wird absichtlich geändert.


Jedes Netz Interface, ob drahtgebunden oder drahtlos, hat seinen eigenen MAC Address. Diese Address wird innerhalb der Datenverbindung Layer (Layer 2 des OSI-Modells) verwendet, um die Hardware Address in jeden ausgetauschten Netzwerkrahmen einzufügen und zu verwalten. Sie wird manchmal auch als _Ethernet-Adresse_ oder _UAA_ (_Universally Administered Address_) bezeichnet. Sie ist standardisiert auf eine Länge von 48 Bits oder 6 Bytes und wird in hexadezimaler Notation geschrieben, im Allgemeinen in Form von Bytes, die durch `:` oder `-` getrennt sind.


Zum Beispiel: "5A:BC:17:A2:AF:15"


In dieser Struktur bezeichnen die ersten drei Bytes den Hersteller der Netzwerkkarte: Dies wird als **OUI** (*Organisationally Unique Identifier*) bezeichnet. Diese von der IEEE zugewiesenen Präfixe werden auch in anderen Hardware-Adressierungssystemen wie Bluetooth und LLDP verwendet, um weltweite Eindeutigkeit zu gewährleisten.


### Ändern eines MAC Address (MAC-Spoofing)


Theoretisch ist der MAC Address so konzipiert, dass er fest bleibt, aber es gibt Möglichkeiten, ihn zu verändern, insbesondere um bestimmte Anforderungen zu erfüllen oder bestimmte Beschränkungen zu umgehen. Bei diesem Vorgang, der oft als _spoofing MAC_ bezeichnet wird, wird der ursprüngliche Hardware-Address durch einen anderen Wert ersetzt, der auf Softwareebene definiert wird. Einige Betriebssysteme erleichtern diese Änderung, insbesondere wenn der eigentliche Ethernet-Address nicht direkt vom Treiber verwendet wird.


Die Gründe für eine solche Änderung sind vielfältig. Es könnte die Notwendigkeit sein, dass eine bestimmte Anwendung ein bestimmtes Ethernet Address benötigt, um korrekt zu funktionieren, oder um einen Konflikt identischer Adressen zwischen zwei Geräten zu lösen, die dasselbe lokale Netzwerk nutzen.


Die Änderung des MAC Address kann auch durch Überlegungen zum Schutz der Privatsphäre motiviert sein: Durch das Verbergen der auf der Karte eingravierten eindeutigen Kennung verringern die Nutzer die Möglichkeit, dass ihr Gerät von Netzen oder Überwachungsdiensten verfolgt wird. Diese Praxis ist jedoch nicht ohne Folgen. Die Änderung eines MAC Address kann bestimmte Filtergeräte stören oder eine Neukonfiguration der Firewalls erfordern, um die neue Hardware zuzulassen.


Einige Netzwerke, insbesondere Wi-Fi, verwenden MAC Address-Filterung, um nur Geräte mit zugelassenen Adressen zuzulassen. Dies bietet zwar ein grundlegendes Maß an Kontrolle, ist aber für sich genommen nicht sicher. Ein Angreifer kann einen gültigen MAC Address abfangen, der bereits im Netzwerk zugelassen ist, und ihn klonen, um die Beschränkungen zu umgehen. Aus diesem Grund sollte die MAC-Filterung immer mit stärkeren Sicherheitsmaßnahmen kombiniert werden.


### MAC/IP-Korrespondenz


Damit ein lokales Netz effizient funktioniert, muss es eine klare Zuordnung zwischen physischen Adressen (MAC-Adressen) und logischen Adressen (IP-Adressen) geben. Ohne diese Verbindung könnte ein Computer zwar die IP Address eines Ziels kennen, wüsste aber nicht, wie er physisch Daten an dieses Ziel im lokalen Netz senden kann.

Diese Zuordnung wird automatisch durch das ARP (_Address Resolution Protocol_) vorgenommen.


In der Praxis kann ein Benutzer, der wissen möchte, welcher MAC Address einem bestimmten IP Address entspricht, das Dienstprogramm `arp` verwenden. Dieses Tool überprüft die lokale ARP-Tabelle des Rechners, um bekannte Übereinstimmungen zwischen IP-Adressen und MAC-Adressen im lokalen Netz anzuzeigen. Auf diese Weise ist es möglich, die effektive Verbindung zwischen der logischen und der physikalischen Schicht schnell zu überprüfen.


Praktisches Beispiel: Wenn Sie prüfen wollen, welche Netzwerkkarte der IP Address `192.168.1.5` entspricht, verwenden Sie folgenden Befehl:


```bash
arp –a 192.168.1.5
```


Die Ausgabe zeigt den zugehörigen physischen Address (MAC), die Art der Eingabe (statisch oder dynamisch) und den betreffenden Interface an.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Es ist wichtig, sich daran zu erinnern, dass der MAC Address und der IP Address zwei völlig unterschiedliche Kennungen sind, die sich jedoch eng ergänzen. Der MAC Address wird vom Hersteller eindeutig in jedes Netzwerk-Interface eingraviert und dient zur physischen Identifizierung des Geräts im lokalen Netzwerk. Der IP-Address hingegen ist ein logischer Address, der entweder dynamisch oder statisch zugewiesen wird und es dem Gerät ermöglicht, dem IP-Netz beizutreten und Exchange-Pakete über sein lokales Netz hinaus zu senden.



- Visuelles Beispiel des MAC Address:


![Image](assets/fr/032.webp)




- Visuelles Beispiel für einen IP Address:


![Image](assets/fr/027.webp)



In einer Unternehmensumgebung können diese beiden Adressierungsebenen nicht getrennt voneinander funktionieren. Wenn zum Beispiel ein DHCP-Server automatisch eine IP Address zuweist, wird die MAC Address des Geräts als Ausgangspunkt verwendet. Der Computer sendet eine DHCP-Broadcast-Anfrage mit seiner MAC Address, damit der Server dem richtigen Gerät eine verfügbare IP Address zuweisen kann. Ohne diese Hardware-Identifikation wüsste der DHCP-Server nicht, welchem Gerät er den Address zuweisen soll.


Das ARP-Protokoll ist daher von grundlegender Bedeutung: Es stellt die Verbindung zwischen IP-Adressen und physischen Adressen her und ermöglicht es Rechnern, ein logisches Ziel in ein tatsächliches physisches Ziel zu übersetzen. Wenn ein Computer ein Paket an einen Rechner im selben Netz senden möchte, konsultiert er zunächst seine ARP-Tabelle, um zu prüfen, ob die MAC Address des Empfängers bereits bekannt ist. Ist dies nicht der Fall, sendet er eine ARP-Anfrage an alle Rechner im lokalen Netz. Der Rechner, der die Ziel-IP Address in dieser Anfrage erkennt, antwortet, indem er seine MAC Address angibt. Der Absender schreibt dann dieses IP/MAC-Paar in seinen ARP-Cache, um zu vermeiden, dass er den Vorgang jedes Mal wiederholen muss, wenn die Anfrage gesendet wird.


Diese ARP-Tabelle fungiert als ein Mini-Mapping-Verzeichnis, das dynamisch aktualisiert wird, ähnlich wie DNS Domänennamen mit IP-Adressen verbindet. Ohne ARP wäre kein lokaler Exchange möglich, da der Data Link Layer die MAC Address kennen muss, um Ethernet-Frames korrekt zu kapseln.


Umgekehrt wurde das RARP-Protokoll (_Reverse Address Resolution Protocol_) für die entgegengesetzte Situation entwickelt: Es ermöglicht einem Rechner, der nur seinen MAC-Address kennt, seinen IP-Address zu ermitteln. Dies war häufig bei älteren Workstations ohne lokale Hard-Platte der Fall, die über das Netzwerk booten und einen IP-Address anfordern mussten. RARP wurde schließlich durch **BOOTP** und dann **DHCP** ersetzt, die flexibler und automatisierter sind.


Diese Assoziierungsprotokolle spielen eine wichtige Rolle beim Routing. Ein Router ist im Wesentlichen ein Gerät mit mehreren Netzwerkschnittstellen, die verschiedene Segmente miteinander verbinden. Wenn ein Router einen Rahmen empfängt, verarbeitet er ihn, um das IP-Datagramm zu extrahieren, und prüft den IP-Header, um das Ziel zu bestimmen. Befindet sich das Ziel in einem direkt angeschlossenen Netz, wird das Datagramm nach Aktualisierung des Headers direkt zugestellt. Gehört das Ziel zu einem anderen Netz, konsultiert der Router seine Routing-Tabelle, um den besten Pfad oder _next hop_ zum Ziel zu ermitteln.


Dadurch wird die Route in kürzere, besser zu handhabende Segmente unterteilt. Jeder zwischengeschaltete Router kennt nur den nächsten Schritt, nicht unbedingt das endgültige Ziel.


**Erinnerung:** Die direkte Zustellung erfolgt, wenn sich Absender und Empfänger im selben physischen Netz befinden. Andernfalls ist die Zustellung indirekt und erfolgt über einen oder mehrere Router.


Die Routing-Tabelle, die entweder manuell (statisches Routing) oder dynamisch (dynamisches Routing) verwaltet wird, enthält die Informationen, die für die Entscheidung über die zu wählende Route erforderlich sind. In kleinen Netzen ist eine statische Konfiguration ausreichend. In größeren Infrastrukturen ist dynamisches Routing unerlässlich, um die Routen automatisch anzupassen, wenn sich die Topologie ändert oder eine Verbindung ausfällt.


Die Routing-Tabelle dient als Zuordnungstabelle zwischen Ziel-IP-Adressen und nächsten Gateways. Sie speichert in der Regel Netzkennungen (_Netz-ID_) und nicht jeden einzelnen Host Address, was ihre Größe erheblich reduziert.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Anhand dieser Einträge kann der Router schnell feststellen, über welchen Interface und an welchen Knoten jedes Datagramm gesendet werden soll. In Kombination mit ARP zur Auflösung der passenden MAC-Adressen sorgt dies für eine effiziente und zuverlässige Datenübertragung im Netz.


Zu den dynamischen Routing-Protokollen gehören Standards wie RIP (_Routing Information Protocol_), das auf dem Distanzalgorithmus basiert, und OSPF (_Open Shortest Path First_), das die kürzesten Wege in einer komplexen Topologie berechnet. Diese Protokolle führen ständig Exchange-Updates durch, um die Routen zu optimieren, die Übertragungskosten zu senken und die Widerstandsfähigkeit gegen Ausfälle oder Überlastungen zu verbessern.



## NAT: Address Übersetzung


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definition


Network Address Translation_ (NAT) ist eine Technik, die entwickelt wurde, um Address die allmähliche Erschöpfung der verfügbaren IPv4-Adressen zu verhindern. NAT wurde als Zwischenlösung vor der weit verbreiteten Einführung von IPv6 entwickelt und ermöglichte es Unternehmen und Einzelpersonen, weiterhin eine große Anzahl von Rechnern anzuschließen und dabei nur eine begrenzte Anzahl öffentlicher IP-Adressen zu verwenden.


**Wichtige Erinnerung:** Der Übergang von IPv4 zu IPv6 löst theoretisch das Erschöpfungsproblem, indem der Address-Raum von 32 Bit auf 128 Bit erweitert wird, was eine nahezu unbegrenzte Anzahl von Adressen (2^128) ermöglicht. In der Praxis ist die Umstellung jedoch noch unvollständig, und NAT wird auch heute noch häufig verwendet.


Das Prinzip von NAT ist einfach, aber höchst effektiv: Statt jedem Gerät im internen Netz eine eindeutige öffentliche IP Address zuzuweisen, wird für alle privaten Geräte eine einzige routingfähige Address (oder ein kleiner Pool von Adressen) verwendet. Das NAT-Gateway, das häufig in den Router oder die Firewall integriert ist, übersetzt dann dynamisch die interne IP Address zusammen mit den Informationen, die für die korrekte Weiterleitung des Datenverkehrs nach außen erforderlich sind, und sorgt dafür, dass Antworten an den ursprünglichen Absender zurückgesendet werden.


Dieser Ansatz hat einen unmittelbaren Vorteil: Er verbirgt die interne Netzarchitektur vollständig. Für einen außenstehenden Beobachter scheinen alle Anfragen von Arbeitsstationen, Servern oder Druckern von der gleichen öffentlichen Identität zu kommen. Private Adressen, die in der Regel aus reservierten Bereichen stammen (z. B. 192.168.x.x oder 10.x.x.x), bleiben für das Internet unsichtbar.


Neben der Behebung der IPv4-Knappheit stärkt NAT auch die Sicherheit, indem es eine erste logische Barriere zwischen dem internen und dem öffentlichen Netz schafft. Unerwünschte eingehende Mitteilungen werden natürlich blockiert, da nur Verbindungen, die von innerhalb des Netzes initiiert werden, von der notwendigen Übersetzung profitieren, um Antworten zu erhalten.



![Image](assets/fr/035.webp)



### Arten der Übersetzung


NAT kann auf unterschiedliche Weise implementiert werden, um den spezifischen Anforderungen gerecht zu werden. Die beiden Hauptbetriebsarten sind statische und dynamische Übersetzung.


*die *statische Übersetzung** schafft eine feste Zuordnung zwischen einem privaten IP-Address und einem öffentlichen IP-Address. Jeder interne Rechner ist permanent mit seinem dedizierten öffentlichen Address verbunden. Beispielsweise könnte ein internes Gerät, das als 192.168.20.1 konfiguriert ist, mit dem routingfähigen Address 157.54.130.1 verbunden sein. Wenn ein ausgehendes Paket das lokale Netzwerk verlässt, ersetzt der Router den Quell-Address des Pakets durch den öffentlichen Address und führt den umgekehrten Vorgang für den eingehenden Verkehr durch. Diese bidirektionale Übersetzung ist für den Benutzer transparent.


**Warnung:** Diese Methode isoliert zwar das interne Netz, löst aber nicht den Mangel an öffentlichen IP-Adressen, da Sie immer noch so viele öffentliche Adressen benötigen, wie es Rechner gibt, die Sie freigeben müssen. Die statische Übersetzung wird daher hauptsächlich verwendet, wenn bestimmte interne Ressourcen von außen erreichbar bleiben müssen (Webserver, Mailserver...).


*bei der *Dynamischen Übersetzung** wird dagegen ein Pool öffentlicher IP-Adressen verwendet. Wenn ein interner Host eine Verbindung aufbaut, weist der Router vorübergehend eine dieser öffentlichen Adressen dem privaten Address des Hosts für die Dauer der Sitzung zu. Die Verbindung ist 1-zu-1, aber temporär: Sobald die Verbindung endet, wird der öffentliche Address für ein anderes Gerät verfügbar. Dynamisches NAT reduziert also die Anzahl der öffentlichen Adressen, die benötigt werden, wenn nicht alle Rechner gleichzeitig online sind, aber es erfordert immer noch einen Block externer Adressen, der mindestens so groß ist wie die maximale Anzahl gleichzeitiger Verbindungen.


*die *Port-Übersetzung** (PAT), auch bekannt als *NAT-Überlastung* oder *IP-Masquerading*, geht noch einen Schritt weiter: Alle privaten Geräte teilen sich eine einzige öffentliche IP Address (oder eine sehr kleine Zahl). Um Sitzungen zu unterscheiden, ändert das Gateway nicht nur den Quell-Address, sondern auch den Quell-Port. Es führt eine Tabelle, die jedes Paar *(private Address, privater Port)* mit einem eindeutigen Paar *(öffentliche Address, öffentlicher Port)* verknüpft. Diese Form von NAT wird in fast allen Heimroutern verwendet und ermöglicht es Dutzenden von Geräten (Computern, Smartphones, angeschlossenen Objekten usw.), sich dieselbe öffentliche IP Address zu teilen, während die Kommunikation flüssig bleibt.


NAT verlängert also die Lebensdauer von IPv4 und bietet gleichzeitig einen wertvollen Layer an Segmentierung und Sicherheit. Mit der zunehmenden Verbreitung von IPv6 und seinem riesigen Address-Raum wird die Rolle von NAT wahrscheinlich abnehmen, auch wenn es aus Kompatibilitäts- und Kontrollgründen in einigen Umgebungen weiterhin zur Segmentierung und Filterung des Datenverkehrs eingesetzt wird.


### NAT-Implementierung


Um den ordnungsgemäßen Betrieb der Address-Übersetzung zu gewährleisten, muss der NAT-Router oder -Gateway eine genaue Aufzeichnung der Zuordnungen führen, die zwischen jedem privaten Address im internen Netz und dem öffentlichen Address, den er für die Kommunikation mit der Außenwelt verwendet, erstellt wurden. Diese Informationen werden in der so genannten "NAT-Übersetzungstabelle" gespeichert, die eine zentrale Rolle bei der Verwaltung des Netzwerkverkehrs spielt.


Jeder Eintrag in dieser Tabelle verknüpft mindestens ein Paar: den internen IP-Address des sendenden Rechners und den externen IP-Address, der im Internet zu sehen ist. Wenn ein Paket aus dem privaten Netz an ein öffentliches Ziel gesendet wird, fängt der NAT-Router den Rahmen ab, analysiert die IP- und TCP/UDP-Header und ersetzt dann den privaten Quell-Address durch den öffentlichen Address des Gateways. Auf dem Rückweg fängt dasselbe Gateway das eingehende Paket ab, prüft die Zuordnungstabelle und führt den umgekehrten Vorgang durch, um den Datenstrom an den ursprünglichen internen IP-Address umzuleiten.


Dieses dynamische Übersetzungsprinzip beruht auf einer präzisen Tabellenverwaltung: Jeder Eintrag bleibt so lange gültig, wie aktiver Verkehr vorliegt, der ihn rechtfertigt. Nach einer konfigurierbaren Zeit der Inaktivität wird der Eintrag gelöscht und kann für neue Verbindungen wieder verwendet werden.


beispiel für eine vereinfachte NAT-Übersetzungstabelle:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

Wenn in diesem Beispiel für den zweiten Eintrag seit über einer Stunde (3.600 Sekunden) kein Paket mehr durchgelassen wurde, wird er als wiederverwendbar markiert. Umgekehrt zeigt eine Dauer von Null eine aktive Kommunikation an, wobei die Zuordnung gesperrt ist.


Während NAT für die meisten gängigen Anwendungen (Web-Browsing, E-Mail, Dateiübertragung usw.) transparent funktioniert, kann es für bestimmte Netzwerkanwendungen zusätzliche Herausforderungen mit sich bringen. Einige Technologien beruhen auf dem expliziten Austausch von IP-Adressen oder Ports innerhalb der Nutzlast der Pakete. Nach dem Durchlaufen eines NAT-Gateways werden diese Informationen inkonsistent.


Typische Beispiele für Einschränkungen sind:


- Peer-to-Peer-Protokolle (P2P), die direkte Verbindungen zwischen Geräten erfordern, werden durch die NAT-Barriere behindert, da alle internen Rechner dieselbe externe IP Address nutzen und ohne spezielle Konfiguration (wie *Port Forwarding* oder UPnP) nicht direkt erreichbar sind;
- Das IPSec-Protokoll, das zur Sicherung der Netzkommunikation verwendet wird, verschlüsselt die Paket-Header. Da NAT diese Header ändern muss, um IP-Adressen zu ersetzen, macht die Verschlüsselung dies ohne Anpassungsmechanismen wie NAT-T (*NAT Traversal*) unmöglich;
- Das X-Window-Protokoll, das die Fernanzeige von grafischen Anwendungen unter Unix/Linux ermöglicht, funktioniert so, dass der X-Server aktiv TCP-Verbindungen an Clients sendet. Diese Umkehrung der üblichen Richtung der Verbindungen kann durch NAT blockiert werden.


Im Allgemeinen ist jedes Protokoll betroffen, das explizit die interne IP Address in der Nutzlast des Pakets enthält, da diese Address nach der Übersetzung nicht mehr mit der realen, im Internet sichtbaren Address übereinstimmt.


**Wichtiger Hinweis:** Um diese Probleme zu lösen, bieten einige NAT-Router _Deep Packet Inspection_ (DPI) oder _Protocol Helpers_ an, die Paketinhalte untersuchen, um Adressen oder Portnummern in Anwendungsdaten zu identifizieren und dynamisch zu ersetzen. Dies erfordert eine eingehende Kenntnis des Protokollformats und kann zu Sicherheitslücken oder einem erhöhten Ressourcenverbrauch führen.


**Vorsicht:** Obwohl NAT dazu beiträgt, das interne Netz zu verbergen und den eingehenden Datenverkehr zu kontrollieren, ist es kein Ersatz für eine spezielle Firewall. Die Übersetzung allein ist keine vollständige Sicherheitsbarriere: Sie muss immer durch klare Filterregeln ergänzt werden, um unerwünschten oder ungewollten Verkehr zu blockieren.


um zu veranschaulichen, wie dies in der Praxis funktioniert, betrachten Sie das folgende Beispiel:_



![Image](assets/fr/037.webp)



In diesem Szenario kann eine interne Arbeitsstation auf den internen Webserver zugreifen, indem sie einfach die URL `http://192.168.1.20:80` aufruft. Die Angabe des Ports ist hier optional, da `80` der Standard-HTTP-Port ist. Wird dagegen eine Anfrage von außen initiiert, so gibt der Benutzer den öffentlichen Address `http://85.152.44.14:80` ein. Der NAT-Router empfängt die Anfrage, konsultiert seine Zuordnungstabelle und übersetzt automatisch den öffentlichen Address in einen privaten, indem er die Verbindung zu `http://192.168.1.20:80` umleitet.


Das gleiche Prinzip gilt für jeden anderen Server, der berechtigt ist, Internetverbindungen zu empfangen, wie z. B. den Extranet-Server (blauer Schaltkreis in der Abbildung).


**Praktischer Hinweis:** In virtualisierten Umgebungen werden häufig Netzwerkschnittstellen namens _virbrX_ (für _Virtual Bridge X_) verwendet. Diese virtuellen Brücken, die insbesondere von der libvirt-Bibliothek oder dem Xen-Hypervisor bereitgestellt werden, verbinden das virtuelle interne Netzwerk von Gastmaschinen mit dem physischen Netzwerk und wenden dabei NAT an. Sie werden im Allgemeinen über Skripte in `/etc/sysconfig/network-scripts/` konfiguriert, wie unten für `virbr0` gezeigt:


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


Sobald die virtuelle Brücke eingerichtet ist, müssen Sie das IP-Routing aktivieren und die Port-Übersetzung mit "iptables" konfigurieren:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Bei dieser Konfiguration wird der ausgehende Datenverkehr geroutet und die NAT-Übersetzung angewendet, so dass die virtuellen Maschinen mit der Außenwelt kommunizieren können, ohne ihre internen IP-Adressen direkt preiszugeben.


Im nächsten Kapitel werden wir uns ausführlich mit der IP Address-Konfiguration unter Linux befassen und dabei sowohl einfache als auch fortgeschrittene Methoden für verschiedene Verwaltungskontexte behandeln.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Wie konfiguriere ich das Netzwerk mit "ip"?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Standard-Konfiguration


Nachdem wir die theoretischen Grundlagen des Netzwerks behandelt und verstanden haben, wie IP-Adressen, Masken, Routing und Übersetzung zusammenarbeiten, ist es an der Zeit, zur praktischen Konfiguration überzugehen. Unter GNU/Linux wird die Netzwerkeinrichtung jetzt mit dem Befehl **`ip`** (Paket _iproute2_) durchgeführt, der das ältere `ifconfig` ersetzt.


mit "IP" können Sie einen IP-Address zuweisen oder ändern, eine Maske ändern, einen Interface starten oder stoppen oder seinen Status jederzeit überprüfen.


**TIPS:** um alle Schnittstellen (aktiv oder nicht) anzuzeigen: `ip addr show`


Beispiel: Zuweisung eines statischen Address und Aktivierung von Interface


Address `192.168.1.2/24` zu Interface `eth0` hinzufügen:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Aktivieren Sie Interface:


```shell
ip link set dev eth0 up
```


Deaktivieren Sie denselben Interface:


```shell
ip link set dev eth0 down
```


Anzeige des Status eines bestimmten Interface:


```shell
ip addr show dev eth2
```


**Praktischer Tipp:** Mit `ip` erfordert das Hinzufügen eines zusätzlichen Address zu einem Interface nicht mehr das Suffix `:1`. Fügen Sie einfach eine weitere `ip addr add ...` Zeile hinzu:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Aktivierungsskripte: ifup / ifdown


Die Programme `ifup` und `ifdown` lesen statische Konfigurationsdateien aus `/etc/sysconfig/network-scripts/` (unter RHEL, CentOS, Rocky Linux, AlmaLinux...) oder `/etc/network/interfaces` (unter Debian/Ubuntu), um Schnittstellen sauber hoch- oder runterzufahren.


```shell
ifup eth1
ifdown eth2
```


Konfigurationsdateien (RHEL-ähnlich):


- /etc/sysconfig/network**: globale Einstellungen (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: spezifische Einstellungen für jedes Interface.


Statisches Beispiel (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


DHCP-Beispiel:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Dieser modulare Aufbau ist nach wie vor gültig und kann auf den aktuellen Systemen leicht automatisiert werden.


### Erweiterte Konfiguration: Bonding


In professionellen Umgebungen besteht das Ziel darin, die Kontinuität der Dienste zu gewährleisten und/oder die Bandbreite zu bündeln. *Bonding* (oder *Teaming* mit _teamd_) Mechanismen erfüllen diese Anforderungen: mehrere physische Schnittstellen funktionieren als ein einziger logischer Interface, der oft als "bond0" oder "team0" bezeichnet wird.



![Image](assets/fr/039.webp)



Voraussetzungen:


- Laden Sie das Modul "bonding" (oder verwenden Sie "teamd");
- Es müssen mindestens zwei physische Schnittstellen vorhanden sein.


#### Die verschiedenen gängigen Klebeverfahren:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Einrichten mit `ip link



- Deaktivieren Sie physische Schnittstellen:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Erstellen Sie das gebundene Interface:


```shell
ip link add bond0 type bond mode balance-alb
```



- Optionen nach der Erstellung konfigurieren


```shell
ip link set bond0 type bond miimon 100
```



- Weisen Sie MAC- und IP-Adressen zu:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Anbringen von Slave-Schnittstellen:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Bringen Sie alles wieder hoch:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Tipp:** um einen Slave zu lösen, ohne die Verbindung zu unterbrechen: `ip link set eth1 nomaster`


#### Permanente Konfiguration (RHEL-ähnlich)


Erstellen Sie drei Dateien in `/etc/sysconfig/network-scripts`:


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


Dann:


```shell
systemctl restart network
```


#### Zusätzliche IP Address (moderner Alias)


Mit "ip" können Sie einfach ein zweites Address an dasselbe Gerät anschließen:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Damit dieser Alias nach einem Neustart bestehen bleibt, fügen Sie entweder einen zweiten `IPADDR2=...` / `PREFIX2=...`-Block zu `ifcfg-eth0` hinzu, oder erstellen Sie eine neue *NetworkManager*-Verbindung über `nmcli`.


Dank `ip` und verwandter Befehle (`ip link`, `ip addr`, `ip route`) ist die Netzwerkkonfiguration konsistenter, skriptfähig und übersichtlich. Bonding ist eine Schlüsselkomponente von Hochverfügbarkeitsarchitekturen, und die Zuweisung mehrerer Adressen an einen einzigen Interface ist viel einfacher geworden.


Im nächsten Kapitel werden wir uns mit den Besonderheiten und der Implementierung der IPv6-Adressierung befassen.


# IPv6-Adressierung


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Normen und Definitionen


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Wir gehen nun zur nächsten Generation der IP-Adressierung über: dem IPv6-Protokoll, ursprünglich bekannt als IPng (_IP Next Generation_). Dieses Protokoll wurde entwickelt, um die strukturellen Beschränkungen von IPv4 zu überwinden, und führt eine stark erweiterte Adressierungsarchitektur sowie zahlreiche technische Optimierungen ein.


Die Beweggründe für die Einführung von IPv6 sind vielfältig und Address für die Entwicklung des Internets von entscheidender Bedeutung. Erstens soll IPv6 das exponentielle Wachstum der Zahl der angeschlossenen Geräte unterstützen (ein Ziel, das mit dem begrenzten Address-Raum von IPv4 nicht zu erreichen ist). Zweitens zielt das Protokoll darauf ab, die Größe der Routing-Tabellen zu verringern, was den Austausch effizienter macht und die Arbeitsbelastung der Router langfristig verringert.


IPv6 versucht auch, bestimmte Aspekte der Paketverarbeitung zu vereinfachen, den Datagrammfluss zu verbessern und die Übertragungsgeschwindigkeit zwischen Netzen zu optimieren. Was die Sicherheit betrifft, so sind die AH/ESP-Header des *IPsec*-Protokolls in der Basisspezifikation enthalten, und alle IPv6-Knoten müssen sie unterstützen können (RFC 6434). Ihre Verwendung bleibt jedoch optional: Es obliegt dem Administrator, sie je nach Kontext zu aktivieren.


Zu den weiteren Zielen gehört eine präzisere Handhabung der Diensttypen, um insbesondere eine bessere Qualität für Echtzeitanwendungen (VoIP, Videokonferenzen usw.) zu gewährleisten. IPv6 soll auch ein flexibleres Mobilitätsmanagement ermöglichen: Ein Gerät kann den Zugangspunkt wechseln, ohne seinen Address für die anderen Geräte sichtbar zu ändern.


Schließlich wurde IPv6 für die Koexistenz mit älteren Protokollen entwickelt. Obwohl es nicht direkt binärkompatibel mit IPv4 ist, bleibt es vollständig interoperabel mit höheren Layer-Protokollen wie TCP, UDP, ICMPv6 und DNS sowie mit Routing-Protokollen wie OSPF und BGP, vorbehaltlich bestimmter Anpassungen. Für die Multicast-Verwaltung verwendet IPv6 das MLD-Protokoll (*Multicast Listener Discovery*), das das funktionale Äquivalent zu IGMP in der IPv4-Umgebung ist.


### Notationsregeln


Eine der wichtigsten Änderungen bei IPv6 ist das Format des IP Address selbst. Um dem chronischen Mangel an IPv4-Adressen entgegenzuwirken, wurde die Länge des Address von 32 Bit auf 128 Bit, also 16 Byte, erhöht. Theoretisch ergibt sich daraus ein möglicher Address-Raum von:


$$3.4 \times 10^{38}$$


Dies gewährleistet eine praktisch unbegrenzte Kapazität für alle aktuellen und zukünftigen Geräte.


IPv6-Adressen werden ganz anders geschrieben als in der bekannten Punkt-Dezimal-Notation. Eine IPv6 Address besteht aus acht 16-Bit-Gruppen, die in hexadezimaler Schreibweise geschrieben und durch Doppelpunkte `:` getrennt sind.


Zum Beispiel:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Um die Schreibweise zu vereinfachen, können führende Nullen in jeder Gruppe weggelassen werden. Das obige Beispiel wird dann zu:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Außerdem kann eine einzelne fortlaufende Folge von Nullgruppen durch:: ersetzt werden, wodurch der Address weiter verkürzt wird:


```
1987:c02:0:84c2::cf2a:9077
```


**Warnung:** Diese Regel ist streng: nur eine Folge von aufeinanderfolgenden Nullen kann durch `::` ersetzt werden. Enthält ein Address mehrere Nullenfolgen, wird nur die längste davon kondensiert. Dies gewährleistet sowohl die Eindeutigkeit als auch die Lesbarkeit.


**Wichtiges Detail:** Das Zeichen `:`, das zur Trennung von Hexadezimalblöcken verwendet wird, kann in URLs zu Mehrdeutigkeiten führen, da `:` auch zur Angabe eines Dienstports verwendet wird. Um Verwirrung zu vermeiden, müssen IPv6-Adressen in URLs in eckige Klammern `[ ]` gesetzt werden.


Beispiel für den HTTP-Zugriff auf einen bestimmten Port für den Address "2002:400:2A41:378::34A2:36":


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Bei der Darstellung eines IPv4-Address in einem IPv6-Kontext können Sie eine gemischte Notation in punktierter Dezimalform verwenden, der ein `::` vorangestellt wird:


```
::192.168.1.5
```


Diese Kompatibilität trägt dazu bei, den Übergang zwischen den beiden Protokollen zu erleichtern, da IPv4-Blöcke in den IPv6-Address-Raum aufgenommen werden können.


**Hinweis:** Um die Schreibweise von Adressen zu standardisieren, definiert RFC 5952 ein kanonisches Format mit Abkürzungsregeln, um Mehrfachdarstellungen desselben Address zu vermeiden. Die Befolgung dieser Empfehlungen trägt zur Verringerung von Fehlinterpretationen bei und gewährleistet konsistente Netzwerkkonfigurationen.


### IPv6 Address-Typen


IPv6 unterscheidet sich von seinem Vorgänger durch eine breite Palette von Address-Kategorien, die jeweils für bestimmte Zwecke ausgelegt sind und gleichzeitig eine flexible Leitweglenkung und Netzverwaltung ermöglichen. Wie bei IPv4 können die Adressen global, lokal, reserviert oder spezifisch für bestimmte Übergangsmechanismen sein.


Ein nicht spezifizierter IPv6-Address wird durch `::` oder, genauer gesagt, durch `::0.0.0.0` dargestellt. Diese spezielle Form wird während der Address-Erfassung oder als Standardwert verwendet, um das Nichtvorhandensein eines Address anzuzeigen.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *In einem privaten LAN wird das Präfix "fd00::/8" für die Zuweisung interner Adressen bevorzugt, die nicht über das Internet geroutet werden können


#### Reservierte Adressen


Bestimmte IPv6-Bereiche sind ausdrücklich reserviert und dürfen nicht als globale Adressen verwendet werden. Sie haben bestimmte technische Zwecke:


- `::/128`**: nicht spezifizierter Address, der nie dauerhaft einem Gerät zugewiesen wurde, aber von einem auf die Konfiguration wartenden Rechner als Quell-Address verwendet wird.
- `::1/128`**: der _loopback_ Address, das direkte Äquivalent zu `127.0.0.1` in IPv4, das es einer Maschine erlaubt, selbst Address zu erreichen.
- 64:ff9b::/96`**: Reserviert für Protokollübersetzer zur Ermöglichung von IPv4/IPv6-Verbindungen, wie in RFC 6052 definiert.
- `::ffff:0:0/96`**: Kompatibilitätsblock zur Darstellung eines IPv4 Address in einer spezifischen IPv6-Struktur, der häufig intern von Anwendungen verwendet wird.


Diese Blöcke gewährleisten die Interoperabilität und erleichtern die Migration zwischen den beiden Protokollversionen.


#### Globale Unicast-Adressen


Globale Unicast-Adressen machen den größten Teil des öffentlich zugänglichen IPv6-Raums aus und machen etwa 1/8 des Address-Raums aus. Seit 1999 hat die IANA diese Blöcke, wie z. B. das Präfix "2001::/16", in CIDR-Blöcken (von "23" bis "12") regionalen Registern zugewiesen, die sie dann an Anbieter und Organisationen weiterverteilen.


Einige Bereiche haben besondere dokumentierte Verwendungszwecke:


- `2001:2::/48`**: Reserviert für Leistungs- und Interoperabilitätstests (RFC 5180).
- 2001:db8::/32`**: Reserviert für Dokumentation und Beispiele (RFC 3849).
- `2002::/16`**: Wird für den 6to4-Mechanismus verwendet, der es dem IPv6-Verkehr ermöglicht, über eine IPv4-Infrastruktur zu laufen (nützlich während der Übergangsphase zwischen den beiden Protokollen).


**Hinweis:** Ein großer Teil der globalen Adressen bleibt ungenutzt und dient als Reserve für künftiges Internet-Wachstum.


#### Eindeutige lokale Adressen (ULA)


Eindeutige lokale Adressen (`fc00::/7`) sind das IPv6-Äquivalent zu den privaten IPv4-Adressen (RFC1918). Sie ermöglichen die Einrichtung isolierter interner Netze, ohne Konflikte mit der öffentlichen Adressierung zu riskieren. In der Praxis lautet das effektive Präfix `fd00::/8`, wobei das 8. Bit auf 1 gesetzt ist, um die lokale Nutzung anzuzeigen. Jeder ULA-Block enthält einen 40-Bit-Pseudo-Zufallsbezeichner, der Address-Kollisionen bei der Verbindung getrennter privater Netze minimiert.


#### Link-lokale Adressen


Link-local-Adressen (`fe80::/64`) werden ausschließlich für die Kommunikation innerhalb desselben Layer 2-Segments (desselben VLAN oder Switch) verwendet. Sie werden niemals über die lokale Verbindung hinaus geroutet. Jeder Netzwerk-Interface generiert automatisch einen link-local Address, der oft von seinem MAC-Address unter Verwendung des EUI-64-Schemas abgeleitet wird.


**Besonderheit**: Ein und derselbe Rechner kann denselben link-local Address an mehreren Schnittstellen verwenden, aber der Interface muss bei der Kommunikation angegeben werden, um Mehrdeutigkeiten zu vermeiden.


#### Multicast-Adressen


In IPv6 wurde Broadcast durch Multicast ersetzt, eine effizientere Methode, um Pakete an eine bestimmte Gruppe von Empfängern zuzustellen. Dem Multicast-Bereich ist das Präfix `ff00::/8` vorangestellt. Dazu gehören Adressen wie "ff02::1", die an alle Knoten auf der lokalen Verbindung gerichtet sind. Dieses Address ist zwar praktisch, wird aber für Anwendungen nicht mehr empfohlen, da es zu unkontrollierten generate-Übertragungen führen kann.


Eine häufige Anwendung von Multicast ist das _Neighbor Discovery Protocol_ (NDP), das ARP in IPv6 ersetzt. NDP verwendet spezifische Multicast-Adressen, wie z. B. "f02::1:ff00:0/104", um automatisch andere Hosts zu finden, die mit der gleichen Verbindung verbunden sind.


Durch die Kombination dieser Address-Typen bietet IPv6 ein komplettes Paket an Optionen, um die Anforderungen an globales Routing, lokale Kommunikation, IPv4/IPv6-Migration und automatische Gerätekonfiguration zu erfüllen und gleichzeitig die Übertragungseffizienz zu verbessern.


### Address Anwendungsbereich


Der Geltungsbereich eines IPv6 Address definiert den genauen Bereich, in dem er gültig und eindeutig ist. Das Verständnis dieses Konzepts ist der Schlüssel zur Beherrschung des Paket-Routings und der logischen Organisation eines IPv6-Netzwerks. IPv6-Adressen werden im Allgemeinen in drei Hauptkategorien eingeteilt, die auf ihrem Anwendungsbereich und ihrer Verwendung basieren: Unicast, Anycast und Multicast.


**Unicast-Adressen** sind am weitesten verbreitet und umfassen mehrere verschiedene Untertypen.

Dazu gehört der _loopback_ (`::1`) Address, dessen Anwendungsbereich auf den Host beschränkt ist, der ihn benutzt, und der verwendet wird, um den Netzwerkstack intern zu testen, ohne Verkehr über das physische Netzwerk zu senden.

Dann gibt es link-local-Adressen (_link-local_), deren Geltungsbereich auf ein einzelnes Netzsegment beschränkt ist: Sie werden für die direkte Kommunikation zwischen Geräten auf derselben physischen oder logischen Verbindung (z. B. einem einzelnen Switch oder VLAN) verwendet.

Einzigartige lokale Adressen (_ULA_, für _Unique Local Addresses_) schließlich sind intern in einem privaten Netz. Sie können zwischen mehreren privaten Segmenten weitergeleitet werden, sind aber nie im Internet sichtbar.


IPv6-Adressen werden häufig als binäre Struktur dargestellt, bei der die erste Hälfte (die ersten 64 Bits) das Netzpräfix und die zweite Hälfte (ebenfalls 64 Bits) den Interface des Geräts in diesem Netz eindeutig kennzeichnet. Diese Aufteilung erleichtert die Address-Autokonfiguration durch Mechanismen wie SLAAC (_Stateless Address Autoconfiguration_), die es Maschinen ermöglichen, automatisch einen stabilen Address auf der Grundlage der MAC Address oder eines Pseudo-Zufallsbezeichners zu wählen.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

Die IPv6-Architektur folgt dem hierarchischen globalen Routing-Modell des heutigen Internets. Die Aufteilung der Präfixe ermöglicht es den regionalen Registern und Netzbetreibern, die Address-Zuweisung dezentral zu verwalten und gleichzeitig die globale Einzigartigkeit zu gewährleisten. In diesem Rahmen kann ein und derselbe Host gleichzeitig einen globalen Unicast-Address für die Internetkommunikation und einen link-lokalen Address für lokale Interaktionen, z. B. mit der unmittelbaren Nachbarschaft oder für Router-Ermittlungsnachrichten, besitzen.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Anycast-Adressen** stellen ein Zwischenkonzept dar, das auf dem Unicast-Modell aufbaut, sich aber in bestimmten Fällen wie Multicast verhalten kann. Ein Anycast-Address ist im Wesentlichen ein Unicast-Address, der mehreren Schnittstellen zugewiesen ist, die über verschiedene Netzknoten verteilt sind. Wenn ein Paket an einen Anycast-Address gesendet wird, versucht das IPv6-Protokoll, es an einen der Hosts zuzustellen, die diesen Address gemeinsam nutzen, in der Regel an denjenigen, der in Bezug auf die Routing-Topologie am nächsten liegt. Dieser Ansatz optimiert die Geschwindigkeit der Abfrageverarbeitung und verbessert die Ausfallsicherheit von verteilten Diensten. Ein klassisches Beispiel sind die Root-DNS-Server, bei denen die Anycast-Adressierung die Abfragen automatisch an den nächstgelegenen Präsenzpunkt leitet.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

In IPv6 ersetzen **Multicast-Adressen** den Broadcast-Mechanismus, der als zu kostspielig und ungeeignet für ein globales Netz angesehen wurde. Eine Multicast-Address identifiziert eine Gruppe von Schnittstellen, typischerweise über mehrere Hosts, die die gleichen Pakete gleichzeitig empfangen möchten.

Jeder Multicast Address enthält ein spezielles 4-Bit _scope_-Feld, das die geografische oder logische Grenze der Übertragung definiert:


- Ein Geltungsbereich von "1" bedeutet, dass das Paket nur für das lokale Gerät bestimmt ist.
- Ein Geltungsbereich von "2" schränkt das Paket auf die lokale Verbindung ein: alle Geräte auf demselben physischen oder virtuellen Segment können es empfangen.
- Ein Bereich von "5" erweitert die Reichweite auf einen Standort, in der Regel ein ganzes Unternehmensnetz.
- Ein Geltungsbereich von "8" erweitert die Reichweite auf eine Organisation und ermöglicht die Zustellung über alle Teilnetze der gleichen Einheit.
- Ein Geltungsbereich von "e" (14 in Hexadezimal) bedeutet eine globale Reichweite, so dass die Multicast-Gruppe von überall im Internet erreichbar ist, wenn die Routing-Infrastruktur dies unterstützt.


Die Struktur einer IPv6-Multicast-Address umfasst:


- ein Feld _Flag_ (4 Bits) gibt an, ob die Gruppe permanent oder temporär ist,
- ein Feld _Scope_ (4 Bits) definiert den Bereich,
- ein Identifikationsfeld (112 Bits), das die Nummer der Multicast-Gruppe angibt.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Ein bekanntes Beispiel für IPv6-Multicast in Aktion ist das _Neighbor Discovery Protocol_ (NDP). Anstatt ARP wie in IPv4 zu verwenden, stützt sich NDP auf Multicast-Adressen wie "f02::1:ff00:0/104", um Anfragen zur Erkennung von Nachbarn zu senden, wobei nur die relevanten Hosts auf derselben Verbindung angesprochen werden.


Durch die genaue Definition von Address-Bereichen strukturiert IPv6, wie Datenströme gesendet, empfangen und weitergeleitet werden. Diese Granularität macht das Protokoll flexibler und effizienter für die Verwaltung sowohl lokaler als auch globaler Kommunikationen, während die Nachteile des allgemeinen Rundfunks vermieden werden.


## Address Assignment in einem lokalen Netz


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


In diesem Kapitel befassen wir uns mit einem der praktischsten Aspekte der IPv6-Einführung: der Zuweisung von IP-Adressen an Hosts in einem lokalen Netzwerk. Die IPv6-Architektur ist auf Flexibilität ausgelegt, so dass jedes Gerät seinen eigenen generate automatisch zuweisen kann, aber bei Bedarf auch eine vollständig manuelle Konfiguration möglich ist.


Ein IPv6-Lokalnetz teilt den Address systematisch in zwei Teile:


- die ersten 64 Bits stellen das Subnetz-Präfix dar, das normalerweise von einem Router oder einer Address-Behörde bereitgestellt wird;
- die restlichen 64 Bits werden vom Host verwendet, um sich in diesem Segment eindeutig zu identifizieren.

Dieses Modell vereinfacht die Routenaggregation und die Verwaltung von Address-Blöcken erheblich.


Für die Zuweisung von Adressen an Geräte gibt es zwei Hauptansätze:


- Manuelle Konfiguration, bei der der Administrator für jedes Interface den genauen Address angibt;
- Automatische Konfiguration, bei der die Geräte generate oder ihre eigenen Adressen dynamisch beziehen.


Bei der manuellen Konfiguration weist der Administrator jedem Interface den kompletten IPv6 Address zu. Bestimmte Werte bleiben reserviert:


- `::/128`: nicht spezifizierter Address, nie dauerhaft zugewiesen ;
- `::1/128`: Loopback Address (_loopback_), IPv4-Äquivalent: `127.0.0.1`.


Im Gegensatz zu IPv4 gibt es kein _Broadcast_-Konzept; die Kombinationen "alle Nullen" oder "alle Einsen" im Host-Teil haben keine besondere Bedeutung.

Die manuelle Konfiguration ist in kontrollierten Umgebungen immer noch nützlich, lässt sich aber in großem Maßstab nur schwer aufrechterhalten.


Für die automatische Konfiguration gibt es mehrere Methoden:


- Das **NDP** (_Neighbor Discovery Protocol_) Protokoll, spezifiziert durch RFC4862, ermöglicht eine *zustandslose* Autokonfiguration. In diesem Modus erhält der Host ein Netzwerkpräfix von einem lokalen Router und vervollständigt den Address selbst mit einer Kennung, die auf seiner MAC Address basiert. Diese Methode ist einfach zu implementieren und erfordert keinen zentralen Server.
- Implementierungen wie die in Windows können generate den Host-Teil pseudozufällig auswählen, um den Datenschutz zu verbessern, indem die direkte Offenlegung der MAC Address vermieden wird. Die Offenlegung der MAC Address in IPv6-Paketen kann datenschutzrechtliche Bedenken aufwerfen, da sie die Verfolgung eines Geräts über verschiedene Netze hinweg ermöglicht.
- DHCPv6-Protokoll: Definiert in RFC3315 und ähnlich wie das für IPv4 verwendete DHCP, ermöglicht es eine kontrolliertere und zentralisierte Konfiguration, einschließlich Lease-Management, zusätzliche Optionen (DNS, MTU...) und Datenbankregistrierung. DHCPv6 kann allein oder zusammen mit der zustandslosen Konfiguration arbeiten, um zusätzliche Parameter bereitzustellen, ohne die IP Address selbst zuzuweisen.


**Wichtiger Hinweis:** Bei der MAC-basierten Methode wird der MAC Address in einen 64-Bit-Identifikator unter Verwendung des EUI-64-Formats umgewandelt. Dieser Mechanismus fügt die Bytes "FFF:FE" in der Mitte des ursprünglichen MAC Address (in 48 Bits) ein und invertiert das siebte Bit, um die globale Eindeutigkeit anzuzeigen. Das Ergebnis ist ein stabiler Interface-Bezeichner, der im vollständigen IPv6 Address verwendet wird.


Hier ein Beispiel, wie ein MAC Address in EUI-64 umgewandelt werden kann:


![Image](assets/fr/045.webp)



Aufgrund der zunehmenden Besorgnis über die Verfolgung von Geräten aktivieren moderne Betriebssysteme (insbesondere Linux, Windows 10+, macOS, Android) jetzt standardmäßig Datenschutzerweiterungen. Diese verwenden zufällig generierte Interface-Kennungen, die für ausgehende Verbindungen regelmäßig erneuert werden, während für die interne Kommunikation (wie DNS oder DHCPv6) eine stabile Kennung beibehalten wird.


Wie bei DHCP in IPv4 können automatisch zugewiesene IPv6-Adressen zwei Lebensdauern haben, die von DHCPv6-Routern oder -Servern festgelegt werden:


- Bevorzugte Lebensdauer*: Nach diesem Zeitraum bleibt der Address gültig, wird aber nicht mehr zum Aufbau neuer Verbindungen verwendet;
- Gültige Lebensdauer*: Wenn diese Zeit abläuft, wird das Address vollständig aus der Interface-Konfiguration entfernt.


Mit diesem System können Netzänderungen dynamisch verwaltet werden, um z. B. einen reibungslosen Übergang von einem ISP zu einem anderen zu gewährleisten. Durch die Aktualisierung der von den Routern angekündigten Präfixe und die parallele Anpassung der DNS-Einträge kann die IPv6-Migration ohne spürbare Dienstunterbrechung durchgeführt werden.


**Tipp:** Die kombinierte Verwendung von Address und DNS-Lebenszyklen ermöglicht die Umsetzung einer schrittweisen Übergangsstrategie, bei der neue Verbindungen in eine neue Topologie übergehen, während bestehende Verbindungen bis zu ihrem natürlichen Ende weiterlaufen.


Kurz gesagt, IPv6 bietet ein breites Spektrum an Flexibilität für Address Assignment: manuelle Konfiguration, zustandslose oder zustandsabhängige automatische Konfiguration, DHCPv6 oder Zufallsgenerierung. Jeder Ansatz hat seine eigenen Vorteile und Einschränkungen und kann je nach dem erforderlichen Maß an Kontrolle, der Größe des Netzes oder den Datenschutzanforderungen angepasst werden.


## Zuweisung von IPv6-Address-Blöcken


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Address Vertrieb


Das IPv6 Address-Zuweisungsschema wurde so strukturiert, dass zwei Ziele erreicht werden: die Gewährleistung der globalen Address-Einmaligkeit und die Ermöglichung einer logischen Hierarchie, die die Aggregation und Vereinfachung von Routing-Tabellen begünstigt.

Wie bei IPv4 steht die *Internet Assigned Numbers Authority* (IANA) an der Spitze dieser Hierarchie. Sie verwaltet den globalen Unicast Address-Raum und delegiert Address-Blöcke an die fünf regionalen Internet-Register (_RIR_).


Die fünf bestehenden RIRs sind:


- ARIN (Nordamerika),
- RIPE NCC (Europa, Naher Osten, Zentralasien),
- APNIC (Asien-Pazifik),
- AFRINIC (Afrika),
- LACNIC (Lateinamerika und Karibik).


Die IANA weist jedem RIR IPv6-Blöcke unterschiedlicher Größe zu, im Allgemeinen zwischen /23 und /12. Dieser Ansatz bietet Flexibilität und gewährleistet gleichzeitig langfristige Skalierbarkeit. Die RIRs wiederum verteilen diese Blöcke an Internet-Diensteanbieter (ISPs), Großunternehmen und öffentliche Einrichtungen weiter.


Seit 2006 hat jedes RIR von der IANA einen IPv6 /12-Block erhalten, eine feste Größe, die eine stabile und ausreichend große Reserve für künftiges Wachstum gewährleisten soll. Die RIRs unterteilen diese in der Regel in /23-, /26- oder /29-Blöcke. Internet-Diensteanbieter erhalten in den meisten Fällen /32-Blöcke, wobei diese Größe je nach Größe und geografischem Gebiet des Diensteanbieters variieren kann. In der Regel werden den Kunden /48-Blöcke zugewiesen. Jeder /48-Block bietet 65.536 verschiedene /64-Subnetze (eine enorme Kapazität im Vergleich zu IPv4).


**Wichtiger Hinweis:** Ein /32-Block enthält genau 65.536 /48-Unterblöcke. Das bedeutet, dass jeder ISP Zehntausende von Kunden bedienen kann, ohne sein Kontingent zu erschöpfen. Dank seiner /48 verfügt jeder Kunde dann über eine gigantische Menge an Platz, um sein eigenes internes Netz mit so vielen /64-Segmenten zu strukturieren, wie er möchte.


Die typische Zuordnungshierarchie sieht wie folgt aus:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Mit dieser Fülle an Adressen ist NAT (*Network Address Translation*), das in IPv4 einst unerlässlich war, um mit Address-Knappheit fertig zu werden, nicht mehr notwendig. Jeder Host kann eine eindeutige, global routbare öffentliche Address-Adresse haben, was die End-to-End-Konnektivität vereinfacht und die Verwendung von Protokollen wie IPSec, VoIP oder eingehenden Verbindungen erleichtert.


Um zu prüfen, zu welcher Organisation ein IPv6 Address gehört, können Sie mit dem Befehl `whois` öffentliche RIR-Datenbanken abfragen. Diese Transparenz ermöglicht es, die Organisation zu identifizieren, der ein Präfix gehört, was für Netzwerk-, Analyse- oder Sicherheitszwecke nützlich sein kann.


### PA vs. PI-Adressierung


Ursprünglich basierte das IPv6-Zuweisungsmodell ausschließlich auf PA-Blöcken (*Provider Aggregatable*), d. h. auf Blöcken, die an den ISP gebunden sind. Bei diesem Modell erhält eine Organisation ihr Präfix von ihrem ISP, was bedeutet, dass bei einem Anbieterwechsel die gesamte Infrastruktur neu nummeriert werden muss.


Obwohl die automatische Konfiguration von IPv6 und die Address-Lebensdauer die Umnummerierung erleichtern, ist sie für Unternehmen mit kritischer Infrastruktur oder mit Verbindungen zu mehreren Providern aus Redundanzgründen nach wie vor unpraktisch.


Seit 2009 erlaubt die Zuweisungspolitik PI-Blöcke (*Provider Independent*). Diese Blöcke (in der Regel mit einer Größe von /48) werden einem Unternehmen oder einer Einrichtung direkt von einem RIR zugewiesen, unabhängig von einem ISP. Dieses Modell eignet sich besonders gut für Organisationen, die *Multihoming* praktizieren (d. h. gleichzeitig mit mehreren Betreibern verbunden sind). In Europa wird beispielsweise in RIPE-512 die Politik für die PI-Zuweisung beschrieben.


### Notation der Subnetzmaske


Wie IPv4 verwendet auch IPv6 CIDR (*Classless Inter-Domain Routing*). Dabei wird die Anzahl der Bits, aus denen das Präfix besteht, nach dem Address mit dem Zeichen "/" angegeben.


Nehmen Sie das folgende Beispiel:


```
2001:db8:1:1a0::/59
```


Das bedeutet, dass die ersten 59 Bits fest sind und das Netz identifizieren. Alle übrigen Bits (hier 69 Bits) können zur Identifizierung von Subnetzen oder Hosts verwendet werden.


Diese Notation deckt also Adressen von `2001:db8:1:1a0:0:0:0:0` bis `2001:db8:1:1bf:ffff:ffff:ffff:ffff` ab.


Dieser Block umfasst daher eine Reihe von 8 /64-Subnetzen, die jeweils eine große Anzahl von Geräten aufnehmen können.


Die CIDR-Notation ermöglicht eine präzise Address-Raumplanung, von großen Netzwerken bis hin zu Heimkonfigurationen und virtualisierten Umgebungen, und fördert die Routenaggregation, wodurch die Routerlast verringert und die Skalierbarkeit verbessert wird.


### IPv6-Pakete und Kopfzeilen


Das IPv6-Paketformat unterscheidet sich von IPv4 dadurch, dass es sowohl einfacher als auch erweiterbar ist. Ein IPv6-Datagramm beginnt immer mit einem Header fester Größe von 40 Byte, der alle wesentlichen Routing-Informationen enthält. Im Vergleich zu IPv4, wo die Länge des Headers variabel ist (von 20 bis 60 Byte), ermöglicht dieser vereinfachte Ansatz eine schnellere und effizientere Verarbeitung der Pakete durch die Router.


IPv6 verzichtet jedoch nicht auf Funktionalität: Anstatt zahlreiche optionale Felder in den Hauptheader zu integrieren, wird ein System von Erweiterungsheadern eingeführt, die unmittelbar nach dem Basisheader platziert werden. Diese optionalen Header ermöglichen das Hinzufügen von Daten oder Anweisungen für bestimmte Funktionen, ohne die normalen Pakete unnötig zu belasten.


Einige Erweiterungsheader folgen einer festen Struktur, während andere eine variable Anzahl von Optionen enthalten können. Diese Optionen werden als Triplets "Typ, Länge, Wert" kodiert:


- Das Feld "Typ" (1 Byte) gibt die Art der Option an;
- Die ersten beiden Bits des "Typs" geben an, was der Router tun soll, wenn die Option nicht erkannt wird:
 - Ignorieren Sie die Option und setzen Sie die Behandlung fort,
 - Verwerfen des Datagramms,
 - Verwerfen und Senden eines ICMP-Fehlers an die Quelle.
 - Verwerfen des Datagramms ohne Benachrichtigung (im Falle von Multicast-Paketen).
- Das Feld "Länge" (1 Byte) gibt die Größe des Feldes "Wert" an, von 0 bis 255 Byte;
- Das Feld "Wert" enthält die mit der Option verbundenen Daten.


Hier ist ein Überblick über die verschiedenen Arten von Erweiterungs-Headern, die von IPv6 definiert werden.


#### Hop-by-Hop-Kopfzeile


Dieser Header wird, falls vorhanden, immer unmittelbar nach dem Basis-Header platziert. Er enthält Informationen, die von jedem Router entlang des Paketweges verarbeitet werden müssen, im Gegensatz zu den meisten anderen Headern, die normalerweise nur vom Zielknoten verarbeitet werden. Typische Verwendungszwecke sind die Übermittlung globaler Parameter oder die Anforderung bestimmter Verarbeitungsschritte, während das Paket das Netz durchläuft.


![Image](assets/fr/047.webp)


#### Routing-Kopfzeile


Der Routing-Header gibt eine Liste von Zwischenadressen an, die das Paket durchlaufen muss. Es gibt zwei Haupt-Routing-Modi:


- Striktes Routing: der genaue Pfad ist vordefiniert
- Loose Routing: Es werden nur bestimmte obligatorische Schritte festgelegt.


Die ersten vier Felder dieses Rooting-Headers sind:


- Next Header**: gibt den Typ des nächsten Headers an;
- Routing Type**: legt die Routing-Methode fest (normalerweise "0");
- Verbleibende Segmente**: Anzahl der noch zu durchfahrenden Segmente ;
- Address[n]**: Liste der Zwischenadressen.


Das Feld "Verbleibende Segmente" beginnt mit der Gesamtzahl der verbleibenden Segmente und wird bei jedem Hop um eins dekrementiert.


![Image](assets/fr/048.webp)


#### Fragmentierungskopf


Bei IPv6 darf nur der Quellhost ein Datagramm fragmentieren, im Gegensatz zu IPv4, wo auch Router dies tun konnten. Alle IPv6-Knoten müssen in der Lage sein, Pakete von mindestens 1280 Byte zu verarbeiten. Wenn ein Router auf ein Paket stößt, das größer ist als die MTU der nächsten Verbindung, sendet er eine Nachricht *ICMPv6 Packet Too Big* an die Quelle zurück, die daraufhin die Größe ihrer Übertragungen anpasst.


Der Fragmentierungskopf enthält die folgenden Felder:


- Kennung**: eindeutige Kennung des Datagramms für die Wiederzusammensetzung.
- Fragment Offset**: die Position des Fragments innerhalb des ursprünglichen Datagramms.
- M-Flag**: zeigt an, ob weitere Fragmente folgen.


![Image](assets/fr/049.webp)


#### Authentifizierungs-Header (AH)


Dieser Header soll die Kommunikation sichern, indem er sowohl die Authentizität des Absenders als auch die Integrität der Daten verifiziert. Er wird in der Regel mit dem IPsec-Protokoll verwendet. Mit Hilfe eines Authentifizierungscodes kann der Empfänger bestätigen, dass die Nachricht wirklich von dem erwarteten Absender stammt und während der Übertragung nicht verändert wurde.


Im Falle eines betrügerischen Änderungsversuchs stimmt der Authentifizierungscode nicht mehr überein, und das Datagramm kann zurückgewiesen werden. Dieser Mechanismus schützt auch vor Wiederholungsangriffen, indem er unerlaubte Vervielfältigungen erkennt.


![Image](assets/fr/050.webp)


#### Zieloptionen Kopfzeile


Dieser Header ist nur für den Endempfänger des Datagramms bestimmt. Er kann verwendet werden, um anwendungsspezifische Optionen oder Metadaten hinzuzufügen, ohne dass diese von zwischengeschalteten Routern berücksichtigt werden.


Ursprünglich war eine solche Option im Protokoll nicht vorgesehen. Dieser Header wurde jedoch bei der Entwicklung von IPv6 eingeführt, um künftige Erweiterungen zu ermöglichen, ohne die Gesamtstruktur des Pakets zu verändern. Die Null-Option wird zum Beispiel nur verwendet, um den Header aus Gründen der Speicherausrichtung auf ein Vielfaches von 8 Byte aufzufüllen.


![Image](assets/fr/051.webp)


Das IPv6-Paketdesign basiert auf einer klaren Trennung zwischen einem minimalen Basis-Header und modularen Erweiterungs-Headern. Diese Architektur gewährleistet sowohl die standardmäßige Verarbeitungsleistung als auch die Flexibilität, die für die Weiterentwicklung des Protokolls und die Integration von Sicherheits-, komplexen Routing- oder Quality-of-Service-Mechanismen erforderlich ist, wobei die Kompatibilität mit künftigen Infrastrukturen gewahrt bleibt.


## Beziehung zwischen IPv6 und DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


In modernen Netzen übersetzt das DNS (*Domain Name System*) Domänennamen in IP-Adressen, die von Rechnern verwendet werden können. Mit der Einführung von IPv6 musste sich das DNS anpassen, um 128-Bit-Adressen zu unterstützen und gleichzeitig die Abwärtskompatibilität mit IPv4 zu wahren. Diese Koexistenz ist besonders wichtig in Dual-Stack-Umgebungen, in denen beide IP-Versionen gleichzeitig betrieben werden.


### IPv6-spezifische DNS-Einträge


Um einen Domänennamen mit einem IPv6-Address zu verknüpfen, verwendet DNS einen AAAA-Eintrag (*Quad-A*), der dem "A"-Eintrag für IPv4-Adressen ähnelt. Der AAAA-Eintrag ordnet einen Domänennamen ausdrücklich einem IPv6-Address zu.

Beispiel:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Dieser Eintrag zeigt an, dass die Domäne `ipv6.mydmn.org` zum IPv6 Address `2001:66c:2a8:22::c100:68b` aufgelöst wird. Es ist möglich und für eine maximale Kompatibilität sogar empfehlenswert, denselben Domänennamen mit mehreren IP-Adressen zu verknüpfen, sei es IPv4 (über einen A-Eintrag) oder IPv6 (über einen AAAA-Eintrag). Dies ermöglicht es IPv6-kompatiblen Kunden, IPv6 zu bevorzugen, während sichergestellt ist, dass nur IPv4-Kunden weiterhin unterstützt werden.


Darüber hinaus unterstützt DNS die umgekehrte Auflösung, d. h. es kann den mit einer bestimmten IP Address verbundenen Domänennamen nachschlagen. Im Falle von IPv6 verwendet dieser Vorgang PTR-Einträge in der Zone "ip6.arpa". Diese Zone ist speziell für die IPv6-Rückwärtsauflösung reserviert. Für IPv4 ist es die Zone "in-addr.arpa".


### Auflösung umkehren


Die umgekehrte Auflösung eines IPv6 Address folgt einem strengen Prozess:

1) Expandieren Sie den Address in die vollständige hexadezimale Schreibweise (16 Bytes, d. h. 32 hexadezimale Ziffern).

Beispiel:


```shell
2001:66c:2a8:22::c100:68b
```


Wird:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Kehren Sie die Reihenfolge der einzelnen Hexadezimalziffern (Nibble) um, trennen Sie sie durch Punkte und fügen Sie "ip6.arpa" an:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Diese Struktur gewährleistet standardisierte, eindeutige Reverse-Lookups im IPv6 Address-Raum.


**Bitte beachten**: DNS-Anfragen können entweder über IPv4 oder IPv6 erfolgen. Das verwendete Transportprotokoll hat keinen Einfluss auf die Art der zurückgegebenen Datensätze.

Zum Beispiel:


- Ein über IPv6 verbundener Client kann einen IPv4-Eintrag anfordern.
- Ein über IPv4 verbundener Client kann einen IPv6-Eintrag anfordern.

Der DNS-Server antwortet einfach mit den Datensätzen, die er hat, unabhängig vom Transportprotokoll der Anfrage.


Wenn ein Hostname sowohl auf IPv4 als auch auf IPv6 abgebildet ist, wird die Wahl des zu verwendenden Address durch RFC 6724 geregelt, das einen Address-Auswahlalgorithmus auf der Grundlage von Faktoren wie Präfixpräferenz, Umfang und Erreichbarkeit definiert. Standardmäßig wird IPv6 bevorzugt, es sei denn, dies wird durch die System- oder Netzwerkkonfiguration außer Kraft gesetzt.


**Wichtige Erinnerung**: Wenn ein IPv6 Address in eine URL (*Uniform Resource Locator*) eingebettet wird, muss er in eckige Klammern (`[]`) gesetzt werden. Dadurch wird eine Verwechslung zwischen dem Doppelpunkt (`:`) innerhalb des IPv6 Address und dem Doppelpunkt, der den Hostnamen vom Port in der URL trennt, vermieden.


Gültiges Beispiel:


```shell
http://[2001:db8::1]:8080
```


Dadurch wird sichergestellt, dass die URL sowohl von Browsern als auch von Webservern korrekt verarbeitet wird.


Die Integration von IPv6 in das DNS-System erfordert daher neue Datensatztypen, eine strenge Methode für die Rückwärtsauflösung und präzise Auswahl- und Formatierungsregeln, um die Kompatibilität und Konsistenz des Routings zu gewährleisten.


### Teil Zusammenfassung


In diesem Abschnitt haben wir uns mit den grundlegenden Prinzipien der IPv6-Adressierung beschäftigt. Zunächst wurde die Struktur des IPv6 Address untersucht: seine 128-Bit-Länge, die hexadezimale Notation und die Vereinfachungsregeln, die zur Verkürzung sich wiederholender Nullenfolgen verwendet werden. Dieses Design ermöglicht es IPv6, die Einschränkungen des Address-Raums von IPv4 zu überwinden und gleichzeitig Skalierbarkeit und eine effiziente Hierarchie zu gewährleisten.


Anschließend haben wir uns die verschiedenen Kategorien von IPv6-Adressen angesehen: Unicast, Anycast und Multicast, wobei wir ihren Anwendungsbereich, ihre typische Verwendung und ihre Darstellung im Address-Raum näher erläutert haben.


Als Nächstes wurden die Methoden zur Zuweisung von IPv6-Adressen in einem lokalen Netz untersucht, sei es durch manuelle Konfiguration, über das DHCPv6-Protokoll oder durch zustandslose Autokonfigurationsmechanismen, wie sie von NDP angeboten werden. Diese Ansätze ermöglichen es den Geräten, automatisch ihre eigene Address aus dem bereitgestellten Präfix und ihrer MAC-Address (über EUI-64) zu vergeben, während sie gleichzeitig Flexibilität in Bezug auf die Verwaltung der Lebensdauer und den Datenschutz bieten.


Wir haben auch detailliert beschrieben, wie Address-Blöcke zugewiesen werden, beginnend bei der IANA, die sie an die fünf RIRs (*Registered Internet Regions*) verteilt, und dann an die ISPs, die sie an ihre Kunden als Subnetze weiterverteilen (oft in /48, was 65536 /64 Subnetze erlaubt). Die Unterscheidung zwischen _Provider Aggregatable_ (PA) und _Provider Independent_ (PI) Blöcken hilft bei der Verwaltung von _multihoming_ oder Provider-Wechsel-Szenarien.


Wir haben gesehen, dass DNS mit der Einführung des AAAA-Datensatzes an IPv6 angepasst wurde und dass die Mechanismen für die Rückwärtsauflösung jetzt auf die Zone "ip6.arpa" angewiesen sind. Wichtig ist, dass DNS unabhängig vom verwendeten Transportprotokoll (IPv4 oder IPv6) bleibt, was eine nahtlose Interoperabilität in einer Dual-Stack-Umgebung gewährleistet.


IPv6 ist daher nicht nur eine inkrementelle Verbesserung gegenüber IPv4, sondern eine völlige Neugestaltung des Adressierungssystems, das sowohl den aktuellen als auch den künftigen Herausforderungen des globalen Internets gerecht werden soll.


Im letzten Teil dieses NET 302 Kurses werden wir in die Praxis gehen und uns auf Netzwerkdiagnosetools konzentrieren.



# Netzwerk-Diagnosetools


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Netzwerkzugang Layer-Tools


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


In diesem ersten Kapitel des letzten Abschnitts über Netzwerkdiagnose konzentrieren wir uns auf Tools zur Analyse des Netzwerkzugangs Layer des TCP/IP-Modells. Diese Layer ist für die direkte Kommunikation zwischen Geräten im selben physischen Netzwerk verantwortlich, insbesondere durch die Verwendung von MAC-Adressen und physischen Netzwerkschnittstellen wie Ethernet-Karten oder Wi-Fi-Schnittstellen.


Ziel ist es, den Administratoren praktische Werkzeuge an die Hand zu geben, mit denen sie diesen wichtigen Layer der Low-Level-Konnektivität überprüfen, testen und optimieren können. Diese Werkzeuge können verwendet werden, um den ordnungsgemäßen Betrieb von Schnittstellen zu überprüfen, Probleme mit der Netzwerkkartenkonfiguration zu beheben oder Anomalien wie Kollisionen, Paketverluste oder Verbindungsfehler zu erkennen.


### IP/MAC-Nachbarschaftsdienstprogramme


#### werkzeug `Arp`


Eines der ältesten Diagnosewerkzeuge des Network Access Layer ist der Befehl `arp`. Obwohl er zunehmend durch moderne Alternativen wie `ip neigh` ersetzt wird (die wir gleich kennenlernen werden). `Arp` ist immer noch auf vielen Systemen vorhanden, um den ARP-Cache (*Address Resolution Protocol*) einzusehen oder zu manipulieren. Dieser Cache speichert die Zuordnungen zwischen IP-Adressen und MAC-Adressen, die lokal auf einem Rechner bekannt sind. Mit anderen Worten: Sie können damit feststellen, welcher physische (MAC-)Address einem bestimmten IP-Address im lokalen Netz entspricht.


In der Praxis muss ein Host, der ein Paket an einen IP-Address innerhalb desselben Subnetzes senden will, zunächst den MAC-Address des Zielrechners kennen. Diese Zuordnung wird von ARP vorgenommen, das eine Anfrage an das lokale Netz sendet und eine Antwort mit der entsprechenden MAC Address erhält. Dieses Ergebnis wird dann vorübergehend in einer lokalen Tabelle, dem so genannten "ARP-Cache", gespeichert, um zu vermeiden, dass die Anfragen für jedes neue Paket wiederholt werden.


Um den Inhalt dieses Caches einzusehen und die dem Rechner derzeit bekannten Einträge zu überprüfen, verwenden Sie:


```bash
arp -a
```


Dieser Befehl listet alle lokal registrierten IP/MAC-Zuordnungen auf, und zwar für alle Schnittstellen. Jede Zeile enthält den Hostnamen (falls auflösbar), den IP-Address, den entsprechenden MAC-Address und den Interface, an dem die Zuordnung beobachtet wird.


Um die Anzeige nach einem bestimmten IP Address zu filtern, geben Sie diesen einfach an:


```bash
arp -a 192.168.1.5
```


Auf diese Weise lässt sich leicht überprüfen, ob eine bestimmte IP Address im Cache vorhanden ist, was bei der Diagnose von Kommunikationsfehlern zwischen zwei Hosts im gleichen Netz hilfreich sein kann.


Um nur die ARP-Einträge anzuzeigen, die mit einem bestimmten Interface-Netzwerk verbunden sind (z. B. eine Ethernet-Karte mit dem Namen "eth0"), können Sie ebenfalls diese Option verwenden:


```bash
arp -a -i eth0
```


Dies ist besonders nützlich in Umgebungen mit mehreren Interface (kabelgebunden, drahtlos, VPN usw.), in denen ein Host mehrere Netzwerkadapter haben kann.


Der `arp`-Befehl ist nicht auf den reinen Lesebetrieb beschränkt. Er kann auch verwendet werden, um den ARP-Cache manuell zu bearbeiten, eine unschätzbare Funktion in bestimmten fortgeschrittenen Fehlersuch-Szenarien oder bei der Simulation bestimmter Bedingungen. Sie können zum Beispiel manuell eine IP/MAC-Zuordnung hinzufügen:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Dieser Befehl erstellt einen statischen Eintrag in der lokalen ARP-Tabelle, der die IP Address `192.168.1.7` mit der MAC Address `00:17:BC:56:4F:25` auf dem Interface `eth2` verbindet.


Sie können auch einen Eintrag aus dem ARP-Cache entfernen, entweder um einen Fehler zu korrigieren oder um eine erneute Suche zu erzwingen:


```bash
arp -d 192.168.1.7
```


Dadurch wird der Eintrag gelöscht und sichergestellt, dass der nächste Kommunikationsversuch eine neue ARP-Anfrage auslöst.


**HINWEIS**: Die Option "Löschen" akzeptiert auch einen Interface-Namen, so dass Sie die Entfernung eines bestimmten Eintrags genauer festlegen können.


Zusammenfassend lässt sich sagen, dass das Tool `arp` eine Low-Level-Diagnose bietet, die besonders in lokalen Netzwerken nützlich ist, wo Verbindungsprobleme oft auf eine falsche oder veraltete Address-Auflösung zurückgeführt werden können. Auf neueren Systemen, insbesondere bei modernen Linux-Distributionen, wird dieses Tool jedoch zunehmend durch den Befehl `ip neigh` aus dem `iproute2`-Toolset ersetzt, der ähnliche Funktionen in einem einheitlicheren Rahmen bietet.


#### werkzeug `Ip neigh`


Auf modernen Systemen, insbesondere bei neueren Linux-Distributionen, ist der Befehl `ip neigh` das Standardwerkzeug für die Überprüfung und Verwaltung von Zuordnungen zwischen IP- und MAC-Adressen. Dieser Befehl ist Teil der "iproute2"-Suite, die nach und nach ältere Tools wie "arp" ersetzt und einen konsistenteren und flexibleren Rahmen für die Diagnose auf der Datenübertragungsstrecke Layer bietet.


Der Befehl "ip neigh" fragt den lokalen IP-Nachbarschafts-Cache ab, der dem ARP-Cache für IPv4 und dem NDP-Cache (_Neighbor Discovery Protocol_) für IPv6 entspricht. Dieser Cache speichert bekannte Verbindungen zwischen IP-Adressen (v4 oder v6) und MAC-Adressen zusammen mit ihrem Status (gültig, ausstehend, abgelaufen...).


Der grundlegende Befehl zum Anzeigen des Cache lautet:


```bash
ip neigh
```


Dies gibt eine Liste von Einträgen aus, die die Ziel-IP Address, das relevante Netzwerk Interface, die zugehörige MAC Address (falls verfügbar) und den Status des Eintrags (z. B. "erreichbar", "veraltet", "verzögert", "fehlgeschlagen" ...) enthält.


Beispielhafte Ausgabe:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Diese Zeile zeigt an, dass der Rechner eine gültige Zuordnung zwischen IP Address `192.168.1.5` und MAC Address `00:17:BC:56:4F:25` über Interface `eth0` kennt.


Sie können die Einträge auch nach Kriterien wie IP Address, Interface oder Status filtern. Zum Beispiel, um nur Address "192.168.1.7" abzufragen:


```bash
ip neigh show 192.168.1.7
```


Oder um alle Einträge für Interface `eth1` anzuzeigen:


```bash
ip neigh show dev eth1
```


Neben der Konsultation kann `ip neigh` auch dazu verwendet werden, den Cache manuell zu bearbeiten. Zum Beispiel, um einen statischen Eintrag hinzuzufügen:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Damit wird die IP Address `192.168.1.7` dauerhaft mit der angegebenen MAC Address auf Interface `eth1` verknüpft. Die Option `nud permanent` (für _Neighbor Unreachability Detection_) stellt sicher, dass der Eintrag nicht automatisch ungültig gemacht wird.


Umgekehrt können Sie einen Cache-Eintrag löschen:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Dadurch wird das System gezwungen, die Zuordnung bei der nächsten Kommunikation mit diesem Address neu aufzulösen.


**HINWEIS**: Das Tool "ip neigh" funktioniert sowohl für IPv4 als auch für IPv6. Bei IPv4 arbeitet es mit ARP zusammen, bei IPv6 mit NDP. Dies bietet einen einheitlichen, konsistenten Ansatz zur Verwaltung von IP/MAC-Beziehungen über Protokollfamilien hinweg und macht `ip neigh` zum modernen Standard für die Verwaltung von Nachbarn auf Linux-Systemen.


### Paketanalyse-Tools


Um die Vorgänge in einem Computernetz gründlich zu analysieren, benötigen Administratoren Werkzeuge, die die zwischen den Rechnern ausgetauschten Pakete erfassen können. Zwei Dienstprogramme haben sich dabei als Referenz erwiesen: `tcpdump` und `Wireshark`. Diese Tools sind unerlässlich, um abnormales Verhalten zu diagnostizieren, den Austausch von Protokollen zu überprüfen oder die Netzwerksicherheit durch die Untersuchung von Frame-Inhalten zu untersuchen.


#### ttcpdump": Befehlszeilenanalyse


tcpdump" ist ein sehr leistungsfähiges Kommandozeilen-Tool, das entwickelt wurde, um Pakete, die durch ein Netzwerk Interface laufen, zu erfassen und anzuzeigen. Es arbeitet in Echtzeit und kann dank seines schlanken Designs auf Systemen ohne grafischen Interface oder mit begrenzten Ressourcen verwendet werden. Es stützt sich auf die `libpcap`-Bibliothek, die hardwareunabhängige Low-Level-Erfassungsfunktionen bietet.


Eine häufige Anwendung von `tcpdump` ist die Überwachung der Netzwerkaktivität eines Rechners oder Netzwerksegments, wobei Pakete nach bestimmten Kriterien gefiltert werden. Die Ergebnisse können in eine Datei umgeleitet werden, so dass der Datenverkehr für eine spätere Analyse archiviert oder in einem anderen Tool, wie z. B. Wireshark, abgespielt werden kann.


Die allgemeine Befehlssyntax lautet:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- w" schreibt erfasste Pakete in eine Datei im `libpcap`-Format (Erweiterung `.cap` oder `.pcap`);
- -i" gibt das zu überwachende Netz Interface an (z. B. "eth0", "wlan0");
- s" legt die maximale Datenmenge fest, die pro Paket erfasst wird. Bei der Angabe von "0" werden alle Pakete erfasst;
- die Option "n" deaktiviert die DNS- und Dienstnamensauflösung und verbessert die Leistung.


Mit Ausdrucksfiltern am Ende des Befehls können Sie die Erfassungen auf eine Teilmenge des Datenverkehrs beschränken. Sie können die Schlüsselwörter `Host`, `Port`, `Src`, `Dst`, usw. kombinieren, um die Auswahl zu verfeinern.


Beispiel: Erfassen von HTTP-Paketen (Port 80) zum oder vom Server "192.168.25.24" und Speichern in einer Datei "fichier.cap":


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Die resultierende Datei kann später mit einem grafischen Tool analysiert oder auf einem anderen System wiedergegeben werden.


#### Wireshark: erweiterte visuelle Analyse


Wireshark, früher bekannt als *Ethereal*, ist ein komplettes Netzwerkanalyseprogramm mit einem grafischen Interface. Im Gegensatz zu `tcpdump` bietet es eine strukturierte, detaillierte Visualisierung von Paketen, einschließlich Protokollzerlegung, Flussdiagrammen, Verkehrsstatistiken und interaktiven Filtern. Es stützt sich auch auf `libpcap`, was bedeutet, dass es von `tcpdump` erzeugte Capture-Dateien öffnen und verarbeiten kann.


Wireshark ist für viele Betriebssysteme, einschließlich Linux und Windows, verfügbar. Für die Installation sind Administratorrechte erforderlich, um auf die Erfassungsschnittstellen zugreifen zu können. Nach dem Start können Sie ein Netzwerk Interface aus dem Menü *Capture* auswählen. Wenn Sie auf *Start* klicken, beginnt die Echtzeit-Paketaufzeichnung. Die Anzeige ist in drei Bereiche unterteilt:


- die Liste der erfassten Bilder;
- protokolldekodierte Details,
- rohe hexadezimale Daten.



![Image](assets/fr/052.webp)



Wireshark eignet sich hervorragend für Szenarien, in denen Sie komplexes Protokollverhalten beobachten, Anwendungsdialoge rekonstruieren (z. B. eine HTTP- oder DNS-Sitzung) oder die Antwortzeiten von Diensten untersuchen müssen. Es unterstützt auch hochspezifische Anzeigefilter, die eine eigene Syntax verwenden (die sich von der von `tcpdump` unterscheidet), um sich nur auf relevante Pakete zu konzentrieren.


#### Ergänzende Instrumente


Es ist wichtig zu beachten, dass `tcpdump` und Wireshark nicht austauschbar sind: beide haben ihre eigenen Stärken. tcpdump" eignet sich besser für Befehlszeilenumgebungen, automatisierte Skripte und Eingriffe in entfernte Server, während Wireshark ideal für detaillierte, interaktive und lehrreiche Verkehrsanalysen ist.


Die beiden Werkzeuge können kombiniert werden: Auf einem entfernten System kann mit `tcpdump` eine Aufzeichnung gemacht werden, dann wird die `.cap`-Datei zur Analyse mit Wireshark auf einen lokalen Rechner übertragen. Dieser Ansatz ist in der Praxis weit verbreitet.


### Interface-Analyse-Tools


Beim Network Access Layer ist es oft notwendig, physikalische Netzwerkschnittstellen abzufragen und zu konfigurieren, um Fehlfunktionen zu diagnostizieren, die Leistung zu optimieren oder die Verbindungsintegrität zu überprüfen. Eines der leistungsfähigsten Werkzeuge, die unter Linux für diesen Zweck zur Verfügung stehen, ist `ethtool`, ein Kommandozeilen-Dienstprogramm, das nicht nur detaillierte technische Informationen über ein Ethernet Interface liefert, sondern auch die Möglichkeit bietet, einige seiner Parameter in Echtzeit anzupassen.


#### Spezifikationen des Interface anzeigen


Ein Hauptmerkmal von `ethtool` ist die Möglichkeit, ein Interface abzufragen und seine aktuellen Eigenschaften anzuzeigen. Damit können Sie überprüfen:


- verbindungsgeschwindigkeit (z. B. 100 Mbit/s, 1 Gbit/s oder 10 Gbit/s);
- aushandlungsmodus (Halbduplex oder Vollduplex) ;
- ob Autonegotiation aktiviert ist;
- die Art des Anschlusses (Kupfer, Glasfaser, usw.) ;
- verbindungsstatus (aktiv oder nicht) ;
- unterstützung für erweiterte Funktionen wie *Wake-on-LAN*.


Diese Informationen sind besonders nützlich für die Diagnose von Problemen im Zusammenhang mit der physischen Konnektivität oder nicht übereinstimmenden Aushandlungseinstellungen zwischen der Netzwerkkarte des Hosts und den Geräten, mit denen er verbunden ist (Switch, Router usw.).


Um diese Informationen zu erhalten, führen Sie einfach aus:


```bash
ethtool enp0s3
```


Dieser Befehl gibt einen detaillierten Bericht über den Interface "enp0s3" aus, eine gängige Namenskonvention auf CentOS- oder RHEL-basierten Systemen.



![Image](assets/fr/053.webp)



#### Dynamische Änderung der Interface-Parameter


das "ethtool" beschränkt sich nicht nur auf die Beobachtung, sondern ermöglicht auch die Einstellung bestimmter Parameter des Interface, ohne dass das Gerät neu gestartet werden muss. So lässt sich beispielsweise eine bestimmte Verbindungsgeschwindigkeit erzwingen oder Funktionen aktivieren, die den Anforderungen des lokalen Netzes entsprechen.


Die Option "s" dient zur dynamischen Konfiguration von Parametern wie z. B.:


- link-Geschwindigkeit (`speed`), explizit eingestellt (z.B. 1000 für 1 Gbit/s) ;
- duplex-Modus (`duplex`), entweder `half` oder `full`;
- aktivierung oder Deaktivierung der Autonegotiation (`autoneg`) ;
- aktivierung von *Wake-on-LAN* (`wol`) ;
- port-Typ.


Beispiel 1: Aktivierung der Autonegotiation auf einem Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Beispiel 2: Aktivieren Sie die Funktion *Wake-on-LAN* (damit der Rechner aus der Ferne über ein magisches Paket aufwachen kann):


```bash
ethtool -s enp0s3 wol p
```


In diesem Beispiel legt die Option "p" fest, dass das Aufwachen erfolgt, sobald ein *Wake-on-LAN*-Paket erkannt wird. Diese Einstellung wird häufig in Unternehmensumgebungen verwendet, um Aktualisierungen über Nacht oder Fernwartung durchzuführen.


#### Einbau der Werkzeuge


Es ist wichtig zu beachten, dass `ethtool` nicht immer standardmäßig installiert ist. Auf Red Hat/CentOS Distributionen kann es mit dem Befehl installiert werden:


```bash
yum install -y ethtool
```


Unter Debian und Ubuntu lautet der entsprechende Befehl:


```bash
sudo apt install ethtool
```


**WARNUNG**: In allen `ethtool`-Befehlen muss der Name des Netzwerks Interface unmittelbar nach der Option (als `-s`) angegeben werden. Jeder Syntaxfehler bei der Platzierung der Parameter führt dazu, dass der Befehl ungültig oder unwirksam wird.



## Netzwerk Layer Werkzeuge


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Tools zur Verkehrsanalyse


In der Netzwerkdiagnose ist der `ping`-Befehl nach wie vor eines der einfachsten und zugleich leistungsfähigsten Werkzeuge zum Testen der Konnektivität zwischen zwei Rechnern. Er prüft, ob ein entfernter Host zu einem bestimmten Zeitpunkt erreichbar ist, und liefert außerdem Informationen über Latenz, Verbindungsstabilität und DNS-Auflösung.


Der Befehl "Ping" basiert auf dem ICMP-Protokoll (*Internet Control Message Protocol*). Wenn ein Benutzer eine "Ping"-Anforderung sendet, sendet das System ein ICMP-"Echo Request"-Paket an einen IP-Address oder einen Hostnamen. Wenn der Zielcomputer online ist und der Netzwerkpfad gültig ist, antwortet er mit einem ICMP-Paket "Echo Reply". Dieser einfache Mechanismus kann zur Messung der Latenzzeit und zur Erkennung von Verbindungsproblemen oder Problemen bei der Namensauflösung verwendet werden.


Beispiel für einen klassischen Befehl:


```bash
ping 172.17.18.19
```


Typische Antwort:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


In diesem Beispiel wurde die Namensauflösung automatisch durchgeführt: Die Domäne `mydmn.org` ist mit der IP Address `172.17.18.19` verbunden, was bestätigt, dass die DNS-Auflösung korrekt funktioniert. Der Befehl liefert auch technische Details wie z. B.:


- iCMP-Sequenznummer (`icmp_seq`), nützlich zur Überprüfung der Reihenfolge der Antworten;
- TTL (*Time-To-Live*), die die Anzahl der verbleibenden Sprünge angibt, bevor das Paket verworfen wird;
- round-Trip-Zeit/Verzögerung (`time`), ausgedrückt in Millisekunden, die eine Schätzung der Verbindungslatenz ermöglicht.


#### Ausführlichere Analyse der ICMP-Parameter


Die TTL ist ein wichtiges Feld im IP-Protokoll. Jedes Datagramm wird vom Absender mit einem TTL-Wert initialisiert (oft 64, 128 oder 255). Jeder Router entlang des Pfades dekrementiert diesen Wert um 1. Erreicht die TTL vor Erreichen des Ziels den Wert 0, wird das Paket verworfen und ein ICMP-Fehler an den Absender zurückgegeben. Dieser Mechanismus verhindert unendliche Routing-Schleifen.


Die Ausbreitungszeit (*round-trip delay/time*) misst die Verzögerung, die ein Paket benötigt, um den Absender zu verlassen, das Ziel zu erreichen und zurückzukehren. In der Praxis wird eine Verzögerung von unter 200 ms als akzeptabel für eine stabile Verbindung angesehen. Ungewöhnlich hohe Verzögerungen können auf eine Überlastung des Netzes, ineffizientes Routing oder schlechte Verbindungsqualität hinweisen.


#### Erweiterte `ping`-Verwendung


ping" bietet Optionen zur Verfeinerung der Tests und zur Beobachtung des spezifischen Netzwerkverhaltens.


Um Broadcast-Anfragen zu senden, können Sie die Option `-b` verwenden, um alle Hosts in einem Subnetz zu erreichen:

```bash
ping -b 192.168.1.255
```


Dies ist in lokalen Netzen nützlich, um aktive Hosts schnell zu erkennen oder zu testen, wie das Netz mit Broadcast-Anfragen umgeht. In vielen Konfigurationen blockieren Router und Firewalls jedoch Broadcast-Pings, um Verstärkungsangriffe zu verhindern.


Mit der Option `-i` können Sie auch ein benutzerdefiniertes Intervall zwischen den Anfragen angeben (Standard: 1 Sekunde):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Dabei werden 10 ICMP-Anfragen im Abstand von 0,2 Sekunden gesendet. Solche Tests sind nützlich, um Latenzschwankungen über einen kurzen Zeitraum festzustellen oder um eine Verbindung leicht zu belasten, um ihre Stabilität zu bewerten.


### Werkzeuge zur Analyse der Routingtabelle


Der `ip route`-Befehl, Teil der `iproute2`-Suite, ist das empfohlene und standardmäßige Werkzeug auf modernen Linux-Systemen zur Überprüfung und Verwaltung der IP-Routing-Tabelle des Kernels. Er ersetzt den veralteten `route`-Befehl und bietet eine klarere Syntax, größere Konsistenz und erweiterte Unterstützung für moderne Funktionen (IPv6, mehrere Tabellen, Namespaces, etc.).


#### Anzeige der Routing-Tabelle


So zeigen Sie die aktuelle Routing-Tabelle an:


```bash
ip route show
```


Diese Ausgabe listet alle dem Kernel bekannten Routen auf, d.h. die Wege, die ausgehende Pakete abhängig von ihrem Ziel nehmen.


Beispielhafte Ausgabe:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Jede Zeile steht für eine Route. Die wichtigsten Felder sind:


- default**: die Standardroute, die verwendet wird, wenn keine spezifischere Route passt.
- via**: das Gateway, über das das Ziel erreicht wird.
- dev**: das verwendete Netzwerk Interface.
- proto**: wie die Route erstellt wurde (manuell, DHCP, Kernel, usw.).
- metric**: Routenkosten, die verwendet werden, um mehrere mögliche Pfade zu priorisieren.
- scope**: Bereich der Route (z. B. `link` für eine direkt verbundene Route).
- src**: die Quell-IP Address, die für ausgehende Pakete auf diesem Interface verwendet wird.


#### Hinzufügen und Löschen von Routen


Sie können die Routing-Tabelle auch dynamisch ändern, z. B. indem Sie statische Routen hinzufügen oder entfernen.


Hinzufügen einer statischen Route:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Damit wird eine Route zum Netz "192.168.1.0/24" über das Gateway "192.168.1.1" auf Interface "eth0" konfiguriert.


Entfernen Sie diese Route:


```bash
ip route del 192.168.1.0/24
```


Dieser Befehl löscht die zuvor definierte Route.


#### Nützliche Befehle


Hier sind einige nützliche Varianten für die Analyse oder das Scripting:


- ip -4 route": zeigt nur IPv4-Routen an;
- ip -6 route": zeigt nur IPv6-Routen an;
- ip route list table main": zeigt die Haupt-Routing-Tabelle an (Standardwert);
- `ip route get <Address>`: zeigt an, welchen Interface und welches Gateway ein Paket zum angegebenen Address benutzen würde.


Beispiel:


```bash
ip route get 8.8.8.8
```


Dies zeigt die genaue Route an, die ein Paket nehmen würde, um `8.8.8.8` zu erreichen.


### Verfolgungswerkzeuge


Eines der wirksamsten Werkzeuge zur Analyse des Weges, den IP-Pakete zwischen einem Quellhost und einem Zielort nehmen, ist der Befehl "Traceroute". Er zeigt Schritt für Schritt den Weg an, den die Pakete nehmen, und identifiziert die dazwischenliegenden Router, die sie durchlaufen. Im Falle einer Störung der Netzverbindung oder eines Dienstausfalls hilft `traceroute`, den genauen Ort des Problems zu ermitteln.


Wie beim Befehl "ping" kann das Ziel entweder durch seinen voll qualifizierten Domänennamen (FQDN) oder durch seine IP Address angegeben werden. Zum Beispiel:


```bash
traceroute mydmn.org
```


#### Funktionsprinzip


die Funktion "Traceroute" beruht auf dem TTL-Feld (*Time To Live*) im Header der IP-Pakete. Wie bereits erläutert, ist dieses Feld ein Zähler, der von jedem Router entlang des Pfades dekrementiert wird. Erreicht die TTL den Wert Null, wird das Paket verworfen, und der Router sendet eine ICMP-Meldung "Time Exceeded" an den Absender zurück. Dieser Mechanismus verhindert Endlosschleifen im Falle einer Fehlleitung.


traceroute" macht sich dieses Verhalten zunutze, um die Router zwischen Absender und Empfänger abzubilden:


- Er sendet zunächst eine Reihe von UDP-Paketen (in der Regel drei) mit einer TTL von 1. Der erste Router trifft auf eine TTL von 0, verwirft also das Paket und antwortet dann mit einer ICMP-Nachricht, in der seine IP Address und die Antwortzeit angegeben sind.
- Als nächstes sendet er eine weitere Reihe von Paketen mit einer TTL von 2, die den zweiten Router verraten.
- Der Vorgang wiederholt sich, bis das Ziel erreicht ist. Dann antwortet der Host mit einer ICMP Port Unreachable Nachricht, die anzeigt, dass der Endpunkt erreicht wurde.


Standardmäßig verwendet `traceroute` UDP-Pakete, die an unbenutzte Ports (typischerweise ab 33434) gesendet werden, kann aber auch so konfiguriert werden, dass es ICMP (wie `ping`) oder sogar TCP verwendet, je nach System oder Befehlsvarianten.


Beispielhafte Ausgabe:


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


Jede Zeile entspricht einem durchlaufenen Router, mit bis zu drei Zeitmessungen (in Millisekunden), die die Latenzzeit des Roundtrips zu diesem Router angeben. Anhand dieser Werte lässt sich die Leistung der einzelnen Netzwerksegmente beurteilen.


#### Interpretation der Ergebnisse


Wenn ein Router nicht antwortet oder ICMP-Nachrichten filtert, werden anstelle der Antwortzeit Sternchen "*" angezeigt. Dies kann bedeuten:


- eine Firewall, die ICMP-Antworten blockiert,
- ein Gerät, das so konfiguriert ist, dass es nicht antwortet, oder
- ein vorübergehendes Verbindungsproblem entlang des Weges.


Traceroute" identifiziert also nicht nur die zurückgelegte Strecke, sondern zeigt auch Punkte mit anormalen Latenzen oder Unterbrechungen auf.


Auf einigen Systemen kann der äquivalente Befehl `tracepath` verwendet werden, der keine root-Rechte erfordert. Für IPv6, verwenden Sie `traceroute6` oder `tracepath6`.


Beispiel für IPv6-Tracing:


```bash
traceroute6 ipv6.google.com
```


### Tools zur Überprüfung aktiver Verbindungen


Um aktive Netzwerkverbindungen zu diagnostizieren und die Netzwerkaktivität auf einem Linux-System zu überwachen, ist der Befehl `ss` (kurz für _socket statistics_) das moderne Referenzwerkzeug. Als Teil der `iproute2`-Suite ersetzt er das inzwischen veraltete `netstat` und bietet eine bessere Leistung und genauere Ergebnisse.


ss" zeigt aktive TCP- und UDP-Verbindungen, lauschende Ports, lokale und entfernte Adressen, Verbindungsstatus und zugehörige Prozesse an.


#### Allgemeiner Gebrauch


Wird der Befehl `ss` ohne Optionen ausgeführt, zeigt er aktive TCP-Verbindungen an. Grundlegende Syntax:


```bash
ss [options]
```


Einige gängige Optionen zur Verfeinerung der Analyse:


- t": nur TCP-Verbindungen anzeigen;
- -u": nur UDP-Verbindungen anzeigen;
- l": nur hörende Sockets anzeigen;
- n": Namensauflösung deaktivieren (raw IPs und Portnummern) ;
- p": Anzeige aller mit dem Socket verbundenen Prozesse (PID und Programmname),
- a": alle Verbindungen anzeigen, auch die inaktiven,
- -s": Anzeige von Socket-Statistiken auf hoher Ebene.


#### Fallstudien


Zur Anzeige aller aktiven Verbindungen über TCP-Port 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Hier werden aktive TCP-Verbindungen über Port 80 angezeigt. Zustände wie `LISTEN`, `ESTABLISHED`, `TIME-WAIT` zeigen den aktuellen Status der einzelnen Exchange an.


Beispielhafte Ausgabe:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Zur Anzeige aller Netzwerkverbindungen mit zugehörigen Prozessen:


```bash
ss -tulnp
```


Um eine Gesamtübersicht über die Socket-Nutzung zu erhalten:

```bash
ss -s
```


Um nur UDP-Verbindungen zu filtern:

```bash
ss -unp
```


Diese Befehle sind besonders nützlich, um verdächtige Verbindungen, unerwartete lauschende Ports oder die Aktivität eines bestimmten Dienstes zu erkennen.


## Transport- und Aufsatzwerkzeuge Layer


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### DNS-Abfrage-Tools


In den oberen Schichten des TCP/IP-Modells, insbesondere bei der Anwendung Layer, ist es wichtig zu verstehen, wie die Namensauflösung funktioniert. Mit DNS-Abfragetools können Sie überprüfen, ob ein Domänenname korrekt mit einer IP Address verknüpft ist, und auch DNS-Serverprobleme wie Fehlkonfigurationen, Ausbreitungsverzögerungen oder Nichtverfügbarkeit diagnostizieren. Diese Tools sind für jeden Netzwerkadministrator oder jeden Benutzer, der ein tieferes Verständnis des DNS-Austauschs in einer IP-Umgebung wünscht, unerlässlich.


#### Der Befehl `nslookup`


Das einfachste DNS-Abfragetool ist `nslookup`. Es sendet eine Abfrage an einen DNS-Server und gibt die IP Address zurück, die mit einem Domänennamen verbunden ist (oder andersherum). Standardmäßig wird der konfigurierte DNS-Server des Systems abgefragt, aber Sie können auch einen Server direkt in dem Befehl angeben.


Beispiel für eine direkte Suche:

```bash
nslookup mydmn.org
```


Abfrage eines bestimmten DNS-Servers:

```bash
nslookup mydmn.org 192.6.23.4
```


Die Anfrage bittet den DNS-Server unter `192.6.23.4`, den Namen `mydmn.org` aufzulösen. Dies ist besonders nützlich, um zu prüfen, ob ein bestimmter DNS-Server einen Domänennamen erkennt oder um zu überprüfen, ob der Server ordnungsgemäß funktioniert.


#### Der Befehl `dig`


`dig` (*Domain Information Groper*) ist ein moderneres, vollständigeres und flexibleres Werkzeug als `nslookup`. Es unterstützt komplexe Abfragen und liefert detaillierte Informationen über den Auflösungsprozess, die Hierarchie der beteiligten Server, den Typ des zurückgegebenen Datensatzes (A, AAAA, MX, TXT usw.) und alle aufgetretenen Fehler.


Beispiel für eine einfache Abfrage:

```bash
dig mydmn.org
```


Abfrage eines bestimmten DNS-Servers:

```bash
dig @192.6.23.4 mydmn.org
```


Dieser Befehl prüft die Verfügbarkeit eines DNS-Eintrags auf einem bestimmten Server.

Einer der Hauptvorteile von `dig` ist, dass es die Details der DNS-Antwort anzeigt, was es sehr nützlich für die Diagnose von Konfigurationsfehlern macht.


#### Manuelle Konfiguration von DNS-Auflösern


Manchmal ist es notwendig, die lokal verwendeten DNS-Server zu überschreiben, zum Beispiel in Testumgebungen oder um die Verwendung bestimmter Server zu erzwingen. Dazu kann die Datei `/etc/resolv.conf` bearbeitet werden, in der die Einstellungen für die DNS-Auflösung des Systems festgelegt sind.


Beispielkonfiguration:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Das Feld "Suche" gibt eine Domäne an, die bei der Auflösung von Kurznamen automatisch angefügt wird.
- Die "Nameserver"-Einträge definieren die zu verwendenden DNS-Server in der Reihenfolge ihrer Priorität.


Bei vielen modernen Distributionen (besonders bei denen, die `systemd-resolved` verwenden) sind Änderungen an `/etc/resolv.conf` temporär und können bei einem Neustart oder einer erneuten Netzwerkverbindung überschrieben werden. Zu den dauerhafteren Methoden gehören die Verwendung von `resolvconf`, `systemd-resolved` oder die Änderung von *NetworkManager*-Konfigurationen.


#### Der Befehl `host`


Ein weiteres einfaches, aber effektives DNS-Tool ist `host`. Es löst Domänennamen in IP-Adressen auf (oder umgekehrt) und kann bei der Diagnose von DNS-Fehlern oder Fehlkonfigurationen in einem Netzwerk Interface helfen.


Beispiele:

```bash
host mydmn.org
```


Rückwärtssuche:

```bash
host 192.6.23.4
```


host" ist besonders praktisch für schnelle Überprüfungen, vor allem wenn es in Befehlszeilenskripten verwendet wird.


Wiederholte oder intensive Anfragen an DNS-Server von Drittanbietern ohne Genehmigung können als Eindringversuch oder böswillige Aktivität interpretiert werden. Bei unsachgemäßer Verwendung oder in Netzwerken, die Sie nicht kontrollieren, können diese Befehle Aufklärungsscans ähneln, die oft ein erster Schritt eines Angriffs sind. Beschränken Sie die Verwendung dieser Befehle immer auf Umgebungen, die Sie verwalten oder für die Sie eine ausdrückliche Genehmigung haben.


### Netzwerk-Scanning-Tools


Bei der Überwachung oder Sicherung eines lokalen oder weitläufigen Netzwerks ist es wichtig, aktive Geräte und die von ihnen angebotenen Dienste zu identifizieren. Genau das leistet das Tool "nmap" (*Network Mapper*).


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Einführung in `nmap`


`nmap` ermöglicht das gezielte Scannen eines oder mehrerer Hosts, um offene Ports, verfügbare Dienste (HTTP, SSH, DNS usw.) und manchmal sogar die Art des verwendeten Betriebssystems zu erkennen. Dank seiner zahlreichen Optionen bietet `nmap` einen präzisen Überblick über die Angriffsfläche eines Netzwerks, was für die Audit- oder Härtungsphasen der Infrastrukturverwaltung unerlässlich ist.


Genau wie der Befehl "host" darf "nmap" niemals auf Netzwerken oder Infrastrukturen verwendet werden, die nicht in Ihrem Besitz sind, oder ohne ausdrückliche Genehmigung. Unerlaubte Port-Scans können als böswillige Aufklärungsversuche gewertet werden, werden häufig von Sicherheitssystemen (Firewalls, IDS/IPS) erkannt und können sogar rechtliche Konsequenzen nach sich ziehen.


#### Grundlegende Verwendung


Um einen bestimmten Host zu scannen und seine offenen Ports anzuzeigen:

```bash
nmap 192.168.0.1
```


Mit diesem Befehl werden die 1000 häufigsten Ports auf dem Host "192.168.0.1" gescannt und die verwendeten Dienste und Protokolle angezeigt. Wenn die DNS-Auflösung konfiguriert ist, können Sie auch den Hostnamen anstelle der IP Address verwenden.


#### Vollständiger Netzwerk-Scan


Einer der Vorteile von `nmap` ist die Fähigkeit, einen ganzen Bereich von Adressen mit einem einzigen Befehl zu scannen. Das macht es zum Beispiel einfach, schnell eine Bestandsaufnahme aller aktiven Maschinen in einem Netzwerk zu machen:


```bash
nmap 192.168.0.0/24
```


In diesem Fall werden alle Hosts im Bereich `192.168.0.0` bis `192.168.0.255` abgefragt. Für jeden IP-Address werden in den Ergebnissen die offenen Ports, ihr Status (offen, gefiltert usw.) und, wenn möglich, der Name des entsprechenden Dienstes aufgeführt.



![Image](assets/fr/055.webp)



Ein Administrator kann sich für verschiedene Aufgaben auf `nmap` verlassen:


- Erkennung aktiver Hosts**: Erkennen, welche Rechner innerhalb eines Subnetzes antworten;
- Dienstinventar**: Sicherstellen, dass nur die notwendigen Ports zugänglich sind (Prinzip der geringsten Berechtigung);
- Compliance-Check**: Abgleich offener Ports mit den Sicherheitsrichtlinien des Unternehmens;
- Schwachstellenvorbeugung**: Erkennen unsicherer oder veralteter Dienste, die auf kritischen Rechnern laufen.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Werkzeuge zur Prozessabfrage


Für eine eingehende Analyse aktiver Prozesse und offener Dateien, insbesondere in einem Netzwerkkontext, greifen Linux-Administratoren häufig auf den Befehl `lsof` (*List Open Files*) zurück. Trotz seines Namens ist `lsof` nicht auf herkömmliche Dateien beschränkt: Auf UNIX-Systemen wird alles als Datei betrachtet, einschließlich Netzwerk-Sockets, Geräte und Kommunikationskanäle.


Dieses Tool bietet daher einen Querschnitt des Systems, indem es aktive Prozesse, offene Netzwerk-Ports, zugegriffene Dateien und die beteiligten Benutzer miteinander in Beziehung setzt.


#### Netzwerkanalyse mit `lsof`


Die Option "-i" schränkt die Ausgabe auf Netzwerkverbindungen (TCP, UDP, IPv4 oder IPv6) ein. So lässt sich leicht erkennen, welche Prozesse über das Netzwerk kommunizieren:


```bash
lsof -i
```


Dieser Befehl listet alle laufenden Prozesse auf, die einen Netzwerk-Socket verwenden, und zeigt den verwendeten Port, das Protokoll (TCP/UDP), den Verbindungsstatus sowie die PID und den zugehörigen Benutzer an.


#### Filterung nach IP Address oder Port


Sie können die Suche durch Angabe einer IP Address und eines Ports verfeinern und so einen bestimmten Netzwerkfluss isolieren. Zum Beispiel, um eine SMTP-Sitzung (Port 25) mit einem bestimmten Host zu überprüfen:


```bash
lsof -n -i @192.168.2.1:25
```


Damit werden nur aktive Netzwerkverbindungen mit dem Host "192.168.2.1" an Port 25 angezeigt, was für die Diagnose verdächtiger Aktivitäten oder von SMTP-Flow-Problemen nützlich ist.


#### Verfolgung des Gerätezugriffs


Eine weitere Stärke von `lsof` ist das Aufspüren spezieller Dateien wie Festplattenpartitionen. Zum Beispiel, um zu überprüfen, welche Prozesse Dateien auf `/dev/sda1` geöffnet haben:


```bash
lsof /dev/sda1
```


Dies ist praktisch, wenn ein Aushängeversuch fehlschlägt, weil das Gerät noch in Gebrauch ist, oder wenn untersucht werden soll, welche Anwendungen auf eine Partition zugreifen.


#### Querschnittsanalyse: Prozess und Netzwerk


Die Optionen können kombiniert werden, um genaue Einblicke zu erhalten. Zum Beispiel, um alle Netzwerkports zu sehen, die von einem Prozess mit der PID 1521 geöffnet wurden:


```bash
lsof -i -a -p 1521
```


Die Option `-a` schneidet die Kriterien (`-i` und `-p`) und schränkt die Ausgabe auf die Netzverbindungen dieses Prozesses ein.


#### Multi-User-Tracking


mit `lsof` kann auch die Aktivität bestimmter Benutzer analysiert werden, indem alle von ihnen geöffneten Dateien aufgelistet werden, optional gefiltert nach PID:


```bash
lsof -p 1521 -u 500,phil
```


Dies zeigt die Dateien oder Netzwerkverbindungen, die vom Benutzer `phil` oder UID 500 verwendet werden, beschränkt auf den Prozess 1521.


### Zusammenfassung der Sektion


In diesem letzten Abschnitt haben wir ein breites Spektrum an unverzichtbaren Werkzeugen für die Diagnose, Analyse und Verwaltung von Computernetzwerken kennengelernt. Anhand der Schichten des TCP/IP-Modells erläutert diese Studie nicht nur, wie die Netzwerkkommunikation funktioniert, sondern stellt auch eine strenge Methodik zur Identifizierung, Isolierung und Lösung potenzieller Probleme auf.


Diese Tools geben den Administratoren eine Reihe kohärenter technischer Hebel in die Hand, um den Zustand des Netzes zu überwachen, den Datenverkehr zu analysieren, Verbindungen zu prüfen und bei fehlerhaften Geräten oder Diensten schnell einzugreifen.


#### Netzwerkzugang Layer


Tools, die einen direkten Einblick in Schnittstellen und Frames ermöglichen:


- arp / ip neigh**: untersucht und ändert den ARP/NDP-Cache, um IP-MAC-Zuordnungen zu überprüfen oder zu korrigieren;
- tcpdump**: Kommandozeilen-Paketaufnahme, filterbar und exportierbar;
- Wireshark**: grafische Paketanalyse mit tiefer Protokolldekodierung;
- ethtool**: Abfrage und Einstellung der physikalischen Parameter der Ethernet-Karte (Geschwindigkeit, Duplex, WoL, etc.).


#### Netzwerk Layer


Tools zur Bewertung von IP-Konnektivität, Routing und Paketverkehr:


- ping**: Test der Erreichbarkeit und Messung der Latenzzeit mit ICMP;
- ip route**: Überprüfung und Änderung der Routing-Tabelle zur Kontrolle der Paketwege;
- traceroute**: Hop-by-Hop-Identifizierung von Routern entlang der Route zu einem Ziel;
- ss**: detaillierte Bestandsaufnahme von TCP/UDP-Sockets und zugehörigen Prozessen (Nachfolger von netstat).


#### Transport- und Anwendungsschichten


Werkzeuge zur Diagnose von Diensten und Prozessen:


- nslookup / dig / host**: DNS-Abfragen zur Überprüfung der Namensauflösung und zur Analyse von Datensätzen;
- nmap**: Untersuchung offener Ports und exponierter Dienste zur Bewertung der Angriffsfläche;
- lsof**: Auflistung von Dateien und Sockets, die von Prozessen geöffnet wurden, um System- und Netzwerkaktivitäten zu korrelieren.


Die Beherrschung dieser Tools, die jeweils auf eine bestimmte Stufe des TCP/IP-Modells ausgerichtet sind, ermöglicht einen methodischen Ansatz: angefangen beim physischen Layer über das Routing bis hin zu den Anwendungsdiensten. Mit dieser Kompetenzkette sind Administratoren in der Lage, ihre Infrastruktur zu diagnostizieren, zu sichern und zu optimieren, um sowohl die Netzwerkleistung als auch die Verfügbarkeit zu gewährleisten.


# Letzter Teil


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Rezensionen und Bewertungen


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Abschlussprüfung


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Schlussfolgerung


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>