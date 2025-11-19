---
term: XOR
---

"Exclusive or" işleminin kısaltması, Fransızca "Ou exclusif" Boole mantığının temel bir işlevidir. Bu işlem, her biri $doğru$ ya da $yanlış$ olan iki Boole işleneni alır ve yalnızca iki işlenen farklı olduğunda bir $doğru$ çıktı üretir. Başka bir deyişle, XOR işleminin çıktısı, işlenenlerden tam olarak biri (ancak ikisi birden değil) $true$ ise $true$ olur. Örneğin, $1$ ve $0$ arasındaki XOR işlemi $1$ sonucunu verecektir. Not ediyoruz:


$$
1 \oplus 0 = 1
$$


Benzer şekilde, XOR işlemi daha uzun bit dizileri üzerinde gerçekleştirilebilir. Örneğin:


$$
10110 \oplus 01110 = 11000
$$


Dizideki her bir bit kendi muadiliyle karşılaştırılır ve XOR işlemi uygulanır. İşte XOR işlemi için doğruluk tablosu:


<div align="center">


| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>


XOR işlemi, bilgisayar bilimlerinin birçok alanında, özellikle de kriptografide, aşağıdaki gibi ilginç özelliklerinden dolayı kullanılır:


- Değişmezliği: İşlenenlerin sırası sonucu etkilemez. Verilen iki değişken $D$ ve $E$ için: $D \oplus E = E \oplus D$;
- İlişkiselliği: işlenenlerin gruplanması sonucu etkilemez. Verilen üç değişken $A$, $B$ ve $C$ için: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Nötr bir elemanı $0$ vardır: $0$ ile xored edilmiş bir operand her zaman operanda eşit olacaktır. Verilen bir $A$ değişkeni için: $A \oplus 0 = A$;
- Her eleman kendi tersidir. Verilen bir $A$ değişkeni için: $A \oplus A = 0$.


Bitcoin bağlamında, XOR işlemi açıkça birçok yerde kullanılmaktadır. Örneğin, XOR, Bitcoin protokolünde yaygın olarak kullanılan SHA256 işlevinde büyük ölçüde kullanılır. Coldcard'ın *SeedXOR* gibi bazı protokoller de bu ilkeli diğer uygulamalar için kullanır. Ayrıca BIP47'de yeniden kullanılabilir ödeme kodunu iletimi sırasında şifrelemek için bulunur.

Daha geniş bir kriptografi alanında, XOR simetrik bir şifreleme algoritması olarak kullanılabilir. Bu algoritmaya "One-Time Pad" ya da mucidinin adıyla anılan "Vernam Cipher" adı verilir. Anahtarın uzunluğu nedeniyle pratik olmamasına rağmen, bu algoritma koşulsuz olarak güvenli kabul edilen tek şifreleme algoritmalarından biridir.