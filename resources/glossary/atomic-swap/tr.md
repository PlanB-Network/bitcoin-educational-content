---
term: Atomic swap
definition: Güvenilir bir aracı olmaksızın iki taraf arasında kripto para birimlerinin değiştirilmesi, burada değişim tamamen başarılı olur ya da tamamen iptal edilir.
---

Güvene ihtiyaç duymadan ve bir aracı gerektirmeden iki taraf arasında kripto para birimlerinin doğrudan Exchange'ına izin veren teknoloji. Bu değiş tokuşlar "atomik" olarak adlandırılır çünkü yalnızca iki sonuçla sonuçlanabilirler:


- Ya Exchange başarılı olur ve her iki katılımcı da kripto paralarını etkin bir şekilde takas etmiş olur;
- Ya da Exchange başarısız olur ve her iki katılımcı da orijinal kripto paralarıyla ayrılır.


Atomik Takaslar aynı kripto para birimi ile gerçekleştirilebilir, bu durumda "*coinswap*" olarak da adlandırılır veya farklı kripto para birimleri arasında gerçekleştirilebilir. Tarihsel olarak, Exchange'ün tamamlanmasını veya tamamen iptal edilmesini garanti eden ve böylece ilgili tarafların fonlarının bütünlüğünü koruyan bir zaman kilitleme sistemi olan "Hash Zaman Kilitli Sözleşmelere" (HTLC) dayanıyorlardı. Bu yöntem hem senaryoları hem de zaman kilitlerini işleyebilen protokoller gerektiriyordu. Ancak son yıllarda eğilim *Adaptor Signatures* kullanımına doğru kaymıştır. Bu ikinci yaklaşım, komut dosyası ihtiyacını ortadan kaldırma ve böylece operasyonel maliyetleri azaltma avantajına sahiptir. Diğer önemli avantajı ise işlemin her iki kısmı için de aynı hashing'in kullanılmasını gerektirmemesidir, bu da aralarındaki bağlantının ortaya çıkmasını önlemeye yardımcı olur.