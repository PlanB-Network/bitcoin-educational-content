---
name: Chất độc
description: Mở ra các cuộc trò chuyện không cần trung gian trên giao thức Tox phi tập trung
---
![cover](assets/cover.webp)



Mã hóa đầu cuối là một dịch vụ được cung cấp bởi nhiều ứng dụng nhắn tin như WhatsApp và Telegram. Mã hóa ở đây có nghĩa là trước khi người gửi gửi tin nhắn, tin nhắn được bảo mật bằng một khóa mật mã mà chỉ người nhận mới có khóa. Hôm nay, chúng ta sẽ cùng khám phá một ứng dụng nhắn tin hoàn toàn phi tập trung, được mã hóa đầu cuối, dựa trên các nguyên tắc tương tự như Blockchain, nhằm cung cấp giao tiếp an toàn, được mã hóa đầu cuối mà không cần trung gian: Tox Chat.



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
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Mã hóa đầu cuối*



## Tox là gì?



Tox là một giao thức truyền thông phi tập trung (mã nguồn mở) miễn phí, sử dụng công nghệ *Thư viện Mạng và Mật mã* (NaCl) cùng với sự kết hợp của các thuật toán mã hóa để đảm bảo an ninh và bảo mật cho người dùng. Tox cho phép bạn nhắn tin văn bản Exchange, thực hiện cuộc gọi thoại và video, chia sẻ tệp và chia sẻ màn hình với bạn bè một cách an toàn, phi tập trung và không cần trung gian.



Công nghệ mà giao thức Tox sử dụng tương tự như các mạng ngang hàng như blockchain, ưu tiên tính phi tập trung của cơ sở hạ tầng giao thức. Không giống như mạng xã hội và các ứng dụng nhắn tin được mã hóa đầu cuối, ứng dụng Tox Chat được xây dựng trên một giao thức phi tập trung, không có máy chủ trung tâm. Tất cả người dùng giao tiếp trong một mạng ngang hàng không có trung gian, chống kiểm duyệt. Để giao tiếp, mỗi người dùng được xác định bằng một ID duy nhất (ToxID) bắt nguồn từ khóa công khai của người đó, được lưu trữ trong bảng Hash phân tán.



## Tham gia Tox



Bạn có thể sử dụng giao thức Tox thông qua ứng dụng nhắn tin tức thời mà bạn có thể tải xuống từ [trang web Tox Chat](https://tox.chat).



![download](assets/fr/01.webp)



Tùy thuộc vào hệ điều hành của bạn, bạn có thể tải xuống và cài đặt ứng dụng khách Tox phù hợp với:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), một ứng dụng khách Tox được viết bằng Kotlin chỉ có trên Android



![aTox](assets/fr/02.webp)





- qTox: Một ứng dụng khách Tox từ [mã nguồn mở](https://github.com/TokTok/qTox) dựa trên Qt Framework (C++) có sẵn trên Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) là một ứng dụng khách Tox được viết bằng C và chạy trên các hệ thống có giao diện dòng lệnh.



![Toxic](assets/fr/04.webp)



Trong hướng dẫn này, chúng ta sẽ sử dụng ứng dụng khách qTox trên Windows và aTox để giao tiếp.



## Bắt đầu với qTox



Sau khi tải xuống, hãy cài đặt ứng dụng Tox và tạo hồ sơ của bạn.



![qTox-acount](assets/fr/05.webp)



Xin chúc mừng, bạn vừa tham gia giao thức Tox. Trên phần mềm qTox, bạn có thể tìm thông tin hồ sơ của mình bằng cách nhấp vào tên người dùng.



![profil](assets/fr/06.webp)



Đặc biệt, bạn sẽ tìm thấy ID Tox của mình, có thể lưu dưới dạng mã QR và chia sẻ với những người muốn liên hệ với bạn.



Xuất tệp hồ sơ Tox của bạn để có bản sao lưu hồ sơ và thông tin liên hệ mà bạn có thể sử dụng để khôi phục. Nhấp vào nút **Xuất**, sau đó chọn đường dẫn đến tệp sao lưu.



![export](assets/fr/07.webp)



Từ menu **Thêm**, thêm bạn bè, nhập danh bạ và quản lý các yêu cầu kết bạn mà bạn nhận được.



![friends](assets/fr/08.webp)



Bạn có thể liên hệ với tôi qua ID Tox này, ví dụ: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Sau khi yêu cầu kết bạn được gửi đi, người nhận sẽ phải chấp nhận hoặc từ chối yêu cầu của bạn trước khi bạn có thể liên hệ với họ.



![request](assets/fr/09.webp)



Ứng dụng Tox của bạn bao gồm tất cả các tùy chọn mà ứng dụng nhắn tin tức thời cung cấp:





- Cuộc gọi video





- Cuộc gọi thoại





- Chia sẻ tập tin





- biểu tượng cảm xúc



![chat](assets/fr/10.webp)



### Nhóm ngang hàng



Khách hàng Tox của bạn cũng cho phép bạn giao tiếp với một nhóm người theo cách hoàn toàn phi tập trung: đây được gọi là hội nghị. Trong menu **Nhóm**, hãy tạo một hội nghị mới hoặc xem danh sách lời mời tham gia hội nghị mà bạn đã nhận được.



![conferences](assets/fr/11.webp)



Sau khi tạo xong hội nghị, bạn có thể mời bạn bè tham gia hội nghị trên máy khách Tox. Trong danh sách bạn bè, nhấp chuột phải vào tên người dùng của người bạn muốn mời. Nhấp vào tùy chọn **Mời tham gia hội nghị**, sau đó chọn tên hội nghị bạn đã tạo. Bạn cũng có thể mời bạn bè bằng cách tự động tạo hội nghị với tùy chọn **Tạo hội nghị mới**.



⚠️ Các ứng dụng khách Tox vẫn đang trong quá trình phát triển, vì vậy bạn có thể gặp lỗi khi tương tác với phần mềm. Các chức năng hội nghị truyền hình và gọi video hiện chưa khả dụng trên ứng dụng khách Tox Android (aTox).



![invite](assets/fr/12.webp)



### Chuyển tập tin



Trong menu **Chuyển tệp**, bạn sẽ tìm thấy lịch sử các tệp bạn đã gửi và các tệp bạn đã nhận từ danh bạ của mình.



![files](assets/fr/13.webp)



Bạn cũng có thể tùy chỉnh cấu hình chia sẻ tệp cho từng cuộc thảo luận. Nhấp chuột phải vào tên người dùng của người nhận và chọn "Hiển thị thêm chi tiết".



![details](assets/fr/14.webp)



Từ thông tin chi tiết của Interface, bạn có thể quản lý các quyền mà bạn cấp cho người nhận đối với:





- Tự động chấp nhận lời mời tham dự hội nghị.





- Tự động chấp nhận tập tin.





- Đường dẫn sao lưu cho các tập tin thảo luận của bạn.



![permissions](assets/fr/15.webp)



### Thêm thông số



Trong menu **Cài đặt**, bạn có thể tùy chỉnh cài đặt của ứng dụng khách Tox.





- Trong phần **Chung**, hãy thay đổi ngôn ngữ cơ bản của ứng dụng khách Tox, xác định đường dẫn sao lưu tệp và kích thước tệp tối đa được chấp nhận tự động.



![general](assets/fr/16.webp)





- Trong phần **Người dùng Interface**, hãy chỉnh sửa phông chữ và kích thước tin nhắn. Bạn cũng có thể thay đổi giao diện của ứng dụng Tox.



![ui](assets/fr/17.webp)





- Thẻ **Quyền riêng tư** cho phép bạn định nghĩa tin nhắn tạm thời bằng cách bỏ chọn hộp "Giữ lịch sử trò chuyện". Bạn cũng có thể thay đổi mã Nospam khi nhận thấy mình đang bị spam bởi các yêu cầu kết bạn bằng cách nhấp vào nút "Mã Nospam ngẫu nhiên generate".



![privacy](assets/fr/18.webp)



### Điều gì đảm bảo tính bảo mật của Tox?



Giao thức Tox sử dụng Bảng Hash Phân tán để tạo ra một mạng lưới các nút phi tập trung. Mỗi máy khách Tox là một phần của mạng DHT và lưu trữ thông tin về các nút khác. Trong trường hợp của Tox, DHT lưu trữ địa chỉ IP dưới dạng giá trị được liên kết với khóa công khai Tox (Tox ID). Điều này giúp dễ dàng tìm kiếm thiết bị máy khách Tox mà không cần phải truy vấn máy chủ trung tâm.



Hãy tưởng tượng việc viết thư cho người dùng `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` của chúng ta, người mà chúng ta sẽ đặt tên là **người dùng B**. Máy khách Tox của bạn sẽ định vị mã định danh này trong bảng Phân tán Hash và truy xuất IP Address được liên kết. Sau khi tìm thấy IP Address, máy khách Tox của bạn sẽ tạo một kênh giao tiếp trực tiếp, được mã hóa với máy của **người dùng B**, hoặc sử dụng các nút khác làm rơle để liên lạc với **Người dùng B**. Các thuật toán mã hóa đảm bảo rằng, bất kể kênh giao tiếp nào, chỉ **Người dùng B** mới có thể đọc được nội dung tin nhắn của bạn.



Nếu bạn thích khám phá Tox và hiểu được lợi ích của nó trong việc tăng cường bảo mật quyền riêng tư, vui lòng đánh giá cao hướng dẫn này. Chúng tôi cũng đề xuất bạn tham khảo hướng dẫn về Simple Login, một công cụ cho phép bạn nhận và gửi email ẩn danh.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41