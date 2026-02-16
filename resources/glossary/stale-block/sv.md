---
term: Förældat (block)
definition: Giltigt block som exkluderas från huvudkedjan när två miners hittar ett block på samma höjd samtidigt.
---

Avser ett block utan barn: ett giltigt block, men uteslutet från den huvudsakliga Bitcoin-kedjan. Det inträffar när två gruvarbetare hittar ett giltigt block på samma kedjehöjd inom en kort tidsperiod och sänder det över nätverket. Noderna väljer så småningom endast ett block att inkludera i kedjan, enligt principen att den kedja som har mest ackumulerat arbete gör den andra "föråldrad". Processen som leder till produktionen av ett föråldrat block är som följer:


- Två gruvarbetare hittar ett giltigt block med samma kedjehöjd inom ett kort tidsintervall. Vi kallar dem "Block A" och "Block B";
- Var och en sänder sitt block till Bitcoin-nodnätverket. Varje nod har nu 2 block på samma höjd. Därför finns det två giltiga kedjor;
- Miners fortsätter att söka efter arbetsbevis för följande block, men för att göra det måste de nödvändigtvis välja endast ett block mellan "Block A" och "Block B" som de ska minera;
- En Miner hittar så småningom ett giltigt block ovanför `Block B`. Låt oss kalla det `Block B+1`;
- De sänder `Block B+1` till nätverksnoderna;
- Eftersom noderna följer den längsta kedjan (med mest ackumulerat arbete) kommer de att uppskatta att "kedja B" är den som ska följas;
- De kommer att överge `Block A` som inte längre är en del av huvudkedjan. Det har därmed blivit ett föråldrat block.





