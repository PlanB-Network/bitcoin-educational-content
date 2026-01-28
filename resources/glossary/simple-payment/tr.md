---
term: Basit ödeme
definition: Genellikle bir ödeme ve bir para üstü olmak üzere 2 çıktılı işlem modeli.
---

Zincir analizinde kullanılan işlem modeli (veya modeli), girdilerde bir veya daha fazla UTXO tüketimi ve çıktılarda 2 UTXO üretimi ile karakterize edilir. Dolayısıyla bu model şu şekilde görünecektir:





Bu basit ödeme modeli, muhtemelen bir gönderme veya ödeme işleminin varlığına işaret etmektedir. Kullanıcı, çıktılarda bir ödeme UTXO'ı ve bir değişiklik UTXO'ı (aynı kullanıcıya iade edilen değişiklik) karşılamak için girdilerde kendi UTXO'ını tüketmiştir. Bu nedenle, gözlemlenen kullanıcının muhtemelen artık çıktılardaki iki UTXO'dan birine (ödeme olan) sahip olmadığını, ancak diğer UTXO'a (değişiklik olan) hala sahip olduğunu biliyoruz.