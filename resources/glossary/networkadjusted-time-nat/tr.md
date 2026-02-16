---
term: Ağa göre ayarlanmış zaman (NAT)
definition: Ağ düğümlerinin saatlerinin medyanına dayanan evrensel zaman tahmini.
---

Ağ düğümlerinin saatleri üzerine kurulu evrensel zaman tahmini. Her düğüm, kendi yerel saati (UTC) ile bağlı olduğu düğümlerin saatleri arasındaki zaman farklarının medyanını alarak NAT'ını hesaplar ve ardından kendi yerel saatini bu farkların medyanına en fazla 70 dakikaya kadar ekler. Dolayısıyla ağa göre ayarlanmış zaman, her düğüm tarafından yerel olarak hesaplanan düğüm zamanlarının ortancasıdır. Bu referans çerçevesi daha sonra blok zaman damgalarının geçerliliğini doğrulamak için kullanılır. Aslında, bir bloğun bir düğüm tarafından kabul edilebilmesi için Timestamp'ın MTP (son 11 çıkarılan bloğun medyan zamanı) ile NAT artı 2 saat arasında olması gerekir:


```text
MTP < Valid Timestamp < (NAT + 2h)
```