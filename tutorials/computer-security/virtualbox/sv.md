---
name: VirtualBox
description: Installera VirtualBox på Windows 11 och skapa din första virtuella dator
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian Burnel publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i originaltexten.*



___




## I. Presentation



I den här handledningen lär vi oss hur du installerar VirtualBox på Windows 11 för att skapa virtuella maskiner, oavsett om du kör Windows 10, Windows 11, Windows Server eller en Linux-distribution (Debian, Ubuntu, Kali Linux, etc.).



Denna inledande handledning till VirtualBox hjälper dig att komma igång med denna virtualiseringslösning med öppen källkod som utvecklats av Oracle och som är helt kostnadsfri. Senare kommer andra handledningar att läggas ut på nätet för att ta dig djupare in i ämnet.



När det gäller att virtualisera en arbetsstation, oavsett om det är för teständamål som en del av ett projekt eller under dina IT-studier, är VirtualBox helt klart en bra lösning. Det är också ett alternativ till andra lösningar som Hyper-V, som är integrerat i Windows 10 och Windows 11 (samt Windows Server), och VMware Workstation (avgiftsbelagd) / VMware Workstation Player (gratis för personligt bruk).



Min konfiguration: **en Windows 11-arbetsstation där jag ska installera VirtualBox**, men du kan installera VirtualBox på Windows 10 (eller en äldre version), liksom på Linux. När det gäller virtuella maskiner stöder VirtualBox ett brett utbud av system, inklusive Windows (t.ex. Windows 10, Windows 11, Windows Server 2022, etc.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, etc.), BSD (PfSense) och macOS.



## II. Ladda ner VirtualBox för Windows 11



För att ladda ner VirtualBox för installation på en Windows-maskin finns det bara en bra Address: den [officiella VirtualBox-webbplatsen] (https://www.virtualbox.org/wiki/Downloads) i avsnittet "**Downloads**". Klicka bara på "Windows hosts" för att börja ladda ner den här körbara filen, som är drygt 100 MB stor.



![Image](assets/fr/025.webp)



## III. Installera VirtualBox på Windows 11



### A. Installera VirtualBox



Installationen av VirtualBox** är enkel och processen är densamma för alla versioner av Windows. Börja med att starta den körbara filen för VirtualBox som du just har laddat ner och klicka sedan på "**Nästa**".



![Image](assets/fr/026.webp)



Denna installation är anpassningsbar, men jag rekommenderar att du installerar alla funktioner: vilket är fallet med standardvalet. I bilden nedan kan du se olika Elements, inklusive :





- VirtualBox USB Support** för att aktivera stöd för USB-enheter i VirtualBox
- VirtualBox Bridged Network** för att integrera nätverksstöd i "Bridge"-läge (den virtuella maskinen kan ansluta direkt till ditt lokala nätverk)
- VirtualBox Host-Only Network** för att integrera nätverksstöd i läget "Host-Only" (den virtuella maskinen kan bara kommunicera med din fysiska Windows 11-värd och andra virtuella maskiner i det här läget)



Klicka på "**Nästa**" för att fortsätta.



![Image](assets/fr/001.webp)



Klicka på "**Yes**" och tänk på att **nätverket kommer att avbrytas för ett ögonblick på din Windows 11-maskin**, medan VirtualBox utför nätverksmodifieringar för att stödja olika nätverkstyper, inklusive Bridge-läge.



![Image](assets/fr/002.webp)



När du har bekräftat kommer installationen att starta... Och ett meddelande "**Vill du installera den här enhetens programvara? **" visas. Markera alternativet "**Lita alltid på programvara från Oracle Corporation**" och klicka på "**Installera**". VirtualBox behöver faktiskt installera flera drivrutiner på din dator.



![Image](assets/fr/003.webp)



Installationen är nu klar! Markera alternativet "**Starta Oracle VM VirtualBox 6.1.34 efter installationen**" och klicka på "**Klicka**" för att starta programvaran.



![Image](assets/fr/004.webp)



### B. Lägg till tilläggspaketet



Fortfarande på den officiella VirtualBox-webbplatsen (se föregående länk) kan du ladda ner ett officiellt tilläggspaket, tillgängligt under avsnittet "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" genom att klicka på länken "**All supported platforms**". Detta paket gör att du kan lägga till ytterligare funktioner i VirtualBox: det är inte obligatoriskt att lägga till det, men det kan vara användbart! Det innehåller t.ex. stöd för USB 3.0 i virtuella datorer, stöd för webbkamera och diskkryptering.



Öppna VirtualBox, klicka på "**File**" och sedan på "**Settings**" i menyn.



![Image](assets/fr/005.webp)



Klicka på "**Extensions**" till vänster (1) och sedan på knappen "**+**" till höger (2) för att **ladda det VirtualBox**-tilläggspaket som du just har laddat ner (3).



![Image](assets/fr/006.webp)



Bekräfta genom att klicka på knappen "**Installation**".



![Image](assets/fr/007.webp)



Klicka på "**OK**": det officiella tilläggspaketet är nu installerat på din VirtualBox-instans!



![Image](assets/fr/008.webp)



Låt oss gå vidare till skapandet av vår första virtuella maskin.



## IV. Skapa din första VirtualBox VM



För att skapa en ny virtuell maskin på VirtualBox klickar du bara på knappen "**New**" för att starta guiden för VM-skapande. Eftersom det här är första gången du startar VirtualBox vill jag ge dig lite mer information om Interface och de andra knapparna.





- Inställningar**: allmän konfiguration av VirtualBox (standardmapp för virtuella datorer, uppdateringshantering, språk, NAT-nätverk, tillägg etc.)
- Import**: importera en virtuell appliance i OVF-format
- Export**: exportera en befintlig virtuell maskin i OVF-format för att skapa en virtuell appliance
- Lägg till**: lägg till en befintlig virtuell maskin i din VirtualBox-inventering, i standard VirtualBox-format (.vbox) eller XML-format



Till vänster ger avsnittet "**Tools**" tillgång till **avancerade funktioner, särskilt för hantering av det virtuella nätverket, men också för hantering av VM-lagring**. Under posten "**Tools**" kommer dina virtuella maskiner att läggas till senare.



![Image](assets/fr/009.webp)



### A. Process för skapande av virtuell dator



**Som en påminnelse stöder VirtualBox en mängd olika operativsystem, inklusive Windows, Linux och BSD. I det här exemplet ska jag skapa en virtuell maskin för Windows 11. Flera fält måste fyllas i:





- Namn**: namn på den virtuella maskinen (detta är det namn som kommer att visas i VirtualBox)
- Maskinmapp**: var den virtuella maskinen ska lagras, eftersom en undermapp med VM:ns namn kommer att skapas på denna plats
- Typ**: typ av operativsystem, beroende på vilket operativsystem du vill installera
- Version**: versionen av det system du vill installera, i det här fallet Windows 11, så "**Windows11_64**"



Klicka på "**Nästa**" för att fortsätta.



![Image](assets/fr/010.webp)



Beroende på vilket operativsystem du väljer i föregående steg ger **VirtualBox rekommendationer om vilka resurser som ska allokeras till den virtuella maskinen**. Här talar vi om RAM-minnet som du vill tilldela VM. Låt oss anta 4 GB, eftersom detta verkligen rekommenderas för Windows 11, men om du har ont om resurser, ange 2 GB istället. ** Fortsätt



**Anmärkning**: De resurser som tilldelas den virtuella maskinen kan ändras senare.



![Image](assets/fr/011.webp)



När det gäller den virtuella Hard-disken börjar vi från noll, så vi måste välja "**Create virtual Hard disk now**" så att den virtuella datorn har lagringsutrymme för att installera operativsystemet och lagra data. Klicka på "**Create**".



![Image](assets/fr/012.webp)



VirtualBox stöder tre olika format för virtuella Hard-diskar, vilket är en stor skillnad jämfört med andra lösningar som VMware och Hyper-V. Det finns tre format att välja mellan:





- VDI**, det officiella VirtualBox-formatet
- VHD**, som är det officiella Hyper-V-formatet, även om det nya VHDX-formatet används oftare nuförtiden
- VMDX** är det officiella VMware-formatet för både VMware Workstation och VMware ESXi



Om du vill skapa en virtuell maskin som bara ska användas i den här VirtualBox-instansen väljer du "**VDI**". Om den virtuella Hard-disken däremot ska anslutas till en Hyper-V-värd vid ett senare tillfälle kan det vara en bra idé att börja med VHD-formatet för att slippa konvertera den. Klicka på "**Nästa**".



![Image](assets/fr/013.webp)



**Den virtuella disken kan vara antingen dynamisk eller ha en fast storlek**. När den är dynamisk kommer filen som representerar **den virtuella disken (här en .vdi-fil) att växa när data skrivs till disken** tills den når sin maximala storlek, men den kommer inte att krympa om data raderas. Om den däremot är av fast storlek allokeras **det totala lagringsutrymmet omedelbart (och reserveras därför)**, vilket ger något högre prestanda, men tar längre tid när den virtuella disken först skapas.



För test av virtuella maskiner med VirtualBox anser jag personligen att läget "**Dynamiskt allokerad**" är tillräckligt.



![Image](assets/fr/014.webp)



**Nästa steg är att ange storleken på den virtuella disken**, med tanke på att disken som standard kommer att lagras i VM-katalogen (detta kan ändras i detta skede). Jag har angett en storlek på 64 GB för att uppfylla kraven i Windows 11, men även här kan en mindre storlek tilldelas. Klicka på "**Create**" för att skapa VM!



![Image](assets/fr/015.webp)



Vid den här tidpunkten finns den virtuella datorn i vårt lager, den är konfigurerad, men operativsystemet är inte installerat. Vi måste slutföra konfigurationen av den virtuella datorn innan vi startar upp den.



### B. Tilldela en ISO-avbildning till en VirtualBox VM



För att installera Windows 11, eller något annat system, behöver vi installationskällor. I de flesta fall använder vi en diskavbildning i ISO-format för att installera ett operativsystem. **Det är nödvändigt att ladda Windows 11 ISO-avbildningen i vår virtuella VM: s virtuella DVD-enhet



Klicka på den virtuella maskinen i VirtualBox-inventeringen (1) och sedan på knappen "**Configuration**" (2), som ger åtkomst till den allmänna konfigurationen av den virtuella maskinen. Denna meny används för att hantera resurser (t.ex. öka RAM, konfigurera CPU, etc.). Klicka på "**Storage**" till vänster (3), på DVD-enheten där det står "**Empty**" för tillfället (4) och klicka sedan på den DVD-formade ikonen (5) och "**Choose a disk file**".



![Image](assets/fr/016.webp)



Välj ISO-imagen för det operativsystem du vill installera och klicka sedan på OK. Det här är vad jag får fram:



![Image](assets/fr/017.webp)



Stanna kvar i avsnittet "**Konfiguration**" i VM, jag har fortfarande några saker att förklara.



### C. VM-nätverksanslutning



Gå till avsnittet "**Nätverk**" till vänster. I det här avsnittet kan du hantera den virtuella maskinens nätverk: antal virtuella nätverksgränssnitt (upp till 4 per VM), MAC Address och nätverksåtkomstläge (NAT, bridge access, internt nätverk etc.). **Om du vill att din virtuella maskin ska ha tillgång till Internet väljer du "NAT" eller "Bridge Access"**, men det här andra läget kräver att en DHCP-server är aktiv i ditt nätverk, annars måste du konfigurera en IP Address manuellt.



Obs: Jag kommer att återkomma till nätverksdelen mer i detalj i en särskild artikel.



![Image](assets/fr/018.webp)



### D. Antalet virtuella processorer



Precis som en fysisk dator behöver en virtuell maskin RAM-minne, en Hard-disk och en processor för att fungera. När vi skapade den virtuella datorn kanske du märkte att guiden inte innehöll någon processorkonfiguration. Denna kan dock konfigureras när som helst via fliken "**System**", sedan "**Processor**", där du kan välja antalet virtuella processorer.



Observera: alternativet "**Enable VT-x/AMD-v nested**" krävs för nested virtualisering.



I mitt fall har den virtuella maskinen 2 virtuella processorer:



![Image](assets/fr/019.webp)



**Tveka inte att ta en titt på de andra avsnitten i konfigurationsmenyn.



### E. Första start och OS-installation



För att starta en virtuell maskin markerar du den i inventarieförteckningen och klickar på knappen "**Start**". Ett nytt fönster öppnas och ger en visuell översikt över den virtuella datorn.



![Image](assets/fr/020.webp)



Ouch, jag får ett otäckt fel och min virtuella maskin startar inte! Felet är "Inloggning misslyckades för virtuell maskin ..." med följande detaljer:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Detta är faktiskt normalt eftersom **virtualiseringsfunktionen inte är aktiverad på min dator**! För att åtgärda detta problem måste du starta om datorn för att komma åt BIOS och aktivera virtualisering.



![Image](assets/fr/021.webp)



Utan att vänta startar jag om datorn och **trycker på "SUPPR"-tangenten för att komma åt BIOS** (tangenten kan variera beroende på maskin och kan t.ex. vara F2) på mitt ASUS-moderkort. För att aktivera virtualisering måste "SVM Mode" vara aktiverat i mitt fall. Här igen, från ett moderkort till ett annat, från en tillverkare till en annan, kan namnet ändras. Leta efter en funktion som hänvisar till **AMD-V** (för en AMD CPU) eller **Intel VT-x** (för en Intel CPU).



![Image](assets/fr/022.webp)



När detta är gjort, spara ändringen och starta om den fysiska maskinen ... Den här gången kan **VirtualBox starta den virtuella maskinen** och ladda Windows ISO-bilden för att installera operativsystemet! 🙂



![Image](assets/fr/023.webp)



På vår fysiska Windows 11-värd, där VirtualBox är installerat, kan vi se att mappen för den virtuella Windows 11-maskinen innehåller olika filer.





- VBOX**-filen (i XML-format) som motsvarar VM-konfigurationen (RAM, CPU, etc.)
- Filen VBOX-PREV** är en säkerhetskopia av den tidigare konfigurationen
- VDI**-filen motsvarar den virtuella Hard-disken i dynamiskt läge, så den är för närvarande bara 13 GB, medan den maximala storleken är 64 GB
- NVRAM**-filen innehåller BIOS-tillståndet för den virtuella maskinen, vilket motsvarar det icke-flyktiga minnet i en fysisk maskin



![Image](assets/fr/024.webp)



## V. Slutsats



**VirtualBox är nu igång på vår fysiska Windows 11-maskin! Allt som återstår är att dra nytta av det och skapa virtuella maskiner!** Jag kommer tillbaka till att installera Windows 11 i en VirtualBox VM i en annan artikel. För Windows 10, Windows Server eller en Linux-distribution (Ubuntu, Debian, etc.), låt oss bara guida dig!