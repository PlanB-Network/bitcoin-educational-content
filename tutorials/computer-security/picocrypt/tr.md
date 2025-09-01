---
name: Picocrypt
description: Verilerinizi şifrelemek için açık kaynaklı bir araç
---
![cover](assets/cover.webp)



___



*Bu eğitim Florian BURNEL tarafından [IT-Connect](https://www.it-connect.fr/) adresinde yayınlanan orijinal içeriğe dayanmaktadır. Lisans [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Orijinal içerikte değişiklikler yapılmıştır.*



___



## I. Sunum



Bu eğitimde, verileri yüksek düzeyde güvenlikle şifrelemek için basit, hafif ve etkili bir şifreleme yazılımı olan Picocrypt'e göz atacağız.



Dosyaları **şifrelemek** için uygun olan bu yazılımı **bilgisayarınızdaki, USB bellekteki** ve aynı zamanda Bulutta depolanan verileri korumak için kullanabilirsiniz. Örneğin, verileri şifreleyebilir ve **Microsoft OneDrive, Google Drive, iCloud veya Dropbox** üzerinde saklayabilirsiniz, ancak bu amaç için gelecekteki bir makalede sunulacak olan başka bir yazılımı tercih ediyorum.



Verileri üçüncü bir tarafla **paylaşmanız** gerektiğinde de kullanabilirsiniz: Picocrypt ve şifre çözme anahtarı sayesinde, kendi makinelerindeki verilerin şifresini çözebileceklerdir. Böylece hesabınız veya bilgisayarınız ele geçirilirse verileriniz korunur.



Picocrypt projesini takip etmek için sadece bir Address vardır:





- [Picocrypt on GitHub](https://github.com/Picocrypt/Picocrypt)



Tamamen **ücretsiz ve açık kaynak** olan PicoCrypt **Windows,** **Linux** ve **macOS** için kullanılabilir. Windows'ta kendi makinenize yükleyebilir veya taşınabilir sürümünü kullanabilirsiniz.



## II. Picocrypt, açık kaynak kodlu şifreleme yazılımı



Picocrypt** şifreleme yazılımı kendisini **VeraCrypt** ve **Cryptomator** (*Bulut ortamlarındaki* verileri şifrelemek için tasarlanmıştır) veya **AxCrypt** gibi diğer iyi bilinen çözümlere **bir alternatif** olarak sunar. Bu arada, Picocrypt'in resmi GitHub'ında bazı rakiplerle bir karşılaştırma bulabilirsiniz:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Kaynak: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt **çok hafiftir**, sadece **3 MB** ağırlığındadır ve yüklenmesi gerekmez: yönetici hakları gerektirmeme avantajına sahip **taşınabilir bir uygulamadır**! Bununla birlikte, **sağlam ve güvenilir algoritmalara** dayandığı için güvenliği ihmal etmez:





- XChaCha20** şifreleme algoritması
- Anahtar bypass fonksiyonu **Argon2**



Az önce bahsedilen avantajların ötesinde, gerçekten cazip olan **kullanım kolaylığıdır**!



Sadece tek bir şeye ihtiyacı var: **Kod denetimi**, ancak yukarıdaki karşılaştırma tablosundan da görebileceğiniz gibi (son satır) bu planlanmıştır. Ancak açık kaynak kodlu olduğu için kaynak koduna göz atmanızı engelleyecek bir şey yok.



Yukarıdaki tabloda BitLocker ile karşılaştırılmış olsa da, **bana göre BitLocker ve Picocrypt farklı kullanımlar için tasarlanmıştır**: BitLocker tüm bir birimi (örneğin Windows'u) şifrelemek için, Picocrypt ise bir ağaç yapısını ya da "Drive" tipi depolama alanını şifrelemek için kullanılır.



## III. Picocrypt Kullanımı



Bu gösterim için bir Windows 11 makinesi kullanılacaktır.



### A. Picocrypt ile veri şifreleme



Öncelikle Picocrypt.exe dosyasını resmi GitHub'dan indirmeniz gerekiyor ([bu sayfaya bakın](https://github.com/Picocrypt/Picocrypt/releases)).



Minimalist Interface'i ekranda görüntülemek için uygulamayı açın. Verileri şifrelemek için, ister **bir dosya, ister birkaç dosya veya bir klasör** olsun, basitçe **sürükle ve Picocrypt'in Interface'ine bırak**. Bu, şifrelenecek verileri seçecektir.



![Image](assets/fr/020.webp)



Ardından, veri şifreleme için, şifreleme anahtarı da dahil olmak üzere çeşitli seçeneklere erişebilirsiniz. Bu **güçlü bir parola** veya **anahtar dosyası şeklinde bir şifreleme anahtarı** ya da **her ikisi** olabilir. Parola örneğini ele alırsak, kendi parolanızı oluşturmak veya Picocrypt ile bir parola oluşturmak arasında seçim yapabilirsiniz.



Bu parola, verilerin şifresini çözmek için kullanılabileceğinden güçlü olmalıdır. "**Parola**" ve "**Parolayı Onayla**" altına girin, ardından verileri şifrelemek için "**Şifrele**" düğmesine tıklayın! Bundan önce, çıktı dizinini belirtmek için "**Çıktıyı farklı kaydet**" seçeneğinin yanındaki "**Değiştir**" düğmesine tıklayabilirsiniz.



**Not**: Dosya formatında bir anahtar kullanmak için, bir anahtar oluşturmak üzere "**Anahtar Dosyaları**"nın sağındaki "**Oluştur**"a tıklayın. Ardından "**Düzenle**" üzerine tıklayarak ve anahtar dosyasını uygun alana sürükleyip bırakarak seçin.



![Image](assets/fr/019.webp)



Seçilen iki dosya **şifrelenir ve "**Encrypted.zip.pcv**" dosyasında birlikte gruplanır**, çünkü **PCV** Picocrypt tarafından kullanılan uzantıdır. Bu ZIP dosyası şifreleme sayesinde okunamaz. Seçilen dosyaların tek bir şifrelenmiş ZIP dosyasında gruplanmasını önlemek için "**Yinelemeli**" seçeneğini işaretlemeniz gerekir, böylece şifrelenecek dosya sayısı kadar şifrelenmiş dosya olur.



Verilerimize erişmek için Picocrypt kullanarak şifrelerini çözmemiz gerekir.



![Image](assets/fr/023.webp)



Veri şifre çözme hakkında konuşmadan önce, işte mevcut seçeneklerden bazıları hakkında bazı bilgiler:





- Paranoid mod**: Picocrypt tarafından sunulan en yüksek güvenlik seviyesini kullanın. Araç, veri kimlik doğrulaması için BLAKE2b yerine birkaç basamaklı şifreleme algoritması (XChaCha20 ve Serpent) ve HMAC-SHA3 kullanacaktır.
- Reed-Solomon**: Bozuk verilerde hata düzeltmeyi kolaylaştırmak için *Reed-Solomon* hata düzeltme kodlarını uygular. Bu, dosyanızın yaklaşık %3'lük bir bozulma seviyesini desteklemenizi sağlar.
- Parçalara böl** veya **birkaç parçaya böl**: Eğer büyük bir dosyayı şifreliyorsanız, Picocrypt'ten dosyayı birkaç parçaya bölmesini isteyebilirsiniz. Bu, dosyanın aktarılmasını kolaylaştırabilir.
- Dosyaları Sıkıştır** veya **Dosyaları sıkıştır**: şifrelenmiş dosyaların boyutunu azaltmak için dosyaları sıkıştırın.
- Silinen dosyalar** veya **Fichiers supprimés**: yalnızca şifrelenmiş sürümü saklamak için kaynak dosyaları silin



### B. Picocrypt ile verilerin şifresini çözme



Verilerin şifresini çözmeniz gerekiyorsa, bu şifrelemekten daha karmaşık değildir. Picocrypt'i açın ve **şifresi çözülecek PCV dosyasını sürükleyip bırakın**. Ardından şifreyi girin ve/veya "**Şifre Çöz**" seçeneğine tıklamadan önce anahtar dosyayı seçin.



![Image](assets/fr/021.webp)



"Encrypted.zip" ZIP arşivinin şifrelenmemiş sürümü artık iki dosyamı açık metin olarak kurtarmamı sağlıyor!



![Image](assets/fr/022.webp)



## IV. Sonuç



**Uyarıldınız: Picocrypt'in kullanımı çok kolaydır ve işe yarar! Interface minimalist olmasına rağmen, şifrelemeyi özelleştirmek için bazı çok kullanışlı seçenekler içerir! Taşınabilir bir sürümü de mevcut olduğundan, nereye giderseniz gidin yanınızda götürebilir, böylece verilerinizin şifresini güvenle çözebilirsiniz**



Verileri korumak için güçlü parolalar kullandığınızdan emin olun ve bir anahtar dosyası kullanıyorsanız, bunu yedeklemeyi unutmamalısınız, aksi takdirde Picocrypt tarafından oluşturulan PCV konteynerinin şifresini artık çözemezsiniz. Son olarak, Picocrypt'i komut satırından çalıştırmanıza izin veren [bir CLI sürümü] (https://github.com/Picocrypt/CLI) (daha az özelliğe sahip) olduğunu bilmelisiniz: burada yine Picocrypt yeni olasılıklara kapı açıyor.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5