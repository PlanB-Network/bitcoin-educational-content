---
term: BETTERHASH
---

Mining protokolü, Matt Corallo tarafından 2018 yılında Mining'ın havuzlar üzerinde artan merkezileşmesine karşı koymak amacıyla geliştirilmiştir. O dönemde standart olan Stratum'dan, hash'lere blok şablonlarına dahil edilecek işlemlerin seçimi üzerinde daha fazla kontrol sunarak ayrılır. BetterHash'in arkasındaki ana fikir, Mining havuzlarının azaltılmış gelir varyansı gibi avantajlarını korurken, hash'lere blok şablonu yapımını kendileri yönetme olanağını geri vermektir.


Stratum protokolünde, Mining havuzları blok şablonlarının oluşturulmasını kontrol eder, yani bloklara hangi işlemlerin dahil edileceğini seçer ve ayrıca hangi Miner zincirinde yer alacağını belirler. Bu merkezileşme, işlem onay sürecini sansüre karşı savunmasız hale getirdiği için Bitcoin'i zayıflatır.


BetterHash, ödüllerin dağıtımını havuzun yönetmesine izin verirken, chopper'ların bu işlemlerin kontrolünü geri almasına olanak tanır. Bir bakıma StratumV2'nin öncülerinden biridir.