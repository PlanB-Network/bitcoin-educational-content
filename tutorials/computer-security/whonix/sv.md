---
name: Whonix
description: Bevara din integritet och konfidentialitet.
---

![cover](assets/cover.webp)



**Whonix** är en Linux-distribution baserad på **Debian**, utformad för att tillhandahålla en miljö som kombinerar **säkerhet**, **anonymitet** och **privacy**. Den är lätt att lära sig och kompatibel med olika gränssnitt (virtuella maskiner, Qubes OS, Live-läge) och innehåller som standard routning av nätverkstrafik via **Tor**, **dubbel brandvägg** (en brandvägg på Gateway och en annan på arbetsstationen), **fullt skydd mot IP/DNS-läckor** och verktyg för att effektivt maskera din aktivitet från nätverksobservatörer, inklusive din ISP. Mer än bara ett anonymt system är **Whonix** en komplett och säker utvecklingsmiljö.



## Varför välja Whonix?





- Gratis**: Som de flesta Linux-distributioner är Whonix ett system med öppen källkod som licensieras helt kostnadsfritt. Det utvecklas i öppen källkod med ett aktivt och öppet community.
- Integritet, säkerhet och anonymitet**: Whonix huvudmål är att erbjuda en extremt säker miljö, där alla dina uppgifter skyddas och din kommunikation krypteras via Tor-nätverket.
- Lätt att använda**: Whonix erbjuder en intuitiv, förkonfigurerad grafisk Interface, som passar även för nybörjare. Du behöver inte vara expert för att dra nytta av avancerat skydd.
- Idealisk miljö för säker utveckling**: Med Whonix kan du utveckla, testa, granska eller köra program utan att någonsin avslöja din riktiga IP Address eller avslöja dina surf- eller nätverkskommunikationsvanor.
- Engångssessioner och Live-läge**: Whonix kan startas i Live-läge eller via engångsmaskiner (t.ex. via **Qubes OS**), vilket gör att kritiska uppgifter kan utföras utan att lämna bestående spår när sessionen har avslutats.
- Relativt enkel installation**: Färdiga avbildningar levereras för snabb installation i virtuella maskiner (VirtualBox, KVM, Qubes). Systemet är dokumenterat och uppdateras regelbundet.



## Installation och konfiguration



Innan vi går vidare med installationen av Whonix är det viktigt att notera att den här distributionen ** ännu inte är officiellt tillgänglig** som ett huvudsystem som kan installeras direkt på Hard-disken (i bare metal-läge). Med andra ord kan du **inte ännu installera Whonix som ett klassiskt värdoperativsystem**, som Ubuntu eller standard Debian.



Det finns dock flera utgåvor som gör att Whonix kan användas **flyktigt** (Live-läge, tillfälliga sessioner) eller **beständigt** (via virtuella maskiner eller integration i Qubes OS).



För långsiktig, stabil användning är **virtualisering för närvarande den enda officiellt rekommenderade metoden**. Du kan köra Whonix med hjälp av **VirtualBox** (Whonix-Gateway och Whonix-Workstation) eller integrera det i ett system som **Qubes OS**. I den här handledningen fokuserar vi på en VirtualBox-installation.



### Förkunskapskrav



Innan du kan installera Whonix i virtuellt läge måste du se till att din maskin uppfyller de tekniska minimikraven. Virtualisering kräver vissa resurser som inte alla datorer kan erbjuda. Det är därför viktigt att din processor stöder virtualiseringsteknik (Intel VT-x eller AMD-V) och att detta alternativ är aktiverat i BIOS/UEFI.



Här är de rekommenderade specifikationerna för en smidig och stabil upplevelse med Whonix:





- Random Access Memory (RAM)**: minst **8 GB** rekommenderas starkt. Ju mer RAM-minne du har, desto mer resurser kan du tilldela de virtuella maskinerna (Gateway och Workstation), vilket förbättrar prestandan.
- Tillgängligt diskutrymme**: se till att det finns minst 30 GB ledigt diskutrymme**. Detta inkluderar det utrymme som krävs för de två virtuella maskinerna, systemfiler och eventuella data eller ögonblicksbilder.
- Processor**: en processor med minst **4 fysiska kärnor** (8 logiska trådar) rekommenderas, särskilt om du vill köra andra tjänster eller verktyg parallellt.



### Ladda ner Whonix



Whonix finns i flera olika utgåvor, beroende på vilken typ av miljö du vill använda det i. För de flesta användare (Windows, Linux eller MacOs) är VirtualBox-utgåvan den enklaste att installera. Du kan ladda ner bilden direkt från [den officiella webbplatsen] (https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **är inte kompatibel** med MacBooks som använder Apple Silicon-processorer (ARM-arkitektur).



## Installera VirtualBox



För att köra Whonix behöver du en **hypervisor** som VirtualBox, Qubes eller KVM.



När du har hämtat filen installerar du den på samma sätt som du installerar annan programvara. Acceptera standardalternativen om du inte har specifika krav. Är du vilse? Kolla in vår guide till hur du använder VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Importera Whonix



När VirtualBox har installerats kan du importera Whonix `.ova`-filer som du laddade ner tidigare (`Whonix-Gateway-Xfce.ova` och `Whonix-Workstation-Xfce.ova`).



Öppna VirtualBox och klicka sedan på **File → Import appliance**.


Välj motsvarande `.ova`-fil (börja med Gateway).



![0_03](assets/fr/03.webp)



Välj den plats där filerna för den virtuella Whonix-maskinen ska lagras.



![0_04](assets/fr/04.webp)



Acceptera användarvillkoren, starta sedan importen och vänta på att processen ska avslutas.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonix-konfiguration



Innan du börjar använda Whonix är det viktigt att du justerar vissa **systeminställningar** för att säkerställa bättre prestanda:



Välj den virtuella maskinen **Whonix-Workstation-Xfce** och klicka sedan på **Configuration**.



![0_06](assets/fr/07.webp)



Gå till fliken **System**, där RAM-minnet som standard är 2048 MB. Vi rekommenderar att du **ökar den till 4096 MB (4 GB)** för bättre flyt, särskilt om du tänker öppna flera program eller arbeta under långa sessioner. Gateway kan ligga kvar på 2048 MB, såvida du inte använder många Tor-anslutningar parallellt.



![0_08](assets/fr/08.webp)



### Komma igång med Whonix



För att Whonix ska fungera korrekt och säkert måste **du följa denna startsekvens**:



Starta först maskinen **Whonix-Gateway-Xfce**. Denna maskin är ansvarig för att dirigera all trafik genom **Tor**-nätverket. Utan gatewayen igång kommer ingen trafik att dirigeras via Tor och du kommer att förlora anonymiteten.



![0_09](assets/fr/09.webp)



När Gateway är helt igång (du ser att Tor är ansluten) kan du starta **Whonix-Workstation-Xfce**, som automatiskt ansluter via Gateway.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Uppdatering av systemet



Öppna terminalen och ange följande kommando för att uppdatera listan över paket:



```shell
sudo apt update
```



Kör sedan följande kommando för att installera de tillgängliga uppdateringarna:



```shell
sudo apt full-upgrade
```



## Upptäck Whonix



**Whonix** är ett system som är utformat för att ge en **säker**, **anonym** och **konfidentiell** datormiljö, perfekt för att surfa på Internet utan att kompromissa med din identitet eller dina data. För att uppnå detta finns det ett antal användbara vardagsapplikationer som är utformade för att förstärka din digitala säkerhet redan från början.


### KeepassXC



**KeePassXC** är Whonix integrerade lösenordshanterare. Med den kan du **skapa, lagra och hantera** dina lösenord på ett säkert sätt, utan att behöva komma ihåg dem manuellt. Lösenorden lagras i en **krypterad databas** som skyddas av ett huvudlösenord.



### Tor webbläsare



**Tor Browser** är Whonix standardwebbläsare. Den förlitar sig på **Tor**-nätverket, som omdirigerar din trafik genom flera reläer runt om i världen, vilket gör det praktiskt taget omöjligt att identifiera din riktiga IP Address.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Elektrum Bitcoin Wallet



**Electrum** är en lätt och snabb Bitcoin Wallet, förinstallerad på Whonix så att du kan hantera **transaktioner i kryptovaluta** anonymt. Den laddar inte ner hela Blockchain utan använder fjärrservrar för att få den nödvändiga informationen, vilket gör den mycket lättare än en fullständig Wallet.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix är mer än bara ett operativsystem: det är en äkta **säker miljö** som är utformad för att skydda din anonymitet, din integritet och dina känsliga aktiviteter. Tack vare sin Tor-baserade arkitektur, intelligenta partitionering mellan Gateway och Workstation och förinstallerade verktyg som Tor Browser, KeePassXC och Electrum, erbjuder Whonix en nyckelfärdig lösning för alla som vill **surfa anonymt**, **arbeta säkert** eller **hantera konfidentiella data**.



Om du vill stärka säkerheten i ditt Unix-system kan du läsa vår handledning om hur du granskar din maskin: leta efter säkerhetshål i operativsystemet och se till att dina data inte äventyras.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af