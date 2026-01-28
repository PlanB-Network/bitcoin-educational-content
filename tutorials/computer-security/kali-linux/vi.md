---
name: Kali
description: Cài đặt Kali Linux trên VirtualBox dưới dạng ổ USB có thể khởi động hoặc khởi động kép, từng bước.
---

![cover-kali](assets/cover.webp)



## Giới thiệu



### Tại sao lại là Kali Linux?



**Kali Linux** là bản phân phối Linux chuyên về bảo mật CNTT.


Sau đây là lý do tại sao chúng tôi sử dụng Kali Linux:





- Nó được cấu hình sẵn với nhiều công cụ kiểm tra thâm nhập (kiểm tra bảo mật hệ thống và mạng).
- Đây là **mã nguồn mở và miễn phí**, vì vậy bạn có thể sử dụng và sửa đổi nó một cách thoải mái.
- **Đáng tin cậy và an toàn**, lý tưởng để tìm hiểu về an ninh mạng.
- Nó cho phép bạn học cách sử dụng Linux trong môi trường sẵn sàng để kiểm tra.
- Có thể cài đặt theo nhiều cách khác nhau: **VirtualBox**, **khóa USB có thể khởi động** hoặc **khởi động kép**.



## Cài đặt và cấu hình



### 1. Điều kiện tiên quyết



**Thiết bị cần thiết:**





- Bộ xử lý 64-bit** (Intel hoặc AMD).
- Tối thiểu 8 GB RAM** (4 GB có thể đủ cho cài đặt nhẹ hoặc VM).
- 50 GB dung lượng đĩa trống** để cài đặt Kali Linux.
- Kết nối Internet** để tải xuống ảnh ISO và bản cập nhật.
- USB tối thiểu 8 GB** để tạo phương tiện có thể khởi động (nếu bạn muốn cài đặt Kali trên PC hoặc thử nghiệm trên Live USB).



Điều quan trọng là phải sao lưu dữ liệu trước khi cài đặt trên máy tính hiện có.



### 2. Tải xuống





- Truy cập [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Chọn ảnh ISO cho ứng dụng của bạn:
  - Cài đặt Image**: để cài đặt trên PC.
  - Virtual Image**: để cài đặt Kali trên VirtualBox hoặc VMware.
- Tải xuống hình ảnh ISO.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Tạo khóa USB có thể khởi động



Bạn có thể sử dụng một số công cụ, chẳng hạn như Balena Etcher:





- Tải xuống và cài đặt [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Mở Balena Etcher, sau đó chọn ảnh Kali ISO.
- Chọn USB làm phương tiện đích.
- Nhấp vào Flash và đợi quá trình hoàn tất.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Cài đặt và bảo mật Kali Linux



#### 4.1 Khởi động bằng ổ USB





- Tắt máy tính.
- Cắm USB (có chứa Kali Linux).
- Bật máy tính. Trên các máy tính đời mới, hệ thống sẽ tự động nhận dạng khóa khởi động USB. Nếu không, hãy khởi động lại bằng cách giữ phím truy cập BIOS/UEFI (thường là F2, F12 hoặc Delete, tùy thuộc vào thương hiệu).
  - Trong menu BIOS/UEFI, chọn ổ USB của bạn làm thiết bị khởi động.
  - Lưu và khởi động lại.



#### 4.2 Khởi chạy cài đặt



##### Màn hình khởi động



Khi khởi động từ ổ USB, màn hình khởi động Kali Linux sẽ xuất hiện. Chọn giữa **cài đặt đồ họa** hoặc **cài đặt văn bản**. Trong ví dụ này, chúng tôi đã chọn cài đặt đồ họa.



![capture](assets/fr/06.webp)



Nếu bạn sử dụng hình ảnh **Live**, bạn sẽ thấy một chế độ khác, **Live**, đây cũng là tùy chọn khởi động mặc định.



![Mode Live](assets/fr/07.webp)



##### Lựa chọn ngôn ngữ



Chọn ngôn ngữ bạn muốn cài đặt và hệ thống.



![Sélection de la langue](assets/fr/08.webp)



Vui lòng ghi rõ vị trí địa lý của bạn.



![Options d'accessibilité](assets/fr/09.webp)



##### Cấu hình bàn phím



Chọn bố cục bàn phím của bạn. Có một trường kiểm tra để kiểm tra xem các phím có tương thích với cấu hình của bạn không.



![Configuration du clavier](assets/fr/10.webp)



##### Kết nối mạng



Quá trình cài đặt sẽ quét các giao diện mạng của bạn, tìm kiếm dịch vụ DHCP, sau đó yêu cầu bạn nhập tên máy chủ cho hệ thống. Trong ví dụ dưới đây, chúng tôi đã nhập **"kali "** làm tên máy chủ.



![Configuration réseau](assets/fr/11.webp)



Bạn có thể tùy chọn cung cấp tên miền mặc định mà hệ thống này sẽ sử dụng (giá trị có thể được lấy từ DHCP hoặc nếu đã có hệ điều hành trước đó).



![Choix du type d'installation](assets/fr/12.webp)



##### Tài khoản người dùng



Tiếp theo, tạo tài khoản người dùng cho hệ thống (họ tên đầy đủ, tên người dùng và mật khẩu mạnh).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Múi giờ



Chọn khu vực địa lý của bạn để thiết lập thời gian hệ thống.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Loại phân vùng



Trình cài đặt sau đó sẽ quét đĩa của bạn và hiển thị một số tùy chọn tùy thuộc vào cấu hình của bạn.



Trong hướng dẫn này, chúng ta bắt đầu từ một **đĩa trống**, cung cấp **bốn lựa chọn khả thi**.


Chúng ta sẽ chọn **Hướng dẫn - sử dụng toàn bộ đĩa**, vì ở đây chúng ta đang thực hiện cài đặt Kali Linux một lần (khởi động một lần). Điều này có nghĩa là không có hệ điều hành nào khác được giữ lại và toàn bộ đĩa có thể bị xóa.



Nếu đĩa của bạn đã chứa dữ liệu, tùy chọn bổ sung **Có hướng dẫn - sử dụng không gian trống liền kề lớn nhất** có thể được hiển thị.



Giải pháp thay thế này cho phép bạn cài đặt Kali Linux mà không xóa dữ liệu hiện có, lý tưởng để khởi động kép với một hệ thống khác.



Trong trường hợp của chúng tôi, đĩa trống nên tùy chọn này không xuất hiện.



![Choix du partitionnement](assets/fr/17.webp)



Chọn đĩa cần phân vùng.



![capture](assets/fr/18.webp)



Tùy thuộc vào nhu cầu, bạn có thể chọn giữ tất cả các tệp của mình trong một phân vùng duy nhất (hành vi mặc định) hoặc có các phân vùng riêng cho một hoặc nhiều thư mục cấp cao nhất.



Nếu bạn không chắc chắn về điều mình muốn, hãy chọn tùy chọn **Tất cả tệp trong một phân vùng**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Sau đó, bạn sẽ có cơ hội cuối cùng để kiểm tra cấu hình ổ đĩa trước khi chương trình cài đặt thực hiện bất kỳ thay đổi không thể đảo ngược nào. Sau khi bạn nhấp vào _Tiếp tục_, chương trình cài đặt sẽ khởi chạy và quá trình cài đặt gần như hoàn tất.



![capture](assets/fr/21.webp)



##### LVM được mã hóa



Nếu tùy chọn này được bật ở bước trước, Kali Linux sẽ thực hiện xóa ổ cứng an toàn trước khi yêu cầu bạn nhập mật khẩu LVM.



Vui lòng sử dụng mật khẩu mạnh, nếu không, cảnh báo về passphrase yếu sẽ được hiển thị.



##### Thông tin proxy



Kali Linux sử dụng kho lưu trữ để phân phối ứng dụng. Bạn sẽ cần nhập thông tin proxy cần thiết nếu môi trường của bạn sử dụng kho lưu trữ.



Nếu bạn **không chắc** có nên sử dụng proxy hay không, **hãy để trống**. Nhập thông tin sai sẽ ngăn kết nối đến kho lưu trữ.



![capture](assets/fr/22.webp)



##### Metapets



Nếu quyền truy cập mạng chưa được cấu hình, bạn sẽ cần phải **cấu hình thêm** khi được nhắc.



Nếu bạn đang sử dụng hình ảnh **Trực tiếp**, bước tiếp theo sẽ không được hiển thị.



Sau đó, bạn có thể chọn [metapackages](https://www.kali.org/docs/general-use/metapackages/) bạn muốn cài đặt. Các tùy chọn mặc định sẽ cài đặt hệ thống Kali Linux tiêu chuẩn, vì vậy bạn không cần phải sửa đổi bất cứ điều gì.



![capture](assets/fr/23.webp)



#### Thông tin khởi nghiệp



Sau đó xác nhận cài đặt trình nạp khởi động GRUB.



![capture](assets/fr/24.webp)



##### Khởi động lại



Cuối cùng, nhấp vào Tiếp tục để khởi động lại cài đặt Kali Linux mới của bạn.



![capture](assets/fr/25.webp)



#### 4.3 Cập nhật và cấu hình Kali Linux sau khi cài đặt



Cập nhật hệ thống là một bước quan trọng sau khi cài đặt mới. Bạn có hai lựa chọn:



##### Tùy chọn 1: Thông qua giao diện người dùng đồ họa (GUI)



Kali, giống như Debian/Ubuntu, cung cấp trình quản lý cập nhật đồ họa tích hợp.



1. Nhấp vào **menu chính** (phía trên bên trái hoặc phía dưới tùy thuộc vào màn hình của bạn).


2. Mở **"Trình cập nhật phần mềm"**.


3. Công cụ sẽ:




    - Kiểm tra các gói cần cập nhật.
    - Bạn sẽ thấy một danh sách (có kích thước và phiên bản).
    - Cho phép bạn khởi chạy bản cập nhật chỉ bằng một cú nhấp chuột.


4. Nhập mật khẩu quản trị viên (`sudo`) khi được yêu cầu.


5. Để cài đặt và khởi động lại nếu cần.



##### Tùy chọn 2: Qua thiết bị đầu cuối



Mở terminal và chạy:



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Không nên sử dụng tài khoản **root** cho công việc hàng ngày; thay vào đó, hãy tạo một người dùng không phải root.



Trong terminal, hãy nhập các lệnh sau:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Đăng xuất và đăng nhập lại bằng người dùng mới.



Chúng ta hãy tóm tắt một số tác vụ cơ bản của Kali Linux trong một bảng.



### Các tác vụ cơ bản trong Kali Linux




| **Danh mục** | **Nhiệm vụ cơ bản** | **Mô tả / Mục tiêu** | **Phương pháp chính** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Điều hướng hệ thống** | Mở terminal | Truy cập vào dòng lệnh chính của Kali | Nhấp vào biểu tượng terminal hoặc sử dụng `Ctrl + Alt + T` |
| | Duyệt các thư mục | Di chuyển trong cấu trúc thư mục hệ thống | `cd /duong/dan/thu/muc`, `ls` để liệt kê các tệp |
| | Tạo / xóa thư mục | Tổ chức các tệp | `mkdir ten_thu_muc`, `rm -r ten_thu_muc` |
| **Quản lý tệp** | Sao chép / di chuyển tệp | Thao tác với các tệp trong terminal | `cp tep dich`, `mv tep dich` |
| | Xóa tệp | Giải phóng dung lượng ổ đĩa | `rm ten_tep` |
| | Hiển thị nội dung tệp văn bản | Đọc nhanh một tệp | `cat tep.txt`, `less tep.txt` |
| **Quản lý hệ thống** | Cập nhật Kali Linux | Cài đặt các phiên bản mới nhất và bản vá bảo mật | `sudo apt update && sudo apt full-upgrade -y` |
| | Cài đặt phần mềm | Thêm một công cụ hoặc tiện ích mới | `sudo apt install ten_goi` |
| | Xóa phần mềm | Làm sạch hệ thống | `sudo apt remove ten_goi` |
| | Dọn dẹp các phụ thuộc không cần thiết | Tiết kiệm dung lượng ổ đĩa | `sudo apt autoremove` |
| **Mạng và Internet** | Kiểm tra kết nối mạng | Kiểm tra quyền truy cập Internet | `ping google.com` |
| | Xác định địa chỉ IP | Biết cấu hình mạng của mình | `ip a` hoặc `ifconfig` |
| | Thay đổi mạng Wi-Fi | Kết nối với một điểm truy cập khác | Biểu tượng mạng → Chọn Wi-Fi mong muốn |
| **Tài khoản và quyền hạn** | Thực thi lệnh quản trị | Tạm thời lấy quyền root | `sudo lenh` |
| | Tạo người dùng mới | Thêm một tài khoản cục bộ | `sudo adduser ten_nguoi_dung` |
| | Thay đổi mật khẩu | Bảo mật tài khoản | `passwd` |
| **Giao diện và tiện nghi** | Thay đổi hình nền | Cá nhân hóa màn hình nền | Nhấp chuột phải vào màn hình nền → **Cài đặt màn hình nền** |
| | Thay đổi chủ đề / biểu tượng | Cải thiện khả năng đọc và thẩm mỹ | Cài đặt → Giao diện / Chủ đề |
| **Công cụ Kali** | Mở menu công cụ | Khám phá các công cụ kiểm tra và bảo mật | Menu **Ứng dụng → Kali Linux** |
| | Khởi chạy công cụ (vd: nmap, wireshark) | Khám phá thực tế các tiện ích bảo mật | `sudo nmap`, `wireshark`, v.v. |
| **Trợ giúp và tài liệu** | Nhận trợ giúp về một lệnh | Hiểu một lệnh trước khi sử dụng | `man lenh` hoặc `lenh --help` |

## Phần kết luận



Cài đặt Kali Linux chỉ là bước đầu tiên để khám phá môi trường mạnh mẽ dành riêng cho an ninh mạng này. Bằng cách thành thạo các tác vụ cơ bản và quản lý hệ thống, mọi người có thể bắt đầu khám phá các công cụ tích hợp và hiểu rõ hoạt động bên trong của một hệ thống Linux. Kali cung cấp một nền tảng học tập tuyệt vời, vừa củng cố kỹ năng kỹ thuật vừa phát triển văn hóa bảo mật CNTT đích thực.