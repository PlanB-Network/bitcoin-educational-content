---
term: Bloom filtresi
definition: Küme üyeliğinin hızlı bir şekilde test edilmesine olanak tanıyan olasılıksal veri yapısı; SPV cüzdanlarında kullanılır.
---

Bir öğenin bir kümenin parçası olup olmadığını test etmek için kullanılan olasılıksal bir veri yapısı. Bloom Filtreleri, tüm veri kümesini test etmeden hızlı üyelik kontrollerine izin verir. Özellikle alan ve hızın kritik olduğu, ancak düşük ve kontrollü bir hata oranının kabul edilebilir olduğu bağlamlarda kullanışlıdırlar. Aslında, Bloom Filtreleri yanlış negatifler üretmez, ancak belirli bir miktarda yanlış pozitif üretirler. Filtreye bir eleman eklendiğinde, birden fazla Hash fonksiyonu bir bit dizisinde generate pozisyonu alır. Üyeliği kontrol etmek için aynı Hash fonksiyonları kullanılır. İlgili tüm bitler ayarlanmışsa, eleman muhtemelen kümededir, ancak yanlış pozitif riski vardır. Bloom Filtreleri veritabanları ve ağlar alanlarında yaygın olarak kullanılmaktadır. Google'ın bunları sıkıştırılmış veritabanı yönetim sistemi *BigTable* için kullandığı özellikle bilinmektedir. Bitcoin protokolünde, özellikle BIP37'ye göre SPV cüzdanları için kullanılırlar.


> ► *Özellikle Bitcoin işlemleri bağlamında Bloom Filtrelerinin kullanımından bahsederken, bazen "İşlem Bloom Filtreleme" terimiyle karşılaşılır.*