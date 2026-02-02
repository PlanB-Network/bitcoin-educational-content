---
term: Assume utxo
definition: Yeni bir düğümün arka planda geçmiş doğrulamadan önce geçerli kabul edilen UTXO setinin bir anlık görüntüsünü kullanarak hızlı bir şekilde senkronize edilmesine izin veren Bitcoin Core parametresi.
---
Bitcoin Core çoğunluk istemcisindeki bir yapılandırma parametresi, yeni başlatılan (ancak henüz IBD yapmamış) bir düğümün, belirli bir anlık görüntüden (snapshot) önceki işlemlerin ve UTXO setinin doğrulamasını ertelemesine olanak tanır. Konsept, Core tarafından sağlanan ve doğru olduğu varsayılan bir UTXO setinin (belirli bir zamanda var olan tüm UTXO'ların listesi) kullanılmasına dayanır ve bu da düğümün en çok birikmiş işe sahip zincirde çok hızlı bir şekilde senkronize olmasını sağlar. Düğüm uzun IBD adımını atladığı için kullanıcısı için çok hızlı bir şekilde işlevsel hale gelir.

Assume UTXO senkronizasyonu (IBD) iki parçaya böler: İlk olarak, düğüm Header First Sync (sadece üstbilgi doğrulaması) gerçekleştirir ve Core tarafından kendisine sağlanan UTXO setini geçerli kabul eder; Ardından, işlevsel hale geldiğinde, düğüm arka planda tam blok geçmişini doğrulayacak ve kendisinin doğruladığı yeni bir UTXO setini güncelleyecektir. Eğer bu sonuncu Core tarafından sağlanan UTXO seti ile eşleşmezse, bir hata mesajı verecektir.

Assume UTXO, Core'da sağlanan güncel bir anlık görüntü (snapshot) sayesinde işlemlerin ve UTXO setinin doğrulama sürecini erteleyerek yeni bir Bitcoin düğümünün hazırlığını hızlandırmaya olanak tanır.







