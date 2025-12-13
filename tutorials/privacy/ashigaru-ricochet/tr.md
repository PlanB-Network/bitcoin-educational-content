---
name: Ashigaru - Ricochet
description: Ricochet işlemlerini anlama ve kullanma
---
![cover ricochet](assets/cover.webp)



> *İşleminize ekstra geçmiş ekleyen premium bir araç. Kara listeleri zorlayın ve haksız 3. taraf hesap kapatmalarına karşı korunmaya yardımcı olun.*

## Ricochet nedir?



Ricochet, bitcoin sahipliğinin transferini simüle etmek için kişinin kendisine yönelik birkaç hayali işlem gerçekleştirmesinden oluşan bir tekniktir. Bu araç, Ashigaru'nun (Samurai Wallet'den miras kalan) diğer işlemlerinden farklı olarak, ileriye dönük anonimlik değil, geriye dönük bir anonimlik biçimi sağlar. Aslında Ricochet, bir Bitcoin parçasının değiştirilebilirliğini tehlikeye atabilecek özellikleri bulanıklaştırır.



Örneğin, bir coinjoin yaparsanız, karışımdan çıkan parçanız bu şekilde tanımlanacaktır. Zincir analizi araçları coinjoin işlemlerinin paternlerini tespit edebilir ve bunlardan çıkan parçalara bir etiket atayabilir. Aslında coinjoin bir coin'in tarihsel bağlantılarını koparmayı amaçlar, ancak coinjoin'ler arasındaki geçişi tespit edilebilir kalır. Benzetme yapmak gerekirse, bu olgu bir metnin şifrelenmesine benzer: orijinal metne açık metin olarak erişilemese de, şifreleme uygulandığını tespit etmek kolaydır.



"Coinjoined" etiketi bir UTXO'nin değiştirilebilirliğini etkileyebilir. Borsa platformları gibi düzenlenmiş kuruluşlar, coinjoined bir UTXO'yi kabul etmeyi reddedebilir, hatta hesabınızın bloke edilmesi veya fonlarınızın dondurulması riskiyle birlikte sahibinden açıklama talep edebilir. Bazı durumlarda, platform davranışınızı devlet yetkililerine bile bildirebilir.



İşte Ricochet yöntemi burada devreye giriyor. Bir coinjoin'in bıraktığı izi silikleştirmek için Ricochet, kullanıcının fonlarını farklı adreslerden kendisine aktardığı dört ardışık işlem gerçekleştirir. Bu işlem dizisinden sonra Ricochet aracı son olarak bitcoinleri bir değişim platformu gibi nihai hedeflerine yönlendirir. Amaç, orijinal coinjoin işlemi ile nihai harcama eylemi arasında mesafe yaratmaktır. Bu şekilde, blok zinciri analiz araçları coinjoin işleminden sonra muhtemelen bir sahiplik transferi gerçekleştiğini ve bu nedenle parayı çıkaran kişiye karşı bir işlem yapılmasına gerek olmadığını varsayacaktır.



![image](assets/fr/01.webp)



Ricochet yöntemiyle karşılaşıldığında, zincir analizi yazılımının incelemesini dört sıçramanın ötesine derinleştireceği düşünülebilir. Ancak bu platformlar tespit eşiğini optimize etme konusunda bir ikilemle karşı karşıyadır. Bir eşik atlama sayısı belirlemeleri gerekir, bu sayıdan sonra bir sahiplik değişikliğinin gerçekleşmiş olabileceğini ve önceki bir coinjoin'e olan bağlantının göz ardı edilmesi gerektiğini kabul ederler. Ancak, bu eşiğin belirlenmesi risklidir: gözlemlenen atlama sayısındaki her bir artış, yanlış pozitiflerin hacmini katlanarak artırır, yani aslında işlem başka biri tarafından gerçekleştirilmişken, hatalı bir şekilde bir coinjoin katılımcısı olarak işaretlenen bireyler. Bu senaryo bu şirketler için büyük bir risk oluşturmaktadır, çünkü yanlış pozitifler memnuniyetsizliğe yol açmakta ve bu da etkilenen müşterileri rekabete yönlendirebilmektedir. Uzun vadede, aşırı iddialı bir tespit eşiği, bir platformun rakiplerinden daha fazla müşteri kaybetmesine yol açar ve bu da yaşayabilirliğini tehdit edebilir. Bu nedenle, bu platformlar için gözlemlenen geri dönüş sayısını artırmak karmaşıktır ve 4 genellikle analizlerine karşı koymak için yeterli bir sayıdır.



Bu nedenle, **Ricochet için en yaygın kullanım durumu, sahip olduğunuz bir UTXO'teki bir coinjoin'e daha önce katıldığınızı gizlemeniz gerektiğinde ortaya çıkar.** İdeal olarak, bir coinjoin'den geçen bitcoinleri düzenlenmiş kuruluşlara transfer etmekten kaçınmak en iyisidir. Bununla birlikte, başka bir seçeneğin kalmaması durumunda, özellikle de bitcoinlerin devlet para biriminde acil olarak tasfiye edilmesi gerektiğinde, Ricochet etkili bir çözüm sunar.



## Ricochet Ashigaru üzerinde nasıl çalışır?



Ricochet, ilk olarak Samurai Wallet geliştiricileri tarafından icat edilen, kişinin kendisine bitcoin gönderme yöntemidir. Bu nedenle, özel bir araca ihtiyaç duymadan Ricochet'i manuel olarak simüle etmek tamamen mümkündür. Bununla birlikte, daha parlak bir sonucun tadını çıkarırken süreci otomatikleştirmek isteyenler için, Ashigaru uygulaması (bir Samourai fork olan) aracılığıyla kullanılabilen Ricochet aracı iyi bir çözümdür.



Ashigaru hizmeti için ücret aldığından, bir Ricochet hizmet ücreti olarak `100.000 sats`ye ve ayrıca bir mining ücretine mal olur. Bu nedenle önemli miktarlardaki transferler için kullanılması tavsiye edilir.



Ashigaru uygulaması iki Ricochet çeşidi sunmaktadır:





- Güçlendirilmiş Ricochet veya "kademeli teslimat", Ashigaru'nun hizmet ücretlerini birbirini takip eden beş işleme yayma avantajı sunar. Bu seçenek aynı zamanda her işlemin ayrı bir zamanda yayınlanmasını ve farklı bir bloğa kaydedilmesini sağlayarak mülkiyet değişikliği davranışını mümkün olduğunca yakından taklit eder. Daha yavaş olmasına rağmen, bu yöntem acelesi olmayanlar için tercih edilir, çünkü Ricochet'in zincir analizine karşı direncini güçlendirerek verimliliğini en üst düzeye çıkarır;





- İşlemi hızlı bir şekilde yürütmek için tasarlanan klasik Ricochet, tüm işlemleri azaltılmış bir zaman aralığında yayınlar. Bu yöntem, bu nedenle, güçlendirilmiş yönteme göre daha az gizlilik ve analize karşı daha az direnç sunar. Yalnızca acil gönderiler için kullanılmalıdır.



## Ashigaru üzerinde nasıl Ricochet yapılır?



Ashigaru'da ricochet yapmak çok basittir: bir gönderme işlemi oluştururken ilgili seçeneği etkinleştirmeniz yeterlidir. Başlamak için, `+` düğmesine, ardından `Gönder` düğmesine tıklayın ve parayı göndermek istediğiniz hesabı seçin.



![Image](assets/fr/02.webp)



İşlem bilgilerini doldurun: gönderilecek tutar ve Ricochet atlamalarından sonra alıcının son adresi. Ardından `Ricochet` seçeneğini işaretleyin.



![Image](assets/fr/03.webp)



Daha sonra teori bölümünde tartışılan iki Ricochet modu arasında seçim yapabilirsiniz: tüm işlemlerin aynı bloğa dahil edildiği klasik Ricochet veya daha uzun bir gecikme pahasına Ricochet kalitesini artıran kademeli teslimat.



Seçiminizi yaptıktan sonra, onaylamak için ekranın altındaki oka basın.



![Image](assets/fr/04.webp)



Bir sonraki ekranda, işleminizin tam bir özetini göreceksiniz. Burası aynı zamanda Ricochet işlemleriniz için ücret oranını piyasa koşullarına göre ayarlayabileceğiniz yerdir. Her şey sizi tatmin ediyorsa, Ricochet işlemlerini imzalamak ve dağıtmak için yeşil oku sürükleyin.



![Image](assets/fr/05.webp)



Çeşitli atlamalar otomatik olarak çalışırken bekleyin.



![Image](assets/fr/06.webp)



İşlemleriniz başarıyla yayınlanmıştır.



![Image](assets/fr/07.webp)



Artık Ashigaru uygulamasında bulunan Ricochet seçeneğine tamamen aşinasınız. Daha ileri gitmek için, size zincir üzerindeki gizliliğinizi nasıl güçlendireceğinizi ayrıntılı olarak öğretecek olan BTC 204 eğitim kursumu almanızı tavsiye ederim.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c