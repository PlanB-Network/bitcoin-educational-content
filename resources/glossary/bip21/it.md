---
term: BIP21

---
Proposta scritta da Nils Schneider e Matt Corallo, basata sul BIP20 scritto da Luke Dashjr, che a sua volta deriva da un altro documento scritto da Nils Schneider. BIP21 definisce come gli indirizzi di ricezione debbano essere codificati negli URI (*Uniform Resource Identifier*) per facilitare i pagamenti. Ad esempio, un URI Bitcoin conforme a BIP21 in cui richiedo all'etichetta "*Pandul*" di inviarmi 0,1 BTC avrebbe il seguente aspetto:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

Questa standardizzazione migliora l'esperienza dell'utente nelle transazioni Bitcoin, consentendo di cliccare su un link o scansionare un codice QR per avviare i parametri. Lo standard BIP21 è ora ampiamente adottato nel software dei portafogli Bitcoin.