---
term: BIP
---

"Bitcoin İyileştirme Teklifi "nin kısaltmasıdır Bitcoin İyileştirme Teklifi (BIP), Bitcoin protokolünde ve standartlarında iyileştirmeler ve değişiklikler önermek ve belgelemek için resmi bir süreçtir. Bitcoin'in güncellemelere karar verecek merkezi bir kuruluşu olmadığından, BIP'ler topluluğun yapılandırılmış ve şeffaf bir şekilde iyileştirmeler önermesine, tartışmasına ve uygulamasına olanak tanır. Her BIP önerilen iyileştirmenin hedeflerini, gerekçelerini, uyumluluk üzerindeki potansiyel etkilerini, avantaj ve dezavantajlarını detaylandırır. BIP'ler topluluğun herhangi bir üyesi tarafından yazılabilir, ancak diğer geliştiriciler ve Bitcoin core GitHub veritabanını koruyan editörler tarafından onaylanmalıdır: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun ve Ruben Somsen. Ancak, bu kişilerin BIP'lerin düzenlenmesindeki rollerinin Bitcoin'i kontrol ettikleri anlamına gelmediğini anlamak önemlidir. Birisi resmi BIP çerçevesinde kabul edilmeyen bir iyileştirme önerirse, bunu yine de doğrudan Bitcoin topluluğuna sunabilir veya hatta değişikliklerini içeren bir Fork oluşturabilir. BIP sürecinin avantajı, Bitcoin kullanıcıları arasında bölünmeyi önlemek için tartışmayı kolaylaştıran ve güncellemeleri uzlaşmacı bir şekilde uygulamaya çalışan formalitesi ve merkezileştirilmesinde yatmaktadır. Sonuçta protokol içindeki güç dinamiklerini belirleyen ekonomik çoğunluk ilkesidir.


BIP'ler üç ana kategoride sınıflandırılmaktadır:


- **Standart İzleme BIP'leri**: İşlem ve blok doğrulama kuralları gibi Bitcoin uygulamalarını doğrudan etkileyen değişikliklerle ilgilidir;
- **Bilgilendirici BIP'ler**: Protokolde doğrudan değişiklik önermeden bilgi veya tavsiyeler sağlar;
- Süreç BIP'leri: Yönetişim süreçleri gibi Bitcoin'ü çevreleyen prosedürlerdeki değişiklikleri tanımlayın.


Standart İzleme ve Bilgilendirici BIP'ler de "Layer" ile sınıflandırılır:


- **Konsensüs Layer**: Bu Layer'daki BIP'ler, blok veya işlem doğrulama kurallarında yapılan değişiklikler gibi Bitcoin'nın mutabakat kuralları ile ilgilidir. Bu teklifler Soft çatalları (geriye dönük uyumlu değişiklikler) veya Hard çatalları (geriye dönük uyumlu olmayan değişiklikler) olabilir. Örneğin, SegWit ve Taproot için BIP'ler bu kategoriye aittir;
- **Eş Hizmetler**: Bu Layer, Bitcoin düğüm ağının çalışmasıyla, yani düğümlerin İnternet üzerinde birbirlerini nasıl buldukları ve iletişim kurdukları ile ilgilidir.
- **API/RPC**: Bu Layer'in BIP'leri, Bitcoin yazılımının düğümlerle etkileşime girmesini sağlayan Uygulama Programlama Arayüzleri (API) ve Uzaktan Prosedür Çağrıları (RPC) ile ilgilidir;
- **Uygulamalar Layer**: Bu Layer, Bitcoin üzerine inşa edilen uygulamalarla ilgilidir. Bu kategorideki BIP'ler genellikle Bitcoin Wallet standartları seviyesindeki değişikliklerle ilgilenir.


Bir BIP gönderme süreci, fikrin kavramsallaştırılması ve *Bitcoin-dev* posta listesinde tartışılmasıyla başlar. Fikir umut vericiyse, yazar belirli bir formatı izleyerek bir BIP taslağı hazırlar ve Core GitHub deposuna bir Çekme İsteği yoluyla gönderir. Editörler, tüm kriterleri karşıladığını doğrulamak için bu öneriyi inceler. BIP teknik olarak uygulanabilir, protokol için faydalı, gerekli formata uygun ve Bitcoin'nin felsefesine uygun olmalıdır. BIP bu koşulları karşılıyorsa, resmi olarak BIP'lerin GitHub deposuna entegre edilir. Daha sonra bir numara atanır. Bu numara genellikle editör, genellikle Luke Dashjr, tarafından belirlenir ve mantıksal olarak atanır: Benzer konuları ele alan BIP'ler genellikle ardışık numaralar alır.


BIP'ler daha sonra yaşam döngüleri boyunca farklı durumlardan geçerler. Mevcut durum her BIP'nin başlığında belirtilir:


- Taslak: Teklif halen taslak hazırlama ve tartışma aşamasındadır;
- Teklif edildi: BIP'nin tamamlandığı ve topluluk tarafından incelenmeye hazır olduğu düşünülmektedir;
- Ertelenmiş: BIP, şampiyon veya bir editör tarafından daha sonra görüşülmek üzere beklemeye alınır;
- Reddedildi: Bir BIP 3 yıl boyunca hiçbir faaliyet göstermemişse reddedilmiş olarak sınıflandırılır. Yazarı daha sonra devam ettirmeyi seçebilir, bu da taslak statüsüne dönmesini sağlar;
- Geri çekilmiştir: BIP, yazarı tarafından geri çekilmiştir;
- Sonuç: BIP kabul edilir ve Bitcoin'de yaygın olarak uygulanır;
- Aktif: Yalnızca süreç BIP'leri için bu statü belirli bir uzlaşmaya varıldığında atanır;
- Değiştirildi / Geçersiz: BIP artık uygulanabilir değildir veya onu gereksiz kılan daha yeni bir teklifle değiştirilmiştir.


![](../../dictionnaire/assets/25.webp)


> ► *BIP, "Bitcoin İyileştirme Önerisi "nin kısaltmasıdır. Fransızca'da "Proposition d'amélioration de Bitcoin" olarak tercüme edilebilir. Bununla birlikte, çoğu Fransızca metin "BIP" kısaltmasını bazen dişil, bazen eril olmak üzere doğrudan ortak bir isim olarak kullanır.*