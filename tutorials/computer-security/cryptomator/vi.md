---
name: Cryptomator
description: Mã hóa các tập tin của bạn trên đám mây
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Florian BURNEL được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc có thể đã được chỉnh sửa.*



___



## I. Trình bày



Trong hướng dẫn này, chúng ta sẽ sử dụng ứng dụng Cryptomator để mã hóa dữ liệu được lưu trữ trên Đám mây, cho dù trên Microsoft OneDrive, Google Drive, Dropbox, Box hay thậm chí là iCloud.



Mã hóa dữ liệu bạn lưu trữ trên các giải pháp lưu trữ trực tuyến như Drive là cách tốt nhất để bảo vệ tệp và quyền riêng tư của bạn. Nhờ mã hóa, bạn là người duy nhất có thể giải mã và đọc dữ liệu của mình, ngay cả khi dữ liệu được lưu trữ trên máy chủ ở Hoa Kỳ hoặc một quốc gia khác trên thế giới.



Trong phần trình diễn này, chúng tôi sẽ sử dụng máy tính Windows 11 22H2 với OneDrive, nhưng quy trình này cũng tương tự trên các phiên bản Windows và dịch vụ lưu trữ khác. Tất cả những gì bạn cần làm là cài đặt ứng dụng đồng bộ hóa và thêm tài khoản của mình. Thao tác này sẽ cho phép Cryptomator lưu trữ dữ liệu trong kho lưu trữ.



![Image](assets/fr/020.webp)



Cryptomator là một lựa chọn thay thế cho các ứng dụng khác, đặc biệt là Picocrypt được trình bày trong một bài viết khác, trông khác biệt nhưng cũng dễ sử dụng. Cryptomator cũng **mã nguồn mở**, tuân thủ RGPD và sẽ **mã hóa dữ liệu bằng thuật toán mã hóa AES-256 bit**. Ngược lại, Picocrypt dựa trên thuật toán XChaCha20 nhanh hơn (cũng 256 bit).



https://planb.academy/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Ứng dụng Cryptomator có sẵn trên **Windows** (exe / msi), **Linux**, **macOS,** cũng như **Android** và **iOS**. Nhân tiện, tất cả các ứng dụng đều miễn phí, ngoại trừ ứng dụng Android, bạn phải trả phí (14,99 euro).



Trên máy của bạn, **Cryptomator sẽ tạo một thư mục để tạo một két an toàn**. Trong két an toàn này, có thể được lưu trữ trên OneDrive, Google Drive hoặc các dịch vụ tương tự, dữ liệu của bạn sẽ được mã hóa. Vì vậy, nếu bạn lưu trữ tất cả dữ liệu trong két an toàn được lưu trữ trên không gian lưu trữ Drive của mình, dữ liệu sẽ được bảo vệ (vì đã được mã hóa).



**Lưu ý**: Bài viết này sử dụng các dịch vụ lưu trữ trực tuyến làm ví dụ, nhưng Cryptomator có thể được sử dụng để mã hóa dữ liệu trên ổ đĩa cục bộ, ổ đĩa ngoài hoặc thậm chí là NAS. Thực tế, không có bất kỳ hạn chế nào.



## II. Cài đặt Cryptomator



Để bắt đầu, bạn cần **tải xuống** và **cài đặt** **Cryptomator**. Sau khi tải xuống hoàn tất, chỉ cần vài cú nhấp chuột là có thể hoàn tất cài đặt. Giống như [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), Cryptomator sẽ dựa vào WinFsp để **gắn ổ đĩa ảo trên máy tính Windows của bạn**.





- [Tải xuống Cryptomator từ trang web chính thức](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Sử dụng Cryptomator trên Windows



### A. Tạo một két an toàn mới



Để tạo két an toàn mới, hãy nhấp vào nút "**Thêm**" và chọn "**Két an toàn mới...**". Các két an toàn hiện có và đã biết của bạn trên máy này sẽ xuất hiện trong Interface, bên trái. **Một két an toàn được tạo trên máy A có thể được mở và sửa đổi trên máy B**, miễn là máy được trang bị Cryptomator (và biết khóa mã hóa).



![Image](assets/fr/015.webp)



Bắt đầu bằng cách đặt tên cho vault, ví dụ: "**IT-Connect**". Thao tác này sẽ tạo một thư mục có tên "**IT-Connect**" trong OneDrive của tôi.



![Image](assets/fr/011.webp)



Ở bước tiếp theo, Cryptomator có thể sẽ **phát hiện "Ổ đĩa"** hiện có trên máy của bạn: Google Drive, OneDrive, Dropbox, v.v... Để cho phép bạn chọn trực tiếp nhà cung cấp. Tôi đã thử điều này trên hai máy Windows 11 khác nhau, với nhiều ổ đĩa, và nó không được phát hiện. Không vấn đề gì, chỉ cần xác định "**Vị trí tùy chỉnh**" và chọn thư mục gốc của không gian lưu trữ. Ví dụ: **C:\Users\<Tên người dùng>\OneDrive**.



![Image](assets/fr/018.webp)



Tiếp theo, bạn có thể điều chỉnh tùy chọn trong cài đặt chuyên gia.



![Image](assets/fr/021.webp)



Tiếp theo, bạn cần định nghĩa **mật khẩu tương ứng với khóa mã hóa**. Mật khẩu này sẽ cho phép bạn **mở khóa két Cryptomator** và truy cập dữ liệu bên trong. **Nếu bạn làm mất nó, bạn sẽ mất quyền truy cập vào dữ liệu**. Cuối cùng, bạn vẫn có tùy chọn **tạo khóa dự phòng** bằng cách chọn tùy chọn "**Đúng vậy, phòng còn hơn chữa bệnh**", tương tự như khóa khôi phục [BitLocker](https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Điều này rất đáng làm, nhưng đừng lưu khóa dự phòng này ở thư mục gốc của OneDrive!



Nhấp vào "**Tạo két an toàn**".



![Image](assets/fr/019.webp)



Sao chép khóa khôi phục và lưu vào trình quản lý mật khẩu yêu thích của bạn. Nhấp vào "**Tiếp theo**".



![Image](assets/fr/013.webp)



Vậy là xong, cốp xe mới của bạn đã được tạo và sẵn sàng để sử dụng!



![Image](assets/fr/014.webp)



### B. Số liệu truy cập



Để truy cập két sắt và dữ liệu bên trong, để **đọc dữ liệu hiện có hoặc thêm dữ liệu mới**, bạn cần phải **mở khóa** két sắt. Cryptomator liệt kê các két sắt đã biết: két sắt IT-Connect sẽ xuất hiện, vì vậy chỉ cần chọn nó và nhấp vào "**Mở khóa**".



![Image](assets/fr/016.webp)



Bạn phải nhập mật khẩu để mở khóa két. Sau đó nhấp vào "**Tháo ổ đĩa**".



![Image](assets/fr/022.webp)



**Két sắt của bạn được gắn trên máy tính Windows dưới dạng ổ đĩa ảo.** Ổ đĩa này, ở đây kế thừa chữ E, cho phép bạn truy cập dữ liệu của mình (ở dạng văn bản thuần túy, vì két sắt đã được mở khóa).



![Image](assets/fr/017.webp)



Về phía OneDrive, chúng ta không thể duyệt trực tiếp kho lưu trữ Cryptomator. Chúng ta không thể xem dữ liệu (cả tên tệp lẫn nội dung). Điều này có nghĩa là bạn không cần phải thêm dữ liệu vào kho lưu trữ Cryptomator thông qua phím tắt OneDrive thông thường. **Bạn phải thêm dữ liệu bằng ổ đĩa ảo của Cryptomator.**



![Image](assets/fr/012.webp)



### C. Tùy chọn cốp xe



Cài đặt của két an toàn được truy cập thông qua nút "**Tùy chọn ổ đĩa được mã hóa**" (khi đã khóa) và sẽ tự động khóa khi không hoạt động, tương tự như bạn vẫn làm với két an toàn có mật khẩu. Tùy chọn "**Mở khóa ổ đĩa được mã hóa khi khởi động**", đúng như tên gọi, sẽ mở khóa ổ đĩa mà không cần bạn can thiệp, và gắn ổ đĩa ảo. Vì lý do bảo mật, tốt nhất bạn nên tránh kích hoạt tùy chọn này.



Thông qua tab "**Gắn kết**", bạn cũng có thể quyết định gắn kết ở chế độ chỉ đọc hoặc gán một chữ cái cụ thể.



![Image](assets/fr/024.webp)



Ngoài ra, trong cài đặt Cryptomator, bạn có thể **bật tính năng tự động khởi động ứng dụng**.



## IV. Kết luận



Với **Cryptomator**, bạn có thể **tạo một két an toàn được mã hóa** chỉ trong vài phút để bảo vệ dữ liệu bạn muốn lưu trữ trên OneDrive và các dịch vụ lưu trữ đám mây khác. Việc "ghép nối" nó với một ổ đĩa rất dễ sử dụng: vì mục đích này, tôi thích Cryptomator hơn Picocrypt.