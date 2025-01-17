---
term: BIP21

---
Proposal written by Nils Schneider and Matt Corallo, based on BIP20 written by Luke Dashjr, which in turn came from another document written by Nils Schneider. BIP21 defines how receiving addresses should be encoded in URIs (*Uniform Resource Identifier*) to facilitate payments. For example, a Bitcoin URI following BIP21 in which I would request under the label “*Pandul*” to send me 0.1 BTC would look like this:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

This standardization improves the user experience of Bitcoin transactions by allowing to click on a link or scan a QR code to initiate their parameters. The BIP21 standard is now widely adopted in Bitcoin wallet software.