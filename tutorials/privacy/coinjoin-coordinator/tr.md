---
name: Coinjoin Koordinatörü - WabiSabi
description: WabiSabi protokolünü (Wasabi Wallet 2.0'da kullanılır) takip eden bir coinjoin koordinatörü nasıl kurulur ve çalıştırılır
---

![cover](assets/cover.webp)


---

## Giriş 👋


Bu uzman kılavuzunda, işlem ücretlerinden tasarruf etmek veya ortak işlemlerde zincir içi gizliliklerini artırmak isteyen kişileri bir araya getiren bir sunucu olan bir coinjoin koordinatörü kurmanıza yardımcı olacağız. Artık Wasabi Wallet ile birlikte şirket tarafından işletilen bir koordinatör bulunmadığından, kullanıcılar kendi tercih ettikleri koordinatör sunucusunu bulmak ve seçmek zorundadır. Sadece birkaç koordinatör %0 koordinasyon ücreti talep etmektedir, bu nedenle Wasabi Wallet geliştiricileri kendi topluluk koordinatörünüzü (Raspberry Pi5 kadar küçük bir donanımda!) çalıştırmaya başlamayı mümkün olduğunca kolaylaştırmak için çok çalışmaktadır. Şu anda %0 koordinasyon ücreti talep eden aktif koordinatörler [LiquiSabi](https://liquisabi.com) ve daha da önemlisi [nostr](https://github.com/Kukks/WasabiNostr) adreslerinde bulunabilir.


## Gereksinimler 🫴



- VPS (barındırılan düğüm) veya bilgisayar/sunucu (kendi kendine barındırılan düğüm)
- Budanmış/Tam Bitcoin Çekirdek düğümü (v29.0 ile test edilmiştir)


İsteğe bağlı:


- düğüme trafik ileten (alt) Etki Alanı (örn. coinjoin.[yourdomain].io)


Tüm adımlar otomatikleştirilemeyeceğinden, komut satırı istemleri ve bash ile biraz deneyim sahibi olmanız önerilir.


Donanım açısından bir sisteme sahip olmanız tavsiye edilir:


- 4 çekirdek
- 16 GB RAM
- 2 TB SSD veya NVMe (tam düğüm için) / 128 GB SSD (pruned düğümü için)


Bu tür gereksinimler, 2 TB NVMe bellek için yaklaşık 100 $ maliyeti olan depolama hariç, sadece 120 $ karşılığında bir Raspberry Pi 5 tarafından sağlanabilir.


Ucuz VPS'ler genellikle yalnızca 1 çekirdek ve 4GB RAM ile gelir; bu da blok yüksekliği 911817'de tüm bitcoin blockchain'i senkronize etmek ve doğrulamak için çok azdır.


Depolama açısından tam bir düğüm, tercihen SSD veya NVMe tipi olmak üzere en az 2 TB disk depolama alanı gerektirecektir. blockchain'yı budarken çok daha küçük bir depolama sürücüsü kabul edilebilir (örneğin 128GB SSD).


Büyük (300+ girdi) coinjoinler için bir koordinatör çalıştırmayı düşünüyorsanız, tüm imza doğrulamaları için daha yüksek performansa sahip daha hızlı/yeni çekirdeklere sahip bir sistem seçmeniz önerilir.


## Kurulum 🛠️


Düğüm üzerinde, wallet'in yanında bağımsız yürütülebilir dosyalar olarak bir arka uç ve koordinatör içeren Wasabi Wallet'nin en son yayınlanan sürümünü indirip kurmak istiyoruz.


En son sürümü bulun: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) ve sürümün PGP imzasını anahtarlarla doğrulayın: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Dağıtım ayrıntıları donanıma (CPU mimarisi) ve işletim sistemi seçimine bağlı olarak farklılık gösterir, aşağıda başlangıç noktası olarak Debian tabanlı RaspiBlitz ile bir Raspberry Pi (ARM-64) için farklı ayrıntılar verilmiştir. Nix kullanarak (X86-64) Ubuntu işletim sistemi dağıtımı için ileri atlayın.


Kurulum talimatlarını burada bulabilirsiniz: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debian konuşlandırması


RaspiBlitz (v1.11 ile test edilmiştir) düğümleri için kaynak koddan script oluşturma dağıtımı kullanılabilir: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Kolay dağıtım


Minimal bir dağıtım için sadece platformunuz için çalıştırılabilir dosyaları bir klasöre çıkarmak istersiniz.

Debian/Ubuntu için örnek komut satırı kodları:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Bu, aşağıdaki geçerli imza mesajıyla sonuçlanmalıdır:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Ve indirilen paketi yüklemeye devam edebilirsiniz:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Yapılandırma 🧾


Koordinatörü çalıştırmadan önce Config.json dosyasını kendi dosyanızla düzenlemeniz gerekir:


- Bitcoin RPC kimlik bilgileri
- Tercih edilen tur parametreleri
- Koordinatör Genişletilmiş Açık Anahtar (toplanan tozu almak için yeni bir SegWit wallet oluşturun)

**Uyarı**: Taproot wallet harcanamaz UTXO'larla sonuçlanacaktır! Burada bir Native Segwit wallet kullanın.


- İzin verilen giriş ve çıkış adres türleri
- Nostr üzerinden yayınlamak için spiker yapılandırması (ad, açıklama, Uri, minimum girişler, nostr rölesi, nostr özel anahtarı)


Sadece .onion adresi üzerinden erişilebilen koordinatörü çalıştırabilir veya özel clearnet alan adınızı kullanabilirsiniz.


Bu yolda yapılandırma dosyasını bulun veya oluşturun:


`~/.walletwasabi/coordinator/Config.json`


Komut ile düzenleyin:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Bu örnek Config.json'a bakın:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Tor yapılandırması 🧅


OnionServicePrivateKey'inizi doldurmak için muhtemelen önce bir tane oluşturmanız gerekir.


Config.json dosyasında ``"PublishAsOnionService": true,`` ayarıyla ilk kez çalıştırırsanız Wasabi Wallet sizin için bir özel anahtar oluşturacaktır.


Koordinatörü komut ile bir kez çalıştırın:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Onion gizli hizmet adresinizi görmek için koordinatör günlüklerini şu şekilde kontrol edin:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


ve şöyle bir şey bulacaksın:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


.onion ile biten uzun URL, gizli hizmet adresiniz veya CoordinatorUri'dir.


Veya koordinatör yapılandırma dosyanızı şu şekilde tekrar kontrol edin:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Şimdi otomatik olarak doldurulması gerekir.


## Koşu ⚡


Tüm yapılandırma parametreleri ayarlandıktan sonra koordinatör hizmetini çalıştırabilir ve ilk turunuzu duyurmaya başlayabilirsiniz 🕶️


Koordinatörü şu komutla başlatmanız yeterlidir:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Mevcut turu ve kayıtlı UTXO'ların / coinlerin sayısını kontrol ederek izleyebilirsiniz (.onion için Tor tarayıcısında):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### İsteğe bağlı: koordinatör sunucusunda hata ayıklama


Herhangi bir sorun veya hatayı ``~/.walletwasabi/backend/Logs.txt`` adresindeki günlük dosyasında izleyebilirsiniz


Tipik sorunlar RPC bağlantı sorunlarını içerir, bunun ```~/.bitcoin/bitcoin.conf`` ile etkinleştirilmesi gerekir:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### İsteğe bağlı: Arka uç sunucusunu çalıştırma


Koordinatörle birlikte, kendi bitcoin düğümü olmayan kullanıcıların ücret tahminleri ve blok filtreleri için bağlanabilecekleri bir arka uç sunucusu da sağlayabilirsiniz.


Bu hizmeti komut ile başlatın:


```
wbackend
```


## Wasabi kullanıcılarını koordinatörünüze davet etme 🫂


Diğer kullanıcıların hizmetinizi bulması için nostr duyurucusuna güvenebilir veya alan adınızla (clearnet) veya gizli hizmetinizle (.onion bağlantısı) sihirli bir bağlantı paylaşabilir ve bunun gibi parametreleri yuvarlayabilirsiniz:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Bir kullanıcı sihirli bağlantıyı kopyalayıp Wasabi Wallet'ünü açtığında, yazılım otomatik olarak alan adınız ve parametrelerinizle birlikte koordinatör iletişim kutusunu gösterecektir.


![detected](assets/en/02.webp)


💚🍣 Bitcoin gizliliğini merkezsizleştirdiğiniz için tebrikler 🕶️


Eğitiminizi unutmayın [wasabika] (https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet sadece savunma içindir 🛡️