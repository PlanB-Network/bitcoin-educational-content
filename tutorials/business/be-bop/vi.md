---
name: be-BOP
description: Hướng dẫn thực tế để kiếm tiền từ doanh nghiệp của bạn với be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** là một nền tảng thương mại điện tử được thiết kế dành cho các doanh nhân muốn bán hàng trực tuyến và ngoại tuyến, hoàn toàn tự chủ, đồng thời chấp nhận thanh toán bằng Bitcoin, qua tài khoản ngân hàng và tiền mặt. Giải pháp này cũng hữu ích cho bất kỳ loại hình tổ chức nào muốn thu thập tiền quyên góp hoặc kiếm tiền từ các hoạt động khác nhau của mình.



Giải pháp này đơn giản, gọn nhẹ và tự động. Nó cho phép tạo ra một cửa hàng trực tuyến, ngay cả trong môi trường mà các dịch vụ tài chính truyền thống còn hạn chế hoặc chưa có. Thật vậy, **be-BOP** được thiết kế để hoạt động hiệu quả dù có hay không có kết nối với ngân hàng, sử dụng Bitcoin làm cơ sở hạ tầng thanh toán.



Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn từng bước:





- Tạo cửa hàng trực tuyến đầu tiên của bạn với **be-BOP**
- Cá nhân hóa gian hàng và sản phẩm của bạn
- Cấu hình các phương thức thanh toán khả dụng
- Hiểu các phương pháp hay nhất để bán hàng trực tuyến hiệu quả với **be-BOP**



Hướng dẫn này không yêu cầu kỹ năng chuyên môn cao. Nó hướng đến cả các nhà phát triển, nghệ nhân, thương nhân, hợp tác xã hoặc doanh nhân mong muốn tham gia vào thương mại điện tử một cách có chủ quyền và bền vững.



## Điều kiện tiên quyết để cài đặt be-BOP trên máy chủ của bạn



Trước khi bắt đầu cài đặt be-BOP, hãy đảm bảo bạn có cơ sở hạ tầng kỹ thuật sau. Những Elements này rất cần thiết để nền tảng hoạt động chính xác:



### Lưu trữ tương thích với S3



be-BOP sử dụng hệ thống lưu trữ để quản lý tệp (chẳng hạn như hình ảnh sản phẩm). Điều này yêu cầu quyền truy cập vào dịch vụ S3, chẳng hạn như:





- [MinIO](https://min.io/) tự lưu trữ
- Amazon S3 (AWS)
- Lưu trữ đối tượng Scaleway



Bạn sẽ cần cấu hình một thùng và cung cấp thông tin sau:





- S3_BUCKET**: tên thùng
- S3_ENDPOINT_URL**: liên kết truy cập đến dịch vụ S3 của bạn
- S3_KEY_ID** và S3_KEY_SECRET: mã truy cập của bạn
- S3_REGION**: khu vực dịch vụ S3 của bạn



### Cơ sở dữ liệu MongoDB ở chế độ ReplicaSet



be-BOP sử dụng MongoDB để lưu trữ dữ liệu cửa hàng, người dùng, sản phẩm và các dữ liệu khác.



Bạn có hai lựa chọn:





- Cài đặt MongoDB cục bộ với **chế độ ReplicaSet được bật**
- Sử dụng dịch vụ trực tuyến như **MongoDB Atlas**



Bạn sẽ cần các biến sau:





- MONGODB_URL**: kết nối cơ sở dữ liệu Address
- MONGODB_DB**: tên cơ sở dữ liệu



## Môi trường Node.js



be-BOP hoạt động với Node.js. Đảm bảo bạn đã cài đặt **Node.js** phiên bản 18 trở lên và **Corepack** đã được bật (cần thiết để quản lý các trình quản lý gói như pnpm). Lệnh cần chạy là `corepack enable`



### Git LFS đã được cài đặt



Một số tài nguyên (chẳng hạn như hình ảnh dung lượng lớn) được quản lý thông qua Git LFS (Lưu trữ Tệp Lớn). Hãy đảm bảo bạn đã cài đặt Git LFS trên máy tính bằng lệnh `git lfs install`. Khi các điều kiện tiên quyết này đã được đáp ứng, bạn đã sẵn sàng chuyển sang bước tiếp theo: tải xuống và cấu hình be-BOP.



**Lưu ý:** Hướng dẫn kỹ thuật về triển khai phần mềm có trong phần hướng dẫn riêng.



## Tạo tài khoản Super-Admin



Lần đầu tiên be-BOP được ra mắt, một tài khoản **Quản trị viên cấp cao** sẽ được tạo. Tài khoản này có đầy đủ quyền hạn cần thiết để quản lý các chức năng back-office. Để tạo tài khoản, hãy làm theo các bước sau:





- Đi tới `yourresiteweb/admin/login`
- Tạo tài khoản quản trị viên siêu cấp với thông tin đăng nhập và mật khẩu an toàn



Tài khoản này sẽ cho phép bạn truy cập tất cả các chức năng của văn phòng. Sau khi tạo, bạn có thể đăng nhập bằng cách nhập tên người dùng và mật khẩu.



![login](assets/fr/001.webp)



## Cấu hình và bảo mật Back-Office



Trước khi cấu hình kết nối back-office Interface, bạn cần tạo một Hash duy nhất. Điều này giúp bảo vệ chống lại các tác nhân độc hại cố gắng đánh cắp liên kết kết nối đến quản trị viên Interface của bạn.



Để tạo Hash, hãy vào `/admin/Settings`. Trong phần dành riêng cho bảo mật (ví dụ: "Quản trị Hash"), hãy định nghĩa một chuỗi duy nhất (Hash). Sau khi đăng ký, URL back-office sẽ được sửa đổi (ví dụ: `/admin-yourhash/login`) để hạn chế quyền truy cập của những người không được ủy quyền.



![hash-login](assets/fr/002.webp)



2.2. Kích hoạt chế độ bảo trì (nếu cần)



Vẫn trong /admin/Settings, (Cài đặt > Chung qua đồ họa Interface), hãy kiểm tra tùy chọn "bật chế độ bảo trì" ở cuối trang.



![maintenance-mode](assets/fr/003.webp)



Nếu cần, bạn có thể chỉ định danh sách các địa chỉ IPv4 được ủy quyền (phân cách bằng dấu phẩy) để cho phép truy cập vào front office trong quá trình bảo trì. Back office vẫn có thể được quản trị viên truy cập.



![ip-bebop](assets/fr/004.webp)



## Thiết lập truyền thông



Để cho phép be-BOP gửi thông báo (ví dụ: đơn hàng, đăng ký hoặc tin nhắn hệ thống), bạn cần cấu hình ít nhất một phương thức liên lạc. Có hai tùy chọn: email (SMTP) hoặc Nostr.



### Cấu hình SMTP (email)



be-BOP có thể gửi email qua máy chủ SMTP. Bạn cần có thông tin đăng nhập SMTP hợp lệ, thường được cung cấp bởi một dịch vụ email (ví dụ: Mailgun, Gmail, v.v.).



Sau đây là những điều bạn cần biết:



SMTP_HOST: Máy chủ SMTP Address (ví dụ: smtp.mailgun.org)



SMTP_PORT: cổng sử dụng (thường là 587 hoặc 465)



SMTP_USER: tên người dùng của bạn (thường là e-mail Address)



SMTP_PASSWORD: mật khẩu hoặc khóa API của bạn



SMTP_FROM: e-mail Address sẽ xuất hiện với tư cách là người gửi




### Cấu hình Nostr



be-BOP cho phép bạn gửi thông báo qua giao thức Nostr, một cơ sở hạ tầng nhắn tin phi tập trung. Để thực hiện việc này, bạn cần generate hoặc Supply một khóa riêng Nostr (NSEC). Bạn có thể generate khóa này trực tiếp thông qua Interface của be-BOP, trong phần dành riêng cho Nostr. Khi các Elements này được cấu hình chính xác, be-BOP sẽ có thể tự động gửi tin nhắn và cảnh báo đến người dùng của bạn.



## Phương thức thanh toán tương thích



be-BOP tương thích với nhiều giải pháp thanh toán, cho phép bạn cung cấp cho khách hàng sự linh hoạt hơn. Dưới đây là những gì bạn cần để thiết lập phương thức thanh toán phù hợp nhất với mình.



### Bitcoin Onchain



be-BOP cho phép bạn chấp nhận thanh toán Bitcoin trực tiếp trên Blockchain (On-Chain), một cách đơn giản và an toàn.



**Các bước cấu hình:**





- Vào menu **Cài đặt thanh toán**
- Nhấp vào **Bitcoin Nodeless** để truy cập các thông số thanh toán On-Chain.
- Hoàn thành các trường sau:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Mẹo:** Để lấy khóa công khai mở rộng (Zpub), bạn có thể tham khảo cài đặt nâng cao của Bitcoin Wallet (Sparrow wallet, BlueWallet, Spectre, v.v.). Đảm bảo Wallet của bạn **không phải là chỉ đọc** nếu bạn muốn sử dụng lịch sử giao dịch.



### Lightning Network



be-BOP cũng có thể chấp nhận thanh toán Bitcoin tức thì nhờ Lightning Network. Hiện có hai tùy chọn cấu hình:



**Phoenixd**



Vào menu `Cài đặt thanh toán`, nhấp vào `Phoenixd`



![phoenixd](assets/fr/006.webp)



Sau đó, bạn sẽ cần nhập **mật khẩu hoặc xác thực token** để kết nối bạn với phiên bản Phoenixd của mình, một chương trình phụ trợ do Acinq phát triển cho phép bạn quản lý thanh toán Lightning bằng nút của riêng mình nhưng không cần phải quản lý các kênh thanh toán phức tạp.



**Thẻ Bitcoin của Thụy Sĩ**



Nếu bạn không muốn tự mình quản lý một nút Lightning, **Swiss Bitcoin Pay** là giải pháp dễ sử dụng, dễ cấu hình, lý tưởng để bắt đầu chấp nhận thanh toán Lightning mà không cần cơ sở hạ tầng phức tạp.



Các bước cấu hình:





- Trong menu "Cài đặt thanh toán", nhấp vào `Swiss Bitcoin Pay`
- Đăng nhập vào tài khoản Swiss Bitcoin Pay của bạn (hoặc tạo một tài khoản nếu bạn chưa có).
- Nhập Khóa API do Swiss Bitcoin Pay cung cấp, sau đó nhấp vào "Lưu"



Sau khi thiết lập, be-BOP sẽ tự động xuất hóa đơn generate Lightning cho khách hàng của bạn và bạn sẽ nhận thanh toán trực tiếp vào tài khoản Swiss Bitcoin Pay của mình. Giải pháp này lý tưởng cho những người dùng muốn tránh sự phức tạp về mặt kỹ thuật của một nút cá nhân trong khi vẫn chấp nhận thanh toán nhanh chóng, chi phí thấp.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Ngoài Bitcoin, be-BOP còn cho phép bạn chấp nhận thanh toán bằng tiền mặt qua PayPal, một giải pháp quốc tế nổi tiếng và được sử dụng rộng rãi.



Các bước cấu hình:





- Vào menu `Cài đặt thanh toán`
- Nhấp vào `PayPal
- Trong tài khoản Paypal của bạn (phần dành cho nhà phát triển), hãy nhập `Client ID` và `Secret`
- Chọn loại tiền tệ bạn muốn (ví dụ: **USD**, **EUR**, **XOF**, v.v.)
- Nhấp vào `lưu



![paypal](assets/fr/008.webp)



**Lưu ý:** Bạn phải có tài khoản doanh nghiệp PayPal để sử dụng generate các mã định danh này. Bạn có thể lấy mã định danh này thông qua cổng thông tin [developer] (https://developer.paypal.com)



### Tóm tắt



Phần mềm hiện tích hợp giải pháp thanh toán **SumUp**, cho phép bạn chấp nhận thanh toán bằng thẻ tín dụng một cách đơn giản, an toàn và hiệu quả. Để tận dụng chức năng này, bạn cần cấu hình ban đầu. Dưới đây là các bước cần thực hiện, được đánh số rõ ràng và theo từng bước để triển khai:





- Bắt đầu bằng cách nhập **Khóa API**, một khóa bảo mật do SumUp cung cấp khi bạn tạo tài khoản nhà phát triển. Khóa này thiết lập kết nối an toàn giữa tài khoản SumUp của bạn và phần mềm.
- Điền vào trường `Mã Người bán` mã duy nhất xác định doanh nghiệp của bạn trong nền tảng SumUp. Mã này rất cần thiết để liên kết các giao dịch với doanh nghiệp của bạn.
- Trong trường `Tiền tệ`, hãy chọn loại tiền tệ chính mà bạn sử dụng cho các giao dịch của mình (ví dụ: **EUR**, **USD**, **CDF**, v.v.).
- Sau khi đã điền chính xác tất cả các trường, hãy nhấp vào nút `Lưu` để lưu cài đặt. Hệ thống sẽ thiết lập liên kết với tài khoản SumUp của bạn và phần mềm sẽ sẵn sàng chấp nhận thanh toán.



![payment-sumup](assets/fr/009.webp)



Sau khi cấu hình xong, tích hợp **SumUp** sẽ được kích hoạt và vận hành, cho phép bạn nhanh chóng rút tiền và theo dõi các giao dịch trực tiếp từ phần mềm.



### Sọc



be-BOP cũng cung cấp khả năng tích hợp đầy đủ với **Stripe**, một trong những nền tảng thanh toán trực tuyến phổ biến nhất. Stripe cho phép bạn chấp nhận thanh toán trực tuyến qua thẻ tín dụng, mã Wallet kỹ thuật số và một số phương thức thanh toán khác. Cách kích hoạt như sau:





- Nhập **khóa bí mật** được cung cấp trong bảng điều khiển Stripe.
- Hoàn thành trường **Khóa công khai** cũng được Stripe cung cấp.
- Chọn **loại tiền tệ chính**.
- Lưu cấu hình, sau đó nhấp vào `Lưu`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Xin lưu ý:** Điều cần thiết là phải biết chế độ VAT áp dụng cho hoạt động của bạn (ví dụ: bán theo VAT tại quốc gia của người bán, miễn trừ theo lý do chính đáng hoặc bán theo mức VAT tại quốc gia của người mua) để cấu hình chính xác các tùy chọn lập hóa đơn trong **be-BOP**.



## Cấu hình tiền tệ



**be-BOP** cung cấp khả năng quản lý tiền tệ tiên tiến và được điều chỉnh phù hợp với môi trường đa tiền tệ và các yêu cầu kế toán cụ thể. Để đảm bảo tính nhất quán trong hoạt động tài chính và báo cáo, việc cấu hình đúng các loại tiền tệ khác nhau được sử dụng trong hệ thống là rất quan trọng. Dưới đây là các bước cần thực hiện để cấu hình:





- Chọn **tiền tệ chính** (`Tiền tệ chính`)
- Chọn `Tiền tệ thứ cấp
- Định nghĩa **tiền tệ tham chiếu** (`Tiền tệ tham chiếu giá`)
- Chỉ ra `Tiền tệ kế toán



Sau khi tất cả các loại tiền tệ được cấu hình chính xác, phần mềm sẽ đảm bảo việc chuyển đổi tự động và chính xác các giao dịch đa tiền tệ, đồng thời duy trì tính nhất quán nghiêm ngặt trong kế toán.



![settings-currencies](assets/fr/011.webp)



## Cấu hình quyền truy cập phục hồi qua email hoặc Nostr



Vẫn trong `/admin/settings`, thông qua mô-đun **ARM**, hãy đảm bảo rằng tài khoản siêu quản trị viên bao gồm **email Address** hoặc **recovery pub**, do đó sẽ tạo điều kiện thuận lợi cho quy trình này nếu bạn quên mật khẩu.



![settings-users](assets/fr/012.webp)



## Cài đặt ngôn ngữ



Phần mềm cung cấp khả năng đa ngôn ngữ để phù hợp với đối tượng người dùng quốc tế và nâng cao trải nghiệm người dùng. Để kích hoạt chức năng đa ngôn ngữ, điều quan trọng là phải cấu hình các ngôn ngữ khả dụng và xác định **ngôn ngữ mặc định**.



![settings-languages](assets/fr/13.webp)



## Interface và cấu hình Identity trong be-BOP



**be-BOP** cung cấp cho các nhà thiết kế tất cả các công cụ cần thiết để thiết kế một trang web. Bước đầu tiên là mở mục `/Admin > Merch > Layout` trong phần cài đặt. Bắt đầu bằng cách cấu hình **Thanh trên cùng**, **Thanh điều hướng** và **Chân trang**.



### Le Top Bar



Cấu hình **Thanh trên cùng** cho phép bạn cá nhân hóa nhận diện thương hiệu phần mềm bằng cách hiển thị thông tin chính ngay từ dòng đầu tiên của Interface. Điều này củng cố nhận diện thương hiệu và cung cấp bối cảnh rõ ràng cho người dùng.



#### Các bước cấu hình:





- Trong trường `Tên thương hiệu`, hãy nhập tên công ty, tổ chức hoặc sản phẩm của bạn. Tên này sẽ xuất hiện ở đầu mẫu Interface và sẽ đại diện cho hình ảnh nhận diện chính của bạn.
- Ghi rõ tiêu đề trang web**: tiêu đề được chọn phải tóm tắt mục đích của nền tảng. Tiêu đề này có thể xuất hiện ở tiêu đề trang hoặc trong tab trình duyệt.
- Thêm mô tả trang web**: đây là nơi bạn nhập mô tả ngắn gọn về sáng kiến của mình. Mô tả này giúp ngữ cảnh hóa công cụ cho người dùng và cũng có thể được sử dụng cho mục đích SEO.



Sau khi nhập thông tin này, **Thanh trên cùng** sẽ hiển thị bản trình bày rõ ràng, chuyên nghiệp và mạch lạc về giải pháp của bạn.



#### Liên kết ở thanh trên cùng



Phần `Liên kết` trên Thanh Trên cùng cho phép bạn thêm lối tắt đến các trang quan trọng trong ứng dụng hoặc trên các trang web bên ngoài. Các liên kết này được hiển thị trực tiếp trên Thanh Trên cùng, mang đến cho người dùng khả năng truy cập nhanh chóng và có cấu trúc.



#### Các bước cấu hình:





- Nhập tên liên kết (Văn bản)**: trong trường `Văn bản`, nhập tên hoặc nhãn của liên kết theo cách hiển thị (ví dụ: Trang chủ, Liên hệ, Trợ giúp...).
- Chỉ định liên kết Address (Url)**: trong trường `Url`, nhập đầy đủ Address của trang đích (nội bộ hoặc bên ngoài).
- Thêm các liên kết khác nếu cần**: mỗi dòng cấu hình cho phép bạn thêm một liên kết bổ sung bằng cách sử dụng các trường `Text` và `Url`.
- Lưu liên kết**: sau khi đã nhập tất cả liên kết, hãy nhấp vào nút "Thêm liên kết thanh trên cùng" để lưu chúng.



Cấu hình này cho phép bạn cung cấp khả năng điều hướng rõ ràng, mượt mà và dễ tiếp cận qua các phần khác nhau của trang web hoặc đến các tài nguyên bổ sung.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



Phần **Thanh điều hướng** cho phép bạn cấu hình menu điều hướng chính của be-BOP, thường nằm ở cạnh bên hoặc phía trên của Interface. Menu này hướng dẫn người dùng đến các trang và chức năng khác nhau của ứng dụng. Việc cấu hình liên kết rất đơn giản và trực quan. Cách thức hoạt động như sau:





- Nhập tên liên kết (`Text`)**: trên dòng cấu hình, hãy bắt đầu bằng cách điền vào trường `Text`. Trường này tương ứng với tên của liên kết hiển thị trên thanh điều hướng (ví dụ: *Dashboard*, *Users*, *Settings*...).
- Nhập liên kết Address (`Url`)**: bên cạnh trường `Văn bản`, bạn sẽ thấy trường `Url`. Trong trường này, hãy nhập Address của trang mà liên kết sẽ chuyển hướng đến. Đây có thể là một tuyến đường nội bộ hoặc một liên kết đến một trang bên ngoài.
- Thêm nhiều liên kết nếu cần**: bên dưới dòng đầu tiên, các trường `Text` và `Url` mới có sẵn để thêm bao nhiêu liên kết tùy thích. Mỗi dòng đại diện cho một liên kết điều hướng bổ sung.
- Lưu liên kết**: sau khi bạn đã nhập tất cả Elements, hãy nhấp vào nút `Thêm liên kết thanh điều hướng` để lưu và hiển thị kết quả trên thanh điều hướng.



Cấu hình này cho phép cấu trúc hóa hiệu quả quyền truy cập vào các phần khác nhau của phần mềm, cải thiện tính công thái học và trải nghiệm của người dùng.



![navbar](assets/fr/015.webp)



### Chân trang



Phần **Chân trang** cho phép bạn tùy chỉnh chân trang của phần mềm, thêm thông tin hoặc liên kết hữu ích. Trước khi cấu hình liên kết, hãy bắt đầu bằng cách kích hoạt một tùy chọn cụ thể:





- Cho phép hiển thị nhãn "Được cung cấp bởi be-BOP"**: kích hoạt nút `Hiển thị được cung cấp bởi be-BOP` để hiển thị nhãn này ở chân trang.
- Nhập tên liên kết (`Văn bản`)**: điền vào trường `Văn bản` tương ứng với nội dung của liên kết ở phần chân trang (ví dụ: *Điều khoản*, *Quyền riêng tư*, *Liên hệ*...).
- Chỉ định liên kết Address (`Url`)**: trong trường `Url`, nhập Address của trang đích (nội bộ hoặc bên ngoài).
- Thêm liên kết nếu cần**: sử dụng các dòng bổ sung để tạo nhiều liên kết tùy thích.
- Lưu liên kết**: nhấp vào nút "Thêm liên kết chân trang" để lưu liên kết.



![footer](assets/fr/016.webp)



### Cá nhân hóa trực quan



**⚠️ Đừng quên thiết lập logo cho chủ đề sáng và tối, cũng như favicon, thông qua** `Admin > Merch > Pictures`.



Sau đây là cách tùy chỉnh giao diện trang web của bạn:



#### Đi đến phần Hình ảnh



Menu `Quản trị` > `Hàng hóa` > `Hình ảnh`.



#### Thêm hình ảnh mới



Nhấp vào `Ảnh mới`.



#### Chọn một tập tin cục bộ



Nhấp vào `Chọn tệp`, sau đó chọn hình ảnh từ đĩa Hard của bạn.



#### Chọn tệp để nhập



Nhấp đúp vào hình ảnh cần nhập (logo sáng, logo tối hoặc favicon).



#### Đặt tên cho hình ảnh



Điền vào trường `Tên của hình ảnh`.



#### Thêm hình ảnh



Nhấp vào `Thêm` để hoàn tất quá trình nhập.



![pictures](assets/fr/017.webp)



### Thiết lập danh tính người bán



#### Cài đặt danh tính



Có thể truy cập thông qua `Quản trị > Danh tính` (hoặc `Cài đặt > Danh tính`), phần này cho phép bạn cấu hình thông tin hành chính và pháp lý của công ty.



#### Thông tin pháp lý





- Tên doanh nghiệp**: tên công ty chính thức.
- Mã số doanh nghiệp**: mã số định danh hợp pháp hoặc số đăng ký (RCCM, SIRET...).



#### Doanh nghiệp Address





- Đường phố**: mã bưu chính Address (đường phố, số nhà...).
- Quốc gia**: quốc gia.
- Tiểu bang**: tỉnh hoặc khu vực.
- Thành phố**: thành phố.
- Mã ZIP**: mã bưu chính.



#### Thông tin liên lạc





- Email**: email chuyên nghiệp Address.
- Điện thoại**: số điện thoại công ty.



#### Tài khoản ngân hàng





- Tên chủ tài khoản**: tên của chủ tài khoản.
- Chủ tài khoản Address**: Address của chủ tài khoản.
- IBAN**: Số tài khoản ngân hàng quốc tế.
- BIC**: Mã SWIFT/BIC.



![bank-account](assets/fr/019.webp)



#### Thanh toán





- Nhấp vào `Điền thông tin cửa hàng chính` để điền trước dữ liệu.
- Thông tin người phát hành ở góc trên bên phải**: trường thông tin pháp lý/thuế hiển thị trên hóa đơn.
- Nhấp vào `Cập nhật` để lưu thay đổi.



**Lưu ý:** bạn cũng có thể nhập thêm thông tin để hiển thị trên Invoice tùy theo nhu cầu của bạn.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Cửa hàng vật lý Address



Đối với những người có cửa hàng vật lý, hãy thêm mã Address đầy đủ cụ thể vào mục `Quản trị > Cài đặt > Danh tính` hoặc một mục riêng. Thao tác này sẽ cho phép mã Address được hiển thị trên các tài liệu chính thức và ở phần chân trang nếu cần.



![seller-id](assets/fr/021.webp)



## Quản lý sản phẩm



### Tạo sản phẩm mới



Vào `Quản trị > Hàng hóa > Sản phẩm` để thêm hoặc sửa đổi sản phẩm. Điền vào các trường sau:



#### Thông tin cơ bản





- Tên sản phẩm**: tên của sản phẩm (ví dụ: *Áo phông BOP phiên bản giới hạn*).
- Slug**: Mã định danh URL không có khoảng trắng (ví dụ: `tshirt-bop-edition-limitee`).
- Biệt danh** *(tùy chọn)*: hữu ích để thêm nhanh vào giỏ hàng thông qua trường chuyên dụng.



![product-config](assets/fr/028.webp)



#### Giá cả





- Số tiền giá**: giá sản phẩm (ví dụ: `25,00`).
- Giá Tiền tệ**: tiền tệ (EUR, USD, BTC, v.v.).
- Sản phẩm đặc biệt**:
  - đây là sản phẩm miễn phí.
  - đây là sản phẩm trả theo nhu cầu của bạn.



#### Tùy chọn sản phẩm





- Sản phẩm đơn lẻ (`độc lập`)**: chỉ có thể thêm một sản phẩm cho mỗi đơn hàng (ví dụ: quyên góp, vé vào cửa).
- Sản phẩm có nhiều biến thể**:
  - Không chọn `Standalone`.
  - Kiểm tra `Sản phẩm có sự thay đổi nhỏ (không có sự khác biệt về số lượng)`.
  - Thêm vào:
    - Tên** (ví dụ: *Kích thước*),
    - Giá trị** (ví dụ: S, M, L, XL),
    - Chênh lệch giá** nếu có (ví dụ: `+2 USD` cho cỡ XL).



![product-details](assets/fr/029.webp)



## Quản lý kho



### Tùy chọn nâng cao khi tạo sản phẩm (Kho, Giao hàng, Vé, v.v.)



#### Sản phẩm có số lượng hạn chế



Nếu sản phẩm của bạn không có sẵn với số lượng không giới hạn, hãy chọn `Sản phẩm có số lượng tồn kho hạn chế`. Thao tác này sẽ kích hoạt tính năng tự động theo dõi số lượng còn lại. Sau khi chọn ô này, một trường sẽ xuất hiện để cho biết **số lượng tồn kho**.



Hệ thống quản lý:





- Hàng tồn kho** → sản phẩm trong giỏ hàng chưa thanh toán
- Hàng đã bán** → sản phẩm đã mua



**Thời gian đặt giỏ hàng**: Khi khách hàng thêm sản phẩm vào giỏ hàng, sản phẩm sẽ được "đặt trước" trong một khoảng thời gian giới hạn. Bạn có thể thay đổi thời gian này trong: `Admin > Config > Cart reservation` (giá trị tính bằng phút)



#### Sản phẩm cần giao?



Đánh dấu vào ô `Sản phẩm có linh kiện vật lý sẽ được vận chuyển đến địa chỉ Address của khách hàng`. Điều này hữu ích cho tất cả các sản phẩm được vận chuyển vật lý (sách, áo phông, v.v.)



#### Các tùy chọn khác





- Vé**: đánh dấu nếu sản phẩm là vé cho một sự kiện
- Đặt chỗ**: kiểm tra xem đây có phải là khoảng thời gian đặt chỗ không (ví dụ: buổi học, cuộc hẹn)



![product-options](assets/fr/030.webp)



### Cài đặt hành động (dưới cùng)



Phần này xác định **nơi** và **cách** có thể xem và mua sản phẩm:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Chỉ chọn những kênh bạn muốn sử dụng.



## Tạo và tùy chỉnh các trang và tiện ích CMS



### Các trang CMS bắt buộc



Vào `Quản trị > Hàng hóa > CMS`. Bạn sẽ thấy danh sách các trang hiện có và có thể thêm trang mới bằng cách chọn **Thêm trang CMS**.



Các trang CMS rất quan trọng đối với:





- Thông báo cho khách truy cập của bạn (ví dụ: điều khoản sử dụng)
- Tuân thủ luật pháp (ví dụ: chính sách bảo mật)
- Giải thích một số tính năng của cửa hàng (ví dụ: thu thập IP, VAT 0%)



Bạn có thể thêm các trang khác nếu cần:





- Giới thiệu về chúng tôi / Chúng tôi là ai
- Hỗ trợ chúng tôi / Quyên góp
- Câu hỏi thường gặp
- Liên hệ
- vân vân.



**Mẹo: Nhấp vào từng liên kết hoặc biểu tượng để sửa đổi **nội dung**, **tiêu đề** hoặc **khả năng hiển thị SEO** của mỗi trang.



### Bố cục và đồ họa Elements



Vào: `Quản trị > Hàng hóa > Bố cục`. Bạn có thể tùy chỉnh giao diện Elements của trang web:



![product-options](assets/fr/032.webp)



#### Thanh trên cùng





- Sửa đổi hoặc xóa liên kết (VÍ DỤ: TRANG CHỦ, GIỚI THIỆU,...)
- Điều hướng giữa các phần chính của trang web



#### Thanh điều hướng (thanh điều hướng chính)





- Có mặt ở vùng màu xám bên dưới thanh trên cùng
- Bao gồm quyền truy cập nhanh vào: `Config`, `Payment Settings`, `Transaction`, `Node Management`, `Widgets`, v.v.
- Chỉ dành cho giám đốc



#### Chân trang





- Có thể chỉnh sửa từ `Admin > Merch > Layout`
- Bao gồm: thông tin liên lạc, liên kết hữu ích, thông báo pháp lý.



#### Tùy chỉnh hình ảnh



Đi tới: `Quản trị > Hàng hóa > Hình ảnh`



Bạn có thể:





- Thay đổi **logo chính**
- Sửa đổi hoặc thêm bố cục **hình ảnh**



#### Mô tả trang web



Ngoài ra, có thể sửa đổi trong `Hình ảnh`, cho phép bạn hiển thị **tóm tắt hoặc khẩu hiệu** ở đầu trang hoặc chân trang, tùy thuộc vào chủ đề.



**Lưu ý:** điều này cho phép bạn điều chỉnh giao diện theo nhận diện thương hiệu của mình (giáo dục, thương mại hoặc cộng đồng).



### Tích hợp tiện ích vào các trang CMS



Tiện ích** làm phong phú thêm các trang CMS của bạn bằng Elements động hoặc trực quan.



#### Tạo tiện ích



Đi tới: `Quản trị > Tiện ích`



Ví dụ về các tiện ích có sẵn:





- Thử thách**: thử thách hoặc nhiệm vụ
- Thẻ**: danh mục hoặc từ khóa
- Thanh trượt**: vòng quay hình ảnh
- Thông số kỹ thuật**: Bảng thông số kỹ thuật
- Biểu mẫu**: biểu mẫu (liên hệ, phản hồi, v.v.)
- Đếm ngược**: bộ đếm thời gian
- Thư viện ảnh**: thư viện ảnh
- Bảng xếp hạng**: bảng xếp hạng của người dùng



![widgets](assets/fr/033.webp)



#### Tích hợp vào các trang CMS



Sử dụng **mã ngắn** trong nội dung trang CMS của bạn:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Thông số hiện tại**:





- `slug`: mã định danh tiện ích duy nhất
- `display=img-1`: hình ảnh cụ thể của sản phẩm
- `width`, `height`, `fit`: kích thước và kiểu dáng hình ảnh
- autoplay=3000`: thời gian tính bằng ms giữa hai trang chiếu



**Thuận lợi**:





- Dễ dàng chèn (sao chép và dán)
- Động: bất kỳ sửa đổi nào đối với tiện ích đều được tự động phản ánh
- Không cần nhà phát triển



## Quản lý đơn hàng và báo cáo



### Theo dõi đơn hàng



Để xem và quản lý các đơn hàng trước đây, hãy vào: `Quản trị > Giao dịch > Đơn hàng`



Tại đây bạn sẽ tìm thấy **danh sách đầy đủ các đơn hàng** đã được đặt trên trang web của bạn.



![orders](assets/fr/034.webp)



#### Hình ảnh hóa và tìm kiếm



Interface cho phép bạn tìm kiếm và lọc đơn hàng theo một số tiêu chí:





- Số đơn hàng: số đơn hàng
- bí danh sản phẩm: mã định danh hoặc tên sản phẩm
- "Phương thức thanh toán": phương thức thanh toán được sử dụng (thẻ, tiền điện tử, v.v.)
- `Email`: email của khách hàng



Các bộ lọc này giúp tìm kiếm nhanh chóng và quản lý có mục tiêu.



#### Chi tiết của từng đơn hàng



Bằng cách nhấp vào một đơn hàng, bạn có thể truy cập vào tệp đầy đủ có chứa:





- Sản phẩm đã đặt hàng
- Thông tin khách hàng
- Giao hàng Address (nếu có)
- Bất kỳ ghi chú nào liên quan đến đơn hàng



#### Các hành động có thể thực hiện trên một đơn hàng



Bạn có thể:





- Xác nhận đơn hàng (nếu đang chờ xử lý)
- Hủy đơn hàng (trong trường hợp có vấn đề hoặc yêu cầu của khách hàng)
- Thêm **nhãn** (để tổ chức nội bộ)
- Tham khảo / thêm **ghi chú nội bộ**



**Lưu ý:** phần này rất cần thiết cho hoạt động hậu cần và quan hệ khách hàng tốt.



### Báo cáo và xuất khẩu



Để truy cập số liệu thống kê bán hàng và thanh toán:


quản trị viên > Cài đặt > Báo cáo



![reporting](assets/fr/035.webp)



Tại đây, bạn sẽ tìm thấy tổng quan về doanh nghiệp của mình dưới dạng **báo cáo hàng tháng và hàng năm**.



#### Báo cáo nội dung



Các báo cáo được chia thành các phần:





- Chi tiết đơn hàng**: số lượng đơn hàng, trạng thái (đã xác nhận, đã hủy, đang chờ xử lý), tiến độ
- Chi tiết sản phẩm**: sản phẩm đã bán, số lượng, sản phẩm phổ biến
- Chi tiết thanh toán**: số tiền đã thu, phân tích theo phương thức thanh toán



#### Xuất dữ liệu



Mỗi phần đều có nút **Xuất CSV** cho phép bạn:





- Tải xuống dữ liệu ở định dạng CSV
- Mở chúng trong Excel, Google Trang tính, v.v.
- Lưu trữ để sử dụng cho mục đích hành chính hoặc kế toán
- Sử dụng chúng cho các báo cáo nội bộ



**Lưu ý:** lý tưởng để theo dõi hiệu suất, kế toán và thuyết trình.



## Cấu hình nhắn tin Nostr (tùy chọn)



![nostr-config](assets/fr/036.webp)



Nền tảng này hỗ trợ giao thức **Nostr** cho một số chức năng nâng cao:





- Thông báo phi tập trung
- Đăng nhập không cần mật khẩu
- Quản lý ánh sáng Interface



### Tạo và thêm khóa riêng Nostr



Đi tới:


quản trị viên > Quản lý nút > Nostr





- Nhấp vào **Tạo nsec** nếu bạn chưa có.
- Hệ thống có thể generate tự động.
- Ngoài ra, bạn có thể sử dụng khóa hiện có (ví dụ: từ Damus hoặc Amethyst).



Kế tiếp:





- Sao chép khóa `nsec`
- Thêm nó vào tệp `.env.local` (hoặc `.env`) của bạn: ```env NOSTR_PRIVATE_KEY=YourNsecIciKey



### Các tính năng được kích hoạt bằng Nostr



Sau khi cấu hình, một số chức năng sẽ khả dụng:



**Thông báo qua Nostr**





- Gửi cảnh báo về đơn hàng, thanh toán hoặc sự kiện hệ thống
- Dành cho người quản trị hoặc người dùng



**Quản lý ánh sáng Interface**





- Có thể truy cập thông qua ứng dụng khách Nostr
- Cho phép quản lý nhanh chóng, thân thiện với thiết bị di động



**Kết nối không cần mật khẩu**





- Đăng nhập bằng liên kết bảo mật (gửi qua Nostr)
- An toàn và tính lưu động cao hơn cho người dùng



## Thiết kế và tùy chỉnh chủ đề



Để điều chỉnh giao diện cửa hàng của bạn theo điều lệ đồ họa, hãy vào: `Quản trị > Hàng hóa > Chủ đề`



Tại đây bạn sẽ tìm thấy tất cả các tùy chọn để **tạo** và **cấu hình** một chủ đề tùy chỉnh.



### Tạo chủ đề



![theme](assets/fr/037.webp)



Khi tạo hoặc sửa đổi chủ đề, bạn có thể xác định:





- Màu sắc**: cho nút, hình nền, văn bản, liên kết, v.v.
- Phông chữ**: lựa chọn kiểu chữ cho tiêu đề, đoạn văn, menu
- Kiểu đồ họa**: đường viền, lề, khoảng cách, hình khối



### Các phần có thể tùy chỉnh



Mỗi phần của trang web có thể được điều chỉnh độc lập:





- Tiêu đề**: thanh điều hướng trên cùng
- Nội dung chính**:
- Footer**: cuối trang



**Lưu ý:** mức độ chi tiết này đảm bảo tính nhất quán giữa hình ảnh của trang web và bản sắc thương hiệu của bạn.



### Kích hoạt chủ đề



Sau khi chủ đề được cấu hình:





- Nhấp vào **Lưu**
- Kích hoạt nó làm **chủ đề chính** của cửa hàng



**Lưu ý:** chủ đề đang hoạt động là chủ đề mà khách truy cập có thể nhìn thấy.



## Cấu hình mẫu email



Nền tảng này cho phép bạn cá nhân hóa các email được gửi tự động đến người dùng. Truy cập: `Quản trị > Cài đặt > Mẫu`



![emails-templates](assets/fr/038.webp)



### Tạo / chỉnh sửa mẫu



Mỗi email (xác nhận đơn hàng, quên mật khẩu, v.v.) đều có:





- Tiêu đề**: tiêu đề của email (ví dụ: "Đơn hàng của bạn đã được xác thực")
- Nội dung HTML**: Nội dung HTML hiển thị trong email



**Lưu ý:** bạn có thể chèn văn bản, hình ảnh, liên kết, v.v. tùy theo nhu cầu.



### Sử dụng các biến động



Để làm cho email trở nên động, hãy chèn các biến như:





- `{orderNumber}}`: thay thế bằng số đơn hàng thực tế
- `{invoiceLink}}`: liên kết đến Invoice
- `{websiteLink}}`: URL của trang web của bạn



**Lưu ý:** các thẻ này sẽ tự động được thay thế khi gửi.



### Mẹo nâng cao





- Tạo email **phản hồi** để dễ đọc trên thiết bị di động
- Thêm **các nút hành động** (thanh toán, tải xuống, theo dõi đơn hàng)
- Kiểm tra email của bạn bằng cách gửi chúng cho chính mình trước khi xuất bản



## Cấu hình các thẻ và tiện ích cụ thể



### Quản lý thẻ



Thẻ có thể được sử dụng để cấu trúc và làm phong phú nội dung của bạn. Để truy cập chúng: `Quản trị > Tiện ích > Thẻ`



![tags-config](assets/fr/039.webp)



### Tạo thẻ



Hoàn thành các trường sau:





- Tên thẻ**: tên thẻ được hiển thị
- Slug**: mã định danh duy nhất (không có khoảng trắng hoặc dấu trọng âm)
- Họ thẻ**: nhóm các thẻ theo danh mục



![targsconfig](assets/fr/040.webp)



#### Các gia đình có sẵn:





- người sáng tạo: tác giả hoặc nhà sản xuất
- nhà bán lẻ: nhân viên bán hàng hoặc điểm bán hàng
- `Thời gian`: thời kỳ hoặc ngày tháng
- sự kiện: sự kiện liên quan



### Các trường tùy chọn



Các trường này có thể được sử dụng để làm giàu thẻ như thể đó là một trang nội dung:





- Tiêu đề
- Phụ đề
- Nội dung ngắn**
- Nội dung đầy đủ** (bằng tiếng Pháp)
- CTA** (nút hành động)



### Sử dụng thẻ



Thẻ có thể là:





- Phân bổ cho sản phẩm
- Được tích hợp vào các trang CMS bằng thẻ: [Tag=slug?display=var-1]



## Cấu hình các tập tin có thể tải xuống



Để cung cấp tài liệu có thể tải xuống cho khách hàng của bạn: `Quản trị > Hàng hóa > Tệp`



### Thêm một tập tin



1. Nhấp vào **Tệp mới**


2. Thông báo:




   - Tên tệp** (ví dụ: *Hướng dẫn cài đặt*)
   - Tệp để tải lên** (PDF, hình ảnh, Word...)



**Lưu ý:** sau khi thêm vào, nền tảng sẽ tự động tạo **liên kết cố định**.



### Sử dụng liên kết



Sau đó, liên kết này có thể được chèn vào:





- Trang CMS** (dưới dạng liên kết văn bản hoặc nút)
- **Ứng dụng email** (thông qua mẫu)
- **Bảng thông tin sản phẩm** (ví dụ: tải xuống thủ công)



Thích hợp để cung cấp *hướng dẫn sử dụng, hướng dẫn kỹ thuật, bảng thông tin sản phẩm...* mà không cần lưu trữ bên ngoài.



## Nostr-bot



Nền tảng này cung cấp khả năng tích hợp nâng cao với giao thức **Nostr** thông qua bot tự động.



Đi tới: Quản lý nút > Nostr



### Các tính năng chính



#### Quản lý rơle





- Thêm hoặc xóa **rơle** được bot sử dụng
- Tối ưu hóa phạm vi tiếp cận và độ tin cậy của tin nhắn đã gửi



#### Tin nhắn giới thiệu tự động





- Kích hoạt tin nhắn tự động khi **tương tác với người dùng lần đầu**
- Lý tưởng cho:
  - Giới thiệu dịch vụ của bạn
  - Gửi một liên kết hữu ích (ví dụ: Câu hỏi thường gặp, liên hệ, đặt hàng)



#### Chứng nhận `npub của bạn





- Thêm **logo** và **tên công khai**
- Liên kết đến **tên miền web đã được xác minh**
- Tăng cường độ tin cậy và khả năng nhận diện danh tính Nostr của bạn



### Các trường hợp sử dụng Nostr-bot





- Gửi **xác nhận đơn hàng** cho bạn
- Phản hồi tự động cho **sự kiện (ví dụ: đơn hàng mới)**
- Tạo ra **tương tác khách hàng phi tập trung**



## Quá tải nhãn dịch thuật



be-BOP hỗ trợ nhiều ngôn ngữ (FR, EN, ES...), nhưng bạn có thể điều chỉnh bản dịch cho phù hợp với nhu cầu của mình.



Để thực hiện việc này, hãy vào: `Cài đặt > Ngôn ngữ`



### Đang tải và chỉnh sửa



Các tệp dịch được lưu ở định dạng JSON. Bạn có thể:





- Tải xuống** tệp ngôn ngữ
- Sửa đổi** các văn bản hiện có
- Thêm** bản dịch của riêng bạn



Liên kết đến các tập tin gốc:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Ví dụ:** thay thế `Thêm vào giỏ hàng` bằng `Ajouter au panier` hoặc `Acheter`.



## Làm việc nhóm & Điểm bán hàng (POS)



### Quản lý người dùng và quyền truy cập



#### Tạo vai trò



Đi tới: `Quản trị > Cài đặt > ARM`



Nhấp vào **Tạo vai trò** để tạo vai trò (ví dụ: `Quản trị viên cấp cao`, `POS`, `Người kiểm tra vé`).



Mỗi vai trò bao gồm:





- quyền truy cập ghi**: quyền truy cập ghi
- quyền truy cập đọc**: quyền truy cập đọc
- cấm truy cập**: các phần xen kẽ



#### Tạo người dùng



Trong cùng menu `Quản trị > Cài đặt > ARM`, thêm người dùng bằng:





- đăng nhập
- bí danh
- phục hồi email
- (tùy chọn) `recovery npub` để kết nối qua Nostr



Chỉ định vai trò đã xác định trước đó.



![pos-users](assets/fr/045.webp)



Người dùng chỉ đọc** sẽ thấy menu được in *in nghiêng* và không thể sửa đổi nội dung.



## Cấu hình điểm bán hàng (POS)



### Chỉ định vai trò POS



Để cấp cho người dùng quyền truy cập vào POS, hãy chỉ định vai trò `Điểm bán hàng (POS)` trong: `Quản trị viên > Cấu hình > ARM`



Anh ấy có thể kết nối thông qua URL an toàn: `/pos` hoặc `/pos/touch`



### Các tính năng dành riêng cho POS



Be-BOP cung cấp Interface chuyên dụng cho bán hàng thực tế (cửa hàng, sự kiện, v.v.).



#### Thêm nhanh qua bí danh



Trong `/cart`, một trường cho phép bạn thêm sản phẩm:





- Bằng cách quét mã vạch ** (ISBN, EAN13)
- Bằng cách nhập **bí danh sản phẩm** theo cách thủ công



**Lưu ý:** sản phẩm sẽ được tự động thêm vào giỏ hàng.



#### Phương thức thanh toán



POS hỗ trợ:





- Giống loài
- Thẻ tín dụng
- Lightning Network (mã hóa)
- Những người khác theo cấu hình



Có hai tùy chọn nâng cao:





- Miễn thuế GTGT**: áp dụng khi có lý do chính đáng (tổ chức phi chính phủ, người nước ngoài...)
- Giảm giá quà tặng**: giảm giá đặc biệt với bình luận bắt buộc



#### Hiển thị phía máy khách



URL `/pos/session` dành cho **màn hình phụ** (HDMI, máy tính bảng...):



Áp phích:





- Sản phẩm đang tiến hành
- Tổng số tiền
- Phương thức thanh toán
- Giảm giá được áp dụng



**Lưu ý:** khách hàng theo dõi đơn hàng trực tiếp, trong khi người bán ghi lại đơn hàng trên `/pos`.



### Tóm tắt POS



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Cảm ơn bạn đã làm theo hướng dẫn này một cách cẩn thận.