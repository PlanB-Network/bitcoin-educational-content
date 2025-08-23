---
term: VARSAYIM UTXO
---

Önde gelen Bitcoin core istemcisinde, yeni başlatılmış (ancak henüz IBD'den geçmemiş) bir düğümün işlemlerin ve UTXO setinin doğrulanmasını belirli bir anlık görüntüye kadar ertelemesine olanak tanıyan bir yapılandırma parametresi. Konsept, Çekirdek tarafından sağlanan ve doğru olduğu varsayılan bir UTXO setinin (belirli bir zamanda mevcut tüm UTXO'ların bir listesi) kullanımına dayanır, bu da düğümün en çok birikmiş işe sahip zincirle çok hızlı bir şekilde senkronize edilmesini sağlar. Düğüm uzun IBD adımını atladığından, kullanıcısı için çok hızlı bir şekilde çalışır hale gelir. UTXO'nin senkronizasyonu (IBD) iki kısma ayırdığını varsayalım:


- İlk olarak, düğüm Header First Sync (yalnızca başlıkların doğrulanması) gerçekleştirir ve Core tarafından sağlanan UTXO setini geçerli olarak kabul eder;
- Daha sonra, çalışmaya başladığında, düğüm arka planda tüm blok geçmişini doğrulayacak ve kendi doğruladığı yeni bir UTXO setini güncelleyecektir. Bu yeni UTXO seti Core tarafından sağlananla eşleşmezse, bir hata mesajı üretecektir.


Bu nedenle, UTXO'nın işlem doğrulama sürecini erteleyerek yeni bir Bitcoin düğümünün hazırlanmasını hızlandırdığını ve UTXO'nın Çekirdek'te sağlanan güncellenmiş bir anlık görüntü aracılığıyla ayarlandığını varsayalım.