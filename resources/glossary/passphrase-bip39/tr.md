---
term: passphrase (BIP39)
---

Kurtarma ifadesiyle birleştirildiğinde, deterministik ve hiyerarşik Bitcoin cüzdanları için ek bir Layer güvenlik sağlayan isteğe bağlı bir parola. HD cüzdanları tipik olarak 12 veya 24 kelimeden oluşan bir kurtarma ifadesinden oluşturulur. Bu kurtarma cümlesi, kayıp durumunda bir Wallet'teki tüm anahtarların geri yüklenmesine izin verdiği için çok önemlidir. Bununla birlikte, tek bir hata noktası (SPOF) oluşturur. Eğer tehlikeye girerse, bitcoinler risk altına girer. passphrase burada devreye girer. Bu, Wallet'ün güvenliğini artırmak için kurtarma ifadesine eklenen, kullanıcı tarafından seçilen isteğe bağlı bir paroladır. PIN kodu ya da sıradan bir parola ile karıştırılmaması gereken passphrase, kriptografik anahtarların türetilmesinde rol oynar.


Kurtarma ifadesiyle birlikte çalışarak anahtarların üretildiği seed'i değiştirir. Böylece, birisi kurtarma cümlenizi ele geçirse bile, passphrase olmadan fonlarınıza erişemez. Bir passphrase kullanımı esasen farklı anahtarlara sahip yeni bir Wallet yaratır. passphrase'in (çok az da olsa) değiştirilmesi generate'yı farklı bir Wallet haline getirecektir.


passphrase isteğe bağlıdır ve kullanıcı tarafından seçilen herhangi bir karakter kombinasyonu olabilir. passphrase kullanımı çeşitli avantajlar sunar. İlk olarak, fonlara erişmek için ikinci bir faktör gerektirerek kurtarma ifadesinin tehlikeye atılmasıyla ilişkili riskleri azaltır. Daha sonra, fonlarınızı çalmak için fiziksel zorlama durumunda, küçük miktarlarda bitcoin içeren sahte cüzdanlar oluşturmak için stratejik olarak kullanılabilir. Son olarak, HD Wallet seed üretiminin rastgeleliğini kontrol etmek istendiğinde kullanımı ilginçtir. passphrase, kaba kuvvet saldırılarına direnmek için yeterince karmaşık olmalı ve güvenilir bir şekilde kaydedilmelidir. passphrase'un kaybedilmesi, tıpkı kurtarma ifadesinin kaybedilmesi gibi fonlara erişilememesine yol açabilir.


> ► *passphrase bazen şu şekilde de adlandırılır: "iki faktörlü seed ifadesi," "şifre," "seed uzantısı," "uzantı kelimesi," hatta "13. veya 25. kelime" Bitcoin'te iki tür parola olduğunu belirtmek gerekir. En iyi bilineni yukarıda açıklanan, BIP-39'a bağlı olan ve tüm bir HD Wallet'ün güvenliğini sağlayan şifredir. Bununla birlikte, BIP-38 ayrıca bir passphrase ile benzersiz bir özel anahtarı güvence altına almanın bir yolunu da belirtmiştir. Bu ikinci tip passphrase günümüzde artık neredeyse hiç kullanılmamaktadır.*