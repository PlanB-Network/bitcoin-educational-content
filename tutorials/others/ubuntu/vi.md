---
name: Ubuntu
description: Hướng dẫn đầy đủ về cài đặt và sử dụng Ubuntu thay thế cho Windows
---
![cover](assets/cover.webp)

## Giới thiệu

Hệ điều hành (OS) là phần mềm chính quản lý mọi tài nguyên của máy tính. Việc lựa chọn một hệ điều hành thay thế như Ubuntu có thể mang lại nhiều lợi thế về mặt bảo mật, chi phí và quyền riêng tư.

### Tại sao lại là Ubuntu?


- Bảo mật nâng cao**: Các bản phân phối Linux nổi tiếng về tính bảo mật và mạnh mẽ
- Không mất phí**: Ubuntu và hầu hết các bản phân phối Linux đều miễn phí
- Cộng đồng lớn**: Một cộng đồng người dùng sẵn sàng trợ giúp thông qua diễn đàn và hướng dẫn
- Tôn trọng quyền riêng tư**: Hệ thống nguồn mở mang lại tính minh bạch hơn
- Đơn giản**: Giao diện thân thiện với người dùng và dễ sử dụng
- Hệ sinh thái phong phú**: Danh mục phần mềm nguồn mở rộng lớn
- Hỗ trợ thường xuyên**: Cập nhật an toàn từ Canonical

## Cài đặt và cấu hình

### 1. Điều kiện tiên quyết

**Thiết bị cần thiết:**


- Một ổ USB có dung lượng ít nhất là 12 GB
- Một máy tính có ít nhất 25 GB dung lượng trống

### 2. Tải xuống


- Truy cập [ubuntu.com/download](https://ubuntu.com/download)
- Chọn phiên bản ổn định (khuyến nghị LTS)
- Tải xuống hình ảnh ISO

![Page de téléchargement Ubuntu](assets/fr/01.webp)

![Sélection de la version Ubuntu](assets/fr/02.webp)

### 3. Tạo khóa USB có thể khởi động

Bạn có thể sử dụng một số công cụ như Balena Etcher:


- Tải xuống và cài đặt [Balena Etcher](https://etcher.balena.io/)

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)


- Mở Balena Etcher, sau đó chọn ảnh ISO Ubuntu
- Chọn khóa USB làm phương tiện đích
- Nhấp vào Flash và đợi quá trình hoàn tất

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4. Cài đặt và bảo mật Ubuntu

**4.1 Khởi động từ thẻ nhớ USB** (bằng tiếng Pháp)


- Tắt máy tính
- Cắm ổ USB (chứa Ubuntu)
- Bật máy tính của bạn. Trên các máy tính gần đây, hệ thống sẽ tự động nhận dạng khóa khởi động USB. Nếu không phải vậy, hãy khởi động lại bằng cách giữ phím truy cập BIOS/UEFI (thường là F2, F12 hoặc Delete, tùy thuộc vào thương hiệu)
 - Trong menu BIOS/UEFI, hãy chọn ổ USB của bạn làm thiết bị khởi động
 - Lưu và khởi động lại

**4.2 Khởi chạy cài đặt** (bằng tiếng Pháp)

**Màn hình khởi động**

Khi khởi động từ ổ USB, bạn sẽ thấy màn hình này cho phép bạn khởi động Ubuntu.

![Écran de démarrage Ubuntu](assets/fr/06.webp)

**Lựa chọn ngôn ngữ

Chọn ngôn ngữ bạn muốn cài đặt và hệ thống.

![Sélection de la langue](assets/fr/07.webp)

**Tùy chọn trợ năng

Cấu hình các tùy chọn trợ năng nếu cần (trình đọc màn hình, độ tương phản cao, v.v.).

![Options d'accessibilité](assets/fr/08.webp)

**Cấu hình bàn phím

Chọn bố cục bàn phím của bạn. Có một trường kiểm tra để kiểm tra xem các phím có tương ứng với cấu hình của bạn không.

![Configuration du clavier](assets/fr/09.webp)

**Kết nối mạng**

Kết nối với mạng Wi-Fi hoặc mạng có dây để tải xuống các bản cập nhật trong quá trình cài đặt.

![Configuration réseau](assets/fr/10.webp)

**Loại cài đặt

Chọn giữa "Dùng thử Ubuntu" (để kiểm tra mà không cần cài đặt) hoặc "Cài đặt Ubuntu".

![Choix du type d'installation](assets/fr/11.webp)

**Phương pháp cài đặt

Chọn cài đặt tương tác.

![Mode d'installation](assets/fr/12.webp)

**Lựa chọn ứng dụng

Chọn giữa cài đặt mặc định hoặc lựa chọn ứng dụng mở rộng.

![Sélection des applications](assets/fr/13.webp)

**Ứng dụng của bên thứ ba

Quyết định có nên cài đặt thêm trình điều khiển và phần mềm độc quyền hay không.

![Installation applications tierces](assets/fr/14.webp)

**Loại phân vùng

Bạn có hai lựa chọn chính:


- "Xóa đĩa và cài đặt Ubuntu": sử dụng toàn bộ đĩa cho Ubuntu
- "Cài đặt thủ công: tạo khởi động kép với Windows hoặc tùy chỉnh phân vùng của bạn

![Choix du partitionnement](assets/fr/15.webp)

**Tạo tài khoản người dùng

Đặt tên người dùng và mật khẩu cho tài khoản Ubuntu của bạn.

![Création du compte](assets/fr/16.webp)

**Múi giờ

Chọn khu vực địa lý của bạn để thiết lập thời gian hệ thống.

![Sélection du fuseau horaire](assets/fr/17.webp)

**Tóm tắt cài đặt**

Kiểm tra tất cả các lựa chọn của bạn trước khi bắt đầu cài đặt cuối cùng. Khi bạn nhấp vào "Cài đặt", quá trình sẽ bắt đầu.

![Résumé de l'installation](assets/fr/18.webp)

**4.3 Nâng cấp Ubuntu sau khi cài đặt** (bằng tiếng Pháp)

Cập nhật hệ thống của bạn là một bước quan trọng sau khi cài đặt mới. Bạn có hai lựa chọn:

**Lựa chọn 1: Thông qua giao diện người dùng đồ họa**


- Tìm kiếm "Phần mềm và cập nhật" trong menu ứng dụng
- Ứng dụng sẽ tự động kiểm tra các bản cập nhật có sẵn
- Làm theo hướng dẫn trên màn hình để cài đặt bản cập nhật

**Lựa chọn 2: Qua Terminal


- Mở Terminal (Ctrl + Alt + T)
- Nhập lệnh sau để kiểm tra các bản cập nhật có sẵn:

```bash
sudo apt update
```


- Nhập mật khẩu của bạn khi được nhắc
- Để cài đặt bản cập nhật, hãy nhập:

```bash
sudo apt upgrade
```


- Xác nhận cài đặt bằng cách nhập 'Y' rồi Enter

### 5. Khám phá các nhiệm vụ cơ bản

**5.1 Duyệt Internet

Theo mặc định, bạn thường sẽ thấy Firefox ở thanh khởi chạy.

Khởi chạy Firefox và bắt đầu duyệt.

Các trình duyệt khác (Chrome, Brave, v.v.) có thể được cài đặt thông qua Trình quản lý phần mềm hoặc thông qua các gói .deb.

**5.2 Xử lý văn bản

Ubuntu đi kèm với bộ phần mềm LibreOffice (Trình soạn thảo văn bản).

Để mở: Hoạt động > Tìm kiếm "LibreOffice Writer" hoặc nhấp vào biểu tượng nếu nó xuất hiện trên thanh.

Bạn có thể tạo, chỉnh sửa và lưu tài liệu ở nhiều định dạng khác nhau (bao gồm .docx).

**5.3 Cài đặt ứng dụng

Trình quản lý phần mềm (gọi là "Phần mềm Ubuntu"): giao diện đồ họa để tìm kiếm và cài đặt ứng dụng.

Từ Terminal, sử dụng lệnh:

```bash
sudo apt install nom-du-paquet
```

Ví dụ:

```bash
sudo apt install vlc
```

### 6. Kết luận và các nguồn tài nguyên bổ sung

Bây giờ bạn đã sẵn sàng sử dụng Ubuntu hàng ngày: bảo mật hệ thống, duyệt web, làm việc văn phòng, cài đặt phần mềm và cập nhật hệ điều hành!

Để nâng cao hơn nữa tính bảo mật cho cuộc sống số của bạn, chúng tôi khuyên bạn nên xem qua dịch vụ nhắn tin được mã hóa của chúng tôi, dịch vụ này hoàn toàn phù hợp để bảo vệ quyền riêng tư của bạn và bổ sung cho cài đặt Ubuntu của bạn:

https://planb.network/tutorials/others/proton-mail
