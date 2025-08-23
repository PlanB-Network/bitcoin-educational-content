---
term: Invoice AYDINLATMA
---

Alıcı tarafından oluşturulan ve işlemi tamamlamak için gereken tüm bilgileri içeren yıldırım ödeme talebi.


Bir Invoice Lightning, alıcı düğümün açık anahtarı biçimindeki ödeme hedefinin yanı sıra bir `LN` öneki, miktar, sona erme süresi, HTLC'lerde kullanılan sırrın Hash'si ve yönlendirme seçenekleri gibi bazıları isteğe bağlı olan diğer meta verileri içerir. Bu faturalar BOLT11 standardı tarafından tanımlanır. Bir Invoice Lightning için ödeme yapıldıktan sonra tekrar kullanılamaz.


> ► *Fransızca'da "Invoice" kelimesini "facture" olarak çevirebiliriz, ancak Fransızca'da bile genellikle İngilizce terimi kullanırız