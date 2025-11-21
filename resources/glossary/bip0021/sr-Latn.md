---
term: BIP0021
---

Predlog napisali Nils Schneider i Matt Corallo, na osnovu BIP20 koji je napisao Luke Dashjr, a koji je, pak, proizašao iz drugog dokumenta koji je napisao Nils Schneider. BIP21 definiše kako bi adrese za primanje trebalo da budu kodirane u URI-jevima (*Uniform Resource Identifier*) radi olakšavanja plaćanja. Na primer, Bitcoin URI koji prati BIP21, u kojem bih tražio pod oznakom “*Pandul*” da mi se pošalje 0.1 BTC, izgledao bi ovako:


```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```


Ova standardizacija poboljšava korisničko iskustvo Bitcoin transakcija omogućavajući klik na link ili skeniranje QR koda za pokretanje njihovih parametara. BIP21 standard je sada široko prihvaćen u Bitcoin Wallet softveru.