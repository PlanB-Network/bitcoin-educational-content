---
term: Coinjoin
definition: Birkaç kullanıcının bitcoin takibini zorlaştırmak için işlemlerini birleştirdiği karıştırma tekniği.
---

CoinJoin, bitcoinlerin izlenebilirliğini kırmak için kullanılan bir tekniktir. Aynı adı taşıyan belirli bir yapıya sahip işbirlikçi bir işleme dayanır: CoinJoin işlemi. CoinJoin işlemleri, dışarıdan gözlemcilerin işlemleri analiz etmesini daha zor hale getirerek Bitcoin kullanıcılarının gizlilik korumasını geliştirmeye yardımcı olur. Bu yapı, tek bir işlemde birden fazla coinin karıştırılmasına olanak tanıyarak giriş ve çıkış adresleri arasındaki bağlantıların belirlenmesini zorlaştırır.


CoinJoin'ün genel işleyişi şu şekildedir: karıştırmak isteyen farklı kullanıcılar bir işlemin girdisi olarak bir tutar yatırır. Bu girdiler aynı miktarın farklı çıktıları olarak ortaya çıkacaktır. İşlemin sonunda hangi çıktının hangi kullanıcıya ait olduğunu belirlemek mümkün değildir. CoinJoin işleminin girdileri ve çıktıları arasında teknik olarak hiçbir bağlantı yoktur. Her bir kullanıcı ile her bir UTXO arasındaki bağlantı, her bir Coin'ün geçmişinde olduğu gibi kopuktur.





Herhangi bir kullanıcı herhangi bir zamanda fonları üzerindeki kontrolünü kaybetmeden CoinJoin'ya izin vermek için, işlem önce bir koordinatör tarafından oluşturulur ve daha sonra her kullanıcıya iletilir. Daha sonra her biri kendi tarafındaki işlemin kendilerine uygun olduğunu doğruladıktan sonra imzalar ve ardından tüm imzalar işleme eklenir. Eğer bir kullanıcı veya koordinatör CoinJoin işleminin çıktılarını değiştirerek diğerlerinin fonlarını çalmaya çalışırsa, imzalar geçersiz olacak ve işlem düğümler tarafından reddedilecektir. Katılımcıların çıktılarının kaydı, girdi ile bağlantıyı önlemek için Chaum'un kör imzaları kullanılarak yapıldığında, bu "Chaumian CoinJoin" olarak adlandırılır.


Bu mekanizma, Bitcoin protokolünde değişiklik yapılmasını gerektirmeden işlemlerin gizliliğini artırır. CoinJoin'in Whirlpool, JoinMarket veya Wabisabi gibi özel uygulamaları, katılımcılar arasındaki koordinasyon sürecini kolaylaştırmak ve CoinJoin işleminin verimliliğini artırmak için çözümler sunar. İşte bir CoinJoin işlemi örneği:


```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```


CoinJoin'da Bitcoin fikrini ilk kimin ortaya attığını ve David Chaum'un kör imzalarını bu bağlamda kullanma fikrinin kime ait olduğunu kesin olarak belirlemek zordur. Genellikle Gregory Maxwell'in [2013'te BitcoinTalk'taki bir mesajda] bu konuyu ilk tartışan kişi olduğu düşünülmektedir (https://bitcointalk.org/index.php?topic=279249.0):

Chaum kör imzalarını kullanma: Kullanıcılar bağlanır ve girdilerin yanı sıra (ve adresleri değiştirerek) özel paralarını göndermek istedikleri Address'nin kriptografik olarak blinded versiyonunu sağlar; sunucu tokenları imzalar ve geri gönderir. Kullanıcılar anonim olarak yeniden bağlanır, çıktı adreslerinin maskesini kaldırır ve bunları sunucuya geri gönderir. Sunucu tüm çıktıların kendisi tarafından imzalandığını ve sonuç olarak tüm çıktıların geçerli katılımcılardan geldiğini görebilir. Daha sonra insanlar yeniden bağlanır ve imzalar.

Maxwell, G. (2013, 22 Ağustos). *CoinJoin: Gerçek dünya için Bitcoin gizliliği*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0


Bununla birlikte, hem karıştırma bağlamında Chaum imzalarından hem de coinjoin'lerden daha önce bahsedilmiştir. [Haziran 2011'de Duncan Townsend BitcoinTalk'ta](https://bitcointalk.org/index.php?topic=12751.0) Chaum imzalarını modern Chaumian coinjoin'lere oldukça benzer bir şekilde kullanan bir karıştırıcı sunar. Aynı başlıkta, [Duncan Townsend'e yanıt olarak hashcoin'den bir mesaj](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) karıştırıcısını geliştirmek için. Bu mesajda coinjoins'e en çok benzeyen şey sunulmaktadır. Alex Mizrahi'nin 2012'de Tenebrix'in yaratıcılarına danışmanlık yaptığı sırada gönderdiği bir mesajda](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry) da benzer bir sistemden bahsedilmektedir. "CoinJoin" teriminin kendisi Greg Maxwell tarafından icat edilmemiştir, ancak Peter Todd'un bir fikrinden ortaya çıkmıştır.


