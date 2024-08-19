---
term: BIP21
---

Vorschlag verfasst von Nils Schneider und Matt Corallo, basierend auf BIP20 von Luke Dashjr, welcher wiederum auf einem anderen Dokument von Nils Schneider basierte. BIP21 definiert, wie Empfangsadressen in URIs (*Uniform Resource Identifier*) kodiert werden sollten, um Zahlungen zu erleichtern. Zum Beispiel würde ein Bitcoin-URI gemäß BIP21, in dem ich unter dem Label „*Pandul*“ darum bitte, mir 0.1 BTC zu senden, so aussehen:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

Diese Standardisierung verbessert die Benutzererfahrung bei Bitcoin-Transaktionen, indem sie es ermöglicht, auf einen Link zu klicken oder einen QR-Code zu scannen, um deren Parameter zu initiieren. Der BIP21-Standard wird mittlerweile weitgehend in Bitcoin-Wallet-Software übernommen.