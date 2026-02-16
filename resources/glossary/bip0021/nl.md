---
term: BIP0021
definition: Standaard die het formaat van Bitcoin URI's definieert (links beginnend met bitcoin) om betalingen via links of QR-codes te vergemakkelijken.
---

Voorstel geschreven door Nils Schneider en Matt Corallo, gebaseerd op BIP20 geschreven door Luke Dashjr, dat op zijn beurt weer voortkwam uit een ander document geschreven door Nils Schneider. BIP21 definieert hoe ontvangstadressen gecodeerd moeten worden in URI's (*Uniform Resource Identifier*) om betalingen te vergemakkelijken. Bijvoorbeeld, een Bitcoin URI volgens BIP21 waarin ik onder het label "*Pandul*" zou vragen om mij 0,1 BTC te sturen, zou er als volgt uitzien:


```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```


Deze standaardisatie verbetert de gebruikerservaring van Bitcoin transacties door het mogelijk te maken op een link te klikken of een QR-code te scannen om hun parameters te starten. De BIP21 standaard wordt nu op grote schaal toegepast in Bitcoin Wallet software.