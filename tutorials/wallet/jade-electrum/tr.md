---
name: Yeşim - Electrum
description: Jade veya Jade Plus'ınızı Electrum (masaüstü) ile kullanma
---

![cover](assets/cover.webp)



_Bu kılavuz bir [Bitcoin Atölye Çalışmaları dersinden] (https://officinebitcoin.it/lezioni/jadeele/index.html)_ alınmıştır



Eğitim Jade Classic ile yapılmıştır, ancak işlemler Jade Plus'a sahip olanlar için de geçerlidir.



Jade'i başlattıktan sonra kullanmaya başlayabilir ve bunun için bir wallet ekranı seçebilirsiniz.



Jade, birkaç wallet veya Blockstream'in sitesinde belirttiği gibi tamamlayıcı uygulamalarla kullanılabilen bir cihazdır.



Bu eğitimde Electrum Wallet'yı USB kablo bağlantısı ile kullanma adımlarını göreceksiniz.



## Açık anahtar transferi



İlklendirilmiş Jade'inizi alın ve açın. Açar açmaz şöyle görünür:




![img](assets/en/32.webp)



Eğer _Unlock Jade_ seçeneğini seçerseniz, cihazınızı yardımcı uygulamaya nasıl bağlayacağınızı seçmeniz gereken menüyü göreceksiniz.



Electrum ile Jade'i yalnızca USB üzerinden bağlayabilirsiniz, bu nedenle bu yöntemi seçin.



Son kullanılan Electrum'i açmak için varsayılan seçenek olarak önerilen wallet'u başlatın.



Jade'i Electrum'a ilk kez bağlıyorsanız, _Create New Wallet_ (Yeni Cüzdan Oluştur) ve ardından _Finish_ (Bitir) öğesini seçin.



![img](assets/en/34.webp)



İsim wallet.



![img](assets/en/35.webp)



Standart Wallet'yi seçin.



![img](assets/en/36.webp)



Anahtar deposunu seçerken, _Bir donanım aygıtı kullan_ seçeneğini seçmek çok önemlidir.



![img](assets/en/37.webp)



Electrum donanım aygıtı için taramaya başlar.



![img](assets/en/38.webp)



USB'yi bilgisayara bağlayarak (USB C tarafında Jade'e zaten bağlı), wallet donanımı size kilit modunda görünür. Jade, kurulum sırasında ayarlanan altı haneli PIN kodunu girerek kilidi açar.




![img](assets/en/39.webp)



Kilitlenmemiş Donanım cihazı, Electrum Jade'i algılar. Sonraki_'ye tıklayarak devam edin.



![img](assets/en/40.webp)



Bu noktada Electrum sizden politika komut dosyasını ayarlamanızı ister: _Native Segwit_ seçeneğini seçin.



![img](assets/en/41.webp)



wallet'den Jade'e Electrum'yi görüntülemek için açık anahtar aktarımı aşaması başlar.



Açık anahtar dışa aktarımı tamamlandığında işlem bitmiş olur.



Yalnızca izleme hazırdır ve Electrum aşağıdaki ekranla tamamlandığına dair uyarı verir.



![img](assets/en/42.webp)



wallet gerçekten oluşturuldu ve onu keşfetmeye başlayabilirsiniz: _adresleri_, _cüzdan bilgilerini_ ve en önemlisi - sağ alt köşede Blockstream'in cihazı olduğunu görebilirsiniz. Blockstream logosunun yanındaki yeşil nokta, cihazın açık olduğunu ve yerel ağa düzgün bir şekilde bağlandığını gösterir.



![img](assets/en/43.webp)



## Alım ve harcama işlemleri



Electrum'in _Receive_ menüsünden, generate fon almak için bir `scriptPubKey` (adres). Her zaman küçük bir miktarla başlayın ve bir alma+harcama testi yapın.



![img](assets/en/44.webp)



Sats'ları aldıktan sonra _Tarih_ menüsünden gelişlerini kontrol edebilirsiniz.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



İşlem onaylandıktan sonra, bu UTXO'ü harcayabilir ve testi bitirebilirsiniz.



Masraflar, imzalamak için Jade'in kullanılmasını içeriyor.



Electrum'ün _Send_ menüsüne gidin, bir scriptPubKey yapıştırın ve iyice kontrol edin.



![img](assets/en/47.webp)



Bitirdiğinizde _Pay_ tuşuna basın.



Doğru işlem ücretlerini ayarlamanın önemli olduğu işlem penceresi açılır. Tüm ayarları tamamladığınızda sağ alt köşedeki _Önizle_ butonuna tıklayın.



![img](assets/en/48.webp)



İşlem penceresi, başta durum olmak üzere bazı önemli ayrıntıları gösterir: `İmzalanmamış`.



Bu aşamada, imzayı Jade ile yapıştırmak için tıklamanız gereken _Sign_ komutunu da görebilirsiniz.



![img](assets/en/49.webp)



Şimdi wallet ekranı ile donanım cihazı arasında bir iletişim aşaması başlar ve bu aşamada Electrum sizi donanım cihazındaki talimatları izlemeniz konusunda uyarır, cihaz açık ve imzalamaya hazırdır.



![img](assets/en/50.webp)



**Yine de, öncelikle neyi imzaladığınızı doğrulasanız iyi olur: yeni kurduğunuz işlemin tüm parametreleri Jade** üzerinde de görünür ve hepsini doğrulayabilirsiniz.



![img](assets/en/51.webp)



Devam etmek için imleci her zaman sonraki adımlara yönlendiren `→` okunun üzerine getirdiğinizden emin olun ve işlemi tamamlamadan sonlandırmak istemiyorsanız asla `X` üzerine getirmeyin.



Doğrulama kısmı ücret gösterimi ile sona erer. Bu noktada onaylama, imzanızı atmakla eşdeğerdir.



![img](assets/en/52.webp)



Kısa bir süre için Jade işlemi işler, bittiğinde ana menüye döner.



![img](assets/en/53.webp)



Electrum üzerindeyken işlemin `İmzasız`dan `İmzalı`ya değişen durumunu görebilirsiniz ve artık _Yayınla_ seçeneğine tıklayarak işlemi yaymanız mümkündür.



![img](assets/en/54.webp)



Bu şekilde test edilen wallet, güvenli depolama amaçlı UTXO'u almak için kullanılabilir.



![img](assets/en/55.webp)



Bu kılavuz, USB üzerinden bağlanan Jade cihazınızın yalnızca wallet saatiyle nasıl kullanılacağına dair bir örnektir. Electrum klasik bir örnektir, ancak diğer wallet yazılımlarını da tercih edebilirsiniz. Jade açık anahtarı diğer birçok cüzdana aktarır: bu eğitimde okuduğunuz benzer işlevleri bulun, size rehberlik etmek ve en sevdiğiniz companio uygulamasını nasıl kullanacağınızı bulmak için.