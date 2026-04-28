---
name: Bisq 2
description: Hướng dẫn đầy đủ về cách sử dụng Bisq 2 và trao đổi bitcoin trên P2P
---
![cover](assets/cover.webp)


## Giới thiệu


Các sàn giao dịch ngang hàng không cần KYC (P2P) rất cần thiết để bảo vệ quyền riêng tư và quyền tự chủ tài chính của người dùng. Chúng cho phép giao dịch trực tiếp giữa các cá nhân mà không cần xác minh danh tính, điều này rất quan trọng đối với những người coi trọng quyền riêng tư. Để hiểu sâu hơn về các khái niệm lý thuyết, hãy tham khảo khóa học BTC204:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Bisq 2 là gì?


Bisq 2 là phiên bản mới của sàn giao dịch phi tập trung Bisq nổi tiếng, ra mắt năm 2024. Khác với phiên bản tiền nhiệm, Bisq 2 được phát triển để hỗ trợ nhiều giao thức trao đổi, mang lại cho người dùng sự linh hoạt hơn.


**Các tính năng mới chính:**




- Hỗ trợ nhiều mạng bảo mật riêng tư (Tor, I2P)
- Nhiều danh tính để bảo mật tốt hơn
- REST API dành cho bot giao dịch
- Hỗ trợ nhiều loại wallet khác nhau
- Hệ thống phân công nhiệm vụ với khoản tiền gửi bắt buộc trong BSQ


Hướng dẫn này tập trung hoàn toàn vào "Bisq Easy", giao thức duy nhất hiện có. Bisq Easy được thiết kế đặc biệt cho người dùng Bitcoin mới. Giao thức này cho phép người dùng mua và bán bitcoin bằng tiền tệ pháp định trên nền tảng ngang hàng phi tập trung. Giao dịch bị giới hạn ở mức tương đương 600 USD (với mức tối thiểu là 6 USD), và tính bảo mật của giao dịch dựa trên uy tín của người bán trên BTC. Bisq Easy không có phí giao dịch hoặc yêu cầu ký quỹ bảo đảm. Dự kiến ​​Bisq Easy sẽ thay thế Bisq 1 cho các giao dịch tiền tệ pháp định dưới 600 USD (hoặc tương đương).


**Các tính năng chính:**




- Ứng dụng máy tính để bàn đa nền tảng
- Có nhiều giao thức trao đổi khác nhau
- Mạng P2P phi tập trung
- Tập trung vào quyền riêng tư (không yêu cầu xác minh danh tính, sử dụng Tor)
- Không lưu giữ tài sản (bạn vẫn giữ quyền kiểm soát tiền của mình)
- Mã nguồn mở (AGPL)


### Sự khác biệt với Bisq 1


**Dành cho người mua:**




- Không yêu cầu đặt cọc
- Không có phí giao dịch
- Không có phí mining
- Bảo mật dựa trên uy tín của nhà cung cấp
- Giới hạn giao dịch thấp hơn (tương đương 600 USD)


**Dành cho người bán:**




- Không yêu cầu đặt cọc bảo đảm
- Xây dựng danh tiếng
- Khả năng đốt cháy BSQ hoặc tạo ra các liên kết BSQ
- Mức giá bán tiềm năng cao hơn (cao hơn thị trường từ 10-15%)


**Lưu ý quan trọng:** Sau khi giao thức Bisq Multisig được triển khai trong Bisq 2, phiên bản cũ của Bisq có thể được loại bỏ dần. Tuy nhiên, Bisq 1 sẽ tiếp tục được sử dụng như một công cụ quản lý cho Bisq CAD và cho các trao đổi BSQ-BTC.


### Quy trình Exchange




- Người đưa ra lời đề nghị sẽ xác định các điều khoản trao đổi
- Sau khi các bên giao dịch đạt được thỏa thuận về các điều khoản (phương thức thanh toán và giá cả), giao dịch bắt đầu
- Người bán gửi thông tin tài khoản ngân hàng của mình cho người mua, và người mua gửi địa chỉ Bitcoin của mình cho người bán
- Người mua thanh toán bằng tiền tệ pháp định và thông báo cho người bán
- Sau khi nhận được thanh toán, người bán sẽ gửi bitcoin đến địa chỉ của người mua
- Giao dịch hoàn tất khi người mua nhận được bitcoin


### Những quy tắc quan trọng




- Trước khi trao đổi thông tin thanh toán, giao dịch có thể bị hủy bỏ mà không cần lý do
- Sau khi các chi tiết đã được trao đổi, việc không thực hiện nghĩa vụ có thể dẫn đến việc bị trục xuất
- Đối với chuyển khoản ngân hàng, **tuyệt đối không sử dụng các thuật ngữ "Bisq" hoặc "Bitcoin"** trong lý do thanh toán (điều này có thể dẫn đến việc tiền bị đóng băng hoặc thậm chí khiến tài khoản ngân hàng của người nhận hoặc người trả tiền bị khóa)
- Các nhà giao dịch phải đăng nhập ít nhất một lần mỗi ngày để theo dõi quy trình
- Trong trường hợp phát sinh vấn đề, các nhà giao dịch có thể nhờ đến sự trợ giúp của người hòa giải


## Cài đặt và cấu hình


### 1. Tải xuống và xác minh Bisq 2


![Téléchargement de Bisq 2](assets/fr/01.webp)




- Truy cập [bisq.network](https://bisq.network/downloads/)
- Tải xuống phiên bản Bisq 2 tương ứng với hệ điều hành của bạn (cuộn xuống cuối trang)
- Hãy xác minh tính xác thực của tệp đã tải xuống (rất khuyến khích). Để được hướng dẫn chi tiết về xác minh chữ ký, hãy xem hướng dẫn sau:


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 2. Cài đặt theo hệ thống của bạn


Vui lòng làm theo các bước cài đặt phù hợp với hệ điều hành của bạn. Nếu gặp bất kỳ khó khăn nào trong quá trình cài đặt, bạn có thể tham khảo hướng dẫn chi tiết trên [wiki chính thức của Bisq](https://bisq.wiki/Downloading_and_installing).


### 3. Công ty khởi nghiệp đầu tiên




- Khởi chạy Bisq 2 và chấp nhận các điều khoản sử dụng


![Conditions d'utilisation](assets/fr/01.webp)




- Tạo hồ sơ mới bằng cách chọn tên và ảnh đại diện


![Création du profil](assets/fr/02.webp)




- Sau đó, bạn sẽ được chuyển đến trang tổng quan chính của ứng dụng, nơi bạn có thể khởi chạy Bisq để mua hoặc bán những đồng bitcoin đầu tiên của mình


![Page d'accueil de Bisq 2](assets/fr/03.webp)


### 4. Thiết lập phương thức thanh toán




- Truy cập mục tài khoản thanh toán từ menu chính


![Liste des comptes de paiement](assets/fr/04.webp)




- Thêm phương thức thanh toán mới bằng cách điền đầy đủ thông tin cần thiết


![Création d'un nouveau compte de paiement](assets/fr/05.webp)


Việc thiết lập trước các phương thức thanh toán là tùy chọn, nhưng được khuyến nghị để tiết kiệm thời gian khi giao dịch. Bạn cũng có thể thiết lập phương thức thanh toán trực tiếp trong quá trình giao dịch bằng cách liên hệ với đối tác sàn giao dịch của mình.


### 5. Bảo mật tài khoản


**Sao lưu dữ liệu:**


Không giống như Bisq 1, Bisq 2 hiện không tích hợp Bitcoin wallet: do đó, các giao dịch được thực hiện thông qua các wallet bên ngoài của riêng bạn. Tuy nhiên, chúng tôi khuyên bạn nên thường xuyên sao lưu thư mục dữ liệu Bisq 2 của mình. Để tìm vị trí thư mục dữ liệu, hãy tham khảo [wiki chính thức của Bisq](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).


**Quản lý danh tính:**


Bisq 2 cho phép bạn tạo nhiều danh tính. Mỗi danh tính có thể được sử dụng cho các loại giao dịch khác nhau. Các danh tính của bạn được lưu trữ trong thư mục dữ liệu.


## Mua bán Bitcoin


### Cách mua Bitcoin


**Phương án 1: Tận dụng ưu đãi hiện có**




- Trên màn hình chính, chọn "Bisq Easy", tab "Bắt đầu", sau đó nhấp vào "Bắt đầu trình hướng dẫn giao dịch"


![Lancer trade wizard](assets/fr/06.webp)




- Chọn "Mua Bitcoin" và chọn loại tiền tệ của bạn


![Sélection achat Bitcoin](assets/fr/07.webp)


![Choix de la devise](assets/fr/08.webp)




- Thiết lập các phương thức thanh toán ưa thích của bạn (SEPA, Revolut, v.v.)


![Configuration méthodes de paiement](assets/fr/09.webp)




- Đến bước này, hoặc bạn đã có danh sách các ưu đãi phù hợp với tiêu chí đã chọn trước đó, hoặc bạn cần truy cập vào "Sổ ưu đãi"


![Liste des offres](assets/fr/10.webp)




- Trong trường hợp thứ hai, bạn có thể hiển thị và lọc các ưu đãi bằng cách sử dụng các nút ở phía trên bên phải giao diện


![Filtres des offres](assets/fr/11.webp)




- Sau khi chọn được ưu đãi, bạn chỉ cần chọn phương thức thanh toán rồi xác nhận tóm tắt giao dịch


![Choix modalités de paiement](assets/fr/12.webp)


![Configuration du trade](assets/fr/13.webp)


![Récapitulatif du trade](assets/fr/14.webp)


**Phương án 2: Tự tạo ưu đãi của riêng bạn**




- Chọn "Bisq Easy" rồi chọn "Offerbook"
- Chọn cặp giao dịch của bạn (ví dụ: BTC/EUR)
- Nhấp vào "Tạo ưu đãi"
- Hãy làm theo hướng dẫn của trình tạo đề nghị: Xác định số tiền (cố định hoặc theo khoảng)


![Configuration du montant](assets/fr/20.webp)




- Chọn phương thức thanh toán được chấp nhận


![Sélection méthodes de paiement](assets/fr/21.webp)




  - Kiểm tra bản tóm tắt và đăng tải ưu đãi


![Récapitulatif et publication](assets/fr/22.webp)


Sau khi quá trình trao đổi được bắt đầu:




- Gửi địa chỉ Bitcoin hoặc hóa đơn Lightning của bạn cho người bán


![Envoi adresse Bitcoin](assets/fr/15.webp)




- Nhận thông tin tài khoản ngân hàng của người bán


![Réception coordonnées bancaires](assets/fr/16.webp)


![Détails coordonnées bancaires](assets/fr/17.webp)




- Thực hiện thanh toán (không đề cập đến "Bisq" hoặc "Bitcoin")
- Thông báo cho người bán về khoản thanh toán của bạn


![Notification paiement](assets/fr/18.webp)




- Chờ Bitcoin đến


![Attente réception](assets/fr/19.webp)


### Làm thế nào để bán Bitcoin?


Quá trình bán hàng trên Bisq 2 diễn ra tương tự như quá trình mua hàng, với các bước chính giống nhau nhưng theo thứ tự ngược lại. Bạn có thể tạo lời chào bán của riêng mình hoặc phản hồi lại lời chào mua hiện có. Dưới đây là phân tích chi tiết các tùy chọn và giai đoạn khác nhau trong quá trình này:


**Phương án 1: Tạo đề nghị bán hàng**




- Chọn "Bisq Easy" rồi chọn "Offerbook"
- Nhấp vào "Tạo đề nghị" và chọn "Bán Bitcoin"
- Tùy chỉnh ưu đãi của bạn:
 - Chọn loại tiền tệ (EUR, USD, v.v.)
 - Chọn phương thức thanh toán được chấp nhận
 - Chọn số tiền (tương đương từ 6 đến 600 USD)
 - Đặt giá bán (cố định hoặc theo phần trăm thị trường)
- Kiểm tra chi tiết và đăng tải ưu đãi


**Phương án 2: Chấp nhận lời đề nghị hiện có**




- Xem các ưu đãi trong tab "Sổ ưu đãi"
- Lọc theo loại tiền tệ và phương thức thanh toán
- Hãy chọn ưu đãi phù hợp với bạn
- Kiểm tra chi tiết và chấp nhận lời đề nghị


**Quy trình bán hàng:**


Sau khi quá trình trao đổi được bắt đầu:




   - Gửi thông tin tài khoản ngân hàng của bạn cho người mua
   - Chờ địa chỉ Bitcoin của người mua
   - Hãy kiểm tra xem địa chỉ có hợp lệ hay không


Sau khi nhận được thông báo thanh toán:




   - Hãy kiểm tra xem khoản thanh toán đã được nhận vào tài khoản của bạn chưa
   - Xác nhận số tiền và thông tin chi tiết khớp nhau
   - Gửi bitcoin đến địa chỉ được cung cấp
   - Đánh dấu giao dịch là đã hoàn tất


Hoàn thiện:




   - Chờ xác nhận từ người mua
   - Hãy để lại phản hồi về giao dịch
   - Xây dựng danh tiếng của bạn để phục vụ cho các giao dịch bán hàng trong tương lai


**Lưu ý quan trọng:** Là người bán, bạn cần đặc biệt cảnh giác với rủi ro bị hoàn tiền. Hãy ưu tiên các phương thức thanh toán an toàn và luôn kiểm tra xem người nhận đã nhận được tiền trước khi gửi bitcoin.


## Thực hành tốt và an toàn


### Mẹo an toàn


**Dành cho người mua:**




- Hãy bắt đầu với số lượng nhỏ
- Kiểm tra uy tín của người bán (điểm tối thiểu 30.000)
- Chỉ sử dụng các phương thức thanh toán được đề xuất
- Hãy kiểm tra xem người bán có đang hoạt động hay không trước khi gửi thanh toán
- Chỉ sử dụng thông tin tài khoản ngân hàng được cung cấp trong cuộc trò chuyện trao đổi
- Tuyệt đối không liên lạc bên ngoài nền tảng Bisq 2
- Hãy giữ lại bằng chứng thanh toán
- Tuyệt đối không gửi thông tin nhạy cảm


**Dành cho người bán:**




- Hãy cẩn thận với các tài khoản mới
- Tránh sử dụng các phương thức thanh toán dễ bị hoàn tiền (PayPal, Venmo)
- Kiểm tra xem thông tin tài khoản có khớp với người mua hay không
- Giới hạn liên lạc qua kênh chat Bisq 2
- Nếu có thắc mắc, hãy mở một cuộc hòa giải


### Xây dựng danh tiếng (cho nhân viên bán hàng)


Để nâng cao uy tín của bạn trên Bisq với tư cách là người bán, hãy thực hiện giao dịch thường xuyên và duy trì giao tiếp chuyên nghiệp với người mua. Phản hồi nhanh chóng các yêu cầu của người mua để đảm bảo trải nghiệm tích cực. Bạn cũng có thể tạo tài khoản BSQ để thể hiện cam kết của mình với nền tảng. Những hành động này sẽ xây dựng lòng tin và thu hút thêm nhiều người mua.


### Giải quyết tranh chấp




- Liên hệ với đối tác của bạn qua trò chuyện
- Nếu cần thiết, hãy mở tranh chấp
- Cung cấp tất cả các bằng chứng được yêu cầu
- Hãy làm theo hướng dẫn của người hòa giải


### Chính sách bảo mật:




- Không cần đăng ký hoặc xác minh danh tính tập trung
- Tất cả các kết nối đều đi qua mạng Tor (và sắp tới là I2P)
- Không có máy chủ trung tâm để lưu trữ dữ liệu
- Chi tiết giao dịch chỉ có thể được đọc bởi các bên liên quan


### Bảo vệ chống lại sự kiểm duyệt:




- Mạng P2P được phân phối hoàn toàn
- Sử dụng mạng Tor (và sắp tới là I2P) để chống lại kiểm duyệt
- Dự án mã nguồn mở được quản lý bởi một DAO, không có thực thể pháp lý tập trung


## Ưu điểm và nhược điểm


### Lợi ích của Bisq 2




- Bảo mật tối đa**: Không yêu cầu xác minh danh tính (KYC), sử dụng Tor
- Phân quyền**: Không có máy chủ trung tâm
- Bảo mật**: Mã nguồn mở, không lưu trữ
- Giao diện trực quan**: đơn giản hơn Bisq 1
- Tính linh hoạt**: Nhiều giao thức trao đổi


### Nhược điểm của Bisq 2




- Thanh khoản hạn chế** (hiện tại):
 - Giao thức mới đang trong giai đoạn khởi động
 - Hiện chỉ còn một vài ưu đãi bán hàng
 - Có thể phải chờ đợi khá lâu để tìm được người mua
- Giới hạn giao dịch**: Tối đa 600 USD mỗi giao dịch (với Bisq easy)
- Chỉ dành cho máy tính để bàn**: Không có ứng dụng di động


## Các giao thức tương lai


Mặc dù Bisq Easy hiện là giao thức duy nhất có sẵn, nhưng một số giao thức khác đang được phát triển cho Bisq 2:




- Bisq Lightning**: Giao thức Exchange dựa trên hệ thống ký quỹ sử dụng mật mã tính toán đa bên trên mạng Lightning.
- Bisq MuSig**: Di chuyển giao thức chính từ Bisq 1 sang Bisq 2, sử dụng multisig 2-on-2 với các khoản tiền đặt cọc bảo đảm.
- Trao đổi BSQ**: Trao đổi nguyên tử tức thì giữa BSQ và BTC.
- Liquid Swaps**: Exchange tài sản trên mạng Liquid (USDT, BTC-L) thông qua giao dịch hoán đổi nguyên tử.
- Giao dịch hoán đổi Monero**: Giao dịch nguyên tử giữa Bitcoin và Monero.
- Liquid MuSig**: Phiên bản của giao thức multisig sử dụng L-BTC để giảm chi phí và tăng cường tính bảo mật.
- Trao đổi tàu ngầm**: Exchange giữa Bitcoin trên mạng Lightning và Bitcoin on-chain.
- Trao đổi Stablecoin**: Giao dịch nguyên tử giữa stablecoin Bitcoin và USD.
- Tùy chọn Multisig**: Tạo các tùy chọn mua và bán P2P với việc chặn BTC trong giao dịch on-chain multisig.
- Multisig Mở Contracts**: Cho phép tạo các hợp đồng có điều kiện tùy chỉnh bằng cách sử dụng hệ thống multisig 2 trên 3 với cơ chế chênh lệch giá.


Các giao thức này hiện đang được phát triển và sẽ được tích hợp dần vào Bisq 2, mang lại sự linh hoạt hơn cho người dùng tùy theo nhu cầu cụ thể của họ.


## Tài nguyên hữu ích




- Trang web chính thức: [bisq.network](https://bisq.network)
- Tài liệu tham khảo: [Bisq Wiki](https://bisq.wiki)
- Hỗ trợ: [Diễn đàn Bisq](https://bisq.community)
- Mã nguồn: [GitHub](https://github.com/bisq-network)