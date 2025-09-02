---
name: Katkı - GitHub Desktop ile Öğretici (Orta Düzey)
description: GitHub Desktop kullanarak Plan ₿ Network'da bir öğretici önermek için eksiksiz kılavuz
---
![cover](assets/cover.webp)


Yeni bir öğretici eklemeye ilişkin bu öğreticiyi takip etmeden önce, bazı ön adımları tamamlamış olmanız gerekir. Henüz yapmadıysanız, sizi önce bu giriş eğitimine bakmaya ve ardından buraya geri dönmeye davet ediyorum:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Zaten var:


- Eğitiminizin temasını seçin;
- Plan ₿ Network ekibiyle [Telegram grubu] (https://t.me/PlanBNetwork_ContentBuilder) veya paolo@planb.network üzerinden iletişime geçin;
- Katkı araçlarınızı seçin.


Bu eğitimde, GitHub Desktop ile yerel ortamınızı kurarak Plan ₿ Network'ye eğitiminizi nasıl ekleyeceğinizi göreceğiz. Git konusunda zaten yetkinseniz, bu çok ayrıntılı eğitim sizin için gerekli olmayabilir. Bunun yerine, ayrıntılı adım adım rehberlik olmadan yalnızca ana yönergeleri sunduğum bu diğer öğreticiye başvurmanızı tavsiye ederim:



- Deneyimli kullanıcılar**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Yerel ortamınızı kurmayı tercih etmiyorsanız, değişiklikleri doğrudan GitHub'ın web Interface'ü üzerinden yaptığımız, yeni başlayanlar için tasarlanmış bu diğer öğreticiyi izleyin:



- Yeni Başlayanlar (web Interface)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Ön Koşullar


Bu öğreticiyi takip etmek için gerekli yazılım:



- [GitHub Desktop](https://desktop.github.com/);
- Obsidian](https://obsidian.md/) gibi bir markdown dosya editörü;
- Bir kod düzenleyici ([VSC](https://code.visualstudio.com/) veya [Sublime Text](https://www.sublimetext.com/)).


![TUTO](assets/fr/01.webp)


Eğitime başlamadan önce önkoşullar:



- Bir [GitHub hesabına] sahip olun (https://github.com/signup);
- Fork kaynak deposunun] (https://github.com/PlanB-Network/Bitcoin-educational-content) bir Plan ₿ Network'ine sahip olun;
- Plan ₿ Network'de bir profesör profiline sahip olun] (https://planb.network/professors) (yalnızca tam bir eğitim öneriyorsanız).


Bu önkoşulları elde etmek için yardıma ihtiyacınız varsa, diğer eğitimlerim size yardımcı olacaktır:



Her şey yerli yerine oturduğunda ve yerel ortamınız Plan ₿ Network'un kendi Fork'unuzla düzgün bir şekilde ayarlandığında, öğreticiyi eklemeye başlayabilirsiniz.


## 1 - Yeni bir şube oluşturun


Tarayıcınızı açın ve Fork deposunun Plan ₿ Network sayfasına gidin. Bu, GitHub'da oluşturduğunuz Fork'tür. Fork'ünüzün URL'si aşağıdaki gibi görünmelidir: `https://github.com/[kullanıcı adınız]/Bitcoin-educational-content`:


![TUTO](assets/fr/03.webp)


Ana dal `dev` üzerinde olduğunuzdan emin olun ve ardından `Sync Fork` düğmesine tıklayın. Fork'ünüz güncel değilse, GitHub dalınızı güncellemeyi teklif edecektir. Bu güncelleme ile devam edin. Aksine, dalınız zaten güncelse, GitHub sizi bilgilendirecektir:


![TUTO](assets/fr/04.webp)


GitHub Desktop yazılımını açın ve pencerenin sol üst köşesinde Fork'inizin doğru seçildiğinden emin olun:


![TUTO](assets/fr/05.webp)


Kaynağı getir` düğmesine tıklayın. Yerel deponuz zaten güncelse, GitHub Desktop herhangi bir ek işlem önermeyecektir. Aksi takdirde, `Köken çek` seçeneği görünecektir. Yerel deponuzu güncellemek için bu düğmeye tıklayın:


![TUTO](assets/fr/06.webp)


Gerçekten `dev` ana dalında olduğunuzu doğrulayın:


![TUTO](assets/fr/07.webp)


Bu şubeye tıklayın, ardından `Yeni Şube` düğmesine tıklayın:


![TUTO](assets/fr/08.webp)


Yeni dalın `PlanB-Network/Bitcoin-educational-content` adlı kaynak depoyu temel aldığından emin olun.


Branşınızı, her kelimeyi ayırmak için tire kullanarak, başlığın amacı hakkında net olacak şekilde adlandırın. Örneğin, amacımızın Sparrow wallet yazılımının kullanımı hakkında bir eğitim yazmak olduğunu varsayalım. Bu durumda, bu öğreticiyi yazmaya adanmış çalışma dalı şöyle adlandırılabilir: `tuto-Sparrow-Wallet-loic`. Uygun isim girildikten sonra, dalın oluşturulmasını onaylamak için `Dal oluştur`a tıklayın:


![TUTO](assets/fr/09.webp)


Şimdi yeni çalışma dalınızı GitHub'daki çevrimiçi Fork'nize kaydetmek için `Dalı yayınla` düğmesine tıklayın:

![TUTORIAL](assets/fr/10.webp)

Şimdi, GitHub Desktop'ta kendinizi yeni dalınızda bulmalısınız. Bu, bilgisayarınızda yerel olarak yapılan tüm değişikliklerin yalnızca bu dala kaydedileceği anlamına gelir. Ayrıca, GitHub Masaüstünde bu dal seçili kaldığı sürece, makinenizde yerel olarak görünen dosyalar, ana dalın (`dev`) değil, bu dalın (`tuto-Sparrow-Wallet-loic`) dosyalarına karşılık gelir.


![TUTORIAL](assets/fr/11.webp)


Yayınlamak istediğiniz her yeni makale için `dev`den yeni bir dal oluşturmanız gerekecektir. Git'teki bir dal, projenin paralel bir sürümüdür ve çalışma birleştirilmeye hazır olana kadar ana dalı etkilemeden değişiklik yapmanıza olanak tanır.


## 2 - Eğitim dosyalarının eklenmesi


Artık çalışma dalı oluşturulduğuna göre, yeni öğreticinizi entegre etme zamanı geldi. İki seçeneğiniz var: gerekli belgelerin oluşturulmasını otomatikleştiren Python betiğimi kullanın veya her dosyayı manuel olarak oluşturun. Her seçenek için izlenecek adımlara bakacağız.


### Python betiğim ile


Makinenize yüklemeniz gerekir:


- Python 3.8 veya üstü.


Komut dosyasını kullanmak için, depolandığı klasöre gidin. Kod, Plan ₿ Network veri havuzunda şu yolda bulunur: `Bitcoin-educational-content/scripts/tutorial-related/data-creator`.


Klasöre girdikten sonra bağımlılıkları yükleyin:


```
pip install -r requirements.txt
```


Ardından yazılımı şu komutla başlatın:


```
python3 main.py
```


Grafiksel bir kullanıcı Interface (GUI) açılacaktır. İlk seferde gerekli tüm bilgileri girmeniz gerekecektir, ancak sonraki kullanımlarda komut dosyası kişisel bilgilerinizi hatırlayacak, böylece tekrar girmeniz gerekmeyecektir.


![DATA-CREATOR-PY](assets/fr/37.webp)


Klonlanmış deponuzdaki `/tutorials` klasörünün yerel yolunu girerek başlayın (`.../Bitcoin-educational-content/tutorials/`). Manuel olarak girebilir veya dosya gezgininizi kullanarak gezinmek için "Gözat" düğmesine tıklayabilirsiniz.


![DATA-CREATOR-PY](assets/fr/38.webp)


Eğitiminizi hangi dilde yazacağınızı seçin.


![DATA-CREATOR-PY](assets/fr/39.webp)


"Contributor's GitHub ID" alanına GitHub kullanıcı adınızı girin.


![DATA-CREATOR-PY](assets/fr/40.webp)


Ardından, profesör profilinizi doldurmanız gerekir. Kullanabileceğiniz birkaç seçenek vardır:


- "Profesör Adı" alanına adınızın ilk harflerini girin. Adınız daha sonra aşağıdaki "Prof. Önerileri" açılır listesinde görünecektir. Üzerine tıklayarak seçin;
- Alternatif olarak, doğrudan "Prof. Önerileri" açılır listesine tıklayabilir ve profesörünüzün adını seçebilirsiniz.


Bu eylem, profesörünüzün UUID'sini ilgili alana otomatik olarak dolduracaktır.



![DATA-CREATOR-PY](assets/fr/41.webp)


Henüz bir profesör profiliniz yoksa, bu eğitime göz atın:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Ardından "Yeni Eğitim" düğmesine tıklayın.


![DATA-CREATOR-PY](assets/fr/42.webp)


Eğitiminiz için bir ana kategori seçin. Ardından, seçtiğiniz ana kategoriye göre ilgili bir alt kategori seçin.


![DATA-CREATOR-PY](assets/fr/43.webp)


Eğitimin zorluk seviyesini belirleyin.


![DATA-CREATOR-PY](assets/fr/44.webp)


Eğitiminiz için özel olarak oluşturulan dizin için bir ad seçin. Bu klasörün adı, kelimeleri ayırmak için kısa çizgiler kullanarak eğitimde ele alınan yazılımı yansıtmalıdır. Örneğin, klasörün adı `red-Wallet` olabilir:


![DATA-CREATOR-PY](assets/fr/45.webp)


Proje_id`, [projeler listesinde] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) bulunan, eğitimde ele alınan aracın arkasındaki şirket veya kuruluşun UUID'sidir. Örneğin, Sparrow wallet ile ilgili bir eğitim için `project_id` dosyasını dosyada bulabilirsiniz: `Bitcoin-educational-content/resources/projects/Sparrow/project.yml`. Bu bilgi öğreticinizin YAML dosyasına eklenir çünkü Plan ₿ Network, Bitcoin veya ilgili projelerde aktif olan şirket ve kuruluşların bir veritabanını tutar. İlişkili `project_id` bilgisini ekleyerek içeriğinizi ilgili varlığa bağlamış olursunuz.


***Güncelleme:*** Komut dosyasının yeni sürümünde, artık `proje_id`yi manuel olarak girmenize gerek yoktur. Projeyi adına göre bulmak ve ilgili `project_id`yi otomatik olarak almak için bir arama işlevi eklendi. Aramak için "Proje Adı" alanına proje adının baş harfini yazın, ardından açılır menüden istediğiniz şirketi seçin. Proje_id`si aşağıdaki alana otomatik olarak doldurulacaktır. Gerekirse manuel olarak da girebilirsiniz.


![DATA-CREATOR-PY](assets/fr/46.webp)


Etiketler için, yalnızca [Plan ₿ Network etiket listesinden] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) seçerek eğitim içeriğinizle ilgili 2 veya 3 anahtar kelime seçin. Yazılım ayrıca açılır listeli bir anahtar kelime arama işlevi de sağlar.


![DATA-CREATOR-PY](assets/fr/47.webp)


Tüm bilgiler girildikten ve doğrulandıktan sonra, eğitim dosyalarınızın oluşturulmasını onaylamak için "Eğitim Oluştur" düğmesine tıklayın. Bu, eğitim klasörünüzü ve seçilen kategorideki gerekli tüm dosyaları yerel olarak generate yapacaktır.


![DATA-CREATOR-PY](assets/fr/48.webp)


Artık "Python betiğim olmadan" alt bölümünü ve 3. adım olan "YAML dosyasını doldurun" kısmını atlayabilirsiniz, çünkü betik bu işlemleri sizin için zaten tamamlamıştır. Doğrudan 4. adıma geçin ve öğreticinizi yazmaya başlayın.


Bu Python betiği hakkında daha fazla bilgi için [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md) adresine de göz atabilirsiniz.


### Python betiğim olmadan


Dosya yöneticinizi açın ve deponuzun yerel klonunu temsil eden `Bitcoin-educational-content` klasörüne gidin. Bu klasörü genellikle `Documents\GitHub\Bitcoin-educational-content` altında bulmanız gerekir.


Bu dizin içinde, öğreticinizi yerleştirmek için uygun alt klasörü bulmanız gerekecektir. Klasör organizasyonu Plan ₿ Network web sitesinin farklı bölümlerini yansıtmaktadır. Örneğimizde, Sparrow wallet hakkında bir eğitim eklemek istediğimizden, aşağıdaki yola gitmeliyiz: `Bitcoin-educational-content\tutorials\Wallet`, bu da web sitesindeki `Wallet` bölümüne karşılık gelir:


![TUTO](assets/fr/12.webp)


Wallet` klasörü içinde, özellikle eğitiminiz için ayrılmış yeni bir dizin oluşturmanız gerekir. Bu klasörün adı eğitimde ele alınan yazılımı çağrıştırmalı ve kelimeleri tire ile birleştirdiğinizden emin olmalısınız. Benim örneğim için klasörün adı `Sparrow-Wallet` olacak:


![TUTO](assets/fr/13.webp)


Öğreticinize ayrılmış bu yeni alt klasöre birkaç Elements eklenmesi gerekiyor:


- Eğitiminiz için gerekli tüm illüstrasyonları almak üzere bir `assets` klasörü oluşturun;
- Bu `assets` klasörünün içinde, eğitimin orijinal dil koduna göre adlandırılmış bir alt klasör oluşturmanız gerekir. Örneğin, eğitim İngilizce yazılmışsa, bu alt klasör `en` olarak adlandırılmalıdır. Eğitimin tüm görsellerini buraya yerleştirin (diyagramlar, resimler, ekran görüntüleri, vb.).
- Öğreticinizle ilgili ayrıntıları kaydetmek için bir `tutorial.yml` dosyası oluşturulmalıdır;
- Eğitiminizin asıl içeriğini yazmak için markdown formatında bir dosya oluşturulacaktır. Bu dosya yazının dil koduna göre adlandırılmalıdır. Örneğin, Fransızca yazılmış bir öğretici için dosya `fr.md` olarak adlandırılmalıdır.


![TUTO](assets/fr/14.webp)


Özetlemek gerekirse, oluşturulacak dosyaların hiyerarşisi şöyledir:


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```


## 3 - YAML dosyasını doldurun


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


Öğretici.yml` dosyanızı değiştirmeyi tamamladığınızda, `Dosya > Kaydet` seçeneğine tıklayarak belgenizi kaydedin:


![TUTO](assets/fr/16.webp)


Artık kod düzenleyicinizi kapatabilirsiniz.


## 4 - Markdown Dosyasını Doldurun


Şimdi, öğreticinizi barındıracak olan ve `fr.md` gibi dilinizin koduyla adlandırılmış dosyanızı açabilirsiniz. Obsidian'a gidin, pencerenin sol tarafında, öğreticinizin klasörünü ve aradığınız dosyayı bulana kadar klasör ağacında ilerleyin:


![TUTO](assets/fr/18.webp)


Dosyayı açmak için üzerine tıklayın:


![TUTO](assets/fr/19.webp)


Belgenin üst kısmındaki `Özellikler` bölümünü doldurarak başlayacağız.


![TUTO](assets/fr/20.webp)


Aşağıdaki kod bloğunu manuel olarak ekleyin ve doldurun:


```
---
name: [Title]
description: [Description]
---
```


![TUTO](assets/fr/21.webp)


Eğitiminizin adını ve kısa bir açıklamasını girin:


![TUTO](assets/fr/22.webp)


Ardından, öğreticinizin başına kapak resminin yolunu ekleyin. Bunu yapmak için, not edin:


```
![cover-sparrow](assets/cover.webp)
```


Bu sözdizimi, öğreticinize bir resim eklemek gerektiğinde faydalı olacaktır. Ünlem işareti, parantezler arasında belirtilen alternatif metin (alt) ile birlikte bunun bir resim olduğunu gösterir. Görüntünün yolu parantezler arasında belirtilir:


![TUTO](assets/fr/23.webp)


## 5 - Logo ve Kapağı Ekleyin


Assets` klasörüne, makaleniz için küçük resim görevi görecek `logo.webp` adlı bir dosya eklemelisiniz. Bu görüntü `.webp` formatında olmalı ve kullanıcı Interface ile uyumlu olması için kare boyutuna uymalıdır. Eğitimde ele alınan yazılımın logosunu veya haklardan muaf olması koşuluyla ilgili herhangi bir görseli seçmekte özgürsünüz. Ayrıca, aynı yere `cover.webp` başlıklı bir resim de ekleyin. Bu görüntü eğitiminizin en üstünde görüntülenecektir. Bu görselin de logo gibi kullanım haklarına saygı gösterdiğinden ve eğitiminizin bağlamına uygun olduğundan emin olun:

## 6 - Öğreticinin Yazılması ve Görsellerin Eklenmesi


İçeriğinizi hazırlayarak öğreticinizi yazmaya devam edin. Bir altyazı eklemek istediğinizde, metnin önüne `##` ekleyerek uygun markdown biçimlendirmesini uygulayın:


![TUTO](assets/fr/24.webp)


Assets` klasöründeki dil alt klasörü, eğitiminize eşlik edecek diyagramları ve görselleri saklamak için kullanılır. İçeriğinizi uluslararası bir kitle için erişilebilir kılmak amacıyla görsellerinize metin eklemekten mümkün olduğunca kaçının. Elbette, sunulan yazılım metin içerecektir, ancak yazılım ekran görüntülerine diyagramlar veya ek göstergeler eklerseniz, bunu metin olmadan yapın veya zorunlu olduğu kanıtlanırsa İngilizce kullanın.


![TUTO](assets/fr/25.webp)


Resimlerinizi adlandırmak için, öğreticideki görünüm sıralarına karşılık gelen numaraları iki basamaklı (veya öğreticiniz 99'dan fazla resim içeriyorsa üç basamaklı) olarak biçimlendirilmiş şekilde kullanın. Örneğin, ilk resminizi `01.webp`, ikincisini `02.webp` olarak adlandırın ve bu şekilde devam edin.


Resimleriniz yalnızca `.webp` formatında olmalıdır. Gerekirse, [görüntü dönüştürme yazılımımı] (https://github.com/LoicPandul/ImagesConverter) kullanabilirsiniz.


![TUTO](assets/fr/26.webp)


Belgenize bir diyagram eklemek için aşağıdaki Markdown komutunu kullanın ve uygun alternatif metnin yanı sıra görüntünün doğru yolunu belirttiğinizden emin olun:


```
![sparrow](assets/fr/01.webp)
```


Baştaki ünlem işareti bunun bir resim olduğunu gösterir. Erişilebilirlik ve SEO'ya yardımcı olan alternatif metin parantezler arasına yerleştirilir. Son olarak, görsele giden yol parantezler arasında belirtilir.


Kendi diyagramlarınızı oluşturmak isterseniz, görsel tutarlılığı sağlamak için Plan ₿ Network'in grafik tüzüğüne uyduğunuzdan emin olun:


- Yazı tipi**: IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans) kullanın;
- Renkler**:
 - Turuncu: #FF5C00
 - Siyah: #000000
 - Beyaz: #FFFFFF


**Eğitimlerinize entegre edilen tüm görsellerin haklardan muaf olması veya kaynak dosyanın lisansına uyması zorunludur**. Ayrıca, Plan ₿ Network'da yayınlanan tüm diyagramlar, metinle aynı şekilde CC-BY-SA lisansı altında kullanıma sunulmaktadır.

**-> İpucu:** Görüntüler gibi dosyaları herkese açık olarak paylaşırken, gereksiz meta verileri kaldırmak önemlidir. Bunlar konum verileri, oluşturma tarihleri veya yazarla ilgili ayrıntılar gibi hassas bilgiler içerebilir. Gizliliğinizi korumak için bu meta verileri silmeniz önerilir. Bu işlemi basitleştirmek için, bir belgenin meta verilerinin basit bir sürükle-bırak yöntemiyle temizlenmesini sağlayan [Exif Cleaner] (https://exifcleaner.com/) gibi özel araçları kullanabilirsiniz.

## 7 - Eğitimi Kaydedin ve Gönderin


Eğitiminizi istediğiniz dilde yazmayı tamamladıktan sonra, bir sonraki adım bir **Çekme Talebi** göndermektir. Daha sonra yönetici, insan incelemeli otomatik çeviri yöntemimiz sayesinde eğitiminizin eksik çevirilerini eklemekle ilgilenecektir.


Çekme İsteğine devam etmek için GitHub Masaüstü yazılımını açın. Yazılım, orijinal depoya kıyasla dalınızda yerel olarak yaptığınız değişiklikleri otomatik olarak algılamalıdır. Devam etmeden önce, Interface'nin sol tarafında bu değişikliklerin beklediğinizle eşleşip eşleşmediğini dikkatlice kontrol edin:


![TUTO](assets/fr/28.webp)


İşleminiz için bir başlık ekleyin, ardından bu değişiklikleri doğrulamak için mavi `Commit to [your branch]` düğmesine tıklayın:


![TUTO](assets/fr/29.webp)


Bir commit, bir projenin zaman içindeki gelişimini takip etmeyi sağlayan açıklayıcı bir mesajla birlikte dalda yapılan değişikliklerin kaydedilmesidir. Bir çeşit ara kontrol noktasıdır.


Ardından `Push origin` düğmesine tıklayın. Bu, işleminizi Fork'inize gönderecektir:


![TUTO](assets/fr/30.webp)


Öğreticinizi bitirmediyseniz, daha sonra geri dönebilir ve yeni taahhütler yapabilirsiniz. Bu dal için değişikliklerinizi tamamladıysanız, şimdi `Preview Pull Request` düğmesine tıklayın:


![TUTO](assets/fr/31.webp)


Yaptığınız değişikliklerin doğru olup olmadığını son bir kez kontrol edebilir ve ardından `Çekme isteği oluştur` düğmesine tıklayabilirsiniz:


![TUTO](assets/fr/32.webp)


Çekme İsteği, şubenizdeki değişiklikleri Plan ₿ Network deposunun ana şubesine entegre etmek için yapılan bir taleptir ve bu da değişikliklerin birleştirilmeden önce gözden geçirilmesine ve tartışılmasına olanak tanır.


GitHub'daki tarayıcınıza otomatik olarak Çekme İsteğinizin hazırlık sayfasına yönlendirileceksiniz:


![TUTO](assets/fr/33.webp)

Kaynak deposu ile birleştirmek istediğiniz değişiklikleri kısaca özetleyen bir başlık belirtin. Bu değişiklikleri açıklayan kısa bir yorum ekleyin (öğreticinizin oluşturulmasıyla ilişkili bir sorun numaranız varsa, yorumda `Closes #{issue number}` yazmayı unutmayın), ardından birleştirme isteğini onaylamak için Green `Create pull request` düğmesine tıklayın:

![TUTO](assets/fr/34.webp)


PR'niz daha sonra ana Plan ₿ Network deposunun `Pull Request` sekmesinde görünür olacaktır. Tek yapmanız gereken, bir yöneticinin katkınızın birleştirilmesini onaylamak veya herhangi bir ek değişiklik talep etmek için sizinle iletişime geçmesini beklemektir.


![TUTO](assets/fr/35.webp)


PR'niz ana dal ile birleştirildikten sonra, Fork'ünüzde temiz bir geçmiş sağlamak için çalışma dalınızı (`tuto-Sparrow-Wallet`) silmeniz önerilir. GitHub, PR sayfanızda bu seçeneği size otomatik olarak sunacaktır:


![TUTO](assets/fr/36.webp)


GitHub Masaüstü yazılımında, Fork'inizin ana dalına (`dev`) geri dönebilirsiniz.


![TUTO](assets/fr/07.webp)


PR'nizi gönderdikten sonra katkınızda değişiklik yapmak isterseniz, prosedür PR'nizin mevcut durumuna bağlıdır:


- PR'niz hala açıksa ve henüz birleştirilmediyse, aynı dalda kalarak değişiklikleri yerel olarak yapın. Değişiklikler tamamlandığında, hala açık olan PR'nize yeni bir commit eklemek için `Push origin` düğmesini kullanın;
- PR'niz zaten ana dal ile birleştirildiyse, yeni bir dal oluşturarak ve ardından yeni bir PR göndererek süreci baştan başlatmanız gerekecektir. Devam etmeden önce yerel deponuzun Plan ₿ Network kaynak deposu ile senkronize olduğundan emin olun.


Eğitiminizi gönderirken teknik zorluklarla karşılaşırsanız, [katkılar için özel Telegram grubumuz] (https://t.me/PlanBNetwork_ContentBuilder) üzerinden yardım istemekten çekinmeyin. Teşekkürler!