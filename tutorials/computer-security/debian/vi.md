---
name: Debian
description: Một bản phân phối Linux nổi tiếng về tính ổn định, mạnh mẽ và khả năng tương thích.
---

![cover](assets/cover.webp)



Debian là một bản phân phối GNU/Linux miễn phí, nổi tiếng với tính mạnh mẽ và độ tin cậy cao. Nhân Linux và tất cả các gói phần mềm của nó đều được kiểm tra nghiêm ngặt để đảm bảo tính ổn định tuyệt đối và mức độ bảo mật cao. Phù hợp cho cả máy chủ và máy trạm, Debian mang đến trải nghiệm dễ sử dụng và danh mục phần mềm phong phú. Dù bạn đang tìm kiếm một hệ thống an toàn cho mục đích sử dụng hàng ngày hay môi trường sản xuất, Debian là lựa chọn hoàn hảo.



## Tại sao nên chọn Debian?





- **Miễn phí và mở**: Debian hoàn toàn là mã nguồn mở, đảm bảo tính minh bạch và không có phí cấp phép.
- **Tính ổn định và bảo mật**: mọi bản phát hành đều trải qua quá trình thử nghiệm kỹ lưỡng, khiến Debian trở thành một trong những bản phân phối đáng tin cậy và bảo mật nhất trên thị trường.
- **Cộng đồng năng động**: một cộng đồng rộng lớn và tài liệu đầy đủ luôn sẵn sàng hỗ trợ bạn bất cứ khi nào bạn cần.
- **Nhẹ và có khả năng mở rộng**: bạn có thể cài đặt Debian trên các máy có tài nguyên khiêm tốn trong khi vẫn duy trì hiệu suất tốt.
- **Danh mục phần mềm mở rộng**: hơn 50.000 gói phần mềm chính thức có sẵn thông qua kho lưu trữ.



## Chọn đồ họa Interface



Debian cung cấp một số môi trường máy tính để bàn phù hợp với nhu cầu của bạn:





- **GNOME**: Interface hiện đại, trực quan, lý tưởng cho người mới bắt đầu. Giao diện này cung cấp menu đồ họa mượt mà, dễ sử dụng để truy cập các ứng dụng.
- **XFCE**: nhẹ và nhanh, hoàn hảo cho những máy có cấu hình yếu.
- **KDE Plasma**: có khả năng tùy chỉnh cao, với giao diện giống Windows.
- **Cinnamon**: Interface đơn giản, thanh lịch, lấy cảm hứng từ Windows.
- **LXDE / LXQt**: siêu nhẹ, phù hợp với máy tính cũ.
- **MATE**: đơn giản và cổ điển, gần giống với GNOME cũ.



💡 Để có trải nghiệm thoải mái và dễ cầm nắm, **GNOME được khuyến nghị mạnh mẽ**.



## Cài đặt và cấu hình Debian


### Yêu cầu về phần cứng



Trước khi bắt đầu cài đặt, vui lòng đảm bảo rằng bạn có các thiết bị sau:





- **Ổ USB**: Tối thiểu 8 GB để chứa ảnh ISO có thể khởi động.
- **Bộ nhớ truy cập ngẫu nhiên (RAM)**: 4 GB để cài đặt và vận hành trơn tru.
- **Dung lượng đĩa**: ít nhất 15 GB dung lượng trống cho hệ thống và các bản cập nhật.



### Tải xuống



Việc lựa chọn ảnh Debian phụ thuộc vào kiến trúc bộ xử lý của bạn:





- **AMD64**: tải xuống phiên bản "live hybrid" từ danh sách [tải xuống](https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- **ARM64**: lấy ảnh DVD từ trang web chính thức [Debian](https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- **Các kiến trúc khác**: tìm ISO tương ứng với kiến trúc của bạn [tại đây](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Tạo khóa USB có thể khởi động



Sau khi tải xuống ảnh ISO phù hợp, hãy tiến hành tạo phương tiện cài đặt:




- Tải xuống **Balena Etcher** từ [trang web chính thức](https://etcher.balena.io/), sau đó lấy tệp nhị phân cho hệ thống của bạn và cài đặt.



![etcher](assets/fr/02.webp)





- **Khởi chạy Etcher**: mở phần mềm và chọn ảnh ISO Debian đã tải xuống trước đó.
- Chọn khóa USB: chỉ định khóa của bạn (8 GB+) làm mục tiêu.
- **Bắt đầu flash**: nhấp vào **Flash!** và đợi cho đến khi quá trình hoàn tất.



![flash](assets/fr/03.webp)



Bây giờ USB của bạn đã sẵn sàng để bắt đầu cài đặt Debian.



## Cài đặt Debian trên hệ thống của bạn



### Khởi động từ ổ USB



Để khởi chạy cài đặt từ ổ USB của bạn:




- **Tắt hoàn toàn** máy tính.
- **Khởi động lại** sau đó truy cập BIOS/UEFI bằng cách nhấn ngay `ESC`, `F2`, `F11` (hoặc phím chuyên dụng tùy thuộc vào thương hiệu của bạn).
- Trong menu khởi động, **chọn ổ USB** của bạn làm thiết bị khởi động.
- **Xác nhận** bằng phím Enter để bắt đầu trên ảnh Debian: thao tác này sẽ đưa bạn đến màn hình chào mừng của trình cài đặt.



### Khởi chạy cài đặt



Màn hình bắt đầu:



![starting](assets/fr/04.webp)



Khi khởi động từ ổ USB, màn hình chào mừng của Debian cung cấp một số tùy chọn:




- **Live System**: khởi chạy Debian mà không cần cài đặt, lý tưởng để thử nghiệm môi trường.
- **Khởi động Trình cài đặt**: bắt đầu cài đặt trực tiếp trên đĩa Hard.
- **Tùy chọn cài đặt nâng cao**: cho phép bạn truy cập vào các chế độ cài đặt tùy chỉnh.



Để khám phá Debian ở chế độ trực tiếp, hãy chọn **Hệ thống Trực tiếp** và xác nhận bằng **Enter**. Sau đó, bạn có thể khởi chạy cài đặt bằng cách nhấp vào **Cài đặt Debian** trong môi trường trực tiếp.



![system](assets/fr/05.webp)





- Lựa chọn ngôn ngữ (tùy chọn)



Chọn ngôn ngữ chính của hệ thống Debian từ danh sách, sau đó nhấp vào OK.



![language](assets/fr/06.webp)





- **Múi giờ** (GMT)



Chọn khu vực địa lý của bạn để tự động đặt ngày và giờ.



![timezone](assets/fr/07.webp)





- Bố cục bàn phím



Chọn ngôn ngữ và bố cục bàn phím. Sử dụng trường kiểm tra tích hợp để kiểm tra xem mỗi phím có tạo ra ký tự mong muốn hay không.



![keyboard](assets/fr/08.webp)



### Phân vùng đĩa





- **Xóa đĩa**: nếu bạn có phân vùng chuyên dụng, tùy chọn này sẽ xóa toàn bộ nội dung của phân vùng đó.
- **Phân vùng thủ công**: chọn tùy chọn này để tạo, thay đổi kích thước hoặc xóa phân vùng theo nhu cầu.



![disk](assets/fr/09.webp)





- Tạo tài khoản người dùng



Nhập họ tên đầy đủ, tên tài khoản và mật khẩu mạnh để đảm bảo phiên đăng nhập của bạn được an toàn.



![user](assets/fr/10.webp)





- Tóm tắt tham số



Tóm tắt các lựa chọn của bạn sẽ được hiển thị: hãy kiểm tra từng mục và quay lại để sửa đổi nếu cần.



![settings](assets/fr/11.webp)





- Khởi chạy cài đặt



Nhấp vào **Cài đặt** để bắt đầu sao chép tệp và cấu hình hệ thống, sau đó đợi cho đến khi quá trình hoàn tất.



![install](assets/fr/12.webp)





- **Khởi động lại**



Sau khi cài đặt hoàn tất, hãy khởi động lại máy tính để áp dụng mọi cấu hình và truy cập hệ thống Debian mới của bạn.



![restart](assets/fr/13.webp)



Khi khởi động, hãy nhập tên người dùng và mật khẩu để truy cập hệ thống.



![login](assets/fr/14.webp)



## Cập nhật hệ thống



Trước khi bắt đầu sử dụng hệ thống, việc cập nhật hệ thống là vô cùng quan trọng. Điều này cho phép bạn tận dụng các bản vá phần mềm mới nhất, kho lưu trữ cập nhật và trong một số trường hợp, cả bản vá bảo mật cho chính hệ điều hành.



### Tùy chọn 1: Cập nhật thông qua Interface đồ họa (GNOME)



Nếu bạn đã cài đặt Debian với môi trường máy tính để bàn GNOME, bạn có thể thực hiện cập nhật bằng giao diện đồ họa. Để thực hiện việc này, hãy mở ứng dụng **Phần mềm**, sau đó chuyển đến tab **Cập nhật**. Sau đó, nhấp vào **Khởi động lại và cập nhật** để bắt đầu quá trình.



### Tùy chọn 2: Cập nhật qua thiết bị đầu cuối (khuyến nghị)



Phương pháp này cung cấp khả năng kiểm soát toàn diện hơn. Nó cho phép bạn cập nhật kho lưu trữ, gói phần mềm và nếu cần, cả kernel.




- Mở terminal bằng phím tắt `Ctrl + Alt + T`.
- Cập nhật danh sách các gói có sẵn bằng lệnh sau:



```shell
sudo apt update
```



Nhập mật khẩu khi được yêu cầu (lưu ý rằng sẽ không có ký tự nào hiển thị khi bạn nhập - đây là điều bình thường).





- Để cài đặt các bản cập nhật có sẵn:



```shell
sudo apt full-upgrade
```



## Khám phá các nhiệm vụ cơ bản



### Duyệt Internet



Trình duyệt web mặc định trên Debian là **Firefox**. Nếu bạn thích trình duyệt khác, bạn có thể cài đặt trình duyệt khác, miễn là nó có sẵn trong kho lưu trữ Debian (như Chromium, Brave...).



### Xử lý văn bản



Bộ phần mềm **LibreOffice** được cài đặt theo mặc định trên Debian.





- Để viết tài liệu, hãy sử dụng **LibreOffice Writer**, tương đương với Microsoft Word.
- Đối với bảng tính, **LibreOffice Calc** hoạt động như một giải pháp thay thế cho Excel.
- Cuối cùng, **LibreOffice Impress** cho phép bạn tạo bài thuyết trình, giống như PowerPoint.



## Cài đặt ứng dụng



Có hai cách để cài đặt ứng dụng trên Debian:



### Phương pháp đồ họa:



Bạn có thể sử dụng **trình quản lý phần mềm** (có thể truy cập thông qua giao diện đồ họa Interface) để dễ dàng tìm kiếm và cài đặt ứng dụng.



### Phương pháp dòng lệnh:



Nếu ứng dụng bạn đang tìm kiếm không xuất hiện trong giao diện đồ họa Interface hoặc nếu bạn thích sử dụng thiết bị đầu cuối, hãy sử dụng lệnh sau:



```shell
sudo apt install <name>
```



Thay thế `<tên>` bằng tên gói. Ví dụ: để cài đặt `curl`:



```shell
sudo apt install curl
```



### Cài đặt gói tải xuống thủ công:



Nếu bạn đã tải xuống tệp `.deb` (gói Debian), bạn có thể cài đặt tệp đó bằng lệnh sau:



```shell
sudo apt install ./name.deb
```



https://planb.academy/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Hệ thống Debian của bạn hiện đã được cài đặt và sẵn sàng để sử dụng cho các tác vụ hàng ngày.


Nhờ môi trường máy tính để bàn **GNOME**, bạn có thể truy cập vào nhiều ứng dụng thông qua giao diện đồ họa thân thiện với người dùng Interface, lý tưởng cho cả người mới bắt đầu và người dùng nâng cao.



Bạn cũng có thể thay đổi môi trường máy tính để bàn (ví dụ: sang XFCE, KDE, v.v.) mà không cần cài đặt lại Debian. Để thực hiện việc này, chỉ cần sử dụng terminal và cài đặt môi trường mới theo ý muốn.



Để tìm hiểu thêm về Debian và nói chung là về các bản phân phối GNU/Linux, tôi khuyên bạn nên tham khảo khóa học này:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1