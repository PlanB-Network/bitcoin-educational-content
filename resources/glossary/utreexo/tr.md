---
term: Utreexo
definition: Merkle ağaçlarına dayalı bir biriktirici aracılığıyla Bitcoin düğümlerinin UTXO setini sıkıştıran protokol.
---

Merkle ağaçlarına dayalı bir akümülatör kullanarak Bitcoin düğümlerinin UTXO kümesini sıkıştırmak için Tadge Dryja tarafından tasarlanan protokol. Önemli miktarda depolama alanı gerektiren klasik UTXO kümesinin aksine Utreexo, yalnızca Merkle Tree köklerini depolayarak ihtiyaç duyulan belleği büyük ölçüde azaltmaktadır. Bu, düğümün işlem girdilerinde kullanılan UTXO'ların varlığını, UTXO'ların tüm kümesini saklamak zorunda kalmadan doğrulamasına olanak tanır. Utreexo kullanarak, her düğüm yalnızca Merkle Root adı verilen bir kriptografik parmak izi tutar. Bir işlem yapıldığında, kullanıcı UTXO'ların Ownership kanıtlarını ve ilgili Merkle yollarını sağlar. Böylece düğüm, tüm UTXO setini saklamadan işlemleri doğrulayabilir. Bu mekanizmayı anlamak için bir diyagram ile örnek verelim:





Bu örnekte, anlamayı kolaylaştırmak için UTXO setini kasıtlı olarak 4 UTXO'ya indirgedim. Gerçekte, bu satırları yazarken Bitcoin üzerinde neredeyse 140 milyon UTXO olduğunu hayal etmek önemlidir. Bu diyagramda, Utreexo düğümünün yalnızca Merkle Root'i RAM'de tutması gerekecektir. Eğer UTXO No. 3'ü (siyah renkte) harcayan bir işlem alırsa, kanıt aşağıdaki Elements'dan oluşacaktır:


- UTXO 3;
- Hash 4;
- Hash 1-2.


İşlem göndericisi tarafından iletilen bu bilgilerle Utreexo düğümü aşağıdaki doğrulamaları gerçekleştirir:


- UTXO 3'ün izini hesaplar, bu da ona Hash 3'ü verir;
- Hash 3 ile Hash 4'ü birleştirir;
- İzlerini hesaplar, bu da ona Hash 3-4 verir;
- Hash 3-4 ile Hash 1-2'yi birleştirir;
- İzlerini hesaplar, bu da ona Merkle Root'yi verir.


Süreci aracılığıyla elde ettiği Merkle Root, RAM'inde depoladığı Merkle Root ile aynıysa, UTXO No. 3'ün gerçekten de UTXO setinin bir parçası olduğuna ikna olur.

Bu yöntem Full node operatörleri için RAM gereksinimlerini azaltır. Bununla birlikte, Utreexo'nun ek kanıtlar nedeniyle blok boyutunda artış ve Utreexo düğümlerinin eksik kanıtları elde etmek için Köprü Düğümlerine potansiyel bağımlılığı gibi sınırlamaları vardır. Köprü Düğümler, Utreexo düğümlerine gerekli kanıtları sağlayan ve böylece tam doğrulamaya izin veren geleneksel tam düğümlerdir. Bu yaklaşım, verimlilik ve ademi merkeziyetçilik arasında bir uzlaşma sunarak işlem doğrulamasını sınırlı kaynaklara sahip kullanıcılar için daha erişilebilir hale getirir.