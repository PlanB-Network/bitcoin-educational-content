---
name: IP-nätverk från teori till praktik
goal: Lär dig grunderna i IP-nätverk för att bättre kunna konfigurera och felsöka dem.
objectives: 


  - Förstå TCP/IP-protokollets arkitektur och funktion
  - Förklara skillnaderna, fördelarna och begränsningarna med IPv4 och IPv6
  - Identifiera och skilja mellan olika typer av IP Address
  - Konfigurera och verifiera IP-adressering på Unix/Linux-system
  - Använda de viktigaste diagnosverktygen för att analysera och lösa nätverksproblem


---

# Viktiga färdigheter för att navigera i IP-världen


Dyk in i hjärtat av IP-världen och skaffa dig kunskap för att förstå och effektivt hantera dina nätverk. I den här kursen får du lära dig allt du behöver veta om datornätverk på ett tydligt och praktiskt sätt.


Du får lära dig hur nätverk och IP-adressering fungerar, hur man skiljer mellan IPv4 och IPv6, hur man identifierar och använder de olika Address-kategorierna och hur man förstår TCP/IP-protokollets betydelse och de länkar som skapas mellan IP-adresser, fysiska adresser och DNS-namn.


NET 302 riktar sig främst till studenter, Linux-användare eller helt enkelt nyfikna som vill förstå grunderna i nätverk och stärka sin självständighet när det gäller att hantera, felsöka och optimera infrastrukturer.


Kom till oss och omvandla din kunskap till verklig operativ expertis!


___


Denna NET 302-kurs är en anpassning av *Les bases du réseau: TCP/IP, IPv4 et IPv6*, skriven av Philippe Pierre på franska och publicerad på [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), under Creative Commons Erkännande - ShareAlike 4.0 International ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)).



Betydande ändringar har gjorts i Loïc Morels originalversion: texten har skrivits om helt och hållet, utökats och berikats för att ge ett uppdaterat och djupgående innehåll, samtidigt som den pedagogiska andan i Philippe Pierres originalverk har bevarats. Diagrammen har också reviderats.


+++


# Inledning


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Kursöversikt


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Den här kursen ger en fullständig introduktion till grunderna i IP-nätverk. Den är uppdelad i fyra huvudavsnitt som vart och ett täcker en viktig aspekt för att förstå, konfigurera och diagnostisera problem i ett datornätverk.


### TCP/IP-protokoll


I den här första delen lägger vi grunden genom att utforska begreppet nätverk och TCP/IP-protokollets historia. Vi kommer att studera dess huvudkomponenter: IP, TCP, samt en kort titt på QoS-protokollet IPv5. Vi går också igenom tjänsteprimitiver för att bättre förstå logiken i data Exchange.


### IPv4-adressering


Därefter går vi vidare till en modul som handlar om IPv4-adressering. Du får lära dig hur IPv4 används i praktiken, dess olika Address-typer (privat, offentlig, broadcast etc.), DNS grundläggande roll samt hur Ethernet-adresser och ARP-protokollet fungerar. Du får också lära dig NAT (Network Address Translation) och grunderna i nätverkskonfiguration.


### IPv6-adressering


Den tredje delen fokuserar på IPv6-adressering, som är nödvändig för att Address begränsningarna i IPv4. Vi går igenom dess standarder och definitioner, Address Assignment inom ett lokalt nätverk, Address blockhantering och förhållandet mellan IPv6 och DNS.


### Verktyg för nätverksdiagnostik


Vi avslutar med en presentation av de viktigaste verktygen för nätverksdiagnostik. Med hjälp av dessa kan du analysera, kontrollera och åtgärda fel. Denna del kommer att vara strukturerad efter lager: Nätverksåtkomst, nätverk, transport och övre lager.


I slutet av kursen har du grundläggande kunskaper för att effektivt administrera en nätverksinfrastruktur och diagnostisera potentiella problem.


Är du redo att dyka in i datornätverkens värld? Då kör vi!


**ANMÄRKNING**: Beskrivningarna är baserade på ett GNU/Linux CentOS 7-system. Nätverkskonfigurationerna är dock i stort sett desamma när man jämför ett Debian- med ett CentOS-system. Så vi kommer inte att göra någon åtskillnad. När det finns en, kommer vi att prefixera den med en specifik logotyp.


**N.B.**: Om du stöter på obekanta termer under kursens gång, vänligen se [ordlistan] (https://planb.network/resources/glossary) för definitioner.



# TCP/IP-protokoll


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Vad är ett nätverk?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



I den här första modulen tar vi en djupdykning i TCP/IP-protokollet, hörnstenen i modern digital kommunikation. Vi diskuterar dess ursprung, grundläggande principer och det adresseringssystem som används, vilket är avgörande för att säkerställa informationsflödet mellan anslutna enheter.


Vi kommer också att beskriva de huvudkomponenter som strukturerar modellen och förklara hur de samverkar för att skapa ett operativt, tillförlitligt och skalbart nätverk. Men först är det viktigt att gå tillbaka till konceptet med ett nätverk.


Etymologiskt avser ett nätverk en uppsättning punkter som är kopplade till varandra och bildar en sammankopplad struktur. Inom telekommunikation och databehandling översätts denna definition till en grupp enheter (datorer, routrar, switchar, accesspunkter etc.) som kan utbyta data via fysiska eller trådlösa medier. Ett nätverk möjliggör därmed ett kontinuerligt eller intermittent informationsflöde, beroende på krav, vilka protokoll som används och hur den distribuerade arkitekturen ser ut.


Med tiden har flera klassiska topologier utvecklats för att uppfylla olika behov när det gäller kostnad, prestanda, motståndskraft och enkelt underhåll. Dessa inkluderar:


- ringnätverk,
- trädnätverk,
- bussnätverk,
- stjärnnätverk,
- mesh-nätverk.



### Ringnätverk


I en ringtopologi är enheterna anslutna i en sluten slinga: varje station är kopplad till nästa och den sista kopplas tillbaka till den första. I den här konfigurationen fungerar varje enhet som ett relä som skickar data vidare till nästa länk. Beroende på nätverkstyp kan informationen cirkulera i endast en riktning eller i båda.


Fördelen med detta arrangemang är att kablarna är enkla att dra och att man inte är beroende av någon central utrustning. Kontinuiteten i hela nätverket beror dock på hur varje enskilt element mår: om en enda station går sönder kan hela kommunikationssystemet avbrytas. Det är därför som redundans- eller förbikopplingsmekanismer ofta sätts in.



![Image](assets/fr/001.webp)



### Trädnätverk


Trädnätverket, eller den hierarkiska topologin, är utformat efter strukturen i ett släktträd. Det består av successiva nivåer: en rotnod högst upp ansluter till flera noder på lägre nivåer, som i sin tur kan ansluta till andra noder, och så vidare.


Denna hierarkiska layout fungerar särskilt bra för stora nätverk som behöver en tydlig ansvarsfördelning och segmenterad hantering. Men det gör också nätverket sårbart för fel i noder på högre nivåer: om roten eller en huvudgren försvinner kan hela delar av infrastrukturen slås ut.



![Image](assets/fr/002.webp)



### Bussnätverk


I en busstopologi delar alla enheter samma överföringsmedium, vanligtvis en koaxial linje eller optisk fiber. Varje enhet är passivt ansluten, vilket innebär att den inte aktivt ändrar signalen, och den kan skicka eller ta emot data via denna delade kanal.


Den största fördelen med busstopologin är den låga installationskostnaden tack vare förenklad kabeldragning.  I äldre koaxialbaserade implementeringar (Ethernet 10BASE2/10BASE5) kan dock bortkoppling eller förlust av en enda station störa eller till och med stoppa all trafik, eftersom bussens elektriska kontinuitet och avslutningsimpedans inte längre upprätthålls. Att ha ett enda fysiskt medium är också en kritisk svaghet: varje avbrott eller fel stoppar kommunikationen för hela nätverket.



![Image](assets/fr/003.webp)



### Stjärnnätverk


Stjärntopologin, även känd som "hub and spoke", är den vanligaste idag, särskilt i Ethernet-nätverk för hem och kontor. Här ansluts alla enheter till en enda central enhet.


Denna layout gör hantering och underhåll enkelt: om en periferienhet går sönder påverkas inte resten av nätverket. Nackdelen är att den centrala enheten är en enda felkälla: om den går ner stannar kommunikationen överallt. Kabelkvalitet och länklängder måste också noga övervägas för att upprätthålla god prestanda.



![Image](assets/fr/004.webp)



**Anmärkning**: Det finns fortfarande nätverk som är organiserade i en linjär, bussliknande topologi, där utrustningen ansluts efter varandra. Den här lösningen är visserligen billig att installera, men har den stora nackdelen att ett enda avbrott isolerar vissa av värdarna och delar upp nätverket i oberoende undergrupper.


### Mesh-nätverk


Mesh-nätverket är utformat för maximal redundans: varje enhet är direkt ansluten till alla andra enheter. Detta säkerställer kontinuitet i tjänsten även om flera länkar eller enheter inte fungerar, eftersom trafiken kan omdirigeras längs alternativa vägar.


Nackdelen är att antalet anslutningar som måste upprättas ökar snabbt med antalet terminaler. För `N` anslutningspunkter krävs `N × (N-1) / 2` separata länkar, vilket gör denna topologi dyr och komplicerad att driftsätta. Den används därför främst i kritiska nätverk som kräver mycket hög tillgänglighet, t.ex. vissa delar av Internet eller känsliga industriella system.



![Image](assets/fr/005.webp)



Det finns andra varianter, t.ex. grid- eller hyperkubnätverk, som är utformade för specialiserade behov inom distribuerad databehandling eller parallellbearbetning.


På global nivå är Internet en massiv sammankoppling av nätverk med olika topologier, som förenas av gemensam adressering (IPv4 och IPv6) och en samling standardiserade protokoll som definieras av IETF (*Internet Engineering Task Force*). Denna mångfald innebär att Internet inte följer en enda topologi: dess struktur är flexibel, skalbar och oberoende av det logiska adresseringsschema som gör det användbart.



## Ursprunget till TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



Ursprunget till TCP-protokollet ligger hos **ARPA** (*Advanced Research Projects Agency*, omdöpt till "DARPA" 1972), som lanserade **ARPANET**-projektet 1966. Det första ARPANET-segmentet togs i drift i oktober 1969 och sammankopplade universiteten UCLA och Stanford. Syftet var att länka samman forskningscentra genom ett paketförmedlat nätverk som kunde hålla kommunikationen igång även om infrastrukturen delvis skulle fallera.


Som ett led i denna dynamik finansierade ARPA University of Berkeley för att integrera de första TCP/IP-protokollen i sitt BSD Unix-system. Detta spelade en viktig roll för spridningen och standardiseringen av protokollet, först inom den akademiska världen och senare inom industrin.


**Note**: På den tiden hade datavetare ännu inte Linux (som inte skulle dyka upp förrän i början av 1990-talet), och inte heller Minix, det utbildningssystem som Andrew Tanenbaum utformat.  De viktigaste alternativen var Unix eller, ibland, proprietära stordatorer som OpenVMS. Tack vare sin flexibilitet och öppenhet bidrog Unix till att sprida de första nätverkskoncepten.


I strikt mening är TCP/IP inte ett enda protokoll utan en svit av protokoll som bygger på TCP och IP. Det blev känt för att det tillhandahöll en standardiserad programmerings-Interface för utbyte av data mellan maskiner i samma nätverk. Denna Interface, baserad på primitiver som kallas "sockets", gjorde det möjligt att skapa tillförlitliga och flexibla anslutningar samtidigt som viktiga applikationsprotokoll integrerades.


ARPANET är därför den historiska grunden till dagens Internet. Internet är ett globalt nätverk som bygger på principen om paketväxling, där information cirkulerar med hjälp av en uppsättning standardiserade protokoll som säkerställer kompatibilitet och driftskompatibilitet mellan heterogena system. Denna öppna arkitektur har gjort det möjligt att utveckla och distribuera otaliga tjänster och applikationer, bland annat


- e-postmeddelanden,
- world Wide Web (www),
- filöverföring och fildelning...


Styrningen och utvecklingen av dessa protokoll övervakas av ***Internet Architecture Board*** (IAB).

Denna organisation samordnar tekniska riktlinjer genom två huvudstrukturer:


- IRTF** (_Internet Research Task Force_), som bedriver långsiktig forskning om utveckling och förbättring av protokoll.
- IETF** (_Internet Engineering Task Force_), som utvecklar, standardiserar och dokumenterar de operativa protokoll som används på Internet


Fördelningen av nätverksresurser (IP Address-områden, nummer för autonoma system, rotdomännamn etc.) samordnas internationellt av **IANA/ICANN**. Den operativa förvaltningen förlitar sig på: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Europa, Mellanöstern, Centralasien), **ARIN**, **APNIC**, **LACNIC** och **AFRINIC**.


Alla TCP/IP-protokollspecifikationer registreras i dokument som kallas **RFC** (_Request For Comments_), vilka fungerar som auktoritativa tekniska referenser. RFC:erna uppdateras och numreras kontinuerligt för att återspegla den pågående utvecklingen av protokollsviten.


TCP/IP-stacken representeras ofta som en stack med fyra funktionella lager, vilket ofta jämförs med den sju-Layer **OSI** (_Open Systems Interconnection_) modellen som utvecklats av **ISO** (_International Standards Organization_), som fungerar som en konceptuell referens för nätverk.


De fyra lagren i TCP/IP-modellen är


- nETWORK ACCESS Layer, som tillhandahåller protokoll för kontroll av fysisk länk och mediaåtkomst;
- iNTERNET Layer, som hanterar routing och IP-adressering;
- tRANSPORT Layer, som garanterar tillförlitlighet och hantering av dataflöden med hjälp av protokoll som TCP eller UDP ;
- aPPLICATION Layer, som samlar användar- och programvaruprotokoll som HTTP, FTP, SMTP och DNS.



![Image](assets/fr/006.webp)



Idag är IPv4 den mest använda versionen av IP, men dess 32-bitars Address-utrymme har tydliga begränsningar. Detta ledde till skapandet av IPv6, som använder 128-bitars adressering och erbjuder praktiskt taget obegränsad kapacitet: avgörande för att stödja den explosiva tillväxten av anslutna enheter och möta utmaningarna med Internet of Things, mobilitet och säkerhet.


Varje Layer i TCP/IP-stacken tillhandahåller specifika tjänster, vilket gör det möjligt att Address olika nätverksbehov på ett modulärt sätt: fysisk överföring, logisk adressering, dataintegritet och tjänster på applikationsnivå.


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

## IPv5 QoS-protokoll


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



Headern i ett IP-paket är en viktig datastruktur som är indelad i flera fält, vart och ett med en specifik roll för att säkerställa att paketen överförs och behandlas korrekt när de färdas genom nätverket. Dessa fält inkluderar destinations-IP Address (som behövs för att dirigera paketet till den avsedda mottagaren), rubrikens längd som anges i fältet IHL (*Internet Header Length*), den totala paketlängden som registreras i fältet *Total Length*, kontroll- och verifieringsinformation samt andra parametrar för att hantera kommunikationsflöde och kvalitet.


Det allra första fältet i rubriken heter Version. Detta 4-bitarsvärde anger vilken version av IP-protokollet som paketet följer. Det är viktigt eftersom det talar om för varje router eller mellanliggande enhet hur de ska tolka och hantera de inkapslade data.


**Notera: Hanteringen och Assignment av IP-protokollversioner hanteras av **IANA**. Ett 4-bitarsfält ger möjlighet till 16 binära kombinationer (värdena 0 till 15). Deras nuvarande Assignment är:



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

Bland dessa finns IPv5 som, även om det är okänt för allmänheten, fanns som ST (_Stream Protocol_). IPv5 utvecklades på 1980-talet och utformades för att tillgodose ett växande behov vid den tiden: att tillhandahålla "_Quality of Service_" (QoS) för vissa dataflöden som krävde kontinuerlig och stabil överföring, t.ex. Voice over IP eller multimediaströmmar. Målet var att garantera bandbredd och prioritet från början till slut, ett koncept som liknar det som RSVP (_Resource Reservation Protocol_) erbjuder idag för att dynamiskt reservera nätverksresurser på moderna routrar.


IPv5 förblev dock experimentellt och implementerades endast på ett litet antal nätverksenheter. Den begränsade användningen, i kombination med det snabbt växande behovet av mer Address-utrymme, ledde till att Internetkonstruktörerna hoppade direkt från IPv4 till IPv6. På så sätt undvek man både IPv4:s Address-begränsningar och risken för förvirring eller inkompatibilitet med IPv5:s experimentella specifikationer.


Även om IPv5 aldrig fick någon utbredd användning spelade den en viktig roll för att forma det tidiga tänkandet kring QoS och trafikhantering. Idag är det mer av en historisk markör än en fungerande standard.


**Påminnelse** - Ett protokoll är en uppsättning kommunikationsregler: datastrukturer, algoritmer, paketformat och konventioner som gör det möjligt för olika enheter att Exchange information på ett tillförlitligt och begripligt sätt. En tjänst är den konkreta implementeringen av ett protokoll genom specifika program (klienter, servrar) som följer dessa regler och gör funktionaliteten tillgänglig för användare och applikationer.


Nu kan vi ta en närmare titt på hur IP-protokollet, som är grunden för all nätverkskommunikation, är uppbyggt och fungerar.



## IP-protokollet


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definitioner och allmän information


IP-protokollet, eller "***Internet Protocol***", är ryggraden i TCP/IP-modellen. Det transporterar datapaket från en värd till en annan inom ett nätverk, oavsett om det är lokalt eller sträcker sig över hela världen. Det har två nyckelroller: att hantera den logiska adresseringen av enheter och att säkerställa att paket dirigeras över ofta heterogena och sammankopplade nätverk.


På den fysiska nivån förlitar sig överföringen på hårdvarugränssnitt för att upprätta punkt-till-punkt-anslutningar mellan noder. Det är dock IP-protokollet som gör end-to-end-kommunikation möjlig genom att ge varje paket den information det behöver för att navigera genom flera möjliga vägar till sin destination.


Tre Elements för nätverkskonfiguration avgör hur ett paket skickas vidare på sin väg:


- IP Address**: identifierar destinationsvärden i nätverket på ett unikt sätt.
- Subnätmask**: anger vilken del av Address som identifierar nätverket och vilken del som identifierar värden, vilket möjliggör logisk uppdelning i subnät.
- Gateway**: anger den mellanliggande router som paketet ska passera för att nå ett externt nätverk eller ett annat segment i det lokala nätverket.


På Internet flödar inte data som en kontinuerlig ström, utan skickas som **datagram**: oberoende datablock, vart och ett inkapslat med all information som behövs för leverans. Detta är principen för **packet switching**, där information delas upp i fristående enheter som kan ta olika vägar för att nå samma mottagare.


Förutom nyttolasten (*payload*) innehåller varje IP-datagram en strukturerad header med fält som destinations-Address, käll-Address, typ av tjänst, protokollets versionsnummer och annan kontrollinformation som behövs för att hantera överföringen.


Den teoretiska maximistorleken på ett IP-datagram är **65 536 oktetter**, en gräns som sätts av fältet för total längd i rubriken. I praktiken uppnås denna storlek sällan, eftersom de fysiska nätverk som transporterar paketen (Ethernet, Wi-Fi, fiberoptik ...) vanligtvis har en striktare gräns som kallas **MTU** (_Maximum Transmission Unit_). Om ett datagram överskrider den fysiska länkens MTU måste det delas upp i mindre paket, som skickas separat och sätts ihop igen vid ankomsten.


Denna anpassningsförmåga gör IP till ett robust och flexibelt protokoll som kan användas med en mängd olika underliggande tekniker och samtidigt upprätthålla universell kompatibilitet mellan heterogena system och nätverk.



### Fragmentering av IP-datagram


När ett IP-datagram måste passera genom ett nätverk vars överföringskapacitet är mindre än datagrammet självt, måste det **fragmenteras** så att det kan färdas utan problem. Denna fysiska storleksgräns kallas **MTU** (Maximum Transmission Unit): den största ramstorleken som kan passera över ett visst nätverk utan att delas upp.


Varje nätverksteknik har sin egen MTU, som bestäms av dess hårdvaru- och protokollegenskaper. Vanliga värden inkluderar:


- ARPANET**: 1000 byte
- Ethernet**: 1500 byte
- FDDI**: 4470 byte


När ett datagram överskrider MTU för ett nätverkssegment som det måste passera, kommer routningsutrustningen att dela upp det i mindre **fragment** som uppfyller gränsen. Detta händer vanligtvis när man flyttar från ett nätverk med hög MTU till ett med lägre kapacitet. Ett datagram som kommer från ett FDDI-nätverk kan t.ex. behöva fragmenteras innan det skickas över ett Ethernet-segment.



![Image](assets/fr/008.webp)



Fragmenteringsprocessen fungerar på följande sätt:


- Routern delar upp datagrammet i fragment som inte är större än målnätverkets MTU.
- Storleken på varje fragment är en multipel av 8 byte, eftersom IP-protokollet använder denna enhet för att koda offset för återmontering.
- Varje fragment får en egen IP-rubrik, som innehåller den information som slutmottagaren behöver för att sätta ihop dem i rätt ordning.


När de har fragmenterats färdas delarna oberoende av varandra genom nätverket. De kan ta olika vägar beroende på routingtabeller, länkbelastningar eller avbrott. Det finns ingen garanti för att de kommer fram i den ordning de skickades.


Vid ankomst hanterar den mottagande maskinen **reassembly**. Med hjälp av informationen i headern (delad identifierare, offset och fragmenteringsflaggor) sätter den tillbaka fragmenten i rätt ordning för att rekonstruera det ursprungliga datagrammet innan det sänds till nästa Layer. Om ett enda fragment förloras eller skadas kasseras vanligtvis hela datagrammet, eftersom resultatet utan varje del skulle bli ofullständigt eller oanvändbart.


Även om fragmentering och återmontering är effektiva finns det nackdelar: extra bearbetning för routrar och värdar och en större risk för paketförlust, vilket kan öka antalet återsändningar. Det är därför som noggrann MTU-hantering och optimering av paketstorleken är viktigt för smidig och effektiv IP-kommunikation.



### Inkapsling av data


För att säkerställa att data dirigeras korrekt genom lagren i TCP/IP-modellen spelar processen med **inkapsling** en viktig roll. Vid varje steg som ett meddelande färdas från avsändarens applikation till mottagarens maskin läggs extra information, så kallade headers, till. Dessa headers ger mellanliggande enheter och programlager de instruktioner de behöver för att bearbeta, leverera och, om nödvändigt, återmontera data.


När ett meddelande skickas passerar det genom de fyra lagren i TCP/IP-stacken. Vid varje Layer läggs en ny header till framför den befintliga datan: varje header innehåller specifika metadata, t.ex. logiska eller fysiska adresser, kommunikationsportar, sekvensnummer, felkontrollflaggor och all information som behövs för att hantera överföring och routing.


Överföringen följer således en strukturerad process:


- Applikationen Layer skapar det första **meddelandet**, som innehåller rådata.
- Transport Layer kapslar in den i ett **segment** och lägger till käll- och destinationsportar, sekvensnummer och mekanismer för flödeskontroll.
- Internet Layer lägger till en IP-rubrik till segmentet för att bilda ett **datagram**, som anger käll- och destinations-IP-adresser.
- Network Access Layer packar in datagrammet i en **ram** och lägger till MAC-adresser och CRC-koder (integrity check codes).



![Image](assets/fr/009.webp)



Denna inkapslingsprocess säkerställer både datans integritet och spårbarhet samt dess anpassningsförmåga: när den flyttas från ett nätverk till ett annat förser rubrikerna enheterna med den information som behövs för att välja väg, kontrollera giltigheten eller utföra fragmentering vid behov.


Vid ankomsten är processen omvänd: den mottagande maskinen får ramen i Network Access Layer, som läser och tar bort motsvarande header. Datagrammet skickas sedan till Internet Layer, som läser IP-huvudet och tar bort det i sin tur för att leverera segmentet till Transport Layer. Transport Layer bearbetar transportrubrikerna, kontrollerar strömmens integritet och levererar slutligen **meddelandet** till målapplikationen i sitt ursprungliga tillstånd.



![Image](assets/fr/010.webp)



Omvandlingen av data vid varje Layer kan sammanfattas enligt följande:


- Meddelande**: informationsblock i applikationen Layer.
- Segment**: dataenhet efter inkapsling av Transport Layer.
- Datagram**: form efter det att IP-huvudet lagts till av Internet Layer.
- Frame**: slutligt block som är klart för överföring över det fysiska mediet av Network Access Layer.



![Image](assets/fr/011.webp)



Denna process, som är nödvändig för att Internetkommunikationen ska vara tillförlitlig och universell, säkerställer att alla data, oavsett hur fragmenterade eller komplexa de är, kan transporteras från början till slut och samtidigt vara begripliga och användbara för den mottagande maskinen.



### IP-adressering


Även med paketväxling, fragmentering och inkapsling på plats kan ett nätverk fortfarande inte fungera utan ett tillförlitligt adresseringssystem. För att säkerställa att varje datapaket når rätt mottagare använder Internet Layer en unik identifierare: **IP Address**.

I IPv4 är en IP Address kodad på **32 bitar** och skrivs som fyra decimaltal åtskilda av punkter, i det välkända N1.N2.N3.N4-formatet (till exempel: 192.168.1.12).


En IP Address består av två delar:


- _netid_**: identifierar det nätverk som värden tillhör
- _hostid_**: identifierar den specifika värden inom det nätverket

Denna uppdelning gör att det globala Internet kan struktureras logiskt i många sammankopplade nätverk.


Historiskt sett har IPv4-systemet förlitat sig på ett klassbaserat system, märkt från A till E, som definierade Address:s räckvidd och deras avsedda användning. Varje klass tilldelade ett visst antal bitar till _netid_ och _hostid_, vilket direkt påverkade det möjliga antalet nätverk och värddatorer.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Värdena kan inte tilldelas alla möjliga värden. I en **klass C** Address erbjuder till exempel den sista byten 8 bitar (256 värden). Men två av dessa är reserverade:


- 0: identifierar själva nätverket
- 255: är **broadcast** Address, som används för att skicka ett paket till alla värdar i nätverket på en gång.

Det ger 254 användbara adresser för enheter.


Antalet tillgängliga adresser varierar stort mellan klasserna: från stora publika nätverk i klass A, till företagsnätverk i klass B, till mindre lokala nätverk i klass C.



![Image](assets/fr/013.webp)



Vissa Address-områden är reserverade för privat bruk och dirigeras aldrig direkt på Internet. Dessa kallas **privata adresser** och används inom organisationer, företag eller hem och kräver Address-översättning, vanligtvis NAT (*Network Address Translation*), för att nå det publika Internet. Dessa är:


- Klass A**: från 10.0.0.0 till 10.255.255.255
- Klass B**: från 172.16.0.0 till 172.31.255.255
- Klass C**: från 192.168.0.0 till 192.168.255.255


När en enhet med en privat Address får åtkomst till Internet ersätts den av en NAT-aktiverad router eller gateway med en giltig publik Address.


Exempel: Om en värd har Address **192.168.7.5** kan vi dra slutsatsen:


- 192.168.7.0: nätverk Address
- 192.168.7.1: ofta den lokala routern
- 192.168.7.5: värden själv


Ett annat specialfall är **127.0.0.1**, känt som "***loopback***".

På Linux-system är den associerad med Interface **lo**. Denna Address gör det möjligt för en maskin att Address sig själv för lokal testning eller diagnostik, utan att gå igenom en fysisk Interface. Hela intervallet **127.0.0.0/8** är reserverat för detta ändamål.


För att optimera användningen av Address och utforma komplexa nätverk är **subnätmasken** (_nätmask_) viktig. Denna binära mask separerar _netid_ från _hostid_ i en IP Address.

Varje klass har en standardmask:


- 255.0,0,0** för klass A,
- 255.255.0.0** för klass B,
- 255.255.255.0** för klass C.


En bra nätverksdesign följer en grundläggande regel: enheter som måste kommunicera direkt bör vara i samma nätverk eller subnät. För att segmentera ett nätverk använder vi subnetting, vilket innebär att vi delar upp ett nätverk i mindre subnät med hjälp av en mer specifik mask.


Exempel på subnätverk:

Ett nätverk av **klass C**: 192.168.1.0/24 med en standardmask på 255.255.255.0.

Vi vill ha 4 subnät med upp till 60 värdar vardera.


**Steg 1**: Antal adresser som behövs per subnät = 60 + 2 reserverade adresser (nätverk + broadcast) = 62.


**Steg 2**: Hitta närmaste potens av 2 ≥ 62. -> 2⁶ = 64.


**Steg 3: Justera masken. Behåll _netid_-bitarna och reservera de nödvändiga _hostid_-bitarna. Vi får en binär mask som, efter konvertering, ger **255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Steg 4**: Beräkna Address-intervallen för varje subnät och variera de bitar som är reserverade för värden.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Steg 5**: Detta skapar fyra undernätverk, vart och ett med stöd för upp till 62 maskiner, samtidigt som det övergripande adresseringsschemat förblir effektivt. Delen _hostid_ delas upp i en del med _subnetid_ och en del med värd.



![Image](assets/fr/016.webp)



Denna grundläggande princip för subnetting är fortfarande oumbärlig i modern nätverksteknik och möjliggör exakt IP-allokering, bättre trafikstyrning, stark segmentisolering och skalbar nätverkshantering.



### CIDR-adressering


I början av 1990-talet, när Internet spreds snabbt bland företag och organisationer, började det traditionella IP-adresseringssystemet baserat på klasser (A, B, C) att visa sina begränsningar.

Dess rigida struktur ledde till ett betydande slöseri med IP-adresser och gjorde routingtabellerna allt större, mer komplexa och svåra att underhålla.

För att Address dessa problem infördes en mer flexibel och effektiv metod: **CIDR** (_Classless Inter-Domain Routing_). CIDR har gradvis blivit standard och har till stor del ersatt det gamla klassbaserade systemet.


Kärnidén bakom CIDR är möjligheten att gruppera flera angränsande nätverk, särskilt klass C-block, till en enda logisk enhet som kallas **supernet** (_supernet_). Med denna aggregering kan en enda post i routingtabellen representera flera undernätverk, vilket minskar antalet rutter som routrarna behöver hantera och förbättrar deras prestanda.


Medan klass C-nätverk ursprungligen hade det största behovet av aggregering på grund av sin mindre kapacitet, har principen också tillämpats på klass B-nätverk och, i teorin, även klass A-nätverk, även om de senare är mindre drabbade tack vare sitt stora Address-område.


Med CIDR försvinner konceptet med fasta klasser. Address-utrymmet behandlas som ett kontinuerligt intervall som kan delas upp eller aggregeras efter behov. CIDR-block definieras med hjälp av subnätmasker som inte är begränsade till standardvärdena för A-, B- eller C-klasser. Ett CIDR-block kan representera antingen ett enda nätverk eller en sammanhängande uppsättning undernätverk som delar samma prefix.


Ett CIDR-block skrivs i formatet "Address/prefix", där siffran efter snedstrecket anger hur många bitar som utgör nätverksdelen. Till exempel innebär /17 att de första 17 bitarna identifierar nätverket, medan de återstående 15 bitarna identifierar värdar.


Exempel:

Ett /17-block innehåller 2^(32-17) adresser, så 2^15 = 32 768 adresser totalt. Om man drar ifrån de två reserverade adresserna (nätverk och broadcast) återstår 32.766 användbara värdadresser. Detta gör att nätverksadministratörer kan dimensionera sina subnät exakt efter verkliga behov och undvika onödigt slöseri.


För att göra CIDR-storleken lättare att förstå finns här en tabell över vanliga prefix och deras motsvarande subnätmasker och användbara adresser:


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


**ANMÄRKNING**: Historiskt sett har RFC 950 avrått från användning av subnät noll, främst för att undvika förvirring vid routning.  Denna begränsning blev föråldrad med RFC 1878, som tillåter användning fullt ut. Den gamla begränsningen berodde mest på att den inte var kompatibel med äldre maskinvara som inte kunde hantera CIDR korrekt. Modern utrustning har inga sådana problem.


Till exempel är subnätet **1.0.0.0** med subnätmasken **255.255.0.0**, som tidigare var tvetydigt med klass A-nätverksidentifieraren, nu helt giltigt och användbart.


**TIPS**: För felfria subnätberäkningar och snabb konvertering av adresser till CIDR-notation finns det praktiska verktyg som ***ipcalc***. Denna "nätverkskalkylator" visar tydligt Address-uppdelningar, tillgängliga intervall och tillhörande masker, perfekt för både administratörer och studenter som lär sig CIDR.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## TCP-protokollet


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



Protokollet **TCP** (_Transmission Control Protocol_) spelar en central roll i TCP/IP-modellens TRANSPORT Layer. Det fungerar som en brygga mellan applikationer och Internet Layer och säkerställer en tillförlitlig överföring av data mellan två avlägsna maskiner.

Medan IP-protokollet helt enkelt skickar paket utan att garantera leverans eller ordning, säkerställer TCP integriteten och konsekvensen i dataflödet genom att leverera det utan förluster, i rätt ordning och utan dubbletter.


TCP:s huvudsakliga ansvarsområden omfattar:


- Omordning av mottagna segment;
- Övervakning av dataflödet för att undvika överbelastning;
- Dela upp eller sätta ihop datablock till lämpliga enheter (segment);
- Hantering av upprättande och avslutande av anslutningar mellan kommunikationens båda ändar.


TCP är ett anslutningsorienterat protokoll, vilket innebär att det upprättar en explicit, pågående relation mellan klient och server. För att göra detta används **sekvensnummer** och **bekräftelser**: för varje segment som skickas tilldelas en unik identifierare så att den mottagande maskinen kan kontrollera både ordningen och integriteten hos data. Mottagaren returnerar sedan ett bekräftelsesegment med **ACK-flaggan** satt till 1, vilket bekräftar mottagandet och anger nästa förväntade sekvensnummer.



![Image](assets/fr/018.webp)



För att förbättra tillförlitligheten använder TCP en timer: när ett segment har skickats startar en nedräkning. Om ingen bekräftelse anländer inom timeout-perioden återsänder avsändaren automatiskt segmentet, förutsatt att det förlorades under transporten. Denna automatiska återsändningsmekanism kompenserar för de förluster som finns i IP-nätverk och som kan uppstå vid överbelastning, fel i routningen eller maskinvarufel.



![Image](assets/fr/019.webp)



TCP kan upptäcka och hantera duplikat. Om ett återsänt segment anländer men originalet också dyker upp, använder mottagaren sekvensnumren för att identifiera duplikatet och bara behålla den korrekta kopian, vilket eliminerar alla tvetydigheter.


För att denna process ska fungera måste båda maskinerna ha en gemensam förståelse för sina initiala sekvensnummer. Detta säkerställs genom att följa ett strikt anslutningsförfarande: å ena sidan lyssnar **servern** på en specifik port och väntar på en inkommande begäran (passivt läge); å andra sidan initierar **klienten** aktivt anslutningen genom att skicka en begäran till servern på samma serviceport.


**ANMÄRKNING**: En "port" är en numerisk identifierare (från 0 till 65 535) som tilldelas en nätverksapplikation på en dator. Den används för att särskilja flera tjänster som körs samtidigt på samma IP Address. När en klient skickar data anger den portnumret så att serverns operativsystem vet vilket program som ska ta emot det (t.ex. 80 för HTTP, 443 för HTTPS, 25 för SMTP). Portar fungerar som dedikerade dörrar som leder trafik in och ut, förhindrar förväxling mellan tjänster och möjliggör finkornig åtkomstkontroll genom brandväggar eller filtreringsregler.


Sekvenssynkroniseringen Exchange baseras på den berömda mekanismen **"*trevägshandskakning*"**, som liknar det sätt på vilket två personer hälsar på varandra för att etablera kontakt. Denna initialiseringsfas, som säkerställer TCP:s tillförlitlighet, sker i 3 steg:

1. **SYN:** Klienten sänder ett första synkroniseringssegment (**SYN**) med lämplig flagga inställd och ett första sekvensnummer (t.ex. C);

2. **SYN-ACK:** Den mottagande servern svarar med ett bekräftelsesegment (**SYN-ACK**), där den bekräftar klientens sekvensnummer och anger sitt eget initiala sekvensnummer;

3. **ACK:** Klienten skickar en slutlig bekräftelse (**ACK**) som bekräftar mottagandet av serverns sekvensnummer och avslutar synkroniseringen. SYN-flaggan är nu inaktiverad och ACK-flaggan förblir aktiverad, vilket indikerar att anslutningen är upprättad.



![Image](assets/fr/020.webp)



Exchange-protokollet säkerställer att båda parter har samma numreringsbas innan nyttodata överförs. När denna synkronisering är klar öppnas sessionen: segment kan nu färdas i båda riktningarna, var och en bekräftad vid mottagandet, vilket säkerställer maximal tillförlitlighet i dataflödet.


Denna ***trevägshandskakning*** gäller endast för upprättande av anslutning. För att stänga använder TCP en *fyravägs handskakning*: FIN → ACK → FIN → ACK, vilket garanterar att inget segment i transit går förlorat innan anslutningen är helt släppt.


Även om denna process har utformats för att vara robust och tillförlitlig har den också gett upphov till sårbarheter som kan utnyttjas. Exempelvis syftar attacker som **IP Spoofing** till att kringgå eller korrumpera detta förtroendeförhållande genom att utge sig för att vara en auktoriserad maskin med hjälp av förfalskade sekvensnummer, vilket skapar ett intrång som gör det möjligt att avlyssna eller manipulera dataflödet.


För att begränsa riskerna för kapning av sekvenssynkronisering och för att hantera belastningen på nätverket använder TCP-protokollet en teknik för flödeshantering som kallas "**_Sliding Window_**". Detta system reglerar hur mycket data som kan skickas utan att det krävs en omedelbar bekräftelse för varje segment, vilket minskar onödig överbelastning på nätverket samtidigt som tillförlitligheten bibehålls.


I praktiken definierar det glidande fönstret ett intervall av sekvensnummer som kan cirkulera fritt mellan sändare och mottagare utan att varje enskilt segment bekräftas. När bekräftelser tas emot av det sändande systemet "glider" fönstret: det glider åt höger och gör plats för nya segment som kan sändas. Storleken på detta fönster (som är avgörande för att optimera genomströmningen och samtidigt undvika överbelastning) anges i fältet "*Window*" i TCP-headern.


**Exempel**: Om det ursprungliga sekvensnumret är 3 och fönstret sträcker sig till sekvens 5, kan segment numrerade 3 till 5 skickas utan att vänta på individuella bekräftelser.



![Image](assets/fr/021.webp)



Storleken på det glidande fönstret är inte fast, utan anpassas dynamiskt till nätverksförhållandena och mottagarens bearbetningskapacitet.  Om mottagaren kan hantera en större mängd data anger den detta i fältet Window, varvid avsändaren uppmanas att utöka sitt fönster. Omvänt kan mottagaren vid överbelastning eller risk för mättnad begära en minskning, varvid avsändaren väntar med att skicka ytterligare segment tills fönstret flyttas framåt.


Protokollet tillhandahåller en symmetrisk procedur för att stänga en TCP-anslutning för att säkerställa en ren och ordnad avstängning. Båda maskinerna kan initiera stängningen genom att skicka ett segment med flaggan **FIN** inställd på 1, vilket signalerar att man avser att avsluta kommunikationen. Den väntar sedan tills alla segment i transit har tagits emot och ignorerar all ytterligare data.


När den andra maskinen har tagit emot detta segment skickar den en bekräftelse, också den markerad med FIN-flaggan. Den avslutar sedan sändningen av eventuella återstående data innan den lokala applikationen informeras om att anslutningen har stängts. Denna dubbla bekräftelse säkerställer en ordnad nedstängning och minimerar risken för dataförlust.


Denna exakta hantering, som kombinerar IP:s flexibla routing med TCP:s strikta kontroll, illustreras ofta med ett diagram som kontrasterar hastigheten hos IP-protokollet (som arbetar på **"best effort"**-basis, utan någon garanti för leverans) mot tillförlitligheten hos TCP-protokollet (som hanterar överföringen genom bekräftelser och förhandlade sekvenser).



![Image](assets/fr/022.webp)



I vissa fall är det dock inte absolut tillförlitlighet som prioriteras, utan hastighet och enkelhet. Det gäller t.ex. applikationer som livestreaming eller VoIP, där man kan tolerera en viss paketförlust utan att det påverkar användarupplevelsen allvarligt. I sådana fall är **UDP** (_User Datagram Protocol_) att föredra.


UDP fungerar på ett helt annat sätt än TCP: det är **kopplingslöst**, vilket innebär att ingen tidigare relation upprättas mellan avsändare och mottagare. När en maskin skickar paket via UDP överförs de i en riktning; mottagaren skickar inga bekräftelser och avsändaren har ingen bekräftelse på att meddelandet har kommit fram. UDP-rubriken är avsiktligt minimal och innehåller endast källport, destinationsport, segmentlängd och en kontrollsumma, utan någon inbyggd mekanism för bekräftelse eller tillståndskontroll. Som alltid bärs IP-adresser av det underliggande IP-huvudet.


En vanlig analogi är att TCP är som ett **telefonsamtal**, där en krets upprättas, följs och kontrolleras under hela samtalet. Medan UDP-protokollet är som att **posta ett brev**, där avsändaren stoppar in ett brev i en brevlåda utan något omedelbart bevis på leverans eller systematisk återkoppling.


Denna komplementaritet mellan TCP och UDP gör det möjligt för moderna nätverk att anpassa sig till en mängd olika behov, välja maximal tillförlitlighet eller prioritera hastighet, beroende på applikation.



## Primitiva tjänster


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Skiktad arkitektur och Exchange-organisation


Som vi har sett är **tjänster** den konkreta implementeringen av de protokoll som vi har beskrivit hittills. Även om TCP/IP-modellen skiljer sig från **OSI**-modellen, använder den samma skiktade strategi: varje Layer är utformad för att utföra en specifik funktion och för att tillhandahålla **tjänster** till Layer direkt ovanför den, vilket resulterar i en modulär, robust och lätt underhållbar arkitektur.


Varje Layer bygger på kapaciteten hos den som ligger under den, och ger i sin tur Layer ovanför en konsekvent Interface för hantering av data. I den här arkitekturen har varje Layer sina egna **datastrukturer**, som är noggrant definierade för att säkerställa perfekt kompatibilitet med de andra lagren. Denna kompatibilitet är avgörande för en smidig, tillförlitlig och tydlig kommunikation från en slutpunkt till en annan.


Två viktiga aspekter styr dessa utbyten:


- Vertikal aspekt**: förhållandet mellan en Layer och den som ligger ovanför eller under den (från Layer N till Layer N+1 och vice versa).



![Image](assets/fr/023.webp)




- Horisontell aspekt**: interaktionen mellan fjärrapplikationer, dvs. dialogen mellan en **klient** och en **server**, i båda riktningarna.



![Image](assets/fr/024.webp)



Den skiktade arkitekturen följer principen att varje Layer endast bearbetar den information som ligger inom dess räckvidd: datastrukturer, rubriker och kontrollmekanismer varierar från en Layer till en annan, men tillsammans bildar de ett sammanhängande system som säkerställer att data gradvis dirigeras till sin slutdestination.


**Påminnelse**: Specifik terminologi används för att beskriva de dataenheter som utbyts mellan skikten:


- meddelande** för applikationen Layer,
- segment** för Transport Layer (TCP),
- datagram** för Internet Layer (IP),
- ram** för nätverksåtkomst Layer.


I tabellen nedan sammanfattas termerna för TCP- och UDP-kontexter:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Tjänsteprimitiver och dataenheter


Kärnan i detta system är **tjänstprimitiver**, som fungerar som kommunikationsgränssnitt. Dessa primitiver fungerar som servicedeskar, lyssnar på reserverade specifika **portar** och gör det möjligt för processer att upprätta, underhålla och avsluta nätverksanslutningar på ett kontrollerat sätt. Medan protokollen organiserar formatet och överföringen av data över nätverket, är det **tjänsterna och deras primitiver** som utgör den vertikala länken mellan lagren.


Genom att kombinera den horisontella aspekten (kommunikation mellan distribuerade applikationer) med den vertikala aspekten (interna interaktioner mellan lager) ger TCP/IP-modellen en komplett och skalbar arkitektur. Genom att överlappa dessa två perspektiv får man en tydlig överblick över hur data utbyts i strukturerad nätverkskommunikation.



![Image](assets/fr/026.webp)



### Del sammanfattning


I detta första stora avsnitt har vi utforskat den grundläggande arkitektur som styr konfigurationen och driften av dagens internetanslutna nätverk. Denna arkitektur bygger på en **fyra-Layer-modell**, inspirerad av OSI-modellen, och är uppbyggd kring protokollsviten **TCP/IP**, som är ryggraden i modern kommunikation. Vi såg att TCP, med sin anslutningsorienterade metod, säkerställer tillförlitliga överföringar, medan UDP, som är lättare och snabbare, är att föredra när hastigheten är viktigare än tillförlitligheten.


För att denna modell ska fungera korrekt krävs att protokoll implementeras genom **tjänstprimitiver**. Dessa säkerställer länken mellan lagren och gör det möjligt att anpassa databehandlingen till de specifika kraven på varje nivå, från transport till applikation, inklusive Internet och nätverksåtkomst. Detta modulära tillvägagångssätt gör systemet både flexibelt och robust.


IP-adressering är en annan hörnsten i denna infrastruktur. Varje ansluten enhet identifieras av en **unik IP Address**, som hämtas från ett Address-utrymme som är organiserat i **klasser** (från A till E). Vissa av dessa adresser är reserverade för speciella ändamål, t.ex. lokal loopback eller multicast, medan andra, s.k. "privata adresser", inte dirigeras över Internet utan översättning (NAT). Denna klassificering möjliggör en logisk, hierarkisk organisation av nätverk.


Vi har också tittat närmare på begreppet **subnät**, som gör det möjligt att dela upp ett nätverk i segment för att bättre hantera IP-resurser och optimera dataflödet. Manuell indelning med hjälp av subnätmasker är fortfarande en viktig princip, men den har till stor del moderniserats tack vare **CIDR** (_Classless Inter-Domain Routing_). Den här metoden har förändrat Address-hanteringen genom att möjliggöra en mer flexibel och rationell allokering av IP-intervall, samtidigt som storleken på routingtabellerna har minskat.


Genom att behärska dessa begrepp - lager, protokoll, serviceprimitiver, adressering och subnät - får du en solid grund för att förstå hur moderna nätverk fungerar tekniskt och för att effektivt konfigurera en nätverksinfrastruktur så att den uppfyller dagens behov.


I nästa avsnitt tar vi en närmare titt på IPv4-adressering.



# IPv4-adressering


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Använda IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



I det här avsnittet kommer vi att gå djupare och titta på hur **IPv4**-adresser faktiskt implementeras i ett verkligt nätverk. Vi går igenom deras format, logiken bakom dem och hur de hänger ihop med andra viktiga Elements-nätverk som **DNS-namn**, **MAC-adresser**, **subnätverk** och **översättningstekniker**.


En IP Address är en unik numerisk identifierare som tilldelas varje **nätverk Interface** på en enhet. Den gör det möjligt att lokalisera enheten i ett nätverk och nå den för att överföra data. Till exempel har en router, server, arbetsstation, nätverksskrivare eller till och med en övervakningskamera minst en egen IP Address. IP Address möjliggör **routing**, dvs. att flytta paket från punkt A till punkt B, även om de fysiskt ligger långt ifrån varandra.


IP-adresser kan tilldelas på två huvudsakliga sätt:


- Statisk**: Ställs in manuellt på enheten.
- Dynamisk**: Tilldelas automatiskt på begäran av en DHCP-server (_Dynamic Host Configuration Protocol_). DHCP förenklar nätverkshanteringen genom att eliminera behovet av manuell konfiguration och samtidigt möjliggöra exakt kontroll genom reservationer och leasingperioder.


**IPv4**-adresser skrivs i ett **32-bitars** format uppdelat i **fyra byte**. Varje byte innehåller 8 bitar och representerar ett decimaltal från 0 till 255. De 4 bytena separeras med punkter för att bilda en tydlig, läsbar notation.


exempel: Address 172.16.254.1



![Image](assets/fr/027.webp)



Varje bit i en byte har ett värde (eller "vikt"): den vänstra biten (den mest signifikanta biten) är värd 128, nästa 64, sedan 32, 16, 8, 4, 2 och 1 för den högra biten (den minst signifikanta biten). På detta sätt omvandlas binär skrivning till decimal genom enkel addition av de inställda vikterna.


Tabellen nedan illustrerar denna korrespondens:



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

För att konvertera binär till decimal adderas vikterna för de bitar som är satta till 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

En IP Address identifierar en enda **nätverks-Interface**, inte hela enheten. En router eller brandvägg med flera portar har flera gränssnitt, vart och ett med sin egen IP Address. En Interface kan till och med ha flera IP-adresser (t.ex. för att betjäna flera virtuella nätverk eller tjänster).


Varje IP-paket innehåller två IP-adresser i sitt huvud:


- Källan Address (**avsändare**)
- Destinationen Address (**mottagare**)

Routrarna läser av adresserna för att räkna ut den bästa vägen att skicka paketet tills det når destinationen. Utan strikta adresseringsregler skulle nätverkstrafiken inte kunna dirigeras korrekt och det skulle vara omöjligt att koppla samman nätverken globalt.


En IPv4 Address består av två delar:


- NetID**: identifierar nätverket
- HostID**: identifierar en enhet inom det nätverket

**Subnätmasken** avgör var NetID slutar och HostID börjar och anger hur många bitar som hör till varje del. Ju längre NetID, desto fler möjliga subnät, men antalet hosts per subnät minskar i motsvarande grad.


Ursprungligen var IPv4-nätverk indelade i fem **klasser**: (A, B, C, D och E). Varje klass motsvarar ett specifikt NetID-område och definierar en fast granularitet:


- Klass A: mycket stora nätverk med ett stort antal hosts
- Klass B: medelstora nät
- Klass C: små nät
- Klass D: adresser reserverade för multicasting (_multicast_)
- Klass E: experimentella adresser, används inte för konventionell adressering



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Särskilda adresser:


- Nätverk Address**: Identifierar själva nätverket (används i routningstabeller).
- Broadcast Address**: Skickar data till alla enheter i subnätet på en gång (alla HostID-bitar satta till 1).


Följande intervall är reserverade för internt bruk:


- 10.0,0,0/8** (Privat klass A)
- 127.0.0.0/8** (lokal loopback eller _loopback_)
- 172.16.0.0 till 172.31.255.255** (privat klass B)
- 192.168.0.0 till 192.168.255.255** (privat klass C)


Adresserna **127.0.0.1** och, mer allmänt, hela 127.0.0.0/8-intervallet används för interna tester: en förfrågan som skickas till den lämnar aldrig maskinen. Detta är användbart för att kontrollera att en lokal nätverkstjänst fungerar utan att involvera det större nätverket.


För att utnyttja Address-utrymmet bättre delar administratörer ofta upp nätverk i **subnät** med hjälp av subnätmasker eller **CIDR**-notation (_Classless Inter-Domain Routing_). CIDR möjliggör en mer exakt hantering och hjälper till att undvika slöseri med adresser. I dag är CIDR viktigt för att finjustera IP-intervall och minska storleken på routingtabeller.


I moderna nätverk kombineras IP-adressering vanligtvis med andra identifierare:



- domännamn** som registrerats i ett **DNS** (_Domain Name System_): Det associerar en numerisk IP Address med ett människovänligt namn.
- MAC Address**: en fysisk identifierare som är inristad i nätverkskortet och som används för lokal transport (_Ethernet_). När ett IP-paket behöver överföras fysiskt matchar ARP-tabellen IP Address med MAC Address för destinationen.


För att hantera bristen på IPv4 Address och för att lägga till en Layer säkerhet använder nätverk ofta Address-översättning (_NAT_). NAT gör det möjligt för många privata enheter att dela en enda offentlig IP Address vid åtkomst till Internet.


**Anmärkning**: Onlineverktyg och inbyggda OS-verktyg, t.ex. [Grenoble CRIC calculator] (http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), gör det mycket enklare att beräkna subnät och masker.

Dessa verktyg hjälper till att planera nätverksdelning på ett effektivt sätt.


Sammanfattningsvis är broadcast Address fortfarande en praktisk funktion för att skicka samma meddelande till alla enheter som är anslutna till ett segment: detta uppnås genom att alla bitar i HostID-delen sätts till 1 så att alla värdar blir målgrupp.



## De olika typerna av IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



IPv4-adresser delas in i två huvudkategorier: publika adresser, som är direkt tillgängliga på Internet, och privata adresser, som är avsedda för internt bruk i ett lokalt nätverk.


En publik IPv4 Address är globalt unik och kan routas över internet. Den tilldelas av officiella myndigheter och krävs för tjänster som vänder sig till allmänheten, t.ex. webbplatser, e-postservrar eller molninfrastruktur.

Att dessa adresser är unika över hela världen är viktigt för att undvika konflikter eller kollisioner i routningen.


**IANA** (_Internet Assigned Numbers Authority_), som lyder under **ICANN** (_Internet Corporation for Assigned Names and Numbers_), sköter fördelningen av dessa IP-områden. Konkret delar IANA upp IPv4-utrymmet i 256 block av storleken /8, enligt CIDR-notationen. Varje block representerar drygt 16,7 miljoner adresser (2³² / 2⁸).


Dessa unicast Address-block anförtros av IANA till **Regional Internet Registries** (RIRs). Dessa RIR ansvarar för att omfördela adresserna på regional nivå, i enlighet med de verkliga behoven hos accessleverantörer, företag eller förvaltningar. Unicast Address-utrymmet sträcker sig från block **1/8 till 223/8**, med delar som antingen reserveras för speciella ändamål (forskning, dokumentation, testning) eller tilldelas direkt till ett nät eller RIR för omfördelning.


Om du vill kontrollera vem som äger en publik IP Address kan du använda RIR-databaserna med kommandot **whois** eller använda de webbgränssnitt som tillhandahålls av varje register. Dessa verktyg kan användas för att spåra Address tillbaka till den organisation eller leverantör som deklarerade den.


Omvänt finns det privata IPv4-adresser, ett praktiskt svar på bristen på offentliga adresser. Dessa adresser, som inte kan routas på Internet, är reserverade för lokala miljöer: företagsnätverk, LAN i hemmet, datacenter eller datorkluster. De är inte unika i hela världen: många privata nätverk kan återanvända samma IP-intervall utan störningar, så länge de förblir isolerade eller använder en Address-översättningsenhet för nätverk för att komma åt Internet.


För att en enhet med en privat IP Address ska kunna komma åt Internet använder nätverken NAT (Network Address Translation). NAT fungerar genom att dynamiskt ersätta den privata Address med en publik, vilket gör att dussintals (eller till och med hundratals) enheter kan dela en enda publik IP Address. Den här metoden optimerar användningen av IPv4-utrymme och ger också en Layer av säkerhet genom att dölja den interna nätverksstrukturen.


En annan speciell kategori är **ospecificerade** adresser. IPv4-notationen **0.0.0.0** eller dess IPv6-version **::/128** betyder "ingen specifik Address". En sådan Address är ogiltig som Address-destination i nätverket, men den kan användas lokalt av en värd för att ange "alla gränssnitt" eller "ingen Address tilldelad ännu". Detta är vanligt i DHCP-dynamiska Assignment eller för att lyssna på alla servergränssnitt.


IPv6 stöder även privat adressering, men standarden rekommenderar i allmänhet offentlig adressering för att undvika att stapla flera NAT-lager. De **site-local-adresserna** (_site-local_) i blocket **fec0::/10** avskaffades av **RFC 3879** av konsekvens- och säkerhetsskäl. De ersattes med **Unique Local Addresses** (_ULA_) som finns i blocket **fc00::/7**. ULA gör det möjligt att skapa privata IPv6-nätverk med ren intern routing, med hjälp av en slumpmässigt genererad 40-bitars identifierare för att säkerställa lokal unikhet.


IPv4:s uttömning bekräftades officiellt 2011. För att förlänga dess livslängd antog Internetgemenskapen flera strategier:


- Gradvis övergång till **IPv6**
- Utbredd användning av **NAT**
- Strängare tilldelningspolicyer från RIR, vilket kräver exakt motivering och hantering av Address-behov
- Återvinning av oanvända eller frivilligt återlämnade Address-block av företag


Dessa åtgärder visar att IP-adressering inte bara är en teknisk utmaning utan också en fråga om global styrning, som är central för Internets fortsatta expansion.



## DNS, en Address katalog


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Låt oss vara ärliga, människor är inte bra på att memorera långa strängar av siffror, vare sig i binär eller decimal form. Den här utmaningen blir ännu större med IP-adresser, som kan vara komplexa och en enda IP Address kan ibland maskera flera adresser, särskilt när tekniker som NAT eller virtuell hosting är inblandade.


För att göra det enklare använder applikationen Layer ett system som länkar en IP Address till ett logiskt, mänskligt läsbart namn. Detta är rollen för **DNS** (*Domain Name System*), en massiv, hierarkisk, distribuerad katalog som matchar läsbara domännamn till IP-adresser. Systemet bygger på en uppsättning protokoll och tjänster. Den mest använda DNS-serverprogramvaran är **BIND** (_Berkeley Internet Name Domain_), ett programpaket med öppen källkod som refererar till en stor del av Internets DNS-infrastruktur.


Grundtanken bakom DNS är enkel: för varje ansluten tjänst, oavsett om det är en webbplats, e-postserver eller annan nätverkstjänst, finns det en post som mappar ett domännamn till en eller flera IP-adresser. Detta fungerar i två riktningar:


- Forward resolution: översättning av ett namn till en IP Address.
- Omvänd upplösning: hitta det domännamn som är associerat med en viss IP Address.

Detta gör nätverksadresseringen användbar för människor samtidigt som routrarna behåller den precision som krävs för att flytta data på rätt sätt.


Ett domännamn är alltid hierarkiskt uppbyggt, där varje nivå är åtskild av en punkt: det fullständiga namnet kallas **FQDN** (_Fully Qualified Domain Name_). Delen längst till höger är **TLD** (_Top Level Domain_), t.ex. `.com`, `.org` eller `.fr`. Delen längst till vänster anger värden, dvs. den specifika maskin eller tjänst som är kopplad till IP Address.


DNS-systemet är utformat som ett **träd av zoner**. En **zon** är en del av domännamnområdet som hanteras av en viss DNS-server. En enda zon kan innehålla flera **underdomäner**, som i sin tur kan delegeras till andra zoner som hanteras av olika servrar. Administratörer är ansvariga för att underhålla sina zoner: hantera uppdateringar, delegeringar och övergripande hantering.


Denna struktur gör det möjligt att inte bara peka på en huvuddomän (t.ex. `example.com`), utan även finjustera poster för enskilda värdar (`www`, `mail`, `ftp`, etc.). I nätverkens barndom hanterades denna mappning med statiska filer som (`/etc/hosts` på Unix-system), men en sådan metod blev snabbt opraktisk för ett snabbt växande, sammankopplat Internet.


Det är viktigt att förstå att en **DNS-server** endast kan användas i begränsad omfattning. Ett företags interna DNS-server kanske till exempel inte är direkt tillgänglig från Internet. Om denna DNS inte är konfigurerad för att vidarebefordra frågor, eller inte har en betrodd relation med andra servrar, kommer vissa frågor att misslyckas: varken namnet eller IP Address kan då lösas utanför den definierade zonen.


DNS spelar också en roll i routningen av e-post. En **MX**-post (_Mail Exchange_) anger t.ex. de e-postservrar som ansvarar för att ta emot e-post för en viss domän. Dessa poster definierar prioriteringar (viktningsfaktor) och failover-lösningar. Zonfilen för en DNS-server måste innehålla en **SOA**-post (_Start Of Authority_), som anger servern som den officiella informationskällan för zonen.


Tack vare sin hierarkiska, distribuerade struktur är DNS fortfarande en hörnsten i Internet, eftersom användarna kan få tillgång till tjänster via tydliga, minnesvärda domännamn i stället för långa, tekniska IP-adresser.


I nästa kapitel ska vi utforska ett annat grundläggande koncept: **Ethernet-adresser**, även kallade **MAC-adresser**, som säkerställer dataleverans på den fysiska Layer i lokala nätverk.



## Identifiering av Ethernet-adresser och ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definitioner


För att dataroutingprotokollet ska fungera på ett tillförlitligt och konsekvent sätt är en nyckelkomponent nödvändig. Som människor kan vi enkelt identifiera en maskin med dess IP Address eller med dess namn som hämtas via DNS. En maskin måste dock entydigt kunna känna igen destinationsenheten för att leverera paket. För att göra detta förlitar den sig på en specifik maskinvaruidentifierare som används direkt av dess nätverk Interface: MAC Address (_Media Access Control_).


**Notera**: Detta har inget att göra med en "fysisk Address" i minnesarkitekturen. Inom databehandling hänvisar ett fysiskt minne Address till en specifik plats på minnesbussen, i motsats till ett virtuellt Address som hanteras av operativsystemet. En MAC Address är däremot strikt relaterad till nätverkshårdvara.


En MAC Address tilldelas permanent och unikt av den tillverkare som utrustningen är tillverkad av. MAC Address identifierar nätverkskortet på ett otvetydigt sätt, oavsett om det är en dator, smartphone, skrivare eller någon annan ansluten enhet. Till skillnad från en IP Address, som kan ändras dynamiskt (via en DHCP-server eller manuell konfiguration), förblir MAC Address normalt densamma under hela enhetens livstid, såvida den inte ändras avsiktligt.


Varje nätverk Interface, trådbundet eller trådlöst, har sin egen MAC Address. Denna Address används inom datalänken Layer (Layer 2 i OSI-modellen) för att infoga och hantera hårdvaran Address i varje nätverksram som utbyts. Detta kallas ibland för _Ethernet-adressen_ eller _UAA_ (_Universally Administered Address_). Den är standardiserad till en längd av 48 bitar, eller 6 byte, och skrivs i hexadecimal notation, i allmänhet i form av byte åtskilda av `:` eller `-`.


Till exempel: `5A:BC:17:A2:AF:15`


I denna struktur identifierar de tre första bytena nätverkskortets tillverkare: detta kallas **OUI** (*Organisationally Unique Identifier*). Dessa prefix, som tilldelas av IEEE, används också i andra hårdvaruadresseringssystem, t.ex. Bluetooth och LLDP, för att garantera unikhet över hela världen.


### Ändra en MAC Address (MAC-spoofing)


I teorin är MAC Address utformat för att förbli fast, men det finns sätt att modifiera det, särskilt för att tillgodose särskilda behov eller för att kringgå vissa begränsningar. Denna operation, som ofta kallas _spoofing MAC_, innebär att den ursprungliga maskinvaran Address ersätts med ett annat värde, definierat på programvarunivå. Vissa operativsystem underlättar denna modifiering, särskilt när det faktiska Ethernet Address inte används direkt av drivrutinen.


Anledningarna till en sådan förändring är många. Det kan handla om att en viss applikation kräver ett specifikt Ethernet Address för att fungera korrekt, eller att lösa en konflikt med identiska adresser mellan två enheter som delar samma lokala nätverk.


Att ändra MAC Address kan också motiveras av integritetshänsyn: genom att dölja den unika identifieraren som är ingraverad på kortet minskar användarna möjligheten att deras enhet spåras av nätverk eller övervakningstjänster. Denna praxis är dock inte utan konsekvenser. Byte av MAC Address kan störa vissa filtreringsenheter eller kräva att brandväggar konfigureras om för att godkänna den nya hårdvaran.


Vissa nätverk, särskilt Wi-Fi, använder MAC Address-filtrering för att endast tillåta enheter med godkända adresser. Även om detta ger en grundläggande kontrollnivå är det inte säkert i sig självt. En angripare kan fånga en giltig MAC Address som redan är godkänd i nätverket och klona den för att kringgå begränsningar. Av den anledningen bör MAC-filtrering alltid kombineras med starkare säkerhetsåtgärder.


### MAC/IP-korrespondens


För att ett lokalt nätverk ska fungera effektivt måste det finnas en tydlig mappning mellan fysiska adresser (MAC-adresser) och logiska adresser (IP-adresser). Utan den här länken kan en dator känna till IP-adressen Address för en destination men inte veta hur den fysiskt ska skicka data till den i det lokala nätverket.

Denna mappning sköts automatiskt av ARP (_Address Resolution Protocol_).


I praktiken kan en användare som vill veta vilken MAC Address som motsvarar en viss IP Address använda verktyget `arp`. Det här verktyget kontrollerar maskinens lokala ARP-tabell för att visa kända matchningar mellan IP-adresser och MAC-adresser i det lokala nätverket. På så sätt går det snabbt att verifiera den effektiva länken mellan det logiska och det fysiska lagret.


Praktiskt exempel: Om du vill kontrollera vilket nätverkskort som motsvarar IP Address `192.168.1.5` använder du följande kommando:


```bash
arp –a 192.168.1.5
```


Utmatningen visar den tillhörande fysiska Address (MAC), typ av inmatning (statisk eller dynamisk) och den berörda Interface.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Det är viktigt att komma ihåg att MAC Address och IP Address är två helt olika identifierare, men som ändå kompletterar varandra. MAC Address graveras unikt in i varje nätverks-Interface av tillverkaren och används för att fysiskt identifiera enheten i det lokala nätverket. IP Address är å andra sidan en logisk Address som tilldelas antingen dynamiskt eller statiskt, vilket gör att maskinen kan ansluta sig till IP-nätverket och Exchange paket utanför det lokala nätverket.



- Visuellt exempel på MAC Address:


![Image](assets/fr/032.webp)




- Visuellt exempel på en IP Address:


![Image](assets/fr/027.webp)



I en företagsmiljö kan dessa två adresseringsnivåer inte fungera separat. När t.ex. en DHCP-server automatiskt tilldelar en IP Address används utrustningens MAC Address som utgångspunkt. Datorn skickar en DHCP-begäran som innehåller dess MAC Address så att servern kan tilldela en tillgänglig IP Address till rätt enhet. Utan denna maskinvaruidentifiering skulle DHCP-servern inte veta vilken enhet den ska leverera Address till.


ARP-protokollet är därför grundläggande: det utgör länken mellan IP-adresser och fysiska adresser, vilket gör det möjligt för maskiner att översätta en logisk destination till en faktisk fysisk destination. När en dator ska skicka ett paket till en maskin i samma nätverk, konsulterar den först sin ARP-tabell för att kontrollera om mottagarens MAC Address redan är känd. Om inte, sänder den ut en ARP-begäran till alla värdar i det lokala nätverket. Den maskin som känner igen mål-IP Address i denna begäran svarar genom att ange sitt MAC Address. Avsändaren skriver sedan detta IP/MAC-par till sin ARP-cache, för att undvika att behöva upprepa åtgärden varje gång begäran skickas.


Denna ARP-tabell fungerar som en liten mappningskatalog som uppdateras dynamiskt på samma sätt som DNS associerar domännamn med IP-adresser. Utan ARP skulle ingen lokal Exchange vara möjlig, eftersom datalänken Layer måste känna till MAC Address för att kunna kapsla in Ethernet-ramar korrekt.


RARP-protokollet (_Reverse Address Resolution Protocol_) utformades däremot för den motsatta situationen: att göra det möjligt för en maskin som bara känner till sin MAC Address att upptäcka sin IP Address. Detta var ofta fallet för äldre arbetsstationer utan en lokal Hard-disk, som var tvungna att starta över nätverket och begära en IP Address. RARP ersattes så småningom av **BOOTP** och sedan **DHCP**, som är mer flexibla och automatiserade.


Dessa associationsprotokoll spelar en viktig roll vid routning. En router är i princip en maskin med flera nätverksgränssnitt som kopplar samman olika segment. När en router tar emot en ram bearbetar den den för att extrahera IP-datagrammet och undersöker IP-rubriken för att bestämma destinationen. Om destinationen finns i ett direktanslutet nätverk levereras datagrammet direkt efter uppdatering av headern. Om destinationen ligger i ett annat nätverk konsulterar routern sin routingtabell för att identifiera den bästa vägen, eller _next hop_, till destinationen.


Detta delar upp rutten i kortare, mer hanterbara segment. Varje mellanliggande router känner bara till nästa steg, inte nödvändigtvis slutdestinationen.


**Påminnelse:** Direkt leverans sker när avsändare och mottagare befinner sig i samma fysiska nätverk. I annat fall är leveransen indirekt och går via en eller flera routrar.


Routingtabellen, som hanteras antingen manuellt (statisk routing) eller dynamiskt (dynamisk routing), innehåller den information som behövs för att bestämma vilken väg som ska tas. I små nätverk räcker det med en statisk konfiguration. I större infrastrukturer är dynamisk routing nödvändig för att automatiskt justera rutterna när topologin ändras eller en länk går ner.


Routingtabellen fungerar som en mappningstabell mellan mål-IP-adresser och nästa gateway. Den lagrar vanligtvis nätverksidentifierare (_nätverks-ID_) i stället för varje enskild värd Address, vilket minskar dess storlek avsevärt.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Med hjälp av dessa poster kan routern snabbt avgöra genom vilken Interface och till vilken nod varje datagram ska skickas. I kombination med ARP för att lösa de matchande MAC-adresserna säkerställer detta effektiv och tillförlitlig dataöverföring över nätverket.


Slutligen omfattar dynamiska routingprotokoll standarder som RIP (_Routing Information Protocol_), baserat på avståndsalgoritmen, och OSPF (_Open Shortest Path First_), som beräknar de kortaste vägarna i en komplex topologi. Dessa protokoll uppdaterar ständigt Exchange för att optimera rutterna, minska överföringskostnaderna och förbättra motståndskraften mot avbrott eller överbelastning.



## NAT: Address-översättning


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definition


Network Address Translation_ (NAT) är en teknik som utvecklats för att Address den gradvisa uttömningen av tillgängliga IPv4-adresser. NAT utformades som en tillfällig lösning innan IPv6 infördes på bred front och gjorde det möjligt för företag och privatpersoner att fortsätta ansluta ett stort antal maskiner samtidigt som de endast använde en begränsad uppsättning offentliga IP-adresser.


**Viktig påminnelse:** Övergången från IPv4 till IPv6 löser teoretiskt sett utmattningsproblemet genom att Address-utrymmet utökas från 32 bitar till 128 bitar, vilket ger ett nästan obegränsat antal adresser (2^128). I praktiken är dock övergången fortfarande ofullständig, och NAT används fortfarande i stor utsträckning idag.


Principen bakom NAT är enkel men mycket effektiv: istället för att tilldela en unik publik IP Address till varje enhet i det interna nätverket används en enda routningsbar Address (eller en liten pool av adresser) för alla privata enheter. NAT-gatewayen, som ofta är integrerad i routern eller brandväggen, översätter sedan dynamiskt den interna IP Address tillsammans med den information som behövs för att dirigera trafiken korrekt till omvärlden och ser till att svar returneras till den ursprungliga avsändaren.


Detta tillvägagångssätt har en omedelbar fördel: det döljer helt den interna nätverksarkitekturen. För en utomstående betraktare ser alla förfrågningar från arbetsstationer, servrar eller skrivare ut att komma från samma offentliga identitet. Privata adresser, som vanligtvis hämtas från reserverade intervall (t.ex. 192.168.x.x eller 10.x.x.x), förblir osynliga från Internet.


Förutom att hantera IPv4-bristen stärker NAT också säkerheten genom att skapa en första logisk barriär mellan det interna och det publika nätverket. Oönskad inkommande kommunikation blockeras på ett naturligt sätt, eftersom endast anslutningar som initieras inifrån nätverket får den översättning som krävs för att få svar.



![Image](assets/fr/035.webp)



### Översättningstyper


NAT kan implementeras på olika sätt för att passa specifika behov. De två huvudsakliga funktionssätten är statisk översättning och dynamisk översättning.


**Statisk översättning** skapar en fast mappning mellan en privat IP Address och en publik IP Address. Varje intern maskin är permanent kopplad till sin dedikerade publika Address. Till exempel kan en intern enhet som är konfigurerad som 192.168.20.1 associeras med den routningsbara Address 157.54.130.1. När ett utgående paket lämnar det lokala nätverket ersätter routern paketets käll-Address med den publika Address, och utför den omvända operationen för inkommande trafik. Denna dubbelriktade översättning är transparent för användaren.


**Även om den här metoden isolerar det interna nätverket löser den inte bristen på offentliga IP-adresser, eftersom du fortfarande behöver lika många offentliga adresser som det finns maskiner att exponera. Statisk översättning används därför främst när vissa interna resurser måste förbli nåbara från utsidan (webbserver, e-postserver ...).


**Dynamisk översättning** använder å andra sidan en pool av offentliga IP-adresser. När en intern värd startar en anslutning tilldelar routern tillfälligt en av dessa publika adresser till värdens privata Address under hela sessionen. Länken är 1-till-1, men tillfällig: när anslutningen avslutas blir den publika Address tillgänglig för en annan enhet. Dynamisk NAT minskar därför antalet publika adresser som behövs när inte alla maskiner är online samtidigt, men det krävs fortfarande ett block med externa adresser som är minst lika stort som det maximala antalet samtidiga anslutningar.


**Port translation** (PAT), även känd som *NAT overload* eller *IP masquerading*, går ett steg längre: alla privata enheter delar en enda offentlig IP Address (eller ett mycket litet antal). För att särskilja sessioner ändrar gatewayen inte bara källan Address utan även källporten. Den håller en tabell som länkar varje *(privat Address, privat port)*-par till ett unikt *(offentligt Address, offentligt port)*-par. Den här formen av NAT används i nästan alla hemroutrar och gör det möjligt för dussintals enheter (datorer, smartphones, anslutna objekt etc.) att dela samma offentliga IP Address, samtidigt som kommunikationen fungerar smidigt.


NAT förlänger därför IPv4:s livslängd, samtidigt som det tillför en värdefull Layer segmentering och säkerhet. I takt med att IPv6 blir allt vanligare och dess enorma Address-utrymme används i större utsträckning kommer NAT:s roll sannolikt att minska, även om det av kompatibilitets- och kontrollskäl fortfarande kommer att användas i vissa miljöer för att segmentera och filtrera trafik.


### NAT-implementering


För att säkerställa att Address-översättningen fungerar korrekt måste NAT-routern eller gatewayen föra ett noggrant register över de mappningar som upprättas mellan varje privat Address i det interna nätverket och den offentliga Address som används för att kommunicera med omvärlden. Den här informationen lagras i den så kallade "NAT-översättningstabellen", som spelar en central roll i hanteringen av nätverkstrafik.


Varje post i den här tabellen länkar minst ett par: den interna IP Address för den sändande maskinen och den externa IP Address som kommer att exponeras på Internet. När ett paket från det privata nätverket skickas till en offentlig destination fångar NAT-routern upp ramen, analyserar IP- och TCP/UDP-rubrikerna och ersätter sedan den privata källans Address med gatewayens offentliga Address. På returvägen fångar samma gateway upp det inkommande paketet, kontrollerar mappningstabellen och utför den omvända operationen för att omdirigera flödet till den ursprungliga interna IP Address.


Denna dynamiska översättningsprincip bygger på en exakt tabellhantering: varje post förblir giltig så länge det finns aktiv trafik som motiverar den. Efter en konfigurerbar period av inaktivitet rensas posten och kan återanvändas för nya anslutningar.


_Exempel på en förenklad NAT-översättningstabell:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

I det här exemplet markeras den andra posten som återanvändbar om inget paket har passerat på över en timme (3 600 sekunder). Omvänt innebär en varaktighet på noll att kommunikationen är aktiv och att mappningen är låst.


Även om NAT fungerar transparent för de vanligaste användningsområdena (webbsurfning, e-post, filöverföring etc.) kan det skapa ytterligare utmaningar för vissa nätverksapplikationer. Vissa tekniker förlitar sig på att IP-adresser eller portar uttryckligen utbyts i paketets nyttolast. Efter att ha passerat genom en NAT-gateway blir denna information inkonsekvent.


Typiska exempel på begränsningar är:


- Peer-to-peer-protokoll (P2P), som kräver direkta anslutningar mellan enheter, hindras av NAT-barriären, eftersom alla interna maskiner delar samma externa IP Address och inte kan nås direkt utan specifik konfiguration (t.ex. *port forwarding* eller UPnP);
- IPSec-protokollet, som används för att säkra nätverkskommunikation, krypterar pakethuvuden. Eftersom NAT måste ändra dessa rubriker för att ersätta IP-adresser, gör krypteringen detta omöjligt utan anpassningsmekanismer som NAT-T (*NAT Traversal*);
- X Window-protokollet, som möjliggör fjärrvisning av grafiska program på Unix/Linux, fungerar på så sätt att X-servern aktivt skickar TCP-anslutningar till klienter. Denna omvändning av den vanliga anslutningsriktningen kan blockeras av NAT.


I allmänhet kommer alla protokoll som uttryckligen innehåller den interna IP Address i paketets nyttolast att påverkas, eftersom den Address inte längre kommer att matcha den verkliga, på internet synliga Address efter översättning.


**Viktigt att notera:** För att Address dessa problem erbjuder vissa NAT-routrar _Deep Packet Inspection_ (DPI) eller _Protocol Helpers_ , som inspekterar paketinnehållet för att identifiera och dynamiskt ersätta adresser eller portnummer i applikationsdata. Detta kräver djupgående kunskaper om protokollformatet och kan skapa säkerhetsproblem eller öka resursanvändningen.


**Försiktighet:** Även om NAT hjälper till att dölja det interna nätverket och kontrollera inkommande trafik, är det inte en ersättning för en dedikerad brandvägg. Enbart översättning är inte en fullständig säkerhetsbarriär: den måste alltid kompletteras med tydliga filtreringsregler för att blockera oönskad eller oönskad trafik.


för att illustrera hur detta fungerar i praktiken, se följande exempel:_



![Image](assets/fr/037.webp)



I det här scenariot kan en intern arbetsstation komma åt den interna webbservern genom att helt enkelt anropa URL:en `http://192.168.1.20:80`. Att ange porten är valfritt här, eftersom `80` är standard HTTP-port. Om en begäran däremot initieras från utsidan kommer användaren att ange den publika Address `http://85.152.44.14:80`. NAT-routern tar emot begäran, konsulterar sin mappningstabell och översätter automatiskt den publika Address till en privat och omdirigerar anslutningen till `http://192.168.1.20:80`.


Samma princip gäller för alla andra servrar som är auktoriserade att ta emot Internetanslutningar, t.ex. Extranet-servern (blå krets i diagrammet).


**Praktisk anmärkning:** I virtualiserade miljöer används ofta nätverksgränssnitt som kallas _virbrX_ (för _Virtual Bridge X_). Dessa virtuella bryggor, som i synnerhet tillhandahålls av libvirt-biblioteket eller Xen hypervisor, ansluter gästmaskinernas virtuella interna nätverk till det fysiska nätverket samtidigt som NAT tillämpas. De konfigureras i allmänhet via skript i `/etc/sysconfig/network-scripts/`, enligt nedan för `virbr0`:


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


När den virtuella bryggan är på plats måste du aktivera IP-routing och konfigurera portöversättning med `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Med den här konfigurationen routas utgående trafik och NAT-översättning tillämpas, vilket gör att virtuella maskiner kan kommunicera med omvärlden utan att direkt exponera sina interna IP-adresser.


I nästa kapitel tittar vi närmare på konfigurationen av IP Address under Linux och går igenom både enkla och avancerade metoder som passar för olika administrationssammanhang.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Hur konfigurerar jag nätverket med `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Standardkonfiguration


Efter att ha gått igenom de teoretiska grunderna för nätverk och förstått hur IP-adresser, masker, routing och översättning fungerar tillsammans, är det dags att gå vidare till praktisk konfiguration. På GNU/Linux hanteras nätverksinställningar nu med kommandot **`ip`** (paketet _iproute2_), som ersätter det äldre `ifconfig`.


med `ip` kan du tilldela eller ändra en IP Address, ändra en mask, starta eller stoppa en Interface eller kontrollera dess status när som helst.


**TIPS:** för att visa alla gränssnitt (aktiva eller inte): `ip addr show`


Exempel: Tilldelning av en statisk Address och aktivering av Interface


Lägg till Address `192.168.1.2/24` till Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Aktivera Interface:


```shell
ip link set dev eth0 up
```


Avaktivera samma Interface:


```shell
ip link set dev eth0 down
```


Visa status för en specifik Interface:


```shell
ip addr show dev eth2
```


**Praktiskt tips:** med `ip`, att lägga till ytterligare en Address till en Interface kräver inte längre ett `:1` suffix. Lägg bara till en ny rad `ip addr add ...`:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Aktiveringsskript: ifup / ifdown


Verktygen `ifup` och `ifdown` läser statiska konfigurationsfiler från `/etc/sysconfig/network-scripts/` (på RHEL, CentOS, Rocky Linux, AlmaLinux...) eller `/etc/network/interfaces` (på Debian/Ubuntu) för att på ett enkelt sätt sätta upp eller stänga av gränssnitt.


```shell
ifup eth1
ifdown eth2
```


Konfigurationsfiler (RHEL-liknande):


- /etc/sysconfig/network**: globala inställningar (NETWORKING, HOSTNAME, GATEWAY ...).
- ifcfg-**: inställningar som är specifika för varje Interface.


Statiskt exempel (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Exempel på DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Denna modulära struktur är fortfarande giltig och kan enkelt automatiseras i dagens system.


### Avancerad konfiguration: bonding


I professionella miljöer är målet att garantera tjänstekontinuitet och/eller att aggregera bandbredd. *Bonding* (eller *teaming* med _teamd_) mekanismer uppfyller dessa behov: flera fysiska gränssnitt fungerar som en enda logisk Interface, ofta kallad `bond0` eller `team0`.



![Image](assets/fr/039.webp)



Förkunskapskrav:


- Ladda modulen `bonding` (eller använd `teamd`) ;
- Ha minst två fysiska gränssnitt tillgängliga.


#### De olika vanliga metoderna för limning:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Installera med `ip-länk



- Inaktivera fysiska gränssnitt:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Skapa den bundna Interface:


```shell
ip link add bond0 type bond mode balance-alb
```



- Konfigurera alternativ efter skapandet


```shell
ip link set bond0 type bond miimon 100
```



- Tilldela MAC- och IP-adresser:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Anslut slavgränssnitt:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Ta upp allt igen:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Tips:** för att koppla bort en slav utan att ta bort bindningen: `ip link set eth1 nomaster`


#### Permanent konfiguration (RHEL-liknande)


Skapa tre filer i `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_ _ifcfg-bond0


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


Då så:


```shell
systemctl restart network
```


#### Ytterligare IP Address (modernt alias)


Med `ip` kan du helt enkelt lägga till en andra Address till samma enhet:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


För att göra detta alias bestående efter en omstart, lägg antingen till ett andra `IPADDR2=...` / `PREFIX2=...`-block till `ifcfg-eth0`, eller skapa en ny *NetworkManager*-anslutning via `nmcli`.


Tack vare `ip` och relaterade kommandon (`ip link`, `ip addr`, `ip route`) är nätverkskonfigurationen mer konsekvent, skriptbar och tydlig. Bonding är en viktig komponent i arkitekturer med hög tillgänglighet, och det har blivit mycket enklare att tilldela flera adresser till en enda Interface.


I nästa kapitel tittar vi närmare på detaljerna och implementeringen av IPv6-adressering.


# IPv6-adressering


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Standarder och definitioner


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Vi går nu över till nästa generation av IP-adressering: IPv6-protokollet, ursprungligen känt som IPng (_IP Next Generation_). Detta protokoll är utformat för att övervinna de strukturella begränsningarna i IPv4 och introducerar en kraftigt utökad adresseringsarkitektur samt många tekniska optimeringar.


Motiven bakom antagandet av IPv6 är varierande och Address kritiska behov för utvecklingen av Internet. För det första är IPv6:s roll att stödja den exponentiella tillväxten i antalet anslutna enheter (ett mål som är omöjligt att uppnå med IPv4:s begränsade Address utrymme). För det andra syftar protokollet till att minska storleken på routingtabellerna, vilket gör utbyten mer effektiva och minskar arbetsbelastningen för routrar på lång sikt.


IPv6 strävar också efter att förenkla vissa aspekter av pakethanteringen, förbättra datagramflödet och optimera överföringshastigheterna mellan nätverken. Ur säkerhetssynpunkt ingår AH/ESP-huvudena i *IPsec*-protokollet i grundspecifikationen och alla IPv6-noder måste kunna stödja dem (RFC 6434). Användningen av dem är dock fortfarande frivillig: det är upp till administratören att aktivera dem beroende på sammanhanget.


Andra mål är en mer exakt hantering av tjänstetyper, framför allt för att säkerställa bättre kvalitet för realtidstillämpningar (VoIP, videokonferenser etc.). IPv6 är också utformat för att möjliggöra en mer flexibel mobilitetshantering: en enhet kan byta accesspunkt utan att ändra sin Address på ett sätt som är synligt för dess kollegor.


Slutligen har IPv6 utformats för att samexistera med äldre protokoll. Även om det inte är direkt binärt kompatibelt med IPv4, är det fullt kompatibelt med högre Layer-protokoll som TCP, UDP, ICMPv6 och DNS, liksom med routingprotokoll som OSPF och BGP, med vissa justeringar. För multicasthantering använder IPv6 protokollet MLD (*Multicast Listener Discovery*), som är den funktionella motsvarigheten till IGMP i IPv4-miljön.


### Regler för notation


En av de viktigaste förändringarna i IPv6 är formatet på själva IP Address. För att råda bot på den kroniska bristen på IPv4-adresser har längden på Address ökats från 32 bitar till 128 bitar, dvs. 16 byte. I teorin ger detta ett möjligt Address-utrymme på:


$$3,4 gånger 10^{38}$$$


Detta garanterar praktiskt taget obegränsad kapacitet för all nuvarande och framtida utrustning.


IPv6-adresser skrivs på ett helt annat sätt än den välkända punktade decimalnotationen. En IPv6 Address består av åtta 16-bitarsgrupper, skrivna i hexadecimal och åtskilda av kolon `:`.


Till exempel:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


För att förenkla notationen kan inledande nollor i varje grupp utelämnas. Ovanstående exempel blir då:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Dessutom kan en enda kontinuerlig sekvens av nollgrupper ersättas med::, vilket ytterligare förkortar Address:


```
1987:c02:0:84c2::cf2a:9077
```


**Varning:** denna regel är strikt: endast en sekvens av på varandra följande nollor kan ersättas med `::`. Om en Address innehåller flera nollsekvenser, kondenseras endast den längsta. Detta säkerställer både unikhet och läsbarhet.


**Viktig detalj:** Tecknet `:` som används för att separera hexadecimala block kan orsaka tvetydighet i URL:er, eftersom `:` också används för att ange en tjänsteport. För att undvika missförstånd måste IPv6-adresser i URL:er omslutas av hakparenteser `[ ]`.


Exempel på HTTP-åtkomst till en specifik port för Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


När du representerar en IPv4 Address i ett IPv6-sammanhang kan du använda en blandad notation i punktdecimalform, föregången av `::`:


```
::192.168.1.5
```


Denna kompatibilitet underlättar övergången mellan de två protokollen genom att IPv4-block kan inkluderas i IPv6 Address-utrymmet.


**Anmärkning:** För att standardisera hur adresser skrivs definierar RFC 5952 ett kanoniskt format med förkortningsregler för att undvika flera representationer av samma Address. Genom att följa dessa rekommendationer kan du minska risken för feltolkningar och säkerställa konsekventa nätverkskonfigurationer.


### IPv6 Address-typer


IPv6 skiljer sig från sin föregångare genom ett brett utbud av Address-kategorier, var och en utformad för specifika användningsområden, samtidigt som den möjliggör flexibel routing och nätverkshantering. Precis som med IPv4 kan adresser vara globala, lokala, reserverade eller specifika för vissa övergångsmekanismer.


En ospecificerad IPv6 Address representeras av `::` eller, mer explicit, `::0.0.0.0`. Denna speciella form används vid förvärv av Address, eller som ett standardvärde för att ange att det inte finns någon Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *På ett privat LAN är prefixet `fd00::/8` att föredra för tilldelning av interna adresser som inte är routbara på Internet


#### Reserverade adresser


Vissa IPv6-områden är uttryckligen reserverade och får inte användas som globala adresser. De har specifika tekniska syften:


- `::/128`**: ospecificerad Address, aldrig permanent tilldelad till en enhet, men används som en källa Address av en maskin som väntar på konfiguration.
- `::1/128`**: _loopback_ Address, den direkta motsvarigheten till `127.0.0.1` i IPv4, vilket gör att en maskin kan Address sig själv.
- `64:ff9b::/96`**: Reserverad för protokollöversättare för att möjliggöra IPv4/IPv6-sammankoppling, enligt definitionen i RFC 6052.
- `::ffff:0:0/96`**: kompatibilitetsblock för att representera en IPv4 Address i en specifik IPv6-struktur, används ofta internt av applikationer.


Dessa block garanterar interoperabilitet och underlättar migrering mellan de två protokollversionerna.


#### Globala unicast-adresser


Globala unicast-adresser utgör större delen av det allmänt routningsbara IPv6-utrymmet och representerar cirka 1/8 av Address-utrymmet. Sedan 1999 har IANA tilldelat dessa block, t.ex. prefixet `2001::/16`, i CIDR-block (från `/23` till `/12`) till regionala register, som sedan distribuerar dem vidare till leverantörer och organisationer.


Vissa områden har särskilda dokumenterade användningsområden:


- `2001:2::/48`**: Reserverad för prestanda- och interoperabilitetstestning (RFC 5180).
- `2001:db8::/32`**: Reserverad för dokumentation och exempel (RFC 3849).
- `2002::/16`**: Används för 6to4-mekanismen, som gör det möjligt för IPv6-trafik att färdas över en IPv4-infrastruktur (användbart under övergångsfasen mellan de två protokollen).


**En stor del av de globala adresserna förblir oanvända och fungerar som en reserv för framtida tillväxt på Internet.


#### Unika lokala adresser (ULA)


Unika lokala adresser (`fc00::/7`) är IPv6-motsvarigheten till privata IPv4-adresser (RFC1918). De gör det möjligt att skapa isolerade interna nätverk utan att riskera konflikter med offentlig adressering. I praktiken är det effektiva prefixet `fd00::/8`, med den 8:e biten satt till 1 för att indikera lokal användning. Varje ULA-block innehåller en 40-bitars pseudoslumpmässig identifierare, vilket minimerar Address-kollisioner vid anslutning av separata privata nätverk.


#### Länk-lokala adresser


Länk-lokala adresser (`fe80::/64`) används uteslutande för kommunikation inom samma Layer 2 segment (samma VLAN eller switch). De dirigeras aldrig bortom den lokala länken. Varje nätverks-Interface genererar automatiskt en länk-lokal Address, som ofta härleds från dess MAC Address med hjälp av EUI-64-schemat.


**Specialfunktion**: samma maskin kan använda samma länk-lokala Address på flera gränssnitt, men Interface måste anges vid kommunikation för att undvika tvetydighet.


#### Multicast-adresser


I IPv6 har broadcast ersatts av multicast, ett mer effektivt sätt att leverera paket till en definierad grupp av mottagare. Multicast-intervallet inleds med `ff00::/8`. Detta inkluderar adresser som `ff02::1`, som riktar sig till alla noder på den lokala länken. Denna Address är visserligen bekväm, men rekommenderas inte längre för applikationer eftersom den kan generate okontrollerade sändningar.


En vanlig användning av multicast är _Neighbor Discovery Protocol_ (NDP), som ersätter ARP i IPv6. NDP använder specifika multicast-adresser, t.ex. `ff02::1:ff00:0/104`, för att automatiskt upptäcka andra värdar som är anslutna till samma länk.


Genom att kombinera dessa Address-typer ger IPv6 en komplett uppsättning alternativ för att tillgodose behoven av global routing, lokal kommunikation, IPv4/IPv6-migrering och automatisk enhetskonfiguration, samtidigt som överföringseffektiviteten förbättras.


### Address omfattning


Omfattningen av en IPv6 Address definierar den exakta domän inom vilken den är giltig och unik. Att förstå detta koncept är nyckeln till att behärska paketroutning och logisk organisation av ett IPv6-nätverk. IPv6-adresser grupperas i allmänhet i tre huvudkategorier baserat på deras omfattning och användning: unicast, anycast och multicast.


**Unicast-adresser** är de vanligaste och omfattar flera olika undertyper.

Bland annat _loopback_ (`::1`) Address, vars räckvidd är begränsad till den värd som använder den, och som används för att testa nätverksstacken internt utan att skicka trafik över det fysiska nätverket.

Sedan finns det länk-lokala adresser (_link-local_), vars räckvidd är begränsad till ett enda nätverkssegment: de används för direkt kommunikation mellan enheter på samma fysiska eller logiska länk (t.ex. en enda switch eller VLAN).

Slutligen är unika lokala adresser (_ULA_, för _Unique Local Addresses_) interna i ett privat nätverk. De kan dirigeras mellan flera privata segment men är aldrig synliga på Internet.


Konceptuellt representeras IPv6-adresser ofta som en binär struktur där den första halvan (de första 64 bitarna) identifierar nätverksprefixet och den andra halvan (också 64 bitar) unikt identifierar enhetens Interface i det nätverket. Denna uppdelning gör Address autokonfiguration enklare genom mekanismer som SLAAC (_Stateless Address Autoconfiguration_), som gör det möjligt för maskiner att automatiskt generate en stabil Address baserat på MAC Address eller en pseudoslumpmässig identifierare.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

IPv6-arkitekturen följer den hierarkiska globala routingmodellen i dagens Internet. Prefixpartitionering gör det möjligt för regionala register och nätoperatörer att hantera Address-allokering på ett decentraliserat sätt, samtidigt som global unikhet säkerställs. Inom detta ramverk kan samma värd samtidigt inneha en global unicast Address för internetkommunikation och en link-local Address för lokala interaktioner, t.ex. med närmaste grannskap eller för meddelanden om routerupptäckt.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Anycast-adresser** representerar ett mellanliggande koncept som bygger på unicast-modellen men som i vissa fall kan bete sig som multicast. En anycast Address är i själva verket en unicast Address som tilldelats flera gränssnitt fördelade över olika nätverksnoder. När ett paket skickas till en anycast Address strävar IPv6-protokollet efter att leverera det till en av de värdar som delar den Address, vanligtvis den som ligger närmast i fråga om routningstopologi. Detta tillvägagångssätt optimerar hastigheten för frågebearbetning och förbättrar motståndskraften hos distribuerade tjänster. Ett klassiskt exempel är DNS-rotservrarna, där anycast-adressering automatiskt leder frågor till den närmaste punkten av närvaro.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

I IPv6 ersätter **multicast-adresser** broadcast-mekanismen, som ansågs vara för kostsam och olämplig för ett globalt nätverk. En multicast Address identifierar en grupp gränssnitt, vanligtvis över flera värdar, som vill ta emot samma paket samtidigt.

Varje multicast Address innehåller ett speciellt 4-bitars _scope_-fält, som definierar den geografiska eller logiska gränsen för sändningen:


- Ett scope på `1` innebär att paketet endast är avsett för den lokala enheten.
- Ett scope på `2` begränsar paketet till den lokala länken: alla enheter på samma fysiska eller virtuella segment kan ta emot det.
- Ett scope på `5` utökar räckvidden till en plats, vanligtvis ett helt företagsnätverk.
- Ett scope på `8` utökar räckvidden till en organisation, vilket möjliggör leverans över alla subnät i samma enhet.
- Ett scope på `e` (14 i hexadecimal) anger en global räckvidd, vilket gör multicast-gruppen tillgänglig från var som helst på Internet om routningsinfrastrukturen stöder det.


Strukturen för en IPv6 multicast Address inkluderar:


- ett fält _Flag_ (4 bitar) anger om gruppen är permanent eller tillfällig,
- ett _Scope_-fält (4 bitar) definierar omfattningen,
- ett identifieringsfält (112 bitar) som identifierar multicastgruppens nummer.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Ett välkänt exempel på IPv6 multicast i praktiken är _Neighbor Discovery Protocol_ (NDP). I stället för att använda ARP som i IPv4 förlitar sig NDP på multicast-adresser som `ff02::1:ff00:0/104` för att sända ut förfrågningar om grannupptäckt, som endast riktar sig till relevanta värdar på samma länk.


Genom att definiera Address-scopes så exakt strukturerar IPv6 hur dataflöden skickas, tas emot och dirigeras. Denna granularitet gör protokollet mer flexibelt och effektivt för att hantera både lokal och global kommunikation, samtidigt som man undviker nackdelarna med generaliserad sändning.


## Address Assignment i ett lokalt nätverk


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


I det här kapitlet tittar vi på en av de mest praktiska aspekterna av IPv6-driftsättning: tilldelning av IP-adresser till värdar i ett lokalt nätverk. IPv6-arkitekturen har utformats för flexibilitet, så att varje enhet kan generate sin egen Address automatiskt, samtidigt som den tillåter helt manuell konfiguration när det behövs.


Ett lokalt IPv6-nätverk delar systematiskt upp Address i två delar:


- de första 64 bitarna representerar subnätprefixet, som vanligtvis tillhandahålls av en router eller en Address-myndighet;
- de återstående 64 bitarna används av värden för att unikt identifiera sig själv på det segmentet.

Denna modell förenklar i hög grad vägaggregering och hantering av Address-block.


Två huvudsakliga metoder används för att tilldela adresser till enheter:


- Manuell konfiguration, där administratören anger varje Interface:s exakta Address;
- Automatisk konfiguration,där enheter generate eller erhåller sina egna adresser dynamiskt.


Vid manuell konfiguration tilldelar administratören den fullständiga IPv6 Address till varje Interface. Vissa värden förblir reserverade:


- `::/128`: ospecificerad Address, aldrig permanent tilldelad ;
- `::1/128`: loopback Address (_loopback_), IPv4-ekvivalent: `127.0.0.1`.


Till skillnad från IPv4 finns det inget _broadcast_-koncept; kombinationer av "alla nollor" eller "alla ettor" i värddelen har ingen särskild betydelse.

Manuell konfiguration är fortfarande användbar i kontrollerade miljöer, men blir svår att upprätthålla i stor skala.


Det finns flera metoder för automatisk konfiguration:


- Protokollet **NDP** (_Neighbor Discovery Protocol_), som specificeras av RFC4862, möjliggör *stateless* automatisk konfiguration. I detta läge tar värden emot ett nätverksprefix från en lokal router och kompletterar själv Address med en identifierare baserad på dess MAC Address. Denna metod är enkel att implementera och kräver ingen central server.
- Implementeringar som de i Windows kan generate värddelen pseudoslumpmässigt för att förbättra integriteten genom att undvika direkt exponering av MAC Address. Att avslöja MAC Address i IPv6-paket kan ge upphov till integritetsfrågor, eftersom det gör det möjligt att spåra en enhet över olika nätverk.
- DHCPv6-protokoll: Definieras i RFC3315 och liknar DHCP som används för IPv4, men möjliggör mer kontrollerad och centraliserad konfiguration, inklusive leasinghantering, extra alternativ (DNS, MTU...) och registrering av databaser. DHCPv6 kan fungera ensamt eller tillsammans med statslös konfiguration för att tillhandahålla ytterligare parametrar utan att tilldela IP Address själv.


**Viktig anmärkning: ** I den MAC-baserade metoden konverteras MAC Address till en 64-bitars identifierare med hjälp av EUI-64-formatet. Denna mekanism infogar bytena `FF:FE` i mitten av den ursprungliga MAC Address (i 48 bitar) och inverterar den 7:e biten för att ange global unikhet. Resultatet är en stabil Interface-identifierare som används i den fullständiga IPv6 Address.


Här är ett exempel på hur man omvandlar en MAC Address till EUI-64:


![Image](assets/fr/045.webp)



På grund av den växande oron för spårning av enheter aktiverar moderna operativsystem (särskilt Linux, Windows 10+, macOS, Android) nu sekretesstillägg som standard. Dessa använder slumpmässigt genererade Interface-identifierare som periodiskt förnyas för utgående anslutningar, samtidigt som en stabil identifierare behålls för intern kommunikation (t.ex. DNS eller DHCPv6).


Precis som med DHCP i IPv4 kan automatiskt tilldelade IPv6-adresser ha två livstider, definierade av DHCPv6-routrar eller servrar:


- Preferred lifetime*: efter denna period förblir Address giltig, men används inte längre för att initiera nya anslutningar;
- Giltig livstid*: när den här tiden löper ut tas Address bort helt från Interface-konfigurationen.


Systemet gör det möjligt att hantera nätverksförändringar dynamiskt, t.ex. för att säkerställa en smidig övergång från en ISP till en annan. Genom att uppdatera prefixet som meddelas av routrar och justera DNS-poster parallellt kan IPv6-migrering genomföras utan något märkbart avbrott i tjänsten.


**Tips: ** Den kombinerade användningen av Address och DNS-livscykler gör det möjligt att implementera en gradvis övergångsstrategi, där nya anslutningar flyttas till en ny topologi, medan befintliga anslutningar fortsätter till sitt naturliga slut.


Kort sagt erbjuder IPv6 ett brett spektrum av flexibilitet för Address Assignment: manuell konfiguration, tillståndslös eller tillståndsstyrd automatisk konfiguration, DHCPv6 eller slumpmässig generering. Varje metod har sina egna fördelar och begränsningar och kan anpassas efter den kontrollnivå som krävs, nätverkets storlek eller integritetsbehov.


## Tilldelning av IPv6 Address-block


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Address distribution


IPv6 Address-allokeringssystemet har strukturerats för att uppfylla två mål: att garantera global Address-unikhet och att möjliggöra en logisk hierarki som gynnar aggregering och förenkling av routingtabeller.

Precis som för IPv4 är det *Internet Assigned Numbers Authority* (IANA) som står högst upp i denna hierarki. Den förvaltar det globala unicastutrymmet Address och delegerar Address-block till de fem regionala Internetregistren (_RIR_).


De fem befintliga RIR är följande:


- ARIN (Nordamerika),
- RIPE NCC (Europa, Mellanöstern, Centralasien),
- APNIC (Asien och Stillahavsområdet),
- AFRINIC (Afrika),
- LACNIC (Latinamerika och Västindien).


IANA tilldelar IPv6-block av varierande storlek till varje RIR, i allmänhet mellan /23 och /12. Detta tillvägagångssätt ger flexibilitet samtidigt som det säkerställer långsiktig skalbarhet. RIR:erna omfördelar i sin tur dessa block till Internet Service Providers (ISP:er), stora företag och offentliga institutioner.


Sedan 2006 har varje RIR fått ett IPv6 /12-block från IANA, en fast storlek som är utformad för att säkerställa en stabil och tillräckligt stor reserv för framtida tillväxt. RIR:erna delar vanligtvis upp dessa i /23-, /26- eller /29-block. Internetleverantörer får oftast /32-block, även om denna storlek kan variera beroende på internetleverantörens storlek och geografiska område. De tilldelar vanligtvis /48-block till kunder. Varje /48 ger 65 536 distinkta /64-undernät (en enorm kapacitet jämfört med IPv4).


**Viktigt att notera:** ett /32-block innehåller exakt 65 536 /48-underblock. Detta innebär att varje ISP kan betjäna tiotusentals kunder utan att uttömma sin tilldelning. Tack vare sin /48 har varje kund sedan ett gigantiskt utrymme för att strukturera sitt eget interna nätverk med så många /64-segment som de vill.


Den typiska fördelningshierarkin ser ut så här:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Med detta överflöd av adresser är NAT (*Network Address Translation*), som en gång var nödvändigt i IPv4 för att klara av Address-bristen, inte längre nödvändigt. Varje värd kan ha en unik, globalt routningsbar publik Address, vilket förenklar end-to-end-anslutning och gör protokoll som IPSec, VoIP eller inkommande anslutningar enklare att använda.


Om du vill kontrollera vilken organisation en IPv6 Address tillhör kan du använda kommandot `whois` för att fråga offentliga RIR-databaser. Denna transparens gör det möjligt att identifiera den organisation som äger ett prefix, vilket kan vara användbart för nätverks-, analys- eller säkerhetsändamål.


### Adressering av PA vs PI


Ursprungligen baserades IPv6-allokeringsmodellen enbart på PA-block (*Provider Aggregatable*), vilket innebär att de är kopplade till internetleverantören. I den här modellen får en organisation sitt prefix från sin ISP, vilket innebär att byte av leverantör kräver omnumrering av hela infrastrukturen.


Även om IPv6:s funktioner för automatisk konfiguration och Address:s livslängd gör det enklare att byta nummer, är det fortfarande besvärligt för organisationer med kritisk infrastruktur eller flera leverantörsanslutningar för redundanskrav.


Sedan 2009 har allokeringspolicyn tillåtit PI-block (*Provider Independent*). Dessa block (i allmänhet /48 i storlek) tilldelas direkt till ett företag eller en institution av en RIR, oberoende av någon ISP. Denna modell lämpar sig särskilt väl för organisationer som tillämpar *multihoming* (dvs. är anslutna till flera operatörer samtidigt). I Europa beskriver RIPE-512 t.ex. policyn för PI-tilldelningar.


### Notation för subnätmask


Precis som i IPv4 använder IPv6 CIDR (*Classless Inter-Domain Routing*). Detta innebär att man anger antalet bitar som prefixet består av efter Address med hjälp av tecknet `/`.


Ta följande exempel:


```
2001:db8:1:1a0::/59
```


Detta innebär att de första 59 bitarna är fasta och identifierar nätverket. Alla återstående bitar (här 69 bitar) kan användas för att identifiera subnät eller värdar.


Denna notation täcker alltså adresser från `2001:db8:1:1a0:0:0:0:0` till `2001:db8:1:1bf:ffff:ffff:ffff:ffff:ffff`.


Detta block omfattar därför en uppsättning av 8 /64 subnät, som vart och ett kan hysa ett stort antal enheter.


CIDR-notation möjliggör exakt planering av Address-utrymme, från storskaliga nätverk till heminställningar och virtualiserade miljöer, och uppmuntrar till aggregering av rutter, vilket minskar routerbelastningen och förbättrar skalbarheten.


### IPv6-paket och -headers


IPv6-paketformatet skiljer sig från IPv4 genom att vara både enklare och mer utbyggbart. Ett IPv6-datagram börjar alltid med en header av fast storlek på 40 byte som innehåller all väsentlig routinginformation. Detta strömlinjeformade tillvägagångssätt, jämfört med IPv4:s variabla headerlängd (från 20 till 60 byte), möjliggör snabbare och effektivare paketbehandling av routrar.


IPv6 tar dock inte bort funktionalitet: i stället för att integrera många valfria fält i huvudrubriken införs ett system med tilläggsrubriker som placeras omedelbart efter den grundläggande rubriken. Dessa valfria rubriker gör det möjligt att lägga till data eller instruktioner som är specifika för vissa funktioner, utan att i onödan belasta vanliga paket.


Vissa tilläggshuvuden följer en fast struktur, medan andra kan innehålla ett varierande antal alternativ. I Dessa alternativ är kodade som `{Typ, Längd, Värde}` tripletter:


- Fältet "Type" (1 byte) anger vilken typ av option det rör sig om;
- De två första bitarna i "Type" anger vad routrarna ska göra om alternativet inte känns igen:
 - Ignorera alternativet och fortsätt behandlingen,
 - Släpp datagrammet,
 - Avbryt och skicka ett ICMP-felmeddelande till källan.
 - Släpper datagrammet utan meddelande (när det gäller multicast-paket).
- Fältet "Length" (1 byte) anger storleken på fältet "Value", från 0 till 255 byte;
- Fältet "Value" innehåller de data som är kopplade till alternativet.


Här är en översikt över de olika typerna av förlängningsrubriker som definieras av IPv6.


#### Hop-by-Hop rubrik


Detta huvud, om det finns, placeras alltid omedelbart efter bashuvudet. Den innehåller information som måste bearbetas av varje router längs paketets väg, till skillnad från de flesta andra headers, som vanligtvis endast hanteras av destinationsnoden. Typiska användningsområden är signalering av globala parametrar eller begäran om specifika bearbetningssteg när paketet färdas genom nätverket.


![Image](assets/fr/047.webp)


#### Routningshuvud


Routningshuvudet anger en lista över mellanliggande adresser som paketet måste passera. Det finns två huvudsakliga routningslägen:


- Strikt routing: den exakta vägen är fördefinierad
- Lös routing: endast vissa obligatoriska steg specificeras.


De fyra första fälten i denna rooting header är:


- Next Header**: Identifierar typen av nästa rubrik;
- Routing Type**: definierar routningsmetoden (vanligtvis `0`);
- Segment kvar**: antal segment som återstår att traversera ;
- Address[n]**: förteckning över mellanliggande adresser.


Fältet "Segments Left" börjar med det totala antalet återstående segment och minskas med ett vid varje hopp.


![Image](assets/fr/048.webp)


#### Fragmenteringshuvud


I IPv6 är det bara källvärden som får fragmentera ett datagram, till skillnad från IPv4 där även routrar fick göra det. Alla IPv6-noder måste kunna hantera paket på minst 1280 byte. Om en router stöter på ett paket som är större än MTU för nästa länk skickar den ett *ICMPv6 Packet Too Big*-meddelande tillbaka till källan, som sedan justerar storleken på sina sändningar.


Fragmenteringshuvudet innehåller följande fält:


- Identification**: unik datagramidentifierare för återmontering.
- Fragment Offset**: fragmentets position inom det ursprungliga datagrammet.
- M-flagga**: anger om fler fragment följer.


![Image](assets/fr/049.webp)


#### Autentiseringshuvud (AH)


Detta huvud är utformat för att säkra kommunikation genom att verifiera både avsändarens äkthet och dataintegriteten. Det används ofta med IPsec-protokollet. Med hjälp av en autentiseringskod kan mottagaren bekräfta att meddelandet verkligen kommer från den förväntade avsändaren och att det inte har ändrats under transporten.


I händelse av ett bedrägligt modifieringsförsök kommer autentiseringskoden inte längre att matcha och datagrammet kan avvisas. Denna mekanism skyddar också mot replay-attacker genom att upptäcka obehöriga dupliceringar.


![Image](assets/fr/050.webp)


#### Destination Options Header


Denna header är endast avsedd för den slutliga mottagaren av datagrammet. Det kan användas för att lägga till alternativ eller metadata som är specifika för applikationen, utan att mellanliggande routrar tar hänsyn till dem.


Ursprungligen fanns inget sådant alternativ definierat i protokollet. Denna header infördes dock när IPv6 utformades, så att framtida tillägg kan läggas till utan att den övergripande paketstrukturen ändras. Alternativet null används t.ex. endast för att fylla ut rubriken till en multipel av 8 byte för minnesjustering.


![Image](assets/fr/051.webp)


IPv6-paketens design bygger på en tydlig separation mellan ett minimalt bashuvud och modulära tilläggshuvuden. Denna arkitektur säkerställer både standardprocessprestanda och den flexibilitet som krävs för att utveckla protokollet och integrera säkerhet, komplex routing eller mekanismer för tjänstekvalitet, samtidigt som kompatibiliteten med framtida infrastrukturer bibehålls.


## Förhållandet mellan IPv6 och DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


I moderna nätverk översätter DNS (*Domain Name System*) domännamn till IP-adresser som maskinerna kan använda. I och med införandet av IPv6 var DNS tvunget att anpassa sig för att stödja 128-bitarsadresser samtidigt som bakåtkompatibilitet med IPv4 upprätthölls. Denna samexistens är särskilt viktig i dual-stack-miljöer, där båda IP-versionerna fungerar samtidigt.


### IPv6-specifika DNS-poster


För att associera ett domännamn med en IPv6 Address använder DNS en AAAA-post (*quad-A*), på samma sätt som "A"-posten för IPv4-adresser. AAAA-posten mappar uttryckligen ett domännamn till en IPv6 Address.

Exempel:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Den här posten visar att domänen `ipv6.mydmn.org` har IPv6 Address `2001:66c:2a8:22::c100:68b`. Det är möjligt, och till och med rekommenderat för maximal kompatibilitet, att associera samma domännamn med flera IP-adresser, oavsett om det är IPv4 (via en A-post) eller IPv6 (via en AAAA-post). Detta gör det möjligt för IPv6-kompatibla kunder att föredra IPv6, samtidigt som det säkerställs att klienter som endast använder IPv4 fortfarande stöds.


Dessutom stöder DNS omvänd upplösning, vilket innebär att den kan leta upp domännamnet som är associerat med en viss IP Address. När det gäller IPv6 använder denna åtgärd PTR-poster som placeras i zonen `ip6.arpa`. Den här zonen är särskilt reserverad för omvänd upplösning för IPv6. För IPv4 är det zonen `in-addr.arpa`.


### Omvänd upplösning


Omvänd upplösning av en IPv6 Address följer en strikt process:

1) Expandera Address till fullständig hexadecimal notation (16 byte, dvs. 32 hexadecimala siffror).

Exempel:


```shell
2001:66c:2a8:22::c100:68b
```


Blir:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Vänd på ordningen för varje hexadecimal siffra (nibble), separera dem med punkter och lägg till `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Denna struktur säkerställer standardiserade, unika omvända uppslagningar i IPv6 Address-utrymmet.


**Vänligen notera**: DNS-frågor kan skickas via antingen IPv4 eller IPv6. Vilket transportprotokoll som används har ingen inverkan på vilken typ av poster som returneras.

Till exempel:


- En klient som är ansluten via IPv6 kan begära en IPv4-post.
- En klient som är ansluten via IPv4 kan begära en IPv6-post.

DNS-servern svarar helt enkelt med de poster den har, oavsett frågans transportprotokoll.


När ett värdnamn är mappat till både IPv4 och IPv6 styrs valet av vilken Address som ska användas av RFC 6724, som definierar en Address-valsalgoritm baserad på faktorer som prefixpreferens, omfattning och nåbarhet. Som standard föredras i allmänhet IPv6 om inte detta åsidosätts genom system- eller nätverkskonfiguration.


**Viktig påminnelse**: När du bäddar in en IPv6 Address i en URL (*Uniform Resource Locator*) måste den omslutas av hakparenteser (`[]`). På så sätt undviks förväxling mellan kolon (`:`) inuti IPv6 Address och kolon som skiljer värdnamnet från porten i URL:en.


Giltigt exempel:


```shell
http://[2001:db8::1]:8080
```


På så sätt säkerställs att webbadressen behandlas korrekt av både webbläsare och webbservrar.


För att integrera IPv6 i DNS-systemet krävs därför nya posttyper, en strikt metod för omvänd upplösning samt exakta urvals- och formateringsregler för att säkerställa kompatibilitet och konsekvens i routningen.


### Del sammanfattning


I det här avsnittet har vi utforskat de grundläggande principerna för IPv6-adressering. Vi började med att undersöka strukturen i IPv6 Address: dess 128-bitarslängd, hexadecimala notation och de förenklingsregler som används för att förkorta repetitiva sekvenser av nollor. Denna design gör det möjligt för IPv6 att övervinna begränsningarna i IPv4:s Address-utrymme, samtidigt som skalbarhet och effektiv hierarki garanteras.


Vi tittade sedan på de olika kategorierna av IPv6-adresser: unicast, anycast och multicast, och beskrev deras omfattning, typiska användning och representation i Address-utrymmet.


Därefter gick vi igenom metoderna för tilldelning av IPv6-adresser i ett lokalt nätverk, antingen genom manuell konfiguration, via DHCPv6-protokollet eller med hjälp av statslösa autokonfigurationsmekanismer som de som erbjuds av NDP. Dessa metoder gör det möjligt för enheter att automatiskt generate sin egen Address från det tillhandahållna prefixet och deras MAC Address (via EUI-64), samtidigt som de erbjuder flexibilitet när det gäller livstidshantering och integritet.


Vi har också beskrivit hur Address-blocken fördelas, från IANA, som distribuerar dem till de fem RIR:erna (*Registered Internet Regions*) och sedan till ISP:erna, som distribuerar dem vidare till sina kunder som undernät (ofta i /48, vilket möjliggör 65536 /64 undernät). Distinktionen mellan blocken _Provider Aggregatable_ (PA) och _Provider Independent_ (PI) hjälper till att hantera _multihoming_ eller scenarier med byte av leverantör.


Vi såg att DNS har anpassats till IPv6 genom införandet av AAAA-posten och att mekanismer för omvänd upplösning nu förlitar sig på zonen `ip6.arpa`. Det är viktigt att DNS förblir oberoende av vilket transportprotokoll som används (IPv4 eller IPv6), vilket säkerställer sömlös interoperabilitet i en dual-stack-miljö.


IPv6 är därför inte bara en stegvis förbättring jämfört med IPv4, utan en fullständig omarbetning av adresseringssystemet, byggt för att möta både nuvarande och framtida utmaningar på det globala Internet.


I den sista delen av denna NET 302-kurs kommer vi att gå in i praktiken och fokusera på verktyg för nätverksdiagnostik.



# Verktyg för nätverksdiagnostik


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Verktyg för nätverksåtkomst Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


I detta första kapitel i det sista avsnittet om nätverksdiagnostik fokuserar vi på verktyg för att analysera nätverksåtkomsten Layer i TCP/IP-modellen. Denna Layer ansvarar för direkt kommunikation mellan enheter i samma fysiska nätverk, framför allt genom användning av MAC-adresser och fysiska nätverksgränssnitt som Ethernet-kort eller Wi-Fi-gränssnitt.


Syftet är att förse administratörer med praktiska verktyg för att inspektera, testa och optimera denna viktiga Layer lågnivåanslutning. Dessa verktyg kan användas för att verifiera att gränssnitten fungerar korrekt, felsöka konfigurationsproblem för nätverkskort eller upptäcka avvikelser som kollisioner, paketförlust eller länkfel.


### IP/MAC grannskapsverktyg


#### verktyget `Arp


Ett av de äldsta diagnosverktygen i Network Access Layer är kommandot `arp`. Även om det alltmer ersätts av moderna alternativ som `ip neigh` (som vi kommer att upptäcka inom kort). `Arp` finns fortfarande på många system för att visa eller manipulera ARP-cachen (*Address Resolution Protocol*). I den här cachen lagras mappningarna mellan IP-adresser och MAC-adresser som är kända lokalt på en maskin. Med andra ord kan du avgöra vilken fysisk (MAC) Address som motsvarar en viss IP Address i det lokala nätverket.


När en värd vill skicka ett paket till en IP Address inom samma subnät måste den i praktiken först känna till målmaskinens MAC Address. Denna mappning hanteras av ARP, som sänder ut en förfrågan i det lokala nätverket och får ett svar som innehåller motsvarande MAC Address. Detta resultat lagras sedan temporärt i en lokal tabell som kallas "ARP-cache", för att undvika att upprepa förfrågningarna för varje nytt paket.


För att visa innehållet i denna cache och kontrollera de poster som för närvarande är kända av maskinen, använd:


```bash
arp -a
```


Detta kommando listar alla lokalt registrerade IP/MAC-mappningar för alla gränssnitt. Varje rad innehåller värdnamnet (om det kan lösas), IP Address, motsvarande MAC Address och Interface där mappningen observeras.


För att filtrera visningen till en specifik IP Address, ange den helt enkelt:


```bash
arp -a 192.168.1.5
```


Det gör det enkelt att kontrollera om en viss IP Address finns i cacheminnet, vilket kan hjälpa till att diagnostisera kommunikationsfel mellan två värdar i samma nätverk.


Om du bara vill visa de ARP-poster som är kopplade till ett visst nätverk Interface (t.ex. ett Ethernet-kort med namnet `eth0`) kan du använda


```bash
arp -a -i eth0
```


Detta är särskilt användbart i multi-Interface miljöer (trådbundna, trådlösa, VPN, etc.), där en värd kan ha flera nätverksadaptrar.


Kommandot `arp` är inte begränsat till skrivskyddad användning. Det kan också användas för att manuellt redigera ARP-cachen, en ovärderlig funktion i vissa avancerade felsökningsscenarier eller när du simulerar specifika förhållanden. Du kan t.ex. lägga till en IP/MAC-mappning manuellt:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Det här kommandot skapar en statisk post i den lokala ARP-tabellen och associerar IP Address `192.168.1.7` med MAC Address `00:17:BC:56:4F:25` på Interface `eth2`. Om ingen Interface anges använder systemet automatiskt den första tillämpliga Interface.


Du kan också ta bort en post från ARP-cachen, antingen för att rätta till ett fel eller för att tvinga fram en ny sökning:


```bash
arp -d 192.168.1.7
```


Detta raderar posten, vilket säkerställer att nästa kommunikationsförsök utlöser en ny ARP-begäran.


**ANMÄRKNING**: Alternativet delete accepterar även ett Interface-namn, vilket gör att du kan rikta borttagningen av en specifik post mer exakt.


Sammanfattningsvis ger verktyget `arp` diagnostik på låg nivå, vilket är särskilt användbart i lokala nätverk där anslutningsproblem ofta kan spåras tillbaka till felaktig eller föråldrad Address-resolution. På nya system, särskilt moderna Linux-distributioner, ersätts dock detta verktyg i allt högre grad av kommandot `ip neigh` från verktygsuppsättningen `iproute2`, som erbjuder liknande funktioner i ett mer enhetligt ramverk.


#### `Ip neigh` verktyg


På moderna system, särskilt de senaste Linux-distributionerna, är kommandot `ip neigh` det bästa verktyget för att inspektera och hantera mappningar mellan IP- och MAC-adresser. Detta kommando är en del av `iproute2`-sviten, som gradvis ersätter äldre verktyg som `arp`, vilket ger ett mer konsekvent och flexibelt ramverk för diagnostik på datalänken Layer.


Kommandot `ip neigh` frågar efter den lokala IP-granncachen, som motsvarar ARP-cachen för IPv4 och NDP-cachen (_Neighbor Discovery Protocol_) för IPv6. I denna cache lagras kända associationer mellan IP-adresser (v4 eller v6) och MAC-adresser, tillsammans med deras status (giltig, väntande, utgången...).


Det grundläggande kommandot för att visa cacheminnet är:


```bash
ip neigh
```


Detta ger en lista med poster som visar destinations-IP Address, relevant nätverk Interface, tillhörande MAC Address (om tillgängligt) och postens status (t.ex. `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).


Exempel på utdata:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Den här raden visar att maskinen känner till en giltig mappning mellan IP Address `192.168.1.5` och MAC Address `00:17:BC:56:4F:25` via Interface `eth0`.


Du kan också filtrera poster efter kriterier som IP Address, Interface eller tillstånd. Till exempel, för att endast fråga Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Eller för att visa alla poster för Interface `eth1`:


```bash
ip neigh show dev eth1
```


Utöver konsultation kan `ip neigh` också användas för att manuellt redigera cacheminnet. Till exempel för att lägga till en statisk post:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Detta associerar IP Address `192.168.1.7` permanent med den angivna MAC Address på Interface `eth1`. Alternativet `nud permanent` (för _Neighbor Unreachability Detection_) säkerställer att posten inte automatiskt ogiltigförklaras.


Omvänt, för att radera en cache-post:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Detta tvingar systemet att lösa mappningen på nytt nästa gång det kommunicerar med den Address.


**ANMÄRKNING**: Verktyget `ip neigh` fungerar för både IPv4 och IPv6. För IPv4 har det ett gränssnitt mot ARP och för IPv6 mot NDP. Detta ger ett enhetligt och konsekvent tillvägagångssätt för att hantera IP/MAC-relationer över protokollfamiljer, vilket gör `ip neigh` till den moderna standarden för grannhantering på Linux-system.


### Paketera analysverktyg


För att grundligt analysera vad som händer i ett datornätverk behöver administratörerna verktyg som kan fånga upp de paket som utväxlas mellan maskiner. Två verktyg sticker ut som riktmärken: `tcpdump` och `Wireshark`. Dessa verktyg är nödvändiga för att diagnostisera onormala beteenden, granska protokollutbyten eller studera nätverkssäkerhet genom att inspektera raminnehåll.


#### `ttcpdump`: analys av kommandoraden


`tcpdump` är ett mycket kraftfullt kommandoradsverktyg som är utformat för att fånga och visa paket som färdas genom ett nätverk Interface. Det fungerar i realtid och tack vare sin lätta design kan det användas på system utan en grafisk Interface eller med begränsade resurser. Det förlitar sig på biblioteket `libpcap`, som tillhandahåller maskinvaruoberoende lågnivåfunktioner.


Ett vanligt användningsområde för `tcpdump` är att övervaka nätverksaktiviteten för en maskin eller ett nätverkssegment genom att filtrera paket enligt specifika kriterier. Resultaten kan omdirigeras till en fil, vilket gör att trafiken kan arkiveras för senare analys eller spelas upp i ett annat verktyg, t.ex. Wireshark.


Den allmänna kommandosyntaxen är:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` skriver fångade paket till en fil i `libpcap`-format (tillägg `.cap` eller `.pcap`);
- `-i` anger det nätverk som Interface ska övervaka (t.ex. `eth0`, `wlan0`);
- `-s` anger den maximala mängden data som samlas in per paket. Om du anger `0` fångas alla paket;
- `-n` inaktiverar DNS och namnmatchning för tjänster, vilket förbättrar prestandan.


Med uttrycksfiltren i slutet av kommandot kan du begränsa registreringen till en delmängd av trafiken. Du kan kombinera nyckelorden `host`, `port`, `src`, `dst`, etc. för att förfina urvalet.


Exempel: att fånga HTTP-paket (port 80) till eller från servern 192.168.25.24 och spara dem i en fil med namnet "fichier.cap":


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Den resulterande filen kan senare analyseras i ett grafiskt verktyg eller spelas upp på nytt på ett annat system.


#### Wireshark: avancerad visuell analys


Wireshark, tidigare känt som *Ethereal*, är ett komplett nätverksanalysprogram med en grafisk Interface. Till skillnad från `tcpdump` ger det strukturerad, detaljerad visualisering av paket, inklusive protokolldissektion, flödesdiagram, trafikstatistik och interaktiva filter. Det förlitar sig också på `libpcap`, vilket innebär att det kan öppna och bearbeta capture-filer som genereras av `tcpdump`.


Wireshark finns tillgängligt på många operativsystem, inklusive Linux och Windows. För att installera programmet krävs administratörsbehörighet för att få tillgång till inspelningsgränssnitten. När du har startat kan du välja ett nätverk Interface från menyn *Capture*. Genom att klicka på *Start* påbörjas paketinspelning i realtid. Displayen är indelad i tre rutor:


- listan över inspelade bildrutor ;
- protokollavkodade detaljer,
- rå hexadecimal data.



![Image](assets/fr/052.webp)



Wireshark utmärker sig i scenarier där du behöver observera komplexa protokollbeteenden, rekonstruera programdialoger (t.ex. en HTTP- eller DNS-session) eller studera tjänsters svarstider. Det stöder också mycket specifika visningsfilter med hjälp av sin dedikerade syntax (som skiljer sig från `tcpdump`) för att bara fokusera på relevanta paket.


#### Kompletterande verktyg


Det är viktigt att notera att `tcpdump` och Wireshark inte är utbytbara: var och en har sina egna styrkor. `tcpdump` är bättre lämpad för kommandoradsmiljöer, automatiserade skript och fjärrserverinterventioner, medan Wireshark är idealisk för detaljerad, interaktiv och pedagogisk trafikanalys.


De två verktygen kan kombineras: en inspelning kan göras på ett fjärrsystem med `tcpdump`, sedan överförs `.cap`-filen för analys med Wireshark på en lokal maskin. Detta tillvägagångssätt används ofta i praktiken.


### Analysverktyg för Interface


På Network Access Layer är det ofta nödvändigt att fråga efter och konfigurera fysiska nätverksgränssnitt för att diagnostisera fel, optimera prestanda eller verifiera anslutningsintegritet. Ett av de mest kraftfulla verktygen som finns tillgängliga under Linux för detta ändamål är `ethtool`, ett kommandoradsverktyg som inte bara ger detaljerad teknisk information om en Ethernet Interface, utan också låter dig justera några av dess parametrar i realtid.


#### Se specifikationer för Interface


En viktig funktion i `ethtool` är dess förmåga att fråga en Interface och visa dess aktuella egenskaper. Detta gör att du kan kontrollera:


- länkhastighet (t.ex. 100 Mbit/s, 1 Gbit/s eller 10 Gbit/s) ;
- förhandlingsläge (halvduplex eller fullduplex) ;
- om autonegotiation är aktiverad;
- typ av port (koppar, fiber etc.) ;
- länkstatus (aktiv eller ej) ;
- stöd för avancerade funktioner som *Wake-on-LAN*.


Den här informationen är särskilt användbar för att diagnostisera problem som rör fysisk anslutning eller felaktiga förhandlingsinställningar mellan värdens nätverkskort och den utrustning som det ansluts till (switch, router etc.).


För att få denna information kör du helt enkelt:


```bash
ethtool enp0s3
```


Detta kommando ger en detaljerad rapport om Interface `enp0s3`, en vanlig namngivningskonvention på CentOS- eller RHEL-baserade system.



![Image](assets/fr/053.webp)



#### Dynamisk modifiering av Interface-parametrar


`ethtool` är inte begränsat till observation: det ger dig också möjlighet att justera vissa Interface-parametrar utan att starta om maskinen. Detta gör det möjligt att t.ex. tvinga fram en specifik länkhastighet eller aktivera funktioner enligt behoven i det lokala nätverket.


Alternativet `-s` används för att dynamiskt konfigurera parametrar som t.ex:


- länkhastighet (`speed`), anges explicit (t.ex. 1000 för 1 Gbit/s) ;
- duplexläge (`duplex`), antingen `half` eller `full` ;
- aktivera eller inaktivera autonegotiation (`autoneg`) ;
- möjliggörande av *Wake-on-LAN* (`wol`) ;
- porttyp.


Exempel 1: aktivera autonegotiation på en Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Exempel 2: aktivera funktionen *Wake-on-LAN* (så att maskinen kan väckas på distans via ett magiskt paket):


```bash
ethtool -s enp0s3 wol p
```


I det här exemplet anger alternativet `p` att uppvaknandet ska ske så snart ett *Wake-on-LAN*-paket upptäcks. Den här inställningen används ofta i företagsmiljöer för att utföra uppdateringar över natten eller fjärrunderhåll.


#### Installation av verktyg


Det är viktigt att notera att `ethtool` inte alltid är installerat som standard. På Red Hat/CentOS-distributioner kan det installeras med kommandot:


```bash
yum install -y ethtool
```


På Debian och Ubuntu är motsvarande kommando:


```bash
sudo apt install ethtool
```


**VARNING**: I alla `ethtool`-kommandon måste namnet på nätverket Interface anges omedelbart efter alternativet (som `-s`). Alla syntaxfel i placeringen av parametrar gör kommandot ogiltigt eller ineffektivt.



## Nätverk Layer verktyg


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Verktyg för trafikanalys


Inom nätverksdiagnostik är kommandot `ping` fortfarande ett av de enklaste men samtidigt mest kraftfulla verktygen för att testa anslutningen mellan två maskiner. Det kontrollerar om en fjärrvärd är nåbar vid en viss tidpunkt, samtidigt som det ger information om latens, länkstabilitet och DNS-upplösning.


Kommandot `ping` förlitar sig på ICMP-protokollet (*Internet Control Message Protocol*). När en användare skickar en `ping`-begäran skickar systemet ett ICMP "Echo Request"-paket till en IP Address eller ett värdnamn. Om målmaskinen är online och nätverksvägen är giltig, svarar den med ett ICMP "Echo Reply"-paket. Denna enkla mekanism kan användas för att mäta latens och upptäcka problem med anslutning eller namnupplösning.


Exempel på ett klassiskt kommando:


```bash
ping 172.17.18.19
```


Typiskt svar:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


I det här exemplet har namnmatchningen utförts automatiskt: domänen `mydmn.org` är associerad med IP Address `172.17.18.19`, vilket bekräftar att DNS-matchningen fungerar korrekt. Kommandot ger också tekniska detaljer som t.ex:


- iCMP-sekvensnummer (`icmp_seq`), användbart för att kontrollera svarsordningen;
- TTL (*Time-To-Live*), som anger antalet återstående hopp innan paketet kasseras;
- round-trip time/delay (`time`), uttryckt i millisekunder, som ger en uppskattning av länkens latens.


#### Mer detaljerad analys av ICMP-parametrar


TTL är ett kritiskt fält i IP-protokollet. Varje datagram initialiseras med ett TTL-värde av avsändaren (ofta 64, 128 eller 255). Varje router längs vägen minskar detta värde med 1. Om TTL når 0 innan det når sin destination, kasseras paketet och ett ICMP-fel returneras till avsändaren. Denna mekanism förhindrar oändliga routingslingor.


Spridningstiden (*round-trip delay/time*) mäter den tid det tar för ett paket att lämna avsändaren, nå målet och återvända. I praktiken anses en fördröjning på under 200 ms vara acceptabel för en stabil länk. Onormalt höga fördröjningar kan tyda på överbelastning i nätverket, ineffektiv routing eller dålig länkkvalitet.


#### Avancerad användning av `ping


`ping` ger alternativ för att förfina tester och observera specifika nätverksbeteenden.


Om du vill skicka broadcast-begäranden kan du använda alternativet `-b` för att rikta in dig på alla värdar i ett subnät:

```bash
ping -b 192.168.1.255
```


Detta är användbart i lokala nätverk för att snabbt upptäcka aktiva värdar eller testa hur nätverket hanterar broadcast-begäranden. I många konfigurationer blockerar dock routrar och brandväggar broadcast-pings för att förhindra förstärkningsattacker.


Du kan också ange ett anpassat intervall mellan begäranden med alternativet `-i` (standard: 1 sekund):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Detta skickar 10 ICMP-förfrågningar med 0,2 sekunders intervall. Sådana tester är användbara för att upptäcka latensfluktuationer under en kort period eller för att lätt stressa en länk för att utvärdera dess stabilitet.


### Verktyg för analys av routingtabeller


Kommandot `ip route`, som ingår i `iproute2`-sviten, är det rekommenderade och standardiserade verktyget på moderna Linux-system för att inspektera och hantera kärnans IP-routingtabell. Det ersätter det föråldrade kommandot `route` och erbjuder tydligare syntax, större konsekvens och utökat stöd för moderna funktioner (IPv6, flera tabeller, namnrymder etc.).


#### Visning av routningstabellen


Så här visar du den aktuella routingtabellen:


```bash
ip route show
```


Denna utdata listar alla vägar som är kända av kärnan, det vill säga de vägar som utgående paket tar beroende på deras destination.


Exempel på utdata:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Varje rad representerar en rutt. Viktiga fält inkluderar:


- default**: standardrutten, som används när ingen mer specifik rutt matchar.
- via**: den gateway som används för att nå destinationen.
- dev**: det nätverk som Interface använde.
- proto**: hur rutten skapades (manuellt, DHCP, kernel, etc.).
- metric**: ruttkostnad, används för att prioritera flera möjliga vägar.
- scope**: ruttomfång (t.ex. `link` för en direktansluten rutt).
- src**: käll-IP Address som används för utgående paket på denna Interface.


#### Lägga till och ta bort rutter


Du kan också ändra routingtabellen dynamiskt, t.ex. genom att lägga till eller ta bort statiska rutter.


Lägga till en statisk rutt:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Detta konfigurerar en rutt till nätverket `192.168.1.0/24` via gatewayen `192.168.1.1` på Interface `eth0`.


Ta bort den här rutten:


```bash
ip route del 192.168.1.0/24
```


Detta kommando raderar den tidigare definierade rutten.


#### Användbara kommandon


Här är några användbara varianter för analys eller skriptning:


- `ip -4 route`: visar endast IPv4-vägar;
- `ip -6 route`: visar endast IPv6-vägar;
- `ip route list table main`: visar den huvudsakliga routingtabellen (standardvärde) ;
- `ip route get <Address>`: visar vilken Interface och gateway ett paket till den angivna Address skulle använda.


Exempel:


```bash
ip route get 8.8.8.8
```


Här visas den exakta vägen som ett paket skulle ta för att nå `8.8.8.8`.


### Verktyg för spårning


Ett av de mest effektiva verktygen för att analysera den väg som IP-paketen tar mellan en källvärd och en måldestination är kommandot `traceroute`. Det visar steg för steg den väg som paketen följer och identifierar de mellanliggande routrar som de passerar. I händelse av fel på en nätverkslänk eller ett driftavbrott kan `traceroute` hjälpa till att exakt lokalisera problemet.


Precis som med kommandot `ping` kan målet anges antingen med dess fullständigt kvalificerade domännamn (FQDN) eller med dess IP Address. Till exempel


```bash
traceroute mydmn.org
```


#### Funktionsprincip


`traceroute` förlitar sig på TTL-fältet (*Time To Live*) i IP-paketens header. Som förklarats tidigare är detta fält en räknare som minskas av varje router längs vägen. När TTL når noll kasseras paketet och routern returnerar ett ICMP-meddelande "Time Exceeded" till avsändaren. Denna mekanism förhindrar oändliga loopar i händelse av felaktig dirigering.


`traceroute` utnyttjar detta beteende för att kartlägga routrarna mellan avsändare och mottagare:


- Den skickar först en serie UDP-paket (vanligtvis tre) med en TTL på 1. Den första routern stöter på en TTL på 0 så den kastar paketet och svarar sedan med ett ICMP-meddelande som avslöjar dess IP Address och svarstid.
- Därefter skickar den ytterligare en serie paket med en TTL på 2, vilket avslöjar den andra routern.
- Processen upprepas tills destinationen har nåtts, varvid värden svarar med ett ICMP Port Unreachable-meddelande som anger att slutpunkten har nåtts.


Som standard använder `traceroute` UDP-paket som skickas till oanvända portar (vanligtvis med början på 33434), men kan också konfigureras att använda ICMP (som `ping`) eller till och med TCP, beroende på system eller kommandovarianter.


Exempel på utdata:


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


Varje rad motsvarar en router som passeras, med upp till tre tidsmätningar (i millisekunder) som anger latensen för tur- och returresan till den routern. Dessa värden hjälper till att bedöma prestandan för varje nätverkssegment.


#### Tolkning av resultat


Om en router inte svarar eller filtrerar ICMP-meddelanden visas asterisker `*` i stället för svarstiden. Detta kan tyda på:


- en brandvägg som blockerar ICMP-svar,
- en enhet som är konfigurerad att inte svara, eller
- ett tillfälligt problem med anslutningen längs vägen.


Således identifierar `traceroute` inte bara den väg som tagits utan belyser också punkter med onormal fördröjning eller avbrott.


På vissa system kan det motsvarande kommandot `tracepath` användas, vilket inte kräver root-behörighet. För IPv6 använder du `traceroute6` eller `tracepath6`.


Exempel för IPv6-spårning:


```bash
traceroute6 ipv6.google.com
```


### Verktyg för att kontrollera aktiva anslutningar


För att diagnostisera aktiva nätverksanslutningar och övervaka nätverksaktiviteten på ett Linux-system är kommandot `ss` (förkortning för _socket statistics_) det moderna referensverktyget. Det är en del av `iproute2`-sviten och ersätter det numera försvunna `netstat`, vilket ger bättre prestanda och mer exakta resultat.


`ss` visar aktiva TCP- och UDP-anslutningar, lyssnande portar, lokala adresser och fjärradresser, anslutningsstatus och tillhörande processer.


#### Allmän användning


När kommandot `ss` körs utan alternativ visas aktiva TCP-anslutningar. Grundläggande syntax:


```bash
ss [options]
```


Några vanliga alternativ för att förfina analysen:


- `-t`: visar endast TCP-anslutningar;
- `-u`: visar endast UDP-anslutningar;
- `-l`: visa endast lyssnande uttag;
- `-n`: inaktivera namnmatchning (råa IP- och portnummer) ;
- `-p`: visar varje socket associerade processer (PID och programnamn),
- `-a`: visa alla anslutningar, även inaktiva,
- `-s`: visa socket-statistik på hög nivå.


#### Fallstudier


För att visa alla aktiva anslutningar som använder TCP-port 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Detta visar aktiva TCP-anslutningar som involverar port 80. Statusar som `LISTEN`, `ESTABLISHED`, `TIME-WAIT` anger den aktuella statusen för varje Exchange.


Exempel på utdata:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


För att visa alla nätverksanslutningar med tillhörande processer:


```bash
ss -tulnp
```


För att få en övergripande sammanfattning av användningen av uttag:

```bash
ss -s
```


Filtrera endast UDP-anslutningar:

```bash
ss -unp
```


Dessa kommandon är särskilt användbara för att upptäcka misstänkta anslutningar, oväntade lyssningsportar eller för att övervaka aktiviteten hos en viss tjänst.


## Transport och påfyllning av Layer-verktyg


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Verktyg för DNS-frågor


I de övre lagren av TCP/IP-modellen, särskilt i Application Layer, är det viktigt att förstå hur namnupplösning fungerar. Med DNS-frågeverktyg kan du kontrollera om ett domännamn är korrekt associerat med en IP Address och även diagnostisera problem med DNS-servern, t.ex. felaktig konfiguration, spridningsfördröjningar eller otillgänglighet. De här verktygen är viktiga för alla nätverksadministratörer och användare som vill få en djupare förståelse för DNS-utbyten i en IP-miljö.


#### Kommandot `nslookup`


Det enklaste verktyget för DNS-frågor är `nslookup`. Det skickar en fråga till en DNS-server och returnerar den IP Address som är associerad med ett domännamn (eller vice versa). Som standard ställs en fråga till systemets konfigurerade DNS-server, men du kan också ange en server direkt i kommandot.


Exempel på en direktuppslagning:

```bash
nslookup mydmn.org
```


Förfrågan till en specifik DNS-server:

```bash
nslookup mydmn.org 192.6.23.4
```


Begäran ber DNS-servern på `192.6.23.4` att lösa namnet `mydmn.org`. Detta är särskilt användbart för att kontrollera om en viss DNS-server känner igen ett domännamn eller för att verifiera att servern fungerar korrekt.


#### Kommandot "dig


`dig` (*Domain Information Groper*) är ett modernare, mer komplett och flexibelt verktyg än `nslookup`. Det stöder komplexa frågor och ger detaljerad information om upplösningsprocessen, den hierarki av servrar som är inblandade, den typ av post som returneras (A, AAAA, MX, TXT etc.) och eventuella fel som uppstått.


Exempel på en grundläggande fråga:

```bash
dig mydmn.org
```


Förfrågan till en specifik DNS-server:

```bash
dig @192.6.23.4 mydmn.org
```


Med det här kommandot kontrolleras tillgängligheten för en DNS-post på en viss server.

En av de viktigaste fördelarna med `dig` är att den visar detaljerna i DNS-svaret, vilket gör den mycket användbar för att diagnostisera konfigurationsfel.


#### Manuell konfiguration av DNS-resolvers


Ibland är det nödvändigt att åsidosätta de DNS-servrar som används lokalt, t.ex. i testmiljöer eller för att tvinga fram användningen av specifika servrar. Detta kan göras genom att redigera filen `/etc/resolv.conf`, som definierar systemets inställningar för DNS-upplösning.


Exempel på konfiguration:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Fältet `search` anger en domän som ska läggas till automatiskt vid upplösning av kortnamn.
- Posterna `nameserver` anger vilka DNS-servrar som ska användas, i prioritetsordning.


På många moderna distributioner (särskilt de som använder `systemd-resolved`) är ändringar i `/etc/resolv.conf` temporära och kan skrivas över vid omstart eller återanslutning till nätverket. Mer permanenta metoder inkluderar användning av `resolvconf`, `systemd-resolved` eller ändring av *NetworkManager*-konfigurationer.


#### Kommandot "host


Ett annat enkelt men effektivt DNS-verktyg är `host`. Det omvandlar domännamn till IP-adresser (eller tvärtom) och kan hjälpa till att diagnostisera DNS-fel eller felkonfigurationer i ett nätverk Interface.


Exempel på detta:

```bash
host mydmn.org
```


Omvänd uppslagning:

```bash
host 192.6.23.4
```


`host` är särskilt praktiskt för snabba kontroller, särskilt när det används i kommandoradsskript.


Upprepade eller intensiva förfrågningar till DNS-servrar från tredje part utan tillstånd kan tolkas som intrångsförsök eller skadlig aktivitet. Om dessa kommandon används på fel sätt, eller mot nätverk som du inte kontrollerar, kan de likna spaningsundersökningar, som ofta är ett första steg i en attack. Begränsa alltid användningen av dem till miljöer som du administrerar eller där du har uttrycklig behörighet.


### Verktyg för nätverksscanning


När man övervakar eller säkrar ett lokalt eller brett nätverk är det viktigt att identifiera aktiva enheter och de tjänster som de exponerar. Det är precis vad verktyget `nmap` (*Network Mapper*) gör.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Introduktion till `nmap`


`nmap` möjliggör riktad skanning av en eller flera värdar för att upptäcka öppna portar, tillgängliga tjänster (HTTP, SSH, DNS, etc.) och ibland till och med vilken typ av operativsystem som används. Tack vare sina många alternativ ger `nmap` en exakt översikt över ett nätverks exponeringsyta, vilket är viktigt under gransknings- eller härdningsfaser av infrastrukturhantering.


Precis som kommandot `host` får `nmap` aldrig användas på nätverk eller infrastrukturer som du inte äger eller utan uttryckligt tillstånd. Obehöriga portskanningar kan flaggas som skadliga spaningsförsök, upptäcks ofta av säkerhetssystem (brandväggar, IDS/IPS) och kan till och med leda till rättsliga konsekvenser.


#### Grundläggande användning


För att skanna en specifik värd och visa dess öppna portar:

```bash
nmap 192.168.0.1
```


Detta kommando skannar de 1000 vanligaste portarna på värd `192.168.0.1` och visar de tjänster som nås och de protokoll som används. Om DNS-upplösning är konfigurerad kan du även använda värdnamnet i stället för IP Address.


#### Fullständig nätverksskanning


En av fördelarna med `nmap` är dess förmåga att skanna ett helt adressområde med ett enda kommando. Det gör det till exempel enkelt att snabbt inventera alla aktiva maskiner i ett nätverk:


```bash
nmap 192.168.0.0/24
```


I det här fallet kommer alla värdar i intervallet `192.168.0.0` till `192.168.0.255` att tillfrågas. För varje IP Address visas en lista över öppna portar, deras status (öppna, filtrerade etc.) och, om möjligt, namnet på motsvarande tjänst.



![Image](assets/fr/055.webp)



En administratör kan förlita sig på `nmap` för flera uppgifter:


- Detektera aktiva värdar**: identifiera vilka maskiner som svarar inom ett subnät;
- Serviceinventering**: se till att endast de nödvändiga portarna är tillgängliga (principen om minsta möjliga privilegier);
- Kontroll av efterlevnad**: jämför öppna portar med organisationens säkerhetspolicy;
- Sårbarhetsförebyggande åtgärder**: upptäcka osäkra eller föråldrade tjänster som körs på kritiska maskiner.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Verktyg för processförhör


För en djupgående analys av aktiva processer och öppna filer, särskilt i nätverkssammanhang, använder Linux-administratörer ofta kommandot `lsof` (*List Open Files*). Trots sitt namn är `lsof` inte begränsat till traditionella filer: på UNIX-system betraktas allt som en fil, inklusive nätverksuttag, enheter och kommunikationskanaler.


Detta verktyg ger därför en tvärsnittsvy av systemet genom att korrelera aktiva processer, öppna nätverksportar, åtkomliga filer och de inblandade användarna.


#### Nätverksanalys med `lsof`


Alternativet `-i` begränsar utdata till nätverksanslutningar (TCP, UDP, IPv4 eller IPv6). Detta gör det enkelt att se vilka processer som kommunicerar via nätverket:


```bash
lsof -i
```


Detta kommando listar alla processer som körs via en nätverkssocket och visar vilken port som används, protokoll (TCP/UDP), anslutningsstatus samt PID och tillhörande användare.


#### Filtrering efter IP Address eller port


Du kan förfina sökningarna genom att ange en IP Address och en port och på så sätt isolera ett visst nätverksflöde. Till exempel för att kontrollera en SMTP-session (port 25) med en specifik värd:


```bash
lsof -n -i @192.168.2.1:25
```


Detta visar endast aktiva nätverksanslutningar med värden `192.168.2.1` på port 25, vilket är användbart för att diagnostisera misstänkt aktivitet eller problem med SMTP-flödet.


#### Spårning av enhetsåtkomst


En annan styrka med `lsof` är spårning av specialfiler som t.ex. diskpartitioner. Till exempel, för att kontrollera vilka processer som har öppnat filer på `/dev/sda1`:


```bash
lsof /dev/sda1
```


Detta är praktiskt när ett avmonteringsförsök misslyckas eftersom enheten fortfarande används, eller när man undersöker vilka program som har åtkomst till en partition.


#### Korsanalys: process och nätverk


Alternativen kan kombineras för att ge exakta insikter. Du kan t.ex. se alla nätverksportar som öppnats av en process med PID 1521:


```bash
lsof -i -a -p 1521
```


Alternativet `-a` korsar kriterierna (`-i` och `-p`) och begränsar utdata till att endast omfatta nätverksanslutningar för den processen.


#### Spårning av flera användare


`lsof` kan också användas för att analysera aktiviteten hos specifika användare genom att lista alla filer som de har öppnat, eventuellt filtrerade efter PID:


```bash
lsof -p 1521 -u 500,phil
```


Detta visar de filer eller nätverksanslutningar som används av användaren `phil` eller UID 500, begränsad till process 1521.


### Sammanfattning av avsnittet


I detta sista avsnitt har vi utforskat ett brett spektrum av oumbärliga verktyg för att diagnostisera, analysera och administrera datornätverk. Denna studie är uppbyggd kring TCP/IP-modellens lager och klargör inte bara hur nätverkskommunikation fungerar, utan etablerar också en rigorös metodik för att identifiera, isolera och lösa potentiella problem.


Dessa verktyg ger administratörerna en sammanhängande uppsättning tekniska verktyg för att övervaka nätverkets hälsa, analysera trafik, granska anslutningar och snabbt ingripa mot felaktig utrustning eller felaktiga tjänster.


#### Nätverksåtkomst Layer


Verktyg som ger direkt insyn i gränssnitt och ramar:


- arp / ip neigh**: inspektera och modifiera ARP/NDP-cachen för att kontrollera eller korrigera IP-MAC-associationer;
- tcpdump**: paketinsamling på kommandoraden, filtrerbar och exporterbar;
- Wireshark**: grafisk paketanalys med djupgående protokollavkodning;
- ethtool**: fråga efter och justera Ethernet-kortets fysiska parametrar (hastighet, duplex, WoL, etc.).


#### Nätverk Layer


Verktyg för att bedöma IP-anslutning, routing och pakettrafik:


- ping**: testa nåbarhet och mät latenstid med ICMP;
- ip route**: inspektera och modifiera routingtabellen för att styra paketens väg;
- traceroute**: identifiering av routrar hopp för hopp längs vägen till en destination;
- ss**: detaljerad inventering av TCP/UDP-sockets och tillhörande processer (efterföljare till netstat).


#### Transport- och applikationslager


Verktyg för att diagnostisera tjänster och processer:


- nslookup / dig / host**: DNS-frågor för att validera namnmatchning och analysera poster;
- nmap**: utforska öppna portar och exponerade tjänster för att bedöma attackytan;
- lsof**: listar filer och uttag som öppnats av processer, vilket korrelerar system- och nätverksaktivitet.


Att behärska dessa verktyg, som vart och ett är anpassat till ett specifikt steg i TCP/IP-modellen, möjliggör ett metodiskt tillvägagångssätt: från den fysiska Layer, via routing och upp till applikationstjänster. Denna kedja av expertis ger administratörer möjlighet att diagnostisera, säkra och optimera sin infrastruktur, vilket säkerställer både nätverksprestanda och tillgänglighet.


# Sista delen


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Recensioner & betyg


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Slutlig examination


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Slutsats


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>