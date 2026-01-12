---
name: PureOS
description: Bản phân phối Linux cho phép bạn kiểm soát cuộc sống số của mình.
---

![cover](assets/cover.webp)



Bảo vệ thông tin cá nhân trong thời đại kỹ thuật số là ưu tiên hàng đầu của mọi người dùng Internet. Các công ty, tổ chức và thậm chí cả hệ điều hành đều là những nguồn thông tin hữu ích để xác định hồ sơ và lối sống của bạn. Việc lựa chọn hệ điều hành phù hợp là bước đầu tiên để tăng cường quyền riêng tư trực tuyến của bạn. Trong hướng dẫn này, chúng ta sẽ tìm hiểu về PureOS, một bản phân phối Linux tập trung vào quyền riêng tư.



https://planb.academy/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Bắt đầu với PureOS



PureOS là hệ điều hành dựa trên Debian do Purism phát triển. PureOS phù hợp cho cả chuyên gia CNTT và người dùng đang tìm kiếm một bản phân phối đơn giản, dễ sử dụng. Điểm độc đáo của nó là *Phần mềm Miễn phí*, tập trung vào việc bảo vệ dữ liệu cá nhân của người dùng bằng cách thiết lập một khuôn khổ dựa trên quyền riêng tư, tự do, bảo mật và ổn định mà Debian mang lại.



### Tại sao nên chọn PureOS?





- **Interface đơn giản, trực quan**: GNOME cung cấp màn hình nền Interface rõ ràng, được thiết kế để dễ sử dụng, ngay cả với những người không thoải mái với dòng lệnh.





- **Miễn phí**: Giống như hầu hết các bản phân phối Linux khác, PureOS hoàn toàn miễn phí sử dụng. Tuy nhiên, có gói đăng ký hàng tháng để hỗ trợ các nhà phát triển.





- **Bảo mật và ổn định**: Kiến trúc và chế độ hoạt động của PureOS khiến nó trở thành bản phân phối có tính bảo mật cao, đảm bảo bảo vệ dữ liệu và tính ổn định của hệ thống.





- **Tài liệu và cộng đồng năng động**: PureOS có tài liệu rõ ràng, dễ tiếp cận và cộng đồng tận tâm, phản hồi nhanh chóng, giúp bạn dễ dàng giải quyết vấn đề và tìm hiểu hệ thống từng bước.



## Cài đặt và cấu hình



Việc cài đặt và cấu hình PureOS trên máy tính của bạn sẽ yêu cầu các tính năng tối giản sau:




- Một ổ USB có dung lượng ít nhất 8GB để flash hệ thống.
- RAM 4 GB.
- 30 GB dung lượng trống trên đĩa Hard của bạn.



Truy cập [trang web chính thức của PureOS](https://pureos.net/) sau đó tải xuống ảnh ISO của hệ điều hành theo cấu trúc máy của bạn.



Để khởi chạy cài đặt PureOS, bạn cần tạo một khóa USB có thể khởi động bằng phần mềm flash như [Balena Etcher](https://www.balena.io/etcher).



Chỉ với ba bước đơn giản, bạn sẽ có một ổ USB khởi động với hệ điều hành PureOS.





- Cắm USB vào và chạy phần mềm Balena đã tải xuống.
- Sau đó chọn ảnh ISO PureOS
- Chọn ổ USB làm thiết bị đầu ra, sau đó nhấp vào nút **Flash** và đợi quá trình hoàn tất.



![0_01](assets/fr/01.webp)



Sau khi khởi động khóa USB, hãy khởi động lại máy tính mà bạn muốn cài đặt PureOS.



Khi khởi động, hãy truy cập BIOS bằng cách nhấn phím `ESC`, `F9` hoặc `F11`, tùy thuộc vào máy của bạn. Chọn ổ USB làm thiết bị khởi động, sau đó nhấn `ENTER` để xác nhận.



### Màn hình khởi động



PureOS cung cấp nhiều tùy chọn để khởi động hệ điều hành. Chọn tùy chọn **Kiểm tra hoặc Cài đặt PureOS** để khởi chạy quá trình cài đặt hệ điều hành.



![0_02](assets/fr/02.webp)



Đặt ngôn ngữ và bố cục bàn phím bạn muốn sử dụng trên máy tính của mình.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Cho phép hoặc từ chối quyền truy cập vào **vị trí địa lý** của bạn đối với các ứng dụng cung cấp đề xuất được cá nhân hóa dựa trên khu vực của bạn.



![0_05](assets/fr/05.webp)



Bạn có thể kết nối với tài khoản **NextCloud** hiện có của mình để truy xuất dữ liệu được liên kết với bộ ứng dụng văn phòng mà bạn đang sử dụng trên hệ thống khác.



![0_06](assets/fr/06.webp)



Có hướng dẫn nhưng bạn có thể đóng cửa sổ nếu muốn bỏ qua bước này.



![0_08](assets/fr/08.webp)



### Khởi chạy cài đặt



Nhấp vào menu **Hoạt động** và khám phá các ứng dụng và công cụ được cài đặt sẵn trên hệ thống. Nhấp vào **Cài đặt PureOS** để bắt đầu cài đặt



![0_09](assets/fr/09.webp)



Đặt ngôn ngữ hệ thống và bố cục bàn phím theo yêu cầu, sau đó cấu hình chế độ phân vùng đĩa Hard.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Bạn có hai tùy chọn để phân vùng đĩa Hard của mình:




- **Xóa đĩa**: Để cài đặt hoàn chỉnh PureOS, hãy xóa toàn bộ dữ liệu có sẵn trên đĩa Hard của bạn.



![0_14](assets/fr/14.webp)





- **Phân vùng thủ công** để tạo điểm số của riêng bạn



⚠️ Khi bạn tạo thủ công các phân vùng cho hệ điều hành của mình, hãy đảm bảo bạn phân bổ một phân vùng tối thiểu 2 GB cho hoạt động của PureOS và sau đó là một phân vùng khác cho dữ liệu.



![0_15](assets/fr/15.webp)



Kích hoạt **mã hóa ổ đĩa** nếu bạn muốn bảo mật dữ liệu. Nhập mật khẩu mạnh và phức tạp.



Liên kết người dùng với hệ điều hành của bạn bằng cách xác định tên người dùng và mật khẩu chữ số có ít nhất 20 ký tự để tăng cường bảo mật dữ liệu.



![0_16](assets/fr/16.webp)



Xem lại các thiết lập bạn đã thực hiện và sửa đổi nếu cần thiết.



![0_17](assets/fr/17.webp)



Nhấp vào **Cài đặt** rồi **Cài đặt ngay** để xác nhận rằng PureOS đã được cài đặt trên máy tính của bạn.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Khi quá trình cài đặt hoàn tất, hãy đánh dấu vào ô **Khởi động lại ngay** để khởi động lại máy tính, sau đó xác nhận:




- Ngôn ngữ.
- Bố cục bàn phím.
- Tài khoản NextCloud của bạn (tùy chọn).



![0_25](assets/fr/25.webp)



## Cập nhật



Trước khi bắt đầu sử dụng PureOS, việc cập nhật hệ thống là vô cùng quan trọng. Việc này sẽ giúp bạn tận dụng các tính năng và bản vá bảo mật mới nhất, đồng thời đảm bảo tính ổn định cao hơn.





- Cập nhật qua đồ họa **Interface**:


Mở ứng dụng **Phần mềm**, sau đó chuyển đến tab **Cập nhật**. Các bản cập nhật khả dụng sẽ tự động hiển thị. Nhấp vào **Tải xuống**, rồi **Cài đặt** sau khi quá trình tải xuống hoàn tất.





- Cập nhật qua **terminal**:


Mở terminal, sau đó nhập lệnh sau để cập nhật danh sách các gói có sẵn:



```shell
sudo apt update
```



Nhập mật khẩu và xác nhận. Sau đó cài đặt các bản cập nhật bằng:



```shell
sudo apt full-upgrade
```



## PureOS dành cho phát triển



Theo mặc định, PureOS không bao gồm tất cả các công cụ cần thiết cho quá trình phát triển.


Bạn có thể cài đặt chúng nhanh chóng bằng lệnh sau:



```shell
sudo apt install build-essential git curl
```



Lệnh này sẽ cài đặt các công cụ biên dịch **Git** và **Curl**, hữu ích trong hầu hết các môi trường phát triển.



## Môi trường PureOS



PureOS nổi bật với cách tiếp cận sáng tạo hướng đến sự hội tụ thực sự: một hệ điều hành duy nhất đảm bảo hoạt động mượt mà, liền mạch trên nhiều thiết bị, bao gồm máy tính xách tay, máy tính bảng, máy tính mini và điện thoại thông minh.



Các ứng dụng PureOS được thiết kế để thích ứng: chúng tự động điều chỉnh theo kích thước màn hình và chế độ nhập liệu (cảm ứng hoặc bàn phím/chuột). Ví dụ: trình duyệt web GNOME tự động điều chỉnh Interface để mang lại trải nghiệm tối ưu trên cả thiết bị di động và máy tính để bàn.



PureOS cũng bao gồm bộ ứng dụng văn phòng **LibreOffice**, bao gồm:





- **Writer**: trình xử lý văn bản hoàn chỉnh để tạo và chỉnh sửa tài liệu.
- **Calc**: một chương trình bảng tính mạnh mẽ để quản lý dữ liệu và tính toán của bạn.
- **Impress**: công cụ tạo bài thuyết trình chuyên nghiệp.



Bộ phần mềm miễn phí này cho phép bạn làm việc hiệu quả mà không cần phụ thuộc vào phần mềm độc quyền.



PureOS cung cấp một môi trường thống nhất, an toàn và linh hoạt, dựa trên nền tảng phân phối mã nguồn mở 100%, đảm bảo kiểm soát toàn diện và tôn trọng quyền riêng tư tuyệt đối. Tính hội tụ thực sự của nó tạo điều kiện thuận lợi cho việc tạo ra các ứng dụng tương thích với nhiều loại thiết bị khác nhau, chẳng hạn như máy tính, máy tính bảng và điện thoại thông minh, mà không cần phải điều chỉnh phức tạp.



Với khả năng truy cập trực tiếp vào các công cụ thiết yếu, trình quản lý gói mạnh mẽ và hệ sinh thái nguồn mở phong phú, PureOS đơn giản hóa việc phát triển, thử nghiệm và triển khai ứng dụng trong một môi trường an toàn. Kiến trúc ổn định và khả năng bảo mật Commitment giúp nó trở thành một nền tảng đáng tin cậy cho nhiều mục đích sử dụng, bao gồm phát triển Blockchain, tạo mẫu nhanh hoặc môi trường sản xuất.



Khám phá khóa học của chúng tôi về cách tăng cường bảo mật và bảo vệ quyền riêng tư kỹ thuật số của bạn.



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1