---
term: STANDARDIZASYON KURALLARI
---

Standartlaştırma kuralları, mutabakat kurallarına ek olarak, Mempool'e kabul ettiği ve eşlerine yayınladığı onaylanmamış işlemlerin yapısını tanımlamak için her Bitcoin düğümü tarafından ayrı ayrı benimsenir. Dolayısıyla bu kurallar her düğüm tarafından yerel olarak yapılandırılır ve yürütülür ve bir düğümden diğerine değişebilir. Sadece onaylanmamış işlemler için geçerlidirler. Bu nedenle, bir düğüm standart dışı olduğunu düşündüğü bir işlemi yalnızca geçerli bir bloğa dahil edilmişse kabul edecektir.


Düğümlerin çoğunun Bitcoin core'de belirlenen varsayılan konfigürasyonları terk ettiği ve böylece ağ genelinde standartlaştırma kurallarının tekdüzeliğini oluşturduğu belirtilmektedir. Mutabakat kurallarına uygun olmasına rağmen bu standardizasyon kurallarına uymayan bir işlem, ağ genelinde yayınlanmakta zorluk çekecektir. Ancak, bir Miner'e ulaşırsa yine de geçerli bir bloğa dahil edilebilir. Uygulamada, "standart dışı" olarak adlandırılan bu işlemler genellikle Bitcoin eşler arası ağın dışındaki harici yollarla doğrudan bir Miner'e iletilir. Bu genellikle bu tür bir işlemi onaylamanın tek yoludur.


Örneğin, hiçbir ücret tahsis etmeyen bir işlem hem mutabakat kurallarına göre geçerlidir hem de standart değildir çünkü `minRelayTxFee` parametresi için Bitcoin core'in varsayılan politikası `0.00001`dir (BTC/kB cinsinden).


> ► *"Mempool kuralları" terimi bazen standardizasyon kurallarını ifade etmek için de kullanılır