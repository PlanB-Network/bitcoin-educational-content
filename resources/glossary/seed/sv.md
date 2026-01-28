---
term: Seed
definition: 512-bitars information som gör det möjligt att generera alla nycklar för en HD Bitcoin-plånbok.
---

I det specifika sammanhanget med en hierarkisk deterministisk Bitcoin-portfölj är en seed en 512-bitars informationsbit som härrör från en slumpmässig händelse. Den används för att deterministiskt och hierarkiskt generate en uppsättning privata nycklar, och deras motsvarande offentliga nycklar, för en Bitcoin-portfölj. seed förväxlas ofta med själva återställningsfrasen. Men det är inte samma sak. seed erhålls genom att tillämpa funktionen `PBKDF2` på Mnemonic-frasen och alla passphrase.


seed uppfanns med BIP32, som definierade grunderna för den hierarkiska deterministiska portföljen. I den här standarden mätte seed 128 bitar. Detta gör att alla nycklar i en portfölj kan härledas från en enda information, till skillnad från JBOK-portföljer (*Just a Bunch Of Keys*), som kräver nya säkerhetskopior för varje nyckel som genereras. BIP39 föreslog sedan en kodning av denna seed för att förenkla läsningen av den för människor. Denna kodning sker i form av en fras, allmänt kallad Mnemonic-fras eller återställningsfras. Denna standard undviker fel när seed sparas, särskilt tack vare användningen av en kontrollsumma.


Utanför sammanhanget Bitcoin, inom kryptografi i allmänhet, är en seed ett initialt värde som används för att generate kryptografiska nycklar, eller mer allmänt, alla typer av data som produceras av en pseudoslumpmässig nummergenerator. Detta initiala värde måste vara slumpmässigt och oförutsägbart för att garantera säkerheten i det kryptografiska systemet. seed introducerar visserligen entropi i systemet, men den efterföljande genereringsprocessen är deterministisk.


> ► * I vanligt språkbruk hänvisar majoriteten av bitcoiners till Mnemonic-frasen när de talar om "seed", och inte till det mellanliggande derivationstillstånd som ligger mellan Mnemonic-frasen och huvudnyckeln.*