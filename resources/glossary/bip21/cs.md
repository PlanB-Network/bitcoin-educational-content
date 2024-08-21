---
term: BIP21
---

Návrh napsaný Nilsem Schneiderem a Mattem Corallo, založený na BIP20 od Luke Dashjra, který zase vycházel z jiného dokumentu napsaného Nilsem Schneiderem. BIP21 definuje, jak by měly být přijímací adresy zakódovány v URI (*Uniform Resource Identifier*) pro usnadnění plateb. Například Bitcoin URI podle BIP21, ve kterém bych požádal pod štítkem “*Pandul*” o zaslání 0.1 BTC, by vypadalo takto:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

Tato standardizace zlepšuje uživatelskou zkušenost s Bitcoin transakcemi tím, že umožňuje kliknout na odkaz nebo naskenovat QR kód pro iniciaci jejich parametrů. Standard BIP21 je nyní široce přijímán v softwaru Bitcoin peněženek.