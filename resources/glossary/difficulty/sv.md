---
term: Svårighetsgrad
definition: Justerbar parameter som bestämmer brytningens komplexitet, justeras var 2016e block.
---

En justerbar parameter som bestämmer komplexiteten i Proof of Work som krävs för att lägga till ett nytt block i Blockchain och få den tillhörande belöningen. Denna svårighet representeras av svårighetsmålet, ett 256-bitarsvärde som anger den övre gräns som blockhuvudets Hash måste uppfylla för att anses vara giltig. Målet är att Hash, som uppnås genom en dubbel exekvering av SHA256 (SHA256d), ska vara mindre än eller lika med detta mål. För att nå denna Hash manipulerar utvinnare `Nonce` i blockhuvudet. Svårighetsgraden justeras vart 2016:e block, eller ungefär varannan vecka, för att hålla den genomsnittliga blockskapandetiden på cirka 10 minuter.