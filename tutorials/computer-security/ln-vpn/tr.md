---
name: LN VPN

description: VPN'inizi kurun
---

![image](assets/cover.webp)


LN VPN, yalnızca yıldırım ödemelerini kabul eden özelleştirilebilir bir VPN hizmetidir. Bugün size onu nasıl kullanacağınızı ve internette gezinirken nasıl daha az iz bırakacağınızı göstereceğim.


Birçok kaliteli VPN hizmet sağlayıcısı vardır ve bu makalede kapsamlı bir inceleme yaptık (köprü). Ancak, LN VPN öne çıkıyor ve onu size tanıtma fırsatını kaçıramazdık.


ProtonVPN ve Mullvad gibi çoğu VPN hizmet sağlayıcısı, bitcoin ile ödeme seçeneği sunar, ancak bir hesap oluşturmayı ve daha uzun veya daha kısa bir süre için bir plan satın almayı gerektirir, bu da herkesin bütçesine uymayabilir.


LN VPN, Bitcoin ödemelerinin Lightning Network üzerinden uygulanması sayesinde bir saat gibi kısa bir süre için isteğe bağlı VPN kullanımına olanak tanır. Anında ve anonim olan yıldırım ödemeleri, mikro ödemeler için bir olasılıklar dünyasının kapılarını açıyor.


Not💡: **Bu kılavuz, LN VPN'in bir Linux Ubuntu 22.04 LTS sisteminden nasıl kullanılacağını açıklamaktadır


## Önkoşullar: Wireguard


Basit bir ifadeyle, Wireguard bilgisayarınız ile internette gezineceğiniz uzak sunucu arasında güvenli bir tünel oluşturmak için kullanılır. Bu sunucunun IP Address'i, bu kılavuzu izleyerek Contract yapacağınız kira sözleşmesi süresince sizin olarak görünecektir.


Resmi Wireguard kurulum kılavuzu: https://www.wireguard.com/install/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## Önkoşullar: Yıldırım Bitcoin Wallet


Henüz bir Lightning Bitcoin Wallet'niz yoksa endişelenmeyin, burada sizin için çok basit bir rehber oluşturduk. (LN öğretici bölümü size yardımcı olabilir)


## Adım 1: Contract Bir Kira Sözleşmesi


Https://lnvpn.com adresinden, VPN tünelinin çıkış IP'sinin ülkesini ve bir süre seçmeniz gerekecektir. Bu parametreler ayarlandıktan sonra Yıldırım ile Öde'ye tıklayın.


![image](assets/1.webp)


Bir yıldırım Invoice görüntülenecektir ve bunu yıldırım Wallet'nızla taramanız yeterlidir.


Invoice'ye ödeme yapıldıktan sonra, Wireguard yapılandırma ayarlarınızın oluşturulması için birkaç saniye ila iki dakika beklemeniz gerekecektir. Biraz daha uzun sürerse panik yapmayın, bu prosedürü düzinelerce kez yaptık ve bazen sadece biraz daha uzun sürüyor.

Aşağıdaki metin, orijinal metinle aynı markdown düzeni korunarak İngilizceye çevrilmiştir:


Bir sonraki ekran görünecek ve "Dosya Olarak İndir" seçeneğine tıklayarak lnvpn-xx-xx.conf gibi bir isme sahip olacak yapılandırma dosyanızı alacaksınız; burada "xx" geçerli tarihe karşılık gelecektir.

![image](assets/2.webp)


## Adım 2: Tüneli etkinleştirin


Öncelikle, Wireguard tarafından otomatik olarak tanınabilmesi için bir önceki adımda elde edilen yapılandırma dosyasını yeniden adlandırmanız gerekecektir.


Bir terminal penceresinde veya dosya gezgini ile indirme klasörünüze gidin ve lnvpn-xx-xx.conf dosyasını aşağıdaki gibi wg0.conf olarak yeniden adlandırın:


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


İşte oldu! Tünel etkinleştirildi!


## Adım 3: Doğrulayın


Genel IP Address'inizin artık yeni etkinleştirdiğiniz VPN'deki IP olduğunu doğrulamak için whatismyip gibi bir çevrimiçi hizmet kullanın.


## Adım 4: Devre Dışı Bırak


Kira sözleşmenizin süresi dolduğunda, internete yeniden erişim sağlamak için bağlantıyı devre dışı bırakmanız gerekecektir. Daha sonra LN VPN ile bir kira sözleşmesi kurmak istediğinizde 1'den 3'e kadar olan adımları tekrarlayabilirsiniz.


Tüneli devre dışı bırakın:


```
$ sudo ip link delete dev wg0
```


İşte bu kadar! Artık benzersiz bir VPN hizmeti olan LN VPN'i nasıl kullanacağınızı biliyorsunuz!