---
term: ÜCRET SNIPING
---

Madencilerin, içerdiği işlem ücretlerini talep etmek için yakın zamanda onaylanmış bir bloğu yeniden yazmaya çalıştıkları ve bu arada Mempool'e gelen yüksek ücretli işlemleri ekledikleri bir saldırı senaryosu. Miner için bu saldırının nihai amacı karlılıklarını artırmaktır. Block reward azaldıkça ve işlem ücretleri madencilerin gelirlerinin daha büyük bir bölümünü oluşturdukça ücret sniping'i giderek daha karlı hale gelebilir. Ayrıca, bir önceki blokta yer alan ücretler bir sonraki en iyi aday blokta yer alan ücretlerden önemli ölçüde daha yüksek olduğunda da avantajlı olabilir. Basitleştirmek gerekirse, Miner teşvikler açısından bu seçimle karşı karşıyadır:


- Düşük bir ödül kazanma olasılığı yüksek olan son bloğun ardından normal bir şekilde madencilik yapın;
- Yüksek bir ödül kazanma olasılığı düşük olan önceki bir bloğu kazmaya çalışın (ücret sniping).


Bu saldırı Bitcoin sistemi için bir risk oluşturmaktadır, çünkü daha fazla madenci bunu benimsedikçe, başlangıçta dürüst olan diğer madenciler de aynı şeyi yapmaya teşvik edilmektedir. Gerçekten de, yeni bir Miner ücret kesme girişiminde bulunanlara her katıldığında, saldıran madencilerden birinin başarılı olma olasılığı artar ve karşılığında dürüst madencilerden birinin zinciri uzatma olasılığı azalır. Bu saldırı kitlesel olarak gerçekleştirilir ve zaman içinde sürdürülürse, blok onayları artık bir Bitcoin işleminin değişmezliğinin güvenilir bir göstergesi olmayacaktır. Bu da sistemi potansiyel olarak kullanılamaz hale getirebilir.


Bu riske karşı koymak için çoğu Wallet yazılımı `nLocktime' alanını otomatik olarak doldurur, böylece işlemin doğrulanmasını bir sonraki blok yüksekliğine dahil edilmesine şart koşar. Böylece işlemin bir önceki bloğun yeniden yazımına dahil edilmesi imkansız hale gelir. Eğer `nLocktime`ın yaygın kullanımı Bitcoin kullanıcıları tarafından benimsenirse, bu durum ücret kırpma teşviklerini önemli ölçüde azaltacaktır. Aslında, Blockchain'in potansiyel karını azaltarak yeniden yazılmasından ziyade ilerlemesini teşvik eder. BIP326, Taproot işlemleri için `nSequence` alanının diğer işlem türleri için `nLocktime` alanının eşdeğer etkisini elde etmek için benzer bir şekilde kullanılmasını önermektedir. Bu kullanım, aynı alanı kullanan ikinci Layer protokollerinin gizliliğini de geliştirerek bir taşla iki kuş vuracaktır.