---
term: UTXO seti
definition: İşlemleri doğrulamak için her düğüm tarafından tutulan, belirli bir zamandaki tüm mevcut UTXO'ların kümesi.
---

Herhangi bir anda mevcut tüm UTXO'ların toplanmasını ifade eder. Başka bir deyişle, harcanmayı bekleyen tüm farklı bitcoin parçalarının büyük bir listesidir. UTXO setindeki tüm UTXO'ların miktarlarını toplarsanız, bu bize dolaşımdaki bitcoinlerin toplam parasal kütlesini verir. Bitcoin ağındaki her düğüm kendi UTXO setini gerçek zamanlı olarak tutar. Yeni geçerli bloklar onaylandıkça, UTXO setinden bazı UTXO'ları tüketen ve karşılığında yenilerini yaratan işlemlerle birlikte bunu günceller.


Bu UTXO seti, işlemlerde harcanan UTXO'ların gerçekten meşru olup olmadığını hızlı bir şekilde doğrulamak için her düğüm tarafından tutulur. Bu, Double-spending girişimlerini tespit etmelerini ve reddetmelerini sağlar. UTXO seti, boyutu doğal olarak çok hızlı arttığı için genellikle Bitcoin'nın merkeziyetsizliği ile ilgili endişelerin merkezinde yer alır. İşlemleri makul bir sürede doğrulamak için bir kısmının RAM'de tutulması gerektiğinden, UTXO seti bir Full node'in işletilmesini kademeli olarak çok maliyetli hale getirebilir. UTXO setinin IBD (*İlk Blok İndirme*) üzerinde de önemli bir etkisi vardır. RAM'e ne kadar çok UTXO seti yerleştirilebilirse, IBD o kadar hızlı olur. Bitcoin core'te UTXO seti `/chainstate' adlı klasörde saklanır.


