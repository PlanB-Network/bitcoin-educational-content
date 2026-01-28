---
term: Scriptpubkey
definition: Script in de output van een transactie die de bestedingsvoorwaarden van een UTXO definieert.
---

Een script in het uitvoergedeelte van een Bitcoin transactie dat de voorwaarden definieert waaronder de bijbehorende UTXO kan worden uitgegeven. Dit script beveiligt dus bitcoins. In zijn meest voorkomende vorm bevat het `scriptPubKey` een voorwaarde die vereist dat de volgende transactie bewijs levert van het bezit van de private sleutel die correspondeert met een gespecificeerde Bitcoin Address. Dit wordt vaak bereikt door een script dat een handtekening eist die correspondeert met de private sleutel. Dit wordt vaak bereikt door een script dat vraagt om een handtekening die overeenkomt met de publieke sleutel die hoort bij de Address die wordt gebruikt om deze fondsen te beveiligen. Wanneer een transactie probeert deze UTXO als invoer te gebruiken, moet het een `scriptSig` leveren dat, eenmaal gecombineerd met de `scriptPubKey`, voldoet aan de gestelde voorwaarden en een geldig script produceert.


Hier is bijvoorbeeld een klassieke P2PKH `scriptPubKey`:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


Het bijbehorende `scriptSig` zou zijn:


```text
<signature> <public key>
```





> ► *Dit schrift wordt in het Engels ook wel "locking script" genoemd.*