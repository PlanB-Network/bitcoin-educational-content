---
name: Ashigaru
description: fork từ Samourai Wallet để bảo mật, quản lý và trộn bitcoin của bạn
---

![cover](assets/cover.webp)



Ashigaru là ứng dụng di động Bitcoin wallet, tiếp nối dự án Samourai Wallet, nhưng ở một hình thức mới. Phần mềm này ra đời trong một bối cảnh đặc biệt: vào tháng 4 năm 2024, những người sáng lập Samourai Wallet đã bị chính quyền Mỹ bắt giữ và máy chủ của họ bị tịch thu. Mặc dù ứng dụng Samurai vẫn có thể sử dụng được, nhưng hiện tại nó không còn được duy trì nữa. Ashigaru là phiên bản fork miễn phí của Samurai Wallet, được duy trì bởi một nhóm ẩn danh để đảm bảo tính liên tục của chức năng Samurai và bảo vệ triết lý ban đầu của nó: bảo vệ quyền riêng tư và chủ quyền của người dùng Bitcoin.



Ashigaru kế thừa phần lớn DNA của Samourai: giao diện tương tự, cách tiếp cận tự quản lý rõ ràng, mã nguồn mở và tập trung vào quyền riêng tư. Mã nguồn được phân phối theo giấy phép GNU GPLv3, đảm bảo rằng bất kỳ ai cũng có thể kiểm tra, sửa đổi hoặc phân phối lại phần mềm.



Ứng dụng Ashigaru tích hợp một bộ công cụ tiên tiến để bảo mật và quản lý UTXO của bạn:




- Whirlpool**, một giao thức coinjoin dựa trên Zerolink, cho phép bạn phá vỡ các liên kết xác định giữa các giao dịch vào và ra mà không mất quyền kiểm soát đối với tiền của mình.
- PayNym**, triển khai mã thanh toán có thể tái sử dụng (BIP47), hiện được thể hiện thông qua hệ thống hình đại diện "*Pepehash*".
- Ricochet**, một tính năng bổ sung các bước nhảy trung gian vào các giao dịch để khiến việc theo dõi trở nên khó khăn hơn.
- Và tất nhiên là ***Coin Control*** để lựa chọn, đóng băng và dán nhãn UTXO của bạn một cách chính xác.
- Chi tiêu theo đợt***, để giảm chi phí bằng cách nhóm nhiều khoản thanh toán vào một giao dịch duy nhất.
- **Chế độ ẩn**, ẩn ứng dụng trên điện thoại di động của bạn sau một trình khởi chạy giả để không bị phát hiện trong quá trình kiểm tra thực tế điện thoại.
- Các công cụ chi tiêu tiên tiến giúp tối ưu hóa tính bảo mật của bạn (payjoin, stonewall...).
- Hệ thống phục hồi được tối ưu hóa bằng cách sử dụng mật khẩu BIP39.
- Một hệ thống tự động tối ưu hóa lựa chọn phí giao dịch.



![Image](assets/fr/01.webp)



Do đó, Ashigaru hướng đến những người dùng nhận thức được các vấn đề liên quan đến khả năng truy xuất giao dịch trên Bitcoin. Cho dù bạn là người dùng quan tâm đến quyền riêng tư, một người dùng Bitcoin dày dạn kinh nghiệm cam kết tự quản lý tài sản, hay một cá nhân phải đối mặt với rủi ro bị giám sát chặt chẽ, ứng dụng wallet này sẽ cung cấp cho bạn những công cụ cần thiết để lấy lại quyền kiểm soát hoạt động của mình trên Bitcoin.



Ashigaru có sẵn phiên bản di động thông qua ứng dụng, chúng ta sẽ tìm hiểu trong hướng dẫn này. Tuy nhiên, bạn cũng có thể sử dụng Ashigaru trên máy tính với ***Ashigaru Terminal***, chúng tôi sẽ giới thiệu trong hướng dẫn sau.



![Image](assets/fr/02.webp)



Trong hướng dẫn này, tôi muốn giới thiệu cho bạn cách sử dụng Ashigaru cơ bản: cài đặt, kết nối với Dojo, sao lưu, nhận và gửi bitcoin. Các công cụ nâng cao sẽ được trình bày trong các hướng dẫn chuyên sâu khác.



## 1. Điều kiện tiên quyết để tham gia Ashigaru



Ứng dụng này yêu cầu một số điều kiện tiên quyết để hoạt động bình thường. Trước hết, đây không phải là ứng dụng có sẵn trên các cửa hàng truyền thống như Google Play Store hay App Store. Ứng dụng chỉ được cài đặt thủ công trên điện thoại của bạn từ tệp `.apk`, có thể tải xuống qua mạng Tor. Vì vậy, nếu bạn đang sử dụng iPhone, phương pháp này sẽ không hiệu quả: bạn sẽ cần một thiết bị Android.



Để tải xuống tệp `.apk` qua Tor, bạn cần một trình duyệt có khả năng truy cập các trang web `.onion`. Cách dễ nhất là cài đặt ứng dụng Tor Browser trên điện thoại, có sẵn từ [Cửa hàng Google Play](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) hoặc trực tiếp [thông qua tệp `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



Hầu hết các điện thoại thông minh mới nhất đều mặc định chặn cài đặt ứng dụng từ các nguồn không xác định. Bạn cần tạm thời kích hoạt tùy chọn này cho Tor Browser trong cài đặt thiết bị để cho phép cài đặt. Sau khi ứng dụng được cài đặt, hãy nhớ tắt chức năng này để tăng cường bảo mật cho điện thoại của bạn.



Một điều kiện tiên quyết thiết yếu khác để sử dụng Ashigaru là một node Bitcoin Dojo. Vì lý do bảo mật và quyền sở hữu, đội ngũ Ashigaru không duy trì một máy chủ tập trung để kết nối ứng dụng của bạn. Vì vậy, bạn sẽ cần chạy phiên bản Dojo của riêng mình hoặc kết nối với một phiên bản đáng tin cậy.



Dojo cho phép ứng dụng Ashigaru của bạn tham khảo thông tin blockchain, xem số dư địa chỉ và phát sóng các giao dịch của bạn trên mạng Bitcoin.



Để tìm hiểu thêm về Dojo và cách cài đặt, tôi mời bạn làm theo hướng dẫn chuyên sâu này:



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Nếu bạn thực sự không đủ khả năng để tự vận hành Dojo, bạn có thể tìm những người sẵn sàng chia sẻ phiên bản Dojo của họ miễn phí tại [dojobay.pw](https://www.dojobay.pw/mainnet/). Đây có thể là giải pháp tạm thời, nhưng về lâu dài, tôi khuyên bạn nên sử dụng Dojo của riêng mình để đảm bảo chủ quyền và tính bảo mật.



## 2. Kiểm tra và cài đặt ứng dụng Ashigaru



### 2.1. Tải ứng dụng Ashigaru



Trên điện thoại, hãy mở Tor Browser và truy cập [trang web chính thức của Ashigaru] (https://ashigaru.rs/download/), trong mục `Tải xuống`. Sau đó, nhấp vào nút `Tải xuống cho Android` để tải xuống tệp cài đặt.



![Image](assets/fr/04.webp)



Trước khi cài đặt ứng dụng trên thiết bị của bạn, chúng tôi sẽ kiểm tra tính xác thực và toàn vẹn của ứng dụng. Đây là một bước rất quan trọng, đặc biệt khi cài đặt ứng dụng trực tiếp từ tệp `.apk'.



### 2.2. Kiểm tra ứng dụng Ashigaru



Quay lại [trang web chính thức của Ashigaru](https://ashigaru.rs/download/) trong mục `Tải xuống`, sau đó sao chép thông báo hiển thị dưới tiêu đề `SHA-256 Hash của tệp APK`. Sao chép toàn bộ khối, từ `BEGIN PGP SIGNED MESSAGE` đến `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Vẫn trên điện thoại, hãy mở một tab mới trong Tor Browser và truy cập [công cụ xác minh Keybase](https://keybase.io/verify). Dán thông báo bạn vừa sao chép vào trường được cung cấp, sau đó nhấp vào nút `Xác minh`.



![Image](assets/fr/06.webp)



Nếu chữ ký là thật, Keybase sẽ hiển thị thông báo xác nhận tệp đã được các nhà phát triển Ashigaru ký. Bạn cũng có thể nhấp vào hồ sơ `ashigarudev` do Keybase chỉ định và kiểm tra xem dấu vân tay khóa của họ có khớp chính xác với: `A138 06B1 FA2A 676B` hay không.



Tuy nhiên, nếu lỗi xuất hiện ở giai đoạn này, điều đó có nghĩa là chữ ký không hợp lệ. Trong trường hợp này, **không cài đặt APK**. Hãy bắt đầu lại từ đầu hoặc nhờ cộng đồng hỗ trợ trước khi tiếp tục.



![Image](assets/fr/07.webp)



Keybase đã cung cấp cho bạn mã băm của ứng dụng. Bây giờ, chúng tôi sẽ kiểm tra xem mã băm của tệp `.apk` bạn đã tải xuống có khớp với mã băm đã được xác minh trên Keybase hay không. Để thực hiện việc này, hãy truy cập [TỆP BĂM TRỰC TUYẾN](https://hash-file.online/).



![Image](assets/fr/08.webp)



Nhấp vào nút `BROWSE...` và chọn tệp `.apk` đã tải xuống ở bước 2.1.


Sau đó chọn hàm băm `SHA-256` và nhấp vào `CALCULATE HASH` để tính toán hàm băm của tệp của bạn.



![Image](assets/fr/09.webp)



Trang web sẽ hiển thị mã băm của tệp `.apk` của bạn. Hãy so sánh với mã băm bạn đã xác minh trên Keybase.io. Nếu hai mã băm giống hệt nhau, quá trình kiểm tra tính xác thực và tính toàn vẹn đã thành công. Bây giờ bạn có thể tiến hành cài đặt ứng dụng.



![Image](assets/fr/10.webp)



### 2.3. Cài đặt ứng dụng Ashigaru



Để cài đặt ứng dụng, hãy mở trình quản lý tệp trên điện thoại và vào thư mục tải xuống. Sau đó, nhấp vào tệp `.apk` bạn vừa chọn và xác nhận cài đặt khi được nhắc.



![Image](assets/fr/11.webp)



Ashigaru hiện đã được cài đặt trên điện thoại của bạn.



## 3. Khởi tạo ứng dụng và tạo danh mục đầu tư Bitcoin



Khi khởi chạy ứng dụng lần đầu tiên, hãy chọn `MAINNET`.



![Image](assets/fr/12.webp)



Sau đó nhấp vào `Bắt đầu`.



![Image](assets/fr/13.webp)



Bây giờ chúng ta sẽ tạo một danh mục đầu tư Bitcoin mới. Nhấn nút `Tạo danh mục đầu tư wallet mới`.



![Image](assets/fr/14.webp)



### 3.1. tạo danh mục đầu tư Bitcoin



Ashigaru cần passphrase BIP39. Chọn passphrase của bạn và nhập vào các ô tương ứng. passphrase phải càng dài và càng ngẫu nhiên càng tốt để chống lại tấn công brute-force.



Hãy sao lưu vật lý ngay lập tức passphrase này. Đây là một bước rất quan trọng: nếu bạn mất điện thoại, **nếu bạn không còn passphrase này nữa, bạn sẽ không thể truy cập vào số bitcoin** được lưu trữ trong Ashigaru wallet của mình nữa. Chính passphrase này cũng được sử dụng để mã hóa tệp khôi phục wallet.



Nếu bạn chưa biết passphrase là gì hoặc chưa hiểu rõ cách thức hoạt động của nó, tôi thực sự khuyên bạn nên đọc hướng dẫn bổ sung này. Điều này rất quan trọng, vì passphrase là một yếu tố quan trọng trong bảo mật của bạn: việc sử dụng sai cách có thể dẫn đến mất tiền vĩnh viễn.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sau khi nhập passphrase, hãy nhấp vào `TIẾP THEO`.



![Image](assets/fr/15.webp)



Sau đó, hãy chọn mã PIN. Mã này sẽ được sử dụng để mở khóa Ashigaru wallet của bạn, bảo vệ nó khỏi sự truy cập vật lý trái phép. Mã này không liên quan đến việc giải mã khóa wallet của bạn. Điều này có nghĩa là, ngay cả khi không biết mã PIN, bất kỳ ai có cụm từ ghi nhớ và passphrase của bạn đều có thể lấy lại quyền truy cập vào bitcoin của bạn.



Chọn mã PIN dài và ngẫu nhiên. Nhớ giữ một bản sao lưu ở một nơi riêng biệt với điện thoại để tránh việc chúng bị xâm phạm cùng lúc.



![Image](assets/fr/16.webp)



Sau khi mã PIN được tạo, Ashigaru sẽ hiển thị cụm từ ghi nhớ của wallet. Cảnh báo: cụm từ này, kết hợp với passphrase, sẽ cho phép bạn truy cập đầy đủ vào bitcoin của mình. Bất kỳ ai nắm giữ nó đều có thể chiếm đoạt tiền của bạn, ngay cả khi họ không có quyền truy cập vào điện thoại của bạn. Chuỗi 12 từ này có thể được sử dụng để khôi phục wallet của bạn trong trường hợp điện thoại bị mất, bị đánh cắp hoặc bị hỏng. Do đó, điều quan trọng là phải lưu trữ nó thật cẩn thận trên một phương tiện vật lý (giấy hoặc kim loại).



Tuyệt đối không lưu cụm từ này dưới dạng kỹ thuật số, nếu không bạn có nguy cơ bị đánh cắp tiền. Tùy thuộc vào chiến lược bảo mật của mình, bạn có thể tạo nhiều bản sao vật lý, nhưng đừng bao giờ chia nhỏ chúng. Hãy giữ các từ theo đúng thứ tự và đảm bảo chúng được đánh số.



Cuối cùng, đừng bao giờ lưu mã ghi nhớ và passphrase ở cùng một nơi. Nếu cả hai bị xâm nhập cùng lúc, kẻ tấn công có thể truy cập vào wallet của bạn.



![Image](assets/fr/17.webp)



Để tìm hiểu thêm về cách bảo mật cụm từ ghi nhớ của bạn, vui lòng tham khảo hướng dẫn bổ sung này:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sau đó, Ashigaru yêu cầu bạn xác nhận lại passphrase của mình. Hãy tận dụng cơ hội này để kiểm tra xem bản sao lưu vật lý của bạn đã chính xác chưa.



![Image](assets/fr/18.webp)



### 3.2. kết nối một võ đường



Tiếp theo là bước kết nối với Dojo của bạn. Như đã giải thích trong phần giới thiệu, Ashigaru phải được kết nối với Dojo để tương tác với mạng Bitcoin.



Đăng nhập vào "Công cụ bảo trì" của Dojo và mở menu `PAIRING`.



![Image](assets/fr/19.webp)



Trên Ashigaru, nhấn nút `Quét QR`, sau đó quét mã QR kết nối được hiển thị bởi DMT của bạn. Sau đó, nhấp vào `Tiếp tục` để xác nhận.



![Image](assets/fr/20.webp)



Nhập mã PIN của bạn để mở khóa wallet. Thao tác này sẽ đưa bạn đến trang đồng bộ hóa. Việc hiển thị lỗi *PayNym* ở giai đoạn này là bình thường, vì wallet là thiết bị mới. Chỉ cần nhấp vào `Tiếp tục`.



![Image](assets/fr/21.webp)



Sau đó, bạn sẽ được đưa đến trang chủ của danh mục đầu tư của mình.



![Image](assets/fr/22.webp)



Trước khi tiếp tục, tôi khuyên bạn nên thực hiện khôi phục thử nghiệm khi wallet vẫn chưa chứa bitcoin. Điều này sẽ cho phép bạn kiểm tra xem các bản sao lưu giấy của mình có hoạt động bình thường hay không. Để tìm hiểu cách thực hiện, hãy làm theo hướng dẫn này:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Thiết lập ứng dụng Ashigaru



Để truy cập cài đặt ứng dụng, hãy nhấp vào hình ảnh *PayNym* của bạn ở góc trên bên trái, sau đó chọn `Cài đặt`.



![Image](assets/fr/23.webp)



Tại đây, bạn sẽ tìm thấy một số tùy chọn để điều chỉnh hoạt động của Ashigaru cho phù hợp với nhu cầu của mình. Tuy nhiên, tôi thực sự khuyên bạn nên kích hoạt 2 thông số quan trọng ngay từ đầu.



Bắt đầu bằng cách mở menu `Bảo mật > Chế độ ẩn`, sau đó kích hoạt tính năng này nếu cần. Tính năng này sẽ ẩn ứng dụng Ashigaru sau tên, logo và giao diện của một ứng dụng thông thường được cài đặt trên điện thoại của bạn. Mục đích là để ngăn chặn bất kỳ ai nhận dạng Ashigaru trong trường hợp kiểm tra thực tế điện thoại của bạn.



![Image](assets/fr/24.webp)



Mỗi ứng dụng giả mạo đều có một phương pháp riêng để mở khóa giao diện Ashigaru thật. Ví dụ: nếu bạn chọn máy tính, ứng dụng Ashigaru sẽ biến mất khỏi màn hình chính và được thay thế bằng một máy tính giả. Khi mở ứng dụng, bạn sẽ thấy giao diện máy tính cổ điển, nhưng để truy cập Ashigaru, bạn chỉ cần nhấn nhanh biểu tượng `=` năm lần.



Tham số quan trọng thứ hai cần kích hoạt là [**RBF** (*Thay thế bằng Phí*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Tùy chọn này cho phép bạn tăng chi phí của một giao dịch nếu nó bị kẹt trong mempool do chi phí quá thấp. Bạn có thể kích hoạt tùy chọn này thông qua menu `Giao dịch > Chi tiêu bằng RBF`.



![Image](assets/fr/25.webp)



Mẹo: Bạn có thể thay đổi đơn vị hiển thị danh mục đầu tư của mình từ `BTC` sang `sat` chỉ bằng cách nhấp vào tổng số dư hiển thị trên trang chủ.



## 5. Nhận bitcoin trên Ashigaru



Bây giờ danh mục đầu tư của bạn đã hoạt động, bạn có thể nhận satss. Để thực hiện, hãy nhấn nút `+` ở góc dưới bên phải giao diện, sau đó nhấn nút `Nhận` màu xanh lá cây.



![Image](assets/fr/26.webp)



Ashigaru sau đó sẽ hiển thị cho bạn địa chỉ nhận chưa sử dụng đầu tiên trong wallet của bạn, nhằm ngăn chặn việc tái sử dụng địa chỉ (việc tái sử dụng địa chỉ là một hành vi rất không tốt cho quyền riêng tư của bạn). Sau đó, bạn có thể chuyển tiếp địa chỉ này cho người hoặc dịch vụ cần gửi bitcoin cho bạn.



![Image](assets/fr/27.webp)



Sau khi giao dịch được phát trên mạng, nó sẽ tự động xuất hiện trên trang chủ của ứng dụng.



![Image](assets/fr/28.webp)



## 6. Gửi bitcoin với Ashigaru



Bây giờ bạn đã có bitcoin trong ví Ashigaru wallet, bạn cũng có thể gửi chúng. Để thực hiện, hãy nhấn nút `+` ở góc dưới bên phải, sau đó chọn nút `Gửi` màu đỏ.



![Image](assets/fr/29.webp)



Sau đó, hãy chọn tài khoản bạn muốn sử dụng để chi tiêu. Hiện tại, chúng ta chưa đề cập đến tài khoản `Postmix`, dành riêng cho coinjoins, mà chúng ta sẽ xem xét trong bài hướng dẫn sau. Vì vậy, chúng ta sẽ gửi tiền từ tài khoản tiền gửi chính.



![Image](assets/fr/30.webp)



Nhập thông tin giao dịch của bạn: số tiền cần gửi và địa chỉ Bitcoin của người nhận.



![Image](assets/fr/31.webp)



Bằng cách nhấp vào ba dấu chấm nhỏ ở góc trên bên phải, sau đó nhấp vào `Hiển thị đầu ra chưa sử dụng`, bạn cũng có thể chọn chính xác UTXO nào bạn muốn sử dụng để tăng cường quyền riêng tư.



![Image](assets/fr/32.webp)



Sau khi điền đầy đủ thông tin, hãy nhấp vào mũi tên màu trắng ở cuối giao diện để tiếp tục.



Sau đó, bạn sẽ được chuyển đến trang tóm tắt hiển thị tất cả thông tin chi tiết về giao dịch của bạn. Một số yếu tố quan trọng được hiển thị:




- Trong khối `Destination`, hãy kiểm tra lại lần cuối xem địa chỉ người nhận và số tiền đã gửi có chính xác không;
- Trong khối `Phí`, bạn có thể xem mức phí do Ashigaru tự động chọn và nếu cần, có thể sửa đổi bằng cách nhấp vào `QUẢN LÝ`;
- Khối `Giao dịch` cho biết loại giao dịch bạn sắp thực hiện. Ở đây, chúng ta đang nói về một giao dịch đơn giản, nhưng Ashigaru cũng hỗ trợ các loại giao dịch khác được tối ưu hóa quyền riêng tư, mà chúng tôi sẽ đề cập chi tiết trong một bài hướng dẫn sau;
- Khối `Cảnh báo Giao dịch` màu đỏ sẽ cảnh báo bạn nếu giao dịch của bạn xuất hiện các mẫu có thể bị các công cụ phân tích chuỗi nhận dạng và có thể xâm phạm quyền riêng tư của bạn. Nhấp vào khối này, bạn có thể xem chi tiết. Ví dụ: trong trường hợp của tôi, Ashigaru cho tôi biết số tiền được gửi là số tròn (`3000 sats`), cho phép tôi suy ra kết quả nào tương ứng với chi phí và kết quả nào là tỷ giá hối đoái. Để tìm hiểu thêm về các phương pháp phân tích chuỗi này, tôi mời bạn tham gia khóa đào tạo BTC 204 của tôi trên Plan ₿ Academy;
- Cuối cùng, bạn có thể thêm nhãn vào giao dịch để lưu lại mục đích của giao dịch.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Sau khi kiểm tra tất cả thông tin, hãy sử dụng mũi tên màu xanh lá cây để gửi bitcoin. Giữ mũi tên, sau đó kéo sang phải để xác nhận tải lên.



![Image](assets/fr/33.webp)



Giao dịch của bạn đã được phát trên mạng Bitcoin.



![Image](assets/fr/34.webp)



## 7. Phục hồi Ashigaru wallet của bạn



Việc khôi phục ví Ashigaru wallet hơi khác so với ví Bitcoin cổ điển, vì ứng dụng này sử dụng cùng phương pháp với ví Samurai Wallet. Nếu bạn mất quyền truy cập vào ví wallet (do quên mã PIN, gỡ cài đặt hoặc làm mất điện thoại), có một số cách để khôi phục bitcoin của bạn.



Nếu bạn vẫn có thể truy cập điện thoại, hoặc nếu bạn đã sao lưu tệp này, phương pháp đơn giản nhất là sử dụng tệp sao lưu `ashigaru.txt`. Tệp này chứa tất cả thông tin bạn cần để khôi phục danh mục đầu tư trên phiên bản Ashigaru mới (hoặc trên Sparrow Wallet), nhưng nó được mã hóa bằng passphrase mà bạn đã xác định ở bước 3.1 của hướng dẫn này. Do đó, bạn phải có cả tệp `ashigaru.txt` và passphrase để sử dụng phương pháp này.



Với hai yếu tố này, bạn có thể khôi phục danh mục đầu tư của mình trên Sparrow Wallet chẳng hạn.



![Image](assets/fr/35.webp)



Nếu bạn không có quyền truy cập vào tệp `ashigaru.txt`, bạn vẫn có thể lấy lại quyền truy cập vào tiền của mình bằng cách sử dụng cụm từ ghi nhớ passphrase, giống như bạn làm với bất kỳ danh mục đầu tư Bitcoin nào khác. Tôi khuyên bạn nên thực hiện việc khôi phục này trên một phiên bản Ashigaru mới hoặc trực tiếp trên Sparrow Wallet để dễ dàng khôi phục các đường dẫn bỏ qua từ Whirlpool nếu bạn đã sử dụng nó. Ngoài ra, bạn có thể nhập thông tin này vào bất kỳ phần mềm nào khác tương thích với BIP39 bằng cách nhập thủ công các đường dẫn dẫn xuất.



Để biết thêm thông tin về quy trình này, vui lòng tham khảo hướng dẫn đầy đủ tôi đã viết về cách phục hồi Wallet Samurai wallet. Vì Ashigaru là fork, quy trình cũng giống hệt nhau:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Như bạn thấy, dù bạn sử dụng phương pháp khôi phục nào, passphrase vẫn là thiết bị không thể thiếu. Vì vậy, hãy đảm bảo sao lưu dữ liệu cẩn thận. Bạn cũng có thể tạo nhiều bản sao, tùy thuộc vào chiến lược bảo mật của mình.



## 8. Cập nhật ứng dụng



Để cập nhật ứng dụng Ashigaru, vì bạn đã cài đặt ứng dụng này từ tệp `.apk` chứ không phải qua Play Store như một ứng dụng thông thường, nên bạn sẽ cần tải xuống tệp `.apk` mới tương ứng với phiên bản đã cập nhật, sau đó cài đặt thủ công.



Lặp lại các bước được mô tả trong phần 2 của hướng dẫn này, ngoại trừ việc khi bạn nhấp vào tệp `.apk` để khởi chạy cài đặt, **điện thoại Android của bạn sẽ cung cấp cho bạn tùy chọn `Cập nhật`, không phải `Cài đặt`**.



![Image](assets/fr/41.webp)



Đây là một điểm rất quan trọng: nếu Android hiển thị `Cài đặt` thay vì `Cập nhật`, có thể bạn đang cài đặt phiên bản giả mạo. Trong trường hợp này, hãy dừng quá trình cài đặt ngay lập tức.



Tương tự như lần cài đặt đầu tiên, vui lòng kiểm tra tính xác thực và toàn vẹn của tệp `.apk` trước khi tiến hành cập nhật.



Để biết khi nào có phiên bản mới, hãy thường xuyên kiểm tra trang web chính thức của Ashigaru. Hãy yên tâm, Ashigaru là một ứng dụng ổn định, hoàn thiện, kế thừa từ Samourai Wallet, và các bản cập nhật tương đối ít thường xuyên so với các phần mềm mới hơn.



## 9. Quyên góp cho dự án Ashigaru



Ashigaru là một dự án mã nguồn mở. Nếu bạn muốn hỗ trợ phát triển dự án, bạn có thể quyên góp trực tiếp từ ứng dụng thông qua PayNym.



Để thực hiện việc này, hãy nhấp vào PayNym của bạn ở góc trên bên phải của giao diện, sau đó chọn mã thanh toán bắt đầu bằng `PM...`.



![Image](assets/fr/36.webp)



Sau đó nhấn nút `+` ở góc dưới bên phải màn hình.



![Image](assets/fr/37.webp)



Chọn `Ashigaru Open Source Project` làm người nhận.



![Image](assets/fr/38.webp)



Nhấp vào nút `KẾT NỐI` để thiết lập kênh truyền thông BIP47 (thông tin thêm về giao thức này trong phần hướng dẫn bên dưới).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Sau khi giao dịch thông báo được xác nhận, bạn có thể gửi tiền quyên góp cho dự án bằng cách nhấp vào mũi tên nhỏ màu trắng ở góc trên bên phải của giao diện.



![Image](assets/fr/40.webp)



Bây giờ bạn đã biết cách sử dụng các tính năng cơ bản của ứng dụng Ashigaru. Trong các bài hướng dẫn sau, chúng ta sẽ xem xét cách tận dụng các giao dịch chi tiêu nâng cao, cũng như Whirlpool, tính năng coinjoin kế thừa từ Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
