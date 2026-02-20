---
term: Konsolidasyon
definition: Gelecekteki ücretleri azaltmak için birkaç küçük UTXO'yu tek bir büyük UTXO'da birleştiren işlem.
---

Birden fazla küçük UTXO'nun çıktı olarak tek ve daha büyük bir UTXO oluşturmak üzere tek bir girdide birleştirildiği özel bir işlem. Bu işlem kişinin kendi Wallet'ine yapılan bir işlemdir. Konsolidasyonun amacı, Bitcoin ağındaki ücretlerin düşük olduğu dönemlerden yararlanarak birkaç küçük UTXO'yu değer olarak daha büyük bir UTXO'da birleştirmektir. Böylece, ücret artışları durumunda zorunlu harcamaları öngörerek gelecekteki işlem ücretlerinden tasarruf edilmesini sağlar.


Gerçekten de çok sayıda girdisi olan işlemler daha ağır ve dolayısıyla daha pahalıdır. İşlem ücretlerinde elde edilebilecek tasarrufun ötesinde, konsolidasyon aynı zamanda bir tür uzun vadeli planlamadır. Wallet'iniz çok küçük UTXO'lar içeriyorsa, Bitcoin ağı uzun süreli yüksek ücret dönemine girerse bunlar kullanılamaz hale gelebilir. Örneğin, 10.000 Sats'lik bir UTXO harcamanız gerekiyorsa, ancak minimum Mining ücretleri 15.000 Sats ise, masraf UTXO'in değerini aşacaktır. Bu küçük UTXO'ların kullanımı ekonomik açıdan mantıksız hale gelir ve ücretler düşmediği sürece kullanılamaz durumda kalır. Bu UTXO'lar genellikle "Dust" olarak adlandırılır Küçük UTXO'larınızı düzenli olarak konsolide ederek, ücret artışlarıyla ilişkili bu riski azaltırsınız.


Ancak, konsolidasyon işlemlerinin bir zincir analizi sırasında fark edilebileceğini unutmamak önemlidir. Böyle bir işlem Ortak Girdi Ownership Sezgiselini (CIOH) gösterir, yani konsolidasyon işleminin girdilerinin tek bir varlığa ait olduğu anlamına gelir. Bu, kullanıcı için gizlilik açısından sonuçlar doğurabilir.


