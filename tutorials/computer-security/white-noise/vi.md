---
name: White Noise
description: Một ứng dụng nhắn tin riêng tư, phi tập trung dựa trên giao thức Nostr và MLS.
---

![cover](assets/cover.webp)




## Giới thiệu



"Trong khó khăn luôn ẩn chứa cơ hội". Câu nói này của Albert Einstein nhắc nhở chúng ta rằng vấn đề không phải là dứt khoát, mà luôn chứa đựng mầm mống của những giải pháp mới, sáng tạo.



Những động lực đằng sau sự ra mắt của giải pháp mà chúng tôi trình bày trong hướng dẫn này minh họa điều đó một cách hoàn hảo. Đó là **White Noise**, ra đời từ nhu cầu cấp thiết.



Theo lời người sáng lập, Max Hillebrand, được *Tạp chí Bitcoin* đưa tin: "Chúng tôi khởi động dự án này vì không có lựa chọn nào khác." Ông giải thích rằng "các ứng dụng mã hóa hiện có hoạt động không hiệu quả trên quy mô lớn: thêm 100 người vào một cuộc trò chuyện nhóm sẽ làm chậm quá trình mã hóa đáng kể. Trong khi đó, các nền tảng phi tập trung lại không cung cấp tính năng nhắn tin riêng tư. Cuối cùng, mạng lưới chuyển tiếp mở của Nostr cho phép mọi người lan truyền ý tưởng, nhưng việc bảo vệ tin nhắn trực tiếp vẫn còn rất thiếu sót. Chúng tôi nhận ra: để bảo vệ tự do, chúng tôi phải kết hợp các hệ thống này."



## White Noise là gì?



White Noise là một ứng dụng nhắn tin mã nguồn mở được phát triển bởi một nhóm phi lợi nhuận. Ứng dụng này thúc đẩy tính bảo mật, quyền riêng tư và tính phi tập trung. Không giống như các ứng dụng thông thường, nó không yêu cầu số điện thoại hay địa chỉ email.


White Noise nổi bật nhờ sự tích hợp của hai giao thức cơ bản - Nostr và MLS - tạo nên nền tảng kỹ thuật của nó.



Nostr (Notes and Other Stuff Transmitted by Relays) là một giao thức phi tập trung, mã nguồn mở được thiết kế để chống lại sự kiểm duyệt. Giao thức này sử dụng các máy chủ chuyển tiếp, cặp khóa và máy khách.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Với White Noise, bạn thậm chí có thể chọn cài đặt rơle riêng để tối đa hóa sự riêng tư.



Mặt khác, MLS (Messaging Layer Security) là một giao thức bảo mật cho phép mã hóa đầu cuối các tin nhắn. Nói cách khác, tin nhắn chỉ có thể được truy cập tại các điểm cuối, tức là người gửi và người nhận tin nhắn. Điều này có nghĩa là các máy chuyển tiếp tham gia vào việc định tuyến tin nhắn không thể truy cập nội dung của chúng.



Dưới đây là bảng so sánh nhanh giữa White Noise và một số ứng dụng nhắn tin nổi tiếng nhất.



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## Bắt đầu với White Noise



### Lắp đặt White Noise



Hãy truy cập trang web [White Noise](https://www.whitenoise.chat/), sau đó nhấp vào **Tải xuống**.



![screen](assets/fr/03.webp)



White Noise hiện chỉ có sẵn trên các thiết bị di động.


Trên giao diện mới hiện ra, hãy nhấn:





- Nhấn vào nút **Zapstore** hoặc **Android APK** nếu bạn muốn tải xuống trên Android;
- Nhấp vào nút **iOS TestFlight** nếu bạn đang sử dụng iPhone.



![screen](assets/fr/04.webp)



Trong hướng dẫn này, chúng ta sẽ tiến hành tải xuống ứng dụng cho Android.


Nếu bạn chọn tải xuống qua **Zapstore**, bạn sẽ được chuyển hướng đến trang này. Sau khi vào Zapstore, hãy nhập **White Noise** vào thanh tìm kiếm. Sau đó tiến hành tải xuống bằng cách nhấp vào **Cài đặt**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Nếu bạn chọn tải xuống tệp APK, bạn sẽ được chuyển hướng đến kho lưu trữ GitHub của White Noise để chọn phiên bản phù hợp với điện thoại thông minh của mình.



Các tệp APK hiện có là:





- whitenoise-0.2.1-arm64-v8a.apk** (57.7 MB), phù hợp với các điện thoại đời mới có bộ xử lý 64-bit;
- whitenoise-0.2.1-armeabi-v7a.apk** (47.5 MB) phù hợp với các điện thoại đời cũ có bộ xử lý 32-bit.



Bạn cũng có các tệp **.sha256**, đây chỉ là mã kiểm tra để xác minh tính toàn vẹn của tệp tải xuống.



![screen](assets/fr/07.webp)



Sau khi quá trình tải xuống hoàn tất, hãy cài đặt và mở ứng dụng.



![screen](assets/fr/08.webp)



### Thiết lập tài khoản người dùng ban đầu



Để kết nối lần đầu với White Noise, hãy nhấn nút **Đăng ký**.



![screen](assets/fr/09.webp)



Tiếp theo, hãy thiết lập hồ sơ của bạn bằng cách chọn ảnh đại diện, tên và thêm một đoạn mô tả ngắn về bản thân. Bạn không cần phải điền thông tin nhận dạng thật của mình (tên và ảnh).


Lưu ý rằng White Noise sẽ tự động chọn một tên (bí danh) cho bạn, bạn có thể giữ nguyên hoặc thay đổi tên này. Cuối cùng, nhấn nút **Kết thúc**.



![screen](assets/fr/10.webp)



Bạn sẽ được chuyển hướng đến **màn hình chính** của White Noise, nơi hiển thị danh sách các cuộc trò chuyện của bạn. Tài khoản của bạn hiện đã được thiết lập và sẵn sàng sử dụng. Bạn có thể chia sẻ hồ sơ của mình hoặc tìm kiếm bạn bè để bắt đầu trò chuyện.



![screen](assets/fr/11.webp)




### Khám phá các giao diện White Noise



Trên giao diện chính, ở phía trên cùng của màn hình, bạn sẽ thấy:



Ở góc trên bên trái, biểu tượng hồ sơ là hình thu nhỏ của ảnh đại diện hoặc chữ cái đầu tiên của tên hồ sơ của bạn. Nhấp vào đó để truy cập cài đặt tài khoản.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



Ở góc trên bên phải, bạn sẽ thấy biểu tượng để bắt đầu một cuộc trò chuyện mới.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Cài đặt tài khoản người dùng



Nhấn vào biểu tượng hồ sơ ở góc trên bên trái để truy cập cài đặt.



![screen](assets/fr/16.webp)



Ở đầu giao diện **Cài đặt**, bạn sẽ thấy ảnh đại diện và tên hồ sơ của mình, tiếp theo là khóa công khai, mà bạn có thể chia sẻ bằng mã QR bên cạnh.



![screen](assets/fr/17.webp)



Ngay bên dưới, bạn sẽ thấy nút **Thay đổi tài khoản**, cho phép bạn kết nối với một hồ sơ khác trong ứng dụng.



![screen](assets/fr/18.webp)



Sau đó, bạn có phần đầu tiên với bốn (4) menu phụ như sau:





- Chỉnh sửa hồ sơ**



Trong menu phụ này, bạn có thể chỉnh sửa tên hồ sơ, địa chỉ Nostr (NIP-05)... Đừng quên nhấn vào **Lưu** để lưu các thay đổi của bạn.



![screen](assets/fr/19.webp)





- Khóa hồ sơ**



Tại đây bạn có thể truy cập vào khóa công khai và khóa riêng tư (bí mật) của mình. Như White Noise đã nhắc nhở, khóa riêng tư của bạn không được tiết lộ trong bất kỳ trường hợp nào.



![screen](assets/fr/20.webp)





- Rơle nguồn



Trong menu phụ này, bạn có thể thêm hoặc xóa **rơle chung** (rơle được định nghĩa để sử dụng trong tất cả các ứng dụng Nostr của bạn), **rơle hộp thư đến** và **rơle gói khóa**.



Để làm vậy, hãy nhấn vào biểu tượng **thùng rác** phía trước một rơle để xóa nó, hoặc nhấn vào biểu tượng **+** (dấu cộng) để thêm một rơle mới.



![screen](assets/fr/21.webp)





- Đang ngắt kết nối**



Nhấp vào menu phụ này để ngắt kết nối tài khoản của bạn khỏi ứng dụng. Nhưng hãy chắc chắn rằng bạn đã lưu khóa riêng tư của mình ngoại tuyến, nếu không bạn sẽ không thể đăng nhập lại sau này.



![screen](assets/fr/22.webp)




Phần thứ hai cung cấp các menu phụ:





- Cài đặt ứng dụng



Tại đây, bạn có thể tùy chỉnh giao diện (chủ đề và ngôn ngữ hiển thị) của ứng dụng, thậm chí xóa dữ liệu nếu cảm thấy dữ liệu đã bị xâm phạm hoặc nếu chính bạn cảm thấy mình đang gặp rủi ro.



![screen](assets/fr/23.webp)





- Quyên góp cho White Noise



Bạn có thể hỗ trợ nhóm đứng sau White Noise (một tổ chức phi lợi nhuận) bằng cách quyên góp thông qua địa chỉ Lightning hoặc địa chỉ thanh toán ẩn danh Bitcoin của họ.



![screen](assets/fr/24.webp)



Cuối cùng, ở phía dưới cùng là **cài đặt dành cho nhà phát triển**.



![screen](assets/fr/25.webp)




## Bắt đầu một cuộc trò chuyện



Giờ chúng ta hãy cùng xem cách bắt đầu một cuộc trò chuyện. Tại thời điểm viết bài này, White Noise cung cấp ba tùy chọn giao tiếp. Lần lượt, chúng ta sẽ tìm hiểu về **Trò chuyện riêng tư** (**Trò chuyện 1:1**), tức là chỉ giữa bạn và một người khác, **Trò chuyện nhóm** và **Gửi tệp đa phương tiện**.




### Mèo 1:1



Từ giao diện chính, để thêm người liên lạc mới, hãy nhấp vào biểu tượng bắt đầu cuộc trò chuyện mới.


Sau đó, quét mã QR của khóa công khai (1) hoặc dán khóa công khai (2) của người liên lạc mới của bạn vào thanh tìm kiếm để tìm người đó.



![screen](assets/fr/26.webp)



Sau đó, nhấn vào nút **Bắt đầu cuộc trò chuyện** để bắt đầu cuộc trò chuyện với người bạn muốn liên lạc. Bạn cũng có thể **Theo dõi** người bạn đó hoặc mời họ tham gia cuộc trò chuyện nhóm bằng cách nhấn vào nút **Thêm vào nhóm**.



![screen](assets/fr/27.webp)



Tin nhắn đầu tiên bạn gửi cho một người liên lạc mới giống như một lời mời. Lời mời này phải được người nhận chấp nhận trước khi bạn có thể liên lạc với họ. Nếu họ từ chối, thì cuộc trò chuyện sẽ không thể diễn ra.



![screen](assets/fr/28.webp)



Hơn nữa, chừng nào họ chưa chấp nhận lời mời của bạn, họ sẽ không thể đọc được nội dung tin nhắn đầu tiên của bạn.



Khi anh ấy chấp nhận lời mời của bạn, anh ấy có thể trả lời lại và hai người có thể giao tiếp liền mạch và an toàn.



![screen](assets/fr/29.webp)



Hơn nữa, trong một cuộc thảo luận, bạn còn có thêm các chức năng bổ sung.



Bạn có thể nhấn giữ vào một tin nhắn cụ thể để hiển thị các tùy chọn như:




- phản hồi lại tin nhắn bằng biểu tượng cảm xúc (1) ;
- tạo một **trích dẫn trực tiếp** để trả lời tin nhắn bằng cách nhấn **Trả lời** (2) ;
- sao chép tin nhắn bằng cách nhấn **Sao chép** (3).



![screen](assets/fr/30.webp)





- Chỉ xóa tin nhắn bằng nút **Xóa** nếu tin nhắn đó do bạn gửi.



![screen](assets/fr/31.webp)



Bạn có thể tìm kiếm trong một cuộc hội thoại.



Nhấp vào ảnh đại diện của người liên lạc ở đầu màn hình để truy cập "thông tin cuộc trò chuyện" và nhấn vào nút **Tìm kiếm trong cuộc trò chuyện**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



Trong thanh tìm kiếm hiện ra, nhập từ bạn muốn tìm và bắt đầu tìm kiếm. Sau đó, bạn sẽ thấy các từ khóa tìm kiếm được tô đậm.



![screen](assets/fr/34.webp)




### Cuộc trò chuyện nhóm



Bạn có thể tạo nhóm trò chuyện trên White Noise.



Để thực hiện việc này, hãy chạm vào biểu tượng trong giao diện khởi tạo cuộc trò chuyện mới, sau đó nhấp vào **Cuộc trò chuyện nhóm mới**. Tiếp theo, trong thanh tìm kiếm, nhập khóa công khai của thành viên đầu tiên bạn muốn thêm vào nhóm.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Cuối cùng, nếu tùy chọn này không hiệu quả, từ giao diện **Bắt đầu cuộc trò chuyện mới**, hãy nhập khóa công khai của thành viên đầu tiên bạn muốn thêm vào nhóm vào thanh tìm kiếm. Bạn cũng có thể quét mã QR liên kết với khóa công khai của người đó.



Lần này, thay vì nhấn vào nút **Bắt đầu cuộc trò chuyện**, hãy nhấn vào nút **Thêm vào nhóm**.



![screen](assets/fr/37.webp)



Trên menu bật lên, hãy nhấn vào **Tạo cuộc trò chuyện nhóm mới**.



![screen](assets/fr/38.webp)



Sau đó nhấn **Tiếp tục** (bạn không cần nhập lại khóa công khai).



![screen](assets/fr/39.webp)



Với tư cách là người tạo nhóm, bạn tự động trở thành quản trị viên của nhóm. Hãy điền thông tin chi tiết về nhóm, chẳng hạn như **tên nhóm và mô tả**, sau đó nhấp vào nút **Tạo nhóm**.



![screen](assets/fr/40.webp)



Người dùng bạn thêm vào với tư cách thành viên đầu tiên, và bất kỳ người dùng nào khác bạn thêm sau đó, sẽ nhận được thông báo mời họ tham gia nhóm. Họ phải chấp nhận bằng cách nhấp vào **Chấp nhận** để tham gia nhóm.



![screen](assets/fr/41.webp)



Bạn cũng có thể thêm một thành viên mới mà bạn đang trò chuyện cùng vào nhóm hiện có. Để làm vậy, hãy nhấp vào ảnh đại diện của người bạn đang trò chuyện ở đầu màn hình để truy cập "thông tin cuộc trò chuyện" và nhấn vào nút **Thêm vào nhóm**.



![screen](assets/fr/42.webp)



Trên giao diện mới hiện ra, **hãy chọn** nhóm bạn muốn thêm người đó vào và nhấn vào **Thêm vào nhóm**. Sau đó chỉ cần đợi người đó đồng ý tham gia nhóm.



![screen](assets/fr/43.webp)



Lưu ý rằng chỉ quản trị viên nhóm mới có thể chỉnh sửa thông tin nhóm và thêm hoặc xóa thành viên. Ngoài ra, việc xoay vòng khóa ngăn chặn các thành viên bị cấm giải mã tin nhắn trong tương lai.



Để xóa một thành viên, từ giao diện chính của nhóm, hãy nhấn vào biểu tượng nhóm ở trên cùng để truy cập giao diện thông tin nhóm.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Sau đó nhấp vào tên thành viên và **Xóa khỏi nhóm**. Từ giao diện này, bạn cũng có thể gửi tin nhắn cho người đó, theo dõi người đó hoặc thêm người đó vào nhóm khác.



![screen](assets/fr/46.webp)



### Gửi các tệp đa phương tiện



Hiện tại, chỉ có thể chia sẻ ảnh giữa các người dùng trên White Noise. Cho dù bạn đang trong cuộc trò chuyện riêng tư hay nhóm chat, để chia sẻ ảnh, bạn cần thực hiện các bước sau:





- Nhấn vào biểu tượng **cộng (+)** ở phía bên trái của ô nhập tin nhắn.



![screen](assets/fr/47.webp)





- Sau đó nhấp vào ô có nhãn **Ảnh** ở phía dưới để truy cập vào thư viện ảnh của bạn.



![screen](assets/fr/48.webp)





- Hãy chọn (các) ảnh bạn muốn gửi.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Những điểm chính cần ghi nhớ



White Noise cung cấp mức độ bảo mật và tính riêng tư tốt. Mặt khác, đây là một ứng dụng rất mới, chưa được sử dụng rộng rãi và vẫn còn trong giai đoạn sơ khai. Do đó, còn quá sớm để đưa ra bất kỳ kết luận chắc chắn nào. Có thể gặp một vài sự cố trong quá trình sử dụng.



Hiện tại, so với các ứng dụng nhắn tin phổ biến, ứng dụng này còn thiếu một số chức năng (không có cuộc gọi thoại hoặc video, không thể gửi các tệp đa phương tiện âm thanh hoặc video).



Tuy nhiên, White Noise vẫn là một lựa chọn thú vị cho các cuộc trò chuyện mà tính bảo mật là tối quan trọng (ví dụ: với gia đình, bạn bè thân thiết hoặc các nhà hoạt động vì một mục tiêu chung), ngay cả khi nó đòi hỏi một chút nỗ lực để cài đặt (thông qua các cửa hàng ứng dụng thay thế hoặc tệp APK) và học cách sử dụng (nắm vững một chút khái niệm về cặp khóa, máy khách và máy chuyển tiếp với giao thức Nostr).



Giờ bạn đã biết cách sử dụng White Noise để liên lạc an toàn với bạn bè và gia đình. Hãy nhấn nút thích nếu bạn thấy hướng dẫn này hữu ích.



Chúng tôi khuyên bạn nên tham khảo hướng dẫn của chúng tôi về Tox Chat, một ứng dụng cho phép bạn trò chuyện trực tiếp thông qua giao thức phi tập trung Tox.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3