---
term: SPV-nod (lätt nod)
definition: Lätt klient som validerar transaktioner genom att endast lagra blockhuvuden och verifiera Merkle-bevis.
---

En SPV-nod (*Simple Payment Verification*), ibland kallad "light-nod", är en lättviktsklient till en Bitcoin-nod som gör det möjligt för användare att validera transaktioner utan att behöva lagra hela Blockchain. Istället lagrar en SPV-nod endast blockhuvudena och hämtar information om specifika transaktioner genom att vid behov fråga fullständiga noder. Denna verifieringsprincip möjliggörs av strukturen hos transaktioner i Bitcoin-block, som är organiserade i en kryptografisk ackumulator (Merkle Tree).


Detta tillvägagångssätt är fördelaktigt för enheter med begränsade resurser, t.ex. mobiltelefoner. SPV-noder är dock beroende av fullständiga noder för att få tillgång till information, vilket innebär en extra nivå av förtroende och därmed lägre säkerhet jämfört med fullständiga noder. SPV-noder kan inte validera transaktioner autonomt, men de kan verifiera om en transaktion ingår i ett block genom att konsultera Merkle-bevis.