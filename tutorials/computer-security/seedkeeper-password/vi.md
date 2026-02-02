---
name: Seedkeeper - Trình quản lý mật khẩu
description: Làm thế nào để lưu mật khẩu của bạn bằng thẻ thông minh Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper là thẻ thông minh được phát triển bởi Satochip, một công ty Bỉ chuyên về các giải pháp phần cứng để quản lý và bảo vệ bí mật kỹ thuật số. Nổi tiếng với dòng thẻ thông minh dành cho hệ sinh thái Bitcoin, Satochip đã phát triển Seedkeeper như một giải pháp thay thế cho các phương pháp truyền thống trong việc lưu trữ cụm từ ghi nhớ và các bí mật kỹ thuật số khác.



Cụ thể, Seedkeeper có dạng một thẻ thông minh đa chức năng, được chứng nhận EAL6, với bộ xử lý bảo mật và bộ nhớ chống giả mạo (còn gọi là "Phần tử Bảo mật"). Đúng như tên gọi, chức năng của nó là lưu trữ các ký tự ghi nhớ và mật khẩu danh mục đầu tư Bitcoin một cách được mã hóa và bảo vệ. Với Seedkeeper, bạn có thể generate, nhập, sắp xếp và lưu trữ bí mật của mình trực tiếp trong thành phần bảo mật của thẻ.



Theo tôi, Seedkeeper có hai công dụng chính mà chúng ta sẽ khám phá trong 2 hướng dẫn riêng biệt:




- Lưu trữ cụm từ ghi nhớ Bitcoin**: thay vì viết 12 hoặc 24 từ ra giấy, bạn có thể nhập chúng vào thẻ thông minh và bảo vệ chúng bằng mã PIN.
- Quản lý mật khẩu**: bạn có thể tạo mật khẩu mạnh thông qua ứng dụng Seedkeeper và lưu trữ trực tiếp trong thẻ thông minh, mang đến cho bạn trình quản lý mật khẩu ngoại tuyến tiện lợi và dễ sử dụng.



Về mặt kỹ thuật, Seedkeeper có dung lượng 8192 byte, cho phép lưu trữ tối thiểu 50 bí mật riêng biệt (con số chính xác sẽ phụ thuộc vào kích thước của chúng và siêu dữ liệu liên quan đến từng bí mật). Seedkeeper có thể được truy cập thông qua [đầu đọc thẻ thông minh được kết nối](https://satochip.io/accessories/) với máy tính hoặc thông qua ứng dụng di động có kết nối NFC. Toàn bộ hệ thống hoạt động ở chế độ ngoại tuyến, không cần kết nối Internet, đảm bảo hạn chế bề mặt tấn công.



![Image](assets/fr/001.webp)



Một tính năng đặc biệt thú vị là khả năng sao chép nội dung của một Seedkeeper sang một Seedkeeper khác để tạo bản sao lưu. Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn cách thực hiện điều đó.



Trong hướng dẫn này, chúng tôi sẽ chỉ đề cập đến việc sử dụng SeedKeeper cho mật khẩu truyền thống, theo cách của một trình quản lý mật khẩu. Nếu bạn muốn sử dụng SeedKeeper để lưu các cụm từ ghi nhớ Bitcoin wallet, vui lòng xem hướng dẫn khác này:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Làm thế nào để tôi có được Seedkeeper?



Có hai cách chính để sở hữu Seedkeeper. Bạn có thể mua trực tiếp từ cửa hàng chính thức của Satochip (https://satochip.io/product/seedkeeper/) hoặc từ một đại lý được ủy quyền. Tuy nhiên, vì Applet Seedkeeper là mã nguồn mở (https://github.com/Toporin/Seedkeeper-Applet), bạn cũng có thể tự cài đặt trên một thẻ thông minh trống (https://satochip.io/product/blank-javacard-for-diy-project/).



Nếu bạn muốn sử dụng chức năng sao lưu của Seedkeeper, rõ ràng là bạn sẽ cần phải mua hai thẻ thông minh.



## 2. Cài đặt ứng dụng Seedkeeper



Bước đầu tiên là cài đặt phần mềm trên máy tính hoặc điện thoại thông minh. Trên PC, bạn cần tải xuống phiên bản Satochip-Utils mới nhất (https://github.com/Toporin/Satochip-Utils/releases). Trên thiết bị di động, ứng dụng Seedkeeper có sẵn trên Cửa hàng Google Play (https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) và trên Cửa hàng Apple App Store (https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Khởi tạo Seedkeeper



Khởi chạy ứng dụng và nhấp vào nút "*Nhấp và Quét*".



![Image](assets/fr/003.webp)



Bạn sẽ được yêu cầu nhập mã PIN cho Seedkeeper. Vì đây là thẻ mới nên chưa có mã PIN nào được xác định. Hãy nhập bất kỳ mã PIN nào để bỏ qua bước này, sau đó nhấp vào "Tiếp theo".



![Image](assets/fr/004.webp)



Sau đó, đặt thẻ vào mặt sau của điện thoại thông minh. Ứng dụng sẽ phát hiện Seedkeeper chưa được khởi tạo và sẽ nhắc bạn đặt mã PIN cho thẻ thông minh, dài từ 4 đến 16 ký tự. Để bảo mật tối ưu, hãy chọn mã PIN mạnh, càng dài càng tốt, ngẫu nhiên và bao gồm nhiều ký tự. Mã PIN này là rào cản duy nhất chống lại việc truy cập vật lý vào mật khẩu của bạn.



**Cũng đừng quên lưu mã PIN này ngay bây giờ**, ví dụ như trong trình quản lý mật khẩu hoặc trên một phương tiện vật lý riêng biệt. Trong trường hợp sau, đừng bao giờ để phương tiện chứa mã PIN ở cùng nơi với Seedkeeper, nếu không, biện pháp bảo mật này sẽ trở nên vô dụng. Điều quan trọng là phải có một bản sao lưu đáng tin cậy: nếu không có mã PIN, bạn sẽ không thể khôi phục các bí mật được lưu trữ trên Seedkeeper.



![Image](assets/fr/005.webp)



Xác nhận mã PIN lần thứ hai.



![Image](assets/fr/006.webp)



Seedkeeper của bạn hiện đã được khởi tạo. Bạn có thể mở khóa bằng cách nhập mã PIN vừa đặt.



![Image](assets/fr/007.webp)



Bây giờ bạn sẽ được đưa đến trang quản lý thẻ thông minh của mình.



![Image](assets/fr/008.webp)



## 4. Lưu mật khẩu trên Seedkeeper



Sau khi Seedkeeper của bạn được mở khóa, hãy nhấp vào nút "*+*".



![Image](assets/fr/009.webp)



Chọn "Tạo bí mật*". Tùy chọn "*Nhập bí mật*" cho phép bạn lưu một bí mật hiện có (ví dụ: mật khẩu bạn đã tạo trước đó).



![Image](assets/fr/010.webp)



Trong trường hợp này, chúng ta muốn lưu mật khẩu. Nhấp vào "*Mật khẩu*".



![Image](assets/fr/011.webp)



Gán "*Nhãn*" cho bí mật này để có thể dễ dàng nhận dạng nếu bạn lưu trữ nhiều thông tin trong Seedkeeper. Bạn cũng có thể thêm mã định danh liên kết với mật khẩu và URL của trang web.



![Image](assets/fr/012.webp)



Chọn độ dài và thông số cho mật khẩu của bạn, sau đó nhấp vào "*Tạo*", rồi "*Nhập*".



![Image](assets/fr/013.webp)



Đặt Seedkeeper ở mặt sau của điện thoại thông minh.



![Image](assets/fr/014.webp)



Mật khẩu của bạn đã được đăng ký.



![Image](assets/fr/015.webp)



## 5. Truy cập mật khẩu Seedkeeper của bạn



Nếu bạn muốn kiểm tra mật khẩu của mình, hãy mở Seedkeeper và nhấp vào nút "*Nhấp & Quét*".



![Image](assets/fr/016.webp)



Nhập mã PIN của bạn, sau đó nhấn "*Tiếp theo*".



![Image](assets/fr/017.webp)



Đặt Seedkeeper ở mặt sau của điện thoại thông minh.



![Image](assets/fr/018.webp)



Thao tác này sẽ đưa bạn đến danh sách tất cả các bí mật đã đăng ký của bạn. Trong ví dụ này, tôi muốn hiển thị mật khẩu cho tài khoản Plan ₿ Academy của mình, vì vậy tôi nhấp vào đó.



![Image](assets/fr/019.webp)



Nhấn nút "*Hiển thị*".



![Image](assets/fr/020.webp)



Quét lại Seedkeeper của bạn.



![Image](assets/fr/021.webp)



Mật khẩu đã lưu trước đó của bạn sẽ hiển thị trên màn hình. Bạn có thể sao chép và sử dụng trên trang web liên quan.



![Image](assets/fr/022.webp)



## 6. Sao lưu Seedkeeper



Bây giờ chúng ta sẽ sao lưu Seedkeeper của tôi trên một Seedkeeper thứ hai để có hai bản sao. Việc sao lưu này có thể là một phần của chiến lược bảo mật các mật khẩu quan trọng nhất của bạn: ví dụ, lưu trữ Seedkeeper ở 2 vị trí riêng biệt để hạn chế rủi ro vật lý, hoặc ủy thác một bản sao cho người thân đáng tin cậy.



Để thực hiện việc này, hãy mang theo Seedkeeper thứ hai của bạn (nhớ đánh dấu một trong hai Seedkeeper để tránh nhầm lẫn). Bắt đầu bằng cách khởi tạo nó, như được mô tả trong bước 3 của hướng dẫn này. Một lần nữa, hãy chọn một mã PIN mạnh. Tùy thuộc vào chiến lược của bạn, bạn có thể chọn một mã PIN khác hoặc giữ nguyên mã PIN.



![Image](assets/fr/023.webp)



Mở ứng dụng, nhấp vào "*Nhấp và Quét*", nhập mã PIN của Seedkeeper n°1 (nguồn), sau đó quét.



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



Vậy là xong! Giờ bạn đã biết cách sử dụng Seedkeeper để lưu trữ mật khẩu. Trong bài hướng dẫn sau, chúng ta sẽ tìm hiểu cách sử dụng Seedkeeper để sao lưu Bitcoin wallet. Tôi cũng mời bạn khám phá cách sử dụng kết hợp với SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356