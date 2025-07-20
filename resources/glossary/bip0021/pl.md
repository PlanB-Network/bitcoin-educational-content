---
term: BIP0021
---

Propozycja napisana przez Nilsa Schneidera i Matta Corallo, oparta na BIP20 napisanym przez Luke'a Dashjra, który z kolei pochodzi z innego dokumentu napisanego przez Nilsa Schneidera. BIP21 definiuje sposób kodowania adresów odbiorczych w URI (*Uniform Resource Identifier*) w celu ułatwienia płatności. Na przykład URI Bitcoin zgodny z BIP21, w którym prosiłbym pod etykietą "*Pandul*" o przesłanie mi 0,1 BTC, wyglądałby następująco:


```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```


Standaryzacja ta poprawia komfort użytkowania transakcji Bitcoin, umożliwiając kliknięcie łącza lub zeskanowanie kodu QR w celu zainicjowania ich parametrów. Standard BIP21 jest obecnie powszechnie stosowany w oprogramowaniu Bitcoin Wallet.