---
term: BIP21
---

Ettepaneku kirjutasid Nils Schneider ja Matt Corallo, põhinedes BIP20-l, mille autoriks oli Luke Dashjr, mis omakorda pärines teisest Nils Schneideri kirjutatud dokumendist. BIP21 määratleb, kuidas vastuvõtvaid aadresse tuleks kodeerida URI-des (*Uniform Resource Identifier*), et hõlbustada makseid. Näiteks Bitcoin URI, mis järgib BIP21 standardit ja milles ma paluksin sildi “*Pandul*” all saata mulle 0.1 BTC, näeks välja selline:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

See standardiseerimine parandab Bitcoin'i tehingute kasutajakogemust, võimaldades klõpsata lingil või skaneerida QR-koodi, et algatada nende parameetrid. BIP21 standard on nüüd laialdaselt kasutusele võetud Bitcoin'i rahakottide tarkvaras.