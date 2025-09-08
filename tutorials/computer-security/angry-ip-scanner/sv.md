---
name: Angry IP Scanner
description: Ett enkelt sätt att skanna ditt nätverk
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian BURNEL publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i originaltexten.*



___



## I. Presentation



Hur skannar man snabbt och enkelt ett Windows-nätverk efter anslutna maskiner? Svaret är Angry IP Scanner. Med detta open source-projekt kan du enkelt skanna ett nätverk med hjälp av en lättanvänd grafisk Interface.



Det här verktyget kan användas av privatpersoner för att **skanna sitt lokala nätverk**, men också av IT-proffs för samma ändamål. Ett bevis på att **det här verktyget är mycket praktiskt** är att det redan har använts av **vissa cyberkriminella grupper** för att skanna företagsnätverk (på samma sätt som Nmap). Ett bra exempel är [ransomware-gruppen RansomHub] (https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Det är fortfarande en bra programvara, men som med andra nätverks- och säkerhetsorienterade verktyg kan dess användning missbrukas.



Här kommer vi att använda det på **Windows 11**, men det är fullt möjligt att använda det på andra versioner av **Windows**, liksom på **Linux** och **macOS**.



**Angry IP** Scanner är mindre omfattande än Nmap, men är ändå intressant för en snabb, grundläggande nätverksanalys, men också för att den är inom räckhåll för alla. Den kommer att **detektera värdar som är anslutna till nätverket** och identifiera **hostnamn** och **öppna portar**.



Om du vill gå vidare kan du läsa handledningen om Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Komma igång med Angry IP Scanner



### A. Ladda ner och installera Angry IP Scanner



Du kan ladda ner den senaste versionen av Angry IP Scanner från applikationens officiella webbplats eller från GitHub. Vi kommer att använda det senare alternativet. Klicka på länken nedan och ladda ner EXE-versionen: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Kör den körbara filen för att fortsätta med installationen. Det finns inget speciellt att göra under installationen.



![Image](assets/fr/013.webp)



### B. Kör en inledande nätverksskanning



Ta dig tid att läsa instruktionerna i fönstret "**Getting Started**" vid första starten för att lära dig mer om hur verktyget fungerar. Förresten finns det flera termer att tänka på:





- Feeder**: modul som genererar listor med IP-adresser som ska skannas, från ett slumpmässigt IP-intervall eller en fil med en lista med IP-adresser.
- Fetcher**: en uppsättning moduler för att hämta information om värdar i nätverket. Det finns t.ex. fetchers för att upptäcka MAC-adresser, skanna portar, upptäcka värdnamn eller skicka HTTP-begäranden.



![Image](assets/fr/018.webp)



För att skanna ett IP-subnät anger du helt enkelt **start IP Address** och **slut IP Address** i fältet "**IP range**" (annars ändrar du typen till höger). Klicka sedan på knappen "**Start**".



![Image](assets/fr/019.webp)



Några tiotals sekunder senare kommer resultatet att synas i programvarans Interface. **För varje IP Address i det analyserade intervallet ser du om Angry IP Scanner har upptäckt en värd eller ej.** En sammanfattning visas också på skärmen och anger antalet aktiva värdar (i det här fallet 6) och antalet värdar med öppna portar.



![Image](assets/fr/020.webp)



Här kan vi se att det finns en värd med namnet "**OPNsense.local.domain**", associerad med IP Address "**192.168.10.1**" och tillgänglig på **port 80** och **443** (HTTP och HTTPS). Om du högerklickar på värden får du tillgång till ytterligare kommandon, t.ex. ping, trace route och webbläsaröppning via denna IP Address.



![Image](assets/fr/012.webp)



### C. Lägg till skanningsportar



Som standard kommer **Angry IP Scanner** att skanna 3 portar: **80** (HTTP), **443** (HTTPS) och **8080**. Du kan lägga till fler portar som ska skannas från programmets inställningar. Klicka på menyn "**Tools**" och sedan på fliken "**Ports**".



Här kan du ändra portlistan via alternativet "**Port selection**". Du kan **ange specifika portnummer åtskilda av ett kommatecken eller portintervall**. I exemplet nedan läggs två portar till: **445** (SMB) och **389** (LDAP). Om du vill skanna portar från 1 till 1000 anger du "**1-1000**". Det anges inte om portskanningen ska utföras i TCP, UDP eller båda.



![Image](assets/fr/021.webp)



Om du kör skanningen igen kommer du sannolikt att få ny information. I exemplet nedan berättar Angry IP Scanner att portarna 389 och 445 är öppna på värdarna "**SRV-ADDS-01**" och "**SRV-ADDS-02**", tack vare den nya konfigurationen av portar som ska skannas.



![Image](assets/fr/022.webp)



**Anmärkning**: Från menyn "**Scanner**" kan du exportera scanningsresultat till en textfil.



Om du vill gå vidare med skanningen kan du klicka på menyn "**Tools**" och sedan på "**Fetchers**". Detta lägger till "förmågor" till skanningen. Välj helt enkelt en fetcher och flytta den till vänster för att aktivera den. Detta kommer att lägga till en extra kolumn i skanningsresultatet.



![Image](assets/fr/014.webp)



I exemplet nedan visas funktionerna "**NetBIOS info**" och "**Web detection**". Den förstnämnda ger ytterligare information, t.ex. maskinens MAC Address och domännamn, medan den sistnämnda visar webbsidans titel (som kan ge en indikation på vilken typ av webbserver eller applikation det är).



![Image](assets/fr/011.webp)



Slutligen kan du i inställningarna också ändra den metod som används för "**ping**", dvs. för att avgöra om en värd är aktiv eller inte. Eftersom vissa värdar inte svarar på pingar kan du prova andra metoder (UDP-paket, TCP port probe, ARP, UDP + TCP kombination, etc.)



## III. Slutsatser



Enkelt och effektivt: Angry IP Scanner upptäcker värdar som är anslutna till ett nätverk och låter dig konfigurera portskanningar. När det gäller alternativ är det inte lika flexibelt som Nmap och går inte lika långt, men det är en bra start för snabb skanning.



Om du vill använda **Nmap** med en grafisk Interface kan du använda **Zenmap-applikationen** (se översikt nedan).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d