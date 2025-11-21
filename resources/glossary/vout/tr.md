---
term: VOUT
---

Gönderilen fonların hedefini belirleyen bir Bitcoin işleminin belirli bir unsuru. Bir işlem, her biri işlem tanımlayıcısı (`txid`) ve `vout` adı verilen bir indeksin kombinasyonu ile benzersiz bir şekilde tanımlanan birden fazla çıktı içerebilir. 0`dan başlayan bu indeks, çıktının işlem çıktıları dizisindeki konumunu işaret eder. Böylece, ilk çıktı `"vout" ile belirtilecektir: 0`, ikincisi `"vout": 1` ve bu şekilde devam eder.


Her `vout` öncelikle iki bilgi parçasını kapsar:


- gönderilen miktarı temsil eden bitcoin cinsinden ifade edilen değer;
- fonların gelecekteki bir işlemde tekrar harcanabilmesi için gereken koşulları belirleyen bir kilitleme komut dosyası (`scriptPubKey`).


Örneğin, `txid` ve belirli bir parçanın `vout` kombinasyonu UTXO olarak adlandırılan şeyi oluşturur:


```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```