---
term: SCRIPTSIG
---

Girdilerde bulunan bir Bitcoin işlemindeki bir öğe. ScriptSig`, fonların harcandığı önceki işlemin `scriptPubKey` tarafından belirlenen koşulları karşılamak için gerekli verileri sağlar. Bu nedenle `scriptPubKey` için tamamlayıcı bir rol oynar. Tipik olarak, `scriptSig` bir dijital imza ve bir açık anahtar içerir. İmza, bitcoinlerin sahibi tarafından kendi özel anahtarları kullanılarak oluşturulur ve UTXO'yi harcama yetkisine sahip olduklarını kanıtlar. Bu durumda, `scriptSig` girdinin sahibinin bir önceki giden işlemin `scriptPubKey`inde belirtilen Address ile ilişkili açık anahtara karşılık gelen özel anahtara sahip olduğunu gösterir.


İşlem doğrulandığında, `scriptSig`deki veriler ilgili `scriptPubKey`de yürütülür. Sonuç geçerliyse, fonların harcanması için gerekli koşulların karşılandığı anlamına gelir. İşlemin tüm girdileri kendi `scriptPubKey`lerini doğrulayan bir `scriptSig` sağlarsa, işlem geçerlidir ve yürütme için bir bloğa eklenebilir.


Örneğin, işte klasik bir P2PKH `scriptSig`:


```text
<signature> <public key>
```


Karşılık gelen `scriptPubKey` olacaktır:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


![](../../dictionnaire/assets/35.webp)


> ► * `scriptSig` bazen İngilizce'de "kilit açma betiği" olarak da adlandırılır