---
term: BIP0021
---

Proposal written by Nils Schneider and Matt Corallo, based on BIP20 written by Luke Dashjr, which itself was derived from another document written by Nils Schneider. 
BIP21 defines how receiving addresses should be encoded in URIs (*Uniform Resource Identifier*) to facilitate payments. For example, a Bitcoin URI following BIP21 that requests 0.1 BTC under the label "Pandul" would look like this:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

This standardization improves the user experience of Bitcoin transactions by enabling payments to be initiated by simply clicking a link or scanning a QR code. Today, the BIP21 standard is widely adopted in Bitcoin wallet software.