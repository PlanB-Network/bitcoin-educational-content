---
term: YENIDEN KULLANILABILIR ÖDEME KODU
---

BIP47'de, yeniden kullanılabilir bir ödeme kodu, bir bildirim işlemine ve benzersiz adreslerin türetilmesine olanak tanıyan bir Bitcoin Wallet'den üretilen statik bir tanımlayıcıdır. Bu, her ödeme için yeni, kullanılmayan adresleri manuel olarak türetmek ve iletmek zorunda kalmadan gizlilik kaybına yol açan adreslerin yeniden kullanılmasını önler. BIP47'de yeniden kullanılabilir ödeme kodları aşağıdaki şekilde oluşturulur:


- Bayt 0 versiyona karşılık gelir;
- Bayt 1, özel kullanım durumunda bilgi eklemek için bir bit alanıdır;
- Bayt 2, açık anahtarın `y` paritesini gösterir;
- 3. bayttan 34. bayta kadar, açık anahtarın `x` değerini bulacaksınız;
- Bayt 35'ten bayt 66'ya kadar, açık anahtarla ilişkili chain code vardır;
- 67. bayttan 79. bayta kadar sıfır dolgu vardır.


Genellikle ödeme kodunun başına bir İnsan Tarafından Okunabilir Parça (HRP) ve sonuna bir sağlama toplamı eklenir ve ardından base58'de kodlanır. Dolayısıyla bir ödeme kodunun yapısı genişletilmiş bir anahtarınkine oldukça benzerdir. İşte benim BIP47 ödeme kodumun base58'deki hali:


```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```


BIP47'nin PayNym uygulamasında, ödeme kodları bir robotun görüntüsüyle ilişkili tanımlayıcılar şeklinde de ifade edilebilir. Örneğin benimki burada:


```text
+throbbingpond8B1
```


PayNym uygulaması ile ödeme kodlarının kullanımı şu anda PC'de Sparrow wallet'te ve mobilde Samourai Wallet'te mevcuttur.