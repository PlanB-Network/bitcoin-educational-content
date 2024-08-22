---
term: WITNESSSCRIPT
---

`witnessScript`は、P2WSHまたはP2SH-P2WSHのUTXOからビットコインを支出する条件を指定するスクリプトです。通常、`witnessScript`はSegWit標準の下でのマルチシグネチャウォレットの条件を決定します。これらのスクリプト標準では、UTXO（出力）の`scriptPubKey`には`witnessScript`のハッシュが含まれています。このUTXOを新しいトランザクションの入力として使用するためには、保持者は元の`witnessScript`を明らかにし、`scriptPubKey`の指紋との一致を証明する必要があります。その後、`witnessScript`はトランザクションの`scriptWitness`に含める必要があり、これにはスクリプトを検証するために必要な要素、例えば署名なども含まれます。したがって、`witnessScript`はP2SHトランザクションの`redeemScript`に相当しますが、違いはトランザクションの証人部分に配置され、`scriptSig`には配置されないという点です。

> ► *注意、`witnessScript`と`scriptWitness`を混同してはいけません。`witnessScript`はP2WSHまたはP2SH-P2WSH UTXOの支出条件を定義し、それ自体がスクリプトを構成しますが、`scriptWitness`には任意のSegWit入力の証人データが含まれます。*