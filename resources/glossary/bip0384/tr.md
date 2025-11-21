---
term: BIP0384
---

Tanımlayıcılar için `combo(KEY)` işlevini tanıtır. Bu fonksiyon, belirli bir açık anahtar için bir dizi olası çıktı komut dosyasını tanımlar. Böylece P2PK, P2PKH, P2WPKH ve P2SH-P2WPKH dahil olmak üzere aynı anda birden fazla komut dosyası türünü kapsar. Verilen anahtar sıkıştırılmışsa, 4 komut dosyası türünün tümü test edilir ve sıkıştırılmamışsa, yalnızca 2 Eski komut dosyası türü test edilir. Amaç, aynı genel anahtara dayalı generate farklı çıktı komut dosyası varyantları için tek bir yöntem sağlayarak tanımlayıcılardaki anahtarların gösterimini basitleştirmektir. BIP384, Descriptor ile ilgili diğer tüm BIP'lerle birlikte (BIP386 hariç) Bitcoin core'ın 0.17 sürümünde uygulanmıştır.