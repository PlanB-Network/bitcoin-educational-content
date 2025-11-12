---
name: Ricochet
description: Ricochet işlemlerini anlama ve kullanma
---
![cover ricochet](assets/cover.webp)


***UYARI:** Samourai Wallet'ın kurucularının tutuklanması ve sunucularına 24 Nisan'da el konulmasının ardından Ricochet aracı artık kullanılamamaktadır. Ancak, bu aracın önümüzdeki haftalarda yeniden kullanıma sunulması mümkündür. Bu arada, Ricochet işlemini yalnızca manuel olarak gerçekleştirebilirsiniz. Bu makalenin teorik kısmı, işleyişini anlamak ve manuel olarak nasıl yapılacağını öğrenmek için geçerliliğini korumaktadır.*


_Bu davayla ilgili gelişmeleri ve ilgili araçlarla ilgili gelişmeleri yakından takip ediyoruz. Yeni bilgiler elde edildikçe bu eğitimi güncelleyeceğimizden emin olabilirsiniz._


_Bu eğitim yalnızca eğitim ve bilgilendirme amaçlıdır. Bu araçların suç amaçlı kullanımını onaylamıyor veya teşvik etmiyoruz. Kendi yargı alanlarındaki yasalara uymak her kullanıcının sorumluluğundadır._


---

> İşleminize ekstra geçmiş ekleyen premium bir araç. Kara listeleri zorlayın ve haksız 3. taraf hesap kapatmalarına karşı korunmaya yardımcı olun.

## Ricochet nedir?


Ricochet, Bitcoin Ownership transferini simüle etmek amacıyla kişinin kendi kendine birden fazla hayali işlem gerçekleştirmesini içeren bir tekniktir. Bu araç diğer Samourai işlemlerinden farklıdır çünkü ileriye dönük bir anonimlik değil, geriye dönük bir anonimlik sağlar. Ricochet, bir Bitcoin Coin'ün değiştirilebilirliğini tehlikeye atabilecek özellikleri bulanıklaştırmaya yardımcı olur.


Örneğin, bir CoinJoin gerçekleştirirseniz, karışımdan elde ettiğiniz Coin çıktınız bu şekilde tanımlanacaktır. Zincir analizi araçları CoinJoin işlemlerinin kalıplarını tespit edebilir ve bunlardan çıkan coinleri etiketleyebilir. Aslında, CoinJoin bir Coin'in tarihsel bağlantılarını kırmayı amaçlar, ancak coinjoins üzerinden geçişi tespit edilebilir kalır. Bir benzetme yapmak gerekirse, bu olgu bir metnin şifrelenmesine benzer: orijinal düz metne erişemesek bile, şifreleme uygulandığı kolayca tespit edilebilir.


Kesin olarak, bu "CoinJoin output Coin" etiketi bir UTXO'un değiştirilebilirliğini etkileyebilir. Exchange platformları gibi düzenlemeye tabi kuruluşlar, CoinJoin'dan geçmiş bir UTXO'u kabul etmeyi reddedebilir, hatta hesaplarının bloke edilmesi veya fonlarının dondurulması riskiyle sahibinden açıklama isteyebilir. Bazı durumlarda, platform davranışınızı devlet yetkililerine bile bildirebilir.


İşte Ricochet yöntemi burada devreye giriyor. Bir CoinJoin tarafından bırakılan ayak izini bulanıklaştırmak için Ricochet, kullanıcının fonlarını farklı adreslerde kendilerine aktardığı dört ardışık işlem gerçekleştirir. Bu işlem dizisinin ardından Ricochet aracı son olarak bitcoinleri bir Exchange platformu gibi nihai hedeflerine yönlendirir. Amaç, orijinal CoinJoin işlemi ile nihai harcama eylemi arasında mesafe yaratmaktır. Bu şekilde, zincir analiz araçları CoinJoin'den sonra muhtemelen bir Ownership transferi yapıldığını ve bu nedenle gönderene karşı harekete geçmenin gereksiz olduğunu düşünecektir.


![ricochet diagram](assets/en/1.webp)


Ricochet yöntemi karşısında, zincir analizi yazılımlarının incelemelerini dört sıçramanın ötesine derinleştireceği düşünülebilir. Ancak bu platformlar tespit eşiğini optimize etme konusunda bir ikilemle karşı karşıyadır. Bir özellik değişikliğinin meydana geldiğini ve önceki bir CoinJoin ile olan bağlantının göz ardı edilmesi gerektiğini kabul ettikleri atlama sayısı üzerinde bir sınır belirlemeleri gerekir. Ancak bu eşiğin belirlenmesi risklidir: gözlemlenen atlama sayısının her uzatılması yanlış pozitiflerin hacmini katlanarak artırır, yani işlem aslında başka biri tarafından gerçekleştirildiği halde hatalı bir şekilde CoinJoin katılımcısı olarak işaretlenen bireyler. Bu senaryo bu şirketler için büyük bir risk oluşturmaktadır, çünkü yanlış pozitifler memnuniyetsizliğe yol açarak etkilenen müşterileri rekabete yönlendirebilir. Uzun vadede, çok iddialı bir eşik, bir platformun rakiplerinden daha fazla müşteri kaybetmesine neden olur ve bu da yaşayabilirliğini tehdit edebilir. Bu nedenle, bu platformlar için gözlemlenen geri dönüş sayısını artırmak karmaşıktır ve 4 genellikle analizlerine karşı koymak için yeterli bir sayıdır.


Bu nedenle, **Ricochet için en yaygın kullanım durumu, size ait bir UTXO üzerindeki bir CoinJoin'e önceki bir katılımı gizlemenin gerekli olduğu durumlarda ortaya çıkar**. İdeal olarak, CoinJoin'ten geçmiş bitcoinleri düzenlenmiş kuruluşlara transfer etmekten kaçınmak en iyisidir. Ancak, başka bir seçeneğin olmadığı durumlarda, özellikle de bitcoinleri fiat para birimine çevirme aciliyetinde, Ricochet etkili bir çözüm sunmaktadır.


## Ricochet Samourai Wallet üzerinde nasıl çalışır?

Ricochet basitçe kişinin kendisine bitcoin gönderdiği bir yöntemdir. Bu nedenle, özel bir araç kullanmadan bir Ricochet'i manuel olarak simüle etmek tamamen mümkündür. Ancak, daha parlak bir sonuçtan faydalanırken süreci otomatikleştirmek isteyenler için Samourai Wallet uygulaması aracılığıyla kullanılabilen Ricochet aracı iyi bir çözümdür.


Hizmet Samourai üzerinden ödendiğinden, bir Ricochet, Mining ücretlerine ek olarak hizmet ücreti olarak `100.000 Sats` maliyetine neden olur. Bu nedenle, kullanımı daha çok önemli miktarlardaki transferler için tavsiye edilir.


Samourai uygulaması Ricochet'in iki çeşidini sunmaktadır:


- Güçlendirilmiş Ricochet ya da "kademeli teslimat", Samourai hizmet ücretlerini birbirini izleyen beş işleme yayma avantajı sunar. Bu seçenek aynı zamanda her işlemin farklı bir zamanda yayınlanmasını ve farklı bir blokta kaydedilmesini sağlar, bu da Ownership değişikliğinin davranışını yakından taklit eder. Daha yavaş olmasına rağmen, bu yöntem acelesi olmayanlar için tercih edilir, çünkü zincir analizine karşı direncini artırarak Ricochet'in verimliliğini en üst düzeye çıkarır.
- Klasik Ricochet, tüm işlemleri azaltılmış bir zaman aralığında yayınlayarak işlemi hızlı bir şekilde yürütmek için tasarlanmıştır. Bu nedenle bu yöntem, güçlendirilmiş yönteme kıyasla daha az gizlilik ve analize karşı daha düşük direnç sunar. Sadece acil transferler için tercih edilmelidir.


## Samourai Wallet'de Ricochet Nasıl Gerçekleştirilir?

Samourai Wallet uygulamasından Ricochet işlemi gerçekleştirmek için eğitim videomuzu izleyin:

![Ricochet YouTube video tutorial](https://youtu.be/Gsz0zuVo3N4)


Bu eğitimde gerçekleştirilen Ricochet işlemlerini incelemek isterseniz, işte buradalar:


- İlk Ricochet işlemi: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://Mempool.space/fr/Testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Son Ricochet işlemi: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://Mempool.space/fr/Testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)


**Harici Kaynaklar:**


- https://docs.samourai.io/en/Wallet/features/ricochet