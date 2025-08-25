---
term: P2SH-P2WSH
---

P2SH-P2WSH, *Pay to Script Hash - Tanığa Ödeme Senaryosu Hash* anlamına gelmektedir. "Yuvalanmış SegWit" olarak da bilinen UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir senaryo modelidir.


P2SH-P2WSH, Ağustos 2017'de SegWit'nın uygulanmasıyla birlikte tanıtılmıştır. Bu komut dosyası, bir P2SH içine sarılmış bir P2WSH'yi açıklar. Bir betiğin Hash'sine dayalı olarak bitcoinleri kilitler. Klasik bir P2WSH'den farkı, betiğin klasik bir P2SH'in `redeemscript`ine sarılmış olmasıdır.


Bu komut dosyası, SegWit'un benimsenmesini kolaylaştırmak için SegWit'un lansmanında oluşturulmuştur. Henüz SegWit ile yerel olarak uyumlu olmayan hizmetler veya cüzdanlarla bile bu yeni standardın kullanılmasına olanak tanır. Günümüzde, çoğu cüzdan yerel SegWit'u uyguladığından, bu tür sarılmış SegWit komut dosyalarını kullanmak artık çok önemli değildir. P2SH-P2WSH adresleri `Base58Check` kodlaması kullanılarak yazılır ve her P2SH Address gibi her zaman `3` ile başlar.