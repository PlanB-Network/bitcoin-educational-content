---
name: "Trezor U2F & FIDO2"
description: Trezor ile çevrimiçi güvenliğinizi güçlendirin
---
![cover](assets/cover.webp)



Trezor cihazları, orijinal olarak bir Bitcoin Wallet'i güvence altına almak için tasarlanmış donanım cüzdanlarıdır, ancak aynı zamanda web üzerinde güçlü kimlik doğrulama için gelişmiş seçeneklere sahiptirler. **U2F** ve **FIDO2** protokolleri ile uyumlulukları sayesinde, yalnızca şifrelere güvenmeden çevrimiçi hesaplarınıza erişimi güvence altına almanızı sağlarlar.



U2F (*Universal 2nd Factor*) protokolü 2014 yılında Google ve Yubico tarafından tanıtılmış, ardından FIDO Alliance tarafından standartlaştırılmıştır. Oturum açarken ikinci bir fiziksel kimlik doğrulama faktörünün (2FA) eklenmesini sağlar. Etkinleştirildikten sonra, klasik şifreye ek olarak, kullanıcılar Trezor'larındaki bir düğmeye basarak hesaplarına bağlanmak için her girişimi onaylamalıdır. Bu bağlamda Trezor, Yubikey'e benzer bir şekilde çalışmaktadır.



Bu yöntem asimetrik kriptografiye dayanır: gizli veri iletilmez, bu da kimlik avı veya durdurma saldırılarını etkisiz hale getirir. U2F artık birçok çevrimiçi hizmet tarafından desteklenmektedir.



İki faktörlü kimlik doğrulama sağlayan U2F'ye ek olarak Trezors, U2F'nin bir evrimi olan FIDO2'yi (*Fast IDentity Online 2.0*) de desteklemektedir. Bu, U2F'nin mantığını genişleten ve şifreleri tamamen değiştirmeyi amaçlayan 2018 tarihli standartlaştırılmış bir kimlik doğrulama protokolüdür. İki bileşene dayanmaktadır: *WebAuthn* (tarayıcı tarafı) ve *CTAP2* (fiziksel anahtar tarafı). FIDO2 "şifresiz" kimlik doğrulama sağlar: kullanıcılar kendilerini yalnızca benzersiz bir kriptografik token görevi gören Trezor cihazları aracılığıyla, ek bir şifre olmadan tanımlar. Bu protokol artık, özellikle işletmelere yönelik olanlar olmak üzere bir dizi çevrimiçi hizmetle uyumludur.



"Parolasız" işlevselliğe ek olarak FIDO2, U2F'ye benzer bir şekilde iki faktörlü kimlik doğrulamayı da mümkün kılar.



FIDO2 ayrıca yerleşik kimlik bilgileri kavramını, yani doğrudan Trezor'da depolanan ve hem bağlantıyı sağlayan özel anahtarı hem de kullanıcının kimlik bilgilerini içeren tanımlayıcıları sunar. Bu mekanizma gerçek anlamda parolasız kimlik doğrulama sağlar: Trezor'unuzu takın ve kimlik ya da parola girmeden erişimi onaylayın. Buna karşılık, daha geleneksel olan yerleşik olmayan kimlik bilgileri yalnızca özel anahtarı cihazda saklar; kullanıcı kimliği sunucu tarafında saklanır ve bu nedenle her bağlantıda girilmesi gerekir. Bunları Trezor'unuza nasıl kaydedeceğinize daha sonra bakacağız.



Bu eğitimde, iki faktörlü kimlik doğrulama için U2F veya FIDO2'yi nasıl etkinleştireceğimizi ve ardından hesaplarınıza parola olmadan doğrudan Trezor'unuzla erişmek için FIDO2'yi nasıl yapılandıracağımızı keşfedeceğiz.



**Not:** U2F tüm Trezor modelleriyle uyumludur, ancak FIDO2 yalnızca Safe 3, Safe 5 ve Model T'de desteklenir, Model One'da desteklenmez.



## Trezor'da 2FA için U2F/FIDO2 kullanma



Başlamadan önce, Trezor'unuzda Bitcoin Wallet'i ayarladığınızdan emin olun. İki faktörlü kimlik doğrulamada U2F ve FIDO2 için kullanılan anahtarlar bu Mnemonic'ten türetildiğinden, Mnemonic'ünüzü doğru şekilde kaydetmeniz önemlidir. Trezor'unuz kaybolur veya hasar görürse, Mnemonic ifadenizi başka bir Trezor cihazına girerek anahtarlarınıza erişimi geri kazanabilirsiniz ("*parolasız*" moddaki FIDO2 kimlik bilgileri için, sonraki bölümlerde göreceğimiz gibi, seed'nın tek başına yeterli olmadığını unutmayın).



Trezor'unuzu bilgisayarınıza bağlayın ve kilidini açın.



![Image](assets/fr/01.webp)



İki faktörlü kimlik doğrulama ile güvence altına almak istediğiniz hesaba erişin. Örneğin, ben bir Bitwarden hesabı kullanacağım. 2FA seçeneğini genellikle hizmet ayarlarında, "*authentication*", "*security*", "*login*" veya "*password*" sekmelerinin altında bulabilirsiniz.



![Image](assets/fr/02.webp)



İki faktörlü kimlik doğrulamaya ayrılmış bölümde "*Passkey*" seçeneğini seçin (bu terim kullandığınız siteye göre değişebilir).



![Image](assets/fr/03.webp)



Sık sık mevcut şifrenizi onaylamanız istenecektir.



![Image](assets/fr/04.webp)



Kolay tanınması için güvenlik anahtarınıza bir isim verin ve ardından "*Anahtarı Oku*" seçeneğine tıklayın.



![Image](assets/fr/05.webp)



Hesap bilgileriniz Trezor ekranında görünecektir. Onaylamak için ekrana dokunun veya düğmeye basın. Ayrıca PIN kodunuzu da onaylamanız istenecektir.



![Image](assets/fr/06.webp)



Bu güvenlik anahtarını kaydedin.



![Image](assets/fr/07.webp)



Şu andan itibaren, hesabınıza bağlanmak istediğinizde, normal şifrenize ek olarak Trezor'unuzu da bağlamanız istenecektir.



![Image](assets/fr/08.webp)



Ardından kimlik doğrulamasını onaylamak için Trezor ekranınıza basabilirsiniz.



![Image](assets/fr/09.webp)



İki faktörlü kimlik doğrulama için bir Hardware Wallet Trezor kullanmanın avantajı, Mnemonic ifadesi sayesinde anahtarlarınızı kolayca kurtarabilmenizdir. Bu temel yedeklemeye ek olarak, 2FA'yı etkinleştirdiğiniz her hizmet tarafından sağlanan bir acil durum kodunu da kullanabilirsiniz. Bu acil durum kodu, güvenlik anahtarınızı kaybetmeniz durumunda hesabınıza bağlanmanızı sağlar. Bu nedenle, gerektiğinde bağlantı için 2FA'nın yerini alır.



Örneğin Bitwarden'da bu koda "*Kurtarma kodunu görüntüle*" seçeneğine tıklayarak erişebilirsiniz.



![Image](assets/fr/10.webp)



Birlikte çalınmalarını önlemek için bu kodu ana parolanızı sakladığınız yerden farklı bir yerde saklamanızı öneririm. Örneğin, parolanız bir parola yöneticisinde kayıtlıysa, 2FA acil durum kodunuzu kağıt üzerinde ayrı bir yerde saklayın.



Bu yaklaşım, 2FA kimlik doğrulaması için Trezor'unuzu kaybetmeniz durumunda size iki düzeyde yedekleme sunar: tüm hesaplarınız için Mnemonic ifadesini kullanan bir ilk yedekleme ve acil durum kodlarıyla her hesaba özel ikinci bir yedekleme. Ancak, **Mnemonic'un rolünü acil durum kodunun rolü ile karıştırmamak önemlidir**:




- 12 veya 24 kelimelik Mnemonic ifadesi, yalnızca tüm hesaplarınızda 2FA için kullanılan anahtarlara değil, aynı zamanda Trezor'unuzla güvence altına alınan bitcoinlerinize de erişmenizi sağlar;
- Acil durum kodu, 2FA talebini yalnızca ilgili hesapta (bu örnekte yalnızca Bitwarden'da) geçici olarak atlamanıza olanak tanır.



## Trezor üzerinde FIDO2 kullanma



İki faktörlü kimlik doğrulamaya ek olarak, FIDO2 ayrıca "parolasız" kimlik doğrulamayı, yani bir sitede oturum açarken parola girmek zorunda kalmadan kimlik doğrulamayı da sağlar. Güvenli hesabınıza bu şekilde erişmek için Trezor'unuzu bilgisayarınıza bağlamanız yeterlidir. Bu özelliği nasıl yapılandıracağınız aşağıda açıklanmıştır.



Başlamadan önce, Trezor'unuzda Bitcoin Wallet'ü kurduğunuzdan emin olun. FIDO2 "*parolasız*" tanımlayıcıları seed'ünüzle şifrelendiği için Mnemonic'i kaydetmeniz önemlidir (bir sonraki bölümde bu tanımlayıcıları nasıl doğru şekilde kaydedeceğinizi öğreneceğiz).



Trezor'u bilgisayarınıza bağlayın ve kilidini açın.



![Image](assets/fr/01.webp)



Güvenliğini sağlamak istediğiniz hesaba "*parolasız*" modda erişin. Örnek olarak bir Bitwarden hesabı kullanacağım. Bu seçenek genellikle hizmet ayarlarında, genellikle "*kimlik doğrulama*", "*güvenlik*" veya "*parola*" sekmesi altında bulunur.



Örneğin Bitwarden'da bu seçenek "*Ana şifre*" sekmesinin altında bulunur. FIDO2 aracılığıyla kimlik doğrulamayı etkinleştirmek için "*Aç*" seçeneğine tıklayın.



![Image](assets/fr/11.webp)



Sık sık şifrenizi onaylamanız istenecektir.



![Image](assets/fr/12.webp)



Hesap bilgileriniz Trezor ekranında görünecektir. Onaylamak için ekrana dokunun veya düğmeye basın. PIN kodunuzu da onaylamanız gerekecektir.



![Image](assets/fr/13.webp)



Sitede, güvenlik anahtarınızı hatırlamak için bir isim ekleyin ve ardından "*Aç*" seçeneğine tıklayın.



![Image](assets/fr/14.webp)



Daha sonra anahtarın düzgün çalışıp çalışmadığını kontrol etmek için kendinizi tanıtmanız istenecektir.



![Image](assets/fr/15.webp)



Şu andan itibaren, hesabınıza giriş yaparken artık Address e-posta adresinizi girmeniz veya oturum açmanız gerekmeyecek. Giriş formunda fiziksel bir anahtarla kimliğinizi doğrulamak için düğmeye tıklamanız yeterlidir.



![Image](assets/fr/16.webp)



Hardware Wallet PIN kodunuzu girerek Trezor'unuzla bağlantıyı onaylayın.



![Image](assets/fr/17.webp)



Şifrenizi girmenize gerek kalmadan hesabınıza bağlanacaksınız.



![Image](assets/fr/18.webp)



**Trezor'unuzda FIDO2 aracılığıyla "*parolasız*" kimlik doğrulamayı etkinleştirseniz bile, çevrimiçi hesabınızın ana parolasının oturum açma amacıyla geçerli olmaya devam edeceğini lütfen unutmayın**



## FIDO2 kimlik bilgilerinizi kaydedin (kimlik bilgileri sakinleri)



İki faktörlü kimlik doğrulama için FIDO2 veya U2F kullanıyorsanız, yani Trezor'unuz aracılığıyla 2FA doğrulamasına ek olarak parola gerektiren hesaplarda oturum açmak için, Mnemonic ifadesi tek başına anahtarlarınıza erişim sağlayacaktır. Ancak, önceki bölümde açıklandığı gibi FIDO2'yi "*parolasız*" modda kullanıyorsanız, bu kimlik bilgilerini şifreleyen Mnemonic ifadenizi yedeklemenin yanı sıra FIDO kimlik bilgilerinizin bir kopyasını da almanız gerekecektir.



Bunu yapmak için Python yüklü bir bilgisayara ihtiyacınız olacak. Bir terminal açın ve gerekli Trezor yazılımını yüklemek için aşağıdaki komutu çalıştırın:



```shell
pip3 install --upgrade trezor
```



Trezor'unuzu USB ile bilgisayara bağlayın ve PIN kodunuzu kullanarak kilidini açın.



![Image](assets/fr/01.webp)



Trezor'da depolanan FIDO2 tanımlayıcılarının listesini almak için aşağıdaki komutu çalıştırın:



```shell
trezorctl fido credentials list
```



Trezor'unuzda dışa aktarımı onaylayın.



![Image](assets/fr/19.webp)



FIDO2 giriş bilgileriniz terminalinizde görüntülenecektir. Örneğin, Bitwarden hesabım için bu bilgileri aldım:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Tüm bu bilgileri kopyalayın ve bir metin dosyasına kaydedin. Bu yedekleme ile ilgili olarak, bu hizmetleri FIDO2 ile kullandığınızı ortaya çıkarmak dışında önemli bir risk yoktur. "*Credential ID*" Wallet'inizin seed'u kullanılarak şifrelenmiştir, bu da bu yedeği alan bir saldırganın hesaplarınıza bağlanamayacağı, sadece bu hesapları kullandığınızı fark edebileceği anlamına gelir. Bu kimliklerin şifresini çözmek için Wallet'inizdeki seed'a ihtiyacınız vardır.



Bu nedenle, bu metin dosyasının birkaç kopyasını oluşturabilir ve bunları farklı yerlerde, örneğin bilgisayarınızda yerel olarak, bir dosya barındırma hizmetinde ve USB bellek gibi harici ortamlarda saklayabilirsiniz. Ancak, bu yedeklemenin otomatik olarak güncellenmediğini unutmayın, bu nedenle Trezor'unuzla her yeni "*parolasız*" bağlantı kurduğunuzda yenilemeniz gerekecektir.



Şimdi Trezor'unuzu kırdığınızı düşünelim. FIDO2 kimlik bilgilerinizi geri almak için öncelikle yeni bir FIDO2 uyumlu Trezor cihazında Mnemonic ifadenizi kullanarak Wallet'inizi kurtarmanız gerekir.



Kurtarma işlemi tamamlandıktan sonra, FIDO2 tanımlayıcılarınızı yeni cihaza aktarmak için terminalinizde aşağıdaki komutu çalıştırın:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Basitçe `<CREDENTIAL_ID>` yerine tanımlayıcılarınızdan birini yazın. Örneğin, benim durumumda bu,:



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Trezor'unuz sizden FIDO2 tanımlayıcınızı içe aktarmanızı isteyecektir. Ekrana basarak onaylayın.



![Image](assets/fr/20.webp)



FIDO2 oturum açma işleminiz artık Trezor'unuzda çalışır durumdadır. Bu prosedürü her bir tanımlayıcınız için tekrarlayın.



Tebrikler, Trezor'unuzu U2F ve FIDO2 ile kullanma konusunda artık hızlısınız! Bu öğreticiyi faydalı bulduysanız, aşağıya bir Green başparmağı bırakırsanız çok minnettar olurum. Lütfen bu öğreticiyi sosyal ağlarınızda paylaşmaktan çekinmeyin. Çok teşekkür ederim!



Ayrıca U2F ve FIDO2 kimlik doğrulaması için başka bir çözümü incelediğimiz bu diğer öğreticiyi de tavsiye ederim:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e