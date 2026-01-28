---
term: Çoklu imza (Multisig)
definition: Bir harcamayı yetkilendirmek için farklı anahtarlardan birkaç imza gerektiren cüzdan.
---

Genellikle "Multisig" olarak kısaltılan çoklu imza cüzdanları, bir harcamayı yetkilendirmek için farklı özel anahtarlardan birden fazla imza gerektirerek bitcoinlerin güvenliğini artırmak için tasarlanmıştır. Bu yöntem, riski birkaç anahtar arasında dağıtarak hem kayıp hem de hırsızlık riskini azaltmaya yardımcı olur (Multisig yapılandırmasına bağlı olarak). Multisig cüzdanları "m-of-n" modelinde çalışır; burada `m` bir işlemi doğrulamak için gereken minimum imza sayısını, `n` ise ilgili toplam anahtar sayısını temsil eder. Örneğin, 3'te 2 kurulumu bir işlemi doğrulamak için olası üç imzadan ikisini gerektirir. Bu yaklaşım, tek anahtarlı cüzdanlara kıyasla daha üstün güvenlik sunar, ancak aynı zamanda yönetim ve yedekleme açısından daha fazla karmaşıklık getirir. Dahası, eski Multisig standartlarını kullanan işlemler geleneksel tek anahtarlı işlemlere kıyasla daha az özeldir ve ücretleri daha pahalıdır. Bununla birlikte, Taproot ve tanımlayıcıların kullanımı gibi son yeniliklerin, multisiglerin bu dezavantajlarını ortadan kaldırmasa bile en aza indirmesi beklenmektedir.


> ► *Bazı bitcoinciler "Multisig" ve "Eşik Multisig" terimleri arasında ayrım yapmaktadır Gerçekten de bazıları bir Multisig'ün mutlaka bir n-of-n olduğunu, eşik Multisig'ün ise bir m-of-n olduğunu savunmaktadır. Bununla birlikte, yaygın dilde m-of-n için bile "Multisig" ifadesi kabul görmektedir.*