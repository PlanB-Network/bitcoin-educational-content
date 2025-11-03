---
name: Debifi
description: Få ett lån utan vårdnadshavare garanterat av Bitcoin.
---

![cover](assets/cover.webp)




## Inledning



I århundraden har traditionell utlåning gjort det möjligt att finansiera många projekt. Den är dock fortfarande långsam, kostsam och inte särskilt inkluderande, särskilt inte för dem som inte har tillgång till en solid bankinfrastruktur.



Uppkomsten av Bitcoin-protokollet inledde en ny finansiell era och förde med sig ett antal utmaningar. En av dessa utmaningar var hur man skulle skaffa likviditet utan att tvingas sälja Bitcoin och därmed förlora exponeringen mot dess tillväxtpotential



Resultatet är **Debifi**, en plattform som positionerar sig som ett modernt alternativ till bankerna. Målet är tydligt: att göra kreditgivning så enkel och transparent som möjligt genom att kombinera fördelarna med det traditionella finansiella systemet med den frihet som Bitcoin erbjuder. Namnet Debifi återspeglar denna vision: ***Decentralized Bitcoin Finance***, en sammandragning som illustrerar mötet mellan decentraliserad finansiering och Bitcoin-innovation.



Debifi är en icke-förvaltande Bitcoin-stödd utlåningsplattform, vilket innebär att du behåller kontrollen över dina privata nycklar. Det gör det möjligt för användare att låsa upp likviditet i Exchange för sina låsta bitcoins som säkerhet. Till skillnad från traditionella banklån använder Debifi ett spärrsystem med flera signaturer (3 av 4) och accepterar inte inteckning av säkerheter, vilket garanterar större säkerhet och transparens.



I praktiken innebär detta att varken Debifi eller en enskild långivare kan spendera dina BTC utan överenskommelse med tre parter (du, långivaren och en betrodd tredje part). Detta gör systemet säkrare: om du lånar på Debifi behåller du Ownership av dina Bitcoin tills lånet har återbetalats i sin helhet.



## Fördelar med Debifi



Med Debifi är det lån mot säkerhet, Blockchain-säkerhet (multisignatur, 2FA), ett urval av stablecoins / vätskor, sekretess och total Bitcoin-kontroll. Debifi "låter dig behålla dina pengar" (dina nycklar, dina mynt), samtidigt som du erbjuder konkurrenskraftiga räntor och global tillgång till BTC-stödda lån.



Här är en snabb jämförelse mellan ett Debifi-lån och ett traditionellt banklån:



| Caractéristiques       | Prêt via Debifi                                                       | Prêt bancaire traditionnel                                                 |
| ---------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Accessibilité          | ✔️ Ouvert à tout détenteur de Bitcoin (même sans historique bancaire) | ❌ Souvent réservé aux clients avec garanties physiques et dossiers solides |
| Vitesse d’obtention    | ✔️ Liquide en quelques minutes/heures                                 | ❌ Processus long (jours ou semaines)                                       |
| Garanties exigées      | ✔️ Collatéral en Bitcoin uniquement                                   | ❌ Garanties physiques (maisons, terrains, revenus stables)                 |
| Contrôle de l’actif    | ✔️ Vous conservez l’exposition au Bitcoin et son potentiel de hausse  | ❌ Vous n’avez aucun lien entre le prêt et vos actifs financiers            |
| Souplesse géographique | ✔️ Disponible partout (sans contrainte géographique bancaire)         | ❌ Limité à la juridiction de la banque                                     |
| Risque principal       | ❌ Risque de liquidation si le prix du BTC chute trop                  | ❌ Risque de saisie de biens ou impact négatif sur la cote de crédit        |

Innan jag visar dig steg för steg hur du lånar på Debifi är det några saker som jag tycker att du behöver veta.




## Definitioner





- Uppläggningsavgifter** är engångsavgifter som tas ut i samband med att ett lån beviljas och beräknas som en procentsats av det lånade beloppet. Dessa avgifter täcker administrativa kostnader, driftskostnader och förvaltningskostnader.





- Säkerhet** är en tillgång som du deponerar för att säkra ett lån. I Debifis fall är säkerheten Bitcoin (BTC), som låntagaren deponerar i Multisig 3/4 escrow.





- Multisig escrow (3/4)**-systemet är en säker insättningsmekanism där en låntagares bitcoins placeras i en Address med flera signaturer. Specifikt har fyra (4) parter vardera en nyckel (låntagare, långivare, Debifi, oberoende tredje part). För att flytta medel krävs minst 3 av 4 signaturer.





- En stablecoin** är en kryptovaluta vars värde är kopplat till en stabil tillgång (t.ex. US-dollar), vilket undviker volatiliteten i Bitcoin. Till exempel är 1 USDC alltid värd ~ $ 1, eftersom den backas upp av fiatreserver.





- Belåningsgraden (LTV)** för ett lån avgör hur mycket kontanter du kan låna som säkerhet för din Bitcoin. LTV-kvot = Lånebelopp / Säkerhetsbelopp * 100. Till exempel innebär en LTV på 50 % att värdet på lånet är lika med 50 % av värdet på den deponerade Bitcoin.




BTC-sessioner videohandledning :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Komma igång med Debifi



För att komma igång med Debifi behöver du några förutsättningar.


### Förkunskapskrav



Innan du kan låna från Debifi, vänligen se till att du har följande saker:





- Bitcoin Wallet: där du har din BTC (helst inte förvarad, t.ex. Hardware Wallet eller en betrodd mobil Wallet). Det är från denna Wallet som du skickar Bitcoin-säkerheten till Debifi och tar emot pengarna.





- Stablecoins eller fiat: Debifi lånar ut i stablecoins och vissa fiatvalutor. De viktigaste stablecoins som används är USDT och USDC.



Du kan använda Aqua, en Bitcoin och Liquid Wallet som också stöder USDT stablecoin-hantering i olika nätverk. Eller COLDCARD (Mk4 eller Q), för närvarande den enda hårdvara som stöds av Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): beroende på vilket låneerbjudande som valts kan en identitetsverifieringsprocess krävas. På Debifi anger varje erbjudande om KYC krävs eller inte. Så förbered dig i enlighet med detta. KYC utförs av pålitliga tredjepartsleverantörer av tjänster som Sumsub.



![image](assets/fr/03.webp)





- Applikation för tvåfaktorsautentisering: Debifi kräver en Authenticator-kod för varje viktig åtgärd. Det är en extra Layer av säkerhet. I den här handledningen kommer vi att använda Google Authenticator. Alternativt kan du använda andra som du tycker passar.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Debifis webbplats och mobilapplikation: Debifi är både en webbplats och en mobilapplikation, och de två fungerar i tandem. Mobilappen blir en Wallet, som lagrar din privata nyckel och hanterar signeringen av kontrakt. Dessutom måste du använda webbplatsen för att ingå avtal (en stor Interface ger dig en allmän överblick över låneavtal och deras detaljer).





- Debifis mobilapp (iOS/Android) krävs för att teckna lån. Du måste ladda ner appen, skapa ett konto och "länka" din enhet (registrera enheten till ditt konto). Debifi-appen stöder tvåfaktorsautentisering (2FA) och utan en smartphone kan du inte bekräfta transaktioner på Debifi.



### Skapa ett konto



Besök [Debifis officiella webbplats] (https://debifi.com/app).



![image](assets/fr/04.webp)



Installera din applikation beroende på vilken typ av smartphone du har och öppna den sedan.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



När du är inne i programmet klickar du på menyn **Settings**.



![image](assets/fr/07.webp)



Klicka sedan på **Login or create account** för att skapa ett konto med din e-post Address.



![image](assets/fr/08.webp)



![image](assets/fr/09.webp)



![image](assets/fr/10.webp)



Du kommer att få en verifieringskod via e-post. Kopiera och klistra in denna kod i applikationen. Öppna sedan Debifi-applikationen på din smartphone och logga in.



![image](assets/fr/11.webp)



### Säkra ditt konto



Av säkerhetsskäl kommer Debifi att be dig att följa tre steg.



![image](assets/fr/12.webp)





- Först måste du ange en stark PIN-kod för att komma åt din ansökan senare.



![image](assets/fr/13.webp)





- Därefter ställer du in tvåfaktorsautentisering (2FA) för att associera din enhet med ditt konto med hjälp av 2FA-koden.



![image](assets/fr/14.webp)





- Slutligen ska du spara de 12 orden i din privata nyckel genom att skriva ner dem på ett tillförlitligt medium och förvara dem på en säker plats. Denna fas är viktig för att återställa ditt konto och hantera dina pengar.



![image](assets/fr/15.webp)





- För ökad säkerhet kan du även lägga till en passphrase.



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Observera att endast din registrerade smartphone kommer att kunna öppna ditt konto (en extra säkerhetsåtgärd).



När du har slutfört dessa steg klickar du på menyn **Erbjudanden** för att se de tillgängliga låneerbjudandena. När du klickar på ett erbjudande omdirigerar det dig till Debifi-webbplatsen.



![image](assets/fr/17.webp)



### Gå in på webbplatsen och ta del av låneerbjudanden



När din enhet är ansluten går du till [Debifis webbplats] (https://debifi.com/). Logga in för att upprätta en säker anslutning mellan Debifis mobilapplikation och webbplattformen. Detta gör det lättare för dig att interagera med tillgängliga låneerbjudanden (en tydlig bild av detaljerna i varje erbjudande) och hantera ditt konto.



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




Videohandledning om hur du loggar in med ditt konto på plattformen :



![video](https://youtu.be/cUwCfTKDAOo)



## Ansökan om lån



Plattformen ger dig tillgång till likviditet av institutionell kvalitet och erbjuder en rad olika alternativ som passar dina behov. Bläddra igenom för att ta reda på vad som finns tillgängligt. Du har också möjlighet att justera låneparametrarna efter din individuella risktolerans och finansiella situation.



![image](assets/fr/22.webp)



De fiatvalutor som Debifi för närvarande erbjuder kan ses på plattformen.



![image](assets/fr/23.webp)



### Tydliga och flexibla avtalsklausuler



Debifi förlitar sig på transparenta och flexibla lånevillkor för att tillgodose behoven hos varje part (långivare och låntagare). Nyckelklausuler inkluderar :



#### Belåningsgrad i förhållande till värde (LTV)


Bitcoin-lånetrancherna är i allmänhet tre (3) till antalet:





- Konservativ (20% - 40% LTV), vilket motsvarar ett lågrisklån, är idealiskt för att maximera säkerheten mot Bitcoin-prisvolatilitet;





- Balanserad (50% belåningsgrad) ;





- Aggressive (70% - 85% LTV), som erbjuder större likviditet, men medför en mycket hög risk för likvidation under marknadsnedgångar. Aktiv övervakning av Bitcoin-marknadsförhållandena är ett måste när man väljer denna tranche.



#### Räntesatser



Räntesättningen beror i allmänhet på din valda belåningsgrad, låneperiodens längd, säkerhetens volatilitet och plattformsspecifika riskbedömningar. Räntorna förblir fasta under lånets löptid.



#### Lånetid och återbetalningsflexibilitet



Återbetalningsplanerna för lån är ofta flexibla och skräddarsydda efter användarens behov. Betalningar kan göras när som helst så länge som kraven på säkerhet är uppfyllda. Lånebetalningar är i allmänhet ränta under lånets löptid och kapitalbelopp som förfaller vid förfallodagen.



#### Likvidationsrätt (Margin call)



Eftersom priset på Bitcoin är volatilt innehåller ett ansvarsfullt lån specifika policyer för marginalsäkerhet i avtalet. Denna policy gör att låntagaren kan underrättas om att antingen ställa ytterligare säkerhet eller återbetala en del av lånet.



### Lansering av låneprocessen



För att välja ett låneerbjudande som passar dina behov, klicka på det för att se dess egenskaper.



![image](assets/fr/24.webp)



Du kan se :


1. Låneinstitutets namn ;


2. Lånets beloppsintervall;


3. Att du kommer att få pengarna i USDC Ethereum ;


4. Lånets löptid, ränta och belåningsgrad;


5. KYC krävs för detta erbjudande;


6. Det exakta belopp du behöver måste anges (detta belopp måste ligga inom intervallet, se 2);


7. Den Ethereum USDC Address som ska användas för att ta emot pengarna måste anges.



När du är nöjd med erbjudandet och har fyllt i nödvändig information klickar du på "Contract request".



![image](assets/fr/25.webp)



Gå tillbaka till mobilapplikationen för ''**Provide public key**''.



![image](assets/fr/26.webp)



Tryck på '' **Provide public key** '' och välj sedan källan till den publika nyckeln. Långivaren kommer också att behöva Supply en publik nyckel.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Nästa steg är att underteckna Contract. Fortfarande i mobilapplikationen trycker du på '' **Signera Contract** ''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



När du är klar med att signera Contract skapar Debifi automatiskt en unik multisignatur Bitcoin Address (escrow 3-sur-4) för din Contract. Så länge dina bitcoins finns i escrow kan de inte användas någon annanstans.



### Insättning av garantin och mottagande av dina medel



Det sista steget är att deponera din Bitcoin-säkerhet i spärrsystemet med flera signaturer. Debifi visar dig sedan escrow Address (B) och mängden BTC (A) som ska skickas som (säkerhet + provision).



![image](assets/fr/33.webp)



Du kommer också att få detta meddelande i din mobilapplikation.



![image](assets/fr/34.webp)



Så snart din insättning har bekräftats kommer långivaren att betala lånebeloppet till den mottagande Address som du har angett, vilket slutför transaktionen och ger dig tillgång till de medel du behöver.



Du kommer då att få ett meddelande från Debifi där du ombeds att betala låneavgifterna eller provisionerna för att statusen för ditt lån ska kunna förbättras.



I verkligheten, när Contract har skapats, dras låneavgifterna automatiskt från den säkerhet som låntagaren har deponerat i den multisignerade deponeringen Address.



Allt du behöver göra är att underteckna en transaktion som gör det möjligt för Debifi att dra av sin provision från garantin. Din långivare måste å sin sida också underteckna transaktionen för avgiftsavdrag, annars kan Debifi inte få sin provision.



![image](assets/fr/35.webp)



De tillämpliga utlåningsavgifterna är 1,5-2%, beroende på löptiden för Contract. Plattformen tar endast ut provisioner i Bitcoin.



## Spårning av lån



När lånet är på gång kan du med Debifi övervaka ditt Contract i realtid. I Interface kommer du att se :





- Det lånade beloppet och återstående löptid.
- Aktuellt LTV-förhållande (lån till värde): LTV ökar om priset på BTC sjunker (eftersom din säkerhet är mindre värd). En varningströskel (i allmänhet 90%) ställs in. Om din LTV överstiger detta tröskelvärde finns det en risk för tvångslikvidation. Debifi kommer då att ge dig 24 timmar att reagera.



Låntagarna kommer att informeras om prissänkningen. Denna information kommer också att finnas tillgänglig på Contract:s sammanfattningssida. För att återställa den ursprungliga belåningsgraden för ett lån måste låntagaren :





- eller deponera en extra garanti ;
- återbetala hela eller delar av skulden.



I händelse av en ökning av priset på säkerheten behåller låntagaren eventuella kapitalvinster på säkerheten. Han är endast skyldig lånebeloppet, som är förutbestämt och oberoende av Bitcoin-priset.




## Återbetalning och återtagande av säkerheter



I slutet av den avtalade löptiden (eller tidigare om du vill) måste du betala tillbaka lånet.


I Debifi :





- Gå till din Contract och klicka på **Gör en återbetalning**. Ange det totala beloppet som ska betalas (kapital + ränta).





- Skicka stablecoins från din Wallet till långivarens Address som anges och återgå för att bekräfta återbetalningen på plattformen genom att kopiera **ID** för återbetalningstransaktionen till den dedikerade fliken. Detta gör det enklare för Debifi att utföra sina kontroller.



När betalningen har bekräftats av långivaren (och av dig) kommer Debifi att be dig att göra en **återbetalning**. Din Bitcoin-säkerhet frigörs och du kan återföra den från spärren till din egen portfölj.  Glöm inte att samla in alla dina Bitcoins.



Så snart du får dina bitcoins ändras lånet Contract till **Contract slutfört**.



Gratulerar, gratulerar! Du har slutfört processen.




## Bästa praxis och säkerhet



Oavsett dina mål eller motiv - finansiering av ett projekt, förvärv av egendom, köp av bitcoins osv. - var extremt försiktig innan du tar ett lån som backas upp av Bitcoin. - var extremt försiktig innan du tar ett lån som backas upp av Bitcoin. Ta dig tid att överväga ditt beslut noggrant, eftersom Bitcoin fortfarande är en volatil tillgång. **En kraftig nedgång i dess pris kan leda till tvångslikvidation av dina bitcoins**.



Övervaka ditt förhållande mellan lån och säkerhet (LTV). Ställ in varningar (BTC-pris, LTV) om möjligt. Låt inte din kvot närma sig 90 %. Om du är osäker, öka säkerheten eller återbetala i förtid.



Kontrollera dina nycklar. Förvara din BTC i en säker Wallet (helst hårdvara eller en ansedd Wallet). Ange inte en PIN-kod som är relaterad till ett viktigt datum i ditt liv och dela aldrig din återställningsfras. På Debifi anger du generate din privata nyckel i applikationen - Debifi vet inte om det.



Börja smått om möjligt. För ditt första lån, testa ett blygsamt belopp för att bekanta dig med processen.



Använd endast Debifis officiella webbplats för att hålla dig uppdaterad med Debifi-nyheter och undvik okända länkar eller phishing-länkar.  Uppdatera applikationen, skydda din smartphone med en PIN-kod och välj en kompatibel Hardware Wallet.



Alternativt, om du är en långivare, kommer den här handledningsvideon att vägleda dig genom att använda Debifi-plattformen. Från att välja låntagare som är intresserade av ditt erbjudande, till att tillhandahålla offentliga nycklar, underteckna avtal, överföra stablecoins och mer.



![video](https://youtu.be/g8iLxwI4xT0)



Du vet nu hur du använder Debifi-plattformen för att få ett lån.



Jag rekommenderar att du går den här kursen, som tar en djupgående titt på Bitcoin, Stablecoins och deras bidrag till suveränitet.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46