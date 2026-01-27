---
name: Breez - POS
description: Breez, işletmeniz için bitcoin ödemelerini toplamayı kolaylaştırır.
---

![cover](assets/cover.webp)



COVID-19 salgınından bu yana, temassız dijital ödemeler en küçük mağazalarda bile yaygınlaştı. Bu süre zarfında birçok işletme, dünyanın her yerinden ödeme almalarını sağlayan bitcoin cash çözümlerinin pratikliğini keşfetti. Ancak bu çözümlerin kullanımı bazen zor veya küçük işletmeler için uygun olmayabiliyor. Bu eğitimde, bitcoinlerinizin yönetimi üzerinde size tam kontrol sağlarken kullanım kolaylığı ile öne çıkan bir çözüm olan Breez ödeme terminaline bir göz atacağız.



## Breez POS'u yükleyin



Breez POS, Breez wallet tarafından sağlanan bir kendi kendine saklama hizmetidir. Bu hizmetin faydası, tüccarların çeşitli Lightning cüzdanlarına çok benzeyen basit bir arayüzde kalırken Bitcoin aracılığıyla ödeme toplamalarını sağlamaktır. Breez POS [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) ve [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS) indirme platformlarında mevcuttur.



![download](assets/fr/01.webp)



![setup](assets/fr/12.webp)



⚠️ Bu uygulamaların hala geliştirilme aşamasında olduğunu ve işlevlerin kullanımında bazı hatalar olabileceğini unutmamak önemlidir. Ölçülü kullanım öneriyoruz.



Bu uygulama ile Breez, bitcoinlerinizi yönetme konusundaki egemenliğinizi garanti ederken, ağ yapılandırmaları ve ücret ayarları üzerinde tam kontrol sağlar.



Aşağıdaki eğitimimizi takip ederek çeşitli Breez wallet seçeneklerini keşfedebilirsiniz. Bu adım, satış noktası ekosistemini daha iyi anlamanıza ve seed'ünüzle ilişkili bitcoinleri etkili bir şekilde güvence altına almak için en iyi uygulamaları benimsemenize yardımcı olacaktır.



https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Breez POS'u Kullanma



Bu eğitimde, işletmenize bir ödeme aracı olarak nasıl entegre edeceğinizi anlamanıza yardımcı olmak için "*Satış Noktası*" bölümüne odaklanacağız.



Satış noktası Breez portföyünün ayrılmaz bir parçasıdır ve ödemeleri toplamak için öncelikle Lightning Network'e dayanır.



"*Point of Sale*" menüsünde, ödemeleri toplamak için doğrudan bir arayüze sahipsiniz. İki bölüme ayrılmıştır:



### Otomatik ödeme



İlk bölüm otomatik ödeme klavyesidir. Bu arayüz, müşterinizin toplam satın alımlarını bildiğinizde veya işletmenizde sabit bir ürün kataloğuna ihtiyaç duymadığınızda (örneğin, serbest hizmetler) bir ödemenin tamamını tahsil etmek için kullanışlıdır.



![keyboard](assets/fr/02.webp)



Breez POS'u ilk kez kullanmak için 2.500 satoshiden (bugünkü kurla yaklaşık 3 avro) fazla bir ödeme almanız gerekir. Yalnızca ilk nakit çıkışınızda ödenen bu tutar, diğer Lightning Network düğümleriyle iletişim kurabilmeniz ve satoshi gönderip alabilmeniz için bir ödeme kanalı oluşturma maliyetini temsil eder.



![channel_fee](assets/fr/03.webp)


### Ürün kataloğu



İkinci bölüm ürün kataloğudur. Bu arayüz, önceden tanımlanmış fiyatlara sahip bir ürün kataloğunuz olduğunda idealdir. Burada ürünlerinizi önceden yapılandırabilir ve ardından nakit makbuzlarınızın izlenebilirliğini artırmak için bunları generate faturalarında kullanabilirsiniz.



![items](assets/fr/04.webp)



Bu arayüzden "**Plus**" düğmesine tıklayarak ve ardından bu kalem için ad, fiyat ve bir tanımlayıcı tanımlayarak her bir kalemi manuel olarak yapılandırabilirsiniz.



![add_items](assets/fr/05.webp)



Daha sonra ekleyebilir ve ilgili ödemeyi tahsil etmek için miktarını tanımlayabilirsiniz.



Kataloğunuz oldukça büyük olduğunda, ürünlerinizi tek tek eklemek karmaşık hale gelebilir. Bu amaçla, **Tercihler > Satış Noktası Ayarları** bölümünde, "Ürün listesi" menüsünden, ürün listenizi CSV dosyalarından otomatik olarak içe ve dışa aktarabilirsiniz.



![import](assets/fr/07.webp)



Aynı bölümde, Lightning faturalarınızın geçerlilik süresini tanımlayabilirsiniz. Şu andan itibaren, tüm faturalarınız için müşterilerinizin ödemelerini yapmak için `N` saniyeleri vardır, aksi takdirde yeni bir Lightning faturası oluşturmanız gerekecektir.



![invoice_time](assets/fr/08.webp)



Bir yönetici olarak, wallet'nizden giden tüm ödemeler için gerekli olacak bir şifre ekleyerek bitcoinlerinizin güvenliğini güçlendirebilirsiniz. Bu özellik, çıkışınızı yöneten tek kişi siz olmadığınızda özellikle kullanışlıdır.



![manager](assets/fr/09.webp)



İşlemler** menüsünde, tahsil ettiğiniz tüm ödemelerin bir listesini bulacaksınız. Ayrıca **Takvim** düğmesine tıklayarak sonuçları belirli bir döneme göre filtreleyebilirsiniz.



![transactions](assets/fr/10.webp)



Ayrıca **Belge** düğmesine tıklayarak satışlarınızın günlük özetini ve toplanan toplam tutarı görüntüleyebilirsiniz.



![summary](assets/fr/11.webp)



Artık Bitcoin'in işletmenize sorunsuz entegrasyonu için Breez uygulaması tarafından sunulan satış noktasını tam olarak kavradınız. Bu eğitimi faydalı bulduysanız, bitcoin ile ödeme almanızı ve işletmenizden para kazanmanızı sağlayan bir e-ticaret platformu olan be-BOP hakkındaki eğitimimizi öneririz.



https://planb.academy/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa