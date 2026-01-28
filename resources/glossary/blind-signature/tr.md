---
term: Kör imza
definition: İmzalayanın imzalanan içeriği bilmediği dijital imza; Chaumian CoinJoins ve ecash'te kullanılır.
---

Chaum'un kör imzaları, imzayı atan kişinin imzaladığı mesajın içeriğini bilmediği bir dijital imza biçimidir. Ancak imza daha sonra orijinal mesaj ile doğrulanabilir. Bu teknik kriptograf David Chaum tarafından 1983 yılında geliştirilmiştir.


Contract gibi gizli bir belgeyi içeriğini açıklamadan doğrulamak isteyen bir şirket örneğini ele alalım. Şirket orijinal belgeyi kriptografik olarak tersine çevrilebilir bir şekilde dönüştüren bir maskeleme işlemi uygular. Bu değiştirilmiş belge, temel içeriği bilmeden kör imza uygulayan bir sertifika yetkilisine gönderilir. Maskelenmiş imzalı belgeyi aldıktan sonra şirket imzanın maskesini kaldırır. Sonuç, yetkilinin orijinal içeriği hiç görmeden, yetkilinin imzasıyla doğrulanmış orijinal bir belgedir.


Böylece Chaum'un kör imzaları, bir belgenin içeriğini bilmeden gerçekliğinin onaylanmasına olanak tanıyarak hem kullanıcının verilerinin gizliliğini hem de imzalanan belgenin bütünlüğünü sağlar.


Bitcoin'de, bu protokol Chaumian bankalarının sistemlerinde bir kaplama olarak (Cashu, Fedimint, vb.), ancak özellikle Chaumian CoinJoin protokollerinde, koordinatörün bir girdiyi bir çıktıya bağlayamamasını sağlamak için kullanılır.