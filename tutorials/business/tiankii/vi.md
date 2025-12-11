---
name: Thiankii
description: Bộ công cụ Lightning dành cho nhà bán lẻ và người tiêu dùng
---

![cover](assets/cover.webp)



Trong hệ sinh thái Bitcoin, việc chấp nhận thanh toán theo thời gian thực vẫn là một thách thức lớn đối với doanh nghiệp và cá nhân. Các giải pháp truyền thống thường đòi hỏi kiến thức kỹ thuật chuyên sâu, cơ sở hạ tầng phức tạp để duy trì, hoặc yêu cầu tiền phải được nắm giữ bởi các bên trung gian. Tình trạng này đang cản trở việc áp dụng rộng rãi Bitcoin như một loại tiền tệ hàng ngày, bất chấp những hứa hẹn về những tiến bộ công nghệ của Lightning Network.



Tiankii, một công ty Salvador ra đời năm 2021, giải quyết vấn đề này bằng cách cung cấp cơ sở hạ tầng Bitcoin dạng mô-đun dễ tiếp cận. Thay vì áp đặt một hệ sinh thái khép kín, Tiankii cung cấp một bộ công cụ kết nối cho phép bất kỳ ai cũng có thể tích hợp Bitcoin Lightning vào doanh nghiệp của mình mà không ảnh hưởng đến quyền kiểm soát nguồn vốn.



## Tiankii là gì?



### Nguồn gốc và triết lý



Tiankii - một thuật ngữ tiếng Nahuatl có nghĩa là "chợ trời dành cho tất cả mọi người" - là công ty khởi nghiệp đầu tiên tại El Salvador sử dụng 100% Bitcoin. Được thành lập bởi Darvin Otero sau khi Bitcoin được chính thức công nhận là tiền tệ hợp pháp của quốc gia, công ty đặt mục tiêu chuyển đổi Bitcoin từ một kho lưu trữ giá trị thành một loại tiền tệ có thể giao dịch cho các giao dịch hàng ngày. Không giống như các nền tảng lưu ký, Tiankii áp dụng phương pháp phi lưu ký, trong đó người dùng vẫn giữ quyền kiểm soát tiền của mình, với cơ sở hạ tầng chỉ đóng vai trò trung gian kỹ thuật.



### Kiến trúc kỹ thuật



Tiankii được định vị là nhà cung cấp cơ sở hạ tầng Bitcoin-as-a-Service dựa trên Lightning Network. Công nghệ lớp thứ hai này cho phép giao dịch gần như tức thời với chi phí không đáng kể, giúp việc thanh toán nhỏ và mua sắm hàng ngày trở nên khả thi.



Kiến trúc dựa trên ba trụ cột:



**Ưu tiên Lightning**: Ưu tiên mạng Lightning một cách có hệ thống vì tốc độ và chi phí thấp hơn, đồng thời vẫn duy trì hỗ trợ giao dịch on-chain cho số lượng lớn.



**Tiêu chuẩn mở**: Sử dụng LNURL để tự động hóa các yêu cầu thanh toán, Lightning Address để đọc ID email và Bolt Card để thanh toán NFC có thể tương tác.



**Tính mô-đun không phụ thuộc vào wallet**: Khả năng kết nối các danh mục đầu tư Lightning khác nhau (LNbits, Blink, BlueWallet) hoặc nút của riêng bạn, mang lại sự linh hoạt tối đa tùy thuộc vào mức độ chuyên môn và quyền tự chủ cần thiết.



## Công cụ hệ sinh thái Tiankii



### Bitcoin POS - Máy thanh toán tại cửa hàng



Ứng dụng biến điện thoại thông minh hoặc máy tính bảng thành thiết bị đầu cuối Lightning. Người bán hàng nhập số tiền bằng tiền tệ địa phương, và ứng dụng sẽ tạo mã QR Lightning hoặc chấp nhận Thẻ Bolt. Giao dịch được ghi có ngay lập tức mà không mất phí hoa hồng, với tính năng chuyển đổi tự động sang hơn 150 loại tiền tệ, quản lý tiền boa và lịch sử bán hàng.



### Merchant Dashboard - Quản lý bán hàng thống nhất



Interface được thiết kế tập trung trên nền tảng web để kết nối với wallet Lightning, theo dõi giao dịch theo thời gian thực, xuất hóa đơn và báo cáo kế toán generate. Nền tảng này tổng hợp tất cả các kênh: thanh toán tại cửa hàng (POS), bán hàng trực tuyến (plugin thương mại điện tử) hoặc tích hợp API. Các khoản thanh toán sẽ được tập trung tại wallet đã chọn.



### Thẻ không tiếp xúc Bitcoin (Thẻ Bolt)



Thẻ NFC Bolt là bước đột phá lớn của Tiankii trong việc phổ cập hóa Bitcoin đến với công chúng. Hoạt động như một thẻ ngân hàng không tiếp xúc, thẻ này cho phép bạn thanh toán các giao dịch mua hàng bằng Bitcoin Lightning chỉ bằng cách chạm vào thiết bị đầu cuối tương thích.



Không giống như các giải pháp lưu ký truyền thống, thẻ này tuân thủ một tiêu chuẩn mở đảm bảo khả năng tương tác. Người dùng có thể liên kết thẻ với wallet của mình thông qua ứng dụng IBI, do đó vẫn giữ được khóa riêng tư và toàn quyền kiểm soát các khoản tiền liên quan. Việc thanh toán chỉ mất một giây, không cần phải lấy điện thoại thông minh ra hoặc kết nối internet đang hoạt động tại thời điểm thanh toán.



Giải pháp này đặc biệt phù hợp với những người không quen sử dụng điện thoại thông minh, cung cấp cổng thông tin dễ tiếp cận đến nền kinh tế Bitcoin.



### Ứng dụng IBI - Interface cá nhân Bitcoin



Ứng dụng IBI (Bitcoin Interface Cá nhân) được thiết kế dành cho những cá nhân muốn sử dụng Bitcoin Lightning hàng ngày. Ưu điểm chính của ứng dụng nằm ở việc tạo ra Address Lightning được cá nhân hóa, một mã định danh thanh toán có thể đọc được dưới dạng email (ví dụ: alice@ibi.me).



Mã định danh này đơn giản hóa đáng kể việc nhận thanh toán: không cần phải tạo hóa đơn mới cho mỗi giao dịch, người gửi chỉ cần nhập địa chỉ Lightning. Giao diện này cũng cho phép bạn quản lý Thẻ Bolt của mình (kích hoạt, hủy kích hoạt, giới hạn chi tiêu), kết nối nhiều ví Lightning khác nhau và thực hiện thanh toán bằng cách quét mã QR.



### Plugin thương mại điện tử



Tích hợp sẵn sàng sử dụng cho WooCommerce, Shopify và Cloudbeds. Cài đặt trong vài phút để thêm Bitcoin Lightning vào thanh toán. Ưu điểm: không hoa hồng (so với thẻ tín dụng 2-3%), thanh toán tức thì, truy cập toàn cầu, loại bỏ hoàn tiền. Thanh toán được gửi trực tiếp đến wallet được kết nối của người bán.



### Bitcoin API và các công cụ dành cho nhà phát triển



Tiankii SDK cho phép tích hợp Bitcoin Lightning vào các ứng dụng hiện có mà không cần duy trì node riêng. API xử lý việc tạo hóa đơn, xác minh thanh toán và gửi thư hàng loạt thông qua cơ sở hạ tầng mạnh mẽ được lưu trữ trên Google Cloud. Command Center hoàn thiện dịch vụ cho các tổ chức với Address Lightning trên các tên miền tùy chỉnh, thanh toán hàng loạt và quản lý tập trung các thiết bị đầu cuối và thẻ NFC.



## Cài đặt và các bước đầu tiên



### Điều kiện tiên quyết cần thiết



Sử dụng Tiankii không yêu cầu bất kỳ điều kiện kỹ thuật phức tạp nào. Ứng dụng hoạt động thông qua trình duyệt web trên điện thoại thông minh, máy tính bảng hoặc máy tính. Không cần cài đặt ứng dụng gốc: tất cả những gì bạn cần là kết nối Internet và trình duyệt mới nhất để truy cập IBI hoặc Merchant Dashboard.



**Dành cho người dùng cá nhân (Ứng dụng IBI)**: Không yêu cầu cài đặt wallet Lightning trước. Khi bạn tạo tài khoản, Tiankii sẽ tự động cấu hình Address Lightning đang hoạt động thông qua [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html], một triển khai không nút sử dụng mạng Liquid ở chế độ nền. Bạn có thể nhận và gửi thanh toán ngay lập tức mà không cần bất kỳ cấu hình kỹ thuật nào. Giải pháp này đơn giản hóa đáng kể việc truy cập cho người mới bắt đầu, đồng thời vẫn đảm bảo tính tự quản.



**Dành cho người bán (Bảng điều khiển Người bán)**: Việc kết nối thiết bị wallet Lightning hiện có là bắt buộc để sử dụng thiết bị đầu cuối POS và nhận thanh toán. Tiankii hỗ trợ nhiều giải pháp: ví di động (Blink, Strike), giải pháp tự lưu trữ (LNbits, LND/CLN node) hoặc ví web (Alby). Hướng dẫn kết nối chi tiết có sẵn trong phần Tài nguyên của hướng dẫn này.



### Dành cho khách hàng cá nhân: Ứng dụng IBI



**Tạo tài khoản



Truy cập accounts.ibi.me để tạo tài khoản. Trên trang này, bạn có thể chọn giữa hai loại tài khoản: "Sử dụng Cá nhân" cho mục đích cá nhân hoặc "Sử dụng Doanh nghiệp" cho mục đích thương mại. Chọn "Sử dụng Cá nhân" để truy cập các công cụ nhận và gửi thanh toán trong Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



Sau khi chọn "Sử dụng Cá nhân", bạn sẽ được tự động chuyển hướng đến go.ibi.me để hoàn tất đăng ký. Bạn có thể thực hiện việc này qua email, số điện thoại hoặc sử dụng tài khoản Google, Microsoft hoặc Twitter của mình. Sau khi tạo, bạn có thể truy cập ngay vào giao diện IBI của mình với Lightning Address đã sẵn sàng hoạt động.



![Création du compte](assets/fr/02.webp)



**Interface chính**



Giao diện IBI hiển thị số dư của bạn bằng satoshi và tiền tệ địa phương (USD). Ba nút cho phép bạn tương tác: "Nhận" để nhận thanh toán, "Quét" để quét mã QR và "Gửi" để gửi satoshi.



![Interface IBI](assets/fr/03.webp)



**Nhận thanh toán**



Để nhận satoshi, hãy nhấn "Nhận". Ứng dụng sẽ tự động tạo mã QR và hiển thị ví Address Lightning (định dạng nom@ibi.me) được cá nhân hóa của bạn. Chia sẻ địa chỉ này hoặc mã QR với người gửi: tiền sẽ ngay lập tức được chuyển vào tài khoản IBI của bạn.



![Réception avec Lightning Address](assets/fr/04.webp)



Sau khi số dư đã được ghi có, bạn có thể sử dụng số satoshi này để thanh toán.



**Gửi thanh toán**



Để gửi satoshi, hãy nhấn "Gửi". Bạn có thể quét mã QR Lightning hoặc nhập trực tiếp địa chỉ đích Lightning Address.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Nhập số tiền mong muốn bằng satoshi, kiểm tra số tiền tương đương bằng tiền tệ địa phương, sau đó xác nhận thanh toán.



![Confirmation du montant](assets/fr/07.webp)



Thông báo thành công xác nhận việc giao hàng kèm theo thông tin chi tiết: số tiền đã gửi, phí giao dịch và người nhận.



![Paiement réussi](assets/fr/08.webp)



**Quản lý tài khoản



Trong Cài đặt, bạn có thể quản lý thẻ NFC Bitcoin (thẻ Bolt). Giao diện cho phép bạn kích hoạt, hủy kích hoạt hoặc đặt giới hạn chi tiêu cho thẻ của mình.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Dành cho người bán: Bảng điều khiển người bán và POS



**Tạo tài khoản doanh nghiệp



Truy cập accounts.ibi.me để tạo tài khoản. Chọn "Sử dụng cho Doanh nghiệp" để truy cập các công cụ dành cho người bán. Loại tài khoản này cho phép truy cập vào Bảng điều khiển dành cho Người bán và thiết bị đầu cuối tại điểm bán hàng.



Sau khi chọn "Sử dụng cho Doanh nghiệp", bạn sẽ tự động được chuyển hướng đến Bảng điều khiển của Nhà cung cấp (pay.tiankii.com). Thao tác này sẽ đưa bạn đến giao diện quản lý doanh nghiệp với các công cụ theo dõi doanh thu, giao dịch và thanh toán. Để bắt đầu chấp nhận thanh toán, trước tiên bạn phải kết nối wallet Lightning bằng cách nhấp vào liên kết ở đầu trang (xem mũi tên trên hình ảnh).



![Dashboard marchand](assets/fr/11.webp)



Kết nối **wallet Lightning**



Bước quan trọng để kích hoạt điểm bán hàng của bạn: kết nối wallet Lightning để nhận thanh toán. Giao diện cung cấp một số tùy chọn kết nối. Xin lưu ý rằng một số tùy chọn (Bitcoin Onchain và Lightning Network) vẫn đang được phát triển và hiển thị màu xám trên giao diện.



![Options de connexion wallet](assets/fr/12.webp)



Trong hướng dẫn này, chúng tôi sử dụng kết nối Lightning Address, tương thích với Chivo, Blink Wallet và Strike. Vui lòng nhập Lightning Address của bạn (định dạng nom@domaine.com), ví dụ từ LN Markets, Alby hoặc bất kỳ nhà cung cấp tương thích nào khác.



![Saisie de la Lightning Address](assets/fr/13.webp)



Sau khi đăng nhập, tài khoản của bạn đã hoạt động. Bây giờ bạn có thể truy cập POS hoặc quay lại bảng điều khiển để cấu hình các cài đặt khác.



![Connexion réussie](assets/fr/14.webp)



*Liên kết thanh toán** *Liên kết thanh toán



Menu "Công cụ Thanh toán" cung cấp quyền truy cập vào "Yêu cầu Thanh toán", cho phép bạn tạo và quản lý liên kết thanh toán. Tính năng này hữu ích để tạo liên kết thanh toán được cá nhân hóa để gửi qua email hoặc tin nhắn: quyên góp, thanh toán một lần, thanh toán nhiều lần, hoặc thậm chí là tường phí để bảo vệ nội dung. Bạn có thể tạo các loại liên kết khác nhau phù hợp với nhu cầu kinh doanh của mình.



![Liens de paiement](assets/fr/15.webp)



**Cấu hình thiết bị đầu cuối bán hàng**



Để chấp nhận thanh toán tại cửa hàng, hãy truy cập menu "Thiết bị đầu cuối bán hàng" từ "Công cụ thanh toán". Phần này cho phép bạn tạo và quản lý thiết bị đầu cuối POS (số lượng thiết bị đầu cuối tùy thuộc vào gói dịch vụ của bạn, xem so sánh gói Freemium và gói Doanh nghiệp bên dưới). Nhấp vào "Mở" để mở giao diện POS trong trình duyệt của bạn.



![Gestion des terminaux](assets/fr/16.webp)




**Tạo doanh số**



Máy POS hiển thị bàn phím số để nhập số tiền bán hàng. Nhập số tiền theo đơn vị tiền tệ địa phương của bạn (ví dụ: 500 sats tương ứng với 630,74 ARS), sau đó nhấn "OK" để xác nhận.



![Saisie du montant](assets/fr/17.webp)



Ứng dụng sẽ ngay lập tức tạo mã QR Lightning và thẻ Lightning Address để thanh toán. Khách hàng có thể quét mã QR bằng thẻ wallet hoặc sử dụng thẻ Bolt trên thiết bị đầu cuối NFC.



![QR code de paiement](assets/fr/18.webp)



Ngay sau khi nhận được thanh toán, màn hình xác nhận sẽ hiển thị số tiền nhận được theo đơn vị tiền tệ địa phương và satoshi. Bạn có thể gửi biên lai qua email, in hóa đơn hoặc bắt đầu giao dịch mới ngay lập tức.



![Paiement encaissé](assets/fr/19.webp)



**Giám sát và quản lý**



Tất cả giao dịch đều được ghi lại trong Bảng điều khiển dành cho Người bán. Bạn có thể theo dõi toàn bộ doanh thu theo kỳ, tổng số lượng bán hàng và lịch sử chi tiết cho mục đích kế toán.



Giao diện Cài đặt cung cấp một số tab cấu hình. Tab "Cài đặt Chung" cho phép bạn quản lý hồ sơ người bán và thông báo. Tab "Người dùng" cho phép bạn thêm và quản lý quyền truy cập vào Bảng điều khiển Người bán cho nhóm của mình (quản lý nhiều người dùng theo kế hoạch của bạn). Tab "Không gian Phát triển" cung cấp quyền truy cập vào khóa API cho các tích hợp nâng cao, trong khi tab "Đăng ký" cho phép bạn quản lý đăng ký của mình.



![Paramètres du compte marchand](assets/fr/20.webp)



**Gói Freemium so với gói Doanh nghiệp



Tiankii cung cấp hai gói cho Merchant Dashboard. Gói **Freemium** (miễn phí) phù hợp cho các doanh nghiệp khởi nghiệp với những hạn chế: một điểm bán hàng duy nhất, một người dùng duy nhất, khối lượng giao dịch hàng tháng giới hạn ở mức 1.000 USD và không được truy cập vào các cổng kết nối thương mại điện tử. Gói **Business** (phí 0,5% mỗi giao dịch) cung cấp số lượng thiết bị đầu cuối không giới hạn, số lượng người dùng không giới hạn, khối lượng giao dịch không giới hạn, quyền truy cập vào các plugin WooCommerce/Shopify/Cloudbeds và thông báo WhatsApp độc quyền.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Lợi ích và hạn chế



### Điểm nổi bật



**Tự quản lý**: Bạn giữ khóa riêng tư và toàn quyền kiểm soát tiền của mình. Không có nguy cơ bị đóng băng tài khoản hoặc nền tảng của bên thứ ba phá sản.



**Đơn giản**: Lightning Address dùng làm địa chỉ email, thanh toán NFC chỉ bằng một cú chạm đơn giản, giao diện trực quan mà không cần chuyên môn kỹ thuật.



**Hệ sinh thái hoàn chỉnh**: Công cụ dành cho mọi hồ sơ (cá nhân, nhà bán lẻ, nhà phát triển) với các tích hợp mô-đun phù hợp với nhu cầu của bạn.



**Tuân thủ chuyên nghiệp**: Lưu trữ đám mây an toàn, tuân thủ PCI-DSS, tuân thủ quy định của Salvador.



### Hạn chế



**Hạn chế về sét đánh**: Yêu cầu kết nối wallet cố định, quản lý thanh khoản cho khối lượng lớn, rủi ro lỗi nếu người nhận ngoại tuyến. Tiankii giảm thiểu những vấn đề này bằng các LSP tích hợp.



**Phụ thuộc vào SaaS**: Nếu Tiankii không khả dụng, việc tạo hóa đơn tạm thời không thể thực hiện được (tiền của bạn vẫn được bảo mật).



**Quyền riêng tư**: Tiankii có thể theo dõi siêu dữ liệu giao dịch (số tiền, ngày tháng). Ít riêng tư hơn so với giải pháp tự lưu trữ như BTCPay Server.



## Phần kết luận



Tiankii minh họa cách một cơ sở hạ tầng được thiết kế tốt có thể loại bỏ các rào cản kỹ thuật ngăn cản việc áp dụng rộng rãi Bitcoin như một loại tiền tệ hàng ngày. Bằng cách kết hợp sức mạnh của Lightning Network với phương pháp tiếp cận phi lưu ký và các công cụ dễ tiếp cận, hệ sinh thái này mang đến một con đường cân bằng giữa chủ quyền tài chính và tính dễ sử dụng.



Đối với các nhà bán lẻ, Tiankii mang đến cơ hội giảm đáng kể chi phí giao dịch đồng thời tiếp cận cơ sở khách hàng mới. Đối với người tiêu dùng, thẻ Lightning Address và NFC biến Bitcoin thành một loại tiền tệ thiết thực, không phức tạp về mặt kỹ thuật.



Mặc dù việc áp dụng rộng rãi Bitcoin vẫn là một thách thức đòi hỏi sự đào tạo và thời gian, nhưng các cơ sở hạ tầng như Tiankii chứng minh rằng các công cụ kỹ thuật đã hiện hữu. Sứ mệnh đơn giản hóa thanh toán Bitcoin không còn là một viễn cảnh xa vời mà đã trở thành hiện thực đối với bất kỳ ai sẵn sàng dấn thân.



## Tài nguyên



### Tài liệu chính thức




- [Trang web chính thức của Tiankii](https://tiankii.com)
- [Trung tâm trợ giúp Tiankii](https://help.tiankii.com)
- [Ứng dụng IBI](https://go.ibi.me)
- [Bảng điều khiển của người bán](https://pay.tiankii.com)
- [Trung tâm chỉ huy](https://cc.ibi.me)



### Hướng dẫn kết nối Wallet




- [Kết nối LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Kết nối BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Kết nối Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Kết nối Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Cộng đồng




- [Lightning Network Plus](https://lightningnetwork.plus) - Tài nguyên giáo dục Lightning
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Sáng kiến kinh tế tuần hoàn của Salvador Bitcoin



### Công cụ liên quan




- [Blink Wallet](https://blink.sv) - Khuyến nghị tương thích với Wallet Lightning
- [LNbits](https://lnbits.com) - Giải pháp wallet tự lưu trữ
- [Thẻ Bolt tiêu chuẩn](https://github.com/boltcard) - Thông số kỹ thuật cho thẻ NFC
