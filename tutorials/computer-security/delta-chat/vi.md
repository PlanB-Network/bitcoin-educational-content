---
name: Trò chuyện Delta
description: Hướng dẫn thực hành về công cụ nhắn tin phi tập trung
---

![image](assets/cover.webp)




## Giới thiệu - Kiểm soát trò chuyện và quyền riêng tư



Những năm gần đây, người ta ngày càng bàn nhiều về Kiểm soát trò chuyện (Chat Control), một đề xuất quy định nhằm mục đích triển khai việc quét tự động các tin nhắn riêng tư trên các nền tảng giao tiếp lớn. Mục tiêu được nêu ra là để chống lại nội dung bất hợp pháp, nhưng vấn đề là cơ chế này trên thực tế sẽ liên quan đến việc giám sát hàng loạt, làm suy yếu mã hóa đầu cuối và do đó làm suy yếu quyền riêng tư của tất cả người dùng, chứ không chỉ riêng những người phạm tội.



Nguy cơ thực sự là các cuộc trò chuyện trở thành môi trường bị kiểm soát, nơi mọi tin nhắn, hình ảnh hoặc tệp đính kèm đều có thể bị xem xét kỹ lưỡng trước khi đến tay người nhận. Và đây là lúc một giải pháp khả thi xuất hiện: chuyển từ các nền tảng tập trung sang các hệ thống nhắn tin phi tập trung, không phụ thuộc vào một nhà cung cấp duy nhất và không dễ bị xem xét kỹ lưỡng như vậy.



Một giải pháp như vậy sẽ được giới thiệu trong hướng dẫn này: Delta Chat. Một công cụ đã hoàn thiện và có thể sử dụng được.




## Tại sao nên chọn Delta Chat và cách thức hoạt động của nó?



Delta Chat vốn đã là một giải pháp nhắn tin rất tốt cho việc sử dụng hàng ngày: rất hữu ích để trò chuyện với bạn bè, gia đình và những người khác, giống như một phiên bản thay thế thực thụ của WhatsApp.



Đây là một hệ thống nhắn tin phi tập trung hoàn toàn dựa trên email. Về cơ bản, nó tận dụng cơ sở hạ tầng của email truyền thống, nhưng xây dựng giao diện và trải nghiệm nhắn tin tức thời hiện đại trên nền tảng đó. Thoạt nhìn, điều này có vẻ hơi ngẫu hứng, nhưng thực tế nó hoạt động rất tốt và mạnh mẽ một cách đáng ngạc nhiên. Bạn có thể sử dụng các máy chủ thư chuyên dụng có tên ChatMail, nhưng nó cũng có thể hoạt động liền mạch với các máy chủ email thông thường. Điều này có nghĩa là bạn có thể đăng nhập bằng tài khoản hiện có nếu muốn, mà không cần phải tạo bất kỳ tài khoản mới nào.



Một điểm nổi bật khác là hỗ trợ cho WebXDCs, là các ứng dụng web nhỏ có thể được sử dụng trực tiếp trong các cuộc trò chuyện, tương tự như các ứng dụng mini trong Telegram. Sự khác biệt quan trọng là các ứng dụng này không có quyền truy cập Internet, vì vậy chúng không thể theo dõi người dùng hoặc gửi dữ liệu ra bên ngoài.



Từ góc độ bảo mật, Delta Chat sử dụng mã hóa đầu cuối đã được xác thực, dựa trên PGP nhưng với các phần mở rộng hiện đại giúp nó có mức độ bảo vệ tương đương với Signal. Điểm thiếu sót hiện tại duy nhất là Perfect Forward Secrecy, nhưng đây là một khía cạnh đang được phát triển.



Do chỉ dựa vào email, Delta Chat hoàn toàn không sử dụng email:




- số điện thoại bắt buộc
- Mã định danh tập trung
- đăng ký liên kết với một dịch vụ duy nhất



Và đó là điều khiến công cụ này có khả năng chống chịu cao với các quy định xâm phạm quyền riêng tư như Kiểm soát trò chuyện.




## Lắp đặt



Từ trang web chính thức của [Delta Chat](https://delta.chat/download), bạn có thể vào mục Tải xuống. Trên Linux, phần mềm này có sẵn thông qua Flathub, nhưng cũng có các gói dành cho Arch, NixOS, Snap và các phiên bản độc lập.



![image](assets/it/01.webp)



Sản phẩm này cũng có sẵn cho:




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Cửa hàng Play](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- và các cửa hàng khác...



Nếu bạn đang tìm hướng dẫn cài đặt F-Droid, hướng dẫn này có thể giúp bạn:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Một điều rất quan trọng: phiên bản dành cho máy tính để bàn không yêu cầu điện thoại. Không giống như WhatsApp hay SimpleX Chat, bạn không cần phải đăng ký trên điện thoại trước. Bạn có thể tạo hồ sơ trực tiếp trên máy tính hoặc chuyển từ thiết bị khác.




## Tạo hồ sơ



Sau khi mở ứng dụng, Delta Chat sẽ hỏi bạn có muốn tạo hồ sơ mới hay sử dụng hồ sơ hiện có.



![image](assets/it/02.webp)



Bằng cách tạo hồ sơ mới, bạn có thể nhập:




- một cái tên
- một hình ảnh (tùy chọn)



Mặc định máy chủ ChatMail được đề xuất, nhưng bạn hoàn toàn có thể tùy chỉnh:




- Chọn một máy chủ ChatMail khác
- sử dụng tài khoản email cổ điển
- Cấu hình thủ công IMAP và SMTP
- đăng ký bằng mã mời của người dùng khác



Sau vài giây, hồ sơ đã được tạo và bạn có thể bắt đầu sử dụng ứng dụng.



![image](assets/it/03.webp)




## Interface và trò chuyện



Giao diện rất đơn giản và dễ sử dụng:




- Tin nhắn thiết bị, là các thông tin liên lạc cục bộ
- Các tin nhắn đã lưu, tương tự như trong Telegram và có thể đồng bộ hóa giữa các thiết bị



![image](assets/it/04.webp)



Để thêm liên hệ, bạn chỉ cần:




- Hiển thị mã QR của bạn
- Quan sát người kia
- Mời qua liên kết (chia sẻ liên kết mời).



![image](assets/it/05.webp)



Sau khi kết nối được thiết lập, mã hóa đầu cuối sẽ được tự động cấu hình. Giao diện người dùng của ứng dụng trò chuyện rất giống với WhatsApp:




- tin nhắn văn bản và tin nhắn thoại
- ảnh, video và tệp tin
- phản hồi tin nhắn
- phản ứng
- tin nhắn bật lên
- Thông báo có thể tùy chỉnh.



![image](assets/it/06.webp)



## WebXDC: Ứng dụng trong cuộc trò chuyện:



Delta Chat cho phép sử dụng WebXDC, tức là các ứng dụng nhỏ được nhúng trong các cuộc hội thoại. Dưới đây là danh sách ngắn những ứng dụng hữu ích nhất đã được xác định:




- khảo sát
- bảng vẽ
- trò chuyện riêng tư tạm thời
- các trò chơi có điểm trò chuyện được chia sẻ



Ngay cả những trò chơi phức tạp hơn cũng có thể được bắt đầu, điều này thể hiện tính linh hoạt của công cụ này.



![image](assets/it/07.webp)



## Nhóm, kênh và các tính năng nâng cao



Bạn có thể tạo nhóm, sử dụng nhãn dán (đặc biệt là trên màn hình máy tính) và, bằng cách kích hoạt các tùy chọn thử nghiệm, thậm chí cả các kênh, tương tự như trong Telegram.



Trong phần cài đặt nâng cao, bạn có thể bật:




- cuộc gọi thoại (vẫn đang trong giai đoạn thử nghiệm)
- quản lý hồ sơ email nâng cao
- Sao lưu toàn bộ.



![image](assets/it/08.webp)



## Đa thiết bị và sao lưu



Delta Chat hỗ trợ đầy đủ nhiều thiết bị:




- Bạn có thể thêm thiết bị thứ hai thông qua mã QR
- Bạn có thể thực hiện chuyển toàn bộ dữ liệu thông qua bản sao lưu.



Chỉ trong vài giây, bạn sẽ tìm thấy lại các cuộc trò chuyện, nhóm và toàn bộ lịch sử của mình mà không cần phụ thuộc vào máy chủ trung tâm.



![image](assets/it/09.webp)




## Phần kết luận



Trong bối cảnh ngày càng có nhiều cuộc thảo luận về việc kiểm soát thông tin liên lạc riêng tư, Delta Chat đại diện cho một giải pháp cụ thể: nhắn tin phi tập trung, mã hóa, thực sự hữu ích trong cuộc sống hàng ngày.



Trong số tất cả các giải pháp tôi đã thử, đây là giải pháp thuyết phục tôi nhất về sự đơn giản, bảo mật và tự do. Nếu muốn, bạn cũng có thể liên hệ với tôi trên Delta Chat qua [liên kết mời](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Nếu bạn thấy hướng dẫn này hữu ích, bạn có thể ủng hộ tôi bằng cách quyên góp và để lại lượt thích. Và hãy nhớ: chỉ khi sử dụng và khám phá Delta Chat trên cả thiết bị di động và máy tính để bàn, bạn mới thực sự khám phá hết chức năng của nó.



Hẹn gặp lại lần sau.