---
term: CISA
definition: Bir işlemin tüm girdilerinin imzalarını tek bir imzada birleştirerek boyutu ve ücretleri azaltmaya yönelik teknik öneri.
---

"Cross-Input Signature Aggregation" için kısaltma. Bu, doğrulamak için gereken imza sayısını azaltarak Bitcoin işlemlerinin boyutunu optimize etmek için tasarlanmış teknik bir öneridir.


Şu anda, Bitcoin'de, bir işlemdeki her girdinin tüketilebilmesi için ayrı bir imzaya sahip olması gerekmektedir. Bu, söz konusu UTXO'nin sahibinin işlemi yetkilendirdiğini kanıtlar. CISA ile amaç, tek bir işlemdeki tüm girdilerin imzalarını tüm girdileri kapsayan tek bir imzada birleştirmektir. Bu, çok sayıda girdisi olan işlemlerin boyutunu küçültmeyi ve dolayısıyla maliyetlerini azaltmayı mümkün kılacaktır. Bu, blok boyutlarını veya aralıklarını değiştirmeden Bitcoin'de daha fazla işlemin onaylanmasını sağlarken, coin birleşmeleri veya konsolidasyonları gerçekleştirenler için özellikle yararlı olacaktır. CISA, imzaların doğrusal olarak toplanmasını sağlayan Schnorr protokolüne dayanmaktadır. Bu, tek bir imzanın birkaç bağımsız anahtara sahip olunduğunu kanıtlayabileceği anlamına gelir.


Ancak, CISA'nın Bitcoin'te uygulanması, komut dosyalarının çalışma biçiminde köklü değişiklikler gerektirdiğinden çok karmaşıktır. Şu anda Bitcoin'te komut dosyası doğrulaması girdi bazında yapılmaktadır. CISA tarafından önerildiği gibi, tüm bir işlemin bir kerede kontrol edildiği bir modele geçmek önemsiz bir değişiklik olmaktan çok uzaktır.