---
term: Sighash-flagga
definition: Parameter som bestämmer vilka komponenter i en transaktion som täcks av signaturen.
---

En parameter i en Bitcoin-transaktion som avgör vilka komponenter i en transaktion (inmatningar och utmatningar) som omfattas av den associerade signaturen och därmed blir oföränderliga. SigHash Flag är en byte som läggs till den digitala signaturen för varje inmatning. Valet av SigHash-flagga påverkar därför direkt vilka delar av transaktionen som fryses av signaturen och vilka som fortfarande kan ändras i efterhand. Denna mekanism säkerställer att signaturer på ett exakt och säkert sätt binder transaktionsdata i enlighet med undertecknarens avsikt. Det finns tre huvudsakliga SigHash-flaggor:



- `SIGHASH_ALL` (`0x01`): Signaturen gäller för alla in- och utgångar i transaktionen och låser dem därmed helt och hållet;



- `SIGHASH_NONE` (`0x02`): Signaturen gäller för alla ingångar men ingen av utgångarna, vilket gör att utgångarna kan ändras efter signaturen;



- `SIGHASH_SINGLE` (`0x03`): Signaturen täcker alla ingångar och endast en utgång som motsvarar indexet för den signerade ingången.


Förutom dessa tre SigHash-flaggor kan modifieraren `SIGHASH_ANYONECANPAY` (`0x80`) kombineras med var och en av de tidigare typerna. När denna modifierare används signeras endast en del av ingångarna, vilket gör att de övriga kan modifieras. Här är de befintliga kombinationerna med modifieraren:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Signaturen gäller för en enda inmatning samtidigt som den täcker alla utmatningar i transaktionen;



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Signaturen täcker en enda input, utan att förbinda sig till någon output;



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Signaturen gäller för en enda inmatning och endast för den utmatning som har samma index som denna inmatning.


> ► *En synonym som ibland används för "SigHash" är "Signature Hash Types"*