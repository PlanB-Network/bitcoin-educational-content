---
term: BIP0156
definition: Dandelion, ett protokoll som förbättrar integriteten vid transaktionsrutning genom att dölja den ursprungliga noden.
---

Förslag, känt som Dandelion, som syftar till att förbättra integriteten för transaktionsrouting i Bitcoin-nätverket för att motverka avanonymisering. I standarddriften av Bitcoin sänds transaktioner omedelbart till flera noder. Om en observatör kan se varje transaktion som vidarebefordras av varje nod i nätverket, kan de anta att den första noden som skickar en transaktion också är ursprungsnoden för den transaktionen, och därför att den kommer från nodens operatör. Detta fenomen skulle potentiellt kunna göra det möjligt för observatörer att koppla samman transaktioner, som normalt är anonyma, med IP-adresser.


Målet med BIP156 är att Address ska lösa detta problem. För att göra detta införs en ytterligare fas i sändningen för att bevara anonymiteten innan den sprids till allmänheten. Således använder Dandelion först en "stem"-fas där transaktionen skickas genom en slumpmässig väg av noder, innan den sänds till hela nätverket i "fluff"-fasen. Stammen och fluffen är referenser till beteendet hos transaktionens spridning genom nätverket, som liknar formen på en maskros (*en dandelion* på engelska).


Denna routingmetod döljer spåret som leder tillbaka till källnoden, vilket gör det svårt att spåra en transaktion genom nätverket tillbaka till dess ursprung. Dandelion förbättrar därmed integriteten genom att begränsa motståndarnas möjlighet att avanonymisera nätverket. Denna metod är ännu mer effektiv när transaktionen under "stem"-fasen passerar en nod som krypterar sin nätverkskommunikation, t.ex. med Tor eller *P2P Transport V2*. BIP156 har ännu inte lagts till i Bitcoin Core.