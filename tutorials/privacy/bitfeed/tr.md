---
name: Bitfeed
description: Ana Bitcoin protokol zincirini keşfedin.
---

![cover](assets/cover.webp)



Bitfeed, Bitcoin protokolünün zincir üzerindeki katmanını görselleştirmeye yönelik bir platformdur. Mempool.space projesine katkıda bulunanlardan biri tarafından başlatılmıştır ve esas olarak minimalist görünümü ve kullanım kolaylığı ile öne çıkmaktadır.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Bu eğitimde, ağdaki tüm işlemleri ve blokları keşfetmenizi sağlayan bu araca bir göz atacağız.



## Bitfeed ile çalışmaya başlama



Bitfeed üç ana noktaya odaklanan bir platformdur:





- Blockchain konsültasyonu**,
- İşlem arama**,
- Mempool'u görselleştirmek**.



### Blok zincirine danışmanlık



Bitfeed ana sayfasında, esas olarak :





- Arama çubuğu: Bu bölüm blok zinciri sorguları için giriş noktasıdır. Burada belirli bir bloğu numarasına veya hash'ine göre arayabilirsiniz. Ayrıca ağdaki belirli işlem bilgilerini doğrulamak için belirli işlemleri ve Bitcoin adreslerini de arayabilirsiniz.



![searchBar](assets/fr/01.webp)



Sol üst köşede, ABD doları (USD) cinsinden tahmin edilen mevcut bitcoin fiyatını görebilirsiniz.



![price](assets/fr/02.webp)



Sağ taraftaki kenar çubuğunda platform menüsü yer almaktadır. Bu menüden platform arayüzünü istediğiniz gibi özelleştirebilir, öğe ekleyebilir veya kaldırabilir ve görüntüleme filtrelerini özelleştirebilirsiniz. Örneğin, her bloğun boyutunu değere göre veya sanal bayt (vBytes) cinsinden ağırlığa göre görüntüleyebilirsiniz.



![menu](assets/fr/03.webp)



Sayfanın ortasında, çıkarılan son blok ve bu blokta yer alan tüm işlemlerin bir görünümü yer almaktadır. Bu bölüm zaman damgası, blokta yer alan toplam bitcoin sayısı, bloğun bayt cinsinden boyutu, işlem sayısı ve bloktaki sanal bayt başına ortalama işlem maliyeti oranı hakkında bilgi sağlar.



![block](assets/fr/04.webp)



Arama çubuğunda belirli bir bloğu arayarak kanalın geçmişine gidebilir ve kriterlerinize göre görüntüleyebilirsiniz.



Örneğin, `879488` bloğundaki işlemleri görüntülemek istiyoruz.



![bloc](assets/fr/05.webp)



Bu bloğun ilk işlemi, bu bloğun madencisinin mining ödülünü kazanmasını sağlayan **coinbase** işlemini temsil eder; bu ödül, yalnızca 100 blok kazıldıktan sonra harcanabilir ve dahil edilen işlem ücretleri ile blok hibesinden oluşur. Bu işlem, sistemde yeni bitcoinlerin çıkarılmasını sağlayan işlemdir.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

Varsayılan olarak, bir bloktaki işlemler iki kritere göre temsil edilir:




- Değer ve ağırlık arasında değişebilen boyut (vByte) ;
- Renk, yaş ve sanal bayt başına işlem ücreti oranı arasında değişebilir.



![options](assets/fr/07.webp)



Dolayısıyla, aynı blokta yer alan tüm işlemlerin blok zincirinde aynı sayıda onaya sahip olduğu sonucuna varabiliriz. En büyük küpler en yüksek miktarda bitcoin içeren işlemleri temsil etmektedir.



Bu yorum, bloğun işlemlerinin renginin ve boyutunun çevirisi hakkında bizi bilgilendiren **"Bilgi "** menü seçeneği ile daha da doğrulanmaktadır.



![infos](assets/fr/08.webp)



Bir bloğun işlemlerini sanal bayt ve ücret oranına göre de görüntüleyebilirsiniz. Bu görünüm bir öncekinden farklı olabilir, çünkü bir işlemde yer alan bitcoin değeri işlemin boyutunu tanımlamaz.



![visualisation](assets/fr/09.webp)



### İşlemleri görüntüleme



Arama çubuğu aracılığıyla tanımlayıcısını kullanarak bir işlemi arayabilirsiniz. Ayrıca bir küpün üzerine tıklayarak o işlemle ilgili bilgileri görebilirsiniz.



Bizim durumumuzda, `879488` bloğundaki en büyük alanı işgal eden işlemi ele alalım.



![biggest](assets/fr/10.webp)



Bu işlemin, kazılan son blok ile bizim seçtiğimiz blok arasındaki farkı temsil eden `42,989` değerine sahip olduğunu göreceksiniz. Bu onaylar Bitcoin ağının güvenliğini güçlendirmeye yardımcı olur, çünkü bu işlemi kötü niyetli olarak değiştirmek için saldırganların tüm ana blok zincirini yeniden yazmak için eşdeğer hesaplama gücüne sahip olması gerekir.



Bu işlemin boyutu `57.088 vByte` olup, bunun başlıca nedeni işlemin yapımında kullanılan UTXO'ların sayısının yüksek olmasıdır (842 giriş). Şaşırtıcı bir şekilde, uygulanan ücret oranı, genel blok ortalaması olan 5,82 sats/vByte ile karşılaştırıldığında nispeten düşük kalmaktadır (sadece 4 sats/vByte).



Bu nedenle, en fazla yer kaplayan işlemin en yüksek işlem maliyeti oranına sahip işlem olması gerekmez.



![transaction](assets/fr/11.webp)



Bilgi** menüsündeki ölçeği takip ederseniz, en yüksek işlem maliyeti oranına sahip işlemin mor renkte olduğunu görürsünüz. Bu, işlem maliyeti oranı `147,49 sats/vByte` olan [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) işlemidir.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool görselleştirme



Mempool, bir bloğa dahil edilmeyi bekleyen Bitcoin işlemlerinin bir arada gruplandığı sanal konumdur. Bitfeed, birkaç Bitcoin madencisinin [mempool](https://planb.academy/resources/glossary/mempool)'una danışılmasına izin vererek çok çeşitli işlem takibi sunar.



![mempool](assets/fr/13.webp)



Bu bölümde, Bitcoin ağının ana zincirindeki tüm geçerli ve henüz onaylanmamış işlemleri takip edebilirsiniz.



![unconfirmed](assets/fr/14.webp)



Artık minimalist, kullanımı kolay bir arayüzden yararlanırken, Bitcoin ağının ana zincirinde bulunan bilgileri görselleştirmek amacıyla blokları ve işlemleri analiz etmek için Bitfeed platformunu kullanma kılavuzuna sahipsiniz. Bu eğitimden keyif aldıysanız, bir sonraki adımı atmanızı öneririz: Amboss projesi aracılığıyla Lightning Network'yi keşfedin.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017