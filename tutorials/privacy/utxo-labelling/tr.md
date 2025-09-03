---
name: Etiketleme UTXO
description: UTXO'inizi nasıl düzgün bir şekilde etiketleyebilirsiniz?
---
![cover](assets/cover.webp)


Bu eğitimde, Bitcoin Wallet'ünüzdeki UTXO'ları etiketleme ve Coin kontrolü hakkında bilmeniz gereken her şeyi keşfedeceksiniz. Ana Bitcoin Wallet yazılımında etiketleri somut olarak nasıl kullanacağımızı keşfettiğimiz pratik bir bölüme geçmeden önce, bu kavramları tam olarak anlamak için teorik bir bölümle başlıyoruz.


## UTXO etiketlemesi nedir?

"Etiketleme", bir Bitcoin Wallet içindeki belirli bir UTXO ile bir ek açıklama veya etiketin ilişkilendirilmesini içeren bir tekniktir. Bu ek açıklamalar Wallet yazılımı tarafından yerel olarak saklanır ve asla Bitcoin ağı üzerinden iletilmez. Etiketleme bu nedenle kişisel yönetim için bir araçtır.


Örneğin, Charles ile Bisq üzerinden bir P2P işleminden bir UTXO alırsam, buna `Bisq P2P Purchase Charles` etiketini atayabilirim.


Etiketleme, fon yönetimini basitleştiren ve kullanıcının gizliliğini optimize eden UTXO'ün kaynağının veya hedeflenen varış yerinin hatırlanmasını sağlar. Etiketleme, "Coin kontrolü" işlevselliği ile birleştirildiğinde daha da önemli hale gelir. Coin kontrolü, iyi Bitcoin cüzdanlarında bulunan ve kullanıcıya bir işlem oluştururken hangi belirli UTXO'ların girdi olarak kullanılacağını manuel olarak seçme olanağı veren bir seçenektir.


Coin kontrollü bir Wallet kullanımı, UTXO etiketlemesi ile birleştiğinde, kullanıcıların işlemleri için UTXO'ları kesin olarak ayırt etmelerini ve seçmelerini sağlar, böylece farklı kaynaklardan gelen UTXO'ların birleştirilmesini önler. Bu uygulama, kullanıcının gizliliğini tehlikeye atabilecek bir işlemin girdilerinin ortak Ownership'ünü öneren Ortak Girdi Ownership Sezgisel (CIOH) ile ilişkili riskleri azaltır.


Bisq'ten gelen KYC'siz UTXO örneğime geri dönelim; bunu, örneğin kimliğimi bilen düzenlenmiş bir Exchange platformundan gelen bir UTXO ile birleştirmekten kaçınmak istiyorum. KYC olmayan UTXO'me ve KYC UTXO'me farklı bir etiket yerleştirerek, Coin kontrol işlevini kullanarak bir harcamayı karşılamak için hangi UTXO'yi girdi olarak kullanacağımı kolayca belirleyebileceğim.


## UTXO'inizi nasıl düzgün bir şekilde etiketleyebilirsiniz?

UTXO'ları etiketlemek için herkese uyan evrensel bir yöntem yoktur. Wallet'nizde yolunuzu kolayca bulabilmeniz için bir etiketleme sistemi tanımlamak size kalmıştır.

Etiketlemede önemli bir kriter de UTXO'nın kaynağıdır. Bu Coin'in Wallet'ünüze nasıl geldiğini basitçe belirtmelisiniz. Bir Exchange platformundan mı? Bir müşteri tarafından yapılan bir fatura ödemesi mi? Eşler arası bir Exchange mü? Ya da bir satın alma işleminden gelen değişikliği mi temsil ediyor? Böylece belirtebilirsiniz:


- "Para Çekme Exchange.com";
- "Ödeme Müşterisi David";
- "P2P Satın Alma Charles";
- "Kanepe satın alımından değişiklik".

![labelling](assets/en/1.webp)

UTXO yönetiminizi iyileştirmek ve Wallet'unuzdaki fon ayrıştırma stratejilerinize bağlı kalmak için etiketlerinizi bu ayrıştırmaları yansıtan ek bir göstergeyle zenginleştirebilirsiniz. Wallet'unuz karıştırmak istemediğiniz iki UTXO kategorisi içeriyorsa, bu grupları açıkça ayırt etmek için etiketlerinize bir işaretleyici entegre edebilirsiniz.


Bu ayrım işaretleri, KYC UTXO (kimliğinizi bilmek) ve KYC olmayan (anonim) arasındaki ayrım veya profesyonel ve kişisel fonlar arasındaki ayrım gibi kendi kriterlerinize bağlı olacaktır. Daha önce bahsedilen etiket örneklerini ele alırsak, bu şu şekilde tercüme edilebilir:


- kYC - Para Çekme Exchange.com`;
- "KYC - Ödeme Müşterisi David";
- "KYC YOK - P2P Satın Alma Charles";
- "KYC YOK - Koltuk alımından değişiklik".

![labelling](assets/en/2.webp)

Her durumda, iyi etiketlemenin ihtiyacınız olduğunda anlayabileceğiniz etiketleme olduğunu unutmayın. Bitcoin Wallet'iniz öncelikle tasarruf amaçlı ise, etiketler sizin için ancak birkaç on yıl sonra faydalı olabilir. Bu nedenle, açık, kesin ve kapsamlı olduklarından emin olun.


İşlemler boyunca Coin'nın etiketlenmesini sürdürmek de tavsiye edilir. Örneğin, KYC'siz bir UTXO konsolidasyonu sırasında, ortaya çıkan UTXO'yi sadece "konsolidasyon" olarak değil, Coin'nın kaynağının net bir izini korumak için özellikle "KYC'siz konsolidasyon" olarak işaretlediğinizden emin olun.


Son olarak, bir etikete tarih koymak zorunlu değildir. Çoğu Wallet yazılımı zaten işlem tarihini görüntüler ve bu bilgiyi Block explorer'i kullanarak txid'tan almak her zaman mümkündür.


## Eğitim: Spectre Masaüstünde Etiketleme


Spectre Desktop'ta Wallet'inizi bağlayın ve açın, ardından `Adresler` sekmesini seçin.


![labelling](assets/notext/3.webp)

Burada, tüm adreslerinizin listesini ve üzerlerinde kilitli olan bitcoinleri göreceksiniz. Varsayılan olarak, adresler `Etiket` sütunu altındaki dizinlerine göre tanımlanır. Bir etiketi değiştirmek için üzerine tıklamanız, istediğiniz etiketi girmeniz ve ardından mavi simgeye tıklayarak onaylamanız yeterlidir.

![labelling](assets/notext/4.webp)


Etiketiniz daha sonra adresleriniz listesinde görünecektir.


![labelling](assets/notext/5.webp)


Alıcı Address'nizi gönderici ile paylaştığınızda önceden bir etiket de atayabilirsiniz. Bunu yapmak için, `Alma' sekmesine erişerek, etiketinizi ayrılmış alana not edin.


![labelling](assets/notext/6.webp)


## Eğitim: Elektrum Üzerinde Etiketleme


Electrum Wallet'te, Wallet'ünüze giriş yaptıktan sonra, `History` sekmesinden etiket atamak istediğiniz işleme tıklayın.


![labelling](assets/notext/7.webp)


Yeni bir pencere açılır. Açıklama kutusuna tıklayın ve etiketinizi yazın.


![labelling](assets/notext/8.webp)


Etiket girildikten sonra bu pencereyi kapatabilirsiniz.


![labelling](assets/notext/9.webp)


Etiketiniz başarıyla kaydedildi. Etiketi `Açıklama` sekmesi altında bulabilirsiniz.


![labelling](assets/notext/10.webp)


Coin kontrolünü gerçekleştirebileceğiniz `Coins` sekmesinde etiketiniz `Label` sütununda bulunur.


![labelling](assets/notext/11.webp)


## Eğitim: Green Wallet üzerinde Etiketleme


Green Wallet uygulamasında, Wallet'nize erişin ve etiketlemek istediğiniz işlemi seçin. Ardından, etiketinizi not etmek için küçük kalem simgesine tıklayın.


![labelling](assets/notext/12.webp)


Etiketinizi yazın ve ardından Green `Kaydet` düğmesine tıklayın.


![labelling](assets/notext/13.webp)


Etiketinizi hem işleminizin ayrıntılarında hem de Wallet'nizin kontrol panelinde bulabilirsiniz.


![labelling](assets/notext/14.webp)


## Eğitim: Samourai Wallet üzerinde etiketleme


Samourai Wallet'de, bir işleme etiket atamanızı sağlayan farklı yöntemler vardır. Birincisi için, Wallet'nizi açarak başlayın ve etiket eklemek istediğiniz işlemi seçin. Ardından `Notlar` kutusunun yanında bulunan `Ekle` düğmesine basın.


![labelling](assets/notext/15.webp)


Etiketinizi yazın ve mavi `Ekle` düğmesine tıklayarak onaylayın.


![labelling](assets/notext/16.webp)


Etiketinizi işleminizin ayrıntılarında ve aynı zamanda Wallet'ünüzün gösterge panelinde bulabilirsiniz.


![labelling](assets/notext/17.webp)

İkinci yöntem için, ekranın sağ üst köşesindeki üç küçük noktaya ve ardından `Harcama Yapılmamış İşlem Çıktılarını Göster` menüsüne tıklayın.

![labelling](assets/notext/18.webp)


Burada, Wallet'inizde bulunan tüm UTXO'ların kapsamlı bir listesini bulacaksınız. Görüntülenen liste mevduat hesabımla ilgilidir, ancak bu işlem özel menüden gidilerek Whirlpool hesapları için çoğaltılabilir.


Ardından etiketlemek istediğiniz UTXO üzerine tıklayın ve ardından `Ekle` düğmesine tıklayın.


![labelling](assets/notext/19.webp)


Etiketinizi yazın ve mavi `Ekle` düğmesine tıklayarak onaylayın. Daha sonra etiketinizi hem işleminizin ayrıntılarında hem de Wallet'nizin kontrol panelinde bulacaksınız.


![labelling](assets/notext/20.webp)


## Eğitim: Sparrow wallet üzerinde etiketleme


Sparrow wallet yazılımı ile etiketleri birden fazla şekilde atamak mümkündür. En basit yöntem, alıcı bir Address'ı göndericiye iletirken önceden bir etiket eklemektir. Bunu yapmak için, `Alma' menüsünde `Etiket' alanına tıklayın ve seçtiğiniz etiketi girin. Bu etiket, bitcoinler Address'a ulaşır ulaşmaz yazılım boyunca korunacak ve erişilebilir olacaktır.


![labelling](assets/notext/21.webp)


Address'inizi teslim aldıktan sonra etiketlemeyi unuttuysanız, daha sonra `İşlemler` menüsü aracılığıyla bir etiket eklemeniz mümkündür. Bunun için `Etiket` sütununda işleminizin üzerine tıklamanız ve ardından istediğiniz etiketi girmeniz yeterlidir.


![labelling](assets/notext/22.webp)


Ayrıca `Adresler` menüsünden etiketlerinizi ekleme veya değiştirme seçeneğiniz de vardır.


![labelling](assets/notext/23.webp)


Son olarak, etiketlerinizi `UTXOs` menüsünde görüntüleyebilirsiniz. Sparrow wallet etiketinizin arkasına otomatik olarak parantez içinde çıktının niteliğini ekler, bu da değişiklikten kaynaklanan UTXO'ları doğrudan alınanlardan ayırt etmeye yardımcı olur.


![labelling](assets/notext/24.webp)