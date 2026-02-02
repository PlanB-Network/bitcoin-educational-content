---
term: P2WSH
definition: Bitcoinleri bir betiğin hash'ine kilitleyen yerel SegWit betiği, bc1q adresleri.
---

P2WSH *Pay to Witness Script Hash* anlamına gelmektedir. Bir UTXO üzerinde harcama koşulları oluşturmak için kullanılan standart bir senaryo modelidir. P2WSH, Ağustos 2017'de SegWit'ın uygulanmasıyla birlikte tanıtılmıştır.


Bu betik P2SH'e (*Pay to Public Script Hash*) benzer, çünkü o da bir betiğin Hash'üne dayalı olarak bitcoinleri kilitler. Aradaki fark, imzaların ve komut dosyalarının işleme nasıl dahil edildiğinde yatmaktadır. Bitcoinleri bu tür bir komut dosyasına harcamak için, alıcının gerekli imzalarla birlikte `witnessScript` (`redeemscript`e eşdeğer) adı verilen orijinal komut dosyasını sağlaması gerekir. Bu mekanizma, multisig gibi daha karmaşık harcama koşullarının uygulanmasına olanak tanır.


P2WSH bağlamında, imza komut dosyası bilgileri (`scriptSig`e eşdeğer olan `scriptWitness`) geleneksel işlem yapısından `Witness` adlı ayrı bir bölüme taşınır. Bu taşıma, imzanın değiştirilebilirliğini önlemeye yardımcı olan SegWit (*Segregated Witness*) güncellemesinin bir özelliğidir. P2WSH işlemleri, şahit bölümünün maliyeti daha düşük olduğundan, Eski işlemlere kıyasla ücretler açısından genellikle daha ucuzdur.


P2WSH adresleri, BCH kodu şeklinde bir sağlama toplamı ile `Bech32` kodlaması kullanılarak yazılır. Bu adresler her zaman `bc1q` ile başlar. P2WSH bir sürüm 0 SegWit çıktısıdır.