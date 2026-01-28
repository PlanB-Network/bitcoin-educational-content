---
term: Extra-nonce
definition: Coinbase içinde, madencilik için arama alanının klasik nonce değerinin ötesine genişletilmesine olanak tanıyan alan.
---

Doğrudan her bloğun başlığında bulunan klasik Nonce'ye ek olarak, zorluk hedefinden daha düşük bir Hash'e sahip olmak için daha fazla sayıda olasılığın test edilmesine olanak tanıyan bir bloğun Coinbase Transaction'inin `scriptSig'inde kullanılan alan.


Coinbase Transaction'teki ekstra Nonce'nin değiştirilmesi bu işlemin tanımlayıcısını ve dolayısıyla bloktaki tüm işlemlerin Merkle Root'ini değiştirir ve bu da blok başlığını değiştirir. Bu, Miner'nın klasik Nonce'nin aralığı zaten tükendiğinde, aday bloğunun yapısını değiştirmeden hash aramaya devam etmesini sağlar.


Mining havuzlarında, ekstra Nonce genellikle iki parçaya bölünür: biri her bir kıyıcıyı tanımlamak için havuz tarafından oluşturulur ve diğeri geçerli bir paylaşım ararken kıyıcı tarafından değiştirilir. Bu, havuzdaki farklı kıyıcıların aynı işi havuz düzeyinde tekrarlamadan, tüm nonces aralığıyla aynı aday blok üzerinde eşzamanlı olarak çalışmasına olanak tanır.