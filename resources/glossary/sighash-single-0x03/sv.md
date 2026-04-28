---
term: SIGHASH_SINGLE (0X03)
definition: SigHash-flagga som kopplar varje signerad input till motsvarande output på samma index.
---

Typ av SigHash Flagga som används i Bitcoin-transaktionssignaturer för att ange att signaturen gäller alla inmatningar i transaktionen och endast en utmatning, som motsvarar indexet för samma inmatning som signerats. Varje inmatning som signeras med `SIGHASH_SINGLE` är således specifikt kopplad till en viss utmatning. De andra utdata är inte bundna av signaturen och kan därför ändras senare. Denna typ av signatur är användbar i komplexa transaktioner där deltagarna vill koppla vissa inmatningar till specifika utmatningar, samtidigt som de lämnar flexibilitet för transaktionens övriga utmatningar.