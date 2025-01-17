---
term: SCRIPTSIG

---
Bitcoini tehingu element, mis asub sisendites. `scriptSig` annab vajalikud andmed, et täita eelmise tehingu `scriptPubKey` poolt seatud tingimusi, millest raha kulutatakse. Seega täidab see täiendavat rolli võrreldes `scriptPubKey`ga. Tavaliselt sisaldab `scriptSig` digitaalallkirja ja avalikku võtit. Allkirja genereerib bitcoinide omanik oma isikliku võtme abil ja see tõestab, et tal on luba UTXO kulutamiseks. Sellisel juhul näitab `scriptSig`, et sisendi omanikul on eelmise väljamineva tehingu `scriptPubKey`-s määratud aadressiga seotud avalikule võtmele vastav eravõti.

Kui tehing on kontrollitud, täidetakse `scriptSig`i andmed vastavas `scriptPubKey`s. Kui tulemus on kehtiv, tähendab see, et raha kulutamise tingimused on täidetud. Kui kõik tehingu sisendid annavad `scriptSig`, mis valideerib nende `scriptPubKey`, on tehing kehtiv ja selle võib plokki täitmiseks lisada.

Näiteks siin on klassikaline P2PKH `scriptSig`:

```text
<signature> <public key>
```

Vastav `scriptPubKey` oleks:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *ScriptSig`i nimetatakse inglise keeles mõnikord ka "unlocking script"