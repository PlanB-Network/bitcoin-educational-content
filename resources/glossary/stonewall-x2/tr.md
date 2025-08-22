---
term: STONEWALL X2
---

Harcamaya dahil olmayan üçüncü bir tarafla işbirliği yaparak bir harcama sırasında kullanıcı gizliliğini artırmayı amaçlayan belirli bir Bitcoin işlemi biçimi. Bu yöntem, üçüncü bir tarafa ödeme yaparken iki katılımcı arasında bir mini-CoinJoin simülasyonu yapar. Stonewall x2 işlemleri hem Samourai Wallet uygulamasında hem de Sparrow wallet yazılımında mevcuttur (her ikisi de birlikte çalışabilir).


İşlemi nispeten basittir: ödemeyi yapmak için elimizdeki bir UTXO'yı kullanır ve sahip oldukları bir UTXO ile katkıda bulunan üçüncü bir tarafın yardımını ister. İşlem dört çıktı ile sona erer: ikisi eşit miktarda, biri ödeme alıcısının Address'üne, diğeri işbirlikçiye ait bir Address'e yöneliktir. Üçüncü bir UTXO, işbirlikçinin başka bir Address'üne geri gönderilerek ilk tutarı geri almalarına olanak tanır (onlar için nötr bir eylem, eksi Mining ücretleri) ve son bir UTXO, ödemeden elde edilen değişikliği oluşturan sahip olduğumuz bir Address'e geri döner. Böylece Stonewall x2 işlemlerinde üç farklı rol tanımlanmış olur:


- Etkin ödemeyi yapan gönderici;
- İşlemin genel anonimliğini artırmak için bitcoin sağlayan işbirlikçi, sonunda fonlarını tamamen geri alır;
- Alıcı, işlemin özel niteliğinden habersiz olabilir ve sadece göndericiden bir ödeme bekler.


![](../../dictionnaire/assets/3.webp)


Stonewall x2 yapısı işleme çok fazla entropi ekler ve zincir analizinin izlerini karıştırır. Dışarıdan bakıldığında, böyle bir işlem iki kişi arasında küçük bir CoinJoin olarak yorumlanabilir. Ancak gerçekte bu bir ödemedir. Dolayısıyla bu yöntem zincir analizinde belirsizlikler yaratır, hatta yanlış izlere yol açar. Dışarıdan bir gözlemci Stonewall x2 işleminin modelini tespit etmeyi başarsa bile, tüm bilgilere sahip olmayacaktır. Eşit miktarlardaki iki UTXO'dan hangisinin ödemeye karşılık geldiğini belirleyemeyeceklerdir. Dahası, ödemeyi kimin yaptığını da bilemeyeceklerdir. Son olarak, iki girdi UTXO'sunun iki farklı kişiden mi geldiğini yoksa bunları birleştiren tek bir kişiye mi ait olduğunu belirleyemeyeceklerdir. Bu son nokta, klasik Stonewall işlemlerinin Stonewall x2 işlemleri ile tamamen aynı modeli izlemesinden kaynaklanmaktadır. Dışarıdan bakıldığında ve bağlam hakkında ek bilgi olmadan, bir Stonewall işlemini bir Stonewall x2 işleminden ayırt etmek imkansızdır. Ancak, birincisi işbirliğine dayalı işlemler değilken, ikincisi öyledir. Bu da harcamalar hakkında daha da fazla şüphe uyandırmaktadır.