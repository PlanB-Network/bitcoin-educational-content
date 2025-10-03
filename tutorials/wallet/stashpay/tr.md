---
name: StashPay
description: Herkes için minimalist Bitcoin Wallet
---

![cover](assets/cover.webp)



Kullanıcı deneyimi, dünya genelinde Bitcoin çözümlerinin benimsenmesinde kilit bir faktördür. Sorunsuz, basit ve teknik açıdan engelsiz bir deneyim sunmak, birçok cüzdan ve Exchange platformu için önceliktir. Bu açıdan StashPay, minimalist yaklaşımıyla öne çıkarken aynı zamanda Lightning Network'nin gücünü de göstermektedir.



Bu eğitimde, nasıl çalıştığını ve küçük işletmeler ya da tek başına çalışan kişiler için nasıl ideal olduğunu öğrenmek için bu portföye bir göz atacağız.



## StashPay ile çalışmaya başlama



StashPay, öncelikle minimalist, kullanıcı merkezli kullanıcı deneyimi ile tanınan bir Lightning kendi kendine emanet Wallet'tir.  Bu Wallet ile ilk satoshilerinizi almak ve göndermek için herhangi bir teknik bilgiye ihtiyacınız yoktur.



StashPay, React Native'de geliştirilen açık kaynaklı bir projedir ve Bitcoin protokolünün ana zincirindeki işlemlerde bile yüksek işlem ücretleri sorununu çözmeyi amaçlamaktadır. Web sitesinde] (https://stashpay.me/) bulunan indirme bağlantıları aracılığıyla Android ve iOS platformlarında bir mobil uygulama olarak mevcuttur.



![introduce](assets/fr/01.webp)



Google Play Store'da bulunmadığı için Android uygulamasını web sitesinden indirmek önemlidir.


İndirme işlemi tamamlandığında, uygulamayı Android telefonunuza yükleyebilmeniz için lütfen gerekli izinleri verin.



Uygulama yüklendikten sonra, StashPay ilk kez açtığınızda sizin için bir ilk Bitcoin Wallet oluşturacaktır. Herhangi bir işlemden önce, bu Wallet'in bir yedeğini almanızı öneririz. Aşağıda, kurtarma ifadelerinizin düzgün bir şekilde yedeklendiğinden emin olmak için tüm yönergelerimizi bulacaksınız.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

"Ayarlar" simgesine tıklayarak StashPay ayarlarına erişin, ardından **Yedek oluştur** seçeneğine tıklayın. Ardından kurtarma ifadelerinin görüntülenmesine izin verin. Kurtarma ifadelerinizi telefonunuzun panosuna kopyalamayın, çünkü bunlar cep telefonunuzda yüklü diğer dolandırıcılık uygulamaları tarafından erişilebilir olabilir.



![backup](assets/fr/02.webp)



Ayrıca **Wallet'u Kurtar** seçeneğine tıklayarak ve 12 veya 24 kurtarma sözcüğünüzü girerek halihazırda kullandığınız bir Bitcoin Wallet'u geri alabilirsiniz.



### StashPay'de ilk satoshilerinizi alın



Ana ekranda, **Al** düğmesine tıklayın ve kırmızı ile belirtilen tutardan daha büyük bir tutar belirleyin. Bizim durumumuzda, StashPay Wallet ile 0,11 USD'den daha az alamayız.



![receive](assets/fr/03.webp)



Tutarı belirledikten sonra **Invoice** Oluştur düğmesine tıklayabilir, ardından satoshis göndericinize göndermek için Invoice'yi tarayabilir veya kopyalayabilirsiniz.



![receive_sats](assets/fr/04.webp)



Ana sayfadaki "saat" simgesine tıklayarak işlem geçmişinizi görüntüleyebilirsiniz.



![network_fee](assets/fr/05.webp)



Satoshis almak için bir ağ ücreti ödemeniz gerektiğini fark etmiş olacaksınız. Bu ücretler, almak üzere olduğunuz satoshilerden düşülecektir. Bunun nedeni StashPay'in Breez Geliştirme Kitine dayalı bir Wallet olmasıdır. Kitin Lightning node içermeyen uygulamasıyla satoshi almak için Breez müşteriden (bizim durumumuzda StashPay) `% 0,25 + 40 satoshi` ücret alacaktır. Misty Breez eğitimimizde daha fazlasını öğrenin.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### StashPay ile bitcoin gönderin



StashPay ile bitcoin göndermek, minimalist Interface sayesinde oldukça sezgiseldir. Ana ekranda **Gönder** düğmesine tıklayın. QR kodunu tarayın veya satoshis göndermek istediğiniz Address'i yapıştırın. StashPay, bitcoin göndermek istediğiniz Bitcoin protokol zincirini otomatik olarak algılayacaktır.



![send](assets/fr/06.webp)



StashPay, Breez Geliştirme Kitini temel alan bir Wallet olduğundan, ilginç bir avantajdan yararlanmaktadır: ana zincirde düşük maliyetle bitcoin göndermek. Breez, Bitcoin protokolünün farklı zincirleri arasındaki işlemleri gerçekleştirmek için Boltz hizmetini kullanır ve Geliştirme Kitini uygulayan müşterilerin bu hizmetten doğrudan uygulamalarında yararlanmasını sağlar.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Bununla birlikte, Breez SDK, ana zincirdeki bir Address'a bitcoin gönderebileceğiniz minimum bir miktar uygular.



![onchain](assets/fr/07.webp)



Ayrıca alıcınızın Lightning Address'sini kullanarak da bitcoin gönderebilirsiniz. İşlem ayrıntılarınızı inceleyin ve ardından **Gönder** düğmesine tıklayarak onaylayın.



![confirm](assets/fr/08.webp)



## Daha fazla konfigürasyon



StashPay ayarlarında, Wallet kullanımınızı kişiselleştirmek için yapılandırmaları ayarlayabilirsiniz.



StashPay, seçtiğiniz yerel para birimine göre Exchange satoshis yapmanızı sağlar. Para birimleri** seçeneğine tıklayın, ardından StashPay tarafından sunulan +113 para birimi listesinde para biriminizi arayın.



![currencies](assets/fr/09.webp)



Alma seçenekleri** menüsünde, StashPay ile bitcoin almak için tüm ayarları bulacaksınız. Örneğin, **Choose Lightning or Onchain** seçeneğini seçerek, Wallet'ünüzün ana zincirden bitcoin almasını etkinleştirin.



![receive-onchain](assets/fr/10.webp)



OnChain adreslerini tara** seçeneği, çeşitli adreslerinize bağlı tüm UTXO'ları (henüz harcamadığınız bitcoinler) kontrol ederek Wallet'ünüzün bakiyesini yenilemenizi sağlar.



![rescan](assets/fr/11.webp)



Günlüğü dışa aktar** menüsü, çeşitli Bitcoin protokol zincirleri arasındaki işlemleriniz ve atomik alışverişlerinizle ilgili tüm Breez ve Boltz altyapı eylemlerini listeler.



![export](assets/fr/12.webp)



StashPay'in minimalist Bitcoin Wallet'si ile yeni tanıştınız. Bu eğitimi faydalı bulduysanız, Bitcoin ile nasıl başlayacağınız ve ilk bitcoinlerinizi nasıl kazanacağınız hakkındaki eğitimimizi öneririz.



https://planb.network/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f