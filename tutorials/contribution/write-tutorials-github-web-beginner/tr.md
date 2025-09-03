---
name: Katkı - GitHub Web eğitimi (başlangıç)
description: GitHub Web ile Plan ₿ Network eğitimleri için eksiksiz kılavuz
---
![cover](assets/cover.webp)


Yeni bir öğretici eklemeye ilişkin bu öğreticiyi takip etmeden önce, birkaç ön adımı tamamlamış olmanız gerekir. Henüz yapmadıysanız, lütfen önce bu giriş eğitimine bir göz atın, ardından buraya geri dönün:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Sende zaten var:




- Eğitiminiz için bir tema seçin;
- Plan ₿ Network ekibiyle [Telegram grubu] (https://t.me/PlanBNetwork_ContentBuilder) veya paolo@planb.network üzerinden iletişime geçin;
- Katkı araçlarınızı seçin.


Bu eğitimde, GitHub'ın web sürümünü kullanarak eğitiminizi Plan ₿ Network'ye nasıl ekleyeceğinizi inceleyeceğiz. Git'te zaten ustalaştıysanız, bu çok ayrıntılı eğitim sizin için gerekli olmayabilir. Bunun yerine, izlenecek yönergeleri ve yerel bir:




- Deneyimli kullanıcılar**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410


- Orta Düzey (GitHub Masaüstü)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Ön Koşullar


Eğitime başlamadan önce önkoşullar:




- Bir [GitHub hesabına] sahip olun (https://github.com/signup);
- Plan ₿ Network kaynak deposunun] (https://github.com/PlanB-Network/Bitcoin-educational-content) bir Fork'ine sahip olun;
- Plan ₿ Network'da bir öğretmen profiline sahip olun] (https://planb.network/professors) (yalnızca tam bir eğitim sunuyorsanız).


Bu önkoşulları sağlamak için yardıma ihtiyacınız varsa, diğer eğitimlerim size yardımcı olacaktır:



https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Her şey yerine oturduğunda ve Fork deposunun Plan ₿ Network'sine sahip olduğunuzda, öğreticiyi eklemeye başlayabilirsiniz.


## 1 - Yeni bir şube oluşturun


Tarayıcınızı açın ve Plan ₿ Network deposundaki Fork sayfanıza gidin. Bu, GitHub'da oluşturduğunuz Fork'dir. Fork'inizin URL'si aşağıdaki gibi görünmelidir: `https://github.com/[your-username]/Bitcoin-educational-content`:


![GITHUB](assets/fr/01.webp)


Ana `dev' dalında olduğunuzdan emin olun, ardından "*Sync Fork*" düğmesine tıklayın. Eğer Fork'niz güncel değilse, GitHub sizden dalınızı güncellemenizi isteyecektir. Bu güncelleme ile devam edin:


![GITHUB](assets/fr/02.webp)


Dev' dalına tıklayın, ardından çalışma dalınızı, başlığını amacını açıkça yansıtacak şekilde, kelimeleri ayırmak için tire kullanarak adlandırın. Örneğin, amacımız Green Wallet kullanımı hakkında bir eğitim yazmaksa, dalın adı şöyle olabilir: `tuto-Green-Wallet-loic`. Uygun bir isim girdikten sonra, `dev` temelinde yeni şubenizin oluşturulmasını onaylamak için "*Şube oluştur*" seçeneğine tıklayın:


![GITHUB](assets/fr/03.webp)


Şimdi yeni iş kolunuzda olmalısınız:


![GITHUB](assets/fr/04.webp)


Bu, yaptığınız tüm değişikliklerin yalnızca söz konusu dala kaydedileceği anlamına gelir.


Yayınlamayı planladığınız her yeni makale için `dev`den yeni bir dal oluşturun.


Git'teki bir dal, projenin paralel bir sürümünü temsil eder ve çalışmanız entegre edilmeye hazır olana kadar ana dalı etkilemeden değişiklikler üzerinde çalışmanıza olanak tanır.


## 2 - Eğitim dosyaları ekleyin


Artık çalışma dalı oluşturulduğuna göre, yeni öğreticinizi entegre etme zamanı geldi.


Branş dosyalarınız içinde, öğreticinizin yerleşimi için uygun alt klasörü bulmanız gerekecektir. Klasörlerin organizasyonu Plan ₿ Network web sitesinin farklı bölümlerini yansıtmaktadır. Örneğimizde, Green Wallet üzerine bir eğitim eklediğimiz için, aşağıdaki yola gidin: web sitesinin `Wallet` bölümüne karşılık gelen `Bitcoin-educational-content\tutorials\Wallet`:


![GITHUB](assets/fr/05.webp)


Wallet` klasöründe, özellikle eğitiminize ayrılmış yeni bir dizin oluşturun. Bu klasörün adı, kelimeleri bağlamak için kısa çizgiler kullanarak eğitimde kapsanan yazılımı açıkça belirtmelidir. Benim örneğim için klasörün adı `Green-Wallet` olacak. "*Dosya Ekle*" ve ardından "*Yeni dosya oluştur*" üzerine tıklayın:


![GITHUB](assets/fr/06.webp)


Klasör olarak oluşturulmasını onaylamak için klasör adını ve ardından bir eğik çizgi `/` girin.


![GITHUB](assets/fr/07.webp)


Eğitiminize adanmış bu yeni alt klasöre birkaç öğe eklemeniz gerekir:




- Eğitiminiz için gereken tüm illüstrasyonları tutmak için bir `assets` klasörü oluşturun;
- Bu `assets` klasörünün içinde, öğreticinin orijinal dil koduna göre adlandırılmış bir alt klasör oluşturun. Örneğin, eğitim İngilizce yazılmışsa, bu alt klasör `en` olarak adlandırılmalıdır. Eğitimin tüm görsellerini (diyagramlar, resimler, ekran görüntüleri, vb.) bu klasöre yerleştirin.
- Öğreticinizin ayrıntılarını kaydetmek için bir `tutorial.yml` dosyası oluşturulmalıdır;
- Öğreticinizin asıl içeriğini yazmak için bir markdown dosyası oluşturulmalıdır. Bu dosya, yazıldığı dilin koduna göre adlandırılmalıdır. Örneğin, Fransızca yazılmış bir öğretici için dosya `fr.md` olarak adlandırılmalıdır.


Özetlemek gerekirse, işte dosya hiyerarşisi (bir sonraki bölümde bunları oluşturmaya devam edeceğiz):


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```


## 3 - YAML dosyasını doldurun


YAML dosyası ile başlayalım. Yeni bir dosya oluşturmak için kutuya `tutorial.yml` yazın:


![GITHUB](assets/fr/08.webp)


Aşağıdaki şablonu kopyalayarak `tutorial.yml` dosyasını doldurun:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


İşte gerekli alanlar:



- id**: Öğreticiyi benzersiz bir şekilde tanımlayan bir UUID (_Universally Unique Identifier_). Bunu [çevrimiçi bir araç] (https://www.uuidgenerator.net/version4) kullanarak generate yapabilirsiniz. Tek gereklilik, platformdaki başka bir UUID ile çakışmayı önlemek için bu UUID'nin rastgele olmasıdır;



- project_id**: Eğitimde sunulan aracın arkasındaki şirket veya kuruluşun UUID'si [proje listesinden] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Örneğin, Green Wallet yazılımı hakkında bir eğitim oluşturuyorsanız, bu `project_id`yi aşağıdaki dosyada bulabilirsiniz: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Bu bilgi öğreticinizin YAML dosyasına eklenir çünkü Plan ₿ Network, Bitcoin veya ilgili projeler üzerinde faaliyet gösteren tüm şirket ve kuruluşların bir veritabanını tutar. Öğreticinize bağlı varlığın `project_id` bilgisini ekleyerek, iki Elements arasında bir bağlantı oluşturursunuz;



- etiketler**: özel olarak [Plan ₿ Network etiket listesinden] seçilen, eğitim içeriğiyle ilgili 2 veya 3 anahtar kelime (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- kategori**: Plan ₿ Network web sitesi yapısına göre öğretici içeriğe karşılık gelen alt kategori (örneğin, cüzdanlar için: `masaüstü`, `donanım`, `mobil`, `yedekleme`);



- seviye**: Öğreticinin zorluk seviyesi, aşağıdakiler arasından seçilir:
    - `başlangıç`
    - `intermediate`
    - `gelişmiş`
    - `uzman`



- professor_id**: Profesör profilinizde] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) görüntülenen `profesör_id`niz (UUID);



- original_language**: Öğreticinin orijinal dili (örneğin, `fr`, `en`, vb.);



- redaksiyon**: Düzeltme süreci hakkında bilgi. Kendi öğreticinizi düzeltmek ilk doğrulama olarak sayıldığından ilk bölümü tamamlayın:
    - dil**: Düzeltme okumasının dil kodu (örneğin, `fr`, `en`, vb.).
    - last_contribution_date**: Günün tarihi.
    - aciliyet**: 1
    - contributor_names**: GitHub kimliğiniz.
    - ödül**: 0


Öğretmen kimliğiniz hakkında daha fazla bilgi için lütfen ilgili eğitime bakın:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


Öğretici.yml` dosyanızı değiştirmeyi tamamladığınızda, "*Değişiklikleri yap...*" düğmesine tıklayarak belgenizi kaydedin:


![GITHUB](assets/fr/09.webp)


Bir başlık ve açıklama ekleyin ve işlemin bu eğitimin başında oluşturduğunuz dala yapıldığından emin olun. Ardından "*Değişiklikleri işle*" seçeneğine tıklayarak onaylayın.


![GITHUB](assets/fr/10.webp)


## 4 - Görüntüler için alt klasörler oluşturma


Tekrar "*Dosya Ekle*" üzerine ve ardından "*Yeni dosya oluştur*" üzerine tıklayın:


![GITHUB](assets/fr/11.webp)


Klasörü oluşturmak için `assets` ve ardından bir eğik çizgi `/` girin:


![GITHUB](assets/fr/12.webp)


Dil alt klasörünü oluşturmak için bu adımı `/assets` klasöründe tekrarlayın, örneğin eğitiminiz Fransızca ise `fr`:


![GITHUB](assets/fr/13.webp)


Bu klasörde, GitHub'ı klasörünüzü tutmaya zorlamak için sahte bir dosya oluşturun (aksi takdirde boş olacaktır). Bu dosyaya `.gitkeep` adını verin. Ardından "*Commit changes...*" seçeneğine tıklayın.


![GITHUB](assets/fr/14.webp)


Doğru dalda olduğunuzu tekrar kontrol edin ve ardından "*Değişiklikleri yap*" seçeneğine tıklayın.


![GITHUB](assets/fr/15.webp)


## 5 - Markdown dosyası oluşturma


Şimdi öğreticinizi barındıracak dosyayı oluşturacağız, dil kodunuza göre adlandıracağız, örneğin Fransızca yazıyorsak `fr.md`. Eğitim klasörünüze gidin:


![GITHUB](assets/fr/16.webp)


"Dosya ekle*" ve ardından "Yeni dosya oluştur*" üzerine tıklayın.


![GITHUB](assets/fr/17.webp)


Dosyayı dil kodunuzu kullanarak adlandırın. Benim durumumda, eğitim Fransızca yazıldığı için dosyamı `fr.md` olarak adlandırıyorum. .md` uzantısı dosyanın Markdown formatında olduğunu gösterir.


![GITHUB](assets/fr/18.webp)


Belgenin üst kısmındaki `Özellikler` bölümünü doldurarak başlıyoruz. Aşağıdaki kod bloğunu manuel olarak ekleyin ve doldurun (`name:` ve `description:` anahtarları İngilizce olarak tutulmalıdır, ancak değerleri eğitiminiz için kullanılan dilde yazılmalıdır):


```
---
name: [Titre]
description: [Description]
---
```


![GITHUB](assets/fr/19.webp)


Eğitiminizin adını ve kısa bir açıklamasını girin:


![GITHUB](assets/fr/20.webp)


Ardından öğreticinizin başındaki kapak resmine giden yolu ekleyin. Bunu yapmak için, not:


```
![cover-green](assets/cover.webp)
```


Bu sözdizimi, eğitiminize bir resim eklemeniz gerektiğinde işinize yarayacaktır. Ünlem işareti, köşeli parantezler arasında alternatif metni (alt) belirtilen bir görüntüyü gösterir. Görüntünün yolu köşeli parantezler arasında belirtilir:


![GITHUB](assets/fr/21.webp)


Bu dosyayı kaydetmek için "*Commit changes...*" düğmesine tıklayın.


![GITHUB](assets/fr/22.webp)


Doğru dalda olup olmadığınızı kontrol edin, ardından işlemi onaylayın.


![GITHUB](assets/fr/23.webp)


Dil kodunuza göre öğretici klasörünüz artık şu şekilde görünmelidir:


![GITHUB](assets/fr/24.webp)


## 6 - Logo ve kapak ekleyin


Assets` klasörüne, makaleniz için küçük resim görevi görecek `logo.webp` adlı bir dosya eklemeniz gerekir. Bu resim `.webp` formatında olmalı ve kullanıcı Interface ile eşleşmesi için kare boyutunda olmalıdır.


Telifsiz olduğu sürece eğitimde kullanılan yazılım logosunu veya ilgili herhangi bir görseli seçmekte özgürsünüz. Ayrıca, aynı yere `cover.webp` başlıklı bir resim ekleyin. Bu, eğitiminizin en üstünde görüntülenecektir. Bu görselin de logo gibi kullanım haklarına saygı gösterdiğinden ve eğitiminizin bağlamına uygun olduğundan emin olun.


Görselleri `/assets` klasörüne eklemek için yerel dosyalarınızdan sürükleyip bırakabilirsiniz. Assets` klasöründe ve doğru dalda olduğunuzdan emin olun, ardından "*Commit changes*" seçeneğine tıklayın.


![GITHUB](assets/fr/26.webp)


Şimdi görüntülerin klasörde göründüğünü görmelisiniz.


![GITHUB](assets/fr/27.webp)


## 7 - Öğreticinin yazılması


İçeriğinizi Markdown dosyasına dil koduyla not ederek öğreticinizi yazmaya devam edin (benim örneğimde, Fransızca, `fr.md` dosyası). Dosyaya gidin ve kalem simgesine tıklayın:


![GITHUB](assets/fr/28.webp)


Öğreticinizi yazmaya başlayın. Bir altyazı eklerken, metnin önüne `##` ekleyerek uygun Markdown biçimlendirmesini kullanın:


![GITHUB](assets/fr/29.webp)


Oluşturmayı daha iyi görselleştirmek için "*Edit*" ve "*Preview*" görünümleri arasında geçiş yapın.


![GITHUB](assets/fr/30.webp)


Çalışmanızı kaydetmek için "*Commit Changes...*" seçeneğine tıklayın, doğru dalda olduğunuzdan emin olun ve ardından tekrar "*Commit Changes*" seçeneğine tıklayarak onaylayın.


![GITHUB](assets/fr/31.webp)


## 8 - Görseller ekleyin


Assets` klasöründeki dil alt klasörü (benim örneğimde: `/assets/en`) eğitiminize eşlik edecek diyagramları ve görselleri saklamak için kullanılır. İçeriğinizi uluslararası bir kitle için erişilebilir kılmak amacıyla görsellerinize metin eklemekten mümkün olduğunca kaçının. Elbette, sunulan yazılım metin içerecektir, ancak yazılım ekran görüntülerine şemalar veya ek göstergeler eklerseniz, bunu metin olmadan yapın veya gerekliyse İngilizce kullanın.


Resimlerinizi adlandırmak için, öğreticideki görünüm sıralarına karşılık gelen numaraları iki basamaklı olarak biçimlendirilmiş şekilde kullanın (veya öğreticiniz 99'dan fazla resim içeriyorsa üç basamaklı). Örneğin, ilk resminizi `01.webp`, ikincisini `02.webp` olarak adlandırın ve bu şekilde devam edin.


Resimleriniz sadece `.webp` formatında olmalıdır. Gerekirse, [görüntü dönüştürme yazılımımı] (https://github.com/LoicPandul/ImagesConverter) kullanabilirsiniz.


![GITHUB](assets/fr/32.webp)


Artık resimlerinizi alt klasöre eklediğinize göre, `.gitkeep' adlı sahte dosyayı silebilirsiniz. Bu dosyayı açın, sağ üst köşedeki üç küçük noktaya ve ardından "*Dosyayı sil*" seçeneğine tıklayın.


![GITHUB](assets/fr/33.webp)


"*Değişiklikleri yap...*" seçeneğine tıklayarak değişikliklerinizi kaydedin.


![GITHUB](assets/fr/34.webp)


Alt klasörünüzdeki bir diyagramı editoryal belgenize eklemek için, uygun alternatif metni ve diliniz için doğru görüntü yolunu belirtmeye dikkat ederek aşağıdaki Markdown komutunu kullanın:


```
![green](assets/fr/01.webp)
```


Baştaki ünlem işareti bir görüntüyü belirtir. Erişilebilirliğe ve referans vermeye yardımcı olan alternatif metin köşeli parantezler arasına yerleştirilir. Son olarak, resme giden yol köşeli parantezler arasında belirtilir.


![GITHUB](assets/fr/35.webp)


Kendi şemalarınızı oluşturmak isterseniz, görsel tutarlılığı sağlamak için Plan ₿ Network grafik yönergelerini izlediğinizden emin olun:




- Yazı tipi**: IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans) kullanın;
- Renkler**:
 - Turuncu: #FF5C00
 - Siyah: #000000
 - Beyaz: #FFFFFF


**Eğitimlerinize entegre edilen tüm görsellerin telif hakkı içermemesi veya kaynak dosya lisansına uyması zorunludur**. Bu nedenle, Plan ₿ Network'te yayınlanan tüm diyagramlar, metinle aynı şekilde CC-BY-SA lisansı altında kullanıma sunulmaktadır.


**-> İpucu:** Görüntüler gibi dosyaları herkese açık olarak paylaşırken, gereksiz meta verileri kaldırmak önemlidir. Bunlar konum verileri, oluşturma tarihleri ve yazar ayrıntıları gibi hassas bilgiler içerebilir. Gizliliğinizi korumak için bu meta verileri kaldırmak iyi bir fikirdir. Bu işlemi basitleştirmek için, bir belgenin meta verilerini basit bir sürükle ve bırak ile temizlemenizi sağlayan [Exif Cleaner] (https://exifcleaner.com/) gibi özel araçları kullanabilirsiniz.


## 9 - Öğreticiyi önerin


Eğitiminizi seçtiğiniz dilde yazmayı tamamladıktan sonra, bir sonraki adım bir **Çekme Talebi** göndermektir. Daha sonra yönetici, otomatik çeviri yöntemimizi insan redaksiyonu ile kullanarak eksik çevirileri eğitiminize ekleyecektir.


Çekme İsteğine devam etmek için, tüm değişikliklerinizi kaydettikten sonra "*Katkıda bulun*" düğmesine ve ardından "*Çekme isteği aç*" düğmesine tıklayın:


![GITHUB](assets/fr/36.webp)


Çekme İsteği, dalınızdaki değişiklikleri Plan ₿ Network deposunun ana dalına entegre etmek için yapılan ve birleştirilmeden önce değişikliklerin gözden geçirilmesine ve tartışılmasına olanak tanıyan bir istektir.


Devam etmeden önce, Interface'in alt kısmında bu değişikliklerin beklediğiniz gibi olup olmadığını dikkatlice kontrol edin:


![GITHUB](assets/fr/37.webp)


Interface'nin en üstünde, çalışma dalınızın Plan ₿ Network deposunun (ana dal olan) `dev' dalıyla birleştirildiğinden emin olun.


Kaynak depoyla birleştirmek istediğiniz değişiklikleri kısaca özetleyen bir başlık girin. Bu değişiklikleri açıklayan kısa bir yorum ekleyin (öğreticinizin oluşturulmasıyla ilişkili bir sorun numaranız varsa, yorum olarak `Closes #{issue number}` notunu eklemeyi unutmayın), ardından birleştirme isteğini onaylamak için Green "*Create pull request*" düğmesine tıklayın:


![GITHUB](assets/fr/38.webp)


PR'niz daha sonra ana Plan ₿ Network deposunun "*Pull Request*" sekmesinde görünür olacaktır. Artık tek yapmanız gereken, bir yöneticinin katkınızın birleştirildiğini onaylamak veya daha fazla değişiklik talep etmek için sizinle iletişime geçmesini beklemektir.


![GITHUB](assets/fr/39.webp)


PR'nizi ana dal ile birleştirdikten sonra, Fork'nizin temiz bir geçmişini korumak için çalışma dalınızı (örneğimde: `tuto-Green-Wallet`) silmenizi öneririz. GitHub, PR sayfanızda bu seçeneği size otomatik olarak sunacaktır:


![GITHUB](assets/fr/40.webp)


PR'nizi gönderdikten sonra katkınızda değişiklik yapmak isterseniz, izlenecek adımlar PR'nizin mevcut durumuna bağlıdır:




- PR'niz hala açıksa ve henüz birleştirilmediyse, değişiklikleri aynı çalışma dalı üzerinde yapın. İşlenen değişiklikler hala açık olan PR'nize eklenecektir;
- PR'nizin ana dalla zaten birleştirilmiş olması durumunda, yeni bir dal oluşturarak ve ardından yeni bir PR göndererek işlemi baştan yapmanız gerekecektir. Devam etmeden önce Fork'ünüzün `dev' dalındaki Plan ₿ Network kaynak deposu ile senkronize olduğundan emin olun.


Öğreticinizi gönderirken teknik zorluklar yaşıyorsanız, lütfen [katkılar için özel Telegram grubumuz] (https://t.me/PlanBNetwork_ContentBuilder) üzerinden yardım istemekten çekinmeyin. Çok teşekkür ederim!