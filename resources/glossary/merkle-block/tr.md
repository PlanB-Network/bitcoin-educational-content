---
term: Merkle bloğu
definition: Hafif istemciler için bir işlemin bloğa dahil edildiğine dair kompakt bir kanıt sağlayan yapı.
---

BIP37 (*Transaction Bloom Filtering*) bağlamında bir bloğa belirli işlemlerin dahil edildiğine dair kompakt bir kanıt sağlamak için kullanılan bir veri yapısı. Özellikle SPV cüzdanları için kullanılır. Merkle Bloğu, blok başlıklarını, filtrelenmiş işlemleri ve kısmi bir Merkle Tree'ı içerir ve hafif istemcilerin tüm işlemleri indirmeden bir işlemin bir bloğa ait olup olmadığını hızlı bir şekilde doğrulamasına olanak tanır.