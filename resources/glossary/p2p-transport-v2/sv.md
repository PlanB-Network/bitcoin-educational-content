---
term: P2P TRANSPORT V2
definition: Ny version av Bitcoins P2P-protokoll med kryptering för att förbättra integriteten.
---

Ny version av transportprotokollet Bitcoin P2P som innehåller opportunistisk kryptering för att förbättra integriteten och säkerheten i kommunikationen mellan noder. Denna förbättring syftar till att Address flera problem med den grundläggande versionen av P2P-protokollet, särskilt genom att göra de utbytta uppgifterna omöjliga att skilja åt för en passiv observatör (t.ex. en internetleverantör), vilket minskar riskerna för censur och attacker genom upptäckt av specifika mönster i datapaket.


Den implementerade krypteringen inkluderar inte autentisering för att undvika att lägga till onödig komplexitet och för att inte äventyra nätverksanslutningens tillståndslösa natur. Detta nya P2P-transportprotokoll ger dock bättre säkerhet mot passiva attacker och gör aktiva attacker betydligt mer kostsamma och upptäckbara (särskilt MITM-attacker). Införandet av en pseudoslumpmässig dataström komplicerar uppgiften för angripare som vill censurera eller manipulera kommunikation.


P2P Transport V2 inkluderades som ett alternativ (inaktiverat som standard) i version 26.0 av Bitcoin Core, som distribuerades i december 2023. Den kan aktiveras med alternativet `v2transport=1` i konfigurationsfilen.