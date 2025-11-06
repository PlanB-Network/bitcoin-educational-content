---
term: TWEAK
---

Kriptografide, bir açık anahtarı "değiştirmek", "ince ayar" adı verilen bir ek değer kullanarak değiştirmektir, böylece hem orijinal özel anahtar hem de ince ayar bilgisi ile kullanılabilir kalır. Teknik olarak ince ayar, orijinal açık anahtara eklenen skaler bir değerdir. Eğer $P$ açık anahtar ve $t$ ince ayar ise, ince ayarlanmış açık anahtar :


$$
P' = P + tG
$$


Burada $G$ kullanılan eliptik eğrinin üretecidir. Bu işlem, kullanılmasına izin veren belirli kriptografik özellikleri korurken orijinalinden türetilmiş yeni bir açık anahtar üretir. Örneğin, bu yöntem Taproot (P2TR) adresleri için, geleneksel şekilde bir Schnorr imzası sunarak ya da "MAST" olarak da bilinen bir Merkle Tree'da belirtilen koşullardan birini yerine getirerek harcamayı sağlamak için kullanılır.