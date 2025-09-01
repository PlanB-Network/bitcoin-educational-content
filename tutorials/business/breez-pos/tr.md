---
name: Breez satış noktası

description: Breez POS kullanarak Bitcoin kabul etmeye başlama kılavuzu
---

![cover](assets/cover.webp)

_Bu metin Breez dokümantasyon web sitesinden alınmıştır: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_


## Breez POS nedir?


**Breez** tam hizmet veren, velayetsiz bir Lightning uygulamasıdır. Bunu biraz açalım:



- Lightning**, işlem sürelerini dakikalardan milisaniyelere ve işlem ücretlerini birkaç dolardan birkaç sente veya daha azına indiren bir Bitcoin ödeme ağıdır. Lightning, Bitcoin'i harika yapan tüm avantajları korurken Bitcoin'i dijital altından dijital para birimine dönüştürür.
- Non-custodial**, Breez'in kullanıcıların parasına el koymadığı anlamına gelir. Birçok Lightning uygulaması kullanıcılarının parasına el koyar. Temelde Bitcoin bankalarıdır. Breez gibi velayetsiz bir uygulama ile tüm kullanıcılar kendi bankalarıdır.
- Tam hizmet**, Breez'in neredeyse tüm teknik işlemleri otomatik olarak ve arka planda hallettiği anlamına gelir. Kanal oluşturma, gelen likidite ve yönlendirme gibi şeyler kaputun altında kalır. (Ancak Breez aynı zamanda açık kaynaklıdır, bu nedenle teknolojiyi denetlemek isteyenler bunu yapabilirler!)


**Breez POS** satış noktası modumuzun kısaltmasıdır. Başka bir deyişle Breez, Lightning ödemelerini kabul etmek isteyen işletmeler ve tüccarlar için dijital bir yazar kasa gibi çalışır (Bitcoin için deri bir Wallet'ün dijital versiyonu ve yeni nesil bir podcast oynatıcı gibi olan "standart" moduna ek olarak). Şimdi Breez'i işletmeniz için bir Lightning yazar kasası olarak nasıl kuracağınıza bakalım.


## Breez'e nasıl başlanır?


1. İlk adım uygulamayı indirmektir. Android ve iOS için mevcuttur (TestFlight'ı yükleyin ve cihazınızdan bağlantıya tıklayın).

2. Breez kendini otomatik olarak Google Drive, iCloud veya herhangi bir WebDav sunucusuna yedekleyebilir.

**Not:** her cihaz kendi Lightning düğümünü çalıştırır. POS modunu istediğiniz kadar cihazda çalıştırabilirsiniz, ancak bakiyeler ayrı kalacaktır.

3. Uygulama açıkken, Satış Noktası modunu bulmak için sol üstteki simgeye tıklayın.


## POS kurulumu


POS'u ayarlamak için sol üstteki simgeye tıklayın, ardından Satış Noktası > POS Ayarları'na tıklayın.


### Yönetici Şifresi


POS Ayarları'nda bir yönetici şifresi oluşturma seçeneğiniz vardır. Yönetici şifresi, Breez uygulamasından yetkilendirme olmadan giden ödemelerin gönderilmesini imkansız hale getirir. Satış personeli yalnızca cihazdan ödeme alabilecektir. Bu seçeneği kullanıyorsanız Breez'in yedeklemesine erişimi de engellemek isteyebileceğinizi unutmayın; bu nedenle bu kullanım durumu için harici bir WebDav hesabı (ör. Nextcloud) kullanılması önerilir.


### Öğeler Listesi


Ürün listesi, satılık ürünlerin ve fiyatlarının yer aldığı bir katalogdur. Listeye ürün eklemenin iki yolu vardır:



- Kalemleri teker teker girmek için ana POS görünümünün üst kısmındaki Kalemler'e, ardından sağ alttaki "+" işaretine tıklayın. Burada tek bir kalem türünün adını, fiyatını (seçtiğiniz para birimi eşdeğerinde görüntülenir) ve SKU'sunu (bu kalem türü için benzersiz bir dahili tanımlayıcı; isteğe bağlıdır) girebilirsiniz.
- Aynı anda çok sayıda kalem girmek için sol üstteki hesap makinesi simgesine, ardından Satış Noktası > Tercihler > POS Ayarları'na ve ardından Kalem Listesi'nin sağındaki üç noktaya ve ardından CSV'den İçe Aktar'a tıklayın. Bu, önceden hazırladığınız ve kalemlerinizin adlarını, fiyatlarını ve SKU'larını içeren bir CSV dosyasını içe aktarmanızı sağlayacaktır.


### Fiat Ekranı


Breez yalnızca Bitcoin gönderir ve alır ve Lightning'de daha küçük miktarlarda olma eğiliminde olan çoğu işlem için toplam genellikle Satoshis, yani Sats olarak görüntülenir (1 BTC = 100.000.000 Sats). Bununla birlikte, birçok tüccar, yerel fiat para biriminde görüntülenen satın alma değerini görebilmeyi (ve müşterilere söyleyebilmeyi) pratik bulmaktadır.


Ana POS görünümünde, o anda görüntülenmekte olan para birimi sağ tarafta görünür (varsayılan SAT'tır). Ayrıca görüntülenebilecek diğer para birimlerinin bir açılır listesi de vardır. Bu açılır listeden para birimleri eklemek veya kaldırmak için Satış Noktası > Tercihler > Fiat Para Birimleri seçeneğine tıklayın. Ardından açılır menünüzde bulunmasını istediğiniz para birimlerini işaretleyin ve çıkarılmasını istediklerinizin işaretini kaldırın.


Görüntülenen değerler, Exchange oranı verileri için saygın bir kaynak olan yadio'dan alınmıştır ve neredeyse gerçek zamanlı olarak güncellenmektedir. Ancak unutmayın: şu anda görüntülenen para birimi değeri ne olursa olsun, ödemenin kendisi Bitcoin cinsindendir.


### Bir Siparişin Ücretlendirilmesi


Siparişi oluşturmak için, ürün listesinden ürün ekleyin veya tuş takımına bir toplam girin. Ardından ana POS görünümünün üst kısmındaki Ücretlendir'e tıklayın. Ardından, müşterinin Lightning uygulamasıyla tarayabileceği, cihazınızdaki başka bir uygulamadan doğrudan paylaşabileceğiniz veya gerektiğinde kopyalayıp yapıştırabileceğiniz bir QR kodu göreceksiniz.


Bu kod tarandığında veya paylaşılan/yapıştırılan Invoice'a tıklandığında, müşteri Lightning uygulamasında Invoice'u görecek ve ödeme yapma ve işlemi hemen gerçekleştirme seçeneğine sahip olacaktır.


Satıcının cihazındaki Breez uygulamasında Ödeme onaylandı! animasyonunu gördüğünüzde, müşteri için bir makbuz generate oluşturmak üzere yazıcı simgesine tıklayabilirsiniz. Android'de bir makbuz yazıcısı kullanmak için bu sürücüyü kullanmayı deneyin. İşlemler ekranı aracılığıyla geçmiş işlemleri de yazdırabileceğinizi unutmayın.


### Satış Raporu


Satışlarınızın günlük, haftalık ve/veya aylık raporunu görüntülemek için (muhasebe veya diğer amaçlar için) sol üstteki simgeye ve ardından İşlemler'e tıklayın. Raporu görüntülemek için Rapor simgesine ve seçilen tarih aralığını değiştirmek için Takvim simgesine tıklayın.


### İşlemleri Dışa Aktarma


Breez'de alınan ödemelerin bir listesini görüntülemek için sol üstteki simgeye ve ardından İşlemler'e tıklayın. Gelen ödemelerin bir listesini CSV formatında dışa aktarmak için sağ üstteki üç noktaya ve ardından Dışa Aktar'a tıklayın. Listeyi belirli bir zaman dilimiyle kısıtlamak için takvim simgesine tıklayarak bir tarih aralığı belirleyin.


### Makbuz Yazdırma


Bir satış makbuzunu yazdırmak için, ödeme onayı iletişim kutusunun sağ üst köşesindeki yazdır simgesine tıklayın. Alternatif olarak, sol üstteki simgeye tıklayın ve ardından İşlemler'e tıklayın. Yazdırılacak satışı bulun, açın ve sağ üstteki yazdır simgesine tıklayın.


**Not:** bu sürücüyü taşınabilir bir 58mm/80mm Bluetooth/USB termal yazıcıya yazdırmak için kullanın.


## Daha fazlasını öğrenmek istiyorum



- Lightning and Breez hakkında daha fazla bilgi için [blog](https://breez.technology/blog) adresimize göz atın.
- Uygulamadan en iyi şekilde nasıl yararlanılacağı ve yaygın işlemlerin nasıl gerçekleştirileceği hakkında daha fazla teknik ipucu için [dokümantasyon](https://breez.technology/documentation) adresimize göz atın.
- Eğer takılırsanız ve cevabı yardım literatürümüzde bulamazsanız, bizi [Telegram](https://t.me/breez_labs) adresinde bulabilir veya bize [email](mailto:support@breez.technology) gönderebilirsiniz.
- Breez POS modunun hayranlarımız ve kullanıcılarımız tarafından yapılan bazı tanıtım videolarını görmek isterseniz, [burada](https://www.youtube.com/watch?v=xxxx) harika bir kısa video ve [burada](https://www.youtube.com/watch?v=xxxx) daha uzun, daha ayrıntılı bir video.