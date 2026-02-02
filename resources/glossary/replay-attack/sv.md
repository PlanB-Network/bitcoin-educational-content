---
term: Repetitionsattack
definition: Attack som återskapar en giltig transaktion från en blockkedja på en annan som delar samma historik.
---

I samband med Bitcoin inträffar en replay-attack när en giltig transaktion på en Blockchain på ett illvilligt sätt reproduceras på en annan Blockchain som har samma transaktionshistorik. Med andra ord kan en transaktion som sänds på en kanal replikeras på en annan utan medgivande från avsändaren av den första transaktionen.


Låt oss ta ett exempel på en hypotetisk Hard Fork från Bitcoin, som heter "*BitcoinBis*". Om du gör en betalning i bitcoins för att köpa en baguette från en bagare på den verkliga Blockchain Bitcoin, kan samma bagare spela upp den legitima transaktionen på *BitcoinBis* för att få samma belopp i kryptovalutor på denna Fork, utan någon åtgärd från din sida.


Denna typ av attack kan endast inträffa om Blockchain förgrenar sig med 2 oberoende kedjor som består över tid. Vanligtvis skulle detta vara fallet med Hard Fork. För att en uppspelningsattack ska vara möjlig måste de två blockkedjorna ha en gemensam historia och den duplicerade transaktionen måste som input konsumera UTXO:er som skapats från tidigare transaktioner som ägde rum innan de två kedjorna delades, eller från tidigare transaktioner som i sig redan har spelats upp i en tidigare uppspelningsattack.


Generellt sett innebär en replay-attack inom databehandling att giltiga data fångas upp och återanvänds för att lura ett system genom att upprepa den ursprungliga överföringen. Detta kan ibland leda till identitetsstöld i ett nätverk.


> ► * När det gäller en replay-attack på en Bitcoin-transaktion kallas detta ibland helt enkelt för en "replay-transaktion". "*