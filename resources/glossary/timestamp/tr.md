---
term: HORODATAGE
---

Zaman damgası veya İngilizce'de "Timestamp", bir olay, veri veya mesaj ile kesin bir zaman işaretini ilişkilendirmek için kullanılan bir mekanizmadır. Bilgisayar sistemlerinin genel bağlamında zaman damgası, işlemlerin kronolojik sırasını belirlemek ve zaman içinde verilerin bütünlüğünü doğrulamak için kullanılır.


Bitcoin'ün özel durumunda, işlemlerin ve blokların kronolojisini oluşturmak için zaman damgaları kullanılır. Blockchain'deki her blok, oluşturulduğu yaklaşık zamanı gösteren bir Timestamp içerir. Satoshi Nakamoto, Beyaz Kitap'ında bugün "Blockchain" olarak adlandırdığımız şeyi tanımlamak için bir "Timestamp sunucusundan" bile bahsetmektedir. Bitcoin'teki zaman damgasının rolü, işlemlerin kronolojisini belirlemektir, böylece merkezi bir otoritenin müdahalesi olmadan hangi işlemin önce geldiği belirlenebilir. Bu mekanizma, her kullanıcının geçmişte bir işlemin var olmadığını doğrulamasını ve böylece kötü niyetli bir kullanıcının çifte harcama yapmasını önlemesini sağlar. Bu mekanizma Satoshi Nakamoto tarafından Beyaz Kitap'ta şu ünlü cümle ile gerekçelendirilmiştir:


> ► *Blok zaman damgaları Bitcoin'da nispeten esnektir, çünkü bir Timestamp'in geçerli sayılması için, kendisinden önceki 11 bloğun medyan zamanından (MTP) büyük ve düğümler tarafından döndürülen zamanların medyanından (ağa göre ayarlanmış zaman) artı 2 saatten küçük olması yeterlidir.*