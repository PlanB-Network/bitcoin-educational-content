---
name: Ente Auth
description: Trình xác thực 2FA mã nguồn mở, được mã hóa đầu cuối
---
![cover](assets/cover.webp)



Xác thực hai yếu tố (2FA) đã trở nên không thể thiếu để bảo mật tài khoản trực tuyến của chúng ta. Ngoài mật khẩu thông thường, nó còn yêu cầu một mã tạm thời, thường được tạo bởi một ứng dụng chuyên dụng. Cơ chế này, được gọi là TOTP (Mật khẩu một lần theo thời gian), đảm bảo rằng ngay cả khi mật khẩu của bạn bị xâm phạm, kẻ tấn công sẽ không thể truy cập vào tài khoản của bạn nếu không có yếu tố thứ hai này, được gia hạn sau mỗi 30 giây.



Tuy nhiên, việc lựa chọn ứng dụng xác thực phù hợp không hề đơn giản. Google Authenticator, mặc dù phổ biến, nhưng có những hạn chế lớn: mã độc quyền không thể kiểm tra, đồng bộ hóa mà không có mã hóa đầu cuối, và nguy cơ mất toàn bộ mã trong trường hợp điện thoại gặp sự cố. Các giải pháp khác, chẳng hạn như Authy, yêu cầu số điện thoại và không đảm bảo tính bảo mật tuyệt đối.



**Ente Auth** nổi bật là một giải pháp thay thế hiện đại và an toàn. Ứng dụng đa nền tảng, mã nguồn mở, miễn phí này, được phát triển bởi đội ngũ [Ente Photos](https://ente.io), cung cấp dịch vụ sao lưu đám mây được mã hóa đầu cuối và đồng bộ hóa liền mạch giữa tất cả các thiết bị của bạn. Không giống như các giải pháp độc quyền, Ente Auth cho phép bạn kiểm soát hoàn toàn mã xác thực mà không ảnh hưởng đến quyền riêng tư.



Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn từng bước cách cài đặt và sử dụng Ente Auth và lý do tại sao giải pháp này khác với các trình xác thực truyền thống.



## Giới thiệu Ente Auth



Ente Auth được phát triển bởi đội ngũ đứng sau Ente Photos, một dịch vụ lưu trữ ảnh được mã hóa đầu cuối và bảo mật quyền riêng tư. Đúng với triết lý của Ente ("Ente" trong tiếng Malayalam có nghĩa là "của tôi", tượng trưng cho quyền kiểm soát dữ liệu của bạn), Ente Auth được thiết kế để trao lại cho người dùng toàn quyền kiểm soát mã xác thực hai yếu tố của họ.



### Các tính năng chính



**Mã TOTP tiêu chuẩn**: Ente Auth tạo mã tạm thời tương thích với hầu hết các dịch vụ (GitHub, Google, Binance, ProtonMail, v.v.). Bạn có thể thêm bao nhiêu tài khoản 2FA tùy thích và ứng dụng sẽ tính toán mã dựa trên các bí mật được cung cấp.



**Sao lưu đám mây được mã hóa đầu cuối**: Mã của bạn được lưu trữ trực tuyến an toàn. Chỉ bạn mới có thể giải mã chúng - khóa mã hóa được lấy từ mật khẩu của bạn và chỉ bạn biết. Ente (máy chủ) không biết bí mật của bạn, hay thậm chí là tên tài khoản của bạn, vì mọi thứ đều được mã hóa ở phía máy khách bằng kiến trúc không kiến thức.



**Đồng bộ hóa đa thiết bị**: Bạn có thể cài đặt Ente Auth trên nhiều thiết bị (điện thoại thông minh, máy tính bảng, máy tính) và truy cập mã của mình trên tất cả các thiết bị đó. Mọi thay đổi đều được tự động và ngay lập tức truyền đến các thiết bị khác của bạn thông qua đám mây được mã hóa, mang lại cho bạn sự linh hoạt tuyệt vời trong công việc hàng ngày.



**Interface tối giản, trực quan**: Ứng dụng cung cấp một Interface được tinh giản, dễ sử dụng ngay cả với người dùng không chuyên. Tài khoản 2FA được hiển thị với tên dịch vụ, thông tin đăng nhập và mã 6 chữ số, được cập nhật theo thời gian thực. Ente Auth cũng hiển thị mã tiếp theo trước vài giây để tránh bị thiếu hụt do hết hạn.



**Mã nguồn mở và đã được kiểm tra**: Mã nguồn của Ente Auth được công khai trên GitHub (https://github.com/ente-io/auth) theo giấy phép AGPL v3.0. Bất kỳ nhà phát triển nào cũng có thể kiểm tra mã nguồn để phát hiện lỗi hoặc hành vi không mong muốn. Mã hóa được triển khai đã được kiểm tra độc lập bên ngoài (https://ente.io/blog/cryptography-audit/), một sự đảm bảo về tính nghiêm ngặt của bảo mật ứng dụng.



### Ưu điểm và hạn chế



**Những lợi ích:**




- Quyền riêng tư được thiết kế với mã hóa đầu cuối
- Đồng bộ hóa an toàn giữa tất cả các thiết bị của bạn
- Mã nguồn mở có thể kiểm tra được
- Interface rõ ràng, trực quan cho người dùng Interface
- Tự động sao lưu để tránh mất mã
- Có sẵn trên mọi nền tảng (di động và máy tính để bàn)



**Giới hạn:**




- Cần có kết nối Internet để đồng bộ hóa
- Người dùng nâng cao có thể thích các giải pháp ngoại tuyến 100% như Aegis (chỉ dành cho Android)
- Tương đối mới so với các giải pháp đã được thiết lập



## Cài đặt



Ente Auth có sẵn trên hầu hết các nền tảng phổ biến. Bạn có thể tải ứng dụng từ [trang web chính thức](https://ente.io/auth) hoặc từ các cửa hàng chính thức.



![Installation d'Ente Auth](assets/fr/01.webp)



*Nhập trang tải xuống Auth với tất cả các nền tảng khả dụng*



### Android


Bạn có một số lựa chọn:




- **Cửa hàng Google Play**: Tìm kiếm "Ente Auth" để cài đặt cổ điển
- **F-Droid**: Có sẵn trong danh mục ứng dụng nguồn mở Android, đảm bảo tính xác thực và không có nội dung độc quyền
- **Cài đặt thủ công**: Có thể tải xuống các tệp APK từ [trang GitHub của dự án](https://github.com/ente-io/auth/releases) với thông báo tích hợp về các phiên bản mới



### iOS (iPhone/iPad)


Cài đặt Ente Auth trực tiếp từ Apple App Store bằng cách tìm kiếm tên ứng dụng. Ứng dụng iOS cũng có thể chạy trên máy Mac được trang bị chip Apple Silicon (M1/M2) thông qua Mac App Store.



### Máy tính (Windows, macOS, Linux)


Ente Auth cung cấp các ứng dụng máy tính để bàn gốc. Truy cập [ente.io/download](https://ente.io/download) hoặc [phần Phát hành trên GitHub](https://github.com/ente-io/auth/releases):





- **Windows**: Trình cài đặt EXE được cung cấp
- **macOS**: Kéo và thả ảnh đĩa DMG trong Ứng dụng
- **Linux**: Có nhiều định dạng (AppImage portable, .deb cho Debian/Ubuntu, .rpm cho Fedora/Red Hat)



**Lưu ý:** Hướng dẫn này dựa trên Ente Auth v4.4.4 trở lên. Các phiên bản trước đó có thể có một số khác biệt nhỏ so với Interface.



### Interface Web


Không cần cài đặt, bạn có thể truy cập mã của mình qua [auth.ente.io](https://auth.ente.io) từ bất kỳ trình duyệt nào. Interface web bị giới hạn ở việc xem mã (hữu ích cho việc khắc phục sự cố), vì việc thêm tài khoản yêu cầu ứng dụng di động hoặc máy tính để bàn vì lý do bảo mật.



## Cấu hình đầu tiên



### Tạo tài khoản



Khi bạn khởi chạy Ente Auth lần đầu, bạn có hai lựa chọn:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Vào màn hình chính Auth với các tùy chọn tạo tài khoản*



**Có tài khoản (khuyến nghị)**: Chọn "Tạo Tài khoản" và nhập email Address cùng mật khẩu. **Quan trọng**: mật khẩu này đóng vai trò là mật khẩu chính để mã hóa dữ liệu của bạn. Hãy chọn một mật khẩu mạnh và duy nhất, vì không có quy trình đặt lại thông thường nào mà không bị mất dữ liệu. Nếu bạn làm mất mật khẩu, dữ liệu đã mã hóa của bạn sẽ không thể khôi phục được.



**Chế độ ngoại tuyến**: Chọn "Sử dụng không cần sao lưu" để sử dụng ứng dụng cục bộ mà không cần lưu trữ đám mây. Ở chế độ này, mã của bạn vẫn được lưu trên thiết bị, nhưng bạn sẽ cần xuất chúng theo cách thủ công để tránh mất.



![Vérification email et récupération de clé](assets/fr/03.webp)



*Quy trình xác minh email và tạo khóa khôi phục 24 từ*



Bạn có thể được yêu cầu xác minh email để xác thực việc tạo tài khoản và cho phép khôi phục trên thiết bị mới. Ente Auth cũng sẽ cung cấp cho bạn một khóa khôi phục gồm 24 ký tự (dựa trên phương pháp BIP39). **Bạn phải lưu khóa này** ở nơi an toàn: đây là cách duy nhất để bạn khôi phục dữ liệu nếu quên mật khẩu.



### An ninh địa phương



Tôi thực sự khuyên bạn nên bật bảo vệ cục bộ bằng mã hoặc sinh trắc học. Vào **Cài đặt → Bảo mật → Màn hình khóa** và cấu hình:





- **Mở khóa sinh trắc học**: Face ID, vân tay tùy thuộc vào khả năng của thiết bị của bạn
- Mã PIN/mật khẩu dành riêng cho ứng dụng
- **Độ trễ khóa tự động**: ví dụ: "Ngay lập tức" hoặc sau 30 giây không hoạt động



Tính năng bảo vệ này ngăn chặn việc truy cập trái phép vào mã của bạn nếu ai đó có được quyền truy cập vào điện thoại đã mở khóa của bạn. Lưu ý rằng khóa này là một rào cản bổ sung: dữ liệu của bạn vẫn được mã hóa đầu cuối ngay cả khi không có tính năng bảo vệ này.



## Thêm tài khoản 2FA



### Quy trình chuẩn



Để thêm tài khoản 2FA mới, chúng ta hãy lấy ví dụ cụ thể về việc kích hoạt 2FA trên Bull Bitcoin:



![Configuration du premier compte](assets/fr/04.webp)



*Interface chính của Ente Auth đã sẵn sàng thêm tài khoản 2FA đầu tiên*



**Phía dịch vụ (Bull Bitcoin)**: Đăng nhập vào tài khoản Bull Bitcoin của bạn, vào phần cài đặt bảo mật và bật xác thực hai yếu tố.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* menu cài đặt bảo mật



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Tùy chọn bật xác thực hai yếu tố trên Bull Bitcoin*



Sau đó, dịch vụ sẽ hiển thị mã QR để bạn quét bằng ứng dụng xác thực của mình:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Mã QR do Bull Bitcoin tạo ra để quét bằng thiết bị xác thực của bạn*



**Trong Ente Auth**: Nhấp vào "Nhập khóa thiết lập" rồi quét mã QR hiển thị trên Bull Bitcoin. Ente Auth sẽ tự động nhận dạng tài khoản và điền vào các trường.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Cấu hình thông tin tài khoản Bull Bitcoin trong Ente Auth*



Bạn có thể tùy chỉnh tên dịch vụ và thông tin đăng nhập để dễ tìm kiếm hơn. Các cài đặt nâng cao (thuật toán SHA1, chu kỳ 30 giây, 6 chữ số) thường chính xác theo mặc định.



**Xác thực phía dịch vụ**: Quay lại Bull Bitcoin và nhập mã 6 chữ số do Ente Auth tạo ra để hoàn tất kích hoạt.



![Saisie du code 2FA](assets/fr/09.webp)



*Nhập mã được tạo bởi Ente Auth để xác thực kích hoạt 2FA*



![2FA activée](assets/fr/10.webp)



*Xác nhận kích hoạt 2FA thành công trên Bull Bitcoin*



**Mã dự phòng**: Bull Bitcoin sẽ cung cấp cho bạn mã khôi phục. **Lưu chúng ở nơi an toàn, tách biệt với thiết bị xác thực của bạn.**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Tùy chọn mã dự phòng khẩn cấp generate trên Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Danh sách mã khôi phục cần lưu giữ ở nơi an toàn*



### Tổ chức và quản lý



Ente Auth cung cấp một số tính năng thực tế:



**Sao chép nhanh**: Nhấn mã để tự động sao chép vào bảng tạm.



**Hành động tùy theo ngữ cảnh**: Nhấn và giữ (hoặc nhấp chuột phải vào màn hình) để chỉnh sửa, xóa, chia sẻ hoặc ghim mục nhập.



**Thẻ và tìm kiếm**: Sắp xếp tài khoản của bạn theo thẻ (cá nhân/chuyên nghiệp, theo danh mục dịch vụ) và sử dụng thanh tìm kiếm để lọc nhanh.



![Création d'un tag](assets/fr/17.webp)



*Quá trình tạo thẻ: menu ngữ cảnh và hộp thoại tạo*



![Tag appliqué](assets/fr/18.webp)



*Thẻ "Bitcoin" đã được áp dụng thành công trên tài khoản Bull Bitcoin*



**Biểu tượng tự động**: Mỗi mục nhập có thể được minh họa bằng logo của dịch vụ, nhờ tích hợp gói biểu tượng [Biểu tượng đơn giản] (https://simpleicons.org/).



**Chia sẻ bảo mật tạm thời**: Một tính năng độc đáo của Ente Auth, chia sẻ bảo mật cho phép bạn truyền mã 2FA cho đồng nghiệp mà không tiết lộ bí mật bên trong. generate là một liên kết được mã hóa có hiệu lực tối đa trong 2, 5 hoặc 10 phút - người nhận sẽ thấy mã theo thời gian thực, nhưng không thể xuất mã hoặc truy cập dữ liệu tài khoản. Phương pháp này lý tưởng cho hỗ trợ kỹ thuật hoặc cộng tác tạm thời, mang lại mức độ bảo mật mà một ảnh chụp màn hình hoặc tin nhắn văn bản đơn giản không thể có được.



![Partage sécurisé](assets/fr/19.webp)



*Chia sẻ an toàn tạm thời Interface: chọn thời lượng (5 phút)*



**Xuất/nhập an toàn**: Ente Auth cho phép bạn xuất mã sang các ứng dụng khác hoặc nhập mã từ Google Authenticator và các giải pháp khác. Việc xuất được thực hiện thông qua tệp được mã hóa hoặc mã QR, đảm bảo tính di động của dữ liệu mà không ảnh hưởng đến tính bảo mật.



**Khóa khôi phục BIP39**: Ứng dụng tự động tạo cụm từ khôi phục 24 từ theo tiêu chuẩn BIP39 (Đề xuất Cải tiến Bitcoin), tương tự như ví tiền điện tử. Cụm từ này là khóa khôi phục tối ưu, cho phép bạn khôi phục tất cả mã ngay cả khi quên mật khẩu chính.



## Cấu hình và cài đặt



Ente Auth cung cấp nhiều tùy chọn tùy chỉnh có thể truy cập thông qua cài đặt ứng dụng:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Tổng quan về các tham số có sẵn trong Ente Auth*



### Quản lý tài khoản và dữ liệu



![Paramètres de sécurité](assets/fr/14.webp)



*Tùy chọn bảo mật nâng cao: xác minh email, mã PIN, phiên hoạt động*



Cài đặt bảo mật cho phép bạn:




- Bật xác minh email cho các kết nối mới
- Kích hoạt Passkey
- Xem các phiên hoạt động trên nhiều thiết bị khác nhau của bạn
- Thiết lập mã PIN hoặc sinh trắc học



### Interface và các tùy chọn sử dụng



![Paramètres généraux](assets/fr/15.webp)



*Thông số Interface và tùy chỉnh ứng dụng*



Cài đặt chung bao gồm:




- **Ngôn ngữ**: Interface đa ngôn ngữ
- **Hiển thị**: Biểu tượng lớn, chế độ nhỏ gọn
- **Quyền riêng tư**: Ẩn mã, tìm kiếm nhanh
- **Đo từ xa**: Báo cáo lỗi (có thể tắt)



## Sao lưu và đồng bộ hóa



### Cách thức hoạt động của mã hóa



Khi bạn thêm một tài khoản với tài khoản Ente đã được kết nối, ứng dụng sẽ ngay lập tức mã hóa dữ liệu nhạy cảm này cục bộ bằng khóa chính (được lấy từ mật khẩu của bạn). Dữ liệu đã mã hóa sau đó sẽ được gửi đến máy chủ Ente để lưu trữ.



Nhờ cơ chế này, bản sao lưu đám mây được mã hóa đầu cuối cho mã của bạn luôn khả dụng. Nếu bạn mất thiết bị, chỉ cần cài đặt lại Ente Auth và kết nối lại: ứng dụng sẽ tự động tải xuống và giải mã tất cả mã của bạn.



### Đồng bộ hóa nhiều thiết bị



Nếu bạn sử dụng Ente Auth trên cả điện thoại thông minh và máy tính, mọi bổ sung hoặc thay đổi trên một thiết bị sẽ được hiển thị trong vòng vài giây trên thiết bị kia. Quá trình đồng bộ hóa này diễn ra thông qua đám mây của Ente, nhưng vì dữ liệu được mã hóa đầu cuối, máy chủ chỉ nhìn thấy nội dung được mã hóa không thể đọc được.



![Synchronisation mobile](assets/fr/16.webp)



*Bản demo đồng bộ hóa: cùng một tài khoản Bull Bitcoin có thể truy cập trên thiết bị di động và máy tính để bàn*



Đồng bộ hóa liền mạch: cài đặt Ente Auth trên điện thoại thông minh, đăng nhập bằng thông tin đăng nhập của bạn và tất cả mã 2FA (ở đây là Bull Bitcoin) sẽ tự động xuất hiện. Ví dụ trên cho thấy sự đồng bộ hóa hoàn hảo giữa máy tính để bàn và thiết bị di động - cùng một mã Bull Bitcoin có thể truy cập được trên cả hai thiết bị.



Về mặt bảo mật, cả Ente lẫn bất kỳ bên thứ ba nào đều không thể truy cập vào bí mật 2FA của bạn. Ngay cả siêu dữ liệu (thẻ, ghi chú, tên dịch vụ) cũng được mã hóa trước khi gửi. Kiến trúc không kiến thức này đảm bảo rằng chỉ bạn mới có thể giải mã được mã của mình.



### Sử dụng ngoại tuyến



Đồng bộ hóa yêu cầu kết nối Internet, nhưng Ente Auth hoạt động hoàn hảo ngoại tuyến trên mọi thiết bị, vì mọi dữ liệu đều được lưu trữ cục bộ. Các thay đổi ngoại tuyến sẽ được xếp hàng và đồng bộ hóa ngay khi kết nối được khôi phục.



## Bảo mật và quyền riêng tư



### Đảm bảo mật mã



Ente Auth dựa trên mã hóa đầu cuối mạnh mẽ với kiến trúc không kiến thức. Mã của bạn được mã hóa bằng khóa riêng do bạn nắm giữ, được lấy từ mật khẩu chính của bạn bằng các hàm suy diễn khóa nâng cao.



**Kiến trúc không kiến thức:** Ente không thể truy cập dữ liệu của bạn một cách vật lý. Ngay cả siêu dữ liệu (tên dịch vụ, thẻ, ghi chú) cũng được mã hóa ở phía máy khách trước khi truyền. Phương pháp này đảm bảo rằng trong trường hợp máy chủ của bạn bị tấn công hoặc nhận được yêu cầu từ chính phủ, Ente chỉ có thể tiết lộ dữ liệu được mã hóa mà không thể đọc được nếu không có mật khẩu của bạn.



**Mã hóa cục bộ**: Quá trình mã hóa diễn ra hoàn toàn trên thiết bị của bạn trước khi được gửi lên đám mây. Máy chủ của Ente chỉ nhận và lưu trữ dữ liệu được mã hóa, khiến việc truy cập trái phép trở nên bất khả thi, ngay cả đối với quản trị viên dịch vụ.



### Minh bạch và kiểm toán



Vì mã nguồn mở (https://github.com/ente-io/auth), cộng đồng có thể xác minh sự vắng mặt của cửa hậu. Ente đã thực hiện nhiều cuộc kiểm tra bên ngoài (https://ente.io/blog/cryptography-audit/) để xác thực tính bảo mật của việc triển khai:





- **Cure53** (Đức): Kiểm toán bảo mật ứng dụng và mật mã
- **Symbolic Software** (Pháp): Chuyên môn mật mã chuyên biệt
- **Fallible** (Ấn Độ): Kiểm tra xâm nhập và phân tích lỗ hổng



Các cuộc kiểm toán độc lập này, do các công ty được công nhận thực hiện, đảm bảo rằng việc triển khai mật mã của Ente Auth tuân thủ các biện pháp bảo mật tốt nhất và không có sai sót nghiêm trọng nào.



### Chính sách bảo mật



Ente Auth áp dụng [chính sách bảo mật mẫu mực](https://ente.io/privacy/) dựa trên việc thu thập dữ liệu tối thiểu. Chỉ những thông tin tối thiểu cần thiết cho hoạt động của dịch vụ mới được lưu giữ: email Address của bạn để xác thực và khôi phục tài khoản.



**Không theo dõi hoặc đo từ xa**: Không giống như hầu hết các ứng dụng khác, Ente Auth không thu thập số liệu sử dụng, không nhận dạng dữ liệu sự cố và không thông tin hành vi. Ứng dụng hoạt động mà không có quảng cáo xâm nhập hoặc trình theo dõi phân tích.



**Tuân thủ GDPR**: Ente hoàn toàn tuân thủ Quy định Bảo vệ Dữ liệu Chung của Châu Âu. Bạn có quyền truy cập, chỉnh sửa hoặc xóa dữ liệu của mình bất cứ lúc nào. Xuất dữ liệu](https://ente.io/take-control/) chỉ bằng một cú nhấp chuột, và việc xóa vĩnh viễn tài khoản sẽ xóa toàn bộ dữ liệu của bạn khỏi máy chủ.



**Lưu trữ phi tập trung, an toàn**: Dữ liệu được mã hóa của bạn được sao chép trên 3 nhà cung cấp khác nhau, ở 3 quốc gia khác nhau, đảm bảo tính khả dụng tối ưu đồng thời tránh phụ thuộc vào một nhà cung cấp đám mây duy nhất.



Mô hình kinh doanh của Ente dựa trên dịch vụ Ente Photos trả phí, cho phép chúng tôi cung cấp Ente Auth **miễn phí và không giới hạn** mà không ảnh hưởng đến quyền riêng tư của bạn bằng cách kiếm tiền từ dữ liệu của bạn. Phương pháp này đảm bảo tính bền vững của dịch vụ mà không phụ thuộc vào quảng cáo hoặc việc bán lại dữ liệu cá nhân.



## So sánh với các giải pháp khác



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth nổi bật là một trong số ít giải pháp kết hợp tất cả các ưu điểm: tính minh bạch của mã nguồn, sao lưu đám mây được mã hóa và đồng bộ hóa đa nền tảng.



## Các trường hợp sử dụng được đề xuất



### Người dùng cá nhân



Ente Auth là lựa chọn lý tưởng cho những cá nhân quan tâm đến bảo mật và kích hoạt 2FA một cách có hệ thống. Bạn sẽ không còn phải lo lắng về việc mất mã khi đổi điện thoại, hay phải lựa chọn giữa sự tiện lợi và bảo mật.



### Sử dụng cho gia đình và nhiều thiết bị



Ứng dụng này sẽ phát huy tác dụng nếu bạn sử dụng nhiều thiết bị. Bạn có thể lưu mã trên điện thoại thông minh và máy tính bảng, hoặc chia sẻ đồng bộ và bảo mật một số mã gia đình (Netflix, Family Cloud).



### Sử dụng chuyên nghiệp



Đối với các nhóm quản lý tài khoản nhạy cảm, Ente Auth tạo điều kiện thuận lợi cho việc cộng tác trong khi vẫn đảm bảo tính bảo mật, nhờ các tính năng chia sẻ nâng cao được tích hợp vào phần "Tổ chức và quản lý".



## Thực hành tốt nhất





- **Lưu mã khẩn cấp**: Giữ mã khôi phục do mỗi dịch vụ cung cấp tránh xa điện thoại của bạn.





- **Sử dụng mật khẩu chính mạnh**: Mật khẩu chính Ente Auth của bạn phải duy nhất và mạnh mẽ để bảo vệ tất cả mã của bạn.





- **Kích hoạt bảo vệ cục bộ**: Cấu hình mã PIN hoặc sinh trắc học để ngăn chặn truy cập vật lý trái phép.





- **Không tùy chỉnh quá mức**: Tránh những sửa đổi nâng cao có thể gây ảnh hưởng đến quá trình đồng bộ hóa.





- **Giữ cho ứng dụng luôn được cập nhật**: Cập nhật để sửa lỗi bảo mật và cải thiện chức năng.





- **Kiểm tra khôi phục**: Thỉnh thoảng hãy kiểm tra xem bạn có thể khôi phục mã của mình trên thiết bị khác không.



## Phần kết luận



Ente Auth là một giải pháp xác thực hai yếu tố hiện đại và toàn diện. Bằng cách kết hợp tính bảo mật, tính minh bạch và tính dễ sử dụng, ứng dụng nguồn mở này đáp ứng nhu cầu của những người dùng khó tính mà không ảnh hưởng đến sự tiện lợi.



Không giống như các giải pháp độc quyền khiến bạn bị giới hạn trong một hệ sinh thái không minh bạch, Ente Auth trao lại cho bạn quyền kiểm soát dữ liệu xác thực đồng thời bảo vệ bạn khỏi mất mát do vô tình nhờ các bản sao lưu được mã hóa.



Cho dù bạn là cá nhân muốn bảo mật tài khoản cá nhân hay là nhóm quản lý quyền truy cập doanh nghiệp, Ente Auth là lựa chọn thông minh để hiện đại hóa phương pháp tiếp cận bảo mật kỹ thuật số của bạn mà không ảnh hưởng đến quyền riêng tư.



## Tài nguyên và hỗ trợ



### Tài liệu chính thức




- **Trang web chính thức**: [ente.io/auth](https://ente.io/auth)
- **Trung tâm trợ giúp**: [help.ente.io/auth](https://help.ente.io/auth)
- **Blog kỹ thuật**: [ente.io/blog](https://ente.io/blog)



### Mã nguồn và tính minh bạch




- **GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- **Kiểm toán mật mã**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Cộng đồng




- **Discord**: [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit**: [r/enteio](https://reddit.com/r/enteio)