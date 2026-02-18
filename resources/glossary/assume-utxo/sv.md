---
term: Assume utxo
definition: En Bitcoin Core-parameter som möjliggör snabb synkronisering av en ny nod genom att använda en ögonblicksbild av UTXO-uppsättningen antagen giltiga, innan historikverifiering i bakgrunden.
---
Konfigurationsparameter i majoritetsklienten Bitcoin Core som gör det möjligt för en nod som just har initierats (men som ännu inte har gjort IBD) att skjuta upp verifieringen av transaktioner och UTXO-setet före en viss snapshot. Konceptet bygger på användningen av ett UTXO-set (lista över alla befintliga UTXO:er vid en given tidpunkt) som tillhandahålls av Core och antas vara korrekt, vilket gör att noden kan synkroniseras mycket snabbt på kedjan med mest ackumulerat arbete. Eftersom noden hoppar över det långa IBD-steget blir den mycket snabbt funktionell för sin användare.

Assume UTXO delar upp synkroniseringen (IBD) i två delar: Först utför noden Header First Sync (endast verifiering av huvuden) och betraktar det UTXO-set som tillhandahålls av Core som giltigt; Sedan, när den är funktionell, kommer noden att verifiera hela blockhistoriken i bakgrunden och uppdatera ett nytt UTXO-set som den själv har verifierat. Om det sistnämnda inte stämmer överens med det UTXO-set som tillhandahålls av Core kommer den att ge ett felmeddelande.

Assume UTXO gör det alltså möjligt att påskynda förberedelsen av en ny Bitcoin-nod genom att skjuta upp verifieringsprocessen för transaktioner och UTXO-setet tack vare en uppdaterad snapshot som tillhandahålls i Core.







