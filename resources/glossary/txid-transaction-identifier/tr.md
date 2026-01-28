---
term: Txid (işlem tanımlayıcı)
definition: Verilerinin SHA256d karması (hash) ile hesaplanan, bir Bitcoin işleminin benzersiz tanımlayıcısı.
---

Her bir Bitcoin işlemi ile ilişkili benzersiz bir tanımlayıcı. İşlem verilerinin `SHA256d` Hash'ü hesaplanarak oluşturulur. txid, Blockchain içinde belirli bir işlemi bulmak için bir referans görevi görür. Ayrıca, esasen önceki bir işlemin txid'sının ve belirlenen çıktının ("vout" olarak da adlandırılır) indeksinin birleştirilmesi olan bir UTXO'e atıfta bulunmak için de kullanılır. SegWit sonrası işlemler için, txid artık işlem tanığını dikkate almaz, bu da değiştirilebilirliği ortadan kaldırır.