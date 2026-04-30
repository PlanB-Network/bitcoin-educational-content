---
name: Vale Bitcoin
description: Vale, gözetim dışı Lightning düğümünü cebinize getiriyor
---

![cover_valet](assets/cover.webp)



## Giriş


Valet, yeni başlayanlar için kolay ve rahat bir işe alım süreci sunan hafif, kendi kendine emanet, Bitcoin ve Lightning wallet'dir. Özellikle uzak bölgelerdeki Bitcoin topluluklarına ve döngüsel ekonomilere hizmet etmek üzere özel olarak tasarlanmıştır.


Herkesin volatilite riski olmadan Lightning ödemelerini kabul etmesini sağlamak için tasarlanmış **Fiat Kanalları** adlı gelişmiş bir Barındırılan Lightning kanalı özelliğine sahip **Basit Bitcoin Wallet'ün (SBW)** bir fork'idir.


Valet şu anda yalnızca Android cihazlar için mevcuttur ve çeşitli açık kaynaklı uygulama mağazalarından indirilip yüklenebilir. Ancak Valet, geliştirici gizliliği ve KYC endişeleri nedeniyle **Google Play Store'da** barındırılmamaktadır.



## Valet'i İndirin ve Kurun


Valet, Standard Sats'nın GitHub sayfasından APK dosyası olarak indirilebilir. [Standard Sats](https://standardsats.github.io/) Valet'i geliştiren şirkettir.


👉 Valet'i indirmek için Standart Sats [GitHub sayfası] (https://github.com/standardsats/valet/releases) adresini ziyaret edin ve **en son** sürümü bulun (Bu genellikle en üstteki sürümdür).


👉 **Assets** bölümüne gidin ve sadece **.apk** uzantılı dosyaya tıklayın. İndirme işleminiz otomatik olarak başlayacaktır.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


i̇ndirme işlemi tamamlandıktan sonra, cihazınızın **Dosya yöneticisi** > **İndirmeler** bölümüne gidin ve Valet apk dosyasını seçin.


![Select_valet_apk](assets/en/002.webp)


👉 Yükleyin ve birkaç saniye içinde uygulamanız hazır olacak ve ana ekranınızda görünecektir.


![valet_icon_on_homescreen](assets/en/003.webp)


Alternatif olarak, Valet'i **F-Droid** uygulama mağazasından da indirebilirsiniz. Cihazınızda F-Droid uygulaması yoksa, [buradan] (https://f-droid.org/en/) indirebilir ve yükleyebilirsiniz.


👉 Ana ekranınızda F-Droid'u açın ve **Valet** için arama yapın. Karşınıza çıkan iki seçenekten **mor ve beyaz simgeli** ilk seçeneği seçin ve **İndir** seçeneğine tıklayın.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


i̇ndirdikten sonra **Yükle** seçeneğine tıklayın ve ekrandaki talimatları izleyin. Kurulum tamamlandığında, **Aç** seçeneğine tıklayarak Valet'i F-Droid'dan başlatabilir veya cihazınızın ana ekranından başlatabilirsiniz.



## Bitcoin Wallet Oluşturma


Valet'te bir Bitcoin wallet'ü iki basit adımda kurabilirsiniz.


👉 Valet'i cihazınızın ana ekranından veya F-Droid uygulamasından başlatın. İki seçenekli bir wallet kurulum ekranı görünecektir: **Yeni Wallet Oluştur** ve **Mevcut Wallet'yı Geri Yükle**.


👉 **Yeni Wallet** Oluştur'u seçin, anında yeni bir wallet oluşturulacak ve ana sayfaya yönlendirileceksiniz.


![set_up_a\_new_wallet](assets/en/006.webp)



## Tohum İfadenizi Yedekleyin


👉 wallet ana sayfasında, üzerinde **"Cihazınızı kaybetmeniz veya değiştirmeniz durumunda wallet kurtarma ifadesini kaydetmek için dokunun" yazılı **Green kartına** tıklayın.**


![seed_phrase_green_card](assets/en/007.webp)


👉 12 İngilizce sözcükten oluşan bir set görüntülenecektir. Bunları 1'den 12'ye kadar sırayla kağıda yazın ve saklayın.


![the_seed_phrase](assets/en/008.webp)


### Dikkat Edin ⚠️:


Aşağıdaki unsurlara dikkat edin:


- Bildiğiniz gibi, Valet kendi kendine emanet edilen bir wallet'tür, bu nedenle seed ifadeniz Wallet'nizi kurtarmak için tek erişimdir.
- seed ifadenizi kaybederseniz, wallet'inize **asla** erişemezsiniz.
- Birisi seed ifadenizi ele geçirirse, tüm Bitcoin'lerinizi geri dönüşü olmayacak şekilde çalabilir.


Bu nedenle, 12 kelimelik seed cümlenizi yazmanız ve güvenli bir yerde saklamanız gerekir. Asla ekran görüntüsü almamalı, e-postanıza taslak olarak kaydetmemeli veya internete bağlı herhangi bir elektronik cihaza kaydetmemelisiniz.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Valet'te Bitcoin'ların Alınması ve Gönderilmesi


Valet, hem wallet hem de Lightning on-chain özelliğine sahip kendinden gözetimli bir Bitcoin'tür. Bu, Bitcoin'ü Valet'ten ya bir **Zincir üzerinde** ya da bir **Lightning Network** aracılığıyla alabileceğiniz ve gönderebileceğiniz anlamına gelir.


Ancak, Lightning aracılığıyla Bitcoin alabilmek veya gönderebilmek için, on-chain Bitcoin'larınızı Liquidity olarak kullanarak bir Lightning kanalı kurmanız gerekir. Ya da satıcılardan bazı Lightning kanal likiditesi satın alabilirsiniz.



## Zincirleme GW Oluşturma-39 Address


Bitcoin'i on-chain üzerinden almak için bir Bitcoin adresi oluşturmanız gerekir.


👉 wallet ana sayfasında, sırasıyla **Bitcoin** ve **Lightning** olarak etiketlenmiş bir **Turuncu** ve bir **Mor kart** göreceksiniz.


👉 **Bitcoin** etiketli Turuncu karta tıklayın. Bitcoin adresini gösteren bir ekrana yönlendirileceksiniz.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Adresi **kopyalayıp** size Bitcoin gönderen kişiye gönderebilir veya QR kodunu sosyal medya veya diğer iletişim kanalları aracılığıyla kişiye göndermek için **paylaş** düğmesine tıklayabilirsiniz.


👉 Ayrıca **Düzenle** düğmesine tıklayarak o adrese gönderilmesi gereken Bitcoin miktarını da ayarlayabilirsiniz.


**Dikkat:** Fatura gibi, düzenleme özelliği de bir adrese bir noktada belirli bir miktarda Bitcoin almak isteyebileceğiniz senaryolarda kullanışlıdır; ancak bu, adresin daha yüksek veya daha düşük miktarlar alamayacağı anlamına gelmez.


👉Yeni rastgele adresler oluşturmak için **Daha fazla yeni adres** üzerine tıklayın.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 wallet ana sayfanızın altındaki **Al** düğmesine tıklayarak da bir on-chain Bitcoin adresi oluşturabilirsiniz. Ardından **Bitcoin adresine al** seçeneğini seçin ve yukarıdaki aynı işlemle devam edin.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Bitcoin'i On-chain üzerinden gönderme


Valet wallet'ten on-chain aracılığıyla Bitcoin göndermek basit bir iştir.


👉 wallet'nızın ana sayfasının altında, **Gönder** düğmesine tıklayın, Bitcoin adresini girin veya adres QR kodunu taramak için **Tara** düğmesine tıklayın, ardından **Tamam** düğmesine tıklayın.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Göndermek istediğiniz Bitcoin tutarını girin. Sats veya Fiat para birimi cinsinden bir tutarı manuel olarak girebilir veya tüm on-chain bakiyenizi kullanmak için **Maks** seçeneğine tıklayabilirsiniz.


i̇şlem için ödemek istediğiniz ücretleri **ücret** etiketli küçük yeşil kutuya tıklayarak ve ardından ücretleri artırmak veya azaltmak için beyaz noktayı sırasıyla sağa veya sola kaydırarak da ayarlayabilirsiniz. İşlemi göndermek için **Ok** öğesine tıklayın.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Bir Lightning Network Kanalı Kurma


Yukarıda belirtildiği gibi, Valet kendi kendine emanet edilen bir Bitcoin ve Lightning wallet'dir; bu nedenle, Lightning ağı üzerinden Bitcoin gönderebilmek ve alabilmek için önce aşağıdaki adımları izleyerek bir Lightning kanalı kurmanız gerekecektir:


👉 Ana ekranda, **Yıldırım** etiketli **Mor kart** üzerine tıklayın. Aşağıdaki seçeneklerin bulunduğu bir sayfaya yönlendirileceksiniz:



- QR Düğümünü Tara
- LNBIG.COM adresinden satın alın
- BITREFILL.COM adresinden satın alın
- LN grafiğinin yeniden senkronizasyonunu talep edin.


Lnbig.com** veya **Purchase from bitrefill.com** seçeneklerinden birini seçtiğinizde, çeşitli kapasitelerde gelen likidite satın alabileceğiniz bu şirketlerin web sitelerine yönlendirileceksiniz. Son seçenek olan **Request LN graph resync** seçeneğini şimdilik dikkate almayın.


Bu yüzden buradaki seçimimiz **Bir Düğüm QR'sini** taramaktır. Bu noktada, kanal açmak istediğiniz düğümün **QR koduna** karar vermiş ve elde etmiş olmanız gerekir. Seçtiğiniz herhangi bir genel düğüme kanal açabilirsiniz. 1ML](https://1ml.com/) veya [Amboss](https://amboss.space/) adreslerine göz atın, seçtiğiniz herhangi bir genel düğümü seçin ve seçtiğiniz düğümün ilgili QR kodunu tarayın.


![channel_opening_options](assets/en/016.webp)


👉 Otomatik olarak kanalınıza para yatırmanız gereken bir sonraki sayfaya yönlendirileceksiniz. Yine, kendi kendine gözetim Lightning ağ kullanımı, bir kanalı finanse etmek için Bitcoin'larınızı kullanmanızı gerektirir. Bu, Lightning kanalını finanse etmek için on-chain wallet'inizde Bitcoin'lara sahip olmanız gerektiği anlamına gelir. Lütfen [Hacken] (https://hacken.io/discover/lightning-network/) tarafından yazılan bu makaleye bakın, Lightning ağı hakkında daha fazla bilgi edinin.


![fund_channel](assets/en/017.webp)


kanalı finanse etmek istediğiniz Bitcoin'lerin **miktarını** girin veya tüm on-chain Bitcoin bakiyenizi kullanmak için **Maks** üzerine tıklayın. Ücreti** ayarlayabilir veya varsayılan ücret ayarını bırakıp **Tamam** seçeneğine tıklayabilirsiniz.


**Dikkat:** Kanalı finanse ettiğiniz miktar, yeni kanalınızın kapasitesi olacaktır (yani, bu kanala ve bu kanaldan işlem yapılabilecek toplam Sats hacmi)


Bir kanal açarken fonlama miktarı olarak **100.000 Sats** üzerinde kullanmanız da önemlidir. Bunun nedeni, birçok Lightning düğümünün kendilerine bir kanal açmak için en az 100.000 Sats kapasite gerektirmesidir. Bu nedenle, deneme ve yanılmadan kaçınmak için, bu aralıktan daha yüksek miktarlar kullanın.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 Bu noktada, wallet ana sayfanızı kontrol ettiğinizde, fonlama tutarınızın artık **Bitcoin kartından** **Lightning kartına** taşındığını göreceksiniz. İşlem geçmişinizde, fonlama işleminin işlendiğini göreceksiniz.


![channel_funding_processing](assets/en/020.webp)


👉 Lightning kartına tıklarsanız, Lightning kanalınızın açıldığını gösteren bilgileri göreceksiniz. Ayrıca işlemler listenizde **kanal fonlama işlemini** göreceksiniz. Fonlama işleminizin blockchain'de onaylanmasını bekleyin ve Lightning kanalınız hazır olacaktır.


![channel_opening](assets/en/021.webp)


👉 Fonlama işlemi onaylanır onaylanmaz, ana sayfanızdaki **Lightning kartına** tıklayın ve Lightning kanalınızla ilgili bilgileri aşağıdaki gibi göreceksiniz:



- NOKTALARLA AYRILMIŞ RASTGELE SAYI SETİ:** Bunlar düğümlerin IP adresleridir. (Sırasıyla IPV4 ve IPV6)
- KAPASİTE:** Bu kanal üzerinden gönderilebilecek ve alınabilecek toplam Sats hacmidir
- GÖNDEREBİLİR:** Bu, bu noktada gönderebileceğiniz Sats miktarıdır. Bunun **Kapasite** ile neredeyse aynı rakam olduğunu fark edeceksiniz. Bunun nedeni, kanal üzerinden herhangi bir ödeme göndermemiş olmanızdır.
- ALABİLİR:** Bu, şu anda bu kanala alabileceğiniz Sats sayısıdır. (Bu noktada çok az ya da hiç olmayacaktır çünkü alabilmeniz için önce gelen bir Liquidity oluşturmak üzere bir miktar Sats göndermeniz gerekir)
- İADE EDİLEBİLİR:** Bu, kanalınızı kapattığınızda on-chain adresinize geri ödenecek tutarı gösterir. Bu aynı zamanda **Kanalınızın yerel bakiyesi** olarak da adlandırılır. Kanal kapasitesinden biraz daha az olduğuna dikkat edin; bunun nedeni, bir kanalı kapatırken, tıpkı kanalı finanse ederken yaptığınız gibi, kapatma işlemini blockchain'de yayınlamak için bir ücret ödemeniz gerektiğidir. Dolayısıyla sistem ödeyeceğiniz yaklaşık en düşük tutarı düşmüştür)
- UÇUŞTAKİ DEĞER:** Birisi kanalınıza bir miktar sats gönderdiğinde veya siz birine bir miktar sats göndermeye çalıştığınızda ve herhangi bir nedenle işlem geciktiğinde, genellikle bu alanda gösterilir.


![channel_info](assets/en/022.webp)


## Kanalınız Aracılığıyla Sats Gönderme


Sats'yi Lightning Network üzerinden göndermek basit bir iştir.


👉 Ana sayfanın alt kısmında **Gönder** seçeneğine tıklayın ve Lightning faturasını (kopyalamış olmanız gerekir) verilen alana **yapıştırın** veya Lightning faturası QR kodunu taramak için **Tara** seçeneğine tıklayın.


![click_send_or_scan](assets/en/023.webp)


Çoğu Lightning faturası, ödenecek önceden girilmiş bir tutarla birlikte gelir. Ancak birkaç durumda, tutarı doldurmanız gereken açık bir fatura olabilir.


👉 Tutarı **Dolar** veya **Sats** cinsinden girin veya Lightning kanalınızdaki tüm bakiyeyi kullanmak için **Maks** seçeneğine tıklayın ve ardından **Tamam** seçeneğine tıklayın. İyi bir yol bulunur bulunmaz, ödemeniz gönderilecek ve birkaç saniye içinde tamamlanacaktır. Ödemenin tamamlanıp tamamlanmadığını görmek için ana sayfaya göz atın. Tamamlandığında yeşil bir onay işareti alacaktır.


![enter_the_amount](assets/en/024.webp)


## Kanalınız Aracılığıyla Sats Alma


Lightning kanalınızda ödeme almak, büyük ölçüde gelen bir Liquidity'nizin olup olmamasına bağlıdır. Bir kanal açtıktan sonra, kanal bağlantısının diğer ucunda **gelen likidite** oluşturmak için en azından bir miktar Sats gönderene kadar ödeme alamazsınız. Sats alıp alamayacağınızı ve alabileceğiniz Sats miktarını onaylamak için kanal bilgilerinizdeki **Alabilir** alanını kontrol edin. Bu size her zaman kaç tane Sats alabileceğinizi gösterecektir.


Şimdi, kanalınızdan bir miktar Sats gönderdiğinizi, artık gelen likiditeniz olduğunu ve Sats alabileceğinizi varsayalım.


Lightning kanalından alım yapmak için bir fatura oluşturmanız gerekir. Adresleri kullanan Bitcoin on-chain'ün aksine, Lightning ağı faturaları kullanır. Valet'te fatura oluşturmak için iki yol vardır.


#### SEÇENEK 1


👉 Ana sayfanın en altında **Al** seçeneğine tıklayın, **Yıldırım faturasına al** seçeneğini seçin. Faturada alınacak tutarı doldurun ve **Tamam** seçeneğine tıklayın. Faturayı kopyalayın veya QR kodunu ödeme yapan kişi ile paylaşın.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### SEÇENEK 2


👉 wallet ana sayfanızdaki mor Lightning kartına tıklayın. Kanalınızda herhangi bir yere dokunduğunuzda bir seçenekler listesi açılacaktır. Kanala al** seçeneğini seçin ve aldığınız miktarı girin (Sats veya dolar cinsinden). Faturayı doldururken kaç tane Sats alabileceğinizi de (gelen kapasite) göreceksiniz. Tamam** seçeneğine tıklayın ve faturayı kopyalayın veya QR kodunu ödeme yapan kişiyle paylaşın.


![receive_to_channel](assets/en/028.webp)


**Dikkat:** İlk seçenek evrensel bir seçenektir, yani birden fazla aktif kanalınız varsa ve ilk seçeneği kullanırsanız, sistem otomatik olarak Sats'yi almak için kanallarınızdan birini seçecektir.


Dolayısıyla, bu senaryoda, belirli bir kanala Sats almak istiyorsanız ikinci seçeneği kullanmak en iyisidir.


### Kanal Pop-Up Seçenekleriniz Açıklandı


Kanalınıza dokunduğunuzda, aşağıdaki seçenek alanları görüntülenecektir:


![channel_pop_ups](assets/en/029.webp)


**LIGHTNING KANAL DETAYLARINI PAYLAŞIN:** Bu, uzak eş kimliği, yerel kanal kimliği, Fonlama işlemi, oluşturma tarihi vb. gibi kanal detaylarınızı paylaşmanızı sağlar.


**CÜZDANA KANAL KAPATMA:** Yıldırım kanalınızı istediğiniz zaman kapatabilirsiniz. Kanalınızı kapatmak için sistem, kanalın kendi tarafınızdaki Bitcoin bakiyenizi kontrol eder (yerel bakiyeniz olarak da bilinen **"Gönderilebilir "** alanını hatırlayın) ve size geri gönderir. Valet'te, kanal kapatıldığında Bitcoin'un nereye gönderilmesini istediğinizi seçebilirsiniz. Yani, **Kanalı wallet'e kapat** iki seçeneğinizden biridir.


👉 Bu seçeneğe tıklayın ve **Bitcoin**'yi seçin. Kanal kapatma işlemi başlayacak ve Bitcoin kanal bakiyeniz wallet'ün on-chain adresine geri gönderilecektir.


![close_channel_to_wallet](assets/en/030.webp)


**KANALI ADDRESS'E KAPAT:** Bu, bir kanalı kapatmak için ikinci seçenektir. Bu seçeneği seçtiğinizde, kanalınızdaki Bitcoin bakiyesinin gönderileceği bir wallet adresi girmeniz istenecektir. Bu seçenekte, yalnızca kanalı kapatmak istediğiniz Bitcoin adresinin QR kodunu tarayabileceğinizi lütfen unutmayın. Şu anda, adresin manuel olarak yapıştırılması için bir seçenek bulunmamaktadır.


👉 Bu seçeneğe tıklayın, Bitcoin adresini tarayın ve **Ok**'a tıklayın. Kanal kapatma işlemi başlayacak ve Lightning Bitcoin bakiyeniz taradığınız adrese gönderilecektir.


![scan_address_and_Ok](assets/en/031.webp)


**KANALA AL: ** Bu, bir fatura oluşturmakla aynı şeydir, ancak bazı durumlarda Fiat kanalları (Valet wallet'de elde edilebilen benzersiz bir Lightning kanalı türü) dahil olmak üzere birden fazla kanalınız olabilir. Dolayısıyla, açık birden fazla kanalınız varsa, bu seçenek belirli bir kanala ödeme alabilmenizi sağlar.


**DİĞER KANALLARDAN DOLUM:** Bu seçenek, bir kanalı mevcut diğer kanallardan doldurmanıza olanak tanıyan bir özelliktir. Örneğin, 2 farklı Lightning kanalınız varsa (A ve B) ve A kanalındaki Bitcoin bakiyesi tükenmişse, bu seçenekle A kanalının bakiyesini B kanalından kolayca ve otomatik olarak doldurabilirsiniz.


**DOĞRUDAN ÖZEL DEĞİL ALMA:** Bu aynı zamanda ödeme almak için bir fatura oluşturma seçeneğidir, ancak bu seçeneği kullandığınızda, gönderen size doğrudan ödeme yapar. Bu, ödemenin normal bir Lightning ödemesi gibi size ulaşmadan önce farklı düğümlerden geçmediği anlamına gelir. Yani, özünde, gönderen ödeme yaptığı kişinin siz olduğunu bilir, kanal kimliğinizi vs. bilir. Bu seçenek genellikle güvendiğiniz bir kaynaktan ödeme aldığınızda ve gizliliğinizi korumanız gerekmediğinde kullanılabilir.


## Barındırılan ve Fiat Kanalları


Diğer birçok Bitcoin wallet gibi Valet de basit, hafif bir Bitcoin ve Lightning wallet'dir. Ancak onu diğer Bitcoin wallet'lerin çoğundan ayıran benzersiz bir Lightning özelliğine sahiptir. Bu özelliğe **Hosted ve Fiat Kanalları** denir.


Fiat kanalları, Lightning ağına kolay giriş ve kullanım sağlayan bir tür Lightning uygulamasıdır. Tıpkı normal bir Lightning kanalında olduğu gibi tam anonimliğe izin veren bir saklama çözümüdür. Fiat kanalları teknolojisi, Lightning ağında Bitcoin türevlerinin oluşturulmasını da sağlar. Fiat kanalları ile tüccarların Bitcoin'nin oynaklığı konusunda endişelenmeden sabit değerli Bitcoin ödemelerini kabul edebilmeleri buna bir örnektir.


Fiat kanallarının Valet üzerindeki mevcut uygulaması, Sats tarafından desteklenen istikrarlı sentetik Fiat para birimlerinin oluşturulmasını sağlar. Ana bilgisayarın bu hizmeti sunan herhangi bir Lightning düğümü olduğu ve müşterinin Valet kullanıcısı olduğu bir Ana Bilgisayar-Müşteri ilişkisi kullanır. Bu bir saklama çözümüdür çünkü tüm Sats'ler Ana Bilgisayar tarafındadır; ancak fatura oluşturma, tor yönlendirme ve ön görüntü oluşturma işlemleri normal bir Lightning kanalında olduğu gibi yine müşteri tarafında gerçekleşir.


Bir Fiat kanalı açmak, bir Lightning kanalı açmakla aynı süreci gerektirir. Tek önemli fark, bu durumda müşterinin (Vale kullanıcısı) kanal kapasitesi oluşturmak için herhangi bir likidite on-chain taahhüt etmek zorunda olmamasıdır. Ana Bilgisayar kanal kapasitesini belirler ve müşteri için tüm ödemeleri yönlendirir.


👉 Bir Fiat kanalı açmak için, wallet ana sayfanızdaki mor **Lightning kartına** tıklayın. Düğüm QR'sini** tara öğesini seçin (Bu noktada, kanal açmak istediğiniz bir Ana Bilgisayar tanımlamış ve düğümün QR'sini almış olmanız gerekir. Fiat kanalı açabileceğiniz bir Ana Bilgisayar düğümü örneği, Standart Sats tarafından SATM düğümüdür)


**Dikkat:** Herkesin Ev Sahibi olabileceğine dikkat etmek önemlidir. İhtiyacınız olan tek şey **Fiat kanal eklentisi** ve bir **Hedging hizmeti** ile bir Lightning düğümü çalıştırmaktır. Fiat kanalları, *Standard Sats* tarafından geliştirilen açık kaynaklı bir projedir. Daha fazla bilgi için [burada](https://github.com/standardsats/fiat-channels-rfc) ve [burada](https://standardsats.github.io/).


SATM düğümü QR aşağıda:


![SATM_node_QR](assets/en/032.webp)


👉 QR düğümünü taradıktan sonra, **Request USD fiat channel** veya **Request EUR fiat channels** seçeneğine tıklayın (Bu, Fiat bakiyelerinizin kote edileceği fiat cinsidir). Şimdilik USD'yi seçin ve **Tamam** seçeneğine tıklayın. Kanal otomatik olarak açılacak ve hemen Sats almaya başlayabilirsiniz. Görüyorsunuz, bu kadar basit!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 wallet'unuzun ana sayfasına gidin, **USD** etiketli **açık yeşil** bir kart göreceksiniz, bu sizin **Fiat kanalınızdır**.


![fiat_channel_card](assets/en/035.webp)


**Dikkat:** Bir Fiat kanalında Sats aldığınızda, aldığınız Sats'nin fiat değeri sabit bir bakiye olarak kilitlenirken, Sats hacmi Bitcoin fiyatı ile dalgalanır. Bu çözüm, çoğunlukla ödeme için Sats'yi kabul etmek isteyen ancak Bitcoin'in volatilite zorluklarıyla yüzleşmek istemeyen tüccarlar için tasarlanmıştır. Bu, Lightning ağında işlem yapmaya devam ederken, Bitcoin'in küresel erişiminden ve Lightning Network'de bir değişim aracı olarak hızlı uzlaşmasından yararlanarak her zaman sabit değeri korumalarına yardımcı olur.


Fiat kanalınız oluşturulduğunda, göreceğiniz Değer alanları ve her birinin ne anlama geldiği aşağıda açıklanmıştır:


![fiat_channel_info](assets/en/036.webp)



- NOKTALARLA AYRILMIŞ RASTGELE SAYI SETİ:** Bunlar düğümlerin IP adresleridir. (Sırasıyla IPV4 ve IPV6)
- SUNUCU FİYATI:** Bu, Barındırıcının size hizmetleri sunduğu Bitcoin piyasa fiyatıdır. Bu genellikle baskın piyasa fiyatından biraz farklı olacaktır, çünkü bir Barındırıcı küçük bir prim ekleyebilir. Bu orana karar vermek tamamen Ev Sahibine bağlıdır; dolayısıyla bu da Ev Sahibinden Ev Sahibine değişecektir.
- FIAT DENGESİ:** Bu, bu kanalda aldığınız her satışın kilitli sabit fiat değeridir. Daha önce açıklandığı gibi, Fiat kanalınıza her Sats aldığınızda, Sats'in alındığı andaki fiat değerinin bu alanda sentetik bir sabit fiat değeri olarak hemen kilitlendiğini unutmayın. Fiat Bakiye** değeriniz Bitcoin piyasa fiyatı ile dalgalanmaz. Bu kanaldan ödeme yapmak istediğinizde, yalnızca bu Fiat bakiyesinin Sats eşdeğerini gönderebilirsiniz. Yani bunu Sats tarafından desteklenen dijital bir fiat para birimi olarak düşünün.
- KAPASİTE:** Bu kanal üzerinden gönderilebilecek ve alınabilecek toplam Sats hacmidir. (Bu da Ana Bilgisayar tarafından ayarlanır. Ve normal bir Lightning kanalından farklı olarak, bu kapasite duruma göre Ana Bilgisayar tarafından ayarlanabilir)
- GÖNDEREBİLİR: ** Bu, fiat bakiyenize bağlı olarak her noktada gönderebileceğiniz Sats hacmidir. Bu, normal bir Lightning kanalında sahip olduğunuzdan tamamen farklıdır, çünkü bu değer Bitcoin fiyatı ile dalgalanır. Dolayısıyla, burada gördüğünüz, **Sunucu Oranına** dayalı olarak herhangi bir zamanda Fiat bakiyenizin Sats değeridir.
- ALABİLİR:** Bu, o anda bu kanala alabileceğiniz Sats sayısıdır. Kanalınızı oluşturduktan sonra bu değer kanal kapasitesi ile aynı olmalıdır.
- UÇUŞTAKİ DEĞER:** Birisi kanalınıza bir miktar sats gönderdiğinde veya siz birine bir miktar sats göndermeye çalıştığınızda ve herhangi bir nedenle işlem geciktiğinde, genellikle bu alanda gösterilir.


İşte Fiat kanalları hakkında dikkat edilmesi gereken önemli noktalar:



- Normal bir Lightning kanalından farklı olarak, bir fiat kanalı açtığınızda, hemen Sats almaya başlayabilirsiniz, ancak gönderemezsiniz. Yalnızca Sats aldığınızda Sats gönderebilirsiniz.
- Her zaman, gönderilen ve alınan varlık Sats'tür. Fiat Bakiyesi*, zamanın herhangi bir noktasında alınan Bitcoin değerinin sentetik bir IOU temsilidir. Yani, bir token yaratımı veya yeni bir kripto para birimi değildir.
- Fiat kanalı çoğunlukla volatilite endişeleri nedeniyle Bitcoin ödemelerini kabul etme konusunda şüpheci olan tüccarlar/işletmeler için yararlıdır. Ayrıca, maaş sermayelerini istikrarsız hale getirebilecek Bitcoin oynaklığının sonuçlarına katlanmadan çalışanlarının maaşlarını Bitcoin olarak ödemek isteyen şirketler için de yararlı olabilir. Bitcoin kullanımının yaygın olduğu bir bölgede yaşayan ancak sabit yaşam maliyetleri olan bireyler için de faydalı olabilir.
- İADE EDİLEBİLİR** olarak etiketlenmiş bir alan olmadığına dikkat edin. Bunun nedeni, teknik olarak, bir Fiat kanalını kapatamazsınız. Bir Fiat kanalını kullanmayı ancak bakiyesini normal Lightning kanalınıza boşaltarak durdurabilirsiniz.


### Fiat Kanal Pop-Up Seçenekleriniz Açıklandı


Fiat Lightning kanalınıza dokunduğunuzda, aşağıdaki alanlar görüntülenecektir:


![fiat_channel_pop_up](assets/en/037.webp)


**ANA KANAL AYRINTILARINI PAYLAŞ:** Bu, uzak eş kimliği, yerel kanal kimliği, oluşturma tarihi vb. gibi Fiat kanal ayrıntılarınızı paylaşmanıza olanak tanır.


**KANAL DURUMUNU DIŞA AKTARMA:** Bu, bir kanalın durumunu herhangi bir noktada dışa aktarmanızı sağlar. Bu genellikle kanal hatalarının düzeltilmesinde yararlıdır ve bir Ana Bilgisayar, ihtiyaç duyulması halinde bunu paylaşmanızı isteyebilir.


**KANAL DENGESİNİ BOŞALTIN:** Daha önce de belirtildiği gibi, teknik olarak bir Fiat kanalını kapatamazsınız, ancak kanalınızın dengesini mevcut normal Lightning kanalınıza boşaltabilirsiniz. Bu, Fiat bakiyenizin Sat eşdeğerini otomatik olarak normal Lightning kanalınıza taşır.


**KANALA AL: ** Bu, bir fatura oluşturmakla aynı şeydir, ancak bazı durumlarda, bir kullanıcının normal Lightning kanalları da dahil olmak üzere farklı Ana Bilgisayarlara sahip birden fazla Fiat kanalı olabilir. Dolayısıyla, bir kullanıcının birden fazla kanalı açıksa, bu seçenek belirli bir kanala ödeme alabilmesini sağlar.


**DİĞER KANALLARDAN DOLUM:** Bu seçenek, kullanıcının bir kanalı mevcut diğer kanallardan doldurmasına izin veren bir özelliktir. Yani, bu seçenekle, Fiat kanalınızı normal bir kanaldan veya sahip olduğunuz diğer Fiat kanallarından doldurabilirsiniz, aynı şekilde boşaltabilirsiniz.


**DOĞRUDAN ÖZEL DEĞİL ALMA:** Bu aynı zamanda ödeme almak için bir fatura oluşturma seçeneğidir, ancak bu seçeneği kullandığınızda, gönderen size doğrudan ödeme yapar. Bu, ödemenin size ulaşmadan önce farklı düğümlerden geçmediği anlamına gelir. Yani, özünde, gönderen ödeme yaptığı kişinin siz olduğunu bilir, kanal kimliğinizi bilir, vb. Bu seçenek genellikle güvendiğiniz bir kaynaktan ödeme aldığınızda ve gizliliğinizi korumanız gerekmediğinde kullanılabilir.


## Vale Ayarları:


Diğer tüm uygulamalar gibi, Valet de zevkinize göre ayarlayabileceğiniz uygulama ayarlarına sahiptir. Ayarlar sayfasına ana ekrandan erişebilirsiniz.


👉Ana ekranda, ayarlara erişmek için ekranın sağ üst köşesinde bulunan **Gear** simgesine tıklayın. Ayarlar bölümünde yer alan bileşenler aşağıdadır.


![settings_icon](assets/en/038.webp)


**YEREL KANAL YEDEKLEME ETKİNLEŞTİRİLDİ:** Aksi halde **Devre Dışı,** ise etkinleştirmelisiniz çünkü Valet'i kaldırıp yeniden yüklerseniz normal Lightning kanallarınızı kurtarmanın tek yolu budur. Bunu daha sonra açıklayacağız. Bu yüzden buna tıklayın ve Valet'e **medya depolama alanınıza** izin verin çünkü yedekleme dosyası buraya kaydedilir.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**YEREL YEDEKLEME NEREDE SAKLANACAK:** Valet'e depolama alanınız için izin verdiğiniz sürece, bu alan otomatik olarak yerel yedeklemeleri **Downloads** klasörünüzde saklayacak şekilde ayarlanacaktır. Ancak buraya tıklayarak ve istediğiniz herhangi bir klasörü seçerek bunu değiştirebilirsiniz.


**ZİNCİR CÜZDANLARI YÖNET** Bu biraz teknik bir konudur ve yeterince deneyimli değilseniz bununla uğraşmanıza gerek yoktur. Buradaki varsayılan ayar gayet iyidir.


**DONANIM CÜZDANI EKLE:** Bağlamak ve izlemek istediğiniz bir Donanım wallet'nız yoksa, bununla da uğraşmamalısınız. Bu ayarla, Trezor veya Cold Kartı gibi donanım wallet'nızı tarayabilir ve bağlayabilir ve faaliyetlerini izleyebilirsiniz. Bu sadece izleme özelliğidir, yani buradan Donanım wallet üzerinde işlem yapamazsınız. Yalnızca wallet etkinliklerini, bakiyelerini vb. gözlemleyebilir ve izleyebilirsiniz.


**SET CUSTOM ELECTRUM NODE:** Bu da teknik bir konudur ve yeterince bilgili değilseniz bununla uğraşmamalısınız. Varsayılan ayar yeterince iyidir.


**BİTCOİN BİRİMLERİ:** Bu, Bitcoin bakiyenizin nasıl görüntülenmesini istediğinizi belirtir. İlk seçenek bakiyenizi Satoshi terimleriyle, örneğin 1.000.000 Sats olarak gösterirken, ikinci seçenek BTC ondalık noktalarıyla gösterir. örneğin 0.01BTC


**Bu kutuyu işaretlerseniz, wallet'ünüze giriş yapmak ve işlemlerin kimliğini doğrulamak için girmeniz gereken bir PIN veya parmak izi ayarlamanız gerekecektir.


**TOR BAĞLANTISI KULLAN:** Bu kutuyu işaretlerseniz, işlemleriniz Tor ağı üzerinden yönlendirilecektir. Ekstra bir gizlilik katmanı ekler, ancak özellikle Lightning ödemeleri için ödeme veriminin gecikmesine neden olabilir.


**BIP39 KURTARMA İFADESİNE BAKIN:** Burası yedekleme için 12 kelimelik seed ifadenize erişebileceğiniz yerdir. Yani daha önce yazmadıysanız veya yazdığınız yeri bulamıyorsanız, Wallet'ünüze hala erişiminiz olduğu sürece, buradan kopyalayabilirsiniz.


**KULLANIM İSTATİSTİKLERİ:** Bu, wallet'nin oluşturulmasından bu yana tüm işlemlerinizin ve faaliyetlerinizin bir özetini gösterir


![usage_stats](assets/en/041.webp)


## Wallet Kurtarma


Valet gözetim altında olmayan bir wallet'dir, bu nedenle cihazınızı kaybederseniz veya wallet uygulamanızı kaldırırsanız, Bitcoin'larınızı ve Lightning kanallarınızı geri almak için bir wallet kurtarma işlemi yapmanız gerekecektir. Bu eğitimin başında, **12 kelimelik seed cümlenizi** yazmanın öneminden bahsetmiştik çünkü bu, wallet'nizi kurtarmanın anahtarıdır. wallet'nize geri dönmenize yardımcı olabilecek hiçbir müşteri hizmetleri temsilcisi yoktur.


Aktif bir Lightning kanalınız olup olmamasına bağlı olarak, Valet wallet'nizi kurtarmak için gereken iki önemli araç vardır. Aktif bir normal Lightning kanalına sahip olmayan bir kullanıcı için tek gereken, aşağıdaki basit adımları izleyerek **12 kelimelik seed cümlesidir**:


👉 Yeni bir Valet uygulaması yükleyin ve uygulamayı başlatın/başlatın.


👉 **Mevcut Wallet**'ü Geri Yükle'yi seçin


![restore_existing_wallet](assets/en/042.webp)


👉 **Sadece kurtarma ifadesini** seçin.


![select_recovery_phrase](assets/en/043.webp)


👉 12 kelimelik kurtarma cümlenizi girin ve **Tamam** düğmesine tıklayın.


![input_12_words](assets/en/044.webp)


wallet'niz kurtarılacaktır. Bu durumda, yalnızca on-chain Bitcoin bakiyeniz geri yüklenecektir.


Ancak, aktif bir normal Yıldırım kanalınız varsa ve wallet'ınızı yalnızca kurtarma ifadesiyle kurtarırsanız, Yıldırım kanalınız zorla kapatılır ve üzerindeki tüm Bitcoin bakiyeniz otomatik olarak on-chain bakiyenize gönderilir.


Valet wallet'inizi kurtarmanın diğer yolu, özellikle de Valet'i kaldırmadan önce normal bir Lightning kanalınız açıksa, **cihazınızda kayıtlı yerel yedekleme dosyasını ve 12 kelimelik seed cümlenizi** kullanmaktır. Bu ikisini kullanırsanız, Lightning kanal durumunuz geri yüklenecek, dolayısıyla Lightning kanalınız zorla kapatılmayacaktır.


İşte adımlar:


👉 Yeni bir Valet uygulaması yükleyin ve uygulamayı başlatın/başlatın.


👉 **Mevcut Wallet'ü Geri Yükle** öğesini seçin.


👉 **Yedekleme + Kurtarma ifadesini** seçin.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Telefonunuzun dosya yöneticisinden Yedekleme dosyasını seçin. (Varsayılan olarak her zaman **Downloads** klasörünüzde saklanır)


![local_backup_file_in_download_folder](assets/en/046.webp)


Doğru yedekleme dosyası seçildiğinde, **"Yedekleme dosyası mevcut "** olduğunu onaylayan bir istem görüntülenecek ve ardından sizden 12 kelimelik seed ifadenizi girmeniz istenecektir.


![enter_12_words](assets/en/047.webp)


👉 12 kelimelik kurtarma cümlenizi girin ve **Tamam** düğmesine tıklayın. wallet ana sayfanıza yönlendirileceksiniz.


👉 Bitcoin ağ senkronizasyonunun (**SYNC**) ve Lightning düğüm senkronizasyonunun (**LN Sync**) tamamlanmasını bekleyin ve Lightning kanallarınız da dahil olmak üzere wallet'niz tamamen geri yüklenecektir.


![LN_sync](assets/en/048.webp)


## Sonuç


Valet, yeni kullanıcıları işe almak için uygun hale getiren özellikleriyle heyecan verici bir wallet çözümüdür. Ayrıca, Fiat tarafından işletilen işletmelerin Bitcoin standardına entegrasyonunu sağlayan çok yeni olmayan bir teknoloji olan Fiat kanalına da sahiptir.


Valet'i bugün indirin ve bir deneyin!!! 🧡