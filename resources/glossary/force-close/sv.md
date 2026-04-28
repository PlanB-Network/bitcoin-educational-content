---
term: Forcerad stängning
definition: Ensidig stängning av en Lightning-kanal genom att sända ut den senaste signerade åtagandetransaktionen.
---

Icke-kooperativ stängningsmekanism för Lightning-kanaler. När två användare öppnar en kanal med en Multisig 2/2, kan var och en ensidigt stänga kanalen genom att sända den sista Commitment Transaction som redan har signerats, för att återfå sina bitcoins i kedjan. Detta är känt som "force close".


Den här metoden används vanligtvis om en av deltagarna inte längre svarar eller om det är omöjligt att stänga kanalen tillsammans. Om force close kan undvikas är det bäst, eftersom det tar längre tid att återfå onchain-medel och kan vara mycket dyrare när det gäller avgifter.


I en force close sänder en av de två användarna Commitment Transaction, vilket återspeglar det senast kända tillståndet för Lightning-kanalen. Det finns sedan en tidslåsning innan bitcoins kan hämtas på kedjan, vilket ger den andra parten tid att verifiera att transaktionen motsvarar det senaste kanaltillståndet. Om en användare försöker fuska genom att publicera en föråldrad Commitment Transaction kan den andra parten använda återkallelsehemligheten för att straffa fuskaren och återfå alla medel i kanalen.