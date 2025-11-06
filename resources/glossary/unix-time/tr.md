---
term: UNIX ZAMANI
---

Unix Zamanı veya Unix Timestamp, 1 Ocak 1970, gece yarısı UTC'den (Unix Epoch) bu yana geçen saniye sayısını temsil eder. Bu sistem Unix işletim sistemlerinde ve türevlerinde zamanı evrensel ve standart bir şekilde işaretlemek için kullanılır. Zaman dilimlerinden bağımsız olarak saatlerin senkronizasyonunu ve zamana dayalı olayların yönetimini sağlar.


Bitcoin bağlamında, düğümlerin yerel saati ve dolayısıyla NAT'ın (Ağa Göre Ayarlanmış Zaman) hesaplanması için kullanılır. Ağa göre ayarlanmış zaman, her düğüm tarafından yerel olarak hesaplanan düğüm zamanlarının bir ortalamasıdır ve bu referans daha sonra blok zaman damgalarının geçerliliğini doğrulamak için kullanılır. Aslında, bir bloğun bir düğüm tarafından kabul edilebilmesi için Timestamp'in MTP (son 11 çıkarılan bloğun Geçmiş Medyan Zamanı) ile NAT artı 2 saat arasında olması gerekir:


```text
MTP < Valid Timestamp < (NAT + 2h)
```


Unix Time, blok sayısı yerine gerçek zamana dayalı olduklarında zaman kilitleri oluşturmak için de kullanılır.