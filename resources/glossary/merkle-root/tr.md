---
term: Merkle Root
---

Ağaçta bulunan tüm bilgilerin bir özetini temsil eden bir Merkle Tree'nin özeti veya "üst Hash". Bir Merkle Tree kriptografik bir akümülatör yapısıdır ve bazen "Hash ağacı" olarak da adlandırılır. Bitcoin bağlamında, Merkle ağaçları bir blok içindeki işlemleri düzenlemek ve belirli bir işlemin dahil edildiğinin hızlı bir şekilde doğrulanmasını kolaylaştırmak için kullanılır. Böylece, Bitcoin bloklarında Merkle Root, yalnızca bir Hash kalana kadar (Merkle Root) işlemlerin çiftler halinde art arda hash edilmesiyle elde edilir. Bu daha sonra ilgili bloğun başlığına dahil edilir. Bu Hash ağacı, UTXO düğüm kümesinin yoğunlaştırılmasına olanak tanıyan bir yapı olan UTREEXO'da ve MAST Taproot'te de bulunur.