---
name: Start9

description: Handledning om att sätta upp en privat Start9-server

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Här är en videohandledning från Southern Bitcoiner, en videoguide som visar hur du ställer in och använder en Start9 / StartOS personlig server, och hur du kör en bitcoin-nod.*


## 1️⃣ Introduktion


### Vad är egentligen Start9?


Start9 är ett företag som grundades 2020, mest känt för att ha utvecklat [**StartOS**,](https://github.com/Start9Labs/start-os) ett Linux-baserat operativsystem utformat för personliga servrar. Det gör det möjligt för användare att enkelt själva vara värd för ett brett utbud av programvarutjänster - till exempel Bitcoin och Lightning-noder, meddelandeappar eller lösenordshanterare - samtidigt som de behåller full kontroll över sina data och eliminerar beroendet av centraliserade tekniska plattformar. StartOS har ett användarvänligt, webbläsarbaserat gränssnitt, en marknadsplats för installation av tjänster och inbyggda integritetsverktyg som Tor-integration och systemomfattande HTTPS-kryptering. Start9 tillhandahåller också hårdvaruenheter som är förinstallerade med operativsystemet, men programvaran kan installeras på kompatibel hårdvara eller virtuella maskiner (VM).


### Vilka alternativ finns att tillgå?


Start9 erbjuder både förbyggda alternativ och DIY-alternativ. [**Server One**](https://store.start9.com/collections/servers/products/server-one) och [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) är officiella hårdvaruenheter med högpresterande komponenter: Server One använder en **AMD Ryzen 7 5825U**-processor med konfigurerbart RAM-minne (16 GB-64 GB) och lagringsutrymme (2 TB-4 TB NVMe SSD), medan Server Pure är utrustad med en **Intel i7-10710U**, som också erbjuder konfigurerbara RAM-minne- och lagringsalternativ. Båda inkluderar **livstids teknisk support** när de köps direkt från Start9. För användare som föredrar flexibilitet kan StartOS installeras gratis på ett brett utbud av befintlig hårdvara, inklusive bärbara datorer, stationära datorer, minidatorer och enkortsdatorer, eller i virtuella datorer.


![image](assets/en/01.webp)


### Vilka är skillnaderna mot Umbrel?


StartOS och Umbrel förenklar båda installationen av tjänster på egen hand, men skiljer sig åt i fråga om arkitektur och funktioner. Umbrel fungerar som ett applikationslager på Debian/Ubuntu-system eller virtuella datorer, medan Start9 är ett dedikerat operativsystem som kräver direkt installation av hårdvara eller virtuell dator. Umbrel har ett polerat, macOS-inspirerat gränssnitt, medan Start9 prioriterar en funktionell, minimal design. Umbrel erbjuder ett större [urval av applikationer](https://apps.umbrel.com/), medan [Start9 Marketplace](https://marketplace.start9.com/) kompenserar med avancerade tekniska funktioner. Start9 förenklar åtkomsten till avancerade inställningar genom validerade användargränssnittsformulär, vilket minskar behovet av kommandoradsinteraktion. Det utmärker sig också i säkerhetskopieringshantering med krypterade systembackuper med ett klick, en funktion som Umbrel saknar inbyggt. StartOS tillhandahåller inbyggda övervakningsverktyg och tillämpar HTTPS-kryptering för lokal nätverksåtkomst, vilket förbättrar säkerheten. Umbrel använder okrypterad HTTP lokalt, även om båda plattformarna stöder säker fjärråtkomst via Tor. Umbrel är lämplig för användare som prioriterar ett rikt ekosystem av appar och ett polerat användargränssnitt. Start9 är ett starkt val för dem som värdesätter säkerhet, konfigurerbarhet, tillförlitlig säkerhetskopiering och avancerad tjänstehantering utan att kräva kommandoradsexpertis. För att lära dig mer om Umbrel och skillnaderna mot Start9, besök den här kursen:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ Förutsättningar för DIY: Minsta och rekommenderade specifikationer


För grundläggande användning med minimala tjänster är **minimumspecifikationerna**: **1 vCPU-kärna (2,0 GHz + boost), 4 GB RAM, 64 GB lagringsutrymme** och en Ethernet-port. Med det sagt skulle jag rekommendera att gå långt utöver det, särskilt om du kör en Bitcoin-nod. Personligen började jag med 1 TB och fick snabbt slut på utrymme. Det är bättre att sikta på **minst 2TB lagring**, tillsammans med en **quad-core CPU (2,5 GHz+)** och **8GB+ RAM**. Det gör en enorm skillnad i prestanda och livslängd. Om du vill dyka djupt, här är en uppdaterad communitytråd om [Hårdvara som kan köra StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Nedladdning och flashning av firmware


För att påbörja installationen, använd en separat dator för att besöka [Start9-webbplatsen](https://start9.com/), och navigera till dokumentationsavsnittet genom att klicka på `DOCS`. Gå sedan till `Flashing Guides` för att hitta rätt version av StartOS. Två alternativ finns tillgängliga:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Denna handledning behandlar alternativet `x86/ARM`.


Den senaste OS-versionen kan laddas ner från [Github release page](https://github.com/Start9Labs/start-os/releases/latest). [Pre-release](https://github.com/Start9Labs/start-os/releases) versioner är också tillgängliga för användare som vill testa nya funktioner. Längst ner på sidan, under `Assets`, hämtar du `x86_64` eller `x86_64-nonfree.iso`.  Bilden `x86_64-nonfree.iso` innehåller icke-fri (sluten källkod) programvara som krävs för Server One och de flesta DIY-maskinvarorna, särskilt för grafik och stöd för nätverksenheter.


Vi rekommenderar att du verifierar filens integritet genom att kontrollera dess SHA256-hash mot den som anges på GitHub. För Linux kan kommandot `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso` användas, medan andra operativsystem behandlas i dokumentationen.


Efter nedladdning och verifiering av StartOS-imagen måste den flashas till en USB-enhet. `BalenaEtcher` är en rekommenderad programvara för denna uppgift. Det är ett gratis verktyg med öppen källkod för att skriva OS-bildfiler till USB-enheter och SD-kort, tillgängligt för Windows, macOS och Linux. Ladda ner rätt version från den officiella [Balena Etcher-webbplatsen](https://www.balena.io/etcher/) och kör installationsprogrammet. Anslut mål-USB-enheten eller SD-kortet, öppna Balena Etcher och klicka på "Flash from file" för att välja den nedladdade OS-bilden. Etcher kommer automatiskt att upptäcka anslutna enheter; välj rätt mål om flera är närvarande. Klicka på `Flash!` för att börja skriva avbildningen. Etcher validerar automatiskt skrivprocessen när den är klar. När du är klar kan du ta bort enheten på ett säkert sätt och använda den för att starta enheten.


![image](assets/en/19.webp)


## 4️⃣ Initial inställning


För den första installationen, se sidan Start9 [documentation](https://docs.start9.com/0.3.5.x/) under `USER MANUAL` följt av `Getting Started - Initial Setup`.  Denna officiella handbok bör konsulteras för att få den senaste informationen.


Två alternativ presenteras:



- Börja om på nytt
- Alternativ för återställning


För en ny serverinstallation väljer du `Start Fresh`. Anslut först servern till ström och en Ethernet-kabel. Kontrollera att den dator som används för installationen finns i samma lokala nätverk. Ta ut den nyligen flashade USB-enheten från datorn och sätt in den i servern.


Du kan fjärrstyra servern från vilken dator som helst i samma nätverk. Öppna en webbläsare och navigera till `http://start.local`.


**Notera**: Om det uppstår anslutningsproblem med den här adressen beror det ofta på att hemmanätverk inte kan lösa domännamnet `.local`. Problemet kan lösas genom att man går direkt till servern via dess IP-adress. IP-adressen hittar du genom att logga in på routerns administratörsgränssnitt (vanligtvis på `192.168.1.1` eller en liknande adress) och leta reda på enheten i listan över DHCP-klienter eller nätverkskartor. Ange sedan den fullständiga IP-adressen (t.ex. `http://192.168.1.105`) i webbläsaren. Detta förbigår DNS-upplösningen. Om problemen kvarstår, se sidan [Vanliga problem](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) eller [kontakta deras support](https://start9.com/contact/)


StartOS-inställningsskärmen bör visas. Klicka på `Start Fresh` för att påbörja installationen av den nya servern.


![image](assets/en/03.webp)


Nästa steg är att välja den lagringsenhet där StartOS-data ska lagras.


![image](assets/en/04.webp)


Ange ett starkt `Lösenord` för servern. Spela in det enligt anvisningarna från Start9 och klicka sedan på `FINISH`.


![image](assets/en/05.webp)


En skärm kommer att visa att StartOS initierar och konfigurerar servern. Nästa steg är att `Ladda ner adressinformation` eftersom adressen `start.local` endast är för installationssyfte och inte kommer att fungera efteråt.


![image](assets/en/06.webp)


Konfigurationsfilen innehåller två kritiska åtkomstadresser: en för det "lokala nätverket (LAN)" och en för säker åtkomst via "Tor". Båda adresserna bör sparas i en säker lösenordshanterare. Nästa steg är att "lita på din rotcertifikatutfärdare". Öppna en ny webbläsarflik och följ instruktionerna för att lita på rotcertifikatutfärdaren och logga in. Root CA-certifikatet kan också laddas ner genom att klicka på `Download certificate` i den nedladdade filen.


## 5️⃣ Lita på din Root CA


Efter att certifikatet har laddats ned måste serverns `Root CA` vara betrodd av operativsystemet. Klicka på "Visa instruktioner" och hitta riktlinjerna för det specifika operativsystemet.


![image](assets/en/07.webp)


För ett Linux-system används följande kommandon. Öppna först en terminal och installera de nödvändiga paketen:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Navigera till den katalog där certifikatet hämtades, vanligtvis `~/Downloads` . Utför dessa kommandon för att lägga till certifikatet i operativsystemets förtroendelager. Byt till nedladdningsmappen med `cd ~/Downloads`. Skapa den katalog som krävs med `sudo mkdir -p /usr/share/ca-certificates/start9`. Kopiera certifikatfilen och ersätt "ditt filnamn.crt" med det faktiska filnamnet med hjälp av "sudo cp "ditt filnamn.crt" /usr/share/ca-certificates/start9/". Registrera certifikatet permanent genom att lägga till dess sökväg till systemkonfigurationen med `sudo bash -c "echo 'start9/ditt-filnamn.crt' >> /etc/ca-certificates.conf"`. Slutligen bygger du om förtroendelagret med `sudo update-ca-certificates`. Det är viktigt att du använder det faktiska certifikatfilnamnet och verifierar alla sökvägar innan du utför dessa kommandon. Denna process etablerar permanent förtroende för Start9-serverns HTTPS-anslutningar.


En lyckad installation kommer att indikeras av ett utdata som säger `1 added`. De flesta applikationer kommer då att kunna ansluta säkert via `https`. Om du använder Firefox krävs ytterligare ett [sista steg](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). För Chrome eller Brave krävs ett annat [sista steg](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) för att konfigurera webbläsaren så att den respekterar rotcertifikatutfärdaren. Testa anslutningen genom att uppdatera sidan. Om problemet kvarstår ska du stänga och öppna webbläsaren igen innan du besöker sidan igen.


![image](assets/en/08.webp)


## 6️⃣ Komma igång med StartOS


Det bör nu vara möjligt att logga in med hjälp av en säker HTTPS-anslutning. Ange `Lösenord` för att komma till `Välkomstskärmen`.


![image](assets/en/09.webp)


På den här skärmen finns användbara genvägar för att komma igång. Det vänstra sidofältet innehåller huvudmenyalternativen för navigering.


## 7️⃣ System


Fliken System i StartOS ger tillgång till centrala systemfunktioner för hantering av den personliga servern. Här finns verktyg för systemunderhåll, säkerhet, diagnostik och konfiguration utan att det krävs kunskaper om kommandoraden.


Avsnittet "Backups" gör det möjligt att skapa säkerhetskopior av hela systemet, inklusive tjänster, konfigurationer och data, som kan återställas senare. Detta är viktigt för katastrofåterställning eller migrering till ny maskinvara. Säkerhetskopiorna kan lagras på externa hårddiskar och krypteras med hjälp av huvudlösenordet.


Avsnittet "Hantera" på fliken System ger kontroll över viktiga systemfunktioner. Användare kan manuellt söka efter och tillämpa StartOS-uppdateringar och på så sätt behålla kontrollen över systemets uppdateringsprocess. Det är möjligt att sidoladda anpassade tjänster eller tjänster från tredje part som inte finns tillgängliga på den officiella marknaden. Om servern inte är ansluten via Ethernet kan Wi-Fi-inställningar konfigureras från det här avsnittet. Avancerade användare kan aktivera SSH-åtkomst för systemhantering på terminalnivå.


![image](assets/en/10.webp)


Avsnittet "Insikter" ger realtidsövervakning av serverns prestanda och hälsa och visar CPU-, RAM- och diskanvändning i form av grafer. Här visas också systemtemperaturen, vilket är användbart för enheter som Raspberry Pi som saknar aktiv kylning. Mätvärden för drifttid och genomsnittlig belastning hjälper till att bedöma systemets stabilitet, och live-loggar finns tillgängliga för felsökning av service- eller systemproblem.


I avsnittet "Support" finns tillgång till inbyggda vanliga frågor, officiell dokumentation och supportkanaler i communityt. Felsökningsloggar kan laddas ner från detta avsnitt för att delas med Start9-support för snabbare problemlösning.


![image](assets/en/11.webp)


## 8️⃣ Marknadsplats


Marknadsplatsen används för att upptäcka, installera och hantera tjänster på den personliga servern. Den ger tillgång till programvara som Bitcoin Core, BTCPay Server och electrs. StartOS stöder flera marknadsplatser, inklusive det officiella Start9-registret och community-drivna register. Dessa kan läggas till genom att klicka på `CHANGE` och byta till `Community Registry`, som ger tillgång till ett bredare utbud av tjänster.


![image](assets/en/12.webp)


## 9️⃣ Installera en Bitcoin Full Node


Att installera en Bitcoin full node på StartOS ger full suveränitet över Bitcoin-upplevelsen. Det möjliggör validering av transaktioner och förbättrar integriteten och säkerheten genom att ta bort beroendet av externa tjänster som kan logga aktiviteter. Full kontroll över transaktioner erhålls, vilket gör att de kan sändas direkt till nätverket. Standardalternativet är `Bitcoin Core`, som integreras nativt med StartOS och möjliggör anslutning till plånböcker som Specter, Sparrow eller Electrum för en självförvaringsinställning. Ett alternativ, `Bitcoin Knots`, är också tillgängligt via Community Registry.


För att installera Bitcoin Core, navigera till Marketplace. Under standardregistret hittar du och installerar Bitcoin Core-tjänsten. Efter installationen visas en uppmaning om "Needs Config" som kräver att inställningarna slutförs innan tjänsten kan köras. Detta inträffar vanligtvis efter uppdateringar eller nya installationer och uppmanar till en granskning av `RPC-inställningar`. Fortsätt med standardkonfigurationen och klicka på `Save`.


![image](assets/en/13.webp)


När din nod är helt synkroniserad kan den fungera som en privat backend för plånböcker som Sparrow, vilket ger ökad integritet och transaktionsvalidering. För användare som lagrar betydande belopp är det dock viktigt att förstå säkerhetsavvägningarna för denna direktanslutning. När en wallet ansluter direkt till Bitcoin Core kan den exponera känslig data, eftersom Bitcoin Core lagrar offentliga nycklar (xpubs) och wallet-saldon okrypterade på värdmaskinen. Ett komprometterat system kan göra det möjligt för en angripare att upptäcka dina innehav och rikta in sig på dig.


För att mildra denna risk och uppnå en mer robust säkerhetsmodell kan du skapa en Private Electrum Server. Den här servern fungerar som en mellanhand och indexerar blockkedjan utan att lagra någon wallet-specifik information. Genom att ansluta din wallet till din egen Electrum-server istället för direkt till Bitcoin Core, förhindrar du att wallet får tillgång till nodens känsliga data.


![image](assets/en/14.webp)


## 🔟 Sätta upp elektriker


`electrs` (Electrum Rust Server) är en snabb, effektiv indexerare som ansluter till din Bitcoin Core-nod och gör det möjligt för Electrum-kompatibla plånböcker att fråga om transaktionshistorik och saldon i realtid. Genom att köra electrs på StartOS eliminerar du beroendet av Electrum-servrar från tredje part, vilket avsevärt förbättrar integriteten och säkerheten - dina wallet-frågor går direkt till din självhostade nod.


För att ställa in det installerar du först electrs-tjänsten från StartOS Marketplace. Systemet kommer att kräva att Bitcoin Core synkroniseras helt innan du fortsätter. Efter installationen bekräftar du inställningarna för `Needs Config` med de rekommenderade standardvärdena och electrs börjar indexera blockchain, vilket kan ta upp till en dag beroende på din hårdvara.


![image](assets/en/15.webp)


När du är klar kan du ansluta plånböcker som Sparrow eller Spectre. En lyckad anslutning gör att din wallet kan synkroniseras direkt med din nod, vilket ger en säker, privat och självhanterad Bitcoin-upplevelse.


## 1️⃣1️⃣ Anslut Sparrow Wallet


För att ansluta `Sparrow Wallet` till din StartOS-nod med hjälp av electrs-implementeringen, se först till att Bitcoin Core är helt synkroniserad och att electrs är installerat och körs. Öppna Sparrow Wallet på din enhet och navigera till `File` -> `Settings` -> `Server`. Välj sedan `Private Electrum Server`. I URL-fältet anger du `Tor hostname` och `Port` för electrs, som du kan hitta i StartOS under `Services` -> `electrs` -> `Properties` (slutar vanligtvis med `.onion:50001`).


![image](assets/en/16.webp)


Därefter aktiverar du Tor genom att markera `Use Proxy`, ställa in proxyadressen till `127.0.0.1` och porten till `9050`. Klicka på `Test Connection` och vänta några ögonblick. Vid en lyckad anslutning visas ett bekräftelsemeddelande som "Ansluten till electrs". När det har verifierats stänger du inställningarna och fortsätter att skapa eller återställa din wallet. Den här inställningen säkerställer att din wallet frågar din egen nod via electrs, vilket ger full integritet och pålitlig drift.


![image](assets/en/17.webp)


## 🎯 Slutsats


StartOS by Start9 är en användarvänlig, integritetsfokuserad plattform som är utformad för självhosting av viktiga tjänster som Bitcoin och Lightning-noder, plånböcker och personliga appar. Den eliminerar behovet av kommandoradsfärdigheter genom att erbjuda ett rent grafiskt gränssnitt, automatiserade säkerhetskopior, hälsoövervakning och säker Tor-åtkomst, vilket gör den idealisk för icke-tekniska användare. Dess modulära arkitektur stöder sömlös integration med verktyg som electrs eller Sparrow, vilket ger dig full kontroll över din finansiella och digitala suveränitet. Med ett starkt fokus på transparens, lokal kontroll och utbyggbarhet gör StartOS det möjligt för användare att återta ägandet från centraliserade plattformar och driva sin egen privata, motståndskraftiga infrastruktur.