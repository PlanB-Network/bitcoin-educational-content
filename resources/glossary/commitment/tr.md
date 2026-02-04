---
term: Commitment
definition: Verileri ifşa etmeden varlığını kanıtlamaya olanak tanıyan kriptografik nesne.
---

Bir Commitment (kriptografik anlamda), $C$ ile gösterilen, yapılandırılmış veri $m$ (mesaj) ve rastgele bir değer $r$ üzerindeki bir işlemden deterministik olarak türetilen matematiksel bir nesnedir. Yazıyoruz :


$$
C = \text{commit}(m, r)
$$


Bu mekanizma iki ana işlemden oluşmaktadır:




- Taahhüt: $C$ üretmek için bir mesaja $m$ ve rastgele bir $r$ kriptografik fonksiyon uygularız;
- Verify: Bu Commitment'nin doğru olup olmadığını kontrol etmek için $C$, $m$ mesajı ve $r$ değerini kullanırız. Fonksiyon `True` veya `False` döndürür.


Bir Commitment iki özelliğe saygı göstermelidir:




- Bağlama: Aynı $C$ değerini üreten iki farklı mesaj bulmak imkansız olmalıdır:


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Mesela :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Gizleme: $C$ bilgisinin $m$ içeriğini açığa çıkarmaması gerekir.


RGB protokolü söz konusu olduğunda, bilginin kendisini ifşa etmeden belirli bir zamanda belirli bir bilginin varlığını kanıtlamak için bir Bitcoin işlemine bir Commitment dahil edilir.