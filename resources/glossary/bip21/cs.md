---
term: BIP21

---
Návrh napsali Nils Schneider a Matt Corallo na základě dokumentu BIP20, který napsal Luke Dashjr a který zase vychází z jiného dokumentu napsaného Nilsem Schneiderem. BIP21 definuje, jak by měly být přijímací adresy kódovány v URI (*Uniform Resource Identifier*), aby se usnadnily platby. Například bitcoinový URI podle BIP21, ve kterém bych pod označením "*Pandul*" požádal o zaslání 0,1 BTC, by vypadal takto:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

Tato standardizace zlepšuje uživatelský zážitek z transakcí s bitcoiny tím, že umožňuje kliknout na odkaz nebo naskenovat QR kód a zahájit tak jejich parametry. Standard BIP21 je nyní široce přijat v softwaru bitcoinových peněženek.