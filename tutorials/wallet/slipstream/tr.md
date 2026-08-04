---
name: Slipstream
description: İmzalı bir işlemi Bitcoin ağına yayınlamadan, Slipstream ile doğrudan bir madenciye gönderme
---

![kapak](assets/cover.webp)

Normalde, bir işlemi imzaladığınızda, işlem Bitcoin ağındaki her Bitcoin düğümüne otomatik olarak yayınlanır. Ardından madenciliğe alınmayı bekler.

Ancak, bir blokta yer almadığı sürece, özel anahtarınızı ele geçirmiş bir saldırgan işlemi değiştirebilir ve fonları çalabilir. Bu, özellikle bir ColdCard donanım cüzdanı kullanıyorsanız söz konusu olur.

Madencilik şirketi MARA'nın Slipstream aracı, işlemi ağa yayınlama adımını atlamanızı sağlar: işlem doğrudan (ve yalnızca) bir madenciye gönderilir; bu da işlemi gizli tutar ve ağda açığa çıkmasını önler. İşlemin madenciliğe alınması muhtemelen daha uzun sürecektir, ancak bir değiştirme saldırısına karşı korunacaktır.

Aşağıda, [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) kullanıcılarının ve [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) cüzdanı kullanıcılarının, [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) sayfası üzerinden madenci MARA'nın Slipstream aracını kullanmasını sağlayan bir eğitim sunuyoruz.

⚠️ **Uyarı**: bu araç yalnızca belirli profiller, başlıca Liana cüzdanları, miniscript cüzdanları ve bazı multisig türleri için tasarlanmıştır. Wizardsardine, fonları halihazırda kritik bir hırsızlık riski altında olan cüzdanlar için, örneğin kurtarma ifadesi rastgele sayı üreteci zafiyetinden etkilenen bir ColdCard cihazında oluşturulmuş cüzdanlar için, bu aracın kullanılmasını **açıkça tavsiye etmez**. Bu durumda saldırganla yarış saniyelerle ölçülür ve tek bir madenciye gönderilen bir işlemin onaylanması, normal şekilde yayınlanan bir işlemden çok daha uzun sürer. Bu sizi ilgilendiriyorsa, önce özel eğitimimizi okuyun:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Liana kullanıcıları için

Liana, [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) sayfasının yayıncısı olan Wizardsardine tarafından sürdürülür; dolayısıyla yol doğrudandır: işlemi yayınlamak yerine yalnızca imzalı PSBT dosyasını dışa aktarırsınız.

*Ön koşul: Liana cüzdanınızda fon bulundurun.*

### Adım 1: İşleminizi Liana ile oluşturun

Her zamanki gibi hedef adresi, açıklamayı ve miktarı (burada cüzdanda kullanılabilir maksimum miktar) ekleyerek işleminizi oluşturun.

Ücret oranını ayarlamak için:

- harcamak istediğiniz coin'leri sol alttaki, "Coins selection" altındaki küçük kutuya tıklayarak seçin;
- ardından ücret oranını girin. Bu sayfada açıklandığı gibi, ücretleri önerilen orandan çok daha yüksek ayarlamayı unutmayın: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Son olarak, "İleri"ye tıklayın.

![Liana'da işlemi oluşturma](assets/fr/01.webp)

### Adım 2: İşlem ayrıntılarınızı kontrol edin

"İmzala"ya tıklamadan önce işlem ayrıntılarınızı kontrol edin; özellikle:

- gönderilen miktarı;
- işlem ücretlerine ayrılan satoshi sayısını;
- ama her şeyden önce, fonları gönderdiğiniz adresi ("adres zehirleme" saldırılarından kaçınmak için adresin ilk 5/6 karakterini, son 5/6 karakterini ve ortasındaki 5/6 karakteri kontrol etmeyi unutmayın).

![İşlem ayrıntılarını kontrol etme](assets/fr/02.webp)

### Adım 3: İmzalama cüzdanlarını seçin

Ardından, işleminizi imzalamak için gereken yazılım ve/veya donanım cüzdanlarını seçin. Kısa bir hatırlatma: 2-of-2 multisig cüzdan söz konusu olduğunda, 2 imzadan 2'sine ihtiyacınız vardır.

### Adım 4: İşleminizin PSBT dosyasını dışa aktarın

Bitcoin işlemi artık uygun anahtarlar tarafından imzalandı. "Yayınla"ya tıklamayın; aksi halde işlem tüm ağla paylaşılır ve bir ColdCard donanım cüzdanı kullanıyorsanız işleminiz herkese açık şekilde açığa çıkar ve fonlarınız risk altına girer.

Artık "Dışa aktar"a tıklayabilir, ardından PSBT dosyasını bilgisayarınıza yerel olarak kaydedebilirsiniz.

![PSBT dosyasını Liana'dan dışa aktarma](assets/fr/03.webp)

### Adım 5: İşlemi outofband.wizardsardine.com üzerinden madenciye gönderin

Şimdi son adımlara geldik. İşlemi madenciye göndermek için tek yapmanız gereken PSBT dosyasını alıp belirlenen alana sürükleyip bırakmaktır.

![PSBT dosyasını outofband.wizardsardine.com üzerine bırakma](assets/fr/04.webp)

Ardından işlem aşağıda gösterildiği gibi görüntülenir.

![Kuyruktaki işlem](assets/fr/05.webp)

### Adım 6: İşlemi Slipstream üzerinden gönderin

Son olarak, işlemin Slipstream üzerinden MARA'ya gönderilmesi için tek yapmanız gereken "Gönder"e tıklamaktır.

![İşlemi Slipstream üzerinden gönderme](assets/fr/06.webp)

Birkaç saniye içinde işlem "Gönderiliyor" durumundan "Kabul edildi" durumuna geçer:

![Slipstream tarafından kabul edilen işlem](assets/fr/07.webp)

Geriye yalnızca işlem tanımlayıcısını (TXID) kopyalamak ve ardından madenciliğe alınmasını izlemek için [mempool.space](https://mempool.space/) üzerine yapıştırmak kalır:

![TXID'yi mempool.space üzerinde arama](assets/fr/08.webp)

Lütfen unutmayın: madenci MARA bir blok çıkarıp işleminizi bu bloğa dahil edene kadar işlem "Transaction not found" olarak görünecektir. MARA, Bitcoin ağının hash rate'inin yalnızca yaklaşık %4,5'ine sahip olduğundan bu işlem birkaç on dakika, hatta saatler sürebilir. 4 Ağustos 2026 itibarıyla bu, yaklaşık her 3 saat 45 dakikada bir çıkarılan bir bloğa karşılık gelir.

## Diğer cüzdan kullanıcıları için

[Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) kullanmıyor ancak yine de aracı kullanmak istiyorsanız, burada 2-of-2 multisig cüzdan kullanan bir eğitim bulunmaktadır. Bunun için [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) yazılım cüzdanını kullanacağız.

*Ön koşul: Sparrow cüzdanınızda fon bulundurun.*

### Adım 1: İşleminizi oluşturun

[Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) ile multisig cüzdanınızda işlemi oluşturun. Bu sayfada açıklandığı gibi, ücretleri önerilen orandan çok daha yüksek ayarlamayı unutmayın: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Oluşturulduktan sonra, "İşlem Oluştur"a tıklayın.

![Sparrow'da işlemi oluşturma](assets/fr/09.webp)

### Adım 2: İşleminizi sonlandırın

İşleminizi sonlandırmak için şimdi imzalamanız gerekir. Bunu yapmak için "İmzalama için İşlemi Sonlandır"a tıklayın.

![İşlemi imzalama için sonlandırma](assets/fr/10.webp)

### Adım 3: İşleminizi farklı anahtarlarınızla imzalayın

Şimdi işlemi imzalama zamanı. Bunu yapmak için kullandığınız yazılım ya da donanım cüzdan(lar)ıyla işlemi imzalamanız yeterlidir.

![İşlemi multisig anahtarlarıyla imzalama](assets/fr/11.webp)

### Adım 4: İmzalı işlemi indirin ve ağa yayınlamayın

Bitcoin işlemi artık 2-of-2 multisig'imizin iki anahtarı tarafından imzalandı. "İşlemi Yayınla"ya tıklamayın; aksi halde işlem tüm ağla paylaşılır ve bir ColdCard donanım cüzdanı kullanıyorsanız işleminiz herkese açık şekilde açığa çıkar ve fonlarınız risk altına girer.

![İmzalı işlem, hazır ama yayınlanmamış](assets/fr/12.webp)

### Adım 5: İmzalı işlem betiğini görüntüleyin veya PSBT dosyasını indirin

İmzalı Bitcoin işlemini görüntülemek için şimdi "Son İşlemi Görüntüle"ye tıklayın. Ardından imzalı Bitcoin işlem betiğini kopyalayabilirsiniz:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![İmzalı işlem betiğini görüntüleme](assets/fr/13.webp)

İşlem dosyasını indirmek isterseniz, iki seçenekten birini kullanabilirsiniz:

- "Dosya"ya, ardından "İşlemi kaydet…"e tıklayın;
- veya sağ alttaki ağ bağlantısı düğmesine (sarı düğme) tıklayın, ardından "Son İşlemi Kaydet"e tıklayın.

Ardından işlem bilgisayarınıza yerel olarak kaydedilecektir.

![Son işlemi yerel olarak kaydetme](assets/fr/14.webp)

### Adım 6: İşlemi outofband.wizardsardine.com üzerinden madenciye gönderin

Şimdi son adımlara geldik. İşlemi madenciye göndermek için tek yapmanız gerekenler:

- [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) adresine gitmek;
- önceki adımda kopyalanan imzalı işlem betiğini yapıştırmak, ardından aşağıdaki "ADD TO QUEUE" düğmesine tıklamak;

![İşlem betiğini araca yapıştırma](assets/fr/15.webp)

- veya dosyayı alıp belirlenen alana sürükleyip bırakmak.

![İşlem dosyasını araca bırakma](assets/fr/16.webp)

Ardından işlem aşağıda gösterildiği gibi görüntülenir.

![Kuyruktaki işlem](assets/fr/17.webp)

Bir mesaj size işleminizdeki satoshi cinsinden toplam girdi miktarının bilinmediğini (ve bunun sonucunda ücretler için satoshi sayısının hesaplanamadığını) söylerse, satoshi cinsinden toplam girdi miktarını manuel olarak girmeniz yeterlidir. Bunu bulmak için Sparrow'da, diyagramın ortasında işleminizin görünümüne tıklamanız yeterlidir:

![Sparrow'da gösterilen toplam girdi miktarı](assets/fr/18.webp)

Ardından bu miktarı (örneğimizde 15.904 sats) [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) aracına girin:

![Toplam girdi miktarını manuel olarak girme](assets/fr/19.webp)

Son olarak, ücret oranının doğru olduğunu kontrol edin.

### Adım 7: İşlemi Slipstream üzerinden gönderin

Son olarak, işlemin Slipstream üzerinden MARA'ya gönderilmesi için tek yapmanız gereken "Gönder"e tıklamaktır.

![İşlemi Slipstream üzerinden gönderme](assets/fr/20.webp)

Birkaç saniye içinde işlem "Gönderiliyor" durumundan "Kabul edildi" durumuna geçer:

![Slipstream tarafından kabul edilen işlem](assets/fr/21.webp)

Geriye yalnızca işlem tanımlayıcısını (TXID) kopyalamak ve ardından madenciliğe alınmasını izlemek için [mempool.space](https://mempool.space/) üzerine yapıştırmak kalır:

![TXID'yi mempool.space üzerinde arama](assets/fr/22.webp)

Lütfen unutmayın: madenci MARA bir blok çıkarıp işleminizi bu bloğa dahil edene kadar işlem "Transaction not found" olarak görünecektir. MARA, Bitcoin ağının hash rate'inin yalnızca yaklaşık %4,5'ine sahip olduğundan bu işlem birkaç on dakika, hatta saatler sürebilir. 4 Ağustos 2026 itibarıyla bu, yaklaşık her 3 saat 45 dakikada bir çıkarılan bir bloğa karşılık gelir.
