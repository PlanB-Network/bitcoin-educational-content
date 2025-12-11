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

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Bitcoin Uygulaması için Matematik

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Eliptik Eğri Kriptografisi

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin İşlem İç Çalışmaları

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin İşlem Ayrıştırma ve ECDSA İmzaları

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Komut Dosyası ve İşlem Doğrulama

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## İşlem Oluşturma ve Senaryoya Ödeme Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Ağ İç Çalışmaları

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin Blokları ve Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Ağ İletişimi ve Merkle Ağaçları

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Gelişmiş Düğüm İletişimi ve Ayrılmış Tanık

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Son Bölüm


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Yorumlar & Derecelendirmeler


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Sonuç


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
