---
name: Picocrypt
description: Một công cụ mã nguồn mở để mã hóa dữ liệu của bạn
---
![cover](assets/cover.webp)



___



*Hướng dẫn này dựa trên nội dung gốc của Florian BURNEL được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Nội dung gốc đã được chỉnh sửa.*



___



## I. Trình bày



Trong hướng dẫn này, chúng ta sẽ tìm hiểu về Picocrypt, một phần mềm mã hóa đơn giản, nhẹ và hiệu quả để mã hóa dữ liệu với mức độ bảo mật cao.



Phù hợp để **mã hóa tệp**, bạn có thể sử dụng nó để bảo vệ **dữ liệu trên máy tính, trên ổ USB**, cũng như dữ liệu được lưu trữ trên Đám mây. Ví dụ: bạn có thể mã hóa dữ liệu và lưu trữ trên **Microsoft OneDrive, Google Drive, iCloud hoặc Dropbox**, mặc dù tôi thích một phần mềm khác hơn, sẽ được giới thiệu trong một bài viết sau.



Bạn cũng có thể sử dụng nó khi cần **chia sẻ dữ liệu với bên thứ ba**: nhờ Picocrypt và khóa giải mã, họ sẽ có thể giải mã dữ liệu trên máy của họ. Vì vậy, nếu tài khoản hoặc máy tính của bạn bị xâm phạm, dữ liệu của bạn vẫn được bảo vệ.



Để theo dõi dự án Picocrypt, chỉ có một Address:





- [Picocrypt trên GitHub](https://github.com/Picocrypt/Picocrypt)



PicoCrypt hoàn toàn **miễn phí và mã nguồn mở**, có sẵn cho **Windows,** **Linux** và **macOS**. Trên Windows, bạn có thể cài đặt trên máy tính của mình hoặc sử dụng phiên bản di động.



## II. Picocrypt, phần mềm mã hóa nguồn mở



Phần mềm mã hóa Picocrypt** tự giới thiệu là **một lựa chọn thay thế** cho các giải pháp nổi tiếng khác như **VeraCrypt** và **Cryptomator** (*được thiết kế để mã hóa dữ liệu trên môi trường đám mây*), hoặc **AxCrypt**. Nhân tiện, trên GitHub chính thức của Picocrypt, bạn có thể tìm thấy bảng so sánh với một số đối thủ cạnh tranh:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Nguồn: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt **rất nhẹ**, chỉ nặng **3 MB**, và không cần cài đặt: đây là một **ứng dụng di động** với ưu điểm là không yêu cầu quyền quản trị viên! Tuy nhiên, nó không hề bỏ qua tính bảo mật, vì nó dựa trên **các thuật toán mạnh mẽ và đáng tin cậy**:





- Thuật toán mã hóa XChaCha20**
- Chức năng bỏ qua phím **Argon2**



Ngoài những ưu điểm vừa nêu, điều thực sự hấp dẫn là **tính dễ sử dụng**!



Nó chỉ cần một thứ: **kiểm tra mã**, nhưng việc này đã được lên kế hoạch, như bạn có thể thấy từ bảng so sánh ở trên (dòng cuối). Nhưng vì nó là mã nguồn mở, nên không có gì ngăn cản bạn xem qua mã nguồn của nó.



Mặc dù được so sánh với BitLocker trong bảng trên, **theo tôi thì BitLocker và Picocrypt được thiết kế cho những mục đích sử dụng khác nhau**: BitLocker để mã hóa toàn bộ ổ đĩa (ví dụ như ổ đĩa Windows) và Picocrypt để mã hóa cấu trúc cây hoặc không gian lưu trữ kiểu "Ổ đĩa".



## III. Sử dụng Picocrypt



Trong phần trình diễn này, chúng tôi sẽ sử dụng máy tính chạy Windows 11.



### A. Mã hóa dữ liệu bằng Picocrypt



Trước hết, bạn cần tải xuống Picocrypt.exe từ GitHub chính thức ([xem trang này](https://github.com/Picocrypt/Picocrypt/releases)).



Mở ứng dụng để hiển thị Interface tối giản trên màn hình. Để mã hóa dữ liệu, dù là **một tệp, nhiều tệp hay một thư mục**, chỉ cần **kéo và thả tệp vào Interface** của Picocrypt. Thao tác này sẽ chọn dữ liệu cần mã hóa.



![Image](assets/fr/020.webp)



Sau đó, để mã hóa dữ liệu, bạn có thể sử dụng một số tùy chọn, bao gồm cả khóa mã hóa. Khóa mã hóa có thể là **mật khẩu mạnh** hoặc **khóa mã hóa dưới dạng tệp khóa**, hoặc **cả hai**. Nếu lấy ví dụ về mật khẩu, bạn có thể chọn giữa việc tự tạo mật khẩu hoặc tạo mật khẩu bằng Picocrypt.



Mật khẩu này phải mạnh vì nó có thể được sử dụng để giải mã dữ liệu. Nhập mật khẩu vào mục "**Mật khẩu**" và "**Xác nhận mật khẩu**", sau đó nhấp vào "**Mã hóa**" để mã hóa dữ liệu! Trước đó, bạn có thể nhấp vào nút "**Thay đổi**" bên cạnh "**Lưu đầu ra thành**" để chỉ định thư mục đầu ra.



**Lưu ý**: Để sử dụng khóa ở định dạng tệp, hãy nhấp vào "**Tạo**" ở bên phải "**Tệp khóa**" để tạo khóa. Sau đó, chọn khóa bằng cách nhấp vào "**Chỉnh sửa**" và kéo thả tệp khóa vào vùng thích hợp.



![Image](assets/fr/019.webp)



Hai tệp đã chọn được **mã hóa và nhóm lại với nhau** trong tệp "**Encrypted.zip.pcv**", vì **PCV** là phần mở rộng được Picocrypt sử dụng. Tệp ZIP này không thể đọc được do đã được mã hóa. Để ngăn các tệp đã chọn bị nhóm lại thành một tệp ZIP được mã hóa duy nhất, bạn cần chọn tùy chọn "**Recursively**" (Đệ quy) để số lượng tệp được mã hóa bằng với số lượng tệp cần mã hóa.



Để truy cập dữ liệu, chúng ta cần giải mã dữ liệu bằng Picocrypt.



![Image](assets/fr/023.webp)



Trước khi nói về giải mã dữ liệu, sau đây là một số thông tin về một số tùy chọn có sẵn:





- Chế độ Paranoid**: sử dụng mức bảo mật cao nhất do Picocrypt cung cấp. Công cụ này sẽ sử dụng một số thuật toán mã hóa xếp tầng (XChaCha20 và Serpent) và HMAC-SHA3 thay vì BLAKE2b để xác thực dữ liệu.
- Reed-Solomon**: triển khai mã sửa lỗi *Reed-Solomon* để hỗ trợ sửa lỗi dữ liệu bị hỏng. Điều này cho phép bạn hỗ trợ mức độ hỏng khoảng 3% tệp của mình.
- Chia thành nhiều phần** hoặc **chia thành nhiều phần**: nếu bạn đang mã hóa một tệp lớn, bạn có thể yêu cầu Picocrypt chia tệp thành nhiều phần. Điều này có thể giúp việc truyền tệp dễ dàng hơn.
- Nén tệp** hoặc **Nén tệp**: nén tệp để giảm kích thước của tệp được mã hóa.
- Các tệp đã xóa** hoặc **Fichiers supprimés**: xóa các tệp nguồn để chỉ giữ lại phiên bản được mã hóa



### B. Giải mã dữ liệu bằng Picocrypt



Nếu bạn cần giải mã dữ liệu, việc này cũng không phức tạp hơn việc mã hóa nó. Chỉ cần mở Picocrypt và **kéo thả tệp PCV cần giải mã**. Sau đó, nhập mật khẩu và/hoặc chọn tệp khóa trước khi nhấp vào "**Giải mã**".



![Image](assets/fr/021.webp)



Phiên bản không được mã hóa của tệp ZIP "Encrypted.zip" hiện cho phép tôi khôi phục hai tệp của mình ở dạng văn bản thuần túy!



![Image](assets/fr/022.webp)



## IV. Kết luận



**Bạn đã được cảnh báo: Picocrypt rất dễ sử dụng và hiệu quả! Mặc dù Interface có thiết kế tối giản, nhưng nó tích hợp một số tùy chọn rất hữu ích để tùy chỉnh mã hóa! Và vì nó có phiên bản di động, bạn có thể mang theo bên mình mọi lúc mọi nơi để giải mã dữ liệu một cách an toàn**



Hãy đảm bảo sử dụng mật khẩu mạnh để bảo vệ dữ liệu, và nếu bạn sử dụng tệp khóa, hãy nhớ sao lưu tệp đó, nếu không bạn sẽ không thể giải mã vùng chứa PCV do Picocrypt tạo ra nữa. Cuối cùng, bạn nên biết rằng cũng có [phiên bản CLI](https://github.com/Picocrypt/CLI) (với ít tính năng hơn) cho phép bạn chạy Picocrypt từ dòng lệnh: một lần nữa, Picocrypt mở ra cánh cửa cho những khả năng mới.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5