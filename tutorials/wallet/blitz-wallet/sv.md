---
name: Blitz Wallet
description: Den enklaste Bitcoin-plånboken.
---

![cover](assets/cover.webp)

Användarupplevelsen är en av de avgörande faktorerna när man väljer en Bitcoin-plånbok. I den här handledningen presenterar vi Blitz Wallet, en plånbok som sätter enkelhet i centrum för sin approach: tack vare integrationen av **Spark**-protokollet erbjuder Blitz dig en av de enklaste och mest kompletta Bitcoin-plånböckerna på marknaden, med omedelbara betalningar och utan teknisk hantering.

## Vad är Blitz Wallet?

Blitz Wallet är en **self-custodial** och **open source** Bitcoin-plånbok som satsar på din suveränitet och en smidig och intuitiv användarupplevelse.

[Blitz Wallet](https://blitz-wallet.com/) är en mobilapplikation tillgänglig på Android (Play Store) och iOS (App Store).

Till skillnad från traditionella Lightning-plånböcker som kräver hantering av betalningskanaler och inkommande likviditet, förlitar sig Blitz Wallet på **Spark-protokollet** för att eliminera dessa tekniska komplexiteter. Resultatet: omedelbara betalningar från och med den första mottagna satoshin, utan någon föregående konfiguration. Målet med Blitz är att göra Bitcoin-betalningar lika enkla som en vanlig betalningsapp, utan att någonsin kompromissa med self-custody av dina medel.

Blitz Wallet stöder även **läsbara adresser** i formatet `användare@domän.com` (via LNURL), vilket gör det möjligt att skicka bitcoin lika enkelt som ett e-postmeddelande, utan att behöva hantera långa invoices eller QR codes vid varje transaktion.

## Förstå Spark-protokollet

Innan vi går vidare till det praktiska är det användbart att förstå teknologin som driver Blitz Wallet under huven: **Spark-protokollet**.

### Vad är Spark?

Spark är ett open source överlagersprotokoll byggt på Bitcoin, utvecklat av teamet bakom Lightspark. Det möjliggör omedelbara transaktioner till låg kostnad, samtidigt som self-custody av dina bitcoin bevaras.

Till skillnad från Lightning Network som bygger på **betalningskanaler** mellan två parter, använder Spark en teknologi som kallas **statechain** (tillståndskedja). Den grundläggande principen är följande: istället för att flytta bitcoin på blockkedjan vid varje transaktion, överför Spark **rätten att spendera** från en användare till en annan, utan on-chain-rörelse.

### Hur fungerar det?

För att förstå Spark på ett intuitivt sätt, låt oss föreställa oss att det krävs att man löser ett pussel med två bitar för att spendera en bitcoin på Spark:
- En bit innehas av användaren (till exempel Alice).
- Den andra biten innehas av en grupp operatörer som kallas **Spark Entity (SE)**.

Bara kombinationen av de två matchande bitarna gör det möjligt att spendera bitcoin.

När Alice vill skicka sina bitcoin till Bob händer följande: ett nytt pussel skapas gemensamt mellan Bob och SE. Pusslet behåller samma form, men bitarna som utgör det ändras. Nu är det Bobs bit som matchar SE:s bit. Alices gamla bit blir oanvändbar, eftersom SE har förstört sin motsvarande bit. Äganderätten till bitcoin har bytt händer, **utan någon transaktion på blockkedjan**.

Bob kan sedan upprepa samma process för att skicka dessa bitcoin till Carol, och så vidare. Varje överföring fungerar genom att pusselbitar byts ut, inte genom on-chain-förflyttning av medel.

### Varför är det säkert?

En berättigad fråga uppstår: vad händer om SE inte faktiskt förstör sin gamla bit?

Spark Entity är inte en enskild entitet: det är en grupp oberoende operatörer. SE:s bit innehas aldrig av en enda operatör. Att byta ut pusslet kräver samarbete mellan flera operatörer. Det räcker att **en enda operatör är ärlig** vid en överföring för att förhindra återaktivering av ett gammalt pussel. Ingen enskild operatör kan i hemlighet behålla ett gammalt aktivt pussel eller återskapa det senare.

Dessutom har Spark en mekanism för ensidig utträde: du kan alltid hämta tillbaka dina bitcoin on-chain utan SE:s medverkan. Denna reservmekanism är en integrerad del av Sparks arkitektur och garanterar att du aldrig är beroende av nätverket för att komma åt dina medel.

### Spark vs Lightning Network

Spark och Lightning konkurrerar inte med varandra: de är **kompletterande**. Blitz Wallet integrerar båda, vilket gör att du kan dra nytta av fördelarna med var och en.

|                               | **Spark**                      | **Lightning Network**  |
| ----------------------------- | ------------------------------ | ---------------------- |
| **Teknologi**                 | Statechains (tillståndskedjor) | Betalningskanaler      |
| **Kanalhantering**            | Krävs ej                       | Krävs                  |
| **Inkommande likviditet**     | Krävs ej                       | Krävs                  |
| **Omedelbara transaktioner**  | Ja                             | Ja                     |
| **Self-custody**              | Ja                             | Ja                     |
| **Lightning-kompatibilitet**  | Ja (via atomic swaps)          | Nativt                 |

Lightning Network förblir ett utmärkt protokoll för omedelbara betalningar, men det medför tekniska begränsningar (kanalhantering, inkommande likviditet, nod online...) som kan avskräcka nybörjare. Spark eliminerar dessa begränsningar samtidigt som det förblir kompatibelt med Lightning.

## Installation och konfiguration

I den här handledningen utgår vi från Android-versionen av Blitz Wallet, men alla processer som presenteras nedan gäller även för iOS.

![installation](assets/fr/01.webp)

Eftersom Blitz Wallet är en self-custody-plånbok har du valet att **skapa en ny plånbok** eller **importera en återställningsfras** (12 eller 24 ord) från en befintlig plånbok.

Här väljer vi att skapa en ny plånbok. Nedan hittar du våra rekommendationer för säkerhetskopiering av din återställningsfras:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **VIKTIGT**: Dessa 12 eller 24 återställningsord är **den enda nyckeln till dina bitcoin**. Blitz är en self-custodial plånbok: varken Blitz eller Spark har tillgång till din återställningsfras eller dina medel. Om du förlorar dessa ord kommer du permanent att förlora åtkomsten till dina bitcoin. Dela dem aldrig med någon: den som har dem kan spendera dina bitcoin.

Skapa sedan en **PIN-kod** för att säkra åtkomsten till din plånbok.

![setup-wallet](assets/fr/02.webp)

## Komma igång med Blitz

Att genomföra transaktioner med Blitz är mer intuitivt än i de flesta andra Bitcoin-plånböcker. Gränssnittet är minimalistiskt och centrerat kring tre huvudsakliga åtgärder: skicka, skanna och ta emot.

### Ta emot bitcoin

För att ta emot bitcoin på din Blitz-plånbok, klicka på ikonen **"Pil ned"** (↓), ange beloppet i satoshis som du vill ta emot, lägg till en valfri beskrivning, och plånboken genererar en faktura (invoice) som du kan dela med avsändaren.

⚠️ **OBS**: En satoshi (eller "sat") är den minsta enheten av bitcoin: **1 bitcoin = 100 000 000 satoshis**.

En av särdragen hos Blitz Wallet är att den stöder flera nätverk och protokoll inom Bitcoin-ekosystemet:

- **Lightning Network**: Ett av Bitcoins överlager som möjliggör omedelbara mikrobetalningar med mycket låga avgifter. Idealiskt för små vardagliga belopp.

- **Bitcoin (on-chain)**: Bitcoinprotokollets huvudblockkedja, anpassad för transaktioner med större belopp där maximal säkerhet och slutgiltighet är prioriterade.

- **Liquid Network**: En sidechain (parallellkedja) till Bitcoin utvecklad av Blockstream, som möjliggör snabba och konfidentiella transaktioner med Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Som standard genererar Blitz en Lightning-faktura, men du kan välja vilket nätverk du vill ta emot dina satoshis på genom att klicka på knappen **"Choose format"** (Välj format).

![receive-sats](assets/fr/03.webp)

### Skapa kontakter

Blitz Wallet förenklar återkommande Bitcoin-överföringar tack vare sitt kontaktsystem.

I menyn **Contacts** kan du spara Blitz-användarnamn eller Lightning-adresser (LNURL) som du ofta interagerar med.

Du kan sedan skicka satoshis till dessa adresser med några klick, utan att behöva skanna en QR code eller manuellt ange en adress varje gång.

### Skicka bitcoin

Utöver de klassiska metoderna för att skicka bitcoin (skanna QR code, manuell adressinmatning) erbjuder Blitz flera praktiska alternativ:

- **Från en bild** (*From Image*): Importera en QR code från ditt fotogalleri.
- **Från urklipp** (*From Clipboard*): Klistra in en adress eller en tidigare kopierad faktura.
- **Manuell inmatning** (*Manual Input*): Ange direkt en Bitcoin-adress, en Lightning-faktura eller en läsbar adress (till exempel `användare@walletofsatoshi.com`).
- **Från dina kontakter**: Välj en förinställd mottagare för att skicka med några klick.

I menyn **Wallet**, klicka på knappen **"Pil upp"** (↑), välj din sändningsmetod, ange beloppet att skicka, lägg till en beskrivning och bekräfta transaktionen.

Minimibeloppet för att göra en överföring är för närvarande **1 000 satoshis**.

![send-bitcoin](assets/fr/05.webp)

## Blitz-butiken

Utöver Bitcoin-överföringar integrerar Blitz Wallet en butik där du kan spendera dina bitcoin för att köpa digitala tjänster direkt från applikationen.

Från huvudmenyn, klicka på fliken **Store** för att komma till butiken. Där hittar du även en länk till plattformen **Bitrefill** som gör det möjligt att köpa presentkort hos tusentals handlare över hela världen, direkt med bitcoin.

- **Artificiell intelligens**: Få tillgång till de senaste generativa AI-modellerna (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) och betala dina krediter direkt i satoshis. Flera abonnemang finns tillgängliga beroende på dina behov (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonyma SMS**: Skicka och ta emot SMS över hela världen utan att avslöja ditt personliga telefonnummer. Tjänsten faktureras i satoshis för varje skickat meddelande.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Skydda din integritet online genom att teckna ett VPN WireGuard-abonnemang (veckovis, månadsvis eller kvartalsvis), betalbart med bitcoin direkt från Blitz-butiken. Du behöver bara ladda ner WireGuard-klientapplikationen på din enhet för att komma igång.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet bakom kulisserna: gå djupare

Bakom Blitz Wallets användarvänlighet döljer sig en genomtänkt teknisk arkitektur som kombinerar flera lager av Bitcoin-ekosystemet.

### Fördelningen av ditt saldo

Blitz Wallet hanterar ditt saldo transparent genom att fördela dina medel mellan de olika protokollen beroende på behov. När ditt saldo är under 500 000 satoshis använder Blitz **Liquid Network** och atomic swaps för att erbjuda en smidig upplevelse och möjliggöra transaktioner på Lightning Network även med små belopp.

Detta tillvägagångssätt garanterar en enkel start för nya användare, utan att de behöver förstå de underliggande mekanismerna. Du kan se fördelningen av ditt saldo mellan de olika lagren i menyn **Inställningar > Balance Info**.

![balance](assets/fr/09.webp)

### Lightning-läge (valfritt)

Som standard använder Blitz Wallet Liquid Network och Spark-protokollet för att erbjuda en smidig upplevelse utan teknisk konfiguration. Blitz ger dig dock möjligheten att aktivera **Lightning-läget** som automatiskt öppnar en betalningskanal när du når ett saldo på **500 000 satoshis** (0,005 BTC).

För att aktivera Lightning-läget, gå till **Inställningar**, sedan under avsnittet **Tekniska inställningar**, klicka på alternativet **Node Info**.

![enable-lightning](assets/fr/10.webp)

Tack vare Spark-protokollet är denna aktivering **valfri**: Spark möjliggör redan Lightning-kompatibla betalningar utan att man behöver öppna en kanal eller hantera inkommande likviditet. Det nativa Lightning-läget är fortfarande användbart för avancerade användare som vill ha sin egen Lightning-nod integrerad i applikationen.

### Kassasystem (PoS)

Blitz Wallet integrerar en **kassasystemfunktion** som gör det möjligt för handlare att ta emot Bitcoin-betalningar direkt från applikationen.

I menyn **Inställningar > Point-of-sale** kan du konfigurera:

- Den unika identifieraren för din butik
- Den lokala fiatvalutan att visa priser i
- Instruktioner för dina anställda
- Dricksalternativet för dina kunder

Dina kunder behöver bara skanna den genererade QR code:n för att genomföra sin Bitcoin-betalning omedelbart.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Resurser som använts för att skriva denna handledning:
- Blogg av [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
