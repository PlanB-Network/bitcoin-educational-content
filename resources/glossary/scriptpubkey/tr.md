---
term: Scriptpubkey
definition: Bir işlemin çıktısında yer alan ve bir UTXO'nun harcanma koşullarını belirleyen script.
---

Bir Bitcoin işleminin çıktı kısmında bulunan ve ilişkili UTXO'nin hangi koşullar altında harcanabileceğini tanımlayan bir komut dosyası. Bu komut dosyası böylece bitcoinleri güvence altına alır. En yaygın haliyle, `scriptPubKey` bir sonraki işlemin belirtilen Bitcoin Address'a karşılık gelen özel anahtara sahip olduğunu kanıtlamasını gerektiren bir koşul içerir. Bu genellikle, bu fonları güvence altına almak için kullanılan Address ile ilişkili açık anahtara karşılık gelen bir imza talep eden bir komut dosyası ile elde edilir. Bir işlem bu UTXO'yi girdi olarak kullanmaya çalıştığında, `scriptPubKey` ile birleştirildiğinde belirlenen koşulları karşılayan ve geçerli bir komut dosyası üreten bir `scriptSig` sağlamalıdır.


Örneğin, işte klasik bir P2PKH `scriptPubKey`:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


Karşılık gelen `scriptSig` olacaktır:


```text
<signature> <public key>
```





> ► *Bu komut dosyası bazen İngilizce'de "kilitleme komut dosyası" olarak da adlandırılır.*