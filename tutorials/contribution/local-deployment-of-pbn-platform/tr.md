---
name: Plan ₿ Network Platformunu Yerel Olarak Çalıştırma Kılavuzu
description: Plan ₿ Network'de içerik katkımı veya eğitim içeriğinin düzeltilmesini/incelenmesini test etmek için Plan ₿ Network'i yerel bir ortamda nasıl çalıştırabilirsiniz?
---
![github](assets/cover.webp)


## Özet olarak


Bu eğitim, Docker, sahte anahtarlar ve özel depo yapılandırmaları kullanarak yerel makinenizde Plan ₿ Network'den Bitcoin Öğrenme Yönetim Sistemini kurmak için adım adım talimatlar sağlar.


Yukarıdaki kısmı anlamadıysanız endişelenmeyin - bu eğitim sizin için!


---

## **Bitcoin Öğrenme Yönetim Sistemi Yerel Olarak Nasıl Çalıştırılır**


Bu eğitimde platformu kurmak, sahte anahtarları işlemek ve depoları özelleştirmek için ayrıntılı adımlar yer almaktadır. Sık karşılaşılan sorunlardan kaçınmak ve yerel ortamınızı düzgün bir şekilde yapılandırmak için aşağıdaki adımları izleyin.



**1. Önkoşullar**


- Docker ve Docker Compose yüklü Linux makinesi (Windows'ta da çalıştığı bildirilmiştir).
- yeterli `nodejs` sürümü (test edildi: 22.12.0)
- sisteminizde `pnpm` yüklü.
- Git, depoları klonlamak için yapılandırıldı.



**2. Depoyu Klonlayın**

Depoyu yerel makinenize klonlayın:


git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-öğrenme-yönetim-sistemi


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. Ortam Değişkenlerini Ayarlayın**


1\. .env.example` dosyasını çoğaltın:


```bash
cp .env.example .env
```


1. .env` dosyasını düzenleyin, adın .example kısmını silin, şimdi gerekli değişkenler için kukla anahtarlar eklemeniz gerekiyor. Örnek:


⚠️ Bu zorunlu bir adımdır, atlanması bazı konteynerler arasında bağlantı reddi gibi hatalara neden olacaktır.


Özel Github PAT'inizi de dosyaya eklemeyi unutmayın



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. Bağımlılıkları Yükleyin**


uygun bir nodejs sürümü yüklediğinizden `emin olun`. 2024-12 itibariyle v22.12.0 (LTS) sürümünün çalıştığı kanıtlanmıştır.



⚠️ Ubuntu 22.04 deposu nodejs sürümü 12.22.9: pnpm yüklemenize izin vermek için çok eski



Nodejs yüklemek için talimatları [burada] (https://nodejs.org/en/download/package-manager) bulabilirsiniz; örneğin `nvm` yükleme yöntemini kullanmayı seçebilirsiniz.


---

Gerekli paketlerin pnpm kurulum aşamasına başlamadan önce, tüm bağımlılıkların kurulu olduğundan emin olun, bunu aşağıdaki komutu çalıştırarak elde edebilirsiniz:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

../Bitcoin-learning-management-system/` klasörünüzün içinde, `pnpm`i yüklemek için aşağıdaki komutu çalıştırın


```bash
pnpm install
```


__TIP:__Zaman zaman hem bağımlılıkları hem de pnpm'nin kendisini güncellemeyi unutmayın



**5. Konteynerleri çalıştırın**

../Bitcoin-learning-management-system/` klasörünüzün içinde, Docker ile geliştirme ortamını başlatın:


```bash
docker compose up --build -V
```

Bir sonraki komutu da bu şekilde çalıştırırsanız, terminalinizde günlükleri görmezsiniz.

```bash
docker compose up -d --build -V
```


Bu, dockers'dan gerekli tüm konteynerleri oluşturacak ve başlatacaktır.


**6. Uygulamaya Erişim**

Konteynerler çalıştıktan sonra, ön uca şu adresten erişin:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


Not: Herhangi bir kaynak dosyayı değiştirirseniz uygulama otomatik olarak yeniden yüklenecektir.



**7.** Veritabanınızı kurun Schema


İlk çalıştırmada, DB geçişlerini çalıştırmanız gerekecektir.


Bunu yapmak için geçiş betiğini çalıştırın: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. Depodan Veri İçe Aktarma**

Verileri veritabanına aktarmak için API'ye bir istekte bulunun:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. Senkronizasyon Birimi Erişim Sorunlarını Düzeltin**

Eğer `cdn` ve `sync` birimlerinde erişim sorunları ile karşılaşırsanız, çalıştırın:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


sonra tekrar:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10. Depoyu Özelleştirme (İsteğe Bağlı)**

Bir Fork veya belirli bir şube kullanmanız gerekiyorsa:

1. Aşağıdaki değişkenleri güncellemek için `.env` dosyasını düzenleyin:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Docker'ı yeniden başlatın:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. Depo verilerini yeniden senkronize edin:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


Bu eğitim, platformun sahte anahtarlarla doğru şekilde kurulmasını, bağımlılıkların yüklenmesini ve depoların gerektiği gibi özelleştirilmesini sağlar. 🎉 Kurulumunuzda iyi şanslar!


**Ekstra yardım için komutlar**


tüm konteynerleri durdur


```
docker compose down
```


mevcut tüm konteynerleri ve hacimleri budayın


```
docker container prune -f
docker volume prune --all
```


resmi kılavuzda kullanılan aynı komutla kapsayıcıları yeniden oluşturun ve senkronizasyon betiğini başlatın:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```