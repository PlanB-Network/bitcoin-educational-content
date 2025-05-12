---
name: Keet
description: Trò chuyện ngang hàng
---
![cover](assets/cover.webp)



Keet là một ứng dụng nhắn tin tức thời được thiết kế để hoạt động mà không cần bất kỳ máy chủ nào. Được ra mắt vào năm 2022 bởi Holepunch (một công ty được Tether và Bitfinex tài trợ), ứng dụng này hoàn toàn dựa trên mạng ngang hàng và có phương pháp tiếp cận phi tập trung triệt để: tin nhắn, cuộc gọi và tệp được trao đổi trực tiếp giữa người dùng, không có trung gian.



Keet mã hóa mọi giao tiếp từ đầu đến cuối và không yêu cầu dữ liệu cá nhân. Đăng ký ẩn danh, không yêu cầu số điện thoại hoặc email. Ngoài việc trao đổi tin nhắn văn bản, Keet còn cung cấp các cuộc gọi video chất lượng rất cao cũng như chia sẻ tệp không giới hạn. Do đó, ứng dụng có thể được sử dụng theo cách kết hợp, cho cả mục đích cá nhân và chuyên nghiệp.



![Image](assets/fr/01.webp)



Hiện tại (tháng 4 năm 2025), Keet không hoàn toàn là mã nguồn mở. Một số mã nguồn có sẵn trên [kho lưu trữ GitHub của Holepunch](https://github.com/holepunchto), đặc biệt là các thành phần mật mã và mạng, nhưng máy khách Interface vẫn chưa có. Tuy nhiên, Holepunch đã công bố ý định biến toàn bộ ứng dụng thành mã nguồn mở. Tùy thuộc vào thời điểm bạn khám phá ra hướng dẫn này, điều này có thể đã được thực hiện.




| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| **Keet**             | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Mã hóa đầu cuối*



## Cài đặt Keet



Keet có sẵn trên mọi nền tảng. Bạn có thể tải ứng dụng trực tiếp từ cửa hàng ứng dụng trên điện thoại của bạn:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [Cửa hàng ứng dụng](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



Trên Android, bạn cũng có thể [cài đặt qua APK](https://github.com/holepunchto/keet-mobile-releases/releases).



Trong hướng dẫn này, chúng tôi sẽ tập trung vào phiên bản di động, nhưng xin lưu ý rằng [phiên bản máy tính cũng khả dụng](https://keet.io/) (MacOS, Linux và Windows). Bạn cũng có thể đồng bộ hóa tài khoản của mình trên nhiều thiết bị.



## Tạo một tài khoản trên Keet



Khi khởi chạy lần đầu, bạn có thể bỏ qua màn hình trình bày.



![Image](assets/fr/02.webp)



Nhấp vào nút "*Tôi là người dùng mới*".



![Image](assets/fr/03.webp)



Chấp nhận các điều khoản sử dụng, sau đó nhấp vào "*Cài đặt nhanh*".



![Image](assets/fr/04.webp)



Chọn tên hoặc biệt danh, sau đó nhấp vào "*Hoàn tất thiết lập*".



![Image](assets/fr/05.webp)



Hồ sơ của bạn đã được tạo. Nhấp vào "*Hoàn tất thiết lập*" một lần nữa để hoàn tất.



![Image](assets/fr/06.webp)



Bạn có thể tùy chỉnh hồ sơ của mình bất kỳ lúc nào từ tab "*Hồ sơ*".



## Lưu tài khoản Keet của bạn



Điều đầu tiên cần làm với tài khoản Keet mới của bạn là lưu cụm từ khôi phục. Đây là một chuỗi gồm 24 từ cho phép bạn khôi phục quyền truy cập vào tài khoản của mình trong trường hợp mất hoặc thay đổi thiết bị. Cụm từ này cấp quyền truy cập đầy đủ vào tài khoản của bạn cho bất kỳ ai biết, vì vậy điều quan trọng là phải sao lưu đáng tin cậy và không bao giờ tiết lộ.



Để thực hiện việc này, hãy nhấp vào tab "*Hồ sơ*" ở góc dưới bên phải của Interface.



![Image](assets/fr/07.webp)



Sau đó truy cập vào menu "*Cài đặt*".



![Image](assets/fr/08.webp)



Chọn "*Quyền riêng tư và Bảo mật*".



![Image](assets/fr/09.webp)



Sau đó nhấp vào "*Cụm từ khôi phục*".



![Image](assets/fr/10.webp)



Nhấn nút "*Xem cụm từ*" để hiển thị cụm từ khôi phục của bạn. Sao chép cẩn thận và giữ ở nơi an toàn.



![Image](assets/fr/11.webp)



## Gửi tin nhắn với Keet



Để giao tiếp trên Keet, bạn cần tạo "*Phòng*". Để thực hiện việc này, hãy nhấp vào biểu tượng bút chì ở góc trên bên phải của Interface.



![Image](assets/fr/12.webp)



Chọn "*Nhóm trò chuyện mới*".



![Image](assets/fr/13.webp)



Chọn tên và mô tả cho "*Phòng*" của bạn, sau đó nhấp vào "*Tạo trò chuyện nhóm*".



![Image](assets/fr/14.webp)



"*Phòng*" của bạn hiện đã được tạo. Nhấp vào biểu tượng "*+*" ở trên cùng bên phải để mời người tham gia.



![Image](assets/fr/15.webp)



Xác định các quyền bạn cấp cho thành viên mới thông qua liên kết mời, cũng như thời hạn hiệu lực của liên kết. Sau đó nhấp vào "*generate Invite*".



![Image](assets/fr/16.webp)



Keet sẽ generate một liên kết để tham gia "*Phòng*" của bạn. Bạn có thể sao chép và chia sẻ hoặc yêu cầu những người bạn muốn mời quét mã QR.



![Image](assets/fr/17.webp)



Bây giờ bạn có thể bắt đầu trao đổi tin nhắn và tệp đa phương tiện. Để bắt đầu cuộc gọi, hãy nhấp vào biểu tượng điện thoại ở góc trên bên phải.



![Image](assets/fr/18.webp)



Từ nhóm này, bạn cũng có thể gửi tin nhắn riêng cho một thành viên cụ thể. Nhấp vào ảnh đại diện của nhóm, sau đó chọn thành viên mong muốn trong phần "*Thành viên*".



![Image](assets/fr/19.webp)



Nhấp vào nút "*Gửi yêu cầu DM*" và nhập tin nhắn của bạn.



![Image](assets/fr/20.webp)



Sau khi yêu cầu nhắn tin trực tiếp được chấp nhận, bạn sẽ thấy người liên hệ này trên trang chủ, nơi bạn có thể nói chuyện riêng với người đó.



![Image](assets/fr/21.webp)



## Đồng bộ hóa tài khoản của bạn trên nhiều thiết bị



Bây giờ bạn đã biết cách sử dụng Keet và có tài khoản, bạn cũng có thể đồng bộ hóa nó trên một thiết bị khác, chẳng hạn như máy tính. Để thực hiện việc này, hãy mở ứng dụng trên điện thoại di động của bạn, sau đó nhấp vào "*Hồ sơ*" và truy cập "*Cài đặt*".



![Image](assets/fr/22.webp)



Sau đó vào menu "*Thiết bị của tôi*".



![Image](assets/fr/23.webp)



Nhấp vào "*Thêm thiết bị*". Keet sẽ generate một liên kết để đồng bộ hóa thiết bị mới. Sao chép liên kết này.



![Image](assets/fr/24.webp)



Trên thiết bị thứ hai của bạn, hãy cài đặt Keet. Trên màn hình chính, hãy chọn tùy chọn "*Tôi là người dùng hiện tại*".



![Image](assets/fr/25.webp)



Sau đó nhấp vào "*Liên kết thiết bị*".



![Image](assets/fr/26.webp)



Dán liên kết được cung cấp bởi thiết bị đầu tiên của bạn, sau đó nhấp vào "*Bắt đầu đồng bộ hóa*".



![Image](assets/fr/27.webp)



Trên thiết bị đầu tiên của bạn, hãy nhấp vào "*Xác nhận liên kết thiết bị*" để cho phép kết nối.



![Image](assets/fr/28.webp)



Trên thiết bị thứ hai, hãy hoàn tất quy trình bằng cách nhấp vào "*Liên kết thiết bị*".



![Image](assets/fr/29.webp)



Bây giờ bạn có thể truy cập tất cả "*Phòng*" và các cuộc trò chuyện của mình từ thiết bị mới này.



![Image](assets/fr/30.webp)



Xin chúc mừng, giờ bạn đã nắm được cách sử dụng Keet messaging, một giải pháp thay thế tuyệt vời cho WathsApp! Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Hãy thoải mái chia sẻ hướng dẫn này trên các mạng xã hội của bạn. Cảm ơn bạn rất nhiều!



Tôi cũng giới thiệu cho bạn hướng dẫn khác này, trong đó tôi giới thiệu cho bạn Proton Mail, một giải pháp thay thế thân thiện hơn nhiều với quyền riêng tư cho Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2