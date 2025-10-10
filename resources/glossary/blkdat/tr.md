---
term: BLK*.DAT
---

Bitcoin core'da Blockchain'in ham blok verilerini saklayan dosyaların adı. Her dosya, adındaki benzersiz bir numara ile tanımlanır. Böylece, bloklar blk00000.dat dosyasından başlayarak kronolojik sırayla kaydedilir. Bu dosya maksimum kapasitesine ulaştığında, sonraki bloklar blk00001.dat dosyasına, ardından blk00002.dat dosyasına kaydedilir ve bu böyle devam eder. Her blk dosyasının maksimum kapasitesi 128 mebibayttır (MiB), bu da 134 megabaytın (MB) biraz üzerine denk gelmektedir. Bu dosyalar 0.8.0 sürümünden itibaren `/blocks` klasörüne taşınmıştır.