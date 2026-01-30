---
term: Cüzdan içe aktarma formatı (WIF)
definition: Cüzdanlar arasında içe veya dışa aktarılmasını kolaylaştırmak için bir Bitcoin özel anahtarının Base58Check kodlama yöntemi.
---

Bir Bitcoin özel anahtarını farklı cüzdanlar arasında daha kolay içe veya dışa aktarılabilecek şekilde kodlamak için bir yöntem. WIF, sürüm hakkında bilgi, ilgili açık anahtarın sıkıştırılması ve yazımda hata tespiti için bir sağlama toplamı içeren `Base58Check` kodlamasına dayanmaktadır. Bir WIF özel anahtarı, sıkıştırılmamış anahtarlar için `5` veya sıkıştırılmış anahtarlar için `K` ve `L` karakterleriyle başlar ve orijinal özel anahtarı yeniden oluşturmak için gerekli tüm karakterleri içerir. WIF formatı, farklı Wallet yazılımları arasında özel bir anahtarın aktarılması için standartlaştırılmış bir araç sağlar.