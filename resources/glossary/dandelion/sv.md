---
term: Dandelion
definition: Integritetsprotokoll som döljer transaktionernas ursprung via en fas av spridning i stjälk och sedan i fluff.
---

Ett förslag som syftar till att förbättra integriteten för transaktionsrouting i Bitcoin-nätverket för att motverka avanonymisering. I standarddriften av Bitcoin sänds transaktioner omedelbart till flera noder. Detta fenomen kan potentiellt göra det möjligt för observatörer att länka transaktioner, som normalt är anonyma, med IP-adresser. Målet med BIP156 är att Address ska lösa detta problem. För att göra detta införs ytterligare en fas i sändningsprocessen för att bevara anonymiteten innan den sprids till allmänheten. Således använder Dandelion först en "stem"-fas där transaktionen skickas genom en slumpmässig väg av noder, innan den sänds till hela nätverket i "fluff"-fasen. Stjälken och fluffet är referenser till beteendet hos transaktionens spridning genom nätverket och liknar formen hos en maskros. Den här routningsmetoden döljer spåret som leder tillbaka till källnoden, vilket gör det svårt att spåra en transaktion genom nätverket tillbaka till dess ursprung.


