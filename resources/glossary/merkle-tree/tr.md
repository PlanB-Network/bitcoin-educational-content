---
term: Merkle Tree
---

Merkle Tree bir kriptografik akümülatördür. Belirli bir bilgi parçasının daha büyük bir küme içindeki üyeliğini kanıtlamak için kullanılan bir yöntemdir. Bilginin kompakt bir formatta doğrulanmasını kolaylaştıran bir veri yapısıdır. Bitcoin sisteminde Merkle Ağaçları, bir bloğun işlemlerini Merkle Root (veya "*Kök Hash*") adı verilen tek bir Hash'te gruplamak ve yoğunlaştırmak için kullanılır. Her işlem hash edilir, ardından bitişik hashler Merkle Root elde edilene kadar hiyerarşik olarak birlikte hash edilir.


![](../../dictionnaire/assets/1.webp)


Bu yapı, tüm işlemleri analiz etmek zorunda kalmadan belirli bir işlemin belirli bir bloğa dahil olup olmadığının hızlı bir şekilde doğrulanmasına olanak tanır. Örneğin, elimde yalnızca Merkle Root varsa ve `TX 7`nin gerçekten de ağacın bir parçası olduğunu doğrulamak istiyorsam, yalnızca aşağıdaki kanıtlara ihtiyacım olacaktır:


- tX 7';
- "Hash 8";
- "Hash 5-6";
- "Hash 1-2-3-4".

Bu bilgilerle Merkle Root'a kadar olan ara düğümleri hesaplayabiliyorum.


![](../../dictionnaire/assets/2.webp)


Merkle Ağaçları özellikle sadece blok başlıklarını tutan ancak işlemleri tutmayan hafif düğümler ("SPV" olarak bilinir) için kullanılır. Bu yapı, UTXO düğüm kümesinin yoğunlaştırılmasına olanak tanıyan bir protokol olan UTREEXO protokolünde ve MAST Taproot'da da bulunur.


> ► *Merkle Tree adını 1979 yılında bu yapıyı tasarlayan kriptograf Ralph Merkle'den almıştır. Bir Merkle Tree aynı zamanda "Hash ağacı" olarak da adlandırılabilir. Fransızca'da "Arbre de Merkle" veya "arbre de hachage" olarak adlandırılır.*