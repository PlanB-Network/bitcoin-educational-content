---
name: Graylog
description: Günlüklerinizi kolayca merkezileştirin ve analiz edin
---
![cover](assets/cover.webp)



___



*Bu eğitim Florian BURNEL tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal metinde değişiklikler yapılmış olabilir.*



___



## Graylog'u Debian 12 üzerinde dağıtma



### I. Sunum



Graylog, makinelerinizden ve ağ cihazlarınızdan gelen günlükleri gerçek zamanlı olarak merkezileştirmek, depolamak ve analiz etmek için tasarlanmış açık kaynaklı bir "log sink" çözümüdür. Bu eğitimde, Graylog'un ücretsiz sürümünü bir Debian 12 makinesine nasıl kuracağımızı öğreneceğiz!



Bir bilgi sistemi içinde, ister **Linux** ister **Windows** çalıştırsın, her **sunucu** ve her **ağ cihazı** (anahtar, yönlendirici, güvenlik duvarı, vb...) **yerel olarak depolanan kendi günlüklerini** oluşturur. Her makinede yerel olarak depolanan günlüklerle, olay analizi ve korelasyon çok zordur ... İşte **Graylog** burada devreye girer. Graylog bir **log lavabosu** olarak hareket eder, yani **tüm makineleriniz ona kendi loglarını** gönderir (örneğin syslog aracılığıyla). Graylog daha sonra **bu günlükleri depolayacak ve indeksleyecek**, aynı zamanda küresel aramalar yapmanıza ve uyarılar oluşturmanıza olanak tanıyacaktır.



Graylog, şüpheli davranışları ve çeşitli sorunları (kararlılık, performans vb.) belirlemeyi kolaylaştıran bir analiz ve izleme aracıdır.




![Image](assets/fr/034.webp)



**Not: Ücretsiz sürüm olan **Graylog Open**, Wazuh gibi bir SIEM değildir, özellikle de gerçek saldırı tespit işlevlerinden yoksundur.



### II. Ön Koşullar



Stack Graylog**, kurmamız ve yapılandırmamız gereken **birkaç bileşene** dayanmaktadır. Burada, tüm bileşenleri aynı sunucuya kuracağız, ancak birkaç düğüme dayalı kümeler oluşturmak ve rolleri birkaç sunucuya dağıtmak mümkündür. Bu eğitimin amaçları doğrultusunda, bugüne kadarki en yeni sürüm olan **Graylog 6.1**'i kuracağız.





- Graylog için önerilen güncel sürüm olan MongoDB 7** (minimum 5.0.7, maksimum 7.x)
- OpenSearch**, Amazon tarafından oluşturulan Elasticsearch'ün açık kaynaklı bir Fork'ı (minimum 1.1.x, maksimum 2.15.x)
- OpenJDK 17**



Graylog sunucusu** **Debian 12** üzerinde çalışmaktadır, ancak Docker aracılığıyla da dahil olmak üzere diğer dağıtımlara kurulum mümkündür. Sanal makine, tüm bileşenler için yeterli kaynağa sahip olmak amacıyla **8 GB RAM** ve **256 GB disk alanı** ile donatılmıştır (aksi takdirde bu performans üzerinde önemli bir etkiye sahip olabilir). Ancak, bunu kaba bir kılavuz olarak veriyorum, çünkü **Graylog mimarisinin boyutlandırılması işlenecek bilgi miktarına bağlıdır**. Graylog günde 30 MB ya da 300 MB veri işleyebileceği gibi günde 300 GB veri de işleyebilir... Bu, **terabaytlarca günlüğü** işleyebilen **ölçeklenebilir bir çözümdür** (bkz. [bu sayfa](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Kaynak: Graylog



Yapılandırmaya başlamadan önce Graylog makinesine statik bir IP Address atayın ve en son güncellemeleri yükleyin. Yerel makinenin saat dilimini ayarladığınızdan ve tarih ve saat senkronizasyonu için bir NTP sunucusu tanımladığınızdan emin olun. İşte çalıştırılacak komut:



```
sudo timedatectl set-timezone Europe/Paris
```



**Not: Bunun yerine **Graylog Data Node** kullanıyorsanız **OpenSearch kurulumu isteğe bağlıdır**.



### III Graylog'un adım adım kurulumu



Paket önbelleğini güncelleyerek ve gelecek için ihtiyacımız olan araçları yükleyerek başlayalım.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. MongoDB'yi Yükleme



Bu işlem tamamlandıktan sonra MongoDB'yi kurmaya başlayacağız. MongoDB deposuna karşılık gelen GPG anahtarını indirin:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Ardından MongoDB 6 deposunu Debian 12 makinesine ekleyin:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Ardından, paket önbelleğini güncelleyeceğiz ve MongoDB'yi yüklemeye çalışacağız:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



Bir bağımlılık eksik olduğu için MongoDB yüklenemiyor: **libssl1.1**. Debian 12'nin depolarında bulunmadığı için devam etmeden önce bu paketi manuel olarak yüklememiz gerekecek.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



"**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (son sürüm) isimli DEB paketini **wget** komutu ile indireceğiz, ardından **dpkg** komutu ile kuracağız. Bu aşağıdaki iki komutu üretir:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



MongoDB kurulumunu yeniden başlatın:



```
sudo apt-get install -y mongodb-org
```



Ardından MongoDB hizmetini yeniden başlatın ve Debian sunucusu başlatıldığında otomatik olarak başlamasını sağlayın.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



MongoDB kurulduktan sonra bir sonraki bileşeni kurmaya geçebiliriz.



#### B. OpenSearch'ü Yükleme



OpenSearch'ü sunucuya yüklemeye devam edelim. Aşağıdaki komut OpenSearch paketleri için imza anahtarı ekler:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Ardından OpenSearch deposunu ekleyin, böylece daha sonra **apt** ile paketi indirebiliriz:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Paket önbelleğinizi güncelleyin:



```
sudo apt-get update
```



Ardından **OpenSearch'ü** yükleyin ve örneğinizin Admin** hesabı için varsayılan parolayı tanımlamaya özen gösterin. Burada parola "**IT-Connect2024!**" şeklindedir, ancak bu değeri güçlü bir parola ile değiştirin. **"**P@ssword123**" gibi zayıf parolalardan** kaçının ve her türden (küçük harf, büyük harf, sayı ve özel karakter) en az bir karakter içeren en az **8 karakter** kullanın, aksi takdirde kurulumun sonunda bir hata olacaktır. **Bu, OpenSearch 2.12.**'den beri bir önkoşuldur



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Lütfen kurulum sırasında sabırlı olun...



İşiniz bittiğinde, minimum yapılandırmayı gerçekleştirmek için bir dakikanızı ayırın. YAML formatındaki yapılandırma dosyasını açın:



```
sudo nano /etc/opensearch/opensearch.yml
```



Dosya açıkken, aşağıdaki seçenekleri ayarlayın:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Bu OpenSearch yapılandırması tek bir düğüm kurmak için tasarlanmıştır. İşte kullandığımız farklı parametrelerin bazı açıklamaları:





- cluster.name: graylog**: bu parametre OpenSearch kümesini "**graylog**" adıyla adlandırır.
- node.name: ${HOSTNAME}**: düğüm adı dinamik olarak yerel Linux makinesininkiyle eşleşecek şekilde ayarlanır. Sadece bir node'umuz olsa bile, onu doğru şekilde adlandırmak önemlidir.
- path.data: /var/lib/opensearch**: bu yol OpenSearch'ün verilerini yerel makinede nerede sakladığını belirtir, bu durumda "**/var/lib/opensearch**" içinde.
- path.logs: /var/log/opensearch**: bu yol OpenSearch günlük dosyalarının nerede saklanacağını tanımlar, burada "**/var/log/opensearch**".
- discovery.type: single-node**: bu parametre OpenSearch'ü tek bir düğümle çalışacak şekilde yapılandırır, dolayısıyla "**single-node**" seçeneği tercih edilir.
- network.host: 127.0.0.1**: bu yapılandırma OpenSearch'ün yalnızca Interface yerel döngüsünü dinlemesini sağlar, bu da Graylog ile aynı sunucuda olduğu için yeterlidir.
- action.auto_create_index: false**: otomatik dizin oluşturmayı devre dışı bırakarak, mevcut bir dizin olmadan bir belge gönderildiğinde OpenSearch otomatik olarak bir dizin oluşturmayacaktır.
- plugins.security.disabled: true**: bu seçenek OpenSearch güvenlik eklentisini devre dışı bırakır, yani kimlik doğrulama, erişim yönetimi veya iletişim şifrelemesi olmayacaktır. Bu ayar Graylog'u kurarken zaman kazandırır, ancak üretimde kaçınılmalıdır (bkz. [bu sayfa](https://opensearch.org/docs/1.0/security-plugin/index/)).



Bazı seçenekler zaten mevcuttur, bu nedenle bunları etkinleştirmek için "#" işaretini kaldırmanız ve ardından değerinizi belirtmeniz yeterlidir. Bir seçenek bulamazsanız, bunu doğrudan dosyanın sonunda bildirebilirsiniz.



![Image](assets/fr/023.webp)



Bu dosyayı kaydedin ve kapatın.



#### C. Java'yı (JVM) Yapılandırma



Bu hizmetin kullanabileceği bellek miktarını ayarlamak için OpenSearch tarafından kullanılan Java Sanal Makinesini yapılandırmanız gerekir. Aşağıdaki yapılandırma dosyasını düzenleyin:



```
sudo nano /etc/opensearch/jvm.options
```



Burada dağıtılan yapılandırma ile **OpenSearch 4 GB ayrılmış bellekle başlar ve 4 GB'a kadar büyüyebilir**, böylece çalışma sırasında bellek değişimi olmaz. Burada yapılandırma, sanal makinenin toplam **8 GB RAM'e** sahip olduğu gerçeğini dikkate alır. Her iki parametre de aynı değere sahip olmalıdır. Bu, satırların değiştirilmesi anlamına gelir:



```
-Xms1g
-Xmx1g
```



Bu satırlarla:



```
-Xms4g
-Xmx4g
```



İşte yapılacak değişikliğin bir görüntüsü:



![Image](assets/fr/022.webp)



Kaydettikten sonra bu dosyayı kapatın.



Ek olarak, Linux çekirdeğindeki "**max_map_count**" parametresinin yapılandırmasını kontrol etmemiz gerekir. Uygulamamızın ihtiyaçlarını karşılamak için işlem başına eşlenen bellek alanlarının sınırını tanımlar. *elasticsearch** gibi *OpenSearch** de bellek yönetimi hatalarını önlemek için bu değerin "262144" olarak ayarlanmasını önerir.



Prensip olarak, yeni kurulmuş bir Debian 12 makinesinde değer zaten doğrudur. Ama kontrol edelim. Bu komutu çalıştırın:



```
cat /proc/sys/vm/max_map_count
```



"**262144**" dışında bir değer alırsanız, aşağıdaki komutu çalıştırın, aksi takdirde gerekli değildir.



```
sudo sysctl -w vm.max_map_count=262144
```



Son olarak, OpenSearch otomatik başlatmayı etkinleştirin ve ilgili hizmeti başlatın.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Sistem durumunuzu görüntülerseniz, 4 GB RAM'e sahip bir Java işlemi görmeniz gerekir.



```
top
```



![Image](assets/fr/029.webp)



Bir sonraki adım: Graylog'un uzun zamandır beklenen kurulumu!



#### D. Graylog'u Yükleme



Graylog 6.1**'i en son sürümünde **kurmak için, aşağıdaki 4 komutu çalıştırarak **Graylog Sunucusunu** indirin ve kurun:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Bu yapıldığında, Graylog'u başlatmaya çalışmadan önce yapılandırmasında bazı değişiklikler yapmamız gerekir.



Bu iki seçeneği yapılandırarak başlayalım:





- password_secret**: bu parametre Graylog tarafından kullanıcı parolalarının saklanmasını güvence altına almak için kullanılan bir anahtar tanımlamak için kullanılır (tuzlama anahtarı ruhunda). Bu anahtar **tek** ve **rastgele** olmalıdır.
- root_password_sha2**: bu parametre Graylog'daki varsayılan yönetici parolasına karşılık gelir. Hash SHA-256 olarak saklanır.



İşe **password_secret** parametresi için 96 karakterlik bir anahtar oluşturarak başlayacağız:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Dönen değeri kopyalayın, ardından Graylog yapılandırma dosyasını açın:



```
sudo nano /etc/graylog/server/server.conf
```



Anahtarı **password_secret** parametresine aşağıdaki gibi yapıştırın:



![Image](assets/fr/027.webp)



Dosyayı kaydedin ve kapatın.



Ardından, varsayılan olarak oluşturulan "**admin**" hesabı için parolayı ayarlamanız gerekir. Yapılandırma dosyasında, parolanın Hash'ü saklanmalıdır, yani hesaplanmalıdır. Aşağıdaki örnek "**LogsWells@**" parolasının Hash değerini vermektedir: değeri kendi parolanıza uyarlayın.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Elde edilen değeri çıktı olarak kopyalayın (satırın sonunda tire işareti olmadan).



Graylog yapılandırma dosyasını tekrar açın:



```
sudo nano /etc/graylog/server/server.conf
```



Değeri **root_password_sha2** seçeneğine aşağıdaki gibi yapıştırın:



![Image](assets/fr/026.webp)



Yapılandırma dosyasındayken, "**http_bind_address**" seçeneğini ayarlayın. Graylog'un Interface web'ine herhangi bir sunucu IP Address üzerinden **9000** portundan erişilebilmesi için "**0.0.0.0:9000**" belirtin.



![Image](assets/fr/024.webp)



Ardından yerel OpenSearch örneğimizi bildirmek için "**elasticsearch_hosts**" seçeneğini `http://127.0.0.1:9200` olarak ayarlayın. Bir **Graylog Data Node** kullanmadığımız için bu gereklidir. Ve bu seçenek olmadan, daha ileri gitmek mümkün olmayacaktır...



![Image](assets/fr/025.webp)



Dosyayı kaydedin ve kapatın.



Bu komut Graylog'u bir sonraki açılışta otomatik olarak başlayacak şekilde etkinleştirir ve hemen Graylog sunucusunu başlatır.



```
sudo systemctl enable --now graylog-server
```



Bu yapıldıktan sonra, bir tarayıcıdan Graylog'a bağlanmayı deneyin. Sunucunun IP Address'sini (veya adını) ve port 9000'i girin.



**Bilginize:**



Çok uzun zaman önce, Graylog'a ilk kez giriş yaptığınızda aşağıdakine benzer bir kimlik doğrulama penceresi görünürdü. "**admin**" kullanıcı adınızı ve şifrenizi girmeniz gerekiyordu. Ve sonra bağlantının çalışmadığını görünce hoş olmayan bir sürprizle karşılaşırdınız.



![Image](assets/fr/031.webp)



Graylog sunucusundaki komut satırına geri dönmek ve günlüklere bakmak gerekiyordu. Daha sonra **ilk bağlantı** için, günlüklerde belirtilen **geçici bir parola** kullanılması gerektiğini görebildik.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Daha sonra "**admin**" kullanıcısı ve geçici parola ile yeniden bağlantı kurmanız gerekiyordu ve bu da oturum açmanıza izin veriyordu!



**Bu artık geçerli değil. Tek yapmanız gereken yönetici hesabınızla ve komut satırında yapılandırılan parolayla oturum açmaktır



![Image](assets/fr/033.webp)



**Graylog'un Interface'ine hoş geldiniz!



![Image](assets/fr/019.webp)



#### E. Graylog: yeni bir yönetici hesabı oluşturun



Graylog tarafından yerel olarak oluşturulan yönetici hesabını kullanmak yerine, kendi kişisel yönetici hesabınızı oluşturabilirsiniz. "**Sistem**" menüsüne ve ardından "**Kullanıcılar ve Ekipler**" menüsüne tıklayarak "**Kullanıcı oluştur**" butonuna tıklayın. Ardından formu doldurun ve hesabınıza yönetici rolü atayın.



![Image](assets/fr/020.webp)



Kişiselleştirilmiş bir hesap, yerel bir yönetici hesabından farklı olarak ad, soyad ve e-posta Address gibi ek bilgiler içerebilir. Dahası, bu, her kişi adlandırılmış bir hesapla çalıştığında daha iyi izlenebilirlik sağlar.



## Günlükleri rsyslog ile Graylog'a gönderme



### I. Sunum



Bu ikinci bölümde, bir Linux makinesini günlüklerini Graylog sunucusuna gönderecek şekilde nasıl yapılandıracağımızı öğreneceğiz. Bunu yapmak için, Rsyslog'u sisteme kuracak ve yapılandıracağız.



### II. Linux günlüklerini almak için Graylog'u yapılandırma



Graylog'u yapılandırarak başlayacağız. Tamamlanması gereken üç adım var:





- Linux makinelerinin **Syslog günlüklerini UDP** üzerinden göndermesine izin veren bir giriş noktası oluşturmak için bir **Giriş** oluşturulması.
- Tüm Linux günlüklerini depolamak ve **indekslemek** için yeni bir **Index** oluşturulması.
- Graylog tarafından alınan günlükleri yeni Linux Dizinine **yönlendirmek** için bir **Akış** oluşturulması.



#### A. Syslog için Girdi Oluşturma



Graylog Interface'da oturum açın, menüde "**Sistem**" ve ardından "**Girişler**" üzerine tıklayın. Açılır listeden "**Syslog UDP**"yi seçin ve ardından "**Yeni girdi başlat**" etiketli düğmeye tıklayın. Bir TCP Syslog Girişi oluşturmak da mümkündür, ancak bu bir TLS sertifikasının kullanılmasını gerektirir: güvenlik için bir artıdır, ancak bu makalede ele alınmamıştır.



![Image](assets/fr/001.webp)



Ekranda bir sihirbaz görünecektir. Bu Girdiye bir ad vererek başlayın, örneğin "**Graylog_UDP_Rsyslog_Linux**" ve bir bağlantı noktası seçin. Varsayılan olarak bağlantı noktası "**514**"tür, ancak bunu özelleştirebilirsiniz. Burada, "**12514**" bağlantı noktası seçilmiştir.



![Image](assets/fr/016.webp)



Tam günlük mesajını Graylog'da saklamak için "**Tam mesajı sakla**" seçeneğini de işaretleyebilirsiniz. "**Girişi Başlat**" üzerine tıklayın.



![Image](assets/fr/017.webp)



Yeni Giriş oluşturuldu ve şimdi aktif. Graylog artık 12514/UDP bağlantı noktasından Syslog günlüklerini alabilir, ancak uygulamayı yapılandırmayı henüz bitirmedik.



![Image](assets/fr/018.webp)


**Not: Tek bir Giriş, birden fazla Linux makinesinden gelen günlükleri depolamak için kullanılabilir.



#### B. Yeni bir Linux Dizini oluşturun



Linux makinelerden gelen logları saklamak için Graylog'da bir Index oluşturmamız gerekiyor. Graylog'daki bir **index**, alınan günlükleri, yani alınan mesajları içeren bir depolama yapısıdır. Graylog, depolama motoru olarak OpenSearch kullanır ve mesajlar hızlı, verimli aramalara olanak sağlamak için dizine eklenir.



Graylog'dan, menüde "**Sistem**" üzerine, ardından "**Dizinler**" üzerine tıklayın. Açılan yeni sayfada "**İndeks seti oluştur**" seçeneğine tıklayın.



![Image](assets/fr/005.webp)



Bu dizini adlandırın, örneğin "**Linux Dizini**", onaylamadan önce bir açıklama ve bir önek ekleyin. Burada, **tüm Linux günlüklerini bu dizinde** depolayacağız. Yalnızca belirli günlükleri depolamak için özel dizinler oluşturmak da mümkündür (yalnızca [SSH] günlükleri (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), Web hizmeti günlükleri vb.)



![Image](assets/fr/006.webp)



Şimdi mesajları bu dizine yönlendirmek için yeni bir akış oluşturmamız gerekiyor.



#### C. Bir Akış Oluşturun



Yeni bir akış oluşturmak için Graylog'un ana menüsündeki "**Akışlar**" seçeneğine tıklayın. Ardından sağdaki "**Akış oluştur**" düğmesine tıklayın. Görünen pencerede akışı adlandırın, örneğin "**Linux Stream**" ve "**Index Set**" adlı alan için "**Linux Index**" indeksini seçin. Seçiminizi onaylayın.



**Not: "**Remove matches from 'Default Stream'**" seçeneğini işaretlemediğiniz sürece, bu akışa karşılık gelen mesajlar da "**Default Stream**"e dahil edilecektir.



![Image](assets/fr/002.webp)



Ardından, steam ayarlarınızda, yeni bir mesaj yönlendirme kuralı eklemek için "**Akış kuralı ekle**" düğmesine tıklayın. Bu pencereyi bulamazsanız, menüden "**Akışlar**" üzerine tıklayın, ardından akışınıza karşılık gelen satırda "**Daha Fazla**" ve ardından "**Kuralları Yönet**" üzerine tıklayın.



"**match input**" tipini seçin ve önceden oluşturulmuş **Rsyslog input in UDP**'yi seçin. "**Kural Oluştur**" düğmesi ile onaylayın. Yeni Girdimize gelen tüm mesajlar artık Linux için Dizin'e gönderilecektir.



![Image](assets/fr/003.webp)



Yeni Akışınız listede görünmeli ve "**Çalışıyor**" durumunda olmalıdır. Şu anda Rsyslog UDP girişine herhangi bir günlük göndermediğimiz için mesaj bant genişliği "**0 msg/s**" gösterir. Bir akışın günlüklerini görüntülemek için adına tıklamanız yeterlidir.



![Image](assets/fr/004.webp)



**Graylog tarafında her şey hazır**. Bir sonraki adım Linux makinesini yapılandırmaktır.



### III. Linux'ta Rsyslog'un Kurulması ve Yapılandırılması



Yerel veya uzaktan Linux makinesinde oturum açın ve ayrıcalıklarını yükseltmek için izinlere sahip bir kullanıcı hesabı kullanın (sudo aracılığıyla). Aksi takdirde, doğrudan "root" hesabını kullanın.



#### A. Rsyslog paketinin yüklenmesi



Paket önbelleğini güncelleyerek ve "**rsyslog**" adlı paketi yükleyerek başlayın.



```
sudo apt-get update
sudo apt-get install rsyslog
```



Ardından hizmet durumunu kontrol edin. Çoğu durumda zaten çalışıyordur.



```
sudo systemctl status rsyslog
```



#### B. Rsyslog'u Yapılandırma



Rsyslog'un burada bulunan bir ana yapılandırma dosyası vardır:



```
/etc/rsyslog.conf
```



Ek olarak, "**/etc/rsyslog.d/**" dizini Rsyslog için ek yapılandırma dosyalarını saklamak için kullanılır. Ana yapılandırma dosyasında, bu dizinde bulunan tüm "**.conf**" dosyalarını içe aktarmak için bir Include yönergesi vardır. Bu, ana dosyayı değiştirmeden Rsyslog'u yapılandırmak için ek dosyalara sahip olmayı mümkün kılar.



Bu dizinde, dosyalar alfabetik sırayla yüklendiğinden, yükleme sırasını tanımlamak için sayılar kullanmanız gerekir. Sayısal bir önek eklemek, birkaç yapılandırma dosyası arasındaki önceliği yönetmenize olanak tanır. Burada sadece bir ek dosyamız var, bu yüzden sorun değil.



Bu dizinde "**10-graylog.conf**" adında bir dosya oluşturacağız:



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Bu dosyaya şu satırı ekleyin:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



İşte bu satırı nasıl yorumlayacağınız:





- `*.*`: Linux makinesindeki tüm Syslog günlüklerini Graylog'a göndermek anlamına gelir.
- `@`: aktarımın UDP'de gerçekleştirildiğini gösterir. TCP'ye geçmek için "**@@**" belirtmelisiniz.
- `192.168.10.220:12514`: Graylog sunucusunun Address'ini ve günlüklerin gönderildiği bağlantı noktasını (Giriş'e karşılık gelir) belirtir.
- `RSYSLOG_SyslogProtocol23Format`: Graylog'a gönderilecek mesajların formatına karşılık gelir.



İşiniz bittiğinde dosyayı kaydedin ve Rsyslog'u yeniden başlatın.



```
sudo systemctl restart rsyslog.service
```



Bu işlemin ardından, ilk mesajlar Graylog sunucunuza ulaşmalıdır!



### IV. Linux günlüklerini Graylog'da görüntüleme



Graylog'dan "**Akışlar**" üzerine tıklayabilir ve ilgili mesajları görüntülemek için yeni akışınızı seçebilirsiniz. Alternatif olarak, "**Arama**" üzerine tıklayın ve Steam'inizi seçin ve bir arama başlatın.



İşte Interface'nin bazı temel özellikleri:



**1** - Mesajların görüntüleneceği dönemi seçin. Varsayılan olarak, son 5 dakikaya ait mesajlar görüntülenir.



**2** - Görüntülenecek akış(lar)ı seçin.



**3** - Mesaj listesinin otomatik olarak yenilenmesini etkinleştirin (örneğin her 5 saniyede bir). Aksi takdirde, statik olur ve manuel olarak yenilemeniz gerekir.



**4** - Dönem, akış veya filtreyi değiştirdikten sonra aramayı başlatmak için büyütece tıklayın.



**5** - Arama filtrelerinizi belirtmek için giriş çubuğu. Burada, yalnızca Rsyslog'u yeni kurduğum yeni makinenin günlüklerini görüntülemek için "**source:srv\-docker**" belirtiyorum.



Günlükler Linux makinesi tarafından gönderilir:



![Image](assets/fr/015.webp)



### V. SSH bağlantı hatasını tanımlama



Graylog'un gücü, günlükleri indeksleme ve çeşitli kriterlere göre arama yapılmasını sağlama yeteneğinde yatmaktadır: kaynak makine, Timestamp, mesaj içeriği vb. Başarısız SSH bağlantılarını tespit etmeye çalışıyor olabiliriz.



Uzak bir makineden (örneğin Graylog sunucusu), Rsyslog'u yapılandırdığınız Linux sunucunuza bağlanmayı deneyin. Örneğin:



```
ssh [email protected]
```



Ardından **generate bağlantı hataları** için kasıtlı olarak yanlış bir **kullanıcı adı** ve **şifre** girin. Bu, "**/var/log/auth.log**" dosyasında aşağıdakine benzer generate günlük mesajları oluşturacaktır:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Bu mesajları Graylog'da bulmanız gerekir.



Graylog'da, yalnızca eşleşen mesajları görüntülemek için aşağıdaki arama filtresini kullanın:



```
message:Failed password AND application_name:sshd
```



Birden fazla sunucunuz varsa ve belirli bir sunucunun günlüklerini analiz etmek istiyorsanız, ek olarak sunucunun adını belirtin:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



İşte günün farklı saatlerinde birkaç bağlantı hatası oluşturduğum bir makinedeki sonucun genel görünümü:



![Image](assets/fr/009.webp)



Başarısız bağlantı denemeleri IP Address "**192.168.10.199**" olan makineden yapılır. Bu ana bilgisayarın etkinliği hakkında daha fazla bilgi edinmek istiyorsanız, **bu IP Address** için arama yapabilirsiniz. Graylog, bu IP Address'in referans alındığı tüm ana bilgisayarlardaki (günlük gönderimi yapılandırılmış) tüm günlüklerin çıktısını alacaktır.



Bu durumda kullanılacak filtre şu olabilir:



```
message:"192.168.10.199"
```



Ek sonuçlar alıyoruz (SSH uygulamasında filtreleme yapmadığımız için şaşırtıcı değil):



![Image](assets/fr/008.webp)



### VI. Sonuç



Bu öğreticiyi takip ederek, bir Linux makinesini günlüklerini Graylog sunucusuna gönderecek şekilde yapılandırabilirsiniz. Bu şekilde, Linux ana bilgisayarlarınızın günlüklerini günlük havuzunuzda merkezileştirebileceksiniz!



Daha da ileri gitmek için, bir anormallik tespit edildiğinde bildirim almak üzere gösterge tabloları ve uyarılar oluşturmayı düşünün.



![Image](assets/fr/007.webp)