---
name: Qubes
description: Ett rimligt säkert operativsystem.
---

![cover](assets/cover.webp)



Qubes OS är ett kostnadsfritt operativsystem med öppen källkod som är utformat för användare som prioriterar säkerhet högt. Dess särdrag bygger på en enkel men radikal idé: i stället för att betrakta datorn som en helhet delar det upp användningen av den i oberoende fack som kallas **_qubes_**.



Varje qube fungerar som en **isolerad virtuell miljö**, med en specifik tillitsnivå och funktion. Så även om en applikation äventyras förblir attacken begränsad till dess qube utan att påverka resten av systemet.



> Om du tar säkerhet på allvar är Qubes OS det bästa operativsystemet som finns tillgängligt idag. - **Edward Snowden**.

Att installera Qubes OS kräver dock mer förberedelser än att installera ett konventionellt operativsystem. Det handlar om att kontrollera vissa hårdvaruförutsättningar, förstå grunderna i virtualisering och acceptera en annorlunda upplevelse, där varje daglig uppgift är tänkt i termer av separation. Men när det väl är på plats erbjuder Qubes OS ett robust ramverk som omdefinierar hur du interagerar med din dator på daglig basis. I den här handledningen förklarar vi hur Qubes OS fungerar och hur du enkelt installerar det på ditt system.



## Hur fungerar Qubes OS?



Qubes OS är baserat på principen om uppdelning i fack. I stället för att använda ett enda system förlitar det sig på hypervisorn **Xen** för att skapa isolerade virtuella maskiner, så kallade qubes. Varje qube är avsedd för en specifik uppgift eller förtroendenivå (arbete, personlig surfning, bankärenden etc.). Denna separation säkerställer att eventuella kompromisser i en qube inte kan spridas till de andra, vilket fungerar som flera oberoende datorer inom en enda maskin.



Användaren Interface hanteras av en central, säker domän som heter **dom0**. Denna domän är helt isolerad från Internet, vilket gör den till systemets hjärta. Även om fönster och menyer visas av dom0, sker den faktiska exekveringen av applikationer i deras respektive qubes.



## De olika typerna av qubes



Runt dom0 kretsar olika typer av qubes, var och en med en mycket specifik roll att spela.





- **AppVM** används för att köra vardagliga applikationer: användaren kan på så sätt separera sina professionella e-postmeddelanden från sin webbsurfning eller bankaktiviteter, där varje miljö förblir helt oberoende av de andra.





- Dessa AppVMs är i sin tur baserade på **TemplateVMs**, som fungerar som centraliserade mallar för installation och uppdatering av programvara, vilket eliminerar behovet av att hantera varje qube separat.



Qubes OS integrerar också virtuella maskiner som är specialiserade på **systemtjänster**.





- **NetVM** hanterar direkt **nätverksenheterna** och säkerställer anslutningen till Internet. De är ofta associerade med **FirewallVM**, som ingriper för att **filtrera trafik** och begränsa exponeringen av andra qubes.





- ServiceVM:er spelar en liknande roll, t.ex. vid hantering av USB-enheter, alltid med samma logik: isolera de mest riskfyllda komponenterna för att minska attackytan.



För enstaka eller riskfyllda uppgifter erbjuder Qubes OS slutligen **DisposableVM**. Dessa kortlivade qubes skapas i farten för att **öppna ett misstänkt dokument** eller **besöka en tvivelaktig webbplats**, och försvinner sedan helt när de stängs, vilket raderar alla spår och förhindrar en ihållande attack.



### Mekanismen för säker kopiering (qrexec)



Utbytet mellan qubes baseras på **qrexec**, ett kommunikationssystem mellan olika virtuella maskiner som är utformat för säkerhet. Istället för att låta qubes kommunicera fritt inför qrexec **specifika policyer**: en fil som kopieras från en AppVM till en annan, eller text som överförs via urklipp, passerar alltid genom en kanal som övervakas och valideras av systemet. På så sätt kontrolleras även den enkla handlingen att kopiera och klistra in för att förhindra spridning av skadlig kod.



### Diskhantering



Qubes OS använder ett sinnrikt system för lagringshantering. TemplateVMs innehåller den gemensamma mjukvarubasen, medan AppVMs endast lägger till sina personliga data och specifika filer. Detta minskar användningen av diskutrymme och underlättar globala uppdateringar. DisposableVMs, å andra sidan, använder tillfälliga volymer som försvinner helt när de stängs. Den här modellen garanterar inte bara högre säkerhet utan också effektiv resurshantering.



## Varför välja Qubes OS?



Fördelarna med Qubes OS ligger framför allt i dess unika säkerhetsmodell. Kärnan i detta tillvägagångssätt är kompartmentalisering, som skyddar användaren genom att isolera varje uppgift i separata virtuella maskiner. I praktiken kan ett infekterat e-postmeddelande eller en skadlig webbplats bara äventyra en enda qube, medan resten av systemet och dina personuppgifter är helt skyddade. Den här arkitekturen begränsar avsevärt komplexa attacker som i ett konventionellt system skulle kunna spridas fritt.



Qubes OS erbjuder också total transparens och kontroll över din digitala miljö. Du vet exakt vilken programvara som har tillgång till vilken resurs, oavsett om det är nätverket, en USB-enhet eller andra känsliga komponenter. Systemet integrerar avancerade säkerhetsfunktioner som standard, t.ex. fullständig diskkryptering, och underlättar användningen av anonymiseringstjänster som operativsystemet Whonix.



https://planb.academy/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

I stället för att försöka skapa ett ogenomträngligt system fokuserar Qubes OS på motståndskraft: det kapslar in skadan i händelse av intrång, vilket minskar risken för resten av systemet. Detta pragmatiska tillvägagångssätt gör Qubes OS till ett förstahandsval för användare med höga säkerhetsbehov eller som vill behålla maximal kontroll över sina digitala liv.



## Installera Qubes OS



Innan du installerar Qubes OS är det viktigt att se till att din maskinvara uppfyller minimikraven, eftersom systemet förlitar sig på virtualisering för att isolera qubes. De viktigaste komponenterna att kontrollera är :




- **Processorn**: En 64-bitars processor som är kompatibel med hårdvaruvirtualisering (Intel VT-x eller AMD-V).
- RAM-minne: minst 8 GB krävs, men vi rekommenderar ett RAM-minne på 16 GB eller mer för att köra flera qubes samtidigt.
- **Lagringsutrymme**: minst 36 GB, helst 128 GB på en SSD-enhet för optimal prestanda.



För att installera Qubes OS, hämta den officiella ISO-bilden från Qubes OS [officiella webbplats](https://www.qubes-os.org/downloads/). Det är viktigt att kontrollera ISO-filens integritet med hjälp av de GPG-signaturer som tillhandahålls, för att säkerställa att filen inte har manipulerats och att nedladdningen är säker.



https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



När ISO-filen har verifierats måste du skapa ett startbart installationsmedium, vanligtvis ett USB-minne. Detta gör du genom att ladda ner och installera programvara som **Rufus** för Windows eller **Etcher** för Windows, Linux eller macOS. Med dessa verktyg kan du kopiera ISO-filen till USB-minnet så att det blir startbart.



Innan installationen påbörjas är det nödvändigt att konfigurera datorns **BIOS eller UEFI** för att **aktivera virtualisering** och tillåta start från USB. Beroende på din maskinmodell kan det vara nödvändigt att **inaktivera Secure Boot**, eftersom Qubes OS kanske inte startar med detta alternativ aktiverat.



![0_02](assets/fr/02.webp)



När dessa villkor har uppfyllts, starta om datorn och öppna BIOS/UEFI genom att omedelbart trycka på **Esc**, **Del**, **F9**, **F10**, **F11** eller **F12** (beroende på tillverkare). I startmenyn väljer du USB-nyckeln som startenhet för att starta installationen av Qubes OS.



**Startskärm för uppstart**


När du startar från USB-minnet kommer du direkt till menyn **GRUB**, där du kan välja vilken åtgärd som ska utföras. Använd piltangenterna på tangentbordet för att välja "Install Qubes OS" och tryck på "Enter".



![0_03](assets/fr/03.webp)



**Val av språk** :



När installationen startar är det första steget att **välja det språk** och den **regionala variant** som passar din konfiguration. På så sätt säkerställs att system- och installationsalternativen visas korrekt på det språk som du föredrar.



![0_04](assets/fr/04.webp)



**Parametrarnas konfiguration** :



I det här skedet måste du konfigurera ett antal Elements innan du startar installationen på din maskin.



![0_05](assets/fr/05.webp)



**Tangentbordets layout** :



Klicka på alternativet **Tangentbord** och välj sedan **lämplig layout** för din dator. När du har gjort ditt val klickar du på **Terminated** för att gå vidare till nästa steg.



**Val av destination** :



Välj alternativet "Installation destination" för att välja den disk som du vill installera Qubes OS på. Som standard sker partitioneringen automatiskt, vilket gör att du kan ta bort alla data från disken och installera systemet på den. Du kan dock välja **Customized** eller **Advanced Customization** för att utföra en anpassad partitionering. Klicka sedan på "Done". Systemet kommer att be dig att ange ett **lösenord**, som fungerar som en säkerhets-Layer för att kryptera dina data. Var noga med att välja ett komplext och unikt lösenord.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Välj datum- och tidsformat** :


Klicka på alternativet Time and date och välj sedan din geografiska zon. Du kan också välja önskat tidsformat: 24 timmar eller 12 timmar.



![0_08](assets/fr/08.webp)



**Skapande av användarkonto** :


Klicka på **Create user** för att skapa ditt **första konto**, som gör det möjligt för dig att logga in på Qubes OS.



![0_09](assets/fr/09.webp)



**Aktivera root-konto** :


Du kan också **aktivera root-kontot** genom att ange ett separat lösenord för administration.



![0_10](assets/fr/10.webp)



När du har gjort dessa inställningar klickar du på **Starta installationen** för att starta processen.



![0_11](assets/fr/11.webp)



Vänta på **slut på installationen** och klicka sedan på **starta om systemet** för att slutföra installationen och starta Qubes OS.



![0_12](assets/fr/12.webp)



**Ytterligare konfiguration** :


Efter omstart uppmanar Qubes OS dig att slutföra **standardmallarna och qubes-konfigurationen**. Ange det lösenord som definierats för att kryptera disken.



![0_13](assets/fr/13.webp)



Därefter börjar du med att välja det **TemplateVM** du vill installera. Vanliga alternativ är **Debian 12 Xfce**, **Fedora 41 Xfce** och **Whonix 17**, där den senare rekommenderas för användningar som kräver **anonymitet och nätverkssäkerhet**. Du kan också definiera **standardmallen**, som kommer att ligga till grund för skapandet av nya **AppVM**.



![0_14](assets/fr/14.webp)



I avsnittet **Huvudkonfiguration** kan du välja att automatiskt skapa viktiga systeminställningar som **sys-net**, **sys-firewall** och **default DisposableVM**. Det är tillrådligt att aktivera alternativet att göra **sys-firewall och sys-usb engångs** för att begränsa exponeringen av enheter och nätverk i händelse av kompromisser. Du kan också skapa standard **AppVMs**, t.ex. **personal**, **work**, **untrusted** och **vault**, för att organisera dina aktiviteter enligt deras tillitsnivå.



![0_15](assets/fr/15.webp)



Med Qubes OS kan du också skapa en **qube dedikerad till USB-enheter** (sys-usb) och konfigurera **Whonix Gateway och Workstation qubes** för att säkra din kommunikation via Tor-nätverket. För avancerade användare kan du i avsnittet **Avancerad konfiguration** skapa en **LVM thin pool** för att effektivt hantera diskutrymme mellan qubes.



När alla dessa alternativ har konfigurerats klickar du på **Complete** och sedan på **Finish configuration**. Vänta medan systemet tillämpar dessa inställningar. Du kommer sedan att uppmanas att **logga in på ditt användarkonto**, och din Qubes OS-miljö kommer att vara redo att användas, säker och korrekt isolerad för dina olika aktiviteter.



![0_17](assets/fr/17.webp)



Operativsystemet är nu installerat och klart att användas.



![0_18](assets/fr/18.webp)



## Skapa en qube på ditt system



För att skapa en qube hanteras processen av verktyget **Qube Manager**, som finns tillgängligt från Start-menyn. I verktygsfönstret klickar du bara på ikonen **Create qube** för att öppna ett nytt konfigurationsfönster. Ange först ett namn för din qube, t.ex. "perso-web" eller "work", för att identifiera dess användning.



Därefter väljer du dess **Typ**, vanligtvis **AppVM** för rutinuppgifter eller **DisposableVM** för tillfällig användning. Det är viktigt att välja den **Template** som din qube kommer att baseras på, till exempel "fedora-39" eller "debian-12", eftersom detta kommer att tillhandahålla operativsystem och programvara. Du kommer också att utse **NetVM**, som är den qube som ansvarar för internetåtkomst, som standard **sys-brandvägg**.



När du har justerat lagringsstorleken och RAM-minnet om det behövs startar skapandeprocessen med ett enkelt klick på **OK**. När processen är klar kommer din nya qube att synas i listan och vara redo att användas.



Sammanfattningsvis är Qubes OS inget vanligt operativsystem, utan en banbrytande säkerhetslösning som omprövar persondatorns arkitektur. Lösningen, som bygger på uppdelning och isolering genom virtualisering, ger ett oöverträffat skydd mot de mest sofistikerade hoten. Genom att segmentera arbetsmiljön i specialiserade qubes för varje uppgift säkerställs att skadlig kod inte kan spridas och äventyra hela systemet.



Oavsett om du behöver surfa säkert på webben, skydda känslig information eller arbeta med varierande nivåer av förtroende, ger Qubes OS ett motståndskraftigt, transparent ramverk. Genom att tillämpa god praxis och utnyttja dess funktioner fullt ut får du en **digital fästning** som är anpassad till moderna hot. Läs mer om hur du skyddar dina data och din integritet.



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1