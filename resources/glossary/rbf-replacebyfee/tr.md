---
term: RBF (Replace-by-fee)
---

Göndericinin onaylanmasını hızlandırmak için daha yüksek ücretler ödeyerek bir işlemi diğeriyle değiştirmesine olanak tanıyan bir işlem mekanizması. Çok düşük ücretli bir işlem takılırsa, gönderici ücretleri artırmak ve mempool'larda yedek işlemlerine öncelik vermek için *Replace-by-fee* kullanabilir.


RBF, işlem mempool'larda olduğu sürece geçerlidir; bir bloğa girdikten sonra artık değiştirilemez. İlk gönderimde, işlem `nSequence` değerini `0xfffffffe` değerinden daha küçük bir sayıya ayarlayarak değiştirilebilirliğini belirtmelidir. Bu bir RBF "bayrağı" olarak bilinir. Bu ayar, işlemin yayınlandıktan sonra güncellenme olasılığına işaret eder ve bu da daha sonra bir RBF'e izin verir. Ancak, bazen RBF sinyali vermemiş bir işlemi değiştirmek mümkündür. Yapılandırma parametresi `mempoolfullrbf=1` kullanan düğümler, başlangıçta RBF sinyali verilmemiş olsa bile bu değiştirmeyi kabul eder.


Alıcının işlemi hızlandırmak için harekete geçebildiği CPFP'in (*Çocuk Ebeveyn İçin Öder*) aksine, RBF (*Replace-by-fee*) gönderenin ücretleri artırarak kendi işlemini hızlandırmak için inisiyatif almasına izin verir.