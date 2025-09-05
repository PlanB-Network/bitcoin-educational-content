---
term: ZORLUK AYARI
---

Zorluk ayarlaması, Bitcoin'deki Proof of Work mekanizması (Mining) için zorluk hedefini yeniden tanımlayan periyodik bir süreçtir. Bu olay her 2016 blokta bir (yaklaşık iki haftada bir) gerçekleşir. Son 2016 bloklarının ne kadar hızlı bulunduğuna bağlı olarak zorluk faktörünü (zorluk hedefi olarak da adlandırılır) artırmaya veya azaltmaya yarar. Ayarlama, madenciler tarafından kullanılan hesaplama gücündeki değişikliklere rağmen, her 10 dakikada bir blok sıklığında istikrarlı ve öngörülebilir bir blok üretim oranını korumayı amaçlamaktadır. Ayarlama sırasında zorluk derecesindeki değişiklik 4 faktörle sınırlıdır. Yeni hedefi hesaplamak için düğümler tarafından yürütülen formül aşağıdaki gibidir:

$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$


Nerede?


- $N$: Yeni hedef;
- $A$: Son 2016 bloğunun eski hedefi;
- $T$: Son 2016 bloğun saniye cinsinden toplam gerçek süresi;
- $1,209,600$: Her biri arasında 10 dakikalık bir aralık olan 2016 blok üretmek için saniye cinsinden hedef süre.


> ► *Fransızcada "reciblage" terimi bazen ayarlama anlamında da kullanılmaktadır. İngilizcede ise "Zorluk Ayarlaması" olarak ifade edilmektedir.*