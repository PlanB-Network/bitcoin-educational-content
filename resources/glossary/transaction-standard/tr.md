---
term: Standart işlem
definition: Hem konsensüs kurallarına hem de Bitcoin Core düğümlerinin varsayılan standartlaştırma kurallarına uyan işlem.
---

Mutabakat kurallarına uymanın yanı sıra Bitcoin core düğümlerinde varsayılan olarak belirlenen standartlaştırma kurallarına da uyan bir Bitcoin işlemi. Bu standardizasyon kuralları, mutabakat kurallarına ek olarak, Mempool'de kabul ettiği ve eşlerine yayınladığı onaylanmamış işlemlerin yapısını tanımlamak için her Bitcoin düğümü tarafından ayrı ayrı uygulanır.


Dolayısıyla bu kurallar her düğüm tarafından yerel olarak yapılandırılır ve yürütülür ve bir düğümden diğerine değişebilir. Bunlar yalnızca onaylanmamış işlemler için geçerlidir. Bu nedenle, bir düğüm standart dışı olduğunu düşündüğü bir işlemi yalnızca geçerli bir bloğa zaten dahil edilmişse kabul edecektir.


Düğümlerin çoğunun Bitcoin core'te belirlenen varsayılan konfigürasyonları terk ettiği ve böylece ağ genelinde standartlaştırma kurallarının tekdüzeliğini oluşturduğu belirtilmektedir. Mutabakat kurallarına uygun olmasına rağmen bu standardizasyon kurallarına uymayan bir işlem ağ boyunca yayılmakta zorluk çekecektir. Ancak, bir Miner'e ulaşırsa yine de geçerli bir bloğa dahil edilebilir. Uygulamada, standart dışı olarak nitelendirilen bu işlemler genellikle Bitcoin eşler arası ağa harici yollarla doğrudan bir Miner'e iletilir. Bu genellikle böyle bir işlemi onaylamanın tek yoludur. Örneğin, hiçbir ücret tahsis etmeyen bir işlem hem mutabakat kurallarına göre geçerlidir hem de standart değildir, çünkü `minRelayTxFee` parametresi için Bitcoin core'ün varsayılan politikası `0.00001`dir (BTC/kB cinsinden).