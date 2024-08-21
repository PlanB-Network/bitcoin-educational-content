---
term: SCRIPTSIG
---

Bitcoin'i tehingus sisalduv element, mis asub sisendites. `scriptSig` pakub vajalikke andmeid eelmisest tehingust, millest vahendeid kulutatakse, seatud `scriptPubKey` tingimuste rahuldamiseks. Seega mängib see täiendavat rolli `scriptPubKey` suhtes. Tavaliselt sisaldab `scriptSig` digitaalset allkirja ja avalikku võtit. Allkiri genereeritakse bitcoine omava isiku poolt nende privaatvõtmega ja tõestab, et neil on õigus UTXO kulutada. Sel juhul näitab `scriptSig`, et sisendi hoidja omab avaliku võtmele vastavat privaatvõtit, mis on määratud eelmise väljamineva tehingu `scriptPubKey`s.

Kui tehing on kontrollitud, käivitatakse `scriptSig` andmed vastavas `scriptPubKey`s. Kui tulemus on kehtiv, tähendab see, et vahendite kulutamise tingimused on täidetud. Kui kõik tehingu sisendid pakuvad `scriptSig`i, mis valideerib nende `scriptPubKey`, on tehing kehtiv ja seda saab lisada plokki täitmiseks.

Näiteks siin on klassikaline P2PKH `scriptSig`:

```text
<allkiri> <avalik võti>
```

Vastav `scriptPubKey` oleks:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <aadress> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *`scriptSig`i nimetatakse inglise keeles mõnikord ka "lukust avavaks skriptiks".*