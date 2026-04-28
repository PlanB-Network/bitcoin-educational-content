---
term: MTP (median time past)
definition: Ağ için zaman referansı görevi gören, son 11 bloğun zaman damgalarının medyanı.
---

Bu kavram Bitcoin protokolünde ağın mutabakatı Timestamp üzerinde bir marj belirlemek için kullanılır. MTP, çıkarılan son 11 bloğun zaman damgalarının medyanı olarak tanımlanır. Bu göstergenin kullanımı, uyuşmazlık durumunda düğümler arasında tam zaman konusunda anlaşmazlıkların önlenmesine yardımcı olur. MTP başlangıçta blok zaman damgalarının geçmişe karşı geçerliliğini doğrulamak için kullanılmıştır. BIP113'ten bu yana, zaman kilidi işlemlerinin geçerliliğini doğrulamak için ağ zamanı için bir referans olarak da kullanılmaktadır (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` ve `OP_CHECKSEQUENCEVERIFY`).