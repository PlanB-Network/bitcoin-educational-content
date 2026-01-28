---
term: P2WPKH
definition: Bitcoinleri bir genel anahtarın hash'ine kilitleyen yerel SegWit betiği, bc1q adresleri.
---

P2WPKH *Pay to Witness Public Key Hash* anlamına gelir. Bir UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir senaryo modelidir. P2WPKH, Ağustos 2017'de SegWit'nin uygulanmasıyla birlikte tanıtılmıştır.


Bu betik P2PKH'ye (*Pay to Public Key Hash*) benzer, çünkü o da bir açık anahtarın Hash'ine, yani alıcı bir Address'e dayalı olarak bitcoinleri kilitler. Aradaki fark, imzaların ve komut dosyalarının işleme nasıl dahil edildiğinde yatmaktadır. P2WPKH durumunda, imza komut dosyası bilgileri (`scriptSig`) geleneksel işlem yapısından `Witness` adı verilen ayrı bir bölüme taşınır. Bu taşıma, SegWit (*Segregated Witness*) güncellemesinin bir özelliği olup imzanın değiştirilebilirliğini önlemeye yardımcı olur. P2WPKH işlemleri, şahit bölümünün maliyeti daha düşük olduğundan, Eski işlemlere kıyasla ücretler açısından genellikle daha ucuzdur.


P2WPKH adresleri, BCH kodu şeklinde bir sağlama toplamı ile `Bech32` kodlaması kullanılarak yazılır. Bu adresler her zaman `bc1q` ile başlar. P2WPKH bir sürüm 0 SegWit çıktısıdır.