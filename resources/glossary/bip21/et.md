---
term: BIP21

---
Nils Schneideri ja Matt Corallo koostatud ettepanek, mis põhineb Luke Dashjr'i kirjutatud BIP20-l, mis omakorda tuleneb Nils Schneideri kirjutatud teisest dokumendist. BIP21 määratleb, kuidas vastuvõtuaadressid tuleks maksete hõlbustamiseks kodeerida URI-desse (*Uniform Resource Identifier*). Näiteks BIP21 järgne Bitcoini URI, milles ma paluksin sildi "*Pandul*" all saata mulle 0,1 BTC, näeks välja järgmiselt:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

See standardimine parandab Bitcoini tehingute kasutajakogemust, võimaldades oma parameetrite algatamiseks klõpsata lingil või skaneerida QR-koodi. BIP21 standard on nüüdseks laialdaselt vastu võetud Bitcoini rahakoti tarkvaras.