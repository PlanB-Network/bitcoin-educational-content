---
term: HMAC-SHA512
---

`HMAC-SHA512`, "Hash tabanlı Mesaj Kimlik Doğrulama Kodu - Güvenli Hash Algoritması 512" anlamına gelir. İki taraf arasında değiş tokuş edilen mesajların bütünlüğünü ve gerçekliğini doğrulamak için kullanılan bir kriptografik algoritmadır. Kriptografik Hash işlevi `SHA512` ile paylaşılan bir gizli anahtarı birleştirerek her mesaj için benzersiz bir Mesaj Kimlik Doğrulama Kodu (MAC) generate oluşturur.


Bitcoin bağlamında, `HMAC-SHA512`nin doğal kullanımı biraz türetilmiştir. Bu algoritma, bir Wallet'ün kriptografik anahtar ağacının deterministik ve hiyerarşik türetme sürecinde kullanılır. hMAC-SHA512` özellikle seed`ten ana anahtara gitmek için ve daha sonra bir üst çiftten alt çiftlere her türetme için kullanılır. Bu algoritma aynı zamanda kurtarma ifadesinden ve passphrase'den seed'e gitmek için kullanılan `PBKDF2` adlı başka bir türetme algoritmasında da bulunur.