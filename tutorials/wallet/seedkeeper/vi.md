---
name: Seedkeeper
description: Làm thế nào để sao lưu wallet Bitcoin của tôi bằng thẻ thông minh Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper là thẻ thông minh được phát triển bởi Satochip, một công ty Bỉ chuyên về các giải pháp phần cứng để quản lý và bảo vệ bí mật kỹ thuật số. Nổi tiếng với dòng thẻ thông minh dành cho hệ sinh thái Bitcoin, Satochip đã thiết kế Seedkeeper như một giải pháp thay thế cho các phương pháp lưu trữ cụm từ ghi nhớ truyền thống.



Cụ thể hơn, Seedkeeper có dạng một thẻ thông minh đa chức năng, được chứng nhận EAL6, với bộ xử lý bảo mật và bộ nhớ chống giả mạo (còn gọi là "Phần tử Bảo mật"). Đúng như tên gọi, chức năng của nó là lưu trữ các ký tự ghi nhớ Bitcoin wallet và mật khẩu theo cách được mã hóa và bảo vệ. Với Seedkeeper, bạn có thể generate, nhập, sắp xếp và lưu trữ bí mật của mình trực tiếp trong thành phần bảo mật của thẻ.



Theo tôi, Seedkeeper có hai công dụng chính mà chúng ta sẽ khám phá trong 2 hướng dẫn riêng biệt:




- Lưu trữ cụm từ ghi nhớ Bitcoin**: thay vì viết 12 hoặc 24 từ ra giấy, bạn có thể nhập chúng vào thẻ thông minh và bảo vệ chúng bằng mã PIN.
- Quản lý mật khẩu**: bạn có thể tạo mật khẩu mạnh thông qua ứng dụng Seedkeeper và lưu trữ trực tiếp trong thẻ thông minh, mang đến cho bạn trình quản lý mật khẩu ngoại tuyến tiện lợi và dễ sử dụng.



Về mặt kỹ thuật, Seedkeeper có dung lượng 8192 byte, cho phép lưu trữ tối thiểu 50 bí mật riêng biệt (con số chính xác sẽ phụ thuộc vào kích thước của chúng và siêu dữ liệu liên quan đến từng bí mật). Seedkeeper có thể được truy cập thông qua [đầu đọc thẻ thông minh được kết nối](https://satochip.io/accessories/) với máy tính hoặc thông qua ứng dụng di động có kết nối NFC. Toàn bộ hệ thống hoạt động ở chế độ ngoại tuyến, không cần kết nối Internet, đảm bảo hạn chế bề mặt tấn công.



![Image](assets/fr/001.webp)



Một tính năng đặc biệt thú vị là khả năng sao chép nội dung của một Seedkeeper sang một Seedkeeper khác để tạo bản sao lưu. Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn cách thực hiện điều đó.



Seedkeeper cũng rất thú vị khi kết hợp với phần cứng không trạng thái wallet như SeedSigner hoặc Spectre DIY. Trong trường hợp này, không cần sử dụng ứng dụng Satochip trên máy tính hoặc điện thoại di động. Seedkeeper giữ seed trong secure element và có thể được sử dụng trực tiếp với thiết bị ký, loại bỏ nhu cầu sử dụng mã QR giấy. Tôi sẽ không trình bày trường hợp sử dụng cụ thể này trong hướng dẫn này, vì nó là chủ đề của một hướng dẫn chuyên sâu khác:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Ứng dụng của Seedkeeper là gì?



Trong hướng dẫn này, tôi sẽ chỉ đề cập đến các trường hợp sử dụng liên quan đến Bitcoin, vì đó là nội dung chính của hướng dẫn này. Chúng ta sẽ không đi sâu vào chức năng quản lý mật khẩu, vì đây sẽ là chủ đề của một hướng dẫn khác.



So với việc sao lưu cụm từ ghi nhớ bằng giấy đơn giản, việc sử dụng Seedkeeper có một số ưu điểm sau:





- Chống trộm:** seed trong wallet của bạn không thể truy cập được dưới dạng văn bản thuần túy. Để trích xuất nó, bạn cần biết mã PIN Seedkeeper. Kẻ trộm nào lấy được thiết bị sẽ không thể làm gì được nếu không có mã này.





- Phân tán rủi ro trên hai yếu tố:** bạn có thể chia bảo mật thành yếu tố kỹ thuật số và yếu tố vật lý. Ví dụ: nếu bạn lưu mã PIN Seedkeeper trong trình quản lý mật khẩu, bạn sẽ cần cả quyền truy cập vào trình quản lý này và sở hữu thẻ thông minh vật lý để có được mã seed (giảm đáng kể khả năng bị tấn công).





- Quản lý tập trung:** Seedkeeper hỗ trợ quản lý nhiều loại hạt giống từ các danh mục đầu tư khác nhau.





- Sao lưu dễ dàng:** chỉ cần sao chép các bản sao lưu được mã hóa sang SeedKeeper khác.



Tuy nhiên, có một số nhược điểm so với việc sao lưu giấy đơn giản của seed:





- Giá:** mặc dù khiêm tốn (khoảng 25 €), vẫn cao hơn giá của một tờ giấy.





- Phụ thuộc vào thiết bị điện toán đa năng:** nhập và quản lý seed yêu cầu máy tính hoặc điện thoại thông minh, nghĩa là mã ghi nhớ của bạn sẽ đi qua một máy có bề mặt tấn công rộng hơn nhiều so với phần cứng wallet. Điều này có thể gây ra rủi ro nếu máy bị xâm phạm. Đây là lý do tại sao tôi không khuyên bạn nên sử dụng Seedkeeper để lưu trữ seed của phần cứng wallet (trừ khi sử dụng không trạng thái mà không có máy tính, như với SeedSigner). Vai trò của phần cứng wallet chính xác là lưu trữ seed trong một môi trường tối giản, có độ bảo mật cao. Bằng cách nhập thủ công seed của bạn trên máy tính thông thường, nó không còn bị giới hạn trong phần cứng wallet nữa: nó cũng sẽ nằm trên một máy đa năng, dễ bị tấn công bởi nhiều vectơ tấn công. Vì vậy, tốt hơn là nên sử dụng Seedkeeper cho wallet nóng thay vì wallet lạnh (trừ phần cứng SeedSigner / wallet không trạng thái).





- Rủi ro mất mát liên quan đến mã PIN:** Việc không thể truy cập trực tiếp vào seed, không giống như sao lưu giấy, thực sự bảo vệ chống lại hành vi trộm cắp vật lý. Tuy nhiên, như thường lệ, bảo mật là một hành động cân bằng giữa rủi ro bị trộm cắp và rủi ro mất mát. Nếu bản sao lưu của bạn yêu cầu mã PIN, việc mất mã này sẽ khiến việc khôi phục cụm từ ghi nhớ của bạn trở nên bất khả thi, và do đó không thể truy cập vào bitcoin của bạn.



Xét đến những ưu điểm và nhược điểm này, tôi cho rằng cách sử dụng tốt nhất cho Seedkeeper (ngoài chức năng quản lý mật khẩu) là, một mặt, lưu trữ hạt giống từ **danh mục phần mềm** của bạn, vì chúng đã nằm trên điện thoại hoặc máy tính của bạn, hoặc từ phần cứng wallet không có màn hình như Satochip, và mặt khác, sử dụng kết hợp với phần cứng wallet không trạng thái như SeedSigner, khi đó nó thực sự phát huy hết tác dụng.



Một trường hợp sử dụng đặc biệt thú vị khác của Seedkeeper là khả năng sao lưu *Mô tả* danh mục đầu tư của bạn một cách an toàn và đáng tin cậy.



## 2. Làm thế nào để tôi có được Seedkeeper?



Có hai cách chính để sở hữu Seedkeeper. Bạn có thể mua trực tiếp từ cửa hàng chính thức của Satochip (https://satochip.io/product/seedkeeper/) hoặc từ một đại lý được ủy quyền. Tuy nhiên, vì Applet Seedkeeper là mã nguồn mở (https://github.com/Toporin/Seedkeeper-Applet), bạn cũng có thể tự cài đặt trên một thẻ thông minh trống (https://satochip.io/product/blank-javacard-for-diy-project/).



Nếu bạn muốn sử dụng chức năng sao lưu của Seedkeeper, rõ ràng là bạn sẽ cần phải mua hai thẻ thông minh.



## 3. Cài đặt ứng dụng Seedkeeper



Trong hướng dẫn này, chúng ta sẽ sao lưu danh mục đầu tư seed của mình trên Seedkeeper. Bước đầu tiên là cài đặt phần mềm trên máy tính hoặc điện thoại thông minh. Trên PC, bạn cần tải xuống phiên bản mới nhất của Satochip-Utils (https://github.com/Toporin/Satochip-Utils/releases). Trên thiết bị di động, ứng dụng Seedkeeper có sẵn trên [Google Play Store] (https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) cũng như trên [Apple App Store] (https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Khởi tạo Seedkeeper



Khởi chạy ứng dụng và nhấp vào nút "*Nhấp và Quét*".



![Image](assets/fr/003.webp)



Bạn sẽ được yêu cầu nhập mã PIN cho Seedkeeper. Vì đây là thẻ mới nên chưa có mã PIN nào được xác định. Hãy nhập bất kỳ mã PIN nào để bỏ qua bước này, sau đó nhấp vào "Tiếp theo".



![Image](assets/fr/004.webp)



Sau đó, đặt thẻ vào mặt sau của điện thoại thông minh. Ứng dụng sẽ phát hiện Seedkeeper chưa được khởi tạo và sẽ nhắc bạn đặt mã PIN cho thẻ thông minh, dài từ 4 đến 16 ký tự. Để bảo mật tối ưu, hãy chọn một mật khẩu mạnh, càng dài càng tốt, ngẫu nhiên và bao gồm nhiều ký tự. Mã PIN này là rào cản duy nhất ngăn chặn việc truy cập vật lý vào cụm từ khôi phục của bạn.



**Cũng đừng quên lưu mã PIN này ngay bây giờ**, ví dụ như trong trình quản lý mật khẩu hoặc trên một phương tiện vật lý riêng biệt. Trong trường hợp sau, đừng bao giờ để phương tiện chứa mã PIN ở cùng nơi với Seedkeeper, nếu không, biện pháp bảo mật này sẽ trở nên vô dụng. Điều quan trọng là phải có một bản sao lưu đáng tin cậy: nếu không có mã PIN, bạn sẽ không thể khôi phục các bí mật được lưu trữ trên Seedkeeper.



![Image](assets/fr/005.webp)



Xác nhận mã PIN lần thứ hai.



![Image](assets/fr/006.webp)



Seedkeeper của bạn hiện đã được khởi tạo. Bạn có thể mở khóa bằng cách nhập mã PIN vừa đặt.



![Image](assets/fr/007.webp)



Bây giờ bạn sẽ được đưa đến trang quản lý thẻ thông minh của mình.



![Image](assets/fr/008.webp)



## 5. Đăng ký seed trên Seedkeeper



Sau khi Seedkeeper của bạn được mở khóa, hãy nhấp vào nút "*+*".



![Image](assets/fr/009.webp)



Chọn "Nhập bí mật*". Tùy chọn "*Tạo bí mật*" cho phép bạn tạo cụm từ ghi nhớ mới trực tiếp từ bên trong ứng dụng.



![Image](assets/fr/010.webp)



Trong trường hợp này, chúng ta muốn lưu seed vào danh mục đầu tư. Nhấp vào "*Mnemonic*".



![Image](assets/fr/011.webp)



Gán "*Nhãn*" cho bí mật này để có thể dễ dàng nhận dạng nếu bạn lưu trữ nhiều thông tin trong Seedkeeper.



![Image](assets/fr/012.webp)



Sau đó, nhập cụm từ khôi phục của bạn vào trường được cung cấp. Nếu muốn, bạn cũng có thể thêm passphrase BIP39 hoặc *Mô tả* của bạn. Sau đó, nhấp vào "Nhập*".



![Image](assets/fr/013.webp)



*Mã ghi nhớ hiển thị trong hình ảnh này là giả mạo và không thuộc về bất kỳ ai. Đây chỉ là ví dụ. Tuyệt đối không tiết lộ mã ghi nhớ của bạn cho bất kỳ ai, nếu không bitcoin của bạn sẽ bị đánh cắp.



Đặt Seedkeeper ở mặt sau của điện thoại thông minh.



![Image](assets/fr/014.webp)



seed của bạn đã được đăng ký.



![Image](assets/fr/015.webp)



## 6. Truy cập seed của bạn trên Seedkeeper



Nếu bạn muốn kiểm tra cụm từ ghi nhớ của mình, hãy cầm Seedkeeper lên và nhấp vào nút "*Nhấp & Quét*".



![Image](assets/fr/016.webp)



Nhập mã PIN của bạn, sau đó nhấn "*Tiếp theo*".



![Image](assets/fr/017.webp)



Đặt Seedkeeper ở mặt sau của điện thoại thông minh.



![Image](assets/fr/018.webp)



Thao tác này sẽ đưa bạn đến danh sách tất cả các bí mật đã đăng ký của bạn. Trong ví dụ này, tôi muốn hiển thị seed trong danh mục đầu tư "*Ứng dụng Blockstream*" của mình, vì vậy tôi nhấp vào nó.



![Image](assets/fr/019.webp)



Nhấn nút "*Hiển thị*".



![Image](assets/fr/020.webp)



Quét lại Seedkeeper của bạn.



![Image](assets/fr/021.webp)



Cụm từ ghi nhớ mà bạn đã ghi trước đó hiện được hiển thị trên màn hình.



![Image](assets/fr/022.webp)



## 7. Sao lưu Seedkeeper



Bây giờ chúng ta sẽ sao lưu Seedkeeper của tôi trên một Seedkeeper thứ hai để có hai bản sao. Sự dự phòng này có thể là một phần của chiến lược bảo mật bitcoin của bạn: ví dụ, lưu trữ cụm từ của bạn ở hai vị trí riêng biệt để hạn chế rủi ro vật lý, hoặc ủy thác một bản sao cho một người thân đáng tin cậy như một phần của kế hoạch thừa kế.



Để thực hiện việc này, hãy mang theo Seedkeeper thứ hai của bạn (nhớ đánh dấu một trong hai Seedkeeper để tránh nhầm lẫn). Bắt đầu bằng cách khởi tạo nó, như được mô tả trong bước 4 của hướng dẫn này. Chọn lại mật khẩu mạnh. Tùy thuộc vào chiến lược của bạn, bạn có thể chọn một mật khẩu khác hoặc giữ nguyên.



![Image](assets/fr/023.webp)



Mở ứng dụng, nhấp vào "*Nhấp & Quét*", nhập mật khẩu Seedkeeper số 1 (nguồn) của bạn, sau đó quét.



![Image](assets/fr/024.webp)



Thao tác này sẽ đưa bạn đến trang chủ, hiển thị danh sách bí mật của bạn. Nhấp vào ba dấu chấm nhỏ ở góc trên bên phải giao diện.



![Image](assets/fr/025.webp)



Chọn "*Tạo bản sao lưu*", sau đó nhấn "*Bắt đầu*".



![Image](assets/fr/026.webp)



Nhập mã PIN của thẻ dự phòng (Seedkeeper số 2).



![Image](assets/fr/027.webp)



Sau đó quét thẻ.



![Image](assets/fr/028.webp)



Thực hiện tương tự với thẻ chính (Seedkeeper số 1), sau đó nhấp vào "*Tạo bản sao lưu*".



![Image](assets/fr/029.webp)



Seedkeeper số 2 của bạn hiện chứa tất cả các bí mật được lưu trữ trên Seedkeeper số 1.



![Image](assets/fr/030.webp)



Bạn có thể quét Seedkeeper n°2 để kiểm tra xem bí mật đã được sao chép hay chưa.



![Image](assets/fr/031.webp)



Vậy là xong! Giờ bạn đã biết cách sử dụng Seedkeeper để lưu cụm từ ghi nhớ của Bitcoin wallet. Trong bài hướng dẫn sau, chúng ta sẽ tìm hiểu cách sử dụng Seedkeeper để lưu trữ mật khẩu. Tôi cũng mời bạn khám phá cách sử dụng kết hợp với SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

Trong hướng dẫn này, chúng tôi đã đề cập đến ***Mô tả*** trong danh mục đầu tư Bitcoin của bạn nhiều lần. Bạn chưa biết chúng là gì? Trong trường hợp đó, tôi khuyên bạn nên tham gia khóa đào tạo CYP 201 miễn phí của chúng tôi, khóa học này sẽ đi sâu vào chi tiết tất cả các cơ chế liên quan đến việc vận hành danh mục đầu tư HD!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f