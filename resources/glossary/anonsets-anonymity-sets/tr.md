---
term: ANONSETS (ANONIMLIK KÜMELERI)
---

Anonsetler, belirli bir UTXO'in gizlilik seviyesini değerlendirmek için gösterge görevi görür. Daha spesifik olarak, incelenen Coin'ı içeren küme içindeki ayırt edilemeyen UTXO'ların sayısını ölçerler. Bir grup aynı UTXO gerekli olduğundan, anonsetler genellikle bir eş birleştirme döngüsü içinde hesaplanır. Uygun olduğunda, eş birleşimlerin kalitesinin değerlendirilmesine olanak sağlarlar. Küme içinde belirli bir UTXO'i ayırt etmek zorlaştığından, büyük bir anonset daha yüksek bir anonimlik seviyesi anlamına gelir. İki tür anonset vardır:


- Muhtemel anonimlik seti;
- Geçmişe dönük anonimlik seti.


İlki, UTXO'ü girişte bilerek, incelenen UTXO'ün gizlendiği grubun büyüklüğünü gösterir. Bu gösterge, Coin'nin gizliliğinin geçmişten günümüze (girdiden çıktıya) bir analize karşı direncinin ölçülmesini sağlar. İngilizce'de bu göstergenin adı "*forward anonset*" veya "*forward-looking metrics*"tir


![](../../dictionnaire/assets/39.webp)


İkincisi, çıkıştaki UTXO'i bilerek, belirli bir Coin için olası kaynakların sayısını gösterir. Bu gösterge, Coin'ün gizliliğinin günümüzden geçmişe (çıktıdan girdiye) bir analize karşı direncinin ölçülmesini sağlar. İngilizce'de bu göstergenin adı "*backward anonset*" veya "*backward-looking metrics*"tir


![](../../dictionnaire/assets/40.webp)


> ► *Fransızca'da genellikle "anonset" teriminin kullanılması kabul edilir Ancak, "ensemble d'anonymat" veya "potentiel d'anonymat" olarak tercüme edilebilir Hem İngilizce hem de Fransızca'da "skor" terimi de bazen anonsetlere atıfta bulunmak için kullanılır (prospektif skor ve retrospektif skor).*