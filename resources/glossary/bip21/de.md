---
term: BIP21

---
Vorschlag von Nils Schneider und Matt Corallo, basierend auf BIP20 von Luke Dashjr, das wiederum aus einem anderen Dokument von Nils Schneider stammt. BIP21 definiert, wie Empfangsadressen in URIs (*Uniform Resource Identifier*) kodiert werden sollten, um Zahlungen zu erleichtern. Ein Bitcoin-URI nach BIP21, in dem ich unter der Bezeichnung "*Pandul*" darum bitte, mir 0,1 BTC zu schicken, würde zum Beispiel so aussehen:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

Diese Standardisierung verbessert die Benutzerfreundlichkeit von Bitcoin-Transaktionen, indem sie es ermöglicht, auf einen Link zu klicken oder einen QR-Code zu scannen, um ihre Parameter zu initiieren. Der BIP21-Standard ist nun in der Bitcoin-Wallet-Software weit verbreitet.