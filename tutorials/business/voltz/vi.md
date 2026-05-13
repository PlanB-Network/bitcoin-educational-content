---
name: Voltz
description: Bộ định tuyến Lightning wallet đa năng dành cho doanh nghiệp của bạn.
---

![cover](assets/cover.webp)



Ý tưởng về nền tảng Voltz xuất phát từ một nhóm những người đam mê Bitcoin muốn cung cấp dịch vụ cổng wallet riêng của họ. Kết quả là một cơ sở hạ tầng hoàn chỉnh để chấp nhận Bitcoin ở cấp độ bán lẻ. Trong hướng dẫn này, chúng tôi sẽ đưa bạn khám phá Voltz và các khả năng tích hợp Bitcoin mà nền tảng này cung cấp.



## Bắt đầu sử dụng Voltz



Ngoài chức năng là một thiết bị lưu trữ Lightning wallet cho phép bạn gửi, nhận và thanh toán hàng ngày, Voltz còn là một nền tảng hoàn chỉnh cung cấp nhiều tiện ích mở rộng để tích hợp bitcoin như một điểm bán hàng hoặc thị trường trong doanh nghiệp của bạn.



Hãy truy cập nền tảng [Voltz](https://www.lnvoltz.xyz/en) và tạo tài khoản bằng cách nhấp vào nút "Dùng thử ngay".



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Điều quan trọng là phải đặt mật khẩu mạnh bao gồm cả chữ và số để tăng khả năng chống lại các cuộc tấn công vét cạn, và hãy kiểm tra xem bạn có đang truy cập trang web chính thức của Voltz khi điền thông tin đăng nhập để phòng tránh bị lừa đảo.



Giao diện của Voltz rất giống với giao diện của nền tảng LnBits.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Thực tế, Voltz được xây dựng trên máy chủ LnBits; hãy xem hướng dẫn của chúng tôi để tìm hiểu cách cài đặt máy chủ LnBits của riêng bạn và xây dựng các giải pháp trên đó.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Nền tảng này cho phép bạn quản lý nhiều danh mục đầu tư một cách hiệu quả. Theo mặc định, khi bạn đăng ký, bạn sẽ tự động có một danh mục đầu tư Lightning. Tuy nhiên, bạn có thể thêm các danh mục đầu tư khác.



![wallets](assets/fr/03.webp)



### Tính di động



Voltz không chỉ giới hạn ở giao diện web: trong phần **Truy cập di động**, bạn có thể kết nối thiết bị Voltz wallet đang hoạt động của mình với các ứng dụng như Zeus hoặc Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Để thực hiện điều này, bạn cần cài đặt và kích hoạt tiện ích mở rộng **LndHub** trên nền tảng.



![lndhub](assets/fr/04.webp)



Chọn danh mục Voltz đang hoạt động của bạn và, tùy thuộc vào các quyền bạn muốn cấp, hãy quét mã QR tương ứng.




- Mã QR trên hóa đơn chỉ cho phép bạn xem lịch sử danh mục đầu tư và các hóa đơn mới generate.
- Mã QR quản trị cho phép bạn xem lịch sử, hóa đơn generate và thanh toán hóa đơn Lightning.



![qrs](assets/fr/05.webp)



Trong hướng dẫn này, chúng ta sẽ kết nối thiết bị Voltz wallet với ứng dụng Blue Wallet.



![connect](assets/fr/06.webp)



Sau khi danh mục đầu tư của chúng ta được kết nối, tất cả các thao tác được thực hiện sẽ được đồng bộ hóa giữa Blue Wallet và Voltz. Ví dụ, khi bạn sử dụng generate để tạo hóa đơn trên Blue Wallet, lịch sử giao dịch cũng sẽ được hiển thị trên Voltz.



![sync](assets/fr/07.webp)



Trong phần **Cấu hình danh mục đầu tư**, bạn sẽ tìm thấy các thông số tối thiểu như tùy chỉnh tên danh mục đầu tư và loại tiền tệ mà bạn muốn nhận thanh toán.



![config](assets/fr/08.webp)



### Phần mở rộng



Một trong những tính năng đặc biệt của nền tảng Voltz là tính mô đun, cho phép bạn kích hoạt các tiện ích mở rộng cần thiết. Danh sách các tiện ích mở rộng có thể được tìm thấy trong menu **Tiện ích mở rộng**.



![extensions](assets/fr/09.webp)



Trong số các tiện ích mở rộng này có TPoS, một thiết bị đầu cuối bán hàng mà bạn có thể sử dụng để quản lý hàng tồn kho và thu tiền từ khách hàng.



![tpos](assets/fr/10.webp)



Từ thiết bị thanh toán POS, bạn có thể:




- Hãy tạo một trang web để bạn có thể chia sẻ với khách hàng và đối tác của mình;
- Quản lý kho sản phẩm;
- Tạo hóa đơn Lightning;
- Thanh toán bằng tiền mặt thông qua thẻ Bolt.



Tiện ích mở rộng này có cả phiên bản miễn phí và phiên bản trả phí với các tính năng nâng cao hơn. Để tạo thiết bị POS, hãy nhấp vào nút **Mở** bên dưới biểu tượng tiện ích mở rộng, sau đó nhấp vào **POS mới**.



![new_tpos](assets/fr/11.webp)



Hãy đặt tên cho điểm bán hàng của bạn, sau đó kết nối thiết bị Voltz wallet với máy POS để thu tiền. Bạn có thể kích hoạt chức năng tiền boa bằng cách chọn ô **Kích hoạt tiền boa**. Đồng thời, hãy kích hoạt tùy chọn in hóa đơn nếu bạn muốn cấp biên lai cho khách hàng (chức năng này vẫn đang trong quá trình phát triển, vì vậy có thể xảy ra lỗi).



Thiết bị thanh toán tại điểm bán cũng bao gồm chức năng cấu hình thuế khi bạn muốn áp dụng trực tiếp thuế của quốc gia mình cho sản phẩm.



![tpos](assets/fr/12.webp)



Sau khi thiết lập xong thiết bị POS, bạn có thể thêm các sản phẩm và dịch vụ đã được cấu hình sẵn để đảm bảo trải nghiệm thanh toán và kế toán suôn sẻ cho bạn và khách hàng.



![product](assets/fr/13.webp)



Tạo sản phẩm bằng cách đặt tên, thêm hình ảnh và thiết lập giá bán. Bạn có thể phân loại sản phẩm để dễ dàng theo dõi. Bạn có thể áp dụng thuế trực tiếp cho một sản phẩm cụ thể. Nếu sản phẩm chưa áp dụng thuế, thuế được cấu hình ở bước tạo thiết bị bán hàng sẽ được áp dụng tự động.



![products](assets/fr/14.webp)



Bạn có thể tự động nhập danh sách sản phẩm của mình từ định dạng JSON bằng cách nhấp vào nút **Nhập/Xuất**.



![exports](assets/fr/15.webp)



Truy cập khu vực thanh toán thông qua liên kết bằng cách nhấp vào biểu tượng **Mở tab mới**, hoặc chia sẻ nền tảng POS của bạn qua mã QR với khách hàng bằng cách nhấp vào biểu tượng **Mã QR**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Khách hàng của bạn có thể xem danh mục sản phẩm và thanh toán trực tiếp từ giao diện này.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



Trong nhóm các tiện ích mở rộng có sẵn, bạn cũng sẽ tìm thấy các công cụ như tiện ích mở rộng **Invoice** và **Payment Link**, cho phép bạn tạo hóa đơn generate với các sản phẩm cụ thể để thu các khoản thanh toán riêng lẻ mà không cần thông qua thiết bị POS.



## Theo dõi các khoản thanh toán của bạn



Trong menu **Thanh toán**, Voltz cung cấp cho bạn tổng quan về các khoản thanh toán cho các danh mục đầu tư khác nhau của bạn.


Bạn có thể theo dõi các khoản thanh toán của mình bằng cách:




- Trạng thái.
- Nhãn: ví dụ **TPOS** cho thanh toán tại điểm bán hàng và **lnhub** thông qua kết nối di động trong ví Zeus và Blue Wallet.
- Danh mục bộ sưu tập.
- Tổng số tiền thu vào và chi ra.
- Một khoảng thời gian được xác định rõ ràng.



![payments](assets/fr/22.webp)



## Nhiều tùy chọn hơn



Voltz cũng là một nền tảng mà trên đó bạn có thể xây dựng các giải pháp của riêng mình. Trong phần **Tiện ích mở rộng**, bạn sẽ tìm thấy hướng dẫn phát triển các tiện ích mở rộng của riêng mình trong hệ sinh thái Voltz và LnBits.



![build](assets/fr/23.webp)



Trong trường hợp bạn muốn phát triển các giải pháp bên ngoài hệ sinh thái nhưng vẫn sử dụng cơ sở hạ tầng của họ, trong phần **URL của node**, bạn sẽ tìm thấy các khóa API và thông tin tài liệu kèm theo ví dụ về những gì bạn có thể làm với dữ liệu này.



Bạn có thể tạo hóa đơn Lightning từ các ứng dụng của mình bằng thiết bị Voltz wallet, thanh toán hóa đơn Lightning, giải mã và xác minh hóa đơn.



![keys](assets/fr/24.webp)



Giờ bạn đã nắm vững Voltz rồi. Nếu bạn thấy hướng dẫn này hữu ích, chúng tôi tin chắc bạn sẽ học được nhiều hơn về các phương pháp và công cụ tốt nhất để tích hợp bitcoin vào doanh nghiệp của mình với khóa học của chúng tôi: Bitcoin dành cho doanh nghiệp.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a