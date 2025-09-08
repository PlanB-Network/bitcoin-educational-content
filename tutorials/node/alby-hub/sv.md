---
name: Alby nav
description: Hur lanserar du enkelt din egen Lightning-nod?
---
![cover](assets/cover.webp)


Alby Hub är den senaste programvaran med öppen källkod från Alby, företaget bakom det populära webbtillägget Lightning. Alby Hub är en självförvaltande Wallet med den mest lättanvända Lightning-noden, tillgänglig från var som helst för att integreras med dussintals appar. Alby Hub är en lättanvänd Interface för hantering av Lightning-noder.


I den här handledningen tittar vi på olika sätt att använda Alby Hub och hur du ansluter den till Alby Go, Albys mobilapp eller Alby Browser Extension. Detta gör att du kan spendera din Sats på resande fot samtidigt som du är självständig i hanteringen av din nod.


![ALBY HUB](assets/fr/01.webp)


## Vad är Alby Hub?


Alby Hub är tänkt att bli det nya flaggskeppsverktyget i Albys ekosystem. Denna programvara gör det möjligt för användare att enkelt hantera sin egen självförvaltande Wallet med en integrerad Lightning-nod, samtidigt som de behåller Ownership för sina nycklar (självförvaltande).


Alby Hub är ett mycket anpassningsbart verktyg. Det kan tillgodose behoven hos både nybörjare och avancerade användare. Nybörjare kommer att använda det för att enkelt driva en riktig Lightning-nod på egen hand, utan att behöva hantera den underliggande komplexiteten. För mer erfarna användare kan Alby Hub användas som en komplett Interface för avancerad hantering av en befintlig Lightning-nod.


Beroende på dina behov finns Alby Hub i 4 olika konfigurationer:




- Alby Hub Cloud :**


Detta första alternativ är idealiskt för nybörjare och är Alby Cloud-alternativet. Det gör att du kan distribuera en hubb direkt på en Alby-hanterad server, tillgänglig via din Alby Hub Interface. Även om Alby hanterar servern behåller du suveräniteten över dina medel, eftersom dina nycklar krypteras med ett lösenord som endast du känner till. Dina nycklar måste dock förbli dekrypterade i RAM-minnet för att noden ska fungera, vilket teoretiskt sett utsätter dem för risk om någon fysiskt kommer åt servern. Det är en intressant kompromiss för nybörjare, men det är viktigt att vara medveten om riskerna.


Den stora fördelen med det här alternativet är att du får en Lightning-nod som är igång 24/7 utan att behöva hantera hostingen själv. Dessutom är säkerhetskopiering av din Lightning-nod förenklad och automatiserad, jämfört med självhostade alternativ där du själv måste hantera säkerhetskopiering av kanaler.


Alby Cloud är en betaltjänst [Kontrollera deras prissättning] (https://albyhub.com/#pricing) för mer information. Avgiften dras automatiskt från din Wallet via en Lightning Invoice utfärdad av Alby. Detta görs via en NWC-anslutning som konfigurerar din nod för att automatiskt betala Alby-fakturor relaterade till ditt abonnemang.





- Alby Hub med en befintlig nod :**


Om du redan har en nod hosted, till exempel på Umbrel eller Start9, kan Alby Hub användas som en avancerad hantering Interface, på samma sätt som ThunderHub eller RTL.




- Alby Hub lokal :**


Det är också möjligt att installera Alby Hub direkt på datorn, men det är ett mindre praktiskt alternativ eftersom datorn måste vara aktiv hela tiden för att få fjärråtkomst till Lightning-noden. Detta alternativ kan dock vara lämpligt för dina specifika behov.




- Alby Hub på en personlig server :**


För avancerade användare kan Alby Hub distribueras på en personlig server med ett enkelt kommando. Detta alternativ behandlas inte i denna handledning, men du kan hitta dedikerade instruktioner [på Albys GitHub] (https://github.com/getAlby/hub?tab=readme-ov-file#docker).


Denna handledning fokuserar främst på Interface, som kommer att vara densamma oavsett vilket alternativ som väljs. Vi kommer också att titta på hur man distribuerar Alby Hub med det betalda molnalternativet och sedan med node-in-box-alternativet (Umbrel eller Start9).


![ALBY HUB](assets/fr/02.webp)


För lokal installation på din PC, [ladda ner och installera programvaran enligt ditt operativsystem] (https://github.com/getAlby/hub/releases), följ sedan samma instruktioner som på Interface.


![ALBY HUB](assets/fr/03.webp)


## Skapa ett Alby-konto


Det första steget är att skapa ett Alby-konto. Även om detta inte är nödvändigt för att använda Alby Hub, gör det att du kan dra full nytta av de tillgängliga alternativen, inklusive möjligheten att få en Lightning Address.


Gå till [den officiella Alby-webbplatsen] (https://getalby.com/) och klicka på knappen "*Create Account*".


![ALBY HUB](assets/fr/04.webp)


Ange ett smeknamn och en e-postadress Address och klicka sedan på "*Signera*". Denna e-postadress Address kommer att användas för att logga in på ditt konto senare.


![ALBY HUB](assets/fr/05.webp)


Ange verifieringskoden som du fick via e-post.


![ALBY HUB](assets/fr/06.webp)


När du har loggat in på ditt onlinekonto klickar du på knappen "*Fortsätt*".


![ALBY HUB](assets/fr/07.webp)


Klicka på "*Fortsätt*" igen.


![ALBY HUB](assets/fr/08.webp)


## Alternativet med molnbaserad hosting


Du måste sedan välja mellan ett självhanterat alternativ, där du installerar Alby Hub på din egen enhet, eller premiumalternativ. Jag börjar med att förklara hur du går vidare med Pro Cloud-alternativet (observera att detta är ett betalalternativ, se detaljer i föregående avsnitt).


Klicka på "*Uppgradering*".


![ALBY HUB](assets/fr/09.webp)


Bekräfta genom att klicka på "*Subscribe Now*".


![ALBY HUB](assets/fr/10.webp)


Klicka på "*Lansera Alby Hub*".


![ALBY HUB](assets/fr/11.webp)


Vänta några ögonblick medan din nod skapas.


![ALBY HUB](assets/fr/12.webp)


Och det var det, din Alby Hub är nu konfigurerad. I nästa avsnitt ska jag visa hur du installerar Alby Hub på en befintlig nod. Om du inte redan har en lightning-nod kan du hoppa vidare till nästa avsnitt för att konfigurera Alby Hub på Alby Cloud.


![ALBY HUB](assets/fr/13.webp)


## Alternativet med egen hosting


Om du föredrar att använda Alby Hub som en Interface för din befintliga Lightning-nod har du flera alternativ: installera den på en server, lokalt på din dator eller via en node-in-box (Umbrel eller Start9). Att använda Alby Hub i dessa konfigurationer är kostnadsfritt. Vi kommer att koncentrera oss på node-in-box-alternativet, eftersom jag anser att serveralternativet, utan fysisk åtkomst, innebär liknande risker som molnversionen, och lokal installation på en dator är ofta olämplig.


För att ställa in detta på Umbrel (stegen för Start9 är identiska) måste du först ha en LND-nod som redan är konfigurerad.


Logga in på din Umbrel Interface och gå till applikationsbutiken.


![ALBY HUB](assets/fr/14.webp)


Leta efter applikationen "*Alby Hub*".


![ALBY HUB](assets/fr/15.webp)


Installera det på din nod.


![ALBY HUB](assets/fr/16.webp)


Din Alby Hub Interface är nu klar. Du kan följa resten av handledningen som om du använde Interface i molnet, men utan alternativen i den betalda versionen. Dessutom, till skillnad från molnversionen, lagras dina nycklar lokalt på din nod, inte på Albys servrar.


![ALBY HUB](assets/fr/17.webp)


## Lansering av Alby Hub


Klicka på knappen "*Get Started*".


![ALBY HUB](assets/fr/18.webp)


Alby Hub kommer sedan att uppmana dig att välja ett lösenord. Detta lösenord är mycket viktigt, eftersom det kommer att användas för att kryptera dina Wallet. I den betalda molnversionen lagras dina nycklar på Alby-servern, krypteras med det här lösenordet som bara du känner till, dekrypteras sedan och lagras endast i RAM-minnet för att signera transaktioner vid behov.


Det är därför viktigt att välja ett starkt lösenord. Vem som helst med detta lösenord kan potentiellt få tillgång till din nod. Se till att du också gör en eller flera fysiska säkerhetskopior av lösenordet på ett papper, eller ännu bättre, på en metallbit för extra säkerhet.


När du noggrant har valt och sparat ditt lösenord klickar du på "*Create Password*".


![ALBY HUB](assets/fr/19.webp)


Du har nu tillgång till din Lightning-nod.


![ALBY HUB](assets/fr/20.webp)


Den första åtgärden du bör vidta är att spara din återställningsfras, från vilken dina nycklar härleds. För att göra detta, klicka på "Inställningar". Med den här frasen kan du återfå åtkomst till din Wallet om du har aktiverat automatiska säkerhetskopior.


![ALBY HUB](assets/fr/21.webp)


Gå sedan till fliken "*Backup*". Ange ditt lösenord för att komma åt det.


![ALBY HUB](assets/fr/22.webp)


Du kommer då att ha tillgång till din 12-ords återhämtningsfras. Gör en eller flera fysiska säkerhetskopior av denna fras på papper eller metall och förvara den på en säker plats.


![ALBY HUB](assets/fr/23.webp)


När du har sparat frasen markerar du rutan för att bekräfta att du har sparat den och klickar på "*Continue*".


![ALBY HUB](assets/fr/24.webp)


## Hur kan jag återfå tillgång till mina bitcoins?


Innan du skickar pengar till din Alby Hub är det viktigt att du förstår hur du återfår dem om det skulle uppstå problem, samt vilken information som krävs för denna återvinning. Processen varierar beroende på vilken typ av medel som ska återvinnas och värdläget för din nod.


För betalande molnanvändare kräver fullständig återställning av dina bitcoins tre viktiga Elements:



- Din återhämtningsfras;
- Tillgång till ditt Alby-konto för att hämta de automatiska säkerhetskopiorna.


Avsaknaden av någon av dessa två uppgifter skulle göra det omöjligt att återfå dina bitcoins i sin helhet.


För dem som kör Alby Hub på sin egen enhet finns återställningsprocessen dokumenterad [här] (https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).


Om du installerade Alby Hub på en befintlig nod måste du följa återställningsprocessen för det specifika operativsystemet för noden. Ett exempel: Umbrel erbjuder [ett alternativ](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) för att kryptera den senaste statusen för dina Lightning-kanaler och spara den dynamiskt och anonymt via Tor. Tänk på att endast de automatiska säkerhetskopiorna från Alby låter dig återställa din Hub helt utan att stänga några kanaler.


## Köp din första Lightning-kanal


Du kan nu följa instruktionerna som tillhandahålls av Alby Hub. Klicka på knappen för att öppna din första kanal för inkommande kontanter.


![ALBY HUB](assets/fr/25.webp)


Välj "*Öppen kanal*". Om du inte har för avsikt att bli en routingnod och inte specifikt behöver en, rekommenderar jag att du väljer privata kanaler.


![ALBY HUB](assets/fr/26.webp)


Alby Hub kommer att generate och Invoice för att du ska kunna betala. Denna betalning täcker transaktionsavgifterna som behövs för att öppna din kanal, samt serviceavgifterna för LSP (*Lightning Service Provider*) som kommer att öppna en kanal till din nod, så att du kan ta emot betalningar omedelbart.


![ALBY HUB](assets/fr/27.webp)


När Invoice har betalats och transaktionen har bekräftats är din första Lightning-kanal etablerad.


![ALBY HUB](assets/fr/28.webp)


På fliken "*Node*" kan du se att du nu har inkommande kontanter, vilket gör att du kan ta emot betalningar via Lightning.


![ALBY HUB](assets/fr/29.webp)


För att ta emot betalning, klicka på fliken "*Wallet*" och sedan på "*Receive*".


![ALBY HUB](assets/fr/30.webp)


Ange ett belopp och lägg till en beskrivning om det behövs, klicka sedan på "*Create Invoice*".


![ALBY HUB](assets/fr/31.webp)


Jag fick min första betalning på 120.000 Sats.


![ALBY HUB](assets/fr/32.webp)


Genom att återgå till fliken "*Wallet*" kan du kontrollera ditt Wallet-saldo. Observera att Alby Hub automatiskt avsätter 354 Sats när du gör din första betalning. För varje Lightning-kanal du öppnar därefter kommer Alby Hub automatiskt att avsätta en reserv motsvarande 1% av kanalens kapacitet. Denna reserv är en säkerhetsåtgärd som gör det möjligt för din nod att återfå kanalens medel i händelse av bedrägeriförsök av din peer. Det är därför, trots att jag har skickat 120 000 Sats, endast 119 646 Sats visas på mitt saldo.


![ALBY HUB](assets/fr/33.webp)


## Insättning av bitcoins på kedjan


Om du vill ha utgående kontanter för att göra betalningar kan du också öppna en kanal själv. För att göra detta behöver du onchain bitcoins i din Wallet.


Från fliken "*Node*" klickar du på "*Deposit*".


![ALBY HUB](assets/fr/34.webp)


Skicka bitcoins till den Address som visas. Denna Address härrör från din tidigare sparade återställningsfras.


![ALBY HUB](assets/fr/35.webp)


Jag skickade 72 000 Sats. De är nu synliga i "*Sparsaldo*", som innehåller alla medel jag äger på kedjan och inte på Lightning.


![ALBY HUB](assets/fr/36.webp)


## Öppna en Lightning-kanal


Nu när du har onchain-medel kan du öppna en ny Lightning-kanal. Det är tillrådligt att öppna flera kanaler med tillräckliga belopp för att säkerställa att du alltid kan göra betalningar utan begränsningar. De flesta LSP:er (*Lightning Service Providers*) kräver minst 150 000 Sats för att öppna en kanal med dig.


På fliken "*Node*" klickar du på "*Open Channel*".


![ALBY HUB](assets/fr/37.webp)


Välj storlek på din kanal. Jag rekommenderar att du inte öppnar kanaler som är för små, med tanke på att detta är en Lightning-nod och att maskinen som är värd för dina nycklar inte erbjuder samma säkerhetsnivå som en Hardware Wallet. Så var försiktig med de belopp som du väljer att blockera.


![ALBY HUB](assets/fr/38.webp)


I menyn "*Advanced Options*" kan du välja vilken LSP du vill öppna din kanal med eller manuellt ange en annan Lightning-nod.


![ALBY HUB](assets/fr/39.webp)


Klicka sedan på "*Öppen kanal*".


![ALBY HUB](assets/fr/40.webp)


Vänta medan din kanal bekräftas på kedjan.


![ALBY HUB](assets/fr/41.webp)


Din nya kanal kommer nu att visas på fliken "*Node*".


![ALBY HUB](assets/fr/42.webp)


## Hantering av noder


Att hantera dina Lightning-kanaler är enklare än du tror. Med Alby Hub kan du överföra Sats mellan ditt utgiftssaldo och ditt On-Chain-saldo. På så sätt kan du öka din utgifts- eller mottagningskapacitet.


![ALBY HUB](assets/fr/66.webp)


## Anslut en utgiftsansökan


Nu när du har en fungerande Lightning-nod kan du använda den för att ta emot och spendera Sats på daglig basis. Även om Alby Hubs webb Interface är praktisk för att hantera din nod, är den inte idealisk för att göra snabba transaktioner på resande fot. För detta kommer vi att använda en Lightning Wallet-app installerad på vår smartphone.


I den här handledningen rekommenderar jag att du väljer Alby Go, som är mycket lätt att använda, men du kan också använda andra kompatibla applikationer som Zeus.


![ALBY HUB](assets/fr/43.webp)


För att installera Alby Go, gå till din enhets programbutik:




- [För Android] (https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [För Apple] (https://apps.apple.com/us/app/alby-go/id6471335774).


![ALBY HUB](assets/fr/44.webp)


Android-användare kan också installera appen via filen `.apk` [tillgänglig på Albys GitHub] (https://github.com/getAlby/go/releases).


![ALBY HUB](assets/fr/45.webp)


När applikationen startas klickar du på "*Connect Wallet*".


![ALBY HUB](assets/fr/46.webp)


I din Alby Hub, under App Store, hittar du "Alby Go" och klickar på "Connect"

![ALBY HUB](assets/fr/47.webp)

Klicka på "Anslut med One-Tab Connections". Då kan du med ett klick länka din Alby Hub till andra appar som använder Alby Go.


![ALBY HUB](assets/fr/48.webp)


Alby Hub kommer sedan att generate en hemlighet för att upprätta anslutningen till Alby Go.


![ALBY HUB](assets/fr/49.webp)


Gå tillbaka till Alby Go-applikationen, skanna QR-koden eller klistra in hemligheten.


![ALBY HUB](assets/fr/50.webp)


Klicka på "Finish*".


![ALBY HUB](assets/fr/51.webp)


Du har nu fjärråtkomst till din Lightning node-drivna Alby Hub från din smartphone, vilket gör det enkelt att spendera och ta emot Sats på resande fot varje dag.


![ALBY HUB](assets/fr/52.webp)


Om det behövs kan du hantera behörigheterna för den här anslutningen direkt på Alby Hub genom att klicka på den.


![ALBY HUB](assets/fr/53.webp)


För att ta emot Sats klickar du bara på "*Ta emot*".


![ALBY HUB](assets/fr/54.webp)


Ändra beloppet och beskrivningen för Invoice genom att klicka på "*Invoice*".


![ALBY HUB](assets/fr/55.webp)


Ladda Invoice för att ta emot Sats.


![ALBY HUB](assets/fr/56.webp)


För att skicka Sats, klicka på "*Sänd*".


![ALBY HUB](assets/fr/57.webp)


Skanna den Invoice som du vill betala.


![ALBY HUB](assets/fr/58.webp)


Klicka sedan på "*Pay*".


![ALBY HUB](assets/fr/59.webp)


Din transaktion är bekräftad.


![ALBY HUB](assets/fr/60.webp)


Genom att klicka på den lilla pilen kommer du åt din transaktionshistorik.


![ALBY HUB](assets/fr/61.webp)


Dessa transaktioner syns också på din Alby Hub.


![ALBY HUB](assets/fr/62.webp)


## Anpassa din Lightning Address


Alby erbjuder dig möjligheten att använda en Lightning Address. Detta gör att du kan ta emot betalningar på din nod utan att manuellt behöva generate och Invoice varje gång. Som standard tilldelar Alby dig en Lightning Address, men du kan anpassa den. Logga in på ditt Alby online-konto, klicka på ditt namn i det övre högra hörnet och välj sedan "*Inställningar*".


![ALBY HUB](assets/fr/63.webp)


Navigera till menyn "*Lightning Address*".


![ALBY HUB](assets/fr/64.webp)


Ändra din Address och bekräfta sedan genom att klicka på "*Uppdatera din blixt Address*".


![ALBY HUB](assets/fr/65.webp)


Observera att när din Address har ändrats tillhör den inte längre dig. Se därför till att du aldrig skickar Sats till den igen.


Och nu vet du hur du använder Lightning med din egen nod med hjälp av Alby Hub-verktyget. Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du lägger en Green-tumme nedan. Du får gärna dela den här artikeln på dina sociala nätverk. Tack så mycket!


För att i detalj förstå alla blixtmekanismer som vi har manipulerat i den här handledningen rekommenderar jag starkt att du upptäcker vår gratis utbildning i ämnet :


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb