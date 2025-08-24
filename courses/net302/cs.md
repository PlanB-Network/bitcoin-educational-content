---
name: IP sítě od teorie k praxi
goal: Osvojte si základy IP sítí, abyste je mohli lépe konfigurovat a řešit problémy.
objectives: 


  - Porozumět architektuře a fungování protokolu TCP/IP
  - Vysvětlete rozdíly, výhody a omezení protokolů IPv4 a IPv6
  - Identifikace a rozlišení různých typů IP Address
  - Konfigurace a ověření adresování IP v systémech Unix/Linux
  - Používání hlavních diagnostických nástrojů k analýze a řešení síťových problémů


---

# Základní dovednosti pro orientaci ve světě duševního vlastnictví


Ponořte se do nitra světa IP a získejte znalosti, které vám umožní porozumět sítím a efektivně je spravovat. V tomto kurzu se srozumitelnou a praktickou formou dozvíte vše, co potřebujete vědět o počítačových sítích.


Dozvíte se, jak fungují sítě a adresování IP, jak rozlišovat mezi IPv4 a IPv6, jak identifikovat a používat různé kategorie Address a jak pochopit celý význam protokolu TCP/IP a vazeb, které vytváří mezi adresami IP, fyzickými adresami a názvy DNS.


NET 302 je určen především studentům, uživatelům Linuxu nebo prostě jen zvědavcům, kteří chtějí pochopit základy sítí a posílit svou samostatnost při správě, řešení problémů a optimalizaci infrastruktur.


Přidejte se k nám a proměňte své znalosti ve skutečné provozní znalosti!


___


Tento kurz NET 302 je adaptací knihy *Les bases du réseau: (https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), pod licencí Creative Commons Uveďte autora - ShareAlike 4.0 International ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)).



V původní verzi Loïca Morela byly provedeny podstatné změny: text byl zcela přepracován, rozšířen a obohacen, aby poskytl aktualizovaný a podrobný obsah a zároveň zachoval vzdělávací duch původního díla Philippa Pierra. Přepracovány byly rovněž diagramy.


+++


# Úvod


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Přehled kurzů


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Tento kurz poskytuje úplný úvod do základů sítí IP. Je rozdělen do čtyř hlavních částí, z nichž každá se zabývá základním aspektem pro pochopení, konfiguraci a diagnostiku problémů v počítačové síti.


### Protokol TCP/IP


V této první části položíme základy a prozkoumáme koncept sítí a historii protokolu TCP/IP. Budeme studovat jeho hlavní součásti: IP, TCP a krátce se podíváme na protokol IPv5 QoS. Budeme se také zabývat primitivy služeb, abychom lépe pochopili logiku datové sítě Exchange.


### Adresování IPv4


Poté přejdeme k modulu věnovanému adresování IPv4. Dozvíte se, jak se IPv4 používá v praxi, jaké jsou jeho různé typy Address (privátní, veřejné, broadcast atd.), jakou základní roli hraje DNS a jak fungují ethernetové adresy a protokol ARP. Seznámíte se také s NAT (Network Address Translation) a se základy konfigurace sítě.


### Adresování IPv6


Třetí část se zaměřuje na adresování IPv6, které je nezbytné pro Address omezení IPv4. Projdeme si jeho standardy a definice, Address Assignment v rámci místní sítě, správu bloků Address a vztah mezi IPv6 a DNS.


### Síťové diagnostické nástroje


Na závěr představíme hlavní nástroje pro diagnostiku sítě. Ty vám umožní analyzovat, kontrolovat a odstraňovat poruchy. Tato část bude strukturována podle vrstev: Přístupová, síťová, transportní a horní vrstva.


Na konci tohoto kurzu získáte základní znalosti pro efektivní správu síťové infrastruktury a diagnostiku případných problémů.


Jste připraveni ponořit se do světa počítačových sítí? Jdeme na to!


**POZNÁMKA**: Popisy jsou založeny na systému GNU/Linux CentOS 7. Síťové konfigurace jsou však při porovnání systému Debian a CentOS z velké části stejné. Nebudeme tedy dělat žádné rozdíly. Pokud nějaké bude, uvedeme před něj specifické logo.


**N.B.**: Pokud se v průběhu kurzu setkáte s neznámými pojmy, vyhledejte si jejich definice ve [slovníčku pojmů](https://planb.network/resources/glossary).



# Protokoly TCP/IP


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Co je to síť?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



V tomto prvním modulu se podrobně seznámíme s protokolem TCP/IP, který je základem moderní digitální komunikace. Probereme jeho původ, základní principy a systém adresování, který používá a který je nezbytný pro zajištění toku informací mezi připojenými zařízeními.


Podrobně se také seznámíme s hlavními součástmi, které tento model tvoří, a vysvětlíme, jak se vzájemně ovlivňují, aby vytvořily funkční, spolehlivou a škálovatelnou síť. Nejprve je však nezbytné vrátit se k pojmu síť.


Etymologicky se síť vztahuje na soubor vzájemně propojených bodů, které tvoří vzájemně propojenou strukturu. V telekomunikacích a výpočetní technice se tato definice překládá jako skupina zařízení (počítačů, směrovačů, přepínačů, přístupových bodů atd.) schopných vyměňovat si data prostřednictvím fyzických nebo bezdrátových médií. Síť tak umožňuje nepřetržitý nebo přerušovaný tok informací v závislosti na požadavcích, používaných protokolech a povaze nasazené architektury.


V průběhu času bylo vyvinuto několik klasických topologií, které splňují různé požadavky na náklady, výkon, odolnost a snadnou údržbu. Patří mezi ně:


- kruhová síť,
- síť stromů,
- síť autobusů,
- hvězdná síť,
- síť mesh.



### Kruhová síť


V kruhové topologii jsou zařízení propojena v uzavřené smyčce: každá stanice je propojena s další a poslední se připojuje zpět k první. V tomto uspořádání funguje každé zařízení jako relé a předává data dalšímu spoji. V závislosti na typu sítě mohou informace obíhat pouze jedním směrem, nebo oběma směry.


Výhodou tohoto uspořádání je jednoduchost kabeláže a absence závislosti na centrálním zařízení. Kontinuita celé sítě však závisí na stavu každého jednotlivého prvku: výpadek jediné stanice může přerušit celý komunikační systém. Proto se často zavádí redundance nebo obchvatové mechanismy.



![Image](assets/fr/001.webp)



### Síť stromů


Stromová síť neboli hierarchická topologie je modelována podle struktury rodokmenu. Skládá se z postupných úrovní: kořenový uzel na vrcholu se připojuje k několika uzlům nižší úrovně, které se mohou samy připojovat k dalším uzlům atd.


Toto hierarchické uspořádání se osvědčuje zejména u velkých sítí, které vyžadují jasné rozdělení odpovědností a segmentovanou správu. Zároveň však činí síť zranitelnou vůči selhání uzlů vyšší úrovně: ztráta kořene nebo hlavní větve může odříznout celé části infrastruktury.



![Image](assets/fr/002.webp)



### Autobusová síť


V topologii sběrnice sdílejí všechna zařízení stejné přenosové médium, obvykle koaxiální vedení nebo optické vlákno. Každá jednotka je pasivně připojena, což znamená, že aktivně nemění signál, a může po tomto sdíleném kanálu odesílat nebo přijímat data.


Hlavní výhodou sběrnicové topologie jsou nízké náklady na instalaci díky zjednodušené kabeláži.  U starších implementací založených na koaxiální sběrnici (Ethernet 10BASE2/10BASE5) by však odpojení nebo ztráta jedné stanice mohla narušit nebo dokonce zastavit veškerý provoz, protože by již nebyla zachována elektrická kontinuita sběrnice a impedance zakončení. Jediné fyzické médium je také kritickou slabinou: jakékoli přerušení nebo porucha zastaví komunikaci pro celou síť.



![Image](assets/fr/003.webp)



### Hvězdná síť


Topologie hvězdy, známá také jako "hub and spoke", je dnes nejběžnější, zejména v domácích a kancelářských sítích Ethernet. Zde se všechna zařízení připojují k jednomu centrálnímu zařízení.


Toto uspořádání usnadňuje správu a údržbu: pokud dojde k poruše jednoho periferního zařízení, zbytek sítě zůstane nedotčen. Nevýhodou je, že centrální zařízení představuje jediný bod selhání: pokud dojde k jeho výpadku, komunikace se zastaví všude. Pro zachování dobrého výkonu je také třeba pečlivě zvážit kvalitu kabelů a délku spojů.



![Image](assets/fr/004.webp)



**Poznámka**: stále existují sítě s lineární topologií podobnou sběrnici, kde jsou zařízení připojena jedno za druhým. Toto řešení je sice levné na nasazení, ale má zásadní nevýhodu v tom, že při jediném přerušení dojde k izolaci některých hostitelů a rozdělení sítě na nezávislé podskupiny.


### Síť Mesh


Síť mesh je navržena pro maximální redundanci: každé zařízení je přímo propojeno s každým dalším zařízením. Tím je zajištěna kontinuita služeb i v případě výpadku více spojů nebo zařízení, protože provoz může být přesměrován po alternativních trasách.


Kompromisem je, že s počtem terminálů rychle roste počet navazovaných spojení. Pro `N` přípojných bodů je zapotřebí `N × (N-1) / 2` samostatných spojů, což činí tuto topologii nákladnou a složitou na zavedení. Používá se proto především v kritických sítích vyžadujících velmi vysokou dostupnost, jako jsou některé části internetu nebo citlivé průmyslové systémy.



![Image](assets/fr/005.webp)



Existují i další varianty, například sítě typu grid nebo hypercube, které jsou určeny pro specializované potřeby distribuovaných výpočtů nebo paralelního zpracování.


V celosvětovém měřítku je internet rozsáhlým propojením sítí s různými topologiemi, které jsou sjednoceny společnou adresací (IPv4 a IPv6) a souborem standardizovaných protokolů definovaných skupinou IETF (*Internet Engineering Task Force*). Tato rozmanitost znamená, že se internet neřídí jedinou topologií: jeho struktura je flexibilní, škálovatelná a nezávislá na logickém adresním schématu, které jej umožňuje používat.



## Počátky protokolu TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



U zrodu protokolu TCP stojí agentura **ARPA** (*Advanced Research Projects Agency*, v roce 1972 přejmenovaná na DARPA), která v roce 1966 zahájila projekt **ARPANET**. První segment sítě ARPANET byl uveden do provozu v říjnu 1969 a propojil univerzity UCLA a Stanford. Cílem bylo propojit výzkumná centra prostřednictvím sítě s přepojováním paketů, která by dokázala udržet komunikaci v chodu i v případě částečného výpadku infrastruktury.


V rámci této dynamiky financovala agentura ARPA na univerzitě v Berkeley integraci prvních protokolů TCP/IP do svého unixového systému BSD. To sehrálo významnou roli při šíření a standardizaci protokolu nejprve v akademickém světě a později v průmyslu.


**Poznámka**: v té době ještě informatici neměli k dispozici Linux (který se objeví až na začátku 90. let) ani Minix, vzdělávací systém navržený Andrewem Tanenbaumem.  Hlavní možností byl Unix nebo někdy proprietární mainframy jako OpenVMS. Díky své flexibilitě a otevřenosti se Unix zasloužil o rozšíření prvních síťových konceptů.


Přesně řečeno, TCP/IP není jediný protokol, ale sada protokolů postavená na TCP a IP. Proslavil se, protože poskytl standardizovaný programovací protokol Interface pro výměnu dat mezi počítači ve stejné síti. Tento protokol Interface, založený na primitivech zvaných "sockety", umožnil vytvářet spolehlivá a flexibilní spojení a zároveň integrovat základní aplikační protokoly.


ARPANET je tedy historickým základem dnešního Internetu. Internet je globální síť založená na principu přepojování paketů, kde se informace šíří pomocí sady standardizovaných protokolů, které zajišťují kompatibilitu a interoperabilitu mezi různorodými systémy. Tato otevřená architektura umožnila vývoj a nasazení bezpočtu služeb a aplikací, včetně např:


- e-maily,
- world Wide Web (www),
- přenos a sdílení souborů...


Na řízení a vývoj těchto protokolů dohlíží ***Internet Architecture Board*** (IAB).

Tato organizace koordinuje technické směry prostřednictvím dvou hlavních struktur:


- IRTF** (_Internet Research Task Force_), která provádí dlouhodobý výzkum vývoje a zdokonalování protokolů.
- IETF** (_Internet Engineering Task Force_), která vyvíjí, standardizuje a dokumentuje operační protokoly používané na internetu


Distribuci síťových prostředků (rozsahy IP Address, čísla autonomních systémů, kořenová doménová jména atd.) koordinuje na mezinárodní úrovni **IANA/ICANN**. Provozní řízení se opírá o: **RIR** (*Regionální internetové registry*): **RIPE NCC** (Evropa, Střední východ, Střední Asie), **ARIN**, **APNIC**, **LACNIC** a **AFRINIC**.


Všechny specifikace protokolů TCP/IP jsou zaznamenány v dokumentech zvaných **RFC** (_Request For Comments_), které slouží jako autoritativní technické odkazy. Dokumenty RFC jsou průběžně aktualizovány a číslovány, aby odrážely neustálý vývoj sady protokolů.


Zásobník TCP/IP je často představován jako zásobník čtyř funkčních vrstev, často srovnávaný se sedmi vrstvami modelu **OSI** (_Open Systems Interconnection_) vyvinutého organizací **ISO** (_International Standards Organization_), který slouží jako koncepční reference pro sítě.


Čtyři vrstvy modelu TCP/IP jsou:


- nETWORK ACCESS Layer, který zajišťuje protokoly řízení fyzického spojení a přístupu k médiím;
- iNTERNET Layer, který zajišťuje směrování a adresování IP;
- tRANSPORT Layer, který zaručuje spolehlivost a správu datových toků pomocí protokolů, jako je TCP nebo UDP ;
- aPLIKACE Layer, která sdružuje uživatelské a softwarové protokoly, například HTTP, FTP, SMTP a DNS.



![Image](assets/fr/006.webp)



Dnes je nejrozšířenější verzí protokolu IPv4, ale jeho 32bitový prostor Address má jasná omezení. To vedlo k vytvoření protokolu IPv6, který používá 128bitové adresování a nabízí prakticky neomezenou kapacitu: je nezbytný pro podporu prudkého nárůstu připojených zařízení a řešení problémů internetu věcí, mobility a bezpečnosti.


Každá část Layer zásobníku TCP/IP poskytuje specifické služby, což umožňuje modulární Address řešení různých síťových potřeb: fyzický přenos, logické adresování, integrita dat a služby na aplikační úrovni.


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

## Protokol IPv5 QoS


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



Záhlaví paketu IP je základní datová struktura rozdělená do několika polí, z nichž každé má specifickou úlohu, která zajišťuje správný přenos a zpracování paketů při jejich průchodu sítí. Tato pole zahrnují cílovou adresu IP Address (potřebnou pro směrování paketu k zamýšlenému příjemci), délku záhlaví udávanou polem IHL (*Internet Header Length*), celkovou délku paketu zaznamenanou v poli *Total Length*, kontrolní a ověřovací informace a další parametry pro řízení toku a kvality komunikace.


Úplně první pole v záhlaví se nazývá Verze. Tato čtyřbitová hodnota určuje, jakou verzi protokolu IP paket používá. Je důležitá, protože každému směrovači nebo zprostředkujícímu zařízení říká, jak má zapouzdřená data interpretovat a zpracovávat.


**Poznámka: správu a Assignment verzí protokolu IP zajišťuje **IANA**. Čtyřbitové pole umožňuje 16 binárních kombinací (hodnoty 0 až 15). Jejich aktuální hodnoty Assignment jsou:



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

Mezi ně patří IPv5, který, ačkoli je veřejnosti z velké části neznámý, existoval jako ST (_Stream Protocol_). Protokol IPv5, vyvinutý v 80. letech 20. století, byl navržen jako Address, což byla v té době rostoucí potřeba: poskytovat "_kvalitu služby_" (QoS) pro určité datové toky, které vyžadovaly nepřetržitý a stabilní přenos, jako například přenos hlasu přes IP nebo multimediální toky. Jeho cílem bylo zaručit koncovou šířku pásma a prioritu, což je podobný koncept, jaký dnes nabízí protokol RSVP (_Resource Reservation Protocol_) pro dynamické rezervování síťových zdrojů v moderních směrovačích.


Protokol IPv5 však zůstal experimentální a byl implementován pouze v malém počtu síťových zařízení. Jeho omezené přijetí spolu s rychle rostoucí potřebou většího prostoru Address vedlo tvůrce internetu k přímému přechodu z IPv4 na IPv6. Tím se vyhnuli jak omezením Address protokolu IPv4, tak riziku záměny nebo nekompatibility s experimentálními specifikacemi protokolu IPv5.


Ačkoli se protokol IPv5 nikdy nerozšířil, hrál důležitou roli při formování prvních úvah o QoS a řízení provozu. Dnes je spíše historickou značkou než funkčním standardem.


**Připomínka** - Protokol je soubor komunikačních pravidel: datových struktur, algoritmů, formátů paketů a konvencí, které umožňují různým zařízením spolehlivě a srozumitelně Exchange informace. Služba je konkrétní implementace protokolu prostřednictvím konkrétních programů (klientů, serverů), které se těmito pravidly řídí a zpřístupňují funkce uživatelům a aplikacím.


Nyní se můžeme blíže podívat na strukturu a fungování protokolu IP, který je základem veškeré síťové komunikace.



## Protokol IP


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definice a obecné informace


Protokol IP neboli "***Internet Protocol***" je základem modelu TCP/IP. Přenáší datové pakety z jednoho hostitele na druhého v rámci sítě, ať už je místní, nebo se rozprostírá po celém světě. Má dvě klíčové úlohy: spravuje logické adresování zařízení a zajišťuje směrování paketů v často heterogenních a propojených sítích.


Na fyzické úrovni se přenos opírá o hardwarová rozhraní, která vytvářejí spojení mezi uzly typu bod-bod. Komunikaci mezi koncovými body však umožňuje protokol IP, který každému paketu poskytuje informace potřebné k tomu, aby mohl projít více možnými cestami ke svému cíli.


Tři konfigurace sítě Elements určují, jakým způsobem bude paket odeslán na svou cestu:


- IP Address**: jednoznačně identifikuje cílového hostitele v síti.
- Maska podsítě**: určuje, která část čísla Address identifikuje síť a která část hostitele, což umožňuje logické rozdělení do podsítí.
- Brána**: označuje zprostředkující směrovač, přes který má paket projít, aby se dostal do vnější sítě nebo jiného segmentu místní sítě.


Na internetu neproudí data jako jeden souvislý proud, ale posílají se jako **datagramy**: nezávislé bloky dat, z nichž každý obsahuje všechny informace potřebné k doručení. Jedná se o princip **přepínání paketů**, kdy jsou informace rozděleny do samostatných jednotek, které mohou k jednomu příjemci dojít různými cestami.


Kromě užitečného zatížení (*payload*) obsahuje každý datagram IP strukturovanou hlavičku s poli, jako je cílový Address, zdrojový Address, typ služby, číslo verze protokolu a další kontrolní informace potřebné pro řízení přenosu.


Teoretická maximální velikost datagramu IP je **65 536 oktetů**, což je limit stanovený polem celkové délky v záhlaví. V praxi se této velikosti dosahuje jen zřídka, protože fyzické sítě přenášející pakety (Ethernet, Wi-Fi, optické sítě...) obvykle stanovují přísnější limity známé jako **MTU** (_Maximum Transmission Unit_). Pokud datagram překročí MTU fyzické linky, musí být rozdělen na menší pakety, z nichž každý je odeslán samostatně a po příchodu znovu složen.


Díky této přizpůsobivosti je protokol IP robustní a flexibilní a je schopen pracovat v široké škále základních technologií při zachování univerzální kompatibility mezi různorodými systémy a sítěmi.



### Fragmentace datagramů IP


Pokud má datagram IP projít sítí, jejíž přenosová kapacita je menší než samotný datagram, musí být **fragmentován**, aby mohl bez problémů projít. Tento limit fyzické velikosti se nazývá **MTU** (Maximum Transmission Unit): největší velikost rámce, který může projít danou sítí bez rozdělení.


Každá síťová technologie má svou vlastní MTU, která je určena vlastnostmi hardwaru a protokolu. Mezi běžné hodnoty patří:


- ARPANET**: 1000 bajtů
- Ethernet**: 1500 bajtů
- FDDI**: 4470 bajtů


Pokud datagram překročí MTU síťového segmentu, kterým musí projít, směrovací zařízení jej rozdělí na menší **fragmenty**, které splňují limit. K tomu obvykle dochází při přechodu ze sítě s vysokou MTU na síť s nižší kapacitou. Například datagram přicházející ze sítě FDDI může být nutné před odesláním přes segment sítě Ethernet fragmentovat.



![Image](assets/fr/008.webp)



Proces fragmentace probíhá následovně:


- Směrovač rozdělí datagram na fragmenty, které nejsou větší než MTU cílové sítě.
- Velikost každého fragmentu je násobkem 8 bajtů, protože protokol IP používá tuto jednotku k zakódování posunu při opětovném sestavování.
- Každý fragment dostane vlastní hlavičku IP, která obsahuje informace potřebné pro konečného příjemce k jejich opětovnému sestavení ve správném pořadí.


Jakmile jsou fragmentovány, putují po síti nezávisle na sobě. V závislosti na směrovacích tabulkách, zatížení linek nebo výpadcích mohou volit různé trasy. Není zaručeno, že dorazí v pořadí, v jakém byly odeslány.


Po příjezdu se přijímací stroj postará o **přemontování**. Pomocí informací v záhlaví (sdílený identifikátor, offset a příznaky fragmentace) sestaví fragmenty ve správném pořadí a zrekonstruuje původní datagram před jeho odesláním dalšímu Layer. Pokud je ztracen nebo poškozen byť jen jeden fragment, je obvykle celý datagram zahozen, bez každého fragmentu by byl výsledek neúplný nebo nepoužitelný.


Fragmentace a opětovné sestavení jsou sice efektivní, ale mají i své nevýhody: dodatečné zpracování směrovači a hostiteli a vyšší pravděpodobnost ztráty paketů, což může zvýšit počet opakovaných přenosů. Proto je pro hladkou a efektivní komunikaci IP důležitá pečlivá správa MTU a optimalizace velikosti paketů.



### Zapouzdření dat


Aby bylo zajištěno správné směrování dat mezi jednotlivými vrstvami modelu TCP/IP, hraje klíčovou roli proces **zapouzdření**. V každé fázi, kdy zpráva putuje z aplikace odesílatele do počítače příjemce, se přidávají další informace, známé jako hlavičky. Tyto hlavičky poskytují zprostředkujícím zařízením a softwarovým vrstvám instrukce, které potřebují ke zpracování, doručení a případnému opětovnému sestavení dat.


Při odesílání zprávy prochází zpráva čtyřmi vrstvami zásobníku TCP/IP. V každé části Layer se před stávající data přidá nová hlavička: každá hlavička obsahuje specifická metadata, jako jsou logické nebo fyzické adresy, komunikační porty, sekvenční čísla, příznaky řízení chyb a veškeré informace potřebné pro řízení přenosu a směrování.


Předávání se tedy řídí strukturovaným procesem:


- Aplikace Layer vytvoří počáteční **zprávu** obsahující nezpracovaná data.
- Transportní modul Layer jej zapouzdří do **segmentu** a přidá zdrojový a cílový port, sekvenční čísla a mechanismy řízení toku.
- Internet Layer přidá k segmentu hlavičku IP a vytvoří tak **datagram**, v němž jsou uvedeny zdrojová a cílová adresa IP.
- Přístup k síti Layer zabalí datagram do rámce**, přidá adresy MAC a kontrolní kódy integrity (CRC).



![Image](assets/fr/009.webp)



Tento proces zapouzdření zajišťuje jak integritu a sledovatelnost dat, tak i jejich přizpůsobivost: při přechodu z jedné sítě do druhé poskytují hlavičky zařízením informace potřebné k výběru trasy, kontrole platnosti nebo případné fragmentaci.


Po příchodu je proces obrácený: přijímací stroj dostane rámec do zařízení Network Access Layer, které přečte a odstraní příslušnou hlavičku. Datagram je poté předán internetovému počítači Layer, který přečte hlavičku IP a zase ji odstraní, aby mohl segment doručit transportnímu počítači Layer. Transportní Layer zpracuje transportní hlavičky, zkontroluje integritu datového toku a nakonec doručí **zprávu** cílové aplikaci v původním stavu.



![Image](assets/fr/010.webp)



Transformaci dat u každého Layer lze shrnout takto:


- Zpráva**: blok informací v aplikaci Layer.
- Segment**: datová jednotka po zapouzdření transportní jednotkou Layer.
- Datagram**: forma, která vznikne po přidání hlavičky IP internetovou službou Layer.
- Rámec**: konečný blok připravený k přenosu přes fyzické médium prostřednictvím zařízení Network Access Layer.



![Image](assets/fr/011.webp)



Tento proces, který je nezbytný pro spolehlivost a univerzálnost internetové komunikace, zajišťuje, že každá část dat, bez ohledu na to, jak je roztříštěná nebo složitá, může být přenesena od konce do konce a zároveň zůstane srozumitelná a použitelná pro přijímající zařízení.



### Adresování IP


I po zavedení přepínání paketů, fragmentace a zapouzdření by síť nemohla fungovat bez spolehlivého systému adresování. Aby bylo zajištěno, že každý datový paket dorazí ke správnému příjemci, používá internetová síť Layer jedinečný identifikátor: **IP Address**.

V protokolu IPv4 je IP adresa Address kódována na **32 bitů** a zapsána jako čtyři desetinná čísla oddělená tečkami ve známém formátu N1.N2.N3.N4 (například: 192.168.1.12).


Protokol IP Address má dvě části:


- _netid_**: identifikuje síť, do které hostitel patří
- _hostid_**: identifikuje konkrétního hostitele v dané síti

Toto rozdělení umožňuje logicky strukturovat globální internet do mnoha vzájemně propojených sítí.


Historicky se systém IPv4 opíral o schéma založené na třídách s označením od A do E, které definovalo rozsah Address a jejich zamýšlené použití. Každá třída přidělovala stanovený počet bitů _netid_ a _hostid_, což přímo ovlivňovalo možný počet sítí a hostitelů.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Hostitelům nelze přiřadit všechny možné hodnoty. Například v **třídě C** Address nabízí poslední bajt 8 bitů (256 hodnot). Dva z nich jsou však vyhrazeny:


- 0: identifikuje samotnou síť
- 255: je **rozesílání** Address, které se používá k odeslání paketu všem hostitelům v síti najednou.

Zbývá tedy 254 použitelných adres pro zařízení.


Počet dostupných adres se v jednotlivých třídách značně liší: od velkých veřejných sítí ve třídě A přes podnikové sítě ve třídě B až po menší místní sítě ve třídě C.



![Image](assets/fr/013.webp)



Některé rozsahy Address jsou vyhrazeny pro soukromé použití a nikdy nejsou směrovány přímo do internetu. Tyto adresy se označují jako **soukromé adresy** a používají se uvnitř organizací, podniků nebo domácností a pro přístup do veřejného Internetu vyžadují překlad Address, obvykle NAT (*Network Address Translation*). Jedná se o tyto adresy:


- Třída A**: od 10.0.0.0 do 10.255.255.255
- Třída B**: od 172.16.0.0 do 172.31.255.255
- Třída C**: od 192.168.0.0 do 192.168.255.255


Když zařízení s privátním kódem Address přistupuje k Internetu, směrovač nebo brána s podporou NAT jej nahradí platným veřejným kódem Address.


Příklad: Pokud má hostitel adresu Address **192.168.7.5**, můžeme odvodit:


- 192.168.7.0: síť Address
- 192.168.7.1: často místní směrovač
- 192.168.7.5: samotný hostitel


Dalším zvláštním případem je **127.0.0.1**, známý jako "***loopback***".

V systémech Linux je přidružena ke klávese Interface **lo**. Tento Address umožňuje počítači, aby se sám připojil k Address pro místní testování nebo diagnostiku, aniž by musel procházet přes fyzický Interface. Pro tento účel je vyhrazen celý rozsah **127.0.0.0/8**.


Pro optimalizaci použití Address a návrh složitých sítí je důležitá **maska podsítě** (_netmask_). Tato binární maska odděluje _netid_ od _hostid_ v IP Address.

Každá třída má výchozí masku:


- 255.0,0,0** pro třídu A,
- 255.255.0.0** pro třídu B,
- 255.255.255.0** pro třídu C.


Správný návrh sítě se řídí základním pravidlem: zařízení, která musí komunikovat přímo, by měla být ve stejné síti nebo podsíti. K segmentaci sítě používáme podsíťování, tedy rozdělení sítě na menší podsítě pomocí specifičtější masky.


Příklad podsítě:

Síť **třídy C**: 192.168.1.0/24 s výchozí maskou 255.255.255.0.

Chceme 4 podsítě po 60 hostitelích.


**Krok 1**: Počet potřebných adres na podsíť = 60 + 2 rezervované adresy (síťové + vysílací) = 62.


**Krok 2**: Najděte nejbližší mocninu čísla 2 ≥ 62. -> 2⁶ = 64.


**Krok 3: Upravte masku. Ponechte bity _netid_ a vyhraďte potřebné bity _hostid_. Získáme binární masku, která po převodu dává **255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Krok 4**: Vypočítejte rozsahy Address pro každou podsíť a měňte bity vyhrazené pro hostitele.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Krok 5**: Tím se vytvoří čtyři podsítě, z nichž každá podporuje až 62 strojů, přičemž celkové adresovací schéma zůstane efektivní. Část _hostid_ je rozdělena na část _subnetid_ a část hostitele.



![Image](assets/fr/016.webp)



Tento základní princip vytváření podsítí je v moderním síťovém inženýrství stále nepostradatelný, protože umožňuje přesné přidělování IP adres, lepší řízení provozu, silnou izolaci segmentů a škálovatelnou správu sítě.



### Adresování CIDR


Na počátku 90. let, kdy se Internet rychle rozšířil mezi podniky a organizacemi, začal tradiční systém adresování IP založený na třídách (A, B, C) vykazovat své limity.

Její rigidní struktura vedla ke značnému plýtvání IP adresami a způsobila, že směrovací tabulky byly stále rozsáhlejší, složitější a obtížněji udržovatelné.

Pro řešení těchto problémů byla zavedena pružnější a účinnější metoda: **CIDR** (_Classless Inter-Domain Routing_). CIDR se postupně stal standardem a z velké části nahradil starý systém založený na třídách.


Základní myšlenkou CIDR je možnost seskupit několik sousedících sítí, zejména bloků třídy C, do jedné logické jednotky zvané **supernet** (_supernet_). Díky této agregaci může jedna položka ve směrovací tabulce představovat více podsítí, což snižuje počet tras, které musí směrovače zpracovávat, a zvyšuje jejich výkon.


Zatímco sítě třídy C původně potřebovaly agregaci nejvíce kvůli své menší kapacitě, tento princip se uplatnil také u sítí třídy B a teoreticky i u sítí třídy A, i když těch se to týká méně díky jejich velkému rozsahu Address.


V případě CIDRu koncept pevných tříd mizí. S prostorem Address se zachází jako se spojitým rozsahem, který lze podle potřeby rozdělit nebo agregovat. Bloky CIDR jsou definovány pomocí masek podsítí, které nejsou omezeny na výchozí třídy A, B nebo C. Blok CIDR může představovat buď jednu síť, nebo souvislou sadu podsítí sdílejících stejný prefix.


Blok CIDR se zapisuje ve formátu "Address/prefix", kde číslo za lomítkem udává, kolik bitů tvoří síťovou část. Například /17 znamená, že prvních 17 bitů identifikuje síť, zatímco zbývajících 15 bitů identifikuje hostitele.


Příklad:

Blok /17 obsahuje 2^(32-17) adres, takže 2^15 = 32 768 celkových adres. Po odečtení dvou rezervovaných adres (síťové a broadcastové) zbývá 32 766 použitelných hostitelských adres. To umožňuje správcům sítě zvolit velikost podsítí přesně podle skutečných potřeb a zamezit tak zbytečnému plýtvání.


Pro snazší pochopení velikosti CIDR uvádíme tabulku běžných prefixů a jejich ekvivalentních masek podsítí a použitelných adres:


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


**POZNÁMKA**: Historicky se v RFC 950 nedoporučovalo používat podsíťovou nulu, hlavně proto, aby se předešlo zmatkům při směrování.  Toto omezení se stalo zastaralým s RFC 1878, které jeho použití plně povoluje. Staré omezení bylo způsobeno především nekompatibilitou se starším hardwarem, který neuměl správně zpracovávat CIDR. Moderní zařízení takový problém nemají.


Například podsíť **1.0.0.0** s maskou podsítě **255.255.0.0**, která byla dříve nejednoznačná s identifikátorem sítě třídy A, je nyní zcela platná a použitelná.


**TIP**: pro bezchybné výpočty podsítí a rychlý převod adres do notace CIDR jsou k dispozici praktické nástroje jako ***ipcalc***. Tato "síťová kalkulačka" přehledně zobrazuje rozdělení Address, dostupné rozsahy a související masky, což je ideální pro správce i studenty, kteří se učí CIDR.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## Protokol TCP


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



Protokol **TCP** (_Transmission Control Protocol_) hraje ústřední roli v modelu TRANSPORT Layer protokolu TCP/IP. Funguje jako most mezi aplikacemi a internetovou sítí Layer a zajišťuje spolehlivý přenos dat mezi dvěma vzdálenými počítači.

Zatímco protokol IP pouze odesílá pakety bez záruky doručení nebo pořadí, protokol TCP zajišťuje integritu a konzistenci datového toku, doručuje je beze ztrát, ve správném pořadí a bez duplicit.


Mezi hlavní povinnosti TCP patří:


- Změna pořadí přijatých segmentů;
- Sledování toku dat, aby se zabránilo přetížení;
- Rozdělení nebo opětovné složení datových bloků do vhodných jednotek (segmentů);
- Správa navazování a ukončování spojení mezi oběma konci komunikace.


Protokol TCP je protokol orientovaný na připojení, což znamená, že vytváří explicitní, trvalý vztah mezi klientem a serverem. K tomu používá **pořadová čísla** a **potvrzení**: každému odeslanému segmentu je přiřazen jedinečný identifikátor, takže přijímající počítač může zkontrolovat pořadí i integritu dat. Příjemce pak vrátí potvrzovací segment s příznakem **ACK** nastaveným na 1, který potvrzuje příjem a udává další očekávané pořadové číslo.



![Image](assets/fr/018.webp)



Pro zvýšení spolehlivosti používá protokol TCP časovač: po odeslání segmentu se spustí odpočítávání. Pokud potvrzení nepřijde během časového limitu, odesílatel automaticky odešle segment znovu, přičemž předpokládá, že byl ztracen při přenosu. Tento mechanismus automatického opakovaného přenosu vyrovnává ztráty vlastní sítím IP, které mohou nastat v případě přetížení, chyb směrování nebo selhání hardwaru.



![Image](assets/fr/019.webp)



Protokol TCP je schopen detekovat a zpracovávat duplicity. Pokud dorazí retransmitovaný segment, ale objeví se i originál, příjemce pomocí sekvenčních čísel identifikuje duplikát a ponechá si pouze správnou kopii, čímž se odstraní jakákoli nejasnost.


Aby tento proces fungoval, musí oba stroje sdílet společnou představu o svých počátečních pořadových číslech. To je zajištěno dodržováním přísného postupu připojení: na jedné straně **server** naslouchá na určitém portu a čeká na příchozí požadavek (pasivní režim); na druhé straně **klient** aktivně zahájí připojení odesláním požadavku serveru na stejný servisní port.


**POZNÁMKA**: Port je číselný identifikátor (od 0 do 65 535) přiřazený síťové aplikaci v počítači. Používá se k rozlišení více služeb běžících současně na stejném IP Address. Když klient odesílá data, uvede číslo portu, aby operační systém serveru věděl, který program je má přijmout (např. 80 pro HTTP, 443 pro HTTPS, 25 pro SMTP). Porty fungují jako vyhrazené dveře, směrují provoz dovnitř a ven, zabraňují záměně služeb a umožňují jemné řízení přístupu pomocí firewallů nebo pravidel filtrování.


Synchronizace sekvence Exchange je založena na známém mechanismu **"*třístranného podání ruky*"**, podobně jako když se dva lidé při navazování kontaktu pozdraví. Tato inicializační fáze, která zajišťuje spolehlivost protokolu TCP, probíhá ve třech fázích:

1. **SYN:** Klient odešle počáteční synchronizační segment (**SYN**) s nastaveným příslušným příznakem a počátečním sekvenčním číslem (např. C);

2. **SYN-ACK:** Přijímající server odpoví potvrzovacím segmentem (**SYN-ACK**), potvrdí klientovo sekvenční číslo a poskytne své vlastní počáteční sekvenční číslo;

3. **ACK:** Klient odešle závěrečné potvrzení (**ACK**), kterým potvrdí přijetí sekvenčního čísla serveru a ukončí synchronizaci. Příznak SYN je nyní vypnut a příznak ACK zůstává nastaven, což znamená, že spojení je navázáno.



![Image](assets/fr/020.webp)



Tento protokol Exchange zajišťuje, že obě strany sdílejí stejnou číslovací základnu před přenosem dat užitečného zatížení. Jakmile je tato synchronizace dokončena, je relace otevřena: segmenty nyní mohou cestovat oběma směry, přičemž každý z nich je po přijetí potvrzen, což zajišťuje maximální spolehlivost datového toku.


Tento ***three-way handshake*** se týká pouze navázání spojení. Pro uzavření spojení používá TCP *čtyřcestný handshake*: FIN → ACK → FIN → ACK, který zaručuje, že před úplným uvolněním spojení nedojde ke ztrátě žádného přenášeného segmentu.


Ačkoli byl tento proces navržen s ohledem na robustnost a spolehlivost, vznikly v něm také zranitelnosti, které lze zneužít. Například útoky jako **IP Spoofing** mají za cíl obejít nebo narušit tento vztah důvěry tím, že se vydávají za autorizovaný stroj prostřednictvím zfalšovaných sekvenčních čísel, čímž vytvoří průlom umožňující zachycení nebo manipulaci s datovým tokem.


K omezení rizika únosu synchronizace sekvencí a k řízení zatížení sítě používá protokol TCP techniku řízení toku známou jako "**_Sliding Window_**". Tento systém reguluje, kolik dat může být odesláno, aniž by bylo vyžadováno okamžité potvrzení pro každý segment, čímž se snižuje zbytečné přetížení sítě při zachování dobré spolehlivosti.


Z praktického hlediska definuje klouzavé okno rozsah sekvenčních čísel, která mohou volně obíhat mezi odesílatelem a příjemcem, aniž by byl potvrzen každý jednotlivý segment. Jakmile odesílající systém obdrží potvrzení, okno se "posune": posune se doprava a vytvoří prostor pro odeslání nových segmentů. Velikost tohoto okna (rozhodující pro optimalizaci propustnosti a zamezení přetížení) je uvedena v poli "*Window*" v hlavičce TCP.


**Příklad**: Pokud je počáteční sekvenční číslo 3 a okno se rozšíří na sekvenci 5, lze segmenty s čísly 3 až 5 odeslat bez čekání na jednotlivá potvrzení.



![Image](assets/fr/021.webp)



Velikost klouzavého okna není pevně stanovena, ale dynamicky se přizpůsobuje podmínkám sítě a kapacitě zpracování přijímače.  Pokud je příjemce schopen zpracovat větší objem dat, oznámí to prostřednictvím pole Okno a vyzve odesílatele, aby své okno rozšířil. Naopak v případě přetížení nebo rizika nasycení může příjemce požádat o zmenšení, odesílatel počká, až se okno posune dopředu, aby mohl odeslat další segmenty.


Protokol poskytuje symetrický postup pro uzavření spojení TCP, aby bylo zajištěno čisté a řádné ukončení. Kterýkoli stroj může iniciovat uzavření odesláním segmentu s příznakem **FIN** nastaveným na hodnotu 1, čímž signalizuje svůj záměr ukončit komunikaci. Poté počká, dokud nebudou přijaty všechny segmenty v přenosu, a ignoruje další data.


Po přijetí tohoto segmentu pošle druhý stroj potvrzení, rovněž označené příznakem FIN. Poté dokončí odesílání zbývajících dat a informuje místní aplikaci, že koekce byla uzavřena. Toto dvojí potvrzení zajišťuje řádné ukončení a minimalizuje riziko ztráty dat.


Toto přesné řízení, které kombinuje flexibilní směrování protokolu IP s přísnou kontrolou protokolu TCP, se často ilustruje diagramem, který porovnává rychlost protokolu IP (který pracuje na základě **"nejlepšího úsilí "** bez záruky doručení) se spolehlivostí protokolu TCP (který řídí přenos pomocí potvrzení a dohodnutých sekvencí).



![Image](assets/fr/022.webp)



V některých případech však není prioritou absolutní spolehlivost, ale rychlost a jednoduchost. To platí pro aplikace, jako je živé vysílání nebo VoIP, které mohou tolerovat určitou ztrátu paketů, aniž by to mělo vážný vliv na uživatelský komfort. V takových případech se dává přednost protokolu **UDP** (_User Datagram Protocol_).


Protokol UDP funguje na zásadně odlišném principu než protokol TCP: je **bez spojení**, což znamená, že mezi odesílatelem a příjemcem není navázán žádný předchozí vztah. Když počítač posílá pakety prostřednictvím protokolu UDP, jsou přenášeny jednosměrně; příjemce neposílá potvrzení a odesílatel nemá žádné potvrzení, že zpráva dorazila. Záhlaví protokolu UDP je záměrně minimální, obsahuje pouze zdrojový port, cílový port, délku segmentu a kontrolní součet, bez zabudovaného mechanismu potvrzování nebo kontroly stavu. Adresy IP jsou jako vždy přenášeny základní hlavičkou IP.


Běžně se používá přirovnání, že protokol TCP je jako **telefonní hovor**, kdy je vytvořen okruh, který je v průběhu hovoru sledován a kontrolován. Zatímco protokol UDP je jako **posílání pošty**, kdy odesílatel vhodí dopis do poštovní schránky bez okamžitého důkazu o doručení nebo systematické zpětné vazby.


Tato komplementarita mezi protokoly TCP a UDP umožňuje moderním sítím přizpůsobit se různým potřebám a v závislosti na aplikaci zvolit maximální spolehlivost nebo upřednostnit rychlost.



## Primitiva služeb


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Vrstevnatá architektura a organizace Exchange


Jak jsme viděli, **služby** jsou konkrétní implementací protokolů, které jsme dosud popsali. Model TCP/IP se sice liší od modelu **OSI**, ale používá stejný vrstvený přístup: každý Layer je navržen tak, aby vykonával konkrétní funkci a poskytoval **služby** Layer, které jsou přímo nad ním, což vede k modulární, robustní a snadno udržovatelné architektuře.


Každá jednotka Layer staví na schopnostech té, která je pod ní, a na oplátku poskytuje nadřazené jednotce Layer konzistentní jednotku Interface pro správu dat. V této architektuře má každý Layer své vlastní **datové struktury**, pečlivě definované tak, aby byla zajištěna dokonalá kompatibilita s ostatními vrstvami. Tato kompatibilita je nezbytná pro hladkou, spolehlivou a jasnou komunikaci z jednoho koncového bodu do druhého.


Tyto výměny se řídí dvěma klíčovými aspekty:


- Vertikální aspekt**: vztah mezi jedním Layer a nad ním nebo pod ním (od Layer N ke Layer N+1 a naopak).



![Image](assets/fr/023.webp)




- Horizontální aspekt**: interakce mezi vzdálenými aplikacemi, tj. dialog mezi **klientem** a **serverem**, a to v obou směrech.



![Image](assets/fr/024.webp)



Vrstevnatá architektura se řídí zásadou, že každý systém Layer zpracovává pouze informace, které spadají do jeho působnosti: datové struktury, hlavičky a kontrolní mechanismy se v jednotlivých systémech Layer liší, ale dohromady tvoří ucelený systém, který zajišťuje, že data jsou postupně směrována ke svému cíli.


**Připomínka**: Pro popis datových jednotek vyměňovaných mezi vrstvami se používá specifická terminologie:


- zpráva** pro aplikaci Layer,
- segment** pro Transport Layer (TCP),
- datagram** pro internet Layer (IP),
- rámce** pro zařízení Network Access Layer.


Níže uvedená tabulka shrnuje pojmy pro kontexty TCP a UDP:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Primitiva služeb a datové jednotky


Jádrem tohoto systému jsou **primitiva služeb**, která fungují jako komunikační rozhraní. Tyto primitivy fungují jako servisní přepážky, naslouchají na vyhrazených specifických **portech** a umožňují procesům navazovat, udržovat a ukončovat síťová spojení řízeným způsobem. Zatímco protokoly organizují formát a přenos dat po síti, jsou to právě **služby a jejich primitiva**, které zajišťují vertikální spojení mezi jednotlivými vrstvami.


Kombinací horizontálního aspektu (komunikace mezi distribuovanými aplikacemi) a vertikálního aspektu (vnitřní interakce mezi vrstvami) poskytuje model TCP/IP kompletní škálovatelnou architekturu. Překrytí těchto dvou hledisek poskytuje jasný přehled o tom, jak se vyměňují data ve strukturované síťové komunikaci.



![Image](assets/fr/026.webp)



### Shrnutí části


V této první velké části jsme se zabývali základní architekturou, která řídí konfiguraci a provoz dnešních sítí připojených k internetu. Tato architektura je založena na modelu **čtyř Layer** inspirovaném modelem OSI a postaveném na sadě protokolů **TCP/IP**, která je páteří moderní komunikace. Viděli jsme, že protokol TCP se svým přístupem orientovaným na spojení zajišťuje spolehlivé přenosy, zatímco lehčí a rychlejší protokol UDP je upřednostňován v případech, kdy je rychlost důležitější než spolehlivost.


Správné fungování tohoto modelu závisí na implementaci protokolů prostřednictvím **servisních primitiv**. Ty zajišťují propojení mezi jednotlivými vrstvami a umožňují přizpůsobit zpracování dat specifickým požadavkům jednotlivých úrovní, od přenosu po aplikaci, včetně přístupu k internetu a síti. Díky tomuto modulárnímu přístupu je systém flexibilní a robustní.


Dalším základním kamenem této infrastruktury je adresování IP. Každé připojené zařízení je identifikováno pomocí **unikátního IP Address**, převzatého z prostoru Address uspořádaného do **tříd** (od A do E). Některé z těchto adres jsou vyhrazeny pro speciální účely, jako je místní zpětná smyčka nebo multicast, zatímco jiné, známé jako "soukromé adresy", nejsou směrovány přes internet bez překladu (NAT). Tato klasifikace umožňuje logické, hierarchické uspořádání sítí.


Prozkoumali jsme také koncept **podsítí**, který umožňuje rozdělit segmenty sítě pro lepší správu zdrojů IP a optimalizaci toku dat. I když ruční dělení pomocí masek podsítí zůstává důležitým principem, bylo do značné míry modernizováno díky **CIDR** (_Classless Inter-Domain Routing_). Tato metoda změnila správu Address tím, že umožnila pružnější a racionálnější přidělování rozsahů IP a zároveň snížila velikost směrovacích tabulek.


Zvládnutím těchto pojmů - vrstev, protokolů, primitivů služeb, adresování a podsítí - získáte pevný základ pro pochopení technického fungování moderních sítí a pro efektivní konfiguraci síťové infrastruktury podle dnešních potřeb.


V příští části se podrobněji podíváme na adresování IPv4.



# Adresování IPv4


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Použití protokolu IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



V této části půjdeme hlouběji a podíváme se, jak jsou adresy **IPv4** skutečně implementovány v reálné síti. Rozebereme jejich formát, logiku, která za nimi stojí, a jejich propojení s dalšími klíčovými síťovými adresami Elements, jako jsou **jména DNS**, **adresy MAC**, **podsítě** a **techniky překladu**.


IP Address je jedinečný číselný identifikátor přidělený každému **síťovému Interface** v zařízení. Umožňuje lokalizovat toto zařízení v rámci sítě a dosáhnout na něj za účelem přenosu dat. Například směrovač, server, pracovní stanice, síťová tiskárna nebo i sledovací kamera mají alespoň jeden vlastní IP Address. IP Address umožňuje **směrování**, tj. přesun paketů z bodu A do bodu B, i když jsou fyzicky daleko od sebe.


IP adresy lze přidělovat dvěma hlavními způsoby:


- Statické**: Ruční nastavení v zařízení.
- Dynamický**: DHCP (_Dynamic Host Configuration Protocol_). Protokol DHCP zjednodušuje správu sítě, protože eliminuje nutnost ruční konfigurace a zároveň umožňuje přesnou kontrolu prostřednictvím rezervací a doby trvání pronájmu.


*adresy *IPv4** se zapisují v **32bitovém** formátu rozděleném na **čtyři bajty**. Každý bajt obsahuje 8 bitů a představuje desítkové číslo od 0 do 255. Tyto 4 bajty jsou odděleny tečkami, aby tvořily jasný a čitelný zápis.


příklad: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Každý bit v bajtu má svou hodnotu (neboli "váhu"): levý bit (nejvýznamnější bit) má hodnotu 128, další 64, pak 32, 16, 8, 4, 2 a 1 pro pravý bit (nejméně významný bit). Tímto způsobem se binární zápis převádí na desítkovou soustavu prostým sečtením nastavených vah.


Tuto shodu ilustruje následující tabulka:



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

Chcete-li převést binární číslo na desítkové, sečtěte váhy bitů, které jsou nastaveny na 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

Adresa IP Address identifikuje jednu **síť Interface**, nikoli celé zařízení. Víceportový směrovač nebo brána firewall má více rozhraní, každé s vlastním IP Address. Jeden Interface může mít dokonce několik IP adres (například pro obsluhu více virtuálních sítí nebo služeb).


Každý paket IP obsahuje v záhlaví dvě adresy IP:


- Zdroj Address (**odesílatel**)
- Cílová stanice Address (**přijímač**)

Směrovače tyto adresy čtou a určují nejlepší cestu pro odeslání paketu, dokud nedorazí do cíle. Bez přísných adresních pravidel by síťový provoz nemohl být správně směrován a globální propojení sítí by nebylo možné.


Protokol IPv4 Address má dvě části:


- NetID**: identifikuje síť
- HostID**: identifikuje zařízení v dané síti

Maska podsítě** určuje, kde končí NetID a začíná HostID, a určuje, kolik bitů patří každé části. Čím delší je NetID, tím větší je počet možných podsítí, ale počet hostitelů na podsíť se odpovídajícím způsobem snižuje.


Původně byly sítě IPv4 rozděleny do pěti **tříd**: (A, B, C, D a E). Každá třída odpovídá určitému rozsahu NetID a definuje pevnou granularitu:


- Třída A: velmi rozsáhlé sítě s velkým počtem hostitelů
- Třída B: středně velké sítě
- Třída C: malé sítě
- Třída D: adresy vyhrazené pro multicasting (_multicast_)
- Třída E: experimentální adresy, které se nepoužívají pro konvenční adresování



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Zvláštní adresy:


- Síť Address**: Identifikuje samotnou síť (používá se ve směrovacích tabulkách).
- Vysílání Address**: Odesílá data všem zařízením v podsíti najednou (všechny bity HostID nastaveny na 1).


Následující rozsahy jsou vyhrazeny pro interní použití:


- 10.0.0.0/8** (soukromá třída A)
- 127.0.0.0/8** (místní zpětná smyčka nebo _loopback_)
- 172.16.0.0 až 172.31.255.255** (privátní třída B)
- 192.168.0.0 až 192.168.255.255** (privátní třída C)


Adresy **127.0.0.1** a obecněji celý rozsah 127.0.0.0/8 slouží k internímu testování: jakýkoli požadavek na ně zaslaný nikdy neopustí počítač. To je užitečné pro kontrolu, zda místní síťová služba funguje, aniž by se zapojila širší síť.


Pro lepší využití prostoru Address správci často rozdělují sítě na **podsítě** pomocí masek podsítí nebo notace **CIDR** (_Classless Inter-Domain Routing_). CIDR umožňuje přesnější správu a pomáhá zabránit plýtvání adresami. CIDR je dnes nezbytný pro přesné nastavení rozsahů IP a snížení velikosti směrovacích tabulek.


V moderních sítích je IP adresa obvykle spojena s dalšími identifikátory:



- název domény** registrovaný v **DNS** (_Systém doménových jmen_): Přiřazuje číselnou IP adresu Address k názvu, který je vhodný pro člověka.
- MAC Address**: fyzický identifikátor vyrytý do síťové karty, používaný pro místní přenos (_Ethernet_). Když je třeba fyzicky přenést paket IP, tabulka ARP porovná IP Address s MAC Address cíle.


Pro řešení nedostatku protokolu IPv4 Address a pro zvýšení bezpečnosti Layer se v sítích často používá překlad Address (_NAT_). NAT umožňuje mnoha soukromým zařízením sdílet při přístupu k internetu jednu veřejnou IP adresu Address.


**Poznámka**: Výpočty podsítí a masek jsou mnohem jednodušší díky online nástrojům a nástrojům integrovaným v operačním systému, jako je například [Grenoble CRIC calculator](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/).

Tyto nástroje pomáhají efektivně plánovat rozdělení sítě.


Závěrem lze říci, že vysílání Address zůstává praktickou funkcí pro odesílání stejných zpráv všem zařízením připojeným k segmentu: toho se dosáhne nastavením všech bitů v části HostID na hodnotu 1, takže jsou cíleni všichni hostitelé.



## Různé typy protokolu IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



Adresy IPv4 se dělí do dvou hlavních kategorií: veřejné adresy, které jsou přímo přístupné na internetu, a privátní adresy, určené pro interní použití v rámci místní sítě.


Veřejná adresa IPv4 Address je globálně jedinečná a směrovatelná v celém internetu. Přidělují ji oficiální orgány a je vyžadována pro veřejně přístupné služby, jako jsou webové stránky, e-mailové servery nebo cloudová infrastruktura.

Celosvětová jedinečnost těchto adres je nezbytná pro zamezení konfliktů nebo kolizí při směrování.


Distribuci těchto IP rozsahů spravuje **IANA** (_Internet Assigned Numbers Authority_), která spadá pod **ICANN** (_Internet Corporation for Assigned Names and Numbers_). Konkrétně IANA rozděluje prostor IPv4 do 256 bloků o velikosti /8 podle notace CIDR. Každý blok představuje něco přes 16,7 milionu adres (2³² / 2⁸).


Tyto unicastové bloky Address svěřuje IANA **regionálním internetovým registrům** (RIR). Tyto RIR odpovídají za přerozdělování adres na regionální úrovni podle skutečných potřeb poskytovatelů přístupu, společností nebo správních orgánů. Unicastový prostor Address se rozprostírá od bloků **1/8 do 223/8**, přičemž části jsou buď vyhrazeny pro zvláštní účely (výzkum, dokumentace, testování), nebo jsou přiděleny přímo síti nebo RIR k redistribuci.


Chcete-li zjistit, kdo vlastní veřejnou adresu IP Address, můžete nahlédnout do databází RIR pomocí příkazu **whois** nebo pomocí webových rozhraní poskytovaných jednotlivými registry. Pomocí těchto nástrojů lze dohledat Address až k organizaci nebo poskytovateli, který jej deklaroval.


Naopak existují privátní adresy IPv4, které jsou praktickou reakcí na nedostatek veřejných adres. Tyto adresy, které nejsou směrovatelné v Internetu, jsou vyhrazeny pro místní prostředí: podnikové sítě, domácí sítě LAN, datová centra nebo výpočetní klastry. Nejsou celosvětově jedinečné: mnoho privátních sítí může bez rušení používat stejné rozsahy IP, pokud zůstanou izolované nebo používají k přístupu na internet zařízení pro překlad sítě Address.


Aby zařízení s privátní adresou IP Address mohlo přistupovat k internetu, používají sítě NAT (Network Address Translation). NAT funguje tak, že dynamicky nahrazuje soukromou adresu Address veřejnou, což umožňuje desítkám (nebo dokonce stovkám) zařízení sdílet jedinou veřejnou adresu IP Address. Tato metoda optimalizuje využití prostoru IPv4 a také přidává zabezpečení Layer tím, že skrývá vnitřní strukturu sítě.


Další zvláštní kategorií jsou **neurčité** adresy. Zápis IPv4 **0.0.0.0** nebo jeho verze IPv6 **::/128** znamená "žádný konkrétní Address". Takový Address je neplatný jako síťový cíl Address, ale může být použit lokálně hostitelem pro označení "všechna rozhraní" nebo "zatím není přiřazen žádný Address". To je běžné u dynamických Assignment DHCP nebo u naslouchání na všech rozhraních serveru.


Protokol IPv6 podporuje také soukromé adresování, ale standard obecně doporučuje veřejné adresování, aby se zabránilo vrstvení více vrstev NAT. **Lokální adresy** (_site-local_) bloku **fec0::/10** byly z důvodu konzistence a bezpečnosti zrušeny v dokumentu **RFC 3879**. Byly nahrazeny **unikátními lokálními adresami** (_ULA_) umístěnými v bloku **fc00::/7**. ULA umožňují vytvářet privátní sítě IPv6 s čistým vnitřním směrováním pomocí náhodně generovaného 40bitového identifikátoru, který zajišťuje místní jedinečnost.


Vyčerpání IPv4 bylo oficiálně potvrzeno v roce 2011. Aby internetová komunita prodloužila jeho životnost, přijala několik strategií:


- Postupný přechod na **IPv6**
- Rozšířené používání **NAT**
- Přísnější politiky přidělování od RIR, které vyžadují přesné zdůvodnění a řízení potřeb Address
- Zpětné získávání nepoužitých nebo dobrovolně vrácených bloků Address společnostmi


Tato opatření ukazují, že adresování IP není jen technickou výzvou, ale také záležitostí globální správy, která má zásadní význam pro pokračující rozšiřování internetu.



## DNS, adresář Address


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Buďme upřímní, lidé si neumí zapamatovat dlouhé řetězce čísel, ať už v binární nebo desítkové soustavě. Tento problém je ještě větší v případě IP adres, které mohou být složité a jedna IP adresa Address může někdy maskovat více adres, zejména pokud jsou zapojeny techniky jako NAT nebo virtuální hosting.


Aplikace Layer používá systém, který spojuje IP Address s logickým, lidsky čitelným názvem. Tuto úlohu plní **DNS** (*Systém doménových jmen*), masivní, hierarchický, distribuovaný adresář, který přiřazuje čitelná doménová jména k IP adresám. Systém je založen na souboru protokolů a služeb. Nejpoužívanějším softwarem serveru DNS je **BIND** (_Berkeley Internet Name Domain_), softwarový balík s otevřeným zdrojovým kódem, který odkazuje na velkou část internetové infrastruktury DNS.


Základní myšlenka systému DNS je jednoduchá: pro jakoukoli připojenou službu, ať už se jedná o webovou stránku, poštovní server nebo jinou síťovou službu, existuje záznam mapující název domény na jednu nebo více IP adres. To funguje ve dvou směrech:


- Překlad názvu na IP adresu Address.
- Reverzní rozlišení: vyhledání názvu domény přiřazeného k dané IP adrese Address.

Díky tomu je síťové adresování použitelné pro lidi a zároveň je zachována přesnost, kterou směrovače potřebují pro správný přenos dat.


Doménové jméno je vždy hierarchicky strukturováno a jednotlivé úrovně jsou odděleny tečkou: celé jméno se nazývá **FQDN** (_Fully Qualified Domain Name_). Nejpravější část je **TLD** (_Top Level Domain_), například `.com`, `.org` nebo `.fr`. Nejlevější část označuje hostitele, tj. konkrétní stroj nebo službu spojenou s IP adresou Address.


Systém DNS je navržen jako **strom zón**. **Zóna** je část jmenného prostoru domény spravovaná konkrétním serverem DNS. Jedna zóna může obsahovat více **subdomén**, které mohou být delegovány do jiných zón spravovaných různými servery. Správci jsou zodpovědní za údržbu svých zón: zajišťují aktualizace, delegace a celkovou správu.


Tato struktura umožňuje nejen ukazovat na hlavní doménu (např. `example.com`), ale také dolaďovat záznamy pro jednotlivé hostitele (`www`, `mail`, `ftp` atd.). V počátcích sítí se toto mapování provádělo pomocí statických souborů (`/etc/hosts` v unixových systémech), ale takový způsob se rychle stal nepraktickým pro rychle rostoucí a propojený internet.


Je důležité si uvědomit, že server **DNS** může sloužit pouze v omezeném rozsahu. Například interní server DNS společnosti nemusí být přímo přístupný z internetu. Pokud tento server DNS není nakonfigurován pro předávání dotazů nebo nemá důvěryhodný vztah s jinými servery, některé dotazy selžou: název ani IP adresu Address pak nelze přeložit mimo definovanou zónu.


DNS hraje roli také při směrování e-mailů. Například záznam **MX** (_Mail Exchange_) určuje poštovní servery odpovědné za příjem e-mailů pro danou doménu. Tyto záznamy definují priority (váhový faktor) a řešení převzetí služeb při selhání. Soubor zóny serveru DNS musí obsahovat záznam **SOA** (_Start Of Authority_), který označuje server jako oficiální zdroj informací pro danou zónu.


Díky své hierarchické a distribuované struktuře zůstává systém DNS základním kamenem internetu a umožňuje uživatelům přistupovat ke službám prostřednictvím jasných a zapamatovatelných doménových jmen namísto dlouhých technických IP adres.


V příští kapitole se budeme zabývat dalším základním pojmem: **Ethernetové adresy**, známé také jako **Adresy MAC**, které zajišťují doručování dat na fyzickém Layer místních sítí.



## Zjišťování adres sítě Ethernet a protokolu ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definice


Pro spolehlivé a konzistentní fungování protokolu směrování dat je nezbytná jedna klíčová součást. Jako lidé můžeme snadno identifikovat stroj podle jeho IP adresy Address nebo podle jeho názvu získaného prostřednictvím DNS. Stroj však musí být schopen jednoznačně rozpoznat cílové zařízení, které má pakety doručit. Za tímto účelem se spoléhá na specifický hardwarový identifikátor, který přímo používá jeho síťový Interface: MAC Address (_Media Access Control_).


**Poznámka**: To nemá nic společného s "fyzickým Address" v paměťové architektuře. Ve výpočetní technice se fyzickou pamětí Address rozumí konkrétní místo na paměťové sběrnici, na rozdíl od virtuální paměti Address spravované operačním systémem. Naproti tomu MAC Address se týká výhradně síťového hardwaru.


MAC Address je trvale a jedinečně přiřazen výrobcem, u kterého je zařízení vyrobeno. MAC Address jednoznačně identifikuje síťovou kartu, ať už se jedná o počítač, chytrý telefon, tiskárnu nebo jiné připojené zařízení. Na rozdíl od IP Address, která se může dynamicky měnit (prostřednictvím serveru DHCP nebo ruční konfigurace), zůstává MAC Address obvykle stejná po celou dobu životnosti zařízení, pokud není záměrně změněna.


Každá síť Interface, kabelová nebo bezdrátová, má vlastní MAC Address. Tento Address se používá v rámci datového spoje Layer (Layer 2 modelu OSI) k vložení a správě hardwarového Address v každém vyměněném síťovém rámci. Někdy se označuje jako _Ethernetová adresa_ nebo _UAA_ (_Univerzálně spravovaná adresa_). Standardně má délku 48 bitů neboli 6 bajtů a zapisuje se v šestnáctkové notaci, obvykle ve formě bajtů oddělených znaky `:` nebo `-`.


Například: `5A:BC:17:A2:AF:15`


V této struktuře identifikují první tři bajty výrobce síťové karty: jedná se o **OUI** (*Organizačně jedinečný identifikátor*). Tyto prefixy, přidělené organizací IEEE, se používají také v jiných schématech hardwarového adresování, jako je Bluetooth a LLDP, aby byla zaručena celosvětová jedinečnost.


### Změna adresy MAC Address (MAC Spoofing)


Teoreticky je MAC Address navržen tak, aby zůstal pevný, ale existují způsoby, jak jej upravit, zejména pro splnění konkrétních potřeb nebo obejití určitých omezení. Tato operace, často označovaná jako _spoofing MAC_, zahrnuje nahrazení původní hardwarové hodnoty Address jinou hodnotou definovanou na softwarové úrovni. Některé operační systémy tuto modifikaci usnadňují, zejména pokud ovladač přímo nepoužívá skutečný ethernetový kód Address.


Důvody pro takovou změnu jsou různé. Může jít o potřebu dané aplikace vyžadovat pro správnou funkci konkrétní Ethernet Address nebo o vyřešení konfliktu stejných adres mezi dvěma zařízeními sdílejícími stejnou místní síť.


Změna MAC Address může být motivována také ochranou soukromí: skrytím jedinečného identifikátoru vyrytého na kartě uživatelé snižují možnost sledování svého zařízení sítěmi nebo sledovacími službami. Tato praxe však není bez následků. Změna MAC Address může narušit některá filtrační zařízení nebo vyžadovat překonfigurování firewallů, aby nový hardware autorizovaly.


Některé sítě, zejména Wi-Fi, používají filtrování MAC Address, které povoluje pouze zařízení se schválenými adresami. To sice zvyšuje základní úroveň kontroly, ale samo o sobě není bezpečné. Útočník může zachytit platnou MAC Address, která již byla v síti autorizována, a naklonovat ji, aby omezení obešel. Z tohoto důvodu by filtrování MAC mělo být vždy kombinováno se silnějšími bezpečnostními opatřeními.


### Korespondence MAC/IP


Aby místní síť fungovala efektivně, musí existovat jasné mapování mezi fyzickými adresami (adresy MAC) a logickými adresami (adresy IP). Bez tohoto spojení by počítač mohl znát IP Address cíle, ale nevěděl by, jak mu fyzicky poslat data v místní síti.

O toto mapování se automaticky stará protokol ARP (_Address Resolution Protocol_).


Pokud chce uživatel zjistit MAC Address odpovídající určitému IP Address, může v praxi použít nástroj `arp`. Tento nástroj kontroluje místní tabulku ARP počítače a zobrazuje známé shody mezi adresami IP a adresami MAC v místní síti. Tímto způsobem je možné rychle ověřit efektivní spojení mezi logickou a fyzickou vrstvou.


Praktický příklad: Chcete-li zjistit, která síťová karta odpovídá IP adrese Address `192.168.1.5`, použijte následující příkaz:


```bash
arp –a 192.168.1.5
```


Na výstupu se zobrazí přidružený fyzický kód Address (MAC), povaha vstupu (statický nebo dynamický) a příslušný kód Interface.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Je důležité si uvědomit, že MAC Address a IP Address jsou dva zcela odlišné identifikátory, které se však úzce doplňují. MAC Address je výrobcem jedinečně vyryt do každého síťového Interface a slouží k fyzické identifikaci zařízení v místní síti. Naproti tomu IP Address je logický identifikátor Address, který se přiděluje buď dynamicky, nebo staticky a umožňuje zařízení připojit se k síti IP a paketům Exchange mimo jeho místní síť.



- Vizuální příklad MAC Address:


![Image](assets/fr/032.webp)




- Vizuální příklad IP Address:


![Image](assets/fr/027.webp)



Ve firemním prostředí nemohou tyto dvě úrovně adresování fungovat odděleně. Například když server DHCP automaticky přiděluje IP Address, jako výchozí bod se použije MAC Address zařízení. Počítač odešle požadavek na vysílání DHCP obsahující jeho MAC Address, aby server mohl přiřadit dostupné IP Address správnému zařízení. Bez této identifikace hardwaru by server DHCP nevěděl, kterému zařízení má doručit kód Address.


Protokol ARP je proto zásadní: zajišťuje spojení mezi adresami IP a fyzickými adresami a umožňuje počítačům převádět logické místo určení na skutečné fyzické místo určení. Když počítač potřebuje odeslat paket stroji ve stejné síti, nejprve nahlédne do své tabulky ARP, aby zjistil, zda je již známa adresa MAC příjemce Address. Pokud ne, vyšle požadavek ARP všem hostitelům v místní síti. Stroj, který v tomto požadavku rozpozná cílovou adresu IP Address, odpoví zadáním své adresy MAC Address. Odesílatel pak zapíše tento pár IP/MAC do své mezipaměti ARP, aby nemusel operaci opakovat při každém odeslání požadavku.


Tato tabulka ARP funguje jako mini mapovací adresář, který je dynamicky aktualizován podobným způsobem, jakým systém DNS přiřazuje doménová jména k IP adresám. Bez ARP by nebylo možné použít místní Exchange, protože datový spoj Layer potřebuje znát MAC Address, aby mohl správně zapouzdřit ethernetové rámce.


Naopak protokol RARP (_Reverse Address Resolution Protocol_) byl navržen pro opačnou situaci: umožňuje počítači, který zná pouze svou MAC adresu Address, zjistit svou IP adresu Address. To byl běžný případ starších pracovních stanic bez místního disku Hard, které musely spouštět systém přes síť a vyžádat si IP Address. Protokol RARP byl nakonec nahrazen protokolem **BOOTP** a poté protokolem **DHCP**, které jsou flexibilnější a automatizovanější.


Tyto asociační protokoly hrají důležitou roli při směrování. Směrovač je v podstatě stroj s několika síťovými rozhraními, který spojuje různé segmenty. Když směrovač přijme rámec, zpracuje jej, aby z něj získal datagram IP, a prozkoumá záhlaví IP, aby určil cíl. Pokud je cíl v přímo připojené síti, je datagram po aktualizaci záhlaví doručen přímo. Pokud cílová stanice patří do jiné sítě, směrovač vyhledá ve své směrovací tabulce nejlepší cestu neboli _next hop_ k cílové stanici.


Tím se trasa rozdělí na kratší, lépe zvládnutelné úseky. Každý zprostředkující směrovač zná pouze další krok, nikoli nutně konečný cíl.


**Připomínáme:** Přímé doručení nastane, když jsou odesílatel a příjemce ve stejné fyzické síti. V opačném případě je doručení nepřímé a prochází přes jeden nebo více směrovačů.


Směrovací tabulka, která je spravována buď ručně (statické směrování), nebo dynamicky (dynamické směrování), obsahuje informace potřebné k rozhodnutí, kterou trasu zvolit. V malých sítích stačí statická konfigurace. Ve větších infrastrukturách je dynamické směrování nezbytné k automatické úpravě tras při změně topologie nebo výpadku linky.


Směrovací tabulka slouží jako mapovací tabulka mezi cílovými IP adresami a dalšími branami. Obvykle jsou v ní uloženy identifikátory sítě (_network ID_), nikoli každý jednotlivý hostitel Address, což značně snižuje její velikost.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Pomocí těchto záznamů může směrovač rychle určit, přes který Interface a do kterého uzlu má být každý datagram odeslán. V kombinaci s ARP pro překlad odpovídajících adres MAC je tak zajištěn efektivní a spolehlivý přenos dat v síti.


Mezi dynamické směrovací protokoly patří standardy jako RIP (_Routing Information Protocol_), založený na algoritmu vzdálenosti, a OSPF (_Open Shortest Path First_), který počítá nejkratší cesty ve složité topologii. Tyto protokoly neustále Exchange aktualizují, aby optimalizovaly trasy, snížily náklady na přenos a zlepšily odolnost proti výpadkům nebo přetížení.



## NAT: Překlad Address


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definice


Network Address Translation_ (NAT) je technika vyvinutá pro Address postupné vyčerpávání dostupných adres IPv4. NAT byl navržen jako dočasné řešení před širokým přijetím protokolu IPv6 a umožnil společnostem a jednotlivcům nadále připojovat velké množství počítačů a přitom používat pouze omezenou sadu veřejných IP adres.


**Důležitá připomínka:** přechod z IPv4 na IPv6 teoreticky řeší problém vyčerpání adres rozšířením prostoru Address z 32 bitů na 128 bitů, což poskytuje téměř neomezený počet adres (2^128). V praxi je však přechod stále neúplný a NAT se dnes stále hojně používá.


Princip NAT je jednoduchý, ale velmi účinný: namísto přidělení jedinečné veřejné IP adresy Address každému zařízení ve vnitřní síti se pro všechna soukromá zařízení používá jediná směrovatelná adresa Address (nebo malý fond adres). Brána NAT, často integrovaná do směrovače nebo brány firewall, pak dynamicky překládá interní adresu IP Address spolu s informacemi potřebnými pro správné směrování provozu do vnějšího světa a zajišťuje, aby se odpovědi vracely původnímu odesílateli.


Tento přístup má okamžitou výhodu: zcela skrývá vnitřní síťovou architekturu. Vnějšímu pozorovateli se zdá, že všechny požadavky z pracovních stanic, serverů nebo tiskáren pocházejí ze stejné veřejné identity. Soukromé adresy, obvykle převzaté z vyhrazených rozsahů (např. 192.168.x.x nebo 10.x.x.x), zůstávají z internetu neviditelné.


Kromě řešení nedostatku IPv4 posiluje NAT také bezpečnost tím, že vytváří první logickou bariéru mezi interní a veřejnou sítí. Nevyžádaná příchozí komunikace je přirozeně blokována, protože pouze spojení iniciovaná zevnitř sítě využívají potřebného překladu k získání odpovědi.



![Image](assets/fr/035.webp)



### Typy překladů


NAT lze implementovat různými způsoby, které vyhovují konkrétním potřebám. Dva hlavní způsoby fungování jsou statický překlad a dynamický překlad.


**Statický překlad** vytváří pevné mapování mezi privátní IP adresou Address a veřejnou IP adresou Address. Každý interní stroj je trvale spojen se svým vyhrazeným veřejným Address. Například interní zařízení nakonfigurované jako 192.168.20.1 může být spojeno se směrovatelným Address 157.54.130.1. Když odchozí paket opouští místní síť, směrovač nahradí zdrojový Address paketu veřejným Address a pro příchozí provoz provede opačnou operaci. Tento obousměrný překlad je pro uživatele transparentní.


**Upozornění:** Tato metoda sice izoluje vnitřní síť, ale neřeší nedostatek veřejných IP adres, protože stále potřebujete tolik veřejných adres, kolik je počítačů, které chcete vystavit. Statický překlad se proto používá hlavně v případě, že některé vnitřní zdroje musí zůstat dosažitelné zvenčí (webový server, poštovní server...).


**Dynamický překlad** naopak využívá fond veřejných IP adres. Když interní hostitel zahájí připojení, směrovač dočasně přiřadí jednu z těchto veřejných adres soukromé adrese Address hostitele po dobu trvání relace. Spojení je 1:1, ale dočasné:jakmile spojení skončí, veřejná adresa Address se uvolní pro jiné zařízení. Dynamický NAT tedy snižuje počet potřebných veřejných adres, pokud nejsou všechna zařízení současně online, ale stále vyžaduje blok externích adres alespoň tak velký, jako je maximální počet současných připojení.


**Port translation** (PAT), známý také jako *NAT overload* nebo *IP masquerading*, jde ještě o krok dále: všechna soukromá zařízení sdílejí jedinou veřejnou IP adresu Address (nebo její velmi malý počet). Pro rozlišení relací brána upravuje nejen zdrojovou adresu Address, ale také zdrojový port. Uchovává tabulku, která spojuje každou dvojici *(soukromý Address, soukromý port)* s jedinečnou dvojicí *(veřejný Address, veřejný port)*. Tato forma NAT se používá téměř ve všech domácích směrovačích a umožňuje desítkám zařízení (počítačům, smartphonům, připojeným objektům atd.) sdílet stejnou veřejnou IP adresu Address při zachování plynulé komunikace.


NAT proto prodlužuje životnost protokolu IPv4 a zároveň přidává cennou segmentaci a zabezpečení Layer. S rostoucím rozšířením protokolu IPv6 a jeho rozsáhlým prostorem Address se však úloha NAT pravděpodobně sníží, i když pro účely kompatibility a kontroly se bude v některých prostředích stále používat k segmentaci a filtrování provozu.


### Implementace NAT


Aby bylo zajištěno správné fungování překladu Address, musí směrovač nebo brána NAT uchovávat přesné záznamy o mapováních vytvořených mezi každým soukromým Address ve vnitřní síti a veřejným Address, který používá ke komunikaci s vnějším světem. Tyto informace jsou uloženy v takzvané "překladové tabulce NAT", která hraje ústřední roli při řízení síťového provozu.


Každá položka v této tabulce spojuje alespoň jednu dvojici: interní IP adresu Address odesílajícího počítače a externí IP adresu Address, která bude vystavena v Internetu. Když je paket z privátní sítě odeslán do veřejného cíle, směrovač NAT zachytí rámec, analyzuje hlavičky IP a TCP/UDP a poté nahradí privátní zdroj Address veřejným Address brány. Na zpáteční cestě stejná brána zachytí příchozí paket, zkontroluje mapovací tabulku a provede zpětnou operaci, aby přesměrovala tok na původní interní IP Address.


Tento princip dynamického překladu se opírá o přesnou správu tabulek: každá položka zůstává platná, dokud existuje aktivní provoz, který ji ospravedlňuje. Po konfigurovatelné době nečinnosti je záznam vymazán a může být znovu použit pro nová spojení.


_Příklad zjednodušené překladové tabulky NAT:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

Pokud v tomto příkladu neprošel u druhé položky žádný paket za více než hodinu (3600 sekund), je označena jako opakovaně použitelná. Naopak doba trvání nula znamená aktivní komunikaci s uzamčeným mapováním.


Zatímco pro většinu běžných použití (prohlížení webu, e-mail, přenos souborů atd.) funguje NAT transparentně, pro některé síťové aplikace může představovat další problémy. Některé technologie se spoléhají na explicitní výměnu IP adres nebo portů v rámci užitečného zatížení paketu. Po průchodu bránou NAT se tyto informace stávají nekonzistentními.


Mezi typické příklady omezení patří:


- Protokoly peer-to-peer (P2P), které vyžadují přímé spojení mezi zařízeními, jsou ztíženy bariérou NAT, protože všechny interní počítače sdílejí stejnou vnější IP adresu Address a nelze se k nim dostat přímo bez specifické konfigurace (např. *předávání portů* nebo UPnP);
- Protokol IPSec, který se používá k zabezpečení síťové komunikace, šifruje hlavičky paketů. Protože NAT musí tyto hlavičky modifikovat, aby nahradil IP adresy, šifrování to znemožňuje bez adaptačních mechanismů, jako je NAT-T (*NAT Traversal*);
- Protokol X Window, který umožňuje vzdálené zobrazování grafických aplikací v systému Unix/Linux, funguje tak, že server X aktivně odesílá připojení TCP klientům. Toto obrácení obvyklého směru spojení lze blokovat pomocí NAT.


Obecně platí, že ovlivněn bude jakýkoli protokol, který v užitečném zatížení paketu explicitně obsahuje interní IP adresu Address, protože tato adresa Address se po překladu již nebude shodovat se skutečnou, v internetu viditelnou adresou Address.


**Důležitá poznámka:** Pro řešení těchto problémů nabízejí některé směrovače NAT funkci _Deep Packet Inspection_ (DPI) nebo _Protocol Helpers_ , které kontrolují obsah paketů a identifikují a dynamicky nahrazují adresy nebo čísla portů v aplikačních datech. To vyžaduje důkladnou znalost formátu protokolu a může vytvářet bezpečnostní zranitelnosti nebo zvyšovat spotřebu prostředků.


**Upozornění:** Přestože NAT pomáhá skrýt vnitřní síť a řídit příchozí přenosy, nenahrazuje vyhrazenou bránu firewall. Samotný překlad není úplnou bezpečnostní bariérou: vždy musí být doplněn jasnými pravidly filtrování, která blokují nevyžádaný nebo nežádoucí provoz.


_Pro ilustraci, jak to funguje v praxi, uveďme následující příklad:_



![Image](assets/fr/037.webp)



V tomto scénáři může interní pracovní stanice přistupovat k internímu webovému serveru jednoduše voláním adresy URL `http://192.168.1.20:80`. Zadání portu je zde nepovinné, protože `80` je standardní port HTTP.Naopak, pokud je požadavek iniciován zvenčí, uživatel zadá veřejný port Address `http://85.152.44.14:80`. Směrovač NAT přijme požadavek, vyhledá svou mapovací tabulku a automaticky přeloží veřejný port Address na soukromý a přesměruje spojení na `http://192.168.1.20:80`.


Stejný princip platí pro jakýkoli jiný server oprávněný přijímat připojení k internetu, například pro server Extranet (modrý okruh na obrázku).


**Praktická poznámka:** ve virtualizovaných prostředích se běžně používají síťová rozhraní s názvem _virbrX_ (pro _Virtual Bridge X_). Tyto virtuální mosty, poskytované zejména knihovnou libvirt nebo hypervizorem Xen, připojují virtuální vnitřní síť hostovaných počítačů k fyzické síti a zároveň používají NAT. Obvykle se konfigurují pomocí skriptů v adresáři `/etc/sysconfig/network-scripts/`, jak je uvedeno níže pro `virbr0`:


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


Po zavedení virtuálního mostu je třeba povolit směrování IP a nakonfigurovat překlad portů pomocí `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Při této konfiguraci je odchozí provoz směrován a je použit překlad NAT, což umožňuje virtuálním počítačům komunikovat s okolním světem, aniž by byly přímo odhaleny jejich vnitřní IP adresy.


V příští kapitole se podrobně podíváme na konfiguraci protokolu IP Address pod systémem Linux, přičemž se budeme zabývat jednoduchými i pokročilými metodami vhodnými pro různé kontexty správy.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Jak nakonfigurovat síť pomocí `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Standardní konfigurace


Po teoretických základech síťování a pochopení toho, jak IP adresy, masky, směrování a překlad fungují společně, je čas přejít k praktické konfiguraci. V systému GNU/Linux se nyní nastavení sítě provádí pomocí příkazu **`ip`** (balíček _iproute2_), který nahrazuje starší příkaz `ifconfig`.


`ip` umožňuje přiřadit nebo změnit IP adresu Address, změnit masku, spustit nebo zastavit Interface nebo kdykoli zkontrolovat jeho stav.


**TIPS:** pro zobrazení všech rozhraní (aktivních i neaktivních): `ip addr show`


Příklad: přiřazení statického Address a aktivace Interface


Přidejte Address `192.168.1.2/24` ke Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Aktivujte Interface:


```shell
ip link set dev eth0 up
```


Deaktivujte stejný přístroj Interface:


```shell
ip link set dev eth0 down
```


Zobrazení stavu konkrétního zařízení Interface:


```shell
ip addr show dev eth2
```


**Praktický tip:** s `ip` již přidání dalšího Address ke Interface nevyžaduje příponu `:1`. Stačí přidat další řádek `ip addr add ...`:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Aktivační skripty: ifup / ifdown


Nástroje `ifup` a `ifdown` načítají statické konfigurační soubory z `/etc/sysconfig/network-scripts/` (v RHEL, CentOS, Rocky Linux, AlmaLinux...) nebo `/etc/network/interfaces` (v Debian/Ubuntu) a čistě tak zapínají nebo vypínají rozhraní.


```shell
ifup eth1
ifdown eth2
```


Konfigurační soubory (podobné systému RHEL):


- /etc/sysconfig/network**: globální nastavení (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: nastavení specifické pro každý Interface.


Statický příklad (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Příklad DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Tato modulární struktura je stále platná a lze ji snadno automatizovat v současných systémech.


### Pokročilá konfigurace: lepení


V profesionálních prostředích je cílem zajistit kontinuitu služeb a/nebo agregovat šířku pásma. *Tyto potřeby splňují mechanismy spojování* (nebo *teaming* s _teamd_): několik fyzických rozhraní funguje jako jedno logické rozhraní Interface, často nazývané `bond0` nebo `team0`.



![Image](assets/fr/039.webp)



Předpoklady:


- Nahrajte modul `bonding` (nebo použijte `teamd`) ;
- Mějte k dispozici alespoň dvě fyzická rozhraní.


#### Různé běžné metody lepení:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Nastavení pomocí `ip link



- Zakázat fyzická rozhraní:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Vytvořte lepený Interface:


```shell
ip link add bond0 type bond mode balance-alb
```



- Konfigurace možností po vytvoření


```shell
ip link set bond0 type bond miimon 100
```



- Přiřazení adres MAC a IP:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Připojení podřízených rozhraní:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Vraťte vše zpět nahoru:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Tip:** pro odpojení podřízeného zařízení bez zrušení vazby: `ip link set eth1 nomaster`


#### Stálá konfigurace (podobná RHEL)


Vytvořte tři soubory v adresáři `/etc/sysconfig/network-scripts`:


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


Pak:


```shell
systemctl restart network
```


#### Další IP Address (moderní přezdívka)


Pomocí `ip` můžete jednoduše přidat druhý Address ke stejnému zařízení:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Chcete-li, aby tento alias zůstal zachován i po restartu, přidejte do `ifcfg-eth0` druhý blok `IPADDR2=...` / `PREFIX2=...` nebo vytvořte nové připojení *NetworkManager* pomocí `nmcli`.


Díky příkazu `ip` a souvisejícím příkazům (`ip link`, `ip addr`, `ip route`) je konfigurace sítě konzistentnější, skriptovatelnější a přehlednější. Spojení je klíčovou součástí architektur s vysokou dostupností a přiřazení více adres jedinému zařízení Interface se výrazně zjednodušilo.


V příští kapitole se podíváme na specifika a implementaci adresování IPv6.


# Adresování IPv6


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Standardy a definice


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Nyní přecházíme na novou generaci adresování IP: protokol IPv6, původně známý jako IPng (_IP Next Generation_). Tento protokol, který byl navržen k překonání strukturálních omezení protokolu IPv4, zavádí značně rozšířenou architekturu adresování a také řadu technických optimalizací.


Motivace pro přijetí protokolu IPv6 jsou různé a Address jsou pro vývoj internetu velmi důležité. Zaprvé, úlohou protokolu IPv6 je podpořit exponenciální růst počtu připojených zařízení (což je cíl nedosažitelný s omezeným prostorem protokolu IPv4 Address). Za druhé je cílem protokolu zmenšit velikost směrovacích tabulek, čímž se zefektivní výměna a dlouhodobě se sníží zatížení směrovačů.


IPv6 se také snaží zjednodušit některé aspekty zpracování paketů, zlepšit tok datagramů a optimalizovat přenosové rychlosti mezi sítěmi. Z hlediska bezpečnosti jsou hlavičky AH/ESP protokolu *IPsec* zahrnuty do základní specifikace a všechny uzly IPv6 je musí podporovat (RFC 6434). Jejich použití však zůstává volitelné: je na správci, zda je povolí v závislosti na kontextu.


Mezi další cíle patří přesnější zpracování typů služeb, zejména zajištění lepší kvality pro aplikace v reálném čase (VoIP, videokonference atd.). IPv6 je také navržen tak, aby umožňoval pružnější správu mobility: zařízení může měnit přístupové body, aniž by se změnil jeho Address způsobem, který je viditelný pro jeho kolegy.


Protokol IPv6 byl navržen tak, aby mohl koexistovat se staršími protokoly. Ačkoli není přímo binárně kompatibilní s protokolem IPv4, zůstává plně interoperabilní s protokoly vyššího řádu, jako jsou TCP, UDP, ICMPv6 a DNS, a také se směrovacími protokoly, jako jsou OSPF a BGP, s výhradou určitých úprav. Pro správu vícesměrového vysílání používá IPv6 protokol MLD (*Multicast Listener Discovery*), který je funkčním ekvivalentem IGMP v prostředí IPv4.


### Pravidla zápisu


Jednou z nejvýznamnějších změn v protokolu IPv6 je formát samotného protokolu IP Address. Kvůli chronickému nedostatku adres IPv4 byla délka Address zvýšena z 32 bitů na 128 bitů, tedy na 16 bajtů. Teoreticky tak vzniká možný prostor Address:


$$3.4 \krát 10^{38}$$


Tím je zajištěna prakticky neomezená kapacita pro všechna současná i budoucí zařízení.


Adresy IPv6 se zapisují zcela odlišně od známého tečkovaného desítkového zápisu. IPv6 Address se skládá z osmi 16bitových skupin zapsaných v šestnáctkové soustavě a oddělených dvojtečkami `:`.


Například:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Pro zjednodušení zápisu lze v každé skupině vynechat počáteční nuly. Výše uvedený příklad pak bude vypadat takto:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Kromě toho lze jedinou souvislou sekvenci nulových skupin nahradit znakem::, čímž se dále zkrátí kód Address:


```
1987:c02:0:84c2::cf2a:9077
```


**Upozornění:** toto pravidlo je přísné: pouze jedna sekvence po sobě jdoucích nul může být nahrazena znakem `::`. Pokud kód Address obsahuje více sekvencí nul, je kondenzována pouze nejdelší z nich. Tím je zajištěna jedinečnost i čitelnost.


**Důležitý detail:** znak `:` používaný k oddělení hexadecimálních bloků může způsobit nejednoznačnost v adresách URL, protože `:` se používá také k označení portu služby. Aby nedošlo k záměně, musí být adresy IPv6 v URL uzavřeny v hranatých závorkách `[ ]`.


Příklad přístupu HTTP na konkrétní port pro Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Při reprezentaci IPv4 Address v kontextu IPv6 můžete použít smíšený zápis v tečkovaném desítkovém tvaru, kterému předchází`::`:


```
::192.168.1.5
```


Tato kompatibilita usnadňuje přechod mezi oběma protokoly tím, že umožňuje zahrnout bloky IPv4 do prostoru IPv6 Address.


**Poznámka:** Za účelem standardizace zápisu adres definuje RFC 5952 kanonický formát s pravidly pro zkracování, aby se zabránilo vícenásobné reprezentaci stejného čísla Address. Dodržování těchto doporučení pomáhá omezit nesprávnou interpretaci a zajišťuje konzistentní síťové konfigurace.


### Typy IPv6 Address


IPv6 se od svého předchůdce liší širokou škálou kategorií Address, z nichž každá je určena pro specifické použití a zároveň umožňuje flexibilní směrování a správu sítě. Stejně jako u IPv4 mohou být adresy globální, lokální, rezervované nebo specifické pro určité přechodové mechanismy.


Nespecifikovaný IPv6 Address je reprezentován znakem `::` nebo explicitněji `::0.0.0.0`. Tento speciální tvar se používá při získávání Address nebo jako výchozí hodnota pro označení neexistence Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *V privátní síti LAN se pro přidělování interních adres, které nejsou směrovatelné v Internetu, upřednostňuje prefix `fd00::/8`


#### Vyhrazené adresy


Některé rozsahy protokolu IPv6 jsou výslovně vyhrazeny a nesmí se používat jako globální adresy. Mají specifické technické účely:


- `::/128`**: nespecifikovaný Address, nikdy trvale nepřidělený zařízení, ale používaný jako zdrojový Address počítačem čekajícím na konfiguraci.
- `::1/128`**: _loopback_ Address, přímý ekvivalent `127.0.0.1` v IPv4, který umožňuje počítači připojit se k Address.
- `64:ff9b::/96`**: Vyhrazeno pro překladače protokolů umožňující propojení IPv4/IPv6, jak je definováno v RFC 6052.
- `::ffff:0:0/96`**: blok kompatibility pro reprezentaci IPv4 Address ve specifické struktuře IPv6, často používaný interně aplikacemi.


Tyto bloky zaručují interoperabilitu a usnadňují přechod mezi oběma verzemi protokolu.


#### Globální jednosměrové adresy


Většinu veřejně směrovatelného prostoru IPv6 tvoří globální jednosměrové adresy, které představují přibližně 1/8 prostoru Address. Od roku 1999 přiděluje IANA tyto bloky, například prefix `2001::/16`, v blocích CIDR (od `/23` do `/12`) regionálním registrům, které je pak přerozdělují poskytovatelům a organizacím.


Některé rozsahy mají zvláštní dokumentované použití:


- `2001:2::/48`**: Vyhrazeno pro testování výkonu a interoperability (RFC 5180).
- `2001:db8::/32`**: Vyhrazeno pro dokumentaci a příklady (RFC 3849).
- `2002::/16`**: Používá se pro mechanismus 6to4, který umožňuje přenos IPv6 přes infrastrukturu IPv4 (užitečné ve fázi přechodu mezi oběma protokoly).


**Poznámka:** velká část globálních adres zůstává nevyužita a slouží jako rezerva pro budoucí růst internetu.


#### Jedinečné místní adresy (ULA)


Jedinečné místní adresy (`fc00::/7`) jsou ekvivalentem privátních adres IPv4 (RFC1918). Umožňují vytvářet izolované vnitřní sítě bez rizika konfliktů s veřejným adresováním. V praxi je efektivní prefix `fd00::/8`, přičemž osmý bit je nastaven na 1, aby bylo označeno místní použití. Každý blok ULA obsahuje 40bitový pseudonáhodný identifikátor, který minimalizuje kolize Address při propojování oddělených privátních sítí.


#### Link-local adresy


Link-local adresy (`fe80::/64`) se používají výhradně pro komunikaci v rámci stejného segmentu Layer 2 (stejné VLAN nebo přepínače). Nikdy nejsou směrovány mimo lokální linku. Každý síťový Interface automaticky generuje linkový lokální Address, často odvozený od jeho MAC Address pomocí schématu EUI-64.


**Zvláštní vlastnost**: stejný počítač může používat stejný linkový lokální server Address na více rozhraních, ale při komunikaci musí být zadán server Interface, aby se předešlo nejednoznačnosti.


#### Vícesměrové adresy


V protokolu IPv6 bylo vysílání nahrazeno vícesměrovým vysíláním, což je efektivnější způsob doručování paketů definované skupině příjemců. Rozsah vícesměrového vysílání má předponu `ff00::/8`. Patří sem adresy jako `ff02::1`, které jsou určeny všem uzlům na místní lince. Ačkoli je tento způsob Address pohodlný, pro aplikace se již nedoporučuje, protože může generate nekontrolovaně vysílat.


Běžným využitím vícesměrového vysílání je protokol _Neighbor Discovery Protocol_ (NDP), který v protokolu IPv6 nahrazuje protokol ARP. NDP používá specifické adresy vícesměrového vysílání, například `ff02::1:ff00:0/104`, k automatickému vyhledávání dalších hostitelů připojených ke stejné lince.


Kombinací těchto typů Address poskytuje IPv6 kompletní sadu možností, které splňují potřeby globálního směrování, místní komunikace, migrace IPv4/IPv6 a automatické konfigurace zařízení a zároveň zvyšují efektivitu přenosu.


### Rozsah působnosti Address


Rozsah IPv6 Address přesně definuje doménu, ve které je platný a jedinečný. Pochopení tohoto konceptu je klíčem ke zvládnutí směrování paketů a logické organizace sítě IPv6. Adresy IPv6 se obecně dělí do tří hlavních kategorií podle rozsahu a použití: unicast, anycast a multicast.


*nejběžnější jsou adresy *Unicast**, které zahrnují několik různých podtypů.

Patří mezi ně _loopback_ (`::1`) Address, jehož rozsah je omezen na hostitele, který jej používá, a který se používá k internímu testování síťového zásobníku bez odesílání provozu po fyzické síti.

Dále existují adresy linkové (_link-local_), jejichž rozsah je omezen na jeden segment sítě: používají se pro přímou komunikaci mezi zařízeními na stejné fyzické nebo logické lince (např. jeden přepínač nebo VLAN).

A konečně, jedinečné místní adresy (_ULA_, zkratka _Unique Local Addresses_) jsou interní adresy privátní sítě. Mohou být směrovány mezi více soukromými segmenty, ale nikdy nejsou viditelné v Internetu.


Koncepčně jsou adresy IPv6 často reprezentovány jako binární struktura, kde první polovina (prvních 64 bitů) identifikuje předponu sítě a druhá polovina (rovněž 64 bitů) jednoznačně identifikuje zařízení Interface v dané síti. Toto rozdělení usnadňuje automatickou konfiguraci Address pomocí mechanismů, jako je SLAAC (_Stateless Address Autoconfiguration_), které umožňují strojům automaticky generate stabilní Address na základě MAC Address nebo pseudonáhodného identifikátoru.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

Architektura IPv6 se řídí hierarchickým modelem globálního směrování dnešního internetu. Rozdělení prefixů umožňuje regionálním registrům a provozovatelům sítí řídit přidělování Address decentralizovaným způsobem a zároveň zajišťuje globální jedinečnost. V tomto rámci může mít tentýž hostitel současně globální jednosměrový Address pro internetovou komunikaci a linkový lokální Address pro místní interakce, např. s nejbližším okolím nebo pro zprávy o vyhledávání směrovačů.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Anycast adresy** představují přechodný koncept, který vychází z modelu unicast, ale v určitých případech se může chovat jako multicast. Anycast Address je v podstatě unicast Address přiřazený několika rozhraním rozmístěným v různých uzlech sítě. Když je paket odeslán na anycast Address, cílem protokolu IPv6 je doručit jej jednomu z hostitelů sdílejících tento Address, obvykle tomu, který je z hlediska topologie směrování nejblíže. Tento přístup optimalizuje rychlost zpracování dotazů a zvyšuje odolnost distribuovaných služeb. Klasickým příkladem jsou kořenové servery DNS, kde anycastové adresování automaticky směřuje dotazy na nejbližší místo výskytu.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

V protokolu IPv6 nahrazují **multicastové adresy** mechanismus broadcast, který byl považován za příliš nákladný a nevhodný pro sítě globálního rozsahu. Vícesměrové vysílání Address identifikuje skupinu rozhraní, obvykle na více hostitelských počítačích, která si přejí přijímat stejné pakety současně.

Každé vícesměrové vysílání Address obsahuje speciální 4bitové pole _scope_, které definuje geografickou nebo logickou hranici vysílání:


- Rozsah `1` znamená, že paket je určen pouze pro místní zařízení.
- Rozsah `2` omezuje paket na místní linku: mohou jej přijímat všechna zařízení ve stejném fyzickém nebo virtuálním segmentu.
- Rozsah `5` rozšiřuje dosah na lokalitu, obvykle na celou podnikovou síť.
- Rozsah `8` rozšiřuje dosah na organizaci a umožňuje doručování ve všech podsítích stejného subjektu.
- Rozsah `e` (14 v šestnáctkové soustavě) označuje globální dosah, takže skupina vícesměrového vysílání je přístupná z kteréhokoli místa na internetu, pokud to směrovací infrastruktura podporuje.


Struktura vícesměrového vysílání IPv6 Address zahrnuje:


- pole _Flag_ (4 bity) určuje, zda je skupina trvalá nebo dočasná,
- pole _Scope_ (4 bity) definuje rozsah,
- identifikační pole (112 bitů) identifikující číslo skupiny vícesměrového vysílání.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Známým příkladem vícesměrového vysílání IPv6 v praxi je protokol _Neighbor Discovery Protocol_ (NDP). Namísto použití protokolu ARP jako v protokolu IPv4 se protokol NDP spoléhá na vícesměrové adresy, jako je `ff02::1:ff00:0/104`, které vysílají požadavky na vyhledání sousedů a zaměřují se pouze na příslušné hostitele na stejné lince.


Díky přesnému vymezení rozsahů Address IPv6 strukturuje způsob odesílání, přijímání a směrování datových toků. Díky této granularitě je protokol flexibilnější a efektivnější pro správu místní i globální komunikace a zároveň se vyhýbá nevýhodám obecného vysílání.


## Address Assignment v místní síti


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


V této kapitole se budeme zabývat jedním z nejpraktičtějších aspektů nasazení protokolu IPv6: přidělováním IP adres hostitelům v místní síti. Architektura IPv6 byla navržena s ohledem na flexibilitu, takže umožňuje každému zařízení generate automaticky přidělovat vlastní Address a zároveň v případě potřeby umožňuje plně manuální konfiguraci.


Místní síť IPv6 systematicky rozděluje Address na dvě části:


- prvních 64 bitů představuje prefix podsítě, který obvykle poskytuje směrovač nebo autorita Address;
- zbývajících 64 bitů používá hostitel k jednoznačné identifikaci v daném segmentu.

Tento model výrazně zjednodušuje agregaci tras a správu bloků Address.


K přidělování adres zařízením se používají dva hlavní přístupy:


- Ruční konfigurace, při níž správce zadá přesné číslo Interface pro každý Address;
- Automatická konfigurace, kdy zařízení generate nebo získávají své vlastní adresy dynamicky.


Při ruční konfiguraci správce přiřadí každému Interface kompletní IPv6 Address. Některé hodnoty zůstávají vyhrazeny:


- `::/128`: nespecifikovaný Address, nikdy trvale nepřiřazen ;
- `::1/128`: zpětná smyčka Address (_loopback_), ekvivalent IPv4: `127.0.0.1`.


Na rozdíl od protokolu IPv4 neexistuje koncept _broadcast_; kombinace "všechny nuly" nebo "všechny jedničky" v hostitelské části nemají žádný zvláštní význam.

Ruční konfigurace je stále užitečná v kontrolovaných prostředích, ale v měřítku se obtížně udržuje.


Pro automatickou konfiguraci existuje několik metod:


- Protokol **NDP** (_Neighbor Discovery Protocol_), specifikovaný v dokumentu RFC4862, umožňuje *bezstavovou* automatickou konfiguraci. V tomto režimu hostitel obdrží síťový prefix od místního směrovače a sám doplní Address identifikátorem založeným na jeho MAC Address. Tato metoda je jednoduchá na nasazení a nevyžaduje žádný centrální server.
- Implementace, jako jsou ty v systému Windows, mohou generate hostitelskou část pseudonáhodně, aby zlepšily soukromí tím, že se vyhnou přímému odhalení MAC Address. Odhalení MAC Address v paketech IPv6 může vyvolat obavy o soukromí, protože umožňuje sledování zařízení v různých sítích.
- Protokol DHCPv6: DHCP je definován v RFC3315 a podobá se DHCP používanému pro IPv4, umožňuje však řízenější a centralizovanější konfiguraci, včetně správy pronájmů, dalších možností (DNS, MTU...) a registrace databází. DHCPv6 může fungovat samostatně nebo spolu s bezstavovou konfigurací a poskytovat další parametry bez vlastního přidělování IP Address.


**Důležitá poznámka:** Při metodě založené na MAC je MAC Address převeden na 64bitový identifikátor pomocí formátu EUI-64. Tento mechanismus vkládá bajty `FF:FE` doprostřed původního MAC Address (ve 48 bitech) a invertuje 7. bit pro označení globální jedinečnosti. Výsledkem je stabilní identifikátor Interface, který se používá v úplném IPv6 Address.


Zde je příklad transformace MAC Address na EUI-64:


![Image](assets/fr/045.webp)



Kvůli rostoucím obavám ze sledování zařízení však moderní operační systémy (zejména Linux, Windows 10+, macOS a Android) nyní ve výchozím nastavení umožňují rozšíření ochrany soukromí. Ta používají náhodně generované identifikátory Interface, které se pravidelně obnovují pro odchozí spojení, zatímco pro vnitřní komunikaci (například DNS nebo DHCPv6) zachovávají stabilní identifikátor.


Stejně jako u protokolu DHCP v protokolu IPv4 mohou mít automaticky přidělené adresy IPv6 dvě doby životnosti definované směrovači nebo servery DHCPv6:


- Preferovaná doba životnosti*: po uplynutí této doby zůstává Address platný, ale již se nepoužívá k navazování nových spojení;
- Platná doba životnosti*: po uplynutí této doby je Address zcela odstraněn z konfigurace Interface.


Tento systém umožňuje dynamicky řídit změny v síti, například zajistit hladký přechod od jednoho poskytovatele internetových služeb k jinému. Aktualizací prefixu ohlašovaného směrovači a souběžnou úpravou záznamů DNS lze provést migraci na IPv6 bez znatelného přerušení služeb.


**Tip:** Kombinované použití životních cyklů Address a DNS umožňuje implementovat strategii postupného přechodu, kdy nová připojení přejdou na novou topologii, zatímco stávající připojení pokračují až do svého přirozeného konce.


Stručně řečeno, IPv6 nabízí širokou škálu flexibility pro Address Assignment: ruční konfiguraci, bezstavovou nebo stavovou automatickou konfiguraci, DHCPv6 nebo náhodné generování. EEkaždý přístup má své výhody a omezení a lze jej přizpůsobit podle požadované úrovně kontroly, velikosti sítě nebo potřeb ochrany osobních údajů.


## Přiřazení bloků IPv6 Address


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Distribuce Address


Schéma přidělování Address protokolu IPv6 bylo strukturováno tak, aby splňovalo dva cíle: zaručit globální jedinečnost Address a umožnit logickou hierarchii, která podporuje agregaci a zjednodušení směrovacích tabulek.

Stejně jako v případě protokolu IPv4 stojí na vrcholu této hierarchie *Úřad pro přidělování čísel v Internetu* (IANA). Spravuje globální prostor pro jednosměrové vysílání Address a deleguje bloky Address pěti regionálním internetovým registrům (_RIR_).


Pět stávajících RIR je následujících:


- ARIN (Severní Amerika),
- RIPE NCC (Evropa, Střední východ, Střední Asie),
- APNIC (Asie a Tichomoří),
- AFRINIC (Afrika),
- LACNIC (Latinská Amerika a Karibik).


IANA přiděluje každému RIR bloky IPv6 různé velikosti, obvykle mezi /23 a /12. Tento přístup nabízí flexibilitu a zároveň zajišťuje dlouhodobou škálovatelnost. Tyto bloky RIR následně přerozdělují poskytovatelům internetových služeb (ISP), velkým společnostem a veřejným institucím.


Od roku 2006 dostává každý RIR od IANA blok IPv6 /12, jehož pevná velikost má zajistit stabilní a dostatečně velkou rezervu pro budoucí růst. RIR je obvykle dělí na bloky /23, /26 nebo /29. Poskytovatelé internetových služeb nejčastěji dostávají bloky /32, i když tato velikost se může lišit v závislosti na velikosti a zeměpisné oblasti poskytovatele. Zákazníkům obvykle přidělují bloky /48. Každý blok /48 poskytuje 65 536 různých podsítí /64 (což je ve srovnání s IPv4 obrovská kapacita).


**Důležitá poznámka:** blok /32 obsahuje přesně 65 536 dílčích bloků /48. To znamená, že každý poskytovatel internetu může obsloužit desítky tisíc zákazníků, aniž by vyčerpal svůj příděl. Díky svému /48 pak bude mít každý zákazník k dispozici gigantické množství prostoru pro strukturování vlastní interní sítě s libovolným počtem segmentů /64.


Typická hierarchie přidělování vypadá takto:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Díky tomuto množství adres již není nutné používat NAT (*Network Address Translation*), který byl v IPv4 nezbytný pro řešení nedostatku adres Address. Každý hostitel může mít jedinečnou, globálně směrovatelnou veřejnou adresu Address, což zjednodušuje konektivitu mezi koncovými body a usnadňuje používání protokolů, jako je IPSec, VoIP nebo příchozí připojení.


Chcete-li zjistit, které organizaci patří IPv6 Address, můžete použít příkaz `whois` k dotazu do veřejných databází RIR. Tato transparentnost umožňuje identifikovat organizaci, která prefix vlastní, což může být užitečné pro síťové, analytické nebo bezpečnostní účely.


### Adresování PA vs. PI


Původně byl model přidělování IPv6 založen výhradně na blocích PA (*Provider Aggregatable*), tedy spojených s poskytovatelem internetových služeb. V tomto modelu organizace získává prefix od svého poskytovatele internetových služeb, což znamená, že změna poskytovatele vyžaduje přečíslování celé infrastruktury.


Přestože funkce automatické konfigurace protokolu IPv6 a životnost Address usnadňují přečíslování, zůstává to pro organizace s kritickou infrastrukturou nebo s připojením více poskytovatelů kvůli požadavkům na redundanci nepohodlné.


Od roku 2009 umožňují zásady přidělování bloků PI (*Nezávislý poskytovatel*). Tyto bloky (obvykle o velikosti /48) přiděluje RIR přímo společnosti nebo instituci, nezávisle na poskytovateli internetových služeb. Tento model je vhodný zejména pro organizace, které používají *multihoming* (tj. jsou připojeny k několika operátorům současně). Například v Evropě je politika přidělování PI popsána v dokumentu RIPE-512.


### Zápis masky podsítě


Stejně jako v protokolu IPv4 používá protokol IPv6 zkratku CIDR (*Classless Inter-Domain Routing*). To spočívá v uvedení počtu bitů tvořících prefix za znakem Address pomocí znaku `/`.


Vezměme si následující příklad:


```
2001:db8:1:1a0::/59
```


To znamená, že prvních 59 bitů je pevných a identifikuje síť. Všechny zbývající bity (zde 69 bitů) lze použít k identifikaci podsítí nebo hostitelů.


Tento zápis tedy zahrnuje adresy od `2001:db8:1:1a0:0:0:0:0` do `2001:db8:1:1bf:ffff:ffff:ffff:ffff:ffff`.


Tento blok tedy pokrývá sadu 8 /64 podsítí, z nichž každá může hostit obrovské množství zařízení.


Zápis CIDR umožňuje přesné plánování prostoru Address od rozsáhlých sítí až po domácí konfigurace a virtualizovaná prostředí a podporuje agregaci tras, čímž snižuje zatížení směrovačů a zlepšuje škálovatelnost.


### Pakety a hlavičky IPv6


Formát paketů IPv6 se od formátu IPv4 liší tím, že je jednodušší a rozšiřitelnější. Datagram IPv6 vždy začíná záhlavím o pevné velikosti 40 bajtů, které obsahuje všechny podstatné směrovací informace. Tento zjednodušený přístup ve srovnání s proměnlivou délkou záhlaví protokolu IPv4 (od 20 do 60 bajtů) umožňuje směrovačům rychlejší a efektivnější zpracování paketů.


Protokol IPv6 však neodstraňuje žádné funkce: namísto začlenění mnoha volitelných polí do hlavní hlavičky zavádí systém rozšiřujících hlaviček, které jsou umístěny bezprostředně za základní hlavičkou. Tyto volitelné hlavičky umožňují přidávat data nebo instrukce specifické pro určité funkce, aniž by zbytečně zatěžovaly běžné pakety.


Některé hlavičky rozšíření mají pevnou strukturu, zatímco jiné mohou obsahovat různý počet možností. V těchto volbách jsou zakódovány jako trojice `{Typ, Délka, Hodnota}`:


- Pole "Typ" (1 bajt) označuje povahu volby;
- První dva bity "Type" určují, co mají směrovače udělat, pokud volba není rozpoznána:
 - Tuto možnost ignorujte a pokračujte v léčbě,
 - Zahoďte datagram,
 - Zahodit a odeslat zdrojovému serveru chybu ICMP.
 - Zahodit datagram bez oznámení (v případě paketů vícesměrového vysílání).
- Pole "Délka" (1 bajt) určuje velikost pole "Hodnota" v rozsahu 0 až 255 bajtů;
- Pole "Hodnota" obsahuje údaje spojené s danou možností.


Zde je přehled různých typů rozšiřujících hlaviček definovaných protokolem IPv6.


#### Záhlaví Hop-by-Hop


Toto záhlaví, pokud je přítomno, je vždy umístěno bezprostředně za základním záhlavím. Obsahuje informace, které musí zpracovat každý směrovač na cestě paketu, na rozdíl od většiny ostatních hlaviček, které obvykle zpracovává pouze cílový uzel. Typické použití zahrnuje signalizaci globálních parametrů nebo požadavek na konkrétní kroky zpracování při průchodu paketu sítí.


![Image](assets/fr/047.webp)


#### Záhlaví směrování


Směrovací hlavička určuje seznam mezilehlých adres, kterými musí paket projít. Existují dva hlavní režimy směrování:


- Přísné směrování: přesná cesta je předem definována
- Volné směrování: jsou specifikovány pouze některé povinné kroky.


První čtyři pole této kořenové hlavičky jsou:


- Next Header**: určuje typ dalšího záhlaví;
- Routing Type**: definuje metodu směrování (obvykle `0`);
- Zbývající segmenty**: počet segmentů, které zbývá projít ;
- Address[n]**: seznam zprostředkujících adres.


Pole "Zbývající segmenty" začíná celkovým počtem zbývajících segmentů a při každém skoku se snižuje o jedničku.


![Image](assets/fr/048.webp)


#### Fragmentační hlavička


V protokolu IPv6 smí datagram fragmentovat pouze zdrojový hostitel, na rozdíl od protokolu IPv4, kde tak mohou činit i směrovače. Všechny uzly protokolu IPv6 musí být schopny zpracovávat pakety o velikosti alespoň 1280 bajtů. Pokud směrovač narazí na paket větší než MTU následujícího spoje, odešle zprávu *ICMPv6 Packet Too Big* zpět zdroji, který pak upraví velikost svých přenosů.


Fragmentační hlavička obsahuje následující pole:


- Identifikace**: jedinečný identifikátor datagramu pro opětovné sestavení.
- Fragment Offset**: pozice fragmentu v původním datagramu.
- M flag**: označuje, zda následují další fragmenty.


![Image](assets/fr/049.webp)


#### Ověřovací hlavička (AH)


Tato hlavička je určena k zabezpečení komunikace ověřením pravosti odesílatele i integrity dat. Běžně se používá s protokolem IPsec. Pomocí ověřovacího kódu může příjemce potvrdit, že zpráva skutečně pochází od očekávaného odesílatele a že nebyla při přenosu pozměněna.


V případě pokusu o podvodnou modifikaci již nebude ověřovací kód odpovídat a datagram může být odmítnut. Tento mechanismus také chrání před útoky typu replay tím, že detekuje neoprávněné duplikace.


![Image](assets/fr/050.webp)


#### Záhlaví možností cíle


Tato hlavička je určena pouze konečnému příjemci datagramu. Může být použita k přidání možností nebo metadat specifických pro aplikaci, aniž by je zprostředkující směrovače braly v úvahu.


Původně taková možnost v protokolu definována nebyla. Tato hlavička však byla zavedena při návrhu protokolu IPv6, aby bylo možné v budoucnu přidávat rozšíření, aniž by se změnila celková struktura paketu. Například volba null se používá pouze k vyplnění záhlaví na násobek 8 bajtů pro účely zarovnání paměti.


![Image](assets/fr/051.webp)


Návrh paketů IPv6 je založen na jasném oddělení minimální základní hlavičky a modulárních rozšiřujících hlaviček. Tato architektura zajišťuje jak standardní výkon zpracování, tak flexibilitu potřebnou pro vývoj protokolu a integraci zabezpečení, komplexního směrování nebo mechanismů kvality služby při zachování kompatibility s budoucími infrastrukturami.


## Vztah mezi IPv6 a DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


V moderních sítích překládá systém DNS (*Systém doménových jmen*) názvy domén na IP adresy, které mohou počítače používat. Se zavedením protokolu IPv6 se musel systém DNS přizpůsobit tak, aby podporoval 128bitové adresy a zároveň zachoval zpětnou kompatibilitu s protokolem IPv4. Tato koexistence je důležitá zejména v prostředích s duálním zásobníkem, kde obě verze protokolu IP fungují současně.


### Záznamy DNS specifické pro IPv6


K přiřazení názvu domény k adrese IPv6 Address používá systém DNS záznam AAAA (*quad-A*), který je obdobou záznamu "A" pro adresy IPv4. Záznam AAAA explicitně mapuje název domény na IPv6 Address.

Příklad:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Tento záznam označuje, že doména `ipv6.mydmn.org` se překládá na IPv6 Address `2001:66c:2a8:22::c100:68b`. Je možné, a pro maximální kompatibilitu dokonce doporučené, přiřadit stejné doménové jméno k několika IP adresám, ať už IPv4 (prostřednictvím záznamu A) nebo IPv6 (prostřednictvím záznamu AAAA). To umožňuje zákazníkům kompatibilním s protokolem IPv6 upřednostňovat IPv6 a zároveň zajišťuje, že klienti podporující pouze IPv4 zůstanou podporováni.


Systém DNS navíc podporuje zpětné rozlišení, což znamená, že dokáže vyhledat název domény přiřazený k danému IP adresnímu místu Address. V případě protokolu IPv6 tato operace využívá záznamy PTR umístěné v zóně `ip6.arpa`. Tato zóna je vyhrazena speciálně pro reverzní překlad protokolu IPv6. V případě protokolu IPv4 je to zóna `in-addr.arpa`.


### Obrácené rozlišení


Reverzní překlad protokolu IPv6 Address probíhá podle přísného postupu:

1) Rozbalte kód Address do úplného šestnáctkového zápisu (16 bajtů, tj. 32 šestnáctkových číslic).

Příklad:


```shell
2001:66c:2a8:22::c100:68b
```


Stává se:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Obraťte pořadí jednotlivých hexadecimálních číslic (nibble), oddělte je tečkami a připojte `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Tato struktura zajišťuje standardizované a jedinečné zpětné vyhledávání v prostoru IPv6 Address.


**Upozornění**: DNS dotazy mohou být zasílány přes IPv4 nebo IPv6. Použitý přenosový protokol nemá žádný vliv na typ vrácených záznamů.

Například:


- Klient připojený přes IPv6 může požádat o záznam IPv4.
- Klient připojený přes IPv4 může požádat o záznam IPv6.

Server DNS jednoduše odpoví záznamy, které má k dispozici, bez ohledu na přenosový protokol dotazu.


Pokud je název hostitele mapován na IPv4 i IPv6, výběr Address se řídí protokolem RFC 6724, který definuje algoritmus výběru Address na základě faktorů, jako je preference předpony, rozsah a dosažitelnost. Ve výchozím nastavení je obecně upřednostňován protokol IPv6, pokud není potlačen konfigurací systému nebo sítě.


**Důležitá připomínka**: při vkládání adresy IPv6 Address do adresy URL (*Uniform Resource Locator*) musí být uzavřena v hranatých závorkách (`[]`). Tím se zabrání záměně dvojtečky (`:`) uvnitř IPv6 Address a dvojtečky oddělující název hostitele od portu v adrese URL.


Platný příklad:


```shell
http://[2001:db8::1]:8080
```


Tím je zajištěno správné zpracování adresy URL prohlížeči i webovými servery.


Integrace protokolu IPv6 do systému DNS se proto opírá o nové typy záznamů, přísnou metodu zpětného rozlišení a přesná pravidla výběru a formátování, která zajišťují kompatibilitu a konzistenci směrování.


### Shrnutí části


V této části jsme prozkoumali základní principy adresování IPv6. Začali jsme zkoumáním struktury protokolu IPv6 Address: jeho 128bitové délky, hexadecimálního zápisu a zjednodušujících pravidel používaných ke zkrácení opakujících se sekvencí nul. Tato konstrukce umožňuje protokolu IPv6 překonat omezení prostoru Address protokolu IPv4 a zároveň zaručuje škálovatelnost a efektivní hierarchii.


Poté jsme se věnovali různým kategoriím adres IPv6: unicast, anycast a multicast, přičemž jsme podrobně popsali jejich rozsah, typické použití a zastoupení v prostoru Address.


Dále jsme se zabývali metodami přidělování adres IPv6 v místní síti, ať už ruční konfigurací, protokolem DHCPv6 nebo pomocí mechanismů bezstavové automatické konfigurace, které nabízí například protokol NDP. Tyto přístupy umožňují zařízením automaticky přidělovat vlastní Address z poskytnutého prefixu a jejich MAC Address (prostřednictvím EUI-64) a zároveň nabízejí flexibilitu z hlediska správy doby životnosti a soukromí.


Podrobně jsme také popsali, jak se bloky Address přidělují, počínaje organizací IANA, která je rozděluje pěti regionům RIR (*Registered Internet Regions*) a poté poskytovatelům internetových služeb, kteří je přerozdělují svým zákazníkům jako podsítě (často ve formátu /48, což umožňuje 65536 /64 podsítí). Rozlišení mezi _Provider Aggregatable_ (PA) a _Provider Independent_ (PI) bloky pomáhá řídit scénáře _multihoming_ nebo změny poskytovatele.


Viděli jsme, že systém DNS se přizpůsobil protokolu IPv6 zavedením záznamu AAAA a že mechanismy reverzního rozlišení se nyní spoléhají na zónu `ip6.arpa`. Důležité je, že systém DNS zůstává nezávislý na použitém přenosovém protokolu (IPv4 nebo IPv6), což zajišťuje bezproblémovou interoperabilitu v prostředí dvou zásobníků.


Protokol IPv6 tedy není jen postupným vylepšením protokolu IPv4, ale kompletním přepracováním adresního systému, který je vytvořen tak, aby vyhovoval současným i budoucím výzvám globálního internetu.


V závěrečné části tohoto kurzu NET 302 přejdeme do praxe a zaměříme se na nástroje pro diagnostiku sítě.



# Síťové diagnostické nástroje


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Nástroje pro přístup k síti Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


V této první kapitole závěrečné části věnované diagnostice sítě se zaměříme na nástroje pro analýzu přístupu k síti Layer modelu TCP/IP. Tento Layer je zodpovědný za přímou komunikaci mezi zařízeními ve stejné fyzické síti, zejména prostřednictvím adres MAC a fyzických síťových rozhraní, jako jsou karty Ethernet nebo rozhraní Wi-Fi.


Cílem je poskytnout správcům praktické nástroje pro kontrolu, testování a optimalizaci této základní Layer konektivity na nízké úrovni. Tyto nástroje lze použít k ověření správné činnosti rozhraní, k řešení problémů s konfigurací síťových karet nebo k odhalení anomálií, jako jsou kolize, ztráta paketů nebo chyby spojení.


### Nástroje pro sousedství IP/MAC


#### nástroj `Arp`


Jedním z nejstarších diagnostických nástrojů v systému Network Access Layer je příkaz `arp`. I když je stále častěji nahrazován moderními alternativami, jako je `ip neigh` (které objevíme za chvíli). `Arp` je stále přítomen v mnoha systémech a slouží k zobrazení nebo manipulaci s mezipamětí protokolu ARP (*Address Resolution Protocol*). Tato mezipaměť uchovává mapování mezi IP adresami a MAC adresami známými lokálně v počítači. Jinými slovy umožňuje určit, který fyzický (MAC) Address odpovídá danému IP Address v místní síti.


V praxi to znamená, že když chce hostitel odeslat paket na IP Address ve stejné podsíti, musí nejprve znát MAC Address cílového počítače. Toto mapování zajišťuje ARP, který vysílá požadavek do místní sítě a přijímá odpověď obsahující odpovídající MAC Address. Tento výsledek je pak dočasně uložen v místní tabulce zvané "mezipaměť ARP", aby se zabránilo opakování požadavků pro každý nový paket.


Chcete-li zobrazit obsah této mezipaměti a zkontrolovat aktuálně známé položky, použijte:


```bash
arp -a
```


Tento příkaz zobrazí seznam všech místně registrovaných mapování IP/MAC na všech rozhraních. Na každém řádku je uveden název hostitele (pokud je možné jej rozlišit), IP Address, odpovídající MAC Address a Interface, kde je mapování pozorováno.


Chcete-li filtrovat zobrazení na konkrétní IP Address, jednoduše jej zadejte:


```bash
arp -a 192.168.1.5
```


Díky tomu lze snadno zkontrolovat, zda je konkrétní IP adresa Address přítomna v mezipaměti, což může pomoci diagnostikovat selhání komunikace mezi dvěma hostiteli ve stejné síti.


Chcete-li zobrazit pouze záznamy ARP spojené s konkrétní sítí Interface (například s kartou Ethernet s názvem `eth0`), můžete použít následující příkaz:


```bash
arp -a -i eth0
```


To je užitečné zejména v prostředích s více Interface (kabelové, bezdrátové, VPN atd.), kde může mít jeden hostitel několik síťových adaptérů.


Příkaz `arp` není omezen na použití pouze pro čtení. Lze jej také použít k ruční úpravě mezipaměti ARP, což je neocenitelná funkce v některých pokročilých scénářích řešení problémů nebo při simulaci specifických podmínek. Můžete například ručně přidat mapování IP/MAC:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Tento příkaz vytvoří statickou položku v místní tabulce ARP, která přiřadí IP adresu Address `192.168.1.7` k MAC adrese Address `00:17:BC:56:4F:25` na zařízení Interface `eth2`.Pokud není zadána žádná adresa Interface, systém automaticky použije první použitelnou.


Záznam můžete z mezipaměti ARP také odebrat, a to buď za účelem opravy chyby, nebo za účelem vynucení opětovného vyhledání:


```bash
arp -d 192.168.1.7
```


Tím se záznam odstraní a zajistí se, že při dalším pokusu o komunikaci bude vyvolán nový požadavek ARP.


**POZNÁMKA**: Volba delete přijímá také název Interface, což umožňuje přesněji zacílit odstranění konkrétní položky.


Nástroj `arp` poskytuje nízkoúrovňovou diagnostiku, která je užitečná zejména v místních sítích, kde lze problémy s připojením často vysledovat až k nesprávnému nebo zastaralému rozlišení Address. V posledních systémech, zejména v moderních distribucích Linuxu, je však tento nástroj stále častěji nahrazován příkazem `ip neigh` ze sady nástrojů `iproute2`, který nabízí podobnou funkčnost v jednotnějším rámci.


#### nástroj `Ip neighbor`


V moderních systémech, zejména v nejnovějších distribucích Linuxu, je příkaz `ip neigh` nástrojem pro kontrolu a správu mapování mezi adresami IP a MAC. Tento příkaz je součástí sady `iproute2`, která postupně nahrazuje starší nástroje, jako je `arp`, a poskytuje konzistentnější a flexibilnější rámec pro diagnostiku na datovém spoji Layer.


Příkaz `ip neighbor` se dotazuje na místní cache sousedů IP, která je ekvivalentní cache ARP pro IPv4 a cache NDP (_Neighbor Discovery Protocol_) pro IPv6. Tato mezipaměť uchovává známé asociace mezi IP adresami (v4 nebo v6) a MAC adresami spolu s jejich stavem (platné, čekající, vypršely...).


Základní příkaz pro zobrazení mezipaměti je:


```bash
ip neigh
```


Vypíše se seznam záznamů, ve kterém se zobrazí cílová IP adresa Address, příslušná síť Interface, přidružená MAC adresa Address (je-li k dispozici) a stav záznamu (např. `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).


Příklad výstupu:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Tento řádek označuje, že počítač zná platné mapování mezi IP adresou Address `192.168.1.5` a MAC adresou Address `00:17:BC:56:4F:25` prostřednictvím Interface `eth0`.


Záznamy můžete také filtrovat podle kritérií, jako je IP Address, Interface nebo stát. Chcete-li se například dotazovat pouze na Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Nebo pro zobrazení všech záznamů pro Interface `eth1`:


```bash
ip neigh show dev eth1
```


Kromě konzultace lze k ruční úpravě mezipaměti použít také funkci `ip neighbor`. Například k přidání statické položky:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Tím se trvale přiřadí IP adresa Address `192.168.1.7` k zadané MAC adrese Address na Interface `eth1`. Volba `nud permanent` (pro _Neighbor Unreachability Detection_) zajišťuje, že záznam nebude automaticky zneplatněn.


Pokud chcete naopak položku mezipaměti odstranit:


```bash
ip neigh del 192.168.1.7 dev eth1
```


To donutí systém, aby při příští komunikaci s daným serverem Address znovu vyřešil mapování.


**POZNÁMKA**: Nástroj `ip neighbor` funguje pro IPv4 i IPv6. Pro IPv4 spolupracuje s ARP; pro IPv6 spolupracuje s NDP. To poskytuje jednotný a konzistentní přístup ke správě vztahů IP/MAC napříč rodinami protokolů, čímž se `ip neigh` stává moderním standardem pro správu sousedů v systémech Linux.


### Nástroje pro analýzu balíčků


K důkladné analýze dění v počítačové síti potřebují správci nástroje, které dokáží zachytit pakety vyměňované mezi počítači. Jako měřítka slouží dva nástroje: `tcpdump` a `Wireshark`. Tyto nástroje jsou nezbytné pro diagnostiku abnormálního chování, audit výměny protokolů nebo studium zabezpečení sítě pomocí kontroly obsahu rámců.


#### `ttcpdump`: analýza příkazového řádku


`tcpdump` je vysoce výkonný nástroj příkazového řádku určený k zachycení a zobrazení paketů procházejících sítí Interface. Pracuje v reálném čase a díky své nenáročné konstrukci jej lze používat na systémech bez grafického prostředí Interface nebo s omezenými prostředky. Spoléhá na knihovnu `libpcap`, která poskytuje hardwarově nezávislé nízkoúrovňové funkce pro zachytávání.


Běžným použitím `tcpdump` je sledování síťové aktivity počítače nebo síťového segmentu a filtrování paketů podle určitých kritérií. Výsledky lze přesměrovat do souboru a provoz archivovat pro pozdější analýzu nebo přehrát v jiném nástroji, například Wireshark.


Obecná syntaxe příkazu je:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` zapíše zachycené pakety do souboru ve formátu `libpcap` (přípona `.cap` nebo `.pcap`);
- `-i` určuje síť Interface, která se má sledovat (např. `eth0`, `wlan0`);
- `-s` nastavuje maximální množství dat zachycených v jednom paketu. Při zadání `0` se zachytí všechny pakety;
- `-n` zakáže překlad názvů DNS a služeb, čímž zlepší výkon.


Výrazové filtry na konci příkazu umožňují omezit zachycení na podmnožinu přenosů. Pro zpřesnění výběru můžete kombinovat klíčová slova `host`, `port`, `src`, `dst` atd.


Příklad: zachycení paketů HTTP (port 80) ze serveru `192.168.25.24` a jejich uložení do souboru `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Výsledný soubor lze později analyzovat v grafickém nástroji nebo přehrát v jiném systému.


#### Wireshark: pokročilá vizuální analýza


Wireshark, dříve známý jako *Ethereal*,je kompletní program pro analýzu sítě s grafickým rozhraním Interface. Na rozdíl od `tcpdump` poskytuje strukturovanou a podrobnou vizualizaci paketů, včetně rozřezání protokolů, grafů toků, statistik provozu a interaktivních filtrů. Spoléhá také na `libpcap`, což znamená, že dokáže otevřít a zpracovat zachycené soubory generované programem `tcpdump`.


Wireshark je k dispozici v mnoha operačních systémech včetně Linuxu a Windows. Jeho instalace vyžaduje oprávnění správce pro přístup k rozhraním pro snímání. Po spuštění můžete z nabídky *Capture* vybrat síť Interface. Klepnutím na tlačítko *Start* zahájíte nahrávání paketů v reálném čase. Zobrazení je rozděleno do tří panelů:


- seznam zachycených snímků ;
- podrobnosti dekódované protokolem,
- surová hexadecimální data.



![Image](assets/fr/052.webp)



Wireshark vyniká ve scénářích, kdy potřebujete sledovat složité chování protokolu, rekonstruovat dialogy aplikace (například relaci HTTP nebo DNS) nebo studovat dobu odezvy služby. Podporuje také velmi specifické filtry zobrazení, které využívají speciální syntaxi (odlišnou od syntaxe `tcpdump`) a zaměřují se pouze na relevantní pakety.


#### Doplňkové nástroje


Je důležité si uvědomit, že `tcpdump` a Wireshark nejsou zaměnitelné: každý z nich má své silné stránky. `tcpdump` je vhodnější pro prostředí příkazového řádku, automatizované skripty a vzdálené zásahy do serveru, zatímco Wireshark je ideální pro podrobnou, interaktivní a výukovou analýzu provozu.


Oba nástroje lze kombinovat: pomocí `tcpdump` lze zachytit data na vzdáleném systému a poté přenést soubor `.cap` k analýze pomocí programu Wireshark na místním počítači. Tento přístup je v praxi hojně využíván.


### Nástroje pro analýzu Interface


V zařízení Network Access Layer je často nutné dotazovat se a konfigurovat fyzická síťová rozhraní za účelem diagnostiky poruch, optimalizace výkonu nebo ověření integrity připojení. Jedním z nejvýkonnějších nástrojů, které jsou pro tento účel v systému Linux k dispozici, je `ethtool`, nástroj příkazového řádku, který nejen poskytuje podrobné technické informace o ethernetovém rozhraní Interface, ale také umožňuje upravovat některé jeho parametry v reálném čase.


#### Zobrazit specifikace Interface


Základní funkcí nástroje `ethtool` je možnost dotazovat se na Interface a zobrazit jeho aktuální charakteristiky. To vám umožní zkontrolovat:


- rychlost linky (např. 100 Mbit/s, 1 Gbit/s nebo 10 Gbit/s);
- režim vyjednávání (poloduplexní nebo plný duplex) ;
- zda je povoleno automatické vyjednávání;
- typ portu (měděný, optický atd.) ;
- stav spojení (aktivní nebo ne) ;
- podpora pokročilých funkcí, jako je *Wake-on-LAN*.


Tyto informace jsou užitečné zejména při diagnostice problémů souvisejících s fyzickým připojením nebo neshodným nastavením vyjednávání mezi síťovou kartou hostitele a zařízením, ke kterému se připojuje (přepínač, směrovač atd.).


Chcete-li tyto informace získat, jednoduše spusťte:


```bash
ethtool enp0s3
```


Tento příkaz vypíše podrobnou zprávu o `enp0s3` Interface, což je běžná konvence pojmenování v systémech CentOS nebo RHEL.



![Image](assets/fr/053.webp)



#### Dynamická úprava parametrů Interface


nástroj `ethtool` se neomezuje pouze na pozorování: umožňuje také upravovat některé parametry Interface bez restartování počítače. To umožňuje například vynutit určitou rychlost linky nebo povolit funkce podle potřeb místní sítě.


Volba `-s` slouží k dynamické konfiguraci parametrů, jako jsou:


- rychlost linky (`speed`), nastavená explicitně (např. 1000 pro 1 Gbit/s) ;
- duplexní režim (`duplex`), buď `poloviční` nebo `plný` ;
- zapnutí nebo vypnutí automatického vyjednávání (`autoneg`) ;
- povolení funkce *Wake-on-LAN* (`wol`) ;
- typ portu.


Příklad 1: Povolení automatického zúčtování na Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Příklad 2: povolte funkci *Wake-on-LAN* (aby se počítač mohl vzdáleně probudit pomocí magického paketu):


```bash
ethtool -s enp0s3 wol p
```


V tomto příkladu určuje volba `p`, že k probuzení dojde, jakmile je detekován paket *Wake-on-LAN*. Toto nastavení se často používá v podnikových prostředích k provádění nočních aktualizací nebo vzdálené údržby.


#### Instalace nástrojů


Je důležité poznamenat, že nástroj `ethtool` není vždy nainstalován ve výchozím nastavení. V distribucích Red Hat/CentOS jej lze nainstalovat příkazem:


```bash
yum install -y ethtool
```


V Debianu a Ubuntu je ekvivalentní příkaz následující:


```bash
sudo apt install ethtool
```


**Pozor**: ve všech příkazech `ethtool` musí být název sítě Interface uveden hned za volbou (jako `-s`). Jakákoli syntaktická chyba v umístění parametrů způsobí neplatnost nebo neúčinnost příkazu.



## Síťové nástroje Layer


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Nástroje pro analýzu provozu


V diagnostice sítě zůstává příkaz `ping` jedním z nejjednodušších a zároveň nejúčinnějších nástrojů pro testování konektivity mezi dvěma počítači. Zjišťuje, zda je vzdálený hostitel v daném okamžiku dosažitelný, a zároveň poskytuje informace o latenci, stabilitě spojení a rozlišení DNS.


Příkaz `ping` využívá protokol ICMP (*Internet Control Message Protocol*). Když uživatel odešle požadavek `ping`, systém odešle paket ICMP "Echo Request" na IP adresu Address nebo název hostitele. Pokud je cílový počítač online a síťová cesta je platná, odpoví paketem ICMP "Echo Reply". Tento jednoduchý mechanismus lze použít k měření latence a zjišťování problémů s připojením nebo s překladem názvu.


Příklad klasického příkazu:


```bash
ping 172.17.18.19
```


Typická odpověď:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


V tomto příkladu bylo překlad názvu proveden automaticky: doména `mydmn.org` je přiřazena k IP adrese Address `172.17.18.19`, což potvrzuje, že překlad DNS funguje správně. Příkaz také poskytuje technické podrobnosti, jako např:


- pořadové číslo iCMP (`icmp_seq`), užitečné pro kontrolu pořadí odpovědí;
- TTL (*Time-To-Live*), který udává počet zbývajících skoků, než bude paket zahozen;
- doba/pozdržení (`time`) vyjádřená v milisekundách, která poskytuje odhad zpoždění linky.


#### Podrobnější analýza parametrů protokolu ICMP


TTL je v protokolu IP kritickým polem. Každý datagram je odesílatelem inicializován hodnotou TTL (často 64, 128 nebo 255). Každý směrovač na cestě tuto hodnotu snižuje o 1. Pokud TTL dosáhne 0 před dosažením cíle, paket je zahozen a odesílateli je vrácena chyba ICMP. Tento mechanismus zabraňuje nekonečným směrovacím smyčkám.


Doba šíření (*okružní zpoždění/čas*) měří zpoždění, s jakým paket opustí odesílatele, dorazí k cíli a vrátí se zpět. V praxi se pro stabilní spojení považuje za přijatelné zpoždění pod 200 ms. Abnormálně vysoké zpoždění může indikovat přetížení sítě, neefektivní směrování nebo špatnou kvalitu spojení.


#### Pokročilé použití `ping`


`ping` poskytuje možnosti pro zpřesnění testů a sledování specifického chování sítě.


Chcete-li odesílat požadavky na vysílání, můžete použít možnost `-b`, která je určena všem hostitelům v podsíti:

```bash
ping -b 192.168.1.255
```


To je užitečné v místních sítích pro rychlé zjištění aktivních hostitelů nebo pro testování, jak síť zpracovává požadavky na vysílání. V mnoha nastaveních však směrovače a brány firewall blokují vysílání pingů, aby se zabránilo útokům zesílením.


Pomocí volby `-i` můžete také zadat vlastní interval mezi požadavky (výchozí: 1 sekunda):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Tím se odešle 10 požadavků ICMP v intervalu 0,2 sekundy. Takové testování je užitečné pro zjišťování kolísání latence v krátkém časovém období nebo pro mírné zatížení spoje za účelem vyhodnocení jeho stability.


### Nástroje pro analýzu směrovacích tabulek


Příkaz `ip route`, který je součástí sady `iproute2`, je v moderních systémech Linux doporučeným a standardním nástrojem pro kontrolu a správu směrovací tabulky IP jádra. Nahrazuje zastaralý příkaz `route` a nabízí přehlednější syntaxi, větší konzistenci a rozšířenou podporu moderních funkcí (IPv6, více tabulek, jmenné prostory atd.).


#### Zobrazení směrovací tabulky


Zobrazení aktuální směrovací tabulky:


```bash
ip route show
```


Tento výstup obsahuje seznam všech tras známých jádru, tj. cest, kterými se odchozí pakety ubírají v závislosti na svém cíli.


Příklad výstupu:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Každý řádek představuje trasu. Klíčová pole zahrnují:


- výchozí**: výchozí trasa, která se použije, pokud neodpovídá žádná specifičtější trasa.
- via**: brána použitá k dosažení cíle.
- dev**: použitá síť Interface.
- proto**: jak byla trasa vytvořena (ručně, DHCP, jádro atd.).
- metric**: náklady na trasu, které se používají k určení priority více možných cest.
- scope**: rozsah trasy (např. `link` pro přímo připojenou trasu).
- src**: zdrojová IP Address používaná pro odchozí pakety na tomto Interface.


#### Přidávání a odstraňování tras


Směrovací tabulku můžete upravovat také dynamicky, například přidáním nebo odebráním statických tras.


Přidání statické trasy:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Tím se nakonfiguruje trasa do sítě `192.168.1.0/24` přes bránu `192.168.1.1` na Interface `eth0`.


Odstranění této trasy:


```bash
ip route del 192.168.1.0/24
```


Tento příkaz odstraní dříve definovanou trasu.


#### Užitečné příkazy


Zde je několik užitečných variant pro analýzu nebo skriptování:


- `ip -4 route`: zobrazí pouze trasy IPv4;
- `ip -6 route`: zobrazí pouze trasy IPv6;
- `ip route list table main`: zobrazí hlavní směrovací tabulku (výchozí hodnota) ;
- `ip route get <Address>`: zobrazí, kterou bránu Interface a bránu použije paket na danou bránu Address.


Příklad:


```bash
ip route get 8.8.8.8
```


Zobrazí se přesná trasa, kterou by paket dosáhl adresy `8.8.8.8`.


### Nástroje pro sledování


Jedním z nejefektivnějších nástrojů pro analýzu trasy, kterou pakety IP procházejí mezi zdrojovým hostitelem a cílovým místem, je příkaz `traceroute`. Ten krok za krokem zobrazuje cestu, kterou pakety procházejí, a identifikuje mezilehlé směrovače, kterými procházejí. V případě poruchy síťového spojení nebo výpadku služby pomáhá příkaz `traceroute` přesně určit místo problému.


Stejně jako u příkazu `ping` lze cíl zadat buď pomocí plně kvalifikovaného názvu domény (FQDN), nebo pomocí IP adresy Address. Například:


```bash
traceroute mydmn.org
```


#### Princip fungování


`traceroute` se spoléhá na pole TTL (*Time To Live*) v záhlaví paketů IP. Jak bylo vysvětleno dříve, toto pole je čítač, který každý směrovač na trase dekrementuje. Když TTL dosáhne nuly, paket je zahozen a směrovač vrátí odesílateli zprávu ICMP "Time Exceeded". Tento mechanismus zabraňuje nekonečným smyčkám v případě chybného směrování.


`traceroute` využívá tohoto chování k mapování směrovačů mezi odesílatelem a příjemcem:


- Nejprve odešle sérii paketů UDP (obvykle tři) s TTL 1. První směrovač narazí na TTL 0, takže paket zahodí a poté odpoví zprávou ICMP, ve které uvede svou IP adresu Address a dobu odezvy.
- Poté odešle další sérii paketů s TTL 2, čímž odhalí druhý směrovač.
- Proces se opakuje, dokud není dosaženo cíle, a hostitel odpoví zprávou ICMP Port Unreachable, která znamená, že koncového bodu bylo dosaženo.


Ve výchozím nastavení používá `traceroute` pakety UDP odesílané na nepoužívané porty (obvykle začínající na 33434), ale může být také nakonfigurován tak, aby používal ICMP (jako `ping`) nebo dokonce TCP, v závislosti na systémech nebo variantách příkazů.


Příklad výstupu:


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


Každý řádek odpovídá jednomu procházenému směrovači a až tři časové údaje (v milisekundách) udávají zpoždění při cestě k danému směrovači. Tyto hodnoty pomáhají posoudit výkonnost jednotlivých segmentů sítě.


#### Interpretace výsledků


Pokud směrovač neodpovídá nebo filtruje zprávy ICMP, zobrazí se místo času odezvy hvězdičky `*`. To může znamenat:


- brána firewall blokuje odpovědi ICMP,
- zařízení nakonfigurované tak, aby neodpovídalo, nebo
- dočasný problém s připojením na trase.


Funkce `traceroute` tak nejen identifikuje prošlou trasu, ale také upozorňuje na místa s neobvyklým zpožděním nebo přerušením.


V některých systémech lze použít ekvivalentní příkaz `tracepath`, který nevyžaduje práva roota. Pro IPv6 použijte `traceroute6` nebo `tracepath6`.


Příklad pro trasování protokolu IPv6:


```bash
traceroute6 ipv6.google.com
```


### Nástroje pro kontrolu aktivních připojení


Pro diagnostiku aktivních síťových připojení a sledování síťové aktivity v systému Linux je moderním referenčním nástrojem příkaz `ss` (zkratka pro _socket statistics_). Je součástí sady `iproute2` a nahrazuje dnes již zastaralý `netstat` a nabízí vyšší výkon a přesnější výsledky.


`ss` zobrazuje aktivní spojení TCP a UDP, naslouchající porty, místní a vzdálené adresy, stavy spojení a související procesy.


#### Obecné použití


Příkaz `ss` zobrazí aktivní připojení TCP, pokud je spuštěn bez voleb. Základní syntaxe:


```bash
ss [options]
```


Některé běžné možnosti zpřesnění analýzy:


- `-t`: zobrazí pouze spojení TCP;
- `-u`: zobrazí pouze UDP spojení;
- `-l`: zobrazí pouze naslouchající zásuvky;
- `-n`: zakáže překlad názvů (surové IP adresy a čísla portů) ;
- `-p`: zobrazí procesy přidružené ke každému soketu (PID a název programu),
- `-a`: zobrazí všechna připojení, včetně neaktivních,
- `-s`: zobrazí statistiky zásuvek na vysoké úrovni.


#### Případové studie


Zobrazení všech aktivních připojení pomocí portu TCP 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Zobrazí se aktivní připojení TCP na portu 80. Stavy jako `LISTEN`, `ESTABLISHED`, `TIME-WAIT` označují aktuální stav každého Exchange.


Příklad výstupu:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Zobrazení všech síťových připojení s přidruženými procesy:


```bash
ss -tulnp
```


Chcete-li získat celkový přehled o využití zásuvek:

```bash
ss -s
```


Filtrování pouze připojení UDP:

```bash
ss -unp
```


Tyto příkazy jsou užitečné zejména pro detekci podezřelých připojení, neočekávaných naslouchajících portů nebo pro sledování aktivity konkrétní služby.


## Přeprava a horní část nástrojů Layer


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Nástroje pro dotazy DNS


Ve vyšších vrstvách modelu TCP/IP, zejména v aplikační vrstvě Layer, je důležité pochopit, jak funguje překlad názvů. Nástroje pro dotazy DNS umožňují zkontrolovat, zda je název domény správně přiřazen k IP Address, a také pomáhají diagnostikovat problémy serveru DNS, jako je nesprávná konfigurace, zpoždění šíření nebo nedostupnost. Tyto nástroje jsou nezbytné pro každého správce sítě nebo uživatele, který chce hlouběji porozumět výměnám DNS v prostředí IP.


#### Příkaz `nslookup`


Nejjednodušším nástrojem pro dotazy DNS je `nslookup`. Ten odešle dotaz na server DNS a vrátí IP adresu Address přiřazenou k názvu domény (nebo naopak). Ve výchozím nastavení se dotazuje na server DNS nakonfigurovaný v systému, ale server můžete zadat i přímo v příkazu.


Příklad přímého vyhledávání:

```bash
nslookup mydmn.org
```


Dotazování na konkrétní server DNS:

```bash
nslookup mydmn.org 192.6.23.4
```


Požadavek žádá server DNS na adrese `192.6.23.4` o překlad názvu `mydmn.org`. To je užitečné zejména pro kontrolu, zda daný server DNS rozpoznává doménové jméno, nebo pro ověření, zda server pracuje správně.


#### Příkaz `dig`


`dig` (*Domain Information Groper*) je modernější, úplnější a flexibilnější nástroj než `nslookup`. Podporuje složité dotazy a poskytuje podrobné informace o procesu řešení, hierarchii zapojených serverů, typu vráceného záznamu (A, AAAA, MX, TXT atd.) a případných chybách.


Základní příklad dotazu:

```bash
dig mydmn.org
```


Dotazování na konkrétní server DNS:

```bash
dig @192.6.23.4 mydmn.org
```


Tento příkaz zkontroluje dostupnost záznamu DNS na daném serveru.

Jednou z hlavních výhod nástroje `dig` je, že zobrazuje podrobnosti odpovědi DNS, což je velmi užitečné pro diagnostiku chyb konfigurace.


#### Ruční konfigurace překladačů DNS


Někdy je nutné přepsat lokálně používané servery DNS, například v testovacích prostředích, nebo vynutit použití konkrétních serverů. To lze provést úpravou souboru `/etc/resolv.conf`, který definuje systémové nastavení rozlišení DNS.


Příklad konfigurace:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Pole `search` určuje doménu, která se má automaticky připojit při překladu krátkých názvů.
- Položky `nameserver` definují servery DNS, které se mají používat, v pořadí podle priority.


V mnoha moderních distribucích (zejména těch, které používají `systemd-resolved`) jsou změny v souboru `/etc/resolv.conf` dočasné a mohou být přepsány při restartu nebo opětovném připojení k síti. Mezi trvalejší metody patří použití `resolvconf`, `systemd-resolved` nebo úprava konfigurace *NetworkManager*.


#### Příkaz `host`


Dalším jednoduchým, ale účinným nástrojem DNS je `host`. Překládá doménová jména na IP adresy (nebo obráceně) a může pomoci diagnostikovat selhání nebo chybnou konfiguraci DNS v síti Interface.


Příklady:

```bash
host mydmn.org
```


Zpětné vyhledávání:

```bash
host 192.6.23.4
```


`host` je obzvláště užitečný pro rychlé kontroly, zejména při použití ve skriptech příkazového řádku.


Opakované nebo intenzivní dotazy na servery DNS třetích stran bez povolení mohou být interpretovány jako pokusy o vniknutí nebo škodlivá činnost. Při nesprávném použití nebo proti sítím, které nemáte pod kontrolou, mohou tyto příkazy připomínat průzkumné skenování, které je často prvním krokem útoku. Vždy omezte jejich použití na prostředí, která spravujete nebo kde máte výslovné oprávnění.


### Nástroje pro skenování sítě


Při monitorování nebo zabezpečení místní nebo rozsáhlé sítě je zásadní identifikovat aktivní zařízení a jimi poskytované služby. Přesně k tomu slouží nástroj `nmap` (*Network Mapper*).


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Představujeme `nmap`


`nmap` umožňuje cílené skenování jednoho nebo více hostitelů za účelem zjištění otevřených portů, dostupných služeb (HTTP, SSH, DNS atd.) a někdy i typu používaného operačního systému. Díky mnoha možnostem poskytuje `nmap` přesný přehled o vystavení sítě, což je nezbytné ve fázích auditu nebo zpřísnění správy infrastruktury.


Stejně jako příkaz `host` nesmí být příkaz `nmap` nikdy použit v sítích nebo infrastrukturách, které nevlastníte, nebo bez výslovného oprávnění. Neoprávněné skenování portů může být označeno jako pokus o škodlivý průzkum, často je detekováno bezpečnostními systémy (firewally, IDS/IPS) a může mít i právní důsledky.


#### Základní použití


Chcete-li prohledat konkrétního hostitele a zobrazit jeho otevřené porty:

```bash
nmap 192.168.0.1
```


Tento příkaz prohledá 1000 nejčastějších portů hostitele `192.168.0.1` a zobrazí služby, ke kterým se přistupuje, a používané protokoly. Pokud je nakonfigurováno rozlišení DNS, můžete místo IP adresy Address použít také název hostitele.


#### Kompletní skenování sítě


Jednou z výhod `nmap` je možnost prohledat celý rozsah adres jediným příkazem. To usnadňuje například rychlou inventarizaci všech aktivních počítačů v síti:


```bash
nmap 192.168.0.0/24
```


V tomto případě budou dotazováni všichni hostitelé v rozsahu `192.168.0.0` až `192.168.0.255`. Pro každou IP adresu Address se ve výsledcích zobrazí seznam otevřených portů, jejich stav (otevřený, filtrovaný atd.), a pokud je to možné, i název příslušné služby.



![Image](assets/fr/055.webp)



Správce se může na `nmap` spolehnout při několika úkolech:


- Zjišťování aktivních hostitelů**: zjištění, které počítače reagují v rámci podsítě;
- Soupis služeb**: zajistěte, aby byly přístupné pouze nezbytné porty (princip nejmenších oprávnění);
- Kontrola shody**: porovnání otevřených portů se zásadami zabezpečení organizace;
- Prevence zranitelností**: odhalení nezabezpečených nebo zastaralých služeb spuštěných na kritických počítačích.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Nástroje pro dotazování procesů


Pro hloubkovou analýzu aktivních procesů a otevřených souborů, zejména v síťovém kontextu, se správci systému Linux často obracejí na příkaz `lsof` (*List Open Files*). Navzdory svému názvu se `lsof` neomezuje na tradiční soubory: v systémech UNIX je za soubor považováno vše, včetně síťových soketů, zařízení a komunikačních kanálů.


Tento nástroj tedy poskytuje průřezový pohled na systém pomocí korelace aktivních procesů, otevřených síťových portů, přístupných souborů a zapojených uživatelů.


#### Analýza sítě pomocí `lsof`


Volba `-i` omezuje výstup na síťová připojení (TCP, UDP, IPv4 nebo IPv6). Díky tomu lze snadno zjistit, které procesy komunikují po síti:


```bash
lsof -i
```


Tento příkaz vypíše všechny spuštěné procesy používající síťový soket a zobrazí používaný port, protokol (TCP/UDP), stav připojení a také PID a přidruženého uživatele.


#### Filtrování podle IP adresy Address nebo portu


Vyhledávání můžete zpřesnit zadáním IP adresy Address a portu a izolovat tak konkrétní síťový tok. Například pro kontrolu relace SMTP (port 25) s konkrétním hostitelem:


```bash
lsof -n -i @192.168.2.1:25
```


Zobrazí se pouze aktivní síťová připojení s hostitelem `192.168.2.1` na portu 25, což je užitečné pro diagnostiku podezřelé aktivity nebo problémů s tokem SMTP.


#### Sledování přístupu k zařízení


Další silnou stránkou `lsof` je sledování speciálních souborů, jako jsou diskové oddíly. Například pro kontrolu, které procesy otevřely soubory na `/dev/sda1`:


```bash
lsof /dev/sda1
```


To se hodí, když se pokus o odmontování nezdaří, protože zařízení je stále používáno, nebo při zjišťování, které aplikace přistupují k oddílu.


#### Křížová analýza: proces a síť


Možnosti lze kombinovat a získat tak přesné informace. Například pro zobrazení všech síťových portů otevřených procesem s PID 1521:


```bash
lsof -i -a -p 1521
```


Volba `-a` protíná kritéria (`-i` a `-p`) a omezuje výstup pouze na síťová spojení daného procesu.


#### Sledování více uživatelů


`lsof` lze také použít k analýze aktivity konkrétních uživatelů, přičemž se zobrazí seznam všech souborů, které otevřeli, volitelně filtrovaný podle PID:


```bash
lsof -p 1521 -u 500,phil
```


Zobrazí se soubory nebo síťová připojení používaná uživatelem `phil` nebo UID 500, omezené na proces 1521.


### Shrnutí sekce


V této závěrečné části jsme se seznámili s celou řadou nepostradatelných nástrojů pro diagnostiku, analýzu a správu počítačových sítí. Tato studie, strukturovaná podle vrstev modelu TCP/IP, nejen objasňuje, jak síťová komunikace funguje, ale také zavádí důslednou metodiku pro identifikaci, izolaci a řešení potenciálních problémů.


Tyto nástroje poskytují správcům ucelenou sadu technických nástrojů pro monitorování stavu sítě, analýzu provozu, audit připojení a rychlé zásahy do vadných zařízení nebo služeb.


#### Přístup k síti Layer


Nástroje poskytující přímý přehled o rozhraních a rámcích:


- arp / ip neigh**: kontrola a úprava mezipaměti ARP/NDP za účelem kontroly nebo opravy asociací IP-MAC;
- tcpdump**: zachytávání paketů z příkazového řádku, možnost filtrování a exportu;
- Wireshark**: grafická analýza paketů s hloubkovým dekódováním protokolů;
- ethtool**: dotaz a nastavení fyzických parametrů karty Ethernet (rychlost, duplex, WoL atd.).


#### Síť Layer


Nástroje pro vyhodnocování připojení IP, směrování a paketového provozu:


- ping**: testování dosažitelnosti a měření latence pomocí protokolu ICMP;
- ip route**: kontrola a úprava směrovací tabulky za účelem kontroly cest paketů;
- traceroute**: identifikace směrovačů na trase k cíli hop po hopu;
- ss**: podrobný soupis soketů TCP/UDP a souvisejících procesů (nástupce netstatu).


#### Transportní a aplikační vrstva


Nástroje pro diagnostiku služeb a procesů:


- nslookup / dig / host**: Dotazy DNS k ověření rozlišení názvů a analýze záznamů;
- nmap**: prozkoumá otevřené porty a vystavené služby a vyhodnotí povrch útoku;
- lsof**: výpis souborů a soketů otevřených procesy, korelace systémové a síťové aktivity.


Zvládnutí těchto nástrojů, z nichž každý odpovídá určité fázi modelu TCP/IP, umožňuje metodický přístup: počínaje fyzickým Layer, přes směrování až po aplikační služby. Tento řetězec odborných znalostí vybavuje správce k diagnostice, zabezpečení a optimalizaci jejich infrastruktury a zajišťuje výkonnost i dostupnost sítě.


# Závěrečná část


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Recenze a hodnocení


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Závěrečná zkouška


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Závěr


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>