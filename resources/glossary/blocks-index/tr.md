---
term: Blok indeksi
definition: Bitcoin Core'da blokların meta verilerini ve konumlarını kataloglayan LevelDB yapısı.
---

Bitcoin core'da tüm bloklar hakkında meta verileri kataloglayan bir LevelDB veri yapısı. Bu dizindeki her girdi bloğun tanımlayıcısı, Blockchain'deki yüksekliği, veritabanındaki bloğun işaretçisi ve diğer meta veriler gibi ayrıntıları sağlar. Bu indeksleme, bellekte saklanan bir bloğun hızlı bir şekilde geri alınmasını sağlar.