---
name: Session
description: Gửi tin nhắn được mã hóa, không phải siêu dữ liệu
---
![cover](assets/cover.webp)



Session là một ứng dụng nhắn tin được mã hóa được tạo ra vào năm 2020, được thiết kế để cung cấp mức độ bảo mật cao hơn so với nhắn tin truyền thống. Ứng dụng này được phát triển lần đầu tiên bởi *Oxen Privacy Tech Foundation*, sau đó là *Session Technology Foundation*.



Session tự hào có một số tính năng kỹ thuật thú vị: mã hóa đầu cuối của tin nhắn, một mạng phi tập trung được tổ chức để đảm bảo tính khả dụng và dự phòng, và định tuyến onion lấy cảm hứng từ Tor. Ngoài ra, không giống như WathsApp hoặc Signal, yêu cầu số điện thoại để đăng ký, Session không yêu cầu thông tin cá nhân (không số, không email, chỉ một cặp khóa mật mã).



Session cho phép bạn gửi tin nhắn, tệp, tin nhắn thoại, cuộc gọi âm thanh cũng như nhóm lên tới 100 thành viên (và cộng đồng lớn hơn thế), đồng thời giảm thiểu rò rỉ siêu dữ liệu.



![Image](assets/fr/01.webp)



Phiên bản này chủ yếu hướng đến những người dùng coi trọng tính bảo mật. Dịch vụ nhắn tin này là một sự thay thế nghiêm túc cho WhatsApp, với kiến trúc được thiết kế để chống lại các mô hình giám sát hiện đại.



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
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Mã hóa đầu cuối*



## Cài đặt ứng dụng Session



Phiên bản này có sẵn trên mọi nền tảng. Bạn có thể tải ứng dụng trực tiếp từ cửa hàng ứng dụng trên điện thoại của mình:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [Cửa hàng ứng dụng](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



Trên Android, bạn cũng có thể [cài đặt qua APK](https://github.com/session-foundation/session-android/releases).



Trong hướng dẫn này, chúng tôi sẽ tập trung vào phiên bản di động, nhưng xin lưu ý rằng [phiên bản máy tính cũng khả dụng](https://getsession.org/download) (MacOS, Linux và Windows). Sau đó, chúng tôi sẽ xem cách đồng bộ hóa tài khoản trên nhiều thiết bị.



## Tạo một tài khoản trên Session



Khi khởi chạy lần đầu, hãy nhấp vào "*Tạo tài khoản*".



![Image](assets/fr/02.webp)



Chọn tên hiển thị cho hồ sơ của bạn. Tên này có thể là bút danh hoặc tên thật của bạn.



![Image](assets/fr/03.webp)



Sau đó, bạn sẽ phải chọn giữa hai chế độ quản lý thông báo:





- Chế độ nhanh ("*Firebase Cloud Messaging/Apple Push Notification Service*"): cho phép bạn nhận thông báo tin nhắn gần như theo thời gian thực, nhờ vào các dịch vụ thông báo do Google hoặc Apple cung cấp (tùy thuộc vào hệ thống của bạn). Để làm được điều này, IP Address của bạn và ID thông báo duy nhất được truyền đến Google hoặc Apple và ID tài khoản Phiên cũng được đăng ký với máy chủ STF (qua Tor). Chế độ này liên quan đến việc tiết lộ siêu dữ liệu (thừa nhận là tối thiểu), nhưng không làm ảnh hưởng đến nội dung tin nhắn hoặc danh bạ, và không cho phép theo dõi hoạt động thực tế của bạn. Do đó, chế độ này hiệu quả hơn về khả năng phản hồi, nhưng dựa vào cơ





- Chế độ chậm (**background polling**): Ứng dụng Session vẫn hoạt động ở chế độ nền, định kỳ thăm dò mạng để tìm tin nhắn mới. Cách tiếp cận này đảm bảo tính bảo mật cao hơn so với cách đầu tiên, vì không có dữ liệu nào được truyền đến máy chủ của bên thứ ba; cả máy chủ Google, Apple và STF đều không nhận được bất kỳ thông tin nào. Mặt khác, chế độ này có hai nhược điểm: thông báo có thể bị trì hoãn (lên đến vài phút) và mức tiêu thụ năng lượng thường cao hơn do hoạt động của ứng dụng ở chế độ nền.



![Image](assets/fr/04.webp)



Bây giờ bạn đã kết nối với ứng dụng Session và có thể bắt đầu trao đổi tin nhắn.



![Image](assets/fr/05.webp)



## Lưu tài khoản Phiên của bạn



Điều đầu tiên cần làm trước khi bạn bắt đầu sử dụng Session là lưu tài khoản của bạn để bạn có thể khôi phục lại nếu bạn mất thiết bị. Để thực hiện việc này, hãy nhấp vào nút "*Tiếp tục*" bên cạnh "*Lưu mật khẩu khôi phục*".



![Image](assets/fr/06.webp)



Sau đó, Session sẽ hiển thị cụm từ Mnemonic. Hãy sao chép cẩn thận và giữ ở nơi an toàn. Cụm từ này cung cấp quyền truy cập đầy đủ vào tài khoản Session của bạn, vì vậy điều quan trọng là không được tiết lộ. Bạn sẽ cần cụm từ này để truy cập tài khoản của mình trên một thiết bị khác, đặc biệt là nếu điện thoại hiện tại của bạn bị mất hoặc bị thay thế.



![Image](assets/fr/07.webp)



Cụm từ này hoạt động theo cách tương tự như cụm từ Mnemonic được sử dụng trong danh mục đầu tư Bitcoin. Do đó, tôi khuyên bạn nên tham khảo hướng dẫn khác này, trong đó tôi giải thích các biện pháp thực hành tốt nhất để lưu cụm từ Mnemonic:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Xin lưu ý**: Không giống như các cụm từ Mnemonic được sử dụng trong danh mục đầu tư Bitcoin, trong Session, **bạn hoàn toàn phải lưu toàn bộ từng từ**. 4 chữ cái đầu tiên là không đủ!



## Thiết lập ứng dụng Phiên



Để truy cập cài đặt ứng dụng, hãy nhấp vào ảnh hồ sơ của bạn ở góc trên bên trái của Interface. Đây là nơi bạn có thể thêm ảnh hồ sơ.



![Image](assets/fr/08.webp)



Trong menu "*Privacy*", bạn có thể bật hoặc tắt nhiều tính năng khác nhau (hãy cẩn thận, một số tính năng có thể làm lộ IP Address của bạn). Tôi cũng khuyên bạn nên kích hoạt tùy chọn "*Lock App*", tùy chọn này yêu cầu xác thực để truy cập ứng dụng.



![Image](assets/fr/09.webp)



Trong menu "*Thông báo*", bạn sẽ thấy tùy chọn giữa "*Chế độ nhanh*" và "*Chế độ chậm*" (xem các phần trước của hướng dẫn). Bạn cũng có thể tùy chỉnh thông báo theo sở thích của mình.



![Image](assets/fr/10.webp)



Cuối cùng, hãy vào menu "*Giao diện*" để điều chỉnh Interface theo sở thích của bạn. Menu "*Mật khẩu khôi phục*" cho phép bạn khôi phục cụm từ Mnemonic nếu bạn muốn tạo bản sao lưu mới.



![Image](assets/fr/11.webp)



## Gửi tin nhắn với Phiên



Để liên hệ với người khác, hãy nhấp vào nút "**+**" trên trang chủ.



![Image](assets/fr/12.webp)



Có một số tùy chọn. Nếu bạn muốn tạo hoặc tham gia một nhóm, hãy chọn "*Tạo nhóm*" hoặc "*Tham gia cộng đồng*".



![Image](assets/fr/13.webp)



Nếu bạn muốn ai đó thêm bạn vào danh bạ, bạn có thể yêu cầu họ quét ID phiên của bạn dưới dạng mã QR.



![Image](assets/fr/14.webp)



Để gửi thông tin đăng nhập từ xa, hãy nhấp vào "*Mời bạn bè*". Sau đó, bạn có thể sao chép ID phiên của mình và gửi qua kênh liên lạc khác. Bạn cũng có thể lấy thông tin này bằng cách nhấp vào ảnh hồ sơ của mình từ trang chủ.



![Image](assets/fr/15.webp)



Nếu bạn có ID phiên của người khác và muốn thêm, hãy nhấp vào "*Tin nhắn mới*".



![Image](assets/fr/16.webp)



Sau đó, bạn có thể dán mã định danh vào văn bản hoặc quét trực tiếp nếu bạn có mã QR.



![Image](assets/fr/17.webp)



Sau đó gửi tin nhắn đầu tiên cho người này.



![Image](assets/fr/18.webp)



Ngay khi người đó chấp nhận yêu cầu của bạn, bạn sẽ thấy tên người dùng của họ xuất hiện và bạn có thể trò chuyện thoải mái với họ.



![Image](assets/fr/19.webp)



## Đồng bộ phần mềm Desktop



Để đồng bộ hóa tài khoản của bạn trên máy tính, bạn cần cài đặt phần mềm. [Tải xuống từ trang web chính thức](https://getsession.org/download). Tôi khuyên bạn nên kiểm tra tính xác thực và toàn vẹn của nó trước khi cài đặt.



![Image](assets/fr/20.webp)



Khi khởi chạy lần đầu, hãy nhấp vào "*Tôi có tài khoản*".



![Image](assets/fr/21.webp)



Nhập cụm từ Mnemonic của bạn, đảm bảo để lại khoảng cách giữa mỗi từ.



![Image](assets/fr/22.webp)



Bây giờ bạn có thể truy cập vào các cuộc trò chuyện của mình từ máy tính.



![Image](assets/fr/23.webp)



Xin chúc mừng, giờ bạn đã biết cách sử dụng tin nhắn phiên, một giải pháp thay thế tuyệt vời cho WathsApp!



Tôi cũng giới thiệu hướng dẫn khác này, trong đó tôi giới thiệu Threema, một giải pháp thay thế thú vị khác cho ứng dụng nhắn tin của bạn:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74