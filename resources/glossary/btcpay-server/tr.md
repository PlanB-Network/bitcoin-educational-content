---
term: BTCPay Server
definition: Aracı olmadan bitcoin ödemelerini kabul etmeyi sağlayan açık kaynaklı ödeme işlemcisi.
---

⚠️ **Kritik güvenlik uyarısı (7 Ağustos 2026):** BTCPay Server'ı etkileyen kritik bir güvenlik açığı aktif olarak istismar ediliyor ve fon kaybına yol açabilir. Sisteminizi `Admin Dashboard > Server > Maintenance > Update` yolundan derhal **version 2.4.2** sürümüne güncelleyin, ardından alt bilgide `2.4.2` yazdığını doğrulayın. Hemen güncelleyemiyorsanız BTCPay Server örneğinizi kapatın. Güncelleme sonrasında ayrıca macaroons dosyalarınızı ve `macaroons.db` veritabanınızı tamamen yenilemeniz, kullandığınız diğer tüm Lightning arka uçlarının kimlik doğrulama dizelerini baştan oluşturmanız ve BTCPay Server içinde sıcak bir on-chain cüzdan oluşturduysanız bu fonları taşıyıp cüzdanı yeniden oluşturmanız gerekir. Entegrasyon geliştiricileri ayrıca NBXplorer'ı version 2.6.10 sürümüne güncellemelidir. Kaynak: [BTCPay Server 2.4.2 sürüm notları](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b

BTCPay Server, tüccarların ve kullanıcıların işlem işleme için üçüncü bir tarafa güvenmeden Bitcoin ödemelerini kabul etmelerini sağlayan açık kaynaklı bir ödeme işlemcisidir. 2017 yılında piyasaya sürülen BTCPay Server, donanım cüzdanları, faturalandırma ve muhasebe araçlarının yanı sıra Lightning Network ile uyumluluk desteği gibi gelişmiş özelliklerle e-ticaret siteleri için bir Bitcoin ödeme entegrasyon çözümü sunmaktadır. Bu çözümün geliştirilmesi, Nicolas Dorier tarafından, kendisine göre kullanıcılarını yanlışlıkla "gerçek" Bitcoin olarak kabul ettiği SegWit2x'in benimsenmesine iterek yanıltan Bitpay'in eylemlerine yanıt olarak başlatıldı. Bu muhalefet, Nicolas Dorier'in Ağustos 2017'de attığı ve artık meşhur olan bir tweet'te özetlenmişti:


> "_Bu yalan, sana olan güvenim kırıldı, seni kullanılmaz hale getireceğim_".

