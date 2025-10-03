---
term: ÇEREZ (.COOKIE)
---

Bitcoin core'da RPC (*Uzaktan Prosedür Çağrısı*) kimlik doğrulaması için kullanılan dosya. bitcoind başlatıldığında, benzersiz bir kimlik doğrulama çerezi oluşturur ve bu dosyada saklar. RPC Interface aracılığıyla bitcoind ile etkileşime girmek isteyen istemciler veya komut dosyaları, güvenli bir şekilde kimlik doğrulaması yapmak için bu çerezi kullanabilir. Bu mekanizma, kullanıcı adları ve parolaların manuel olarak yönetilmesini gerektirmeden bitcoind ile harici uygulamalar (örneğin Wallet yazılımı gibi) arasında güvenli iletişim sağlar. .cookie` dosyası bitcoind'nin her yeniden başlatılmasında yeniden oluşturulur ve kapatıldığında silinir.