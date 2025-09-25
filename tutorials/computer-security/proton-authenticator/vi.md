---
name: Proton Authenticator
description: Tôi có thể sử dụng Proton Authenticator để bảo mật tài khoản của mình bằng 2FA như thế nào?
---
![cover](assets/cover.webp)



Xác thực hai yếu tố (2FA) bổ sung thêm một rào cản bảo mật cho tài khoản của bạn bằng cách yêu cầu, ngoài mật khẩu, một bằng chứng bổ sung chứng minh chỉ bạn mới có mật khẩu. Việc bật 2FA giúp giảm đáng kể nguy cơ bị hack, ngay cả khi mật khẩu của bạn bị lộ thông qua lừa đảo hoặc rò rỉ dữ liệu. Nếu không có 2FA, kẻ tấn công sẽ chỉ cần mật khẩu của bạn để truy cập tài khoản; với 2FA, chúng cũng sẽ cần đến yếu tố thứ hai của bạn, ngăn chặn hầu hết các nỗ lực đánh cắp tài khoản.



Có nhiều loại 2FA khác nhau. Mã SMS tốt hơn không có gì, nhưng vẫn dễ bị tấn công và đánh cắp thông tin qua SIM. Chúng tôi không khuyến nghị sử dụng SMS làm 2FA chính. Ứng dụng xác thực (TOTP) generate sử dụng mã tạm thời cục bộ trên thiết bị của bạn, khiến chúng khó bị đánh cắp hơn nhiều. Khóa bảo mật vật lý mang lại khả năng bảo mật tốt nhất, nhưng yêu cầu phần cứng chuyên dụng.



Proton Authenticator là trình xác thực TOTP. Đây là giải pháp của Proton nhằm khắc phục những hạn chế của các ứng dụng hiện có: nhiều ứng dụng độc quyền, chứa trình theo dõi quảng cáo và không cung cấp sao lưu được mã hóa. Proton Authenticator tạo nên sự khác biệt bằng cách cung cấp một ứng dụng mã nguồn mở, không quảng cáo và trình theo dõi, với khả năng sao lưu được mã hóa đầu cuối.



## Giới thiệu Proton Authenticator



Proton Authenticator là ứng dụng xác thực TOTP dành cho thiết bị di động và máy tính để bàn được phát triển bởi Proton, nổi tiếng với các dịch vụ tập trung vào quyền riêng tư. Giống như tất cả các sản phẩm của Proton, ứng dụng này là mã nguồn mở và đã trải qua các cuộc kiểm tra bảo mật độc lập. Ứng dụng này có sẵn miễn phí trên tất cả các nền tảng (Android, iOS, Windows, macOS, Linux).



Proton Authenticator cung cấp các tính năng chính sau:





- Tạo mã **TOTP** cho tài khoản 2FA của bạn, tương thích với hầu hết các trang web sử dụng Google Authenticator, Authy, v.v.





- **Sao lưu đám mây được mã hóa tùy chọn**: bạn có thể liên kết ứng dụng với tài khoản Proton của mình để sao lưu và đồng bộ hóa mã với mã hóa đầu cuối. Nếu bạn bị mất thiết bị, chỉ cần kết nối lại thiết bị mới để khôi phục tất cả mã.





- **Đồng bộ hóa đa thiết bị**: bằng cách đăng nhập vào Proton trên ứng dụng, mã 2FA của bạn sẽ tự động đồng bộ hóa giữa nhiều thiết bị thông qua mã hóa đầu cuối. Trên iOS, một lựa chọn thay thế là đồng bộ hóa qua iCloud.





- **Khóa cục bộ bằng mật khẩu hoặc sinh trắc học**: ứng dụng cung cấp tính năng khóa bằng mã PIN và/hoặc vân tay/Face ID. Vì vậy, ngay cả khi ai đó truy cập trực tiếp vào điện thoại đã mở khóa của bạn, họ cũng sẽ không thể mở Proton Authenticator.





- **Không thu thập dữ liệu hoặc trình theo dõi**: Proton cam kết không thu thập dữ liệu cá nhân thông qua ứng dụng. Không có quảng cáo ẩn hoặc phân tích hành vi.





- **Dễ dàng nhập/xuất**: một trong những điểm mạnh của Proton Authenticator là trình hướng dẫn nhập cho các tài khoản hiện có, tương thích với các ứng dụng khác (Google Authenticator, Authy, Aegis, v.v.). Bạn cũng có thể xuất mã của mình sang tệp nếu cần.



Tóm lại, Proton Authenticator hướng tới mục tiêu trở thành giải pháp 2FA hoàn hảo: an toàn, riêng tư, linh hoạt.



## Cài đặt



Proton Authenticator được cung cấp miễn phí trên mọi nền tảng. Để tải ứng dụng, hãy truy cập trang web chính thức: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Trang Proton Authenticator chính thức hiển thị các tính năng chính của ứng dụng và Interface*



Trên trang này, bạn sẽ tìm thấy các liên kết tải xuống cho tất cả các hệ điều hành: Android, iOS, Windows, macOS và Linux. Chỉ cần nhấp vào hệ điều hành bạn chọn và làm theo các bước cài đặt tiêu chuẩn.



Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn cách cài đặt và cấu hình ứng dụng trên macOS, sau đó chúng ta sẽ xem cách cài đặt ứng dụng trên iOS và đồng bộ hóa mã giữa hai thiết bị.



### Cài đặt trên macOS



Sau khi tải xuống và cài đặt ứng dụng, hãy khởi chạy Proton Authenticator. Trong lần khởi chạy đầu tiên, ứng dụng sẽ hướng dẫn bạn qua một vài màn hình cấu hình ban đầu:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Màn hình chào mừng của Proton Authenticator với thông báo "Bảo mật trong mọi mã" và nút "Bắt đầu"*



### Nhập khẩu ban đầu



Nếu Proton Authenticator phát hiện bạn đã sử dụng một ứng dụng 2FA khác trước đó, trình hướng dẫn nhập có thể xuất hiện. Trình hướng dẫn này hỗ trợ nhập trực tiếp từ một số ứng dụng nhất định (Google Authenticator, 2FAS, Authy, Aegis, v.v.). Ngoài ra, bạn có thể bỏ qua bước này và thêm tài khoản thủ công sau.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Trình hướng dẫn nhập để chuyển mã từ các ứng dụng xác thực khác*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Các ứng dụng nhập tương thích: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth và Google Authenticator*



### Bảo vệ ứng dụng cục bộ



Đặt mã PIN mở khóa hoặc bật tính năng mở khóa sinh trắc học (Touch ID) nếu có. Bước này rất quan trọng để ngăn chặn bất kỳ ai sử dụng máy Mac của bạn truy cập miễn phí vào mã 2FA của bạn.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Màn hình cấu hình Touch ID với thông báo "Bảo vệ dữ liệu của bạn" và nút "Kích hoạt Touch ID"*



### Tùy chọn đồng bộ hóa



Ứng dụng này cũng cho phép bạn kích hoạt tính năng đồng bộ hóa iCloud để sao lưu dữ liệu an toàn giữa các thiết bị Apple của bạn.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*Tùy chọn đồng bộ hóa iCloud với thông báo "Sao lưu dữ liệu của bạn một cách an toàn với tính năng đồng bộ hóa iCloud được mã hóa"*



Sau khi hoàn tất các bước này, Proton Authenticator đã sẵn sàng để sử dụng.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface chính Proton Authenticator trống với tùy chọn "Tạo mã mới" và "Nhập mã"*



## Thêm tài khoản 2FA với ProtonMail



Bây giờ chúng ta sẽ xem cách thêm mã 2FA đầu tiên, sử dụng ProtonMail làm ví dụ. Phương pháp này hoạt động giống hệt nhau trên tất cả các dịch vụ hỗ trợ xác thực hai yếu tố.



### Bật 2FA trên ProtonMail



Trước hết, bạn có thể tham khảo hướng dẫn sử dụng ProtonMail của chúng tôi để biết thêm thông tin:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Đăng nhập vào tài khoản ProtonMail của bạn và vào phần cài đặt bảo mật. Tìm tùy chọn "Xác thực hai yếu tố" và kích hoạt.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*Trang cài đặt ProtonMail với tùy chọn "Ứng dụng xác thực" trong phần "Xác thực hai yếu tố"*



Nhấp vào nút để kích hoạt trình xác thực và ProtonMail sẽ nhắc bạn chọn ứng dụng xác thực.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*Cửa sổ cấu hình ProtonMail 2FA với các nút "Hủy" và "Tiếp theo"*



Sau đó, ProtonMail sẽ hiển thị mã QR để bạn quét bằng ứng dụng xác thực.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*Mã QR ProtonMail để quét bằng ứng dụng xác thực của bạn, với tùy chọn "Nhập mã thủ công" khả dụng*



Nếu bạn muốn nhập khóa theo cách thủ công, hãy nhấp vào "Nhập khóa theo cách thủ công" để xem khóa bí mật.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Nhập thủ công thông tin 2FA: Khóa, Khoảng thời gian (30) và Chữ số (6)*



### Quét mã QR bằng Proton Authenticator



Trong Proton Authenticator trên macOS, hãy nhấp vào "Tạo mã mới". Ứng dụng cung cấp cho bạn một số tùy chọn: **Quét mã QR** hoặc **Nhập khóa thủ công**.



Sử dụng camera của máy Mac để quét mã QR hiển thị trên màn hình ProtonMail. Sau khi quét mã QR, bạn sẽ được chuyển đến màn hình cấu hình mã mới.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Cửa sổ tạo mục nhập mới với Tiêu đề (ProtonMail), Bí mật, Người gửi (Proton), tham số chữ số và trường khoảng cách*



Proton Authenticator sẽ tự động điền thông tin. Bạn có thể tùy chỉnh tên nếu muốn, sau đó nhấp vào "Lưu".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*Mã TOTP được tạo cho ProtonMail (848 812) với thời gian còn lại được hiển thị*



### Xác thực cấu hình



ProtonMail sẽ yêu cầu bạn nhập mã gồm 6 chữ số do Proton Authenticator tạo ra để xác nhận rằng 2FA đang hoạt động chính xác.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*Màn hình xác thực ProtonMail yêu cầu bạn nhập mã 6 chữ số (848812)*



Sao chép mã từ ứng dụng (bằng cách nhấp vào mã) và dán vào ProtonMail để hoàn tất quá trình kích hoạt.



Sau khi xác thực, ProtonMail sẽ yêu cầu bạn tải xuống mã khôi phục. Điều quan trọng là phải lưu chúng cẩn thận.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*Màn hình mã khôi phục ProtonMail với danh sách mã khôi phục và nút "Tải xuống"*



### Mã khẩn cấp



Khi thêm tài khoản, hãy giữ lại mã khôi phục do dịch vụ cung cấp. Hầu hết các trang web đều cung cấp mã khôi phục tĩnh, dùng một lần để lưu trữ ở nơi an toàn. Hãy giữ các mã dự phòng này bên ngoài Proton Authenticator để bạn có thể truy cập tài khoản nếu mất quyền truy cập vào ứng dụng 2FA.



## Cài đặt IOS và nhập mã



Bây giờ bạn đã thiết lập Proton Authenticator trên macOS, bạn cũng có thể muốn sử dụng nó trên iPhone hoặc iPad. Sau đây là cách lấy mã 2FA trên nhiều thiết bị.



### Tải ứng dụng trên iOS



Truy cập App Store và tìm kiếm "Proton Authenticator". Tải xuống và cài đặt ứng dụng trên thiết bị iOS của bạn.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Quá trình cài đặt trên iOS: màn hình chào mừng, trình hướng dẫn nhập, lựa chọn các ứng dụng tương thích và màn hình cuối cùng "Nhập mã từ Proton Authenticator"*



### Phương pháp 1: Xuất/Nhập qua tệp JSON



Nếu bạn không sử dụng tính năng đồng bộ hóa tự động (tài khoản iCloud hoặc Proton), bạn sẽ cần phải chuyển mã thủ công từ máy Mac sang iPhone:



**Bước 1 - Xuất từ macOS**:



Trên máy Mac, hãy mở Proton Authenticator và vào Cài đặt (biểu tượng bánh răng). Trong menu, nhấp vào "Xuất".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Menu cài đặt Proton Authenticator trên macOS với tùy chọn "Xuất" hiển thị*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Xuất cửa sổ với tên tệp "Proton_Authenticator_backup_2025" và nút "Lưu"*



Lưu tệp JSON trên máy Mac của bạn. Bạn có thể gửi tệp qua email bảo mật hoặc lưu vào iCloud Drive để truy cập từ iPhone.



**Bước 2 - Nhập vào iOS**:



Trên iPhone, hãy cài đặt Proton Authenticator và trong quá trình cấu hình, hãy chọn nhập mã. Chọn "Proton Authenticator" từ danh sách và nhập tệp JSON.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Quy trình nhập trên iOS: Bản địa hóa tệp JSON, xác nhận nhập và màn hình cấu hình với tùy chọn Face ID và iCloud*



### Phương pháp 2: Đồng bộ hóa tự động



**Thông qua tài khoản Proton (để đồng bộ hóa đa nền tảng)** :



Nếu bạn chưa thiết lập tài khoản Proton và muốn đồng bộ hóa giữa các hệ điều hành khác nhau, ứng dụng sẽ nhắc bạn tạo hoặc kết nối tài khoản Proton.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Màn hình đồng bộ hóa thiết bị yêu cầu bạn tạo tài khoản Proton miễn phí hoặc kết nối với tài khoản hiện có*



**Qua iCloud (chỉ dành cho hệ sinh thái Apple)** :


Nếu bạn chỉ sử dụng thiết bị Apple, bạn có thể chọn đồng bộ hóa iCloud trong cài đặt ứng dụng. Phương pháp này sẽ tự động đồng bộ hóa mã của bạn giữa tất cả các thiết bị Apple mà không cần tài khoản Proton.



## Sao lưu và khôi phục được mã hóa



Một trong những tính năng chính của Proton Authenticator là sao lưu mã 2FA từ đầu đến cuối, đảm bảo rằng việc mất hoặc thay đổi thiết bị không có nghĩa là bạn phải bắt đầu lại từ đầu.



### Mã hóa đầu cuối



Khi nói đến sao lưu đám mây được mã hóa với Proton Authenticator, bí mật TOTP của bạn được mã hóa cục bộ trên thiết bị của bạn trước khi được gửi đến máy chủ Proton. Việc giải mã chỉ có thể được thực hiện bởi bạn, trên các thiết bị được kết nối với tài khoản Proton của bạn. Proton AG không có khóa để đọc mã đã đăng ký của bạn.



Trên iOS, nếu bạn chọn iCloud thay vì tài khoản Proton, dữ liệu của bạn sẽ được mã hóa theo tiêu chuẩn của Apple. Tính năng sao lưu cục bộ trên Android cho phép bạn mã hóa tệp sao lưu bằng mật khẩu tùy chọn.



### Phục hồi trong trường hợp mất mát



Nếu điện thoại của bạn bị mất, bị đánh cắp hoặc bạn thay đổi điện thoại:



**Khi bật sao lưu Proton**: Cài đặt Proton Authenticator trên thiết bị mới. Trong quá trình thiết lập ban đầu, hãy đăng nhập vào cùng tài khoản Proton. Ngay lập tức, ứng dụng sẽ đồng bộ hóa và tải xuống tất cả mã 2FA của bạn từ bản sao lưu đã mã hóa.



**Với sao lưu iCloud (iOS)**: Kết nối iPhone/iPad mới với cùng một Apple ID và đảm bảo kích hoạt iCloud Keychain. Sau khi cài đặt Proton Authenticator, hãy kết nối với iCloud. Mã của bạn sẽ được đồng bộ hóa qua iCloud và hiển thị.



**Không có bản sao lưu đám mây**: Bạn sẽ cần nhập tài khoản theo cách thủ công. Nếu bạn đã xuất tệp sao lưu, hãy sử dụng chức năng Nhập trong Proton Authenticator. Trong trường hợp xấu nhất, nếu bạn không có bản sao lưu, bạn sẽ cần sử dụng mã sao lưu cho từng dịch vụ hoặc liên hệ với bộ phận hỗ trợ.



Proton Authenticator cho phép bạn xuất tài khoản bất cứ lúc nào, dưới dạng tệp được mã hóa hoặc mã QR cho nhiều tài khoản. Các tùy chọn này mang lại cho bạn sự an tâm hơn.



## Thực hành tốt nhất



Sử dụng xác thực 2FA sẽ tăng cường đáng kể tính bảo mật của bạn, nhưng bạn phải tuân thủ một số biện pháp tốt nhất sau:



### Lưu mã khẩn cấp của bạn



Khi bạn kích hoạt 2FA trên một dịch vụ, bạn thường được cung cấp một danh sách mã khôi phục. Hãy giữ chúng ngoài điện thoại (trên giấy, trong trình quản lý mật khẩu được mã hóa, v.v.). Trong trường hợp mất toàn bộ mã xác thực, những mã tĩnh này sẽ cứu bạn.



### Đừng nhầm lẫn mật khẩu và mã 2FA



Thật hấp dẫn khi sử dụng một trình quản lý mật khẩu cũng lưu trữ TOTP. Tuy nhiên, việc giữ mật khẩu và mã 2FA ở cùng một nơi sẽ tạo ra một điểm lỗi duy nhất và làm suy yếu xác thực kép. Để bảo mật tối đa, nhiều chuyên gia khuyên bạn nên tách biệt hai yếu tố: mật khẩu trong một trình quản lý an toàn và mã 2FA trong một ứng dụng riêng biệt như Proton Authenticator. Tuy nhiên, sử dụng một trình quản lý tích hợp vẫn tốt hơn là không có 2FA nào cả.



### Kích hoạt một số phương pháp 2FA



Tốt nhất, hãy sử dụng nhiều hơn một yếu tố thứ hai cho các tài khoản quan trọng của bạn. Đừng ngần ngại thêm khóa bảo mật vật lý nếu dịch vụ cho phép. Xem hướng dẫn của chúng tôi về khóa vật lý Yubikey để biết thêm thông tin:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Tương tự như vậy, hãy luôn giữ sẵn các mã khẩn cấp đã in sẵn.



### Hãy giữ kín đáo và bảo vệ thiết bị của bạn



Đừng để ai kiểm tra điện thoại đã mở khóa của bạn. Với Proton Authenticator, mã PIN/sinh trắc học của bạn được bảo vệ - đừng tiết lộ mã PIN này. Tương tự, hãy cẩn thận với lừa đảo: ngay cả khi sử dụng 2FA, nếu bạn cung cấp mã cho một trang web lừa đảo theo thời gian thực, kẻ tấn công vẫn có thể lợi dụng mã đó.



### Cập nhật và kiểm tra



Luôn cập nhật Proton Authenticator (cập nhật để sửa các lỗi tiềm ẩn). Vì mã nguồn mở, cộng đồng sẽ tiến hành kiểm tra không chính thức và Proton sẽ công bố kết quả kiểm tra chính thức.



## So sánh với các ứng dụng khác



So sánh Proton Authenticator với các ứng dụng xác thực khác như thế nào? Dưới đây là tóm tắt so sánh:



**Proton Authenticator**: Mã nguồn mở, sao lưu đám mây được mã hóa E2EE tùy chọn, đồng bộ hóa nhiều thiết bị, khóa cục bộ, không theo dõi, có sẵn trên thiết bị di động và máy tính để bàn.



**Google Authenticator**: Độc quyền, sao lưu qua tài khoản Google từ năm 2023 nhưng không có mã hóa đầu cuối (Google có thể xem khóa), đồng bộ hóa nhiều thiết bị được thêm vào năm 2023, không khóa ứng dụng theo mặc định, chứa trình theo dõi của Google.



**Aegis Authenticator**: Mã nguồn mở, chỉ sao lưu cục bộ, không đồng bộ hóa đám mây, khóa mã/sinh trắc học, không theo dõi, chỉ dành cho Android.



**Authy**: Sao lưu đám mây độc quyền, được mã hóa bằng mật khẩu nhưng mã đóng, đồng bộ hóa nhiều thiết bị, khóa mã PIN/vân tay, thu thập số điện thoại, ứng dụng dành cho máy tính để bàn đã ngừng hoạt động vào tháng 3 năm 2024.



Bạn sẽ tìm thấy hướng dẫn về Authy của chúng tôi bên dưới:



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator là một trong những giải pháp toàn diện và an toàn nhất hiện nay: mã nguồn mở, đồng bộ hóa được mã hóa trên nhiều thiết bị, không cần theo dõi thương mại.



## Tài nguyên và hỗ trợ



### Tài liệu chính thức




- **Trang web chính thức**: [proton.me/authenticator](https://proton.me/authenticator) - Giới thiệu sản phẩm và tải xuống
- **Trang tải xuống**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Liên kết cho tất cả các hệ điều hành
- **Hỗ trợ Proton**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Hướng dẫn kích hoạt 2FA chính thức
- **Blog Proton**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Thông báo và các tính năng chi tiết



### Mã nguồn và tính minh bạch




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Mã nguồn mở
- **Kiểm toán bảo mật**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Báo cáo kiểm toán độc lập



### Các thử nghiệm an toàn được khuyến nghị


Sau khi cấu hình, hãy kiểm tra thiết lập của bạn:




- [Tôi đã bị tấn công chưa](https://haveibeenpwned.com/) - Kiểm tra xem tài khoản của bạn có bị xâm phạm không
- [Thư mục 2FA](https://2fa.directory/) - Danh sách các dịch vụ hỗ trợ 2FA



### Cộng đồng và thảo luận




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Cộng đồng Proton chính thức
- **Diễn đàn Hướng dẫn về Quyền riêng tư**: [discuss.privacyguides.net](https://discuss.privacyguides.net) - Thảo luận kỹ thuật về các vấn đề quyền riêng tư
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Mẹo chung về quyền riêng tư



### Khác




- [Tôi đã bị tấn công chưa](https://haveibeenpwned.com/) - Kiểm tra xem tài khoản của bạn có bị xâm phạm không
- [Thư mục 2FA](https://2fa.directory/) - Danh sách các dịch vụ hỗ trợ 2FA