---
name: JoinMarket

description: Komut satırı aracılığıyla Bitcoin üzerinden CoinJoin yapmak için JoinMarket'in nasıl kullanılacağına dair kılavuz ve öğretici
---

![cover](assets/cover.webp)



---

Eğer bu sayfayı internette "JoinTmarket" araması yaparak bulduysanız, size en içten takdirlerimi sunarım. Ancak, tamamen farklı ama son derece ilginç bir konuyla ilgilenen bir rehbere rastladınız! 🚬🍁



Bu eğitimin amacı, JoinMarket'in komut satırı üzerinden teorik ve pratik çalışmasını göstermektir. 🐢 💚



## JoinMarket Teorik Tanım



JoinMarket'i, diğer kullanıcılarla CoinJoin'ü tamamen Trustless bir şekilde ve herhangi bir merkezi koordinatör olmadan sağlayan bir araç veya bir Wallet olarak tanımlayabiliriz.



Bu aracın tüm teorik kısmı son derece geniş olduğundan, podcast'imin belirli bir bölümünde Address'e karar verdim. İtalyanca anlayabilenler için, bu programı düzgün bir şekilde kullanmak için temel kavramları daha iyi özümsemek amacıyla bölümü dinledikten sonra okumaya devam etmenizi şiddetle tavsiye ederim.



Bölümü bu doğrudan bağlantılardan takip edebilirsiniz:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (buradan doğrudan tarayıcıdan dinleyebilirsiniz).
- [Antenna pod](https://antennapod.org/) kayıt gerektirmeyen ücretsiz ve açık kaynaklı bir podcast yöneticisidir. Bölümü bulmak için uygulamayı indirin, _feed rss_ bölümüne [this link](https://Anchor.fm/s/bd5d5b20/podcast/rss) adresini yapıştırarak podcast'imi manuel olarak ekleyin, ardından JoinMarket'e adanmış bölümü arayın.



## Kurulum



İşletim sistemleri:





- Raspiblitz
- Şemsiye
- MyNode
- Raspibolt



## Yapılandırma Dosyaları



JoinMarket sonsuz sayıda ayara sahip özelleştirilebilir bir yazılımdır; bu ayarlar ana program dizininde bulunan `Joinmarket.cfg` adlı bir yapılandırma dosyasında belirtilir.



Bu bölümde, ihtiyaçlarınıza bağlı olarak keşfetmeyi ve/veya değiştirmeyi ilginç bulabileceğiniz bazı alanların üzerinden geçeceğiz. Aşağıda listelenen tüm değişikliklerin, zorunlu olmamakla birlikte, yazılımın çalışmasını kişisel ihtiyaçlara uyarlamak için bilinmesinin yararlı olduğunu vurgulamak isterim.



Öncelikle `joinmarket/scripts` klasörüne gidelim ve komutu çalıştıralım:



```bash
python wallet-tool.py generate
```


Bu noktada bir hata almamız gerekir, ancak bunu yapmak yazılımın bizim için önceden ayarlanmış bir ayar dosyasını generate yapmasına neden olacaktır. Terminalden ayar dosyasını şu şekilde düzenleyebiliriz:



```bash
nano joinmarket.cfg
```



ya da:



```bash
vim joinmarket.cfg
```



açıldığında, çeşitli ayarlar ve bunların İngilizce açıklamalarını içeren çok sayıda satır göreceğiz. Özellikle en ilginç değişkenleri aşağıda analiz edeceğiz:





- yapıcı olarak yapmamız durumunda `merge_algorithm` bu alan yazılımın harcanmamış Çıktıları ne kadar agresif bir şekilde konsolide edeceğini ayarlar. Birleştirilecek çok sayıda UTXO'muz olması durumunda, _gradual_'dan _greedy_'e geçmek mantıklı olabilir
- tx_fees` işlemin ödeneceği ücretleri bir alıcı olarak ayarlar, tumbler'ı sık kullanmanız durumunda bu ayarı değiştirmek çok yararlıdır (bundan daha sonra bahsedeceğiz) çünkü ikincisinin yürütülmesi sırasında ücretlerde bir artış olursa, bu alanı doğru ayarlamazsak, CoinJoin için çok fazla Sats harcama riskimiz vardır. Değerleri binlik olarak ayarladığınızda (örneğin 2000) bu 2 Sats/vByte'a, 3500 3,5 Sats/vByte'a vb. eşit olacaktır. İhtiyaçlarınıza bağlı olarak 1500 ila 6000 arasında değişen bir sayı tavsiye ederim.
- max_cj_fee_abs`, CoinJoin sırasında seçtiğimiz yapımcılar için mutlak olarak ne kadar ödemek istediğimizi belirtmek için kullanılır. Yapımcılar için bu alan varsayılan olarak 200 Sats'tür, iyi bir seçenek karşı taraf başına 200 ila 1000 Sats arasında değişen bir sayı olabilir (bu, ne kadar harcamak istediğinize ve CoinJoin'leriniz için ne kadar anon-set aradığınıza bağlıdır)
- max_cj_fee_rel` yukarıdaki alanla aynı işleve sahiptir, ancak her bir karşı tarafa ödemek istediğimiz göreceli ücretleri (yüzdeler) belirtir. Bu bir `yüzde` değeri olduğundan, büyük miktarlı CoinJoin'lerde yüksek maliyetlerden kaçınmak için yüksek değerler ayarlamamaya dikkat edin. Maker'lar için varsayılan değer _0.00002_'dir, benzer veya biraz daha yüksek bir değer öneririm.
- `minimum_makers` kaç tane karşı tarafla CoinJoin yapacağımızı belirten alandır, varsayılan olarak joinMarket her zaman 4 ila 9 karşı taraf seçer, daha fazla gizlilik için istersek bu değeri 5 veya 6'ya yükseltebiliriz (yine de işlemleri daha pahalı hale getirecektir).
- cjfee_a`, bir yapımcı olarak hareket etmemiz durumunda, likiditemizi kiralamak için mutlak olarak kaç Sats toplamak istediğimizi belirtir. Bu alan tamamen özneldir, varsayılan değer zaten çok iyidir (böylece bir yapımcı olarak daha iyi gizliliğe sahip olacağız) daha kısa sürede daha fazla CoinJoin kazanmak istiyorsak 0'a almayı düşünebiliriz.
- cjfee_r` yukarıdaki alanla aynıdır ancak mutlak değil yüzde cinsindendir. Yine varsayılan değeri bırakmanızı veya daha fazla alıcı çekmek için düşürmenizi öneririm.
- `ordertype` bu alan ile maker'dan mutlak (absoffer) veya yüzdelik (reloffer) ücretlendirmeyi seçeriz. Genellikle alıcılar ekonomik konular için mutlak teklifleri tercih ederler.
- `minsize` eğer bir yapımcı olarak UTXO'nin çok küçük olmasını istemiyorsak, katılmak için minimum CoinJoin'yi belirtebiliriz. Bu alan Satoshi olarak ifade edilir ve tamamen özneldir. Bu alanı 0'da bırakabilir veya 500000 (Sats), 1000000 (Sats) vb. değerlere yükseltebiliriz.



Yanlış alanları düzenlememek için çok dikkatli olun, joinmarket.cfg dosyasındaki bazı değişkenler yanlış ayarlanırsa yazılımın işlevselliğini tehlikeye atabilir veya gizliliğinizi tamamen yok edebilir, gözler açık ve maksimum dikkat!



## Çalışma Ortamı Kurulumu



Bazı düğümler joinmarket.cfg dosyasında bu alanlar için doğru değerleri otomatik olarak ayarlar, manuel olarak tekrar kontrol etmenizi öneririm:





- `rpc_user = yourusername-as-in-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #default genellikle doğru`
- `rpc_port = 8332 # Mainnet için varsayılan`



Bu noktada JoinMarket içinde Wallet'ümüzü oluşturmaya devam edebiliriz:



```bash
python wallet-tool.py generate
```



Bu komut, Wallet'i şifrelemek için bir şifre ve vermek istediğimiz adı girmemizi sağlayacaktır, size sadakat bağlarını desteklemek isteyip istemediğinizi sorduğunda _yes_ seçeneğini kullanmanızı tavsiye ederim, döndürülen çıktı aşağıdaki gibi görünecektir:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


bir hata görünmesi durumunda, büyük olasılıkla yukarıda belirtilen 4 RPC alanını yanlış ayarlamışızdır. Bu durumda, orijinal JoinMarket belgelerinde bulunan [bu kılavuzu] (https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) takip etmek yardımcı olabilir.



Çalışma ortamımızın kurulumunu tamamladık ve bizim için en yararlı olacak komutları keşfetmeye başlayabiliriz. Tartışacağımız tüm betikler konsolda başlatılabilir ve ardından derinlemesine bir açıklama için `-help` ile devam edilebilir.



Şimdi fırlatmayı deneyebiliriz:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



bu komut size çeşitli Wallet mixdepths ile kategorize edilmiş çeşitli adresleri gösterecektir:




- Yeni (Address hiç kullanılmadı)
- Değişim (önceki bir işlemin kalanı)
- Cj-out (bir CoinJoin'un çıkışı)



i̇şte sonucun pratik bir örneği:



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


Şimdi ilk Satoshilerimizi bir veya daha fazla adrese yatırmaya devam edebiliriz, yapımcı veya alıcıdan bağımsız olarak, yazılımın asla gidip UTXO'i doğrudan farklı karışım derinliklerinde birleştirmeyeceğini hatırlayarak, bu şekilde farklı gizlilik seviyelerine sahip Satoshileri Wallet içinde ayrı tutabiliriz.



## Bitcoin'ün CoinJoin Tekli ile Gönderilmesi



Artık Satoshilerimizi hareket ettirebiliriz. Bu yazılımdaki ana komutlardan biri komut dosyasıdır:



```bash
pyhton sendpayment.py
```


gW-34 ile veya CoinJoin olmadan başka adreslere işlem göndermemizi sağlayacak. Şimdi nasıl çalıştığını ve bazı pratik örnekleri gözden geçirelim. Varsayılan olarak komutun biçimlendirmesi şöyledir (< ve > sembolleriyle çevrelenmiş metni değiştirmeyi unutmayın):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



temel bir kullanım örneği şöyle olabilir:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


bu durumda Address'ya 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc yani 5000000 Satoshi'yi mixdepth 0'dan (varsayılan olan) CoinJoin için 4 ila 9 karşıt seçerek (varsayılan seçenek) göndereceğiz.



Hangi UTXO'ların nasıl harcanacağı konusunda daha fazla kontrol sahibi olmak için bu komutun ek seçeneklerini gözden geçirebiliriz:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


bu örnekte iki özellik ekledik: -N, kaç karşı tarafla karışım yapacağımızı, -m ise fon çekeceğimiz karışım derinliğini gösterir. Aslında, mixdepth 1'deki fonlarla ve 5 karşı tarafla karıştırarak Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c'ye 100.000.000 Sats (1 btc) gönderdik.



Bir mixdepth belirterek send değeri olarak 0 koyarsak joinMarket `sweep` denilen işlemi gerçekleştirecek, yani o mixdepth içindeki tüm fonları birbiriyle konsolide ederek gönderecektir:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



burada tüm fonları mixdepth 0'dan gönderdik (bunu belirtmeyebilirdik çünkü bu varsayılandır) ve 7 muadil ile karıştırdık.



Sendpayment komutu, joinMarket'ten harici Wallet'e para taşımak veya bir kişiyle aramıza bir Layer gizlilik ekleyerek ona Satoshi göndermek için kullanılır. UTXO'larımızda yeterli düzeyde gizlilik elde etmek için, bu kılavuzun ilerleyen bölümlerinde açıklayacağımız tumbler.py komutunu kullanmak daha uygundur.



## Maker Olmak



Bu bölümde ele alacağımız senaryo şudur:



```bash
yg-privacyenhanced.py
```



Bu program joinMarket'te bir yapımcı olarak hareket etmek için kullanılır. Yazılım, Bitcoin düğümümüze ve üreticilerin kendilerini likidite teklifçileri olarak sundukları ve alıcıların karşı tarafları aradıkları platformun iç pazarına bağlanacaktır. Bir sadakat bonosu kullanmak istemeniz durumunda, bu biçimlendirme ile bir tane oluşturabilirsiniz:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



örneğin:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



bize iade edilecek çıktı bir Bitcoin Address olacaktır (yani, fidelity'ye tahsis etmek istediğiniz fonları yatırmanız gereken çıktı).



**Dikkat**: Bir Fidelity Bond (a.k.a. FB) oluşturacaksanız çok dikkat etmeniz gereken iki şey vardır;





- fonlar bir kez yatırıldıktan sonra, süresi dolana kadar tekrar taşınamazlar. Address'ya kaç Sats gönderdiğinize ve tarihi nasıl biçimlendirdiğinize dikkat edin. Hatalara izin verilmez!
- Sadakat bonosu zincir üzerinde kolayca tanınabilir, bu nedenle bir CoinJoin aracılığıyla ve kimliğinizle ilgisi olmayan bir kaynakla para yatırmanız önerilir. Aynı şeyi, süresi dolan sadakat bonosunu JoinMarket'in dışına taşımak istediğinizde de yapmanız önerilir.



Sadakat bonosunun yalnızca bir işlemle yeniden yüklenmesinin mümkün olduğunu, UTXO katları durumunda yalnızca en büyük olanın FB için geçerli sayılacağını unutmamak önemlidir.



Şimdi bu paragrafın başında bahsedilen komut dosyasını ele alalım, sadakat bağını oluşturduktan sonra (isteğe bağlı olduğunu hatırlıyoruz) joinMarket'te bir yapımcı olarak hareket etmek için yürütülebilir dosyayı çalıştırmaya hazırız. Sats'lar çeşitli adreslere ve mixdepth'e yatırıldıktan sonra komutu çalıştırabiliriz:



```bash
python yg-privacyenhanced.py <wallet name>
```



Bu noktadan itibaren (ağa bağlandıktan birkaç dakika sonra) ve komut dosyasını durdurana kadar, JoinMarket istemcimiz protokoldeki aktif yapıcılar listesinde görünecek ve CoinJoin yapmak için likiditemizi çeşitli karşı taraflara sunacaktır. Günde düzinelerce CoinJoins beklemeyin (Wallet'de büyük bir fidlity ve büyük likidite yatırmadığınız sürece), ayrıca gerekli ücretler ve yatırılan Satoshiler gibi faktörlerin ne sıklıkta bir yapımcı olacağınızı etkilediğini unutmayın.



Aşağıdaki komutu çalıştırarak Wallet'de yapılan tüm işlemlerin geçmişini ve Wallet'in ömrü boyunca elde ettiğiniz herhangi bir kazancı (eğer bir yapıcıysanız) veya ücret giderini (eğer bir alıcıysanız) görebileceksiniz.



```bash
python wallet-tool.py <wallet name> history
```



Satoshileriniz CoinJoins yaptıktan sonra, sonuncuya ulaşana kadar karışım derinliğinden karışım derinliğine hareket edeceklerdir. Dördüncüyü geçtikten sonra karışım derinliği 0'a döneceklerdir, onları bir Cold Wallet'ye taşımadan önce ne kadar gizlilik elde edeceğiniz size bağlıdır, tam bir Wallet döngüsünü bitirmeniz tavsiye edilir.



## Bardak



İşte sonunda JoinMarket'in en lezzetli kısmına geldik, tumbler! Podcast'i dinlediyseniz, bunun neyle ilgili olduğunu zaten biliyorsunuzdur. Başlamadan önce bir tavsiye: **joinmarket.cfg dosyasındaki limitleri ayarlamayı unutmayın (başlangıçta açıklandığı gibi) ve programı yalnızca zincir içi ücretler nispeten düşük olduğunda (10 Sats/vB'nin altında) çalıştırmayı düşünün.



Tumbler'ı başlatmak için script'i maker'dan durdurmuş olmak gerekir (eğer aktifse), bundan sonra komutu çalıştırabiliriz:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Tumbler için **en az** 3 çıkış adresi girmek önemlidir: bu, iyi bir gizlilik sağlamak ve süreç boyunca UTXO'lar arasında bariz bağlantılar oluşturmamak içindir. Her zamanki gibi komuta `-help` ekleyerek tüm ek ayrıntıları görebilirsiniz. Gelişmiş kurallar içeren daha karmaşık bir örneği görüntüleyelim:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



Bu durumda, varsayılan muadil sayısını kullanmayacak (-N parametresi, maksimum 2 varyansla 7 muadile ihtiyacımız olduğunu gösterir, bu nedenle 5 ila 9 arasında rastgele sayıda yapımcı) ve karışım derinliği başına daha fazla sayıda CoinJoin ile (varsayılan olarak bu komut dosyası, CoinJoin bölümü başına 1 ila 3 arasında değişen rastgele sayıda Wallet yapar, bunun yerine -c 3 1 komutunu kullanarak 2 ila 4 arasında olacaktır) bir yuvarlama komut dosyası başlattık. Bu şekilde ücretlerde daha fazla Sats harcayacağız ancak daha büyük bir anonimlik setine sahip olacağız.



Ayrıca istediğiniz kadar çıktı adresi ekleyebilirsiniz (minimum 3, sağduyu dışında maksimum yoktur). Ancak, gizlilik nedeniyle, Satoshi'in çıktı olarak belirtilen adresler arasında nasıl dağıtılacağına karar vermek mümkün değildir.



Tumbler kasıtlı olarak uzun bir süreçtir, bazen bir şeyler çalışmayı durdurabilir, çoğu durumda bu birkaç saat içinde kendiliğinden çözülür. Tamamen çökmesi durumunda şu komutla yeniden başlatmayı deneyebiliriz:



```bash
python tumbler.py --restart
```



Ya da sadece yeni bir tamburlama komutunu yeniden başlatın. Bu, önceki tamburun zamanlamasını başlatmayacak ancak yeni bir karıştırma döngüsü başlatacaktır. Düğümünüzün SSH terminalini kapatmanın da komut dosyasını durdurması durumunda, komutla yüklenebilen `TMUX` programından yararlanabilirsiniz:



```bash
sudo apt install tmux
```



Kabuktan `tmux` yazarak başlattığınızda sizin için bir terminal açılacak ve uzak bağlantıyı kapatsanız bile arka planda aktif kalacaktır. Düğümünüze şu komutla yeniden bağlandığınızda: tmux attach` komutuyla yeniden bağlandığınızda, arka planda aktif kalan kabuğu yeniden açacaksınız.



## Sonuç



JoinMarket sınırsız ve özelleştirilebilir bir yazılımdır. Bu kılavuzda ana işlevleri keşfettik, böylece herkesin (veya en azından ben denedim, bu yazılımı kullanmanın parkta yürümek olmadığının farkındayım) kullanması mümkün. JoinMarket ile ilgili en büyük sorunlardan biri tam da bu: onu kullanan ve yapımcı olan kişi sayısı. Az sayıda kullanıcı bu yazılımdan yararlanırsa, genel gizlilik (anon-set) azalır. Bu nedenle bu kılavuzun kullanımı teşvik edeceğini ve sizi CoinJoin yapmak için en sevdiğim yazılımı indirip kurmaya ikna edeceğini umuyorum. Bazı konularda daha da derine inmek isterseniz, github'daki çeşitli derinlemesine dokümanları okumanızı tavsiye ederim, çok iyi hazırlanmışlar ve onları burada bulabilirsiniz.



Mutlu karıştırma kaplumbağaları!🐢 💚



[Burada](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) Turtlecute'u destekleyebilirsiniz