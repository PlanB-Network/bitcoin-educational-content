---
name: Cashu.me
description: Cashu.me guide för användning av ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Här är en videohandledning från BTC Sessions, en videoguide som går igenom hur du ställer in och använder Cashu.me Bitcoin Wallet, vilket ger dig tillgång till enkla, billiga och privata Bitcoin-transaktioner - utan behov av en appbutik!


I denna handledning kommer vi att utforska Cashu.me, en webbläsarbaserad Wallet för privata Bitcoin-betalningar med Chaumian ecash. Innan vi dyker in, låt oss ha en kort introduktion till ecash och hur det fungerar.


## Introduktion till ecash


Tänk dig att ha digitala kontanter som fungerar precis som fysiska sedlar i din ficka - privata, omedelbara och användbara peer-to-peer utan mellanhänder. Det är vad ecash möjliggör: en digital betalningsmetod som ger tillbaka integriteten hos fysiska kontanter till den digitala världen. Till skillnad från onchain-Bitcoin, som registrerar varje transaktion på en offentlig Ledger som är synlig för alla, skapar ecash privata tokens som representerar verkligt Bitcoin-värde samtidigt som dina utgiftsvanor hålls konfidentiella.


Tänk på ecash som digitala innehavarinstrument som lagras på din enhet - om du håller dem äger du dem, precis som fysiska kontanter. Dessa tokens utfärdas av betrodda tjänster som kallas `Mints` som innehar de underliggande Bitcoin-reserverna. När du använder ecash sänder du inte ut dina transaktioner till hela nätverket. Istället byter du privata tokens direkt med andra, vilket skapar en betalningsupplevelse som känns mer som att ge någon kontanter än att göra en traditionell digital betalning.


Cashu är ett Chaumian ecash-protokoll med fri och öppen källkod byggt för Bitcoin. Tekniken bygger på David Chaums banbrytande kryptografiska forskning från 1980-talet och använder "blinda signaturer" för att säkerställa integritet. När du får ecash-tokens signerar myntverket dem utan att veta var de kommer att spenderas nästa gång - en viktig funktion som förhindrar transaktionsspårning. Det är viktigt att ecash inte ersätter Bitcoin; det kompletterar det genom att ta itu med några kritiska frågor som följer med Bitcoin-arkitekturkraven. Det ger den integritet som fysiska kontanter erbjuder (vilket Bitcoin:s transparenta Ledger saknar) och möjliggör omedelbara mikrotransaktioner utan Blockchain-avgifter eller bekräftelsefördröjningar.


Ecash integreras sömlöst med Lightning Network. Du använder Lightning för att sätta in Bitcoin i ett myntverk (omvandlar ditt Bitcoin-värde till ecash-tokens) och för att ta ut senare (omvandlar tokens tillbaka till ett spenderbart Lightning-saldo). Tillsammans bildar de en kraftfull kombination: Bitcoin ger den säkra avvecklingen Layer, Lightning möjliggör snabba transaktioner och nätverksinteroperabilitet och ecash lägger till integriteten Layer som gör att digitala betalningar känns riktigt privata igen.


## Cashu.me


Cashu.me är en `Progressive Web App (PWA)` som implementerar Cashu-protokollet - en specifik implementering av Chaumian ecash utformad för Bitcoin. Som en PWA fungerar den direkt i din webbläsare utan att kräva installation från appbutiker, även om du kan "installera" den på din enhet för enklare åtkomst. Detta webbaserade tillvägagångssätt säkerställer bred kompatibilitet mellan operativsystem samtidigt som säkerheten upprätthålls genom kryptografiska protokoll snarare än plattformsbegränsningar.


## 🎉 Viktiga funktioner


Låt oss dyka in i funktionerna och utforska vad Cashu.me har att erbjuda:



- Chaumian ecash på Lightning**: Använder blinda signaturer så att myntverk inte kan spåra användarsaldon eller transaktionshistorik
- Självförvaltande av tokens**: Du kontrollerar ecash-tokens lokalt med din seed-fras
- Säkerhetskopior av seed-fras**: 12-ords återställningsfras för återställning av Wallet
- Oberoende av myntverk**: Fungerar med flera oberoende myntverk - du är inte låst till en leverantör
- Omedelbara, kostnadsfria transaktioner**: Inom samma myntsystem slutförs betalningar på några sekunder utan avgifter
- Sekretesskyddande arkitektur**: Mints kan inte se vem som gör transaktioner med vem
- Offline ecash**: Skicka/ta emot polletter via ett lokalt överföringsprotokoll, som NFC, QR-kod, Bluetooth etc. utan internetanslutning
- Upptäck ecash-mynt via Nostr**: Hitta och verifiera betrodda mynthanterare via Nostr-protokollet
- Byt ecash mellan myntverk**: Alla myntverk talar Lightning, vilket innebär att du kan överföra värde mellan dem.
- Fjärrstyr din Wallet med Nostr Wallet Connect (NWC)**: Anslut till andra appar som Nostr Client och börja zappa via NWC


Den kritiska avvägningen är "förtroende": medan du kontrollerar själva symbolerna måste du lita på att myntverk förvaltar de underliggande Bitcoin-reserverna. Som Cashus dokumentation säger:


> ... myntet driver Lightning-infrastrukturen och förvarar satoshis för myntens ecash-användare. Användare måste lita på att myntet Redeem deras ecash när de vill byta ut till Lightning.

- Cashu-dokumentation, [Allmänna frågor om säkerhet och sekretess](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Detta gör ecash till en depåförvaringslösning för själva Bitcoin, även om du behåller full kontroll över tokens.


## 1️⃣ Initial inställning


① Börja med att besöka [Wallet.cashu.me](https://Wallet.cashu.me) i din webbläsare. Eftersom Cashu.me är en `PWA` behöver du inte ladda ner den från appbutiker, utan bara öppna webbplatsen direkt i din webbläsare. För enklare åtkomst kan du välja att installera den på din enhets startskärm.


för att installera PWA, tryck på menyknappen ⋮ i din webbläsare och välj "Lägg till på startskärmen". När installationen är klar stänger du webbläsarfliken och startar Cashu.me från enhetens startskärm. På välkomstskärmen trycker du på `Nästa` för att fortsätta.


③ Säkerhet är avgörande. Förvara din seed-fras säkert i en lösenordshanterare eller, ännu bättre, skriv ner den på papper. Denna återställningsfras på 12 ord är det enda sättet att få tillbaka pengar om du förlorar åtkomsten till den här enheten. Tryck på ikonen 👁️ för att visa din seed-fras, skriv noggrant ner alla 12 orden i ordning och kryssa sedan i rutan "Jag har skrivit ner den". Tryck på `Nästa` för att fortsätta och markera rutan för att bekräfta att du accepterar `villkoren` på följande skärm.


![image](assets/en/01.webp)


När du har slutfört installationen måste du ansluta till en `Mint`. Tryck på `ADD MINT` följt av `DISCOVER MINTS` för att se mints som rekommenderas av Nostr-communityn. För ytterligare verifiering kan du granska myntens betyg på [bitcoinmints.com](bitcoinmints.com).


Tryck sedan på `Klicka för att bläddra bland mints` för att se hela listan. Välj en mynta genom att kopiera dess URL, klistra in den i URL-fältet och ge den ett igenkännligt namn. I det här exemplet använder vi:


URL: `https://mint.minibits.cash/Bitcoin`

Namn: `Minibits`


![image](assets/en/02.webp)


Tryck på `ADD MINT` för att slutföra processen. På bekräftelseskärmen, verifiera att du litar på den här myntens operatör och tryck sedan på `ADD MINT` igen. Minibits mint kommer nu att visas på din startskärm. När din Wallet har konfigurerats måste du sätta in pengar på den innan du kan göra transaktioner.


![image](assets/en/03.webp)


## 2️⃣ Finansiering av din Wallet


Cashu.me erbjuder två olika metoder för att finansiera din Wallet. När du trycker på `Mottag` på startskärmen ser du alternativ för att ta emot pengar via `ECASH` eller via `LIGHTNING.` Låt oss utforska båda alternativen.


![image](assets/en/04.webp)


### Finansiering via LIGHTNING


Det första alternativet är att finansiera Wallet via Lightning Invoice. `Välj ett myntverk` om du har lagt till olika myntverk och definiera det `belopp (Sats)` du vill ta emot. Tryck sedan på `SKAPA Invoice.` Nu får du en QR-kod som du kan skanna med en annan blixt Wallet eller så kan du helt enkelt `Kopiera` Invoice och klistra in i en annan Wallet för att betala och finansiera din cashu.me Wallet.


![image](assets/en/05.webp)


### Mottagande av ecash


Med ecash-metoden kan du ta emot tokens direkt från en annan ecash Wallet. Börja med att trycka på `Receive`-knappen och välj `ECASH`-alternativet. Du kommer att kunna `Pasta` eller `Scan` eller använda `NFC` för att skicka en Cashu token från en annan Wallet. Om du väljer att klistra in, ange token-strängen som du har kopierat från en annan Wallet, kommer `Amount` och `Mint` automatiskt att visas. Tryck på `RECEIVE` för att slutföra transaktionen, och Sats kommer att visas i din Wallet. Observera att ditt saldo nu är fördelat över flera myntverk. Du kan t.ex. ha 1 000 Sats i din Minibits `Mint` och ytterligare 1 000 Sats i en Coinos `Mint`. Denna separation mellan olika myntverk är en viktig aspekt av Cashus arkitektur.


![image](assets/en/06.webp)


### Byte mellan minttabletter


Om du inte längre litar på ett visst myntverk som du har lagt till, erbjuder cashu.me en funktion för att `byta` pengar från ett myntverk till ett annat. Navigera till fliken myntverk och skrolla ner tills du ser `Multimint Swaps`. Välj myntverket `FRÅN` och `TILL` från rullgardinsmenyerna och ange det belopp du vill överföra. Tryck på `SWAP` för att flytta tokens mellan mints. Detta kommer att utföras via Lightning-transaktion, så du måste lämna utrymme för potentiella Lightning-avgifter. I mitt exempel räckte det med 1 sat.


![image](assets/en/07.webp)


## 3️⃣ Sändning av medel


För att skicka Sats erbjuder Cashu.me två alternativ. Att skicka via `ecash` eller via `blixt`. Låt oss ta en titt på båda alternativen.


### Sändning via Lightning


Följ dessa steg för att skicka via Lightning:


1. Tryck på "SEND" på hemskärmen och välj "Blixten

2. Appen kommer att uppmana dig att ange en `Lightning Invoice` eller `-Address`. Du kan klistra in Invoice/Address direkt, eller använda alternativet skanna QR-kod för att fånga den visuellt och sedan bekräfta med `ENTER`

3. Välj det myntverk som du vill betala från med hjälp av rullgardinsmenyn och tryck på "BETALA" för att bekräfta. **Note**: det finns också ett alternativ att använda `Multinut` under `Settings` -> `Experimental` som gör att du kan betala fakturor från flera myntverk samtidigt.

4. När du har slutfört betalningen ser du en betalningsbekräftelse och det belopp som dragits från ditt saldo.


![image](assets/en/08.webp)


### Skickar via ecash


Att skicka ecash är på samma sätt okomplicerat.


1. Tryck på `SEND` och välj den här gången alternativet `ECASH`.

2. "Välj en myntautomat" och ange det "belopp" du vill skicka i Sats och tryck på "Skicka" för att bekräfta

3. Detta skapar en "animerad QR-kod" som du kan anpassa genom att justera parametrarna för hastighet och storlek. Vem som helst kan skanna denna QR-kod för att Redeem Sats omedelbart, eller så kan du trycka på COPY för att skicka token-strängen till någon annan via alternativa kanaler som Bluetooth, NFC eller standardmeddelanden.

4. Jag öppnar en annan Wallet. Klistra in från klippbordet och välj `Motta ecash` i den andra Wallet.


![image](assets/en/09.webp)


## 4️⃣ Ytterligare funktioner


Utöver kärnfunktionerna för sändning och mottagning erbjuder Cashu.me kraftfulla tilläggsfunktioner som förbättrar din Bitcoin-upplevelse inom Nostrs ekosystem.


### Nostr Wallet Anslut


Nostr Wallet Connect (`NWC`) förändrar hur du interagerar med Nostr-applikationer genom att skapa en sömlös anslutning mellan din Wallet och sociala appar. Detta protokoll gör det möjligt för applikationer som [Damus](https://damus.io/) eller [Primal](https://primal.net/home) att begära betalningar direkt via Nostr-reläer utan att du behöver lämna appen.


Att sätta upp `NWC` i Cashu.me:


1. Gå till "Inställningar" på den övre vänstra Hamburger-menyn

2. Bläddra till avsnittet "NOSTR Wallet CONNECT" och tryck på knappen "Aktivera

3. Du kommer sedan att sätta en ersättning för att fastställa det maximala belopp som applikationer kan spendera från din Wallet.

4. När du har konfigurerat den kan du kopiera anslutningssträngen och klistra in den i vilken Nostr-klient som helst som stöder `NWC`, vilket möjliggör omedelbar zapping och tipping-funktionalitet.


![image](assets/en/10.webp)


### Blixten Address via npub.cash


Cashu.me integreras med [npub.cash](https://npub.cash/) för att ge dig en Lightning Address som fungerar sömlöst med Nostr-protokollet. Här kan du registrera dig och göra anspråk på ditt användarnamn genom att tillhandahålla din Nostr `nsec`, som kostar 5.000 Sats och stöder npub.cash-projektet, eller så kan du använda vilken Nostr-offentlig nyckel som helst (`npub`) utan registrering.


Gå först till `Inställningar` och tryck på `Aktivera` Blixt Address med npub.cash. Detta kommer att generate en npub.cash Address med en `npub`-sträng som härrör från din Wallet seed-fras som standard.


Alternativt kan du besöka [den här webbsidan](https://npub.cash/username) för att få ett anpassat användarnamn med din egen Nostr `nsec`, vilket ger dig en personlig Lightning Address som username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Slutsats


Cashu.me levererar privata Bitcoin-betalningar som fungerar som fysiska kontanter - omedelbart och peer-to-peer utan att avslöja din transaktionshistorik. Jag uppskattar personligen dess PWA-arkitektur eftersom den fungerar utan begränsningar från appbutiker. Genom att kombinera säkerheten hos Bitcoin, hastigheten hos Lightning och integriteten hos ecash erbjuder Wallet användningsfall som kan förbättra den dagliga användningen av Bitcoin.


Även om du har full kontroll över dina ecash-tokens genom självförvaring, kom ihåg att mints fungerar som betrodda tredje parter som håller de underliggande Bitcoin-reserverna. Möjligheten att använda flera myntverk och byta mellan dem ger flexibilitet samtidigt som integriteten upprätthålls.


Tack vare funktioner som NWC och npub.cash-adresser är Cashu.me ett tilltalande Wallet-alternativ för sociala klienter som värdesätter integritet och suveränitet över stora tekniska policybegränsningar.


## 📚 Resurser


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)