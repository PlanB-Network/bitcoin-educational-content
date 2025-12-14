---
name: Bitcoin Programlama
goal: Sıfırdan eksiksiz bir Bitcoin kütüphanesi oluşturun ve Bitcoin'in kriptografik temellerini anlayın
objectives: 

 - Python'da sonlu alan aritmetiği ve eliptik eğri işlemlerini uygulama
 - Bitcoin işlemlerini programlı olarak oluşturma ve ayrıştırma
 - Testnet adresleri oluşturun ve işlemleri ağ üzerinden yayınlayın
 - Bitcoin'ün güvenlik modelinin altında yatan matematiksel temellere hakim olma

---
# Bitcoin'in senaryolarına ve programlarına bir yolculuk


Jimmy Song tarafından verilen bu iki günlük yoğun kurs, sıfırdan eksiksiz bir Bitcoin kütüphanesi oluşturarak sizi Bitcoin'in teknik temellerinin derinliklerine götürür. Sonlu alanlar ve eliptik eğrilerin temel matematiği ile başlayarak, işlem ayrıştırma, komut dosyası yürütme ve ağ iletişimi yoluyla ilerleyeceksiniz. Jupyter not defterlerindeki uygulamalı kodlama alıştırmaları sayesinde, kendi Testnet Address'nizi oluşturacak, işlemleri manuel olarak oluşturacak ve bunları doğrudan ağa yayınlayacaksınız - tüm bunları yaparken Bitcoin'i güvenli ve Trustless yapan kriptografik ilkeler hakkında derin bir anlayış kazanacaksınız.


Keşfinizin tadını çıkarın!


+++

# Giriş

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Dersin Genel Görünümü

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

PRO 202 _**Programming Bitcoin**_ kursuna hoş geldiniz. Bu yoğun yolculuk sizi sonlu alan aritmetiğinden Bitcoin Testnet'te gerçek işlemler oluşturma ve yayınlamaya kadar götürecektir.

Bu derste, Python’da adım adım bir Bitcoin kütüphanesi oluşturacak ve Bitcoin’in güvenliği ile iç işleyişini doğru şekilde anlamak için gereken kriptografi, protokol ve yazılım temellerini edineceksiniz. PRO 202 yaklaşımı tamamen uygulamalıdır: her kavram Jupyter defterlerinde anında uygulanır ve teori ile kodun birbirini güçlendirmesi sağlanır.

### Bitcoin için Temel Matematiksel Kavramlar

Bu ilk bölüm, vazgeçilmez matematiksel temeli oluşturur. Sonlu alan aritmetiğini ve eliptik eğri işlemlerini (grup kanunu, toplama, ikiye katlama, skaler çarpma...) uygulayacaksınız — ECDSA için ön koşullar. Amaç iki yönlü: kriptografik imzaları mümkün kılan cebirsel yapıyı anlamak ve bunları işlemek için güvenilir Python araçları oluşturmak.

Daha sonra ECDSA’nın bileşenlerini resmileştireceksiniz: anahtar oluşturma, nokta biçimlendirme, hashleme, imza oluşturma ve doğrulama. Bu bölüm, teoriyi doğrudan uygulamayla ilişkilendirir ve uygulama ayrıntılarını ve temel güvenlik modelinin sağlamlığını vurgular.

### Bir Bitcoin İşleminin İç Yapısı

İkinci bölümde, bir Bitcoin işleminin yapısını analiz edeceksiniz: UTXO'lar, girişler/çıkışlar, diziler, betikler, kodlamalar ve daha fazlası. İşlemleri oluşturmak, imzalamak ve doğrulamak için kod yazacak, hash tarafından neyin taahhüt edildiğini ve nedenini tam olarak anlayacaksınız.

Sonraki adımda, minimal bir _Script_ yürütücü uygulayacak, temel opkodları inceleyecek ve harcama yollarını doğrulayacaksınız. Amaç, işlem davranışlarını denetleyebilmenizi, doğrulama hatalarını teşhis edebilmenizi ve harcama politikalarının güvenliği hakkında değerlendirme yapabilmenizi sağlamaktır.

### Bitcoin Ağının İç Yapısı

Üçüncü bölümde, işlemi daha geniş bir sistem içine yerleştireceksiniz: blok yapısı, başlıklar, zorluk ve İş Kanıtı (Proof-of-Work) mekanizması. Protokol mesajlarını, blok başlıklarını ve Merkle ağaçlarını ele alacaksınız.

Son olarak, eşler arası (peer-to-peer) düğüm iletişimini, mesaj optimizasyonunu ve SegWit’in tanıtımını inceleyeceksiniz.

Plan ₿ Academy'deki her derste olduğu gibi, son bölüm anlayışınızı pekiştirmek için tasarlanmış bir değerlendirme içerir. Bitcoin’in iç işleyişini ortaya çıkarmaya ve onu çalıştıran kodu yazmaya hazır mısınız? Haydi başlayalım!

# Bitcoin için Temel Matematiksel Kavramlar

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Bitcoin Uygulaması için Matematik

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Eliptik Eğri Kriptografisi

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin İşlem İç Çalışmaları

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin İşlem Ayrıştırma ve ECDSA İmzaları

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Komut Dosyası ve İşlem Doğrulama

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## İşlem Oluşturma ve Senaryoya Ödeme Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Ağ İç Çalışmaları

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Blokları ve Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Ağ İletişimi ve Merkle Ağaçları

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Gelişmiş Düğüm İletişimi ve Ayrılmış Tanık

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Son Bölüm


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Yorumlar & Derecelendirmeler


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Sonuç


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
