---
term: CHAUMIAN CoinJoin
---

Katılımcılar ve koordinatörün sunucusu arasındaki iletişim için David Chaum'un kör imzalarını ve Tor'u kullanan bir CoinJoin protokolü. Chaumian CoinJoin'in amacı katılımcılara koordinatörün bitcoinleri çalamayacağını ya da girdi ve çıktıları birbirine bağlayamayacağını garanti etmektir.


Bunu başarmak için, kullanıcılar girdilerini ve kriptografik olarak blinded alım Address'ü koordinatöre gönderir. Bu Address, bir kez unblinded olduğunda, bitcoinleri CoinJoin'ten bir çıktı olarak almayı amaçlamaktadır. Koordinatör bu tokenları imzalar ve kullanıcılara iade eder. Kullanıcılar daha sonra yeni bir Tor kimliği ile koordinatörün sunucusuna anonim olarak yeniden bağlanır ve işlem yapımı için çıktı adreslerini düz metin olarak açıklar. Koordinatör, daha önce blinded sürümlerini kendi özel anahtarıyla imzaladığı için tüm bu alım adreslerinin meşru kullanıcılardan geldiğini doğrulayabilir. Ancak, belirli bir Address çıktısını belirli bir girdi kullanıcısıyla ilişkilendiremez. Bu nedenle, koordinatörün bakış açısından bile girdiler ve çıktılar arasında bir bağlantı yoktur. İşlem koordinatör tarafından oluşturulduktan sonra, çıktılarının gerçekten de bu işlemde olduğunu doğruladıktan sonra, girdilerinin kilidini açmak için imzalayan katılımcılara geri gönderir. Katılımcılar imzayı koordinatöre gönderir. Tüm imzalar toplandıktan sonra koordinatör CoinJoin işlemini Bitcoin ağında yayınlayabilir.


![](../../dictionnaire/assets/38.webp)


Bu yöntem, koordinatörün tüm CoinJoin süreci boyunca ne katılımcıların anonimliğini tehlikeye atabilmesini ne de bitcoinleri çalabilmesini sağlar.


CoinJoin'de Bitcoin fikrini ilk kimin ortaya attığını ve David Chaum'un kör imzalarını bu bağlamda kullanma fikrinin kime ait olduğunu kesin olarak belirlemek zordur. Genellikle Gregory Maxwell'in [2013'te BitcoinTalk'taki bir mesajda] bu konuyu ilk tartışan kişi olduğu düşünülmektedir (https://bitcointalk.org/index.php?topic=279249.0):


> *"Chaum kör imzalarını kullanarak: Kullanıcılar bağlanır ve girdilerin yanı sıra (ve adresleri değiştirerek) özel paralarını göndermek istedikleri Address'un kriptografik olarak blinded versiyonunu sağlarlar; sunucu tokenları imzalar ve iade eder. Kullanıcılar anonim olarak yeniden bağlanır, çıktı adreslerinin maskesini kaldırır ve bunları sunucuya iade eder. Sunucu tüm çıktıların kendisi tarafından imzalandığını ve dolayısıyla tüm çıktıların geçerli katılımcılardan geldiğini görebilir. Daha sonra insanlar yeniden bağlanır ve imzalar. "*

Maxwell, G. (2013, 22 Ağustos). *CoinJoin: Gerçek dünya için Bitcoin gizliliği*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

Bununla birlikte, hem karıştırma bağlamında Chaum'un imzaları hem de coinjoinler için daha önce bahsedilen başka şeyler de vardır. [Haziran 2011'de Duncan Townsend BitcoinTalk'ta](https://bitcointalk.org/index.php?topic=12751.0) Chaum imzalarını modern Chaumian coinjoin'lere oldukça benzer bir şekilde kullanan bir karıştırıcı sunmuştur. Aynı başlıkta, [Duncan Townsend'e yanıt olarak hashcoin'den bir mesaj](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) karıştırıcısını geliştirmek için. Bu mesaj tam olarak coinjoins'e en çok benzeyen şeyi sunmaktadır. Alex Mizrahi'nin 2012 yılında Tenebrix'in yaratıcılarına danışmanlık yaptığı sırada gönderdiği bir mesajda da benzer bir sistemden bahsedilmektedir](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry). "CoinJoin" teriminin kendisi Greg Maxwell tarafından icat edilmemiş olabilir, ancak Peter Todd'un bir fikrinden kaynaklanıyor olabilir.