---
term: BIP0049
---

BIP49, bir HD Wallet'te generate İç içe SegWit adresleri için kullanılan türetme yöntemini tanıtan bilgilendirici bir BIP'dir. Önerilen türetme yolu, hedefin derinliğinde `49'` (sertleştirilmiş türetme) indeksi ile BIP43 ve BIP44 standartlarını takip eder. Örneğin, bir P2SH-P2WPKH hesabının ilk Address'i şu yoldan türetilecektir: `m/49'/0'/0'/0/0`. İç içe geçmiş SegWit komut dosyaları, SegWit'ün benimsenmesini kolaylaştırmak için SegWit'ün lansmanında icat edilmiştir. Henüz SegWit ile yerel olarak uyumlu olmayan cüzdanlarda bile bu yeni standardın kullanılmasına izin verirler.