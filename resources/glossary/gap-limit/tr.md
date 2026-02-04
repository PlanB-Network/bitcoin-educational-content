---
term: Gap limit
definition: İşlem aramayı durdurmadan önceki maksimum ardışık kullanılmayan adres sayısı.
---

Bitcoin Wallet yazılımında, ek işlemlerin aranmasını durdurmadan önce generate'a ardışık kullanılmayan adreslerin maksimum sayısını belirlemek için kullanılan bir parametre. Tüm işlemlerin bulunduğundan emin olmak için bir Wallet kurtarılırken bu parametrenin ayarlanması genellikle gereklidir. Yetersiz bir Boşluk Sınırı, türetme aşamaları sırasında adresler atlanmışsa bazı işlemlerin kaçırılmasına neden olabilir. Boşluk Sınırının artırılması, Wallet'ün ilişkili tüm işlemleri kurtarmak için Address dizisinde daha fazla arama yapmasını sağlar.


Gerçekten de, tek bir `xpub' teorik olarak 4 milyardan fazla alıcı adresi (hem iç hem de dış adresler) türetebilir. Ancak, Wallet yazılımı büyük bir operasyonel maliyete katlanmadan bunların hepsini türetemez ve kullanım açısından kontrol edemez. Bu nedenle, normalde tüm Wallet yazılımlarının adresleri üretme sırası bu olduğundan, dizin sırasına göre ilerlerler. Yazılım bir sonrakine geçmeden önce kullanılan her Address'ü kaydeder ve art arda bir dizi boş adresle karşılaştığında aramasını durdurur. Bu sayı Boşluk Sınırı olarak adlandırılır.


Örneğin, Boşluk Sınırı `20` olarak ayarlanmışsa ve Address `m/84'/0'/0'/0/15/` boşsa, Wallet `m/84'/0'/0'/0/34/`e kadar olan adresleri türetecektir. Bu adres aralığı kullanılmamışsa, arama burada durur. Sonuç olarak, Address `m/84'/0'/0'/0/40/` adresini kullanan bir işlem bu örnekte tespit edilemeyecektir.