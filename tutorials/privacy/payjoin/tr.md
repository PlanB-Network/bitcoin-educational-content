---
name: PayJoin
description: Bitcoin üzerindeki PayJoin nedir?
---
![Payjoin thumbnail - steganography](assets/cover.webp)








## PayJoin'yi Anlama Bitcoin Üzerindeki İşlemler


PayJoin, ödeme alıcısı ile işbirliği yaparak ödeme sırasında kullanıcı gizliliğini artıran özel bir Bitcoin işlem yapısıdır.


2015 yılında [LaurentMT](https://twitter.com/LaurentMT) ilk olarak [buradan](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt) erişilebilen bir belgede bu yöntemden "steganografik işlemler" olarak bahsetmiştir. Bu teknik daha sonra Samourai Wallet tarafından benimsenmiş ve 2018 yılında Stowaway aracı ile uygulayan ilk istemci olmuştur. PayJoin kavramı [BIP79](https://github.com/Bitcoin/bips/blob/master/bip-0079.mediawiki) ve [BIP78](https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki)'de de yer almaktadır. PayJoin'e atıfta bulunmak için çeşitli terimler kullanılmaktadır:


- PayJoin
- Kaçak Yolcu
- P2EP (Pay-to-End-Point)
- Steganografik işlem


PayJoin'nın benzersizliği, ilk bakışta sıradan görünen ancak aslında iki taraf arasında mini bir CoinJoin olan bir işlemi generate yapabilmesinde yatmaktadır. Bunu başarmak için işlem yapısı, girdilerdeki gerçek göndericinin yanı sıra ödeme alıcısını da içerir. Alıcı, işlemin ortasında kendisine ödeme yapılmasını sağlayan bir ödeme içerir.


Somut bir örnek verelim: `10.000 Sats`lik bir UTXO kullanarak `4000 Sats`lik bir baget satın alırsanız ve PayJoin'yi tercih ederseniz, fırıncınız `4000 Sats`inize ek olarak, girdi olarak kendilerine ait olan ve çıktı olarak tam olarak alacakları `15.000 Sats`lik bir UTXO ekleyecektir:

![Payjoin transaction diagram](assets/en/1.webp)


Bu örnekte, fırıncı girdi olarak `15,000 Sats` verir ve bagetin fiyatı olan tam `4000 Sats`lik bir farkla `19,000 Sats` ile çıkar. Sizin tarafınızda, `10,000 Sats` ile girersiniz ve çıktı olarak `6,000 Sats` ile sonuçlanırsınız, bu da bagetin fiyatı olan `-4000 Sats`lik bir dengeyi temsil eder. Örneği basitleştirmek için, bu işlemde Mining ücretlerini kasıtlı olarak ihmal ettim.


## PayJoin işleminin amacı nedir?


Bir PayJoin işlemi, kullanıcıların ödemelerinin gizliliğini artırmalarına olanak tanıyan iki amaca hizmet eder.

Öncelikle PayJoin, zincir analizinde bir yem oluşturarak harici bir gözlemciyi yanıltmayı amaçlamaktadır. Bu, Ortak Girdi Ownership Sezgiselliği (CIOH) ile mümkün olmaktadır. Genellikle, Blockchain üzerindeki bir işlemin birden fazla girdisi olduğunda, tüm bu girdilerin muhtemelen aynı tüzel kişiye veya kullanıcıya ait olduğu varsayılır. Dolayısıyla, bir analist bir PayJoin işlemini incelediğinde, tüm girdilerin aynı kişiden geldiğine inanmaya yönlendirilir. Ancak bu algı yanlıştır çünkü asıl ödeme yapan kişinin yanı sıra ödeme alıcısı da girdilere katkıda bulunmaktadır. Dolayısıyla, zincir analizi yanlış olduğu ortaya çıkan bir yoruma doğru yönlendirilir.


Ayrıca PayJoin, dışarıdan bir gözlemcinin yapılan ödemenin gerçek tutarı konusunda aldatılmasına da olanak tanımaktadır. İşlem yapısını inceleyen analist, ödemenin çıktılardan birinin tutarına eşdeğer olduğuna inanabilir. Ancak gerçekte ödeme tutarı herhangi bir çıktıya karşılık gelmemektedir. Aslında alıcının UTXO çıktısı ile alıcının UTXO girdisi arasındaki farktır. Bu anlamda, PayJoin işlemi steganografi alanına girer. Bir işlemin gerçek tutarının yem görevi gören sahte bir işlem içinde gizlenmesine olanak tanır.


Lütfen **Stenografi** tanımımıza dikkat edin:

> Steganografi, gizli bilginin varlığının algılanamayacağı şekilde diğer veri veya nesneler içinde bilgi gizleme tekniğidir. Örneğin, gizli bir mesaj, kendisiyle hiçbir ilgisi olmayan bir metindeki bir noktanın içine gizlenerek çıplak gözle algılanamaz hale getirilebilir (bu mikro nokta tekniğidir). Şifre çözme anahtarı olmadan bilgiyi anlaşılmaz hale getiren şifrelemenin aksine, steganografi bilgiyi değiştirmez. Açık bir şekilde görüntülenmeye devam eder. Amacı daha ziyade gizli mesajın varlığını gizlemektir, oysa şifreleme, anahtar olmadan erişilemez olmasına rağmen gizli bilginin varlığını açıkça ortaya koyar.

Baget ödemesi için PayJoin işlemi örneğimize geri dönelim.

![Payjoin transaction schema from the outside](assets/en/2.webp)

Bu işlemi Blockchain üzerinde gören ve zincir analizinin olağan sezgisel yöntemlerini takip eden bir dış gözlemci bunu şu şekilde yorumlayacaktır: "*Alice, Bob'e `19.000 Sats` ödemek için işlemin girdileri olarak 2 UTXO'yu birleştirdi*."

![Incorrect interpretation of Payjoin transaction from the outside](assets/en/3.webp)

Bu yorum açıkça yanlıştır çünkü bildiğiniz gibi, iki girdi UTXO'su aynı kişiye ait değildir. Ayrıca, ödemenin gerçek değeri `19,000 Sats` değil, `4,000 Sats`tir. Dış gözlemcinin analizi böylece hatalı bir sonuca yönlendirilerek paydaşların gizliliğinin korunması sağlanır![PayJoin işlem diyagramı](assets/en/1.webp)

Gerçek bir PayJoin işlemini analiz etmek isterseniz, işte Testnet üzerinde yaptığım bir işlem: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://Mempool.space/fr/Testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)







**Harici kaynaklar:**

- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki.
- https://payjoin.org/
https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

