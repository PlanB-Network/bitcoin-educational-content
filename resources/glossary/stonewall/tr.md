---
term: STONEWALL
---

Bitcoin işleminin belirli bir biçimi, gerçekte bir kişi olmadan iki kişi arasındaki bir CoinJoin'ı taklit ederek bir harcama sırasında kullanıcı gizliliğini artırmayı amaçlamaktadır. Aslında bu işlem işbirliğine dayalı değildir. Bir kullanıcı, girdi olarak yalnızca kendi UTXO'larını içerecek şekilde tek başına oluşturabilir. Bu nedenle, başka bir kullanıcıyla senkronize olmanıza gerek kalmadan herhangi bir durum için bir Stonewall işlemi oluşturabilirsiniz.


Stonewall işleminin işleyişi şu şekildedir: işlemin girişinde, gönderici kendisine ait olan 2 UTXO'yu kullanır. İşlem daha sonra 4 çıktı üretir, bunlardan 2'si tam olarak aynı miktarda olacaktır. Diğer 2 tanesi değişikliği oluşturacaktır. Aynı miktardaki 2 çıktıdan sadece biri ödemenin alıcısına gidecektir.


Dolayısıyla, bir Stonewall işleminde yalnızca 2 rol vardır:


- Gönderen, asıl ödemeyi yapan kişi;
- Alıcı, işlemin özel niteliğinden habersiz olabilir ve sadece göndericiden bir ödeme bekler.


![](../../dictionnaire/assets/33.webp)

Stonewall işlemleri hem Samourai Wallet uygulamasında hem de Sparrow wallet yazılımında mevcuttur.


Stonewall yapısı işleme çok fazla entropi ekler ve zincir analizi için izi gizler. Dışarıdan bakıldığında, böyle bir işlem iki kişi arasında küçük bir CoinJoin olarak yorumlanabilir. Ancak gerçekte, tıpkı Stonewall x2 işlemi gibi, bu bir ödemedir. Dolayısıyla bu yöntem zincir analizinde belirsizlikler yaratır, hatta yanlış izlere yol açar. Dışarıdan bir gözlemci Stonewall işleminin modelini tespit etmeyi başarsa bile, tüm bilgilere sahip olmayacaktır. Aynı tutardaki iki UTXO'dan hangisinin ödemeye karşılık geldiğini belirleyemeyeceklerdir. Dahası, girişteki iki UTXO'nun iki farklı kişiden mi geldiğini yoksa bunları birleştiren tek bir kişiye mi ait olduğunu belirleyemeyeceklerdir. Bu son nokta, Stonewall x2 işlemlerinin Stonewall işlemleri ile tamamen aynı modeli izlemesinden kaynaklanmaktadır. Dışarıdan bakıldığında ve ek bağlam bilgisi olmadan, bir Stonewall işlemini bir Stonewall x2 işleminden ayırt etmek imkansızdır. Ancak, birincisi işbirliğine dayalı işlemler değilken, ikincisi öyledir. Bu durum, bu harcamaya ilişkin şüpheleri daha da artırmaktadır.