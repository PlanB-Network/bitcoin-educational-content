---
name: Alby

description: Bitcoin ve Lightning Network için tarayıcı uzantısı
---

![cover](assets/cover.webp)




Bitcoin ile ödemeleri giderek daha kolay hale getirmek, sektördeki birçok şirketin karşılaştığı bir zorluktur. Alby, tarayıcılar için Alby wallet uzantısı ile kalabalığın arasından sıyrılıyor. Bu uzantı, adresleri otomatik olarak algılayan ve sorunsuz bitcoin ödemeleri yapmanızı sağlayan akıcı bir çerçeve kurmayı amaçlıyor. Bu eğitimde, Alby uzantısını keşfediyor ve tarayıcıdan ödemeleri nasıl kolaylaştırdığını test ediyoruz.




![video](https://youtu.be/nd5fX2vHuDw)




## Alby uzatma



Alby uzantısı, web tarayıcınızın Bitcoin ağı ve Lightning Network katmanı ile kolayca ve güvenli bir şekilde etkileşime girmesini sağlayan bir araçtır. Üç yönü ile karakterize edilir:




- Lightning Network wallet: Lightning Network katmanı üzerinden hızlı ve ucuz bir şekilde bitcoin göndermek ve almak için Alby düğümünüzü veya hesabınızı bağlayın.
- Web üzerinden akışkan ödemeler: Lightning'i destekleyen web sitelerinde bitcoin ödemeleri için QR kodlarını tarama veya uygulamalar arasında geçiş yapma ihtiyacını ortadan kaldırır. Tek bir tıklama ile veya bir bütçe belirlediyseniz onay olmadan sorunsuz işlem yapılmasını sağlar.
- Bir Nostr yöneticisi: Uzantı, Nostr anahtarlarınızı yöneterek, özel anahtarınızı her platforma ifşa etmeden güvenli bir imza sahibi olarak hareket eden Nostr uygulamalarına bağlanmayı ve bunlarla etkileşim kurmayı kolaylaştırır.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Uzantıya bağlanın



Bu eğitimde, Alby uzantısını Firefox işletim sistemi altında Ubuntu tarayıcısında kullanacağız. Ancak, Windows'ta ve Chrome gibi tarayıcılarda da kullanılabilir.



Alby uzantısını tarayıcınıza [Firefox] uzantı mağazasını (https://addons.mozilla.org/fr/firefox/addon/alby/) veya [Chrome] uzantı mağazasını (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe) ziyaret ederek ekleyebilirsiniz.



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Her türlü korsanlığı veya bitcoinlerinizin çalınmasını önlemek için uzantının yazarının gerçekten resmi Alby hesabı olup olmadığını kontrol etmek önemlidir.



Sağdaki düğmeye tıklayarak uzantıyı tarayıcınıza ekleyin.


Uzantıyı yüklemek ve kullanmak için gerekli izinleri verin, ardından kolay erişim için uzantıyı araç çubuğuna sabitleyin.



![pin](assets/fr/03.webp)



Ayrıca, tarayıcınızdan Lightning wallet'nize güvenli erişimi garanti edecek bir kilit açma kodu (çok önemli) tanımlamalısınız. Güçlü bir alfanümerik şifre belirlemenizi öneririz.



ℹ️ Bu şifreyi güvenli bir yere kaydedin, böylece unuttuğunuzda erişebilirsiniz, çünkü değiştirilebilir ancak geri alınamaz.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby, size iki seçenek sunarak uyarlanabilirliğini göstermektedir:




- Bitcoinlerinizin kontrolünü elinizde tutarken uygulamaların keyfini çıkarmak istiyorsanız Alby hesabıyla devam edin.
- Uzantı tarafından desteklenen bir düğümünüz varsa kendi wallet veya Lightning düğümünüzü bağlayın.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


Bu eğitimde, Alby ekosisteminin özelliklerinden yararlanmak için Alby hesabıyla devam etmeyi seçiyoruz.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Alby hesabınıza giriş yapın veya henüz bir hesabınız yoksa bir hesap oluşturun.



![signup](assets/fr/05.webp)



## İlk ödemelerinizi yapmak



Giriş yaptıktan sonra, portföyünüze erişmek için araç çubuğundaki Alby uzantısına tıklayabilirsiniz.



![buzzin](assets/fr/06.webp)



Alby hesabınızı oluşturduktan sonra, satoshi harcamak için hesabınızı bir wallet'e bağlamanız gerekecektir. Bitcoin wallet'i Alby hesabınıza bağlamak için, bilgisayarınızda kurabileceğiniz veya Alby tarafından sunulan bir plana abone olabileceğiniz bir Alby Hub düğümü kullanmanızı öneririz.



![hubplan](assets/fr/13.webp)




Bu eğitimde, Alby hesabımız makinemizdeki yerel bir kurulum tarafından desteklenmektedir.


Kendi Alby düğümünüzü oluşturmak için Alby Hub eğitimimizi öneririz.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Bu düğüm, kendi kendine emanet Lightning portföyleri oluşturmanıza ve satoshis göndermek ve almak için Lightning kanallarınızı verimli bir şekilde yönetmenize olanak tanır.



![channels](assets/fr/14.webp)



Alabileceğiniz toplam satoshis sayısını tanımlayan alım kanallarını açın.



![receivechanal](assets/fr/15.webp)



Bir bitcoin onchain adresindeki satoshileri bloke ederek gönderme kanallarını açın. Bloke ettiğiniz satoshiler, harcayabileceğiniz toplam satoshileri tanımlar.



![spend](assets/fr/16.webp)



Artık Alby uzantısı üzerinden satoshis gönderebilir ve alabilirsiniz.



![exchange](assets/fr/08.webp)



Bu noktadan sonra Alby uzantısı, ziyaret ettiğiniz web sayfalarında bulunan Lightning adreslerini ve faturaları tespit edebilir ve bunları doğrudan uzantınızdan bitcoin veya Lightning ile ödemenizi önerecektir.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Kurtarma anahtarlarını ana anahtarla güvence altına alma



Alby uzantısı tarafından sunulan ana anahtar, ana Bitcoin ağ katmanı (Onchain), Nostr sistemi ile güvenli bir şekilde iletişim kurmanızı ve Nostr uygulamaları ile Lightning bağlantısını etkinleştirmenizi sağlayan koruyucu bir kaplama görevi görür.



![masterKey](assets/fr/11.webp)



Bu ana anahtar, kurtarma ifadenize benzer 12 kelimeden oluşur. Bu nedenle, istediğiniz zaman erişilebilmesini sağlamak için güvenli yöntemler kullanarak saklamanızı öneririz.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Artık Alby uzantısı ile sorunsuz bitcoin ve Lightning ödemelerini deneyimleyebilirsiniz. Bu eğitimi beğendiyseniz, kendi Alby düğümünüzü kurmak ve Alby cüzdanlarınızın tüm yönlerini sorunsuz ve güçlü bir arayüzden kontrol etmek için Alby Hub eğitimimizi öneririz.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a