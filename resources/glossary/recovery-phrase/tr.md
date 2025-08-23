---
term: KURTARMA IFADESI
---

Bazen Mnemonic, seed cümlesi veya gizli cümle olarak da adlandırılan bir kurtarma cümlesi, genellikle 12 veya 24 kelimeden oluşan ve bir entropi kaynağından sözde rastgele bir şekilde üretilen bir dizidir. Sözde rastgele dizi her zaman bir sağlama toplamı ile tamamlanır. Mnemonic ifadesi, isteğe bağlı bir passphrase ile birlikte, bir HD (Hiyerarşik Deterministik) Wallet ile ilişkili tüm anahtarları deterministik olarak türetmek için kullanılır. Bu, bu ifadeden, Bitcoin Wallet'ün tüm özel ve açık anahtarlarını deterministik olarak generate ve yeniden oluşturmanın ve sonuç olarak onunla ilişkili fonlara erişmenin mümkün olduğu anlamına gelir. Kurtarma ifadesinin amacı, bitcoinlerin hem güvenli hem de kullanımı kolay bir şekilde yedeklenmesi ve kurtarılması için bir araç sağlamaktır.


Mnemonic'ye sahip olan herkes ilgili Wallet'in fonlarına erişebileceğinden, bu ifadeyi güvenli ve emniyetli bir yerde saklamak önemlidir. Geleneksel bir Wallet bağlamında ve isteğe bağlı bir passphrase olmadan kullanılırsa, genellikle bir SPOF (Tek Arıza Noktası) oluşturur. Bu nedenle kurtarma ifadesi, sözde rasgele dizinin ve sağlama toplamının, insanlar tarafından gösterimini ve okunabilirliğini kolaylaştırmak için günlük kelimelere kodlanmasıdır. Bu kodlama için kullanılan 2048 kelimelik bir listeyi tanımlayan ve sıralayan BIP39 standardına göre oluşturulur.


> ► *BIP39'daki 2048 kelimelik liste çeşitli dillerde mevcuttur, ancak Wallet yazılımı tarafından en yaygın şekilde desteklenen sürüm olduğu için yalnızca İngilizce sürümünün kullanılması tavsiye edilir.*