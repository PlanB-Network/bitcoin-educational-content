---
name: Aegis Authenticator
description: Bạn có thể sử dụng Aegis Authenticator để bảo mật tài khoản của mình bằng xác thực kép như thế nào?
---

![cover](assets/cover.webp)



Ngày nay, xác thực hai yếu tố (2FA) là điều cần thiết để bảo mật tài khoản trực tuyến. Ngoài mật khẩu, nó còn bổ sung thêm một yếu tố thứ hai (thường là mã 6 chữ số) hết hạn sau 30 giây, khiến tin tặc khó khăn hơn đáng kể. Sử dụng ứng dụng TOTP (Mật khẩu dùng một lần theo thời gian) chuyên dụng an toàn hơn so với SMS, vốn có thể bị tấn công bằng cách hoán đổi SIM.



Tuy nhiên, không phải tất cả các ứng dụng xác thực đều được tạo ra như nhau. Nhiều giải pháp độc quyền (Google Authenticator, Authy, v.v.) gây ra nhiều vấn đề: chúng độc quyền và mã nguồn đóng (không thể kiểm tra tính bảo mật), đôi khi tích hợp trình theo dõi quảng cáo, không cung cấp bản sao lưu được mã hóa cho mã của bạn, và thậm chí có thể ngăn chặn việc xuất tài khoản của bạn để khóa bạn vào hệ sinh thái của họ.



Mặt khác, Aegis Authenticator tự giới thiệu mình là một giải pháp thay thế miễn phí và hợp lý cho các ứng dụng này. Aegis là một ứng dụng mã nguồn mở, miễn phí, an toàn để quản lý mã thông báo xác minh hai bước trên Android. Việc phát triển ứng dụng tập trung vào các tính năng thiết yếu mà các ứng dụng khác không có, bao gồm mã hóa dữ liệu cục bộ mạnh mẽ và khả năng sao lưu an toàn. Nhìn chung, Aegis cung cấp một giải pháp xác thực kép cục bộ, có thể kiểm tra, lý tưởng cho bất kỳ ai muốn kiểm soát hoàn toàn mã 2FA của mình.



## Giới thiệu Aegis Authenticator



Aegis Authenticator là một ứng dụng xác thực hai yếu tố (2FA) mã nguồn mở dành cho Android, được phát hành theo giấy phép GPL v3. Ứng dụng nổi bật với triết lý "quyền riêng tư được thiết kế": ứng dụng hoạt động hoàn toàn ngoại tuyến và không yêu cầu kết nối với dịch vụ từ xa. Do đó, mã thông báo của bạn được lưu trữ cục bộ trên thiết bị, trong một két an toàn mà chỉ bạn mới có thể nắm giữ khóa.



### Các tính năng chính



**Kho lưu trữ được mã hóa:** tất cả mã OTP của bạn được lưu trữ trong kho lưu trữ được mã hóa AES-256 (chế độ GCM), được bảo vệ bằng mật khẩu chính do người dùng thiết lập. Bạn có thể mở khóa kho lưu trữ này bằng mật khẩu hoặc dữ liệu sinh trắc học (vân tay, nhận dạng khuôn mặt) để thuận tiện hơn. Nếu không có mật khẩu, dữ liệu sẽ không được mã hóa - vì vậy chúng tôi đặc biệt khuyến nghị bạn nên đặt mật khẩu.



**Tổ chức nâng cao:** Aegis giúp sắp xếp hợp lý nhiều tài khoản 2FA của bạn. Bạn có thể sắp xếp các mục theo thứ tự bảng chữ cái hoặc theo thứ tự mong muốn, nhóm chúng theo danh mục (ví dụ: Cá nhân, Công việc, Xã hội) để dễ dàng truy xuất và gán cho mỗi mục một biểu tượng được cá nhân hóa. Thanh tìm kiếm được tích hợp để tìm kiếm ngay một dịch vụ hoặc tài khoản theo tên.



**Sao lưu cục bộ được mã hóa:** Để đảm bảo bạn không bao giờ mất quyền truy cập vào tài khoản của mình, Aegis cung cấp tính năng sao lưu tự động vào két an toàn. Các bản sao lưu này được mã hóa (bằng mật khẩu) và có thể được lưu trữ ở vị trí bạn chọn (bộ nhớ trong, thư mục đám mây, v.v.). Ứng dụng cũng có thể xuất cơ sở dữ liệu tài khoản của bạn theo cách thủ công, ở định dạng được mã hóa hoặc không được mã hóa tùy theo yêu cầu. Việc nhập tài khoản từ các ứng dụng 2FA khác cũng dễ dàng như vậy (Aegis hỗ trợ nhập từ Authy, Google Authenticator, FreeOTP và OTP, v.v.).



**Bảo mật và quyền riêng tư:** ứng dụng hoàn toàn ngoại tuyến theo mặc định. Nó không yêu cầu quyền truy cập mạng - nghĩa là không truyền dữ liệu ra bên ngoài, và không có trình theo dõi quảng cáo hay mô-đun phân tích hành vi. Aegis không hiển thị quảng cáo và không yêu cầu tài khoản người dùng: ngay sau khi cài đặt, ứng dụng sẽ hoạt động mà không cần đăng ký. Vì mã nguồn của nó được công khai trên GitHub, cộng đồng có thể tự do kiểm tra, đảm bảo không có các chức năng độc hại hoặc ẩn.



**Interface hiện đại:** Aegis áp dụng thiết kế Material Design gọn gàng, hỗ trợ giao diện tối (bao gồm chế độ AMOLED) và thậm chí có tùy chọn hiển thị mã theo ô để hiển thị dưới dạng lưới. Interface gọn gàng, không rườm rà và ngăn chặn việc chụp màn hình mã như một biện pháp bảo mật.



## Cài đặt



Vì Aegis Authenticator là mã nguồn mở, các nhà phát triển ưu tiên các kênh phân phối thân thiện với quyền riêng tư. Có hai cách chính để cài đặt:



### Qua F-Droid (khuyến nghị)



Cách an toàn và dễ dàng nhất là thông qua F-Droid, cửa hàng ứng dụng thay thế miễn phí. Nếu F-Droid chưa được cài đặt trên điện thoại của bạn, hãy bắt đầu bằng cách tải xuống từ trang web chính thức [F-Droid.org](https://f-droid.org). Sau đó:





- Mở F-Droid và đảm bảo bạn đã cập nhật kho lưu trữ của mình để có danh sách ứng dụng mới nhất
- Tìm kiếm "Aegis Authenticator" trong F-Droid. Ứng dụng chính thức sẽ xuất hiện (nhà phát hành: Beem Development)
- Bắt đầu cài đặt bằng cách nhấn Cài đặt. Vì Aegis là một trong những ứng dụng được F-Droid xác minh, bạn sẽ được hưởng lợi từ quá trình tải xuống đáng tin cậy và an toàn.



Cài đặt qua F-Droid mang lại lợi thế là nhận được các bản cập nhật ứng dụng tự động ngay khi chúng được phát hành. Hơn nữa, F-Droid đảm bảo rằng ứng dụng không chứa các thành phần độc quyền không mong muốn.



### Qua GitHub (APK đã ký)



Nếu bạn muốn cài đặt ứng dụng mà không cần thông qua cửa hàng, bạn có thể tải xuống APK chính thức trực tiếp từ trang GitHub của dự án. Trên kho lưu trữ Aegis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), hãy vào mục Bản phát hành, nơi các phiên bản ổn định được phát hành.





- Tải xuống phiên bản APK mới nhất
- Trước khi cài đặt APK, hãy đảm bảo bạn đã cho phép cài đặt ứng dụng từ nguồn không xác định trên thiết bị của mình (trong Cài đặt Android)
- APK được cung cấp trên GitHub được nhà phát triển ký bằng cùng khóa như trên F-Droid



Sau khi cài đặt thủ công, ứng dụng sẽ hoạt động giống hệt nhau. Xin lưu ý rằng các bản cập nhật sẽ không tự động: bạn cần kiểm tra GitHub định kỳ để biết phiên bản mới.



### Cửa hàng Google Play so với F-Droid



Aegis Authenticator có sẵn trên cả Google Play Store và F-Droid, cho phép bạn lựa chọn phương pháp cài đặt:



**Cửa hàng Google Play:**




- ✅ Cập nhật tự động được tích hợp vào hệ thống Android
- ✅ Cài đặt đơn giản, quen thuộc
- ✅ APK có chữ ký giống như trên các kênh khác



**F-Droid (khuyến nghị):**




- ✅ Cửa hàng miễn phí và mã nguồn mở
- ✅ Xây dựng có thể tái tạo và xác minh được
- ✅ Không cần dịch vụ Google
- ✅ Tôn trọng triết lý phần mềm miễn phí



Việc lựa chọn giữa hai tùy chọn này phụ thuộc vào sở thích của bạn về hệ sinh thái Google. Nếu bạn thích sự đơn giản, Cửa hàng Play là lựa chọn lý tưởng. Nếu bạn muốn một giải pháp bảo mật hơn, độc lập với các dịch vụ của Google, F-Droid là lựa chọn tốt hơn.



## Cấu hình đầu tiên



Khi Aegis được khởi chạy lần đầu tiên, một quy trình cấu hình ban đầu sẽ được đề xuất để bảo vệ mã 2FA của bạn an toàn:



![Configuration initiale Aegis](assets/fr/01.webp)



*Quy trình cấu hình Aegis ban đầu: màn hình chào mừng, lựa chọn bảo mật, định nghĩa mật khẩu chính và hoàn tất*



### Đặt mật khẩu chính



Trước tiên, Aegis sẽ yêu cầu bạn chọn mật khẩu chính. Mật khẩu này sẽ được sử dụng để mã hóa tất cả mã thông báo xác thực được lưu trữ trong kho lưu trữ. Chúng tôi đặc biệt khuyên bạn nên đặt một mật khẩu mạnh, duy nhất mà chỉ bạn mới biết.



**⚠️ Cảnh báo:** đừng quên mật khẩu này - nếu bạn làm mất nó, mã 2FA đã mã hóa của bạn sẽ không thể truy cập được (không có cửa hậu). Aegis sẽ yêu cầu bạn nhập mật khẩu hai lần để xác nhận.



### Bật mở khóa sinh trắc học (tùy chọn)



Nếu thiết bị Android của bạn được trang bị đầu đọc dấu vân tay hoặc cảm biến sinh trắc học khác, Aegis sẽ nhắc bạn kích hoạt mở khóa sinh trắc học. Tùy chọn này là tùy chọn nhưng rất thiết thực: cho phép bạn nhanh chóng mở khóa ứng dụng bằng dấu vân tay hoặc khuôn mặt, thay vì phải nhập mật khẩu mỗi lần.



Lưu ý rằng sinh trắc học là một tiện ích bổ sung: bạn vẫn cần nhập mật khẩu chính nếu sinh trắc học bị thay đổi hoặc thiết bị được khởi động lại.



### Khám phá cài đặt ứng dụng



Khi đã vào ứng dụng (Interface chính ban đầu trống), hãy làm quen với các tùy chọn cấu hình có sẵn. Truy cập cài đặt thông qua menu thả xuống ở góc trên bên phải màn hình (ba dấu chấm dọc), sau đó chọn "Cài đặt".



![Interface principale et paramètres](assets/fr/02.webp)



*Aegis chính của Interface trống khi bắt đầu, truy cập vào menu tham số và tổng quan về các tùy chọn có sẵn*



Menu cài đặt Aegis nhóm một số phần quan trọng lại với nhau:





- **Giao diện**: Tùy chỉnh chủ đề (sáng, tối, AMOLED), ngôn ngữ và các cài đặt hình ảnh khác
- **Hành vi**: Cấu hình hành vi ứng dụng khi tương tác với danh sách mục nhập
- **Gói biểu tượng**: quản lý và nhập gói biểu tượng để tùy chỉnh giao diện cho tài khoản của bạn
- **Bảo mật**: Cài đặt mã hóa, mở khóa sinh trắc học, khóa tự động và các thông số bảo mật khác
- **Sao lưu**: Cấu hình sao lưu tự động đến vị trí bạn chọn
- **Nhập & Xuất**: Nhập bản sao lưu từ các ứng dụng xác thực khác và xuất thủ công kho lưu trữ Aegis của bạn
- **Nhật ký kiểm tra**: Nhật ký chi tiết về tất cả các sự kiện quan trọng trong ứng dụng



Tổ chức rõ ràng này cho phép bạn cấu hình Aegis theo sở thích và nhu cầu bảo mật của mình.



## Thêm tài khoản 2FA



Sau khi cấu hình Aegis, hãy chuyển sang phần thiết yếu: thêm tài khoản hai yếu tố của bạn. Quá trình này rất đơn giản và Aegis cung cấp nhiều phương pháp để tích hợp mã xác thực của bạn.



### Ba phương pháp bổ sung có sẵn



Từ Aegis Interface chính, nhấn nút **+** ở góc dưới bên phải để truy cập các tùy chọn thêm. Bạn có ba tùy chọn:





- **Quét mã QR**: Quét trực tiếp mã QR được hiển thị bởi dịch vụ web
- **Quét hình ảnh**: Quét mã QR từ hình ảnh được lưu trên thiết bị của bạn
- **Nhập thủ công**: Nhập thông tin tài khoản 2FA theo cách thủ công



### Ví dụ thực tế: cấu hình Bitwarden



Chúng ta hãy lấy ví dụ cụ thể về kích hoạt 2FA trên Bitwarden để minh họa quy trình:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Ví dụ về kích hoạt 2FA trên Bitwarden: Web Interface với các tùy chọn xác thực và khuyến nghị Aegis*





- **Đăng nhập và truy cập cài đặt**: Đăng nhập vào tài khoản Bitwarden của bạn và truy cập cài đặt, tab "Bảo mật"
- **Phần Nhà cung cấp**: Vào phần "Nhà cung cấp" và nhấp vào "Quản lý" trong phần "Ứng dụng xác thực"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Hoàn tất quy trình thêm tài khoản: Mã QR được dịch vụ hiển thị, khóa bí mật hiển thị và mã xác minh được nhập*





- **Quét mã QR**: Một cửa sổ bật lên sẽ mở ra với mã QR và khóa bí mật
- Trong **Aegis**: Sử dụng "Quét mã QR" để tự động thu thập thông tin
- **Xác minh**: Nhập mã 6 chữ số do Aegis tạo ra vào trường "Mã xác minh"
- **Kích hoạt**: Nhấp vào "Bật" để hoàn tất kích hoạt



### Thêm chi tiết theo cách thủ công



Nếu bạn muốn hoặc không thể quét mã QR, hãy sử dụng tùy chọn "Nhập thủ công". Biểu mẫu cho phép bạn nhập:



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Quy trình thêm tài khoản 2FA mới: điền Interface, thêm tùy chọn, nhập thủ công và thêm tài khoản thành công*





- **Tên**: Tên dịch vụ (ví dụ: Bitwarden, GitHub...)
- **Người phát hành**: Người phát hành (thường giống với tên)
- **Nhóm**: Tùy chọn, để sắp xếp tài khoản của bạn theo danh mục
- **Lưu ý**: Nhận xét cá nhân về tài khoản này
- **Bí mật**: Khóa bí mật do dịch vụ cung cấp (mặc định được che giấu)
- **Nâng cao**: Các tham số nâng cao (thuật toán, dấu chấm, số chữ số)



Sau khi tài khoản được thêm vào, tài khoản sẽ xuất hiện trong danh sách của bạn với mã hiện tại và chỉ báo thời gian hiển thị thời gian còn lại trước khi gia hạn.



### Khả năng tương thích phổ quát



Aegis tương thích với tất cả các dịch vụ sử dụng tiêu chuẩn TOTP và HOTP, bao gồm hầu hết các trang web cung cấp 2FA: mạng xã hội, ngân hàng, trình quản lý mật khẩu, nền tảng tiền điện tử, v.v.



### Tổ chức lối vào



Sau khi thêm nhiều tài khoản, bạn sẽ thấy được các công cụ tổ chức của Aegis:





- **Sắp xếp tùy chỉnh:** Theo mặc định, các tài khoản được liệt kê theo thứ tự bảng chữ cái, nhưng bạn có thể thay đổi thứ tự theo cách thủ công
- **Nhóm và danh mục:** Tạo nhóm để tách tài khoản cá nhân của bạn khỏi tài khoản doanh nghiệp hoặc nhóm chúng theo loại dịch vụ (ngân hàng, email, mạng xã hội, v.v.)
- **Biểu tượng tùy chỉnh:** Aegis cố gắng tự động gán một biểu tượng phù hợp nếu có, nếu không, bạn có thể chọn từ nhiều biểu tượng chung hoặc nhập một hình ảnh
- **Tìm kiếm nhanh:** Thanh tìm kiếm ở trên cùng cho phép bạn nhập một vài chữ cái để lọc ngay lập tức các mục phù hợp



Khi chạm vào một mục, mã OTP sẽ hiển thị ở kích thước đầy đủ (nếu mục đó bị ẩn) và bạn có thể sao chép mã đó vào bảng tạm bằng cách nhấn và giữ lâu - rất tiện lợi để dán vào ứng dụng bạn muốn kết nối.



## Bảo mật và sao lưu



Với tính bảo mật là trọng tâm của Aegis, điều quan trọng là phải hiểu cách mã 2FA của bạn được bảo vệ và cách đảm bảo chúng luôn tồn tại trong trường hợp có sự cố.



### Kiến trúc bảo mật



**Mã hóa mạnh mẽ**: Tất cả mã của bạn được lưu trữ trong két an toàn được mã hóa bằng **thuật toán AES-256 ở chế độ GCM**, kết hợp với mật khẩu chính của bạn. Việc tạo khóa dựa trên **scrypt**, mang lại khả năng bảo vệ nâng cao chống lại các cuộc tấn công dò mật khẩu.



**Mở khóa an toàn**: Cần có mật khẩu chính để giải mã dữ liệu của bạn. Sinh trắc học (tùy chọn) sử dụng **Android Secure Keystore** và TEE (Môi trường thực thi tin cậy) để bảo vệ khóa mã hóa.



**Quyền tối thiểu**: Aegis hoạt động ngoại tuyến theo mặc định, chỉ yêu cầu quyền truy cập vào camera (quét mã QR), sinh trắc học và máy rung. Không thu thập hoặc chia sẻ dữ liệu nào.



### Tùy chọn sao lưu



Aegis cung cấp nhiều chiến lược sao lưu phù hợp với các nhu cầu bảo mật và tiện lợi khác nhau:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface hoàn chỉnh với tài khoản bổ sung, cảnh báo sao lưu, cài đặt sao lưu tự động và chiến lược sao lưu*



**1. Sao lưu cục bộ tự động**




- Cấu hình thư mục đích theo lựa chọn của bạn
- Tần suất có thể tùy chỉnh (sau mỗi lần thay đổi, hàng ngày, v.v.)
- Các tệp được mã hóa được bảo vệ bằng mật khẩu (.aesvault)
- Tương thích với các thư mục được đồng bộ hóa (Nextcloud, Dropbox, v.v.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Quy trình lựa chọn thư mục sao lưu: trình khám phá tệp, thư mục đích và quyền truy cập*



**2. Sao lưu đám mây Android**




- Tích hợp tùy chọn với hệ thống sao lưu Android
- Chỉ có sẵn cho két an toàn được mã hóa (bảo mật được giữ nguyên)
- Sao lưu minh bạch với dữ liệu Android khác
- Tự động khôi phục khi chuyển đổi thiết bị



**3. Xuất thủ công**




- Xuất theo yêu cầu thông qua **Cài đặt > Nhập & Xuất**
- Lựa chọn định dạng được mã hóa (khuyến nghị) hoặc định dạng rõ ràng
- Hữu ích cho việc di chuyển hoặc sao lưu thường xuyên



### Thực hành an toàn tốt





- Giữ nhiều phiên bản **sao lưu** để ngăn ngừa hỏng hóc
- **Kiểm tra thường xuyên** bản sao lưu của bạn bằng cách thử khôi phục
- Lưu trữ mã khôi phục do dịch vụ cung cấp riêng biệt
- **Mật khẩu chính** của bạn vẫn được yêu cầu ngay cả khi đã sao lưu trên đám mây
- **Bảo mật mật khẩu chính của bạn**: sử dụng mật khẩu mạnh và duy nhất được lưu trữ trong trình quản lý mật khẩu
- Giữ cho ứng dụng của bạn được **cập nhật** với các bản vá bảo mật mới nhất
- Kích hoạt tính năng **tự động khóa** trong cài đặt để bảo mật quyền truy cập vào ứng dụng
- Tắt **ảnh chụp màn hình** (tùy chọn mặc định) để ngăn chặn mã của bạn bị chặn
- **Sử dụng sinh trắc học một cách tiết kiệm**: ưu tiên mật khẩu cho các truy cập quan trọng



## So sánh với các ứng dụng khác



Aegis so với các ứng dụng xác thực phổ biến khác như thế nào?



### Aegis so với Google Authenticator



**Aegis :**




- ✅ Mã nguồn mở và có thể kiểm tra
- ✅ Sao lưu được mã hóa cục bộ
- ✅ Tổ chức nâng cao (nhóm, biểu tượng, tìm kiếm)
- ✅ Không thu thập dữ liệu
- ❌ Chỉ dành cho Android



**Google Authenticator :**




- ✅ Có sẵn trên Android và iOS
- ✅ Đồng bộ hóa đám mây (từ năm 2023)
- ❌ Mã nguồn đóng
- ❌ Chức năng hạn chế
- ❌ Khả năng thu thập dữ liệu của Google



### Aegis so với Authy



**Aegis :**




- ✅ Mã nguồn mở
- ✅ Không cần tài khoản
- ✅ Có thể xuất mã
- ✅ Kiểm soát dữ liệu toàn diện
- ❌ Không có đồng bộ hóa đa thiết bị gốc



**Authy :**




- ✅ Đồng bộ hóa nhiều thiết bị
- ✅ Có sẵn trên Android và iOS
- ❌ Mã nguồn đóng
- ❌ Cần có số điện thoại
- ❌ Không thể xuất mã
- ❌ Các ứng dụng máy tính để bàn đã bị xóa vào tháng 3 năm 2024



Aegis là lựa chọn tuyệt vời cho người dùng Android coi trọng tính minh bạch, bảo mật cục bộ và quyền kiểm soát hoàn toàn dữ liệu. Các lựa chọn thay thế như Authy sẽ phù hợp hơn nếu bạn thực sự cần đồng bộ hóa tự động nhiều thiết bị.




## Phần kết luận



Aegis Authenticator là giải pháp tuyệt vời cho những ai đang tìm kiếm một ứng dụng 2FA thân thiện với quyền riêng tư, an toàn và minh bạch. Phương pháp mã nguồn mở, kết hợp với mã hóa mạnh mẽ và Interface gọn gàng, Aegis Authenticator là lựa chọn hàng đầu để bảo mật tài khoản trực tuyến của bạn.



Mặc dù chỉ giới hạn ở Android và thiếu tính năng đồng bộ hóa đám mây gốc, Aegis đã bù đắp những hạn chế này bằng triết lý "quyền riêng tư theo thiết kế" và khả năng kiểm soát dữ liệu toàn diện. Đối với người dùng quan tâm đến quyền riêng tư kỹ thuật số, Aegis mang đến một giải pháp thay thế đáng tin cậy và mạnh mẽ cho các giải pháp độc quyền đang thống trị thị trường.



Bảo mật tài khoản trực tuyến của bạn không nhất thiết phải phụ thuộc vào thiện chí của các công ty thương mại. Với Aegis, bạn có thể kiểm soát mã xác thực của mình trong một két sắt kỹ thuật số mà chỉ mình bạn nắm giữ chìa khóa.



## Tài nguyên



### Trang web chính thức




- **Trang web chính thức**: [getaegis.app](https://getaegis.app/) - Trình bày và tải xuống ứng dụng
- **Mã nguồn**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Kho lưu trữ GitHub chính thức
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Cài đặt qua cửa hàng miễn phí



### Tài liệu kỹ thuật




- **Tài liệu về Vault**: [Thiết kế Vault](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Mô tả kỹ thuật về mã hóa và kiến trúc bảo mật
- **Câu hỏi thường gặp chính thức**: [getaegis.app/#faq](https://getaegis.app/#faq) - Câu trả lời cho các câu hỏi thường gặp
- **Wiki dự án**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Tài liệu hướng dẫn sử dụng đầy đủ