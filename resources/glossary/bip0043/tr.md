---
term: BIP0043
---

Daha önce BIP32'de tanıtılan HD cüzdanlarının yapısındaki amaç alanını tanımlamak için bir türetme yolu seviyesinin kullanılmasını sağlayan iyileştirme önerisi. BIP43'e göre, bir HD Wallet'in ilk türetme seviyesi, `m/` olarak gösterilen ana anahtardan hemen sonra, yolun geri kalanı için kullanılan türetme standardını gösteren amaç numarası için ayrılmıştır. Bu numara sertleştirilmiş bir indeks olarak kaydedilir. Örneğin, Wallet SegWit standardını (BIP84) takip ediyorsa, türetme yolunun başlangıcı şöyle olacaktır: `m/84'/`. Böylece BIP43, her bir Wallet yazılımı tarafından benimsenen standartların netleştirilmesine ve aralarında daha iyi birlikte çalışabilirlik sağlanmasına olanak tanır. Türetme yolunun geri kalanının standartlaştırılması BIP44'te açıklanmaktadır.