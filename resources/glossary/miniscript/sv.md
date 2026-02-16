---
term: Miniscript
definition: Ramverk som förenklar skapande, analys och verifiering av Bitcoin-skript.
---

Ramverk utformat för att tillhandahålla ett ramverk för programmering av skript på ett säkert sätt på Bitcoin. Det inbyggda språket i Bitcoin kallas script. Det är ganska komplicerat att använda i praktiken, särskilt för sofistikerade och anpassade applikationer. Framför allt är det mycket svårt att verifiera ett scripts begränsningar. Miniscript använder en delmängd av Bitcoin-skript för att förenkla skapandet, analysen och verifieringen av dem. Varje miniscript är likvärdigt 1 för 1 med ett inbyggt script. Ett användarvänligt policyspråk används, som sedan kompileras till miniscript, för att slutligen motsvara ett inbyggt skript.





Miniscript gör det alltså möjligt för utvecklare att bygga sofistikerade skript på ett säkrare och mer tillförlitligt sätt. De viktigaste egenskaperna hos Miniscript är följande:


- Det möjliggör en statisk analys av skriptet, inklusive de utgiftsvillkor som det tillåter och dess kostnad i form av resurser;
- Det gör det möjligt att skapa skript som följer konsensus;
- Det gör det möjligt att analysera om de olika utgiftsvägarna överensstämmer med nodernas standardregler eller inte;
- Den fastställer en allmän standard, begriplig och komponerbar, för all Wallet-programvara och -maskinvara.


Miniscript-projektet lanserades 2018 av Peter Wuille, Andrew Poelstra och Sanket Kanjalkar genom företaget Blockstream. Miniscript lades till i Bitcoin Core Wallet i watch-only-läge i december 2022 med version 24.0, och sedan fullt ut i maj 2023 med version 25.0.