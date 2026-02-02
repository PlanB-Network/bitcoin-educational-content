---
name: Amboss
description: Lightning Network'ı keşfedin ve analiz edin
---

![cover](assets/cover.webp)



Lightning Network, Bitcoin protokolünün bir Layer'üdür ve öncelikle her işlemin işlem hızını artırarak Bitcoin ödemelerinin günlük bazda benimsenmesini teşvik etmek için geliştirilmiştir. Merkezi olmama ilkesine dayanan Lightning Network, eşler arası iletişim kuran ve birbirlerine veri (ödemeler ve ödeme doğrulaması) ileten düğümlerden (Lightning uygulaması çalıştıran bilgisayarlar) oluşur.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Tıpkı ana zincirde olduğu gibi, düğümler arasındaki bağlantıları kolaylaştırmak ve genellikle ağda ortaya çıkan likidite sorununu en aza indirmek için kullanıcıların ağın bilgilerini ve durumunu bilmelerini sağlamak çok önemli hale gelmiştir. Nitekim Lightning Network'te, Bitcoin ana zincirindeki işlemlere kıyasla nispeten daha küçük miktarlarda mikro ödemeler yapılmasını öneriyoruz.



Tüm Lightning düğümlerinin Amboss platformunda mevcut olmadığını unutmamak önemlidir.



Bitcoin protokolünün ana zinciri hakkında faydalı bilgiler sağlayan [Mempool Space](https://Mempool.space) gibi, 2022'den beri [Amboss](https://amboss.space) hakkında bilgi sağlamaktadır:





- Lightning Network üzerindeki düğümler
- Ödeme kanalları ve ödeme kapasiteleri
- Lightning Network'un zaman içindeki gelişimi
- Ödemeleriniz için düğümleri aktarma ücretlerine ilişkin istatistikler.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Bu eğitimde, Lightning Network kullanıcıları, ağı genişletmek için düğümlerini bağlamak isteyenler vb. için önemli bir kaynak olan bu platformda sizi bir tura çıkaracağız.




## Çiftleri bulun



Amboss platformunun amaçlarından biri, ağdaki çeşitli düğümlerin birbirleriyle bağlantı kurmasını ve bilgi iletmesini sağlamaktır. Platformun ana sayfasında, zaten bildiğiniz bir düğümün adını doğrudan arayabilir veya kullandığınız en popüler Lightning portföylerinden düğümler bulabilirsiniz.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Ana sayfada, ayrıca 'ye göre sınıflandırılmış düğümler bulacaksınız:




- Kapasite gelişimi: düğümün açık anahtarıyla ilişkili Bitcoin miktarı ve tüm kanallarında mevcut olan toplam miktar.
- Kanal gelişimi: ağdaki diğer düğümlere yapılan yeni bağlantıların sayısı.
- Düğüm popülerliği: düğümün ne sıklıkta kullanıldığı.



![nodes](assets/fr/03.webp)



Bu nedenle bağlanmak için doğru düğümü seçmek, aşağıdaki kriterleri kontrol etmeye bağlıdır:





- Düğümün yeterli miktarda bitcoine sahip olduğundan emin olun; düğümün kapasitesi ne kadar büyükse, ödeyebileceğiniz bitcoin miktarı da o kadar fazla olur.





- Düğümün ağdaki diğer düğümlerle çok sayıda bağlantıya ve açık kanala sahip olduğundan emin olun.





- Yeni kanal sayısını kontrol ederek düğümün aktif olduğundan ve akranları tarafından hala takdir edildiğinden emin olun; bu düğüm ne kadar çok yeni kanal açarsa, ağdaki diğer düğümler tarafından o kadar çok takdir edilir.



Doğru düğümü bulduğunuzda, düğüm bilgileri sayfasına yönlendirilmek için düğümün adına tıklayın.



Bu Interface'de, yeni oluşturulan kanalın Timestamp'ünü kontrol ederek, bu düğümün etkinliği hakkında bir ipucu elde edeceksiniz. Bu düğümün kanallarının kapasitesi hakkında da bilgi bulacaksınız: ödemelerinizi yapmak için bu düğümü aktif olarak kullanmak istiyorsanız bu bilgi hayati önem taşır.




![node_info](assets/fr/04.webp)



Sol taraftaki bölümde, bu düğümün konumu hakkında daha fazla ayrıntı bulacaksınız. Örneğin, görüntüleyebilirsiniz :




- Açık anahtar: düğüm adının hemen altındaki tanımlayıcı.
- Bu düğümün coğrafi konumu.




![channels](assets/fr/05.webp)



Bu Interface size bu düğüm için bağlantı Address'ini söyler: `pubkey@ip:port` şeklini alır. Örneğimizde, :




- genel anahtar `pubkey`: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Port: `9735`



![geoinfo](assets/fr/06.webp)



Kanallar** bölümünde, açık kanalların listesini ve düğümün ağdaki diğer düğümlerle olan bağlantılarını göreceksiniz. Bu Interface'de, bu düğümün ihtiyaçlarımıza karşılık geldiğini veya güvenilir olduğunu doğrulamak için birkaç bilgi hayati önem taşır:





- Gelen oran**: Seçilen kanala bağlı olarak düğümün aldığı her bir milyon Satoshi için sizden talep edeceği miktar.
- Oran (milyon başına parça)** : kanallarından biri aracılığıyla bir ödeme yapmaya karar verdiğinizde düğümün sizden alacağı milyon birim başına Satoshi sayısını temsil eder. Diyelim ki ppm oranı `500 Sats` olan bir kanal üzerinden `10_000 Sats`lik bir ödeme yapmaya karar verdiniz, düğüme `10_000 * 500 / 1_000_000` satoshis, yani `5 Sats` ödemeniz gerekecek.
- HTLC](https://planb.academy/resources/glossary/htlc) maksimum** : Bu düğümün bu kanallardan biri üzerinden geçiş yapmanıza izin verdiği maksimum miktar.



Bu Interface'deki tabloya başvurarak, eşleştirildiği düğümle ilgili tüm bu bilgileri de bulabilirsiniz.



![channels_info](assets/fr/07.webp)



Kanal haritaları** bölümünde, bu düğüm üzerindeki çeşitli kanalların dağılımını ve kapasitesini görebilirsiniz. Sağdaki açılır listedeki seçeneklerden birini seçerek görüntülenen dağıtım kriterlerini değiştirebilirsiniz.



![cha_maps](assets/fr/08.webp)



Kapanan kanallar** bölümü, düğümün tüm eski kanallarını kapanma türüne göre gruplandırır:




- Karşılıklı kapanış**: kanalın kapanışını ve içindeki bakiyelerin dağıtımını işaret eden işlemi imzalamak için özel anahtarlarını kullanan her iki tarafın anlaşmasını temsil eder
- Bir **zorla kapatma**: kanalın bir bölümünün aniden, tek taraflı olarak kapatılmasını temsil eder. Lightning Network cezaya dayalı bir protokol olduğu için bu tür bir kapatma tavsiye edilmez: bir kanalın bakiyesini dolandırmaya çalıştığınızda, o kanaldaki mevcut tüm bakiyenizi kaybetme riskiyle karşı karşıya kalırsınız.



![closed](assets/fr/09.webp)



Ödemelerinizi kullandığınız düğümdeki bir kanal üzerinden yönlendirmek için transit ücretleri hakkında bilgi alın



![fees](assets/fr/10.webp)



## Ağ bilgileri



Amboss sadece ağ üyesi bilgilerine değil, aynı zamanda ağın kendi durumuna da odaklanır.



İstatistikler** bölümünde, sol taraftaki "Simülasyonlar" menüsünün altında, ödeme tutarının bir fonksiyonu olarak başarılı bir ödeme olasılığını gösteren bir grafik bulacaksınız.



Aslında, eğrinin azaldığını fark edeceksiniz, çünkü ödemenizin miktarı arttıkça, bu ödemenin gerçekleştiğini görme şansınız azalır. Bu, Lightning Network'teki gerçek likidite sorununu yansıtmaktadır. Örneğin, `10_000` satoshis ödemenizin gerçekleşme şansı `%79`dur. Öte yandan, `3_000_000` satoshi`lik bir ödeme için başarı şansınız `%13`ten daha azdır.



![network](assets/fr/11.webp)



Ağ istatistikleri** menüsü, . için istatistikleri grafiksel olarak görüntülemenizi sağlar:




- Ödeme kanalları
- Düğümler
- Kapasite
- Ücretler
- Kanal evrimi.



![network_stat](assets/fr/12.webp)



Piyasa istatistikleri** menüsündeki **Sipariş ayrıntıları** seçeneği, Lightning Network üzerindeki likidite talebini görüntülemenizi sağlar. Bu grafik aynı zamanda hangi kanalların en çok talep gördüğünü ve/veya hangilerinin önemli kapasiteye sahip olduğunu gösterebilir.



![markets](assets/fr/13.webp)




## Araçlar



Amboss, aramalarınızı ve eylemlerinizi optimize etmenize yardımcı olacak bir dizi araç sunar.



### Lightning Network dekoder



Bu araç esas olarak size bir Lightning Invoice, Lightning Address veya Lightning URL'nin yapısının ayrıntılarını vermekten sorumludur.



Ana sayfada, **Araçlar** bölümünde, örneğin Lightning Address'unuzu gönderin.



![decoder](assets/fr/14.webp)



Bu dekoderden aşağıdaki gibi bilgiler elde edebilirsiniz:




- lightning Address'unuzla ilişkili düğümün ortak anahtarı;
- Address'inizden bir Invoice'nin son kullanma süresi;
- Gönderebileceğiniz minimum ve maksimum değer;
- Bu düğümde Nostr etkinleştirilmişse, Address'ünüzle ilişkili Nostr düğümü.



![decode](assets/fr/15.webp)



### Magma IA



Lightning Network düğümlerine bağlantılarınızı verimli bir şekilde yönetmek için Amboss tarafından açıklanan en son aracı keşfedin. Magma AI, önemli bir soruna odaklanmak için özel yapay zeka kullanır: bağlanmak için iyi bir düğüm seçimi yapmak.



![magma](assets/fr/16.webp)



### Satoshi hesap makinesi



Bitcoin'in yerel para biriminizdeki (EUR / USD) güncel fiyatını bulun. Ana sayfada, güncel piyasa fiyatını bulmak için satoshis hesaplayıcısını kullanın.



![calculator](assets/fr/17.webp)




Artık platformun özellikleri ve analiz araçları hakkında tam bir tur attınız. Lütfen Bitcoin **Mempool.space** explorer ile ilgili makalemizi aşağıda bulabilirsiniz.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f