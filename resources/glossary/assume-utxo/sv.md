---
term: ANTAGANDE UTXO
---

En konfigurationsparameter i den ledande Bitcoin Core-klienten som gör det möjligt för en nod som just har initialiserats (men som ännu inte har genomgått IBD) att skjuta upp verifieringen av transaktioner och UTXO-uppsättningen till en given ögonblicksbild. Konceptet bygger på användningen av en UTXO-uppsättning (en lista över alla befintliga UTXO:er vid en viss tidpunkt) som tillhandahålls av Core och som antas vara korrekt, vilket gör att noden mycket snabbt kan synkroniseras med den kedja som har mest ackumulerat arbete. Eftersom noden hoppar över det långa IBD-steget blir den operativ för sin användare mycket snabbt. Anta att UTXO delar upp synkroniseringen (IBD) i två delar:


- Först utför noden Header First Sync (verifiering av endast headers) och betraktar UTXO-uppsättningen som tillhandahålls av Core som giltig;
- När noden sedan är i drift kommer den att verifiera hela blockhistoriken i bakgrunden och uppdatera en ny UTXO-uppsättning som den själv har verifierat. Om denna nya UTXO-uppsättning inte stämmer överens med den som tillhandahålls av Core, kommer den att producera ett felmeddelande.


Antag därför att UTXO påskyndar förberedelsen av en ny Bitcoin-nod genom att skjuta upp transaktionsverifieringsprocessen och UTXO-uppsättningen genom en uppdaterad ögonblicksbild som tillhandahålls i Core.