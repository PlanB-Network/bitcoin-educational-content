---
term: Miniscript
definition: Bitcoin betiklerinin (scripts) oluşturulmasını, analizini ve doğrulanmasını basitleştiren çerçeve.
---

Bitcoin üzerinde güvenli bir şekilde komut dosyaları programlamak için bir çerçeve sağlamak üzere tasarlanmış çerçeve. Bitcoin'ın yerel dili script olarak adlandırılır. Özellikle sofistike ve özelleştirilmiş uygulamalar için pratikte kullanımı oldukça karmaşıktır. Hepsinden önemlisi, bir betiğin sınırlamalarını doğrulamak çok zordur. Miniscript, oluşturulmalarını, analiz edilmelerini ve doğrulanmalarını basitleştirmek için Bitcoin betiklerinin bir alt kümesini kullanır. Her bir miniscript, yerel bir script ile 1'e 1 eşdeğerdir. Kullanıcı dostu bir politika dili kullanılır ve bu dil daha sonra miniscript'e derlenerek nihayetinde yerel bir komut dosyasına karşılık gelir.





Miniscript böylece geliştiricilerin daha güvenli ve güvenilir bir şekilde sofistike komut dosyaları oluşturmasına olanak tanır. Miniscript'in temel özellikleri aşağıdaki gibidir:


- İzin verdiği harcama koşulları ve kaynaklar açısından maliyeti de dahil olmak üzere komut dosyasının statik analizine olanak tanır;
- Uzlaşıya uygun senaryoların oluşturulmasını sağlar;
- Farklı harcama yollarının düğümlerin standart kurallarına uyup uymadığının analiz edilmesini sağlar;
- Tüm Wallet yazılım ve donanımları için anlaşılabilir ve birleştirilebilir genel bir standart oluşturur.


Miniscript projesi 2018 yılında Peter Wuille, Andrew Poelstra ve Sanket Kanjalkar tarafından Blockstream şirketi aracılığıyla başlatılmıştır. Miniscript, Bitcoin core Wallet'e Aralık 2022'de 24.0 sürümü ile yalnızca izleme modunda ve ardından Mayıs 2023'te 25.0 sürümü ile tamamen eklendi.