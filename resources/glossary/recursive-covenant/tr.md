---
term: Özyinelemeli (covenant)
definition: Mevcut işleme ve onu süresiz olarak takip eden tüm işlemlere koşullar dayatan covenant.
---

Bitcoin üzerindeki özyinelemeli bir sözleşme, yalnızca mevcut işleme değil, aynı zamanda bu işlemin çıktılarını harcayan gelecekteki işlemlere de koşullar getiren bir Smart contract türüdür. Bu, her birinin zincirdeki ilk işlem tarafından tanımlanan belirli kurallara uyması gereken işlem zincirlerinin oluşturulmasına olanak tanır. Tekrarlanabilirlik, her birinin kısıtlamaları ana işleminden devraldığı bir dizi işlem oluşturur. Bu, bitcoinlerin nasıl harcanabileceği üzerinde karmaşık ve uzun vadeli bir kontrol sağlar, ancak aynı zamanda harcama özgürlüğü ve değiştirilebilirlikle ilgili riskleri de beraberinde getirir.


Özetlemek gerekirse, yinelemesiz bir taahhüt kendisini yalnızca kuralları belirleyen işlemin hemen ardından gelen işlemle sınırlayacaktır. Buna karşılık, özyinelemeli bir sözleşme, bir KİS-2'ye süresiz olarak belirli koşullar getirme yeteneğine sahiptir. İşlemler birbirini takip edebilir, ancak söz konusu KİS-2 her zaman kendisine eklenmiş olan başlangıç koşullarını koruyacaktır. Teknik olarak, bir UTXO'ün `scriptPubKey'i, söz konusu UTXO'ü harcayan bir işlemin çıktılarının `scriptPubKey'i üzerinde kısıtlamalar tanımladığında, yinelemesiz bir sözleşmenin kurulması gerçekleşir. Öte yandan, bir UTXO'ün `scriptPubKey'i, söz konusu UTXO'ü harcayan bir işlemin çıktılarının `scriptPubKey'i ve bu UTXO'ün harcanmasını takip edecek tüm `scriptPubKey'ler üzerinde kısıtlamalar tanımladığında, özyinelemeli bir sözleşmenin kurulması gerçekleşir.


Daha genel olarak, bilgi işlemde "tekrarlanabilirlik" olarak adlandırılan şey, bir fonksiyonun kendini çağırarak bir tür döngü yaratma yeteneğidir.