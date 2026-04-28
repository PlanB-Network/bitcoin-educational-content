---
term: Index (sleutel)
definition: Opeenvolgend nummer toegewezen aan een kind-sleutel om deze te onderscheiden van zijn broers en zussen in een HD-wallet.
---

Verwijst in de context van een HD-portfolio naar het volgnummer dat is toegewezen aan een kindsleutel die is gegenereerd uit een oudersleutel. Deze index wordt gebruikt in combinatie met de oudersleutel en de ouderstringcode om op deterministische wijze unieke kindsleutels af te leiden. Het maakt een gestructureerde organisatie en reproduceerbare generatie van meerdere paren zusterkindsleutels uit een enkele oudersleutel mogelijk. Het is een geheel getal van 32 bits dat wordt gebruikt in de `HMAC-SHA512` afleidingsfunctie. Dit getal kan worden gebruikt om kindsleutels binnen een HD-portfolio te onderscheiden.