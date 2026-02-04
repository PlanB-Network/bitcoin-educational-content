---
term: Resynkronisering
definition: Ersättning av en del av blockkedjan med en konkurrerande kedja som har mer ackumulerat arbete.
---

Avser ett fenomen där Blockchain genomgår en modifiering av sin struktur på grund av att det finns konkurrerande block på samma höjd. Detta inträffar när en del av Blockchain ersätts av en annan kedja med en större mängd ackumulerat arbete.


Dessa resynkroniseringar är en del av Bitcoin:s naturliga funktion, där olika gruvarbetare kan hitta nya block nästan samtidigt och därmed dela Bitcoin-nätverket i två. I sådana fall kan nätverket tillfälligt delas upp i konkurrerande kedjor. Så småningom, när en av dessa kedjor ackumulerar mer arbete, överges de andra kedjorna av noderna och deras block blir vad som kallas "föråldrade block" eller "föräldralösa block" Denna process där en kedja ersätts med en annan kallas resynkronisering.





Resynkroniseringar kan få olika konsekvenser. För det första, om en användare fick en transaktion bekräftad i ett block som visar sig vara övergivet, men den här transaktionen inte finns i den slutligen giltiga kedjan, blir deras transaktion obekräftad igen. Det är därför som det rekommenderas att alltid vänta på minst 6 bekräftelser för att betrakta en transaktion som verkligt oföränderlig. Efter 6 djupa block är resynkroniseringar så osannolika att risken för att en sådan ska inträffa kan betraktas som praktiskt taget noll.


På global systemnivå innebär resynkroniseringar dessutom ett slöseri med minrarnas beräkningskraft. När en split inträffar kommer vissa miners att vara on chain `A` och andra on chain `B`. Om kedja `B` till slut överges under en resynkronisering, är all beräkningskraft som används av gruvarbetarna på denna kedja per definition bortkastad. Om det sker för många resynkroniseringar i Bitcoin-nätverket minskar därför nätverkets övergripande säkerhet. Det är delvis därför som det kan vara farligt att öka blockstorleken eller minska intervallet mellan varje block (10 minuter).


> ► *Vissa bitcoiners föredrar att använda "Orphan block" för att referera till ett block som löpt ut. Även om det är en anglicism, är en "omorganisation" eller en "reorg" i vanligt språkbruk ofta att föredra framför "resynkronisering"*