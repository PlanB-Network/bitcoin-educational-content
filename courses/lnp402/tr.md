---
name: SDK ile Lightning üzerinde geliştirme
goal: Orta düzey Rust ve SDK eğitimi ile yıldırım geliştirme becerilerinizi geliştirin.
objectives: 

  - Rust Diline alışmak
  - Bitcoin'yi geliştirmek için neden Rust kullanıldığını anlayın
  - SDK'nın temelini alın

---

# LN geliştirme becerilerinizde ilerleme


SDK ile LN yolculuğunuza hoş geldiniz.


Bu kursta, Rust kitabının temellerini öğrenecek, ardından SDK'ları kullanarak bazı LN programlama ile devam edecek ve bazı pratik alıştırmalarla bitireceksiniz. Çeşitli geçmişlere sahip öğretmenlerimiz sizi pratik becerilere yönlendirecek ve günümüzün LN mühendislerinin sıklıkla karşılaştığı çeşitli zorlukları açıklayacaktır.


Bu kurs, Fulgur'Ventures tarafından Ekim 2023'te LN Tuscany etkinliği sırasında düzenlenen CANLI seminer sırasında çekilmiştir.


Kursun tadını çıkarın!


+++

# Giriş

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Kursa genel bakış

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Giriş**


SDK'larla ilgili bu ileri düzey programlama kursuna hoş geldiniz. Bu eğitimde, Rust'un temellerini öğrenecek, ardından BTC ve Rust'a odaklanacak ve SDK'ları kullanarak bazı pratik alıştırmalarla bitireceksiniz.


Bu eğitim şimdilik sadece İngilizce olarak sunulacak ve geçtiğimiz Ekim ayında Fulgure Venture tarafından Toskana'da düzenlenen canlı seminerin bir parçası olacak. CANLI etkinliğin programı aşağıda bulunabilir ve bu eğitim sadece ilk haftaya odaklanacaktır. İkinci yarı RGB'a yöneliktir ve RGB kursunda bulunabilir.


**Öğretmenler**


Bu programın bir parçası olan öğretmenlerimize çok teşekkür ederiz:



- Alekos: "Hey, ben bir İtalyan kodlayıcı ve hacker'ım. bitcoindevkit, magicalbitcoin ve h4ckbs gibi çeşitli projelerde çalıştım"
- Andrei : "LIPA'da yıldırım uzmanı"
- Gabriel : "Kod yazıyorum ve bir şeyler yapıyorum."
- Jesse de wit : "Lightning Network meraklısı | geliştirici | Breez"


**Seminer şeması**


LN Toskana etkinliğinin 1. haftası

![image](assets/1.webp)


Bu kursu tamamladıktan sonra, devam eğitimiyle ilgileniyorsanız, programın ikinci bölümünü burada bulabilirsiniz:

![image](assets/2.webp)



Bu eğitim size Rust ve çeşitli SDK'ları kullanarak Lightning Network üzerinde programlama becerilerinizi geliştirme fırsatı verir. Lightning Network'e özgü geliştirmeye dalmak isteyen sağlam bir programlama geçmişine sahip geliştiriciler için tasarlanmıştır. Rust'in temellerini, neden Bitcoin geliştirme için uygun olduğunu öğrenecek ve ardından özel SDK'ları kullanarak uygulamalı uygulamaya geçeceksiniz.


**Bölüm 2: Rust** ile kod yazmayı öğrenin

Bu bölümde, bir dizi aşamalı bölüm aracılığıyla Rust'in temellerini keşfedeceksiniz. Rust kodu yazmayı, özelliklerini anlamayı ve yedi ayrıntılı bölüm boyunca temel özelliklerinde ustalaşmayı öğreneceksiniz. Bu modül, Rust'in neden Bitcoin geliştirme için tercih edilen bir dil olduğunu anlamak için gereklidir.


**Bölüm 3: Rust & Bitcoin**

Burada, Rust'ün Bitcoin geliştirme için neden uygun bir seçim olduğunu derinlemesine inceleyeceğiz. Hata modeli, UniFFI aracı ve asenkron özellikler hakkında bilgi edineceksiniz - bunların hepsi sağlam ve güvenli yazılım oluşturmada Elements'in temel özellikleridir.


**Bölüm 4: SDK'lar ile LNP/BP geliştirme**

Breez SDK ve Lipa için Greenlight gibi çeşitli SDK'ları kullanarak LN düğümlerini nasıl geliştireceğinizi öğreneceksiniz. Bitcoin ve Lightning geliştirmeyi basitleştirmek için tasarlanmış kütüphaneleri kullanarak Lightning Network uygulamalarını nasıl uygulayacağınızı göreceksiniz.


Lightning Network becerilerinizi Rust ile geliştirmeye hazır mısınız? Hadi başlayalım!

# Rust kitabı ile nasıl kod yazılacağını öğrenin

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Rust'a Giriş (1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::


## Rust'e Giriş (2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


## Rust'ye Giriş (3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::


## Rust'e Giriş (4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::


## Rust'e Giriş (5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::


## Rust'e Giriş (6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::


## Rust'ya Giriş (7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::


# Rust & BTC

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Neden Bitcoin başına Rust

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


## Hata modeli

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::


## Unniffit

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::


## Asenkron özellikler

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>


:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::


# SDK ile LNP/BP Geliştirme

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## SDK üzerinde LN düğümü

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::


## Lipa için yeşil ışık

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::


## Lipa için Breez sdk

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>


:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::


# Son Bölüm

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>




## Yorumlar & Derecelendirmeler

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Sonuç

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>