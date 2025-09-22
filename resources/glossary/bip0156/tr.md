---
term: BIP0156
---

Dandelion olarak bilinen öneri, anonimleştirmeye karşı koymak için Bitcoin ağındaki işlem yönlendirmesinin gizliliğini artırmayı amaçlamaktadır. Bitcoin'ın standart işleyişinde işlemler anında birden fazla düğüme yayınlanır. Bir gözlemci ağdaki her bir düğüm tarafından aktarılan her bir işlemi görebiliyorsa, bir işlemi gönderen ilk düğümün aynı zamanda bu işlemin kaynak düğümü olduğunu ve dolayısıyla düğümün operatöründen geldiğini varsayabilir. Bu olgu, gözlemcilerin normalde anonim olan işlemleri IP adresleriyle ilişkilendirmesine olanak sağlayabilir.


BIP156'nın amacı bu sorunu Address'e taşımaktır. Bunu yapmak için, genel yayılımdan önce anonimliği korumak için yayına ek bir aşama getirmektedir. Böylece Dandelion, "fluff" aşamasında tüm ağa yayınlanmadan önce işlemin rastgele bir düğüm yolu üzerinden gönderildiği bir "stem" aşaması kullanır. Kök ve kabarıklık, işlemin ağ boyunca yayılma davranışına atıfta bulunur ve bir karahindiba (İngilizce'de *a dandelion*) şeklini andırır.


Bu yönlendirme yöntemi, kaynak düğüme geri giden izi gizleyerek bir işlemin ağ üzerinden kaynağına kadar izlenmesini zorlaştırır. Dandelion böylece düşmanların ağı anonimleştirme kabiliyetini sınırlandırarak gizliliği artırır. Bu yöntem, işlem "kök" aşamasında Tor veya *P2P Transport V2* gibi ağ iletişimlerini şifreleyen bir düğümden geçtiğinde daha da etkilidir. BIP156 henüz Bitcoin core'ye eklenmemiştir.