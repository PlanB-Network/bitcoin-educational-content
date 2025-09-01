---
name: Fedora
description: Bản phân phối Linux cung cấp cho bạn không gian làm việc miễn phí, đầy đủ và an toàn.
---


![cover](assets/cover.webp)





Fedora là một hệ điều hành mã nguồn mở, miễn phí dựa trên Linux, ra mắt năm 2003, được phát triển bởi cộng đồng **Dự án Fedora** và được hỗ trợ bởi **Red Hat Linux**. Hệ điều hành này nổi tiếng với tính ổn định, hiệu năng tốt và dễ sử dụng, khiến nó trở thành một lựa chọn tuyệt vời cho cả người dùng mới bắt đầu và người dùng nâng cao. Hệ thống chạy trên hầu hết các kiến trúc bộ xử lý hiện đại, giúp dễ dàng cài đặt trên hầu hết mọi máy tính. Fedora cũng có sẵn trong một số phiên bản được cấu hình sẵn, được gọi là "Fedora Spins" hoặc "Fedora Editions", được thiết kế cho các nhu cầu cụ thể (trò chơi điện tử, thiên văn học, phát triển...).



## Kiến trúc Fedora Linux



Như bạn đã đọc trước đó, Fedora là một hệ điều hành miễn phí dựa trên nhân Linux. Nhân Linux là một phần của hệ điều hành, giao tiếp với phần cứng máy tính và quản lý tài nguyên hệ thống như bộ nhớ và sức mạnh xử lý.



Fedora Linux bao gồm nhiều công cụ phần mềm và ứng dụng cần thiết để chạy hệ điều hành trên nhân Linux. Kiến trúc mô-đun của Fedora chủ yếu bao gồm một tập hợp các thành phần riêng lẻ có thể dễ dàng thêm vào, gỡ bỏ hoặc thay thế khi cần thiết. Điều này cho phép bạn định hình hệ điều hành chỉ bằng cách sử dụng các tài nguyên bạn cần.



Fedora cũng bao gồm một môi trường desktop, đó là Interface, nơi người dùng thực hiện các tác vụ và truy cập các ứng dụng. Môi trường desktop mặc định của Fedora là GNOME, một môi trường desktop thân thiện với người dùng, dễ sử dụng và có khả năng tùy chỉnh cao.



## Tại sao nên chọn Fedora?



Trong số rất nhiều bản phân phối Linux hiện có, Fedora nổi bật đặc biệt ở:





- Tính mô-đun**: Tương thích với nhiều kiến trúc bộ xử lý khác nhau, Fedora có thể được cài đặt trên hầu hết các máy tính, kể cả máy tính có công suất thấp, đáp ứng hoàn hảo nhu cầu của bạn.





- Interface** đơn giản, trực quan: Fedora kết hợp Interface đồ họa hiện đại với Interface dòng lệnh mạnh mẽ, giúp dễ sử dụng cho mọi cấu hình.





- Tính ổn định của hạt nhân**: Dựa trên Red Hat, Fedora nổi tiếng về độ tin cậy của các bản cập nhật, đặc biệt là các bản cập nhật hạt nhân, được thực hiện mà không có lỗi lớn nhờ vào sự đóng góp miễn phí từ một cộng đồng lớn.





- Cài đặt nhanh chóng, dễ dàng**: với kích thước ảnh chỉ 3 GB, việc cài đặt diễn ra nhanh chóng và dễ dàng, ngay cả trên những máy có tài nguyên hạn chế.



## Các phiên bản Fedora



Tùy thuộc vào hồ sơ và cách sử dụng của bạn, Fedora cung cấp các phiên bản phù hợp với nhu cầu của bạn. Bạn sẽ chủ yếu tìm thấy:





- Fedora Workstation**: Lý tưởng cho mục đích sử dụng cá nhân và/hoặc chuyên nghiệp trên máy tính của bạn, phiên bản này được cài đặt các tiện ích chung như trình duyệt, bộ ứng dụng văn phòng (trình soạn thảo văn bản) và phần mềm phát phương tiện.





- Fedora Server**: Phiên bản này dành riêng cho việc quản lý máy chủ. Fedora Server bao gồm nhiều công cụ giúp bạn triển khai và quản lý máy chủ theo quy mô của riêng mình.





- Fedora CoreOS**: Bạn muốn dễ dàng chạy và triển khai các ứng dụng đám mây? Fedora CoreOS là phiên bản cung cấp cho bạn các công cụ để tạo và quản lý hình ảnh với Docker và Kubernets chẳng hạn.



Trong hướng dẫn này, chúng ta sẽ thực hiện trên phiên bản Fedora Workstation. Tuy nhiên, các quy trình chi tiết bên dưới cũng tương tự đối với các phiên bản khác.



## Cài đặt và cấu hình Fedora Workstation



Để cài đặt Fedora Workstation cần có cấu hình phần cứng sau:




- Một ổ USB có dung lượng tối thiểu **8 GB** để khởi động hệ điều hành.
- Ít nhất **40 GB dung lượng trống** trên ổ đĩa Hard của máy tính.
- RAM 4 GB** cho trải nghiệm mượt mà.



### Tải xuống Fedora Workstation



Bạn có thể tải xuống phiên bản [Fedora Workstation] (https://fedoraproject.org/fr/workstation/download) từ trang web chính thức của dự án Fedora. Sau đó, chọn phiên bản tương ứng với kiến trúc bộ xử lý của bạn (32-bit - 64-bit) và nhấp vào biểu tượng **Tải xuống**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Tạo một khóa USB có thể khởi động



Để cài đặt Fedora, bạn cần tạo một khóa USB có thể khởi động bằng phần mềm như [Balena Etcher](https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Sau khi cài đặt xong Balena Etcher, hãy mở ứng dụng và chọn ảnh ISO Fedora Workspace đã tải xuống. Chọn ổ USB làm phương tiện đích và nhấp vào nút **Flash** để bắt đầu tạo khóa khởi động.



![boot](assets/fr/05.webp)


### Cài đặt Fedora



Khi bạn khởi động xong USB, hãy tắt máy tính.


Bật máy tính, sau đó truy cập BIOS trong khi khởi động bằng cách nhấn phím `F2`, `F12` hoặc `ESC`, tùy thuộc vào máy tính của bạn.



Trong tùy chọn khởi động, hãy chọn ổ USB của bạn làm thiết bị khởi động chính. Sau khi xác nhận lựa chọn này, máy tính của bạn sẽ khởi động lại và tự động chạy trình cài đặt Fedora** có trên ổ USB.



Sau khi máy tính của bạn khởi động từ ổ USB, màn hình **GRUB** sẽ xuất hiện.



Ở giai đoạn này, bạn có các lựa chọn sau:




- Kiểm tra phương tiện**: Tùy chọn này cho phép bạn kiểm tra tính toàn vẹn của ổ USB và đảm bảo tất cả các thành phần phụ thuộc cần thiết cho quá trình cài đặt chính xác đều có sẵn. Đây là bước tùy chọn, nhưng được khuyến nghị nếu bạn có bất kỳ nghi ngờ nào về ổ USB.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Khởi động Fedora**: Thao tác này sẽ khởi chạy Fedora ở chế độ "trực tiếp", không cần cài đặt.



Trên màn hình Fedora (chế độ trực tiếp), nhấp vào **Cài đặt Fedora** (hoặc Cài đặt trên đĩa Hard) để bắt đầu quá trình cài đặt. Bạn có thể chọn cài đặt sau và dùng thử Fedora mà không cần cài đặt.



![install-live](assets/fr/08.webp)



Bước đầu tiên là chọn **ngôn ngữ cài đặt** và **bố cục bàn phím** của Fedora



![language](assets/fr/10.webp)





- Chọn đĩa cài đặt:



Chọn đĩa Hard mà bạn muốn cài đặt Fedora.



Nếu ổ đĩa trống, Fedora sẽ tự động sử dụng toàn bộ dung lượng trống. Nếu không, bạn có thể tùy chỉnh phân vùng (thủ công hoặc tự động).



![disk](assets/fr/11.webp)





- Mã hóa:



Ở giai đoạn này, Fedora đề xuất mã hóa ổ đĩa của bạn để tăng cường bảo mật Layer. Điều này đảm bảo dữ liệu của bạn chỉ có thể được đọc bởi hệ thống Fedora của bạn.



![chiffrement](assets/fr/12.webp)



Trước khi khởi chạy cài đặt, Fedora sẽ hiển thị tóm tắt các lựa chọn của bạn. Xác nhận và nhấp vào nút cài đặt để bắt đầu cài đặt Fedora.



![resume](assets/fr/13.webp)



Trong quá trình cài đặt, Fedora sẽ sao chép các tập tin và cấu hình hệ thống. Khi hoàn tất, máy tính sẽ tự động khởi động lại.



![installation](assets/fr/14.webp)



### Cấu hình cơ bản


Khi sử dụng lần đầu, bạn sẽ cần hoàn thiện một số cài đặt sau:




- Thay đổi ngôn ngữ hệ thống nếu cần thiết.



![language](assets/fr/15.webp)





- Chọn bố cục bàn phím phù hợp với sở thích của bạn.



![keyboard](assets/fr/16.webp)





- Chọn múi giờ của bạn bằng cách nhập tên thành phố vào thanh tìm kiếm, sau đó nhấp vào gợi ý tương ứng.



![timezone](assets/fr/17.webp)





 - Bật hoặc tắt quyền truy cập vào vị trí của bạn cho các ứng dụng cần quyền này, cũng như tự động gửi báo cáo lỗi.



![location](assets/fr/18.webp)





- Quyết định xem bạn có muốn bật kho lưu trữ phần mềm của bên thứ ba hay không.



![logs](assets/fr/19.webp)





- Nhập tên đầy đủ của bạn và xác định tên người dùng cho tài khoản của bạn.



![name](assets/fr/20.webp)





- Tạo mật khẩu an toàn cho phiên làm việc của bạn: càng dài càng tốt (tối thiểu 20 ký tự), càng ngẫu nhiên càng tốt và bao gồm nhiều ký tự (chữ thường, chữ hoa, số và ký hiệu). Nhớ lưu mật khẩu của bạn.



![mdp](assets/fr/21.webp)



Sau khi hoàn tất tất cả các bước này, hãy khởi chạy Fedora và bắt đầu sử dụng ngay lập tức mà không cần khởi động lại nữa.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Sau khi hoàn tất quá trình cài đặt, bạn có thể tham khảo một số tiện ích đã được cài đặt sẵn trong nhà Interface của mình.



![install-now](assets/fr/09.webp)



## Khám phá các nhiệm vụ cơ bản



### Duyệt Internet


Trình duyệt mặc định của Fedora là Firefox. Trình duyệt này dễ sử dụng và phù hợp với hầu hết các nhu cầu.


Nếu bạn thích trình duyệt khác, bạn có thể cài đặt từ **trình quản lý phần mềm** hoặc thông qua **thiết bị đầu cuối**.


### Xử lý văn bản


Fedora mặc định bao gồm bộ ứng dụng văn phòng **LibreOffice**, cung cấp một số công cụ hữu ích:




- Writer** để xử lý văn bản.
- Calc** dành cho bảng tính.
- Impress** để tạo bài thuyết trình.


## Cài đặt ứng dụng


Để cài đặt ứng dụng mới, bạn có thể sử dụng **trình quản lý phần mềm** của Fedora (gọi là _Software_), giúp việc cài đặt dễ dàng và trực quan hơn. Tuy nhiên, sử dụng **terminal** thường nhanh hơn và chính xác hơn.



Trước khi cài đặt bất kỳ phần mềm nào, hãy luôn nhớ cập nhật **kho lưu trữ** để đảm bảo bạn có quyền truy cập vào phiên bản mới nhất.



Sau đó sử dụng lệnh sau để khởi chạy cài đặt ứng dụng mong muốn:


sudo dnf cài đặt phần mềm_tên`


## Cập nhật hệ điều hành của bạn


Sau khi cài đặt, điều quan trọng là phải cập nhật Fedora để tận dụng các bản vá bảo mật và cập nhật phần mềm mới nhất.


### Tùy chọn 1: Thông qua đồ họa Interface




- Mở **Cài đặt** của Fedora, sau đó đi tới phần **Hệ thống**.
- Nhấp vào **Cập nhật phần mềm**.
- Bắt đầu tải xuống các bản cập nhật và đợi cho đến khi quá trình hoàn tất.



Có thể cần phải **khởi động lại** sau khi cài đặt bản cập nhật.


### Tùy chọn 2: Qua thiết bị đầu cuối




- Mở terminal và bắt đầu bằng cách cập nhật **kho lưu trữ** để đảm bảo bạn có phiên bản mới nhất của:



```shell
sudo dnf check-update
```





- Tiếp theo, cập nhật tất cả phần mềm đã cài đặt bằng lệnh sau:



```shell
sudo dnf upgrade
```



Giờ đây, hệ thống Fedora của bạn đã được cập nhật và sẵn sàng sử dụng cho mọi tác vụ hàng ngày. Khám phá hướng dẫn của chúng tôi về Linux Mint, một bản phân phối Linux khác, và cách thiết lập một môi trường an toàn và lành mạnh cho các giao dịch Bitcoin của bạn.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5