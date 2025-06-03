---
name: Ba mẹ
description: Nhắn tin tức thời an toàn, ẩn danh
---
![cover](assets/cover.webp)



Được thành lập vào năm 2012 tại Thụy Sĩ, Threema là một ứng dụng nhắn tin tức thời được thiết kế để đảm bảo quyền riêng tư và bảo mật. Không giống như WhatsApp, Telegram hoặc Signal, Threema không yêu cầu số điện thoại hoặc e-mail Address để tạo tài khoản. Mỗi người dùng có một mã định danh duy nhất, cho phép đăng ký hoàn toàn ẩn danh.



Về mặt kỹ thuật, thông tin liên lạc qua Threema được mã hóa từ đầu đến cuối. Mã ứng dụng di động đã là mã nguồn mở kể từ năm 2020, nhưng cơ sở hạ tầng máy chủ vẫn độc quyền và tập trung. Máy chủ được lưu trữ độc quyền tại Thụy Sĩ (một quốc gia nổi tiếng về khuôn khổ pháp lý bảo vệ dữ liệu).



![Image](assets/fr/01.webp)



Threema có các ứng dụng cơ bản dành cho Android và iOS. Ngoài ra còn có ứng dụng web cũng như phần mềm dành cho Windows, Linux và macOS. Tuy nhiên, để sử dụng chúng, trước tiên bạn phải đăng ký trên thiết bị di động.



Ứng dụng Threema không miễn phí. Nó hoạt động theo mô hình mua một lần: 5,99 € để sử dụng ứng dụng trọn đời (hoặc 4,99 € nếu bạn mua trực tiếp). Để thực sự sử dụng Threema ẩn danh, thanh toán cũng cần phải ẩn danh. Đó là lý do tại sao bạn có thể mua khóa kích hoạt bằng bitcoin hoặc tiền mặt trên "*Threema Shop*" để kích hoạt phiên bản Android. Mặt khác, trên iOS, giao dịch mua phải thông qua App Store, do hạn chế của Apple đối với việc kiếm tiền từ ứng dụng.



Ngoài ra còn có phiên bản dành riêng cho doanh nghiệp có tên là "*Threema Work*". Trong hướng dẫn này, chúng ta sẽ tập trung vào phiên bản dành cho gia đình.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| **Threema**          | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Mã hóa đầu cuối*



## Cài đặt ứng dụng Threema



Threema có sẵn trên mọi nền tảng. Bạn có thể tải ứng dụng trực tiếp từ cửa hàng ứng dụng trên điện thoại của mình:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Thư viện ứng dụng Huawei](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



Trên Android, bạn cũng có thể [cài đặt qua APK](https://shop.threema.ch/en/download).



Ngoài ra còn có [phiên bản máy tính](https://threema.ch/download) (MacOS, Linux và Windows). Hướng dẫn này sẽ chỉ cho bạn cách đồng bộ hóa chúng.



## Mua giấy phép Threema



Sau khi cài đặt ứng dụng, nếu bạn đã trực tiếp truy cập qua cửa hàng ứng dụng, bạn đã trả tiền cho giấy phép và sẽ có quyền truy cập ngay lập tức. Nếu bạn đã truy cập qua F-Droid hoặc APK, bây giờ bạn cần mua giấy phép trên trang web chính thức.



[Truy cập "*Cửa hàng Threema*"(https://shop.threema.ch/) và nhấp vào nút "*Mua Threema cho Android*".



![Image](assets/fr/02.webp)



Chọn số lượng giấy phép bạn muốn mua (chỉ một nếu chỉ dành cho bạn), chọn loại tiền tệ và chọn phương thức giao giấy phép. Bạn có thể chọn nhận giấy phép qua email hoặc trực tiếp trên trang web nếu bạn muốn ẩn danh. Sau đó nhấp vào "*Tiến hành thanh toán*".



![Image](assets/fr/03.webp)



Chọn phương thức thanh toán của bạn. Trong trường hợp của tôi, tôi sẽ thanh toán bằng bitcoin, tôi cũng khuyên bạn nên làm như vậy, vì nó cho phép bạn ẩn danh (với điều kiện bạn sử dụng Bitcoin một cách phù hợp) và thuận tiện hơn nhiều so với thanh toán bằng tiền mặt từ xa. Sau đó nhấp vào "*Tiếp theo*".



![Image](assets/fr/04.webp)



Nếu bạn không cần Invoice, hãy nhấp vào "*Tiếp theo*" một lần nữa mà không cần nhập bất kỳ thông tin cá nhân nào.



Sau đó xác nhận giao dịch mua của bạn bằng cách nhấp vào "*Xác nhận thanh toán*".



![Image](assets/fr/05.webp)



Sau đó, bạn sẽ cần gửi số tiền đã chỉ định đến Bitcoin Address đã cung cấp (thật không may, Lightning vẫn chưa được hỗ trợ). Sau khi giao dịch được xác nhận trên Blockchain, hãy nhấp vào "*Đóng*" bên cạnh Invoice.



Sau đó, bạn sẽ có quyền truy cập vào khóa cấp phép của mình. Xin lưu ý: nếu bạn chưa nhập e-mail Address, khóa này sẽ chỉ được hiển thị ở đây. Hãy nhớ lưu URL của trang để bạn có thể truy cập sau nếu cần.



![Image](assets/fr/06.webp)



## Tạo một tài khoản trên Threema



Bây giờ bạn đã có khóa cấp phép, cuối cùng bạn có thể khởi chạy ứng dụng. Khi khởi chạy lần đầu, nếu bạn chưa mua Threema qua cửa hàng ứng dụng, bạn sẽ được yêu cầu nhập khóa cấp phép đã mua trên trang web.



![Image](assets/fr/07.webp)



Sau đó nhấp vào nút "*Thiết lập ngay*".



![Image](assets/fr/08.webp)



Di chuyển ngón tay của bạn trên màn hình để generate, một nguồn entropy cần thiết để tạo ra "*Threema ID*" của bạn.



![Image](assets/fr/09.webp)



"*Threema ID*" của bạn sau đó sẽ được hiển thị. Nó sẽ cho phép bạn liên hệ với những người dùng khác. Nhấp vào "*Tiếp theo*".



![Image](assets/fr/10.webp)



Chọn một mật khẩu. Nó sẽ cho phép bạn khôi phục quyền truy cập vào tài khoản của mình khi cần thiết. Hãy tạo mật khẩu dài và ngẫu nhiên nhất có thể, và giữ một bản sao an toàn của mật khẩu, ví dụ như trong trình quản lý mật khẩu.



![Image](assets/fr/11.webp)



Sau đó chọn tên người dùng, có thể là tên thật hoặc bút danh của bạn.



![Image](assets/fr/12.webp)



Sau đó, bạn có thể liên kết ID Threema của mình với số điện thoại. Điều này giúp bạn dễ dàng tìm kiếm trong danh bạ của mình hơn, nhưng nếu bạn sử dụng Threema, điều này cũng nhằm mục đích bảo vệ tính ẩn danh của bạn: vì vậy tốt nhất là không liên kết nó. Nhấp vào "*Tiếp theo*".



![Image](assets/fr/13.webp)



Sau khi hoàn tất bước này, hãy nhấp vào "*Hoàn tất*".



![Image](assets/fr/14.webp)



Bây giờ bạn đã kết nối với Threema và có thể bắt đầu giao tiếp.



![Image](assets/fr/15.webp)



## Thiết lập Threema



Trước hết, hãy truy cập cài đặt bằng cách nhấp vào ba dấu chấm nhỏ ở góc trên bên phải, sau đó chọn "*Cài đặt*".



![Image](assets/fr/16.webp)



Trong tab "*Quyền riêng tư*", bạn sẽ tìm thấy một số tùy chọn để điều chỉnh theo nhu cầu của mình:




- Đồng bộ hóa danh bạ trên điện thoại của bạn;
- Chấp nhận tin nhắn từ người lạ;
- Chỉ báo viết trong quá trình nhập dữ liệu;
- Thông báo nhận được tin nhắn..



![Image](assets/fr/17.webp)



Trong tab "*Bảo mật*", tôi khuyên bạn nên kích hoạt tùy chọn "*Cơ chế khóa*" để bảo vệ quyền truy cập vào ứng dụng. Bạn cũng nên kích hoạt passphrase để bảo mật bản sao lưu cục bộ của mình.



![Image](assets/fr/18.webp)



Bạn có thể thoải mái khám phá các phần cài đặt khác để tùy chỉnh ứng dụng theo sở thích của mình.



![Image](assets/fr/19.webp)



## Sao lưu tài khoản Threema của bạn



Trước khi bắt đầu trao đổi tin nhắn, điều quan trọng là phải lập kế hoạch khôi phục tài khoản của bạn, đặc biệt là nếu điện thoại của bạn bị thay đổi hoặc bị mất. Để thực hiện việc này, hãy nhấp vào ba dấu chấm ở góc trên bên phải của Interface, sau đó truy cập menu "*Sao lưu*".



![Image](assets/fr/20.webp)



Tại đây bạn sẽ tìm thấy hai tùy chọn để sao lưu dữ liệu của mình:




- "*An toàn Threema*";
- "*Sao lưu dữ liệu*".



"Threema Safe* lưu tất cả thông tin tài khoản của bạn, ngoại trừ các cuộc trò chuyện, trên máy chủ của Threema. Dữ liệu này được mã hóa bằng mật khẩu bạn đã chọn khi tạo tài khoản, đảm bảo Threema không thể truy cập vào dữ liệu đó. Các bản sao lưu được thực hiện tự động và thường xuyên.



Với "*Threema Safe*", để khôi phục tài khoản của bạn trên thiết bị mới, tất cả những gì bạn cần làm là nhập "*Threema ID*" và mật khẩu của bạn. Nếu thiếu một trong hai thông tin này, bạn sẽ không thể khôi phục tài khoản của mình.



Tùy chọn này chỉ cho phép bạn lấy lại ID, hồ sơ, danh bạ, nhóm và một số cài đặt nhất định, nhưng **không phải lịch sử trò chuyện** của bạn.



Để kích hoạt "*Threema Safe*", chỉ cần kiểm tra tùy chọn trong menu "*Sao lưu*".



![Image](assets/fr/21.webp)



Nếu bạn cũng muốn sao lưu và khôi phục lịch sử trò chuyện của mình, bạn sẽ cần sử dụng tùy chọn "*Sao lưu dữ liệu*". Tùy chọn này sẽ tạo bản sao lưu đầy đủ tài khoản của bạn, được lưu trữ cục bộ trên điện thoại của bạn. Bạn sẽ cần chuyển bản sao lưu này sang thiết bị mới và sử dụng mật khẩu (và có thể là passphrase) để khôi phục toàn bộ tài khoản của mình.



Vì bản sao lưu này chỉ là cục bộ nên cần phải sao chép thường xuyên sang phương tiện bên ngoài. Nếu không, nếu thiết bị của bạn bị mất, việc khôi phục sẽ không thể thực hiện được. Do đó, phương pháp này phù hợp nhất với việc chuyển dữ liệu theo kế hoạch từ thiết bị này sang thiết bị khác, thay vì trong các tình huống khẩn cấp.



Xin lưu ý: "*Sao lưu dữ liệu*" chỉ hoạt động nếu bạn sử dụng cùng một hệ điều hành. Ví dụ, bạn sẽ không thể sử dụng nó để di chuyển từ Samsung sang iPhone.



## Tùy chỉnh hồ sơ Threema của bạn



Ở góc trên bên trái của Interface, nhấp vào ảnh hồ sơ của bạn, sau đó chọn "*Hồ sơ của tôi*".



![Image](assets/fr/22.webp)



Tại đây bạn có thể tùy chỉnh hồ sơ của mình: thêm ảnh, chọn người có thể xem ảnh hoặc xem thông tin đăng nhập Threema của bạn.



![Image](assets/fr/23.webp)



## Đồng bộ hóa phần mềm PC



Nếu bạn muốn truy cập các cuộc trò chuyện của mình trên PC, bạn có thể đồng bộ hóa tài khoản Threema của mình với phần mềm chuyên dụng. Tải xuống phần mềm cho hệ điều hành của bạn [từ trang web chính thức](https://threema.ch/en/download).



![Image](assets/fr/24.webp)



Trên điện thoại, hãy nhấp vào ba dấu chấm ở góc trên bên phải, sau đó mở menu "*Threema 2.0 dành cho máy tính để bàn*".



![Image](assets/fr/25.webp)



Nhấp vào "*Thêm thiết bị*", sau đó sử dụng điện thoại để quét mã QR được phần mềm trên máy tính hiển thị.



![Image](assets/fr/26.webp)



Để xác nhận đồng bộ hóa, hãy nhấp vào nhóm biểu tượng cảm xúc được hiển thị trong phần mềm.



![Image](assets/fr/27.webp)



Trên máy tính, hãy đăng nhập bằng mật khẩu của bạn.



![Image](assets/fr/28.webp)



Ngoài ứng dụng di động, giờ đây bạn có thể truy cập tài khoản Threema trực tiếp từ máy tính.



![Image](assets/fr/29.webp)



## Gửi tin nhắn với Threema



Bây giờ mọi thứ đã được thiết lập đúng, bạn có thể bắt đầu giao tiếp. Nhấp vào nút "*Bắt đầu trò chuyện*".



![Image](assets/fr/30.webp)



Chọn "*Liên hệ mới*".



![Image](assets/fr/31.webp)



Nhập hoặc quét "*Threema ID*" của người liên lạc với bạn.



![Image](assets/fr/32.webp)



Nhấp vào biểu tượng tin nhắn.



![Image](assets/fr/33.webp)



Gửi tin nhắn đầu tiên cho người liên lạc của bạn.



![Image](assets/fr/34.webp)



Khi người liên lạc của bạn trả lời, kết nối sẽ được thiết lập và bạn sẽ có thể thấy tên và ảnh hồ sơ của người đó. Sau đó, bạn có thể gửi tin nhắn Exchange, tệp đa phương tiện và thậm chí thực hiện cuộc gọi.



![Image](assets/fr/35.webp)



Xin chúc mừng, giờ bạn đã nắm được cách sử dụng Threema messaging, một giải pháp thay thế tuyệt vời cho WathsApp! Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Hãy thoải mái chia sẻ hướng dẫn này trên các mạng xã hội của bạn. Cảm ơn bạn rất nhiều!



Tôi cũng giới thiệu cho bạn hướng dẫn khác này, trong đó tôi giới thiệu cho bạn Proton Mail, một giải pháp thay thế thân thiện hơn nhiều với quyền riêng tư cho Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2