---
term: SCRIPTSIG
---

Élément dans une transaction Bitcoin situé dans les inputs. Le `scriptSig` fournit les données nécessaires pour satisfaire les conditions posées par le `scriptPubKey` de la transaction précédente dont les fonds sont dépensés. Il joue donc un rôle complémentaire au `scriptPubKey`. Typiquement, le `scriptSig` contient une signature numérique et une clé publique. La signature est générée par le propriétaire des bitcoins à l'aide de sa clé privée et prouve qu'il a l'autorisation de dépenser l'UTXO. Dans ce cas, le `scriptSig` démontre que le détenteur de l'input possède la clé privée correspondant à la clé publique associée à l'adresse spécifiée dans le `scriptPubKey` de la transaction sortante précédente.

Lorsque la transaction est vérifiée, les données du `scriptSig` sont exécutées dans le `scriptPubKey` correspondant. Si le résultat est valide, cela signifie que les conditions de dépense des fonds ont été remplies. Si toutes les entrées de la transaction fournissent un `scriptSig` qui valide leur `scriptPubKey`, la transaction est valide et pourra être ajoutée à un bloc pour son exécution.

Par exemple, voici un `scriptSig` P2PKH classique :

```text
<signature> <clé publique>
```

Le `scriptPubKey` correspondant serait :

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <adresse> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *Le `scriptSig` est également parfois nommé « unlocking script » ou « script de déverrouillage » en français.*

