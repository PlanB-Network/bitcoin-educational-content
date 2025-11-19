---
term: ERLAY
---

Bitcoin düğümleri arasında onaylanmamış işlemlerin aktarılmasının verimliliğini artırmak için önerilen ağ protokolü.


Şu anda, her işlem, her düğümün farkında olduğu işlemi tüm eşlerine yayınladığı bir sistem aracılığıyla yayılmaktadır. Sorun, bunun çok fazla fazlalığa ve yinelemeler için bant genişliği kullanımına yol açmasıdır. Alıcı bu işlemleri zaten bildiğinden ve her düğümün her işlem hakkında yalnızca bir kez bilgi sahibi olması gerektiğinden, birçok işlem yayını gereksizdir. Erlay, bir düğümün farkında olduğu işlemleri doğrudan gönderdiği eş sayısını varsayılan olarak 8 ile sınırlamayı ve ardından eksik işlemleri daha verimli bir şekilde paylaşmak için minisketch kütüphanesine dayalı bir uzlaştırma süreci kullanmayı önermektedir.


Erlay bant genişliği tüketimini yaklaşık %40 oranında azaltarak Full node'in sınırlı internet bağlantısı olan kullanıcılar için daha erişilebilir olmasını sağlayacak ve böylece ağın daha iyi merkezsizleştirilmesini teşvik edecektir. Bu protokol ayrıca bağlantı sayısı arttıkça bant genişliği tüketimini neredeyse sabit tutacaktır. Bu da düğüm operatörlerinin eşlerinden çok sayıda bağlantı kabul etmelerinin çok daha kolay olacağı anlamına gelmektedir ki bu da ister kasıtlı ister kazara olsun bölünme riskini azaltarak Bitcoin ağının güvenliğini artıracaktır. Buna ek olarak Erlay, bir işlemin kaynak düğümünü belirlemeyi daha zor hale getirecek ve böylece Tor altında çalışmayan düğümlerin kullanıcıları için gizliliği artıracaktır.


Erlay, BIP330'da önerilmiştir.