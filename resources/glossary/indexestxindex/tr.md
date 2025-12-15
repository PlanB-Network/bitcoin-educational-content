---
term: INDEXES/TXINDEX/
---

Bitcoin core'daki dosyalar Blockchain'de bulunan tüm işlemlerin indekslenmesine ayrılmıştır. Bu indeksleme, Blockchain'in tamamını gözden geçirmek zorunda kalmadan, tanımlayıcısını (txid) kullanarak bir işlem hakkında ayrıntılı bilgilerin hızlı bir şekilde aranmasını sağlar. Bu indeksleme dosyalarının oluşturulması Bitcoin core'da varsayılan olarak etkinleştirilmemiş bir seçenektir. Bu özellik etkinleştirilmezse, node'unuz yalnızca node'unuza bağlı cüzdanlarla ilişkili işlemleri indeksleyecektir. Tüm işlemlerin indekslenmesini etkinleştirmek için `Bitcoin.conf` dosyasında `-txindex=1` parametresini ayarlamanız gerekir. Bu seçenek özellikle Bitcoin'nin işlem geçmişinde sık sık arama yapan uygulamalar ve hizmetler için kullanışlıdır.