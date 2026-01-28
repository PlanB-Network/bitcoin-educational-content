---
term: Covenant
definition: Bir bitcoinin gelecekteki işlemlerde nasıl harcanabileceğine dair koşullar getiren mekanizma.
---

Gelecekteki işlemler de dahil olmak üzere, belirli bir para biriminin nasıl harcanabileceğine ilişkin belirli koşulların uygulanmasına izin veren bir mekanizma. Bir UTXO üzerinde komut dosyası dili tarafından genellikle izin verilen koşulların ötesinde, sözleşme, bu Bitcoin'ın sonraki işlemlerde nasıl harcanabileceğine ilişkin ek kısıtlamalar getirir. Teknik olarak, bir UTXO'in `scriptPubKey'i, söz konusu UTXO'i harcayan bir işlemin çıktılarının `scriptPubKey'i üzerinde kısıtlamalar tanımladığında bir sözleşmenin kurulması gerçekleşir. Senaryonun kapsamını genişleterek, sözleşmeler Bitcoin üzerinde drivechain'lerin iki taraflı olarak sabitlenmesi, kasaların uygulanması veya Lightning gibi kaplama sistemlerinin iyileştirilmesi gibi çok sayıda gelişmeyi mümkün kılacaktır. Sözleşme teklifleri üç kritere göre farklılaştırılmaktadır:


- Onların kapsamı;
- Bunların uygulanması;
- Tekrarlanabilirlikleri.


Bitcoin üzerinde sözleşmelerin kullanılmasına izin verecek birçok öneri bulunmaktadır. Uygulama sürecinde en gelişmiş olanları şunlardır: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) ve `OP_VAULT`. Diğer teklifler arasında şunlar vardır: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, vb.


Sözleşme kavramını daha iyi anlamak için şu benzetmeyi düşünün: içinde küçük banknotlar halinde 500 € bulunan bir kasa hayal edin. Doğru anahtarla bu kasanın kilidini açmayı başarırsanız, bu parayı istediğiniz gibi kullanmakta özgürsünüz. Bitcoin ile ilgili normal durum budur. Şimdi, aynı kasada 500 Avro'luk banknotlar değil, eşdeğer değerde yemek kuponları olduğunu düşünün. Bu kasayı açmayı başarırsanız, bu tutarı kullanabilirsiniz. Ancak, bu kuponları yalnızca belirli restoranlarda ödeme yapmak için kullanabileceğiniz için harcama özgürlüğünüz kısıtlanır. Dolayısıyla, bu parayı harcamanın ilk koşulu, uygun anahtarla kasayı açmayı başarmaktır. Ancak bu meblağın gelecekteki kullanımına ilişkin ek bir koşul daha vardır: bu meblağ sadece ortak restoranlarda harcanmalıdır, serbestçe değil. Gelecekteki işlemlerle ilgili bu kısıtlamalar sistemine sözleşme denir.


