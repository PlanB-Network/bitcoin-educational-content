---
name: Lightning Network Daemon (Linux)
description: Linux üzerinde Lightning Network Daemon'i yükleme ve çalıştırma
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network, Bitcoin'ün ikinci bir Layer'üdür ve özellikle sunduğu işlemlerin hızı ve düşük maliyeti sayesinde yıldırım boyutlarına ulaşmasını sağlar.



Bu eğitimde, Lightning Network Daemon uygulamasını Linux makinemize (Ubuntu 24.04 dağıtımı) kuracağız.



## Lightning Network Daemon nedir?



Lightning Network Daemon, Lightning Network'in eksiksiz bir Go uygulamasıdır. Lightning Labs tarafından oluşturulmuştur ve makinenizde bir Lightning düğümünün tam bir örneğini çalıştırmanıza olanak tanır.


Başka bir deyişle, bu uygulama ile, :





- Lightning Network** ile etkileşim kurun: Doğrudan makine terminalinizden Lightning cüzdanları oluşturmak, ödeme kanallarını ve rotalarını yönetmek ve çok daha fazlasını yapmak için komut satırlarını kullanabilirsiniz.
- Uzak bir Bitcoin düğümünü veya kendi Bitcoin core örneğinizi bağlama**: LND, bir Bitcoin örneğini bağlamanıza ve onu arka uç olarak kullanmanıza olanak tanır. Bu uygulamayı kullanmak için makinenizde bir Bitcoin core örneği çalıştırmanıza gerek yoktur.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Neden kendi Lightning düğümünüz var?


Lightning, transfer sürecini optimize eden ve işlem maliyetlerini azaltan bir Bitcoin kaplamasıdır.



Lightning düğümünüzü döndürerek egemenlik ve özerklik kazanırsınız. Fonlarınızın kontrolü sizde, bu yüzden aklınızda bulundurun:



"Ne anahtarlarınız, ne de bitcoinleriniz."



Bu anlamda, bir Lightning düğümü çalıştırmak verilerinizin güvenliğini ve bütünlüğünü aşağıdaki şekillerde artırır:





- Tam kontrol**: Kendi ödeme kanallarınızı yönetin, kendi bankanız olun ve varlıklarınızın efendisi olun.
- Gizlilik**: Gizliliğinizi korumak için üçüncü taraflara güvenmeden işlem yapın.
- Öğrenme ve özerklik**: Lncli` komutları sayesinde, terminalinizden kendiniz uygulayarak Lightning'in altında yatan süreçleri daha iyi anlayabilirsiniz.
- Adem-i Merkeziyetçilik**: Bitcoin / Lightning Network'ün güçlendirilmesi ve ademi merkezileştirilmesinde aktif rol oynayın.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Makinemizde LND uygulamasının bir örneğini çalıştırmak için iki seçeneğiniz vardır. Ortamı kendi makinemizde yerel olarak çalışacak şekilde kurabilir ya da LND'yı bir Docker konteynerinden yükleyebiliriz. Burada ilk seçeneğe odaklanacağız ve Docker ile nasıl ilerleyeceğimizi daha sonraki bir eğitimde göreceğiz.


## LND'yi kaynak kodundan yükleyin



### Ön Koşullar


LND Go dilinde yazıldığından, Linux makinenizde GoLang ortamına ve gerekli bağımlılıklara sahip olduğunuzdan emin olmanız gerekir.





- Donanım gereksinimleri:**


Sorunsuz ve sorunsuz bir deneyim için, makinenizin LND Lightning düğümünüzü çalıştırmak için gerekli kapasiteye sahip olması gerekir.



İhtiyacınız olacak :


1. *optimum akışkanlık için *8 GB RAM**,


2. **Düğümünüzün eylemlerini verimli bir şekilde yönetmek için çok çekirdekli bir işlemci (dört çekirdekli veya daha fazla)**,


3. **pruned düğüm modu için en az 5GB disk alanı** ve Bitcoin core'yi çalıştırmak için 1TB (uzak bir düğüm kullanılıyorsa isteğe bağlı)





- Yararlı bağımlılıkları yükleyin:**


Aşağıdaki komut, LND'yi çalıştırmak için ihtiyacınız olan araçları makinenize yüklemenizi sağlayacaktır. Diğer şeylerin yanı sıra, bir sürüm oluşturma aracı olan `Git`i ve LND uygulamasını kaynak koddan çalıştırabilen ve derleyebilen `make`yi yüklemeniz gerekecektir.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Linux makinenize GoLang yükleyin**



Bu eğitimin yayınlandığı tarih itibariyle, LND kurulum için Go***'un 1.23.6 sürümünü gerektirmektedir.



Önceki bir sürümü zaten yüklediyseniz, yeni Go kurulumu için onu kaldırın.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Go** ortam yapılandırması


Go'yu Linux sisteminize eklemek için `~/.bashrc` dosyanızda aşağıdaki ortam değişkenlerini başlatın.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Kurulumun kontrol edilmesi** (Fransızca)


```bash
go version
```



![go-version](assets/fr/03.webp)


### LND GitHub deposunu klonlayın



Makinenizde yerel olarak LND kaynak kodunun bir kopyasını almak için git'i kullanın


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Oluşturun ve kurun



Daha önce yüklenmiş olan `make` aracı, LND kaynak kodundan bir çalıştırılabilir dosya oluşturmanızı ve kurulumunuza devam etmenizi sağlayacaktır.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Makinenize LND'yi yükleyin



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Kurulumunuzu kontrol etme** (Fransızca)



Her şeyin yolunda gittiğinden emin olmak için bu komutu çalıştırdığınızda şu anda çalıştırmakta olduğunuz LND sürümünü öğrenebilirsiniz.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Bakım ve yükseltmeler



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **ÖNEMLİ**: LND güncellemeleri Go'nun daha yeni sürümlerini gerektirebilir, bu nedenle kurulum sırasında bağımlılık sorunlarından kaçınmak için sisteminizi güncellediğinizden emin olun.


### Lightning Network Daemon'un Yapılandırılması



Bir Lightning LND düğümünün yapılandırması Bitcoin'inkine benzer ve düğümünüzün tüm parametrelerini içeren bir yapılandırma dosyasında gerçekleştirilir. Bunu yapmak için, makinenizin kök dizininde gizli bir `.LND` klasörü oluşturabilir ve ardından bu klasörde `LND.conf` yapılandırma dosyanızı oluşturabilirsiniz.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





Yapılandırma dosyasında LND düğümünüzü ayarlayabilirsiniz.



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## Yapılandırmanızı anlama



LND düğümünüzün doğru ve eksiksiz kurulumu için ihtiyacınız olan minimum yapılandırmayı anlamanız önemlidir.



~/.LND/LND.conf` dosyasının içeriğine dayanarak, alanların ayrıntıları aşağıda verilmiştir:





- noseedbackup**: LND'nın cüzdanlarınızın otomatik yedeklemelerini gerçekleştirmesini isteyip istemediğinizi seçmenizi sağlar.  Bu özelliği `0` olarak ayarlamak, geri yükleme bilgilerini kişisel olarak seçilen güvenli bir konuma manuel olarak kaydetmenize olanak tanır.





- debuglevel**: Bir eylem sırasında hata oluşması durumunda hataların ve günlüklerin ayrıntı düzeyini tanımlamanızı sağlar.





- Bitcoin.active**: LND'e bir Bitcoin düğümü olarak çalışması ve Bitcoin ağıyla etkileşime girmesi talimatını verir.





- Bitcoin.Mainnet**: LND'nin Bitcoin'ın ana ağına (Mainnet) bağlanmasını belirtir, Bitcoin Signet ve Bitcoin Regtest ağları için sırasıyla `bitcoind.signet` ve `bitcoind.regtest` değerlerini ayarlayabilirsiniz





- Bitcoin.node**: LND'ün bağlanması gereken Bitcoin düğümünün türünü belirtir.





- Bitcoin.rpcuser** ve **Bitcoin.rpcpassword** : Temsil eder.


gW-46 düğümünüze bağlanmak için sırasıyla oturum açma bilgileri (kullanıcı, parola)





- bitcoind.zmqpubrawblock** ve **bitcoind.zmqpubrawtx**: sırasıyla Bitcoin ağındaki yeni bloklar ve işlemler hakkında bildirim almak için ZeroMQ uç noktalarını tanımlar.




## LND ile kurulumunuzu kontrol etme



Muhtemelen işlemin başarılı olduğundan ve düğüm bilgilerinizi güncel tutmak için Lightning Network ile senkronizasyon yaptığınızdan emin olmak isteyeceksiniz.



LND uygulamasını başlatmak ve düğümünüz hakkında bilgi almak için komutu yazmanız yeterlidir:


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## LND üzerinde eylemler gerçekleştirme



Kurulumunuz tamamlandıktan ve kontrol edildikten sonra kullanmaya başlayabilirsiniz.


İşte başlamanız için gerekli komutlar.



### Bir Wallet oluşturun


Lightning Wallet'ünüz, fonlarınızı yönetmeye yönelik her türlü eylemin ilk adımıdır.



⚠️ **ÖNEMLI**: 24 kelimelik **seed cümlenizi** dikkatlice not alın. Sorun çıkması durumunda fonlarınızı geri almak için buna ihtiyacınız olacak.



Ayrıca Wallet parolanızı kaydedin, böylece LND düğümünüzü yeniden başlattığınızda `lncli unlock` komutuyla kilidini açabilirsiniz.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Bakiyenizi kontrol edin



Hesaplarınıza doğrudan terminalinizden bakın:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Düğümünüz hakkında bilgi



Düğümünüzde hangi kanalların etkin olduğunu öğrenmek için aşağıdaki komutu kullanın.



```bash
lncli listchannels
```



Ayrıca bağlı olduğunuz düğümlerin bir listesini de edinebilirsiniz.



```bash
lncli listpeers
```



### Kanal yönetimi



Lightning kanalı, Lightning Network** üzerindeki başka bir düğümle **doğrudan, çift çift bağlantı kurmanızı sağlar. Bu kanalda, kanalın kapasitesine kadar Exchange Satoshileri serbestçe kullanabilirsiniz.



### Bir düğüme bağlanma



Lightning'in gücüne aktif olarak katılmak ve bu güçten faydalanmak istiyorsanız diğer Lightning düğümlerine bağlanmak temel bir eylemdir.



Bir eşe (Lightning düğümü) bağlanmak için üç parça bilgiye ihtiyacınız olacaktır:




- Düğümün açık anahtarı**: Bu, düğümün Bitcoin ağındaki benzersiz tanımlayıcısıdır;
- IP** : Düğümün kurulu olduğu makinenin IP'si;
- PORT** :  Makinede açık olan ve bu düğümle iletişime izin veren bağlantı noktası.



Lightning düğümleri hakkındaki bilgileri listeleyen bir platform olan [amboss](https://amboss.space/) adresinde bağlanmak için düğümler bulabilirsiniz.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Kendi sisteminizin bütünlüğünü korumak için **güvenilir düğümlere** bağlandığınızdan emin olun. İşte doğru bağlantıları seçmek için bazı öneriler.





- Coğrafi çeşitlendirme**: Farklı bölgelerdeki düğümlere bağlanın.





- İtibar**: Kullanılabilirliği iyi olan düğümleri seçin.





- Kapasite**: Likiditesi iyi olan düğümleri seçin.





- Ücretler**: Çek yönlendirme ücretleri.


### Bir ödeme kanalı açın


Bir ödeme kanalı açmak için, eş düğüme **bağlı** olduğunuzdan emin olun, ardından bu kanalda bloke etmek istediğiniz **kapasiteyi** (satoshi miktarı) tanımlayın.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Bir Yıldırım Invoice oluşturun



Bir Lightning Invoice, Lightning Wallet'ünüzde satoshis alma isteğinizi ifade eden bir karakter dizisini temsil eder.


Kendi düğümünüzle Lightning faturaları oluşturmak, verilerinizi (coğrafi ve kişisel) korumanıza olanak tanır ve fonlarınızın yönetimi üzerinde size %100 özerklik sağlar.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Yıldırım Invoice Ödemesi



```bash
lncli payinvoice <FACTURE>
```


### Bir kanalı kapatın



Mevcut düğümünüzdeki aktif bir kanalı kapatmanın iki yolu vardır.





- Kooperatif kapanışı**: Bu, node'unuzun ödeme kanalından çekilme isteğini bildirerek devam eden görevlerin tamamlanmasını ve fon kaybını önlemek için verilerin yedeklenmesini sağlar.


```
lncli closechannel <ID_CANAL>
```




- Zorla kapatma**: ⚠️ Mümkünse kaçınılması gereken bu eylem, ödeme kanalınızda devam eden süreçleri kesintiye uğratır ve fon kaybı riskini artırır.


```
lncli closechannel --force <ID_CANAL>
```


## LND düğümünüz için en iyi uygulamalar ve güvenlik.


Bir Bitcoin/ Lightning düğümü kullanırken güvenlik çok önemlidir. İşte kurulumunuzun güvenliğini güçlendirmek için birkaç nokta:





- seed ifadenizi güvenli, çevrim dışı bir yerde saklayın.





- ~/.LND/channel.backup` dosyasını düzenli olarak yedekleyin: Bu dosya, düğümünüzde her yeni kanal açıldığında (veya eski bir kanal kapatıldığında) kanal durumlarınızı kaydeder.


⚠️ Veri kaybı veya düğüm arızası durumunda kanalları geri yüklemenizi ve ödeme kanallarında bloke edilen fonları kurtarmanızı sağlar



Bu dosyanın yedekleme yolunu belirterek aşağıdaki komutla fonlarınızı geri yükleyebilirsiniz:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Lightning Wallet'unuzun geri yükleme sözcüklerini ve parolasını kaydettiğinizden emin olun.
- Sisteminizi güncel tutun.



## Güncel sorun giderme


### Sık karşılaşılan sorunlar




- bitcoind bağlantı hatası** : RPC giriş bilgilerinizi kontrol edin
- Senkronizasyon engellendi** : İnternet bağlantınızı kontrol edin
- İzin hatası**: ~/.LND` klasörünün haklarını kontrol edin




Bu eğitimin sonuna geldiniz. Lightning hakkında daha fazla bilgi edinmek isterseniz, Lightning Network'ün arkasındaki kavramları ve uygulamaları daha iyi anlamanızı sağlamak için bu giriş kursunu sunuyoruz.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb