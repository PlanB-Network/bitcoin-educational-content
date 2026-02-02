---
term: Statik adres
definition: Silent Payments için adres yeniden kullanımı veya görünür on-chain bağlantı olmadan ödeme alınmasını sağlayan benzersiz tanımlayıcı.
---

Sessiz Ödemeler bağlamında, Address yeniden kullanılmadan, etkileşim olmadan ve çeşitli ödemeler ile statik Address arasında görünür bir On-Chain bağlantısı olmadan ödemelerin alınmasına olanak tanıyan benzersiz bir tanımlayıcı anlamına gelir. Bu teknik, her işlem için yeni, kullanılmayan alıcı adresleri KİS-2 ihtiyacını ortadan kaldırır, böylece alıcının ödeyene yeni bir KİS-3 sağlaması gereken KİS-4'teki olağan etkileşimlerden kaçınır. Bu, BIP47 bağlamında yeniden kullanılabilir ödeme koduna bir şekilde eşdeğerdir.


Bu Address iki açık anahtardan oluşur: tarama için $B_{\text{scan}}$ ve harcama için $B_{\text{spend}}$, statik Address $B = B_{\text{scan}} oluşturmak üzere birleştirilir \text{ ‖ } B_{\text{spend}}$. Alıcı bu Address'yı yayınlayarak göndericilerin alıcıyla başka bir etkileşime girmeden benzersiz ödeme adresleri türetmesine olanak tanır. Birden fazla farklı ödeme kaynağını yönetmek için $B_{\text{spend}}$'e bir etiket eklenebilir, böylece $B_1$, $B_2$ vb. gibi birkaç etiketli statik adres oluşturulabilir. Bu, tek bir temel Address kullanırken ödemelerin ayrılmasını sağlar ve böylece Blockchain taraması için iş yükünü azaltır. Bununla birlikte, $B_{\text{scan}}$'ın ortak kullanımı nedeniyle bir tüzel kişinin tüm statik adresleri kolayca ilişkilendirilebilir.