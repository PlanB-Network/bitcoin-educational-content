---
name: Watch Tower
description: Watch Tower'i anlama ve kullanma
---

## Gözetleme kuleleri nasıl çalışır?


Lightning Network ekosisteminin önemli bir parçası olan gözetleme kuleleri, kullanıcıların yıldırım kanallarına ekstra bir koruma derecesi sağlar. Ana sorumluluğu, kanalların sağlığını gözetmek ve kanal taraflarından biri diğerini dolandırmaya çalışırsa müdahale etmektir.


Peki bir Watchtower bir kanalın ihlal edilip edilmediğini nasıl belirleyebilir? Watchtower, herhangi bir ihlali doğru bir şekilde tespit etmek ve müdahale etmek için ihtiyaç duyduğu bilgileri kanal taraflarından biri olan müşteriden alır. En son işlem detayları, mevcut kanal durumu ve ceza işlemleri oluşturmak için gereken bilgiler sıklıkla bu bilgilere dahil edilir. Verileri Watchtower'e iletmeden önce, müşteri gizliliği ve mahremiyeti korumak için şifreleyebilir. Bu, Watchtower'ün veriyi alsa bile gerçekten bir ihlal gerçekleşmediği sürece şifrelenmiş verinin şifresini çözmesini engeller. İstemcinin gizliliği, Watchtower'ün özel verilere yetkisi olmadan erişmesini de engelleyen bu şifreleme sistemi ile korunur.


## Kendi Eye of Satoshi'ünüzü nasıl kurar ve katkıda bulunmaya başlarsınız?


Satoshi'nın Gözü ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos?ref=blog.summerofbitcoin.org)), [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org) ile uyumlu, gözetim altında olmayan bir Yıldırım Watchtower'tir. İki ana bileşeni vardır:


1. teos: bir CLI ve kulenin sunucu tarafı çekirdek işlevselliğini içerir. Bu sandık oluşturulduğunda iki ikili dosya -teosd ve teos-CLI- üretilecektir.

2. teos-common: Paylaşılan sunucu tarafı ve istemci tarafı işlevselliğini içerir (bir istemci oluşturmak için yararlıdır).


Kuleyi başarılı bir şekilde çalıştırmak için, kuleyi teosd komutuyla çalıştırmadan önce bitcoind'un çalışıyor olması gerekir. Bu iki komutu da çalıştırmadan önce Bitcoin.conf dosyanızı ayarlamanız gerekir. İşte bunu nasıl yapacağınıza dair adımlar:-


1. Bitcoin core'yi kaynaktan yükleyin veya indirin. İndirdikten sonra Bitcoin.conf dosyasını Bitcoin core kullanıcı dizinine yerleştirin. Kullandığınız işletim sistemine bağlı olarak dosyayı nereye yerleştireceğinizle ilgili daha fazla bilgi için bu bağlantıyı kontrol edin.

2. Dosyanın oluşturulması gereken yeri belirledikten sonra, şu seçenekleri ekleyin:-


```
#RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

#chain
regtest=1```

- server: For RPC requests
- rpcuser and rpcpassword: RPC clients can authenticate with the server
- regtest: Not required but useful if you're planning for development.

rpcuser and rpcpassword need to be picked by you. They must be written without quotes. Eg:-

```

rpcuser=aniketh

rpcpassword=strongpassword``


Şimdi, bitcoind'ü çalıştırırsanız düğümü çalıştırmaya başlamalıdır.


1. Kule kısmı için öncelikle teos'u kaynaktan yüklemeniz gerekiyor. Bu bağlantıda verilen talimatları izleyin.

2. Teos'u sisteminize başarıyla kurduktan ve testleri çalıştırdıktan sonra, teos kullanıcı dizininde teos.toml dosyasını ayarlamak olan son adıma geçebilirsiniz. Dosyanın ev klasörünüzün altındaki .teos (noktaya dikkat edin) adlı bir klasöre yerleştirilmesi gerekir. Örneğin, Linux için /home/<kullanıcı adınız>/.teos. Yeri bulduktan sonra, bir teos.toml dosyası oluşturun ve bitcoind'te değiştirdiğimiz şeylere karşılık gelen bu seçenekleri ayarlayın.


```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>```

Notice that here the username and password need to be written quoted, that is, for the same example as before:

```

btc_rpc_user = "aniketh"

btc_rpc_password = "strongpassword"``


Bunu yaptıktan sonra kuleyi çalıştırmaya hazır olmalısınız. Regtest üzerinde çalıştırdığımız için, kule ilk kez bağlandığında Bitcoin test ağında çıkarılmış herhangi bir blok olmayacaktır (varsa, kesinlikle bir sorun vardır). Kule, bitcoind'daki en son 100 bloğun dahili bir önbelleğini oluşturur, bu nedenle ilk kez çalıştırıldığında aşağıdaki hatayı alabiliriz:


_ERROR [teosd] Kuleyi başlatmak için yeterli blok yok (gerekli: 100). En az 100 tane daha çıkar_


Regtest üzerinde çalıştığımız için, diğer ağlarda (Mainnet veya Testnet gibi) genellikle gördüğümüz 10 dakikalık medyan süresini beklemeye gerek kalmadan bir RPC komutu vererek blok madenciliği yapabiliriz. bitcoin-cli yardımını kontrol edin ve blokların nasıl çıkarılacağını arayın. Eğer yardıma ihtiyacınız varsa, bu makaleyi inceleyebilirsiniz.


![image](assets/2.webp)


İşte bu, kuleyi başarıyla çalıştırdınız. Tebrik ederim. 🎉