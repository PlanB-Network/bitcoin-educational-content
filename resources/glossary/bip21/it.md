Proposta scritta da Nils Schneider e Matt Corallo, basata su BIP20 scritto da Luke Dashjr, che a sua volta proviene da un altro documento scritto da Nils Schneider. BIP21 definisce come gli indirizzi di ricezione dovrebbero essere codificati negli URI (*Uniform Resource Identifier*) per facilitare i pagamenti. Ad esempio, un URI Bitcoin seguendo BIP21 in cui richiederei sotto l'etichetta “*Pandul*” di inviarmi 0.1 BTC sarebbe così:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

Questa standardizzazione migliora l'esperienza utente delle transazioni Bitcoin consentendo di cliccare su un link o di scansionare un codice QR per iniziare i loro parametri. Lo standard BIP21 è ora ampiamente adottato nel software di portafoglio Bitcoin.