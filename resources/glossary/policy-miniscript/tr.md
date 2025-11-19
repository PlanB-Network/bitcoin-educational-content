---
term: POLİTİKA (MİNİ YAZI)
---

Miniscript çerçevesinde bir UTXO'in kilidinin açılabileceği koşulların basit bir şekilde belirtilmesine olanak tanıyan yüksek seviyeli, kullanıcı odaklı bir dil. Politika, harcama kurallarının soyut bir tanımıdır. Daha sonra Bitcoin'ın yerel komut dosyası dilindeki işlemlerle bire bir eşdeğer olan miniscript'e derlenebilir.


![](../../dictionnaire/assets/30.webp)


Politika dili mini kod dilinden biraz farklıdır. Örneğin, birincil yolu A anahtarı ve kurtarma yolu B anahtarı olan, ancak bir yıllık (yaklaşık 52.560 blok) bir zaman kilidi altında olan bir güvenlik sistemi düşünün. Politikada bu şöyle olacaktır:


```plaintext
or(pk(A),and(pk(B),older(52560)))
```


Miniscript olarak derlendiğinde, öyle olacaktır:


```plaintext
andor(pk(B),older(52560),pk(A))
```


Ve bir kez yerel yazıya dönüştürüldüğünde, öyle olacaktır:


```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```