---
term: BIP0143
---

SegWit sonrası komut dosyalarında imza doğrulaması için işlemi karma hale getirmenin yeni bir yolunu sunar. Amaç, doğrulama sırasında gereksiz işlemleri en aza indirmek ve UTXO'ların değerini imzadaki girdiye dahil etmektir. Bu, orijinal işlem karma algoritması ile ilgili iki önemli sorunu çözer:


- İmza sayısı ile veri karma işleminin ikinci dereceden büyümesi;
- İmzaya girdi değerinin dahil edilmemesi, özellikle gerçekleşen işlem ücretlerinin bilinmesiyle ilgili olarak donanım cüzdanları için bir risk oluşturuyordu.

BIP141'de açıklanan SegWit güncellemesi, senaryosu eski düğümler tarafından doğrulanmayacak yeni bir işlem biçimi getirdiğinden, BIP143 bu sorunu bir Hard Fork gerektirmeden Address için bu fırsatı kullanır. Bu nedenle BIP143, SegWit Soft Fork'nin bir parçasıdır.