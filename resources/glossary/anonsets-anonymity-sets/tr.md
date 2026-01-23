---
term: Anonsets (anonimlik kümeleri)
definition: Bir UTXO'nın gizlilik derecesini bir setteki ayırt edilemeyen UTXO'ların sayısını sayarak ölçen göstergeler, tipik olarak coinjoin'den sonra.
---
Anonsetler, belirli bir UTXO’nun gizlilik derecesini değerlendirmek için gösterge olarak kullanılır. Daha spesifik olarak, incelenen çıktıyı içeren küme içerisindeki ayırt edilemeyen UTXO sayısını ölçerler. Aynı UTXO’lardan oluşan bir grubun gerekli olması nedeniyle anonsetler genellikle bir coinjoin döngüsü içinde hesaplanır. Gerektiğinde coinjoinlerin kalitesini değerlendirmeyi mümkün kılarlar. Büyük bir anonset, daha yüksek bir anonimlik düzeyi anlamına gelir; çünkü küme içinde belirli bir UTXO’yu ayırt etmek zorlaşır.

İki tür anonset vardır: forward anonset (forward-looking metrics); ve backward anonset (backward-looking metrics). "*score*" terimi de bazen anonsetleri tanımlamak için kullanılır.

Birincisi, giriş UTXO’su bilindiğinde, incelenen çıkış UTXO’sunun gizlendiği grubun büyüklüğünü gösterir. Bu gösterge, geçmişten bugüne yönelik bir analize (girişten çıkışa) karşı paranın gizliliğinin dayanıklılığını ölçmeyi sağlar. İkincisi, çıkış UTXO’su bilindiğinde, belirli bir para için olası kaynakların sayısını gösterir. Bu gösterge, bugünden geçmişe yönelik bir analize (çıkıştan girişe) karşı paranın gizliliğinin dayanıklılığını ölçmeyi sağlar.
















