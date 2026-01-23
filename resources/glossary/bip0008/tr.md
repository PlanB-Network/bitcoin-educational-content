---
term: BIP0008
definition: Madencilerin ayrılan süre içinde desteklerini belirtmemeleri durumunda otomatik bir UASF mekanizmasını entegre eden soft fork etkinleştirme yöntemi.
---

Etkinleştirilmesi için BIP9 kullanılan SegWit üzerindeki tartışmaların ardından geliştirilen BIP8, otomatik bir UASF (*Kullanıcı Tarafından Etkinleştirilen Soft Fork*) mekanizmasını doğal olarak içeren bir Soft Fork etkinleştirme yöntemidir. BIP9 gibi BIP8 de Miner sinyalizasyonunu kullanır ancak `LOT` (*Lock-in On Time out*) parametresini ekler. Eğer `LOT` `true` olarak ayarlanırsa, sinyalleşme süresinin gerekli eşiğe ulaşmadan sona ermesi üzerine, bir UASF otomatik olarak tetiklenir ve Soft Fork'ın etkinleştirilmesini zorlar. Bu yaklaşım madencileri işbirliğine zorlar ya da kullanıcılar tarafından UASF uygulanması riskini doğurur. Ayrıca, BIP9'dan farklı olarak, BIP8 sinyalizasyon süresini blok yüksekliğine göre tanımlayarak madenciler tarafından Hash oranı yoluyla olası manipülasyonları ortadan kaldırır. BIP8 ayrıca değişken bir oylama eşiği belirlemeye olanak tanır ve aktivasyon için minimum blok yüksekliği için bir parametre getirerek madencilere hazır olmaları gerekmeden önceden hazırlanmaları ve anlaşmalarını bildirmeleri için zaman tanır. Bir Soft Fork, `LOT=true` parametresi ile BIP8 aracılığıyla etkinleştirildiğinde, bu, hemen potansiyel bir UASF baskısı altına giren madencilere karşı çok agresif bir yöntem kullanır. Gerçekten de onlara sadece 2 seçenek bırakır:


- İşbirlikçi olun ve böylece aktivasyon sürecini kolaylaştırın;
- İşbirliği yapmazsa, bu durumda kullanıcılar Soft Fork'ü uygulamak için otomatik olarak bir UASF gerçekleştirir.