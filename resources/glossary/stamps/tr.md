---
term: STAMPS
---

Biçimlendirilmiş görüntü verilerinin ham çoklu imza işlemleri (P2MS) yoluyla doğrudan Bitcoin Blockchain'a entegre edilmesini sağlayan bir protokol. Stamps bir görüntünün ikili içeriğini 64 tabanında kodlar ve bunu 1/3 P2MS'nin anahtarlarına ekler. Anahtarlardan biri gerçektir ve fonları harcamak için kullanılır, diğer ikisi ise verileri saklayan sahte anahtarlardır (ilişkili özel anahtar bilinmemektedir). Verileri `OP_RETURN` çıktılarını kullanmak yerine doğrudan açık anahtarlar olarak kodlayarak, Stamps protokolü ile depolanan görüntüler düğümler için özellikle iş yükü yoğundur. Bu yöntem özellikle birden fazla UTXO oluşturur, bu da UTXO setinin boyutunu artırır ve tam düğümler için sorun teşkil eder.