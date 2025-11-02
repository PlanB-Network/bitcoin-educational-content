---
name: BTCPAY SERVER - Ô
description: Cài đặt và sử dụng BTCPAY SERVER trên Umbrel để chấp nhận Bitcoin và Lightning
---

![cover](assets/cover.webp)



Trong hệ sinh thái Bitcoin, việc chấp nhận thanh toán là một thách thức lớn đối với cả người bán và doanh nghiệp. Các giải pháp truyền thống, dù là ngân hàng (thẻ tín dụng, Stripe, PayPal) hay thậm chí là Bitcoin (BitPay, Coinbase Commerce), đều áp đặt các bên trung gian thu phí đáng kể, thu thập dữ liệu kinh doanh nhạy cảm của bạn và có thể kiểm duyệt hoặc kiểm duyệt giao dịch của bạn theo ý muốn. Sự phụ thuộc này đi ngược lại các nguyên tắc cơ bản của Bitcoin về phi tập trung, bảo mật và chủ quyền tài chính.



BTCPAY SERVER đang nổi lên như một giải pháp mã nguồn mở cho vấn đề này. Bộ xử lý thanh toán tự lưu trữ này biến nút Bitcoin của bạn thành một cơ sở hạ tầng chuyên nghiệp, không qua trung gian, không phí xử lý bổ sung và không ảnh hưởng đến quyền riêng tư. Được phát triển bởi cộng đồng đóng góp toàn cầu từ năm 2017, BTCPAY SERVER cho phép bạn nhận thanh toán Bitcoin và Lightning trực tiếp vào ví của mình, đồng thời vẫn giữ toàn quyền kiểm soát tiền của bạn mọi lúc.



Theo truyền thống, việc cài đặt BTCPAY SERVER đòi hỏi các kỹ năng kỹ thuật nâng cao: cấu hình máy chủ Linux, thành thạo Docker, quản lý chứng chỉ SSL và bảo mật mạng. Umbrel cách mạng hóa phương pháp này với tính năng cài đặt chỉ bằng một cú nhấp chuột, được tích hợp trực tiếp với Bitcoin và LIGHTNING NODE của bạn. Sự đơn giản hóa này giúp mọi người đều có thể sử dụng những gì trước đây chỉ dành cho các kỹ thuật viên giàu kinh nghiệm.



**Quan trọng cần hiểu**: BTCPAY SERVER trên Umbrel mặc định chỉ hoạt động trên mạng cục bộ của bạn. Bạn có thể tạo hóa đơn, chấp nhận thanh toán Lightning và Bitcoin, và quản lý kế toán từ bất kỳ thiết bị nào được kết nối với mạng gia đình (máy tính, điện thoại thông minh, máy tính bảng). Cấu hình này lý tưởng để thanh toán cho các dịch vụ trực tiếp, quản lý thanh toán trực tiếp hoặc sử dụng BTCPAY SERVER từ mạng cục bộ của bạn. Mặt khác, để tích hợp BTCPAY SERVER vào một cửa hàng trực tuyến có thể truy cập công khai trên Internet, cần có một cấu hình bổ sung với chế độ công khai (chúng tôi sẽ đề cập đến vấn đề này ở cuối hướng dẫn).



Hướng dẫn này sẽ hướng dẫn bạn cài đặt hoàn chỉnh BTCPAY SERVER trên Umbrel, cấu hình Bitcoin, Wallet và LIGHTNING NODE, tạo và thanh toán hóa đơn, cũng như quản lý báo cáo kế toán. Bạn sẽ tìm hiểu cách sử dụng BTCPAY SERVER hiệu quả trên mạng cục bộ, và sau đó chúng ta sẽ thảo luận về các giải pháp hiển thị công khai nếu bạn muốn tích hợp nó với một trang web thương mại điện tử.



## Điều kiện tiên quyết



Để làm theo hướng dẫn này, bạn cần cài đặt và cấu hình Umbrel đúng cách. Nếu bạn chưa cài đặt, vui lòng xem hướng dẫn cài đặt Umbrel của chúng tôi.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Nút Bitcoin core của bạn phải được đồng bộ hóa hoàn toàn với Blockchain (100% trong ứng dụng Bitcoin của Umbrel). Quá trình đồng bộ hóa ban đầu này thường mất từ 3 ngày đến 2 tuần, tùy thuộc vào phần cứng và kết nối Internet của bạn.



Để chấp nhận thanh toán Lightning tức thì, bạn cũng cần cài đặt LND (Lightning Network Daemon) trên Umbrel. Xem hướng dẫn của chúng tôi về cách cài đặt và cấu hình LND trên Umbrel nếu bạn muốn bật tính năng này.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Dành ít nhất 50 GB dung lượng đĩa trống cho BTCPAY SERVER, cơ sở dữ liệu và dữ liệu Lightning. Khuyến nghị kết nối Internet ổn định qua cáp Ethernet để tránh mất kết nối.



## Cài đặt BTCPAY SERVER trên Umbrel



Từ Umbrel Interface (`umbrel.local`), hãy vào App Store và tìm kiếm "BTCPAY SERVER" trong danh mục Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Nhấp vào Cài đặt. Umbrel sẽ tự động kiểm tra xem Bitcoin core và LND đã được cài đặt chưa, sau đó bắt đầu triển khai (2-5 phút).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Sau khi cài đặt, hãy mở ứng dụng. Bạn cần tạo một tài khoản quản trị viên có thông tin xác thực mạnh.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Sau khi tài khoản của bạn được tạo, BTCPAY SERVER sẽ ngay lập tức nhắc bạn thiết lập cửa hàng đầu tiên. Chọn tên chuyên nghiệp và chọn loại tiền tệ tham chiếu (EUR, USD hoặc BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Truy cập BTCPAY SERVER trên mạng cục bộ của bạn



BTCPAY SERVER có thể truy cập từ bất kỳ thiết bị nào trong mạng cục bộ của bạn (WiFi hoặc Ethernet). Truy cập từ trình duyệt của bạn để:



```url
http://umbrel.local
```



Hoặc trực tiếp đến:



```url
http://umbrel.local:3003
```



**Truy cập từ xa với Tailscale**: Để truy cập BTCPAY SERVER từ bất kỳ đâu trên thế giới, hãy sử dụng Tailscale. VPN an toàn này cho phép bạn kết nối với Umbrel như thể bạn đang ở trên mạng cục bộ. Xem hướng dẫn của chúng tôi dành riêng cho Tailscale trên Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Cấu hình danh mục đầu tư Bitcoin của bạn



Để chấp nhận thanh toán, bạn cần cấu hình Bitcoin Wallet. BTCPAY SERVER hiển thị các tùy chọn cấu hình trong bảng điều khiển.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Để cấu hình Wallet Bitcoin, hãy vào "Ví" > "Bitcoin".



Bạn có hai lựa chọn: tạo danh mục đầu tư mới trực tiếp trong BTCPay hoặc nhập danh mục đầu tư hiện có. Có một số phương pháp để nhập danh mục đầu tư:




- Kết nối Hardware Wallet** (khuyến nghị): Nhập khóa công khai của bạn thông qua ứng dụng Vault
- Nhập tệp Wallet** (khuyến nghị): Tải lên tệp đã xuất từ danh mục đầu tư của bạn
- Nhập khóa công khai mở rộng**: Nhập XPub/YPub/ZPub của bạn theo cách thủ công
- Quét mã QR Wallet**: Quét mã QR từ BlueWallet, Cobo Vault, Passport hoặc Spectre DIY
- Nhập Wallet seed** (không khuyến nghị): Nhập cụm từ khôi phục gồm 12 hoặc 24 từ của bạn



![Options de création de portefeuille](assets/fr/06.webp)



Trong hướng dẫn này, chúng ta sẽ tạo một ví Hot Wallet mới: do đó, khóa riêng tư sẽ được lưu trữ trên máy chủ Umbrel của chúng ta. Trong trường hợp này, chúng tôi đặc biệt khuyên bạn nên chuyển tiền thường xuyên sang ví Cold Wallet để tránh lưu trữ số tiền lớn trên máy chủ.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Sau khi cấu hình, BTCPAY SERVER sẽ xác nhận rằng Wallet của bạn đã sẵn sàng chấp nhận thanh toán On-Chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Kích hoạt Lightning Network



Để chấp nhận thanh toán Lightning tức thì, hãy vào Ví > Lightning. Sau đó, vì nút LND của bạn đã được cài đặt trên Umbrel, chỉ cần nhấp vào nút "Lưu" để xác thực kết nối giữa BTCPAY SERVER và LIGHTNING NODE.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Tạo và thanh toán hóa đơn



Trong Interface BTCPAY SERVER, hãy điều hướng đến Hóa đơn > Tạo Invoice. Nhập số tiền, thêm mô tả tùy chọn và nhấp vào Tạo.



![Création d'une nouvelle facture](assets/fr/10.webp)



Sau đó, bạn có thể nhấp vào nút "Thanh toán" để hiển thị Invoice. BTCPay sau đó sẽ tạo một Invoice với mã QR thống nhất (BIP21) chứa Bitcoin, Address và Lightning Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Khách hàng của bạn có thể quét mã QR bằng bất kỳ thiết bị Wallet tương thích nào.



![Page de paiement avec QR code](assets/fr/12.webp)



Sau khi thanh toán, Invoice sẽ được "Thanh toán" chỉ trong vài giây đối với Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Quản lý và theo dõi thanh toán



Trong mục "Báo cáo", tab "Hóa đơn", bạn sẽ tìm thấy lịch sử đầy đủ các hóa đơn của mình, bao gồm ngày, số tiền, trạng thái và phương thức thanh toán. Bạn có thể xuất dữ liệu này nếu cần.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Cấu hình cửa hàng



BTCPAY SERVER cho phép bạn quản lý nhiều cửa hàng với các thông số riêng biệt. Mỗi cửa hàng đại diện cho một thực thể kinh doanh riêng biệt: cửa hàng thương mại điện tử, điểm bán hàng thực tế hoặc thanh toán dịch vụ.



Trong phần cài đặt cửa hàng, bạn sẽ tìm thấy một số phần quan trọng:



![Paramètres du magasin](assets/fr/15.webp)





- Cài đặt chung**: Tên cửa hàng, loại tiền tham chiếu (BTC, EUR, USD), thời gian hết hạn Invoice (mặc định là 15 phút), số lượng xác nhận Blockchain cần thiết
- Tỷ giá**: Cấu hình nguồn tỷ giá Exchange và chuyển đổi fiat/Bitcoin
- Giao diện thanh toán**: Tùy chỉnh giao diện trang thanh toán của bạn (logo, màu sắc, thông điệp được cá nhân hóa)
- Cài đặt Email**: Cấu hình thông báo qua email về các khoản thanh toán đã nhận
- Mã thông báo truy cập**: Quản lý API token cho tích hợp thương mại điện tử (WooCommerce, Shopify, v.v.)
- Người dùng**: Quản lý quyền truy cập của người dùng vào cửa hàng với các cấp độ quyền khác nhau (Chủ sở hữu, Khách)
- Webhooks**: Cấu hình Webhook để đồng bộ hóa thời gian thực với hệ thống kế toán hoặc ERP của bạn



BTCPAY SERVER cũng cung cấp phần Plugin để mở rộng chức năng với tích hợp thương mại điện tử, hệ thống điểm bán hàng và các công cụ bổ sung.



![Gestion des plugins](assets/fr/16.webp)



## Ưu điểm và hạn chế của việc sử dụng tại địa phương



**Lợi ích của BTCPAY SERVER trên Umbrel**:




- Chủ quyền hoàn toàn: kiểm soát độc quyền các khóa riêng tư và tiền, không bên thứ ba nào có thể đóng băng hoặc kiểm duyệt các khoản thanh toán của bạn
- Tiết kiệm đáng kể: chỉ tốn chi phí mạng Bitcoin (vài xu cho Lightning) so với 2-3% cho bộ xử lý truyền thống
- Bảo mật tối đa: không cần đăng ký, xác minh danh tính hoặc chia sẻ dữ liệu với các công ty bên thứ ba
- Kiến trúc nguồn mở đảm bảo tính minh bạch, khả năng kiểm toán và tính bền vững thông qua một cộng đồng lớn các nhà phát triển
- Cài đặt dễ dàng thông qua Umbrel, không cần kỹ năng kỹ thuật nâng cao



**Hạn chế quan trọng**:




- Chỉ dành cho mạng cục bộ**: BTCPAY SERVER trên Umbrel chỉ có thể truy cập từ mạng gia đình của bạn. Hoàn hảo cho việc thanh toán trực tiếp, dịch vụ tự do hoặc doanh nghiệp nhỏ, nhưng không phù hợp với các cửa hàng trực tuyến có thể truy cập công khai trên Internet.
- Chịu trách nhiệm kỹ thuật toàn diện: bảo trì nút, sao lưu thường xuyên, giám sát kết nối
- Quản lý thanh khoản Lightning: mở và quản lý các kênh có đủ khả năng tiếp nhận
- Hỗ trợ giới hạn ở tài liệu cộng đồng và diễn đàn, đòi hỏi nhiều quyền tự chủ hơn so với bộ phận dịch vụ khách hàng thương mại



Hạn chế về mạng LAN này là trở ngại chính khi tích hợp BTCPAY SERVER vào cửa hàng thương mại điện tử, nơi khách hàng cần có khả năng truy cập vào các trang thanh toán từ bất kỳ đâu trên Internet.



## Thực hành tốt nhất và an toàn



Kích hoạt tính năng sao lưu Umbrel tự động và lưu trữ một bản sao trên thiết bị lưu trữ ngoài (USB, ổ đĩa Hard, đám mây được mã hóa). Lưu trữ các cụm từ khôi phục (seed) Bitcoin (cụm từ khôi phục) ở một nơi an toàn, tách biệt về mặt vật lý. Lưu tệp LND channel.backup để khôi phục Lightning.



Thường xuyên theo dõi đồng bộ hóa Bitcoin core, kênh Lightning và phản hồi BTCPAY SERVER. Một bài kiểm tra đơn giản hàng tuần: generate và thanh toán hóa đơn với vài satoshi. Hãy cập nhật Umbrel (bản vá bảo mật, cải tiến). Sao lưu trước khi cập nhật lớn. Đối với mục đích sử dụng chuyên nghiệp, hãy cân nhắc sử dụng dịch vụ giám sát bên ngoài (UptimeRobot) với cảnh báo qua email/SMS.



## Hiển thị BTCPAY SERVER công khai cho một cửa hàng trực tuyến



Để tích hợp BTCPAY SERVER vào cửa hàng thương mại điện tử trên nền tảng web (WooCommerce, Shopify, v.v.), khách hàng của bạn cần có thể truy cập vào các trang thanh toán từ mọi nơi, không chỉ từ mạng cục bộ của bạn.



**Giải pháp: Trình quản lý Proxy Nginx**



Bạn có thể công khai BTCPAY SERVER bằng Nginx Proxy Manager (có sẵn trên Umbrel App Store). Giải pháp này yêu cầu:




- Tên miền (cổ điển hoặc miễn phí qua DuckDNS, No-IP, Afraid.org)
- Cấu hình chuyển tiếp cổng (cổng 80 và 443) trên bộ định tuyến của bạn
- Cài đặt Nginx Proxy Manager, tự động quản lý chứng chỉ SSL



Cấu hình này sẽ khiến máy chủ của bạn bị lộ ra ngoài Internet và đòi hỏi sự cảnh giác cao độ (mật khẩu mạnh, xác thực hai yếu tố (2FA), cập nhật thường xuyên). Chúng tôi sẽ chuẩn bị một hướng dẫn chi tiết về quy trình này.



## Phần kết luận



BTCPAY SERVER trên Umbrel kết hợp sức mạnh của nút Bitcoin với sự đơn giản của Umbrel để tạo ra một cơ sở hạ tầng thanh toán chuyên nghiệp tự lưu trữ, dễ dàng tiếp cận với tất cả mọi người. Quyền tự chủ tài chính này đi kèm với trách nhiệm bảo trì, nhưng Umbrel đơn giản hóa đáng kể gánh nặng vận hành so với những lợi ích: loại bỏ phí xử lý, bảo vệ quyền riêng tư, chống kiểm duyệt và kiểm soát hoàn toàn tiền của bạn.



Việc sử dụng mạng cục bộ đã bao phủ một loạt các ứng dụng: thanh toán cho các dịch vụ tự do, thanh toán trực tiếp, cửa hàng vật lý nhỏ, hoặc đơn giản là tìm hiểu và thử nghiệm Bitcoin và Lightning trong môi trường được kiểm soát. Đối với các nhu cầu thương mại điện tử đòi hỏi sự công khai, giải pháp Nginx Proxy Manager đã có sẵn, nhưng yêu cầu cấu hình kỹ thuật bổ sung, chúng tôi sẽ trình bày chi tiết trong một hướng dẫn chuyên sâu.



Dù bạn đang điều hành một doanh nghiệp, một dự án mới hay chỉ đơn giản là đang thử nghiệm, BTCPAY SERVER trên Umbrel đều mang đến sự tự chủ tài chính hoàn toàn. Hành trình bắt đầu với một cửa hàng đầu tiên, một Invoice đầu tiên, khoản thanh toán đầu tiên được nhận trực tiếp vào cơ sở hạ tầng có chủ quyền của bạn.



## Tài nguyên



### Tài liệu chính thức




- [Trang web chính thức của BTCPAY SERVER](https://btcpayserver.org)
- [Tài liệu đầy đủ về BTCPAY SERVER](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Tài liệu Tailscale](https://tailscale.com/kb)


### Cộng đồng và hỗ trợ




- [Diễn đàn BTCPAY SERVER](https://chat.btcpayserver.org)
- [Diễn đàn ô](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)