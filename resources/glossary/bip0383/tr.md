---
term: BIP0383
---

Tanımlayıcılar için `multi(NUM, KEY, ..., KEY)` ve `sortedmulti(NUM, KEY, ..., KEY)` fonksiyonlarını tanıtır. Bu fonksiyonlar, tanımlayıcılarda çoklu imza komut dosyalarının tanımlanmasına izin verir ve `sortedmulti`, içe aktarma sırasında uyumluluğu sağlamak için açık anahtarları leksikografik sıraya göre sıralar. BIP383, Descriptor ile ilgili diğer tüm BIP'lerle birlikte (BIP386 hariç) Bitcoin core'ın 0.17 sürümünde uygulanmıştır.