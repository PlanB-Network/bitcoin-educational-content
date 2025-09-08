---
name: PlanB Network'e bir etkinlik ekleyin
description: PlanB Network'e yeni bir etkinlik eklemeyi nasıl öneririm?
---
![event](assets/cover.webp)


PlanB'nin misyonu, Bitcoin hakkında mümkün olduğunca çok dilde üst düzey eğitim kaynakları sağlamaktır. Sitede yayınlanan tüm içerik açık kaynaklıdır ve GitHub'da barındırılmaktadır, bu da herkese platformun zenginleştirilmesine katkıda bulunma fırsatı sunmaktadır.


PlanB Network sitesine bir Bitcoin konferansı eklemek ve etkinliğinizin görünürlüğünü artırmak istiyor ancak nasıl yapacağınızı bilmiyorsanız? Bu eğitim tam size göre!

![event](assets/01.webp)


- İlk olarak, GitHub'da bir hesabınızın olması gerekir. Nasıl hesap oluşturacağınızı bilmiyorsanız, size rehberlik edecek ayrıntılı bir eğitim hazırladık.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- PlanB'nin verilere adanmış GitHub deposuna] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) `resources/conference/` bölümüne gidin:

![event](assets/02.webp)


- Sağ üstteki `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![event](assets/03.webp)


- PlanB Network'ün içeriğine daha önce hiç katkıda bulunmadıysanız, orijinal deponun Fork'ünü oluşturmanız gerekecektir. Bir depoyu çatallamak, kendi GitHub hesabınızda o deponun bir kopyasını oluşturmak anlamına gelir ve orijinal depoyu etkilemeden proje üzerinde çalışmanıza olanak tanır. Fork this repository` düğmesine tıklayın:

![event](assets/04.webp)


- Daha sonra GitHub düzenleme sayfasına ulaşacaksınız:

![event](assets/05.webp)


- Konferansınız için bir klasör oluşturun. Bunu yapmak için, `Dosyanızı adlandırın...` kutusuna konferansınızın adını boşluk yerine tire ile küçük harflerle yazın. Örneğin, konferansınızın adı "Paris Bitcoin Konferansı" ise, `paris-Bitcoin-conference` yazmalısınız. Ayrıca konferansınızın yılını da ekleyin, örneğin: `paris-Bitcoin-conference-2024`:

![event](assets/06.webp)


- Klasörün oluşturulduğunu doğrulamak için, aynı kutuya adınızdan sonra bir eğik çizgi not edin, örneğin: `paris-Bitcoin-conference-2024/`. Eğik çizgi eklemek otomatik olarak bir dosya yerine bir klasör oluşturur:

![event](assets/07.webp)


- Bu klasörde `events.yml` adında ilk YAML dosyasını oluşturacaksınız:

![event](assets/08.webp)


- Bu şablonu kullanarak bu dosyayı konferansınızla ilgili bilgilerle doldurun:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
project:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language:
-
links:
website:
replay_url:
live_url :
tags:
-
```


Örneğin, YAML dosyanız aşağıdaki gibi görünebilir:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

Kuruluşunuz için henüz bir "*proje*" tanımlayıcınız yoksa, bu diğer öğreticiyi izleyerek ekleyebilirsiniz.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Bu dosyada değişiklik yapmayı tamamladığınızda, `Değişiklikleri yap...` düğmesine tıklayarak kaydedin:

![event](assets/10.webp)


- Değişiklikleriniz için bir başlık ve kısa bir açıklama ekleyin:

![event](assets/11.webp)


- Green `Değişiklik öner` düğmesine tıklayın:

![event](assets/12.webp)


- Daha sonra tüm değişikliklerinizi özetleyen bir sayfaya ulaşacaksınız:

![event](assets/13.webp)


- Sağ üstteki GitHub profil resminize ve ardından `Repolarınız` seçeneğine tıklayın:

![event](assets/14.webp)


- PlanB Ağ deposundan Fork'nizi seçin:

![event](assets/15.webp)


- Pencerenin üst kısmında yeni dalınızla birlikte bir bildirim görmelisiniz. Muhtemelen `patch-1` olarak adlandırılmıştır. Üzerine tıklayın:

![event](assets/16.webp)


- Şu anda çalışma şubenizdesiniz:

![event](assets/17.webp)


- Resources/conference/` klasörüne geri dönün ve bir önceki işlemde oluşturduğunuz konferansınızın klasörünü seçin:

![event](assets/18.webp)


- Konferansınızın klasöründe, `Dosya ekle` düğmesine ve ardından `Yeni dosya oluştur` düğmesine tıklayın:

![event](assets/19.webp)


- Bu yeni klasöre `assets` adını verin ve sonuna bir eğik çizgi `/` koyarak oluşturulduğunu onaylayın:

![event](assets/20.webp)


- Bu `assets` klasöründe `.gitkeep` adında bir dosya oluşturun:

![event](assets/21.webp)


- Değişiklikleri ilet...` düğmesine tıklayın:

![event](assets/22.webp)


- İşlem başlığını varsayılan olarak bırakın ve `Doğrudan patch-1 dalına işle` kutusunun işaretli olduğundan emin olun, ardından `Değişiklikleri işle` seçeneğine tıklayın:

![event](assets/23.webp)


- Assets` klasörüne geri dönün:

![event](assets/24.webp)


- Önce `Dosya ekle` düğmesine, ardından `Dosya yükle` düğmesine tıklayın: ![event](assets/25.webp)
- Yeni bir sayfa açılacaktır. Konferansınızı temsil eden ve PlanB Network sitesinde görüntülenecek bir görseli sürükleyip bırakın:

![event](assets/26.webp)


- Logo, bir küçük resim veya hatta bir poster olabilir:

![event](assets/27.webp)


- Görüntü yüklendikten sonra, `Doğrudan patch-1 dalına aktar` kutucuğunun işaretli olduğunu kontrol edin ve ardından `Değişiklikleri aktar` seçeneğine tıklayın:

![event](assets/28.webp)


- Dikkatli olun, resminiz `thumbnail` olarak adlandırılmalı ve `.webp` formatında olmalıdır. Bu nedenle tam dosya adı şöyle olmalıdır: `thumbnail.webp` olmalıdır:

![event](assets/29.webp)


- Assets` klasörünüze dönün ve `.gitkeep` ara dosyasına tıklayın:

![event](assets/30.webp)


- Dosyanın üzerine geldiğinizde, sağ üstteki 3 küçük noktaya ve ardından `Dosyayı sil` seçeneğine tıklayın:

![event](assets/31.webp)


- Hala aynı çalışma dalında olduğunuzu doğrulayın, ardından `Değişiklikleri ilet` düğmesine tıklayın:

![event](assets/32.webp)


- İşleminize bir başlık ve açıklama ekleyin, ardından `Değişiklikleri ilet` seçeneğine tıklayın:

![event](assets/33.webp)


- Deponuzun kök dizinine geri dönün:

![event](assets/34.webp)


- Şubenizde değişiklik yapıldığını belirten bir mesaj görmelisiniz. Karşılaştır ve çekme isteği düğmesine tıklayın:

![event](assets/35.webp)


- PR'ınıza net bir başlık ve açıklama ekleyin:

![event](assets/36.webp)


- Çekme isteği oluştur` düğmesine tıklayın:

![event](assets/37.webp)

Tebrikler! Halkla İlişkileriniz başarıyla oluşturuldu. Şimdi bir yönetici bunu kontrol edecek ve her şey yolundaysa PlanB Network'ün ana havuzuyla birleştirecektir. Etkinliğinizin birkaç gün sonra web sitesinde göründüğünü göreceksiniz.


Halkla ilişkilerinizin ilerleyişini takip ettiğinizden emin olun. Bir yönetici ek bilgi isteyen bir yorum bırakabilir. PR'niz onaylanmadığı sürece, PlanB Network GitHub deposundaki `Pull requests` sekmesinde ona danışabilirsiniz:

![event](assets/38.webp)

Değerli katkılarınız için çok teşekkür ederiz! :)