---
term: Commitment Transaction
---

Lightning içindeki çift yönlü bir kanal bağlamında Commitment Transaction, her iki tarafın da ana zincirde yayınlamadan oluşturduğu ve imzaladığı bir işlemdir. Bir kanalın tarafları arasındaki fon dağıtımının mevcut durumunu temsil eder ve her Lightning ödemesi yeni bir Commitment Transaction ile sonuçlanır. Bu işlemler geçerlidir ancak yalnızca kanal tek taraflı olarak kapatıldığında yayınlanır. Her bir taraf için, kanalın açılmasından bu yana yapılan Lightning ödemelerine göre fon dağılımını yansıtan çıktılar içerirler. Ceza mekanizmaları, tarafları kanalın eski durumlarını, yani yanlış bir fon dağılımını yansıtan eski Commitment işlemlerini yayınlamaktan caydırmak için ilişkilendirilmiştir.