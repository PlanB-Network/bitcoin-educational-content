---
term: Kilit (.lock)
definition: Birden fazla Bitcoin Core örneğinin aynı dizine aynı anda erişmesini engelleyen dosya.
---

Bitcoin core'da veri dizinini kilitlemek için kullanılan dosya. bitcoind veya Bitcoin-qt başladığında, yazılımın birden fazla örneğinin aynı veri dizinine aynı anda erişmesini önlemek için oluşturulur. Amaç, çakışmaları ve veri bozulmasını önlemektir. Yazılım beklenmedik bir şekilde durursa, .lock dosyası kalabilir ve Bitcoin core yeniden başlatılmadan önce manuel olarak silinmelidir.