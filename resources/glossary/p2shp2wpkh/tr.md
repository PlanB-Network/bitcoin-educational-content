---
term: P2SH-P2WPKH
---

P2SH-P2WPKH, *Pay to Script Hash - Pay to Witness Public Key Hash* anlamına gelmektedir. "İç İçe SegWit" olarak da bilinen UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir senaryo modelidir.


P2SH-P2WPKH, Ağustos 2017'de SegWit'un uygulanmasıyla birlikte tanıtılmıştır. Bu komut dosyası bir P2WPKH'in içine sarılmış bir P2SH'dir. Bir açık anahtarın Hash'una dayalı olarak bitcoinleri kilitler. Klasik P2WPKH'den farkı, betiğin klasik bir P2SH'in `redeemscript'sine sarılmış olmasıdır.


Bu komut dosyası, SegWit'ün benimsenmesini kolaylaştırmak için SegWit'ün lansmanında oluşturulmuştur. Henüz SegWit ile yerel olarak uyumlu olmayan hizmetler veya cüzdanlarla bile bu yeni standardın kullanılmasına izin verir. Bu, yeni standarda doğru bir tür geçiş betiğidir. Günümüzde, çoğu cüzdan yerel SegWit'ü uyguladığından, bu tür sarılmış SegWit komut dosyalarını kullanmak artık çok önemli değildir. P2SH-P2WPKH adresleri `Base58Check` kodlaması kullanılarak yazılır ve herhangi bir P2SH Address gibi her zaman `3` ile başlar.


> ► *`P2SH-P2WPKH` bazen `P2WPKH-nested-in-P2SH` olarak da adlandırılır.*