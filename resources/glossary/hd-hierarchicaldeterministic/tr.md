---
term: HD (HIYERARŞIK-DETERMINISTIK)
---

Çok sayıda açık ve özel anahtar çiftini sıralı ve tekrarlanabilir bir şekilde generate yapmak için benzersiz bir bilgi parçası (seed) kullanan bir Bitcoin Wallet'ü ifade eder. Bu anahtar yönetme yöntemi BIP32 standardı tarafından tanımlanmıştır. HD cüzdanların ana avantajı, kullanıcıların çok sayıda farklı anahtar çiftine sahip olmalarına izin verirken, özellikle Address'in yeniden kullanılmasını önlemek ve hepsini tek bir bilgi parçasından yeniden üretebilmeleridir. Bu yapı hiyerarşik olarak tanımlanır çünkü tek bir seed'ten birden fazla anahtar ve adresin ağaç benzeri bir organizasyonunun oluşturulmasını sağlar. Ve her seed'ün bu sisteme uyan herhangi bir Wallet'te her zaman aynı anahtar dizisini üretmesi anlamında deterministiktir.