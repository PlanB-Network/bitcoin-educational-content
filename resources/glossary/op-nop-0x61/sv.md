---
term: OP_NOP (0X61)
definition: Opcode som inte ger någon effekt, används som en införingspunkt för framtida soft forks.
---

Ger ingen effekt på stacken eller skriptets tillstånd. Den utför inga rörelser, kontroller eller modifieringar. Det gör helt enkelt ingenting om inte annat beslutas via en Soft Fork. Sedan de modifierades av Satoshi Nakamoto 2010 används kommandona `OP_NOP` (`OP_NOP1` (`0XB0`) till `OP_NOP10` (`0XB9`)) för att lägga till nya opkoder i form av en Soft Fork.


Således har `OP_NOP2` (`0XB1`) och `OP_NOP3` (`0XB2`) redan använts för att implementera `OP_CHECKLOCKTIMEVERIFY` respektive `OP_CHECKSEQUENCEVERIFY`. De används i kombination med `OP_DROP` för att ta bort de associerade temporala värdena från stacken, vilket gör att skriptets exekvering kan fortsätta, oavsett om noden är uppdaterad eller inte. Kommandona `OP_NOP` gör det därför möjligt att infoga en avbrottspunkt i ett skript för att kontrollera ytterligare villkor som redan finns eller kan läggas till med framtida Soft-forks. Sedan Tapscript har användningen av `OP_NOP` ersatts av den mer effektiva `OP_SUCCESS`.